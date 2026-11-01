---
retention_scope: session
part: 1
total_parts: 4
---

[Part 1/4 of: New non-arithmetic complex hyperbolic lattices]

---
source_file: 1401_0308.pdf
converter: mathpix
format: mmd
---

\title{
New non-arithmetic complex hyperbolic lattices
}

\author{
Martin Deraux, John R. Parker, Julien Paupert
}

May 15, 2015

\begin{abstract}
We produce a family of new, non-arithmetic lattices in PU(2, 1). All previously known examples were commensurable with lattices constructed by Picard, Mostow, and Deligne-Mostow, and fell into 9 commensurability classes. Our groups produce 5 new distinct commensurability classes. Most of the techniques are completely general, and provide efficient geometric and computational tools for constructing fundamental domains for discrete groups acting on the complex hyperbolic plane.
\end{abstract}

\section*{1 Introduction}

The general context of this paper is the study of lattices in semisimple Lie groups and their classification. In what follows, $X$ denotes an irreducible symmetric space of non-compact type, and $G$ denotes its isometry group. Recall that $X$ is a homogeneous space $G / K$ with $K$ a maximal compact subgroup of $G$, and up to scale, it carries a unique $G$-invariant Riemannian metric.

A subgroup $\Gamma \subset G$ is called a lattice if $\Gamma \backslash G$ has finite Haar measure (equivalently, if $\Gamma \backslash X$ has finite Riemannian volume for the invariant metric on $X$ ). Mostow-Prasad rigidity says that, for most symmetric spaces, a given lattice $\Gamma$ in $G$ admits a unique discrete faithful representation into $G$ (unique in the sense that all such representation are conjugate in $G$ ). In order for this to hold, the only case to exclude is $X=\mathbf{H}_{\mathbb{R}}^{2}$ (equivalently $G=\operatorname{PSL}_{2}(\mathbb{R})$ ), where lattices are known to admit pairwise non-conjugate continuous deformations.

The discreteness assumption in the statement of the Mostow-Prasad rigidity theorem cannot be removed, since Galois automorphisms sometimes produce non-discrete representations that are clearly faithful and type-preserving (see the non-standard homomorphisms constructed in [Mos80], and also Section 6.2 of the present paper). This is related to the notion of arithmeticity of lattices, which we now briefly recall.

There is a general construction of lattices, obtained by taking integer matrices in the set of real points of linear algebraic groups defined over $\mathbb{Q}$; this is a special case of the more general notion of arithmetic group, where one considers lattices commensurable with the image of an integral group under surjective homomorphisms with compact kernel (see [Mar91] for instance). Recall for further reference that subgroups $\Gamma_{1}$ and $\Gamma_{2}$ of a group $G$ are commensurable if there is a $g \in G$ such that $\Gamma_{1} \cap g \Gamma_{2} g^{-1}$ has finite index in both $\Gamma_{1}$ and $g \Gamma_{2} g^{-1}$.

Arithmetic groups are classified, and they can be understood (up to commensurability) from purely number-theoretical data (see [Wei60], [Tit66]). Indeed, it follows from rigidity that any lattice in a simple real Lie group not isomorphic to $\operatorname{PSL}_{2}(\mathbb{R})$ is defined over a number field, and semisimple groups over arbitrary number fields can be classified in a way similar to the well known classification of semisimple groups over $\mathbb{Q}$ (one uses Dynkin diagrams
with a symmetry corresponding to the action of the Galois group of the number field). The arithmeticity condition says that the lattice is given up to commensurability by taking the corresponding $\mathbb{Z}$-points in the group, hence there are only countably many arithmetic lattices (since there are only countably many number fields).

It follows from work of Margulis [Mar75], together with work of Corlette [Cor92] and Gromov-Schoen [GS92], that most lattices are arithmetic; given the discussion in the previous paragraph, this means that there is a satisfactory classification of lattices in most semisimple Lie groups. More specifically, if the isometry group $G$ of a symmetric space $X=G / K$ of non-compact type contains a non-arithmetic lattice, then $X$ can only be $\mathbf{H}_{\mathbb{R}}^{n}$ or $\mathbf{H}_{\mathbb{C}}^{n}$ for some $n$; in other words, up to index $2, G$ can only be $\operatorname{PO}(n, 1)$ or $\operatorname{PU}(n, 1)$.

Real hyperbolic space $\mathbf{H}_{\mathbb{R}}^{n}$ is the model $n$-dimensional negatively curved space form, i.e. it is the unique complete simply connected Riemannian manifold of constant negative curvature (we may assume that constant is -1). Similary, $\mathbf{H}_{\mathbb{C}}^{n}$ is the model negatively curved complex space form, in the sense it is the unique complete, simply connected Kähler manifold whose holomorphic sectional curvature is a negative constant, which we may assume is -1. With that normalization, the real sectional curvatures of $\mathbf{H}_{\mathbb{C}}^{n}$ vary between -1 and -1/4. This makes complex hyperbolic spaces very different from real hyperbolic ones (apart from the coincidence that $\mathbf{H}_{\mathbb{C}}^{1}$ is isometric to $\mathbf{H}_{\mathbb{R}}^{2}$ ).

In the real hyperbolic case, the hybridization procedure described by Gromov and Piatetski-Shapiro [GPS88] allows the construction of (infinitely many commensurability classes of) non-arithmetic lattices in $\operatorname{PO}(n, 1)$ for any $n \geqslant 2$. In $\operatorname{PU}(n, 1)$, it is not clear how to make sense of the construction of such hybrids, and the construction of non-arithmetic lattices in the complex hyperbolic setting is a longstanding challenge.

In fact, for $n \geqslant 2$, only a handful of examples are known. The first ones were constructed by Mostow [Mos80], who showed that some complex reflection groups are non-arithmetic lattices in $\operatorname{Isom}\left(\mathbf{H}_{\mathbb{C}}^{2}\right)$ (the analogous statement was well known for real reflection groups in $\operatorname{Isom}\left(\mathbf{H}_{\mathbb{R}}^{n}\right)$ for low values of $n$, see [Vin68]).

Complex hyperbolic manifolds are of special interest in complex geometry, because of the extremal properties of their ratios of Chern numbers. Indeed, compact complex hyperbolic manifolds are complex manifolds of general type (i.e. their Kodaira dimension is maximal), and they have the same ratios of Chern numbers as complex projective space $\mathbf{P}_{\mathbb{C}}^{n}$, which is the compact symmetric space dual to $\mathbf{H}_{\mathbb{C}}^{n}$ (this is explained by the Hirzebruch proportionality principle). In fact, any compact complex manifold of general type that realizes equality in the Miyaoka-Yau inequality $(-1)^{n} c_{1}^{n} \leq(-1)^{n} \frac{2 n+2}{n} c_{1}^{n-2} c_{2}$ is biholomorphic to a quotient of $\mathbf{H}_{\mathbb{C}}^{n}$ (this is a corollary of the Calabi conjecture, proved by Aubin and Yau). In the special case $n=2$, the corresponding equality reads $c_{1}^{2}=3 c_{2}$, and it plays an important role in so-called surface geography.

In principle, this characterization should give a simple way to produce many complex hyperbolic manifolds, but so far this has been successful in very few cases, only in dimension 2. A spectacular example was obtained by Mumford, using sophisticated techniques from algebraic geometry to produce a fake projective plane, i.e. a compact surface with the same Betti numbers as $\mathbf{P}_{\mathbb{C}}^{2}$ but not biholomorphic to it. The fundamental group of any such surface is infinite, and admits a faithful and discrete representation into PU(2, 1), even though it took a long time for this representation to be made somewhat explicit for Mumford's example (see Kat08]). It is now well known that fake projective planes must be arithmetic (see Kli03] and [Yeu04]), and this was used to classify them (see [PY07] and [CS10]).

Hirzebruch systematically explored coverings of $\mathbf{P}_{\mathbb{C}}^{2}$ branched along configurations of lines,
and found all the ball quotients that could be produced in this way, see [Hir83], [BHH87]. The arithmetic properties of Hirzebruch ball quotients were studied later (see [Shv92]). It turns out that all the non-arithmetic examples can also be obtained from the Deligne-Mostow construction [DM86].

Our construction is closer in spirit to Mostow's approach in [Mos80]. We start with some well-chosen complex reflection groups in PU(2, 1) and show that they are lattices by constructing explicit fundamental domains (the domains are shown to be fundamental domains by applying the Poincaré polyhedron theorem).

The application of this general strategy in the context of complex hyperbolic space is difficult and subtle, as can be seen in the difficulties in Mostow's proof that were analyzed in [Der05]. It has been successfully carried out in several places, but always for groups closely related to Mostow's (see [DFP05], [Par06], [FP06], [Zha12]). For the groups we consider in this paper, the previously used techniques seem difficult to implement (for instance, the Dirichlet domains we studied in [DPP11] have extremely complicated combinatorial structure).

Mostow's lattices turn out to be closely related to monodromy groups of hypergeometric functions studied a century earlier by Picard [Pic81]. The hypergeometric interpretation was extended by Deligne and Mostow [DM86], who showed that these monodromy groups produce a handful of non-arithmetic lattices in PU(2, 1), and a single one in PU(3, 1) (which is currenctly the only known non arithmetic lattice in $\operatorname{PU}(n, 1)$ wih $n \geqslant 3$ ).

Note that the above hypergeometric monodromy groups can also be interpreted as modular groups for moduli spaces of weighted points on $\mathbf{P}_{\mathbb{C}}^{1}$, or equivalently moduli spaces of flat metrics on the sphere with prescribed cone angle singularities (see [Thu98]). The few other examples of moduli spaces that are known to admit a complex hyperbolic uniformization (see [ACT02], [Kon00] for instance) produce arithmetic lattices.

The commensurability relations between Deligne-Mostow lattices were studied in detail in [Sau90] and [DM93], then more recently in [KM12] and [McM13]. In particular, it turns out that non-arithmetic Deligne-Mostow lattices in PU(2, 1) fall into exactly nine commensurability classes.

The main result of this paper produces five new commensurability classes of non-arithmetic lattices in PU(2, 1). They are the first such groups to be constructed since the work of Deligne and Mostow.

We consider groups generated by two isometries, namely a complex reflection and a regular elliptic element of order 3. For historical reasons (see [Mos80]), these two isometries will be denoted respectively by $R_{1}$ and $J$; we will also denote $R_{2}=J R_{1} J^{-1}$ and $R_{3}=J R_{2} J^{-1}$. It turns out that conjugacy classes of such groups are parametrized by the pair $(\psi, \tau)$, where $\psi$ is the rotation angle of $R_{1}$ and $\tau$ is the trace of $R_{1} J$. There are restrictions on the pair $(\psi, \tau)$ for a group with a given angle/trace pair to exist (see the discussion in [PP09]); when it exists, we denote the corresponding group by $\Gamma(\psi, \tau)$.

Following previous work on complex reflection groups (see [Mos80], [Sch02], [Der06], [Tho10]), one expects such groups to be lattices only when well-chosen short words in the generators are elliptic. For instance, for (4,4,4)-triangle groups, Schwartz conjectured that the discreteness was controlled by the word 1232, in the sense that the group should be discrete if and only if $R_{1} R_{2} R_{3} R_{2}$ is loxodromic, parabolic, or elliptic of finite order (here the $R_{j}$ denote the generating complex reflections). The (4,4,4)-triangle group where $R_{1} R_{2} R_{3} R_{2}$ is elliptic of order $n$ (more specifically has eigenvalues $1, e^{ \pm 2 \pi i / n}$ ) is referred to as the (4, 4, 4; $n$ )-triangle group. This seems to have infinite covolume for $n>5$, see for instance the group in [Sch03], which is the (4, 4, 4; 7)-triangle group. On the other hand, it was observed in [Der06] that
the (4, 4, 4; 5)-triangle group is a lattice. When considering (4, 4, 4; n)-triangle groups, an important distinction between $n=5$ and $n \geqslant 6$ is the type of the isometry $R_{1} R_{2} R_{3}=\left(R_{1} J\right)^{3}$, which is loxodromic for $n \geqslant 6$, but elliptic of order 10 when $n=5$. It is then natural to expect the ellipticity of the words 123 and 1232 to control the property of triangle groups to be a lattice. This is confirmed for some other triangle groups by the results in [Tho10].

This motivated us to study groups $\Gamma(\psi, \tau)$ where $R_{1} R_{2}$ and $R_{1} J$ are both elliptic of finite order (in fact we allow $R_{1} R_{2}$ to be parabolic as well, but not $R_{1} J$ ). The groups $\Gamma(\psi, \tau)$ satisfying these conditions were listed by the last two authors (see [Par08] and [PP09]); the key ingredient in their arguments is a result of Conway and Jones [CJ76] that classifies rational relations between roots of unity.

We proved in [DPP11] that only finitely many of these groups can be lattices. We also gave a conjectural list of ten groups that we strongly suspected to be lattices, corresponding to three special choices of $\tau$, namely
$$\sigma_{1}=-1+i \sqrt{2}, \quad \bar{\sigma}_{4}=\frac{-(1+i \sqrt{7})}{2}, \quad \sigma_{5}=e^{-\pi i / 9} \frac{i \sqrt{3}+\sqrt{5}}{2},$$
for some well-chosen rotation angles $\psi$. The main result of this paper is the following:
Theorem 1.1 Let $\tau=-(1+i \sqrt{7}) / 2$, and let $p \in \mathbb{Z}$. Then $\Gamma(2 \pi / p, \tau)$ is a lattice in $\operatorname{PU}(2,1)$ if and only if $p=3,4,5,6,8$ or 12, and that lattice is
\begin{itemize}
\item[1.] cocompact if and only if $p=3,5,8$ or 12;
\item[2.] arithmetic if and only if $p=3$;
\end{itemize}
Moreover, the six lattices lie in distinct commensurability classes, and they are not commensurable to any Deligne-Mostow lattice.

The values of $p$ in the theorem may seem mysterious, but one can rephrase the theorem as an integrality condition, in the vein of the Picard integrality condition (see [DM86] for instance). Indeed (see section 4.3), $\left(R_{1} R_{2}\right)^{2}$ is a complex reflection with angle $2 \pi / c$, and $\left(R_{1} R_{2} R_{3} R_{2}^{-1}\right)^{3}$ is a reflection with angle $2 \pi / d$, where:
$$c=2 p /(p-4) ; \quad d=2 p /(p-6) .$$
The values of $p$ in the theorem are precisely those for which both $c$ and $d$ are integers (or infinite).

Non-arithmeticity of these groups was proved in [Pau10]. For completeness, we prove that the five commensurability classes are new and distinct in Section 6, and recall the proof of non-arithmeticity in Section 6.2; see also [Pau10]. The fact that the groups are non-discrete for all other integer values of $p$ was proved in [DPP11].

We prove that the six groups that appear in Theorem 1.1 are lattices by constructing explicit fundamental polyhedra for their respective actions on $\mathbf{H}_{\mathbb{C}}^{2}$, using Theorem 3.2. By this method we obtain presentations of the lattices:

Theorem 1.2 Let $\tau=-(1+i \sqrt{7}) / 2$. For $p=3,4,5,6,8,12$ the group $\Gamma(2 \pi / p, \tau)$ has the presentation:
$$\left\langle\begin{array}{c}
R_{1}^{p}=J^{3}=\left(R_{1} J\right)^{7}=i d, R_{2}=J R_{1} J^{-1}, R_{3}=J^{-1} R_{1} J, \\
R_{1}, R_{2}, R_{3}, J \mid \\
\left(R_{1} R_{2}\right)^{2}=\left(R_{2} R_{1}\right)^{2},\left(R_{1} R_{2}\right)^{4 p /(p-4)}=\left(R_{1} R_{2} R_{3} R_{2}^{-1}\right)^{6 p /(p-6)}=i d
\end{array}\right\rangle .$$
If an exponent is infinite or negative then the relation should be omitted.

Moreover, from the detailed analysis of the polyhedra and the groups, we obtain the orbifold Euler characteristic $\chi$ of the quotient orbifolds (hence their complex hyperbolic volume which is $8 \pi^{2} \chi / 3$ ):

\begin{table}
\captionsetup{labelformat=empty}
\caption{Theorem 1.3 Let $\tau=-(1+i \sqrt{7}) / 2$. Let $\chi(2 \pi / p, \tau)$ be the orbifold Euler characteristic of the orbifold $\Gamma(2 \pi / p, \tau) \backslash \mathbf{H}_{\mathbb{C}}^{2}$. Then $\chi(2 \pi / p, \tau)$ has the following values}
\begin{tabular}[t]{|l|l|l|l|l|l|l|}
\hline $p$ & 3 & 4 & 5 & 6 & 8 & 12 \\
\hline $\chi(2 \pi / p, \tau)$ & 2/63 & 25/224 & 47/280 & 25/126 & 99/448 & 221/1008 \\
\hline
\end{tabular}
\end{table}

These statements prove our conjecture from [DPP11] for five groups out of ten. The corresponding statement about lattices with $\tau=\sigma_{1}$ and $\tau=\sigma_{5}$ would follow from similar techniques, but some of the verifications are too tedious to be written up here.

For a fixed value of $\tau$ the number of sides of the domain is the same, and the combinatorial structure is very similar. For each of the groups presented in the paper, the domain has 28 sides, but there are only two isometry types of sides (the domain is invariant under a regular elliptic element of order 7, and sides are paired isometrically). This decreases the complexity enough to make it possible to present most of the proof in detail on paper.

For $\sigma_{1}$ (resp. $\sigma_{5}$ ), our construction would produce a polyhedron with 64 (resp. 130) sides, and there would be four (resp. three) isometry types of sides. This makes some of the verifications longer, but not more difficult in any essential way. One important place where the arguments would be more painful is the verification that the bounding pyramids glue to build a copy of $S^{3}$, see section 4.7 of the present paper. In these more complicated cases, one could resort to the solution of the Poincaré conjecture, and check only that the bounding 3-complex is a manifold with trivial fundamental group; that argument can easily be automatized, but the computation would be difficult to write down on paper.

Our main results are proved using a standard application of the Poincaré polyhedron theorem, but we also provide new, useful techniques for studying fundamental domains for lattices in $\operatorname{PU}(2,1)$.

We apply systematic techniques for producing a fundamental domain with fairly simple combinatorics and with sides contained in bisectors (as other nice features, all vertices are fixed by specific isometries in the group, and all 1-faces of our polyhedron are chosen to be geodesic arcs). These techniques, which were in part inspired by the construction in [Sch03], will be briefly summarized in section 4.4.

Another novel aspect is the provision of efficient computational tools in Section 4.8 for certification of the combinatorics of a polyhedron bounded by (finitely many) bisectors. We summarize these techniques, since they have not systematically been used in the literature.

The determination of the combinatorics amounts to solving a system of (finitely many) quadratic inequalities in the real and imaginary parts of ball coordinates, for which no standard computational techniques are known. The main difficulty is to determine which pairs of bisectors contain a non-empty 2-face, and to give a precise list of the vertices and edges adjacent to that 2-face.

Using geometric properties of bisectors and bisector intersections (see Section 2.3), we can give parameters for any intersection $\mathscr{B}_{1} \cap \mathscr{B}_{2}$ of bisectors, and write explicit equations for the intersection $\mathscr{B}_{1} \cap \mathscr{B}_{2} \cap \mathscr{B}_{3}$ for any third bisector $\mathscr{B}_{3}$. For well-chosen parametrizations, these equations are given by polynomials in two variables, quadratic in each variable. This is a consequence of the fact that the (hyperbolic cosine of the) distance between two points in
$\mathbf{H}_{\mathbb{C}}^{2}$ is given by a quadratic polynomial in the real and imaginary part of affine coordinates for the points. The coefficients of these polynomial equations are algebraic numbers (in fact, they lie in the adjoint trace field), which allows for arbitrary precision calculations.

The determination of the combinatorics is then reduced to the minimization of finitely many polynomials in two variables on finitely many polygonal regions, where the polygons are bounded by plane curves of degree at most two. We perform this minimization by computing the critical points of the above polynomials, which can be done by exact computations since the coefficients are known exactly. Even though these verifications can in principle be performed by hand, it is most reasonable to use a computer, given the large number of computations. Open source software that performs the necessary checks is available on the first author's web page.

Most of these techniques are completely general, and can be used to reduce the certification of fundamental domains for discrete subgroups of PU(2, 1) to a finite number of verifications. Note that the determination of fundamental domains is clearly important in the context of the search of non-arithmetic lattices, but it is also important for arithmetic ones, where discreteness comes for free. For instance, the determination of explicit group presentations for small covolume arithmetic lattices in $\operatorname{PU}(2,1)$ allowed Cartwright and Steger to complete the classification of fake projective planes (see [PY07] and [CS10]).

The paper is organized as follows. In Sections 2 and 3 we give well-known background material. Section 4 starts by establishing basic notation for the specific groups we study in the paper. We then sketch the general procedure that was used in order to produce the combinatorial model for our fundamental polyhedron (Sections 4.3 and 4.4).

The details of the combinatorial model $\widehat{E}$ for the groups that appear in this paper (incidence properties of facets of various dimensions) are discussed in Section 4.6, and the strategy to show that it is homeomorphic to its geometric realization $E$ is outlined in Section 4.6.2. To that end, an important point is to show that the 3-skeleton of $\widehat{E}$ is homeomorphic to $S^{3}$, which is proved in section 4.7. We then show that the geometric realization of $\widehat{E}$ is embedded, see Section 4.8, apply the Poincaré polyhedron theorem to $E$ in order to show that our groups are lattices, Section 5; and finally we show that these lattices are non-arithmetic and not commensurable to each other or to any Deligne-Mostow lattice, Section 6.
Acknowledgements: The authors would like to thank the following institutions for their support during the preparation of this paper, in chronological order: the University of Utah, Université de Fribourg, Durham University, Université de Grenoble, Arizona State University. The authors acknowledge support from the ANR through the program "Structures Géométriques et Triangulations", NSF grants DMS 1107452, 1107263, 1107367 (the GEAR Network) and ICERM at Brown University. The third author was also partially supported by SNF grant 200020-121506/1 and NSF grant DMS 1007340/1249147. The authors would also like to thank Bernard Parisse and Fabrice Rouillier for useful assistance on the computational aspects of this project, as well as the referee for several suggestions which improved the exposition of the paper.

\section*{2 Complex hyperbolic geometry}

We define complex hyperbolic space, introduce totally geodesic subspaces and bisectors, and review properties of bisector intersections. Most of this material may be found in [Gol99].

\subsection*{2.1 Complex hyperbolic space}

We define $\mathbf{H}_{\mathbb{C}}^{n}$ to be the subset of $\mathbf{P}_{\mathbb{C}}^{n}$ consisting of negative complex lines in $\mathbb{C}^{n, 1}$. Here $\mathbb{C}^{n, 1}$ denotes $\mathbb{C}^{n+1}$ equipped with a Hermitian form of signature $(n, 1)$, and a negative line is one spanned by a vector $\mathbf{u} \in \mathbb{C}^{n, 1}$ with $\langle\mathbf{u}, \mathbf{u}\rangle<0$. There is a natural action on $\mathbf{H}_{\mathbb{C}}^{n}$ of the unitary group of the Hermitian form, which is denoted by $\mathrm{U}(n, 1)$. We shall often work with $\mathrm{SU}(n, 1)$, which is an $(n+1)$-fold cover of the projective group $\mathrm{PU}(n, 1)$.

Up to scaling, $\mathbf{H}_{\mathbb{C}}^{n}$ carries a unique $\mathrm{U}(n, 1)$-invariant Riemannian metric, which makes it a symmetric space. It is well known that $\mathbf{H}_{\mathbb{C}}^{n}$ is a complex space form, in fact the holomorphic sectional curvature of the above metric is equal to -1. This implies that real sectional curvatures are pinched between -1 and -1/4 (when $n=1$ the curvature is in fact constant).

It is a standard fact that the group of holomorphic isometries of $\mathbf{H}_{\mathbb{C}}^{n}$ is precisely $\operatorname{PU}(n, 1)$. The full group $\operatorname{Isom}\left(\mathbf{H}_{\mathbb{C}}^{n}\right)$ contains $\operatorname{PU}(n, 1)$ with index 2, the other component consisting of all anti-holomorphic isometries (an example of which is complex conjugation in affine coordinates, provided that the Hermitian form has real entries).

The only metric information we will need in this paper is the following distance formula:
$$\cosh \left(\frac{d(u, v)}{2}\right)=\frac{|\langle\mathbf{u}, \mathbf{v}\rangle|}{\sqrt{\langle\mathbf{u}, \mathbf{u}\rangle\langle\mathbf{v}, \mathbf{v}\rangle}},$$
where u, v denote lifts of $u, v$ to $\mathbb{C}^{n+1}$. The standard choice of a Hermitian form of signature $(n, 1)$ is the Lorentzian form
$$\langle\mathbf{u}, \mathbf{v}\rangle=-u_{0} \bar{v}_{0}+u_{1} \bar{v}_{1}+\cdots+u_{n} \bar{v}_{n} .$$
In the affine coordinates $\left(z_{1}, \ldots, z_{n}\right)=\left(u_{1} / u_{0}, \ldots, u_{n} / u_{0}\right)$ for the chart $\left\{u_{0} \neq 0\right\}$ of $\mathbf{P}_{\mathbb{C}}^{n}$, complex hyperbolic space corresponds to the unit ball $\left|z_{1}\right|^{2}+\cdots+\left|z_{n}\right|^{2}<1$. We will denote $\overline{\mathbf{H}}_{\mathbb{C}}^{n}=\mathbf{H}_{\mathbb{C}}^{n} \cup \partial \mathbf{H}_{\mathbb{C}}^{n}$ the corresponding closed ball.

We will use the standard classification of isometries of negatively curved spaces into elliptic, parabolic and hyperbolic isometries, with the following refinements. An elliptic element of $\operatorname{PU}(n, 1)$ is called regular elliptic if any of its lifts to $\mathrm{U}(n, 1)$ has distinct eigenvalues. In particular, regular elliptic isometries have isolated fixed points in $\mathbf{H}_{\mathbb{C}}^{n}$ (given by the single negative eigenspace). When $n=2$, non-regular elliptic isometries of $\mathbf{H}_{\mathbb{C}}^{2}$ have two distinct eigenvalues, one simple and one double eigenvalue. These elements are called complex reflections in points or in lines, depending on the sign of the simple eigenspace.

\subsection*{2.2 Totally geodesic subspaces}

If $V \subset \mathbb{C}^{n, 1}$ is any complex linear subspace where the restriction of the Hermitian form has signature $(k, 1)$, then the set of negative complex lines in $V$ gives a copy of $\mathbf{H}_{\mathbb{C}}^{k}$, which can easily be checked to be totally geodesic. In terms of the ball model, they correspond to the intersection with the unit ball of complex affine subspaces in $\mathbb{C}^{n}$. When $k=n-1$, the subspaces $V$ as above are simply obtained by taking the orthogonal complement of a positive vector $\mathbf{n}$, which we refer to as a polar vector to the corresponding complex hyperplane. When $k=1$, the complex totally geodesic submanifolds described above are called complex lines, or complex geodesics. Note that there is a unique complex line joining any two distinct points in $\mathbf{H}_{\mathbb{C}}^{n}$.

Similarly, some $\mathbb{R}$-linear subspaces can be used to produce totally geodesic submanifolds, namely those where the Hermitian form restricts to a quadratic form of hyperbolic signature.

These yield copies of $\mathbf{H}_{\mathbb{R}}^{k}, k \leqslant n$ (with real sectional curvature $-1 / 4$ ). For $k=1$ these are precisely the real geodesics, and for $k=2$, they are called $\mathbb{R}$-planes.

It is a standard fact that every complete totally geodesic submanifold is in one of the two families described above (see [Gol99], Section 3.1.11). Note that in particular, there are no totally geodesic real hypersurfaces in complex hyperbolic spaces.

\subsection*{2.3 Bisectors}

The basic building blocks for our fundamental domains are bisectors, which are hypersurfaces equidistant from two given points. Their geometric structure has been analyzed in great detail in [Mos80], [Gol99], we only recall a few facts that will be needed in the paper.

Given two distinct points $p_{0}, p_{1} \in \mathbf{H}_{\mathbb{C}}^{n}$, write
$$\mathscr{B}\left(p_{0}, p_{1}\right)=\left\{u \in \mathbf{H}_{\mathbb{C}}^{n}: d\left(u, p_{0}\right)=d\left(u, p_{1}\right)\right\}$$
for the bisector equidistant from $p_{0}$ and $p_{1}$.
There is some freedom in choosing the pair of points $p_{0}, p_{1}$, but perhaps surprisingly, the possible choices are much more constrained than in constant curvature geometries. Indeed, the points $q_{0}$ for which there exists a $q_{1}$ with $\mathscr{B}\left(q_{0}, q_{1}\right)=\mathscr{B}\left(p_{0}, p_{1}\right)$ all lie on the complex line through $p_{0}$ and $p_{1}$; thus the complex line through the two points is canonically attached to the bisector, and is called its complex spine.

The real spine is the intersection of the complex spine with the bisector itself, which is a (real) geodesic; it is the locus of points inside the complex spine which are equidistant from $p_{0}$ and $p_{1}$. It consists of points $z \in \mathbf{H}_{\mathbb{C}}^{n}$ associated to negative vectors $\mathbf{u} \in \mathbb{C}^{n, 1}$ that are in the complex span of $\mathbf{p}_{0}$ and $\mathbf{p}_{1}$ and that satisfy
$$\left|\left\langle\mathbf{u}, \mathbf{p}_{0}\right\rangle\right|=\left|\left\langle\mathbf{u}, \mathbf{p}_{1}\right\rangle\right|,$$
where $\mathbf{p}_{0}$ and $\mathbf{p}_{1}$ denote lifts of $p_{0}$ and $p_{1}$ to $\mathbb{C}^{n, 1}$ with the same norm (e.g. one could take $\left\langle\mathbf{p}_{0}, \mathbf{p}_{0}\right\rangle=\left\langle\mathbf{p}_{1}, \mathbf{p}_{1}\right\rangle=-1$ ). The nonzero vectors in $\operatorname{Span}_{\mathbb{C}}\left(\mathbf{p}_{0}, \mathbf{p}_{1}\right)$ satisfying (3), but that are not necessarily negative, span a real projective line in $\mathbf{P}_{\mathbb{C}}^{n}$, which we call the extended real spine of the bisector.

We will sometimes describe bisectors by giving two points of their extended real spines; as mentioned in Section 2.2, we can think of a real geodesic as a real 1-dimensional hyperbolic space. Hence, we can describe it as the projectivization of a totally real 2-dimensional subspace of $\mathbb{C}^{n, 1}$, i.e. we take two vectors v and w in $\mathbb{C}^{n+1}$ with $\langle\mathbf{v}, \mathbf{w}\rangle \in \mathbb{R}$, and consider their real span. The simplest way to guarantee that the span really yields a geodesic in $\mathbf{H}_{\mathbb{C}}^{n}$ is to require moreover that $\mathbf{v}$ and $\mathbf{w}$ form a Lorentz basis, i.e. $\langle\mathbf{v}, \mathbf{v}\rangle=-1,\langle\mathbf{w}, \mathbf{w}\rangle=1$ and $\langle\mathbf{v}, \mathbf{w}\rangle=0$.

Recall that bisectors are not fixed point sets of any isometric involution, since they are not totally geodesic. According to the discussion in Section 2.2, there are two kinds of maximal totally geodesic submanifolds contained in a given bisector. The complex ones are called complex slices of $\mathscr{B}$; they are the preimages of points of the real spine under orthogonal projection onto the complex spine. They can also be described as hyperplanes with polar vectors $\mathbf{n} \in \mathbb{C}^{n, 1}$ satisfying $\langle\mathbf{n}, \mathbf{n}\rangle>0$ and $\left|\left\langle\mathbf{n}, \mathbf{p}_{0}\right\rangle\right|=\left|\left\langle\mathbf{n}, \mathbf{p}_{1}\right\rangle\right|$, see equation (3). The totally real submanifolds that are contained in $\mathscr{B}$ are precisely those containing the real spine and are called real slices of $\mathscr{B}$.

\subsection*{2.4 Bisectors and geodesics}

Several times in the paper, we will need to determine when a geodesic arc is contained in a bisector. Recall that bisectors in $\mathbf{H}_{\mathbb{C}}^{2}$ are not convex: given two distinct points $p, q$ in a bisector $\mathscr{B}$, the geodesic through $p$ and $q$ is in general not contained in $\mathscr{B}$. This is stated more precisely in the following (see Theorem 5.5.1 of [Gol99]).

Lemma 2.1 Let $\alpha \subset \mathbf{H}_{\mathbb{C}}^{2}$ be a real geodesic, and let $\mathscr{B}$ be a bisector. Then $\alpha$ is contained in $\mathscr{B}$ if and only if it is contained either in a real slice or in a complex slice of $\mathscr{B}$.

In particular, we have:
Lemma 2.2 Let $u$ and $v$ be distinct points of a bisector $\mathscr{B}$, such that $u$ is on the real spine of $\mathscr{B}$. Then the geodesic through $u$ and $v$ is contained in $\mathscr{B}$.

Indeed, if $v$ is in the complex slice through $u$ this is obvious. Otherwise, taking lifts $\mathbf{u}$, $\mathbf{v}$ of $u$, $v$, the point $v$ is in a slice $\mathbf{w}^{\perp}$ with $\langle\mathbf{u}, \mathbf{w}\rangle \neq 0$ in which case $\mathbf{u}, \mathbf{v}, \mathbf{w}$ are linearly independent. Since $\langle\mathbf{v}, \mathbf{w}\rangle=0$, we can normalize $\mathbf{u}, \mathbf{v}, \mathbf{w}$ to have pairwise real inner products, so they span a copy of $\mathbf{H}_{\mathbb{R}}^{2}$ which contains the real spine of $\mathscr{B}$, i.e. they span a real slice of $\mathscr{B}$.

The following result will also be useful (see also Lemma 2.2 of [DFP05] for a related statement).

Lemma 2.3 Let $\mathscr{B}$ be a bisector and let $C$ be a complex line orthogonal to a complex slice of $\mathscr{B}$. Then $C \cap \mathscr{B}$ is a real geodesic contained in a real slice of $\mathscr{B}$.

Proof. In the unit ball, we may normalize the real spine $\sigma$ of $\mathscr{B}$ to be the set of points of the form $\left(x_{1}, 0\right)$, with $x_{1} \in \mathbb{R}$, the slice of $\mathscr{B}$ to be $\left\{z_{1}=0\right\}$, and $C$ to be of the form $\left\{z_{2}=\beta\right\}$ for some $\beta$ (with $|\beta|<1$ ). Since orthogonal projection onto $\left\{z_{2}=0\right\}$ is just the usual projection onto the first coordinate axis, and a bisector is the preimage of its real spine under orthogonal projection onto its complex spine, $C \cap \mathscr{B}$ is given by $\left(x_{1}, \beta\right)$ with $x_{1} \in \mathbb{R}$ (and $\left|x_{1}\right|<\sqrt{1-|\beta|^{2}}$ ). The latter curve is a geodesic; in fact it is the intersection $C \cap L$ where $L$ is obtained from the real ball $B_{\mathbb{R}}^{2} \subset B_{\mathbb{C}}^{2}$ by applying the isometry $\left(z_{1}, z_{2}\right) \mapsto\left(z_{1}, \frac{\beta}{|\beta|} z_{2}\right)$. \(\square\)

\subsection*{2.5 Coequidistant bisector intersections}

It is well-known that bisector intersections can be somewhat complicated, see the detailed analysis in [Gol99]. In what follows, for simplicity of notation, we restrict ourselves to the case of complex dimension $n=2$.

A simple way to get these intersections to be somewhat reasonable is to restrict to coequidistant pairs, i.e. intersections $\mathscr{B}_{1} \cap \mathscr{B}_{2}$ where $\mathscr{B}_{1}, \mathscr{B}_{2}$ are equidistant from a common point $p_{0} \in \mathbf{H}_{\mathbb{C}}^{n}$. We write $\Sigma_{1}, \Sigma_{2}$ for the complex spines of $\mathscr{B}_{1}, \mathscr{B}_{2}$ respectively, and $\sigma_{1}, \sigma_{2}$ for their real spines.

In view of the discussion in Section 2.3, it should be clear that this is a restrictive condition, which implies that $\Sigma_{1}, \Sigma_{2}$ intersect inside $\mathbf{H}_{\mathbb{C}}^{n}$. Since complex lines with two points in common coincide, there are two possibilities for coequidistant pairs $\mathscr{B}_{1}, \mathscr{B}_{2}$; either the complex spines coincide or they intersect in a single point.

When the complex spines coincide, the bisectors are called cospinal, and the intersection is easily understood; it is non-empty if and only if the real spines $\sigma_{1}$ and $\sigma_{2}$ intersect, and
in that case the intersection $\mathscr{B}_{1} \cap \mathscr{B}_{2}$ consists of a complex line (namely the complex line orthogonal to $\Sigma_{1}=\Sigma_{2}$ through $\sigma_{1} \cap \sigma_{2}$ ).

Now suppose $\Sigma_{1}$ and $\Sigma_{2}$ intersect in a point which lies outside of the real spines $\sigma_{1}$ and $\sigma_{2}$, so that $\mathscr{B}_{1} \cap \mathscr{B}_{2}$ can be written as the equidistant locus from three points $p_{0}, p_{1}, p_{2}$ which are not contained in a common complex line. The following important result is due to G. Giraud [Gir21] (see also Theorem 8.3.3 of [Gol99]).

Proposition 2.4 Let $p_{0}, p_{1}, p_{2}$ be distinct points in $\mathbf{H}_{\mathbb{C}}^{2}$, not all contained in a complex line. When it is non empty, the intersection $\mathscr{B}\left(p_{0}, p_{1}\right) \cap \mathscr{B}\left(p_{0}, p_{2}\right)$ is a (non-totally geodesic) smooth disk. Moreover, it is contained in precisely three bisectors, namely $\mathscr{B}\left(p_{0}, p_{1}\right), \mathscr{B}\left(p_{0}, p_{2}\right)$ and $\mathscr{B}\left(p_{1}, p_{2}\right)$.

Definition 2.5 We define a Giraud disk to be a bisector intersection as in Proposition 2.4 and we denote it by $\mathscr{G}\left(p_{0}, p_{1}, p_{2}\right)$.

Given a Giraud disk $\mathscr{G}=\mathscr{B}_{1} \cap \mathscr{B}_{2} \cap \mathscr{B}_{3}$, the complex slices of the three bisectors $\mathscr{B}_{j}$ intersect $\mathscr{G}$ in hypercycles, so that $\mathscr{G}$ has three pairwise transverse foliations by arcs.
Parametrizing Giraud disks: Let $\mathbf{p}_{j}$ denote a lift of $p_{j}$ to $\mathbb{C}^{3}$. By rescaling the lifts, we may assume that the three square norms $\left\langle\mathbf{p}_{j}, \mathbf{p}_{j}\right\rangle$ are equal, and also that $\left\langle\mathbf{p}_{0}, \mathbf{p}_{1}\right\rangle$ and $\left\langle\mathbf{p}_{0}, \mathbf{p}_{2}\right\rangle$ are real and positive.

Now for $j=1,2$, consider $\tilde{\mathbf{v}}_{j}=\mathbf{p}_{0}-\mathbf{p}_{j}$ and $\tilde{\mathbf{w}}_{j}=i\left(\mathbf{p}_{0}+\mathbf{p}_{j}\right)$ (note that $\tilde{\mathbf{v}}_{j}$ corresponds to the midpoint of the geodesic segment between $p_{0}$ and $p_{j}$ ), and normalize these to unit vectors $\mathbf{v}_{j}=\tilde{\mathbf{v}}_{j} / \sqrt{-\left\langle\tilde{\mathbf{v}}_{j}, \tilde{\mathbf{v}}_{j}\right\rangle}$ and $\mathbf{w}_{j}=\tilde{\mathbf{w}}_{j} / \sqrt{\left\langle\tilde{\mathbf{w}}_{j}, \tilde{\mathbf{w}}_{j}\right\rangle}$.

Here recall that $\mathbf{u} \boxtimes \mathbf{v}$ is the Hermitian cross product of $\mathbf{u}$ and $\mathbf{v}$ associated to the Hermitian form $H$ (see p. 43 of [Gol99]). By definition, $\mathbf{u} \boxtimes \mathbf{v}$ is $\mathbf{0}$ if u and v are collinear, and spans their $H$-orthogonal complement otherwise. In other words, it is the Euclidean cross product of the vectors $\mathbf{u}^{*} H$ and $\mathbf{v}^{*} H$, where $H$ is the matrix defining the Hermitian form (the cross product makes sense because the vector space of homogeneous coordinates has dimension three).

Then the extended real spine of $\mathscr{B}\left(p_{0}, p_{j}\right)$ is given by real linear combinations of $\mathbf{v}_{j}$ and $\mathbf{w}_{j}$, so (lifts of) points in $\mathscr{B}_{1} \cap \mathscr{B}_{2}$ are given by negative vectors of the form
$$V\left(t_{1}, t_{2}\right)=\left(\mathbf{w}_{1}+t_{1} \mathbf{v}_{1}\right) \boxtimes\left(\mathbf{w}_{2}+t_{2} \mathbf{v}_{2}\right),$$
with $t_{1}, t_{2} \in \mathbb{R}$. The only linear combinations we are missing with this parametrization of the extended real spines are $\mathbf{v}_{1}$ and $\mathbf{v}_{2}$, but these are negative vectors so the projectivization of their orthogonal complement does not intersect $\mathbf{H}_{\mathbb{C}}^{2}$. We will call $t_{1}, t_{2}$ spinal coordinates for $\mathscr{G}$.

We will use this parametrization repeatedly; for now, note that, given three points $p_{0}, p_{1}$ and $p_{2}$, it is easy to determine whether the intersection $\mathscr{B}\left(p_{0}, p_{1}\right) \cap \mathscr{B}\left(p_{0}, p_{2}\right)$ is empty or not. Indeed, negative vectors in $\mathbb{C}^{2,1}$ are characterized by the fact that their orthogonal complement is a positive definite complex 2-plane, so the condition that $\left(\mathbf{w}_{1}+t_{1} \mathbf{v}_{1}\right) \boxtimes\left(\mathbf{w}_{2}+t_{2} \mathbf{v}_{2}\right)$ is negative is equivalent to requiring that $g\left(t_{1}, t_{2}\right)>0$ where
$$g\left(t_{1}, t_{2}\right)=\operatorname{det}\left[\begin{array}{ll}
\left\langle\mathbf{w}_{1}+t_{1} \mathbf{v}_{1}, \mathbf{w}_{1}+t_{1} \mathbf{v}_{1}\right\rangle & \left\langle\mathbf{w}_{1}+t_{1} \mathbf{v}_{1}, \mathbf{w}_{2}+t_{2} \mathbf{v}_{2}\right\rangle \\
\left\langle\mathbf{w}_{2}+t_{2} \mathbf{v}_{2}, \mathbf{w}_{1}+t_{1} \mathbf{v}_{1}\right\rangle & \left\langle\mathbf{w}_{2}+t_{2} \mathbf{v}_{2}, \mathbf{w}_{2}+t_{2} \mathbf{v}_{2}\right\rangle
\end{array}\right] .$$

\subsection*{2.6 Cotranchal bisectors}

We will encounter more complicated intersections than coequidistant ones. Two bisectors are called cotranchal if they have a common complex slice; the intersection of cotranchal bisectors is completely understood; see Thm 9.2.7 in [Gol99].

Theorem 2.6 (Goldman) Let $\mathscr{B}_{1}, \mathscr{B}_{2}$ be distinct bisectors, with real spines $\sigma_{1}, \sigma_{2}$. Assume that $\mathscr{B}_{1}$ and $\mathscr{B}_{2}$ share a complex slice $C_{0}$.
\begin{itemize}
\item[(1)] If $\sigma_{1}$ and $\sigma_{2}$ intersect, then $\mathscr{B}_{1} \cap \mathscr{B}_{2}$ is equal to $C_{0}$;
\item[(2)] If $\sigma_{1}$ and $\sigma_{2}$ lie in a common $\mathbb{R}$-plane $L$ and are ultraparallel, then $\mathscr{B}_{1} \cap \mathscr{B}_{2}=C_{0} \cup L$;
\item[(3)] If $\sigma_{1}$ and $\sigma_{2}$ do not lie in a totally geodesic plane, then either $\mathscr{B}_{1} \cap \mathscr{B}_{2}=C_{0}$, or $\mathscr{B}_{1} \cap \mathscr{B}_{2}=C_{0} \cup R$ where $R$ is diffeomorphic to a disk and $R \cap C_{0}$ is a hypercycle.
\end{itemize}

Goldman's proof also gives a way to distinguish between the two very different possibilities that are described in case (3), working with Heisenberg coordinates for the vertices of the bisectors (which are the endpoints in $\partial \mathbf{H}_{\mathbb{C}}^{2}$ of their real spines). We briefly review this in terms of our notation.

Let $C$ be a complex line with polar vector $\mathbf{n}$. Note that this implies $\langle\mathbf{n}, \mathbf{n}\rangle>0$. Let $\mathbf{v}_{1}$ and $\mathbf{v}_{2}$ be two vectors in $\mathbf{n}^{\perp}$ with $\left\langle\mathbf{v}_{j}, \mathbf{v}_{j}\right\rangle<0$. Hence $\mathbf{v}_{j}$ projects to a point $v_{j}$ in $\mathbf{H}_{\mathbb{C}}^{2}$, which of course is in $C$. Consider bisectors $\mathscr{B}_{1}$ and $\mathscr{B}_{2}$ so that the extended real spine of $\mathscr{B}_{j}$ contains n and $\mathbf{v}_{j}$. (Note that we have to be careful when choosing the lift $\mathbf{v}_{j}$ in $\mathbb{C}^{2,1}$ of the corresponding points $v_{j}$ in $C$ since we want the extended spine to be the real span of n and $\mathbf{v}_{j}$; choosing a different lift of $\mathbf{v}_{j}$ rotates $\mathscr{B}_{j}$ around $C$.) We want to decide when the intersection of $\mathscr{B}_{1}$ and $\mathscr{B}_{2}$ is precisely $C$; see [Gol99], [Hsi03].

Proposition 2.7 Let $\mathscr{B}_{1}, \mathscr{B}_{2}$ be cotranchal bisectors with common slice $C$. Let $\mathbf{n}$ be a polar vector for $C$ and let $\mathbf{v}_{1}, \mathbf{v}_{2}$ be negative vectors with $\left\langle\mathbf{v}_{j}, \mathbf{n}\right\rangle=0$ so that the extended real spine of $\mathscr{B}_{j}$ is the real span of $\mathbf{n}$ and $\mathbf{v}_{j}$. Then the intersection of $\mathscr{B}_{1}$ and $\mathscr{B}_{2}$ is precisely $C$ if and only if
$$\left\langle\mathbf{v}_{1}, \mathbf{v}_{1}\right\rangle\left\langle\mathbf{v}_{2}, \mathbf{v}_{2}\right\rangle \geq\left(\Re\left\langle\mathbf{v}_{1}, \mathbf{v}_{2}\right\rangle\right)^{2} .$$

Proof. By assumption $C$ is a slice of $\mathscr{B}_{1}$ and $\mathscr{B}_{2}$. The other slices are parametrized by the polar vectors $t_{j} \mathbf{n}+\mathbf{v}_{j}$ subject to $\left\langle t_{j} \mathbf{n}+\mathbf{v}_{j}, t_{j} \mathbf{n}+\mathbf{v}_{j}\right\rangle>0$. In other words,
$$t_{j}^{2}>\frac{-\left\langle\mathbf{v}_{j}, \mathbf{v}_{j}\right\rangle}{\langle\mathbf{n}, \mathbf{n}\rangle} .$$
Hence we want to find conditions under which the corresponding slices are disjoint, for all $t_{1}$ and $t_{2}$ satisfying this inequality.

Two complex lines $\mathbf{a}^{\perp}$ and $\mathbf{b}^{\perp}$ are disjoint if and only if the restriction of the Hermitian form to the span of a and b is indefinite, so the above condition is equivalent to the following inequality being satisfied for all $t_{1}$ and $t_{2}$ in the range (6):
$$\begin{aligned}
0 \leq & \left|\left\langle t_{1} \mathbf{n}+\mathbf{v}_{1}, t_{2} \mathbf{n}+\mathbf{v}_{2}\right\rangle\right|^{2}-\left\langle t_{1} \mathbf{n}+\mathbf{v}_{1}, t_{1} \mathbf{n}+\mathbf{v}_{1}\right\rangle\left\langle t_{2} \mathbf{n}+\mathbf{v}_{2}, t_{2} \mathbf{n}+\mathbf{v}_{2}\right\rangle \\
= & -t_{1}^{2}\langle\mathbf{n}, \mathbf{n}\rangle\left\langle\mathbf{v}_{2}, \mathbf{v}_{2}\right\rangle+t_{1} t_{2}\langle\mathbf{n}, \mathbf{n}\rangle 2 \Re\left\langle\mathbf{v}_{1}, \mathbf{v}_{2}\right\rangle-t_{2}^{2}\langle\mathbf{n}, \mathbf{n}\rangle\left\langle\mathbf{v}_{1}, \mathbf{v}_{1}\right\rangle \\
& +\left|\left\langle\mathbf{v}_{1}, \mathbf{v}_{2}\right\rangle\right|^{2}-\left\langle\mathbf{v}_{1}, \mathbf{v}_{1}\right\rangle\left\langle\mathbf{v}_{2}, \mathbf{v}_{2}\right\rangle .
\end{aligned}$$

First, note that the constant term is non-negative since
$$1 \leq \cosh ^{2}\left(\frac{d\left(v_{1}, v_{2}\right)}{2}\right)=\frac{\left|\left\langle\mathbf{v}_{1}, \mathbf{v}_{2}\right\rangle\right|^{2}}{\left\langle\mathbf{v}_{1}, \mathbf{v}_{1}\right\rangle\left\langle\mathbf{v}_{2}, \mathbf{v}_{2}\right\rangle} .$$
Therefore, the expression in (7) is always non-negative if and only if its quadratic part is positive semi-definite. (Recall $\langle\mathbf{n}, \mathbf{n}\rangle>0$ and $\left\langle\mathbf{v}_{j}, \mathbf{v}_{j}\right\rangle<0$.) This is equivalent to
$$\left\langle\mathbf{v}_{1}, \mathbf{v}_{1}\right\rangle\left\langle\mathbf{v}_{2}, \mathbf{v}_{2}\right\rangle \geq\left(\Re\left\langle\mathbf{v}_{1}, \mathbf{v}_{2}\right\rangle\right)^{2} .$$
Finally, note that the range (6) is irrelevant in the argument as we may rescale $t_{1}$ and $t_{2}$ without affecting the sign of the quadratic form. \(\square\)

\subsection*{2.7 Computational issues}

As described in the previous sections, bisector intersections can be studied by checking the sign of various functions, sometimes defined in a somewhat complicated compact region.

This will be facilitated by the fact that all geometric objects we introduce are defined over specific number fields. For general computational tools in number fields, see [Coh93]. Throughout this section, we denote by $k$ a number field, and we assume complex hyperbolic space is given as the set of lines in projective space that are negative with respect to a Hermitian inner product defined over $k$.

Definition 2.8 A point $p \in \mathbf{P}_{\mathbb{C}}^{2}$ will be called $k$-rational if it can be represented by a vector in $k^{3}$. A real geodesic will be called $k$-rational if it can be parametrized by vectors of the form $\mathbf{v}+t \mathbf{w}(t \in \mathbb{R})$ with $\mathbf{v}, \mathbf{w} \in k^{3}$. A bisector will be called $k$-rational if its real spine is $k$-rational.

Note that a real geodesic through two $k$-rational points is automatically $k$-rational. Indeed, if $v \neq w$ are two $k$-rational points in $\mathbf{H}_{\mathbb{C}}^{2}$, then they have lifts to $\mathbf{v}, \mathbf{w} \in k^{3}$ such that $\langle\mathbf{v}, \mathbf{w}\rangle$ is real and positive (given any two lifts, multiply $\mathbf{w}$ by $\langle\mathbf{v}, \mathbf{w}\rangle$, which is in $k$ because the Hermitian form is defined over $k$ ). The real geodesic segment from $v$ to $w$ is then parametrized by vectors of the form $\mathbf{v}+t(\mathbf{w}-\mathbf{v}), t \in[0,1]$, where $\mathbf{v}$ and $\mathbf{w}$ are $k$-rational. In these circumstances, we will also say that the geodesic segment $[v, w]$ is $k$-rational.

Note also that a bisector is $k$-rational if and only if it can be written as $\mathscr{B}(p, q)$ for some $k$-rational points $p, q$.

Proposition 2.9 Let $[p, q]$ be a geodesic segment defined by $k$-rational endpoints. Let $\mathscr{B}$ be a $k$-rational bisector. The following statements can be checked by performing arithmetic in $k$ :
\begin{itemize}
\item[-] $p$ is in $\mathscr{B}$ (resp. $p$ is not in $\mathscr{B}$ );
\item[-] $[p, q]$ is contained in $\mathscr{B}$;
\item[-] $[p, q]$ is in a specific component of $\mathbf{H}_{\mathbb{C}}^{2} \backslash \mathscr{B}$.
\item[-] $p$ is in $\mathscr{B}$ and $[p, q]$ is tangent to $\mathscr{B}$.
\end{itemize}

Proof. We parametrize the geodesic segment by vectors $\mathbf{z}_{t}=\mathbf{v}+t(\mathbf{w}-\mathbf{v}), t \in[0,1]$. If $\mathscr{B}=\mathscr{B}\left(q_{0}, q_{1}\right)$ and $\mathbf{q}_{0}, \mathbf{q}_{1} \in k^{3}$ are corresponding lifts, the intersection of the extended real geodesic with (the extension to $\mathbf{P}_{\mathbb{C}}^{2}$ of) $\mathscr{B}$ is described by the following equation,
$$\frac{\left|\left\langle\mathbf{z}_{t}, \mathbf{q}_{0}\right\rangle\right|^{2}}{\left\langle\mathbf{q}_{0}, \mathbf{q}_{0}\right\rangle}=\frac{\left|\left\langle\mathbf{z}_{t}, \mathbf{q}_{1}\right\rangle\right|^{2}}{\left\langle\mathbf{q}_{1}, \mathbf{q}_{1}\right\rangle},$$
which has degree at most two in $t$.
The geodesic is contained in $\mathscr{B}$ if and only if this equation is identically zero; checking whether this holds amounts to checking whether $a=b=c=0$ where
$$\begin{gathered}
a=\left|\left\langle\mathbf{w}-\mathbf{v}, \mathbf{q}_{0}\right\rangle\right|^{2} /\left\langle\mathbf{q}_{0}, \mathbf{q}_{0}\right\rangle-\left|\left\langle\mathbf{w}-\mathbf{v}, \mathbf{q}_{1}\right\rangle\right|^{2} /\left\langle\mathbf{q}_{1}, \mathbf{q}_{1}\right\rangle \\
b=\Re\left(\left\langle\mathbf{v}, \mathbf{q}_{0}\right\rangle\left\langle\mathbf{q}_{0}, \mathbf{w}-\mathbf{v}\right\rangle /\left\langle\mathbf{q}_{0}, \mathbf{q}_{0}\right\rangle-\left\langle\mathbf{v}, \mathbf{q}_{1}\right\rangle\left\langle\mathbf{q}_{1}, \mathbf{w}-\mathbf{v}\right\rangle /\left\langle\mathbf{q}_{1}, \mathbf{q}_{1}\right\rangle\right) \\
c=\left|\left\langle\mathbf{v}, \mathbf{q}_{0}\right\rangle\right|^{2} /\left\langle\mathbf{q}_{0}, \mathbf{q}_{0}\right\rangle-\left|\left\langle\mathbf{v}, \mathbf{q}_{1}\right\rangle\right|^{2} /\left\langle\mathbf{q}_{1}, \mathbf{q}_{1}\right\rangle .
\end{gathered}$$
This can be decided with arithmetic in $k$.
In order to check that the segment is on a specific side of $\mathscr{B}$, we need to check that a strict inequality holds between the two sides of (8). A natural way to do this is to find the solutions of (8), and to check that they are all negative (resp. positive); the latter requires extracting square-roots, which is not quite arithmetic in $k$. Alternatively, one can simply check that there is no sign change between the endpoints, in conjunction with a computation of the value of the polynomial at the point where its derivative vanishes.

Suppose $p \in \mathscr{B}$ and $q \notin \mathscr{B}$. Then the geodesic is tangent to $\mathscr{B}$ if and only if
$$\left.\Re\left\{\left\langle\mathbf{w}, \mathbf{q}_{0}\right\rangle\left\langle\mathbf{q}_{0}, \mathbf{v}\right\rangle\right\} /\left\langle\mathbf{q}_{0}, \mathbf{q}_{0}\right\rangle=\Re\left\{\left\langle\mathbf{w}, \mathbf{q}_{1}\right\rangle\left\langle\mathbf{q}_{1}, \mathbf{v}\right\rangle\right)\right\} /\left\langle\mathbf{q}_{1}, \mathbf{q}_{1}\right\rangle .$$
This condition is checked by arithmetic in $k$, since the vectors $\mathbf{v}, \mathbf{w}, \mathbf{q}_{0}, \mathbf{q}_{1}$ are rational, and the Hermitian form is defined over $k$. \(\square\)

\section*{3 Discrete groups and lattices}

\subsection*{3.1 Lattices and arithmeticity}

A given lattice $\Gamma \subset \operatorname{SU}(n, 1)$ can be conjugated in complicated ways, but it is a classical fact that one can always represent it as a subgroup of some $\operatorname{GL}(N, k)$ where $k$ is a number field (of course one needs to require $n>1$ to exclude lattices in $\operatorname{SU}(1,1) \simeq \operatorname{SL}(2, \mathbb{R})$ ). For a general result along these lines, see Theorem 7.67 in Rag72. The smallest field one can use is given by the field $\mathbb{Q}(\operatorname{tr} \operatorname{Ad} \Gamma)$ generated by traces in the adjoint representation, see Proposition (12.2.1) of DM86 and also Section 6.1.

In this manner, $\Gamma$ determines a $k$-form of $\operatorname{SU}(n, 1)$, and the $k$-forms of $\operatorname{SU}(n, 1)$ are known to be obtained as $\operatorname{SU}(H)$ for some Hermitian form $H$ on $F^{r}$, where $F$ is a division algebra with involution over a quadratic imaginary extension $\mathbb{L}$ of the totally real field $k$ (see [Wei60], [Tit66]). For dimension reasons, $r$ must divide $n+1$; in fact $n+1=r d$, where $d$ is the degree of $F$. In particular, if $n=2$ then $r$ can only be 1 or 3. This gives two types of lattices in $\mathrm{PU}(2,1)$, those related to Hermitian forms over number fields ( $d=1$, hence $r=3)$ and those related to division algebras $(d=3, r=1)$. These are often referred to as arithmetic lattices of the first and second type, respectively.

Note that the groups we construct in the present paper are clearly not arithmetic of the second type, because they contain Fuchsian subgroups. For the relationship between Fuchsian subgroups and groups of the second type, see [Rez95], [Sto12] (and also [McR06]). For lattices preserving a Hermitian form over a number field, there is a fairly simple arithmeticity criterion, which we now state for future reference. The following result is essentially Mostow's Lemma 4.1 of [Mos80] (following Vinberg [Vin68], see also Corollary 12.2.8 of [DM86]). We refer to this statement as the Mostow-Vinberg arithmeticity criterion.

Proposition 3.1 Let $\mathbb{L}$ be a purely imaginary quadratic extension of a totally real field $k$, and $H$ a Hermitian form of signature $(n, 1)$ defined over $\mathbb{L}$. Suppose $\Gamma \subset \operatorname{SU}\left(H ; \mathcal{O}_{\mathbb{L}}\right)$ is a lattice. Then $\Gamma$ is arithmetic if and only if for all $\varphi \in \operatorname{Gal}(\mathbb{L})$ not inducing the identity on $\mathbb{Q}(\operatorname{tr} \operatorname{Ad} \Gamma)$, the form ${ }^{\varphi} H$ is definite.

Note that when $\Gamma$ is as in Proposition 3.1 and it is not arithmetic, the whole group of integral matrices $\operatorname{SU}\left(H ; \mathcal{O}_{\mathbb{L}}\right)$ is non discrete in $\operatorname{SU}(H)$, and in particular $\Gamma$ must have infinite index in $\operatorname{SU}\left(H ; \mathcal{O}_{\mathbb{L}}\right)$.

\subsection*{3.2 The Poincaré polyhedron theorem}

Various versions of the Poincaré polyhedron theorem for complex hyperbolic space have been given (see for example [Mos80], [DFP05], [FP06], [Par06]). For the purpose of the present paper, just as in [Mos80], we need to consider fundamental polyhedra for coset decompositions, where the polyhedron is invariant under a non-trivial subgroup.

Since the hypotheses as well as the conclusions of the theorem require quite a bit of notation, we now give a detailed statement of the Poincaré polyhedron theorem. A detailed proof can be found in [Par]. For simplicity, we only state this theorem for finite-sided polyhedra, as this is sufficient when considering lattices (for a more general statement that applies to locally finite polyhedra, see [Par]).
Polyhedra: For the purpose of the present paper, we only consider finite CW complexes which are regular, in the sense that every attaching map is an embedding. In particular, the closure of each cell is homeomorphic to a closed ball of the appropriate dimension, with embedded boundary sphere. A (finite-sided) polyhedron is the geometric realization in $\overline{\mathbf{H}}_{\mathbb{C}}^{n}$ of such a complex with a single top-dimensional cell of dimension $2 n$.

We will refer to closed cells of a polyhedron as facets, and denote by $\mathscr{F}_{k}(E)$ the set of codimension $k$ facets of $E$. We give special names to facets of each codimension: facets of codimension one, two, three and four will be called sides, ridges, edges and vertices, respectively. Because the focus of the present paper is mainly about lattices, we will assume $E \cap \partial \mathbf{H}_{\mathbb{C}}^{n}$ consists of finitely many vertices, which we call ideal vertices.

Given a facet $f$, we denote by $f^{\circ}$ the relative interior of $f$ (equivalently, $f^{\circ}$ is the set of points that are on $f$ but not in any other facet of the same codimension). It follows from the regularity assumption that for each $k$-cell $f$, the $(k-2)$-cells in $\partial f$ are contained in precisely two $(k-1)$-cells of $\partial f$. In particular, in the above terminology, a ridge of a polyhedron is on precisely two sides.

In the context of complex hyperbolic space, there is no canonical choice of hypersurfaces that can be used to bound polyhedra. Indeed, as mentioned in Section 2, there are no totally geodesic real hypersurfaces in $\mathbf{H}_{\mathbb{C}}^{n}, n \geqslant 2$. In fact the polyhedra that appear in this paper are bounded exclusively by bisectors, and they actually have piecewise smooth boundary
(one can relax this to allow for more general faces, see [Mos80] and [Par] for a specific set of hypotheses).
Side pairings: A map $\sigma: \mathscr{F}_{1}(E) \longrightarrow \operatorname{Isom}\left(\mathbf{H}_{\mathbb{C}}^{n}\right)$ is called a side pairing for $E$ if it satisfies the following conditions:
\begin{itemize}
\item[1.] For each side $s \in \mathscr{F}_{1}(E)$ there is another side $s^{-}$in $\mathscr{F}_{1}(E)$ so that $S=\sigma(s)$ maps $s$ onto $s^{-}$preserving the cell structure. Moreover, $\sigma\left(s^{-}\right)=S^{-1}$. In particular, if $s=s^{-}$ then $S=S^{-1}$ and so $S$ is an involution. We call $S^{2}=i d$ a reflection relation. (In fact $s \neq s^{-}$in all the cases we consider in this paper.)
\item[2.] If $s \in \mathscr{F}_{1}(E)$ and $\sigma(s)=S$ then $S^{-1}(E) \cap E=s$ and $S^{-1}\left(E^{\circ}\right) \cap E^{\circ}=\emptyset$.
\item[3.] If $w \in s^{\circ}$ then there is an open neighborhood $U(w)$ of $w$ contained in $E \cup S^{-1}(E)$.
\end{itemize}
We say that $S=\sigma(s)$ is the side-pairing map associated to the side $s \in \mathscr{F}_{1}(E)$.
We suppose the polyhedron $E$ is preserved by a finite group $\Upsilon<\operatorname{Isom}\left(\mathbf{H}_{\mathbb{C}}^{n}\right)$, which acts by cell-preserving automorphisms. We assume moreover that we have a presentation of $\Upsilon$ in terms of generators and relations (in the examples treated in this paper, $\Upsilon$ will simply be a finite cyclic group).

Let $\Gamma<\operatorname{Isom}\left(\mathbf{H}_{\mathbb{C}}^{n}\right)$ be the group generated by $\Upsilon$ and the side-pairing maps. In what follows, we will need to consider $\Upsilon$-orbits of sides and ridges. We suppose that the side pairing $\sigma$ is compatible with $\Upsilon$ in the following sense: for all $s \in \mathcal{F}_{1}(E)$ and all $P \in \Upsilon$ we have $\sigma(P s)=P \sigma(s) P^{-1}$.
Ridge cycles: Consider a ridge $\rho_{1} \in \mathscr{F}_{2}(E)$. We know that $\rho_{1}$ is contained in exactly two sides of $E$, so we can write $\rho_{1}=s_{1} \cap s^{\prime}$ where $s_{1}, s^{\prime} \in \mathscr{F}_{1}(E)$. Let $S_{1}=\sigma\left(s_{1}\right)$ be the side pairing map associated to $s_{1}$. Then we know that $S_{1}\left(s_{1}\right)$ is another side $s_{1}^{-}$of $E$. Since the side pairing maps are bijections preserving the cell structure, it must be the case that $\rho_{2}=S_{1}\left(\rho_{1}\right)$ is a ridge contained in $s_{1}^{-}$. In other words, there is a side $s_{2} \in \mathscr{F}_{1}(E)$ so that $\rho_{2}=s_{2} \cap s_{1}^{-}$. Let $S_{2}=\sigma\left(s_{2}\right)$ be the side pairing map associated to $s_{2}$. We repeat the above process and thereby obtain a sequence of ridges $\rho_{i}$, sides $s_{i}$ and side pairing maps $S_{i}$ so that $\rho_{i}=s_{i} \cap s_{i-1}^{-}$and $S_{i}=\sigma\left(s_{i}\right)$.

If $\rho_{2}=\rho_{1}$, we set $m=0$; otherwise let $m>0$ be the smallest positive integer such that $\rho_{m+1}$ is in the same $\Upsilon$-orbit as $\rho_{1}$ (there must exist such an $m$, since the set of ridges is finite).

Note that there is then a unique $P \in \Upsilon$ such that $P \rho_{m+1}=\rho_{1}$ (or else there would be a non-trivial element of $\Upsilon$ fixing $\rho_{1}$ pointwise and preserving the pair of sides containing it). We then have $\rho_{1}=s_{1} \cap P s_{m}^{-}$, and the other side $s^{\prime}$ containing $\rho_{1}$ must be $P s_{m}^{-}$.

We say that $\left(\rho_{1}, \ldots, \rho_{m+1}\right)$ is the ridge cycle of $\rho_{1}$ and we define the cycle transformation $T=T\left(\rho_{1}\right)$ of $\rho_{1}$ to be $T=P \circ S_{m} \circ \cdots \circ S_{1}$. Then $T$ maps $\rho_{1}$ to itself:
$$T\left(\rho_{1}\right)=P \circ S_{m} \circ \cdots \circ S_{2} \circ S_{1}\left(\rho_{1}\right)=\cdots=P \circ S_{m}\left(\rho_{m}\right)=P\left(\rho_{m+1}\right)=\rho_{1} .$$
Note that $T$ may not act as the identity on $\rho_{1}$ and, even if it does, then it may not be the identity on the whole of $\mathbf{H}_{\mathbb{C}}^{n}$. We assume that $T$ has finite order $\ell$. The relation $T^{\ell}=i d$ is called the cycle relation associated to $\rho_{1}$.

Note that the sequence $\rho_{1}, \ldots, \rho_{m}$ is entirely determined by $\rho_{1}$ and the choice of the first side $s_{1}$. Observe that if we had started at another ridge in the cycle, say $\rho_{i}$ then, using our hypothesis that the side pairings are compatible with $\Upsilon$, we would obtain the ridge
cycle $\left(\rho_{i}, \rho_{i+1}, \ldots, \rho_{m}, P^{-1} \rho_{1}, P^{-1} \rho_{2}, \ldots, P^{-1} \rho_{i}\right)$. Because $\Upsilon$ is compatible with the side pairings, the cycle transformation of $\rho_{i}$ is
$$\begin{aligned}
T_{i} & =P \circ\left(P^{-1} S_{i-1} P\right) \circ \cdots \circ\left(P^{-1} S_{1} P\right) \circ S_{m} \circ \cdots \circ S_{1} \\
& =S_{i-1} \circ \cdots \circ S_{1} \circ P \circ S_{m} \circ \cdots \circ S_{i} .
\end{aligned}$$
This is just a cyclic permutation of $T$. Likewise, if we had started at $\rho_{1}$ but had chosen the first side pairing to be the one associated to the other side $s^{\prime}$ instead, we would have obtained (up to elements of $\Upsilon$ ) the same sequence of sides in the reverse order, with the side pairing maps inverted. Furthermore, if $Q \in \Upsilon$ then the ridge cycle of $Q \rho_{1}$ is $\left(Q \rho_{1}, \ldots, Q \rho_{m+1}\right)$ and the corresponding cycle transformation is $Q T Q^{-1}$. Hence it suffices to consider the cycle associated to a single ridge in each $\Upsilon$-orbit of ridge cycles.

Writing out $T$ in terms of $P$ and the $S_{i}$, we let $\mathcal{C}=\mathcal{C}\left(\rho_{1}\right)$ be the collection of suffix subwords of $T^{\ell}$, that is
$$\mathcal{C}\left(\rho_{1}\right)=\left\{S_{i} \circ \cdots \circ S_{1} \circ T^{j}: 0 \leqslant i \leqslant m-1,0 \leqslant j \leqslant \ell-1\right\}$$
where $i=0$ means we write none of the $S_{i}$ (this includes the case where $m=0$ ) and so $i=j=0$ corresponds to the identity map.

For $i \in\{1, \ldots, m\}$ we have $\rho_{i}=s_{i} \cap s_{i-1}^{-}$, where $s_{0}^{-}=P s_{m}^{-}$. From the side pairing conditions, $s_{i}=E \cap S_{i}^{-1}(E)$ and $s_{i}^{-}=E \cap S_{i-1}(E)$ and so $\rho_{i} \subset E \cap S_{i}^{-1}(E) \cap S_{i-1}(E)$. Furthermore, for $2 \leqslant i \leqslant m$ we have $\rho_{i}=S_{i-1} \circ \cdots \circ S_{1}\left(\rho_{1}\right)$. Therefore
$$\begin{aligned}
\rho_{1} & =S_{1}^{-1} \circ \cdots \circ S_{i-1}^{-1}\left(\rho_{i}\right) \\
& \subset S_{1}^{-1} \circ \cdots \circ S_{i-1}^{-1}\left(S_{i}^{-1}(E) \cap E \cap S_{i-1}(E)\right) \\
& =\left(S_{1}^{-1} \circ \cdots \circ S_{i}^{-1}(E)\right) \cap\left(S_{1}^{-1} \circ \cdots \circ S_{i-1}^{-1}(E)\right) \cap\left(S_{1}^{-1} \circ \cdots \circ S_{i-2}^{-1}(E)\right) .
\end{aligned}$$
Hence, $\rho_{1}$ is contained in $S_{1}^{-1} \circ \cdots \circ S_{i-1}^{-1}(E)$ for all $i$ between 1 and $m$ where, as before, $i=1$ corresponds to the identity map. Note that, since $P(E)=E$ we have
$$T^{-1}(E)=S_{1}^{-1} \circ \cdots \circ S_{m}^{-1} \circ P^{-1}(E)=S_{1}^{-1} \circ \cdots \circ S_{m}^{-1}(E) .$$
Hence we have shown that
$$\rho_{1} \subset \bigcap_{C \in \mathcal{C}\left(\rho_{1}\right)} C^{-1}(E) .$$
We say that $E$ and $\Gamma$ satisfy the cycle condition at $\rho_{1}$ if this intersection is precisely $\rho_{1}$ and all these copies of $E$ tessellate around $\rho_{1}$. That is:
\begin{itemize}
\item[1.]
$$\rho_{1}=\bigcap_{C \in \mathcal{C}\left(\rho_{1}\right)} C^{-1}(E) .$$
\item[2.] If $C_{1}, C_{2} \in \mathcal{C}\left(\rho_{1}\right)$ with $C_{1} \neq C_{2}$ then $C_{1}^{-1}\left(E^{\circ}\right) \cap C_{2}^{-1}\left(E^{\circ}\right)=\emptyset$.
\item[3.] For all $w \in \rho_{1}^{\circ}$ there exists an open neighborhood $U(w)$ of $w$ so that
$$U(w) \subset \bigcup_{C \in \mathcal{C}\left(\rho_{1}\right)} C^{-1}(E) .$$
\end{itemize}

Consistent system of horoballs: When $E$ has cusps, we need an extra hypothesis, related to metric completeness of the quotient of the polyhedron under the side-pairing maps. Let $\xi_{1}, \ldots \xi_{m}$ be the cusps of $E$. We will assume the existence of a consistent system of horoballs, which is a collection $\left\{U_{1}, \ldots, U_{m}\right\}$, where each $U_{j}$ is a horoball based at $\xi_{j}$ which is preserved by the stabilizer of $\xi_{j}$ in $\Gamma$. By shrinking if necessary, we may suppose that a consistent system is made up of pairwise disjoint horoballs. The existence of a consistent system of horoballs can be checked by verifying that all cycle transformations fixing a given cusp are non-loxodromic (since in that case they automatically preserve every horoball based at that ideal vertex).

Then the statement of the complex hyperbolic Poincaré polyhedron theorem (see [Mos80] or [Par]) is the following.

Theorem 3.2 Suppose $E$ is a smoothly embedded finite-sided polyhedron in $\mathbf{H}_{\mathbb{C}}^{n}$, together with a side pairing $\sigma: \mathscr{F}_{1}(E) \longrightarrow \operatorname{Isom}\left(\mathbf{H}_{\mathbb{C}}^{n}\right)$. Let $\Upsilon<\operatorname{Isom}\left(\mathbf{H}_{\mathbb{C}}^{n}\right)$ be a group of automorphisms of $E$. Let $\Gamma$ be the group generated by $\Upsilon$ and the side-pairing maps. Suppose the cycle condition is satisfied for each ridge in $\mathcal{F}_{2}(E)$, and that there is a consistent system of horoballs at the cusps of $E$ (if it has any).

Then the images of E under the cosets of $\Upsilon$ in $\Gamma$ tessellate $\mathbf{H}_{\mathbb{C}}^{n}$. That is
\begin{itemize}
\item[1.]
$$\bigcup_{A \in \Gamma} A(E)=\mathbf{H}_{\mathbb{C}}^{n} .$$
\item[2.] If $A \in \Gamma-\Upsilon$ then $E^{\circ} \cap A\left(E^{\circ}\right)=\emptyset$.
\end{itemize}
Moreover, $\Gamma$ is discrete and a fundamental domain for its action on $\mathbf{H}_{\mathbb{C}}^{n}$ is obtained by intersecting $E$ with a fundamental domain for $\Upsilon$.

Finally, one obtains a presentation for $\Gamma$ in terms of the generators given by the side pairing maps together with a generating set for $\Upsilon$; the relations are given by the reflection relations, the cycle relations and the relations in a presentation for $\Upsilon$.

Finite volume: Note that the statement of the Poincaré polyhedron theorem says nothing about the volume of the quotient $\Gamma \backslash \mathbf{H}_{\mathbb{C}}^{n}$, which is also the volume of $E$. This volume is of course finite when $E$ is entirely contained in $\mathbf{H}_{\mathbb{C}}^{n}$, in which case $\Gamma$ is a cocompact lattice in $\operatorname{PU}(n, 1)$.

Some of the groups we study in this paper are not cocompact (namely, when $p=4,6$ ). In that case, $E$ has some ideal vertices, but one easily sees that the volume of $E$ is finite by studying the structure of the stabilizer of the ideal vertices. Let $x$ be an ideal vertex with stabilizer $\Gamma_{x}$. By the existence of a consistent system of horoballs, the ideal point corresponding to $x$ in the quotient $\Gamma \backslash \mathbf{H}_{\mathbb{C}}^{n}$ has a neighborhood diffeomorphic to $(0,+\infty) \times H_{x}$, where $H_{x}$ is the quotient of any horosphere based at $x$ by the action of $\Gamma_{x}$. It is well known that the fact that $\Gamma_{x}$ acts cocompactly on $\partial \mathbf{H}_{\mathbb{C}}^{2} \backslash\{x\}$ (or equivalently, on horospheres based at $x$ ) implies that cusp neighborhoods in the quotient have finite volume (see for example Lemma 5.2 in [HP96]). This is clear for our polyhedra, whose cusp cross-sections are compact (see Section 5.3, Figure 17 for their explicit description).
Toy model: To illustrate this theorem and to help understand our family of examples, it is instructive to work through a toy example with $n=1$. Consider a triangle in the Poincaré disk $\mathbf{H}_{\mathbb{C}}^{1}$ with vertices $q_{R}$ with angle $\pi / 2, q_{J}$ with angle $\pi / 3$ and $q_{P}$ with angle $\pi / 7$ (see Figure 1).

Let $R, J$ and $P$ be elements of $\operatorname{Isom}\left(\mathbf{H}_{\mathbb{C}}^{1}\right)$, with orders 2, 3 and 7, fixing the respective points and satisfying $P=R J$. Let $\Gamma$ be the group generated by $R, J$ and $P$. The usual fundamental domain $D$ for this group consists of this triangle together with its image under reflection in the side joining $q_{P}$ and $q_{R}$. There is a natural $P$-invariant hyperbolic heptagon $E$, obtained as the union of the seven images of $D$ under powers of $P$. This heptagon is a fundamental domain for the cosets of $\Upsilon=\langle P\rangle$ in $\Gamma$.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/31f0f35c-0604-47ef-a2ef-a49ed021037c-18.jpg?height=671&width=755&top_left_y=696&top_left_x=669}
\captionsetup{labelformat=empty}
\caption{Figure 1: Toy model for fundamental domains for coset decompositions.}
\end{figure}

The vertices of the heptagon $E$ are of the form $P^{k} q_{J}$, where $k=0, \ldots, 6$, and the midpoints of its sides are given by the points $P^{k} q_{R}$. Now let $r$ be the edge from $q_{J}$ to $q_{R}$ and let $r^{-}$be the edge from $q_{R}$ to $P q_{J}=R q_{J}$. Then we define the side pairing map $R: r \longrightarrow r^{-}$, and extend this to the other sides in a way that is compatible with $\Upsilon$. Namely, we have side pairings $P^{k} R P^{-k}: P^{k} r \longrightarrow P^{k} r^{-}$. We obtain two vertex cycles, which we write in terms of the edges and the vertices.

\begin{tabular}[t]{|l|l|l|}
\hline $R$ & $r \cap r^{-}$ & $q_{R}$ \\
\hline & $r \cap r^{-}$ & $q_{R}$ \\
\hline $R$ & $r \cap P^{-1} r^{-}$ & $q_{J}$ \\
\hline $P^{-1}$ & $P r \cap r^{-}$ & $R q_{J}$ \\
\hline & $r \cap P^{-1} r^{-}$ & $q_{J}$ \\
\hline
\end{tabular}
It is easy to check local tessellation around the vertices and so Poincaré's theorem shows that the heptagons tile the Poincaré disk.

For $r \cap r^{-}$, the cycle transformation is $R$, and the cycle relation is $R^{2}=i d$. For $r \cap$ $P^{-1} r^{-}$, the cycle transformation is $P^{-1} R$ and the cycle relation is $\left(P^{-1} R\right)^{3}=i d$. Adding the generator $P$ of $\Upsilon$ and its relation $P^{7}=i d$ gives the well known presentation
$$\Gamma=\left\langle R, P \mid R^{2}=\left(P^{-1} R\right)^{3}=P^{7}=i d\right\rangle .$$
Note that a fundamental domain for $\Gamma$ is obtained by intersecting $E$ with a fundamental domain for $\Upsilon$ (one example of such a fundamental domain is of course given simply by $D$ ).