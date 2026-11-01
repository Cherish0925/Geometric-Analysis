---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: An Unexpected Rational Blowdown]

Proof. Consider a twice-punctured torus with two meridians $\alpha_{1}$ and $\alpha_{2}$, a longitude $\beta$, and the two boundary parallel curves $\delta_{1}$ and $\delta_{2}$, as in Figure 18. For brevity, we will use the same notation for the curve and for the positive Dehn twist around this curve. By KO08, Section 3.2], we have a relation
$$\delta_{1} \delta_{2}=\left(\alpha_{1} \alpha_{2} \beta\right)^{4}$$
in the mapping class group of the 2-holed torus.
Using relations $\alpha_{i} \beta \alpha_{i}=\beta \alpha_{i} \beta$ and $\alpha_{1} \alpha_{2}=\alpha_{2} \alpha_{1}$, and writing $x^{y}=y^{-1} x y$ for conjugates, we have $\delta_{1} \delta_{2}=\left(\alpha_{1} \alpha_{2} \beta\right)^{4}=\alpha_{1} \alpha_{2} \beta \alpha_{1} \alpha_{2} \beta \alpha_{1} \underline{\alpha_{2} \beta \alpha_{2}} \alpha_{1} \beta=\alpha_{1} \alpha_{2} \beta \alpha_{1} \alpha_{2} \beta \alpha_{1} \beta \alpha_{2} \underline{\beta \alpha_{1} \beta}=\alpha_{1} \underline{\alpha_{2} \beta \alpha_{2}} \alpha_{1} \beta \alpha_{1} \beta \alpha_{2} \underline{\alpha_{1} \beta \alpha_{1}}=$ $\alpha_{1} \beta \alpha_{2} \beta \alpha_{1} \beta \alpha_{1} \beta \alpha_{2} \alpha_{1}^{2} \beta^{\alpha_{1}}=\alpha_{1} \beta \alpha_{2} \alpha_{1} \beta \alpha_{1}^{2} \beta \alpha_{2} \alpha_{1}^{2} \beta^{\alpha_{1}}=\alpha_{1} \beta \alpha_{2} \alpha_{1} \beta \alpha_{1}^{4} \beta^{\alpha_{1}^{2}} \alpha_{2} \beta^{\alpha_{1}}=\alpha_{1} \beta \alpha_{2} \alpha_{1}^{5} \beta^{\alpha_{1}^{4}} \beta^{\alpha_{1}^{2}} \alpha_{2} \beta^{\alpha_{1}}=$ $\alpha_{1}^{6} \beta_{1}^{\alpha_{1}^{5}} \alpha_{2} \beta^{\alpha_{1}^{4}} \beta^{\alpha_{1}^{2}} \alpha_{2} \beta^{\alpha_{1}}=\alpha_{1}^{6} \alpha_{2}\left(\beta^{\alpha_{1}^{5}}\right)^{\alpha_{2}} \beta^{\alpha_{1}^{4}} \beta^{\alpha_{1}^{2}} \alpha_{2} \beta^{\alpha_{1}}$,

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/e81a01d2-897b-4840-89f5-84d3bbdef6cc-21.jpg?height=481&width=309&top_left_y=314&top_left_x=885}
\captionsetup{labelformat=empty}
\caption{Figure 18. Curves $\alpha_{1}, \alpha_{2}, \beta, \delta_{1}, \delta_{2}$ on a 2 -holed torus.}
\end{figure}
with the subwords to be changed at each step underlined for ease for reading. Taking the cube of this relation and performing similar manipulations to move $\alpha_{1}$ and $\alpha_{2}$ at the cost of taking further conjugates of the Dehn twists around the longitudinal curve $\beta$, we obtain a relation of the form
$$\alpha_{1}^{18} \alpha_{2}^{3} \text { (15 other positive Dehn twists) }=\delta_{1}^{3} \delta_{2}^{3} .$$
In turn, this gives gives a relation
$$\alpha_{1}^{18} \alpha_{2}^{3} \text { (15 other positive Dehn twists) }=1$$
on the torus when the two holes are capped off, and therefore gives an elliptic fibration over $S^{2}$. Treating each Dehn twist as a vanishing cycle for a Lefschetz singularity, we have a Lefschetz fibration on $E(3)$ with torus fiber and 36 nodal fibers. The punctures in the original relation (6.1) correspond to sections of this fibration, with self-intersection -3. Alternatively, we can replace some of the Lefschetz singularities by more complicated singular fibers: we isolate the subword $\alpha_{1}^{6} \alpha_{2}$ and think of it as the monodromy around a singular point corresponding to an $I_{7}$ fiber (see [HKK86, Table 1.9] or [SSS07, Section 2.1]). The $I_{7}$ fiber is given by the necklace of seven spheres obtained by collapsing $\alpha_{2}$ and six parallel copies of $\alpha_{1}$. By carefully keeping track of the vanishing cycles separating the intersection of the fiber with two sections (represented by the boundary components $\delta_{1}, \delta_{2}$ ) we see that for the chosen $I_{7}$ fiber, the two sections of $E(3)$ intersect it in adjacent spheres of the necklace of length 7.

To find another section in the complement of this configuration of curves, we can go through a similar argument leveraging the "star relation"
$$\delta_{1} \delta_{2} \delta_{3}=\left(\alpha_{1} \alpha_{2} \alpha_{3} \beta\right)^{3}$$
in the mapping class of the torus with 3 holes, where $\delta_{1}, \delta_{2}, \delta_{3}$ are the boundary-parallel curves, and $\alpha_{1}, \alpha_{2}, \alpha_{3}$ are three meridians separating them, [Ger01, KO08]. Manipulating the cube of this relation, we can similarly construct an elliptic fibration on $E(3)$ with an $I_{7}$ fiber and three sections intersecting prescribed spheres in the $I_{7}$ necklace. Isolating an additional $\alpha_{1} \alpha_{2}$ term together with the factor $\alpha_{1}^{6} \alpha_{2}$ used to create $I_{7}$, we can find the required $I_{2}$ fiber.

Finally, we can assume that $E(3)$ is equipped with a complex structure such that the fibers are symplectic; this ensures that the (-2)-spheres are symplectic. The sections can be assumed to be symplectic because we can use the standard symplectic disk bundles with a symplectic 0-section of self-intersection -1 to cap off the boundary of the fibration arising from (6.1). \(\square\)

Proposition 6.2. The blowup $E(3) \# 5 \overline{\mathbb{C P}}^{2}$ of the elliptic fibration from Lemma 6.1 contains a plumbing given by the graph $G_{0,1}$. Blowing down this graph produces an exotic copy of $5 \mathbb{C P}^{2} \# 27 \overline{\mathbb{C P}}^{2}$.

Proof. Using the dual graph given by the lemma, we blow up 4 times at one of the $(-3)$ vertices, and do one more blowup at a (-2)-vertex adjacent to the (-3)-vertex, as in the figure. The resulting

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/e81a01d2-897b-4840-89f5-84d3bbdef6cc-22.jpg?height=365&width=907&top_left_y=305&top_left_x=627}
\captionsetup{labelformat=empty}
\caption{Figure 19. Left: A configuration of embedded spheres in $E(3)$. Right: after the blowups, there is a subgraph $G_{0,1}$. Unlabeled vertices are understood to have framing -2.}
\end{figure}
configuration contains the graph $G_{0,1}$. Since this is a plumbing of symplectic disk bundles, we have the canoninical contact structure induced on the boundary of the plumbing $G_{0,1}$. Surgering out this symplectic plumbed 4-manifold and replacing it with the Stein rational homology disk filling $W$ provided by Theorem 1.1, we get a new closed symplectic manifold $X=X^{\prime} \cup_{Y} W$, where $X^{\prime}$ is the complement of the plumbing in the blowup of $E(3)$, and $Y$ is its boundary. The intersection form of $X$ is odd: in the elliptic fibration constructed in Lemma 6.1, we can find a section disjoint from all the components of the $G_{0,1}$ curve configuration; this section is unaffected by the surgery and thus gives a homology class in $X$ of self-intersection -3 . We check that $X$ is simply connected. By construction, the filling $W$ is the complement of $\cup_{i} \nu\left(\Gamma_{i}\right)$ in the blowup of the 4-ball. Fixing a basepoint in $Y$, we have $\pi_{1}(W) \hookrightarrow \pi_{1}(Y)$, because $\pi_{1}(W)$ is generated by the loops around the cocore disks of $\nu\left(\Gamma_{i}\right)$ 's. It remains to check that $X^{\prime}$ is simply connected. Since $X^{\prime}$ is the complement of the tree plumbing of spheres in a simply connected manifold, $\pi_{i}(X)$ is generated by the loops that are boundaries of the normal disks to the spheres of the plumbing; moreover, it suffices to consider only the loops that correspond to the leaves of the tree. For our embedding of the configuration $G_{0,1}$, two of the leaves are the spheres of $I_{7}$ in the original elliptic fibration, and the other two correspond to the sections. For the first pair of leaves, the loops that are boundaries of the normal disks to the spheres of $I_{7}$ are contractible because they bound disks in the two punctured spheres given by the "leftover" part of the $I_{7}$ fiber (in the complement of our configuration). For the leaves that are sections, we need to check that the loops corresponding to the curves $\delta_{1}$ and $\delta_{2}$ in the $I_{7}$ fiber are contractible in $X^{\prime}$. This follows from the fact that the curves $\alpha_{1}$ and $\alpha_{2}$ bound disks in $X^{\prime}$, since by construction the elliptic fibration of Lemma 6.1 has an $I_{2}$ fiber where these curves in a nearby regular fiber are collapsed to points: using these disks, we can find a nullhomotopy for $\delta_{1}$ and $\delta_{2}$.

Since $\sigma(E(3))=-24$ and $b_{2}(E(3))=34$, after 5 blowups and a blowdown of a negative definite 7-vertex tree, we have $\sigma(X)=-22$ and $b_{2}(X)=32$, so $b_{2}^{+}(X)=5, b_{2}^{-}(X)=27$. It now follows that $X$ is homeomorphic to $5 \mathrm{CP}^{2} \# 27 \overline{\mathrm{CP}}^{2}$, but the two manifolds are not diffeomorphic because $X$ is symplectic, and $5 \mathbb{C P}^{2} \# 27 \overline{\mathbb{C P}^{2}}$ has vanishing Seiberg-Witten invariant. \(\square\)

\section*{7. QHD fillings for the two-parameter family}

In this section, we prove Theorem 1.1 for the general case of the graphs $G_{k, n}$. We give more schematic diagrams with brief comments, but this should be sufficient as the steps are similar to those in Section 5. We only treat the case $k$ even; $k$ odd is similar.

The decorated germ corresponding to the graph $G_{k, n}$ has $n+k+6$ irreducible components, see Section 2. We set $s=n+k+6$ for brevity. The Scott deformation is obtained similarly to the previous examples, where the curves corresponding to $C_{1}, \ldots C_{k+6}$ are shown in blue, and the curves corresponding to $C_{1}^{\prime}, \ldots C_{n}^{\prime}$ are shown in red. Assume $n \geq 2$, since the case $n=1$ was done previously.
![](https://cdn.mathpix.com/cropped/e81a01d2-897b-4840-89f5-84d3bbdef6cc-23.jpg?height=425&width=1504&top_left_y=314&top_left_x=352)
In the diagram of the Scott deformation, we use move (4.4) to split the multipoint $\mathrm{I}_{2 n}^{1}$ :
![](https://cdn.mathpix.com/cropped/e81a01d2-897b-4840-89f5-84d3bbdef6cc-23.jpg?height=419&width=1525&top_left_y=834&top_left_x=352)
Then use merge move (4.5) to combine the $\mathrm{I}_{2 s}^{s+2}$ multipoint with crossings of the (blue) strand $(s+1)$ passing above:
![](https://cdn.mathpix.com/cropped/e81a01d2-897b-4840-89f5-84d3bbdef6cc-23.jpg?height=417&width=1510&top_left_y=1388&top_left_x=352)
Note that $k+4$ is even and use move (4.8) to switch multipoints, moving the $(k+4)$ copies of $\mathrm{I}_{2 s}^{s+1}$ to the left:
![](https://cdn.mathpix.com/cropped/e81a01d2-897b-4840-89f5-84d3bbdef6cc-23.jpg?height=419&width=1512&top_left_y=1934&top_left_x=352)
Then move the $(k+4)$ copies of $\mathrm{I}_{2 s}^{s+1}$ through the tangency nest on the left, using move (4.11) $k+4$ times (note the braiding $\Delta^{ \pm(k+4)}$ on the left of the next diagram):
![](https://cdn.mathpix.com/cropped/e81a01d2-897b-4840-89f5-84d3bbdef6cc-24.jpg?height=412&width=1510&top_left_y=292&top_left_x=354)
Using moves (4.7) and (4.5), combine the $k+4$ multipoints $\mathrm{I}_{s}^{1}$ down past the crossings with red strands, and combine each multipoint with the double point crossings of one additional blue strand, forming multipoints $\mathrm{I}_{s+n+2}^{n+2}, \ldots, \mathrm{I}_{2 s-1}^{s-1}$ :
![](https://cdn.mathpix.com/cropped/e81a01d2-897b-4840-89f5-84d3bbdef6cc-24.jpg?height=410&width=1517&top_left_y=917&top_left_x=357)
Use move (4.7) to slide $(n-1)$ copies of $\mathrm{I}_{s+n}^{s+1}$ to the right of the diagram, where they become multipoints $I_{n}^{1}$. Then use move (4.11) to slide one of the two remaining copies of $\mathrm{I}_{s+n}^{s+1}$ up through the tangency nest, creating additional braiding on the red strands, then combine this multipoint with the second copy of $\mathrm{I}_{s+n}^{s+1}$ and all the double point crossings on the red strands to make $\mathrm{I}_{s+n}^{s+1-n}$ via move (4.4). Slide multipoint $\mathrm{I}_{2 s}^{s+n+1}$ on the blue strands to the left under the red strands, where it becomes $\mathrm{I}_{2 s-n}^{s+1}$ :
![](https://cdn.mathpix.com/cropped/e81a01d2-897b-4840-89f5-84d3bbdef6cc-24.jpg?height=425&width=1502&top_left_y=1594&top_left_x=354)
Apply move (4.11) to slide $\mathrm{I}_{2 s-n}^{s+1}$ up through the tangency nest on blue strands; the result is $\mathrm{I}_{s}^{n+1}$ and the extra braiding on the left:
![](https://cdn.mathpix.com/cropped/e81a01d2-897b-4840-89f5-84d3bbdef6cc-25.jpg?height=382&width=1500&top_left_y=312&top_left_x=352)
Slide $\mathrm{I}_{s}^{n+1}$ over the crossings with red strands; it becomes $\mathrm{I}_{k+6}^{1}$. Use move (4.9) to switch $\mathrm{I}_{s+n}^{s+1-n}$ to the left of the tangency nest on the red strands:
![](https://cdn.mathpix.com/cropped/e81a01d2-897b-4840-89f5-84d3bbdef6cc-25.jpg?height=387&width=1495&top_left_y=804&top_left_x=352)

Combine $\mathrm{I}_{k+6}^{1}$ and one of the copies of $\mathrm{I}_{n}^{1}$ with double points of the $n$ red strands, using move (4.4) to create $\mathrm{I}_{s}^{1}$ :
![](https://cdn.mathpix.com/cropped/e81a01d2-897b-4840-89f5-84d3bbdef6cc-25.jpg?height=387&width=1495&top_left_y=1345&top_left_x=352)

Using (4.12), move (blue) strand $s+n+1$ that has double point intersections with $n$ (red) strands $s+1, \ldots s+n$ located to the right of the red tangency nest:
![](https://cdn.mathpix.com/cropped/e81a01d2-897b-4840-89f5-84d3bbdef6cc-25.jpg?height=387&width=1495&top_left_y=1878&top_left_x=352)

Use (4.6) to combine double points from this last blue strand with $\mathrm{I}_{s}^{1}$ into $\mathrm{I}_{s+1}^{1}$ :
![](https://cdn.mathpix.com/cropped/e81a01d2-897b-4840-89f5-84d3bbdef6cc-26.jpg?height=380&width=1497&top_left_y=312&top_left_x=350)

Use move (4.8) to switch $\mathrm{I}_{s+1}^{1}$ with multipoints $\mathrm{I}_{n}^{1}$ on the right, moving these $(n-2)$ multipoints next to the red tangency nest:
![](https://cdn.mathpix.com/cropped/e81a01d2-897b-4840-89f5-84d3bbdef6cc-26.jpg?height=374&width=1517&top_left_y=857&top_left_x=331)

Move the red intersections through the red tangency nest using (4.14); this creates extra braiding $\Delta^{n-2}$. Using move (4.15), we can slide these half twists to the left side, past $\mathrm{I}_{s+n}^{s+1-n}$ and then under the blue strands.
![](https://cdn.mathpix.com/cropped/e81a01d2-897b-4840-89f5-84d3bbdef6cc-26.jpg?height=374&width=1517&top_left_y=1422&top_left_x=331)

We now focus on the subdiagram in the middle of the figure, formed by the red strands with tangency nest, the multipoints $\mathrm{I}_{s+n}^{s+1-n}$ and $(n-2)$ copies of $\mathrm{I}_{s}^{k+7}$. This subconfiguration is similar to the previous ones, and we can work with it separately: although the blue strand passing through the middle cannot be isotoped away, it does not interfere with any moves we need. The indices in the pictures are shifted by $k+6$ for legibility. The subdiagram on the red strands is the Scott deformation of a star-shaped graph in $\mathcal{C}$, and the subdiagram we produce is the $\mathbb{Q H D}$ arrangement for that singularity. We break up the multipoint $\mathrm{I}_{2 n}^{1}$ as $\mathrm{I}_{2 n}^{n} \mathrm{X}_{n, 2 n}^{1, n-1} \mathrm{I}_{2 n}^{n+2}$ by (4.4), and follow our previous strategy. Namely, combine $\mathrm{I}_{2 n}^{n+2}$ with the strand above it and the corresponding double points to make $\mathrm{I}_{2 n}^{n+1}$. Then, slide copies of $\mathrm{I}_{n}^{1}$ down through X one by one, combining each with double points on one strand. This creates the multipoints $\mathrm{I}_{2 n}^{n}, \ldots, \mathrm{I}_{n+2}^{2}$. Finally, we slide $\mathrm{I}_{2 n}^{n+1}$ up through the tangency nest, at the cost of extra braiding, and combine with the remaining strand.
![](https://cdn.mathpix.com/cropped/e81a01d2-897b-4840-89f5-84d3bbdef6cc-27.jpg?height=1439&width=715&top_left_y=318&top_left_x=698)

After incorporating this last diagram as a subconfiguration into the previous diagram on the red and blue strands and decorating all intersections with marked points, we get a diagram representing DJVS arrangement that produces a rational homology disk. To get a simpler picture, we can move the braiding in the subconfiguration to the edge of the large diagram by (4.15), and then cancel the braiding on the edges as in Subsection 4.7 to arrive at the final diagram. \(\square\)
![](https://cdn.mathpix.com/cropped/e81a01d2-897b-4840-89f5-84d3bbdef6cc-28.jpg?height=417&width=1482&top_left_y=327&top_left_x=322)

\section*{References}
[A'C75] Norbert A'Campo. Le groupe de monodromie du déploiement des singularités isolées de courbes planes. I. Math. Ann., 213:1-32, 1975.
[Arv92] William A. Arvola. The fundamental group of the complement of an arrangement of complex hyperplanes. Topology, 31(4):757-765, 1992.
[Bek25] Márton Beke. Minimal rational graphs admitting a $\mathbb{Q H D}$ smoothing, 2025. arXiv:2504.06929.
[BH16] R. İnanç Baykur and Kenta Hayano. Multisections of Lefschetz fibrations and topology of symplectic 4manifolds. Geom. Topol., 20(4):2335-2395, 2016.
[BK86] Egbert Brieskorn and Horst Knörrer. Plane algebraic curves. Modern Birkhäuser Classics. Birkhäuser/Springer Basel AG, Basel, 1986. Translated from the German original by John Stillwell, [2012] reprint of the 1986 edition.
[BS11] Mohan Bhupal and András I Stipsicz. Weighted homogeneous singularities and rational homology disk smoothings. American journal of mathematics, 133(5):1259-1297, 2011.
[CPP04] Clément Caubel and Patrick Popescu-Pampu. On the contact boundaries of normal surface singularities. Comptes Rendus Mathematique, 339(1):43-48, 2004.
[CS97] Daniel C. Cohen and Alexander I. Suciu. The braid monodromy of plane algebraic curves and hyperplane arrangements. Comment. Math. Helv., 72(2):285-315, 1997.
[dJvS98] T. de Jong and D. van Straten. Deformation theory of sandwiched singularities. Duke Math. J., 95(3):451-522, 1998.
[Fow13] Jacob R Fowler. Rational homology disk smoothing components of weighted homogeneous surface singularities. PhD thesis, The University of North Carolina at Chapel Hill, 2013.
[FS97] Ronald Fintushel and Ronald J. Stern. Rational blowdowns of smooth 4-manifolds. J. Differential Geom., 46(2):181-235, 1997.
[Ger01] Sylvain Gervais. A finite presentation of the mapping class group of a punctured surface. Topology, 40(4):703-725, 2001.
[HKK86] John Harer, Arnold Kas, and Robion C Kirby. Handlebody decompositions of complex surfaces, volume 350. American Mathematical Soc., 1986.
[KO08] Mustafa Korkmaz and Burak Ozbagci. On sections of elliptic fibrations. Michigan Mathematical Journal, 56(1):77-87, 2008.
[Lau73] Henry B. Laufer. Taut two-dimensional singularities. Math. Ann., 205:131-164, 1973.
[LHMW18] Samuel Lisi, Jeremy Van Horn-Morris, and Chris Wendl. On symplectic fillings of spinal open book decompositions I: Geometric constructions, 2018.
[LHMW20] Samuel Lisi, Jeremy Van Horn-Morris, and Chris Wendl. On symplectic fillings of spinal open book decompositions II: Holomorphic curves and classification, 2020.
[MRW24] Hyunki Min, Agniva Roy, and Luya Wang. Spinal open books and symplectic fillings with exotic fibers, 2024. arXiv:2410.10697.
[Par05] Jongil Park. Simply connected symplectic 4-manifolds with $b_{2}^{+}=1$ and $c_{1}^{2}=2$. Invent. Math., 159(3):657-667, 2005.
[PS23] Olga Plamenevskaya and Laura Starkston. Unexpected Stein fillings, rational surface singularities and plane curve arrangements. Geom. Topol., 27(3):1083-1202, 2023.
[PS25] Olga Plamenevskaya and Laura Starkston. Sandwiched singularities and nearly Lefschetz fibrations, 2025. arXiv:2507.21293.
[SS05] András I. Stipsicz and Zoltán Szabó. An exotic smooth structure on $\mathbb{C P}^{2} \# 6 \overline{\mathbb{C} \mathbb{P}^{2}}$. Geom. Topol., 9:813-832, 2005.
[SSS07] András I Stipsicz, Zoltán Szabó, and Ágnes Szilárd. Singular fibers in elliptic fibrations on the rational elliptic surface. Periodica Mathematica Hungarica, 54(2):137-162, 2007.
[SSW08] András I. Stipsicz, Zoltán Szabó, and Jonathan Wahl. Rational blowdowns and smoothings of surface singularities. J. Topol., 1(2):477-517, 2008.
[Sym98] Margaret Symington. Symplectic rational blowdowns. J. Differential Geom., 50(3):505-518, 1998.
[Tei76] Bernard Teissier. The hunting of invariants in the geometry of discriminants. Real and complex singularities, Oslo, pages 565-677, 1976.
[Wah81] Jonathan Wahl. Smoothings of normal surface singularities. Topology, 20(3):219-246, 1981.
[Wah11] Jonathan Wahl. On rational homology disk smoothings of valency 4 surface singularities. Geometry \& Topology, 15(2):1125-1156, 2011.

Alfréd Rényi Institute of Mathematics, Budapest, University of Technology and Economics, Budapest, Hungary

Email address: bekem@renyi.hu
Department of Mathematics, Stony Brook University, Stony Brook, NY, 11794, U.S.A.
Email address: olga@math.stonybrook.edu
Deparment of Mathematics, University of California, Davis, 1 Shields Avenue, Davis, CA, 95616, U.S.A.
Email address: lstarkston@math.ucdavis.edu