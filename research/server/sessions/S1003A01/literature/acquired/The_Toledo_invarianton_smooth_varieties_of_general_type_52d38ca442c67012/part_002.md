---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: The Toledo invarianton smooth varieties of general type]

Note that the support of $D^{\prime}$ is included in the support of $D$, hence in $\operatorname{Ex}(\varphi)$, so that
$$c_{1}\left(K_{X}^{-1} \otimes\left[D^{\prime}\right]\right) \cdot\left(f^{\star} \omega \mathcal{y}\right)^{m-1}=c_{1}\left(K_{X}^{-1}\right) \cdot\left(f^{\star} \omega \mathcal{y}\right)^{m-1}=\frac{1}{q} c_{1}\left(K_{X}^{-q} \otimes[D]\right) \cdot\left(f^{\star} \omega \mathcal{y}\right)^{m-1},$$
for $f=g \circ \tilde{\varphi}$. Now,
$$c_{1}\left(K_{X}^{-q} \otimes[D]\right) \cdot\left(f^{\star} \omega \mathcal{y}\right)^{m-1}=c_{1}\left(\operatorname{det} V^{\prime} \otimes(\operatorname{det} W)^{-m}\right) \cdot\left(f^{\star} \omega_{\mathcal{Y}}\right)^{m-1}=-\frac{m+1}{4 \pi} \int_{X}\left(f^{\star} \omega_{\mathcal{Y}}\right)^{m}$$
because $K_{X}^{-q} \otimes[D]$ and $\operatorname{det} V^{\prime} \otimes(\operatorname{det} W)^{-m}$ are isomorphic outside codimension 2. Hence
$$c_{1}(I) \cdot\left(f^{\star} \omega_{\mathcal{Y}}\right)^{m-1}=-\frac{1}{2 \pi} \frac{m+1}{2 q} \int_{X}\left(f^{\star} \omega_{\mathcal{Y}}\right)^{m} .$$

On the other hand, $c_{1}(I) \cdot\left(f^{\star} \omega_{\mathcal{Y}}\right)^{m-1}$ can be computed using the fact that $I$ is a subbundle of $W^{\star} \otimes V^{\prime}$ (outside codimension 2). If $\sigma$ is its second fundamental form in $W^{\star} \otimes V^{\prime}$, then the first Chern form of $I$ is
$$\frac{i}{2 \pi} \operatorname{tr}\left(R^{I}\right)=\frac{i}{2 \pi}\left(\operatorname{tr}\left(R_{\mid I}^{W^{\star} \otimes V^{\prime}}\right)-\operatorname{tr}\left(\sigma \wedge \sigma^{\star}\right)\right) .$$
Around a point $x$ in the dense open subset of $X$ where $\mathrm{d} f: T_{X} \longrightarrow I \subset W^{\star} \otimes V^{\prime}$ is injective we choose local coordinates $\left\{z_{k}\right\}$ such that $\beta_{k}:=\mathrm{d} f\left(\frac{\partial}{\partial z_{k}}\right)$ is an orthonormal basis of the fiber of $I$ at $x$ with respect to the metric $f^{\star} \omega \mathcal{Y}$. We identify the fiber of $W^{\star} \otimes V^{\prime}$ with the space of $q \times q m$ complex matrices endowed with the pull-back of the Hermitian scalar product $h$ on $T_{\mathcal{Y}}$, see Subsection 4.1. Then, $f^{\star} \omega_{\mathcal{Y}}=\frac{i}{2} \sum_{k} d z_{k} \wedge d \bar{z}_{k}$ and $R^{W^{\star} \otimes V^{\prime}} \xi=-\sum_{j, k}\left(\beta_{j}{ }^{t} \bar{\beta}_{k} \xi+\xi^{t} \bar{\beta}_{k} \beta_{j}\right) d z_{j} \wedge d \bar{z}_{k}$, so that
$$\operatorname{tr}\left(R_{\mid I}^{W^{\star} \otimes V^{\prime}}\right)=-4 \sum_{j, k, l} \operatorname{tr}\left({ }^{t} \bar{\beta}_{l} \beta_{j}{ }^{t} \bar{\beta}_{k} \beta_{l}+{ }^{t} \bar{\beta}_{l} \beta_{l}{ }^{t} \bar{\beta}_{k} \beta_{j}\right) d z_{j} \wedge d \bar{z}_{k} .$$
Hence,
$$\begin{aligned}
i \operatorname{tr}\left(R_{\mid I}^{W^{\star} \otimes V^{\prime}}\right) \wedge\left(f^{\star} \omega y\right)^{m-1} & =-\frac{8}{m}\left(\sum_{k, l} \operatorname{tr}\left({ }^{t} \bar{\beta}_{l} \beta_{k}{ }^{t} \bar{\beta}_{k} \beta_{l}+{ }^{t} \bar{\beta}_{l} \beta_{l}{ }^{t} \bar{\beta}_{k} \beta_{k}\right)\right)\left(f^{\star} \omega \mathcal{y}\right)^{m} \\
& \leq-\frac{8}{m}\left(\sum_{k} \operatorname{tr}\left(\bar{\beta}_{k} \beta_{k}\right)^{2}+\operatorname{tr}\left(\sum_{k}{ }^{t} \bar{\beta}_{k} \beta_{k}\right)^{2}\right)\left(f^{\star} \omega \mathcal{y}\right)^{m} \\
& \leq-\frac{8}{q m}\left(\sum_{k}\left(\operatorname{tr}^{t} \bar{\beta}_{k} \beta_{k}\right)^{2}+\left(\sum_{k} \operatorname{tr} \bar{\beta}_{k} \beta_{k}\right)^{2}\right)\left(f^{\star} \omega \mathcal{y}\right)^{m} \\
& =-\frac{m+1}{2 q}\left(f^{\star} \omega \mathcal{y}\right)^{m} .
\end{aligned}$$
By continuity, this inequality holds at the points where both sides are defined, namely outside a codimension 2 subset of $X$.

Summing up, we have
$$\begin{aligned}
-\frac{m+1}{2 q} \int_{X}\left(f^{\star} \omega \mathcal{y}\right)^{m} & =(2 \pi) c_{1}(I) \cdot\left(f^{\star} \omega \mathcal{y}\right)^{m-1} \\
& \leq-\frac{m+1}{2 q} \int_{X}\left(f^{\star} \omega \mathcal{y}\right)^{m}-\int_{X} i \operatorname{tr}\left(\sigma \wedge \sigma^{\star}\right) \wedge\left(f^{\star} \omega \mathcal{y}\right)^{m-1} .
\end{aligned}$$
Therefore the semipositive form $i \operatorname{tr}\left(\sigma \wedge \sigma^{\star}\right) \wedge\left(f^{\star} \omega \mathcal{y}\right)^{m-1}$ vanishes, and equality holds in the inequality $i \operatorname{tr}\left(R_{\mid I}^{W^{\star} \otimes V^{\prime}}\right) \wedge\left(f^{\star} \omega_{\mathcal{Y}}\right)^{m-1} \leq-\frac{m+1}{2 q}\left(f^{\star} \omega_{\mathcal{Y}}\right)^{m}$. The first point means that the second fundamental form of $I$ is zero on the dense open set where it is defined and $f^{\star} \omega \mathcal{y}$ is positive definite, so that $f$ maps $\widetilde{X}$ into a totally geodesic $m$-dimensional submanifold $\mathcal{Z}$ of $\mathcal{Y}$. The second one implies that for all $k \neq l$, all the column vectors of $\beta_{k}$ are orthogonal to all the column vectors of $\beta_{l}$, and that for all $k$ the column vectors of $\beta_{k}$ are pairwise orthogonal
and have the same norm (w.r.t. the standard Hermitian scalar product on $\mathbb{C}^{q m}$ ). Using the formula for the holomorphic sectional curvature in $\mathcal{Y}$, we see that the holomorphic sectional curvature of every complex line in $\mathrm{d} f\left(T_{\widetilde{X}}\right) \subset T_{\mathcal{Y}}$ equals $-\frac{1}{q}$. Hence the totally geodesic submanifold $\mathcal{Z}$ is indeed a ball $\mathbb{B}^{m}$ of maximal possible holomorphic sectional curvature in $\mathcal{Y}$.

We are ready to prove that $X_{\text {can }}$ is smooth. We may consider that the target of the maps $f$ and $g$ is $\mathcal{Z}$, and that they are equivariant with respect to the induced representation of $\pi_{1}(X)$ in the automorphism group $\operatorname{Aut}(\mathcal{Z})$ of $\mathcal{Z}$, which will be still denoted by $\rho$. Note that this new representation is still maximal as a representation in the rank one Lie group $\operatorname{Aut}(\mathcal{Z})$. Indeed, the maximality of the initial representation means that
$$\int_{X} f^{\star} \omega \mathcal{Y} \wedge c_{1}\left(\varphi^{\star} K_{X_{\mathrm{can}}}\right)^{m-1}=\frac{q}{m+1} \int_{X} c_{1}\left(\varphi^{\star} K_{X_{\mathrm{can}}}\right)^{m}$$
but if $\omega_{\mathcal{Z}}$ denotes the complex hyperbolic metric on $\mathcal{Z}$ normalized to have constant holomorphic sectional curvature $-1, \omega_{\mathcal{Z}}=\left.\frac{1}{q} \omega_{\mathcal{Y}}\right|_{\mathcal{Z}}$, so that
$$\int_{X} f^{\star} \omega_{\mathcal{Z}} \wedge c_{1}\left(\varphi^{\star} K_{X_{\mathrm{can}}}\right)^{m-1}=\frac{1}{m+1} \int_{X} c_{1}\left(\varphi^{\star} K_{X_{\mathrm{can}}}\right)^{m},$$
which is exactly the maximality of $\rho: \pi_{1}(X) \longrightarrow \operatorname{Aut}(\mathcal{Z})$.
If $X_{\text {can }}$ were indeed smooth and $\rho(\Gamma)$ discrete and torsion free, the adjunction formula would immediately implies that $K_{X_{\text {can }}}=g^{\star} K_{Z}+R$ where $Z=\rho(\Gamma) \backslash \mathcal{Z}$ and $R$ is the ramification divisor. In fact, neither the (possible) singularities of $X_{\text {can }}$ nor the non discreteness of $\rho(\Gamma)$ are an obstruction for such a formula to hold. Indeed, the line bundle $g^{\star} K_{\mathcal{Z}}$ goes down on $X_{\text {can }}$ where it defines a Cartier divisor. On the smooth part $X_{\text {can }}^{0}$ of $X_{\text {can }}$, thanks to its equivariance, the Jacobian of $g$ defines a (nonzero) section of $K_{X_{\text {can }}^{0}} \otimes g^{\star} K_{\mathcal{Z}}^{-1}$ and we denote by $R^{0}$ its zero divisor. Then, on $X_{\text {can }}^{0}$, we have the relation $K_{X_{\text {can }}^{0}}=\left(g^{\star} K_{\mathcal{Z}}\right)_{\mid X_{\text {can }}^{0}}+R^{0}$. Recall that $X_{\text {can }} \backslash X_{\text {can }}^{0}$ is at least 2-codimensional, and since $K_{X_{\text {can }}}$ and $g^{\star} K_{\mathcal{Z}}$ are $\mathbb{Q}$-Cartier, if $R$ denotes the compactification of the divisor $R^{0}$, we have $K_{X_{\text {can }}}=g^{\star} K_{\mathcal{Z}}+R$.

By the maximality of the Toledo invariant,
$$K_{X_{\mathrm{can}}}^{m}=f^{\star} K_{\mathcal{Z}} \cdot\left(\varphi^{\star} K_{X_{\mathrm{can}}}\right)^{m-1}=g^{\star} K_{\mathcal{Z}} \cdot K_{X_{\mathrm{can}}}^{m-1}=K_{X_{\mathrm{can}}}^{m}-R \cdot K_{X_{\mathrm{can}}}^{m-1}$$
and the ampleness of $K_{X_{\text {can }}}$ implies that $R=0$ because $R$ is effective. We conclude that in fact $K_{X_{\text {can }}}=g^{\star} K_{\mathcal{Z}}$ and $g$ is a local biholomorphism on $\widetilde{X}_{\text {can }} \backslash \widetilde{A}$.

We then remark that each point $x \in X_{\text {can }}$ is isolated in the fiber $g^{-1}(g(x))$. Again, if $\rho(\Gamma)$ is discrete and torsion free we are done because a positive dimensional irreducible component of $g^{-1}(g(x))$ then defines a $s$-dimensional subvariety $S \subset X_{\text {can }}$ (for some $s>0$ ) on which $g^{\star} K_{\mathcal{Z}}$ is trivial and $K_{X_{\text {can }}}^{s} \cdot S=\left(g^{\star} K_{\mathcal{Z}}\right)^{s} \cdot S=0$ contradicts the ampleness of $K_{X_{\text {can }}}$. In the general case, we consider the set $\left\{x \in \tilde{X}_{\text {can }}, \operatorname{dim}_{x} g^{-1}(g(x))>0\right\}$. This set is analytic (see [F], Theorem 3.6) and $\pi_{1}\left(X_{\text {can }}\right)$-invariant thus it defines an analytic subset of $X_{\text {can }}$. If it is nonempty and $S$ is a $s$-dimensional irreducible component of it, we also have $K_{X_{\text {can }}}^{s} \cdot S=0$.

Now, we can apply Proposition 3.1.2 in [GR]: for any $x \in \widetilde{X}_{\text {can }}$, there exists open neigh-borhoods $U$ of $x$ in $\widetilde{X}_{\text {can }}$ and $V$ of $g(x)$ in $\mathcal{Z}$ with $g(U) \subset V$, such that the induced map $g_{U, V}: U \longrightarrow V$ is a (proper) finite holomorphic map (that is a finite branched covering) and such that $g_{U, V}^{-1}\left(g_{U, V}(x)\right)=\{x\}$. In fact, it follows from the purity of ramification locus (see the very beginning of [N]) that for any $x^{\prime} \in U, \mathcal{O}_{g\left(x^{\prime}\right), V}$ and $\mathcal{O}_{x^{\prime}, U}$ are isomorphic. Indeed, the ramification locus of $g$, if non empty, should be of pure codimension one and hence would intersect the smooth part of $U$. But we saw above that $g$ is a local biholomorphism on $\widetilde{X}_{\text {can }} \backslash \widetilde{A}$. Therefore, $U$ is (maybe only locally) biholomorphic to $V$, and $X_{\text {can }}$ is smooth.

Finally, the map $g: \tilde{X}_{\text {can }} \longrightarrow \mathbb{B}^{m}$ is a local biholomorphism and thus $X_{\text {can }}$ can be endowed with a metric of constant holomorphic sectional curvature -1, so that it is indeed uniformized by the ball $\mathbb{B}^{m}$. It follows immediately that $g$ is proper and that $\rho$ is discrete and faithful. \(\square\)

\section*{References}
\begin{itemize}
\item[] [BCHM] C. Birkar, P. Cascini, C. D. Hacon, J. McKernan, Existence of minimal models for varieties of log general type, arXiv:math/0610203v1, 2006 3, 4, 10
\item[] [BGG1] S. B. Bradlow, O. Garcia-Prada and P. B. Gothen, Surface group representations and $\mathrm{U}(p, q)$-Higgs bundles, J. Diff. Geom. 64, 2003, 111-170 2
\item[] [BGG2] S. B. Bradlow, O. Garcia-Prada and P. B. Gothen, Maximal surface group representations in isometry groups of classical Hermitian symmetric spaces, Geom. Dedicata 122, 2006, 185-213 2
\item[] [BI] M. Burger and A. Iozzi, Bounded differential forms, generalized Milnor-Wood inequality and an application to deformation rigidity, Geom. Dedicata 125, 2007, 1-23 1 , 2
\item[] [BIW] M. Burger, A. Iozzi and A. Wienhard, Surface group representations with maximal Toledo invariant, to appear in Ann. of Math. 2
\item[] [C] K. Corlette, Flat $G$-bundles with canonical metrics, J. Diff. Geom. 28, 1988, 361-382 2 , 12
\item[] [D1] M. Deraux, On the universal cover of certain exotic Kähler surfaces of negative curvature, Math. Ann. 329, 2004, 653-683 3
\item[] [D2] M. Deraux, A negatively curved Kähler threefold not covered by the ball, Invent. Math. 160, 2005, 501-525 3
\item[] [E] I. Enoki, Stability and negativity for tangent sheaves of minimal Kähler spaces, Geometry and analysis on manifolds (Katata/Kyoto, 1987), Lecture Notes in Math. 1339, Springer, Berlin, 1988, 118-126 12
\item[] [EM] P. Eyssidieux and N. Mok, On the validity or failure of gap rigidity for certain pairs of bounded symmetric domains, Asian J. Math. 8, 2004, 773-794 4 , 15
\item[] [F] G. Fischer, Complex analytic geometry, Lecture Notes in Mathematics 538, Springer-Verlag, Berlin-New York, 1976 [17]
\item[] [GM] W. M. Goldman and J. J. Millson, Local rigidity of discrete groups acting on complex hyperbolic space, Invent. Math. 88, 1987, 495-520 2
\item[] [GR] H. Grauert and R. Remmert, Coherent analytic sheaves, Grundlehren der Mathematischen Wissenschaften 265, Springer-Verlag, Berlin, 198417
\item[] [GS] P. Griffiths and W. Schmid, Locally homogeneous complex manifolds, Acta Math. 123, 1969, 253-302 5
\item[] [He] S. Helgason, Differential geometry, Lie groups, and symmetric spaces, Graduate Studies in Mathematics 34, American Mathematical Society, Providence, RI, 20018
\item[] [Hi1] N. J. Hitchin, The self-duality equations on a Riemann surface, Proc. London Math. Soc. 55, 1987, 59-126 2
\item[] [Hi2] N. J. Hitchin, Lie groups and Teichmüller space, Topology 31, 1992, 449-473 2
\item[] [Ka] Y. Kawamata, The Zariski decomposition of log-canonical divisors, Algebraic geometry, Bowdoin, 1985 (Brunswick, Maine, 1985), Proc. Sympos. Pure Math. 46, Part 1, Amer. Math. Soc., Providence, RI, 1987, 425-433 10
\item[] [KMM] Y. Kawamata, K. Matsuda and K. Matsuki, Introduction to the minimal model problem, Adv. Stud. Pure Math. 10, North-Holland, Amsterdam, 1987, 283-360 9
\item[] [Kl] B. Klingler, Sur la rigidité de certains groupes fondamentaux, l'arithméticité des réseaux hyperboliques complexes, et les "faux plans projectifs", Invent. Math. 153, 2003, 105-143 4
\item[] [Kn] A. W. Knapp, Lie groups beyond an introduction, second edition, Progress in Mathematics 140, Birkhäuser Boston, Inc., Boston, MA, 2002 [5, 7]
\item[] [Ko] S. Kobayashi, Differential geometry of complex vector bundles, Princeton University Press, 1987 4, 13
\item[] [KM1] V. Koziarz and J. Maubon, Harmonic maps and representations of non-uniform lattices of $\mathrm{PU}(m, 1)$, Ann. Inst. Fourier (Grenoble) 58, 2008, 507-558 2 , 13
\item[] [KM2] V. Koziarz and J. Maubon, Representations of complex hyperbolic lattices into rank 2 classical Lie Groups of Hermitian type, Geom. Dedicata, DOI 10.1007/s10711-008-9288-3 [2 3, 1314
\item[] [L] X. Liu, Curvature estimates for irreducible symmetric spaces, Chinese Ann. Math. Ser. B 27, 2006, 287-302 (in Chinese), arXiv:math/0505626v1, 2005 (English version) 8
\end{itemize}
\begin{itemize}
\item[] [Mo] N. Mok, Factorization of semisimple discrete representations of Kähler groups, Invent. Math. 110, 1992, 557-614 3
\item[] [Mu] S. Murakami, Sur certains espaces fibrés principaux différentiables et holomorphes, Nagoya Math. J 15, 1959, 171-199 5
\item[] [N] M. Namba, Branched coverings and algebraic functions, Pitman Research Notes in Mathematics Series 161, Longman Scientific \& Technical, Harlow; John Wiley \& Sons, Inc., New York, 1987 [17]
\item[] [R] A. Reznikov, All regulators of flat bundles are torsion, Ann. of Math. 141, 1995, 373-386 4
\item[] [Sim1] C. T. Simpson, Constructing variations of Hodge structure using Yang-Mills theory and applications to uniformization, J. Amer. Math. Soc. 1, 1988, 867-918 2 12
\item[] [Sim2] C. T. Simpson, Higgs bundles and local systems, Inst. Hautes Études Sci. Publ. Math. 75, 1992, 5-95 2
\item[] [Siu] Y.-T. Siu, The complex-analyticity of harmonic maps and the strong rigidity of compact Kähler manifolds, Ann. of Math. 112, 1980, 73-111 2
\item[] [Ta] S. Takayama, Local simple connectedness of resolutions of log-terminal singularities, Internat. J. Math. 14, 2003, 825-836 15
\item[] [To1] D. Toledo, Harmonic mappings of surfaces to certain Kähler manifolds, Math. Scand. 45, 1979, 13-26 2
\item[] [To2] D. Toledo, Representations of surface groups in complex hyperbolic space, J. Diff. Geom. 29, 1989, 125-133 2
\item[] [Z] K. Zuo, Kodaira dimension and Chern hyperbolicity of the Shafarevich maps for representations of compact Kähler manifolds, J. reine angew. Math. 472, 1996, 139-156 3
\end{itemize}

IECN, Nancy-Université, CNRS, INRIA, Boulevard des Aiguillettes B. P. 239, F-54506
Vandeuvre-lès-Nancy, France
E-mail address: koziarz@iecn.u-nancy.fr
E-mail address: maubon@iecn.u-nancy.fr