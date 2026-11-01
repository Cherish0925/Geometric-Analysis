---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: math_0007122.pdf
converter: mathpix
format: mmd
---

\title{
A SPLITTING THEOREM FOR KÄHLER MANIFOLDS WHOSE RICCI TENSORS HAVE CONSTANT EIGENVALUES
}

\author{
VESTISLAV APOSTOLOV, TEDI DRĂGHICI AND ANDREI MOROIANU
}

\begin{abstract}
It is proved that a compact Kähler manifold whose Ricci tensor has two distinct constant non-negative eigenvalues is locally the product of two Kähler-Einstein manifolds. A stronger result is established for the case of Kähler surfaces. Without the compactness assumption, irreducible Kähler manifolds with Ricci tensor having two distinct constant eigenvalues are shown to exist in various situations: there are homogeneous examples of any complex dimension $n \geq 2$ with one eigenvalue negative and the other one positive or zero; there are homogeneous examples of any complex dimension $n \geq 3$ with two negative eigenvalues; there are non-homogeneous examples of complex dimension 2 with one of the eigenvalues zero. The problem of existence of Kähler metrics whose Ricci tensor has two distinct constant eigenvalues is related to the celebrated (still open) conjecture of Goldberg [24]. Consequently, the irreducible homogeneous examples with negative eigenvalues give rise to complete Einstein strictly almost Kähler metrics of any even real dimension greater than 4.
\end{abstract}

2000 Mathematics Subject Classification. Primary 53B20, 53C25

\section*{1. Introduction}

In this note we consider compact Kähler manifolds $(M, g, J)$ whose Ricci tensor, Ric, (or rather the symmetric endomorphism corresponding to Ric via the metric) has two distinct constant eigenvalues. Since for Kähler manifolds the Ricci tensor is invariant under the action of $J$ (i.e. it satisfies $\operatorname{Ric}(J \cdot, J \cdot)=\operatorname{Ric}(\cdot, \cdot)$ ), each eigenvalue is of even multiplicity.

One source of motivation for studying such manifolds comes from a conjecture of Lichnerowicz concerning compact Kähler spin manifolds with least possible (compared to the scalar curvature) eigenvalue of the Dirac operator. It was shown by Kirchberg in 1990 that every eigenvalue $\nu$ of the Dirac operator on a compact Kähler spin manifold $M$ of even complex dimension $n$ satisfies
$$\nu^{2} \geq \frac{n}{4(n-1)} \inf _{M} s,$$
where $s$ denotes the scalar curvature of $M$. The limiting case of this inequality is characterized by the existence of spinor fields satisfying a certain first order differential equation, and it was conjectured by Lichnerowicz that the Ricci tensor of such manifolds has to be parallel. In 1997, it was shown in [33] that the Ricci tensor of every limiting manifold for the above inequality has two constant eigenvalues, one positive with multiplicity $2 n-2$ and one zero with multiplicity 2; after some more work, the conjecture was proved in [34] using Spin ${ }^{c}$ geometry.

\footnotetext{
The first two authors were supported in part by NSF grant INT-9903302.
}

Nevertheless, the general question whether the Ricci tensor of a compact Kähler manifold has to be parallel as soon as it has two non-negative constant eigenvalues was left open in [34]. A positive answer to this question is summarized in the following splitting theorem.

Theorem 1. Let $(M, g, J)$ be a compact Kähler manifold whose Ricci tensor has two distinct constant non-negative eigenvalues $\lambda$ and $\mu$. Then the universal cover of $(M, g, J)$ is the product of two simply connected Kähler-Einstein manifolds of scalar curvatures $\lambda$ and $\mu$, respectively.

Note that local irreducible examples of Kähler manifolds with eigenvalues of the Ricci tensor equal to 0 and 1 are known to exist in complex dimension two, cf. [13] and [2, Remark 1(c)]. Note also that the above result fails if one allows the Ricci tensor to have more than two different eigenvalues, as shown by the compact homogeneous Kähler manifolds (the generalized complex flag manifolds).

We also mention that Kähler manifolds with Ricci tensors having constant eigenvalues are related to different generalizations of Calabi's construction of Kähler metrics with constant scalar curvature [21]; in this vein R. Bielawski recently proved [10] that the total space of the canonical bundle of a Kähler manifold with Ricci tensor having constant eigenvalues carries a Ricci-flat Kähler metric. Interesting new examples actually appear when the underlying manifold is irreducible and non-homogeneous; the completeness of the Ricci-flat metric corresponds to the case when the underlying manifold is compact and the Ricci tensor has positive constant eigenvalues.

Another motivation for our study came from an a priori unexpected link with a conjecture of Goldberg [24], which states that any compact Einstein almost Kähler manifold is, in fact, Kähler-Einstein. This link is presented in the first part of the Section 2, while preparing the ground for the proof of Theorem 1. For any Kähler manifold $(M, g, J)$ with Ricci tensor having two distinct constant eigenvalues, one can define another $g$-orthogonal almost complex structure $\bar{J}$, by changing the sign of $J$ on one of the eigenspaces of Ric. The new almost complex structure $\bar{J}$, which is not integrable in general, commutes with $J$ and has a closed fundamental 2-form, i.e. $(g, \bar{J})$ gives rise to an almost Kähler structure on the manifold. The integrability of $\bar{J}$ holds precisely when the Ricci tensor of $g$ is parallel, or equivalently, when $g$ is locally a product of two Kähler-Einstein metrics; see Lemma 1. Moreover, any Kähler structure $(g, J)$ with Ricci tensor having two distinct constant eigenvalues either both positive, or both negative, determines (and is determined by) a certain Einstein almost Kähler structure $(\widetilde{g}, \bar{J})$, see Corollary 1.

The proof of Theorem 1 is completed in Section 2. We show the integrability of the almost Kähler structure $(g, \bar{J})$ using essentially an integral formula found by Sekigawa in [42], where he gave an affirmative answer to the Goldberg conjecture in the case of non-negative scalar curvature. However, in our situation a more detailed analysis is required to extract the conclusion, which we accomplish by making use of some Weitzenböck formulae elaborated in [12].

In Section 3 we consider the homogeneous Kähler manifolds, as an important class of Kähler manifolds whose Ricci tensors have constant eigenvalues. Theorem 1 implies the splitting of any compact homogeneous Kähler manifold with Ricci tensor having two distinct positive eigenvalues (see Corollary 3); the splitting in
the case when one of the eigenvalues is zero and the other one is positive was already known from classical results [14, 35].

On the other hand, according to the structure theorem for homogeneous Kähler manifolds [48, 18], there are lots of irreducible examples with Ricci tensor having eigenvalues (-1, +1), or (-1, 0).

We finally exhibit irreducible (non-compact) homogeneous Kähler manifolds of any complex dimension $n \geq 3$ whose Ricci tensors have two distinct eigenvalues, both negative and constant. Our construction relies on an appropriate realization of a bounded homogeneous domain as a Siegel domain of type II; the metric is then invariant under the simply transitive action of a solvable group of affine transformations of the relevant Siegel domain. By virtue of Corollary 1, any such homogeneous metric can be deformed to a Kähler-Einstein one, which also admits a strictly almost Kähler structure. (Here and henceforth, strictly almost Kähler structure means that the corresponding almost complex structure is not integrable). We thus provide irreducible complete Einstein strictly almost Kähler manifolds of any even dimension greater than four. (The previously known such examples were constructed by D. Alekseevsky on certain solvable Lie groups of high dimensions, see e.g. [9, pp. 419-421 \& Rem. 14.100]). Even more surprising is the fact that some non-compact Hermitian symmetric spaces admit a strictly almost Kähler structure commuting with the standard Hermitian structure (Corollary 4). Particular examples (filling all real dimensions $2 n, n \geq 3$ ) are the Hermitian symmetric spaces $M^{2 n}=\mathrm{SO}(2, n) /(\mathrm{SO}(2) \times \mathrm{SO}(n)), n \geq 3$; see Example 1. By contrast, J. Armstrong [5] showed that the (unique) irreducible non-compact Hermitian symmetric space of complex dimension 2, the complex hyperbolic space, does not admit (even locally) strictly almost Kähler structures commuting with the standard Kähler structure. Note that symmetric spaces of compact type of any dimension do not (locally) carry orthogonal strictly almost Kähler structures, cf. [22], [20] (see also Remark 2 below); it is also known from [5, 37, 38] that real hyperbolic spaces do not (locally) admit orthogonal strictly almost Kähler structures either.

In the last part of the paper, we provide a stronger version of Theorem 1 for the case of compact Kähler manifolds of complex dimension 2.

Theorem 2. Let $(M, g, J)$ be a compact Kähler surface whose Ricci tensor has two distinct constant eigenvalues. Then one of the following alternatives holds :
\begin{itemize}
\item[(i)] $(M, g, J)$ is locally symmetric, i.e. locally is the product of Riemann surfaces of distinct constant Gauss curvatures;
\item[(ii)] if $(M, g, J)$ is not as described in (i), then the eigenvalues of the Ricci tensor are both negative and $(M, J)$ must be a minimal surface of general type with ample canonical bundle and with even and positive signature. Moreover, in this case, reversing the orientation, the manifold would admit an Einstein, strictly almost Kähler metric.
\end{itemize}

The additional ingredients for the proof of Theorem 2 come from the classification results of Kähler surfaces and from consequences of the Seiberg-Witten theory, see [28, 31, 39]. At this time, we do not know if the alternative (ii) may really hold. As pointed out, if it does, it also provides a counter-example to the 4-dimensional Goldberg conjecture.

Let us also note here that the compactness assumption in Theorem 2 is essential: Complete (non-compact) examples are the non-symmetric homogeneous

Kähler surfaces with Ricci tensor having eigenvalues (-1, +1) or (-1, 0), see respectively [44] and [29]. The case of eigenvalues (-1, 0) corresponds to the unique proper 3-symmetric space in four dimensions, also viewed as the non-compact Kähler geometry $\mathbf{F}^{4}$ of [49]. Moreover, the constructions of [13] and [2] give further local examples of non-homogeneous Kähler surfaces with Ricci tensor of constant eigenvalues; in all these examples one of the two eigenvalues of Ric is non-negative, therefore, by Theorem 2, none of them can be compactified.

\section*{2. Proof of Theorem 1}
2.1. The commuting almost Kähler structure. The main idea of the proof of our results is to construct an almost Kähler structure $\bar{J}$ on $(M, g, J)$, which is compatible with $g$ and commutes with $J$.

Lemma 1. Let ( $M, g, J)$ be a Kähler manifold whose Ricci tensor has constant eigenvalues $\lambda<\mu$. Denote by $E_{\lambda}$ and $E_{\mu}$ the corresponding $J$-invariant eigenspaces and define a $g$-orthogonal almost complex structure $\bar{J}$ by setting $\bar{J}_{\mid E_{\lambda}}=J_{\mid E_{\lambda}} ; \bar{J}_{\mid E_{\mu}}=$ $-J_{\mid E_{\mu}}$. Then $J$ and $\bar{J}$ mutually commute and $(g, \bar{J})$ is an almost Kähler structure, i.e. the fundamental form $\bar{\Omega}(\cdot, \cdot)=g(\bar{J} \cdot, \cdot)$ is symplectic. Moreover, $(g, \bar{J})$ is Kähler (i.e. $\bar{J}$ is integrable) if and only if $(M, g)$ is locally product of two Kähler-Einstein manifolds of scalar curvatures $\lambda$ and $\mu$, respectively.

Proof. Denote by $\Omega(\cdot, \cdot)=g(J \cdot, \cdot)$ the fundamental form of $(g, J)$ and consider the (1,1)-forms $\alpha$ and $\beta$ defined by
$$\begin{gathered}
\alpha(X, Y)=\Omega\left(\operatorname{pr}^{\lambda}(X), \operatorname{pr}^{\lambda}(Y)\right), \forall X, Y \in T M ; \\
\beta=\Omega-\alpha,
\end{gathered}$$
where $\mathrm{pr}^{\lambda}$ (resp. $\mathrm{pr}^{\mu}$ ) denotes the orthogonal projection of the tangent bundle $T M$ onto $E_{\lambda}$ (resp. $E_{\mu}$ ). The Ricci form $\rho(\cdot, \cdot)=\operatorname{Ric}(J \cdot, \cdot)$ of $(M, g, J)$ is then given by
$$\rho=\lambda \alpha+\mu \beta .$$
As $\Omega=\alpha+\beta$ and $\rho$ are both closed (1,1)-forms, so are the 2-forms $\alpha$ and $\beta$. By the very definition of $\bar{J}$, the fundamental form $\bar{\Omega}(\cdot, \cdot)=g(\bar{J} \cdot, \cdot)$ is given by
$$\bar{\Omega}=\alpha-\beta,$$
and hence is closed, i.e. $(g, \bar{J}, \bar{\Omega})$ is an almost Kähler structure; it is Kähler as soon as the Ricci tensor is parallel (equivalently, $\alpha$ and $\beta$ are parallel), i.e. when $(M, g)$ is locally a product of two Kähler-Einstein manifolds with scalar curvatures $\lambda$ and $\mu$, respectively. Q.E.D.

Remark 1. Note that the Ricci tensor of the almost Kähler structure ( $g, \bar{J}, \bar{\Omega}$ ) constructed in Lemma 1 is $\bar{J}$-invariant, i.e. is of type $(1,1)$ with respect to $\bar{J}$. In the compact case, almost Kähler structures with Ricci tensors of type $(1,1)$ are the critical points of the Hilbert functional, the integral of the scalar curvature, restricted to the set of all compatible metrics to symplectic form $\bar{\Omega}$ (cf. [11]). Compatible Kähler metrics provide absolute maxima for the functional in this setting and it was a natural question [11] to ask if every critical metric is necessarily Kähler. The answer turns out to be negative in dimension greater than four [17], while in four dimensions the problem is still open, as no examples of compact, non-Kähler, almost Kähler structures with Ricci tensor of type $(1,1)$ are known yet.

Let us consider for a moment the more general context of Kähler manifolds $(M, g, J)$ which admit a commuting almost Kähler structure $\bar{J}$. Any $g$-orthogonal almost complex structure $\bar{J}$ which commutes with and differs from $\pm J$ gives rise to a $g$-orthogonal, $J$-invariant endomorphism $Q=-J \circ \bar{J}$ of $T M$ such that $Q^{2}=\operatorname{Id}_{\left.\right|_{T M}}$; we thus define an orthogonal, $J$-invariant splitting of the tangent bundle $T M$
$$T M=E_{+} \oplus E_{-}$$
into the sum of the ±1-eigenspaces of $Q$, the (complex) sub-bundles $E_{ \pm}$, respectively. As in the proof of Lemma 1, we consider the (1,1)-forms $\alpha$ and $\beta$, the restrictions of the fundamental form $\Omega$ of $(g, J)$ to the spaces $E_{+}$and $E_{-}$, respectively. The fundamental forms $\Omega$ and $\bar{\Omega}$ of $(g, J)$ and $(g, \bar{J})$ are then given by
$$\Omega=\alpha+\beta ; \quad \bar{\Omega}=\alpha-\beta,$$
proving that $\alpha$ and $\beta$ are closed. Therefore, corresponding to any Kähler metric $(g, J)$ admitting a commuting almost Kähler structure $\bar{J}$, we may consider a natural 1 -parameter family $g^{t}$ of metrics having the same property (see [34]):
$$g^{t}=g_{\left.\right|_{E_{+}}}+t g_{\left.\right|_{E_{-}}}, \quad t>0,$$
where $g_{\left.\right|_{E_{+}}}$(resp. $g_{\left.\right|_{E_{-}}}$) denotes the restriction of $g$ to the eigenspaces $E_{+}$(resp. to $E_{-}$).

Lemma 2. For any $t>0$, the metric $g^{t}$ is Kähler with respect to J, almost Kähler with respect to $\bar{J}$ and has the same Ricci tensor as the metric $g=g^{1}$.

Proof. The first statements follow from the fact that the fundamental form of $\left(g^{t}, J\right)$ (resp. $\left(g^{t}, \bar{J}\right)$ ) is closed as being equal to $\alpha+t \beta$ (resp. $\alpha-t \beta$ ), where $\alpha$ and $\beta$ are constructed as above with respect to $g=g^{1}$. For the last claim, note that the volume form of the metric $g^{t}$ is a constant multiple of the volume form of $g=g^{1}$, so, from the local expression in complex coordinates, the Ricci forms of the Kähler structures $\left(g^{t}, J\right)$ and $(g, J)$ coincide. Q.E.D.

As for Kähler metrics with Ricci tensor having distinct constant eigenvalues, Lemma 2 shows that one can deform any such given metric to one whose Ricci tensor has constant eigenvalues equal to -1, 0 or +1. In particular, we get

Corollary 1. On a complex manifold $\left(M^{2 n}, J\right)$ there is a one-to-one correspondence between Kähler metrics with Ricci tensor of constant eigenvalues $\lambda<\mu$ with $\lambda \mu>0$ and Kähler-Einstein metrics $\widetilde{g}$ of scalar curvature $2 n \lambda$ carrying an orthogonal almost Kähler structure $\bar{J}$ which commutes with and differs from ± J; in this correspondence $\bar{J}$ is compatible also with $g$ and coincides (up to sign) with the almost Kähler structure defined in Lemma 1; moreover, $\bar{J}$ is integrable precisely when $g$ (and $\widetilde{g}$ ) is locally product of two Kähler-Einstein metrics.

Proof. Let $(M, g, J)$ be a Kähler manifold whose Ricci tensor has constant eigenvalues $\lambda<\mu$ and $\bar{J}$ be the almost Kähler structure commuting with $J$ given by Lemma 1. It is easy to see that the ±1-eigenspaces of the endomorphism $Q=-J \circ \bar{J}$ above are given by $E_{+}=E_{\lambda}, E_{-}=E_{\mu}$, where, we recall, $E_{\lambda}$ and $E_{\mu}$ are the eigenspaces of Ric. By Lemma 2, the metric $\widetilde{g}=g^{\mu / \lambda}$ obtained via (1) is Kähler-Einstein with scalar curvature $2 n \lambda$. Conversely, starting from a Kähler-Einstein structure $(\widetilde{g}, J)$ of scalar curvature $2 n \lambda$, endowed with an almost Kähler structure $\bar{J}$ commuting with $J$, the deformation (1) provides a Kähler metric $(g, J)$ whose Ricci tensor has constant eigenvalues $\lambda<\mu$, by putting $g^{1}=\widetilde{g}$ and $g=g^{\lambda / \mu}$. The almost complex
structure $\bar{J}$ is compatible to both $g$ and $\widetilde{g}$. It is clear then that the common Ricci tensor of $g$ and $\widetilde{g}$ is $\bar{J}$-invariant, and therefore, $\bar{J}$ coincides (up to sign) with the almost complex structure defined in Lemma 1. By Lemma 1 we also conclude that the integrability of $\bar{J}$ is equivalent to $g$ (hence also $\widetilde{g}$ ) being locally a product of two Kähler-Einstein metrics. Q.E.D.
2.2. Curvature obstructions to existence of strictly almost Kähler structures. The proof of Theorem 1 will be derived by showing the integrability of the almost Kähler structure obtained in Corollary 1. To do this we first observe that existence of a strictly almost Kähler structure imposes several non-trivial relations between different $U(n)$-components of the curvature. Because the almost Kähler structure will take the center stage in what follows, we drop the bar-notation from the previous sub-section and will even forget for now that in our situation the manifold also admits a Kähler structure.

Thus, let $(M, g, J)$ be an almost Kähler manifold of (real) dimension $2 n$. We start by reviewing some necessary elements of almost Kähler geometry.

The almost complex structure $J$ gives rise to a type decomposition of complex vectors and forms, and accordingly, of any complex tensor field; by convention, $J$ acts on the cotangent bundle $T^{*} M$ by $J a(X)=a(-J X)$. We thus have a decomposition of the complexified cotangent bundle
$$T^{*} M \otimes \mathbb{C}=\Lambda^{1,0} M \oplus \Lambda^{0,1} M,$$
and of the bundle of complex 2 -forms
$$\Lambda^{2} M \otimes \mathbb{C}=\Lambda^{1,1} M \oplus \Lambda^{2,0} M \oplus \Lambda^{0,2} M .$$
A similar decomposition holds for the complex bundle $S^{2} M \otimes \mathbb{C}$ of symmetric 2-tensors. When considering real sections of $\Lambda^{2} M$ (resp. of $S^{2} M$ ), we prefer to introduce the super-scripts ' and " for denoting the projections to the real subbundles $\Lambda_{\mathbb{R}}^{1,1} M$ (resp. $S_{\mathbb{R}}^{1,1} M$ ) of $J$-invariant 2-forms (resp. symmetric 2-tensors) and to $\llbracket \Lambda^{2,0} M \rrbracket$ (resp. $\llbracket S^{2,0} M \rrbracket$ ) of $J$-anti-invariant ones (here and henceforth $\llbracket \rrbracket$ stands for the real vector bundle underlying a given complex bundle). Thus, for any section $\psi$ of $\Lambda^{2} M$ (resp. of $S^{2} M$ ) we have the splitting $\psi=\psi^{\prime}+\psi^{\prime \prime}$, where
$$\psi^{\prime}(\cdot, \cdot)=\frac{1}{2}(\psi(\cdot, \cdot)+\psi(J \cdot, J \cdot)) \text { and } \psi^{\prime \prime}(\cdot, \cdot)=\frac{1}{2}(\psi(\cdot, \cdot)-\psi(J \cdot, J \cdot)) \text {. }$$
Note that $\Lambda_{\mathbb{R}}^{1,1} M$ can be identified with $S_{\mathbb{R}}^{1,1} M$ via the complex structure $J$ : for any $\alpha \in \Lambda_{\mathbb{R}}^{1,1} M$,
$$A=(J \circ \alpha):=\alpha(J \cdot, \cdot)$$
is the corresponding section of $S_{\mathbb{R}}^{1,1} M$.
The real bundle $\llbracket \Lambda^{2,0} M \rrbracket$ (resp. $\llbracket S^{2,0} M \rrbracket$ ) inherits a canonical complex structure $J$, acting by
$$(J \psi)(X, Y):=-\psi(J X, Y), \forall \psi \in \llbracket \Lambda^{2,0} M \rrbracket .$$
(We adopt a similar definition for the action of $J$ on $\llbracket S^{2,0} M \rrbracket$ ).
It is well known that the fundamental form $\Omega(\cdot, \cdot)=g(J \cdot, \cdot)$ of an almost Kähler structure is a real harmonic 2-form of type (1, 1), i.e. satisfies:
$$\Omega(J \cdot, J \cdot)=\Omega(\cdot, \cdot), \mathrm{d} \Omega=0 \text { and } \delta \Omega=0,$$
where d and $\delta$ are the differential and co-differential operators acting on forms. Moreover, if ∇ is the Levi-Civita connection of $g$, then $\nabla \Omega$ (which is identified with the Nijenhuis tensor of $J$ ) is a section of the real vector bundle $\llbracket \Lambda^{1,0} M \otimes \Lambda^{2,0} M \rrbracket$.

We first derive several consequences from the classical Weitzenböck formula for a 2-form $\psi$ :
$$\begin{array}{r}
\Delta \psi-\nabla^{*} \nabla \psi=[\operatorname{Ric}(\Psi \cdot, \cdot)-\operatorname{Ric}(\cdot, \Psi \cdot)]-2 R(\psi) \\
=\frac{2(n-1)}{n(2 n-1)} s \psi-2 W(\psi)+\frac{(n-2)}{(n-1)}\left[\operatorname{Ric}_{0}(\Psi \cdot, \cdot)-\operatorname{Ric}_{0}(\cdot, \Psi \cdot)\right],
\end{array}$$
where: $\Delta=\mathrm{d} \delta+\delta \mathrm{d}$ denotes the Riemannian Laplace operator acting on 2-forms, $\nabla^{*}$ denotes the adjoint of ∇ with respect to $g$; Ric $_{0}=$ Ric $-\frac{s}{2 n} g$ is the traceless part of the Ricci tensor, $s=\operatorname{trace}(R i c)$ is the scalar curvature, $\Psi$ is the skew-symmetric endomorphism of $T M$ identified to $\psi$ via the metric, and $R$ and $W$ are respectively the curvature tensor and the Weyl tensor, considered as endomorphisms of $\Lambda^{2} M$ or as sections of $\Lambda^{2} M \otimes \Lambda^{2} M$, depending on the context.

Applying relation (2) to the (harmonic) fundamental form $\Omega$ of the almost Kähler structure $(g, J)$, we obtain
$$\nabla^{*} \nabla \Omega=2 R(\Omega)-[\operatorname{Ric}(J \cdot, \cdot)-\operatorname{Ric}(\cdot, J \cdot)] .$$

Note that the Ricci tensor of a Kähler structure is $J$-invariant, but this is no longer true for an arbitrary almost Kähler structure. It will be thus useful to introduce the invariant and the anti-invariant parts of the Ricci tensor with respect to the almost complex structure $J$, Ric' and Ric'', respectively. We also put
$$\rho=J \circ \text { Ric }^{\prime}$$
to be the (1,1)-form corresponding the the $J$-invariant part of Ric, which will be called Ricci form of $(M, g, J)$. For Kähler manifolds, $\rho$ is clearly equal to the image of $\Omega$ under the action of the curvature $R$, but this is not longer true for almost Kähler manifolds. In fact,
$$\rho^{*}=R(\Omega)$$
can be considered as a second (twisted) Ricci form of $(M, g, J)$ which is not, in general, $J$-invariant (see e.g. [47]). We will consequently denote by $\left(\rho^{*}\right)^{\prime}$ and $\left(\rho^{*}\right)^{\prime \prime}$ the corresponding 2-forms which are sections of the bundles $\Lambda_{\mathbb{R}}^{1,1} M$ and $\llbracket \Lambda^{2,0} M \rrbracket$, respectively. With these notations, formula (3) is a measure of the difference of the two types of Ricci forms on an almost Kähler manifold:
$$\rho^{*}-\rho=\frac{1}{2}\left(\nabla^{*} \nabla \Omega\right) .$$
Taking the inner product with $\Omega$ of the relation (4) we obtain the difference of the two types of scalar curvatures:
$$s^{*}-s=|\nabla \Omega|^{2}=\frac{1}{2}|\nabla J|^{2},$$
where, we recall $s=\operatorname{trace}($ Ric $)$ is the usual scalar curvature of $g$, and $s^{*}=$ $2\langle R(\Omega), \Omega\rangle$ is the so-called star-scalar curvature of the almost Kähler structure $(g, J)$. Here and throughout the paper, the inner product induced by the metric $g$ on various tensor bundles over the manifold will be denoted by $\rangle$, while the corresponding norm is denoted by | |; note that 〈 〉acting on 2-forms differs by a factor of 1/2 compared to when it acts on corresponding tensors or endomorphisms. In the present paper $\nabla \Omega$ is viewed as a $\Lambda^{2} M$-valued 1-form, while $\nabla J$ is considered as a section of $\left(T^{*} M\right)^{\otimes 2} \otimes T M$, etc.

Formulae (4) and (5) can be interpreted as "obstructions" to the (local) existence of a strictly almost Kähler structure $J$, compatible with a given metric $g$; see e.g.
[5]. We derived these relations by using properties of the 2-jet of $J$ (although eventually (5) depends on the 1-jet only), so that (4) and (5) can be viewed as obstructions to the lifting of the 0-jet of $J$ to the 2-jet.

Remark 2. In the vein of what was mentioned above one can easily derive local non-existence results of compatible strictly almost Kähler structures for certain Riemannian metrics: For example, if we denote by $P$ the curvature type operator acting on $\Lambda^{2} M$ by
$$P(\psi)=\frac{2(n-1)}{n(2 n-1)} s \psi-2 W(\psi),$$
then, by (2) and (5), $s-s^{*}=\langle P(\Omega), \Omega\rangle=-|\nabla \Omega|^{2} \leq 0$. This shows that Riemannian metrics for which $P$ is semi-positive definite do not admit even locally compatible strictly almost Kähler structures; the latter curvature condition is equivalent to the non-negativity of the isotropic sectional curvatures. This criterion of non-existence applies in particular to conformally flat manifolds of non-negative scalar curvature, or to the symmetric spaces of compact type; see [22, 20].

In fact, there is even a more general identity than (4), due to Gray [25], which could also be interpreted as an obstruction to the lifting of the 0-jet of $J$ to the 2-jet: Starting from the splitting
$$\Lambda^{2} M=\Lambda_{\mathbb{R}}^{1,1} M \oplus \llbracket \Lambda^{2,0} M \rrbracket,$$
we denote by $\widetilde{R}$ the component of the curvature operator acting trivially on the first factor, i.e.
$$\widetilde{R}_{X, Y, Z, T}=\frac{1}{4}\left(R_{X, Y, Z, T}-R_{J X, J Y, Z, T}-R_{X, Y, J Z, J T}+R_{J X, J Y, J Z, J T}\right) .$$
Thus, $\widetilde{R}$ can be viewed as a section of the bundle $\operatorname{End}_{\mathbb{R}}\left(\llbracket \Lambda^{2,0} M \rrbracket\right)$, which in turn decomposes further as
$$\operatorname{End}_{\mathbb{R}}\left(\llbracket \Lambda^{2,0} M \rrbracket\right)=\left(\operatorname{End}_{\mathbb{R}}\left(\llbracket \Lambda^{2,0} M \rrbracket\right)\right)^{\prime} \oplus\left(\operatorname{End}_{\mathbb{R}}\left(\llbracket \Lambda^{2,0} M \rrbracket\right)\right)^{\prime \prime},$$
into the sub-bundles of endomorphisms of $\llbracket \Lambda^{2,0} M \rrbracket$ which commute, respectively, anti-commute with the action of $J$ on $\llbracket \Lambda^{2,0} M \rrbracket$. Denoting by $\widetilde{R}^{\prime}$ and $\widetilde{R}^{\prime \prime}$ the corresponding components of $\widetilde{R}$, Gray's identity is [25]
$$\widetilde{R}^{\prime}=-\frac{1}{4} \sum\left(\nabla_{e_{j}} \Omega\right) \otimes\left(\nabla_{e_{j}} \Omega\right) .$$
As for the component $\widetilde{R}^{\prime \prime}$, from its definition we have
$$\begin{aligned}
\left(\widetilde{R}^{\prime \prime}\right)_{X, Y, Z, T}=\frac{1}{8} & \left(R_{X, Y, Z, T}-R_{J X, J Y, Z, T}-R_{X, Y, J Z, J T}+R_{J X, J Y, J Z, J T}\right. \\
& \left.+R_{X, J Y, Z, J T}+R_{J X, Y, Z, J T}+R_{X, J Y, J Z, T}+R_{J X, Y, J Z, T}\right),
\end{aligned}$$
showing that
$$\left(\widetilde{R}^{\prime \prime}\right)_{Z_{1}, Z_{2}, Z_{3}, Z_{4}}=R_{Z_{1}, Z_{2}, Z_{3}, Z_{4}}=W_{Z_{1}, Z_{2}, Z_{3}, Z_{4}} \quad \forall Z_{i} \in T^{1,0} M .$$
Thus, $\widetilde{R}^{\prime \prime}$ is actually determined by the Weyl curvature of $M$.
The next result provides a further obstruction, this time to the lift of the 3-jet of $J$ to the 4-jet (see also [1] for more detailed discussion).

Proposition 1. For any almost Kähler structure $(g, J, \Omega)$ the following relation holds:
$$\begin{aligned}
\Delta\left(s^{*}-s\right)= & -4 \delta\left(J \delta\left(J \operatorname{Ric}^{\prime \prime}\right)\right)+8 \delta\left(\left\langle\rho^{*}, \nabla \cdot \Omega\right\rangle\right)+2\left|\operatorname{Ric}^{\prime \prime}\right|^{2} \\
& -8\left|\widetilde{R}^{\prime \prime}\right|^{2}-\left|\nabla^{*} \nabla \Omega\right|^{2}-|\phi|^{2}+4\langle\rho, \phi\rangle-4\left\langle\rho, \nabla^{*} \nabla \Omega\right\rangle,
\end{aligned}$$
where the semi-positive (1,1)-form $\phi$ is given by $\phi(X, Y)=\left\langle\nabla_{J X} \Omega, \nabla_{Y} \Omega\right\rangle ; \delta$ denotes the co-differential with respect to ∇ , acting on 1-forms and 2-tensors.

Integrating (7) over the manifold, one obtains an integral formula identical to the one in [42, Proposition 3.2], up to some integration by parts. In particular we have:

Corollary 2. ([42]) For any compact almost Kähler manifold with J-invariant Ricci tensor the following inequality holds:
$$\int_{M}\left[4\langle\rho, \phi\rangle-4\left\langle\rho, \nabla^{*} \nabla \Omega\right\rangle-\left|\nabla^{*} \nabla \Omega\right|^{2}-|\phi|^{2}\right] d V_{g} \geq 0$$
where $d V_{g}=\frac{1}{n!} \Omega^{n}$ is the volume form of $g$.
Remark 3. As shown by Sekigawa, the above inequality gives an obstruction to the (global) existence of strictly almost Kähler structures, when the metric $g$ is Einstein with non-negative scalar curvature. Indeed, in this case Ric'' = 0 and $2\langle\rho, \phi\rangle=\left\langle\rho, \nabla^{*} \nabla \Omega\right\rangle=\frac{s}{2 n}|\nabla \Omega|^{2}$, so that, by (8), $\nabla \Omega=0$, i.e. $J$ is necessarily Kähler. In dimension 4, other integrability results have been derived from (7); see e.g. [19], [1], [37].
Proof of Proposition 1. We start from the identity $\frac{1}{2} s^{*}=\langle\Omega \otimes \Omega, R\rangle$, which follows from the very definition of $s^{*}$. (Note that on the bundle $\Lambda^{2} M \otimes \Lambda^{2} M$ the inner product $\rangle$ induced by $g$ differs now by a factor of $1 / 4$ from the one induced on $\left(T^{*} M\right)^{\otimes 4}$.) Applying the Laplacian to both sides of the above equality, we get
$$\begin{aligned}
\frac{1}{2} \Delta s^{*}= & \Delta\langle\Omega \otimes \Omega, R\rangle \\
= & -2 \sum\left(\nabla_{e_{i}}\left\langle\nabla_{e_{i}}(\Omega \otimes \Omega), R\right\rangle\right) \\
& -\left\langle\nabla^{*} \nabla(\Omega \otimes \Omega), R\right\rangle+\left\langle\Omega \otimes \Omega, \nabla^{*} \nabla R\right\rangle .
\end{aligned}$$
We next consider each of the terms appearing in the right-hand side of relation (9). Since $R$ is a symmetric endomorphism of $\Lambda^{2} M$, the first term gives
$$\begin{aligned}
-2 \sum\left(\nabla_{e_{i}}\left\langle\nabla_{e_{i}}(\Omega \otimes \Omega), R\right\rangle\right) & =-4 \sum\left(\nabla_{e_{i}}\left\langle R(\Omega), \nabla_{e_{i}} \Omega\right\rangle\right) \\
& =4 \delta\left(\left\langle\rho^{*}, \nabla \cdot \Omega\right\rangle\right) .
\end{aligned}$$
Using again that $R \in S^{2}\left(\Lambda^{2} M\right)$, the second term can be written as
$$-\left\langle\nabla^{*} \nabla(\Omega \otimes \Omega), R\right\rangle=2 \sum\left\langle\left(\nabla_{e_{i}} \Omega \otimes \nabla_{e_{i}} \Omega\right), R\right\rangle-2\left\langle\left(\nabla^{*} \nabla \Omega\right) \otimes \Omega, R\right\rangle .$$
Since $\sum\left(\nabla_{e_{i}} \Omega \otimes \nabla_{e_{i}} \Omega\right) \in\left(\operatorname{End}_{\mathbb{R}}\left(\llbracket \Lambda^{2,0} M \rrbracket\right)\right)^{\prime}$, Gray's relation (6) implies
$$2 \sum\left\langle\left(\nabla_{e_{i}} \Omega \otimes \nabla_{e_{i}} \Omega\right), R\right\rangle=2 \sum\left\langle\left(\nabla_{e_{i}} \Omega \otimes \nabla_{e_{i}} \Omega\right), \widetilde{R}^{\prime}\right\rangle=-|\phi|^{2} .$$
From (4), we have
$$\left(\rho^{*}\right)^{\prime \prime}=\left(\nabla^{*} \nabla \Omega\right)^{\prime \prime} \text { and }\left(\rho^{*}\right)^{\prime}-\rho=\left(\nabla^{*} \nabla \Omega\right)^{\prime} .$$

Taking these into account, we have
$$2\left\langle\left(\nabla^{*} \nabla \Omega\right) \otimes \Omega, R\right\rangle=2\left\langle\rho, \nabla^{*} \nabla \Omega\right\rangle+\left|\nabla^{*} \nabla \Omega\right|^{2} .$$
Thus from (11), (12), (13), we obtain for the second term
$$-\left\langle\nabla^{*} \nabla(\Omega \otimes \Omega), R\right\rangle=-|\phi|^{2}-\left|\nabla^{*} \nabla \Omega\right|^{2}-2\left\langle\rho, \nabla^{*} \nabla \Omega\right\rangle .$$
To compute the last term, we start by writing the Weitzenböck formula for sections of $\Lambda^{2} M \otimes \Lambda^{2} M$, applied to the curvature tensor $R$ (see [12, Proposition 4.2]):
$$\nabla^{*} \nabla R=\left(d^{\nabla} \delta^{\nabla}+\delta^{\nabla} d^{\nabla}\right) R-2 R \circ\left(\frac{1}{2} \operatorname{Ric} \oslash g-R\right)+K(\stackrel{\circ}{\mathrm{R}} \circ \stackrel{\circ}{\mathrm{R}}) .$$
The notations in the above relation follow the ones used by Bourguignon in [12], namely:
\begin{itemize}
\item[-] $d^{\nabla}$ and $\delta^{\nabla}$ are the differential and the co-differential operators defined on the bundle of $\Lambda^{2} M$-valued 2-forms using ∇;
\item[-] ( ) denotes the Kulkarni-Nomizu product which allows us to consider any symmetric tensor $S$ as an element $S \triangle g$ of $\Lambda^{2} M \otimes \Lambda^{2} M$;
\item[-] For any section $A$ of $\Lambda^{2} M \otimes \Lambda^{2} M$, $\AA$ denotes the endomorphism of $\left(T^{*} M\right)^{\otimes 2}$ defined by
$$\left(T^{*} M\right)^{\otimes 2} \ni h_{X, Y} \longmapsto(\AA(h))_{X, Y}=\sum A\left(e_{i}, X, e_{j}, Y\right) h\left(e_{i}, e_{j}\right) ;$$
\item[-] $K(\cdot)$ is 4 times the projection of $\left(T^{*} M\right)^{\otimes 4}$ onto $\Lambda^{2} M \otimes \Lambda^{2} M$.
\end{itemize}
Note that apparently there is difference compared to the formula of Proposition 4.2 in [12], namely the coefficient "2" that we have in front of the second term. That is needed because originally the formula in [12] was written for sections of $\left(T^{*} M\right)^{\otimes 2} \otimes \Lambda^{2} M$ and there is a difference of a factor of 2 in the definition there of $\hat{A} \circ \hat{B}$ compared to the composition in $\operatorname{End}\left(\Lambda^{2} M\right)$ used here.

Using (4), we obtain
$$\begin{array}{r}
-2\left\langle R \circ\left(\frac{1}{2} \operatorname{Ric} \otimes g-R\right), \Omega \otimes \Omega\right\rangle=2\left\langle\left(R-\frac{1}{2} \operatorname{Ric} \otimes g\right)(\Omega), R(\Omega)\right\rangle \\
=2\left\langle\rho^{*}, \rho^{*}-\rho\right\rangle=\left\langle\rho, \nabla^{*} \nabla \Omega\right\rangle+\frac{1}{2}\left|\nabla^{*} \nabla \Omega\right|^{2}
\end{array}$$
From the definitions of $K(\stackrel{\circ}{\mathrm{R}} \circ \stackrel{\circ}{\mathrm{R}})$ and $\widetilde{R}$, it follows
$$\begin{aligned}
\langle K(\stackrel{\circ}{\mathrm{R}} \circ \stackrel{\circ}{\mathrm{R}}), \Omega \otimes \Omega\rangle & =4\langle\widetilde{R}, J \widetilde{R} J\rangle \\
& =4\left(\left|\widetilde{R}^{\prime}\right|^{2}-\left|\widetilde{R}^{\prime \prime}\right|^{2}\right)=\frac{1}{2}|\phi|^{2}-4\left|\widetilde{R}^{\prime \prime}\right|^{2},
\end{aligned}$$
where for the last step we used Gray's relation (6).
Finally, we express the term $\left\langle\left(d^{\nabla} \delta^{\nabla}+\delta^{\nabla} d^{\nabla}\right) R, \Omega \otimes \Omega\right\rangle$. Because of the second Bianchi identity, $d^{\nabla} R=0$ and
$$\left(\delta^{\nabla} R\right)_{X}(Y, W)=\left(\nabla_{Y} \operatorname{Ric}\right)(X, W)-\left(\nabla_{W} \operatorname{Ric}\right)(X, Y) .$$
Further, a short computation gives
$$\left(d^{\nabla} \delta^{\nabla} R\right)_{X, Y, W, Z}=K(A)_{X, Y, Z, W},$$
where $A_{X, Y, Z, W}=\left(\nabla_{X, W}^{2} \operatorname{Ric}\right)(Y, Z)$. Using this and the product rule for the differential several times, we eventually obtain
$$\begin{aligned}
\left\langle d^{\nabla} \delta^{\nabla} R, \Omega \otimes \Omega\right\rangle= & \frac{1}{2} \Delta s-2 \delta\left(J \delta\left(J \operatorname{Ric}^{\prime \prime}\right)\right)+\mid \text { Ric }\left.^{\prime \prime}\right|^{2} \\
& +2\langle\rho, \phi\rangle-\left\langle\rho, \nabla^{*} \nabla \Omega\right\rangle .
\end{aligned}$$
Summing up (18), (16), (17) and using (15), we finally get the last term of the right hand-side of (9),
$$\begin{aligned}
\left\langle\nabla^{*} \nabla R, \Omega \otimes \Omega\right\rangle= & \frac{1}{2} \Delta s-2 \delta\left(J \delta\left(J \operatorname{Ric}^{\prime \prime}\right)\right) \\
& +\left|\operatorname{Ric}^{\prime \prime}\right|^{2}-4\left|\widetilde{R}^{\prime \prime}\right|^{2}+2\langle\rho, \phi\rangle+\frac{1}{2}\left|\nabla^{*} \nabla \Omega\right|^{2}+\frac{1}{2}|\phi|^{2} .
\end{aligned}$$
Using (10), (14), (19) back in relation (9), we get the formula (7) claimed in the statement. Q.E.D.

Proof of Theorem 1. We now turn back to the notation used in Section 2.1. Thus, $(g, J, \Omega)$ denotes the Kähler structure, with Ricci tensor having two non-negative distinct constant eigenvalues $0 \leq \lambda<\mu$, while $(g, \bar{J}, \bar{\Omega})$ is the almost Kähler structure constructed by Lemma 1; we shall also use the (1,1)-forms $\alpha$ and $\beta$ introduced in Section 2.1, so that we have
$$\Omega=\alpha+\beta ; \bar{\Omega}=\alpha-\beta ; \rho=\lambda \alpha+\mu \beta ; \bar{\rho}=\lambda \alpha-\mu \rho,$$
where $\rho$ and $\bar{\rho}$ are the Ricci forms of $(g, J)$ and $(g, \bar{J})$, respectively.
For proving Theorem 1 it is enough to show that $\bar{J}$ is integrable (see Lemma 1), or equivalently, that $\nabla \bar{\Omega}=0$. The latter will be derived from the integral inequality stated in Corollary 2 (see Remark 3).

Let $\bar{\phi}(X, Y)=\left\langle\nabla_{\bar{J} X} \bar{\Omega}, \nabla_{Y} \bar{\Omega}\right\rangle$ be the semi-positive definite (1,1)-form with respect to $\bar{J}$, defined in Proposition 1. By (20) and using the semi-positivity of the (1,1)-forms $\alpha$ and $\bar{\phi}$, we get
$$\begin{aligned}
\langle\bar{\rho}, \bar{\phi}\rangle-\left\langle\bar{\rho}, \nabla^{*} \nabla \bar{\Omega}\right\rangle= & (\lambda-\mu)\langle\alpha, \bar{\phi}\rangle+(\mu-\lambda)\left\langle\alpha, \nabla^{*} \nabla \bar{\Omega}\right\rangle \\
& +\mu\langle\bar{\Omega}, \bar{\phi}\rangle-\mu\left\langle\bar{\Omega}, \nabla^{*} \nabla \bar{\Omega}\right\rangle \\
= & (\lambda-\mu)\langle\alpha, \bar{\phi}\rangle+(\mu-\lambda)\left\langle\alpha, \nabla^{*} \nabla \bar{\Omega}\right\rangle-\frac{\mu}{2}|\nabla \bar{\Omega}|^{2} \\
\leq & (\mu-\lambda)\left\langle\alpha, \nabla^{*} \nabla \bar{\Omega}\right\rangle-\frac{\mu}{2}|\nabla \bar{\Omega}|^{2} .
\end{aligned}$$
Since $\langle\alpha, \nabla \bar{\Omega}\rangle=0$ (because $\alpha$ and $\nabla \bar{\Omega}$ are of type $(1,1)$ and (2, 0)+(0, 2), respectively), we have
$$\left\langle\alpha, \nabla^{*} \nabla \bar{\Omega}\right\rangle=\langle\nabla \alpha, \nabla \bar{\Omega}\rangle=\frac{1}{2}|\nabla \bar{\Omega}|^{2},$$
where in the last step we used that $\alpha=\frac{1}{2}(\Omega+\bar{\Omega})$ and $\Omega$ is parallel. Substituting into the inequality (21), we obtain
$$\langle\bar{\rho}, \bar{\phi}\rangle-\left\langle\bar{\rho}, \nabla^{*} \nabla \bar{\Omega}\right\rangle \leq-\frac{\lambda}{2}|\nabla \bar{\Omega}|^{2} .$$
Since by assumption $\lambda \geq 0$, the latter inequality shows that $\langle\bar{\rho}, \bar{\phi}\rangle-\left\langle\bar{\rho}, \nabla^{*} \nabla \bar{\Omega}\right\rangle$ is an everywhere non-positive function and Corollary 2 then implies that $\nabla^{*} \nabla \bar{\Omega}=0$; after multiplying by $\bar{\Omega}$ we reach $\nabla \bar{\Omega}=0$. Q.E.D.

Remark 4. The inequality of Corollary 2 can actually be used for any of the almost Kähler structures $\left(g_{t}, \bar{J}\right)$ constructed in Section 2.1 and after some computation it
is not difficult to determine the $t$ dependence of each of the terms. One would then hope to obtain some additional information taking limits when $t \rightarrow 0$ and $t \rightarrow \infty$. Indeed some conclusions can be drawn in the more general situation when only the largest eigenvalue $\mu$ is assumed non-negative, but we fell short of obtaining integrability in this case. We do obtain that all components of the Nijenhuis tensor $N^{\bar{J}}$ of $\bar{J}$ are zero except maybe those of the form $\left\langle N^{\bar{J}}(A, B), B^{\prime}\right\rangle=-\left\langle N^{\bar{J}}(B, A), B^{\prime}\right\rangle$, for $A \in E_{\lambda}, B, B^{\prime} \in E_{\mu}$. This is equivalent to $E_{\lambda}$ being a totally geodesic distribution.

\section*{3. Homogeneous Kähler manifolds}

In this section we consider connected simply connected homogeneous Kähler manifolds $(M, g, J)$, meaning that the group of all holomorphic isometries of $(M, g, J)$ acts transitively. Note that for any such manifold the Ricci tensor, which is completely determined by an invariant volume form, coincides up to sign with the canonical Hermitian form of $(M, g, J)$ [27]; in particular Ric has constant eigenvalues with respect to $g$.

Any homogeneous Kähler manifold admits a holomorphic fibering over a homogeneous bounded domain whose fiber, with the induced Kähler structure, is isomorphic to a direct product of a flat homogeneous Kähler manifold and a simply connected compact homogeneous Kähler manifold; cf. [23],[18]. In this structure theorem an important role is played by the Ricci tensor whose kernel corresponds to the flat factor [35]; thus, when the Ricci tensor is non-negative, the manifold splits as the product of a flat homogeneous manifold (corresponding to the kernel of Ric) and a compact homogeneous Kähler manifold (and thus having positive Ricci form), see [14]. As for the case of compact homogeneous manifolds, Theorem 1 implies

Corollary 3. A compact irreducible homogeneous Kähler manifold is either Kähler-Einstein, or else the Ricci tensor has at least three distinct eigenvalues.

Of course, the above corollary can be easily derived from the classification of the compact homogeneous Kähler manifolds, see e.g. [52].

Considering non-trivial (Kähler) homogeneous fibrations over bounded homogeneous domains we obtain lots of examples of irreducible homogeneous Kähler manifolds with two distinct eigenvalues $\lambda<0, \mu \geq 0$ (for explicit examples in complex dimension 2 see e.g. [44, 13, 2]).

We are now going to provide (non-compact) simply connected irreducible homogeneous Kähler manifolds $(M, g, J)$ with Ricci tensor having two negative eigenvalues $\lambda<\mu<0$. According to Corollary 1 these also provide complete examples of Einstein strictly almost Kähler manifolds.

Since Ric is negative definite, $(M, J)$ must be holomorphically equivalent to a bounded homogeneous domain; see [43, 36, 35]. It is a result of Vinberg, Gindikin and Piatetskii-Shapiro [48] that any such domain has a realization as a Siegel domain of type II, i.e. a domain $D=\left\{(z, w) \in \mathbb{C}^{n} \times \mathbb{C}^{m}: \operatorname{Im} z-H(w, w) \in \mathfrak{C}\right\}$, where $\mathfrak{C}$ is an open convex cone (containing no lines) in $\mathbb{R}^{n}$ and $H: \mathbb{C}^{m} \times \mathbb{C}^{m} \mapsto \mathbb{C}^{n}$ is a Hermitian map which is $\mathfrak{C}$-positive in the sense that
$$H(w, w) \in \overline{\mathfrak{C}}-\{0\} \quad \forall w \neq 0 .$$
If $m=0$, then $D=\mathbb{R}^{n}+i \mathfrak{C}$, i.e. we obtain a Siegel domain of type $I$ (called also a tube domain).

Any Siegel domain admits a simply transitive action of a solvable subgroup $S$ of affine transformations of $D$, so that, fixing a point $p \in D$, we can identify $S$ with $D$. Then, the complex structure $J$ and the Bergman metric $\tilde{g}$ on $D$ pull back to define a canonical left-invariant Kähler-Einstein structure $(\tilde{g}, J)$ on $S$. Our purpose is to show the existence of other left-invariant Kähler metrics on $S$, whose Ricci tensor has two distinct eigenvalues. The construction is purely algebraic and relies on the theory of normal $j$-algebras, see e.g. [23], [48].

The (real) Lie algebra $\mathfrak{s}$ of $S$ is equipped with a scalar product $\rangle$ (coming from $\tilde{g})$ and with a vector space endomorphism $j($ coming from $J)$. This shows that $\mathfrak{s}$ has the structure of a normal $j$-algebra, meaning that there exists a 1-form $\omega$ with $\omega([j X, Y])=\langle X, Y\rangle$ for any $X, Y \in \mathfrak{s}$, cf. [40]. (Abstractly, a normal $j$-algebra $(\mathfrak{s}, j, \omega)$ is a real Lie algebra $\mathfrak{s}$ endowed with an endomorphism $j$ and a 1-form $\omega$ satisfying certain compatibility relations; corresponding to any such algebra there exists a bounded homogeneous domain defining $\mathfrak{s}$ as above.) A result of Piatetskii-Shapiro [40] (see also [15]) describes the structure of the root spaces of $\mathfrak{s}$ : Letting $\mathfrak{n}=[\mathfrak{s}, \mathfrak{s}]$, the orthogonal complement $\mathfrak{a}$ of $\mathfrak{n}$ in $(\mathfrak{s},\langle \rangle)$ is a commutative sub-algebra and $\mathfrak{n}$ can be represented as the direct〈 〉-orthogonal sum of root spaces $\mathfrak{n}_{\epsilon}=\{X \in$ $\mathfrak{n}:[A, X]=\epsilon(A) X, \forall A \in \mathfrak{a}\}$; if we denote by $\epsilon_{1}, \ldots, \epsilon_{r}$ the (non-zero) roots whose root spaces are mapped into $\mathfrak{a}$ by $j$, then $r=\operatorname{dim} \mathfrak{a}=\operatorname{rank} \mathfrak{s}$, and with proper labeling, all other roots are of the form $\frac{1}{2} \epsilon_{k}, \frac{1}{2}\left(\epsilon_{\ell} \pm \epsilon_{s}\right) ; 1 \leq k \leq r ; 1 \leq \ell<s \leq r$ (although some of them can be zero). It follows that $\operatorname{dim}_{\mathbb{R}} \mathfrak{n}_{\epsilon_{k}}=1$ and we then denote by $X_{k}$ a $\left\rangle\right.$-unitary generator of $\mathfrak{n}_{\epsilon_{k}}$; using the fact that $\left[\mathfrak{n}_{\epsilon^{\prime}}, \mathfrak{n}_{\epsilon^{\prime \prime}}\right] \subset \mathfrak{n}_{\epsilon^{\prime}+\epsilon^{\prime \prime}}$ together with the orthogonality of the root spaces, one easily checks

Lemma 3. If $\mathfrak{n}_{\frac{1}{2} \epsilon_{r}}=0$, then the 2-form $\alpha$ which is the $\left\rangle\right.$-dual of $X_{r} \wedge j X_{r}$, is $j$-invariant and closed, i.e. for any $X, Y, Z \in \mathfrak{g}$
$$\begin{gathered}
\alpha(j X, j Y)=\alpha(X, Y) \\
\alpha([X, Y], Z)+\alpha([Z, X], Y)+\alpha([Y, Z], X)=0 .
\end{gathered}$$

Under the hypothesis of Lemma 3 we may define on $S$ (by translations) a left invariant closed (1,1)-form $\alpha$ and a $J$-invariant distribution $\mathcal{R}=\operatorname{span}\left(X_{r}, j X_{r}\right)$. It then follows that the (left-invariant) almost complex structure $\bar{J}$ on $S$, defined by $\left.\bar{J}\right|_{\mathcal{R}^{\perp}}=\left.J\right|_{\mathcal{R}^{\perp}}$ and $\left.\bar{J}\right|_{\mathcal{R}}=-\left.J\right|_{\mathcal{R}}$, where $\mathcal{R}^{\perp}$ denotes the $\tilde{g}$-orthogonal complement of $\mathcal{R}$, has closed fundamental form (equal to $\widetilde{\Omega}-2 \alpha$, where $\widetilde{\Omega}$ is the Kähler form of $\tilde{g}$ ), i.e. $(M, \tilde{g}, \bar{J})$ is an Einstein almost Kähler manifold. Note that $\bar{J}$ is not integrable, provided that $\mathfrak{s}$ (equivalently $D$ ) is irreducible (see Lemma 1); by virtue of Corollary 1, we have also a family of left invariant Kähler metrics on $S$, whose Ricci tensor has two distinct negative eigenvalues.

It only remains the question of existence of irreducible Siegel domains satisfying the hypothesis of Lemma 3. Actually, non-symmetric examples can be found in each complex dimension greater than four, see [40, pp. 63-64] and [15, pp. 411-412]. But even more interestingly, they also exist amongst the classical (Hermitian) symmetric domains.

Corollary 4. Every irreducible Hermitian symmetric space of non-compact type which admits a realization as a tube domain carries a strictly almost Kähler structure commuting with the standard Kähler structure.

Proof. Suppose that $(M, g, J)$ is a Hermitian symmetric space of the non-compact type and denote by $D$ one (of the many possible) realization of $(M, J)$ as a Siegel
domain (called in this case symmetric domain). It is well known that $g$ is now the Bergman metric of $D$ and the real dimensions of the root spaces $\mathfrak{n}_{\frac{1}{2} \epsilon_{k}}$ are all equal to $\frac{2 m}{r}$ (see e.g. [16, 41]); in particular, the condition $\mathfrak{n}_{\frac{1}{2} \epsilon_{r}}=0$ means that $(M, g, J)$ admits a realization as a tube domain (see above). The complete list of the Hermitian symmetric spaces admitting a tube domain realization can be found for example in [41, pp. 114-118]. Q.E.D.

Example 1. An explicit example of a symmetric strictly almost Kähler manifold (of real dimension $2 n, n \geq 3$ ) is given by $\operatorname{SO}(2, n) /(\operatorname{SO}(2) \times \operatorname{SO}(n)), n \geq 3$. (It is well known that this space admits a realization as a tube domain).

\section*{4. The two dimensional case - Proof of Theorem 2}

From now on we assume that $(M, g, J)$ is a Kähler surface with two distinct constant eigenvalues $\lambda<\mu$. We note that in real four dimensions, an almost complex structure $\bar{J}$ which commutes with $J$ (and differs from $\pm J$ ) induces the orientation opposite to that of $(M, J)$; if we denote by $\bar{M}$ the smooth manifold $M$, but endowed with the opposite orientation, then, by Lemma 1, $\bar{M}$ carries a symplectic structure $\bar{\Omega}$. As a matter of fact, a way of rephrasing Lemma 1 is to say that $\bar{\Omega}$ defines an indefinite Kähler metric on $(M, J)$, meaning that $\bar{\Omega}$ is a non-degenerate, closed (1,1)-form which induces the orientation opposite to the one of $(M, J)$.

By Theorem 1 we can further assume $\lambda<0$; in this case, using the same deformation trick as in the proof of Corollary 1, one can deform our metric to one whose Ricci tensor has constant eigenvalues $\lambda<\mu$ with $\lambda+\mu<0$.

The next lemma is a consequence of results of [28] and [39] and relies essentially on the Kodaira classification of compact complex surfaces (see e.g. [8]), combined with the non-triviality of certain Seiberg-Witten invariants on the symplectic manifold $\bar{M}$, cf. [45].

Lemma 4. Let $(M, g, J)$ be a compact Kähler surface whose Ricci tensor has two distinct constant eigenvalues $\lambda<\mu$ with $\lambda+\mu<0$. Then the manifold is one of the following:
\begin{itemize}
\item[(i)] a minimal ruled surface which is the projectivization of a holomorphic rank 2 vector bundle over a curve of genus at least 2 and $\lambda<0<\mu$, or
\item[(ii)] a minimal properly elliptic surface which is an elliptic fibration over a curve of genus at least 2 with no fibers of singular reduction and $\lambda<\mu=0$, or
\item[(iii)] a minimal surface of general type with ample canonical bundle and with even and non-negative signature and $\lambda<\mu<0$.
\end{itemize}

Proof. We first recall that for any Kähler surface $(M, g, J, \Omega)$ of negative scalar curvature we have $H^{0}\left(M, K^{\otimes-m}\right)=0$, where $K$ denotes the canonical bundle of $(M, J)$ (cf. e.g. [51]).
J. Petean [39] classified the compact complex surfaces possibly admitting indefinite Kähler metrics; those of Kähler type which satisfy $H^{0}\left(M, K^{\otimes-m}\right)=0$ could be either the surfaces described in (i) \& (ii), or minimal surfaces of general type with even and non-negative signature. This is also a consequence of more general results of D. Kotschick [28].

As for the signs of the eigenvalues $\lambda, \mu$ we recall that $\frac{1}{2 \pi} \rho$ represents $c_{1}$ in $H^{2}(M, \mathbb{R})$ so that
$$c_{1}^{2}(M)=\frac{1}{4 \pi^{2}} \int_{M} \lambda \mu d V_{g},$$
where $d V_{g}=\frac{1}{2} \Omega \wedge \Omega$ is the volume form of $(g, J, \Omega)$. It is well known [8] that the complex surfaces described in (i) satisfy $c_{1}^{2}<0$, for those in (ii) we have $c_{1}^{2}=0$, while a minimal surface of general type satisfies $c_{1}^{2}(M)>0$; since $\lambda+\mu<0$ we get the needed conclusions.

We complete the proof by observing that the minimal surfaces of general type appearing in (iii) have ample canonical bundle since $\rho$ is a negative definite representative of $c_{1}$. Q.E.D.

Remark 5. Some minimal complex surfaces of general type with positive signature (which therefore admit no locally homogeneous structure) do admit indefinite Kähler metrics (cf. [26], [6]). Unfortunately, we do not know if they admit Kähler metrics with constant eigenvalues of the Ricci tensor.

Using a result of [30] and arguments from [4] and [2], we prove the integrability of $\bar{J}$ provided that one of the constant eigenvalues is non-negative.

Lemma 5. Every compact Kähler surface $(M, g, J)$ whose Ricci tensor has two distinct constant eigenvalues $\lambda<\mu$ with $\mu \geq 0$ is locally symmetric.

Proof. According to Theorem 1 and Lemma 2, we may assume that the scalar curvature $s=2(\lambda+\mu)$ is negative. Thus, we have to consider the two possibilities for $(M, J)$ listed in Lemma 4, (i)\&(ii).
(i) If $(M, J)$ is a minimal ruled surface as in Lemma 4(i), then by a result of LeBrun [30] $(M, g, J)$ is locally Hermitian symmetric. Alternatively, using (1), one can deform our Kähler metric $g$ to one whose Ricci tensor has eigenvalues $(-1,+1)$ (see Lemma 2), i.e. to a scalar-flat Kähler metric; the later is locally symmetric [7], and so is then $g$.
(ii) Let $(M, J)$ be a minimal properly elliptic surface. By Lemma 4, we have $\lambda<\mu=0$. Adopting the notations used in Section 2, $E_{\lambda}$ and $E_{\mu}$ denote the corresponding eigenspaces of Ric and so on. We thus have that Ric is semi-negative definite and $\operatorname{Ker}($ Ric $)=E_{\mu}$. From Lemma 4 (ii) we also know that $(M, J)$ is an elliptic fibration over an irrational complex curve with no fibers of singular reduction. As observed for example in [4], after replacing $(M, J)$ with a finite cover if necessary, we may assume that $(M, J)$ carries a non-vanishing holomorphic vector field $X$ (acting by translations on the fibers). Now the Bochner-Lichnerowicz formula (cf. e.g. [9]) shows that $X$ belongs to $E_{\mu}$ and that $X$ is parallel with respect to the Levi-Civita connection of $g$; it follows that $E_{\mu}$ is parallel and so is its orthogonal complement $E_{\lambda}$. Since $J$ is parallel by assumption, the almost complex structure $\bar{J}$ defined in Lemma 1 must be parallel too. Thus $(g, \bar{J})$ is Kähler and $(M, g)$ is locally symmetric, as observed in Lemma 1. Q.E.D.

Let us now consider the case (iii) of Lemma 4.
Lemma 6. A complex surface $(M, J)$ carries a Kähler metric $g$ whose Ricci tensor has two distinct, negative, constant eigenvalues if and only if there exists a Kähler-Einstein metric $\widetilde{g}$ on $(M, J)$ of negative scalar curvature, which admits a compatible almost Kähler structure $\bar{J}$ commuting with $J$; moreover, $\bar{J}$ is integrable precisely
when $g$ (and $\widetilde{g}$ ) is locally symmetric. If the manifold is assumed compact, $\bar{J}$ is integrable if and only if the signature of $M$ is zero.

Proof. The first part of the lemma follows from Corollary 1; by Lemma 1 we conclude that the integrability of $\bar{J}$ is equivalent to $(M, g)$ (hence also $(M, \widetilde{g})$ ) being locally symmetric, i.e. locally a product of two curves of distinct constant Gauss curvatures. In the compact case, the signature of any such complex surface is zero. To complete the proof it remains to show that conversely, if the signature of $M$ is zero, then $\bar{J}$ is necessarily integrable.

Suppose for contradiction that the signature of $M$ is zero and that $\bar{J}$ is not integrable. It then follows by Lemma 1, Remark 1 and [19, Th. 2] that $c_{1}(\bar{M})$. $[\bar{\Omega}]<0$. By a result of Taubes [46] we conclude that the Seiberg-Witten invariant (for the appropriate chamber) of the symplectic manifold $(\bar{M}, \bar{\Omega})$ is non-zero so that, according to a result of Leung [31] (see also [28]), $(M, J)$ is uniformized by a polydisk. From the uniqueness of the Kähler-Einstein metric [50] we conclude that $\widetilde{g}$ is locally a product metric and therefore changing the orientation on one of the factors defines a (locally product) Kähler structure ( $\widetilde{g}, \widetilde{J}$ ) on $\bar{M}$; it then follows for example by [3] that $\bar{J}$ coincides (up to sign) with $\widetilde{J}$, i.e. $\bar{J}$ is integrable, a contradiction. Q.E.D.

Remark 6. Claude LeBrun suggested to us an alternative way to see the connection with the Goldberg conjecture, as follows: Let $(g, J)$ be a Kähler structure with Ricci tensor $\mathrm{Ric}^{g}$ having two distinct negative eigenvalues. The metric $g$ has constant central curvature, so considering the Kähler metric $\widetilde{g}=-\operatorname{Ric}^{g}$, this has the same Ricci form as the metric $g$ (see [32]). Thus $(\widetilde{g}, J)$ is a Kähler-Einstein metric. Now it is not hard to see that the Kähler form of $g$ is a harmonic form of constant length with respect to $\widetilde{g}$; so will then be its anti-self-dual part which gives rise to a negative almost Kähler (Einstein) structure $(\widetilde{g}, \bar{J})$.

Proof of Theorem 2. Theorem 2 now follows from Theorem 1 and Lemmas 5 and 6.

Acknowledgments. We are very grateful to Claude LeBrun for suggesting the relation between the constant eigenvalues problem and the Goldberg conjecture, to Gideon Maschler for explaining his results on central Kähler metrics, and to Dimitrii Alekseevsky for many useful and instructive discussions on bounded homogeneous domains. We would also like to thank the referee for useful observations and to several other people with whom we had stimulating discussions - J. Armstrong, R. Bielawski, Ph. Delanoe, P. Gauduchon and C. Simpson. The first-named author would like to thank the hospitality of Max-Planck-Institut in Bonn and IHÉS during the preparation of this work.

\section*{References}
\begin{itemize}
\item[] [1] V. Apostolov, J. Armstrong, Symplectic 4-manifolds with Hermitian Weyl tensor, Trans. Amer. Math. Soc., 352 (2000), 4501-4513.
\item[] [2] V. Apostolov, J. Armstrong and T. Draghici, Local rigidity of certain classes of almost Kähler 4-manifolds, Preprint 1999, available at math.DG/9911197.
\item[] [3] V. Apostolov and T. Draghici, Hermitian conformal classes and almost Kähler structures on four manifolds, Diff. Geom. Appl., 11 (1999), 179-195.
\item[] [4] V. Apostolov, T. Draghici and D. Kotschick, An integrability theorem for almost Kähler 4-manifolds, C. R. Acad. Sci., Paris, Ser. I, t. 329 (1999), 413-418.
\end{itemize}
\begin{itemize}
\item[] [5] J. Armstrong, An Ansatz for Almost-Kähler, Einstein 4-manifolds, to appear in J. reine angew. Math.
\item[] [6] M. Atiyah, The signature of fiber bundles, in "Global Analysis", Papers in Honor of K. Kodaira, Tokyo University Press (1969).
\item[] [7] P. de Bartolomeis and D. Burns, Stability of vector bundles and extremal metrics, Inv. Math. 92 (1988), 403-407.
\item[] [8] W.Barth, C.Peters and A. Van de Ven, Compact complex surfaces, Springer-Verlag, 1984.
\item[] [9] A. L. Besse, Einstein manifolds, Ergeb. Math. Grenzgeb.3, Folge 10, Springer-Verlag, Berlin, Heidelberg, New York, 1987.
\item[] [10] R. Bielawski, Ricci-flat Kähler metrics on canonical bundles, preprint 2000, available at math.DG/0006144.
\item[] [11] D. E. Blair and S. Ianus, Critical associated metrics on symplectic manifolds, Contemp. Math. 51 (1986), 23-29.
\item[] [12] J.-P. Bourguignon, Les variétés de dimension 4 à signature non nulle dont la courbure est harmonique sont d'Einstein, Inv. Math. 63 (1981), 263-286.
\item[] [13] R. Bryant, private communication.
\item[] [14] J. Cheeger and S. Gromoll, The splitting theorem for manifolds of non-negative Ricci curvature, J. Differential Geom., 6 (1971), 119-128.
\item[] [15] J.E. D'Atri, Holomorphic sectional curvatures of bounded homogeneous domains and related questions, Trans. Amer. Math. Soc. 256 (1979), 405-413.
\item[] [16] J.E. D'Atri and D. Miatello, A characterization of bounded symmetric domains by curvature, Trans. Amer. Math. Soc., 267 (1983), 531-540.
\item[] [17] J. Davidov and O. Muškarov, Twistor spaces with Hermitian Ricci tensor, Proc. Amer. Math. Soc. 109 (1990), no. 4, 1115-1120.
\item[] [18] J. Dorfmeister and K. Nakajiama, The fundamental conjecture for homogeneous Kähler manifolds, Acta Math., 161 (1988), 23-70.
\item[] [19] T. Draghici, Almost Kähler 4-manifolds with J-invariant Ricci tensor, Houston J. Math., 25 (1999), 133-145.
\item[] [20] L. Hernández-Lamoneda, Curvature vs. Almost Hermitian Structures, Geom. Dedicata, 79 (2000), 205-218.
\item[] [21] A. Hwang and M. Singer, A momentum construction for circle-invariant Kähler metrics, available at math.DG/9811024.
\item[] [22] P. Gauduchon, Complex structures on compact conformal manifolds of negative type, in "Complex Analysis and Geometry", (eds. V. Ancona, E. Ballico and A. Silva) Marcel Dekker, New York-Basel-Hong Kong, 1996, 201-212.
\item[] [23] S.G. Gindikin, I.I. Piatetskii-Shapiro, and E.B. Vinberg, Homogeneous Kähler manifolds, in "Geometry of Homogeneous Bounded Domains", C.I.M.E., 1967, 1-88.
\item[] [24] S.I. Goldberg, Integrability of almost Kähler manifolds, Proc. Amer. Math. Soc. 21 (1969), 96-100.
\item[] [25] A. Gray, Curvature identities for Hermitian and almost Hermitian manifolds, Tôhoku Math. J. 28 (1976), 601-612.
\item[] [26] K. Kodaira, A certain type irregular algebraic surfaces, J. Analyse Math. 19 (1967), 207-215.
\item[] [27] J.L. Koszul, Sur la forme hermitienne canonique des espaces homogènes complexes, Canad. J. Math. 7 (1955), 562-576.
\item[] [28] D. Kotschick, Orientations and geometrisations of compact complex surfaces, Bull. London Math. Soc. 29 (1997), no. 2, 145-149.
\item[] [29] O. Kowalski, Generalized Symmetric Spaces, LNM 805, 1980.
\item[] [30] C. LeBrun, Polarized 4-manifolds, extremal Kähler metrics and Seiberg-Witten theory, Math. Res. Lett. 2, No.5, 653-662 (1995).
\item[] [31] N.C. Leung, Seiberg-Witten invariants and uniformizations, Math. Ann. 306 (1996), 31-46.
\item[] [32] G. Maschler, Central Kähler metrics, Preprint.
\item[] [33] A. Moroianu, On Kirchberg inequality for compact Kähler manifolds of even complex dimension, Ann. Global Anal. Geom. 15 (1997), 235-242.
\item[] [34] A. Moroianu, Kähler manifolds with small eigenvalues of the Dirac operator and a conjecture of Lichnerowicz, Ann. Inst. Fourier (Grenoble), 49 (1999), 1637-1659.
\item[] [35] K. Nakajima, Homogeneous Kähler manifolds of non-degenerate Ricci curvature, J. Math. Soc. Japan, 42 (1990), 475-494.
\end{itemize}
[36] K. Nakajima, Homogeneous Kähler manifolds of non-positive Ricci curvature, J. Math. Kyoto Univ., 26 (1986), 547-558.
[37] T. Oguro, K. Sekigawa, Four-dimensional almost Kähler Einstein and $*$-Einstein manifolds, Geom. Dedicata, 69 (1998), 91-112.
[38] Z. Olszak, A note on almost Kähler manifolds, Bull. Acad. Polon. Sci., XXVI (1978), 139-141.
[39] J. Petean, Indefinite Kähler-Einstein metrics on compact complex surfaces, Comm. Math. Phys. 189 (1997), 227-235.
[40] I.I. Piatetskii-Shapiro, Automorphic functions and the geometry of classical domains, English transl., Gordon and Breach, New York, 1969.
[41] I. Satake, Algebraic Structures of Symmetric Domains, Iwanami Shoten Publ. and Princeton University Press, 1980.
[42] K. Sekigawa, On some compact Einstein almost Kähler manifolds, J. Math. Soc. Japan, 39 (1987), 677-684.
[43] H. Shima, On homogeneous Kähler manifolds of solvable Lie groups, J. Math. Soc. Japan, 25 (1973), 422-445.
[44] H. Shima, On homogeneous Kähler manifolds with non-degenerate canonical Hermitian form of signature $(2,2(n-1))$, Osaka J. Math., 10 (1973), 477-493.
[45] C. H. Taubes, The Seiberg-Witten Invariants and Symplectic Forms, Math. Res. Lett., 1 (1994), 809-822.
[46] C. H. Taubes, SW ⇒ Gr: from the Seiberg-Witten equations to pseudo-holomorphic curves, J. Amer. Math. Soc., 9(1996), no.3, 845-918.
[47] F. Tricerri and L. Vanhecke, Curvature tensors on almost Hermitian manifolds, Trans. Amer. Math. Soc., 267 (1981), 365-398.
[48] E.B. Vinberg, S.G. Gindinkin, and I.I. Piatetskii-Shapiro, Classification and canonical realization of complex bounded homogeneous domains, Trudy Moskov. Mat. Obsc. 12 (1963), 359-388; [Trans. Moscow Math. Soc., 1963, 404-437].
[49] C. T. C. Wall, Geometric structures on compact complex analytic surfaces, Topology 25 (1986), 119-153.
[50] S.-T. Yau, On the Ricci curvature of a compact Kähler manifold and the complex Monge-Ampère equation I, Comm. Pure Appl. Math. 31, (1978) 339-411.
[51] S.-T. Yau, On the scalar curvature of compact Hermitian manifolds, Inv. Math. 29 (1974), 213-239.
[52] H.C. Wang, Closed manifolds with homogeneous complex structure, Amer. J. Math., 76 (1954), 1-32.

Vestislav Apostolov, Département de Mathématiques, Université du Québec à Montréal, Case postale 8888, succursale centre-ville, Montréal (Québec), H3C 3P8, Canada
E-mail address: apostolo@math.uqam.ca
Tedi Drăghici, Department of Mathematics, Florida International University, Miami FL 33199, USA
E-mail address: draghici@fiu.edu
Andrei Moroianu, CMAT, École Polytechnique, UMR 7640 du CNRS, 91128 Palaiseau, France
E-mail address: am@math.polytechnique.fr