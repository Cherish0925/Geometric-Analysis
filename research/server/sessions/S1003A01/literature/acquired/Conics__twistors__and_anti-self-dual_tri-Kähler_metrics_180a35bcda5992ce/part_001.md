---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Conics, twistors, and anti-self-dual tri-Kähler metrics]

---
source_file: Conics__twistors__and_anti-self-dual_tri-Kähler_metrics_ec48b2ef5c9d.pdf
converter: mathpix
format: mmd
---

\title{
CONICS, TWISTORS, AND ANTI-SELF-DUAL TRI-KÄHLER METRICS
}

\author{
MACIEJ DUNAJSKI AND PAUL TOD
}

\begin{abstract}
We describe the range of the Radon transform on the space $M$ of irreducible conics in $\mathbb{C P}^{2}$ in terms of natural differential operators associated to the $S O(3)$-structure on $M=S L(3, \mathbb{R}) / S O(3)$ and its complexification. Following [27] we show that for any function $F$ in this range, the zero locus of $F$ is a four-manifold admitting an anti-self-dual conformal structure which contains three different scalar-flat Kähler metrics. The corresponding twistor space $\mathcal{Z}$ admits a holomorphic fibration over $\mathbb{C P}^{2}$. In the special case where $\mathcal{Z}=\mathbb{C P}^{3} \backslash \mathbb{C P}^{1}$ the twistor lines project down to a four-parameter family of conics which form triangular Poncelet pairs with a fixed base conic.
\end{abstract}

\section*{1. Introduction}

The twistor construction of Penrose [31], and its Riemannian version developed by Atiyah-Hitchin-Singer [1] give one-to-one correspondences between anti-self-dual conformal structures $[\gamma]$ on a four-manifold $X$, and complex three-folds $\mathcal{Z}$ with a four parameter family of rational curves. More conditions need to be imposed on $\mathcal{Z}$ if the conformal structure is to contain a Ricci-flat metric. In this case there exists a holomorphic fibration $\mathcal{Z} \rightarrow \mathbb{C P}^{1}$ with a twisted symplectic form on the fibres. A weaker condition is needed [32] if there exists a Kähler metric in $[\gamma]$. Then $\mathcal{Z}$ admits an anti-canonical divisor given by a section of $\kappa_{\mathcal{Z}}{ }^{-1 / 2}$, where $\kappa_{\mathcal{Z}}$ is the holomorphic canonical bundle of $\mathcal{Z}$. While there exist many explicit examples of twistor correspondences in both Ricci-flat [19, 36], and Kähler [26] cases, the resulting metrics in the conformal class are special in that they admit continuous groups of isometries. There are some notable exceptions in the Ricci-flat case, if the twistor space fibers holomorphically over the total space of a line bundle $\mathcal{O}(k)$. The corresponding hyper-Kähler metrics arise from the generalised Legendre transform [24], and admit tri-holomorphic Killing spinors [8], but in general no Killing vectors.

Much less is known about the Kähler case. Moraru [28, 27] considered twistor spaces which holomorphically fiber over $\mathbb{C P}^{2}$. He identified a set of second-order linear operators on the space $M$ of irreducible plane conics in $\mathbb{C P}^{2}$, and showed how any function $F$ in the kernel of these operators gives rise to a conformal structure on the hypersurface $F=0$ in $M$. Moraru's papers do not contain explicit examples, and an attempt to find such examples led us to this work. We show that some of Moraru's operators on $M$ are redundant, and we construct a set of independent operators out of natural geometric structures on $M: M$ is an irreducible symmetric space carrying an Einstein metric of negative scalar curvature, and a symmetric cubic three-form which, together with the metric, gives an $S O(3)$ structure in the sense of [4], [15]. The corresponding operators characterise the range of the Penrose-Radon transform defined below on the space of conics.

We find several explicit functions in the range of this conic Penrose-Radon transform, and construct corresponding conformal structures $[\gamma]$. There is a preferred metric, which we call the barycenter metric, in each $[\gamma]$. The barycenter metric admits three linearly independent solutions to the conformal Killing-Yano equations. Each such solution gives

\footnotetext{
Date: 16 May 2019.
}
rise to an explicit conformal factor which reswcales the barycenter metric to a Kähler metric. Kähler metrics in a given ASD conformal class $(X,[\gamma])$ correspond [10] to parallel sections of a certain connection on a rank ten vector bundle
$$E=\Lambda_{+}^{2}(X) \oplus \Lambda^{1}(X) \oplus \Lambda_{-}^{2}(X) .$$
The ASD conformal structures arising from our construction admit a three-dimensional space of parallel sections of $E$. We call them tri-Kähler.

In the next Section we shall introduce a $G L(2)$-structure isomorphism
$$\rho: T_{m} M \otimes \mathbb{C} \rightarrow \operatorname{Sym}^{4}\left(\mathbb{C}^{2}\right)$$
on the space of irreducible real conics with no real points $M=S L(3, \mathbb{R}) / S O(3)$, and use it (Proposition 2.3) to construct an Einstein metric and a cubic three-form on $M$. They will both be given in terms of the bi-linear pairing $\left\langle,>_{k}: V_{l} \times V_{n} \rightarrow V_{l+n-2 k}\right.$ given by (2.7), where $V_{n}=\operatorname{Sym}^{n}\left(\mathbb{C}^{2}\right)$. In §3 these structures give rise to a metric Laplacian $\Delta_{g}$, and another second order differential operator □ with values in $\Lambda^{1}(M)$ which characterise (Theorem 3.1) the range of the Penrose-Radon transform on conics as follows: if $U$ is a neighbourhood of an irreducible conic $C_{m} \subset \mathbb{C P}^{2}$ corresponding to $m \in M$, and $f \in$ $H^{1}\left(U, \mathcal{O}_{\mathbb{C P}^{2}}(-1)\right)$. Then the Penrose-Radon transform $F: M \rightarrow \mathbb{R}$ of $f$ satisfies the system of PDEs
$$\Delta_{g} F=-\frac{1}{12} F, \quad \square F=\frac{1}{24} d F .$$
Theorem 3.1 makes some of the differential operators introduced in [27] redundant, and clarifies the geometric meaning of the remaining operators.

In §4 we introduce a four-manifold $X$ as a hyper-surface in $M$ corresponding to the zero set of any function in the range of the Penrose-Radon transform. We show (Theorem 4.3 and Theorem 4.4) that this conformal structure is anti-self-dual, and that it contains a barycentre metric. We shall give several explicit examples of barycentre metrics, including a Ricci-flat example. Finally in §5 we consider a holomorphic fibration of the complement of a rational normal curve in $\mathbb{C P}^{3}$ over $\mathbb{C P}^{2}$. We characterise (Proposition 5.6 and Proposition 5.4) the four-parameter family of conics which arise as images of lines in $\mathbb{C P}^{2}$ under a quadratic map. This brings up some classical 19th century projective geometry involving loci of Gergonne points and the Poncelet porism [16, 7]. We shall prove

Theorem 1. Let $Q: \mathbb{C P}^{3} \backslash \mathbb{C P}^{1} \rightarrow \mathbb{C P}^{2}$ be the projectivisation of the moment map for the symplectic $S L(2, \mathbb{C})$ action on the space of cubics with at least two distinct roots. The image of lines in $\mathbb{C P}^{3} \backslash \mathbb{C P}^{1}$ are conics in $\mathbb{C P}^{2}$ corresponding to a hypersurface $X \subset M$. If $x \in X$, then there exists a triangle inscribed in the corresponding conic $C_{x}$ and circumscribed about a base conic $\left(Z^{1}\right)^{2}+\left(Z^{2}\right)^{2}+\left(Z^{3}\right)^{2}=0$. Equivalently
$$2 \operatorname{Tr}\left(A_{x}{ }^{2}\right)-\operatorname{Tr}\left(A_{x}\right)^{2}=0,$$
where $A_{x}=A_{x}{ }^{T}$ is the non-singular symmetric 3 by 3 matrix defining the conic $C_{x}$.
Acknowledgements. We are grateful to Claude LeBrun and Lionel Mason for discussion about twistor theory, and to Robert Bryant, Nigel Hitchin and Miles Reid for correspondence clarifying the quadratic map discussed in §5. The work of M.D. has been partially supported by STFC consolidated grant no. ST/P000681/1. Part of this work was done while P.T. held the Brenda Ryman Visiting Fellowship in the Sciences at Girton College, Cambridge, and he gratefully acknowledges the hospitality of the College.

\section*{2. The space of plane conics}
2.1. $G L(2)$ structure and twistor theory. Let $Z=\left[Z^{1}, Z^{2}, Z^{3}\right]$ be the homogeneous coordinates in $\mathbb{C P}^{2}$. A general conic in $\mathbb{C P}^{2}$ is of the form
$$f([Z], A) \equiv Z A Z^{T}=0,$$
where $A$ is a complex symmetric matrix. Thus the space of conics is $\mathbb{P}\left(\operatorname{Sym}^{2}\left(\mathbb{C}^{3}\right)\right)=$ $\mathbb{C P}^{5}$. We shall consider the five-dimensional space $M_{\mathbb{C}}$ of irreducible conics normalised by $\operatorname{det}(A)=1$. The projective group $P S L(3, \mathbb{C})$ acts on $M_{\mathbb{C}}$ transitively by
$$A \longrightarrow N A N^{T} \quad \text { where } \quad N \in S L(3, \mathbb{C}),$$
so $M_{\mathbb{C}} \cong S L(3, \mathbb{C}) / S O(3, \mathbb{C})$ as $S O(3, \mathbb{C})$ stabilises the conic $A=\mathbf{1}$. The conic $A=\mathbf{1}$, or equivalently $Z Z^{T}=0$ admits no real points, so it belongs to $\mathbb{C P}^{2} \backslash \mathbb{R P}^{2}$. Its $S L(3, \mathbb{R})$ orbit consists of conics with real coefficients but no real points. The real five-dimensional manifold of such conics is $M=S L(3, \mathbb{R}) / S O(3, \mathbb{R})$. It is a real slice in the complex manifold $M_{\mathbb{C}}$.

The vector fields in $M_{\mathbb{C}}$ can be canonically identified with homogeneous fourth order polynomials in two variables - this will play a role in what follows. To formalise it, let us first make a definition

Definition 2.1. $A G L(2)$ structure on an $(n+1)$ - complex dimensional complex manifold $M_{\mathbb{C}}$ is an isomorphism:
$$T M_{\mathbb{C}} \cong \operatorname{Sym}^{n}(\mathbb{S})$$
where $\mathbb{S}$ is a rank-two complex symplectic vector bundle over $M_{\mathbb{C}}$.
This structure was called a paraconformal structure in [9], and $G_{n}$ structure in [5]. In practice a $G L(2)$ structure is specified by a one-form $S$ on $M_{\mathbb{C}}$ with values in $\operatorname{Sym}^{n}\left(\mathbb{C}^{2}\right)$. Let $e^{1}, e^{2}, \ldots, e^{n+1}$ be $(n+1)$ independent one-forms on $M_{\mathbb{C}}$. Then
$$S=t^{n} e^{1}+n t^{n-1} s e^{2}+\frac{1}{2} n(n-1) t^{n-2} s^{2} e^{3}+\cdots+s^{n} e^{n+1},$$
and the isomorphism (2.4) is given by $\rho(V)=V\lrcorner S$, where $V \in \Gamma\left(T M_{\mathbb{C}}\right)$ and $\lrcorner$ denotes contraction of a vector field with a form.

For even $n=2 l$ there are two real forms of the $G L(2)$ structure. In the indefinite case the one forms $e^{1}, \ldots, e^{n+1}$ can be taken to be real, and $[s, t] \in \mathbb{R P}^{1}$. In the positive definite case
$$\overline{S(\lambda)}=(-1)^{l} \bar{\lambda}^{2 l} S(-1 / \bar{\lambda}), \quad \text { where } \quad \lambda=t / s .$$
In what follows we shall be interested in the case $n=4$, where the holomorphic five-manifold $M_{\mathbb{C}}$ admits real form $M$ with a positive definite quadratic form. In this case
$$S[s, t]=t^{4} e^{1}+4 t^{3} s e^{2}+6 t^{2} s^{2} e^{3}-4 t s^{3} \overline{e^{2}}+s^{4} \overline{e^{1}},$$
where the one-forms $e^{1}, e^{2}$ are complex, and $e^{3}$ is real.
Proposition 2.2. The space of plane conics carries a $G L(2)$ structure.
Proof. All plane conics are rational curves and two neighbouring conics intersect at four points. Thus if $C_{m} \cong \mathbb{C P}^{1}$ is a conic corresponding to $m \in M_{\mathbb{C}}$ then the normal bundle $N\left(C_{m}\right) \cong \mathcal{O}(4)$. The obstruction group $H^{1}\left(\mathbb{C P}^{1}, \mathcal{O}(4)\right)=0$, so $M_{\mathbb{C}}$ is a locally complete family, and there exists a Kodaira isomorphism [25]
$$T_{m} M_{\mathbb{C}} \cong H^{0}\left(C_{m}, N\left(C_{m}\right)\right)=\operatorname{Sym}^{4}\left(\mathbb{C}^{2}\right)$$
identifying vectors tangent to $M_{\mathbb{C}}$ with binary quartics. Therefore $M_{\mathbb{C}}$ carries a $G L(2)$ structure. The isomorphism (2.6) is specified by a fourth-order polynomial $S$ homogeneous
in two variables and with values in $\Lambda^{1}\left(M_{\mathbb{C}}\right)$. Given such $S$, the binary quartic corresponding under (2.6) to a vector field $V \in T M_{\mathbb{C}}$ is the contraction $\left.V\right\lrcorner S$. \(\square\)
2.1.1. Transvectants and Invariants. In the reminder of this section we shall use the $G L(2)$ structure on $M_{\mathbb{C}}$ to construct a conformal structure, and a symmetric cubic three-form. Both structures originate from classical invariants of binary quartics [14], and these invariants can be conveniently introduced using the transvectant/spinor notation together with some representation theory of $\mathfrak{s l}(2, \mathbb{C})$.

Let $V_{l}=\operatorname{Sym}^{l}\left(\mathbb{C}^{2}\right)$ be the $(l+1)$-dimensional complex vector space of binary quantics of degree $l$. These quantics are the same as polynomials in $[s, t]$ homogeneous of degree $l$. Given two binary quantics $\phi \in V_{n}$ and $\psi \in V_{l}$, the $k$ th transvectant is a map $<,>_{k}$ : $V_{l} \times V_{n} \rightarrow V_{l+n-2 k}$ given by a quantic of degree $l+n-2 k$
$$<\phi, \psi>_{k}:=\sum_{j=1}^{k}(-1)^{j}\binom{k}{j} \frac{\partial^{k} \phi}{\partial s^{k-j} \partial t^{j}} \frac{\partial^{k} \psi}{\partial s^{j} \partial t^{k-j}} .$$
This map is $S L(2, \mathbb{C})$ equivariant, and is symmetric for $k$ even and skew-symmetric for $k$ odd. Where possible, we will use the notation (2.7) instead of the spinor notation [12] which we summarise in the Appendix. For example if $\phi \in V_{3}$ and $\psi \in V_{4}$ then $<\phi, \psi>_{2}$ is a cubic proportional to $\phi_{(A}{ }^{D E} \psi_{B C) D E}$.
2.2. Conformal structure and Einstein metric. In the next Proposition we shall give a twistor construction of an Einstein metric on a five dimensional manifold $M$ which is a real slice of $M_{\mathbb{C}}$. The metric itself is well known in the theory of symmetric spaces [18]. Our treatment will follow the twistor procedure of [11].

Proposition 2.3. Let $\left[g_{\mathbb{C}}\right]$ be the conformal structure on the space of complex irreducible conics $M_{\mathbb{C}}=S L(3, \mathbb{C}) / S O(3, \mathbb{C})$ such that the vector field $V \in \Gamma\left(T M_{\mathbb{C}}\right)$ is null iff the corresponding 4th order polynomial has a vanishing transvectant $<V, V>_{4}=0$.
\begin{itemize}
\item[-] There exists a real form $M=S L(3, \mathbb{R}) / S O(3)$ of $M_{\mathbb{C}}$ where $\left[g_{\mathbb{C}}\right]$ gives a positive definite conformal structure $[g]$, and such that there exists a Riemannain metric $g \in[g]$ which is Einstein, has negative scalar curvature, and admits $S L(3, \mathbb{R})$ as its isometry group.
\item[-] Local coordinates $(a, b, p, q, r)$ can be used on $M$ to parametrise conics, such that then
$$g=8\left[(2 d a+d b)^{2}+3 d b^{2}+e^{2 a+4 b} d p^{2}+e^{2 a-2 b} d r^{2}+e^{4 a+2 b}(d q-p d r)^{2}\right] .$$
\end{itemize}

Proof. A vector in $V \in \mathbb{C} \otimes T M$ is null if the corresponding quartic has vanishing transvectant i. e.
$$<V, V>_{4}=4 \alpha \epsilon-8 \beta \delta+6 \gamma^{2}, \quad \text { where } \quad V=\alpha t^{4}+4 \beta t^{3} s+6 \gamma t^{2} s^{2}+4 \delta t s^{3}+\epsilon s^{4} .$$
This nullity condition can be interpreted in terms of the roots of $V$ : they can be transformed to vertices of a regular tetrahedron in $\mathbb{C P}^{1}$ (if they are distinct), or at least three of the roots coincide ${ }^{1}$ [14].

\footnotetext{
${ }^{1}$ Such a conformal structure exists on any odd-dimensional manifold with a $G L(2)$-structure. The geometric interpretation in terms of roots of the associated homogeneous polynomial also exists, but is a little more complicated [12]. For even $n$, say $n=2 l$, the real forms are as follows: in the indefinite case the quadratic form $<\rho(V), \rho(V)>_{2 l}$ has signature $(l, l+1)$, and is invariant under $S L(2, \mathbb{R})$; in the positve definite case this quadratic form is positive-definite, and is invariant under $\operatorname{SU}(2)$.
}

To find explicit forms of the metric and the $G L(2)$ stucture on $M$ we use the fact that any symmetric matrix $A$ is of the form
$$A=B B^{T},$$
where $B$ is upper triangular, so that the general conic (2.2) is $Z B B^{T} Z^{T}=0$. A convenient parametrisation of $B$ turns out to be
$$B=\left(\begin{array}{ccc}
e^{c} & p e^{b} & q e^{a} \\
0 & e^{b} & r e^{a} \\
0 & 0 & e^{a}
\end{array}\right),$$
where $(a, b, p, q, r)$ are real coordinates on $M$. To single out the irreducible conics we chose the normalisation $\operatorname{det}(B)=1$ which corresponds to $a+b+c=0$.

To find the paraconformal structure consider a neighbouring conic where $B$ is replaced by $B+d B$ in (2.2). It will intersect the conic (2.2) at four points corresponding to the roots of a quartic
$$S(s, t)=\left.\sum_{\alpha, \beta} \frac{\partial f}{\partial B_{\alpha \beta}}\right|_{Z=Z([s, t], B)} d B_{\alpha \beta},$$
where $Z([s, t], B)$ is a rational parametrisation of the general conic and $\operatorname{det}(B)=1$. To find this rational parametrisation consider a conic $W=\left[W^{1}, W^{2}, W^{3}\right]$ given by
$$\left(W^{1}\right)^{2}+\left(W^{2}\right)^{2}+\left(W^{3}\right)^{3}=0$$
which is (2.2) with $B=\mathbf{1}$. Any other conic is projectively equivalent to this one, so we can use (2.11) with $f=Z B B^{T} Z^{T}$, and the parametrisation
$$\begin{aligned}
Z & =W B^{-1}, \quad \text { where } \quad W=\left[s^{2}-t^{2}, 2 t s, i\left(s^{2}+t^{2}\right)\right] \\
& =\left[e^{a+b}\left(s^{2}-t^{2}\right), 2 e^{-b} s t-e^{a+b} p\left(s^{2}-t^{2}\right), e^{a+b}(p r-q)\left(s^{2}-t^{2}\right)-2 r e^{-b} s t+i e^{-a}\left(s^{2}+t^{2}\right)\right] .
\end{aligned}$$
The formula (2.11) leads to
$$S=W \Omega W^{T}, \quad \text { where } \quad \Omega \equiv B^{-1} d B+\left(B^{-1} d B\right)^{T} .$$
Note that the $S L(3, \mathbb{R})$ action on $M$ takes the form $B \rightarrow N B$. This does not preserve the upper-triangular matrices $B$, but it preserves $B^{-1} d B$. Therefore both the paraconformal structure encoded in the quartic $S$ and the resulting metric (2.9) are $S L(3, \mathbb{R})$ invariant. Computing $S$ explicitly gives
$$\begin{aligned}
S(s, t) & =t^{4}\left(\Omega_{11}-\Omega_{33}-2 i \Omega_{13}\right)+4 t^{3} s\left(i \Omega_{23}-\Omega_{12}\right)+6 t^{2} s^{2}\left(\frac{2}{3} \Omega_{22}-\frac{1}{3} \Omega_{11}-\frac{1}{3} \Omega_{33}\right) \\
& +4 t s^{3}\left(i \Omega_{23}+\Omega_{12}\right)+s^{4}\left(\Omega_{11}-\Omega_{33}+2 i \Omega_{13}\right)
\end{aligned}$$
This leads to the positive definite $S L(3)$-invariant conformal structure (2.9)
$$g=4\left(\Omega_{12}^{2}+\Omega_{13}^{2}+\Omega_{23}^{2}\right)+\left(\Omega_{11}-\Omega_{33}\right)^{2}+3\left(\Omega_{11}+\Omega_{33}\right)^{2}$$
where we have used $\Omega_{11}+\Omega_{22}+\Omega_{33}=0$. To find the explict form of the conformal structure compute
$$B^{-1} d B=\left(\begin{array}{ccc}
-d a-d b & e^{2 b+a} d p & e^{2 a+b}(d q-p d r) \\
0 & d b & e^{a-b} d r \\
0 & 0 & d a
\end{array}\right) .$$
Using $(a, b, p, q, r)$ as real coordinates on $M$ yields the Riemannian metric (2.8). We verify by explicit calculation that this metric is Einstein with negative scalar curvature equal to $-15 / 16$. The isometry group of (2.8) is $S L(3, \mathbb{R})$. The Killing vectors generating this goup are given in the Appendix by the formula (A2). \(\square\)
2.3. $S O(3)$ structure on the space of conics. In this Section we shall reveal an additional structure on the space of irreducible conics which will (in §3) play a role in a characterisation of the Penrose-Radon transform on coincs.

Definition 2.4. An integrable $S O(3)$ structure on a five-dimensional manifold $M$ is a pair $(g, G)$, where $g$ is a Riemannain metric, and $G$ is a symmetric three-form on $T M$ such that [15, 4].
$$\nabla_{a} G_{b c d}=0, \quad 6 G^{a}{ }_{(b c} G_{d e) a}=g_{(b c} g_{d e)}, \quad G_{a b c} g^{a b}=0 .$$

We have seen that the fourth transvectant endows the space of conics with an Einstein metric. We shall now see that another transvectant operation gives an $S O(3)$ structure on $(M, g)$.

Proposition 2.5. Let $g$ be the Einstein metric on the space of conics from Proposition 2.3, such that $g(V, V)=<V, V>_{4}$. The symmetric cubic form
$$G: T M \odot T M \odot T M \rightarrow \mathbb{R}$$
given by $G(V, V, V)=\ll V, V>_{2}, V>_{4}$ gives an integrable $S O(3)$ structure.
Proof. We will establish the identities (2.13) directly. The $G L(2)$ structure $S \in \Lambda^{1}(M) \otimes$ $\operatorname{Sym}^{4}\left(\mathbb{C}^{2}\right)$ is given by (2.5), where $e^{1}, \ldots, e^{5}$ is the pentad of one-forms on $M$ given by
$$\begin{aligned}
& e^{1}=-2\left(d b+2 d a+i e^{2 a+b}(d q-p d r)\right), \quad e^{2}=-\left(e^{a+2 b} d p-i e^{a-b} d r\right), \quad e^{3}=2 d b, \\
& e^{5}=\overline{e^{1}}, \quad e^{4}=-\overline{e^{2}} .
\end{aligned}$$
This gives rise to the metric $g$ from Proposition 2.3, and a symmetric three-form $G$ as
$$\begin{aligned}
g & =2 e^{1} \odot e^{5}-8 e^{2} \odot e^{4}+6 e^{3} \odot e^{3} \\
G & =6\left(e^{1} \odot e^{5} \odot e^{3}+2 e^{2} \odot e^{4} \odot e^{3}-e^{3} \odot e^{3} \odot e^{3}-e^{1} \odot e^{4} \odot e^{4}-e^{5} \odot e^{2} \odot e^{2}\right),
\end{aligned}$$
where
$$\begin{aligned}
u \odot v & :=\frac{1}{2}(u \otimes v+v \otimes u) \\
u \odot v \odot w & :=\frac{1}{6}(u \otimes v \otimes w+u \otimes w \otimes v+v \otimes u \otimes w+v \otimes w \otimes u+w \otimes u \otimes v++w \otimes v \otimes w) .
\end{aligned}$$
The metric and the cubic form satisfy (2.13). Moreover the $S L(3)$ action (2.3) on $M$ preserves $G$. \(\square\)

\section*{3. The Penrose-Radon transform on the space of conics}

Let $\mathcal{L} \rightarrow \mathbb{C} \mathbb{P}^{2}$ be a holomorphic line bundle such that $\left.\mathcal{L}\right|_{C_{m}} \cong \mathcal{O}_{\mathbb{C} \mathbb{P}^{1}}(-2)$ for any conic and let $f \in H^{1}(U, \mathcal{L})$, where $U$ is a neighbourhood of $C_{m}$ in $\mathbb{C P}^{2}$. Restricting $f$ to a conic $C_{m}$ and integrating over a contour $\Gamma \subset C_{m}$ defines a function on $M$ by
$$F(m)=\oint_{\Gamma \subset C_{m}} f\left[Z^{1}(s, t, m), Z^{2}(s, t, m), Z^{3}(s, t, m)\right](s d t-t d s)$$
If $\left[Z^{1}, Z^{2}, Z^{3}\right]$ are three quadrics in $[s, t]$, then
$$\theta=f\left(Z^{i}\right)(s d t-t d s), \quad d \theta=\left(Z^{i} \frac{\partial f}{\partial Z^{i}}+f\right) d s \wedge d t .$$
Thus we require $f$ to be homogeneous of degree -1 in $Z$. For example taking
$$f=\frac{Z^{2}}{Z^{1} Z^{3}}$$
and using a contour enclosing the singularity at $[s, t]=[1,0]$ in $\mathbb{C P}^{1}$ gives (on taking the real part) ${ }^{2}$
$$F=\frac{e^{a-b} r}{e^{2 b}+r^{2} e^{2 a}} .$$
3.1. Differential operators on $S L(3, \mathbb{R}) / S O(3)$, and the range of the Penrose-Radon transfom. We aim to characterise the range of the transform (3.15) as the kernel of some differential operators on $M$. One natural operator is the metric Laplacian $\Delta_{g}=$ $g^{a b} \nabla_{a} \nabla_{b}$ of the metric (2.8) explicitly given in the Appendix by (A3). Another operator can be defined for any $S O(3)$ structure as follows. Define a second-order operator □ with values in $\Lambda^{1}(M)$ by
$$\square F=\left(G_{a}{ }^{b c} \nabla_{b} \nabla_{c} F\right) e^{a},$$
where the indices are raised and lowered by $g$ and its inverse.
Theorem 3.1. Let the function $F: M \rightarrow \mathbb{R}$ belong to the image of the Penrose-Radon transform (3.15). Then
$$\Delta_{g} F=-\frac{1}{12} F, \quad \square F=\frac{1}{24} d F .$$

Proof. This must follow from the abstract machinery of the Penrose transform [2], but here we present a concrete proof based on an explicit computation which hinges on a link between plane conics and the geometry of a certain fifth-order ODE. We start with the integral (3.15) and transform it by observing that each $Z^{i}$ is homogeneous of degree 2 in the pair $[s, t]$, while $f$ is homogeneous of degree -1 in the $Z^{i}$. Thus, with $\lambda=t / s$,
$$F(m)=\oint f\left(Z^{i}(\lambda)\right) d \lambda .$$
Introduce $x(\lambda)=Z^{1}(\lambda) / Z^{3}(\lambda), y(\lambda)=Z^{2}(\lambda) / Z^{3}(\lambda)$ to obtain
$$F(m)=\oint \tilde{f}(x, y) \frac{d \lambda}{Z^{3}(\lambda)},$$
where $\tilde{f}(x, y)=f(x, y, 1)$.
The pair $(x(\lambda), y(\lambda))$ defines a conic in parametric form but the conic can also be defined by giving $y$ as a function of $x$. In this case, with overdot for $d / d \lambda$, we may calculate
$$p:=\frac{d y}{d x}=\frac{Z^{3} \dot{Z}^{2}-Z^{2} \dot{Z}^{3}}{Z^{3} \dot{Z}^{1}-Z^{1} \dot{Z}^{3}},$$
and then
$$q:=\frac{d^{2} y}{d x^{2}}=\frac{\Delta\left(Z^{3}\right)^{3}}{\left(Z^{3} \dot{Z}^{1}-Z^{1} \dot{Z}^{3}\right)^{3}},$$
where
$$\Delta=\ddot{Z^{1}}\left(Z^{2} \dot{Z}^{3}-Z^{3} \dot{Z}^{2}\right)+\ddot{Z}^{2}\left(Z^{3} \dot{Z}^{1}-Z^{1} \dot{Z}^{3}\right)+\ddot{Z}^{3}\left(Z^{1} \dot{Z}^{2}-Z^{2} \dot{Z}^{1}\right),$$
which can be calculated from §2.2, with the result $\Delta=8 i$, in particular $\Delta$ is constant. It is now easy to see that
$$\frac{d \lambda}{Z^{3}(\lambda)}=\frac{d x}{\dot{x} Z^{3}}=q^{1 / 3} \Delta^{-1 / 3} d x$$

\footnotetext{
${ }^{2}$ Some other solutions are obtained as the residues:
$$\begin{gathered}
Z_{3} /\left(Z_{1}\right)^{2} \rightarrow \frac{q-p r}{e^{a+b}}, \quad Z_{2} /\left(Z_{1} Z_{3}\right) \rightarrow \frac{r e^{a}+i e^{b}}{e^{b}\left(r^{2} e^{2 a}+e^{2 b}\right)}, \\
Z_{3} /\left(Z_{1} Z_{2}\right) \rightarrow \frac{r-i e^{b-a}}{e^{a+b}}, \quad Z_{2} /\left(Z_{1}\right)^{2} \rightarrow p e^{-a-b}, \quad 1 / Z_{1} \rightarrow-e^{-a-b} .
\end{gathered}$$
}
and so, up to a multiplicative constant, which we ignore
$$F(m)=\oint \tilde{f}(x, y(x)) q^{1 / 3} d x$$
This will be the form of the integral with which we calculate. Both $y(x)$ and $q$ depend on $m$, the conic on which the integral is performed. It is straightforward to see that (3.18) agrees with the formula on p47 of [28].

For the next stage we review and revise some theory from [9]. Consider the following differential equation for dependent variable $y(x)$ :
$$y^{(5)}=\Lambda(x, y, p, q, r, s)=-\frac{40}{9} \frac{r^{3}}{q^{2}}+5 \frac{r s}{q}$$
with $p=y^{\prime}, q=y^{\prime \prime}, r=y^{\prime \prime \prime}, s=y^{\prime \prime \prime \prime}$. It is well-known, but in any case easy to see, that the solutions of (3.19) are the conics (first observe that the equation can be written as $\left.\left(q^{-2 / 3}\right)^{\prime \prime \prime}=0\right)$. Write the solution as
$$y=Z\left(x, X^{\mathbf{a}}\right), \quad \mathbf{a}=1, \ldots, 5,$$
so that $X^{\mathbf{a}}$ are coordinates on the solution space, that is on the space of conics, and concrete indices are bold. It will be convenient to choose the $X^{\mathbf{a}}$ to be the derivatives of $y$ from order zero to order four at some fixed but arbitrary choice of $x$. Call these ( $\mathbf{y}, \mathbf{p}, \mathbf{q}, \mathbf{r}, \mathbf{s}$ ).

Following [9], we suppose that there is a metric and spin-structure on the solution space such that the gradient of $Z$ is a quartic with a quadrupole root
$$\mathbf{y}_{, a}:=Z_{, a}=\iota_{A} \iota_{B} \iota_{C} \iota_{D},$$
for some spinor $\iota_{A}$ (and abstract indices are italic). There is an abstract justification for this assumption, as the space of conics admits the $G L(2)$ structure of Proposition 2.2. With prime for $d / d x$ we may suppose
$$\iota_{A}^{\prime}=P o_{A}$$
for some $P$ to be found, where $o_{A}$ completes a spinor basis, so that $o_{A} \iota^{A}=1$ and $\epsilon_{A B}=$ $o_{A} \iota_{B}-o_{B} \iota_{A}$. Now necessarily
$$o_{A}^{\prime}=Q \iota_{A},$$
for some $Q$ also to be found. Next we calculate
$$\left.\mathbf{p}_{, a}=\left(\mathbf{y}_{, a}\right)^{\prime}=4 P o_{(A} \iota_{B} \iota_{C} \iota_{D}\right),$$
and continue in the same way to express $\mathbf{q}_{, a}, \mathbf{r}_{, a}$ and $\mathbf{s}_{, a}$ in the spinor dyad. One more derivative together with (3.19) gives a set of identities which fix $P$ and $Q$.

Defining the metric $\tilde{g}_{a b}$ from $\epsilon_{A B}$ in the standard way as
$$\tilde{g}_{a p}=\tilde{g}_{A B C D \cdot P Q R S}=\epsilon_{(A}^{W} \epsilon_{B}^{X} \epsilon_{C}^{Y} \epsilon_{D)}^{Z} \epsilon_{P W} \epsilon_{Q X} \epsilon_{R Y} \epsilon_{S Z}$$
we may express all coordinate gradients $X_{, a}^{\mathbf{a}}$ in the spinor dyad and hence calculate all inner products $\tilde{g}^{a b} X_{, a}^{\mathbf{a}} X_{, b}^{\mathbf{b}}$, and then deduce the metric in these coordinates. For the covariant metric we find
$$\left(\tilde{g}_{\mathbf{a b}}\right)=\left(\begin{array}{ccccc}
\frac{\mathbf{r}^{\mathbf{2}} \mathbf{s}}{24 \mathbf{q}^{\mathbf{5}}}-\frac{5 \mathbf{r}^{\mathbf{4}}}{162 \mathbf{q}^{\mathbf{6}}}-\frac{\mathbf{s}^{\mathbf{2}}}{72 \mathbf{q}^{\mathbf{4}}} & \frac{\mathbf{r} \mathbf{s}}{72 \mathbf{q}^{\mathbf{4}}}-\frac{\mathbf{r}^{\mathbf{3}}}{54 \mathbf{q}^{\mathbf{5}}} & \frac{13}{72} \frac{\mathbf{r}^{\mathbf{2}}}{\mathbf{q}^{\mathbf{4}}}-\frac{\mathbf{s}}{12 \mathbf{q}^{\mathbf{3}}} & -\frac{\mathbf{r}}{8 \mathbf{q}^{\mathbf{3}}} & \frac{1}{\left.24 \mathbf{q}^{\mathbf{2}}\right)} \\
* & \frac{\mathbf{s}}{24 \mathbf{q}^{\mathbf{3}}}-\frac{\mathbf{r}^{\mathbf{2}}}{18 \mathbf{q}^{\mathbf{4}}} & \frac{\mathbf{r}}{24 \mathbf{q}^{\mathbf{3}}} & -\frac{1}{\left.24 \mathbf{q}^{\mathbf{2}}\right)} & 0 \\
* & * & -\frac{1}{24 \mathbf{q}^{\mathbf{2}}} & 0 & 0 \\
* & * & * & 0 & 0 \\
* & * & * & * & 0
\end{array}\right),$$
where asterisked terms are determined by symmetry. It is straightforward to check that this metric is Einstein with $R=-60$ and that it is indeed the metric of §2.2 multiplied by the constant factor 1/64. The corresponding $\tilde{G}_{a}{ }^{b c}$ with indices arranged like that is readily
found to be $8 G_{a}{ }^{b c}$, again with $G_{a}{ }^{b c}$ as in §2.3. These changes modify the eigenvalues in (3.16) so that those equations become
$$\tilde{\Delta} F=-\frac{16}{3} F, \quad \tilde{\square} F=\frac{1}{3} d F,$$
and our aim is to deduce these equations from the integral expression (3.18) for $F$, which can now be written
$$F\left(X^{\mathbf{a}}\right)=\oint \tilde{f}\left(x, Z\left(x, X^{\mathbf{a}}\right)\right) \mathbf{q}^{1 / 3} d x$$

Calculating in abstract indices we obtain
$$\begin{gathered}
\nabla_{a} F=\oint\left(\frac{\partial \tilde{f}}{\partial y} Z_{a} \mathbf{q}^{1 / 3}+\frac{1}{3} \tilde{f} \mathbf{q}^{-2 / 3} \mathbf{q}_{a}\right) d x \\
\tilde{\nabla}_{a} \nabla_{b} F=\oint\left(\frac{\partial^{2} \tilde{f}}{\partial y^{2}} Z_{a} Z_{b}+\frac{\partial \tilde{f}}{\partial y} \tilde{\nabla}_{a} Z_{b}\right) \mathbf{q}^{1 / 3} d x \\
+\oint\left(\frac{1}{3} \mathbf{q}^{-2 / 3} \frac{\partial \tilde{f}}{\partial y}\left(Z_{a} \mathbf{q}_{b}+Z_{b} \mathbf{q}_{a}\right)+\frac{1}{3} \tilde{f}\left(\mathbf{q}^{-2 / 3} \tilde{\nabla}_{a} \mathbf{q}_{b}-\frac{2}{3} \mathbf{q}^{-5 / 3} \mathbf{q}_{a} \mathbf{q}_{b}\right)\right) d x .
\end{gathered}$$
For $\tilde{\Delta} F$ we need to note
$$\tilde{g}^{a b} Z_{a} Z_{b}=0=\tilde{\Delta} Z=\tilde{g}^{a b} Z_{a} \mathbf{q}_{b}=\tilde{\Delta} \mathbf{q}, \quad \tilde{g}^{a b} \mathbf{q}_{a} \mathbf{q}_{b}-24 \mathbf{q}^{2}=0,$$
all of which follow from the expressions for $\tilde{g}^{a b} X_{, a}^{\mathbf{a}} X_{, b}^{\mathbf{b}}$, for then
$$\tilde{\Delta} F=-\frac{2}{9} \oint 24 \mathbf{q}^{1 / 3} \tilde{f} d x=-\frac{16}{3} F,$$
as required.
For $\tilde{\square} F$ we need expressions for $\tilde{G}_{a}{ }^{b c} X_{b}^{\mathbf{b}} X_{c}^{\mathbf{c}}$ which can be obtained from the coordinate gradients $X^{\mathbf{a}}{ }_{, a}$ in the spinor dyad. In particular we find
$$\tilde{G}_{a}^{b c} Z_{b} Z_{c}=0=\tilde{G}_{a}^{b c} \mathbf{q}_{b} Z_{c}-2 \mathbf{q} Z_{a}=\tilde{G}_{a}^{b c} \tilde{\nabla}_{b} Z_{c}+Z_{a}=\tilde{G}_{a}^{b c} \tilde{\nabla}_{b} \mathbf{q}_{c}+\mathbf{q}_{a}=\tilde{G}_{a}^{b c} \mathbf{q}_{b} \mathbf{q}_{c}+2 \mathbf{q} \mathbf{q}_{a} .$$
Then
$$\begin{gathered}
\tilde{\square} F=\int\left(-\mathbf{q}^{1 / 3} \tilde{f}_{y} d Z+\frac{4}{3} \mathbf{q}^{1 / 3} \tilde{f}_{y} d Z-\frac{1}{3} \mathbf{q}^{-2 / 3} \tilde{f} d \mathbf{q}-\frac{2}{9} \mathbf{q}^{-5 / 3} \tilde{f}(-2 \mathbf{q} d \mathbf{q})\right) d x \\
=\int\left(\frac{1}{3} \mathbf{q}^{1 / 3} \tilde{f}_{y} d Z+\frac{1}{9} \tilde{f} \mathbf{q}^{-2 / 3} d \mathbf{q}\right) d x=\frac{1}{3} d F
\end{gathered}$$
again as required, establishing the claim. \(\square\)

In the Appendix (formula (A5)) we give explicit expressions for the second order operator anihilating the functions in the range of (3.15).

The next proposition shows that the two sets of equations (3.17) are not independent: $\Delta_{g} F=-\frac{1}{12} F$ is implied by $\square F=\frac{1}{24} d F$. We shall establish a slightly more general result applicable to other forms of integrable $S O(3)$-structures with arbitrary constant and non-zero Ricci scalar

Proposition 3.2. Let $(M, g, G)$ be a five-dimensional integrable $S O(3)$ structure such that the Ricci scalar $R$ of $g$ is constant, and different than zero. Let $F: M \rightarrow \mathbb{R}$ satisfy
$$G_{a}{ }^{b c} \nabla_{b} \nabla_{c} F=\kappa \nabla_{a} F$$
for some constant $\kappa$. Then
$$\Delta_{g} F=\mu F, \quad \text { where } \quad \mu=6 \kappa^{2}+\frac{R}{10} .$$

Proof. Consider the $S O(3)$ structure (2.13), and trace (2.13) to obtain
$$G_{e f a} G^{e f}{ }_{b}=\frac{7}{12} g_{a b} \quad \text { and } \quad G_{a b c} G^{a b c}=\frac{35}{12} .$$
Commute derivatives on $G_{a b c}$ to obtain
$$R_{a b c}{ }^{(d} G^{e f) c}=0,$$
where $R_{a b c}{ }^{d}$ is the Riemann tensor of $g$. Define
$$\chi_{a b c d}=6 G^{e}{ }_{a b} G_{c d e}, \quad F_{b c a d}=\chi_{a[b c] d},$$
and claim
$$\chi_{a b c d}=\chi_{(a b c d)}+\frac{2}{3} F_{b c a d}+\frac{2}{3} F_{b d a c},$$
with
$$\chi_{(a b c d)}=6 G_{(a b}^{e} G_{c d) e}=g_{a(b} g_{c d)} .$$
Expand (3.24):
$$R_{a b c}{ }^{d} G^{e f c}+R_{a b c}{ }^{e} G^{f d c}+R_{a b c}{ }^{f} G^{d e c}=0$$
and contract with $G_{\text {efp }}$ to deduce
$$R_{a b c d} F_{p q}^{c d}=\frac{7}{4} R_{a b p q},$$
after relabeling of indices.
The system of interest is (3.22, 3.23) Compress notation by writing $F_{a}=\nabla_{a} F$ then from (3.22)
$$\begin{gathered}
6 \kappa^{2} F^{a}=6 G^{a b c} G_{b}{ }^{d e} \nabla_{c} \nabla_{d} F_{e}=\chi^{a c d e} \nabla_{c} \nabla_{d} F_{e} \\
=\left(g^{a(c} g^{d e)}+\frac{2}{3} F^{c d a e}+\frac{2}{3} F^{c e a d}\right) \nabla_{c} \nabla_{d} F_{e}
\end{gathered}$$
Here the first term is
$$\begin{gathered}
\frac{1}{3}\left(g^{a c} g^{d e}+g^{a d} g^{e c}+g^{a e} g^{c d}\right) \nabla_{c} \nabla_{d} F_{e} \\
=\frac{1}{3}\left(\nabla^{a} \Delta F+2 \nabla_{c} \nabla^{a} F^{c}\right) \\
=\frac{1}{3}\left(\nabla^{a} \Delta F+2 R^{a b} F_{b}+2 \nabla^{a} \Delta F\right) \\
=\nabla^{a}\left(\Delta F+\frac{2}{15} R F\right) .
\end{gathered}$$
The other two terms become
$$\begin{gathered}
\frac{4}{3} F^{c d a e} \nabla_{c} \nabla_{d} F_{e}=-\frac{2}{3} F^{c d a e} R_{c d f e} F^{f} \\
=-\frac{2}{3} \cdot \frac{7}{4} R^{a e}{ }_{f e} F^{f}=-\frac{7}{6} R^{a}{ }_{f} F^{f}=-\frac{7}{30} R F^{a} .
\end{gathered}$$
Putting them together
$$6 \kappa^{2} F_{a}=\nabla_{a}\left(\Delta F-\frac{1}{10} R F\right),$$
whence
$$\mu=6 \kappa^{2}+\frac{R}{10} .$$
Conversely, a solution $F$ of (3.22) with some $\kappa$ will necessarily satisfy (3.23) with the value of $\mu$ given by (3.27), possibly after adding a constant to $F$. \(\square\)
3.2. Examples. The general solution of the system (3.17) is given by integrating the cohomology classes of functions on suitable $U \subset \mathbb{C P}^{2}$ along conics. An explicit formula for $F$ seems to be out of reach, but there is a class of solutions of the form
$$F=\left(\gamma_{1}+\gamma_{2} p+\gamma_{3} r+\left(\gamma_{4}+\gamma_{5} p\right)(a+2 b)\right) e^{-a-b}+\left(\gamma_{6}+\gamma_{7} q+\gamma_{8} r\right) e^{-2 a},$$
where $\left(\gamma_{1}, \ldots, \gamma_{8}\right)$ are arbitrary constants. In particular all solutions which are independent of $(q, r)$ are of this form with $\gamma_{3}=\gamma_{7}=\gamma_{8}=0$.

Another class is obtained by looking for $F$ which does not depend on $r$. Setting $u=$ $\sqrt{p^{2} e^{2(b-a)}+e^{-2(2 a+b)}}$ leads to a general solution of the form
$$F=\frac{1}{u} e^{-2 a} K(u, q)+F_{1}(a, b, p), \quad \text { where } \quad \frac{\partial^{2} K}{\partial q^{2}}+\frac{\partial^{2} K}{\partial u^{2}}=0$$
and $F_{1}(a, b, p)$ is of the form (3.28) with $\gamma_{3}=\gamma_{7}=\gamma_{8}=0$. More examples arise from utilising the $S L(3)$ action on solutions to (3.17) induced by the action (2.3). For example by taking $F=r e^{-2 a}=\frac{A_{23}}{\left(A_{33}\right)^{2}}$, and replacing $A$ by $\hat{A}=N A N^{T}$.

\section*{4. Anti-self-dual conformal structures in dimension four}

This is the main section of our paper. Given a function $F$ in the range of the Penrose-Radon transform from §3, we shall construct an anti-self-dual metric $\gamma$ on the hypersurface $X$ given by the zero set of $F$ in $M$. The twistor space of $(X, \gamma)$ fibers holomorphically over $\mathbb{C P}^{2}$, and the twistor curves project to the four-parameter family of conics in $\mathbb{C P}^{2}$ such that the cohomology class corresponding to $F$ vanishes on this family. The resulting conformal structure is equivalent to that constructed by Moraru [27], but our procedure is different and leads to an explicit metric (which we call barycenter in §4.3), which admits three linearly independent solutions to the conformal Killing-Yano equations. Thus the barycenter metric is conformal to Kähler in three different ways. In §4.4 we shall give several examples of this construction. We shall prove

Theorem 2. Let $F: M \rightarrow \mathbb{R}$, and let $X$ be a four-manifold defined by
$$X=\{m \in M, F(m)=0\} .$$
Let $[\gamma]$ be a conformal structure on $X$ such that $V \in \mathbb{C} \otimes T M$ is null if $\rho(V)=h \otimes \iota$ where $h \in \operatorname{Sym}^{3}\left(\mathbb{C}^{2}\right)$ is such that $<h, \rho(d F)>_{3}=0$ and $\iota \in \mathbb{C}$. Then
\begin{itemize}
\item[(1)] The Weyl tensor of $[\gamma]$ is anti-self-dual if $F$ satisfies (1.1).
\item[(2)] There exists a basis $\left\{\Omega^{(1)}, \Omega^{(2)}, \Omega^{(3)}\right\}$ of $\Lambda^{2}{ }_{+}(X)$ such that $d \Omega^{(i)}=0, i=1,2,3$ if and only if $F$ satisfies (1.1).
\item[(3)] The conformal class $[\gamma]$ is tri-Kähler: given any metric $\gamma \in[\gamma]$ there exist three scalar-flat Kähler structures $\left(\gamma^{(i)}, \Omega^{(i)}\right)$, where $\gamma^{(i)}=\left|\Omega^{(i)}\right|_{\gamma} \gamma$.
\end{itemize}
This theorem will follow from Theorems 4.3 and 4.4.
Define a four-manifold by
$$X=\{m \in M, F(m)=0\},$$
where the function $F: M \rightarrow \mathbb{R}$ satisfies (3.17). Let $\rho(d F) \in \operatorname{Sym}^{4}\left(\mathbb{C}^{2}\right)$ be the quartic corresponding to $d F \in \Lambda^{1}(M)$ by the $G L(2)$ structure (2.5). Let $H \in \operatorname{Sym}^{3}\left(\mathbb{C}^{2}\right)$ be a cubic and let $l \in \mathbb{C}^{2}$ be a linear form. The conformal structure $[\gamma]$ on $X$ is determined by specifying the null cone to be the set of quartics
$$\mathcal{N}=\left\{H \otimes l, \quad \text { where } \quad<\rho(d F), H>_{3}=0\right\} .$$

This will be non-degenerate iff the $J$-invariant of the quartic $\rho(d F)$ given by
$$J=\ll \rho(d F), \rho(d F)>_{2}, \rho(d F)>_{4}$$
does not vanish, as then the space of solutions to the linear system of equations (4.30) for the four components of $H$ is two-dimensional.

We shall now rephrase this in the spinor notation (see Appendix A). Let $F: M \rightarrow \mathbb{R}$ and let $F_{A B C D}$ be defined by $d F=F_{A B C D} e^{A B C D}$, where $e^{A B C D}$ is defined by (A1).

A vector $V^{A B C D}$ is null on $X$ iff $V^{A B C D}=h^{\left(A B C{ }_{\iota}{ }^{D)}\right.}$, where $F_{A B C D} h^{A B C}=0$. Instead of solving this system for $h^{A B C}$ we use projections
$$h^{A B C} \rightarrow|F|^{2} h^{A B C}-2 h^{P Q R} F_{P Q R S} F^{S A B C},$$
of (for example) $o^{A} o^{B} o^{C}$ and $\iota^{A} \iota^{B} \iota^{C}$. To construct the explicit frame for $[\gamma]$ set
$$H=h_{0} s^{3}+3 h_{1} s^{2} t+3 h_{2} s t^{2}+h_{3} t^{3},$$
and solve (4.30) for $\left(h_{1}, h_{2}\right)$ in terms of $\left(h_{0}, h_{3}\right)$. Let $H_{0}$ be the cubic corresponding to $\left(h_{0}, h_{3}\right)=(1,0)$, and let $H_{1}$ corresponds to $\left(h_{0}, h_{3}\right)=(0,1)$. Let $V^{00}, V^{10}, V^{01}, V^{11}$ be four vector fields on $M$ corresponding to the quartics $H_{0} s, H_{0} t, H_{1} s, H_{1} t$. By construction, these vector fields annihilate the one-form $d F$, and so they span $T X$. To construct the conformal stucture explicitly, let $V_{F} \in T M$ be a vector field such that $\left.V_{F}\right\lrcorner S=d F$, where $S$ is the $G L(2)$ structure (2.11), and let $e^{00}, e^{01}, e^{10}, e^{11}, d V$ be a basis of $T^{*} M$ dual to $V^{00}, V^{01}, V^{10}, V^{11}, V_{F}$. Then the ASD conformal structure is
$$[\gamma]=\Omega^{2}\left(e^{01} e^{10}-e^{00} e^{11}\right)$$
where $\Omega: X \rightarrow \mathbb{R}^{+}$.
4.1. Conformal structure from self-dual two-forms. First recall the 'usual' twistor picture [31], but with primed and unprimed indices swapped round. Let $(X, \gamma)$ be an oriented Riemannian four-manifold with volume form $\operatorname{vol}_{X}$. The integrable twistor distribution is $L_{A^{\prime}}=\pi^{A} \nabla_{A^{\prime} A}$, and the self-dual (SD) two forms are $\Sigma^{A B}=1 / 2 \epsilon_{A B} e^{A^{\prime} A} \wedge e^{B^{\prime} B}$. The relation between $L_{A^{\prime}}$ and $\Sigma^{A B}$ is
$$\operatorname{vol}_{X}\left(L_{A^{\prime}}, L_{B^{\prime}}, \cdot, \cdot\right)=\epsilon_{A^{\prime} B^{\prime}} \pi_{A} \pi_{B} \Sigma^{A B} .$$
Conversely, given $\Sigma=\pi_{A} \pi_{B} \Sigma^{A B}$, the twistor distribution (and so the conformal structure) arises as the kernel of $\Sigma$, and the conformal structure can be recovered from the Urbantke formula [37]: Let $[\gamma]$ be a conformal structure on a four-manifold $X$ such that the two-forms $\Sigma^{A B}$ are self-dual. Then $\gamma(V, V)=0$ for any $\gamma \in[\gamma]$ if and only if
$$\Sigma_{A B}(V, \cdot) \wedge \Sigma^{B C}(V, \cdot) \wedge \Sigma_{C}{ }^{A}=0 .$$
In Theorem 4.3 below we shall reproduce (4.33) for the twistor discribution arising on the space of conics.

We make use of the isomorphisms
$$\mathbb{C} \otimes T_{m} M \cong \operatorname{Sym}^{4}\left(\mathbb{C}^{2}\right), \quad \Lambda^{2}\left(\operatorname{Sym}^{4}\left(\mathbb{C}^{2}\right)\right) \cong \operatorname{Sym}^{6}\left(\mathbb{C}^{2}\right) \oplus \operatorname{Sym}^{2}\left(\mathbb{C}^{2}\right)$$
to introduce a basis of $\Lambda^{2}(M)$
$$\sigma^{A B}=\frac{1}{48} e^{A C D E} \wedge e_{C D E}^{B}, \quad \sigma^{A B C D E F}=\frac{1}{8} e^{G(A B C} \wedge e^{D E F)}{ }_{G},$$
where $\sigma^{A B}$ and $\sigma^{A B C D E F}$ are defined in the Appendix.
Let us define three two-forms $\Sigma^{A B}=\Sigma^{(A B)}$ on $M$ by
$$\Sigma^{A B}=F^{A B}{ }_{C D} \sigma^{C D}+\frac{15}{2} F_{C D E F} \sigma^{A B C D E F} .$$
These will pull back to two-forms on the four-manifold $X$ defined by (4.29).

Lemma 4.1. Let $\Gamma^{A}{ }_{B}$ be the spin-connection of ( $M, g$ ). The following identity
$$d \Sigma^{A B}+\frac{1}{2} \Gamma^{(A}{ }_{C} \wedge \Sigma^{B) C}=-\sqrt{6} \square^{A B}{ }_{C D} F \star \sigma^{C D}+5 \sqrt{6} \square_{C D E F} F \star \sigma^{A B C D E F}-\frac{5 \sqrt{6}}{6} \Delta_{g} F \star \sigma^{A B}$$
holds for any $F: M \rightarrow \mathbb{R}$.
Proof. We find that
$$d \sigma^{A B}+\frac{1}{2} \Gamma_{C}^{(A}{ }_{C} \wedge \sigma^{B) C}=0, \quad d \sigma^{A B C D E F}+\frac{3}{2} \Gamma_{G}^{(A} \wedge \sigma^{B C D E F) G}=0$$
where
$$\Gamma^{1}{ }_{1}=-\Gamma^{0}{ }_{0}=\frac{1}{4}\left(e^{0000}-e^{1111}\right), \quad \Gamma^{1}{ }_{0}=-e^{0001}, \quad \Gamma^{0}{ }_{1}=-e^{0111} .$$
In five dimensions $\Lambda^{2}(M) \cong \Lambda^{3}(M)$ by Hodge isomorphism, and we take $\star \sigma^{A B}, \star \sigma^{A B C D E F}$ to be the basis of $\Lambda^{3}(M)$. The following identities can be established by an explicit computation
$$\begin{aligned}
e_{A B C D} \wedge \sigma^{E F} & =-\frac{\sqrt{6}}{2} \star \sigma_{A B C D}{ }^{E F}-\frac{2 \sqrt{6}}{5} \epsilon^{(E}{ }_{(A} \epsilon^{F)}{ }_{B} \star \sigma_{C D)}, \\
e_{A B C D} \wedge \sigma^{E F G H I J} & =-\frac{\sqrt{6}}{5} \epsilon^{(E}{ }_{(A} \epsilon^{F}{ }_{B} \epsilon_{C}^{G} \epsilon_{D)} \star \sigma^{I J)}+\sqrt{6} \epsilon_{(A} \epsilon_{B} \star \sigma^{G H I J)}{ }_{C D)} .
\end{aligned}$$
The identity (4.35) can now be verified directly. \(\square\)
4.2. The double fibration picture. Consider a double fibration
$$M_{\mathbb{C}} \longleftarrow \mathcal{F} \xrightarrow{\rho} \mathbb{C P}^{2},$$
where $\mathcal{F} \subset M_{\mathbb{C}} \times \mathbb{C P}^{2}$ is the six-dimensional manifold of incident pairs $(m, \xi)$ such that $\xi \in C_{m}$, where $\xi \in \mathbb{C P}^{2}$, and the conic $C_{m} \subset \mathbb{C P}^{2}$ corresponds to a point $m \in M_{\mathbb{C}}$. A point $\xi \in \mathbb{C P}^{2}$ corresponds to a hyper-surface $\hat{\xi} \subset T M_{\mathbb{C}}$ which is totally null in the sense of [9]: the normal vector to $\hat{\xi}$ is a polynomial with a quadruple root. The map $\rho$ is the quotient by the rank-four distribution $\mathcal{O}_{\mathbb{C} \mathbb{P}^{1}}(-1) \otimes \mathbb{C}^{4}$ given by $\mathcal{D}_{A B C}=\pi^{D} \nabla_{A B C D}$. Consider the projection of this distribution to a rank-two distribution on $\mathcal{F}$
$$\mathcal{D}_{A B C} \rightarrow L_{A B C}=|F|^{2} \mathcal{D}_{A B C}-2 F_{A B C D} F^{D P Q R} \mathcal{D}_{P Q R} .$$
In the next Theorem we shall establish the integrability of the distribution $\mathcal{D}_{A B C}$ assuming that the system (3.17) holds for $F$.

Theorem 4.2. Let $[\gamma]$ be a conformal structure on the four-manifold $X$ (4.29) such that $V \in T X$ is null iff $V^{A B C D}=h^{\left(A B C{ }_{\iota}{ }^{D)}\right.}$, where $F_{A B C D} h^{A B C}=0$. Then $[\gamma]$ is $A S D$ if equations (3.17) hold.

Proof. In the proof we shall use the constant rescaling of the metric by 1/64 which leads to equations (3.21).

Given $M$ and the zero-locus $X$ of $F$, consider the two-dimensional distribution spanned by $h^{(A B C} \iota^{D)}$ on $X$ where $\iota^{A}$ is the spinor field on $M$ introduced in (3.20) for one fixed choice of $x$ and $h^{A B C}$ is any solution of
$$h^{A B C} F_{A B C D}=0,$$
then this distribution is integrable provided $F$ satisfies the system
$$\square_{A B C D} F=\kappa F_{A B C D}, \quad \Delta F=\mu F,$$
with $\kappa=1 / 3$ and $\mu=-16 / 3$.

Evidently vectors of the form $h^{(A B C} \iota^{D)}$ are tangent to $X$. Choose two such vectors
$$X^{a}=h^{(A B C} \iota^{D)}, \quad Y^{a}=\tilde{h}^{\left(A B C_{\iota}\right.}{ }^{D)},$$
and consider their commutator $Z=[X, Y]$, or
$$Z^{A B C D}:=X^{P Q R S} \nabla_{P Q R S} Y^{A B C D}-Y^{P Q R S} \nabla_{P Q R S} X^{A B C D},$$
where $\nabla_{A B C D}$ is the metric covariant derivative on $M$. We wish to show that $Z^{A B C D}=$ $\hat{h}^{(A B C} \iota^{D)}$ for some $\hat{h}^{A B C}$ annihilating $F_{A B C D}$. From [13] we quote the formula
$$\iota^{S} \nabla_{P Q R S} \iota_{D}=\frac{1}{2} \iota_{P} \iota_{Q} \iota_{R} o_{D}+\gamma \iota_{P} \iota_{Q} \iota_{R} \iota_{D},$$
for some $\gamma$ which is known but will turn out to be irrelevant, and $\left(o^{A}, \iota^{A}\right)$ is a normalised spinor dyad. We calculate
$$\begin{gathered}
Z^{A B C D}=X^{P Q R S} \nabla_{P Q R S} Y^{A B C D}-Y^{P Q R S} \nabla_{P Q R S} X^{A B C D} \\
=\iota^{S}\left(h^{P Q R} \nabla_{P Q R S} \tilde{h}^{(A B C}-\tilde{h}^{P Q R} \nabla_{P Q R S} h^{(A B C)}\right) \iota^{D)} \\
+\iota^{S}\left(h^{P Q R} \tilde{h}^{(A B C}-\tilde{h}^{P Q R} h^{(A B C)} \nabla_{P Q R S} \iota^{D)} .\right.
\end{gathered}$$
It will be convenient to introduce a spinor field $\chi^{Q R}{ }_{B C}$, symmetric on each pair of spinor indices and with the interchange symmetry, by
$$h^{P Q R} \tilde{h}_{A B C}-\tilde{h}^{P Q R} h_{A B C}:=\delta_{(A}^{(P} \chi^{Q R)}{ }_{B C)} .$$
From the definition of $\chi^{Q R}{ }_{B C}$ it follows that
$$0=F_{P Q R S}\left(h^{P Q R} \tilde{h}_{A B C}-\tilde{h}^{P Q R} h_{A B C}\right)=F_{P Q R S} \delta_{(A}^{(P} \chi^{Q R)}{ }_{B C)}=F_{Q R S(A} \chi^{Q R}{ }_{B C)},$$
which also implies that
$$F_{Q R A B} \chi_{C D}^{Q R}=\frac{1}{2} \phi\left(\epsilon_{A C} \epsilon_{B D}+\epsilon_{B C} \epsilon_{A D}\right)$$
for some $\phi$, when by tracing on $A C$
$$F_{Q R S B} \chi^{Q R S D}=\frac{3}{2} \phi \delta_{B}^{D}$$
and, by tracing again,
$$\phi=\frac{1}{3} F_{P Q R S} \chi^{P Q R S} .$$
Thus
$$F_{Q R A B} \chi^{Q R}{ }_{C D}=\frac{1}{6}\left(F_{P Q R S} \chi^{P Q R S}\right)\left(\epsilon_{A C} \epsilon_{B D}+\epsilon_{B C} \epsilon_{A D}\right) .$$
With these we deduce that
$$Z^{A B C D}=\phi^{(A B C} \iota^{D)}$$
with
$$\phi^{A B C}=\iota^{S}\left(h^{P Q R} \nabla_{P Q R S} \tilde{h}^{A B C}-\tilde{h}^{P Q R} \nabla_{P Q R S} h^{A B C}\right)+\iota_{Q} \iota_{R} \chi^{Q R(A B}\left(\frac{1}{2} o^{C)}+\gamma \iota^{C)}\right),$$
where the last term uses (4.40). It remains to check that $\phi^{A B C} F_{A B C D}$ vanishes. From (4.42) we calculate
$$\begin{aligned}
& F_{A B C D} \phi^{A B C}= \\
& F_{A B C D}\left(\iota^{S}\left(h^{P Q R} \nabla_{P Q R S} \tilde{h}^{A B C}-\tilde{h}^{P Q R} \nabla_{P Q R S} h^{A B C}\right)+\iota_{Q} \iota_{R} \chi^{Q R(A B}\left(\frac{1}{2} o^{C)}+\gamma \iota^{C)}\right)\right.
\end{aligned}$$
and then, using $h^{A B C} F_{A B C D}=0=\tilde{h}^{A B C} F_{A B C D}$,
$$\begin{aligned}
& F_{A B C D} \phi^{A B C}= \\
& -\iota^{S}\left(h^{P Q R} \tilde{h}^{A B C}-\tilde{h}^{P Q R} h^{A B C}\right) \nabla_{P Q R S} F_{A B C D}+F_{A B C D} \iota_{Q} \iota_{R} \chi^{Q R(A B}\left(\frac{1}{2} o^{C)}+\gamma \iota^{C)}\right) .
\end{aligned}$$
Now we need to notice, again by symmetry, that there is a spinor field $Q^{R S}{ }_{C D}$ symmetric in both pairs of spinor indices and with the interchange symmetry satisfying
$$\nabla^{A Q R S} F_{A B C D}=\nabla^{A Q R S} \nabla_{A B C D} F=\delta_{(B}^{Q} Q_{C D)}^{R S)} .$$
Contractions then show that
$$Q^{R S}{ }_{C D}=\frac{3}{2} \square^{R S}{ }_{C D} F+\frac{1}{6} \Delta F\left(\delta_{C}^{R} \delta_{D}^{S}+\delta_{D}^{R} \delta_{C}^{S}\right) .$$
when with the aid of the system (4.39),
$$Q^{R S}{ }_{C D}=\frac{3 \kappa}{2} F^{R S}{ }_{C D}+\frac{\mu}{3} \delta_{(C}^{(R} \delta_{D)}^{S)} F .$$
With these in hand, (4.43) reduces to
$$F_{A B C D} \phi^{A B C}=\frac{1}{2} \kappa\left(\chi_{A B C D} F^{A B C D}\right) \iota_{D}-\frac{1}{6}\left(\chi_{A B C D} F^{A B C D}\right) \iota_{D},$$
where we have dropped the term proportional to $\mu$ as it vanishes on $X$. Evidently this vanishes if $\kappa=1 / 3$ (and we have seen elsewhere that with this value of $\kappa$ the other part of the system (4.39) automatically holds with $\mu=-16 / 3$ ). \(\square\)

The leaves of the distribution (4.38) are $\alpha$-surfaces of $(X,[\gamma])$. The set of conics through a given point in $\mathbb{C P}^{2}$ in a given direction is a three-dimensional surface in $M$. The intersection of this surface with the hyper-surface $F=0$ is two-dimensional. This is an $\alpha$-surface in $X$ or equivalently a point in the twistor space $\mathcal{Z}$ of $(X,[\gamma])$.

In the next Theorem we shall give a direct way to construct the ASD conformal structure on $X$ in terms of a preferred basis of self-dual two-forms on $X$. Let $\pi: X \rightarrow M$ be the map given by (4.29).

Theorem 4.3. Let $[\gamma]$ be the conformal structure on the four-manifold $X$ (4.29) such that $V \in \mathbb{C} \otimes T X$ is null iff $V^{A B C D}=h^{\left(A B C{ }_{\iota}{ }^{(D)}\right.}$, where $F_{A B C D} h^{A B C}=0$. Then the two-forms $\Sigma^{A B}$ given by (4.34) pull back to two-forms which are self-dual w.r.t the orientation given by the pull back of $\star_{5} d F$ from $M$ to $X$.

Conversely, let $\Sigma^{A B}$ be given by (4.34). Then
$$\pi^{*}\left(\Sigma^{(A B} \wedge \Sigma^{C D)}\right)=0,$$
and so $\Sigma^{A B}=(1 / 2) \epsilon_{A^{\prime} B^{\prime}} e^{A A^{\prime}} \wedge e^{B B^{\prime}}$ for some tetrad $e^{A A^{\prime}}$ on $X$ which is non-degenrate iff $J \neq 0$. The corresponding conformal structure is given by $[\gamma]$.

Proof. Consider the rank 2 distribution $L_{A B C}$ given by (4.38). Therefore for any $v^{A B C}$ the vector field $V=v^{A B C} L_{A B C}$ is a null vector field on ( $X,[\gamma]$ ) in the sense of Moraru:
$$V^{A B C D}=\pi^{(A} h^{B C D)}, \quad \text { where } \quad h^{B C D}=|F|^{2} v^{B C D}-2 F^{B C D E} F_{E P Q R} v^{P Q R}$$
so that $h^{B C D} F_{A B C D}=0$, where we have used the identity $2 F_{A B C D} F^{A B C E}=\delta_{D}{ }^{E}|F|^{2}$.
Let $\operatorname{vol}_{X}=\pi^{*}\left(\star_{5} d F\right)$ be a volume form on $X$. Consider the $\mathcal{O}_{\mathbb{C P}^{1}}(2)$-valued two form on $\mathbb{C P}^{1} \times X$ given by
$$\mathcal{S}=\left(\star_{5} d F\right)\left(L_{000}, L_{111}, \cdot, \cdot\right) .$$

We have verified using MAPLE that $\mathcal{S}=s \pi^{*}\left(\pi_{A} \pi_{B} \Sigma^{A B}\right)$, where the scalar multiple $s$ is, up to a constant numerical factor, given by
$$s=\pi^{*}\left(|F|^{2} F_{P Q R S} F^{P Q}{ }_{M N} o^{R} o^{M} \iota^{S} \iota^{N}\right),$$
and the two-forms $\Sigma^{A B}$ are given by (4.34). To establish the second part compute
$$\begin{gathered}
\Sigma^{00} \wedge \Sigma^{00} \wedge d F=\Sigma^{00} \wedge \Sigma^{01} \wedge d F=\Sigma^{11} \wedge \Sigma^{11} \wedge d F=\Sigma^{11} \wedge \Sigma^{01} \wedge d F=0 \\
\star\left(\Sigma^{00} \wedge \Sigma^{11} \wedge d F\right)=-2 \star\left(\Sigma^{01} \wedge \Sigma^{01} \wedge d F\right)=\frac{25 \sqrt{6}}{2592} J
\end{gathered}$$ \(\square\)
4.3. The barycenter metric, and the tri-Kähler structure. According to Moraru [27] there is a sphere of scalar-flat-Kähler metrics in every conformal class arising from conics. In Theorem 4.4 below we shall construct these Kähler forms explicitly, but let us first explain why one should expect them to exist from the twistor perspective.

Pick a section of $\mathcal{O}_{\mathbb{C P}^{2}}(1)$ which is of the form $\omega=W_{i} Z^{i}$ for some $[W] \in \mathbb{C P}^{2^{*}}$, and restrict it to a conic $C_{m}$ given by (2.12) and such that $F(m)=0$. This gives a quadratic polynomial - a section of $\mathcal{O}(2)$ restricted to a twistor line - given by $\omega_{A B} \pi^{A} \pi^{B}$, where $\omega_{A B}$ depends on $m \in M$, as well as $W$. There is a two-parameter family of $W \mathrm{~s}$, as linear functions on $\mathbb{C P}^{2}$ are defined up to scale of $\mathbb{C}^{3}$, so there is a (at least) three-dimensional space of solutions to the twistor equation $\left.\nabla_{A^{\prime}\left({ }_{A}\right.} \omega_{B C}\right)=0$ on the four-manifold $X$ given by (4.29).

Let $Z=\left[Z^{1}, Z^{2}, Z^{3}\right]$ be homogeneous coordinates on $\mathbb{C P}^{2}$, and let a rational parametrisation of the conic $Z A Z^{T}=0$ be $Z^{i}=Z_{A B}^{i} \pi^{A} \pi^{B}$, where $i=1,2,3$, and $Z_{A B}^{i}$ are functions of the components of the symmetric determinant-one matrix $A$ which defines the conic. Set
$$\left.\theta^{(i)}=\left(Z_{A B}^{(i)} Z^{(i) A B}\right)^{-3 / 2} \quad \text { (no summation over } i\right) .$$

Theorem 4.4. The two-forms
$$\left.\Omega^{(i)}=\theta^{(i)} Z_{A B}^{(i)} \Sigma^{A B} \quad \text { (no summation over } i\right)$$
pull-back to self-dual, closed two-forms on $X$ if and only if $F$ satisfies (3.17).
Proof. Let $\pi: X \rightarrow M$ be given by $F=0$, where $F: M \rightarrow \mathbb{R}$. Then, for any differential form $\Omega, \pi^{*} \Omega=0$ iff $\left.(\Omega \wedge d F)\right|_{F=0}=0$. Consider the parametrisation (with $\pi_{A}=[s, t]$ )
$$Z=\left[e^{a+b}\left(s^{2}-t^{2}\right), 2 e^{-b} s t-e^{a+b} p\left(s^{2}-t^{2}\right), e^{a+b}(p r-q)\left(s^{2}-t^{2}\right)-2 r e^{-b} s t+i e^{-a}\left(s^{2}+t^{2}\right)\right],$$
and compute
$$\theta^{(1)}=e^{-3 a-3 b}, \quad \theta^{(2)}=\left(4 p^{2} e^{2 a+2 b}+4 e^{-2 b}\right)^{-3 / 2}, \quad \theta^{(3)}=\left(2 e^{2 a+2 b}(p r-q)^{2}+2 e^{-2 a}+2 r^{2} e^{-2 b}\right)^{-3 / 2} .$$
Now use the identity (4.35) to compute
$$\left.\left(d \Omega^{(i)} \wedge d F\right)\right|_{F=0},$$
and find, using MAPLE, that it vanishes for $i=1,2,3$ if $\square F=(1 / 24) d F$ (this is the second set of equations (3.17)) and $\Delta_{g} F=c F$ for any $c$. Thus the constant $c$ (which should be -1/12 to agree with (3.17)) has not been determined. We have however shown in Proposition 3.2 that this constant is determined by the second set of equations together with the scalar curvature of $g$. \(\square\)

Let $\gamma \subset[\gamma]$ be any metric in the conformal class. Then the conformal class $[\gamma]$ contains three scalar-flat Kähler structures $\left(\gamma^{(i)}, \Omega^{(i)}\right)$, where
$$\gamma^{(i)}=\left|\Omega^{(i)}\right|_{\gamma} \gamma, \quad \text { where } \quad|\Omega|_{\gamma}=\sqrt{\Omega_{\alpha \beta} \Omega_{\gamma \delta} \gamma^{\alpha \gamma} \gamma^{\beta \delta}} .$$
For any metric $\gamma$ in the ASD conformal class $[\gamma]$ construct the barycenter metric
$$\gamma_{B}=\left(\left|\Omega^{(1)}\right|_{\gamma} \cdot\left|\Omega^{(2)}\right|_{\gamma} \cdot\left|\Omega^{(3)}\right|_{\gamma}\right)^{1 / 3} \gamma .$$
Then
$$\begin{aligned}
\Omega_{B}^{(3)} & =\frac{\left(\left|\Omega^{(1)}\right|_{\gamma} \cdot\left|\Omega^{(2)}\right|_{\gamma}\right)^{\frac{1}{2}}}{\left|\Omega^{(3)}\right|_{\gamma}} \Omega^{(3)}, \\
\Omega_{B}^{(2)} & =\frac{\left(\left|\Omega^{(1)}\right|_{\gamma} \cdot\left|\Omega^{(3)}\right|_{\gamma}\right)^{\frac{1}{2}}}{\left|\Omega^{(2)}\right|_{\gamma}} \Omega^{(2)}, \\
\Omega_{B}^{(1)} & =\frac{\left(\left|\Omega^{(3)}\right|_{\gamma} \cdot\left|\Omega^{(2)}\right|_{\gamma}\right)^{\frac{1}{2}}}{\left|\Omega^{(1)}\right|_{\gamma}} \Omega^{(1)}
\end{aligned}$$
are self-dual conformal Killing-Yano tensors for $\gamma_{B}$. Each such form gives rise [10] to a Kähler class, and the resulting tri-Kähler structure is (4.46)
4.4. Examples of tri-Kähler metrics. In this Section we shall construct some examples of anti-self-dual conformal structures containing (at least) three Kähler metrics, and corresponding to particular subcases of the solution (3.28).
4.4.1. An ASD Einstein example. Consider
$$F=e^{-2 a}+p e^{-a-b},$$
which is (3.28) with $\gamma_{2}=\gamma_{6}=1$, and the remaining constants equal to zero. The quartic corresponding to $d F$ via the isomorphism $\mathbb{C} \otimes T^{*} M=\operatorname{Sym}^{4}(\mathbb{S})$ is
$$\left(p e^{-a-b}+2 e^{-2 a}\right) s^{4}+4 e^{-2 a-3 b} s^{3} t+\left(4 e^{-2 a}-2 p e^{-a-b}\right) s^{2} t^{2}-4 e^{-2 a-3 b} s t^{3}+\left(p e^{-a-b}+2 e^{-2 a}\right) t^{4} .$$
Computing the $J$-invariant of this quartic, and restricting it to the surface $F=0$ yields $e^{-6(a+b)}$, which is nowhere zero. Therefore the condition (4.30) has two linearly independent solutions $H_{0}$ and $H_{1}$ which lead to a non-degenerate frame $e^{00}, e^{01}, e^{10}, e^{11}$ and the conformal structure (4.32) on the four-manifold $X$. It is given by
$$\begin{aligned}
& e^{00}=\left(e^{3 b}-e^{-3 b}\right) d a-\left(e^{3 b}+2 e^{-3 b}\right) d b-i\left(e^{2 a+4 b} d q+\left(1+2 e^{6 b}\right) e^{a-b} d r\right), \quad e^{11}=-\overline{e^{00}} \\
& e^{10}=2 d a+d b+i\left(e^{2 a+b} d q+e^{a+2 b} d r\right), \quad e^{01}=\overline{e^{10}},
\end{aligned}$$
and it gives rise to a metric (4.32). It is possible to chose the conformal factor $\Omega$ such that the resulting metric is ASD and Einstein, with scalar curvature equal to -24
$$\gamma=(d a+2 d b)^{2}+e^{6 b}(d a-d b)^{2}+e^{4 a+8 b} d q^{2}+4 e^{3 a+9 b} d q d r+\left(4 e^{6 b}+1\right) e^{2 a+4 b} d r^{2} .$$
This metric is Kähler, but with opposite orientation: the ASD Kähler two form is
$$\Sigma=e^{2 a+4 b}(d a+2 d b) \wedge d q+e^{5 b+a}(d a+5 d b) \wedge d r .$$
All anti-self-dual Einstein manifolds which are Kähler with opposite orientation have constant holomorphic sectional curvature, i.e. they are diffeomorphic to $\mathbb{C P}^{2}$ with its Fubini-Study metric, its non-compact form $\widetilde{\mathbb{C P}}^{2}=S U(2,1) / U(2)$ with the Bergman metric, or
flat space $\mathbb{C}^{2}$. Our metric has negative scalar curvature so it is the Bergman space $\widetilde{\mathbb{C P}}^{2}$. Setting $y=e^{b-a}, z=e^{-a-2 b}$ puts it in the form
$$\gamma=\frac{1}{z^{2}}\left(z^{2} h_{\mathbb{H}^{3}}+\frac{1}{z^{2}}(d q+2 y d r)^{2}\right), \quad \text { where } \quad h_{\mathbb{H}^{3}}=\frac{d r^{2}+d y^{2}+d z^{2}}{z^{2}},$$
and the 8-dimensional group of isometries can be constructed explicitly. Any ASD Einstein metric with symmetry is conformal to a Kähler metric [10], so (4.48) contains eight Kähler metrics with SD Kähler forms in its conformal class. Only three of these correspond to the tri-Kähler structure arising from conics. Below we shall examine one of these three, and put it in the canonical $S U(\infty)$-Toda form. The conformaly rescaled metric
$$\tilde{\gamma}=e^{-4 a-8 b} \gamma$$
has vanishing scalar curvature, and is Kähler with the 'correct' orientation. The SD Kähler form is
$$\Omega=e^{-2 a-4 b}(d a+2 d b) \wedge d q+3 e^{-3 a-3 b}(d a+d b) \wedge d r .$$
To recognise this metric we shall put it into a general framework of [26]. Any scalar-flat Kähler metric with symmetry can be locally put in the form
$$\tilde{\gamma}=P\left(e^{u}\left(d r^{2}+d y^{2}\right)+d \zeta^{2}\right)+\frac{1}{P}(d q+\alpha)^{2}$$
where $u=u(r, y, \zeta)$ is a solution of the $S U(\infty)$ Toda equation
$$u_{r r}+u_{y y}+\left(e^{u}\right)_{\zeta \zeta}=0,$$
the function $P$ is a solution to the linearised $S U(\infty)$ Toda, and $\alpha$ is a one-form which satisfies the generalised monopole equation. Set $z^{2}=2 \zeta$, and consider $\tilde{\gamma}=4 \zeta^{2} \gamma$, where $\gamma$ is given by (4.49). Then $\tilde{\gamma}$ is of the form (4.50) where $e^{u}=2 \zeta$, and $P=1$.
4.4.2. Towards the flat model. Consider the one-parameter family of solutions
$$F=e^{-2 a}+(p+\kappa r) e^{-a-b}$$
which is a special case of (3.28), and which contains the conformal class (4.48) as the particular case $\kappa=0$. Using the conformal factor $\Omega^{2}=6^{12}\left(e^{6 b}\left(\kappa^{2}+1\right)+1\right) e^{-8 a-6 b}$ gives an ASD Einstein metric with scalar curvature $-24\left(\kappa^{2}+1\right)$. It is Kähler with the opposite orientation, and the ASD Kähler form
$$e^{2 a+4 b}(1+\kappa r)(d a+2 d b) \wedge d q+e^{5 b+a}(d a+5 d b) \wedge d r-3 \kappa e^{6 b} d a \wedge d b .$$
The metric $\hat{\gamma}=e^{-4 a-8 b} \gamma$ is scalar-flat and Kähler. The analytic continuation $(q, r) \rightarrow$ (iq, ir) of this example to imaginary $\gamma$ gives a one parameter family of $S L(3)$-invariant Einstein metrics in neutral signature on $S L(3, \mathbb{R}) / G L(2, \mathbb{R})$. The special case $\kappa=i$ gives a flat metric in neutral signature.
4.4.3. An ASD Ricci-flat example. The most general element of $\operatorname{Ker}(\hat{\square}) \cap \operatorname{Ker}(\triangle+(1 / 12) I d)$ which depends only on $(a, b)$ is given by a special case of (3.28)
$$F=\left(\gamma_{1}+\gamma_{2}(a+2 b)\right) e^{-a-b}+\gamma_{3} e^{-2 a},$$
where $\gamma_{1}, \gamma_{2}, \gamma_{3}$ are constants, and $\gamma_{2} \neq 0$ for $J(d F) \neq 0$. This class is characterised by invariance under the three-dimensional group generated by the Heisenberg algebra $\left(X_{1}, X_{2}, X_{3}\right)$, in (A2).

Translating $(a, b)$ using the 2-parameter group generated by $X_{4}, X_{5}$ in (A2) can be used to set $\gamma_{1}=0$, and an overall rescaling of $F$ allows setting $\gamma_{2}=1$, which leaves a one-parameter family of solutions depending on one constant $\kappa \equiv \gamma_{3}$ which must be non-zero for $J \neq 0$. The four-manifold (4.29) is a hypersurface in $M$ parametrised by
$$a=\frac{1}{3}(s-2 \ln s+2 \ln \kappa), \quad b=\frac{1}{3}(s+\ln s-\ln \kappa) .$$
The ASD conformal structure (4.32) contains the Ricci-flat metric
$$\gamma=(s-1)\left(e^{-2 s} d s^{2}+\kappa^{2} e^{-2 s} d r^{2}+d p^{2}\right)+(s-1)^{-1} \kappa^{2}(d q-p d r)^{2} .$$
The constant $\kappa$ can be set to 1 by rescaling $(q, r)$. Setting $\left(X+i Y=e^{-s+i r}, Z=p\right)$ we recognise this as a Gibbons-Hawking metric
$$\gamma=V\left(d X^{2}+d Y^{2}+d Z^{2}\right)+V^{-1}(d q+\Phi)^{2},$$
where $d V=*_{3} d \Phi$, and the harmonic function $V$ on $\mathbb{R}^{3}$ given by $V=-\ln \left(X^{2}+Y^{2}\right)-1$. Thus we have arrived at the Ooguri-Vafa metric [30] which arises by putting $N$ centres in the ALF Gibbons-Hawking gravitational instanton on a line, and taking a limit when $N \rightarrow \infty$.
4.4.4. A Scalar-flat Kähler example. We shall give one more example, where the barycentre metric (4.47) does not contain either Einstein or Ricci-flat metrics in its conformal class.

Consider
$$F=p e^{-a-b}+r e^{-2 a} .$$
which is (3.28) with $\gamma_{2}=\gamma_{8}=1$, and remaining constants set to zero. The $J$-invariant of the quartic $Q(d F)$ is a constant multiple of $e^{-6 a-6 b} r$. Thus, using $(a, b, r, q)$ as local coordinates on $X$ we expect the conformal class to degenerate on the hyper-surface $r=0$.

The resulting ASD conformal class (4.32) admits three scalar-flat Kähler metrics with Kähler forms given by (4.45). One of these is
$$\gamma=\frac{r}{r^{2}+y^{2}}\left(2 z\left(r^{2}+y^{2}\right)\left(d r^{2}+d y^{2}\right)+d z^{2}\right)+\frac{r^{2}+y^{2}}{r}\left(d q-y^{2} d y+2 r y d r+\frac{y}{r^{2}+y^{2}} d z\right)^{2},$$
where
$$y=\frac{b}{a}, \quad z=\frac{1}{2 a^{2} b^{4}} .$$
The Käher form is given by
$$\Omega=2 d(r y z) \wedge d r+d z \wedge d\left(q-\frac{y^{3}}{3}\right) .$$
The singularity on the $r=0$ surface is a fold in the sense of Hitchin [23]. The points on this surface correspond to twistor curves with normal bundle $\mathcal{O} \oplus \mathcal{O}(2)$. The metric blows up, but the Kähler form remains regular and drops its rank.

Comparing this expression for $\gamma$ with the general form of the scalar-flat Kähler metric with symmetry (4.50) allows us to read-off the corresponding solutions to the $S U(\infty)$ Toda equation, and its linearisation:
$$e^{u}=2 z\left(r^{2}+y^{2}\right), \quad P=\frac{r}{r^{2}+y^{2}} .$$
4.4.5. ASD Einstein cohomogeneity-one metrics. Moraru [27] claims (without giving a proof) that all ASD conformal classes which contain three different Kähler (but not hyper-Kähler) metrics arises from some solution to (3.17).

It is known [35] that all ASD Einstein cohomogeneity-one metrics arise from the Painlevé VI equation with parameters (1/8, -1/8, 1/8, 3/8). This case is actually not transcendental, and all solutions can be expressed in terms of the Weierstrass elliptic function. This is because this particular PVI is related by a Bäcklund transformation [29] to PVI with parameters (0, 0, 0, 1/2) and that case corresponds to a projectively-flat projective structure and has been solved by Picard.

With any symmetry generator we can associate a Kähler scale (by taking the SD derivative), so (if the claim of [27] is right) it should arise from the linear system (3.17), and a contour integral formula. If the Painlevé solution was transcendental it would be a contradiction, but as it is not, it only shows that there is some integral formula for the elliptic functions.

\section*{5. Conics in $\mathbb{C P}^{2}$ from lines in $\mathbb{C P}^{3}$}

The anti-self-dual tri-Kähler metrics arising from Theorem 2 admit twistor spaces which holomorphically fiber over $\mathbb{C P}^{2}$ (this is Moraru's starting point, [27]), and the twistor curves with the normal bundle $\mathcal{O}(1) \oplus \mathcal{O}(1)$ project to the four-parameter family conics in $\mathbb{C P}^{2}$ such that the cohomology class corresponding to the function (3.15) vanishes on this family. Some twistor spaces with this property appeared in [6]. In this Section we shall consider a simple case where the twistor space $\mathbb{C P}^{3} \backslash \mathcal{C}$, where $\mathcal{C} \cong \mathbb{C P}^{1}$ is the rational normal curve. The holomorphic projection to $\mathbb{C P}^{2}$ can in this case be described by classical projective geometry of Poncelet pairs.

In this section we shall use the notation introduced in §2.1.1 and regard $V_{l}=\operatorname{Sym}^{l}\left(\mathbb{C}^{2}\right)$ as $(k+1)$-dimensional representation space of $S L(2, \mathbb{C})$.
5.1. A quadratic map. Consider $\mathbb{C P}^{3}$ as the projectivisation $\mathbb{P}\left(\operatorname{Sym}^{3}\left(\mathbb{C}^{2}\right)\right)$ of the space $V_{3}$ of homogeneous cubic polynomials. We will define a holomorphic projection to $\mathbb{C P}^{2}=$ $\mathbb{P}\left(\operatorname{Sym}^{2}\left(\mathbb{C}^{2}\right)\right)$ by picking three quadrics in $\mathbb{C P}^{3}$ and declaring them to be the homogeneous coordinates on $\mathbb{C P}^{2}$. This triple of quadrics gives a point in $\mathbb{C P}^{2}$ which (perhaps rather confusingly) is identified with a quadric as $\mathbb{C P}^{2}=\mathbb{P}\left(V_{2}\right)$.

Let $\mathcal{C}$ be the rational normal curve in $\mathbb{C P}^{3}$ consisting of all cubics with a triple root $(a x-b y)^{3} \in V_{3}$. Let the quadratic map $Q$ be defined on the complement of the rational normal curve by (in this section we shall use the notation from §2.1.1, but applied to homogeneous polynomials in two variables $[x, y]$ )
$$Q: \mathbb{C P}^{3} \backslash \mathcal{C} \rightarrow \mathbb{C P}^{2}, \quad Q(p)=<p, p>_{2} .$$
Thus in spinor notation (see Appendix), the quadric (a point in $\mathbb{C P}^{2}$ ) corresponding to a cubic $p_{A B C}$ (a point in $\mathbb{C P}^{3} / \mathcal{C}$ ) is $p_{A}{ }^{D E} p_{B D E}$. The map (5.52) is given by a choice of three quadrics in $\mathbb{C P}^{3}$. The choice is not generic, as the zero locus of a generic triple of quadrics in four variables is eight points in $\mathbb{C P}^{3}$, and our triple vanishes on a curve.

In Lemmas 5.1 and 5.2 we shall give two more equivalent characterisations of the map (5.52). In the Lemma 5.1 below we shall make use of the map $\mathbb{C P}^{1} \times \mathbb{C P}^{1} \rightarrow \mathbb{C P}^{2}$ which assigns a quadratic polynomial (up to an overall scale) to a pair of roots, i. e. $\left(\alpha_{A}, \beta_{B}\right) \rightarrow$ $\alpha_{(A} \beta_{B)}$. This is a double covering branched over a conic $\mathcal{B} \subset \mathbb{C P}^{2}$ which is the locus of all
points corresponding to quadratics with a repeated root ${ }^{3}$, i. e.
$$\mathcal{B}=\left\{\left[t^{2}, 2 s t, s^{2}\right], \quad[s, t] \in \mathbb{C P}^{1}\right\} .$$

Lemma 5.1. Any point $p \in \mathbb{C P}^{3} \backslash \mathcal{C}$ lies on a unique secant of $\mathcal{C}$, and thus gives a pair of points on $\mathcal{C}$ (or a tangent in a limiting case). These are the roots of the quadric $Q(p)$.

Proof. Given $p$ not in $\mathcal{C}$, seek two points $(u, v) \in \mathcal{C}$ such that $(p, u, v)$ lie on the same line in $\mathbb{C P}^{3}$. Therefore
$$p_{A B C}=t u_{A} u_{B} u_{C}+s v_{A} v_{B} v_{C}$$
and $Q(p)_{A B}=t s u_{(A} v_{B)}(u \cdot v)^{2}$ which is a quadratic with roots $(u, v)$. The points $(u, v)$ necessarily exist, as given $p$ the equation (5.54) is a system of four equations with four unknowns ( $t, s, u, v$ ). Tangents and secants of $\mathcal{C}$ are pairwise disconnected, so $p$ belongs to a unique secant. For the uniqueness consider
$$u_{A} u_{B} u_{C}+t\left(v_{A} v_{B} v_{C}-u_{A} u_{B} u_{C}\right)=w_{A} w_{B} w_{C}+s\left(k_{A} k_{B} k_{C}-w_{A} w_{B} w_{C}\right),$$
and contract both sides with $u^{(A} v^{B} w^{C)}$. This gives $(k \cdot w)(k \cdot u)(k \cdot w) s=0$. So (if all points are distinct) $s=0$, and then $t=0$.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/25817afe-ea29-49ae-a66c-fdda118de7cd-21.jpg?height=498&width=698&top_left_y=1096&top_left_x=704}
\captionsetup{labelformat=empty}
\caption{Figure 1. Secant of the twisted cubic}
\end{figure} \(\square\)

In Lemma 5.2 we shall regard $V_{3}$ as the 4-dimensional symplectic representation space of $S L(2, \mathbb{C})$.

Lemma 5.2. The map (5.52) is the projectivisation of the moment map for the symplectic $\operatorname{SL}(2, \mathbb{C})$ action on the space of cubics $\mathbb{C}^{4}=\operatorname{Sym}^{3}\left(\mathbb{C}^{2}\right)$.