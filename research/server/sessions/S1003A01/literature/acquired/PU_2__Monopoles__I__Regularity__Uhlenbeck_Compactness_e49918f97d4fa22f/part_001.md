---
retention_scope: session
part: 1
total_parts: 7
---

[Part 1/7 of: PU(2) Monopoles, I: Regularity, Uhlenbeck Compactness ...]

---
source_file: dg-ga_9710032.pdf
converter: mathpix
format: mmd
---

\title{
PU(2) MONOPOLES, I: REGULARITY, UHLENBECK COMPACTNESS, AND TRANSVERSALITY ${ }^{1}$
}

\author{
PAUL M. N. FEEHAN AND THOMAS G. LENESS
}

\section*{1. Introduction}

At seminars at Harvard and MIT, during October 1994, Edward Witten introduced the U(1) monopole equations and the Seiberg-Witten invariants to smooth four-manifold topology and conjectured their relationship with Donaldson invariants on the basis of new developments in quantum field theory [19, 98]. The conjecture, recently extended in [60], has been verified for all four-manifolds whose Donaldson and Seiberg-Witten invariants have been independently computed. Within two months of Witten's announcement, a program was outlined by V. Pidstrigach and A. Tyurin and others which should lead to a mathematical proof of the relationship between these two invariants [68, 71, 74]. This approach is unrelated to the quantum field-theoretic arguments of [60, 98] and uses a moduli space of PU(2) monopoles to construct a cobordism between links of Seiberg-Witten moduli spaces of U(1) monopoles and the Donaldson moduli space of anti-self-dual connections, which appear as singularities in this larger stratified moduli space.

It was soon recognized, however, that despite the appeal and elegance of the PU(2) monopole program, its implementation involves substantial technical difficulties due to the contributions of moduli spaces of U(1) monopoles in the lower levels of the Uhlenbeck compactification of the moduli space of PU(2) monopoles. Many of these difficulties had never been resolved even in the case of Donaldson theory where similar problems arise, albeit in a rather simpler form, in attempts to prove the Kotschick-Morgan conjecture for Donaldson invariants of four-manifolds $X$ with $b^{+}(X)=1$. That conjecture asserts that the Donaldson invariants computed using metrics lying in different chambers of the positive cone of $H^{2}(X ; \mathbb{R}) / \mathbb{R}^{*}$ differ by terms depending only the homotopy type of $X$ [45]. In the case of the Kotschick-Morgan conjecture, the heart of the problem lies in describing the links of the lower-level reducibles via gluing and then in calculating the pairings of the Donaldson cohomology classes with those links. Thus far, such links have been described and their pairings with cohomology classes computed only in certain special cases [14, 15, 16, 20, 21, 32, 58, 99]. The methods used to obtain these special cases fall very far short of the

\footnotetext{
${ }^{1}$ Journal of Differential Geometry, to appear. Submitted September 11, 1996, and in revised form, May 5, 1997. This version: October 29, 1997. dg-ga/9710032
The first author was supported in part by an NSF Mathematical Sciences Postdoctoral Fellowship under grant DMS 9306061.
}
kind of general analysis needed to prove the Kotschick-Morgan conjecture. On the other hand, by assuming the Kotschick-Morgan conjecture, L. Göttsche computed the coefficients of the wall-crossing formula in [45] in terms of modular forms by exploiting the presumed homotopy invariance of the coefficients [35]. A related approach to the Witten conjecture was proposed by Pidstrigach and Tyurin [72]. Certain aspects of the PU(2) monopole program have been considered from a quantum-field theoretic viewpoint in [13, 38, 39, 50, 51, 52, 53].

In the present article and its sequels [25, 26, 27] we address the analytical problems associated with constructing the links of lower-level Seiberg-Witten moduli spaces and in establishing the analogues of the Kotschick-Morgan conjecture for PU(2) monopoles needed to compute the pairings of cohomology classes with these links. We hope to return to the actual computations and a verification of Witten's conjecture [60, 98] in a subsequent paper. In this article we describe the basic regularity, Uhlenbeck compactness, and transversality results we need for the moduli space of PU(2) monopoles and in the sequels [26, 27] we develop the gluing theory required to construct the links of the lower-level Seiberg-Witten moduli spaces. An announcement of the main results of the this article appeared in [24].

\subsection*{1.1. Statement of results.}
1.1.1. PU(2) monopoles and holonomy perturbations. We consider Hermitian twoplane bundles $E$ over $X$ whose determinant line bundles $\operatorname{det} E$ are isomorphic to a fixed Hermitian line bundle over $X$ endowed with a fixed $C^{\infty}$, unitary connection. Let $\left(\rho, W^{+}, W^{-}\right)$be a spin ${ }^{c}$ structure on $X$, where $\rho: T^{*} X \rightarrow \operatorname{End} W$ is the Clifford map, and the Hermitian four-plane bundle $W=W^{+} \oplus W^{-}$is endowed with a $C^{\infty}$ spin ${ }^{c}$ connection.

Let $k \geq 3$ be an integer and let $\mathcal{A}_{E}$ be the space of $L_{k}^{2}$ connections $A$ on the U(2) bundle $E$ all inducing the fixed determinant connection on $\operatorname{det} E$. Equivalently, following [48, §2(i)], we may view $\mathcal{A}_{E}$ as the space of $L_{k}^{2}$ connections $A$ on the PU(2) = $\operatorname{SO}(3)$ bundle $\mathfrak{s u}(E)$. We pass back and forth between these viewpoints, via the fixed connection on $\operatorname{det} E$, and rely on the context to make the distinction clear. Given a connection $A$ on $\mathfrak{s u}(E)$ with curvature $F_{A} \in L_{k-1}^{2}\left(\Lambda^{2} \otimes \mathfrak{s} \mathfrak{o}(\mathfrak{s} \mathfrak{u}(E))\right)$, then $\operatorname{ad}^{-1}\left(F_{A}^{+}\right) \in$ $L_{k-1}^{2}\left(\Lambda^{+} \otimes \mathfrak{s} \mathfrak{u}(E)\right)$ is its self-dual component, viewed as a section of $\Lambda^{+} \otimes \mathfrak{s} \mathfrak{u}(E)$ via the isomorphism $\operatorname{ad}: \mathfrak{s u}(E) \rightarrow \mathfrak{s o}(\mathfrak{s u}(E))$. When no confusion can arise, the isomorphism ad : $\mathfrak{s u}(E) \rightarrow \mathfrak{s o}(\mathfrak{s u}(E))$ will be implicit and so we regard $F_{A}$ as a section of $\Lambda^{+} \otimes \mathfrak{s u}(E)$ when $A$ is a connection on $\mathfrak{s} \mathfrak{u}(E)$. Let $D_{A}: L_{k}^{2}\left(W^{+} \otimes E\right) \rightarrow L_{k-1}^{2}\left(W^{-} \otimes E\right)$ be the corresponding Dirac operator.

For an $L_{k}^{2}$ section $\Phi$ of $W^{+} \otimes E$, let $\Phi^{*}$ be its pointwise Hermitian dual and let $\left(\Phi \otimes \Phi^{*}\right)_{00}$ be the component of the Hermitian endomorphism $\Phi \otimes \Phi^{*}$ of $W^{+} \otimes E$ which lies in $\mathfrak{s u}\left(W^{+}\right) \otimes \mathfrak{s u}(E)$. The Clifford multiplication $\rho$ defines an isomorphism $\rho: \Lambda^{+} \rightarrow \mathfrak{s u}\left(W^{+}\right)$and thus an isomorphism $\rho=\rho \otimes \mathrm{id}_{\mathfrak{s u}(E)}$ of $\Lambda^{+} \otimes \mathfrak{s u}(E)$ with
$\mathfrak{s} \mathfrak{u}\left(W^{+}\right) \otimes \mathfrak{s} \mathfrak{u}(E)$. Then
$$\begin{aligned}
F_{A}^{+}-\rho^{-1}\left(\Phi \otimes \Phi^{*}\right)_{00} & =0 \\
D_{A} \Phi & =0
\end{aligned}$$
are the unperturbed PU(2) monopole equations considered in [67, 68, 71, 74], with a slightly differing trace conditions (see below), for a pair $(A, \Phi)$ consisting of a connection on $\mathfrak{s u}(E)$ and a section $\Phi$ of $W^{+} \otimes E$.

Donaldson's proof of the connected-sum theorem for his polynomial invariants [18, Theorem B] makes use of certain 'extended anti-self-dual equations' [18, Equation (4.24)] to which the Freed-Uhlenbeck generic metrics theorem does not apply [18, §4(v)]. These extended equations model a neighborhood of the product connection appearing in the Uhlenbeck compactification of the moduli space of anti-self-dual SU(2) connections. To obtain transversality for the zero locus of the extended equations, he employs holonomy perturbations which give gauge-equivariant $C^{\infty}$ maps $\mathcal{A}_{E}^{*}(X) \rightarrow \Omega^{+}(\mathfrak{s u}(E))$ which are then used to perturb the extended anti-self-dual equations [17, §2], [18, pp. 282-287]. These perturbations are continuous with respect to Uhlenbeck limits and yield transversality not only for the top-level moduli space, but also for all lower-level moduli spaces and for all intersections of the geometric representatives defining the Donaldson invariants.

In §2.5.2 and in the Appendix we describe a generalization of Donaldson's idea which we use to prove transversality for the moduli space of solutions to a perturbed version of the PU(2) monopole equations (1.1). Unfortunately, in the case of the moduli space of PU(2) monopoles, the analysis is considerably more intricate and the method we employ here is rather different to the one developed in [18]. We use an infinite sequence of holonomy sections defined on the infinite-dimensional configuration space of pairs; when restricted to small enough open balls in the configuration space, away from reducibles, only finitely many of these perturbing sections are non-zero and they vanish along the reducibles.

Let $\mathcal{G}_{E}$ be the Hilbert Lie group of $L_{k+1}^{2}$ unitary gauge transformations of $E$ with determinant one. Let $S_{Z}^{1}$ denote the center of U(2) and set
$${ }^{\circ} \mathcal{G}_{E}:=S_{Z}^{1} \times{ }_{\left\{ \pm \mathrm{id}_{E}\right\}} \mathcal{G}_{E},$$
which we may view as the group of $L_{k+1}^{2}$ unitary gauge transformations of $E$ with constant determinant. The stabilizer of a unitary connection $A$ on $E$ in ${ }^{\circ} \mathcal{G}_{E}$ (which coincides with its stabilizer in the full group Aut $E$ of unitary automorphisms of $E$ ) always contains the center $S_{Z}^{1} \subset \mathrm{U}(2)$, corresponding to the constant, central, unitary automorphisms of $E$. We call $A$ irreducible if its stabilizer is exactly $S_{Z}^{1}$ and reducible otherwise.

It is also possible, as in [71, 74], to fix a smooth representative $\omega \in \Omega^{2}(X, \mathbb{R})$ for $c_{1}(E)$ and instead consider the space of unitary connections $A$ on $E$ satisfying the trace condition $\operatorname{tr} F_{A}=-2 \pi i \omega$, modulo the action of the full group Aut $E$ of unitary autommorphisms of $E$. The resulting moduli space of nonabelian monopoles is then a
torus bundle over the moduli space we define below, with fibers $H^{1}(X ; \mathbb{R}) / H^{1}(X ; \mathbb{Z})$. These tori complicate the analysis of the links of singularities when $b^{1}(X)>0$ and do not contain any additional information, so we choose to eliminate them by instead imposing the stronger fixed-determinant-connection trace condition and working with a compatible group of gauge transformations. A similar framework is used in [68, 92].

We refer to §2.5 for a detailed account of the construction of our holonomy perturbations. The large number of technical points involving regularity and uniform estimates for these perturbations (which still allow us to obtain an Uhlenbeck compactification) are discussed in the Appendix. We fix $r \geq k+1$ and define gauge-equivariant $C^{\infty}$ maps (see §2.5),
$$\begin{aligned}
& \mathcal{A}_{E}(X) \ni A \mapsto \vec{\tau} \cdot \overrightarrow{\mathfrak{m}}(A) \in L_{k+1}^{2}\left(X, \mathfrak{g} \mathfrak{l}\left(\Lambda^{+}\right) \otimes_{\mathbb{R}} \mathfrak{s} \mathfrak{o}(\mathfrak{s} \mathfrak{u}(E))\right), \\
& \mathcal{A}_{E}(X) \ni A \mapsto \vec{\vartheta} \cdot \overrightarrow{\mathfrak{m}}(A) \in L_{k+1}^{2}\left(X, \operatorname{Hom}\left(W^{+}, W^{-}\right) \otimes_{\mathbb{C}} \mathfrak{s} \mathfrak{l}(E)\right),
\end{aligned}$$
where $\vec{\tau}:=\left(\tau_{j, l, \alpha}\right)$ is a suitably convergent sequence in $C^{r}\left(X, \mathfrak{g l}\left(\Lambda^{+}\right)\right)$and $\vec{\vartheta}:=\left(\vartheta_{j, l, \alpha}\right)$ is a suitably convergent sequence in $C^{r}\left(X, \Lambda^{1} \otimes \mathbb{C}\right)$, while $\overrightarrow{\mathfrak{m}}(A):=\left(\mathfrak{m}_{j, l, \alpha}(A)\right)$ is a sequence in $L_{k+1}^{2}(X, \mathfrak{s u}(E))$ of holonomy sections constructed by extending the method of [17, 18], and
$$\begin{aligned}
& \vec{\tau} \cdot \overrightarrow{\mathfrak{m}}(A):=\sum_{j, l, \alpha} \tau_{j, l, \alpha} \otimes_{\mathbb{R}} \operatorname{ad}\left(\mathfrak{m}_{j, l, \alpha}(A)\right), \\
& \vec{\vartheta} \cdot \overrightarrow{\mathfrak{m}}(A):=\sum_{j, l, \alpha} \rho\left(\vartheta_{j, l, \alpha}\right) \otimes_{\mathbb{C}} \mathfrak{m}_{j, l, \alpha}(A) .
\end{aligned}$$
We call a point $(A, \Phi)$ in the pre-configuration space of $L_{k}^{2}$ pairs $\tilde{\mathcal{C}}_{W, E}:=\mathcal{A}_{E} \times$ $L_{k}^{2}\left(W^{+} \otimes E\right)$ a PU(2) monopole if it solves
$$\begin{aligned}
F_{A}^{+}-\left(\mathrm{id}+\tau_{0} \otimes \mathrm{id}_{\mathfrak{s u}(E)}+\vec{\tau} \cdot \overrightarrow{\mathfrak{m}}(A)\right) \rho^{-1}\left(\Phi \otimes \Phi^{*}\right)_{00} & =0, \\
D_{A} \Phi+\rho\left(\vartheta_{0}\right) \Phi+\vec{\vartheta} \cdot \overrightarrow{\mathfrak{m}}(A) \Phi & =0 .
\end{aligned}$$
We let $M_{W, E}$ be the moduli space of solutions cut out of the configuration space of pairs $\mathcal{C}_{W, E}:=\tilde{\mathcal{C}}_{W, E} /{ }^{\circ} \mathcal{G}_{E}$ by the equations (1.3). We let $M_{W, E}^{*, 0} \subset M_{W, E}$ be the subspace of pairs $[A, \Phi]$ such that $A$ is irreducible and the section $\Phi$ is not identically zero. The sections $\vec{\tau} \cdot \overrightarrow{\mathfrak{m}}(A)$ and $\vec{\vartheta} \cdot \overrightarrow{\mathfrak{m}}(A)$ vanish at reducible connections $A$ by construction; plainly, the terms in (1.3) involving the perturbations $\vec{\tau} \cdot \overrightarrow{\mathfrak{m}}(A)$ and $\vec{\vartheta} \cdot \overrightarrow{\mathfrak{m}}(A)$ are zero when $\Phi$ is zero.
1.1.2. Uhlenbeck compactness. The holonomy-perturbation maps in (1.2) are continuous with respect to the Uhlenbeck topology (see §4.5), just as are those of [18]. Suppose $\left\{A_{\beta}\right\}$ is a sequence in $\mathcal{A}_{E}(X)$ which converges in the Uhlenbeck topology to a limit $(A, \mathbf{x})$ in $\mathcal{A}_{E_{-\ell}}(X) \times \operatorname{Sym}^{\ell}(X)$. The sections $\vec{\tau} \cdot \overrightarrow{\mathfrak{m}}\left(A_{\beta}\right)$ and $\vec{\vartheta} \cdot \overrightarrow{\mathfrak{m}}\left(A_{\beta}\right)$ then converge in $L_{k+1}^{2}(X)$ to a section $\vec{\tau} \cdot \overrightarrow{\mathfrak{m}}(A, \mathbf{x})$ of $\mathfrak{g} \mathfrak{l}\left(\Lambda^{+}\right) \otimes_{\mathbb{R}} \mathfrak{s} \mathfrak{o}\left(\mathfrak{s} \mathfrak{u}\left(E_{-\ell}\right)\right)$ and a section
$\vec{\vartheta} \cdot \overrightarrow{\mathfrak{m}}(A, \mathbf{x})$ of $\operatorname{Hom}\left(W^{+}, W^{-}\right) \otimes_{\mathbb{C}} \mathfrak{s} \mathfrak{l}\left(E_{-\ell}\right)$, respectively. For each $\ell \geq 0$, the maps of (1.2) extend continuously to gauge-equivariant maps
$$\begin{aligned}
& \mathcal{A}_{E_{-\ell}}(X) \times \operatorname{Sym}^{\ell}(X) \rightarrow L_{k+1}^{2}\left(X, \mathfrak{g} \mathfrak{l}\left(\Lambda^{+}\right) \otimes_{\mathbb{R}} \mathfrak{s} \mathfrak{o}\left(\mathfrak{s} \mathfrak{u}\left(E_{-\ell}\right)\right)\right), \\
& \mathcal{A}_{E_{-\ell}}(X) \times \operatorname{Sym}^{\ell}(X) \rightarrow L_{k+1}^{2}\left(X, \operatorname{Hom}\left(W^{+}, W^{-}\right) \otimes_{\mathbb{C}} \mathfrak{s l}\left(E_{-\ell}\right)\right),
\end{aligned}$$
given by $(A, \mathbf{x}) \mapsto \vec{\tau} \cdot \overrightarrow{\mathfrak{m}}(A, \mathbf{x})$ and $(A, \mathbf{x}) \mapsto \vec{\vartheta} \cdot \overrightarrow{\mathfrak{m}}(A, \mathbf{x})$, which are $C^{\infty}$ on each $C^{\infty}$ stratum determined by $\operatorname{Sym}^{\ell}(X)$.

Our construction of the Uhlenbeck compactification for $M_{W, E}$ requires us to consider moduli spaces
$$\mathbf{M}_{W, E_{-\ell}} \subset \mathcal{C}_{W, E_{-\ell}} \times \operatorname{Sym}^{\ell}(X)$$
of triples $[A, \Phi, \mathbf{x}]$ given by the zero locus of the ${ }^{\circ} \mathcal{G}_{E_{-\ell}}$-equivariant map
$$\mathfrak{S}: \tilde{\mathcal{C}}_{W, E_{-\ell}} \times \operatorname{Sym}^{\ell}(X) \rightarrow L_{k}^{2}\left(\Lambda^{+} \otimes \mathfrak{s} \mathfrak{u}\left(E_{-\ell}\right)\right) \oplus L_{k}^{2}\left(W^{-} \otimes E_{-\ell}\right)$$
defined as in (1.3) except using the perturbing sections $\vec{\tau} \cdot \overrightarrow{\mathfrak{m}}$ and $\vec{\vartheta} \cdot \overrightarrow{\mathfrak{m}}$ in (1.4) instead of those in (1.2). We call $\mathbf{M}_{W, E_{-\ell}}$ a lower-level moduli space if $\ell>0$ and call $\mathbf{M}_{W, E_{-0}}=M_{W, E}$ the top or highest level.

In the more familiar case of the unperturbed PU(2) monopole equations (1.1), the spaces $\mathbf{M}_{W, E_{-\ell}}$ would simply be products $M_{W, E_{-\ell}} \times \operatorname{Sym}^{\ell}(X)$. In general, though, the spaces $\mathbf{M}_{W, E_{-\ell}}$ are not products when $\ell>0$ due to the slight dependence of the section $\mathfrak{S}(A, \Phi, \mathbf{x})$ on the points $\mathbf{x} \in \operatorname{Sym}^{\ell}(X)$ through the perturbations $\vec{\tau} \cdot \overrightarrow{\mathfrak{m}}$ and $\vec{\vartheta} \cdot \overrightarrow{\mathfrak{m}}$. A similar phenomenon is encountered in [18, §4(iv)-(vi)] for the case of the extended anti-self-dual equations, where holonomy perturbations are also employed in order to achieve transversality.

We define $\bar{M}_{W, E}$ to be the Uhlenbeck closure of $M_{W, E}$ in the space of ideal PU(2) monopoles,
$$\bigcup_{\ell=0}^{N} \mathbf{M}_{W, E_{-\ell}} \subset \bigcup_{\ell=0}^{N}\left(\mathcal{C}_{W, E_{-\ell}} \times \operatorname{Sym}^{\ell}(X)\right),$$
for any integer $N \geq N_{p}$, where $N_{p}$ is a sufficiently large integer to be specified below.
Theorem 1.1. Let $X$ be a closed, oriented, smooth four-manifold with $C^{\infty}$ Riemannian metric, spin ${ }^{c}$ structure ( $\rho, W^{+}, W^{-}$) with spin ${ }^{c}$ connection on $W=W^{+} \oplus W^{-}$, and a Hermitian two-plane bundle $E$ with unitary connection on $\operatorname{det} E$. Then there is a positive integer $N_{p}$, depending at most on the curvatures of the fixed connections on $W$ and $\operatorname{det} E$ together with $c_{2}(E)$, such that for all $N \geq N_{p}$ the topological space $\bar{M}_{W, E}$ is compact, second countable, Hausdorff, and is given by the closure of $M_{W, E}$ in $\cup_{\ell=0}^{N} \mathbf{M}_{W, E_{-\ell}}$.

Remark 1.2. The existence of an Uhlenbeck compactification for the moduli space of solutions to the unperturbed PU(2) monopole equations (1.1) was announced by Pidstrigach [71] and an argument was outlined in [74]. A similar argument for the equations (1.1) was outlined by Okonek and Teleman in [68]. Theorem 1.1 yields the
standard Uhlenbeck compactification for the system (1.1) and for the perturbations of (1.1) described in [23, 93] - see Remark 1.4. An independent proof of Uhlenbeck compactness for (1.1) and certain perturbations of these equations is given in [92, 93].
1.1.3. Transversality. The space $\operatorname{Sym}^{\ell}(X)$ is smoothly stratified, the strata being enumerated by partitions of $\ell$. If $\Sigma \subset \operatorname{Sym}^{\ell}(X)$ is a smooth stratum, we define
$$\left.\mathbf{M}_{W, E_{-\ell}}\right|_{\Sigma}:=\left\{[A, \Phi, \mathbf{x}] \in \mathbf{M}_{W, E_{-\ell}}: \mathbf{x} \in \Sigma\right\},$$
with $\mathbf{M}_{W, E_{-0}}:=M_{W, E}$ when $\ell=0$. We then have the following transversality result for the equations (1.3), at least away from the solutions where the connection is reducible or the spinor vanishes.

Theorem 1.3. Let $X$ be a closed, oriented, smooth four-manifold with $C^{\infty}$ Riemannian metric, spin ${ }^{c}$ structure ( $\rho, W^{+}, W^{-}$) with spin ${ }^{c}$ connection on $W=W^{+} \oplus W^{-}$, and a Hermitian line bundle $\operatorname{det} E$ with unitary connection. Then there is a first-category subset of the space of $C^{\infty}$ perturbation parameters such that the following holds. For each 4-tuple $\left(\tau_{0}, \vartheta_{0}, \vec{\tau}, \vec{\vartheta}\right)$ in the complement of this first-category subset, integer $\ell \geq 0$, and smooth stratum $\Sigma \subset \operatorname{Sym}^{\ell}(X)$, the moduli space $\left.\mathbf{M}_{W, E_{-} \ell}^{*, 0}\right|_{\Sigma}\left(\tau_{0}, \vartheta_{0}, \vec{\tau}, \vec{\vartheta}\right)$ is a smooth manifold of the expected dimension,
$$\begin{aligned}
\left.\operatorname{dim} \mathbf{M}_{W, E_{-\ell}}^{*, 0}\right|_{\Sigma}= & \operatorname{dim} M_{W, E_{-\ell}}^{*, 0}+\operatorname{dim} \Sigma \\
= & -2 p_{1}\left(\mathfrak{s u}\left(E_{-\ell}\right)\right)-\frac{3}{2}(e(X)+\sigma(X))+\operatorname{dim} \Sigma \\
& +\frac{1}{2} p_{1}\left(\mathfrak{s u}\left(E_{-\ell}\right)\right)+\frac{1}{2}\left(\left(c_{1}\left(W^{+}\right)+c_{1}(E)\right)^{2}-\sigma(X)\right)-1,
\end{aligned}$$
where $\operatorname{det}\left(E_{-\ell}\right)=\operatorname{det} E$ and $c_{2}\left(E_{-\ell}\right)=c_{2}(E)-\ell$.

Remark 1.4. Different approaches to the question of transversality for the PU(2) monopole equations (1.1) with generic perturbation parameters have been considered by Pidstrigach and Tyurin in [74] and by Teleman in [92]. More recently, a new approach to transversality for (1.1) has been discovered independently by the first author [23] and by Teleman [93]: the method uses only the perturbations $\left(\tau_{0}, \vartheta_{0}\right)$ together with perturbations of the Riemannian metric $g$ on $X$ and compatible Clifford map $\rho$.

A choice of generic Riemannian metric on $X$ ensures that the moduli space $M_{E}^{\text {asd }, *}$ of irreducible anti-self-dual connections on $\mathfrak{s u}(E)$ is smooth and of the expected dimension [20, 30], although the points of $M_{E}^{\text {asd }, *}$ need not be regular points of $M_{W, E}^{*}$ as the linearization of (1.3) may not be surjective there. A choice of generic parameter $\tau_{0}$ ensures that the moduli spaces $M_{W, E, L_{1}}^{\text {red, } 0}$ of non-zero-section solutions to (1.3) which are reducible with respect to the splitting $E=L_{1} \oplus(\operatorname{det} E) \otimes L_{1}^{*}$ are smooth and of the expected dimension [25]. Again, the points of $M_{W, E, L_{1}}^{\text {red, } 0}$ need not be regular points of $M_{W, E}^{0}$ since the linearization of (1.3) may not be surjective there.

We note that related transversality and compactness issues have been recently considered in approaches to defining Gromov-Witten invariants for general symplectic manifolds [59, 75, 79].
1.2. Outline. We indicate how the remainder of our article is organized. In §2.2 we prove a slice result for the configuration space $\mathcal{C}_{W, E}$ (Proposition 2.8) while in §2.6 we describe the elliptic deformation complex for (1.3) and compute the expected dimension of $M_{W, E}$. We develop the regularity theory for a generalization of the PU(2) monopole equations (1.3) (obtained by allowing additional inhomogeneous terms) in §3: the main technical result there is that an $L_{1}^{2}$ solution to an inhomogeneous version of (1.3) and the Coulomb gauge equation is $C^{\infty}$ (Corollary 3.4). By combining this with the slice result of Proposition 2.8, we then show that any PU(2) monopole $(A, \Phi)$ in $L_{k}^{2}$ is $L_{k+1}^{2}$ gauge-equivalent to a PU(2) monopole in $C^{\infty}$ (Proposition 3.7).

We establish local estimates for $L_{1}^{2}$ solutions to the inhomogeneous version of (1.3) in §3.3 and §3.4. We use the sharp $L_{1}^{2}$ regularity result of Corollary 3.4 in §4 to prove the removability of point singularities for PU(2) monopoles (Theorem 4.10). In the sequels [26, 27], these regularity results and estimates are needed to prove that $L_{1}^{2}$ gluing solutions to (1.3) are $C^{\infty}$ and to analyse the asymptotic behavior of Taubes' gluing maps and their differentials near the lower strata of the Uhlenbeck compactification.

The proof of Theorem 1.1 relies heavily on both the regularity theory of §3 and the fact that solutions $(A, \Phi)$ to (1.3) satisfy a 'universal energy bound', with constant depending only on the data in the hypotheses of Theorem 1.1. The section $\Phi$ also satisfies a universal $C^{0}$ bound: these bounds are the analogues for PU(2) monopoles of the now well-known a priori estimates for Seiberg-Witten monopoles [47, 62, 77, 98] and follow, in much the same way, from the maximum principle and the Bochner-Weitzenböck formula for $D_{A}$ provided $k \geq 3$ (see §4.1). In §4 we prove the removability of point singularities for solutions to (1.3) (Theorem 4.10) using our a priori bounds and regularity results. While the PU(2) monopole equations are not conformally invariant, they are invariant under constant rescalings of the metric (in the sense of §4.2) and, as in the case of anti-self-dual connections, this scale invariance is exploited in the proof of Theorem 1.1, whose proof is completed in §4.6.

Theorem 1.3 is initially established in §5 for $C^{r}$ perturbations for any fixed $3 \leq$ $r<\infty$, in order to avail of the Sard-Smale theorem for Fredholm maps of Banach manifolds [80], while in §5.1.2 we show that generic $C^{\infty}$ perturbation parameters are sufficient for transversality. (See Corollary 5.6 for the special case $\ell=0$ and §5.1.3 for its extension to the general case $\ell \geq 0$.)

As we shall explain in §5, our proof of Theorem 1.3 ultimately hinges on the fact that if $(A, \Phi)$ is a PU(2) monopole and $A$ is reducible on a non-empty open subset containing the support of the holonomy perturbations depending on $A$, then $A$ is reducible over $X$. The proof of this result (Theorem 5.11) occupies §5.3; the result follows from the Agmon-Nirenberg unique continuation theorem after the system (1.3)
has been transformed into an ordinary differential equation for a one-parameter family of pairs over $S^{3}$. The unique continuation property holds for both the perturbed PU(2) monopole equations (1.3), when the initial open subset of $X$ contains the balls in $X$ supporting holonomy perturbations, and the unperturbed equations (1.1) for any initial open subset.
1.3. Other approaches to transversality. As we noted in Remark 1.4, transversality for the PU(2) monopole equations (1.1) has also been proved very recently using only the perturbations $\left(\tau_{0}, \vartheta_{0}\right)$, together with perturbations of the Riemannian metric $g$ on $X$ and compatible Clifford map $\rho$ [23, 93]. The transversality proof given in [23] is considerably more delicate than the method we employ in the present article. When using holonomy perturbations, the main technical difficulties are due to the noncompactness of the moduli space of PU(2) monopoles and the core transversality argument itself is more straightforward, whereas in [23] the situation is entirely reversed. To place these various transversality results in a suitable context, we briefly discuss some other approaches to transversality, both for the PU(2) monopole equations and the closely related 'spin ${ }^{c}$-ASD' equations of [73], which Pidstrigach and Tyurin used to define spin polynomial invariants.

Suppose $(A, \Phi)$ is a solution to either the equations (1.1), the equations (1.1) with perturbations $\left(\tau_{0}, \vartheta_{0}\right)$, or the holonomy-perturbed equations (1.3). If $A$ is reducible, then $\Phi$ has rank less than or equal to one (see Lemma 5.22). However, as observed by Teleman [69, 92], if $\Phi$ is rank one then $A$ is not necessarily reducible and he describes a simple counterexample for the equations (1.1) when $X$ is a Kähler manifold with its canonical spin ${ }^{c}$ structure.

It is not too difficult to prove that $M_{W, E}^{*, 0}$ is a smooth manifold of the expected dimension away from the locus of irreducible, rank-one solutions using the perturbation parameters $\left(\tau_{0}, \vartheta_{0}\right)$ alone. However, as irreducible, rank-one solutions to (1.3) could be present in $M_{W, E}^{*, 0}$, it appears impossible to prove that the entire space $M_{W, E}^{*, 0}$ is a smooth manifold of the expected dimension using only the parameters $\left(\tau_{0}, \vartheta_{0}\right)$. A similar problem arises in the proof of transversality for the spin ${ }^{c}$-ASD equations given in [73, Proposition I.3.5]; a version of these equations can be obtained from the equations (1.1) by omitting the quadratic term $\rho^{-1}\left(\Phi \otimes \Phi^{*}\right)_{00}$. In the proof of [73, Proposition I.3.5] it is claimed that if $D_{A} \Phi=0$ and $\Phi$ is rank one, then $A$ is reducible [p. 277]: Teleman's counterexample shows that this claim is incorrect and he points out an error in their argument [69, 92]. On the other hand, the possible presence or absence of irreducible, rank-one solutions to the PU(2) monopole equations makes no difference to the transversality argument we describe in §5 using holonomy perturbations, as these perturbations are strong enough to yield transversality without a separate analysis of the locus of irreducible, rank-one solutions.
1.4. Applications. In [25] we discuss the singularities of the moduli space $M_{W, E}$. We introduce cohomology classes and geometric representatives on $M_{W, E}^{*}$, construct the links of the top-level singular strata of anti-self-dual and Seiberg-Witten moduli
spaces, compute the Chern characters of their normal bundles in suitably defined ambient manifolds, and define the orientations of these links. We thus obtain a relation between Donaldson and Seiberg-Witten invariants when the reducible solutions appear only in the top level of the Uhlenbeck compactification. In [26, 27], we develop the gluing theory for PU(2) monopoles: this is used to construct links of the lower-level Seiberg-Witten moduli spaces, to show that the pairing of the cohomology classes with this link is well-defined, and to eliminate the requirement of [25] that the reducible solutions appear only in the top level. A survey of some of the results contained in the present article and its sequels [25, 26, 27] is provided in [24].

Acknowledgements. The first author is especially grateful to Peter Kronheimer, Tom Mrowka, and Cliff Taubes for helpful conversations and for their enthusiasm and encouragement. He is particularly grateful to Tom Mrowka for his corrections to the manuscript. He would also like to thank the Harvard Mathematics Department and the National Science Foundation for their generous support. The second author is very grateful to Selman Akbulut, Ron Fintushel, and Tom Parker for helpful conversations and the Mathematics Departments at Harvard and Michigan State Universities for their hospitality and support. We warmly thank the referee for his corrections, careful reading of the manuscript, and thoughtful comments.

\section*{2. The PU(2) monopole equations}

We lay out a framework for gauge theory for pairs in §2.1 and §2.2: In §2.1 we define the Hilbert spaces of pairs and gauge transformations, while in §2.2 we establish the main slice result we require for the configuration space of pairs modulo gauge transformations, paying particular attention to the structure near 'reducibles'. The PU(2) monopole equations and their holonomy perturbations are introduced in §2.5. The role of the perturbations in obtaining transversality results will be explained in §5. To preserve continuity a detailed discussion of the technical points which need to be addressed when using holonomy perturbations in the present context is deferred to the Appendix. The moduli space and the elliptic deformation complex for solutions to the PU(2) monopole equations are described in §2.6.
2.1. Configuration spaces of connections and pairs. In this section we define the spaces of connections, pairs, gauge transformations, and configuration spaces we will use throughout our work.
2.1.1. Connections on Hermitian two-plane bundles. We consider Hermitian twoplane bundles $E$ over $X$ whose determinant line bundles $\operatorname{det} E$ are isomorphic to a fixed Hermitian line bundle over $X$ endowed with a fixed $C^{\infty}$, unitary connection $A_{e}$. The Hermitian line bundle over $X$ and its unitary connection $A_{e}$ are fixed for the remainder of this article.

Let $k \geq 2$ be an integer and let $\mathcal{A}_{E}$ be the space of $L_{k}^{2}$ connections $A$ on the U(2) bundle $E$ all inducing the fixed determinant connection $A_{e}$ on $\operatorname{det} E$. Equivalently,
following [48, §2(i)], we may view $\mathcal{A}_{E}$ as the space of $L_{k}^{2}$ connections $A$ on the $\mathrm{PU}(2)=$ SO(3) bundle $\mathfrak{s u}(E)$. We shall pass back and forth between these viewpoints, via the fixed connection on $\operatorname{det} E$, relying on the context to make the distinction clear. Explictly, if $A$ is a unitary connection on $E$ and $s \in \Omega^{0}(X, E)$, then $\nabla_{A} s \in \Omega^{1}(E)$. For $\zeta \in \Omega^{0}(X, \mathfrak{u}(E))$, then $\nabla_{A} \zeta \in \Omega^{1}(X, \mathfrak{u}(E))$ is determined by
$$\left(\nabla_{A} \zeta\right) s=\nabla_{A}(\zeta s)-\zeta\left(\nabla_{A} s\right),$$
so, if $A^{\tau} \in \Omega^{1}(U, \mathfrak{u}(2))$ denotes the local connection matrix defined by a choice of local frame for $E$ over an open subset $U \subset X$, then
$$\begin{aligned}
\nabla_{A} s & =d s+A^{\tau} s \\
\nabla_{A} \zeta & =d \zeta+\left[A^{\tau}, \zeta\right]=d \zeta+\left(\operatorname{ad} A^{\tau}\right) \zeta
\end{aligned}$$
Similarly, the connection $A$ on $E$ induces connections on $\mathfrak{s u}(E)$ and $\operatorname{det} E$. For example, if $\xi \in \Omega^{0}(X, \mathfrak{s u}(E))$, then $\nabla_{A} \xi \in \Omega^{1}(X, \mathfrak{s u}(E))$ is also given locally by
$$\nabla_{A} \xi=d \xi+\left[A^{\tau}, \xi\right]=d \xi+\left[\left(A^{\tau}\right)_{0}, \xi\right]=d \zeta_{0}+\left(\operatorname{ad} A^{\tau}\right) \zeta_{0},$$
while if $\lambda \in \Omega^{0}(X, \operatorname{det} E)$ then $\nabla_{A} \lambda \in \Omega^{1}(X, \operatorname{det} E)$ is given by
$$\nabla_{A} \lambda=d \lambda+\left(\operatorname{tr} A^{\tau}\right) \lambda .$$
The above local connection matrices are related by
$$A^{\tau}=\left(A^{\tau}\right)_{0}+\frac{1}{2}\left(\operatorname{tr} A^{\tau}\right) \mathrm{id}_{\mathbb{C}^{2}} \in \Omega^{1}(U, \mathfrak{u}(2)),$$
where $\left(A^{\tau}\right)_{0}=A^{\tau}-\frac{1}{2}\left(\operatorname{tr} A^{\tau}\right) \operatorname{id}_{\mathbb{C}^{2}} \subset \Omega^{1}(U, \mathfrak{s u}(2))$ is the traceless component of $A^{\tau}$ while $\operatorname{tr} A^{\tau} \subset \Omega^{1}(U, \mathfrak{u}(1))=\Omega^{1}(U, i \mathbb{R})$ is the induced local connection form for $\operatorname{det} E$ given by the trace component of $A^{\tau}$. Note that $\left(A^{\tau}\right)_{0} \in \Omega^{1}(U, \mathfrak{s u}(2))$ and that $\operatorname{ad}\left(A^{\tau}\right)_{0}=$ $\operatorname{ad} A^{\tau} \in \Omega^{1}(U, \mathfrak{s o}(3))$ is the induced local connection matrix for the SO(3) bundle $\mathfrak{s} \mathfrak{u}(E)$, where we use the standard identification $\mathfrak{s} \mathfrak{o}(3)=\operatorname{ad}(\mathfrak{s} \mathfrak{u}(2))$.

Conversely, given a unitary connection $A_{e}$ for $\operatorname{det} E$ and a Riemannian connection $\hat{A}$ for $\mathfrak{s u}(E)$, we obtain a unitary connection for $E$ given in terms of local connection matrices by
$$A^{\tau}=\operatorname{ad}^{-1}\left(\hat{A}^{\tau}\right)+\frac{1}{2} A_{e}^{\tau} \operatorname{id}_{\mathbb{C}^{2}} \in \Omega^{1}(U, \mathfrak{u}(2)) .$$
The curvatures of these connection matrices are related by
$$F_{A^{\tau}}=\operatorname{ad}^{-1}\left(F_{\hat{A}^{\tau}}\right)+\frac{1}{2} F_{A_{e}^{\tau}} \mathrm{id}_{\mathbb{C}^{2}} \in \Omega^{2}(U, \mathfrak{u}(2)),$$
with $F_{\hat{A}^{\tau}} \in \Omega^{2}(U, \mathfrak{s o}(3))$ and $F_{A_{e}^{\tau}} \in \Omega^{2}(U, \mathfrak{u}(1))$. Thus, $\left(F_{A^{\tau}}\right)_{0}=\operatorname{ad}^{-1}\left(F_{\hat{A}^{\tau}}\right)$ and $\operatorname{tr} F_{A^{\tau}}=F_{A_{e}^{\tau}}=F\left(\operatorname{tr} A^{\tau}\right)$. Therefore, globally we have $\left(F_{A}\right)_{0}=\operatorname{ad}^{-1} F_{\hat{A}} \in \Omega^{2}(X, \mathfrak{s u}(E))$ and $\operatorname{tr} F_{A}=F_{A_{e}} \in \Omega^{2}(X, \mathfrak{u}(1))=\Omega^{2}(X, i \mathbb{R})$, so that
$$F_{A}=\operatorname{ad}^{-1}\left(F_{\hat{A}}\right)+\frac{1}{2} F_{A_{e}} \operatorname{id}_{E} \in \Omega^{2}(X, \mathfrak{u}(E)),$$
as $\mathfrak{u}(E)=\mathfrak{s u}(E) \oplus(i \mathbb{R}) \operatorname{id}_{E}$.
When we are not explicitly discussing connections which are reducible with respect to some splitting of $E$, it is generally more convenient to view our connections as being
defined on $\mathfrak{s u}(E)$ rather than $E$ as we can then avoid explicit mention of the otherwise unimportant choice of fixed connection on $\operatorname{det} E$. Of course, these viewpoints are equivalent via the choice of this fixed determinant connection. The isomorphism $\operatorname{ad}: \mathfrak{s u}(E) \rightarrow \mathfrak{s o}(\mathfrak{s u}(E))$ will remain implicit when no confusion can arise so that, given a connection $A$ on $\mathfrak{s u}(E)$, we write its curvature as $F_{A} \in \Omega^{2}(\mathfrak{s u}(E))$ and associated deformation complexes on $\Omega^{\bullet}(\mathfrak{s u}(E))$ rather than $F_{A} \in \Omega^{2}(\mathfrak{s o}(\mathfrak{s u}(E)))$, with deformation complexes on $\Omega^{\bullet}(\mathfrak{s o}(\mathfrak{s u}(E)))$ (see [30, Chapter 10], for comparison).
2.1.2. Spin ${ }^{c}$ structures. The minimal, axiomatic approach to the definition of spin ${ }^{c}$ structures and the Dirac operator employed by Kronheimer-Mrowka [49] and Mrowka-Ozsváth-Yu [66] is extremely useful for our purposes, so this is the method we shall follow here.

Recall that a real-linear map $\rho_{+}: T^{*} X \rightarrow \operatorname{Hom}\left(W^{+}, W^{-}\right)$defines a Clifford map $\rho: \Lambda^{\bullet}\left(T^{*} X\right) \otimes \mathbb{C} \rightarrow \operatorname{End}(W)$, with $W:=W^{+} \oplus W^{-}$, if and only if [57, 77]
$$\rho_{+}(\alpha)^{\dagger} \rho_{+}(\alpha)=g(\alpha, \alpha) \operatorname{id}_{W^{+}}, \quad \alpha \in C^{\infty}\left(T^{*} X\right),$$
where $g$ denotes the Riemannian metric on $T^{*} X$. The real-linear map $\rho: T^{*} X \rightarrow$ $\operatorname{End}_{\mathbb{C}}\left(W^{+} \oplus W^{-}\right)$is obtained by defining a real-linear map
$$\rho_{-}: T^{*} X \rightarrow \operatorname{Hom}\left(W^{-}, W^{+}\right), \quad \alpha \mapsto \rho_{-}(\alpha):=-\rho_{+}(\alpha)^{\dagger},$$
and setting
$$\rho(\alpha):=\left(\begin{array}{cc}
0 & \rho_{-}(\alpha) \\
\rho_{+}(\alpha) & 0
\end{array}\right) .$$
This extends to a linear map $\rho: \Lambda^{\bullet}\left(T^{*} X\right) \otimes \mathbb{C} \rightarrow \operatorname{End}\left(W^{+} \oplus W^{-}\right)$and satisfies
$$\rho(\alpha)^{\dagger}=-\rho(\alpha) \quad \text { and } \quad \rho(\alpha)^{\dagger} \rho(\alpha)=g(\alpha, \alpha) \operatorname{id}_{W}, \quad \alpha \in C^{\infty}\left(T^{*} X\right) .$$

A unitary connection ∇ on $W$ and $g$-compatible Clifford map $\rho$ induces a unique SO(4) connection $\nabla^{g}$ on $T^{*} X$ by requiring that
$$\left[\nabla_{\eta}, \rho(\alpha)\right]=-\rho\left(\nabla_{\eta}^{g} \alpha\right),$$
for all $\eta \in C^{\infty}(T X)$ and $\alpha \in \Omega^{1}(X, \mathbb{R})$. (As in [66], we use a minus sign on the right-hand side of (2.4) since our basic Clifford map and Dirac operator are defined using Clifford multiplication by one-forms rather than the more traditional tangent vectors of [57] or [77].) The unitary connection ∇ on $W$ uniquely determines a unitary connection on $\operatorname{det} W^{+} \simeq \operatorname{det} W^{-}$in the standard way [43]. Conversely, the preceding data uniquely determines a unitary connection ∇ on $W$. The connection $\nabla$ on $W$ is called a spin ${ }^{c}$ connection if the connection $\nabla^{g}$ on $T^{*} X$ is also torsion free, that is, if $\nabla^{g}$ is the Levi-Civita connection for the metric $g$.

Given a unitary connection $A$ on an auxiliary Hermitian two-plane bundle $E$, we let $\nabla_{A}$ denote the induced unitary connection on $W \otimes E$. The corresponding Dirac
operator $D_{A}$ is defined by
$$D_{A}:=\sum_{\mu=1}^{4} \rho\left(v^{\mu}\right) \nabla_{A, v_{\mu}},$$
where $\left\{v_{\mu}\right\}$ is a local frame for $T X$ and $\left\{v^{\mu}\right\}$ is the dual frame for $T^{*} X$ defined by $v^{\mu}\left(v_{\mu}\right)=\delta_{\mu \nu}$.
2.1.3. Pre-configuration spaces and automorphism groups. We denote $\Lambda^{\bullet}:=\Lambda^{\bullet}\left(T^{*} X\right)$. For any fixed $L_{k}^{2}$ connection $A_{0} \in \mathcal{A}_{E}$ we therefore write
$$\mathcal{A}_{E}=A_{0}+L_{k}^{2}\left(\Lambda^{1} \otimes \mathfrak{s u}(E)\right),$$
for either fixed-determinant, unitary connections on $E$ or determinant-one, orthogonal connections on $\mathfrak{s u}(E)$. Our pre-configuration space of pairs is given by
$$\tilde{\mathcal{C}}_{W, E}:=\mathcal{A}_{E} \times L_{k}^{2}\left(W^{+} \otimes E\right),$$
and for any fixed $L_{k}^{2}$ pair $\left(A_{0}, \Phi_{0}\right) \in \tilde{\mathcal{C}}_{W, E}$, we have
$$\tilde{\mathcal{C}}_{W, E}=\left(A_{0}, \Phi_{0}\right)+L_{k}^{2}\left(\Lambda^{1} \otimes \mathfrak{s u}(E)\right) \oplus L_{k}^{2}\left(W^{+} \otimes E\right),$$
for the cases of either fixed-determinant, unitary connections on $E$ or determinantone, orthogonal connections on $\mathfrak{s} \mathfrak{u}(E)$.

Given any $C^{\infty}$ connection $A_{0} \in \mathcal{A}_{E}$, our Sobolev norms are defined in the usual way: for example, if $a \in \Omega^{1}(\mathfrak{s u}(E))$, we write
$$\|a\|_{L_{\ell, A_{0}}^{p}(X)}:=\left(\sum_{j=0}^{\ell}\left\|\nabla_{A_{0}}^{j} a\right\|_{L^{p}(X)}^{p}\right)^{1 / p},$$
and if $(a, \phi) \in \Omega^{1}(\mathfrak{s u}(E)) \oplus \Omega^{0}\left(W^{+} \otimes E\right)$, we write
$$\|(a, \phi)\|_{L_{\ell, A_{0}}^{p}(X)}:=\left(\|a\|_{L_{\ell, A_{0}}^{p}(X)}^{2}+\|\phi\|_{L_{\ell, A_{0}}^{p}(X)}^{p}\right)^{1 / p},$$
for any $1 \leq p \leq \infty$ and integer $\ell \geq 0$.
For convenience, we let $i \mathbb{R}_{Z}=(i \mathbb{R}) \operatorname{id}_{\mathbb{C}^{2}} \subset \mathfrak{u}(2)$ denote the center of the Lie algebra $\mathfrak{u}(2)$ and let $S_{Z}^{1}=\exp \left(i \mathbb{R}_{Z}\right) \subset \mathrm{U}(2)$ denote the center $Z(\mathrm{U}(2))$ of the Lie group U(2) given by
$$i \mathbb{R}_{Z}=\left\{\left(\begin{array}{cc}
i \theta & 0 \\
0 & i \theta
\end{array}\right): \theta \in \mathbb{R}\right\} \quad \text { and } \quad S_{Z}^{1}=\left\{\left(\begin{array}{cc}
e^{i \theta} & 0 \\
0 & e^{i \theta}
\end{array}\right): \theta \in \mathbb{R}\right\} .$$
Following [48, §2] we consider the induced action for connections on $\mathfrak{s u}(E)$ by the group $\mathcal{G}_{E}$ of determinant-one, unitary $L_{k+1}^{2}$ automorphisms of $E$ rather than the group $\mathcal{G}_{\mathfrak{s} \mathfrak{u}(E)}$ of determinant-one, orthogonal $L_{k+1}^{2}$ automorphisms of $\mathfrak{s} \mathfrak{u}(E)$ even to define quotient spaces of connections on $\mathfrak{s u}(E)$. The reasons for this choice are explained further in [25]; see also §2.3. We have
$$\mathcal{G}_{E}:=\left\{u \in L_{k+1}^{2}(\mathfrak{g} \mathfrak{l}(E)): u^{\dagger} u=\operatorname{id}_{E} \text { and } \operatorname{det} u=1 \text { a.e. }\right\},$$
and
$${ }^{\circ} \mathcal{G}_{E}:=S_{Z}^{1} \times{ }_{\left\{ \pm \mathrm{id}_{E}\right\}} \mathcal{G}_{E} .$$
One can define the action of ${ }^{\circ} \mathcal{G}_{E}$ on $\mathcal{A}_{E}$ either by push-forward or pullback and one obtains equivalent quotient spaces in either case, but the choice does affect the orientation of moduli spaces so we specify the action here: for $u \in{ }^{\circ} \mathcal{G}_{E}$ and $(A, \Phi) \in$ $\tilde{\mathcal{C}}_{W, E}$, the action of ${ }^{\circ} \mathcal{G}_{E}$ is defined by
$$u(A, \Phi):=(u(A), u \Phi)=\left(u_{*} A, u \Phi\right)=\left(\left(u^{-1}\right)^{*} A, u \Phi\right) .$$
The push-forward action, $u(A)=u_{*} A$, agrees with the conventions of [9, 20]. For the associated covariant derivative $\nabla_{A}$ on $E$ and $u \in \operatorname{Aut} E$, we have
$$\nabla_{u(A)}=u \circ \nabla_{A} \circ u^{-1},$$
so that $u(A)=A-\left(\nabla_{A} u\right) u^{-1}$. In terms of a local connection matrix $A^{\tau} \in \Omega^{1}(U, \mathfrak{u}(2))$, this gives $u\left(A^{\tau}\right)=u A^{\tau} u^{-1}-(d u) u^{-1}$, where we use $u$ to denote both the gauge transformation and the element of $\Omega^{0}(U, \mathrm{U}(2))$.

In order to define quotients by the action of ${ }^{\circ} \mathcal{G}_{E}$, we need to choose $k \geq 2$, so gauge transformations are at least continuous. The proof of the following proposition is a standard application of the Sobolev multiplication theorem: see [30, Props. A.2, A.3, A.9].

Proposition 2.1. Let $X$ be a closed Riemannian four-manifold, let $E$ be a Hermitian vector bundle over $X$, and let $k \geq 2$ be an integer. Then the following hold.
\begin{itemize}
\item[1.] The space ${ }^{\circ} \mathcal{G}_{E}$ is a Hilbert Lie group with Lie algebra $T_{\mathrm{id}}{ }^{\circ} \mathcal{G}_{E}=L_{k+1}^{2}(\mathfrak{s u}(E)) \oplus$ $i \mathbb{R}_{Z}$;
\item[2.] The action of ${ }^{\circ} \mathcal{G}_{E}$ on $\tilde{\mathcal{C}}_{W, E}$ is smooth;
\item[3.] For $(A, \Phi) \in \tilde{\mathcal{C}}_{W, E}$, the differential, at the identity $\operatorname{id}_{E} \in{ }^{\circ} \mathcal{G}_{E}$, of the map ${ }^{\circ} \mathcal{G}_{E} \rightarrow$ $\tilde{\mathcal{C}}_{W, E}$ given by $u \mapsto u(A, \Phi)=\left(A-\left(d_{A} u\right) u^{-1}, u \Phi\right)$ is $\zeta \mapsto-d_{A, \Phi}^{0} \zeta:=\left(-d_{A} \zeta, \zeta \Phi\right)$ as a map
$$L_{k+1}^{2}(\mathfrak{s u}(E)) \oplus i \mathbb{R}_{Z} \rightarrow L_{k}^{2}\left(\Lambda^{1} \otimes \mathfrak{s u}(E)\right) \oplus L_{k}^{2}\left(W^{+} \otimes E\right) .$$
\end{itemize}

We denote $\mathcal{B}_{E}=\mathcal{A}_{E} / \mathcal{G}_{E}=\mathcal{A}_{E} /{ }^{\circ} \mathcal{G}_{E}$. The configuration space of pairs is given by $\mathcal{C}_{W, E}:=\tilde{\mathcal{C}}_{W, E} /{ }^{\circ} \mathcal{G}_{E}$, that is,
$$\mathcal{C}_{W, E}:=\left(\mathcal{A}_{E} \times L_{k}^{2}\left(W^{+} \otimes E\right)\right) /{ }^{\circ} \mathcal{G}_{E}=\mathcal{A}_{E} \times{ }_{\circ} \mathcal{G}_{E} L_{k}^{2}\left(W^{+} \otimes E\right),$$
and is endowed with the quotient $L_{k}^{2}$ topology.
If $\pi$ denotes the projection $\tilde{\mathcal{C}}_{W, E} \rightarrow \mathcal{C}_{W, E}$, a base for the quotient $L_{k}^{2}$ topology of $\mathcal{C}_{W, E}$ is given by open subsets $\pi^{-1} \pi\left(B_{(A, \Phi)}(\varepsilon)\right) \supset B_{(A, \Phi)}(\varepsilon)$, where $B_{(A, \Phi)}(\varepsilon)$ is the $L_{k}^{2}$-ball of radius $\varepsilon$ and center $(A, \Phi)$ in $\tilde{\mathcal{C}}_{W, E}$ given by $\left\{\left(A_{1}, \Phi_{1}\right) \in \tilde{\mathcal{C}}_{W, E}: \|\left(A_{1}, \Phi_{1}\right)-\right.$ $\left.(A, \Phi) \|_{L_{k, A}^{2}}<\varepsilon\right\}$.
2.1.4. Stabilizers. The space $\mathcal{C}_{W, E}$ is not a manifold - it has singularities at points $[A, \Phi]$ with non-trivial stabilizer $\operatorname{Stab}_{A, \Phi} \subset{ }^{\circ} \mathcal{G}_{E}$. Recall that the stabilizer subgroup (of the group of bundle automorphisms) for a connection on a $G$ bundle always contains the center $Z(G) \subset G$ [20, §4.2.2]. We let $S_{Z}^{1} \subset{ }^{\circ} \mathcal{G}_{E}$ denote the constant, central automorphisms of $E$.

Definition 2.2. Suppose $(A, \Phi)$ is a point in $\tilde{\mathcal{C}}_{W, E}$. The stabilizer $\operatorname{Stab}_{A, \Phi} \subset{ }^{\circ} \mathcal{G}_{E}$ of $(A, \Phi)$ in ${ }^{\circ} \mathcal{G}_{E}$ is given by $\left\{\gamma \in{ }^{\circ} \mathcal{G}_{E}: \gamma(A, \Phi)=(A, \Phi)\right\}$, while the stabilizers of $A$ and $\Phi$ are denoted by $\operatorname{Stab}_{A}$ and $\operatorname{Stab}_{\Phi}$, respectively.
\begin{itemize}
\item[1.] The point $(A, \Phi)$ is a zero-section pair if $\Phi \equiv 0$;
\item[2.] The point $(A, \Phi)$ is an irreducible pair if the connection $A$ has minimal stabilizer $\operatorname{Stab}_{A}=Z(\mathrm{U}(2))=S_{Z}^{1} \subset{ }^{\circ} \mathcal{G}_{E}$ and is reducible otherwise, that is, if $\operatorname{Stab}_{A} \supsetneq S_{Z}^{1}$.
\end{itemize}
The point $(A, \Phi)$ is a reducible, zero-section pair if $(A, \Phi)$ is both a reducible and zero-section pair.

As usual, the stabilizer subgroup $\operatorname{Stab}_{A} \subset{ }^{\circ} \mathcal{G}_{E}$ may be identified with a closed subgroup of $\mathrm{U}\left(E_{x_{0}}\right) \simeq \mathrm{U}(2)$ for any point $x_{0} \in X$ by parallel translation with respect to the connection $A$ [20, §4.2.2], [61]. The following lemma implies that the stabilizer in Aut $E$ of a unitary connection on $E$ coincides with its stabilizer on ${ }^{\circ} \mathcal{G}_{E}$.

Lemma 2.3. Let $E$ be a Hermitian two-plane bundle over a connected four-manifold $X$, let $A$ be a unitary connection on $E$, and let $u$ be a unitary automorphism of $E$ such that $u \in \operatorname{Stab}_{A} \subset \operatorname{Aut} E$. Then $\operatorname{det} u: X \rightarrow S^{1}$ is a constant map.

Proof. The gauge transformation $u$ may be viewed as an Ad-equivariant map $u$ : $P \rightarrow \mathrm{U}(2)$, where $E=P \times \times_{\mathrm{U}(2)} \mathbb{C}^{2}$, so $\operatorname{det} u$ may be viewed as a map from $P$ to $S^{1}$. Since $\operatorname{det} u$ is constant on the fibers of $P$, it descends to a map on $X$. Over a small enough open set $U \subset X$, we may write $u=\exp \zeta$, where $\zeta \in \Omega^{0}(\operatorname{ad} P)$ and $\operatorname{ad} P:=P \times_{\mathrm{ad}} \mathfrak{g} \simeq \mathfrak{u}(E)$, with $G=\mathrm{U}(2)$ and $\mathfrak{g}=\mathfrak{u}(2)$. Differentiating the action of $u$ on $A$ we see that $\nabla_{A} \zeta=0$, so $\zeta$ is covariantly constant over $U$. Then $\operatorname{det} u=\exp (\operatorname{tr} \zeta)$ and $\nabla(\operatorname{det} u)=\operatorname{tr}\left(\nabla_{A} \zeta\right)=0$, so $\operatorname{det} u$ is constant on $U$ and thus on $X$, since $X$ is connected. \(\square\)

For a pair $(A, \Phi)$ on $\left(E, W^{+} \otimes E\right)$ or $\left(\mathfrak{s u}(E), W^{+} \otimes E\right)$, the Lie algebras of $\operatorname{Stab}_{A}$ and $\operatorname{Stab}_{A, \Phi}$ are given by
$$\begin{aligned}
H_{A}^{0} & :=\operatorname{Ker}\left\{d_{A}: L_{k+1}^{2}(\mathfrak{s u}(E)) \oplus i \mathbb{R}_{Z} \rightarrow L_{k}^{2}\left(\Lambda^{1} \otimes \mathfrak{s u}(E)\right)\right\}, \\
H_{A, \Phi}^{0} & :=\operatorname{Ker}\left\{d_{A, \Phi}^{0}: L_{k+1}^{2}(\mathfrak{s u}(E)) \oplus i \mathbb{R}_{Z} \rightarrow L_{k}^{2}\left(\Lambda^{1} \otimes \mathfrak{s u}(E)\right) \oplus L_{k}^{2}\left(\Lambda^{1} \otimes W^{+} \otimes E\right)\right\} .
\end{aligned}$$
The first identification is standard (see [20, §4.2.2], [30, Chapter 3], or [61]) and the second follows by the same argument.

From [20, §4.2.2] and [30, Theorem 10.8] we have the following characterization of the stabilizer $\operatorname{Stab}_{B} \subset \mathcal{G}_{V}=\operatorname{Aut} V$ of a connection $B$ on an SO(3) bundle $V$. Note that the four-manifold $X$ below need not be simply-connected or closed and that $H_{B}^{0}=\operatorname{Ker}\left\{d_{B}: L_{k+1}^{2}(\mathfrak{s o}(V)) \rightarrow L_{k}^{2}\left(\Lambda^{1} \otimes \mathfrak{s o}(V)\right)\right\}$.

Lemma 2.4. Let $B$ be an orthogonal connection on an SO(3) bundle $V$ over a connected smooth four-manifold $X$. The following are equivalent provided $B$ is not flat:
\begin{itemize}
\item[1.] $\operatorname{Stab}_{B} \simeq \mathrm{SO}(2) \simeq S^{1}$;
\item[2.] $H_{B}^{0} \neq 0$;
\item[3.] $B$ is reducible with respect to an orthogonal splitting $V=N \oplus \underline{\mathbb{R}}$, where $N$ is a complex line bundle over $X$ and $\mathbb{R}=X \times \mathbb{R}$ (that is, $B$ reduces to an $\operatorname{SO}(2)$ connection);
\item[4.] $\operatorname{Stab}_{B} \neq\left\{\operatorname{id}_{V}\right\}$.
\end{itemize}
Finally, $B$ is flat if $\operatorname{Stab}_{B}=\operatorname{SO}(3)$.
Remark 2.5. Note that the 'twisted reducible' (that is, locally reducible) connections on $\mathfrak{s u}(E)$ discussed by Kronheimer and Mrowka in [48, §2(i)] are globally irreducible in the sense that they have minimal stabilizer $\left\{\operatorname{id}_{\mathfrak{s} \mathfrak{u}(E)}\right\}$. The condition that $B$ is not flat is used in the proof that (4) implies (1) [30, p. 48]: The stabilizer $\operatorname{Stab}_{B}$ is isomorphic to the centralizer of the holonomy group $\operatorname{Hol}_{B}$ so, if $\operatorname{Stab}_{B} \supsetneq S^{1}$, then $\operatorname{Hol}_{B} \subsetneq S^{1}$ and hence $\operatorname{Hol}_{B}$ is discrete. Since the Lie algebra of $\operatorname{Hol}_{B}$ vanishes, the Ambrose-Singer holonomy theorem implies that the connection $B$ is flat. In particular, we only need $X$ to be a connected four-manifold for these arguments to hold.

As customary, we call an SO(3) connection $B$ on $V$ irreducible if $\operatorname{Stab}_{B}=\left\{\mathrm{id}_{V}\right\}$. We say that a unitary connection $A$ on $E$ is projectively flat if the induced connection $A^{\text {ad }}$ on $\mathfrak{s u}(E)$ is flat. By modifying the proofs of Theorem 3.1 in [30] and Proposition II.8.10 [56], we obtain the following relation between (i) the stabilizers $\operatorname{Stab}_{A}$ in ${ }^{\circ} \mathcal{G}_{E}$ of U(2) connections $A$ on $E$ or their induced SO(3) connections $A^{\text {ad }}$ on $\mathfrak{s u}(E)$ and (ii) the stabilizers $\operatorname{Stab}_{A^{\text {ad }}}$ in $\mathcal{G}_{\mathfrak{s u}(E)}$ of SO(3) connections $A^{\text {ad }}$ on $\mathfrak{s u}(E)$.

Lemma 2.6. Let $A$ be a U(2) connection on a Hermitian two-plane bundle $E$ over a smooth, connected four-manifold $X$ and let $A^{\text {ad }}$ be the induced SO(3) connection on the bundle $\mathfrak{s u}(E)$. Then the following are equivalent:
\begin{itemize}
\item[1.] $\operatorname{Stab}_{A^{\text {ad }}} \simeq S^{1}$;
\item[2.] $\operatorname{Stab}_{A} \simeq S^{1} \times S_{Z}^{1}$;
\item[3.] $H_{A}^{0} \simeq i \mathbb{R} \oplus i \mathbb{R}_{Z}$;
\item[4.] $H_{A, \Phi}^{0} \supsetneq i \mathbb{R}_{Z}$;
\item[5.] $A$ is reducible with respect to an orthogonal splitting $E=L_{1} \oplus L_{2}$, where $L_{1}$ and $L_{2}$ are complex line bundles over $X$ (that is, $A$ reduces to a $T^{2}=S^{1} \times S^{1}$ connection);
\item[6.] $\operatorname{Stab}_{A} \supsetneq S_{Z}^{1}$.
\end{itemize}
Finally, the connection $A$ on $E$ is projectively flat (or the connection $A^{\text {ad }}$ on $\mathfrak{s u}(E)$ is flat) if $\operatorname{Stab}_{A}=\mathrm{U}(2)$.

Proof. (1) ⟹ (2): Let $\pi: \mathrm{U}(2) \rightarrow \mathrm{SO}(3)=\mathrm{U}(2) / S_{Z}^{1}$ be the projection $u \mapsto$ $\pm(\operatorname{det} u)^{-1 / 2} u$. Then $\pi^{-1}\left(\operatorname{Stab}_{A^{\text {ad }}}\right) \simeq \operatorname{Stab}_{A^{\text {ad }}} \times S_{Z}^{1}$ and so $\operatorname{Stab}_{A^{\text {ad }}} \simeq S^{1}$ implies that $\operatorname{Stab}_{A} \simeq S^{1} \times S_{Z}^{1}$.
(2) ⟹ (3): Immediate from the identification of $H_{A}^{0}$ as the Lie algebra of $\operatorname{Stab}_{A}$.
(3) ⟹ (4): Trivial.
(4) ⟹ (5): We argue as in the proof of Theorem 3.1 in [30]. Note that $\operatorname{Ker}\left\{d_{A}:\right.$ $\left.L_{k+1}^{2}(X, \mathfrak{u}(E)) \rightarrow \Omega^{1}(X, \mathfrak{u}(E))\right\}$ is isomorphic to
$$\begin{gathered}
\operatorname{Ker}\left\{d_{A}: L_{k+1}^{2}(X, \mathfrak{s u}(E))\right\} \oplus \operatorname{Ker}\left\{d: L_{k+1}^{2}\left(X, i \mathbb{R}_{Z}\right)\right\} \\
=\operatorname{Ker}\left\{d_{A^{\text {ad }}}: L_{k+1}^{2}(X, \mathfrak{s u}(E))\right\} \oplus i \mathbb{R}_{Z} .
\end{gathered}$$
Given (4), we may choose $0 \not \equiv \zeta \in \operatorname{Ker}\left\{d_{A}: L_{k+1}^{2} \Omega^{0}(X, \mathfrak{s u}(E))\right\}$. The pointwise traceless, skew-Hermitian endomorphism $\zeta$ of $E$ has eigenvalues $i \lambda_{1}, i \lambda_{2}= \pm i \lambda$ for some $0 \not \equiv \lambda \in L_{k+1}^{2}(X, \mathbb{R})$. On the open subset of $X$ where $\lambda \neq 0$, let $\xi_{j}, j=1,2$, be $L_{k+1}^{2}$ eigenvectors of $\zeta$ such that $\zeta\left(\xi_{j}\right)=i \lambda_{j} \xi_{j}$ and $\left\langle\xi_{j}, \xi_{k}\right\rangle=\delta_{j k}$. Just as in [30, p. 47], we find that $\lambda$ is constant, the eigenvectors $\xi_{j}$ are globally defined and $d_{A} \xi_{j}=0$ for $j=1,2$. In particular, we have an orthogonal splitting $E=L_{1} \oplus L_{2}$, where $\xi_{j} \in L_{k+1}^{2}(X, E)$ is a section of $L_{j}$ and $d_{A}=d_{A_{1}} \oplus d_{A_{2}}$ with respect to this splitting, so this gives (5).
$(5) \Longrightarrow$ (6): Given (5), the connection $A$ reduces to $A_{1} \oplus A_{2}$ with respect to the splitting $E=L_{1} \oplus L_{2}$ and so has stabilizer $S_{L_{1}}^{1} \times S_{L_{2}}^{1}$, where we identify the constant maps in $\operatorname{Map}^{k+1}\left(X, S^{1}\right)$ with $S_{L_{i}}^{1}$ for $i=1,2$. Since $S_{L_{1}}^{1} \times S_{L_{2}}^{1} \simeq S^{1} \times S_{Z}^{1}$, this gives (2).
(6) ⟹ (1): Given $u \in \operatorname{Stab}_{A}$ and $u \notin S_{Z}^{1}$, we obtain $u_{1}= \pm(\operatorname{det} u)^{-1 / 2} u \in$ $\operatorname{Stab}_{A^{\text {ad }}}$. (By Lemma 2.3, the determinant $\operatorname{det} u$ is a constant map.) If $u_{1}=\operatorname{id}_{\mathfrak{s u}(E)}$ then we would have $u_{1}= \pm \operatorname{id}_{E}$ and $u= \pm(\operatorname{det} u)^{1 / 2} u_{1} \in S_{Z}^{1}$, so $u_{1} \neq \operatorname{id}_{\mathfrak{s u}(E)}$. Therefore, $\operatorname{Stab}_{A^{\text {ad }}} \supsetneq\left\{\operatorname{id}_{\mathfrak{s u}(E)}\right\}$ and Lemma 2.4 implies that $\operatorname{Stab}_{A^{\text {ad }}} \simeq S^{1}$.

Lastly, $A$ is projectively flat if $\operatorname{Stab}_{A^{\mathrm{ad}}}=\operatorname{SO}(3)$ (by Lemma 2.4) and $\operatorname{Stab}_{A^{\mathrm{ad}}}=$ $\mathrm{SO}(3) \simeq \mathrm{U}(2) / S_{Z}^{1}$ if and only if $\operatorname{Stab}_{A}=\mathrm{U}(2)$. \(\square\)

The equivalence of (1) and (2) above can alternatively be seen by noting that $H_{A^{\text {ad }}}^{0} \simeq i \mathbb{R}$ if and only if $H_{A}^{0} \simeq i \mathbb{R} \oplus i \mathbb{R}_{Z}$, so $\operatorname{Stab}_{A^{\text {ad }}} \simeq S^{1}$ if and only if $\operatorname{Stab}_{A} \simeq$ $S^{1} \times S_{Z}^{1}$.

From Lemmas 2.4 and 2.6 we see that $A$ is an irreducible U(2) connection if and only if $A^{\text {ad }}$ is an irreducible SO(3) connection. Note that $\operatorname{Stab}_{A, \Phi}=\operatorname{Stab}_{A} \cap \operatorname{Stab}_{\Phi}$. The stabilizer $\operatorname{Stab}_{A, \Phi}$ of a zero-section pair $(A, \Phi)$ contains $S_{Z}^{1}$. The stabilizer $\operatorname{Stab}_{A, \Phi}$ of a reducible pair $(A, \Phi)$ need not contain the stabilizer $\operatorname{Stab}_{A}$ since $\operatorname{Stab}_{A}$ may not fix $\Phi$.

We write $\tilde{\mathcal{C}}_{W, E}^{*}$ (respectively, $\tilde{\mathcal{C}}_{W, E}^{0}$ ) for the complement of the reducible pairs (respectively, zero section pairs) in $\tilde{\mathcal{C}}_{W, E}$ and let $\tilde{\mathcal{C}}_{W, E}^{*, 0}=\tilde{\mathcal{C}}_{W, E}^{*} \cap \tilde{\mathcal{C}}_{W, E}^{0}$. The quotients $\mathcal{C}_{W, E}^{*}, \mathcal{C}_{W, E}^{0}$, and $\mathcal{C}_{W, E}^{*, 0}$ are similarly defined.

If $(A, \Phi) \in \tilde{\mathcal{C}}_{W, E}^{*, 0}$, then $\operatorname{Stab}_{A, \Phi}=\left\{\operatorname{id}_{E}\right\}$, as the stabilizer of an irreducible connection $A$ will be $S_{Z}^{1}$ and if $S_{Z}^{1}$ stabilizes the section $\Phi$ then $e^{i \theta} \Phi=0$ for all $\theta \in \mathbb{R}$ and so $\Phi \equiv 0 \in L_{k}^{2}\left(X, W^{+} \otimes E\right)$ (note that $\Phi$ need not be continuous). Therefore, ${ }^{\circ} \mathcal{G}_{E}$ acts freely on $\mathcal{C}_{W, E}^{*, 0}$ and, as we shall see in the next section, the quotient $\mathcal{C}_{W, E}^{*, 0}$ is a Banach
manifold. Conversely, if $(A, \Phi)$ is a PU(2) monopole, $A$ is reducible, and $\Phi \not \equiv 0$, then Lemma 5.22 implies that $\operatorname{Stab}_{A, \Phi} \simeq S^{1}$.
2.2. A slice for the action of the group of gauge transformations. Let $k \geq 2$ be an integer. The slice $\mathbf{S}_{A, \Phi} \subset \tilde{\mathcal{C}}_{W, E}$ through a pair $(A, \Phi)$ is given by $\mathbf{S}_{A, \Phi}:=$ $(A, \Phi)+\mathbf{K}_{A, \Phi}$, where
$$\mathbf{K}_{A, \Phi}:=\operatorname{Ker} d_{A, \Phi}^{0, *} \subset L_{k}^{2}\left(\Lambda^{1} \otimes \mathfrak{s u}(E)\right) \oplus L_{k}^{2}\left(W^{+} \otimes E\right)$$
If $\pi$ is the projection from $\tilde{\mathcal{C}}_{W, E}$ onto $\mathcal{C}_{W, E}=\tilde{\mathcal{C}}_{W, E} /{ }^{\circ} \mathcal{G}_{E}$, denoted by $(A, \Phi) \mapsto[A, \Phi]$, we let
$$\mathbf{B}_{A, \Phi}(\varepsilon)=\pi^{-1} B_{A, \Phi}(\varepsilon) \cap \mathbf{S}_{A, \Phi},$$
be the open $L_{k}^{2}$ ball in $\mathbf{S}_{A, \Phi}$ with center $(A, \Phi)$ and radius $\varepsilon$, so that
$$\begin{aligned}
\mathbf{B}_{A, \Phi}(\varepsilon) & :=\left\{\left(A_{1}, \Phi_{1}\right) \in \mathbf{S}_{A, \Phi}:\left\|\left(A_{1}, \Phi_{1}\right)-(A, \Phi)\right\|_{L_{k, A}^{2}}<\varepsilon\right\} \\
& =(A, \Phi)+\left\{(a, \phi) \in \mathbf{K}_{A, \Phi}:\|(a, \phi)\|_{L_{k, A}^{2}}<\varepsilon\right\} .
\end{aligned}$$
The Hilbert Lie group ${ }^{\circ} \mathcal{G}_{E}$ has Lie algebra $L_{k+1}^{2}(\mathfrak{s u}(E)) \oplus i \mathbb{R}_{Z} \subset L_{k+1}^{2}(\mathfrak{s u}(E))$ and exponential map $\exp : L_{k+1}^{2}(\mathfrak{s u}(E)) \oplus i \mathbb{R}_{Z} \rightarrow{ }^{\circ} \mathcal{G}_{E}$ given by $\zeta \mapsto u=\exp \zeta$. Let $\operatorname{Stab}_{A, \Phi}^{\perp}=\exp \left(\left(\operatorname{Ker} d_{A, \Phi}^{0}\right)^{\perp}\right) \subset{ }^{\circ} \mathcal{G}_{E}$, where
$$\left(\operatorname{Ker}\left(\left.d_{A, \Phi}^{0}\right|_{L_{k+1}^{2}}\right)\right)^{\perp}=\operatorname{Im}\left(\left.d_{A, \Phi}^{0, *}\right|_{L_{k+2}^{2}}\right) \subset L_{k+1}^{2}(\mathfrak{s u}(E)),$$
noting that
$$d_{A, \Phi}^{0, *}: L_{k+2}^{2} \Omega^{1}(\mathfrak{s u}(E)) \rightarrow L_{k+1}^{2}(\mathfrak{s u}(E)) \oplus L_{k}^{2}\left(W^{+} \otimes E\right)$$
has closed range. Recall that $\operatorname{Stab}_{A, \Phi} \subset{ }^{\circ} \mathcal{G}_{E}$ is given by $\left\{\gamma \in{ }^{\circ} \mathcal{G}_{E}: \gamma(A, \Phi)=(A, \Phi)\right\}$ and has Lie algebra $H_{A, \Phi}^{0}=\operatorname{Ker}\left(\left.d_{A, \Phi}^{0}\right|_{L_{k+1}^{2}}\right) \subset L_{k+1}^{2}(\mathfrak{s u}(E)) \oplus i \mathbb{R}_{Z}$, so that
$$L_{k+1}^{2}(\mathfrak{s u}(E)) \oplus i \mathbb{R}_{Z}=\left(\operatorname{Ker}\left(\left.d_{A, \Phi}^{0}\right|_{L_{k+1}^{2}}\right)\right)^{\perp} \oplus H_{A, \Phi}^{0} .$$
The subspace $\operatorname{Stab}_{A, \Phi}^{\perp} \subset{ }^{\circ} \mathcal{G}_{E}$ is closed and is a Banach submanifold of ${ }^{\circ} \mathcal{G}_{E}$ with codimension $\operatorname{dim} H_{A, \Phi}^{0}$.

The map $d_{A, \Phi}^{0}: L_{k+1}^{2}(\mathfrak{s u}(E)) \oplus i \mathbb{R}_{Z} \rightarrow L_{k}^{2}\left(\Lambda^{1} \otimes \mathfrak{s u}(E)\right) \oplus L_{k}^{2}\left(W^{+} \otimes E\right)$ has closed range and so we have an $L^{2}$-orthogonal decomposition
$$T_{A, \Phi} \tilde{\mathcal{C}}_{W, E}=\operatorname{Im}\left(\left.d_{A, \Phi}^{0}\right|_{L_{k+1}^{2}}\right) \oplus \mathbf{K}_{A, \Phi}$$
of the tangent space to the space of $L_{k}^{2}$ pairs at the point $(A, \Phi)$.
The proof that the quotient space $\mathcal{C}_{W, E}$ is Hausdorff and our later proof of removable singularities for PU(2) monopoles make use of the following well-known technical result [20, Proposition 2.3.15], [30, Proposition A.5], [56, Theorem II.7.11]. Note that the space of $L_{2}^{2}$ unitary automorphisms of $E$ is neither a Hilbert Lie group nor does it act smoothly on the space of $L_{2}^{2}$ unitary connections on $E$.

Lemma 2.7. Let $E$ be a Hermitian bundle over a Riemannian manifold $X$ and let $k \geq 2$ be an integer. Suppose $\left\{A_{\alpha}\right\}$ and $\left\{B_{\alpha}\right\}$ are sequences of $L_{k}^{2}$ unitary connections on $E$ and that $\left\{u_{\alpha}\right\}$ is a sequence of unitary automorphisms of $E$ such that $u_{\alpha}\left(A_{\alpha}\right)=$ $B_{\alpha}$. Then the following hold.
\begin{itemize}
\item[1.] The sequence $\left\{u_{\alpha}\right\}$ is in $L_{k+1}^{2}$;
\item[2.] If $\left\{A_{\alpha}\right\}$ and $\left\{B_{\alpha}\right\}$ converge in $L_{k}^{2}$ to limits $A_{\infty}, B_{\infty}$, then there is a subsequence $\left\{\alpha^{\prime}\right\} \subset\{\alpha\}$ such that $\left\{u_{\alpha^{\prime}}\right\}$ converges in $L_{k+1}^{2}$ to $u_{\infty}$ and $B_{\infty}=u_{\infty}\left(A_{\infty}\right)$.
\end{itemize}

The following slice result was established by Parker [70], but only for pairs which are neither zero-section nor reducible; see also [9]. It is, of course, the analogue of the usual result for the topology and manifold structure of the configuration space $\mathcal{B}_{E}=\mathcal{A}_{E} / \mathcal{G}_{E}$ of connections. The proof we give here is modelled on the corresponding arguments for connections given in [20, Proposition 2.3.4], [30, Theorem 3.2 \& 4.4], and [56, Theorem II.10.4]. We will ultimately need a rather more involved version of this method in order to show that our gluing maps are diffeomorphisms, so we give the argument in the simpler model case below in some detail and establish some of the notation and conventions we later require.

Proposition 2.8. Let $X$ be a closed, oriented, Riemannian spin ${ }^{c}$ four-manifold, let $E$ be a Hermitian two-plane bundle over $X$, and let $k \geq 2$ be an integer. Then the following hold.
\begin{itemize}
\item[1.] The space $\mathcal{C}_{W, E}$ is Hausdorff;
\item[2.] The subspace $\mathcal{C}_{W, E}^{*, 0} \subset \mathcal{C}_{W, E}$ is open and is a $C^{\infty}$ Hilbert manifold with local parametrizations given by $\pi: \mathbf{B}_{A_{0}, \Phi_{0}}(\varepsilon) \rightarrow \mathcal{C}_{W, E}^{*, 0}$ for sufficiently small $\varepsilon=$ $\varepsilon\left(A_{0}, \Phi_{0}, k\right)$;
\item[3.] The projection $\pi: \tilde{\mathcal{C}}_{W, E}^{*, 0} \rightarrow \mathcal{C}_{W, E}^{*, 0}$ is a $C^{\infty}$ principal ${ }^{\circ} \mathcal{G}_{E}$ bundle;
\item[4.] For $\left(A_{0}, \Phi_{0}\right) \in \tilde{\mathcal{C}}_{W, E}$, the projection $\pi: \mathbf{B}_{A_{0}, \Phi_{0}}(\varepsilon) / \operatorname{Stab}_{A_{0}, \Phi_{0}} \rightarrow \mathcal{C}_{W, E}$ is a home-omorphism onto an open neighborhood of $\left[A_{0}, \Phi_{0}\right] \in \mathcal{C}_{W, E}$ and a diffeomorphism on the complement of the set of points in $\mathbf{B}_{A_{0}, \Phi_{0}}(\varepsilon)$ with non-trivial stabilizer.
\end{itemize}
Proof. The stabilizer $\operatorname{Stab}_{A_{0}, \Phi_{0}}$ (which we can identify with a Lie subgroup U(2)) acts freely on ${ }^{\circ} \mathcal{G}_{E}$ and thus on the Hilbert manifold ${ }^{\circ} \mathcal{G}_{E} \times \mathbf{S}_{A_{0}, \Phi_{0}}$ by $(u, A, \Phi) \mapsto$ $\gamma \cdot(u, A, \Phi)=\left(u \gamma^{-1}, \gamma(A, \Phi)\right)$ and so the quotient ${ }^{\circ} \mathcal{G}_{E} \times_{\operatorname{Stab}_{A_{0}, \Phi_{0}}} \mathbf{S}_{A_{0}, \Phi_{0}}$ is again a Hilbert manifold. We define a smooth map
$$\boldsymbol{\Psi}:{ }^{\circ} \mathcal{G}_{E} \times \operatorname{Stab}_{A_{0}, \Phi_{0}} \mathbf{S}_{A_{0}, \Phi_{0}} \rightarrow \tilde{\mathcal{C}}_{W, E}, \quad[u, A, \Phi] \mapsto u(A, \Phi) .$$
Our first task is to show that the map $\boldsymbol{\Psi}$ is a diffeomorphism onto its image upon restriction to a sufficiently small neighborhood ${ }^{\circ} \mathcal{G}_{E} \times_{\operatorname{Stab}_{A_{0}, \Phi_{0}}} \mathbf{B}_{A_{0}, \Phi_{0}}(\varepsilon)$. Given $\delta>0$, let $B_{\mathrm{id}}(\delta)$ be the ball $\left\{u \in{ }^{\circ} \mathcal{G}_{E}:\left\|u-\operatorname{id}_{E}\right\|_{L_{k+1, A_{0}}^{2}}<\delta\right\}$ and let $B_{\mathrm{id}}^{\perp}(\delta)=B_{\mathrm{id}}(\delta) \cap$ Stab $_{A_{0}, \Phi_{0}}^{\perp}$.
Claim 2.9. For small enough $\delta=\delta\left(A_{0}, \Phi_{0}, k\right)$, the ball $B_{\mathrm{id}}(\delta)$ is diffeomorphic to an open neighborhood in $B_{\mathrm{id}}^{\perp}(\delta) \times \operatorname{Stab}_{A_{0}, \Phi_{0}}$, with inverse map given by $\left(u_{0}, \gamma\right) \mapsto u=u_{0} \gamma$.

Proof. The differential of the multiplication map
$$\operatorname{Stab}_{A_{0}, \Phi_{0}}^{\perp} \times \operatorname{Stab}_{A_{0}, \Phi_{0}} \rightarrow{ }^{\circ} \mathcal{G}_{E}, \quad\left(u_{0}, \gamma\right) \mapsto u_{0} \gamma,$$
at $\left(\mathrm{id}_{E}, \mathrm{id}_{E}\right)$ is given by
$$\operatorname{Ker}\left(\left.d_{A_{0}, \Phi_{0}}^{0}\right|_{L_{k+1}^{2}} ^{2}\right)^{\perp} \oplus H_{A_{0}, \Phi_{0}}^{0} \rightarrow L_{k+1}^{2}(\mathfrak{s u}(E)) \quad(\zeta, \chi) \mapsto \zeta+\chi,$$
and is just the identity map with respect to the $L^{2}$-orthogonal decomposition (2.8) of the range. Hence, the Hilbert space implicit function theorem implies that there is a diffeomorphism from an open neighborhood of $\left(\mathrm{id}_{E}, \mathrm{id}_{E}\right)$ onto an open neighborhood of $\mathrm{id}_{E} \in{ }^{\circ} \mathcal{G}_{E}$. For small enough $\delta$, we may suppose that if $u \in B_{\mathrm{id}}(\delta)$, then $u$ can be written uniquely as $u=u_{0} \gamma$ with $u_{0} \in B_{\mathrm{id}}^{\perp}(\delta)$ and $\gamma \in \operatorname{Stab}_{A_{0}, \Phi_{0}}$. \(\square\)

Claim 2.10. For small enough $\varepsilon=\varepsilon\left(A_{0}, \Phi_{0}, k\right)$, the map $\boldsymbol{\Psi}$ is a diffeomorphism from ${ }^{\circ} \mathcal{G}_{E} \times_{\operatorname{Stab}_{A_{0}, \Phi_{0}}} \mathbf{B}_{A_{0}, \Phi_{0}}(\varepsilon)$ onto its image in $\tilde{\mathcal{C}}_{W, E}$.