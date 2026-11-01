---
retention_scope: session
part: 1
total_parts: 3
---

[Part 1/3 of: [math/0611157] Rational blow-downs and smoothings of surface singularities]

---
source_file: math_0611157.pdf
converter: mathpix
format: mmd
---

\title{
Rational blow-downs and smoothings of surface singularities
}

\author{
András I. Stipsicz \\ Zoltán Szabó \\ Jonathan Wahl \\ Rényi Institute of Mathematics \\ Hungarian Academy of Sciences \\ H-1053 Budapest \\ Reáltanoda utca 13-15, Hungary \\ Department of Mathematics, Princeton University, Princeton, NJ, 08544 \\ Department of Mathematics, The University of North Carolina, Chapel Hill, NC 27599-3250
}

Email: stipsicz@math-inst.hu szabo@math.princeton.edu jmwahl@email.unc.edu

\begin{abstract}
In this paper we give a necessary combinatorial condition for a negative-definite plumbing tree to be suitable for rational blow-down, or to be the graph of a complex surface singularity which admits a rational homology disk smoothing. New examples of surface singularities with rational homology disk smoothings are also presented; these include singularities with resolution graph having valency four nodes.
\end{abstract}

AMS Classification
Keywords

\section*{1 Introduction}

One of the basic operations in algebraic geometry is the blow-up process, which in complex dimension 2 (and for a point) is simply the replacement of a point with a rational curve of homological square -1. From the differential topological point of view this operation corresponds to replacing a closed tubular neighbourhood of a point (which is simply the closed 4-disk) by the tubular neighbourhood of a sphere with self-intersection -1. The inverse operation, i.e., the replacement of the tubular neighbourhood of a (-1)-sphere with the 4-disk, is called the blow-down process. It is well-known how these operations affect topological and complex analytic invariants; and the effect on Seiberg-Witten invariants is the blow-up formula of [4].

This operation has been generalized by Fintushel and Stern [5]: in the rational blow-down operation the (closed) tubular neighbourhood of certain chains of 2-spheres (whose self-intersections are the negatives of the continued fraction coefficients of $p^{2} /(p-1), p \geq 2$ an integer) have been replaced by 4-manifolds with boundary, with rational homology equal to the rational homology of the 4-disk. This idea was extended by J. Park [23], using the linear chains of spheres arising from the continued fraction coefficients of $p^{2} /(p q-1)$, for $p>q>0$ relatively prime. (We will denote such a plumbing chain by $\Gamma_{p / q}$.) The usefulness of this operation stems from the fact that the Seiberg-Witten invariants of the 4-manifold we get by rationally blowing down these chains of 2-spheres can be computed using a fairly simple formula from the Seiberg-Witten invariants of the original manifold [5], [23]. This scheme admits many applications in finding 4-manifolds with various properties, for example in searching for exotic smooth structures on 4-manifolds with small Euler characteristic [6], [24], [25], [30].

The boundary of a tubular neighbourhood of such a chain of spheres is a lens space, and it had already been known that a lens space $L\left(p^{2}, p q-1\right)$ bounds a rational homology disk, by constructions of Casson and Harer [1]. Even more, it had been known that the two-dimensional cyclic quotient singularity determined by $p^{2} /(p q-1)$ (whose resolution graph is $\Gamma_{p / q}$ ) admitted a smoothing with vanishing Milnor number, hence its link bounds a rational homology disk (the "Milnor fiber") admitting a Stein structure (see [34, Example (5.9.1)] and Sections 7 and 8 below). Of course, one cannot expect to be able to do complex-analytic surgery, and replace one compact complex surface by another, cf. [14], [22] for related discussion.

The simplicity of the formula relating the Seiberg-Witten invariants of the 4-manifolds before and after rational blow-down follows from three facts:
\begin{itemize}
\item[(1)] if the given configuration of spheres is tautly embedded for a given spin ${ }^{c}$ structure s (see Subsection 2.1), then the restriction of the spin ${ }^{c}$ structure extends from the complement of the configuration of spheres to the rational homology disk;
\item[(2)] this extended spin ${ }^{c}$ structure gives rise to a Seiberg-Witten moduli space with the same expected dimension as s; and finally
\item[(3)] the 3-manifold along which we cut and glue admits the simplest possible Seiberg-Witten Floer homology (since it is a lens space, possessing a metric of positive scalar curvature).
\end{itemize}

It has been shown by Symington [31], [32] that a configuration $\Gamma_{p / q}$ of symplectic spheres in a symplectic 4-manifold can be blown down symplectically; that is, the symplectic form, when restricted to the complement of the spheres, ex-
tends to the rational homology disk. This observation explains the appearance of properties (1) and (2) above. The existence of the appropriate symplectic structure on the rational homology disk is a consequence of the fact that it is the Milnor fiber of a smoothing of the corresponding quotient singularity, hence admits a Stein structure. It is known that a surface singularity admitting a rational homology disk smoothing is necessarily rational (see also Subsection 2.3), and the link of a rational singularity is an $L$-space [16] (i.e., has the simplest possible Heegaard Floer homology, which is conjectured to be equivalent to the link admitting simple Seiberg-Witten Floer homology). This observation explains (3) above.

After the success of the rational blow-down process in constructing new and interesting smooth and symplectic 4-manifolds (and more recently complex surfaces [14], [22]), it was natural to ask which other plumbing trees possess similar properties. Casson and Harer [1] provided many examples of 3-manifolds which bound rational homology disks; but when performing the rational blow-down process along them, the lack of (some of) the properties (1-3) listed above implied that the resulting 4-manifolds were usually uninteresting (i.e., had trivial Seiberg-Witten invariants). Correspondingly, it has been known for some time that the only cyclic quotient singularities admitting smoothings with Milnor number 0 (i.e., rational homology disk smoothings) are those with graph $\Gamma_{p / q}$, see [15, Remark (5.10)]. On the other hand, a triply-infinite family of singularities admitting Milnor number 0 smoothings appeared already in 1980 [34, (5.9.2)].

We will see that minimal negative-definite plumbing graphs $\Gamma$ of interest in these problems satisfy very strong combinatorial restrictions. Properties (1) and (2) above lead to the following

Definition 1.1 The plumbing tree $\Gamma$ on $n$ vertices is a symplectic plumbing tree if $\Gamma$ admits an embedding $\varphi$ into the negative-definite diagonal lattice $\left(\mathbb{Z}^{n}, Q_{n}\right)$ with $Q_{n}=n\langle-1\rangle$ such that
\begin{itemize}
\item[-] for vertices $v_{1} \neq v_{2} \in \Gamma$ we have $Q_{n}\left(\varphi\left(v_{1}\right), \varphi\left(v_{2}\right)\right)=1$ or 0 depending on whether $v_{1}$ and $v_{2}$ are adjacent in $\Gamma$,
\item[-] $Q_{n}(\varphi(v), \varphi(v))$ is equal to the decoration of $v$ for all $v \in \Gamma$, and
\item[-] with the basis $\left\{E_{1}, \ldots, E_{n}\right\}$ of $Q_{n}$ satisfying $Q_{n}\left(E_{i}, E_{j}\right)=-\delta_{i j}$ and with the notation $K=\sum_{i=1}^{n} E_{i}$ we have the adjunction equality
$$Q_{n}(v, K)+Q_{n}(v, v)=-2$$
for every vertex $v$ of $\Gamma$.
\end{itemize}

A graph $\Gamma$ is called minimal if there is no vertex in $\Gamma$ with decoration (-1). We denote the set of minimal, connected symplectic plumbing trees by $\mathcal{S}$.

Remark 1.2 The name for the set $\mathcal{S}$ comes from the fact that the adjunction equality is naturally satisfied by a tree of symplectically embedded spheres in a symplectic 4-manifold. Notice that if a resolution of a complex surface singularity has dual graph given by $\Gamma$, then $K$, the restriction of the first Chern class of the complex structure, satisfies (1.1) - as a result of the adjunction formula.

Remark 1.3 From the point of view of [15], consider the negative-definite lattice
$$L=\bigoplus_{v \in \Gamma} \mathbb{Z} \cdot v$$
generated by the vertices of $\Gamma$, using intersections $v \cdot v^{\prime}$ as given by the graph; one has as well an element $K \in L^{*}$. Then Definition 1.1 requires that $L$ be a sublattice of a unimodular lattice $L^{\prime}$ of the same rank, which contains the characteristic element $K$. As in [15], the existence of such an $L^{\prime}$ and $K$ is equivalent to the existence of a self-isotropic subspace of the discriminant quadratic group $\left(L^{*} / L, q\right)$ (see also Section 2.3); however, in this case examples indicate that one would not necessarily have that $L^{\prime}$ is diagonal, as is further required by Definition 1.1 .

Our main goal is to determine a necessary combinatorial property of a plumbing tree $\Gamma$ (and its associated plumbing 4-manifold $M_{\Gamma}$ ) such that there exists a rational homology disk $B_{\Gamma}$ (with $\partial M_{\Gamma} \cong \partial B_{\Gamma}$ ), and for which one of the following holds: (a) for $M_{\Gamma} \subset(X, \mathbf{s})$ tautly embedded into a spin ${ }^{c} 4$-manifold with $S W_{X}(\mathbf{s}) \neq 0$, the new manifold $\left(X-M_{\Gamma}\right) \cup B_{\Gamma}$ has nontrivial Seiberg-Witten invariants; (b) a symplectically embedded $M_{\Gamma}$ can be blown down in the symplectic category; (c) there is a singularity with resolution graph $\Gamma$ admitting a rational homology disk smoothing. As will be explained in the next section, the graphs in $\mathcal{S}$ are the only candidates for these three problems. (We will also explain the relation among the three problems mentioned above.) In summary, we can compile the results of the next section into

Proposition 1.4 (cf. Corollaries 2.2, 2.3, 2.5) Let $\Gamma$ be a negative-definite minimal plumbing tree of spheres which can be tautly embedded and rationally blown down, or can be symplectically blown down, or gives rise to a complex surface singularity admitting a rational homology disk smoothing. Then $\Gamma \in \mathcal{S}$.

The main theorem of the present paper (Theorem 1.8) gives a combinatorial description of the set $\mathcal{S}$. Aside from the set $\Gamma_{p / q}$, the graphs consist of 3 triply-infinite families $\mathcal{W}, \mathcal{N}, \mathcal{M}$, built on the 3 basic examples shown by Figure 1. There are 3 more classes $\mathcal{A}, \mathcal{B}, \mathcal{C}$ built out of variations of these basic examples,

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/df5f5431-21ef-431b-b837-d2c96a8445b9-05.jpg?height=494&width=1167&top_left_y=666&top_left_x=505}
\captionsetup{labelformat=empty}
\caption{Figure 1: Graphs of the basic examples, giving the families $\mathcal{W}, \mathcal{N}, \mathcal{M}$}
\end{figure}
cf. Definition 1.5 below.
The other key results of the paper (e.g., Theorems 1.9, 1.10) show that many of the graphs in $\mathcal{S}$ actually do occur in one of our situations (cf. also [7]). But, not all $\Gamma \in \mathcal{S}$ occur; further constraints and a better understanding of the geometric picture will be addressed in a subsequent project, see also Subsection 2.4. In order to state the main result of the paper, we need a definition.

Definition 1.5 ● For integers $p>q>0$ relatively prime, consider the continued fraction expansion of $p^{2} /(p q-1)$, i.e.,
$$p^{2} /(p q-1)=a_{1}-\frac{1}{a_{2}-\frac{1}{\ddots-\frac{1}{a_{k}}}},$$
where $a_{i} \in \mathbb{N}, a_{i} \geq 2$. Figure 2 shows the corresponding negative-definite plumbing tree, denoted by $\Gamma_{p / q}$. We denote the set of all such graphs by $\mathcal{G}$.
\begin{itemize}
\item[-] The plumbing tree given by Figure 3 will be denoted by $\Gamma_{p, q, r}(p, q, r \geq$ $0)$. We denote the set of these plumbing trees by $\mathcal{W}$.
\end{itemize}
$$\Gamma_{p / q}=\stackrel{-a_{1}}{\bullet} \quad \stackrel{-a_{2}}{\bullet} \ldots \stackrel{-a_{k-1}}{\bullet}-a_{k}$$

\begin{figure}
\captionsetup{labelformat=empty}
\caption{Figure 2: The graph $\Gamma_{p / q}$ in $\mathcal{G}$}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/df5f5431-21ef-431b-b837-d2c96a8445b9-06.jpg?height=342&width=778&top_left_y=895&top_left_x=696}
\end{figure}

Figure 3: The graph $\Gamma_{p, q, r}$ in $\mathcal{W}$
\begin{itemize}
\item[-] The plumbing tree of Figure 4 will be denoted by $\Delta_{p, q, r}$ ( $p \geq 1$ and $q, r \geq 0)$. The slight modification of the graph $\Delta_{p, q, r}$ when $p=0$ is shown in Figure 5. The set of graphs $\Delta_{p, q, r}$ with $p, q, r \geq 0$ will be denoted by $\mathcal{N}$.
\item[-] The plumbing graph of Figure 6 is $\Lambda_{p, q, r}$ with $p, r \geq 1$ and $q \geq 0$. Modifications of these graphs for $p=0, r \geq 1$ and $p \geq 1, r=0$ are shown by Figures 7 and 8. The last degeneration, when $p=r=0$ (as shown by Figure 9) will appear in the family $\mathcal{C}$ defined below. The set of graphs $\left\{\Lambda_{p, q, r} \mid p, q, r \geq 0,(p, r) \neq(0,0)\right\}$ will be denoted by $\mathcal{M}$.
\item[-] Let us define $\mathcal{A}$ as the family of graphs we get in the following way: start with the graph of Figure 10(a), blow up its (-1)-vertex or any edge emanating from the (-1)-vertex and repeat this procedure of blowing up (either the new (-1)-vertex or an edge emanating from it) finitely many times, and finally modify the single (-1)-decoration to (-4). Depending on the number and configuration of the chosen blow-ups, this procedure defines an infinite family of graphs. Define $\mathcal{B}$ similarly, when starting with Figure 10(b) and substituting (-1) in the last step with (-3), and finally define $\mathcal{C}$ in the same vein by starting with Figure 10(c) and putting
\end{itemize}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/df5f5431-21ef-431b-b837-d2c96a8445b9-07.jpg?height=169&width=1018&top_left_y=472&top_left_x=662}
\captionsetup{labelformat=empty}
\caption{Figure 4: The graph $\Delta_{p, q, r}$ in for $p \geq 1$ and $q, r \geq 0$}
\end{figure}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/df5f5431-21ef-431b-b837-d2c96a8445b9-07.jpg?height=157&width=774&top_left_y=891&top_left_x=698}
\captionsetup{labelformat=empty}
\caption{Figure 5: The graph $\Delta_{0, q, r}$}
\end{figure}
(-2) instead of (-1) in the final step.
Remark 1.6 Figure 11 gives a pictorial description of what we mean by blowing up a (-1)-vertex (Figure 11(a)) and an edge emanating from a (-1)-vertex (Figure 11(b)). Notice that in the plumbing 4-manifold both operations correspond to blowing up the (-1)-sphere defined by the vertex, either in a generic point or in an intersection with another sphere of the plumbing configuration. The reverse of the blow-up operation will be called blowing down; notice that only a vertex of valency 1 or 2 can be blown down in the category of plumbing trees.

Remark 1.7 In classes $\mathcal{N}$ and $\mathcal{M}$, the need to make special graphs when some of $p, q, r$ are 0 disappears if we look instead at the "dual graphs", which arise in smoothings of negative weight (see Subsection 8.1).

After these preparations we are ready to state the main theorems of the paper:
Theorem 1.8 The set $\mathcal{S}$ is equal to the union $\mathcal{G} \cup \mathcal{W} \cup \mathcal{N} \cup \mathcal{M} \cup \mathcal{A} \cup \mathcal{B} \cup \mathcal{C}$.
We will show that these 7 types of graphs are in $\mathcal{S}$ by exhibiting explicit embeddings in $n\langle-1\rangle$ : for $\mathcal{G}$, use Proposition 4.4: $\mathcal{W}, \mathcal{N}, \mathcal{M}$ are done in the Appendix; for $\mathcal{A}, \mathcal{B}, \mathcal{C}$, proceed by induction as in Proposition 5.7. (One can give an abstract proof for the first four classes by combining the Examples in Section 8 with Corollary 2.5). That $\mathcal{S}$ consists only of these types is the heart of this paper.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/df5f5431-21ef-431b-b837-d2c96a8445b9-08.jpg?height=168&width=1087&top_left_y=472&top_left_x=662}
\captionsetup{labelformat=empty}
\caption{Figure 6: The graph $\Lambda_{p, q, r}$ in for $p, r \geq 1$ and $q \geq 0$}
\end{figure}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/df5f5431-21ef-431b-b837-d2c96a8445b9-08.jpg?height=167&width=725&top_left_y=758&top_left_x=767}
\captionsetup{labelformat=empty}
\caption{Figure 7: The graph $\Lambda_{0, q, r}$ for $r \geq 1$ and $q \geq 0$}
\end{figure}

The next question is which $\Gamma \in \mathcal{S}$ are suitable for rational blow-down, or which can be the graph of a normal surface singularity admitting a rational homology disk smoothing. On the positive side, in many cases there are several constructions for the appropriate rational homology disks. Using Kirby calculus, one can prove (Section 7):

Theorem 1.9 A plumbing graph $\Gamma \in \mathcal{G} \cup \mathcal{W} \cup \mathcal{N} \cup \mathcal{M}$ defines the plumbing 4-manifold $M_{\Gamma}$ with the property that $\partial M_{\Gamma}$ bounds a rational homology disk.

In fact, a stronger result is true; two methods for constructing smoothings of normal surface singularities (Section 8) lead to:

Theorem 1.10 Any graph $\Gamma \in \mathcal{G} \cup \mathcal{W} \cup \mathcal{N} \cup \mathcal{M}$ gives rise to a normal surface singularity which admits a smoothing with vanishing Milnor number. Some infinite families of graphs in each of $\mathcal{A}, \mathcal{B}$, and $\mathcal{C}$, including some with a node of valency 4, admit the same property.
(Concerning the valency 4 Examples 8.7, 8.12 and 8.14, see [11] for a related discussion.) While Theorem 1.8 excludes graphs with a node of valency $\geq 5$ or two nodes of valency 4, it allows graphs with two (or more) nodes of valency $\geq 3$; but at present none of these examples are known to admit a smoothing with vanishing Milnor number. Finally, it is worth noting that any $\Gamma \in \mathcal{S}$ which is star-shaped with a node of valency 3 is taut in the sense of Laufer [12]: there is a unique singularity (necessarily rational and weighted homogeneous) with graph $\Gamma$. On the other hand, [12, Theorem 4.1] shows that any singularity with star-shaped $\Gamma \in \mathcal{S}$ with a node of valency 4 is weighted homogeneous, and its analytic type is determined by the cross-ratio of the 4 special points on

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/df5f5431-21ef-431b-b837-d2c96a8445b9-09.jpg?height=158&width=845&top_left_y=473&top_left_x=767}
\captionsetup{labelformat=empty}
\caption{Figure 8: The graph $\Lambda_{p, q, 0}$ for $p \geq 1$ and $q \geq 0$}
\end{figure}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/df5f5431-21ef-431b-b837-d2c96a8445b9-09.jpg?height=155&width=484&top_left_y=761&top_left_x=802}
\captionsetup{labelformat=empty}
\caption{Figure 9: The graph $\Lambda_{0, q, 0}$ for $q \geq 0$}
\end{figure}
the central curve in the minimal resolution. But in Example 8.12, for instance, there exists a homology disk smoothing for only one of these analytic types; in fact, the deformation space of that particular singularity contains a "smoothing component" of dimension 1, cf. [34, Theorem 3.13(c)].

On the other hand, certain classes in $\mathcal{A}, \mathcal{B}$ and $\mathcal{C}$ give 3-manifolds which do not even bound rational homology disks (because of their $\mu$-invariant). For this and other obstructions, see Subsection 2.4.

The paper is organized as follows: In Section 2 we motivate our definition of $\mathcal{S}$ through a more detailed discussion of the rational blow-down operation in the smooth and symplectic category, and briefly review some basic facts about normal surface singularities. In Section 3, we consider a graph $\Gamma \in \mathcal{S}$, and write each vertex $v \in \Gamma$ as an integral combination of the basis vectors $E_{i}$, deducing quickly strong conditions on the coefficients, hence on the graphs. The hard technical work in Sections 4, 5 and 6 provides the proof of Theorem 1.8 (with the addendum of describing the actual embeddings of graphs in $\mathcal{W} \cup \mathcal{M} \cup \mathcal{N}$, which is deferred to the Appendix given in Section 9). Section 7 is devoted to the proof of the existence of rational homology disks for plumbing graphs in $\mathcal{G} \cup \mathcal{W} \cup \mathcal{M} \cup \mathcal{N}$; here we use techniques of smooth 4-manifold topology. Finally, in Section 8 two algebro-geometric methods are described and applied to verify the existence of rational homology disk smoothings for large families of singularities given by plumbing graphs of $\mathcal{S}$.

Acknowledgements: The first author would like to thank the Institute for Advanced Study in Princeton for their hospitality while some part of this work has been carried out. AS was partially supported by OTKA T49449; ZSz was supported by NSF grant number DMS 0406155; and JW was partially supported by NSA grant number FA9550-06-1-0063. The first and second authors were

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/df5f5431-21ef-431b-b837-d2c96a8445b9-10.jpg?height=497&width=1166&top_left_y=500&top_left_x=574}
\captionsetup{labelformat=empty}
\caption{Figure 10: Nonminimal plumbing trees giving rise to the families $\mathcal{A}, \mathcal{B}$ and $\mathcal{C}$}
\end{figure}
also supported by EU Marie Curie TOK project BudAlgGeo. We would like to thank the referee for his/her many valuable comments and suggestions.

\section*{2 Plumbing trees}

The main purpose of this section is to justify Definition 1.1. We show that if the plumbing 4-manifold $M_{\Gamma}$ can be (Seiberg-Witten or symplectically) blown down then $\Gamma \in \mathcal{S}$; similarly, if $\Gamma$ is the resolution graph of a normal surface singularity with a smoothing with vanishing Milnor number, then $\Gamma \in \mathcal{S}$.

\subsection*{2.1 Tautly embedded plumbing trees}

Suppose that $\Gamma$ is a given negative-definite plumbing tree of spheres and $M_{\Gamma}$ is the corresponding plumbed 4-manifold with boundary. Let $\Sigma_{v} \subset M_{\Gamma}$ denote the 2-sphere corresponding to the vertex $v \in \Gamma$. We say that $M_{\Gamma}$ is tautly embedded in a closed, oriented spin ${ }^{c} 4$-manifold $(X, \mathbf{s})$ if
$$\left\langle c_{1}(\mathbf{s}),\left[\Sigma_{v}\right]\right\rangle+\left[\Sigma_{v}\right]^{2}=-2$$
for all $v \in \Gamma$. With a slight abuse of terminology, sometimes we say that the graph $\Gamma$ is tautly embedded.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/df5f5431-21ef-431b-b837-d2c96a8445b9-11.jpg?height=470&width=1150&top_left_y=426&top_left_x=496}
\captionsetup{labelformat=empty}
\caption{Figure 11: The blow-up of (a) a (-1)-vertex and (b) an edge emanating from a (-1)-vertex}
\end{figure}

Definition 2.1 The 4 -manifold $M_{\Gamma}$ (or the plumbing graph $\Gamma$ ) can be Seiberg-Witten blown down if there is a 4-manifold $B_{\Gamma}$, with the same rational homology as the disk $D^{4}$ and with $\partial B_{\Gamma} \cong \partial M_{\Gamma}$, with the following property: for a taut embedding $M_{\Gamma} \subset(X, \mathbf{s})$ for which $S W_{X}(\mathbf{s}) \neq 0$,
\begin{itemize}
\item[-] the spin ${ }^{c}$ structure $\left.\mathbf{s}\right|_{X-M_{\Gamma}}$ extends to $\mathbf{s}^{\prime} \in \operatorname{Spin}^{c}\left(X^{\prime}\right)$, where $X^{\prime}=$ $\left(X-M_{\Gamma}\right) \cup B_{\Gamma}$,
\item[-] the Seiberg-Witten moduli spaces $\mathcal{M}_{X^{\prime}}\left(\mathbf{s}^{\prime}\right)$ and $\mathcal{M}_{X}(\mathbf{s})$ have the same expected dimensions, and
\item[-] $S W_{X}(\mathbf{s})= \pm S W_{X^{\prime}}\left(\mathbf{s}^{\prime}\right)$.
\end{itemize}
Since the expected dimension of the Seiberg-Witten moduli space is given by the formula
$$\operatorname{dim} \mathcal{M}_{X}(\mathbf{s})=\frac{1}{4}\left(c_{1}^{2}(\mathbf{s})-3 \sigma(X)-2 e(X)\right)$$
(where, as usual, $\sigma(X)$ and $e(X)$ denote the signature and Euler characteristic of the 4-manifold $X$ ), the assumption $\operatorname{dim} \mathcal{M}_{X}(\mathbf{s})=\operatorname{dim} \mathcal{M}_{X^{\prime}}\left(\mathbf{s}^{\prime}\right)$ together with the facts
$$\sigma\left(X^{\prime}\right)=\sigma(X)+|\Gamma| \text { and } e\left(X^{\prime}\right)=e(X)-|\Gamma|$$
(following from the negative-definiteness of $\Gamma$ ) imply
$$c_{1}^{2}(\mathbf{s})-c_{1}^{2}\left(\mathbf{s}^{\prime}\right)=-|\Gamma| .$$
The symbol $|\Gamma|$ denotes the rank of $\Gamma$, that is, the cardinality of its vertex set.

Let $X_{\Gamma}=M_{\Gamma} \cup \overline{B_{\Gamma}}$, where $\overline{B_{\Gamma}}$ denotes the 4-manifold $B_{\Gamma}$ with the opposite orientation. Since $\Gamma$ is a negative-definite graph and $B_{\Gamma}$ is a rational homology disk, it follows that $X_{\Gamma}$ is a negative-definite closed, oriented 4-manifold, and rk $H_{2}\left(X_{\Gamma} ; \mathbb{Z}\right)=|\Gamma|$. According to Donaldson's famous diagonalizability theorem [2], [3] we have that the intersection form $Q$ on $H_{2}\left(X_{\Gamma} ; \mathbb{Z}\right) /$ Torsion is diagonalizable, providing an embedding of $\Gamma$ on $n$ vertices into the diagonal form $\left(\mathbb{Z}^{n}, Q_{n}\right)$ with $Q_{n}=n\langle-1\rangle$. (For a Heegaard Floer theoretic proof of Donaldson's result, see [21, Theorem 9.1].) By gluing the spin ${ }^{c}$ structure $\left.\mathbf{s}\right|_{M_{\Gamma}}$ to the extension of $\left.\mathbf{s}\right|_{\partial M_{\Gamma}}$ over $\overline{B_{\Gamma}}$ we get a spin ${ }^{c}$ structure $\mathbf{s}_{\Gamma} \in \operatorname{Spin}^{c}\left(X_{\Gamma}\right)$. The assumption on the expected dimensions of the Seiberg-Witten moduli spaces and the fact that $H_{2}\left(B_{\Gamma} ; \mathbb{Q}\right)=0$ readily implies that
$$c_{1}^{2}\left(\mathbf{s}_{\Gamma}\right)=c_{1}^{2}(\mathbf{s})-c_{1}^{2}\left(\mathbf{s}^{\prime}\right)=-|\Gamma|=-n .$$
Since in the negative-definite diagonal lattice of rank $n$ there is essentially a unique characteristic element of square $-n$ (which is $\sum_{i=1}^{n} E_{i}$ for an orthonormal basis $\left\{E_{1}, \ldots, E_{n}\right\}$ ), the assumption on $M_{\Gamma}$ being tautly embedded implies that Equation (1.1) holds for every $v \in \Gamma$, providing

Corollary 2.2 If the minimal, negative-definite plumbing tree $\Gamma$ gives rise to $M_{\Gamma}$ which can be Seiberg-Witten blown down, then $\Gamma \in \mathcal{S}$. \(\square\)

\subsection*{2.2 Trees which can be symplectically blown down}

Next we deal with a necessary condition for a negative-definite plumbing tree $\Gamma$ to be blown down symplectically. Suppose that $M_{\Gamma} \subset(X, \omega)$ is a symplectic embedding into the closed 4-manifold $X$ with symplectic form $\omega$, that is, the spheres $\Sigma_{v}$ are symplectic submanifolds in $(X, \omega)$ for all $v \in \Gamma$ and they intersect each other $\omega$-perpendicularly. Suppose that the 3 -manifold $\partial M_{\Gamma}$ bounds a rational homology disk $B_{\Gamma}$. We say that $\Gamma$ can be blown down symplectically if $\left.\omega\right|_{X-M_{\Gamma}}$ can be extended over the glued-up rational homology disk $B_{\Gamma}$ to produce a symplectic structure $\omega^{\prime}$ on $X^{\prime}=\left(X-M_{\Gamma}\right) \cup B_{\Gamma}$, cf. [31, Definition 1.1]. If $\mathbf{s}_{\omega} \in \operatorname{Spin}^{c}(X)$ denotes the spin ${ }^{c}$ structure induced by $\omega$ then this property implies that
\begin{itemize}
\item[-] $M_{\Gamma}$ is tautly embedded in $\left(X, \mathbf{s}_{\omega}\right)$ (since the spheres $\Sigma_{v}$ are symplectic submanifolds),
\item[-] $S W_{X}\left(\mathbf{s}_{\omega}\right)= \pm 1$ and the expected dimension of the Seiberg-Witten moduli space $\mathcal{M}_{X}\left(\mathbf{s}_{\omega}\right)$ is equal to zero, and finally
\end{itemize}
\begin{itemize}
\item[-] if $\omega^{\prime}$ induces the spin ${ }^{c}$ structure $\mathbf{s}_{\omega^{\prime}}^{\prime} \in \operatorname{Spin}^{c}\left(X^{\prime}\right)$ then $S W_{X^{\prime}}\left(\mathbf{s}_{\omega^{\prime}}^{\prime}\right)=$ ±1 and the expected dimension of the Seiberg-Witten moduli space $\mathcal{M}_{X^{\prime}}\left(\mathbf{s}_{\omega^{\prime}}^{\prime}\right)$ is zero.
\end{itemize}

Therefore $\Gamma$ fits in the category of the previous subsection, hence if $\Gamma$ can be symplectically blown down then (at least for the spin ${ }^{c}$ structure induced by the symplectic structure) it can be Seiberg-Witten blown down. This observation immediately yields

Corollary 2.3 If the minimal, negative-definite plumbing tree $\Gamma$ can be symplectically blown down, then $\Gamma \in \mathcal{S}$. \(\square\)

\subsection*{2.3 Normal surface singularities}

For more details about the following, see e.g. [15]. Let $\rho:(\tilde{Y}, E) \rightarrow(Y, o)$ be the minimal good resolution of a germ of a normal surface singularity with rational homology sphere link $\Sigma$ (i.e., $H_{1}(\Sigma ; \mathbb{Q})=0$ ). Then the exceptional divisor $E=$ $\cup_{v} E_{v}=\rho^{-1}(0)$ decomposes into smooth rational curves, giving a dual resolution graph $\Gamma$, whose vertices are indexed by the $v$ 's; $\Gamma$ is a negative-definite tree which (except for lens spaces) determines and is determined by the homotopy type of the 3-manifold $\Sigma$. Consider the lattice $\mathbb{E}=\oplus_{v \in \Gamma} \mathbb{Z}\left[E_{v}\right] \subset H_{2}(\tilde{Y} ; \mathbb{Z})$ (called $L$ in Remark 1.3). The intersection pairing gives the discriminant group $D(\Gamma) \cong \mathbb{E}^{*} / \mathbb{E}$ and
$$D(\Gamma) \cong H_{1}(\Sigma ; \mathbb{Z}) .$$
The complex structure on $\tilde{Y}$ gives rise to a relative cohomology class $K_{\tilde{Y}}$, and a rational invariant $K_{\tilde{Y}} \cdot K_{\tilde{Y}} \in \mathbb{Q}$ computable from $\Gamma$. The analytic invariant $p_{g}(Y)=\operatorname{dim} R^{1} \rho_{*} \mathcal{O}_{\tilde{Y}}$ (the geometric genus) is generally not computable from $\Gamma$. We say that $Y$ has a rational singularity if $p_{g}(Y)=0$, and this is determined by the graph condition $Z \cdot\left(Z+K_{\tilde{Y}}\right)=-2$, where $Z$ (the fundamental cycle) is the smallest effective cycle for which $Z \cdot E_{v} \leq 0$, all $v$. For example, any negative-definite tree $\Gamma$ for which the valency of every vertex is at most the negative of the self-intersection is automatically rational.

Consider a smoothing $f:(\mathcal{Y}, o) \rightarrow(\Delta, o)$ of $(Y, o)$, where $(\Delta, o)$ is the germ of an open disk in $\mathbb{C}$ (in particular, $\left(f^{-1}(o), o\right)=(Y, o)$ ). With appropriate attention to the boundaries of representatives of these germs, one can define a "general fiber" of the smoothing, the Milnor fiber $M . M$ is a compact oriented 4-manifold with boundary $\Sigma$, and its first Betti number is 0; it also has a rational invariant $K_{M} \cdot K_{M} \in \mathbb{Q}$. The Milnor number $\mu$ of the smoothing is the rank of $H_{2}(M ; \mathbb{Q})$, and in general depends on which smoothing of $Y$
one considers. Denoting the Sylvester invariants of the intersection pairing on $H_{2}(M ; \mathbb{Q})$ by $\left(\mu_{0}, \mu_{+}, \mu_{-}\right)$, one has the general formulae
$$\begin{gathered}
\mu_{0}+\mu_{+}=2 p_{g}(Y), \\
K_{M} \cdot K_{M}+\chi(M)=K_{\tilde{Y}} \cdot K_{\tilde{Y}}+\chi(\tilde{Y})+12 p_{g}(Y) .
\end{gathered}$$
Now suppose that one has a singularity and a smoothing whose Milnor fibre is a rational homology disk (i.e., $\mu=\mu_{0}+\mu_{+}+\mu_{-}=0$ ); then for topological reasons $K_{M}=0$. But the above formulas and discussion imply further that $Y$ has a rational singularity, and hence (if $n$ denotes the number of exceptional curves)
$$n+K_{\tilde{Y}} \cdot K_{\tilde{Y}}=0 .$$
For cyclic quotient singularities $\mathbb{C}^{2} / G, \Gamma$ is a string, and the condition above is valid only for the type $p^{2} /(p q-1)$ (see [15, Theorem (5.10)]).

The finite group $H_{1}(\Sigma ; \mathbb{Z})$ has a natural non-degenerate linking pairing into $\mathbb{Q} / \mathbb{Z}$, which is the same as the one on $D(\Gamma)$; but this is induced via a finer object, a quadratic function $q: H_{1}(\Sigma ; \mathbb{Z}) \rightarrow \mathbb{Q} / \mathbb{Z}$, coming from the function on $\mathbb{E}$ given by $e \mapsto(1 / 2)\left(e \cdot e+e \cdot K_{\tilde{Y}}\right)$. Theorem 4.5 of [15] implies that if a Milnor fiber $M$ has $H_{2}(M ; \mathbb{Q})=0$, then the kernel $I$ of the natural surjection $H_{1}(\Sigma ; \mathbb{Z}) \rightarrow H_{1}(M ; \mathbb{Z})$ is $q$-isotropic; in particular, $I=I^{\perp}$, so the order of $D(\Gamma)$ is a square, and the class of $K_{\tilde{Y}}$ is in $I$. In addition, by gluing the Milnor fiber $M$ with $\mu=0$ (with opposite orientation) to $\tilde{Y}$ along $\Sigma$ we get a negative-definite 4 -manifold; hence, by Donaldson's Theorem we conclude that $\Gamma$ embeds into the negative-definite diagonal lattice of rank $|\Gamma|=n$. We collect these results in

Proposition 2.4 Suppose that the normal surface singularity $(Y, o)$ with resolution graph $\Gamma$ admits a smoothing whose Milnor fiber $M$ is a rational homology disk. Then
\begin{itemize}
\item[(1)] $Y$ has a rational singularity,
\item[(2)] on the minimal good resolution $|\Gamma|+K_{\tilde{Y}} \cdot K_{\tilde{Y}}=0$,
\item[(3)] there is a self-isotropic subgroup $I \subset H_{1}(\Sigma ; \mathbb{Z})$, and $H_{1}(M ; \mathbb{Z}) \cong H_{1}(\Sigma ; \mathbb{Z}) / I$ (hence is $\cong I$ ) and
\item[(4)] $\Gamma$ admits an embedding into the diagonal lattice $\left(\mathbb{Z}^{n}, Q_{n}\right)$ of the same rank, and the class of $K_{\tilde{Y}}$ is a characteristic element of the lattice. \(\square\)
\end{itemize}
In conclusion

Corollary 2.5 If the minimal plumbing tree $\Gamma$ gives rise to a complex surface singularity which admits a rational homology disk smoothing, then $\Gamma \in \mathcal{S}$. □

Since the only rational singularities with trivial $D(\Gamma)$ are a smooth point and rational double point of type $E_{8}$, it follows that every Milnor fiber $M$ with $\mu=0$ has non-trivial $H_{1}(M ; \mathbb{Z})$. Examples with $\pi_{1}(M)$ finite and non-abelian will be shown in Section 8, e.g. Example 8.12. On the other hand, recall that Milnor fibers of hypersurface and complete intersection singularities are always simply connected.

Remark 2.6 As it was pointed out earlier, if $\Gamma$ can be blown down symplectically, then it can be Seiberg-Witten blown down. Correspondingly, if a singularity with resolution graph $\Gamma$ admits a rational homology disk smoothing, then $\Gamma$ can be blown down symplectically. This last observation is a direct consequence of the main result of [8].

\subsection*{2.4 Further considerations}

Notice that graphs in $\mathcal{S}$ only capture some aspects of the combinatorics for a configuration to admit a rational homology disk smoothing or to be one which can be rationally blown down. We make some short remarks concerning the question of which elements of $\mathcal{S}$ actually arise in one of our three situations. Further discussion is postponed to a future project.

If $\Sigma$ is a compact rational homology 3-sphere with no 2-torsion in its first homology, then there is a well-known topological obstruction for $\Sigma$ to bound (smoothly) a rational homology disk. The $\mu$-invariant of $\Sigma$ is an integer $\bmod$ 16 computed from the signature of a spin 4 -manifold bounded by $\Sigma$ (e.g., [10, p. 46]); it must be 0 if $\Sigma$ bounds a rational homology disk. Neumann and Raymond [17] show how to compute $\mu$ for a plumbed 3-manifold. One easily finds that the class $\mathcal{C}$ example given by Figure 12 has $\mu=8$, hence its boundary cannot bound a rational homology disk. Similar examples exist for types $\mathcal{A}$ and $\mathcal{B}$.

There are further exclusions when considering smoothability of surface singularities; as already mentioned, any such must have the graph of a rational surface singularity. For example the graph of Figure 13 is of class $\mathcal{B}$, but represents a minimally elliptic singularity (of geometric genus 1 [13]), so could not give a rational homology disk smoothing. Futher obstruction for a surface singularity to admit rational homology disk smoothing is provided by the integer valued invariant $\bar{\mu}$ of Neumann, cf. [29].

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/df5f5431-21ef-431b-b837-d2c96a8445b9-16.jpg?height=156&width=328&top_left_y=611&top_left_x=820}
\captionsetup{labelformat=empty}
\caption{Figure 12: A graph in $\mathcal{C}$ with $\mu=8$}
\end{figure}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/df5f5431-21ef-431b-b837-d2c96a8445b9-16.jpg?height=313&width=330&top_left_y=844&top_left_x=855}
\captionsetup{labelformat=empty}
\caption{Figure 13: Graph in $\mathcal{B} \subset \mathcal{S}$ with no rational homology disk smoothing}
\end{figure}

\section*{3 Symplectic plumbing trees}

The next four sections are devoted to the proof of Theorem 1.8. The arguments in these sections are purely combinatorial. We start with some generalities regarding plumbing trees in $\mathcal{S}$. From now on, we will identify the vertex $v$ of $\Gamma$ with its image $\varphi(v)$ (a linear combination of the $E_{i}$ 's) in the diagonal lattice $\left\langle E_{1}, \ldots, E_{n}\right\rangle=n\langle-1\rangle$. We will say that $E_{i}$ is in $v$ (or $E_{i}$ contributes to $v$ ) if $Q\left(E_{i}, v\right) \neq 0$. In this case the multiplicity of $E_{i}$ in $v$ is equal to $-Q\left(E_{i}, v\right)$. With a slight abuse of notation, the product $Q(v, w)$ sometimes will be written as $v \cdot w$ or even as $v w$.

Lemma 3.1 Suppose that $\Gamma \in \mathcal{S}$. For a vertex $v \in \Gamma$ we have either
$$v=E_{i_{v}}-\sum_{j \in J_{v}} E_{j}$$
or
$$v=-2 E_{i_{v}}-\sum_{j \in J_{v}} E_{j}$$
with $i_{v}$ not being in the index set $J_{v} \subset\{1, \ldots, n\}$.

Proof Suppose that $v=\sum_{k} \alpha_{k} E_{k}$ with $\alpha_{k} \in \mathbb{Z}$. From the fact that
$$\left(\sum_{i=1}^{n} E_{i}\right) \cdot v+v \cdot v=-2,$$
we conclude that
$$-\sum_{k} \alpha_{k}\left(\alpha_{k}+1\right)=-2,$$
implying that either exactly one $\alpha_{k}$ is equal to 1 and all the others are 0 or -1, or exactly one is equal to -2 and all the others are 0 or -1. This observation clearly implies the result. \(\square\)

It is easy to see that (in some sense) the converse of this statement also holds: if the minimal plumbing tree $\Gamma$ is embedded into the diagonal lattice $n\langle-1\rangle$ with $n=|\Gamma|$ and for all $v \in \Gamma$ we have that $v$ (in the orthogonal basis of the diagonal lattice) has one of the forms listed in the statement of the lemma above, then $v$ satisfies (3.1) and so $\Gamma$ is, in fact, in $\mathcal{S}$.

Corollary 3.2 Suppose that $\left\{v_{i_{1}}, \ldots, v_{i_{k}}\right\}$ are vertices of $\Gamma \in \mathcal{S}$ determining a connected subtree. Then
$$\sum_{j=1}^{k} v_{i_{j}}$$
is of the form given by Lemma 3.1.

Proof Notice that if $v_{1}$ and $v_{2}$ both satisfy (3.1) and $v_{1}, v_{2}$ are adjacent vertices in $\Gamma$ (that is, $v_{1} \cdot v_{2}=1$ ) then
$$\left(\sum_{i=1}^{n} E_{i}\right) \cdot\left(v_{1}+v_{2}\right)+\left(v_{1}+v_{2}\right)^{2}=-2,$$
hence the sum of the classes $v_{1}$ and $v_{2}$ also satisfies (3.1). Then Lemma 3.1 together with a simple inductive argument implies the corollary. \(\square\)

Applying the above idea for $\Gamma$ itself we get the following
Corollary 3.3 If $\Gamma \in \mathcal{S}$ is defined on $n$ vertices $\left\{v_{1}, \ldots, v_{n}\right\}$ then
$$\left|\sum_{i=1}^{n} v_{i}^{2}\right| \leq 3 n+1 .$$

Proof Notice that $\left(\sum_{i=1}^{n} v_{i}\right)^{2}=2 \sum_{i<j} v_{i} v_{j}+\sum_{i=1}^{n} v_{i}^{2}$, and since $\Gamma$ is a tree, we have $\sum_{i<j} v_{i} v_{j}=n-1$. Now the fact $\sum_{i=1}^{n} v_{i}=-2 E_{i}-\sum_{j \in J} E_{j}$ or $\sum_{i=1}^{n} v_{i}=E_{i}-\sum_{j \in J} E_{j}$ (with $J \subset\{1, \ldots, n\}-\{i\}$ ) implies that $\left(\sum_{i=1}^{n} v_{i}\right)^{2}$ is either $-4-|J| \geq-3-n$ or $-1-|J| \geq-n$. This observation implies the statement. \(\square\)

Proposition 3.4 Suppose that for $\Gamma$ as above there is a vertex $v$ of the form $-2 E_{i_{v}}-\sum_{j \in J_{v}} E_{j}$. Then for all other vertices $w \in \Gamma$ we have
$$w=E_{i_{w}}-\sum_{j \in J_{w}} E_{j} .$$

Proof Suppose that there are two vertices $v_{1}, v_{2}$ in $\Gamma$ such that
$$v_{k}=-2 E_{i_{v_{k}}}-\sum_{j \in J_{v_{k}}} E_{j} \quad(k=1,2) .$$
Consider the path $\left\{w_{l} \mid l=1, \ldots, m\right\}$ of vertices connecting $v_{1}$ and $v_{2}$ in $\Gamma$, that is, $w_{1}=v_{1}, w_{n}=v_{2}$ and $w_{i}$ is adjacent to $w_{i+1}$ for $i=1, \ldots, m-1$. Assume furthermore that the elements $w_{l}$ for $l$ different from 1 and $m$ are of the form $E_{i_{w_{l}}}-\sum_{j \in J_{w_{l}}} E_{j}$. (Otherwise we could choose a shorter chain with endpoints admitting the same properties as $v_{1}, v_{2}$ and satisfying this additional requirement.) It is easy to see that if $m>2$ then $w_{1}+w_{2}$ (and so by induction $w_{1}+\ldots+w_{m-1}$ is of the form $-2 E_{i}-\sum_{j \in J} E_{j}$ for some $i$ and index set $J$ ): if $w_{1}=-2 E_{i_{w_{1}}}-\sum_{j \in J_{w_{1}}} E_{j}$ and $w_{2}=E_{i_{w_{2}}}-\sum_{j \in J_{w_{2}}} E_{j}$ then $Q\left(w_{1}, w_{2}\right)=1$ implies that either $i_{w_{2}} \in J_{w_{1}}$ and $J_{w_{1}} \cap J_{w_{2}}=\emptyset$ (giving $w_{1}+w_{2}=-2 E_{i_{w_{1}}}-$ $\sum_{j \in J_{w_{1}} \cup J_{w_{2}}-i_{w_{2}}}$ ), or $i_{w_{1}}=i_{w_{2}}$ and $J_{w_{1}} \cap J_{w_{2}}=\{p\}$. In this latter case $w_{1}+w_{2}=-2 E_{p}-\sum_{j \in J_{w_{1}} \cup J_{w_{2}} \cup\left\{i_{w_{1}}\right\}-\{p\}} E_{j}$. Then the sum $w_{1}+\ldots+w_{m}$ would violate (3.1), since it contains at least two $E_{k}$ 's with multiplicity -2, contradicting Corollary 3.2. \(\square\)

In short, by Proposition 3.4 in $\Gamma \in \mathcal{S}$ there is at most one vertex $v$ which is of the form $-2 E_{i_{v}}-\sum_{j \in J_{v}} E_{j}$ and all other vertices are of the shape $E_{k}-\sum_{j \in J} E_{j}$. A slight generalization of the above proposition follows from the same principle:

Corollary 3.5 Suppose that $\Gamma \in \mathcal{S}$ and $\Gamma_{1}, \Gamma_{2} \subset \Gamma$ are disjoint connected subtrees. Then at least one of the vectors $w_{k}=\sum_{v \in \Gamma_{k}} v(k=1,2)$ is of the form $E_{i_{w_{k}}}-\sum_{j \in J_{w_{k}}} E_{j}$. \(\square\)

Lemma 3.6 Suppose that for two vertices $v_{1} \neq v_{2}$ we have
$$v_{k}=E_{i_{v_{k}}}-\sum_{j \in J_{v_{k}}} E_{j} \quad(k=1,2) .$$
Then $i_{v_{1}} \neq i_{v_{2}}$.
Proof Recall that the pairing $Q\left(v_{1}, v_{2}\right)$ is either 1 or 0 (depending on whether $v_{1}$ and $v_{2}$ are adjacent in $\Gamma$ or not). If $i_{v_{1}}=i_{v_{2}}$ then
$$) \leq Q\left(v_{1}, v_{2}\right)=\left(E_{i_{v_{1}}}-\sum_{j \in J_{v_{1}}} E_{j}\right) \cdot\left(E_{i_{v_{2}}}-\sum_{j \in J_{v_{2}}} E_{j}\right)=-1+\sum_{j \in J_{v_{1}} \cap J_{v_{2}}}(-1) \leq-1,$$
providing the desired contradiction. \(\square\)

Consequently, each $E_{i}$ appears in at most one $v_{j} \in \Gamma$ with positive coefficient. By Corollary 3.2, the sum $w=\sum_{v \in \Gamma} v$ is either of the form $E_{i}-\sum_{j \in J} E_{j}$ or of the form $-2 E_{k}-\sum_{j \in J} E_{j}$; so, summing all the coefficients of $E_{i}$ gives 1, 0, -1, or -2. Hence, for an index $i$ there are ten possibilities for $E_{i}$ to be contained by vectors of $\Gamma$ :

Lemma 3.7 If $i$ is an index between 1 and $n$ then for the basis vector $E_{i}$ of the diagonal lattice $Q_{n}$ one of the following ten possibilities can occur:
\begin{itemize}
\item[(1)] $E_{i}$ appears in a single vector of $\Gamma$ with multiplicity 1;
\item[(2)] $E_{i}$ appears in a single vector of $\Gamma$ with multiplicity -1;
\item[(3)] $E_{i}$ appears in a single vector of $\Gamma$ with multiplicity -2;
\item[(4)] $E_{i}$ appears in two vectors of $\Gamma$, once with multiplicity 1 and in another with multiplicity -1;
\item[(5)] $E_{i}$ is in two vectors of $\Gamma$, with multiplicities 1 and -2 ;
\item[(6)] $E_{i}$ is in two vectors of $\Gamma$, with both multiplicities -1;
\item[(7)] $E_{i}$ is in three vectors of $\Gamma$, with multiplicities $1,-1,-1$;
\item[(8)] $E_{i}$ is in three vectors of $\Gamma$, with multiplicities 1, -1 and -2;
\item[(9)] $E_{i}$ is in four vectors of $\Gamma$, once with multiplicity 1, and in three with multiplicity -1;
\item[(10)] $E_{i}$ does not appear in any vector of $\Gamma$ at all.
\end{itemize} \(\square\)

We start with a few observations regarding the types of indices occuring in an embedding $\Gamma \subset n\langle-1\rangle$. First, it is easy to see that (8) cannot occur, since if $v_{1}$ contains $-E_{i}$ and $v_{2}$ contains $-2 E_{i}$ then $Q\left(v_{1}, v_{2}\right) \leq-1$, contradicting our
assumptions. If $i$ is an index of type (10), then adding $-E_{i}$ to a single (but otherwise arbitrary) $v \in \Gamma$ we change $\Gamma$ and $\varphi$ (through the decoration of the vertex to which we added $-E_{i}$ ) in a way that the resulting $\Gamma^{\prime}$ is still in $\mathcal{S}$ but the index of type (10) is turned into an index of type (2). (Later we will see that if $i$ is an index of type (2) then $-E_{i}$ can appear only in a vector of square -2, hence we cannot change an index of type (2) to one of type (10) within the category of minimal plumbing trees.) In the following we will always assume that $\Gamma$ admits no index of type (10).

If $\Gamma \subset n\langle-1\rangle$ involves an index of type (1) then by changing both $\Gamma$ and the embedding $\varphi$ we get a new embedding $\varphi^{\prime}: \Gamma^{\prime} \rightarrow n\langle-1\rangle$ where no index of type (1) exists: if $v=E_{i_{v}}-\sum_{j \in J_{v}} E_{j}$ and $E_{i_{v}}$ does not appear in any other vector (that is, $i_{v}$ is of type (1)) then by changing $v$ to $v^{\prime}=-2 E_{i_{v}}-\sum_{j \in J_{v}} E_{j}$ we get another $\Gamma^{\prime} \in \mathcal{S}$ which only differs from $\Gamma$ by the decoration of $v$ (which has been reduced by 3). Therefore a type (1) index can be changed to be of type (3). Therefore we can assume that $\Gamma$ contains no index of type (1). The next theorem shows that, in fact, a type (3) index can never appear in a graph of $\mathcal{S}$ defined on more than one vertex:

Theorem 3.8 There is no minimal symplectic plumbing tree $\Gamma \in \mathcal{S}$ on $n>1$ vertices involving an index of type (3).

Proof A simple check shows that the theorem holds for $n=2$. Suppose that $\Gamma$ is a plumbing tree on $n$ vertices $(n \geq 3)$ and it involves an embedding into $n\langle-1\rangle$ with an index $i$ of type (3). Consider such a $\Gamma$ with the smallest possible $n$. Let $v=E_{i_{v}}-\sum_{j \in J_{v}} E_{j}$ be a leaf of the graph $\Gamma$ (i.e., a vertex of valency one). The existence of such $v$ follows from our assumption $n>1$. It follows from its form that $E_{i}$ does not appear in $v$. If $i_{v}$ is of type (5), (7) or (9) then the sum
$$u=\sum_{v_{j} \neq v} v_{j}$$
of all the other vertices (which form a connected subgraph, since $v$ is a leaf) will contain $-E_{i_{v}}$ with multiplicity at least 2, but $u$ also contains $-2 E_{i}$ (recall that $i$ is the index of type (3)) contradicting Corollary 3.2. If $i_{v}$ is of type (4) (the only remaining possibility), then consider the unique vertex $v^{\prime} \in \Gamma$ with $Q\left(v, v^{\prime}\right)=1$, and distinguish two cases according to whether $-E_{i_{v}}$ does or does not appear in $v^{\prime}$. Suppose first that the unique $-E_{i_{v}}$ is in $v^{\prime}$. By changing $\Gamma$ to $\Gamma^{\prime}$ via replacing the edge $\overline{v v^{\prime}}$ (and its two vertices) by one vertex $v+v^{\prime}$, we eliminate the index $i_{v}$ from the embedding; but $\Gamma^{\prime} \in \mathcal{S}$ is now a minimal symplectic plumbing tree on $(n-1)$ vertices (with an embedding
into $(n-1)\langle-1\rangle)$ which still has $i$ as an index of type (3), contradicting our choice of $\Gamma$. (Notice that since $\left(v+v^{\prime}\right)^{2}=v^{2}+\left(v^{\prime}\right)^{2}+2 \leq v^{2}<-1$, minimality of $\Gamma^{\prime}$ obviously follows.) Finally, if $-E_{i_{v}}$ appears in a vertex $v^{\prime \prime}$ different from $v^{\prime}$ then change $\Gamma$ by deleting $v$ and replacing the vector $v^{\prime \prime}$ by $v^{\prime \prime}+E_{i_{v}}$. Once again, the resulting $\Gamma^{\prime \prime}$ will be contained by $(n-1)\langle-1\rangle$ (since the index $i_{v}$ has been eliminated) and $i$ is still an index of type (3) in $\Gamma^{\prime \prime}$, hence if it is minimal, then it contradicts our choice for $\Gamma$. The plumbing graph $\Gamma^{\prime \prime}$ can contain only a unique vector with square -1: this is $v^{\prime \prime}+E_{i_{v}}$, implying that $v^{\prime \prime}=E_{i_{v^{\prime \prime}}}-E_{i_{v}}$. In this case, however
$$0=Q\left(v, v^{\prime \prime}\right)=1+Q\left(E_{i_{v}}-\sum_{j \in J_{v}} E_{j}, E_{i_{v^{\prime \prime}}}\right) \geq 1,$$
which is a contradiction. \(\square\)

Remark 3.9 Notice that for $n=1$ the plumbing graph (-4) on one vertex (with the embedding $-2 E_{1}$ ) does admit an index of type (3), hence our assumption $n>1$ is essential. In fact, the above theorem can be rephrased as follows: $\Gamma \in \mathcal{S}$ contains an index of type (3) if and only if $|\Gamma|=1$. This form of the previous result will be very helpful in our later arguments, cf. Lemma 5.6.

Remark 3.10 We also note that the line of argument above (considering a leaf $v=E_{i_{v}}-\sum_{j \in J_{v}} E_{j}$, distinguishing two cases according to whether $i_{v}$ is of types (5),(7), (9), or of type (4), and in this latter case examining where $-E_{i_{v}}$ is) will be repeatedly applied throughout the proof of Theorem 1.8.

From the result above we conclude that an index of type (1) in $\Gamma \in \mathcal{S}$ is also impossible once $|\Gamma|>1$. (For a graph $\Gamma$ with $|\Gamma|=1$ the presence of an index of type (1) contradicts the minimality of $\Gamma$.) It follows then that the sum $w=\sum_{v \in \Gamma} v$ is of the form
$$-2 E_{w}-\sum_{j \in J_{w}} E_{j} .$$
In order to analyze more systematically which types of indices can actually occur, let $\left\{v_{1}, \ldots, v_{n}\right\}$ denote the vertices of $\Gamma$ and notice that the sum
$$\sum_{i<j} Q\left(v_{i}, v_{j}\right)$$
is equal to the number of edges in $\Gamma$, and since $\Gamma$ is assumed to be a connected tree, it is equal to $n-1$. The sum (3.2) can be expanded according to the expansions of the vectors $v_{i}$ in the basis $\left\{E_{1}, \ldots, E_{n}\right\}$, and since $Q\left(E_{i}, E_{j}\right)=0$
once $i \neq j$, the sum $n-1=\sum_{i<j} Q\left(v_{i}, v_{j}\right)$ decomposes as the sum of contributions of individual indices through the multiplicity of $Q\left(E_{i}, E_{i}\right)$ appearing in the expansion of (3.2). It is easy to see that for indices of types (4) and (7) this contribution is 1, for type (5) indices it is 2, if $i$ is of type (6) then this contribution is -1 and finally for type (2) and (9) indices it is 0.

Now we can have a better picture about the possible types of indices $\Gamma$ can have. Since $w=\sum_{i=1}^{n} v_{i}$ is of the form $-2 E_{i}-\sum_{j \in J_{i}} E_{j}$, there is exactly one index $i$ of type (6) or (9). A simple analysis shows that
\begin{itemize}
\item[-] (A) If this index $i$ is of type (6), then the remaining $n-1$ indices contribute $n$ to the sum (3.2), therefore one of them must be of type (5). By Proposition 3.4 at most one index of type (5) can exist, so the rest of the indices are either of type (4) or of type (7).
\item[-] (B) If $i$ is of type (9) and there is an index of type (5) among the remaining ones (and then it is necessarily unique), then there exists a unique index of type (2), and the rest of the indices are of types (4) or (7).
\item[-] (C) If $i$ is of type (9) and there is no index of type (5) then all others are of types (4) or (7).
\end{itemize}

In the next three sections we will analyize these three possibilities separately. More precisely, we will verify the following three statements, the combination of which (together with Propositions 4.4, 5.7 and 6.9) prove Theorem 1.8.

Theorem 3.11 If $\Gamma \in \mathcal{S}$ with rank $|\Gamma|=n$ embeds into $n\langle-1\rangle$ with indices as described in Case (A) above then $\Gamma \in \mathcal{G}$.

Theorem 3.12 If $\Gamma \in \mathcal{S}$ with rank $|\Gamma|=n$ embeds into $n\langle-1\rangle$ with indices as described in Case (B) above then $\Gamma \in \mathcal{C}$.

Theorem 3.13 If $\Gamma \in \mathcal{S}$ with rank $|\Gamma|=n$ embeds into $n\langle-1\rangle$ with indices as described in Case (C) above then $\Gamma \in \mathcal{W} \cup \mathcal{N} \cup \mathcal{M} \cup \mathcal{A} \cup \mathcal{B}$.

Before starting the proofs, however, we make some preparatory definitions and observations.

Definition 3.14 A vector $v$ is full if it is of the form $E_{i_{v}}-\sum_{j \in J_{v}} E_{j}$ and $i_{v}$ is of type (5), (7) or (9). The plumbing graph $\Gamma$ is full if it has an embedding with no index of type (4).

Lemma 3.15 A symplectic plumbing tree $\Gamma \in \mathcal{S}$ with $n$ vertices is full if and only if (after possibly reordering the indices)
$$\sum_{i=1}^{n} v_{i}=-E_{1}-E_{2}-\ldots-E_{n-1}-2 E_{n} .$$

Proof By the exclusion of indices of types (1), (3), (4), (8) and (10), in the sum $w=\sum_{v \in \Gamma} v$ each $E_{i}$ comes with multiplicity -1 or -2, and there is a single one with multiplicity -2, verifying the lemma. \(\square\)

Lemma 3.16 A symplectic plumbing tree $\Gamma \in \mathcal{S}$ is full if and only if
$$\sum_{i=1}^{n} v_{i}^{2}=-3 n-1$$

Proof Consider the vector $w=\sum_{i=1}^{n} v_{i}$. It is easy to see that $w^{2}=\sum_{i=1}^{n} v_{i}^{2}+$ $2 \sum_{i<j} v_{i} v_{j}$. Since $\sum_{i<j} v_{i} v_{j}$ counts the number of edges in $\Gamma$, and it is a connected tree, we get that
$$w^{2}=\sum_{i=1}^{n} v_{i}^{2}+2(n-1) .$$
Since by the previous observation $\Gamma$ is full if and only if $w^{2}=-n-3$, the result follows. \(\square\)

Remark 3.17 Notice that according to Corollary 3.3 the graph is full if and only if $\left|\sum_{i=1}^{n} v_{i}^{2}\right|$ is maximal.

Proposition 3.18 The plumbing trees $\Gamma_{p, q, r} \in \mathcal{W}$ are full for all $p, q, r \geq 0$.
Proof A simple direct check provides the proof:
$$\sum v_{i}^{2}=-2(p+q+r)-p-3-q-3-r-3-4=-3(p+q+r+4)-1 .$$ \(\square\)

Similarly, a somewhat more tedious, but straightforward computation shows that

Proposition 3.19 The plumbing trees $\Delta_{p, q, r}, \Lambda_{p, q, r} \in \mathcal{M} \cup \mathcal{N}$ are full for all $p, q, r \geq 0$. \(\square\)

It is not hard to see that the graphs of Figure 10 become full after adding -1, -2, -3 appropriately to the (-1)-vertex. However, the graphs in the families $\mathcal{A}, \mathcal{B}, \mathcal{C}$ are full only in the cases when during the blow-up process we only blow up edges of the configuration.

\section*{4 The classification of graphs of Case (A)}

Before starting the proof of Theorem 3.11 we need a little preparation, showing in particular that the graphs in $\mathcal{G}$ are all full.

\subsection*{4.1 Continued fraction computations}

In this subsection we flesh out Remark (2.8.2) of [33]. Define the class of plumbing trees $\mathcal{G}_{r}$ as the minimal set of plumbing trees which (a) contains $\Gamma=$ (-4) and (b) if the linear chain $\Gamma=\left(-a_{1}, \ldots,-a_{k}\right)$ is in $\mathcal{G}_{r}\left(a_{i} \in \mathbb{N}, a_{i} \geq 2\right)$ then so are $\Gamma_{1}=\left(-2,-a_{1}, \ldots,-a_{n}-1\right)$ and $\Gamma_{2}=\left(-a_{1}-1,-a_{2}, \ldots,-a_{n},-2\right)$. Notice that for all $\Gamma \in \mathcal{G}_{r}$ we have that the tree is, in fact, a chain. Let $\left[a_{1}, \ldots, a_{k}\right]$ (with $a_{i} \geq 2$ integers) denote the value of the continued fraction expansion
$$a_{1}-\frac{1}{a_{2}-\frac{1}{\ddots-\frac{1}{a_{k}}}}$$

Proposition 4.1 The plumbing tree $\Gamma=\left(-a_{1}, \ldots,-a_{k}\right)$ (with $a_{i} \geq 2$ integers) is in $\mathcal{G}_{r}$ if and only if there are relatively prime $p>q>0$ such that
$$\left[a_{1}, \ldots, a_{k}\right]=\frac{p^{2}}{p q-1} .$$

Proof We start the proof with a simple auxiliary result concerning continued fractions. Suppose therefore that $\left[a_{1}, \ldots, a_{k}\right]=\frac{p^{2}}{p q-1}$; we determine the value of $\left[a_{1}+1, \ldots, a_{k}, 2\right]$. In the computation we will use the fact [19, Appendix] that if $\left[b_{1}, \ldots, b_{n}\right]=\frac{u}{v}$ then $\left[b_{n}, \ldots, b_{1}\right]=\frac{u}{v^{\prime}}$, where $v v^{\prime} \equiv 1(\bmod u)$. According to this principle and the definition, we get that
$$\left[a_{1}+1, \ldots, a_{k}\right]=\frac{p^{2}}{p q-1}+1=\frac{p^{2}+p q-1}{p q-1},$$
hence
$$\left[a_{k}, \ldots, a_{1}+1\right]=\frac{p^{2}+p q-1}{p^{2}-q^{2}-2},$$
consequently
$$\left[2, a_{k}, \ldots, a_{1}+1\right]=\frac{(p+q)^{2}}{p^{2}+p q-1},$$
implying that
$$\left[a_{1}+1, \ldots, a_{k}, 2\right]=\frac{(p+q)^{2}}{q(p+q)-1} .$$
In a similar manner we get that
$$\left[2, a_{1}, \ldots, a_{k}+1\right]=\frac{(p+q)^{2}}{p(p+q)-1} .$$
Consider now a tree $\Gamma \in \mathcal{G}_{r}$, given by the array $\left(-a_{1}, \ldots,-a_{k}\right)$. Using induction on $k$ it is fairly easy to see that the statement of the Proposition holds: for $\Gamma=(-4)$ choose $p=2$ and $q=1$; otherwise $\Gamma$ is constructed from $\Gamma^{\prime}$ of shorter length, hence induction, the above computation and the fact that $p+q$ and $q$ are relatively prime if and only if $p$ and $q$ are, conclude one direction of the proof.

Suppose now that $\Gamma$ is given by an array $\left(-a_{1}, \ldots,-a_{k}\right)$ such that $\left[a_{1}, \ldots, a_{k}\right]=$ $\frac{p^{2}}{p q-1}$ for some relatively prime integers $p$ and $q$. Induction on the length of the Euclidean algorithm for determining $(p, q)=1$, together with the above formulae and the uniqueness of the continued fraction expansion readily imply the converse direction. \(\square\)

Notice that, as a consequence of the above result, elements of $\mathcal{G}$ are exactly the plumbing chains considered in [23] as generalized rational blow-downs. In particular, $\mathcal{G}_{r}=\mathcal{G}$.

Proposition 4.2 For any $p>q>0$ relative prime, the symplectic plumbing tree $\Gamma_{p / q}$ is full.

Proof Since for $|\Gamma|=1$ the graph (-4) is full, and the inductive step constructing elements of $\mathcal{G}_{r}$ decreases $\sum v_{i}^{2}$ by 3 when increasing the number of vertices by 1, it is obvious that elements of $\mathcal{G}_{r}$ are full. Now the above identification of $\mathcal{G}$ with $\mathcal{G}_{r}$ concludes the proof. \(\square\)

\subsection*{4.2 The proof of Theorem 3.11}

After these preliminary results we are ready to prove Theorem 3.11. It turns out to be more convenient to prove a slightly stronger statement than Theorem 3.11, which obviously implies the result.

Proposition 4.3 Suppose that $\Gamma \in \mathcal{S}$ involves an index $t$ of type (6), that is, $\Gamma$ is listed in Case (A). Then $\Gamma \in \mathcal{G}$ with the additional property that the two vectors containing $-E_{t}$ are the two endpoints of the plumbing chain.

Proof The proof will proceed by induction on $n=|\Gamma|$. The statement is easy to check for $n=2$. Consider a graph $\Gamma$ on $n$ vertices; by our inductive hypothesis we can assume that for all $k<n$ the symplectic plumbing trees of Case (A) defined on $k$ vertices satisfy the conclusion of the proposition. We can also assume that $n \geq 3$.

First we show that if the two vectors $v_{1}, v_{2}$ containing $-E_{t}$ are leaves of $\Gamma$ then $\Gamma \in \mathcal{G}$. Add $E_{t}$ to $v_{1}, v_{2}$ and delete the one (call it $v$ ) which has smaller decoration in absolute value. The resulting plumbing tree $\Gamma^{\prime} \in \mathcal{S}$, defined on $(n-1)$ vertices, is still connected (since we deleted a leaf), and it is embedded in $(n-1)\langle-1\rangle=\oplus_{i \neq t}\left\langle E_{i}\right\rangle$. It follows from the above construction that $\Gamma^{\prime}$ still has no index of type (9), therefore it is still of Case (A). We claim that $\Gamma^{\prime}$ is also minimal. If it contains a vertex of the form $E_{i}$, then the two leaves $v_{1}, v_{2}$ of $\Gamma$ containing $-E_{t}$ had the shape $v_{1}=E_{v_{1}}-E_{t}$ and $v_{2}=E_{v_{2}}-E_{t}$. This implies $Q\left(v_{1}, v_{2}\right)=-1$, a contradiction. Therefore $\Gamma^{\prime}$ is minimal, and so by our inductive hypothesis we have that $\Gamma^{\prime} \in \mathcal{G}$ and the index $t^{\prime}$ of type (6) appears in the two leaves of $\Gamma^{\prime}$. Since a graph in $\mathcal{G}$ is full, for the deleted vector $v$ we have $\left|v^{2}\right| \leq 2$, therefore it can only have the shape $v=E_{t^{\prime}}-E_{t}$. This observation readily implies that $\Gamma$ can be built from $\Gamma^{\prime}$ by adding $-E_{t}$ to the vector on one of its ends, and concatenating $\Gamma^{\prime}$ with a new vector $v$ having $v^{2}=-2$ on the other end. Since $\Gamma^{\prime} \in \mathcal{G}$, this shows that $\Gamma \in \mathcal{G}$. We also see that in $\Gamma$ the vectors involving type (6) indices are on the two ends of the plumbing chain.

Suppose now that (at least) one of the vectors $v_{1}, v_{2}$ containing $-E_{t}$ is not a leaf, say it is $v_{1}$. Our goal is to derive a contradiction from this assumption. Since $|\Gamma| \geq 3$, it has at least two leaves, therefore we have a leaf $v$ with $Q\left(v, E_{t}\right)=0$. The vector $v$ cannot be full, since then $\sum_{u \neq v} u$ would contain both $E_{i_{v}}$ and $E_{t}$ with multiplicity -2. Similarly, by Corollary 3.5 the vector $v$ cannot be of the form $-2 E_{i_{v}}-\sum_{j \in J_{v}} E_{j}$ either. So we can assume that $v=E_{i_{v}}-\sum_{j \in J_{v}} E_{j}$ and $i_{v}$ is of type (4), that is, there is a single further $-E_{i_{v}}$ in one of the vectors of $\Gamma$. Let $v^{\prime}$ denote the single vector adjacent to $v$ in $\Gamma$. If $-E_{i_{v}}$ is not in $v^{\prime}$, then we can erase $v$ from $\Gamma$ and $-E_{i_{v}}$ from the vector $w$ containing it, and the resulting graph $\Gamma^{\prime}$ (now on $(n-1)$ vertices, with an embedding into $\left.(n-1)\langle-1\rangle=\oplus_{i \neq i_{v}}\left\langle E_{i}\right\rangle\right)$ is still minimal. Indeed, we changed only $w$, hence $\Gamma^{\prime}$ is nonminimal only if $w$ was of the form $E_{i_{w}}-E_{i_{v}}$, in which case $Q(v, w) \geq 1$, giving a contradiction, since $w \neq v^{\prime}$ and $v^{\prime}$ is the only vector having nontivial pairing with $v$. Noting that the adjunction equality (1.1) still holds at $w, \Gamma^{\prime} \in \mathcal{S}$. The graph $\Gamma^{\prime}$ still does not have any index of type (9), hence by induction $\Gamma^{\prime} \in \mathcal{G}$ and so $\Gamma^{\prime}$ is full. As before, this fact implies $\left|v^{2}\right| \leq 2$, hence either $v=E_{i_{v}}$ (contradicting the minimality of $\Gamma$ ) or
$v=E_{i_{v}}-E_{j}$. Then $v^{\prime}=E_{j}-\sum_{k \in J_{v^{\prime}}} E_{k}$, hence after deleting $v$ the vector $v^{\prime}$ in $\Gamma^{\prime}$ will not be full, providing the desired contradiction.

In the last case to consider, when $-E_{i_{v}}$ is in $v^{\prime}$, we need to refine the above argument in order to prove minimality for $\Gamma^{\prime}$. Modify $\Gamma$ first by adding $v$ to $v^{\prime}$; notice that with this move we eliminated the index $i_{v}$, hence the resulting $\Gamma^{\prime \prime}$ embeds into $(n-1)\langle-1\rangle$. Since $\left(v+v^{\prime}\right)^{2} \leq v^{2} \leq-2$ and the adjunction equality (1.1) holds for $v+v^{\prime}$, it follows that $\Gamma^{\prime \prime}$ is in $\mathcal{S}$ involving no index of type (9), hence by induction $\Gamma^{\prime \prime} \in \mathcal{G}$ and $v_{1}, v_{2}$ (containing $-E_{t}$ ) are both leaves in $\Gamma^{\prime \prime}$, although $v_{1}$ was not a leaf in $\Gamma$. This shows that $v^{\prime}=v_{1}$, hence by deleting $v$ from $\Gamma$ and $-E_{i_{v}}$ from $v^{\prime}=v_{1}$ we get a minimal graph $\Gamma^{\prime}$, since $v_{1}=v^{\prime}$ still contains $-E_{t}$. Therefore the argument given for the case above applies and provides the desired contradiction, completing the proof. \(\square\)

For the proof of Theorem 1.8 we also need
Proposition 4.4 If $\Gamma \in \mathcal{G}$ then $\Gamma \in \mathcal{S}$.
Proof For the graph $\Gamma \in \mathcal{G}$ with $|\Gamma|=1$ the statement is obvious: since $\Gamma$ is full, it is (-4) and so the embedding $v \mapsto-2 E$ is suitable. If $\Gamma \subset(n-1)\langle-1\rangle=$ $\oplus_{i=1}^{n}\left\langle E_{i}\right\rangle$ with $-E_{t}$ in $v_{1}, v_{2}$ on the two ends of the plumbing chain (recall that $t$ is of type (6)), then the new vector $E_{t}-E_{n}$ and the modification $v_{2}-E_{n}$ provides an appropriate embedding of the next element $\Gamma_{\text {next }} \in \mathcal{G}$ into $n\langle-1\rangle$. (See also the arguments in Sections 7 and 8.) \(\square\)

\section*{5 Classification of graphs of Case (B)}

Before examining the graphs listed under Case (B), we need a little preparation.

\subsection*{5.1 Generalities for embeddings of Cases (B) and (C)}

Notice first that a simple case-by-case check shows that on 4 vertices there are exactly three graphs in $\mathcal{S}$ with embeddings into $4\langle-1\rangle$ of Cases (B) and (C); these configurations are shown by Figure 1. Notice that these graphs are all full and the graph of Figure 1(a) is both in $\mathcal{W}$ and in $\mathcal{A}$; similarly Figure 1(b) belongs to both the families $\mathcal{N}$ and $\mathcal{B}$, and Figure 1(c) to both $\mathcal{M}$ and $\mathcal{C}$.

Definition 5.1 A vector $v=E_{i_{v}}-\sum_{j \in J_{v}} E_{j}$ in the minimal plumbing tree $\Gamma$ is called reducible if the further $-E_{i_{v}}$ 's are contained exactly by the vectors adjacent to $v$. That is, $Q(v, w)=1$ if and only if $Q\left(E_{i_{v}}, w\right)=1$.

Note that for a reducible vector $v=E_{i_{v}}-\sum_{j \in J_{v}} E_{j}$ we have that $Q\left(-\sum_{j \in J_{v}} E_{j}, w\right)=$ 0 for all $w \neq v$ in $\Gamma$ : If $Q(v, w)=0$ then $w$ contains no $-E_{i_{v}}$ by the reducibility of $v$, hence $Q\left(-\sum_{j \in J_{v}} E_{j}, w\right)=Q(v, w)=0$. If $Q(v, w)=1$ then
$$1=Q(v, w)=Q\left(E_{i_{v}}, w\right)+Q\left(-\sum_{j \in J_{v}} E_{j}, w\right)=1+Q\left(-\sum_{j \in J_{v}} E_{j}, w\right),$$
which implies the statement. For example the central (that is, of valency three) vertices of the graphs of Figure 1 under the embeddings given by Propositions 5.7 and 6.9 are reducible. Notice that the valency of a reducible vector $v$ is 1, 2 or 3, and in the last case $v=E_{1}-\sum_{j \in J_{1}} E_{j}$ where 1 is the index of type (9). The presence of a reducible vector will be convenient when applying inductive proofs.

Proposition 5.2 Consider the graph $\Gamma \in \mathcal{S}$ with indices either of Case (B) or of Case (C). Suppose that in $\Gamma$ all leaves are full. Then $\Gamma$ is full.

Proof We start with the observation that such a graph admits a unique vertex of valency three and all others are of valency $\leq 2$. This follows from the fact that if 1 denotes the index of type (9) then every leaf $v \in \Gamma$ must contain $-E_{1}$; otherwise, the sum $\sum_{u \neq v} u$ would have both $-2 E_{i_{v}}$ and $-2 E_{1}$. (The case $i_{v}=1$ is easily excluded.) Therefore there are at most three leaves and if there are only two, then the sums of the two sides of $v_{1}=E_{1}-\sum_{j \in J_{1}} E_{j}$ are $-2 E_{1}-\sum_{j \in J^{\prime}} E_{j}$ and $E_{i}-E_{1}-\sum_{j \in J^{\prime \prime}} E_{j}$, and these two vectors pair negatively. In addition, if $v=E_{i_{v}}-\sum_{j \in J_{v}} E_{j}$ is a full leaf, then one $-E_{i_{v}}$ is in another leaf: by considering the sum $u$ of all vectors which are not leaves we see that $u$ contains $E_{1}$ with multiplicity +1 and so it cannot contain $-2 E_{i_{v}}$.

Turning to the proof of the proposition, suppose first that there is a reducible vector $v=E_{i_{v}}-\sum_{j \in J_{v}} E_{j}$ in $\Gamma$. Since all leaves are full, no reducible vector of valency 1 exists in $\Gamma$. If $v$ is of valency two, then change $v$ to $E_{i_{v}}$, blow down $E_{i_{v}}$ and add $v-E_{i_{v}}=-\sum_{j \in J_{v}} E_{j}$ to the potential (-1)-vertex. (If there is no (-1)-vertex in the blown down graph then add it to any vector of the graph.) In this way we get a minimal tree in $\mathcal{S}$, still of Case (B) or (C), with full leaves, therefore induction applies and so the blown down graph is full. Since we changed the sum of the squares by 3, it shows that $\Gamma$ was full. If the reducible vector is of valency three, then it is equal to $v_{1}=E_{1}-\sum_{j \in J_{1}} E_{j}$ (where 1 is the index of type (9)), and since the leaves are full, we have $n=4$ : any leaf must contain $-E_{1}$ but since $v_{1}$ is reducible, all vectors containing - $E_{1}$ are adjacent to $v_{1}$. The graphs in $\mathcal{S}$ on 4 vertices (given by Figure 1) are known to be full.

In the case when there is no reducible vector we need a lemma:

Lemma 5.3 Let $w \in \Gamma$ be a vector different from the central vector $v_{1}$ (of valency three) and let the vector next to $w$ in the path connecting $w$ to the central vector $v_{1}$ be denoted by $w^{\prime}$. Suppose that there is no reducible vector on the path between $w$ and $v_{1}$. Then $-E_{i_{w}}$ is in $w^{\prime}$.

Proof If $w_{1}=w, w_{2}=w^{\prime}, w_{3}, \ldots, w_{k}=v_{1}$ denote the vectors on the path connecting $w$ with $v_{1}$ then $w_{k-1}$ does not admit $E_{i_{v_{1}}}=E_{1}$ (since besides $v_{1}$ this basis vector is in leaf only), so $w_{k}=v_{1}$ must contain $-E_{w_{k-1}}$ in order $Q\left(w_{k-1}, w_{k}\right)=1$ to hold. Since $w_{k-1}$ is not reducible, the potential other $-E_{w_{k-1}}$ cannot be in $w_{k-2}$, implying that $w_{k-1}$ must contain $-E_{w_{k-2}}$. Applying the same principle we arrive to the fact that $w^{\prime}=w_{2}$ contains $-E_{i_{w}}$. \(\square\)