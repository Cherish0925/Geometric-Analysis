# Invariants of some compactified Picard modular surfaces and applications

- Category: papers
- Identity: arxiv:1411.3381
- Content status: fulltext_ok

---

---
source_file: 1411_3381.pdf
converter: mathpix
format: mmd
---

\title{
Invariants of some compactified Picard modular surfaces and applications
}

\author{
Amir Džambić \\ Institut für Mathematik \\ Goethe-Universität Frankfurt \\ Robert-Mayer Str. 6-8, 60325 Frankfurt am Main \\ Email: dzambic@math.uni-frankfurt.de
}

\begin{abstract}
The paper investigates invariants of compactified Picard modular surfaces by principal congruence subgroups of Picard modular groups. The applications to the surface classification and modular forms are discussed.
\end{abstract}

\section*{1 Introduction}

The following note should be considered as a supplement to the work of R. P. Holzapfel on invariants of Picard modular surfaces which are quotients of the two dimensional complex ball by principal congruence subgroups.
In his papers [Hol80] and [Hol98a], Holzapfel developes concrete formulas for the Chern numbers and related invariants of compactified ball quotients by principal congruence subgroups $\Gamma_{K}(N)$ of Picard modular groups $\Gamma_{K}=\operatorname{SU}\left((2,1), \mathcal{O}_{K}\right)$ where $K=\mathbb{Q}(\sqrt{-d})$ is an imaginary quadratic field and $N$ is a positive integer. There, he uses results which are mainly developed in [Hol98b]. Using Riemann-Roch theory in combination with proportionality theorems, he also gets informations on the classification of these compactified ball quotients and dimensions of spaces of cusp forms relative to the congruence subgroups.
In this article we slightly extend Holzapfel's results considering not only principal congruence subgroups by natural numbers, but also general integral ideals $\mathfrak{a}$ of the quadratic field $K=\mathbb{Q}(\sqrt{-d})$. Including some technical number theoretical details, Holzapfel's arguments can also be applied to this slightly more general and larger class of congruence subgroups. One technical result is a formula for the index $\left[\Gamma_{K}: \Gamma_{K}(\mathfrak{a})\right]$. The final results in principle do not differ from those obtained in [Hol80] und [Hol98a]: We characterize the class of principal congruence subgroups - excluding few technically caused possible "exceptional cases" - for which the (smooth) compactified ball quotient is a surface of general type. For these surfaces the "coordinates" $\left(c_{2}, c_{1}^{2}\right)$ in the surface geography are explicitly known. The dimensions of spaces of cusp forms can also be computed explicitely.

\section*{2 Picard modular groups and their congruence subgroups}

Let $K=\mathbb{Q}(\sqrt{-d})$ be an imaginary quadratic field, and denote $\mathcal{O}_{K}$ the ring of integers of $K$. Let $V$ be a 3-dimensional $K$-vector space equipped with a hermitian form $h: V \times V \longrightarrow K$. Let us assume that the signature of $h$ is (2, 1), i. e. that $h$ has two positive and one negative eigenvalue. Such $h$ can, for instance be represented by the diagonal matrix $\operatorname{diag}(1,1,-1)$, but often it is useful to use another hermitian form. We consider the special unitary group
$$\mathbf{G}:=\operatorname{SU}(h)=\left\{g \in \operatorname{SL}_{3}(\mathbb{C}) \mid h(g v, g w)=h(v, w) \text { for all } v, w \in V_{\mathbb{C}}\right\}$$
as an algebraic group defined over $\mathbb{Q}$. Its group of $\mathbb{Q}$-rational points is
$$\mathbf{G}(\mathbb{Q}):=\operatorname{SU}(h, K)=\left\{g \in \mathrm{SL}_{3}(K) \mid h(g v, g w)=h(v, w), \text { for all } v, w \in V\right\} .$$
Often the interpretation of G as a group corresponding to an involution is useful. For this, we remark that the map $\iota=\iota_{h}$ which associates with every matrix $g \in M_{3}(K)$ the matrix $g^{\iota h}:=M_{h} \bar{g}^{t} M_{h}^{-1}, M_{h}$ denoting the matrix which represents $h$ with respect to a suitable basis (diag(1,1,-1) say), defines an involution of second kind on the matrix algebra $M_{3}(K)$. This means that $\iota$ is an anti-automorphism of $M_{3}(K)$ which acts as the complex conjugation, when restricted to the diagonal matrices $\operatorname{diag}(\alpha, \alpha, \alpha)$. In this description the group G appears as the groups of all matrices $g \in \mathrm{SL}_{3}$ such that $g g^{\iota h}=1_{3}$.

We define the so-called full Picard modular group as
$$\Gamma_{K}=\mathrm{SU}\left(h, \mathcal{O}_{K}\right)=\mathrm{SL}_{3}\left(\mathcal{O}_{K}\right) \cap \mathbf{G}(\mathbb{Q}) .$$
$\Gamma_{K}$ is obviously an arithmetic subgroup in $\mathbf{G}(\mathbb{Q})$ as well as its subgroups of finite index which we simply call Picard modular groups. If $\mathfrak{a}$ is an ideal of $\mathcal{O}_{K}$, let $\Gamma_{K}(\mathfrak{a})$ denote the principal congruence subgroup of $\Gamma_{K}$ with respect to $\mathfrak{a}$. It is defined as the subgroup of $\Gamma_{K}$ consisting of all elements $\gamma \in \Gamma_{K}$ such that $\gamma-1_{3} \in M_{3}(\mathfrak{a})$. In other words, $\Gamma_{K}(\mathfrak{a})$ can be defined as the kernel of the canonical reduction map
$$\rho: \Gamma_{K} \longrightarrow \operatorname{SL}_{3}\left(\mathcal{O}_{K} / \mathfrak{a}\right) .$$
We define the level of $\Gamma_{K}(\mathfrak{a})$ as the absolute norm $N(\mathfrak{a})=\left|\mathcal{O}_{K} / \mathfrak{a}\right|$. There are finitely many principal congruence subgroups of fixed level. By definition a congruence subgroup of $\Gamma_{K}$ is a group which contains a principal congruence subgroup. Since every principal congruence subgroup has a finite index in $\Gamma_{K}$ (which is obvious by definition), all congruence subgroups are Picard modular groups. In this section we will treat the following two technical problems:
\begin{itemize}
\item[-] Compute the index $\left[\Gamma_{K}: \Gamma_{K}(\mathfrak{a})\right]$.
\item[-] Determine $\mathfrak{a}$ for which the principal congruence subgroup $\Gamma_{K}(\mathfrak{a})$ is a neat subgroup.
\end{itemize}
Thereby we say that an arithmetic group is neat, if the subgroup of $\mathbb{C}^{*}$ generated by the eigenvalues of all elements in $\Gamma$ is torsion free. A neat group is obviously torsion free.

\subsection*{2.1 Index computations}

In order to compute the index $\left[\Gamma_{K}: \Gamma_{K}(\mathfrak{a})\right]$, we make use of some local-to-global principles which are applicable in the present case.
For a prime number $p$ the group of $\mathbb{Q}_{p}$-rational points $\mathbf{G}\left(\mathbb{Q}_{p}\right)$ is
$$\mathbf{G}\left(\mathbb{Q}_{p}\right)=\left\{g \in \mathrm{SL}_{3}\left(K \otimes_{\mathbb{Q}} \mathbb{Q}_{p}\right) \mid g g^{\iota_{p}}=1_{3}\right\},$$
where we write $\iota_{p}$ for the natural extension of $\iota_{h}$ to the algebra $M_{3}\left(K \otimes_{\mathbb{Q}} \mathbb{Q}_{p}\right)$. The group $\mathbf{G}\left(\mathbb{Z}_{p}\right)$ is defined in an obvious manner. We can also define principal congruence subgroups $\mathbf{G}\left(\mathbb{Z}_{p}\right)(\mathfrak{a})$ of $\mathbf{G}\left(\mathbb{Z}_{p}\right)$ in the same way as in the case $\Gamma_{K}$, now taking two-sided ideals $\mathfrak{a}$ of the order $\mathcal{O}_{K} \otimes \mathbb{Z}_{p}$ into account. The following lemma is the starting point of the index calculation. It is an important consequence of the strong approximation.

Lemma 2.1. Let $\mathfrak{a} \subset \mathcal{O}_{K}$ be an integral ideal of $K$ and let $\mathfrak{a}=\mathfrak{p}_{1}^{e_{1}} \cdots \mathfrak{p}_{t}^{e_{t}}$ be the prime ideal decomposition of $\mathfrak{a}$, and denote $p_{i}=\mathfrak{p}_{i} \cap \mathbb{Z}$ the unique integer prime over which $\mathfrak{p}$ lies. Then, there is an isomorphism
$$\Gamma_{K} / \Gamma_{K}(\mathfrak{a}) \cong \prod_{i=1}^{t} \mathbf{G}\left(\mathbb{Z}_{p_{i}}\right) / \mathbf{G}\left(\mathbb{Z}_{p_{i}}\right)\left(\mathfrak{p}^{e_{i}}\right) .$$

In particular
$$\left[\Gamma_{K}: \Gamma_{K}(\mathfrak{a})\right]=\prod_{i=1}^{t}\left[\mathbf{G}\left(\mathbb{Z}_{p_{i}}\right): \mathbf{G}\left(\mathbb{Z}_{p_{i}}\right)\left(\mathfrak{p}^{e_{i}}\right)\right]$$
Proof. Let $\lambda$ be the map
$$\lambda: \Gamma_{K} \longrightarrow \prod_{i=1}^{t} \mathbf{G}\left(\mathbb{Z}_{p_{i}}\right) / \mathbf{G}\left(\mathbb{Z}_{p_{i}}\right)\left(\mathfrak{p}^{e_{i}}\right)$$
given by
$$\gamma \mapsto\left(\gamma \bmod \mathfrak{p}_{1}^{e_{1}}, \ldots, \gamma \bmod \mathfrak{p}_{t}^{e_{t}}\right) .$$
The kernel of $\lambda$ is obviously $\Gamma_{K}(\mathfrak{a})$, by definition. To show the surjectivity we recall the strong approximation property: For any given finite set of primes, $p_{1}, \ldots, p_{t}$ say, and given elements $g_{p_{1}} \in$ $\mathbf{G}\left(\mathbb{Z}_{p_{1}}\right), \ldots, g_{p_{t}} \in \mathbf{G}\left(\mathbb{Z}_{p_{t}}\right)$ as well as exponents $e_{1}, \ldots, e_{t}$ one can find an element $g \in \mathbf{G}(\mathbb{Z})=\Gamma_{K}$ such that $g \equiv g_{p_{i}} \bmod p_{i}^{e_{i}}$ for $i=1, \ldots, t$. But as $\mathfrak{p}_{i} \mid p_{i}$ this $g$ satisfies $g \equiv g_{p_{i}} \bmod \mathfrak{p}_{i}^{e_{i}}$. This already proves the surjectivity of $\lambda$. \(\square\)

In order to compute the local indices, we first need to know more about the local groups $\mathbf{G}\left(\mathbb{Q}_{p}\right)$. Looking at their definition (2.1) we see that their structure highly depends on the structure of $K \otimes \mathbb{Q}_{p}$, which itself is determined by the decomposition behaviour of the prime $p$. Essentially there are two cases:
\begin{itemize}
\item[i)] $p$ is decomposed in $K=\mathbb{Q}(\sqrt{-d})$. In this case $K \otimes \mathbb{Q}_{p} \cong K_{\mathfrak{p}} \oplus K_{\overline{\mathfrak{p}}}$ with two conjugate prime ideals $\mathfrak{p} \neq \overline{\mathfrak{p}}$ in $\mathcal{O}_{K}$ such that $p=\mathfrak{p} \overline{\mathfrak{p}}$. Therefore $M_{3}\left(K \otimes \mathbb{Q}_{p}\right) \cong M_{3}\left(K_{\mathfrak{p}}\right) \oplus M_{3}\left(K_{\overline{\mathfrak{p}}}\right)$. Since $p$ is decomposed in $K,\left(\frac{-d}{p}\right)=1$ and $-d$ is a square in $\mathbb{Q}_{p}$. Therefore $K_{\mathfrak{p}} \cong K_{\overline{\mathfrak{p}}} \cong \mathbb{Q}_{p}$. The extension of the field automorphism ${ }^{-}: K \longrightarrow K$ to $K \otimes \mathbb{Q}_{p}$ must be an involution on $K_{\mathfrak{p}} \oplus K_{\overline{\mathfrak{p}}} \cong \mathbb{Q}_{p} \oplus \mathbb{Q}_{p}$ and the only possibility is $\overline{(x, y)}=(y, x)$. Therefore the extension $\iota_{p}$ of $\iota=\iota_{h}$ is given by changing the summands in $M_{3}\left(\mathbb{Q}_{p}\right) \oplus M_{3}\left(\mathbb{Q}_{p}\right)$. Now it is easy to see that the projection on one of the summands gives an isomorphy between $\mathbf{G}\left(\mathbb{Q}_{p}\right)$ and $S L_{3}\left(\mathbb{Q}_{p}\right)$, since $\mathbf{G}\left(\mathbb{Q}_{p}\right)$ is defined as the group consisting of those pairs $(g, h) \in \mathrm{SL}_{3}\left(\mathbb{Q}_{p}\right) \oplus \mathrm{SL}_{3}\left(\mathbb{Q}_{p}\right)$ with $\left(g^{-1}, h^{-1}\right)=(h, g)$.
\item[ii)] $p$ is non-decomposed in $K$. In this case there is the unique prime ideal $\mathfrak{p}$ lying over $p$ such that $K \otimes \mathbb{Q}_{p}=K_{\mathfrak{p}}$, which is a quadratic extension of $\mathbb{Q}_{p}$. The extended involution $\iota_{p}$ is an involution of second kind on $M_{3}\left(K_{\mathfrak{p}}\right)$ given by $g \mapsto M_{h} \bar{g} M_{h}^{-1}$ and $\mathbf{G}\left(\mathbb{Q}_{p}\right)=\operatorname{SU}\left(h, K_{\mathfrak{p}}\right)$.
\end{itemize}

Lemma 2.2. If $p$ is non-decomposed, $\mathbf{G}\left(\mathbb{Q}_{p}\right) \cong \operatorname{SU}_{3}\left(K_{\mathfrak{p}}\right)$.
Proof. By Landherr's Theorem, the isometry class of a hermitian form $h$ in $n$ variables associated with a quadratic extension $E / F$ of local fields is uniquely determined by its discriminant $\mathbf{d}(h)=$ $[\operatorname{det}(h)] \in F^{*} / N_{E / F}\left(E^{*}\right) \cong \mathbb{Z} / 2 \mathbb{Z}$. On the other hand the isomorphism class of the associated unitary group $S U(h)$ only depends on $h$ up to multiplicative constant. Hence, the unitary group associated with $\operatorname{diag}(1,1,-1)$ is isomorphic to the unitary group associated with $\operatorname{diag}(-1,-1,1)$. Since the discriminant of the latter is 1, the result follows. \(\square\)

Now we compute the local indices
Lemma 2.3. Let $\mathfrak{p}$ be a prime ideal of $K=\mathbb{Q}(\sqrt{-d})$ such that $p=\mathfrak{p} \cap \mathbb{Z}$ is decomposed in $K$. Then
$$\left[\mathbf{G}\left(\mathbb{Z}_{p}\right): \mathbf{G}\left(\mathbb{Z}_{p}\right)\left(\mathfrak{p}^{n}\right)\right]=p^{8 n}\left(1-p^{-3}\right)\left(1-p^{-2}\right)$$
for any positive integer $n$.
Proof. By our discussion above, in the decomposed case $\mathbf{G}\left(\mathbb{Q}_{p}\right)=\mathrm{SL}_{3}\left(\mathbb{Z}_{p}\right)$ and $\mathbf{G}\left(\mathbb{Z}_{p}\right)\left(\mathfrak{p}^{n}\right)=$ $\mathrm{SL}_{3}\left(\mathbb{Z}_{p}\right)\left(p^{n}\right)$. We note that the sequence
$$1 \longrightarrow S L_{n}\left(\mathbb{Z}_{p}\right)\left(p^{n}\right) \longrightarrow S L_{n}\left(\mathbb{Z}_{p}\right) \longrightarrow S L_{n}\left(\mathbb{Z}_{p} / p^{n} \mathbb{Z}_{p}\right) \longrightarrow 1$$
is exact. In fact, (2.2) is exact even if we replace $\mathbb{Z}_{p}$ and $p^{n}$ by any commutative ring $R$ and ideal $\mathfrak{I}$ such that $R / \mathfrak{I}$ is finite (see [Bas64], Cor. 5.2). Therefore
$$\left[\mathbf{G}\left(\mathbb{Z}_{p}\right): \mathbf{G}\left(\mathbb{Z}_{p}\right)\left(\mathfrak{p}^{n}\right)\right]=\left|S L_{3}\left(\mathbb{Z}_{p} / p^{n} \mathbb{Z}_{p}\right)\right|=\left|S L_{3}\left(\mathbb{Z} / p^{n} \mathbb{Z}\right)\right| .$$
The latter number can be computed in an elementary way:
Denote $\rho: \mathrm{GL}_{3}\left(\mathbb{Z} / p^{n} \mathbb{Z}\right) \longrightarrow \mathrm{GL}_{3}(\mathbb{Z} / p \mathbb{Z})$ the canonical projection map which sends every residue $\bmod p^{n}$ to its residue $\bmod p$. The kernel $\operatorname{ker}(\rho)$ consists of $p^{9(n-1)}$ elements. With the well-known number $\left|\mathrm{GL}_{3}(\mathbb{Z} / p \mathbb{Z})\right|=p^{9}\left(1-p^{-3}\right)\left(1-p^{-2}\right)\left(1-p^{-1}\right)$, we get $\left|\mathrm{GL}_{3}\left(\mathbb{Z} / p^{n} \mathbb{Z}\right)\right|=p^{9 n}\left(1-p^{-3}\right)(1-$ $\left.p^{-2}\right)\left(1-p^{-1}\right)$. Dividing this number by $\varphi\left(p^{n}\right)$ which is the order of the multiplicative group $\left(\mathbb{Z} / p^{n} \mathbb{Z}\right)^{*}$ we get the desired result. \(\square\)

For some technical reasons we exclude from now on the prime 2 from our consideration.
Lemma 2.4. Let $\mathfrak{p}$ be a prime ideal in $\mathcal{O}_{K}$ and $p=\mathfrak{p} \cap \mathbb{Z} \neq 2$ non-decomposed. For every $n \geq 1$ the following holds:
\begin{itemize}
\item[1.] If $p$ is inert,
$$\left[\mathbf{G}\left(\mathbb{Z}_{p}\right): \mathbf{G}\left(\mathbb{Z}_{p}\right)\left(\mathfrak{p}^{n}\right)\right]=p^{8 n}\left(1+p^{-3}\right)\left(1-p^{-2}\right) .$$
\item[2.] If $p$ is ramified,
$$\left[\mathbf{G}\left(\mathbb{Z}_{p}\right): \mathbf{G}\left(\mathbb{Z}_{p}\right)\left(\mathfrak{p}^{n}\right)\right]=p^{\epsilon_{n}}\left(1-p^{-2}\right),$$
where $\epsilon_{n}$ is defined as
$$\epsilon_{n}=\left\{\begin{array}{cc}
4 n & \text { if } n \equiv 0 \bmod 2 \\
4 n-1 & \text { if } n \equiv 1 \bmod 2
\end{array}\right.$$
\end{itemize}
Proof. First, we identify the asked index with the order of the finite group $\operatorname{SU}\left(\bar{h}, \mathcal{O}_{\mathfrak{p}} / \mathfrak{p}^{n}\right)$, where $\mathcal{O}_{\mathfrak{p}}=\mathcal{O}_{K_{\mathfrak{p}}}$ denotes the ring of integers in $K_{\mathfrak{p}}$ and $\bar{h}$ the restriction of $h$ to $\mathcal{O}_{\mathfrak{p}} / \mathfrak{p}^{n}$. To do so, we have to prove the surjectivity of the canonical reduction map $\mathbf{G}\left(\mathbb{Z}_{p}\right)=\operatorname{SU}\left(h, \mathcal{O}_{\mathfrak{p}}\right) \longrightarrow \operatorname{SU}\left(h, \mathcal{O}_{\mathfrak{p}} / \mathfrak{p}^{n}\right)$. But this follows from the identity
$$\mathbf{G}\left(\mathbb{Z}_{p}\right) / \mathbf{G}\left(\mathbb{Z}_{p}\right)\left(p^{n}\right) \cong \operatorname{SU}\left(\bar{h}, \mathcal{O}_{\mathfrak{p}} / p^{n}\right),$$
see [Hol98b, Prop. 5A.2.7], and the surjectivity of the reduction $\operatorname{SU}\left(\bar{h}, \mathcal{O}_{\mathfrak{p}} / p^{n}\right) \longrightarrow \mathrm{SU}\left(\bar{h}, \mathcal{O}_{\mathfrak{p}} / \mathfrak{p}^{n}\right)$. Moreover, we can extract the above local index formulas again from [Hol98b, Cor. 5A.1.3] for the case in which $p$ is inert, or $p$ is ramified and $n$ is an even positive integer. According to this, the only non trivial case is the situation where $p$ is ramified and $n$ is odd. Let us from now on assume this situation, that is, $p$ is ramified and $n$ is odd.
By [Hol98b, Cor. 5A.1.3] again we know that
$$\mathbf{G}\left(\mathbb{Z}_{p}\right) / \mathbf{G}\left(\mathbb{Z}_{p}\right)\left(\mathfrak{p}^{n+1}\right)=\left|\mathbf{G}\left(\mathbb{Z}_{p}\right) / \mathbf{G}\left(\mathbb{Z}_{p}\right)\left(p^{(n+1) / 2}\right)\right|=p^{4(n+1)}\left(1-p^{-2}\right) .$$
By the multiplicativity of index we obtain
$$\mathbf{G}\left(\mathbb{Z}_{p}\right) / \mathbf{G}\left(\mathbb{Z}_{p}\right)\left(\mathfrak{p}^{n}\right)=p^{4(n+1)}\left(1-p^{-2}\right) /\left[\mathbf{G}\left(\mathbb{Z}_{p}\right)\left(\mathfrak{p}^{n}\right) / \mathbf{G}\left(\mathbb{Z}_{p}\right)\left(\mathfrak{p}^{n+1}\right)\right] .$$
In order to compute the index in the denominator, we first recall the isomorphism $\mathbf{G}\left(\mathbb{Q}_{p}\right) \cong$ $\mathrm{SU}_{3}\left(K_{\mathfrak{p}}\right)$ from Lemma 2.2. Let $\pi$ be a generator of the valuation ideal $\mathfrak{p}$ of $\mathcal{O}_{\mathfrak{p}}$. As $p \neq 2$, the extension $K_{\mathfrak{p}} / \mathbb{Q}_{p}$ is tamely ramified and we can choose $\pi$ such that $\bar{\pi}=-\pi$, where ${ }^{-}$denotes the conjugation in $K_{\mathfrak{p}}$ (compare [Lan70, Prop. II.5.12] ).
As a matrix in $M_{3}\left(K_{\mathfrak{p}}\right)$, every $g \in \mathbf{G}\left(\mathbb{Z}_{p}\right)$ has a $\mathfrak{p}$-adic representation:
$$g=g_{0}+\pi g_{1}+\pi^{2} g_{2}+\pi^{3} g_{3}+\ldots,$$
with some matrices $g_{j} \in M_{3}\left(\mathcal{O}_{\mathfrak{p}} / \mathfrak{p}\right)=M_{3}(\mathbb{Z} / p \mathbb{Z})$, where the latter equation holds since $p$ is ramified. We note that a matrix $g \in \mathbf{G}\left(\mathbb{Z}_{p}\right)$ lies in $\mathbf{G}\left(\mathbb{Z}_{p}\right)\left(\mathfrak{p}^{n}\right)$ if and only if its $\mathfrak{p}$-adic representation starts with
$$g=1_{3}+\pi^{n} g_{n}+\pi^{n+1} g_{n+1}+\ldots .$$

For this reason, the application $g \mapsto g_{n}$ gives a map
$$\mathbf{G}\left(\mathbb{Z}_{p}\right) / \mathbf{G}\left(\mathbb{Z}_{p}\right)\left(\mathfrak{p}^{n}\right) \longrightarrow M_{3}(\mathbb{Z} / p \mathbb{Z}) .$$
We further note that, as $p$ is ramified, the conjugation acts as the identity on $\mathcal{O}_{\mathfrak{p}} / \mathfrak{p}^{n}$. Now let us consider a representative $g \in \mathbf{G}\left(\mathbb{Z}_{p}\right)\left(\mathfrak{p}^{n}\right)$ of the class $[g] \in \mathbf{G}\left(\mathbb{Z}_{p}\right)\left(\mathfrak{p}^{n}\right) / \mathbf{G}\left(\mathbb{Z}_{p}\right)\left(\mathfrak{p}^{n+1}\right)$. Two equations characterize $g$ as an element of $\mathrm{SU}_{3}\left(K_{\mathfrak{p}}\right): g$ is hermitian, that is, $g \bar{g}^{t}=\left(1_{3}+\pi^{n} g_{n}+\ldots\right)\left(1_{3}+\bar{\pi}^{n} \bar{g}_{n}+\right.$ $\ldots)^{t}=1_{3}$ or equivalently $\left(1_{3}+\pi^{n} g_{n}+\ldots\right)\left(1_{3}-\pi^{n} \bar{g}_{n}^{t}+\ldots\right)=1_{3}$. In other words $g_{n}-g_{n}^{t}=0$, that is, $g_{n}$ is symmetric. On the other hand, as $\operatorname{det}(g)=\operatorname{det}\left(1_{3}+\pi^{n} g_{n}+\ldots\right)=1 \equiv 1+\pi^{n} \operatorname{Tr}\left(g_{n}\right) \bmod \pi^{n+1}$, $g_{n}$ has trace 0. By this, the factor group $\mathbf{G}\left(\mathbb{Z}_{p}\right)\left(\mathfrak{p}^{n}\right) / \mathbf{G}\left(\mathbb{Z}_{p}\right)\left(\mathfrak{p}^{n+1}\right)$ is characterized as the set of symmetric matrices in $M_{3}(\mathbb{Z} / p \mathbb{Z})$ with trace equal to 0. There are exactly $p^{5}$ such matrices, and the equation (2.3) gives for $n$ odd and $p$ ramified
$$\mathbf{G}\left(\mathbb{Z}_{p}\right) / \mathbf{G}\left(\mathbb{Z}_{p}\right)\left(\mathfrak{p}^{n}\right)=p^{4 n-1}\left(1-p^{-2}\right),$$
from which the final formula follows. \(\square\)

Now, summarizing results from Lemma 2.3 and Lemma 2.4, we get
Theorem 2.5. Let $\mathfrak{a}$ be an integral ideal in $K=\mathbb{Q}(\sqrt{-d})$ and let $\mathfrak{a}=\mathfrak{p}_{1}^{e_{1}} \cdots \mathfrak{p}_{t}^{e_{t}}$ be the prime ideal decomposition of $\mathfrak{a}$ with $p_{i}=\mathfrak{p}_{i} \cap \mathbb{Z}$. Assume that $p_{i} \neq 2$ for all $i=1, \ldots t$, if 2 is non-decomposed in $K$. Then it holds
$$\left[\Gamma_{K}: \Gamma_{K}(\mathfrak{a})\right]=\prod_{i=1}^{t} p^{\epsilon_{i}}\left(1-p_{i}^{-2}\right)\left(1-\chi_{D}\left(p_{i}\right) p_{i}^{-3}\right),$$
where $D$ is the discriminant of $K, \chi_{D}()$ is the Jacobi symbol $\chi_{D}(p)=\left(\frac{D}{p}\right)$ and $\epsilon_{i}$ is defined by
$$\epsilon_{i}=\left\{\begin{array}{cl}
8 e_{i}, & \text { if } \chi_{D}\left(p_{i}\right) \neq 0 \\
4 e_{i}, & \text { if } \chi_{D}\left(p_{i}\right)=0 \text { and } e_{i} \equiv 0 \bmod 2 \\
4 e_{i}-1, & \text { if } \chi_{D}\left(p_{i}\right)=0 \text { and } e_{i} \equiv 1 \bmod 2
\end{array}\right.$$

We remark that this result generalizes [Hol98b, Theorem 5A.2.14].

\subsection*{2.2 Determination of neat subgroups}

In this section we discuss the question, for which integral ideals $\mathfrak{a}$ the principal congruence subgroup $\Gamma_{K}(\mathfrak{a})$ is a neat subgroup. This rather technical property will be used in our consideration of Picard modular surfaces.

Lemma 2.6. Assume that $\mathfrak{a}$ is an ideal in $\mathcal{O}_{K}$ such that $\mathfrak{a} \cap \mathbb{Z}$ and 2 are coprime. Then, the principal congruence subgroup $\Gamma_{K}(\mathfrak{a})$ is neat if $N(\mathfrak{a})>3$.
Proof. (compare [Hol80, Lemma 4.3])
Assume that $\Gamma_{K}(\mathfrak{a})$ is not neat. Then, there are eigenvalues $\zeta$ of elements $\gamma \in \Gamma_{K}(\mathfrak{a})$ which generate a torsion subgroup in $\mathbb{C}^{*}$. One concludes that such eigenvalues must be roots of unity (Hol80, proof of Lemma 4.3]). Now, on the one hand, such an eigenvalue $\zeta$ is a root of unity, $n$-th root of unity say, and on the other hand, $\zeta$ is a zero of the characteristic polynomial of $\gamma$ which has degree 3 over $K$. Therefore $[\mathbb{Q}(\zeta): \mathbb{Q}]=\varphi(n) \leq 6$. Without loss of generality we can assume that $n=p$ is a prime number. So, in fact we have to check that for $n=2,3,5,7$ the primitive $n$-th root of unity does not appear as the the eigenvalue of elements in $\Gamma_{K}(\mathfrak{a})$ for stated ideals $\mathfrak{a}$. For this, we first observe that there is a relation between the eigenvalues $\zeta$ of elements in $\Gamma_{K}(\mathfrak{a})$ and the ideal $\mathfrak{a}$, namely
$$\mathfrak{a} \mathbb{Z}[\zeta] \mid(\zeta-1) \mathbb{Z}[\zeta]$$
Taking norms on both sides we obtain
$$N(\mathfrak{a} \mathbb{Z}[\zeta])=N(\mathfrak{a})^{\varphi(n) / 2} \mid N_{\mathbb{Q}(\zeta) / \mathbb{Q}}(\zeta-1)=n .$$
It is easely checked that none of the above primes satisfies this relation by given $\mathfrak{a}$ with $(2, \mathfrak{a} \cap \mathbb{Z})=1$ and $N(\mathfrak{a})>3$. \(\square\)

\section*{3 Proportionality principle for compactified Picard modular surfaces}

As a non-compact almost simple Lie group, $\mathbf{G}(\mathbb{R})=\operatorname{SU}(h, \mathbb{C})$ has a naturally associated irreducible simply connected hermitian symmetric domain $\mathbb{B}=\operatorname{SU}(h) / C$, with a maximal compact subgroup $C$. Taking $h$ to be represented by $\operatorname{diag}(1,1,-1)$ this symmetric domain is exactly the 2-dimansional complex unit ball
$$\mathbb{B}=\mathbb{B}_{2}=\left\{\left.\left(z_{1}, z_{2}\right)| | z_{1}\right|^{2}+\left|z_{2}\right|^{2}<1\right\} .$$
It is more natural to consider $\mathbb{B}$ embedded in $\mathbb{P}_{2}(\mathbb{C})$ which is interpreted as the compact dual symmetric space of $\mathbb{B}$. From the construction of $\mathbb{B}$ it is clear that the group $\operatorname{SU}(h)$ acts on $\mathbb{B}$ as a group of biholomorphic transformations. According to the theorem of Borel and Harish-Chandra (see [BHC62]), the group $\Gamma_{K}$, and consequently every group $\Gamma$ commensurable to $\Gamma_{K}$ is a discrete subgroup of finite covolume in the Lie group $\mathbf{G}(\mathbb{R})=\operatorname{SU}(h, \mathbb{C})$ corresponding to G. Therefore, the action of each $\Gamma$ is properly discontinuous, and it is reasonable to consider the quotient space $Y(\Gamma):=\Gamma \backslash \mathbb{B}$. Now we recall some basic properties of $Y(\Gamma)$

Theorem 3.1. Let $\Gamma \subset \Gamma_{K}$ be a Picard modular group and $Y(\Gamma)=\Gamma \backslash \mathbb{B}$ the corresponding locally symmetric space. Then the following hold:
\begin{itemize}
\item[1.] $Y(\Gamma)$ is not compact.
\item[2.] There exists a compactification $\overline{Y(\Gamma)}$ of $Y(\Gamma)$, which set theoreticaly is $Y(\Gamma) \cup\{$ finitely many points $\}$ and has a structure of a normal projective variety. $\overline{Y(\Gamma)}$ is called the Baily-Borel compactification.
\item[3.] There exists a rational map $\widetilde{Y(\Gamma)} \longrightarrow \overline{Y(\Gamma)}$ such that $\widetilde{Y(\Gamma)}$ is smooth. $\widetilde{Y(\Gamma)}$ is called the smooth compactification of $Y(\Gamma)$.
\end{itemize}

The proof of the above statements, which are in fact special cases of theorems, being valid in much greater generality, can be found in [Hol98b]. Let us roughly sketch the main steps of the proofs, also in order to introduce some notions which will be used later. The non-compactness follows from [BHC62, 11. 8.]. By this theorem $Y(\Gamma)$ is compact if and only if there are no non-trivial unipotent elements in $\mathbf{G}(\mathbb{Q})$. But there are many unipotent elements and they all lie in the unipotent radicals of minimal rational parabolic subgroups of G, which themselves fix maximal $h$ -isotropic subspaces of $V=K^{3}$. The compactification $\overline{Y(\Gamma)}$ of $Y(\Gamma)$ is obtained by taking quotient $\overline{Y(\Gamma)}=\Gamma \backslash \mathbb{B}^{*}$, where $\mathbb{B}^{*}=\mathbb{B} \cup \partial_{\mathbb{Q}} \mathbb{B}$ with $\partial_{\mathbb{Q}} \mathbb{B}=\mathbf{G}(\mathbb{Q}) / \mathbf{P}$ with some fixed rational parabolic subgroup $\mathbf{P} \subset \mathbf{G}$. By a suitable choice of $\mathbf{P}$ one can assume that $\partial_{\mathbb{Q}} \mathbb{B}=\left\{[v] \in \mathbb{P}_{2}(K) \mid h(v, v)=0\right\}$. The set $\partial_{\Gamma} \mathbb{B}=\Gamma \backslash \mathbf{G}(\mathbb{Q}) / \mathbf{P}$ is finite, so $\overline{Y(\Gamma)}=Y(\Gamma) \cup\{$ finitely many points $\}$. By the theorem of Baily-Borel $\overline{Y(\Gamma)}$ is a normal projective variety. The singularities come from non-trivial torsion elements in $\Gamma$ and possibly from cusps, that is, points of $\overline{Y(\Gamma)}-Y(\Gamma)$. If we assume that $\Gamma$ is neat, the theory of toroidal compactifications (see Hol98b, chapter 4] for the special case of arithmetic lattices in $\operatorname{SU}(2,1)$ ) provides a smooth compactification by replacing every cusp by a smooth elliptic curve. Note that by a theorem of Borel neat normal subgroups $\Gamma^{\prime} \triangleleft \Gamma_{K}$ of finite index exist. If $\Gamma$ is not neat, the toroidal compactification provides a surface with at most quotient singularities. They can be resolved by known methods. This resolution gives a map $\widetilde{Y(\Gamma)} \rightarrow \overline{Y(\Gamma)}$, with smooth $\widetilde{Y(\Gamma)}$.

\subsection*{3.1 Chern numbers of compactified Picard modular surfaces}

The two Chern numbers $c_{2}$ and $c_{1}^{2}$ of a smooth compact complex surface are important numerical invariants. The famous proportionality theorem of F. Hirzebruch states that the Chern numbers of a (2-dimensional) ball quotient by a torsion free cocompact discrete subgroup satisfy $c_{1}^{2}=3 c_{2}$. D. Mumford generalized Hirzebruch's theorem also to non-compact quotients. Before we state the proportionality result for Picard modular groups, as described in [Hol98b], we need to introduce
some notions.
Let $\Gamma$ be a neat Picard modular group. The quotient $Y(\Gamma)$ is not compact, but one can still define Chern numbers of $Y(\Gamma)$ as the volumes
$$\begin{aligned}
& c_{2}(Y(\Gamma))=\int_{F(\Gamma)} \eta_{2} \\
& c_{1}^{2}(Y(\Gamma))=\int_{F(\Gamma)} \eta_{1}^{2}
\end{aligned}$$
where $F(\Gamma)$ is a fundamental domain of $\Gamma$ in $\mathbb{B}$ and $\eta_{2}$ and $\eta_{1}^{2}$ are suitably normalized volume forms related to the $\Gamma$-invariant Bergman metric on $\mathbb{B}$.
On the other hand, on the smooth compactification $\widetilde{Y(\Gamma)}$ of $Y(\Gamma)$ there are also usual Chern numbers. Before we relate these two kind of Chern numbers, we note that $\widetilde{Y(\Gamma)}$ arises from $Y(\Gamma)$ by replacing a cusp $\kappa \in \partial_{\Gamma} \mathbb{B}$ by an elliptic curve $E_{\kappa}$. Hence, the difference between $\widetilde{Y(\Gamma)}$ and $Y(\Gamma)$ is encoded in the compactification divisor $T_{\Gamma}=\sum_{\kappa \in \partial_{\Gamma} \mathbb{B}} E_{\kappa}$.

Proposition 3.2. (Hol98b, Proposition 4.3.6]) Let $\Gamma$ be a neat Picard modular group, $Y(\Gamma)=$ $\Gamma \backslash \mathbb{B}, \widetilde{Y(\Gamma)}$ the smooth compactification of $Y(\Gamma)$ and $T_{\Gamma}$ the compactification divisor. Let $\left(T_{\Gamma} . T_{\Gamma}\right)$ denote the selfintersection number of $T_{\Gamma}$. Then:
\begin{itemize}
\item[1.] $c_{2}(\widetilde{Y(\Gamma)})=c_{2}(Y(\Gamma))$
\item[2.] $c_{1}^{2}(\widetilde{Y(\Gamma)})=3 c_{2}(Y(\Gamma))+\left(T_{\Gamma} \cdot T_{\Gamma}\right)$
\end{itemize}

\subsection*{3.2 Chern numbers of quotients by principal congruence subgroups}

By the above propostion 3.2, two magnitudes are essential for the computation of Chern invariants of the smooth compactification of a Picard modular surface $Y(\Gamma)=\Gamma \backslash \mathbb{B}$, namely the volume $c_{2}(Y(\Gamma))$ and the selfintersection number $\left(T_{\Gamma} . T_{\Gamma}\right)$. In the case of a ball quotient by a principal congruence subgroup this two numbers can be given in terms of a number theoretic expression. Let us shortly write $Y(\mathfrak{a})$ for the ball quotient $\Gamma_{K}(\mathfrak{a}) \backslash \mathbb{B}$ by the principal congruence subgroup $\Gamma_{K}(\mathfrak{a})$. In this context we also write $Y(1)$ for the quotient $\Gamma_{K} \backslash \mathbb{B}$ by a full Picard modular group.

Proposition 3.3. (see [Hol98b, Thm. 5A.4.7]) Let $K=\mathbb{Q}(\sqrt{-d})$ and let $\Gamma_{K}$ be the full Picard modular group corresponding to $K$. Let $D$ be the discriminant of $K$ and $\chi_{D}()=\left(\frac{D}{.}\right)$ the Dirichlet character associated to $K$. Then
$$c_{2}(Y(1))=c_{2}\left(\Gamma_{K} \backslash \mathbb{B}\right)=\delta_{K} \frac{|D|^{5 / 2}}{32 \pi^{3}} L\left(3, \chi_{D}\right),$$
where $L\left(s, \chi_{D}\right)$ denotes the Dirichlet $L$-function associated with $\chi_{D}$, and $\delta_{K}$ is defined as $\delta_{K}=1 / 3$ if $d=3$, and $\delta_{K}=1$ otherwise.
Consequently, for every integral ideal $\mathfrak{a}$ of $K$ and the principal congruence subgroup $\Gamma_{K}(\mathfrak{a})$
$$c_{2}(Y(\mathfrak{a}))=\left[\Gamma_{K}: \Gamma_{K}(\mathfrak{a})\right] \delta_{K} \frac{|D|^{5 / 2}}{32 \pi^{3}} L\left(3, \chi_{D}\right) .$$
Remark 3.4. The above volume formula can be seen as a special case of a general formula developed by G. Prasad, expressing the volume of a quotient of a Lie group by an arithmetic subgroup, by values of L-functions. The reader can consult [PY07] for the case of the unitary group corresponding to a hermitian form of signature (2, 1).

A similar arithmetic expression for the selfintersection number of the compactification divisor can be deduced using [Hol80, Lemma 4.7, Lemma 4.8]:

Proposition 3.5. Let $h_{K}$ denote the ideal class number of $K$ and let $\eta_{K}$ and $\vartheta_{\mathfrak{a}}$ be defined as
$$\begin{gathered}
\vartheta_{\mathfrak{a}}=\min \{n \in \mathbb{N}|\mathfrak{a}| n \sqrt{-d}\} \\
\eta_{K}= \begin{cases}1 & \text { if } D=-4 \\
1 / 6 & \text { if } D=-3 \\
2 & \text { if } D \neq-4, D \equiv 0 \bmod 4 \\
1 / 2 & \text { if } D \neq-3, D \equiv 1 \bmod 4\end{cases}
\end{gathered}$$
Then, we have the following formula for the selfintersection number $\left(T_{\Gamma_{K}(\mathfrak{a})} \cdot T_{\Gamma_{K}(\mathfrak{a})}\right)$ :
$$\left(T_{\Gamma_{K}(\mathfrak{a})} \cdot T_{\Gamma_{K}(\mathfrak{a})}\right)=-\frac{h_{K} \eta_{K}}{\vartheta_{\mathfrak{a}}^{2}}\left[\Gamma_{K}: \Gamma_{K}(\mathfrak{a})\right] .$$

\subsection*{3.3 Values of Dirichlet L-functions at integers}

In order to get concrete values of Chern numbers of Picard modular surfaces, we need to know the value $L\left(3, \chi_{D}\right)$ explicitely. Let us briefly discuss the well-known method for the computation of this number.

We first recall the functional equation for Dirichlet L-functions (see, for instance, [Was82], chapter 4, in particular Thm. 4.2). This equation implies
$$L\left(3, \chi_{D}\right)=-\frac{2 \pi^{3}}{|D|^{5 / 2}} L\left(-2, \chi_{D}\right)=\frac{2 \pi^{3}}{3|D|^{5 / 2}} B_{3, \chi_{D}} .$$

There, $B_{n, \chi_{D}}$ denotes the $n$-th generalized Bernoulli number associated with $\chi_{D}$ (see Was82, chapter 4] for the definition). The generalized Bernoulli numbers can be computed easily by the following formula, which for instance can be found in [Was82, Proposition 4.2]:
$$B_{n, \chi_{D}}=|D|^{n-1} \sum_{k=1}^{|D|} \chi_{D}(k) B_{n}\left(\frac{k}{|D|}\right) .$$
In the above formula $B_{n}(X)$ denotes the $n$-th Bernoulli polynomial which can be defined as
$$B_{n}(X)=\sum_{k=0}^{n}\binom{n}{k} B_{k} X^{n-k},$$
$B_{k}$ denoting the usual $k$-th Bernoulli number. It is now easy to provide a list of values $L\left(3, \chi_{D}\right)$, knowing $B_{3}(X)=\frac{1}{2} X-\frac{3}{2} X^{2}+X^{3}$. Here we give the first values of $B_{3, \chi_{D}}$ :

\begin{tabular}[t]{|l|l|l|l|l|l|l|l|l|l|l|l|l|}
\hline $|D|$ & 3 & 4 & 7 & 8 & 11 & 15 & 19 & 20 & 23 & 24 & 31 & 35 \\
\hline $B_{3, \chi_{D}}$ & 2/3 & 3/2 & 48/7 & 9 & 18 & 48 & 66 & 90 & 144 & 138 & 288 & 108 \\
\hline
\end{tabular}

\section*{4 Applications}

In this section we discuss some applications of the explicit formulas for the Chern invariants of compactified ball quotients by principal congruence subgroups.

\subsection*{4.1 Classification}

Theorem 4.1. Let $\mathfrak{a}$ be an integral ideal of $K=\mathbb{Q}(\sqrt{-d})$ such that $N(\mathfrak{a})>3$ and $\mathfrak{a} \cap \mathbb{Z}$ and the prime 2 are coprime. The smooth compactification $\widetilde{Y(\mathfrak{a})}=\widetilde{\Gamma_{K}(\mathfrak{a}) \backslash \mathbb{B}}$ is a surface of general type, with the (additional) possible exception for $K=\mathbb{Q}(\sqrt{-7})$ and $\mathfrak{a} \cap \mathbb{Z}$ ramified in $K$.

Proof. First we note that $\widetilde{Y(\mathfrak{a})}$ is smooth and compact algebraic surface, since $\Gamma_{K}(\mathfrak{a})$ is neat by Lemma 2.6 (see also Theorem. 3.1). In order to show that $\widetilde{Y(\mathfrak{a})}$ is of general type it is sufficient to check that $c_{1}^{2}(\widetilde{Y(\mathfrak{a})})>9$. This follows from the classification theory of algebraic surfaces. It is also sufficient to check the inequality only for the surfaces $\widetilde{Y(\mathfrak{p})}$, where $\mathfrak{p}$ is a prime ideal, since the Kodaira dimension can not decrease by the passage to a finite covering. Hence, if $\widetilde{Y(\mathfrak{p})}$ is of general type, then also $\widetilde{Y(\mathfrak{a})}$ for any ideal $\mathfrak{a}$ such that $\mathfrak{p} \mid \mathfrak{a}$.
From Lemma 3.2, Proposition 3.3, and Proposition 3.5, we obtain the following formula for $c_{1}^{2}(\widetilde{Y(\mathfrak{p})})$ :
$$c_{1}^{2}(\widetilde{Y(\mathfrak{p})})=\left[\Gamma_{K}: \Gamma_{K}(\mathfrak{a})\right]\left(\frac{3 \delta_{K}|D|^{5 / 2}}{32 \pi^{3}} L\left(3, \chi_{D}\right)-\frac{h_{K} \eta_{K}}{\vartheta_{\mathfrak{p}}^{2}}\right)$$
Looking at the index formula in Theorem 2.5, we see that $\left[\Gamma_{K}: \Gamma_{K}(\mathfrak{p})\right]>9$ if $N(\mathfrak{p})>3$ and $\mathfrak{p} \cap \mathbb{Z} \neq(2)$. Thus, it suffices to show that
$$\frac{3 \delta_{K}|D|^{5 / 2}}{32 \pi^{3}} L\left(3, \chi_{D}\right)-\frac{h_{K} \eta_{K}}{\vartheta_{\mathfrak{p}}^{2}} \geq 1$$
First we show that the inequality (4.2) holds, if $|D|>35$.
Recall first the analytic class number formula
$$h_{K}=\frac{\mu_{K} \sqrt{-D}}{2 \pi} L\left(1, \chi_{D}\right)=-\left(\mu_{K} / 4\right) B_{1, \chi_{D}},$$
where $\mu_{K}$ denotes the number of roots of unity contained in $K$. Using the facts on generalized Bernoulli numbers summarized in section 3.3, and in particular the formula (3.1), we get a trivial bound $h_{K} \leq|D| / 4$ which holds for $|D| \neq 3,4$. On the other hand, comparing the Euler factors the value $L\left(3, \chi_{D}\right)$ can be estimated below by a known value of the Riemann zeta function, namely $L\left(3, \chi_{D}\right)>1 / \sqrt{\zeta_{\mathbb{Q}}(2)}=\sqrt{6} / \pi$. More precisely, one shows that $\left(1-p^{-2}\right)\left(1-\chi_{D}(p) p^{-3}\right)^{2}<1$ for all primes, from which the lower bound follows. Noting additionally that always $\eta_{K} \leq 2$ and $\vartheta_{\mathfrak{p}} \geq 1$, the inequality (4.2) will follow from the inequality
$$|D|^{5 / 2}>\frac{16 \pi^{4}}{3 \sqrt{6}}(2+|D|)$$
This inequality holds for $|D|>35$.
For discriminants $D$ with $|D| \leq 35$ we have to check the inequality $c_{1}^{2}(\widetilde{Y(\mathfrak{p})})>9$ case by case. For this, one first uses the functional equation to reformulate the formula (4.1) as
$$c_{1}^{2}(\widetilde{Y(\mathfrak{p})})=\left[\Gamma_{K}: \Gamma_{K}(\mathfrak{a})\right]\left(\frac{3 \delta_{K}}{16} B_{3, \chi_{D}}-\frac{h_{K} \eta_{K}}{\vartheta_{\mathfrak{p}}^{2}}\right)$$
and than uses the exact values $B_{3, \chi_{D}}$ from the table in section 3.3. For instance, let us consider the case $D=-35$. With $h_{K}=2, \eta_{K}=1 / 2$ and $B_{3}, \chi_{-35}=108$ we have $c_{1}^{2}=\left[\Gamma_{K}: \Gamma_{K}(\mathfrak{p})\right](81 / 4-$ $\left.1 / \vartheta_{\mathfrak{p}}^{2}\right) \geq 81\left[\Gamma_{K}: \Gamma_{K}(\mathfrak{p})\right] / 4>9$. The other cases are treated in the same manner. The cases $|D|=-3,-4,-7,-8$ need to be considered more carefully, since in these situations $c_{1}^{2}$ can be negative.
$D=-8$. Let us shortly write $I_{\mathfrak{p}}$ instead of $\left[\Gamma_{K}: \Gamma_{K}(\mathfrak{p})\right]$. For the selfintersection we have: $c_{1}^{2}=I_{\mathfrak{p}}\left\{27 / 48-2 / \vartheta_{\mathfrak{p}}^{2}\right\}$. Now, it is easy to see that $c_{1}^{2}<0$ if and only if $\vartheta_{\mathfrak{p}}=1$ which is exactly the case when $p=\mathfrak{p} \cap \mathbb{Z}$ is ramified in $K=\mathbb{Q}(\sqrt{-2})$. From this it follows that $p=2$, and this case is excluded. Otherwise, $c_{1}^{2}>9$ if $I_{\mathfrak{p}}>144$. This is the case for $N(\mathfrak{p})>3$ and $p$ unramified, as the index formula shows.
$D=-7$. Here we have $c_{1}^{2}=I_{\mathfrak{p}}\left\{3 / 7-1 / 2 \vartheta_{\mathfrak{p}}^{2}\right\}$. This expression is negative if and only if $\vartheta_{\mathfrak{p}}=1$, which means that $p=\mathfrak{p} \cap \mathbb{Z}$ is ramified. This is the exeption we have to exclude. Indeed, for $\mathfrak{p}=(\sqrt{-7})$ we have $c_{2}=48$ and $c_{1}^{2}=-24$. In other cases $c_{1}^{2}>9$.
$D=-4$. Here we get a negative $c_{1}^{2}$ for $\vartheta_{\mathfrak{p}}=1$ or 2. But $\vartheta_{\mathfrak{p}}=1$ is only possible for $\mathfrak{p}=(1)$ and $\vartheta_{\mathfrak{p}}=2$ is only possible for those $\mathfrak{p}$ which contain the prime 2.
$D=-3$. In this case $c_{1}^{2}<0$ is only possible for a prime ideal $\mathfrak{p}$ such that $p$ is ramified in $K$. But then $N(\mathfrak{p})=3$, a case which is excluded. \(\square\)

The invariants of $\widetilde{Y(\mathfrak{a})}$ are in general very large due to the fact that the index, which grows very fast with the norm of the ideal, dominates the expressions. However, the surfaces $\widetilde{Y(\mathfrak{a})}$ are interesting from the point of view of surface geography, since the pairs $\left(c_{1}^{2}(\widetilde{Y(\mathfrak{a})}), c_{2}(\widetilde{Y(\mathfrak{a})})\right)$ are located in an interesting region of the $\left(c_{1}^{2}, c_{2}\right)$-plane, namely the ratio $c_{1}^{2} / c_{2}$ is close to 3 (see [Hol80], and first part of [Hun89] for a detailed discussion on surface geography). More precisely the ratio $c_{1}^{2}(\widetilde{Y(\mathfrak{a})}) / c_{2}(\widetilde{Y(\mathfrak{a})})$ tends to 3 when either the norm $N(\mathfrak{a})$ or the discriminant $|D|$ tends to infinity (see also [Hol80].)
This is easily seen, since
$$\frac{c_{1}^{2}(\widetilde{Y(\mathfrak{a})})}{c_{2}(\widetilde{Y(\mathfrak{a})})}=3-\frac{\frac{h_{K} \eta_{K}}{\vartheta_{a}^{2}}}{\frac{|D|^{5 / 2} \delta_{K}}{32 \pi^{3}} L\left(3, \chi_{D}\right)}$$

Now, as $\vartheta_{\mathfrak{a}}^{2} \longrightarrow \infty$ for $N(\mathfrak{a}) \rightarrow \infty$, we see that for a fixed $D$ the ratio tends to 3. Let us, on the other hand, fix $\mathfrak{a}$ but let $D$ vary. We first observe, as $L\left(3, \chi_{D}\right)$ is bounded by the value of the Riemann zeta function at $s=3$, namely $\zeta(3)^{-1}<L\left(3, \chi_{D}\right)<\zeta(3)$, that there are constants $C$ and $C^{\prime}$ not depending on $D$ such that
$$C^{\prime} \frac{h_{K}}{|D|^{5 / 2}} \geq \frac{\frac{h_{K} \eta_{K}}{\vartheta_{a}^{2}}}{\frac{|D|^{5 / 2} \delta_{K}}{32 \pi^{3}} L\left(3, \chi_{D}\right)} \geq C \frac{h_{K}}{|D|^{5 / 2}}$$
There are well known bounds for the class number of an imaginary quadratic field, namely for any $\epsilon>0$ there are constants $C_{1}=C_{1}(\epsilon)$ and $C_{2}=C_{2}(\epsilon)$ such that $C_{1}|D|^{1 / 2+\epsilon}>h_{K}>C_{2}|D|^{1 / 2-\epsilon}$. Bringing this into (4.5) we see that the expression $\frac{h_{K} \eta_{K}}{\vartheta_{\mathrm{a}}^{2}} / \frac{|D|^{5 / 2} \delta_{K}}{32 \pi^{3}} L\left(3, \chi_{D}\right)$ tends to zero as $|D| \rightarrow$ $\infty$. Hence
$$\lim _{|D| \rightarrow \infty} \frac{c_{1}^{2}(\widetilde{Y(\mathfrak{a})})}{c_{2}(\widetilde{Y(\mathfrak{a})})}=3$$
Already for small discriminants and norms, the Chern number ratio is very close to 3, see [Hol80], table 1.

\subsection*{4.2 Dimension formulas}

Another application of the above explicit formulas for the Chern numbers of Picard modular surfaces is an explicit formula for the dimensions of spaces of cusp forms relative to a Picard modular group $\Gamma$.
A holomorphic function $f$ on the ball is called a cusp form of weight $k$ with respect to $\Gamma$ if it satisfies the following conditions:
\begin{itemize}
\item[-] For all $\gamma \in \Gamma$ and all $z \in \mathbb{B} f(\gamma z)=j(\gamma, z)^{k} f(z)$, where $j(\gamma, z)$ denotes the determinant of the Jacobian matrix corresponding to the holomorphic map $\gamma: \mathbb{B} \longrightarrow \mathbb{B}$ at the point $z$.
\item[-] $f(z)$ vanishes at cusps of $\Gamma$, i. e. it vanishes on $\partial_{\Gamma} \mathbb{B}=\Gamma \backslash \partial_{\mathbb{Q}} \mathbb{B}$.
\end{itemize}
Let $\Gamma$ be a neat Picard modular group. In the following, $S_{k}(\Gamma)$ will denote the space of cusp forms of weight $k$ and with respect to $\Gamma$. By a result of Hemperley [Hem72], the cusp forms of weight $k$ can be interpreted as the sections of a certain line bundle $\mathbb{L}^{(k)}$ on the smooth compactification $\widetilde{Y(\Gamma)}$. Thus, $\operatorname{dim} S_{k}(\Gamma)=\operatorname{dim} H^{0}\left(\widetilde{Y(\Gamma)}, \mathbb{L}^{(k)}\right)$. As an application of the Riemann-Roch and the Kodaira vanishing theorem, one gets the following formula for $\operatorname{dim} S_{k}(\Gamma)$

Theorem 4.2 (see [Hol98a]). Let $\Gamma$ be a neat Picard modular group and $k \geq 2$.
$$\operatorname{dim} S_{k}(\Gamma)=\left[\Gamma_{K}: \Gamma\right]\left\{\frac{9 k(k-1)+2}{6} c_{2}(Y(\Gamma))+\frac{1}{12}\left(T_{\Gamma} \cdot T_{\Gamma}\right)\right\}$$

Now it is clear that we have an explicit formula for the dimensions of spaces of cusp forms of weight $k \geq 2$ which are automorphic with respect to a neat principal congruence subgroup $\Gamma_{K}(\mathfrak{a})$, namely
$$S_{k}\left(\Gamma_{K}(\mathfrak{a})\right)=\frac{\left[\Gamma_{K}: \Gamma_{K}(\mathfrak{a})\right]}{6}\left\{(9 k(k-1)+2) \frac{\delta_{K}\left|D^{5 / 2}\right|}{32 \pi^{3}} L\left(3, \chi_{D}\right)-\frac{h_{K} \eta_{K}}{2 \vartheta_{\mathfrak{a}}^{2}}\right\}$$

These dimensions are very large in general, even in the case of small discriminants and small norms.

\section*{References}
\begin{itemize}
\item[] [Bas64] H. Bass. K-theory and stable algebra. Inst. Hautes Études Sci. Publ. Math., (22):5-60, 1964.
\item[] [BHC62] Armand Borel and Harish-Chandra. Arithmetic subgroups of algebraic groups. Ann. of Math. (2), 75:485-535, 1962.
\item[] [Hem72] John C. Hemperly. The parabolic contribution to the number of linearly independent automorphic forms on a certain bounded domain. Amer. J. Math., 94:1078-1100, 1972.
\item[] [Hol80] Rolf-Peter Holzapfel. A class of minimal surfaces in the unknown region of surface geography. Math. Nachr., 98:211-232, 1980.
\item[] [Hol98a] R.-P. Holzapfel. Zeta dimension formula for Picard modular cusp forms of neat natural congruence subgroups. Abh. Math. Sem. Univ. Hamburg, 68:169-192, 1998.
\item[] [Hol98b] Rolf-Peter Holzapfel. Ball and surface arithmetics. Aspects of Mathematics, E29. Friedr. Vieweg \& Sohn, Braunschweig, 1998.
\item[] [Hun89] Bruce Hunt. Complex manifold geography in dimension 2 and 3. J. Differential Geom., 30(1):51-153, 1989.
\item[] [Lan70] Serge Lang. Algebraic number theory. Addison-Wesley Publishing Co., Inc., Reading, Mass.-London-Don Mills, Ont., 1970.
\item[] [PY07] Gopal Prasad and Sai-Kee Yeung. Fake projective planes. Invent. Math., 168(2):321-370, 2007.
\item[] [Was82] Lawrence C. Washington. Introduction to cyclotomic fields, volume 83 of Graduate Texts in Mathematics. Springer-Verlag, New York, 1982.
\end{itemize}
