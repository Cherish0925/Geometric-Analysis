# Hyperbolic four-manifolds with one cusp

- Category: papers
- Identity: doi:10.1007/s00039-013-0247-2
- Content status: fulltext_ok

---

---
source_file: 1303_6122.pdf
converter: mathpix
format: mmd
---

\title{
HYPERBOLIC FOUR-MANIFOLDS WITH ONE CUSP
}

\author{
ALEXANDER KOLPAKOV AND BRUNO MARTELLI
}

\begin{abstract}
We introduce an algorithm which transforms every fourdimensional cubulation into an orientable cusped finite-volume hyperbolic four-manifold. Combinatorially distinct cubulations give rise to topologically distinct manifolds.

Using this algorithm we construct the first examples of finite-volume hyperbolic four-manifolds with one cusp. More generally, we show that the number of $k$-cusped hyperbolic four-manifolds with volume $\leqslant V$ grows like $C^{V \ln V}$ for any fixed $k$. As a corollary, we deduce that the 3-torus bounds geometrically a hyperbolic manifold.
\end{abstract}

\section*{Introduction}

By Margulis' Lemma, a finite-volume complete hyperbolic $n$-manifold $M^{n}$ has a finite number of ends called cusps, each of which is diffeomorphic to $N^{n-1} \times[0,+\infty)$ for a certain closed connected flat $(n-1)$-manifold $N^{n-1}$.

In dimension three, we may construct cusped hyperbolic manifolds in various ways, for instance by removing a knot or link complement from $S^{3}$. There are essentially two different techniques to prove that a link complement is hyperbolic: by decomposing it into geodesic ideal hyperbolic polyhedra, or by checking that the manifold does not contain an immersed essential surface with $\chi \geqslant 0$ and thus invoking geometrisation. The first method was used by Thurston in his notes [19], where he constructed various hyperbolic 3-manifolds with an arbitrary number of cusps. The computer program SnapPy [6] may be used to check the hyperbolicity of any link with a reasonable number of crossings.

In higher dimensions, constructing hyperbolic manifolds is more complicated. Due to the absence of a geometrisation theorem of any kind, the hyperbolic structure on a smooth manifold needs to be established explicitly, and this is typically done either by arithmetic methods or by assembling geodesic polyhedra. The largest known census of cusped hyperbolic 4-manifolds is the list produced by J. Ratcliffe and S. Tschantz [17] which contains 1171 distinct manifolds, all obtained by pairing isometrically the faces of the ideal hyperbolic 24-cell: these manifolds have either 5 or 6 cusps.

\footnotetext{
The first named author is supported by the SNSF researcher scholarship PBFRP2-145885 and the SNSF project "Discrete hyperbolic geometry" no. 200020-144438/1. The second named author was supported by the Italian FIRB project "Geometry and topology of low-dimensional manifolds", RBFR10GHHH.
}

We construct here the first example of a finite-volume hyperbolic fourmanifold having only one cusp. One of the motivations for this work is a result by D. Long and A. Reid [12] which shows that, amongst the six diffeomorphism types of orientable flat 3-manifolds, at least two of them cannot be cusp sections of a single-cusped four-manifold (but they are sections in some multi-cusped one [14]). The authors then asked [12, 13] whether any single-cusped hyperbolic manifold exists in dimension $n \geqslant 4$. The techniques introduced in the present paper answer this question in the affirmative if the dimension is $n=4$, but are not applicable in higher dimensions. We note that by a recent result of M. Stover [18] there are no single-cusped hyperbolic arithmetic orbifolds in dimension $n \geqslant 30$.

In the present paper, we show that there are plenty of single-cusped hyperbolic four-manifolds, and more generally of hyperbolic four-manifolds with any given number $k \geqslant 1$ of cusps. Let $\rho_{k}(V)$ be the number of pairwise non-homeomorphic orientable hyperbolic four-manifolds with $k$ cusps and volume at most $V$. The main result is the following.

Theorem 0.1. For every integer $k \geqslant 1$ there are two constants $C>1$, $V_{0}>0$ such that $\rho_{k}(V)>C^{V \ln V}$ for all $V>V_{0}$.

Let $\rho(V)$ be the total number of hyperbolic four-manifolds with volume at most $V$ : it was proved in [4] that $C_{1}^{V \ln V}>\rho(V)>C_{2}^{V \ln V}$ for some constants $C_{1}>C_{2}>1$.

Following P. Ontaneda [16], we say that a flat manifold bounds geometrically a hyperbolic manifold if it is diffeomorphic to a cusp section of some single-cusped hyperbolic manifold. By analysing the cusp shapes we deduce the following corollary.

Corollary 0.2. The 3-torus bounds geometrically a hyperbolic manifold.

In fact, Ontaneda has proved that every flat manifold bounds geometrically a negatively pinched Riemannian manifold [16], but Long and Reid showed that at least two among the six orientable flat 3-manifolds cannot bound a hyperbolic manifold [12]. As we said above, the 3-torus is the first example of a connected flat manifold of dimension $n \geqslant 3$ that bounds a hyperbolic manifold.

The proof of Theorem 0.1 is constructive and proceeds as follows. The ideal hyperbolic 24-cell $\mathscr{C}$ is a well-known ideal right-angled four-dimensional hyperbolic polytope with 24 facets and 24 ideal vertices: each facet is a regular ideal octahedron. The 24 facets are naturally divided into three sets of 8 facets each, which we colour correspondingly in green, red and blue. We produce four identical copies $\mathscr{C}_{11}, \mathscr{C}_{12}, \mathscr{C}_{21}$ and $\mathscr{C}_{22}$ of $\mathscr{C}$ and identify the

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/e1f9552b-732f-4160-b413-dfbf4a46503f-03.jpg?height=357&width=359&top_left_y=406&top_left_x=883}
\captionsetup{labelformat=empty}
\caption{Figure 1. The minimally twisted chain link with 6 components. Its complement is tessellated by four regular ideal octahedra. The block $\mathscr{B}$ has eight geodesic boundary components, each isometric to this hyperbolic link complement.}
\end{figure}
corresponding red and blue facets as described by the pattern below:
![](https://cdn.mathpix.com/cropped/e1f9552b-732f-4160-b413-dfbf4a46503f-03.jpg?height=206&width=236&top_left_y=1109&top_left_x=945)
That is, we identify the red facets "horizontally" and the blue facets "vertically". The resulting object is a four-dimensional complete hyperbolic manifold $\mathscr{B}$ with non-compact geodesic boundary. The geodesic boundary is formed by the $4 \times 8=32$ green facets which were left un-paired and has eight components, each isometric to a well-known cusped hyperbolic three-manifold: the complement of the chain link shown in Fig. 1.

The block $\mathscr{B}$ has eight boundary components and 24 cusps, each diffeomorphic to $S^{1} \times S^{1} \times[0,1] \times[0,+\infty)$ : this is a four-dimensional analogue of the annular cusps arising in dimension three. It turns out that $\mathscr{B}$ looks combinatorially much alike as a four-dimensional hypercube $H$ : the eight boundary components correspond to the facets of $H$ and the 24 cusps correspond to the 24 two-dimensional faces of $H$. This combinatorial correspondence preserves all the geometric adjacencies.

As usual, we define a four-dimensional cubulation as the combinatorial data that consists of $n$ (four-dimensional) hypercubes and an isometric pairing of the resulting $8 n$ facets. Having noticed that $\mathscr{B}$ looks like a hypercube, we may transform every cubulation into an orientable complete finite-volume cusped hyperbolic four-manifold by substituting every hypercube with an instance of $\mathscr{B}$ and glueing the geodesic boundaries as described by the combinatorics of the facet pairing. This construction was inspired by a similar algorithm introduced in [5], which transforms a triangulation into a hyperbolic 3-manifold. We have constructed a map
$$\{\text { cubulations }\} \longrightarrow\left\{\begin{array}{l}
\text { orientable complete finite }- \text { volume } \\
\text { cusped hyperbolic four }- \text { manifolds }
\end{array}\right\} .$$

Various informations on the topology and geometry of the resulting hyperbolic four-manifold $M$ can be derived directly from the cubulation. The volume of $M$ is $\frac{16 n}{3} \pi^{2}$ where $n$ is the number of hypercubes in the cubulation. The cusps of $M$ may be recovered as follows: the facet-pairings in the cubulation induce a partition of the $24 n$ two-dimensional faces into cycles, and every cycle corresponds to a cusp. Therefore, in order to construct a hyperbolic four-manifold with one cusp we only need to construct a cubulation where all two-dimensional faces become identified (shortly: a cubulation with only one 2-face). This can be done with a single hypercube.

The Mostow-Prasad rigidity together with the Epstein-Penner canonical decomposition [8] ensure us that combinatorially distinct cubulations produce non-homeomorphic four-manifolds. In other words, the map from the set of cubulation into the set of cusped hyperbolic manifolds described above is injective. Therefore, in order to prove that $\rho_{1}(V) \geqslant C^{V \ln V}$ we only need to show that the number of cubulations with $n$ hypercubes and one 2-face grows faster than $C^{n \ln n}$.

The algorithm that transforms cubulations into hyperbolic manifolds can also be used to construct plenty of closed Riemannian four-manifolds with non-positive sectional curvature or with Einstein metrics. It suffices to construct a cubulation where every cusp is homeomorphic to a 3-torus (this condition is easily checked combinatorially) and then perform a Dehn filling, i.e. glue a copy of $D^{2} \times T^{2}$ at each cusp. The Dehn filling is encoded by a triple $(p, q, r)$ of co-prime integers, and if the triple is sufficiently complicated the resulting manifold admits a non-positively curved metric (by Gromov-Thurston's $2 \pi$ theorem, see [1]) and even an Einstein metric thanks to a theorem of Anderson [1] that extends Thurston's Dehn filling theorem to all dimensions.

Thus, various closed Einstein four-manifolds can be constructed on the basis of a simple combinatorial data: this can be seen as an analogue of presenting closed hyperbolic 3-manifolds as Dehn surgeries along links in $S^{3}$.

Structure of the paper. We introduce the building block $\mathscr{B}$ in Section 1, and then use it in order to transform cubulations into hyperbolic fourmanifolds in Section 2. We apply this construction in Section 3 completing the proof of Theorem 0.1. Finally, we discuss Dehn fillings in Section 4.

\section*{1. The building block}

We define the object which will play the central rôle in the sequel, namely, the building block $\mathscr{B}$. This is a hyperbolic four-dimensional finite-volume manifold with non-compact totally geodesic boundary. In the following section we shall use $\mathscr{B}$ in order to transform any cubulation into a hyperbolic four-manifold.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/e1f9552b-732f-4160-b413-dfbf4a46503f-05.jpg?height=372&width=1154&top_left_y=402&top_left_x=486}
\captionsetup{labelformat=empty}
\caption{Figure 2. The minimally twisted chain link with 6 components (left) is symmetric with respect to a $\pi$-rotation $\iota$ about the dotted circle. This symmetry quotients the hyperbolic link complement $N$ down to the octahedral orbifold (right), obtained from the central picture by contracting each solid arc to a vertex. All the edges in the orbifold on the right have index 2.}
\end{figure}
1.1. The octahedral 3-manifold. Let us start with the description of a cusped hyperbolic 3-manifold whose eight disjoint isometric copies will form the boundary of the block $\mathscr{B}$.

Let $O$ be a regular ideal hyperbolic octahedron. Let us colour the faces of $O$ in blue and red in the chequerboard fashion (thus, every edge of $O$ is adjacent to a red and a blue triangle). Now we take four identical copies $O_{11}, O_{21}, O_{12}$ and $O_{22}$ of $O$ and pair their faces following the rules below:
\begin{itemize}
\item[-] for $i \in\{1,2\}$ we glue each red face of $O_{i 1}$ to the corresponding red face of $\mathscr{C}_{i 2}$;
\item[-] for $j \in\{1,2\}$ we glue each blue face of $O_{1 j}$ to the corresponding blue face of $\mathscr{C}_{2 j}$.
\end{itemize}
The facets are matched by identifying all the pairs of corresponding points in them by means of a hyperbolic isometry. The rules are summarised in the following glueing diagram:
![](https://cdn.mathpix.com/cropped/e1f9552b-732f-4160-b413-dfbf4a46503f-05.jpg?height=211&width=245&top_left_y=1843&top_left_x=941)

This glueing clearly gives rise to a hyperbolic 3-manifold $N$, since the dihedral angle along each edge in $O$ equals $\frac{\pi}{2}$ and the edges are assembled into sets of four elements each. We call $N$ the octahedral manifold. We may define an involution $\iota$ by interchanging $O_{11}$ with $O_{22}$ and $O_{12}$ with $O_{21}$. The quotient orbifold $N / \iota$ may be then described as
$$O_{11} \underset{B}{\stackrel{R}{\rightleftarrows}} O_{12} .$$

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/e1f9552b-732f-4160-b413-dfbf4a46503f-06.jpg?height=443&width=301&top_left_y=410&top_left_x=911}
\captionsetup{labelformat=empty}
\caption{Figure 3. The regular ideal octahedron has a maximal horocusp section that consists of six Euclidean unit squares.}
\end{figure}
It is tessellated by two isometric octahedra, with all the corresponding faces identified. Therefore $N / \iota$ is the octahedral orbifold shown in Fig. 2-(right) with base space $S^{3}$ and singular locus the 1-skeleton of an octahedron (all of its edges are labelled with the index 2). The manifold $N$ is a double cover of that orbifold, and Fig. 2 shows that $N$ is homeomorphic to the complement of the minimally twisted six chain link.

The regular ideal octahedron $O$ has a maximal horocusp section that consists of six Euclidean unit squares, see Fig. 3. The maximal horocusp sections of $O_{11}, O_{12}, O_{21}$ and $O_{22}$ glue together up to a maximal horocusp section of $N$ that consists of six flat tori, each isometric to the square torus $T$ of area 4, constructed by identifying the opposite edges of a 2 × 2 square. The six cusps of $N$ are in a natural 1-1 correspondence with the ideal vertices of the octahedron $O$.

Let $H$ (resp. $V$ ) be the isometry of $N$ that interchanges $O_{i 1}$ with $O_{i 2}$ (resp. $O_{1 j}$ with $O_{2 j}$ ) for all $i$ (resp. $j$ ). The isometries $H$ and $V$ are orientation-reversing and we have $\iota=H \cdot V=V \cdot H$.

Proposition 1.1. Every isometry of $N$ induces an isometry of $O$. Moreover, there is the following exact sequence
$$0 \longrightarrow \mathbb{Z}_{2} \oplus \mathbb{Z}_{2} \longrightarrow \operatorname{Isom}(N) \longrightarrow \operatorname{Isom}(O) \longrightarrow 0,$$
where $\mathbb{Z}_{2} \oplus \mathbb{Z}_{2}$ is generated by $H$ and $V$.
Proof. The four octahedra form the canonical Epstein-Penner decomposition [8, Theorem 3.6] of $N$ and therefore are preserved by any isometry. On the other hand, every isometry $\varphi$ of $O$ is realised by an isometry of $N$ : if $\varphi$ preserves the red-blue colouring, then it suffices to act by $\varphi$ on each $O_{i j}$, if it inverts the colouring then we act by $\varphi$ on each $O_{i j}$ and then exchange $O_{11}$ with $O_{22}$, in order to invert the colourings in the square diagram (1), so that the resulting isometry is well-defined on $N$.

The kernel of the surjective map $\operatorname{Isom}(N) \rightarrow \operatorname{Isom}(O)$ consists of all isometries of $N$ that fix the cusps. These are naturally identified with the
symmetries of the square (1) that preserve the red-blue colouring. Indeed, the kernel is the $\mathbb{Z}_{2} \oplus \mathbb{Z}_{2}$ group generated by $H$ and $V$. \(\square\)

Corollary 1.2. The involution $\iota$ is the unique orientation-preserving nontrivial isometry of $N$ that fixes the cusps.

The action of $\iota$ on each cusp is non-trivial: the cusp shape is a square torus, and $\iota$ acts like a reflection with respect to the centre of the square. Therefore $\iota$ acts as an elliptic involution, whose effect on the homology is multiplication by -1.

Let $T \subset M$ be a torus inside an orientable closed three-manifold. The operation of cutting $M$ along $T$ and re-glueing back using an elliptic involution is sometimes called a mutation: the result of this operation is a new orientable three-manifold, which often is not homeomorphic to $M$. Here we introduce a similar operation for hyperbolic four-manifolds.

Definition 1.3. Let $M$ be an orientable hyperbolic four-manifold which contains a three-dimensional geodesic sub-manifold $N$ isometric to the octahedral manifold. Let us call a mutation of $M$ along $N$ the operation of cutting $M$ along $N$ and re-glueing it back via the involutary isometry $\iota$. The result of this operation is a hyperbolic four-manifold, which is typically non-homeomorphic to the initial one.

Remark 1.4. An embedded cusp section $X$ of $M$ is a collection of threedimensional flat manifolds that intersect the geodesic three-manifold $N$ along six flat tori. A mutation of $M$ along $N$ changes the cusp section $X$ via mutation along these tori, because $\iota$ acts on the cusps like an elliptic involution.
1.2. The 24 -cell. The 24 -cell $\mathscr{C}$ is the only regular polytope in all dimensions $n \geqslant 3$ which is self-dual and not a simplex. It may be defined as the convex hull
$$\mathscr{C}=\operatorname{Conv}(V)$$
of the set $V$ that contains 24 points in $\mathbb{R}^{4}$ obtained by permuting the coordinates of
$$( \pm 1, \pm 1,0,0) .$$
These 24 points are the vertices of $\mathscr{C}$. One checks easily that $\mathscr{C}$ has 24 facets, whose affine supporting hyperplanes are
$$\left\{ \pm x_{i}=1\right\}, \quad\left\{ \pm \frac{x_{1}}{2} \pm \frac{x_{2}}{2} \pm \frac{x_{3}}{2} \pm \frac{x_{4}}{2}=1\right\} .$$
Each facet is a regular octahedron. The dual polytope $\mathscr{C}^{*}$ is therefore the convex hull
$$\mathscr{C}^{*}=\operatorname{Conv}(G \cup R \cup B)$$
where $G$ contains the 8 points obtained by permuting the coordinates of
$$( \pm 1,0,0,0)$$
and $R \cup B$ contains 16 points of the form
$$\left( \pm \frac{1}{2}, \pm \frac{1}{2}, \pm \frac{1}{2}, \pm \frac{1}{2}\right) .$$
It is convenient to partition the latter set into $R \sqcup B$ where $R$ (resp. $B$ ) is the subset of 8 points having an even (resp. odd) number of minus signs.

The facets of $\mathscr{C}$ are regular octahedra in a 1-1 correspondence with the vertices $G \cup R \cup B$ of $\mathscr{C}^{*}$ and we colour them accordingly in green, red and blue. This three-colouring of $\mathscr{C}$ is indeed natural: one can prove that every symmetry of $\mathscr{C}$ induces a permutation of the sets $G, R$ and $B$, and vice versa every permutation may be realised in this way.

Another fact worth mentioning is that $\operatorname{Conv}(R \cup B)$ represents a hypercube and $\operatorname{Conv}(G)$ corresponds to its dual 16-cell, also the same is true after permuting the sets $R, B$ and $G$.

The 24-cell $\mathscr{C}$ is self-dual, i.e. it has a homothetic dual $\mathscr{C}^{*}$. Thus $\mathscr{C}$ has 24 facets, 96 triangular two-dimensional faces, 96 edges and 24 vertices. A facet is a regular octahedron, and (in accordance with the self-duality) each vertex figure is a cube.
1.3. The hypercube. Let us consider the hypercube
$$H=[-1,1]^{4} .$$
We have already noticed that the barycentre of a facet in $H$ is a point in $G$. Thus we get a natural 1-1 correspondence
$$\{\text { facets of } H\} \longleftrightarrow G \longleftrightarrow\{\text { green facets of } \mathscr{C}\} \text {. }$$
The vertices in $V$ are precisely the barycentres of the 2 -dimensional faces in $H$, and thus we get one more $1-1$ correspondence
$$\{2-\text { faces of } H\} \longleftrightarrow V \longleftrightarrow\{\text { vertices of } \mathscr{C}\} .$$

Said in a single phrase, the 24-cell with its green facets and its vertices looks like a hypercube with its (cubic) facets and its (square) 2-faces. This analogy is the core of our construction.

Restricted to the facets, this analogy is just the duality of polyhedra: an octahedral green facet of $\mathscr{C}$ is dual to a cubic facet of $H$, both contained in the same affine hyperplane $x_{i}= \pm 1$. The duality map sends the vertices of the octahedron to the square faces of the cube.

Remark 1.5. Although we will not use it here, we mention that the analogy extends to all the strata of $H$, as follows:
$$\begin{gathered}
\{\text { vertices of } H\} \longleftrightarrow B \cup R \longleftrightarrow\{\text { blue and red facets of } \mathscr{C}\} \\
\{\text { edges of } H\} \longleftrightarrow\left\{\begin{array}{c}
\text { triangular } 2-\text { faces of } \mathscr{C} \\
\text { separating blue and red facets }
\end{array}\right\}
\end{gathered}$$
1.4. The regular ideal hyperbolic 24 -cell. Every $n$-dimensional regular polytope $P$ has a hyperbolic ideal presentation obtained by normalising the coordinates of its vertices so that they lie on the unit sphere $S^{n-1}$ and by interpreting $S^{n-1}$ as the ideal boundary of $\mathbb{H}^{n}$ in Klein's ball model.

Note that the vertex figure of an ideal vertex is a Euclidean regular $(n-1)$ dimensional polytope in some horosphere, whose dihedral angles coincide with the dihedral angles of $P$. For that reason, the ideal regular hyperbolic tetrahedron, cube, octahedron and dodecahedron have Coxeter dihedral angles $\frac{\pi}{3}, \frac{\pi}{3}, \frac{\pi}{2}$ and $\frac{\pi}{3}$, respectively, since their vertex figures are either equilateral triangles or squares.

In what follows we keep denoting by $\mathscr{C}$ the ideal regular hyperbolic 24cell obtained from the Euclidean 24-cell $\mathscr{C}$ defined in Section 1.2 in the way described above. The vertex figure of $\mathscr{C}$ is a Euclidean cube and therefore $\mathscr{C}$ has all dihedral angles $\frac{\pi}{2}$. The 24-cell is the unique regular four-dimensional polytope having cubical vertex figures: the vertex figures of the other five regular four-dimensional polytopes are other Platonic solids, and therefore their dihedral angles are not sub-multiples of $\pi$. Hence $\mathscr{C}$ may be used as a building block in order to construct cusped hyperbolic 4-manifolds, as shown by J. Ratcliffe and S. Tschantz [17].

The boundary of $\mathscr{C}$ consists of 24 regular ideal hyperbolic octahedra, 96 ideal triangular 2-dimensional faces and 96 geodesic edges.

Recall that the octahedral facets of $\mathscr{C}$ are coloured in green, red and blue. We now glue four isometric copies of $\mathscr{C}$ together to produce a hyperbolic 4 -manifold $\mathscr{B}$ with totally geodesic boundary.
1.5. The 24-cell block $\mathscr{B}$. In Section 1.1 we constructed the octahedral hyperbolic 3-manifold $N$ by glueing four copies of the regular ideal octahedron $O$ according to the diagram (1), and by employing the bi-colouring of $O$. Now we construct the building block $\mathscr{B}$ from $\mathscr{C}$ exactly in the same way, using the colouring of its facets.

We pick four isometric copies of $\mathscr{C}$, which we denote by $\mathscr{C}_{11}, \mathscr{C}_{12}, \mathscr{C}_{21}$ and $\mathscr{C}_{22}$, then pair some of their facets as follows:
\begin{itemize}
\item[-] for $i \in\{1,2\}$ we glue each red facet of $\mathscr{C}_{i 1}$ to the corresponding red facet of $\mathscr{C}_{i 2}$;
\item[-] for $j \in\{1,2\}$ we glue each blue facet of $\mathscr{C}_{1 j}$ to the corresponding blue facet of $\mathscr{C}_{2 j}$.
\end{itemize}
The facets are matched by identifying all the pairs of corresponding points in them by means of a hyperbolic isometry. We have glued together the red and the blue facets according to the same square diagram as (1):
![](https://cdn.mathpix.com/cropped/e1f9552b-732f-4160-b413-dfbf4a46503f-09.jpg?height=211&width=236&top_left_y=2221&top_left_x=945)

We denote by $\mathscr{B}$ the resulting topological object. The identifications have paired all the blue and red facets: the un-paired facets of $\mathscr{B}$ are therefore the $4 \times 8=32$ remaining green facets. As above, the fact that $\mathscr{C}$ is right-angled should guarantee that the resulting object is a hyperbolic manifold: now we prove this in detail.

Proposition 1.6. The space $\mathscr{B}$ is a hyperbolic four-manifold with totally geodesic boundary.

Proof. The building block $\mathscr{B}$ is obtained from $\mathscr{C}_{11}, \mathscr{C}_{21}, \mathscr{C}_{12}$ and $\mathscr{C}_{22}$ by an isometric glueing of some pairs of their facets. Let us consider $\mathscr{B}$ as a cell complex. Then the 4- and 3-dimensional strata of $\mathscr{B}$ clearly have a hyperbolic structure (with geodesic boundary). We need to check that the structure extends to any point $x$ lying in the 1- or 2-dimensional stratum $S$, i.e. on an edge or in an ideal triangle.

We may suppose that $x$ lies in a boundary edge or a triangle $S$ of $\mathscr{C}_{11}$. Let us represent $\mathscr{C}_{11}$ in the upper half-space model for $\mathbb{H}^{4}$ and send one of the ideal vertices of $S$ to the infinity. Let $U_{x}$ be a horizontal horosphere passing through $x$. Suppose for now that the fourth coordinate $x_{4}$ of $x$ is big enough, so that the intersection $U_{x} \cap \mathscr{C}_{11}$ is a Euclidean cube $C_{11}$. The point $x$ is either a vertex of or contained in an edge of $C_{11}$.

The faces of the cube $C_{11}$ are coloured in green, red and blue according to the colours of the facets of $\mathscr{C}_{11}$ they are contained in. Opposite faces share the same colour. The block $\mathscr{B}$ contains four isometric copies $C_{11}, C_{12}, C_{21}, C_{22}$ of this cube, which are glued according to the same pattern as above:
![](https://cdn.mathpix.com/cropped/e1f9552b-732f-4160-b413-dfbf4a46503f-10.jpg?height=211&width=243&top_left_y=1547&top_left_x=941)
These cubes form a flat manifold in $\mathscr{B}$, which is isometric to $T \times[0,1]$, where $T$ is the Euclidean square torus of area 4, obtained by identifying the opposite sides of a 2 × 2 square. Therefore $x$ is contained in a hyperbolic cusp based on that flat manifold: the hyperbolic structure clearly extends to $x$. If $x_{4}$ is arbitrary, then the intersection $\mathscr{B} \cap U_{x}$ is only a subset of a cube, but still it looks geometrically like a piece of a cube near $x$ and hence the same argument applies. \(\square\)

During the proof we have described the cusps of $\mathscr{B}$ : they are of the type $T \times[0,1] \times[0,+\infty)$, and they are 24 in total, one for each ideal vertex of $\mathscr{C}$. We will return to that later: first we describe the totally geodesic boundary of $\mathscr{B}$.

Proposition 1.7. The block $\mathscr{B}$ has eight totally geodesic boundary components, each isometric to the octahedral 3-manifold.

Proof. A green octahedral facet $O$ of $\mathscr{C}$ gives rise to four regular ideal octahedra $O_{11}, O_{12}, O_{21}$ and $O_{22}$ glued together in accordance with the square diagram (1), forming an octahedral 3-manifold. The eight green facets of $\mathscr{C}$ produce eight such manifolds. \(\square\)

The eight boundary components naturally correspond to the green facets of $\mathscr{C}$. There is a sequence of $1-1$ correspondences (recall that $H$ is the hypercube):
$$\{\text { facets of } H\} \longleftrightarrow G \longleftrightarrow\{\text { green facets of } \mathscr{C}\} \longleftrightarrow\left\{\begin{array}{c}
\text { (geodesic) boundary } \\
\text { components of } \mathscr{B}
\end{array}\right\}$$
1.6. The maximal cusp section. Finally, we describe the cusps of $\mathscr{B}$. As an ideal regular polytope, the 24 -cell $\mathscr{C}$ has a maximal horosection which meets every boundary octahedron also in a maximal (two-dimensional) horosection. The maximal horosection of an ideal regular octahedron clearly consists of six unit squares. Hence the maximal horosection of $\mathscr{C}$ comprises a unit Euclidean cube $C$ for each vertex $v$ of $\mathscr{C}$.

The faces of $C$ inherit the colour of the facets of $\mathscr{C}$ that they are contained in: every cube is hence coloured in green, red or blue, with opposite faces sharing the same colour. The block $\mathscr{B}$ contains four isometric copies $C_{11}, C_{12}, C_{21}$ and $C_{22}$ of $C$, which are glued in accordance to the usual pattern:
![](https://cdn.mathpix.com/cropped/e1f9552b-732f-4160-b413-dfbf4a46503f-11.jpg?height=211&width=241&top_left_y=1366&top_left_x=941)
These four cubes glue together in order to form the flat manifold $T \times[0,1]$ where $T$ is the Euclidean torus obtained by identifying the opposite sides of a 2 × 2 square. The maximal horosection of $\mathscr{C}$ then gives rise to a maximal horosection of $\mathscr{B}$ made of 24 components (one for each vertex of $\mathscr{C}$ ), each isometric to $T \times[0,1]$.

A horosection isometric to $T \times[0,1]$ bounds a toric cusp homeomorphic to $T \times[0,1] \times[0,+\infty)$ : this is a four-dimensional analogue to the annular cusps that one may find in hyperbolic 3-manifolds with totally geodesic boundary, see fig. 4.

Thus, concerning the geodesic boundary components, we have found a sequence of natural 1-1 correspondences:
$$\{2-\text { faces of } H\} \longleftrightarrow V \longleftrightarrow\{\text { vertices of } \mathscr{C}\} \longleftrightarrow\{\text { (toric) cusps of } \mathscr{B}\} .$$

Summing up, the block $\mathscr{B}$ looks combinatorially like the hypercube $H$, with 8 geodesic boundary components corresponding to the facets of $H$, and 24 toric cusps corresponding to the 2-faces of $H$. (The vertices and edges of $H$ do not play a rôle here.) The correspondence is easily described on the facets: a geodesic boundary component $N$ is made of four copies of an octahedral green facet $O$ of $\mathscr{C}$, which is dual to the corresponding cubic facet

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/e1f9552b-732f-4160-b413-dfbf4a46503f-12.jpg?height=357&width=1192&top_left_y=406&top_left_x=466}
\captionsetup{labelformat=empty}
\caption{Figure 4. A toric cusp in $\mathscr{B}$. Every flat section is $T \times[0,1]$, up to a similarity, where $T$ is the square torus obtained by identifying the opposite sides of a 2 × 2 square. The flat section is tessellated by four cubes: these are four copies of the same vertex cube in $\mathscr{C}$, glued following the pattern as in (1).}
\end{figure}
$C$ of $H$. The six cusps of $N$ correspond to the six vertices of $O$ and hence, by duality, to the square faces of $C$.

The picture is similar to the one given in [5] where the authors constructed a 3-dimensional block combinatorially equivalent to a tetrahedron. In that paper this correspondence was used to transform any 3-dimensional triangulation into an orientable hyperbolic cusped 3-manifold. Here we perform an analogous construction, using hypercubes instead of tetrahedra.

\section*{2. Cubulations}

We now construct orientable hyperbolic four-manifolds by glueing several copies of the block $\mathscr{B}$ along their totally geodesic boundaries. The combinatorial tool which is best suited to describe this procedure is a cubulation.
2.1. The construction. A combinatorial four-dimensional cubulation (here for short, a cubulation) is a data that consists of $n$ copies $H_{1}, \ldots, H_{n}$ of the standard hypercube $H$ together with an isometric pairing of the given $8 n$ facets. An isometric pairing is a partition of the $8 n$ facets into pairs, together with a Euclidean isometry between the two cubes in each pair.

Here we show how a cubulation determines a finite-volume cusped orientable hyperbolic four-manifold, unique up to some well-understood mutations (recall Definition 1.3). Note that we make no requirements on the cubulation: the topological space obtained by glueing the hypercubes $H_{1}, \ldots, H_{n}$ does not need to be a manifold. However, we always assume that it is connected.

First, we pick $n$ isometric copies $\mathscr{B}_{1}, \ldots, \mathscr{B}_{n}$ of the block $\mathscr{B}$. Recall that there is a 1-1 correspondence between the facets (resp., 2-faces) of $H$ and the boundary components (resp., cusps) of $\mathscr{B}$. For every isometric pairing $\varphi: C^{1} \rightarrow C^{2}$ of two cubic facets we construct an isometry $\varphi_{*}: N^{1} \rightarrow N^{2}$ between the corresponding geodesic boundary components. Recall that $N^{h}$
is made of four copies $O_{i j}^{h}$ of an ideal octahedron $O^{h}$ naturally dual to the cube $C^{h}$, for every $h=1,2$. The isometry $\varphi$ defines an isometry $\varphi: O^{1} \rightarrow O^{2}$ according to the duality.

By Proposition 1.1, there are precisely four distinct choices for $\varphi_{*}$. Let $\varphi_{*}^{i j}: N^{1} \rightarrow N^{2}$ be the isometry that sends $O_{11}^{1}$ to $O_{i j}^{2}$ via $\varphi$ and extends (uniquely) to the whole of $N^{1}$. The four choices are
$$\varphi_{*}^{11}, \quad \varphi_{*}^{12}=H \circ \varphi_{*}^{11}, \quad \varphi_{*}^{21}=V \circ \varphi_{*}^{11}, \quad \varphi_{*}^{22}=\iota \circ \varphi_{*}^{11} .$$
Amongst these isometries, two are orientation-preserving and the other two are orientation-reversing; the isometries $\varphi_{*}^{11}$ and $\varphi_{*}^{22}$ are of the same type and differ only by the involution $\iota$, as are the isometries $\varphi_{*}^{12}$ and $\varphi_{*}^{21}$. The following lemma follows from the construction.

Lemma 2.1. The map $\varphi_{*}^{11}$ is orientation-reversing if and only if $\varphi$ is.
Since we want to obtain an orientable four-manifold, we choose one of the two orientation-reversing isometries.

The possible two choices differ exactly by composition with the involution $\iota$. That is, the resulting orientable four-manifold $M$ is uniquely determined, up to mutations along some of the $4 n$ geodesic octahedral manifolds which it contains by construction.

Summing up, we have described an algorithm that transforms every cubulation into a cusped hyperbolic orientable four-manifold, well-defined up to a mutation. We now study these hyperbolic manifolds in detail.
2.2. The hyperbolic four-manifolds. A cubulation $C$ is an isometric pairing of the facets of $n$ hypercubes $H_{1}, \ldots, H_{n}$. Every hypercube has 8 cubic facets and 24 square two-dimensional faces. Every square face is contained in exactly two cubic facets and is hence identified by the pairing to two other square faces (counted with multiplicities).

Consider the abstract set of $24 n$ square faces and connect two of them if they are identified by some pairing: the resulting graph will be a union of cycles. The number $k$ of the resulting cycles and the length of each depend not only on $n$, but on the combinatorial structure of the cubulation as well.

We have described a procedure that transforms the cubulation $C$ into a hyperbolic orientable four-manifold $M$. A considerable amount of information about $M$ can be derived directly from $C$, thanks to the following correspondences that follow immediately from the construction:
\begin{itemize}
\item[-] the $n$ hypercubes in $C$ correspond to the $n$ copies of the block $\mathscr{B}$ in $M$;
\item[-] the $4 n$ pairs of cubes in $C$ correspond to the totally geodesic octahedral 3-manifolds separating two adjacent blocks;
\item[-] the $k$ cycles of squares in $C$ correspond to the $k$ cusps of $M$.
\end{itemize}

For example, the volume formula is a direct consequence:
Proposition 2.2. We have $\chi(M)=4 n$ and $\operatorname{Vol}(M)=\frac{4 \pi^{2}}{3} \chi(M)=\frac{16 n}{3} \pi^{2}$.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/e1f9552b-732f-4160-b413-dfbf4a46503f-14.jpg?height=404&width=900&top_left_y=404&top_left_x=612}
\captionsetup{labelformat=empty}
\caption{Figure 5. A cusp in $M$ is constructed from $T \times[0, h]$ by glueing the two boundary tori via an isometry that preserves the tessellation into four unit squares. In the picture, $h=4$.}
\end{figure}

Proof. The manifold $M$ is tessellated by $n$ isometric copies of $\mathscr{B}$ and hence by $4 n$ copies of the 24 -cell $\mathscr{C}$, which has the volume $\frac{4}{3} \pi^{2}$, see for instance [11]. The formula $\operatorname{Vol}(M)=\frac{4 \pi^{2}}{3} \chi(M)$ holds for any hyperbolic four-manifold [7]. \(\square\)

Note that there exist cusped hyperbolic four-manifolds having any positive Euler characteristic, c.f. [17].

We now turn to the $k$ cusps of $M$, corresponding to the $k$ cycles of squares in $C$. The toric maximal sections of the $\mathscr{B}_{i}$ 's glue together to a maximal cusp section of $M$, determined only by the cubulation. It consists of $k$ components, one for each cycle of squares. As above, let $T$ denote the square torus obtained by identifying the opposite sides of a 2 × 2 Euclidean square. We tessellate $T$ into four unit squares in the obvious way.

Proposition 2.3. Let $X$ be a connected component of the maximal cusp section of $M$, corresponding to a cycle of $h$ square 2-faces. The flat 3manifold $X$ is isometric to
$$T \times[0, h] / \psi$$
where $\psi$ identifies $T \times 0$ and $T \times h$ via an orientation-preserving isometry of $T$ which preserves its tessellation into unit squares. Topologically, the cusp section is homeomorphic to the torus bundle over $S^{1}$ with one of the following monodromies:
$$\left(\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right), \quad\left(\begin{array}{cc}
-1 & 0 \\
0 & -1
\end{array}\right), \quad\left(\begin{array}{cc}
0 & 1 \\
-1 & 0
\end{array}\right) .$$
Proof. The flat manifold $X$ is made of $h$ pieces, each isometric to a toric cusp $T \times[0,1]$ corresponding to some vertex in some block $\mathscr{B}_{i}$. The tessellation into squares of $T$ corresponds to the subdivision of $\mathscr{B}$ into $\mathscr{C}_{i j}$ 's. By construction, every piece is glued to the subsequent one via an isometry that preserves the tessellation: therefore the maximal cusp section looks exactly as required, see Fig. 5.

The manifold $X$ is homeomorphic to a torus bundle over $S^{1}$ with some monodromy $A$ having $\operatorname{det} A=1$. Since $\psi$ preserves the tessellation, it also preserves the pair (meridian, longitude) up to signs and permutation of its components. Therefore $A$ preserves the unordered pair of coordinate axis in $\mathbb{R}^{2}$ and hence is one of the following rotation matrices:
$$\left(\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right), \quad\left(\begin{array}{cc}
-1 & 0 \\
0 & -1
\end{array}\right), \quad\left(\begin{array}{cc}
0 & 1 \\
-1 & 0
\end{array}\right), \quad\left(\begin{array}{cc}
0 & -1 \\
1 & 0
\end{array}\right) .$$
The latter two are conjugate and hence give rise to the same fibred 3manifold, up to homeomorphism. \(\square\)

Corollary 2.4. The flat 3-manifold $X$ has volume $4 h$. The maximal cusp section of $M$ has total volume $4 \times 24 n=96 n$.

Recall that a cusped hyperbolic manifold has an Epstein-Penner canonical decomposition into geodesic ideal polytopes, determined by the choice of a section at each cusp [8].

Proposition 2.5. The Epstein-Penner canonical decomposition of $M$ determined by the maximal cusp section is the decomposition of $M$ into $4 n$ ideal 24-cells.

Proof. The maximal cusp section and the decomposition into ideal 24-cells lift to the tessellation of $\mathbb{H}^{4}$ by ideal 24-cells, together with a horocusp at each ideal vertex. The set of horocusps is invariant under the action of the isometry group of the tessellation. The Epstein-Penner decomposition is formed by interpreting the horocusps as points of the light cone in $\mathbb{R}^{4,1}$ and taking their convex hull. Thus, by symmetry, the resulting decomposition is just the original decomposition into 24-cells. \(\square\)

How can we determine the precise isometry or homeomorphism class of $X$ by looking only at the combinatorics of $C$ ? It is much easier to answer this question when the cubulation is orientable.
2.3. Orientable cubulations. Recall that a cubulation $C$ is an isometric pairing of the $8 n$ facets of $n$ copies $H_{1}, \ldots, H_{n}$ of the hypercube $H$. As usual, the natural orientation of $H$ induces an orientation on all its facets, which is replicated in the copies $H_{1}, \ldots, H_{n}$.

Definition 2.6. The cubulation $C$ is orientable if all the isometric pairings are orientation-reversing.

In our construction, a cubulation $C$ determines a hyperbolic manifold $M$ only up to mutations. When $C$ is orientable, we may resolve this ambiguity as follows: by Lemma 2.1 every glueing map $\varphi_{*}^{11}$ is orientation-reversing, and hence we choose $\varphi_{*}=\varphi_{*}^{11}$ in all our pairings.

This choice turns out to be very convenient for the analysis of the maximal cusp section. Recall that each cusp of $M$ corresponds to a cycle of squares
in $C$, which may be represented as
$$Q_{1} \xrightarrow{\psi_{1}} Q_{2} \xrightarrow{\psi_{2}} \cdots \xrightarrow{\psi_{h-1}} Q_{h} \xrightarrow{\psi_{h}} Q_{1} .$$

Each $Q_{i}$ is a square in some hypercube and each $\psi_{i}$ is an isometry. The composition $\psi=\psi_{h} \circ \cdots \circ \psi_{1}$ is an isometry of a Euclidean square, whose conjugacy class depends only on the cycle and thus is called its monodromy. Since $C$ is orientable, the monodromy $\psi$ is orientation-preserving and is represented (up to a conjugation) by one of the following rotation matrices:
$$\left(\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right), \quad\left(\begin{array}{cc}
-1 & 0 \\
0 & -1
\end{array}\right), \quad\left(\begin{array}{cc}
0 & 1 \\
-1 & 0
\end{array}\right) .$$
As above, let $T$ be the torus obtained by identifying the opposite faces of the $2 \times 2$ square $[-1,1]^{2}$. The matrix $\psi$ acts on $[-1,1]^{2}$ and hence on $T$.

Proposition 2.7. Let $C$ be an orientable cubulation. The cusp section corresponding to a cycle of $h$ squares with monodromy $\psi$ is isometric to $T \times[0, h] / \psi$.

Proof. The cycle of squares (2) corresponds to a cycle of tori
$$T_{1} \xrightarrow{f_{1}} T_{2} \xrightarrow{f_{2}} \cdots \xrightarrow{f_{h-1}} T_{h} \xrightarrow{f_{h}} T_{1} .$$
in the cusp section. Each $T_{i}$ is a square $2 \times 2$ torus. Let $S_{i} \subset T_{i}$ be the unit top-left square in $T_{i}$ : it is naturally dual to the square $Q_{i}$. By our convention, the isometry $f_{i}$ sends $S_{i}$ onto $S_{i+1}$, and it does so via an isometry dual to $\psi_{i}$. Therefore $f=f_{h} \circ \cdots \circ f_{1}$ sends $S_{1}$ to itself via a map conjugate to $\psi$. Therefore the whole of $f$ is conjugate to $\psi$, as required. \(\square\)

Example 2.8. Define an orientable cubulation by taking one hypercube $H$ and pairing its opposite facets via translations. All the parallel square 2-faces are identified: we thus get 6 cycles of 4 squares each; each cycle has trivial monodromy. The resulting hyperbolic manifold $M$ has 6 cusps. Each maximal cusp section is a 3-torus isometric to a right-angled parallelepiped with side lengths 2, 2 and 4 whose opposite faces are identified by translations.

Example 2.9. Define an orientable cubulation by taking two copies $H_{1}$ and $H_{2}$ of the hypercube $H$ and pairing each facet of $H_{1}$ with the corresponding facet of $H_{2}$ via the identity map. We get 24 cycles of square 2-faces, each cycle containing only two squares with trivial monodromy. The resulting hyperbolic manifold $M$ has 24 cusps. Each maximal cusp section is a cubic 3-torus isometric to a cube with side-lengths 2 whose opposite faces are identified by translations. This very symmetric manifold $M$ may be constructed directly by taking eight copies of the triple-coloured 24 -cell $\mathscr{C}$ and glueing
them together according to the following cubic diagram:
![](https://cdn.mathpix.com/cropped/e1f9552b-732f-4160-b413-dfbf4a46503f-17.jpg?height=322&width=329&top_left_y=471&top_left_x=898)

The manifold $M$ is analogous to the octahedral manifold $N$ : indeed we can compute $\operatorname{Isom}(M)$ by applying the same proof of Proposition 1.1. Let $H$ (resp. $V$, and $L$ ) be the isometry of $M$ that interchanges $\mathscr{C}_{i j 1}$ with $\mathscr{C}_{i j 2}$ (resp. $\mathscr{C}_{i 1 j}$ with $\mathscr{C}_{i 2 j}$, and $\mathscr{C}_{1 i j}$ with $\mathscr{C}_{2 i j}$ ). Then $\iota=H \cdot V \cdot L$ is the central involution of the above cubical diagram. We get the following exact sequence:
$$0 \longrightarrow \mathbb{Z}_{2} \oplus \mathbb{Z}_{2} \oplus \mathbb{Z}_{2} \longrightarrow \operatorname{Isom}(M) \longrightarrow \operatorname{Isom}(\mathscr{C}) \longrightarrow 0,$$
where the group $\mathbb{Z}_{2} \oplus \mathbb{Z}_{2} \oplus \mathbb{Z}_{2}$ is generated by $H, V$ and $L$.
2.4. Uniqueness. Two cubulations
$$C=\left\{H_{1}, \ldots, H_{n}\right\}, \quad C^{\prime}=\left\{H_{1}^{\prime}, \ldots, H_{n}^{\prime}\right\}$$
are combinatorially equivalent if there is a sequence of isometries $\left\{\varphi_{i}: H_{i} \rightarrow\right.$ $\left.H_{i}^{\prime}\right\}_{i=1, \ldots, n}$ which transforms all the pairings of $C$ into the pairings of $C^{\prime}$. Below we prove the following theorem.

Theorem 2.10. Non-equivalent cubulations with at least 3 hypercubes produce non-homeomorphic hyperbolic four-manifolds.

A cubulation actually produces a finite set of hyperbolic four-manifolds related by mutations, and the theorem says that any two manifolds produced by non-equivalent cubulations with at least 3 hypercubes are nonhomeomorphic. A similar theorem was proved in [5], and our proof strategy is the same. We do not know if the hypothesis on the number of hypercubes is necessary, but it helps to simplify the arguments. We start by proving a lemma.

Lemma 2.11. Combinatorially non-equivalent cubulations with at least 3 hypercubes produce combinatorially non-equivalent decompositions into ideal 24-cells.

Proof. A cubulation $C$ consisting of $n$ hypercubes gives rise to a hyperbolic four-manifold $M$ (defined up to mutations) which can be decomposed into $4 n$ hyperbolic ideal regular 24-cells. We show that the cubulation $C$ can be recovered (up to combinatorial equivalence) from such a decomposition: this proves the lemma.

Recall that in the block $\mathscr{B}$ every 24 -cell is adjacent to two other 24 -cells along two sets of eight facets sharing same colour. If every 24-cell of the
decomposition is adjacent only to two other 24-cells along eight facets, then the blocks can be recovered from the decomposition into 24-cells. Thus, the decomposition into blocks determine $C$ and the lemma is proved.

If not, there is a 24-cell which is adjacent to three 24-cells, along eight facets to each. This implies that the block $\mathscr{B}$ that contains this 24 -cell is incident along all of its 8 geodesic boundary components to another block $\mathscr{B}^{\prime}$ (which might coincide with $\mathscr{B}$ ). Therefore $C$ consists only of one or two hypercubes, which contradicts our hypothesis. \(\square\)

We would like to conclude by saying that the decomposition into ideal 24-cells is determined by the topology of $M$ only. Proposition 2.5 says that the decomposition is determined by the topology of $M$ and the maximum cusp section: thus we need to prove that the maximum cusp section is determined by the topology. When $M$ has only one cusp this is immediate: when the are more cusps the situation is more delicate, because the maximum cusp section depends on the ratios of the volumes spanned by different cusp sections. Luckily, the topology alone tells us which ratio to choose. A similar argument was used in [5].

Lemma 2.12. Let $M$ be a hyperbolic manifold produced by a cubulation. Then the maximal cusp section of $M$ is determined only by its topology.

Proof. The maximal cusp section is obtained by selecting for each cusp corresponding to a cycle of $h$ squares the unique section $X$ with three-dimensional volume equal to $4 h$. If we show that the integer $h$ can be recovered intrinsically from the topology of the cusp, the proof is finished.

More precisely, the flat manifold $X$ is only determined up to similarity, and we now prove that $h$ can be recovered from its similarity class. As Proposition 2.3 says, up to a similarity we have $X=T \times[0, h] / \psi$, where $T$ is the 2 × 2 square torus and $\psi$ identifies $T \times 0$ with $T \times h$ via an orientationpreserving isometry of $T$ that preserves its tessellation into four unit squares.

We have that $X=\mathbb{R}^{3} / \Gamma$ where $\Gamma$ is a discrete group of orientationpreserving isometries of $\mathbb{R}^{3}$ without fixed points, determined only up to a similarity. The group $\Gamma$ contains a finite-index translation subgroup $\mathcal{T}<\Gamma$ isomorphic to $\mathbb{Z}^{3}$ which may be seen as a lattice in $\mathbb{R}^{3}$, which is also defined up to a similarity.

Let $v_{1}, v_{2} \in \mathcal{T}$ be two vectors such that the following conditions are satisfied:
\begin{itemize}
\item[(1)] $v_{1}$ and $v_{2}$ are orthogonal and have the same length $l$;
\item[(2)] the number $h=\frac{2 \mathrm{Vol}(X)}{l^{3}}$ is an integer;
\item[(3)] $v_{1}$ and $v_{2}$ are the shortest such vectors.
\end{itemize}
The resulting integer $h=\frac{2 \operatorname{Vol}(X)}{l^{3}}$ depends only on the similarity class of $X$ because the formula is invariant under a rescaling of the flat metric on $X$. To show that in this way we recover the number $h$, we have to analyse separately a number of cases proving the existence of the vectors $v_{1}$ and $v_{2}$ in each of them. Recall that up to a similarity we have $X=T \times[0, h] / \psi$. Then,
if $h \geqslant 3$, it is clear that $v_{1}$ and $v_{2}$ are the length two vectors corresponding to the translations along the respective dimensions of $T$, which is a side of the parallelepiped that gives rise to the lattice $\mathcal{T}$. If $h=2$, there can be another pair of vectors having length two, not necessarily corresponding to $T$, that we can choose as $v_{i}$ 's. However, we always have $l=2$ and $\operatorname{Vol}(X)=l^{2} h=\frac{l^{3} h}{2}$. Thus, we are left with the case of $h=1$.

Suppose $\psi$ is not a translation, that is $X$ is not a 3-torus. Thus $\mathcal{T} \neq \Gamma$ and $\mathcal{T}$ is generated by $(2,0,0),(0,2,0)$, and a third vector of the form $(a, b, c)$ with $c=2$ or $c=4$, which corresponds to either $\psi^{2}$ or $\psi^{4}$ depending on the homeomorphism class of $X$. In this case we conclude as above. Finally, we are left with the case $\mathcal{T}=\Gamma$ and $h=1$. We know that $\psi$ preserves the tessellation of the torus $T$ into four squares. There are four possible such translations, and so the lattice $\mathcal{T}$ is generated by one of the following triples:
$$\begin{aligned}
& (2,0,0),(0,2,0),(0,0, h) ; \\
& (2,0,0),(0,2,0),(1,0, h) ; \\
& (2,0,0),(0,2,0),(0,1, h) ; \\
& (2,0,0),(0,2,0),(1,1, h) .
\end{aligned}$$
It is easy to check that in all the above cases $v_{1}$ and $v_{2}$ are either the original vectors (2, 0, 0) and (0, 2, 0) that generate the torus $T$, or some other pair of vectors having length $l=2$, that we can choose as $v_{i}$ 's. The requirement that $\frac{2 \mathrm{Vol}(X)}{l^{3}}$ is an integer excludes the solutions with $l=\sqrt{2}$ that arise for instance if $v_{1}=(1,0,1)$ and $v_{2}=(-1,0,1)$ when $\Gamma$ is generated by ( $2,0,0$ ), (0, 2, 0), and (1, 0, 1). \(\square\)

Proof of 2.10. Non-equivalent cubulations produce combinatorially nonequivalent decompositions into ideal 24-cells by Lemma 2.11. These decompositions are certain Epstein-Penner canonical decompositions by Proposition 2.5, which depend only on the topology of the manifolds by Lemma 2.12. Therefore, non-equivalent decompositions give rise to non-homeomorphic manifolds. \(\square\)

\section*{3. Four-manifolds with $k$ cusps}

We can now use cubulations to construct plenty of cusped hyperbolic fourmanifolds. Let $\rho_{k}(V)$ denote the number of non-homeomorphic orientable hyperbolic four-manifolds with $k$ cusps and volume at most $V$. Below, we prove the following theorem.

Theorem 3.1. For every integer $k \geqslant 1$ there are two constants $C>1$, $V_{0}>0$ such that $\rho_{k}(V)>C^{V \ln V}$ for all $V>V_{0}$.

Let us start by constructing a hyperbolic four-manifold with one cusp.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/e1f9552b-732f-4160-b413-dfbf4a46503f-20.jpg?height=761&width=801&top_left_y=404&top_left_x=662}
\captionsetup{labelformat=empty}
\caption{Figure 6. The Schlegel diagram of the hypercube $H$. Each facet is labelled with an integer 1 to 8. The innermost facet has label 7, the outermost has label 8.}
\end{figure}
3.1. A hyperbolic manifold with one cusp. In the previous section we have shown how to transform a four-dimensional cubulation into a hyperbolic four-manifold. Recall that the 2-dimensional faces in a cubulation are partitioned into cycles, and that each cycle gives rise to a cusp in the respective manifold. Therefore, in order to construct a hyperbolic manifold with one cusp we have to find a cubulation with only one cycle of square 2-faces. We construct such a cubulation here.

The cubulation consists of one hypercube $H$ shown in Fig. 6. Its eight cubic facets are numbered from 1 to 8. We pair the opposite faces (1, 2), (3, 4), $(5,6)$ and $(7,8)$ via certain Euclidean isometries. The isometries are described in Fig. 7: we have reproduced every facet from Fig. 6 and drawn a frame $x, y, z$ in each, that consists of a vertex and three adjacent oriented edges ordered as $x, y, z$. We identify the facets on the left with the facets on the corresponding right using the unique isometry that matches the frames.

Proposition 3.2. The cubulation is orientable and has a unique cycle of 2-faces.

Proof. Every facet inherits an orientation from the orientation of $H$. In Fig. 6, all the facets are projected inside 8. Therefore, the orientation of the facets 1 to 7 is the same, and that of 8 is reversed. The isometries in Fig. 7 pairing $(1,2),(3,4)$ and $(5,6)$ are orientation-reversing as isometries in $\mathbb{R}^{3}$, while that pairing $(7,8)$ is orientation-preserving. Thus, all the isometries

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/e1f9552b-732f-4160-b413-dfbf4a46503f-21.jpg?height=1803&width=711&top_left_y=400&top_left_x=707}
\captionsetup{labelformat=empty}
\caption{Figure 7. The pairing of the facets of $H$. Every row describes a pair of opposite facets, which are identified by the unique isometry which matches the $x, y, z$ frames. The facet labels of $H$ are encircled. The square 2-face labels are bold. All facets have the same orientation, except for 8.}
\end{figure}
are orientation-reversing if seen with the intrinsic orientation of $\partial H$ : the cubulation is hence orientable.

We now prove that all the square 2-faces form a unique cycle. We have labelled the 24 distinct 2-faces of $H$ with the symbols
$$\mathbf{a}, \mathbf{b}, \mathbf{c}, \mathbf{d}, \mathbf{e}, \mathbf{f}, \mathbf{1}, \mathbf{2}, \mathbf{3}, \mathbf{4}, \mathbf{5}, \mathbf{6}, \mathbf{g}, \mathbf{h}, \mathbf{k}, \mathbf{1}, \mathbf{7}, \mathbf{8}, \mathbf{9}, \mathbf{0}, \mathbf{m}, \mathbf{n}, \mathbf{o}, \mathbf{p} .$$
The labels are shown in Fig. 7. The facet pairing induces the following identifications of the corresponding 2-faces:
$$\begin{array}{llll}
\mathrm{a} \rightarrow 1 & \mathrm{f} \rightarrow 6 & 1 \rightarrow 8 & \mathrm{c} \rightarrow \emptyset \\
\mathrm{~b} \rightarrow 2 & \mathrm{e} \rightarrow 5 & \mathrm{~g} \rightarrow 9 & \mathrm{k} \rightarrow 7 \\
\mathrm{c} \rightarrow 3 & \mathrm{~d} \rightarrow 4 & \mathrm{~h} \rightarrow \mathrm{~d} & \mathrm{l} \rightarrow 6
\end{array}$$
$$\begin{array}{cccc}
\mathrm{m} \rightarrow \emptyset & \mathrm{n} \rightarrow \mathrm{l} & \mathrm{e} \rightarrow \mathbf{9} & \mathbf{2} \rightarrow \mathrm{~g} \\
3 \rightarrow \mathrm{f} & \mathrm{a} \rightarrow 4 & \mathrm{n} \rightarrow \mathbf{5} & \mathrm{o} \rightarrow \mathrm{~b} \\
\mathrm{~h} \rightarrow \mathrm{o} & 8 \rightarrow \mathrm{p} & \mathrm{k} \rightarrow \mathrm{~m} & 7 \rightarrow \mathrm{p}
\end{array}$$

Altogether these identifications produce a unique cycle:
a18p7kmøc3f6ln5e9g2bohd4a. \(\square\)

The algorithm described in the previous section transforms the cubulation into a cusped hyperbolic four-manifold $\mathscr{M}$ with one cusp.
3.2. Proof of Theorem 3.1. Thanks to the discussion carried over in the previous sections, the proof of Theorem 3.1 reduces to the following lemma, which deals with cubulations only and not with hyperbolic geometry. Let $\eta_{k}(n)$ be the number of combinatorially distinct cubulations with at most $n$ hypercubes whose 2-dimensional faces form exactly $k$ cycles.

Lemma 3.3. For every integer $k \geqslant 1$ there are two constants $C, n_{0}>1$ such that $\eta_{k}(n)>C^{n \ln n}$ for all $n>n_{0}$.

Proof of Theorem 3.1 from Lemma 3.3. By Theorem 2.10 non-equivalent cubulations (with at least 3 hypercubes) produce non-homeomorphic hyperbolic four-manifolds. \(\square\)

The rest of this section is devoted to the proof of Lemma 3.3. The incidence graph $G$ of a cubulation $C$ is constructed by placing a vertex for every hypercube and an edge for every facet-pairing. Every vertex in $G$ has valence 8. We start by the following proposition.

Proposition 3.4. Let a cubulation $C$ have $k>1$ cycles of square 2-faces and incidence graph $G$. There is a cubulation $C^{\prime}$ with $k-1$ cycles of 2-faces, whose incident graph $G^{\prime}$ is obtained from $G$ by applying the transformation depicted in Fig. 8 to some edge of $G$.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/e1f9552b-732f-4160-b413-dfbf4a46503f-23.jpg?height=200&width=604&top_left_y=406&top_left_x=761}
\captionsetup{labelformat=empty}
\caption{Figure 8. Adding a flower to an edge of the incidence graph. The new cubulation $C^{\prime}$ has one hypercube more than $C$.}
\end{figure}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/e1f9552b-732f-4160-b413-dfbf4a46503f-23.jpg?height=378&width=458&top_left_y=819&top_left_x=834}
\captionsetup{labelformat=empty}
\caption{Figure 9. The sequence of 2-faces in the partial cubulation.}
\end{figure}

Proof. Every cycle of 2-faces in $C$ may be seen as a closed path in $G$. This closed path may pass multiple times over a vertex or edge of $G$. Let us denote these cycles by $f_{1}, \ldots, f_{k}$.

Every edge $e$ of $G$ corresponds to a pairing of 3-dimensional cubes, identified to a single cube $K$ in the cubulation. The edge $e$ is traversed 6 times by the paths $f_{1}, \ldots, f_{k}$ : each passing corresponds to a 2-face of $K$. A path may traverse $e$ multiple times in both directions.

Since $k>1$, it is easy to deduce that there is at least one edge $e$ which is traversed by at least two distinct paths: in other words, not all of the six faces in the corresponding cube $K$ belong to the same cycle. Then we may pick two non-opposite 2-faces of $K$ that belong to distinct cycles, say $f_{1}$ and $f_{2}$.

We now want to insert a new hypercube at $e$ and construct a new cubulation in which $f_{1}$ and $f_{2}$ become a single cycle. In order to do so, we construct a "partial cubulation" as follows. Let us consider a new hypercube $H$ as in Fig. 6 and pair the facets $(3,4),(5,6)$ and $(7,8)$ as described by Fig. 7, leaving the facets 1 and 2 unglued. The 2-faces of the facets 1 and 2 are labelled respectively with the symbols a, b, c, d, e, f and 1, 2, 3, 4, 5, 6. The partial cubulation induces a partition of the 24 two-dimensional faces of $H$ into six sequences, obtained by cutting the cycle (5) at six points, separating the pairs a1, c3, f6, 5e, 2b, d4. These six sequences are:
18p7kmøc, 3f, 6ln5, e9g2, bohd, 4a.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/e1f9552b-732f-4160-b413-dfbf4a46503f-24.jpg?height=425&width=1195&top_left_y=412&top_left_x=466}
\captionsetup{labelformat=empty}
\caption{Figure 10. By inserting the partial cubulation at an edge we reduce the number of cycles by one.}
\end{figure}

We visualise the six paths in Fig. 9. Each path connects a pair of 2-faces belonging to the unglued facets 1 and 2. We note that there are only two paths connecting two square 2-faces belonging to the same 3-dimensional cube: they connect b to d and 5 to 6.

We now turn back to our original cubulation $C$. We visualise the six paths traversing the edge $e$ as in Fig. 10-(left): the three pairs of paths correspond to the three pairs of opposite faces in $K$. By hypothesis, the cycles $f_{1}$ and $f_{2}$ pass through two non-opposite faces. We now modify the cubulation $C$ by inserting the partial cubulation at the edge $e$ as suggested by Fig. 10. The incidence graph changes as in Fig. 8 and the cycles look now as shown in Fig. 10: the two cycles $f_{1}$ and $f_{2}$ are fused into a single cycle, and all other cycles remain the same. This proves the proposition. \(\square\)

We can now prove Lemma 3.3 in the case of $k=1$.
Lemma 3.5. There are two constants $C, n_{0}>1$ such that $\eta_{1}(n) \geqslant C^{n \ln n}$ for all $n>n_{0}$.

Proof. Recall that a regular $v$-graph is a simple graph where every vertex has valency $v$. By simple we mean that every edge connects two distinct vertices and distinct edges connect distinct pairs of vertices.

By [3], the number of non-isomorphic $v$-regular graphs with $n$ vertices grows like $C^{n \ln n}$ for any fixed $v \geqslant 3$ and $C>1$ depending only on $v$. Therefore, it would have been sufficient to prove that every 8-regular graph $G$ arises as the incidence graph of a cubulation with only one 2-face. However, we are unable to prove exactly this statement, but we can use the previous proposition to prove a slightly weaker version of it, which is enough for our purposes.

Let $G$ be a 8-regular graph with $n$ vertices. Let $C$ be any cubulation with incidence graph $G$. The cubulation $C$ has at most $24 n$ cycles of square 2-faces: Proposition 3.4 implies that by adding at most $24 n$ flowers at its edges, as shown in Fig. 8, we may transform $G$ into a graph $G^{\prime}$, which is the incidence graph of a cubulation with only one 2-face.

Every flower increases the number of vertices of $G$ by one. Therefore every 8-regular graph $G$ with $n$ vertices gives rise to a graph $G^{\prime}$ with at most $25 n$ vertices which is the incidence graph of some cubulation with one 2-face. The graph $G$ can be reconstructed from $G^{\prime}$ by eliminating all the petals, i.e. the edges with coinciding endpoints: therefore non-isomorphic regular graphs $G$ and $H$ give rise to non-isomorphic graphs $G^{\prime}$ and $H^{\prime}$ and hence to non-isomorphic cubulations.

Let $f(n)$ be the number of non-isomorphic simple 8-regular graphs. We know that $f(n)>C_{0}{ }^{n} \ln n$ for some $C_{0}, n_{0}>1$ and all $n>n_{0}$. We have proved that $\eta_{1}(25 n) \geqslant f(n)>C_{0}{ }^{n \ln n}$. The latter implies that $\eta_{1}(n) \geqslant$ $C_{1}{ }^{n \ln n}$, with some $C_{0}>C_{1}>1$ and $n_{1}>n_{0}>1$. \(\square\)

We now turn to the general case, and so we will need the following proposition.

Proposition 3.6. Let $C$ be a cubulation with incidence graph $G$. For every $k>0$ there is a cubulation $C^{\prime}$ with more than $2 k$ cycles of 2-faces, whose incident graph $G^{\prime}$ is obtained from $G$ by applying $k$ times the move of Fig. 8.

Proof. First we construct a partial cubulation as in the proof of Proposition 3.4, but this time we use the cubulation from Example 2.8: we take a hypercube $H$ and identify three pairs of opposite facets by a translation, leaving the fourth pair unglued. In contrary to the one used in the proof of Proposition 3.4, this partial cubulation contains two inner cycles of 2-faces. Take any edge $e$ of $G$. Let us insert $k$ subsequent copies of this partial cubulation at $e$ : the resulting cubulation $C^{\prime}$ contains more than $2 k$ cycles of 2-faces. The graph $G$ changes by adding $k$ flowers at $e$, as required. \(\square\)

We finish the proof of Lemma 3.3.
Lemma 3.7. For every integer $k>1$ there are two constants $C, n_{0}>1$ such that $\eta_{k}(n) \geqslant C^{n \ln n}$ for all $n>n_{0}$.

Proof. The proof proceeds as for Lemma 3.5. Let $C$ a cubulation with incidence graph $G$. By adding $k$ flowers we get a cubulation $C^{\prime}$ with more than $2 k$ cycles of 2-faces thanks to Proposition 3.6. Then, in accordance with Proposition 3.4, by adding at most $25(n+k)$ more flowers we finally get a cubulation $C^{\prime \prime}$ with exactly $k$ distinct cycles of square 2-faces. The rest of the argument is analogous to that of Lemma 3.5. \(\square\)

The proof of Theorem 3.1 is now complete.
3.3. Cusp shapes. In Section 3.1 we have introduced an orientable cubulation $C$ with one hypercube $H$ and one cycle of 2-faces, determining a hyperbolic manifold $\mathscr{M}$ with one cusp. We are now interested in determining the topology of its cusp section.

Proposition 3.8. The maximal cusp section of $\mathscr{M}$ is the flat 3-torus obtained by identifying the opposite faces of a right-angled parallelepiped of size $2 \times 2 \times 24$.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/e1f9552b-732f-4160-b413-dfbf4a46503f-26.jpg?height=1029&width=1261&top_left_y=415&top_left_x=432}
\captionsetup{labelformat=empty}
\caption{Figure 11. The pairing of the facets of $H$ and the evolution of the frame associated with the square 2-face labelled a. The facets of $H$ are flattened.}
\end{figure}

Proof. We need to determine the monodromy of the respective cycle of 2faces. In order to do so, we develop the eight cubic faces of the hypercube $H$ as in Fig. 11 and we fix a marking frame on the square face a in the cube 1 as follows:
![](https://cdn.mathpix.com/cropped/e1f9552b-732f-4160-b413-dfbf4a46503f-26.jpg?height=105&width=110&top_left_y=1863&top_left_x=1008)
Then we accurately carry the frame along the cycle
a18p7kmøc3f6ln5e9g2bohd4a
until we find out that the final frame matches the initial one (marked with a circle in the figure). Therefore the monodromy is the identity map and Proposition 2.7 implies that the maximal section is as required. \(\square\)

Corollary 3.9. The 3-torus bounds geometrically a hyperbolic manifold.
Which flat manifolds are realisable as cusp sections of some manifolds arising from our construction? We already know from Proposition 2.3 that

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/e1f9552b-732f-4160-b413-dfbf4a46503f-27.jpg?height=786&width=1259&top_left_y=417&top_left_x=434}
\captionsetup{labelformat=empty}
\caption{Figure 12. The cubulation giving rise to the manifold $\mathscr{K}$ from Proposition 3.10}
\end{figure}
only three homeomorphism types may be realised. We have obtained the 3-torus with one cusps, and we can also obtain the other two types with two cusps:

Proposition 3.10. Let $X$ be a torus bundle over $S^{1}$ with monodromy
$$\left(\begin{array}{cc}
-1 & 0 \\
0 & -1
\end{array}\right) \text { or }\left(\begin{array}{cc}
0 & 1 \\
-1 & 0
\end{array}\right) \text {. }$$
There exists a hyperbolic 4-manifold with two cusps, both having a crosssection homeomorphic to $X$.

Proof. We consider the orientable cubulations with one hypercube $H$ depicted in Fig. 12 and Fig. 13 (also, see Fig. 6): these give rise to two hyperbolic manifolds $\mathscr{K}$ and $\mathscr{L}$. Each cubulation has two cycles of square 2-faces: the monodromies are calculated in Fig. 14 and Fig. 15 and they are respectively
$$\left(\begin{array}{cc}
0 & 1 \\
-1 & 0
\end{array}\right),\left(\begin{array}{cc}
0 & -1 \\
1 & 0
\end{array}\right) \quad \text { and } \quad\left(\begin{array}{cc}
-1 & 0 \\
0 & -1
\end{array}\right),\left(\begin{array}{cc}
-1 & 0 \\
0 & -1
\end{array}\right) .$$ \(\square\)

Using Ontaneda's terminology [16], we may say that $X \sqcup X$ bounds geometrically a hyperbolic manifold when $X$ is a torus bundle with monodromy $\left(\begin{array}{cc}-1 & 0 \\ 0 & -1\end{array}\right)$ or $\left(\begin{array}{cc}0 & 1 \\ -1 & 0\end{array}\right)$. We were not able to prove that $X$ bounds a hyperbolic

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/e1f9552b-732f-4160-b413-dfbf4a46503f-28.jpg?height=786&width=1259&top_left_y=417&top_left_x=434}
\captionsetup{labelformat=empty}
\caption{Figure 13. The cubulation giving rise to the manifold $\mathscr{L}$ from Proposition 3.10}
\end{figure}
manifold with our constructions; in fact, we formulate the following conjecture:

Conjecture 3.11. The cusp section of a hyperbolic 4-manifold with a single cusp arising from a cubulation is a flat 3-torus.

Finally, it is easy to construct for every integer $n \geqslant 1$ a $n$-sheeted covering $\mathscr{M}_{n}$ of $\mathscr{M}$ with $n$ cusps, whose sections are $n$ flat tori. It suffices to take $n$ copies $H_{0}, \ldots, H_{n-1}$ of the hypercube $H$ shown in Fig. 6 and pair their facets as follows:
$$\left(1_{i}, 2_{i}\right), \quad\left(3_{i}, 4_{i}\right), \quad\left(5_{i}, 6_{i}\right), \quad\left(7_{i}, 8_{i+1}\right)$$
where $N_{i}$ indicates the facet number $N$ in $H_{i}$ and $i+1$ means addition modulo $n$. For every pair, the isometry is again the one described in Fig. 7.

Proposition 3.12. The resulting hyperbolic manifold $\mathscr{M}_{n}$ has n cusps. Its maximal cusp section consists of $n$ flat 3-tori, each obtained by identifying the opposite faces of a right-angled parallelepiped of size 2 × 2 × 24.

Proof. The square 2-faces are identified according to the following patterns, obtained by adding subscripts to (3)-(4):
$$\begin{array}{cccc}
\mathbf{a}_{i} \rightarrow \mathbf{1}_{i} & \mathbf{f}_{i} \rightarrow \mathbf{6}_{i} & \mathbf{1}_{i} \rightarrow \mathbf{8}_{i} & \mathbf{c}_{i} \rightarrow \emptyset_{i} \\
\mathbf{b}_{i} \rightarrow \mathbf{2}_{i} & \mathbf{e}_{i} \rightarrow \mathbf{5}_{i} & \mathbf{g}_{i} \rightarrow \mathbf{9}_{i} & \mathbf{k}_{i} \rightarrow \mathbf{7}_{i} \\
\mathbf{c}_{i} \rightarrow \mathbf{3}_{i} & \mathbf{d}_{i} \rightarrow \mathbf{4}_{i} & \mathbf{h}_{i} \rightarrow \mathbf{d}_{i} & \mathbf{l}_{i} \rightarrow \mathbf{6}_{i}
\end{array}$$

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/e1f9552b-732f-4160-b413-dfbf4a46503f-29.jpg?height=1014&width=1259&top_left_y=402&top_left_x=434}
\captionsetup{labelformat=empty}
\caption{Figure 14. The cycles of 2-faces, giving rise to the cusps of the manifold $\mathscr{K}$ from Proposition 3.10. The frames that allow us to compute the monodromy are depicted}
\end{figure}
$$\begin{array}{cccc}
\mathbf{m}_{i} \rightarrow \emptyset_{i} & \mathbf{n}_{i} \rightarrow \mathbf{l}_{i} & \mathbf{e}_{i} \rightarrow \mathbf{9}_{i+1} & \mathbf{2}_{i} \rightarrow \mathbf{g}_{i+1} \\
\mathbf{3}_{i} \rightarrow \mathbf{f}_{i} & \mathbf{a}_{i} \rightarrow \mathbf{4}_{i} & \mathbf{n}_{i} \rightarrow \mathbf{5}_{i+1} & \mathbf{o}_{i} \rightarrow \mathbf{b}_{i+1} \\
\mathbf{h}_{i} \rightarrow \mathbf{o}_{i} & \mathbf{8}_{i} \rightarrow \mathbf{p}_{i} & \mathbf{k}_{i} \rightarrow \mathbf{m}_{i+1} & \mathbf{7}_{i} \rightarrow \mathbf{p}_{i+1} .
\end{array}$$

The cubulation has exactly $n$ cycles of square 2-faces, each of the form
$$\mathbf{a}_{i} \mathbf{1}_{i} \mathbf{8}_{i} \mathbf{p}_{i} \mathbf{7}_{i-1} \mathbf{k}_{i-1} \mathbf{m}_{i} \emptyset_{i} \mathbf{c}_{i} \mathbf{3}_{i} \mathbf{f}_{i} \mathbf{6}_{i} \mathbf{l}_{i} \mathbf{n}_{i} \mathbf{5}_{i+1} \mathbf{e}_{i+1} \mathbf{9}_{i+2} \mathbf{g}_{i+2} \mathbf{2}_{i+1} \mathbf{b}_{i+1} \mathbf{o}_{i} \mathbf{h}_{i} \mathbf{d}_{i} \mathbf{4}_{i} \mathbf{a}_{i} .$$
The cycle is analogous to (5) and thus has trivial monodromy. \(\square\)

Corollary 3.13. For every integer $n$ there is a hyperbolic orientable fourmanifold with $n$ cusps, all whose sections are 3 -tori.

\section*{4. Dehn filling}

In the previous sections we have developed an algorithm that transforms an orientable cubulation $C$ into a hyperbolic four-manifold $M$. Here we assume that the monodromy of every cycle of 2-dimensional faces is trivial, so every cusp section is isometric to the 3 -torus obtained by identifying the

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/e1f9552b-732f-4160-b413-dfbf4a46503f-30.jpg?height=1014&width=1259&top_left_y=402&top_left_x=434}
\captionsetup{labelformat=empty}
\caption{Figure 15. The cycles of 2-faces, giving rise to the cusps of the manifold $\mathscr{L}$ from Proposition 3.10. The frames that allow us to compute the monodromy are depicted.}
\end{figure}
opposite faces of the right-angled parallelepiped $[-1,1] \times[-1,1] \times[0, h]$ (see for instance Examples 2.8 and 2.9).

The manifold $M$ is the interior of a compact manifold $\bar{M}$ with boundary that consists of 3-tori. Let us consider one boundary component $X \subset \partial \bar{M}$. A Dehn filling on $X$ is the topological operation that consists of attaching a copy of $D^{2} \times T^{2}$ along $X$. The resulting smooth manifold is determined only by the homotopy class of the closed curve $\partial D^{2} \times\{\mathrm{pt}\}$ in $\pi_{1}(X)=H_{1}(X, \mathbb{Z})$. If we fix a basis for the homology, we identify $H_{1}(X, \mathbb{Z})$ with $\mathbb{Z}^{3}$ and the Dehn filling is determined by a triple ( $p, q, r$ ) of co-prime integers. A natural basis here is given by the three sides of the parallelepiped.

It is then possible to encode the Dehn fillings of $M$ by assigning a triple $(p, q, r)$ at each cycle of 2-dimensional faces. This determines a curve in the 3-torus $[-1,1] \times[-1,1] \times[0, h] / \sim$ having length $\ell=\sqrt{(2 p)^{2}+(2 q)^{2}+(h r)^{2}}$.

By Thurston-Gromov's $2 \pi$-theorem, which holds in all dimensions (see for instance [1]), whenever $\ell \geqslant 2 \pi$ the Dehn filled manifold admits a nonpositively curved metric and is hence in particular aspherical by CartanHadamard theorem. We can therefore construct plenty of non-positively
curved four-manifolds from a simple combinatorial datum: a cubulation where each cycle of 2-faces has trivial monodromy and is assigned a triple of co-prime numbers ( $p, q, r$ ) such that $p^{2}+q^{2}+(h r / 2)^{2}>\pi^{2}$.

Recently, M. Anderson has extended Thurston's Dehn filling theorem by showing that if $\ell$ is big enough then the filled manifold admits an Einstein metric [1], see also [2]. We can therefore also construct many such manifolds from a simple combinatorial datum.

Let $\sigma$ and $\|\cdot\|$ denote the signature and Gromov norm, respectively, and let $n$ denote the number of hypercubes in the original cubulation. Let $v_{4}$ be the volume of the ideal regular hyperbolic 4-simplex.

Proposition 4.1. The Dehn filled manifold $M^{\text {fill }}$ has
$$\begin{aligned}
\chi\left(M^{\mathrm{fill}}\right) & =\chi(M)=4 n, \\
\sigma\left(M^{\mathrm{fill}}\right) & =\sigma(M)=0, \\
\left\|M^{\mathrm{fill}}\right\| & \leqslant\|M\|=\frac{\operatorname{Vol}(M)}{v_{4}}=\frac{16 n}{3 v_{4}} \pi^{2} .
\end{aligned}$$
Proof. Both the Euler characteristic and the signature are additive on the pieces when we glue $T^{2} \times D^{2}$ to $\bar{M}$ by Novikov's additivity theorem [15]. We have $\sigma\left(T^{2} \times D^{2}\right)=\chi\left(T^{2} \times D^{2}\right)=0$, and hence $\chi\left(M^{\text {fill }}\right)=\chi(M)=4 n$ by Proposition 2.2 and $\sigma\left(M^{\text {fill }}\right)=\sigma(M)=-\eta(\partial \bar{M})$ by [12]. The boundary of $\bar{M}$ consists of 3-tori, that are mirrorable and hence their $\eta$-invariant vanishes.

The Gromov norm of $M^{\text {fill }}$ is not bigger than that of $M$ by [10] and we have $\|M\|=\frac{\operatorname{Vol}(M)}{v_{4}}=\frac{16 n}{3 v_{4}} \pi^{2}$. \(\square\)

Via cubulations we may also construct certain hyperbolic four-manifolds $M_{1}, \ldots, M_{k}$, representing the interiors of compact ones, say $\overline{M_{1}}, \ldots, \overline{M_{k}}$, with toric boundaries, and then pair the boundary tori along some diffeomorphisms, obtaining various graph manifolds [9].

\section*{References}
\begin{itemize}
\item[] [1] M. Anderson, Dehn filling and Einstein metrics in higher dimensions, J. Diff. Geom. 73 (2006), 219-261.
\item[] [2] R.H. Bamler, Construction of Einstein metrics by generalized Dehn filling, J. Eur. Math. Soc. 14, 887-909.
\item[] [3] B. Bollobàs, The asymptotic number of unlabelled regular graphs, J. London Math. Soc. 26 (1982), 201-206.
\item[] [4] M. Burger - T. Gelander - A. Lubotzky - S. Mozes, Counting hyperbolic manifolds, Geom. \& Funct. Anal., 12, (2002), 1161-1173.
\item[] [5] F. Costantino - R. Frigerio - B. Martelli - C. Petronio, Triangulations of 3-manifolds, hyperbolic relative handlebodies, and Dehn filling, Comm. Math. Helv. 82 (2007), 903-934.
\item[] [6] M. Culler - N. Dunfield - J. Weeks, SnapPy, a computer program for studying the geometry and topology of 3-manifolds, http://snappy.computop.org/
\item[] [7] M. Gromov, Volume and bounded cohomology, Publ. IHES, 56 (1982), 5-99.
\item[] [8] D.B.A. Epstein - R.C. Penner, Euclidean decompositions of non-compact hyperbolic manifolds, J. Diff. Geom. 27 (1988), 67-80.
\end{itemize}
\begin{itemize}
\item[] [9] R. Frigerio - J. Lafont - A. Sisto, Rigidity of high dimensional graph manifolds, arXiv:1107.2019
\item[] [10] K. Fujiwara - J.F. Manning, Simplicial volume and fillings of hyperbolic manifolds, Algebraic \& Geometric Topology 11 (2011), 2237-2264.
\item[] [11] A. Kolpakov, On the optimality of the ideal right-angled 24-cell, Alg. Geom. Topol., 12 (2012), 1941-1960.
\item[] [12] D.D. Long - A.W. Reid, On the geometric boundaries of hyperbolic 4-manifolds, Geom. Topol. 4 (2000) 171-178.
\item[] [13] $\_\_\_\_$, All flat manifolds are cusps of hyperbolic orbifolds, Alg. Geom. Topol. 2 (2002), 285-296.
\item[] [14] B.E. Nimershiem, All flat three-manifolds appear as cusps of hyperbolic fourmanifolds, Topology and Its Appl. 90 (1998), 109-133.
\item[] [15] S.P. Novikov, Pontrjagin Classes, the Fundamental Group and some Problems of Stable Algebra, Essays on Topology and Related Topics (1970) 147-155; available from http://www.maths.ed.ac.uk/~aar/papers/novstable.pdf
\item[] [16] P. Ontaneda, Pinched Smooth Hyperbolization, arXiv:1110.6374
\item[] [17] G.J. Ratcliffe - S.T. Tschantz, The volume spectrum of hyperbolic 4-manifolds, Experimental Math. 9 (2000), 101-125.
\item[] [18] M. Stover, On the number of ends of rank one locally symmetric spaces, Geom. Topol. 17 (2013), 905-924.
\item[] [19] W.P. Thurston, "Geometry and Topology of 3-Manifolds," mimeographed notes, Princeton University, 1979; available from www.msri.org/publications/books/gt3m/
\end{itemize}

Department of Mathematics, 1326 Stevenson Center, Nashville, TN 37240, USA
E-mail address: kolpakov dot alexander at gmail dot com
Dipartimento di Matematica "Tonelli", Largo Pontecorvo 5, 56127 Pisa, Italy
E-mail address: martelli at dm dot unipi dot it
