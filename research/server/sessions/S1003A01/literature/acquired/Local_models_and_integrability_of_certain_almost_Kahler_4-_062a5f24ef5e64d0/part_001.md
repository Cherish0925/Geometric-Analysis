---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Local models and integrability of certain almost Kahler 4- ...]

---
source_file: math_0109098.pdf
converter: mathpix
format: mmd
---

\title{
LOCAL MODELS AND INTEGRABILITY OF CERTAIN ALMOST KÄHLER 4-MANIFOLDS
}

\author{
VESTISLAV APOSTOLOV, JOHN ARMSTRONG AND TEDI DRĂGHICI
}

\begin{abstract}
We classify, up to a local isometry, all non-Kähler almost Kähler 4-manifolds for which the fundamental 2-form is an eigenform of the Weyl tensor, and whose Ricci tensor is invariant with respect to the almost complex structure. Equivalently, such almost Kähler 4-manifolds satisfy the third curvature condition of A. Gray. We use our local classification to show that, in the compact case, the third curvature condition of Gray is equivalent to the integrability of the corresponding almost complex structure.
\end{abstract}

2000 Mathematics Subject Classification. Primary 53B20, 53C25

\section*{1. Introduction}

Let $(M, \Omega)$ be a symplectic manifold of dimension $2 n$. An almost complex structure $J$ is called compatible with the symplectic form $\Omega$, if there exists a Riemannian metric $g$ such that
$$\Omega(\cdot, \cdot)=g(J \cdot, \cdot) .$$
In this case, the metric $g$ is also called compatible with $\Omega$, while the triple $(g, J, \Omega)$ is referred to as an almost Kähler structure on $M$. If, additionally, the compatible almost complex structure $J$ is integrable, then $(g, J, \Omega)$ is a Kähler structure on $M$. Almost Kähler manifolds for which the almost complex structure $J$ is not integrable will be called strictly almost Kähler.

Gromov's theory of pseudo-holomorphic curves [27], Taubes' characterization of SeibergWitten invariants of symplectic 4-manifolds [45, 46] and the recent works of Donaldson [17, 18] conclusively situated the study of (strictly) almost Kähler manifolds into the mathematical main-stream. A very recent work of LeBrun [38], for instance, inspired by some aspects of Taubes' construction of solutions of the Seiberg-Witten equations on symplectic 4-manifolds, relates the existence of strictly almost Kähler 4-manifolds having particular properties of the curvature with some fundamental problems in Riemannian Geometry, such as the existence and uniqueness of Einstein metrics, or of metrics minimizing volume among all Riemannian metrics satisfying point-wise lower bounds on sectional curvatures.

Despite the now compelling appeal of the "Riemannian" aspect of almost Kähler geometry, the subject suffered for a long time from a genuine lack of interesting examples. For instance, an old still open conjecture of Goldberg [23] affirms that there are no Einstein, strictly almost Kähler metrics on a compact symplectic manifold. K. Sekigawa proved [44] that the conjecture is true if the scalar curvature is non-negative. The case of negative scalar curvature is still wide open, despite of the recent discovery of complete Einstein strictly almost Kähler manifolds of any dimension $2 n \geq 6$ [6], and of (local) Ricci-flat strictly almost Kähler metrics of dimension four [4, 9, 41]. Indeed, in addition to some subtle topological obstructions in dimension four [32, 36, 37, 38], it turns out that there

\footnotetext{
The first author was supported in part by a PAFARC-UQAM grant, NSERC grant OGP0023879 and by FCAR grant NC-7264. He is also member of EDGE, Research Training Network HPRN-CT-2000-00101, supported by the European Human Potential Programme. The first and the third authors were supported in part by NSF grant INT-9903302.
}
is a number of (rather not well understood yet) local obstructions to the existence of Einstein strictly almost Kähler metrics compatible with a given symplectic form [2]. Further progress on the Goldberg conjecture seems to hinge on a better understanding of these obstructions.

Classically, on a compact manifold $M$, the Einstein condition appears as the EulerLagrange equation of the Hilbert functional S, the total scalar curvature, acting on the space of all Riemannian metrics on $M$ of a given volume. A "symplectic" setting of this variational problem was first considered by Blair and Ianus [13]: let $(M, \Omega)$ be a compact symplectic manifold and restrict the functional $\mathbf{S}$ to the space of $\Omega$-compatible Riemannian metrics, then the critical points are the almost Kähler metrics $(g, J, \Omega)$ whose Ricci tensor Ric is $J$-invariant, i.e. satisfies:
$$\operatorname{Ric}(J \cdot, J \cdot)=\operatorname{Ric}(\cdot, \cdot) .$$
The Euler-Lagrange equation (1) is a weakening of both the Einstein and the Kähler conditions. Furthermore, Blair [12] observed that for any almost Kähler metric $(g, J)$ the following relation holds:
$$\frac{1}{4} \int_{M}|\nabla J|^{2} d \mu+\mathbf{S}(g)=\frac{4 \pi}{(n-1)!}\left(c_{1} \cdot[\Omega]^{\wedge(n-1)}\right)(M)$$
where ∇ is the Riemannian connection of $g,|\cdot|$ is the point-wise norm induced by $g$, and $c_{1}$ and $d \mu=\frac{1}{n!} \Omega^{\wedge n}$ are respectively the first Chern class and the the volume form of $(M, \Omega)$. Note that the right hand-side of the above equality is a symplectic invariant (hence is independent of the choice of a particular $\Omega$-compatible metric); thus the $\Omega$-compatible almost Kähler structures satisfying (1) are also the critical points of the Energy functional, which acts on the space of $\Omega$-compatible almost complex structures by
$$\mathbf{E}(J)=\int_{M}|\nabla J|^{2} d \mu$$
From this point of view, critical almost Kähler metrics have been recently studied in [34]. Clearly, the functional E (resp. S) is bounded from below (resp. from above), the Kähler metrics being minima of $\mathbf{E}$ (resp. maxima of $\mathbf{S}$ ). However, a direct variational approach of finding extremal metrics for these functionals seems not to be easily applicable as it may happen that the infimum of $\mathbf{E}$ be zero, although $M$ does not carry Kähler structures at all (see [34]). In fact, apart from the explicit compact examples of [1, 16] (which, multiplied by Kähler manifolds, provide examples of any dimension $2 n \geq 6$ ), almost nothing seems to be known in general about existence of compact strictly almost Kähler metrics satisfying (1). In particular, no such example is yet known on a compact symplectic 4-manifold.

One reason for which some technical difficulties appear in applying global methods is perhaps hidden in the fact that even locally the equation (1) is difficult to be solved. Indeed, it consists of a system of PDE's for a compatible metric with $\Omega$, which does not satisfy the Cartan test [2]. One finds instead a number of nontrivial relations between higher jets of $J$ and the curvature of $g$. On a compact manifold precisely these relations are at the origin of the integrability results obtained in [2, 5, 9, 20, 44]. The few known (local) examples appear, in fact, as a byproduct of additional geometric structure which makes the study of the Euler-Lagrange equation (1) more tractable.

The additional structure relevant to this paper comes as an extra-assumption imposed on the curvature tensor of the almost Kähler 4-manifold, namely
$$W(\Omega)=\nu \Omega,$$
where $W$ is the Weyl tensor of $g$, viewed as a symmetric traceless endomorphism acting on the space of 2-forms; thus, equation (2) is equivalent to $\Omega$ being an eigenform of the Weyl tensor, in which case the eigenfunction $\nu$ is smooth and equal, up to a factor 1/6, to the so-called conformal scalar curvature $\kappa$ of $(g, J)$ (see Section 2.3 for a precise definition).

The condition (2) in its own right appears to be natural in the context of four dimensional almost Kähler geometry. Indeed, motivated by harmonic maps theory, C. Wood [48] showed that an almost Kähler 4-manifold $(M, g, J, \Omega)$ satisfies (2) if and only if $J$ is a critical point of the energy functional $\mathbf{E}$, but under variations through all almost complex structures compatible with the given metric $g$; for this reason such almost complex structures were called harmonic in [48]. Furthermore, almost Kähler metrics saturating the new curvature estimates of [38] must all satisfy (2).

Let us finally mention that each of the conditions (1) and (2) corresponds to the vanishing of a certain irreducible component of the curvature $R$ under the action of $U(2)$ on the space of algebraic curvature tensors [47]. Taken together, (1) \& (2) are equivalent to the more familiar third curvature condition of Gray (see [26]):
$$R_{X Y Z U}=R_{J X J Y J Z J U} .$$
Evidently, the curvature of a Kähler manifold satisfies (3), hence any of the conditions (1) and (2).

In [3], we have constructed an explicit family of strictly almost Kähler metrics that all satisfy the third Gray condition (3). The main purpose of this paper is to close the circle of ideas from our previous work [3], by showing that, conversely, any strictly almost Kähler 4-manifold which satisfies (3) is locally modeled by a metric in this family:

Theorem 1. Let $\left(\Sigma, g_{\Sigma}, \Omega_{\Sigma}\right)$ be an oriented Riemann surface with metric $g_{\Sigma}$ and volume form $\Omega_{\Sigma}$, and let $h=w+i v$ be a non-constant holomorphic function on $\Sigma$, whose real part $w$ is everywhere positive. On the product of $\Sigma$ with $\mathbb{R}^{2}=\{(z, t)\}$ consider the symplectic form
$$\Omega=\Omega_{\Sigma}-d z \wedge d t$$
and the compatible Riemannian metric
$$g=g_{\Sigma}+w d z^{\otimes 2}+\frac{1}{w}(d t+v d z)^{\otimes 2}$$
Then,
\begin{itemize}
\item[(i)] $(g, \Omega)$ defines a strictly almost Kähler structure whose curvature satisfies the third Gray condition (3).
\item[(ii)] For any connected strictly almost Kähler 4-manifold $(M, g, \Omega)$ whose curvature satisfies (3) there exists an open dense subset $U$ with the following property: in a neighborhood of any point of $U,(g, \Omega)$ is homothetic to an almost Kähler structure given by (4-5).
\end{itemize}

This local classification of strictly almost Kähler 4-manifolds satisfying (3) includes as particular cases some previously known results from [3] and [9]. Indeed, the Einstein metrics in our family correspond to the case when $\left(\Sigma, g_{\Sigma}\right)$ is a flat surface so that $g$ is a Gibbons-Hawking metric [22] with respect to a translation-invariant harmonic function; we get precisely the selfdual Ricci-flat strictly almost Kähler examples of [9, 41, 43]. Furthermore, if we consider the half-plane realization of the hyperbolic space $\left(\mathbb{H}^{2}, g=\frac{d x^{2}+d y^{2}}{x^{2}}\right)$ and take the holomorphic function $h=x+i y$, then (4-5) gives the four dimensional proper 3-symmetric space $\left(\operatorname{Isom}\left(\mathbb{E}^{2}\right) \cdot \operatorname{Sol}_{2}\right) / S O(2)$ (see [25, 33]), which can be characterized as
the only strictly almost Kähler 4-manifold whose curvature tensor preserves the type decomposition of complex 2-forms [3] (a condition known as the second curvature condition of Gray [26]).

To prove Theorem 1 we use local methods which have originated from [9], and have been further developed in [3]. However, the more general result of the current paper requires two main new ingredients. The first comes in the form of a Unique Continuation Principle for the Nijenhuis tensor, $N$, of an almost Kähler 4-manifold satisfying (3) (Proposition 1), which allows us to realize the dense set $U$ in Theorem 1 as the subset of points where $N$ does not vanish. We then consider on $U$ the orthogonal splitting of the tangent bundle $T M$ into the sum of two linear complex sub-bundles, $D$ and $D^{\perp}$, where $D=\left\{T M \ni X: \nabla_{X} J=0\right\}$ is the so-called Kähler nullity of $J$, while its orthogonal complement, $D^{\perp}$, is identified with the canonical bundle $K_{J}$ of $J$ (see Sec. 2.2). This allows us to define another almost complex structure, $I$, which is equal to $J$ when acting on $D$, but to $-J$ on $D^{\perp}$. The almost complex structure $I$ is compatible with $g$, and induces the opposite orientation on $M$. Motivated by this fact, we shall often refer to $(g, I)$ as the opposite almost Hermitian structure associated to $(g, J)$. The second new ingredient, which is the heart of the proof of the above Theorem 1, consists of showing that for any strictly almost Kähler metric $(g, J)$ satisfying (3), the opposite almost Hermitian structure $(g, I)$ is, in fact, a Kähler structure (Proposition 2). Once this is achieved, Theorem 1 follows by [3, Theorem 2] (see also Theorem 3 below).

Note that the metric (5) of Theorem 1 is endowed with an $\mathbb{R}^{2}$-isometric action which is surface-orthogonal and preserves the symplectic form (4); such an action cannot be extended to a Hamiltonian toric action on a compact symplectic 4-manifold. One is then lead to suspect that there will be no compact examples of strictly almost Kähler 4-manifolds satisfying (3) (although there are complete ones [3]). We confirm this with the following integrability theorem, which is a direct generalization of results of [5] and [9]:

Theorem 2. A compact almost Kähler 4-manifold whose curvature satisfies the third Gray condition (3) is necessarily Kähler .

The proof of Theorem 2 involves the local result of Theorem 1 and the unique continuation property established in Proposition 1, together with some global arguments relying on the Enriques-Kodaira classification of compact complex surfaces and structure results for non-singular holomorphic foliations [15, 24] and authomorphism groups [39] of ruled surfaces.

This article can be seen as a natural continuation (and conclusion) of our previous work [3]. The authors have nonetheless endeavored to make the current paper as self-contained as possible. The necessary background of almost Kähler geometry and a quick review of previous results is displayed in Sections 2 and 3 below. The proofs of Theorems 1 and 2 are then presented in Sections 4 and 5.

\section*{2. Elements of almost Kähler geometry}
2.1. Type-decompositions of forms and vectors. Throughout the paper, ( $M, g, J, \Omega$ ) will denote an almost Kähler manifold of (real) dimension 4, where: $g$ is a Riemannian metric, $J$ is a $g$-orthogonal almost-complex structure - i.e. $(M, g, J)$ is an almost Hermitian manifold - and $\Omega(\cdot, \cdot)=g(J \cdot, \cdot)$ is the fundamental 2-form of $(g, J)$, which is closed, and therefore $(M, \Omega)$ is a symplectic manifold.

We denote by: $T M$ the (real) tangent bundle of $M ; T^{*} M$ the (real) cotangent bundle; $\Lambda^{r} M, r=1, \ldots, 4$ the bundle of real $r$-forms; $\langle\cdot, \cdot\rangle$ the inner product induced by $g$ on these bundles (or on their tensor products), with the following conventions for the wedge product
and for the inner product on forms:
$$\begin{gathered}
\left(\alpha_{1} \wedge \ldots \wedge \alpha_{r}\right)_{X_{1}, \ldots, X_{r}}=\operatorname{det}\left(\left(\alpha_{i}\left(X_{j}\right)\right),\right. \\
\left\langle\alpha_{1} \wedge \ldots \wedge \alpha_{r}, \beta_{1} \wedge \ldots \wedge \beta_{r}\right\rangle=\operatorname{det}\left(\left\langle\alpha_{i}, \beta_{j}\right\rangle\right),
\end{gathered}$$
where det denotes the determinant.
Using the metric, we shall implicitly identify vectors and covectors and, accordingly, a 2-form $\phi$ with the corresponding skew-symmetric endomorphism of the tangent bundle $T M$, by putting: $\langle\phi(X), Y\rangle=\phi(X, Y)$ for any vector fields $X, Y$. Also, if $\phi, \psi \in T^{*} M^{\otimes 2}$, by $\phi \circ \psi$ we understand the endomorphism of $T M$ obtained by the composition of the endomorphisms corresponding to the two tensors.

The almost-complex structure $J$ gives rise to a type decomposition of complex vectors and forms. By convention, $J$ acts on the cotangent bundle $T^{*} M$ by $(J \alpha)_{X}=-\alpha_{J X}$, so that $J$ commutes with the Riemannian duality between $T M$ and $T^{*} M$. We shall use the standard decomposition of the complexified cotangent bundle
$$T^{*} M \otimes \mathbb{C}=\Lambda^{1,0} M \oplus \Lambda^{0,1} M,$$
given by the $( \pm i)$-eigenspaces of $J$, the type decomposition of complex 2-forms
$$\Lambda^{2} M \otimes \mathbb{C}=\Lambda^{1,1} M \oplus \Lambda^{2,0} M \oplus \Lambda^{0,2} M,$$
and the type decomposition of symmetric (complex) bilinear forms
$$S^{2} M \otimes \mathbb{C}=S^{1,1} M \oplus S^{2,0} M \oplus S^{0,2} M .$$

Besides the type decomposition of complex forms, we shall also consider the splitting of real 2-forms into $J$-invariant and $J$-anti-invariant ones; for any real section of $\Lambda^{2} M$ (resp. of $S^{2} M$ ), we shall use the super-script ' to denote the projection to the real sub-bundle $\Lambda_{\mathbb{R}}^{1,1} M$ (resp. $S_{\mathbb{R}}^{1,1} M$ ) of $J$-invariant 2 -forms (resp. symmetric 2 -tensors), while the superscript " stands for the projection to the bundle $\llbracket \Lambda^{0,2} M \rrbracket$ (resp. $\llbracket S^{0,2} M \rrbracket$ ) of $J$-anti-invariant ones; here and henceforth $\llbracket \cdot \rrbracket$ denotes the real vector bundle underlying a given complex bundle. Thus, for any section $\psi$ of $\Lambda^{2} M$ (resp. of $S^{2} M$ ), we have the orthogonal splitting $\psi=\psi^{\prime}+\psi^{\prime \prime}$, where
$$\psi^{\prime}(\cdot, \cdot)=\frac{1}{2}(\psi(\cdot, \cdot)+\psi(J \cdot, J \cdot)) \text { and } \psi^{\prime \prime}(\cdot, \cdot)=\frac{1}{2}(\psi(\cdot, \cdot)-\psi(J \cdot, J \cdot)) \text {. }$$
We finally define the $U(2)$-decomposition (with respect to $J$ ) of real 2-forms
$$\Lambda^{2} M=\mathbb{R} \cdot \Omega \oplus \Lambda_{0}^{1,1} M \oplus \llbracket \Lambda^{0,2} M \rrbracket$$
where $\Lambda_{0}^{1,1} M$ is the sub-bundle of the primitive (1,1)-forms, i.e. the $J$-invariant 2-forms which are point-wise orthogonal to $\Omega$. The above splitting fits in with the well known $S O(4)$-decomposition of $\Lambda^{2} M$
$$\Lambda^{2} M=\Lambda^{+} M \oplus \Lambda^{-} M$$
into the sub-bundles $\Lambda^{ \pm} M$ of selfdual (resp. anti-selfdual) forms. Indeed, we have
$$\Lambda^{+} M=\mathbb{R} \cdot \Omega \oplus \llbracket \Lambda^{0,2} M \rrbracket, \quad \Lambda^{-} M=\Lambda_{0}^{1,1} M .$$
Note that $S_{\mathbb{R}}^{1,1} M$ can be identified with $\Lambda_{\mathbb{R}}^{1,1} M$ via the complex structure $J$ : for any $S \in$ $S_{\mathbb{R}}^{1,1} M$,
$$(S \circ J)(\cdot, \cdot):=S(J \cdot, \cdot)$$
is the corresponding element of $\Lambda_{\mathbb{R}}^{1,1} M$. Also, the real bundle $\llbracket \Lambda^{0,2} M \rrbracket$ (resp. $\llbracket S^{0,2} M \rrbracket$ ) inherits a canonical complex structure, still denoted by $J$, which is given by
$$(J \psi)(X, Y):=-\psi(J X, Y), \forall \psi \in \llbracket \Lambda^{0,2} M \rrbracket,$$
so that $\left(\llbracket \Lambda^{0,2} M \rrbracket, J\right)$ becomes isomorphic to the anti-canonical bundle $K_{J}^{-1}(M)$ of $M$. We adopt a similar definition for the action of $J$ on $\llbracket S^{0,2} M \rrbracket$. Notice that, using the metric $g$, $\llbracket S^{0,2} M \rrbracket$ can be also viewed as the bundle of symmetric, $J$-anti-commuting endomorphisms of $T M$.
2.2. The $U(2)$-decomposition of the curvature. The Riemannian curvature $R$ is defined by $R_{X, Y} Z=\left(\nabla_{[X, Y]}-\left[\nabla_{X}, \nabla_{Y}\right]\right) Z$, where ∇ is the Levi-Civita connection of $g$. Using the metric, it will be considered as a section of the bundle $S^{2}\left(\Lambda^{2} M\right)$ of symmetric endomorphisms of $\Lambda^{2} M$, or of the tensor product $\Lambda^{2} M \otimes \Lambda^{2} M$, depending on the context. The conformal part of $R$, the Weyl tensor $W$, commutes with the Hodge operator * acting on 2-forms and, accordingly, splits as $W=W^{+}+W^{-}$, where $W^{ \pm}=\frac{1}{2}(W \pm W \circ *) . W^{+}$is called the selfdual Weyl tensor; it acts trivially on $\Lambda^{-} M$ and will be considered in the sequel as a field of (symmetric, trace-free) endomorphisms of $\Lambda^{+} M$. Similarly, the anti-selfdual Weyl tensor, $W^{-}$, will be considered as a field of endomorphisms of $\Lambda^{-} M$.

The Ricci tensor, Ric, is the symmetric bilinear form defined by $\operatorname{Ric}(X, Y)=\operatorname{tr}\{Z \rightarrow$ $\left.R_{X, Z} Y\right\}$; alternatively, $\operatorname{Ric}(X, Y)=\sum_{i=1}^{4}\left\langle R_{X, e_{i}} Y, e_{i}\right\rangle$ for any $g$-orthonormal basis $\left\{e_{i}\right\}$. We then have $\operatorname{Ric}=\frac{s}{4} g+\operatorname{Ric}_{0}$, where $s$ is the scalar curvature (that is, the trace of Ric with respect to $g$ ) and Ric ${ }_{0}$ is the trace-free Ricci tensor. The latter can be made into a section of $S^{2}\left(\Lambda^{2} M\right)$, then denoted by $\widetilde{\operatorname{Ric}_{0}}$, by putting $\widetilde{\operatorname{Ric}_{0}}(X \wedge Y)=\operatorname{Ric}_{0}(X) \wedge Y+X \wedge \operatorname{Ric}_{0}(Y)$; equivalently, for any section $\phi$ of $\Lambda^{2} M$ we have
$$\widetilde{\operatorname{Ric}}_{0}(\phi)=\operatorname{Ric}_{0} \circ \phi+\phi \circ \operatorname{Ric}_{0} .$$
It is readily checked that $\widetilde{\mathrm{Ric}_{0}}$ satisfies the first Bianchi identity, i.e. $\widetilde{\mathrm{Ric}_{0}}$ is a tensor of the same kind as $R$ itself, as well as $W^{+}$and $W^{-}$; moreover, Ric $_{0}$ anti-commutes with *, so that it can be viewed as a field of homomorphisms from $\Lambda^{+} M$ into $\Lambda^{-} M$, or from $\Lambda^{-} M$ into $\Lambda^{+} M$ (adjoint to each other); we eventually get the well-known Singer-Thorpe decomposition of $R$, see e.g. [11]:
$$R=\left(\begin{array}{c|c}
W^{+}+\frac{s}{12} \mathrm{Id}_{\mid \Lambda+M} & \left(\frac{1}{2} \widetilde{\mathrm{Ric}_{0}}\right)_{\mid \Lambda-M} \\
\hline\left(\frac{1}{2} \widetilde{\mathrm{Ric}_{0}}\right)_{\mid \Lambda^{+} M} & W^{-}+\frac{s}{12} \mathrm{Id}_{\mid \Lambda^{-} M}
\end{array}\right) .$$

In the presence of a $g$-orthogonal almost complex structure $J$, which induces the chosen orientation of $M$, the above $S O(4)$-decomposition can be further refined to get seven irreducible $U(2)$-invariant pieces [47]. To see this, we first decompose the traceless Ricci tensor into its $J$-invariant and $J$-anti-invariant parts, $\operatorname{Ric}_{0}^{\prime}$ and Ric ${ }_{0}^{\prime \prime}=\operatorname{Ric}^{\prime \prime}$, which gives rise to the decomposition
$$\widetilde{\operatorname{Ric}_{0}}=\left(\widetilde{\operatorname{Ric}_{0}^{\prime}} \mid \widetilde{\operatorname{Ric}_{0}^{\prime \prime}}\right) .$$
We shall denote by $\rho$ the Ricci form of $(M, g, J)$, which is the (1,1)-form corresponding to $\operatorname{Ric}^{\prime}$ via $J$ (we thus have $\rho=\operatorname{Ric}^{\prime} \circ J$ ), and by $\rho_{0}=\operatorname{Ric}_{0}^{\prime} \circ J$ its primitive part.

Furthermore, with respect to (7), $W^{+}$decomposes as
$$W^{+}=\left(\begin{array}{c|c}
\frac{\kappa}{6} & W_{2}^{+} \\
\hline\left(W_{2}^{+}\right)^{*} & -\left.\frac{\kappa}{12} \operatorname{Id}\right|_{\llbracket \Lambda^{0,2} M \rrbracket}+W_{3}^{+}
\end{array}\right),$$
where:
\begin{itemize}
\item[-] the smooth function $\kappa$ is the so called conformal scalar curvature of $(g, J)$, defined by $\kappa=3\left\langle W^{+}(\Omega), \Omega\right\rangle$; thus, $\kappa$ is determined by the scale action of $W^{+}$on any of the two factor of (7).
\item[-] the component $W_{2}^{+}$is the piece of $W^{+}$that interchanges the two factors of (7); it thus can be seen as a section of $K_{J}^{-1}(M)$ by the following equality
$$W_{2}^{+}=\frac{1}{2}\left(\rho_{*}^{\prime \prime} \otimes \Omega+\Omega \otimes \rho_{*}^{\prime \prime}\right),$$
where $\rho_{*}^{\prime \prime}$ is the $J$-anti-invariant component of the so-called star-Ricci form $\rho_{*}=R(\Omega)$ of $(g, J)$; recall that the star-Ricci tensor Ric* is then defined by Ric* $(\cdot, \cdot)=-\rho_{*}(J \cdot, \cdot)$; in particular, $\rho_{*}^{\prime \prime}=0$ if and only if $W^{+}(\Omega)=\frac{\kappa}{6} \Omega$;
\item[-] the component $W_{3}^{+}$can be viewed as a section of $K_{J}^{-2}(M)$; with respect to any (local) section $\phi$ of $\llbracket \Lambda^{0,2} M \rrbracket$, it can be written as
$$W_{3}^{+}=\frac{\lambda}{2}[\phi \otimes \phi-J \phi \otimes J \phi]+\frac{\mu}{2}[\phi \otimes J \phi+J \phi \otimes \phi],$$
$\lambda$ and $\mu$ being (locally defined) smooth functions; equivalently, $W_{3}^{+}$is the component of $W^{+}$that belongs to the bundle of symmetric endomorphisms of $\llbracket \Lambda^{0,2} M \rrbracket$ which anti-commute with $J$.
\end{itemize}

We thus get the $U(2)$-splitting of the Riemannian curvature of an almost Hermitian 4manifold [47]:
$$R=\frac{s}{12} \operatorname{Id}_{\mid \Lambda^{2} M}+W_{1}^{+}+W_{2}^{+}+W_{3}^{+}+\widetilde{\operatorname{Ric}_{0}^{\prime}}+\widetilde{\operatorname{Ric}_{0}^{\prime \prime}}+W^{-},$$
where $W_{1}^{+}$denotes the scalar component of $W^{+}$, specifically given by
$$W_{1}^{+}=\frac{\kappa}{8} \Omega \otimes \Omega-\frac{\kappa}{12} \operatorname{Id}_{\mid \Lambda^{+} M} .$$

The following immediate application of the decomposition (10) provides alternative definitions (in dimension 4) for the third curvature condition of Gray (3):

Lemma 1. [47] For an almost Hermitian 4-manifold $(M, g, J)$ the following conditions are equivalent:
\begin{itemize}
\item[(i)] $\operatorname{Ric}^{\prime \prime}=0$ and $\rho_{*}^{\prime \prime}=0$.
\item[(ii)] $\operatorname{Ric}^{\prime \prime}=0$ and $W(\Omega)=\frac{\kappa}{6} \Omega$.
\item[(iii)] $\mathrm{Ric}^{*}-\mathrm{Ric}=\frac{(\kappa-s)}{6} g$.
\item[(iv)] $R_{X Y Z U}=R_{J X J Y J Z J U}$.
\item[(v)] $R$ preserves the type decomposition (with respect to $J$ ) of real 2-forms.
\end{itemize}
2.3. The Nijenhuis tensor and the curvature. A central object in our study is the Nijenhuis tensor (or complex torsion) of an almost complex structure $J$, defined by
$$N_{X, Y}=[J X, J Y]-J[J X, Y]-J[X, J Y]-[X, Y] .$$
Thus, $N$ is a 2-form with values in $T M$, which by Newlander-Nirenberg theorem [40] vanishes if and only if $J$ is integrable.

Alternatively, the Nijenhuis tensor can be viewed as a map from $\Lambda^{1,0} M$ to $\Lambda^{0,2} M$ in the following manner: given a complex $(1,0)$-form $\psi$, we define by $\partial \psi$ and $\bar{\partial} \psi$ the projectors of $d \psi$ to $\Lambda^{2,0} M$ and $\Lambda^{1,1} M$, respectively. In general, $d \neq \partial+\bar{\partial}$, as $d \psi$ can also have a component of type (0,2), which we denote by $N(\psi)$; writing $\psi=\alpha+i J \alpha$ where $\alpha$ is a real 1-form, one calculates
$$N(\psi)_{X, Y}=\frac{1}{2} \alpha\left(N_{X, Y}\right)=\frac{1}{4} \psi\left(N_{X, Y}\right), \quad \forall X, Y \in T^{0,1} M .$$

Equivalently, for every real 1-form $\alpha$ we have
$$\left(d^{J} \alpha\right)_{X, Y}^{\prime \prime}=\left(J(d \alpha)^{\prime \prime}\right)_{X, Y}+\frac{1}{2} J \alpha\left(N_{X, Y}\right),$$
where $d^{J}=i(\bar{\partial}-\partial)$; thus, $d^{J}$ acts on real functions by $d^{J} f=J d f$, on real 1-forms by $\left(d^{J} \alpha\right)_{X, Y}=-d(J \alpha)_{J X, J Y}$, etc. Observe that $d^{2}=0$ does not imply $d d^{J}+d^{J} d=0$, unless $N \equiv 0$. For example, using (12) one obtains on functions
$$\left(d d^{J}+d^{J} d\right) f=2\left(d d^{J} f\right)^{\prime \prime}=\left(d^{J} f\right)_{N(\cdot, \cdot)} .$$
In particular, $d d^{J} f$ is not, in general, a (1, 1)-form; however, for an almost Kähler manifold its projection to the $\Omega$-factor of (6) is a second order linear differential operator which, up to a sign, is nothing else than the Riemannian Laplacian of $(M, g)$ :
$$\Delta f=-\left\langle d d^{J} f, \Omega\right\rangle .$$

For an almost Kähler manifold $(M, g, J, \Omega)$, the vanishing of $N$ is equivalent to $\Omega$ being parallel with respect to the Levi-Civita connection ∇ of $g$; specifically, for any almost Kähler manifolds the following identity holds (cf. e.g. [30]):
$$\left(\nabla_{X} \Omega\right)(\cdot, \cdot)=\frac{1}{2}\langle J X, N(\cdot, \cdot)\rangle .$$
Using the above relation, we shall often think of $N$ as a $T^{*} M$-valued 2 -form, or as a $\Lambda^{2} M$ -valued 1-form, by tacitly identifying $N$ with $\nabla \Omega$. Further, since $\Omega$ is closed and $N$ is a $J$-anti-invariant 2 -form with values in $T M$, one easily deduces that $\nabla \Omega$ is, in fact, a section of the vector bundle $\llbracket \Lambda^{0,1} M \otimes \Lambda^{0,2} M \rrbracket$, i.e. the following relation holds:
$$\nabla_{J X} J=-J\left(\nabla_{X} J\right), \quad \forall X \in T M .$$
Note that, in four dimensions, any section of $\llbracket \Lambda^{0,1} M \otimes \Lambda^{0,2} M \rrbracket$ has a non-trivial kernel; then, at any point $x \in M$, we define the sub-space
$$D_{x}=\left\{X \in T_{x} M:\left(\nabla_{X} J\right)_{x}=0\right\},$$
which we call the Kähler nullity of $(g, J)$; thus, $\operatorname{dim}_{\mathbb{R}}(D)=4$ or 2, depending on whether or not $N$ vanishes at the given point. Assuming that $N \neq 0$, we let $D^{\perp}$ be the orthogonal complement of $D$ in $T M$. Relation (16) identifies the complex line bundle $D^{\perp}$ with the canonical bundle $K_{J}(M) \cong \Lambda^{2,0} M$; consequently, we have the following relations for the corresponding first Chern classes:
$$c_{1}\left(D^{\perp}\right)=-c_{1}(T M)=-c_{1}(J), \quad c_{1}(D)=c_{1}(T M)-c_{1}\left(D^{\perp}\right)=2 c_{1}(J) .$$
On the open subset of points where $N \neq 0$, we shall also consider the opposite almost complex structure $I$, which is equal to $J$ on $D$, but to $-J$ on $D^{\perp}$; clearly $I$ is compatible with the metric but yields the opposite orientation to the one of $(M, J)$. We mention below the following observation due to J. Armstrong [8] and C. LeBrun [38]:

Lemma 2. Let $(M, g, J, \Omega)$ be an almost-Kähler 4-manifold for which the Nijenhuis tensor nowhere vanishes. Then, the Chern classes of the almost complex structures $J$ and $I$ satisfy $c_{1}(I)=3 c_{1}(J)$; if, moreover, $M$ is compact, then the Euler characteristic $\chi(M)$ and signature $\sigma(M)$ of $M$ are related by $5 \chi(M)=-6 \sigma(M)$.

Proof. We clearly have
$$c_{1}(I)=c_{1}(D)-c_{1}\left(D^{\perp}\right)=3 c_{1}(J) .$$
By Wu's formula we know that $c_{1}^{2}(M, J)=2 \chi(M)+3 \sigma(M)$ and $c_{1}^{2}(M, I)=2 \chi(M)-3 \sigma(M)$, so that we get $-9(2 \chi(M)+3 \sigma(M))=2 \chi(M)-3 \sigma(M)$; the claim follows. □

For a Kähler structure $(g, J, \Omega)$ some of the curvature components defined in Section 2.2 identically vanish: indeed, in this case $\operatorname{Ric}^{\prime \prime}=0, W_{2}^{+}=0, W_{3}^{+}=0$ and the scalar function
$\kappa$ is nothing else than the scalar curvature $s$. This suggests that for an almost Kähler structure those components depend directly on the Nijenhuis tensor (and its covariant derivative). To see this, consider the Ricci identity for $\Omega$ :
$$\left(\nabla_{X, Y}^{2}-\nabla_{Y, X}^{2}\right)(\Omega)=\left[J, R_{X, Y}\right]$$
where $R_{X, Y}$ is viewed as an endomorphism of $T M$ and $[\cdot, \cdot]$ denotes the commutator. A contraction of this relation leads to
$$-\sum_{i=1}^{4}\left(\nabla_{e_{i}, Z}^{2} \Omega\right)\left(e_{i}, X\right)=\operatorname{Ric}(J X, Z)-\operatorname{Ric}^{*}(J X, Z) .$$
Symmetrising (18) in $X$ and $Z$, one obtains the relation between Ric'' and the Nijenhuis tensor:
$$\left(J \operatorname{Ric}^{\prime \prime}\right)_{X, Z}=\frac{1}{2} \sum_{i=1}^{4}\left(\left(\nabla_{e_{i}, Z}^{2} \Omega\right)\left(e_{i}, X\right)+\left(\nabla_{e_{i}, X}^{2} \Omega\right)\left(e_{i}, Z\right)\right) .$$
Anti-symmetrising (18) in $X$ and $Z$ and using $d \Omega=0$, one gets
$$\frac{1}{2} \nabla^{*} \nabla \Omega=\rho_{*}-\rho$$
which can be recognized as being nothing but the usual Weitzenböck formula [11] applied to the harmonic 2-form $\Omega$. From (19) we also get immediately
$$\begin{gathered}
2 \rho_{*}^{\prime \prime}=\left(\nabla^{*} \nabla \Omega\right)^{\prime \prime}, \quad \rho_{0}=\left(\rho_{*}^{\prime}\right)_{0} \text { and } \\
s^{*}-s=|\nabla \Omega|^{2}, \text { where } s^{*}=\frac{2 \kappa+s}{3}
\end{gathered}$$
is the trace of the star-Ricci tensor Ric*.
Finally, the component $W_{3}^{+}$is determined by the $\llbracket \Lambda^{0,2} M \rrbracket$-component of the relation (17).

As $\nabla \Omega$ is a section of the bundle $\llbracket \Lambda^{0,1} M \otimes \Lambda^{0,2} M \rrbracket$, it will be very convenient at times to express the higher jets of $\Omega$ in terms of a (local) section $\phi \in \llbracket \Lambda^{0,2} M \rrbracket$ of square-norm 2. Observe that we have an $S^{1}$-freedom for the choice of $\phi$ and, for this reason, such a form $\phi$ will be called a gauge.

Thus, assuming that we have made a choice for the gauge $\phi$, we can write:
$$\nabla \Omega=a \otimes \phi-J a \otimes J \phi .$$
The gauge-dependent 1-form $a$ is dual to a vector field in $D^{\perp}$ and satisfies $|\nabla \Omega|^{2}=4|a|^{2}$, which shows that $|a|^{2}$ is a gauge-independent quantity. As $\left\{\frac{1}{\sqrt{2}} \Omega, \frac{1}{\sqrt{2}} \phi, \frac{1}{\sqrt{2}} J \phi\right\}$ is an orthonormal basis of $\Lambda^{+} M$, the covariant derivatives of $\phi$ and $J \phi$ are given by
$$\nabla \phi=-a \otimes \Omega+b \otimes J \phi ; \quad \nabla J \phi=J a \otimes \Omega-b \otimes \phi,$$
for some gauge-dependent 1-form $b$. In fact, if we change the gauge by
$$\phi^{\prime}=(\cos \theta) \phi+(\sin \theta) J \phi,$$
the corresponding 1-forms change as follows
$$a^{\prime}=(\cos \theta) a-(\sin \theta) J a ; b^{\prime}=b+d \theta .$$
From (21) and (22), we get
$$\left.\nabla^{2}\right|_{\Lambda^{2} M} \Omega=(d a-J a \wedge b) \otimes \phi-(d(J a)+a \wedge b) \otimes J \phi,$$
so, the Ricci identity for $\Omega$, (17), can be rewritten as
$$d a-J a \wedge b=-R(J \phi) ; d(J a)+a \wedge b=-R(\phi) .$$

From the Ricci identity for $\phi$
$$\left(\nabla_{X, Y}^{2}-\nabla_{Y, X}^{2}\right)(\phi)=\left[\phi, R_{X, Y}\right]$$
after using (21) and (22), one gets the gauge independent relation
$$d b=a \wedge J a-R(\Omega)=a \wedge J a-\rho_{*} .$$
Note that the closed, gauge independent 2-form
$$\gamma_{J}=-d b=R(\Omega)-a \wedge J a$$
is a deRham representative of $2 \pi c_{1}(M, J)$, calculated with respect to the first canonical connection of $(M, g, J)$
$$\nabla_{X}^{1} Y=\nabla_{X} Y-\frac{1}{2} J\left(\nabla_{X} J\right)(Y),$$
see e.g. [21]. We shall refer to $\gamma_{J}$ as the canonical Chern form of $(M, g, J)$.
2.4. The differential Bianchi identity for almost Kähler 4-manifolds. For a Riemannian 4-manifold ( $M, g$ ) the differential Bianchi identity can be written as $\delta W=C$, where $W$ is the Weyl tensor, $C$ denotes the Cotton-York tensor of $(M, g)$ and the codifferential $\delta$ acts on $W$ as on a $\Lambda^{2} M$-valued 2-form. Recall that $C$ is defined by
$$C_{X, Y, Z}=-\left(d^{\nabla} h\right)(X, Y, Z)=-\left(\nabla_{X} h\right)(Y, Z)+\left(\nabla_{Y} h\right)(X, Z),$$
where $h=\frac{1}{2}$ Ric $_{0}+\frac{s}{24} g$ denotes the normalized Ricci tensor and $d^{\nabla}$ is the Riemannian differential acting on $T^{*} M$ valued 1-forms. Both $\delta W$ and $C$ are sections of the bundle $\Lambda^{1} M \otimes \Lambda^{2} M$ and because of the splitting $\Lambda^{2} M=\Lambda^{+} M \oplus \Lambda^{-} M$, the differential Bianchi identity splits in two halves, self-dual and anti-self-dual:
$$\delta W^{+}=C^{+}, \quad \delta W^{-}=C^{-},$$
where the ±-superscript denotes the self-dual, resp. anti-self-dual component of the corresponding tensor. We would like to express the above formulae in terms of the various $U(2)$ curvature components of an almost Kähler 4-manifold $(M, g, J, \Omega)$. We start with the Cotton-York tensor $C$.

Contracting the differential Bianchi identity $\delta W=C$, we obtain
$$\delta\left(\operatorname{Ric}_{0}-\frac{s}{4} g\right)=0$$
and this, together with the fact that the fundamental form $\Omega$ is harmonic, implies:
$$-\delta\left(\rho_{0}-\frac{s}{4} \Omega\right)=J \delta\left(\operatorname{Ric}^{\prime \prime}\right) .$$
Taking the Hodge star operator of both sides, the above relation is equivalent to
$$d \rho=*\left(J \delta \operatorname{Ric}^{\prime \prime}\right) .$$
In particular, if Ric" $=0$, then $\rho$ is closed [19].
For a given vector field $Z$, we denote by $C_{Z}$ the section of $\Lambda^{2} M$, defined by $C_{Z}(X, Y):=$ $C(X, Y, Z)$, and similarly we define $C_{Z}^{+}$and $C_{Z}^{-}$. Denote also by $A_{Z}$ the $\Lambda^{2} M$-valued 1-form given by
$$A_{Z}=\left(d^{\nabla} \operatorname{Ric}^{\prime \prime}\right)_{Z}+\iota_{J Z}(d \rho),$$
where $\iota$ stands for interior derivative, and let $A_{Z}^{ \pm}$be the self-dual and anti-self-dual components of $A_{Z}$.

Lemma 3. Let ( $M, g, J, \Omega$ ) be an almost Kähler 4-manifold. Then, for any vector field $Z$, the Cotton-York tensor $C_{Z}$ is given by
$$2 C_{Z}=\nabla_{J Z} \rho_{0}-\frac{1}{4}\left(\left(d^{J} s\right)_{Z}\right) \Omega+\nabla_{\rho_{0}(Z)} \Omega+\frac{1}{6} d s \wedge Z^{b}-A_{Z}$$
where $Z^{b}$ denotes the $g$-dual 1-form of $Z$.
Proof. Since $h=\frac{1}{2}$ Ric $-\frac{s}{12} g$, the Cotton-York tensor is written as:
$$C_{Z}=-\frac{1}{2}\left(d^{\nabla} \operatorname{Ric}^{\prime \prime}\right)_{Z}-\frac{1}{2}\left(d^{\nabla} \operatorname{Ric}^{\prime}\right)_{Z}+\frac{1}{12} d s \wedge Z^{b} .$$
Taking into account that $\rho(\cdot, \cdot)=\operatorname{Ric}^{\prime}(J \cdot, \cdot)$, we have
$$\begin{aligned}
\left(d^{\nabla} \operatorname{Ric}^{\prime}\right)(X, Y, Z) & =\left(\nabla_{X} \operatorname{Ric}^{\prime}\right)(Y, Z)-\left(\nabla_{Y} \operatorname{Ric}^{\prime}\right)(X, Z) \\
& =\left(d^{\nabla} \rho\right)(X, Y, J Z)+\left(\rho\left(Y,\left(\nabla_{X} J\right) Z\right)-\rho\left(X,\left(\nabla_{Y} J\right) Z\right)\right) .
\end{aligned}$$
For the term $d^{\nabla} \rho$ we have
$$\begin{aligned}
\left(d^{\nabla} \rho\right)(X, Y, J Z) & =\left(\nabla_{X} \rho\right)(Y, J Z)-\left(\nabla_{Y} \rho\right)(X, J Z) \\
& =-\left(\nabla_{J Z} \rho\right)(X, Y)+(d \rho)(X, Y, J Z) \\
& =-\left(\nabla_{J Z} \rho\right)(X, Y)+\iota_{J Z}(d \rho)(X, Y) .
\end{aligned}$$

To refine the last term of (29), note that as an algebraic object, $\nabla_{X} J$ is a skew-symmetric endomorphism of $T M$, associated (by $g$-duality) to the section $\nabla_{X} \Omega$ of the bundle $\llbracket \Lambda^{0,2} M \rrbracket$. Thus $\nabla_{X} J$ anti-commutes with $J$, and commutes with any skew-symmetric endomorphism associated to a section of $\Lambda^{-} M$; in particular, it commutes with the endomorphism corresponding to $\rho_{0}$ via the metric (which will be still denoted by $\rho_{0}$ ). We thus obtain
$$\begin{aligned}
\rho\left(Y,\left(\nabla_{X} J\right)(Z)\right)- & \rho\left(X,\left(\nabla_{Y} J\right)(Z)\right)=\frac{s}{4}\left(\left(\nabla_{Y} \Omega\right)(X, J Z)-\left(\nabla_{X} \Omega\right)(Y, J Z)\right) \\
& +\left(\nabla_{X} \Omega\right)\left(Y, \rho_{0}(Z)\right)-\left(\nabla_{Y} \Omega\right)\left(X, \rho_{0}(Z)\right) \\
& =\frac{s}{4}\left(\nabla_{J Z} \Omega\right)(X, Y)-\left(\nabla_{\rho_{0}(Z)} \Omega\right)(X, Y),
\end{aligned}$$
where for the last equality we used the closedness of $\Omega$.
Substituting (30) and (31) in (29), we get
$$\begin{aligned}
\left(d^{\nabla} \text { Ric }^{\prime}\right)_{Z}= & -\nabla_{J Z} \rho_{0}-\nabla_{\rho_{0}(Z)} \Omega \\
& +\frac{1}{4}\left(\left(d^{J} s\right)_{Z}\right) \Omega+\iota_{J Z}(d \rho) .
\end{aligned}$$
From (28) and (32), we obtain relation (27) claimed in the statement. □
Lemma 4. Let $(M, g, J, \Omega)$ be an almost Kähler 4-manifold. Then the differential Bianchi identities $\delta W^{+}=C^{+}, \delta W^{-}=C^{-}$are equivalent to:
$$\begin{aligned}
0= & -\frac{1}{4}\left(d^{J}(\kappa-s)\right)_{Z} \Omega+\frac{1}{6}\left(d(\kappa-s) \wedge Z^{b}\right)^{+}+\left(\delta \rho_{*}^{\prime \prime}\right)_{Z} \Omega \\
& +\frac{\kappa}{4} \nabla_{J Z} \Omega-\nabla_{\rho_{0}(Z)} \Omega+\nabla_{\rho_{*}^{\prime \prime}(Z)} \Omega+\nabla_{J Z} \rho_{*}^{\prime \prime}+2\left(\delta W_{3}^{+}\right)_{Z}+A_{Z}^{+} ; \\
0= & \nabla_{J Z} \rho_{0}+\frac{1}{6}\left(d s \wedge Z^{b}\right)^{-}-2 \delta W_{Z}^{-}-A_{Z}^{-} .
\end{aligned}$$
Proof. Relation (34) follows from $\delta W^{-}=C^{-}$by simply taking the anti-self-dual component of (27). Similarly, for (33) we take the self-dual component of (27), but we also use the relations
$$\left(\delta W_{1}^{+}\right)_{Z}=-\frac{1}{8}\left(d^{J} \kappa\right)_{Z} \Omega+\frac{\kappa}{8} \nabla_{J Z} \Omega+\frac{1}{12}\left(d \kappa \wedge Z^{b}\right)^{+},$$
$$\left(\delta W_{2}^{+}\right)_{Z}=\frac{1}{2} \nabla_{J Z}\left(\rho_{*}\right)^{\prime \prime}+\frac{1}{2} \nabla_{\left(\rho_{*}\right)^{\prime \prime}(Z)} \Omega+\frac{1}{2}\left(\delta \rho_{*}^{\prime \prime}\right)(Z) \Omega,$$
which easily follow from (11) and (8). □
It will be useful to further determine the $\Omega$-component and the $\llbracket \Lambda^{0,2} M \rrbracket$-component of (33) in accordance with the decomposition (7) of $\Lambda^{+} M$. These are given by

Corollary 1. For any almost Kähler 4-manifold the following identities hold:
$$\begin{aligned}
0 & =-\frac{1}{3}\left(d^{J}(\kappa-s)\right)_{Z}+2\left\langle\left(\delta W_{3}^{+}\right)_{Z}, \Omega\right\rangle \\
& +2\left(\delta \rho_{*}^{\prime \prime}\right)_{Z}-\left\langle\rho_{*}^{\prime \prime}, \nabla_{J Z} \Omega\right\rangle+\left\langle A_{Z}^{+}, \Omega\right\rangle \\
0= & \frac{1}{6}\left(d(\kappa-s) \wedge Z^{b}\right)^{\prime \prime}+\frac{\kappa}{4} \nabla_{J Z} \Omega-\nabla_{\rho_{0}(Z)} \Omega+2\left(\delta W_{3}^{+}\right)_{Z}^{\prime \prime} \\
& +\nabla_{\rho_{*}^{\prime \prime}(Z)} \Omega+\left(\nabla_{J Z} \rho_{*}^{\prime \prime}\right)^{\prime \prime}+\left(A_{Z}^{+}\right)^{\prime \prime}
\end{aligned}$$
2.5. A Weitzenböck formula and unique continuation of the Nijenhuis tensor. Recall that the weak unique continuation property for a map $u: M \rightarrow E$ between connected Riemannian manifolds, $M$ and $E$, says that if $u$ is a constant map on an open subset $U \subset M$, then $u$ is constant everywhere; for the strong unique continuation property, the condition that $u$ is constant on an open subset is replaced with the assumption that at a given point, $u$ has a contact of infinite order with the constant map (see e.g. [29]).

In this subsection we shall show that the (strong) unique continuation property holds for the Nijenhuis tensor of an almost Kähler 4-manifold which satisfies certain curvature conditions. In fact, we shall concentrate our attention on $\nabla \Omega$, which is identified to the Nijenhuis tensor via (15). As typically happens in Riemannian geometry, the unique continuation property appears as a consequence of a Weitzenböck formula. In our case, we shall use a general Weitzenböck formula of Bourguignon [14] applied to $\nabla \Omega$, seen as a section of the bundle of $\Lambda^{2} M$-valued 1-forms. The role of the "constant map" in this setting is played by the zero section.

Proposition 1. Let $(M, g, J, \Omega)$ be an almost Kähler 4-manifold whose curvature satisfies the third Gray condition (3). Then, the following identity holds:
$$\nabla^{*} \nabla(\nabla \Omega)+\frac{3 s}{4} \nabla \Omega+\nabla_{\operatorname{Ric}_{0}(\cdot)} \Omega=0,$$
In particular, if $M$ is connected, then the (strong) unique continuation property holds for $\nabla \Omega$ (hence for the Nijenhuis tensor $N$ as well).

Proof: We shall in fact establish a formula for $\nabla^{*} \nabla(\nabla \Omega)$ on an arbitrary almost Kähler 4-manifold, and then relation (39) will be an immediate consequence. The starting point is the general Weitzenböck formula for a $\Lambda^{2} M$-valued 1-form $V$ (e.g. see [14], p.282):
$$\left(\left(d^{\nabla} \delta^{\nabla}+\delta^{\nabla} d^{\nabla}\right) V\right)_{X}=\left(\nabla^{*} \nabla V\right)_{X}+V_{\operatorname{Ric}(X)}+(R \cdot V)_{X} .$$
In the above formula
\begin{itemize}
\item[-] $d^{\nabla}$ is the Riemannian differential acting on $\Lambda^{2} M$-valued $k$-forms;
\item[-] $\delta^{\nabla}$ is the formal adjoint of $d^{\nabla}$;
\item[-] the curvature action is given by:
$$(R \cdot V)_{X}=\sum_{i=1}^{4}\left[R_{X, e_{i}}, V_{e_{i}}\right]$$
\end{itemize}
where $\left\{e_{1}, \ldots, e_{4}\right\}$ is an orthonormal basis of $T M$, the 2-forms $R_{X, e_{i}}, V_{e_{i}}$ are freely identified with the corresponding skew-symmetric endomorphism of $T M$ and $[\cdot, \cdot]$ denotes the commutator. We apply (40) to $V=\nabla \Omega$; using (19), (20) and (17) we get
$$\begin{aligned}
\delta^{\nabla}(\nabla \Omega) & =\nabla^{*} \nabla \Omega=2\left(\rho_{*}-\rho\right)=2 \rho_{*}^{\prime \prime}+\frac{(\kappa-s)}{3} \Omega, \\
\left(d^{\nabla}(\nabla \Omega)\right)_{X, Y} & =\left(\nabla_{X, Y}^{2} \Omega\right)-\left(\nabla_{Y, X}^{2} \Omega\right)=\left[J, R_{X, Y}\right] .
\end{aligned}$$
From (41) we derive immediately
$$\left(d^{\nabla} \delta^{\nabla}(\nabla \Omega)\right)_{X}=2 \nabla_{X} \rho_{*}^{\prime \prime}+\frac{1}{3} d(\kappa-s)_{X} \Omega+\frac{(\kappa-s)}{3} \nabla_{X} \Omega,$$
whereas a short computation starting from (42) leads to
$$\left(\delta^{\nabla} d^{\nabla}(\nabla \Omega)\right)_{X}=-(R \cdot(\nabla \Omega))_{X}+\left(\left(\nabla_{e_{i}} R\right)_{e_{i}, X}(J \cdot, \cdot)+\left(\nabla_{e_{i}} R\right)_{e_{i}, X}(\cdot, J \cdot)\right) .$$
Using the differential Bianchi identity and (32), we get
$$\begin{aligned}
\left(\left(\nabla_{e_{i}} R\right)_{e_{i}, X}(J \cdot, \cdot)\right. & \left.+\left(\nabla_{e_{i}} R\right)_{e_{i}, X}(\cdot, J \cdot)\right)=\left(d^{\nabla} \operatorname{Ric}\right)_{X}(J \cdot, \cdot)+\left(d^{\nabla} \operatorname{Ric}\right)_{X}(\cdot, J \cdot) \\
& =A_{X}(J \cdot, \cdot)+A_{X}(\cdot, J \cdot)+2\left(\nabla_{\operatorname{Ric}_{0}^{\prime}(X)} \Omega\right)(\cdot, \cdot) \\
& =-2\left(J\left(A_{X}^{+}\right)^{\prime \prime}\right)(\cdot, \cdot)+2\left(\nabla_{\operatorname{Ric}_{0}^{\prime}(X)} \Omega\right)(\cdot, \cdot) .
\end{aligned}$$
From the relations (43-45) and (40), we obtain
$$\begin{aligned}
\nabla^{*} \nabla(\nabla \Omega)= & 2 \nabla \rho_{*}^{\prime \prime}-2 J\left(A^{+}\right)^{\prime \prime}-\nabla_{\operatorname{Ric}(\cdot)} \Omega \\
& -2 R \cdot(\nabla \Omega)+2 \nabla_{\operatorname{Ric}_{0}^{\prime}(\cdot)} \Omega+\frac{1}{3} d(\kappa-s) \otimes \Omega+\frac{(\kappa-s)}{2} \nabla \Omega .
\end{aligned}$$
It remains to detail the expression of the term $R \cdot(\nabla \Omega)$. For this, we shall use the $U(2)$ decomposition of the curvature (10) and compute the action of each component on $\nabla \Omega$. It is clear that the action of $W^{-}$is zero, and for the action of the component $\widetilde{\operatorname{Ric}_{0}^{\prime \prime}}$ we will not attempt to do any simplification, as $\mathrm{Ric}_{0}^{\prime \prime}=0$ for almost Kähler 4-manifolds satisfying (3). For the other components though, from their definitions (see (11), (8), (9)), one computes successively:
$$\begin{aligned}
\left(\frac{s}{12} \operatorname{Id}_{\mid \Lambda^{2} M} \cdot(\nabla \Omega)\right)_{X} & =\frac{s}{12}\left(\nabla_{X} \Omega\right) ; \\
\left(W_{1}^{+} \cdot(\nabla \Omega)\right)_{X} & =\frac{\kappa}{6}\left(\nabla_{X} \Omega\right) ; \\
\left(W_{2}^{+} \cdot(\nabla \Omega)\right)_{X} & =-\left(\nabla_{J \rho_{*}^{\prime \prime}(X)} \Omega\right)-\frac{1}{2}\left\langle\rho_{*}^{\prime \prime}, \nabla_{X} \Omega\right\rangle \Omega ; \\
\left(W_{3}^{+} \cdot(\nabla \Omega)\right)_{X} & =\left\langle\left(\delta W_{3}^{+}\right)_{J X}, \Omega\right\rangle \Omega ; \\
\left(\widetilde{\operatorname{Ric}}_{0}^{\prime} \cdot(\nabla \Omega)\right)_{X} & =\nabla_{\operatorname{Ric}_{0}^{\prime}(X)} \Omega .
\end{aligned}$$
Finally, using the relations above, back in (46), we obtain:
$$\begin{aligned}
\left(\nabla^{*} \nabla(\nabla \Omega)\right)_{X}= & -\nabla_{\operatorname{Ric}_{0}^{\prime}(X)} \Omega-\frac{3 s}{4} \nabla_{X} \Omega \\
& +\left(\frac{1}{3} d(\kappa-s)_{X}-2\left\langle\left(\delta W_{3}^{+}\right)_{J X}, \Omega\right\rangle\right) \Omega \\
& +2\left(\nabla_{X} \rho_{*}^{\prime \prime}\right)^{\prime \prime}+2 \nabla_{J \rho_{*}^{\prime \prime}(X)^{\Omega}} \\
& -\nabla_{\operatorname{Ric}_{0}^{\prime \prime}(X)} \Omega-2 J\left(A_{X}\right)^{\prime \prime}-2\left(\widetilde{\operatorname{Ric}}_{0}^{\prime \prime} \cdot(\nabla \Omega)\right)_{X} .
\end{aligned}$$

For an almost Kähler 4-manifold which satisfies the third Gray condition, the terms in the last two lines of the above equation all vanish, as they contain Ric ${ }^{\prime \prime}$ and $\rho_{*}^{\prime \prime}$, see Lemma 1. In fact, the expression of the second line is also 0, as a consequence of the Bianchi relation (37). Thus, under the assumption $\mathrm{Ric}^{\prime \prime}=0 \& \rho_{*}^{\prime \prime}=0$, the general formula (47) reduces to (39); the fact that the relation (39) implies the (strong) unique continuation property for $\nabla \Omega$ (and therefore also for the Nijenhuis tensor $N$ ), follows from the classical result of Aronszajn [7]. □

Remark 1. (i) Note that solely for the purpose of getting the unique continuation property for $\nabla \Omega$, we need not make the effort to compute the action of each of the curvature components on $\nabla \Omega$. Indeed, to apply the result of Aronszajn [7], it is enough to obtain an estimate of the form
$$\left|\nabla^{*} \nabla(\nabla \Omega)\right|^{2} \leq M\left(|\nabla(\nabla \Omega)|^{2}+|\nabla \Omega|^{2}\right),$$
and relation (46) already implies such an estimate, once we also note that
$$\frac{2}{3}|d(\kappa-s)|=\left|d\left(|\nabla \Omega|^{2}\right)\right| \leq 2|\nabla(\nabla \Omega)||\nabla \Omega|=\frac{4}{3}(\kappa-s)|\nabla(\nabla \Omega)| .$$
More generally, from (47) (or equally well from (46)), one can deduce that the (strong) unique continuation property for $\nabla \Omega$ holds for almost Kähler 4-manifolds for which two of the three tensors, $\operatorname{Ric}^{\prime \prime}, \rho_{*}^{\prime \prime}$, and $W_{3}^{+}$vanish. Indeed, in the case when $\rho_{*}^{\prime \prime}=0 \& W_{3}^{+}=0$, the differential Bianchi identity (38) can be written as
$$-\left(A_{Z}^{+}\right)^{\prime \prime}=\frac{1}{6}\left(d(\kappa-s) \wedge Z^{b}\right)^{\prime \prime}+\frac{\kappa}{4} \nabla_{J Z} \Omega-\nabla_{\rho_{0}(Z)} \Omega .$$
Putting the above relation back in (46), one again obtains the needed estimate to apply [7]. One can proceed similarly in the case $\mathrm{Ric}^{\prime \prime}=0 \& W_{3}^{+}=0$. In fact, in this latter case, employing a different estimate, it was shown in [2] that an even stronger version of the unique continuation property of $\nabla \Omega$ holds; namely, if $\nabla \Omega$ vanishes at one point, then it must be identically zero.
(ii) One would expect formula (47) to eventually lead to the integrability of compact almost Kähler 4-manifolds satisfying certain curvature conditions. This is indeed the case: along these lines it was proved in [20] that on a compact symplectic 4-manifold there are no critical, strictly almost Kähler structures of everywhere non-negative scalar curvature.

\section*{3. The examples of almost Kähler 4-manifolds satisfying the third Gray CONDITION}

We give here more details about the explicit construction given in Theorem 1; the material in this section has appeared in [3].

Let $\left(\Sigma, g_{\Sigma}\right)$ be any oriented Riemann surface and $h=w+i v$ be a holomorphic function on $\Sigma$, such that $w=\mathfrak{R e}(h)$ is a positive (harmonic) function on $\Sigma$. We can then locally write the metric $g_{\Sigma}$ as
$$g_{\Sigma}=e^{u} w\left(d x^{\otimes 2}+d y^{\otimes 2}\right),$$
where $x, y$ are (local) isotherm coordinates of $\left(\Sigma, g_{\Sigma}\right)$ and $u$ is a function on $\Sigma$. We consider the metric
$$\begin{aligned}
g & =g_{\Sigma}+w d z^{\otimes 2}+\frac{1}{w}(d t+v d z)^{\otimes 2} \\
& =e^{u} w\left(d x^{\otimes 2}+d y^{\otimes 2}\right)+w d z^{\otimes 2}+\frac{1}{w}(d t+v d z)^{\otimes 2}
\end{aligned}$$
defined on $M=\Sigma \times \mathbb{R}^{2}$, where $(z, t)$ are the canonical coordinates of $\mathbb{R}^{2}$. Clearly, $K_{1}=$ $\frac{\partial}{\partial z}$ and $K_{2}=\frac{\partial}{\partial t}$ are two commuting Killing fields, so that $g$ is an $\mathbb{R}^{2}$-invariant metric compatible with the product structure in the sense of [28].

As observed in [35], the metric (48) carries a compatible Kähler structure, $I$, whose fundamental form is
$$\bar{\Omega}=\Omega_{\Sigma}+d z \wedge(d t+v d z)=\left(e^{u} w\right) d x \wedge d y+d z \wedge d t,$$
where $\Omega_{\Sigma}$ denotes the volume form of $\left(\Sigma, g_{\Sigma}\right)$. Equivalently, $I$ is defined by its action on 1-forms:
$$I(d x)=d y ; I(d z)=\frac{1}{w}(d t+v d z)$$
Thus, $I$ is compatible with the product structure as well, and induces an orientation on $M$ and on each of the factors $\Sigma$ and $\mathbb{R}^{2}$. Besides $I$, one can consider the almost complex structure $J$, which coincides with $I$ on $\Sigma$, but which is equal to $-I$ on $\mathbb{R}^{2}$, i.e.
$$J(d x)=d y ; J(d z)=-\frac{1}{w}(d t+v d z) .$$
Thus, $J$ is compatible with $g$ and yields on $M$ the orientation opposite to the one induced by $I$. Furthermore, the fundamental form of $J$ is given by
$$\Omega=\Omega_{\Sigma}-d z \wedge(d t+v d z)=\Omega_{\Sigma}-d z \wedge d t$$
and is clearly closed, meaning that $(g, J)$ is an almost Kähler structure. It is easily seen that $J$ is integrable (i.e. $(g, J)$ is Kähler ) if and only if $h$ is constant (i.e. $g$ is a product metric), a possibility which we exclude in what follows below.

An important feature of the construction comes from the following observation: at any point where $d w \neq 0$, the Kähler nullity $D=\left\{T M \ni X: \nabla_{X} J=0\right\}$ of $J$ is a two dimensional subspace of $T M$, which is tangent to the surface $\Sigma$ (see [3]); thus, the Kähler structure $I$ and the almost Kähler structure $J$ are equivalently related by
$$J_{D}=I_{D} \quad J_{D^{\perp}}=-I_{D^{\perp}} .$$

The almost Kähler structure $(g, J, \Omega)$ is sufficiently explicit to make it straightforward, though tedious, to check that its curvature satisfies the third Gray condition (3); see our previous paper [3] for detailed calculations. But the heart of [3] consists of the following abstract characterization of the almost Kähler structures given by (48-50):

Theorem 3. [3, Theorem 2] Let $(M, g, J, \Omega)$ be a strictly almost Kähler 4-manifold whose curvature satisfies (3). At each point $x \in M$ where the Nijenhuis tensor of $J$ does not vanish, consider the orthogonal almost complex structure $I$ which is equal to $J$ on the Kähler nullity $D_{x} \subset T_{x} M$, but to $-J$ on the orthogonal complement of $D_{x}$. If we suppose that $(g, I)$ is Kähler on an open subset $U$, then for every sufficiently small neighborhood of $x \in U,(g, J, I)$ is given by (48-50), up to a homothety.

The key point for obtaining the above result in [3] was to show that the distribution $D^{\perp}$ is (locally) spanned by commuting hamiltonian Killing fields, a subject to a straightforward verification of the integrability condition of a relevant Frobenius system; then, according to [35], the Kähler metric ( $g, I$ ) can be put (locally) in the form (48-49) and Theorem 3 follows easily.

On the other hand, it was shown in [9] that when $(g, J)$ is an Einstein, strictly almost Kähler structure satisfying (3), $(g, I)$ is necessarily Kähler ; the same was later established for strictly almost Kähler 4-manifolds satisfying the second curvature condition of Gray (see [3]). In the next section we generalize these results.

\section*{4. Proof of Theorem 1}

The following proposition, which via Proposition 1 and Theorem 3 implies Theorem 1, is the technical core of the present paper.

Proposition 2. Let $(M, g, J, \Omega)$ be a strictly almost Kähler 4-manifold satisfying the third Gray condition (3) and let $(g, I)$ be the opposite almost Hermitian structure associated to $(g, J)$ as in Theorem 3. Then, on the open set $U \subset M$, where $|\nabla J| \neq 0,(g, I)$ is a Kähler structure.

There are three main steps in the proof, corresponding roughly to Lemmas 5, 6 and 7 below. In Lemma 5, we first establish that under the third Gray condition (3) for $(g, J)$, the opposite almost Hermitian structure $(g, I)$ is almost Kähler and we specifically find, in accordance with Lemma 2, the exact form representing the difference $\gamma_{I}-3 \gamma_{J}$, where $\gamma_{J}$ and $\gamma_{I}$ are the canonical Chern forms of $(g, J)$ and $(g, I)$ respectively (see Section 2.3). Under the second Gray condition studied in [3], or with the Einstein assumption made in [9], Lemma 5 is essentially enough to obtain that $(g, I)$ is Kähler. Assuming the (weaker) third Gray condition only, the same conclusion is still true, but not so immediate. The idea of the proof is to proceed by contradiction, thus assuming that $(g, I)$ is not Kähler and to try to iterate the construction. This is somehow complicated by the fact that, a priori, $(g, I)$ does not satisfy the third Gray condition (3). Nevertheless, in Lemma 6 we show that the curvature has the necessary features to allow the iteration of the construction. The last step is essentially done in Lemma 7: We consider $(g, \tilde{J})$, the opposite almost Hermitian structure associated to $(g, I)$ and, analogously to Lemma 5, we get an explicit expression for the exact form representing $\gamma_{\tilde{J}}-3 \gamma_{I}$, where $\gamma_{\tilde{J}}$ denotes the canonical Chern form of $(g, \tilde{J})$. But one immediately notices that, in view of Lemma 5, the "opposite of the opposite" almost complex structure $\tilde{J}$ is nothing else than $-J$, hence we also have $\gamma_{\tilde{J}}=-\gamma_{J}$. Therefore, the expression for $\gamma_{\tilde{J}}-3 \gamma_{I}$ obtained in Lemma 7 provides another relation between $\gamma_{J}$ and $\gamma_{I}$, different than the one obtained in Lemma 5 (see also Lemma 2). The combination of the two leads to the desired contradiction.

This is the outline of the proof of Proposition 2. Before we proceed to detail each of the three mentioned steps, let us first recall some notations from Section 2 and introduce some new ones, for convenience. As mentioned in Section 2.3, it is useful to make computations using a gauge $\phi$; recall that $\phi$ is a local section of norm $\sqrt{2}$ of the bundle $\llbracket \Lambda^{0,2} M \rrbracket$. We thus choose an arbitrary gauge $\phi$ and fix it. By formulae (21) and (22), we define the local 1-forms $a$ and $b$ corresponding to $\phi$. We shall denote the (local) endomorphisms of $T M$ induced by $\phi$ and $J \phi$ by $J_{1}$ and, respectively, $J_{2}$; note that the triple $\left(J, J_{1}, J_{2}=J J_{1}\right)$ is a local almost quaternionic structure on the manifold. We also make the convention to denote a tensor (or form) defined by the opposite almost complex structure $(g, I)$ with the same symbol as the corresponding one defined by $(g, J)$, but with a "bar" sign on top. Thus, for instance, the fundamental form of $(g, I)$ is denoted by $\bar{\Omega}$, the Ricci form of $(g, I)$ by $\bar{\rho}$, etc.

Because of the existence of the opposite almost Hermitian structure $(g, I)$, the decomposition (6) of the bundle of 2-forms further refines to:
$$\Lambda^{2} M=\mathbb{R} \cdot \Omega \oplus \llbracket \Lambda_{J}^{0,2} M \rrbracket \oplus \mathbb{R} \cdot \bar{\Omega} \oplus \llbracket \Lambda_{I}^{0,2} M \rrbracket$$
where $\llbracket \Lambda_{J}^{0,2} M \rrbracket, \llbracket \Lambda_{I}^{0,2} M \rrbracket$ denote the underlying real bundles of the anti-canonical bundles of $(g, J),(g, I)$, respectively. We shall keep the convention made earlier to use the superscripts ${ }^{\prime}$ and " for the $J$-invariant, respectively, $J$-anti-invariant parts of a 2-form, or symmetric 2-tensor. But we shall need occasionally to also consider $\llbracket \Lambda_{I}^{0,2} M \rrbracket$-components of 2-forms and we make the convention to use the notation $(\cdot)_{I}^{\prime \prime}$ for this. Thus, for instance, $\left(\bar{\rho}_{*}\right)_{I}^{\prime \prime}$ will
denote the $\llbracket \Lambda_{I}^{0,2} M \rrbracket$-component of the $*$-Ricci form $\bar{\rho}_{*}$ of $(g, I)$. In addition to $d^{J}$, we shall also use $d^{I}$, the complex differential with respect to $I$, acting on functions by $d^{I} f=I d f$ (see Sec. 2.3).

The Lemma below was essentially proved in our previous work [3].
Lemma 5. Let $(M, g, J, \Omega)$ be a strictly almost Kähler 4-manifold satisfying (3). Then, on the open set $U$ where $N \neq 0$, the Kähler nullity $D$ of $(g, J)$, and its orthogonal complement, $D^{\perp}$, are both involutive distributions. Furthermore, on $U,(g, I)$ is an almost Kähler structure and the Kähler nullity of $(g, I)$ contains the distribution $D^{\perp}$. Moreover, the following relation between the canonical Chern forms $\gamma_{I}$ and $\gamma_{J}$ of $(g, I)$ and $(g, J)$ holds:
$$\gamma_{I}=3 \gamma_{J}-d d^{J}\left(\ln |\nabla \Omega|^{2}\right) .$$
Proof. The opposite almost complex structure $I$ is defined (on $U$ ) through the distributions $D$ and $D^{\perp}$, which in turn are determined by the 1-jet of $J$. To obtain information about the 1 -jet of $I$, we thus need to study the 2 -jet of $J$ (equivalently, the 2 -jet of $\Omega$ ). For this purpose, let us define the 1-forms $m_{i}, n_{i}, i=1,2$, by the first relation below, while the other three relations follow easily from the first one and (21), (22).
$$\begin{aligned}
\nabla a & =m_{1} \otimes a+n_{1} \otimes J a+m_{2} \otimes J_{1} a+n_{2} \otimes J_{2} a ; \\
\nabla(J a) & =-n_{1} \otimes a+m_{1} \otimes J a+\left(a-n_{2}\right) \otimes J_{1} a+\left(m_{2}-J a\right) \otimes J_{2} a ; \\
\nabla\left(J_{1} a\right) & =-m_{2} \otimes a+\left(n_{2}-a\right) \otimes J a+m_{1} \otimes J_{1} a+\left(b-n_{1}\right) \otimes J_{2} a ; \\
\nabla\left(J_{2} a\right) & =-n_{2} \otimes a+\left(J a-m_{2}\right) \otimes J a+\left(n_{1}-b\right) \otimes J_{1} a+m_{1} \otimes J_{2} a .
\end{aligned}$$
Note that for a strictly almost Kähler 4-manifold $(M, g, J, \Omega)$ satisfying (3), the identity (37) becomes
$$0=\frac{1}{6}\left(d^{J}(\kappa-s)\right)_{Z}-\left\langle\left(\delta W_{3}^{+}\right)_{Z}, \Omega\right\rangle .$$
Using (20), (9) and (21), this can be further written as
$$\frac{1}{4} d|\nabla \Omega|^{2}=d|a|^{2}=-J\left\langle\delta W_{3}^{+}, \Omega\right\rangle=-2 J W_{3}^{+}(\phi)(a) .$$
Hence the 1 -form $m_{1}$ is immediately determined to be:
$$m_{1}=\frac{1}{2} d\left(\ln |\nabla \Omega|^{2}\right)=-\frac{1}{|a|^{2}} J W_{3}^{+}(\phi)(a) .$$
As a consequence, observe that $m_{1}^{\sharp} \in D$, where here and henceforth the superscript ♯ denotes the dual vector field of a 1-form, through the metric. The forms $n_{1}, m_{2}, n_{2}$ are determined by the relations (23). Indeed, under the condition (3), the 2-forms $R(\phi)$ and $R(J \phi)$ are $J$-anti-invariant, thus, according to (23), we have
$$(d a-J a \wedge b)^{\prime}=0, \quad(d(J a)+a \wedge b)^{\prime}=0 .$$
These relations combined with (52) lead to
$$\begin{aligned}
& n_{1}=-b-J m_{1}=-b-\frac{1}{2} d^{J}\left(\ln |\nabla \Omega|^{2}\right) \\
& m_{2}=\frac{1}{2} J a+J m_{0} \\
& n_{2}=-J m_{2}=\frac{1}{2} a+m_{0}
\end{aligned}$$
where $m_{0}$ is a 1-form dual to a vector field in $D$.

Thus, formulae (52), (54) and (55) imply
$$\begin{aligned}
d a\left(X, X^{\prime}\right) & =d(J a)\left(X, X^{\prime}\right)=0, \forall X, X^{\prime} \in D \\
d\left(J_{1} a\right)\left(Y, Y^{\prime}\right) & =d\left(J_{2} a\right)\left(Y, Y^{\prime}\right)=0, \forall Y, Y^{\prime} \in D^{\perp}
\end{aligned}$$
As the vector fields dual to $a, J a$ generate $D^{\perp}$ and the vector fields dual to $J_{1} a, J_{2} a$ generate $D$, the above relations show that $D^{\perp}$ and $D$ are involutive distributions.

To show that $(g, I)$ is almost Kähler, observe first that the fundamental forms of $(g, I)$ and $(g, J)$ are related by $\bar{\Omega}=\Omega-\frac{2}{|a|^{2}} a \wedge J a$. We take the covariant derivative of this relation and use (21) and (52-55) to get
$$\nabla \bar{\Omega}=2 m_{0} \otimes \bar{\phi}-2 I m_{0} \otimes I \bar{\phi},$$
where $\bar{\phi} \in \llbracket \Lambda_{I}^{0,2} M \rrbracket$ is the natural gauge for ( $g, I$ ), determined by $\phi$ through the relation
$$\bar{\phi}=\phi+\frac{2}{|a|^{2}} J a \wedge J_{2} a .$$
Then, $d \bar{\Omega}=0$ is immediate from (56), and so is the claim about the Kähler nullity of $(g, I)$ since $\bar{a}=2 m_{0}$ is dual to a vector field in $D$.

Finally, taking the covariant derivative of (57) and using (22) and (52-55), one finds
$$\nabla \bar{\phi}=\bar{b} \otimes I \bar{\phi}-\bar{a} \otimes \bar{\Omega},$$
where $\bar{a}=2 m_{0}$ and
$$\bar{b}=3 b+d^{J}\left(\ln |\nabla \Omega|^{2}\right) .$$
Since $\gamma_{I}=-d \bar{b}$ and $\gamma_{J}=-d b$ (see (25)), relation (51) follows. □
The next step is to gather more information on the curvature components of the almost Kähler metric $(g, I)$.

Lemma 6. Let $(M, g, J)$ be a strictly almost Kähler 4-manifold satisfying (3) and $(g, I)$ be the opposite almost Kähler structure as above. Then, the trace-free Ricci form $\rho_{0}$ of $(g, J)$ and the $\llbracket \Lambda_{I}^{2,0} M \rrbracket$-component of the star-Ricci form $\bar{\rho}_{*}$ of $(g, I)$ are given by:
$$\rho_{0}=\frac{1}{4}\left(s+\frac{|\nabla \bar{\Omega}|^{2}}{4}\right) \bar{\Omega}+\bar{\Psi}, \quad\left(\bar{\rho}_{*}\right)_{I}^{\prime \prime}=\bar{\Psi}, \quad \text { where } \bar{\Psi}=\frac{1}{2} \nabla_{d\left(\ln |\nabla \Omega|^{2}\right)} \bar{\Omega} .$$
Moreover, the identity (34) reads as
$$\frac{1}{4} d|\nabla \bar{\Omega}|^{2}=d|\bar{a}|^{2}=-I\left\langle\delta W_{3}^{-}, \bar{\Omega}\right\rangle=-2 I W_{3}^{-}(\bar{\phi})(\bar{a}) .$$
Proof. We first prove the equalities in (60). With respect to the gauge $\bar{\phi}$ from the previous lemma, the Ricci identity for $\bar{\Omega}$ takes the form (compare with (23))
$$d \bar{a}-I \bar{a} \wedge \bar{b}=-R(I \bar{\phi}) ; d(I \bar{a})+\bar{a} \wedge \bar{b}=-R(\bar{\phi}) .$$
We proved in Lemma 5 that $\bar{a}^{\sharp} \in D$ and that $D$ is an involutive distribution. It thus follows that the left-hand sides of the relations (62) vanish on $X \wedge J X$ with $X \in D^{\perp}$. This is equivalent with the fact that the $\llbracket \Lambda_{I}^{0,2} M \rrbracket$-components of $R(\Omega)$ and $R(\bar{\Omega})$ are equal. Thus
$$\left(\rho_{0}\right)_{I}^{\prime \prime}=\left(\bar{\rho}_{*}\right)_{I}^{\prime \prime}=\bar{\Psi},$$
and it remains to obtain the claimed expressions of $\bar{\Psi}$ and the $\bar{\Omega}$-component of $\rho_{0}$. For this we turn to relation (51). Using (24) and its analogue for $\bar{\phi}$
$$d \bar{b}=\bar{a} \wedge I \bar{a}-R(\bar{\Omega}),$$
relation (51) is equivalent to
$$\frac{3}{2} R(\Omega)-\frac{1}{2} R(\bar{\Omega})-\frac{1}{2} d d^{J}\left(\ln |\nabla \Omega|^{2}\right)-\frac{3}{2} a \wedge J a+\frac{1}{2} \bar{a} \wedge J \bar{a}=0 .$$
Taking the $\llbracket \Lambda_{I}^{0,2} M \rrbracket$-component of (63) we obtain
$$\bar{\Psi}=\frac{1}{2}\left(d d^{I}\left(\ln |\nabla \Omega|^{2}\right)\right)_{I}^{\prime \prime}=\frac{1}{2} \nabla_{d\left(\ln |\nabla \Omega|^{2}\right)} \bar{\Omega}$$
where the first equality uses that $\left(d\left(\ln |\nabla \Omega|^{2}\right)\right)^{\sharp} \in D$ (see (53)), hence $d^{J}\left(\ln |\nabla \Omega|^{2}\right)=$ $d^{I}\left(\ln |\nabla \Omega|^{2}\right)$, and the second equality follows from (13) and (15).

Since $\left(d^{J}\left(\ln |\nabla \Omega|^{2}\right)\right)^{\sharp} \in D$ and $D$ is involutive, we also have
$$\left\langle d d^{J}\left(\ln |\nabla \Omega|^{2}\right),(\Omega-\bar{\Omega})\right\rangle=0 .$$
Thus, taking the inner product of relation (63) with $1 / 2(\Omega-\bar{\Omega})$ and using (20) and its analogue for the almost Kähler structure $(g, I)$, we derive
$$\langle R(\Omega), \bar{\Omega}\rangle=\frac{s}{2}+\frac{1}{8}|\nabla \bar{\Omega}|^{2},$$
and the desired form of the $\bar{\Omega}$-component of $\rho_{0}$ follows.
Now we prove the relation (61). The starting point for this is the identity (34) established in Lemma 4. Taking into account that the Ricci tensor is $J$-invariant and that the antiself-dual Weyl tensor decomposes into $W^{-}=W_{1}^{-}+W_{2}^{-}+W_{3}^{-}$(with respect to the almost complex structure $I$ ), relation (34) can be written as
$$0=\nabla_{J Z} \rho_{0}+\frac{1}{6}\left(d s \wedge Z^{b}\right)^{-}-2\left(\delta W_{1}^{-}\right)_{Z}-2\left(\delta W_{2}^{-}\right)_{Z}-2\left(\delta W_{3}^{-}\right)_{Z}$$
We consider the $\bar{\Omega}$-component of this relation, taking into account that for $\left(\delta W_{1}^{-}\right)_{Z}$, $\left(\delta W_{2}^{-}\right)_{Z}$ we have similar expressions to the ones for $\left(\delta W_{1}^{+}\right)_{Z},\left(\delta W_{2}^{+}\right)_{Z}$ given in (35) and (36). We thus get
$$\begin{aligned}
0= & \left\langle\nabla_{J Z} \rho_{0}, \bar{\Omega}\right\rangle-\frac{1}{6}\left(d^{I}(\bar{\kappa}-s)\right)_{Z}+\frac{1}{2}\left(d^{I} \bar{\kappa}\right)_{Z} \\
& -\left\langle\nabla_{I Z}\left(\bar{\rho}_{*}\right)_{I}^{\prime \prime}, \bar{\Omega}\right\rangle-2\left(\delta\left(\bar{\rho}_{*}\right)_{I}^{\prime \prime}\right)_{Z}-2\left\langle\left(\delta W_{3}^{-}\right)_{Z}, \bar{\Omega}\right\rangle .
\end{aligned}$$
We plug the expressions for $\rho_{0}$ and for $\left(\bar{\rho}_{*}\right)_{I}^{\prime \prime}$ given by (60) into the above formula to eventually obtain
$$\begin{aligned}
0= & 2\left(d^{I}|\bar{a}|^{2}\right)_{Z}-\frac{1}{2}\left(d^{J}|\bar{a}|^{2}\right)_{Z}-\frac{1}{2}\left(d^{I} s-d^{J} s\right)_{Z} \\
& -2(\delta \bar{\Psi})_{Z}-2\left\langle\left(\delta W_{3}^{-}\right)_{Z}, \bar{\Omega}\right\rangle
\end{aligned}$$
To derive the latter formula we have also used that $\left\langle\bar{\Psi}, \nabla_{I Z-J Z} \bar{\Omega}\right\rangle=0$ which follows by Lemma 5, since $I Z-J Z \in D^{\perp}$.

Substituting the expression for $\rho_{0}$ found in (60) into (26), and applying $J$, we get
$$d^{I} s-d^{J} s=-d^{I}|\bar{a}|^{2}+4 \delta \bar{\Psi} .$$
Using this last relation back in (64) to replace the term $\frac{1}{2}\left(d^{I} s-d^{J} s\right)_{Z}$, we obtain
$$0=2\left(d^{I}|\bar{a}|^{2}\right)_{Z}-\frac{1}{2}\left(d^{J}|\bar{a}|^{2}+d^{I}|\bar{a}|^{2}\right)_{Z}-2\left\langle\left(\delta W_{3}^{-}\right)_{Z}, \bar{\Omega}\right\rangle .$$
Since $\bar{a}^{\sharp} \in D$, the 1 -form
$$\left\langle\delta W_{3}^{-}, \bar{\Omega}\right\rangle=2 W_{3}^{-}(\bar{\phi})(\bar{a})$$
is dual to a vector field in $D^{\perp}$, and then relation (65) is equivalent with the relation (61). \(\square\)

The next result is an "iteration" of Lemma 5.
Lemma 7. Let $(M, g, J)$ be a strictly almost Kähler 4-manifold satisfying (3) and let $U$ denote the open set of points where $\nabla J \neq 0$. Let $(g, I)$ be the opposite almost Kähler structure on $U$, associated to $(g, J)$ and assume that on a non-empty open subset $U_{0} \subset U$ the opposite almost Kähler structure ( $g, I$ ) is not Kähler. Then, on $U_{0}$, the opposite almost Hermitian structure $(g, \tilde{J})$ associated to $(g, I)$ is $(g,-J)$. Moreover, the following relation between the canonical Chern forms of $(g, I)$ and $(g, \tilde{J})$ holds
$$\gamma_{\tilde{J}}=-\gamma_{J}=3 \gamma_{I}-d d^{I}\left(\ln |\nabla \bar{\Omega}|^{2}\right)-2 d d^{J}\left(\ln |\nabla \Omega|^{2}\right) .$$
Proof. From the assumption that $(g, I)$ is not Kähler on $U_{0}$ and from Lemma 5, it follows that the Kähler nullity of $(g, I)$ is precisely the distribution $D^{\perp}$ on $U_{0}$; the opposite almost complex structure $\tilde{J}$ associated to $(g, I)$ is then defined by $\tilde{J}=I$ on $D^{\perp}$ and $\tilde{J}=-I$ on $D$, i.e., $\tilde{J}=-J$.