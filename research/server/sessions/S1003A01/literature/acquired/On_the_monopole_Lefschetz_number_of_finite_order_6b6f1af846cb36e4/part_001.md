---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: On the monopole Lefschetz number of finite order ...]

---
source_file: 2004_05497v3.pdf
converter: mathpix
format: mmd
---

\title{
ON THE MONOPOLE LEFSCHETZ NUMBER OF FINITE ORDER DIFFEOMORPHISMS
}

\author{
JIANFENG LIN, DANIEL RUBERMAN, AND NIKOLAI SAVELIEV
}

\begin{abstract}
Let $K$ be a knot in an integral homology 3-sphere $Y$, and $\Sigma$ the corresponding $n$-fold cyclic branched cover. Assuming that $\Sigma$ is a rational homology sphere (which is always the case when $n$ is a prime power), we give a formula for the Lefschetz number of the action that the covering translation induces on the reduced monopole homology of $\Sigma$. The proof relies on a careful analysis of the Seiberg-Witten equations on 3-orbifolds and of various $\eta$-invariants. We give several applications of our formula: (1) we calculate the Seiberg-Witten and Furuta-Ohta invariants for the mapping tori of all semi-free actions of $\mathbb{Z} / n$ on integral homology 3-spheres; (2) we give a novel obstruction (in terms of the Jones polynomial) for the branched cover of a knot in $S^{3}$ being an $L$-space; (3) we give a new set of knot concordance invariants in terms of the monopole Lefschetz numbers of covering translations on the branched covers.
\end{abstract}

\section*{1. Introduction}

Monopole Floer homology, as defined by Kronheimer and Mrowka [22] and Frøyshov [17], is a powerful invariant of 3-manifolds. Orientation preserving self-diffeomorphisms of the 3-manifold act on the monopole Floer homology. We initiated a study of this action in [33], where we calculated the monopole Lefschetz number of an involution on a rational homology 3-sphere that makes it into a double branched cover over a link in the 3-sphere. In this paper we continue this study and extend our calculations to all finite order diffeomorphisms making a rational homology 3-sphere into a branched cover of a knot in an integral homology 3-sphere. Note that the case of free diffeomorphisms of finite order was dealt with in [43].

\footnotetext{
2010 Mathematics Subject Classification. 57R57, 57R58, 57K10, 57K31, 57K41.
The first author was partially supported by the NSF Grant DMS-1707857, the second author was partially supported by NSF Grant DMS-1811111 and a Simons Fellowship, and the third author was partially supported by Collaboration Grant \# 426269 from the Simons Foundation.
}

Given a knot $K$ in an integral homology 3-sphere $Y$ and an integer $n \geqslant 2$, consider the $n$-fold cyclic branched cover $\Sigma \rightarrow Y$ with branch set $K$ and denote by $\tau: \Sigma \rightarrow \Sigma$ the covering translation. Assume that $\Sigma$ is a rational homology 3-sphere (which is always true when $n$ is a prime power). Observe that $\Sigma$ admits a unique spin ${ }^{c}$ structure $\mathfrak{s}$ such that $\tau_{*}(\mathfrak{s})=\mathfrak{s}$, and that this spin ${ }^{c}$ structure is actually a spin structure; see Remark 6.3. Our main theorem can now be stated as follows.

Theorem A. Let $\tau_{*}: H M^{\mathrm{red}}(\Sigma, \mathfrak{s}) \rightarrow H M^{\mathrm{red}}(\Sigma, \mathfrak{s})$ be the map in the reduced monopole Floer homology induced by the covering translation $\tau$. Then
$$\operatorname{Lef}\left(\tau_{*}\right)=n \cdot \lambda(Y)+\frac{1}{8} \cdot \sum_{m=1}^{n-1} \operatorname{sign}_{m / n}(K)-h(\Sigma, \mathfrak{s}),$$
where $\lambda(Y)$ is the Casson invariant of $Y, \operatorname{sign}_{m / n}(K)$ are the Tristram-Levine signatures of $K$, and $h(\Sigma, \mathfrak{s})$ is the Frøyshov invariant.

The formula (1) was first conjectured in [33] but its proof here will use methods completely different from those in [33]: we will first calculate the Seiberg-Witten invariant $\lambda_{\mathrm{SW}}(X)$ for the mapping torus $X$ of $\tau$ using the original definition of $\lambda_{\mathrm{SW}}(X)$ from [39], and then apply the splitting theorem of [32] to derive (1).

Theorem B. Let $\Sigma$ be a rational homology sphere as above and $X$ the mapping torus of the covering translation $\tau: \Sigma \rightarrow \Sigma$ with the standard orientation and homology orientation. Then
$$-\lambda_{\mathrm{SW}}(X)=n \cdot \lambda(Y)+\frac{1}{8} \cdot \sum_{m=1}^{n-1} \operatorname{sign}_{m / n}(K) .$$

We should mention that formula (2) was independently proved by Langte Ma [34] using a different set of techniques. His result actually holds without the assumption that $\Sigma$ is a rational homology sphere.
1.1. Motivation. As in our previous work, the research in this paper is motivated by a conjectural relationship between two gauge theoretic invariants of homology $S^{1} \times S^{3} \mathrm{~s}$, one from the Donaldson theory and the other from the Seiberg-Witten theory. In this section, we discuss our motivation and provide some further implications.
1.1.1. The Witten-style conjecture for finite-order mapping tori. Recall that classical gauge theoretic invariants of a smooth closed oriented 4-manifold $X$ (the Seiberg-Witten invariants and the Donaldson polynomial invariants) are only defined when $X$ satisfies the condition $b_{2}^{+}(X) \geqslant 1$. However, with suitable modifications, some of these invariants can be defined for other 4-manifolds. In particular, let $X$ be a smooth closed oriented 4-manifold such that
$$H_{*}(X ; \mathbb{Z})=H_{*}\left(S^{1} \times S^{3} ; \mathbb{Z}\right) \quad \text { and } \quad H_{*}(\tilde{X} ; \mathbb{Q})=H_{*}\left(S^{3} ; \mathbb{Q}\right),$$
where $\tilde{X}$ is the universal abelian cover of $X$. Then there are two gauge theoretic invariants for $X$. The first one is the invariant $\lambda_{\mathrm{SW}}(X)$ we mentioned earlier. It was defined in [39] by counting Seiberg-Witten monopoles on $X$ and modifying this count by an index-theoretic correction term. The second invariant, called $\lambda_{\mathrm{FO}}(X)$, was defined by Furuta and Ohta [18] as one quarter times the degree zero Donaldson polynomial of $X$. Furuta and Ohta used somewhat more restrictive hypotheses on $X$; we extended their definition to all manifolds $X$ satisfying (3) in our paper [33].

Conjecture C ([39, 33]). For any X satisfying (3), the following equality holds
$$\lambda_{\mathrm{SW}}(X)=-\lambda_{\mathrm{FO}}(X) .$$
Note that Conjecture C relates a Seiberg-Witten type invariant to a Donaldson type invariant. Therefore, it can be thought of as a Witten-style conjecture [49] for homology $S^{1} \times S^{3} \mathrm{~s}$.

The main results of this paper are inspired by Conjecture C for finite order mapping tori, and we confirm this conjecture for the mapping tori of Theorem B. More precisely, we have the following theorem.

Theorem D. Let $\Sigma$ be a rational homology sphere which is a cyclic branched cover of an integral homology sphere, with branch set a knot. Let $X$ be the mapping torus of the covering transformation $\tau: \Sigma \rightarrow \Sigma$. Then $X$ satisfies (3) and we have
$$\lambda_{\mathrm{SW}}(X)=-\lambda_{\mathrm{FO}}(X) .$$
Note that, in their previous work [43], the second and third authors verified Conjecture C for the mapping tori of all finite order diffeomorphisms $\tau: \Sigma \rightarrow \Sigma$ of integral homology spheres that generate a free group action on $\Sigma$.

Corollary E. Let $\Sigma$ be an integral homology sphere and $\tau: \Sigma \rightarrow \Sigma$ an orientation preserving diffeomorphism of order $n$ generating a semi-free action of $\mathbb{Z} / n$ on $\Sigma$. If $X$ is the mapping torus of $\tau$ then $\lambda_{\mathrm{SW}}(X)=-\lambda_{\mathrm{FO}}(X)$.
1.1.2. Normalized Lefschetz number in monopole and instanton Floer homology. Theorem D has an intriguing Floer theoretic interpretation in terms of an expected comparison of the reduced monopole homology groups $H M_{*}^{\text {red }}(Y)$ of Kronheimer and Mrowka [22] with the reduced instanton homology groups $\widehat{\mathrm{HF}}_{*}(Y)$ of Frøyshov [16]. As an extension of Witten's conjecture [49] on closed 4-manifolds, such a comparison should also include the maps between the homology groups in question induced by cobordisms. For the product cobordism between integral homology spheres, this manifests itself in the known relationship between the Casson invariant and the Euler characteristic of the reduced homologies normalized by the respective $h$-invariants:
$$\begin{aligned}
\chi\left(H M^{\mathrm{red}}(\Sigma)\right)+h(\Sigma) & =\lambda(\Sigma), \\
\frac{1}{2} \chi(\widehat{\mathrm{HF}}(\Sigma))-h_{D}(\Sigma) & =\lambda(\Sigma),
\end{aligned}$$
where $h$ and $h_{D}$ are respectively the monopole and instanton Frøyshov invariants. Taking (4) as a model, let us define the normalized Lefschetz numbers of a homology cobordism $W$ from an integral homology sphere $\Sigma$ to itself to be
$$\begin{aligned}
& \text { Lef }\left(W_{*}: H M^{\text {red }}(\Sigma) \rightarrow H M^{\text {red }}(\Sigma)\right)+h(\Sigma) \quad \text { and } \\
& \frac{1}{2} \text { Lef }\left(W_{*}: \widehat{\mathrm{HF}}(\Sigma) \rightarrow \widehat{\mathrm{HF}}(\Sigma)\right)-h_{D}(\Sigma)
\end{aligned}$$
in the monopole and instanton cases, respectively. In the special case of an orientation preserving self-diffeomorphism $\tau: \Sigma \rightarrow \Sigma$, the normalized Lefschetz numbers of its mapping cylinder is referred to as the normalized Lefschetz numbers of $\tau$.

Corollary F. If $\Sigma$ is an integral homology sphere and $\tau: \Sigma \rightarrow \Sigma$ an orientation preserving diffeomorphism of order $n$ generating a semi-free action of $\mathbb{Z} / n$ on $\Sigma$, then the normalized monopole and instanton Lefschetz numbers of $\tau$ agree.

This can be seen as follows. Let $X$ be the homology $S^{1} \times S^{3}$ obtained by gluing up the two boundary components of $W$ via the identity map. Then the normalized monopole Lefschetz number of $W$ equals $-\lambda_{\mathrm{SW}}(X)$ by the splitting formula [32], and the normalized instanton Lefschetz number of $W$ equals $\lambda_{\mathrm{FO}}(X)$ by the
splitting formula of Anvari [1]. Comparing this with Corollary E completes the proof.

Note that for any 3-manifold, it is conjectured [23] that the sutured versions of monopole Floer homology and instanton Floer homology coincide. However, relations between all other versions remain mysterious. It is possible that Corollary F is a shadow of some deeper relation between these two theories.
1.2. Applications. Theorem A can be used to study knots in $S^{3}$ and smooth concordance between them. Given a knot $K \subset S^{3}$ and an integer $n>1$, we let $\Sigma_{n}(K)$ be the $n$-fold cyclic branched cover of $K$. Denote by $L_{n}(K)$ the Lefschetz number of the map $\tau_{*}: H M^{\text {red }}\left(\Sigma_{n}(K)\right) \rightarrow H M^{\text {red }}\left(\Sigma_{n}(K)\right)$ induced by the covering transformation $\tau$. Then we have the following corollary of Theorem A, which generalizes [33, Corollary F].

Corollary G. Let $n=p^{m}$ for $p$ a prime number. Then the integer $L_{n}(K)$ is an additive smooth concordance invariant.

Recall that a closed oriented 3-manifold $\Sigma$ is called an $L$-space if $H_{1}(\Sigma ; \mathbb{Q})=0$ and $H M^{\text {red }}(\Sigma ; \mathbb{Z})=0$. Recent work of Boileau, Boyer, and Gordon [5, 6] has focused attention on the question of which branched covers of knots are $L$-spaces. This is of interest in its own right but also as a test case for the $L$-space conjecture [7] equating the property of a rational homology sphere not being an $L$-space with the left-orderability of its fundamental group. Using $L_{n}(K)$, we can show that the property of a knot $K \subset S^{3}$ not having an $L$-space branched cover can sometimes hold for an entire concordance class of $K$.

Theorem H. Let $n=p^{m}$ for $p$ a prime number. There is a knot $K_{n}$ such that, for any knot $K$ that is smoothly concordant to $K_{n}$, its $n$-fold cyclic branched cover $\Sigma_{n}(K)$ is not an $L$-space.

In a further application in this vein, we give a systematic obstruction of branched covers being an $L$-space in terms of the Jones polynomial.

Theorem I. Let $K \subset S^{3}$ be a knot with $\operatorname{det}(K)=1$ and $J_{K}^{\prime}(-1) \neq 0$, where $J_{K}(t)$ is the Jones polynomial of $K$. Then, for any $m \geqslant 1$, the $2 m$-fold cyclic branched cover $\Sigma_{2 m}(K)$ is not an $L$-space.

There are, of course, plenty of examples of knots $K$ whose cyclic branched covers $\Sigma_{n}(K)$ are not $L$-spaces for all $n$. The novelty of our result is in that it produces
such examples in a systematic way. Note that $\Sigma_{2 m}(K)$ in the above theorem may fail to be an $L$-space simply because it is not a rational homology sphere. However, since $\operatorname{det}(K)=1$, the manifold $\Sigma_{2 m}(K)$ is an $m$-fold cyclic branched cover of the integral homology sphere $\Sigma_{2}(K)$ and so it is automatically a rational homology sphere whenever $m$ is a prime power.

Finally, recall the conjectural behavior [43, Remark 4.2] of the invariant $\lambda_{\mathrm{SW}}$ under orientation reversal.

Conjecture J. Let $X$ be a smooth spin rational homology $S^{1} \times S^{3}$ which is oriented and homology oriented, and denote by $-X$ the manifold $X$ with reversed orientation but the same homology orientation. Then $\lambda_{\mathrm{SW}}(-X)=-\lambda_{\mathrm{SW}}(X)$.

Note that proving this conjecture would provide an alternate route to the resolution of the triangulation conjecture [36]. We can verify Conjecture J in a special case.

Theorem K. Let $X$ be the mapping torus of an orientation preserving diffeomorphism (not necessarily of finite order) of a rational homology sphere. Then, for any choice of spin structure on $X$, we have
$$-\lambda_{\mathrm{SW}}(X)=\lambda_{\mathrm{SW}}(-X) .$$
Theorem K will actually follow from our splitting formula [32]. We decided to include Theorem K here because of its relevance to the main result of this paper, Theorem B.
1.3. An outline of the proof. We will first prove Theorem B by computing the invariant $\lambda_{\mathrm{SW}}(X)$ directly from its definition [39],
$$\lambda_{\mathrm{SW}}(X)=\# \mathcal{M}(X, g, \beta)+w(X, g, \beta),$$
where $g$ and $\beta$ are generic metric and perturbation, $\mathcal{M}(X, g, \beta)$ the Seiberg-Witten moduli space, and $w(X, g, \beta)$ an index theoretic correction term. In the special case of the mapping torus $X$ at hand, we have an orbifold circle bundle $\pi: X \rightarrow Y^{o}$, where $Y^{o}$ is the orbifold with the underlying space $Y$, the singular set $K$, and the cone angle $2 \pi / n$ along $K$. According to Baldridge [4], for the right choice of metrics and perturbations, the moduli space $\mathcal{M}(X, g, \beta)$ splits into a disjoint union of the orbifold Seiberg-Witten moduli spaces corresponding to all possible orbifold spin ${ }^{c}$ structures on $Y^{o}$. We relate these orbifold moduli spaces to the Seiberg-Witten moduli space on $Y$ in Section 2 using an argument reminiscent of the pillowcase
argument of Herald [20] in Donaldson's theory. The correction term $w(X, g, \beta)$ for the mapping torus $X$ is just a combination of the $\eta$-invariants of $Y$, which we calculate in Section 3 and Section 4 using surgery techniques and the splitting formula of Mazzeo and Melrose [37]. All of this gives us a formula for $\lambda_{\text {SW }}(X)$ in terms of certain invariants of $Y$. It is converted into (2) in Section 5 using the formula of Lim [31] for the Casson invariant in the Seiberg-Witten theory.

Theorem A follows easily from Theorem B using the splitting theorem of [32]. Theorem D is proved in Section 6. It can be viewed as a generalization of [45] to rational homology spheres, or as a generalization of [33, Theorem 7.1] to $n \geqslant 2$, and it is proved by essentially the same methods. Proofs for all of the applications are contained in Section 7.

Acknowledgments: We thank the organizers of the 2018 Conference on Gauge Theory at the University of Regensburg, where the broad outline of this project took shape. We thank Tye Lidman for pointing out the references [9, 15, 46] on Heegaard-Floer $L$-spaces.

\section*{2. Counting Seiberg-Witten monopoles}

Let $K \subset Y$ be a knot in an oriented integral homology 3-sphere. Denote by $Y^{o}$ the orbifold with the underlying space $Y$, the singular set $K$, and the cone angle $2 \pi / n$ along $K$. In this section, we study monopoles on $Y^{o}$ using the Seiberg-Witten theory on manifolds with product ends. For the latter, we follow closely the exposition in Lim [30, 31].
2.1. Monopoles on product end manifods. Let $D(K)$ be a tubular neighborhood of $K \subset Y$ and $N=Y-\operatorname{Int}(D(K))$ the knot exterior, which is a compact 3-manifold with boundary a 2-torus $T$. Associate with $N$ the product end manifold
$$N^{*}=N \cup_{T}([0, \infty) \times T) .$$
Fix a metric $g(N)$ on $N$ that restricts to a flat metric on the boundary and is a product metric in its collar neighborhood. This metric extends in an obvious fashion to a product end metric on the manifold $N^{*}$.

The manifold $Y$ has a unique spin structure. It restricts to a spin structure on $N$, which in turn extends to a spin structure on $N^{*}$ with spinor bundle $E$. Let $A$ be a unitary connection in the determinant bundle of $E$, and $\varphi$ a spinor on $N^{*}$.

Let us consider the $(\omega, \alpha)$-perturbed Seiberg-Witten equations
$$F_{A}+\omega=\tau(\varphi), \quad \mathcal{D}_{A}(\varphi)+\alpha \cdot \varphi=0,$$
where $\omega$ is a closed 2-form on $N^{*}$ and $\alpha$ is a 1-form on $N^{*}$, both with coefficients in $i \mathbb{R}$ and with compact support in $\operatorname{Int}(N)$. The solutions $(A, \varphi)$ of these equations will be called monopoles. Denote by $\mathcal{M}_{\alpha, \omega}\left(N^{*}\right)$ the $L^{2}$-moduli space of monopoles on $N^{*}$ with respect to the gauge group action. The monopoles in $\mathcal{M}_{\alpha, \omega}\left(N^{*}\right)$ are known to have asymptotic values at infinity, with a flat connection and the zero spinor (a proof can be derived by crossing $N^{*}$ with $S^{1}$ as in [48]; compare [42, Chapter 4.2]). This gives rise to a map
$$R: \mathcal{M}_{\alpha, \omega}\left(N^{*}\right) \longrightarrow \chi(T),$$
where $\chi(T)$ is the moduli space of flat $U(1)$ connections on $\operatorname{det}\left(\left.E\right|_{T}\right)$, modulo gauge transformation on $\left.E\right|_{T}$. Equivalently, we can view $\chi(T)$ as the $U(1)$ character variety of $\pi_{1}(T)$. One can easily see that $\chi(T)$ is a 2-torus; we will introduce a set of coordinates on $\chi(T)$ as follows.

Choose simple closed curves $m, \ell$ on the 2-torus $T$ so that $m$ bounds a disk in $D(K)$ and $\ell$ bounds a Seifert surface in $N$. Let $\mathcal{D}(T)$ be the Dirac operator on the 2-torus $T$ associated to the spin connection. An easy calculation shows that there exists a unique point $\left[A_{0}\right] \in \chi(T)$ for which the coupled Dirac operator $\mathcal{D}_{A_{0}}(T)$ has non-zero kernel. Then, for any $[A] \in \chi(T)$, we can write $A-A_{0}=\alpha \in \Omega^{1}(T ; i \mathbb{R})$ and define
$$m(A)=-2 i \int_{m} \alpha \quad \text { and } \quad \ell(A)=-2 i \int_{\ell} \alpha .$$
The assignment of $(m(A), \ell(A))$ to $[A]$ gives a homeomorphism $\chi(T) \rightarrow \mathbb{R}^{2} /(2 \mathbb{Z})^{2}$. For $a, b \in \mathbb{R} / 2 \mathbb{Z}$, denote by $\left[A_{(a, b)}\right]$ the point in $\chi(T)$ with coordinates $m\left(A_{(a, b)}\right)=a$ and $\ell\left(A_{(a, b)}\right)=b$. Note that the restriction of the unique flat $U(1)$ connection on $Y$ to the torus $T$ is the flat connection $A_{(1,1)}$.

We will treat $\left[A_{(0,0)}\right]=\left[A_{0}\right]$ as a singular point of $\chi(T)$. For sufficiently small $\epsilon>0$, denote by $U_{\epsilon}$ the complement in $\chi(T)$ of the closed $\epsilon$-disk centered at $\left[A_{(0,0)}\right]$. Also, for future use, denote by $\mathcal{S}_{a}$ the circle in the torus $\chi(T)$ which consists of the points $\left[A_{(a, b)}\right]$ with the fixed $a$ and arbitrary $b$.

The monopoles in $\mathcal{M}_{\alpha, \omega}\left(N^{*}\right)$ having $\varphi=0$ will be called reducible, and all other monopoles will be called irreducible. Denote by $\mathcal{M}_{\alpha, \omega}^{\text {red }}\left(N^{*}\right)$ and $\mathcal{M}_{\alpha, \omega}^{\text {irr }}\left(N^{*}\right)$ the reducible, respectively, irreducible loci of $\mathcal{M}_{\alpha, \omega}\left(N^{*}\right)$. The restrictions of the
map $R$ to $\mathcal{M}_{\alpha, \omega}^{\text {irr }}\left(N^{*}\right)$ and to $\mathcal{M}_{\alpha, \omega}^{\text {red }}\left(N^{*}\right)$ will be called, respectively,
$$R^{\mathrm{irr}}: \mathcal{M}_{\alpha, \omega}^{\mathrm{irr}}\left(N^{*}\right) \rightarrow \chi(T) \quad \text { and } \quad R^{\mathrm{red}}: \mathcal{M}_{\alpha, \omega}^{\mathrm{red}}\left(N^{*}\right) \rightarrow \chi(T) .$$

The following structure theorem for the moduli space $\mathcal{M}_{\alpha, \omega}\left(N^{*}\right)$ is proved in Lim [30, Theorem 1.3] and [31, Theorem 3].

Theorem 2.1. For any sufficiently small $\epsilon>0$ there are arbitrarily small perturbations $\alpha$ and $\omega$ such that the following statements hold:
\begin{itemize}
\item[(1)] The map $R^{\text {red }}$ is a diffeomorphism onto its image, which is a circle contained in $U_{\epsilon}$
\item[(2)] The closure of $\left(R^{\mathrm{irr}}\right)^{-1}\left(U_{\epsilon}\right)$ in $\mathcal{M}_{\alpha, \omega}\left(N^{*}\right)$ is a smooth compact 1-manifold with boundary; its boundary points lie in $\mathcal{M}_{\alpha, \omega}^{\text {red }}\left(N^{*}\right) \cup R^{-1}\left(\partial \bar{U}_{\epsilon}\right)$
\item[(3)] Any boundary point of the closure of $\left(R^{\mathrm{irr}}\right)^{-1}\left(U_{\epsilon}\right)$ that lies in $\mathcal{M}_{\alpha, \omega}^{\text {red }}\left(N^{*}\right)$ has a neighborhood in $\mathcal{M}_{\alpha, \omega}\left(N^{*}\right)$ which is modeled on the zeroes of the map $\mathbb{R} \times \mathbb{R}^{+} \rightarrow \mathbb{R}$ sending $(t, z)$ to $t z$, with $\mathbb{R} \times\{0\}$ corresponding to the reducibles
\item[(4)] The map $R$ is smooth on $\left(R^{\mathrm{irr}}\right)^{-1}\left(U_{\epsilon}\right)$
\item[(5)] Both $\left(R^{\text {irr }}\right)^{-1}\left(U_{\epsilon}\right)$ and $\mathcal{M}_{\alpha, \omega}^{\text {red }}\left(N^{*}\right)$ are canonically oriented by the choice of orientation on the real line $H^{1}\left(N^{*} ; \mathbb{R}\right)$.
\end{itemize}
From now on, we will always work with $\epsilon, \omega$, and $\alpha$ that satisfy the conditions of Theorem 2.1. There will be further conditions that will require $\epsilon, \omega$, and $\alpha$ to be sufficiently small. These conditions will be summarized in Remark 3.5.

One can say more about the map $R^{\text {red }}$, see discussion after Theorem 3 in [30] and Section 7 of [31]. The reducible monopoles are given by the equation $F_{A}+\omega=0$. If $\omega=0$, these are just flat connections on $N^{*}$, which are mapped to the circle $b=-1$ in the torus $\chi(T)$. The same is true for any $\omega$ with the vanishing cohomology class in $H_{c}^{2}\left(N^{*} ; \mathbb{R}\right)=H^{2}(N, \partial N ; \mathbb{R})=\mathbb{R}$. In general, it follows by a direct calculation that
$$\ell(A)=-1+i \int_{F} \omega,$$
where $F$ is a Seifert surface for $\ell \subset N$. In particular, the image of $R^{\text {red }}$ : $\mathcal{M}_{\alpha, \omega}^{\text {red }}\left(N^{*}\right) \rightarrow \chi(T)$ is a circle given by the equation $b=-1+c(\omega)$, where $c(\omega) \in \mathbb{R}$ can be made arbitrarily small by choosing small $\omega$. Such a circle is indicated near the bottom of Figure 1.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/84d2ee83-4f0d-43cc-9189-269418503996-10.jpg?height=700&width=732&top_left_y=399&top_left_x=702}
\captionsetup{labelformat=empty}
\caption{Figure 1. The image of $\mathcal{M}_{\alpha, \omega}\left(N^{*}\right)$ in $U_{\epsilon}$}
\end{figure}
2.2. Monopoles on orbifolds. Recall that we denoted by $Y^{o}$ the orbifold with the underlying space $Y$, the singular set $K$, and the cone angle $2 \pi / n$ along $K$, and that we equipped the knot exterior $N=Y^{o}-D^{o}(K)$ with a metric $g(N)$ which restricts to a flat metric on the boundary $T$. We will further assume that, with respect to this flat metric, the meridian $m$ and the longitude $\ell$ are orthogonal geodesics of length $u$ and $v$, respectively. We will equip $Y^{o}$ with an orbifold metric obtained by gluing $g(N)$ to an orbifold metric $g_{u, v}^{o}$ on $D^{o}(K)$. The latter metric is defined as follows.

Definition 2.2. Let $D^{2} \times S^{1}$ be a solid torus with the polar coordinates $(r, \theta, \xi)$, where $0 \leqslant r \leqslant \pi / 2$ and $\theta, \xi \in \mathbb{R} / 2 \pi$. For any $u, v>0$, define the metric $g_{u, v}$ on $D^{2} \times S^{1}$ by the formula
$$\frac{v^{2}}{4 \pi^{2}} d \xi \otimes d \xi+\frac{u^{2}}{4 \pi^{2}}\left(d r \otimes d r+h(r)^{2} d \theta \otimes d \theta\right),$$
where $h:[0, \pi / 2] \rightarrow \mathbb{R}$ is a smooth function such that
\begin{itemize}
\item[-] $h(r)=\sin r$ when $0 \leqslant r \leqslant \pi / 6$,
\item[-] $h(r)=1$ when $5 \pi / 12 \leqslant r \leqslant \pi / 2$, and
\item[-] $h^{\prime \prime}(r)<0$ when $\pi / 6 \leqslant r \leqslant 5 \pi / 12$.
\end{itemize}
We call $g_{u, v}$ the smooth bullet-type metric. With respect to this metric, the boundary of $D^{2}$ has length $u$, and the circle factor has length $v$. We define the orbifold
bullet-type metric $g_{u, v}^{o}$ as the quotient metric of $g_{n u, v}$ under the finite-order isometry $\iota$ of $D^{2} \times S^{1}$ taking $(r, \theta, \xi)$ to $(r, \theta+2 \pi / n, \xi)$. Note that both $g_{u, v}$ and $g_{u, v}^{o}$ are flat near the boundary and have positive scalar curvature $\operatorname{scal}\left(g_{u, v}\right)$ and $\operatorname{scal}\left(g_{u, v}^{o}\right)$ elsewhere.

We will need to perturb the Seiberg-Witten equations near $K$. To do this, we let $\nu$ be the 2-form on $D^{2} \times S^{1}$ obtained by pulling back an $i \mathbb{R}$-valued 2-form on the unit disk $D^{2}$ which is supported in the region $r \leqslant \pi / 6$ and integrates to $i / 2$. We define the orbifold 2-form $\nu^{o}$ to be the quotient of the form $n \cdot \nu$ by the action of the isometry $\iota$. The following lemma is straightforward.

Lemma 2.3. There exists a constant $\delta_{0}>0$ such that the inequalities
$$\left|\delta_{0} \nu(x)\right| \leqslant \operatorname{scal}\left(g_{u, v}\right)(x) \quad \text { and } \quad\left|\delta_{0} \nu^{o}(y)\right| \leqslant \operatorname{scal}\left(g_{u, v}^{o}\right)(y)$$
hold for all $x \in D(K)$ and $y \in D^{o}(K)$.
In what follows, we will choose $\epsilon>0$ (the radius of the disk around the singularity in $\chi\left(T^{2}\right)$ ) smaller than the constant $\delta_{0}>0$ of Lemma 2.3.

Denote by $g\left(Y^{o}\right)$ the orbifold metric on $Y^{o}=N \cup_{T} D^{o}(K)$ obtained by gluing together the metrics $g(N)$ and $g_{u, v}^{o}$. Recall that the underlying space of $Y^{o}$ is an integral homology 3-sphere. Therefore, the orbifold spin ${ }^{c}$ structures $\mathfrak{s}_{k}$ on $Y^{o}$ can be canonically parametrized by integers $0 \leqslant k \leqslant n-1$; see Baldridge [4, Theorem 7 and Theorem 4]. Given an orbifold $\operatorname{spin}^{c}$ structure $\mathfrak{s}_{k}$, consider the orbifold Seiberg-Witten equations as in Baldridge [4, Section 2.4],
$$F_{A}+\omega^{o}=\tau(\varphi), \quad \mathcal{D}_{A}(\varphi)=0,$$
where $\omega^{o}$ is a closed orbifold 2-form on $Y^{o}$ with coefficients in $i \mathbb{R}$. Equations (7) give rise to the orbifold Seiberg-Witten moduli space, which will be called $\mathcal{M}\left(Y^{o}, \mathfrak{s}_{k}, g\left(Y^{o}\right), \omega^{o}\right)$. This moduli space can be recovered from $\mathcal{M}_{\alpha, \omega}\left(N^{*}\right)$ by using the right choice of metric and perturbation on $Y^{o}$. The metric will be the metric $g\left(Y^{o}\right)_{L}$ on the orbifold
$$Y^{o}=N \cup_{T}([-L, L] \times T) \cup_{T} D^{o}(K)$$
obtained from $g\left(Y^{o}\right)$ by 'neck stretching', and the perturbation 2-form $\omega_{\delta}^{o}=\omega+$ $\delta \cdot \nu^{o}$ being the sum of the 2-form $\omega$ supported in $\operatorname{Int}(N)$, and the orbifold 2-form $\delta \cdot \nu^{o}$ supported in $\operatorname{Int}\left(D^{o}(K)\right)$, which integrates to $i \delta / 2$ on each meridional disk.

Proposition 2.4. For a generic $\delta \in\left(\epsilon, \delta_{0}\right)$, the map $R^{\mathrm{irr}}$ is transversal to $\mathcal{S}_{2 k / n+1-\delta}$ for all $k$. Moreover, for all sufficiently large $L>0$, the zero-dimensional manifolds
$$\mathcal{M}^{\operatorname{irr}}\left(Y^{o}, \mathfrak{s}_{k}, g\left(Y^{o}\right)_{L}, \omega_{\delta}^{o}-d \alpha\right) \quad \text { and } \quad\left(R^{\mathrm{irr}}\right)^{-1}\left(\mathcal{S}_{2 k / n+1-\delta}\right)$$
are orientation preserving diffeomorphic.
Proof. The transversality assertion follows from Theorem 2.1 and Sard's Theorem. The identification between $\mathcal{M}^{\text {irr }}\left(Y^{o}, \mathfrak{s}_{k}, g\left(Y^{o}\right)_{L}, \omega_{\delta}^{o}-d \alpha\right)$ and $\left(R^{\text {irr }}\right)^{-1}\left(\mathcal{S}_{2 k / n+1-\delta}\right)$ is an orbifold version of [30, Theorem 1.4] and [31, Theorem 4], which is essentially a gluing argument along a torus, hence the presence of orbifold points makes no difference. The key ingredient is the inequality (6), which implies that the $\delta \cdot \nu^{o}-$perturbed Seiberg-Witten equations on the cylindrical-end orbifold $((-\infty, 0] \times$ $T) \cup_{T} D^{o}(K)$ have no irreducible solutions with finite energy. \(\square\)

An argument similar to that in [31, page 637] then shows that the oriented count of points in $\left(R^{\text {irr }}\right)^{-1}\left(\mathcal{S}_{2 k / n+1-\delta}\right)$ is given by the intersection number of $R\left(\mathcal{M}_{\alpha, \omega}^{\text {irr }}\left(N^{*}\right)\right)$ with the circle $\mathcal{S}_{2 k / n+1-\delta}$ in the torus $\chi(T)$, where the torus $\chi(T)$ is oriented by $\partial / \partial a \wedge \partial / \partial b$, and the circle $\mathcal{S}_{2 k / n+1-\delta}$ is oriented by $\partial / \partial b$ (again, the presence of orbifold points makes no difference). By combining this observation with Proposition 2.4, we obtain the following result.

Corollary 2.5. For a generic $\delta \in\left(\epsilon, \delta_{0}\right)$ and for all $L>0$ sufficiently large, the oriented count of points in the moduli space $\mathcal{M}^{\mathrm{irr}}\left(Y^{o}, \mathfrak{s}_{k}, g\left(Y^{o}\right)_{L}, \omega_{\delta}^{o}-d \alpha\right)$ equals the intersection number of $R\left(\mathcal{M}_{\alpha, \omega}^{\mathrm{irr}}\left(N^{*}\right)\right)$ with the circle $\mathcal{S}_{2 k / n+1-\delta}$ in the torus $\chi(T)$.
2.3. Monopoles on $Y$. Now we study the perturbed Seiberg-Witten equations on the homology sphere $Y$. Let us consider the splitting $Y=N \cup_{T} D(K)$ with a metric $g(Y)$ which restricts to the metric $g(N)$ on $N$ and a smooth bullet-type metric $g_{u, v}$ on $D(K)=S^{1} \times D^{2}$ (see Definition 2.2). For any constant $L>0$, equip the manifold
$$Y=N \cup_{T}([-L, L] \times T) \cup_{T} D(K)$$
with the metric $g(Y)_{L}$ obtained from $g(Y)$ by 'neck stretching'. In addition, let $\omega_{\delta}=\omega+\delta \cdot \nu$ be the sum of the form $\omega$ supported on $N$ and the 2-form $\delta \cdot \nu$ supported on $D(K)$ (as defined in Section 2.2), which integrates to $i \delta / 2$ on each
meridional disk. Then the $\left(\omega_{\delta}, \alpha\right)$-perturbed Seiberg-Witten equations, as studied by Lim [31], are of the form
$$F_{A}+\omega_{\delta}=\tau(\varphi), \quad \mathcal{D}_{A}(\varphi)+\alpha \cdot \varphi=0 .$$
The corresponding moduli space $\mathcal{M}_{\alpha, \omega_{\delta}}(Y, g(Y))$ contains exactly one reducible solution. We wish to compare $\mathcal{M}_{\alpha, \omega_{\delta}}(Y, g(Y))$ with the moduli space $\mathcal{M}(Y, g(Y), \beta)$ (which was used in [39] to define $\lambda_{\mathrm{SW}}$ ) given by the equations
$$F_{A}=\tau(\varphi)+d \beta, \quad \mathcal{D}_{A}(\varphi)=0 .$$
To this end, observe that any closed 2-form $\omega_{\delta}$ is exact on the homology sphere $Y$, hence can be written in the form $\omega_{\delta}=d \gamma_{\delta}$, where $\gamma_{\delta}$ is a 1-form with coefficients in $i \mathbb{R}$.

Proposition 2.6. The choice of $\beta_{\delta}=\alpha-\gamma_{\delta}$ establishes an orientation preserving diffeomorphism between the moduli spaces $\mathcal{M}_{\alpha, \omega_{\delta}}(Y, g(Y))$ and $\mathcal{M}\left(Y, g(Y), \beta_{\delta}\right)$.

Proof. The change of variables $B=A+\alpha$ in the Seiberg-Witten equations (8) results in the equations $F_{B}-d \alpha+d \gamma_{\delta}=\tau(\varphi)$ and $\mathcal{D}_{B}(\varphi)=0$, which match the equations (9) defining $\mathcal{M}\left(Y, g(Y), \beta_{\delta}\right)$ once we set $\beta_{\delta}=\alpha-\gamma_{\delta}$. The result now follows by comparing the orientation conventions for the two moduli spaces. \(\square\)

The following result is a special case of Corollary 2.5 when $n=1$.
Corollary 2.7. For a generic $\delta \in\left(\epsilon, \delta_{0}\right)$, the map $R^{\mathrm{irr}}$ is transversal to $\mathcal{S}_{1-\delta}$. Moreover, for all $L>0$ sufficiently large, the oriented count of points in the moduli space $\mathcal{M}^{\mathrm{irr}}\left(Y, g(Y)_{L}, \beta_{\delta}\right)$ equals the intersection number of $R\left(\mathcal{M}_{\alpha, \omega}^{\mathrm{irr}}\left(N^{*}\right)\right)$ with the circle $\mathcal{S}_{1-\delta}$ in the torus $\chi(T)$.
2.4. The spectral flow formula. According to Part (1) of Theorem 2.1, the moduli space $\mathcal{M}_{\alpha, \omega}^{\text {red }}\left(N^{*}\right)$ is a circle, for any sufficiently small generic perturbations $\alpha$ and $\omega$. This circle admits a parametrization by $\theta\left(N^{*}, a\right)=\left(R^{\text {red }}\right)^{-1}\left(\mathcal{S}_{a}\right)$, thereby giving rise to a family of twisted Dirac operators $D_{\theta\left(N^{*}, a\right)}$ on the product end manifold $N^{*}$. The $L^{2}$ completions of these operators are self-adjoint, which leads to a well-defined notion of spectral flow; see for instance Cappell, Lee, and Miller [10]. The points where the operators $D_{\theta\left(N^{*}, a\right)}$ have non-zero kernels are precisely the points in $\mathcal{M}_{\alpha, \omega}^{\text {red }}\left(N^{*}\right)$ which serve as the boundary points of the closure of $\left(R^{\text {irr }}\right)^{-1}\left(U_{\epsilon}\right)$. It then follows from Part (3) of Theorem 2.1 that, for any choice of perturbations $\alpha$ and $\omega$ as in that theorem, the spectral flow is transverse, that is,
the spectral curves of the family $D_{\theta\left(N^{*}, a\right)}$ intersect the $a$-axis transversely with multiplicity one.

Lemma 2.8. For sufficiently small $\alpha$ and $\omega$, the spectral flow of the family of twisted Dirac operator $\mathcal{D}_{\theta\left(N^{*}, a\right)}$ around the circle is equal to zero.

Proof. Let $f: N^{*} \rightarrow S^{1}$ be an arbitrary smooth function which induces an isomorphism $f_{*}: H_{1}(X) \rightarrow \mathbb{Z}$ and consider the family $\mathcal{D}_{a}=\mathcal{D}+i a d f$ of twisted Dirac operators on $N^{*}$. The unperturbed spin Dirac operator $\mathcal{D}$ is quaternionic linear, hence the $j$-conjugate of $\mathcal{D}_{a}$ is $\mathcal{D}_{-a}$, which makes the picture of the spectral curves of $\mathcal{D}_{a}$ symmetric with respect to the involution sending $a$ to $-a$. This ensures that the spectral flow of the family $\mathcal{D}_{a}$, which was defined in [3, Section 7] as the intersection number of the spectral curves with a small vertical shift of the $a$-axis, vanishes. The family $\mathcal{D}_{\theta\left(N^{*}, a\right)}$ is a deformation of the family $\mathcal{D}_{a}$ hence its spectral flow vanishes as well, as long as the perturbations $\alpha$ and $\omega$ are sufficiently small. \(\square\)

In what follows, we will choose a generic $\delta>0$ such that following condition is satisfied:
$$\text { the operators } \mathcal{D}_{\theta\left(N^{*}, a\right)} \text { are invertible at } a=2 k / n-1-\delta \text { for all } k \text {. }$$

Proposition 2.9. For all sufficiently large $L>0$, sufficiently small generic perturbations $\alpha$ and $\omega$, and generic $\delta>0$, one has the relation
$$\begin{aligned}
\# \mathcal{M}^{\operatorname{irr}}\left(Y^{o}, \mathfrak{s}_{k}, g\left(Y^{o}\right)_{L}, \omega_{\delta}^{o}-d \alpha\right)= & \# \mathcal{M}^{\operatorname{irr}}\left(Y, g(Y)_{L}, \beta_{\delta}\right) \\
& -\operatorname{SF}\left(\mathcal{D}_{\theta\left(N^{*}, 1-\delta\right)}, \mathcal{D}_{\theta\left(N^{*}, 2 k / n+1-\delta\right)}\right) .
\end{aligned}$$
The spectral flow in this formula is calculated along any path in the circle $\theta\left(N^{*}, a\right)$ that leads from $\theta\left(N^{*}, 1-\delta\right)$ to $\theta\left(N^{*}, 2 k / n+1-\delta\right)$; according to Lemma 2.8, this is a well defined quantity.

Proof. According to Corollary 2.5 and Corollary 2.7, we have the following identities
$$\begin{gathered}
\# \mathcal{M}^{\mathrm{irr}}\left(Y^{o}, \mathfrak{s}_{k}, g\left(Y^{o}\right)_{L}, \omega_{\delta}^{o}-d \alpha\right)=\#\left(R\left(\mathcal{M}_{\alpha, \omega}^{\mathrm{irr}}\left(N^{*}\right)\right) \cap \mathcal{S}_{2 k / n+1-\delta}\right) \quad \text { and } \\
\# \mathcal{M}^{\mathrm{irr}}\left(Y, g(Y)_{L}, \beta_{\delta}\right)=\#\left(R\left(\mathcal{M}_{\alpha, \omega}^{\mathrm{irr}}\left(N^{*}\right)\right) \cap \mathcal{S}_{1-\delta}\right) .
\end{gathered}$$
According to Theorem 2.1, the one-dimensional moduli space $\mathcal{M}_{\alpha, \omega}^{\text {irr }}\left(N^{*}\right)$ provides an oriented cobordism between the points in $\mathcal{M}_{\alpha, \omega}^{\text {irr }}\left(N^{*}\right) \cap R^{-1}\left(\mathcal{S}_{1-\delta}\right)$, the points
in $\mathcal{M}_{\alpha, \omega}^{\text {irr }}\left(N^{*}\right) \cap R^{-1}\left(\mathcal{S}_{2 k / n-1-\delta}\right)$, and the reducible boundary points in $\mathcal{M}_{\alpha, \omega}^{\text {red }}\left(N^{*}\right)$ that fit into the interval between $\theta\left(N^{*}, 1-\delta\right)$ and $\theta\left(N^{*}, 2 k / n+1-\delta\right)$; of the two intervals in the circle $\mathcal{M}_{\alpha, \omega}^{\text {red }}\left(N^{*}\right)$ having the same endpoints, we chose the one that does not contain $\theta\left(N^{*}, 0\right)$ so as to stay within $U_{\epsilon}$. The reducible boundary points in $\mathcal{M}_{\alpha, \omega}^{\text {red }}\left(N^{*}\right)$ correspond to the points where the Dirac operators $D_{\theta\left(N^{*}, a\right)}$ have non-zero kernels hence these are precisely the points that contribute to the spectral flow in the statement of the proposition. That they contribute with the right sign follows from the description of the signs in [30, Section 11.3] and [31, page 635]: when moving in the direction of the orientation of $\mathcal{M}_{\alpha, \omega}^{\text {red }}\left(N^{*}\right)$, the contribution to the spectral flow at $\theta\left(N^{*}, a\right)$ is positive if and only if the orientation of $\mathcal{M}_{\alpha, \omega}^{\text {irr }}\left(N^{*}\right)$ is into $\theta\left(N^{*}, a\right)$. \(\square\)

\section*{3. Eta-invariant of the Dirac operator}

Let $X$ be the mapping torus of the covering translation $\tau: \Sigma \rightarrow \Sigma$ with the standard orientation and homology orientation. A choice of spin structure on $X$ induces a spin structure on $\Sigma$. This induced spin structure is invariant under $\tau$ hence it is the same spin structure that lifts the unique spin structure on the integral homology sphere $Y$. We will have these particular spin structures in mind when talking about the spin manifolds $\Sigma$ and $Y$. In this section, we will compare the $\eta$-invariants of the (twisted) spin Dirac operators on $\Sigma$ and $Y$. The idea for this comparison comes from Lim [31].

For the knot $K \subset Y$, consider its preimage $\widetilde{K} \subset \Sigma$ under the branched cover projection $\Sigma \rightarrow Y$. The knot $\widetilde{K}$ can also be viewed as the fixed point set of the covering translation $\tau: \Sigma \rightarrow \Sigma$. Write
$$Y=N \cup D(K) \quad \text { and } \quad \Sigma=N_{n} \cup \widetilde{D}(K),$$
where $N_{n} \rightarrow N$ is a regular $n$-fold cover. Let $Y(0)$ be the manifold obtained from $Y$ by 0-surgery on the knot $K$, and similarly $\Sigma(0)$ the manifold obtained from $\Sigma$ by 0-surgery on $\widetilde{K}$. Write
$$Y(0)=N \cup D(0) \quad \text { and } \quad \Sigma(0)=N_{n} \cup \widetilde{D}(0),$$
where $D(0)$ is a solid torus $D^{2} \times S^{1}$ glued to $N$ along its torus boundary by sending its longitude and meridian to the curve $m$ and $l$ in $T=\partial N$ respectively (see Section 2.1), and similarly for $\widetilde{D}(0)$. The regular $n$-fold cover $N_{n} \rightarrow N$ extends to a regular $n$-fold cover $\Sigma(0) \rightarrow Y(0)$. The aforementioned spin structures on $Y$ and $\Sigma$ give
rise to spin structures on $Y(0)$ and $\Sigma(0)$. Denote by $g(Y(0))$ the metric on the manifold $Y_{0}$ that equals $g_{N}$ on $N$ and the bullet-type metric $g_{v, u}$ on $D(0)$. We use the symbol $g(\Sigma)$ and $g(\Sigma(0))$ to denote the pull back of the metrics $g\left(Y^{o}\right)$ and $g(Y(0))$. For any positive constant $L$, denote by $g(*)_{L}$ the metrics on these manifolds obtained from $g(*)$ by neck stretching as in Section 2; these metrics will sometimes be suppressed in our notations.

Let $\theta(Y)$ be the unique reducible monopole in $\mathcal{M}_{\alpha, \omega_{\delta}}\left(Y, g(Y)_{L}\right)$ for the choices of $\alpha, \omega_{\delta}$ and $L$ as Corollary 2.7; this monopole is the unique extension to $Y$ of the reducible monopole $\theta\left(N^{*}, 1-\delta\right)$ on $N^{*}$ whose limiting value is the flat connection $A_{(1-\delta,-1+c(\omega))}$. Denote by $\theta(\Sigma)$ the lift of $\theta(Y)$ to $\Sigma$.

Note that each reducible monopole $\theta\left(N^{*}, a\right)$ on $N^{*}$ admits a unique extension to a reducible monopole on $Y(0)$, which will be called $\theta(Y(0), a)$. This follows by applying Theorem 2.1 to the manifold $D(0)$ in place of $N$, and matching the limiting values in $\chi(T)$ by choosing an appropriate perturbation on $D(0)$. This perturbation can be made arbitrary small by choosing small $\alpha$ and $\omega$. A similar construction applied to $\Sigma(0)$ in place of $Y(0)$ gives rise to the monopole $\theta(\Sigma(0), a)$ on $\Sigma(0)$. The monopoles $\theta(Y(0), 1-\delta)$ and $\theta(\Sigma(0), 1-\delta)$ will be referred to as simply $\theta(Y(0))$ and $\theta(\Sigma(0))$.

Lemma 3.1. For any generic $\delta>0$ that satisfied (10), there exist constants $C_{1}$ and $C_{2}$ which are independent of $Y, \Sigma, K$, and $L$ (but may depend on $\delta$ ) such that, for all sufficiently large $L>0$, the following property holds
$$\begin{aligned}
& \eta\left(\mathcal{D}_{\theta(Y)}\right)=\eta\left(\mathcal{D}_{\theta(Y(0))}\right)+C_{1}+o(1), \\
& \eta\left(\mathcal{D}_{\theta(\Sigma)}\right)=\eta\left(\mathcal{D}_{\theta(\Sigma(0))}\right)+C_{2}+o(1),
\end{aligned}$$
where $o(1)$ as usual denotes a quantity that limits to zero as $L$ goes to infinity.
Proof. The restrictions of the monopoles $\theta(Y)$ and $\theta(Y(0))$ to the tubular neigh-borhoods $D(K)$ and $D(0)$ give rise to the monopoles on the product end manifolds
$$D^{*}(K)=((-\infty, 0] \times T) \cup_{T} D(K) \quad \text { and } \quad D^{*}(0)=((-\infty, 0] \times T) \cup_{T} D(0)$$
which will be called, respectively, $\theta\left(D^{*}(K)\right)$ and $\theta\left(D^{*}(0)\right)$. Since both manifolds $D^{*}(K)$ and $D^{*}(0)$ have non-negative scalar curvature, the Dirac operators $\mathcal{D}_{\theta\left(D^{*}(K)\right)}$ and $\mathcal{D}_{\theta\left(D^{*}(0)\right)}$ are invertible. Combined with the invertibility of $\mathcal{D}_{\theta\left(N^{*}, 1-\delta\right)}$, this implies that, for all sufficiently large $L>0$, the operators $\mathcal{D}_{\theta(Y)}$
and $\mathcal{D}_{\theta(Y(0))}$ are invertible. Moreover, it follows from Mazzeo and Melrose [37] that
$$\begin{aligned}
& \eta\left(\mathcal{D}_{\theta(Y)}\right)=\eta\left(\mathcal{D}_{\theta\left(N^{*}, 1-\delta\right)}\right)+\eta\left(\mathcal{D}_{\theta\left(D^{*}(K)\right)}\right)+o(1) \text { and } \\
& \eta\left(\mathcal{D}_{\theta(Y(0))}\right)=\eta\left(\mathcal{D}_{\theta\left(N^{*}, 1-\delta\right)}\right)+\eta\left(\mathcal{D}_{\theta\left(D^{*}(0)\right)}\right)+o(1) .
\end{aligned}$$
Subtracting these two formulas, we obtain formula (13) with the constant $C_{1}=$ $\eta\left(\mathcal{D}_{\theta\left(D^{*}(K)\right)}\right)-\eta\left(\mathcal{D}_{\theta\left(D^{*}(0)\right)}\right)$, which is a linear combination of the $\eta$-invariants of standard solid tori and hence is independent of $Y, K$, and $L$. Formula (14) is proved similarly. \(\square\)

Lemma 3.2. One has the following identity
$$\eta\left(\mathcal{D}_{\theta(\Sigma(0))}\right)=\sum_{k=0}^{n-1} \eta\left(\mathcal{D}_{\theta(Y(0), 2 k / n+1-\delta)}\right) .$$
Proof. Since $\theta(\Sigma(0))$ is the lift of $\theta(Y(0))$ under the regular $n$-fold covering map $\Sigma(0) \rightarrow Y(0)$, the covering translation $\tau: \Sigma(0) \rightarrow \Sigma(0)$ induces an action on the spinors, splitting each operator $\mathcal{D}_{\theta(\Sigma(0))}$ into a direct sum of the operators $\mathcal{D}_{\theta(\Sigma(0))}^{\alpha}$ on its eigenspaces. This in turn leads to the identity
$$\eta\left(\mathcal{D}_{\theta(\Sigma(0))}\right)=\sum_{\alpha} \eta\left(\mathcal{D}_{\theta(\Sigma(0))}^{\alpha}\right) .$$
One can easily check that the operators $\mathcal{D}_{\theta(\Sigma(0))}^{\alpha}$ in this formula are precisely the operators $\mathcal{D}_{\theta(Y(0), 2 k / n+1-\delta)}$, which completes the proof. \(\square\)

Lemma 3.3. For all sufficiently large $L>0$ and all $k$, one has
$$\eta\left(\mathcal{D}_{\theta(Y(0), 2 k / n+1-\delta)}\right)=\eta\left(\mathcal{D}_{\theta(Y(0))}\right)+2 \operatorname{SF}\left(\mathcal{D}_{\theta\left(N^{*}, 1-\delta\right)}, \mathcal{D}_{\theta\left(N^{*}, 2 k / n+1-\delta\right)}\right) .$$
Proof. According to [3], the difference $\eta\left(\mathcal{D}_{\theta(Y(0), 2 k / n+1-\delta)}\right)-\eta\left(\mathcal{D}_{\theta(Y(0))}\right)$ equals twice the spectral flow $\operatorname{SF}\left(\mathcal{D}_{\theta(Y(0))}, \mathcal{D}_{\theta(Y(0), 2 k / n+1-\delta)}\right)$. According to [10], for all sufficiently large $L>0$, this spectral flow is the sum of the spectral flow over $D^{*}(0)$ and the spectral flow over $N^{*}$. The former vanishes because the metric on $D^{*}(0)$ has non-negative scalar curvature and the perturbation is small, and the latter equals the spectral flow $\operatorname{SF}\left(\mathcal{D}_{\theta\left(N^{*}, 1-\delta\right)}, \mathcal{D}_{\theta\left(N^{*}, 2 k / n+1-\delta\right)}\right)$. \(\square\)

Corollary 3.4. For any $\delta$ that satisfies (10), there exists a constant $C^{\prime}$ which, for all sufficiently large $L>0$, is independent of $Y, \Sigma, K$, and $L$, and has the
property that
$$\eta\left(\mathcal{D}_{\theta(\Sigma)}\right)=n \cdot \eta\left(\mathcal{D}_{\theta(Y)}\right)+2 \sum_{k=0}^{n-1} \operatorname{SF}\left(\mathcal{D}_{\theta\left(N^{*}, 1-\delta\right)}, \mathcal{D}_{\theta\left(N^{*}, 2 k / n+1-\delta\right)}\right)+C^{\prime}+o(1) .$$

Remark 3.5. So far, we have made choices of the following parameters:
\begin{itemize}
\item[-] $\epsilon>0$ : the radius of the disk around the singular point $\left[A_{(0,0)}\right] \in \chi(T)$,
\item[-] $\alpha, \omega$ : differential forms on $N^{*}$ used to perturb the Seiberg-Witten equations, and
\item[-] $\delta>0$ : a positive number whose products with the fixed 2-forms $\nu$ and $\nu^{o}$ serve as the perturbations on $D(K)$ and $D^{o}(K)$.
\end{itemize}
(Other parameters, such as the bullet type metric $g_{u, v}$ and the 2-form $\nu$ on $D(K)$, have been fixed since the moment they were defined). We have imposed several constraints on these parameters. To clarify that these constrains do not contradict each other, we summarize them here: First, we choose $\epsilon>0$ to be small enough so that Theorem 2.1 applies. The parameter $\epsilon>0$ also needs to be smaller than the constant $\delta_{0}>0$ of Lemma 2.3. Then we choose generic $\alpha$ and $\omega$ that meet the requirements of Theorem 2.1. The perturbations $\alpha$ and $\omega$ also need to be small enough so that Lemma 2.8, Proposition 2.9, and all results of Section 3 hold. Finally, we choose a generic $\delta \in\left(\epsilon, \delta_{0}\right)$ to satisfy the condition (10) and the condition of Corollary 2.5. We will fix all these choices from now on and will not discuss them further.

\section*{4. Eta-invariant of the signature operator}

In this section, we will analyze the eta-invariants of the odd signature operators on the manifolds $M=Y, \Sigma, Y(0)$, and $\Sigma(0)$. As before, we fix the long neck metrics $g(M)_{L}$ on these manifolds and use $\eta_{\text {sign }}(M)$ to denote the corresponding eta-invariants. Since $\eta_{\text {sign }}(M)$ is closely related to a topological invariant (the signature), its analysis is much easier than that of the eta-invariant of the Dirac operator; cf. [38].

Lemma 4.1. One has the following identities
$$\eta_{\text {sign }}(\Sigma)=\eta_{\text {sign }}(\Sigma(0)) \quad \text { and } \quad \eta_{\text {sign }}(Y)=\eta_{\text {sign }}(Y(0)) .$$
Proof. This will follow from an excision argument for $\eta_{\text {sign }}(M)$. We will focus on the second equality since the first one is similar. To keep better track of notation,
we will denote by
$$f_{1}: \partial D(K) \rightarrow T=\partial N \quad \text { and } \quad f_{0}: \partial D(0) \rightarrow T=\partial N$$
the gluing maps for $Y$ and $Y(0)$, and denote by $g(T)$ the restriction of the metric $g(N)$ to $T$. We form a Riemannian 4-manifold with corners,
$$W=([0,3] \times[-L, L] \times T) \cup([0,1] \times D(K)) \cup([2,3] \times D(0)),$$
where $[0,1] \times D(K)$ is glued to $[0,3] \times[-L, L] \times T$ via the map
$$\operatorname{id}_{[0,1]} \times f_{1}:[0,1] \times \partial D(K) \rightarrow[0,1] \times\{L\} \times T,$$
and $[2,3] \times D(0)$ is glued to $[0,3] \times[-L, L] \times T$ via the map
$$\operatorname{id}_{[2,3]} \times f_{0}:[2,3] \times \partial D(K) \rightarrow[2,3] \times\{L\} \times T .$$
A schematic picture of this region is depicted in Figure 2.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/84d2ee83-4f0d-43cc-9189-269418503996-19.jpg?height=458&width=1123&top_left_y=1261&top_left_x=430}
\captionsetup{labelformat=empty}
\caption{Figure 2. $g(W)$}
\end{figure}

The metric $g(W)$ on $W$ is obtained by gluing together the product metrics $[0,3] \times[-L, L] \times g(T),[0,1] \times g_{u, v}$, and $[2,3] \times g_{v, u}$. The connected component
$$(\{1\} \times D(K)) \cup([1,2] \times\{L\} \times T) \cup(\{2\} \times D(0))$$
of the boundary of $W$ is the sphere $S^{3}$ with a non-smooth metric. We modify the metric $g(W)$ in a collar neighborhood of this $S^{3}$ to obtain a new metric $g^{\prime}(W)$ that equals the product metric with the standard smooth round metric $g\left(S^{3}\right)$. Next, we form the manifold $W^{\prime}=W \cup([0,3] \times N)$ by gluing the two pieces together via the map
$$\operatorname{id}_{[0,3] \times T}:[0,3] \times\{-L\} \times T \rightarrow[0,3] \times \partial N .$$

The metric $g\left(W^{\prime}\right)$ is obtained by gluing together $g^{\prime}(W)$ and the product metric $[0,3] \times g(N)$. Note that $\left(W^{\prime}, g\left(W^{\prime}\right)\right)$ is a smooth Riemannian manifold (without corners). It has three boundary components, $\left(Y, g(Y)_{L}\right),\left(Y(0), g(Y(0))_{L}\right)$, and $\left(S^{3}, g\left(S^{3}\right)\right)$. The signature of $W^{\prime}$ is zero because the map $H^{2}\left(W^{\prime}, \partial W^{\prime} ; \mathbb{R}\right) \rightarrow$ $H^{2}\left(W^{\prime} ; \mathbb{R}\right)$ is trivial. The eta-invariant of $S^{3}$ vanished because $\left(S^{3}, g\left(S^{3}\right)\right)$ admits an orientation-reversing isometry. The Pontryagin form on $[0,3] \times N$ also vanishes with respect to the product metric. Now, using the Atiyah-Patodi-Singer index theorem [2], we obtain the equality
$$\eta_{\operatorname{sign}}(Y)-\eta_{\operatorname{sign}}(Y(0))=-\frac{1}{3} \int_{W^{\prime}} p_{1}\left(g^{\prime}(W)\right)$$
whose right hand side is a constant independent of $N$. To compute this constant, we can set $N=D^{2} \times S^{1}$ and $g(N)=g_{u, v}$. Then both $\left(Y, g(Y)_{L}\right)$ and $\left(Y(0), g(Y(0))_{L}\right)$ admit orientation reversing isometries hence their eta-invariants vanish. Thus we conclude that, for any $N$, the equality $\eta_{\text {sign }}(Y)-\eta_{\text {sign }}(Y(0))=0$ holds. \(\square\)

Lemma 4.2. One has the following identity
$$\eta_{\text {sign }}(\Sigma(0))=n \cdot \eta_{\text {sign }}(Y(0))-\sum_{m=1}^{n-1} \operatorname{sign}_{m / n}(K) .$$

Proof. The manifold $\Sigma(0)$ is a regular (unbranched) $n$-fold cyclic cover of $Y(0)$. By splitting the forms on $\Sigma(0)$ into eigenspaces for the induced action of $\tau$, we obtain the relation
$$\eta_{\operatorname{sign}}(\Sigma(0))=\eta_{\operatorname{sign}}(Y(0))+\sum_{\alpha \neq 1} \eta_{\operatorname{sign}, \alpha}(Y(0)) .$$
Since $\rho_{\alpha}(Y(0))=\eta_{\text {sign }}(Y(0))-\eta_{\text {sign }, \alpha}(Y(0))$, this immediately implies that
$$\eta_{\text {sign }}(\Sigma(0))=n \cdot \eta_{\text {sign }}(Y(0))-\sum_{\alpha \neq 1} \rho_{\alpha}(Y(0)) .$$
Now, if $\alpha$ sends the meridian of $K$ to $m \in \mathbb{Z} / n$, it follows from Gilmer [19, Theorem 3.6] that $\rho_{\alpha}(Y(0))=\operatorname{sign}_{m / n}(K)$. Gilmer only states his result for $Y=S^{3}$ but his method will work more generally for any integral homology sphere. \(\square\)

Corollary 4.3. The eta-invariants of $\Sigma$ and $Y$ are related by the formula
$$\eta_{\mathrm{sign}}(\Sigma)=n \cdot \eta_{\mathrm{sign}}(Y)-\sum_{m=1}^{n-1} \operatorname{sign}_{m / n}(K) .$$

\section*{5. Proof of Theorem B}

Let $X$ be the mapping torus of $\tau: \Sigma \rightarrow \Sigma$. Since $\tau$ has finite order, $X$ admits an obvious circle action and the orbifold circle bundle $\pi: X \rightarrow Y^{o}$. Let $i \eta$ be the connection form of this bundle. Any orbifold metric $g\left(Y^{o}\right)_{L}$ on $Y^{o}$ as in Proposition 2.4 defines a metric $g=\eta^{2}+\pi^{*} g\left(Y^{o}\right)_{L}$ on $X$. Similarly, a perturbation form $\omega_{\delta}^{o}-d \alpha$ as in Proposition 2.4 lifts to a $\tau$-invariant form $\omega$ on $\Sigma$. Since $\Sigma$ is a rational homology sphere, we can write $\omega=d \gamma$ for some 1-form $\gamma$ on $\Sigma$ and let $\beta=\pi^{*} \gamma$. With respect to the metric $g$ and perturbation $\beta$, we conclude as in Baldridge [4] that
$$\# \mathcal{M}^{\mathrm{irr}}(X, g, \beta)=\sum_{k=0}^{n-1} \# \mathcal{M}^{\mathrm{irr}}\left(Y^{o}, \mathfrak{s}_{k}, g\left(Y^{o}\right)_{L}, \omega_{\delta}^{o}-d \alpha\right)$$

Remark 5.1. A fine point in this kind of argument is the discrepancy between the spinorial connection and the Levi-Civita connection associated with the metric. This discrepancy does not arise in our case because the two Dirac operators in question differ by the Clifford multiplication by the 3-form $\eta \wedge d \eta$ (see Baldridge [4, Lemma 17]) which vanishes because $\eta$ is a flat connection.

Remark 5.2. It follows from Baldridge [4] that the irreducible part of the Seiberg-Witten moduli space on $X$ is non-degenerate. The definition of $\lambda_{\mathrm{SW}}(X)$ in [39] further requires that the (perturbed) blown up Seiberg-Witten moduli space on $X$ be free of reducibles. That this is the case for our mapping torus $X$ follows by a simple Fourier analysis argument from a similar property of the blown up Seiberg-Witten moduli space on $Y^{o}$.

Proposition 2.9 now implies that
$$\begin{aligned}
& \# \mathcal{M}^{\mathrm{irr}}(X, g, \beta)= \\
& \quad n \# \mathcal{M}^{\mathrm{irr}}\left(Y, g_{L}, \beta_{\delta}\right)-\sum_{k=0}^{n-1} \operatorname{SF}\left(\mathcal{D}_{\theta\left(N^{*}, 1-\delta\right)}, \mathcal{D}_{\theta\left(N^{*}, 2 k / n+1-\delta\right)}\right)
\end{aligned}$$
The correction terms of Lim [30] and Mrowka-Ruberman-Saveliev [39] in the product end case are, respectively,
$$c\left(Y, g_{L}, \beta_{\delta}\right)=\frac{1}{2} \eta\left(\mathcal{D}_{\theta(Y)}\right)+\frac{1}{8} \eta_{\operatorname{sign}}(Y)$$
and
$$w(X, g, \beta)=\frac{1}{2} \eta\left(\mathcal{D}_{\theta(\Sigma)}\right)+\frac{1}{8} \eta_{\operatorname{sign}}(\Sigma) .$$

It follows from Corollary 3.4 and Corollary 4.3 that there is a constant $C$, which is independent of $Y, \Sigma, N, K, L$ but may depend on $\delta$ such that
$$\begin{aligned}
w(X, g, \beta)=n \cdot c\left(Y, g_{L}, \beta_{\delta}\right)+\sum_{k=0}^{n-1} & \operatorname{SF}\left(\mathcal{D}_{\theta\left(N^{*}, 1-\delta\right)}, \mathcal{D}_{\theta\left(N^{*}, 2 k / n+1-\delta\right)}\right) \\
& -\frac{1}{8} \sum_{k=0}^{n-1} \operatorname{sign}_{k / n}(K)+C+o(1) .
\end{aligned}$$
Combining formulas (15) and (16) with the Lim formula [30] for the Casson invariant, $-\lambda(Y)=\# \mathcal{M}^{\text {irr }}\left(Y, g_{L}, \beta_{\delta}\right)+c\left(Y, g_{L}, \beta_{\delta}\right)$, we obtain ${ }^{1}$
$$\begin{aligned}
\lambda_{\mathrm{SW}}(X)=\# \mathcal{M}^{\mathrm{irr}}(X, g, \beta)+w & (X, g, \beta) \\
& =-n \cdot \lambda(Y)-\frac{1}{8} \cdot \sum_{m} \operatorname{sign}_{m / n}(K)+C+o(1) .
\end{aligned}$$
Since $\lambda_{\mathrm{SW}}(X), \lambda(Y), \operatorname{sign}_{k / n}(K)$ are metric independent and $C$ is independent of $L$, by passing to the limit as $L \rightarrow \infty$, we obtain the formula
$$\lambda_{\mathrm{SW}}(X)=-n \cdot \lambda(Y)-\frac{1}{8} \cdot \sum_{m} \operatorname{sign}_{m / n}(K)+C$$
which further implies that $C$ is a truly universal constant (independent, in particular, of $Y, K$, and $\delta$ ). By applying this formula to $Y=S^{3}$ and an unknot $K$, we conclude that $C=0$. This finishes the proof.

\section*{6. Computing the Furuta-Ohta invariant}

Let as before $K$ be a knot in an integral homology sphere $Y$, and $\Sigma$ the $n$-fold cyclic cover of $Y$ with branch set $K$ for $n \geqslant 2$. We continue to assume that $\Sigma$ is a rational homology sphere. It comes equipped with the covering translation $\tau: \Sigma \rightarrow \Sigma$ which is an orientation preserving diffeomorphism of order $n$. The mapping torus of $\tau$ is the smooth 4-manifold $X=([0,1] \times \Sigma) /(0, x) \sim(1, \tau(x))$ with the product orientation.

Proposition 6.1. The manifold $X$ has the integral homology of $S^{1} \times S^{3}$.
Proof. Let $N$ be the knot $K$ exterior, $N_{n} \rightarrow N$ the $n$-fold cyclic cover of $N$, and $N_{\infty} \rightarrow N$ its infinite cyclic cover. Denote by $\tau: N_{\infty} \rightarrow N_{\infty}$ the covering

\footnotetext{
${ }^{1}$ Our orientation conventions differ from those of Lim [31], hence the Casson invariant $\lambda(Y)$ shows up with the negative sign. This is the same issue we dealt in [43, Section 7].
}
translation; it descends to the covering translations $\tau: N_{n} \rightarrow N_{n}$ and $\tau: \Sigma \rightarrow \Sigma$. It follows from the Wang exact sequence
$$\ldots \longrightarrow H_{1}(\Sigma) \xrightarrow{\tau_{*}-1} H_{1}(\Sigma) \longrightarrow H_{1}(X) \longrightarrow H_{0}(\Sigma)=\mathbb{Z} \xrightarrow{\tau_{*}-1} H_{0}(\Sigma)=\mathbb{Z}$$
that all we need to prove is to show that $\tau_{*}-1: H_{1}(\Sigma) \rightarrow H_{1}(\Sigma)$ is surjective. To this end, choose a Seifert surface for $K$ and a basis for its first homology yielding the $2 h \times 2 h$ Seifert matrix $V$. Then we have the following presentations [8, Theorem 8.8 and Proposition 8.20] for the first homology of $N_{\infty}$ and $\Sigma$ as modules over, respectively, $\mathbb{Z}\left[t, t^{-1}\right]$ and $\mathbb{Z}[\mathbb{Z} / n]$ :
$$\begin{aligned}
H_{1}\left(N_{\infty}\right) & =\left(\mathbb{Z}\left[t, t^{-1}\right]\right)^{2 h} /\left(V^{\top}-t V\right), \\
H_{1}(\Sigma) & =(\mathbb{Z}[\mathbb{Z} / n])^{2 h} /\left(V^{\top}-t V\right) .
\end{aligned}$$
It is a standard fact [29] that $\tau_{*}-1: H_{1}\left(N_{\infty}\right) \rightarrow H_{1}\left(N_{\infty}\right)$ is an isomorphism. Writing $\pi$ for the projection homomorphism
$$\pi: \mathbb{Z}\left[t, t^{-1}\right] \longrightarrow \mathbb{Z}\left[t, t^{-1}\right] /\left(t^{n}-1\right)=\mathbb{Z}[\mathbb{Z} / n],$$
we obtain a commutative diagram
![](https://cdn.mathpix.com/cropped/84d2ee83-4f0d-43cc-9189-269418503996-23.jpg?height=235&width=632&top_left_y=1395&top_left_x=737)
which readily implies that the map $\tau_{*}-1: H_{1}(\Sigma) \rightarrow H_{1}(\Sigma)$ is surjective. \(\square\)

Corollary 6.2. The automorphism $\tau_{*}: H_{1}(\Sigma) \rightarrow H_{1}(\Sigma)$ has zero fixed point set.
Remark 6.3. The manifold $X$ has a unique spin ${ }^{c}$ structure. Its restriction to $\Sigma$ is the unique spin ${ }^{c}$ structure $\mathfrak{s}$ with the property $\tau_{*}(\mathfrak{s})=\mathfrak{s}$ which appears in the statement of Theorem A. This spin ${ }^{c}$ structure is in fact a spin structure, obtained by restricting to $\Sigma$ either of the two distinct spin structures on $X$; see the discussion at the beginning of Section 3.

The infinite cyclic cover $\tilde{X} \rightarrow X$, which is just the product $\mathbb{R} \times \Sigma$, has the rational homology of $S^{3}$, hence the conditions (3) are satisfied. According to [33, Section 7.1], the manifold $X$ has a well-defined Furuta-Ohta invariant,
$$\lambda_{\mathrm{FO}}(X)=\frac{1}{4} \# \mathcal{M}^{*}(X) \in \mathbb{Q},$$
where $\# \mathcal{M}^{*}(X)$ stands for the signed count of points in the (possibly perturbed) moduli space $\mathcal{M}^{*}(X)$ of irreducible ASD connections in a trivial $S U(2)$-bundle $E \rightarrow X$, with the signs determined by a choice of orientation and homology orientation on $X$. In this section, we will prove the following formula for this invariant.

Theorem 6.4. Let $\lambda(Y)$ be the Casson invariant of $Y$, and denote by $\operatorname{sign}_{m / n}(K)$ the Tristram-Levine equivariant signatures of the knot $K$. Then
$$\lambda_{\mathrm{FO}}(X)=n \cdot \lambda(Y)+\frac{1}{8} \cdot \sum_{m=1}^{n-1} \operatorname{sign}_{m / n}(K) .$$
This formula was proved in [14] and [45] under the assumption $\Sigma$ is an integral homology sphere, and in [33] under the assumption that $n=2$. Our proof here will rely on the extension of those techniques to the general case at hand.
6.1. Equivariant theory. We will first describe $\mathcal{M}^{*}(X)$ in terms of $\mathcal{R}(\Sigma)$, the $S U(2)$-character variety of $\pi_{1}(\Sigma)$. To this end, consider the splitting
$$\mathcal{R}(\Sigma)=\{\theta\} \sqcup \mathcal{R}_{\mathrm{ab}}(\Sigma) \sqcup \mathcal{R}_{\mathrm{irr}}(\Sigma),$$
whose three components consist of the trivial representation $\theta$ and the conjugacy classes of abelian (that is, non-trivial reducible) and irreducible representations, respectively. This decomposition is preserved by the map $\tau^{*}: \mathcal{R}(\Sigma) \rightarrow \mathcal{R}(\Sigma)$ induced by the covering translation. Denote by $\mathcal{R}^{\tau}(\Sigma)$ the fixed point set of the map $\tau^{*}$ acting on $\mathcal{R}(\Sigma) \backslash\{\theta\}=\mathcal{R}_{\text {ab }}(\Sigma) \sqcup \mathcal{R}_{\text {irr }}(\Sigma)$ so that
$$\mathcal{R}^{\tau}(\Sigma)=\mathcal{R}_{\mathrm{ab}}^{\tau}(\Sigma) \sqcup \mathcal{R}_{\mathrm{irr}}^{\tau}(\Sigma) .$$
The following algebraic lemma will allow us to obtain useful information about the action of $\tau^{*}$ on $\mathcal{R}_{\mathrm{ab}}(\Sigma)$.

Lemma 6.5. Let $G$ be a finite abelian group and $s: G \rightarrow G$ an automorphism with zero fixed point set. Then the induced automorphism $s^{*}: \operatorname{Hom}(G, U(1)) \rightarrow$ $\operatorname{Hom}(G, U(1))$ of the character group of $G$ has the trivial character as its only fixed point.

Proof. Let us consider the homomorphism $u: G \rightarrow G$ given by the formula $u(g)=$ $s(g)-g$. Since $s$ has zero fixed point set, $u$ is injective and, since $G$ is finite, $u$ is an isomorphism. This implies that $u^{*}$ is also an isomorphism, which completes the proof because $u^{*}(\chi)=s^{*}(\chi) \cdot \chi^{-1}$ on characters $\chi: G \rightarrow U(1)$. \(\square\)

The significance of the character group $\operatorname{Hom}\left(H_{1}(\Sigma), U(1)\right)$ to us is that its quotient by the equivalence relation identifying $\alpha$ with $\alpha^{-1}$ is precisely $\mathcal{R}_{\mathrm{ab}}(\Sigma)$. We call a character $\alpha \in \operatorname{Hom}\left(H_{1}(\Sigma), U(1)\right)$ central if the representation obtained by composing $\alpha$ with the inclusion of $U(1)$ in $S U(2)$ as a maximal torus is central; the latter simply means that the image of $\alpha$ is contained in $\{ \pm 1\} \subset U(1)$.

Proposition 6.6. The fixed point set $\mathcal{R}_{\mathrm{ab}}^{\tau}(\Sigma)$ consists of the equivalence classes of non-central characters $\alpha \in \operatorname{Hom}\left(H_{1}(\Sigma), U(1)\right)$ such that $\tau^{*} \alpha=\alpha^{-1}$. In particular, $\mathcal{R}_{\mathrm{ab}}^{\tau}(\Sigma)$ is empty for odd $n$, and $\mathcal{R}_{\mathrm{ab}}^{\tau}(\Sigma)=\mathcal{R}_{\mathrm{ab}}(\Sigma)$ for $n=2$.

Proof. A character $\alpha$ gives rise to a point in $\mathcal{R}_{\mathrm{ab}}^{\tau}(\Sigma)$ if and only if $\tau^{*} \alpha=\alpha$ or $\tau^{*} \alpha=\alpha^{-1}$. The former only occurs for the trivial character by Lemma 6.5. For a central character $\alpha$, the condition $\tau^{*} \alpha=\alpha^{-1}$ is equivalent to $\tau^{*} \alpha=\alpha$ hence $\alpha$ is again trivial. If $n$ is odd, it follows that $\alpha=\alpha^{-1}$ so $\alpha$ is central and hence trivial. If $n=2$, it follows from Lemma 6.5 that $\tau^{*}$ acts as the negative identity on the character group and therefore as the identity on $\mathcal{R}_{\mathrm{ab}}(\Sigma)$. \(\square\)

Proposition 6.7. Let $i: \Sigma \rightarrow X$ be the inclusion map given by the formula $i(x)=[0, x]$. Then the induced map
$$i^{*}: \mathcal{M}^{*}(X) \rightarrow \mathcal{R}^{\tau}(\Sigma)$$
is well-defined, and is a one-to-one correspondence over $\mathcal{R}_{\mathrm{ab}}^{\tau}(\Sigma)$ and a two-to-one correspondence over $\mathcal{R}_{\text {irr }}^{\tau}(\Sigma)$.

Proof. The natural projection $X \rightarrow S^{1}$ is a locally trivial bundle whose homotopy exact sequence
$$0 \longrightarrow \pi_{1}(\Sigma) \longrightarrow \pi_{1}(X) \longrightarrow \mathbb{Z} \longrightarrow 0$$
splits, making $\pi_{1}(X)$ into a semi-direct product of $\pi_{1}(\Sigma)$ and $\mathbb{Z}$. Let $t$ be a generator of $\mathbb{Z}$ then every representation $A: \pi_{1}(X) \rightarrow S U(2)$ determines and is uniquely determined by the pair $(\alpha, u)$ where $u=A(t)$ and $\alpha=i^{*} A: \pi_{1}(\Sigma) \rightarrow S U(2)$ is a representation such that $\tau^{*} \alpha=u \alpha u^{-1}$. In particular, the conjugacy class of $\alpha$ is fixed by $\tau^{*}$.

If $\alpha$ is trivial, $A$ must be reducible. If $\alpha$ is non-trivial abelian, it cannot be central by Proposition 6.6. Given a non-central abelian $\alpha$, conjugate it to a representation whose image is in the group $U(1)$ of unit complex numbers in $S U(2)$. Then $\tau^{*} \alpha=$ $\alpha^{-1}$ by Proposition 6.6, hence $\alpha=i^{*} A$ with $u=A(t)$ in the circle $j \cdot U(1)$. In
particular, $A$ is irreducible and $u^{2}=-1$. Since any two elements of $j \cdot U(1)$ are conjugate to each other by a unit complex number, the map $i^{*}$ is a one-to-one correspondence over $\mathcal{R}_{\mathrm{ab}}^{\tau}(\Sigma)$. Finally, let $\alpha$ be an irreducible representation with the conjugacy class in $\mathcal{R}_{\text {irr }}^{\tau}(\Sigma)$. Then there is a unit quaternion $u$ such that $\tau^{*} \alpha=u \alpha u^{-1}$, and therefore $\alpha$ is in the image of $i^{*}$. Moreover, there are exactly two different choices of $u$ such that $\tau^{*} \alpha=u \alpha u^{-1}$ because if $u_{1} \alpha u_{1}^{-1}=u_{2} \alpha u_{2}^{-1}$ then $u_{1}= \pm u_{2}$ since $\alpha$ is irreducible. Therefore, the map $i^{*}$ is a two-to-one correspondence in this case. Also note that the irreducibility of $\alpha$ implies that $u^{n}= \pm 1$. \(\square\)

Remark 6.8. It follows from the above proof that the characters in $\mathcal{M}^{*}(X)$ that are mapped by $i^{*}$ to $\mathcal{R}_{\mathrm{ab}}^{\tau}(\Sigma)$ are binary dihedral, while those mapped to $\mathcal{R}_{\text {irr }}^{\tau}(\Sigma)$ are not.

The Zariski tangent space to $\mathcal{R}^{\tau}(\Sigma)$ at a point $[\alpha] \in \mathcal{R}^{\tau}(\Sigma)$ is the fixed point set of the map $\tau^{*}: T_{[\alpha]} \mathcal{R}(\Sigma) \rightarrow T_{[\alpha]} \mathcal{R}(\Sigma)$. Using an identification $T_{[\alpha]} \mathcal{R}(\Sigma)=$ $H^{1}(\Sigma, \operatorname{ad} \alpha)$ and the fact that $\tau^{*} \alpha=u \alpha u^{-1}$, this set can be described in cohomological terms as the fixed point set of the map
$$\operatorname{Ad} u \circ \tau^{*}: H^{1}(\Sigma, \operatorname{ad} \alpha) \rightarrow H^{1}(\Sigma, \operatorname{ad} \alpha) .$$
We call $\mathcal{R}^{\tau}(\Sigma)$ non-degenerate if the equivariant cohomology groups $H_{\tau}^{1}(\Sigma, \operatorname{ad} \alpha)=$ $\operatorname{Fix}\left(\operatorname{Ad} u \circ \tau^{*}: H^{1}(\Sigma, \operatorname{ad} \alpha) \rightarrow H^{1}(\Sigma, \operatorname{ad} \alpha)\right)$ vanish for all $[\alpha] \in \mathcal{R}^{\tau}(\Sigma)$. The moduli space $\mathcal{M}^{*}(X)$ is called non-degenerate if $\operatorname{coker}\left(d_{A}^{*} \oplus d_{A}^{+}\right)=0$ for all $[A] \in$ $\mathcal{M}^{*}(X)$. Since $\operatorname{ind}\left(d^{*} \oplus d_{A}^{+}\right)=\operatorname{dim} \mathcal{M}^{*}(X)=0$, this is equivalent to $\operatorname{ker}\left(d_{A}^{*} \oplus\right.$ $\left.d_{A}^{+}\right)=0$ and, since $A$ is flat and irreducible, to simply $H^{1}(X, \operatorname{ad} A)=0$.

Proposition 6.9. The moduli space $\mathcal{M}^{*}(X)$ is non-degenerate if and only if $\mathcal{R}^{\tau}(\Sigma)$ is non-degenerate.

Proof. The group $H^{1}(X, \operatorname{ad} A)$ can be computed with the help of the Leray-Serre spectral sequence of the fibration $X \rightarrow S^{1}$ with fiber $\Sigma$. The $E_{2}$-page of this spectral sequence is
$$E_{2}^{p q}=H^{p}\left(S^{1}, \mathcal{H}^{q}(\Sigma, \operatorname{ad} \alpha)\right),$$
where $\alpha=i^{*} A$ and $\mathcal{H}^{q}(\Sigma, \operatorname{ad} \alpha)$ is the local coefficient system associated with the fibration. The groups $E_{2}^{p q}$ vanish for all $p \geqslant 2$ hence the spectral sequence collapses at $E_{2}$-page, and
$$H^{1}(X, \operatorname{ad} A)=H^{1}\left(S^{1}, \mathcal{H}^{0}(\Sigma, \operatorname{ad} \alpha)\right) \oplus H^{0}\left(S^{1}, \mathcal{H}^{1}(\Sigma, \operatorname{ad} \alpha)\right) .$$