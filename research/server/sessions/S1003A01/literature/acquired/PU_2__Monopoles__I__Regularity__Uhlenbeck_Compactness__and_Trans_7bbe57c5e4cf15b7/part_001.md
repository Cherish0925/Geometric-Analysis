---
retention_scope: session
part: 1
total_parts: 6
---

[Part 1/6 of: PU(2) Monopoles. I: Regularity, Uhlenbeck Compactness, and Transversality]

# PU(2) Monopoles. I: Regularity, Uhlenbeck Compactness, and Transversality

> Source: https://projecteuclid.org/journals/journal-of-differential-geometry/volume-49/issue-2/rm-PU2-monopoles-I-Regularity-Uhlenbeck-compactness-and-transversality/10.4310/jdg/1214461020.pdf
> Fetched: 2026-10-13 23:15
> Method: FULLTEXT_HTML_FIRECRAWL|FETCHERS=JINA,FIRECRAWL,BRIGHTDATA

---

## Verified object metadata

```json
{
  "object_type": "web",
  "identifier": "",
  "identifiers": {},
  "identifier_aliases": {},
  "version": "",
  "published_at": "",
  "updated_at": "",
  "license": "",
  "language": "",
  "source": "tavily",
  "source_url": "https://projecteuclid.org/journals/journal-of-differential-geometry/volume-49/issue-2/rm-PU2-monopoles-I-Regularity-Uhlenbeck-compactness-and-transversality/10.4310/jdg/1214461020.pdf",
  "metadata": {
    "provenance_urls": [
      "https://projecteuclid.org/journals/journal-of-differential-geometry/volume-49/issue-2/rm-PU2-monopoles-I-Regularity-Uhlenbeck-compactness-and-transversality/10.4310/jdg/1214461020.pdf"
    ],
    "search_origins": [
      {
        "source": "tavily",
        "query": "Seiberg-Witten monopoles on orbifolds ALE quotient singularities Uhlenbeck compactness"
      }
    ]
  },
  "declared_files": []
}
```

## Source description

the anti-self-dual equation — which uses a local elliptic regularity result for L2 solutions to the Coulomb gauge and inhomogeneous anti-self-dual equation (namely, Proposition 4.4.13 in ) and which in turn has its antecedent in the proof of Theorem 4.5 in . This, of course, is not the only possible approach: Uhlenbeck's original argument  employed a differential inequality to obtain a pointwise decay estimate for solutions near the singular point, and this was the method generalized by Parker to the case of certain coupled Yang-Mills equations; see [77, §9.2] for a proof of removable singularities for Seiberg-Witten monopoles which also uses differential inequalities. It will be convenient to define the following annuli in X, given a point xo G X and a positive constant r: Q(xo;r) := {x [...] the curvature F A , if (A, < £ > ) is a PU(2) monopole on (su(E), W+ ®E); these generalize the well-known a priori bounds for Seiberg-Witten monopoles , , . In our proof of removable singularities we need to take into account the variation of spin c structures with the Riemannian metric and the rescaling behavior of the PU(2) equations; this variation is discussed in §4.2. In §4.3 we prove the removability of point singularities for PU(2) monopoles. T. Parker established the removability of point singularities for solutions to the second-order coupled Yang-Mills equations, namely, dA F A = q(&) and D A& = 0, for a unitary connection A on E and a section $ of W ® E, where q is a certain 

## Retrieved source content

# PU(2) MONOPOLES. I: REGULARITY, UHLENBECK COMPACTNESS, AND TRANSVERSALITY

PAUL M. N. FEEHAN & THOMAS G. LENESS

## 1. Introduction

At seminars at Harvard and MIT, during October 1994, Edward Witten introduced the U(1) monopole equations and the Seiberg-Witten invariants to smooth four-manifold topology and conjectured their relationship with Donaldson invariants on the basis of new developments in quantum field theory [19], [98]. The conjecture, recently extended in [60], has been verified for all four-manifolds whose Donaldson and Seiberg-Witten invariants have been independently computed. Within two months of Witten’s announcement, a program was outlined by V. Pidstrigach and A. Tyurin and others, which should lead to a mathematical proof of the relationship between these two invariants [68], [71], [74]. This approach is unrelated to the quantum field-theoretic arguments of [60], [98] and uses a moduli space of PU(2) monopoles to construct a cobordism between links of Seiberg-Witten moduli spaces of U(1) monopoles and the Donaldson moduli space of anti-self-dual connections, which appear as singularities in this larger stratified moduli space.

It was soon recognized, however, that despite the appeal and elegance of the PU(2) monopole program, its implementation involves substantial technical difficulties due to the contributions of moduli spaces of U(1) monopoles in the lower levels of the Uhlenbeck compactification of the moduli space of PU(2) monopoles. Many of these difficulties had

Received September 11, 1996, and, in revised form, May 5, 1997. The first author was supported in part by an NSF Mathematical Sciences Postdoctoral Fellowship under grant DMS 9306061.

---

never been resolved even in the case of Donaldson theory where similar problems arise, albeit in a rather simpler form, in attempts to prove the Kotschick-Morgan conjecture for Donaldson invariants of four-manifolds $X$ with $b^+(X) = 1$. That conjecture asserts that the Donaldson invariants computed using metrics lying in different chambers of the positive cone of $H^2(X; \mathbb{R})/\mathbb{R}^*$ differ only by homotopy-invariant terms [45]. In the case of the Kotschick-Morgan conjecture, the heart of the problem lies in describing the links of the lower-level reducibles via gluing and then in calculating the pairings of the Donaldson cohomology classes with those links. Thus far, such links have been described and their pairings with cohomology classes computed only in certain special cases [14], [15], [16], [20], [21], [32], [58], [99]. The methods used to obtain these special cases fall very far short of the kind of general analysis needed to prove the Kotschick-Morgan conjecture. On the other hand, by assuming the Kotschick-Morgan conjecture, L. Göttsche computed the coefficients of the wall-crossing formula in [45] in terms of modular forms by exploiting the presumed homotopy invariance of the coefficients [35]. A related approach to the Witten conjecture was proposed by Pidstrigach and Tyurin [72]. Certain aspects of the PU(2) monopole program have been considered from a quantum-field theoretic viewpoint in [13], [38], [39], [50], [51], [52], [53].

In the present article and its sequels [25], [26], [27] we address the analytical problems associated with constructing the links of lower-level Seiberg-Witten moduli spaces and in establishing the analogues of the Kotschick-Morgan conjecture for PU(2) monopoles needed to compute the pairings of cohomology classes with these links. We hope to return to the actual computations and a verification of Witten’s conjecture [60], [98] in a subsequent paper. In this article we describe the basic regularity, Uhlenbeck compactness, and transversality results we need for the moduli space of PU(2) monopoles, and in the sequels [26], [27] we develop the gluing theory required to construct the links of the lower-level Seiberg-Witten moduli spaces. An announcement of the main results of this article appeared in [24].

## 1.1. Statement of results

1.1.1. PU(2) monopoles and holonomy perturbations. We consider Hermitian two-plane bundles $E$ over $X$ whose determinant line bundles det $E$ are isomorphic to a fixed Hermitian line bundle over $X$ endowed with a fixed $C^\infty$, unitary connection. Let $(\rho, W^+, W^-)$ be a spin$^c$ structure on $X$, where $\rho : T^* X \rightarrow \text{End} W$ is the Clifford map, and the Hermitian four-plane bundle $W = W^{+} \oplus W^{-}$ is endowed with a $C^{\infty}$ spin$^c$ connection.

Let $k \geq 3$ be an integer and let $\mathcal{A}_E$ be the space of $L_k^2$ connections $A$ on the U(2) bundle $E$ all inducing the fixed determinant connection on det $E$. Equivalently, following [48, §2(i)], we may view $\mathcal{A}_E$ as the space of $L_k^2$ connections $A$ on the PU(2) = SO(3) bundle $\mathfrak{su}(E)$. We pass back and forth between these viewpoints, via the fixed connection on det $E$, and rely on the context to make the distinction clear. Given a connection $A$ on $\mathfrak{su}(E)$ with curvature $F_A \in L_{k-1}^2(\Lambda^2 \otimes \mathfrak{so}(\mathfrak{su}(E)))$, then ad$^{-1}(F_A^+) \in L_{k-1}^2(\Lambda^+ \otimes \mathfrak{su}(E))$ is its self-dual component, viewed as a section of $\Lambda^+ \otimes \mathfrak{su}(E)$ via the isomorphism ad : $\mathfrak{su}(E) \rightarrow \mathfrak{so}(\mathfrak{su}(E))$. When no confusion can arise, the isomorphism ad : $\mathfrak{su}(E) \rightarrow \mathfrak{so}(\mathfrak{su}(E))$ will be implicit, and so we regard $F_A$ as a section of $\Lambda^+ \otimes \mathfrak{su}(E)$ when $A$ is a connection on $\mathfrak{su}(E)$. Let $D_A : L_k^2(W^{+} \otimes E) \rightarrow L_{k-1}^2(W^{-} \otimes E)$ be the corresponding Dirac operator.

For an $L_k^2$ section $\Phi$ of $W^{+} \otimes E$, let $\Phi^* = \langle \cdot, \Phi \rangle$ be its pointwise Hermitian dual and let $(\Phi \otimes \Phi^*)_{00}$ be the component of the Hermitian endomorphism $\Phi \otimes \Phi^*$ of $W^{+} \otimes E$ which lies in $\mathfrak{su}(W^{+}) \otimes \mathfrak{su}(E)$. The Clifford multiplication $\rho$ defines an isomorphism $\rho : \Lambda^+ \rightarrow \mathfrak{su}(W^{+})$ and thus an isomorphism $\rho = \rho \otimes \mathrm{id}_{\mathfrak{su}(E)}$ of $\Lambda^+ \otimes \mathfrak{su}(E)$ with $\mathfrak{su}(W^{+}) \otimes \mathfrak{su}(E)$. Then

$$
\begin{aligned}
F_A^+ - \rho^{-1}(\Phi \otimes \Phi^*)_{00} &= 0, \\
D_A \Phi &= 0,
\end{aligned}
$$

are the unperturbed PU(2) monopole equations considered in [67], [68], [71], [74], with a slightly differing trace conditions (see below), for a pair $(A, \Phi)$ consisting of a connection on $\mathfrak{su}(E)$ and a section $\Phi$ of $W^{+} \otimes E$.

Donaldson’s proof of the connected-sum theorem for his polynomial invariants [18, Theorem B] makes use of certain ‘extended anti-self-dual equations’ [18, Equation (4.24)] to which the Freed-Uhlenbeck generic metrics theorem does not apply [18, §4(v)]. These extended equations model a neighborhood of the product connection appearing in the Uhlenbeck compactification of the moduli space of anti-self-dual SU(2) connections. As the zero locus of the extended equations may not be transverse, Donaldson employs holonomy perturbations which give gauge-equivariant $C^{\infty}$ maps $\mathcal{A}_E^*(X) \rightarrow \Omega^{+}(\mathfrak{su}(E))$ and thus perturbations of the extended anti-self-dual equations [17, §2], [18, pp. 282–287]. These perturbations are continuous with respect to Uhlenbeck limits and yield transversality not only for the top-level moduli space, but also for all lower-level moduli spaces and all intersections of the geometric representatives defining the Donaldson invariants.

In §2.5.2 and the Appendix we describe a generalization of Donaldson’s idea which we use to prove transversality for the moduli space of solutions to a perturbed version of the PU(2) monopole equations (1.1). Unfortunately, in the case of of PU(2) monopoles, the analysis is considerably more intricate and the method we employ here is rather different from the one developed in [18]. We use an infinite sequence of holonomy sections defined on the infinite-dimensional configuration space of pairs; when restricted to small enough open balls in the configuration space, away from reducible connections, only finitely many of these perturbing sections are non-zero and they vanish at reducible connections.

Let $G_E$ be the Hilbert Lie group of $L_{k+1}^2$ unitary gauge transformations of $E$ with determinant one. Let $S_Z^1$ denote the center of U(2) and set $^\circ G_E := S_Z^1 \times_{\{\pm id_E\}} G_E$, which we may view as the group of $L_{k+1}^2$ unitary gauge transformations of $E$ with constant determinant. The stabilizer of a unitary connection $A$ on $E$ in $^\circ G_E$ (which coincides with its stabilizer in the full group Aut $E$ of unitary automorphisms of $E$) always contains the center $S_Z^1 \subset U(2)$, corresponding to the constant, central, unitary automorphisms of $E$. We call A irreducible if its stabilizer is exactly $S_Z^1$ and reducible otherwise.

It is also possible, as in [71], [74], to fix a smooth representative $\omega \in \Omega^2(X;\mathbb{R})$ for $c_1(E)$ and instead consider the space of unitary connections $A$ on $E$ satisfying the trace condition tr $F_A = -2\pi i\omega$, modulo the action of the full group Aut $E$ of unitary automorphisms of $E$. The resulting moduli space of nonabelian monopoles is then a torus bundle over the moduli space which we define below, with fibers $H^1(X;\mathbb{R})/H^1(X;\mathbb{Z})$. These tori complicate the analysis of the links of singularities when $b^1(X) > 0$ and do not contain any additional information, so we choose to eliminate them by instead imposing the stronger fixed-determinant-connection trace condition and working with a compatible group of gauge transformations. A similar framework is used in [68], [92].

We refer to §2.5 for a detailed account of the construction of our holonomy perturbations. The large number of technical points involving regularity and uniform estimates for these perturbations (which still allow us to obtain an Uhlenbeck compactification) are discussed in the Appendix. We fix $r \geq k+1$ and define gauge-equivariant $C^\infty$ maps (see

---

§2.5),

$$\mathcal{A}_E(X) \rightarrow L_{k+1}^2(X, \mathfrak{gl}(\Lambda^+) \otimes_{\mathbb{R}} \mathfrak{so}(\mathfrak{su}(E))),$$
$$A \mapsto \vec{\tau} \cdot \vec{\mathfrak{m}}(A),$$

(1.2)

$$\mathcal{A}_E(X) \rightarrow L_{k+1}^2(X, \mathrm{Hom}(W^+, W^-) \otimes_{\mathbb{C}} \mathfrak{sl}(E)),$$
$$A \mapsto \vec{\vartheta} \cdot \vec{\mathfrak{m}}(A),$$

where $\vec{\tau} := (\tau_{j,l,\alpha})$ is a suitably convergent sequence in $C^r(X, \mathfrak{gl}(\Lambda^+))$, and $\vec{\vartheta} := (\vartheta_{j,l,\alpha})$ is a suitably convergent sequence in $C^r(X, \Lambda^1 \otimes \mathbb{C})$, while $\vec{\mathfrak{m}}(A) := (\mathfrak{m}_{j,l,\alpha}(A))$ is a sequence in $L_{k+1}^2(X, \mathfrak{su}(E))$ of holonomy sections constructed by extending the method of [17], [18], and

$$\vec{\tau} \cdot \vec{\mathfrak{m}}(A) := \sum_{j,l,\alpha} \tau_{j,l,\alpha} \otimes_{\mathbb{R}} \mathrm{ad}(\mathfrak{m}_{j,l,\alpha}(A)),$$
$$\vec{\vartheta} \cdot \vec{\mathfrak{m}}(A) := \sum_{j,l,\alpha} \rho(\vartheta_{j,l,\alpha}) \otimes_{\mathbb{C}} \mathfrak{m}_{j,l,\alpha}(A).$$

We call a point $(A, \Phi)$ in the pre-configuration space of $L_k^2$ pairs $\tilde{\mathcal{C}}_{W,E} := \mathcal{A}_E \times L_k^2(W^+ \otimes E)$ a PU(2) monopole if it solves

$$F_A^+ - (\mathrm{id} + \tau_0 \otimes \mathrm{id}_{\mathfrak{su}(E)} + \vec{\tau} \cdot \vec{\mathfrak{m}}(A)) \rho^{-1}(\Phi \otimes \Phi^*)_{00} = 0,$$
$$D_A \Phi + \rho(\vartheta_0)\Phi + \vec{\vartheta} \cdot \vec{\mathfrak{m}}(A)\Phi = 0.$$

We let $M_{W,E}$ be the moduli space of solutions cut out of the configuration space of pairs $\mathcal{C}_{W,E} := \tilde{\mathcal{C}}_{W,E}/^\circ \mathcal{G}_E$ by the equations (1.3). We let $M_{W,E}^*,0 \subset M_{W,E}$ be the subspace of pairs $[A, \Phi]$ such that $A$ is irreducible and the section $\Phi$ is not identically zero. The sections $\vec{\tau} \cdot \vec{\mathfrak{m}}(A)$ and $\vec{\vartheta} \cdot \vec{\mathfrak{m}}(A)$ vanish at reducible connections $A$ by construction; plainly, the terms in (1.3) involving the perturbations $\vec{\tau} \cdot \vec{\mathfrak{m}}(A)$ and $\vec{\vartheta} \cdot \vec{\mathfrak{m}}(A)$ are zero when $\Phi$ is zero.

1.1.2. Uhlenbeck compactness. The holonomy-perturbation maps in (1.2) are continuous with respect to the Uhlenbeck topology (see §4.5), just as those of [18]. Suppose $\{A_\beta\}$ is a sequence in $\mathcal{A}_E(X)$ which converges in the Uhlenbeck topology to a limit $(A, \mathbf{x})$ in $\mathcal{A}_{E-\ell}(X) \times \mathrm{Sym}^{\ell}(X)$, where $E_{-\ell}$ is a Hermitian two-plane bundle on $X$ with $\det(E_{-\ell}) = \det E$ and $c_2(E_{-\ell}) = c_2(E) - \ell$, and $\ell \geq 0$ is an integer. The sections $\vec{\tau} \cdot \vec{\mathfrak{m}}(A_\beta)$ and $\vec{\vartheta} \cdot \vec{\mathfrak{m}}(A_\beta)$ then converge in $L_{k+1}^2(X)$ to a section $\vec{\tau} \cdot \vec{\mathfrak{m}}(A, \mathbf{x})$ of $\mathfrak{gl}(\Lambda^+) \otimes_{\mathbb{R}} \mathfrak{so}(\mathfrak{su}(E_{-\ell}))$ and a section $\vec{\vartheta} \cdot \vec{\mathfrak{m}}(A, \mathbf{x})$ of

---

Hom(W+,W-) $\otimes_{\mathbb{C}} \mathfrak{sl}(E_{-\ell})$, respectively. For each $\ell \geq 0$, the maps of (1.2) extend continuously to gauge-equivariant maps

(1.4)
$$\mathcal{A}_{E_{-\ell}}(X) \times \text{Sym}^{\ell}(X) \rightarrow L_{k+1}^{2}(X, \mathfrak{gl}(\Lambda^{+}) \otimes_{\mathbb{R}} \mathfrak{so}(\mathfrak{su}(E_{-\ell}))),$$
$$\mathcal{A}_{E_{-\ell}}(X) \times \text{Sym}^{\ell}(X) \rightarrow L_{k+1}^{2}(X, \text{Hom}(W^{+}, W^{-}) \otimes_{\mathbb{C}} \mathfrak{sl}(E_{-\ell})),$$

given by $(A, x) \mapsto \vec{\tau} \cdot \vec{\mathbf{m}}(A, x)$ and $(A, x) \mapsto \vec{\vartheta} \cdot \vec{\mathbf{m}}(A, x)$, which are $C^{\infty}$ on each $C^{\infty}$ stratum determined by Sym$\ell$(X).

Our construction of the Uhlenbeck compactification for $M_{W,E}$ requires us to consider moduli spaces

$$\mathbf{M}_{W,E_{-\ell}} \subset \mathcal{C}_{W,E_{-\ell}} \times \text{Sym}^{\ell}(X)$$

of triples [A, Φ, x] given by the zero locus of the $^{\circ}\mathcal{G}_{E_{-\ell}}$-equivariant map

$$\mathfrak{S}: \tilde{\mathcal{C}}_{W,E_{-\ell}} \times \text{Sym}^{\ell}(X) \rightarrow L_{k}^{2}(\Lambda^{+} \otimes \mathfrak{su}(E_{-\ell})) \oplus L_{k}^{2}(W^{-} \otimes E_{-\ell})$$

defined as in (1.3) except using the perturbing sections $\vec{\tau} \cdot \vec{\mathbf{m}}$ and $\vec{\vartheta} \cdot \vec{\mathbf{m}}$ in (1.4) instead of those in (1.2). We call $\mathbf{M}_{W,E_{-\ell}}$ a lower-level moduli space if $\ell > 0$ and call $\mathbf{M}_{W,E_{-0}} = M_{W,E}$ the top or highest level.

In the more familiar case of the unperturbed PU(2) monopole equations (1.1), the spaces $\mathbf{M}_{W,E_{-\ell}}$ would simply be products $M_{W,E_{-\ell}} \times \text{Sym}^{\ell}(X)$. In general, though, the spaces $\mathbf{M}_{W,E_{-\ell}}$ are not products when $\ell > 0$ due to the slight dependence of the section $\mathfrak{S}(A, \Phi, x)$ on the points $x \in \text{Sym}^{\ell}(X)$ through the perturbations $\vec{\tau} \cdot \vec{\mathbf{m}}$ and $\vec{\vartheta} \cdot \vec{\mathbf{m}}$. A similar phenomenon is encountered in [18, §4(iv)-(vi)] for the case of the extended anti-self-dual equations, where holonomy perturbations are also employed in order to achieve transversality.

We define $\bar{M}_{W,E}$ to be the Uhlenbeck closure of $M_{W,E}$ in the space of ideal PU(2) monopoles,

$$\bigcup_{\ell=0}^{N} \mathbf{M}_{W,E_{-\ell}} \subset \bigcup_{\ell=0}^{N} \left(\mathcal{C}_{W,E_{-\ell}} \times \text{Sym}^{\ell}(X)\right),$$

for any integer $N \geq N_p$, where $N_p$ is a sufficiently large integer to be specified below.

Theorem 1.1. Let $X$ be a closed, oriented, smooth four-manifold with $C^{\infty}$ Riemannian metric, spin$^c$ structure ($\rho, W^{+}, W^{-}$) with spin$^c$ connection on $W = W^{+} \oplus W^{-}$, and a Hermitian two-plane bundle $E$ with unitary connection on det $E$. Then there is a positive integer $N_p$, depending at most on the curvatures of the fixed connections on $W$ and det $E$ together with $c_2(E)$, such that for all $N \geq N_p$ the topological space $\bar{M}_{W,E}$ is compact, second countable, Hausdorff, and is given by the closure of $M_{W,E}$ in $\cup_{\ell=0}^{N} M_{W,E-\ell}$.

Remark 1.2. The existence of an Uhlenbeck compactification for the moduli space of solutions to the unperturbed PU(2) monopole equations (1.1) was announced by Pidstrigach [71] and an argument was outlined in [74]. A similar argument for equations (1.1) was outlined by Okonek and Teleman in [68]. Theorem 1.1 yields the standard Uhlenbeck compactification for the system (1.1) and the perturbations of (1.1) described in [23], [93] — see Remark 1.4. An independent proof of Uhlenbeck compactness for (1.1) and certain perturbations of these equations is given in [92], [93].

1.1.3. Transversality. The space $\text{Sym}^{\ell}(X)$ is smoothly stratified, the strata being enumerated by partitions of $\ell$. If $\Sigma \subset \text{Sym}^{\ell}(X)$ is a smooth stratum, we define

$$\mathbf{M}_{W,E-\ell}|_{\Sigma} := \{[A, \Phi, \mathbf{x}] \in \mathbf{M}_{W,E-\ell}: \mathbf{x} \in \Sigma\},$$

with $\mathbf{M}_{W,E-0} := M_{W,E}$ when $\ell = 0$. We then have the following transversality result for equations (1.3), at least away from the solutions where the connection is reducible or the spinor vanishes. Let $M_E^{\text{asd}}$ denote the moduli space of anti-self-dual connections on $\mathfrak{su}(E)$.

Theorem 1.3. Let $X$ be a closed, oriented, smooth four-manifold with $C^\infty$ Riemannian metric, spin$^c$ structure $(\rho, W^{+}, W^{-})$ with spin$^c$ connection on $W = W^{+} \oplus W^{-}$, and a Hermitian line bundle $\det E$ with unitary connection. Then there is a first-category subset of the space of $C^\infty$ perturbation parameters such that the following holds. For each 4-tuple $(\tau_0, \vartheta_0, \vec{\tau}, \vec{\vartheta})$ in the complement of this first-category subset, the corresponding moduli space $M_{W,E}^{*,0}$ is a smooth manifold of the expected dimension,

$$\dim M_{W,E}^{*,0} = \dim M_E^{\text{asd},*} + 2 \operatorname{Ind}_\mathbb{C} D_A - 1$$

$$= -2p_1(\mathfrak{su}(E_{-\ell})) - \frac{3}{2}(e(X) + \sigma(X))$$

$$+ \frac{1}{2}p_1(\mathfrak{su}(E_{-\ell})) + \frac{1}{2}\left((c_1(W^{+}) + c_1(E))^2 - \sigma(X)\right) - 1.$$

Moreover, for each integer $\ell \geq 0$, and smooth stratum $\Sigma \subset \text{Sym}^{\ell}(X)$, the moduli space $M_{W,E-\ell}^{*,0}|_{\Sigma}$ is a smooth manifold of the expected dimension,

$$\dim M_{W,E-\ell}^{*,0}|_{\Sigma} = \dim M_{W,E-\ell}^{*,0} + \dim \Sigma.$$

---

Remark 1.4. Different approaches to the question of transversality for the PU(2) monopole equations (1.1) with generic perturbation parameters have been considered by Pidstrigach and Tyurin in [74] and Teleman in [92]. More recently, a new approach to transversality for (1.1) has been discovered independently by the first author [23] and Teleman [93]: the method uses only the perturbations ($\tau_0, \vartheta_0$) together with perturbations of the Riemannian metric $g$ on $X$ and compatible Clifford map $\rho$.

A choice of generic Riemannian metric on $X$ ensures that the moduli space $M_E^{\text{asd},*}$ of irreducible anti-self-dual connections on $\mathfrak{su}(E)$ is smooth and of the expected dimension [20], [30], although the points of $M_E^{\text{asd},*}$ need not be regular points of $M_W, E^*$ as the linearization of (1.3) may not be surjective there. A choice of generic parameter $\tau_0$ ensures that the moduli spaces $M_{W, E, L_1}^{\text{red},0}$ of non-zero-section solutions to (1.3) which are reducible with respect to the splitting $E = L_1 \oplus (\det E) \otimes L_1^*$ are smooth and of the expected dimension [25]. Again, the points of $M_{W, E, L_1}^{\text{red},0}$ need not be regular points of $M_0^W, E$ since the linearization of (1.3) may not be surjective there.

We note that related transversality and compactness issues have been recently considered in approaches to defining Gromov-Witten invariants for general symplectic manifolds [59], [75], [79].

1.2. Outline. We indicate how the remainder of our article is organized. In §2.2 we prove a slice result for the configuration space $C_{W, E}$ (Proposition 2.8) while in §2.6 we describe the elliptic deformation complex for (1.3) and compute the expected dimension of $M_{W, E}$. We develop the regularity theory for a generalization of the PU(2) monopole equations (1.3) (obtained by allowing additional inhomogeneous terms) in §3: the main technical result there is that an $L_1^2$ solution to an inhomogeneous version of (1.3) and the Coulomb gauge equation is $C^\infty$ (Corollary 3.4). By combining this with the slice result of Proposition 2.8, we then show that any $L_k^2$ PU(2) monopole $(A, \Phi)$ is $L_{k+1}^2$ gauge-equivalent to a $C^\infty$ PU(2) monopole (Proposition 3.7).

We establish local estimates for $L_1^2$ solutions to the inhomogeneous version of (1.3) in §3.3 and §3.4. We use the sharp $L_1^2$ regularity result of Corollary 3.4 in §4 to prove the removability of point singularities for PU(2) monopoles (Theorem 4.10). In the sequels [26], [27], these regularity results and estimates are needed to prove that $L_1^2$ gluing solutions to (1.3) are $C^\infty$ and to analyse the asymptotic behavior of Taubes' gluing maps and their differentials near the lower strata of the Uhlenbeck compactification.

The proof of Theorem 1.1 relies heavily on both the regularity theory of §3 and the fact that solutions $(A, \Phi)$ to (1.3) satisfy a ‘universal energy bound’, with constant depending only on the data in the hypotheses of Theorem 1.1. The section $\Phi$ also satisfies a universal $C^0$ bound: these bounds are the analogues for PU(2) monopoles of the now well-known a priori estimates for Seiberg-Witten monopoles [47], [62], [77], [98] and follow, in much the same way, from the maximum principle and the Bochner-Weitzenböck formula for $D_A$ provided $k \geq 3$ (see §4.1). In §4 we prove the removability of point singularities for solutions to (1.3) (Theorem 4.10) using our a priori bounds and regularity results. While the PU(2) monopole equations are not conformally invariant, they are invariant under constant rescalings of the metric (in the sense of §4.2) and, as in the case of anti-self-dual connections, this scale invariance is exploited in the proof of Theorem 1.1, whose proof is completed in §4.6.

Theorem 1.3 is initially established in §5 for $C^r$ perturbations for any fixed $3 \leq r < \infty$, in order to avail of the Sard-Smale theorem for Fredholm maps of Banach manifolds [80], while in §5.1.2 we show that generic $C^\infty$ perturbation parameters are sufficient for transversality. (See Corollary 5.6 for the special case $\ell = 0$ and §5.1.3 for its extension to the general case $\ell \geq 0.$)

As we shall explain in §5, our proof of Theorem 1.3 ultimately hinges on the fact that if $(A, \Phi)$ is a PU(2) monopole and $A$ is reducible on a non-empty open subset containing the support of the holonomy perturbations depending on $A$, then $A$ is reducible over $X$. The proof of this result (Theorem 5.11) occupies §5.3; the result follows from the Agmon-Nirenberg unique continuation theorem after the system (1.3) has been transformed into an ordinary differential equation for a one-parameter family of pairs over $S^3$. The unique continuation property holds for both the perturbed PU(2) monopole equations (1.3), when the initial open subset of $X$ contains the balls in $X$ supporting holonomy perturbations, and the unperturbed equations (1.1) for any initial open subset.

1.3. Other approaches to transversality. As we noted in Remark 1.4, transversality for the PU(2) monopole equations (1.1) has also been proved very recently using only the perturbations $(\tau_0, \vartheta_0)$, together with perturbations of the Riemannian metric $g$ on $X$ and compatible Clifford map $\rho$ [23], [93]. The transversality proof given in [23] is more delicate than the method we employ in the present article. When using holonomy perturbations, the main technical difficulties are due to the noncompactness of the moduli space of PU(2) monopoles, and the core transversality argument itself is more straightforward, whereas in [23] the situation is entirely reversed. To place these various transversality results in a suitable context, we briefly discuss some other approaches to transversality, both for the PU(2) monopole equations and the closely related ‘spin-ASD’ equations of [73], which Pidstrigach and Tyurin used to define spin polynomial invariants.

Suppose $(A, \Phi)$ is a solution to either equations (1.1), equations (1.1) with perturbations $(\tau_0, \vartheta_0)$, or the holonomy-perturbed equations (1.3). If $A$ is reducible, then $\Phi$ has rank less than or equal to one (see Lemma 5.22). However, as observed by Teleman [69], [92], if $\Phi$ is rank one, then $A$ is not necessarily reducible and he describes a simple counterexample for equations (1.1) when $X$ is a Kähler manifold with its canonical spin$^c$ structure.

It is not too difficult to prove that $M_{W,E}^{*,0}$ is a smooth manifold of the expected dimension away from the locus of irreducible, rank-one solutions using the perturbation parameters $(\tau_0, \vartheta_0)$ alone. However, as irreducible, rank-one solutions to (1.3) could be present in $M_{W,E}^{*,0}$, it appears impossible to prove that the entire space $M_{W,E}^{*,0}$ is a smooth manifold of the expected dimension using only the parameters $(\tau_0, \vartheta_0)$. A similar problem arises in the proof of transversality for the spin-ASD equations given in [73, Proposition I.3.5]; a version of these equations can be obtained from equations (1.1) by omitting the quadratic term $\rho^{-1}(\Phi \otimes \Phi^*)_{00}$. In the proof of [73, Proposition I.3.5] it is claimed that if $D_A\Phi = 0$ and $\Phi$ is rank one, then $A$ is reducible [p. 277]: Teleman’s counterexample shows that this claim is incorrect, and he points out an error in their argument [69], [92]. On the other hand, the possible presence or absence of irreducible, rank-one solutions to the PU(2) monopole equations makes no difference to the transversality argument which we describe in §5 using holonomy perturbations, as these perturbations are strong enough to yield transversality without a separate analysis of the locus of irreducible, rank-one solutions.

1.4. Applications. In [25] we discuss the singularities of the moduli space $M_{W,E}$. We introduce cohomology classes and geometric representatives on $M_{W,E}^*$, construct the links of the strata of anti-self-dual and Seiberg-Witten moduli spaces in $M_{W,E}$, and compute the Chern characters of their normal bundles in suitably defined ambient manifolds. We thus obtain a relation between Donaldson and Seiberg-

---

Witten invariants when the reducible solutions appear only in the top level of the Uhlenbeck compactification. In [26], [27], we develop the gluing theory for PU(2) monopoles: this is used to construct links of the lower-level Seiberg-Witten moduli spaces, to show that the pairing of the cohomology classes with this link is well-defined, and to eliminate the requirement of [25] that the reducible solutions appear only in the top level. A survey of some of the results contained in the present article and its sequels [25], [26], [27] is provided in [24].

## Acknowledgements

The first author is especially grateful to Peter Kronheimer, Tom Mrowka, and Cliff Taubes for helpful conversations and for their enthusiasm and encouragement. He is particularly grateful to Tom Mrowka for bringing to his attention a couple of points in the manuscript that needed correcting. He would also like to thank the Harvard Mathematics Department and the National Science Foundation for their generous support. The second author is very grateful to Selman Akbulut, Ron Fintushel, and Tom Parker for helpful conversations and the Mathematics Departments at Harvard and Michigan State Universities for their hospitality and support. We warmly thank the referee for his careful reading of the manuscript and thoughtful comments.

## 2. The PU(2) monopole equations

We develop a framework for gauge theory for pairs in §2.1 and §2.2. In §2.1 we define the Hilbert spaces of pairs and gauge transformations, while in §2.2 we establish the main slice result which we require for the configuration space of pairs modulo gauge transformations, paying particular attention to the structure near ‘reducibles’. The relationship between the groups of SO(3) and SU(2) gauge transformations is discussed in §2.3. A few linear algebra issues which will be important for later compactness and transversality arguments are discussed in §2.4. The PU(2) monopole equations and their holonomy perturbations are introduced in §2.5. The role of the perturbations in obtaining transversality results will be explained in §5. To preserve continuity a detailed discussion of the technical points which need to be addressed when using holonomy perturbations in the present context is deferred to the Appendix. The moduli space and the elliptic deformation complex for solutions to the PU(2) monopole equations are described in §2.6.

2.1. Configuration spaces of connections and pairs. In this section we define the spaces of connections, pairs, gauge transformations, and configuration spaces which we will use throughout our work.

2.1.2. Connections on Hermitian two-plane bundles. We consider Hermitian two-plane bundles $E$ over $X$ whose determinant line bundles det $E$ are isomorphic to a fixed Hermitian line bundle over $X$ endowed with a fixed $C^\infty$, unitary connection $A_e$. The Hermitian line bundle over $X$ and its unitary connection $A_e$ are fixed for the remainder of this article.

Let $k \geq 2$ be an integer and let $\mathcal{A}_E$ be the space of $L_k^2$ connections $A$ on the U(2) bundle $E$ all inducing the fixed determinant connection $A_e$ on det $E$. Equivalently, following [48, §2(i)], we may view $\mathcal{A}_E$ as the space of $L_k^2$ connections $A$ on the PU(2) = SO(3) bundle $\mathfrak{su}(E)$. We shall pass back and forth between these viewpoints, via the fixed connection on det $E$, relying on the context to make the distinction clear. Explicitly, if $A$ is a unitary connection on $E$ and $s \in \Omega^0(X, E)$, then $\nabla_A s \in \Omega^1(E)$. For $\zeta \in \Omega^0(X, \mathfrak{u}(E))$, then $\nabla_A \zeta \in \Omega^1(X, \mathfrak{u}(E))$ is determined by

$$
(\nabla_A \zeta)s = \nabla_A(\zeta s) - \zeta(\nabla_A s),
$$

so, if $A^\tau \in \Omega^1(U, \mathfrak{u}(2))$ denotes the local connection matrix defined by a choice of local frame for $E$ over an open subset $U \subset X$, then

$$
\nabla_A s = ds + A^\tau s,
$$

$$
\nabla_A \zeta = d\zeta + [A^\tau, \zeta] = d\zeta + (\mathrm{ad}A^\tau)\zeta.
$$

Similarly, the connection $A$ on $E$ induces connections on $\mathfrak{su}(E)$ and det $E$. For example, if $\xi \in \Omega^0(X, \mathfrak{su}(E))$, then $\nabla_A \xi \in \Omega^1(X, \mathfrak{su}(E))$ is also given locally by

$$
\nabla_A \xi = d\xi + [A^\tau, \xi] = d\xi + [(A^\tau)_0, \xi] = d\zeta_0 + (\mathrm{ad}A^\tau)\zeta_0,
$$

while if $\lambda \in \Omega^0(X, \det E)$ then $\nabla_A \lambda \in \Omega^1(X, \det E)$ is given by

$$
\nabla_A \lambda = d\lambda + (\mathrm{tr}A^\tau)\lambda.
$$

The above local connection matrices are related by

$$
A^\tau = (A^\tau)_0 + \frac{1}{2}(\mathrm{tr}A^\tau) \mathrm{id}_{\mathbb{C}^2} \in \Omega^1(U, \mathfrak{u}(2)),
$$ where $(A^{\tau})_0 = A^{\tau} - \frac{1}{2}(\text{tr } A^{\tau}) \text{id}_{\mathbb{C}^2} \subset \Omega^1(U, \mathfrak{su}(2))$ is the traceless component of $A^{\tau}$, while $\text{tr } A^{\tau} \subset \Omega^1(U, \mathfrak{u}(1)) = \Omega^1(U, i\mathbb{R})$ is the induced local connection form for det $E$ given by the trace component of $A^{\tau}$. Note that $(A^{\tau})_0 \in \Omega^1(U, \mathfrak{su}(2)),$ and that $\text{ad}(A^{\tau})_0 = \text{ad}A^{\tau} \in \Omega^1(U, \mathfrak{so}(3))$ is the induced local connection matrix for the SO(3) bundle $\mathfrak{su}(E)$, where we use the standard identification $\mathfrak{so}(3) = \text{ad}(\mathfrak{su}(2))$.

Conversely, given a unitary connection $A_e$ for det $E$ and a Riemannian connection $\hat{A}$ for $\mathfrak{su}(E)$, we obtain a unitary connection for $E$ given in terms of local connection matrices by

$$A^{\tau} = \text{ad}^{-1}(\hat{A}^{\tau}) + \frac{1}{2}A_e^{\tau} \text{id}_{\mathbb{C}^2} \in \Omega^1(U, \mathfrak{u}(2)).$$

The curvatures of these connection matrices are related by

$$F_{A^{\tau}} = \text{ad}^{-1}(F_{\hat{A}^{\tau}}) + \frac{1}{2}F_{A_e^{\tau}} \text{id}_{\mathbb{C}^2} \in \Omega^2(U, \mathfrak{u}(1)).$$

Thus, $(F_{A^{\tau}})_0 = \text{ad}^{-1}(F_{\hat{A}^{\tau}})$ and $\text{tr } F_{A^{\tau}} = F_{A_e^{\tau}} = F(\text{tr } A^{\tau})$. Therefore, globally we have $(F_A)_0 = \text{ad}^{-1}F_{\hat{A}} \in \Omega^2(X, \mathfrak{su}(E))$ and $\text{tr } F_A = F_{A_e} \in \Omega^2(X, \mathfrak{u}(1)) = \Omega^2(X, i\mathbb{R})$, so that

$$F_A = \text{ad}^{-1}(F_{\hat{A}}) + \frac{1}{2}F_{A_e} \text{id}_E \in \Omega^2(X, \mathfrak{u}(E)),

as $\mathfrak{u}(E) = \mathfrak{su}(E) \oplus (i\mathbb{R}) \text{id}_E$.

When we are not explicitly discussing connections which are reducible with respect to some splitting of $E$, it is generally more convenient to view our connections as being defined on $\mathfrak{su}(E)$ rather than $E$ as we can then avoid explicit mention of the otherwise unimportant choice of fixed connection on det $E$. Of course, these viewpoints are equivalent via the choice of this fixed determinant connection. The isomorphism $\text{ad}: \mathfrak{su}(E) \rightarrow \mathfrak{so}(\mathfrak{su}(E))$ will remain implicit when no confusion can arise so that, given a connection $A$ on $\mathfrak{su}(E)$, we write its curvature as $F_A \in \Omega^2(\mathfrak{su}(E))$ and associated deformation complexes on $\Omega^\bullet(\mathfrak{su}(E))$ rather than $F_A \in \Omega^2(\mathfrak{so}(\mathfrak{su}(E)))$, with deformation complexes on $\Omega^\bullet(\mathfrak{so}(\mathfrak{su}(E)))$ (see [30, Chapter 10], for comparison).

2.1.2. Spin$^c$ structures. The minimal, axiomatic approach to the definition of spin$^c$ structures and the Dirac operator employed by Kronheimer-Mrowka [49] and Mrowka-Ozsváth-Yu [66] is extremely useful for our purposes, so this is the method we shall follow here.

Recall that a real-linear map $\rho_+ : T^*X \rightarrow \text{Hom}(W^+, W^-)$ defines a Clifford map $\rho : \Lambda^\bullet(T^*X) \otimes \mathbb{C} \rightarrow \text{End}(W)$, with $W := W^+ \oplus W^-$, if and only if [57], [77]

(2.1) $\rho_+(\alpha)^\dagger \rho_+(\alpha) = g(\alpha, \alpha)\mathrm{id}_{W^+}, \quad \alpha \in C^\infty(T^*X),$

where $g$ denotes the Riemannian metric on $T^*X$. The real-linear map $\rho : T^*X \to \mathrm{End}(W^+ \oplus W^-)$ is obtained by defining a real-linear map

$$
\rho_- : T^*X \to \mathrm{Hom}(W^-, W^+), \quad \alpha \mapsto \rho_-(\alpha) := -\rho_+(\alpha)^\dagger,
$$

and setting

(2.2) $\rho(\alpha) := \begin{pmatrix} 0 & \rho_-(\alpha) \\ \rho_+(\alpha) & 0 \end{pmatrix}.$

This extends to a linear map $\rho : \Lambda^\bullet(T^*X) \otimes \mathbb{C} \to \mathrm{End}(W^+ \oplus W^-)$ and satisfies

(2.3) $\rho(\alpha)^\dagger = -\rho(\alpha)$ and $\rho(\alpha)^\dagger \rho(\alpha) = g(\alpha, \alpha)\mathrm{id}_W,$
$$
\alpha \in C^\infty(T^*X).
$$

A unitary connection $\nabla$ on $W$ and $g$-compatible Clifford map $\rho$ induce a unique SO(4) connection $\nabla^g$ on $T^*X$ by requiring that

(2.4) $[\nabla_\eta, \rho(\alpha)] = \rho(\nabla_\eta^g \alpha),$

for all $\eta \in C^\infty(TX)$ and $\alpha \in \Omega^1(X, \mathbb{R})$; the sign above is opposite to that used in [66]. The unitary connection $\nabla$ on $W$ uniquely determines a unitary connection on $\det W^+ \simeq \det W^-$ in the standard way [43]. Conversely, the preceding data uniquely determines a unitary connection $\nabla$ on $W$. The connection $\nabla$ on $W$ is called a spin$^c$ connection if the connection $\nabla^g$ on $T^*X$ is also torsion free, that is, if $\nabla^g$ is the Levi-Civita connection for the metric $g$.

Given a unitary connection $A$ on an auxiliary Hermitian two-plane bundle $E$, we let $\nabla_A$ denote the induced unitary connection on $W \otimes E$. The corresponding Dirac operator $D_A$ is defined by

$$
D_A := \sum_{\mu=1}^4 \rho(v^\mu)\nabla_{A,v_\mu},
$$

where $\{v_\mu\}$ is a local frame for $TX$ and $\{v^\mu\}$ is the dual frame for $T^*X$ defined by $v^\mu(v_\mu) = \delta_{\mu\nu}$.

---

2.1.3. Pre-configuration spaces and automorphism groups
We denote $\Lambda^\bullet := \Lambda^\bullet(T^*X)$. For any fixed $L_k^2$ connection $A_0 \in \mathcal{A}_E$ we therefore write

$$\mathcal{A}_E = A_0 + L_k^2(\Lambda^1 \otimes \mathfrak{su}(E)),$$

for either fixed-determinant, unitary connections on $E$ or determinant-one, orthogonal connections on $\mathfrak{su}(E)$. Our pre-configuration space of pairs is given by

$$\tilde{\mathcal{C}}_{W,E} := \mathcal{A}_E \times L_k^2(W^+ \otimes E),$$

and for any fixed $L_k^2$ pair $(A_0, \Phi_0) \in \tilde{\mathcal{C}}_{W,E}$, we have

(2.5) $$\tilde{\mathcal{C}}_{W,E} = (A_0, \Phi_0) + L_k^2(\Lambda^1 \otimes \mathfrak{su}(E)) \oplus L_k^2(W^+ \otimes E),$$

for the cases of either fixed-determinant, unitary connections on $E$ or determinant-one, orthogonal connections on $\mathfrak{su}(E)$.

Given any $C^\infty$ connection $A_0 \in \mathcal{A}_E$, our Sobolev norms are defined in the usual way: for example, if $a \in \Omega^1(\mathfrak{su}(E))$, we write

$$\|a\|_{L_\ell^p,A_0(X)} := \left( \sum_{j=0}^{\ell} \|\nabla_A^j a\|_{L_p(X)} \right)^{1/p},$$

and if $(a, \phi) \in \Omega^1(\mathfrak{su}(E)) \oplus \Omega^0(W^+ \otimes E)$, we write

$$\|(a, \phi)\|_{L_\ell^p,A_0(X)} := \left( \|a\|_{L_\ell^p,A_0(X)} + \|\phi\|_{L_\ell^p,A_0(X)} \right)^{1/p},$$

for any $1 \leq p \leq \infty$ and integer $\ell \geq 0$.

For convenience, we let $i\mathbb{R}_Z = (i\mathbb{R}) \mathrm{id}_{\mathbb{C}^2} \subset \mathfrak{u}(2)$ denote the center of the Lie algebra $\mathfrak{u}(2)$, and let $S_Z^1 = \exp(i\mathbb{R}_Z) \subset U(2)$ denote the center $Z(U(2))$ of the Lie group $U(2)$ given by

(2.6) $$i\mathbb{R}_Z = \left\{ \begin{pmatrix} i\theta & 0 \\ 0 & i\theta \end{pmatrix}: \theta \in \mathbb{R} \right\}, \quad S_Z^1 = \left\{ \begin{pmatrix} e^{i\theta} & 0 \\ 0 & e^{i\theta} \end{pmatrix}: \theta \in \mathbb{R} \right\}.$$

Following [48, §2], we consider the induced action for connections on $\mathfrak{su}(E)$ by the group $\mathcal{G}_E$ of determinant-one, unitary $L_k^2+1$ automorphisms of $E$ rather than the group $\mathcal{G}_{\mathfrak{su}(E)}$ of determinant-one, orthogonal $L_k^2+1$ automorphisms of $\mathfrak{su}(E)$ to define quotient spaces of connections on $\mathfrak{su}(E)$. The reasons for this choice are explained further in [25]; see also §2.3. We have

$$\mathcal{G}_E := \{ u \in L_k^2+1(\mathfrak{gl}(E)) : u^{\dagger}u = \mathrm{id}_E \text{ and det } u = 1 \text{ a.e.}\},$$ and

$$
^\circ G_E := S_Z^1 \times_{\pm id_E} G_E.
$$

One can define the action of $^\circ G_E$ on $A_E$ either by push-forward or pullback, and obtain equivalent quotient spaces in either case; but the choice does affect the orientation of moduli spaces, so we specify the action here: for $u \in^\circ G_E$ and $(A, \Phi) \in \tilde{C}_{W,E}$, the action of $^\circ G_E$ is defined by

$$u(A, \Phi) := (u(A), u\Phi) = (u_* A, u\Phi) = ((u^{-1})^* A, u\Phi).$$

The push-forward action, $u(A) = u_* A$, agrees with the conventions of [9], [20]. For the associated covariant derivative $\nabla_A$ on $E$ and $u \in \text{Aut } E$, we have

$$\nabla_{u(A)} = u \circ \nabla_A \circ u^{-1},$$

so that $u(A) = A - (\nabla_A u)u^{-1}$. In terms of a local connection matrix $A^\tau \in \Omega^1(U, \mathfrak{u}(2))$, this gives $u(A^\tau) = uA^\tau u^{-1} - (du)u^{-1}$, where we use $u$ to denote both the gauge transformation and the element of $\Omega^0(U, \text{U}(2))$.

In order to define quotients by the action of $^\circ G_E$, we need to choose $k \geq 2$, so gauge transformations are at least continuous. The proof of the following proposition is a standard application of the Sobolev multiplication theorem; see [30, Propositions A.2, A.3, A.9].

**Proposition 2.1.** Let $X$ be a closed Riemannian four-manifold, $E$ be a Hermitian vector bundle over $X$, and $k \geq 2$ be an integer. Then the following hold:

(1) The space $^\circ G_E$ is a Hilbert Lie group with Lie algebra $T_{\mathrm{id}}^\circ G_E = L_{k+1}^2(\mathfrak{su}(E)) \oplus i\mathbb{R}_Z$.

(2) The action of $^\circ G_E$ on $\tilde{C}_{W,E}$ is smooth.

(3) For $(A, \Phi) \in \tilde{C}_{W,E}$, the differential, at the identity $id_E \in^\circ G_E$, of the map $^\circ G_E \rightarrow \tilde{C}_{W,E}$ given by $u \mapsto u(A, \Phi) = (A - (d_A u)u^{-1}, u\Phi)$ is $\zeta \mapsto -d_A^0_\phi \zeta := (-d_A \zeta, \zeta\Phi)$ as a map

$$L_{k+1}^2(\mathfrak{su}(E)) \oplus i\mathbb{R}_Z \rightarrow L_k^2(\Lambda^1 \otimes \mathfrak{su}(E)) \oplus L_k^2(W^+ \otimes E).$$

We denote $B_E = A_E/G_E = A_E/^\circ G_E$. The configuration space of pairs is given by $C_{W,E} := \tilde{C}_{W,E}/^\circ G_E$, that is,

$$C_{W,E} := \left( A_E \times L_k^2(W^+ \otimes E) \right)/^\circ G_E = A_E \times^\circ G_E L_k^2(W^+ \otimes E),$$ and is endowed with the quotient $L_k^2$ topology.

If $\pi$ denotes the projection $\tilde{\mathcal{C}}_{W,E} \rightarrow \mathcal{C}_{W,E}$, a base for the quotient $L_k^2$ topology of $\mathcal{C}_{W,E}$ is given by open subsets $\pi^{-1}\pi(B_{(A,\Phi)}(\varepsilon)) \supset B_{(A,\Phi)}(\varepsilon)$, where $B_{(A,\Phi)}(\varepsilon)$ is the $L_k^2$-ball of radius $\varepsilon$ and center $(A,\Phi)$ in $\tilde{\mathcal{C}}_{W,E}$ given by $\{(A_1,\Phi_1) \in \tilde{\mathcal{C}}_{W,E}: \|(A_1,\Phi_1) - (A,\Phi)\|_{L_k^2,A} < \varepsilon\}$.

2.1.4. Stabilizers. The space $\mathcal{C}_{W,E}$ is not a manifold — it has singularities at points $[A,\Phi]$ with non-trivial stabilizer $\text{Stab}_{A,\Phi} \subset {}^\circ G_E$. Recall that the stabilizer subgroup (of the group of bundle automorphisms) for a connection on a $G$ bundle always contains the center $Z(G) \subset G$ [20, §4.2.2]. We let $S_Z^1 \subset {}^\circ G_E$ denote the constant, central automorphisms of $E$.

Definition 2.2. Suppose $(A,\Phi)$ is a point in $\tilde{\mathcal{C}}_{W,E}$. The stabilizer $\text{Stab}_{A,\Phi} \subset {}^\circ G_E$ of $(A,\Phi)$ in ${}^^\circ G_E$ is given by $\{\gamma \in {}^\circ G_E : \gamma(A,\Phi) = (A,\Phi)\}$, while the stabilizers of $A$ and $\Phi$ are denoted by $\text{Stab}_A$ and $\text{Stab}_\Phi$, respectively.

(1) The point $(A,\Phi)$ is a zero-section pair if $\Phi \equiv 0$;

(2) The point $(A,\Phi)$ is an irreducible pair if the connection $A$ has minimal stabilizer $\text{Stab}_A = Z(\text{U}(2)) = S_Z^1 \subset {}^\circ G_E$ and is reducible otherwise, that is, if $\text{Stab}_A \supseteq S_Z^1$.

The point $(A,\Phi)$ is a reducible, zero-section pair if $(A,\Phi)$ is both a reducible and zero-section pair.

As usual, the stabilizer subgroup $\text{Stab}_A \subset {}^\circ G_E$ may be identified with a closed subgroup of $\text{U}(E_x_0) \simeq \text{U}(2)$ for any point $x_0 \in X$ by parallel translation with respect to the connection $A$ [20, §4.2.2], [61]. The following lemma implies that the stabilizer in Aut $E$ of a unitary connection on $E$ coincides with its stabilizer on ${}^^\circ G_E$.

Lemma 2.3. Let $E$ be a Hermitian two-plane bundle over a connected four-manifold $X$, let $A$ be a unitary connection on $E$, and let $u$ be a unitary automorphism of $E$ such that $u \in \text{Stab}_A \subset \text{Aut } E$. Then det $u : X \to S^1$ is a constant map.

Proof. The gauge transformation $u$ may be viewed as an Ad-equivariant map $u : P \rightarrow \text{U}(2)$, where $E = P \times_{\text{U}(2)} \mathbb{C}^2$, so det $u$ may be viewed as a map from $P$ to $S^1$. Since det $u$ is constant on the fibers of $P$, it descends to a map on $X$. Over a small enough open set $U \subset X$, we may write $u = \exp \zeta$, where $\zeta \in \Omega^0(\text{ad}P)$, and $\text{ad}P := P \times_{\text{ad}} \mathfrak{g} \simeq \mathfrak{u}(E)$, with $G = \text{U}(2)$ and $\mathfrak{g} = \mathfrak{u}(2)$. Differentiating the action of $u$ on $A$ we see that $\nabla_A \zeta = 0$, so that $\zeta$ is covariantly constant over $U$. Thus det $u = \exp(\text{tr} \zeta)$ and $\nabla(\det u) = \text{tr}(\nabla_A \zeta) = 0$, so det $u$ is constant on $U$ and therefore on $X$, since $X$ is connected. q.e.d.

For a pair $(A, \Phi)$ on $(E, W^+ \otimes E)$ or $(\mathfrak{su}(E), W^+ \otimes E)$, the Lie algebras of Stab$_A$ and Stab$_{A,\Phi}$ are given by

$$H_0^A := \text{Ker}\{d_A : L_{k+1}^2(\mathfrak{su}(E)) \oplus i\mathbb{R}_Z$$
$$\rightarrow L_k^2(\Lambda^1 \otimes \mathfrak{su}(E))\},$$

$$H_0^A_{A,\Phi} := \text{Ker}\{d_{A,\Phi}^0 : L_{k+1}^2(\mathfrak{su}(E)) \oplus i\mathbb{R}_Z$$
$$\rightarrow L_k^2(\Lambda^1 \otimes \mathfrak{su}(E)) \oplus L_k^2(\Lambda^1 \otimes W^+ \otimes E)\}.$$

The first identification is standard (see [20, §4.2.2], [30, Chapter 3], or [61]) and the second follows by the same argument.

From [20, §4.2.2] and [30, Theorem 10.8] we have the following characterization of the stabilizer Stab$_B \subset \mathcal{G}_V = \text{Aut } V$ of a connection $B$ on an SO(3) bundle $V$. Note that the four-manifold $X$ below need not be simply-connected or closed and that $H_B^0 = \text{Ker}\{d_B : L_{k+1}^2(\mathfrak{so}(V)) \rightarrow L_k^2(\Lambda^1 \otimes \mathfrak{so}(V))\}.$

**Lemma 2.4.** Let $B$ be an orthogonal connection on an SO(3) bundle $V$ over a connected smooth four-manifold $X$. The following are equivalent provided $B$ is not flat:

(1) Stab$_B \simeq \text{SO}(2) \simeq S^1$;

(2) $H_B^0 \neq 0$;

(2) $B$ is reducible with respect to an orthogonal splitting $V = N \oplus \mathbb{R}$, where $N$ is a complex line bundle over $X$ and $\mathbb{R} = X \times \mathbb{R}$ (that is, $B$ reduces to an SO(2) connection);

(4) Stab$_B \neq \{\text{id}_V\}.$

Finally, $B$ is flat if Stab$_B = \text{SO}(3).$

**Remark 2.5.** Note that the ‘twisted reducible’ (that is, locally reducible) connections on $\mathfrak{su}(E)$ discussed by Kronheimer and Mrowka in [48, §2(i)] are globally irreducible in the sense that they have minimal stabilizer $\{\text{id}_{\mathfrak{su}(E)}\}$. The condition that $B$ is not flat is used in the proof that (4) implies (1) [30, p. 48]: the stabilizer Stab$_B$ is isomorphic to the centralizer of the holonomy group Hol$_B$ so, if Stab$_B \supset S^1$, then Hol$_B \subset S^1$ and hence Hol$_B$ is discrete. Since the Lie algebra of Hol$_B$ vanishes, the Ambrose-Singer holonomy theorem implies that the connection $B$ is flat. In particular, we only need $X$ to be a connected four-manifold for these arguments to hold.

As customary, we call an SO(3) connection $B$ on $V$ irreducible if $\text{Stab}_B = \{\text{id}_V\}$. We say that a unitary connection $A$ on $E$ is projectively flat if the induced connection $A^{\text{ad}}$ on $\mathfrak{su}(E)$ is flat. By modifying the proofs of Theorem 3.1 in [30] and Proposition II.8.10 [56], we obtain the following relation between (i) the stabilizers $\text{Stab}_A$ in $^\circ G_E$ of U(2) connections $A$ on $E$ or their induced SO(3) connections $A^{\text{ad}}$ on $\mathfrak{su}(E)$ and (ii) the stabilizers $\text{Stab}_{A^{\text{ad}}}$ in $G_{\mathfrak{su}(E)}$ of SO(3) connections $A^{\text{ad}}$ on $\mathfrak{su}(E)$.

**Lemma 2.6.** Let $A$ be a U(2) connection on a Hermitian two-plane bundle $E$ over a smooth, connected four-manifold $X$, and let $A^{\text{ad}}$ be the induced SO(3) connection on the bundle $\mathfrak{su}(E)$. Then the following are equivalent:

(1) $\text{Stab}_{A^{\text{ad}}} \simeq S^1$;

(2) $\text{Stab}_A \simeq S^1 \times S^1_Z$;

(3) $H_A^0 \simeq i\mathbb{R} \oplus i\mathbb{R}_Z$;

(4) $H_{A,\Phi}^0 \supset i\mathbb{R}_Z$;

(5) $A$ is reducible with respect to an orthogonal splitting $E = L_1 \oplus L_2$, where $L_1$ and $L_2$ are complex line bundles over $X$ (that is, $A$ reduces to a $T^2 = S^1 \times S^1$ connection);

(6) $\text{Stab}_A \supset S^1_Z$.

Finally, the connection $A$ on $E$ is projectively flat (or the connection $A^{\text{ad}}$ on $\mathfrak{su}(E)$ is flat) if $\text{Stab}_A = \U(2)$.

**Proof.** (1) $\implies$ (2): Let $\pi : \U(2) \rightarrow \text{SO}(3) = \U(2)/S^1_Z$ be the projection $u \mapsto \pm(\det u)^{-1/2}u$. Then $\pi^{-1}(\text{Stab}_{A^{\text{ad}}}) \simeq \text{Stab}_{A^{\text{ad}}} \times S^1_Z$ and so $\text{Stab}_{A^{\text{ad}}} \simeq S^1$ implies that $\text{Stab}_A \simeq S^1 \times S^1_Z$.

(2) $\implies$ (3): Immediate from the identification of $H_A^0$ as the Lie algebra of $\text{Stab}_A$.

(3) $\implies$ (4): Trivial.

---

$$
(4)\implies(5)
$$

(4) $ \Longrightarrow $ (5): We argue as in the proof of Theorem 3.1 in [30]. Note that Ker $ \{d_{A}:L_{k+1}^{2}(X,\mathfrak{u}(E))\to\Omega^{1}(X,\mathfrak{u}(E))\} $ is isomorphic to

$$
\mathrm{Ker}\{d_A:L_{k+1}^2(X,\mathfrak{u}(E))\to\Omega^1(X,\mathfrak{u}(E))\}
$$

$$
\begin{align*}\mathrm{Ker}\{d_A:L^2_{k+1}(X,\mathfrak{s u}(E))\}\oplus\mathrm{Ker}\{d:L^2_{k+1}(X,i\mathbb{R}_Z)\}\\=\mathrm{Ker}\{d_{A^{\mathrm{ad}}}:L^2_{k+1}(X,\mathfrak{s u}(E))\}\oplus i\mathbb{R}_Z.\end{align*}
$$

Given (4), we may choose $ 0\neq \zeta\in\operatorname{Ker}\left\{d_{A}:L_{k+1}^{2}\Omega^{0}(X,\mathfrak{su}(E))\right\}.$ The pointwise traceless, skew-Hermitian endomorphism $ \zeta $ of E has eigenvalues $ i\lambda_{1},i\lambda_{2}=\pm i\lambda $ for some $ 0\neq \lambda\in L_{k+1}^{2}(X,\mathbb{R}) $ . On the open subset of X where $ \lambda\neq0 $ , let $ \xi_{j}, j=1,2 $ , be $ L_{k+1}^{2} $ eigenvectors of $ \zeta $ such that $ \zeta(\xi_{j})=i\lambda_{j}\xi_{j} $ and $ \langle \xi_{j},\xi_{k}\rangle=\delta_{jk} $ . Just as in [30, p. 47], we find that $ \lambda $ is constant, the eigenvectors $ \xi_{j} $ are globally defined and $ d_{A}\xi_{j}=0 $ for $ j=1,2 $ . In particular, we have an orthogonal splitting $ E=L_{1}\oplus L_{2} $ where $ \xi_{j}\in L_{k+1}^{2}(X,E) $ is a section of $ L_{j} $ and $ d_{A}=d_{A_{1}}\oplus d_{A_{2}} $ with respect to this splitting, so this gives (5).

$$
0\not\equiv\zeta\in\mathrm{Ker}\{d_A:L_{k+1}^2\Omega^0(X,\mathfrak{s u}(E))\}
$$

$$
\zeta
$$

$$
i\lambda_{1},i\lambda_{2}=\pm i\lambda
$$

$$
0\not\equiv\lambda\in L_{k+1}^2(X,\mathbb{R})
$$

$$
\lambda\ne0
$$

$$
\xi_{j},j=1,2
$$

$$
L_{k+1}^{2}
$$

$$
\zeta
$$

$$
\zeta(\xi_{j})=i\lambda_{j}\xi_{j}
$$

$$
\langle\xi_{j},\xi_{k}\rangle=\delta_{jk}
$$

$$
\left[30,p.47\right]
$$

$$
d_{A}\xi_{j}=0
$$

$$
\xi_{j}
$$

$$
\lambda
$$

$$
E=L_{1}\oplus L_{2}.
$$

$$
j=1,2
$$

$$
\xi_{j}\in L_{k+1}^{2}(X,E)
$$

$$
d_{A}=d_{A_{1}}\oplus d_{A_{2}}
$$

$$
L_{j}
$$

(5) $ \Longrightarrow $ (6): Given (5), the connection A reduces to $ A_{1}\oplus A_{2} $ with respect to the splitting $ E=L_{1}\oplus L_{2} $ and so has stabilizer $ S_{L_{1}}^{1}\times S_{L_{2}}^{1}, $ where we identify the constant maps in $ \mathrm{Map}^{k+1}(X,S^{1}) $ with $ S_{L_{i}}^{1} $ for i=1,2. Since $ S_{L_{1}}^{1}\times S_{L_{2}}^{1}\simeq S^{1}\times S_{Z}^{1}, $ this gives (2).

$$
(5)\implies(6)
$$

$$
A_{1}\oplus A_{2}
$$

$$
E=L_{1}\oplus L_{2}
$$

$$
S_{L_{1}}^{1}\times S_{L_{2}}^{1},
$$

$$
\mathrm{Map}^{k+1}(X,S^1)
$$

$$
S_{L_{i}}^{1}
$$

$$
S_{L_{1}}^{1}\times S_{L_{2}}^{1}\simeq S^{1}\times S_{Z}^{1}
$$

(6) $ \implies $ (1): Given $ u\in\mathrm{Stab}_{A} $ and $ \pm(\det u)^{-1/2}u\in\mathrm{Stab}_{A^{\mathrm{ad}}}. $ （By Lemma 2.3 a constant map.) If $ u_{1}=\operatorname{id}_{\mathfrak{su}(E)} $ then we w $ u=\pm(\det u)^{1/2}u_{1}\in S_{Z}^{1}, $ so $ u_{1}\neq\operatorname{id}_{\mathfrak{su}(E)}. $ The and Lemma 2.4 implies that $ \mathrm{Stab}_{A^{\mathrm{ad}}}\simeq S^{1}. $

$ \notin S_{Z}^{1} $ , we obtain $ u_{1}= $ the determinant det u is should have $ u_{1}=\pm \mathrm{id}_{E} $ and before, $ \operatorname{Stab}_{A^{\mathrm{ad}}}\supset\left\{\mathrm{id}_{\mathfrak{su}(E)}\right\} $

$$
\begin{array}{ccc}\left(6\right)&\Longrightarrow&\left(1\right)\\\end{array}
$$

$$
u\in\mathrm{Stab}_{A}
$$

$$
u_{1}=
\notin S_{Z}^{1}
$$

$$
\pm(\det u)^{-1/2}u\in\mathrm{Stab}_{A^{\mathrm{ad}}}
$$

$$
u_{1}=\mathrm{id}_{\mathfrak{s u}(E)}
$$

$$
u_{1}=\pm\mathrm{id}_{E}
$$

$$
u=\pm(\det u)^{1/2}u_{1}\in S_{Z}^{1}
$$

$$
u_{1}\neq\mathrm{id}_{\mathfrak{s u}(E)}
$$

$$
\mathrm{Stab}_{A^{\mathrm{ad}}}\supsetneq\{\mathrm{id}_{\mathfrak{s u}(E)}\}
$$

$$
\mathrm{Stab}_{A^{\mathrm{ad}}}\simeq S^{1}
$$

Lastly, A is projectively flat if $ \mathrm{Stab}_{A^{\mathrm{ad}}}=\mathrm{SO}(3) $ (by Lemma 2.4) and $ \mathrm{Stab}_{A^{\mathrm{ad}}}=\mathrm{SO}(3)\simeq\mathrm{U}(2)/S_{Z}^{1} $ if and only if $ \mathrm{Stab}_{A}=\mathrm{U}(2). $ q.e.d.

$$
\mathrm{_{A^{ad}}=SO(3)}
$$

$$
\mathrm{Stab}_{A^{\mathrm{ad}}}=\mathrm{SO}(3)\simeq\mathrm{U}(2)/S_{Z}^{1}
$$

$$
_A=\mathrm{U}(2)
$$

The equivalence of (1) and (2) above noting that $ H_{A^{\mathrm{ad}}}^{0}\simeq i\mathbb{R} $ if and only if $ H_{A}^{0}\simeq $ if and only if $ \operatorname{Stab}_{A}\simeq S^{1}\times S_{Z}^{1}. $

an alternatively be seen by $ i\mathbb{R}\oplus i\mathbb{R}_{Z} $ , so $ \mathrm{Stab}_{A^{\mathrm{ad}}}\simeq S^{1} $

$$
H^{0}_{A^{ad}}\simeq
$$

$$
H_{A}^{0}\simeq i\mathbb{R}\oplus i\mathbb{R}_{Z}
$$

$$
\mathrm{Stab}_{A^{\mathrm{ad}}}\simeq S^{1}
$$

$$
\hat{\mathrm{Stab}}_{A}\simeq S^{1}\times S^{1}_{Z}
$$

From Lemmas 2.4 and 2.6 we see that A is an irreducible U(2) connection if and only if $ A^{\mathrm{ad}} $ is an irreducible SO(3) connection. Note that $ \mathrm{Stab}_{A,\Phi}=\mathrm{Stab}_{A}\cap\mathrm{Stab}_{\Phi}. $ The stabilizer $ \mathrm{Stab}_{A,\Phi} $ of a zero-section pair (A, $ \Phi $ ) contains $ S_{Z}^{1}. $ The stabilizer $ \mathrm{Stab}_{A,\Phi} $ of a reducible pair (A, $ \Phi $ ） need not contain the stabilizer $ \mathrm{Stab}_{A} $ since $ \mathrm{Stab}_{A} $ may not fix $ \Phi. $

$$
A^{\mathrm{ad}}
$$

$$
\mathrm{Stab}_{\underline{A},\underline{\Phi}}=\mathrm{Stab}_{\underline{A}}\cap\mathrm{Stab}_{\underline{\Phi}}
$$

$$
\mathrm{Stab}_{A,\Phi}
$$

$$
S_{Z}^{1}
$$

$$
A{,}\Phi
$$

$$
\mathrm{Stab}_{A}
$$

We write $ \tilde{\mathcal{C}}_{W,E}^{*} $ (respectively, $ \tilde{\mathcal{C}}_{W,E}^{0} $ ) for the complement of the reducible pairs (respectively, zero section pairs) in $ \tilde{\mathcal{C}}_{W,E} $ , and let $ \tilde{\mathcal{C}}_{W,E}^{*,0}=\tilde{\mathcal{C}}_{W,E}^{*}\cap\tilde{\mathcal{C}}_{W,E}^{0}. $ The quotients $ \mathcal{C}_{W,E}^{*} $ $ \mathcal{C}_{W,E}^{0} $ , and $ \mathcal{C}_{W,E}^{*,0} $ are similarly defined. If $ (A,\Phi)\in\tilde{\mathcal{C}}_{W,E}^{*,0} $ , then $ \mathrm{Stab}_{A,\Phi}=\{\mathrm{id}_{E}\} $ , as the stabilizer of an irreducible connection A will be $ S_{Z}^{1} $ and if $ S_{Z}^{1} $ stabilizes the section $ \Phi $

$$
\tilde{\mathcal{C}}_{W,E}^*
$$

$$
\tilde{\mathcal{C}}_{W,E}^{0})
$$

$$
\tilde{\mathcal{C}}_{W,E},
$$

$$
\tilde{\mathcal{C}}_{W,E}^{*}\cap\tilde{\mathcal{C}}_{W,E}^{0}
$$

$$
\tilde{\mathcal{C}}_{W,E}^{*,0}=
\mathcal{C}_{W,E}^{*},\mathcal{C}_{W,E}^{0}
$$

$$
\mathcal{C}_{W,E}^{*,0}
$$

$$
(A,\Phi)\;\in\;\tilde{\mathcal{C}}_{W,E}^{*,0}.
$$

$$
\cdot_{A,\Phi}\;=\;\{\mathrm{id}_E\}
$$

$$
S_{Z}^{1}
$$

$$
S_{Z}^{1}
$$ then $e^{i\theta}\Phi = 0$ for all $\theta \in \mathbb{R}$ and so $\Phi \equiv 0 \in L_k^2(X, W^+ \otimes E)$ (note that $\Phi$ need not be continuous). Therefore, $^\circ G_E$ acts freely on $\tilde{C}_{W,E}^*, 0$ and, as we shall see in the next section, the quotient $C_{W,E}^*$, is a Banach manifold. Conversely, if $(A, \Phi)$ is a PU(2) monopole, $A$ is reducible, and $\Phi \neq 0$, then Lemma 5.22 implies that Stab$_{A,\Phi} \simeq S^1$.

2.2. A slice for the action of the group of gauge transformations. Let $k \geq 2$ be an integer. The slice $S_{A,\Phi} \subset \tilde{C}_{W,E}$ through a pair $(A, \Phi)$ is given by $S_{A,\Phi} := (A, \Phi) + K_{A,\Phi}$, where

(2.7) $K_{A,\Phi} := \text{Ker } d_{A,\Phi}^{0,*} \subset L_k^2(\Lambda^1 \otimes \mathfrak{su}(E)) \oplus L_k^2(W^+ \otimes E)$.

If $\pi$ is the projection from $\tilde{C}_{W,E}$ onto $C_{W,E} = \tilde{C}_{W,E}/^\circ G_E$, denoted by $(A, \Phi) \mapsto [A, \Phi]$, we let

$$B_{A,\Phi}(\varepsilon) = \pi^{-1} B_{A,\Phi}(\varepsilon) \cap S_{A,\Phi}$$

be the open $L_k^2$ ball in $S_{A,\Phi}$ with center $(A, \Phi)$ and radius $\varepsilon$, so that

$$B_{A,\Phi}(\varepsilon) := \{(A_1, \Phi_1) \in S_{A,\Phi}: \|(A_1, \Phi_1) - (A, \Phi)\|_{L_k^2,A} < \varepsilon\}$$

$$= (A, \Phi) + \{(a, \phi) \in K_{A,\Phi}: \|(a, \phi)\|_{L_k^2,A} < \varepsilon\}.$$

The Hilbert Lie group $^\circ G_E$ has Lie algebra

$$L_k^2(k+1)(\mathfrak{su}(E)) \oplus i\mathbb{R}_Z \subset L_k^2(k+1)(\mathfrak{su}(E))$$

and exponential map exp : $L_k^2(k+1)(\mathfrak{su}(E)) \oplus i\mathbb{R}_Z \to^\circ G_E$ given by $\zeta \mapsto u = \exp \zeta$. Let

$$\text{Stab}_{A,\Phi}^{\perp} := \exp((\text{Ker } d_{A,\Phi}^0)^{\perp}) \subset^\circ G_E,$$

where

$$
(\text{Ker}(d_{A,\Phi}^0|_{L_k^2+1}))^{\perp} = \text{Im}(d_{A,\Phi}^0|_{L_k^2+2}) \subset L_k^2(k+1)(\mathfrak{su}(E)),
$$

noting that

$$d_{A,\Phi}^* : L_k^2(k+2)\Omega^1(\mathfrak{su}(E)) \rightarrow L_k^2(k+1)(\mathfrak{su}(E)) \oplus L_k^2(W^+ \otimes E)$$

has closed range. Recall that Stab$_{A,\Phi} \subset^\circ G_E$ is given by

$$\{\gamma \in^\circ G_E : \gamma(A, \Phi) = (A, \Phi)\}$$

and has Lie algebra

$$H_{A,\Phi}^0 = \text{Ker}(d_{A,\Phi}^0|_{L_k^2+1}) \subset L_k^2(k+1)(\mathfrak{su}(E)) \oplus i\mathbb{R}_Z,$$ so that

(2.8) $L_{k+1}^2(\mathfrak{su}(E)) \oplus i\mathbb{R}_Z = (\text{Ker}(d^0_{A,\Phi}|_{L_{k+1}^2}))^\perp \oplus H^0_{A,\Phi}$.

The subspace $\text{Stab}_{A,\Phi}^{\perp} \subset {}^\circ\mathcal{G}_E$ is closed and is a Banach submanifold of ${}^\circ\mathcal{G}_E$ with codimension $H^0_{A,\Phi}$.

The map $d^0_{A,\Phi}: L_{k+1}^2(\mathfrak{su}(E)) \oplus i\mathbb{R}_Z \rightarrow L_k^2(\Lambda^1 \otimes \mathfrak{su}(E)) \oplus L_k^2(W^+ \otimes E)$ has closed range and so we have an $L^2$-orthogonal decomposition

(2.9) $T_{A,\Phi}\tilde{\mathcal{C}}_{W,E} = \text{Im}(d^0_{A,\Phi}|_{L_{k+1}^2}) \oplus \mathbf{K}_{A,\Phi}$

of the tangent space to the space of $L_k^2$ pairs at the point $(A, \Phi)$.

The proof that the quotient space $\mathcal{C}_{W,E}$ is Hausdorff and our later proof of removable singularities for PU(2) monopoles make use of the following well-known technical result [20, Proposition 2.3.15], [30, Proposition A.5], [56, Theorem II.7.11]. Note that the space of $L_k^2$ unitary automorphisms of $E$ is neither a Hilbert Lie group nor does it act smoothly on the space of $L_k^2$ unitary connections on $E$.

**Lemma 2.7.** Let $E$ be a Hermitian bundle over a Riemannian manifold $X$ and let $k \geq 2$ be an integer. Suppose that $\{A_\alpha\}$ and $\{B_\alpha\}$ are sequences of $L_k^2$ unitary connections on $E$, and that $\{u_\alpha\}$ is a sequence of unitary automorphisms of $E$ such that $u_\alpha(A_\alpha) = B_\alpha$. Then the following hold.

(1) The sequence $\{u_\alpha\}$ is in $L_k^2$.

(2) If $\{A_\alpha\}$ and $\{B_\alpha\}$ converge in $L_k^2$ to limits $A_\infty$, $B_\infty$, then there is a subsequence $\{\alpha'\} \subset \{\alpha\}$ such that $\{u_{\alpha'}\}$ converges in $L_k^2$ to $u_\infty$ and $B_\infty = u_\infty(A_\infty)$.

The following slice result was established by Parker [70], but only for pairs which are neither zero-section nor reducible; see also [9]. It is, of course, the analogue of the usual result for the topology and manifold structure of the configuration space $\mathcal{B}_E = A_E/G_E$ of connections. The proof we give here is modelled on the corresponding arguments for connections given in [20, Proposition 2.3.4], [30, Theorems 3.2 & 4.4], and [56, Theorem II.10.4]. We will ultimately need a rather more involved version of this method in order to show that our gluing maps are diffeomorphisms, so we give the argument in the simpler model case below in some detail and establish some of the notation and conventions we will later require.

---

Proposition 2.8. Let X be a closed, oriented, Riemannian spin$^c$
four-manifold, let E be a Hermitian two-plane bundle over X, and let k ≥ 2 be an integer. Then the following hold.

(1) The space $C_{W,E}$ is Hausdorff.

(2) The subspace $C^{*,0}_{W,E} \subset C_{W,E}$ is open and is a $C^\infty$ Hilbert manifold with local parametrizations given by $\pi : B_{A_0,\Phi_0}(\varepsilon) \rightarrow C^{*,0}_{W,E}$ for sufficiently small $\varepsilon = \varepsilon(A_0,\Phi_0,k)$.

(3) The projection $\pi : \tilde{C}^{*,0}_{W,E} \rightarrow C^{*,0}_{W,E}$ is a $C^\infty$ principal $^\circ G_E$ bundle.

(4) For $(A_0,\Phi_0) \in \tilde{C}_{W,E}$, the projection $\pi : B_{A_0,\Phi_0}(\varepsilon)/\text{Stab}_{A_0,\Phi_0} \rightarrow C_{W,E}$ is a homeomorphism onto an open neighborhood of $[A_0,\Phi_0] \in C_{W,E}$ and a diffeomorphism on the complement of the set of points in $B_{A_0,\Phi_0}(\varepsilon)$ with non-trivial stabilizer.

Proof. The stabilizer $\text{Stab}_{A_0,\Phi_0}$ (which we can identify with a Lie subgroup of U(2)) acts freely on $^\circ G_E$ and thus on the Hilbert manifold $^\circ G_E \times S_{A_0,\Phi_0}$ by $(u,A,\Phi) \mapsto \gamma \cdot (u,A,\Phi) = (u\gamma^{-1},\gamma(A,\Phi))$, and so the quotient $^\circ G_E \times_{\text{Stab}_{A_0,\Phi_0}} S_{A_0,\Phi_0}$ is again a Hilbert manifold. We define a smooth map

$$\Psi : ^\circ G_E \times_{\text{Stab}_{A_0,\Phi_0}} S_{A_0,\Phi_0} \rightarrow \tilde{C}_{W,E}, \quad [u,A,\Phi] \mapsto u(A,\Phi).$$

Our first task is to show that the map $\Psi$ is a diffeomorphism onto its image upon restriction to a sufficiently small neighborhood $^\circ G_E \times_{\text{Stab}_{A_0,\Phi_0}} B_{A_0,\Phi_0}(\varepsilon)$. Given $\delta > 0$, let $B_{\text{id}}(\delta)$ be the ball

$$\{u \in ^\circ G_E : \|u - \text{id}_E\|_{L^{2}_{k+1},A_0} < \delta\},$$

and let $B_{\text{id}}^{\perp}(\delta) = B_{\text{id}}(\delta) \cap \text{Stab}_{A_0,\Phi_0}^{\perp}$.

Claim 2.9. For small enough $\delta = \delta(A_0,\Phi_0,k)$, the ball $B_{\text{id}}(\delta)$ is diffeomorphic to an open neighborhood in $B_{\text{id}}^{\perp}(\delta) \times \text{Stab}_{A_0,\Phi_0}$, with inverse map given by $(u_0,\gamma) \mapsto u = u_0\gamma$.

Proof. The differential of the multiplication map

$$\text{Stab}_{A_0,\Phi_0} \times \text{Stab}_{A_0,\Phi_0} \rightarrow ^\circ G_E, \quad (u_0,\gamma) \mapsto u_0\gamma$$

at $(\text{id}_E,\text{id}_E)$ is given by

$$\text{Ker}(d^0_{A_0,\Phi_0}|_{L^{2}_{k+1}})^{\perp} \oplus H^0_{A_0,\Phi_0} \rightarrow L^{2}_{k+1}(\mathfrak{su}(E)) \quad (\zeta,\chi) \mapsto \zeta + \chi,$$ and is just the identity map with respect to the $L^2$-orthogonal decomposition (2.8) of the range. Hence, the Hilbert space implicit function theorem implies that there is a diffeomorphism from an open neighborhood of $(\text{id}_E, \text{id}_E)$ onto an open neighborhood of $\text{id}_E \in \circ G_E$. For small enough $\delta$, we may suppose that if $u \in B_{\text{id}}(\delta)$, then $u$ can be written uniquely as $u = u_0 \gamma$ with $u_0 \in B_{\text{id}}^\perp(\delta)$ and $\gamma \in \text{Stab}_{A_0,\Phi_0}$. q.e.d.

Claim 2.10. For small enough $\varepsilon = \varepsilon(A_0, \Phi_0, k)$, the map $\Psi$ is a diffeomorphism from $\circ G_E \times_{\text{Stab}_{A_0,\Phi_0}} \mathbf{B}_{A_0,\Phi_0}(\varepsilon)$ onto its image in $\tilde{\mathcal{C}}_{W,E}$.

Proof. We first restrict the map $\Psi$ to a neighborhood $B_{\text{id}}(\delta) \times_{\text{Stab}_{A_0,\Phi_0}} \mathbf{S}_{A_0,\Phi_0}$, which is diffeomorphic to the neighborhood $B_{\text{id}}^\perp(\delta) \times_{\mathbf{S}_{A_0,\Phi_0}} \text{Stab}_{\perp A_0,\Phi_0} \times_{\mathbf{S}_{A_0,\Phi_0}}$ by Claim 2.9. The differential of the induced map

$$\Psi : \text{Stab}_{\perp A_0,\Phi_0} \times_{\mathbf{S}_{A_0,\Phi_0}} \to \tilde{\mathcal{C}}_{W,E}, \quad (u, A, \Phi) \mapsto u(A, \Phi)$$

at $(\text{id}_E, A_0, \Phi_0)$ is given by

$$(D\Psi)_{(\text{id}, A_0, \Phi_0)} : T_{\text{id}} \text{Stab}_{\perp A_0,\Phi_0} \oplus T_{A_0,\Phi_0} \mathbf{S}_{A_0,\Phi_0} \to T_{A_0,\Phi_0} \tilde{\mathcal{C}}_{W,E},$$

$$(\zeta, a, \phi) \mapsto -d_{A_0,\Phi_0}^0 \zeta + (a, \phi),$$

where we recall that $T_{A_0,\Phi_0} \mathbf{S}_{A_0,\Phi_0} = \mathbf{K}_{A_0,\Phi_0}$ and

$$T_{\text{id}} \text{Stab}_{\perp A_0,\Phi_0} = (\text{Ker}(d_{A_0,\Phi_0}^0|_{L_{k+1}^2}))^\perp = \text{Im}(d_{A_0,\Phi_0}^0|_{L_{k+2}^2}).$$

Using the $L^2$-orthogonal decomposition (2.9) of the range we see that the map

$$-d_{A_0,\Phi_0}^0 \oplus \text{id}_E : (\text{Ker}(d_{A_0,\Phi_0}^0|_{L_{k+1}^2}))^\perp \oplus \mathbf{K}_{A_0,\Phi_0} \to \text{Im}(d_{A_0,\Phi_0}^0|_{L_{k+2}^2}) \oplus \mathbf{K}_{A_0,\Phi_0}$$

given by $(\zeta, b, \psi) \mapsto -d_{A_0,\Phi_0}^0 \zeta + (b, \psi)$ is a Hilbert space isomorphism. So, by the Hilbert space implicit function theorem, there are positive constants $\varepsilon = \varepsilon(A_0, \Phi_0, k)$ and $\delta = \delta(A_0, \Phi_0, k)$ and an open neighborhood $\mathcal{U}_{A_0,\Phi_0} \subset \tilde{\mathcal{C}}_{W,E}$ such that the map

$$\Psi : B_{\text{id}}^\perp(\delta) \times \mathbf{B}_{A_0,\Phi_0}(\varepsilon) \to \mathcal{U}_{A_0,\Phi_0}, \quad (u, A, \Phi) \mapsto u(A, \Phi)$$

gives a diffeomorphism from an open neighborhood of $(\text{id}_E, A_0, \Phi_0)$ onto an open neighborhood of $(A_0, \Phi_0)$. In particular, we obtain a map $\mathcal{U}_{A_0,\Phi_0} \to \text{Stab}_{\perp A_0,\Phi_0}$, given by $(A, \Phi) \mapsto u = u_A,\Phi$, such that

$$\Psi^{-1}(A, \Phi) = \left( u, u^{-1}(A, \Phi) \right) \in B_{\text{id}}^\perp(\delta) \times \mathbf{B}_{A_0,\Phi_0}(\varepsilon)$$

$$\subset \text{Stab}_{\perp A_0,\Phi_0} \times \mathbf{B}_{A_0,\Phi_0}(\varepsilon).$$

---

Hence, for any $(A, \Phi) \in \mathcal{U}_{A_0,\Phi_0}$ there is a unique $u \in B_{\text{id}}^{\perp}(\delta)$ such that $u^{-1}(A, \Phi) - (A_0, \Phi_0) \in \mathbf{K}_{A_0,\Phi_0}$:

(2.10) $d_{A_0,\Phi_0}^{0,*} (u^{-1}(A_1, \Phi_1) - (A_0, \Phi_0)) = 0$.

The neighborhood $\mathbf{B}_{A_0,\Phi_0}(\varepsilon)$ is Stab$_{A_0,\Phi_0}$-invariant: if $(A, \Phi) \in \mathbf{B}_{A_0,\Phi_0}(\varepsilon)$ and $\gamma \in \text{Stab}_{A_0,\Phi_0}$, then

$$\|\gamma(A_1, \Phi_1) - (A, \Phi)\|_{L^2_k,A_0} = \|(A_1, \Phi_1) - \gamma^{-1}(A, \Phi)\|_{L^2_k,\gamma^{-1}(A_0)}$$

$$= \|(A_1, \Phi_1) - (A, \Phi)\|_{L^2_k,A_0} < \varepsilon,

and

$$d_{A_0,\Phi_0}^{0,*} (\gamma(A, \Phi) - (A_0, \Phi_0)) = \gamma \left(d_{\gamma^{-1}(A_0,\Phi_0)}^{0,*} ((A, \Phi) - (A_0, \Phi_0))\right)$$

$$= \gamma \left(d_{A_0,\Phi_0}^{0,*} ((A, \Phi) - (A_0, \Phi_0))\right) = 0,

so $\gamma(A, \Phi) \in \mathbf{B}_{A_0,\Phi_0}(\varepsilon)$.

The group $^\circ G_E$ acts on $^\circ G_E \times \mathbf{S}_{A_0,\Phi_0}$ by $(u, A, \Phi) \mapsto (vu, A, \Phi)$, and so gives a diffeomorphism

$$B_{\text{id}}(\delta) \times \mathbf{B}_{A_0,\Phi_0}(\varepsilon) \to B_v(\delta) \times \mathbf{B}_{A_0,\Phi_0}(\varepsilon), \quad (u, A, \Phi) \mapsto (vu, A, \Phi),

and as this action commutes with the given action of Stab$_{A_0,\Phi_0}$, it descends to a diffeomorphism

$$B_{\text{id}}(\delta) \times_{\text{Stab}_{A_0,\Phi_0}} \mathbf{B}_{A_0,\Phi_0}(\varepsilon) \to B_v(\delta) \times_{\text{Stab}_{A_0,\Phi_0}} \mathbf{B}_{A_0,\Phi_0}(\varepsilon),$$

$$[u, A, \Phi] \mapsto [vu, A, \Phi],$$

for each $v \in^\circ G_E$. Consequently, the $^\circ G_E$-equivariant map

$$^\circ G_E \times_{\text{Stab}_{A_0,\Phi_0}} \mathbf{B}_{A_0,\Phi_0}(\varepsilon) \to \tilde{\mathcal{C}}_{W,E}

is a diffeomorphism onto its image, as desired. q.e.d.

Plainly, $[\gamma(A, \Phi)] = [A, \Phi]$ for each $\gamma \in \text{Stab}_{A_0,\Phi_0}$ and $(A, \Phi) \in \mathbf{B}_{A_0,\Phi_0}(\varepsilon)$ and hence, the projection $\pi : \mathbf{B}_{A_0,\Phi_0}(\varepsilon) \to \mathcal{C}_{W,E}$ factors through $\mathbf{B}_{A_0,\Phi_0}(\varepsilon)/\text{Stab}_{A_0,\Phi_0}$.

Claim 2.11. There is a positive constant $\delta = \delta(A_0, \Phi_0, k)$ with the following significance. If $(A_i, \Phi_i) \in \mathbf{B}_{A_0,\Phi_0}(\varepsilon)$ for $i = 1, 2$ and there is a gauge transformation $u \in B_{\text{id}}(\delta)$ such that $u(A_1, \Phi_1) = (A_2, \Phi_2)$, then $u \in \text{Stab}_{A_0,\Phi_0}$.

---

Proof. For small enough $\delta$, Claim 2.9 implies that $u \in B_{\text{id}}(\delta)$ can be written uniquely as $u = u_1\gamma$ with $u_1 \in B_{\text{id}}^{\perp}(\delta)$ and $\gamma \in \text{Stab}_{A_0,\Phi_0}$. Thus, $(A_2,\Phi_2) = u_1\gamma(A_1,\Phi_1) \in \mathbf{B}_{A_0,\Phi_0}(\varepsilon)$. But the neighborhood $\mathbf{B}_{A_0,\Phi_0}(\varepsilon)$ is $\text{Stab}_{A_0,\Phi_0}$-invariant, so we also have $\gamma(A_1,\Phi_1) \in \mathbf{B}_{A_0,\Phi_0}(\varepsilon)$. Therefore $u_1 = \text{id}_E$ by the uniqueness assertion of Claim 2.9 and so $u = \gamma \in \text{Stab}_{A_0,\Phi_0}$. This completes the proof of the claim. q.e.d.

Claim 2.11 shows that $\mathbf{B}_{A_0,\Phi_0}(\varepsilon)/\text{Stab}_{A_0,\Phi_0}$ injects into the quotient $\mathcal{C}_{W,E}$ modulo the assumption that the gauge transformations are close to $\text{id}_E$. It remains to show that if $(A_i,\Phi_i) \in \mathbf{B}_{A_0,\Phi_0}(\varepsilon)$ for $i=1,2$ and there is a gauge transformation $u \in \circ^\circ G_E$ such that $u(A_1,\Phi_1) = (A_2,\Phi_2)$, then $u$ is necessarily close to $\text{id}_E$ and hence that $\mathbf{B}_{A_0,\Phi_0}(\varepsilon)/\text{Stab}_{A_0,\Phi_0}$ injects into the quotient $\mathcal{C}_{W,E}$.

Claim 2.12. For small enough $\varepsilon(A_0,\Phi_0)$, the projection

$$\pi : \mathbf{B}_{A_0,\Phi_0}(\varepsilon)/\text{Stab}_{A_0,\Phi_0} \rightarrow \mathcal{C}_{W,E}$$

is injective.