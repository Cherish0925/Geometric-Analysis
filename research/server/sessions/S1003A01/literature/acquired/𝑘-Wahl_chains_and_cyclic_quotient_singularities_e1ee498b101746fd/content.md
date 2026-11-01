---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 2603_27126v1.pdf
converter: mathpix
format: mmd
---

\title{
$k$-Wahl chains and cyclic quotient singularities
}

\author{
Yusuke Sato
}

\begin{abstract}
We study two-dimensional cyclic quotient singularities defined by $k$-Wahl chains, a class of Hirzebruch-Jung continued fractions obtained inductively starting from $[k+2]$. This class includes the classical Wahl singularities in the case $k=2$ and also contains cyclic quotient singularities arising from $k$-generalized Markov triples. For singularities defined by $k$-Wahl chains, we prove that the combinatorics of the continued fraction is encoded in the special representations of the associated cyclic group. We also study zero continued fractions on the dual side and obtain consequences for the deformation theory of these singularities, including the existence of extremal P-resolutions in the case of 1-Wahl chains.
\end{abstract}

\section*{1 Introduction}

Two-dimensional cyclic quotient singularities form a fundamental class of surface singularities that can be described explicitly by Hirzebruch-Jung continued fractions. For a cyclic quotient singularity of type $\frac{1}{r}(1, a)$, where $r$ and $a$ are coprime, the continued fraction expansion
$$\frac{r}{a}=\left[b_{1}, \ldots, b_{\ell}\right]=b_{1}-\frac{1}{b_{2}-\frac{1}{\ddots-\frac{1}{b_{\ell}}}}, \quad b_{i} \in \mathbb{Z}_{\geq 2} .$$
gives the self-intersection numbers of the exceptional curves in the minimal resolution. Because of this, combinatorial properties of Hirzebruch-Jung continued fractions often reflect geometric properties of the corresponding singularities.

In this paper, we study a distinguished class of cyclic quotient singularities arising from what we call $k$-Wahl chains. A $k$-Wahl chain is defined by a Hirzebruch-Jung continued fraction obtained inductively from the initial chain $[k+2]$ by repeatedly attaching a 2 either to the left or to the right, while increasing the opposite end by one. When $k=2$, this recovers the classical Wahl chains, and the associated cyclic quotient singularities are the Wahl singularities, which form a distinguished subclass of $T$-singularities and appear naturally in the study of $\mathbb{Q}$-Gorenstein deformations [9, 14].

Another motivation comes from number theory. The notion of $k$-Wahl chains is closely related to the theory of a $k$-generalized Markov equation. The $k$-generalized Markov equation is introduced by Gyoda and Matsushita [4] as following:
$$x^{2}+y^{2}+z^{2}+k(x y+y z+x z)=(3+3 k) x y z .$$
Its positive integer solutions are called $k$-generalized Markov triples, and the integers appearing in such triples are called $k$-generalized Markov numbers. The $k$-generalized Markov
triple determines a Hirzebruch-Jung continued fraction, and this continued fraction is a $k$-Wahl chain [5]. Thus, $k$-Wahl chains provide a natural geometric framework containing cyclic quotient singularities arising from $k$-generalized Markov numbers.

Our first main result establishes a representation-theoretic property of cyclic quotient singularities defined by $k$-Wahl chains. For a cyclic group $G=\frac{1}{r}(1, a) \subset G L(2, \mathbb{C})$, the special McKay correspondence gives a bijection between the exceptional curves in the minimal resolution of $\mathbb{C}^{2} / G$ and the nontrivial special representations of $G$ [11, 15]. To a $k$-Wahl chain, we associate its length encoding, which records the pattern of successive attachments of 2's in the inductive construction. On the other hand, from the sequence of special representations of $G$, we define the length encoding of special representations (LESR) by taking the run-length encoding of the corresponding differences. Our first main theorem shows that these two encodings coincide.

Theorem 1.1. Let $G=\frac{1}{r}(1, a)$ be a cyclic quotient singularity with $\operatorname{gcd}(r, a)=1$, and suppose that the Hirzebruch-Jung continued fraction $\frac{r}{a}=\left[b_{1}, \ldots, b_{s}\right]$ is a $k$-Wahl chain. Then the length encoding of $\left[b_{1}, \ldots, b_{s}\right]$ coincides, up to reversal, with the length encoding of special representations of $G$.

This theorem shows that the inductive combinatorics of $k$-Wahl chains is reflected precisely in the arrangement of special representations of the corresponding cyclic group. The second theme of this paper is the connection between $k$-Wahl chains and deformation theory via zero continued fractions. A zero continued fraction is a negative continued fraction
$$\left[a_{1}, \ldots, a_{s}\right], \quad a_{i} \geq 1,$$
whose value is equal to zero. For a cyclic quotient singularity $X=\mathbb{C}^{2} / G$ with $G=\frac{1}{r}(1, a)$ and its Hirzebruch-Jung continued fraction $\frac{r}{a}=\left[b_{1}, \ldots, b_{s}\right]$, we set a dual Hirzebruch-Jung continued fraction
$$\frac{r}{r-a}=\left[e_{1}, \ldots, e_{\ell}\right] .$$
A fundamental result of Christophersen [3], revisited from the toric viewpoint by Altmann [1], states that the P-resolutions of $X$ are in one-to-one correspondence with the admissible zero continued fractions on the dual side. Thus, the existence of a P-resolution can be read combinatorially from the existence of a zero continued fraction supported by the dual Hirzebruch-Jung continued fraction. Since P-resolutions are in bijection with the irreducible components of the versal deformation space, zero continued fractions provide concrete information on the deformation theory of cyclic quotient singularities [1, 3, 9].

In this direction, we study the minimal weight of zero continued fractions for dual 0-and 1-Wahl chains.

Theorem 1.2. Let $\left[b_{1}, \ldots, b_{s}\right]$ be a Hirzebruch-Jung continued fraction with $s \geq 2$. Then the following hold:
\begin{itemize}
\item[(i)] If it is a dual 1-Wahl chain, then $\alpha\left(\left[b_{1}, \ldots, b_{s}\right]\right)=1$.
\item[(ii)] If it is a dual 0 -Wahl chain, then $\alpha\left(\left[b_{1}, \ldots, b_{s}\right]\right)=2$,
\end{itemize}
where $\alpha\left(\left[b_{1}, \ldots, b_{s}\right]\right)$ denotes the minimal weight of an admissible zero continued fraction.
In particular, dual 1-Wahl chains give rise to extremal P-resolutions for cyclic quotient singularities corresponding to 1-Wahl chains. In this way, cyclic quotient singularities associated with $k$-Wahl chains may be viewed as lying at the intersection of number theory, representation theory, and deformation theory.

The organization of this paper is as follows. In Section 2, we review the definition of $k$-Wahl chains and their duals. In Section 3, we introduce the length encoding of $k$-Wahl chains and compare it with the special representations of the corresponding cyclic group, proving the representation-theoretic characterization above. In Section 4, we study zero continued fractions and their weights, and we investigate how dual $k$-Wahl chains give rise to $P$-resolutions. This provides a deformation-theoretic interpretation of the class of cyclic quotient singularities defined by $k$-Wahl chains.

\section*{$2 k$-Wahl chains and cyclic quotient singularities}

In this section, we explain cyclic quotient singularities associated with $k$-Wahl chains. Let $a, b, r$ be positive integers and let $\varepsilon$ be a primitive $r$-th root of unity. Let $G$ be the cyclic group generated by the diagonal matrix $\left(\begin{array}{cc}\varepsilon^{a} & 0 \\ 0 & \varepsilon^{b}\end{array}\right)$. We denote this generator (and also the group) by $\frac{1}{r}(a, b)$. Then $G$ acts on $\mathbb{C}^{2}$ by $(x, y) \mapsto\left(\varepsilon^{a} x, \varepsilon^{b} y\right)$, and the quotient $\mathbb{C}^{2} / G$ is called a cyclic quotient singularity of type $\frac{1}{r}(a, b)$.

Before stating properties of $k$-Wahl chains, we recall the relation between two-dimensional cyclic quotients and continued fractions. Let $G_{r, a}=\frac{1}{r}(1, a)$ with $\operatorname{gcd}(r, a)=1$. The Hirzebruch-Jung continued fraction is
$$\frac{r}{a}=\left[b_{1}, \ldots, b_{\ell}\right]=b_{1}-\frac{1}{b_{2}-\frac{1}{\ddots-\frac{1}{b_{\ell}}}}, \quad b_{i} \in \mathbb{Z}_{\geq 2}$$
Then $-b_{1}, \ldots,-b_{\ell}$ are the self-intersection numbers of the exceptional curves $E_{1}, \ldots, E_{\ell}$ in the minimal resolution of $\mathbb{C}^{2} / G_{r, a}$.

Motivated by this, we introduce the following special class of Hirzebruch-Jung fractions.
Definition 2.1. Let $k$ be a non-negative integer. A $k$-Wahl chain is defined inductively by:
\begin{itemize}
\item[1.] $[k+2]$ is a $k$-Wahl chain.
\item[2.] If $\left[b_{1}, \ldots, b_{\ell}\right]$ is a $k$-Wahl chain, then so are
$$\left[b_{1}+1, b_{2}, \ldots, b_{\ell}, 2\right] \quad \text { and } \quad\left[2, b_{1}, \ldots, b_{\ell-1}, b_{\ell}+1\right] .$$
\end{itemize}

Example 2.2. When $k=0$, the fractions [2], [3, 2], [4, 2, 2], and [2, 3, 3] are 0-Wahl chains. Moreover, if $\left[b_{1}, \ldots, b_{\ell}\right]$ is a $k$-Wahl chain, then $\left[b_{\ell}, \ldots, b_{1}\right]$ is also a $k$-Wahl chain.

Remark 2.3. The notion of $k$-Wahl chains originally appeared (for $k=2$ ) in the work of Wahl [14], Kollár, and Shepherd-Barron [9]. In particular, the cyclic quotient singularities determined by 2-Wahl chains are Wahl singularities, which belong to the class of $T$-singularities. A two-dimensional quotient singularity is called a $T$-singularity if it admits a $\mathbb{Q}$-Gorenstein smoothing. Moreover, if a quotient singularity is a $T$-singularity, then it is either a rational double point or a cyclic quotient singularity of type $\frac{1}{d m^{2}}(1, a d m-1)$ with $\operatorname{gcd}(a, m)=1$ and $m>1$. The case $d=1$ (and not a rational double point) is called a Wahl singularity.

Theorem 2.4 ([5]). Let $t \in(0,1)$ be a reduced fraction, and let $m_{k, t}$ be the associated $k$-GM number. Let $u_{k, t}^{+}$be the corresponding characteristic number. Then the Hirzebruch-Jung continued fraction $\frac{m_{k, t}}{u_{k, t}^{+}}$is a $k$-Wahl chain.

The relationship between Wahl singularities and the Markov equation, namely the 0-GM equation, has been studied by Hacking and Prokhorov [6], Perling [10], and Urzúa and Zúñiga [13]. These previous works consider the weighted projective surface $\mathbb{P}\left(a^{2}, b^{2}, c^{2}\right)$ associated with an ordinary Markov triple, that is, a 0-GM triple $(a, b, c)$, and it is known that this weighted projective surface has only Wahl singularities. On the other hand, Theorems 2.4 and 2.5 show that the cyclic quotient singularities associated with the squares of 0-GM triples are Wahl singularities.

Theorem 2.5 ([4]). If $(a, b, c)$ is a 0-GM triple, then $\left(a^{2}, b^{2}, c^{2}\right)$ is a 2-GM triple. Conversely, if $(A, B, C)$ is a 2-GM triple, then $(\sqrt{A}, \sqrt{B}, \sqrt{C})$ is a 0-GM triple.

Remark 2.6. The converse of Theorem 2.4 does not hold in general: for example, $\frac{10}{3}=$ [4, 2, 2] is a 0-Wahl chain, but 10 is not a 0-GM number.

Proposition 2.7. Let $\frac{r}{a}=\left[b_{1}, \ldots, b_{s}\right]$ be a $k$-Wahl chain for some non-negative integer $k$. Then we have
$$\frac{r}{r-a-k}=\left[b_{s}, \ldots, b_{1}\right] .$$
In particular, it follows that $a(r-a-k) \equiv 1(\bmod r)$.

Proof. We argue by induction on the length of the Hirzebruch-Jung continued fraction. First, note that $\frac{k+2}{1}=[k+2]$ satisfies the claim, since $k+2-1-k=1$.

Now suppose that $\frac{r}{a}=\left[b_{1}, \ldots, b_{s}\right]$ is a $k$-Wahl chain and that the statement holds for this continued fraction. We consider the extension $\left[b_{1}+1, b_{2}, \ldots, b_{s}, 2\right]$. By the induction hypothesis we have
$$\left[2, b_{s}, \ldots, b_{1}\right]=2-\frac{r-a-k}{r}=\frac{r+a+k}{r} .$$

From this, we deduce
$$\left[b_{1}, \ldots, b_{s}, 2\right]=\frac{r+a+k}{r^{\prime}},$$
where $r^{\prime}$ denotes the integer such that $r^{\prime} \cdot r \equiv 1(\bmod r+a+k)$. It leads to
$$\left[b_{1}+1, b_{2}, \ldots, b_{s}, 2\right]=1+\left[b_{1}, \ldots, b_{s}, 2\right]=\frac{r^{\prime}+r+a+k}{r^{\prime}} .$$

On the other hand, since
$$\left[1+b_{1}, b_{2}, \ldots, b_{s}\right]=1+\frac{r}{a}=\frac{r+a}{a},$$
we have
$$\left[2, b_{s}, \ldots, b_{2}, b_{1}+1\right]=2-\frac{a^{\prime}}{r+a}=\frac{2 r+2 a-a^{\prime}}{r+a},$$
where $a^{\prime}$ denotes the integer satisfying $a^{\prime} \cdot a \equiv 1(\bmod r+a)$. By the basic property of Hirzebruch-Jung continued fractions, we have $2 r+2 a-a^{\prime}=r^{\prime}+r+a+k$. Hence
$$\left[2, b_{s}, \ldots, b_{2}, b_{1}+1\right]=\frac{r^{\prime}+r+a+k}{r+a} .$$
It remains to check that the denominator is
$$\left(r^{\prime}+r+a+k\right)-r^{\prime}-k=r+a,$$
which is immediate. Therefore the claim follows.
A similar argument applies to $\left[2, b_{1}, \ldots, b_{s-1}, b_{s}+1\right]$. This completes the induction and proves the proposition. \(\square\)

Definition 2.8. Let $k$ be a non-negative integer. We define a dual $k$-Wahl chain as follows.
\begin{itemize}
\item[(i)] The Hirzebruch-Jung continued fraction with $k+1$ consecutive 2s [2, . . . , 2] is a dual $k$-Wahl chain.
\item[(ii)] If $\left[b_{1}, \ldots, b_{l}\right]$ is a dual $k$-Wahl chain, then $\left[b_{1}+1, b_{2}, \ldots, b_{\ell}, 2\right]$ and $\left[2, b_{1}, \ldots, b_{\ell-1}, b_{\ell}+1\right]$ are also dual $k$-Wahl chains.
\end{itemize}

Remark 2.9. Any dual $k$-Wahl chain arises as the Hirzebruch-Jung dual of some $k$-Wahl chain. In other words, if $\left[b_{1}, \ldots, b_{\ell}\right]=\frac{r}{a}$ is a $k$-Wahl chain, then $\frac{r}{r-a}=\left[a_{1}, \ldots, a_{s}\right]$ is a dual $k$-Wahl chain.

In general, the Hirzebruch-Jung dual of a continued fraction does not coincide with its reversal. However, for a 0-Wahl chain, they do coincide by Proposition 2.7: namely, $\frac{r}{r-a}=\left[b_{\ell}, \ldots, b_{1}\right]$.

\section*{3 Length encoding}

In this section, we study the special representations associated with the cyclic groups determined by $k$-Wahl chains. By the special McKay correspondence, these special representations are in one-to-one correspondence with the exceptional curves appearing in the minimal resolution of the corresponding cyclic quotient singularities. Using this geometric correspondence, we introduce the relationship between the length encoding of a $k$-Wahl chain and that of the special representations.

\subsection*{3.1 Special representations}

Let $G_{r, a}=\frac{1}{r}(1, a)$ be a finite cyclic group, and let $g=\frac{1}{r}(1, a)$ denote its generator. For each integer $i$, we define the character $\chi_{i}: g \mapsto \varepsilon^{i}$, where $\varepsilon$ is a primitive $r$-th root of unity, and let $\rho_{i}$ be the one-dimensional representation associated to $\chi_{i}$. Since $G_{r, a}$ is abelian, all its irreducible representations are one-dimensional. Among these irreducible representations, we now introduce the notion of special representations. Originally, special representations were defined for small finite subgroups of $\mathrm{GL}(2, \mathbb{C})$ (see [11], [15]). For the purposes of this work, we shall restrict the definition to finite cyclic groups.

Definition 3.1. Let $G$ be a finite cyclic group and $\rho$ a one-dimensional representation of $G$ with representation space $V_{\rho}$. We say that $\rho$ is a nontrivial special representation of $G$ if $\left(\mathbb{C}[x, y] \otimes V_{\rho}\right)^{G}$ is generated by two elements as a module over $\mathbb{C}[x, y]^{G}$.

There is a one-to-one correspondence between nontrivial special representations and the exceptional curves appearing in the minimal resolution of the cyclic quotient singularity $\mathbb{C}^{2} / G$. This correspondence is known as the special McKay correspondence ([16]).

A monomial $x^{m} y^{n}$ in $\mathbb{C}[x, y]$ transforms by the character $\chi_{m+a n}$. Equivalently, the weight of $x^{m} y^{n}$ is
$$\operatorname{wt}\left(x^{m} y^{n}\right) \equiv m+a n \quad(\bmod r) .$$
In particular, the monomials $x^{i}$ and $y^{j}$ define the same character if and only if $i \equiv a j$ $(\bmod r)$. Therefore, if an exceptional curve is described by a monomial ratio $x^{i}: y^{j}$, then the corresponding special representation is $\rho_{i}$.

From the toric point of view, the cyclic quotient singularity $\mathbb{C}^{2} / G_{r, a}$ is the affine toric surface associated with the cone $\sigma \subset N_{\mathbb{R}}$, where
$$N=\mathbb{Z}^{2}+\frac{1}{r}(1, a) \mathbb{Z}, \text { and } \sigma=\mathbb{R}_{\geq 0}(1,0)+\mathbb{R}_{\geq 0}(0,1) .$$
The minimal resolution of $\mathbb{C}^{2} / G_{r, a}$ is obtained by a simplicial subdivision whose rays pass through the lattice points on the Newton boundary, and each lattice point on the Newton boundary corresponds to an exceptional divisor. If $i \equiv a j(\bmod r)$, then we have $\frac{1}{r}(j, i) \in$ $N$. Moreover, this lattice point is precisely the toric point corresponding to the exceptional divisor associated with the special representation $\rho_{i}$.

Remark 3.2. Let $\frac{r}{a}=\left[b_{1}, \ldots, b_{s}\right]$ be the Hirzebruch-Jung continued fraction of the cyclic quotient singularity of type $\frac{1}{r}(1, a)$. The integers $a_{0}, \ldots, a_{s+1}$ are defined by
$$a_{0}:=r, \quad a_{1}:=a, \quad a_{i+1}:=b_{i} a_{i}-a_{i-1} \quad(i=1, \ldots, s) .$$
Then
$$r=a_{0}>a_{1}>\cdots>a_{s}=1>a_{s+1}=0,$$
and the indices of the special representations are precisely these intermediate remainders:
$$\rho_{a_{1}}, \rho_{a_{2}}, \ldots, \rho_{a_{s}} .$$
In particular, the subscripts of the special representations are not the coefficients $b_{i}$ of the Hirzebruch-Jung continued fraction, but the remainder sequence associated with it.

Definition 3.3. Let $G_{r, a}=\frac{1}{r}(1, a)$ be a cyclic group. Denote by $\rho_{a_{1}}, \ldots, \rho_{a_{s}}$ the special representations of $G_{r, a}$, where $r>a_{1}>a_{2}>\cdots>a_{s}>0$. For each $i=1, \ldots, s-1$, set $d_{i}:=a_{i}-a_{i+1}$.

The special representation length encoding (LESR) of $G_{r, a}$ is defined as the sequence obtained from $\left(d_{1}, \ldots, d_{s-1}\right)$ by replacing each maximal block of consecutive equal integers with its length. In particular, when $G_{r, a}$ admits only one special representation, that is $G_{r, 1}$, we set $\operatorname{LESR}\left(G_{r, a}\right)=\varnothing$.

Example 3.4. Let $G=G_{29,12}$. Then the special representations of $G_{29,12}$ are $\rho_{12}, \rho_{7}, \rho_{2}, \rho_{1}$, corresponding to the monomial ratios $x^{12}: y, x^{7}: y^{3}, x^{2}: y^{5}$, and $x: y^{17}$, respectively. These special representations correspond bijectively to the exceptional curves $\mathbb{P}^{1}$ in the minimal resolution of $\mathbb{C}^{2} / G_{29,12}$.

From this we obtain the sequence
$$d_{1}=12-7=5, \quad d_{2}=7-2=5, \quad d_{3}=2-1=1 .$$
Hence the sequence $\left(d_{1}, d_{2}, d_{3}\right)=(5,5,1)$. Applying length encoding, we compress this into
$$\operatorname{LESR}\left(G_{29,12}\right)=(2,1) .$$

Note that, by definition of LESR, reversing the order of the continued fraction also reverses its length encoding. Namely, if the LESR of $\left[b_{1}, \ldots, b_{s}\right]$ is $\left(c_{1}, \ldots, c_{m}\right)$, then the LESR of $\left[b_{s}, \ldots, b_{1}\right]$ is $\left(c_{m}, \ldots, c_{1}\right)$.

Lemma 3.5. Let $\frac{r}{a}=\left[b_{1}, \ldots, b_{s}\right]$, and write the special representations of $G_{r, a}$ as $\rho_{a_{1}}, \ldots, \rho_{a_{s}}$, where $a_{1}=a$ and $a_{s}=1$. For each $i=0, \ldots, s$, set $d_{i}=a_{i}-a_{i+1}$, where $a_{0}=r, a_{s+1}=0$. Then $b_{i}=2$ if and only if $d_{i}-d_{i-1}=0$ for $i=1, \ldots, s$.

Proof.By Remark 3.2, we have $b_{i} \cdot a_{i}=a_{i+1}+a_{i-1}$ for $i=1, \ldots, s$. Hence
$$d_{i}-d_{i-1}=\left(a_{i}-a_{i+1}\right)-\left(a_{i-1}-a_{i}\right)=2 a_{i}-a_{i+1}-a_{i-1}=\left(2-b_{i}\right) a_{i} .$$
Since $a_{i}>0$, the claim holds. \(\square\)

As a consequence of this lemma, we obtain the following.

Corollary 3.6. Assume that the LESR of $\left[b_{1}, \ldots, b_{s}\right]$ is $\left(c_{1}, \ldots, c_{m}\right)$. Then the LESR of $\left[b_{1}, \ldots, b_{s}, 2\right]$ is as follows:
\begin{itemize}
\item[-] If $b_{s}=2$, then $\left(c_{1}, \ldots, c_{m-1}, c_{m}+1\right)$,
\item[-] if $b_{s} \geq 3$, then $\left(c_{1}, \ldots, c_{m-1}, c_{m}, 1\right)$.
\end{itemize}
Proof.If $b_{s}=2$, then the last difference satisfies $d_{s}-d_{s-1}=0$ by Lemma 3.5. Hence the final block in the length encoding is extended, giving $\left(c_{1}, \ldots, c_{m-1}, c_{m}+1\right)$. If instead $b_{s} \geq 3$, then $d_{s}-d_{s-1} \neq 0$, so a new block of length one appears at the end of the encoding $\left(c_{1}, \ldots, c_{m-1}, c_{m}, 1\right)$. \(\square\)

Lemma 3.7. If the LESR of $\left[b_{1}, b_{2}, \ldots, b_{s}\right]$ is $\left(c_{1}, \ldots, c_{m}\right)$, then the LESR of $\left[b_{1}^{\prime}, b_{2}, \ldots, b_{s}\right]$ is also $\left(c_{1}, \ldots, c_{m}\right)$.

Proof.
Let $\left[b_{2}, \ldots, b_{s}\right]=\frac{p}{q}$. Then we have
$$\left[b_{1}, \ldots, b_{s}\right]=b_{1}-\frac{q}{p}=\frac{p \cdot b_{1}-q}{p} .$$
Similarly, we have $\left[b_{1}^{\prime}, b_{2}, \ldots, b_{s}\right]=\frac{p \cdot b_{1}^{\prime}-q}{p}$. By Remark 3.2, the remainder sequences of these two continued fractions are
$$b_{1} p-q, p, q, \ldots, 1,0 \quad \text { and } \quad b_{1}^{\prime} p-q, p, q, \ldots, 1,0 \text {, }$$
respectively. Hence the indices of the special representations are $a_{1}=q, \ldots, a_{s}=1$ in both cases. Therefore the corresponding difference sequences are identical, so the LESR are equal. \(\square\)

\subsection*{3.2 Length encoding of $k$-Wahl chain}

Definition 3.8. The length encoding of a $k$-Wahl chain is defined as follows:
\begin{itemize}
\item[(i)] The empty sequence $\emptyset$ for $[k+2]$.
\item[(ii)] Suppose that the sequence $\left(c_{1}, \ldots, c_{m}\right)$ encodes a $k$-Wahl chain $\left[a_{1}, \ldots, a_{s}\right]$ with $a_{1} \neq$ 2, then for any $c_{m+1}>0,\left(c_{1}, \ldots, c_{m+1}\right)$ encodes the $k$-Wahl chain corresponding to
$$\left[(2)^{c_{m+1}}, a_{1}, \ldots, a_{s-1}, a_{s}+c_{m+1}\right],$$
where (2) ${ }^{\ell}$ denotes a string of $\ell$ consecutive 2's.
\end{itemize}
\begin{itemize}
\item[(iii)] Suppose that the sequence $\left(c_{1}, \ldots, c_{m}\right)$ encodes a $k$-Wahl chain $\left[a_{1}, \ldots, a_{s}\right]$ with $a_{s} \neq$ 2, then for any $c_{m+1}>0,\left(c_{1}, \ldots, c_{m+1}\right)$ encodes the $k$-Wahl chain corresponding to $\left[a_{1}+c_{m+1}, a_{2}, \ldots, a_{s},(2)^{c_{m+1}}\right]$.
\end{itemize}

In other words, the length encoding of a $k$-Wahl chain records on which side successive 2's are attached, starting from $[k+2]$. Moreover, the length encodings of $\left[b_{1}, \ldots, b_{s}\right]$ and $\left[b_{s}, \ldots, b_{1}\right]$ coincide, which does not affect the correspondence, since both represent the isomorphic cyclic quotient singularity.

Example 3.9. The length encoding of the 0-Wahl chain [4, 2, 2] is given by (2). The length encoding of [2, 4, 2, 3] is given by (2, 1), and that of [3, 2, 4, 2, 4, 2] is (2, 2, 1).

Theorem 3.10. Let $G=\frac{1}{r}(1, a)$ be a cyclic quotient singularity, where $r$ and a are coprime. Suppose that the Hirzebruch-Jung continued fraction $r / a=\left[b_{1}, \ldots, b_{s}\right]$ is a $k$-Wahl chain. Then the length encoding of $\left[b_{1}, \ldots, b_{s}\right]$ agrees, up to reversal, with the length encoding of special representations (LESR) of $G$.

Proof.
We proceed by induction on the number of steps in the inductive construction of a $k$-Wahl chain. Equivalently, we start from $[k+2]$ and at each step attach a 2 either to the left or to the right. For the initial chain $[k+2]$, both the length encoding and the LESR are empty. At the first step, the chains $[k+3,2]$ and $[2, k+3]$ both have length encoding (1), and a direct computation shows that their LESR is also (1).

Assume that the claim holds for a $k$-Wahl chain $\left[b_{1}, \ldots, b_{s}\right]$ whose length encoding and LESR are both $\left(c_{1}, \ldots, c_{m}\right)$. By definition of a $k$-Wahl chain, one of $b_{1}$ and $b_{s}$ is equal to 2. By Definition 3.8, the length encoding is unchanged under reversal, and the same is true for the LESR. Therefore, without loss of generality, we may assume that $b_{s}=2$. Then we have $b_{1} \geq 3$.

Case 1: We consider $\left[b_{1}+1, b_{2}, \ldots, b_{s}, 2\right]$. By Definition 3.8, its length encoding is $\left(c_{1}, \ldots, c_{m-1}, c_{m}+1\right)$. On the other hand, by Corollary 3.6 and Lemma 3.7, its LESR is also $\left(c_{1}, \ldots, c_{m-1}, c_{m}+1\right)$.
Case 2: We consider $\left[2, b_{1}, b_{2}, \ldots, b_{s}+1\right]$. By Definition 3.8, its length encoding is $\left(c_{1}, \ldots, c_{m}, 1\right)$. Considering instead the reversed chain $\left[b_{s}+1, b_{s-1}, \ldots, b_{1}, 2\right]$, and applying Corollary 3.6 with $b_{1} \geq 3$, we obtain that the LESR is also $\left(c_{1}, \ldots, c_{m}, 1\right)$.

Thus in both cases the length encoding and the LESR coincide. This completes the induction step and proves the theorem. \(\square\)

Since the length encoding of a $k$-Wahl chain is invariant under reversal of the continued fraction, the two encodings in fact coincide.

Example 3.11. Let $G=\frac{1}{29}(1,12)$ be the cyclic group generated by $\frac{1}{29}(1,12)$. Since $\frac{29}{12}=[3,2,4,2]$, this is a 0-Wahl chain, and its length encoding is (2, 1). On the other hand, by Example 3.4 the LESR of $G$ is also (2, 1). Thus they coincide.

\section*{4 Zero continued fractions and P-resolutions}

A P-resolution of a cyclic quotient singularity $W=\mathbb{C}^{2} / G_{r, a}$ is a partial resolution $f$ : $W^{\prime} \rightarrow W$ such that $W^{\prime}$ has only $T$-singularities and the canonical divisor $K_{W^{\prime}}$ is $f$-ample. From the point of view of deformation theory, this is essential: by the theorem of Kollár and Shepherd-Barron [9], there is a bijection between the set of P-resolutions of $W$ and the irreducible components of the versal deformation space $\operatorname{Def}(W)$. Moreover, each component is dominated by the $\mathbb{Q}$-Gorenstein deformations of the corresponding P-resolution. Thus the existence of a P-resolution ensures the presence of a distinguished component of $\operatorname{Def}(W)$, and the combinatorics of zero continued fractions provides an explicit description of all such P-resolutions.

In this section, we study zero continued fractions for dual $k$-Wahl chains and relate them to P-resolutions of cyclic quotient singularities. By Theorem 4.8, admissible zero continued fractions of the dual Hirzebruch-Jung continued fraction are in one-to-one correspondence with P-resolutions. We then determine the minimal weight $\alpha\left(\left[b_{1}, \ldots, b_{s}\right]\right)$ for dual 2-, 1-, and 0-Wahl chains, obtaining the values 0, 1, and 2, respectively. In particular, the case of dual 1-Wahl chains leads to extremal P-resolutions.

Definition 4.1. A zero continued fraction is a negative continued fraction $\left[a_{1}, \ldots, a_{s}\right]$, with integers $a_{i} \geq 1$, such that its value is equal to 0.

Every zero continued fraction can be obtained from the basic case [1,1] by successive blow-ups. The blow-up operation is defined as follows.

For any consecutive pair $(u, v)$ in a continued fraction, replace it by
$$[\ldots, u, v, \ldots] \longmapsto[\ldots, u+1,1, v+1, \ldots] .$$

If the chosen pair lies at the boundary, the same rule applies with the convention that only the existing neighbor is increased. Thus
$$[u, \ldots] \longmapsto[1, u+1, \ldots], \quad[\ldots, v] \longmapsto[\ldots, v+1,1] .$$

Starting from [1, 1] and iterating these blow-ups generates all zero continued fractions.
Example 4.2. The following continued fractions are zero continued fractions:
$$[1,1] \mapsto[1,2,1], \quad[1,2,1] \mapsto[1,3,1,2], \quad[1,2,1] \mapsto[1,2,2,1] .$$

It is a classical observation that zero continued fractions can be naturally interpreted in terms of triangulations of convex polygons. More precisely, consider a convex polygon with vertices $P_{0}, \ldots, P_{r}$. By choosing a triangulation, each vertex $P_{i}$ is contained in a certain number $v_{i}$ of triangles. Then the sequence $\left[v_{1}, \ldots, v_{r}\right]$ is a zero continued fraction, and, conversely, every zero continued fraction can be realized from some triangulation in this way. In Figure 1, we have $v_{0}=3, v_{1}=1, v_{2}=2, v_{3}=2, v_{4}=1$. Therefore, [1, 2, 2, 1], [2, 2, 1, 3], [2, 1, 3, 1], [1, 3, 1, 2], [3, 1, 2, 2] are zero continued fractions.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/2dae99b7-7727-4d39-986f-6b5c5a7baa79-11.jpg?height=490&width=480&top_left_y=409&top_left_x=845}
\captionsetup{labelformat=empty}
\caption{Figure 1: Zero continued fractions and polygon triangulations}
\end{figure}

Definition 4.3. Let $\frac{r}{a}=\left[b_{1}, \ldots, b_{s}\right]$ be the Hirzebruch-Jung continued fraction, where $b_{i} \geq 2$ for all $i$. We say that $\left[b_{1}, \ldots, b_{s}\right]$ admits a zero continued fraction of weight $\lambda$ if there are indices $i_{1}<i_{2}<\cdots<i_{u}$ for some $u \geq 1$ and integers $d_{i_{j}} \geq 1$ such that
$$\left[\ldots, b_{i_{1}}-d_{i_{1}}, \ldots, b_{i_{2}}-d_{i_{2}}, \ldots, b_{i_{u}}-d_{i_{u}}, \ldots\right]=0,$$
and $\lambda+1=\sum_{j=1}^{u} d_{i_{j}}$.
Definition 4.4. Among all admissible zero continued fractions $\left[e_{1}, \ldots, e_{s}\right]$ for $\left[b_{1}, \ldots, b_{s}\right]$ and all possible choices of $\left(i_{j}, d_{i_{j}}\right)$ as above, let
$$\alpha\left(\left[b_{1}, \ldots, b_{s}\right]\right)$$
denote the minimum of the resulting weights $\lambda$. We call $\alpha\left(\left[b_{1}, \ldots, b_{s}\right]\right)$ the minimal weight of zero $C F$ of $\left[b_{1}, \ldots, b_{s}\right]$. When convenient, we also write $\alpha(r / a)$ for $\left[b_{1}, \ldots, b_{s}\right]=r / a$.

Remark 4.5. Every Hirzebruch-Jung continued fraction $\left[b_{1}, \ldots, b_{s}\right]$ with $s \geq 2$ has at least one zero continued fraction $[1,2, \ldots, 2,1]$. In particular, for an $A_{n}$ singularity, the admissible zero continued fraction is unique except when $n=3$. More precisely, if $n=3$, then there are exactly two such zero continued fractions, namely [1, 2, 1] and [2, 1, 2].

Proposition 4.6. [12, Proposition 1.18] The Hirzebruch-Jung continued fraction $\left[b_{1}, \ldots, b_{s}\right]$ has a zero continued fraction of weight 0 if and only if its dual is a $T$-chain, i.e. the Hirzebruch-Jung continued fraction of $\frac{d m^{2}}{a d m-1}$. In particular, a dual 2-Wahl chain has a zero continued fraction of weight 0.

Proposition 4.7. [12, Proposition 1.19] Let $0<q<m$ be coprime integers. If $\frac{m}{m-q}=$ $\left[b_{1}, \ldots, b_{s}\right]$ admits a zero continued fraction of weight 1 , then the HJ continued fraction of $\frac{m}{q}$ is a $T$-chain with $d=2$ and $n>1$, or
$$\frac{m}{q}=\left[W_{0}, c, W_{1}\right],$$
where $c \geq 1$ and $W_{i}$ are 2-Wahl chains (including one or both empty).

Theorem 4.8. [1, 3] Let $W=\mathbb{C}^{2} / G_{r, a}$ be a cyclic quotient singularity, and let $\frac{r}{r-a}=$ $\left[b_{1}, \ldots, b_{s}\right]$ be the dual Hirzebruch-Jung continued fraction.

Define
$$K(W):=\left\{\left[k_{1}, \ldots, k_{s}\right]=0 \mid 1 \leq k_{i} \leq b_{i} \text { for all } i\right\} .$$
Then there is a one-to-one correspondence between the set $K(W)$ and the set of $P$-resolutions of $W$. Equivalently, in the notation of Definition 4.3, the admissible zero continued fractions supported on $\left[b_{1}, \ldots, b_{s}\right]$ are in one-to-one correspondence with the $P$-resolutions of $W$.

Theorem 4.9. Let $\left[b_{1}, \ldots, b_{s}\right]$ be a Hirzebruch-Jung continued fraction with $s \geq 2$. Then the following hold:
\begin{itemize}
\item[(i)] If it is a dual 1-Wahl chain, then $\alpha\left(\left[b_{1}, \ldots, b_{s}\right]\right)=1$.
\item[(ii)] If it is a dual 0 -Wahl chain, then $\alpha\left(\left[b_{1}, \ldots, b_{s}\right]\right)=2$.
\end{itemize}

Proof.
First, we prove (i). The dual 1-Wahl chain [2, 2] admits a zero continued fraction [1, 1], whose weight is 1.
We claim that if $\left[b_{1}, \ldots, b_{s}\right]$ has a zero continued fraction $\left[v_{1}, \ldots, v_{s}\right]$ which is induced by a triangulation of the convex polygon $P_{0} P_{1} \ldots P_{s}$ with $v_{0}=1$, then $\left[2, b_{1}, \ldots, b_{s-1}, b_{s}+1\right]$ and $\left[b_{1}+1, b_{2}, \ldots, b_{s}, 2\right]$ have zero continued fractions $\left[2, v_{1}, \ldots, v_{s-1}, v_{s}+1\right]$ and $\left[v_{1}+\right.$ $\left.1, v_{2}, \ldots, v_{s}, 2\right]$, respectively. Indeed, consider the polygon $P_{0} P_{1} \ldots P_{s}$ with triangulation given by $\left(v_{0}, \ldots, v_{s}\right)$. Adding a new vertex $P_{s+1}$ so that $P_{0} P_{1} \ldots P_{s} P_{s+1}$ is convex, we obtain $v_{s+1}=1$, and both $v_{0}$ and $v_{s}$ increase by one compared to the original triangulation (see Figure 2). Hence the sequence $\left[v_{0}, v_{1}, \ldots, v_{s-1}, v_{s}+1\right]$, which equals $\left[2, v_{1}, \ldots, v_{s-1}, v_{s}+1\right]$, is a zero continued fraction. Thus $\left[2, b_{1}, \ldots, b_{s-1}, b_{s}+1\right]$ admits a zero continued fraction of weight 1 . Similarly, if we add the new vertex $P_{s+1}$ so that $P_{0} P_{s+1} P_{1} \ldots P_{s}$ becomes convex, then $v_{0}$ and $v_{1}$ both increase by one, and we obtain $\left[v_{1}+1, v_{2}, \ldots, v_{s}, v_{0}\right]$, that is $\left[v_{1}+1, v_{2}, \ldots, v_{s}, 2\right]$, as a zero continued fraction. By Proposition 4.6, weight 0 is impossible for a dual 1-Wahl chain. Hence $\alpha=1$ for all dual 1-Wahl chains.
Next we prove (ii). The dual 0-Wahl chain [3, 2] admits a zero continued fraction [1, 1], and its weight is 2 . Moreover, this zero continued fraction corresponds to a triangulation with $v_{0}=1$. By the same inductive argument as above, every dual 0 -Wahl chain admits a zero continued fraction of weight 2 arising from a triangulation with $v_{0}=1$.

It remains to show that this weight is minimal. Let $\left[v_{1}, \ldots, v_{s}\right]$ be any admissible zero continued fraction of $\left[b_{1}, \ldots, b_{s}\right]$, and write $d_{i}:=b_{i}-v_{i}$ for $1 \leq i \leq s$. Then, by Definition 4.4, we have
$$\lambda+1=\sum_{i=1}^{s} d_{i}=\sum_{i=1}^{s}\left(b_{i}-v_{i}\right),$$
Therefore, for fixed $\left[b_{1}, \ldots, b_{s}\right]$, minimizing the weight $\lambda$ is equivalent to maximizing $\sum_{i=1}^{s} v_{i}$.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/2dae99b7-7727-4d39-986f-6b5c5a7baa79-13.jpg?height=342&width=1252&top_left_y=408&top_left_x=465}
\captionsetup{labelformat=empty}
\caption{Figure 2: Adding a new vertex}
\end{figure}

On the other hand, if $\left[v_{1}, \ldots, v_{s}\right]$ corresponds to a triangulation of the $(s+1)$-gon $P_{0} P_{1} \cdots P_{s}$, then
$$\sum_{i=0}^{s} v_{i}=3(s-1) .$$
Since every triangulation satisfies $v_{0} \geq 1, \sum_{i=1}^{s} v_{i}$ is maximal if and only if $v_{0}=1$. Now the weight 2 zero continued fraction constructed above for a dual 0-Wahl chain is realized by a triangulation with $v_{0}=1$. Hence it maximizes $\sum_{i=1}^{s} v_{i}$, and therefore its weight is minimal among all admissible zero continued fractions. Therefore, we conclude that $\alpha\left(\left[b_{1}, \ldots, b_{s}\right]\right)=2$. \(\square\)

We recall the notion of an extremal P-resolution. Extremal P-resolutions arise naturally in the birational geometry of degenerations of surfaces with Wahl singularities. In Urzúa's framework of $W$-surfaces, they appear as surface-theoretic models associated with semistable extremal neighborhoods and their flips. Thus, among all P-resolutions, extremal P-resolutions correspond to the case where the exceptional locus is as small as possible and all singularities on the partial resolution are Wahl singularities.

Definition 4.10. Let $f: W^{+} \rightarrow W$ be a P-resolution of a cyclic quotient singularity $(P \in W)$. We say that $f$ is an extremal $P$-resolution if $f^{-1}(P)$ is a smooth rational curve $\Gamma$, and $W^{+}$has only Wahl singularities.

Remark 4.11. Let $W=\mathbb{C}^{2} / G_{r, a}$ be a cyclic quotient singularity, and let $\frac{r}{r-a}=\left[b_{1}, \ldots, b_{s}\right]$ be the dual Hirzebruch-Jung continued fraction. By [7, §4.1], the extremal P-resolutions of $W$ are in one-to-one correspondence with pairs of indices $1 \leq i<j \leq s$ such that
$$\left[b_{1}, \ldots, b_{i}-1, \ldots, b_{j}-1, \ldots, b_{s}\right]=0 .$$
In our terminology, this means precisely that the dual Hirzebruch-Jung continued fraction admits an admissible zero continued fraction of weight 1 .

Remark 2.9, Theorem 4.9 and Remark 4.11 lead to the following.
Corollary 4.12. If $r / a$ is a 1 -Wahl chain, then the cyclic quotient singularity $\mathbb{C}^{2} / G_{r, a}$ has an extremal $P$-resolution.

\section*{References}
\begin{itemize}
\item[] [1] K. Altmann, P-Resolutions of Cyclic Quotients from the Toric Viewpoint. In: Arnold, V.I., Greuel, GM., Steenbrink, J.H.M. (eds) Singularities. Progress in Mathematics 162. Birkhäuser, Basel (1998), 241-250.
\item[] [2] D. A. Cox, J. B. Little, and H. K. Schenck, Toric varieties, Graduate Studies in Mathematics, vol. 124, Amer. Math. Soc., (2011)
\item[] [3] J.A. Christophersen, On the components and discriminant of the versal base space of cyclic quotient singularities, Singularity theory and its applications, Part I(Coventry, 1988/1989), (1991), 81-92.
\item[] [4] Y. Gyoda and K. Matsushita, Generalization of Markov Diophantine equation via generalized cluster algebra, Electron. J. Combin., 30(4) (2023), 4-10.
\item[] [5] Y. Gyoda, S. Maruyama and Y. Sato, SL(2, Z)-matrixizations of Generalized Markov numbers, arXiv: 2407.08203, 2024.
\item[] [6] P. Hacking and Y. Prokhorov, Smoothable del Pezzo surfaces with quotient singularities, Compos. Math. 146 (2010), 169-192.
\item[] [7] P. Hacking, J. Tevelev, and G. Urzúa, Flipping surfaces, Journal of Algebraic Geometry 26 (2017), 279-345.
\item[] [8] Y. Ito, Special McKay correspondence, In Geometry of toric varieties, volume 6 of Semin.Congr., Soc. Math. France, Paris, (2002), 213-225.
\item[] [9] J. Kollár and N. I. Shepherd-Barron, Threefolds and deformations of surface singularities, Invent. Math. 91 (1988), 299-338.
\item[] [10] M. Perling, Unfocused notes on the Markoff equation and T-Singularities, 2022. preprint, arXiv:2210.12982, 2022.
\item[] [11] O. Riemenschneider, Characterization and application of special reflexive modules on rational surface singularities, Institute Mittag-Leffler Report No. 3 (1987).
\item[] [12] G. Urzúa, Negative continued fractions in birational geometry: A guide to degenerations of surfaces with Wahl singularities, book, https://www.mat.uc.cl/urzua/libro.pdf, (2025)
\item[] [13] G. Urzúa and J. P. Zúñiga, The birational geometry of Markov numbers, arXiv:2310.17957, 2023.
\item[] [14] J. Wahl, Smoothings of normal surface singularities, Topology, 20(3), (1981), 219-246.
\item[] [15] J. Wunram, Reflexive modules on cyclic quotient surface singularities, in Singularities, Representations of Algebras, and Vector Bundles. Greuel, Trautmann (eds.) Lect. Notes math. 1273. Springer (1987).
\end{itemize}
[16] J. Wunram, Reflexive modules on quotient surface singularities, Math Ann. 279 (1988), 583-598.

\section*{Yusuke Sato}

Department of Mathematics, Osaka Institute of Technology, 5-16-1 Ohmiya, Asahi-ku, Osaka, 535-8585, Japan.
email: yusuke.sato@oit.ac.jp