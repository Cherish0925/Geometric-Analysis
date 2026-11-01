---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 1312_5368.pdf
converter: mathpix
format: mmd
---

\title{
A SHARP CUSP COUNT FOR COMPLEX HYPERBOLIC SURFACES AND RELATED RESULTS
}

\author{
GABRIELE DI CERBO AND LUCA F. DI CERBO
}

\begin{abstract}
We derive a sharp cusp count for finite volume complex hyperbolic surfaces which admit smooth toroidal compactifications. We use this result, and the techniques developed in [DiC12], to study the geometry of cusped complex hyperbolic surfaces and their compactifications.
\end{abstract}

Contents
\begin{itemize}
\item[1.] Introduction
1
\item[1.1.] Preliminaries and main results
2
\item[2.] A sharp cusp count
4
\item[3.] Applications
5
\end{itemize}

References
9

\section*{1. Introduction}

The problem of counting the number of ends in complete pinched negatively curved finite volume manifolds is a long standing problem in classical differential geometry. For real and complex hyperbolic manifolds, geometric topology techniques have been widely and successfully applied. The literature on the subject is enormous, we thus refer the interested reader to the classical paper of Parker [Par98] and to the more recent work of Stover [Sto13] for an overview.

For cusped complex hyperbolic manifolds, techniques coming from algebraic geometry can also be applied. The key for this approach is the existence of particularly nice compactifications of such complex hyperbolic manifolds, known as toroidal compactifications. We recently applied this circle of ideas in [DiC12], where many of the finiteness properties of cusped hyperbolic manifolds and their compactifications were made effective.

The purpose of this paper is to improve, in complex dimension two, the results contained in [DiC12]. The main novelty contained here is that some of the results are now sharp. This is quite unusual even in low dimensions and it seems to be the first instance where sharpness is actually achieved.

Acknowledgements. We thank the organizers of the conference "Algebraic \& Hyperbolic Geometry - New Connections" for stimulating our interest in these topics.
1.1. Preliminaries and main results. Let $\mathcal{H}^{2}$ be the two dimensional complex hyperbolic space. Given a torsion free non-uniform lattice $\Gamma$ in $\operatorname{PU}(1,2)$, then $\mathcal{H}^{2} / \Gamma$ is a non-compact finite volume complex hyperbolic surface with cuspidal ends. The cusps of $\mathcal{H}^{2} / \Gamma$ are then in one to one correspondence with the conjugacy classes of maximal parabolic subgroups in $\Gamma$. It is known that when the parabolic elements in $\Gamma$ have no rotational part (e.g. if $\Gamma$ is neat), then $\mathcal{H}^{2} / \Gamma$ admits a compactification $(X, D)$ consisting of a smooth projective surface and an exceptional divisor $D$. Recall that each maximal parabolic subgroup can be thought as a lattice in $\mathrm{N} \rtimes \mathrm{U}(1)$ where N is a Heisenberg type Lie group, and that a parabolic isometry is said to have no rotational part if it has no U(1) component. The pair $(X, D)$ is known as the toroidal compactification of $\mathcal{H}^{2} / \Gamma$. For a more detailed discussion of these topics, we refer to the classical references [Ash et al.10], [BJ06]. For a quick introduction, the interested reader may also refer to Section 1.1 in [DiC12] and the bibliography therein.

Let us recall a few important geometric features of $(X, D)$. First, the exceptional divisor $D$ consists of disjoint smooth elliptic curves with negative self-intersection which are in one to one correspondence with the cusps of $X \backslash D$. Second, the pair $(X, D)$ is of logarithmic general type and $D$-minimal, i.e., the log-canonical divisor $K_{X}+D$ has maximal Kodaira dimension and $X$ does not contain any exceptional curve $E$ of the fist kind such that $E \cdot D \leq 1$. Finally, because of the Hirzebruch-Mumford proportionality theorem [Mum77], we have
$$3 \bar{c}_{2}=\bar{c}_{1}^{2}$$
where $\bar{c}_{1}^{2}$ and $\bar{c}_{2}$ denote the logarithmic Chern numbers of the compactification $(X, D)$. Recall that $\bar{c}_{1}^{2}$ is the self-intersection of $K_{X}+D$, while $\bar{c}_{2}$ is the topological Euler characteristic of $X \backslash D$. Since $X \backslash D$ is by construction negatively curved, Gromov-Harder's generalization of Chern-Gauss-Bonnet [Gro82] implies that $\bar{c}_{2}$ must be a strictly positive integer.

In [DiC12], we showed that, in any dimension, $K_{X}+D$ is not only big and nef but it is a limit of ample divisors of the form $K_{X}+\alpha D$ where $\alpha$ is a real number strictly less than one. Let us recall the technical form of this result as it will be used here.

Theorem 1.1 ([DiC12], Theorem 1.1). Let $(X, D)$ be a toroidal compactification. Then $K_{X}+\alpha D$ is ample for any $\alpha \in\left(\frac{1}{3}, 1\right)$.

As extensively shown in [DiC12], this "gap" theorem has many consequences for the theory of cusped complex hyperbolic manifolds. In fact, one of the first applications is a cusp count in terms of the volume, valid in any dimension, which turned out to be the best count available in the literature for surfaces and threefolds, see Theorem 1.5 in [DiC12].

The main purpose of this note is to show that, in complex dimension two, such cusp count can not only be improved but also made sharp. Recall that, if we
normalize the holomorphic sectional curvature of $X \backslash D$ to be -1, we have
$$\operatorname{Vol}_{-1}(X \backslash D)=\frac{8}{9} \pi^{2}\left(K_{X}+D\right)^{2}$$
where by $\operatorname{Vol}_{-1}(X \backslash D)$ we indicate the Riemannian volume of $X \backslash D$ computed with respect to the normalized locally symmetric metric. We then state the cusp count in terms of the self-intersection of the log-canonical divisor of the compactification $(X, D)$.

Theorem 1.2. Let $\left(X^{2}, D\right)$ be a toroidal compactification. Let $q$ be the number of components of $D$. Then
$$q \leq \frac{4}{3}\left(K_{X}+D\right)^{2} .$$
Moreover, there exists a smooth toroidal compactification which saturates this bound.
Despite the existence of many linear upper bounds on the number of cusps of a locally symmetric space in terms of its volume, Theorem 1.2 appears to be the first sharp bound. Unfortunately, Theorem 1.2 holds in complex dimension two only and it is not clear how to obtain sharp bounds in higher dimensions. On the other hand, it seems an extremely complicated problem to sharpen any "effective" technique, either in geometric topology or complex/differential geometry, in higher dimensions. To give an example of the difficulty of this problem, it will suffice to recall that we are missing an explicit example of a smooth threefold which is the toroidal compactification of a cusped complex hyperbolic threefold. Of course, for group theoretical reasons we know that such objects exist in great profusion. Nevertheless, we still seem to miss a technique to systematically produce explicit examples. Fortunately, Hirzebruch in [Hir82] constructed many explicit examples in complex dimension two, see Section 2 for details. These examples play a crucial role in testing the sharpness of Theorem 1.2.

Next, using Theorems 1.1 and 1.2 we can study in details the geometry of cusped complex hyperbolic surfaces and their compactifications. The results which follows substantially improve, in complex dimension two, the ones contained in [DiC12]. First, we describe the pair $(X, D)$ when realized as a sub-variety in some projective space.

Theorem 1.3. Let $\left(X^{2}, D\right)$ be a toroidal compactification. Let $L:=K_{X}+D$ and let us denote by $D_{i}$ the components of $D$. Then $7 L-4 D$ is very ample. In particular, $7 L-4 D$ embeds $X$ as a smooth subvariety of $\mathbb{P}^{5}$ of degree $d \leq 49 L^{2}$. Moreover, if we let $d_{i}$ be the degree of $D_{i}$ under the embedding given by $7 L-4 D$, then $d_{i}<6 L^{2}$.

The importance of this result relies on the fact that it can be used to derive an explicit bound on the number of complex hyperbolic surfaces with given upper bound on the volume. More precisely, Theorem 1.3 can be combined with classical Chow varieties techniques to derive an effective version of the classical Wang's finiteness theorem, [Wan72]. For the numerical value of this bound we refer to Corollary 3.2 in Section 3.

Second, we can construct very explicitly the singular compactifications (Baily-Borel-Siu-Yau) of these ball quotients by studying the pluri-log-canonical maps of their toroidal compactifications.

Theorem 1.4. Let $\left(X^{2}, D\right)$ be a toroidal compactification. Then for all $m \geq 3$ the map associated to $\left|m\left(K_{X}+D\right)\right|$ is a morphism which maps all the different components of $D$ to distinct singular points. Furthermore, for all $m \geq 4$ this morphism defines an embedding of $X \backslash D$ into some projective space.

Theorem 1.4 does not only improve Theorem 1.3 in [DiC12] when the dimension is equal to two, but also Theorem B in [DiC12a] which appears to be the most accurate result currently available in the literature.

Finally, we present two sided bounds on the Picard numbers of toroidal compactifications in terms of the number of cusps and the volume. Interestingly, we are able to show that the lower bound is sharp.

Theorem 1.5. Let $\left(X^{2}, D\right)$ be a toroidal compactification. Let $q$ be the number of components of $D$ and let us denote by $\rho(X)$ the Picard number of $X$. Then
$$q+1 \leq \rho(X) \leq 4+\frac{13}{3}\left(K_{X}+D\right)^{2} .$$
Moreover, there exists a smooth toroidal compactification which saturates the lower bound.

In Section 3.4 of [DiC12], we computed an explicit upper bound on the Picard number of a toroidal compactification in terms of the top self-intersection of its logcanonical divisor. Unfortunately, the techniques presented in Section 3.4 of [DiC12] are applicable in dimension bigger or equal than three and they do not generalize to the case of surfaces. On the other hand, Theorem 1.3 and Corollary 3.2 are enough to theoretically imply the existence of such an upper bound in the two dimensional case. The explicit upper bound given in Theorem 1.5 fixes this gap.

\section*{2. A sharp cusp count}

In this section, we present a sharp cusp count for complex hyperbolic surfaces which admit smooth toroidal compactifications. More precisely, we give a proof of Theorem 1.2 stated in the Introduction. The strategy of the proof relies on the fact that we are working in complex dimension two. In fact, the Kodaira-Enriques classification [BHPV04] of compact complex surface is crucially used. The other important ingredients are the Hirzebruch-Mumford proportionality and, in order to prove sharpness, an explicit toroidal compactification which can be extracted from the work of Hirzebruch in [Hir82].

Proof of Theorem 1.2. Given a two dimensional toroidal compactification $(X, D)$, let us observe that the holomorphic Euler characteristic, say $\chi\left(\mathcal{O}_{X}\right)$, of $X$ must be nonnegative. In fact, since $\chi\left(\mathcal{O}_{X}\right)$ is a birational invariant, by the Kodaira-Enriques classification we know that the only surfaces with negative holomorphic Euler characteristic are birational to ruled surfaces over Riemann surfaces with genus greater or equal than two. It remains to show that such surfaces cannot be
toroidal compactifications. The key observation is that they cannot contain any smooth elliptic curve. Assume not, then a smooth elliptic curve must be a section of the ruling. We then obtain a surjective morphism from the elliptic curve to the base of the ruling which we are assuming to be of genus greater or equal than two. This contradicts the classical genus formula of Riemann-Hurwitz [GH78].

Thus, by Noether's formula, see page 9 in [Fri98], and Hirzebruch-Mumford proportionality we conclude that
$$c_{1}^{2}+c_{2}=\bar{c}_{1}^{2}+D^{2}+\frac{1}{3} \bar{c}_{1}^{2} \geq 0$$
which then implies
$$\frac{4}{3} \bar{c}_{1}^{2} \geq-D^{2} \geq q .$$
It remains to show that this bound is sharp. To this aim, recall the construction of a four cusps complex hyperbolic surface with normalized Riemannian volume equal to $\frac{8}{3} \pi^{2}$. Let $Y=\mathbb{C}^{2} / \Gamma$ be a product Abelian surface, with $\Gamma=\Lambda_{1, \tau} \times \Lambda_{1, \tau}$ where $\Lambda_{1, \tau}$ is the lattice in $\mathbb{C}$ generated by 1 and $\tau=e^{\frac{\pi i}{3}}$. In $Y$, let us consider a curve $C$ defined by the equations
$$w=0, \quad z=0, \quad w=z, \quad w=\tau z$$
where $(w, z)$ are the natural product coordinates on $Y$. The divisor $C$ consists of four smooth disjoint elliptic curves intersecting at the point $p=(0,0)$ only. Given $(Y, C)$, by blowing up the point $p$ we obtain a pair $(X, D)$, where $X$ is the blow up at $p$ of Y and $D$ the proper transform of $C$ which consits of four disjoint smooth elliptic curves. Now the pair $(X, D)$ can be shown to be a toroidal compactification, see [Hir82] and Section 4 in [DiC13]. Thus, since
$$\left(K_{X}+D\right)^{2}=K_{X}^{2}-D^{2}=3,$$
the bound is proven to be sharp and the proof is complete. \(\square\)

Note that the proof of Theorem 1.2 gives also a bound of the self-intersection of $D$ in terms of the self-intersection of the log-canonical divisor of the pair $(X, D)$. This fact is important when trying to apply Chow varieties techniques in complex dimension two. Thus, we summarize this bound into a corollary as it will be used in Section 3.

Corollary 2.1. Let $\left(X^{2}, D\right)$ be a toroidal compactification. Then
$$0<-D^{2} \leq \frac{4}{3}\left(K_{X}+D\right)^{2} .$$

\section*{3. Applications}

In this section, we substantially improve the theory developed [DiC12] in the special case of surfaces. In particular, we give the proof of Theorem 1.3, 1.4 and 1.5 stated in the introduction. These improvements not only rely on Theorem 1.2, but also on the fact that the birational geometry of adjoint linear systems on surfaces is completely understood thanks to the theorem of Reider. Let us recall the statement of this theorem, for more details see [Rei88].

Theorem 3.1 (Reider). Let $X$ be a smooth surface and let $L$ be a nef line bundle on $X$. Then the following hold:
\begin{itemize}
\item[(1)] If $L^{2} \geq 5$ and $x \in X$ is a base point of $\left|K_{X}+L\right|$ then there exists a curve $C$ through $x$ such that either
$$\begin{aligned}
& C \cdot L=0 \quad \text { and } \quad C^{2}=-1 ; \text { or } \\
& C \cdot L=1 \quad \text { and } \quad C^{2}=0 .
\end{aligned}$$
\item[(2)] If $L^{2} \geq 10$ and $x, y \in X$ are two (possibly infinitely near) points which $\left|K_{X}+L\right|$ does not separate then there exists a curve $C$ through $x$ and $y$ such that either
$$\begin{aligned}
& C \cdot L=0 \quad \text { and } C^{2} \in\{-1,-2\} ; \text { or } \\
& C \cdot L=1 \quad \text { and } C^{2} \in\{0,-1\} ; \text { or } \\
& C \cdot L=2 \quad \text { and } C^{2}=0 .
\end{aligned}$$
\end{itemize}

The next theorem exhibits a two dimensional toroidal compactification $(X, D)$ as a smooth sub-variety of $\mathbb{P}^{5}$. Moreover, it gives a bound on its degree as well as on the degree of the irreducible components of $D$.

Proof of Theorem 1.3. Let $L:=K_{X}+D$. Because of Theorem 1.1, we know that $2 K_{X}+D=2 L-D$ is ample. Theorem 3.1 implies us that $K_{X}+3(2 L-D)=7 L-4 D$ is very ample. In particular, $7 L-4 D$ embeds $X$ as a smooth sub-variety of some projective space of degree $d=(7 L-4 D)^{2} \leq 49 L^{2}$. By general projection, for details see page 173 in [GH78], we can always reduce to $\mathbb{P}^{5}$ since $X$ is two dimensional. Next, we need to bound the degree of the components $D_{i}$ of $D$ under the embedding given by the line bundle $7 L-4 D$. First, recall that $D_{i} \cdot D_{j}=0$ if $i \neq j$. Then
$$\begin{aligned}
d_{i} & =D_{i} \cdot(7 L-4 D)=-4 D_{i} \cdot D \\
& =-4 D_{i}^{2} \leq-4 D^{2}<6 L^{2},
\end{aligned}$$
where the last inequality is given by Corollary 2.1. \(\square\)

The previous theorem can be used to count the number of toroidal compactifications with fixed volume. We will estimate this number bounding the number of pairs in a fixed projective space of bounded degrees as in Theorem 1.3. This can be achieved studying a particular Chow variety. To ease the proof of the result, let us introduce some notation. We define $\operatorname{Chow}_{m}\left(d ; d_{1}, \ldots, d_{q}\right)$ to be the closed subvariety of
$$\operatorname{Chow}_{m}(2, d) \times \operatorname{Chow}_{m}\left(1, d_{1}\right) \times \cdots \times \operatorname{Chow}_{m}\left(1, d_{q}\right),$$
parametrizing pairs $\left(X, \sum_{i=1}^{q} D_{i}\right)$ where $X$ is a smooth surface of degree $d$ in $\mathbb{P}^{m}$ and each $D_{i}$ is a smooth one-dimensional subvariety of degree $d_{i}$ in $\mathbb{P}^{m}$ contained in $X$.

The following corollary is a combination of the previous results and an effective bound on the number of components of $\operatorname{Chow}\left(d: d_{1}, \ldots, d_{q}\right)$. We give only a sketch of the proof since it is essentially the same as in [DiC12].

Corollary 3.2. Fix a positive integer $V$. Then the number of toroidal compactifications with $\operatorname{dim}(X)=2$ and $\left(K_{X}+D\right)^{2} \leq V$ is bounded by
$$\sum_{q=1}^{q_{0}} d_{0}(6 V)^{q}\binom{6 d_{0}}{5}^{6(q+1)\left({ }_{5}^{5+d_{0}}\right)}$$
where $d_{0}=49 V$ and $q_{0}=\lfloor 1.33 V\rfloor$.
Proof. We can embed $(X, D)$ in $\mathbb{P}^{5}$ with bounded degrees using Theorem 1.3. Let $d$ be the degree of $X$ and let $d_{i}$ be the degree of $D_{i}$. The pair $(X, D)$ corresponds to a point of $\operatorname{Chow}_{5}\left(d ; d_{1}, \ldots, d_{q}\right)$. By a theorem of Fujiki in Fuj92, $(X, D)$ is infinitesimally rigid under deformations of the pair. In particular, the number of irreducible components of $\operatorname{Chow}_{5}\left(d ; d_{1}, \ldots, d_{q}\right)$ provides an upper bound on the number of toroidal compactifications with fixed degrees $d$ and $d_{1}, \ldots, d_{q}$. It is not difficult to extend the classical bound on the number of irreducible components of Chow varieties in [Kol96] to this setting, see Proposition 3.2 in [Hwa05]. Combining this formula and the bounds provided by Theorem 1.3 we obtain the result. \(\square\)

Next, we can explicitly construct the Baily-Borel compactifications of cusped complex hyperbolic surfaces as projective algebraic varieties. In other words, we give the proof of Theorem 1.4 stated in the Introduction.

Proof of Theorem 1.4. Let $L:=K_{X}+D$. Since
$$3 \bar{c}_{2}=\bar{c}_{1}^{2}, \quad \bar{c}_{2}>0,$$
we conclude that $L^{2} \geq 3$. Note that the null locus of $L$ is precisely $D$, i.e., the only curves that intersect trivially with the log-canonical are contained in $D$. By Reider's theorem, $K_{X}+2 L$ is base point free away from $D$. Adding $D$ we get that $3\left(K_{X}+D\right)$ is base point free away from $D$. Next, let us consider the short exact sequence
$$0 \rightarrow \mathcal{O}_{X}\left(2 K_{X}+D\right) \xrightarrow{D} \mathcal{O}_{X}\left(2\left(K_{X}+D\right)\right) \rightarrow \mathcal{O}_{D} \rightarrow 0 .$$
By Kawamata-Viehweg's vanishing, see Theorem 12.2 page 181 in [BHPV04], we have that
$$H^{1}\left(X, \mathcal{O}_{X}\left(2 K_{X}+D\right)\right)=0 .$$
Thus, taking the long exact sequence in cohomology, there exists a surjective map
$$H^{0}\left(X, \mathcal{O}_{X}\left(2\left(K_{X}+D\right)\right)\right) \rightarrow \bigoplus_{i=1}^{q} H^{0}\left(D_{i}, \mathcal{O}_{D_{i}}\right),$$
which then implies that $2 L$ is base point free along $D$. Finally, we conclude by applying Reider's theorem to $K_{X}+3 L$. \(\square\)

Let us conclude this section by deriving a two sided bound on the Picard number of two dimensional toroidal compactifications. More precisely, we give the proof of Theorem 1.5 stated in the introduction.

Proof of Theorem 1.5. For any complex 4-manifold, we have
$$p_{1}(X)=c_{1}^{2}-2 c_{2}$$
where $p_{1}$ is the first Pontrjagin class. By Hodge index and Hirzebruch's signature formula, we conclude that
$$2 p_{g}(X)+2-h^{1,1}(X)=\frac{1}{3}\left(c_{1}^{2}-2 c_{2}\right),$$
where $p_{g}(X)=h^{0}\left(X, \mathcal{O}_{X}\left(K_{X}\right)\right)$. As observed in the proof of Theorem 1.2. the holomorphic Euler characteristic of $X$ is necessarily nonnegative. Noether's formula then implies that
$$h^{1,1}(X) \leq 2 p_{g}(X)+2-4 \chi\left(\mathcal{O}_{X}\right)+c_{2} \leq 2 p_{g}(X)+2+c_{2} .$$
Next, let us observe that since $D$ is effective then
$$p_{g}(X) \leq h^{0}\left(X, \mathcal{O}_{X}\left(K_{X}+D\right)\right) .$$
By a theorem of Matsusaka, see [Kol96],
$$h^{0}\left(X, \mathcal{O}_{X}\left(K_{X}+D\right)\right) \leq 2\left(K_{X}+D\right)^{2}+2,$$
which finally implies
$$h^{1,1}(X) \leq 4+\frac{13}{3}\left(K_{X}+D\right)^{2} .$$
It remains to show the existence of a sharp lower bound for $\rho(X)$ in terms of the number of cusps. Say that $q$ is the number of components of $D$. Suppose by contradiction that $\rho(X) \leq q$. Let $H$ be an ample divisor on $X$. Then there exists a relation of the form
$$a_{0} H+\sum_{i=1}^{q} a_{i} D_{i} \equiv 0$$
with not all of the $\left\{a_{i}\right\}_{i=0}^{q} \in \mathbb{R}$ equal to zero. Since $D_{i} \cdot D_{j}=0$ for all $j \neq i$, and $D_{i}^{2}<0$ for all $i$, the irreducible components of $D$ are not numerically equivalent and we can then assume $a_{0}=1$. Intersecting the above relation with $D_{i}$, we get that $a_{i}>0$ for all $i$. On the other hand
$$0=H \cdot\left(H+\sum_{i=1}^{q} a_{i} D_{i}\right)=H^{2}+\sum_{i=1}^{q} a_{i} D_{i} \cdot H>0,$$
gives a contradiction. Finally, we need to prove that this lower bound is sharp. To this aim, let $(X, D)$ be the particular toroidal compactification used to show that Theorem 1.2 was sharp. Then $X$ is the blow up of a very particular Abelian surface $Y$ with maximal Picard number, i.e., $\rho(Y)=h^{1,1}(Y)=4$. We then conclude that $\rho(X)=5$. Since $D$ consists of four irreducible components, the lower bound is then sharp. \(\square\)

\section*{References}
\begin{itemize}
\item[] [Ash et al.10] A. Ash, D. Mumford, M. Rapoport, Y.-S. Tai, Smooth compactifications of locally symmetric varieties. Cambridge Mathematical Library. Cambridge University Press, Cambridge, 2010.
\item[] [BHPV04] W. Barth, K. Hulek, C. Peters, A. Van de Ven, Compact complex surfaces. Ergebnisse der Mathematik undihrer Grenzgebiete (3), 4. Springer-Verlag, Berlin, 2004.
\item[] [BB66] W. L. Baily, A. Borel, Compactifications of arithmetic quotients of bounded symmetric domains, Ann. of Math., 84 (1966), no.2, 442-528.
\item[] [BJ06] A. Borel, L. Ji, Compactifications of locally symmetric varieties. Mathematics: Theory \& Applications, Birkäuser Boston, Inc. Boston, MA, 2006.
\item[] [DiC12] G. Di Cerbo, L. F. Di Cerbo, Effective results for complex hyperbolic manifolds, arXiv:1212.0501 [mathDG], 2012.
\item[] [DiC13] L. F. Di Cerbo, Classification of toroidal compactifications with $3 \bar{c}_{2}=\bar{c}_{1}^{2}$ and $\bar{c}_{2}=1$, arXiv:1309.5516 [mathAG], 2013.
\item[] [DiC12a] L. F. Di Cerbo, Finite-volume complex-hyperbolic surfaces, their toroidal compactifications, and geometric applications. Pacific J. Math., 255 (2012), no.2, 305-315.
\item[] [Fuj92] A. Fujiki, An $L^{2}$ Dolbeaut lemma and its applications, Publ. Res. Inst. Math. Sci. 28 (1992), 845-884.
\item[] [GH78] P. Griffiths, J. Harris, Principles of Algebraic Geometry. Pure and Applied Mathematics. Wiley-Interscience, New York, NY, 1978.
\item[] [Gro82] M. Gromov, Volume and bounded cohomology, Publ. Math. Inst. Hautes Etudes Sci. 56 (1982), 5-99.
\item[] [Hir82] F. Hirzebruch, Chern numbers of algebraic surfaces: an example, Math. Ann. 266 (1982), 351-356.
\item[] [Hwa05] J.-M. Hwang, On the number of complex hyperbolic manifolds of bounded volume, Internat. J. Math. 8 (2005), 863-873.
\item[] [Kol96] J. Kollár, Rational curves on algebraic varieties, Ergebnisse der Mathematik und ihrer Grenzgebiete. 3. Folge. A Series of Modern Surveys in Mathematics, vol. 32. Springer-Verlag, Berlin, 1996.
\item[] [Mum77] D. Mumford, Hirzebruch's proportionality theorem in the non-compact case. Invent. Math. 42 (1977), 239-272.
\item[] [Par98] J. R. Parker, On the volume of cusped, complex hyperbolic manifolds and orbifolds, Duke Math. J. 94 (1998), 433-464.
\item[] [Rei88] I. Reider, Vector bundles of rank 2 and linear systems on algebraic surfaces, Ann. Math. 127 (1988), 309-316.
\item[] [Sto13] M. Stover, On the number of ends of rank one locally symmetric spaces. Geom. Topol. 17 (2013), 905-924.
\item[] [Fri98] R. Friedman, Algebraic Surfaces and Holomorphic Vector Bundles, Univesitext. Springer-Verlag, New York 1998.
\item[] [SY82] Y. T. Siu, S. T. Yau, Compactification of negatively curved complete Kähler manifolds of finite volume, Seminars in Differential Geometry, pp. 363-380, Ann. of Math. Stud., Vol. 102, Princeton Univ. Press, Princeton, N. J., 1982.
\item[] [Wan72] H. C. Wang, Topics on totally discontinuous groups, Symmetric Spaces, 459-487, edited by W. B. Boothby and G. L. Weiss, Pure and Appl. Math. 8, Marcel Dekker, New York, 1972.
\end{itemize}