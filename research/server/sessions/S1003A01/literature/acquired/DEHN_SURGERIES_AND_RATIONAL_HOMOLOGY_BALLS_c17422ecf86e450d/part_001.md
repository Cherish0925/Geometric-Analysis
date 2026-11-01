---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: DEHN SURGERIES AND RATIONAL HOMOLOGY BALLS]

---
source_file: Dehn_surgeries_and_rational_homology_balls_a138d5dd883e.pdf
converter: mathpix
format: mmd
---

\title{
DEHN SURGERIES AND RATIONAL HOMOLOGY BALLS
}

\author{
PAOLO ACETO AND MARCO GOLLA
}

\begin{abstract}
We consider the question of which Dehn surgeries along a given knot bound rational homology balls. We use Ozsváth and Szabó's correction terms in Heegaard Floer homology to obtain general constraints on the surgery coefficients. We then turn our attention to the case of integral surgeries, with particular emphasis on positive torus knots. Finally, combining these results with a lattice-theoretic obstruction based on Donaldon's theorem, we classify which integral surgeries along torus knots of the form $T_{k q \pm 1, q}$ bound rational homology balls.
\end{abstract}

\section*{1. Introduction}

A filling of a closed 3-manifold $Y$ is a smooth, compact 4-manifold $Z$ with $\partial Z=Y$. It is very natural to ask how simple fillings of a given $Y$ can be: Lickorish [13] and Wallace [31] showed that there is always a simply-connected filling; Milnor [18] proved that there is always a spin filling. The Rokhlin invariant [29] and, more recently, Donaldson's theorems [5] provided formidable obstructions to the existence of fillings which are integral or rational homology balls (i.e. have the same homology of a point, with integral or rational coefficients).

On the more constructive side, Casson and Harer [4] built families of Seifert fibred spaces admitting a rational homology ball filling. Lisca [14, 15] used Donaldson's theorem to find all relations among lens spaces in the rational homology 3-dimensional cobordism group. Lecuona [12] tackled the problem of determining which 3-legged Seifert fibred spaces bound rational homology balls; the first author [1] studied which rational homology $S^{1} \times S^{2}$ 's bound rational homology $S^{1} \times D^{3}$ 's.

In another direction, Owens and Strle [22] addressed the question of when the intersection form of $Z$ can be negative definite, in the case when $Y$ is obtained as Dehn surgery along a knot in $S^{3}$, and answered it completely in the case of torus knots.

Given a knot $K$ in $S^{3}$ we address the following question: which Dehn surgeries along $K$ bound rational homology balls? From this viewpoint Lisca's work [14] can be regarded as a complete answer for the unknot. Moreover, since Dehn surgeries on concordant knots are homology cobordant, this provides a complete answer for every smoothly slice knot.

We use Ozsváth and Szabó's correction terms in Heegaard Floer homology [23] to obtain constraints on the surgery coefficients. For instance, we prove the following.

Theorem 1.1. For every knot $K$ and every positive integer $q$, there exist finitely many positive integers $p$ such that $S_{p / q}^{3}(K)$ bounds a rational homology ball.

Many of our results will be expressed in terms of the knot invariant $\nu^{+}$, a byproduct of the Heegaard Floer package defined by Hom and Wu [9] (see Section 3 below).

Theorem 1.2. There are at most two positive integer values of $n$ such that $S_{n}^{3}(K)$ bounds a rational homology ball; if there are two, they are consecutive squares and $1+8 \nu^{+}(K)$ is a perfect square.

We then turn our attention to the case of positive torus knots. We prove the following:
Theorem 1.3. If $p, q>1$ are coprime integers with $p>9 q$, then no positive integral surgery along $T_{p, q}$ bounds a rational homology ball.

Finally, combining these results with a lattice-theoretic obstruction based on Donaldson's theorem, we classify which integral surgeries along torus knots of the form $T_{k q \pm 1, q}$ bound rational homology balls.

Theorem 1.4. Let $p, q>1$ be integers such that $p \equiv \pm 1(\bmod q)$. The 3-manifold $S_{n}^{3}\left(T_{p, q}\right)$ bounds a rational homology ball if and only if the triple $(p, q ; n)$ is one of the following:
\begin{itemize}
\item[(i)] $(p, q ; n)=\left(q+1, q ; q^{2}\right)$ for some $q \geq 2$;
\item[(ii)] $(p, q ; n)=\left(q+1, q ;(q+1)^{2}\right)$ for some $q \geq 2$;
\item[(iii)] $(p, q ; n)=\left(4 q \pm 1, q ;(2 q)^{2}\right)$ for some $q \geq 2$;
\item[(iv)] $(p, q ; n) \in\{(5,2 ; 9),(5,3 ; 16),(13,2 ; 25)\}$;
\item[(v)] $(p, q ; n) \in\{(9,4 ; 36),(25,4 ; 100)\}$;
\item[(vi)] $(p, q ; n) \in\{(17,3 ; 49),(22,3 ; 64),(43,6 ; 256)\}$.
\end{itemize}
The manifolds corresponding to triples in (iv) are lens spaces; the ones corresponding to triples in (v) are connected sums of two lens spaces; all the other manifolds are Seifert fibred over $S^{2}$ with three singular fibres.

It is very interesting to compare our list with the list of [6], where Fernández de Bobadilla, Luengo, Melle Hernández and Némethi classify singularities with one Puiseux pair that appear as cusps of rational unicuspidal curves in the complex projective plane. The complement of a regular neighbourhood of such a curve (taken with the opposite orientation with respect to the one inherited by $\mathbb{C P}^{2}$ ) is in fact a rational homology ball whose boundary is a positive surgery along a torus knot (see also [3]).

The family (ii) and the sub-family $\left(4 q-1, q ;(2 q)^{2}\right)$ above correspond to the families (a) and (b) in [6, Theorem 1.1]; the cases (2, 13; 25), (4, 25; 100), belong to the families (d) and (c), respectively, while (3, 22; 64), and (6, 43; 256) correspond to cases (e) and (f). On one hand, the comparison shows that the topological setting is, perhaps unsurprisingly, richer than the algebraic setting; on the other, it shows that the two non-algebraic infinite families we find are not-too-far from the algebraic ones. Finally, it also shows that there are many more triples $(p, q ; n)$ for which $S_{n}^{3}\left(T_{p, q}\right)$ bounds a rational homology ball, if we drop the assumption $p \equiv \pm 1(\bmod q)$ (namely, the families (c) and (d) in [6, Theorem 1.1]).

In a forthcoming paper, joint with Kyle Larson, we will address related questions for integral surgeries along cables of knots.

Organisation of the paper. In Section 2 and Section 3 we recall some basic facts about plumbings and Donaldson's theorem, and about correction terms in Heegaard Floer homology. In Section 4 we study correction terms of lens spaces and rational
surgeries along knots in $S^{3}$ and prove Theorem 4.12, which is a quantitative version of Theorem 1.1. In Section 5 we focus on integral surgeries and prove Theorem 1.2 as a corollary of Theorem 5.1; we then turn to the special cases of alternating and torus knots, proving Theorem 1.3. Finally, in Section 6 we study in more detail surgeries along torus knots and we prove Theorem 1.4.

Acknowledgements. We would like to thank József Bodnár, Daniele Celoria, Kyle Larson, Francesco Lin, Paolo Lisca, and Duncan McCoy for interesting conversations. The first author was partially supported by the ERC Advanced Grant LDTBud. The second author was partially supported by the PRIN-MIUR research project 2010-11 "Varietà reali e complesse: geometria, topologia e analisi armonica", by the FIRB research project "Topologia e geometria di varietà in bassa dimensione", and by the Alice and Knut Wallenberg foundation.

\section*{2. Plumbed manifolds and rational homology cobordisms}

In this section we briefly recall the language of plumbed manifolds; we then state the lattice-theoretic obstruction based on Donaldson's diagonalisation theorem which we will use in Section 6, and we study the extension of spin ${ }^{c}$ structures from the boundary to a rational homology ball.
2.1. Plumbings. In this paper, a plumbing graph $\Gamma$ is a finite tree where every vertex has an integral weight assigned to it. To every plumbing graph $\Gamma$ we associate a smooth oriented 4-manifold $P(\Gamma)$ with boundary $\partial P(\Gamma)$ in the following way. For each vertex take a disc bundle over the 2 -sphere with Euler number prescribed by the weight of the vertex. Whenever two vertices are connected by an edge we identify the trivial bundles over two small discs (one in each sphere) by exchanging the role of the fiber and the base coordinates. We call $P(\Gamma)$ (resp. $\partial P(\Gamma)$ ) a plumbed 4-manifold (resp. plumbed 3-manifold).

This definition can be extended to reducible 3-manifolds; if the graph is a finite forest (i.e. a finite disjoint union of trees) we take the boundary connected sum of the plumbed 4-manifolds associated to each connected component of $\Gamma$.

The group $H_{2}(P(\Gamma) ; \mathbb{Z})$ is free Abelian, generated by the zero sections of the sphere bundles (i.e. by vertices of the graph). Moreover, with respect to this basis, the intersection form of $P(\Gamma)$, which we indicate by $Q_{\Gamma}$, is described by the matrix $M_{\Gamma}$ whose entries $\left(a_{i j}\right)$ are defined as follows:
\begin{itemize}
\item[-] $a_{i i}$ equals the Euler number of the corresponding disc bundle,
\item[-] $a_{i j}=1$ if the corresponding vertices are connected,
\item[-] $a_{i j}=0$ otherwise.
\end{itemize}
Finally note that $M_{\Gamma}$ is also a presentation matrix for the group $H_{1}(\partial P(\Gamma) ; \mathbb{Z})$.
Recall from [19] that every plumbed 3-manifold has a unique description via a positive canonical plumbing graph as well as a negative one. Note that if $\Gamma$ is the positive canonical plumbing graph of a plumbed 3-manifold, $Q_{\Gamma}$ is not necessarily positive definite. Moreover, given a plumbed 3-manifold $\partial P(\Gamma)$ where $\Gamma$ is a positive canonical plumbing graph, there is an algorithm to construct the positive plumbing graph of
$-\partial P(\Gamma)$ (i.e. $\partial P(\Gamma)$ with the reversed orientation). We call this graph the dual of $\Gamma$ and we denote it with $\Gamma^{*}$.
2.2. Intersection forms and spin ${ }^{c}$ structures. An integral lattice is a pair $\left(G, Q_{G}\right)$ where $G$ is a free Abelian group, equipped with a symmetric bilinear form $Q_{G}$. We denote with $\left(\mathbb{Z}^{N}, \pm I\right)$ the standard positive or negative definite diagonal integral lattice. A morphism of integral lattices is a homomorphism of Abelian groups which preserves the intersection form. In particular, to a plumbed 3-manifold we can associate the intersection lattice $H_{2}(P(\Gamma) ; \mathbb{Z})$.

The next result is implicit in several papers, see for instance [14] and [12].
Proposition 2.1. Let $\partial P(\Gamma)$ be a rational homology sphere plumbed 3-manifold described by its positive (respectively negative) canonical plumbing graph $\Gamma$ which has N vertices. Suppose that $Q_{\Gamma}$ is definite and that $\partial P(\Gamma)$ bounds a rational homology ball. Then, there exists an injective morphism of integral lattices
$$\left(H_{2}(P(\Gamma) ; \mathbb{Z}), Q_{\Gamma}\right) \hookrightarrow\left(\mathbb{Z}^{N}, I\right)$$
(resp. $\left(H_{2}(P(\Gamma) ; \mathbb{Z}), Q_{\Gamma}\right) \hookrightarrow\left(\mathbb{Z}^{N},-I\right)$ ).
If there exists an embedding as in the statement above, we will often simply say that $H_{2}(P(\Gamma) ; \mathbb{Z})$ (or even $Q_{\Gamma}$ or $\Gamma$ ) embeds.

Proof. Let $W$ be the rational homology ball bounded by $\partial P(\Gamma)$ and let $X=P(\Gamma) \cup-W$. By Donaldson's diagonalisation theorem the intersection form on $X$ is standard and the inclusion $P(\Gamma) \hookrightarrow X$ induces the desired morphism of integral lattices. \(\square\)

We now turn to studying the extension problem for spin ${ }^{c}$ structures. Recall that the space $\operatorname{Spin}^{c}(Z)$ of spin ${ }^{c}$ structures on a manifold $Z$ is freely acted upon by $H^{2}(Z ; \mathbb{Z})$, and that the restriction $\operatorname{Spin}^{c}(Z) \rightarrow \operatorname{Spin}^{c}(Y)$ induced by an inclusion $Y \hookrightarrow Z$ is equivariant with respect to this $H^{2}$-action. Namely, fix a spin ${ }^{c}$ structure $\mathfrak{s}$ on $Z$ and a class $\alpha \in H^{2}(Z ; \mathbb{Z})$; call $\mathfrak{t}$ the restriction of $\mathfrak{s}$ to $Y$ and $\beta \in H^{2}(Y ; \mathbb{Z})$ the restriction of $\alpha$. Then, the restriction of $\alpha \cdot \mathfrak{s}$ is $\beta \cdot \mathfrak{t}$.

The following proposition is well-known, and it will be extensively used in the following sections. For completeness, we also sketch a proof.

Proposition 2.2. Let $K$ be a knot in $S^{3}, r=p / q \neq 0$ be rational, and suppose that $Y=S_{r}^{3}(K)$ bounds a rational homology ball $Z$. Then $p=m^{2}$ is a square and the set of spin ${ }^{c}$ structures on $Y$ that extend to $Z$ is a cyclic quotient of $H^{2}(Z ; \mathbb{Z})$ comprised of $m$ elements.

Sketch of proof. Since $Y$ is a rational homology sphere, $H^{1}(Y ; \mathbb{Z})=0$. Moreover, since $\partial Z=Y$, the map $H^{3}(Y ; \mathbb{Z}) \rightarrow H^{4}(Z, Y ; \mathbb{Z})$ is an isomorphism. The long exact sequence in cohomology for the pair $(Z, Y)$ reads as follows:
$$0 \rightarrow H^{2}(Z, Y ; \mathbb{Z}) \rightarrow H^{2}(Z ; \mathbb{Z}) \rightarrow H^{2}(Y ; \mathbb{Z}) \rightarrow H^{3}(Z, Y ; \mathbb{Z}) \rightarrow H^{3}(Z ; \mathbb{Z}) \rightarrow 0 .$$
From Poincaré-Lefschetz duality and the universal coefficient theorem, one obtains that all groups involved are finite, and moreover $\left|H^{2}(Z, Y ; \mathbb{Z})\right|=\left|H^{3}(Z ; \mathbb{Z})\right|$ and $\left|H^{2}(Z ; \mathbb{Z})\right|=$ $\left|H^{3}(Z, Y ; \mathbb{Z})\right|$. This shows that $\left|H^{2}(Y)\right|=p$ is a square, and that the image of the map $H^{2}(Z ; \mathbb{Z}) \rightarrow H^{2}(Y ; \mathbb{Z})$ has order $m=\sqrt{p}$.

That is, the set of $\operatorname{spin}^{c}$ structures on $Y$ that extend to $Z$ has order $m$, and since $H^{2}(Y ; \mathbb{Z})$ is cyclic, so is the image of $H^{2}(Z ; \mathbb{Z}) \rightarrow H^{2}(Y ; \mathbb{Z})$. \(\square\)

\section*{3. Correction terms in Heegaard Floer homology}

Heegaard Floer homology is a family of invariants of 3-manifolds introduced by Ozsváth and Szabó [26]; in this paper we are concerned with the 'plus' version, which associates to a rational homology sphere $Y$ equipped with a spin ${ }^{c}$ structure $\mathfrak{t}$ a $\mathbb{Q}$-graded $\mathbb{Z}[U]$-module $\operatorname{HF}^{+}(Y, \mathfrak{t})$. Recall that the action of $U$ decreases the degree by 2.

The group $\operatorname{HF}^{+}(Y, \mathfrak{t})$ further splits as a direct sum of $\mathbb{Z}[U]$-modules $\mathcal{T}^{+} \oplus \mathrm{HF}_{\text {red }}^{+}(Y, \mathfrak{t})$, where $\mathcal{T}^{+}=\mathbb{Z}\left[U, U^{-1}\right] / U \cdot \mathbb{Z}[U]$. The degree of the element $1 \in \mathcal{T}^{+}$is called the correction term of $(Y, \mathfrak{t})$, and it is denoted by $d(Y, \mathfrak{t})$.

Theorem 3.1 ([23]). The correction term satisfies the following properties:
\begin{itemize}
\item[-] $d(Y, \overline{\mathfrak{t}})=d(Y, \mathfrak{t})=-d(-Y, \mathfrak{t})$, where $\overline{\mathfrak{t}}$ is the conjugate of $\mathfrak{t}$;
\item[-] if $(W, \mathfrak{s})$ is a negative definite spin ${ }^{c} 4$-manifold with boundary $(Y, \mathfrak{t})$, then
$$c_{1}(\mathfrak{s})^{2}+b_{2}(W) \leq 4 d(Y, \mathfrak{t}) .$$
\end{itemize}
In particular $d(Y, \mathfrak{t})$ is invariant under spin ${ }^{c}$ rational homology cobordisms.
Corollary 3.2. If $W$ is a rational homology ball with boundary $Y$, and $\mathfrak{t}$ is a spin ${ }^{c}$ structure on $Y$ that extends to $W$, then $d(Y, \mathfrak{t})=0$.

When $Y$ is obtained as rational surgery along a knot $K$ in $S^{3}$, one can recover the correction terms of $Y$ in terms of a family of invariants of $K$, first introduced by Rasmussen [28] and then further studied by Ni and Wu [21], and Hom and Wu [9]. We call these invariants $\left\{V_{i}(K)\right\}_{i \geq 0}$, adopting Ni and Wu's notation instead of Rasmussen's - who used $h_{i}(K)$ instead - as this seems to have become more standard.

We denote with $\mathcal{O}$ the unknot.
Theorem 3.3 ([21, 28]). The sequence $\left\{V_{i}(K)\right\}_{i \geq 0}$ takes values in the non-negative integers and is eventually 0. Moreover, $V_{i}(K)-1 \leq V_{i+1}(K) \leq V_{i}(K)$ for every $i \geq 0$.

For every rational number $p / q$ and for an appropriate indexing of spin ${ }^{c}$ structures on $S_{p / q}^{3}(\mathcal{O})$ and $S_{p / q}^{3}(K)$, we have
$$d\left(S_{p / q}^{3}(K), i\right)=-2 \max \left\{V_{\lfloor i / q\rfloor}(K), V_{\lceil(p-i) / q\rceil}(K)\right\}+d\left(S_{p / q}^{3}(\mathcal{O}), i\right) .$$

Definition 3.4 ([9]). The minimal index $i$ such that $V_{i}(K)=0$ is called $\nu^{+}(K)$.
In order to know the correction terms of $S_{p / q}^{3}(K)$ it suffices to know the values of $V_{i}(K)$ for each $i$ as well as the values of the correction terms of lens spaces.

Proposition 3.5 ([23, Proposition 4.8]). Let $p, q, i$ be integers with $p>q>0$, $\operatorname{gcd}(p, q)=1$ and $0 \leq i<p+q$. Denote with $r$ and $j$ the reductions of $p$ and $i$ mod $q$ respectively. Then, for an appropriate indexing of spin ${ }^{c}$ structures,
$$d(L(p, q), i)=\frac{1}{4}-\frac{(p+q-2 i-1)^{2}}{4 p q}-d(L(q, r), j) \text {. }$$

Remark 3.6. Notice that in [9, 21, 23] the lens space $L(p, q)$ is defined as obtained by doing $p / q$-surgery along the unknot $\mathcal{O}$. We adopt the convention that $L(p, q)$ is obtained by doing $-p / q$-surgery along $\mathcal{O}$, following [14,19] (among others): this explains the sign difference in Equation (2) with respect to the original.

\section*{4. Generalities on rational surgeries}

In this section we study correction terms of lens spaces; we then turn to surgeries along arbitrary knots in the 3-sphere.
4.1. Correction terms of lens spaces. Recall from [14] that the function $I: \mathbb{Q}_{>1} \rightarrow$ $\mathbb{Z}$ is defined in terms of the negative continued fraction expansion as follows. If $p / q \in \mathbb{Q}$ is larger than 1, we denote with $\left[a_{1}, \ldots, a_{n}\right]^{-}$, where $a_{i} \geq 2$ for each $i$, its negative continued fraction expansion, that is $p / q=a_{1}-\frac{1}{a_{2}-\ldots}$. If $p / q=\left[a_{1}, \ldots, a_{n}\right]^{-}$, we let
$$I(p / q)=\sum_{i=1}^{n}\left(a_{i}-3\right) .$$
Given a rational number $p / q>1$, we associate to $p / q$ the linear plumbing $P(p / q)$ represented by the diagram with $n$ vertices and weights $-a_{1}, \ldots,-a_{n}$. Its plumbing graph is the following:
$$-a_{1}-\cdots \square^{-a_{n}}$$
Recall that $P(p / q)$ is the negative canonical plumbing with boundary $L(p, q)$ and that its associated intersection form is negative definite.

Definition 4.1. We say that a rational number $p / q=\left[a_{1}, \ldots, a_{n}\right]^{-}>1$ is embeddable if there exists an embedding of the integral lattice associated to $P(p / q)$ in $\left(\mathbb{Z}^{n},-I\right)$.

Remark 4.2. We observe here that if $S_{p / q}^{3}(K)$ bounds a rational homology ball, then $p / q$ is embeddable. To this end, recall that one can express a rational surgery along a knot $K$ as an integral surgery along a link as follows: consider the negative continued fraction expansion $p / q=\left[a_{1}, \ldots, a_{n}\right]^{-}$; then $S_{p / q}^{3}(K)$ is obtained by doing integral surgery on the link shown in Figure 1. In particular, the intersection form of the corresponding 4-dimensional 2-handlebody is the same as the intersection form of $P(p / q)$, and the claim follows from the proof of Proposition 2.1.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/72ba5561-4a2e-4e16-9100-e636a5a592d5-06.jpg?height=338&width=1175&top_left_y=1946&top_left_x=473}
\captionsetup{labelformat=empty}
\caption{Figure 1. The integral surgery picture for $p / q$-surgery along $K$, where $p / q=\left[a_{1}, \ldots, a_{n}\right]^{-}$.}
\end{figure}

Lemma 4.3. If $p / q>1$ is embeddable and $I(p / q)<0$, then $L(p, q)$ bounds a rational homology ball.

This result is implicit in Lisca's paper [14]; here we adopt his notation.
Proof (sketch). [14, Theorem 6.4] shows that the standard subset associated to $p / q$ with $I(p / q)<0$ can be contracted to the standard subset associated to 4/3; in [14, Section 7] this fact is used to characterise the set of possible continued fraction expansions of $p / q$; in [14, Section 8], by direct inspection it is shown that each of these lens spaces does in fact bound a rational homology ball. \(\square\)

Lemma 4.4. Let $p=m^{2}$ and $q$ be positive integers. If there exists $0 \leq k<m$ such that
$$d(L(p, q), k)=d(L(p, q), k+m)=\cdots=d(L(p, q), k+(m-1) m)=0,$$
then $q \geq m-1$. In particular, this holds if $L(p, q)$ bounds a rational homology ball.
Proof. By Proposition 2.2 and Corollary 3.2, if $L(p, q)$ bounds there exists an integer $0 \leq k_{0}<p$ such that $d\left(L(p, q), k_{0}+h m\right)=0$ for each integer $h$ (where we think of the spin ${ }^{c}$ structures as being cyclically labelled). In particular, we can assume that $k_{0}=k$ is the remainder of the division of $k_{0}$ by $m$, and hence $0 \leq k<m$. This shows that the second part of the statement follows from the first.

Suppose now that the assumption hold and that, by contradiction, $q \leq m-2$. In this case, $k+q m<p$, and hence
$$d(L(p, q), k)=d(L(p, q), k+q m)=0 .$$
We now apply Equation (2) to both correction terms above and subtract them, to obtain
$$\frac{(k+q m)^{2}}{p q}-\frac{k^{2}}{p q}-m q\left(\frac{1}{p q}-\frac{1}{p}-\frac{1}{q}\right)=0,$$
from which one gets
$$0=2 k+m q+1-m^{2}-q<0,$$
yielding a contradiction. \(\square\)

Lemma 4.5. Whenever $q, r$ are coprime and $0<r<q$, for every $0 \leq j \leq q-1$ we have $4|d(L(q, r), j)| \leq q-1$. Moreover, if equality is attained then $r$ is either 1 or $q-1$.

Proof. The statement is symmetric with respect to the involution $r \mapsto q-r$, hence we can assume $r<q / 2$. Moreover, if $r=1$ and if $q=5, r=2$ the result can be readily checked from Equation (2); hence, we can suppose $q \geq 6$ and $2 \leq r<q / 2$.

We will proceed by induction on $q$. We now apply the recursion for $0 \leq j<q$ :
$$d(L(q, r), j)=\frac{1}{4}-\frac{(q+r-2 j-1)^{2}}{4 q r}-d(L(r, s), k)$$

Notice that the second summand is bounded from above by 0 and from below by $-\frac{(q+r-1)^{2}}{4 q r}$, while the last summand is bounded by $\frac{r-1}{4}$ in absolute value, by the inductive assumption.

Summing up,
$$4 d(L(q, r), j) \leq 1+0+r-1=r<q-1$$
and
$$\begin{aligned}
-4 d(L(q, r), j) & \leq-1+\frac{(q+r-1)^{2}}{q r}+r-1= \\
& =-1+\left(\frac{q-2}{r}+r\right)+2+\frac{r}{q}-\frac{2}{q}+\frac{1}{q r}-1 .
\end{aligned}$$
Now notice that $\frac{q-2}{r}+r$ is bounded from above by $\frac{2(q-2)}{q-1}+\frac{q-1}{2}<\frac{q+3}{2}$, that $\frac{r}{q}<\frac{1}{2}$, and that $\frac{1}{q r}<\frac{2}{r}$. Therefore,
$$-4 d(L(q, r), j)<\frac{q}{2}+\frac{3}{2}+\frac{1}{2}=\frac{q}{2}+2,$$
and the latter quantity is bounded by $q-1$ if $q \geq 6$. \(\square\)

Lemma 4.6. Let $p / q$ be an embeddable rational number. Then at least one of the correction terms of $L(p, q)$ vanishes.

Proof. Let $\left[a_{1}, \ldots, a_{n}\right]^{-}$be the negative continued fraction expansion of $p / q$.
The plumbing $P=P(p / q)$ has no bad vertices in the sense of [25], hence the correction terms of its boundary can be computed in terms of the squares of the characteristic vectors in $H_{2}(P)$. More specifically, it follows from [25, Corollary 1.5] that
$$d(-Y, \mathfrak{t})=\frac{1}{4}\left(\max c_{1}^{2}(\mathfrak{s})+n\right)$$
where the maximum is taken over all spin ${ }^{c}$ structures on $P$ whose restriction to $Y$ is $\mathfrak{t}$.
Fix an embedding of the intersection lattice $L \cong H_{2}(P ; \mathbb{Z})$ of $P$ in the negative definite diagonal lattice $D=\left(\mathbb{Z}^{n},-I\right)$, with a fixed orthonormal basis $\left\{e_{1}, \ldots, e_{n}\right\}$. The vector space $L_{\mathbb{Q}}:=L \otimes \mathbb{Q}=D \otimes \mathbb{Q}$ comes with a natural scalar product, and there is an embedding $\iota$ of the dual lattice $L^{*}$ into $L_{\mathbb{Q}}$ that turns evaluations into products. That is, for every $\lambda \in L^{*}$ and $l \in L$ we have
$$\lambda(l)=\iota(\lambda) \cdot l$$
The sum $s=e_{1}+\cdots+e_{n} \in L_{\mathbb{Q}}$ is in $L^{*}$, and it is a characteristic covector (since it is a characteristic vector in $D$ ); $s$ also maximises the norm among characteristic vectors in $D$, and in particular it maximises the norm in the set $s+L$. By Equation (3) the associated spin ${ }^{c}$ structure on $-Y$ has correction term $\left(s^{2}+n\right) / 4=0$. \(\square\)

Lemma 4.7. If $p=m^{2}$ is a square and $d(L(p, q), i)$ is an integer, then $2 i+1 \equiv q$ $(\bmod m)$.

Proof. Recall that correction terms of lens spaces can be computed in terms of Dedekind and Dedekind-Rademacher sums; we only need two properties of these sums, and we refer the reader to [10,11] for precise definitions and proofs.

More specifically, it is shown in [11, Theorem 1.2] that
$$d(L(q, t), j)=2 s(t, q ; j)+s(t, q)-\frac{1}{2 q}$$
where $s(t, q ; j), s(t, q)$ are two rational numbers such that $6 q s(t, q)$ and $12 q s(t, q ; j)$ are both integers (see [10, Section 2], where the notation for $s(t, q ; j)$ is $r_{j}(t, q)$ ). In particular, $12 q d(L(q, t), j)$ is an integer for each $j$.

We apply Equation (4) setting $t=p$ and $j$ equal to the reduction of $i$ modulo $q$ : if $d(L(p, q), i)$ is an integer, then so is $12 q d(L(p, q), i)$. However, applying Equation (2),
$$12 q d(L(p, q), i)=3 q-3 \frac{(p+q-2 i-1)^{2}}{p}-12 q d(L(q, t), j),$$
and this implies that $3\left(\frac{p+q-2 i-1}{m}\right)^{2}$ is an integer, hence that $m$ divides $m^{2}+q-2 i-1$, which is equivalent to the thesis. \(\square\)

Lemma 4.8. If $p=m^{2}$ and $d(L(p, q), i) \in \mathbb{Z}$ then $d(L(p, q), i+m) \in \mathbb{Z}$. Moreover, if $d(L(p, q), i)$ and $d\left(L(p, q), i^{\prime}\right)$ are both integers, then $m \mid\left(i-i^{\prime}\right)$.

The proof of this lemma follows closely the proof of [11, Corollary 1.8].
Proof. Recall that [11, Lemma 2.2] asserts that $2 p d(L(p, q), i)$ and $2 q d(L(q, r), j)$ are integers for every $i$ and $j$. We refine this by applying Equation (2) with $i<p$ and $i+q$ : subtracting the two equations and multiplying by $p$ we obtain that
$$p d(L(p, q), i) \equiv p d(L(p, q), i+q) \quad(\bmod 1),$$
i.e. either $p d(L(p, q), i)$ is integer for each $i$, or it is a half-integer for each $i$.
Consider Equation (2) for $i$ and $i^{\prime}$, and let $j$ and $j^{\prime}$ be the reductions of $i$ and $i^{\prime}$ modulo $q$; multiplying by $q$ and subtracting the two identities we get:
$$q\left(d(L(p, q), i)-d\left(L(p, q), i^{\prime}\right)\right)=\frac{\left(i^{\prime}-i\right)\left(p+q-i-i^{\prime}-1\right)}{p}-q d(L(q, r), j)+q d\left(L(q, r), j^{\prime}\right) .$$

We are now in position to prove that if $d(L(p, q), i)$ is an integer, then also $d(L(p, q), i+$ $m$ ) is. Set $i^{\prime}=i+m$ in Equation (5). Notice that $d(L(p, q), i)$ is an integer by assumption, and the last two summands on the right-hand side are either both integers or both half-integers, and in either case their sum is an integer. Moreover, $i-i^{\prime}=m$ by assumption, and $m$ divides $p+q-i-i^{\prime}-1=p+2-2 i-m-1$ by Lemma 4.7. It follows that $q d\left(L(p, q), i^{\prime}\right)$ is an integer, and since $2 p d\left(L(q, p), i^{\prime}\right)$ is an integer then so is $d\left(L(p, q), i^{\prime}\right)$.

The second part of the statement is obvious when $p$ is odd. Suppose $p$ is even and $d(L(p, q), i)$ is an integer; combining Lemma 4.7 with the first part of the statement, it is enough to show that $d\left(L(p, q), i+\frac{m}{2}\right)$ is not an integer.

Let $m=2 n$ and plug in $i^{\prime}=i+n$ in Equation (5): multiplying by 2, the left-hand side is congruent to $-2 q d\left(L(p, q), i^{\prime}\right)$ modulo 1, and the right-hand side is congruent to $2 \frac{n(p+q-2 i-n-1)}{4 n^{2}}=\frac{p+q-2 i-1}{2 n}-\frac{1}{2} \equiv \frac{1}{2}$ modulo 1. The first summand is integer by Lemma 4.7, hence $2 q\left(L(p, q), i^{\prime}\right)$ cannot be an integer. \(\square\)

\subsection*{4.2. Correction terms of rational surgeries.}

Lemma 4.9. Let $p=m^{2}$. The correction term $d\left(S_{p / q}^{3}(K), i\right)$ is an integer if and only if $d\left(S_{p / q}^{3}(\mathcal{O}), i\right)$ is. In particular, if $S_{p / q}^{3}(K)$ has an integral correction term, there are exactly $m$ integers $i_{0}, i_{0}+m, \ldots, i_{0}+(m-1) m$ such that $d\left(S_{p / q}^{3}(K), i\right) \in \mathbb{Z}$.

Proof. Using Equation (1), we observe that $d\left(S_{p / q}^{3}(K), i\right)$ is an integer if and only if $d\left(S_{p, q}^{3}(\mathcal{O}), i\right)$ is, and applying Lemma 4.8 we conclude the proof. \(\square\)

Proposition 4.10. Let $0<q<p$ be coprime integers with $I(p / q)<0$, and suppose that $S_{p / q}^{3}(K)$ bounds a rational homology ball; then $\nu_{+}(K)=0$.
Proof. By Remark 4.2, $p / q$ is embeddable; since $I(p / q)<0$, Lemma 4.3 shows that $L(p, q)=S_{-p / q}^{3}(\mathcal{O})$ bounds a rational homology ball. It follows from Lemma 4.4 that $q \geq m-1$, where $m^{2}=p$. Notice also that $I\left(\frac{m^{2}}{m-1}\right)=1>0$, hence the case $p / q=$ $m^{2} /(m-1)$ is excluded, and we can suppose $q>m$.

By Proposition 2.2, $m$ equally spaced correction terms of $L(p, q)$ vanish, and there is an $0 \leq i \leq m-1<q$ such that
$$0=d\left(S_{p / q}^{3}(K), i\right)=d(L(p, p-q), i)-2 V_{\lfloor i / q\rfloor}(K)=0-2 V_{0}(K),$$
hence $V_{0}(K)=0$, or, equivalently, $\nu_{+}(K)=0$. \(\square\)

Remark 4.11. We observe that the following partial converse to the proposition above holds: if $\nu^{+}(K)=0$ and $S_{p / q}^{3}(K)$ bounds, then also $L(p, q)$ bounds. In fact, since $\nu^{+}(K)=0$, the correction terms of $S_{p / q}^{3}(K)$ are the same as the correction terms of $-L(p, q)=S_{p / q}^{3}(\mathcal{O})$. Since $S_{p / q}^{3}(K)$ bounds, it has $\sqrt{p}$ vanishing correction terms, hence so does $\pm L(p, q)$ and Greene has recently shown that this in turn implies that $L(p, q)$ bounds a rational homology ball [8].

We are now ready to prove a quantitative version of Theorem 1.1.
Theorem 4.12. Let $K$ be a knot in $S^{3}$ with $\nu^{+}(K)=\nu$, and $p, q$ be positive, coprime integers with $p=m^{2}$; suppose that $S_{p / q}^{3}(K)$ bounds a rational homology ball. Then, if $\nu>0$ :
$$\sqrt{(2 \nu-1) q}<m<\frac{q+2+\sqrt{q^{2}+8 q \nu+8}}{2},$$
while if $\nu=0$ then $m \leq q+1$.
Proof. We treat the case $\nu=0$ first. If $\nu=0$, then the correction terms of $S_{p / q}^{3}(K)$ are the same as the correction terms of $-L(p, q)$, and Proposition 2.2 implies that there exists $0 \leq k<m$ such that
$$d\left(L(p, q), \mathfrak{t}_{k}\right)=d\left(L(p, q), \mathfrak{t}_{k+m}\right)=\cdots=d\left(L(p, q), \mathfrak{t}_{k+(m-1) m}\right)=0 .$$
It follows from Lemma 4.4 that $q \geq m-1$.
We now treat the case $\nu>0$. We first rule out the possibility that $p=1$; in fact, if $p=1$, then $S_{p / q}^{3}(K)$ is an integral homology sphere, and by (1) its unique correction term is $-2 V_{0}(K) \neq 0$. In particular, it never bounds a rational homology ball.

We can now suppose $p>1$. We begin by proving the left-hand side inequality: if $p / q>1$, by Remark 4.2 we know that $p / q$ is embeddable.

If $p<q$, we can write ${ }^{1} p / q=\left[1,2, \ldots, 2, a_{1}+1, \ldots, a_{\ell}\right]^{-}$for some $a_{i} \geq 2$. The plumbing graph associated to this continued fraction expansion is negative definite and

\footnotetext{
${ }^{1}$ In Section 4.1 we defined negative continued fraction expansions only for $p / q>1$ and we required that all terms in the expansion be larger than 1 . We make an exception here to treat the case $p / q<1$.
}
the intersection form of the plumbing embeds, according to Remark 4.2. By successively blowing down we obtain an embedding of $P\left(p / q^{\prime}\right)$, where $q^{\prime}=\left[a_{1}, \ldots, a_{\ell}\right]^{-}$, and $0<$ $q^{\prime}=q-\lfloor q / p\rfloor p<p$. In particular, $p / q^{\prime}$ is embeddable and $L\left(p, q^{\prime}\right)=L(p, q)$; by extension, we say that also $p / q$ is embeddable.

Regardless of whether $p<q$ or $p>q$, it follows from Lemma 4.6 that at least one of the correction terms of $S_{p / q}^{3}(\mathcal{O})$ vanishes; choose $i_{0}$ such that $d\left(S_{p / q}^{3}(\mathcal{O}), i_{0}\right)=0$. By Lemma 4.9, the values of $i$ for which $d\left(S_{p / q}^{3}(\mathcal{O}), i\right)$ is an integer are all integers of the form $i=i_{0}+k m$ between 0 and $m-1$.

Since $S_{p / q}^{3}(K)$ bounds a rational homology ball, by Proposition 2.2 there are $m$ spin ${ }^{c}$ structures on $S_{p / q}^{3}(K)$ with vanishing correction terms. In particular, these have to be the $m \operatorname{spin}^{c}$ structures with integral correction term, i.e. the ones labelled with $i_{0}+k m$.

We now apply Equation (1) with $i=i_{0}$ :
$$\begin{aligned}
0=d\left(S_{p / q}^{3}(K), i_{0}\right) & =-2 \max \left\{V_{\left\lfloor i_{0} / q\right\rfloor}(K), V_{\left\lceil\left(p-i_{0}\right) / q\right\rceil}(K)\right\}+d\left(S_{p / q}^{3}(\mathcal{O}), i_{0}\right)= \\
& =-2 \max \left\{V_{\left\lfloor i_{0} / q\right\rfloor}(K), V_{\left\lceil\left(p-i_{0}\right) / q\right\rceil}(K)\right\},
\end{aligned}$$
hence $V_{\left\lfloor i_{0} / q\right\rfloor}(K)=V_{\left\lceil\left(p-i_{0}\right) / q\right\rceil}(K)=0$. These equalities imply that $i_{0} \geq q \nu$ and $p-i_{0}>$ $(\nu-1) q$ respectively, and summing them yields $p>(2 \nu-1) q$.

Notice that this implies, a posteriori, $p>q$.
We now turn to the right-hand side inequality, keeping in mind that we can assume $p>q$. From Equation (2)
$$d\left(L\left(m^{2}, q\right), i\right)=\frac{1}{4}-\frac{\left(m^{2}+q-2 i-1\right)^{2}}{4 m^{2} q}-d(L(q, r), j) .$$
Hence, applying Lemma 4.5, $d\left(L\left(m^{2}, q\right), i\right)$ can vanish only if $\left(m^{2}+q-2 i-1\right)^{2} \leq$ $\left|m^{2} q(4 d(L(q, r), j)+1)\right| \leq m^{2} q^{2}$, that is only if
$$m^{2}-m q \leq 2 i+1-q \leq m^{2}+m q .$$

Moreover, by Lemma 4.7, if $d\left(L\left(m^{2}, q\right), i\right)$ is integral then $2 i+1-q \equiv 0(\bmod m)$, hence if $2 i$ is one of $m^{2}-m q+q-1-m$ or $m^{2}-m q+q-1-2 m$, the corresponding correction term of $L\left(m^{2}, q\right)$ is integral but does not vanish.

If $S_{p / q}^{3}(K)$ bounds a rational homology ball, then for each $i<m^{2}-m q-q-1$ for which the corresponding spin ${ }^{c}$ structure extends, Equation (1) shows that the invariant $V_{\lfloor i / q\rfloor}(K)$ is nonzero, and in particular $\left\lfloor\frac{i}{q}\right\rfloor<\nu$. Thus, the following inequality holds
$$\frac{m^{2}-m q+q-1-2 m}{2}=\min \left\{\frac{m^{2}-m q+q-1-2 m}{2}, \frac{m^{2}-m q+q-1-m}{2}\right\}<q \nu$$
from which the right-hand side inequality follows. \(\square\)

Remark 4.13. We can gain something more from the right-hand side inequality if we assume that $m^{2} \not \equiv \pm 1(\bmod q)$. In this case, we know that the inequality coming from Lemma 4.5 is strict, hence we can use $m^{2}-m q+q-1$ instead of $m^{2}-m q+q-1-2 m$, hence obtaining
$$m<\frac{q+1+\sqrt{(q-1)^{2}+8 q \nu+4}}{2}$$

However, this assumption is not particularly harmful, since whenever $m^{2} \equiv \pm 1(\bmod q)$ the correction terms of $L\left(m^{2}, q\right)$ can be computed explicitly by applying the symmetry formula once, together with the computation of $d(L(q, 1), j)$.

Corollary 4.14. If $p \equiv 1(\bmod q)$, then $S_{p / q}^{3}\left(T_{3,2}\right)$ bounds a rational homology ball if and only if $p=(q+1)^{2}$ or $p / q=25 / 3$.

Proof. First, we observe that the case $p=1$ is excluded by Theorem 4.12.
We are now going to prove the "only if" direction. Let $p=m^{2}, K=T_{3,2}$, and suppose that $S_{p / q}^{3}(K)$ bounds a rational homology ball. Since $m^{2} / q=\left[\left[m^{2} / q\right], 2^{[q-1]}\right]^{-}$, we have that $I\left(m^{2} / q\right)=\left\lceil m^{2} / q\right\rceil-q-2$, and hence $I(p / q)<0$ if $m \leq q-1$. Since $\nu^{+}(K)=1$, Proposition 4.10 shows that $m \geq q+1$.

On the other hand, the right-hand side inequality in Theorem 4.12 says that
$$m<\frac{q+2+\sqrt{q^{2}+8 q+8}}{2}<\frac{q+2+\sqrt{q^{2}+8 q+16}}{2}=q+3,$$
hence the only possible values for $m$ are $q+1$ and $q+2$. Observe that if $m=q+2$, then the condition $m^{2} \equiv 1(\bmod q)$ reads $(q+2)^{2} \equiv 1(\bmod q)$, from which $q \mid 3$. Therefore, the "only if" direction is proved.

When $q \geq 5$, the 3-manifold $S_{(q+1)^{2} / q}^{3}(K)$ bounds the negative definite plumbing associated to the graph (see Section 6.1 below for the details)
![](https://cdn.mathpix.com/cropped/72ba5561-4a2e-4e16-9100-e636a5a592d5-12.jpg?height=337&width=847&top_left_y=1500&top_left_x=638)
which Park, Shin and Stipsicz have proven to bound a rational homology ball (see [27], Figure 1, third graph from the bottom). When $q=4, S_{25 / 4}^{3}(K)=L(25,14)$, and this bounds by the work of Lisca [14].

When $q=3,-S_{16 / 3}^{3}(K)$ bounds the plumbing
![](https://cdn.mathpix.com/cropped/72ba5561-4a2e-4e16-9100-e636a5a592d5-12.jpg?height=268&width=504&top_left_y=2191&top_left_x=810)
and also the plumbing
![](https://cdn.mathpix.com/cropped/72ba5561-4a2e-4e16-9100-e636a5a592d5-13.jpg?height=270&width=799&top_left_y=369&top_left_x=664)

It follows from [1, Proposition 4.6] that $-S_{16 / 3}^{3}(K)$ is rationally homology cobordant to $L(4,3)$, hence it bounds a rational homology ball.

When $q=2, S_{9 / 2}^{3}(K)$ is known to be diffeomorphic to $-S_{9}^{3}(K)$ [17], hence it bounds a rational homology ball as well (e.g. see Theorem 1.4). Finally, $S_{25 / 3}^{3}(K)$ bounds a rational homology ball, too; this was included in Casson-Harer's list [4], setting $p=3, s=4, k=5$ in their first family. \(\square\)

\section*{5. Integral surgeries}

In this section we study integral surgeries along knots in the 3-sphere, and we then focus on alternating knots and torus knots.

The following is a quantitative version of Theorem 1.2.
Theorem 5.1. Let $m$ be a positive integer, $K \subset S^{3}$ be a knot, and suppose that $S_{m^{2}}^{3}(K)$ bounds a rational homology ball. Let $\nu=\nu_{+}(K)$. Then
$$1+\sqrt{1+8 \nu} \leq 2 m<3+\sqrt{9+8 \nu} \quad \text { or, equivalently, } \quad 0 \leq \frac{m(m-1)}{2}-\nu<m .$$

Lemma 5.2. The correction term $d\left(S_{m^{2}}^{3}(K), i\right)$ is integral if and only if $i=m(m-$ $2 k-1) / 2$ for some integer $k$.

Proof. By a direct computation from Equation (2),
$$d\left(S_{m^{2}}^{3}(\mathcal{O}), i\right)=\frac{\left(m^{2}-2 i\right)^{2}}{4 m^{2}}-\frac{1}{4} .$$
This is an integer if and only if $m^{2}-2 i \equiv m(\bmod 2 m)$, which in turn is equivalent to the condition $i=m(m-2 k-1) / 2$ for some integer $k$; the same holds for $S_{m^{2}}^{3}(K)$ in light of Lemma 4.9. \(\square\)

Applying (1) and (6), we obtain:
$$d\left(S_{m^{2}}^{3}(K), i\right)=-2 V_{i}(K)+\frac{\left(m^{2}-2 i\right)^{2}}{4 m^{2}}-\frac{1}{4} .$$

Lemma 5.3. If $S_{m^{2}}^{3}(K)$ bounds a rational homology ball, then
$$d\left(S_{m^{2}}^{3}(K), \frac{m(m-2 k-1)}{2}\right)=0$$
for each $k=0, \ldots,\left\lfloor\frac{m-1}{2}\right\rfloor$.

Proof. It follows from Proposition 2.2 that if $S_{m^{2}}^{3}(K)$ bounds a rational homology ball $Z$, then $m$ of its spin ${ }^{c}$ structures extend to a $Z$; Corollary 3.2, in turn, implies that the corresponding correction terms vanish. Lemma 5.2 now pins down exactly which correction terms of $S_{m^{2}}^{3}(K)$ can be integral: since there are exactly $m$ of them, they must all vanish. \(\square\)

Proof of Theorem 5.1. Notice that the first chain of inequalities is obtained from the second by solving for $m$; hence, we set out to prove the latter.

It follows from Lemma 5.3 the correction term of $S_{m^{2}}^{3}(K)$ corresponding to $\frac{m(m-1)}{2}$ vanishes; if $m \geq 3$, the one corresponding to $\frac{m(m-3)}{2}$ vanishes, too.

Since the correction term corresponding to $\frac{m(m-1)}{2}$ vanishes, from (7) we obtain
$$0=d\left(S_{m^{2}}^{3}(K), \frac{m(m-1)}{2}\right)=-2 V_{\frac{m(m-1)}{2}}(K)+d\left(S_{m^{2}}^{3}(\mathcal{O}), \frac{m(m-1)}{2}\right)=-2 V_{\frac{m(m-1)}{2}}(K),$$
from which we obtain the inequality $\frac{m(m-1)}{2} \geq \nu$.
Notice now that if $m<3$ then the second inequality is automatically satisfied by $m$, so to prove the remaining part of the statement we can assume $m \geq 3$. From the vanishing of the correction term corresponding to $\frac{m(m-3)}{2}$ from (7) we obtain
$$0=d\left(S_{m^{2}}^{3}(K), \frac{m(m-3)}{2}\right)=-2 V_{\frac{m(m-3)}{2}}(K)+d\left(S_{m^{2}}^{3}(\mathcal{O}), \frac{m(m-3)}{2}\right)=2-2 V_{\frac{m(m-3)}{2}}(K),$$
from which $\frac{m(m-1)}{2}-m=\frac{m(m-3)}{2}<\nu$. \(\square\)

We are now ready to prove Theorem 1.2.
Proof of Theorem 1.2. Let $\nu=\nu^{+}(K)$. Theorem 5.1 asserts that, if $S_{m^{2}}^{3}(K)$ bounds a rational homology ball, then $2 m$ is in the interval $I_{\nu}=[1+\sqrt{1+8 \nu}, 3+\sqrt{9+8 \nu}) ; I_{\nu}$ has length
$$2+\sqrt{9+8 \nu}-\sqrt{1+8 \nu}=2+\frac{8}{\sqrt{9+8 \nu}+\sqrt{1+8 \nu}} \leq 4,$$
hence it contains at most two even integers, and, if it contains two, they are consecutive.
Moreover, if $I_{\nu}$ contains two even integers, then we have
$$1+\sqrt{1+8 \nu} \leq 2 m<2 m+2<3+\sqrt{9+8 \nu} .$$
The left-hand side inequality can be rearranged as $1+8 \nu \leq(2 m-1)^{2}$, while the right-hand side inequality reads $(2 m-1)^{2}<9+8 \nu$; that is,
$$1+8 \nu \leq(2 m-1)^{2}<9+8 \nu .$$
Since odd squares are congruent to 1 modulo 8, we have $(2 m-1)^{2}=1+8 \nu$. \(\square\)

Example 5.4. There exist knots that have two positive, integral surgeries bounding a rational homology ball: if $K$ is the $(q+1, q)$-torus knot, then Theorem 1.4 shows that both $S_{q^{2}}^{3}(K)$ and $S_{(q+1)^{2}}^{3}(K)$ bound rational homology balls.

The second example is in fact realised in an algebro-geometric fashion [6]: the curve $C=\left\{x^{q+1}+y^{q} z\right\}$ is rational with a unique singularity at (0, 0, 1), of type $(q+1, q)$; the boundary of an open regular neighbourhood of $C$ is $-S_{(q+1)^{2}}^{3}(K)$.

Remark 5.5. When $m$ is odd and $S_{m^{2}}^{3}(K)$ bounds a rational homology ball, we can also infer that $m^{2}=1+8 V_{0}(K)$. In particular, $1+8 V_{0}(K)$ is a perfect square.

This follows immediately from the fact that when $m$ is odd, the spin ${ }^{c}$ structure labelled with 0 extends to the rational homology ball, hence
$$0=d\left(S_{m^{2}}^{3}(K), 0\right)=-2 V_{0}(K)+d\left(L\left(m^{2},-1\right), 0\right)=-2 V_{0}(K)+\frac{m^{2}-1}{4} .$$
5.1. Alternating knots. The knot Floer homology of alternating knots is very simple, and it is fully determined by the Alexander polynomial and the signature [24]; in fact, alternating knots are Floer-thin, in the sense that their knot Floer homology is supported on a diagonal with constant $i-j$ (we refer to [24] for the notation).

More generally, quasi-alternating knots have been shown to be Floer-thin by Manolescu and Ozsváth [16]; for all quasi-alternating knots, the constant $i-j$ is equal to half of the signature.

Proposition 5.6. Let $K$ be a Floer-thin knot supported on the diagonal $i-j=\sigma / 2$, and $m$ be an integer such that $S_{m^{2}}^{3}(K)$ bounds a rational homology ball. Then $m \leq 5$.

Moreover:
\begin{itemize}
\item[-] if $m=1, \sigma \geq 0$;
\item[-] if $m=2, \sigma \geq-2$;
\item[-] if $m=3$, either $\sigma=-2$ or $\sigma=-4$;
\item[-] if $m=4$, either $\sigma=-6$ or $\sigma=-8$;
\item[-] if $m=5, \sigma=-12$.
\end{itemize}

In particular, the statement holds when $K$ is alternating, and $\sigma=\sigma(K)$ is its signature.

Proof. Combining results from [16,24] as in [9, Theorem 2], one has:
$$V_{i}(K)=\max \left\{\left\lceil\frac{\tau(K)-i}{2}\right\rceil, 0\right\} .$$

Suppose $m \geq 5$. According to Lemma 5.3, the spin ${ }^{c}$ structures on $S_{m^{2}}^{3}(K)$ labelled by $\frac{m(m-2 k-1)}{2}$ for $k=0,1,2$ have vanishing correction term. By (7), one gets:
$$V_{\frac{m(m-3)}{2}}(K)=1, \quad V_{\frac{m(m-5)}{2}}(K)=3$$
But it follows from Equation (8) that $\left|V_{i}(K)-V_{j}(K)\right| \geq\lfloor|i-j| / 2\rfloor$, and therefore $2 \geq\lfloor m / 2\rfloor$, from which $m \leq 5$.

As for the second part of the statement, recall that when $K$ is Floer-thin, one has that $2 \tau(K)=-\sigma$, and moreover
$$\nu^{+}(K)= \begin{cases}\tau(K) & \text { if } \tau(K) \geq 0 \\ 0 & \text { if } \tau(K)<0\end{cases}$$
Bearing these in mind:
\begin{itemize}
\item[-] if $m=1$, then $V_{0}(K)=0$, hence $\tau(K) \leq 0, \sigma(K) \geq 0$;
\item[-] if $m=2$, then $V_{1}(K)=0$, hence $\tau(K) \leq 1, \sigma(K) \geq-2$;
\item[-] if $m=3$, then $V_{0}(K)=1$, from which either $\tau(K)=1$ or $\tau(K)=2$;
\item[-] if $m=4$, then $V_{2}(K)=1$, from which either $\tau(K)=3$ or $\tau(K)=4$;
\end{itemize}
\begin{itemize}
\item[-] if $m=5$, then $V_{0}(K)=3$ and $V_{5}(K)=1$, from which $\tau(K)=6$.
\end{itemize} \(\square\)

Remark 5.7. Notice that Theorem 1.4 shows that all cases with $\sigma<0$ above are realised; the cases with $\sigma=0$ are realised by the unknot. Finally, Fintushel and Stern [7] have proved that $S_{+1}^{3}\left(T_{3,-2}\right)$ bounds a rational homology ball, hence showing that the pair $(\sigma, m)=(2,1)$ is realised, too.
5.2. Torus knots. Now we can prove Theorem 1.3. A second proof will be given in Section 6.1.

First proof of Theorem 1.3. The case of integral surgeries along alternating torus knots (i.e. $T_{2 k+1,2}$ ) has already been treated in Proposition 5.6, hence we will focus on the case $q>2$.

Recall that for a torus knot $T_{p, q}$ the function $V(i)=V_{i}\left(T_{p, q}\right)$ is related to the gap counting function $I_{\Gamma}$ of the semigroup $\Gamma=\langle p, q\rangle \subset \mathbb{Z}_{\geq 0}$ generated by $p$ and $q$ as follows. Let $\nu=\nu^{+}\left(T_{p, q}\right)$, and recall that $\nu=g\left(T_{p, q}\right)=\frac{(p-1)(q-1)}{2}$. The function $I_{\Gamma}$ is defined as
$$I_{\Gamma}(j)=\#\left(\mathbb{Z}_{\geq j} \backslash \Gamma\right) ;$$
Borodzik and Livingston [3] proved that
$$V(j)=I_{\Gamma}(j+\nu) .$$
In particular, $V(j)=1$ exactly when $j+\nu$ varies between the second largest gap of the semigroup and its largest gap, i.e. between the last two elements that are not expressible as a nonnegative integer combination of $p$ and $q$. Similarly, $V(j)=2$ between the second and third largest gaps. The largest gap is well-known to be $g_{1}=p q-p-q=2 \nu-1$. A graph of the function $V(\cdot)$ is sketched in Figure 2.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/72ba5561-4a2e-4e16-9100-e636a5a592d5-16.jpg?height=791&width=1408&top_left_y=1521&top_left_x=357}
\captionsetup{labelformat=empty}
\caption{Figure 2. A portion of the graph of the function $V(\cdot)$, under the assumption $p>9 q$. We let $\nu=\nu\left(T_{p, q}\right)=\frac{(p-1)(q-1)}{2}$.}
\end{figure}

Suppose now that $p>9 q$.
In what follows, we will need to use Lemma 5.3 with $k=4$, and this is allowed only when $m \geq 9$. However, we notice that if $q>3$, then $\nu \geq \frac{9 q(q-1)}{2} \geq 36>28$, and that if $q=3$ and $p>29$ then $\nu>28$; in both cases, thanks to Theorem 5.1, $m$ is strictly larger than $\frac{1+\sqrt{1+28 \cdot 8}}{2}=8$.

The two cases $q=3, p=28,29$ need separate treatment: in both instances, Theorem 5.1 implies that the only possible value of $m$ is 8, and a direct computation shows that the correction term $d\left(S_{64}^{3}\left(T_{p, 3}\right), 20\right)$ is -4. That is, $S_{64}^{3}\left(T_{28,3}\right)$ and $S_{64}^{3}\left(T_{29,3}\right)$ do not bound rational homology balls.

Since neither $T_{28,3}$ nor $T_{29,3}$ has a surgery that bounds a rational homology ball, we can suppose that $\nu>28$, and in particular $m \geq 9$.

Recall that the semigroup of the singularity is symmetric [30, Theorem 4.3.5], in the sense that $x$ belongs to the semigroup if and only if $p q-p-q-x$ does not. Hence, since $p>9 q$, the first nine elements of the semigroup are $0, q, \ldots, 9 q$, and therefore the nine largest gaps $g_{9}<\cdots<g_{1}$ are $g_{k}=(q-1) p-k q$ (see Figure 2).

This shows that if $V(i)=10$, then $i<g_{9}-\nu$; if $k=1, \ldots, 9, V(i)=k$ exactly when $g_{k}-\nu \leq i<g_{k-1}-\nu$.

If $S_{m^{2}}^{3}\left(T_{p, q}\right)$ bounds and $m \geq 9$, then Lemma 5.3 implies that its correction terms in the spin ${ }^{c}$ structures labelled by $\frac{m(m-9)}{2}, \frac{m(m-7)}{2}, \frac{m(m-5)}{2}, \frac{m(m-3)}{2}, \frac{m(m-1)}{2}$ must all vanish. Applying Equation (7), we obtain $V\left(\frac{m(m-9)}{2}\right)=10, V\left(\frac{m(m-7)}{2}\right)=6, V\left(\frac{m(m-5)}{2}\right)=3$, $V\left(\frac{m(m-3)}{2}\right)=1$.

These translate into the inequalities
$$\begin{aligned}
\frac{m(m-9)}{2} & <\nu-9 q, \quad \nu-6 q \leq \frac{m(m-7)}{2}<\nu-5 k, \\
\nu-3 q \leq \frac{m(m-5)}{2} & <\nu-2 q, \quad \nu-q \leq \frac{m(m-3)}{2}<\nu .
\end{aligned}$$

In particular, the first row of inequalities implies that $m=\frac{m(m-7)}{2}-\frac{m(m-9)}{2}>3 q$; the second row, on the other hand, shows that $m=\frac{m(m-3)}{2}-\frac{m(m-5)}{2}<3 q$, which leads to a contradiction. \(\square\)
5.3. Asymptotic classification. Recall that Theorem 5.1 asserts that if $S_{m^{2}}^{3}(K)$ bounds a rational homology ball, then
$$\frac{1+\sqrt{1+8 \nu}}{2} \leq m<\frac{3+\sqrt{9+8 \nu}}{2},$$
from which one obtains
$$2 \nu+2-(1+\sqrt{1+8 \nu}) \leq(m-1)(m-2)<2 \nu+2 .$$
If we call $2 \varepsilon$ the difference $2 \nu+2-(m-1)(m-2)$, we have $0<2 \varepsilon \leq 1+\sqrt{1+8 \nu} \leq 2 m$.
Let us now focus on the case $K=T_{p, q}$, so that $2 \nu=(p-1)(q-1)$. We can recast the inequalities above in terms of the semigroup function $\Gamma$ that associates to an integer $i$ the $i$-th element $\Gamma(i)$ of the semigroup $\Gamma_{p, q}$ generated by $p$ and $q$. Since $q<p$, we always have $\Gamma(1)=0$ and $\Gamma(2)=q$. Manipulating the identity $d\left(S_{m^{2}}^{3}\left(T_{p, q}\right), j\right)=0$ as in
[2, Section 6] yields, for each $j \in\{0, \ldots, m-2\}$, the two inequalities
$$\Gamma\left(\frac{(j+1)(j+2)}{2}\right) \leq j m+\varepsilon$$
and
$$\Gamma\left(\frac{(j+1)(j+2)}{2}+1\right)>j m+\varepsilon$$

These are formally very similar to the inequalities $\left(\star_{j}\right)$ and $\left(\star \star_{j}\right)$ in [2, Section 6.1]. In fact, the two latter inequalities collapse to an identity for $g=0$ (as in [3]), and these identity are sufficient to classify singularities with one Puiseux pairs that appear as the only singularity of a rational plane curve, up to finitely many exceptions [6, Theorem 1.1] (see [2, Remark 1.5]). It is natural to ask whether (9) and (10) are strong enough to provide the same kind of result in the topological, rather than in the complex curve, setting.

Question 5.8. Are (9) and (10) sufficient to recover all but finitely many triples $\left(p, q ; m^{2}\right)$ for which $S_{m^{2}}^{3}\left(T_{p, q}\right)$ bounds a rational homology balls?

\section*{6. Integral surgeries on torus knots}

The goal of this section is the proof of Theorem 1.4. Along the way, we briefly recall the plumbing description for Seifert fibred manifolds and a lemma on rational homology cobordant Seifert manifolds. We also recall Owens and Strle's concordance invariant $m$, and we describe the plumbing graph of the Seifert fibred spaces which arise as Dehn surgery on torus knots.

Suppose $\Gamma$ is a negative canonical plumbing graph with $n$ vertices. Let $-\Gamma$ be the graph with the opposite sign on each weight. Then $\partial P(-\Gamma)=-\partial P(\Gamma)$ and $-\Gamma$ is the positive canonical plumbing graph of $-\partial P(\Gamma)$. The dual of $\Gamma$, i.e. $\Gamma^{*}$, is the negative canonical plumbing graph of $-\partial P(\Gamma)$. Finally $-\Gamma^{*}$ is the positive canonical plumbing graph of $\partial P(\Gamma)$. Note that $-\left(\Gamma^{*}\right)=(-\Gamma)^{*}$. If $\Gamma$ is negative definite then $\Gamma$ embeds in $\left(\mathbb{Z}^{n},-I\right)$ if and only if $-\Gamma$ embeds in $\left(\mathbb{Z}^{n}, I\right)$.

In order to simplify the notation and to make the proofs easier to read, in this section we switch from negative plumbing graphs to positive ones. Since the topological property we want to detect is not affected by reversal of orientation this modification will not affect the arguments in our proofs.
6.1. Preliminaries. We recall from [20] the basic definitions of Seifert manifolds. A closed Seifert fibred manifold over $S^{2}$ can be described by its unnormalized Seifert invariants
$$\left(b ; \frac{\alpha_{1}}{\beta_{1}}, \ldots, \frac{\alpha_{k}}{\beta_{k}}\right) .$$
Here $b, \alpha_{i}, \beta_{i}$ are integers, $\alpha_{i}>1$ and $\operatorname{gcd}\left(\alpha_{i}, \beta_{i}\right)=1$. We denote such a manifold with $Y\left(b ; \frac{\alpha_{1}}{\beta_{1}}, \ldots, \frac{\alpha_{k}}{\beta_{k}}\right)$. These data determine the manifold, but every Seifert fibred manifold admits several such descriptions. A surgery description for $Y\left(b ; \frac{\alpha_{1}}{\beta_{1}}, \ldots, \frac{\alpha_{k}}{\beta_{k}}\right)$ is depicted in Figure 3.

Theorem 6.1. Let $\Gamma$ be the following star-shaped positive canonical plumbing graph.
![](https://cdn.mathpix.com/cropped/72ba5561-4a2e-4e16-9100-e636a5a592d5-19.jpg?height=378&width=489&top_left_y=364&top_left_x=816)
Then $\partial P(\Gamma)$ is orientation-preserving diffeomorphic to $Y\left(b ; \frac{\alpha_{1}}{\beta_{1}}, \ldots, \frac{\alpha_{k}}{\beta_{k}}\right)$ where $\frac{\alpha_{i}}{\beta_{i}}=$ $\left[a_{1}^{i}, \ldots, a_{n_{i}}^{i}\right]^{-}$.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/72ba5561-4a2e-4e16-9100-e636a5a592d5-19.jpg?height=241&width=657&top_left_y=930&top_left_x=750}
\captionsetup{labelformat=empty}
\caption{Figure 3. A surgery description for the Seifert fibred manifold $Y\left(b ; \frac{\alpha_{1}}{\beta_{1}}, \ldots, \frac{\alpha_{k}}{\beta_{k}}\right)$.}
\end{figure}

The following lemma is implicit in [12, Section 3.1]. Here we deduce it as a special case of a more general result which can be found in [1, Section 4].
Lemma 6.2. Let $Y:=Y\left(b ; \frac{\alpha_{1}}{\beta_{1}}, \ldots, \frac{\alpha_{n}}{\beta_{n}}\right)$ be a Seifert manifold with $\alpha_{i}>\beta_{i} \geq 1$ for each $i$. Assume that there exist $h, k$ such that
$$\frac{\beta_{h}}{\alpha_{h}}+\frac{\beta_{k}}{\alpha_{k}}=1 .$$
Let $Y^{\prime}:=Y\left(b-1 ; \frac{\alpha_{1}}{\beta_{1}}, \ldots, \widehat{\frac{\alpha_{h}}{\beta_{h}}}, \ldots, \widehat{\frac{\alpha_{k}}{\beta_{k}}}, \ldots, \frac{\alpha_{n}}{\beta_{n}}\right)$. Then, $Y$ and $Y^{\prime}$ are rational homology cobordant.

Proof. This Lemma is a direct consequence of [1, Proposition 4.6]. In order to apply this result we need to show that the positive canonical plumbing graph of $Y$ is obtained from that of $Y^{\prime}$ by attaching a plumbing graph which represents $S^{1} \times S^{2}$. The attachment is obtained by identifing two vertices, the weight of the new vertex is the sum of the weitghts of the identified vertices.

Consider the linear graph
![](https://cdn.mathpix.com/cropped/72ba5561-4a2e-4e16-9100-e636a5a592d5-19.jpg?height=79&width=937&top_left_y=2099&top_left_x=593)
where $a_{i} \geq 2, b_{j} \geq 2$ for each $i, j$ and
$$\left[a_{1}, \ldots, a_{n}\right]^{-}=\frac{\alpha_{h}}{\beta_{h}} ; \quad\left[b_{1}, \ldots, b_{m}\right]^{-}=\frac{\alpha_{k}}{\beta_{k}} .$$

It is easy to see that this plumbing graph describes the plumbed 3-manifold $S^{1} \times S^{2}$. It follows from Theorem 6.1 that the canonical plumbing graph of $Y$ is obtained from
that of $Y^{\prime}$ by adding two legs with weights $\left(a_{1}, \ldots, a_{n}\right),\left(b_{1}, \ldots, b_{m}\right)$ and by increasing the weight of the central vertex by one. This operation is precisely the attachment described above and the conclusion now follows from [1, Proposition 4.6]. \(\square\)

Observe that, in order to apply Lemma 6.2, one needs $\alpha_{h}=\alpha_{k}$, i.e. that the two fibres must have the same multiplicity.

Given a knot $K \subset S^{3}$ Owens and Strle in [22] introduce the following invariant:
$$m(K)=\inf \left\{r \in \mathbb{Q}_{>0} \mid S_{r}^{3}(K) \text { bounds a negative definite 4-manifold }\right\} .$$
They show that $m$ is a concordance invariant and that it vanishes on negative knots. They also show the following

Theorem 6.3. Let $T_{p, q}$ be the positive $(p, q)$-torus knot. Then
$$m\left(T_{p, q}\right)= \begin{cases}p q-\frac{q}{p *} & \text { if } n \text { is even } \\ p q-\frac{p}{q *} & \text { if } n \text { is odd }\end{cases}$$
where
\begin{itemize}
\item[-] $n$ is the number of steps in the Euclidean algorithm for $p$ and $q$,
\item[-] $0<q^{*}<p$ is such that $q q^{*} \equiv 1(\bmod p)$,
\item[-] $0<p^{*}<q$ is such that $p p^{*} \equiv 1(\bmod q)$.
\end{itemize}

Remark 6.4. Since rational homology balls are negative, definite, if $S_{r}^{3}(K)$ bounds a $\mathbb{Q} H B^{4}$ for some $r>0$ then, $r \geq m(K)$.

We are now in position to give the second proof of Theorem 1.3.
Second proof of Theorem 1.3. It follows from Theorem 6.3 that $m\left(T_{p, q}\right) \geq q(p-1)$; therefore, by the remark above, if $m^{2}<q(p-1)$ then $S_{m^{2}}^{3}\left(T_{p, q}\right)$ does not bound a rational homology ball.

Applying the right-hand side inequality of Theorem 5.1, we get that if
$$\left(\frac{3+\sqrt{9+8 \nu}}{2}\right)^{2} \leq q(p-1),$$
no integral surgery along $T_{p, q}$ bounds a rational homology ball. We now set out to prove that if $p>9 q$ the above inequality holds. Indeed, expanding and substituting $2 \nu=(p-1)(q-1)$ yields
$$3 \sqrt{9+8 \nu} \leq 2 p-11$$
Since $p>9 q \geq 18$, we can square again and obtain
$$81+36 p q-36 p-36 q+36 \leq 4 p^{2}-44 p+121 \Longleftrightarrow 9(p-1) q \leq p^{2}-2 p-1 \Longleftrightarrow 9 q+1 \leq p,$$
which is exactly what we required. \(\square\)

The following lemma is proved in [22, Lemma 4.4].
Lemma 6.5. For any rational number $r$
$$S_{r}^{3}\left(T_{p, q}\right)=Y\left(2 ; \frac{p}{q^{*}}, \frac{q}{p^{*}}, \frac{p q-r}{p q-r-1}\right) .$$

Now we give an explicit description of the canonical plumbing graphs which describe certain surgeries on torus knots.

Proposition 6.6. Assume that $r \notin[p q-1, p q+1]$. The 3 -manifold $S_{r}^{3}\left(T_{p, q}\right)$ can be described via the following positive canonical plumbing graph
![](https://cdn.mathpix.com/cropped/72ba5561-4a2e-4e16-9100-e636a5a592d5-21.jpg?height=270&width=484&top_left_y=536&top_left_x=819)
where $\left[a_{1}, \ldots, a_{n}\right]^{-}=\frac{p}{q^{*}},\left[b_{1}, \ldots, b_{m}\right]^{-}=\frac{q}{p^{*}}$, and:
\begin{itemize}
\item[-] if $r>p q+1$ then $d=1$ and $\left[c_{1}, \ldots, c_{k}\right]^{-}=r-p q$;
\item[-] if $r<p q-1$ then $d=2$ and $\left[c_{1}, \ldots, c_{k}\right]^{-}=\frac{p q-r}{p q-r-1}$.
\end{itemize}

Proof. Note that $\frac{p}{q^{*}}>1$ and $\frac{q}{p^{*}}>1$. Moreover
$$\frac{p q-r}{p q-r-1}=\frac{r-p q}{r-p q+1}=1-\frac{1}{r-p q+1} .$$
If $r-p q>1$, by Lemma 6.5 and Figure 3 we see that $S_{r}^{3}\left(T_{p, q}\right)$ is described by the positive canonical plumbing graph depicted above. The case $r<p q-1$ is analogous. \(\square\)
6.2. Main results. A 2-chain is a linear connected plumbing graph where the weight of every vertex is 2.

Lemma 6.7. Let $\Gamma$ be a positive definite plumbing graph with $m$ vertices. Suppose that there exist vertices $v_{1}, \ldots, v_{k}$ such that $\Gamma \backslash\left\{v_{1}, \ldots, v_{k}\right\}=\Gamma_{1} \sqcup \cdots \sqcup \Gamma_{h}$, where each $\Gamma_{i}$ is a 2 -chain whose length is not 3, there is at most one 2 -chain of length 1 , and $h>k$. Then $\Gamma$ does not embed.

Proof. Every 2 -chain whose length is not 3 has an essentially unique realisation as a sublattice of the standard lattice $\left(\mathbb{Z}^{N}, I\right)$. In particular $N$ is strictly larger than length of the 2-chain. If, moreover, there are no chains of length 1 it is easy to see that each basis vector, say $e_{i}$, appears in the expression of a unique 2 -chain. Therefore every 2-chain requires a set of basis vectors which are orthogonal to each vector belonging to any another 2-chain. It follows that the subgraph $\widetilde{\Gamma}:=\Gamma \backslash\left\{v_{1}, \ldots, v_{k}\right\}=\Gamma_{1} \sqcup \cdots \sqcup \Gamma_{h}$ has a unique realization as a sublattice of the standard lattice $\left(\mathbb{Z}^{N}, I\right)$ and that $N \geq$ $m-k+h>m$. \(\square\)

Following [14], we use the notation $\left[\ldots, 2^{[h]}, \ldots\right]^{-}$to denote a length- $h$ string of 2 in a continued fraction expansion.

Lemma 6.8. For each $q \geq 2$ and $k \geq 1$ we have
\begin{itemize}
\item[(1)] $\frac{k q+1}{k q+1-k}=\left[2^{[q-1]}, k+1\right]^{-}$
\item[(2)] $\frac{k q^{2}+q+1}{q^{2}}=\left[k+1,2^{[q-2]}, 2+q\right]^{-}$
\item[(3)] $\frac{k q^{2}+q-1}{q^{2}}=\left[k+1,2^{[q]}, q\right]^{-}$
\end{itemize}
\begin{itemize}
\item[(4)] $\frac{q^{2}}{q-1}=\left[q+2,2^{[q-2]}\right]^{-}$
\item[(5)] $\frac{q^{2}}{q+1}=\left[q, 2^{[q]}\right]^{-}$
\end{itemize}

These identities can easily be proved by induction. We omit the proof.
Now we are ready to prove Theorem 1.4.
Proof of Theorem 1.4. We start by dealing with two special cases, namely $q=2$ and $k=1$.

First assume that $q=2$. In this case $T_{p, q}$ is alternating and therefore we can apply Proposition 5.6. If $S_{n}^{3}\left(T_{p, q}\right)$ bounds a $\mathbb{Q} H B^{4}$ then $n \leq 25$. Moreover, since $p-1=$ $2 \nu^{+}\left(T_{p, 2}\right)=-\sigma\left(T_{p, 2}\right)=-\sigma<0$ we have:
\begin{itemize}
\item[-] if $n=1$ then $\sigma \geq 0$ and we can ignore this possibility because $T_{p, 2}$ is a positive torus knot;
\item[-] if $n=4$ then $\sigma=-2$, that is $p=3$ and $S_{4}^{3}\left(T_{3,2}\right)=Y\left(2 ; \frac{3}{2}, 2,2\right)$ bounds a $\mathbb{Q} H B^{4}$ by Lemma 6.2;
\item[-] if $n=9$ then $p \in\{3,5\}$. The 3-manifold $S_{9}^{3}\left(T_{3,2}\right)=Y\left(2 ; \frac{3}{2}, 2, \frac{3}{2}\right)$ bounds a $\mathbb{Q} H B^{4}$ by [6] while $S_{9}^{3}\left(T_{5,2}\right)=-L(9,4)$ bounds a $\mathbb{Q} H B^{4}$ by [14];
\item[-] if $n=16$ then $p \in\{7,9\}$. By Lemma 6.2 both $S_{16}^{3}\left(T_{7,2}\right)$ and $S_{16}^{3}\left(T_{9,2}\right)$ are rational homology cobordant to $-L(4,1)$ and therefore each bounds a rational homology ball;
\item[-] if $n=25$ then $p=13$ and $S_{25}^{3}\left(T_{13,2}\right)=-L(25,4)$ which bounds a rational homology ball by [14].
\end{itemize}

Now assume that $k=1$. It is easy to see, via Lemma 6.5, that
$$S_{n}^{3}\left(T_{q+1, q}\right)=Y\left(2 ; \frac{q+1}{q}, q, \frac{q^{2}+q-n}{q^{2}+q-n-1}\right) .$$
If, in particular, $n=q^{2}$ we have $S_{q^{2}}^{3}\left(T_{q+1, q}\right)=Y\left(2 ; \frac{q+1}{q}, q, \frac{q}{q-1}\right)$. By Lemma 6.2 this manifold is $\mathbb{Q} H$-cobordant to $S^{3}$. Since $m\left(T_{q+1, q}\right)=q^{2}$, if $T_{q+1, q}$ has another integral surgery that bounds a $\mathbb{Q} H B^{4}$ then, by Theorem 1.2, this manifold is $S_{(q+1)^{2}}^{3}\left(T_{q+1, q}\right)$. We have
$$S_{(q+1)^{2}}^{3}\left(T_{q+1, q}\right)=Y\left(2 ; \frac{q+1}{q}, q, \frac{q+1}{q+2}\right)=Y\left(1 ; \frac{q+1}{q}, q, q+1\right)$$
which, again by Lemma 6.2, bounds a $\mathbb{Q} H B^{4}$.
From now on we may assume that $k>1$ and $q>2$. Write $p=k q \pm 1$ and assume that $S_{n}^{3}\left(T_{p, q}\right)$ bounds a $\mathbb{Q} H B^{4}$. We split the proof in two cases according to whether $p=k q+1$ or $p=k q-1$. Each case is further divided into subcases distinguishing the possible values for the surgery coefficient $n$.

First case: $p=k q+1$.
Note that $n \geq m\left(T_{k q+1, q}\right)=k q^{2}$. We distinguish the following three cases
\begin{itemize}
\item[(1)] $n>k q^{2}+q+1$;
\item[(2)] $k q^{2} \leq n<k q^{2}+q-1$;
\end{itemize}
$$n \in\left\{k q^{2}+q-1, k q^{2}+q, k q^{2}+q+1\right\} .$$

First subcase: $n>k q^{2}+q+1$. We claim that there are no candidate triples in this subcase. It is enough to show that:
$$n \leq k q^{2}+q+1 .$$

Note that inequality (11) implies that there is at most one value of $n$ such that the corresponding surgered manifold bounds a $\mathbb{Q} H B^{4}$. To see this we need to show that the interval $\left[k q^{2}, k q^{2}+q+1\right]$ contains at most one square. Suppose $N^{2}$ is the smallest square in $\left[k q^{2}, k q^{2}+q+1\right]$. We have
$$k q^{2} \leq N^{2} \Rightarrow q \leq \frac{N}{\sqrt{k}}$$
and therefore
$$k q^{2}+q+1 \leq N^{2}+\frac{N}{\sqrt{k}}+1<N^{2}+2 N+1=(N+1)^{2} .$$
To prove (11) we consider the positive canonical plumbing graph associated to $-S_{n}^{3}\left(T_{k q+1, q}\right)$ with $n>k q^{2}+q+1=p q+1$, which is easily seen to be positive definite. This plumbing graph is obtained by taking the dual of the graph described in Proposition 6.6, and it has the form
![](https://cdn.mathpix.com/cropped/72ba5561-4a2e-4e16-9100-e636a5a592d5-23.jpg?height=441&width=624&top_left_y=1582&top_left_x=750)

By removing the vertex whose weight is $q+1$ we obtain a disjoint union of two 2-chains. One of these 2-chains has length
$$(q-1)+1+\left(n-k q^{2}-q-1\right) \geq 4$$
since $q \geq 3$ and $n>k q^{2}+q+1$, and the other has length $k-1$. If $k \neq 4$, it follows by Lemma 6.7 that the above plumbing graph does not embed and therefore $S_{n}^{3}\left(T_{k q+1, q}\right)$
does not bound a $\mathbb{Q} H B^{4}$. If $k=4$ the plumbing graph has the form
![](https://cdn.mathpix.com/cropped/72ba5561-4a2e-4e16-9100-e636a5a592d5-24.jpg?height=438&width=621&top_left_y=380&top_left_x=750)

Consider the following portion of the above plumbing graph
![](https://cdn.mathpix.com/cropped/72ba5561-4a2e-4e16-9100-e636a5a592d5-24.jpg?height=79&width=510&top_left_y=961&top_left_x=806)
There are two choices for the embedding of the 2-chain. One choice requires four basis vectors and can be excluded (as in the proof of Lemma 6.7). The other choice gives us an embedding of the 2-chain of the form
$$e_{1}+e_{2}, e_{2}+e_{3}, e_{2}-e_{e_{1}} .$$
It is easy to see that there is no vector $v$ such that $v \cdot\left(e_{1}+e_{2}\right)=1$ and $v \cdot\left(e_{2}-e_{1}\right)=0$. This shows that $n \leq k q^{2}+q+1$ and inequality (11) follows.

Second subcase: $k q^{2} \leq n<k q^{2}+q-1$.
Suppose that $k=4$. We have
$$S_{4 q^{2}}^{3}\left(T_{4 q+1, q}\right)=Y\left(2 ; \frac{4 q+1}{4 q-3}, q, \frac{q}{q-1}\right)$$
By Lemma 6.2, applied to the two exceptional fibres with invariants $q$ and $\frac{q}{q-1}$, this manifold is $\mathbb{Q} H$-cobordant to a lens space obtained via the following plumbing graph
![](https://cdn.mathpix.com/cropped/72ba5561-4a2e-4e16-9100-e636a5a592d5-24.jpg?height=74&width=480&top_left_y=1849&top_left_x=821)
where $\left[a_{1}, \ldots, a_{n}\right]^{-}=\frac{4 q+1}{4 q-3}$. It is easy to see that this lens space is just $-L(4,1)$. It follows that $S_{4 q^{2}}^{3}\left(T_{4 q+1, q}\right)$ bounds a $\mathbb{Q} H B^{4}$ and, by (11) this is the only integral surgery on $T_{4 q+1, q}$ with this property.

Recall from Theorem 1.3 that $k<9$. Now we will examine each possible value of $k$ in the set \{2, 3, 5, 6, 7, 8\}. We have
$$S_{n}^{3}\left(T_{k q+1, q}\right)=Y\left(2 ; \frac{k q+1}{k q+1-k}, q, \frac{k q^{2}+q-n}{k q^{2}+q-n-1}\right)$$
and all the Seifert invariants are strictly greater than 1. It follows that the positive canonical plumbing graph for $S_{n}^{3}\left(T_{k q+1, q}\right)$ has the form
![](https://cdn.mathpix.com/cropped/72ba5561-4a2e-4e16-9100-e636a5a592d5-25.jpg?height=440&width=656&top_left_y=342&top_left_x=733)
where we have used Lemma 6.8, i.e. that $\frac{k q+1}{k q-1+k}=\left[2^{[q-1]}, k+1\right]^{-}$. In order to emphasise the 2 -chain in this plumbing graph we rewrite it as
![](https://cdn.mathpix.com/cropped/72ba5561-4a2e-4e16-9100-e636a5a592d5-25.jpg?height=340&width=1102&top_left_y=954&top_left_x=509)
Write $N=k q^{2}+2 q-n-1$ for the length of the 2-chain. Note that $N \geq 4$. The graph has $N+2$ vertices. If the corresponding integral lattice embeds in $\left(\mathbb{Z}^{N+2}, I\right)$ then we can write the vectors corresponding to the 2-chain as
$$e_{1}+e_{2}, \ldots, e_{k q^{2}+q-n-1}+e_{k q^{2}+q-n}, e_{k q^{2}+q-n}+e_{k q^{2}+q-n+1}, \ldots, e_{N}+e_{N+1} .$$
Let us call $v$ the vector whose weight is $k+1$. It can be written in one of the two following ways:
\begin{itemize}
\item[-] $v=\alpha e_{N+2}+\beta e_{N+1}+\gamma \sum_{i=1}^{N}(-1)^{i} e_{i}$, with $\gamma \neq 0$;
\item[-] $v=e_{N+1}+\sqrt{k} e_{N+2}$.
\end{itemize}
The second equality implies that $k$ is a square and can be excluded (since we already dealt with the values 1 and 4 and we know that $k<9$ ). Therefore the first equation holds. Since $v \cdot v=k+1$ we have
$$\alpha^{2}+\beta^{2}+N \gamma^{2}=k+1 \leq 9 .$$
Since $v \cdot\left(e_{N}+e_{N+1}\right)=1$ we see that $\beta+\gamma=1$. Then, we may write $k+1=$ $\alpha^{2}+\beta^{2}+N(1-\beta)^{2}$. Moreover, since $N \geq 4$, we obtain
$$\alpha^{2}+\beta^{2}+4(1-\beta)^{2} \leq \alpha^{2}+\beta^{2}+N(1-\beta)^{2} \leq 9$$
from which we get $(1-\beta)^{2} \leq 1$. Since $\gamma \neq 0$ and $\beta+\gamma=1$ we see that $\beta \neq 1$. We conclude that $(1-\beta)^{2}=1$, i.e. $\beta \in\{0,2\}$.

If $\beta=2$ we have
$$8 \leq \alpha^{2}+4+N \leq 9$$
Which implies $(\alpha, k) \in\{(0,7),(0,8),( \pm 1,8)\}$. Note that $N \geq q+1$. In the first case we quickly obtain $(p, q ; n)=(22,3 ; 64)$ and by [6] the corresponding surgered manifold
bounds a $\mathbb{Q} H B^{4}$. In the second case we have $n \in\{72,126\}$, and thus it is not a square. In the third case we get $n=73$ which is not a square.

If $\beta=0$ we have
$$\alpha^{2}+4 \leq \alpha^{2}+N \leq 9$$
In particular $|\alpha| \leq 2$. If $\alpha=0$ we have $N=k+1$ and $n=k q^{2}+2 q-k-2$. Notice that since $N \geq q+1$ and $k<9$ there are only finitely many possible values of $q$.

By listing all possibilities, we obtain the set of all candidate triples $(p, q ; n)$. The only one for which $n$ is a square is (21, 4; 64). The corresponding definite plumbing graph is positive definite:
![](https://cdn.mathpix.com/cropped/72ba5561-4a2e-4e16-9100-e636a5a592d5-26.jpg?height=369&width=623&top_left_y=751&top_left_x=749)
And the corresponding integral lattice does not embed, by direct inspection.
If $|\alpha|=1$ we have $4 \leq N=k \leq 9$. Just like in the previous case we can list all the candidate triples and discard the ones whose surgery coefficient is not a square. We are left with (43, 6; 256) which by [6] corresponds to a manifold which bounds a $\mathbb{Q} H B^{4}$.

If $|\alpha|=2$ we have $N \in\{4,5\}$ and $k=N+3$. In this case the only triple we get is (22, 3; 64), which, as already noted, bounds a $\mathbb{Q} H B^{4}$.