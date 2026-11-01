---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Bounds on Wahl singularitiesfrom symplectic topology]

---
source_file: 1708_02268v2.pdf
converter: mathpix
format: mmd
---

\title{
BOUNDS ON WAHL SINGULARITIES FROM SYMPLECTIC TOPOLOGY
}
by

\author{
Jonathan David Evans \& Ivan Smith
}

\begin{abstract}
Let $X$ be a minimal surface of general type with $p_{g}>0\left(b^{+}>1\right)$ and let $K^{2}$ be the square of its canonical class. Building on work of Khodorovskiy and Rana, we prove that if $X$ develops a Wahl singularity of length $\ell$ in a Q-Gorenstein degeneration, then $\ell \leq 4 K^{2}+7$. This improves on the current best-known upper bound due to Lee $\left(\ell \leq 400\left(K^{2}\right)^{4}\right)$. Our bound follows from a stronger theorem constraining symplectic embeddings of certain rational homology balls in surfaces of general type. In particular, we show that if the rational homology ball $B_{p, 1}$ embeds symplectically in a quintic surface, then $p \leq 12$, partially answering the symplectic version of a question of Kronheimer.
\end{abstract}

Keywords: Wahl singularities, surfaces of general type, rational homology balls, symplectic embeddings, Seiberg-Witten invariants. MSC 2000: 14J29, 53D35, 57R57.

\section*{1. Introduction}

A complex surface is said to have general type if its canonical bundle is big. The moduli space of surfaces of general type with fixed characteristic numbers $K^{2}$ and $\chi$ admits a compactification, constructed by Kollár and Shepherd-Barron, whose boundary points correspond to surfaces with semi-log-canonical (slc) singularities, in much the way that the boundary points of Deligne-Mumford space correspond to nodal curves. See [11] for a survey of these moduli spaces.

The fact that this moduli space is compact was proved by Alexeev [1], and is equivalent to the fact that there is a bound (in terms of $K^{2}$ and $\chi$ ) on the index of the slc singularities which appear at the boundary of the moduli space. A long-standing question is to give explicit and effective bounds on the possible indices in terms of

\footnotetext{
I.S. is partially supported by EPSRC Fellowship EP/N01815X/1.
J.E. is supported by EPSRC Standard Grant EPSRC Grant EP/P02095X/1.
}
the characteristic numbers. Existing upper bounds are much weaker than one would expect from the known examples.
In this paper, we focus on cyclic quotient singularities of type $\frac{1}{p^{2}}(p q-1,1)$ (Wahl singularities), and give a boundedness result via an approach from symplectic topology.

To state the result, we recall that the minimal resolution of the Wahl singularity $\frac{1}{p^{2}}(p q-1,1)$ has exceptional locus a chain of spheres $C_{1}, \ldots, C_{\ell}$ with negative squares $C_{i}^{2}=-b_{i}$, where
$$\frac{p^{2}}{p q-1}=b_{1}-\frac{1}{b_{2}-\frac{1}{b_{3}-\cdots}}$$
is a continued fraction expansion. The number $\ell$ is called the length of the singularity. The index of the singularity is $p$, and is bounded above by $2^{\ell}$.

Theorem 1.1. - Let $X$ be a minimal surface of general type with positive geometric genus $p_{g}>0$ which has a finite set of Du Val and Wahl singularities. Then the length $\ell$ of any of the Wahl singularities satisfies
$$\ell \leq 4 K_{X}^{2}+7 .$$

Remark 1.2. - The best bound for Wahl singularities we could find in the algebraic geometry literature ${ }^{(1)}$ is due to Lee [17, Theorem 23], who showed that if $X$ is a stable surface of general type having a Wahl singularity of length $\ell$, and if the minimal model $S$ of the minimal resolution $\widetilde{X}$ of $X$ has general type, then
$$\ell \leq 400\left(K_{X}^{2}\right)^{4} .$$
In another paper, Rana [33, Theorem 1.2] assumes further that the map $\widetilde{X} \rightarrow S$ involves blowing down exactly $\ell-1$ times and proves that, in this case, $\ell$ is either 2 or 3. She uses this to study the boundary of the Kollár-Shepherd-Barron-Alexeev (KSBA) moduli space for surfaces with $K^{2}=\chi=5$ (e.g. quintic surfaces).

Remark 1.3. - The hypothesis that $p_{g}>0$ (which is equivalent to $b^{+}(X)>1$ ) is there because our proof uses results from Seiberg-Witten theory and holomorphic curve theory which break down when $b^{+}(X)=1$ (or at least when the minimal model of $\widetilde{X}$ is rational or ruled). The hypothesis entails that the minimal model $S$ is neither rational nor ruled, but allows, for example, that $S$ is an elliptic surface of positive genus (see Remark 1.11 below for examples).

Theorem 1.1 is really a theorem about symplectic topology. The Wahl singularity $\frac{1}{p^{2}}(p q-1,1)$ admits a Q-Gorenstein smoothing whose smooth fibre is a symplectic rational homology ball $B_{p, q}$ [44]. In [14], Khodorovskiy conjectures that, for a surface $X$ of general type with $b^{+}>1$, there is a bound on $p$ (depending only on $K_{X}^{2}$ ) such that $B_{p, 1}$ embeds symplectically in $X$. What we prove is the following:

\footnotetext{
${ }^{(1)}$ After the first version of this paper was prepared, in June 2017, we learned that a very similar (slightly stronger, and optimal) result had been proved by Rana and Urzúa (see [34]). They use algebro-geometric rather than symplectic methods, so do not recover the purely symplectic Theorem 1.4 below. It is possible that their arguments can be used to strengthen our bounds.
}

Theorem 1.4 (Generalised Khodorovskiy conjecture). - Let $(X, \omega)$ be a symplectic 4-manifold with $K_{X}=[\omega]$ and $b^{+}(X)>1$. If there is a symplectic embedding $\iota: B_{p, q} \rightarrow X$, then
$$\ell \leq 4 K^{2}+7,$$
where $\ell$ is the length of the continued fraction expansion of $p^{2} /(p q-1)$. In the special case $p=n, q=1$ (when $\ell=n-1$ ) we get the stronger inequality:
$$\ell \leq 2 K^{2}+1 .$$

Remark 1.5. - To see how Theorem 1.1 follows from this, note that if $X$ is a minimal surface of general type then its canonical model is a symplectic orbifold with at worst Du Val singularities where the canonical map has contracted a collection of -2-spheres. A Du Val singularity can be smoothed symplectically by excising a neighbourhood of the singularity and replacing it with a copy of the Milnor fibre of the singularity. The Milnor fibre of a Du Val singularity is a symplectic manifold which deformation-retracts onto a configuration of Lagrangian spheres (the vanishing cycles). The result is a symplectic 4-manifold $(X, \omega)$ with $K_{X}=[\omega]$; see [36, Proposition 3.1] for more details. One can also smooth Wahl singularities symplectically, by replacing a neighbourhood of the singularity with a copy of the Milnor fibre $B_{p, q}$. Therefore if a surface of general type develops a Wahl singularity, one can find a symplectic 4-manifold diffeomorphic to $X$ with $K_{X}=[\omega]$, admitting a symplectic embedding of $B_{p, q}$.

For other papers which find obstructions to symplectic embeddings of rational homology balls, see [5, 20]. Theorem 1.4 could also be restated as a constraint on Lagrangian embeddings of pinwheels as in [5].

Remark 1.6. - Given a Q-Gorenstein degeneration $\mathcal{X} \rightarrow \Delta$ over the disc with central fibre $X_{0}$ of general type (so having ample canonical class) and having a Wahl singularity $1 / p^{2}(1, p q-1)$, one constructs the embedding $B_{p, q} \hookrightarrow X_{1}$ into the general fibre by symplectic parallel transport. If $X_{0}$ does not have ample canonical class, there is no global (orbifold) Kähler form in the class $K_{\mathcal{X}}$. In this case, one may need to perturb the (cohomology class of the) Kähler form in order to define parallel transport.

In [12], Hacking, Tevelev and Urzúa show that a surface of general type may admit degenerations in which infinitely many different Wahl singularities arise on the central fibre, where the central fibres are not ample (they are obtained by 3-fold flips from a $K$-ample degeneration). Translating back into the symplectic category, this implies that there are symplectic four-manifolds $X$ with the property that $K_{X}=[\omega]$, and an open neighbourhood $K_{X} \in U \subset H^{2}(X ; \mathbf{R})$, for which infinitely many rational balls $B_{p, q}$ admit symplectic embeddings into $\left(X, \omega_{s}\right)$ for some symplectic form with $\left[\omega_{s}\right] \in U$. (The parameter $s$ will depend on the particular rational ball; in the setting of the previous paragraph, it is determined by the geometry of the flip.) Thus,
not only is Theorem 1.4 an essentially symplectic rather than smooth phenomenon, but it is also sensitive to the cohomology class of the symplectic form ${ }^{(2)}$.

Remark 1.7. - In [14], Khodorovskiy uses techniques from Seiberg-Witten theory and holomorphic curves to get strong restrictions on the way in which -1-spheres can intersect the curves $C_{1}, \ldots, C_{\ell}$ in the minimal resolution. All of the techniques and ideas we use to prove Theorem 1.4 can be found in some form in Khodorovskiy's paper, and the structure of our case analysis is closely modelled on that in Rana's paper [33]. The key trick which makes our case analysis easier than in Rana's seems to be the fact that we can perturb the almost complex structure on the minimal resolution so that the only somewhere-injective holomorphic curves present are the curves $C_{1}, \ldots, C_{\ell}$ and a finite set of embedded -1-spheres.

Remark 1.8. - Theorem 1.4 is related to a question of Kronheimer [43, Problem 4.7], who asked: For which $p$ does $B_{p, 1}$ embed in the quintic surface? If you ask for the embedding to be symplectic, then from Theorem 1.4, we know that $p \leq 12$. Indeed, Theorem 1.4 applies to any surface of degree $d \geq 5$ in $\mathbf{C P}^{3}$, which has $K^{2}=d(d-4)^{2}$ and $p_{g}=\frac{d}{6}\left(d^{2}-6 d+11\right)-1$. Smooth embeddings of $B_{p, 1}$ into 4-manifolds are much more plentiful, see [16, 31].

Remark 1.9. - The projective plane contains $B_{p, q}$ for infinitely many $p$, cf. [5], so some hypotheses on the ambient manifold are certainly required to obtain a finiteness result.

Remark 1.10. - It is unfortunate that we need to make the restriction $b^{+}(X)>1$ (rather than just $K_{X}=[\omega]$ ) because huge numbers of examples have been constructed when $b^{+}=1$. See [37] for an impressive list. The original recipe for constructing examples like these is due to Park [32] and Lee and Park [18]: you blow up CP ${ }^{2}$ a large number of times, find a configuration of curves $C_{1}, \ldots, C_{\ell}$ combinatorially equivalent to the exceptional locus of the minimal resolution of a Wahl singularity $\frac{1}{p^{2}}(p q-1,1)$, then contract and smooth to get a surface of general type with $b^{+}=1$ containing a symplectic embedding of $B_{p, q}$. It seems that it would require new ideas to prove a bound when $b^{+}=1$. The key input which fails when $b^{+}=1$ is Corollary 2.2 This is more than a technical issue: for a startling illustration of the geometric ramifications of this failure, see Remark 2.14

Remark 1.11. - Happily, there are examples of Wahl singularities of type $\frac{1}{n-2}(n-$ 3,1) in Horikawa surfaces $H(n)$ (again due to Lee and Park [19]) where the minimal model of the minimal resolution is an elliptic surface $E(n)$. In particular, these satisfy $b^{+}(H(n))=2 n-1$ and $K_{H(n)}^{2}=4 n-6$, so in this case the length $\ell=n-1$ is $\frac{1}{4}\left(K^{2}+2\right)$. In particular, we see that the best we can hope for is a bound which is linear in $K^{2}$. These examples are particularly interesting: the KSBA stable surface whose smoothing is $H(n)$ has two Wahl singularities of type $\frac{1}{n-2}(n-3,1)$ and they

\footnotetext{
${ }^{(2)}$ Added in proof: The recent paper [6] uses these ideas to find a single non-monotone symplectic form on a quintic surface which admits infinitely many symplectically embedded rational balls $B_{p, q}$ with $p$ unbounded.
}
cannot be smoothed independently of one another, because the surface obtained by smoothing one and resolving the other violates the Noether inequality (see [8, Corollary 7.5]). This shows one big advantage of the symplectic approach to bounding singularities: we can always rationally blow-down one of the singularities and bound the singularities one at a time.

Remark 1.12. - The rational homology balls $B_{p, q}$ have played a prominent role in low-dimensional topology since the papers of Fintushel and Stern [8, 9, 10], where they have been used to construct exotic 4-manifolds with small Betti numbers, starting with the paper [32].
1.1. Structure of the paper. - In Section 2, we introduce the tools that we will use in the rest of the paper. The key result is Corollary 2.2, which uses Seiberg-Witten theory to rule out the existence of certain holomorphic rational curves in symplectic manifolds with $b^{+}>1$. This is used in Sections 2.2-2.4 to prove results about limits of sequences of holomorphically embedded -1-spheres under Gromov compactness, and in Section 2.5 to find constraints on how other rational curves can intersect these limits when $b^{+}>1$.

In Section 3, we remind the reader about the basic properties of Wahl singularities and their minimal resolutions.

In Section 4, we define a class of almost complex structures on the minimal resolution for which the only irregular holomorphic curves are contained in a neighbourhood of the exceptional locus $\mathcal{C}$ of the minimal resolution.

In Section 5, we recall the topological description of the discrepancies of the minimal resolution, and use this to find a constraint on the way holomorphic -1-spheres can intersect $\mathcal{C}$ (Theorem 5.5).

In Sections 6-8, we complete the case analysis required to prove our inequality. The idea of the proof is that the blow-down map $\widetilde{X} \rightarrow S$ from the minimal resolution to its minimal model must contain at least $\ell-K^{2}$ exceptional curves. We show that (roughly) at least half of the exceptional curves $E$ have $E \cdot \mathcal{C} \geq 2$ ("good curves") and the rest of the exceptional curves have $E \cdot \mathcal{C}=1$ ("bad curves"). Once we prove that $\sum_{E} E \cdot \mathcal{C} \leq \ell+1$, this implies the desired inequality. This part of the argument is modelled heavily on Rana's paper [33, Lemmas 2.8 and 2.9].

In Section 9, we explain how in certain special cases, one can prove that all curves are good, which gives an improved inequality.
1.2. Acknowledgements. - The authors would like to thank: Weiyi Zhang for extremely helpful discussions about how -1-spheres can degenerate under Gromov compactness - see Remark 2.14 - and how our paper might generalise beyond the $p_{g}>0$ setting; Paul Hacking for useful comments and for making us aware of the ongoing work of Rana and Urzúa; Julie Rana and Giancarlo Urzúa for constructive
discussions once we learned about their work [34]; and the anonymous referee for their comments.

\section*{2. Rational curves and blowing down}

We begin by reviewing some theorems about rational holomorphic curves and exceptional curves in symplectic 4-manifolds with $b^{+}>1$. The main result here is Corollary 2.2, which will be the main technical tool later in the paper.
2.1. Rational curves. - A complex line bundle $L \rightarrow X$ on a smooth four-manifold $X$ is called characteristic if $c_{1}(L)$ is an integer lift of $w_{2}(X)$. Note that if $L$ is characteristic, then (using additive notation for line bundles as for divisors) $L+2 L^{\prime}$ is characteristic, for any $L^{\prime}$.

Theorem 2.1 (Fintushel and Stern, [7, Theorem 1.3]). - Let $X$ be a smooth 4-manifold with $b^{+}(X)>1$ and write $\sigma(X)$ for the signature of $X$ and $e(X)$ for the Euler characteristic of $X$. Let $L$ be a characteristic line bundle on $X$ with nonvanishing Seiberg-Witten invariant $S W_{X}(L) \neq 0$; we will also write $L$ for the first Chern class of $L$. Suppose that the virtual dimension
$$\operatorname{dim} \mathcal{M}_{X}(L)=\frac{1}{4}\left(L^{2}-(3 \sigma(X)+2 e(X))\right)$$
of the moduli space of solutions to the Seiberg-Witten equations can be written as $\sum \ell_{i}\left(\ell_{i}+1\right)$ for some collection of nonnegative integers $\ell_{1}, \ldots, \ell_{r}$. If a nonzero homology class $A$ can be represented by an immersed sphere with $p$ positive double points then either:
$$2 p-2 \geq \begin{cases}A^{2}+|L \cdot A|+4 \sum_{i=1}^{r} \ell_{i}, & p \geq r \\ A^{2}+|L \cdot A|+4 \sum_{i=1}^{p} \ell_{i}+2 \sum_{i=p+1}^{r} \ell_{i}, & p>r\end{cases}$$
or
$$S W_{X}(L)= \begin{cases}S W_{X}(L+2 A), & A \cdot L \geq 0 \\ S W_{X}(L-2 A), & A \cdot L \leq 0 .\end{cases}$$
We will use Theorem 2.1 to prove the following result, for which we could not find a proof in the literature:

Corollary 2.2. - Let $(X, J)$ be an almost complex 4-manifold with $b^{+}(X)>1$ and suppose that the canonical class $K$ associated to $J$ has $S W(K) \neq 0$ (for example, this holds if $J$ is homotopic to an $\omega$-tame almost complex structure for some symplectic form $\omega$ on $X$ ). Suppose that $u: S^{2} \rightarrow X$ is a somewhere-injective $J$-holomorphic curve representing a homology class $A$. If $K \cdot A \leq-1$ then $A^{2}=-1, K \cdot A=-1$. In this case, by the adjunction formula, $u$ is an embedding.

Proof. - The adjunction formula [25, Theorem 1.3], [27, Theorem 2.2.1] tells us that
$$A^{2}+2+K \cdot A \geq 0$$
with equality if and only if $u$ is an embedding. If $K \cdot A \leq-1$ then this means $A^{2} \geq-1$ with equality if and only if $K \cdot A=-1$ and $u$ is an embedding. Henceforth we will assume that $A^{2} \geq 0, K \cdot A \leq-1$ and derive a contradiction.

We will prove by induction on $m$ that:
$$S W_{X}(K-2 m A) \neq 0 \text { for all nonnegative integers } m \text {. }$$
This will give a contradiction, since the set of cohomology classes with nonvanishing Seiberg-Witten invariant is finite [45, Section 3]. The base case $m=0$ holds by assumption. The fact that this holds whenever $J$ is homotopic to an $\omega$-tame almost complex structure for some symplectic form $\omega$ is a result of Taubes [40, Main Theorem]. We now assume that $S W_{X}(K-2 m A) \neq 0$.

By [25, Proposition 1.2] or [27, Theorem 4.1.1], there is a homotopic $J^{\prime}$ and a $\mathcal{C}^{\infty}$ - small perturbation $u^{\prime}$ of $u$ such that $u^{\prime}$ is a $J^{\prime}$-holomorphic immersion with positive transverse double points. Therefore, without loss of generality, we may assume that $u$ is an immersion with positive transverse double points. Let $p$ be the number of positive transverse double points of $u$. If we smooth the double points we find an embedded symplectic surface $\Sigma$ with genus $p$ in the homology class $A$; by the standard adjunction formula, we have $A^{2}+2-2 p=-K \cdot A$, or
$$2 p-2=A^{2}+K \cdot A .$$
We will apply Theorem 2.1 to $u$ with $L_{m}=K-2 m A$. We have
$$L_{m} \cdot A=K \cdot A-2 m A^{2}=-c_{1}(A)-2 m A^{2} \leq 0,$$
as we are assuming $K \cdot A \leq-1$ and $A^{2} \geq 0$. Theorem 2.1 then tells us that either $S W_{X}\left(L_{m+1}\right) \neq 0$ (which would complete the induction step) or
$$2 p-2 \geq A^{2}+\left|L_{m} \cdot A\right|+\text { nonnegative terms } \geq A^{2} .$$
However, from Equation (1), we know that $2 p-2=A^{2}+K \cdot A<A^{2}$. This completes the induction step. \(\square\)

Remark 2.3. - We observe the following result of Zhang [47]:
Lemma 2.4 ([47, Lemma 2.1]). - Let $(X, \omega)$ be a symplectic 4-manifold whose minimal model is neither rational nor ruled and let $J$ be an $\omega$-tame almost complex structure on $X$. If $C \subset X$ is a somewhere-injective holomorphic curve whose domain is a compact, connected Riemann surface and $K \cdot C<0$, then $C$ is an embedded sphere with self-intersection -1.

This also relies on Seiberg-Witten theory in an essential way, via result of Taubes [42] and Li-Liu [21] which prove existence of a $J$-holomorphic representative of twice the canonical class. It seems likely that one could use this lemma in our proof to replace the $b^{+}>1$ assumption by the weaker assumption that the minimal model of the minimal resolution is rational or ruled, however, there is one small technical hurdle (in the proof of Proposition 2.11) which currently requires us to work with non-tame almost complex structures.

If we assume that $X$ is a projective surface then Lemma 2.4 is a very classical result [3]. McDuff [26. Theorem 1.4] was the first to prove a symplectic version of this, under the stronger assumption that $K \cdot C<-1$.

A first (well-known) consequence of Corollary 2.2 is:
Lemma 2.5. - Let $(X, \omega)$ be a symplectic 4-manifold with $b^{+}(X)>1$. Suppose that $E_{1}$ and $E_{2}$ are homology classes in $H_{2}(X)$ which can be represented by embedded symplectic spheres, and suppose that $E_{1}^{2}=E_{2}^{2}=-1$. Then either $E_{1}=E_{2}$ or $E_{1} \cdot E_{2}=0$. Moreover, there are only finitely many Hamiltonian isotopy classes of symplectically embedded -1-spheres.

Proof. - The Gromov invariants of the class $E_{1}$ and of the class $E_{2}$ are both 1, so for a generic almost complex structure $J$, these classes can be represented by $J$ -holomorphic spheres $S_{1}$ and $S_{2}$ respectively. These spheres must either be identical or else disjoint: otherwise, we could blow $S_{1}$ down, and the image $S_{2}^{\prime}$ of $S_{2}$ under the blow-down would be a rational curve with $K \cdot S_{2}^{\prime}=K \cdot S_{2}-S_{1} \cdot S_{2}<-1$, contradicting Corollary 2.2 Therefore, $E_{1}=E_{2}$ or $E_{1} \cdot E_{2}=0$.

The finiteness statement is clear on the level of homology: there can be at most $b^{-}(X)$ pairwise orthogonal -1-classes in the homology of $X$. Moreover, if there are two homologous symplectically embedded -1-spheres $S_{1}$ and $S_{2}$, then we can pick a $J_{1}$ making $S_{1}$ holomorphic and a $J_{2}$ making $S_{2}$ holomorphic. A generic path $J_{t}$ connecting $J_{1}$ and $J_{2}$ in the space of compatible almost complex structures will avoid the codimension 2 locus where the spheres in this class bubble, and the unique $J_{t}$-holomorphic sphere $S_{t}$ in this homology class traces out a Hamiltonian isotopy connecting $S_{1}$ and $S_{2}$. Therefore there are only finitely many Hamiltonian isotopy classes of symplectically embedded -1-spheres. \(\square\)

Remark 2.6. - All of the facts proved here will fail if the surface is rational (except finiteness of the number of -1-classes if the surface is Del Pezzo).
2.2. Exceptional curves of the first kind. - In this subsection, we review some basic material about birational maps of complex surfaces, and extend the theory to handle symplectic 4-manifolds.

Definition 2.7. - An exceptional curve of the first kind in a complex surface $X$ is a (possibly reducible, nonreduced) divisor $E$ for which there is a holomorphic birational map $\pi: X \rightarrow Y$ to a smooth complex surface $Y$ and a point $p \in Y$ such that $\pi^{-1}(p)=E$.

An embedded sphere $E$ with $E^{2}=-1$ (or, equivalently, $K \cdot E=-1$ ) is an exceptional curve of the first kind. Any irreducible exceptional curve of the first kind has this form. Any exceptional curve of the first kind with $m$ irreducible components can be obtained by taking an exceptional curve of the first kind with $m-1$ irreducible components, blowing up a point on the curve, and taking the total transform.

Here are some examples. In each, we will represent the exceptional curve by drawing a graph with a vertex for each irreducible component; we label the vertex associated to the component $C$ with the integer $K \cdot C$. We also write the name of the component and its multiplicity above the vertex.

Example 2.8. - We start with a -1-sphere $E$. We will denote the proper transform of a curve $C$ under a blow-up by $\widetilde{C}$.
\begin{itemize}
\item[(1)] Blow-up a point on $E$ and take total transform to get a curve:
![](https://cdn.mathpix.com/cropped/d0185d7b-b1ff-418a-8e7d-246058910b7a-09.jpg?height=103&width=150&top_left_y=845&top_left_x=1429)
\item[(2)] Blow-up a point $p$ on the previous example. Let $F_{1}$ be the new -1-sphere, let $F_{1}=\widetilde{E}_{2}$ and $F_{3}=\widetilde{E}_{2}$. There are three possibilities:
$$p \in E_{1}, p \notin E_{2}$$
$$p \notin E_{1}, p \in E_{2}$$
$$p \in E_{1} \cap E_{2}$$
![](https://cdn.mathpix.com/cropped/d0185d7b-b1ff-418a-8e7d-246058910b7a-09.jpg?height=104&width=245&top_left_y=1095&top_left_x=966)
\item[] ![](https://cdn.mathpix.com/cropped/d0185d7b-b1ff-418a-8e7d-246058910b7a-09.jpg?height=105&width=247&top_left_y=1217&top_left_x=966)
\item[] The following properties of exceptional curves of the first kind are easy to prove by induction on the number of components of the curve. For a full treatment of exceptional curves of the first kind, see [2].
\end{itemize}

Theorem 2.9. — (1) Every irreducible component of an exceptional curve of the first kind $E$ is an embedded sphere with negative self-intersection number.
\begin{itemize}
\item[(2)] Any two irreducible components intersect at most once, transversely.
\item[(3)] If $G$ is the dual graph whose vertices correspond to irreducible components of $E$ and whose edges correspond to intersections between components, then $G$ is a connected tree.
\item[(4)] We can factor the blow-down map $\pi: X \rightarrow Y$ as a sequence
$$X=X_{1} \xrightarrow{\pi_{1}} X_{2} \xrightarrow{\pi_{2}} X_{3} \rightarrow \cdots \xrightarrow{\pi_{n}} X_{n+1}=Y$$
where each $\pi_{i}$ blows down one -1-sphere. Let $\Pi_{i}=\pi_{i} \circ \pi_{i-1} \circ \cdots \circ \pi_{1}$. We call $A_{i}$ the component of $E$ which is contracted by $\Pi_{i}$ but not $\Pi_{i-1}$. Then, for every $i$, there is at most one $j>i$ for which $A_{i} \cdot A_{j} \neq 0$.
\item[(5)] If we write $E=\sum_{i=1}^{n} m_{i} A_{i}$ then
$$m_{i}=\sum_{j<i} m_{j} A_{j} \cdot A_{i}$$
\end{itemize}
\begin{itemize}
\item[(6)] We have $E \cdot A_{i}=0$ for $i<n$ and $E \cdot A_{n}=-1$. In particular, $E \cdot \sum_{i=1}^{n} A_{i}=-1$.
\item[(7)] There is at least one -1-sphere amongst the irreducible components, and every -1-sphere component can intersect at most 2 other components.
\end{itemize}
2.3. Exceptional curves in symplectic manifolds. - In what follows, we use an analogue of exceptional curves of the first kind in symplectic topology.

Definition 2.10. - Let $(X, \omega)$ be a symplectic 4-manifold. Let $\Sigma$ be a nodal Riemann surface of genus zero and $u: \Sigma \rightarrow X$ be a continuous map from a nodal Riemann surface. We say that $u$ is an exceptional curve of the first kind if there exists:
\begin{itemize}
\item[-] a neighbourhood $M$ of $u(\Sigma)$ and an open neighbourhood $N$ of $0 \in \mathbf{C}^{2}$;
\item[-] an integrable complex structure $J$ on $M$ homotopic to an $\omega$-tame one;
\item[-] a holomorphic birational map $\pi: M \rightarrow N$;
\end{itemize}
such that $u$ is a $J$-holomorphic stable map and $\pi^{-1}(0)=u(\Sigma)$.
Proposition 2.11. - Suppose that $(X, \omega)$ is a symplectic 4-manifold with $b^{+}(X)>1$ and $J$ is an $\omega$-tame almost complex structure. If $u$ is a $J$-holomorphic stable map representing a homology class $E$ with $K \cdot E=-1$, and if $E$ can be represented by an embedded symplectic 2-sphere, then $u$ is an exceptional curve of the first kind.

Proof. - If $J$ is an arbitrary almost complex structure on $X$ and $u$ is $J$-holomorphic, then, by [35. Theorem 3], there exists another (homotopic, but not obviously tame ${ }^{(3)}$ ) almost complex structure $J^{\prime}$ for which $u$ is $J^{\prime}$-holomorphic and $J^{\prime}$ is integrable on a neighbourhood of the image of $u$. We may therefore assume without loss of generality that $J$ is integrable on a neighbourhood of $u(\Sigma)$.

We will prove the proposition by induction on the number of irreducible components of the image of $u$. The induction step involves blowing down existing -1-spheres. To blow-down, we use integrability of $J$ near the exceptional curve. We observe that Corollary 2.2 holds for $J$-curves in $X$ because $J$ is homotopic to a tame almost complex structure; it continues to hold for blow-downs because the blow-down formula for Seiberg-Witten invariants implies that the canonical class is still a Seiberg-Witten basic class.

Lemma 2.12 (cf [47, Corollary 2.10]). - If the image of $u$ has $n \geq 1$ components then one of them is an embedded -1-sphere $e$.

\footnotetext{
${ }^{(3)}$ If one could prove that Sikorav's result yields a tame complex structure then we could appeal to Lemma 2.4 instead of Corollary 2.2 and deduce all of our results in the more general setting that the minimal model is not rational or ruled. Added in proof: This improvement was recently made by Chen and Zhang 4. Appendix A].
}

Proof. - Let $A_{1}, \ldots, A_{n}$ be simple holomorphic curves underlying the irreducible components of the image of $u$ and $m_{1}, \ldots, m_{n}$ be the covering multiplicities, so that $E=\sum_{i=1}^{n} m_{i} A_{i}$. We have
$$-1=K \cdot E=\sum_{i=1}^{n} m_{i} K \cdot A_{i},$$
so at least one of the numbers $K \cdot A_{i}$ is negative. By Lemma 2.2, $A_{i}^{2}=-1$ and this component is an embedded -1-sphere. \(\square\)

We write $\pi: X \rightarrow X^{\prime}$ for the holomorphic map which blows down the curve $e$ produced by Lemma 2.12 After possibly adding marked points to the domain, the composition $\pi \circ u$ is a stable map representing a homology class $\pi_{*}(E)$.

If $E$ and $e$ are distinct classes then, by Lemma 2.5, they satisfy $E \cdot e=0$.
Lemma 2.13. - Either $\pi \circ u$ is constant or $K_{X^{\prime}} \cdot \pi_{*}(E)=-1$.
Proof. - Recall that $E=\sum_{i=1}^{n} m_{i} A_{i}$ and that one of the $A_{i}$, say $A_{1}$, is a class $e$ with $e^{2}=-1$. By Lemma 2.5, either $E=e$ or $E \cdot e=0$. If $E=e$ then $\pi \circ u$ is constant, so we may assume $E \cdot e=0$. Then:
$$0=E \cdot e=-m_{1}+\sum_{i=2}^{n} m_{i} A_{i} \cdot e$$
so $m_{1}=\sum_{i=2}^{n} m_{i} A_{i} \cdot e$. Moreover,
$$K_{X} \cdot E=m_{1} K_{X} \cdot e+\sum_{i=2}^{n} K_{X} \cdot A_{i},$$
so
$$-1=\sum_{n=2}^{n} m_{i}\left(A_{i} \cdot e+K_{X} \cdot A_{i}\right) .$$
The expression $K_{X} \cdot A_{i}+e \cdot A_{i}$ is equal to $K_{X^{\prime}} \cdot \pi_{*}\left(A_{i}\right)$. Therefore Equation (2) tells us that $K_{X^{\prime}} \cdot \pi_{*}(E)=-1$. \(\square\)

By induction, this implies that $u$ can be blown down to a point; therefore $u$ is an exceptional curve of the first kind. \(\square\)

Remark 2.14. — Proposition 2.11 fails if the minimal model is rational. We are grateful to Weiyi Zhang for pointing out the following wonderful example. Let $C$ be a rational plane quartic curve with three nodes. Blow up the three nodes, along with five other points on the curve. The proper transform of $C$ is an embedded symplectic -1-sphere in the homology class
$$E:=4 H-2 E_{1}-2 E_{2}-2 E_{3}-E_{4}-E_{5}-E_{6}-E_{7}-E_{8},$$
which satisfies $K \cdot E=-1$ and $E^{2}=-1$. However, for a nongeneric complex structure, this can be represented by a stable map which is not an exceptional curve of the
first kind: the arithmetic genus of the image is one. To see this, take a line $C_{1}$ and a conic $C_{2}$ which intersect at two points, and blow-up three points on the line and five on the conic. The proper transform of $2 C_{1}+C_{2}$ lives in the class $E$; it can be represented by a stable map whose domain has three components $a, b, c$ in a chain which map respectively to $C_{1}, C_{2}, C_{1}$. This is not an exceptional curve of the first kind; for example its components intersect one another twice. For many counter-intuitive examples of $J$-holomorphic subvarieties of rational surfaces, as well as some constraints for nef classes or certain ruled surfaces, we refer the interested reader to papers by Li-Zhang and Zhang [22, 47, 46].

\subsection*{2.4. Nesting of exceptional curves. -}

Definition 2.15. - If two exceptional curves of the first kind, $E_{1}$ and $E_{2}$, have the property that all of the components of $E_{1}$ are also components of $E_{2}$, then we say $E_{1} \subset E_{2}$, or that the classes are nested.

Proposition 2.16. - If $(X, \omega)$ is a symplectic manifold with $b^{+}(X)>1$ and two exceptional curves of the first kind $E_{1}, E_{2} \subset X$ share a component, then they are nested.

Proof. - Given a pair of exceptional curves of the first kind, $E_{1}, E_{2}$, having $N_{E_{1}}$, respectively $N_{E_{2}}$, components, define
$$M_{E_{1} E_{2}}=\max \left(N_{E_{1}}, N_{E_{2}}\right) .$$
If $M_{E_{1} E_{2}}=1$ then both $E_{1}$ and $E_{2}$ are irreducible, so, if they share a component, then they are certainly nested (indeed they are geometrically indistinct). Let us assume, as an induction hypothesis, that any pair of exceptional curves of the first kind $E_{1}$ and $E_{2}$ in any symplectic manifold $X$ with $b^{+}(X)>1$, which share a component and satisfy $M_{E_{1} E_{2}}<m$, are nested.

Let $E_{1}$ and $E_{2}$ be a pair of exceptional curves of the first kind with $M_{E_{1} E_{2}}=m$ and which share a component. Suppose for a contradiction that they are not nested. Then there exists a component $A \subset E_{1}$ which intersects $E_{2}$ but is not contained in it. This component cannot be a -1-sphere, as it would have positive intersection number with $E_{2}$, which would contradict Lemma 2.5 Therefore we can blow down all the -1-spheres in $E_{1}$ and $E_{2}$ to obtain a non-nested configuration $E_{1}^{\prime}, E_{2}^{\prime}$ with $M_{E_{1}^{\prime} E_{2}^{\prime}}<m$. This contradicts the induction hypothesis, so we deduce that $E_{1}$ and $E_{2}$ are nested. \(\square\)
2.5. Iterated blow-down of rational curves. - The following lemma will be useful in streamlining our arguments later. (Our convention in the figures is that a black box denotes a component of square -1.)

Lemma 2.17. - Let $(X, \omega)$ be a symplectic manifold with $b^{+}(X)>1$. Suppose that $E$ is an exceptional curve of the first kind which is just a chain of spheres $F_{1}, \ldots, F_{n}$ with a single -1 -sphere $F_{i}, i \in\{2, \ldots, n-1\}$. Suppose that $S$ is a rational curve which intersects $F_{i}$ once transversely and is disjoint from the other components of $E$. Then, after blowing down
$E$, the image $T$ of $S$ is a rational curve with $K \cdot T \leq K \cdot S-2(n-1)$. In particular, by Corollary 2.2 we have
$$n \leq \frac{1}{2}(K \cdot S+3) .$$
![](https://cdn.mathpix.com/cropped/d0185d7b-b1ff-418a-8e7d-246058910b7a-13.jpg?height=205&width=736&top_left_y=721&top_left_x=664)
Proof. - To simplify notation, we will begin by considering a special case. We take $i=2$, and suppose that $F_{3}, \ldots, F_{n}$ are all -2-spheres. As a diagram, labelling each vertex by $K \cdot F_{i}$, that means:
![](https://cdn.mathpix.com/cropped/d0185d7b-b1ff-418a-8e7d-246058910b7a-13.jpg?height=199&width=749&top_left_y=1164&top_left_x=659)
When we blow down $F_{2}$, we get the following diagram:
![](https://cdn.mathpix.com/cropped/d0185d7b-b1ff-418a-8e7d-246058910b7a-13.jpg?height=202&width=750&top_left_y=1517&top_left_x=658)
and when we blow down the next component, we get
![](https://cdn.mathpix.com/cropped/d0185d7b-b1ff-418a-8e7d-246058910b7a-13.jpg?height=202&width=750&top_left_y=1873&top_left_x=659)
where the double line indicates an intersection multiplicity of 2. After blowing down all the components $F_{2}, \ldots, F_{n}$, we are left with a single -1-sphere which intersects the blow-down $S^{\prime}$ of $S$ at this stage with multiplicity $n-1$. Moreover, $K \cdot S^{\prime}=$ $K \cdot S-(n-1)$. When we blow down the final -1 -sphere, since $S^{\prime}$ intersects it with multiplicity $n-1$, the resulting blowdown $T$ of $S^{\prime}$ has
$$K \cdot T=K \cdot S-2(n-1) .$$

Since $K \cdot T \geq-1$ by Corollary 2.2, we deduce
$$n \leq \frac{1}{2}(K \cdot S+3) .$$
In this special case, at every stage until the last, we were blowing down the component of $E$ to the right of the previous one. For any other exceptional curve $E$, we would occasionally need to shift direction and blow down the curve to the left. This only serves to make Inequality (3) stronger. To explain why, observe that:
\begin{itemize}
\item[-] Let $S^{(k)}$ denote the blow-down of $S$ at stage $k$ (i.e. when $k$ components of $E$ have been blown down). At each stage except the first and last, $S^{(k)}$ intersects precisely two of the remaining spheres in the chain (the two which were adjacent to the curve which was blown down at the previous stage). Let us call these $F_{L}^{(k)}$ and $F_{R}^{(k)}$ (for "left" and "right").
\item[-] One of these two spheres $F_{L}^{(k)}$ or $F_{R}^{(k)}$ is necessarily the next curve to be blown down, say without loss of generality $F_{L}^{(k)}$. After blowing down $F_{L}^{(k)}$, we have
$$\begin{aligned}
K \cdot S^{(k+1)} & =K \cdot S^{(k)}-F_{L}^{(k)} \cdot S^{(k)} \\
F_{L}^{(k+1)} \cdot S^{(k+1)} & =F_{L}^{(k)} \cdot S^{(k)}\left(\text { if } F_{L}^{(k+1)} \text { exists }\right) \\
F_{R}^{(k+1)} \cdot S^{(k+1)} & =\left(F_{L}^{(k)}+F_{R}^{(k)}\right) \cdot S^{(k)}
\end{aligned}$$
so the intersection number of $S^{(k)}$ with $F_{L}^{(k)}$ and $F_{R}^{(k)}$ increases by one each time, starting at one when $k=1$. We see that the maximum of the intersection number between $S^{(k)}$ and the remaining spheres in the chain is always at least $k$.
\item[-] Each blow-down therefore reduces $K \cdot S^{(k)}$ by at least one, and the final blow-down reduces it by at least $n-1$ because $S$ hits the final sphere with multiplicity at least $n-1$. Again, we deduce Inequality (3). \(\square\)
\end{itemize}

\section*{3. Basic notions}
3.1. Definitions. - In this section, we fix the notation for the rest of the paper.

Wahl singularities: Given coprime positive integers $p, q$, let $\boldsymbol{\mu}_{p^{2}}$ denote the group of $p^{2}$ th roots of unity and consider the action $\Gamma_{p, q}$ of $\boldsymbol{\mu}_{p^{2}}$ on $\mathbf{C}^{2}$ where a root $\mu$ acts as
$$\mu \cdot(x, y)=\left(\mu^{p q-1} x, \mu y\right) .$$
The cyclic quotient singularity $\mathbf{C}^{2} / \Gamma_{p, q}$ is called a Wahl singularity and is conventionally written $\frac{1}{p^{2}}(p q-1,1)$. It has the property that its Milnor fibre $B_{p, q}$ is a rational homology ball; here the Milnor fibre is a compact Stein domain obtained by taking a compact neighbourhood of the singularity and smoothing the singular point.

Let $\Sigma_{p, q}$ be the boundary of $B_{p, q}$; this is a contact hypersurface contactomorphic to $S^{3} / \Gamma_{p, q} \subset \mathbf{C}^{2} / \Gamma_{p, q}$.
$X, \hat{X}$ : Let $(X, \omega)$ be a symplectic manifold and suppose that there is a symplectic embedding $\iota: B_{p, q} \hookrightarrow X$. Let $\hat{X}$ denote the symplectic orbifold obtained by excising $\iota\left(B_{p, q}\right)$ from $X$ and replacing it with a neighbourhood of the singular point in $\mathbf{C}^{2} / \Gamma_{p, q}$. We will say that $\hat{X}$ is obtained from $X$ by collapsing the image of $\iota$.

The minimal resolution $\widetilde{X}$ : The singularity $\frac{1}{p^{2}}(p q-1,1)$ has a minimal resolution: if
$$\frac{p^{2}}{p q-1}=b_{1}-\frac{1}{b_{2}-\frac{1}{b_{3}-\cdots}}$$
is the continued fraction expansion of $p^{2} /(p q-1)$ then the exceptional divisor is a chain of spheres $C_{1}, \ldots, C_{\ell}$ where
$$C_{i} \cdot C_{j}= \begin{cases}1 & \text { if }|i-j|=1 \\ -b_{i} & \text { if } i=j \\ 0 & \text { otherwise. }\end{cases}$$
We call the number $\ell$ of spheres in this chain the length of the singularity. We will write $\mathcal{C}$ for the set $\left\{C_{1}, \ldots, C_{\ell}\right\}$. The process of collapsing the image of $\iota$ and then taking the minimal resolution makes sense purely symplectically [8, 38, 39, 15] and is called generalised rational blow-up. We denote the generalised rational blow-up of $X$ along $\iota$ by $\widetilde{X}$, and will usually just refer to this as the minimal resolution of $\hat{X}$. Note that it is only determined up to symplectic deformation equivalence: for instance, one has to choose the symplectic areas of the curves $C_{j}$.

The minimal model $S$ : While $\widetilde{X} \rightarrow \hat{X}$ is the minimal resolution (in the sense that its exceptional divisor contains no components which can be contracted smoothly), it may not be minimal (in the sense that it may contain exceptional curves of the first kind which are not contained in the exceptional divisor). Let $S$ be the symplectic minimal model of $\widetilde{X}$. By [24. Theorem 1.1(i)], $S$ is obtained from $\widetilde{X}$ by blowing down a maximal collection of disjoint embedded symplectic -1-spheres. Again, it is only determined up to symplectic deformation equivalence.

\subsection*{3.2. Combinatorics of Wahl singularities. -}

Definition 3.1. - We call a string $\left[b_{1}, \ldots, b_{\ell}\right]$ a $T$-string if it arises as $b_{j}=-C_{j}^{2}$ for the chain of spheres in the exceptional locus of the minimal resolution of a Wahl singularity.

Theorem 3.2. - Any $T$-string can be obtained from the string [4] (corresponding to $p=2$, $q=1)$ by a sequence of operations $L$ and $R$ :
$$L\left[b_{1}, \ldots, b_{\ell}\right]=\left[2, b_{1}, \ldots, b_{\ell-1}, b_{\ell}+1\right], R\left[b_{1}, \ldots, b_{\ell}\right] \quad=\left[b_{1}+1, b_{2}, \ldots, b_{\ell}, 2\right] .$$

Let us define $F(x, y)=x^{2} /(x y-1)$. If $b=\left[b_{1}, \ldots, b_{\ell}\right]$ is the continued fraction expansion of $F(p, q)$ then $L b$ is the continued fraction expansion of $F(p+q, q)$ and $R b$ is the continued fraction expansion of $F(p+(p-q), p-q)$.

Corollary 3.3. - If $\left[b_{1}, \ldots, b_{\ell}\right]$ is a $T$-string then
$$\sum_{j=1}^{\ell}\left(b_{j}-2\right)=\ell+1 .$$
Proof. - This is true in the base case [4] and is preserved by the operations $L$ and $R$, so is true for all T-strings. \(\square\)

\section*{4. Almost complex structures for irregular curves}

A version of the following result was proved by McDuff and Opshtein [28, Definitions 1.2.1, 2.2.1 and Lemma 2.2.3]. Because we require slightly more of our almost complex structures, we explain the proof here.

Lemma 4.1. - There exists a nonempty set $\mathcal{J}_{\text {reg }}(\mathcal{C}, \kappa)$ of $\omega$-tame almost complex structures $J$ on $\widetilde{X}$ with the following properties:
\begin{itemize}
\item[-] there is a neighbourhood $\nu$ of $\mathcal{C}$ on which $J$ is equal to the standard complex structure $J_{0}$ on the minimal resolution of the $\frac{1}{p^{2}}(p q-1,1)$ singularity. In particular, the symplectic spheres $C_{1}, \ldots, C_{\ell}$ are all $J$-holomorphic, and there is a $J$-holomorphic projection map $\rho: \nu \rightarrow \mathbf{C}^{2} / \Gamma_{p, q}$ which contracts these spheres to the origin and is injective elsewhere.
\item[-] the image of any nonconstant genus zero J-holomorphic curve D with $\int_{D} \omega<\kappa$ and $K \cdot D \geq 0$ is necessarily contained $C_{1} \cup \cdots \cup C_{\ell}$. Indeed, if $b^{+}(\widetilde{X})>1$, then the only embedded $J$-holomorphic spheres in $\widetilde{X}$ with energy less than $\kappa$ are $C_{1}, \ldots, C_{\ell}$ and possibly a finite collection of pairwise disjoint embedded -1-spheres.
\end{itemize}

Proof. - Fix the standard (integrable) complex structure $J_{0}$ on a neighbourhood $\nu$ of $C_{1} \cup \cdots \cup C_{\ell}$ and let $\rho: \nu \rightarrow \mathbf{C}^{2} / \Gamma_{p, q}$ denote the holomorphic map which contracts the curves $C_{i}$ to the point 0.

The next lemma follows immediately from the proof of [29, Proposition 3.2.1]:
Lemma 4.2. - Let $\mathcal{J}(\nu)$ denote the space of almost complex structures on $\widetilde{X}$ which agree with $J_{0}$ on $\nu$. There is a residual subset $\mathcal{J}_{\text {reg }}(\mathcal{C}, \kappa) \subset \mathcal{J}(\nu)$ such that for any $J \in \mathcal{J}_{\text {reg }}(\mathcal{C}, \kappa)$, any somewhere-injective irregular $J$-holomorphic sphere with energy less than $\kappa$ is contained in $\nu$.

In four dimensions, a sphere in the class $D$ is regular only if $K \cdot D \leq-1$ (otherwise the virtual dimension of its moduli space is negative). If $D$ is a $J$-holomorphic sphere with $K \cdot D \geq 0$ then the underlying somewhere-injective curve $D^{\prime}$ also has $K \cdot D^{\prime} \geq$

0 and is therefore irregular. Therefore if $J \in \mathcal{J}_{\text {reg }}(\mathcal{C}, \kappa)$ and $D$ is a $J$-sphere with $K \cdot D \geq 0$ and energy less than $\kappa$ then $D$ is contained in $\nu$.

If $D$ is any nonconstant $J$-holomorphic curve in $\widetilde{X}$ which is completely contained in $\nu$ then its image under $\rho$ is a holomorphic curve in $\mathbf{C}^{2} / \Gamma_{p, q}$, and is therefore constant, so $D \subset C_{1} \cup \cdots \cup C_{\ell}$ as required.

Suppose $b^{+}(\widetilde{X})>1$. If $D$ is a $J$-sphere in $\widetilde{X}$ with energy less than $\kappa$ then, by Corollary 2.2, either $D$ is an embedded -1-sphere (of which there is a finite collection and they are all pairwise disjoint, by Lemma 2.5) or else $K \cdot D \geq 0$ and by what we have proved so far, $D$ is one of the spheres $C_{1}, \ldots, C_{\ell}$. \(\square\)

\section*{5. Topological obstructions}
5.1. Discrepancies. - Consider the minimal resolution of the singularity $\frac{1}{p^{2}}(p q-$ 1, 1), with exceptional locus $C_{1}, \ldots, C_{\ell}$. Let $\widetilde{U}$ be a neighbourhood of the exceptional locus, and let $\Sigma$ be the boundary of $\widetilde{U}$. Alexander-Lefschetz duality tells us that
$$H^{2}(\widetilde{U} ; \mathbf{Q}) \cong H_{2}(\widetilde{U}, \Sigma ; \mathbf{Q}) \cong H_{2}(\widetilde{U} ; \mathbf{Q}),$$
as $H_{*}(\Sigma ; \mathbf{Q})$ is concentrated in degree zero. In particular, we can write $K_{\widetilde{U}}$ as a rational linear combination of the classes $C_{j}$, Poincaré-dual to the corresponding curves:
$$K_{\widetilde{U}}=\sum_{j=1}^{\ell} a_{j} C_{j} .$$
The coefficients $a_{j}$ are called the discrepancies of the singularities. Note that discrepancies will be rational (non-integer) numbers because, over $\mathbf{Z}$, the sublattice $H_{2}(\widetilde{U} ; \mathbf{Z}) \subset H_{2}(\widetilde{U}, \Sigma ; \mathbf{Z})$ has index $p^{2}$. We can calculate the discrepancies in terms of the T-string $\left[b_{1}, \ldots, b_{\ell}\right]$ by solving the system of simultaneous equations:
$$\begin{aligned}
b_{1}-2=K_{\widetilde{U}} \cdot C_{1} & =-a_{1} b_{1}+a_{2} \\
b_{2}-2=K_{\widetilde{U}} \cdot C_{2} & =a_{1}-a_{2} b_{2}+a_{3} \\
\vdots & \\
b_{\ell-1}-2=K_{\widetilde{U}} \cdot C_{\ell-1} & =a_{\ell-2}-a_{\ell-1} b_{\ell-1}+a_{\ell} \\
b_{\ell}=K_{\widetilde{U}} \cdot C_{\ell} & =a_{\ell-1}-a_{\ell} b_{\ell} .
\end{aligned}$$
For example, when $\ell=1$ and the T-string is [4], we get $a_{1}=-\frac{1}{2}$.
Note that this definition necessarily agrees with the usual algebro-geometric definition of discrepancies because, in both cases, the $a_{j}$ are determined by the simultaneous equations (4).

Wahl singularities are log terminal, which means that $a_{j} \in(-1,0)$ for all $j$. The discrepancies of Wahl singularities are discussed extensively in [13, 17], and from a more symplectic perspective in [30]. The only property we will use is the following:

Lemma 5.1 ([13, Corollary 3.2]). -
$$a_{1}+a_{\ell}=-1 .$$
5.2. Mayer-Vietoris. - Let $\iota: B_{p, q} \rightarrow X$ be a symplectic embedding, let $\hat{X}$ be the orbifold obtained by collapsing $\iota\left(B_{p, q}\right)$, and $\widetilde{X}$ be the minimal resolution of $\hat{X}$. As in the previous section, let $\widetilde{U}$ be a neighbourhood of the exceptional locus $\mathcal{C}=C_{1} \cup \ldots \cup$ $C_{\ell}$ of the resolution; let $V \subset \widetilde{X}$ be the complement of $\widetilde{U}$, and let $\Sigma$ be the interface between $\widetilde{U}$ and $V$. As the boundary of $\widetilde{U}$ is a rational homology sphere, the Mayer-Vietoris sequence for $\widetilde{X}=\widetilde{U} \cup V$ over $\mathbf{Q}$ gives
$$H^{2}(\widetilde{X} ; \mathbf{Q})=H^{2}(\widetilde{U} ; \mathbf{Q}) \oplus H^{2}(V ; \mathbf{Q}) .$$
In terms of this decomposition, we have
$$K_{\widetilde{X}}=\left(K_{\widetilde{U}}, K_{V}\right),$$
because the first Chern class is natural under pullbacks.
Lemma 5.2. - If $F$ is a cycle in $\widetilde{X}$, there is a (closed) cycle $F^{\prime}$ in $V$, obtained by multiplying $F$ by $p^{2}$, slicing it along $\Sigma$ and capping off the result, such that
$$\left(0, K_{V}\right) \cdot F=\frac{1}{p^{2}} K_{V} \cdot F^{\prime} .$$
Proof. - Consider the composition $\Phi$ of maps
$$H_{2}(\widetilde{X} ; \mathbf{Z}) \rightarrow H_{2}(\widetilde{X}, \widetilde{U} ; \mathbf{Z}) \cong H_{2}(V, \Sigma ; \mathbf{Z}) \rightarrow H_{1}(\Sigma ; \mathbf{Z}) .$$
Since $H_{1}(\Sigma ; \mathbf{Z})=\mathbf{Z} /\left(p^{2}\right)$, we see that $\Phi\left(p^{2} F\right)=0$. Let $s$ be the 1-cycle in $\Sigma$ which is the image of $p^{2} F$ under the chain-level version of $\Phi$. Pick a 2-chain $P$ in $\Sigma$ such that $\partial P=-s$. Now the chain $F^{\prime}=p^{2} F+P$ is a (closed, not relative) cycle in $V$. We have
$$K_{V} \cdot F=\frac{1}{p^{2}} K_{V} \cdot F^{\prime} .$$
To see that there is no contribution to the intersection pairing from the 2-chain $P$, note that, after multiplying both sides of the equality by $p^{2}$ to make the canonical bundle trivial and not just torsion in a neighbourhood of $\Sigma$, one could represent the canonical class $K_{V}$ by the first Chern form of a connection which was flat in a neighbourhood of $\Sigma$. \(\square\)

Assuming that the 1-cycle $s$ considered in the proof of Lemma 5.2 is a combination of Reeb orbits in $\Sigma$ for the standard contact form, we now explain how to choose the caps to have positive symplectic area. This will be used in Section 5.3 below to find restrictions on how certain holomorphic curves can intersect $\mathcal{C}$.

Lemma 5.3. - Let $\alpha$ be the standard contact form on $\Sigma$ and let $\gamma$ be a closed Reeb orbit for $\alpha$. The $p^{2}$-fold cover of $\gamma$ is the asymptote of a holomorphic disc in $\left(\mathbf{C}^{2} \backslash\{0\}\right) / \Gamma_{p, q}$.

Proof. - The Reeb orbits in the standard 3-sphere are in bijection with the possible slopes $[a: b]$ of complex lines in $\mathbf{C}^{2}$ : an affine complex line $a x+b y+c=0$ in $\mathbf{C}^{2}$ is asymptotic to the Reeb orbit corresponding to $[a: b]$. The action $\Gamma_{p, q}$ of $\boldsymbol{\mu}_{p^{2}}$ on $\mathbf{C}^{2}$ gives an action of $\boldsymbol{\mu}_{p^{2}}$ on the $\mathbf{C P}^{1}$ of Reeb orbits; for example, under this action, the points [ 1 : 0] and [0 : 1] each have stabiliser isomorphic to $\boldsymbol{\mu}_{p^{2}}$.

Reeb orbits $\gamma$ in the quotient $S^{3} / \Gamma_{p, q}$ are in correspondence with $\mathbf{C P}^{1} / \Gamma_{p, q}$. Let $\gamma$ be the Reeb orbit corresponding to $[a: b] \in \mathbf{C P}^{1} / \Gamma_{p, q}$. The complex line $a x+b y+c$ with $c \neq 0$ gives a holomorphic plane in $\left(\mathbf{C}^{2} \backslash\{0\}\right) / \Gamma_{p, q}$ which is asymptotic to the $\operatorname{Stab}([a: b])$-fold cover of $\gamma$. If we let $m=p^{2} / \operatorname{Stab}([a: b])$ and precompose the plane with the $m$-fold branched cover $\mathbf{C} \rightarrow \mathbf{C}, z \mapsto z^{m}$, then we get a holomorphic plane asymptotic to $p^{2}$ times the Reeb orbit $\gamma$, as required. \(\square\)

\subsection*{5.3. Negative monotonicity. -}

Lemma 5.4. - Suppose that $(X, \omega)$ is a negatively monotone symplectic manifold, that is (after possibly rescaling the symplectic form) $K_{X}=[\omega]$. Let $\iota: B_{p, q} \rightarrow X$ be a symplectic embedding, let $\hat{X}$ be the orbifold obtained by collapsing $\iota\left(B_{p, q}\right)$, and $\rho: \widetilde{X} \rightarrow \hat{X}$ be the minimal resolution of $\hat{X}$. Let $J \in \mathcal{J}_{\text {reg }}(\mathcal{C}, \kappa)$. If $F \subset \widetilde{X}$ is a $J$-holomorphic curve such that $\rho(F)$ is nonconstant then $K_{V} \cdot F>0$.

Proof. - Since $J$ is standard on a neighbourhood of $\mathcal{C}$, there is an almost complex structure $\hat{J}$ on $\hat{X}$ obtained by contracting $\mathcal{C}$ to the singular point $p$, and a holomorphic map $\rho: \widetilde{X} \rightarrow \hat{X}$. If $R$ is a Riemann surface and $u: R \rightarrow \widetilde{X}$ is a $J$-holomorphic curve in $\widetilde{X}$ then $\rho \circ u$ is a $\hat{J}$-holomorphic curve in $\hat{X}$. Let $Z=(\rho \circ u)^{-1}(p)$. The curve $\left.\rho \circ u\right|_{R \backslash Z}$ is a punctured holomorphic curve in a noncompact symplectic manifold where the noncompact end is modelled on a punctured neighbourhood of $0 \in \mathbf{C}^{2} / \Gamma_{p, q}$. This means that the punctures of $\left.\rho \circ u\right|_{R \backslash Z}$ are asymptotic to covers of Reeb orbits for the standard contact form on $\Sigma$. Let $\phi: R^{\prime} \rightarrow R$ be an $N$-fold branched cover such that each point $z \in Z$ is a branch point with multiplicity $p^{2}$ (there may also be other branch points and $R^{\prime}$ may have higher genus than $R$ ). Let $Z^{\prime}=\phi^{-1}(Z)$. Now $\left.\rho \circ u \circ \phi\right|_{R^{\prime} \backslash Z^{\prime}}$ is a punctured holomorphic curve which is asymptotic to covers of Reeb orbits where the covering multiplicity is a multiple of $p^{2}$. Now, just topologically, glue $\left.\rho \circ u \circ \phi\right|_{R^{\prime} \backslash Z^{\prime}}$ to the holomorphic planar caps constructed in Lemma 5.3. We get a topological surface with positive area in $V=\hat{X} \backslash\{p\}$ which is homologous to $N[u]$. \(\square\)

Theorem 5.5. - Suppose that $K_{X}=[\omega]$. If $J \in \mathcal{J}_{\text {reg }}(\mathcal{C}, \kappa)$ and $F \subset \widetilde{X}$ is a $J$-holomorphic curve then
$$\sum_{j=1}^{\ell} a_{j} F \cdot C_{j}<K_{\widetilde{X}} \cdot F .$$
If $K_{\widetilde{X}} \cdot F=-1$ (for example, if $F$ is an embedded symplectic -1-sphere) then the following intersection patterns between $F$ and the $C_{j}$ curves cannot occur:
\begin{itemize}
\item[(1)] $F \cdot C_{j}=0$ for all $j \neq j_{0}$ and $F \cdot C_{j_{0}}=1$.
\item[(2)] $F \cdot C_{1}=F \cdot C_{\ell}=1$ and $F \cdot C_{j}=0$ for $j \notin\{2, \ldots, \ell-1\}$.
\end{itemize}

Proof. - Since $\rho(F)$ is a nonconstant holomorphic curve in $\hat{X}$, Lemma 5.4 tell us that $K_{V} \cdot F>0$. Therefore,
$$0<K_{V} \cdot F=K_{\widetilde{X}} \cdot F-\sum_{j=1}^{\ell} a_{j} C_{j} \cdot F$$
This tells us that
$$\sum_{j=1}^{\ell} a_{j} F \cdot C_{j}<K_{\widetilde{X}} \cdot F .$$
Now suppose that $K_{\widetilde{X}} \cdot F=-1$.
\begin{itemize}
\item[(1)] If $F \cdot C_{j}=0$ for all $j \neq j_{0}$ and $F \cdot C_{j_{0}}=1$ then Equation (5) implies
$$-1<a_{j_{0}}<K_{\widetilde{X}} \cdot F=-1,$$
(using Lemma 5.1) which gives a contradiction.
\item[(2)] If $F \cdot C_{1}=F \cdot C_{\ell}=1$ and $F \cdot C_{j}=0$ for $j \in\{2, \ldots, \ell-1\}$ then Equation (5) implies (using Lemma 5.1)
$$-1=a_{1}+a_{\ell}<K_{\widetilde{X}} \cdot F=-1,$$
which, again, gives a contradiction.
\end{itemize} \(\square\)

\section*{6. Exceptional spheres and their limits}

Let $S_{1}, \ldots, S_{k}$ be a maximal set of pairwise disjoint embedded symplectic -1-spheres in $\widetilde{X}$ and let $E_{i}=\left[S_{i}\right]$. Since $b^{+}(\widetilde{X})>1$, Lemma 2.5 tells us that there is a unique such set up to Hamiltonian isotopy and it contains one symplectic -1-sphere from every possible isotopy class. Let $\mathcal{E}=\left\{E_{1}, \ldots, E_{k}\right\}$.

Theorem 6.1. - We have $k \geq \ell-K_{X}^{2}$, where $K_{X}$ is the canonical class of $X$.
Proof. - We have $K_{\widetilde{X}}^{2}=K_{X}^{2}-\ell$ and $K_{S}^{2}=K_{\widetilde{X}}^{2}+k$, so
$$K_{S}^{2}=K_{X}^{2}+k-\ell .$$
By a theorem of Taubes [41, Theorem A(3)] (in the case $b^{+}>1$ ) and Liu [23, Main Theorem A] (whenever the minimal model is not irrational ruled), since $S$ is minimal, we have $K_{S}^{2} \geq 0$. This implies $k \geq \ell-K_{X}^{2}$. \(\square\)

Pick $\kappa \in \mathbf{R}$ bigger than $\max _{i=1}^{k} \int_{S_{i}} \omega$ and let $J \in \mathcal{J}_{\text {reg }}(\mathcal{C}, \kappa)$. By definition (see Lemma 4.1), the only somewhere-injective $J$-holomorphic spheres with energy less than $\kappa$ are $C_{1}, \ldots, C_{\ell}$ and possibly a collection of embedded -1-spheres. Let $\left\{J_{t}\right\}_{t=1}^{\infty}$, be a sequence of almost complex structures such that $\lim _{t \rightarrow \infty} J_{t}=J$ and such that for all $t<\infty$, the classes $E_{1}, \ldots, E_{k}$ have embedded $J_{t}$-holomorphic representatives $E_{i}\left(J_{t}\right)$ (this is possible because the space of almost complex structures for which the homology classes $E_{i}$ are represented by embedded holomorphic curves is dense in the space of all tame almost complex structures). In the limit $t \rightarrow \infty$, Gromov's compactness theorem asserts that the curves $E_{i}\left(J_{t}\right)$ converge to $J$-holomorphic stable maps.

Definition 6.2. - We will abuse notation and write $E_{i}$ for the $J$-holomorphic stable map in the class $E_{i}$. We say that $E_{i}$ is an unbroken curve if its domain is irreducible; otherwise, we say that $E_{i}$ is a broken curve. We will write $\mathcal{E}_{\text {broken }} \subset \mathcal{E}$ for the subset of broken curves and $\mathcal{E}_{\text {unbroken }} \subset \mathcal{E}$ for the subset of unbroken curves. By Proposition 2.11, all of these curves are exceptional curves of the first kind because they all satisfy $K_{\widetilde{X}} \cdot E_{i}=-1$ and they all inhabit homology classes which can be represented by embedded symplectic spheres.

Remark 6.3. - At this point in the proof, we may appeal once again to [35]. Theorem 3] and assume that $J$ is integrable in a neighbourhood of all the curves $(\mathcal{C}$ and $\mathcal{E})$ under consideration. This is important because, in what follows, when we talk about blowing down a curve, we mean the usual complex analytic blow-down.

\subsection*{6.1. Unbroken curves. -}

Lemma 6.4. - Suppose that $E \in \mathcal{E}_{\text {unbroken }}$ is an unbroken curve. Then:
\begin{itemize}
\item[(a)] $\sum_{j=1}^{\ell} E \cdot C_{j} \geq 2$.
\item[(b)] $E \cdot C_{j} \leq b_{j}-1$ with equality if and only if $b_{j}=2$ and $E \cdot C_{j}=1$.
\end{itemize}

Proof. - Part (a) follows from Theorem 5.5(1). See also [14. Section 3, Step 3].
To prove part (b), let $S^{\prime}$ be the result of blowing down the sphere $E$, and let $C_{j}^{\prime}$ denote the image of $C_{j}$ under this blow-down map. We have
$$K_{S^{\prime}} \cdot C_{j}^{\prime}=K_{\widetilde{X}} \cdot C_{j}-E \cdot C_{j}=b_{j}-2-E \cdot C_{j},$$
and Corollary 2.2 tells us that $K_{S^{\prime}} \cdot C_{j}^{\prime} \geq-1$ with equality if and only if $C_{j}^{\prime}$ is an embedded -1-sphere. This implies that $E \cdot C_{j} \leq b_{j}-1$ with equality if and only if $C_{j}^{\prime}$ is an embedded -1-sphere, which can happen only if $E \cdot C_{j}=1$ (or else $C_{j}^{\prime}$ fails to be embedded), in which case $b_{j}=2$. \(\square\)
6.2. Broken curves. - Since we have chosen $J \in \mathcal{J}_{\text {reg }}(\mathcal{C}, \kappa)$, the image of a broken curve comprises a finite set of -1 -spheres $e_{1}, \ldots, e_{m}$ together with a subset of the curves $C_{j}$ (there are no other simple $J$-holomorphic curves). If $C_{j}$ appears as an irreducible component of $E$ we will call it an internal sphere and write $C_{\text {int }}$ for the sum of all internal spheres; otherwise we call it an external sphere and write $C_{\text {ext }}$ for the sum of all external spheres.

\section*{7. Towards a bound}

The following lemma is a modification of a lemma of Rana [33]. Lemma 2.8] to the symplectic context.

Lemma 7.1. — We have:
$$\sum_{i=1}^{k} \sum_{j=1}^{\ell} E_{i} \cdot C_{j} \leq \ell+1 .$$
Proof. - We have $K_{\widetilde{X}} \cdot C_{j}=b_{j}-2$ and
$$\sum_{j=1}^{\ell}\left(b_{j}-2\right)=K_{\widetilde{X}} \cdot \sum_{j=1}^{\ell} C_{j}=\ell+1$$
by Corollary 3.3. The image of each $C_{j}$ under $\pi$ is a rational curve in a minimal symplectic manifold with $b^{+}(X)>1$, so by Corollary 2.2. $K_{S} \cdot \pi\left(C_{j}\right) \geq 0$, giving
$$\pi^{*} K_{S} \cdot \sum_{j=1}^{\ell} C_{j} \geq 0 .$$
We have
$$K_{\widetilde{X}}=\pi^{*} K_{S}+\sum_{i=1}^{k} E_{i},$$
so
$$\ell+1=K_{\widetilde{X}} \cdot \sum_{j=1}^{\ell} C_{j}=\pi^{*} K_{S} \cdot \sum_{j=1}^{\ell} C_{j}+\sum_{i=1}^{k} \sum_{j=1}^{\ell} E_{i} \cdot C_{j} \geq \sum_{i=1}^{k} \sum_{j=1}^{\ell} E_{i} \cdot C_{j} .$$ \(\square\)

Lemma 7.2. - Let $J \in \mathcal{J}_{\text {reg }}(\mathcal{C}, \kappa)$ and let $E \in \mathcal{E}$ be a $J$-holomorphic exceptional curve of the first kind. We have
$$1 \leq E \cdot \sum_{j=1}^{\ell} C_{j}$$
with equality if and only if the following conditions hold.
\begin{itemize}
\item[-] The curve $E$ has precisely one component $e$ with $e^{2}=-1$ which intersects only two spheres $C_{x^{\prime}}$ and $C_{y^{\prime}}$ from the chain $C_{1}, \ldots, C_{\ell}$, and intersects both once transversely.
\end{itemize}
\begin{itemize}
\item[-] The other components of $E$ are one of the following:
\begin{itemize}
\item[(A)] $C_{1}, C_{2}, \ldots, C_{x}, C_{y}, C_{y+1}, \ldots, C_{\ell}$ for some $1 \leq x^{\prime} \leq x<y-1<y^{\prime} \leq \ell$ :
![](https://cdn.mathpix.com/cropped/d0185d7b-b1ff-418a-8e7d-246058910b7a-23.jpg?height=192&width=838&top_left_y=729&top_left_x=576)
\item[(B1)] $C_{1}, C_{2}, \ldots, C_{x}$ for some $1 \leq x^{\prime} \leq x<y^{\prime}$ :
![](https://cdn.mathpix.com/cropped/d0185d7b-b1ff-418a-8e7d-246058910b7a-23.jpg?height=191&width=836&top_left_y=1131&top_left_x=576)
\item[(B2)] $C_{y}, C_{y+1}, \ldots, C_{\ell}$ for some $1 \leq x^{\prime}<y \leq y^{\prime} \leq \ell$ :
![](https://cdn.mathpix.com/cropped/d0185d7b-b1ff-418a-8e7d-246058910b7a-23.jpg?height=192&width=835&top_left_y=1532&top_left_x=578)
\end{itemize}
\end{itemize}
In any of these equality cases, we say $E$ is $a$ bad curve of type (A), (B1) or (B2).

Proof. - For an unbroken curve, we know that $E \cdot \sum_{j=1}^{\ell} C_{j} \geq 2$ by Lemma 6.4(a), so we may assume that $E$ is broken.

Recall from Section 6.2 that $E$ comprises a finite set of -1 -spheres $e_{1}, \ldots, e_{m}$ together with a collection of internal spheres (from amongst the $C_{j} \mathrm{~s}$ ). By Theorem 2.9(6), we know that
$$-1 \leq E \cdot C_{\text {int }} .$$
( $C_{\text {int }}$ is the sum of the internal spheres; while that theorem also takes into account terms of the form $E \cdot e_{i}$, unless $E$ is unbroken, the spheres $e_{i}$ are all blown down before the final component, so $E \cdot e_{i}=0$ ).

For a broken curve $E$, the intersection number $E \cdot C_{\text {ext }}$ (where $C_{\text {ext }}$ is the sum of the external spheres) is greater than or equal to $\sum_{i=1}^{m} e_{i} \cdot C_{\text {ext }}$ plus the number of interfaces between $C_{\text {int }}$ and $C_{\text {ext }}$ (it could be strictly greater if some of the components of $E$ come with higher multiplicity).

Each sphere $e_{i}$ is itself an unbroken curve, so $\sum_{j=1}^{\ell} e_{i} \cdot C_{j} \geq 2$. In particular, there must be at least one external sphere, otherwise the graph $G$ defined in Theorem 2.9 would contain a cycle. This means that there is at least one interface between $C_{\text {int }}$ and $C_{\text {ext }}$, so $E \cdot \sum_{j=1}^{\ell} C_{j} \geq 0$.
\begin{itemize}
\item[(A)] If $e_{1}$ does not intersect an external sphere, then it intersects two internal spheres. These spheres cannot be connected in the chain $C_{1}, \ldots, C_{\ell}$ by a sequence of spheres in $C_{\text {int }}$, or else the dual graph to $E$ would contain a cycle (contradicting Theorem 2.9(3)), so in this case there would necessarily be two interfaces between $C_{\text {int }}$ and $C_{\text {ext }}$ and, again, we get $E \cdot \sum_{j=1}^{\ell} C_{j} \geq 1$. If equality holds then there are precisely two interfaces, and we deduce that $C_{\text {int }}=$ $C_{1}+\cdots+C_{x}+C_{y}+\cdots+C_{\ell}$ for some $1 \leq x^{\prime} \leq x<x+1 \leq<y-1<y \leq y^{\prime} \leq \ell$, where $C_{x^{\prime}}$ and $C_{y^{\prime}}$ are the internal spheres hit by $e_{1}$.
\item[(B)] If $e_{1}$ intersects an external sphere then we get $E \cdot \sum_{j=1}^{\ell} C_{j} \geq 1$. If we have equality then there is at most one interface between $C_{\text {int }}$ and $C_{\text {ext }}$, which means that either:
\begin{itemize}
\item[(B1)] $C_{\text {int }}=C_{1}+\cdots+C_{x}$ for some $1 \leq x<y^{\prime} \leq \ell$, where $C_{y^{\prime}}$ is the external sphere hit by $e_{1}$, or
\item[(B2)] $C_{\text {int }}=C_{y}+\cdots+C_{\ell}$ for some $1 \leq x^{\prime}<y \leq \ell$, where $C_{x^{\prime}}$ is the external sphere hit by $e_{1}$.
\end{itemize}
\end{itemize}
If $m>1$ (so that there is a further -1-sphere $e_{2}$ ) then $e_{2}$ either intersects an external sphere or else it connects two internal spheres, and to avoid creating a cycle in the dual graph we must find another interface between $C_{\text {int }}$ and $C_{\text {ext }}$. In either case, this pushes the inequality up to $E \cdot \sum_{j=1}^{\ell} C_{j} \geq 2$ as desired. \(\square\)

Lemma 7.3. - If there are precisely $p$ bad curves amongst the $E_{i}$ then
$$\ell \leq 2 K_{X}^{2}+p+1 .$$
Proof. - This follows from the fact that the total number of blow-ups required is $k \geq \ell-K_{X}^{2}$, so at least $\ell-K_{X}^{2}-p$ of these blow-ups are associated to good curves. Therefore
$$2\left(\ell-K_{X}^{2}-p\right)+p \leq \sum_{i=1}^{k} \sum_{j=1}^{\ell} E_{i} \cdot C_{j},$$
and the right hand side is less than or equal to $\ell+1$ by Lemma 7.1. This gives
$$\ell \leq 2 K_{X}^{2}+p+1,$$
as required. \(\square\)

Therefore the problem of establishing bounds is reduced to the problem of bounding the number of bad curves amongst the exceptional divisors.

\section*{8. Bounding bad curves}

The following is immediate from Proposition 2.16.
Corollary 8.1. - Any two bad curves of type (B1) share a common component. By Proposition 2.16, we know that they are nested. Therefore, if there are any bad curves of type (B1), there is a maximal one with respect to nesting. The same holds for curves of type (B2), and it also follows that a bad curve of type (B1) and a bad curve of type (B2) cannot share a component.

If there is a bad curve of type ( $A$ ) then it shares components with any other bad curve, so in this situation there is a maximal bad curve with respect to nesting.

Corollary 8.2. - Suppose there are no bad curves of type (A). Let $n_{1}$ be the number of internal spheres in the maximal bad curve of type (B1) (zero if there are none) and $n_{2}$ the corresponding number for (B2). Then there are at most $n_{1}+n_{2}$ bad curves in total.

If there is a bad curve of type $(A)$, let $n$ be the number of internal spheres in the maximal one. Then there are at most $n$ bad curves in total.

Proof. - Any two distinct bad curves $E_{1}$ and $E_{2}$ satisfy $E_{1} \cdot E_{2}=0$ by Lemma 2.5. Since any bad curve is contained in a neighbourhood $N$ of the maximal one (of its type, if there is no bad curve of type (A)), this means that if there are $p$ bad curves then there are $p+1$ homology classes in the homology of $N$ which are orthogonal with respect to the intersection product ( $p$ coming from the bad curves, one coming from the -1-sphere which is necessarily there). Since the total rank of the homology of $N$ is equal to the number of internal spheres $(n)$ plus one, we see that $p \leq n$. \(\square\)

Proposition 8.3. - Let $E$ be a bad curve of type $(A)$, maximal with respect to nesting. Suppose that it contains $n$ internal spheres. Then
$$n \leq \frac{1}{2}(\ell+4) .$$
Proof. - We separate into a number of cases; any cases not explicitly listed here are related to one of the listed cases by symmetry (e.g. reflecting the diagram).
![](https://cdn.mathpix.com/cropped/d0185d7b-b1ff-418a-8e7d-246058910b7a-25.jpg?height=190&width=1071&top_left_y=2206&top_left_x=484)

In this case, blowing down $e$ means that either $\pi_{1}\left(C_{x^{\prime}}\right)$ or $\pi_{1}\left(C_{y^{\prime}}\right)$ becomes a -1-sphere which intersects three other components of the exceptional curve, which contradicts Theorem 2.9(7).
![](https://cdn.mathpix.com/cropped/d0185d7b-b1ff-418a-8e7d-246058910b7a-26.jpg?height=479&width=1072&top_left_y=690&top_left_x=484)
We handle these cases simultaneously. By the argument in Case (A.1), $C_{x^{\prime}}$ cannot become a -1-sphere until all of the spheres $C_{j}, y \leq j \leq \ell$, have been blown down. In particular, this means that $C_{y}, \ldots, C_{\ell}$ is a chain of -2-spheres. Let us define $n_{1}:=\ell-y+1$ to be the number of the -2-spheres in this chain. We have $K \cdot \Pi_{n_{1}+1}\left(C_{x^{\prime}}\right)=K \cdot C_{x^{\prime}}-n_{1}-1$ since we have blown down $e, C_{y}, \ldots, C_{\ell}$. Since $K \cdot C_{x^{\prime}}^{\left(n_{1}\right)}=-1$, we see that
$$K \cdot C_{x^{\prime}}=n_{1} .$$
Moreover,
$$K \cdot C_{1} \geq n_{1},$$
because our T-string terminates in a chain of $n_{1}-2$-spheres. Once we have blown down $e, C_{y}, \ldots, C_{\ell}$, we are left with an exceptional curve $\Pi_{n_{1}+1}\left(C_{1}\right), \ldots, \Pi_{n_{1}+1}\left(C_{x}\right)$ with $x=n-n_{1}$ components, containing a single -1 -sphere $\Pi_{n_{1}+1}\left(C_{x^{\prime}}\right)$. We take $S$ to be $\pi_{n_{1}+1}\left(C_{y-1}\right)$, which has $K \cdot S \leq K \cdot C_{y-1}-1$ because $C_{y-1}$ has been attached to some curves which have been blown down. The configuration
$$\Pi_{n_{1}+1}\left(C_{1}\right), \ldots, \Pi_{n_{1}+1}\left(C_{x}\right), S$$
is precisely the configuration covered by Lemma 2.17. Therefore
$$n-n_{1} \leq \frac{1}{2}\left(K \cdot C_{y-1}+2\right) .$$
Overall, we have
$$n \leq \frac{1}{2}\left(K \cdot\left(C_{1}+C_{x^{\prime}}+C_{y-1}\right)+2\right) \leq \frac{1}{2}(\ell+3),$$
by Corollary 3.3
![](https://cdn.mathpix.com/cropped/d0185d7b-b1ff-418a-8e7d-246058910b7a-27.jpg?height=195&width=1014&top_left_y=531&top_left_x=483)
Let us, suppose without loss of generality, that $C_{y}$ is the second curve to be blown down in $E$. Then, if we set $S=\pi_{1}\left(C_{y-1}\right)$, we find a configuration
$$\pi_{1}\left(C_{1}\right), \ldots, \pi_{1}\left(C_{x}\right), \pi_{1}\left(C_{y}\right), \ldots \pi_{1}\left(C_{\ell}\right), S$$
to which we can apply Lemma 2.17 and get
$$n \leq \frac{1}{2}\left(K \cdot C_{y-1}+3\right) \leq \frac{1}{2}(\ell+4),$$
by Corollary 3.3
![](https://cdn.mathpix.com/cropped/d0185d7b-b1ff-418a-8e7d-246058910b7a-27.jpg?height=193&width=1012&top_left_y=1140&top_left_x=484)
Let $n_{1}$ be the number of curves $C_{1}, \ldots, C_{n_{1}}$ which are blown down before the component $C_{y}$ is blown down. These necessarily form a (possibly empty) chain of -2-spheres. As in Case (A.2), we obtain
$$\begin{aligned}
& K \cdot C_{y}=n_{1} \\
& K \cdot C_{\ell} \geq n_{1} .
\end{aligned}$$
As soon as $\Pi_{n_{1}+1}\left(C_{y}\right)$ becomes a -1 -sphere, we can take $S=\Pi_{n_{1}+1}\left(C_{y-1}\right)$ and apply Lemma 2.17 to the configuration
$$\Pi_{n_{1}+1}\left(C_{x}\right), \Pi_{n_{1}+1}\left(C_{x-1}\right), \ldots, \Pi_{n_{1}} 1\left(C_{n_{1}+1}\right), \Pi_{n+1}\left(C_{y}\right), \ldots, \Pi_{n+1}\left(C_{\ell}\right), S$$
to get
$$n-n_{1} \leq \frac{1}{2}\left(K \cdot C_{y-1}+3\right) .$$
Overall,
$$n \leq \frac{1}{2}\left(K \cdot\left(C_{y-1}+C_{y}+C_{\ell}\right)+3\right) \leq \frac{1}{2}(\ell+4) .$$
![](https://cdn.mathpix.com/cropped/d0185d7b-b1ff-418a-8e7d-246058910b7a-27.jpg?height=192&width=1008&top_left_y=2075&top_left_x=483)

This configuration cannot occur by Theorem 5.5(2). \(\square\)