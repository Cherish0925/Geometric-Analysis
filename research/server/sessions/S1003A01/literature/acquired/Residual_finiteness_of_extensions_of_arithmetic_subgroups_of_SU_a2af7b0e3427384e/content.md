---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 2203_14793.pdf
converter: mathpix
format: mmd
---

\title{
Residual finiteness of extensions of arithmetic subgroups of $\operatorname{SU}(d, 1)$ with cusps
}

\author{
Richard M. Hill \\ University College London \\ r.m.hill@ucl.ac.uk
}

\begin{abstract}
Let $\Gamma$ be an arithmetic subgroup of $\operatorname{SU}(d, 1)$ with cusps, and let $X_{\Gamma}$ be the associated locally symmetric space. In this paper we investigate the pre-image of $\Gamma$ in the covering groups of $\operatorname{SU}(d, 1)$. Let $H_{!}^{\bullet}\left(X_{\Gamma}, \mathbb{C}\right)$ be the inner cohomology, i.e. the image in $H^{\bullet}\left(X_{\Gamma}, \mathbb{C}\right)$ of the compactly supported cohomology. We prove that if the first inner cohomology group $H_{!}^{1}\left(X_{\Gamma}, \mathbb{C}\right)$ is non-zero then the pre-image of $\Gamma$ in each connected cover of $\operatorname{SU}(d, 1)$ is residually finite. At the end of the paper we give an example of an arithmetic subgroup $\Gamma$ satisfying the criterion $H_{!}^{1}\left(X_{\Gamma}, \mathbb{C}\right) \neq 0$.
\end{abstract}

Keywords: Arithmetic group, residual finiteness, cohomology, ball quotient.

Mathematics Subject Classification: 11F06, 11F75, 20E26.

Competing Interests: None.

\section*{1 Introduction}

Let $\Gamma$ be an arithmetic subgroup of $\operatorname{SU}(d, 1)$ for some $d \geq 2$. The universal cover $\widetilde{\operatorname{SU}(d, 1)}$ of $\operatorname{SU}(d, 1)$ is an infinite cyclic cover, so that we have a central extension
$$1 \rightarrow \mathbb{Z} \rightarrow \widetilde{\mathrm{SU}(d, 1)} \rightarrow \operatorname{SU}(d, 1) \rightarrow 1 .$$
Furthermore, for every positive integer $n$, there is a unique connected $n$-fold cover of $\operatorname{SU}(d, 1)$, which is isomorphic to $\widetilde{\operatorname{SU}(d, 1)} / n \mathbb{Z}$. Let $\tilde{\Gamma}^{(n)}$ be the pre-image of $\Gamma$ in the connected $n$-fold cover, and let $\tilde{\Gamma}$ be the pre-image of $\Gamma$ in the universal cover. In this paper, we shall investigate whether the groups $\tilde{\Gamma}$ and $\tilde{\Gamma}^{(n)}$ are residually finite. There are two motivations for studying this question.
\begin{itemize}
\item[1.] It is a famous open question whether every word-hyperbolic group is residually finite. If all such groups are indeed residually finite, then every $\tilde{\Gamma}^{(n)}$ must be residually finite. This would imply that $\tilde{\Gamma}$ is also residually finite.
\end{itemize}
\begin{itemize}
\item[2.] If $\tilde{\Gamma}^{(n)}$ is residually finite, then for every sufficiently large integer $m$, there exist modular forms on $\operatorname{SU}(d, 1)$ of weight $\frac{m}{n}$ whose level is a subgroup of finite index in $\Gamma$. The existence of such modular forms is discussed in [9], and some examples of the forms (of weight $\frac{1}{3}$ ) have recently been described in [5].
\end{itemize}

The question of whether $\tilde{\Gamma}$ and $\tilde{\Gamma}^{(n)}$ are residually finite has recently been studied in [13], [9] [14] and [5]. In both [9], and [14], it is is shown (independently) that for a certain class of cocompact arithmetic subgroups $\Gamma$, the groups $\tilde{\Gamma}$ and $\tilde{\Gamma}^{(n)}$ are residually finite. In the current paper, we give some evidence that a similar result might be true when $\Gamma$ has cusps.

To put our result in context, we first recall a theorem from [9] and [14]. Let $k$ be a CM field of degree $[k: \mathbb{Q}]=2 e$. Choose a $(d+1) \times(d+1)$ Hermitian matrix $J$ with entries in $k$, such that
\begin{itemize}
\item[-] The matrix $J$ has signature is $(d, 1)$ at one of the complex places of $k$;
\item[-] For each of the other $e-1$ complex places of $k$, the matrix $J$ is either positive definite or negative definite.
\end{itemize}
Given such a matrix $J$, we define an algebraic group $\mathbb{G}$ over $\mathbb{Q}$ by
$$\mathbb{G}(A)=\left\{g \in \operatorname{SL}_{d+1}\left(A \otimes_{\mathbb{Q}} k\right): \bar{g}^{t} J g=J\right\},$$
for any commutative $\mathbb{Q}$-algebra $A$. We shall regard $\mathbb{G}(\mathbb{Q})$ as a subgroup of $\mathbb{G}(\mathbb{R}) \times \mathbb{G}\left(\mathbb{A}_{f}\right)$, where $\mathbb{A}_{f}$ is the ring of finite adèles of $\mathbb{Q}$. We have an isomorphism $\mathbb{G}(\mathbb{R}) \cong \operatorname{SU}(d, 1) \times \operatorname{SU}(d+1)^{e-1}$. Given any compact open subgroup $K_{f} \subset \mathbb{G}\left(\mathbb{A}_{f}\right)$, we let $\Gamma\left(K_{f}\right)$ be the group of elements of $\mathbb{G}(\mathbb{Q})$, which project into $K_{f}$. The projection of $\Gamma\left(K_{f}\right)$ in $\operatorname{SU}(d, 1)$ is called a congruence subgroup of $\operatorname{SU}(d, 1)$ of the first kind. Any subgroup of $\operatorname{SU}(d, 1)$ which is commensurable with $\Gamma\left(K_{f}\right)$ is called an arithmetic subgroup of the first kind.

Theorem 1 ([9],[14]). Let $\Gamma$ be an arithmetic subgroup of $\operatorname{SU}(d, 1)$ of the first kind, constructed using a CM field $k$ with $[k: \mathbb{Q}]>2$. Then the groups $\tilde{\Gamma}$ and $\tilde{\Gamma}^{(n)}$ are residually finite.

It is not known whether the theorem extends to the case $[k: \mathbb{Q}]=2$, and this is the question which we investigate in this paper. The case $[k: \mathbb{Q}]=2$ is geometrically different from the case $e \geq 2$, since the groups $\Gamma$ are cocompact for $[k: \mathbb{Q}]>2$ but have cusps in the case $[k: \mathbb{Q}]=2$.

To describe our result, let $X_{\Gamma}$ be the locally symmetric space corresponding to $\Gamma$. We shall write $H_{!}^{1}\left(X_{\Gamma}, \mathbb{C}\right)$ for the image in $H^{1}\left(X_{\Gamma}, \mathbb{C}\right)$ of the cohomology of compact support $H_{\text {compact }}^{1}\left(X_{\Gamma}, \mathbb{C}\right)$. We prove the following result:
Theorem 2. Let $\Gamma$ be an arithmetic subgroup of $\operatorname{SU}(d, 1)$ with cusps (i.e. constructed from an complex quadratic field $k$ ). Assume that there exists an arithmetic subgroup $\Gamma^{\prime}$ commensurable with $\Gamma$ such that $H_{!}^{1}\left(X_{\Gamma^{\prime}}, \mathbb{C}\right) \neq 0$. Then the groups $\tilde{\Gamma}$ and $\tilde{\Gamma}^{(n)}$ are all residually finite.

We'll briefly discuss the hypothesis that $H_{!}^{1}\left(X_{\Gamma^{\prime}}, \mathbb{C}\right) \neq 0$. The cuspidal cohomology is contained in the inner cohomology (see [8]), so if $H^{1}\left(X_{\Gamma^{\prime}}, \mathbb{C}\right)$ contains any non-zero cusp forms then the hypothesis of Theorem 2 holds. Furthermore, it is known (see for example [11]) that there exists a congruence subgroup $\Gamma^{\prime}$, such that $H^{1}\left(X_{\Gamma^{\prime}}, \mathbb{C}\right) \neq 0$. However, the hypothesis of Theorem 2 is that $H_{!}^{1}\left(X_{\Gamma^{\prime}}, \mathbb{C}\right) \neq 0$ and this is rather stronger. We shall give an example of a group satisfying this hypothesis at the end of the paper; the author is extremely grateful to Matthew Stover for suggesting this example.

Here are some equivalent formulations of the hypothesis:

Proposition 1. Let $\Gamma$ be a neat arithmetic subgroup of $\operatorname{SU}(d, 1)$ of the first kind with cusps. Let $\omega \in H^{2}\left(X_{\Gamma}, \mathbb{C}\right)$ be the cohomology class represented by the invariant Kähler form on the symmetric space attached to $\operatorname{SU}(d, 1)$. Then the following are equivalent:
\begin{itemize}
\item[1.] $H_{!}^{1}\left(X_{\Gamma}, \mathbb{C}\right) \neq 0$;
\item[2.] $H_{!}^{2 d-1}\left(X_{\Gamma}, \mathbb{C}\right) \neq 0$;
\item[3.] There exists $\phi \in H^{1}\left(X_{\Gamma}, \mathbb{C}\right)$ such that $\phi \cup \omega^{d-1} \neq 0$ in $H^{2 d-1}\left(X_{\Gamma}, \mathbb{C}\right)$.
\end{itemize}
(Here we are writing $\cup$ for the cup product operation.)
The equivalence of 1 and 2 is by duality (see (2)). The equivalence of 2 and 3 follows immediately from Lemma 10 below. In this context, it is reassuring to note that $\omega^{d-1}$ represents a non-zero cohomology class in $H^{2 d-2}\left(X_{\Gamma}, \mathbb{C}\right)$ (see Lemma 6 below).

The paper is organized as follows. In section 2, we recall a purely group theoretical lemma, which gives a method for showing that certain extension groups are residually finite. In section 3, we recall some standard facts about the the locally symmetric spaces $X_{\Gamma}$ and their compactifications. In section 4 we prove Theorem 2. In section 5 we give an example of a group $\Gamma$ satisfying $H_{!}^{1}(\Gamma, \mathbb{C}) \neq 0$, allowing us to apply Theorem 2 in this case.

Acknowledgements The author would like to thank Matthew Stover for suggesting the example in section 5.

\section*{2 A group theoretical lemma}

The method of proof of Theorem 2 is a modification of the argument in [9]. In particular, we shall use the following lemma, which is proved in both [9], [13] and [14]. For completeness, we include a short proof.

Lemma 1. Let $G$ be a finitely generated, residually finite group, and suppose that we have a central extension
$$1 \rightarrow \mathbb{Z} \rightarrow \tilde{G} \rightarrow G \rightarrow 1 .$$
Let $\sigma_{\mathbb{Z}} \in H^{2}(G, \mathbb{Z})$ be the cohomology class of the extension, and let $\sigma_{\mathbb{C}}$ be the image of $\sigma_{\mathbb{Z}}$ in $H^{2}(G, \mathbb{C})$. Assume that there exist elements $\phi_{i}, \psi_{i} \in H^{1}(G, \mathbb{C})$ such that
$$\sigma_{\mathbb{C}}=\phi_{1} \cup \psi_{1}+\cdots+\phi_{r} \cup \psi_{r} .$$
Then $\tilde{G}$ is residually finite. Furthermore, the quotient group $\tilde{G} / n \mathbb{Z}$ is residually finite for every positive integer $n$.

Proof. Let $G^{\mathrm{ab}}=G /[G, G]$. Elements of $H^{1}(G, \mathbb{C})$ may be regarded as group homomorphisms $G \rightarrow \mathbb{C}$. Every such homomorphism is the inflation of a homomorphism $G^{\mathrm{ab}} \rightarrow \mathbb{C}$. Hence $\sigma_{\mathbb{C}}$ is also the inflation of a cohomology class on $G^{\mathrm{ab}}$, and we shall write $\widetilde{G^{\mathrm{ab}}}$ for the corresponding central extension. It follows that we have a commutative diagram with exact rows:
![](https://cdn.mathpix.com/cropped/712eeaab-ba3d-4488-b604-04478794304c-04.jpg?height=203&width=744&top_left_y=255&top_left_x=661)
We shall write $\Delta$ for the image of $\tilde{G}$ in $\widetilde{G^{\mathrm{ab}}}$. The group $\widetilde{G^{\mathrm{ab}}}$ is nilpotent. Hence $\Delta$ is a finitely generated nilpotent group, and is therefore residually finite. The group $\tilde{G}$ injects into $\Delta \times G$. Since $\Delta$ and $G$ are both residually finite, it follows that $\tilde{G}$ is residually finite. Similarly, since $\Delta / n \mathbb{Z}$ is residually finite, it follows that $\tilde{G} / n \mathbb{Z}$ is residually finite. \(\square\)

Again let $\Gamma$ be an arithmetic subgroup of $\operatorname{SU}(d, 1)$ of the first kind with cusps. Lemma 1 will be applied in the case that $G=\Gamma, \tilde{G}$ is its pre-image in $\widehat{\mathrm{SU}(d, 1)}$ and $\tilde{G} / n \mathbb{Z}=\tilde{\Gamma}^{(n)}$. We note that one may construct a different central extension of $\Gamma$ for which Lemma 1 cannot be applied. For example, take $d=2$ and let $\tau \in H^{2}(\Gamma, \mathbb{Z})$ be a cohomology class whose restriction to the Borel-Serre boundary of $X_{\Gamma}$ is non-torsion (for example an Eisenstein cohomology class, see [7]). Such a class $\tau$ cannot be expressed as a sum of cup products of elements of $H^{1}$, because all such cup products restrict to torsion on the Borel-Serre boundary.

\section*{3 Background material}

We shall now recall the construction of arithmetic subgroups of $\operatorname{SU}(d, 1)$ with cusps. Let $k$ be a complex quadratic extension of $\mathbb{Q}$; we shall identify $k$ with a subfield of $\mathbb{C}$, and we shall write $z \mapsto \bar{z}$ for complex conjugation on $\mathbb{C}$ or on $k$. Let $J_{0}$ be a $(d-1) \times(d-1)$ positive definite Hermitian matrix with entries in $k$ and let
$$J=\left(\begin{array}{ccc}
0 & 0 & 1 \\
0 & J_{0} & 0 \\
1 & 0 & 0
\end{array}\right) .$$
The matrix $J$ defines a Hermitian form on $\mathbb{C}^{n+1}$ of signature $(d, 1)$ by
$$(v, w)=\bar{v}^{t} J w,$$
where $\bar{v}^{t}$ denotes the conjugate transpose of a column matrix $v$.
We define an algebraic group $\mathbb{G}$ over $\mathbb{Q}$ to be the group of isometries in $\mathrm{SL}_{d+1}$ of the Hermitian form. More precisely, for a $\mathbb{Q}$-algebra $A$, we define
$$\mathbb{G}(A)=\left\{g \in \operatorname{SL}_{3}\left(A \otimes_{\mathbb{Q}} k\right): \bar{g}^{t} J g=J\right\} .$$
Since the matrix $J$ has signature $(d, 1)$, the group $\mathbb{G}(\mathbb{R})$ may be identified with $\operatorname{SU}(d, 1)$.
Let $\mathbb{A}_{f}$ be the ring of finite adèles of $\mathbb{Q}$. The group $\mathbb{G}\left(\mathbb{A}_{f}\right)$ is totally disconnected, and contains the projection of $\mathbb{G}(\mathbb{Q})$ as a dense subgroup (by Kneser's Strong Approximation Theorem). For a compact open subgroup $K_{f} \subset \mathbb{G}\left(\mathbb{A}_{f}\right)$, the intersection $\Gamma\left(K_{f}\right)=\mathbb{G}(\mathbb{Q}) \cap K_{f}$ is called a congruence subgroup of $\mathbb{G}(\mathbb{Q})$. Any subgroup of $\mathbb{G}(\mathbb{Q})$ which is commensurable with a congruence subgroup is called an arithmetic subgroup. It is known that there exist arithmetic subgroups of $\mathbb{G}(\mathbb{Q})$, which are not congruence subgroups.

The group $\mathbb{G}\left(\mathbb{A}_{f}\right)$ may be identified with the projective limit of the sets $\mathbb{G}(\mathbb{Q}) / \Gamma\left(K_{f}\right)$, where $\Gamma\left(K_{f}\right)$ ranges over the congruence subgroups of $\mathbb{G}(\mathbb{Q})$. We also define the arithmetic completion $\widehat{\mathbb{G}(\mathbb{Q})}$ to be the projective limit of the sets $\mathbb{G}(\mathbb{Q}) / \Gamma$, where $\Gamma$ ranges over all the arithmetic subgroups of $\mathbb{G}(\mathbb{Q})$. Since the filtration by arithmetic subgroups is invariant under conjugation, the arithmetic completion is a group, and we have a natural surjective homomorphism $\widehat{\mathbb{G}(\mathbb{Q})} \rightarrow$ $\mathbb{G}\left(\mathbb{A}_{f}\right)$. The kernel of the homomorphism is an infinite profinite group, and is called the congruence kernel $C_{\mathbb{G}}$ of $\mathbb{G}$.

An arithmetic group $\Gamma$ is said to be neat if for every $g \in \Gamma$, the eigenvalues of $g$ generate a torsion-free subgroup of $\mathbb{C}^{\times}$. For every congruence subgroup $\Gamma$, there is a neat congruence subgroup $\Gamma^{\prime}$ of finite index in $\Gamma$. Every subgroup of a neat group is neat, and every neat group is torsion-free.

\subsection*{3.1 Quotient spaces and compactifications}

Let
$$\mathcal{H}=\left\{[v] \in \mathbb{P}^{d}(\mathbb{C}):(v, v)<0\right\},$$
where we are writing $[v]$ for the point in projective space represented by a non-zero vector $v$. The complex manifold $\mathcal{H}$ has an obvious action of $\operatorname{SU}(d, 1)$, and is a model of the symmetric space attached to $\operatorname{SU}(d, 1)$. For each arithmetic subgroup $\Gamma$ in $\mathbb{G}(\mathbb{Q})$, we shall write $X=X_{\Gamma}$ for the quotient space $\Gamma \backslash \mathcal{H}$. If $\Gamma$ is neat then $X_{\Gamma}$ is a smooth, non-compact complex manifold.

By a cusp, we shall mean a point $[v]$ of $\mathbb{P}^{d}(k)$, such that $(v, v)=0$. For each such $[v]$, there is a parabolic subgroup $P_{v}$ of $\operatorname{SU}(d, 1)$, defined by
$$P_{v}=\{g \in \operatorname{SU}(d, 1):[g \cdot v]=[v]\} .$$
If $\Gamma$ is an arithmetic subgroup of $\mathbb{G}(\mathbb{Q})$, then $\Gamma$ permutes the cusps with finitely many orbits.
Assume that $[v]$ is a cusp, with corresponding parabolic subgroup $P_{v}$. We may choose a Langlands decomposition
$$P_{v}=M_{v} A_{v} N_{n},$$
where $A_{v}$ is the connected component of a split torus in $P_{v}$ which is isomorphic to $\mathbb{R}^{>0}$; the group $M_{v}$ is isomorphic to $\mathrm{U}(d-1)$, and $N_{v}$ is the unipotent radical of $P_{v}$. There is a homomorphism $\phi_{v}: P_{v} \rightarrow \mathbb{R}^{>0}$ defined by $\phi_{v}(p)=|\lambda|$, where $\lambda \in \mathbb{C}$ satisfies $p v=\lambda \cdot v$. The subgroups $M_{v}$ and $N_{n}$ are in the kernel of $\phi_{v}$, and the restriction of $\phi_{v}$ to $A_{v}$ is an isomorphism.

By the Iwasawa decomposition, the group $A_{v} \ltimes N_{v}$ acts simply transitively on the symmetric space $\mathcal{H}$, so by choosing a base point, we may identify $\mathcal{H}$ with this group.

Assume from now on that $\Gamma$ is a neat arithmetic subgroup of $\mathbb{G}(\mathbb{Q})$. For such groups $\Gamma$, the intersection $\Gamma_{v}=\Gamma \cap P_{v}$ is contained in $N_{v}$, and is a cocompact subgroup of $N_{v}$. The subgroup $\Gamma_{v}$ acts on $A_{v} \ltimes N_{v}$ by translation on $N_{v}$, preserving the $A_{v}$-coordinate. It therefore acts also on the following subset
$$A_{v}^{<\epsilon} N_{v}=\left\{a n: a \in A_{v}, n \in N_{v},\left|\phi_{v}(a)\right|<\epsilon\right\},$$
where $\epsilon$ is a positive real number. We may choose $\epsilon$ sufficiently small so that the quotient space $U_{v}=\Gamma_{v} \backslash\left(A_{v}^{<\epsilon} N_{v}\right)$ injects into $X_{\Gamma}$. We shall call such a subset $U_{v}$ of $X_{\Gamma}$ a neighbourhood of the cusp $[v]$. By reduction theory, there are finitely many non-intersecting cusp neighbourhoods
(one for each $\Gamma$-orbit of cusps), such that the complement of the cusp neighbourhoods is a compact subset of $X_{\Gamma}$.

As an example, choose the cusp $v=\left(\begin{array}{c}1 \\ 0 \\ \vdots \\ 0\end{array}\right)$. In this case $N_{v}$ is a Heisenberg group, consisting of all matrices of the form
$$n(z, x)=\left(\begin{array}{ccc}
1 & -\bar{z}^{t} J_{0} & -\frac{\|z\|^{2}}{2}+i x \\
0 & I_{n-1} & z \\
0 & 0 & 1
\end{array}\right), \quad z \in \mathbb{C}^{d-1}, x \in \mathbb{R}$$
where $\|z\|^{2}=\bar{z}^{t} J_{0} z$. We have a short exact sequence of Lie groups:
$$\begin{array}{lclclclc}
1 & \rightarrow & \mathbb{R} & \rightarrow & N_{v} & \rightarrow & \mathbb{C}^{d-1} & \rightarrow \\
& & x & \mapsto & n(0, x) & & & \\
& & & n(z, x) & \mapsto & z &
\end{array}$$
The image of $\Gamma_{v}$ in $\mathbb{C}^{d-1}$ is a full lattice $L_{v}$, and the quotient $\mathbb{C}^{d-1} / L_{v}$ is an abelian variety (indeed $L_{v}$ is commensurable with $\mathcal{O}_{k}^{d-1}$ ). The kernel of the map $\Gamma_{v} \rightarrow L_{v}$ is isomorphic to $\mathbb{Z}$. Hence the topological space $\Gamma_{v} \backslash N_{v}$ is an $\mathbb{R} / \mathbb{Z}$ bundle over the abelian variety $\mathbb{C}^{d-1} / L_{v}$. The cusp neighbourhood $U_{v}$ is the product of this space with the open interval $(0, \epsilon)$.

If we choose any other cusp $v$, then the groups $P_{v}$ and $N_{v}$ are conjuagates in $\operatorname{SU}(d, 1)$ of the subgroups described above. Hence the cusp neighbourhood has a similar description as a product of an open interval with a circle bundle over an abelian variety.

We shall consider two compactifications of $X$. The first is the Borel-Serre compactification in which we embed each cusp neighbourhood $U_{v}$ into a larger topological space $U_{v}^{\mathrm{BS}}$ as follows:
$$\begin{gathered}
U_{v}=\Gamma_{v} \backslash N_{v} \times(0, \epsilon) \\
\cap \\
U_{v}^{\mathrm{BS}}=\Gamma_{v} \backslash N_{v} \times[0, \epsilon) .
\end{gathered}$$
The embedding $U_{v} \rightarrow U_{v}^{\mathrm{BS}}$ is evidently a homotopy equivalence. Therefore the resulting compactification $X^{\text {BS }}$ has the same cohomology groups as $X$.

We shall write $\partial X^{\mathrm{BS}}$ for the complement of $X$ in its Borel-Serre compactification. The boundary of the Borel-Serre compactification is a disjoint union of manifolds homeomorphic to
$$\partial X_{v}^{\mathrm{BS}}=\Gamma_{v} \backslash N_{v} .$$
Each of the boundary components $\partial X_{v}^{\mathrm{BS}}$ is a circle bundle over an abelian variety.
The second compactification which we shall consider is the smooth compactification $\tilde{X}$ constructed in [1]. This may be obtained from the Borel-Serre compactification by quotienting each boundary component $\Gamma_{v} \backslash N_{v}$ by the centre of $N_{v}$, i.e. by the subgroup of matrices of the form $n(0, x)$. The resulting boundary component is the abelian variety
$$\partial \tilde{X}_{v}=\mathbb{C}^{d-1} / L_{v} .$$

The compactification $\tilde{X}$ is a smooth complex manifold but is not homotopic to to $X$. There is an obvious projection map $X^{\mathrm{BS}} \rightarrow \tilde{X}$.

We shall write $\partial \tilde{X}$ for the complement of $X$ in its smooth compactification. This boundary set $\partial \tilde{X}$ is the disjoint union of the abelian varieties $\partial \tilde{X}_{v}$.

\subsection*{3.2 Cohomology groups}

In this paper we shall use various cohomology groups. For convenience, we list the notation and some standard properties for each of these. In almost all cases we shall consider cohomology with coefficients in $\mathbb{C}$. In such cases, we shall not always write in the coefficients.
\begin{itemize}
\item[-] The continuous cohomology groups of the group $\operatorname{SU}(d, 1)$ will be written $H_{\text {cts }}^{\bullet}(\operatorname{SU}(d, 1),-)$. We may identify $H_{\text {cts }}^{r}(\operatorname{SU}(d, 1), \mathbb{C})$ with the vector space of differential $r$-forms on $\mathcal{H}$, which are invariant under the action of $\operatorname{SU}(d, 1)$ (see [2]).
For example, there is an invariant Kähler form $\omega$ on $\mathcal{H}$. The form $\omega$ generates $H_{\text {cts }}^{2}(\operatorname{SU}(d, 1), \mathbb{C})$. More generally we have
$$H_{\mathrm{cts}}^{r}(\mathrm{SU}(1, d), \mathbb{C})= \begin{cases}\mathbb{C} \cdot \omega^{r / 2} & \text { if } r=0,2,4, \ldots, 2 d \\ 0 & \text { otherwise }\end{cases}$$
\item[-] The measurable cohomology groups (see [10]) of a connected Lie group $G$ will be written $H_{\text {meas }}^{\bullet}(G,-)$. For a connected Lie group $G$ with fundamental group $\pi_{1}(G)$, there is a canonical isomorphism $H_{\text {meas }}^{2}(G, \mathbb{Z}) \cong \operatorname{Hom}\left(\pi_{1}(G), \mathbb{Z}\right)$.
In particular, the group $\operatorname{SU}(d, 1)$ has fundamental group $\mathbb{Z}$, so we have $H_{\text {meas }}^{2}(\operatorname{SU}(d, 1), \mathbb{Z}) \cong$ $\mathbb{Z}$. We shall choose a generator $\sigma_{\mathbb{Z}}$ for this group, i.e.
$$H_{\text {meas }}^{2}(\mathrm{SU}(d, 1), \mathbb{Z})=\mathbb{Z} \cdot \sigma_{\mathbb{Z}} .$$
The group extension of $\operatorname{SU}(d, 1)$ corresponding to the cocycle $\sigma_{\mathbb{Z}}$ is the universal cover of $\operatorname{SU}(d, 1)$.
By [15] there is an isomorphism
$$H_{\mathrm{cts}}^{\bullet}(G, \mathbb{C}) \cong H_{\mathrm{meas}}^{\bullet}(G, \mathbb{Z}) \otimes \mathbb{C} .$$
In particular, the image of $\sigma_{\mathbb{Z}}$ in $H_{\text {cts }}^{2}(\operatorname{SU}(d, 1), \mathbb{C})$ is a non-zero multiple of $\omega$.
\item[-] For an arithmetic subgroup $\Gamma$, the Eilenberg-MacLane cohomology groups will be written $H^{\bullet}(\Gamma,-)$. There are restriction maps $H_{\text {cts }}^{r}(\mathrm{SU}(d, 1), \mathbb{C}) \rightarrow H^{r}(\Gamma, \mathbb{C})$. Some of these maps are injective and others are zero. (In fact, we'll see in Lemma 6 that the map is injective if $r<2 d$ and zero if $r=2 d$ ).
\item[-] If $\Gamma$ is a neat arithmetic subgroup of $\operatorname{SU}(d, 1)$, then the quotient space $X=\Gamma \backslash \mathcal{H}$ is a complex $d$-dimensional manifold. We shall write $H^{\bullet}(X)$ for the singular or de Rham cohomology groups of this manifold with complex coefficients.
Apart from the manifold $X$, we shall also consider two compactifications $X^{\mathrm{BS}}$ and $\tilde{X}$.
\end{itemize}

Recall that there are canonical isomorphisms
$$H^{\bullet}\left(X^{\mathrm{BS}}\right) \cong H^{\bullet}(X) \cong H^{\bullet}(\Gamma, \mathbb{C}) .$$
The composition
$$H_{\mathrm{cts}}^{\bullet}(\mathrm{SU}(d, 1), \mathbb{C}) \xrightarrow{\text { Rest }} H^{\bullet}(\Gamma, \mathbb{C}) \cong H^{\bullet}(X),$$
takes an invariant differential form on $\mathcal{H}$ to its de Rham cohomology class on $X$.
\begin{itemize}
\item[-] We shall write $c_{1}(X)$ for the first Chern class of the canonical sheaf on $X$, regarded as an element of $H^{2}(X)$. It is known that $c_{1}(X)$ is a multiple of the cohomology class $\omega$ by a positive real number.
\item[-] We shall write $H_{\text {compact }}^{\bullet}(X)$ for the compactly supported cohomology of $X$ with complex coefficients. The space $H_{\text {compact }}^{2 d}(X)$ is one-dimensional, and the cup-product map
$$\cup: H^{r}(X) \otimes H_{\text {compact }}^{2 d-r}(X) \rightarrow H_{\text {compact }}^{2 d}(X) \cong \mathbb{C}$$
is a perfect pairing, allowing us to identify $H^{r}(X)$ with the dual space of $H_{\text {compact }}^{2 d-r}(X)$.
\item[-] We shall write $\partial X^{\mathrm{BS}}$ and $\partial \tilde{X}$ for the boundaries of the compactifications. The relative cohomology groups $H^{\bullet}\left(X^{\mathrm{BS}}, \partial X^{\mathrm{BS}}\right)$ and $H^{\bullet}(\tilde{X}, \partial \tilde{X})$ are both canonically isomorphic to the compactly supported cohomology. We therefore have a commutative diagram whose rows are long exact sequences:
![](https://cdn.mathpix.com/cropped/712eeaab-ba3d-4488-b604-04478794304c-08.jpg?height=221&width=1506&top_left_y=1334&top_left_x=331)
We shall write $H_{!}^{\bullet}(X)$ for the kernel of the restriction map $H^{\bullet}(X) \rightarrow H^{\bullet}\left(\partial X^{\mathrm{BS}}\right)$, or equivalently the image of the map $H_{\text {compact }}^{\bullet}(X) \rightarrow H^{\bullet}(X)$. The vector spaces $H_{!}^{\bullet}(X)$ are known as the inner cohomology groups.
\item[-] For $r=0, \ldots, 2 d$ there is a perfect pairing (see [8]):
$$\langle-,-\rangle: H_{!}^{r}(X) \otimes H_{!}^{2 d-r}(X) \rightarrow H_{\text {compact }}^{2 d}(X) \cong \mathbb{C},$$
defined as follows. Given $a \in H_{!}^{r}(X)$ and $b \in H_{!}^{2 d-r}(X)$, we may choose a pre-image $a_{\text {compact }} \in H_{\text {compact }}^{r}(X)$ of $a$. The pairing $\langle a, b\rangle$ is defined to be the cup product $a_{\text {compact }} \cup b$. This cup product does not depend on the choice of $a_{\text {compact }}$.
\item[-] We shall use the notation
$$H_{\text {stable }}^{\bullet}=\underset{\Gamma^{\prime}}{\lim _{\longrightarrow}} H^{\bullet}\left(X_{\Gamma^{\prime}}\right), \quad H_{!, \text {stable }}^{\bullet}=\underset{\Gamma^{\prime}}{\lim } H_{!}^{\bullet}\left(X_{\Gamma^{\prime}}\right), \quad H_{\text {compact,stable }}^{\bullet}=\underset{\Gamma^{\prime}}{\lim } H_{\text {compact }}^{\bullet}\left(X_{\Gamma^{\prime}}\right),$$
where the limits are taken over all arithmetic subgroups $\Gamma^{\prime}$ of $\Gamma$. These direct limits may be regarded as unions, since all of the connecting homomorphisms are injective.
There is an obvious action of $\mathbb{G}(\mathbb{Q})$ on the vector spaces $H_{\text {stable }}^{\bullet}$ and $H_{!, \text {stable }}^{\bullet}$, and this action extends to a smooth action of the totally disconnected group $\widehat{\mathbb{G}(\mathbb{Q})}$.
\end{itemize}
\begin{itemize}
\item[-] Since cup products are compatible with restriction maps, the pairing (2) extends to a perfect pairing
$$H_{!, \text {stable }}^{r} \otimes H_{!, \text {stable }}^{2 d-r} \rightarrow H_{\text {compact,stable }}^{2 d} \cong \mathbb{C}$$
This pairing is $\widehat{\mathbb{G}(\mathbb{Q})}$-invariant, in the sense that
$$\langle g a, g b\rangle=\langle a, b\rangle \quad \text { for all } g \in \widehat{\mathbb{G}(\mathbb{Q})} \text {. }$$
\item[-] There is also an invariant positive definite inner product on $H_{!, \text {stable }}^{r}$ defined by
$$\langle\langle a, b\rangle\rangle=\langle a, * b\rangle,$$
(see page 73 of [8]). In particular, the representation $H_{!, \text {stable }}^{r}$ of $\widehat{\mathbb{G}(\mathbb{Q})}$ is semi-simple.
\item[-] We shall use the notation
$$H_{!, \text {Cong. }}^{\bullet}=\underset{K_{f}}{\lim _{\longrightarrow}} H_{!}^{\bullet}\left(X_{\Gamma\left(K_{f}\right)}\right),$$
where the limit is taken over all congruence subgroups $\Gamma\left(K_{f}\right)$. There is a smooth action of $\mathbb{G}\left(\mathbb{A}_{f}\right)$ on the vector space $H_{!, \text {Cong }}^{\bullet}$, and we may identify $H_{!, \text {Cong }}^{\bullet}$ with the subspace of invariants $\left(H_{!, \text {stable }}^{\bullet}\right)^{C_{\mathbb{G}}}$, where $C_{\mathbb{G}}$ is the congruence kernel of $\mathbb{G}$.
\item[-] The vector space $H_{!, \text {Cong. }}^{\bullet}$ is a semi-simple representation of $\mathbb{G}\left(\mathbb{A}_{f}\right)$. More precisely there is a countable direct sum decomposition (see [8]):
$$H_{!, \text {Cong. }}^{r}=\bigoplus_{\pi \in \Pi_{!}^{r}} H_{\mathrm{cts}}^{r}\left(\mathrm{SU}(d, 1), \pi_{\infty}\right) \otimes \pi_{f},$$
where $\Pi_{!}^{r}$ is a certain set of automorphic representations of $\mathbb{G}(\mathbb{A})$. Each of the automorphic representations $\pi$ decomposes as $\pi_{\infty} \otimes \pi_{f}$, where $\pi_{\infty}$ is a simple representation of $\operatorname{SU}(d, 1)$ and $\pi_{f}$ is a smooth, simple representation of $\mathbb{G}\left(\mathbb{A}_{f}\right)$.
\item[-] We shall be particularly interested in the subspace $\left(H_{!, \text {stable }}^{\bullet}\right) \widehat{\mathbb{G}(\mathbb{Q})}$ of $\widehat{\mathbb{G}(\mathbb{Q})}$-invariant cohomology classes. Since $\left(H_{!, \text {stable }}^{\bullet}\right)^{C_{\mathrm{G}}}=H_{!, \text {Cong }}^{\bullet}$, it follows that
$$\left(H_{!, \text {stable }}^{\bullet}\right)^{\widehat{\mathbb{G}(\mathbb{Q})}}=\left(H_{!, \text {Cong. }}^{\bullet}\right)^{\mathbb{G}\left(\mathbb{A}_{f}\right)} .$$
The right hand side of (4) may be evaluated using (3). The trivial representation $\mathbb{C}$ occurs with multiplicity at most 1 in each set $\Pi_{!}^{r}$. For all non-trivial representations $\pi$ in $\Pi_{!}^{r}$, the vector space $\pi_{f}$ is infinite dimensional. This implies
$$\left(H_{!, \text {stable }}^{r}\right)^{\widehat{\mathbb{G}(\mathbb{Q})}} \cong \begin{cases}H_{\text {cts }}^{r}(\mathrm{SU}(d, 1), \mathbb{C}) & \text { if the trivial representation is in } \Pi_{!}^{r}, \\ 0 & \text { otherwise. }\end{cases}$$
By the discussion above, if $\left(H_{!, \text {stable }}^{r}\right)^{\widehat{G(\mathbb{Q})}}$ is non-zero, then $r$ is even and this space is spanned by the cohomology class of $\omega^{r / 2}$ on $X_{\Gamma}$ (or more accurately, by the image of this cohomology class in the direct limit $H_{\text {stable }}^{r}$ ).
\end{itemize}

Lemma 2. Let $\Gamma$ be an arithmetic subgroup of $\mathbb{G}(\mathbb{Q})$. The invariant Kähler form $\omega$ represents a non-zero cohomology class on $X_{\Gamma}$. Consequently, the restriction of $\sigma_{\mathbb{Z}}$ to $\Gamma$ is a non-zero element of $H^{2}(\Gamma, \mathbb{Z})$.
(Here we are using the assumption that $d \geq 2$; the statement would be false for SU(1, 1).)
Proof. Since $\omega$ is a multiple of the image of $\sigma_{\mathbb{Z}}$, it is sufficient to prove the statement for $\omega$. It is also sufficient to prove the result with $\Gamma$ sufficiently small. We may therefore assume, without loss of generality, that $\Gamma$ is neat. Hence $X$ is a smooth complex manifold.

Suppose for a moment that there exists a compact Riemann surface $Y \subset X$. The Kähler form $\omega$ restricts to a Kähler form on $Y$, and by positivity of Kähler forms (see for example [6]) we have
$$\int_{[Y]} \omega>0 .$$
Therefore $\omega$ represents a non-zero cohomology class on $Y$, and hence also on $X$.
It is therefore sufficient to find a compact Riemann surface $Y$ contained in $X$. The folloing construction of such a $Y$ is taken from [11]. We may choose a 2-dimensional subspace $S \subset k^{d+1}$, such that the Hermitian form has signature $(1,1)$ on $S$ and is anisotropic. Let $G$ be the group of isometries of $S \otimes_{\mathbb{Q}} \mathbb{R}$. Our choice of $S$ implies that $G$ is isomorphic to $\operatorname{SU}(1,1)$ and $\Gamma \cap G$ is cocompact in $G$. Let $Y$ be the locally symmetric space corresponding to the subgroup $\Gamma \cap G$ of $G$. The inclusion of $G$ in $\operatorname{SU}(d, 1)$ gives us an inclusion of $Y$ in $X$ as a compact Riemann surface. \(\square\)

Lemma 3. Let $\Gamma$ be a neat arithmetic subgroup of $\mathbb{G}(\mathbb{Q})$. For any cusp $[v]$, the restrictions of $\sigma_{\mathbb{Z}}$ and $\omega$ to $\Gamma_{v}$ are coboundaries.

Proof. As $\omega$ is a multiple of the image of $\sigma_{\mathbb{Z}}$ in $H_{\text {cts }}^{2}(\mathrm{SU}(d, 1), \mathbb{C})$, it is sufficient to prove the result for $\sigma_{\mathbb{Z}}$. Since $\Gamma$ is neat, we have $\Gamma_{v} \subset N_{v}$. Therefore the restriction map $H_{\text {meas }}^{2}(\operatorname{SU}(d, 1), \mathbb{Z}) \rightarrow$ $H^{2}\left(\Gamma_{v}, \mathbb{Z}\right)$ factors through the group $H_{\text {meas }}^{2}\left(N_{v}, \mathbb{Z}\right)$. Since the Lie group $N_{v}$ is simply connected, we have $H_{\text {meas }}^{2}\left(N_{v}, \mathbb{Z}\right)=0$. Therefore the restriction of $\sigma_{\mathbb{Z}}$ to $\Gamma_{v}$ is zero. \(\square\)

Lemma 4. Let $\Gamma$ be a neat arithmetic subgroup of $\mathbb{G}(\mathbb{Q})$ and let $X=X_{\Gamma}$. The image of $\omega$ in $H^{2}(X)$ is in the subspace $H_{!}^{2}(X)$ of inner cohomology classes.

Proof. It is sufficient to show that the class $\omega$ vanishes on each Borel-Serre boundary component $\partial X_{v}^{\mathrm{BS}}$. This follows from Lemma 3, in view of the following commutative diagram.
$$\begin{aligned}
H^{2}\left(X^{\mathrm{BS}}\right) & \longrightarrow H^{2}\left(\partial X_{v}^{\mathrm{BS}}\right) \\
& { }_{\| 2} \\
H^{2}(\Gamma, \mathbb{C}) & \longrightarrow H^{2}\left(\Gamma_{v}, \mathbb{C}\right)
\end{aligned}$$ \(\square\)

Lemma 5. The vector space $\left(H_{!, \text {stable }}^{2}\right)^{\widehat{G(\mathbb{Q})}}$ is one-dimensional, and is spanned by the cohomology class of the invariant Kähler form $\omega$ on $X_{\Gamma}$.

Proof. By (5), the space $\left(H_{!, \text {stable }}^{2}\right)^{\widehat{G(\mathbb{Q})}}$ is at most one-dimensional, so it is sufficient to show that $\omega$ is a non-zero element in this space. Lemma 4 shows that $\omega$ is in the subspace of inner cohomology classes, and Lemma 2 implies that $\omega$ represents a non-zero cohomology class on $X_{\Gamma}$ for every arithmetic subgroup $\Gamma$. \(\square\)

Lemma 6. Let $\Gamma$ be an arithmetic subgroup of $\mathbb{G}(\mathbb{Q})$. For $r=1, \ldots, d-1$, the $2 r$-form $\omega^{r}$ represents a non-zero cohomology class on $X_{\Gamma}$, which spans $\left(H_{!, \text {stable }}^{2 r}\right)^{\widehat{\mathbb{G}(\mathbb{Q})}}$.

Proof. By Lemma 5, the representation $H_{!, \text {stable }}^{2}$ of $\widehat{\mathbb{G}(\mathbb{Q})}$ has a trivial 1-dimensional subrepresentation spanned by $\omega$. Hence by duality, $H_{!\text {,stable }}^{2 d-2}$ has a trivial 1-dimensional quotient representation. By semi-simplicity, it follows that $\left(H_{!, \text {stable }}^{2 d-2}\right) \widehat{\mathbb{G}(\mathbb{Q})}$ is non-zero. By the discussion above, $\left(H_{!, \text {stable }}^{2 d-2}\right) \widehat{\mathbb{G}(\mathbb{Q})}$ is one-dimensional, and is spanned by $\omega^{d-1}$. In particular, $\omega^{d-1}$ represents a non-zero cohomology class on $X_{\Gamma}$. From this, it follows that $\omega^{r}$ represents a non-zero cohomology class on $X_{\Gamma}$ for $1 \leq r \leq d-1$. The image of $\omega^{r}$ in $H_{!, \text {stable }}^{2 r}$ spans a trivial one-dimensional subrepresentation. Therefore $\left(H_{!, \text {stable }}^{2 r}\right)^{\widehat{G(\mathbb{Q})}} \neq 0$. By the discussion above, $\left(H_{!, \text {stable }}^{2 r}\right)^{\widehat{G(\mathbb{Q})}}$ is spanned by $\omega^{r}$. \(\square\)

Proposition 2. Let $\Gamma$ be a neat arithmetic subgroup of $\mathbb{G}(\mathbb{Q})$ and let $X=X_{\Gamma}$. Then there exists an element $\tilde{\omega} \in H^{2}(\tilde{X})$, such that
\begin{itemize}
\item[-] the restriction of $\tilde{\omega}$ to $X$ is the invariant Kähler form $\omega$.
\item[-] $\tilde{\omega}$ is in the ample cone in $H^{1,1}(\tilde{X})$.
\end{itemize}

Proof. The lemma does not depend on our choice of normalization of $\omega$; we shall assume for simplicity that $\omega=c_{1}(X)$ in $H^{2}(X)$.

Let $\tilde{\omega}=c_{1}(\tilde{X})+\epsilon \cdot[\partial \tilde{X}]$, where $c_{1}(\tilde{X})$ is the first Chern class of the canonical sheaf on $\tilde{X}$, and $\epsilon$ is a positive real number. Here we are writing $[\partial \tilde{X}]$ for the Poincaré dual of the $2 d-2$-cycle $\partial \tilde{X}$, or equivalently the first Chern class of the line bundle corresponding the the divisor $\partial \tilde{X}$. It is shown in [3], that if $\epsilon$ is sufficiently small then $\tilde{\omega}$ is in the ample cone. By naturality of Chern classes, it follows that the restriction of $c_{1}(\tilde{X})$ to $X$ is $c_{1}(X)$, which we are assuming is equal to $\omega$. The restriction of the divisor $\partial \tilde{X}$ to $X$ is 0; hence the restriction of $[\partial \tilde{X}]$ to $X$ is 0 . It follows that the restriction of $\tilde{\omega}$ to $X$ is $\omega$. \(\square\)

\section*{4 Proof of Theorem 1}

Fix a neat arithmetic subgroup $\Gamma \subset \mathbb{G}(\mathbb{Q})$ and let $X$ be the quotient space $\Gamma \backslash \mathcal{H}$. We shall let $\tilde{X}$ denote the smooth compactification of $X$. We shall write $\partial \tilde{X}$ for the union of the boundary components of $\tilde{X}$. Each boundary component is an abelian variety. We choose a neighbourhood $\tilde{U}$ of $\partial \tilde{X}$, so that $\partial \tilde{X}$ is a deformation retract of $\tilde{U}$. We shall also write $U$ for the intersection $\tilde{U} \cap X$. Note that $U$ is homotopic to the Borel-Serre boundary of $X$. The Mayer-Vietoris sequence for the cover $\tilde{X}=X \cup \tilde{U}$ takes the form:
$$\rightarrow H^{n}(\tilde{X}) \rightarrow H^{n}(X) \oplus H^{n}(\partial \tilde{X}) \rightarrow H^{n}\left(\partial X^{\mathrm{BS}}\right) \rightarrow H^{n+1}(\tilde{X}) \rightarrow .$$

Let $[v] \in \mathbb{P}^{d}(k)$ be a cusp, and let $N_{v}$ be the unipotent radical in the parabolic subgroup fixing $[v]$. Recall that we have a central group extension:
$$1 \rightarrow \mathbb{R} \rightarrow N_{v} \rightarrow \mathbb{C}^{d-1} \rightarrow 1 .$$
We shall write $\Gamma_{v}$ for the intersection of $\Gamma$ with $N_{v}$. We also let $L_{v}$ be the image of $\Gamma_{v}$ in $\mathbb{C}^{d-1}$ and $Z_{v}$ be the kernel of the map $\Gamma_{v} \rightarrow L_{v}$.

The next three lemmas are well known (for example, see [7]). We include proofs for the sake of completeness.

Lemma 7. The restriction map $H^{1}\left(\Gamma_{v}, \mathbb{C}\right) \rightarrow H^{1}\left(Z_{v}, \mathbb{C}\right)$ is zero.
Proof. We shall regard elements of $H^{1}(\Gamma, \mathbb{C})$ as group homomorphisms $\phi: \Gamma_{v} \rightarrow \mathbb{C}$. We must prove that $\phi(g)=0$ for all elements $g \in Z_{v}$. For any such $g$, there is a positive integer $n$ such that $g^{n} \in\left[\Gamma_{v}, \Gamma_{v}\right]$. Therefore $\phi(g)=\frac{1}{n} \phi\left(g^{n}\right)=0$. \(\square\)

Lemma 8. The pullback map $H^{1}(\partial \tilde{X}) \rightarrow H^{1}\left(\partial X^{\mathrm{BS}}\right)$ is an isomorphism.
Proof. It is sufficient to show that for each cusp $v$, the pullback $H^{1}\left(\partial \tilde{X}_{v}\right) \rightarrow H^{1}\left(\partial X_{v}^{\mathrm{BS}}\right)$ is an isomorphism. Recall that $\partial \tilde{X}_{v}$ is an abelian variety $\mathbb{C}^{d-1} / L_{v}$, and $\partial X_{v}^{\mathrm{BS}}$ is a circle bundle over this abelian variety, homeomorphic to $\Gamma_{v} \backslash N_{v}$. We shall write $Z_{v}$ for the kernel of the homomorphism $\Gamma_{v} \rightarrow L_{v}$. We therefore have a commutative diagram
$$\begin{aligned}
H^{1}\left(\partial \tilde{X}_{v}\right) & \longrightarrow H^{1}\left(\partial X_{v}^{\mathrm{BS}}\right) \\
\text { ॥ } 2 & \text { ॥ } 2 \\
0 \longrightarrow H^{1}\left(L_{v}, \mathbb{C}\right) & \longrightarrow H^{1}\left(\Gamma_{v}, \mathbb{C}\right) \longrightarrow H^{1}\left(Z_{v}, \mathbb{C}\right),
\end{aligned}$$
where the bottom row is the inflation-restriction sequence in group cohomology. The result now follows from Lemma 7. \(\square\)

Lemma 9. The restriction map gives an isomorphism $H^{1}(\tilde{X}) \cong H^{1}(X)$.
Proof. Consider the following section of the Mayer-Vietoris sequence (6):
$$H^{0}(X) \oplus H^{0}(\partial \tilde{X}) \rightarrow H^{0}\left(\partial X^{\mathrm{BS}}\right) \rightarrow H^{1}(\tilde{X}) \rightarrow H^{1}(X) \oplus H^{1}(\partial \tilde{X}) \rightarrow H^{1}\left(\partial X^{\mathrm{BS}}\right) .$$
The map $H^{0}(\partial \tilde{X}) \rightarrow H^{0}\left(\partial X^{\mathrm{BS}}\right)$ is clearly an isomorphism. By Lemma 8, the pull-back map $H^{1}(\partial \tilde{X}) \rightarrow H^{1}\left(\partial X^{\mathrm{BS}}\right)$ is an isomorphism. Hence $H^{1}(\tilde{X}) \cong H^{1}(X)$. \(\square\)

Lemma 10. The map $H^{1}(X) \rightarrow H^{2 d-1}(X)$ given by cup product with $\omega^{d-1}$ has image $H_{!}^{2 d-1}(X)$.
Proof. By Proposition 2, there exists an ample class $\tilde{\omega} \in H^{2}(\tilde{X})$, whose restriction to $X$ is the class $\omega$. We have a commutative diagram:
![](https://cdn.mathpix.com/cropped/712eeaab-ba3d-4488-b604-04478794304c-12.jpg?height=219&width=885&top_left_y=2288&top_left_x=591)
where the vertical maps are given by cup product with $\tilde{\omega}^{d-1}$ and $\omega^{d-1}$ respectively. The bottom row is exact, as it is part of the Mayer-Vietoris sequence (6). Note that $H^{2 d-1}(\partial \tilde{X})=0$ because $\partial \tilde{X}$ has dimension $2 d-2$.

The diagram is commutative because the restriction of $\tilde{\omega}$ to $X$ is $\omega$. Since $\tilde{\omega}$ is ample, the Hard Lefschetz Theorem implies that the left hand vertical map is an isomorphism. Therefore the image of the right hand vertical map is $H_{!}^{2 d-1}(X)$. \(\square\)

Lemma 11. Assume $H_{!}^{1}(X) \neq 0$. Then there exist $\phi \in H_{!}^{1}(X)$ and $\psi \in H^{1}(X)$ such that $\left\langle\phi \cup \psi, \omega^{d-1}\right\rangle \neq 0$.
Proof. Choose a non-zero $\phi \in H_{!}^{1}(X)$. Then there exists an element $\phi^{*} \in H_{!}^{2 d-1}(X)$, such that $\left\langle\phi, \phi^{*}\right\rangle \neq 0$. By Lemma 10, we have $\phi^{*}=\psi \cup \omega^{d-1}$ for some $\psi \in H^{1}(X)$.

By Lemma 4 we have $\omega \in H_{!}^{2}(X)$, so we may choose a pre-image $\omega_{\text {compact }}$ of $\omega$ in $H_{\text {compact }}^{2}(X)$. By definition of the pairing $\langle-,-\rangle$ in (2), we have
$$\begin{aligned}
\left\langle\phi \cup \psi, \omega^{d-1}\right\rangle & =(\phi \cup \psi) \cup \omega_{\text {compact }}^{d-1} \\
& =\phi \cup\left(\psi \cup \omega_{\text {compact }}^{d-1}\right) \\
& =\left\langle\phi, \psi \cup \omega^{d-1}\right\rangle \\
& =\left\langle\phi, \phi^{*}\right\rangle \\
& \neq 0 .
\end{aligned}$$
In the third equality above, we have used the fact that $\psi \cup \omega_{\text {compact }}^{d-1} \in H_{\text {compact }}^{2 d-1}(X)$ is a pre-image of the element $\psi \cup \omega^{d-1} \in H_{!}^{2 d-1}(X)$. \(\square\)

Theorem. Let $\Gamma$ be an arithmetic subgroup of $\operatorname{SU}(d, 1)$ with cusps (i.e. constructed from an complex quadratic field $k$ ). Assume that there exists an arithmetic subgroup $\Gamma^{\prime}$ commensurable with $\Gamma$ such that $H_{!}^{1}\left(X_{\Gamma^{\prime}}\right) \neq 0$. Then the groups $\tilde{\Gamma}$ and $\tilde{\Gamma}^{(n)}$ are all residually finite.
Proof. Consider the subspace $V$ of $H_{!\text {,stable }}^{2}$ spanned by cup products $\phi \cup \psi$ with $\phi \in H_{\text {stable }}^{1}$ and $\psi \in H_{!, \text {stable }}^{1}$. We have a linear map
$$\Phi: V \rightarrow \mathbb{C}, \quad \Phi(\Sigma)=\left\langle\Sigma, \omega^{d-1}\right\rangle .$$
The map $\Phi$ is a morphism of $\widehat{\mathbb{G}(\mathbb{Q})}$ representations because $\omega$ is $\widehat{\mathbb{G}(\mathbb{Q})}$-invariant. Using our assumption on $\Gamma^{\prime}$, Lemma 11 shows that $\Phi$ is surjective. Therefore $V$ has a 1-dimensional trivial quotient. Since $H_{!, \text {stable }}^{2}$ is semi-simple, $V$ must have a 1-dimensional trivial subrepresentation. By Lemma 5, $\left(H_{!, \text {stable }}^{2} \widehat{\mathbb{G}(\mathbb{Q})}\right.$ is spanned by $\omega$. Therefore $\omega \in V$. In other words, there exist elements $\phi_{i} \in H_{\text {stable }}^{1}$ and $\psi_{i} \in H_{!, \text {stable }}^{1}$ such that
$$\omega=\phi_{1} \cup \psi_{1}+\cdots+\phi_{r} \cup \psi_{r} .$$
Choose an arithmetic subgroup $\Gamma^{\prime \prime}$ of sufficiently high level, so that all of the elements $\phi_{i}$ and $\psi_{i}$ are images in the direct limit of elements of $H^{1}\left(X^{\prime \prime}\right)$, where $X^{\prime \prime}=\Gamma^{\prime \prime} \backslash \mathcal{H}$. Then (7) holds in $H^{2}\left(X^{\prime \prime}\right)$.

The group extension $\widetilde{\mathrm{SU}}(d, 1)$ of $\mathrm{SU}(d, 1)$ is represented by the cocycle $\sigma_{\mathbb{Z}} \in H_{\text {meas }}^{2}(\mathrm{SU}(d, 1), \mathbb{Z})$. We shall write $\sigma_{\mathbb{C}}$ for the image of $\sigma_{\mathbb{Z}}$ in $H_{\text {cts }}^{2}(\operatorname{SU}(d, 1), \mathbb{C})$. Recall that $\sigma_{\mathbb{C}}$ is a multiple of $\omega$. By (7) the restriction of $\sigma_{\mathbb{C}}$ to $\Gamma^{\prime \prime}$ is a sum of cup products of elements of $H^{1}\left(\Gamma^{\prime \prime}, \mathbb{C}\right)$. This means that the restriction of $\sigma_{\mathbb{Z}}$ to $\Gamma^{\prime \prime}$ satisfies the hypothesis of Lemma 1. By Lemma 1, the groups $\tilde{\Gamma}^{\prime \prime}$ and ${\tilde{\Gamma^{\prime \prime}}}^{(n)}$ are all residually finite. Since $\tilde{\Gamma} \cap \tilde{\Gamma^{\prime \prime}}$ has finite index in $\tilde{\Gamma}$ and $\tilde{\Gamma} \cap \tilde{\Gamma^{\prime \prime}}{ }^{(n)}$ has finite index in $\tilde{\Gamma}^{(n)}$, it follows that $\tilde{\Gamma}$ and $\tilde{\Gamma}^{(n)}$ are also residually finite. \(\square\)

\section*{5 Non-vanishing of the first inner cohomology}

In this section, we give an example of an arithmetic subgroup $\Gamma$ of $\operatorname{SU}(2,1)$ with cusps, for which $H_{!}^{1}\left(X_{\Gamma}, \mathbb{C}\right) \neq 0$. This demonstrates that the hypothesis of Theorem 2 is satisfied in at least one case. The construction which we describe here was suggested to the author by Matthew Stover, and is a modification of his construction of the towers $C_{j}$ in section 5 of [12].

We begin with the Deligne-Mostow group $\Gamma_{\mu}$, where $\mu=\left(\frac{2}{6}, \frac{2}{6}, \frac{3}{6}, \frac{4}{6}, \frac{1}{6}\right)$ (see [4]). The group $\Gamma_{\mu}$ is an arithmetic subgroup od SU $(2,1)$ with cusps (see the table on page 86 of [4]). It is known (see section 5 of [12]) that there is a finite index subgroup $\Gamma^{\prime} \subseteq \Gamma_{\mu}$ for which there exists a surjective homomorphism
$$f: \Gamma^{\prime} \rightarrow \Sigma,$$
where $\Sigma$ is a hyperbolic surface group, i.e. the fundamental group of a compact Riemann surface of genus at least 2. The next theorem shows that whenever such a homomorphism $f$ exists, the hypothesis of Theorem 2 is true.

Theorem 3. Let $\Gamma$ be an arithmetic subgroup of $\operatorname{SU}(d, 1)$ with cusps. Assume that there exists a surjective homomorphism $\Gamma \rightarrow \Sigma$, where $\Sigma$ is a hyperbolic surface group. Then there exists an arithmetic subgroup $\Gamma^{\prime} \subset \Gamma$, such that $H_{!}^{1}\left(X_{\Gamma^{\prime}}, \mathbb{C}\right) \neq 0$.

In the rest of this section, we shall prove Theorem 3 in a series of lemmata. We shall assume from now on that $\Gamma$ is an arithmetic subgroup of $\operatorname{SU}(d, 1)$ with cusps, and that we have a surjective homomorphism $f: \Gamma \rightarrow \Sigma$, where $\Sigma$ is a hyperbolic surface group. Replacing $\Gamma$ and $\Sigma$ by finite index subgroups if necessary, we shall assume that $\Gamma$ is torsion-free.

For a technical reason (in the proof of Lemma 16 below) it will be more convenient in this section to work with cohomology with coefficients in $\mathbb{R}$.

Recall that the cusps of $\Gamma$ are the elements $[v] \in \mathbb{P}^{d}(k)$ such that $(v, v)=0$, where $(-,-)$ is the Hermitian form of signature $(d, 1)$. In what follows, we shall abuse notation slightly by writing $v$ for a cusp, rather than $[v]$. Let $v$ be a cusp of $\Gamma$, and let $\Gamma_{v}$ be the stabilizer of $v$ in $\Gamma$. Since $\Gamma$ is torsion-free, the subgroup $\Gamma_{v}$ is contained in the Heisenberg group $N_{v}$, and is a cocompact lattice in $N_{v}$. In particular, the restriction map gives an isomorphism $H_{\text {cts }}^{1}\left(N_{v}, \mathbb{R}\right) \cong H^{1}\left(\Gamma_{v}, \mathbb{R}\right)$.

Given any subgroup $\Sigma^{\prime}$ of finite index in $\Sigma$, there is a linear map $R_{\Sigma^{\prime}, v}: H^{1}\left(\Sigma^{\prime}, \mathbb{R}\right) \rightarrow$ $H_{\text {cts }}^{1}\left(N_{v}, \mathbb{R}\right)$, defined as the following composition:
$$R_{\Sigma^{\prime}, v}: H^{1}\left(\Sigma^{\prime}, \mathbb{R}\right) \xrightarrow{f^{*}} H^{1}\left(\Gamma^{\prime}, \mathbb{R}\right) \xrightarrow{\text { Rest }} H^{1}\left(\Gamma_{v}^{\prime}, \mathbb{R}\right) \cong H_{\text {cts }}^{1}\left(N_{v}, \mathbb{R}\right) .$$
Where $\Gamma^{\prime}=f^{-1}\left(\Sigma^{\prime}\right)$. If $\Sigma^{\prime \prime} \subseteq \Sigma^{\prime}$ is a subgroup of finite index, then we have $R_{\Sigma^{\prime}, v}=R_{\Sigma^{\prime \prime}, v} \circ$ Rest, where Rest : $H^{1}\left(\Sigma^{\prime}, \mathbb{R}\right) \rightarrow H^{1}\left(\Sigma^{\prime \prime}, \mathbb{R}\right)$ is the restriction map, so we actually have a map
$$R_{v}: \lim _{\rightarrow} H^{1}\left(\Sigma^{\prime}, \mathbb{R}\right) \rightarrow H_{\mathrm{cts}}^{1}\left(N_{v}, \mathbb{R}\right),$$
where the direct limit is taken over all subgroups $\Sigma^{\prime}$ of finite index in $\Sigma$. Since the restriction maps $H^{1}\left(\Sigma^{\prime}, \mathbb{R}\right) \rightarrow H^{1}\left(\Sigma^{\prime \prime}, \mathbb{R}\right)$ are injective, the direct limit above may be regarded as a union of an increasing sequence of finite dimensional vector spaces.

We shall call $v$ an essential cusp is the map $R_{v}$ is non-zero. This is equivalent to saying that there exists a subgroup $\Sigma^{\prime}$ of finite index in $\Sigma$, such that the map $R_{\Sigma^{\prime}, v}$ is non-zero. Note that if $R_{\Sigma^{\prime}, v}$ is non-zero then $R_{\Sigma^{\prime \prime}, v}$ is non-zero for each subgroup $\Sigma^{\prime \prime} \subseteq \Sigma^{\prime}$.

Lemma 12. Let $\Sigma^{\prime}$ be a normal subgroup of finite index in $\Sigma$. If $R_{\Sigma^{\prime}, v}$ is non-zero, then for all $g \in \Gamma$ the map $R_{\Sigma^{\prime}, g v}$ is non-zero.
Proof. Assume that $R_{\Sigma^{\prime}, v}$ is non-zero. Choose an element $\phi \in H^{1}\left(\Sigma^{\prime}, \mathbb{C}\right)$ such that $R_{\Sigma^{\prime}, v}(\phi) \neq 0$. In other words, $\phi: \Sigma^{\prime} \rightarrow \mathbb{C}$ is a homomorphism and the composition
$$\Gamma_{v}^{\prime} \hookrightarrow \Gamma^{\prime} \xrightarrow{f} \Sigma^{\prime} \xrightarrow{\phi} \mathbb{C}$$
is non-zero. Choose an element $n \in \Gamma_{v}^{\prime}$ whose image in $\mathbb{C}$ is non-zero.
Define $\psi \in H^{1}\left(\Sigma^{\prime}, \mathbb{C}\right)$ by $\psi(\sigma)=\phi\left(f(g)^{-1} \sigma f(g)\right)$. The element $n^{\prime}=g n g^{-1}$ is in $\Gamma_{g v}^{\prime}$, and we have
$$\psi\left(f\left(n^{\prime}\right)\right)=\phi(f(n)) \neq 0 .$$
Therefore $R_{\Sigma^{\prime}, g v}(\psi) \neq 0$. \(\square\)

Lemma 13. Let $\Sigma^{\prime}$ be a subgroup of finite index in $\Sigma$ and let $\Gamma^{\prime}$ be the pre-image of $\Sigma^{\prime}$ in $\Gamma$. For all $g \in \Gamma^{\prime}$ and all cusps $v$ we have $\operatorname{ker}\left(R_{\Sigma^{\prime}, g v}\right)=\operatorname{ker}\left(R_{\Sigma^{\prime}, v}\right)$.
Proof. Let $\phi \in \operatorname{ker}\left(R_{\Sigma^{\prime}, v}\right)$. This means that $\phi: \Sigma^{\prime} \rightarrow \mathbb{C}$ is a homomorphism and $\phi(f(n))=0$ for all $n \in \Gamma_{v}^{\prime}$. If $n^{\prime} \in \Gamma_{g v}^{\prime}$ then we have $n^{\prime}=g n g^{-1}$ for some $n \in \Gamma_{v}^{\prime}$. This implies
$$\phi\left(f\left(n^{\prime}\right)\right)=\phi(f(g))+\phi(f(n))-\phi(f(g))=0 .$$
Hence $\phi \in \operatorname{ker} R_{\Sigma^{\prime}, g v}$. The converse is proved in the same way, replacing $g$ by $g^{-1}$. \(\square\)

Lemma 14. If $v$ and $w$ are cusps and $w=g v$ for some $g \in \Gamma$ then $v$ is essential if and only if $w$ is essential.

Proof. This follows immediately from Lemma 12. \(\square\)

Lemma 15. There exists a normal subgroup $\Sigma_{0}$ of finite index in $\Sigma$, such that for each essential cusp $v$, the map $R_{\Sigma_{0}, v}$ is non-zero.

Proof. Let $v_{1}, \ldots, v_{r}$ be a set of representatives for the $\Gamma$-orbits of the essential cusps. For each $i$, we may choose a normal subgroup $\Sigma_{i}$ of $\Sigma$, such that $R_{\Sigma_{i}, v_{i}}$ is non-zero. We shall prove the lemma with $\Sigma_{0}=\Sigma_{1} \cap \cdots \cap \Sigma_{r}$. Suppose $w$ is any essential cusp. By Lemma 14 we have $w=g v_{i}$ for some $g \in \Gamma$. By Lemma 12 the map $R_{\Sigma_{i}, w}$ is non-zero. Since $\Sigma_{0} \subseteq \Sigma_{i}$, it follows that $R_{\Sigma_{0}, w}$ is non-zero. \(\square\)

Lemma 16. Let $\Sigma_{0}$ be chosen as in Lemma 15 and let $\Gamma_{0}$ be the pre-image of $\Sigma_{0}$ in $\Gamma$. There exists a surjective homomorphism $\rho: \Sigma_{0} \rightarrow \mathbb{Z}$, such that for every essential cusp $v$, the composition $\rho \circ f: \Gamma_{0} \rightarrow \mathbb{Z}$ is non-zero on $\Gamma_{0, v}$.

Proof. Note that $\rho \circ f$ is non-zero on $\Gamma_{0, v}$ if and only if $R_{\Sigma_{0}, v}(\rho) \neq 0$. We must therefore show that there is an element of $H^{1}\left(\Sigma_{0}, \mathbb{Z}\right)$ which is not in the kernel of $R_{\Sigma_{0}, v}$ for any essential cusp $v$.

Let $v_{1}, \ldots, v_{s}$ be a set of representatives for the $\Gamma_{0}$-orbits of essential cusps. We have chosen $\Sigma_{0}$ so that each of the maps $R_{\Sigma_{0}, v_{i}}$ is non-zero. Hence ker $R_{\Sigma_{0}, v_{i}}$ is a proper subspace of $H^{1}\left(\Sigma_{0}, \mathbb{R}\right)$. In particular, the union of the kernels of the $R_{\Sigma_{0}, v_{i}}$ is not the whole vector space $H^{1}\left(\Sigma_{0}, \mathbb{R}\right)$, and there is an open cone in $H^{1}\left(\Sigma_{0}, \mathbb{R}\right)$ which does not intersect any of these kernels. Choose a non-zero element $\rho \in H^{1}\left(\Sigma_{0}, \mathbb{Z}\right)$ in this open cone, so $\rho \notin \operatorname{ker} R_{\Sigma_{0}, v_{i}}$ for all $i$. It follows from Lemma 13 that $\rho \notin \operatorname{ker} R_{\Sigma_{0}, v}$ for all essential cusps $v$. Dividing $\rho$ by a constant if necessary, we may assume that $\rho: \Sigma_{0} \rightarrow \mathbb{Z}$ is surjective. \(\square\)

Now let $\Sigma_{0}$ be chosen as in Lemma 15 and let $\rho: \Sigma_{0} \rightarrow \mathbb{Z}$ be a homomorphism chosen as in Lemma 16. We now define a sequence of arithmetic groups $\Gamma_{n}$ as follows:
$$\Gamma_{n}=f^{-1}\left(\Sigma_{n}\right), \quad \text { where } \Sigma_{n}=\left\{\sigma \in \Sigma_{0}: \rho(\sigma) \equiv 0 \bmod n\right\} .$$

Lemma 17. The number of $\Gamma_{n}$-orbits of essential cusps is bounded independently of $n$.
Proof. Choose any essential cusp $v$, and let $S_{n}$ be the set of $\Gamma_{n}$-orbits of cusps which are in the same $\Gamma_{0}$-orbit as $v$. It is sufficient to show that the cardinality of each $S_{n}$ is bounded independently of $n$. By the orbit-stabilizer theorem there is a bijection between $S_{n}$ and the double coset set:
$$S_{n} \simeq \Gamma_{n} \backslash \Gamma_{0} / \Gamma_{0, v} .$$
Using the homomorphism $\rho \circ f$, we may identify $\Gamma_{n} \backslash \Gamma_{0}$ with $\mathbb{Z} / n \mathbb{Z}$. Therefore there is a bijection between $S_{n}$ and the group $\mathbb{Z} /\left(n \mathbb{Z}+\rho\left(f\left(\Gamma_{0, v}\right)\right)\right.$. In particular we have
$$\left|S_{n}\right| \leq\left|\mathbb{Z} / \rho\left(f\left(\Gamma_{0, v}\right)\right)\right| .$$
The homomorphism $\rho$ is chosen so that $\rho\left(f\left(\Gamma_{0, v}\right)\right) \neq 0$, so we have a bound on the cardinality of $S_{n}$ which does not depend on $n$. \(\square\)

Lemma 18. The rank of the composition $H^{1}\left(\Sigma_{n}, \mathbb{R}\right) \xrightarrow{f^{*}} H^{1}\left(\Gamma_{n}, \mathbb{R}\right) \rightarrow H^{1}\left(\partial X_{\Gamma_{n}}, \mathbb{R}\right)$ is bounded independently of $n$.

Proof. There is a decomposition
$$H^{1}\left(\partial X_{\Gamma_{n}}, \mathbb{R}\right)=\bigoplus_{v} H^{1}\left(\Gamma_{n, v}, \mathbb{R}\right),$$
where $v$ ranges over the $\Gamma_{n}$-orbits of cusps. However, if $v$ is not an essential cusp, then the map $H^{1}\left(\Sigma_{n}, \mathbb{C}\right) \rightarrow H^{1}\left(\Gamma_{n, v}, \mathbb{C}\right)$ is zero. Therefore, the image of $H^{1}\left(\partial X_{\Gamma_{n}}, \mathbb{C}\right)$ is contained in the direct sum of the spaces $H^{1}\left(\Gamma_{n, v}, \mathbb{C}\right)$, where $v$ ranges over the $\Gamma_{n}$-orbits of the essential cusps. The result now follows from Lemma 17. \(\square\)

Lemma 19. For n sufficiently large, the inner cohomology $H_{!}^{1}\left(X_{\Gamma_{n}}, \mathbb{R}\right)$ is non-zero.
Proof. Since $\Sigma_{0}$ is a hyperbolic surface group, the dimension of $H^{1}\left(\Sigma_{n}, \mathbb{R}\right)$ tends to infinity as $n \rightarrow \infty$. In view of Lemma 18, for large enough $n$, the map $H^{1}\left(\Sigma_{n}, \mathbb{R}\right) \rightarrow H^{1}\left(\partial X_{\Gamma_{n}}, \mathbb{R}\right)$ is not injective. Choose a non-zero element $\phi \in \operatorname{ker}\left(H^{1}\left(\Sigma_{n}, \mathbb{R}\right) \rightarrow H^{1}\left(\partial X_{\Gamma_{n}}, \mathbb{R}\right)\right)$. Then $f^{*}(\phi)$ is a non-zero element of $H_{!}^{1}\left(\Gamma_{n}, \mathbb{R}\right)$. \(\square\)

Lemma 19 concludes the proof of Theorem 3. By the discussion above, this shows that the preimage of $\Gamma_{\left(\frac{2}{6}, \frac{2}{6}, \frac{3}{6}, \frac{4}{6}, \frac{1}{6}\right)}$ in each every connected cover of $\operatorname{SU}(2,1)$ is residually finite.

\section*{References}
\begin{itemize}
\item[] [1] A. Ash, D. Mumford, M. Rapoport and Y. Tai. Smooth compactification of locally symmetric varieties, Cambridge University Press 2010.
\end{itemize}
\begin{itemize}
\item[] [2] A. Borel and N. Wallach, Continuous cohomology, discrete subgroups, and representations of reductive groups. Second edition. Mathematical Surveys and Monographs, 67. American Mathematical Society 2000.
\item[] [3] G. Di Cerbo and L. F. Di Cerbo, "Effective results for complex hyperbolic manifolds", J. London Math. Soc. 91, no. 1 (2015) 89-104.
\item[] [4] P. Deligne and G. D. Mostow, "Monodromy of hypergeometric functions and non-lattice integral monodromy", Publ. math. de l'I.H.E.S. 63 (1986), 5-89.
\item[] [5] E. Freitag and R. M. Hill, "Modular forms on SU(2, 1) of weight $\frac{1}{3}$." preprint https://arxiv.org/abs/2203.01106.
\item[] [6] P. Griffiths and J. Harris, Principles of algebraic geometry. Wiley Classics Library. John Wiley \& Sons, Inc., New York, 1994.
\item[] [7] G. Harder, "Eisensteinkohomologie für Gruppen vom Typ GU(2,1)." Math. Ann. 278 (1987), no. 1-4, 563-592.
\item[] [8] G. Harder, Cohomology of Arithmetic Groups, preprint book https://www.math.uni-bonn.de/people/harder/Manuscripts/buch/Volume-III.pdf.
\item[] [9] R. M. Hill, "Fractional weight multiplier systems on $\operatorname{SU}(d, 1)$ ", preprint 2021 https://arxiv.org/abs/2108.04538.
\item[] [10] C. C. Moore, "Extensions and low dimensional cohomology theory of locally compact groups I, II.", Trans. A.M.S. Vol. 113, No. 1 (1964), pp. 40-86.
\item[] [11] G. Shimura, "Automorphic forms and the periods of abelian varieties", J. Math. Soc. Japan Vol. 31, No. 3 (1979) 561-592.
\item[] [12] M. Stover, "Cusp and $b_{1}$ growth for ball quotients and maps onto $\mathbb{Z}$ with finitely generated kernel", Indiana Univ. Math. J. 70 (2021), no. 1, 213-233.
\item[] [13] M. Stover and D. Toledo, "Residually finite lattices in $\widetilde{P U(2,1)}$ and fundamental groups of smooth projective surfaces", preprint 2021 https://arxiv.org/abs/2105.12772.
\item[] [14] M. Stover and D. Toledo, "Residual finiteness for central extensions of lattices in $P U(n, 1)$ and negatively curved projective varieties", preprint 2021 https://arxiv.org/abs/2108.12404.
\item[] [15] D. Wigner, "Algebraic cohomology of topological groups", Trans. AMS 178 (1973), 83-93.
\end{itemize}