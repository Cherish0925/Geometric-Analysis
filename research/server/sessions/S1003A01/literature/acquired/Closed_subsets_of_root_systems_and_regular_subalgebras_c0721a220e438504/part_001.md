---
retention_scope: session
part: 1
total_parts: 3
---

[Part 1/3 of: Closed subsets of root systems and regular subalgebras]

---
source_file: Closed_subsets_of_root_systems_and_regular_subalgebras_88a71b5c4271.pdf
converter: mathpix
format: mmd
---

\title{
CLOSED SUBSETS OF ROOT SYSTEMS AND REGULAR SUBALGEBRAS
}

\author{
ANDREW DOUGLAS ${ }^{1,2}$ AND WILLEM A. DE GRAAF ${ }^{3}$
}

\begin{abstract}
We describe an algorithm for classifying the closed subsets of a root system, up to conjugation by the associated Weyl group. Such a classification for an irreducible root system is closely related to the classification of the regular subalgebras, up to inner automorphism, of the corresponding simple Lie algebra. We implement our algorithm to classify the closed subsets of the irreducible root systems of ranks 3 through 7. We present a complete description of the classification for the closed subsets of the rank 3 irreducible root system. We employ this root system classification to classify all regular subalgebras of the rank 3 simple Lie algebras. We present only summary data for the classifications in higher ranks due to the large size of these classifications. Our algorithm is implemented in the language of the computer algebra system GAP.
\end{abstract}

\section*{1. Introduction}

Closed subsets of root systems appear in a number of contexts. They are integral to the classification of regular semisimple subalgebras of the exceptional Lie algebras [Dyn52, [dGr09, LG72]. Closed subsets of root systems also find application to classifications of the reflection subgroups of finite and affine Weyl groups [DL11]. They appear in the theory of Chevalley groups [HV96]. And, the problem of decomposing a root system into a union of two closed subsets has aided in the classification of complex homogeneous spaces [Mal80].

The problem of classifying all closed subsets of root systems is an unsolved problem, but incomplete results exist. We mention three examples. Borevich [Bor77] determined the number of topologies of a set of $n$ elements for $n \leq 8$. Because topologies on a set of size $n$ correspond to closed sets in the root system of type $A_{n-1}$ (see Section 2.1), he therefore also determined the number of closed sets in the root systems $A_{l}$ for $l \leq 7$. Subsequently this has been taken further by other authors, see [BM02] for relatively recent work in this direction. Furthermore, in [DCH94] a classification of the invertible closed subsets of a root system was given. Thirdly, the work of Dynkin Dyn52 contains an algorithm to classify the root subsystems of a root system, up to the action by the Weyl group.

In this article, we describe an algorithm for classifying the closed subsets of a root system, up to conjugation by the associated Weyl group. Such a classification for an irreducible root system is closely related to the classification of the regular subalgebras,

\footnotetext{
${ }^{1}$ Mathematics and Physics Programs, The Graduate Center, City University of New York, USA
${ }^{2}$ Department of Mathematics, New York City College of Technology, City University of New York, USA
${ }^{3}$ Department of Mathematics, University of Trento, Povo (Trento), Italy
E-mail addresses: adouglas2@gc.cuny.edu, degraaf@science.unitn.it.
Date: March 15, 2019.
2010 Mathematics Subject Classification. 17B05, 17B10, 17B20, 17B30, 17B37.
Key words and phrases. Root systems, closed subsets of root systems, regular subalgebras.
}
up to inner automorphism, of the corresponding simple Lie algebra. We implement our algorithm to classify the closed subsets of the irreducible root systems of ranks 3 through 7. We present a complete description of the classification for the closed subsets of the rank 3 irreducible root systems. We employ this to classify all regular subalgebras of the rank 3 simple Lie algebras. This is part of a bigger project to classify the non semisimple subalgebras of small-dimensional simple Lie algebras, see [DR15, DR16a, DR16b, DR17, May16. We present only summary data for the classifications in higher ranks due to the large size of these classifications.

The article is organized as follows. In Section 2, we review root systems and closed subsets of root systems. In Section 3, we describe our algorithm for classifying the closed subsets of root systems, along with its implementation in GAP4 [GAP], using the SLA package [dGr09]. The latest version of this package (version 1.5) contains this implementation. We present the runtimes of the main steps of the algorithm on some sample inputs. All timings in this paper have been obtained on a 2.0Ghz processor with 4GB of memory for sf GAP.

Next, in Section 4, we present the full classification of the closed subsets of the irreducible root system of rank 3 derived from the implementation of our algorithm. In this section we also present summary data for the classifications of closed subsets of the irreducible root systems of ranks 4 through 7. In Section 5, we discuss the relationship between closed subsets of irreducible root systems and regular subalgebras of the corresponding simple Lie algebras. In this section, we also employ the classification of closed subsets of rank 3 irreducible root systems to yield a classification of regular subalgebras of the corresponding simple Lie algebras.

The ground field for Lie algebras in this article is the complex numbers. Unless explicitly stated otherwise, " $\oplus$ " denotes the direct sum of vector spaces, not of Lie algebras.

Acknowledgement: We thank Heiko Dietrich for his help with the computation of the closed subsets of the root system of type $E_{7}$, for which his computer worked several weeks. AD would also like to thank WAdG and the Department of Mathematics at the University of Trento for their warm hospitality during a recent visit.

\section*{2. Roots systems and their closed subsets}

Let E be a Euclidean space with positive definite symmetric bilinear form denoted $(\alpha, \beta)$, for $\alpha, \beta \in \mathrm{E}$. A subset $\Phi$ of E is called a root system in E if the following axioms are satisfied:
\begin{itemize}
\item[(R1)] $\Phi$ is finite, spans E, and does not contain 0.
\item[(R2)] If $\alpha \in \Phi$, the only multiples of $\alpha$ in $\Phi$ are $\pm \alpha$.
\item[(R3)] If $\alpha \in \Phi$, the reflection determined by $\alpha$ leaves $\Phi$ invariant.
\item[(R4)] If $\alpha, \beta \in \Phi$, then $\left\langle\beta, \alpha^{\vee}\right\rangle=\frac{2(\beta, \alpha)}{(\alpha, \alpha)} \in \mathbb{Z}$.
\end{itemize}

The root system $\Phi$ is called irreducible if it cannot be partitioned into the union of two proper subsets such that each root in one set is orthogonal to each root in the other. Let $s_{\alpha}$ denote the reflection determined by $\alpha \in \Phi$. The Weyl group of a root system is the subgroup of GL(E) generated by the reflections $s_{\alpha}, \alpha \in \Phi$.

A subset $T$ of a root system $\Phi$ is closed if for any $\alpha, \beta \in T, \alpha+\beta \in \Phi$ implies $\alpha+\beta \in T$. Any closed set $T$ is a disjoint union of its symmetric part $T^{r}=\{\alpha \in T \mid-\alpha \in T\}$, and its special part $T^{u}=\{\alpha \in T \mid-\alpha \notin T\}$.

Closed subsets $T$ and $T^{\prime}$ of a root system $\Phi$ are conjugate if there exists an element $w \in W(\Phi)$ such that $w(T)=T^{\prime}$. The following lemma is well-known (and easy to prove).
Lemma 2.1. $T^{r}$ is a closed root subsystem of $\Phi$. For any two roots $\alpha \in T^{u}$ and $\beta \in T$ such that $\alpha+\beta$ is a root, we have that $\alpha+\beta \in T^{u}$. In particular, $T^{u}$ is closed.
2.1. Topologies on finite sets and closed subsets of the root systems of type $A_{n-1}$. Here we briefly describe the correspondence that exists between the closed sets in the root systems of type $A_{n-1}$ and the topologies that a set of size $n$ can have. To the best of our knowledge this correspondence has first been described by Borevich ([Bor76], [Bor77]). Various computer programs have been developed to enumerate the topologies of a finite set (see for example [BM02]).

Let $n \geq 1$ and $X=\{1,2, \ldots, n\}$. A topology on $X$ is a collection $\tau$ of subsets of $X$ such that $\emptyset, X \in \tau$ and the union and intersection of elements of $\tau$ is again in $\tau$. The elements of $\tau$ are said to be closed sets. For $i \in X$ we denote by $\bar{i}$ the smallest closed set containing $i$. The topology $\tau$ is called $T_{0}$ if for $i, j \in X, i \neq j$ we have that $i \notin \bar{j}$ or $j \notin \bar{i}$. Two topologies $\tau, \tau^{\prime}$ are called homeomorphic if there is a $\pi \in S_{n}$ with $\tau^{\prime}=\{\pi(T): T \in \tau\}$.

To a topology $\tau$ on $X$ we associate an $n \times n$-matrix $\sigma^{\tau}$, where $\sigma_{i j}^{\tau}=1$ if $i \in \bar{j}$, and $\sigma_{i j}^{\tau}=0$ otherwise. It is clear that from $\sigma^{\tau}$ we can reconstruct $\tau$. Furthermore, a matrix $\sigma$ with coefficients 0,1 corresponds to a topology if
$$\sigma_{i i}=1 \text { for all } i \text { and } \sigma_{i j}=1, \sigma_{j k}=1 \text { imply } \sigma_{i k}=1 .$$
Finally, we have that $\tau, \tau^{\prime}$ are homeomorphic if and only if there is a $\pi \in S_{n}$ with $\sigma_{i j}^{\tau^{\prime}}=$ $\sigma_{\pi(i), \pi(j)}^{\tau}$.

The root system $\Phi$ of type $A_{n-1}$ consists of all $\alpha_{i j}$ for $1 \leq i \neq j \leq n$. Here $\alpha_{1,2}, \alpha_{2,3}, \ldots, \alpha_{n-1, n}$ are the simple roots. If $i<j$ then $\alpha_{i j}=\alpha_{i, i+1}+\alpha_{i+1, i+2}+\cdots+\alpha_{j-1, j}$. If $i>j$ then $\alpha_{i j}=-\alpha_{j i}$. This implies that $\alpha_{i j}+\alpha_{k l} \in \Phi$ if $j=k$, when the sum is $\alpha_{i l}$, or if $l=i$, when the sum is $\alpha_{k j}$. The Weyl group of $\Phi$ is isomorphic to $S_{n}$, and for $\pi \in S_{n}$ we have $\pi \cdot \alpha_{i j}=\alpha_{\pi(i), \pi(j)}$.

Let $\tau$ be a topology on $X$, and set $S=\left\{\alpha_{i j} \in \Phi \mid \sigma_{i j}^{\tau}=1\right\}$. Then by (1) we see that $S$ is closed. Moreover, $\tau$ is $T_{0}$ if and only if for each $i, j \in X, i \neq j$, at least one of $\sigma_{i j}^{\tau}, \sigma_{j i}^{\tau}$ is 0 . But this is the same as saying that $S$ is special.

Conversely, let $S \subset \Phi$ be closed. Define the matrix $\sigma$ such that $\sigma_{i i}=1$ for all $i$ and $\sigma_{i j}=1$ if $\alpha_{i j} \in S$, and $\sigma_{i j}=0$ otherwise. Then $\sigma$ satisfies (1), and therefore defines a topology on $X$. It is also clear that two topologies are homeomorphic if and only if the corresponding closed sets are conjugate under $S_{n}$.

The conclusion is that topologies on $X$ correspond to closed sets in $\Phi$, whereas topologies up to homeomorphism correspond to closed sets up to conjugacy by the Weyl group. In this correspondence the $T_{0}$ topologies correspond to special closed sets. Therefore, the tables in [BM02] imply that the root system of type $A_{15}$ contains 4483130665195086 special closed sets.

\section*{3. The algorithm}

In this section we outline an algorithm for listing the closed sets of a root system $\Phi$. This algorithm is split into two parts. In the first part we find all special closed subsets of $\Phi$ up to conjugacy. The second part is a procedure to list, up to conjugacy, all non-special closed sets whose special part is a given special closed set obtained by the first half of the algorithm.
3.1. Listing the special closed sets. We first give a simple algorithm for listing the special closed sets of a root system up to conjugacy by the Weyl group. Subsequently we describe some ideas that can be used to implement it reasonably efficiently.

The algorithm is based on three lemmas, the first of which is proved in [Bou68], Chapter VI, Proposition 22, see Sop04 for an easier proof.

Lemma 3.1. A special closed set is conjugate to a subset of $\Phi^{+}$.
For a closed set $T$ we let $T+T$ be the set of all $\gamma \in T$ such that $\gamma=\alpha+\beta$ for certain $\alpha, \beta \in T$. Let $\Phi^{+}$be a fixed subset of positive roots with set of simple roots $\Delta$. If $\alpha=\sum_{\alpha \in \Delta} k_{\alpha} \alpha$, then $\sum_{\alpha \in \Delta} k_{\alpha}$ is called the height of $\alpha$. Write $W=W(\Phi)$, the Weyl group of $\Phi$.

Lemma 3.2. Let $T$ be a special closed set. Then $T+T$ is strictly contained in $T$.
Proof. Suppose that $T \subset \Phi^{+}$and let $\alpha \in T$ be of minimal height. Then $\alpha$ cannot be a sum of two elements of $T$. The general case follows by Lemma 3.1. \(\square\)

For a closed set $T$ we denote its conjugacy class by $[T]$, that is,
$$[T]=\{w(T) \mid w \in W\} .$$
Let $T$ be a special closed set. By Lemma 3.2 there is an $\alpha \in T \backslash(T+T)$. Set $T^{\prime}=T \backslash\{\alpha\}$. Then $T^{\prime}$ is closed and we say that $\left[T^{\prime}\right]$ is a successor of $[T]$. Note that the set of successors of $[T]$ depends on the class $[T]$ and not on the choice of $T$. Indeed, let $S \in[T]$, then there is a $w \in W$ with $w(T)=S$. So $\beta=w(\alpha) \in S \backslash(S+S)$ and with $S^{\prime}=S \backslash\{\beta\}$ we have $S^{\prime}=w\left(T^{\prime}\right)$ and therefore $\left[S^{\prime}\right]=\left[T^{\prime}\right]$.

Lemma 3.3. Let $T^{\prime}$ be a special closed set of cardinality $n<\left|\Phi^{+}\right|$. Then there is a special closed set $T$ of cardinality $n+1$ such that $\left[T^{\prime}\right]$ is a successor of $[T]$.

Proof. By Lemma 3.1 we may assume that $T^{\prime} \subset \Phi^{+}$. Set
$$\mathcal{N}\left(T^{\prime}\right)=\left\{\alpha \in \Phi \mid \alpha+\beta \in T^{\prime} \text { for all } \beta \in T^{\prime} \text { such that } \alpha+\beta \in \Phi\right\},$$
which we call the normalizer of $T^{\prime}$. We claim that there is a $\gamma \in \Phi^{+}$with $\gamma \notin T^{\prime}$, $\gamma \in \mathcal{N}\left(T^{\prime}\right)$. Let $\mathfrak{g}$ be the semisimple Lie algebra over $\mathbb{C}$ with Cartan subalgebra $\mathfrak{h}$ such that the corresponding root system is isomorphic to $\Phi$. In the sequel we identify this root system and $\Phi$. Let $\mathfrak{n}^{+}$be the subalgebra of $\mathfrak{g}$ spanned by the root vectors corresponding to the roots in $\Phi^{+}$. Let $\mathfrak{a}$ be the subspace of $\mathfrak{n}^{+}$spanned by the root vectors corresponding to the roots in $T^{\prime}$. Since $T^{\prime}$ is closed, $\mathfrak{a}$ is a subalgebra. Because $\mathfrak{a}$ is spanned by root vectors we have $[\mathfrak{h}, \mathfrak{a}] \subset \mathfrak{a}$. Consider the normalizer of $\mathfrak{a}$ in $\mathfrak{n}^{+}, \mathfrak{n}(\mathfrak{a})=\left\{x \in \mathfrak{n}^{+} \mid[x, \mathfrak{a}] \subset \mathfrak{a}\right\}$. Let $x \in \mathfrak{n}(\mathfrak{a})$ and $y \in \mathfrak{a}, h \in \mathfrak{h}$, then $[[h, x], y]=-[[x, y], h]-[[y, h], x]$. Now $[x, y] \in \mathfrak{a}$ and hence $[[x, y], h] \in \mathfrak{a}$. Secondly, $[y, h] \in \mathfrak{a}$ so that $[[y, h], x] \in \mathfrak{a}$ as well. We conclude that $[h, x] \in \mathfrak{n}(\mathfrak{a})$. It follows that $\mathfrak{n}(\mathfrak{a})$ is a subalgebra of $\mathfrak{n}^{+}$, normalized by $\mathfrak{h}$. Therefore, $\mathfrak{n}(\mathfrak{a})$ is also spanned by root vectors. If $\mathfrak{n}(\mathfrak{a})=\mathfrak{a}$ then $\mathfrak{a}$ would be a Cartan subalgebra of $\mathfrak{n}^{+}$. But the only Cartan subalgebra of $\mathfrak{n}^{+}$is $\mathfrak{n}^{+}$itself. We conclude that $\mathfrak{n}(\mathfrak{a})$ contains a root vector corresponding to a $\gamma \in \Phi^{+}$, not lying in $\mathfrak{a}$. Then $\gamma \notin T^{\prime}, \gamma \in \mathcal{N}\left(T^{\prime}\right)$.

Set $T=T^{\prime} \cup\{\gamma\}$. Then $T$ is closed and $\gamma \in T \backslash(T+T)$. The lemma follows. \(\square\)

Remark 3.4. Let $T$ be a special closed set and $W_{T}=\{w \in W \mid w(T)=T\}$, the stabilizer of $T$ in $W$. Let $\alpha, \beta \in T \backslash(T+T)$ be such that $\beta=w(\alpha)$, for a certain $w \in W_{T}$. Then $w(T \backslash\{\alpha\})=T \backslash\{\beta\}$.

This, together with the previous lemma, implies the correctness of the following algorithm. It takes as input a set $M$ of representatives of the conjugacy classes of special closed sets of cardinality $n+1$. It outputs a set of representatives of the conjugacy classes of special closed sets of cardinality $n$. The basic idea is to compute the successors of each element of $M$ and weed out the conjugate copies. Remark 3.4 helps with the latter task. The algorithm takes the following steps:
\begin{itemize}
\item[(1)] Set $L=\emptyset$.
\item[(2)] For each $T$ in $M$ do
\begin{itemize}
\item[(a)] Compute $W_{T}$.
\item[(b)] Compute the orbits of $W_{T}$ on $T \backslash(T+T)$.
\item[(c)] For each such orbit take a representative $\alpha$ and set $S=T \backslash\{\alpha\}$. If $S$ is not conjugate to any element of $L$, then add $S$ to $L$.
\end{itemize}
\item[(3)] Return $L$.
\end{itemize}

Write $m=\left|\Phi^{+}\right|$. Now starting with the set $M$ containing the one special closed subset of $\Phi^{+}$of maximal cardinality, that is, $\Phi^{+}$itself, we iterate this algorithm and obtain the special closed sets (up to conjugacy) of sizes $m-1, m-2, \ldots, 1$. So in the end we obtain, by Lemma 3.1, all special closed sets of $\Phi$ up to conjugacy.

Remark 3.5. We give some technical details of the implementation. The algorithm has been implemented in the language of the computer algebra system GAP4 [GAP], as part of the package SLA [dGr11].

In our implementation we use a list $\alpha_{1}, \ldots, \alpha_{N}$ of all the roots of the root system. A root is represented by its position in this list. So instead of $\alpha_{i}$ we just use $i$. This gives a memory efficient way to represent a closed set as a list of indices. The addition relations of the roots are stored in a table. This is a 2-dimensional table $\mathcal{T}$ such that if $\mathcal{T}(i, j)=k$, then $\alpha_{i}+\alpha_{j}=\alpha_{k}$ if $k \neq 0$, and $\alpha_{i}+\alpha_{j}$ is not a root if $k=0$.

The Weyl group is given as a permutation group on $\{1, \ldots, N\}$. This allows us to use the functionality for permutation groups present in GAP4. Thus we can readily compute generators of $W_{T}$ (the command for this is Stabilizer( W, T, OnSets )) and the orbits of $W_{T}$ on $T \backslash(T+T)$ (the command here is Orbits( H, D ), where $\mathrm{H}=W_{T}$ and $\mathrm{D}=$ $T \backslash(T+T))$.

For deciding whether two sets are conjugate under the Weyl group backtrack methods (see [Ser03], Chapter 9) are used. They are present in the GAP core system, the command for checking whether $S_{1}, S_{2}$ are conjugate is RepresentativeAction( W, S1, S2, OnSets ).

In order to make the implementation more efficient we make use of certain invariants of closed sets. An invariant of closed sets is a function $\chi:\{$ closed sets $\} \rightarrow A$, where $A$ is some set, such that $S=w(T)$ for a $w \in W$ implies that $\chi(S)=\chi(T)$. First we describe three invariants. In order to describe the first two of these we need some well known facts on weights (see [Hum72], Chapter 13), which we recall first.

Let $\Delta=\left\{\alpha_{1}, \ldots, \alpha_{\ell}\right\}$ be a fixed set of simple roots of $\Phi$. Define the elements $\lambda_{i}$ of the real space $E$ spanned by $\Phi$ by $\left\langle\lambda_{i}, \alpha_{j}^{\vee}\right\rangle=\delta_{i, j}$. These $\lambda_{i}$ are called the fundamental weights. A weight is a $\mathbb{Z}$-linear combination of the fundamental weights. A weight $\lambda=$ $m_{1} \lambda_{1}+\cdots+m_{\ell} \lambda_{\ell}$ is dominant if $m_{i} \geq 0$ for all $i$. The Weyl group $W$ acts on the set of weights, and each weight $\lambda$ is $W$-conjugate to a unique dominant weight (Hum72, Lemma 13.2.A). This dominant weight is computed as follows. Set $\mu_{1}=\lambda$. Let $i \geq 1$
and suppose that $\mu_{i}$ is defined. Write $\mu_{i}=n_{1} \lambda_{1}+\cdots+n_{\ell} \lambda_{\ell}$. If $n_{j} \geq 0$ for all $j$ then $\mu_{i}$ is the dominant weight that we are after. Otherwise there is a $j$ with $n_{j}<0$ and we set $\mu_{i+1}=s_{\alpha_{j}}\left(\mu_{i}\right)$. It is not difficult to show that this procedure terminates and returns the unique dominant weight conjugate to $\lambda$ (see, for example, [dGr00], p. 319). Note that by recording the $s_{\alpha_{j}}$ that are used we also find a $w \in W$ such that $w(\lambda)$ is dominant.

Now let $S \subset \Phi$ then its sum vector is $\xi(S)=\sum_{\alpha \in S} \alpha$. The sum vectors of conjugate sets are obviously conjugate, but in general not the same. In order to get an invariant we compute the unique dominant weight that is conjugate to $\xi(S)$. We denote the result by $\sigma(S)$. Then $\sigma$ is an invariant of closed sets.

For a second invariant let $r$ be a rational number and consider the set $S^{(r)}=\{\alpha \in \Phi \mid$ $(\alpha, \beta) \geq r$ for all $\beta \in S\}$. If $T=w(S)$ for a $w \in W$ then also $T^{(r)}=w\left(S^{(r)}\right)$ because the Weyl group leaves the inner product invariant. Define $\delta^{r}(S)=\sigma\left(S^{r}\right)$; then $\delta^{r}$ is an invariant of closed sets. In our implementation we normalize the inner product so that $(\alpha, \alpha)=2$ for short roots $\alpha$ and we use the invariant $\delta^{-1}$. We also considered other values of $r$, but $r=-1$ turned out to work best.

Let $T=\left\{\alpha_{i_{1}}, \ldots, \alpha_{i_{m}}\right\}$ be a closed set. The matrix of its inner products is $M_{T}=$ $\left(\left(\alpha_{i_{k}}, \alpha_{i_{l}}\right)\right)_{1 \leq k, l \leq m}$, and let $\widehat{M}_{T}$ be the matrix consisting of the sorted rows of $M_{T}$, which are listed in lexicographical order. Since the Weyl group leaves the inner product invariant, if $T, S$ are conjugate, then $M_{T}$ can be obtained from $M_{S}$ by applying a permutation to both the rows and the columns. So in that case $\widehat{M}_{T}=\widehat{M}_{S}$. Hence we have a third invariant.

We have three applications of these invariants: to make the computation of the stabilizer $W_{T}$ more efficient, to reduce the number of sets $S$ that we attempt to insert in the list $L$ in Step (2c), and reduce the number of conjugacy tests that we perform in Step (2c) (that is, the number of calls to RepresentativeAction).

The computation of the stabilizer. We can use the invariant $\sigma(T)$ to compute a subgroup $W^{\prime} \subset W$ such that the $W_{T}^{\prime}=W_{T}$, making the computation of the stabilizer more efficient. For this we consider the sum vector $\xi(T)$. We compute a $w \in W$ such that $w(\xi(T))$ is dominant. Let $\lambda_{1}, \ldots, \lambda_{\ell}$ denote the fundamental weights as above and write $w(\xi(T))=m_{1} \lambda_{1}+\cdots+m_{\ell} \lambda_{\ell}$. Then the stabilizer $W_{w(\xi(T))}$ is generated by the $s_{\alpha_{i}}$ where $i$ is such that $m_{i}=0$ ([Hum72], Lemma 10.3B). Obviously $W_{\xi(T)}=w^{-1} W_{w(\xi(T))} w$. We see that it is straightforward to compute the group $W_{\xi(T)}$ and we can let this be $W^{\prime}$. Furthermore, in practice it is useful to check whether the generators of $W^{\prime}$ leave $T$ invariant. If this is the case then we have the stabilizer without any further computation.

Reducing the number of sets $S$ in Step (2c). Note that the algorithm starts with the closed set $\Phi^{+}$and the other closed sets are constructed as subsets of that. Hence each closed set produced by the algorithm is contained in $\Phi^{+}$.

In Step (2c) of the algorithm different non-conjugate sets $T$ of size $n+1$ can produce conjugate successors $S$ of size $n$ (and usually this happens rather often). In order to reduce the number of closed sets $S$ that go into the second part of the step (that is, the conjugacy testing) we first compute all sets $T^{\prime} \subset \Phi^{+}$having $S$ as a successor, and only continue with $S$ if $\sigma(T)$ is minimal among all $\sigma\left(T^{\prime}\right)$. (For this we can use any order on the weights, for example the lexicographical order on coordinate vectors.) If it is not, then we are certain that a set conjugate to $S$ will be constructed as successor of another set of size $n+1$. More precisely we replace Step (2c) by the following
\begin{itemize}
\item[] (2c) For each such orbit take a representative $\alpha$ and set $S=T \backslash\{\alpha\}$.
\end{itemize}
\begin{itemize}
\begin{itemize}
\item[(i)] Compute $\mathcal{N}^{+}(S)=\left\{\beta \in \Phi^{+} \mid \beta \notin S, S \cup\{\beta\}\right.$ is closed $\}$.
\item[(ii)] For each $\beta \in \mathcal{N}^{+}(S)$ set $T^{\prime}=S \cup\{\beta\}$ and compute $\sigma\left(T^{\prime}\right)$.
\item[(iii)] If $\sigma(T)$ is minimal among all $\sigma\left(T^{\prime}\right)$ then check whether $S$ is not conjugate to any element of $L$. If it is not then add $S$ to $L$.
\end{itemize}
\end{itemize}

Reduce the number of conjugacy tests. Next we come to the conjugacy testing. In order to limit the necessary tests we use the invariants $\widehat{M}_{S}$ and $\delta^{-1}(S)$. Only if a set $S^{\prime}$ in the list $L$ has $\widehat{M}_{S}=\widehat{M}_{S^{\prime}}$ and $\delta^{-1}(S)=\delta^{-1}\left(S^{\prime}\right)$ we do a conjugacy test, otherwise we already know that $S, S^{\prime}$ are not conjugate. Often no $S^{\prime}$ in $L$ has $\widehat{M}_{S}=\widehat{M}_{S^{\prime}}$ and $\delta^{-1}(S)=\delta^{-1}\left(S^{\prime}\right)$ and in those cases $S$ can directly be added to $L$. This explains the relatively low number of conjugacy tests in the sixth column of Table 1.

Remark 3.6. • One other powerful invariant is the permanent of the matrix $M_{T}$. Experiments show that it is very effective. However, it is difficult to compute the permanent of a matrix, and the time needed to compute the permanents outweighs the gains made from using this invariant.
\begin{itemize}
\item[-] Of course it is possible to use the invariants $\delta^{-1}, \widehat{M}_{T}$ also for reducing the number of sets $S$ in Step (2c)(ii). In fact, experiments show that these manage to reduce the number of sets even further. However, the number of sets $T^{\prime}$ for which these invariants have to be computed can be very large (see the fourth column of Tabe [1). Therefore the invariant $\sigma$ works better because it is much easier to compute. Similarly, $\sigma$ could also be used to limit the number of conjugacy tests. But here the extra time needed to compute the invariants $\widehat{M}_{T}$ and $\delta^{-1}$ pays off: these invariants limit the number of conjugacy tests more effectively.
\item[-] Many alternatives to our algorithm are possible. Here we briefly go into two of them. Instead of our approach to conjugacy testing it is possible compute a minimal image of each closed set; that is, a closed set $T$ is replaced by the minimal element of its orbit (in some ordering, for example the the lexicographical). Then the conjugacy problem boils down to testing equality. In [JJPW19] algorithms for computing minimal images are given which have been implemented in the GAP4 package images ([JJPW18]). However, it appears that computing a minimal image of each closed set in the output of our algorithm takes longer than listing the closed sets in the first place (for example, for the root system of type $E_{6}$ we find 94635 special closed sets which are listed in 149 seconds, whereas the computation of a minimal image of each of the 94635 closed sets took 443 seconds). Another more general purpose algorithm that can be used for our problem is described in [Bet18]. The rough structure of this algorithm is similar to ours. It starts with two sets $\mathcal{A}$ and $\mathcal{B}$ (in our case these are the special closed sets of sizes $n+1$ and $n$ respectively) on which a group $G$ acts (in our case the Weyl group). Also given is a relation $\mathcal{R} \subset \mathcal{A} \times \mathcal{B}$ (in our case this is the successor relation). Knowing the $G$-orbits in $\mathcal{A}$ the algorithm computes the $G$-orbits in $\mathcal{B}$. We have not implemented this algorithm, but it seems to be hard to combine it with the invariants that we use and which are very succesful at making our algorithm more efficient. Probably it would be possible to modify the algorithm in [Bet18] to also use those invariants, but then the result would be a method very similar to ours.
\item[-] There always is the obvious question as to the reliability of our implementations. In other words: how can we be sure that output of our computations is correct. Of
\end{itemize}
course we can never be absolutely sure. However, we do have some circumstantial evidence that our implementations are correct. Firstly, in the course of our work we also have tried completely different algorithms, and the output has always been the same. Secondly, for the root systems of type $A_{n}$ the number of special closed sets that we get is confirmed by the data in [BM02].
3.2. Practical performance. Here we present some data on the practical performance of our algorithm. In Table 1 we list the running times of various parts of the algorithm. As test root systems we have taken $F_{4}, E_{6}, B_{6}, B_{7}$. The second column of this table has the total time needed to compute the stabilizers $W_{T}$. The third column lists the time taken to compute the orbits of $W_{T}$ on $T \backslash(T+T)$. The fourth column has the time taken to compute $\sigma(T)$ for the various $T$ (to limit the number of sets $S$ that we try to insert in the list $L$ ). The fifth column displays the total time taken to compute the invariants $\widehat{M}_{T}, \delta^{-1}$. The sixth column has the total time taken to do the conjugacy tests (that is, the time taken in calls to RepresentativeAction). The integer following the running times in these columns is the number of times the algorithm entered the computation (so, for example, for $B_{6}$ there have been 1273371 computations of $\sigma(T)$ ). The seventh and eighth colums show, respectively, the number of closed sets in the output and the total time taken. The last column has the number of miliseconds taken for each closed set in the output (this is the quotient of the entries in the eighth and seventh columns).

We list a few obvious observations:
\begin{itemize}
\item[-] The parts contributing most to the running time are the computation of the stabilizers (which is done for almost every final closed set), and the computation of the invariant $\sigma$ (which is done a huge number of times).
\item[-] The conjugacy test is not perfomed very often (compared to the number of closed sets in the output).
\item[-] The time taken per closed set increases markedly with increasing rank.
\end{itemize}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|l|}
\hline type & Stab & Orb & Invariant $\sigma$ & Invariants $\widehat{M}_{T}, \delta^{-1}$ & Conjugacy & Number of closed sets & Time & ms per closed set \\
\hline $F_{4}$ &
\begin{tabular}[t]{l}
0.9 \\
3577
\end{tabular} &
\begin{tabular}[t]{l}
0.3 \\
3577
\end{tabular} &
\begin{tabular}[t]{l}
0.4 \\
19889
\end{tabular} &
\begin{tabular}[t]{l}
0.4 \\
3954
\end{tabular} &
\begin{tabular}[t]{l}
0.12 \\
410
\end{tabular} & 3579 & 2.2 & 0.61 \\
\hline $E_{6}$ &
\begin{tabular}[t]{l}
56.7 \\
94634
\end{tabular} &
\begin{tabular}[t]{l}
9.6 \\
94634
\end{tabular} &
\begin{tabular}[t]{l}
36.6 \\
828924
\end{tabular} &
\begin{tabular}[t]{l}
24.2 \\
115652
\end{tabular} &
\begin{tabular}[t]{l}
17.8 \\
30925
\end{tabular} & 94635 & 149 & 1.57 \\
\hline $B_{6}$ &
\begin{tabular}[t]{l}
90.2 \\
151384
\end{tabular} &
\begin{tabular}[t]{l}
16.9 \\
151384
\end{tabular} &
\begin{tabular}[t]{l}
50.5 \\
1273371
\end{tabular} &
\begin{tabular}[t]{l}
23.5 \\
174243
\end{tabular} &
\begin{tabular}[t]{l}
13.4 \\
27234
\end{tabular} & 151386 & 201 & 1.33 \\
\hline $B_{7}$ &
\begin{tabular}[t]{l}
5009 \\
6115471
\end{tabular} &
\begin{tabular}[t]{l}
659 \\
6115471
\end{tabular} &
\begin{tabular}[t]{l}
4656 \\
69416764
\end{tabular} &
\begin{tabular}[t]{l}
1506 \\
7223257
\end{tabular} &
\begin{tabular}[t]{l}
1414 \\
1718047
\end{tabular} & 6115473 & 13803 & 2.26 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 1. Running times (in seconds) of various parts of the algorithm. See the text for a description of the contents of the columns.}
\end{table}
3.3. Listing the non-special closed sets. Now we turn to the second part of the procedure, that is, to finding the non-special closed sets, given the special ones. We will
outline an algorithm for obtaining the closed sets $Q$ such that $Q^{u}=T$, where $T$ is a given special closed set. Since we have the list of all special closed sets, by Lemma 2.1 this suffices to get all closed sets. We start with the following simple lemma.

Lemma 3.7. Let $T$ be a special closed set. Let $\alpha \in \Phi \backslash(T \cup-T)$. There is a closed set $S$ such that $S^{u}=T$ and $\alpha,-\alpha \in S^{r}$ if and only if $T \cup\{\alpha,-\alpha\}$ is closed.

Proof. If there is such an $S$, then Lemma 2.1 shows that $T \cup\{\alpha,-\alpha\}$ is closed. For the converse we can take $S=T \cup\{\alpha,-\alpha\}$. \(\square\)

The next lemma is similar to [Sop04], Proposition 5.
Lemma 3.8. Let $T$ be a special closed set. Set $S=\{\alpha \in \Phi \backslash(T \cup-T) \mid T \cup$ $\{\alpha,-\alpha\}$ is closed $\}$. Then $R=S \cup T$ is a closed set with $R^{r}=S, R^{u}=T$.

Proof. We first show that $S$ is closed. Let $\alpha, \beta \in S$ be such that $\alpha+\beta \in \Phi$. We show that $T \cup\{\alpha+\beta,-\alpha-\beta\}$ is closed. Let $\gamma \in T$ be such that $\alpha+\beta+\gamma \in \Phi$. Then at least two of $\alpha+\beta, \alpha+\gamma, \beta+\gamma$ are roots. (If $\Phi$ is simply laced, this can be shown by using the property that for $\delta, \epsilon \in \Phi$ we have that $\delta+\epsilon \in \Phi$ if and only if $(\delta, \epsilon)<0$. In general the intersection of $\Phi$ and the set of linear combinations of $\alpha, \beta, \gamma$ is a root system of rank at most 3. For those root systems it is easy to show the statement by a brute force verification.) So at least one of $\alpha+\gamma, \beta+\gamma$ lies in $\Phi$. Suppose $\alpha+\gamma \in \Phi$. Since $T \cup\{\alpha,-\alpha\}$ is closed, $\alpha+\gamma \in T$. But then also $\beta+\alpha+\gamma \in T$. In the same way we see that if $-\alpha-\beta+\gamma \in \Phi$ then $-\alpha-\beta+\gamma \in T$. Hence $T \cup\{\alpha+\beta,-\alpha-\beta\}$ is closed and the same follows for $S$.

Now it is obvious that $R$ is closed. Furthermore, if $\alpha \in S$ then also $-\alpha \in S$ so that $R^{r}=S$, implying also $R^{u}=T$. \(\square\)

Now fix a special closed set $T$. The algorithm first constructs the set $S$ as in the previous lemma. By Lemma 3.7, $S$ contains all closed sets that are the symmetric part of a closed set whose special part is $T$. So an immediate way of proceeding would be to enumerate all symmetric closed subsets of $S$, for each such set $P$ form the closed set $P \cup T$, and get rid of conjugate copies. However, there is a much more efficient way of doing it.

First note that $S$ is a root subsystem of $\Phi$. Let $\alpha \in S$, then the reflection $s_{\alpha}$ sends $T$ to itself. (Indeed, if $\beta \in T$ then the string $\{\beta+k \alpha \mid k \in \mathbb{Z}\}$ is contained in $S$ as $S$ is closed, and it has to be contained in $T$ by Lemma 2.1.) So $T$ is stabilized by the Weyl group $W^{S}$ of $S$. Hence, if two closed symmetric subsets $P, P^{\prime} \subset S$ are conjugate under $W^{S}$, then $P \cup T, P^{\prime} \cup T$ are as well, so that they are conjugate under $W$. Now we use Dynkin's algorithm ([Dyn52], see [dGr17], §5.9 for a more recent description) to find all symmetric closed subsets of $S$ up to conjugacy by $W^{S}$. For each symmetric closed set $P$ found we form the set $P \cup T$. Let $W_{T}$ be the stabilizer of $T$ in $W$. Two closed subsets $P \cup T, P^{\prime} \cup T$ are conjugate under $W$ if and only if they are under $W_{T}$. So we erase the $W_{T}$-conjugate copies from the list and we are done. Note that in order to execute this we do not have to compute the stabilizers $W_{T}$ as they have already been constructed by the algorithm of Section 3.1.

By comparing the running times for the root systems $F_{4}, B_{5}, B_{6}, E_{6}$ in Tables 1, 10 we see that computing the non-special closed sets does not weigh heavily on the runnning time. The main part of the computation time is taken for listing the special closed sets.

\section*{4. Closed subsets of irreducible root systems}

In this section, we present the full classification of the closed subsets of the irreducible root systems of rank 3 derived from the implementation of our algorithm. This classification is contained in Tables 2 through 9. In this section we also present summary data for the classifications of closed subsets of the irreducible root systems of ranks 4 through 7 in Table 10.

For each root system, the classification is divided into three parts: The symmetric closed subsets $T^{r}$, for which the special part is empty $T^{u}=\emptyset$; the special closed subsets $T^{u}$, for which the symmetric part is empty $T^{r}=\emptyset$; and the Levi decomposable closed subsets $T^{r} \dot{\cup} T^{u}$, for which $T^{r} \neq \emptyset$ and $T^{u} \neq \emptyset$.

For symmetric closed subsets, we identify the isomorphism classes. The symmetric closed subsets have been computed with the implementation of Dynkin's algorithm ([Dyn52]) in the SLA package ([dGr11]) of GAP4.

\begin{table}
\begin{tabular}[t]{|l|l|}
\hline & Special closed subsets $\mathbf{T}^{\mathbf{u}}\left(\mathbf{T}^{\mathbf{r}}=\mathbf{0}\right)$ \\
\hline 1 & $\alpha_{1}, \alpha_{2}, \alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}$ \\
\hline 2 & $\alpha_{2}, \alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}$ \\
\hline 3 & $\alpha_{1}, \alpha_{2}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}$ \\
\hline 4 & $\alpha_{1}, \alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}$ \\
\hline 5 & $\alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}$ \\
\hline 6 & $\alpha_{1}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}$ \\
\hline 7 & $\alpha_{2}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}$ \\
\hline 8 & $\alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}$ \\
\hline 9 & $\alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}$ \\
\hline 10 & $\alpha_{3}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}$ \\
\hline 11 & $\alpha_{1}, \alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}$ \\
\hline 12 & $\alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}$ \\
\hline 13 & $\alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}$ \\
\hline 14 & $\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}$ \\
\hline 15 & $\alpha_{3}$ \\
\hline & Levi decomposable closed subsets $\mathbf{T}^{\mathbf{r}} \oplus \mathbf{T}^{\mathbf{u}}\left(\mathbf{T}^{\mathbf{r}}, \mathbf{T}^{\mathbf{u}} \neq \mathbf{0}\right)$ \\
\hline 16 & $\alpha_{1}, \alpha_{2}, \alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3},-\alpha_{1}$ \\
\hline 17 & $\alpha_{1}, \alpha_{2}, \alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3},-\alpha_{3}$ \\
\hline 18 & $\alpha_{1}, \alpha_{2}, \alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3},-\alpha_{2}$ \\
\hline 19 & $\alpha_{1}, \alpha_{2}, \alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3},-\alpha_{1},-\alpha_{3}$ \\
\hline 20 & $\alpha_{1}, \alpha_{2}, \alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3},-\alpha_{1},-\alpha_{2},-\alpha_{1}-\alpha_{2}$ \\
\hline 21 & $\alpha_{1}, \alpha_{2}, \alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3},-\alpha_{2},-\alpha_{3},-\alpha_{2}-\alpha_{3}$ \\
\hline 22 & $\alpha_{2}, \alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3},-\alpha_{3}$ \\
\hline 23 & $\alpha_{1}, \alpha_{2}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3},-\alpha_{1}$ \\
\hline 24 & $\alpha_{1}, \alpha_{3}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3},-\alpha_{1}$ \\
\hline 25 & $\alpha_{1}, \alpha_{2}, \alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3},-\alpha_{2}$ \\
\hline 26 & $\alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3},-\alpha_{1}-\alpha_{2}$ \\
\hline 27 & $\alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3},-\alpha_{3}$ \\
\hline 28 & $\alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3},-\alpha_{1}-\alpha_{2}$ \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 2. The special and Levi decomposable closed subsets of the root system $A_{3}$.}
\end{table}

\begin{table}
\begin{tabular}[t]{|l|l|l|}
\hline & Symmetric closed subsets $\mathbf{T}^{\mathbf{r}}\left(\mathbf{T}^{\boldsymbol{u}}=\mathbf{0}\right)$ & Isomorphism class \\
\hline 29 & $\alpha_{1},-\alpha_{1}$ & $A_{1}$ \\
\hline 30 & $\alpha_{1}, \alpha_{2}, \alpha_{1}+\alpha_{2},-\alpha_{1},-\alpha_{2},-\alpha_{1}-\alpha_{2}$ & $A_{2}$ \\
\hline 31 & $\alpha_{1}, \alpha_{3},-\alpha_{1},-\alpha_{3}$ & $A_{1} \times A_{1}$ \\
\hline 32 & $\Phi$ & $A_{3}$ \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 3. The symmetric closed subsets of the root system $A_{3}$.}
\end{table}

\begin{table}
\begin{tabular}[t]{|l|l|}
\hline & Special closed subsets $\mathbf{T}^{\mathbf{u}}\left(\mathbf{T}^{\mathbf{r}}=\mathbf{0}\right)$ \\
\hline 1 & $\Phi^{+}$ \\
\hline 2 & $\alpha_{1}, \alpha_{2}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{2}+2 \alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3}$ \\
\hline 3 & $\alpha_{2}, \alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{2}+2 \alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3}$ \\
\hline 4 & $\alpha_{1}, \alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{2}+2 \alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3}$ \\
\hline 5 & $\alpha_{1}, \alpha_{2}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{2}+2 \alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3}$ \\
\hline 6 & $\alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{2}+2 \alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3}$ \\
\hline 7 & $\alpha_{1}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{2}+2 \alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3}$ \\
\hline 8 & $\alpha_{2}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{2}+2 \alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3}$ \\
\hline 9 & $\alpha_{1}, \alpha_{2}, \alpha_{1}+\alpha_{2}, \alpha_{2}+2 \alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3}$ \\
\hline 10 & $\alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{2}+2 \alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3}$ \\
\hline 11 & $\alpha_{1}, \alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{2}+2 \alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3}$ \\
\hline 12 & $\alpha_{1}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3}$ \\
\hline 13 & $\alpha_{2}, \alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{2}+2 \alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3}$ \\
\hline 14 & $\alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{2}+2 \alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3}$ \\
\hline 15 & $\alpha_{3}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{2}+2 \alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3}$ \\
\hline 16 & $\alpha_{1}, \alpha_{1}+\alpha_{2}, \alpha_{2}+2 \alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3}$ \\
\hline 17 & $\alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3}$ \\
\hline 18 & $\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{2}+2 \alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3}$ \\
\hline 19 & $\alpha_{2}, \alpha_{1}+\alpha_{2}, \alpha_{2}+2 \alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3}$ \\
\hline 20 & $\alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3}$ \\
\hline 21 & $\alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{2}+2 \alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3}$ \\
\hline 22 & $\alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3}$ \\
\hline 23 & $\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{2}+2 \alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3}$ \\
\hline 24 & $\alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}$ \\
\hline 25 & $\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3}$ \\
\hline 26 & $\alpha_{1}+\alpha_{2}, \alpha_{2}+2 \alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3}$ \\
\hline 27 & $\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3}$ \\
\hline 27 & $\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3}$ \\
\hline 29 & $\alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{2}+2 \alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3}$ \\
\hline 30 & $\alpha_{1}, \alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3}$ \\
\hline 31 & $\alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3}$ \\
\hline 32 & $\alpha_{2}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3}$ \\
\hline 33 & $\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{2}+2 \alpha_{3}$ \\
\hline 34 & $\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}$ \\
\hline 35 & $\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3}$ \\
\hline 36 & $\alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}$ \\
\hline 37 & $\alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3}$ \\
\hline 38 & $\alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3}$ \\
\hline 39 & $\alpha_{2}+2 \alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3}$ \\
\hline 40 & $\alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{2}+2 \alpha_{3}$ \\
\hline 41 & $\alpha_{2}, \alpha_{2}+2 \alpha_{3}$ \\
\hline 42 & $\alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}$ \\
\hline 43 & $\alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3}$ \\
\hline 44 & $\alpha_{1}+\alpha_{2}+\alpha_{3}$ \\
\hline 45 & $\alpha_{2}+2 \alpha_{3}$ \\
\hline 46 & $\alpha_{1}, \alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3},-\alpha_{2}$ \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 4. The special closed subsets of the root system $B_{3}$.}
\end{table}

\begin{table}
\begin{tabular}[t]{|l|l|}
\hline & Levi decomposable closed subsets $\mathbf{T}^{\mathbf{r}} \oplus \mathbf{T}^{\mathbf{u}}\left(\mathbf{T}^{\mathbf{r}}, \mathbf{T}^{\mathbf{u}} \neq \mathbf{0}\right)$ \\
\hline 47 & $\alpha_{1}, \alpha_{2}, \alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{2}+2 \alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3},-\alpha_{3}$ \\
\hline 48 & $\alpha_{1}, \alpha_{2}, \alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{2}+2 \alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3},-\alpha_{1}$ \\
\hline 49 & $\alpha_{1}, \alpha_{2}, \alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{2}+2 \alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3},-\alpha_{2}$ \\
\hline 50 & $\alpha_{1}, \alpha_{2}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{2}+2 \alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3},-\alpha_{1}$ \\
\hline 51 & $\alpha_{2}, \alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{2}+2 \alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3},-\alpha_{3}$ \\
\hline 52 & $\alpha_{1}, \alpha_{2}, \alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{2}+2 \alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3},-\alpha_{1},-\alpha_{3}$ \\
\hline 53 & $\alpha_{1}, \alpha_{2}, \alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{2}+2 \alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3},-\alpha_{2}$ \\
\hline 54 & $\alpha_{1}, \alpha_{2}, \alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{2}+2 \alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3},-\alpha_{1},-\alpha_{2},-\alpha_{1}-\alpha_{2}$ \\
\hline 55 & $\alpha_{1}, \alpha_{3}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{2}+2 \alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3},-\alpha_{1}$ \\
\hline 56 & $\alpha_{1}, \alpha_{2}, \alpha_{1}+\alpha_{2}, \alpha_{2}+2 \alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3},-\alpha_{2}$ \\
\hline 57 & $\alpha_{1}, \alpha_{2}, \alpha_{1}+\alpha_{2}, \alpha_{2}+2 \alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3},-\alpha_{1}$ \\
\hline 58 & $\alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{2}+2 \alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3},-\alpha_{1}-\alpha_{2}$ \\
\hline 59 & $\alpha_{1}, \alpha_{2}, \alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{2}+2 \alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3},-\alpha_{2},-\alpha_{3},-\alpha_{2}-\alpha_{3},-\alpha_{2}-2 \alpha_{3}$ \\
\hline 60 & $\alpha_{1}, \alpha_{2}, \alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3},-\alpha_{2}$ \\
\hline 61 & $\alpha_{1}, \alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3},-\alpha_{3}$ \\
\hline 62 & $\alpha_{1}, \alpha_{2}, \alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{2}+2 \alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3},-\alpha_{2},-\alpha_{2}-2 \alpha_{3}$ \\
\hline 63 & $\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{2}+2 \alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3},-\alpha_{2}$ \\
\hline 64 & $\alpha_{1}, \alpha_{2}, \alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3},-\alpha_{2}$ \\
\hline 65 & $\alpha_{1}, \alpha_{2}, \alpha_{1}+\alpha_{2}, \alpha_{2}+2 \alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3},-\alpha_{2},-\alpha_{2}-2 \alpha_{3}$ \\
\hline 66 & $\alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3},-\alpha_{3}$ \\
\hline 67 & $\alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3},-\alpha_{1}-\alpha_{2}$ \\
\hline 68 & $\alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3},-\alpha_{3}$ \\
\hline 69 & $\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3},-\alpha_{2}$ \\
\hline 70 & $\alpha_{1}, \alpha_{2}, \alpha_{1}+\alpha_{2}, \alpha_{2}+2 \alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3},-\alpha_{1},-\alpha_{2},-\alpha_{1}-\alpha_{2}$ \\
\hline 71 & $\alpha_{1}, \alpha_{2}+2 \alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3},-\alpha_{1}$ \\
\hline 72 & $\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{2}+2 \alpha_{3},-\alpha_{2}$ \\
\hline 73 & $\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{2}+2 \alpha_{3},-\alpha_{1}-\alpha_{2}-\alpha_{3}$ \\
\hline 74 & $\alpha_{2}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3},-\alpha_{2}$ \\
\hline 75 & $\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3},-\alpha_{2}$ \\
\hline 76 & $\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{2}+2 \alpha_{3},-\alpha_{2},-\alpha_{2}-2 \alpha_{3}$ \\
\hline 77 & $\alpha_{2}, \alpha_{2}+2 \alpha_{3},-\alpha_{2}$ \\
\hline 78 & $\alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{2}+2 \alpha_{3},-\alpha_{1}-\alpha_{2}-\alpha_{3}$ \\
\hline 79 & $\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{2}+2 \alpha_{3},-\alpha_{2},-\alpha_{1}-\alpha_{2}-\alpha_{3}$ \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 5. The Levi decomposable closed subsets of the root system $B_{3}$.}
\end{table}

\begin{table}
\begin{tabular}[t]{|l|l|l|}
\hline & Symmetric closed subsets $\mathbf{T}^{\mathbf{r}}\left(\mathbf{T}^{\mathbf{u}}=\mathbf{0}\right)$ & Isomorphism class \\
\hline 80 & $\alpha_{1},-\alpha_{1}$ & $A_{1}$ \\
\hline 81 & $\alpha_{3},-\alpha_{3}$ & $A_{1}$ \\
\hline 82 & $\alpha_{1}, \alpha_{3},-\alpha_{1},-\alpha_{3}$ & $A_{1} \times A_{1}$ \\
\hline 83 & $\alpha_{1}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3},-\alpha_{1},-\alpha_{1}-2 \alpha_{2}-2 \alpha_{3}$ & $A_{1} \times A_{1}$ \\
\hline 84 & $\alpha_{1}, \alpha_{2}, \alpha_{1}+\alpha_{2},-\alpha_{1},-\alpha_{2},-\alpha_{1}-\alpha_{2}$ & $A_{2}$ \\
\hline 85 & $$\begin{gathered}
\alpha_{1}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3}, \\
-\alpha_{1},-\alpha_{2}-\alpha_{3},-\alpha_{1}-\alpha_{2}-\alpha_{3},-\alpha_{1}-2 \alpha_{2}-2 \alpha_{3}
\end{gathered}$$ & $B_{2}$ \\
\hline 86 & $\alpha_{1}, \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3},-\alpha_{1},-\alpha_{3},-\alpha_{1}-2 \alpha_{2}-2 \alpha_{3}$ & $A_{1} \times A_{1} \times A_{1}$ \\
\hline 87 & $$\begin{gathered}
\alpha_{1}, \alpha_{2}, \alpha_{1}+\alpha_{2}, \alpha_{2}+2 \alpha_{3}, \alpha_{1}+\alpha_{2}+2 \alpha_{3}, \alpha_{1}+2 \alpha_{2}+2 \alpha_{3}, \\
-\alpha_{1},-\alpha_{2},-\alpha_{1}-\alpha_{2},-\alpha_{2}-2 \alpha_{3},-\alpha_{1}-\alpha_{2}-2 \alpha_{3},-\alpha_{1}-2 \alpha_{2}-2 \alpha_{3}
\end{gathered}$$ & $A_{3}$ \\
\hline 88 & $\Phi$ & $B_{3}$ \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 6. The symmetric closed subsets of the root system $B_{3}$.}
\end{table}

\begin{table}
\begin{tabular}[t]{|l|l|}
\hline & Special closed subsets $\mathbf{T}^{\mathbf{u}}\left(\mathbf{T}^{\mathbf{r}}=\mathbf{0}\right)$ \\
\hline 1 & $\Phi^{+}$ \\
\hline 2 & $\alpha_{2}, \alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, 2 \alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3}$ \\
\hline 3 & $\alpha_{1}, \alpha_{2}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, 2 \alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3}$ \\
\hline 4 & $\alpha_{1}, \alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, 2 \alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3}$ \\
\hline 5 & $\alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, 2 \alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3}$ \\
\hline 6 & $\alpha_{1}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, 2 \alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3}$ \\
\hline 7 & $\alpha_{1}, \alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, 2 \alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3}$ \\
\hline 8 & $\alpha_{2}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, 2 \alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3}$ \\
\hline 9 & $\alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3}$ \\
\hline 10 & $\alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, 2 \alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3}$ \\
\hline 11 & $\alpha_{1}, \alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, 2 \alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3}$ \\
\hline 12 & $\alpha_{1}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3}$ \\
\hline 13 & $\alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, 2 \alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3}$ \\
\hline 14 & $\alpha_{3}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, 2 \alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3}$ \\
\hline 15 & $\alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, 2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3}$ \\
\hline 16 & $\alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3}$ \\
\hline 17 & $\alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3}$ \\
\hline 18 & $\alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, 2 \alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3}$ \\
\hline 19 & $\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, 2 \alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3}$ \\
\hline 20 & $\alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, 2 \alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3}$ \\
\hline 21 & $\alpha_{3}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3}$ \\
\hline 22 & $\alpha_{1}, \alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3}$ \\
\hline 23 & $\alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3}$ \\
\hline 24 & $\alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3}$ \\
\hline 25 & $\alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, 2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3}$ \\
\hline 26 & $\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, 2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3}$ \\
\hline 27 & $\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, 2 \alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}$ \\
\hline 28 & $\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3}$ \\
\hline 29 & $\alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3}$ \\
\hline 30 & $\alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3}$ \\
\hline 31 & $\alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}$ \\
\hline 32 & $\alpha_{3}, 2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3}$ \\
\hline 33 & $\alpha_{1}+\alpha_{2}+\alpha_{3}, 2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3}$ \\
\hline 34 & $\alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3}$ \\
\hline 35 & $\alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3}$ \\
\hline 36 & $\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3}$ \\
\hline 37 & $\alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}$ \\
\hline 38 & $\alpha_{1}+\alpha_{2}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3}$ \\
\hline 39 & $\alpha_{1}+\alpha_{2}+\alpha_{3}, 2 \alpha_{2}+\alpha_{3}$ \\
\hline 40 & $2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3}$ \\
\hline 41 & $\alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}$ \\
\hline 42 & $\alpha_{1}+\alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3}$ \\
\hline 43 & $\alpha_{1}+\alpha_{2}+\alpha_{3}$ \\
\hline 44 & $2 \alpha_{2}+\alpha_{3}$ \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 7. The special closed subsets of the root system $C_{3}$.}
\end{table}

\begin{table}
\begin{tabular}[t]{|l|l|}
\hline & Levi decomposable closed subsets $\mathbf{T}^{\mathbf{r}} \oplus \mathbf{T}^{\mathbf{u}}\left(\mathbf{T}^{\mathbf{r}}, \mathbf{T}^{\mathbf{u}} \neq \mathbf{0}\right)$ \\
\hline 45 & $\alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3},-\alpha_{3}$ \\
\hline 46 & $\alpha_{1}, \alpha_{2}, \alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, 2 \alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3},-\alpha_{1}$ \\
\hline 47 & $\alpha_{1}, \alpha_{2}, \alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, 2 \alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3},-\alpha_{3}$ \\
\hline 48 & $\alpha_{1}, \alpha_{2}, \alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, 2 \alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3},-\alpha_{2}$ \\
\hline 49 & $\alpha_{1}, \alpha_{2}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, 2 \alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3},-\alpha_{1}$ \\
\hline 50 & $\alpha_{2}, \alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, 2 \alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3},-\alpha_{3}$ \\
\hline 51 & $\alpha_{1}, \alpha_{2}, \alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, 2 \alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3},-\alpha_{1},-\alpha_{3}$ \\
\hline 52 & $\alpha_{1}, \alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, 2 \alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3},-\alpha_{3}$ \\
\hline 53 & $\alpha_{1}, \alpha_{2}, \alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, 2 \alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3},-\alpha_{1},-\alpha_{2},-\alpha_{1}-\alpha_{2}$ \\
\hline 54 & $\alpha_{1}, \alpha_{3}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, 2 \alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3},-\alpha_{1}$ \\
\hline 55 & $\alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, 2 \alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3},-\alpha_{3}$ \\
\hline 56 & $\alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3},-\alpha_{1}-\alpha_{2}$ \\
\hline 57 & $\alpha_{1}, \alpha_{2}, \alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, 2 \alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3},-\alpha_{2},-\alpha_{3},-\alpha_{2}-\alpha_{3},-2 \alpha_{2}-\alpha_{3}$ \\
\hline 58 & $\alpha_{1}, \alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3},-\alpha_{3}$ \\
\hline 59 & $\alpha_{1}, \alpha_{2}, \alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3},-\alpha_{2}$ \\
\hline 60 & $\alpha_{1}, \alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, 2 \alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3},-\alpha_{3},-2 \alpha_{2}-\alpha_{3}$ \\
\hline 61 & $\alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, 2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3},-2 \alpha_{2}-\alpha_{3}$ \\
\hline 62 & $\alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, 2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3},-\alpha_{3}$ \\
\hline 63 & $\alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, 2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3},-\alpha_{1}-\alpha_{2}$ \\
\hline 64 & $\alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3},-\alpha_{3}$ \\
\hline 65 & $\alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, 2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3},-2 \alpha_{2}-\alpha_{3}$ \\
\hline 66 & $\alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, 2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3},-\alpha_{3},-2 \alpha_{2}-\alpha_{3}$ \\
\hline 67 & $\alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3},-\alpha_{1}-\alpha_{2}$ \\
\hline 68 & $\alpha_{3}, \alpha_{1}+\alpha_{2}+\alpha_{3}, 2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3},-2 \alpha_{2}-\alpha_{3}$ \\
\hline 69 & $\alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, 2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3},-\alpha_{1}-\alpha_{2},-2 \alpha_{2}-\alpha_{3}$ \\
\hline 70 & $\alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3},-\alpha_{2}-\alpha_{3}$ \\
\hline 71 & $\alpha_{3}, 2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3},-\alpha_{3}$ \\
\hline 72 & $\alpha_{1}+\alpha_{2}, \alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3},-\alpha_{1}-\alpha_{2}$ \\
\hline 73 & $\alpha_{1}+\alpha_{2}+\alpha_{3}, 2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3},-2 \alpha_{2}-\alpha_{3}$ \\
\hline 74 & $\alpha_{1}+\alpha_{2}+\alpha_{3}, 2 \alpha_{2}+\alpha_{3},-2 \alpha_{2}-\alpha_{3}$ \\
\hline 75 & $\alpha_{3}, \alpha_{1}+\alpha_{2}, \alpha_{1}+\alpha_{2}+\alpha_{3}, 2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3},-\alpha_{3},-\alpha_{1}-\alpha_{2},-\alpha_{1}-\alpha_{2}-\alpha_{3},-2 \alpha_{1}-2 \alpha_{2}-\alpha_{3}$ \\
\hline 76 & $\alpha_{3}, 2 \alpha_{2}+\alpha_{3},-\alpha_{3}$ \\
\hline 77 & $\alpha_{1}+\alpha_{2}, 2 \alpha_{2}+\alpha_{3},-\alpha_{1}-\alpha_{2}$ \\
\hline 78 & $\alpha_{3}, 2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3},-\alpha_{3},-2 \alpha_{1}-2 \alpha_{2}-\alpha_{3}$ \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 8. The Levi decomposable closed subsets of the root system $C_{3}$.}
\end{table}

\begin{table}
\begin{tabular}[t]{|l|l|l|}
\hline & Symmetric closed subsets $\mathbf{T}^{\mathbf{r}}\left(\mathbf{T}^{\mathbf{u}}=\mathbf{0}\right)$ & Isomorphism class \\
\hline 79 & $\alpha_{1},-\alpha_{1}$ & $A_{1}$ \\
\hline 80 & $\alpha_{3},-\alpha_{3}$ & $A_{1}$ \\
\hline 81 & $\alpha_{1}, \alpha_{3},-\alpha_{1},-\alpha_{3}$ & $A_{1} \times A_{1}$ \\
\hline 82 & $\alpha_{3}, 2 \alpha_{2}+\alpha_{3},-\alpha_{3},-2 \alpha_{2}-\alpha_{3}$ & $A_{1} \times A_{1}$ \\
\hline 83 & $\alpha_{1}, \alpha_{2}, \alpha_{1}+\alpha_{2},-\alpha_{1},-\alpha_{2},-\alpha_{1}-\alpha_{2}$ & $A_{2}$ \\
\hline 84 & $$\begin{gathered}
\alpha_{1}, 2 \alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3}, \\
-\alpha_{1},-2 \alpha_{2}-\alpha_{3},-\alpha_{1}-2 \alpha_{2}-\alpha_{3},-2 \alpha_{1}-2 \alpha_{2}-\alpha_{3}
\end{gathered}$$ & $B_{2}$ \\
\hline 85 & $\alpha_{3}, 2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3},-\alpha_{3},-2 \alpha_{2}-\alpha_{3},-2 \alpha_{1}-2 \alpha_{2}-\alpha_{3}$ & $A_{1} \times A_{1} \times A_{1}$ \\
\hline 86 & $$\begin{gathered}
\alpha_{1}, \alpha_{3}, 2 \alpha_{2}+\alpha_{3}, \alpha_{1}+2 \alpha_{2}+\alpha_{3}, 2 \alpha_{1}+2 \alpha_{2}+\alpha_{3}, \\
-\alpha_{1},-\alpha_{3},-2 \alpha_{2}-\alpha_{3},-\alpha_{1}-2 \alpha_{2}-\alpha_{3},-2 \alpha_{1}-2 \alpha_{2}-\alpha_{3}
\end{gathered}$$ & $A_{1} \times B_{2}$ \\
\hline 87 & $\Phi$ & $C_{3}$ \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 9. The symmetric closed subsets of the root system $C_{3}$.}
\end{table}