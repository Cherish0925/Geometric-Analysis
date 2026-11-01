---
retention_scope: session
part: 1
total_parts: 3
---

[Part 1/3 of: Integrable Background Geometries]

---
source_file: Integrable_Background_Geometries_cc827212df19.pdf
converter: mathpix
format: mmd
---

\title{
Integrable Background Geometries ${ }^{\star}$
}

\author{
David M.J. CALDERBANK \\ Department of Mathematical Sciences, University of Bath, Bath BA2 7AY, UK \\ E-mail: D.M.J.Calderbank@bath.ac.uk \\ URL: http://people.bath.ac.uk/dmjc20/
}

Received January 21, 2014, in final form March 18, 2014; Published online March 28, 2014
http://dx.doi.org/10.3842/SIGMA.2014.034

\begin{abstract}
This work has its origins in an attempt to describe systematically the integrable geometries and gauge theories in dimensions one to four related to twistor theory. In each such dimension, there is a nondegenerate integrable geometric structure, governed by a nonlinear integrable differential equation, and each solution of this equation determines a background geometry on which, for any Lie group $G$, an integrable gauge theory is defined. In four dimensions, the geometry is selfdual conformal geometry and the gauge theory is selfdual Yang-Mills theory, while the lower-dimensional structures are nondegenerate (i.e., nonnull) reductions of this. Any solution of the gauge theory on a $k$-dimensional geometry, such that the gauge group $H$ acts transitively on an $\ell$-manifold, determines a $(k+\ell)$-dimensional geometry $(k+\ell \leqslant 4)$ fibering over the $k$-dimensional geometry with $H$ as a structure group. In the case of an $\ell$-dimensional group $H$ acting on itself by the regular representation, all $(k+\ell)$-dimensional geometries with symmetry group $H$ are locally obtained in this way. This framework unifies and extends known results about dimensional reductions of selfdual conformal geometry and the selfdual Yang-Mills equation, and provides a rich supply of constructive methods. In one dimension, generalized Nahm equations provide a uniform description of four pole isomonodromic deformation problems, and may be related to the SU( $\infty$ ) Toda and dKP equations via a hodograph transformation. In two dimensions, the $\operatorname{Diff}\left(S^{1}\right)$ Hitchin equation is shown to be equivalent to the hyperCR Einstein-Weyl equation, while the $\operatorname{SDiff}\left(\Sigma^{2}\right)$ Hitchin equation leads to a Euclidean analogue of Plebanski's heavenly equations. In three and four dimensions, the constructions of this paper help to organize the huge range of examples of Einstein-Weyl and selfdual spaces in the literature, as well as providing some new ones. The nondegenerate reductions have a long ancestry. More recently, degenerate or null reductions have attracted increased interest. Two of these reductions and their gauge theories (arguably, the two most significant) are also described.
\end{abstract}

Key words: selfduality; gauge theory; twistor theory; integrable systems
2010 Mathematics Subject Classification: 53A30; 32L25; 37K25; 37K65; 53B35; 53C25; 58J70; 70S15; 83C20; 83C80

\section*{1 Introduction}

\section*{Background}

This paper concerns differential geometry in dimensions one to four, and (primarily) four kinds of geometric structure, one in each dimension, governed by four nonlinear integrable differential equations. Associated to each manifold carrying one of these geometric structures, and to each Lie group, is an integrable gauge theory, generalizing a well-known gauge theory on flat space: the selfdual Yang-Mills equation on $\mathbb{R}^{4}$ or $\mathbb{R}^{2,2}$ and the gauge field equations arising as reductions by a (nondegenerate) group of translations to lower-dimensional flat spaces. Specifically, reduction by a single non-null translation gives the Bogomolny equation for monopoles on $\mathbb{R}^{3}$,

\footnotetext{
*This paper is a contribution to the Special Issue on Progress in Twistor Theory. The full collection is available at http://www.emis.de/journals/SIGMA/twistors.html
}
or its Lorentzian analogue on $\mathbb{R}^{2,1}$ [3, 59]. Reduction by two such translations yields the Hitchin equation for Higgs pairs on a Riemann surface, harmonic maps from a Riemann surface to a Lie group, or the principal chiral model on a two-dimensional space-time [30, 59]. Reduction by three non-null translations leads to the Nahm equation [44].

In addition to the physical motivation, the selfdual Yang-Mills equation has attracted interest because of its good integrability properties, which are inherited by the Bogomolny, Hitchin and Nahm equations, and their analogues. Further integrable systems may be obtained by reducing the selfdual Yang-Mills equation by other groups of conformal transformations of $\mathbb{R}^{4}$ or $\mathbb{R}^{2,2}$, and many such reductions have been investigated [41]. For example, hyperbolic monopoles arise from the reduction to three dimensions by a rotation, the Ernst equation is a reduction to two dimensions by a translation and rotation, while reductions to one dimension may be interpreted as isomonodromic deformation problems with four poles, governed (in the generic case) by the Schlesinger equation [31, 41, 43].

Twistor theory gives one explanation for this integrability: there is a Ward correspondence (see [5]) between solutions of the selfdual Yang-Mills equation on flat space and holomorphic vector bundles on (suitable open subsets of) $\mathbb{C P}^{3}$. This suggests that the selfdual Yang-Mills equation will continue to be integrable on other spaces $M$ so long as there is still a Ward correspondence between solutions and holomorphic vector bundles on some complex 3-manifold $Z$, the twistor space of $M$. Such curved twistor spaces $Z$ were introduced by Penrose [49] to study selfdual vacuum metrics. (Note that in Euclidean signature, selfdual Ricci-flat metrics are locally hyperkähler.)

Deep relationships between gauge field equations and selfdual vacuum metrics have been observed in a number of places. In [62], Ward considered gauge theories on $\mathbb{R}^{4-\ell}$ with the gauge group being a transitive group of diffeomorphisms of an $\ell$-manifold $\Sigma^{\ell}$. He focused on the group of diffeomorphisms preserving a fixed volume form on $\Sigma^{\ell}$ and observed that gauge fields then give rise to selfdual vacuum metrics on $\mathbb{R}^{4-\ell} \times \Sigma^{\ell}$. When $\ell=1$, the group of volume preserving diffeomorphisms of a circle or a line is U(1) or $\mathbb{R}$ acting by translation, so the monopoles are Abelian, and Ward's construction reduces to the Gibbons-Hawking Ansatz [24]. For $\ell=2$, finite-dimensional subgroups of $\operatorname{SDiff}\left(\Sigma^{2}\right)$ yield other interesting constructions of selfdual vacuum metrics [19], while $\ell=3$ gives the Ashtekar-Jacobson-Smolin description of selfdual vacuum metrics in terms of the Nahm equation [2]. One can also view the (closely related) Mason-Newman formulation [40] as the case $\ell=4$.

In Ward's construction, gauge fields on lower-dimensional flat spaces give rise to curved 4-manifolds. On the other hand, the example of hyperbolic monopoles shows that the lower-dimensional spaces can also be curved.

One of the goals of this paper is to place these miscellaneous results and observations in a geometric framework which simultaneously unifies and generalizes them. Selfdual vacuum metrics do not provide the right setting for this. For example, the natural generalization of the Gibbons-Hawking Ansatz to Abelian monopoles on hyperbolic space is LeBrun's hyperbolic Ansatz for scalar-flat Kähler metrics [39], and even on $\mathbb{R}^{4-\ell}$, one finds that without the volume-preserving condition, Ward's construction leads to hypercomplex, rather than hyperkähler, structures - see Hitchin [33] and Joyce [37] (or Dunajski [17]) for the analogue of the Ashtekar-Jacobson-Smolin and Mason-Newman description respectively.

In order to incorporate these constructions, it is essential to take into account a second basic feature of the selfdual Yang-Mills equation, in addition to integrability: conformal invariance. The selfdual Yang-Mills equation makes sense on any oriented conformal 4-manifold $M$, and the purely conformal part of Penrose's nonlinear graviton shows that there is a curved twistor space $Z$ as long as the conformal structure on $M$ is selfdual [4, 49].

The thesis of this paper is that reductions of selfdual conformal geometry to lower dimensions provide "integrable background geometries" on which curved versions of the Bogomolny, Hitchin
and Nahm equations (with good integrability properties) can be defined. This thesis can be illustrated by the three-dimensional case: the Jones-Tod correspondence [36] shows that the reduction of a selfdual conformal structure to three dimensions is an Einstein-Weyl structure, and selfdual Yang-Mills fields reduce to generalized monopoles on such Einstein-Weyl spaces, placing Euclidean and hyperbolic monopoles in a common framework. Selfdual spaces with symmetry over a given Einstein-Weyl space are built out of Abelian monopoles, and this provides many constructions (generalizing the Gibbons-Hawking and hyperbolic Ansätze) of hyperkähler, scalarflat Kähler and selfdual Einstein metrics, and also of hypercomplex structures [10, 22, 29, 39].

The role of gauge fields and Abelian monopoles in Ward's construction and the Jones-Tod construction respectively suggests an underlying principle relating gauge field equations and constructions of selfdual spaces. This is amplified by the following two generalizations of the Jones-Tod construction.

First, in [8], the Jones-Tod construction and Ward's construction on $\mathbb{R}^{3}$ were simultaneously generalized by considering the Einstein-Weyl Bogomolny equation with the gauge group acting transitively by diffeomorphisms on a circle or a line. The volume preserving case gives the usual Jones-Tod correspondence between selfdual spaces with symmetry and Abelian monopoles on Einstein-Weyl spaces, but more general gauge groups lead to new constructions of selfdual conformal structures and metrics, including, in special cases, hyperkähler and selfdual Einstein metrics.

Second, note that the Jones-Tod construction gives rise to a procedure for constructing a new selfdual space from an invariant selfdual Maxwell field on a given selfdual space with one-dimensional symmetry group: the selfdual Maxwell field descends to an Abelian monopole on the quotient Einstein-Weyl space, out of which a new selfdual space may be built. This was generalized, by Maszczyk, Mason and Woodhouse [43], to any freely acting symmetry group, using a construction they call the "switch map" [41]: given a selfdual space with freely acting group of conformal transformations $H$, and an invariant selfdual Yang-Mills connection on a bundle $P$ with a gauge group $G$ of the same dimension as $H$, the quotient of $P$ by $H$ is another selfdual space, with symmetry group $G$. Hence, for example, $T^{3}$-invariant SU(2) Yang-Mills fields on $\mathbb{R}^{4}$ give rise to selfdual conformal structures with SU(2) symmetry, such as the scalar-flat Kähler, hypercomplex and selfdual Einstein metrics of [14, 31, 33, 47, 55].

\section*{Overview}

Ward's construction, the (generalized) Jones-Tod correspondence, and the switch map all point to the following framework for dimensional reduction of selfdual conformal geometry and the selfdual Yang-Mills equation.
\begin{itemize}
\item[(i)] There are background geometries in each dimension less than four obtained by dimensional reduction of the selfduality condition for conformal structures.
\item[(ii)] The nonlinear differential equations defining these background geometries have the surprising feature that they do not depend on the symmetry group that one reduces by. Therefore, including selfdual conformal geometry, there are only four kinds of (nondegenerate) background geometry.
\item[(iii)] Instead, the symmetry group enters as a gauge group for a gauge theory defined on the background geometry, and the gauge field equation is the dimensional reduction of the selfdual Yang-Mills equation. Hence the gauge field equations play a remarkable dual role: solutions give rise both to selfdual conformal 4-manifolds and also to selfdual Yang-Mills fields on such manifolds.
\end{itemize}

In this paper, the above framework is established and studied in full generality. Furthermore, the different geometries are related not just by symmetry reduction, but by a more general
form of dimensional reduction, of which Ward's construction and the generalized Jones-Tod construction are examples (cf. also [25]). Such constructions also relate the lower-dimensional geometries to each other. More precisely:
\begin{itemize}
\item[-] For $1 \leqslant k<k+\ell \leqslant 4,(k+\ell)$-dimensional geometries are obtained from a $k$-dimensional geometry by solving the gauge field equation on that background where the gauge group acts transitively by diffeomorphisms on an $\ell$-manifold.
\end{itemize}

In four dimensions, the gauge fields and background geometries are, of course, selfdual Yang-Mills fields on selfdual spaces, while in three dimensions, one obtains monopoles on Einstein-Weyl spaces. The one and two-dimensional stories are new, although these structures have been implicitly studied in many places, at least in special cases [28, 51] and the twistor theory of the two-dimensional geometry has been developed independently by Donaldson and Fine [66, 76]. I first describe briefly the two-dimensional geometries, in the form obtained by reduction from Euclidean signature. The two reductions from Kleinian signature $(2,2)$ are similar.

Given a complex line bundle $\mathcal{W}$ over a Riemann surface $N$ with a Hermitian metric on $\mathcal{W}^{*} \otimes T N$, the geometric structure is a triple consisting of a U(1)-connection $a$ on $\mathcal{W}^{*} \otimes T N$, a section $\psi$ of $\mathcal{W}^{*}$ and a section $\mathcal{C}$ of $\mathcal{W}^{*} \otimes \mathcal{W}^{*} \otimes T N$ satisfying the following equations:
$$\bar{\partial}^{a} \mathcal{C}=0, \quad \bar{\partial}^{a} \psi=-3 \mathcal{C} \bar{\psi}, \quad * F^{a}=|\psi|^{2}-2|\mathcal{C}|^{2} .$$
The flat geometry is obtained by setting $\mathcal{W}=T N$, with the trivial connection on $\mathcal{W}^{*} \otimes T N$ and $\mathcal{C}=\psi=0$. This is simply a Riemann surface with no additional structure. The general two-dimensional background geometry was found in joint work with Lionel Mason [9].

The gauge fields on this background, with gauge group $G$, are pairs $(A, \Phi)$ consisting of a $G$-connection $A$ and a section $\Phi$ of $\mathcal{W}^{*} \otimes \mathfrak{g}_{N}$, where $\mathfrak{g}_{N}$ is the associated Lie algebra bundle. These pairs satisfy the following equations:
$$F^{A}-[\Phi, \bar{\Phi}]=\psi \wedge \bar{\Phi}+\bar{\psi} \wedge \Phi, \quad \bar{\partial}^{a, A} \Phi=\mathcal{C} \bar{\Phi} .$$
On the flat geometry, where $\mathcal{C}=0=\psi$, these are the Hitchin equations for stable pairs, but in the general case, the equations are coupled to the background geometry.

In one dimension, the background geometry is governed by a symmetric traceless (3 × 3)-matrix $\mathcal{B}$ satisfying the Riccati equation $\mathcal{B}_{r}=2\left(\mathcal{B}^{2}\right)_{0}$, where $r$ is an affine coordinate and the subscript zero denotes the traceless part. More invariantly, $\mathcal{B}$ is a section of $T^{*} C \otimes \operatorname{Sym}_{0} \mathcal{E}$ where $\mathcal{E}$ is a rank 3 conformal vector bundle over a curve $C$, with $\wedge^{3} \mathcal{E}=(T C)^{3}$, and one fixes compatible connections on $\mathcal{E}$ and $T C$ to define the $r$-derivative $\mathcal{B}_{r}$.

The gauge fields on this background are sections $\Phi$ of $\mathcal{E}^{*} \otimes \mathfrak{g}_{C}$ (where $\mathfrak{g}_{C}$ is a Lie algebra bundle over $C$ ) satisfying the equation $\Phi_{r}-*[\Phi, \Phi]=\mathcal{B} \cdot \Phi$, where $*$ denotes the star operator on $\mathcal{E}$ and one fixes a $G$-connection to define $\Phi_{r}$. The flat geometry is the trivial solution $\mathcal{B}=0$, in which case this gauge field equation reduces to the Nahm equation.

There is one further important property of the Jones-Tod correspondence that continues to hold in the general framework: it is constructive, i.e., a selfdual conformal structure is explicitly determined by an Einstein-Weyl structure together with a monopole, and conversely. The correspondence between additional monopoles and selfdual Yang-Mills fields is equally explicit. The same remarks hold for the switch map and Ward's construction. I therefore present explicit formulae for the constructions of the paper.

For convenience of exposition, I will concentrate on the reductions from Euclidean signature and the notation will be adapted to this case. However, the non-null reductions from Kleinian signature $(2,2)$ are completely analogous, as are such reductions of complex geometries: I indicate throughout the nondegeneracy assumptions that need to be made, and any changes in notation that are needed. On the other hand, it remains an interesting open project to study the integrable background geometries arising from null reductions: only two such reductions are considered here.

\section*{User guide}

This is a long paper to read from start to finish, so I give a detailed guide to the sections, both to draw attention to the highlights and to enable the reader to dip into the paper more easily.

The general theory of the paper is developed in Sections 2, 4, 6 and 8. Section 2 concerns selfdual spaces with a freely acting symmetry group and presents the background geometry equations in dimensions 1-3. In each case the main result, Theorems 2.3, 2.6 or 2.9, identifies the selfduality condition on a conformal structure with the background geometry equations: in particular Theorem 2.9 is the Jones-Tod correspondence [36]. Section 4 deals with invariant selfdual Yang-Mills fields on selfdual spaces with a freely acting symmetry group. Here the gauge field equations on the background geometries are computed.

The main general theorems are in Sections 6 and 8, where the inverse constructions to Section 2 are established and generalized. Theorem 6.1 proves that selfdual spaces may be constructed from solutions to gauge field equations on $k$-dimensional background geometries where the gauge group acts transitively on a $(4-k)$-manifold: in the case of a group acting on itself by the regular representation, this theorem reconstructs the selfdual spaces with freely acting symmetry group of Section 2 - although, as mentioned already, in the general case, the group need not even be finite-dimensional.

Theorem 8.1 generalizes all this to gauge groups acting on $\ell$-manifolds, giving explicit constructions of $(k+\ell)$-dimensional background geometries from gauge fields on $k$-dimensional geometries for $k+\ell \leqslant 4$. Unfortunately, the calculations here are too complicated to present in full. However, I do provide explicit formulae: in examples arising in practice, it is usually not too hard to verify that the $(k+\ell)$-dimensional geometry satisfies the background equations, once one has a formula.

The relation between selfdual spaces, and the three-dimensional background geometries, Einstein-Weyl spaces, is a longstanding one, and as a consequence the latter have been extensively studied [8, 10, 11, 21, 22, 29, 36, 39, 55, 56, 60]. By contrast, the background geometries in one and two dimensions, Riccati spaces, and spinor-vortex spaces, although implicitly underlying previous work, have only been introduced and investigated relatively recently (see, e.g., [9, 66]). Assuming that one is not interested in zero-dimensional differential geometry (see Remark 7.9), then these geometries form the foundation for the more well-known higher-dimensional structures (using Theorems 6.1 and 8.1).

In Section 10, the geometry of Riccati spaces is described. Although there are only six Riccati spaces up to local isomorphism, they have a rather rich structure, which is most easily revealed in a complexified setting, since only three of the Riccati spaces arise as reductions from Euclidean signature. The six solutions correspond to the six types of quartic polynomial, i.e., the five types of configuration of four points on $\mathbb{C P}^{1}$ together with the zero polynomial. These types are denoted (I, II, III, D, N, 0), following the well-known application of this classification to Weyl tensors. It is easy to see that the gauge field equation on the trivial (0) Riccati space is the Nahm equation. One can also observe that the gauge field equations on the nontrivial Riccati spaces are equivalent to (strong) isomonodromy equations for a connection with four poles on $\mathbb{C P}^{1}$, the configuration of the poles corresponding to the type of Riccati space. This leads to a uniform Lax pair for these problems, which reduces to the usual Lax pair for the Nahm equation in the trivial case.

The theory of this paper would be very dry without examples and applications, so I intersperse the main development with interludes, which motivate or illustrate the theory, yet are, to varying degrees, self-contained. The first interlude, Section 3, relates the approach of Section 2 to other studies of selfdual Bianchi metrics [14, 15, 47, 53, 54, 55].

The second interlude, Section 5, provides a simple a priori explanation for the conformal invariance of Hitchin's selfduality equation on a Riemann surface [30] (and of course, reductions
from Kleinian signature also give conformally invariant equations: harmonic maps into a Lie group, and the principal chiral model). This demystifies this conformal invariance: it is, after all, a consequence of conformal invariance in four dimensions.

The third interlude, Section 7, is a unified treatment of various constructions (or at least interpretations) of hypercomplex and hyperkähler structures. My aim here is three-fold:
\begin{itemize}
\item[(i)] to provide geometrical descriptions of the well-known Mason-Newman [40], Ashtekar-Jacobson-Smolin [2], and Park-Ward [46, 62] constructions of hyperkähler metrics from lower-dimensional gauge fields;
\item[(ii)] to give, at the same time, hypercomplex generalizations, following [17, 26, 33, 37];
\item[(iii)] to prove that all hypercomplex and hyperkähler structures are locally obtained from any of these constructions, in a way that is manifestly compatible with any reality conditions, and that clarifies the extra choice that needs to be made to reduce a hypercomplex or hyperkähler structure to a solution of the relevant gauge field equation.
\end{itemize}

I hope that the overview provided here is useful, at least to the reader who is not familiar with the treatments in the physics literature. In addition this work answers - and extends to the hypercomplex case - a question of Ward [62], who conjectured that any hyperkähler metric could be obtained from Hitchin's selfduality equation, with gauge group $\operatorname{SDiff}\left(\Sigma^{2}\right)$. I also show how this description gives a Euclidean analogue of Plebanski's heavenly equations, which is well-adapted to the study of hyperkähler metrics on elliptic fibrations.

The fourth interlude, Section 9, is a two-part analysis of hyperCR Einstein-Weyl spaces, the three-dimensional analogue of hypercomplex structures. In the first part, following an approach of Tod [56], the hyperCR Einstein-Weyl equation is shown to be equivalent to the $\operatorname{Diff}\left(S^{1}\right)$ Hitchin equation (revealing a hidden SO(3) symmetry in the latter). This can be viewed as a three-dimensional version of the constructions of Section 7 although it is remarkable that the fibres are only one-dimensional, since such constructions are not sufficiently general in four dimensions. In the second part, Einstein-Weyl spaces admitting a dimensional reduction with geodesic one-dimensional fibres are studied. They are shown to be hyperCR, and the quotient spaces are trivial or spherical spinor-vortex geometries. Conversely, any shear-free geodesic congruence on a hyperCR Einstein-Weyl space defines a generalized dimensional reduction.

The final interlude again consists of two-parts. The first shows that hyperCR Einstein-Weyl spaces may also be constructed from the $\operatorname{Diff}\left(\Sigma^{2}\right)$ Nahm equations. In the second part, I present a proof that the well-known $\operatorname{SU}(\infty)$ Toda field equation $u_{x x}+u_{y y}+\left(e^{u}\right)_{z z}=0$ and the dKP equation $u_{y y}=\left(u_{t}-u u_{x}\right)_{x}$ are both equivalent to generalized Nahm equations, via a hodograph transformation (cf. [20] in the dKP case). Even these results are to a large extent self-contained, although the the work of Section 8 shows that the construction is a special case of the general theory, while Section 10 shows that the backgrounds for these generalized Nahm equations are the type (D) and (N) Riccati spaces respectively. To the best of my knowledge, all examples of hodograph solutions to the $\operatorname{SU}(\infty)$ Toda field equation or dKP equation arise in this way from explicit solutions of a generalized Nahm equation. I end the interlude by discussing these examples.

\section*{Addenda}

The majority of this paper was written in the period 1999-2001, and the present content is not substantially different from a January 2002 version which has been posted on my academic home page since that time. The intervening 12 years have seen many advances in the field (for instance, by Dunajski and his collaborators [67, 68, 69, 70, 71]), and I have collected a few of the most closely related papers as "Additional references" at the end of the bibliography.

Some of these works develop ideas from the 2002 version of this paper, or discover related ideas independently.

There has also been much work on null reductions and geometries, which were only touched upon in the original version of this paper. A major driving force has been the introduction of a global twistor theory of holomorphic discs by LeBrun and Mason [77, 78, 80, 82], both for Kleinian signature selfdual conformal structures and 2-dimensional projective structures. Dunajski and West [72, 73] established a relationship between these structures by considering selfdual conformal structures with a null conformal Killing vector field. As explained in [65], the natural context for their construction is the null reduction of selfdual conformal structures along a $\beta$-surface foliation. The quotient is a surface with a natural projective structure structure, and the gauge field equations are projectively invariant on this background geometry. In [81] the global Mason-LeBrun theories are related by this construction. More recently, similar methods have been applied in Einstein-Weyl geometry [79, 83].

One of the most intriguing recent developments has been the introduction, by Ferapontov and his coworkers, of the method of hydrodynamic reductions to analyse integrability. This was applied in [74] to study the central quadric Ansatz and its relation to the Painlevé equations. In doing so, they independently rediscovered equations equivalent to the $\operatorname{SDiff}\left(\Sigma^{2}\right)$ generalized Nahm equations on Riccati spaces. More recently, in [75], Ferapontov and Kruglikov construct a Weyl structure from the formal linearization of a second-order PDE in three dimensions, and show that it is Einstein-Weyl for all solutions if and only if the system is integrable. This and related conjectures for second-order PDEs in four dimensions suggest deep connections with the integrable background geometry concept.

For these reasons, the main (odd-numbered) sections have been updated with addenda which place the above works in the framework of this paper. Section 12 and Subsection 11.2 have also been updated to reflect the exciting new directions that are currently unfolding.

\section*{Notation}

In order to manipulate, in a tensorial way, the objects and structures entering into the equations and constructions of this paper, it will be convenient to employ the formalism of densities. If $V$ is a real $n$-dimensional vector space and $w$ any real number, then the oriented one-dimensional linear space $L^{w}=L_{V}^{w}$ carrying the representation $A \mapsto|\operatorname{det} A|^{w / n}$ of $\operatorname{GL}(V)$ is called the space of densities of weight $w$ or $w$-densities. It can be constructed canonically as the space of maps $\rho:\left(\wedge^{n} V\right) \backslash 0 \rightarrow \mathbb{R}$ such that $\rho(\lambda \omega)=|\lambda|^{-w / n} \rho(\omega)$ for all $\lambda \in \mathbb{R}^{\times}$and $\omega \in\left(\wedge^{n} V\right) \backslash 0$.

For a vector bundle $\mathcal{V} \rightarrow M$ this construction yields an oriented real line bundle $L_{\mathcal{V}}^{w}$, a density line bundle. If $\mathcal{V}$ is oriented and of rank $n$, then $L_{\mathcal{V}}^{-n}$ is canonically isomorphic to $\wedge^{n} \mathcal{V}$; indeed an orientation may be defined as an orientation form $* 1 \in \mathrm{C}^{\infty}\left(M, L_{\mathcal{V}}^{n} \wedge^{n} \mathcal{V}^{*}\right)$. (Here and elsewhere, when tensoring with a density line bundle, I shall often omit the tensor product sign.) More generally, the Hodge star operator is the isomorphism
$$*: L_{\mathcal{V}}^{w-k} \wedge^{k} \mathcal{V} \rightarrow L_{\mathcal{V}}^{w+n-k} \wedge^{n-k} \mathcal{V}^{*}$$
determined by the nondegenerate pairing $\wedge^{k} \mathcal{V}^{*} \otimes \wedge^{n-k} \mathcal{V}^{*} \rightarrow \wedge^{n} \mathcal{V}^{*} \cong L_{\mathcal{V}}^{-n}$.
A conformal structure on $\mathcal{V}$ is a nondegenerate symmetric bilinear form on $\mathcal{V}$ with values in $L_{\mathcal{V}}^{2}$, or equivalently a metric on $L_{\mathcal{V}}^{-1} \mathcal{V}$. The conformal inner product of sections $X, Y$ is $\langle X, Y\rangle \in \mathrm{C}^{\infty}\left(M, L_{\mathcal{V}}^{2}\right)$ and the conformal structure itself may be viewed as a section $\mathrm{c} \in$ $\mathrm{C}^{\infty}\left(M, L_{\mathcal{V}}^{2} S^{2} \mathcal{V}^{*}\right)$. I shall make free use of the isomorphism between $L_{\mathcal{V}}^{w-k} \wedge^{k} \mathcal{V}$ and $L_{\mathcal{V}}^{w+k} \wedge^{k} \mathcal{V}^{*}$ given by a conformal structure.

When $\mathcal{V}$ is the tangent bundle of $M, L_{M}^{w}=L_{T M}^{w}$ is called the bundle of $w$-densities of $M$, denoted $L^{w}$ when $M$ is understood. The line bundles $L^{w}$ are trivializable and a nonvanishing
(usually positive) section $\mu$ of $L=L^{1}$ will be called a length scale or gauge. I shall also say that tensors in $L^{w} \otimes(T M)^{j} \otimes\left(T^{*} M\right)^{k}$ have weight $w+j-k$.

A Weyl derivative is a covariant derivative $D$ on $L$. It induces covariant derivatives on $L^{w}$ for all $w$. If $M$ is conformal, i.e., there is a conformal structure c on $T M$, then any Weyl derivative induces (via the Koszul formula) a Weyl connection: a torsion-free connection $D$ on $T M$ with $D \mathrm{c}=0$. Compatible Riemannian metrics $g$ correspond to length scales $\mu$, and the Weyl connection induced by the Weyl derivative preserving $\mu$ is, of course, the Levi-Civita connection of $g=\mu^{-2} \mathrm{c}$.

The curvature $R^{D}$ of a Weyl connection $D$, as a $\mathfrak{c o}(T M)$-valued 2-form, decomposes as
$$R_{X, Y}^{D}=W_{X, Y}-\llbracket r^{D}(X), Y \rrbracket+\llbracket r^{D}(Y), X \rrbracket .$$
Here $W$ is the Weyl curvature of the conformal structure, an so( $T M$ )-valued 2-form independent of the choice of $D$, and $r^{D}$ is a covector valued 1-form, the (normalized) Ricci curvature of $D$. For a 1-form $\gamma$ and tangent vector $X, \llbracket \gamma, X \rrbracket=\gamma(X) \operatorname{id}+\gamma \Delta X$, where $(\gamma \Delta X)(Y)=\gamma(Y) X-$ $\langle X, Y\rangle \gamma$. This bracket is part of a Lie algebra structure on $T M \oplus \mathfrak{c o}(T M) \oplus T^{*} M$ and the same notation will be used for the commutator bracket in $\mathfrak{c o}(T M)$.

The normalized Ricci curvature decomposes into a symmetric traceless part $r_{0}^{D}$, a scalar part scal ${ }^{D}$ (the scalar curvature) and a skew part, which is just a multiple of the curvature of $D$ on $L$ called the Faraday curvature $F^{D}$. In practice a Weyl derivative is described by its connection 1-form $\omega$ relative to a length scale: $\omega$ is called the Weyl 1-form, and $F^{D}=\mathrm{d} \omega$. If $F^{D}=0$ then $D$ is said to be closed. It follows that there are local length scales $\mu$ with $D \mu=0$. If such a length scale exists globally then $D$ is said to be exact.

The above constructions can also be carried out locally on complex manifolds, except that $L^{1}$ is now a choice of local $n$th root of $\wedge^{n} T M$.

Although confusion with the index $i$ is unlikely, as a courtesy to the reader, I denote the (chosen) square root of -1 by $\boldsymbol{i}$.

\section*{Twistors and Lax pairs}

Several of the results in this paper were motivated by twistor or integrable systems methods: in particular the idea of generalized dimensional reduction arises naturally when one considers holomorphic foliations of twistor spaces. However, I have deliberately suppressed discussion of twistor spaces and Lax pairs, for at least two reasons: first, to make the paper accessible to the reader not familiar with these ideas; second, because I believe it is a useful to present all calculations and formulae in purely differential geometric terms - it is often impossible to carry out twistor constructions in practice. An unfortunate consequence is that some of the results and formulae appear miraculous: the twistor point of view provides a quick way to see why such results are true, while the Lax pair formalism provides one way to carry out more detailed calculations.

\section*{2 Selfdual spaces and the background geometries}

On a conformal 4 -manifold, the Hodge star operator is an involution on 2 -forms, so there is a decomposition $\wedge^{2} T^{*} M=\wedge_{+}^{2} T^{*} M \oplus \wedge_{-}^{2} T^{*} M$, and the eigenspaces $\wedge_{ \pm}^{2} T^{*} M$ are called the selfdual and antiselfdual 2-forms. This induces a similar decomposition $\operatorname{so}(T M)=\operatorname{so}_{+}(T M) \oplus$ so_( $T M$ ) of the skew endomorphisms of $T M$. The Weyl curvature $W$ splits as a sum of selfdual and antiselfdual 2-forms $W^{ \pm}$with values in so( $T M$ ): in fact $W^{+}$is so ${ }_{+}(T M)$-valued and $W^{-}$is so_( $T M$ )-valued (essentially because $W$ is traceless).

A selfdual space is a conformal 4-manifold with selfdual Weyl curvature, i.e., $W^{-}=0$.

In [37], Joyce studied selfdual spaces with a surface-orthogonal action of the torus $T^{2}$ by conformal transformations, and found new explicit selfdual conformal metrics on connected sums of complex projective planes. The key idea in his approach is the use of conformal connections with torsion, and the following observation.

Lemma 2.1 (see Joyce [37]). Let $(M, \mathrm{c})$ be an oriented conformal 4-manifold and $\mathcal{D}$ a conformal connection (i.e., $\mathcal{D} \mathrm{c}=0$, but $\mathcal{D}$ may have torsion). Suppose that the antiselfdual part of the torsion of $\mathcal{D}$ is tracelike. Then $(M, \mathrm{c})$ is selfdual if and only if the Weyl part of the curvature of $\mathcal{D}$ is selfdual.

When the torsion is selfdual and traceless, this lemma follows easily, since $\mathcal{D}$ then differs from a Weyl connection by an $\operatorname{so}_{+}(T M)$-valued 1-form, so that the so- $(T M)$-valued part of the curvature of $\mathcal{D}$ agrees with that of the Weyl connection. The general case is a consequence of the fact that the trace parts of the torsion (which are 1-forms) cannot contribute to the Weyl part of the curvature.

I shall refer to this result as Joyce's lemma: although simple, and perhaps previously known, its application by Joyce [37] was one of the main motivations for the present work. Indeed, for a conformal manifold with a surface-orthogonal $T^{2}$-action, Joyce constructed, on the open set where the torus acts freely, a conformal connection with torsion, and hence separated the selfduality equation for the conformal structure into a nonlinear equation for a quotient geometry and a linear equation defined on this background. He then showed that the quotient geometry in this case is the hyperbolic plane, and superposed known solutions of the linear equation to find new explicit metrics.

In this section, Joyce's lemma will be applied to selfdual spaces with any freely acting group of conformal transformations, and a large class of dimensional reductions of the selfduality equation will be obtained. The restriction to freely acting groups of symmetries will also be relaxed later, leading to a generalized version of dimensional reduction.

Let $M$ be a conformal manifold with a free proper action of a group $H$, so that $M$ is a principal $H$-bundle over the orbit space $Q=M / H$. The generators of the action form a Lie algebra $\mathfrak{h}$ of vector fields on $M$ and pointwise evaluation defines an isomorphism $M \times \mathfrak{h} \rightarrow V M$, where $V M$ is the vertical bundle of $M \rightarrow Q$. Now suppose that $H$ acts conformally with nondegenerate orbits. Then $Q$ is a conformal manifold and the horizontal distribution $V M^{\perp} \leqslant T M$ defines a principal $H$-connection $\alpha$ on $\pi: M \rightarrow Q$; furthermore, $V M$ is isomorphic to the pullback of a conformal vector bundle $\mathcal{V} \rightarrow Q$ with $L_{\mathcal{V}}^{1}=L_{Q}^{1}$. Although $M \times \mathfrak{h}$ and $\pi^{*} \mathcal{V}$ are both isomorphic to $V M$, it will be crucial in the following to distinguish between them, since the trivialization of $V M$ given by the $H$-action is not, in general, compatible with the conformal structure. However, the isomorphism $\pi^{*} \mathcal{V} \rightarrow M \times \mathfrak{h}$ is $H$-equivariant, so it may be viewed as a bundle isomorphism $\varphi: \mathcal{V} \rightarrow \mathfrak{h}_{Q}$ over $Q$, where $\mathfrak{h}_{Q}=M \times_{H}$ h. To summarize, the conformal geometry of $M$ is encoded by:
\begin{itemize}
\item[-] a conformal structure on $Q$;
\item[-] a conformal vector bundle $\mathcal{V} \rightarrow Q$ with $L_{\mathcal{V}}^{1}=L_{Q}^{1}$;
\item[-] a principal $H$-connection $\alpha$ on $M \rightarrow Q$;
\item[-] a bundle isomorphism $\varphi: \mathcal{V} \rightarrow \mathfrak{h}_{Q}$ over $Q$.
\end{itemize}
The data $(\alpha, \varphi)$ identify the tangent bundle $T M$ with the pullback of $\mathcal{V} \oplus T Q$ : sections of $\mathcal{V}$ or $T Q$ will be denoted $U, V, W$ or $X, Y, Z$ respectively, and identified with invariant vector fields on $M$.

The curvature of the principal connection $\alpha$ on $\pi: M \rightarrow Q$ is an $\mathfrak{h}_{Q}$-valued 2-form $F^{\alpha}$, given by minus the Frobenius curvature of the horizontal distribution: $F^{\alpha}(X, Y)=-\varphi([X, Y])$, where $\varphi$ extended by zero from $\mathcal{V}$ to $\mathcal{V} \oplus T Q$.

Choose a conformal connection $D$ on $\mathcal{V}$ over $Q$. This induces a Weyl derivative on $L_{\mathcal{V}}^{1}=L_{Q}^{1}$, hence a torsion-free conformal connection on $T Q$ and a direct sum connection on $\mathcal{V} \oplus T Q$. These conformal connections will be denoted by $D$, as will the pullback connection on $T M=$ $\pi^{*}(\mathcal{V} \oplus T Q)$, which is conformal, but not torsion-free in general: the fibres of $\pi: M \rightarrow Q$ need not be umbilic unless $Q$ is three-dimensional, the nonlinear connection on $M \rightarrow Q$ need not be flat unless $Q$ is one-dimensional, and the sections of $\mathcal{V}$ parallel along the fibres of $\pi$ will have nontrivial Lie brackets unless $\mathfrak{h}$ is Abelian.

In order to apply Joyce's lemma, the torsion needs to be reduced. To do this, introduce $\psi: \wedge^{2} T Q \rightarrow \mathcal{V}$ and $\mathcal{C}: S_{0}^{2} \mathcal{V} \rightarrow T Q$, and define $\mathcal{D}=D+\widehat{\mathcal{C}}+\widehat{\psi}$, where $\widehat{\mathcal{C}}$ and $\widehat{\psi}$ are the sections of $T^{*} M \otimes \operatorname{so}(T M)$ given by
$$\begin{aligned}
& \widehat{\mathcal{C}}_{U+X}(V+Y)=\mathcal{C}(U, V)-\langle\mathcal{C}(U, \cdot), Y\rangle, \\
& 2 \widehat{\psi}_{U+X}(V+Y)=\langle\psi(X, \cdot), V\rangle+\langle\psi(Y, \cdot), U\rangle-\psi(X, Y) .
\end{aligned}$$
The idea is that $\psi$ will compensate for the curvature of the horizontal distribution, while $\mathcal{C}$ will offset the traceless second fundamental form of the fibres. It will then be possible to make the torsion selfdual by the choice of $D$.

The torsion $T^{\mathcal{D}}$ of this modified conformal connection may be computed by applying it to invariant vector fields, as long as one is careful that the Lie bracket on invariant vertical vector fields is minus the Lie bracket on the Lie algebra $\mathfrak{h}$ of generators of the action, hence minus the bracket on the associated Lie algebra bundle $\mathfrak{h}_{Q}$ over $Q$
$$\begin{aligned}
& T^{\mathcal{D}}(U, V)=\varphi^{-1}[\varphi(U), \varphi(V)]_{\mathfrak{h}}, \\
& T^{\mathcal{D}}(U, X)=\varphi^{-1} D_{X}^{\alpha} \varphi(U)-\langle\mathcal{C}(U), X\rangle, \\
& T^{\mathcal{D}}(X, Y)=\varphi^{-1} F^{\alpha}(X, Y)-\psi(X, Y) .
\end{aligned}$$
Here $D^{\alpha}$ denotes the connection on $\pi^{*}\left(\mathcal{V} \otimes \mathfrak{h}_{Q}\right)$ induced by $D$ and $\alpha$. Note that the torsion is vertical-valued.

The computation of the curvature is a little more complicated. First of all the curvatures of $\mathcal{D}$ and $D$ (on $T M$ ) are related by
$$R_{U+X, V+Y}^{\mathcal{D}}=R_{U+X, V+Y}^{D}+\mathrm{d}^{D}(\widehat{\mathcal{C}}+\widehat{\psi})_{U+X, V+Y}+\llbracket(\widehat{\mathcal{C}}+\widehat{\psi})_{U+X},(\widehat{\mathcal{C}}+\widehat{\psi})_{V+Y} \rrbracket .$$
The second term is the twisted exterior derivative of $\mathrm{so}(T M)$-valued 1-forms and must be handled carefully, since $D$ has torsion. Relating this to the torsion of $\mathcal{D}$ gives
$$\begin{aligned}
\mathrm{d}^{D}(\widehat{\mathcal{C}}+\widehat{\psi})_{U+X, V+Y}= & D_{U+X}(\widehat{\mathcal{C}}+\widehat{\psi})_{V+Y}-D_{V+Y}(\widehat{\mathcal{C}}+\widehat{\psi})_{U+X} \\
& +(\widehat{\mathcal{C}}+\widehat{\psi})_{T^{\mathcal{D}}}(U+X, V+Y)+(\widehat{\mathcal{C}}+\widehat{\psi})_{\psi(X, Y)}+(\widehat{\mathcal{C}}+\widehat{\psi})_{\langle\mathcal{C}(U), Y\rangle-\langle\mathcal{C}(V), X)} .
\end{aligned}$$
Notice that the derivatives in vertical directions are zero, since the connection is a pullback connection and $\widehat{\mathcal{C}}, \widehat{\psi}$ are invariant. Also, $R^{D}$ is horizontal. Hence putting everything together leads to the following formula for the "torsion-adjusted" curvature of $\mathcal{D}$
$$\begin{aligned}
R_{U+X, V+Y}^{\mathcal{D}, t a}:= & R_{U+X, V+Y}^{D}-(\widehat{\mathcal{C}}+\widehat{\psi})_{T^{\mathcal{D}}(U+X, V+Y)} \\
= & R_{X, Y}^{D}+D_{X} \widehat{\mathcal{C}}_{V}-D_{Y} \widehat{\mathcal{C}}_{U}+D_{X} \widehat{\psi}_{V}-D_{Y} \widehat{\psi}_{U} \\
& +\widehat{\mathcal{C}}_{\psi(X, Y)}+\widehat{\psi}_{\langle\mathcal{C}(U), Y\rangle}-\widehat{\psi}_{\langle\mathcal{C}(V), X\rangle}+\llbracket \widehat{\psi}_{U+X}, \widehat{\mathcal{C}}_{V} \rrbracket+\llbracket \widehat{\mathcal{C}}_{U}, \widehat{\psi}_{V+Y} \rrbracket \\
& +\widehat{\mathcal{C}}_{\langle\mathcal{C}(U), Y\rangle}-\widehat{\mathcal{C}}_{\langle\mathcal{C}(V), X\rangle}+\llbracket \widehat{\mathcal{C}}_{U}, \widehat{\mathcal{C}}_{V} \rrbracket+\widehat{\psi}_{\psi(X, Y)}+\llbracket \widehat{\psi}_{U+X}, \widehat{\psi}_{V+Y} \rrbracket .
\end{aligned}$$
Now suppose that $T^{\mathcal{D}}$ is selfdual. Then, by Joyce's lemma, the Weyl curvature $W$ of $M$ is selfdual if and only if the Weyl part of this formula is selfdual. This condition is a nonlinear
differential equation on $Q$ defining a reduced background geometry. A key feature of the formula is that the right hand side is manifestly independent of $(\alpha, \varphi)$ and so the group structure of $H$ decouples from the reduced background geometry.

The details depend on the dimension; in particular, ensuring that the torsion is selfdual constrains $D$. In the following subsections, I will explain these constraints and obtain the background geometries explicitly. For later use I will also introduce individual notations for the geometries in each dimension. As far as possible, the notation will be chosen to be consistent with existing usage. The case of a four-dimensional group acting on itself is left as an exercise: a field $\mathcal{Y} \in \wedge_{-}^{2} \mathcal{V}^{*} \otimes \mathcal{V}$ is needed here to make the torsion selfdual; see Remark 7.9.

\subsection*{2.1 Reduction to one dimension}

In this case $Q$ is a oriented curve, with weightless unit tangent $\xi$, and $\psi=0$. Write $\mathcal{C}(U, V)=$ $\langle\mathcal{B}(U), V\rangle \xi$, so that $\mathcal{B}$ is a symmetric traceless endomorphism of weight -1. I will denote the curve $Q$ by $C$ and the bundle $\mathcal{V}$ by $\mathcal{E}$. Thus $\mathcal{E}$ is a rank 3 conformal vector bundle over $C$ with $L_{\mathcal{E}}^{1}=L_{C}^{1}=T C$, the last identification being given by $\xi$. The Hodge star operator is an isomorphism between $\wedge^{2} \mathcal{E}$ and $T C \otimes \mathcal{E}=L^{1} \mathcal{E}$.

The two components of the torsion of $\mathcal{D}$ are given by
$$T^{\mathcal{D}}(U, V)=\varphi^{-1}[\varphi(U), \varphi(V)]_{\mathfrak{h}}, \quad T^{\mathcal{D}}(U, \xi)=\varphi^{-1} D_{\xi}^{\alpha} \varphi(U)-\mathcal{B}(U) .$$
This will be selfdual if and only if
$$\varphi^{-1}\left(D_{\xi}^{\alpha} \varphi-*[\varphi, \varphi]_{\mathfrak{h}}\right)=\mathcal{B} .$$
Conformal connections $D$ on $\mathcal{E}$ form an affine space modelled on $T^{*} C \otimes \mathfrak{c o}(\mathcal{E})$. Hence $D$ can be chosen uniquely so that the left hand side is symmetric and traceless and this in turn defines $\mathcal{B}$.

The two components of the torsion-adjusted curvature of $\mathcal{D}$ are
$$R_{U, V}^{\mathcal{D}, t a}=\llbracket \widehat{\mathcal{B}}_{U}, \widehat{\mathcal{B}}_{V} \rrbracket, \quad R_{U, \xi}^{\mathcal{D}, t a}=-D_{\xi} \widehat{\mathcal{B}}_{U}+\widehat{\mathcal{B}}_{\mathcal{B}(U)} .$$
A straightforward calculation shows that the Weyl part is selfdual if and only if $D_{\xi} \mathcal{B}=2\left(\mathcal{B}^{2}\right)_{0}$, where the subscript zero denotes the traceless part. Since $D$ is flat, this is really just a Riccati equation for a 3 × 3 symmetric traceless matrix. On the other hand, the orientation of $C$ is not needed if $\mathcal{B}$ is viewed as an endomorphism-valued 1-form on $C$.
Definition 2.2. Suppose that $\mathcal{E}$ is a rank 3 conformal vector bundle over a curve $C$ with $L_{\mathcal{E}}^{1}=L_{C}^{1}$. Equip $\mathcal{E}$ with a conformal connection $D$ and a section $\mathcal{B}$ of $T^{*} C \otimes \operatorname{Sym}_{0} \mathcal{E}$. Then $(C, \mathcal{E})$ is said to be a Riccati space if $(D, \mathcal{B})$ satisfy the equation
$$D \mathcal{B}=2\left(\mathcal{B}^{2}\right)_{0} .$$
Equivalently, with respect to a conformal trivialization of $\mathcal{E}$, the connection $D$ is given by a section ( $a, \Theta$ ) of $T^{*} C \otimes \mathfrak{c o}(\mathcal{E})=T^{*} C \oplus\left(T^{*} C \otimes \operatorname{so}(\mathcal{E})\right)$ and
$$\dot{\mathcal{B}}-a \mathcal{B}+\llbracket \Theta, \mathcal{B} \rrbracket=2\left(\mathcal{B}^{2}\right)_{0},$$
where the dot denotes differentiation with respect to a compatible coordinate. In particular, using a $D$-parallel trivialization of $\mathcal{E}$ and an affine coordinate $r$ (i.e., $D \mathrm{~d} r=0), \mathcal{B}_{r}=2\left(\mathcal{B}^{2}\right)_{0}$.

Joyce's lemma now gives the following result.
Theorem 2.3. Let $M$ be an oriented conformal manifold with a 3-dimensional Lie algebra $\mathfrak{h}$ of linearly independent conformal vector fields such that the projection $\pi$ onto the space of orbits is a submersion over a curve $C$. Let $\mathcal{E}$ be a rank 3 conformal vector bundle on $C$ such that $\pi^{*} \mathcal{E}$ is the vertical bundle of $M$ (trivialized along the fibres by invariant vector fields) and define $(D, \mathcal{B})$ by equation (2.4) as explained above.

Then $M$ is selfdual if and only if $(C, \mathcal{E})$ is a Riccati space.

\subsection*{2.2 Reduction to two dimensions}

The two-dimensional geometry is perhaps the richest. In the Euclidean case, $Q$ is a Riemann surface, which will be denoted $N$, and the conformal vector bundle $\mathcal{V}$ has rank two, and so will be viewed as a complex line bundle $\mathcal{W} \rightarrow N$. It will be convenient to view $\varphi: \mathcal{W} \rightarrow \mathfrak{h}_{N}$ as a complex linear map $\frac{1}{2}(\varphi-\boldsymbol{i} \varphi \circ J): \mathcal{W} \rightarrow \mathfrak{h}_{N} \otimes \mathbb{C}$. The constraint $L_{\mathcal{W}}^{1}=L_{N}^{1}$ means that there is a Hermitian metric on $\mathcal{W}^{*} \otimes_{\mathbb{C}} T N$. On fixing orientations, this may also be interpreted as an identification $\mathcal{W} \otimes_{\mathbb{C}} \overline{\mathcal{W}}=T N \otimes_{\mathbb{C}} \overline{T N}$, or $\wedge^{1,1} \mathcal{W}=\wedge^{1,1} T N$. Here the orientations will be chosen so that the induced almost complex structure $J$ on $T M=\pi^{*}(\mathcal{W} \oplus T N)$ is selfdual, i.e., the corresponding weightless 2-form $\Omega \in \mathrm{C}^{\infty}\left(M, L^{2} \wedge^{2} T^{*} M\right)$ is selfdual.

The Hodge star operator on $\wedge^{2} T M$ interchanges the vertical and horizontal components using the identification above, and acts on mixed bivectors by $*(U \wedge X)=-J U \wedge J X$. In particular the torsion of the modified connection $\mathcal{D}$ is selfdual if and only if
$$\begin{aligned}
& \varphi^{-1}\left(F^{\alpha}-[\varphi, \bar{\varphi}]_{\mathfrak{h}}\right)=\psi \\
& \varphi^{-1}\left(D_{X}^{\alpha} \varphi(U)+D_{J X}^{\alpha} \varphi(J U)\right)=\langle\mathcal{C}(U), X\rangle+\langle\mathcal{C}(J U), J X\rangle
\end{aligned}$$
for any vector field $X$ and section $U$ of $\mathcal{W}$. The first equation defines $\psi$ uniquely. For the second equation, note that conformal connections $D$ on $\mathcal{W}$ form an affine space modelled on $T^{*} N \otimes_{\mathbb{R}} \mathfrak{c} \mathfrak{o}(\mathcal{W})$, and therefore $D$ can be chosen uniquely such that $\varphi^{-1} D_{X}^{\alpha} \varphi$ is symmetric and traceless for all $X$. The remaining ambiguity in $\mathcal{C}$ is fixed by supposing it is complex linear, i.e., a section of $S_{0}^{2} \mathcal{W}^{*} \otimes_{\mathbb{C}} T N$, so that the second equation determines it uniquely. Note though, that the second equation does not use all of $D$ : only the induced holomorphic structure of $\mathcal{W}$ is needed.

For the selfduality of the Weyl curvature, it now suffices to compute $R_{U, Y}^{D, t a}$ and one additional component. To see this, note first that $\widehat{\psi}$ and $\widehat{\mathcal{C}}$ are so $(T M)$-valued, and therefore no information is lost by considering $R^{\mathcal{D}}$ and $R^{D}$ to be the curvatures on $L^{-1} T M$ rather than $T M$, so that the curvature equation is an identity between $\operatorname{so}(T M)$-valued 2-forms. The selfduality condition is obtained by requiring that the Weyl part of $R^{\mathcal{D}, t a}$ is selfdual. This amounts to considering the traceless part of the induced bundle map from $\wedge_{-}^{2} T M$ to so-( $T M$ ). Let $\bar{\Omega}$ and $\bar{J}$ be the sections of these bundles obtained by reversing the orientation of $\Omega$ and $J$ on $T N$. There are therefore three equations to find:
\begin{itemize}
\item[(i)] The traceless part of the $\bar{\Omega}^{\perp} \otimes \bar{J}^{\perp}$ component of $R^{\mathcal{D}, \text { ta }}$ should be zero.
\item[(ii)] The part of $R^{\mathcal{D}, t a}$ in $\bar{\Omega}^{\perp} \otimes\langle\bar{J}\rangle$ should be zero.
\item[(iii)] The multiple of $\bar{\Omega} \otimes \bar{J}$ should equal half the trace in $\bar{\Omega}^{\perp} \otimes \bar{J}^{\perp}$.
\end{itemize}
All of these except (iii) involve considering only the part of $R^{\mathcal{D}, t a}$ in $\bar{\Omega}^{\perp} \otimes \operatorname{so}(T M)$, which involves evaluating $R^{\mathcal{D}, \text { ta }}$ on bivector fields of the form $U \wedge Y-*(U \wedge Y)=U \wedge Y+J U \wedge J Y$. An easy calculation gives
$$\begin{aligned}
R_{U, Y}^{D, t a}= & -D_{Y} \mathcal{C}(U, \cdot)+D_{Y} \mathcal{C}(U, \cdot)^{\mathrm{T}}-\frac{1}{4} D_{Y} \psi(J U)(J-\bar{J}) \\
& +\mathcal{C}(\langle\mathcal{C}(U), Y\rangle, \cdot)-\mathcal{C}(\langle\mathcal{C}(U), Y\rangle, \cdot)^{\mathrm{T}}-\frac{1}{4}\langle\mathcal{C}(U, J \psi), Y\rangle(3 J-\bar{J})-\frac{1}{4} J \psi(U) J \psi \Delta Y,
\end{aligned}$$
where ${ }^{\mathrm{T}}$ denotes the transpose, and I have contracted horizontal and vertical skew endomorphisms using $X \triangle Y=\frac{1}{2} \Omega(X, Y)(J-\bar{J})$ and $U \triangle V=\frac{1}{2} \Omega(U, V)(J+\bar{J})$. Also, using $\Omega, \psi$ may be viewed as a section of $\mathcal{W}^{*}$, so that $\psi(X, Y)=2 \Omega(X, Y) J \psi$.

One readily obtains conditions (i) and (ii):
$$\begin{aligned}
& D_{X} \mathcal{C}(U, \cdot)+D_{J X} \mathcal{C}(J U, \cdot)=0, \\
& \frac{1}{2}\left(D_{X} \psi(U)+D_{J X} \psi(J U)\right)=-3\langle\mathcal{C}(\psi, U), X\rangle,
\end{aligned}$$
for any vector field $X$ and section $U$ of $\mathcal{W}$.

It remains to compute condition (iii). For this note that $R^{D}$ is given by $\frac{1}{4} s_{N}(\Omega-\bar{\Omega}) \otimes(J-$ $\bar{J})+\frac{1}{4} s_{\mathcal{W}}(\Omega-\bar{\Omega}) \otimes(J+\bar{J})$, where $s_{N}=\frac{1}{2} \operatorname{scal}_{N}$ and $s_{\mathcal{W}}=\frac{1}{2} \operatorname{scal}_{\mathcal{W}}$ are the normalized scalar curvatures of $D$ on $T N$ and $\mathcal{W}$. This yields, finally,
$$s_{N}-s_{\mathcal{W}}=|\psi|^{2}-2|\mathcal{C}|^{2} .$$

These equations, and the equations defining $\mathcal{C}$ and $\psi$, depend only on $D$ through the induced holomorphic structure $\bar{\partial}^{a}$ on $\mathcal{W}$. The conformal connections on $\mathcal{W}$ and $T N$ may be viewed as Chern connections determined by the holomorphic structures on these bundles together with the choice of a Weyl derivative on $L^{1}$. The difference $s_{N}-s_{\mathcal{W}}$ does not depend on the choice of Weyl derivative, since it is the normalized scalar curvature of the Chern connection on the Hermitian line bundle $\mathcal{W}^{-1} T N$.

Aside 2.4. The construction of a "Chern-Weyl" connection does not seem to be known and relates to a simple coordinate-free description (also not well-known) of the usual Chern connection, so I will sketch it here. Let $E$ be a complex vector bundle (over a complex manifold $M, J$ ) with holomorphic structure $\bar{\partial}^{E}$ and compatible conformal metric c: $S_{\mathbb{R}}^{2} E \rightarrow L_{E}^{2}$ with respect to which the complex structure on $E$ is orthogonal; the latter is equivalently a conformal Hermitian structure $\bar{E} \otimes_{\mathbb{C}} E \rightarrow L_{E}^{2} \otimes \mathbb{C}$. (Note that a complex line bundle automatically has a conformal Hermitian structure.) Now given any covariant derivative $D$ on $L_{E}^{1}$, let $\bar{\partial}_{X}^{D}=\frac{1}{2}\left(D_{X}+\boldsymbol{i} D_{J X}\right)$ (for all vector fields $X$ ) be the induced almost holomorphic structure on $L_{E}^{2} \otimes \mathbb{C}$. Then there is a unique conformal Hermitian connection $D^{E}$ on $E$ inducing $D$ on $L_{E}^{1}$. It is given by the formula
$$\left\langle D_{X}^{E} s_{1}, s_{2}\right\rangle=\bar{\partial}_{X}^{D}\left\langle s_{1}, s_{2}\right\rangle-\left\langle s_{1}, \bar{\partial}_{X}^{E} s_{2}\right\rangle+\left\langle\bar{\partial}_{X}^{E} s_{1}, s_{2}\right\rangle,$$
where $s_{1}$ and $s_{2}$ are sections of $E$. The proof is immediate (the idea behind the formula is simply that $D^{E}=\partial^{E}+\bar{\partial}^{E}$, where $\partial^{E}$ is the complex-linear part of the derivative). In the case that the covariant derivative on $L_{E}^{1}$ is just a trivialization, so that $\bar{\partial}^{D}=\bar{\partial}$, this is the usual Chern connection by uniqueness.

Definition 2.5. Suppose that $\mathcal{W}$ is a complex line bundle over a Riemann surface $N$ such that $L_{\mathcal{W}}^{1}=L_{N}^{1}$ (i.e., there is a Hermitian metric on $\mathcal{W}^{-1} T N$ ). Equip $\mathcal{W}$ with a holomorphic structure $\bar{\partial}^{a}$, a section $\mathcal{C}$ of $\mathcal{W}^{-2} T N$, and a section $\psi$ of $\mathcal{W}^{-1}$. Then $(N, \mathcal{W})$ is said to be a spinor-vortex space if $\left(\bar{\partial}^{a}, \mathcal{C}, \psi\right)$ satisfy the equations
$$\begin{aligned}
& \bar{\partial}^{a} \mathcal{C}=0, \\
& \bar{\partial}^{a} \psi=-3 \mathcal{C} \bar{\psi}, \\
& s_{\mathcal{W}^{-1} T N}=\psi \bar{\psi}-2 \mathcal{C} \overline{\mathcal{C}},
\end{aligned}$$
where $s_{\mathcal{W}^{-1} T N}$ is the normalized scalar curvature of the Chern connection on $\mathcal{W}^{-1} T N$.
Joyce's lemma now gives the following result.
Theorem 2.6. Let $M$ be an oriented conformal manifold with a 2-dimensional Lie algebra $\mathfrak{h}$ of linearly independent conformal vector fields such that the projection $\pi$ onto the space of orbits is a submersion over a Riemann surface $N$. Let $\mathcal{W}$ be a complex line bundle on $N$ such that $\pi^{*} \mathcal{W}$ is the vertical bundle of $M$ (trivialized along the fibres by invariant vector fields) and define $\left(\bar{\partial}^{a}, \mathcal{C}, \psi\right)$ by (2.5) as explained above.

Then $M$ is selfdual if and only if $(N, \mathcal{E})$ is a spinor-vortex space.
Of course there are only two possible 2-dimensional Lie algebras. In the case that $\mathfrak{h}$ is Abelian and $\psi=0$, this result reduces to the original application of Lemma 2.1 by Joyce [37].

Remark 2.7. It is straightforward to adapt the calculations of this subsection to other signatures: in general $N$ is a conformal surface with two line bundles $\mathcal{W}, \widetilde{\mathcal{W}}$ such that $\mathcal{W} \widetilde{\mathcal{W}} \cong$ $T^{1,0} N T^{0,1} N$ where $T^{1,0} N$ and $T^{0,1} N$ are the null line subbundles of $T N \otimes \mathbb{C}$. The line bundles $\mathcal{W}$ and $\widetilde{\mathcal{W}}$ are equipped with "(anti)holomorphic structures" $\tilde{\partial}^{a}, \partial^{a}$ and there are sections $(\mathcal{C}, \widetilde{\mathcal{C}}, \psi, \widetilde{\psi})$ satisfying appropriate reality conditions: in the Euclidean case $\widetilde{\mathcal{W}}=\overline{\mathcal{W}}, \widetilde{\mathcal{C}}=\overline{\mathcal{C}}$ and $\psi=\bar{\psi}$, but there is also a Lorentzian case, when the fields are all real, and a Euclidean reduction from Kleinian signature $(2,2)$ when $\widetilde{\psi}=-\bar{\psi}$.

\subsection*{2.3 Reduction to three dimensions}

The reduction to three dimensions is the Jones-Tod correspondence [36], which was one of the motivations for this work. The proof using Joyce's lemma is outlined in [37], so I will only recall the main ideas and definitions.

In this case, $Q$ is an oriented 3-dimensional conformal manifold, which will be denoted $B$, and $\mathcal{V}$ is an oriented line bundle isomorphic to $L^{1}=L_{B}^{1}$. Note that $\mathcal{C}$ automatically vanishes, and write $\psi=* \omega$, where $\omega$ is a 1-form on $B$. Then the torsion $T^{\mathcal{D}}$ will be selfdual provided that
$$*(D \varphi-\omega \varphi)=F^{\alpha} .$$
(The connection $\alpha$ does not act on $\varphi$ since $\mathfrak{h}$ is Abelian.)
This equation determines $(D, \omega)$ up to the gauge freedom $D \mapsto D+\gamma, \omega \mapsto \omega-\gamma$ for any 1-form $\gamma$ on $B$ (note that $(D+\gamma) \varphi=D \varphi-\gamma \varphi$, since $\varphi$ has weight -1). In other words, it determines uniquely the Weyl derivative $D+\omega$. This is called the Jones-Tod Weyl structure.

The gauge freedom can be used to set $D \varphi=0$, or to set $\omega=0$. Taking the latter point of view, the Jones-Tod Weyl structure is just $D$, determined by $* D \varphi=F^{\alpha}$.

The curvature of $\mathcal{D}$ is simply the pullback of the curvature of $D$ on $B$. In particular the Weyl part will be selfdual iff it vanishes and this is readily seen to be equivalent to the vanishing of $r_{0}^{D}$ [37].

Definition 2.8. Suppose that $B$ is a conformal 3-manifold and let $D$ be a Weyl connection on $B$. Then $B$ is said to be an Einstein-Weyl space iff $r_{0}^{D}=0$, i.e., the symmetric traceless Ricci tensor of $D$ vanishes.

Theorem 2.9 ([36]). Let $M$ be an oriented conformal 4-manifold and $K$ a nonvanishing conformal vector field such that the projection $\pi$ of $M$ onto the space of trajectories is a submersion over a conformal manifold $B$. Equip $B$ with the Jones-Tod Weyl structure.

Then $M$ is selfdual if and only if $B$ is Einstein-Weyl.
All three background geometries are themselves defined by geometric gauge theories: conformal local trivializations of the bundle $\mathcal{V}$ over $Q$ are related by gauge transformations. In the three-dimensional case, $\mathcal{V}$ is simply $L^{1}$, so conformal trivializations are length scales, and this is Weyl's original gauge theory [63]. Analogously, in the one and two-dimensional case, $\mathcal{E}$ and $\mathcal{W}$ should be regarded as part of the geometry of the space, not auxiliary bundles, and these background equations, although gauge-theoretic, should not be confused with the gauge field equations on auxiliary $G$-bundles which will be studied in Section 4.

\section*{Addenda: null reductions}

The constructions of this section assume nondegeneracy of the conformal structure c on $M$ along the orbits of the symmetry group $H$. In (real) Euclidean signature, this is automatic, but this is not the case when $M$ has Kleinian signature, nor when $M$ is a holomorphic conformal manifold. When the conformal structure degenerates on the orbits, the reduction is said to be
null. For the generic local considerations of this paper, I assume that the radical (or kernel) $R_{V}:=V M \cap V M^{\perp}$ of the conformal structure along the $H$ orbits has constant rank (as before, $V M$ denotes the tangent bundle to the $H$ orbits). There are thus three possibilities:
\begin{itemize}
\item[(1)] $R_{V}$ has rank one;
\item[] (2+) $R_{V}=U_{+}$has rank two and is selfdual;
\item[] (2-) $R_{V}=U_{-}$has rank two and is antiselfdual.
\end{itemize}

In case (1), $R_{V}^{\perp}=V M+V M^{\perp}$ has rank three, and $R_{V}^{\perp} / R_{V}$ is the sum of two null subbundles with a nondegenerate pairing between them. Their inverse images $U_{ \pm}$in $R_{V}^{\perp}$ are selfdual and antiselfdual null 2-plane distributions. There are several subcases to consider here, depending on the rank of $V M$. If either $U_{ \pm} \subseteq V M$ then $V M$ must have rank 3, in which case $V M^{\perp} \subset V M$, hence $V M^{\perp}=R_{V}$ and $R_{V}^{\perp}=V M$, so $V M=U_{+}+U_{-}$. If $V M$ has rank two, then $T M=$ $V M+U_{+}+U_{-}$, and clearly if rank $V_{M}=1$, then $R_{V}=V M$.

Cases (2±) are simpler, at least when $\operatorname{rank} V M=2$, so $V M=R_{V}$ is a bundle of selfdual or antiselfdual 2-planes. I concentrate on these two cases here. One justification for such a focus is that in the other cases, one may be able to prove that the distributions $U_{+}$or $U_{-}$are integrable, and hence study the reduction in terms of their leaf spaces. For instance, Dunajski-West [72] establish such an integrability result when $\operatorname{rank} V M=1$.

Suppose then that $\pi: M \rightarrow Q=M / H$ is a principal $H$-bundle over a manifold $Q$ such that $V M$ has rank two and is totally null. As $V M^{\perp}=V M$, neither $V M$ nor $T Q$ inherit conformal structures from $M$; instead there is a nondegenerate pairing $V M \times \pi^{*} T Q \rightarrow L^{2}$. This pairing in $H$-invariant, and thus identifies $V M=\pi^{*}\left(T^{*} Q \otimes \mathcal{V}\right)$, for a line bundle $\mathcal{V} \rightarrow Q$ (whose pullback to $M$ will be identified with $L^{2}$ ). As in the nondegenerate setting the isomorphism of $V M$ with $M \times \mathfrak{h}$ descends to a bundle isomorphism $\varphi: T^{*} Q \otimes \mathcal{V} \rightarrow \mathfrak{h}_{Q}:=M \times_{H} \mathfrak{h}$ over $Q$. There is no canonical splitting of the short exact sequence $0 \rightarrow \pi^{*} T^{*} Q \otimes \mathcal{V} \rightarrow T M \rightarrow \pi^{*} T Q \rightarrow 0$, but such a splitting may be chosen so that the complementary subbundle to $V M$ is $H$-invariant and null. This yields a principal $H$-connection $\alpha$ on $\pi: M \rightarrow Q$.

A torsion-free connection on $T N$ and a connection on $\mathcal{V}$ together induce a conformal connection $D$ on $T M$ with vertical-valued torsion as before. A conformal connection $\mathcal{D}$ with selfdual torsion may be obtained by adding correction terms to $D$. Compared to the nondegenerate case, the correction term $\mathcal{C}$ may be absorbed into the choice of $D$, and replaced by a vertical correction $\chi: \wedge^{2}\left(T^{*} Q \otimes \mathcal{V}\right) \rightarrow T^{*} Q \otimes \mathcal{V}$. Thus $\mathcal{D}=D+\widehat{\chi}+\widehat{\psi}$, where $\psi: \wedge^{2} T Q \rightarrow T^{*} Q \otimes \mathcal{V}$ as before, and
$$\begin{aligned}
& 2 \widehat{\chi}_{U+X}(V+Y)=\langle\chi(U, \cdot), Y\rangle+\langle\chi(V, \cdot), X\rangle-\chi(U, V), \\
& 2 \widehat{\psi}_{U+X}(V+Y)=\langle\psi(X, \cdot), Y\rangle+\langle\psi(Y, \cdot), X\rangle-\psi(X, Y) .
\end{aligned}$$
The torsion satisfies
$$\begin{aligned}
& T^{\mathcal{D}}(U, V)=\varphi^{-1}[\varphi(U), \varphi(V)]_{\mathfrak{h}}-\chi(U, V), \\
& T^{\mathcal{D}}(U, X)=\varphi^{-1} D_{X}^{\alpha} \varphi(U), \\
& T^{\mathcal{D}}(X, Y)=\varphi^{-1} F^{\alpha}(X, Y)-\psi(X, Y),
\end{aligned}$$
while the curvature computes to
$$\begin{aligned}
R_{U+X, V+Y}^{D}= & R_{U+X, V+Y}^{D}+(\widehat{\chi}+\widehat{\psi})_{T^{\mathcal{D}}(U+X, V+Y)} \\
& +D_{U+X}(\widehat{\chi}+\widehat{\psi})_{V+Y}-D_{V+Y}(\widehat{\chi}+\widehat{\psi})_{U+X} \\
& +(\widehat{\chi}+\widehat{\psi})_{\psi(X, Y)}+(\widehat{\chi}+\widehat{\psi})_{\chi(U, V)}+\llbracket(\widehat{\chi}+\widehat{\psi})_{U+X},(\widehat{\chi}+\widehat{\psi})_{V+Y} \rrbracket .
\end{aligned}$$

Hence the torsion-adjusted curvature is
$$\begin{aligned}
R_{U+X, V+Y}^{D, t a}= & R_{X, Y}^{D}+\llbracket(\widehat{\chi}+\widehat{\psi})_{X},(\widehat{\chi}+\widehat{\psi})_{Y} \rrbracket+\widehat{\chi}_{\psi(X, Y)} \\
& +D_{X}(\widehat{\chi}+\widehat{\psi})_{Y}-D_{Y}(\widehat{\chi}+\widehat{\psi})_{X}+D_{X} \widehat{\chi}_{V}-D_{Y} \widehat{\chi}_{U} \\
& +\llbracket(\widehat{\chi}+\widehat{\psi})_{X}, \widehat{\chi}_{V} \rrbracket+\llbracket \widehat{\chi}_{U},(\widehat{\chi}+\widehat{\psi})_{Y} \rrbracket+\llbracket \widehat{\chi}_{U}, \widehat{\chi}_{V} \rrbracket+\widehat{\chi}_{\chi(U, V)} .
\end{aligned}$$

\section*{Antiselfdual ( $\alpha$-surface) reduction}

When $V M$ is antiselfdual, the fibres of $\pi: M \rightarrow Q$ are $\alpha$-surfaces (i.e., they correspond to points in the twistor space of $M$ ). Under the isomorphism of $T M$ with $\pi^{*}\left(T^{*} Q \otimes \mathcal{V} \oplus T Q\right)$, the antiselfdual bivectors decompose into three rank one subbundles: $\wedge^{2}\left(T^{*} Q \otimes \mathcal{V}\right), \wedge^{2} T Q$, and the tracelike part of $T Q \otimes T^{*} Q \otimes \mathcal{V}$. The corresponding decomposition of so_( $T M$ ) has summands Hom_( $T Q, T^{*} Q \otimes \mathcal{V}$ ), Hom_ $\left(T^{*} Q \otimes \mathcal{V}, T Q\right)$ and the span of $\operatorname{id}_{T^{*} Q \otimes \mathcal{V}}-\operatorname{id}_{T Q}$; here Hom_ denotes the subbundle of skew symmetric operators.

In order to interpret equations (2.10)-(2.12) and (2.13), it is convenient to set $\mathcal{V}=\mathcal{L}^{2} \otimes \wedge^{2} T Q$ for a line bundle $\mathcal{L}$, so that $\varphi, \psi$ and $\chi$ may be viewed as 1-forms on $Q$, with values in $\mathcal{L}^{2} \otimes \mathfrak{h}_{Q}$, $\mathcal{L}^{-2}$ and $\mathcal{L}^{2}$ respectively.

Then $T^{\mathcal{D}}$ is selfdual iff $\chi \wedge \varphi=\frac{1}{2}[\varphi \wedge \varphi]_{\mathfrak{h}}, \psi \wedge \varphi=F^{\alpha}$ and $\mathrm{d}^{D, \alpha} \varphi=0$. The first two equations determine $\chi$ and $\psi$ uniquely (since $\varphi: T N \rightarrow \mathcal{L} \otimes \mathfrak{h}_{Q}$ is injective), while the third depends only on (and essentially determines) the connection $a$ induced by $D$ on $\mathcal{L}$.

In the expression (2.13) for the torsion-adjusted curvature, very few terms contribute to the antiselfdual Weyl part. For instance, only the trace part of first and last lines contribute, and the latter trace vanishes identically. After some tedious computations, the background equations for the 1-forms $\psi$ and $\chi$ and the connection $a$ on $\mathcal{L}$ reduce to
$$\mathrm{d}^{a} \psi=0, \quad \mathrm{~d}^{a} \chi=0, \quad F^{a}=\chi \wedge \psi,$$
which may be interpreted as the flatness of the connection $\mathrm{d}^{a}+\psi+\chi$ on $\mathcal{L} \oplus \mathcal{L}^{-1}$ (where $\mathrm{d}^{a}$ is the direct sum connection, while $\psi$ and $\chi$ are viewed as 1 -forms with values in $\operatorname{Hom}\left(\mathcal{L}^{-1}, \mathcal{L}\right)$ and $\left.\operatorname{Hom}\left(\mathcal{L}, \mathcal{L}^{-1}\right)\right)$.

\section*{Selfdual ( $\beta$-surface) reduction}

In the selfdual case, only the mixed part of $T^{\mathcal{D}}$ has a antiselfdual component, so there is no loss in setting $\psi=\chi=0$. The selfduality of the torsion then reduces to $D^{\alpha} \varphi=\frac{1}{2} \mathrm{~d}^{D^{\alpha}} \varphi$, where $\varphi$ is interpreted as a 1-form on $Q$ as before. This equation determines $D$ up to projective transformation $\left(D_{X} Y \mapsto D_{X} Y+\gamma(X) Y+\gamma(Y) X\right.$ for a 1-form $\left.\gamma\right)$, and the background equations are vacuous. Hence the background geometry is an arbitrary (torsion-free) projective surface $(Q,[D])$; this reduction was obtained in [72] and [65].

\section*{3 Interlude: Bianchi metrics}

Selfdual conformal manifolds with a freely acting three-dimensional symmetry group have been studied in many places [14, 15, 31, 42, 43, 47, 53, 54, 55]. In this interlude, I will show briefly how the direct approach to selfdual Bianchi metrics is related to the Riccati space reduction of the previous section.