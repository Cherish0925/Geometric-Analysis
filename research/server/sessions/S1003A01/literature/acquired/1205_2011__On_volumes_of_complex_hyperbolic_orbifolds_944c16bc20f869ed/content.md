---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 1205_2011.pdf
converter: mathpix
format: mmd
---

\title{
ON VOLUMES OF COMPLEX HYPERBOLIC ORBIFOLDS
}

\author{
ILESANMI ADEBOYE AND GUOFANG WEI
}

\begin{abstract}
We construct an explicit lower bound for the volume of a complex hyperbolic orbifold that depends only on dimension.
\end{abstract}

\section*{0. Introduction}

A hyperbolic orbifold is a quotient of real, complex, quaternionic or octonionic hyperbolic space, by a discrete group of isometries, usually denoted by $\Gamma$. An orbifold is a manifold when $\Gamma$ contains no elements of finite order.

The real hyperbolic 2-orbifold of minimum volume was identified by Siegal [20]. An analogous result in dimension three was proved by Gehring and Martin [7]. In the remaining dimensions, and algebras of definition, the existence of a hyperbolic orbifold of minimum volume is guaranteed by a theorem of Wang [22].

In this paper, we prove an explicit lower bound for the volume of any complex hyperbolic orbifold that depends only on dimension. Our methods here are similar to those of the prequel [2], which addressed the real hyperbolic case. The complex setting provides an additional corollary and the corresponding Lie group curvature calculations are of independent interest.

Let $\mathbf{H}_{\mathbb{C}}^{n}$ denote complex hyperbolic $n$-space. The holomorphic sectional curvature of $\mathbf{H}_{\mathbb{C}}^{n}$ is normalized to be -1, accordingly, the sectional curvatures are pinched between -1 and -1/4. Let $\operatorname{SU}(n, 1)$ denote the indefinite special unitary group of indicated signature. This group is a Lie group and it acts transitively by isometries on complex hyperbolic space. With an appropriate scale of a canonical metric on $\operatorname{SU}(n, 1)$, we define a Riemannian submersion $\pi: \operatorname{SU}(n, 1) / \Gamma \rightarrow \mathbf{H}_{\mathbb{C}}^{n} / \Gamma$. The volume of a complex hyperbolic $n$-orbifold is thereby described in terms of the volume of the fundamental domain of a lattice in a Lie group. The latter is then bounded from below using results due to Wang [22] and Gunther (see e.g. [6]). In what follows dimension will refer to complex dimension, unless otherwise stated.

Theorem 0.1. The volume of a complex hyperbolic $n$-orbifold is bounded below by $\mathcal{C}(n)$, an explicit constant depending only on dimension, given by
$$\mathcal{C}(n)=\frac{2^{n^{2}+n+1} \pi^{n / 2}(n-1)!(n-2)!\cdots!3!2!1!}{(36 n+21)^{\left(n^{2}+2 n\right) / 2} \Gamma\left(\left(n^{2}+2 n\right) / 2\right)} \int_{0}^{\min [0.06925 \sqrt{36 n+21}, \pi]} \sin ^{n^{2}+2 n-1} \rho d \rho$$

\footnotetext{
The second author is partially supported by NSF grant DMS-1105536.
}

The formula of Theorem 0.1 gives a lower bound of 0.002 for complex 1-orbifolds and $2.918 \times 10^{-9}$ for complex hyperbolic 2-orbifolds. Since complex hyperbolic 1-space is isometric to real hyperbolic 2-space, a sharp volume bound of $\pi / 21$ for complex hyperbolic 1-orbifolds follows immediately from the classical results of Hurwitz [11] and Siegel [20].

As in [2], we note that volume bounds for hyperbolic orbifolds provide immediate information on the order of the symmetry groups of hyperbolic manifolds. Following Hurwitz's formula for groups acting on surfaces, we have the following corollary.

Corollary 0.2. Let $M$ be an complex hyperbolic $n$-manifold. Let $H$ be a group of isometries of $M$. Then
$$|H| \leq \frac{\operatorname{Vol}[M]}{\mathcal{C}(n)} .$$

The Chern-Gauss-Bonnet formula (see e.g. [10]) describes volume in terms of Euler characteristic:
$$\operatorname{Vol}(M)=\frac{(-4 \pi)^{n}}{(n+1)!} \chi(M) .$$
This formula gives an explicit lower bound for the class of complex hyperbolic manifolds. In that case the Euler characteristic is integer valued. However, there is no such restriction for orbifolds. The formula also provides an alternate version of Corollary 0.2.

Corollary 0.3. Let $M$ be a finite volume complex hyperbolic $n$-manifold. Let $H$ be a group of isometries of $M$. Then
$$|H| \leq \frac{(-4 \pi)^{n}}{\mathcal{C}(n)(n+1)!} \chi(M) .$$

The next section gives a definition of complex hyperbolic space and concludes with our preferred symmetric space representation. A comprehensive treatment of complex hyperbolic geometry can be found in [9]. Section 2 provides the background on the geometry of $\operatorname{SU}(n, 1)$ that we will use, subsequently. For more details, the reader may consult Chapter 6 of [13] or Sections 1-3 of [2], where we undertook a similar analysis of $\mathrm{SO}_{o}(n, 1)$.

\section*{1. Complex Hyperbolic Space}

Let $\mathbb{C}^{n, 1}$ be a complex vector space of dimension $(n+1)$ equipped with the Hermitian form
$$\langle\mathbf{z}, \mathbf{w}\rangle=\mathbf{z} J \mathbf{w}^{*}=z_{1} \overline{w_{1}}+z_{2} \overline{w_{2}}+\cdots+z_{n} \overline{w_{n}}-z_{n+1} \overline{w_{n+1}},$$
where
$$J=\left(\begin{array}{lllll}
1 & & & & \\
& 1 & & & \\
& & \ddots & & \\
& & & 1 & \\
& & & -1
\end{array}\right)$$
and $(\cdot)^{*}$ represents conjugate transpose. Note that, for all $\mathbf{z} \in \mathbb{C}^{n, 1}$ and $\lambda \in \mathbb{C},\langle\mathbf{z}, \mathbf{z}\rangle \in \mathbb{R}$ and $\langle\lambda \mathbf{z}, \lambda \mathbf{z}\rangle=|\lambda|^{2}\langle\mathbf{z}, \mathbf{z}\rangle$.

Let
$$V_{-}=\left\{\mathbf{z} \in \mathbb{C}^{n, 1}:\langle\mathbf{z}, \mathbf{z}\rangle<0\right\},$$
and let
$$\mathbb{P}: \mathbb{C}^{n, 1}-\{0\} \rightarrow \mathbb{C} \mathbf{P}^{n}$$
be the canonical projection onto complex projective space. Complex hyperbolic $n$-space, $\mathbf{H}_{\mathbb{C}}^{n}$, is defined to be the space $\mathbb{P}\left(V_{-}\right)$together with the Bergman metric. The Bergman metric is defined by the distance function $\rho$, given by the formula
$$\cosh ^{2}\left(\frac{\rho(z, w)}{2}\right)=\frac{\langle\mathbf{z}, \mathbf{w}\rangle\langle\mathbf{w}, \mathbf{z}\rangle}{\langle\mathbf{z}, \mathbf{z}\rangle\langle\mathbf{w}, \mathbf{w}\rangle},$$
where $\mathbf{z}$ and $\mathbf{w}$ are lifts of $z, w \in \mathbf{H}_{\mathbb{C}}^{n}$.
Let $\operatorname{GL}(n, \mathbb{C})$ be the group of complex nonsingular $n$-by- $n$ matrices. The unitary group is defined and denoted by
$$U(n)=\left\{A \in \operatorname{GL}(n, \mathbb{C}) \mid A A^{*}=I\right\} .$$
Denote by $U(n, 1)$ the group of all linear transformation of $\mathbb{C}^{n, 1}$ which leave the form $\langle\mathbf{z}, \mathbf{w}\rangle$ invariant. That is,
$$U(n, 1)=\left\{A \in \operatorname{GL}(n+1, \mathbb{C}) \mid A J A^{*}=J\right\} .$$

The induced action of $U(n, 1)$ on $\mathbb{C} \mathbf{P}^{n}$ preserves $\mathbf{H}_{\mathbb{C}}^{n}$ and acts by isometries. The stabilizer of the point of $\mathbf{H}_{\mathbb{C}}^{n}$ with homogeneous coordinates $[0: \cdots: 0: 1]$ is
$$U(n) \times U(1)=\left\{\left.\left(\begin{array}{cc}
A & 0 \\
0 & e^{i \theta}
\end{array}\right) \right\rvert\, A \in U(n), \theta \in[0,2 \pi)\right\} .$$
We can identify $U(n)$ with the elements of $U(n) \times U(1)$ that have determinant 1 by the map
$$A \rightarrow\left(\begin{array}{cc}
A & 0 \\
0 & (\operatorname{det} A)^{-1}
\end{array}\right) .$$

Hence,
$$\mathbf{H}_{\mathbb{C}}^{n}=U(n, 1) /\{U(n) \times U(1)\}=\operatorname{SU}(n, 1) / S\{U(n) \times U(1)\}=\operatorname{SU}(n, 1) / U(n) .$$

\section*{2. The Lie group SU $(n, 1)$}

A matrix Lie group is a closed subgroup of $\operatorname{GL}(n, \mathbb{C})$. Recall that for a square matrix $X$,
$$e^{X}=I+X+\frac{1}{2} X^{2}+\cdots .$$
The Lie algebra of a matrix Lie group $G$ is a vector space, defined as the set of matrices $X$ such that $e^{t X} \in G$, for all real numbers $t$. The Lie algebra of $\operatorname{GL}(n, \mathbb{C})$, denoted by $\mathfrak{g} \mathfrak{l}(n, \mathbb{C})$, is the set of all $n \times n$ matrices over $\mathbb{C}$.

The indefinite special unitary group,
$$\operatorname{SU}(n, 1)=\{A \in U(n, 1): \operatorname{det} A=1\},$$
is a matrix Lie group of real dimension $n^{2}+2 n$. The Lie algebra of $\operatorname{SU}(n, 1)$ is defined and denoted by
$$\mathfrak{s} \mathfrak{u}(n, 1)=\left\{X \in \mathfrak{g} \mathfrak{l}(n, \mathbb{C}) \mid J X^{*} J=-X, \text { trace } X=0\right\} .$$

Definition 2.1. For each $n$, let $e_{j k} \in \mathfrak{g l}(n+1, \mathbb{C})$ be the matrix with 1 in the $j k$-position and 0 elsewhere. Furthermore, let $\alpha_{j k}=\left(e_{j k}-e_{k j}\right), \beta_{j k}=\left(e_{j k}+e_{k j}\right)$ and $h_{j}=i\left(e_{j j}-e_{n+1, n+1}\right)$. The standard basis for $\mathfrak{s} \mathfrak{u}(n, 1)$, denoted by $\mathfrak{B}$, consists of the following set of $n^{2}+2 n$ matrices:
$$\begin{aligned}
& \alpha_{j k}, 1 \leq j<k \leq n, \quad i \beta_{j k}, 1 \leq j<k \leq n, \\
& \beta_{j, n+1}, 1 \leq j \leq n, \quad i \alpha_{j, n+1}, 1 \leq j \leq n, \\
& h_{j}, 1 \leq j \leq n .
\end{aligned}$$

The Lie bracket of a matrix Lie algebra is determined by matrix operations:
$$[X, Y]=X Y-Y X .$$
The following proposition describes the Lie bracket of $\mathfrak{s} \mathfrak{u}(n, 1)$. The proof involves straightforward calculation and is omitted.

Proposition 2.2. For $1 \leq j<k \leq n, 1 \leq l<m \leq n$,
$$\begin{gathered}
{\left[\alpha_{j k}, \alpha_{l m}\right]=\delta_{k l} \alpha_{j m}+\delta_{k m} \alpha_{l j}+\delta_{j m} \alpha_{k l}+\delta_{l j} \alpha_{m k},} \\
{\left[i \beta_{j k}, i \beta_{l m}\right]=-\left(\delta_{k l} \alpha_{j m}+\delta_{k m} \alpha_{j l}+\delta_{j m} \alpha_{k l}+\delta_{l j} \alpha_{k m}\right),} \\
{\left[h_{j}, h_{k}\right]=0,} \\
{\left[\alpha_{j k}, i \beta_{l m}\right]=i\left(\delta_{k l} \beta_{j m}+\delta_{k m} \beta_{j l}-\delta_{j m} \beta_{k l}-\delta_{l j} \beta_{k m}\right),} \\
{\left[\alpha_{j k}, h_{l}\right]=i\left(\delta_{k l} \beta_{j l}-\delta_{l j} \beta_{k l}\right),} \\
{\left[h_{l}, i \beta_{j k}\right]=\delta_{k l} \alpha_{j l}+\delta_{l j} \alpha_{k l},}
\end{gathered}$$
$$\begin{aligned}
{\left[\alpha_{j k}, \beta_{l, n+1}\right] } & =\delta_{l k} \beta_{j, n+1}-\delta_{j l} \beta_{k, n+1}, \\
{\left[\alpha_{j k}, i \alpha_{l, n+1}\right] } & =i\left(\delta_{k l} \alpha_{j, n+1}-\delta_{l j} \alpha_{k, n+1}\right), \\
{\left[i \beta_{j k}, \beta_{l, n+1}\right] } & =i\left(\delta_{l k} \alpha_{j, n+1}+\delta_{j l} \alpha_{k, n+1}\right), \\
{\left[i \beta_{j k}, i \alpha_{l, n+1}\right] } & =-\left(\delta_{l k} \beta_{j, n+1}+\delta_{j l} \beta_{k, n+1}\right), \\
{\left[h_{j}, \beta_{l, n+1}\right] } & =i\left(\delta_{j l} \alpha_{j, n+1}+\alpha_{l, n+1}\right), \\
{\left[h_{j}, i \alpha_{l, n+1}\right] } & =-\left(\delta_{j l} \beta_{j, n+1}+\beta_{l, n+1}\right),
\end{aligned}$$
$$\begin{gathered}
{\left[\beta_{j, n+1}, \beta_{k, n+1}\right]=\alpha_{j k},} \\
{\left[i \alpha_{j, n+1}, i \alpha_{k, n+1}\right]=\alpha_{j k},} \\
{\left[i \alpha_{j, n+1}, \beta_{k, n+1}\right]=i\left(\beta_{j k}-2 \delta_{j k} e_{n+1, n+1}\right) .}
\end{gathered}$$

Remark 2.3. Proposition 2.2 illustrates a Cartan decomposition $\mathfrak{s u}(n, 1)=\mathfrak{k} \oplus \mathfrak{p}$, where
$$\begin{gathered}
\mathfrak{k}=\operatorname{span}\left\{\alpha_{j k}, i \beta_{j k}, h_{j}, 1 \leq j<k \leq n\right\}, \mathfrak{p}=\operatorname{span}\left\{\beta_{j, n+1}, i \alpha_{j, n+1}, 1 \leq j \leq n\right\}, \\
{[\mathfrak{k}, \mathfrak{k}] \subset \mathfrak{k}, \quad[\mathfrak{k}, \mathfrak{p}] \subset \mathfrak{p}, \text { and }[\mathfrak{p}, \mathfrak{p}] \subset \mathfrak{k} .}
\end{gathered}$$
2.1. The Canonical Metric of $\operatorname{SU}(n, 1)$. For $X \in \mathfrak{s u}(n, 1)$, the adjoint action of $X$ is the $\mathfrak{s u}(n, 1)$-endomorphism defined by the Lie bracket,
$$\operatorname{ad} X(Y)=[X, Y] .$$
The Killing form on $\mathfrak{s u}(n, 1)$ is a symmetric bilinear form given by
$$B(X, Y)=\operatorname{trace}(\operatorname{ad} X \operatorname{ad} Y) .$$
A positive definite inner product on $\mathfrak{s u}(n, 1)$ is then defined by putting
$$\langle X, Y\rangle= \begin{cases}B(X, Y) & \text { for } X, Y \in \mathfrak{p}, \\ -B(X, Y) & \text { for } X, Y \in \mathfrak{k}, \\ 0 & \text { otherwise. }\end{cases}$$

By identifying $\mathfrak{s u}(n, 1)$ with the tangent space at the identity of $\operatorname{SU}(n, 1)$, we extend $\langle\cdot, \cdot\rangle$ to a left invariant Riemannian metric over $\operatorname{SU}(n, 1)$. We denote this metric by $g$ and refer to it as the canonical metric for $\operatorname{SU}(n, 1)$.

Lemma 2.4. For $X, Y \in \mathfrak{B}$,
$$\langle X, Y\rangle=\left\{\begin{array}{cc}
4 n+4 & \text { if } \quad X=Y \\
0 & \text { otherwise } .
\end{array}\right.$$
Proof. Let
$$\begin{aligned}
\mathfrak{k}_{j k} & =\operatorname{span}\left\{\alpha_{j k}, i \beta_{j k}\right\}, 1 \leq j<k \leq n, \\
\mathfrak{k}_{h} & =\operatorname{span}\left\{h_{j}, j=1, \cdots, n\right\}, \\
\mathfrak{p}_{j} & =\operatorname{span}\left\{\beta_{j, n+1}, i \alpha_{j, n+1}\right\}, 1 \leq j \leq n .
\end{aligned}$$

By (2.5), (2.6), (2.11) and (2.12), for each $h \in \mathfrak{k}_{h}, \operatorname{ad} h\left(\mathfrak{k}_{j k}\right) \subset \mathfrak{k}_{j k}$ and $\operatorname{ad} h\left(\mathfrak{p}_{j}\right) \subset \mathfrak{p}_{j}$. In fact, if $h=\sum_{s} d_{s} h_{s}$, then
$$\begin{gathered}
{\left[h, \alpha_{j k}\right]=\left(d_{j}-d_{k}\right) i \beta_{j k},} \\
{\left[h, i \beta_{j k}\right]=\left(d_{k}-d_{j}\right) \alpha_{j k},} \\
{\left[h, \beta_{j, n+1}\right]=\left(d_{j}+\sum_{s} d_{s}\right) i \alpha_{j, n+1},} \\
{\left[h, i \alpha_{j, n+1}\right]=-\left(d_{j}+\sum_{s} d_{s}\right) \beta_{j, n+1} .}
\end{gathered}$$

Therefore,
$$\begin{aligned}
B(h, h)=\operatorname{trace}\left((\operatorname{ad} h)^{2}\right) & =\sum_{j<k} \operatorname{trace}\left(\left(\left.\operatorname{ad} h\right|_{\mathfrak{k}_{j k}}\right)^{2}\right)+\sum_{j} \operatorname{trace}\left(\left(\left.\operatorname{ad} h\right|_{\mathfrak{p}_{j}}\right)^{2}\right) \\
& =-\sum_{j, k}\left(d_{j}-d_{k}\right)^{2}-2 \sum_{j}\left(d_{j}+\sum_{k} d_{k}\right)^{2} \\
& =-(2 n+2)\left(\sum_{j} d_{j}^{2}+\left(\sum_{j} d_{j}\right)^{2}\right) \\
& =(2 n+2)(\operatorname{trace} h)^{2} .
\end{aligned}$$
Since each element of $\mathfrak{s} \mathfrak{u}(n, 1)$ can be diagonalized, for each $X \in \mathfrak{s} \mathfrak{u}(n, 1)$, there is a matrix $A$ such that $A X A^{-1} \in \mathfrak{k}_{h}$. By the invariance of $B$ and trace, $B(X, X)=2(n+1) \operatorname{trace}\left(X^{2}\right)$. By polarization,
$$B(X, Y)=2(n+1) \operatorname{trace}(X Y), \quad X, Y \in \mathfrak{s u}(n, 1) .$$
Hence when $X \neq Y \in \mathfrak{B}$, we have $\langle X, X\rangle=4(n+1)$ and $\langle X, Y\rangle=0$. \(\square\)

Corollary 2.5. The matrix representation for the canonical metric $g$ of $\operatorname{SU}(n, 1)$ is the square $n^{2}+2 n$ diagonal matrix
$$\left(\begin{array}{cccc}
4 n+4 & & & \\
& 4 n+4 & & \\
& & \ddots & \\
& & & 4 n+4
\end{array}\right) .$$

We will be interested in the metric on $\operatorname{SU}(n, 1)$ that induces holomorphic sectional curvature -1 on the quotient $\operatorname{SU}(n, 1) / U(n)$. To this end, we scale the canonical metric by a factor of $\frac{1}{n+1}$. Formally,

Definition 2.6. Let $g$ be the canonical metric on $\operatorname{SU}(n, 1)$. The metric $\tilde{g}$ on $\operatorname{SU}(n, 1)$ is defined by
$$\tilde{g}=\frac{1}{n+1} g .$$

Finally, a canonical metric on a Lie algebra $\mathfrak{g}$ induces a norm given by
$$\|X\|=\langle X, X\rangle^{1 / 2} .$$
Let,
$$N(\operatorname{ad} X)=\sup \{\|\operatorname{ad} X(Y)\| \mid Y \in \mathfrak{g},\|Y\|=1\},$$
$$C_{1}=\sup \{N(\operatorname{ad} X) \mid X \in \mathfrak{p},\|X\|=1\} \text { and } C_{2}=\sup \{N(\operatorname{ad} X)\|X \in \mathfrak{k},\| X \|=1\} .$$

The appendix to [22] includes a table of the constants $C_{1}$ and $C_{2}$ for noncompact and nonexceptional Lie groups. The values for $\operatorname{SU}(n, 1)$ are
$$C_{1}=C_{2}=(n+1)^{-1 / 2} .$$
However, with respect to the scaled canonical metric $\tilde{g}$, we have
$$C_{1}=C_{2}=1 .$$
2.2. The Sectional Curvatures of $\operatorname{SU}(n, 1)$. A connection ∇ on the tangent bundle of a manifold can be expressed in terms of a left invariant metric by the Koszul formula. For any left invariant vector fields $X, Y, Z$ we have
$$\left\langle\nabla_{X} Y, Z\right\rangle=\frac{1}{2}\{\langle[X, Y], Z\rangle-\langle Y,[X, Z]\rangle-\langle X,[Y, Z]\rangle\} .$$
The curvature tensor of a connection ∇ is defined by
$$R(X, Y) Z=\nabla_{X} \nabla_{Y} Z-\nabla_{Y} \nabla_{X} Z-\nabla_{[X, Y]} Z .$$
In [2], we derived the curvature formulas for the canonical metric of a semisimple noncompact Lie group. These formulas also apply to $\tilde{g}$, as it is simply a scale of the canonical metric. Let $U, V, W \in \mathfrak{k}$ and $X, Y, Z \in \mathfrak{p}$ denote left invariant vector fields.

Proposition 2.7.
$$\begin{aligned}
R(U, V) W & =\frac{1}{4}[[V, U], W], \\
R(X, Y) Z & =-\frac{7}{4}[[X, Y], Z], \\
R(U, X) Y & =\frac{1}{4}[[X, U], Y]-\frac{1}{2}[[Y, U], X], \\
R(X, Y) V & =\frac{3}{4}[X,[V, Y]]+\frac{3}{4}[Y,[X, V]] .
\end{aligned}$$
In particular,
$$\begin{aligned}
\langle R(U, V) W, X\rangle & =0, \\
\langle R(X, Y) Z, U\rangle & =0, \\
\langle R(U, V) V, U\rangle & =\frac{1}{4}\|[U, V]\|^{2}, \\
\langle R(X, Y) Y, X\rangle & =-\frac{7}{4}\|[X, Y]\|^{2}, \\
\langle R(U, X) X, U\rangle & =\frac{1}{4}\|[U, X]\|^{2} .
\end{aligned}$$

The sectional curvature of the planes spanned by $X, Y \in \mathfrak{g}$ is denoted and defined by
$$K(X, Y)=\frac{\langle R(X, Y) Y, X\rangle}{\|X\|^{2}\|Y\|^{2}-\langle X, Y\rangle^{2}} .$$

Proposition 2.8. The sectional curvature of $\operatorname{SU}(n, 1)$ with respect to the metric $\tilde{g}$ at the planes spanned by standard basis elements is bounded above by 1/4.

Proof. Since the basis elements are mutually orthogonal, the sectional curvature at the plane spanned by any distinct elements $X, Y \in \mathfrak{B}$ is given by
$$K(X, Y)=\frac{\langle R(X, Y) Y, X\rangle}{\|X\|^{2}\|Y\|^{2}} .$$
By (2.27), (2.28), (2.29) and Proposition 2.2, the largest sectional curvature spanned by basis directions are the planes spanned by $h_{j}, i \alpha_{j, n+1}$ or $h_{j}, \beta_{j, n+1}$. And
$$K\left(h_{j}, i \alpha_{j, n+1}\right)=\frac{\frac{1}{4}\left\|\left[h_{j}, i \alpha_{j, n+1}\right]\right\|^{2}}{\left\|h_{j}\right\|^{2}\left\|i \alpha_{j, n+1}\right\|^{2}}=\frac{1}{4} \frac{\left\|-2 \beta_{j, n+1}\right\|^{2}}{4 \cdot 4}=1 / 4 .$$ \(\square\)

Proposition 2.9. The sectional curvatures of $\operatorname{SU}(n, 1)$ with respect to $\tilde{g}$ are bounded above by
$$\frac{1}{4}+2 \cdot \frac{1}{4}+2 \cdot \frac{6}{4} \cdot(2 n+1)+2 \cdot \frac{3}{4} \cdot(2 n+1)=\frac{36 n+21}{4} .$$
Proof. Again with $U, V \in \mathfrak{k}$ and $X, Y \in \mathfrak{p}$, we have by (2.25) and (2.26)
$$\begin{aligned}
\langle R(X+U, Y+V) Y+V, X+U\rangle & =\langle R(X, Y) Y, X\rangle+\langle R(U, V) V, U\rangle+\langle R(U, Y) Y, U\rangle \\
& +\langle R(X, V) V, X\rangle+2\langle R(X, Y) V, U\rangle+2\langle R(X, V) Y, U\rangle .
\end{aligned}$$
Assume that $\|U+X\|=1,\|V+Y\|=1$ and $\langle U+X, V+Y\rangle=0$. Write
$$\begin{gathered}
U=\sum_{j<k}\left(a_{j k} \alpha_{j k}+b_{j k} i \beta_{j k}\right)+\sum_{j} c_{j} h_{j}, \quad V=\sum_{j<k}\left(a_{j k}^{\prime} \alpha_{j k}+b_{j k}^{\prime} i \beta_{j k}\right)+\sum_{j} c_{j}^{\prime} h_{j}, \\
X=\sum_{j=1}^{n}\left(e_{j} i \alpha_{j, n+1}+f_{j} \beta_{j, n+1}\right), \quad Y=\sum_{j=1}^{n}\left(e_{j}^{\prime} i \alpha_{j, n+1}+f_{j}^{\prime} \beta_{j, n+1}\right) .
\end{gathered}$$
Note that
$$\sum_{j<k}\left|a_{j k}\right|^{2}+\left|b_{j k}\right|^{2}+c_{j}^{2}, \sum_{j<k}\left|a_{j k}^{\prime}\right|^{2}+\left|b_{j k}^{\prime}\right|^{2}+\left|c_{j}^{\prime}\right|^{2}, \sum_{j=1}^{n} e_{j}^{2}+f_{j}^{2}, \sum_{j=1}^{n}\left|e_{j}^{\prime}\right|^{2}+\left|f_{j}^{\prime}\right|^{2} \leq \frac{1}{4} .$$
By (2.21) and (2.23),
and
$$\begin{aligned}
R(U, V) V & =\frac{1}{4}[[V, U], V]=-\frac{1}{4} \operatorname{ad} V \circ \operatorname{ad} V(U) \\
R(U, Y) Y & =-\frac{1}{4}[[Y, U], Y]=\frac{1}{4} \operatorname{ad} Y \circ \operatorname{ad} Y(U) .
\end{aligned}$$

Therefore, by (2.20),
and
$$\begin{aligned}
\langle R(U, V) V, U\rangle & \leq \frac{1}{4} C_{2}^{2}=\frac{1}{4} \\
\langle R(U, Y) Y, U\rangle & \leq \frac{1}{4} C_{1}^{2}=\frac{1}{4} .
\end{aligned}$$

By (2.24), we have
$$\langle R(X, Y) V, U\rangle=-\frac{3}{4}(\langle[U, X],[V, Y]\rangle+\langle[V, X],[U, Y]\rangle) .$$
From (2.7)-(2.12),
$$\begin{aligned}
\|[U, Y]\|^{2}= & \left\|\left[\sum_{j<k}\left(a_{j k} \alpha_{j k}+b_{j k} i \beta_{j k}\right)+\sum_{j} c_{j} h_{j}, \sum_{l=1}^{n}\left(e_{l}^{\prime} i \alpha_{l, n+1}+f_{l}^{\prime} \beta_{l, n+1}\right)\right]\right\|^{2} \\
= & \| \sum_{l}\left\{\left(\sum_{j}\left(a_{l j} e_{j}^{\prime}+b_{l j} f_{j}^{\prime}+c_{j} f_{l}^{\prime}\right)+c_{l} f_{l}^{\prime}\right) i \alpha_{l, n+1}\right. \\
& \left.+\left(\sum_{j}\left(a_{l j} f_{j}^{\prime}-b_{l j} e_{j}^{\prime}-c_{j} e_{l}^{\prime}\right)-c_{l} e_{l}^{\prime}\right) \beta_{l, n+1}\right\} \|^{2} \\
= & 4 \sum_{l}\left\{\left(\sum_{j}\left(a_{l j} e_{j}^{\prime}+b_{l j} f_{j}^{\prime}+c_{j} f_{l}^{\prime}\right)+c_{l} f_{l}^{\prime}\right)^{2}+\left(\sum_{j}\left(a_{l j} f_{j}^{\prime}-b_{l j} e_{j}^{\prime}-c_{j} e_{l}^{\prime}\right)-c_{l} e_{l}^{\prime}\right)^{2}\right\} \\
\leq & 4 \sum_{l}\left(2 \sum_{j}\left(a_{l j}^{2}+b_{l j}^{2}+c_{j}^{2}\right) \cdot \sum_{j}\left(\left|e_{j}^{\prime}\right|^{2}+\left|f_{j}^{\prime}\right|^{2}+\left|f_{l}^{\prime}\right|^{2}\right)+2 c_{l}^{2}\left|f_{l}^{\prime}\right|^{2}\right) \\
& +4 \sum_{l}\left(2 \sum_{j}\left(a_{l j}^{2}+b_{l j}^{2}+c_{j}^{2}\right) \cdot \sum_{j}\left(\left|f_{j}^{\prime}\right|^{2}+\left|e_{j}^{\prime}\right|^{2}+\left|e_{l}^{\prime}\right|^{2}\right)+2 c_{l}^{2}\left|e_{l}^{\prime}\right|^{2}\right) \\
\leq & 8 \sum_{l}\left(\frac{1}{4}\left[\frac{1}{4}+n\left|f_{l}^{\prime}\right|^{2}\right]+c_{l}^{2}\left|f_{l}^{\prime}\right|^{2}\right)+8 \sum_{l}\left(\frac{1}{4}\left[\frac{1}{4}+n\left|e_{l}^{\prime}\right|^{2}\right]+c_{l}^{2}\left|e_{l}^{\prime}\right|^{2}\right) \\
\leq & 2 n+1 .
\end{aligned}$$
Here we define $a_{k j}=-a_{j k}, b_{k j}=b_{j k}, b_{j j}=0$. Hence
$$\langle R(X, Y) V, U\rangle \leq \frac{6}{4} \cdot(2 n+1) .$$
Similarly, by (2.23),
$$\langle R(X, V) Y, U\rangle \leq \frac{3}{4} \cdot(2 n+1) .$$ \(\square\)

\section*{3. The Volume of Complex Hyperbolic Orbifolds}

This section concludes with a proof of Theorem 0.1. We begin by assembling the required prerequisites. First, a result due to H. C. Wang is used to produce a value such that the fundamental domain of any discrete subgroup $\Gamma$ of $\operatorname{SU}(n, 1)$ contains a metric ball of that radius. Next, a comparison theorem of Gunther is employed in order to bound from below the volume of a ball in $\operatorname{SU}(n, 1)$. In the third subsection, a Riemannian submersion from the quotient of $\operatorname{SU}(n, 1)$ by $\Gamma$ onto the complex hyperbolic orbifold defined by $\Gamma$ is constructed.
3.1. H. C. Wang's Result. Let G be a semisimple Lie group without compact factor. Let $C_{1}$ and $C_{2}$ be the corresponding constants as defined in (2.19). The number $R_{G}$ is defined to be the least positive zero of the real-valued function
$$F(t)=\exp C_{1} t-1+2 \sin C_{2} t-\frac{C_{1} t}{\exp C_{1} t-1} .$$

The following result (Theorem 5.2 in [22]) gives Wang's quantitative version of the well-known result of Kazhdan-Margulis [14].
Theorem 3.1 (Wang). Let $G$ be a semisimple Lie group without compact factor, let e be the identity of $G$, let $\rho$ be the distance function derived from a canonical metric, and let
$$B_{G}=\left\{x \in G: \rho(e, x) \leq R_{G}\right\} .$$
Then for any discrete subgroup $\Gamma$ of $G$, there exists $g \in G$ such that $B_{G} \cap g \Gamma g^{-1}=\{e\}$.
In addition, Wang showed that number $R_{G}$ is less than the injectivity radius of $G$. Consequently, the volume of the fundamental domain of any discrete subgroup $\Gamma$ of $G$, when viewed as a group of left translations of $G$, is bounded from below by the volume of a $\rho$-ball of radius $R_{G} / 2$.

By (2.20) and (3.1),
$$R_{\mathrm{SU}(n, 1)} \approx 0.277 \ldots$$
3.2. Gunther's Result. Let $V(d, k, r)$ denote the volume of a ball of radius $r$ in the complete simply connected Riemannian manifold of dimension $d$ with constant curvature $k$. A proof of the following comparison theorem can be found in [6, Theorem 3.101].
Theorem 3.2 (Gunther). Let $M$ be a complete Riemannian manifold of dimension $d$. For $m \in M$, let $B_{m}(r)$ be a ball which does not meet the cut-locus of $m$.

If the sectional curvatures of $M$ are bounded above by a constant $b$, then
$$\operatorname{Vol}\left[B_{m}(r)\right] \geq V(d, b, r) .$$

Proposition 3.3. Let $\Gamma$ be a discrete subgroup of $\operatorname{SU}(n, 1)$. Then
$$\operatorname{Vol}[\operatorname{SU}(n, 1) / \Gamma] \geq V\left(d_{0}, k_{0}, r_{0}\right),$$
where $d_{0}=n^{2}+2 n, k_{0}=\frac{36 n+21}{4}$ and $r_{0}=0.1385$.
Proof. The inequality is immediate from Theorems 3.1 and 3.2. The values of $d_{0}, k_{0}$ and $r_{0}$ follow from Definition 2.1, Proposition 2.9 and (3.2), respectively. \(\square\)
3.3. Riemannian Submersions. Let $(M, g)$ and $(N, h)$ be Riemannian manifolds and $q: M \rightarrow N$ a surjective submersion. The map $q$ is said to be a Riemannian submersion if
$$g(X, Y)=h(d q X, d q Y) \text { whenever } X, Y \in(\operatorname{Ker} d q)_{x}^{\perp} \text { for some } x \in M \text {. }$$

The following elementary results are proved in [2].
Lemma 3.4. Let $G$ be a semisimple Lie group and let $\mathfrak{g}$ be its Lie algebra, with Cartan decomposition $\mathfrak{g}=\mathfrak{k} \oplus \mathfrak{p}$. Let $K$ be the maximal compact subgroup of $G$ with Lie algebra $\mathfrak{k}$. Then, with respect to the canonical metric, $K$ is totally geodesic in $G$.

Lemma 3.5. Let $K \rightarrow M \xrightarrow{q} N$ denote a fiber bundle where $q$ is a Riemannian submersion and $K$ is a compact and totally geodesic submanifold of $M$. Then for any subset $Z \subset N$,
$$\operatorname{Vol}\left[q^{-1}(Z)\right]=\operatorname{Vol}[Z] \cdot \operatorname{Vol}[K]$$

Let $X, Y$ be orthonormal vector fields on $N$ and let $\tilde{X}, \tilde{Y}$ be their horizontal lifts to $M$. O'Neill's formula (see e.g. [6, Page 127]), relates the sectional curvature of the base space of a Riemannian submersion with that of the total space:
$$K_{b}(X, Y)=K_{t}(X, Y)+\frac{3}{4}\left\|[X, Y]^{\perp}\right\|^{2},$$
where $Z^{\perp}$ represents the vertical component of $Z$.
Recall the definitions and notation of Section 2 and consider the quotient map
$$\pi: \operatorname{SU}(n, 1) \rightarrow \operatorname{SU}(n, 1) / U(n) .$$
The restriction of the inner product $\langle X, Y\rangle$, defined on $\mathfrak{s u}(n, 1)=\mathfrak{k} \oplus \mathfrak{p}$, to $d_{e} \pi(\mathfrak{p})=$ $T_{\pi(e)} \operatorname{SU}(n, 1) / U(n)$, induces a Riemannian metric on the quotient space. With respect to these metrics, the map $\pi$ is a Riemannian submersion.

We now show that if $\operatorname{SU}(n, 1) / U(n)$ is equipped with the restriction of the scaled canonical metric $\tilde{g}$, it has constant holomorphic sectional curvature -1. It then follows that $\pi$ is a Riemannian submersion from $\operatorname{SU}(n, 1)$ to $\mathbf{H}_{\mathbb{C}}^{n}$, complex hyperbolic $n$-space.

Let $X \in \mathfrak{p}$ represent both a unit vector field on $\operatorname{SU}(n, 1) / U(n)$ as well as its horizontal lift. Write $X=\sum_{j=1}^{n}\left(a_{j} i \alpha_{j, n+1}+b_{j} \beta_{j, n+1}\right)$. Since $\|X\|=1$, we have $\sum_{j}\left(a_{j}^{2}+b_{j}^{2}\right)=\frac{1}{4}$.

From the identification of complex structure
$$\left(\begin{array}{cc}
0 & \xi^{*} \\
\xi & 0
\end{array}\right) \longleftrightarrow \xi \quad \text { for } \xi \in \mathbb{C},$$
$J X=\sum_{k=1}^{n}\left(-b_{k} i \alpha_{k, n+1}+a_{k} \beta_{k, n+1}\right)$. By (2.28), the holomorphic sectional curvature
$$K_{t}(X, J X)=\langle R(X, J X) J X, X\rangle=-\frac{7}{4}\|[X, J X]\|^{2} .$$

By (2.13)-(2.15),
$$\begin{aligned}
{[X, J X]^{\perp} } & =[X, J X] \\
& =\sum_{j, k}\left(a_{k} b_{j}-a_{j} b_{k}\right) \alpha_{j k}+\sum_{j \neq k}\left(a_{j} a_{k}+b_{j} b_{k}\right) i \beta_{j k}+2 \sum_{j}\left(a_{j}^{2}+b_{j}^{2}\right) h_{j} \\
& =2\left\{\sum_{j<k}\left[\left(a_{k} b_{j}-a_{j} b_{k}\right) \alpha_{j k}+\left(a_{j} a_{k}+b_{j} b_{k}\right) i \beta_{j k}\right]+\sum_{j}\left(a_{j}^{2}+b_{j}^{2}\right) h_{j}\right\} .
\end{aligned}$$
Hence
$$\begin{aligned}
K_{b}(X, J X) & =-\|[X, J X]\|^{2} \\
& =-4 \cdot 4\left\{\sum_{j<k}\left[\left(a_{k} b_{j}-a_{j} b_{k}\right)^{2}+\left(a_{j} a_{k}+b_{j} b_{k}\right)^{2}\right]+\left(\sum_{j}\left(a_{j}^{2}+b_{j}^{2}\right)^{2}\right)\right\} \\
& =-4 \cdot 4\left[\sum_{j}\left(a_{j}^{2}+b_{j}^{2}\right) \sum_{k}\left(a_{k}^{2}+b_{k}^{2}\right)\right]=-1 .
\end{aligned}$$

For a discrete group $\Gamma<\operatorname{SU}(n, 1)$ and complex hyperbolic orbifold $Q=\Gamma \backslash \mathbf{H}_{\mathbb{C}}^{n}$, the map $\pi$ induces another Riemannian submersion
$$\pi^{\prime}: \operatorname{SU}(n, 1) / \Gamma \rightarrow Q .$$
The fibers of $\pi^{\prime}$ on the smooth points of $Q$ are totally geodesic embedded copies of $U(n)$.
3.4. Main Result. We now give a proof of Theorem 0.1, which for convenience is restated below.

Theorem 0.1 The volume of a complex hyperbolic $n$-orbifold is bounded below by $\mathcal{C}(n)$, an explicit constant depending only on dimension, given by
$$\mathcal{C}(n)=\frac{2^{n^{2}+n+1} \pi^{n / 2}(n-1)!(n-2)!\cdots!3!2!1!}{(36 n+21)^{\left(n^{2}+2 n\right) / 2} \Gamma\left(\left(n^{2}+2 n\right) / 2\right)} \int_{0}^{\min [0.06925 \sqrt{36 n+21}, \pi]} \sin ^{n^{2}+2 n-1} \rho d \rho$$
Proof. Let $Q$ be a complex hyperbolic $n$-orbifold. By the last paragraph of the previous subsection, Proposition 3.3 and Lemma 3.5,
$$V\left(d_{0}, k_{0}, r_{0}\right) \leq \operatorname{Vol}[\operatorname{SU}(n, 1) / \Gamma] \leq \operatorname{Vol}\left[\pi^{-1}(Q)\right]=\operatorname{Vol}[Q] \cdot \operatorname{Vol}[U(n)] .$$
The proof follows from the following two observations:
The volumes of the classical compact groups are given explicitly in [8, Page 399]. For the unitary group, the volume with respect to the metric $\tilde{g}$ is
$$\operatorname{Vol}[U(n)]=\frac{2^{n} \pi^{\left(n^{2}+n\right) / 2}}{(n-1)!(n-2)!\cdots!3!2!1!} .$$

The complete simply connected Riemannian manifold with constant curvature $k>0$ is the sphere of radius $k^{-1 / 2}$. By explicit computation we have
$$V(d, k, r)=\frac{2(\pi / k)^{d / 2}}{\Gamma(d / 2)} \int_{0}^{\min \left[r k^{1 / 2}, \pi\right]} \sin ^{d-1} \rho d \rho$$ \(\square\)

\section*{4. Volume Bounds}

In this section, we give an outline of current results on complex hyperbolic volume. The isometries of complex hyperbolic space are classified into three types: elliptic, parabolic and loxodromic (see e.g. [9]). A finite volume complex hyperbolic orbifold $\mathbf{H}_{\mathbb{C}}^{n} / \Gamma$ is : a manifold when $\Gamma$ does not contain elliptic elements; closed (or compact) when $\Gamma$ does not contain parabolic elements and cusped (or noncompact) when it does; and arithmetic when $\Gamma$ can be derived by a specific number-theoretic construction (see e.g. [4]).
4.1. Complex Hyperbolic Manifolds. In [10], Hersonsky and Paulin used the Chern-Gauss-Bonnet formula to prove that the smallest volume of a closed complex hyperbolic 2 -manifold is $8 \pi^{2}$. The work of Prasad and Yeung [17], [18] and Cartwright and Steger [3] on the classification of fake projective planes has produced 51 explicit examples. An article by Yeung [24] shows that this list is exhaustive. Xie, Wang and Jiang [23] give, for each dimension $n$, an explicit lower bound for the largest number such that every complex hyperbolic $n$-manifold contains an embedded ball of that radius.
4.2. Cusped Complex Hyperbolic Manifolds. Parker [16] proved that the smallest volume of a cusped (and so of any) complex hyperbolic 2 -manifold is $8 \pi^{2} / 3$ and found one such example. A total of eight such manifolds are given by Stover [21]. Volume bounds for noncompact complex hyperbolic manifolds in terms of dimension and the number of cusps were given by Hersonsky and Paulin [10] and Parker [16]. These bounds were later improved by Hwang [12] using methods from algebraic geometry. Kim and Kim [15] give a bound that is sharper than [12] in the case where a complex hyperbolic manifold has exactly one cusp.
4.3. Complex Hyperbolic Orbifolds. Parker [16] also proved that the volume of a cusped complex hyperbolic 2-orbifold is bounded below by 1/4. He identified two orbifolds with volume $\pi^{2} / 27$, and conjectured them to be the cusped complex hyperbolic 2-orbifolds of minimum volume. Extending a result for the real hyperbolic case [1], Fu, Li and Wang [5] obtained a lower bound for the volume of a complex hyperbolic orbifold, depending on dimension and the maximal order of torsion in the orbifold fundamental group.
4.4. Arithmetic Complex Hyperbolic Orbifolds. The smallest known complex hyperbolic 2-manifolds, closed or cusped, are arithmetically defined. Stover [21] proved that the orbifolds considered by Parker [16] are the smallest volume cusped arithmetic complex hyperbolic 2-orbifolds. In [4], Emery and Stover determine, for each dimension $n$, the smallest volume cusped arithmetic complex hyperbolic orbifold. It is shown that, as
$n$ varies, minimum volume among all cusped arithmetic complex hyperbolic orbifolds is realized in dimension 9. Smaller volume orbifolds have been found in the compact case. For example, Sauter [19] exhibited a closed arithmetic complex hyperbolic 2-orbifold with volume $\pi^{2} / 108$.

\section*{ACKNOWLEDGMENTS}

The authors are grateful to Dick Canary, Ben McReynolds and Matthew Stover for useful conversations.

\section*{References}
\begin{itemize}
\item[] [1] Ilesanmi Adeboye. Lower bounds for the volume of hypebolic $n$-orbifolds. Pacific Journal of Mathematics, 237(1):1-19, 2008.
\item[] [2] Ilesanmi Adeboye and Guofang Wei. On volumes of hyperbolic orbifolds. Algebraic \& Geometric Topology, 12(1):215-233, 2012.
\item[] [3] Donald I. Cartwright and Tim Steger. Enumeration of the 50 fake projective planes. C. R. Math. Acad. Sci. Paris, 348(1-2):11-13, 2010.
\item[] [4] Vincent Emery and Matthew Stover. Covolumes of nonuniform lattices in $P U(n, 1)$. To appear in American Journal of Mathematics.
\item[] [5] X. Fu, L. Li, and X. Wang. A lower bound for the volumes of complex hyperbolic orbifolds. Geometriae Dedicata, 155:21-30, 2011.
\item[] [6] S. Gallot, D. Hulin, and J. Lafontaine. Riemannian Geometry. Springer-Verlag, second edition, 1990.
\item[] [7] F. Gehring and G. Martin. Minimal co-volume hyperbolic lattices. i. the spherical points of a kleinian group. Annals of Mathematics. Second Series, 170(1):123-161, 2009.
\item[] [8] Robert Gilmore. Lie Groups, Lie Algebras, and Some of Their Applications. John Wiley \& Sons, 1974.
\item[] [9] William M. Goldman. Complex hyperbolic geometry. Oxford Mathematical Monographs. The Clarendon Press Oxford University Press, 1999.
\item[] [10] Sa'ar Hersonsky and Frédéric Paulin. On the volumes of complex hyperbolic manifolds. Duke Math. J., 84(3):719-737, 1996.
\item[] [11] Adolf Hurwitz. Über algebraische gebilde mit eindeutigen transformationen in sich. Mathematische Annalen, 41:403-442, 1893.
\item[] [12] Jun-Muk Hwang. On the volumes of complex hyperbolic manifolds with cusps. Internat. J. Math., 15(6):567-572, 2004.
\item[] [13] Jürgen Jost. Riemannian geometry and geometric analysis. Springer-Verlag, 1995.
\item[] [14] D. A. Každan and G. A. Margulis. A proof of Selberg's Conjecture. Mathematics of the U.S.S.R.-Sbornik, 4(1):147-152, 1968.
\item[] [15] Inkang Kim and Joonhyung Kim. On the volumes of canonical cusps of complex hyperbolic manifolds. J. Korean Math. Soc., 46(3):513-521, 2009.
\item[] [16] John R. Parker. On the volumes of cusped, complex hyperbolic manifolds and orbifolds. Duke Math. J., 94(3):433-464, 1998.
\item[] [17] Gopal Prasad and Sai-Kee Yeung. Fake projective planes. Invent. Math., 168(2):321-370, 2007.
\item[] [18] Gopal Prasad and Sai-Kee Yeung. Arithmetic fake projective spaces and arithmetic fake Grassmannians. Amer. J. Math., 131(2):379-407, 2009.
\item[] [19] John Kurt Sauter, Jr. Isomorphisms among monodromy groups and applications to lattices in PU(1, 2). Pacific J. Math., 146(2):331-384, 1990.
\item[] [20] Carl Ludwig Siegel. Some remarks on discontinuous groups. Ann. of Math. (2), 46:708-718, 1945.
\item[] [21] Matthew Stover. Volumes of Picard modular surfaces. Proc. Amer. Math. Soc., 139(9):3045-3056, 2011.
\item[] [22] Hsien-Chung Wang. Discrete nilpotent subgroups of Lie groups. Journal of Differential Geometry, 3:481-492, 1969.
\end{itemize}
\begin{itemize}
\item[] [23] Baohua Xie, Jieyan Wang, and Yueping Jiang. Balls in complex hyperbolic manifolds. arXiv:1203.3610v1, 2012.
\item[] [24] Sai-Kee Yeung. Classification of surfaces of general type with Euler number 3. to appear in J. Reine Angew. Math.
Math and Computer Science Department, Wesleyan University, Middletown, CT 06459
E-mail address: iadeboye@wesleyan.edu
Department of Mathematics, University of California, Santa Barbara, CA 93106
E-mail address: wei@math.ucsb.edu
\end{itemize}