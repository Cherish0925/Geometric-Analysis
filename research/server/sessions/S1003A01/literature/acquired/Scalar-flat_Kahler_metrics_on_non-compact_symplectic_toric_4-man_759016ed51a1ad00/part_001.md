---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Scalar-flat Kahler metrics on non-compact symplectic toric 4-manifolds]

---
source_file: 0910_5466.pdf
converter: mathpix
format: mmd
---

\title{
SCALAR-FLAT KÄHLER METRICS ON NON-COMPACT SYMPLECTIC TORIC 4-MANIFOLDS
}

\author{
MIGUEL ABREU AND ROSA SENA-DIAS
}

\begin{abstract}
In a recent paper Donaldson [D1] explains how to use an older construction of Joyce J] to obtain four dimensional local models for scalarflat Kähler metrics with a 2-torus symmetry. In [D2], using the same idea, he recovers and generalizes the Taub-NUT metric by including it in a new family of complete scalar-flat toric Kähler metrics on $\mathbb{R}^{4}$. In this paper we generalize Donaldson's method and construct complete scalar-flat toric Kähler metrics on any symplectic toric 4-manifold with "strictly unbounded" moment polygon. These include the asymptotically locally Euclidean scalar-flat Kähler metrics previously constructed by Calderbank and Singer [CS], as well as new examples of complete scalar-flat toric Kähler metrics which are asymptotic to Donaldson's generalized Taub-NUT metrics. Our construction is in symplectic action-angle coordinates and determines all these metrics via their symplectic potentials. When the first Chern class is zero we obtain a new description of known Ricci-flat Kähler metrics.
\end{abstract}

\section*{1. Introduction}

The problem of finding constant scalar curvature Kähler metrics has been a source of a lot of interesting work in Kähler geometry. In particular a lot of effort has been put in proving a general existence result for such metrics, under suitable hypothesis in the compact case. Recently, this problem was completely settled for smooth compact toric complex surfaces by Donaldson in [D2], using a particularly nice feature of toric manifolds: the existence of global symplectic action-angle coordinates, where compatible toric complex structures can be easily parametrized via a symplectic potential function (see [A2]). However, even in this case, these compact constant scalar curvature Kähler metrics remain somewhat elusive and it is quite hard to find explicit examples.

A Kähler metric on a complex surface is
\begin{itemize}
\item[(i)] scalar-flat iff it is anti-self-dual, and
\item[(ii)] Ricci-flat iff it is hyperkähler.
\end{itemize}
There are several constructions that use these facts to produce explicit examples of scalar-flat Kähler metrics, notably in the non-compact toric setting:
\begin{itemize}
\item[-] The gravitational instantons of Gibbons, Hawking, Hitchin and Kronheimer [GH, Hi, K], give asymptotically locally Euclidean (ALE) Ricci-flat Kähler metrics on toric resolutions $A_{p}$ of orbifolds of the form $\mathbb{C}^{2} / \Gamma_{p}$, where $\Gamma_{p}$ is a finite subgroup of $S U(2)$ of order $p \in \mathbb{N}$. When $p=1$ one gets the standard flat metric on $A_{1}=\mathbb{C}^{2}$, and when $p=2$ one gets the Eguchi-Hanson metric on the total space of the line bundle $\mathcal{O}(-2)$ over $\mathbb{C P}^{1}$.
\item[-] LeBrun L1, L2] constructs ALE scalar-flat Kähler metrics on toric resolutions of orbifolds of the form $\mathbb{C}^{2} / \Gamma$, where $\Gamma$ is a finite cyclic diagonal
\end{itemize}

\footnotetext{
Partially supported by the Fundação para a Ciência e a Tecnologia (FCT/Portugal).
}
\begin{itemize}
\item[] subgroup of $U(2)$. These correspond to the total spaces of the line bundles $\mathcal{O}(-k)$ over $\mathbb{C P}^{1}$. When $k=1$ one gets the Burns metric on $\mathcal{O}(-1)$.
\item[-] Joyce, Calderbank and Singer J, CS], construct ALE scalar-flat Kähler metrics on toric resolutions of orbifolds of the form $\mathbb{C}^{2} / \Gamma$, where $\Gamma$ is a finite cyclic subgroup of $U(2)$ such that $\mathbb{C}^{2} / \Gamma$ has an isolated singular point at the origin. A crucial ingredient in [CS] is the work of Calderbank and Pedersen [CP] expressing Joyce's construction in terms of axi-symmetric harmonic functions on $\mathbb{R}^{3}$.
\item[-] LeBrun [L3] studies the asymptotically locally flat (ALF) Ricci-flat Kähler metrics constructed by Hawking [Ha] on the above $A_{p}$ resolutions. These give the Taub-NUT metric on $A_{1}=\mathbb{C}^{2}$ and "multi Taub-NUT metrics" on the other $A_{p}$.
\end{itemize}

In this paper we describe an explicit method to obtain ALE and "generalized Taub-NUT" scalar-flat toric Kähler metrics on any smooth toric complex surface $X$ that can be obtained as a finite sequence of blow ups of a minimal resolution of $\mathbb{C}^{2} / \Gamma$, with $\Gamma$ some finite ciclic subgroup of $U(2)$. These include all of the above metrics, together with the Taub-NUT version of the scalar-flat Kähler metrics constructed in [CS].

Our method is based on the recent work of Donaldson [D1], where he shows how to translate the work of Joyce [J] into the framework of symplectic actionangle coordinates, describing a process to write down symplectic potentials of local scalar-flat toric Kähler metrics. In [D2], section 6, he uses this method to recover the symplectic potentials of the flat and Taub-NUT metrics on $\mathbb{R}^{4}$. Moreover, he shows how the Taub-NUT metric can be included in a new family of complete scalar-flat toric Kähler metrics on $\mathbb{R}^{4}$. We will often refer to these metrics as Donaldson's generalized Taub-NUT metrics or simply as generalized Taub-NUT metrics. We extend Donaldson's method to general non-compact symplectic toric 4-manifolds. This allows us to do the following:
\begin{itemize}
\item[-] First, we explicitly construct the symplectic potential of an ALE scalarflat toric Kähler metric for any (strictly) unbounded symplectic toric 4manifold. Although it follows from the work of Fujiki [F] and Wright [W1] that these metrics are isometric to the ones constructed in [CS], our point of view is different. See also [W2] for yet another description of these metrics.
\item[-] Second, again for any (strictly) unbounded symplectic toric 4-manifold, we explicitly construct the symplectic potential of a family of complete scalarflat toric Kähler metrics which are asymptotic to Donaldson's generalized Taub-NUT metrics.
\end{itemize}
By a strictly unbounded symplectic toric 4-manifold we roughly mean one whose moment polygon has two non-parallel unbounded edges (see Section 2). As we show in Proposition 2.8, this is the precise symplectic counterpart of "a finite sequence of blow ups of a minimal resolution of $\mathbb{C}^{2} / \Gamma$, with $\Gamma$ a finite cyclic subgroup of $U(2)$ such that $\mathbb{C}^{2} / \Gamma$ has an isolated singular point at the origin".

Our construction is explicit up to inverting an algebraic function. Moreover, in the case where $c_{1}=0$, we can determine which of the metrics constructed above are Ricci-flat. One can check that those are the gravitational instantons and multi Taub-NUT metrics

To summarize, we prove the following theorem.

Theorem 1.1. Any strictly unbounded symplectic toric 4-manifold admits an ALE scalar-flat toric Kähler metric as well as a two parameter family of complete scalarflat toric Kähler metrics, each of which is asymptotic to a Donaldson generalized Taub-NUT metric.

Any strictly unbounded symplectic toric 4-manifold with $c_{1}=0$ admits an ALE Ricci-flat toric Kähler metric as well as a one parameter family of complete Ricciflat toric Kähler metrics, each of which is asymptotic to a Taub-NUT metric.

Remark 1.2. The above family of generalized scalar-flat Taub-NUT metrics is naturally parametrized by points in the interior of a cone in $\mathbb{R}^{2}$. This cone is determined by the (ordered) pair of non-parallel unbounded edges of the moment polygon of the symplectic toric 4-manifold (see Remark 4.2). When $c_{1}=0$, the above family of generalized Ricci-flat Taub-NUT metrics corresponds to points in a ray in the interior of this cone (see Lemma 6.2 and Lemma 6.3).

Remark 1.3. The precise meaning of "asymptotic to a generalized Taub-NUT metric" is explained in the proof of Proposition 5.1. A further analysis of the asymptotic behaviour of this family of metrics will be carried out in [AS], where we will also prove that these are the only complete scalar-flat toric Kähler metrics on strictly unbounded symplectic 4-manifolds. Here we will limit ourselves to identifying in Proposition 5.6, for each metric in the 2-parameter family of generalized Taub-NUT metrics in the above theorem, a unique 1-dimensional subspace of the Lie algebra of $\mathbb{T}^{2}$ whose vectors induce vector fields on $X$ with bounded length.

This 1-dimensional subspace encodes significant information about the metric's asymptotic behaviour. When it is "rational", i.e. the Lie algebra of a circle subgroup $S^{1} \subset \mathbb{T}^{2}$, one might expect that the metric is ALF. In fact, this happens in the $c_{1}=0$ cases for the 1-parameter family of Ricci-flat metrics. In these cases this circle $S^{1} \subset \mathbb{T}^{2}$ corresponds to the $S^{1}$-symmetry mentioned in [L3] and one can use the 4-dimensional case of the more general classification result of Bielawski [B] to identify this 1-parameter family of Ricci-flat metrics with the ALF "multi Taub-NUT metrics". When this 1 -dimensional subspace is "irrational", i.e. the Lie algebra of a dense 1-parameter subgroup of $\mathbb{T}^{2}$, the asymptotic behaviour is not as clear and here we will only characterize it as asymptotic to one of Donaldson's generalized Taub-NUT metrics on $\mathbb{R}^{4}$.

Remark 1.4. Using Remark 2.6 and the set-up of [A3], this theorem can be easily generalized to unbounded symplectic toric 4-orbifolds.

The paper is organized as follows. In Section 2 we give a precise definition and characterization of (strictly) unbounded symplectic toric 4-manifolds. We also describe how toric Kähler metrics on these manifolds can be parametrized using action-angle coordinates and symplectic potentials. In Section 3 we review Donaldson's version of Joyce's construction. In this version, the construction gives the symplectic potential of any local scalar-flat toric Kähler metric. In Section 4 we show how to make this construction compatible with boundary conditions arising from an unbounded moment polygon. In Section 5 we analyze the asymptotic behavior of the constructed metrics. In Section 6 we specialize to the $c_{1}=0$ case and determine which of the constructed metrics are Ricci-flat. Finaly, in Section 7 we carry out the construction process very explicitly in several examples to obtain concrete symplectic potentials. In particular, we write down the explicit formula for the symplectic potential of the family of generalized Taub-NUT metrics on the total
space of the line bundle $\mathcal{O}(-2)$ over $\mathbb{C P}^{1}$. These are the simplest new scalar-flat toric Kähler metrics obtained in this paper.

Acknowledgments: The first author thanks José Natário for useful conversations. The second author thanks Peter Kronheimer for encouragement and helpful discussions. We both thank Simon Donaldson and Claude Lebrun for relevant comments.

After posting this paper on the arXiv, the authors learned that Dominic Wright sketched in his 2009 Ph.D thesis [W3] a construction related to the one we use in the proof of Theorem 1.1. We thank him for pointing this out and for sending us a copy of his thesis.

\section*{2. Toric Kähler metrics on unbounded symplectic toric 4-manifolds}

In this section we give a precise definition and characterization of (strictly) unbounded symplectic toric 4-manifolds. We also describe how toric Kähler metrics on these manifolds can be parametrized using action-angle coordinates and symplectic potentials.

\subsection*{2.1. Unbounded symplectic toric 4-manifolds.}

Definition 2.1. A symplectic toric 4-manifold is a connected 4-dimensional symplectic manifold $(X, \omega)$ equipped with an effective Hamiltonian action $\tau: \mathbb{T}^{2} \rightarrow$ $\operatorname{Diff}(X, \omega)$ of the standard (real) 2 -torus $\mathbb{T}^{2}=\mathbb{R}^{2} / 2 \pi \mathbb{Z}^{2}$, such that the corresponding moment map $\mu: X \rightarrow \mathbb{R}^{2}$, well-defined up to a constant, is proper onto its convex image $P=\mu(X) \subset \mathbb{R}^{2}$.

When $X$ is compact, the convexity theorem of Atiyah-Guillemin-Sternberg states that $P$ is the convex hull of the image of the points in $X$ fixed by $\mathbb{T}^{2}$, i.e. a compact convex polygon in $\mathbb{R}^{2}$. A theorem of Delzant [De] then says that this compact convex polygon $P \subset \mathbb{R}^{2}$ completely determines the symplectic toric manifold, up to equivariant symplectomorphisms.

Delzant's theorem can be generalized to the class of non-compact symplectic toric 4-manifolds considered in the above definition (see [KL] for the general classification of non-compact symplectic toric manifolds). In order to state this generalization one needs the following definition.

Definition 2.2. A moment polygon is a convex polygonal region $P \subset \mathbb{R}^{2}$ such that:
\begin{itemize}
\item[(1)] any edge has an interior normal $\nu$ which is a primitive vector of the lattice $\mathbb{Z}^{2}$;
\item[(2)] for any pair of intersecting edges, the corresponding interior normals determined by (1) form a $\mathbb{Z}$-basis of the lattice $\mathbb{Z}^{2}$.
\end{itemize}

Two moment polygons are isomorphic if one can be mapped to the other by a translation in $\mathbb{R}^{2}$.

Theorem 2.3. Let $(X, \omega, \tau)$ be a symplectic toric 4-manifold, with moment map $\mu: X \rightarrow \mathbb{R}^{2}$. Then $P \equiv \mu(X)$ is a moment polygon.

Two symplectic toric 4-manifolds are equivariant symplectomorphic (with respect to a fixed torus acting on both) if and only if their associated moment polygons are isomorphic. Moreover, every moment polygon arises from some symplectic toric 4-manifold.

Non-compact sumplectic toric manifolds can have an infinite number of fixed points. As specified in the following definition, we will not consider that possibility in this paper.

Definition 2.4. A symplectic toric 4-manifold is said to be unbounded if its moment polygon is unbounded and has a finite number of vertices

A symplectic toric 4-manifold is said to be strictly unbounded if it is unbounded, and its moment polygon has non-parallel unbounded edges.

Remark 2.5. When $P$ is the moment polygon of an unbounded symplectic toric 4manifolds, we will order its edges $E_{1}, \ldots, E_{d}$, and corresponding primitive interior normals $\nu_{1}, \ldots, \nu_{d}$, so that:
\begin{itemize}
\item[(i)] $E_{1}$ and $E_{d}$ are the unbounded edges of $P$.
\item[(ii)] $E_{i-1} \cap E_{i} \neq \emptyset$ and $\operatorname{det}\left(\nu_{i-1}, \nu_{i}\right)=-1$, for all $i=2, \ldots, d$.
\end{itemize}

Some well known examples of strictly unbounded symplectic toric 4-manifolds are minimal resolutions of $\left(\mathbb{R}^{4} \cong \mathbb{C}^{2}\right) / \Gamma$, where $\Gamma$ is a finite cyclic subgroup of U(2) such that $\mathbb{C}^{2} / \Gamma$ has an isolated singular point at the origin (see the proof of Proposition 2.8 below). For every choice of coprime integers $0<q<p$ there is one such $\Gamma \subset U(2)$, generated by
$$\left(\begin{array}{cc}
e^{\frac{2 i \pi}{p}} & 0 \\
0 & e^{\frac{2 i \pi q}{p}}
\end{array}\right) .$$
Note that $\Gamma \subset S U(2)$ iff $q=p-1$. These are the $\Gamma_{p} \subset S U(2)$ mentioned in the introduction.

The simplest example of an unbounded symplectic toric 4-manifold which is not strictly unbounded is $S^{2} \times \mathbb{R}^{2}$ with standard product symplectic form and $\mathbb{T}^{2}$-action. Its unbounded moment polygon is
$$P=\{(x, y): y \in[0, a], x \geq 0\}$$
where $a>0$ parametrizes the symplectic area of $S^{2} \times\{0\}$, i.e. the cohomology class of the symplectic form. Although Theorem 1.1 does not apply, $S^{2} \times \mathbb{R}^{2}$ does carry an obvious zero scalar curvature toric Kähler metric: the round metric on $S^{2}$ times the hyperbolic metric on $\mathbb{R}^{2}$. However, this metric is neither ALE nor ALF. Moreover, $S^{2} \times \mathbb{R}^{2}$ equipped with the complex structure determined by this metric is biholomorphic to $\mathbb{C P}^{1} \times D$, where $D \subset \mathbb{C}$ is the disc, while the smooth toric complex surface that the moment polygon $P$ naturally determines is $\mathbb{C P}^{1} \times \mathbb{C}$.

Remark 2.6. One can use the work of Lerman and Tolman [LT] to generalize Theorem 2.3 to orbifolds. The outcome is a classification of symplectic toric 4-orbifolds via rational labeled moment polygons, i.e. moment polygons where " $\mathbb{Z}$ -basis" in (2) of Definition 2.2 is replaced by "Q-basis" and one attaches a positive integer label to each edge.

Each edge $E$ of a rational moment polygon $P \subset \mathbb{R}^{2}$ determines a unique lattice vector $\nu_{E} \in \mathbb{Z}^{2}$ : the primitive inward pointing normal lattice vector. A convenient way of thinking about a positive integer label $m_{E} \in \mathbb{N}$ attached to $E$ is by dropping the primitive requirement from this lattice vector: consider $m_{E} \nu_{E}$ instead of $\nu_{E}$.

In other words, a rational labeled moment polygon can be defined as a rational polygonal region $P \subset \mathbb{R}^{2}$ with an inward pointing normal lattice vector associated to each of its edges. Using this definition and the set-up of [A3], the contents of this paper generalize immediately to unbounded symplectic toric 4-orbifolds.
2.2. The smooth toric complex surface determined by a symplectic toric 4-manifold. The proof of Theorem 2.3 gives an explicit construction of a canonical model for each symplectic toric 4-manifold, i.e. it associates to each moment polygon $P$ an explicit symplectic toric 4-manifold $\left(X_{P}, \omega_{P}, \tau_{P}\right)$ with moment map $\mu_{P}: X_{P} \rightarrow P$. Moreover, since this explicit construction consists of a certain Kähler reduction of the standard $\mathbb{C}^{d}$, for $d=$ number of edges of $P, X_{P}$ has a canonical $\mathbb{T}^{2}$-invariant complex structure $J_{P}$ compatible with $\omega_{P}$. In other words, each symplectic toric 4-manifold is Kähler and to each moment polygon $P \subset \mathbb{R}^{2}$ one can associate a canonical toric Kähler surface $\left(X_{P}, \omega_{P}, J_{P}, \tau_{P}\right)$ with moment map $\mu_{P}: X_{P} \rightarrow P$. In particular, to each moment polygon $P \subset \mathbb{R}^{2}$ one can associate a canonical smooth toric complex surface $\left(X_{P}, J_{P}, \tau_{P}\right)$.

There is another natural way to associate a smooth toric complex surface to a moment polygon $P \subset \mathbb{R}^{2}$. One considers the fan $F_{P}$ determined by the interior normals to the edges of $P$ and the smooth toric complex surface $X_{F_{P}}$ determined by this fan.

The following well-known result relates these two smooth toric complex surfaces naturally associated to a moment polygon.
Proposition 2.7. $\left(X_{P}, J_{P}, \tau_{P}\right)$ and $X_{F_{P}}$ are biholomorphic smooth toric complex surfaces.

The next proposition shows that the smooth toric complex surfaces determined by the symplectic toric 4-manifolds considered in Theorem 1.1 are the same as the ones appearing in [CS].

Proposition 2.8. Let $X$ be a strictly unbounded symplectic toric 4-manifold. Then, as a smooth complex surface, $X$ can be obtained as a finite sequence of blow ups of a minimal resolution of $\mathbb{C}^{2} / \Gamma$, where $\Gamma$ is a finite cyclic subgroup of $U(2)$ such that $\mathbb{C}^{2} / \Gamma$ has an isolated singular point at the origin.
Proof. Let $P$ be the moment polygon of $X$. By considering a change of basis of the torus $\mathbb{T}^{2}$, we may assume that one of the unbounded edges of $P$ is the $x_{1}$-axis, with interior normal the vector (0, 1), and the other unbounded edge has interior normal $(p,-q)$, with coprime $p, q \in \mathbb{N}$ such that $0<q<p$. Let $\Gamma$ be the subgroup of $U(2)$ generated by
$$\left(\begin{array}{cc}
e^{\frac{2 i \pi}{p}} & 0 \\
0 & e^{\frac{2 i \pi q}{p}}
\end{array}\right) .$$
Then $Y=\mathbb{C}^{2} / \Gamma$ is a toric orbifold whose moment polygon has two unbounded edges with normals $(0,1)$ and $(p,-q)$, and no bounded edges. Denote by $X_{0}$ the minimal toric resolution of $Y$. The normals to the edges of the moment polygon of $X_{0}$ can be obtained from the continued fraction expansion of $q / p$. Minimality implies that any other toric resolution of $Y$ is an iterated blow up of $X_{0}$. Now the fan of $Y$ has exactly one 2-dimensional cone: the cone determined by $(0,1)$ and $(p,-q)$. As for the fan of $X$, its 2-dimensional cones are the cones determined by the normals of adjacent edges and the union of such cones is the cone determined by $(0,1)$ and $(p,-q)$. So the fan of $X$ is a refinement of the fan of $Y$ and there must be a proper birational map
$$X \rightarrow Y .$$
Since $X$ is smooth, this proves that $X$ is a resolution of $Y$ and thus an iterated blow up of $X_{0}$. \(\square\)

Remark 2.9. The ALE scalar-flat Kähler metrics of Theorem 1.1 are the same as the ones of Theorem $A$ in [CS]. The $d-2$ parameters appearing in [CS] are determined in our setting by the lengths of the bounded edges of an unbounded moment polygon with $d$ edges (see the proof of Theorem 4.1).
2.3. Toric Kähler metrics. A Kähler metric on a symplectic manifold $(M, \omega)$ is given by a compatible complex structure $J \in \mathcal{I}(M, \omega)$, i.e. an integrable complex structure $J$ on $M$ such that $g(\cdot, \cdot):=\omega(\cdot, J \cdot)$ is a Riemannian metric. If the symplectic manifold is toric, a toric Kähler metric is given by a toric compatible complex structure $J \in \mathcal{I}^{\mathbb{T}}(M, \omega)$, i.e. a compatible complex structure that is invariant by the torus action (or equivalently, for which the torus action is holomorphic).

We will now describe how toric compatible complex structures on symplectic toric 4-manifolds can be parametrized using action-angle coordinates and symplectic potentials. In fact, one easily checks that the set-up and results of [A2, A3] extend to the non-compact setting considered in this paper, provided we restrict to the following class of toric compatible complex structures.

Definition 2.10. Let $(X, \omega, \tau)$ be a symplectic toric 4-manifold and denote by $Y_{1}, Y_{2} \in \mathcal{X}(X, \omega)$ the Hamiltonian vector fields generating the 2-torus action. A toric compatible complex structure $J \in \mathcal{I}^{\mathbb{T}}(X, \omega)$ is said to be complete if the $J$ -holomorphic vector fields $J Y_{1}, J Y_{2} \in \mathcal{X}(X)$ are complete. The space of all complete toric compatible complex structures on $(X, \omega, \tau)$ will be denoted by $\mathcal{I}_{c}^{\mathbb{T}}(X, \omega)$.
Remark 2.11. Let $P \subset \mathbb{R}^{2}$ be a moment polygon and $\left(X_{P}, \omega_{P}, J_{P}, \tau_{P}\right)$ its associated smooth toric Kähler surface. As in [A2], Appendix A, one can prove that if $J \in \mathcal{I}_{c}^{\mathbb{T}}\left(X_{P}, \omega_{P}\right)$ is any complete compatible toric complex structure then $\left(X_{P}, J_{P}, \tau_{P}\right)$ and $\left(X_{P}, J, \tau_{P}\right)$ are isomorphic smooth toric complex surfaces.
Remark 2.12. Note that there is no immediate relation between completeness of a toric compatible complex structure and completeness of the associated toric Kähler metric. For example, consider again $S^{2} \times \mathbb{R}^{2}$ with the scalar-flat toric Kähler metric given by the round metric on $S^{2}$ times the hyperbolic metric on $\mathbb{R}^{2}$. Although this metric is complete, the associated complex structure $J$ is not. In fact, $\left(S^{2} \times \mathbb{R}^{2}, J\right)$ is biholomorphic to $\mathbb{C P}^{1} \times D$, where $D \subset \mathbb{C}$ is a disc.

Let $P \subset \mathbb{R}^{2}$ be a moment polygon and $\left(X_{P}, \omega_{P}, \tau_{P}\right)$ its associated symplectic toric 4-manifold with moment map $\mu_{P}: X_{P} \rightarrow P$. Let $\breve{P}$ denote the interior of $P$, and consider $\breve{X}_{P} \subset X_{P}$ defined by $\breve{X}_{P}=\mu_{P}^{-1}(\breve{P})$. One can easily check that $\breve{X}_{P}$ is a smooth open dense subset of $X_{P}$, consisting of all the points where the $\mathbb{T}^{2}$-action is free. It can be described as
$$\breve{X}_{P} \cong \breve{P} \times \mathbb{T}^{2}=\left\{(x, \theta): x=\left(x_{1}, x_{2}\right) \in \breve{P} \subset \mathbb{R}^{2}, \theta=\left(\theta_{1}, \theta_{2}\right) \in \mathbb{R}^{2} / 2 \pi \mathbb{Z}^{2}\right\},$$
where $(x, \theta)$ are symplectic action-angle coordinates for $\omega_{P}$, i.e.
$$\omega_{P}=d x_{1} \wedge d \theta_{1}+d x_{2} \wedge d \theta_{2} .$$

If $J$ is any complete $\omega_{P}$-compatible toric complex structure on $X_{P}$, the symplectic $(x, \theta)$-coordinates on $\breve{X}_{P}$ can be chosen so that the matrix that represents $J$ in these coordinates has the form
$$\left[\begin{array}{ccc}
0 & \vdots & -U^{-1} \\
\ldots \ldots & \cdots & \cdots \\
U & \vdots & 0
\end{array}\right]$$
where $U=U(x)=\left[u_{j k}(x)\right]_{j, k=1}^{2,2}$, is a symmetric and positive-definite real matrix. The integrability condition for the complex structure $J$ is equivalent to $U$ being the Hessian of a smooth function $\mathbf{u} \in C^{\infty}(\breve{P})$, i.e.
$$U=\operatorname{Hess}_{x}(\mathbf{u}), u_{j k}(x)=\frac{\partial^{2} \mathbf{u}}{\partial x_{j} \partial x_{k}}(x), 1 \leq j, k \leq 2 .$$
Holomorphic coordinates for $J$ are given in this case by
$$z(x, \theta)=\xi(x)+i \theta=\frac{\partial \mathbf{u}}{\partial x}(x)+i \theta$$
We will call $\mathbf{u}$ the symplectic potential of the compatible toric complex structure $J$. Note that the metric $g(\cdot, \cdot)=\omega_{P}(\cdot, J \cdot)$ is given in these $(x, \theta)$-coordinates by the matrix
$$\left[\begin{array}{ccc}
\operatorname{Hess}(\mathbf{u}) & \vdots & 0 \\
\ldots \ldots \ldots \ldots & \ldots \ldots \ldots \\
0 & \vdots & \operatorname{Hess}^{-1}(\mathbf{u})
\end{array}\right]$$

We will now characterize the symplectic potentials that correspond to complete toric compatible complex structures on a symplectic toric 4-manifold $\left(M_{P}, \omega_{P}, \tau_{P}\right)$. Every moment polygon $P \subset \mathbb{R}^{2}$ can be described by a set of inequalities of the form
$$\ell_{i}(x) \equiv\left\langle x, \nu_{i}\right\rangle+\lambda_{i} \geq 0, i=1, \ldots, d,$$
where $d$ is the number of edges of $P$, each $\nu_{i}$ is a primitive element of the lattice $\mathbb{Z}^{2} \subset \mathbb{R}^{2}$ (the inward-pointing normal to the $i$-th edge of P ), and each $\lambda_{r}$ is a real number. Then $x \in P$ belongs to the $i$-th edge iff $\ell_{i}(x)=0$, and $x \in \breve{P}$ iff $\ell_{i}(x)>0$ for all $i=1, \ldots, d$.

The following theorem follows from a result of Guillemin [G].
Theorem 2.13. Let $\left(X_{P}, \omega_{P}, \tau_{P}\right)$ be the symplectic toric 4-manifold associated to a moment polygon $P \subset \mathbb{R}^{2}$. Then the canonical compatible toric complex structure $J_{P}$ is complete and, in suitable action-angle $(x, \theta)$-coordinates on $\breve{X}_{P} \cong \breve{P} \times \mathbb{T}^{2}$, its symplectic potential $\mathbf{u}_{P} \in C^{\infty}(\breve{P})$ is given by
$$\mathbf{u}_{P}(x)=\frac{1}{2} \sum_{i=1}^{d} \ell_{i}(x) \log \ell_{i}(x) .$$

The next theorem provides the symplectic version of the $\partial \bar{\partial}$-lemma in this toric context and is an immediate extension to our complete non-compact setting of the compact version proved in [A2] (see [A3] for the compact orbifold version).

Theorem 2.14. Let $J$ be any complete compatible toric complex structure on the symplectic toric 4-manifold $\left(X_{P}, \omega_{P}, \tau_{P}\right)$. Then, in suitable action-angle $(x, \theta)$ -coordinates on $\breve{X}_{P} \cong \breve{P} \times \mathbb{T}^{2}, J$ is given by a symplectic potential $\mathbf{u} \in C^{\infty}(\breve{P})$ of the form
$$\mathbf{u}(x)=\mathbf{u}_{P}(x)+h(x),$$
where $\mathbf{u}_{P}$ is given by Theorem 2.13, $h$ is smooth on the whole $P$, and the matrix $\operatorname{Hess}(\mathbf{u})$ is positive definite on $P$ and has determinant of the form
$$\operatorname{det}(\operatorname{Hess}(\mathbf{u}))=\left(\delta \prod_{i=1}^{d} \ell_{r}\right)^{-1},$$
with $\delta$ being a smooth and strictly positive function on the whole $P$.
Conversely, any such potential $\mathbf{u}$ determines a (not necessarily complete) complex structure on $\breve{X}_{P} \cong \breve{P} \times \mathbb{T}^{2}$, that extends uniquely to a well-defined compatible toric complex structure $J$ on the symplectic toric 4-manifold $\left(X_{P}, \omega_{P}, \tau_{P}\right)$.

Remark 2.15. As we will see, the metrics we refer to in Theorem 1.1 correspond to complete compatible toric complex structures.
2.4. Scalar curvature. We now recall from A1 a particular formula for the scalar curvature in action-angle $(x, \theta)$-coordinates. A Kähler metric of the form (2) has scalar curvature $s$ given by
$$s=-\sum_{j, k} \frac{\partial}{\partial x_{j}}\left(u^{j k} \frac{\partial \log \operatorname{det}(\operatorname{Hess}(\mathbf{u}))}{\partial x_{k}}\right),$$
which after some algebraic manipulations becomes the more compact
$$s=-\sum_{j, k} \frac{\partial^{2} u^{j k}}{\partial x_{j} \partial x_{k}},$$
where the $u^{j k}, 1 \leq j, k \leq 2$, are the entries of the inverse of the matrix $\operatorname{Hess}_{x}(\mathbf{u})$, $\mathbf{u} \equiv$ symplectic potential.

\section*{3. Joyce's construction in action-angle coordinates}

In [J], Joyce constructs local scalar-flat Kähler metrics with torus symmetry on $\mathbb{R}^{4}$. In this section we recall Donaldson's action-angle coordinates version of Joyce's construction and discuss some solutions of a relevant PDE which is used in it.

The main ingredient is a pair of linearly independent solutions of the PDE
$$\frac{\partial^{2} \xi}{\partial H^{2}}+\frac{\partial^{2} \xi}{\partial r^{2}}+\frac{1}{r} \frac{\partial \xi}{\partial r}=0$$
on $\mathbb{H}=\left\{(H, r) \in \mathbb{R}^{2}: r>0\right\}$. The main theorem is the following.
Theorem 3.1 (Donaldson, [D1]). Let $\xi_{1}$ and $\xi_{2}$ be two solutions of equation (4). Let
$$\epsilon_{1}=r\left(\frac{\partial \xi_{2}}{\partial r} d H-\frac{\partial \xi_{2}}{\partial H} d r\right)$$
and
$$\epsilon_{2}=-r\left(\frac{\partial \xi_{1}}{\partial r} d H-\frac{\partial \xi_{1}}{\partial H} d r\right) .$$
Then these two 1-forms are closed. Let $x_{1}$ and $x_{2}$ denote their primitives, well defined up to a constant. Then $\left(x_{1}, x_{2}\right)$ are local coordinates in $\mathbb{R}^{2}$. Let
$$\epsilon=\xi_{1} d x_{1}+\xi_{2} d x_{2} .$$
This 1-form is also closed. Let u be a primitive of $\epsilon$ and write $\xi=\left(\xi_{1}, \xi_{2}\right)$. Then, if $\operatorname{det} D \xi>0$, where
$$D \xi=\left(\begin{array}{ll}
\xi_{1, H} & \xi_{1, r} \\
\xi_{2, H} & \xi_{2, r}
\end{array}\right),$$
the function $\mathbf{u}$ is a local symplectic potential for some toric Kähler metric on $\mathbb{R}^{4}$ whose scalar curvature is 0.

There are some obvious solutions to equation (4):
\begin{itemize}
\item[-] Any affine function of $H$, namely $\xi=a H+b$ with $a, b \in \mathbb{R}$ constants. These are the only $r$-independent solutions.
\item[-] The only $H$-independent solutions are $\xi=a \log (r)+b$ with $a, b \in \mathbb{R}$ constants.
\item[-] Another important solution is
$$\xi=\frac{1}{2} \log \left(H+a+\sqrt{(H+a)^{2}+r^{2}}\right)$$
for any given constant $a \in \mathbb{R}$. This solution satisfies the following important property
\end{itemize}

Proposition 3.2. As $r$ tends to zero the above solution is asymptotic to
$$\begin{cases}\log (r)+O(1), & \text { if } H<-a \\ O(1) & \text { if } H>-a\end{cases}$$
Proof. When $r$ is close to 0,
$$H+a+\sqrt{(H+a)^{2}+r^{2}} \quad \text { is close to } \quad H+a+|H+a|,$$
so that
$$\log \left(H+a+\sqrt{(H+a)^{2}+r^{2}}\right) \quad \text { is } O(1) \text { when } H+a>0 \text {. }$$
By dividing and multiplying the argument of the log by
$$-(H+a)+\sqrt{(H+a)^{2}+r^{2}}$$
the function $\xi$ can be written as
$$\log (r)-\frac{1}{2} \log \left(-(H+a)+\sqrt{(H+a)^{2}+r^{2}}\right) .$$
When $r$ is small
$$-(H+a)+\sqrt{(H+a)^{2}+r^{2}} \quad \text { is close to } \quad-(H+a)+|H+a|$$
so that
$$\log \left(-(H+a)+\sqrt{(H+a)^{2}+r^{2}}\right) \quad \text { is } O(1) \text { when } H+a<0 .$$ \(\square\)
\begin{itemize}
\item[-] An analogous solution to the above is
$$\xi=\frac{1}{2} \log \left(-(H+a)+\sqrt{(H+a)^{2}+r^{2}}\right),$$
whose behavior near $r=0$ is given by
$$\begin{cases}O(1), & \text { if } H<-a \\ \log (r)+O(1) & \text { if } H>-a\end{cases}$$
\end{itemize}

\section*{4. The construction of the metrics}

Let $X$ be a symplectic toric 4-manifold whose moment polygon $P$ is unbounded. The purpose of this section is to use Donaldson's action-angle coordinates version of Joyce's construction to give a method for obtaining explicit symplectic potentials for scalar-flat toric Kähler metrics on $X$. More precisely, we will prove the following theorem.

Theorem 4.1. Let $X$ be an unbounded symplectic toric 4-manifold and $P$ its moment polygon. Let $d$ be the number of edges of $P$. Let $\nu_{i}=\left(\alpha_{i}, \beta_{i}\right) \in \mathbb{Z}^{2}$, $i=1, \cdots, d$, be the primitive interior normals to the edges of $P$, ordered according to Remark 2.5. Let $\nu=(\alpha, \beta)$ be a vector in $\mathbb{R}^{2}$ such that
$$\operatorname{det}\left(\nu, \nu_{1}\right), \operatorname{det}\left(\nu, \nu_{d}\right) \geq 0 .$$
Set
$$\xi_{1}=\alpha_{1} \log (r)+\frac{1}{2} \sum_{i=1}^{d-1}\left(\alpha_{i+1}-\alpha_{i}\right) \log \left(H+a_{i}+\sqrt{\left(H+a_{i}\right)^{2}+r^{2}}\right)+\alpha H$$
and
$$\xi_{2}=\beta_{1} \log (r)+\frac{1}{2} \sum_{i=1}^{d-1}\left(\beta_{i+1}-\beta_{i}\right) \log \left(H+a_{i}+\sqrt{\left(H+a_{i}\right)^{2}+r^{2}}\right)+\beta H$$
where $a_{1}<\cdots<a_{d-1}$ are real numbers determined by the moment polygon $P$. Let
$$\epsilon_{1}=r\left(\frac{\partial \xi_{2}}{\partial r} d H-\frac{\partial \xi_{2}}{\partial H} d r\right) \quad \text { and } \quad \epsilon_{2}=-r\left(\frac{\partial \xi_{1}}{\partial r} d H-\frac{\partial \xi_{1}}{\partial H} d r\right) .$$
Then these two 1-forms are closed and their primitives $x_{1}$ and $x_{2}$ define symplectic action coordinates on $\breve{P}$ for some scalar-flat toric Kähler metric on $X$, whose symplectic potential $\mathbf{u}$ satisfies
$$d \mathbf{u}=\xi_{1} d x_{1}+\xi_{2} d x_{2} .$$

Remark 4.2. Note that the set of vectors $\nu \in \mathbb{R}^{2}$ satisfying condition (5), forms a cone with edge vectors $-\nu_{1}$ and $\nu_{d}$. This cone has non-empty interior as long as the moment polygon $P$ is strictly unbounded.

Remark 4.3. Note that the moment map and the coordinates $x=\left(x_{1}, x_{2}\right)$ are only defined up to constants. What the theorem says is that these constants can be arranged so that $x_{1}$ and $x_{2}$ do define global symplectic action coordinates on $P$. We will assume in the proof that the "first" vertex of $P$ is the origin in $\mathbb{R}^{2}$.

Proof. In view of Theorems 2.14 and 3.1, together with the fact that
$$\log \left(H+a+\sqrt{(H+a)^{2}+r^{2}}\right)$$
is a solution of equation (4) for any $a \in \mathbb{R}$, there are three missing ingredients:
\begin{itemize}
\item[-] We need to show that, under the above assumptions, $\operatorname{det} D \xi>0$.
\item[-] We need to show that $x=\left(x_{1}, x_{2}\right)$ define global symplectic action coordinates on $P$.
\item[-] We need to show that the boundary behavior of $\mathbf{u}(x)$ on $\partial P$ is the one required by Theorem 2.14
\end{itemize}

We start by showing that $\operatorname{det} D \xi>0$. When $\nu=0$ this is a result of Joyce ([J], Lemma 3.3.2, see also [CS]). In this case, a direct calculation shows that
$$D \xi=\left(\begin{array}{ll}
\sum_{i=1}^{d-1} \frac{\left(\alpha_{i+1}-\alpha_{i}\right)}{2 \rho_{i}} & \frac{\alpha_{1}}{r}+\sum_{i=1}^{d-1} \frac{\left(\alpha_{i+1}-\alpha_{i}\right) r}{2\left(H_{i}+\rho_{i}\right) \rho_{i}} \\
\sum_{i=1}^{d-1} \frac{\left(\beta_{i+1}-\beta_{i}\right)}{2 \rho_{i}} & \frac{\beta_{1}}{r}+\sum_{i=1}^{d-1} \frac{\left(\beta_{i+1}-\beta_{i}\right) r}{2\left(H_{i}+\rho_{i}\right) \rho_{i}}
\end{array}\right),$$
where we have used the notation
$$H_{i}=H+a_{i} \quad \text { and } \quad \rho_{i}=\sqrt{H_{i}^{2}+r^{2}} .$$

When $\nu \neq 0$ we start by noticing that, because of convexity of the moment polygon, the condition
$$\operatorname{det}\left(\nu, \nu_{1}\right), \operatorname{det}\left(\nu, \nu_{d}\right) \geq 0$$
actually implies
$$\operatorname{det}\left(\nu, \nu_{i}\right) \geq 0, \quad \forall i=1, \cdots, d .$$
In this case $D \xi$ is obtained by adding
$$\left(\begin{array}{ll}
\alpha & 0 \\
\beta & 0
\end{array}\right)$$
to (6), which in turn changes $\operatorname{det} D \xi$ by adding the following quantity:
$$\begin{array}{r}
\operatorname{det}\left(\nu, \nu_{1}\right)\left(\frac{1}{r}-\frac{r}{2 \rho_{1}\left(H_{1}+\rho_{1}\right)}\right)+ \\
\frac{r}{2} \sum_{i=1}^{d-1} \operatorname{det}\left(\nu, \nu_{i}\right)\left(\frac{1}{\rho_{i-1}\left(H_{i-1}+\rho_{i-1}\right)}-\frac{1}{\rho_{i}\left(H_{i}+\rho_{i}\right)}\right)+ \\
\frac{r}{2} \operatorname{det}\left(\nu, \nu_{d}\right) \frac{1}{\rho_{d}\left(H_{d}+\rho_{d}\right)}
\end{array}$$
One can easily check that
$$\frac{1}{r}-\frac{r}{2 \rho_{1}\left(H_{1}+\rho_{1}\right)}>0 \quad \text { and } \quad \frac{1}{\rho_{d}\left(H_{d}+\rho_{d}\right)}>0 .$$
We have that
$$\frac{1}{\rho_{i-1}\left(H_{i-1}+\rho_{i-1}\right)}-\frac{1}{\rho_{i}\left(H_{i}+\rho_{i}\right)}=\frac{\rho_{i}\left(H_{i}+\rho_{i}\right)-\rho_{i-1}\left(H_{i-1}+\rho_{i-1}\right)}{\rho_{i} \rho_{i-1}\left(H_{i-1}+\rho_{i-1}\right)\left(H_{i}+\rho_{i}\right)} .$$
Since the denominator of the right hand side is clearly positive, we just need to show that its numerator is positive. A simple calculation shows that this numerator can be written as
$$\left(H_{i-1}+a\right)\left(H_{i-1}+a+\sqrt{\left(H_{i-1}+a\right)^{2}+r^{2}}\right)-H_{i-1}\left(H_{i-1}+\sqrt{H_{i-1}^{2}+r^{2}}\right),$$
where $a=a_{i}-a_{i-1}>0$. To show that this is positive, fix $H_{i-1}, r \in \mathbb{R}$ and consider the function $f: \mathbb{R} \rightarrow \mathbb{R}$ defined by
$$f(a)=\left(H_{i-1}+a\right)\left(H_{i-1}+a+\sqrt{\left(H_{i-1}+a\right)^{2}+r^{2}}\right)-H_{i-1}\left(H_{i-1}+\sqrt{H_{i-1}^{2}+r^{2}}\right) .$$
Then $f(0)=0$ and
$$f^{\prime}(a)=\frac{\left(H_{i-1}+a+\sqrt{\left(H_{i-1}+a\right)^{2}+r^{2}}\right)^{2}}{\sqrt{\left(H_{i-1}+a\right)^{2}+r^{2}}}>0 \Rightarrow f(a)>0, \forall a>0 .$$
Hence, we conclude that all the terms in (7) are positive, which finishes the proof that $\operatorname{det} D \xi>0$.

We will now prove that $x=\left(x_{1}, x_{2}\right)$ define global symplectic action coordinates on $P$. Some easy calculations show that if
$$\xi=\frac{1}{2} \log \left(H+a+\sqrt{(H+a)^{2}+r^{2}}\right)$$
then
$$\epsilon=r\left(\frac{\partial \xi}{\partial r} d H-\frac{\partial \xi}{\partial H} d r\right)=\frac{1}{2} d\left(H+a-\sqrt{(H+a)^{2}+r^{2}}\right) .$$
Hence, when $\nu=0$ we have that
$$x_{1}=\beta_{1} H+\frac{1}{2} \sum_{i=1}^{d-1}\left(\beta_{i+1}-\beta_{i}\right)\left(H+a_{i}-\sqrt{\left(H+a_{i}\right)^{2}+r^{2}}\right)$$
and
$$x_{2}=-\alpha_{1} H-\frac{1}{2} \sum_{i=1}^{d-1}\left(\alpha_{i+1}-\alpha_{i}\right)\left(H+a_{i}-\sqrt{\left(H+a_{i}\right)^{2}+r^{2}}\right) .$$
Note that $x=\left(x_{1}, x_{2}\right)$ extends continuously to $r=0$. To show that these define global symplectic action coordinates on $P$ we need to determine the $a_{i}$ 's so that $\left(x_{1}(H, 0), x_{2}(H, 0)\right) \in \partial P$. When $r=0$ we have
$$x_{1}=\beta_{1} H+\frac{1}{2} \sum_{i=1}^{d-1}\left(\beta_{i+1}-\beta_{i}\right)\left(H+a_{i}-\left|H+a_{i}\right|\right)$$
and
$$x_{2}=-\alpha_{1} H-\frac{1}{2} \sum_{i=1}^{d-1}\left(\alpha_{i+1}-\alpha_{i}\right)\left(H+a_{i}-\left|H+a_{i}\right|\right),$$
which means that:
\begin{itemize}
\item[(i)] if $-a_{1}<H$ then
$$x_{1}=\beta_{1} H \quad \text { and } \quad x_{2}=-\alpha_{1} H .$$
\item[(ii)] if $-a_{j+1}<H<-a_{j}$ then
$$x_{1}=\beta_{j+1} H+\sum_{i=1}^{j} a_{i}\left(\beta_{i+1}-\beta_{i}\right) \quad \text { and } \quad x_{2}=-\alpha_{j+1} H-\sum_{i=1}^{j} a_{i}\left(\alpha_{i+1}-\alpha_{i}\right) .$$
\item[(iii)] if $H<-a_{d-1}$ then
$$x_{1}=\beta_{d} H+\sum_{i=1}^{d-1} a_{i}\left(\beta_{i+1}-\beta_{i}\right) \quad \text { and } \quad x_{2}=-\alpha_{d} H-\sum_{i=1}^{d-1} a_{i}\left(\alpha_{i+1}-\alpha_{i}\right) .$$
Hence, we have that:
\item[(i)] if $-a_{1}<H$ then
$$x \cdot \nu_{1}=0 .$$
\item[(ii)] if $-a_{j+1}<H<-a_{j}$ then
$$x \cdot \nu_{j+1}=-\sum_{i=1}^{j} a_{i} \operatorname{det}\left(\nu_{i+1}-\nu_{i}, \nu_{j}\right) .$$
\end{itemize}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/162ce568-c28b-4fe6-8a3b-77dc65ba6e91-14.jpg?height=453&width=967&top_left_y=397&top_left_x=580}
\captionsetup{labelformat=empty}
\caption{Figure 1. The map $x:(\overline{\mathbb{H}}, \partial \mathbb{H}) \longrightarrow(P, \partial P)$.}
\end{figure}
\begin{itemize}
\item[(iii)] if $H<-a_{d-1}$ then
$$x \cdot \nu_{d}=-\sum_{i=1}^{d-1} a_{i} \operatorname{det}\left(\nu_{i+1}-\nu_{i}, \nu_{d-1}\right)$$
Note that each of the above expressions is a constant independent of $H$.
\end{itemize}

Let $P$ be given by
$$P=\left\{x \in \mathbb{R}^{2}: \ell_{j}(x) \equiv\left\langle x, \nu_{j}\right\rangle+\lambda_{j} \geq 0, j=1, \ldots, d\right\} .$$
We may assume that $\lambda_{1}=\lambda_{2}=0$, which is equivalent to the "first" vertex of $P$ being the origin in $\mathbb{R}^{2}$. We then have that:
\begin{itemize}
\item[(i)] if $-a_{1}<H$ then
$$\ell_{1}(x)=0 \Leftrightarrow x \cdot \nu_{1}=0 .$$
\item[(ii)] if $-a_{j+1}<H<-a_{j}$ then
$$\ell_{j+1}(x)=0 \Leftrightarrow \sum_{i=1}^{j} a_{i} \operatorname{det}\left(\nu_{i+1}-\nu_{i}, \nu_{j}\right)=\lambda_{j+1} .$$
\item[(iii)] if $H<-a_{d-1}$ then
$$\ell_{d}(x)=0 \Leftrightarrow \sum_{i=1}^{d-1} a_{i} \operatorname{det}\left(\nu_{i+1}-\nu_{i}, \nu_{d-1}\right)=\lambda_{d} .$$
Using the fact that
$$\operatorname{det}\left(\nu_{j+1}, \nu_{j}\right)=1,$$
one easily checks that the linear system of equations in (ii) and (iii) above determine the $a_{j}$ 's uniquely. With this choice of $a_{j}$ 's, it follows from the above expression for $x(H, 0)$ that $x: \partial \mathbb{H} \rightarrow \partial P$ is a proper homeomorphism.
\end{itemize}

Hence, we may conclude that
$$x:(\overline{\mathbb{H}}, \partial \mathbb{H}) \longrightarrow(P, \partial P)$$
is a proper homeomorphism, whose restriction to $\mathbb{H}$ is a smooth proper diffeomorphism onto $\breve{P}$ (see Figure 1). This proves that $x=\left(x_{1}, x_{2}\right)$ can be used as symplectic action coordinates on $\breve{P}$.

We will now study the boundary behavior of the symplectic potential $\mathbf{u}: \breve{P} \rightarrow \mathbb{R}$, defined up to a constant by
$$d \mathbf{u}=\xi_{1} d x_{1}+\xi_{2} d x_{2}$$
We start by showing that
$$\operatorname{det}\left(\operatorname{Hess}_{x}(\mathbf{u})\right)=\left(\delta \prod_{i=1}^{d} l_{i}\right)^{-1},$$
with $\delta$ being a smooth and strictly positive function on the whole P. We know from [D1] that $r=\left(\operatorname{det} \operatorname{Hess}_{x}(\mathbf{u})\right)^{-1 / 2}$, so we need to show that
$$r=\left(\delta \prod_{i=1}^{d} \ell_{i}\right)^{1 / 2},$$
which is equivalent to
$$\prod_{i=1}^{d} \ell_{i}=\frac{r^{2}}{\delta} .$$
Hence, it suffices to prove that as we approach the edge $E_{j}$ of $P$ we have
$$\frac{\partial \ell_{j}}{\partial r} \sim r \gamma_{j},$$
with $\gamma_{j}$ being a smooth and strictly positive function. Since
$$\frac{\partial x_{1}}{\partial r}=-\frac{r}{2} \sum_{i=1}^{d-1} \frac{\beta_{i+1}-\beta_{i}}{\rho_{i}} \quad \text { and } \quad \frac{\partial x_{2}}{\partial r}=\frac{r}{2} \sum_{i=1}^{d-1} \frac{\alpha_{i+1}-\alpha_{i}}{\rho_{i}},$$
we have that
$$\begin{aligned}
\frac{\partial \ell_{j}}{\partial r} & =\frac{\partial x_{1}}{\partial r} \alpha_{j}+\frac{\partial x_{2}}{\partial r} \beta_{j} \\
& =-\frac{r}{2} \sum_{i=1}^{d-1} \frac{\left(\beta_{i+1}-\beta_{i}\right) \alpha_{j}-\left(\alpha_{i+1}-\alpha_{i}\right) \beta_{j}}{\rho_{i}} \\
& =\frac{r}{2} \sum_{i=1}^{d-1} \frac{\operatorname{det}\left(\nu_{i+1}-\nu_{i}, \nu_{j}\right)}{\rho_{i}} \\
& =\frac{r}{2}\left(-\frac{\operatorname{det}\left(\nu_{1}, \nu_{j}\right)}{\rho_{1}}+\sum_{i=2}^{d-1} \operatorname{det}\left(\nu_{i}, \nu_{j}\right)\left(\frac{1}{\rho_{i-1}}-\frac{1}{\rho_{i}}\right)+\frac{\operatorname{det}\left(\nu_{d}, \nu_{j}\right)}{\rho_{d-1}}\right) .
\end{aligned}$$
Hence, we need to show that
$$\gamma_{j}:=\frac{1}{2}\left(-\frac{\operatorname{det}\left(\nu_{1}, \nu_{j}\right)}{\rho_{1}}+\sum_{i=2}^{d-1} \operatorname{det}\left(\nu_{i}, \nu_{j}\right)\left(\frac{1}{\rho_{i-1}}-\frac{1}{\rho_{i}}\right)+\frac{\operatorname{det}\left(\nu_{d}, \nu_{j}\right)}{\rho_{d-1}}\right)$$
is strictly positive when $r=0$ and $H$ varies in the interval corresponding to the edge $E_{j}$. Since $\rho_{i}=\left|H+a_{i}\right|$ when $r=0$, we have that:
\begin{itemize}
\item[(i)] if $-a_{1}<H$, i.e. $j=1$, then
$$\gamma_{j}(H, 0)=\sum_{i=2}^{d-1} \operatorname{det}\left(\nu_{i}, \nu_{1}\right)\left(\frac{1}{H+a_{i-1}}-\frac{1}{H+a_{i}}\right)+\frac{\operatorname{det}\left(\nu_{d}, \nu_{1}\right)}{H+a_{d-1}} .$$
\end{itemize}

All the terms on the right hand side are strictly positive, since
$$0<H+a_{i-1}<H+a_{i}, \forall 1<i<d, \quad \text { and } \quad \operatorname{det}\left(\nu_{i}, \nu_{1}\right)>0, \forall 1<i \leq d .$$
\begin{itemize}
\item[(ii)] if $-a_{j}<H<-a_{j-1}$, i.e. $1<j<d$, then $\operatorname{det}\left(\nu_{1}, \nu_{j}\right)<0, \operatorname{det}\left(\nu_{d}, \nu_{j}\right)>0$ and
$$\operatorname{det}\left(\nu_{i}, \nu_{j}\right)<0, \frac{1}{\rho_{i-1}}-\frac{1}{\rho_{i}}<0, \text { for every } 1<i<j,$$
while
$$\operatorname{det}\left(\nu_{i}, \nu_{j}\right)>0, \frac{1}{\rho_{i-1}}-\frac{1}{\rho_{i}}>0, \text { for every } j<i<d-1 .$$
Hence, $\gamma_{j}(H, 0)>0$.
\item[(iii)] if $H<-a_{d}$, i.e. $j=d$, then
$$\gamma_{j}(H, 0)=\frac{\operatorname{det}\left(\nu_{1}, \nu_{d}\right)}{H+a_{1}}+\sum_{i=2}^{d-1} \operatorname{det}\left(\nu_{i}, \nu_{d}\right)\left(\frac{1}{H+a_{i}}-\frac{1}{H+a_{i-1}}\right) .$$
Again, all the terms on the right hand side are strictly positive, since
$$H+a_{i-1}<H+a_{i}<0, \forall 1<i<d, \quad \text { and } \quad \operatorname{det}\left(\nu_{i}, \nu_{d}\right)<0, \forall 1 \leq<i<d .$$
This finishes the proof of (8).
\end{itemize}

Now, using Proposition 3.2, we write down the asymptotic expression for $d \mathbf{u}$ when $r$ tends to 0 . When $-a_{j}<H<-a_{j-1}, j=2, \ldots, d-1$, we have
$$\xi_{1}=\alpha_{1} \log (r)+\sum_{i=1}^{j-1}\left(\alpha_{i+1}-\alpha_{i}\right) \log (r)+O(1)$$
and
$$\xi_{2}=\beta_{1} \log (r)+\sum_{i=1}^{j-1}\left(\beta_{i+1}-\beta_{i}\right) \log (r)+O(1) .$$
Therefore
$$\xi_{1}=\alpha_{j} \log (r)+O(1),$$
and
$$\xi_{2}=\beta_{j} \log (r)+O(1) .$$
One easily checks that these formulas also hold when $j=1$ and $j=d$. Hence, this implies that
$$d \mathbf{u}=\log (r)\left(\alpha_{j+1} d x_{1}+\beta_{j+1} d x_{2}\right)+O(1)$$
which, taking into account the fact that $r=\left(\delta \prod_{\ell}\right)^{1 / 2}$, is the same as saying that close to the interior of the edge $E_{j+1}$ of $P$,
$$d \mathbf{u}=\frac{1}{2} \log \left(\ell_{j+1}\right)\left(\alpha_{j+1} d x_{1}+\beta_{j+1} d x_{2}\right)+O(1)$$
close to the interior of the edge $E_{j+1}$ of $P$. This is the boundary behavior required by Theorem 2.14.

It remains to check what happens near a vertex of $P$. We may consider, without any loss of generality, the vertex corresponding to $\left(-a_{1}, 0\right) \in \overline{\mathbb{H}}$ and assume that $a_{1}=0$. Hence we have $0<a_{2}<\cdots<a_{d-1}$. As $r$ and $H$ tend to zero, we have
$$H+a_{i}+\sqrt{\left(H+a_{i}\right)^{2}+r^{2}} \rightarrow 2 a_{i}$$
and
$$H+a_{i}-\sqrt{\left(H+a_{i}\right)^{2}+r^{2}} \simeq-\frac{r^{2}}{2 a_{i}}$$
for $i=2, \cdots, d-1$ As a consequence
$$x_{1}=\beta_{1} H+\frac{1}{2}\left(\beta_{2}-\beta_{1}\right)\left(H-\sqrt{H^{2}+r^{2}}\right)+O\left(r^{2}\right)$$
and
$$x_{2}=-\alpha_{1} H-\frac{1}{2}\left(\alpha_{2}-\alpha_{1}\right)\left(H-\sqrt{H^{2}+r^{2}}\right)+O\left(r^{2}\right) .$$
We see that
$$\left(\nu_{2}-\nu_{1}\right) \cdot x=H+O\left(r^{2}\right),$$
since
$$\left(\alpha_{2}-\alpha_{1}\right) \beta_{1}-\left(\beta_{2}-\beta_{1}\right) \alpha_{1}=\operatorname{det}\left(\nu_{2}-\nu_{1}, \nu_{1}\right)=1 .$$
Similarly, we can see that
$$\nu_{1} \cdot x=-\frac{1}{2}\left(H-\sqrt{H^{2}+r^{2}}\right)+O\left(r^{2}\right) .$$
Putting these together we conclude that
$$H+\sqrt{H^{2}+r^{2}}=2 \nu_{2} \cdot x+O\left(r^{2}\right) .$$
Note that, as we have seen before, $r=\left(\delta \prod \ell_{i}\right)^{1 / 2}$. Near the vertex this becomes $r=\delta^{\prime} \ell_{1}^{1 / 2} \ell_{2}^{1 / 2}$. We also have
$$\xi_{1}=\alpha_{1} \log (r)+\frac{1}{2}\left(\alpha_{2}-\alpha_{1}\right) \log \left(H+\sqrt{H^{2}+r^{2}}\right)+O(1)$$
and
$$\xi_{2}=\beta_{1} \log (r)+\frac{1}{2}\left(\beta_{2}-\beta_{1}\right) \log \left(H+\sqrt{H^{2}+r^{2}}\right)+O(1) .$$
Substituting the above expression for $r$, we obtain
$$\xi_{1}=\frac{1}{2} \alpha_{1} \log \left(\ell_{1}\right)+\frac{1}{2} \alpha_{2} \log \left(\ell_{2}\right)+O(1)$$
and
$$\xi_{2}=\frac{1}{2} \beta_{1} \log \left(\ell_{1}\right)+\frac{1}{2} \beta_{2} \log \left(\ell_{2}\right)+O(1) .$$
This implies that
$$d \mathbf{u}=\frac{1}{2}\left(\left(\log \left(\ell_{1}\right) \alpha_{1}+\log \left(\ell_{2}\right) \alpha_{2}\right) d x_{1}+\left(\log \left(\ell_{1}\right) \beta_{1}+\log \left(\ell_{2}\right) \beta_{2}\right) d x_{2}\right)+O(1)$$
which again is the boundary behavior required by Theorem 2.14.
Finally, we note that the boundary $(r=0)$ behavior of $\xi=\left(\xi_{1}, \xi_{2}\right)$ is independent of $\nu$. Hence, the fact that $x=\left(x_{1}, x_{2}\right)$ define global symplectic action coordinates on $P$ and $\mathbf{u}$ has the required boundary behavior when $\nu=0$, remains true when $\nu \neq 0$. \(\square\)

\section*{5. Asymptotic Behavior}

The goal of this section is to study the asymptotic behavior of the metrics and complex structures produced by Theorem 4.1.

Proposition 5.1. Let $X$ be a strictly unbounded smooth symplectic toric 4-manifold and $P$ its moment polygon. Let $d$ be the number of edges of $P$. Let $\nu_{i}=\left(\alpha_{i}, \beta_{i}\right), i=$ $1, \cdots, d$ be the interior primitive normals to the edges of $P$ and let $\nu=(\alpha, \beta) \in \mathbb{R}^{2}$ such that
$$\operatorname{det}\left(\nu, \nu_{1}\right), \operatorname{det}\left(\nu, \nu_{d}\right)>0,$$
when $\nu \neq 0$. Then the metric defined in Theorem 4.1 is ALE when $\nu=0$ and complete and asymptotic to a generalized Taub-NUT metric when $\nu \neq 0$.

Remark 5.2. Note that in the case of $\mathbb{R}^{4}$, which corresponds to $d=2, \nu_{1}=(0,1)$ and $\nu_{2}=(1,0)$, condition (9) is equivalent to $\alpha>0$ and $\beta<0$. This condition coincides with the condition imposed by Donaldson in [D2] for his generalized Taub-NUT metrics. In fact, in this case, multiplying $\nu$ by a constant only changes the metric by an isometry, so that our construction only yields a one parameter family of metrics.

Proof. The fact that, when $\nu=0$, the metrics given by Theorem 4.1 are ALE follows from [J, CS]. Nevertheless we will check their completeness, since this will be useful for the $\nu \neq 0$ case.

What we need to show is that if a curve in $X$ "tends to infinity" then its length also tends to infinity. We will use coordinates $\left(H, r, \theta_{1}, \theta_{2}\right)$ in $X$. These are defined on an open dense subset of $X$ and we may assume that our curve lies in that set. It follows from [D1] that the metrics constructed in Theorem 4.1 split as
$$g=V\left(d r^{2}+d h^{2}\right)+a d \theta_{1}^{2}+b d \theta_{2}^{2}+c d \theta_{1} d \theta_{2},$$
where
$$V=r(\operatorname{det} D \xi)$$
and $a, b$ and $c$ are functions of $H$ and $r$. If follows that
$$l(\gamma) \geq \int \sqrt{V\left((\dot{H})^{2}+(\dot{r})^{2}\right)} .$$
for any curve $\gamma(t)=\left(H(t), r(t), \theta_{1}(t), \theta_{2}(t)\right), t \in[0, T]$, in $X$.
We will first analyze the case $\nu=0$ and $H(t) \geq 0$ for large $t$. As we have seen, $D \xi$ is then given by
$$\left(\begin{array}{ll}
\sum_{i=1}^{d-1} \frac{\left(\alpha_{i+1}-\alpha_{i}\right)}{2 \rho_{i}} & \frac{\alpha_{1}}{r}+\sum_{i=1}^{d-1} \frac{\left(\alpha_{i+1}-\alpha_{i}\right) r}{2\left(H_{i}+\rho_{i}\right) \rho_{i}} \\
\sum_{i=1}^{d-1} \frac{\left(\beta_{i+1}-\beta_{i}\right)}{2 \rho_{i}} & \frac{\beta_{1}}{r}+\sum_{i=1}^{d-1} \frac{\left(\beta_{i+1}-\beta_{i}\right) r}{2\left(H_{i}+\rho_{i}\right) \rho_{i}}
\end{array}\right),$$
where we again us the notation $H_{i}=H+a_{i}$ and $\rho_{i}=\sqrt{H_{i}^{2}+r^{2}}$, as in the proof of Theorem 4.1. Since $\gamma(t)$ tends to infinity as $t \rightarrow \infty$, we have that
$$\rho:=\sqrt{H^{2}+r^{2}} \rightarrow \infty \quad \text { as } t \rightarrow \infty .$$
For $H \geq 0$ and $t \rightarrow \infty$ we have that
$$\frac{1}{H_{i}+\rho_{i}}-\frac{1}{H+\rho}=O\left(\frac{1}{\rho^{2}}\right) \quad \text { and } \quad \frac{1}{\rho_{i}}-\frac{1}{\rho}=O\left(\frac{1}{\rho^{2}}\right) .$$

As $t \rightarrow \infty$ the matrix $D \xi$ becomes
$$\left(\begin{array}{ll}
\frac{\left(\alpha_{d}-\alpha_{1}\right)}{2 \rho} & \frac{\alpha_{1}}{r}+\frac{\left(\alpha_{d}-\alpha_{1}\right) r}{2 \rho(H+\rho)} \\
\frac{\left(\beta_{d}-\beta_{1}\right)}{2 \rho} & \frac{\beta_{1}}{r}+\frac{\left(\beta_{d}-\beta_{1}\right) r}{2 \rho(H+\rho)}
\end{array}\right)+O\left(\frac{1}{\rho^{2}}\right)$$
Hence
$$\begin{aligned}
V & =r \frac{\left(\alpha_{d}-\alpha_{1}\right)}{2 \rho}\left(\frac{\beta_{1}}{r}+\frac{\left(\beta_{d}-\beta_{1}\right) r}{2 \rho(H+\rho)}\right)-r \frac{\left(\beta_{d}-\beta_{1}\right)}{2 \rho}\left(\frac{\alpha_{1}}{r}+\frac{\left(\alpha_{d}-\alpha_{1}\right) r}{2 \rho(H+\rho)}\right)+O\left(\frac{1}{\rho^{2}}\right) \\
& =\frac{\beta_{1}\left(\alpha_{d}-\alpha_{1}\right)-\alpha_{1}\left(\beta_{d}-\beta_{1}\right)}{2 \rho}+O\left(\frac{1}{\rho^{2}}\right) \\
& =\frac{\operatorname{det}\left(\nu_{d}, \nu_{1}\right)}{2 \rho}+O\left(\frac{1}{\rho^{2}}\right)=V_{\text {Euclidean }}+O\left(\frac{1}{\rho^{2}}\right)
\end{aligned}$$
Because $P$ is strictly unbounded, we have $\operatorname{det}\left(\nu_{d}, \nu_{1}\right)>0$ which implies that, as $t \rightarrow \infty$,
$$l(\gamma) \geq C \int \sqrt{\frac{(\dot{H})^{2}+(\dot{r})^{2}}{\rho}},$$
for some positive constant $C$. It follows that $l(\gamma) \rightarrow \infty$ as $T \rightarrow \infty$.
Now we analyze the case $\nu \neq 0$ and $H \geq 0$. The matrix $D \xi$ changes by the addition of
$$\left(\begin{array}{ll}
\alpha & 0 \\
\beta & 0
\end{array}\right) .$$
This in turn changes $V$ by adding to (10)
$$\alpha r\left(\frac{\beta_{1}}{r}+\frac{\left(\beta_{d}-\beta_{1}\right) r}{2 \rho(H+\rho)}\right)-\beta r\left(\frac{\alpha_{1}}{r}+\frac{\left(\alpha_{d}-\alpha_{1}\right) r}{2 \rho(H+\rho)}\right)+O\left(\frac{1}{\rho^{2}}\right)$$
Simplifying, we see that $V$ is now given by the expression
$$\begin{aligned}
V & =\operatorname{det}\left(\nu, \nu_{1}\right)\left(1-\frac{r^{2}}{2 \rho(H+\rho)}\right)+\operatorname{det}\left(\nu, \nu_{d}\right) \frac{r^{2}}{2 \rho(H+\rho)}+\frac{\operatorname{det}\left(\nu_{d}, \nu_{1}\right)}{2 \rho}+O\left(\frac{1}{\rho^{2}}\right) \\
& =V_{\text {Taub }-N U T}+O\left(\frac{1}{\rho^{2}}\right)
\end{aligned}$$
This is what we mean by asymptotic to Taub-NUT. Since $H \geq 0$ we have that
$$0 \leq \frac{r^{2}}{2 \rho(H+\rho)} \leq \frac{1}{2} .$$
Therefore, the fact that $\operatorname{det}\left(\nu, \nu_{1}\right)>0$ implies that $V$ is bounded away from zero, hence
$$l(\gamma) \geq C \int \sqrt{(\dot{H})^{2}+(\dot{r})^{2}}$$
for some positive constant $C$. It again follows that $l(\gamma) \rightarrow \infty$ as $T \rightarrow \infty$.
We will now discuss curves in the region where $H \leq 0$. Under the symmetry $(H, r) \mapsto(-H, r),\left(\nu_{1}, \ldots, \nu_{d}\right) \mapsto\left(\nu_{d}, \ldots, \nu_{1}\right),\left(a_{1}, \ldots, a_{d}\right) \mapsto\left(-a_{d}, \ldots,-a_{1}\right)$ and $\nu \mapsto-\nu$, a curve in the region $H \leq 0$ goes to a curve of the exact same length in the region $H \geq 0$, where now the condition $\operatorname{det}\left(\nu, \nu_{d}\right)>0$ implies completeness.

This finishes the proof. \(\square\)

Remark 5.3. Although the proof above does not work in the case where the first and last edge are parallel, there is at least one example of an unbounded moment polygon with unbounded parallel edges that carries a complete scalar-flat toric Kähler metric. This metric is neither ALE nor ALF. More precisely, consider the non-compact moment polygon whose normals are (0, 1), $(1,0)$ and (0, -1). The symplectic potential for the $\nu=0$ scalar-flat toric Kähler metric given by Theorem 4.1 is
$$\mathbf{u}=\frac{1}{2}(x \log x+y \log y+(2 a-y) \log (2 a-y)-\log (x+2 a)) .$$
Consider a curve with $x=t$ and $y$ fixed. The length of such a curve is
$$l=\int \mathbf{u}_{x x}=\int \sqrt{\frac{1}{t}-\frac{1}{t+2 a}} d t$$
which is unbounded. It is not hard to show that this implies completeness of this metric.

This is not surprising, since the toric manifold corresponding to this moment polygon is $S^{2} \times \mathbb{R}^{2}$ and the metric given by this symplectic potential is the round × hyperbolic metric.

We will now determine which of the toric compatible complex structures given by Theorem 4.1 are complete in the sense of Definition 2.10.

Proposition 5.4. Let $X$ be an unbounded symplectic toric 4-manifold and $P$ its moment polygon. The toric compatible complex structure $J$ defined by a symplectic potential $\mathbf{u}$ given by Theorem 4.1 is complete iff $P$ is strictly unbounded.

Proof. It follows from (1) that
$$\left(\xi_{1}, \xi_{2}, \theta_{1}, \theta_{2}\right), \text { where } \xi_{i}=\frac{\partial \mathbf{u}}{\partial x_{i}}$$
are holomorphic coordinates for $J$. Hence,
$$J \frac{\partial}{\partial \theta_{i}}=-\frac{\partial}{\partial \xi_{i}}, i=1,2,$$
which means that $J$ is complete iff the map
$$\begin{aligned}
\xi: \breve{P} \cong \mathbb{H} & \rightarrow \mathbb{R}^{2} \\
(H, r) & \mapsto\left(\xi_{1}(H, r), \xi_{2}(H, r)\right)
\end{aligned}$$
is surjective.
We showed in the proof of Theorem 4.1 that, when $-a_{j}<H<-a_{j-1}, j=$ $1, \ldots, d$, with $a_{0}=+\infty$ and $a_{d}=-\infty$, we have
$$\xi=\log (r) \nu_{j}+O(1) \quad \text { as } \quad r \rightarrow 0 .$$
Similarly, one can show that, for a fixed arbitrary $H \in \mathbb{R}$, we have
$$\xi=\frac{1}{2} \log (r)\left(\nu_{1}+\nu_{d}\right)+O(1) \quad \text { as } \quad r \rightarrow \infty .$$
These asymptotic expressions for $\xi$ easily imply that
$$\xi \text { is surjective iff } \nu_{1}+\nu_{d} \neq 0,$$
which finishes the proof. \(\square\)

Remark 5.5. In the example of Remark 5.3, the toric compatible complex structure determined by $\mathbf{u}$ cannot be complete. In fact, as mentioned in section 2. $S^{2} \times \mathbb{R}^{2}$ equipped with this complex structure is biholomorphic to $\mathbb{C P}^{1} \times D$, where $D \subset \mathbb{C}$ is the disc.

To finish this section we discuss one more asymptotic feature of our generalized Taub-NUT metrics. Namely, we prove the following proposition (cf. Remark 1.3).

Proposition 5.6. Let $X$ be a strictly unbounded smooth symplectic toric 4-manifold and $P$ its moment polygon. Let $d$ be the number of edges of $P$. Let $\nu_{i}=\left(\alpha_{i}, \beta_{i}\right), i=$ $1, \cdots, d$ be the interior primitive normals to the edges of $P$ and let $0 \neq \nu=(\alpha, \beta) \in$ $\mathbb{R}^{2}$ such that
$$\operatorname{det}\left(\nu, \nu_{1}\right), \operatorname{det}\left(\nu, \nu_{d}\right)>0 .$$
Then $(\alpha, \beta) \in \mathbb{R}^{2}$ generates the unique 1-dimensional subspace of the Lie algebra of $\mathbb{T}^{2}$ whose vectors induce vector fields on $X$ with bounded length.

Proof. Given the asymptotic behavior of our metric it is enough to check that the above holds for the generalized Taub-NUT metrics. We will again use coordinates $\left(H, r, \theta_{1}, \theta_{2}\right)$ on an open set of $X$ and consider a vector field
$$v=a \frac{\partial}{\partial \theta_{1}}+b \frac{\partial}{\partial \theta_{2}}$$
We will proceed to calculate the length of $v$ as $H$ is fixed and $r$ tends to infinity. As we have seen in symplectic action-angle coordinates our metric is given by equation (2), i.e.
$$\left[\begin{array}{ccc}
\operatorname{Hess}(\mathbf{u}) & \vdots & 0 \\
\ldots \ldots \ldots \ldots & \ldots \ldots \ldots \\
0 & \vdots & \operatorname{Hess}^{-1}(\mathbf{u})
\end{array}\right]$$
where $\operatorname{Hess}(\mathbf{u})=\operatorname{Hess}_{x}(\mathbf{u})$. The norm of $v$ is
$$v^{t} \operatorname{Hess}^{-1}(\mathbf{u}) v .$$
We proceed to determine $\operatorname{Hess}^{-1}(\mathbf{u})$.
$$\operatorname{Hess}(\mathbf{u})=D_{x} \xi=D \xi \frac{\partial(H, r)}{\partial x} \Longrightarrow \operatorname{Hess}^{-1}(\mathbf{u})=\frac{\partial x}{\partial(H, r)}(D \xi)^{-1} .$$
Hence using
$$d x_{1}=r\left(\frac{\partial \xi_{2}}{\partial r} d H-\frac{\partial \xi_{2}}{\partial H} d r\right) \quad \text { and } \quad d x_{2}=-r\left(\frac{\partial \xi_{1}}{\partial r} d H-\frac{\partial \xi_{1}}{\partial H} d r\right) .$$
we see that
$$\operatorname{Hess}^{-1}(\mathbf{u})=r\left(\begin{array}{cc}
\xi_{2, r} & -\xi_{2, H} \\
-\xi_{1, r} & \xi_{1, H}
\end{array}\right)\left(\begin{array}{ll}
\xi_{1, H} & \xi_{1, r} \\
\xi_{2, H} & \xi_{2, r}
\end{array}\right)^{-1}$$
which yields
$$\operatorname{Hess}^{-1}(\mathbf{u})=\frac{r}{\xi_{1, H} \xi_{2, r}-\xi_{1, r} \xi_{2, H}}\left(\begin{array}{cc}
\left(\xi_{2, r}^{2}+\xi_{2, H}^{2}\right) & -\left(\xi_{1, r} \xi_{2, r}+\xi_{1, H} \xi_{2, H}\right) \\
-\left(\xi_{1, r} \xi_{2, r}+\xi_{1, H} \xi_{2, H}\right) & \left(\xi_{1, r}^{2}+\xi_{1, H}^{2}\right)
\end{array}\right) .$$
For the generalized Taub-NUT metric corresponding to the vector $\nu=(\alpha, \beta)$ the matrix $D \xi$ is
$$\left(\begin{array}{cc}
\frac{1}{\rho}+\alpha & \frac{r}{\rho(H+\rho)} \\
-\frac{1}{\rho}+\beta & \frac{r}{\rho(-H+\rho)}
\end{array}\right),$$
where as before $\rho=\sqrt{H^{2}+r^{2}}$ and condition (11) implies that $\alpha>0$ and $\beta<0$. We have that $\operatorname{Hess}^{-1}(\mathbf{u})$ is given by
$$\frac{\rho r^{2}}{(\beta+\alpha) H+(\alpha-\beta) \rho+2}\left(\begin{array}{cc}
\frac{(1-\beta \rho)^{2}}{\rho^{2}}+\frac{r^{2}}{\rho^{2}(\rho-H)^{2}} & -\alpha \beta+\frac{\alpha-\beta}{\rho} \\
-\alpha \beta+\frac{\alpha-\beta}{\rho} & \frac{(1+\alpha \rho)^{2}}{\rho^{2}}+\frac{r^{2}}{\rho^{2}(\rho-H)^{2}}
\end{array}\right) .$$
When $r$ tends to infinity and $H$ is fixed, the above matrix can be written as
$$\frac{r^{2}}{\alpha-\beta}\left(\begin{array}{cc}
\beta^{2}-\frac{2 \beta}{r} & -\alpha \beta+\frac{\alpha-\beta}{r} \\
-\alpha \beta+\frac{\alpha-\beta}{r} & \alpha^{2}+\frac{2 \alpha}{r}
\end{array}\right)+O(1)$$
The norm of the vector $v$ in our metric is therefore
$$\frac{r^{2}}{\alpha-\beta}\left(a^{2}\left(\beta^{2}-\frac{2 \beta}{r}\right)+b^{2}\left(\alpha^{2}+\frac{2 \alpha}{r}\right)+2 a b\left(-\alpha \beta+\frac{\alpha-\beta}{r}\right)\right)+O(1) .$$
Hence if we consider
$$v=\alpha \frac{\partial}{\partial \theta_{1}}+\beta \frac{\partial}{\partial \theta_{2}},$$
we see that the norm of $v$ is $O(1)$ as $r$ tends to infinity (for fixed $H$ ) and our claim follows. \(\square\)

\section*{6. Ricci-flat toric Kähler metrics}

An unbounded symplectic toric 4-manifold $X$ can only admit a Ricci-flat toric Kähler metric when $c_{1}(X)=0$. In this section we will show that when $c_{1}(X)=0$ the ALE metric constructed in Theorem 4.1 is indeed Ricci-flat. We will also show that, in this case, a one parameter sub-family of generalized Taub-NUT metrics from Theorem 4.1 is also Ricci-flat. The fact that the ALE metric is Ricci-flat is mentioned in [CS] as a consequence of the fact that this metric is hyperkähler. From our viewpoint, this follows quite easily from calculations in action-angle coordinates.

Throughout this section $P$ will denote a strictly unbounded moment polygon with $d$ edges whose interior primitive normals will be denoted by $\nu_{i}=\left(\alpha_{i}, \beta_{i}\right) \in$ $\mathbb{Z}^{2}, i=1, \cdots, d$. Moreover, $\nu=(\alpha, \beta) \in \mathbb{R}^{2}$ will be such that
$$\operatorname{det}\left(\nu, \nu_{1}\right), \operatorname{det}\left(\nu, \nu_{d}\right)>0,$$
when $\nu \neq 0$.
We begin with a well known fact.
Proposition 6.1. Let $(X, \omega)$ be a symplectic toric manifold endowed with a toric Kähler metric $g$ whose symplectic potential is $\mathbf{u}$. Then $\operatorname{Ric}(g)=0$ iff $\log \operatorname{det}(\operatorname{Hess}(\mathbf{u}))$ is an affine function of the complex coordinates.

Proof. This is only a sketch as the above fact is well known.
Action-angle coordinates ( $x, \theta$ ) and complex coordinates ( $\xi, \theta$ ) are related by
$$x=\phi_{\xi} \quad \text { and } \quad \xi=\mathbf{u}_{x},$$
where $\phi=\phi(\xi)$ is the Kähler potential of $\omega$, i.e.
$$\omega=\partial \bar{\partial} \phi .$$
It is easy to see that
$$\operatorname{Ric}(g)=\partial \bar{\partial} \log \operatorname{det}(\operatorname{Hess}(\phi)),$$
because $\operatorname{det}(\operatorname{Hess}(\phi))$ is the Hermitian metric induced by $\omega$ on the canonical bundle of $X$. Since, up to a constant, we have
$$\phi_{\xi} \circ \mathbf{u}_{x}=\mathrm{id} \quad \text { and } \quad \mathbf{u}_{x} \circ \phi_{\xi}=\mathrm{id},$$
then
$$\operatorname{Hess}(\phi)=\operatorname{Hess}(\mathbf{u})^{-1},$$
at the appropriate points. Therefore
$$\operatorname{Ric}(g)=-\partial \bar{\partial} \log \operatorname{det}(\operatorname{Hess}(\mathbf{u})) .$$
Since $\log \operatorname{det}(\operatorname{Hess}(\mathbf{u}))=\log r$ is independent of $\theta$, as a function of the complex coordinates $(\xi, \theta)$, we conclude that
$$\operatorname{Ric}(g)=0 \quad \text { iff } \quad \log r \text { is affine in } \xi .$$ \(\square\)

Next we use our formulas from Theorem 4.1 to prove the following:
Lemma 6.2. The scalar-flat toric Kähler metrics defined in Theorem 4.1 are Ricciflat iff there is a non-zero vector $\eta \in \mathbb{R}^{2}$ such that
$$\eta \cdot \nu_{j}=1, \quad \forall j=1, \cdots, d$$
and
$$\eta \cdot \nu=0 .$$
Proof. We have seen that Ric is zero when $\log \operatorname{det}(\operatorname{Hess}(\mathbf{u}))=\log r$ is an affine function of $\xi$, i.e. if there is a vector $\eta \in \mathbb{R}^{2}$ such that $\eta \cdot \xi=\log (r)+$ constant. But we have
$$\xi_{1}=\alpha_{1} \log (r)+\frac{1}{2} \sum_{i=1}^{d-1}\left(\alpha_{i+1}-\alpha_{i}\right) \log \left(H+a_{i}+\sqrt{\left(H+a_{i}\right)^{2}+r^{2}}\right)+\alpha H,$$
and
$$\xi_{2}=\beta_{1} \log (r)+\frac{1}{2} \sum_{i=1}^{d-1}\left(\beta_{i+1}-\beta_{i}\right) \log \left(H+a_{i}+\sqrt{\left(H+a_{i}\right)^{2}+r^{2}}\right)+\beta H$$
so that
$$\eta \cdot \xi=\eta \cdot \nu_{1} \log (r)+\frac{1}{2} \sum_{i=1}^{d-1}\left(\eta \cdot\left(\nu_{i+1}-\nu_{i}\right)\right) \log \left(H+a_{i}+\sqrt{\left(H+a_{i}\right)^{2}+r^{2}}\right)+\eta \cdot \nu H .$$
We see that $\log (r)$ is an affine function of $\xi$ exactly when
$$\eta \cdot\left(\nu_{j+1}-\nu_{j}\right)=\eta \cdot \nu=0, \quad \forall j=1, \cdots d$$
and the result follows. \(\square\)

To finish, we need the following:
Lemma 6.3. Let $X$ be an unbounded smooth symplectic toric 4-manifold. Then if the first Chern class of $X$ is zero there is a non-zero vector $\eta=(-\beta, \alpha) \in \mathbb{R}^{2}$ such that
$$\eta \cdot \nu_{j}=1 \quad \forall j=1, \cdots, d$$
and $\nu=(\alpha, \beta)$ satisfies
$$\operatorname{det}\left(\nu, \nu_{1}\right), \operatorname{det}\left(\nu, \nu_{d}\right)>0 .$$

Proof. Let $D_{j}$ be the pre-image under the moment map of the $j$-th edge of the moment polygon of $X$. For $j=2, \cdots, d-1, D_{j}$ is a 2-sphere. First note that if $c_{1}=0$ then
$$D_{j} \cdot D_{j}=-2,$$
where the above refers to the self-intersection number of $D_{j}$. This follows from the adjunction formula. It is also easy to check that
$$D_{j} \cdot D_{j}=\operatorname{det}\left(\nu_{j-1}, \nu_{j+1}\right), \forall j=2, \cdots, d-1 .$$
Hence
$$c_{1}=0 \Longrightarrow \operatorname{det}\left(\nu_{j-1}, \nu_{j+1}\right)=-2 .$$
Now, given $\nu_{j-1}$ and $\nu_{j}$, the normal $\nu_{j+1}$ is completely determined by the relations
$$\operatorname{det}\left(\nu_{j-1}, \nu_{j+1}\right)=-2 \quad \text { and } \quad \operatorname{det}\left(\nu_{j}, \nu_{j+1}\right)=-1 .$$
One can easily see this by reducing to the case where $\nu_{j-1}=(0,1)$ and $\nu_{j}=(1,0)$. The above relations then imply that $\nu_{j+1}=(2,-1)$. Applying this argument inductively we see that the moment polygon of $X$ is completely determined by its first two normal vectors and its total number $d$ of edges. More precisely, if $c_{1}(X)=0$ then the moment polygon of $X$ is $S L(2, \mathbb{Z})$ equivalent to a moment polygon with the following normals: $\nu_{1}=(0,1), \nu_{2}=(1,0), \nu_{3}=(2,-1)$, up to $\nu_{d}=(d-1,-(d-2))$. When $d=p+1$ this is the moment polygon of the $A_{p}$ toric resolution mentioned in the Introduction (see Figure 3)

Take $\eta=(1,1)$. Then, we see that indeed
$$\eta \cdot \nu_{j}=1, \quad \forall j=1, \cdots, d,$$
while $\nu=(1,-1)$ satisfies
$$\operatorname{det}\left(\nu, \nu_{1}\right)=1>0 \quad \text { and } \quad \operatorname{det}\left(\nu, \nu_{d}\right)=-(d-2)+(d-1)=1>0 .$$
In the general case, we can simply use the $S L(2, \mathbb{Z})$ transformation to determine $v$ and that completes the proof. \(\square\)

Putting the above results together we see that
Proposition 6.4. When $c_{1}(X)=0$, the ALE metrics from Theorem 4.1 are Ricciflat and there is a one parameter family of Ricci-flat metrics among those which are asymptotic to the Taub-NUT metric.

\section*{7. Examples}
7.1. ALE metrics on $\mathcal{O}(-p)$. Let $\Gamma$ be the finite cyclic diagonal subgroup of $U(2)$ generated by
$$e^{\frac{2 i \pi}{p}}\left(\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right) .$$
It is well known that the minimal resolution of $\mathbb{C}^{2} / \Gamma$ is $\mathcal{O}(-p)$. As mentioned in the Introduction, LeBrun [L1] constructed ALE scalar-flat toric Kähler metrics on these non-compact complex surfaces. Their symplectic potentials can easily be written down explicitly since these metrics can be seen as part of Calabi's family of extremal Kähler metrics (see [A4]). Here, as a warm-up, we will see how to obtain these symplectic potentials using our method.

The moment polygon of $X=\mathcal{O}(-p)$ has normals $\nu_{1}=(0,1), \nu_{2}=(1,0)$ and $\nu_{3}=(p,-1)$ (see Figure 2).

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/162ce568-c28b-4fe6-8a3b-77dc65ba6e91-25.jpg?height=215&width=168&top_left_y=400&top_left_x=980}
\captionsetup{labelformat=empty}
\caption{Figure 2. The moment polygon of $\mathcal{O}(-p)$.}
\end{figure}