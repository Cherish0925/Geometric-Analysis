---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 1709_05210v1.pdf
converter: mathpix
format: mmd
---

\title{
CLOSED ALMOST KÄHLER 4-MANIFOLDS OF CONSTANT NON-NEGATIVE HERMITIAN HOLOMORPHIC SECTIONAL CURVATURE ARE KÄHLER.
}

\author{
MEHDI LEJMI AND MARKUS UPMEIER
}

\begin{abstract}
We show that a closed almost Kähler 4-manifold of globally constant holomorphic sectional curvature $k \geq 0$ with respect to the canonical Hermitian connection is automatically Kähler. The same result holds for $k<0$ if we require in addition that the Ricci curvature is $J$-invariant. The proofs are based on the observation that such manifolds are self-dual, so that Chern-Weil theory implies useful integral formulas, which are then combined with results from Seiberg-Witten theory.
\end{abstract}

\section*{1. Introduction}

Dating back to the Goldberg conjecture [14], the question how the geometry of a closed almost Kähler 4-manifold can force the integrability of an almost complex structure has been considered by many authors. This conjecture has been verified for non-negative scalar curvature by Sekigawa [29]. Much else of what is known has now been subsumed by Apostolov-Armstrong-Drăghici in [1], where it is shown that the third Gray curvature condition is in fact sufficient. There are also strong results for the $*$-Ricci curvature [5], [10]. Assuming non-negative scalar curvature, the third Gray condition can be relaxed to the Ricci tensor being $J$-invariant [11].

Strengthening the Einstein condition, Blair [9] has shown that almost Kähler manifolds of constant sectional curvature are flat Kähler. For non-flat examples it is natural to consider instead the holomorphic sectional curvature, where one restricts the sectional curvature to $J$-invariant planes.

Restricting to a subclass of the Gray-Hervella classification, say almost Kähler, the problem of classifying manifolds of constant holomorphic sectional curvature was posed by Gray-Vanhecke [16]. A related problem is understanding when the notions of pointwise constant and globally constant holomorphic sectional curvature agree. This holds for nearly Kähler manifolds [15], but there are non-compact counterexamples in the almost Kähler case [28]. Moreover, for almost Kähler manifolds the classification problem so far has remained inconclusive (see also [12, 19]).

The purpose of this paper is to prove such a classification result for the Hermitian holomorphic sectional curvature instead of the Riemannian one. We obtain optimal results for non-negative curvature, while in the negative case we need to impose the 'natural' condition of the Ricci tensor being $J$-invariant.

\footnotetext{
The authors are thankful to Vestislav Apostolov for his comments. The first author was supported in part by a PSC-CUNY award \#60053-00 48, jointly funded by The Professional Staff Congress and The City University of New York. The first author thanks all the members of the Math Department of University of Augsburg for their warm hospitality during his stay in July 2017. The second author was partially funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) - UP 85/2-1, UP 85/3-1.
}

Note that constant Hermitian holomorphic sectional curvature does not obviously imply the Einstein condition, nor that any of the scalar curvatures are constant. Assuming this, we also obtain a partial result in Corollary 5.3.
1.1. Overview of results. Let $(M, g, J, F)$ be an almost Hermitian 4-manifold. Define the (first canonical) Hermitian connection by
$$\nabla_{X} Y:=D_{X}^{g} Y-\frac{1}{2} J\left(D_{X}^{g} J\right) Y .$$
From its curvature we derive the Hermitian holomorphic sectional curvature
$$H(X):=-R_{X, J X, X, J X}^{\nabla},$$
a function on the unit tangent bundle. We now state the main results of this paper.
Theorem 1.1. Let $M$ be a closed almost Kähler 4-manifold of globally constant Hermitian holomorphic sectional curvature $k \geq 0$.

Then $M$ is Kähler-Einstein, holomorphically isometric to:
$(k>0): \mathbb{C} P^{2}$ with the Fubini-Study metric.
$(k=0)$ : a complex torus or a hyperelliptic curve with the Ricci-flat Kähler metric.
Recall here that a hyperelliptic curve is a quotient of a complex torus by a finite free group action. This classification is well-known for Kähler manifolds (see [20, Theorems 7.8, 7.9] and [17, 18] in the simply-connected case and [3, Theorem 2] in general). The main goal of this paper is to show that $J$ is automatically integrable.

In case $k<0$ we shall prove the following weaker result:
Theorem 1.2. Let $M$ be a closed almost Kähler 4-manifold of pointwise constant Hermitian holomorphic sectional curvature $k<0$. Assume also that the Ricci tensor is $J$-invariant. Then $M$ is Kähler-Einstein, holomorphically isometric to a compact quotient of the complex hyperbolic ball $\mathbb{B}^{4}$ with the Bergman metric.

The proofs rely on the following pointwise result of independent interest, in which $M$ may be non-compact:

Theorem 1.3. Let $M$ be an almost Hermitian 4-manifold. The holomorphic sectional curvature with respect to the Hermitian connection is constant $k$ at the point $p \in M$ if and only if at that point
\begin{itemize}
\item[i)] $W^{-}=0$,
\item[ii)] $* \rho=r$.
\end{itemize}

Condition ii) may also be expressed using the (Riemannian) Ricci tensor, see Proposition 4.2 (we refer to [7] in the Hermitian case). Hence in proving Theorems 1.1, 1.2 we may restrict attention to self-dual manifolds, meaning $W^{-}=0$. Their classification is an old and in general still open problem, but under additional assumptions many results have been obtained. See [2, 3, 8, 22] for results and further overview. Our main theorems can also be regarded in this way.
1.2. Strategy of proof. The first step is to reformulate constant Hermitian holomorphic sectional curvature in terms of the Riemannian curvature tensor (Theorem 1.3). This an algebraic argument at a point, based on the decomposition of the Riemannian curvature tensor in dimension 4 and the explicit nature of the gauge potential in (1). In some sense, the assumption of constant curvature is played off
against the symmetries of the Riemannian curvature tensor. This is carried out in Section 3, after having recalled some preliminaries in the next section.

The next step is then in Section 4 to improve in the almost Kähler case our understanding of the Hermitian curvature tensor. It is remarkable that in (29) we obtain information on the full curvature tensor, even though our assumptions depend only upon its (1,1)-part.

Up to this point our arguments are mostly algebraic. To proceed, we must exploit consequences of the differential Bianchi identity. Thus in Section 5 we formulate the index theorems for the signature and the Euler characteristic using Chern-Weil theory. Applied to the Levi-Civita and the Hermitian connection, we obtain further information (40), (41), (42).

The formulas are then used in Section 6 to show Kählerness under further topological restrictions. Finally, combined with deep results from Seiberg-Witten theory, these results imply Theorem 1.1 in the case $k \geq 0$.

Theorem $1.2(k<0)$ follows by combining our results with formulas for the Bach tensor obtained in [4]. These formulas require the Ricci tensor to be $J$-invariant. It is well possible that this additional assumption in Theorem 1.2 may be removed.

\section*{2. Preliminaries}
2.1. Conventions. Throughout let $(M, J, g, F)$ be an almost Hermitian 4-manifold. Thus $J: T M \rightarrow T M$ is an almost complex structure, $g$ is a Riemannian metric for which $J$ is orthogonal, and $F=g(J \cdot, \cdot)$. Later we will also assume $d F=0$ so that we have an almost Kähler structure. Recall that an almost Hermitian manifold is Kähler precisely when $J$ is parallel for the Levi-Civita connection $D^{g} J=0$.

Let $\left(z_{1}, z_{2}\right)$ be a local orthonormal frame of $T^{1,0} M$ for the induced Hermitian metric $h(Z, W)=g_{\mathbb{C}}(Z, \bar{W})$ on $T M \otimes \mathbb{C}=T^{1,0} M \oplus T^{0,1} M$ split in the usual fashion. Using the dual frame, the fundamental form is $F=i\left(z^{1} \bar{z}^{\overline{1}}+z^{2} \bar{z}^{\overline{2}}\right)$. All tensors are extended complex linearly and we adopt the summation convention.
2.2. Two-forms on 4-manifolds. The Hodge operator decomposes the bundle of two-forms into the self-dual and anti-self-dual parts
$$\Lambda^{2}=\Lambda^{+} \oplus \Lambda^{-} .$$
For the structure group $U(2) \subset S O(4)$ we may split further
$$\Lambda^{+} \otimes \mathbb{C}=\Lambda^{2,0} \oplus \Lambda^{0,2} \oplus \mathbb{C} \cdot F, \quad \quad \Lambda^{-} \otimes \mathbb{C}=\Lambda_{0}^{1,1}$$
Here $\Lambda_{0}^{1,1}$ stands for complex $(1,1)$-forms pointwise orthogonal to $F$.
2.3. Gauge potential. The gauge potential $A=\nabla-D^{g}$ of the canonical connection (1) with respect to the Levi-Civita connection $D^{g}$ is complex anti-linear
$$A_{X} \circ J=-J \circ A_{X} .$$
In dimension four, the almost Kähler condition is equivalent to
$$A_{J X}=-J \circ A_{X} .$$
Note that $M$ is Kähler $\Longleftrightarrow A=0$.
2.4. Curvature decomposition. Regard the Hermitian curvature (and similarly the Riemannian curvature) as a bilinear form on $\Lambda^{2}$, grouping $X Y$ and $Z W$, by
$$R_{X Y Z W}^{\nabla}:=g\left(\left[\nabla_{X}, \nabla_{Y}\right] Z-\nabla_{[X, Y]} Z, W\right) .$$
When we decompose $\Lambda^{2}$ into direct summands, we get a corresponding decomposition of $R^{\nabla}$ into a matrix of bilinear forms, where the first entry corresponds to the rows. The representing matrix of a bilinear form with respect to a basis (one-dimensional summands) will be indicated by ' $\equiv$ '.

All of the algebraic properties of the Riemannian curvature tensor $R^{g}$ are summarized in the following representation with respect to (3) and (4), see [5, 8]:
$$\begin{aligned}
-R^{g} & =\left(\begin{array}{c|c}
\Lambda^{+} & \Lambda^{-} \\
W^{+}+\frac{s_{g}}{12} g & R_{0} \\
\hline R_{0}^{T} & W^{-}+\frac{s_{g}}{12} g
\end{array}\right) \\
& =\left(\begin{array}{cc|c}
\mathbb{C} F & \Lambda^{2,0} \oplus \Lambda^{0,2} & \Lambda_{0}^{1,1} \\
d \cdot g & W_{F}^{+} & R_{F} \\
\left(W_{F}^{+}\right)^{T} & W_{00}^{+}+\frac{c}{2} g & R_{00} \\
\hline R_{F}^{T} & R_{00}^{T} & W^{-}+\frac{s_{g}}{12} g
\end{array}\right)
\end{aligned}$$
Here $W^{ \pm}$are the Weyl curvatures, trace-free symmetric bilinear forms on $\Lambda^{ \pm}$and $s_{g}$ denotes the Riemannian scalar curvature. The $*$-scalar curvature is
$$s_{*}:=4 d, \quad \frac{s_{g}}{4}=c+d .$$
Moreover $R_{0}: \Lambda^{+} \otimes \Lambda^{-} \rightarrow \mathbb{R}$ corresponds to the trace-free Riemannian Ricci tensor $r_{0}$, namely $R_{0}(\cdot)=\frac{1}{2}\left\{r_{0}, \cdot\right\}$ is the anti-commutator, see [13, (A.1.8)]. Finally $R_{0}^{T}(x, y):=R_{0}(y, x)$, and $R_{00}, R_{F}$ denote further restrictions in the first argument. We take the tensorial norm for bilinear forms, even when they are symmetric.
2.5. Ricci forms. Having torsion, the curvature tensor of the canonical connection has fewer symmetries than the Riemannian one; for example the algebraic Bianchi identity no longer holds. By contracting indices we now obtain two Ricci forms
$$\begin{aligned}
& \rho:=i R_{\alpha \bar{\beta} \gamma}^{\gamma} z^{\alpha} \wedge \bar{z}^{\bar{\beta}}, \\
& r:=i R_{\gamma}^{\nabla}{ }_{\gamma \bar{\mu}} z^{\lambda} \wedge \bar{z}^{\bar{\mu}} .
\end{aligned}$$
The Chern and Hermitian scalar curvatures are obtained by a further trace
$$s_{C}:=\Lambda(\rho)=\Lambda(r)=R^{\nabla}{ }_{\alpha}{ }^{\alpha}{ }_{\gamma}{ }^{\gamma}, \quad s_{H}:=2 s_{C} .$$
In the Kähler case, the canonical and the Levi-Civita connection agree so that both forms in (10) are equal to the usual Ricci form.
2.6. Holomorphic sectional curvature. For $Z \in T^{1,0} M$ the holomorphic sectional curvature is defined from the (1,1)-part of the curvature as
$$H(Z)=\frac{R_{Z, \bar{Z}, Z, \bar{Z}}^{\nabla}}{h(Z, Z) h(Z, Z)} .$$

The holomorphic sectional curvature is constant at the point $p \in M$ if (12) is a constant $k(p)$ for all $Z \in T_{p}^{1,0} M$. We say it is pointwise constant if $H$ is constant at each point of $M$. If the constant $k$ is the same at every point $p \in M$ we speak of globally constant holomorphic sectional curvature.

Note that the Hermitian connection is always understood.

\section*{3. Relation to Self-dual Manifolds}

In this section we will prove Theorem 1.3.
3.1. Preparatory lemmas. Being the complexification of a real tensor, the (1,1)part of the curvature has the following form in the basis $\left(z_{1 \overline{1}}, z_{1 \overline{2}}, z_{2 \overline{1}}, z_{2 \overline{2}}\right)$ :
$$\left.R^{\nabla}\right|_{\Lambda^{1,1} \otimes \Lambda^{1,1}} \equiv\left(\begin{array}{cccc}
\bar{k} & \bar{a} & a & w \\
\bar{a}^{\prime} & \bar{x} & \bar{v} & \bar{b} \\
a^{\prime} & v & x & b \\
u & \bar{b}^{\prime} & b^{\prime} & l
\end{array}\right), \quad k, l, u, w \in \mathbb{R} .$$

We first show that the (1, 1)-part of $R^{\nabla}$ is automatically restricted further.
Lemma 3.1. Let $M$ be an almost Hermitian 4-manifold. With respect to the decomposition $\Lambda^{1,1}=\mathbb{C} F \oplus \Lambda_{0}^{1,1}$ we have
$$\left.R^{\nabla}\right|_{\Lambda^{1,1} \otimes \Lambda^{1,1}}=-\left(\begin{array}{cc}
\mathbb{C} F & \Lambda_{0}^{1,1} \\
\frac{s_{C}}{2} g & R_{F} \\
R_{F}^{T}+\beta_{0} & W^{-}+\frac{s_{g}}{12} g
\end{array}\right)$$
for some $\beta_{0}: \Lambda_{0}^{1,1} \otimes \mathbb{C} F \rightarrow \mathbb{C}$. Moreover $a+b=a^{\prime}+b^{\prime}$ and $v=\frac{s_{g}}{12}$ in (13).
Proof. By direct calculation (or see [8, p. 25])
$$R_{X Y Z W}^{\nabla}=R_{X Y Z W}^{g}+\underbrace{g\left(\left(\nabla_{X} A_{Y}-\nabla_{Y} A_{X}-A_{[X, Y]}\right) Z, W\right)}_{\alpha:=}-\underbrace{g\left(\left[A_{X}, A_{Y}\right] Z, W\right)}_{\beta:=} .$$
By (5), $\alpha \in \Lambda^{2} \otimes \Lambda^{2,0+0,2}$, so only $\beta$ will contribute to the restriction of $R^{\nabla}$. Since $\left[A_{X}, A_{Y}\right]$ is complex-linear, $\beta \in \Lambda^{2} \otimes \Lambda^{1,1}$. On $\Lambda^{1,1}$ consider the orthonormal basis
$$\left(\frac{i}{\sqrt{2}}\left(z_{1 \overline{1}}+z_{2 \overline{2}}\right), z_{1 \overline{2}}, z_{2 \overline{1}}, \frac{i}{\sqrt{2}}\left(z_{1 \overline{1}}-z_{2 \overline{2}}\right)\right) .$$
In dimension 4, $\beta$ is in fact restricted to $\Lambda^{2} \otimes \mathbb{C} F$. Indeed, the explicit formula
$$\beta\left(X, Y, z_{\alpha}, \bar{z}_{\bar{\beta}}\right)=A_{[X \alpha \gamma} A_{Y] \bar{\beta}}^{\gamma}$$
shows $\beta_{X Y 1 \overline{2}}=\beta_{X Y 2 \overline{1}}=\beta_{X Y 1 \overline{1}}-\beta_{X Y 2 \overline{2}}=0$ (here '[]' denotes anti-symmetrization):
$$\left.\beta\right|_{\Lambda^{1,1} \otimes \Lambda^{1,1}}=\left(\begin{array}{cc}
\mathbb{C} F & \Lambda_{0}^{1,1} \\
\tilde{\beta} \cdot g & 0 \\
\beta_{0} & 0
\end{array}\right) .$$
Complexifying and restricting to $\Lambda^{1,1} \otimes \Lambda^{1,1}$ we hence have
$$R^{\nabla}=R^{g}+\alpha-\beta=-\left(\begin{array}{cc}
\mathbb{C} F & \Lambda_{0}^{1,1} \\
d \cdot g_{\mathbb{C}} & R_{F} \\
R_{F}^{T} & W^{-}+\frac{s_{g}}{12} g_{\mathbb{C}}
\end{array}\right)+0-\left(\begin{array}{cc}
\mathbb{C} F & \Lambda_{0}^{1,1} \\
\tilde{\beta} \cdot g_{\mathbb{C}} & 0 \\
\beta_{0} & 0
\end{array}\right) .$$
Note that the upper left corner of (14) is $-s_{C} / 2$ by definition (11). A change of basis shows that the bilinear form (13) is represented in the basis (15) by
$$\left.R^{\nabla}\right|_{\Lambda^{1,1} \otimes \Lambda^{1,1}} \equiv\left(\begin{array}{cccc}
\frac{-k-l-u-w}{2} & \frac{i}{\sqrt{2}}\left(\overline{a+b^{\prime}}\right) & \frac{i}{\sqrt{2}}\left(a+b^{\prime}\right) & \frac{-k+l-u+w}{2} \\
\frac{i}{\sqrt{2}}\left(\overline{b+a^{\prime}}\right) & \bar{x} & \bar{v} & \frac{i}{\sqrt{2}}\left(a^{\prime}-b\right) \\
\frac{i}{\sqrt{2}}\left(b+a^{\prime}\right) & v & x & \frac{i}{\sqrt{2}}\left(a^{\prime}-b\right) \\
\frac{-k+l+u-w}{2} & \frac{i}{\sqrt{2}}\left(\overline{a-b^{\prime}}\right) & \frac{i}{\sqrt{2}}\left(a-b^{\prime}\right) & \frac{-k-l+u+w}{2}
\end{array}\right) .$$

In this basis (15) the inner product on 2-forms has the matrix
$$g_{\mathbb{C}} \equiv\left(\begin{array}{llll}
1 & & & \\
& & -1 & \\
& -1 & & \\
& & & 1
\end{array}\right),$$
so by comparing (17) and (18) and using that $W^{-}+\frac{s_{g}}{12} g$ is symmetric we get
$$a+b=a^{\prime}+b^{\prime}, \quad v=\frac{s_{g}}{12} \in \mathbb{R}$$
For later use we note that in this basis the condition $W^{-}=0$ means that the lower right 3 × 3-submatrix of (18) reduces to
$$\left(\begin{array}{lll} 
& \frac{s_{g}}{12} & \\
\frac{s_{g}}{12} & & \\
& & -\frac{s_{g}}{12}
\end{array}\right) .$$
In other words, it means $x=0, a=b^{\prime}, u+2 v+w=k+l$. \(\square\)

Lemma 3.2. The holomorphic sectional curvature is constant $k$ at a point if and only if (13) reduces at that point to
$$\left.R^{\nabla}\right|_{\Lambda^{1,1} \otimes \Lambda^{1,1}} \equiv\left(\begin{array}{cccc}
k & \bar{a} & a & w \\
-\bar{a} & 0 & \bar{v} & \bar{b} \\
-a & v & 0 & b \\
u & -\bar{b} & -b & k
\end{array}\right) \quad \text { with } \quad u+v+\bar{v}+w=2 k .$$
Proof. Let $Z=x z_{1}+y z_{2}$ for arbitrary $x, y \in \mathbb{C}$, and expand both sides of the equation $k \cdot h(Z, Z)^{2}=R^{\nabla}(Z, \bar{Z}, Z, \bar{Z})$. We have
$$k \cdot h(Z, Z)^{2}=k|x|^{4}+2 k|x|^{2}|y|^{2}+k|y|^{4}$$
while for the right hand side
$$\begin{aligned}
& |x|^{4} R_{z_{1} \bar{z}_{1} z_{1} \bar{z}_{1}}+|y|^{4} R_{z_{2} \bar{z}_{2} z_{2} \bar{z}_{2}} \\
& +|x|^{2}|y|^{2}\left(R_{z_{1} \bar{z}_{1} z_{2} \bar{z}_{2}}+R_{z_{2} \bar{z}_{2} z_{1} \bar{z}_{1}}+R_{z_{2} \bar{z}_{1} z_{1} \bar{z}_{2}}+R_{z_{1} \bar{z}_{2} z_{2} \bar{z}_{1}}\right) \\
& +x^{2} \bar{y}^{2} R_{z_{1} \bar{z}_{2} z_{1} \bar{z}_{2}}+\bar{x}^{2} y^{2} R_{z_{2} \bar{z}_{1} z_{2} \bar{z}_{1}} \\
& +x^{2} \bar{x} \bar{y}\left(R_{z_{1} \bar{z}_{1} z_{1} \bar{z}_{2}}+R_{z_{1} \bar{z}_{2} z_{1} \bar{z}_{1}}\right) \\
& +\bar{x}^{2} x y\left(R_{z_{2} \bar{z}_{1} z_{1} \bar{z}_{1}}+R_{z_{1} \bar{z}_{1} z_{2} \bar{z}_{1}}\right) \\
& +\bar{x} y^{2} \bar{y}\left(R_{z_{2} \bar{z}_{2} z_{2} \bar{z}_{1}}+R_{z_{2} \bar{z}_{1} z_{2} \bar{z}_{2}}\right) \\
& +x \bar{y}^{2} y\left(R_{z_{2} \bar{z}_{2} z_{1} \bar{z}_{2}}+R_{z_{1} \bar{z}_{2} z_{2} \bar{z}_{2}}\right)
\end{aligned}$$
Since $x, y \in \mathbb{C}$ are arbitrary, this an equality between polynomials in the variables $x, \bar{x}, y, \bar{y}$. For them to agree, all coefficients must be equal. \(\square\)

Remark 3.3. The above is a simplified proof of a theorem of Balas [6] for Hermitian manifolds.
3.2. Proof of Theorem 1.3. First note that by Lemma 3.1 we automatically have $a+b=a^{\prime}+b^{\prime}$ and $v=\frac{s_{g}}{12} \in \mathbb{R}$ in (13).

Lemma 3.2 shows that $H$ is constant $k$ at a point if and only if
$$x=0, \quad a^{\prime}=-a, \quad a=-b, \quad k=l, \quad u+2 v+w=2 k .$$
On the other hand, by (18) and the following discussion, self-duality means
$$x=0, \quad a=b^{\prime}, \quad u+2 v+w=k+l .$$
From (13) we read off
$$\begin{aligned}
& \rho=i(k+w) z^{1 \overline{1}}+i \overline{\left(a^{\prime}+b\right)} z^{1 \overline{2}}+i\left(a^{\prime}+b\right) z^{2 \overline{1}}+i(u+l) z^{2 \overline{2}} \\
& r=i(k+u) z^{1 \overline{1}}+i \overline{\left(a+b^{\prime}\right)} z^{1 \overline{2}}+i\left(a+b^{\prime}\right) z^{2 \overline{1}}+i(w+l) z^{2 \overline{2}}
\end{aligned}$$
Therefore $* \rho=r$ means
$$k=l, \quad a^{\prime}+b=-\left(a+b^{\prime}\right) .$$
Under the general assumption $a+b=a^{\prime}+b^{\prime}$ and $v \in \mathbb{R}$ it is easy to verify that (20) is equivalent to (21) with (22). \(\square\)

\section*{4. Sharper results for almost Kähler manifolds}

We now obtain more information on the terms in
$$R^{\nabla}=R^{g}+\alpha-\beta$$ \(\square\)

Lemma 4.1. Let $M$ be an almost Kähler 4-manifold. Then
$$\tilde{\beta}=-\frac{1}{2}|A|^{2}, \quad\left\|\beta_{0}\right\|^{2}=\frac{1}{4}|A|^{4} .$$

Here we use the convention $|A|^{2}=\frac{1}{2} \sum_{i=1}^{4} \operatorname{tr}\left(A_{e_{i}}^{T} A_{e_{i}}\right)$.
Proof. More precisely, from (6) we have $\beta \in \Lambda^{1,1} \otimes \mathbb{C} \cdot F$. Using (16) one sees
$$\beta=\left(\begin{array}{cc|c}
\mathbb{C} F & \Lambda^{2,0} \oplus \Lambda^{0,2} & \Lambda_{0}^{1,1} \\
\tilde{\beta} & 0 & 0 \\
0 & 0 & 0 \\
\hline \beta_{0} & 0 & 0
\end{array}\right)$$
where
$$\tilde{\beta}=-\left|A_{112}\right|^{2}-\left|A_{212}\right|^{2}, \quad \beta_{0}=\left(\begin{array}{c}
i \sqrt{2} \cdot A_{112} \overline{A_{212}} \\
i \sqrt{2} \cdot A_{212} \overline{A_{112}} \\
\left|A_{212}\right|^{2}-\left|A_{112}\right|^{2}
\end{array}\right) .$$
In the upper left corner of (17) we recover the well-known formula ([4], [13, (9.4.5)])
$$\frac{s_{*}-s_{H}}{4}=\frac{1}{2}|A|^{2} .$$ \(\square\)

Proposition 4.2. Let $M$ be a self-dual almost Hermitian 4-manifold. Then $M$ has constant holomorphic sectional curvature at $p \in M$ precisely when
$$R_{F}=-\frac{1}{2} \beta_{0}^{T} .$$
at that point. In particular, when $M$ is almost Kähler and $M$ has pointwise constant holomorphic sectional curvature, then: $M$ is Kähler $\Longleftrightarrow R_{F}=0$.

Proof. Putting the self-duality condition (21) from the proof of Theorem 1.3 into (18) we get representative matrices
$$-R_{F} \equiv(\sqrt{2} i \bar{a}, \sqrt{2} i a, v+w-k), \quad R_{F}^{T}+\beta_{0} \equiv-\left(\begin{array}{c}
\sqrt{2} i \bar{b} \\
\sqrt{2} i b \\
\frac{u+v-k}{2}
\end{array}\right)$$
with respect to the orthonormal basis (15). Hence a self-dual manifold has constant holomorphic sectional curvature (20) precisely when (27) holds.

In the almost Kähler case we may use (24) to get
$$\left\|R_{F}\right\|^{2}=\frac{1}{4}\left\|\beta_{0}\right\|^{2}=\frac{|A|^{4}}{16} .$$ \(\square\)

\subsection*{4.2. Constant holomorphic sectional curvature.}

Proposition 4.3. Let $M$ be almost Kähler of constant holomorphic sectional curvature $k$. Then we have
$$-R^{\nabla}=\left(\begin{array}{cc|c}
\mathbb{C} F & \Lambda^{2,0} \oplus \Lambda^{0,2} & \Lambda_{0}^{1,1} \\
\frac{s_{C}}{2} g & 0 & R_{F} \\
W_{F}^{+} & 0 & R_{00} \\
\hline-R_{F}^{T} & 0 & \frac{s_{g}}{12} g
\end{array}\right)$$
Proof. Put all the facts $\alpha \in \Lambda^{2} \otimes \Lambda^{2,0+0,2}, R^{\nabla} \in \Lambda^{2} \otimes \Lambda^{1,1}$, and (25), (27) into the formula $R^{\nabla}=R^{g}+\alpha-\beta$. \(\square\)

We now collect some formulas that will be useful. For these, assume that $M$ is almost Kähler and has pointwise constant holomorphic sectional curvature $k$.

Comparing the upper left corners of (18) and (29) and then using (20) we see
$$s_{C}=4 k-2 v .$$
Recall also
$$s_{g}=12 v .$$
Since $M$ is almost Kähler we have for the $*$-scalar curvature [13, (9.4.5)]
$$s_{*}=4 s_{C}-s_{g}=16 k-20 v .$$
Moreover (27) can now be written
$$\left|R_{F}\right|^{2}=\frac{1}{4}\left(\frac{s_{*}-s_{H}}{4}\right)^{2}=(k-2 v)^{2}$$

Putting these formulas into (26) shows:
Lemma 4.4. Let $M$ be almost Kähler of pointwise constant holomorphic sectional curvature $k$. We then have $v \leq \frac{k}{2}$ with equality if and only if $M$ is Kähler. \(\square\)

The formulas also show that when $M$ has globally constant holomorphic sectional curvature, the constancy of any of $s_{g}, s_{*}, s_{C}$ is equivalent to that of $v$.

\section*{5. Integral formulas}

Having understood the pointwise (algebraic) implications of constant holomorphic sectional curvature, we now turn to properties that do not hold for general algebraic curvature tensors. Thus we formulate the consequences of Chern-Weil theory, which stem ultimately from the differential Bianchi identity.

We will assume in this section that $M$ is an almost Kähler 4-manifold of pointwise constant holomorphic sectional curvature, but generalizations are possible.
5.1. Chern-Weil theory. Given an arbitrary metric connection ∇ on $T M$ and a polynomial $P$ on $\mathfrak{s o}(4)$, invariant under the adjoint action of $S O(4)$, one obtains a differential form $P\left(R^{\nabla}\right)$ by substituting the indeterminants by the curvature $R^{\nabla}: \Lambda^{2} \rightarrow \mathfrak{s o}(T M)$. The upshot of Chern-Weil theory (see for example [26]) is that $P\left(R^{\nabla}\right)$ defines a closed form whose cohomology class is independent of ∇ . In particular, the integral over $M$ remains the same for all connections.

In the 4-dimensional case, it suffices to consider the Pontrjagin and Pfaffian polynomials. To express these conveniently, use the metric to identify $\mathfrak{s o}(T M) \cong \Lambda^{2}$ and decompose as above
$$-R^{\nabla}=\left(\begin{array}{c|c}
\Lambda^{+} & \Lambda^{-} \\
R_{s d}^{+} & R_{a s d}^{+} \\
\hline R_{s d}^{-} & R_{a s d}^{-}
\end{array}\right) .$$
Then
$$\begin{aligned}
& p_{1}\left(R^{\nabla}\right)=\frac{1}{4 \pi^{2}}\left(\left\|R_{s d}^{+}\right\|^{2}+\left\|R_{s d}^{-}\right\|^{2}-\left\|R_{a s d}^{+}\right\|^{2}-\left\|R_{a s d}^{-}\right\|^{2}\right) \text { vol, } \\
& \operatorname{Pf}\left(R^{\nabla}\right)=\frac{1}{8 \pi^{2}}\left(\left\|R_{s d}^{+}\right\|^{2}-\left\|R_{s d}^{-}\right\|^{2}-\left\|R_{a s d}^{+}\right\|^{2}+\left\|R_{a s d}^{-}\right\|^{2}\right) \text { vol, }
\end{aligned}$$
where the norm is induced by the usual inner product $\operatorname{tr}\left(f^{*} g\right)$ on $\operatorname{End}\left(\Lambda^{2}\right)$. For the Levi-Civita connection we evaluate (34) using (8), $W^{-}=0$, and $\|I\|^{2}=3$ :
$$\begin{aligned}
p_{1}\left(D^{g}\right) & =\frac{1}{4 \pi^{2}}\left(\left\|W^{+}+\frac{s_{g}}{12} I\right\|^{2}+\left\|R_{0}^{*}\right\|^{2}-\left\|R_{0}\right\|^{2}-\left\|W^{-}+\frac{s_{g}}{12} I\right\|^{2}\right) \operatorname{vol}_{g} \\
& =\frac{1}{4 \pi^{2}}\left(\left\|W^{+}\right\|^{2}-\left\|W^{-}\right\|^{2}\right) \operatorname{vol}_{g} \\
& =\frac{1}{4 \pi^{2}}\left\|W^{+}\right\|^{2} \operatorname{vol}_{g}
\end{aligned}$$
and ${ }^{1}$
$$\begin{aligned}
\operatorname{Pf}\left(D^{g}\right) & =\frac{1}{8 \pi^{2}}\left(\left\|W^{+}+\frac{s_{g}}{12} I\right\|^{2}+\left\|W^{-}+\frac{s_{g}}{12} I\right\|^{2}-\left\|R_{0}^{*}\right\|^{2}-\left\|R_{0}\right\|^{2}\right) \operatorname{vol}_{g} \\
& =\frac{1}{8 \pi^{2}}\left(\left\|W^{+}\right\|^{2}+\left\|W^{-}\right\|^{2}+\frac{1}{24} s_{g}^{2}-2\left\|R_{0}\right\|^{2}\right) \operatorname{vol}_{g} \\
& =\frac{1}{8 \pi^{2}}\left(\left\|W^{+}\right\|^{2}+\frac{1}{24} s_{g}^{2}-2\left\|R_{0}\right\|^{2}\right) \operatorname{vol}_{g}
\end{aligned}$$

\footnotetext{
${ }^{1}$ Traditionally one writes $2\left\|R_{0}\right\|^{2}=\frac{1}{2}\left\|r_{0}\right\|^{2}$ in terms of the Ricci tensor $r_{0}$.
}

Similarly, for the Hermitian connection we evaluate (34) using (29):
$$\begin{aligned}
& p_{1}(\nabla)=\frac{1}{4 \pi^{2}}\left(\frac{s_{C}^{2}}{4}+\left\|W_{F}^{+}\right\|^{2}+\left\|R_{00}\right\|^{2}-\frac{s_{g}^{2}}{48}\right) \operatorname{vol}_{g} \\
& \operatorname{Pf}(\nabla)=\frac{1}{8 \pi^{2}}\left(\frac{s_{C}^{2}}{4}+\left\|W_{F}^{+}\right\|^{2}+\frac{s_{g}^{2}}{48}-2\left\|R_{F}\right\|^{2}-\left\|R_{00}\right\|^{2}\right) \operatorname{vol}_{g}
\end{aligned}$$
5.2. Index theorems. The pre-factors in (34) are chosen so that for the signature and Euler characteristic the classical index theorems hold (see [26]):
$$\begin{aligned}
\sigma & =\frac{1}{3} \int_{M} p_{1}\left(R^{\nabla}\right) \\
\chi & =\int_{M} \operatorname{Pf}\left(R^{\nabla}\right)
\end{aligned}$$

This gives us two expressions for the signature and for the Euler characteristic (39). Equating these leads to the same conclusion in both cases:

Proposition 5.1. Let $M$ be a closed almost Kähler 4-manifold of pointwise constant holomorphic sectional curvature $k$. Then (we omit the volume form)
$$\int_{M}\left|W_{F}^{+}\right|^{2}+\left|W_{00}^{+}\right|^{2}+4(5 k-7 v)(k-2 v)=\int_{M}\left|R_{00}\right|^{2}$$
Proof. By the above remarks
$$\int_{M} p_{1}\left(D^{g}\right)=\int_{M} p_{1}(\nabla)$$
and we insert (35), (37). Then using (8) we get
$$\left\|W^{+}\right\|^{2}=2\left\|W_{F}^{+}\right\|^{2}+\left\|W_{00}^{+}\right\|^{2}+\frac{1}{6}\left(3 s_{C}-s_{g}\right)^{2} .$$
since in the almost Kähler case $s_{*}=4 d, \frac{s_{g}}{4}=c+d$, and $\frac{s_{g}+s_{*}}{2}=2 s_{C}$. Finally insert (30)-(32) to obtain the conclusion (40). Doing the same computation for the Pfaffian, use $\left\|R_{0}\right\|^{2}=\left\|R_{00}\right\|^{2}+\left\|R_{F}\right\|^{2}$. This leads to the same formula (40). \(\square\)

Putting (40) and (30)-(33) into (39) gives the following:
Proposition 5.2. Let $M$ be a closed almost Kähler 4-manifold of pointwise constant holomorphic sectional curvature $k$. Then
$$\begin{aligned}
\chi & =\frac{-1}{8 \pi^{2}} \int_{M}\left|W_{00}^{+}\right|^{2}+\left(60 v^{2}-72 k v+18 k^{2}\right) \\
\frac{3}{2} \sigma & =\frac{1}{8 \pi^{2}} \int_{M} 2\left|W_{F}^{+}\right|^{2}+\left|W_{00}^{+}\right|^{2}+6(2 k-3 v)^{2} \geq 0
\end{aligned}$$

Combined with [5, Lemma 3] we conclude:
Corollary 5.3. Let $M$ be closed almost Kähler of globally constant holomorphic sectional curvature $k$. Suppose $M$ is simply connected (or, more generally, that $5 \chi+6 \sigma \neq 0$ ) and that any of $s_{g}, s_{*}, s_{C}$ is constant. Then $M$ is Kähler.

Proof. Suppose by contradiction that $J$ is not integrable, so that $v<\frac{k}{2}$ at some point, by Lemma 4.4. Then (28) and (33) show that $|N|^{2}$ is a non-zero constant. Hence by [5, Lemma 3] we must have
$$5 \chi+6 \sigma=0 .$$
This contradicts $\chi=2+b_{2}>0$ and $\sigma \geq 0$ from (42). \(\square\)

\section*{6. Proof of Main Theorems}
6.1. Intermediate results. Before proving Theorem 1.1 we need to establish two preliminary results that give Kählerness under topological restrictions.

Proposition 6.1. Let $M$ be closed almost Kähler 4-manifold of pointwise constant holomorphic sectional curvature $k$. Suppose $\sigma=0$ for the signature.

Then $k=0$ and $M$ is Kähler, with a Ricci-flat metric.
Proof. By (42), $\sigma=0$ implies $W_{F}^{+}=0, W_{00}^{+}=0$, and $v=\frac{2}{3} k$. Putting this into (40) shows $R_{00}=0$ and $k=0$, since the left hand side reduces to $-\frac{4}{9} k^{2} \cdot \operatorname{Vol}(M)$ and the right hand side is non-negative. Hence integrability follows from Lemma 4.4

Then from (33) we also get $R_{F}=0$, so $R_{0}=R_{00}+R_{F}=0$. Hence the metric is Ricci-flat. \(\square\)

We next show a 'reverse' Bogomolov-Miyaoka-Yau inequality.
Proposition 6.2. If $M$ is closed almost Kähler of globally constant holomorphic sectional curvature $k \geq 0$ then
$$3 \sigma \geq \chi$$
Equality holds if and only if $M$ is Kähler (even Kähler-Einstein).
Proof. Estimate (43) follows by combining (41), (42) to get
$$3 \sigma-\chi=\frac{1}{8 \pi^{2}} \int_{M}\left|W_{F}^{+}\right|^{2}+3\left|R_{00}\right|^{2}+6 k(k-2 v)$$
and the fact $v \leq \frac{k}{2}$. Putting $3 \sigma=\chi$ into (44) shows
$$0=\int_{M}\left|W_{F}^{+}\right|^{2}+3\left|R_{00}\right|^{2}+6 k(k-2 v)$$
which is the sum of three non-negative terms. Hence all summands vanish. When $k \neq 0$ is a global non-zero constant we get
$$\int_{M}(k-2 v) \mathrm{vol}=0 .$$
Since $k-2 v \geq 0$ this means $k=2 v$ everywhere, hence integrability by Lemma 4.4 If on the other hand we suppose $k=0$ then (45) gives $W_{F}^{+}=0, R_{00}=0$. Putting this into (40) shows
$$0=\int_{M}\left|W_{00}^{+}\right|^{2}+56 v^{2}$$
and so $v=0$. We again therefore have $v=\frac{k}{2}=0$ and may apply Lemma 4.4. \(\square\)
6.2. Proof of Theorem 1.1. By Lemma 4.4 we know that if $v=\frac{k}{2}$ everywhere, then $M$ is Kähler. Let us argue by contradiction and therefore suppose that $v<\frac{k}{2}$ somewhere (the case $k>0$ can also be deduced directly). Then
$$\int_{M} c_{1}(T M) \cup \omega=\int_{M} \frac{s_{C}}{2 \pi}=\int_{M} \frac{4 k-2 v}{2 \pi}=\underbrace{\int_{M} \frac{3 k}{2 \pi}}_{\geq 0}+\int_{M} \frac{k-2 v}{2 \pi}>0 .$$
According to results in Seiberg-Witten theory of Taubes [30], Lalonde-McDuff [21], and Liu [25], this implies that $M$ is symplectomorphic to a ruled surface or to $\mathbb{C} P^{2}$ (see LeBrun [23, Section 2] for an overview, or also [27, Theorem 1.2]). In the case $\mathbb{C} P^{2}$ we get a contradiction to Proposition 6.2. Suppose therefore that $M$ is a ruled surface. Since $\sigma \leq 0$ for ruled surfaces, by (42) we must have $\sigma=0$, contradicting Proposition 6.1.

Hence we have shown that $M$ is Kähler. The classification stated in Theorem 1.1 now follows from [3, Theorem 2]. \(\square\)
6.3. Proof of Theorem 1.2. By Theorem 1.3 we have $W^{-}=0$. Hence the Bach tensor vanishes and so [4, Remark 2, p. 13] applies
$$0=\int_{M}\left(\frac{\left|d s_{g}\right|^{2}}{2}-s_{g} \cdot\left|r_{0}\right|^{2}\right) \mathrm{vol} .$$
The proof in [4] is a consequence of a Weitzenböck formula and the $J$-invariance of the Ricci tensor is used in a crucial way.

Since $s_{g}=12 v \leq 6 k<0$ we have in (47) two non-negative terms. Hence $s_{g}$ is constant and $R_{0}=0$. Therefore $M$ is Kähler-Einstein by Proposition 4.2. \(\square\)
6.4. Further Discussion. Besides removing in Theorem 1.2 the condition that the Ricci curvature is $J$-invariant, we mention the following open problems:
\begin{itemize}
\item[i)] Analogous results in the non-compact case. The case of Lie groups will be the topic of an upcoming paper of L. Vezzoni and the first named author [24].
\item[ii)] Counterexamples to Schur's Theorem. Are there almost Kähler manifolds of pointwise constant Hermitian holomorphic sectional curvature that are not globally constant? In particular, are there compact examples?
\item[iii)] There may be an alternative approach to our results using the twistor space of $M$. Note that in our situation, the tautological almost complex structure on the twistor space is integrable. What are the further geometric implications of constant holomorphic sectional curvature in terms of the twistor space?
\end{itemize}

\section*{References}
[1] V. Apostolov, J. Armstrong, and T. Drăghici. Local models and integrability of certain almost Kähler 4-manifolds. Math. Ann., 323(4):633-666, 2002.
[2] V. Apostolov, D. M. J. Calderbank, and P. Gauduchon. The geometry of weakly self-dual Kähler surfaces. Compositio Math., 135(3):279-322, 2003.
[3] V. Apostolov, J. Davidov, and O. Muškarov. Compact self-dual Hermitian surfaces. Trans. Amer. Math. Soc., 348(8):3051-3063, 1996.
[4] V. Apostolov and T. Drăghici. Almost Kähler 4-manifolds with $J$-invariant Ricci tensor and special Weyl tensor. Q. J. Math., 51(3):275-294, 2000.
[5] J. Armstrong. On four-dimensional almost Kähler manifolds. Q. J. Math., 48(192):405-415, 1997.
[6] A. Balas. Compact Hermitian manifolds of constant holomorphic sectional curvature. Math. $Z$., 189(2):193-210, 1985.
[7] A. Balas and P. Gauduchon. Any Hermitian metric of constant nonpositive (Hermitian) holomorphic sectional curvature on a compact complex surface is Kähler. Math. Z., 190(1):39-43, 1985.
[8] A. Besse. Einstein manifolds, volume 10 of Ergebnisse der Mathematik und ihrer Grenzgebiete. Springer-Verlag, 1987.
[9] D. E. Blair. Nonexistence of 4-dimensional almost Kaehler manifolds of constant curvature. Proc. Amer. Math. Soc., 110(4):1033-1039, 1990.
[10] T. Drăghici. On some 4-dimensional almost Kähler manifolds. Kodai Math. J., 18(1):156-168, 1995.
[11] T. Drăghici. Almost Kähler 4-manifolds with J-invariant Ricci tensor. Houston J. Math., 25(1):133-145, 1999.
[12] M. Falcitelli, A. Farinola, and O. T. Kassabov. Almost Kähler manifolds whose antiholomorphic sectional curvature is pointwise constant. Rend. Mat. Appl. (7), 18(1):151-166, 1998.
[13] P. Gauduchon. Calabi's extremal Kähler metrics: An elementary introduction. Book project in preparation.
[14] S. I. Goldberg. Integrability of almost Kaehler manifolds. Proc. Amer. Math. Soc., 21:96-100, 1969.
[15] A. Gray. Classification des variétés approximativement kählériennes de courbure sectionnelle holomorphe constante. C. R. Acad. Sci. Paris Sér. A, 279:797-800, 1974.
[16] A. Gray and L. Vanhecke. Almost Hermitian manifolds with constant holomorphic sectional curvature. Časopis Pěst. Mat., 104(2):170-179, 1979.
[17] N. S. Hawley. Constant holomorphic curvature. Canadian J. Math., 5:53-56, 1953.
[18] J. Igusa. On the structure of a certain class of Kaehler varieties. Amer. J. Math., 76:669-678, 1954.
[19] O. T. Kassabov. Almost Kähler manifolds of constant antiholomorphic sectional curvature. Serdica, 9(4):372-376 (1984), 1983.
[20] S. Kobayashi and K. Nomizu. Foundations of differential geometry. Vol. II. John Wiley \& Sons, Inc., New York, 1996.
[21] F. Lalonde and D. McDuff. $J$-curves and the classification of rational and ruled symplectic 4-manifolds. In Contact and symplectic geometry (Cambridge, 1994), volume 8, pages 3-42. Cambridge Univ. Press, 1996.
[22] C. LeBrun. On the topology of self-dual 4-manifolds. Proc. Amer. Math. Soc., 98(4):637-640, 1986.
[23] C. LeBrun. Weyl curvature, Del Pezzo surfaces, and almost-Kähler geometry. J. Geom. Anal., 25(3):1744-1772, 2015.
[24] M. Lejmi and L. Vezzoni. 4-dimensional almost-Kähler Lie algebras of constant Hermitian holomorphic sectional curvature are Kähler. Preprint in preparation.
[25] A. Liu. Some new applications of general wall crossing formula, Gompf's conjecture and its applications. Math. Res. Lett., 3(5):569-585, 1996.
[26] J. W. Milnor and J. D. Stasheff. Characteristic classes. Princeton University Press, 1974. Annals of Mathematics Studies, No. 76.
[27] H. Ohta and K. Ono. Notes on symplectic 4 -manifolds with $b_{2}^{+}=1$. II. Internat. J. Math., 7(6):755-770, 1996.
[28] T. Sato. An example of an almost Kähler manifold with pointwise constant holomorphic sectional curvature. Tokyo J. Math., 23(2):387-401, 2000.
[29] K. Sekigawa. On some 4-dimensional compact Einstein almost Kähler manifolds. Math. Ann., 271(3):333-337, 1985.
[30] C. H. Taubes. The Seiberg-Witten and Gromov invariants. Math. Res. Lett., 2(2):221-238, 1995.

Department of Mathematics, Bronx Community College of CUNY, Bronx, NY
10453, USA.
E-mail address: mehdi.lejmi@bcc.cuny.edu
Universitätsstrasse 14, 86159 Augsburg, Germany.
E-mail address: Markus.Upmeier@math.uni-augsburg.de