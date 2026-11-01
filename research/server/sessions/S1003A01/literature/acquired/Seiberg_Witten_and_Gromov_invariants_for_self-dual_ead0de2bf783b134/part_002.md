---
retention_scope: session
part: 2
total_parts: 3
---

[Part 2/3 of: Seiberg–Witten and Gromov invariants for self-dual]

Now we consider $J$-holomorphic curves in the completion $(\bar{X}, \omega, J)$ of a symplectic cobordism $(X, \omega):\left(Y_{+}, \lambda_{+}\right) \rightarrow\left(Y_{-}, \lambda_{-}\right)$, including the special case of a symplectization $\bar{X}=\mathbb{R} \times Y$. Denote by $\mathcal{M}\left(\Theta^{+}, \Theta^{-}\right)$the moduli space of $J$-holomorphic currents in $\bar{X}$ asymptotic to orbit sets $\Theta^{ \pm}$ (see [3, §2.2]), and by $\mathcal{M}_{I}\left(\Theta^{+}, \Theta^{-}\right)$the subset of such currents with ECH index $I \in \mathbb{Z}$. Let $\pi: N_{C} \rightarrow C$ be the (holomorphic) normal bundle of an immersed connected $J$-holomorphic curve $C$ in $\mathcal{M}\left(\Theta^{+}, \Theta^{-}\right)$, and denote by $S_{N_{C}} \subset N_{C}$ the unit circle subbundle. Form the $n$-vortex bundle
$$\mathfrak{C}_{N_{C}, n}:=S_{N_{C}} \times{ }_{S^{1}} \mathfrak{C}_{n}$$
whose projection onto $C$ will also be denoted by $\pi$. With respect to a Hermitian metric and compatible connection on $N_{C}$, the $(1,0)$-part of its vertical tangent space is
$$T_{1,0}^{\text {vert }} \mathfrak{C}_{N_{C}, n}=(\operatorname{Ker} d \pi)_{1,0}=S_{N_{C}} \times_{S^{1}} T_{1,0} \mathfrak{C}_{n}$$
Sections $\mathfrak{c} \in \Gamma\left(\mathfrak{C}_{N_{C}, n}\right)$ can be viewed as $S^{1}$-invariant maps $S_{N_{C}} \rightarrow \mathfrak{C}_{n}$, so their covariant derivative can be taken and restricted to the horizontal subspace $T^{\text {hor }} S_{N_{C}}$. This defines a "del-bar" operator
$$\mathfrak{c} \mapsto \bar{\partial} \mathfrak{c} \in \Gamma\left(\mathfrak{c}^{*} T_{1,0}^{\text {vert }} \mathfrak{C}_{N_{C}, n} \otimes T^{0,1} C\right)$$
Given the pair $\left(\nu_{C}, \mu_{C}\right) \in \Gamma\left(T^{0,1} C\right) \times \Gamma\left(T^{0,1} C \otimes N_{C}^{2}\right)$ associated with the deformation operator $D_{C}$ of $C$ (see [3, §2.5]), we define the section $\mathfrak{h}_{\nu_{C} \mu_{C}}$ of $\pi^{*} T^{0,1} C \rightarrow \mathfrak{C}_{N_{C}, n}$ pointwise by
$$\mathfrak{h}_{\nu_{C} \mu_{C}}\left(p,\left(A_{p}, \alpha_{p}\right)\right)=\frac{1}{4 \pi} \int_{\mathbb{C}}\left[2 \nu_{C, p}|z|^{2}+\left(\mu_{C, p} \bar{z}^{2}+\bar{\mu}_{C, p} z^{2}\right)\right]\left(1-\left|\alpha_{p}\right|^{2}\right) d \mathrm{vol}$$
after identifying a fiber of $N_{C}$ with $\mathbb{C}$ and identifying a point in $\mathfrak{C}_{N_{C}, n}$ with $\left(p,\left(A_{p}, \alpha_{p}\right)\right) \in C \times \mathfrak{C}_{n}$. Denote by $\nabla^{1,0} \mathfrak{h}_{\nu_{C} \mu_{C}}$ the corresponding section of $T_{1,0}^{\text {vert }} \mathfrak{C}_{N_{C}, n} \otimes \pi^{*} T^{0,1} C$.

As will become evident in Section 3.2, we are interested in certain sections of $\mathfrak{C}_{N_{C}, n}$ asymptotic to zero on the ends of $C$. They should be considered as objects that are "halfway" between $J$-holomorphic curves and SW instantons. They were originally introduced in [27, §3], see also [32, §2.e], and are defined as follows.

Definition 3.4. The subspace $\mathcal{Z}_{0} \subset L_{1}^{2}\left(\mathfrak{C}_{N_{C}, n}\right)$ consists of those sections $\mathfrak{c}$ satisfying
$$\bar{\partial} \mathfrak{c}+\mathfrak{c}^{*} \nabla^{1,0} \mathfrak{h}_{\nu_{C} \mu_{C}}=0$$

We can spell out this subspace more concretely using the biholomorphism (3.1). Namely, (3.1) induces a bundle isomorphism $\mathfrak{C}_{N_{C}, n} \cong \bigoplus_{j=1}^{n} N_{C}^{j}$ and under this isomorphism (3.3) takes the form
$$\bar{\partial} \eta+\nu_{C} \aleph(\eta)+\mu_{C} \mathbb{F}(\eta)=0$$
for sections $\eta \in L_{1}^{2}\left(\bigoplus_{j=1}^{n} N_{C}^{j}\right)$. Here, $\bar{\partial}$ is the del-bar operator with respect to the Hermitian connection on $N_{C}$,
$$\aleph: \Gamma\left(\bigoplus_{j=1}^{n} N_{C}^{j}\right) \rightarrow \Gamma\left(\bigoplus_{j=1}^{n} N_{C}^{j}\right)$$
is the map that multiplies the $j^{\text {th }}$ summand by $j$, and
$$\mathbb{F}: \Gamma\left(\bigoplus_{j=1}^{n} N_{C}^{j}\right) \rightarrow \Gamma\left(\bigoplus_{j=1}^{n} N_{C}^{j-2}\right)$$
is some fiber-preserving bundle map that is not $\mathbb{R}$-linear unless $n=1$. When $n=1$, this map $\mathbb{F}$ is the complex conjugation operator and so (3.4) becomes
$$\bar{\partial} \eta+\nu_{C} \eta+\mu_{C} \bar{\eta}=0$$
for sections $\eta \in L_{1}^{2}\left(N_{C}\right)$. Thus, $\mathcal{Z}_{0}$ is identified with $\operatorname{Ker}\left(D_{C}\right)$ when $n=1$. For example, if $C$ is a Fredholm index zero curve cut out transversely then $\mathcal{Z}_{0}$ is a point, the constant map to the unique "symmetric" vortex.

Remark 3.5. In the setting of [31] where $\bar{X}$ is a symplectization, the only multiply covered curves were $\mathbb{R}$-invariant cylinders with $\mu_{C}=0$. The nonlinear map $\mathbb{F}$ only played a role in the setting of 28 where $\bar{X}$ is a closed manifold, due to the existence of multiply covered tori with $\mu_{C} \neq 0$. In this paper, the space of solutions to (3.3) for $n>1$ will be of concern whenever $C$ is a special curve.

In [32, §2.f], Taubes introduces the appropriate Morrey spaces as certain completions of the spaces of compactly supported sections of the bundles $\mathfrak{c}^{*} T_{1,0}^{\text {vert }} \mathfrak{C}_{N_{C}, n}$ and $\mathfrak{c}^{*} T_{1,0}^{\text {vert }} \mathfrak{C}_{N_{C}, n} \otimes T^{0,1} C$. They are denoted by $\mathcal{K}_{\mathfrak{c}}$ and $\mathcal{L}_{\mathfrak{c}}$, respectively. A nice feature of these Banach space completions is that the small normed elements can be used to define deformations of $\mathfrak{c}$ (see [32, Equation 2-28]).

At any given $\mathfrak{c} \in L_{1}^{2}\left(\mathfrak{C}_{N_{C}, n}\right)$, define the $\mathbb{R}$-linear operator $\boldsymbol{\Delta}_{\mathfrak{c}}: \mathcal{K}_{\mathfrak{c}} \rightarrow \mathcal{L}_{\mathfrak{c}}$ to be the linearization of the operator in (3.3) which cuts out $\mathcal{Z}_{0}$. From the viewpoint of $\bigoplus_{j=1}^{n} N_{C}^{j}$ the corresponding linearization of the operator in (3.4) is
$$\Delta_{\mathfrak{c}}: \zeta \mapsto \bar{\partial} \zeta+\nu_{C} \aleph(\zeta)+\mu_{C} d \mathbb{F}_{\mathfrak{c}}(\zeta)$$
When $\mathfrak{c} \in \mathcal{Z}_{0}$ the operators $\boldsymbol{\Delta}_{\mathfrak{c}}$ and $\Delta_{\mathfrak{c}}$ are conjugate to each other using a bundle isomorphism induced from (3.1) (see [27, Proposition 3.2(5)]). An element $\mathfrak{c} \in \mathcal{Z}_{0}$ is called regular if $\operatorname{Coker}\left(\boldsymbol{\Delta}_{\mathfrak{c}}\right)=$ 0, or equivalently $\operatorname{Coker}\left(\Delta_{\mathfrak{c}}\right)=0$.

\subsection*{3.2 Maps between ECH and HM}

In [31], Taubes defined a canonical isomorphism of relatively graded $\mathbb{Z} / d \mathbb{Z}$-modules (with $\mathbb{Z} / 2 \mathbb{Z}$ coefficients)
$$E C H_{*}^{L}(Y, \lambda, \Gamma, J) \cong \widehat{H M}_{L}^{-*}\left(Y, \lambda, \mathfrak{s}_{\xi}+\operatorname{PD}(\Gamma), J, r\right)$$
under the assumption that $r$ is sufficiently large and $(\lambda, J)$ is a generic ${ }^{10} L$-flat pair, where $d$ denotes the divisibility of $c_{1}\left(\mathfrak{s}_{\xi}+\mathrm{PD}(\Gamma)\right)=c_{1}(\xi)+2 \mathrm{PD}(\Gamma)$ in $H^{2}(Y ; \mathbb{Z}) /$ Torsion. Taking the direct limit as $L \rightarrow \infty$, Taubes' isomorphism becomes
$$E C H_{*}(Y, \xi, \Gamma) \cong \widehat{H M}^{-*}\left(Y, \mathfrak{s}_{\xi}+\mathrm{PD}(\Gamma)\right)$$
A detailed explanation can be found in [13], specifically the proof of [13, Theorem 1.3]. Taubes' isomorphism also preserves the absolute gradings by homotopy classes of oriented 2-plane fields
$$E C H_{j}(Y, \xi) \cong \widehat{H M}^{j}(Y)$$
where $E C H_{*}(Y, \xi):=\bigoplus_{\Gamma \in H_{1}(Y ; \mathbb{Z})} E C H_{*}(Y, \xi, \Gamma)$ and $j \in J(Y)$ (see 2 ), and it also intertwines the respective $U$-maps (see [35, Theorem 1.1]). We now briefly explain how this isomorphism (3.6) was constructed.

Theorem 3.6 (Taubes). Fix $L>0$ and a generic ${ }^{10} L$-flat pair $(\lambda, J)$ on the nondegenerate contact 3-manifold $(Y, \lambda)$. Then for $r$ sufficiently large and $\Gamma \in H_{1}(Y ; \mathbb{Z})$, there is a canonical bijection from the set of generators of $\widehat{C M}_{L}^{*}\left(Y, \lambda, \mathfrak{s}_{\xi}+\operatorname{PD}(\Gamma), J, r\right)$ to the set of generators of $E C C_{*}^{L}(Y, \lambda, \Gamma, J)$.

As shown in [31, Theorem 4.2], the isomorphism (3.6) is actually established on generators of the chain complexes, so that for any given admissible orbit set $\Theta \in E C C_{*}^{L}(Y, \lambda, \Gamma, J)$ there exists a unique irreducible monopole
$$\mathfrak{c}_{\Theta}=\left[A_{\Theta},\left(\alpha_{\Theta}, \beta_{\Theta}\right)\right] \in \widehat{C M}_{L}^{-*}\left(Y, \lambda, \mathfrak{s}_{\xi}+\operatorname{PD}(\Gamma), J, r\right)$$
To construct $\mathfrak{c}_{\Theta}$, an arbitrary smooth map $\mathfrak{c}_{\Theta_{i}}: S^{1} \rightarrow \mathfrak{C}_{m_{i}}$ is first assigned to each pair $\left(\Theta_{i}, m_{i}\right) \in \Theta$. From such a map, a "potential candidate" ( $A_{r},\left(\alpha_{r}, 0\right)$ ) for a monopole is constructed which almost solves Taubes' perturbed Seiberg-Witten equations (2.1) when $r$ is large; this would not be possible if $\Theta_{i}$ was not a Reeb orbit (see [32, Lemma 3.4]). When $\mathfrak{c}_{\Theta_{i}}$ satisfies (3.2), perturbation theory is then used to find an honest solution nearby this candidate. In fact, by Theorem 3.2 there is precisely one such map $\mathfrak{c}_{\Theta_{i}}$.

As shown in [31, Theorem 4.3], the chain complex differentials also agree: Given two generators $\Theta^{ \pm} \in E C C_{*}^{L}(Y, \lambda, \Gamma, J)$ and their corresponding generators $\mathfrak{c}_{\Theta^{ \pm}} \in \widehat{C M}_{L}^{-*}\left(Y, \lambda, \mathfrak{s}_{\xi}+\operatorname{PD}(\Gamma), J, r\right)$, for $r$ sufficiently large there is an orientation-preserving diffeomorphism between $\mathcal{M}_{1}\left(\Theta^{+}, \Theta^{-}\right)$and $\mathfrak{M}_{1}\left(\mathfrak{c}_{\Theta-}, \mathfrak{c}_{\Theta+} ; \mathfrak{s}\right)$ which is $\mathbb{R}$-equivariant with respect to the translation actions. In analogy with the construction for chain complex generators, this diffeomorphism
$$\Psi_{r}: \mathcal{M}_{1}\left(\Theta^{+}, \Theta^{-}\right) \rightarrow \mathfrak{M}_{1}\left(\mathfrak{c}_{\Theta^{-}}, \mathfrak{c}_{\Theta^{+}} ; \mathfrak{s}\right)$$
is constructed as follows (see [32, §5] for more details). Given $\mathcal{C} \in \mathcal{M}_{1}\left(\Theta^{+}, \Theta^{-}\right)$there exists a complex line bundle $E \rightarrow \mathbb{R} \times Y$ and a "potential candidate"
$$\left(A^{*}, \Psi^{*}\right) \in \operatorname{Conn}(E) \oplus \Gamma\left(E \oplus K^{-1} E\right)$$
for a SW instanton which almost solves Taubes' perturbed Seiberg-Witten equations (2.2) when $r$ is large. Here, $E$ has a section whose zero set (with multiplicity) is $\mathcal{C}$, and away from $\mathcal{C}$ the bundle

\footnotetext{
${ }^{10}$ Genericity here is in the sense that $J$ is chosen from a residual subset of almost complex structures (endowed with the $C^{\infty}$ Fréchet space topology) for which the $L$-filtered ECH is well-defined.
}
$E$ is identified with the trivial bundle. Away from $\mathcal{C}$ the pair ( $A^{*}, \Psi^{*}$ ) is close to $\left(A_{0},(1,0)\right)$, where $A_{0}$ is the flat connection on $E$ coming from the product structure. Near a component $(C, d) \in \mathcal{C}$ the pair $\left(A^{*}, \Psi^{*}\right)$ is determined by the zero-section $0 \in \mathcal{Z}_{0} \subset \Gamma\left(\mathfrak{C}_{N_{C}, d}\right)$. Then an implicit function theorem argument may be used to perturb $\left(A^{*}, \Psi^{*}\right)$ to a SW instanton $\Psi_{r}(\mathcal{C})$.

Remark 3.7. This remark is intended to complement Remark 3.5. Roughly speaking, we can generalize the construction of $\left(A^{*}, \Psi^{*}\right)$ using nontrivial sections in $\mathcal{Z}_{0} \subset L_{1}^{2}\left(\mathfrak{C}_{N_{C}, d}\right)$, such that if all $\mathcal{Z}_{0}$ were regular then sufficiently $L^{\infty}$-small elements of $\mathcal{Z}_{0}$ would parametrize a neighborhood of $\Psi_{r}(\mathcal{C})$ in the SW moduli space, and if some $\mathcal{Z}_{0}$ were zero-dimensional (with additional hypotheses on $(C, d)$ ) then there would be an associated SW instanton for each point in that $\mathcal{Z}_{0}$. When $d=1$, the operator (3.5) is precisely the deformation operator $D_{C}$ which has trivial cokernel (for generic $J$ ), and hence $\mathcal{Z}_{0}$ consists of regular points. When $d>1$, there is no guarantee that any point of $\mathcal{Z}_{0}$ is regular if $\mu_{C} \neq 0$. Luckily for ECH, if $d>1$ then $C$ is an $\mathbb{R}$-invariant cylinder with $\mu_{C}=0$, in which case $\mathcal{Z}_{0}$ consists of a single regular point (the zero-section).

Given a basepoint $y \in Y$, there is an analogous bijection between point-constrained moduli spaces $\mathcal{M}_{2}\left(\Theta^{+}, \Theta^{-} ; y\right) \rightarrow \mathfrak{M}_{2}\left(\mathfrak{c}_{\Theta-}, \mathfrak{c}_{\Theta^{+}} ; \mathfrak{s}, y\right)$ used to relate the respective $U$-maps. It is established in [35, Theorem 2.6] and closely follows the construction of $\Psi_{r}$.

We end this section by pointing the reader to Taubes' papers for the various properties of $\Psi_{r}$. The assertion that $\Psi_{r}$ maps $\mathcal{M}_{1}\left(\Theta^{+}, \Theta^{-}\right)$onto a union of components of $\mathfrak{M}_{1}\left(\mathfrak{c}_{\Theta-}, \mathfrak{c}_{\Theta+} ; \mathfrak{s}\right)$ that contain solely nondegenerate SW instantons is given in [33, §3.a]. The proof that $\Psi_{r}$ is surjective consists of three main arguments spelled out in [34, §3-§7]. First, certain global properties of SW instanton solutions to Taubes' perturbed Seiberg-Witten equations are established in [34, §3] and in [34, Lemma 5.2, Lemma 5.3]. Second, these global results are used to assign an element in $\mathcal{M}_{1}\left(\Theta^{+}, \Theta^{-}\right)$to a given SW instanton in $\mathfrak{M}_{1}\left(\mathfrak{c}_{\Theta-}, \mathfrak{c}_{\Theta^{+}} ; \mathfrak{s}\right)$ and is done so in [34, §4] and in [26, §5-§7]. Third, these assignments are given by the map $\Psi_{r}$ and is done so in [34, §6-§7].

\section*{4 Equating ECH and HM cobordism counts}

In light of Section 1.4, we now fix $(X, \omega, \mathfrak{s})$ such that $E \cdot \tau_{\omega}(\mathfrak{s}) \geq-1$ for all $E \in \mathcal{E}_{\omega}$. Subsequently, $\left(-\partial X_{0}, \lambda_{\mathfrak{s}}\right)$ and $\left(\bar{X}_{0}, \omega, J\right)$ are also fixed. We also fix an ordering of the zero-circles of $\omega$, as well as a homology orientation of $X_{0}$ (hence of $X$ ). Denote by
$$\mathfrak{s}_{\mathfrak{s}}:=\mathfrak{s}_{\omega}+\tau_{\omega}(\mathfrak{s})$$
the spin-c structure on $X_{0}$ (and on $\bar{X}_{0}$ ) that corresponds to the relative class $\tau_{\omega}(\mathfrak{s})$, identified with the spin-c structure $\mathfrak{s}_{\xi_{0}}+1$ on the ends of $\bar{X}_{0}$. Denote by $E \rightarrow \bar{X}_{0}$ the complex line bundle for the spinor decomposition $\mathbb{S}_{+}=E \oplus K^{-1} E$ associated with $\mathfrak{s}_{\mathfrak{s}}$. Now, make the following choices:
\begin{itemize}
\item[-] an integer $I \geq 0$,
\item[-] an integer $p \in\{0, \ldots, I\}$ such that $I-p$ is even,
\item[-] an ordered set of $p$ disjoint oriented loops $\bar{\eta}:=\left\{\eta_{1}, \ldots, \eta_{p}\right\} \subset X_{0}$,
\item[-] a set of $\frac{1}{2}(I-p)$ disjoint points $\bar{z}:=\left\{z_{1}, \ldots, z_{(I-p) / 2}\right\} \subset X_{0}-\bar{\eta}$.
\end{itemize}
Recall from [3] that the choice $I=d(\mathfrak{s})$ is used to define $\operatorname{Gr}_{X, \omega}(\mathfrak{s})$. Denote by $\mathfrak{M}_{I}\left(\mathfrak{c}, \varnothing ; \mathfrak{s}_{\mathfrak{s}}, \bar{z}, \bar{\eta}\right)$ the subset of SW instantons $\mathfrak{d}=[A, \Psi=(\alpha, \beta)] \in \mathfrak{M}_{I}\left(\mathfrak{c}, \varnothing ; \mathfrak{s}_{\mathfrak{s}}\right)$ for which $\alpha \in \Gamma(E)$ vanishes at each point $z_{i} \in \bar{z}$ and at some point $w_{i}$ along each loop $\eta_{i} \in \bar{\eta}$.

Although the upcoming Theorem 4.2 is a statement using $\mathbb{Z} / 2 \mathbb{Z}$ coefficients, we specify the coherent orientations and the signed weights attached to SW instantons because it is expected that the theorem also holds over $\mathbb{Z}$. To define the sign $q(\mathfrak{d})$ attached to each $\mathfrak{d} \in \mathfrak{M}_{I}\left(\mathfrak{c}, \varnothing ; \mathfrak{s}_{\mathfrak{s}}, \bar{z}, \bar{\eta}\right)$, we build the $\mathbb{R}^{I}$-vector space
$$V_{\mathfrak{d}}:=\bigoplus_{i=1}^{\frac{1}{2}(I-p)} E_{z_{i}} \oplus \bigoplus_{i=1}^{p}\left(E_{w_{i}} / \nabla_{A} \alpha\left(T_{w_{i}} \eta_{i}\right)\right)$$
as in [29, §2.c]. For generic choices of perturbations $\mu \in \Omega^{2}\left(\bar{X}_{0}\right)$ that define Taubes' perturbed Seiberg-Witten equations (2.2), the covariant derivative of $\alpha$ along $\eta_{i}$ at $w_{i}$ is nonzero and the restriction map
$$\operatorname{Ker}\left(\mathfrak{D}_{\mathfrak{d}}\right) \rightarrow V_{\mathfrak{d}}$$
is an isomorphism. Then $q(\mathfrak{d})= \pm 1$ depending on whether this restriction map is orientationpreserving or orientation-reversing. Here, $\operatorname{Ker}\left(\mathfrak{D}_{\mathfrak{d}}\right)$ is oriented by the coherent orientations (see Section 2.5), and $V_{\mathfrak{d}}$ is naturally oriented because the complex bundle $E$ is oriented, the loops $\gamma_{i}$ are oriented, and the points $w_{i}$ are ordered.

Notation 4.1. Fix an admissible orbit set $\Theta$ with action less than $\rho_{\mathfrak{s}}$ and its corresponding monopole $\mathfrak{c}_{\Theta}$. Since the moduli spaces $\mathcal{M}_{I}\left(\varnothing, \Theta ; \tau_{\omega}(\mathfrak{s}), \bar{z}, \bar{\eta}\right)$ and $\mathfrak{M}_{I}\left(\mathfrak{c}_{\Theta}, \varnothing ; \mathfrak{s}_{\mathfrak{s}}, \bar{z}, \bar{\eta}\right)$ will appear often, we denote them by $\mathcal{M}$ and $\mathfrak{M}$ unless otherwise specified. We remind the reader that both $\mathcal{M}$ and $\mathfrak{M}$ depend on $(\lambda, J)$ while $\mathfrak{M}$ also depends on $r$ (and abstract perturbations).

Theorem 4.2. For an admissible orbit set $\Theta$ with action less than $\rho_{\mathfrak{s}}$, generic $J$ as needed to make 1.6 well-defined, and sufficiently large $r$,
$$\sum_{\mathcal{C} \in \mathcal{M}} q(\mathcal{C}) \equiv \sum_{\mathfrak{d} \in \mathfrak{M}} q(\mathfrak{d}) \quad \bmod 2$$

The proof of Theorem 4.2 is spelled out in the following subsections. A key point is that all relevant constructions of Taubes' isomorphisms which occur in a symplectization and a closed symplectic manifold generalize to (completed) symplectic cobordisms, because the analysis takes place local to the $J$-holomorphic curves. We will construct a multi-valued bijective map ${ }^{11}$
$$\Psi_{r}: \mathcal{M} \rightarrow \mathfrak{M}$$
such that $q(\mathcal{C})$ is equal to the number of points in $\Psi_{r}(\mathcal{C})$ for each $\mathcal{C} \in \mathcal{M}$ (see Definition 4.8). The construction is similar to that in Section 3.2, but the analysis associated with $\mathbb{R}$-invariant cylinders (in [31]) disappears and the analysis associated with holomorphic tori (in [28]) appears. The map $\Psi_{r}$ is multi-valued because, for a multiply covered special curve, the associated space $\mathcal{Z}_{0}$ may consist of more than a single (possibly non-regular) point. Such a complication was alluded to in Remarks 3.5 and 3.7.

Here is an outline of the following subsections. Section 4.1 preemptively studies the spaces $\mathcal{Z}_{0}$ (given by Definition 3.4) associated with special curves. The knowledge obtained about $\mathcal{Z}_{0}$ is then crucially used in Section 4.2 to construct the multi-valued injective map $\Psi_{r}: \mathcal{M} \rightarrow \mathfrak{M}$. Section 4.3

\footnotetext{
${ }^{11}$ A multi-valued map is bijective if the image of the domain is the full codomain (surjectivity) and the images of any two points in the domain are disjoint (injectivity).
}
then explains surjectivity of $\Psi_{r}$ while Section 4.4 relates the image of $\Psi_{r}$ to the weighted count of points in $\mathcal{M}$, completing the proof of Theorem 4.2.

To further ground the reader, similarly to viewing [32, §5-§7] as a Floer-theoretic variant of the arguments for [29, Proposition 4.1], the upcoming two sections may be viewed as a Floer-theoretic variant of the arguments for [29, Proposition 4.2] which generalizes [29, Proposition 4.1].

\subsection*{4.1 SW instantons from multiply covered tori and planes}

In regards to constructing the analogous bijection $\mathcal{M}_{1}\left(\Theta^{+}, \Theta^{-}\right) \rightarrow \mathfrak{M}_{1}\left(\mathfrak{c}_{\Theta}, \mathfrak{c}_{\Theta+} ; \mathfrak{s}\right)$ over a symplectization (see (3.7)), the analysis in [31] to handle covers of $\mathbb{R}$-invariant cylinders is simple: for an $\mathbb{R}$-invariant cylinder $C=\mathbb{R} \times \gamma$, the section $\mu_{C}$ vanishes and hence the unique "symmetric" vortex which solves (3.2) over $\gamma$ extends to the unique "symmetric" vortex solution to (3.4) over $C$. If $\mu_{C}$ did not vanish, the bundle map $\mathbb{F}$ would prevent such an extension (since $\mathbb{F}(0) \neq 0$ ). This unfortunately turns out to be the case for the special curves in the scenario at hand. The appropriate analysis to handle the special tori is given in [28] and can be mimicked to handle the special planes. A key point to mimicking Taubes' analysis here is that the special planes limit to elliptic orbits with multiplicity one, which allows us to bypass the analysis at the ends in this case and instead places us in the simplified setting [32, §5.a.1].

Proposition 4.3. Let $(C, d)$ be a component of $\mathcal{C} \in \mathcal{M}$ where $C$ is a special curve and $d \geq 1$. Then the subspace $\mathcal{Z}_{0} \subset L_{1}^{2}\left(\bigoplus_{j=1}^{d} N_{C}^{j}\right)$ carved out by (3.4) is compact for generic $J$ as needed to make 1.6 well-defined. If $C$ is furthermore a plane, then by replacing $\mu_{C}$ in the definition of $\mathcal{Z}_{0}$ with $t \mu_{C}$ for any $t \in[0,1]$, the resulting space of sections $\mathcal{Z}_{0}^{t}$ remains compact for each $t$.

Proof. When $C$ is a torus, this is precisely [29, Proposition 2.8] which in turn is the combination of [29, Proposition 2.7] and the fact that $(C, d)$ is " $d$-nondegenerate" (see [25, Lemma 5.4]). When $C$ is a plane, we may copy the proof of [29, Proposition 2.7] in [29, §3] for the analogous case that $C$ is a torus. Strictly speaking, [29], Proposition 2.7] argues that $\mathcal{Z}_{0}$ is compact if and only if certain Cauchy-Riemann type operators associated to multiple covers of $C$ have trivial kernel and cokernel (which is then guaranteed by $d$-nondegeneracy of $C$ ). As the relevant analysis is performed locally along the curve, the argument extends almost verbatim to the case that $C$ is a plane. The argument is actually shorter than that for tori, and what follows is a brief sketch.

Let $\pi: N_{C} \rightarrow C$ denote the normal bundle of $C$ with respect to $\bar{X}_{0}$, and let $s: N_{C} \rightarrow \pi^{*} N_{C}$ denote the tautological section. Define the maps
$$\begin{gathered}
R: L_{1}^{2}\left(\bigoplus_{q=1}^{d} N_{C}^{q}\right) \rightarrow \mathbb{R}, \quad y=\left(y_{1}, \ldots, y_{d}\right) \mapsto \sup _{C} \sup _{q}\left|y_{q}\right|^{1 / q} \\
p: L_{1}^{2}\left(\bigoplus_{q=1}^{d} N_{C}^{q}\right) \rightarrow L_{1}^{2}\left(\pi^{*} N_{C}^{d}\right), \quad y=\left(y_{1}, \ldots, y_{d}\right) \mapsto s^{d}+\pi^{*} y_{1} \cdot s^{d-1}+\cdots+\pi^{*} y_{d}
\end{gathered}$$
and suppose there exists a sequence $\left\{y^{j}\right\}_{j \in \mathbb{N}} \subset \mathcal{Z}_{0}^{t}$ with $R_{j}:=R\left(y^{j}\right)$ increasing and unbounded. Then define the subsets
$$\Sigma_{j}:=\left\{\eta \in N_{C} \mid p\left(y^{j}\right)\left(R_{j} \cdot \eta\right)=0\right\}$$
The proof of [29, Proposition 3.1] shows that a subsequence of $\left\{\Sigma_{j}\right\}_{j \in \mathbb{N}}$ converges pointwise to the image of a somewhere-injective $J^{t}$-holomorphic map $\varphi: C^{\prime} \rightarrow N_{C}$ which does not factor through
the zero-section of $N_{C}$. Here, $J^{t}$ on $T N_{C}=\pi^{*} N \oplus \pi^{*} T C$ is the unique almost complex structure defined by the condition that $T^{1,0} N_{C}$ is locally spanned by $\pi^{*} d z$ and $\left(\nabla s+\pi^{*} \nu_{C} \cdot s+t \cdot \pi^{*} \mu_{C} \cdot \bar{s}\right) \cdot \pi^{*} d \bar{z}$, where ∇ is the Levi-Civita connection induced by the metric on $\bar{X}_{0}$.

Now, the composition $\pi \circ \varphi: C^{\prime} \rightarrow C$ is a $d$-fold (possibly branched ${ }^{12}$ ) holomorphic covering and $\varphi$ defines a nontrivial element in the kernel of the Cauchy-Riemann type operator $D_{\pi \circ \varphi}^{t}$ over $\varphi^{*} \pi^{*} N_{C}$ that is the pull-back of $D^{t}:=\bar{\partial}+\nu_{C}+t \mu_{C}$ over $N_{C}$ (see [38]). But this contradicts "super-rigidity" of $C$ [3, Lemma 3.20]. Thus, $\mathcal{Z}_{0}^{t}$ is compact. \(\square\)

Remark 4.4. Since a special plane $C$ has index zero and satisfies super-rigidity, it may be possible to modify $J$ in a small neighborhood of its image so that $\mu_{C}$ becomes 0, following the methodology of Taubes' $L$-flat approximations in [31, Appendix] (this was suggested by Taubes). The a priori issue is that there may be other nearby $J$-holomorphic curves in $\bar{X}_{0}$ which pop into existence at some point along the smooth path of modifications of $J$, altering the moduli space of curves. If this issue can be dealt with, as in the case of the $L$-flat approximations, then $\mathcal{Z}_{0}$ is a single (regular) point and there is no need for the Kuranishi structures along special planes that appear in Section 4.2.

\subsection*{4.2 Kuranishi structures}

In this section we give a proof of the following.
Proposition 4.5. Let $\Theta, \mathcal{M}, \mathfrak{M}$ be as in Notation 4.1. Given the hypotheses of Theorem 4.2, there is a multi-valued injective map $\Psi_{r}: \mathcal{M} \rightarrow \mathfrak{M}$. It is described in Definition 4.8 and is only multi-valued at those currents in $\mathcal{M}$ which contain a special curve of multiplicity greater than one.

Proof. We closely follow [32, §5-§7] and the analogous [27, §4-§6], while noting that the point/loop constraints cause no changes to the arguments (see [35, §4.e]).

The first main step in [32, §5] is to construct specific configurations $\left(A^{*}, \Psi^{*}\right) \in \operatorname{Conn}(E) \times \Gamma\left(\mathbb{S}_{+}\right)$ for each $\mathcal{C}=\left\{\left(C_{k}, d_{k}\right)\right\}_{k} \in \mathcal{M}$ (and $r \in \mathbb{R}$ ), such that away from $\bigcup_{k} C_{k} \subset \bar{X}_{0}$ the curvature of $A^{*}$ is flat and the $E$-component of $\Psi^{*}$ is covariantly constant. The construction involves patching together local configurations on open sets in $\bar{X}_{0}$. The difference between compact and noncompact $\bar{X}_{0}$ is that, in the noncompact case, there need not be an embedding of a fixed-radius tubular neighborhood of the punctured curves. This complication occurs because the curves may have multiple ends approaching multiple covers of the same Reeb orbit, or an end approaching a multiple cover of a Reeb orbit (see Appendix A). But by [3, Proposition 3.16] this complication does not occur for the special planes - this is important to note because we may now treat special planes and special tori on equal footing.

Fix a $\mathcal{C}=\left\{\left(C_{k}, d_{k}\right)\right\}_{k} \in \mathcal{M}$ and write $\Theta=\left\{\left(\Theta_{i}, m_{i}\right)\right\}_{i}$. The cover of $\bar{X}_{0}$ is prescribed by the bullet points of [32, Equation 5-3] but augmented by a simplified version [32, §5.a. 1 Step 1] over the special curves, and described as follows (a schematic example is depicted in Figure 2):
\begin{itemize}
\item[-] There is an open set $U_{\Theta_{i}}$ for each orbit $\Theta_{i}$ that is not approached by a special plane, such that $U_{\Theta_{i}}$ lives far out on the ends of $\bar{X}_{0}$ and contained in a fixed-radius tubular neighborhood of $\mathbb{R} \times \Theta_{i}$ in that region. These sets are pairwise disjoint.
\end{itemize}

\footnotetext{
${ }^{12}$ The proof of [29] Proposition 2.7] (and in particular, the proof of [29, Proposition 3.2]) for a torus $C$ is more involved because it is shown there that $\pi \circ \varphi: C^{\prime} \rightarrow C$ is unbranched, i.e. the domain $C^{\prime}$ is also a torus.
}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/d787d2b4-e9c9-4ab7-9c05-44a3a9f294e2-26.jpg?height=329&width=477&top_left_y=277&top_left_x=821}
\captionsetup{labelformat=empty}
\caption{Figure 2: $C_{k}$ in black, $U_{C_{k}}$ in red, $U_{\Theta_{i}}$ in blue ( $U_{0}$ not shown)}
\end{figure}
\begin{itemize}
\item[-] There is an open set $U_{C_{k}}$ for each punctured component $C_{k}$ that is not a special plane, such that $U_{C_{k}}$ lives in a compact region of $\bar{X}_{0}$ and contained in a fixed-radius tubular neighborhood of $C_{k}$ in that region - this set does not contain the entire $C_{k}$. These sets are pairwise disjoint and only intersect $U_{\Theta_{i}}$ when $\Theta_{i}$ is approached by $C_{k}$.
\item[-] There is an open set $U_{C_{k}}$ for each closed component and special plane $C_{k}$, given by a fixedradius tubular neighborhood of $C_{k}$. These sets are pairwise disjoint and disjoint from all preceding open sets, which is possible because each special plane is asymptotic to an elliptic orbit with multiplicity one.
\item[-] There is an open set $U_{0}$ to cover the remainder of $\bar{X}_{0}$.
\end{itemize}

Notation 4.6. Let $\Theta^{\prime}$ denote the subset of $\Theta$ consisting of elliptic orbits with multiplicity one that are approached by a special plane, and denote the complement $\Theta^{\prime \prime}=\Theta-\Theta^{\prime}$. Let $\mathcal{C}^{\prime}$ denote the subset of $\mathcal{C}$ consisting of special curves, and denote the complement $\mathcal{C}^{\prime \prime}=\mathcal{C}-\mathcal{C}^{\prime}$. Use $k^{\prime}$ to index the components of $\mathcal{C}^{\prime}$, and use $k^{\prime \prime}$ to index the (remaining) components of $\mathcal{C}^{\prime \prime}$.

As in [32, §5.a] and [27, §2.d], the configuration $\left(A^{*}, \Psi^{*}\right)$ is defined by patching up the configurations respectively on $U_{C_{k}}$ for each $\left(C_{k}, d_{k}\right) \in \mathcal{C}$, on $U_{\Theta_{i}}$ for each $\left(\Theta_{i}, m_{i}\right) \in \Theta$, and on $U_{0}$, defined in the following manner:
\begin{itemize}
\item[-] Over $U_{0}$, we trivialize $\left.E\right|_{U_{0}}=U_{0} \times \mathbb{C}$ and set $A^{*}$ to be the trivial (flat) connection and $\Psi^{*}=\left.(1,0) \in \mathbb{C} \oplus K^{-1}\right|_{U_{0}}$.
\item[-] Over $U_{C}$ for a component $(C, 1) \in \mathcal{C}^{\prime \prime}$, the pair $\left(A^{*}, \Psi^{*}\right)$ is constructed from $\mathfrak{c}=0 \in L_{1}^{2}\left(\mathfrak{C}_{N_{C}, 1}\right)$ via the equations [32, Equation 5-2].
\item[-] Over $U_{\Theta_{i}}$ for an orbit $\left(\Theta_{i}, m_{i}\right) \in \Theta^{\prime \prime}$, after identifying $U_{\Theta_{i}}$ with $(-\infty,-R) \times S^{1} \times \mathbb{C}$ for some $R \gg 1$ via [32, Equation 4-1] ${ }^{13}$, the pair $\left(A^{*}, \Psi^{*}\right)$ is defined by the equations [32, Equation 5-8, Equation 5-9] and constructed from the aforementioned configurations on $U_{0} \cup \bigcup_{(C, 1) \in \mathcal{C}^{\prime \prime}} U_{C}$ (with cutoff functions) and also from $\bigcup_{k} C_{k}$ by viewing the latter as the graph of a map $(-\infty,-R) \times S^{1} \rightarrow \operatorname{Sym}^{m_{i}}(\mathbb{C}) \approx \mathfrak{C}_{m_{i}}$ which sends $(s, t)$ to the set of $m_{i}$ intersections of $\bigcup_{k} C_{k}$ with $(\{(s, t)\} \times \mathbb{C})$ [32, §5.c].
\item[-] Over $U_{C}$ for a component $(C, d) \in \mathcal{C}^{\prime}$, after identifying $U_{C}$ with the unit disk subbundle of $\pi: N_{C} \rightarrow C$ using the exponential map, we set $\left.E\right|_{U_{C}}=\pi^{*} N_{C}^{d}$. The pair $\left(A^{*}, \Psi^{*}\right)$ is constructed from $\mathfrak{c}=0 \in L_{1}^{2}\left(\mathfrak{C}_{N_{C}, d}\right)$ via the analog of equations [32, Equation 5-2] in which
\end{itemize}

\footnotetext{
${ }^{13}$ The $r$-independent lower bound on $R$ depends on $\mathcal{C}$ 32, §4.c].
}
the section $\mathfrak{s} /|\mathfrak{s}|$ (notation of [32, §5.a]) and connection $\theta_{\mathfrak{s}}$ (defined by [32, Equation 5-1]) over $\pi^{*} N_{C}$ are replaced by the induced $\mathfrak{s}^{d} /|\mathfrak{s}|^{d}$ and $d \theta_{\mathfrak{s}}$ over $\pi^{*} N_{C}^{d} .{ }^{14}$
An examination of Taubes' arguments for constructing SW instantons, in particular [32, §7.e.1] and [27, §3.b], leads to the conclusion that the constructions in [32, §5] of $\left(A^{*}, \Psi^{*}\right)$ did not have to require the section $\boldsymbol{\mathfrak { c }}=\left(\mathfrak{c}_{k}\right)_{k} \in \times_{k} L_{1}^{2}\left(\mathfrak{C}_{N_{C_{k}}, d_{k}}\right)$ to be the zero element nor to live in $\times_{k} \mathcal{Z}_{0}^{(k)}$, where $\mathcal{Z}_{0}^{(k)}$ denotes the $\left(C_{k}, d_{k}\right)$ version of (3.4). Instead, it can and will be assumed that $\mathfrak{c}$ belongs to the space
$$\mathcal{Y}:=\left(\times_{k^{\prime}} \mathcal{K}_{\Lambda}^{\left(k^{\prime}\right)}\right) \times\left(\times_{k^{\prime \prime}}\{0\}\right)$$
where $\mathcal{K}_{\Lambda}^{\left(k^{\prime}\right)}$ is a suitably small open neighborhood of $\mathcal{Z}_{0}^{\left(k^{\prime}\right)}$ in $L_{1}^{2}\left(\bigoplus_{j=1}^{d_{k^{\prime}}} N_{C_{k^{\prime}}}^{j}\right)$; this neighborhood will be specified in the upcoming Lemma 4.7 (similar to what is denoted by the same notation in 27). To clarify, recall from Remark 3.7 that all $\mathcal{Z}_{0}^{(k)}$ are regular in the setting of 32. In our context, the versions of $\mathcal{Z}_{0}$ associated to special curves are no longer regular, and the arguments in [32] need to be augmented with the more general gluing arguments from [27, Proposition 5.2]. The version of $\left(A^{*}, \Psi^{*}\right)$ constructed from $\boldsymbol{\mathfrak { c }} \in \mathcal{Y}$ will be denoted henceforth by $\left(A_{\mathfrak{c}}^{*}, \Psi_{\mathbf{c}}^{*}\right)$.

As in [32, §5.b, §5.d], we continue the search for a solution to the large $r$ version of Taubes' perturbed Seiberg-Witten equations (2.2) by considering a family of deformations of $\left(A_{\mathbf{c}}^{*}, \Psi_{\mathbf{c}}^{*}\right)$, i.e. particular families ${ }^{15}\left(A_{\mathbf{c}}^{\xi}(\mathfrak{b}), \Psi_{\mathbf{c}}^{\xi}(\mathfrak{b})\right)$ of configurations parametrized by
$$\begin{aligned}
& \mathfrak{c} \in \mathcal{Y} \\
& \xi \in \mathcal{K}_{\mathfrak{c}} \cap \mathcal{K}_{\mathfrak{c} *} \subset \mathcal{K}_{\mathfrak{c}}:=\left(\times_{k^{\prime}} \mathcal{K}_{\mathfrak{c}_{k^{\prime}}}\right) \times \mathcal{K}^{\prime \prime} \\
& \mathfrak{b} \in \mathbb{H}\left(i T^{*} \bar{X}_{0} \oplus \mathbb{S}_{+}\right)
\end{aligned}$$
Here, each $\mathcal{K}_{\mathfrak{c}_{k^{\prime}}}$ is the space mentioned at the end of Section 3.1, while $\mathcal{K}^{\prime \prime}$ is a Banach space described in the same manner as that in [32, §5.b Step 4] by completing a product space (using the norm defined by [32, Equation 5-13]) whose factors are indexed by the elements $\left(C_{k^{\prime \prime}}, d_{k^{\prime \prime}}\right) \in \mathfrak{C}^{\prime \prime}$ and $\left(\Theta_{i}, m_{i}\right) \in \Theta^{\prime \prime}$ and characterized by [32, Equation 5-12], and $\mathcal{K}_{\mathfrak{c} *}$ is a Banach space similar to $\mathcal{K}_{\mathfrak{c}}$ using slightly different norms (see [32, §5.b Step 4]). Finally, $\mathbb{H}$ is the completion of the space of compactly supported sections of $i T^{*} \bar{X}_{0} \oplus \mathbb{S}_{+}$using the norm defined by [32, Equation 6-2]. Such an element $\xi \in \mathcal{K}_{\mathfrak{c}} \cap \mathcal{K}_{\mathfrak{c} *}$ is used to deform the model configurations $\left(A_{\mathfrak{c}}^{*}, \Psi_{\mathfrak{c}}^{*}\right)$ on the respective open sets $U_{C_{k}}$ and $U_{\Theta_{i}}$ and patching them together: This deformation $\left(A_{\mathfrak{c}}^{\xi}(0), \Psi_{\mathfrak{c}}^{\xi}(0)\right)$ is constructed in exactly the same manner as [32, Equation 5-15] except over the open sets $U_{C}$ for $(C, d) \in \mathcal{C}^{\prime}$ where it is constructed by the analog of [32, Equation 5-11] in which $\pi^{*} N_{C}^{d}$ replaces the bundle $E$ there. Then an element $\mathfrak{b} \in \mathbb{H}$ defines a global perturbation $\left(A_{\mathfrak{c}}^{\xi}(\mathfrak{b}), \Psi_{\mathfrak{c}}^{\xi}(\mathfrak{b})\right)$ of $\left(A_{\mathfrak{c}}^{\xi}(0), \Psi_{\mathfrak{c}}^{\xi}(0)\right)$ by [32, Equation 5-19].

Such a configuration $\left(A_{\mathfrak{c}}^{\xi}(\mathfrak{b}), \Psi_{\mathfrak{c}}^{\xi}(\mathfrak{b})\right)$ solves the large $r$ version of Taubes' perturbed Seiberg-Witten equations when [32, Equation 5-20] (equivalently, [32, Equation 6-1]) is satisfied, written schematically as
$$\begin{gathered}
\mathfrak{D} \mathfrak{b}+r^{1 / 2} \mathfrak{b} * \mathfrak{b}-\mathfrak{v}=0 \\
\lim _{s \rightarrow-\infty} \mathfrak{b}=\mathfrak{b}_{\Theta}
\end{gathered}$$

\footnotetext{
${ }^{14}$ This model also appears in 32 §5.a. 2 Step 2] when $C$ is an $\mathbb{R}$-invariant cylinder in a symplectization.
${ }^{15}$ The corresponding notation in 32 is such that $\left(A_{0}^{\xi}(\mathfrak{b}), \Psi_{0}^{\xi}(\mathfrak{b})\right)$ equals 32 , Equation 5-19] with $\left(A_{0}^{\xi}(0), \Psi_{0}^{\xi}(0)\right)$ denoted by $\left(A^{\xi}, \Psi^{\xi}\right)$.
}
where $\mathfrak{b}_{\Theta}$ is a solution to [32, Equation 3-5]) determined by $\mathfrak{c}_{\Theta}$. Here, $\mathfrak{b} \mapsto \mathfrak{b} * \mathfrak{b}$ denotes an $r$-independent quadratic fiber-preserving map from $i T^{*} \bar{X}_{0} \oplus \mathbb{S}_{+}$to $i \wedge_{+}^{2} T^{*} \bar{X}_{0} \oplus \mathbb{S}_{-}, \mathfrak{D}$ is the deformation operator associated with $\left(A_{\mathfrak{c}}^{\xi}(0), \Psi_{\mathfrak{c}}^{\xi}(0)\right)$, and $\mathfrak{v}$ is the remainder (it is an error term determined by the failure of $\left(A_{\mathfrak{c}}^{\xi}(0), \Psi_{\mathfrak{c}}^{\xi}(0)\right)$ to solve the Seiberg-Witten equations). The idea now is Lyapunov-Schmidt reduction, i.e. to first project (4.1) onto a certain subspace, solve for $\mathfrak{b}$ in terms of $\mathfrak{c}$ and $\xi$ (and $r$ ), and then use the remaining part of (4.1) to solve for $\xi$ in terms of $\mathfrak{c}$.

For each $\boldsymbol{\mathfrak { c }} \in \mathcal{Y}$ and $\xi \in \mathcal{K}_{\mathfrak{c}} \cap \mathcal{K}_{\mathfrak{c} *}$, 32, §6.a] introduces a map $\mathfrak{t}_{\xi}: \mathcal{K}_{\mathfrak{c}}^{2} \rightarrow L^{2}\left(i T^{*} \bar{X}_{0} \oplus \mathbb{S}_{+}\right)$ (see [32, Equation 6-9]), where $\mathcal{K}_{\mathfrak{c}}^{2}$ is the version of $\mathcal{K}_{\mathfrak{c}}$ using the $L^{2}$-norm. Let $\Pi_{\xi}$ denote the $L^{2}$ orthogonal projection onto the image of $\mathfrak{t}_{\xi}$. The result of [32, §6] is a solution to
$$\left(1-\Pi_{\xi}\right)\left(\mathfrak{D} \mathfrak{b}+r^{1 / 2} \mathfrak{b} * \mathfrak{b}\right)=\left(1-\Pi_{\xi}\right) \mathfrak{v}$$
Specifically, [32, Proposition 6.4] solves for $\mathfrak{b}$ as a smooth function of $\{\mathfrak{c}, \xi, r\}$ (using the contraction mapping principle indirectly), given appropriate bounds on $\xi$ and further assuming bounds on a certain term
$$\left(1-\Pi_{\xi}\right)\left(\mathfrak{v}-\mathfrak{v}_{\mathfrak{h}}\right)$$
that appears when (4.2) is rewritten as in [32, §6.c] ( $\mathfrak{v}_{\mathfrak{h}}$ is given by [32, Equation 6-21]). It is shown in [32, Lemma 6.3] that this assumed bound on $\left(1-\Pi_{\xi}\right)\left(\mathfrak{v}-\mathfrak{v}_{\mathfrak{h}}\right)$ is guaranteed when $\mathfrak{c} \in \times_{k} \mathcal{Z}_{0}^{(k)}$, but in general we have to check whether this bound is actually satisfied.

It then remains to solve
$$\Pi_{\xi}\left(\mathfrak{D} \mathfrak{b}+r^{1 / 2} \mathfrak{b} * \mathfrak{b}-\mathfrak{v}\right)=0$$
and also to find those $\boldsymbol{\mathfrak { c }} \in \mathcal{Y}$ for which the term $\left(1-\Pi_{\xi}\right)\left(\mathfrak{v}-\mathfrak{v}_{\mathfrak{h}}\right)$ is suitably bounded. When $\mathfrak{c} \notin \times_{k} \mathcal{Z}_{0}^{(k)}$, the constructions in [32, §7] need to be augmented by the constructions in [27]. Indeed, it is also shown in [32, §7.d] that the related term
$$\Pi_{\xi}\left(\mathfrak{v}-\mathfrak{v}_{\mathfrak{h}}\right)$$
is large when $\mathfrak{c}_{k}$ is far away from $\mathcal{Z}_{0}^{(k)}$, so that (4.3) need not be solvable. What follows are the modifications to [32, §7] that come directly from [27, §5]. Again, it is important to note the special curves $C_{k^{\prime}}$ are disjoint from the other components of $\mathcal{C}$ and only approach embedded Reeb orbits which are furthermore not approached by the other components of $\mathcal{C}$, so the analysis in [27] complements (and does not interfere with) the analysis in 32 , ${ }^{16}$

\footnotetext{
${ }^{16}$ Since the arguments in 27 and 32 follow the same principle of obstructed gluing theory, here are some similarities/differences between the notions and equations in [27, §2-§5] and our setup (which follows [32, §5-§7]). Ignoring contributions from the ends of the curves, our variables $\left\{\mathfrak{c}, \xi, \mathfrak{b}, \mathfrak{v}-\mathfrak{v}_{\mathfrak{h}}\right\}$ may be viewed as analogs of $\left\{y, x, q^{\prime}, \operatorname{err}\right\}$ in [27], though the pairs $(\mathfrak{c}, \xi)$ and $(y, x)$ play different roles in the respective gluing arguments. The respective points of expansion of a tentative Seiberg-Witten solution are $\left(A_{\mathfrak{c}}^{\xi}(0), \Psi_{\mathfrak{c}}^{\xi}(0)\right)$ in our setup and the version of $\left(\underline{a}_{r},\left(\underline{\alpha}_{r}, \underline{\beta}_{r}\right)\right)$ in [27, §3.b] constructed from $y$ (and from $x$ as in 27, Equation 5.10]). This configuration $\left(\underline{a}_{r},\left(\underline{\alpha}_{r}, \underline{\beta}_{r}\right)\right)$ is a modification to the configuration $\left(a_{r},\left(\alpha_{r}, 0\right)\right)$ in 27, §2.d] (whose analog is our $\left(A_{\mathfrak{c}}^{*}, \Psi_{\mathfrak{c}}^{*}\right)$ ) using the "correction" term $u_{r}$ defined by 27. Equation 3.13] (whose analog is part of our $\mathfrak{b}$ ). The Seiberg-Witten equations are then given by Equation (4.1) with linear variable $\mathfrak{b}$ and by 27, Equation 4.2] with linear variable $q^{\prime}$. The argument of 32, §7.d] concerning $\Pi_{\xi}\left(\mathfrak{v}-\mathfrak{v}_{\mathfrak{h}}\right)$ is analogous to that of [27, §5.f] concerning $\Pi$ err.

While we're at it, here is a parallel between the above constructions and the analogous constructions for Reeb orbits, i.e. the construction of $\Theta \mapsto \mathfrak{c}_{\Theta}$ (Theorem 3.6). Our equations (4.1), 4.2), 4.3) are the analogs of [32]. Equation 3-6, Equation 3-16, Equation 3-35]. Solving these equations amounts to a proof of Theorem 3.6 for the following reason: A key lemma [32, Lemma 3.8] guarantees a unique solution to [32, Equation 3-35] whenever $\mathfrak{c} \in \mathcal{Z}_{0}$ with Coker $\Delta_{\mathfrak{c}}=0$, while Theorem 3.2 guarantees that $\mathcal{Z}_{0}=\{0\}$ with Coker $\Delta_{0}=0$; so there is a unique monopole $\mathfrak{c}_{\Theta}$.
}

As in [32, §7], we view the left hand side of (4.3) as a bundle map over $\mathcal{Y}$ given fiberwise by an operator
$$\mathcal{K}_{\mathfrak{c}} \rightarrow \mathcal{L}_{\mathfrak{c}}, \quad \xi \mapsto r^{-1 / 2} \mathcal{T}(\mathfrak{c}, \xi)$$
Here, the Banach space $\mathcal{L}_{\mathfrak{c}}$ is defined similarly to that in 32, §6.a.7] - it is the analog of our $\mathcal{K}_{\mathfrak{c}}$ in which all relevant bundles involved in its definition are tensored with the components $T^{0,1} C_{k}$. We then consider the Taylor expansion
$$\mathcal{T}(\mathfrak{c}, \xi)=\mathcal{T}_{0}(\mathfrak{c})+\mathcal{T}_{1}(\mathfrak{c}) \cdot \xi+\mathcal{T}_{2}(\mathfrak{c}, \xi)$$
where $\mathcal{T}_{0}(\mathfrak{c}):=\mathcal{T}(\mathfrak{c}, 0)$ and $\mathcal{T}_{1}(\mathfrak{c})$ is linear and $\mathcal{T}_{2}(\mathfrak{c}, \cdot)$ is the remainder. In the absence of special curves, the zeros of $\mathcal{T}(\mathbf{c}, \xi)$ are described by [32, Proposition 7.1]. The existence of zeros hinges on appropriate bounds on $\left\{\mathcal{T}_{j}\right\}$ and requires $\mathcal{T}_{1}(\mathbf{c})$ to satisfy additional properties; they are granted as follows:
\begin{itemize}
\item[(i)] the bounds on $\mathcal{T}_{2}$ are established in [32, §7.e.3] and granted by the small norms on $\mathcal{K}_{\mathfrak{c}}$,
\item[(ii)] the bounds on $\mathcal{T}_{0}(\mathfrak{c})$ are established in [32, §7.e.1] and granted by the constraint $\boldsymbol{\mathfrak { c }} \in \times_{k} \mathcal{Z}_{0}^{(k)}$,
\item[(iii)] the properties of $\mathcal{T}_{1}(\mathfrak{c})$ are ultimately granted by the constraint $\bigoplus_{k}$ Coker $\Delta_{\mathfrak{c}_{k}}=0$, which in turn is granted by the fact that $\bigoplus_{k}$ Coker $D_{C_{k}}=0$ for generic $J$ (see Section 3.1).
\end{itemize}

However, for a special curve $C_{k^{\prime}}$ it can be the case that Coker $\Delta_{\mathfrak{c}_{k^{\prime}}} \neq 0$, so item (iii) no longer holds and the proof of [32, Proposition 7.1] needs to be modified. The resolution is to relax the constraint $\mathfrak{c}_{k^{\prime}} \in \mathcal{Z}_{0}^{\left(k^{\prime}\right)}$ (so item (ii) also needs to be modified) and appeal to Kuranishi structures as in the proofs of [27, Lemma 5.1, Proposition 5.2]. We do this now.

Using the fact that $\mathcal{Z}_{0}^{\left(k^{\prime}\right)}$ is compact (Proposition 4.3) we have the following analog of 27, Lemma 5.1] whose proof is contained in [27, §5.a, §5.g.2] ${ }^{17}$

Lemma 4.7. Let $(C, d)$ be a special curve with multiplicity. There exists a finite dimensional vector subspace $\Lambda \subset L_{1}^{2}\left(\bigoplus_{j=1}^{d} N_{C}^{j} \otimes T^{0,1} C\right)$ such that for all $\mathfrak{c} \in \mathcal{Z}_{0}$, the projection of $\Lambda$ onto Coker $\Delta_{\mathfrak{c}}$ is surjective. Denote by $Q_{\Lambda}: L_{1}^{2}\left(\bigoplus_{j=1}^{d} N_{C}^{j} \otimes T^{0,1} C\right) \rightarrow \Lambda$ the $L^{2}$ orthogonal projection. There also exists a smooth $\operatorname{dim}(\Lambda)$-dimensional submanifold $\mathcal{K}_{\Lambda} \subset L_{1}^{2}\left(\bigoplus_{j=1}^{d} N_{C}^{j}\right)$ with compact closure, satisfying the following properties:
\begin{itemize}
\item[1)] If $\mathfrak{c} \in \mathcal{K}_{\Lambda}$ then
$$\left(1-Q_{\Lambda}\right)\left(\bar{\partial} \mathfrak{c}+\nu_{C} \aleph(\mathfrak{c})+\mu_{C} \mathbb{F}(\mathfrak{c})\right)=0$$
\item[2)] $\mathcal{Z}_{0}$ embeds in $\mathcal{K}_{\Lambda}$ as the zero set of the map
$$\psi_{\Lambda}: \mathcal{K}_{\Lambda} \rightarrow \Lambda, \quad \mathfrak{c} \mapsto Q_{\Lambda}\left(\bar{\partial} \mathfrak{c}+\nu_{C} \aleph(\mathfrak{c})+\mu_{C} \mathbb{F}(\mathfrak{c})\right)$$
\item[3)] For a suitably chosen $r$-independent constant $\varepsilon>0$, for each $\mathfrak{c} \in \mathcal{K}_{\Lambda}$ there is some element in $\mathcal{Z}_{0}$ that is within $\varepsilon$ distance (with respect to the $L^{2}$ norm) to $\mathfrak{c}$, and $\left(1-Q_{\Lambda}\right) \Delta_{\mathfrak{c}}$ is surjective.
\end{itemize}

We now show how this lemma is used to modify the arguments in [32, §7], along the lines of the analogous arguments that prove [27, Proposition 5.2]. Still following [32, §7.b.5], we write the

\footnotetext{
${ }^{17}$ The submanifold $\mathcal{K}_{\Lambda}$ in [27, Lemma 5.1] has dimension $d+\operatorname{dim}(\Lambda)$, where $d=\operatorname{ind}_{\mathbb{R}} \Delta$. In our case, $\operatorname{ind}_{\mathbb{R}} \Delta=$ $\operatorname{ind}_{\mathbb{R}} D_{C}=0$. For the reader's benefit, we point out that the integer $d$ is misstated in [27, Lemma 5.1] though correctly stated as $d=2 m(1-g)+m(m+1) n=2 m(n+1-g)+m(m-1) n$ in [27, Proposition 3.2].
}
components of $\mathcal{T}$ as $\left(\left(\mathcal{T}_{C_{k}}\right)_{C_{k} \in \mathcal{C}},\left(\mathcal{T}_{\Theta_{j}}\right)_{\Theta_{j} \in \Theta^{\prime \prime}}\right)$. In terms of the Taylor expansion, each component $\mathcal{T}_{C_{k}}\left(\mathfrak{c}_{k}, \xi_{k}\right)$ equals the sum of the $0{ }^{\text {th }}$ order term
$$\mathcal{T}_{0 C_{k}}\left(\mathfrak{c}_{k}, \xi_{k}\right)=\bar{\partial} \mathfrak{c}_{k}+\nu_{C_{k}} \aleph\left(\mathfrak{c}_{k}\right)+\mu_{C_{k}} \mathbb{F}\left(\mathfrak{c}_{k}\right)+\operatorname{err}$$
and the linear term
$$\mathcal{T}_{1 C_{k}}\left(\mathfrak{c}_{k}, \xi_{k}\right)=\Delta_{\mathfrak{c}_{k}} \xi_{k}+\text { err }$$
and the remainder $\mathcal{T}_{2 C_{k}}\left(\mathfrak{c}_{k}, \xi_{k}\right) .{ }^{18}$ For special curves, the linear term $\mathcal{T}_{1 C_{k^{\prime}}}$ may have nonzero (co)kernel. To deal with this, we first apply the operator $1-Q_{\Lambda}^{\left(k^{\prime}\right)}$ to the $\mathcal{T}_{C_{k^{\prime}}}$ components, and we denote the resulting operator by
$$\mathcal{T}_{Q}:=\left(\left(\left(1-Q_{\Lambda}^{\left(k^{\prime}\right)}\right) \mathcal{T}_{C_{k^{\prime}}}\right)_{C_{k^{\prime}} \in \mathcal{C}^{\prime}},\left(\mathcal{T}_{C_{k^{\prime \prime}}}\right)_{C_{k^{\prime \prime}} \in \mathcal{C}^{\prime \prime}},\left(\mathcal{T}_{\Theta_{j}}\right)_{\Theta_{j} \in \Theta^{\prime \prime}}\right)$$
We then restrict the fiberwise domain of $\mathcal{T}_{Q}$ to $\left(\times_{k^{\prime}} \mathcal{L}_{\mathfrak{c}_{k^{\prime}}}^{\perp}\right) \times \mathcal{K}^{\prime \prime}$, where $\mathcal{L}_{\mathfrak{c}_{k^{\prime}}}^{\perp}$ denotes the $L^{2}$ orthogonal complement of
$$\mathcal{L}_{\mathfrak{c}_{k^{\prime}}}:=\operatorname{Ker}\left(1-Q_{\Lambda}^{\left(k^{\prime}\right)}\right) \Delta_{\mathfrak{c}_{k^{\prime}}} \subset L_{1}^{2}\left(\bigoplus_{j=1}^{d_{k^{\prime}}} N_{C_{k^{\prime}}}^{j}\right)$$
We now rerun [32, §7], with $\mathcal{T}_{Q}$ replacing $\mathcal{T}$, to solve the projected equation $\mathcal{T}_{Q}(\mathfrak{c}, \xi)=0$. In this regard, the aforementioned item (i) is unchanged, item (ii) is now granted by the relaxed constraint $\boldsymbol{\mathfrak { c }} \in \mathcal{Y}$ thanks to Lemma 4.7(1), and item (iii) is now satisfied thanks to Lemma 4.7(3).

The corresponding result of [32, Proposition 7.1, Proposition 7.6$]^{19}$ is an $L^{\infty}$-small ball
$$B \subset \bigoplus_{C \in \mathcal{C}^{\prime \prime}} \operatorname{Ker}\left(D_{C}\right)$$
and map $q_{\mathfrak{c}}: \mathcal{K}_{\mathfrak{c}} \rightarrow \bigoplus_{C \in \mathcal{C}^{\prime \prime}} \operatorname{Ker}\left(D_{C}\right)$ such that the zeros of $\mathcal{T}_{Q}(\mathfrak{c}, \xi)$, as a function of $(\mathfrak{c}, b) \in \mathcal{Y} \times B$, are
$$\xi(\mathfrak{c}, b) \in\left(\times_{k^{\prime}} \mathcal{L}_{\mathfrak{c}_{k^{\prime}}}^{\perp}\right) \times \mathcal{K}^{\prime \prime}$$
given by the restriction of $q_{\mathbf{c}}^{-1}(b)$ to an $L^{\infty}$-small ball (this ball corresponds to that specified in [32, Proposition 6.4]). This association $(\mathfrak{c}, b) \mapsto \xi(\mathfrak{c}, b)$ induces the smooth map
$$\Psi_{\mathcal{C}, r}: \mathcal{Y} \times B \rightarrow \mathcal{B}\left(\mathfrak{c}_{\Theta}, \varnothing ; \mathfrak{s}_{\mathfrak{s}}\right), \quad(\mathfrak{c}, b) \mapsto\left(A_{\mathfrak{c}}^{\xi(\mathfrak{c}, b)}(\mathfrak{b}(\mathfrak{c}, \xi(\mathfrak{c}, b))), \Psi_{\mathfrak{c}}^{\xi(\mathfrak{c}, b)}(\mathfrak{b}(\mathfrak{c}, \xi(\mathfrak{c}, b)))\right)$$
and we note that the pre-image
$$\mathcal{Y}_{\bar{z}, \bar{\eta}}:=\Psi_{\mathcal{C}, r}^{-1}\left(\mathcal{B}\left(\mathfrak{c}_{\Theta}, \varnothing ; \mathfrak{s}_{\mathfrak{s}}, \bar{z}, \bar{\eta}\right)\right) \subset \mathcal{Y} \times B$$

\footnotetext{
${ }^{18}$ The "err" term in $\mathcal{T}_{0 C_{k}}$ is the sum of two parts: $r^{1 / 2} \Pi_{\xi}\left(\mathfrak{D} \mathfrak{b}+r^{1 / 2} \mathfrak{b} * \mathfrak{b}-\mathfrak{v}\right)-r^{1 / 2} \Pi_{\xi}\left(\mathfrak{v}-\mathfrak{v}_{\mathfrak{h}}\right)$ evaluated at $\xi=0$ (which is bounded similarly to that done in 32. §7.b.2, §7.b.3]), and $r^{1 / 2} \Pi_{\xi}\left(\mathfrak{v}-\mathfrak{v}_{\mathfrak{h}}\right)-\left(\bar{\partial} \mathfrak{c}_{k}+\nu_{C_{k}} \aleph\left(\mathfrak{c}_{k}\right)+\mu_{C_{k}} \mathbb{F}\left(\mathfrak{c}_{k}\right)\right)$ evaluated at $\xi=0$ (which is bounded similarly to that done in 32. §7.d.1, §7.d.2]). The "err" term in $\mathcal{T}_{1 C_{k}}$ is the difference between $\Delta_{\mathfrak{c}_{k}} \xi_{k}$ and a directional derivative of $r^{1 / 2} \Pi_{\xi}\left(\mathfrak{v}-\mathfrak{v}_{\mathfrak{h}}\right)$ at $\xi=0$ (similar to 32, §7.e.2]).
${ }^{19}$ The vector space $V_{0}:=\bigoplus \operatorname{Ker}\left(D_{C}\right)$ is constructed more generally in [32, Equation 7-43], but thanks to the asymptotics of our currents $\mathcal{C}$ and contact form $\lambda_{\mathfrak{s}}$, there are no contributions from what is denoted $V_{\gamma \pm, k}$ there (its dimension [33, Equation 3-44] is zero).
}
is diffeomorphic to $\times_{k^{\prime}} \mathcal{K}_{\Lambda}^{\left(k^{\prime}\right)}$ because no special curve $C_{k^{\prime}}$ intersects the points $\bar{z}$ and loops $\bar{\eta}$ (see also [35, Proposition 4.2] and [29, Proposition 2.10]). It remains to find those $\boldsymbol{\mathfrak { c }} \in \mathcal{Y}_{\bar{z}, \bar{\eta}}$ that will satisfy $\Psi_{\mathcal{C}, r}(\mathfrak{c}) \in \mathfrak{M}$.

The evaluation of the projection $Q_{\Lambda}^{\left(k^{\prime}\right)} \mathcal{T}_{C^{\prime}}$ defines the smooth map ${ }^{20}$
$$\psi_{\mathcal{C}, r}: \mathcal{Y} \times B \rightarrow \bigoplus_{k^{\prime}} \Lambda_{k^{\prime}}, \quad(\mathfrak{c}, b) \mapsto \bigoplus_{k^{\prime}}\left[\psi_{\Lambda}^{\left(k^{\prime}\right)}\left(\mathfrak{c}_{k^{\prime}}\right)+Q_{\Lambda}^{\left(k^{\prime}\right)}\left(\Delta_{\mathfrak{c}_{k^{\prime}}} \xi(\mathfrak{c}, b)_{k^{\prime}}+\mathcal{R}_{C_{k^{\prime}}}\left(\mathfrak{c}_{k^{\prime}}, \xi(\mathfrak{c}, b)_{k^{\prime}}\right)\right)\right]$$
where $\mathcal{R}_{C_{k^{\prime}}}$ denotes the sum of $\mathcal{T}_{2 C_{k^{\prime}}}$ and the "err" terms, and we note that by construction,
$$\psi_{\mathcal{C}, r}^{-1}(0) \cap \mathcal{Y}_{\bar{z}, \bar{\eta}}=\Psi_{\mathcal{C}, r}^{-1}(\mathfrak{M})$$
As explained in [27, §6] and 35, §4] (see also [29, Property 2.22]), $\Psi_{\mathcal{C}, r}$ is a smooth embedding for sufficiently large $r$, it maps $\psi_{\mathcal{C}, r}^{-1}(0) \cap \mathcal{Y}_{\bar{z}, \bar{\eta}}$ homeomorphically onto a subset of $\mathfrak{M}$, and the images of $\left\{\Psi_{\mathcal{C}, r}\right\}_{\mathcal{C} \in \mathcal{M}}$ in $\mathcal{B}\left(\mathfrak{c}_{\Theta}, \varnothing ; \mathfrak{s}_{\mathfrak{s}}\right)$ are disjoint. (In this regard, each image $\operatorname{Im} \Psi_{\mathcal{C}, r}$ constitutes a "Kuranishi model" for a subset of $\mathfrak{M}$.) We can now state the anticipated correspondence between $\mathcal{M}$ and $\mathfrak{M}$, completing the proof of Proposition 4.5.

Definition 4.8. The multi-valued injective map $\Psi_{r}: \mathcal{M} \rightarrow \mathfrak{M}$ is given by the composition
$$\mathcal{C} \mapsto \psi_{\mathcal{C}, r}^{-1}(0) \cap \mathcal{Y}_{\bar{z}, \bar{\eta}} \mapsto \Psi_{\mathcal{C}, r}\left(\psi_{\mathcal{C}, r}^{-1}(0) \cap \mathcal{Y}_{\bar{z}, \bar{\eta}}\right)$$
where the first map is multi-valued and the second map is injective. \(\square\)

\subsection*{4.3 Surjectivity of $\Psi_{r}$}

In this section we give a proof of the following.
Proposition 4.9. Given the hypotheses of Theorem 4.2, Proposition 4.5's map $\Psi_{r}$ is surjective.
Its proof uses the upcoming Lemma 4.10 numerous times along with other estimates established in [26] on closed symplectic manifolds and in 34 on symplectizations. It is explained in [13, §7] how the estimates from [34] on a symplectization carry over, with minor modifications, to exact symplectic cobordisms. For everything to carry over to strong (non-exact) symplectic cobordisms, such as $\left(X_{0}, \omega\right)$, we sometimes must make an additional modification. We will elaborate on these modifications when necessary.

Lemma 4.10. There exists $\kappa \geq 1$ such that if $r \geq \kappa$ and if ( $A, \Psi=(\alpha, \beta)$ ) solves Taubes' perturbed Seiberg-Witten equations (2.2) on $\bar{X}_{0}$ then
$$\begin{gathered}
|\alpha| \leq 1+\kappa r^{-1} \\
|\beta|^{2} \leq \kappa r^{-1}\left(1-|\alpha|^{2}\right)+\kappa^{2} r^{-2}
\end{gathered}$$

\footnotetext{
${ }^{20}$ This map appears in Taubes' papers as [27, Equation 5.21].
}

Proof. This was already stated in [13, Lemma 7.3] for exact symplectic cobordisms, and there are no changes in general. In fact, the proof follows the arguments in [26, Proposition 2.1, Proposition 2.3] on the compact region $X_{0}$ of $\bar{X}_{0}$. Those arguments extend over the ends $(-\infty, 0] \times \partial X_{0}$ of $\bar{X}_{0}$, as in the case of symplectizations [34, Lemma 3.1], because the analogous bounds on the monopoles over $\partial X_{0}$ are granted by [34, Lemma 2.3]. We now outline the proof.

From $D_{\mathbf{A}} \Psi=0$ we know that $D_{\mathbf{A}}^{*} D_{\mathbf{A}} \Psi=0$. We rewrite this equation using the Bochner-Weitzenböck formula,
$$\nabla_{\mathbf{A}}^{*} \nabla_{\mathbf{A}} \Psi+\frac{R_{g}}{4} \Psi+\frac{1}{2} \mathrm{cl}_{+}\left(F_{\mathbf{A}}^{+}\right) \Psi=0$$
where $R_{g}$ denotes the Ricci scalar curvature of $g$ on $\bar{X}_{0}$. Introducing the components $\Psi=(\alpha, \beta)$,
$$\alpha=\frac{1}{2}\left(1+\frac{i}{2} \operatorname{cl}_{+}(\widehat{\omega})\right) \Psi, \quad \beta=\frac{1}{2}\left(1-\frac{i}{2} \operatorname{cl}_{+}(\widehat{\omega})\right) \Psi$$
we take the inner products of (4.5) with $\Psi$ and $(\alpha, 0)$ and $(0, \beta)$ separately. We then apply the maximum principle (using [34, Lemma 2.3] as $s \rightarrow-\infty$ on the ends of $\bar{X}_{0}$ ) to each of the resulting equations. Then we combine all of the resulting inequalities to get the asserted bounds. \(\square\)

Proof of Proposition 4.9. With appropriate modifications coming from [10,13], we will follow the proof of [34, Theorem 1.2] and the proof of [29, Proposition 2.10]. We note again that the point/loop constraints do not affect the arguments (see also [35, §4.e]), so no further comments will be made about them.

Assume first that special curves do not exist. The proof of [34, Theorem 1.2] can then be copied to show that $\Psi_{r}$ is surjective, albeit with the following modifications that are also explained in [13, §7] and [10] ${ }^{21}$ We must replace the manifold $\mathbb{R} \times M$ by $\bar{X}_{0}$ and introduce a piecewise-smooth function $s_{*}: \bar{X}_{0} \rightarrow(-\infty, 0]$ that agrees with the $(-\infty, 0]$ coordinate on each cylindrical end of $\bar{X}_{0}$ and equals 0 on $X_{0}$. Then we replace the subsets $\left[s_{1}, s_{2}\right] \times M$ by $s_{*}^{-1}\left(\left[s_{1}, s_{2}\right]\right)$, the 2-form $d s \wedge a+\frac{1}{2} * a$ by $\widehat{\omega}$, the 2-form $\frac{\partial}{\partial s} A \pm B_{A}$ by $F_{A}^{ \pm}$(for a given SW instanton $\mathfrak{d}=[A,(\alpha, \beta)] \in \mathfrak{M}$ ), and the spectral flow $f_{\mathfrak{d}}$ by $\operatorname{ind}\left(\mathfrak{D}_{\mathfrak{d}}\right)$. Most importantly, we must replace the first assertion of the key lemma [34, Lemma 6.1] with the following key lemma, which asserts that SW instantons on a symplectic cobordism give rise to pseudoholomorphic curves.

Lemma 4.11. Fix a nondegenerate monopole $\mathfrak{c} \in \mathfrak{M}\left(-\partial X_{0}, \mathfrak{s}_{\xi_{0}}+1\right)$. Let $[A,(\alpha, \beta)]$ be an element of $\mathfrak{M}_{I}\left(\mathfrak{c}, \varnothing ; \mathfrak{s}_{\mathfrak{s}}, \bar{z}, \bar{\eta}\right)$ for $r$ sufficiently large. Then
$$E(\mathfrak{c})<2 \pi \rho_{\mathfrak{s}}$$
and there exists a current $\mathcal{C} \in \mathcal{M}_{I}\left(\varnothing, \Theta ; \tau_{\omega}(\mathfrak{s}), \bar{z}, \bar{\eta}\right)$ asymptotic to the admissible orbit set $\Theta$ determined by $\mathfrak{c}$ in Theorem 3.6. Furthermore, given a real number $\delta>0$ there exists a real number $r_{\delta} \geq 1$ such that
$$\sup _{z \in \mathcal{C}} \operatorname{dist}\left(z, \alpha^{-1}(0)\right)+\sup _{z \in \alpha^{-1}(0)} \operatorname{dist}(\mathcal{C}, z)<\delta$$
whenever $r \geq r_{\delta}$.

\footnotetext{
${ }^{21}$ The reader of 13 34, will notice the appearance of the "Seiberg-Witten action," denoted by $\mathfrak{a}$ in 34, Equation 3-2] and [13. Equation 97]. In the context of our paper, it is a gauge-invariant functional $\mathfrak{a}: \mathcal{B}\left(S^{1} \times S^{2}, \mathfrak{s}_{\xi_{0}}+1\right) \rightarrow \mathbb{R}$ because $\mathfrak{s}_{\xi_{0}}+1$ is a torsion spin-c structure. It differs from the Chern-Simons-Dirac functional $\mathcal{L}_{\text {CSD }}$ by an $O(r)$ constant, and its set of critical points is precisely the moduli space of monopoles $\mathfrak{M}\left(S^{1} \times S^{2}, \mathfrak{s}_{\xi_{0}}+1\right)$.
}

We postpone the proof of this lemma until the end of this section. The remaining modifications to the proof of [34, Theorem 1.2] are as follows. As explained in [13, §7], the arguments in [34, §3-5] over symplectizations are replaced by the corresponding arguments in [13, §7.3-7.5] over exact symplectic cobordisms. Then as explained more generally in [10] over strong (non-exact) symplectic cobordisms, they are further augmented over our symplectic cobordism $\left(X_{0}, \omega\right)$ so that:
\begin{itemize}
\item[-] the (broken) pseudoholomorphic curves represent the relative homology class $\tau_{\omega}(\mathfrak{s})$, and
\item[-] the energy bounds on the SW monopoles over $\partial X_{0}$ are increased by the amount $2 \pi \rho_{\mathfrak{s}}$.
\end{itemize}
For example, these two bulleted statements are apparent in the statement of Lemma 4.11.
Assume now that special curves exist, and note that Lemma 4.11 does not depend on the existence of special curves or lack thereof. To prove surjectivity of $\Psi_{r}$ in general it remains to further modify the proof of [34, Theorem 1.2] to show that each element $\mathfrak{d} \in \mathfrak{M}$ lies in the image of $\Psi_{\mathcal{C}, r}$ for the element $\mathcal{C} \in \mathcal{M}$ afforded by Lemma 4.11. This is precisely the final assertion of [29], Proposition 2.10] for $\bar{X}_{0}$ closed, which as explained in [29, §5], is a special case of [29, Proposition 5.1]. We now explain these modifications in our scenario.

When following the proof of [34] Theorem 1.2] to prove surjectivity of $\Psi_{r}$, we make use of a refinement of Lemma 4.11: The bound $\delta$ on the Hausdorff distance in (4.6) is replaced by $\delta r^{-1 / 2}$. The analogous statement is [34, Lemma 6.2] which refines [34, Lemma 6.1], and its proof in [34, §7] extends (without further modifications than the ones already listed) to our scenario in the absence of special curves. Taubes remarks at the beginning of [34, §7] that the arguments for [34, Lemma 6.2] closely follow the arguments in [29, §5] for [29, Proposition 5.1], so by explaining how the proof of [29] Proposition 5.1] extends to our scenario we will have simultaneously explained why this refinement of Lemma 4.11 holds in the presence of special curves.

Remark 4.12. The relevant arguments from [34, §7] and [29, §5] involve "special sections" of powers of $N_{C_{k}}$ associated with any component $\left(C_{k}, d_{k}\right) \in \mathcal{C}$, denoted by $\mathfrak{o}$ in [34]. Equation 7-9] and by $h$ in [29, Equation 5.26]; they differ by an inconsequential factor of $\frac{1}{d_{k} \pi}$. In this regard, Taubes also remarks at the beginning of [34, §7] that [29, Lemma 5.5] (which is used to prove [29, Proposition 5.1]) is flawed and must be replaced by [34, Lemma 7.1]. For the convenience of the reader, here is a further dictionary: [29, Lemma 5.4] corresponds to [34, Lemma 4.10] ${ }^{22}$ while 29, Lemma 5.8] corresponds to [34, Lemma 7.2].

The proof of [29], Proposition 5.1] can be copied for the following reason. We have already explained in Sections 4.1+ 4.2 that special planes and special tori may be treated on equal footing, in the sense that they are endowed with an embedded fixed-radius tubular neighborhood (through their normal bundle), they are $d$-nondegenerate (for a given multiplicity $d \geq 1$ ), and their associated space $\mathcal{Z}_{0}$ (given by Definition 3.4) is compact. Thus, those aspects of the proof of [29], Proposition 5.1] referring to a multiply covered special torus may now refer to any multiply covered special curve. The remaining aspects of the proof of [29, Proposition 5.1] consist of local arguments which carry over to our scenario in addition to the analogous arguments in [34, §7]. ${ }^{23}$ \(\square\)

\footnotetext{
${ }^{22}$ There is a typo in the statement of [34, Lemma 4.10]: replace the word "least" with "most" in the last sentence.
${ }^{23}$ The proof of [29, Proposition 5.1] hinges on [29, Proposition 5.3, Lemma 5.10], particularly the assertion that at least one of the "special sections" $\mathfrak{o}$ is nontrivial. Some details to the proof of this assertion are lacking in 29], but are found by mimicking the proof of [34, Lemma 7.4] (private communication with Taubes). In this regard, we warn the reader that the statement of 34. Lemma 7.4] is technically incorrect but fixed by replacing the constraint $\rho \in\left[\chi \delta_{n} r_{n}^{-1 / 2}, \kappa^{-2}\right]$ with $\rho=\chi \delta_{n} r_{n}^{-1 / 2}$.
}

Proof of Lemma 4.11. We start with the following lemma, which is proved more generally in [10] for strong symplectic cobordisms. It is the analog of [13, Proposition 5.2] over exact symplectic cobordisms and of [26, Theorem 1.3] over closed symplectic manifolds.

Lemma 4.13. Let $[A,(\alpha, \beta)]$ be an element of $\mathfrak{M}_{I}\left(\mathfrak{c}, \varnothing ; \mathfrak{s}_{\mathfrak{s}}, \bar{z}, \bar{\eta}\right)$ for $r$ sufficiently large. Then $E(\mathfrak{c})<2 \pi \rho_{\mathfrak{s}}$, and there exists a (possibly broken) $J$-holomorphic curve $\mathcal{C}$ which contains $\bar{z} \cup \bar{\eta}$, has total homology class $\tau_{\omega}(\mathfrak{s})$, and is asymptotic to the admissible orbit set $\Theta$ determined by $\mathfrak{c}$ in Theorem 3.6.

Now thanks to [3, Proposition 3.13], $\mathcal{C}$ is in fact unbroken. It then also has ECH index $I$, thanks to [2, Theorem 5.1]. To elaborate on the previous sentence, $\alpha^{-1}(0)$ is close (with respect to the Hausdorff distance) to the image of $\mathcal{C}$ in $\bar{X}_{0}$ for $r$ sufficiently large, and it determines a relative homology class $Z_{\alpha} \in H_{2}\left(\bar{X}_{0}, \varnothing, \Theta\right)$ such that $[\mathcal{C}]=Z_{\alpha}$. Thus, $I(\mathcal{C})=I\left(Z_{\alpha}\right)$, and the fact that $I\left(Z_{\alpha}\right)=I$ is the content of [2, Theorem 5.1] ${ }^{24}$

The proof of the remaining part of Lemma 4.11 follows that of [13, Proposition 7.1]. \(\square\)

\subsection*{4.4 Proof of Theorem 4.2}

We now combine the results of the previous sections. Especially in this section, we use $\mathbb{Z} / 2 \mathbb{Z}$ coefficients and hence ignore orientations.

Proof of Theorem 4.2. As a warm-up case, suppose that $\mathcal{M}$ does not contain any elements with special curve components. Propositions 4.5 and 4.9 then imply that $\Psi_{r}$ is an honest bijection ${ }^{25}$
$$\mathcal{M} \longleftrightarrow \mathfrak{M}$$
and the desired result follows immediately.
As a second warm-up case, make the following assumptions: $I=0$, and each space $\mathcal{Z}_{0}^{\left(k^{\prime}\right)}$ associated with any special curve $\left(C_{k^{\prime}}, d_{k^{\prime}}\right) \in \mathcal{C} \in \mathcal{M}$ consists of only regular points. Since each $\mathcal{Z}_{0}^{\left(k^{\prime \prime}\right)}$ associated with any non-special curve $\left(C_{k^{\prime \prime}}, 1\right) \in \mathcal{C} \in \mathcal{M}$ is identified with $\operatorname{Ker}\left(D_{C_{k^{\prime \prime}}}\right)$ (see Section 3.1), the former assumption implies that $\mathcal{Z}_{0}^{\left(k^{\prime \prime}\right)}$ is a single point for generic $J$ as needed to make 1.6 well-defined. Since each $\mathcal{Z}_{0}^{\left(k^{\prime}\right)}$ associated with a special curve is compact by Proposition 4.3, the latter assumption implies that $\mathcal{Z}_{0}^{\left(k^{\prime}\right)}$ is a finite set of points. Propositions 4.5 and 4.9 then imply that $\Psi_{r}$ induces a bijection ${ }^{26}$
$$\bigcup_{\left\{\left(C_{k}, d_{k}\right)\right\} \in \mathcal{M}} \times_{k} \mathcal{Z}_{0}^{(k)} \longleftrightarrow \mathfrak{M}$$
In order to finish the proof of Theorem 4.2 in this case, we need to show that the number of points in each $\mathcal{Z}_{0}^{(k)}$ is equivalent modulo 2 to $r\left(C_{k}, d_{k}\right)$, where $r(C, d)$ is the integer weight attached to each component $(C, d) \in \mathcal{C}$ such that $q(\mathcal{C})= \pm \prod_{(C, d) \in \mathcal{C}} r(C, d)$ (see 3, §3.5]). The proof of such equality will be subsumed in the proof of the general scenario, where $\mathcal{Z}_{0}^{(k)}$ may also contain non-regular points.

\footnotetext{
${ }^{24}$ The proof of [2, Theorem 5.1] over symplectic cobordisms mimics that given in [33, §2.b, §2.c] of the analogous statement over symplectizations.
${ }^{25}$ This bijection is the analog of [31], Theorem 4.3] over symplectizations and of [29, Proposition 2.6] over closed symplectic manifolds.
${ }^{26}$ This bijection is the analog of [29, Proposition 2.9] over closed symplectic manifolds.
}

Consider now the general scenario. Propositions 4.5 and 4.9 then reduce Theorem 4.2 to the following claim:
$$\prod_{k^{\prime}} r\left(C_{k^{\prime}}, d_{k^{\prime}}\right) \equiv\left|\psi_{\mathcal{C}, r}^{-1}(0) \cap \mathcal{Y}_{\bar{z}, \bar{\eta}}\right| \quad \bmod 2$$
where $k^{\prime}$ indexes over the set of special curve components $\mathcal{C}^{\prime}$. We establish this claim in two steps.
Step 1. As explained in [29, §2.g.2], there is a well-defined weight
$$r^{\prime}\left(C_{k^{\prime}}, d_{k^{\prime}}\right) \in \mathbb{Z} / 2 \mathbb{Z}$$
given by the (modulo 2) count of zeros of any smooth perturbation $w: \mathcal{K}_{\Lambda}^{\left(k^{\prime}\right)} \rightarrow \Lambda_{k^{\prime}}$ of the map $\psi_{\Lambda}^{\left(k^{\prime}\right)}: \mathcal{K}_{\Lambda}^{\left(k^{\prime}\right)} \rightarrow \Lambda_{k^{\prime}}$ from Lemma 4.7, such that $|w|<\left|\psi_{\Lambda}^{\left(k^{\prime}\right)}\right|$ on the complement of a compact neighborhood of $\mathcal{Z}_{0}^{\left(k^{\prime}\right)}$ and such that $\psi_{\Lambda}^{\left(k^{\prime}\right)}+w$ has only nondegenerate zeros. In particular, if $\mathcal{Z}_{0}^{\left(k^{\prime}\right)}$ is a finite set of regular points then $r^{\prime}\left(C_{k^{\prime}}, d_{k^{\prime}}\right)$ is its cardinality.