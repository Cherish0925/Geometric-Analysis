---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: An Unexpected Rational Blowdown]

---
source_file: 2510_00115.pdf
converter: mathpix
format: mmd
---

\title{
AN UNEXPECTED RATIONAL BLOWDOWN
}

\author{
MÁRTON BEKE, OLGA PLAMENEVSKAYA, AND LAURA STARKSTON
}

\begin{abstract}
The rational blowdown operation in 4-manifold topology replaces a neighborhood of a configuration of spheres by a rational homology ball. Such configurations typically arise from resolutions of surface singularities that admit rational homology disk smoothings. Conjecturally, all such singularities must be weighted homogeneous and belong to certain specific families: Stipsicz-Szabó-Wahl constructed $\mathbb{Q H D}$ smoothings for these families and used Donaldson's theorem to obtain very restrictive necessary conditions on the resolution graphs for singularities with this property. In particular, these results, as well as subsequent work of Bhupal-Stipsicz, show that for certain resolution graphs, the canonical contact structure on the link of the singularity cannot admit a QHD symplectic filling. By contrast, we exhibit Stein rational homology disk fillings for the contact links of an infinite family of rational singularities that are not weighted homogeneous, producing a new symplectic rational blowdown. Inspiration for our construction comes from de Jong-van Straten's description of Milnor fibers of sandwiched singularities; we use the symplectic analog of de Jong-van Straten theory developed by the second and third authors. The unexpected Stein fillings are built using spinal open books and nearly Lefschetz fibrations.
\end{abstract}

\section*{1. Introduction}

In 4-manifold topology, a rational blowdown surgery [FS97] is used to create exotic pairs of smooth manifolds, [Par05, SS05]; this operation can be done symplectically Sym98. Rational blowdowns typically come from smoothings of certain surface singularities. If $(X, 0)$ is a normal surface singularity with minimal good resolution $\tilde{X}$, then the standard neighborhood of the exceptional divisor in $\tilde{X}$ is a plumbing of disk bundles over the exceptional curves, according to the dual resolution graph $G$. If the corresponding configuration of surfaces is contained in a smooth 4-manifold, it can be replaced by the Milnor fiber of a smoothing of the singularity. To create a manifold with small homology, one wants a Milnor fiber that is a rational homology disk.

From another perspective, understanding the topology of Milnor fibers is an interesting question in singularity theory. By Wah81, a surface singularity must be rational if it admits a smoothing that is a rational homology disk. However, few rational singularities have such smoothings. All known examples fall into several specific families of weighted homogeneous singularities; the corresponding resolution graphs have one node, of valency three or four, [SSW08]. It has been conjectured ([Wah11, Conjecture 8.10]) that the known examples give a complete list of surface singularities with $\mathbb{Q H D}$ smoothings.

In [SSW08], Stipsicz-Szabó-Wahl used Donaldson's theorem to attack the question by examining possible embeddings of the homology lattice of the plumbing into the diagonal lattice of the same rank. This gives very restrictive necessary conditions for the dual resolution graphs whose link can admit a symplectic QHD filling. Bhupal-Stipsicz ([BS11]) settled additional cases by studying symplectic fillings of the links of the corresponding singularities with their canonical contact structures: they showed that the only weighted homogeneous singularities whose links admit $\mathbb{Q H D}$ fillings are those with known $\mathbb{Q H D}$ smoothings. (This classification is reproved and extended with methods closer to the ones used in this paper in [Bek25] when combined with the results of [PS25].)

One could perhaps hope that the conjectural list exhausts all options for a symplectic rational blowdown, namely that $\mathbb{Q H D}$ symplectic fillings for the contact link only exist for the singularities on this list. In particular, one could conjecture that $\mathbb{Q H D}$ symplectic fillings cannot exist for resolution graphs with two or more nodes. However, we prove:

Theorem 1.1. Let $G_{k, n}$ be a dual resolution graph as in Figure 1, $\left(Y_{k, n}, \xi_{k, n}\right)$ the link of the corresponding singularity with its canonical contact structure. Then for all $k \geq 0, n \geq 1,\left(Y_{k, n}, \xi_{k, n}\right)$ admits
a Stein filling which is a rational homology disk, despite the fact that the surface singularities of the given topological type admit no rational homology disk smoothing.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/e81a01d2-897b-4840-89f5-84d3bbdef6cc-02.jpg?height=537&width=722&top_left_y=417&top_left_x=705}
\captionsetup{labelformat=empty}
\caption{Figure 1. The family $G_{k, n}$ for $k \geq-1, n \geq 0$, where $G_{k, n}$ has $k+n+6$ vertices, with $k$ vertices between the two nodes. The graph $G_{-1,1}$ has a single node of valency 4, with 6 vertices total.}
\end{figure}

For $k \geq 0$, the graphs of Figure 1 all have two nodes and belong to the family $\mathcal{C}$ of [SSW08], producing a new symplectic rational blowdown. It is interesting to note that for ${ }^{1} k=-1$, a rational homology disk smoothing actually exists for a singularity in the corresponding topological type by [Fow13, Theorem 5(a)], when the cross ratio of the intersection points of the node with the four arms is 9. Our construction produces a QHD Stein filling in this case as well, but we do not know whether our filling is diffeomorphic to the Milnor fiber. With this in mind, our construction is an extension of the $\mathcal{C}^{4}$ family of [BS11].

It seems plausible that similar $\mathbb{Q H D}$ Stein fillings can be constructed for other families of graphs of the $\mathcal{A}, \mathcal{B}, \mathcal{C}$ types of [SSW08] by similar extensions of $\mathcal{A}^{4}, \mathcal{B}^{4}$ or a different arm of $\mathcal{C}^{4}$. Possibly, one can find such fillings for graphs with an arbitrary large number of nodes (our arguments in Section 7 hint at a possible induction process), but we currently lack the methods to show that the corresponding singularities cannot admit any $\mathbb{Q H D}$ deformations. Combinatorial possibilities for many families with $\mathbb{Q H D}$ Stein fillings can be found by a computer search. However, each new family requires tedious separate analysis, so we only produce one 2-parameter family in this paper.

These graphs all correspond to sandwiched singularities (in combinatorial terms, this means that the graph can be augmented, by adding (-1) vertices, to a plumbing graph that can be blown down to a smooth point). Deformation theory for this class of singularities can be understood thanks to a very attractive approach of de Jong-van Straten [JJvS98]: the surface singularity $(X, 0)$ is encoded via the germ of a singular plane curve $(C, 0)$, and all smoothings of $(X, 0)$ correspond to certain picture deformations of $(C, 0)$, decorated with marked points. Milnor fibers can be reconstructed directly from picture deformations. In particular, a Milnor fiber of a smoothing is a rational homology disk if and only if the number of irreducible components of $(C, 0)$ matches the number of marked points of the corresponding picture deformation. The combinatorial features of the arrangement of curves and marked points in a picture deformation depend on the original dual resolution graph. In [Bek25], the first author was able to rule out rational homology disk smoothings for certain families of graphs through combinatorial analysis of possible curve and point arrangements. The family of Figure 1 was discovered in the process: combinatorial obstructions vanish, even though rational homology smoothings do not exist in this case by [Wah11, Theorem 8.6], since the graphs of Figure 1 are taut of type $\left(L_{2}\right)-\left(J_{1}\right)-\left(R_{1}\right)$ in the sense of Laufer [Lau73, Section 2.2]. For symplectic fillings of the

\footnotetext{
${ }^{1}$ This notation means contracting the edge between the two nodes, and giving them framing $a+b+2$ if the two nodes were framed $a, b$ respectively.
}
contact link of a sandwiched singularity, the second and third author developed an analog of the de Jong-van Straten theory [PS23, PS25], showing that all fillings arise in a similar way from certain immersed disk arrangements in $\mathbb{C}^{2}$ compatible with the germ $(C, 0)$ associated to the singularity. The constructions of [PS25] use spinal open books and nearly Lefschetz fibrations; the symplectic input comes from [BH16, LHMW18, LHMW20, MRW24].

Using the setting of [PS25], we will describe the unexpected QHD fillings by means of these immersed disk arrangements. In turn, the arrangements are encoded via braided wiring diagrams with tangencies; braided wiring diagrams were first introduced in [Arv92] as a tool to study complex line arrangements. To get a filling of the given link, we need to fix the boundary braid of the arrangement, up to isotopy. Inspired by [CS97], we develop diagrammatic moves that preserve the boundary monodromy, and then construct a new family of fillings from standard smoothings via a series of moves. As our examples demonstrate, this gives a useful strategy to create interesting 4-manifolds in certain situations. These tools may have further applications in the study of complex curves and surfaces in symplectic 4-manifolds.

From the de Jong-van Straten correspondence and non-existence of the corresponding QHD smoothings, it follows that the combinatorial arrangements producing our $\mathbb{Q H D}$ fillings cannot be realized by analytic deformations of the corresponding curve germs. We do not know how to prove this deformation non-realizability by a direct argument for analytic deformation of plane curves; it would be interesting to investigate this phenomenon further.

Given the significance of rational blowdown in 4-manifold topology, a natural question is whether our new rational blowdown can be used to construct any interesting exotica. So far we have not been able to produce anything novel. However, we can, for example, embed the corresponding symplectic plumbing into an elliptic fibration and use standard techniques to obtain some basic examples of exotic manifolds.

We have tried to make the paper reasonably self-contained by outlining the de Jong-van Straten construction as well as the symplectic analog of [PS25] in Section 2. Section 3 describes braided wiring diagrams with tangencies, Section 4 gives a number of boundary-preserving moves on such diagrams. In Section 5, we use these moves to construct the arrangements that yield unexpected Stein fillings for graphs $G_{k, 1}$. We treat this case first for expository reasons: the diagrams are smaller and easier to follow, and we explain all steps in detail. The general 2-parameter family is relegated to Section 7 for the persistent reader; we give the diagrammatic moves with brief explanations. In Section 6, we give a basic example of our rational blowdown producing some 4-manifold exotica.

Acknowledgements. This work was initiated by the first two authors during the conference "New structures in low-dimensional topology" in Budapest, July 2024. We are grateful to András Némethi, András Stipsicz, and Luya Wang for helpful conversations. MB is partially supported by the Doctoral Excellence Fellowship Programme (DCEP) funded by the National Research Development and Innovation Fund of the Ministry of Culture and Innovation and the Budapest University of Technology and Economics and by ERC Advanced Grant KnotSurf4d. OP has been partially supported by the NSF grant DMS 2304080. LS has been partially supported by NSF CAREER grant DMS 2042345 and Sloan grant FG 2021-16254.

\section*{2. Picture deformations, DJVS arrangements, and 4-manifold constructions}

We briefly describe de Jong-van Straten's deformation theory for sandwiched singularities. We will use de Jong-van Straten's picture deformations to construct a particular Milnor fiber for the link $\left(Y_{k, n}, \xi_{k, n}\right)$, which we then modify to obtain unexpected fillings. A picture deformation gives an arrangement of algebraic curves; for the modification, we use DJVS immersed disk arrangements introduced in [PS25].

A normal surface singularity ( $X, 0$ ) is sandwiched if there exists an embedding of the tubular neighborhood of the exceptional set of its resolution $\tilde{X}$ into some blowup of $\mathbb{C}^{2}$. One can consider arbitrary resolutions here; for simplicity, we always work with the minimal good resolution, where the exceptional curves are smooth and intersect at transverse double points only. (Note that the minimal resolution
is good for all rational singularities.) A good resolution can be encoded by the dual resolution graph, whose vertices correspond to the irreducible components of the exceptional divisor, and the edges record intersections between the components. Sandwiched singularities can be defined by a combinatorial condition on the dual resolution graph: a graph is sandwiched if it can be augmented by adding new end vertices with self-intersection (-1) in a way that the resulting augmented graph can be blown down to a smooth point at 0 . (The choice of such augmentation is generally not unique.) The $(-1)$ vertices correspond to a distinguished collection of (-1) curves in a blowup of $\mathbb{C}^{2}$ with the embedding of $\tilde{X}$, so that the configuration of these (-1) curves together with the original exceptional set can be completely blown down.

In [JJvS98], the sandwiched singularity is then encoded by an associated singular plane curve germ, as follows. For each distinguished (-1) curve, fix a transverse complex disk $\tilde{C}_{i}$ through a generic point. Blow down the configuration of the exceptional curves of $(X, 0)$ together with these $(-1)$ curves; the image $C_{i}$ of the disk $\tilde{C}_{i}$ under the blowdown is (a germ of) a curve in $\mathbb{C}^{2}$, possibly singular at the origin. We set $C=\cup C_{i}$ and decorate $C$ with a weight $w$, a collection of integers $w_{i}=w\left(C_{i}\right)$. For each $C_{i}$, the number $w_{i}$ is the sum of multiplicities of the intersections of the image of $\tilde{C}_{i}$ with the exceptional curves during the blowdown process. (If $C_{i}$ is smooth, then $w_{i}$ is simply the number of blowdowns that the corresponding component goes through.) The original singularity can be reconstructed from the decorated germ $(C, w)$, where $C=\cup C_{i}$ and $w$ is collection of weights $w_{i}$ : the corresponding blowups recover the embedding of the tubular neighborhood of the exceptional set of the resolution given by $G$ into some blowup of $\mathbb{C}^{2}$.

Figure 2 shows the augmented graph, the blowdown process, and the resulting decorated germ for the graph $G_{0,1}$ of Figure 1. Each component $C_{i}$ of the germ is modeled on the cusp $y^{2}=x^{3}$ because the previous steps of the blowdown give a familiar embedded resolution of the cuspidal cubic. We also see that components $C_{i}$ and $C_{j}$ have intersection multiplicity 8 when $i, j=1, \ldots, 6$, and $C_{0}$ and $C_{i}$ have multiplicity of intersection 7 for each $i=1, \ldots, 6$. In general, for the graphs $G_{k, n}$ with $k \geq 0$ we get cusps $C_{1}, \ldots, C_{6+k}$ with decoration $7+k$ and pairwise intersection multiplicity $8+k$ for each pair, and instead of $C_{0}$ we have $n$ cusps $C_{1}^{\prime}, \ldots C_{n}^{\prime}$ with decoration $7+k+n$, with $C_{i}^{\prime} \cdot C_{j}^{\prime}=8+k+n$ for $1 \leq i<j \leq n$ and $C_{j}^{\prime} \cdot C_{i}=7+k$ for $i=1, \ldots, k+6, j=1, \ldots, n$.
Remark 2.1. Strictly speaking, our pictures encode topological rather than analytic data. If we consider the exceptional set of the resolution $\tilde{X}$ as an embedded configuration of complex curves, then, once the augmented graph is fixed, $C$ is a germ of a reducible complex curve in $\mathbb{C}^{2}$ (defined up to analytic equivalence). However, if we only fix the resolution graph and its augmentation, the output of the blowdown process is the topological type of a germ $C$, that is, the link $C \cap S^{3}$ of the plane curve singularity $(C, 0)$ obtained by intersecting the curve $C$ with a small sphere centered at the origin. (This is a link in $S^{3}$ in the knot-theoretic sense, defined up to smooth isotopy.) By [CPP04], the contact link $(Y, \xi)$ of the singularity $(X, 0)$ depends only on the topological type; to generate symplectic fillings, we will only need to know the isotopy class of $C \cap S^{3}$.

De Jong-van Straten's theory describes Milnor fibers of smoothings of a sandwiched surface singularity $(X, 0)$ via picture deformations of the decorated germ.

A picture deformation of a decorated germ $(C, w)$ as above is a 1-parameter small analytic deformation $C^{t}$ equipped with a collection $p$ of marked points (for each $t$ ) such that
\begin{itemize}
\item[] $(\mathrm{C}-1) C^{t}$ is a $\delta$-constant deformation,
\item[] (C-2) the only singularities of the curve $C^{t}$ are transverse multiple points for all $t>0$,
\item[] (C-3) the marked points $p_{j}$ are chosen on $C^{t}$, so that each self-intersection and each intersection
\end{itemize} between two irredicible components is marked; additionally, there may be free marked points on each $C_{i}$ away from the intersections,
\begin{itemize}
\item[] (C-4) each component $C_{i}^{t}$ carries $w_{i}$ marked points, counted with multiplicity of intersection.
\end{itemize}

In [dJvS98], $p$ is the deformation of the corresponding multiplicity scheme, originally concentrated at 0 and reduced for $t>0$, but we will think of the marked points simply as a set.

The $\delta$-constant property implies that the deformation preserves the branches, and each $C_{i}^{t}$ is an immersed disk in a Milnor ball $B$, [Tei76]. With the appropriate choice of coordinates, we can assume

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/e81a01d2-897b-4840-89f5-84d3bbdef6cc-05.jpg?height=1242&width=1512&top_left_y=292&top_left_x=288}
\captionsetup{labelformat=empty}
\caption{Figure 2. The decorated germ for the graph $G_{0,1}$. Each component $C_{i}$ of the germ has a cusp singularity modeled on $y^{2}=x^{3}$. The intersection multiplicities are $C_{0} \cdot C_{i}=$ 7 for $i=1, \ldots, 6$, and $C_{i} \cdot C_{j}=8$ for $i, j=1, \ldots, 6$. The weights are as indicated, $w\left(C_{0}\right)=8, w\left(C_{i}\right)=7$ for $i=1, \ldots, 6$.}
\end{figure}
that none of the tangent cones of the branches $C_{i}$ of the decorated germ are vertical and, moreover, all vertical tangencies of the projections $C_{i}^{t} \rightarrow \mathbb{C}_{x}$ are nondegenerate. This means that outside of self-intersections, each projection is a branched covering with simple branch points only; the degree of the covering is the multiplicity of the corresponding branch $C_{i}$ at 0. We fix a good representative of the deformation in a Milnor ball, thought of as the product $B=D_{x} \times D_{y}$ of two coordinate disks, with corners smoothed. All the constructions will take place inside this ball. We will also assume that $C \cap \partial B$ is contained in $\partial D_{x} \times D_{y}$, and think of the link of $C$ as a braid.

In [PS25], the second and third authors introduced immersed disk arrangements that are more general than picture deformations but have similar topological properties. Let $(\Gamma, p)$ be an arrangement of immersed smooth disks $\Gamma=\cup \Gamma_{i}$ in $D_{x} \times D_{y}$, with $\Gamma_{i}=n_{i}(D)$ for an immersion $n_{i}: D \rightarrow D_{x} \times D_{y}$. Let $p=\left\{p_{j}\right\} \subset \Gamma$ be a finite collection of marked points.

We say that $(\Gamma, p)$ is a DJVS immersed disk arrangement if
$(\Gamma-1) \pi_{x} \circ n_{i}: D \rightarrow D_{x}$ is a simple branched covering for each $i$;
$(\Gamma-2)$ All intersections $\Gamma_{i} \cap \Gamma_{k}$ and self-intersections of the components $\Gamma_{i}$ are positive transverse multiple points locally modeled on the intersection of complex lines.
$(\Gamma-3)$ All intersections and self-intersections are marked, and there can be additional free marked points.
$(\Gamma-4)$ Each disk $\Gamma_{i}$ intersects the boundary of $D_{x} \times D_{y}$ transversely, $\Gamma_{i} \cap \partial\left(D_{x} \times D_{y}\right) \subset \partial D_{x} \times \operatorname{Int} D_{y}$, all marked points and branch points are contained in the interior of $D_{x} \times D_{y}$ and their projections to $D_{x}$ are distinct.

The weight $w\left(\Gamma_{i}\right)$ of the component $\Gamma_{i}$ is the number of the marked points on $\Gamma_{i}$, again counted with multiplicity of intersection. (For example, if $p_{j}$ marks a double point of $\Gamma_{j}$, it is counted twice.) We will always assume that $\Gamma_{i}$ is oriented compatibly with the orientation of $D_{x} \subset \mathbb{C}$.

A DJVS arrangement $(\Gamma, p)$ is compatible with the decorated germ $(C, w)$ if the braids $\partial \Gamma$ and $\partial C$ are isotopic in $\partial D_{x} \times \operatorname{Int} D_{y}$, and $w\left(\Gamma_{i}\right)=w\left(C_{i}\right)$ for the corresponding components. Equivalently, we can assume that $\partial \Gamma_{i}=\partial C_{i}$, by using braid isotopy to modify the arrangement $\Gamma$ in the collar neighborhood of the boundary (this modification preserves all the topological data used in Theorem 2.3).

Given a DJVS arrangement $(\Gamma, p)$, we construct a smooth 4-manifold with boundary $W_{(\Gamma, p)}$ : blow up the ball $B$ at all the marked points $p_{j}$ and take the complement of the tubular neighborhoods of the strict transforms $\tilde{\Gamma}_{i}$ in $B \#_{n} \overline{\mathbb{C P}}^{2}$,
$$W_{(\Gamma, p)}=\left[\left(D_{x} \times D_{y}\right) \#_{n} \overline{\mathbb{C P}}^{2}\right] \backslash \cup_{i} \nu\left(\tilde{\Gamma}_{i}\right) .$$
By hypothesis $(\Gamma-2)$, the strict transforms can be taken as in the standard complex model, and after the blowup, $\tilde{\Gamma}_{i}$ are disjoint smoothly embedded curves. We say that $W_{(\Gamma, p)}$ is obtained from $(\Gamma, p)$ by the DJVS construction. Our work builds on the following key results.

Theorem 2.2. ([dJvS98]) Every Milnor fiber of a deformation of a sandwiched singularity $(X, 0)$ can be obtained by the DJVS construction from some picture deformation of a fixed decorated germ $(C, w)$ for $(X, 0)$.

Theorem 2.3. ([PS25]) (1) For every DJVS arrangement $(\Gamma, p)$ compatible with $(X, 0)$, the 4-manifold $W_{(\Gamma, p)}$ carries a Stein structure and gives a Stein filling of the contact link $(Y, \xi)$ of $(X, 0)$.
(2) Every minimal symplectic filling of the contact link $(Y, \xi)$ can be obtained by the DJVS construction from some DJVS arrangement compatible with $(C, w)$.

We will only use the easier part (1) of Theorem 2.3 in this paper: the unexpected QHD fillings will be constructed from appropriate DJVS arrangements.

Homological invariants of $W_{(\Gamma, p)}$ can be easily computed from the combinatorics of the arrangement:
$$b_{1}=0, \quad b_{2}=\#(\text { marked points })-\#(\text { disks }) .$$
Indeed, it is not hard to see that $H_{1}\left(W_{\Gamma, p}\right)$ is generated by loops around $\tilde{\Gamma}_{i}$ 's, $H_{2}(W)$ can be identified with the kernel of the incidence map $\mathcal{I}: \mathbb{Z}\left\langle p_{j}\right\rangle \rightarrow \mathbb{Z}\left\langle\Gamma_{i}\right\rangle$, and $H_{1}(W)$ is the cokernel of this map. We have $b_{1}=0$ because $W$ consists of 1- and 2-handles only, and $b_{1}(Y)=0$ for the link $Y=\partial W$ since the singularity is rational, c.f. [dJvS98, Theorem 5.2], [PS23, Section 6.1]. Thus, to produce a QHD filling, the arrangement $(\Gamma, p)$ must have the number of marked points matching the number of components $\Gamma_{i}$; this is rare, since typically an arrangement $\Gamma$ has a much larger number of marked points than components.

To illustrate the discussion, we describe the Milnor fiber of one of the smoothings of the singularities in our family. Consider the germ $C$ of Figure 2 and take its Scott deformation, constructed iteratively as follows. We blow up at the singular point at the origin, perform a small deformation of the strict transform so that its singularities become disjoint from the exceptional curve $E$, and the branches of the strict transforms are transverse to $E$ (equivalently, we can think of this as "shifting" the exceptional curve $E$ off the singularity in the strict transform), and then blow down $E$ to get a deformed curve $C^{\prime}$ in $\mathbb{C}^{2}$. As a result, the curve $C^{\prime}$ has a new transverse multiple point as well as the collection of singularities occurring on the strict transform of $C$ in the blowup of $\mathbb{C}^{2}$ at $p$. The procedure is repeated until all the singularities at the given stage are transverse multiple points. See [JJvS98, A'C75] for details, including the explanation why this procedure can be actually realized by a 1-parameter deformation. Figure 3 illustrates the Scott deformation of our decorated germ from Figure 2. The marked points on the picture deformation include all the intersections as well as the free points to match the weights on the
components of the singular germ $C$. (Decorated germs look similar for all singularities corresponding to graphs $G_{0, n}$, with the number of intersection points increasing with $n$, although the parity of $n$ affects the order of curve "tails" on the right side of the picture.) For an arbitrary decorated germ, the Scott deformation produces the Artin smoothing under the de Jong-van Straten correspondence, with the Milnor fiber that is diffeomorphic to the minimal resolution of the surface singularity [dJvS98].

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/e81a01d2-897b-4840-89f5-84d3bbdef6cc-07.jpg?height=372&width=780&top_left_y=541&top_left_x=668}
\captionsetup{labelformat=empty}
\caption{Figure 3. The Scott deformation of the decorated germ of Figure 2. The blue curve corresponds to $C_{0}$ in the decorated germ. Yellow, orange and red curves show deformations of three of the six curves $C_{1}, \ldots, C_{6}$; each of the other three curves, not pictured, goes through the same intersection points and have one free marked point.}
\end{figure}

Figure 3 shows familar nodal cubics in the real plane, but it is not very useful when one wants to understand the topology of the arrangement in $\mathbb{C}^{2}$. In the next section, we will use braided wiring diagrams with tangencies to encode the arrangements.

The isotopy type of the boundary braid of a given germ (and therefore of any compatible arrangement) can be easily read off from the Puiseux coefficients of the plane curve singularity, [BK86]. For the germ corresponding to the graph $G_{0,1}$ of Figure 1, each component of the boundary braid is a trefoil knot, with the linking number of the knots equal to the intersection multiplicity of the corresponding components $C_{i}$ of $C$. The topological type of the individual components and the pairwise linking numbers uniquely determine the topological type of an algebraic link, see [BK86]. It is also easy to see, by direct inspection of the arrangement, that the Scott deformation of the curve will have the same boundary braid (as it should). However, when we try to construct other disk arrangements with the same boundary braid, it is not easy to manipulate the combinatorics of the arrangement and keep track of its boundary braid directly. In the next two sections, we will develop a diagrammatic approach that will help us describe the curve arrangements and modify them while controlling the boundary braid.

\section*{3. Braided wiring diagrams with tangencies}

Braided wiring diagrams were introduced by Arvola [Arv92] to study complex line arrangements. In [PS25], we adapted these diagrams to encode DJVS arrangements. Away from the $x$-values of transverse (self)-intersections, the projection of a DJVS arrangement to $D_{x}$ is a branched covering with simple branch points. The branch points of the projection correspond to points where a component $\Gamma_{i}$ is tangent to a fiber of $\pi_{x}$. We refer to these points as tangencies; tangencies and intersections are the singular points of $\pi_{x}: \Gamma \rightarrow D_{x}$. The braided wiring diagram of a DJVS arrangement records the intersections and the tangencies of the arrangement, and how they connect to one another, possibly with some braiding of the components in between.

For a DJVS arrangement $\Gamma$, let $q_{1}, \ldots, q_{N} \in D_{x}$ be the images of intersection points and tangencies (branch points) of $\Gamma$ under the projection $\pi_{x}$. Choose an embedded piecewise linear arc $\alpha: I \rightarrow D_{x}$ such that $\alpha\left(t_{1}\right)=q_{1}, \ldots, \alpha\left(t_{N}\right)=q_{N}$ for $0<t_{1}<\cdots<t_{N}<1$ and $\left.\alpha\right|_{\left[t_{i}-\delta, t_{i}+\delta\right]}(t)=\left(t-t_{i}\right)+q_{i}$ runs parallel to the real axis in $D_{x}$ for some sufficiently small $\delta>0$. Then $\pi_{x}^{-1}(\alpha(I)) \cong[0,1] \times \mathbb{C}$, and $\Gamma \cap \pi_{x}^{-1}(\alpha(I))$ is a 1-dimensional braid, except at singular points above $q_{1}, \ldots, q_{N}$. This restriction of $\Gamma$ over the preimage of the arc $\alpha$ is the braided wiring diagram for $\Gamma$. (The diagram depends on the
choice of $\alpha$.) Given a braided wiring diagram, the arrangement $\Gamma$ can be reconstructed, up to isotopy, by connecting the local models for the singular points with the thickened braided portions, see [PS25, Section 4]. The intersection points are modeled on the intersection of complex lines. For tangencies, we fix a local model as in [PS25, Section 4.3]. This involves a choice of perturbation to avoid highly degenerate wiring diagrams. While a different choice of the local model would encode equivalent data, it is important to fix conventions for consistent interpretation of wiring diagrams. Fix $0<\mu \ll \pi / 2$. Our model for a tangency is the complex curve $\left\{(x, y) \in \mathbb{C}^{2} \mid e^{i \mu} x=y^{2}\right\}$ with the tangency of $\pi_{x}$ at the origin. The preimage of the model over the interval in the real $x$-axis includes the singularity and gives the picture for the braided wiring diagram near a tangency, see [PS25, Figure 7]. If there are two nearby tangencies with nested branches, both in these specific models, then a direct inspection of the model shows that the strands in the corresponding wiring diagram are braided in the neighborhood of the tangencies, as shown in Figure 4.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/e81a01d2-897b-4840-89f5-84d3bbdef6cc-08.jpg?height=204&width=511&top_left_y=902&top_left_x=804}
\captionsetup{labelformat=empty}
\caption{Figure 4. For two nearby vertical tangencies on curves with nested real parts as on the left, the wiring diagram has braiding of the strands near the tangencies, as shown. The branches of the same curve are shown by strands of the same color.}
\end{figure}

The boundary braid of $\Gamma$ can be read off from the wiring diagram: after constructing $\Gamma$ from the local models for the singularities and the thickened braids, the braid $\partial \Gamma$ is the restriction of $\Gamma$ over the preimage of the boundary $\partial \nu(\alpha)$ of the tubular neighborhood of the arc $\alpha$. The contribution of each combinatorial element of the diagram (interesection point, tangency, braiding) to the boundary braid can be seen directly from the models. Specifically, when the arc $\alpha$ is a segment of the real line in the $x$-plane, the loop $\partial \nu(\alpha)$ is formed by the pushoffs of $\alpha$ into the domains $\operatorname{Im} x<0$ ("front") and $\operatorname{Im} x>0$ ("back"). The braid monodromy of $\partial \Gamma$ over the loop $\partial \nu(\alpha)$ (traversed counterclockwise) is obtained by composing the inverse of the braid given by the preimage of $\Gamma$ over the pushoff of $\alpha$ in the positive imaginary direction (the back of the diagram) with the braid given by the preimage of $\Gamma$ over the pushoff in the negative imaginary direction (the front of the diagram). By direct inspection, an intersection point in the diagram contributes a positive half-twist on the corresponding strands both to the front and to the inverse of the back portion. (Due to orientations, the contribution to the back is a negative half-twist.) A tangency, with our choice of the local model, contributes a negative half-twist to the back of the diagram (thus a positive half-twist to its inverse) and two parallel strands in the front. The braided part looks the same in the back and the front pushoffs (contributing to the total boundary braid as partial conjugation due to the sign reversal on the back). If the braided wiring diagram has a unique singular point, we recover the total boundary monodromy of a full positive twist for an intersection point of all strands, and a half-positive twist on two strands for a tangency; the "front" and "back" analysis allows us to find the monodromy of a diagram with several singular points and braiding. See [PS25, Section 4.3] for more details and pictures.

We will use the notational convention where the braids and the braided wiring diagrams are read left to right, and the strands are labeled top to bottom. These conventions differ from those in [CS97] but seem to be more common in low-dimensional topology, although there are no standard conventions in the literature.

As a warm-up, we illustrate the above discussion with an example of arrangement that shares some similarities with the arrangements of Figure 3 but is much simpler.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/e81a01d2-897b-4840-89f5-84d3bbdef6cc-09.jpg?height=144&width=1510&top_left_y=324&top_left_x=322}
\captionsetup{labelformat=empty}
\caption{Figure 5. The Scott deformation of the germ of Example 3.1: the real part of the deformed curve (left) and the braided wiring diagram (right). The figure is taken from [PS25].}
\end{figure}

Example 3.1. Consider the Scott deformation $C^{t}$ of a germ $C$ with two irreducible components, each with a simple cusp singularity, intersecting each other with multiplicity 7. Figure 5 shows the real part of the complex curve $C^{t}$ which is the general fiber of the Scott deformation (left), and the corresponding braided wiring diagram (right). Note the intertwined strands in the neighborhood of the two tangencies. Constructing the "back" and "front" pushoff of the wiring diagram as explained above, we can express the boundary braid of the arrangement as [inverse of "back"]["front"], which gives
$$\partial C^{t}=\left[\Delta_{1,4} \sigma_{3}^{3} \sigma_{2} \sigma_{3} \sigma_{1} \sigma_{2}\right]\left[\sigma_{1}^{-1} \sigma_{3}^{-1} \sigma_{3}^{3} \Delta_{1,4}\right]$$
where $\sigma_{i}$ stands, as usual, for the positive half-twist between the $i$-th and the $(i+1)$-th strands, and $\Delta_{1,4}$ is the positive half-twist on all strands $1, \ldots, 4$, and we used the square brackets to emphasize the contributions from the back and the front of the diagram. The reader can write a simpler expression for the (conjugacy class of) this closed braid and verify that it is consistent with the braid one gets from the Puiseux expansion.

We are now ready to analyze the Scott deformation of the germs corresponding to the family of singularities (topologically) encoded by the graphs $G_{k, n}$. We ignore the marked points for the moment, since our goal is to understand the boundary braid. The diagrams in Figures 7 and 8 represent the cases $k=-1$ and $k=0$ : note that the diagrams are slightly different because the order of the strands on the right of the diagram is affected by parity. These diagrams easily generalize to all $k$ odd resp. $k$ even: increasing $k$ to $k+2$ adds two new germ components (that is, four new strands in the diagram) and two new multipoints involving the "bottom" strands of all the components. We hope that the reader is able to see how the patterns in the pictures extend to infinite families.

To be able to write formulas for the diagrams, we introduce notation for certain elements that appear in our examples, see Figure 6. The braiding will be written using the standard braid generators, where $\sigma_{i}$ denotes the positive half-twist between the $i$-th and the $(i+1)$-th strands. (We do not use the word "crossing" to avoid confusion with the intersections.) The multipoint intersection of strands $i, i+1, \ldots, j$ is denoted $\mathrm{I}_{j}^{i}$; we only indicate the first and the last strand since the intersection point involves consecutive strands. For an intersection of only two strands, we also write $\mathrm{I}_{i}=\mathrm{I}_{i+1}^{i}$. We write $\mathrm{X}_{j+1, k}^{i, j}$ for a configuration of double points where parallel strands $i \ldots, j$ intersect parallel strands $j+1, \ldots, k$ in a square grid pattern. (Since the strands are necessarily consecutive, one of the indices is redundant and could be dropped from notation, but we found that the longer notation helps keep track of strands and relations. We will write $\mathrm{X}_{i+1, k}^{i}$ resp. $\mathrm{X}_{j+1}^{i, j}$ when there is only one strand is the top or bottom collection.) The vertical tangency involving the strands $i$ and $(i+1)$ is denoted by $\mathrm{T}_{i}$; this notation only makes sense if the two strands belong to the same component of the germ. We encode the diagrams by words in these elements, written from left to right. Exponents will mean that the subword is repeated the corresponding number of times; for example, $\left(\mathrm{I}_{j}^{i}\right)^{r}$ means that there are $r$ consecutive intersection points involving all strands from $i$ to $j$. With this notation, the diagram of Figure 5 is written as $\mathrm{T}_{2} \sigma_{1}^{-1} \sigma_{3}^{-1} \mathrm{~T}_{2}\left(\mathrm{I}_{3}\right)^{3} \mathrm{I}_{4}^{1}$. In our examples that arise from Scott deformation of germs with cuspidal cubic components, we often see a collection of curves with nearby tangencies, with nested pairs of branches and a particular braiding pattern. We call this pattern a tangency nest and denote it $\mathbb{T}_{j, 2 k+j-1}$ in a braided wiring diagram, with $k$ tangencies spanning strands from $j$ to $2 k+j-1$, see Figure 6. We drop indices and write $\mathbb{T}$ for the tangency nest on all strands. For this

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/e81a01d2-897b-4840-89f5-84d3bbdef6cc-10.jpg?height=696&width=825&top_left_y=316&top_left_x=698}
\captionsetup{labelformat=empty}
\caption{Figure 6. Notation for elements of braided wiring diagrams with tangencies.}
\end{figure}
pattern on $2 n$ strands, we have
$$\mathbb{T}_{1,2 n}=\mathrm{T}_{n} \sigma_{n-1}^{-1} \sigma_{n+1}^{-1} \sigma_{n-2}^{-1} \sigma_{n+2}^{-1} \ldots \sigma_{1}^{-1} \sigma_{2 n}^{-1} \mathrm{~T}_{n} \sigma_{n-1}^{-1} \sigma_{n+1}^{-1} \sigma_{n-2}^{-1} \sigma_{n+2}^{-1} \ldots \sigma_{2}^{-1} \sigma_{2 n-1}^{-1} \ldots \mathrm{~T}_{n} \sigma_{n-1}^{-1} \sigma_{n+1}^{-1} \mathrm{~T}_{n},$$
and the diagram of Figure 5 is $\mathbb{T}\left(\mathrm{I}_{4}^{3}\right)^{3} \mathrm{I}_{4}^{1}$.
Proposition 3.2. The braided wiring diagram on $2(k+7)$ strands representing the Scott deformation of the decorated germ with $m=k+7$ components associated to the graph $G_{k, 1}$ is given by
$$\mathbb{T}_{1,2 m} \mathrm{I}_{2 m-1+\epsilon}^{m+1+\epsilon}\left(\mathrm{I}_{2 m}^{m+1}\right)^{m-4} \mathrm{I}_{2 m}^{1},$$
where $\epsilon=0$ for $k$ odd, $\epsilon=1$ for $k$ even. For $k=-1,0$, the diagrams are shown in Figures 7 and 8 .

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/e81a01d2-897b-4840-89f5-84d3bbdef6cc-10.jpg?height=245&width=769&top_left_y=1783&top_left_x=679}
\captionsetup{labelformat=empty}
\caption{Figure 7. Wiring diagram for the Scott deformation for the germ of the graph $G_{-1,1}$. Here and in subsequent figures, the strands are labeled top to bottom. Strands representing the same irreducible component of the germ are shown in the same color. Diagrams for all odd $k$ follow the same pattern.}
\end{figure}

Proof. This immediately follows the structure of the Scott deformation for the given germs (see Figure 3), with the careful treatment of the braiding near the tangencies. \(\square\)

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/e81a01d2-897b-4840-89f5-84d3bbdef6cc-11.jpg?height=219&width=1343&top_left_y=318&top_left_x=391}
\captionsetup{labelformat=empty}
\caption{Figure 8. Wiring diagram for the Scott deformation for the germ of the graph $G_{0,1}$. Diagrams for all even $k$ follow the same pattern.}
\end{figure}

\section*{4. Boundary-preserving moves on braided wiring diagrams}

To prove Theorem 1.1, we need to find DJVS arrangements that are compatible with the corresponding decorated germs and have the number of marked points equal to the number of disks, see (2.2). If one tries to manipulate the combinatorics of the arrangement directly by drawing pictures, it is difficult to control the boundary monodromy that has to remain fixed for compatibility. We will use a sequence of simple moves, each giving a useful modification of the diagram while preserving the boundary braid of the arrangement. (The marked points will be ignored during the moves; we only add them at the final stage. All intersection points need to be marked, so the number of intersections must not exceed the given weights, but there can be free marked points if the weights are higher).

For complex line arrangements, moves on braided wiring diagrams that preserve the monodromy function on $\pi_{1}\left(\mathbb{C}_{x} \backslash\right.$ singular values) were studied by Cohen-Suciu [CS97]. Some of their moves are Hurwitz-type modifications relating wiring diagrams by different choices of the path $\alpha$ for the same arrangement, although this is not explicit in [CS97]. We will use some of the Cohen-Suciu moves, but generally our moves are different in nature: they can change the combinatorics of the arrangement, fixing only the boundary braid. If two braided wiring diagrams have the same boundary braid we will denote this relation by $=_{\partial}$. Below we describe the moves we use and verify that each move preserves the boundary braid, up to isotopy. (We will only focus on the boundary braid property that we need; stronger properties, such as Hurwitz-type, may hold for some of the moves, but we will not make or verify any stronger claims.)
4.1. Commuting elements, expanding X and $\mathbb{T}$. Clearly, elements $\mathrm{I}, \mathrm{X}, \mathrm{T}, \sigma$ on disjoint subsets of strands commute since the corresponding arrangements are obviously isotopic through a one-parameter family of DJVS arrangements, with the boundary braid in the same isotopy class. In particular,
$$\mathrm{I}_{j}^{i} \mathrm{I}_{l}^{k}=\mathrm{I}_{l}^{k} \mathrm{I}_{j}^{i}, \quad \mathrm{I}_{j}^{i} \mathrm{~T}_{k}=\mathrm{T}_{k} \mathrm{I}_{j}^{i}, \quad \mathrm{I}_{j}^{i} \sigma_{k}=\sigma_{k} \mathrm{I}_{j}^{i},$$
if $i<j<k<l$. We can draw commuting elements in the diagram without specifying their order.
A trivial notational relation expands an element $\mathrm{X}_{j+1, l}^{i, j}$ by separating strands:
$$\mathrm{X}_{j+1, l}^{i, j}=\mathrm{X}_{j+1, l}^{i^{\prime}, j} \mathrm{X}_{i^{\prime}, i^{\prime}+l-j-1}^{i, i^{\prime}-1}=\mathrm{X}_{j+1, l^{\prime}}^{i, j} \mathrm{X}_{l^{\prime}+1, l}^{i+l^{\prime}-j, i+l^{\prime}} .$$
For example, $\mathrm{X}_{m+1,2 m}^{2, m}=\mathrm{X}_{m+1,2 m}^{3, m} \mathrm{X}_{3, m+2}^{2}$ means that the configuration of parallel strands $2, \ldots m$ intersecting parallel strands $m+1, \ldots, 2 m$ is the same as strands $3, \ldots, m$ intersecting $m+1, \ldots, 2 m$ followed by strand 2 intersecting the bottom $m$ strands (which have indices $3, \ldots, m+2$ after crossing the previous strands).

Similarly, we can expand a tangency nest:
$$\mathbb{T}_{1,2 n}=\mathbb{T}_{2,2 n-1} \sigma_{2 n-1}^{-1} \ldots \sigma_{n+1}^{-1} \sigma_{1}^{-1} \ldots \sigma_{n-1}^{-1} \mathrm{~T}_{n} .$$
4.2. Splitting/merging multipoints. A multipoint involving $n$ consecutive strands in the diagram can split in a number of ways. It can split generically into $\binom{n}{2}$ double points, or there can be several multipoints corresponding to the intersection of some subsets of the original set of strands, with other strands intersecting at double points. The inverse move merges two or more multipoints into one. See Figure 9. Note that no braiding is introduced between the intersections when splitting a multipoint.

One can see this using a model given by complexified real lines, or by directly working with braid relations for the front and back braid pushoffs. Correspondingly, when merging multipoints, it is critical that there is no braiding in between the multipoints which could interfere with deforming them to a single multipoint. In our notation, when a multipoint involving strands from $i$ to $k$ splits into a multipoint of intersection of strands from $i$ to $j$ and the other of strands from $j+1$ to $k, i \leq j \leq k$, with the pairs of strands from these different groups meeting at double points:
$$\mathrm{I}_{k}^{i}={ }_{\partial} \mathrm{I}_{j}^{i} \mathrm{I}_{k}^{j+1} \mathrm{X}_{j+1, k}^{i, j}={ }_{\partial} \mathrm{X}_{j+1, k}^{i, j} \mathrm{I}_{i+k-j-1}^{i} \mathrm{I}_{k}^{i+k-j} .$$

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/e81a01d2-897b-4840-89f5-84d3bbdef6cc-12.jpg?height=236&width=1371&top_left_y=688&top_left_x=417}
\captionsetup{labelformat=empty}
\caption{Figure 9. Splitting a multipoint, as in (4.4).}
\end{figure}

When just one strand (top or bottom) is moved off a multipoint, meeting the other strands in double points instead, we have the relation
$$\mathrm{I}_{j}^{i}={ }_{\partial} \mathrm{I}_{j}^{i+1} \mathrm{X}_{i+1, j}^{i}={ }_{\partial} \mathrm{X}_{i+1, j}^{i} \mathrm{I}_{j-1}^{i}={ }_{\partial} \mathrm{I}_{j-1}^{i} \mathrm{X}_{j}^{i, j-1}=_{\partial} \mathrm{X}_{j}^{i, j-1} \mathrm{I}_{i+1}^{j},$$
and similarly
$$\mathrm{I}_{k}^{i}={ }_{\partial} \mathrm{X}_{j+1, k}^{j} \mathrm{I}_{k-1}^{i} \mathrm{X}_{k}^{i+k-j, k-1}$$
for splitting strand $j$ off an intersection multipoint of strands $i$ to $k, i<j<k$. There are other variants for splitting into various partitions of the set of strands.
4.3. Moving multipoints through other lines. Using an isotopy of individual components, we can move a multipoint through a collection of adjacent parallel strands that intersect the strands in the multipoint in double points:
$$\mathrm{I}_{j}^{i} \mathrm{X}_{j+1, k}^{i, j}={ }_{\partial} \mathrm{X}_{j+1, k}^{i, j} \mathrm{I}_{k}^{i+k-j}, \quad \mathrm{I}_{k}^{j+1} \mathrm{X}_{j+1, k}^{i, j}={ }_{\partial} \mathrm{X}_{j+1, k}^{i, j} \mathrm{I}_{i+k-j-1}^{i} .$$
see Figure 10(top). Note how the indices of I and X must match for this move to be possible. This move is modeled by the corresponding move on the complexification of a real line arrangement. Note that the multipoint splittings in the previous subsection are related by a sequence of moves of this type.

We can also switch the order of two multipoints when one involves a subset of strands of the other as in Figure 10(bottom):
$$\mathrm{I}_{j}^{i} \mathrm{I}_{k}^{i}={ }_{\partial} \mathrm{I}_{k}^{i} \mathrm{I}_{k}^{k+i-j}, \quad i<j \leq k .$$
This move can be obtained as a composition of a multipoint splitting, moving multipoint past lines, and merging back (moves (4.4), its inverse, and move (4.7)), or proved directly, cf [CS97].
4.4. Switching self-intersections and tangencies on same strands. We can interchange a tangency with an adjacent intersection between the same two strands in the diagram:
$$\mathrm{I}_{i} \mathrm{~T}_{i}={ }_{\partial} \mathrm{T}_{i} \mathrm{I}_{i},$$
see Figure 11. The boundary monodromy given by $\sigma_{i}^{3}$. More generally, one can switch a full intersection of $2 n$ strands and a tangency nest on these $2 n$ strands,
$$\mathbb{T}_{1,2 n} \mathrm{I}_{2 n}^{1}={ }_{\partial} \mathrm{I}_{2 n}^{1} \mathbb{T}_{1,2 n} .$$
This move is modeled by the Scott deformations of two topologically equivalent germs of $n$ cusps with intersection multiplicity 4; the boundary braid is determined by the topological type of the singularity.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/e81a01d2-897b-4840-89f5-84d3bbdef6cc-13.jpg?height=537&width=1096&top_left_y=324&top_left_x=567}
\captionsetup{labelformat=empty}
\caption{Figure 10. Top: moving multipoints past other lines, as in (4.7). Bottom: switching two multipoints.}
\end{figure}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/e81a01d2-897b-4840-89f5-84d3bbdef6cc-13.jpg?height=425&width=904&top_left_y=1100&top_left_x=604}
\captionsetup{labelformat=empty}
\caption{Figure 11. Swapping self-intersection and tangency, as in 4.9}
\end{figure}
4.5. Moving multipoints through tangencies. We can move an intersection point through a tangency or a tangency nest, in several ways. Move (i) below is a basic version, moves (ii) and (iii) are its generalizations, and moves (iv) and (v) are variants. See Figure 12. These moves are more involved than the previous ones: they introduce additional braiding rather than simply switching the elements of the diagram. Only moves (i) and (ii) will be used in Section 5, the rest are not needed until Section 7. For this type of move, one needs to be careful with various symmetric versions: because of the asymmetry in our chosen tangency model, the braiding is somewhat asymmetric.
(i) Moving a double point up or down through a tangency:
$$\mathrm{T}_{i} \mathrm{I}_{i+1}={ }_{\partial} \sigma_{i+1} \sigma_{i}^{-1} \mathrm{~T}_{i+1} \mathrm{I}_{i}$$
(ii) Moving a multipoint up or down through a tangency nest on the same strands:
$$\mathbb{T}_{1,2 n} \mathrm{I}_{n}^{1}={ }_{\partial} \Delta_{1, n} \Delta_{n+1,2 n}^{-1} \mathbb{T}_{1,2 n} \mathrm{I}_{2 n}^{n+1}$$
where $\Delta_{j, k}$ stands for a positive half-twist on the collection of strands $j, \ldots, k$. We stated the move for the tangency nest on strands $1, \ldots, 2 n$.
(iii) Moving a strand through a tangency nest, with double point intersections:
$$\mathbb{T}_{1,2 n} \mathrm{I}_{2 n} \mathrm{I}_{2 n-1} \ldots \mathrm{I}_{n+1}={ }_{\partial} \sigma_{2 n} \sigma_{2 n-1} \ldots \sigma_{n+1} \sigma_{n}^{-1} \sigma_{n-1}^{-1} \ldots \sigma_{1}^{-1} \mathbb{T}_{1,2 n} \mathrm{I}_{1} \mathrm{I}_{2} \ldots \mathrm{I}_{n} .$$
(iv) Switching the order of a double point and a tangency:
$$\mathrm{T}_{i} \mathrm{I}_{i+1}={ }_{\partial} \mathrm{I}_{i+1} \sigma_{i+1} \mathrm{~T}_{i} \sigma_{i+1}^{-1}$$
(v) Moving a multipoint to the other side of a tangency nest on the same strands:
$$\mathbb{T}_{1,2 n} \mathrm{I}_{n}^{1}={ }_{\partial} \mathrm{I}_{1, n} \Delta_{1, n} \mathbb{T}_{1,2 n} \Delta_{1, n}^{-1}$$

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/e81a01d2-897b-4840-89f5-84d3bbdef6cc-14.jpg?height=1409&width=1160&top_left_y=640&top_left_x=477}
\captionsetup{labelformat=empty}
\caption{Figure 12. Moving multipoints through tangencies and tangency nests: moves (i)-(v).}
\end{figure}

It seems plausible that the moves (i)-(v) can be realized by isotopies of individual components. Move (iv) is a Hurwitz move. However, we only prove a weaker claim that we need: if the local move is performed on a larger arrangement, the elements before and after the move make equivalent contribution into the total boundary braid of the global arrangement, therefore the boundary braid is preserved, up to isotopy. For each move, we write the "front" and "back" boundary braids, as
explained in Section 3, and show that the "front" braid of the left-hand side is isotopic to the "front" of the right-hand side, and the same is true for the "back" braids.

Remark 4.1. Note that the moves $(i)-(v)$ each have a symmetric pair, where the braiding appears on the other side of the equation. This can be seen by concatenating the diagrams with the inverse braid (and removing the braiding on one side by a braid isotopy). For example, for move (i) we multiply equation (4.10) by $\sigma_{i} \sigma_{i+1}^{-1}$ on the left to get
$$\sigma_{i} \sigma_{i+1}^{-1} \mathrm{~T}_{i} \mathrm{I}_{i+1}={ }_{\partial} \mathrm{T}_{i+1} \mathrm{I}_{i} .$$
For moves (iv), (v), it is also useful to observe that $\Delta_{1, n}$ and $\mathrm{I}_{n}^{1}$ commute.
Similarly, by mirroring the proofs along two axes, one gets another symmetric version of the moves. This corresponds to reading the formulas right to left and switching the indices $j \leftrightarrow 2 n-j+1$, where $2 n$ is the number of strands.

Proof of Move (i): The front and back braids for (4.10) are given by
$$\text { front: } \sigma_{i+1}=\sigma_{i+1} \sigma_{i}^{-1} \sigma_{i}, \quad \text { back: } \sigma_{i}^{-1} \sigma_{i+1}^{-1}=\sigma_{i+1} \sigma_{i}^{-1} \sigma_{i+1}^{-1} \sigma_{i}^{-1},$$
see Figure 13. \(\square\)

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/e81a01d2-897b-4840-89f5-84d3bbdef6cc-15.jpg?height=271&width=941&top_left_y=1096&top_left_x=584}
\captionsetup{labelformat=empty}
\caption{Figure 13. Proof of Move (i): the front and back braids of the diagram, before and after sliding a double point past a tangency.}
\end{figure}

Proof of Move (ii): For (4.11), the front braid of the diagram before and after the move is given by front: $\Delta_{1, n}^{-1} \Delta_{n+1,2 n}^{-1} \Delta_{1, n}=\Delta_{1, n} \Delta_{n+1,2 n}^{-1} \Delta_{1, n}^{-1} \Delta_{n+1,2 n}^{-1} \Delta_{n+1,2 n}=\Delta_{n+1,2 n}^{-1}$.
The back braids, before and after the move, are
$$\text { back: } B \Delta_{1, n}^{-1}=\Delta_{1, n} \Delta_{n+1,2 n}^{-1} B \Delta_{n+1,2 n}^{-1} \text {, }$$
where $B=\left(\sigma_{n}^{-1} \sigma_{n-1}^{-1} \ldots \sigma_{1}^{-1}\right) \ldots\left(\sigma_{2 n+1}^{-1} \ldots \sigma_{n}^{-1}\right)$ is the braid where the parallel strands $1, \ldots, n$ cross under the parallel strands $(n+1), \ldots, 2 n$, and the relation above follows from the identities such as $\Delta_{1, n} B=B \Delta_{n+1,2 n}$ (one can slide any braid on the strands $1, \ldots, n$ past $B$ by an isotopy to get the same braid on the strands $n+1, \ldots, 2 n$ on the other side). See Figure 14. \(\square\)

Proof of Move (iii): this can be seen by induction from Move (i) or by comparing the front and back braids directly. We have
$$\text { front: } \Delta_{1, n}^{-1} \Delta_{n+1,2 n}^{-1} \sigma_{2 n-1} \ldots \sigma_{n+1}=\sigma_{2 n-1} \ldots \sigma_{n+1} \sigma_{n}^{-1} \ldots \sigma_{1}^{-1} \Delta_{2, n+1}^{-1} \Delta_{n+2,2 n+1}^{-1} \sigma_{1} \ldots \sigma_{n},$$
where the identity holds because the braid $\sigma_{1} \ldots \sigma_{n}$ represents strand 1 crossing over strands $2, \ldots n+1$, so $\Delta_{2, n+1}^{-1} \sigma_{1} \ldots \sigma_{n}=\sigma_{1} \ldots \sigma_{n} \Delta_{1, n}^{-1}$, and similarly $\Delta_{n+1,2 n}^{-1} \sigma_{2 n-1} \ldots \sigma_{n+1}=\Delta_{n+2,2 n+1}^{-1} \sigma_{2 n-1} \ldots \sigma_{n+1}$. The back braids are examined similarly (the reader should draw a picture). \(\square\)

Proof of Move (iv): this is very similar to Move (i),
$$\text { front: } \sigma_{i+1}=\sigma_{i+1} \sigma_{i+1} \sigma_{i+1}^{-1}, \quad \text { back: } \sigma_{i}^{-1} \sigma_{i+1}^{-1}=\sigma_{i+1}^{-1} \sigma_{i+1} \sigma_{i}^{-1} \sigma_{i+1}^{-1},$$ \(\square\)

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/e81a01d2-897b-4840-89f5-84d3bbdef6cc-16.jpg?height=610&width=958&top_left_y=335&top_left_x=576}
\captionsetup{labelformat=empty}
\caption{Figure 14. Proof of Move (ii): the back (top figure) and the front (bottom figure) braids of the diagram, before and after sliding a multipoint past a tangency nest.}
\end{figure}

Proof of Move (v): using the braid $B$ as in Move (ii), we have
$$\begin{aligned}
\text { front: } & \Delta_{n+1,2 n}^{-1} \Delta_{1, n}^{-1} \Delta_{1, n}=\Delta_{1, n} \Delta_{1, n} \Delta_{1, n}^{-1} \Delta_{n+1,2 n}^{-1} \Delta_{1, n}^{-1} \\
\text { back: } & B \Delta_{1, n}^{-1}=\Delta_{1, n}^{-1} \Delta_{1, n} B \Delta_{1, n}^{-1}
\end{aligned}$$ \(\square\)

Remark 4.2. Note that $\Delta_{1, n} \Delta_{n+1,2 n} B=\Delta_{1,2 n}$, which can also be used to justify the general move of Figure 11
4.6. Moving braiding past other elements. We can move a braid element through an intersection or tangency that involves the corresponding strands. For a generator, we have
$$\sigma_{j} \mathrm{I}_{k}^{i}={ }_{\partial} \mathrm{I}_{k}^{i} \sigma_{i+k-j-1}, \quad i \leq j<k .$$
This is Cohen-Suciu move 5(d), see [CS97]; for a proof in our setting, compare back and front braids before and after.

There is another type of move, for switching a braid element with tangencies; we leave it to the reader since this move will not be needed in this paper.
4.7. Removing braiding at the edges. If there is a braid element at the beginning or the end of a diagram, this element obviously cancels in the closed braid when we compose the inverse of the back braid with the front braid of the diagram. Therefore, we can get rid of any braid element at the edge of the diagram. (In fact, the entire disk arrangement can be isotoped to remove the braiding, cf [CS97, Section 5.6 (1)-(2)].)

\section*{5. QHD fillings via diagrammatic moves}

In this section, we give a proof of Theorem 1.1 for graphs $G_{k, 1}$, postponing the general case until Section 7. Starting with the Scott deformation of the germ corresponding to the family of singularities in Theorem 1.1, we would like to obtain an arrangement with the same boundary braid, such that the number of intersection points equals the number of curves. The latter requirement holds for the combinatorial arrangement where the curve $\Gamma_{0}$ of weight $8+k$ has its double point disjoint from all the other curves, and for each of the remaining curves $\Gamma_{1}, \ldots, \Gamma_{k+6}$, all the other curves go through the double point of every $\Gamma_{i}$ with multiplicity 1 for $i=1, \ldots, k+6$. To generate the immersed disk
arrangement with prescribed combinatorial data and the correct boundary, we use the diagrammatic moves from the previous section. The output of the moves, at the end of the procedure, will be the wiring diagrams of the desired arrangements; these are shown in Figure 16 for $k$ odd and Figure 17 for $k$ even. (The marked points for these DJVS arrangements are the intersection points in the diagram.)

Proof of Theorem 1.1 for $n=1$. The proof consists of presenting a sequence of moves changing the diagrams as required; we give this sequence for $k$ odd. The moves for $k$ even are similar. For a reader willing to accept a proof by picture, the entire proof is in Figure 15 illustrating the moves connecting Figure 7 to Figure 16 for $k=-1$; the pattern extends in a straightforward way to all odd $k$. For a more rigorous argument, we spell out the required moves in formulas below.

By Proposition 3.2, the Scott deformation is given by the diagram
$$\mathbb{T} \mathrm{I}_{2 m-1}^{m+1}\left(\mathrm{I}_{2 m}^{m+1}\right)^{m-4} \mathrm{I}_{2 m}^{1}$$
on $2 m$ strands, with $m=k+7$ even. Use (4.4) to split the multipoint on the right as $\mathrm{I}_{2 m}^{1}=$ $\mathrm{I}_{m-1}^{1} \mathrm{X}_{m, 2 m}^{1, m-1} \mathrm{I}_{m+1}^{1}$, which gives
$$\mathbb{T} \mathrm{I}_{2 m-1}^{m+1}\left(\mathrm{I}_{2 m}^{m+1}\right)^{m-4} \mathrm{I}_{m-1}^{1} \mathrm{X}_{m, 2 m}^{1, m-1} \mathrm{I}_{m+1}^{1},$$
Figure 15(a). For the next step, combine the multipoint $\mathrm{I}_{m-1}^{1}$ with the adjacent strand of double points (the pink strand in Figure 15(a)): $\operatorname{expand} \mathrm{X}_{m, 2 m}^{1, m-1}=\mathrm{X}_{m}^{1, m-1} \mathrm{X}_{m+1,2 m}^{2, m}$ by (4.2) and then replace $\mathrm{I}_{m-1}^{1} \mathrm{X}_{m}^{1, m-1}=\mathrm{I}_{m}^{1}$ by (4.5) to get
$$\mathbb{T} \mathrm{I}_{2 m-1}^{m+1}\left(\mathrm{I}_{2 m}^{m+1}\right)^{m-4} \mathrm{I}_{m}^{1} \mathrm{X}_{m+1,2 m}^{2, m} \mathrm{I}_{m+1}^{1},$$
which equals $\mathbb{T} \mathrm{I}_{2 m-1}^{m+1} \mathrm{I}_{m}^{1}\left(\mathrm{I}_{2 m}^{m+1}\right)^{m-4} \mathrm{X}_{m+1,2 m}^{2, m} \mathrm{I}_{m+1}^{1}$ because the corresponding multipoints commute. Then slide the $(m-4)$ bottom multipoints $\left(\mathrm{I}_{2 m}^{m+1}\right)^{m-4}$ up and combine them, one by one, with the double points on strands $2, \ldots, m-3$ going down: the two multipoints in Figure 15(a) are combined with the purple and blue strands of double points, respectively. More formally, expanding $\mathrm{X}_{m+1,2 m}^{2, m}=$ $\mathrm{X}_{m+1,2 m}^{3, m} \mathrm{X}_{3, m+2}^{2}$, then moving a multipoint past parallel strands by (4.7), and merging it with double points by (4.5) gives
$$\mathrm{I}_{2 m}^{m+1} \mathrm{X}_{m+1,2 m}^{2, m}={ }_{\partial} \mathrm{I}_{2 m}^{m+1} \mathrm{X}_{m+1,2 m}^{3, m} \mathrm{X}_{3, m+2}^{2}={ }_{\partial} \mathrm{X}_{m+1,2 m}^{3, m} \mathrm{I}_{m+2}^{3} \mathrm{X}_{3, m+2}^{2}={ }_{\partial} \mathrm{X}_{m+1,2 m}^{3, m} \mathrm{I}_{m+2}^{2},$$
which takes care of the rightmost multipoint. We then repeat this procedure inductively:
$$\begin{aligned}
& \mathbb{T} \mathrm{I}_{2 m-1}^{m+1} \mathrm{I}_{m}^{1}\left(\mathrm{I}_{2 m}^{m+1}\right)^{m-4} \mathrm{X}_{m+1,2 m}^{2, m} \mathrm{I}_{m+1}^{1}={ }_{\partial} \mathbb{T} \mathrm{I}_{2 m-1}^{m+1} \mathrm{I}_{m}^{1}\left(\mathrm{I}_{2 m}^{m+1}\right)^{m-5} \mathrm{X}_{m+1,2 m}^{3, m} \mathrm{I}_{m+2}^{2} \mathrm{I}_{m+1}^{1}={ }_{\partial} \\
& \mathbb{T} \mathrm{I}_{2 m-1}^{m+1} \mathrm{I}_{m}^{1}\left(\mathrm{I}_{2 m}^{m+1}\right)^{m-5} \mathrm{X}_{m+1,2 m}^{4, m} \mathrm{X}_{4, m+3}^{3} \mathrm{I}_{m+2}^{2} \mathrm{I}_{m+1}^{1}={ }_{\partial} \\
& \mathbb{T} \mathrm{I}_{2 m-1}^{m+1} \mathrm{I}_{m}^{1}\left(\mathrm{I}_{2 m}^{m+1}\right)^{m-6} \mathrm{X}_{m+1,2 m}^{4, m} \mathrm{I}_{m+3}^{4} \mathrm{X}_{4, m+3}^{3} \mathrm{I}_{m+2}^{2} \mathrm{I}_{m+1}^{1}={ }_{\partial} \\
& \mathbb{T} \mathrm{I}_{2 m-1}^{m+1} \mathrm{I}_{m}^{1}\left(\mathrm{I}_{2 m}^{m+1}\right)^{m-6} \mathrm{X}_{m+1,2 m}^{4, m} \mathrm{I}_{m+3}^{3} \mathrm{I}_{m+2}^{2} \mathrm{I}_{m+1}^{1}={ }_{\partial} \cdots={ }_{\partial} \\
& \mathbb{T} \mathrm{I}_{2 m-1}^{m+1} \mathrm{I}_{m}^{1} \mathrm{X}_{m+1,2 m}^{m-2, m} \mathrm{I}_{2 m-3}^{m-3} \cdots \mathrm{I}_{m+2}^{2} \mathrm{I}_{m+1}^{1} .
\end{aligned}$$
The resulting diagram is in Figure 15(b). The multipoints $\mathrm{I}_{m}^{1}$ and $\mathrm{I}_{2 m-1}^{m+1}$ commute, so we rewrite
$$\mathbb{T} \mathrm{I}_{m}^{1} \mathrm{I}_{2 m-1}^{m+1} \mathrm{X}_{m+1,2 m}^{m-2, m} \mathrm{I}_{2 m-3}^{m-3} \ldots \mathrm{I}_{m+2}^{2} \mathrm{I}_{m+1}^{1}$$
and use (4.11) to slide $\mathrm{I}_{1, m}$ down past the tangency nest to get
$$\Delta_{1, m} \Delta_{m+1,2 m}^{-1} \mathbb{T} \mathrm{I}_{2 m}^{m+1} \mathrm{I}_{2 m-1}^{m+1} \mathrm{X}_{m+1,2 m}^{m-2, m} \mathrm{I}_{2 m-3}^{m-3} \ldots \mathrm{I}_{m+2}^{2} \mathrm{I}_{m+1}^{1},$$
shown in Figure 15(c). Next, we move strand $(m+1)$ from $\mathrm{I}_{2 m}^{m+1}$ to $\mathrm{I}_{2 m-1}^{m+1}$ by split and then merge moves (4.5),
$$\mathrm{I}_{2 m}^{m+1} \mathrm{I}_{2 m-1}^{m+1}={ }_{\partial} \mathrm{I}_{2 m}^{m+2} \mathrm{X}_{m+2,2 m}^{m+1} \mathrm{I}_{2 m-1}^{m+1}={ }_{\partial} \mathrm{I}_{2 m}^{m+2} \mathrm{I}_{2 m}^{m+1} .$$
The result is the diagram in Figure 15(d),
$$\Delta_{1, m} \Delta_{m+1,2 m}^{-1} \mathbb{T} \mathrm{I}_{2 m}^{m+2} \mathrm{I}_{2 m}^{m+1} \mathrm{X}_{m+1,2 m}^{m-2, m} \mathrm{I}_{2 m-3}^{m-3} \ldots \mathrm{I}_{m+2}^{2} \mathrm{I}_{m+1}^{1}$$

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/e81a01d2-897b-4840-89f5-84d3bbdef6cc-18.jpg?height=1994&width=1338&top_left_y=346&top_left_x=346}
\captionsetup{labelformat=empty}
\caption{Figure 15. The sequence of moves.}
\end{figure}

Now these two multipoints at the bottom can be moved up and combined with strands of double points (red and green strands in the figure). Namely, expand $\mathrm{X}_{m+1,2 m}^{m-2, m}=\mathrm{X}_{m+1,2 m}^{m-1, m} \mathrm{X}_{m-1,2 m-2}^{m-2}$ by (4.2), move the multipoint by (4.7), and merge with double points by (4.5),
$$\mathrm{I}_{2 m}^{m+1} \mathrm{X}_{m+1,2 m}^{m-2, m}={ }_{\partial} \mathrm{I}_{2 m}^{m+1} \mathrm{X}_{m+1,2 m}^{m-1, m} \mathrm{X}_{m-1,2 m-2}^{m-2}={ }_{\partial} \mathrm{X}_{m+1,2 m}^{m-1, m} \mathrm{I}_{2 m-2}^{m-1} \mathrm{X}_{m-1,2 m-2}^{m-2}={ }_{\partial} \mathrm{X}_{m+1,2 m}^{m-1, m} \mathrm{I}_{2 m-2}^{m-2},$$
producing the diagram
$$\Delta_{1, m} \Delta_{m+1,2 m}^{-1} \mathbb{T} \mathrm{I}_{2 m}^{m+2} \mathrm{X}_{m+1,2 m}^{m-1, m} \mathrm{I}_{2 m-2}^{m-2} \mathrm{I}_{2 m-3}^{m-3} \ldots \mathrm{I}_{m+2}^{2} \mathrm{I}_{m+1}^{1}$$
in Figure 15(e). Then similarly move up $\mathrm{I}_{2 m}^{m+2}$ and combine with double points to get the diagram
$$\begin{aligned}
& \Delta_{1, m} \Delta_{m+1,2 m}^{-1} \mathbb{T} \mathrm{X}_{m+1,2 m}^{m} \mathrm{I}_{m}^{m-1} \mathrm{I}_{2 m-2}^{m} \mathrm{I}_{2 m-2}^{m-2} \mathrm{I}_{2 m-3}^{m-3} \mathrm{I}_{m+2}^{2} \mathrm{I}_{m+1}^{1}={ }_{\partial} \\
& \Delta_{1, m} \Delta_{m+1,2 m}^{-1} \mathbb{T} \mathrm{I}_{m+1}^{m} \mathrm{X}_{m+2,2 m}^{m+1} \mathrm{I}_{m}^{m-1} \mathrm{I}_{2 m-1}^{m} \mathrm{I}_{2 m-2}^{m-2} \mathrm{I}_{2 m-3}^{m-3} \ldots \mathrm{I}_{m+2}^{2} \mathrm{I}_{m+1}^{1}
\end{aligned}$$
in Figure 15(f). In this last figure, the strands $m$ and $m+1$ have a tangency and an adjacent intersection, and we can use move (4.9). To write this in formulas, separate the innermost tangency from the tangency nest:
$$\mathbb{T}={ }_{\partial} \mathbb{T}_{2,2 m-1} \sigma_{1}^{-1} \ldots \sigma_{m-1}^{-1} \sigma_{2 m-1}^{-1} \ldots \sigma_{m+1}^{-1} \mathrm{~T}_{m}={ }_{\partial} \mathbb{T}_{2,2 m-1} \sigma_{\text {top }}^{-1} \sigma_{\text {bot }}^{-1} \mathrm{~T}_{m},$$
where we introduced notation $\sigma_{\text {top }}^{-1}$ and $\sigma_{\text {bot }}^{-1}$ to shorten the formulas. Then after move (4.9), we get the diagram
$$\Delta_{1, m} \Delta_{m+1,2 m}^{-1} \mathbb{T}_{2,2 m-1} \sigma_{t o p}^{-1} \sigma_{b o t}^{-1} \mathrm{I}_{m+1}^{m} \mathrm{~T}_{m} \mathrm{X}_{m+2,2 m}^{m+1} \mathrm{I}_{m}^{m-1} \mathrm{I}_{2 m-1}^{m} \mathrm{I}_{2 m-2}^{m-2} \mathrm{I}_{2 m-3}^{m-3} \ldots \mathrm{I}_{m+2}^{2} \mathrm{I}_{m+1}^{1}$$
shown in Figure 15(g). The elements $\mathrm{X}_{m+2,2 m}^{m+1}$ and $\mathrm{I}_{m}^{m-1}$ commute, so we rewrite $\mathrm{T}_{m} \mathrm{X}_{m+2,2 m}^{m+1} \mathrm{I}_{m}^{m-1}=\partial$ $\mathrm{T}_{m} \mathrm{I}_{m}^{m-1} \mathrm{X}_{m+2,2 m}^{m+1}$ and then slide the intersection point $\mathrm{I}_{m}^{m-1}$ down past the tangency $\mathrm{T}_{m}$ by (4.10) to get the diagram
$$\begin{aligned}
& \Delta_{1, m} \Delta_{m+1,2 m}^{-1} \mathbb{T}_{2,2 m-1} \sigma_{\text {top }}^{-1} \sigma_{\text {bot }}^{-1} \mathrm{I}_{m+1}^{m} \sigma_{m-1} \sigma_{m}^{-1} \mathrm{~T}_{m-1} \mathrm{I}_{m+1}^{m} \mathrm{X}_{m+2,2 m}^{m+1} \\
& \quad \mathrm{I}_{2 m-1}^{m} \mathrm{I}_{2 m-2}^{m-2} \mathrm{I}_{2 m-3}^{m-3} \ldots \mathrm{I}_{m+2}^{2} \mathrm{I}_{m+1}^{1}{ }_{e}{ }_{\partial} \\
& \Delta_{1, m} \Delta_{m+1,2 m}^{-1} \mathbb{T}_{2,2 m-1} \sigma_{\text {top }}^{-1} \sigma_{\text {bot }}^{-1} \mathrm{I}_{m+1}^{m} \sigma_{m-1} \sigma_{m}^{-1} \mathrm{~T}_{m-1} \mathrm{X}_{m+1,2 m}^{m} \mathrm{I}_{2 m-1}^{m} \mathrm{I}_{2 m-2}^{m-2} \mathrm{I}_{2 m-3}^{m-3} \ldots \mathrm{I}_{m+2}^{2} \mathrm{I}_{m+1}^{1}
\end{aligned}$$
in Figure 15(h). Finally, use (4.5) to combine the remaining strand of double points with the adjacent multipoint, $\mathrm{X}_{m+1,2 m}^{m} \mathrm{I}_{2 m-1}^{m}=\mathrm{I}_{2 m}^{m}$, which gives the diagram
$$\Delta_{1, m} \Delta_{m+1,2 m}^{-1} \mathbb{T}_{2,2 m-1} \sigma_{t o p}^{-1} \sigma_{b o t}^{-1} \mathrm{I}_{m+1}^{m} \sigma_{m-1} \sigma_{m}^{-1} \mathrm{~T}_{m-1} \mathrm{I}_{2 m}^{m} \mathrm{I}_{2 m-2}^{m-2} \mathrm{I}_{2 m-3}^{m-3} \ldots \mathrm{I}_{m+2}^{2} \mathrm{I}_{m+1}^{1}$$
shown in Figure 16. When all intersection points are marked, this final diagram satisfies the combinatorial condition (2.2), as desired, and therefore produces a QHD filling via the DJVS construction. The diagram can be slightly simplified to
$$\mathbb{T}_{2,2 m-1} \sigma_{t o p}^{-1} \sigma_{b o t}^{-1} \mathrm{I}_{m+1}^{m} \sigma_{m-1} \sigma_{m}^{-1} \mathrm{~T}_{m-1} \mathrm{I}_{2 m}^{m} \mathrm{I}_{2 m-2}^{m-2} \mathrm{I}_{2 m-3}^{m-3} \ldots \mathrm{I}_{m+2}^{2} \mathrm{I}_{m+1}^{1}$$
by removing the braiding in the beginning, see subsection 4.7.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/e81a01d2-897b-4840-89f5-84d3bbdef6cc-19.jpg?height=243&width=1338&top_left_y=2054&top_left_x=393}
\captionsetup{labelformat=empty}
\caption{Figure 16. The pattern for arrangements producing a $\mathbb{Q H D}$ filling for $k$ odd $(k=-1$ is shown).}
\end{figure}

For $k$ even, a DJVS arrangement with the desired properties in shown in Figure 17. We omit the moves for this case, the final factorization is as follows:
$$\mathbb{T}_{2,2 m-1} \sigma_{b o t}^{-1} \sigma_{t o p}^{-1} \mathrm{I}_{m+1}^{m} \sigma_{m} \sigma_{m-1}^{-1} T_{m+1} \mathrm{I}_{m+1}^{1} \mathrm{I}_{m+3}^{3} \ldots \mathrm{I}_{2 m}^{m} .$$
As for $k$ odd, one of the moves slides an intersection point past a tangency nest, adding some braiding at the beginning of the diagram. To simplify the picture, we gave an equivalent diagram with this braiding removed.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/e81a01d2-897b-4840-89f5-84d3bbdef6cc-20.jpg?height=217&width=1474&top_left_y=647&top_left_x=327}
\captionsetup{labelformat=empty}
\caption{Figure 17. The pattern for arrangements producing a $\mathbb{Q H D}$ filling for $k$ even ( $k=0$ is shown).}
\end{figure}

\section*{6. Constructing exotic 4-manifolds with new rational blowdowns}

Our new rational blowdown can in principle be used to create exotic 4-manifolds in the same way as the classical rational blowdown, although we have yet to find any interesting exotica that cannot be constructed by classical means. To give a very basic example, we show how the configuration of spheres corresponding to our blowdown graph can be found in a blowup of $E(3)$. We will use an elliptic fibration that has an $I_{7}$ fiber; recall that this fiber is formed by a cyclic chain of seven 2-spheres, $S_{1}, \ldots, S_{7}$, such that $S_{i}$ and $S_{j}$ intersect transversely at one point iff $i=j \pm 1 \bmod 7$, and are disjoint for distinct $i, j$ otherwise. The configuration corresponding to $G_{0,1}$ will be formed by (the strict transforms of) a linear chain of 5 spheres $S_{1}, \ldots S_{5}$ in the $I_{7}$ fiber together with two disjoint sections, one of them intersecting $S_{3}$ and the other $S_{4}$ at a generic point. Additionally, we will need a third section disjoint from the above configuration (and intersecting $S_{7}$ at a generic point). This is provided by the next lemma:

Lemma 6.1. There is an elliptic fibration $E(3)$ that contains a configuration of smoothly embedded spheres shown in Figure 19: a necklace of seven (-2) spheres forming an $I_{7}$ fiber, and two disjoint sections that intersect two adjacent spheres in the necklace. Further, we can find a fibration as above with an $I_{2}$ fiber and a third section that is disjoint from the other two and intersects the $I_{7}$ fiber at another prescribed sphere.

The spheres in the configuration can be assumed to be symplectic with respect to a compatible symplectic structure on $E(3)$.