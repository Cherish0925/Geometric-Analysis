---
retention_scope: session
part: 1
total_parts: 4
---

[Part 1/4 of: Monodromy of certain Painlevé–VI transcendents and reflection groups]

---
source_file: math_9806056.pdf
converter: mathpix
format: mmd
---

\title{
MONODROMY OF CERTAIN PAINLEVE'-VI TRANSCENDENTS AND REFLECTION GROUPS
}

\author{
B. Dubrovin and M. Mazzocco \\ International School of Advanced Studies, SISSA-ISAS, Trieste.
}

\begin{abstract}
We study the global analytic properties of the solutions of a particular family of Painlevé VI equations with the parameters $\beta=\gamma=0, \delta=\frac{1}{2}$ and $\alpha$ arbitrary. We introduce a class of solutions having critical behaviour of algebraic type, and completely compute the structure of the analytic continuation of these solutions in terms of an auxiliary reflection group in the three dimensional space. The analytic continuation is given in terms of an action of the braid group on the triples of generators of the reflection group. This result is used to classify all the algebraic solutions of our Painlevé VI equation.
\end{abstract}

SISSA preprint no. 149/97/FM, 28 November 1997, revised 8 June 1998.

\section*{INTRODUCTION}

In this paper, we will study the structure of the analytic continuation of the solutions of the following differential equation
$$\begin{aligned}
y_{x x}= & \frac{1}{2}\left(\frac{1}{y}+\frac{1}{y-1}+\frac{1}{y-x}\right) y_{x}^{2}-\left(\frac{1}{x}+\frac{1}{x-1}+\frac{1}{y-x}\right) y_{x} \\
& +\frac{1}{2} \frac{y(y-1)(y-x)}{x^{2}(x-1)^{2}}\left[(2 \mu-1)^{2}+\frac{x(x-1)}{(y-x)^{2}}\right],
\end{aligned}$$
PVIμ
in the complex plane, $\mu$ is an arbitrary complex parameter satisfying the condition $2 \mu \notin \mathbb{Z}$.
This is a particular case of the general Painlevé VI equation (see [Ince]) PVI $(\alpha, \beta, \gamma, \delta)$, that depends on four parameters $\alpha, \beta, \gamma, \delta$, specified by the following choice of the parameters:
$$\alpha=\frac{(2 \mu-1)^{2}}{2}, \quad \beta=\gamma=0 \quad \delta=\frac{1}{2} .$$
The general solution $y\left(x ; c_{1}, c_{2}\right)$ of $\operatorname{PVI}(\alpha, \beta, \gamma, \delta)$ satisfies the following two important properties (see [Pain]):
\begin{itemize}
\item[1)] The solution $y\left(x ; c_{1}, c_{2}\right)$ can be analytically continued to a meromorphic function on the universal covering of $\overline{\mathbb{C}} \backslash\{0,1, \infty\}$.
\item[2)] For generic values of the integration constants $c_{1}, c_{2}$ and of the parameters $\alpha, \beta, \gamma, \delta$, the solution $y\left(x ; c_{1}, c_{2}\right)$ can not be expressed via elementary or classical transcendental functions.
\end{itemize}

The former claim is the so-called Painlevé property of the equation $\operatorname{PVI}(\alpha, \beta, \gamma, \delta)$, i.e. its solutions $y\left(x ; c_{1}, c_{2}\right)$ may have complicated singularities only at the critical points of the equation, $0,1, \infty$, the position of which does not depend on the choice of the particular solution (the so-called fixed singularities), and all the other singularities of the solution are poles. Positions of the poles depend on the integration constants (the so-called movable singularities).

All the second order ordinary differential equations of the type:
$$y_{x x}=\mathcal{R}\left(x, y, y_{x}\right),$$
where $\mathcal{R}$ is rational in $y_{x}$ and meromorphic in $x$ and $y$ and satisfies the Painlevé property of absence of movable critical singularities, were classified by Painlevé and Gambier (see [Pain], and [Gamb]). Only six of these equations, which are given in the Painlevé-Gambier list, satisfy the property 2), i.e. they can not be reduced to known differential equations for elementary and classical special functions. The solutions of these equations define some new functions, the so-called Painlevé transcendents. $\operatorname{PVI}(\alpha, \beta, \gamma, \delta)$ is the most general equation of Painlevé-Gambier list. Indeed all the others can be obtained from $\mathrm{PVI}(\alpha, \beta, \gamma, \delta)$ by a confluence procedure (see [Ince] §14.4).

There are many physical applications of particular solutions of the Painlevé equations which we do not discuss here. We mention only the paper [Tod] where our $\mathrm{PVI} \mu$ appears in the problem of the construction of self-dual Bianchi-type IX Einstein metrics, and the
paper [Dub] where the same equation was used to classify the solutions of WDVV equation in $2 D$-topological field theories.

The name of transcendents could be misleading; indeed, for some particular values of $\left(c_{1}, c_{2}, \alpha, \beta, \gamma, \delta\right)$, the solution $y\left(x ; c_{1}, c_{2}\right)$ can be expressed via classical functions. For example Picard (see [Pic] and [Ok]) showed that the general solution of $\operatorname{PVI}\left(0,0,0, \frac{1}{2}\right)$ can be expressed via elliptic functions, and, more recently, Hitchin [Hit] obtained the general solution of $\operatorname{PVI}\left(\frac{1}{8}, \frac{1}{8}, \frac{1}{8}, \frac{3}{8}\right)$ in terms of the Jacobi theta-functions (see also [Man]). Particular examples of classical solutions, that can be expressed via hypergeometric functions, of PVI were first constructed by Lukashevich [Luka]. A general approach to study the classical solutions of PVI was proposed by Okamoto (see [Ok1][Ok2]). One of the main tools of this approach is the symmetry group of PVI: the particular solutions are those being invariant with respect to some symmetry of PVI. The symmetries act in a non trivial way on the space of the parameters $(\alpha, \beta, \gamma, \delta)$. Okamoto described the fundamental region of the action of this symmetry group and showed that all the classical solutions known at that moment, fit into the boundary of this fundamental region.

The theory of the classical solutions of the Painlevé equations was developed by Umemura and Watanabe ([Um], [Um1], [Um2], [Um3], [Wat]); in particular, all the oneparameter families of classical solutions of PVI were classified in [Wat]. Watanabe also proved that, loosely speaking, all the other classical solutions of PVI (i.e. not belonging to the one-parameter families) can only be given by algebraic functions.

Examples of algebraic solutions were found in [Hit1], for $\operatorname{PVI}\left(\frac{1}{8},-\frac{1}{8}, \frac{1}{2 k^{2}}, \frac{1}{2}-\frac{1}{2 k^{2}}\right)$, for an arbitrary integer $k$. Other examples for $\mathrm{PVI} \mu$ were constructed in [Dub]. They turn out to be related to the group of symmetries of the regular polyhedra in the three dimensional space. Other algebraic solutions of PVI can be extracted from the recent paper [Seg].

The main aim of our work is to elaborate a tool to classify all the algebraic solutions of the Painlevé VI equation (for the other five Painlevé equations, algebraic solutions have been classified, see [Kit], [Wat1], [Mur] and [Mur1]). Our idea is very close to the main idea of the classical paper of Schwartz (see [Schw]) devoted to the classification of the algebraic solutions of the Gauss hypergeometric equation. Let $y\left(x ; c_{1}, c_{2}\right)$ be a branch of a solution of PVI; its analytic continuation along any closed path $\gamma$ avoiding the singularities is a new branch $y\left(x ; c_{1}^{\gamma}, c_{2}^{\gamma}\right)$ with new integration constants $c_{1}^{\gamma}, c_{2}^{\gamma}$. Since all the singularities of the solution on $\overline{\mathbb{C}} \backslash\{0,1, \infty\}$ are poles, the result of the analytic continuation depends only on the homotopy class of the loop $\gamma$ on the Riemann sphere with three punctures. As a consequence, the structure of the analytic continuation is described by an action of the fundamental group:
$$\gamma \in \overline{\mathbb{C}} \backslash\{0,1, \infty\}, \quad \gamma:\left(c_{1}, c_{2}\right) \rightarrow\left(c_{1}^{\gamma}, c_{2}^{\gamma}\right) .$$
To classify all the algebraic solutions of Painlevé VI, all the finite orbits of this action must be classified.

Our problem differs from Schwartz's linear analogue, because (0.1) is not a linear representation but a non-linear action of the fundamental group. It is also more involved than the problem of the classification of the algebraic solutions of the other five Painlevé equations, because the PVI is the only equation on the Painlevé-Gambier list having a non-abelian fundamental group of the complement of the critical locus.

Although the main idea seems to work for the general $\operatorname{PVI}(\alpha, \beta, \gamma, \delta)$, we managed
to completely describe the action (0.1), and to solve the problem of the classification of the algebraic solutions, only for the particular one-parameter family $\mathrm{PVI} \mu$. Nevertheless, we have decided to publish these results separately, postponing the investigation of the general case to another paper (in an effort to keep the paper within a reasonable size, we also postpone the study of the resonant case $2 \mu \in \mathbb{Z}$, see [Ma]). One of the motivations for the present publication is a nice geometrical interpretation of the structure of the analytic continuation (0.1), that seems to disappear in the general PVI equation.

We now outline the main results and describe the structure of the paper. Let us introduce a class of solutions of $\mathrm{PVI} \mu$ a-priori containing all the algebraic solutions. We say that a branch of a solution $y\left(x ; c_{1}, c_{2}\right)$ has critical behaviour of algebraic type, if there exist three real numbers $l_{0}, l_{1}, l_{\infty}$ and three non-zero complex numbers $a_{0}, a_{1}, a_{\infty}$, such that
$$y(x)=\left\{\begin{array}{rc}
a_{0} x^{l_{0}}\left(1+\mathcal{O}\left(x^{\varepsilon}\right)\right), & \text { as } \quad x \rightarrow 0, \\
1-a_{1}(1-x)^{l_{1}}\left(1+\mathcal{O}\left((1-x)^{\varepsilon}\right)\right), & \text { as } \quad x \rightarrow 1, \\
a_{\infty} x^{1-l_{\infty}}\left(1+\mathcal{O}\left(x^{-\varepsilon}\right)\right), & \text { as } \quad x \rightarrow \infty,
\end{array}\right.$$
where $\varepsilon>0$ is small enough. We show that there exists a three-parameter family of solutions of $\mathrm{PVI} \mu$ with critical behaviour of algebraic type, where $\mu$ itself is a function of $l_{0}, l_{1}, l_{\infty}$. Of course, for an algebraic solution, the indices $l_{0}, l_{1}, l_{\infty}$ must be rational.

It turns out that the three-parameter family of solutions (0.2) is closed under the analytic continuation (0.1), if and only if $\mu$ is real. One of our main results is the parameterization of the solutions (0.2) by ordered triples of planes in the three dimensional Euclidean space(see Section 1.4). In particular, the indices $l_{0}, l_{1}, l_{\infty}$ are related to the angles $\pi r_{0}, \pi r_{1}, \pi r_{\infty}$ between the planes:
$$l_{i}=\left\{\begin{array}{rl}
2 r_{i} & \text { if } \\
2-2 r_{i} & \text { if } \\
2-2 \leq r_{i} \leq \frac{1}{2}
\end{array} \quad i=0,1, \infty,\right.$$
and the parameter $\mu$ is determined within the ambiguity $\mu \mapsto \pm \mu+n, n \in \mathbb{Z}$, by the equation:
$$\sin ^{2} \pi \mu=\cos ^{2} \pi r_{0}+\cos ^{2} \pi r_{1}+\cos ^{2} \pi r_{\infty}+2 \cos \pi r_{0} \cos \pi r_{1} \cos \pi r_{\infty} .$$
This ambiguity and the one due to the reordering of the planes can be absorbed by the symmetries of $\mathrm{PVI} \mu$ described in Section 1.2.

We compute the analytic continuation (0.1) in terms of some elementary operations on the planes. This computation leads to prove that, for an algebraic solution of $\mathrm{PVI} \mu$, the reflections in the planes must generate the symmetry group of a regular polyhedron in $\mathbb{R}^{3}$. Another result of this paper is the classification of all algebraic solutions of $\mathrm{PVI} \mu$. They are in one-to-one correspondence, modulo the symmetries of the equations described in Section 1.2, with the reciprocal pairs of the three-dimensional regular polyhedra and star-polyhedra (the description of the star-polyhedra can be found in [Cox]). The solutions corresponding to the regular tetrahedron, cube and icosahedron are the ones obtained in
[Dub] using the theory of polynomial Frobenius manifolds. The solutions corresponding to the regular great icosahedron, and regular great dodecahedron are new. Our method not only allows to classify the solutions, but also to obtain the explicit formulae, as we do in Section 2.4.

The main tool to obtain these results is the isomonodromy deformation method (see [Fuchs], [Sch] and [JMU], [ItN], [FlN]). The Painlevé VI is represented as the equation of isomonodromy deformation of the auxiliary Fuchsian system
$$\frac{\mathrm{d} Y}{\mathrm{~d} z}=\left(\frac{A_{0}}{z}+\frac{A_{1}}{z-1}+\frac{A_{x}}{z-x}\right) Y .$$
For PVI $\mu$, the 2 × 2 matrices $A_{0}, A_{1}, A_{x}$ are nilpotent and
$$A_{0}+A_{1}+A_{x}=\left(\begin{array}{cc}
-\mu & 0 \\
0 & \mu
\end{array}\right) .$$
The entries of the matrices $A_{i}$ are complicated expressions of $x, y, y_{x}$ and of some quadrature $\int R(x, y) \mathrm{d} x$. The monodromy of (0.3) remains constant if and only if $y=y(x)$ satisfies PVI. Thus, the solutions of $\mathrm{PVI} \mu$ are parameterized by the monodromy data of the Fuchsian system (0.3) (see Section 1.1). In section 1.2, we compute the structure of the analytic continuation in terms of the monodromy data. On this basis, in Section 1.3, we classify all the monodromy data of the algebraic solutions of $\mathrm{PVI} \mu$. To this end, we classify all the rational solutions of certain trigonometric equations using the method of a paper by Gordan (see [Gor]). In Section 1.4, we parameterize the monodromy data of $\mathrm{PVI} \mu$ by ordered triples of planes in the three-dimensional space, considered modulo rotations. The structure of the analytic continuation of the solutions of $\mathrm{PVI} \mu$ is reformulated in terms of a certain action of the braid group $B_{3}$ on the triples of planes. The group $G$ generated by the reflections with respect to the planes remains unchanged. For the algebraic solutions, the group $G$ turns out to coincide with the symmetry group of one of the regular polyhedra in the three-dimensional Euclidean space. We also give another proof, suggested by E. Vinberg, of this result, and we establish that the class of solutions of $\mathrm{PVI} \mu$ parameterized by triples of planes in the three dimensional Euclidean space is invariant with respect to the analytic continuation.

In the second part of the paper, we identify this class of solutions of $\mathrm{PVI} \mu$ with the class of solutions having critical behaviour of algebraic type (0.2). In Section 2.1, we prove that the solution $y(x)$ of the form (0.2), for a fixed value of $\mu$, is uniquely determined by its asymptotic behaviour near one of the critical points, i.e. by any of the pairs $\left(a_{0}, l_{0}\right)$, $\left(a_{1}, l_{1}\right),\left(a_{\infty}, l_{\infty}\right)$. In particular, we prove that, for an algebraic solution of $\mathrm{PVI} \mu$, the indices $l_{0}, l_{1}, l_{\infty}$ must satisfy:
$$0<l_{i} \leq 1, \quad i=0,1, \infty .$$
To derive the connection formulae establishing the relations between these pairs, we use (see Section 2.3) the properly adapted method of Jimbo (see [Jim]). This method allows to express the monodromy data of the auxiliary Fuchsian system (0.3) in terms of the parameters $\left(a_{0}, l_{0}\right),\left(a_{1}, l_{1}\right)$ or $\left(a_{\infty}, l_{\infty}\right)$. For convenience of the reader, and because of some differences between the assumptions of Jimbo's work and ours, we give a complete
derivation of the connection formulae in Section 2.2. Using the results of the Sections 1.3 and 1.4, we complete the computation of the critical behaviour (0.2) for all the branches of the analytic continuation of the solution. The result of this computation is used in Section 2.4 to obtain the explicit formulae for the algebraic solutions of $\mathrm{PVI} \mu$.

Remark 0.1. The resulting classification of the algebraic solutions of $\mathrm{PVI} \mu$ is in striking similarity to the Schwartz's classification (see [Schw]) of the algebraic solutions of the hypergeometric equation. According to Schwartz, the algebraic solutions of the hypergeometric equation, considered modulo contiguity transformations, are of fifteen types (the first type consists of an infinite sequence of solutions). The rows (2-15) of Schwartz's list (see, for example, the table in Section 2.7.2 of [Bat]) correspond to the triples of generating reflections of the symmetry groups of regular polyhedra in the three-dimensional Euclidean space (we are grateful to E. Vinberg for bringing this point to our attention). The parameter $\lambda, \mu, \nu$ of the hypergeometric equation shown in the table are just the angles between the mirrors of the reflections, divided by $\pi$.

According to our classification, the algebraic solutions of $\mathrm{PVI} \mu$, considered modulo symmetries, are in one-to-one correspondence to the classes of equivalence of the triples of generating reflections in the symmetry groups of regular polyhedra. The equivalence is defined by an action of the braid group $B_{3}$ on the triples and by orthogonal transformations. We find that in the groups $G=W\left(A_{3}\right)$ and $G=W\left(B_{3}\right)$, the symmetry groups of respectively the regular tetrahedron and of the cube or regular octahedron, there is only one equivalence class of triples of generating reflections; these are given respectively by the rows $(2,3)$ and by $(4,5)$ of Schwartz's table. In the group $W\left(H_{3}\right)$ of symmetries of regular icosahedron or regular dodecahedron, there are three equivalence classes of triples of reflections which are given respectively by the rows (6, 8, 13), (11, 14, 15) and (7, 9, 10, 12) of the Schwartz's table and correspond to icosahedron, great icosahedron and great dodecahedron (or to their reciprocal pairs, see [Cox]). To establish the correspondence, we associate a standard system of generating reflections to a regular polyhedron in the following way: let $H$ be the center of the polyhedron, $O$ the center of a face, $P$ a vertex of this face and $Q$ the center of an edge of the same face through the vertex $P$. Then the reflections with respect to the planes $H O P, H O Q$ and $H P Q$ are the standard system of generators. Our five algebraic solutions correspond to the classes of equivalence of the standard systems of generators obtained by this contruction applied to tetrahedron, cube, icosahedron, great icosahedron, great dodecahedron.

Summarizing, we see that the list of all the algebraic solutions of $\mathrm{PVI} \mu$ is obtained by folding of the list of Schwartz modulo the action of the braid group. This relation between the algebraic solutions of $\mathrm{PVI} \mu$ and the algebraic hypergeometric functions seems to be surprising also from the point of view of the results of Watanabe (see [Wat]) who classified all the one-parameter families of classical solutions of $\mathrm{PVI} \mu$ (essentially, all of them are given by hypergeometric functions). Using these results, one can easily check that our algebraic solutions do not belong to any of the one-parameter families of classical solutions of $\mathrm{PVI} \mu$.

Acknowledgments
The authors are indebted to E. Vinberg for the elegant proof of theorem 1.8. We thank A. Akhmedov for a simple proof of the Algebraic Lemma, Section 1.4. We thank also R. Conte for drawing our attention to the classical work of Picard (see [Pic]) and V. Sokolov and F. Zanolin for useful discussions.

\section*{1. STRUCTURE OF ANALYTIC CONTINUATION AND ALGEBRAIC SOLUTIONS OF $\mathbf{P V I} \boldsymbol{\mu}$}
1.1. Painlevé VI equation as isomonodromy deformation equation.

In this section we show how the $\mathrm{PVI} \mu$ equation can be reduced to the isomonodromy deformation equation of an auxiliary Fuchsian system (see [Sch], [JMU]); moreover we describe the parameterization, essentially due to Schlesinger (see. [Sch]), of the solutions of the $\mathrm{PVI} \mu$ equation by the monodromy data of such Fuchsian system.
1.1.1. An auxiliary Fuchsian system and its monodromy data. In this subsection, we introduce an auxiliary Fuchsian system, define its monodromy and connection matrices, and extabilish the correspondence between monodromy matrices and coefficients of the Fuchsian system for a given set of poles.

Let us consider the following Fuchsian system with four regular singularities at $u_{1}$, $u_{2}, u_{3}$ and $\infty$ :
$$\frac{\mathrm{d}}{\mathrm{~d} z} Y=\mathcal{A}(z) Y, \quad z \in \overline{\mathbb{C}} \backslash\left\{u_{1}, u_{2}, u_{3}, \infty\right\}$$
where $\mathcal{A}(z)$ is a matrix-valued function:
$$\mathcal{A}(z)=\frac{\mathcal{A}_{1}}{z-u_{1}}+\frac{\mathcal{A}_{2}}{z-u_{2}}+\frac{\mathcal{A}_{3}}{z-u_{3}},$$
$\mathcal{A}_{i}$ being 2 × 2 matrices independent on $z$, and $u_{1}, u_{2}, u_{3}$ being pairwise distinct complex numbers. We assume that the matrices $\mathcal{A}_{i}$ satisfy the following conditions:
$$\mathcal{A}_{i}^{2}=0 \quad \text { and } \quad \mathcal{A}_{\infty}:=-\mathcal{A}_{1}-\mathcal{A}_{2}-\mathcal{A}_{3}=\left(\begin{array}{cc}
\mu & 0 \\
0 & -\mu
\end{array}\right) .$$
Indeed, we will see in the latter part of this section that this choice corresponds to the particular case $\mathrm{PVI} \mu$ of the Painlevé VI equation. In this paper we consider the non-resonant case $2 \mu \notin \mathbb{Z}$.

The solution $Y(z)$ of the system (1.1) is a multi-valued analytic function in the punctured Riemann sphere $\mathbb{C} \backslash\left\{u_{1}, u_{2}, u_{3}\right\}$ and its multivaluedness is described by the so-called monodromy matrices.

Let us briefly recall the definition of the monodromy matrices of the Fuchsian system (1.1). First, we fix a basis $\gamma_{1}, \gamma_{2}, \gamma_{3}$ of loops in the fundamental group, with base point at $\infty$, of the punctured Riemann sphere
$$\pi_{1}\left(\overline{\mathbb{C}} \backslash\left\{u_{1}, u_{2}, u_{3}, \infty\right\}, \hat{x}\right),$$
and a fundamental matrix for the system (1.1). To fix the basis of the loops, we first perform some cuts between the singularities, namely we cut three parallel segments $\pi_{i}$ between the point at infinity and each $u_{i}$; the segments $\pi_{i}$ are ordered according to the order of the points $u_{1}, u_{2}, u_{3}$, as in the figure 1. Take $\gamma_{i}$ to be a simple closed curve starting and finishing at infinity, going around $u_{i}$ in positive direction ( $\gamma_{i}$ is oriented counter-clockwise, $u_{i}$ lies inside, while the other singular points lie outside) and not crossing the cuts $\pi_{i}$. Near $\infty$, we take every loop $\gamma_{i}$ close to the cut $\pi_{i}$ as in the figure 1.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/64ce0006-7367-4aae-9e25-7b8a1be4f808-08.jpg?height=485&width=785&top_left_y=916&top_left_x=732}
\captionsetup{labelformat=empty}
\caption{Fig.1. The cuts $\pi_{i}$ between the singularities $u_{i}$ and the oriented loops $\gamma_{i}$.}
\end{figure}
Now, we fix the fundamental matrix $Y_{\infty}(z)$ of the system (1.1) in such a way that
$$Y_{\infty}(z)=\left(\mathbf{1}+\mathcal{O}\left(\frac{1}{z}\right)\right)\left(\begin{array}{cc}
z^{-\mu} & 0 \\
0 & z^{\mu}
\end{array}\right), \quad \text { as } \quad z \rightarrow \infty,$$
where $z^{\mu}:=e^{\mu \log z}$, with the choice of the principal branch of the logarithm, with the branch-cut along the common direction of the cuts $\pi_{1}, \pi_{2}, \pi_{3}$. Such a fundamental matrix $Y_{\infty}(z)$ exists and, due to the non-resonance condition, it is uniquely determined. It can be analytically continued to an analytic function on the universal covering of $\overline{\mathbb{C}} \backslash\left\{u_{1}, u_{2}, u_{3}, \infty\right\}$. For any element $\gamma \in \pi_{1}\left(\overline{\mathbb{C}} \backslash\left\{u_{1}, u_{2}, u_{3}, \infty\right\}, \infty\right)$ we denote the result of the analytic continuation of $Y_{\infty}(z)$ along the loop $\gamma$ by $\gamma\left[Y_{\infty}(z)\right]$. Since $\gamma\left[Y_{\infty}(z)\right]$ and $Y_{\infty}(z)$ are two fundamental matrices in the neighborhood of infinity, they must be related by the following relation:
$$\gamma\left[Y_{\infty}(z)\right]=Y_{\infty}(z) M_{\gamma}$$
for some constant invertible $2 \times 2$ matrix $M_{\gamma}$ depending only on the homotopy class of $\gamma$. Particularly, the matrix $M_{\infty}:=M_{\gamma_{\infty}}, \gamma_{\infty}$ being a simple loop around infinity in the clock-wise direction, is given by:
$$M_{\infty}=\left(\begin{array}{cc}
\exp (2 i \pi \mu) & 0 \\
0 & \exp (-2 i \pi \mu)
\end{array}\right) .$$

The resulting monodromy representation is an anti-homomorphism:
$$\begin{array}{rlc}
\pi_{1}\left(\overline{\mathbb{C}} \backslash\left\{u_{1}, u_{2}, u_{3}, \infty\right\}, \infty\right) & \rightarrow & S L_{2}(\mathbb{C}) \\
& \mapsto & M_{\gamma} \\
& & \\
M_{\gamma \tilde{\gamma}}=M_{\tilde{\gamma}} M_{\gamma} . & &
\end{array}$$
The images $M_{i}:=M_{\gamma_{i}}$ of the generators $\gamma_{i}, i=1,2,3$ of the fundamental group, are called the monodromy matrices of the Fuchsian system (1.1). They generate the monodromy group of the system, i.e. the image of the representation (1.5). Moreover, due to the fact that, in our particular case, the $\mathcal{A}_{i}$ are nilpotent, satisfy the following relations:
$$\operatorname{det}\left(M_{i}\right)=1, \quad \operatorname{Tr}\left(M_{i}\right)=2, \quad \text { for } \quad i=1,2,3,$$
with $M_{i}=\mathbf{1}$ if and only if $\mathcal{A}_{i}=0$. Moreover, since the loop $\left(\gamma_{1} \gamma_{2} \gamma_{3}\right)^{-1}$ is homotopic to $\gamma_{\infty}$, the following relation holds:
$$M_{\infty} M_{3} M_{2} M_{1}=\mathbf{1} .$$
A simultaneous conjugation $\mathcal{A}_{i} \mapsto D^{-1} \mathcal{A}_{i} D, i=1,2,3$ of the coefficients $\mathcal{A}_{i}$ of the Fuchsian system (1.1) by a diagonal matrix $D$, implies the same conjugation of the monodromy matrices $M_{\gamma} \mapsto D^{-1} M_{\gamma} D$, for any $\gamma \in \pi_{1}\left(\overline{\mathbb{C}} \backslash\left\{u_{1}, u_{2}, u_{3}, \infty\right\}, \infty\right)$.

We now recall the definition of the connection matrices. Let us assume that $M_{i} \neq \mathbf{1}$, or equivalently $\mathcal{A}_{i} \neq 0$, for every $i=1,2,3$. We choose the fundamental matrices $Y_{i}(z)$ of the system (1.1), such that:
$$Y_{i}=G_{i}\left(\mathbf{1}+\mathcal{O}\left(z-u_{i}\right)\right)\left(z-u_{i}\right)^{J}, \quad \text { as } \quad z \rightarrow u_{i},$$
where $J$ is the Jordan normal form of $\mathcal{A}_{i}$, namely $J=\left(\begin{array}{ll}0 & 1 \\ 0 & 0\end{array}\right)$, the invertible matrix $G_{i}$ is defined by $\mathcal{A}_{i}=G_{i} J G_{i}^{-1}$, and the choice of the branch of $\log \left(z-u_{i}\right)$ needed in the definition of
$$\left(z-u_{i}\right)^{J}=\left(\begin{array}{cc}
1 & \log \left(z-u_{i}\right) \\
0 & 1
\end{array}\right)$$
is similar to the one above. The fundamental matrix $Y_{i}(z)$ is uniquely determined up to the ambiguity:
$$Y_{i}(z) \mapsto Y_{i}(z) R_{i},$$
where $R_{i}$ is any matrix commuting with $J$.
Continuing, along, say, the right-hand-side of the cut $\pi_{i}$, the solution $Y_{\infty}$ to a neighborhood of $u_{i}$, we obtain another fundamental matrix around $u_{i}$, that must be related to $Y_{i}(z)$ by:
$$Y_{\infty}(z)=Y_{i}(z) C_{i},$$
for some invertible matrix $C_{i}$. The matrices $C_{1}, C_{2}, C_{3}$ are called connection matrices, and are related to the monodromy matrices as follows:
$$M_{i}=C_{i}^{-1} \exp (2 \pi i J) C_{i}, \quad i=1,2,3 .$$

Lemma 1.1. Given three matrices $M_{1}, M_{2}, M_{3}, M_{i} \neq \mathbf{1}$ for every $i=1,2,3$, satisfying the relations (1.7) and (1.8), then
\begin{itemize}
\item[i)] there exist three matrices $C_{1}, C_{2}, C_{3}$ satisfying the (1.11). Moreover they are uniquely determined by the matrices $M_{1}, M_{2}, M_{3}$, up to the ambiguity $C_{i} \mapsto R_{i}^{-1} C_{i}$, where $R_{i} J=J R_{i}$, for $i=1,2,3$.
\item[ii)] If the matrices $M_{1}, M_{2}, M_{3}$ are the monodromy matrices of a Fuchsian system of the form (1.1), then any triple $C_{1}, C_{2}, C_{3}$ satisfying (1.11) can be realized as the connection matrices of the Fuchsian system itself.
\end{itemize}
Proof. i) By the (1.7), the monodromy matrices have all the eigenvalues equal to one; moreover they can be reduced to the Jordan normal form because $M_{i} \neq \mathbf{1}$. Namely there exists a matrix $\tilde{C}_{i}$ such that:
$$M_{i}=\tilde{C}_{i}^{-1}\left(\begin{array}{ll}
1 & 1 \\
0 & 1
\end{array}\right) \tilde{C}_{i} .$$
Taking
$$C_{i}=\left(\begin{array}{cc}
1 & 2 \pi i \\
0 & 1
\end{array}\right) \tilde{C}_{i}$$
we obtain the needed matrix. Two such matrices $C_{i}$ and $C_{i}^{\prime}$ give the same matrix $M_{i}$ if and only if $C_{i}^{-1} C_{i}^{\prime}$ commutes with $J$, namely if and only if they are related by $C_{i}=R_{i}^{-1} C_{i}^{\prime}$. ii) Let us now assume that $C_{1}^{\prime}, C_{2}^{\prime}, C_{3}^{\prime}$ are the connection matrices of a Fuchsian system of the form (1.1), with monodromy matrices $M_{1}, M_{2}, M_{3}$; id est $Y_{\infty}(z)=Y_{i}^{\prime}(z) C_{i}^{\prime}, i=1,2,3$, for some choice of the solutions $Y_{1}^{\prime}, Y_{2}^{\prime}$ and $Y_{3}^{\prime}$ of the form (1.9). We have
$$M_{i}=\left(C_{i}^{\prime}\right)^{-1} \exp (2 \pi i J) C_{i}^{\prime}=C_{i}^{-1} \exp (2 \pi i J) C_{i}, \quad i=1,2,3 .$$
So the matrices $R_{i}=C_{i}^{\prime} C_{i}^{-1}$ must commute with $J$ and $C_{1}, C_{2}, C_{3}$ are the connection matrices with respect to the new solutions $Y_{i}(z)=Y_{i}^{\prime}(z) R_{i}$. \(\square\)

Now, we state the result about the correspondence between monodromy data and coefficients of the Fuchsian system, for a given set of poles:

Lemma 1.2. Two Fuchsian systems (1.1) with the same poles $u_{1}, u_{2}$ and $u_{3}$, and the same value of $\mu$, coincide if and only if they have the same monodromy matrices $M_{1}, M_{2}$, $M_{3}$, with respect to the same basis of the loops $\gamma_{1}, \gamma_{2}$ and $\gamma_{3}$.

Proof. Let $Y_{\infty}^{(1)}(z)$ and $Y_{\infty}^{(2)}(z)$ be the fundamental matrices of the form (1.3) of the two Fuchsian systems. Let us consider the following matrix:
$$Y(z):=Y_{\infty}^{(2)}(z) Y_{\infty}^{(1)}(z)^{-1} .$$
$Y(z)$ is an analytic function around infinity:
$$Y(z)=1+\mathcal{O}\left(\frac{1}{z}\right), \quad \text { as } z \rightarrow \infty .$$

Since the monodromy matrices coincide, $Y(z)$ is a single valued function on $\overline{\mathbb{C}} \backslash\left\{u_{1}, u_{2}, u_{3}\right\}$. Let us prove that $Y(z)$ is analytic also at the points $u_{i}$. Due to Lemma 1.1, we can choose the fundamental matrices $Y_{i}^{(1)}(z)$ and $Y_{i}^{(2)}(z)$ in such a way that
$$Y_{\infty}^{(1),(2)}(z)=Y_{i}^{(1),(2)}(z) C_{i} \quad i=1,2,3 .$$
with the same connection matrices $C_{i}$. Then near the point $u_{i}$,
$$Y(z)=G_{i}^{(2)}\left(\mathbf{1}+\mathcal{O}\left(z-u_{i}\right)\right)\left[G_{i}^{(1)}\left(\mathbf{1}+\mathcal{O}\left(z-u_{i}\right)\right)\right]^{-1} .$$
This proves that $Y(z)$ is an analytic function on all $\overline{\mathbb{C}}$ and then, by the Liouville theorem
$$Y(z)=1,$$
and the two Fuchsian systems must coincide.
Corollary 1.1. Two Fuchsian systems (1.1) with the same poles $u_{1}, u_{2}$ and $u_{3}$, and the same value of $\mu$, are conjugated
$$\mathcal{A}_{i}^{(1)}=D^{-1} \mathcal{A}_{i}^{(2)} D, \quad i=1,2,3,$$
with a diagonal matrix $D$, if and only if their monodromy matrices $M_{i}^{(1)}$ and $M_{i}^{(2)}$, with respect to the same basis of the loops $\gamma_{1}, \gamma_{2}$ and $\gamma_{3}$, are conjugated:
$$M_{i}^{(1)}=D^{-1} M_{i}^{(2)} D, \quad i=1,2,3 .$$
1.1.2. The isomonodromy deformations of the Fuchsian system (1.1) and the Painlevé equation $\mathbf{P V I} \mu$. We now want to deform the poles of the Fuchsian system keeping the monodromy fixed. The theory of these deformations is described by the following two results:

Theorem 1.1. Let $M_{1}, M_{2}, M_{3}$ be the monodromy matrices of the Fuchsian system:
$$\frac{\mathrm{d}}{\mathrm{~d} z} Y^{0}=\left(\frac{\mathcal{A}_{1}^{0}}{z-u_{1}^{0}}+\frac{\mathcal{A}_{2}^{0}}{z-u_{2}^{0}}+\frac{\mathcal{A}_{3}^{0}}{z-u_{3}^{0}}\right) Y^{0},$$
of the above form (1.2), with pairwise distinct poles $u_{i}^{0}$, and with respect to some basis $\gamma_{1}, \gamma_{2}, \gamma_{3}$ of the loops in $\pi_{1}\left(\overline{\mathbb{C}} \backslash\left\{u_{1}^{0}, u_{2}^{0}, u_{3}^{0}, \infty\right\}, \infty\right)$. Then there exists a neighborhood $U \subset \mathbb{C}^{3}$ of the point $u^{0}=\left(u_{1}^{0}, u_{2}^{0}, u_{3}^{0}\right)$ such that, for any $u=\left(u_{1}, u_{2}, u_{3}\right) \in U$, there exists a unique triple $\mathcal{A}_{1}(u), \mathcal{A}_{2}(u), \mathcal{A}_{3}(u)$ of analytic matrix valued functions such that:
$$\mathcal{A}_{i}\left(u^{0}\right)=\mathcal{A}_{i}^{0}, \quad i=1,2,3,$$
and the monodromy matrices of the Fuchsian system
$$\frac{\mathrm{d}}{\mathrm{~d} z} Y=A(z ; u) Y=\left(\frac{\mathcal{A}_{1}(u)}{z-u_{1}}+\frac{\mathcal{A}_{2}(u)}{z-u_{2}}+\frac{\mathcal{A}_{3}(u)}{z-u_{3}}\right) Y,$$
with respect to the same basis ${ }^{1} \gamma_{1}, \gamma_{2}, \gamma_{3}$ of the loops, coincide with the given $M_{1}, M_{2}$, $M_{3}$. The matrices $\mathcal{A}_{i}(u)$ are the solutions of the Cauchy problem with the initial data $\mathcal{A}_{i}^{0}$ for the following Schlesinger equations:
$$\frac{\partial}{\partial u_{j}} \mathcal{A}_{i}=\frac{\left[\mathcal{A}_{i}, \mathcal{A}_{j}\right]}{u_{i}-u_{j}}, \quad \frac{\partial}{\partial u_{i}} \mathcal{A}_{i}=-\sum_{j \neq i} \frac{\left[\mathcal{A}_{i}, \mathcal{A}_{j}\right]}{u_{i}-u_{j}} .$$
The solution $Y_{\infty}^{0}(z)$ of (1.12) of the form (1.3) can be uniquely continued, for $z \neq u_{i}$ $i=1,2,3$, to an analytic function
$$Y_{\infty}(z, u), \quad u \in U,$$
such that
$$Y_{\infty}\left(z, u^{0}\right)=Y_{\infty}^{0}(z) .$$
This continuation is the local solution of the Cauchy problem with the initial data $Y_{\infty}^{0}$ for the following system that is compatible to the system (1.13):
$$\frac{\partial}{\partial u_{i}} Y=-\frac{\mathcal{A}_{i}(u)}{z-u_{i}} Y .$$
Moreover the functions $\mathcal{A}_{i}(u)$ and $Y_{\infty}(z, u)$ can be continued analytically to global meromorphic functions on the universal coverings of
$$\mathbb{C}^{3} \backslash\{\text { diags }\}:=\left\{\left(u_{1}, u_{2}, u_{3}\right) \in \mathbb{C}^{3} \mid u_{i} \neq u_{j} \text { for } i \neq j\right\},$$
and
$$\left\{\left(z, u_{1}, u_{2}, u_{3}\right) \in \mathbb{C}^{4} \mid u_{i} \neq u_{j} \text { for } i \neq j \text { and } z \neq u_{i}, i=1,2,3\right\},$$
respectively.
The proof can be found, for example, in [Mal], [Miwa], [Sib]. We recall the theorem of solvability of the inverse problem of the monodromy (see [Dek]):

Theorem 1.2. Given three arbitrary matrices, satisfying (1.7) and (1.8), with $M_{\infty}$ of the form (1.4), and given a point $u^{0}=\left(u_{1}^{0}, u_{2}^{0}, u_{3}^{0}\right) \in \mathbb{C}^{3} \backslash\{$ diags $\}$, for any neighborhood $U$ of $u^{0}$, there exist $\left(u_{1}, u_{2}, u_{3}\right) \in U$ and a Fuchsian system of the form (1.1), with the given monodromy matrices, the given $\mu$ and with poles in $u_{1}, u_{2}, u_{3}$.

Remark 1.1. Fuchsian systems of the form (1.1), with coefficients $\mathcal{A}_{i}$ satisfying (1.2), depend on four parameters, one of them being $\mu$. The triples of the monodromy matrices satisfying (1.7) and (1.8), with $M_{\infty}$ of the form (1.4), depend on four parameters too. Loosely speaking, Theorems 1.1 and 1.2 claim that, not only the monodromy matrices are first integrals for the equations of isomonodromy deformation (1.14), but they provide

\footnotetext{
${ }^{1}$ Observe that the basis $\gamma_{1}, \gamma_{2}, \gamma_{3}$ of $\pi_{1}\left(\overline{\mathbb{C}} \backslash\left\{u_{1}, u_{2}, u_{3}, \infty\right\}, \infty\right)$ varies continuously with small variations of $u_{1}, u_{2}, u_{3}$. This new basis is homotopic to the initial one, so we can identify them.
}
a full system of first integrals for such equations. We denote $\mathcal{A}\left(u_{1}, u_{2}, u_{3} ; M_{1}, M_{2}, M_{3}\right)$ the solution of the Schlesinger equations locally uniquelly determined by the triple of monodromy matrices $\left(M_{1}, M_{2}, M_{3}\right)$.

All the above arguments remain valid for a general 2 × 2 Fuchsian system, provided the non-resonancy condition of the eigenvalues of $\mathcal{A}_{i}$ and $\mathcal{A}_{\infty}$.

Remark 1.2. We observe that the isomonodromy deformations equations preserve the connection matrices $C_{i}$ too. This follows from Lemma 1.1.
1.1.3. Reduction to the $\mathbf{P V I} \mu$ equation. Let us now explain, following [JMU], how to reduce the Schlesinger equations (1.14) to the $\mathrm{PVI} \mu$ equation. The Schlesinger equations are invariant with respect to the gauge transformations of the form:
$$\mathcal{A}_{i} \mapsto D^{-1} \mathcal{A}_{i} D, \quad i=1,2,3, \quad \text { for any } D \text { diagonal matrix. }$$
First of all we have to factor out such gauge transformations; to this aim, we introduce two coordinates $(p, q)$ on the quotient of the space of the matrices satisfying (1.2) with respect to the equivalence relation
$$\mathcal{A}_{i} \sim D^{-1} \mathcal{A}_{i} D, \quad i=1,2,3, \quad \text { for any } D \text { diagonal matrix. }$$
The coordinates $(p, q)$ are defined as follows: $q$ is the root of the following linear equation:
$$\left[\mathcal{A}\left(q ; u_{1}, u_{2}, u_{3}\right)\right]_{12}=0,$$
and $p$ is given by:
$$p=\left[\mathcal{A}\left(q ; u_{1}, u_{2}, u_{3}\right)\right]_{11},$$
where $\mathcal{A}\left(z ; u_{1}, u_{2}, u_{3}\right)$ is given in (1.13). The matrices $\mathcal{A}_{i}$ are expressed rationally in terms of the coordinates $(p, q)$ and an auxiliary coordinate $k$, coming from the gauge freedom (1.15):
$$\begin{aligned}
& \left(\mathcal{A}_{i}\right)_{11}=-\left(\mathcal{A}_{i}\right)_{22}=\frac{q-u_{i}}{2 \mu P^{\prime}\left(u_{i}\right)}\left[P(q) p^{2}+2 \mu \frac{P(q)}{q-u_{i}} p+\mu^{2}\left(q+2 u_{i}-\sum_{j} u_{j}\right)\right], \\
& \left(\mathcal{A}_{i}\right)_{12}=-\mu k \frac{q-u_{i}}{P^{\prime}\left(u_{i}\right)}, \\
& \left(\mathcal{A}_{i}\right)_{21}=k^{-1} \frac{q-u_{i}}{4 \mu^{3} P^{\prime}\left(u_{i}\right)}\left[P(q) p^{2}+2 \mu \frac{P(q)}{q-u_{i}} p+\mu^{2}\left(q+2 u_{i}-\sum_{j} u_{j}\right)\right]^{2},
\end{aligned}$$
for $i=1,2,3$, where $P(z)=\left(z-u_{1}\right)\left(z-u_{2}\right)\left(z-u_{3}\right)$ and $P^{\prime}(z)=\frac{\mathrm{d} P}{\mathrm{~d} z}$. The Schlesinger equations in these coordinates reduce to:
$$\begin{aligned}
\frac{\partial q}{\partial u_{i}} & =\frac{P(q)}{P^{\prime}\left(u_{i}\right)}\left[2 p+\frac{1}{q-u_{i}}\right] \\
\frac{\partial p}{\partial u_{i}} & =-\frac{P^{\prime}(q) p^{2}+\left(2 q+u_{i}-\sum_{j} u_{j}\right) p+\mu(1-\mu)}{P^{\prime}\left(u_{i}\right)},
\end{aligned}$$
for $i=1,2,3$. The system of the reduced Schlesinger equations (1.17) is invariant under the transformations of the form
$$u_{i} \mapsto a u_{i}+b, \quad q \mapsto a q+b, \quad p \mapsto \frac{p}{a}, \quad \forall a, b \in \mathbb{C}, \quad a \neq 0 .$$
We introduce the following new invariant variables:
$$\begin{aligned}
& x=\frac{u_{2}-u_{1}}{u_{3}-u_{1}}, \\
& y=\frac{q-u_{1}}{u_{3}-u_{1}} ;
\end{aligned}$$
the system (1.17), expressed in the these new variables, reduces to the $\mathrm{PVI} \mu$ equation for $y(x)$.

Remark 1.3. The system (1.17) admits the following singular solutions (see [Ok1] and [Wat]):
$$q \equiv u_{i} \quad \text { for some } i,$$
and $p$, in the variable $x$, can be expressed via Gauss hypergeometric functions (see [Ok1]). Moreover the monodromy group of the system (1.1) reduces to the monodromy group of the Gauss hypergeometric equation, namely the following lemma holds true:

Lemma 1.3. The solutions of the full Schlesinger equations, corresponding to the solution $q \equiv u_{i}$, for some $i$, have the form:
$$A_{i}(u) \equiv 0, \quad \text { and for } j \neq i \quad A_{j}(u)=D(u)^{-1} A_{j}^{0} D(u),$$
where $D(u)$ is a diagonal matrix depending on $u$, and $A_{j}^{0}$ is a constant matrix. The monodromy matrix $M_{i}$ of the corresponding Fuchsian system turns out to be the identity. Conversely, if one of the monodromy matrices $M_{i}$ is the identity, $M_{i}=\mathbf{1}$, then the solution of (1.17) is degenerate.

Proof. The matrix $A_{i}$, for $q \equiv u_{i}$, is identically 0 , thanks to (1.16). Having $A_{i} \equiv 0, M_{i}$ is 1. Conversely, if $M_{i}=\mathbf{1}$, then $A_{i} \equiv 0$. Solving the Schlesinger equations (1.13), we obtain $q \equiv u_{i}$, and the equation for $p$ is reduced to a Gauss hypergeometric equation. \(\square\)

The singular solutions do not give any solution of the $\mathrm{PVI} \mu$ equation. All the other solutions do, via (1.18). Conversely, starting from any solution $y(x)$ of $\mathrm{PVI} \mu$, we arrive at the solution:
$$\begin{aligned}
q & =\left(u_{3}-u_{1}\right) y\left(\frac{u_{2}-u_{1}}{u_{3}-u_{1}}\right)+u_{1} \\
p & =\frac{P^{\prime}\left(u_{2}\right)}{2 P(q)} y^{\prime}\left(\frac{u_{2}-u_{1}}{u_{3}-u_{1}}\right)-\frac{1}{2} \frac{1}{q-u_{2}}
\end{aligned}$$
of the reduced Schlesinger equations (1.17). To obtain a solution of the full Schlesinger equations, the function $k$ must be given by a quadrature:
$$\frac{\partial k}{\partial u_{i}}=(2 \mu-1) \frac{q-u_{i}}{P^{\prime}\left(u_{i}\right)} .$$
We conclude this section summarizing all the above results in the following:

Theorem 1.3. The branches of solutions of the PVI $\mu$ equation near a given point $x_{0} \in$ $\overline{\mathbb{C}} \backslash\{0,1, \infty\}$, are in one-to-one correspondence with the triples of the monodromy matrices $M_{1}, M_{2}, M_{3}$ satisfying (1.7) and (1.8), with $M_{\infty}$ of the form (1.4), none of them being equal to 1, considered modulo diagonal conjugations.

Remark 1.4. A triple of $2 \times 2$ matrices $M_{1}, M_{2}, M_{3} \in S L(2 ; \mathbb{C})$, considered modulo conjugations, is a point $\rho$ of the space of representations
$$\rho: F_{3} \rightarrow S L(2 ; \mathbb{C})$$
of the free group $F_{3}$ with three generators $\gamma_{1}, \gamma_{2}, \gamma_{3}$, specified by
$$M_{i}=\rho\left(\gamma_{i}\right), \quad i=1,2,3 .$$
In the general case, i.e. with the matrices $\mathcal{A}_{i}$ and $\mathcal{A}_{\infty}$ not necassarly of the form (1.2), the corresponding solution $(p, q)$ of the reduced Schlesinger equations will be denoted
$$p=p\left(u_{1}, u_{2}, u_{3} ; \rho\right), \quad q=q\left(u_{1}, u_{2}, u_{3} ; \rho\right) .$$
It is locally uniquelly specified by the representation $\rho$, provided the non-resonancy condition of the eigenvalues of $\mathcal{A}_{i}$ and $\mathcal{A}_{\infty}$.

\subsection*{1.2. The structure of the analytic continuation.}

We parameterized branches of the solutions of $\mathrm{PVI} \mu$ by triples of monodromy matrices. Now we show how do these parameters change with a change of the branch in the process of analytic continuation of the solutions along a path in $\overline{\mathbb{C}} \backslash\{0,1, \infty\}$. Recall that, as it follows from Theorem 1.1, the solutions of $\mathrm{PVI} \mu$, defined in a neighborhood of a given point $x_{0} \in \overline{\mathbb{C}} \backslash\{0,1, \infty\}$, can be analytically continued to a meromorphic function on the universal covering of $\overline{\mathbb{C}} \backslash\{0,1, \infty\}$ (the above mentioned Painlevé Property). The fundamental group $\pi_{1}(\overline{\mathbb{C}} \backslash\{0,1, \infty\})$ is non-abelian. As a consequence, the global structure of the analytic continuation of the solutions of PVI is more involved than that of the other Painlevé equations. In fact the solutions of PI,..., PV have at most two critical singularities and the corresponding fundamental group is abelian.

As a first step we introduce a parameterization of the monodromy matrices.
1.2.1. The parameterization of the monodromy data Let $\mathcal{M}_{1}, \mathcal{M}_{2}$ and $\mathcal{M}_{3}$ be three linear operators $\mathcal{M}_{i}: \mathbb{C}^{2} \rightarrow \mathbb{C}^{2}$ satisfying (1.7). We introduce for them a parameterization which will be useful for studying the analytic continuation of the solutions of the $\mathrm{PVI} \mu$ equation.

Lemma 1.4. If $\mathcal{M}_{1}, \mathcal{M}_{2}$ are such that
$$\operatorname{Tr}\left(\mathcal{M}_{1} \mathcal{M}_{2}\right) \neq 2,$$
then there exists a basis in $\mathbb{C}^{2}$ such that, in this basis, the matrices of $\mathcal{M}_{1}, \mathcal{M}_{2}$ have the form:
$$M_{1}=\left(\begin{array}{cc}
1 & -x_{1} \\
0 & 1
\end{array}\right), \quad M_{2}=\left(\begin{array}{cc}
1 & 0 \\
x_{1} & 1
\end{array}\right),$$
where $x_{1}=\sqrt{2-\operatorname{Tr}\left(\mathcal{M}_{1} \mathcal{M}_{2}\right)}$; when $\mathcal{M}_{1}, \mathcal{M}_{2}$ are such that $\operatorname{Tr}\left(\mathcal{M}_{1} \mathcal{M}_{2}\right)=2$, they have a common eigenvector, and then there exists a basis in $\mathbb{C}^{2}$ such that, in this basis, the matrices $M_{1}, M_{2}$ are both upper-triangular.

Proof. Due to the (1.7), there exist two vectors $e_{1}$ and $e_{2}$ such that
$$\mathcal{M}_{1} e_{1}=e_{1}, \quad \mathcal{M}_{2} e_{2}=e_{2} .$$
We now prove that these two vectors are linearly dependent if and only if $\operatorname{Tr}\left(\mathcal{M}_{1} \mathcal{M}_{2}\right)=2$. In fact if the two vectors are linearly dependent, then we can find a linear independent vector $e_{2}^{\prime}$ such that, in the basis $\left(e_{1}, e_{2}^{\prime}\right)$ the matrices of $M_{1}, M_{2}$ have the form:
$$M_{1}=\left(\begin{array}{cc}
1 & \lambda_{1} \\
0 & 1
\end{array}\right), \quad M_{2}=\left(\begin{array}{cc}
1 & \lambda_{2} \\
0 & 1
\end{array}\right),$$
so $\operatorname{Tr}\left(M_{1} M_{2}\right)=2$. Conversely, in the basis $\left(e_{1}, e_{2}^{\prime}\right)$ the matrix $M_{1}$ has the form $M_{1}=$ $\left(\begin{array}{cc}1 & \lambda_{1} \\ 0 & 1\end{array}\right)$ and, requiring that
$$\operatorname{Tr}\left(\mathcal{M}_{1} \mathcal{M}_{2}\right)=2, \quad \operatorname{eigenv}\left(M_{2}\right)=1,$$
also the matrix $M_{2}$ must have the above form $M_{2}=\left(\begin{array}{cc}1 & \lambda_{2} \\ 0 & 1\end{array}\right)$. Then, the two vectors $e_{1}$ and $e_{2}$ are linearly dependent. As a consequence, if $\operatorname{Tr}\left(\mathcal{M}_{1} \mathcal{M}_{2}\right) \neq 2$, the two vectors $e_{1}$ and $e_{2}$ are linearly independent, and in the basis $\left(e_{1}, e_{2}\right)$ the matrices of $M_{1}, M_{2}$ have the form:
$$M_{1}=\left(\begin{array}{cc}
1 & \lambda_{1} \\
0 & 1
\end{array}\right), \quad M_{2}=\left(\begin{array}{cc}
1 & 0 \\
\lambda_{2} & 1
\end{array}\right),$$
with $\operatorname{Tr}\left(M_{1} M_{2}\right)=2+\lambda_{1} \lambda_{2}$. Rescaling the basic vectors $\left(e_{1}, e_{2}\right)$, we obtain the (1.19). QED

Lemma 1.5. Let $\mathcal{M}_{1}, \mathcal{M}_{2}, \mathcal{M}_{3}$ satisfy also the condition (1.8) with $\mathcal{M}_{\infty}$ given by (1.4), and $2 \mu \notin \mathbb{Z}$. Then the following statements are true:
\begin{itemize}
\item[i)] If two of the following numbers
$$\operatorname{Tr}\left(\mathcal{M}_{1} \mathcal{M}_{2}\right), \quad \operatorname{Tr}\left(\mathcal{M}_{1} \mathcal{M}_{3}\right), \quad \operatorname{Tr}\left(\mathcal{M}_{3} \mathcal{M}_{2}\right)$$
are equal to 2, then one of the matrices of $M_{i}$ is equal to one.
\item[ii)] If $\operatorname{Tr}\left(\mathcal{M}_{1} \mathcal{M}_{2}\right) \neq 2$, then there exists a basis in $\mathbb{C}^{2}$ such that, in this basis, the matrices $M_{1}, M_{2}$ and $M_{3}$ have the form
$$M_{1}=\left(\begin{array}{cc}
1 & -x_{1} \\
0 & 1
\end{array}\right), \quad M_{2}=\left(\begin{array}{cc}
1 & 0 \\
x_{1} & 1
\end{array}\right), \quad M_{3}=\left(\begin{array}{cc}
1+\frac{x_{2} x_{3}}{x_{1}} & -\frac{x_{2}^{2}}{x_{1}} \\
\frac{x_{3}^{2}}{x_{1}} & 1-\frac{x_{2} x_{3}}{x_{1}}
\end{array}\right),$$
where
$$\operatorname{Tr}\left(M_{1} M_{2}\right)=2-x_{1}^{2}, \quad \operatorname{Tr}\left(M_{3} M_{2}\right)=2-x_{2}^{2}, \quad \operatorname{Tr}\left(M_{1} M_{3}\right)=2-x_{3}^{2},$$
\end{itemize}
\begin{itemize}
\item[] and
$$x_{1}^{2}+x_{2}^{2}+x_{3}^{2}-x_{1} x_{2} x_{3}=4 \sin ^{2} \pi \mu .$$
\item[iii)] If two triples of matrices $M_{1}, M_{2}, M_{3}$ and $M_{1}^{\prime}, M_{2}^{\prime}, M_{3}^{\prime}$ satisfying (1.8), with none of them equal to 1, have the form (1.20) with the parameters $\left(x_{1}, x_{2}, x_{3}\right)$ and $\left(x_{1}^{\prime}, x_{2}^{\prime}, x_{3}^{\prime}\right)$ respectively, then these triples are conjugated
$$M_{i}=T^{-1} M_{i}^{\prime} T$$
with some invertible matrix $T$ if and only if the triple $\left(x_{1}^{\prime}, x_{2}^{\prime}, x_{3}^{\prime}\right)$ is equal to the triple $\left(x_{1}, x_{2}, x_{3}\right)$, up to the change of the sign of two of the coordinates.
\end{itemize}

Proof.
\begin{itemize}
\item[i)] Let us assume that
$$\operatorname{Tr}\left(\mathcal{M}_{1} \mathcal{M}_{2}\right)=2, \quad \operatorname{Tr}\left(\mathcal{M}_{1} \mathcal{M}_{3}\right)=2 .$$
Let $e_{1}$ and $e_{3}$ be the common eigenvectors of $\mathcal{M}_{1}, \mathcal{M}_{2}$ and $\mathcal{M}_{1}, \mathcal{M}_{3}$ respectively, (see Lemma 1.4). If $\mathcal{M}_{1} \neq \mathbf{1}$, then the eigenvectors $e_{1}$ and $e_{3}$ coincide. Then we can find a linear independent vector $e_{2}^{\prime}$ such that, in the basis $\left(e_{1}, e_{2}^{\prime}\right)$ the matrices of $M_{1}, M_{2}$, $M_{3}$ all have the form
$$M_{i}=\left(\begin{array}{cc}
1 & \lambda_{i} \\
0 & 1
\end{array}\right), \quad i=1,2,3 .$$
Then
$$\operatorname{Tr}\left(M_{3} M_{2} M_{1}\right) 1 \operatorname{Tr}\left(M_{\infty}\right)=2 .$$
This contradicts the assumption $2 \mu \notin \mathbb{Z}$.
\item[ii)] Let us choose the basis such that, according to Lemma 1.4, the matrices $M_{1}, M_{2}$ have the form (1.19). Solving the equations
$$\operatorname{Tr}\left(M_{3} M_{2}\right)=2-x_{2}^{2}, \quad \operatorname{Tr}\left(M_{1} M_{3}\right)=2-x_{3}^{2},$$
we arrive at the formula (1.20). The (1.21) is obtained by straightforward computations from
$$\operatorname{Tr}\left(M_{3} M_{2} M_{1}\right)=2 \cos 2 \pi \mu .$$
\item[iii)] The two triples of matrices $M_{1}, M_{2}, M_{3}$ and $M_{1}^{\prime}, M_{2}^{\prime}, M_{3}^{\prime}$ are conjugated
$$M_{i}=T^{-1} M_{i}^{\prime} T$$
with some invertible matrix $T$ if and only if they are the matrices of the same operators $\mathcal{M}_{1}, \mathcal{M}_{2}, \mathcal{M}_{3}$, written in different bases. Since the traces do not depend on the choice of the basis, then
$$x_{i}^{2}={x_{i}^{\prime}}^{2}, \quad i=1,2,3 .$$
According to the proof of Lemma 1.4, the basis $\left(e_{1}, e_{2}\right)$ is uniquely determined up to changes of sign. A change of sign $e_{1} \mapsto-e_{1}$ corresponds to the change of sign $x_{1} \mapsto-x_{1}$; then the form of the matrix $M_{3}$ is preserved if and only if we change one of the signs of $x_{2}$ or $x_{3}$. \(\square\)
\end{itemize}

Remark 1.5. The matrices (1.20) have a simple geometrical meaning. Let us consider the three-dimensional linear space with a basis $\left(e_{1}, e_{2}, e_{3}\right)$ and with a skew-symmetric bilinear form $\{\cdot, \cdot\}$ such that
$$\left\{e_{1}, e_{2}\right\}=x_{1}, \quad\left\{e_{1}, e_{3}\right\}=x_{3}, \quad\left\{e_{2}, e_{3}\right\}=x_{2} .$$
Let us consider the reflections $R_{1}, R_{2}, R_{3}$ in this space, with respect to the hyperplanes skew-orthogonal to the basic vectors:
$$R_{i}(x)=x-\left\{e_{i}, x\right\} e_{i}, \quad i=1,2,3 .$$
The reflections have a one-dimensional invariant subspace, namely the kernel of the bilinear form. The matrices of the reflections acting on the quotient are the (1.20).

Definition. A triple $\left(x_{1}, x_{2}, x_{3}\right)$ is called admissible if it has at most one coordinate equal to zero. Two such triples are called equivalent if they are equal up to the change of two signs of the coordinates.

Observe that for an admissible triple $\left(x_{1}, x_{2}, x_{3}\right)$ none of the matrices (1.20) is equal to the identity. So the admissible triples correspond to the non-singular solutions of the reduced Schlesinger equations (1.17). Moreover, two equivalent triples generate the same solution. We can summarize the above results in the following:

Theorem 1.4. The branches of solutions of the PVI $\mu$ equation near a given point $x_{0} \in$ $\overline{\mathbb{C}} \backslash\{0,1, \infty\}$ are in one-to-one correspondence with the equivalence classes of the admissible triples satisfying (1.21).

Proof. Starting from a solution of $\mathrm{PVI} \mu$ we obtain the monodromy matrices satisfying (1.7). None of them is equal to the identity. So the canonical form (1.20) of $M_{1}, M_{2}, M_{3}$ is determined uniquely up to a choice of the admissible triple $\left(x_{1}, x_{2}, x_{3}\right)$ within the equivalence class. Conversely, given an admissible triple $\left(x_{1}, x_{2}, x_{3}\right)$ satisfying (1.21), we obtain the matrices $M_{1}, M_{2}, M_{3}$ of the form (1.20). The matrix $M_{3} M_{2} M_{1}$ is diagonalizable with the eigenvalues $\exp ( \pm 2 \pi i \mu)$ (here we use the non-resonance condition $2 \mu \notin \mathbb{Z}$ ). Reducing this matrix to the diagonal form
$$M_{3} M_{2} M_{1}=T^{-1}\left(\begin{array}{cc}
\exp (2 \pi i \mu) & 0 \\
0 & \exp (-2 \pi i \mu)
\end{array}\right) T$$
we obtain the monodromy matrices $T M_{i} T^{-1}$ satisfying (1.7) and thus specifying a branch of the solution of $\mathrm{PVI} \mu$.
1.2.2. Monodromy data and symmetries of $\mathbf{P V I} \mu$. The Painlevé VI equation possesses a rich family of symmetries, i. e. transformations of the dependent and independent variables $(y, x)$, and also of the parameters, that preserve the shape of the equation. The theory of these symmetries, and its applications to the construction of particular solutions, was developed in [Ok]. Here we list the symmetries which preserve our $\mathrm{PVI} \mu$ and compute their action on the monodromy data.

First of all we observe that the trivial symmetry $\mu \mapsto 1-\mu$ preserves the Painleve' equation, i.e. $\operatorname{PVI} \mu=\operatorname{PVI}(1-\mu)$, so it maps the solutions $y(x)$ in themselves.

Then we consider the permutations of the poles $u_{1}, u_{2}, u_{3}$ which generate the action of the symmetric group $S_{3}$ on the solutions $y(x)$. In particular the involution
$$i_{1}: u_{2} \leftrightarrow u_{3},$$
produces the transformation
$$x \mapsto \frac{1}{x}, \quad y \mapsto \frac{y}{x},$$
and
$$i_{2}: u_{1} \leftrightarrow u_{3},$$
produces the transformation
$$x \mapsto 1-x, \quad y \mapsto 1-y .$$
Both these transformations clearly preserve the equation $\mathrm{PVI} \mu$.
Let us compute the action of these symmetries on the monodromy data. The only thing that changes is the basis in the fundamental group $\pi_{1}\left(\overline{\mathbb{C}} \backslash\left\{u_{1}, u_{2}, u_{3}, \infty\right\}\right)$. In fact, the cuts $\pi_{1}, \pi_{2}, \pi_{3}$ along which we take our basis $\gamma_{1}, \gamma_{2}, \gamma_{3}$, are ordered according to the order of the poles. Applying the transformation $i_{1}$ we then arrive at the new basis $\gamma_{1}^{\prime}, \gamma_{2}^{\prime}, \gamma_{3}^{\prime}$ shown in figure 2.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/64ce0006-7367-4aae-9e25-7b8a1be4f808-19.jpg?height=486&width=471&top_left_y=1510&top_left_x=866}
\captionsetup{labelformat=empty}
\caption{Fig.2. The new basis $\gamma_{1}^{\prime}, \gamma_{2}^{\prime}, \gamma_{3}^{\prime}$ obtained by the action of $i_{1}$.}
\end{figure}
This new basis has the following form
$$\gamma_{1}^{\prime}=\gamma_{1}, \quad \gamma_{2}^{\prime}=\gamma_{2} \gamma_{3} \gamma_{2}^{-1}, \quad \gamma_{3}^{\prime}=\gamma_{2} .$$
As a consequence the new monodromy matrices are
$$M_{1}^{\prime}=M_{1}, \quad M_{2}^{\prime}=M_{2}^{-1} M_{3} M_{2}, \quad M_{3}^{\prime}=M_{2} .$$

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/64ce0006-7367-4aae-9e25-7b8a1be4f808-20.jpg?height=486&width=599&top_left_y=240&top_left_x=811}
\captionsetup{labelformat=empty}
\caption{Fig.3. The new basis $\gamma_{1}^{\prime}, \gamma_{2}^{\prime}, \gamma_{3}^{\prime}$ obtained by the action of $i_{2}$.}
\end{figure}
For the second transformation $i_{2}$, the basis of the new loops is shown in figure 3. It has the following form
$$\gamma_{1}^{\prime}=\gamma_{3}, \quad \gamma_{2}^{\prime}=\gamma_{3}^{-1} \gamma_{2} \gamma_{3}, \quad \gamma_{3}^{\prime}=\gamma_{3}^{-1} \gamma_{2}^{-1} \gamma_{1} \gamma_{2} \gamma_{3} .$$
The new monodromy matrices are
$$M_{1}^{\prime}=M_{3}, \quad M_{2}^{\prime}=M_{3} M_{2}^{-1} M_{3}, \quad M_{3}^{\prime}=M_{3} M_{2} M_{1} M_{2}^{-1} M_{3}^{-1} .$$

Lemma 1.6. In the coordinates $\left(x_{1}, x_{2}, x_{3}\right)$ on the space of the monodromy matrices, the action of the symmetries $i_{1}, i_{2}$ is given by the formulae
$$i_{1}:\left(x_{1}, x_{2}, x_{3}\right) \mapsto\left(x_{3}-x_{1} x_{2},-x_{2}, x_{1}\right), \quad i_{2}:\left(x_{1}, x_{2}, x_{3}\right) \mapsto\left(-x_{2},-x_{1}, x_{1} x_{2}-x_{3}\right) .$$
The proof is straightforward.
The last symmetry is more complicated because it changes the value of the parameter $\mu$, i.e. $\mu \mapsto-\mu$, or equivalently $\mu \mapsto 1+\mu$ as it follows form the fact that PVI $(-\mu)=$ PVI $(1+\mu)$. This simmetry comes from the following simultaneous conjugation of the coefficients of the Fuchsian system:
$$A_{i} \rightarrow \Sigma A_{i} \Sigma,$$
where
$$\Sigma=\Sigma^{-1}=\left(\begin{array}{ll}
0 & 1 \\
1 & 0
\end{array}\right) .$$
Indeed,
$$\Sigma A_{\infty} \Sigma=-A_{\infty} .$$
Using the parameterization (1.16) of the matrices $A_{1}, A_{2}, A_{3}$ by the coordinates $(p, q)$, we arrive at the following

Lemma 1.7. The formula
$$\tilde{y}=y \frac{\left(p_{0}\left(y^{\prime}\right)^{2}+p_{1} y^{\prime}+p_{2}\right)^{2}}{q_{0}\left(y^{\prime}\right)^{4}+q_{1}\left(y^{\prime}\right)^{3}+q_{2}\left(y^{\prime}\right)^{2}+q_{3} y^{\prime}+q_{4}},$$
where
$$\begin{aligned}
p_{0} & =x^{2}(x-1)^{2} \\
p_{1} & =2 x(x-1)(y-1)[2 \mu(y-x)-y] \\
p_{2} & =y(y-1)\left[y(y-1)-4 \mu(y-1)(y-x)+4 \mu^{2}(y-x)(y-x-1)\right] \\
q_{0} & =x^{4}(x-1)^{4} \\
q_{1} & =-4 x^{3}(x-1)^{3} y(y-1) \\
q_{2} & =2 x^{2}(x-1)^{2} y(y-1)\left[3 y(y-1)+4 \mu^{2}(y-x)(1+x-3 y)\right] \\
q_{3} & =4 x(x-1) y^{2}(y-1)^{2}\left[-y(y-1)-16 \mu^{3}(y-x)^{2}+4 \mu^{2}(y-x)(3 y-x-1)\right] \\
q_{4} & =y^{2}(y-1)^{2}\left\{y^{2}(y-1)^{2}+64 \mu^{3} y(y-1)(y-x)^{2}-8 \mu^{2} y(y-1)(y-x)(3 y-x-1)+\right. \\
& \left.+16 \mu^{4}(y-x)^{2}\left[(x-1)^{2}+y(2+2 x-3 y)\right]\right\}
\end{aligned}$$
transforms solutions of PVI $\mu$ to solutions of PVI $(-\mu)$. The class of equivalence of the monodromy data $\left(x_{1}, x_{2}, x_{3}\right)$ does not change under such a symmetry.

Proof. The new monodromy matrices $M_{1}^{\prime}, M_{2}^{\prime}, M_{3}^{\prime}$ have the form
$$M_{i}^{\prime}=\Sigma M_{i} \Sigma, \quad i=1,2,3 .$$
Then, the canonical form (1.20) of the monodromy operators does not change. \(\square\)

Other symmetries are superpositions of (1.24) with the trivial one $\mu \rightarrow 1-\mu$. Using these symmetries, one can transform $\mathrm{PVI}_{\mu}$ to $\mathrm{PVI}_{\mu^{\prime}}$, with $\mu^{\prime}= \pm \mu+n$ for an arbitrary integer $n$.

Remark 1.6. One can show that the above symmetries, and their superpositions, exhaust all the birational transformations preserving our one-parameter family of PVI equations. We will not do it here (see [Ok]). It is important, however, that these symmetries preserve the class of algebraic solutions of $\mathrm{PVI} \mu$. We will classify all the algebraic solutions modulo the above symmetries.

Remark 1.7. It is not difficult to show that the denominator of the formula (1.24) does not vanish identically for any solution of $\mathrm{PVI} \mu$, with $2 \mu \notin \mathbb{Z}$. Indeed, eliminating $y_{x x}$ and $y_{x}$ form the system
$$\begin{aligned}
y_{x x}= & \frac{1}{2}\left(\frac{1}{y}+\frac{1}{y-1}+\frac{1}{y-x}\right) y_{x}^{2}-\left(\frac{1}{x}+\frac{1}{x-1}+\frac{1}{y-x}\right) y_{x} \\
& +\frac{1}{2} \frac{y(y-1)(y-x)}{x^{2}(x-1)^{2}}\left[(2 \mu-1)^{2}+\frac{x(x-1)}{(y-x)^{2}}\right],
\end{aligned}$$
$$\begin{aligned}
Q\left(y_{x}, y, x, \mu\right) & =0, \\
\frac{\mathrm{~d}}{\mathrm{~d} x} Q\left(y_{x}, y, x, \mu\right) & =0,
\end{aligned}$$
where $Q$ is the denominator, the resultant equation
$$(2 \mu+1)^{4} \mu^{16}\left[x(x-1)^{2}\right]^{4}[y(y-1)(y-x)]^{4}$$
never vanishes.
1.2.3. The analytic continuation of the solutions of $\mathbf{P V I} \mu$ and the braid group $B_{3}$. In this subsection, we describe the procedure of the analytic continuation towards an action of the braid group on the admissible triples $\left(x_{1}, x_{2}, x_{3}\right)$ parameterizing the branches of the solutions of $\mathrm{PVI} \mu$.

According to Theorem 1.1, any solution of the Schlesinger equations can be continued analytically from a point $\left(u_{1}^{0}, u_{2}^{0}, u_{3}^{0}\right)$ to another point $\left(u_{1}^{1}, u_{2}^{1}, u_{3}^{1}\right)$ along a path
$$\left(u_{1}(t), u_{2}(t), u_{3}(t)\right) \in \mathbb{C}^{3} \backslash\{\operatorname{diags}\}, \quad 0 \leq t \leq 1,$$
with
$$u_{i}(0)=u_{i}^{0}, \quad \text { and } \quad u_{i}(1)=u_{i}^{1},$$
provided that the end-points are not the poles of the solution. The result of the analytic continuation depends only on the homotopy class of the path in $\mathbb{C}^{3} \backslash\{d i a g s\}$. Particularly, to find all the branches of a solution near a given point $u^{0}=\left(u_{1}^{0}, u_{2}^{0}, u_{3}^{0}\right)$ one has to compute the results of the analytic continuation along any homotopy class of closed loops in $\mathbb{C}^{3} \backslash\{$ diags $\}$ with the beginning and the end at the point $u^{0}=\left(u_{1}^{0}, u_{2}^{0}, u_{3}^{0}\right)$. Let
$$\beta \in \pi_{1}\left(\mathbb{C}^{3} \backslash\{\text { diags }\} ; u^{0}\right)$$
be an arbitrary loop. Any solution of the Schlesinger equations near the point $u^{0}=$ $\left(u_{1}^{0}, u_{2}^{0}, u_{3}^{0}\right)$, is uniquely determined by the monodromy matrices $M_{1}, M_{2}$ and $M_{3}$, computed in the basis $\gamma_{1}, \gamma_{2}, \gamma_{3}$. Continuing analytically this solution along the loop $\beta$, we arrive at another branch of the same solution near $u^{0}$. This new branch is specified, according to Theorem 1.3, by some new monodromy matrices $M_{1}^{\beta}, M_{2}^{\beta}$ and $M_{3}^{\beta}$, computed in the same basis $\gamma_{1}, \gamma_{2}, \gamma_{3}$. Our nearest goal is to compute these new matrices for any loop $\beta \in \pi_{1}\left(\mathbb{C}^{3} \backslash\{\right.$ diags $\left.\} ; u^{0}\right)$.

The fundamental group $\pi_{1}\left(\mathbb{C}^{3} \backslash\{\right.$ diags $\left.\} ; u^{0}\right)$ is isomorphic to the pure (or unpermuted) braid group, $P_{3}$ with three strings (see [Bir]); this is a subgroup of the full braid group $B_{3}$. The full braid group is isomorphic to the fundamental group of the same space where the permutations are allowed:
$$B_{3} \simeq \pi_{1}\left(\mathbb{C}^{3} \backslash\{\operatorname{diags}\} / S_{3} ; u^{0}\right),$$
$S_{3}$ being the symmetric group acting by permutations of the coordinates $\left(u_{1}, u_{2}, u_{3}\right)$. Any loop in $B_{3}$ has the form
$$\left(u_{1}(t), u_{2}(t), u_{3}(t)\right) \in \mathbb{C}^{3} \backslash\{\operatorname{diags}\}, \quad 0 \leq t \leq 1,$$
with
$$u_{i}(0)=u_{i}^{0}, \quad u_{i}(1)=u_{p(i)}^{0},$$
where $p$ is a permutation of $\{1,2,3\}$. The elements of the subgroup $P_{3}$ of pure braids are specified by the condition $p=\mathrm{id}$.

To simplify the computations we extend the procedure of the analytic continuation to the full braid group
$$M_{1}, M_{2}, M_{3} \mapsto M_{1}^{\beta}, M_{2}^{\beta}, M_{3}^{\beta}, \quad \beta \in B_{3}=\pi_{1}\left(\mathbb{C}^{3} \backslash\{\operatorname{diags}\} / S_{3} ; u^{0}\right) .$$
For a generic braid $\beta \in B_{3}$, the new monodromy matrices describe the superposition of the analytic continuation and of the permutation
$$u_{i} \mapsto u_{p(i)}, \quad \mathcal{A}_{i} \mapsto \mathcal{A}_{p(i)} .$$
The braid group $B_{3}$ admits a presentation with generators $\beta_{1}$ and $\beta_{2}$ and the defining relation
$$\beta_{1} \beta_{2} \beta_{1}=\beta_{2} \beta_{1} \beta_{2} .$$
The generators $\beta_{1}$ and $\beta_{2}$ are shown in the figure 4.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/64ce0006-7367-4aae-9e25-7b8a1be4f808-23.jpg?height=259&width=1271&top_left_y=1181&top_left_x=532}
\captionsetup{labelformat=empty}
\caption{Fig.4. The generators of the braid group $B_{3}$.}
\end{figure}

Lemma 1.8. For the generators $\beta_{1}, \beta_{2}$ shown in the figure 4, the matrices $M_{i}^{\beta}$ have the following form:
$$\begin{array}{ll}
M_{1}^{\beta_{1}}=M_{2}, & M_{2}^{\beta_{1}}=M_{2} M_{1} M_{2}^{-1}, \quad M_{3}^{\beta_{1}}=M_{3}, \\
M_{1}^{\beta_{2}}=M_{1}, & M_{2}^{\beta_{2}}=M_{3}, \quad M_{3}^{\beta_{2}}=M_{3} M_{2} M_{3}^{-1} .
\end{array}$$
Proof. Changing the positions of the points $u_{1}$ and $u_{2}$ by the braid $\beta_{1}$, the basis of the loops will be deformed into the new basis $\gamma_{1}^{\prime}, \gamma_{2}^{\prime}, \gamma_{3}^{\prime}$ shown in the figure 5 .

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/64ce0006-7367-4aae-9e25-7b8a1be4f808-23.jpg?height=485&width=573&top_left_y=1951&top_left_x=819}
\captionsetup{labelformat=empty}
\caption{Fig.5. The new loops $\gamma_{i}^{\prime}$ obtained under the action of the braid $\beta_{1}$.}
\end{figure}

Thanks to the fact that we deal with isomonodromy deformations, the monodromy matrices $M_{i}^{\prime}$ of the system (1.1) with respect to the new basis $\gamma_{1}^{\prime}, \gamma_{2}^{\prime}, \gamma_{3}^{\prime}$ are the same $M_{i}$, up to the reordering:
$$M_{1}^{\prime}=M_{2}, \quad M_{2}^{\prime}=M_{1}, \quad M_{3}^{\prime}=M_{3} .$$
We want to compute the monodromy matrices with respect to the old basis $\gamma_{1}, \gamma_{2}, \gamma_{3}$. To this aim we notice the following obvious relation in the fundamental group:
$$\gamma_{1}=\gamma_{1}^{\prime}, \quad \gamma_{2}=\left(\gamma_{1}^{\prime}\right)^{-1} \gamma_{2}^{\prime} \gamma_{1}^{\prime}, \quad \gamma_{3}=\gamma_{3}^{\prime} .$$
Using this relations and the (1.29), we immediately obtain the (1.27). Similarly the deformation of the basis of the fundamental group corresponding to the braid $\beta_{2}$ is shown in the figure 6.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/64ce0006-7367-4aae-9e25-7b8a1be4f808-24.jpg?height=483&width=473&top_left_y=867&top_left_x=864}
\captionsetup{labelformat=empty}
\caption{Fig.6. The new loops $\gamma_{i}^{\prime}$ obtained under the action of the braid $\beta_{2}$.}
\end{figure}

Here we have the permutation
$$M_{1}^{\prime}=M_{1} \quad M_{2}^{\prime}=M_{3}^{\prime}, \quad M_{3}^{\prime}=M_{2},$$
and the relations in the fundamental group:
$$\gamma_{1}=\gamma_{1}^{\prime}, \quad \gamma_{2}=\gamma_{2}^{\prime}, \quad \gamma_{3}=\left(\gamma_{2}^{\prime}\right)^{-1} \gamma_{3}^{\prime} \gamma_{2}^{\prime} .$$
From this we obtain the (1.28) and the lemma is proved.

The action (1.27), (1.28) of the braid group on the triples of monodromy matrices commutes with the diagonal conjugation of them. As a consequence this action not only describes the structure of the analytic continuation of the solutions of the Schlesinger equations (1.14), but also of the reduced ones (1.17). Moreover, the class of the singular solutions is closed under this analytic continuation. In fact if some of the matrices $M_{i}$ is equal to 1 then for any $\beta$ there is a $j$ such that $M_{j}^{\beta}=\mathbf{1}$. As a consequence the following lemma holds true:

Lemma 1.9. The structure of the analytic continuation of the solutions of the PVI $\mu$ equation is determined by the action (1.27), (1.28) of the braid group on the triples of monodromy matrices.

Our next step is to rewrite the action (1.27), (1.28) of the braid group in the coordinates $\left(x_{1}, x_{2}, x_{3}\right)$ in the space of the monodromy data. This is given by the following

Lemma 1.10. In the coordinates $\left(x_{1}, x_{2}, x_{3}\right)$, the action (1.27), (1.28) of the braid group is given by the formulae:
$$\begin{aligned}
& \beta_{1}:\left(x_{1}, x_{2}, x_{3}\right) \mapsto\left(-x_{1}, x_{3}-x_{1} x_{2}, x_{2}\right), \\
& \beta_{2}:\left(x_{1}, x_{2}, x_{3}\right) \mapsto\left(x_{3},-x_{2}, x_{1}-x_{2} x_{3}\right) .
\end{aligned}$$
Proof. The above formulae are obtained by straightforward computations from (1.27), (1.28) by means of the parameterization of the monodromy matrices (1.20).

We can summarize the results of this section in the following:
Theorem 1.5. The structure of the analytic continuation of the solutions of the PVI $\mu$ equation is determined by the action (1.30) of the braid group on the triples $\left(x_{1}, x_{2}, x_{3}\right)$.

Remark 1.8. It is easy to see that the braid $\left(\beta_{1} \beta_{2}\right)^{3}$ acts trivially on the monodromy data. This braid is the generator of the center of $B_{3}$ (see [Bir]). The quotient
$$B_{3} / \text { center } \simeq P S L(2 ; \mathbb{Z})$$
coincides with the mapping class group of the complex plane with three punctures [Bir]. Also in the general case, the structure of analytic continuation of solutions of PVI equation is described by the following natural action $\rho \rightarrow \rho^{\beta}$ of the mapping class group on the representation space (see remark 1.4)
$$\rho^{\beta}(\gamma)=\rho\left(\beta_{\star}^{-1}(\gamma)\right)$$
where
$$\begin{gathered}
\gamma \in F_{3} \simeq \pi_{1}\left(\overline{\mathbb{C}} \backslash\left\{u_{1}, u_{2}, u_{3}, \infty\right\}, \infty\right), \\
\beta: \overline{\mathbb{C}} \backslash\left\{u_{1}, u_{2}, u_{3}, \infty\right\} \rightarrow \overline{\mathbb{C}} \backslash\left\{u_{1}, u_{2}, u_{3}, \infty\right\}, \quad \beta(\infty)=\infty
\end{gathered}$$
is a homeomorphism, and
$$\rho: F_{3} \rightarrow S L(2 ; \mathbb{C}) .$$
Our action (1.30) is obtained restricting (1.31) onto the subspace of representations of the form (1.7). The problem of selection of algebraic solutions of Painlevé VI (see below) with generic values of the parameters $\alpha, \beta, \gamma, \delta$ can be reduced to the classification of finite orbits of the action (1.31).

\subsection*{1.3. Monodromy data and algebraic solutions of the $\mathbf{P V I} \mu$ equation.}
1.3.1. A preliminary discussion on the algebraic solutions of the $\mathbf{P V I} \mu$ equation and their monodromy data. Here we state some necessary condition for the triples $\left(x_{1}, x_{2}, x_{3}\right)$ to generate the algebraic solutions.

Definition. A solution $y(x)$ is called algebraic if there exists a polynomial in two variables such that
$$F(x, y(x)) \equiv 0 .$$

If $y(x)$ is an algebraic solution then the correspondent solution $p(\mathbf{u}), q(\mathbf{u}), \mathbf{u}=$ $\left(u_{1}, u_{2}, u_{3}\right)$ of the reduced Schlesinger equations (1.17) is also algebraic. According to Theorem 1.1, the solutions of the reduced Schlesinger equations (1.17) can ramify only on the diagonals $u_{1}=u_{2}, u_{1}=u_{3}, u_{3}=u_{2}$. Analogously the ramification points of $y(x)$ are allowed to lie only at $0,1, \infty$.

We now characterize the monodromy data such that the correspondent solution of the $\mathrm{PVI} \mu$ equation is algebraic.

Lemma 1.11. A necessary and sufficient condition for a solution of PVIμ to be algebraic is that the correspondent monodromy matrices, defined modulo diagonal conjugations, have a finite orbit under the action of the braid group (1.27), (1.28).

Proof. By definition, any algebraic function has a finite number of branches. Allowing also the permutations (1.26), we still obtain a finite number of values for $M_{1}^{\beta}, M_{2}^{\beta}$ and $M_{3}^{\beta}$, $\beta \in B_{3}$ up to diagonal conjugations.