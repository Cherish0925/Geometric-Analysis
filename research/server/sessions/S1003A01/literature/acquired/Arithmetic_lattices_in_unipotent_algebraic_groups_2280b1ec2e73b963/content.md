---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: Arithmetic_lattices_in_unipotent_algebraic_groups_9766d3d717c7.pdf
converter: mathpix
format: mmd
---

\title{
Arithmetic lattices in unipotent algebraic groups
}

\author{
Khalid Bou-Rabee* Daniel Studenmund ${ }^{\dagger}$
}

April 19, 2018

\begin{abstract}
Fixing an arithmetic lattice $\Gamma$ in an algebraic group $G$, the commensurability growth function assigns to each $n$ the cardinality of the set of subgroups $\Delta$ with $[\Gamma: \Gamma \cap \Delta][\Delta: \Gamma \cap \Delta]=n$. This growth function gives a new setting where methods of F. Grunewald, D. Segal, and G. C. Smith's "Subgroups of finite index in nilpotent groups" apply to study arithmetic lattices in an algebraic group. In particular, we show that for any unipotent algebraic $\mathbb{Z}$-group with arithmetic lattice $\Gamma$, the Dirichlet function associated to the commensurability growth function satisfies an Euler decomposition. Moreover, the local parts are rational functions in $p^{-s}$, where the degrees of the numerator and denominator are independent of $p$. This gives regularity results for the set of arithmetic lattices in $G$.
\end{abstract}
keywords: commensurability, lattices, unipotent algebraic groups, subgroup growth

\section*{1 Introduction}

Let $G$ be an algebraic group defined over $\mathbb{Z}$ (an algebraic $\mathbb{Z}$-group). Two subgroups $\Delta_{1}$ and $\Delta_{2}$ of $G(\mathbb{R})$ are commensurable if their commensurability index
$$\mathrm{c}\left(\Delta_{1}, \Delta_{2}\right):=\left[\Delta_{1}: \Delta_{1} \cap \Delta_{2}\right]\left[\Delta_{2}: \Delta_{1} \cap \Delta_{2}\right]$$
is finite. An arithmetic lattice of $G$ is a subgroup of $G(\mathbb{R})$ that is commensurable with $G(\mathbb{Z})$. The first purpose of this article is to show that when $G$ is unipotent, the set of arithmetic lattices in $G$ has a great deal of regularity. The second purpose is to bring attention to a new notion of quantifying commensurability.

The main tool of this article is the commensurability growth function $\mathbb{N} \rightarrow \mathbb{N} \cup\{\infty\}$ assigning to each $n \in \mathbb{N}$ the cardinality
$$\mathbf{c}_{n}(G(\mathbb{Z}), G(\mathbb{R})):=|\{\Delta \leq G(\mathbb{R}): \mathrm{c}(G(\mathbb{Z}), \Delta)=n\}| .$$
We study $\mathbf{c}_{n}(G(\mathbb{Z}), G(\mathbb{R}))$ for groups $G$ in the class $\mathcal{U}$ of unipotent algebraic $\mathbb{Z}$-groups, starting with the fact that $\mathbf{c}_{n}(G(\mathbb{Z}), G(\mathbb{R}))$ is finite for all $n$ in Lemma 3.1. Note that the map $G \mapsto G(\mathbb{Z})$ gives the Mal'cev correspondence [Mc71] between torsion-free finitely generated nilpotent groups and unipotent $\mathbb{Z}$-groups (see also [GO85]).

Our method of attack is that of F. Grunewald, D. Segal, and G. C. Smith [GSS88], who studied the subgroup growth function of torsion-free finitely generated nilpotent groups $\Gamma$, defined by
$$a_{n}(\Gamma):=\{\Delta \leq \Gamma:[\Gamma: \Delta]=n\},$$

\footnotetext{
*K.B. supported in part by NSF grant DMS-1405609
${ }^{\dagger}$ D.S. supported in part by NSF grant DMS-1246989
}
by decomposing the associated zeta function into a product of local functions (see also [dS93]). In view of the relationship $\mathbf{c}_{n}(\Gamma, \Gamma)=a_{n}(\Gamma)$, the function $\mathbf{c}_{n}$ extends $a_{n}$ to pairs of groups. While we have the simple relationship $\mathbf{c}_{n}(G(\mathbb{Z}), G(\mathbb{R})) \geq a_{n}(G(\mathbb{Z}))$, it is clear from the results in this paper that this inequality is strict when $G$ is unipotent. The difference is evident even in the one-dimensional case.

\subsection*{1.1 The setting}

Our results about $\mathbf{c}_{n}$ are stated in the language of zeta functions. Let $G$ be an algebraic group and let $\mathcal{F}$ a family of subgroups of $G(\mathbb{R})$. We associate to such a family the Dirichlet series
$$\zeta_{\mathcal{F}}(s)=\sum_{\Delta \in \mathcal{F}} \mathrm{c}(G(\mathbb{Z}), \Delta)^{-s}=\sum_{n=1}^{\infty} \mathbf{c}_{n}(\mathcal{F}) n^{-s}$$
where
$$\mathbf{c}_{n}(\mathcal{F}):=|\{\Delta \in \mathcal{F}: \mathrm{c}(G(\mathbb{Z}), \Delta)=n\}| .$$

Following [GSS88], there are two questions one can ask about the sequence $\mathbf{c}_{n}(\mathcal{F})$ : (a) how fast does it grow, and (b) how regularly does it behave? Pursuing (a) is the study of commensurability growth, which we do not directly address here. We will address (b) by decomposing $\zeta_{\mathcal{F}}$ into local parts and proving a local regularity theorem. The families we consider are the following:
$$\begin{aligned}
\mathcal{L}(G) & :=\{\text { all arithmetic lattices inside } G\}, \\
\mathcal{L}_{n}(G) & :=\{\Delta \in \mathcal{L}(G): c(\Delta, G(\mathbb{Z}))=n\}, \\
\mathcal{L}_{(p)}(G) & :=\{\Delta \in \mathcal{L}(G): c(\Delta, G(\mathbb{Z})) \text { is a power of } p\} .
\end{aligned}$$
Define the global and local commensurability zeta functions:
$$\zeta_{G}:=\zeta_{\mathcal{L}(G)} \quad \text { and } \quad \zeta_{G, p}:=\zeta_{\mathcal{L}_{(p)}(G)} .$$

\subsection*{1.2 The main results}

We start with an elementary example, proved in §2.
Proposition 1.1. Let $G=G_{a}$, the additive algebraic group, so that $G(\mathbb{Z})=\mathbb{Z}$ and $G(\mathbb{R})=\mathbb{R}$. Then formally,
$$\zeta_{G}(s)=\frac{\zeta^{2}(s)}{\zeta(2 s)} .$$

The zeta functions introduced in [GSS88] decompose into Euler products. Our first main result, proved in 43.1 is an analogous decomposition of the commensurability zeta function $\zeta_{G}$ for $G \in \mathcal{U}$.

Proposition 1.2. If $G \in \mathcal{U}$, then
$$\zeta_{G}(s)=\prod_{p} \zeta_{G, p}(s)$$
as formal products over all primes of Dirichlet series.
The main content of this article, our next result, is proved in §3.2.
Theorem 1.3. Let $G \in \mathcal{U}$, then the function $\zeta_{G, p}(s)$ is rational in $p^{-s}$, where the degrees of the numerators and denominators are bounded independently of the prime $p$.

Proposition 1.2 and Theorem 1.3 provide regularity results for the set of arithmetic lattices, $\mathcal{L}(G)$.
Corollary 1.4. Let $G \in \mathcal{U}$, then
\begin{itemize}
\item[1.] $\mathbf{c}_{n}(\mathcal{L}(G))=\prod \mathbf{c}_{p_{i}^{e_{i}}}(\mathcal{L}(G))$ where $n=\prod p_{i}^{e_{i}}$ is the prime factorization of $n$;
\item[2.] there exists positive integers $l$ and $k$ such that, for each prime $p$, the sequence $\left(\mathbf{c}_{p^{i}}(\mathcal{L}(G))\right)_{i>l}$ satisfies a linear recurrence relation over $\mathbb{Z}$ of length at most $k$.
\end{itemize}

Our proof of Theorem 1.3 uses [Mac90, Theorem 22], which is a stronger rationality theorem than that used in [GSS88]. Our setup requires such a theorem since we express the local commensurability zeta function as a $p$-adic integral over an unbounded set (see Proposition 3.12). To find this explicit formula, we constructed a parametrization of lattices that gives a closed form for the commensurability index function (see Lemma 3.10). We also discovered an explicit correspondence
$$\left\{\text { closed } K \leq G\left(\mathbb{Q}_{p}\right): \mathrm{c}\left(G\left(\mathbb{Z}_{p}\right), K\right)=p^{k}\right\} \leftrightarrow\left\{\Delta \leq G(\mathbb{Q}): \mathrm{c}(G(\mathbb{Z}), \Delta)=p^{k}\right\},$$
that may be of independent interest (see Lemma 3.5).
We were moved to pursue this subject after reading the work of N. Avni, S. Lim, and E. Nevo [ALN12] on the related concept of commensurator growth. Commensurator growth in [ALN12], subgroup growth in [GSS88], and commensurability growth in this paper are all studied through their associated zeta functions. Associating zeta functions to growth functions in groups is an active area of research, centering around subgroup growth and representation growth. For background reading on these subjects we recommend the references [LS03, Vol11, Klo11].

Notation
$$\mathrm{c}(A, B)=[A: A \cap B][B: A \cap B] .$$
$\mathcal{U}=$ the class of unipotent algebraic $\mathbb{Z}$-groups.
$\mathcal{T}=$ the class of torsion-free finitely generated nilpotent groups.
$|S|=$ the cardinality of the set $S$.
$[x, y]=x^{-1} y^{-1} x y=x^{-1} x^{y}$.
$G^{n}=\left\langle g^{n}: g \in G\right\rangle$ for $n \in \mathbb{Z}$.
$Z(G)=$ the center of $G$.
$T_{n}(R)=$ set of lower-triangular $n \times n$ matrices over a commutative ring $R$.
$\zeta(s)$ is the Riemann zeta function.

Acknowledgements We are grateful to Benson Farb, Tasho Kaletha, Michael Larsen, and Andrew Putman for their conversations and support. In particular, Benson Farb provided helpful comments on an early draft.

\section*{2 The 1-dimensional case}

We begin with the integers. In this case we can directly relate the commensurability zeta function with the classical zeta function.

Proposition 2.1. Let $G=G_{a}$, the additive algebraic group, so that $G(\mathbb{Z})=\mathbb{Z}$ and $G(\mathbb{R})=\mathbb{R}$. Then formally,
$$\zeta_{G}(s)=\frac{\zeta^{2}(s)}{\zeta(2 s)} .$$

Proof. The subgroups of $\mathbb{R}$ commensurable with $\mathbb{Z}$ are all of the form $r \mathbb{Z}$ where $r \in \mathbb{Q}^{*}$. Writing $r=n / d$ in reduced form, we have $\mathrm{c}(\mathbb{Z}, r \mathbb{Z})=n d$. Hence,
$$\mathbf{c}_{n}(\mathcal{L}(G))=|\{a / b: a, b \in \mathbb{N},(a, b)=1, a b=n\}| .$$
From this, we get for distinct primes $p_{1}, p_{2}, p_{3}, \ldots, p_{n}$,
$$\mathbf{c}_{p_{1}^{j_{1}} p_{2}^{j_{2}} \cdots p_{n}^{j_{n}}}(\mathcal{L}(G))=\mathbf{c}_{p_{1}^{j_{1}}}(\mathcal{L}(G)) \mathbf{c}_{p_{2}^{j_{2}}}(\mathcal{L}(G)) \cdots \mathbf{c}_{p_{n}^{j_{n}}}(\mathcal{L}(G)) .$$
And for any prime $p$,
$$\mathbf{c}_{p^{k}}(\mathcal{L}(G))=2 .$$
Hence,
$$\mathbf{c}_{n}(\mathcal{L}(G))=2^{\omega_{n}},$$
where $\omega_{n}$ is the number of distinct primes dividing $n$. Following [HW08, p. 255], we compute:
$$\begin{aligned}
\zeta_{G}(s) & =\sum_{n=1}^{\infty} 2^{\omega_{n}} n^{-s} \\
& =\prod_{p \text { prime }}\left(1+\sum_{k=1}^{\infty} \frac{2}{p^{k s}}\right) \\
& =\prod_{p \text { prime }}\left(\frac{2 p^{-s}}{1-p^{-s}}+1\right) \\
& =\prod_{p \text { prime }} \frac{1-p^{-2 s}}{\left(1-p^{-s}\right)^{2}} \\
& =\frac{\zeta^{2}(s)}{\zeta(2 s)} .
\end{aligned}$$ \(\square\)

\section*{3 Unipotent algebraic groups}

To any $G \in \mathcal{U}$ we fix an embedding of $G(\mathbb{R})$ into a group $T_{n}(\mathbb{R})$ such that $G(\mathbb{Q})=T_{n}(\mathbb{Q}) \cap G(\mathbb{Q})$ given by Kolchin's Theorem [Kol48]. With this in hand, we first show that for any unipotent algebraic $\mathbb{Z}$ -group $G$, the commensurability growth function takes values in $\mathbb{N}$ :

Lemma 3.1. Let $G$ be in $\mathcal{U}$. Then $\mathcal{L}_{n}(G)$ is finite for any $n \in \mathbb{N}$.
Proof. Given $n \in \mathbb{N}$, for any $\Delta \in \mathcal{L}_{n}(G)$ and for every $h \in \Delta$, we have $h^{n} \in G(\mathbb{Z})$. Then by [Seg83, Exercise 7, page 114], there exists a finitely generated subgroup $\Gamma \leq G(\mathbb{Q})$ that contains every $n$th root of an element of $G$. Then every element in $\mathcal{L}_{n}(G)$ is a subgroup of $\Gamma$ of index at most $n[\Gamma: G(\mathbb{Z})]$. Since $\Gamma$ is finitely generated, it has finitely many subgroups of any given index, so $\mathcal{L}_{n}(G)$ is finite. \(\square\)

As an immediate consequence of the proof of Lemma 3.1, we get the well-known fact that arithmetic lattices in $G$ are contained in $G(\mathbb{Q})$ :

Lemma 3.2. Let $G$ be in $\mathcal{U}$. Then each element of $\mathcal{L}(G)$ is a subgroup of $G(\mathbb{Q})$. \(\square\)

Slight modifications of a technical idea in the proof of Lemma 3.1 will be used repeatedly throughout the rest of the paper, so we encapsulate them here. Throughout, for any $\Delta \leq G(\mathbb{R})$ and $n \in \mathbb{N}$, we write $\Delta^{1 / n}$ to be the group generated by elements $g \in G(\mathbb{R})$ such that $g^{n} \in \Delta$.

Lemma 3.3. Let $G$ be in $\mathcal{U}$ and $\Gamma=G(\mathbb{Z})$ have nilpotence class $c$ and Hirsch length $d$.
\begin{itemize}
\item[1.] For any $k \in \mathbb{N},\left[\Gamma^{1 / k}: \Gamma\right]$ is finite.
\item[2.] We have $\left(\Gamma^{p^{-k}}\right)^{p^{k c(c+1) / 2}} \leq \Gamma$.
\item[3.] For any prime $p$ and any $k \in \mathbb{N}$, we have $\left[\Gamma^{p^{-k}}: \Gamma\right] \leq p^{d k c(c+1) / 2}$.
\end{itemize}

Proof. Item 1 follows from [Seg83, Exercise 7, page 114]. Item 2 follows from [Seg83, Proposition 3, pp. 113]. For the final statement, by [Seg83, Exercise 7, page 114] the group $\Gamma^{p^{-k}}$ is a finitely generated nilpotent group. Moreover, by being in $G(\mathbb{Q})$, it has Hirsch length at most $d$, and hence
$$\left[\Gamma^{p^{-k}}:\left(\Gamma^{p^{-k}}\right)^{p^{k c(c+1) / 2}}\right] \leq p^{d k c(c+1) / 2}$$
Then by Item 2 it follows that we have bounded $\left[\Gamma^{p^{-k}}: \Gamma\right]$ as desired. \(\square\)

\subsection*{3.1 The Euler decomposition}

Proposition 3.4. If $G$ is in $\mathcal{U}$, then
$$\zeta_{G}(s)=\prod_{p \text { prime }} \zeta_{G, p}(s) .$$
Proof. Any group in $\mathcal{L}_{n}(G)$ is a subgroup of $G(\mathbb{Z})^{1 / n}$. Hence, by applying Item 1 of Lemma 3.3, we see that $\Omega=\left\langle\mathcal{L}_{n}(G)\right\rangle$ is finitely generated and contains each element of $\mathcal{L}_{n}(G)$ as a subgroup of finite index. Hence, $\Lambda_{n}^{\prime}=\cap_{A \in \mathcal{L}_{n}(G)} A$ is a subgroup of finite index in $\Omega$. Let $\Lambda_{n}$ be the normal core of $\Lambda_{n}^{\prime}$ in $\Omega$.

Consider the group $\Gamma:=\Omega / \Lambda_{n}$. It is a finite nilpotent group, and hence decomposes into a product of its Sylow $p$-subgroups:
$$\Omega / \Lambda_{n}=\prod_{p} S_{p} .$$
For any image $A$ in $\Gamma$ of an element $\Delta \in \mathcal{L}_{n}(G)$, we get the following decomposition:
$$A=\prod_{p} A_{p},$$
where $A_{p}$ are the Sylow $p$-subgroups of $A$ and $A_{p} \leq S_{p}$ for every $p$. A similar statement is true for the image $Q$ of $G(\mathbb{Z})$ in $\Gamma$, we have
$$Q=\prod_{p \text { prime }} Q_{p}$$
where $Q_{p} \leq S_{p}$. We compute,
$$Q \cap A=\prod_{p \text { prime }}\left(A_{p} \cap Q_{p}\right) .$$
Hence,
$$\mathrm{c}(G(\mathbb{Z}), \Delta)=\mathrm{c}(Q, A)=\prod_{p \text { prime }} \mathrm{c}\left(A_{p}, Q_{p}\right) .$$
Further, $\mathrm{c}\left(A_{p}, Q_{p}\right)$ is the greatest power of $p$ that divides $n$. Since any such element of $\mathcal{L}_{n}(G)$ arises from such a decomposed $A$, we have
$$\mathbf{c}_{n}(\mathcal{L})=\prod_{p^{k} \| n} \mathbf{c}_{p^{k}}(\mathcal{L}),$$
and hence the Euler decomposition for the commensurability zeta function above holds. \(\square\)

\section*{$3.2 p$-adic formulation and the proof of Theorem 1.3}

Let $G \in \mathcal{U}$. Fix a Mal'cev basis ( $x_{1}, \ldots, x_{n}$ ) for $G(\mathbb{Z})$, so that
$$1<\left\langle x_{1}\right\rangle<\left\langle x_{1}, x_{2}\right\rangle<\cdots<\left\langle x_{1}, \ldots, x_{n}\right\rangle=G(\mathbb{Z})$$
is a central series with infinite cyclic successive quotients. Elements in $G\left(\mathbb{Q}_{p}\right)$ may be identified with the set of all " $p$-adic words" of the form
$$\mathbf{x}(\mathbf{a})=x_{1}^{a_{1}} \cdots x_{n}^{a_{n}},$$
where $\mathbf{a} \in \mathbb{Q}_{p}^{n}$. Note that $\mathbf{x}$ parametrizes $G(\mathbb{Z})$ when restricted to $\mathbf{a} \in \mathbb{Z}^{n}$. Let $\lambda, \kappa$, and $\mu^{(i)}$ for $i \geq 2$ be polynomials defined over $\mathbb{Q}$ as in [GSS88, pp. 197] for the $\mathcal{T}$ group $G(\mathbb{Z})$, so that for $\mathbf{a} \in \mathbb{Z}^{n}$ we have
$$\begin{aligned}
\mathbf{x}(\mathbf{a})^{k}=\mathbf{x}\left(a_{1}, a_{2}, a_{3}, \ldots, a_{n}\right)^{k} & =\mathbf{x}(\lambda(\mathbf{a}, k)), \\
\mathbf{x}\left(\mathbf{a}_{1}\right) \mathbf{x}\left(\mathbf{a}_{2}\right) \cdots x\left(\mathbf{a}_{i}\right) & =\mathbf{x}\left(\mu^{(i)}\left(\mathbf{a}_{1}, \mathbf{a}_{2}, \ldots \mathbf{a}_{i}\right)\right), \\
{\left[\mathbf{x}\left(\mathbf{a}_{1}\right), \mathbf{x}\left(\mathbf{a}_{2}\right)\right] } & =\mathbf{x}\left(\kappa\left(\mathbf{a}_{1}, \mathbf{a}_{2}\right)\right) .
\end{aligned}$$

We denote the closure of a subset $S$ of $G\left(\mathbb{Q}_{p}\right)$ to be $\bar{S}$ or $S^{-}$. For any $\Gamma \in \mathcal{L}(G)$ we have that $\bar{\Gamma}$ is the pro- $p$ completion of $\Gamma$ [Wil98, Theorem 4.3.5].

Lemma 3.5. For each $k$, the closure map gives a one-to-one correspondence between elements of $\mathcal{L}_{p^{k}}(G)$ and closed subgroups $H$ of $G\left(\mathbb{Q}_{p}\right)$ with $c\left(H, G\left(\mathbb{Z}_{p}\right)\right)=p^{k}$.

Proof. Let $\Gamma=G(\mathbb{Z})^{p^{-k}}$. Note that $\Gamma$ contains every subgroup in $\mathcal{L}_{p^{k}}(G)$. Moreover, by Item 2 of Lemma 3.3, we have that $\Gamma^{p^{N}} \leq G(\mathbb{Z})$ for $N=k c(c+1) / 2$, where $c$ is the nilpotence class of $G$. It follows that any $\Delta \in \mathcal{L}_{p^{k}}(G)$ contains $\Gamma^{p^{N+k}}$. Note that $\Gamma^{p^{N+k}}$ is a normal subgroup of $\Gamma$ and the quotient group $\Gamma / \Gamma^{p^{N+k}}$ is a finite $p$-group. It follows that for each $\Delta \in \mathcal{L}_{p^{k}}(G)$ there is some $\ell \in \mathbb{N}$ such that $[\Gamma: \Delta]=p^{\ell}$.

Let $K$ be the closure of $\Gamma$ in $G\left(\mathbb{Q}_{p}\right)$. Then $K$ is a finitely generated pro- $p$ group. Any closed subgroup $H \leq G\left(\mathbb{Q}_{p}\right)$ satisfying $c\left(H, G\left(\mathbb{Z}_{p}\right)\right)=p^{k}$ is a finite-index subgroup of $G\left(\mathbb{Z}_{p}\right)^{p^{-k}}=K$. The closure map gives an index-preserving bijection between subgroups of $\Gamma$ with index a power of $p$ and finite-index subgroups of $K$. This completes the proof. \(\square\)

Define $G_{i}=\left\langle x_{1}^{r_{1}}, \ldots, x_{i}^{r_{i}}: r_{1}, \ldots, r_{i} \in \mathbb{Q}_{p}\right\rangle$. The following is an extension of the notion of good basis from [GSS88] to the $G\left(\mathbb{Q}_{p}\right)$ setting.

Definition 3.6. Let $H$ be a closed subgroup of $G\left(\mathbb{Q}_{p}\right)$. An $n$-tuple $\left(h_{1}, \ldots, h_{n}\right)$ of elements in $H$ is called a good basis if for each $i=1, \ldots, n$,
$$\left\langle h_{1}, \ldots, h_{i}\right\rangle^{-}=H \cap G_{i} .$$

Lemma 3.7. Let $h_{i} \in G_{i} \backslash G_{i-1}$ for $i=1, \ldots, n$ and let $H=\left\langle h_{1}, \ldots, h_{n}\right\rangle^{-}$. Then:
\begin{itemize}
\item[1.] $\mathrm{c}\left(H, G\left(\mathbb{Z}_{p}\right)\right)<\infty$.
\item[2.] $\left(h_{1}, \ldots, h_{n}\right)$ is a good basis for $H$ if and only if
$$\left[h_{i}, h_{j}\right] \in\left\langle h_{1}, \ldots, h_{i-1}\right\rangle^{-} \text {for } 1 \leq i<j \leq n .$$
\item[3.] Suppose Equation 2 holds, and let $h_{1}^{\prime}, \ldots, h_{n}^{\prime} \in H$. Then $\left(h_{1}^{\prime}, \ldots, h_{n}^{\prime}\right)$ is a good basis for $H$ if and only if there exists $r_{i} \in \mathbb{Z}_{p}^{*}$ and $w_{i} \in\left\langle h_{1}, \ldots, h_{i-1}\right\rangle^{-}$such that
$$h_{i}^{\prime}=w_{i} h_{i}^{r_{i}} \text { for } 1 \leq i \leq n .$$
\end{itemize}

Proof. Since $h_{i} \in G_{i} \backslash G_{i-1}$ for $i=1, \ldots, n$, we have
$$h_{i}=x_{1}^{r_{i 1}} x_{2}^{r_{i 2}} \cdots x_{n}^{r_{i n}},$$
where $r_{i j} \in \mathbb{Q}_{p}$. For any such nonzero $r_{i j}$ we have $r_{i j}=u p^{-k}$ where $k \in \mathbb{Z}$ and $u \in \mathbb{Z}_{p}^{*}$. If all such $k$ are nonpositive, then we appeal to [GSS88, Lemma 2.1]. Otherwise, let $k$ be the maximal integer that appears in this way. Then
$$H \leq\left\langle x_{1}^{p^{-k}}, x_{2}^{p^{-k}}, \ldots, x_{n}^{p^{-k}}\right\rangle^{-} \leq G\left(\mathbb{Z}_{p}\right)^{p^{-k}} .$$
By continuity of taking powers, $G\left(\mathbb{Z}_{p}\right)^{p^{-k}}$ is the closure of $G(\mathbb{Z})^{p^{-k}}$ in $G\left(\mathbb{Q}_{p}\right)$. Thus, by applying Item 2 of Lemma 3.3, we have that there exists $m \in \mathbb{N}$ such that $H^{m} \leq G\left(\mathbb{Z}_{p}\right)$. It follows that $G\left(\mathbb{Z}_{p}\right) \cap H$ must have the same dimension as $G$, and so Item 1 follows.

Items 2 and 3 follow from small modifications of the proof of [GSS88, Lemma 2.1]. \(\square\)

Definition 3.8. For $\Delta \in \mathcal{L}(G)$, define $\mathfrak{U}(\Delta)$ to be the collection of pairs $(A, B)$ where $A \in T_{n}\left(\mathbb{Q}_{p}\right)$, $B \in T_{n}\left(\mathbb{Z}_{p}\right)$, such that, if $a_{i}$ denotes the ith row of $A$ and $b_{i}$ denotes the ith row of $B$,
\begin{itemize}
\item[1.] $\left(\mathbf{x}\left(a_{1}\right), \ldots, \mathbf{x}\left(a_{n}\right)\right)$ is a good basis for $\bar{\Delta}$, and
\item[2.] $\left(\mathbf{x}\left(b_{1}\right), \ldots, \mathbf{x}\left(b_{n}\right)\right)$ is a good basis for $\bar{\Delta} \cap G\left(\mathbb{Z}_{p}\right)$.
\end{itemize}

Combining suitable $\mathfrak{U}(\Delta)$ into one set, we define
$$\mathfrak{U}_{p}:=\bigcup_{k=1}^{\infty}\left(\bigcup_{\Delta \in \mathcal{L}_{p^{k}}(G)} \mathfrak{U}(\Delta)\right) .$$
The next proposition shows that $\mathfrak{U}_{p}$ is $L_{p}$-defined in the sense of [Mac90] (that is, it can be defined using first-order logic, $p$-norms, and field operations). Note that $|x|_{p} \geq|y|_{p}$ can be stated in $L_{P}$ (see the example in [Mac90, Page 71]).

Lemma 3.9. Let $(A, B) \in T_{n}\left(\mathbb{Q}_{p}\right) \times T_{n}\left(\mathbb{Z}_{p}\right)$. Then $(A, B) \in \mathfrak{U}_{p}$ if and only if each of the following holds.
\begin{itemize}
\item[1.] $\operatorname{det}(A) \neq 0$ and the rows $a_{1}, \ldots, a_{n}$ of the matrix $A$ satisfy
$$\begin{array}{r}
\text { for } 1 \leq i<j \leq n \text { there exist } Y_{i j}^{1}, \ldots, Y_{i j}^{i-1} \in \mathbb{Z}_{p} \text { such that } \\
\qquad \kappa\left(a_{i}, a_{j}\right)=\mu^{(i-1)}\left(\lambda\left(a_{1}, Y_{i j}^{1}\right), \ldots, \lambda\left(a_{i-1}, Y_{i j}^{i-1}\right)\right) .
\end{array}$$
\item[2.] $\operatorname{det}(B) \neq 0$ and the rows $b_{1}, \ldots, b_{n}$ of the matrix $B$ satisfy
$$\begin{aligned}
& \text { for } 1 \leq i<j \leq n \text { there exist } Y_{i j}^{1}, \ldots, Y_{i j}^{i-1} \in \mathbb{Z}_{p} \text { such that } \\
& \qquad \kappa\left(b_{i}, b_{j}\right)=\mu^{(i-1)}\left(\lambda\left(b_{1}, Y_{i j}^{1}\right), \ldots, \lambda\left(b_{i-1}, Y_{i j}^{i-1}\right)\right) .
\end{aligned}$$
Moreover, let $\mathbf{y}: \mathbb{Z}_{p}^{n} \rightarrow G\left(\mathbb{Q}_{p}\right)$ be the function defined by
$$\mathbf{y}(\mathbf{d}):=\mathbf{x}\left(a_{1}\right)^{d_{1}} \mathbf{x}\left(a_{2}\right)^{d_{2}} \cdots \mathbf{x}\left(a_{n}\right)^{d_{n}} .$$
Then there exists vectors $c_{1}, \ldots, c_{i} \in \mathbb{Z}_{p}^{n}$ such that for all $i=1, \ldots, n$,
$$\mathbf{y}\left(c_{i}\right)=\mathbf{x}\left(b_{i}\right) .$$
\item[3.] $|\operatorname{det}(B)|_{p}$ is maximal over all $B$ satisfying 2
\end{itemize}

Proof. Let $(A, B) \in \mathfrak{U}(\Delta)$. Then Conditions 1 and 2 are satisfied by Lemma 3.7. To see Condition 3, note that $|\operatorname{det}(B)|_{p}=[G(\mathbb{Z}): G(\mathbb{Z}) \cap \Delta]$, while any matrix $B^{\prime}$ satisfying Condition 2 determines a subgroup of $G\left(\mathbb{Z}_{p}\right) \cap \bar{\Delta}$ and hence satisfies $\left|\operatorname{det}\left(B^{\prime}\right)\right|_{p} \leq[G(\mathbb{Z}): G(\mathbb{Z}) \cap \Delta]$.

Let $(A, B) \in \mathfrak{U}_{p}$. Let $H$ be the closed subgroup of $G\left(\mathbb{Q}_{p}\right)$ generated by $\mathbf{x}\left(a_{i}\right)$ where $a_{i}$ are the rows or $A$ and let $\Delta$ be the subgroup in $\mathcal{L}_{p^{\ell}}(G)$ corresponding to $H$ given by Lemma 3.5. The conditions above ensure $(A, B) \in \mathfrak{U}(\Delta)$. \(\square\)

Our parametrization of arithmetic lattices gives a nice formula for the commensurability index:
Lemma 3.10. Let $\Delta \in \mathcal{L}(G)$. Then for any $(A, B) \in \mathfrak{U}(\Delta)$, we have
$$\mathrm{c}\left(\bar{\Delta}, G\left(\mathbb{Z}_{p}\right)\right)=\left|\operatorname{det}(B)^{2} \operatorname{det}(A)^{-1}\right|_{p}^{-1} .$$
Proof. A direct application of the results of [GSS88, pp. 198] shows
$$\left[G\left(\mathbb{Z}_{p}\right): G\left(\mathbb{Z}_{p}\right) \cap \bar{\Delta}\right]=|\operatorname{det}(B)|_{p}^{-1} .$$

Let $C$ be the matrix whose $i$ th row $c_{i}$ satisfies $\mathbf{y}\left(c_{i}\right)=\mathbf{x}\left(b_{i}\right)$, where y is the function defined in Lemma 3.9. Note that $C \in T_{n}\left(\mathbb{Z}_{p}\right)$. Because $\bar{\Delta}=\mathbf{y}\left(\mathbb{Z}_{p}\right)$, it follows as above from [GSS88, pp. 198] that
$$\left[\bar{\Delta}: G\left(\mathbb{Z}_{p}\right) \cap \bar{\Delta}\right]=|\operatorname{det}(C)|_{p}^{-1} .$$

Using the fact that the rows of $B$ are coordinate vectors of a good basis, computation shows that
$$b_{i}=\left(q_{i 1}, \ldots, q_{i(i-1)}, a_{i i} c_{i i}, 0, \ldots, 0\right),$$
where $q_{i j} \in \mathbb{Q}_{p}$ for all $j<i$ and $a_{i i}$ and $c_{i i}$ are the respective diagonal elements of $A$ and $C$. It follows that
$$|\operatorname{det}(B)|_{p}^{-1}=|\operatorname{det}(A C)|_{p}^{-1} .$$
The desired result follows. \(\square\)

For $n \in \mathbb{N}$, let $v$ be the Haar measure on $\mathbb{Q}_{p}^{n}$ normalized such that $v\left(\mathbb{Z}_{p}^{n}\right)=1$.
Lemma 3.11. For a matrix $M \in T_{n}\left(\mathbb{Q}_{p}\right)$, let $f(M):=\prod_{i=1}^{n} m_{11} \cdots m_{i i}$. Let $\Delta \in \mathcal{L}(G)$. Then $\mathfrak{U}(\Delta)$ is an open subset of $T_{n}\left(\mathbb{Q}_{p}\right) \times T_{n}\left(\mathbb{Z}_{p}\right)$ and
$$v(\mathfrak{U}(\Delta))=\left(1-p^{-1}\right)^{2 n}|f(A) f(B)|_{p},$$
for any $(A, B) \in \mathfrak{U}(\Delta)$.
Proof. For $\Delta \in \mathcal{L}(G)$ and a ring $R$, let $\mathcal{M}_{R}(\Delta)$ be the set of matrices in $T_{n}(R)$ such that the rows $m_{1}, \ldots, m_{n}$ of $M$ satisfy $\mathbf{x}\left(m_{1}\right), \ldots, \mathbf{x}\left(m_{n}\right)$ are a good basis for $\bar{\Delta}$. Notice that $\mathfrak{U}(\Delta)=\mathcal{M}_{\mathbb{Q}_{p}}(\Delta) \times$ $\mathcal{M}_{\mathbb{Z}_{p}}(G(\mathbb{Z}) \cap \Delta)$. Hence, that $\mathfrak{U}(\Delta)$ is an open subset of $T_{n}\left(\mathbb{Q}_{p}\right) \times T_{n}\left(\mathbb{Z}_{p}\right)$ is a straightforward application of the first part of the proof of [GSS88, Lemma 2.5, pp. 198].

Moreover, the second part of the proof of [GSS88, Lemma 2.5, pp. 198] and Fubini's Theorem gives:
$$\begin{aligned}
\int_{\mathfrak{U}(\Delta)} 1 d v & =\int_{\mathcal{M}_{\mathbb{Q}_{p}}(\Delta) \times \mathcal{M}_{\mathbb{Z}_{p}}(G(\mathbb{Z}) \cap \Delta)} 1 d v \\
& =\int_{\mathcal{M}_{\mathbb{Q}_{p}}(\Delta)} \int_{\mathcal{M}_{\mathbb{Z}_{p}}(G(\mathbb{Z}) \cap \Delta)} 1 d v \\
& =\int_{\left.\mathcal{M}_{\mathbb{Q}_{p}} \Delta\right)}\left(1-p^{-1}\right)^{n}|f(B)|_{p} d v \\
& =\left(1-p^{-1}\right)^{2 n}|f(A) f(B)|_{p}
\end{aligned}$$ \(\square\)

Proposition 3.12. Let $f$ be as in Lemma 3.11 We have
$$\zeta_{G, p}(s)=\frac{1}{\left(1-p^{-1}\right)^{2 n}} \int_{(A, B) \in \mathfrak{U}_{p}}|f(A) f(B)|_{p}^{-1}\left|\operatorname{det}(B)^{2} \operatorname{det}(A)^{-1}\right|_{p}^{s} d v$$
Proof. By Lemma 3.11 for any $(A, B) \in \mathfrak{U}(\Delta)$, the integrand evaluates to:
$$v(\mathfrak{U}(\Delta))^{-1}\left(\mathrm{c}(\Delta, G(\mathbb{Z}))^{-s} .\right.$$
By decomposing $\mathfrak{U}_{p}$ into disjoint open sets,
$$\mathfrak{U}_{p}=\bigcup_{k=1}^{\infty}\left(\bigcup_{\Delta \in \mathcal{L}_{p^{k}}(G)} \mathfrak{U}(\Delta)\right),$$
using Lemma 3.11 we compute:
$$\begin{aligned}
& \frac{1}{\left(1-p^{-1}\right)^{2 n}} \int_{\mathfrak{U}_{p}}\left(|f(A) f(B)|_{p}^{-1}\left|\operatorname{det}(B)^{2} \operatorname{det}(A)^{-1}\right|_{p}^{s}\right) d v \\
= & \sum_{k=1}^{\infty}\left(\sum_{\Delta \in \mathcal{L}_{p^{k}}(G)}\left(\int_{\mathfrak{U}(\Delta)} v(\mathfrak{U}(\Delta))^{-1}\left(\mathrm{c}(\Delta, G(\mathbb{Z}))^{-s} d v\right)\right)\right. \\
= & \sum_{k=1}^{\infty}\left(\sum_{\Delta \in \mathcal{L}_{p^{k}}(G)}\left(\int_{\mathfrak{U}(\Delta)} v(\mathfrak{U}(\Delta))^{-1} p^{-k s} d v\right)\right) \\
= & \sum_{k=1}^{\infty}\left(\sum_{\Delta \in \mathcal{L}_{p^{k}}(G)} p^{-k s}\right)=\sum_{k=1}^{\infty} \frac{\mathbf{c}_{p^{k}}(\mathcal{L}(G))}{p^{k s}}=\zeta_{G, p}(s) .
\end{aligned}$$ \(\square\)

We are now ready to prove our main result:
Proof of Theorem 1.3. We first show that the local commensurability zeta functions converge for sufficiently large $s$. Given $\Delta \in \mathcal{L}_{p^{k}}(G)$, for any $\gamma \in \Delta$ we have $\gamma^{p^{k}} \in G\left(\mathbb{Z}_{p}\right)$ so $\Delta \leq \Gamma_{k}:=(G(\mathbb{Z}))^{p^{-k}}$. Then by Item 3 of Lemma 3.3 there exists $D$, depending only on $G$, such that
$$\left|\Gamma_{k}: G(\mathbb{Z})\right| \leq p^{D k} .$$
Hence, any $\Delta \in \mathcal{L}_{p^{k}}(G)$ is a subgroup of $\Gamma_{k}$ of index at most $p^{(1+D) k}$, giving
$$\mathbf{c}_{p^{k}}(\mathcal{L}(G)) \leq s_{p^{(1+D) k}}\left(\Gamma_{k}\right) \leq s_{p^{(1+D) k}}(N) .$$
where $s_{m}(G)$ is the subgroup growth function (the number of subgroups of index at most $m$ ) and $N$ is the free nilpotent group of class and rank equal to that of $G(\mathbb{Z})$. It follows from [GSS88] that $s_{p^{(1+D) k}}(N) \leq p^{\alpha k}$ for some fixed $\alpha$ that does not depend on $p$. Hence, Inequality (6) gives that $\zeta_{G, p}(s)$ is finite for $s>M$ where $M$ does not depend on $p$.

The integrand in Proposition 3.12 and $\mathfrak{U}_{p}$ are both $L_{p}$-definable in the sense of [Mac90] (see also [Den84]) by Lemma 3.9] Thus, by [Mac90, Theorem 22] we have that $\zeta_{G, p}(s)$ is a rational function with numerator and denominator degrees bounded by a constant depending only on $G$. \(\square\)

\section*{References}
\begin{itemize}
\item[] [ALN12] Nir Avni, Seonhee Lim, and Eran Nevo, On commensurator growth, Israel J. Math. 188 (2012), 259-279. MR 2897732
\item[] [Den84] J. Denef, The rationality of the Poincaré series associated to the $p$-adic points on a variety, Invent. Math. 77 (1984), no. 1, 1-23. MR 751129
\item[] [dS93] Marcus P. F. du Sautoy, Finitely generated groups, $p$-adic analytic groups and Poincaré series, Ann. of Math. (2) 137 (1993), no. 3, 639-670. MR 1217350
\item[] [GO85] Fritz Grunewald and Joyce O'Halloran, Nilpotent groups and unipotent algebraic groups, J. Pure Appl. Algebra 37 (1985), no. 3, 299-313. MR 797867
\item[] [GSS88] F. J. Grunewald, D. Segal, and G. C. Smith, Subgroups of finite index in nilpotent groups, Invent. Math. 93 (1988), no. 1, 185-223. MR 943928 (89m:11084)
\item[] [HW08] G. H. Hardy and E. M. Wright, An introduction to the theory of numbers, sixth ed., Oxford University Press, Oxford, 2008, Revised by D. R. Heath-Brown and J. H. Silverman, With a foreword by Andrew Wiles. MR 2445243
\item[] [Klo11] Benjamin Klopsch, An introduction to compact $p$-adic Lie groups, Lectures on profinite topics in group theory, London Math. Soc. Stud. Texts, vol. 77, Cambridge Univ. Press, Cambridge, 2011, pp. 7-61. MR 2807855
\item[] [Ko148] E. R. Kolchin, Algebraic matric groups and the Picard-Vessiot theory of homogeneous linear ordinary differential equations, Ann. of Math. (2) 49 (1948), 1-42. MR 0024884
\item[] [LS03] Alexander Lubotzky and Dan Segal, Subgroup growth, Progress in Mathematics, vol. 212, Birkhäuser Verlag, Basel, 2003. MR 1978431
\item[] [Mac90] Angus Macintyre, Rationality of $p$-adic Poincaré series: uniformity in $p$, Ann. Pure Appl. Logic 49 (1990), no. 1, 31-74. MR 1076249
\item[] [Mc71] AnatoliĭIvanovi c Mal' cev, The metamathematics of algebraic systems. Collected papers: 1936-1967, North-Holland Publishing Co., Amsterdam-London, 1971, Translated, edited, and provided with supplementary notes by Benjamin Franklin Wells, III, Studies in Logic and the Foundations of Mathematics, Vol. 66. MR 0349383
\item[] [Seg83] Daniel Segal, Polycyclic groups, Cambridge Tracts in Mathematics, vol. 82, Cambridge University Press, Cambridge, 1983. MR 713786
\item[] [Vol11] Christopher Voll, A newcomer's guide to zeta functions of groups and rings, Lectures on profinite topics in group theory, London Math. Soc. Stud. Texts, vol. 77, Cambridge Univ. Press, Cambridge, 2011, pp. 99-144. MR 2807857
\item[] [Wil98] John S. Wilson, Profinite groups, London Mathematical Society Monographs. New Series, vol. 19, The Clarendon Press, Oxford University Press, New York, 1998. MR 1691054
\end{itemize}

Khalid Bou-Rabee
Department of Mathematics, City College of New York
E-mail: kbourabee@ccny.cuny.edu
Daniel Studenmund
Department of Mathematics, University of Notre Dame
E-mail: dstudenm@nd.edu