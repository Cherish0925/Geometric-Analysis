# The Fundamental Groups of Open Manifolds with Nonnegative Ricci Curvature

- Category: papers
- Identity: doi:10.3842/sigma.2020.078
- Content status: fulltext_ok

---

---
source_file: 2006_00745v2.pdf
converter: mathpix
format: mmd
---

\title{
The Fundamental Groups of Open Manifolds with Nonnegative Ricci Curvature
}

\author{
Jiayin PAN \\ Department of Mathematics, University of California-Santa Barbara, Santa Barbara CA 93106, USA \\ E-mail: j_pan@math.ucsb.edu \\ URL: http://web.math.ucsb.edu/~j_pan/
}

Received June 02, 2020, in final form August 04, 2020; Published online August 17, 2020
https://doi.org/10.3842/SIGMA.2020.078

\begin{abstract}
We survey the results on fundamental groups of open manifolds with nonnegative Ricci curvature. We also present some open questions on this topic.
\end{abstract}

Key words: Ricci curvature; fundamental groups
2020 Mathematics Subject Classification: 53C21; 53C23; 57S30

\section*{1 Introduction}

One fascinating topic in Riemannian geometry is the interplay between curvature and topology. Our primary interest in this survey is how nonnegative Ricci curvature determines the structure of fundamental groups of open (complete and non-compact) manifolds.

For comparison, we recall the topological implications of nonnegative sectional curvature for open manifolds. By Cheeger-Gromoll soul theorem [11], any open manifold $M$ of sec $\geq 0$ is homotopic to a closed totally geodesic submanifold in $M$. In particular, $M$ has finite topology. On the fundamental group level, the soul theorem implies that $\pi_{1}(M)$ is finitely generated and virtually abelian (contains an abelian subgroup of finite index). In contrast, an open manifold with Ric $\geq 0$ may have infinite second or higher Betti number, even when the manifold has Euclidean volume growth [3, 26, 36, 38, 39, 49, 50]; the reader may refer to Section 4 of [41] for a survey on the examples of manifolds with nonnegative Ricci curvature and infinite topology. Therefore, it is particularly interesting to see whether the structure of fundamental groups, finite generation and virtual abelianness, still holds for open manifolds with nonnegative Ricci curvature.

On finite generation, this is the longstanding Milnor conjecture raised in 1968.
Conjecture 1.1 (Milnor [27]). Let $M$ be an open $n$-manifold of Ric $\geq 0$. Then $\pi_{1}(M)$ is finitely generated.

The Milnor conjecture remains open.
On virtual abelianness, Wei constructed an open manifold of positive Ricci curvature whose fundamental group is not virtually abelian [47]. Later, Wilking showed that any finitely generated virtually nilpotent group can be realized the fundamental group of some open manifold of positive Ricci curvature [48]. On the other hand, by the work of Gromov and Milnor [20, 27], nonnegative Ricci curvature implies that any finitely generated subgroup of the fundamental group is virtually nilpotent. Kapovitch and Wilking proved a stronger result by dropping the finite generation condition and achieving a uniform bound on the index [23].

\footnotetext{
This paper is a contribution to the Special Issue on Scalar and Ricci Curvature in honor of Misha Gromov on his 75th Birthday. The full collection is available at https://www.emis.de/journals/SIGMA/Gromov.html
}

We summarize these results in the table below.

\begin{table}
\begin{tabular}[t]{|l|l|l|l|}
\hline \multicolumn{2}{|c|}{let $M$ be an open manifold of} & $\mathrm{sec} \geq 0$ & Ric $\geq 0$ \\
\hline \multirow{3}{*}{then $\pi_{1}(M)$ is} & finitely generated & true & unknown \\
\hline & virtually abelian & true & false \\
\hline & virtually nilpotent & true & true \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 1. Nonnegative curvature and fundamental groups.}
\end{table}

Given that proving or disproving the Milnor conjecture seems very difficult with the current understanding of nonnegative Ricci curvature, it is natural to ask the following question:

Question 1.2. For an open manifold of $\mathrm{Ric} \geq 0$, on what conditions is $\pi_{1}(M)$ finitely generated?
Though virtual abelianness does not hold for all open manifolds with nonnegative Ricci curvature, we can ask a similar question:

Question 1.3. For an open manifold of $\mathrm{Ric} \geq 0$, on what conditions is $\pi_{1}(M)$ virtually abelian?
In Section 2, we go through some basic tools in Ricci curvature and their applications to fundamental groups. This covers Bishop-Gromov relative volume comparison, Cheeger-Gromoll splitting theorem, and structure results on asymptotic cones. For applications on fundamental groups, we include the finiteness result by Anderson [2] and Li [24], Milnor's estimate on the growth function [27], and fundamental groups of closed manifolds with nonnegative Ricci curvature [10].

We survey results related the Milnor conjecture in Section 3. We describe Gromov's short generators [19], Kapovitch-Wilking's bound on the number of short generators [23], and Wilking's reduction on the Milnor conjecture [48]. Regarding answers to Question 1.2, we survey the work by Sormani on manifolds with small linear diameter growth [43], the classification by Liu in dimension 3 [25], and the recent progress by the author via asymptotic geometry [29, 30, 31].

In Section 4, we first describe the construction by Wei [47] and other related examples by Nabonnand [28] and Bérard-Bergery [4]. Then we present author's recent work on Question 1.3 [31, 32, 33].

We also post some further questions and conjectures in Sections 3 and 4.
We mention that there are also many beautiful results on the finite topology of open manifolds under additional geometric constraints like sectional curvature, conjugate radius, diameter growth, etc. We are unable to survey these results here due to the limited space.

\section*{2 Some basic tools in Ricci curvature}

We review some basic tools in Ricci curvature with a focus on the applications to fundamental groups of open manifolds with Ric $\geq 0$. Though some of the results in this section hold in a more general setting, we will only consider the case of nonnegative Ricci curvature.

Because the fundamental group acts isometrically on the Riemannian universal cover by path lifting, these tools are commonly applied to not only the manifold itself but also its universal cover when we study the fundamental group.

\subsection*{2.1 Volume comparison}

One of the basic tools is the Bishop-Gromov relative volume comparison.

Theorem 2.1 (Bishop-Gromov [5, 21]). Let $M$ be an open $n$-manifold of Ric $\geq 0$ and let $x \in M$. Then
$$\operatorname{vol}\left(B_{r}(x)\right) \leq \operatorname{vol}\left(B_{r}^{n}(0)\right), \quad \frac{\operatorname{vol}\left(B_{R}(x)\right)}{\operatorname{vol}\left(B_{r}(x)\right)} \leq \frac{\operatorname{vol}\left(B_{R}^{n}(0)\right)}{\operatorname{vol}\left(B_{r}^{n}(0)\right)}=\frac{R^{n}}{r^{n}}$$
for all $R>r>0$, where $B_{r}(x)$ is the metric $r$-ball centered at $x$ and $B_{r}^{n}(0)$ is the $r$-ball in the standard Euclidean space $\mathbb{R}^{n}$.

Theorem 2.1 implies that on an open manifold $M$ of Ric $\geq 0$, the limit
$$\lim _{r \rightarrow \infty} \frac{\operatorname{vol}\left(B_{r}(x)\right)}{\operatorname{vol}\left(B_{r}^{n}(0)\right)}=L$$
always exists with $L \in[0,1]$, where $x \in M$. Moreover, this limit does not depend on the choice of $x$. When $L>0$, we say that $M$ has Euclidean volume growth of constant $L$.

If $L$ equals the maximum value 1, then $M$ is isometric to the standard Euclidean space $\mathbb{R}^{n}$. When $M$ has almost max volume growth, that is, $L$ is sufficiently close to 1, there is a corresponding almost rigidity result: Perelman proved that such a manifold is contractible [35]; later Cheeger and Colding proved that it is diffeomorphic to $\mathbb{R}^{n}$ [6].

For $L>0$, Li and Anderson independently proved that $\pi_{1}(M)$ is finite.
Theorem 2.2 (Li [24], Anderson [2]). Let $M$ be an open $n$-manifold of Ric $\geq 0$. If $M$ has Euclidean volume growth of constant $L$, then $\pi_{1}(M)$ is finite with order at most $1 / L$.

In particular, if $L>1 / 2$, then $M$ is simply connected. Li's proof uses heat kernel on the universal cover. We briefly go through Anderson's proof, which utilizes the volume comparison and a method to calculate the volume via Dirichlet domain. As $\pi_{1}(M, x)$ acts freely, discretely, and isometrically on the Riemannian universal cover $\widetilde{M}$, we can construct the Dirichilet domain $D$ centered at $\tilde{x}$, where $\tilde{x} \in \widetilde{M}$ is a lift of $x . D$ is a fundamental domain; in particular, under $\pi_{1}(M, x)$-action, $\gamma \cdot\left(B_{r}(\tilde{x}) \cap D\right)$ and $\gamma^{\prime} \cdot\left(B_{r}(\tilde{x}) \cap D\right)$ are disjoint whenever $\gamma$ and $\gamma^{\prime}$ are different elements in $\pi_{1}(M, x)$. Also, $D$ satisfies $\operatorname{vol}\left(B_{r}(x)\right)=\operatorname{vol}\left(B_{r}(\tilde{x}) \cap D\right)$ for all $r>0$. To prove Theorem 2.2, we take a finite subset $S \subseteq \pi_{1}(M, x)$ and choose $d>0$ such that $d(\gamma \tilde{x}, \tilde{x}) \leq d$ for all $\gamma \in S$. Let
$$S(k)=\left\{\gamma \in \pi_{1}(M, x) \mid \gamma \text { can be expressed as a word in } S \text { with word length } \leq k\right\},$$
where $k \in \mathbb{N}$. Note that $d(\gamma \tilde{x}, \tilde{x}) \leq k d$ for all $\gamma \in S(k)$. For any $r>0$, we estimate the volume of $S(k) \cdot\left(B_{r}(\tilde{x}) \cap D\right)$ :
$$\# S(k) \cdot \operatorname{vol}\left(B_{r}(x)\right)=\# S(k) \cdot \operatorname{vol}\left(B_{r}(\tilde{x}) \cap D\right)=\operatorname{vol}\left(S(k) \cdot\left(B_{r}(\tilde{x}) \cap D\right)\right) \leq \operatorname{vol}\left(B_{r+k d}(\tilde{x})\right) .$$
It follows from volume comparison that
$$\# S(k) \leq \frac{\operatorname{vol}\left(B_{r+k d}(\tilde{x})\right)}{\operatorname{vol}\left(B_{r}(x)\right)} \leq \frac{\operatorname{vol}\left(B_{r+k d}^{n}(0)\right)}{\operatorname{vol}\left(B_{r}(x)\right)} .$$
Let $r \rightarrow \infty$, we see that
$$\# S(k) \leq \lim _{r \rightarrow \infty} \frac{\operatorname{vol}\left(B_{r+k d}^{n}(0)\right)}{\operatorname{vol}\left(B_{r}^{n}(0)\right)} \cdot \frac{\operatorname{vol}\left(B_{r}^{n}(0)\right)}{\operatorname{vol}\left(B_{r}(x)\right)}=\frac{1}{L} .$$
Since this estimate holds for any $k \in \mathbb{N}$ and any finite subset $S \subseteq \pi_{1}(M, x)$, Theorem 2.2 follows. This proof also indicates that if $M$ and $\widetilde{M}$ have the same volume growth rate, then $\pi_{1}(M)$ is finite as well.

Later, this finiteness result was extended to any manifold whose volume growth has order $n-\epsilon$ for some sufficiently small $\epsilon>0$.

Theorem 2.3 (Wu [51]). Given $n$, there exists a constant $\epsilon(n)>0$ such that the following holds.

Let $M$ be an open $n$-manifold of $\mathrm{Ric} \geq 0$. If there is $x \in M$ such that
$$\lim _{r \rightarrow \infty} \frac{\operatorname{vol}\left(B_{r}(x)\right)}{r^{n-\epsilon}(n)} \in(0, \infty),$$
then $\pi_{1}(M)$ is finite.
Also see Wan's work on finiteness under a relative volume growth condition [46], which implies Theorem 2.3. It is unknown whether the volume growth condition in Theorem 2.3 can be weakened to liminf or any $\epsilon \in(0,1)$.

When $\pi_{1}(M, x)$ is infinite, Milnor proved that the volume comparison provides an estimate on the growth function of any finitely generated subgroup, which in turn implies virtual nilpotency by Gromov's work.

Theorem 2.4. Let $M$ be a complete (open or closed) $n$-manifold of Ric $\geq 0$. Then any finitely generated subgroup of $\pi_{1}(M)$
\begin{itemize}
\item[(1)] has polynomial growth with degree at most $n$ (Milnor [27]),
\item[(2)] is virtually nilpotent (Gromov [20]).
\end{itemize}

We can derive Theorem 2.4(1) from Anderson's proof. Let $S$ be a generating set of the finitely generated subgroup. By taking $r=1$, then we can estimate $\# S(k)$ by
$$\# S(k) \leq \frac{\operatorname{vol}\left(B_{1+k d}^{n}(0)\right)}{\operatorname{vol}\left(B_{1}(x)\right)},$$
where the right hand side is a polynomial of $k$ with degree $n$.
Theorem 2.4(2) is useful to prove that certain fundamental group is virtually abelian under additional conditions: without lose of generality, we can start with a nilpotent one. It also follows from Theorem 2.4(2) that every finitely generated subgroup is finitely presented [52].

We end this section with Kapovitch-Wilking's result, which significantly improves Theorem 2.4(2).

Theorem 2.5 (Kapovitch-Wilking [23]). Given $n$, there exists a constant $C(n)$ such that the following holds.

Let $M$ be an open $n$-manifold of $\mathrm{Ric} \geq 0$. Then $\pi_{1}(M)$ contains a nilpotent subgroup $N$ of index at most $C(n)$. Moreover, any finitely generated subgroup of $N$ has nilpotency length at most $n$.

\subsection*{2.2 Splitting theorem}

A line is an isometric embedding $\gamma: \mathbb{R} \rightarrow M$; in other words,
$$d(\gamma(s), \gamma(t))=|s-t|$$
for all $s, t \in \mathbb{R}$. Cheeger-Gromoll splitting theorem is a fundamental tool in nonnegative Ricci curvature.

Theorem 2.6 (Cheeger-Gromoll [10]). Let $M$ be an open $n$-manifold of Ric $\geq 0$. If $M$ contains a line, then $M$ splits isometrically as a metric product $\mathbb{R} \times N$.

The splitting theorem implies the virtual abelianness of $\pi_{1}(M)$ when $M$ is closed and has nonnegative Ricci curvature.

Theorem 2.7 (Cheeger-Gromoll [10]). Let $M$ be a closed $n$-manifold of Ric $\geq 0$. Then $\pi_{1}(M)$ is virtually abelian.

In fact, as a consequence of Theorem 2.6, the universal cover of $M$ must split isometrically as $\mathbb{R}^{k} \times N$, where $N$ is a compact manifold. Consequently, its isometry group splits as well
$$\operatorname{Isom}(\widetilde{M})=\operatorname{Isom}\left(\mathbb{R}^{k}\right) \times \operatorname{Isom}(N),$$
where $\operatorname{Isom}(N)$ is a compact Lie group. Also, without lose of generality, we can assume that $\pi_{1}(M)$ is nilpotent by Theorem 2.4. Since we can view $\pi_{1}(M)$ as a subgroup of $\operatorname{Isom}(\widetilde{M})$, Theorem 2.7 follows from the algebraic fact that any nilpotent subgroup of $\operatorname{Isom}\left(\mathbb{R}^{k}\right) \times K$ is virtually abelian, where $K$ is a compact Lie group.

We mention that it was conjectured by Fukaya and Yamaguchi that the index of the abelian subgroup in Theorem 2.7 can be uniformly bounded by some constant $C(n)$ [18]. This conjecture is open even for nonnegative sectional curvature.

Theorem 2.7 has an analog for open manifolds. For each element $\gamma \in \pi_{1}(M, x)$, among all the loops based at $x$ representing $\gamma$, we can choose one of the minimal length. This loop is a geodesic loop and we call it a representing geodesic loop of $\gamma$.

Theorem 2.8. Let $M$ be an open $n$-manifold of $\mathrm{Ric} \geq 0$. If for some $x \in M$, all representing geodesic loops of elements in $\pi_{1}(M, x)$ are contained in a bounded set, then $\pi_{1}(M)$ is virtually abelian.

Though in this case, the universal cover may not be the metric product of $\mathbb{R}^{k}$ and a compact space, it can be shown that $\pi_{1}(M, x)$ is contained in $\operatorname{Isom}\left(\mathbb{R}^{k}\right) \times K$ for some compact Lie group $K$, which is sufficient for virtual abelianness (see Appendix A of [32] for a proof).

The assumption in Theorem 2.8 always holds when $\sec \geq 0$ by setting $x$ in a soul of $M$. This follows from Cheeger-Gromoll soul theorem and Sharafutdinov retraction [11, 40]. On the other hand, the assumption in Theorem 2.8 is very restricted for manifolds with nonnegative Ricci curvature. In fact, if $M$ has positive Ricci curvature and an infinite fundamental group, then it follows from the Cheeger-Gromoll splitting theorem that the representing geodesic loops $c_{\gamma}$ will always escape from any bounded sets as $\gamma$ exhausts $\pi_{1}(M, x)$ [45]. In Section 4.2, we will see the author's work [32, 33] generalizing Theorem 2.8.

\subsection*{2.3 Asymptotic geometry}

The Gromov-Hausdorff distance between two metric spaces measures how close they look alike. Using relative volume comparison Theorem 2.1, Gromov proved a precompactness result. This concept of convergence revolutionizes the Riemannian geometry.

Theorem 2.9 (Gromov [21]). Let $\left(M_{i}, x_{i}\right)$ be a sequence of complete $n$-manifolds of Ric $\geq$ $-(n-1)$, then after passing to a subsequence, it converges in the (pointed) Gromov-Hausdorff topology to a length metric space $(X, x)$.

The limit space $X$ is called a Ricci limit space. Cheeger, Colding, and Naber developed the fundamental theory on the structure of these Ricci limit spaces [6, 7, 8, 9, 12, 13, 14, 15].

In the context of an open manifold $M$ with Ric $\geq 0$, we can use Gromov-Hausdorff convergence to study its asymptotic geometry. For any sequence $r_{i} \rightarrow \infty$, passing to a subsequence if necessary, we obtain a convergent sequence
$$\left(r_{i}^{-1} M, x\right) \xrightarrow{\mathrm{GH}}(Y, y) .$$
The limit $(Y, y)$ is called an asymptotic cone of $M$, or a tangent cone of $M$ at infinity. It does not depend on the base point $x$, but it may depend on the scaling sequence $r_{i}$.

Cheeger and Colding substantially generalized the splitting theorem to Ricci limit spaces [6]. For convenience, we denote $\mathcal{M}(n, 0)$ the set of all Ricci limit spaces coming from sequences of complete $n$-manifolds of Ric $\geq 0$.

Theorem 2.10 (Cheeger-Colding [6]). Let $X \in \mathcal{M}(n, 0)$. If $X$ contains a line, then $X$ splits isometrically as a metric product $\mathbb{R} \times N$.

One important class of asymptotic cones is metric cones.
Theorem 2.11 (Cheeger-Colding [6]). Let $M$ be an open $n$-manifold of Ric $\geq 0$. Suppose that $M$ has Euclidean volume growth. Then any asymptotic cone $(Y, y)$ of $M$ is a metric cone with vertex $y$.

For a metric cone $C(Z) \in \mathcal{M}(n, 0), \operatorname{diam}(Z) \geq \pi$ is equivalent to $C(Z)$ containing a line. Then by Theorem 2.10, $C(Z)$ splits isometrically as $\mathbb{R}^{k} \times C\left(Z^{\prime}\right)$, where $\operatorname{diam}\left(Z^{\prime}\right)<\pi$.

Since we want to study $\pi_{1}(M, x)$, which acts on the universal cover $\widetilde{M}$ as isometries, it is natural to apply the asymptotic method to $\left(\widetilde{M}, \pi_{1}(M, x)\right)$ as well. This involves the equivariant Gromov-Hausdorff convergence, introduced by Fukaya and Yamaguchi [17, 18]. Let $r_{i} \rightarrow \infty$, after passing to a subsequence, we can obtain the diagram below:
![](https://cdn.mathpix.com/cropped/7068ed42-c92b-4cc9-a5ba-ef1621ef14ba-06.jpg?height=235&width=731&top_left_y=1045&top_left_x=389)
The $\pi_{1}(M, x)$-actions on $r_{i}^{-1} \widetilde{M}$ passes a limit $G$-action on $\widetilde{Y}$, where $G$ is some closed subgroup of $\operatorname{Isom}(\widetilde{Y})$. It follows from Theorem 2.12 below that $G$ is a Lie group.

Theorem 2.12 (Colding-Naber [15]). Let $X \in \mathcal{M}(n, 0)$. Then $\operatorname{Isom}(X)$ is a Lie group.
Theorem 2.12 was first proved for the non-collapsing case by Cheeger-Colding [8], then the general case by Colding-Naber [15].

If $X \in \mathcal{M}(n, 0)$ is a metric cone, then due to the splitting $X=\mathbb{R}^{k} \times C\left(Z^{\prime}\right)$, where $Z^{\prime}$ has diameter less than $\pi$, the isometry group of $X$ splits as well
$$\operatorname{Isom}(X)=\operatorname{Isom}\left(\mathbb{R}^{k}\right) \times \operatorname{Isom}\left(Z^{\prime}\right) .$$

\section*{3 Finite generation}

\subsection*{3.1 Gromov's short generators and their properties}

Gromov introduced a geometric method to choose generators of $\pi_{1}(M, x)$ successively [19]. We first choose $\gamma_{1} \in \pi_{1}(M, x)-\{e\}$ such that
$$d\left(\gamma_{1} \tilde{x}, \tilde{x}\right)=\min _{\gamma \in \pi_{1}(M, x)-\{e\}} d(\gamma \tilde{x}, \tilde{x}) .$$
Supposing that $\gamma_{k}$ is chosen for some $k \in \mathbb{N}$, we pick $\gamma_{k+1} \in \pi_{1}(M, x)-H_{k}$ such that
$$d\left(\gamma_{k+1} \tilde{x}, \tilde{x}\right)=\min _{\gamma \in \pi_{1}(M, x)-H_{k}} d(\gamma \tilde{x}, \tilde{x}),$$
where $H_{k}=\left\langle\gamma_{1}, \ldots, \gamma_{k}\right\rangle$ is the subgroup generated by first $k$ generators. It follows from the choice of these generators that
$$d\left(\gamma_{i} \tilde{x}, \gamma_{j} \tilde{x}\right) \geq \max \left\{d\left(\gamma_{i} \tilde{x}, \tilde{x}\right), d\left(\gamma_{j} \tilde{x}, \tilde{x}\right)\right\}$$
for all $i, j$. When $M$ has sec $\geq 0$, applying Toponogov comparison theorem to the geodesic triangle with vertices $\tilde{x}, \gamma_{i} \tilde{x}$, and $\gamma_{j} \tilde{x}$, one can see that $\theta_{i, j}$, the angle of this geodesic triangle at $\tilde{x}$, is at least $\pi / 3$. A standard packing argument then leads to Gromov's bound on the number of short generators.

Theorem 3.1 (Gromov [19]). Given $n$, there exists a constant $C(n)$ such that the following holds.

Let $M$ be an open $n$-manifold of $\sec \geq 0$ and let $x \in M$. Then the number of short generators of $\pi_{1}(M, x)$ is bounded by $C(n)$.

For Ricci curvature, Kapovitch and Wilking proved the following:
Theorem 3.2 (Kapovitch-Wilking [23]). Given $n$, there exists a constant $C(n)$ such that the following holds.

Let $M$ be an open $n$-manifold of $\operatorname{Ric} \geq 0$ and let $x \in M$. Let $\Gamma$ be a finitely generated subgroup of $\pi_{1}(M, x)$. Then there is a point $q \in B_{1}(x)$ such that the number of short generators of $\Gamma$ at $q$ is bounded by $C(n)$.

The statement proved by Kapovitch and Wilking is indeed local. Note that unlike Theorem 3.1, Theorem 3.2 gives a bound on the number of short generators at a point near $x$, not exactly at $x$. The proof of Theorem 3.2 is much more complicated than the sectional curvature case. It starts with a contradicting sequence
$$\left(M_{i}, x_{i}\right) \xrightarrow{\mathrm{GH}}(X, x)$$
so that the number of short generators at all points in $B_{1}\left(x_{i}\right)$ is larger than $i$. The proof involves an induction argument on the dimension of $X$ in the Colding-Naber sense and a successive blowup argument to increase the dimension of the limit space. In this process, one has to shift base points multiple times. Thus this method cannot bound the number of short generators at a priorly fixed reference point.

Note that if a bound $C(n)$ can be obtained at the base point $x$, then finite generation would follow directly by taking the first $C(n)+1$ many short generators to generate a subgroup. Also see the work by Rong and the author where a bound at the base point is achieved under certain conditions on $\pi_{1}(M, x)$-action [34]. On the other hand, Theorem 3.2 does immediately imply that any finitely generated subgroup of $\pi_{1}(M)$ can be generated by at most $C(n)$ many elements. However, this is far away from the Milnor conjecture. A typical example with this algebraic property is the set of rational numbers $\mathbb{Q}$ as an additive group: $\mathbb{Q}$ is not finitely generated, but every finitely generated subgroup is cyclic. An even simpler example is the cyclic dyadic rationals
$$\Gamma=\left\{\left.\frac{p}{2^{i}} \right\rvert\, p \in \mathbb{Z}, i \in \mathbb{N}\right\} .$$
A set of short generators of $\Gamma$ could potentially be $\gamma_{1}=1 / 2, \ldots, \gamma_{i}=1 /\left(2^{i}\right)$, etc. Ruling out these abelian groups as fundamental groups is crucial. In fact, with the help of Wilking's reduction, it is sufficient to consider abelian ones.

Theorem 3.3 (Wilking [48]). Let $M$ be an open $n$-manifold of $\mathrm{Ric} \geq 0$. If $\pi_{1}(M)$ is not finitely generated, then $\pi_{1}(M)$ has an abelian subgroup that is not finitely generated.

Another geometric property of short generators is about its representing geodesic loops. Let $c$ be a unit speed representing geodesic loop of a short generator $\gamma$ and let $r$ be the length of $c$, then by the choice of short generators, $c$ must be minimal up to its halfway, that is, $d(x, m)=r / 2$,
where $m=c(r / 2)$ is the midpoint of $c$. This implies that $m$ is a cut point of $x$; in particular, for $y \in M$ with $d(x, y)>r / 2$, we have
$$d(x, m)+d(y, m)-d(x, y)>0 .$$
Applying the Abresch-Gromoll inequality [1] to the universal cover, Sormani established a quantitative version of the above estimate [43]: for all $y \in M$ with $d(x, y) \geq r / 2+S(n) r$, we have
$$d(x, m)+d(y, m)-d(x, y) \geq 2 S(n) r,$$
where $S(n)>0$ is a small constant depending only on $n$. If $\pi_{1}(M, x)$ is not finitely generated, then $M$ has the above uniform cut estimate at a sequence of midpoints $m_{i}$ with $d\left(x, m_{i}\right) \rightarrow \infty$. With this, Sormani confirmed the Milnor conjecture when $M$ has small linear diameter growth.
Theorem 3.4 (Sormani [43]). Given $n$, there is a constant $S(n)>0$ such that the following holds.

Let $M$ be an open $n$-manifold of $\mathrm{Ric} \geq 0$. If $M$ has small linear diameter growth
$$\limsup _{r \rightarrow \infty} \frac{\operatorname{diam}\left(\partial B_{r}(x)\right)}{r} \leq S(n),$$
then $\pi_{1}(M)$ is finitely generated.
The diameter here is extrinsic so $\operatorname{diam}\left(\partial B_{r}(x)\right) \leq 2 r$ always holds. Theorem 3.4 also covers manifolds with linear volume growth [42], that is,
$$\limsup _{r \rightarrow \infty} \frac{\operatorname{vol}\left(B_{r}(x)\right)}{r}<\infty .$$

If $\pi_{1}(M, x)$ is not finitely generated, then we have a sequence of scales $r_{i}=d\left(\gamma_{i} \tilde{x}, \tilde{x}\right) \rightarrow \infty$, where $\left\{\gamma_{i}\right\}_{i}$ is a set of short generators. Using this sequence $r_{i}$, we can see the consequences of infinite generation through asymptotic geometry.
Proposition 3.5. Let $M$ be an open $n$-manifold of Ric $\geq 0$. Suppose that $\pi_{1}(M)$ is not finitely generated with a set of short generators $\left\{\gamma_{1}, \ldots, \gamma_{i}, \ldots\right\}$. Then in the diagram (2.1) with $r_{i}=$ $d\left(\gamma_{i} \tilde{x}, \tilde{x}\right) \rightarrow \infty$,
\begin{itemize}
\item[(1)] $Y$ is not polar at $y$ [43];
\item[(2)] the orbit $G \cdot \tilde{y}$ is not connected [30].
\end{itemize}
$Y$ being polar at $y$ means that for any $z \in Y-\{y\}$, there is a ray starting at $y$ going through $z$. Recall that short generators $\left\{\gamma_{1}, \ldots, \gamma_{i}, \ldots\right\}$ provides a sequence of representing geodesic loops based at $x$, on which the uniform cut estimate holds at the midpoint $m_{i}$. Passing this estimate to the asymptotic cone $Y$, we get a limit cut point in $Y$. This leads to (1) above. For (2), let $H_{i}$ be the subgroup of $\pi_{1}(M, x)$ that is generated by the first $i$ many short generators. Then we consider the convergence
$$\left(r_{i}^{-1} \widetilde{M}, \tilde{x}, H_{i}, \pi_{1}(M, x)\right) \xrightarrow{\mathrm{GH}}(\widetilde{Y}, \tilde{y}, H, G) .$$
The orbit $H \cdot \tilde{y}$ contains the connected component of $G \cdot \tilde{y}$ that includes $\tilde{y} \cdot \gamma_{i+1}$ converges to an element $\gamma_{\infty} \in G$ with $d\left(H \cdot \tilde{y}, \gamma_{\infty} \tilde{y}\right)=1$; in particular, $G \cdot \tilde{y}$ is not connected.

We mention that Sormani observed another way to see the consequence of infinite generation from afar by using the loop to infinity property [44]. An open manifold satisfies the loop to infinity property, if for any noncontractible loop $c$ and any compact subset $K$, there exists a loop in $M-K$ that is freely homotopic to $c$. This property gives a surjective inclusion map $i_{\star}: \pi_{1}(M-K, y) \rightarrow \pi_{1}(M, y)$, where $K$ is compact and $y \in M-K$. Sormani proved that for any open manifold $M$ of Ric $\geq 0$, either $M$ has the loop to infinity property or a double cover of $M$ splits off a line isometrically; in particular, manifolds of positive Ricci curvature always have this property. As a result, if there is an example $M$ with Ric $>0$ and an infinitely generated $\pi_{1}(M)$, then we can slide all these infinitely many generators to the end of $M$.

\subsection*{3.2 3-manifolds}

The Milnor conjecture is true in dimension 3. Schoen and Yau proved that any open 3-manifold of positive Ricci curvature is diffeomorphic to $\mathbb{R}^{3}$ [37]. Using Schoen-Yau's minimal surface theory and Perelman's solution to Poincaré conjecture, Liu classified open 3-manifold of nonnegative Ricci curvature [25]: either it is diffeomorphic to $\mathbb{R}^{3}$ or its universal cover splits off a line isometrically; in particular, this confirms the Milnor conjecture in dimension 3.

Theorem 3.6 (Liu [25]). The Milnor conjecture holds in dimension 3.
Later, the author gave an alternative proof of the finite generation of $\pi_{1}(M)$ by using asymptotic geometry and short generators [30]. Here we give an outline of the proof by the author. With Wilking's reduction and a topological result in dimension 3 by Evans and Moser [16], if $\pi_{1}(M)$ is not finitely generated, then without lose generality we can assume that it is a subgroup of $\mathbb{Q}$; in particular, $\pi_{1}(M)$ is torsion-free. This implies a geometric feature on the asymptotic cones: for any equivariant asymptotic cone $(\widetilde{Y}, \tilde{y}, G)$ of $(\widetilde{M}, \Gamma)$, the limit orbit $G \cdot y$ cannot be discrete.

Suppose that $\pi_{1}(M, x)$ is not finitely generated. Let $\left\{\gamma_{1}, \ldots, \gamma_{i}, \ldots\right\}$ be a set of short generators and let $r_{i}=d\left(\gamma_{i} \tilde{x}, \tilde{x}\right) \rightarrow \infty$. We consider the corresponding asymptotic cones as in the diagram (2.1). To derive a contradiction, the proof eliminates all the possibilities of asymptotic cones $\widetilde{Y}$ and $Y$ regarding their dimensions in the Colding-Naber sense [15], which are integers 1, 2 or 3.

Case 1. $\operatorname{dim}(\widetilde{Y})=3$. This case occurs if and only if $\widetilde{M}$ has Euclidean volume growth. Hence $\widetilde{Y}$ is a metric cone. If $\widetilde{Y}$ splits off an $\mathbb{R}^{2}$ or $\mathbb{R}^{3}$ factor, then Cheeger-Colding theory implies that $\widetilde{M}$ is isometric to $\mathbb{R}^{3}$ [7]. If $\widetilde{Y}$ splits off exactly one $\mathbb{R}$ factor, then the orbit $G \cdot \tilde{y}$ is contained in a line. It follows from Theorem 3.5(2) that the orbit must be discrete, which contradicts the non-discreteness that we derived from the reduction. If $\widetilde{Y}$ does not split off any line, then the orbit $G \cdot \tilde{y}$ must be the cone tip $\widetilde{y}$; a contradiction to both non-discreteness from the reduction and the non-connectedness from Theorem 3.5(2).

Case 2. $\operatorname{dim}(\widetilde{Y})=\operatorname{dim}(Y)=2$. Since $Y=\widetilde{Y} / G$, it is reasonable to believe that $G$ is a discrete group, thus the orbit $G \cdot y$ must be discrete as well. This again contradicts the nondiscreteness. Note that ruling out this case does not require that $Y$ and $\widetilde{Y}$ come from the scaling sequence $r_{i}$, the length of short generators.

Case 3. $\operatorname{dim}(Y)=1$. A Ricci limit space of dimension 1 is either a ray or a line [22]. Combined with Proposition 3.5(1), the $(Y, y)$ must be a ray with $y$ not being the starting point. By choosing a suitable rescaling $s_{i} \rightarrow \infty$, we can obtain a different asymptotic cone $Y^{\prime}$ with $\operatorname{dim}\left(Y^{\prime}\right) \geq 2$. Together with the results from cases 1 and 2, one can derive a contradiction as well.

\subsection*{3.3 Equivariant stability at infinity}

With the idea of investigating equivariant asymptotic cones, the author proved new partial results on the Milnor conjecture [29, 31]. These results are related to certain geometric stability condition on the universal cover at infinity and the question below:

Question 3.7. Does geometric stability at infinity implies equivariant stability at infinity?
To understand how Question 3.7 is related to the Milnor conjecture, we think of an example: the universal cover has a unique asymptotic cone as a standard Euclidean space $\mathbb{R}^{k}$ for some $k$. We have seen in Proposition 3.5(2) that if $\pi_{1}(M, x)$ is not finitely generated, then
$$\left(r_{i}^{-1} \widetilde{M}, \tilde{x}, \pi_{1}(M, x)\right) \xrightarrow{\mathrm{GH}}\left(\mathbb{R}^{k}, 0, G\right)$$
has a limit orbit $G \cdot 0$ that is not connected. If we change the scale $r_{i}$ to $s r_{i}$, where $s>0$, then the corresponding limit $\left(s^{-1} \mathbb{R}^{k}, 0, G\right)$ is not equivariantly isometric to $\left(\mathbb{R}^{k}, 0, G\right)$, because the distance between two components of $G \cdot 0$ is changed by a scale of $s^{-1}$. On the other hand, because we assumed that the asymptotic cone of $\widetilde{M}$ is independent of the scaling sequence, one may wonder whether the equivariant limit is independent of the scales as well. If this turns out to be true, then any equivariant asymptotic cone at infinity ought to have a connected orbit at the base point and finite generation would follow. Moreover, it can be shown that if $G$ is nilpotent and $\left(s \mathbb{R}^{k}, 0, G\right)$ are all equivariantly isometric to each other for all scales $s>0$, then the $G=\mathbb{R}^{l} \times K$, where $K$-action fixes 0 and the subgroup $\mathbb{R}^{l} \times\{e\}$ acts as translations. Hence one may expect that if $\widetilde{M}$ has a unique asymptotic cone as $\mathbb{R}^{k}$, then any equivariant asymptotic cone $\left(\mathbb{R}^{k}, 0, G\right)$ of $\left(\widetilde{M}, \pi_{1}(M)\right)$ should have a splitting structure $G=\mathbb{R}^{l} \times K$ as described above, where $\pi_{1}(M)$ is nilpotent.

The author studied Question 3.7 when the Riemannian universal cover satisfies one of the conditions below.
\begin{itemize}
\item[-] $\widetilde{M}$ is $k$-Euclidean at infinity, where $k$ is an integer. This means that any asymptotic cone of $\widetilde{M}$ is a metric cone that splits off exactly $\mathbb{R}^{k}$.
\item[-] $\widetilde{M}$ is $\left(C(X), \epsilon_{X}\right)$-stable at infinity, where $C(X) \in \mathcal{M}(n, 0)$ is a metric cone and $\epsilon_{X}$ is a constant only depending on the cross-section $X$. This means that any asymptotic cone of $\widetilde{M}$ is a metric cone, whose cross-section is $\epsilon_{X}$-close to $X$ with respect to Gromov-Hausdorff distance.
\end{itemize}

Theorem 3.8 ([29, 31]). Let $M$ be an open $n$-manifold of $\mathrm{Ric} \geq 0$. Suppose that one of the following conditions holds on the Riemannian universal cover $\widetilde{M}$ :
\begin{itemize}
\item[(1)] $\widetilde{M}$ is $k$-Euclidean at infinity for some $0 \leq k \leq n$; or
\item[(2)] $\widetilde{M}$ is $\left(C(X), \epsilon_{X}\right)$-stable at infinity for some metric cone $C(X) \in \mathcal{M}(n, 0)$ and a sufficiently small $\epsilon_{X}>0$.
\end{itemize}

Then $\pi_{1}(M)$ is finitely generated.
Both cases include the case that $M$ has nonnegative sectional curvature, with which $\widetilde{M}$ has a unique asymptotic cone as a metric cone. They also cover the case that $\widetilde{M}$ has Euclidean volume growth and a unique asymptotic cone. Another special case for (2) is when $\widetilde{M}$ has Euclidean volume growth of constant at least $1-\epsilon(n)$ for some small $\epsilon(n)>0$; in this case, due to Cheeger-Colding almost maximal volume rigidity [6], any asymptotic cone of $\widetilde{M}$ has a cross-section being Gromov-Hausdorff close to the unit $(n-1)$-dimensional sphere.

We view the condition in Theorem 3.8 as a geometric stability condition of $\widetilde{M}$ at infinity. As indicated, the key to proving finite generation is establishing corresponding equivariant stability at infinity. For simplicity, we only state the result of equivariant stability when $\widetilde{M}$ has a unique cone as a metric cone $C(Z)$ here.

Theorem 3.9. Let $M$ be an open $n$-manifold with Ric $\geq 0$ and a nilpotent fundamental group. Suppose that the universal cover $\widetilde{M}$ has a unique asymptotic cone as a metric cone $C(Z)$. Then there exist a closed nilpotent subgroup $K$ of $\operatorname{Isom}(Z)$ and an integer $l \in[0, n]$ such that any equivariant asymptotic cone $(\widetilde{Y}, \tilde{y}, G)$ of $\left(\widetilde{M}, \pi_{1}(M, x)\right)$ is $\left(C(Z), z, \mathbb{R}^{l} \times K\right)$, where $K$-action fixes $z$ and the subgroup $\mathbb{R}^{l} \times\{e\}$ acts as translations in the Euclidean factor of $C(Z)$.

To prove Theorem 3.9, it is essential to treat the set of all equivariant asymptotic cones of $\left(\widetilde{M}, \pi_{1}(M, x)\right)$, denoted as $\Omega\left(\widetilde{M}, \pi_{1}(M, x)\right)$, as a whole, not as individual spaces. It is known that $\Omega\left(\widetilde{M}, \pi_{1}(M, x)\right)$ is compact and connected in the pointed equivariant Gromov-Hausdorff topology. This fact serves as an intuition behind the proof.

The proof of Theorem 3.9 is a contradicting argument. Suppose that there are two different equivariant asymptotic cones $\left(C(Z), z, G_{1}\right)$ and $\left(C(Z), z, G_{2}\right)$. Using the connectedness of $\Omega\left(\widetilde{M}, \pi_{1}(M, x)\right)$, we can find a chain of spaces in $\Omega\left(\widetilde{M}, \pi_{1}(M, x)\right)$ connecting $\left(C(Z), z, G_{1}\right)$ and $\left(C(Z), z, G_{2}\right)$, such that the adjacent spaces in the chain are very close in the equivariant Gromov-Hausdorff topology. Roughly speaking, we find a contradiction somewhere in the chain. The author developed two technical tools to achieve this. One is a critical rescaling argument. We view $\left(C(Z), z, G_{1}\right)$ and $\left(C(Z), z, G_{2}\right)$ as the limits coming from two different scales
$$\left(r_{i}^{-1} \widetilde{M}, \tilde{x}, \pi_{1}(M, x)\right) \xrightarrow{\mathrm{GH}}\left(C(Z), z, G_{1}\right), \quad\left(s_{i}^{-1} \widetilde{M}, \tilde{x}, \pi_{1}(M, x)\right) \xrightarrow{\mathrm{GH}}\left(C(Z), z, G_{2}\right) .$$
Adjusting the scales, we can assume that one is the rescaling of the other by some $t_{i} \rightarrow \infty$. The critical rescaling argument chooses a suitable intermediate scaling sequence $l_{i} \rightarrow \infty$ with $l_{i} \leq t_{i}$ and looks for a contradiction in the corresponding limit coming from $l_{i}$. This argument helps reduce the problem to a compact one regarding isometric actions on the cross-section $Z$. The other tool is an equivariant Gromov-Hausdorff distance gap between isometric actions on $Z$. To describe this, we think of a chain of spaces $\left\{\left(Z, H_{j}\right)\right\}_{j=1}^{m}$, where each $H_{j}$ is a closed subgroup of $\operatorname{Isom}(Z)$. The equivariant Gromov-Hausdorff distance gap implies that if the distance between adjacent spaces is sufficiently small along the chain, then all $\left(Z, H_{j}\right)$ have to be the same space. Theorem 2.12 is crucial in establishing such a distance gap.

Based on [29, 31], we ask the following question on open manifolds whose Riemannian universal covers have Euclidean volume growth.

Question 3.10. When the Riemannian universal cover $\widetilde{M}$ has Euclidean volume growth, is there any equivariant stability among all equivariant asymptotic cones of $\left(\widetilde{M}, \pi_{1}(M, x)\right)$ ?

One may think of the Euclidean volume growth condition as certain geometric stability condition at infinity as well, but a very weak one: we only know that all asymptotic cones are metric cones whose cross sections share the same $(n-1)$-dimensional Hausdorff volume. An affirmative answer to Question 3.10 would imply the finite generation for this class of manifolds.

\section*{4 Virtual abelianness}

\subsection*{4.1 Wei's construction and related examples}

Wei first constructed an open manifold of positive Ricci curvature whose fundamental group is not virtually abelian, as a torsion-free nilpotent group [47]. Based on this construction, later Wilking showed that any finitely generated virtually nilpotent group can be realized as the fundamental group of some open manifold with positive Ricci curvature [48]. We briefly describe Wei's construction and other related examples.

Let $\left(S^{p-1}, d s^{2}\right)$ be the unit $(p-1)$-dimensional sphere and let $\left(N, g_{0}\right)$ be a closed manifold. A doubly warped product $[0, \infty) \times_{f} S^{p-1} \times_{h} N$ has the metric
$$g=d r^{2}+f(r)^{2} d s^{2}+h(r)^{2} g_{0},$$
It is diffeomorphic to $\mathbb{R}^{p} \times N$ if the warping functions $f$ and $h$ are smooth and satisfy
$$f(0)=0, \quad f^{\prime}(0)=1, \quad f^{\prime \prime}(0)=0, \quad h(0)>0, \quad h^{\prime}(0)=0$$
and $f(r)>0, h(r)>0$ for all $r>0$.
Nabonnand constructed a doubly warped product $[0, \infty) \times_{f} S^{2} \times_{h} S^{1}$ of positive Ricci curvature [28]. Later, Bergery generalized this method to a doubly warped product $M=[0, \infty) \times_{f}$ $S^{p-1} \times_{h} N$ of positive Ricci curvature, where $N$ is any closed manifold with nonnegative Ricci
curvature [4]. Note that $\pi_{1}(M)=\pi_{1}(N)$ is always virtually abelian. In this construction, warping function $h(r)$ can be adjusted so that $h(r) \rightarrow 0$ or $h(r) \rightarrow c>0$ as $r \rightarrow \infty$.

We illustrate Wei's example. Let $\widetilde{N}$ be a simply connected nilpotent Lie group and let $\Gamma$ be a lattice in $\widetilde{N}$. When $\widetilde{N}$ has nilpotency length $\geq 2, \Gamma$ is not virtually abelian and thus the compact quotient manifold $N=\widetilde{N} / \Gamma$ does not admit a metric of nonnegative Ricci curvature. However, $N$ admits a family of metrics $g_{r}$ with almost nonnegative sectional curvature. Wei constructed a warped product $M=[0, \infty) \times_{f} S^{p-1} \times N_{r}$ of positive Ricci curvature with the metric
$$g=d r^{2}+f(r)^{2} d s^{2}+g_{r}$$
This metric is not a doubly warped product in the usual sense since the metric $g_{r}$ decays at different rates for different steps of $N$. Note that $\pi_{1}(M)=\pi_{1}(N)$ is not virtually abelian. In Wei's construction, $\operatorname{diam}\left(N, g_{r}\right)$ has polynomial decay as $r \rightarrow \infty$.

We mention that one can construct a doubly warped product $[0, \infty) \times_{f} S^{p-1} \times_{g} S^{1}$ with positive Ricci curvature and a logarithm decaying $h(r)$ (see Appendix B of [32]). However, unlike Wei's construction, it is impossible to use logarithm decaying functions to warp a nilpotent manifold $M=[0, \infty) \times_{f} S^{p-1} \times N_{r}$ while keeping positive Ricci curvature. We will see the reason in the next section.

\subsection*{4.2 Escape rate}

In the light of Theorem 2.8, we see that the virtual abelianness is related to where the representing geodesic loops of $\pi_{1}(M, x)$ are positioned. We also mentioned in Section 2.2 that the escape phenomenon is prevalent for nonnegative Ricci curvature. Motivated by these, the author introduced the escape rate to quantify this phenomenon by comparing the size of representing geodesic loops to their length [32].

Definition 4.1. Let $(M, x)$ be an open manifold with an infinite fundamental group. We define the escape rate of $(M, x)$, a scaling invariant, as
$$E(M, x)=\limsup _{|\gamma| \rightarrow \infty} \frac{d_{\mathrm{H}}\left(x, c_{\gamma}\right)}{|\gamma|},$$
where $\gamma \in \pi_{1}(M, x),|\gamma|=\operatorname{length}\left(c_{\gamma}\right)$, and $d_{\mathrm{H}}$ is the Hausdorff distance.
As a loop based at $x$, its size $d_{\mathrm{H}}\left(x, c_{\gamma}\right)$ is at most half of its length. Hence $E(M, x)$ always ranges from 0 to 1/2. When all representing geodesic loops stay inside a bounded set or escape at a sublinear rate compared to their length, we have $E(M, x)=0$.

Regarding examples as warped products $[0, \infty) \times_{f} S^{p-1} \times_{h} N$, their escape rates are determined by the warping function $h(r)$. As $\operatorname{diam}\left(N_{r}\right)$ decreases to 0, the representing geodesic loop will take advantage of the thin end to shorten its length, which will in turn enlarge its size. In other words, one should expect that the faster $\operatorname{diam}\left(N_{r}\right)$ decays, the larger the escape rate is. In fact, if $h(r)$ has polynomial decay, as in Wei's construction, then $E(M, x)$ is positive; if $h(r)$ has logarithm decay or converges to a positive constant, then $E(M, x)=0$.

It turns out that this simple geometric quantity can measure the structure of fundamental group. First recall that if $\pi_{1}(M, x)$ is not finitely generated, then we have infinitely many short generators whose representing geodesic loops are minimal up to halfway. This shows that $E(M, x)=1 / 2$ if $\pi_{1}(M)$ is not finitely generated. The author proved that zero escape rate implies virtual abelianness, which substantially generalizes Theorem 2.8.

Theorem 4.2 ([32]). Let $(M, x)$ be an open $n$-manifold of Ric $\geq 0$. If $E(M, x)=0$, then $\pi_{1}(M, x)$ is virtually abelian.

We outline the proof of Theorem 4.2, which goes through the asymptotic geometry. A crucial step is showing that the following statements are equivalent:
\begin{itemize}
\item[(1)] $E(M, x)=0$;
\item[(2)] in any equivariant asymptotic cone $(\widetilde{Y}, \tilde{y}, G)$ of $\left(\widetilde{M}, \pi_{1}(M, x)\right)$, the orbit $G \cdot \tilde{y}$ is geodesic in $\widetilde{Y}$, that is, its intrinsic and extrinsic metric agree;
\item[(3)] in any equivariant asymptotic cone $(\widetilde{Y}, \tilde{y}, G)$ of $\left(\widetilde{M}, \pi_{1}(M, x)\right)$, the orbit $G \cdot \tilde{y}$ is geodesic in $\widetilde{Y}$ and is isometric to a standard Euclidean space.
\end{itemize}

The proof of (2) ⇒ (3) relies on the Cheeger-Colding splitting theorem and a critical rescaling argument, which is the type of argument we mentioned before in Section 3.3 when explaining Theorem 3.9. The details are distinct from the proof of Theorem 3.9 due to different contexts.

To derive virtual abelianness from (3), we take a nilpotent subgroup $N$ in $\pi_{1}(M, x)$ of finite index. For any $r_{i} \rightarrow \infty$, we consider
$$\left(r_{i}^{-1} \widetilde{M}, \tilde{x}, N, \pi_{1}(M, x)\right) \xrightarrow{\mathrm{GH}}(\widetilde{Y}, \tilde{y}, H, G) .$$
It can be shown that $H$ acts on $G \cdot \tilde{y}=H \cdot \tilde{y}=\mathbb{R}^{k}$ by translations. This limiting behavior restricts $N$-action at large scale on $\widetilde{M}$ : they acts as almost translations in the sense that $d\left(\gamma^{2} \tilde{x}, \tilde{x}\right)$ is close to twice of $d(\gamma \tilde{x}, \tilde{x})$ when $\gamma$ has large displacement at $\tilde{x}$. It was observed in [31] that this feature implies virtual abelianness.

We explain why the Heisenberg 3-group $H^{3}$ cannot act this way isometrically. For convenience, we write $|\gamma|=d(\gamma \tilde{x}, \tilde{x})$. The commutator calculus in $H^{3}$ has $\left[g^{k}, h\right]=[g, h]^{k}=\left[g, h^{k}\right]$ for all $g, h \in H^{3}$ and $k \in \mathbb{N}$. Now let $g, h \in H^{3}$ with $[g, h] \neq e$. We choose a large integer $k$ such that $R \leq\left|[g, h]^{\left(k^{2}\right)}\right|=\left|\left[g^{k}, h^{k}\right]\right|$. We set $\alpha=g^{k}$ and $\beta=h^{k}$, then continue to raise the power. For any integer $p$ and $l=2^{p}$, we have
$$\left|[\alpha, \beta]^{\left(l^{2}\right)}\right|=\left|\left[\alpha^{l}, \beta^{l}\right]\right| \leq 2 \cdot 2^{p}(|\alpha|+|\beta|) .$$
On the other hand, the almost translation at large scale condition implies that
$$\left|[\alpha, \beta]^{\left(l^{2}\right)}\right| \geq(1.9)^{2 p}|[\alpha, \beta]| .$$
This leads to a contradiction when $p$ is sufficiently large.
For manifolds in Theorem 3.8, as a consequence of their equivariant stability at infinity, they have zero escape rate [32]. We can further bound the index of the abelian subgroup if in addition the universal cover has Euclidean volume growth.

Theorem 4.3 ([31]). Let $M$ be an open $n$-manifold of Ric $\geq 0$. Suppose that one of the following conditions holds on the Riemannian universal cover $\widetilde{M}$ :
\begin{itemize}
\item[(1)] $\widetilde{M}$ is $k$-Euclidean at infinity for some $0 \leq k \leq n$; or
\item[(2)] $\widetilde{M}$ is $\left(C(X), \epsilon_{X}\right)$-stable at infinity for some metric cone $C(X) \in \mathcal{M}(n, 0)$ and a sufficiently small $\epsilon_{X}>0$.
\end{itemize}
Then $\pi_{1}(M)$ is virtually abelian. If in addition $\widetilde{M}$ has Euclidean volume growth of constant at least $L>0$, then the index can be bounded by some constant $C(n, L)$.

For manifolds whose universal covers have Euclidean volume growth, if one can answer Question 3.10 affirmatively, then that would confirm $E(M, x)=0$ and the conjecture below.

Conjecture 4.4. Given $n$ and $L \in(0,1]$, there exists a constant $C(n, L)$ such that the following holds.

Let $M$ be an open $n$-manifold of Ric $\geq 0$. If the Riemannian universal cover of $M$ has Euclidean volume growth of constant at least $L$, then $\pi_{1}(M)$ is finitely generated and contains an abelian subgroup of index at most $C(n, L)$.

As mentioned in Section 3.3, the case $L$ being close to 1 is indeed included in Theorems 3.8(2) and 4.3(2).

Theorem 4.2 is further generalized to an escape rate gap by the author.
Theorem 4.5 ([33]). Given $n$, there exists a constant $\epsilon(n)>0$ such that the following holds.
Let $(M, x)$ be an open $n$-manifold of Ric $\geq 0$. If $E(M, x) \leq \epsilon(n)$, then $\pi_{1}(M, x)$ is virtually abelian.

To end this section, we pose the question whether escape rate can detect nilpotent groups of different steps.

Question 4.6. For each $n$, are there positive constants $\epsilon(n, k)$ strictly increasing in $k$ such that the following holds?

For any open $n$-manifold ( $M, x$ ) of Ric $\geq 0$, if $E(M, x) \leq \epsilon(n, k)$, then $\pi_{1}(M)$ contains a free nilpotent subgroup of nilpotency length at most $k$ with finite index.

\section*{Acknowledgements}

The author is partially supported by AMS Simons travel grant. The author would like to thank Guofang Wei and Christina Sormani for their encouragement and suggestions when preparing this survey.

\section*{References}
\begin{itemize}
\item[] [1] Abresch U., Gromoll D., On complete manifolds with nonnegative Ricci curvature, J. Amer. Math. Soc. 3 (1990), 355-374.
\item[] [2] Anderson M.T., On the topology of complete manifolds of nonnegative Ricci curvature, Topology 29 (1990), 41-55.
\item[] [3] Anderson M.T., Kronheimer P.B., LeBrun C., Complete Ricci-flat Kähler manifolds of infinite topological type, Comm. Math. Phys. 125 (1989), 637-642.
\item[] [4] Bérard-Bergery L., Quelques exemples de variétés riemanniennes complètes non compactes à courbure de Ricci positive, C. R. Acad. Sci. Paris Sér. I Math. 302 (1986), 159-161.
\item[] [5] Bishop R.L., A relation between volume, mean curvature and diameter, Amer. Math. Soc. Not. 10 (1963), 364-364.
\item[] [6] Cheeger J., Colding T.H., Lower bounds on Ricci curvature and the almost rigidity of warped products, Ann. of Math. 144 (1996), 189-237.
\item[] [7] Cheeger J., Colding T.H., On the structure of spaces with Ricci curvature bounded below. I, J. Differential Geom. 46 (1997), 406-480.
\item[] [8] Cheeger J., Colding T.H., On the structure of spaces with Ricci curvature bounded below. II, J. Differential Geom. 54 (2000), 13-35.
\item[] [9] Cheeger J., Colding T.H., On the structure of spaces with Ricci curvature bounded below. III, J. Differential Geom. 54 (2000), 37-74.
\item[] [10] Cheeger J., Gromoll D., The splitting theorem for manifolds of nonnegative Ricci curvature, J. Differential Geometry 6 (1971), 119-128.
\item[] [11] Cheeger J., Gromoll D., On the structure of complete manifolds of nonnegative curvature, Ann. of Math. 96 (1972), 413-443.
\end{itemize}
\begin{itemize}
\item[] [12] Cheeger J., Naber A., Lower bounds on Ricci curvature and quantitative behavior of singular sets, Invent. Math. 191 (2013), 321-339, arXiv:1103.1819.
\item[] [13] Cheeger J., Naber A., Regularity of Einstein manifolds and the codimension 4 conjecture, Ann. of Math. 182 (2015), 1093-1165, arXiv:1406.6534.
\item[] [14] Colding T.H., Ricci curvature and volume convergence, Ann. of Math. 145 (1997), 477-501.
\item[] [15] Colding T.H., Naber A., Sharp Hölder continuity of tangent cones for spaces with a lower Ricci curvature bound and applications, Ann. of Math. 176 (2012), 1173-1229, arXiv:1102.5003.
\item[] [16] Evans B., Moser L., Solvable fundamental groups of compact 3-manifolds, Trans. Amer. Math. Soc. 168 (1972), 189-210.
\item[] [17] Fukaya K., Theory of convergence for Riemannian orbifolds, Japan. J. Math. (N.S.) 12 (1986), 121-160.
\item[] [18] Fukaya K., Yamaguchi T., The fundamental groups of almost non-negatively curved manifolds, Ann. of Math. 136 (1992), 253-333.
\item[] [19] Gromov M., Almost flat manifolds, J. Differential Geometry 13 (1978), 231-241.
\item[] [20] Gromov M., Groups of polynomial growth and expanding maps, Inst. Hautes Études Sci. Publ. Math. (1981), 53-73.
\item[] [21] Gromov M., Metric structures for Riemannian and non-Riemannian spaces, Modern Birkhäuser Classics, Birkhäuser Boston, Inc., Boston, MA, 2007.
\item[] [22] Honda S., On low-dimensional Ricci limit spaces, Nagoya Math. J. 209 (2013), 1-22.
\item[] [23] Kapovitch V., Wilking B., Structure of fundamental groups of manifolds of Ricci curvature bounded below, arXiv:1105.5955.
\item[] [24] Li P., Large time behavior of the heat equation on complete manifolds with nonnegative Ricci curvature, Ann. of Math. 124 (1986), 1-21.
\item[] [25] Liu G., 3-manifolds with nonnegative Ricci curvature, Invent. Math. 193 (2013), 367-375, arXiv:1108.1888.
\item[] [26] Menguy X., Noncollapsing examples with positive Ricci curvature and infinite topological type, Geom. Funct. Anal. 10 (2000), 600-627.
\item[] [27] Milnor J., A note on curvature and fundamental group, J. Differential Geometry 2 (1968), 1-7.
\item[] [28] Nabonnand P., Sur les variétés riemanniennes complètes à courbure de Ricci positive, C. R. Acad. Sci. Paris Sér. A-B 291 (1980), A591-A593.
\item[] [29] Pan J., Nonnegative Ricci curvature, stability at infinity and finite generation of fundamental groups, Geom. Topol. 23 (2019), 3203-3231, arXiv:1710.05498.
\item[] [30] Pan J., A proof of Milnor conjecture in dimension 3, J. Reine Angew. Math. 758 (2020), 253-260, arXiv:1703.08143.
\item[] [31] Pan J., Nonnegative Ricci curvature, almost stability at infinity, and structure of fundamental groups, arXiv:1809.10220.
\item[] [32] Pan J., On the escape rate of geodesic loops in an open manifold with nonnegative Ricci curvature, Geom. Topol., to appear, arXiv:2003.01326.
\item[] [33] Pan J., Nonnegative Ricci curvature and escape rate gap, in preparation.
\item[] [34] Pan J., Rong X., Ricci curvature and isometric actions with scaling nonvanishing property, arXiv:1808.02329.
\item[] [35] Perelman G., Manifolds of positive Ricci curvature with almost maximal volume, J. Amer. Math. Soc. 7 (1994), 299-305.
\item[] [36] Perelman G., Construction of manifolds of positive Ricci curvature with big volume and large Betti numbers, in Comparison Geometry (Berkeley, CA, 1993-94), Math. Sci. Res. Inst. Publ., Vol. 30, Cambridge University Press, Cambridge, 1997, 157-163.
\item[] [37] Schoen R., Yau S.T., Complete three-dimensional manifolds with positive Ricci curvature and scalar curvature, in Seminar on Differential Geometry, Ann. of Math. Stud., Vol. 102, Princeton University Press, Princeton, N.J., 1982, 209-228.
\item[] [38] Sha J.-P., Yang D., Examples of manifolds of positive Ricci curvature, J. Differential Geometry 29 (1989), 95-103.
\item[] [39] Sha J.P., Yang D., Positive Ricci curvature on the connected sums of $S^{n} \times S^{m}$, J. Differential Geom. 33 (1991), 127-137.
\item[] [40] Sharafutdinov V.A., Convex sets in a manifold of nonnegative curvature, Math. Notes 26 (1979), 556-560.
\end{itemize}
[41] Shen Z., Sormani C., The topology of open manifolds with nonnegative Ricci curvature, Commun. Math. Anal. (2008), 20-34, arXiv:math.DG/0606774.
[42] Sormani C., The almost rigidity of manifolds with lower bounds on Ricci curvature and minimal volume growth, Comm. Anal. Geom. 8 (2000), 159-212, arXiv:math.DG/9903171.
[43] Sormani C., Nonnegative Ricci curvature, small linear diameter growth and finite generation of fundamental groups, J. Differential Geom. 54 (2000), 547-559, arXiv:math.DG/9809133.
[44] Sormani C., On loops representing elements of the fundamental group of a complete manifold with nonnegative Ricci curvature, Indiana Univ. Math. J. 50 (2001), 1867-1883, arXiv:math.DG/9904096.
[45] Sormani C., Wei G., Various covering spectra for complete metric spaces, Asian J. Math. 19 (2015), 171-202, arXiv:1211.7123.
[46] Wan J., On the fundamental group of complete manifolds with almost Euclidean volume growth, Proc. Amer. Math. Soc. 147 (2019), 4493-4498, arXiv:1902.05292.
[47] Wei G., Examples of complete manifolds of positive Ricci curvature with nilpotent isometry groups, Bull. Amer. Math. Soc. (N.S.) 19 (1988), 311-313.
[48] Wilking B., On fundamental groups of manifolds of nonnegative curvature, Differential Geom. Appl. 13 (2000), 129-165.
[49] Wraith D., Surgery on Ricci positive manifolds, J. Reine Angew. Math. 501 (1998), 99-113.
[50] Wraith D., New connected sums with positive Ricci curvature, Ann. Global Anal. Geom. 32 (2007), 343-360.
[51] Wu B.Y., On the fundamental group of Riemannian manifolds with nonnegative Ricci curvature, Geom. Dedicata 162 (2013), 337-344.
[52] Wylie W.C., Noncompact manifolds with nonnegative Ricci curvature, J. Geom. Anal. 16 (2006), 535-550, arXiv:math.DG/0510139.
