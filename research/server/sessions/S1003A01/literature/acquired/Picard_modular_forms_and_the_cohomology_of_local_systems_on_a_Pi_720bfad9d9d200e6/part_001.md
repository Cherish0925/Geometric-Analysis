---
retention_scope: session
part: 1
total_parts: 4
---

[Part 1/4 of: Picard modular forms and the cohomology of local systems on a Picard modular surface]

---
source_file: 2012_07673.pdf
converter: mathpix
format: mmd
---

\title{
PICARD MODULAR FORMS AND THE COHOMOLOGY OF LOCAL SYSTEMS ON A PICARD MODULAR SURFACE
}

\author{
JONAS BERGSTRÖM AND GERARD VAN DER GEER
}

\begin{abstract}
We formulate a detailed conjectural Eichler-Shimura type formula for the cohomology of local systems on a Picard modular surface associated to the group of unitary similitudes $\mathrm{GU}(2,1, \mathbb{Q}(\sqrt{-3}))$. The formula is based on counting points over finite fields on curves of genus three which are cyclic triple covers of the projective line. Assuming the conjecture we are able to calculate traces of Hecke operators on spaces of Picard modular forms. We provide ample evidence for the conjectural formula.

Along the way we prove new results on characteristic polynomials of Frobenius acting on the first cohomology group of cyclic triple covers of any genus, dimension formulas for spaces of Picard modular forms and formulas for the numerical Euler characteristics of the local systems.
\end{abstract}

\section*{1. Introduction}

In his 1963 paper [45] Shimura listed a number of arithmetic ball quotients that are rational and that parametrize Jacobians of finite covers of the projective line. This paper deals with one of these cases and tries to use the link with the moduli of curves to study the modular forms on one of these ball quotients. The case at hand is the 2-dimensional ball quotient studied by Picard in the 1880s ([39, 40, 41]) associated to the unitary group in three variables $U(2,1)$ over the field $F=\mathbb{Q}(\sqrt{-3})$. It parametrizes curves of genus 3 that are cyclic covers of degree 3 of the projective line. Around 1979 Shintani considered vector-valued Picard modular forms on such unitary groups in three variables and gave a criterion for such modular forms to be Hecke eigenforms, see [47]. The volume [31] is devoted to showing that the $L$-function of a Picard modular surface is the product of automorphic $L$-functions. But though the literature on automorphic forms on unitary groups is extensive explicit examples are rare. Holzapfel and Feustel studied the rings of scalar-valued modular forms on the group in question, [27, 17], and Finis gave in [18] a list of Hecke eigenforms of weight $\leq 12$ and gave a few Hecke eigenvalues.

We decided to use the interpretation of this ball quotient as a Hurwitz space of cyclic triple covers to investigate the traces of Hecke operators using

\footnotetext{
2010 Mathematics Subject Classification. 11F03, 11G18, 11G20, 14H10, 14G35, 14J15
}
the cohomology of local systems on this moduli space. By counting points on the curves in our family over finite fields we are able to calculate the traces of Frobenius acting on the local systems associated to the cohomology of these curves. We follow the approach initiated in the papers [15, 5] dealing with Siegel modular forms of degree 2 and 3. From the traces of Frobenius on the étale cohomology of our local systems we try to calculate the traces of the Hecke operators on the spaces of vector-valued Picard modular cusp forms.

In the case of modular forms on $\operatorname{SL}(2, \mathbb{Z})$ the basic formula, essentially due to Deligne, expresses the compactly supported cohomology of a local system $\mathbb{V}_{k}$ on the moduli $\mathcal{A}_{1}$ of elliptic curves in terms of the motive $S[k+2]$ of modular forms of weight $k+2$ by an Eichler-Shimura type formula
$$e_{c}\left(\mathcal{A}_{1}, \mathbb{V}_{k}\right)=-S[k+2]-1 .$$
The main goal of this paper is to provide a detailed conjectural analogue of this formula for Picard modular forms for $F$; this formula takes the form
$$e_{c}\left(\mathcal{X}_{\Gamma_{1}[\sqrt{-3}]}, \mathbb{W}_{\lambda}\right)=\breve{S}[n(\lambda)]+e_{\operatorname{extr}}(\lambda),$$
where $\mathbb{W}_{\lambda}$ is a local system, the term $\breve{S}[n(\lambda)]$ is the contribution of genuine Picard modular forms (that have 3-dimensional Galois representations) of weight $n(\lambda)$ and $e_{\text {extr }}(\lambda)$ is a correction term and the analogue of 1 in the earlier formula, but rather complicated due to lifts from smaller groups.

To determine the correction term $e_{\text {extr }}(\lambda)$ we need to substract the contribution of the boundary, the so-called Eisenstein cohomology, essentially determined by Harder [22]. Since we are interested in the genuine Picard modular eigenforms, the forms that are not lifts from smaller groups and come with 3-dimensional Galois representations, we also need to subtract the so-called endoscopic terms. In the case at hand there is a multitude of endoscopic terms and by analyzing the traces that we computed we were able to make a detailed conjectural description of all the endoscopic contributions. Subtracting the Eisenstein contribution and the conjectured endoscopic terms we find heuristically the traces of the Hecke operators on the spaces of genuine Picard modular forms. These are Picard modular forms on the congruence subgroup of level $\sqrt{-3}$ and thus there is a symmetry group, equal to the symmetric group $\mathfrak{S}_{4}$, acting. More precisely, we get traces of Hecke operators $T_{\nu}$ on spaces of Picard modular forms of a given weight for primes $\nu$ in the ring of integers $\mathcal{O}_{F}$ with norm $N(\nu) \equiv_{3} 1$ in a equivariant way, that is, taking into account the $\mathfrak{S}_{4}$-isotypic parts.

The many terms appearing in the correction term $e_{\text {extr }}(\lambda)$ point to the difficulty of getting such detailed results on Picard modular forms using trace formulas, cf. [30].

In order to do this we need to be able to calculate the characteristic polynomial of Frobenius on the étale cohomology $H^{1}\left(C_{f}, \overline{\mathbb{Q}}_{\ell}\right)$ of a curve $C_{f}$ given by $y^{3}=f(x)$ over a finite field in an efficient way. More precisely, we need the characteristic polynomial of Frobenius on the part of the cohomology
where the cyclic Galois automorphism $\alpha$ of order 3 of $C_{f}$ acts by a given third root of one. The formula that we give for the characteristic polynomial for arbitrary genus generalizes a theorem of Gauss dealing with the case of genus 1.

The conjectures in this article are based upon counts of curves together with their characteristic polynomials of Frobenius for prime powers $q \equiv_{3} 1$ with $q \leq 67$. Using this data we can compute traces of Frobenius $F_{q}$ for any local systems $\mathbb{W}_{\lambda}$ (or it is at least computationally very inexpensive). We settled for those of Deligne weight at most 40. In turn this (assuming our conjectures) gave the traces of $T(\nu)$ for $N(\nu) \leq 67$ on the corresponding spaces of Picard cusp forms.

To make such a computation over a finite field of $q$ elements, we need roughly $q$ operations for each curve (to compute the characteristic polynomial) and there are roughly $q^{2}$ points, i.e. curves, in our moduli space (since it is a surface). This tells us that it should be possible to make these computations for significantly larger $q$.

The evidence that we have for the validity of our conjectures is manifold. In this paper we calculate the dimensions of the spaces of modular forms and we calculate the numerical Euler characteristics of the cohomology of our local systems. To begin with, our procedure for calculating the traces of Hecke operators always yields zero when the dimension of cusp forms is zero. Moreover, since we started this project about ten years ago Fabien Cléry and one of us guided by these heuristic data have constructed explicitly vectorvalued modular forms and the results thus obtained in [9] agree with the conjectures. Another striking piece of evidence is provided by congruences of Harder type. Harder predicts congruences modulo primes appearing in the critical values of $L$-series of Hecke characters and we find quite a number of examples of such congruences.

We now sketch the contents of this paper. After recalling the modular surfaces and modular forms and Hecke operators and local systems, we treat the BGG complex for our Shimura variety and use it to describe the Hodge structure on the cohomology of our local systems. We use it to describe the Eisenstein cohomology. After that we calculate the dimensions of spaces of cusp forms on our groups using Riemann-Roch and the holomorphic Lefschetz formula. We then discuss the moduli of abelian threefolds with multiplication by $\mathcal{O}_{F}$ and the moduli of curves of genus three with a cyclic Galois automorphism of order three, including degenerations of such curves. We give a theorem describing the characteristic polynomial of Frobenius on the étale cohomology on cyclic triple covers of the projective line. We introduce the Euler characteristics of our local systems and explain how we carried out the counts on our curves over finite fields. We then state the conjectures on the endoscopic terms. We conclude with many examples of our heuristic results on Picard modular forms and explain the evidence for the correctness
of these results. In particular we list a number of congruences of Harder type.

We intend to make our results available on a website in the style of [7].

\section*{Acknowledgements}

We like to thank Fabien Cléry and Günter Harder for many discussions and Thomas Peternell for a proof of Prop. 3.4. The second author would like to thank the Stockholm University, YMSC of Tsinghua University and the University of Luxembourg for hospitality during work on this paper.

\section*{Contents}
1. Introduction ..... 1
Acknowledgements ..... 4
2. Picard modular surfaces and Picard modular forms ..... 4
3. Cohomology of complex local systems ..... 11
4. The dimension of spaces of Picard modular forms ..... 18
5. Moduli spaces of abelian threefolds with $\rho$-action ..... 22
6. Characteristic polynomials of Frobenius ..... 29
7. Euler characteristics of $\ell$-adic local systems ..... 35
8. Counts over finite fields ..... 39
9. Numeric Euler characteristics of local systems ..... 44
10. Our approach ..... 46
11. Conjectured Lifts ..... 48
12. Conjectures on the cohomology of local systems ..... 52
13. Examples ..... 57
14. Congruences of Harder type ..... 63
References ..... 65

\section*{2. Picard modular surfaces and Picard modular forms}

We will first introduce the complex fibres of our spaces using their interpretation as quotients of a complex 2-ball by an arithmetic group, together with the associated modular forms.
2.1. Picard modular groups and surfaces for the Eisenstein integers. Let $F$ be the number field $\mathbb{Q}(\sqrt{-3})=\mathbb{Q}(\rho)$ with $\rho$ a third root of unity, and with ring of integers $\mathcal{O}_{F}=\mathbb{Z}[\rho]$. Consider the vector space $V=F^{3}$ with non-degenerate hermitian form $h\left(z_{1}, z_{2}, z_{3}\right)=z_{1} z_{2}^{\prime}+z_{1}^{\prime} z_{2}+z_{3} z_{3}^{\prime}$, where the prime refers to the Galois automorphism of $F$. Let $G$ be the corresponding algebraic group defined over $\mathbb{Q}$ of similitudes of $h$
$$G(\mathbb{Q})=\{g \in \mathrm{GL}(3, F): \forall z \in V, h(g z)=\eta(g) h(z) \text { with } \eta(g) \in \mathbb{Q}\} .$$
We have that $\eta^{3}(g)=N_{F / \mathbb{Q}}(\operatorname{det}(g))$ (with $N_{F / \mathbb{Q}}$ the norm) and $\eta$ defines a homomorphism $G \rightarrow \mathbb{G}_{m}$ called the multiplier or similitude norm. This
group is also denoted by $\mathrm{GU}(2,1, F)$ and it is called the group of unitary similitudes of signature (2, 1). The group $G^{0}=\operatorname{ker}(\eta)$, also denoted $\mathrm{U}(2,1, F)$, is the ordinary unitary group and $G^{0} \cap \mathrm{ker}$ det, also denoted $\operatorname{SU}(2,1, F)$, is the special unitary group. If we do a base change to $F$ our group $G$ becomes isomorphic to $\operatorname{GL}(3, F) \times \mathbb{G}_{m}$, where the last factor corresponds to the multiplier $\eta$.

We identify the Picard modular group $G^{0}(\mathbb{Z})$ with $\left\{g \in \operatorname{GL}\left(3, \mathcal{O}_{F}\right):\right.$ $h(g z)=h(z)\}$ and we use the notation
$$\Gamma:=G^{0}(\mathbb{Z}) \quad \text { and } \quad \Gamma_{1}:=G^{0}(\mathbb{Z}) \cap \text { ker det } .$$

The following congruence subgroups play a central role in this paper:
$$\Gamma[\sqrt{-3}]:=\{g \in \Gamma: g \equiv 1(\bmod \sqrt{-3})\}$$
and
$$\Gamma_{1}[\sqrt{-3}]:=\left\{g \in \Gamma_{1}: g \equiv 1(\bmod \sqrt{-3})\right\} .$$
Note that the center of $\Gamma_{1}, \Gamma_{1}[\sqrt{-3}]$ and $\Gamma[\sqrt{-3}]$ equals $\mu_{3}$, while the center of $\Gamma$ is $\mu_{6}$. There are isomorphisms (see also below)
$$\Gamma / \Gamma_{1}[\sqrt{-3}] \cong \mathfrak{S}_{4} \times \mu_{6}, \quad \Gamma_{1} / \Gamma_{1}[\sqrt{-3}] \cong \mathfrak{S}_{4},$$
where the symmetric group $\mathfrak{S}_{4}$ occurs as the special orthogonal group of the $\mathbb{F}_{3}$-vector space $\mathcal{O}_{F}^{3} \subset V$ modulo $(\sqrt{-3})$.

Choose an embedding $\sigma: F \rightarrow \mathbb{C}$ and identify $F \otimes_{\mathbb{Q}} \mathbb{R}$ with $\mathbb{C}$. With this identification we get a 3-dimensional complex vector space $Z=V_{\mathbb{R}}=V \otimes_{\mathbb{Q}} \mathbb{R}$ which is a hermitian space of signature (2, 1). We let $G(\mathbb{R})$ act on $V_{\mathbb{R}}$ as the standard representation. The set of complex lines in $Z$ on which $h$ is negative definite
$$B:=\left\{U \subset Z: \operatorname{dim}(U)=1, h_{\mid U}<0\right\}$$
gives us a complex 2-ball inside $\mathbb{P}(Z)=\mathbb{P}^{2}$. If we set $u=z_{3} / z_{2}$ and $v=z_{1} / z_{2}$ we find an explicit description of this ball,
$$B=\left\{(u, v) \in \mathbb{C}^{2}: v+\bar{v}+u \bar{u}<0\right\} .$$
Any element $g=\left(g_{i j}\right)$ in $G^{+}(\mathbb{R}):=\{g \in G(\mathbb{R}): \eta(g)>0\}$ now acts on $B$ by
$$g \cdot(u, v):=\left(\frac{g_{31} v+g_{32}+g_{33} u}{g_{21} v+g_{22}+g_{23} u}, \frac{g_{11} v+g_{12}+g_{13} u}{g_{21} v+g_{22}+g_{23} u}\right) .$$

All finite index subgroups $\Gamma_{*}$ of $\Gamma$ act properly discontinuously on $B$ and the complex quotient surface $\Gamma_{*} \backslash B$, denoted by $X_{\Gamma_{*}}$, is called a Picard modular surface. Such a quotient is not compact, but can be compactified by adding finitely many points, called cusps, which are the orbits of the group action on the set $\partial B \cap \mathbb{P}^{2}(F)$ of rational points. This is called the Baily-Borel compactification and it will be denoted by $X_{\Gamma_{*}}^{*}$.

In the specific cases that we consider, these Picard modular surfaces have been studied in detail by Holzapfel and Feustel and most of the statements in this section can be found in [27, 28] (see also [17]).

The action of $\Gamma$ on $\partial B \cap \mathbb{P}^{2}(F)$ has only one orbit since the class number of $F$ is 1 , see [48]. The group $\Gamma_{1}[\sqrt{-3}]$ has four cusps and the isomorphism $\Gamma / \Gamma_{1}[\sqrt{-3}] \cong \mathfrak{S}_{4} \times \mu_{6}$ above is given by $g \mapsto(\sigma(g), \operatorname{det}(g))$, where $\sigma(g)$ is the permutation of the four cusps.

The action of $\Gamma_{1}[\sqrt{-3}]$ modulo its center on $B$ is not free, but has three orbits of isolated fixed points. These three points become quotient singularities of the form $\mathbb{C}^{2} / A$ with $A=\left\langle\operatorname{diag}\left(\rho, \rho^{2}\right)\right\rangle \subset \operatorname{GL}(2, \mathbb{C})$ on the surface $X_{\Gamma_{1}[\sqrt{-3}]}$. They can be resolved by a configuration of two non-singular rational curves with self-intersection number -2 intersecting transversally in one point.

The cusps of $X_{\Gamma_{1}[\sqrt{-3}]}^{*}$ are singular points and each cusp singularity can be resolved by an elliptic curve $E=\mathbb{C} / \sqrt{-3} \mathcal{O}_{F}$. All these elliptic curves have self-intersection number -3. We number the cusps by $i=1,2,3,4$ and the resolution curves accordingly by $E_{i}$.

The smooth surface resulting from resolving the quotient and cusp singularities of $X_{\Gamma_{1}[\sqrt{-3}]}^{*}$ is denoted by $Y_{\Gamma_{1}[\sqrt{-3}]}$. Both these spaces admit an action of $\mathfrak{S}_{4} \times \mu_{6}$.

We can define a modular curve on $Y_{\Gamma_{1}[\sqrt{-3}]}$ by considering the embedding of the complex upper half-plane $\mathfrak{H}$ in $B$ by $\tau \mapsto(0, \sqrt{-3} \tau)$ with corresponding embedding of algebraic groups $\mathrm{GL}_{2} \rightarrow G$ given by
$$\left(\begin{array}{cc}
a & b \\
c & d
\end{array}\right) \mapsto\left(\begin{array}{ccc}
a & \sqrt{-3} b & 0 \\
c / \sqrt{-3} & d & 0 \\
0 & 0 & a d-b c
\end{array}\right) .$$
This defines an algebraic curve on $X_{\Gamma_{1}[\sqrt{-3}]}$ isomorphic to $\Gamma_{0}(3) \backslash \mathfrak{H}$. Its closure in $X_{\Gamma_{1}[\sqrt{-3}]}^{*}$ passes through two cusps. Applying the action of $\mathfrak{S}_{4}$ we get a curve $D_{i j}$ on $X_{\Gamma_{1}[\sqrt{-3}]}^{*}$ passing through the cusps $i$ and $j$ for each $1 \leq i<j \leq 4$.

After blow-up, we get the following configuration of curves on $Y_{\Gamma_{1}[\sqrt{-3}]}$.
\begin{itemize}
\item[(i)] Four elliptic curves $E_{i} 1 \leq i \leq 4$ with $E_{i}^{2}=-3$.
\item[(ii)] Six rational curves $D_{i j}$ intersecting $E_{i}$ and $E_{j}$ transversally.
\item[(iii)] Three pairs of rational curves $R_{i j}, R_{k l}$ with $\{i, j, k, l\}=\{1,2,3,4\}$ resolving the quotient singularities, with $D_{i j} R_{i j}=1$ and $D_{i j} R_{k, l}=0$ if $\{k, l\} \neq\{i, j\}$.
\end{itemize}

The surface $X_{\Gamma_{1}[\sqrt{-3}]}^{*}$ can be identified with the 3-fold cover of the hyperplane $x_{1}+x_{2}+x_{3}+x_{4}=0$ in $\mathbb{P}^{3}$ given by
$$\zeta^{3}=\prod_{1 \leq i<j \leq 4}\left(x_{i}-x_{j}\right)$$
with the action of $(\sigma, \pm \rho) \in \mathfrak{S}_{4} \times \mu_{6} \cong \Gamma / \Gamma_{1}[\sqrt{-3}]$ by $x_{i} \mapsto x_{\sigma(i)}$ and $\zeta \mapsto \rho \zeta$. The four cusps correspond to the points with $\zeta=0$ and $\left(x_{1}, x_{2}, x_{3}, x_{4}\right)=$ $(1: 1: 1:-3),(1: 1:-3: 1),(1:-3: 1: 1),(-3: 1: 1: 1)$, and the remaining three singularities to points with $\zeta=0$ and $\left(x_{1}, x_{2}, x_{3}, x_{4}\right)=(1:$
$1:-1:-1),(1:-1: 1:-1),(1: 1: 1:-1)$. The curves $x_{i}=x_{j}$ give the images of the curves $D_{i j}$.

Taking the quotient by $\Gamma[\sqrt{-3}] / \Gamma_{1}[\sqrt{-3}] \cong \mu_{3}$ gives an identification of $X_{\Gamma[\sqrt{-3}]}^{*}$ with $\mathbb{P}^{2}$ as the hyperplane above in $\mathbb{P}^{3}$ with action by $\Gamma / \Gamma[\sqrt{-3}] \cong$ $\mathfrak{S}_{4} \times \mu_{2}$.
2.2. Picard modular forms. Fix a point $x_{0} \in B$ and let $K$ be the stabilizer of $x_{0}$ under the action of $G(\mathbb{R})$. Recall that an automorphy factor is a mapping $J: G(\mathbb{R}) \times B \rightarrow \operatorname{GL}(W)$, with $W$ a complex finite-dimensional vector space, fulfiling a cocycle condition and where $J$ restricted to $K \times x_{0}$ is a representation.

The action of the group $G^{+}(\mathbb{R})$ on $B$ determines two factors of automorphy for $g=\left(g_{i j}\right) \in G^{+}(\mathbb{R})$ and $(u, v) \in B$ given by
$$j_{1}(g, u, v):=g_{21} v+g_{22}+g_{23} u$$
and
$$j_{2}(g, u, v):=\operatorname{det}(g)^{-1}\left(\begin{array}{ll}
G_{32} u+G_{33} & G_{32} v+G_{31} \\
G_{12} u+G_{13} & G_{12} v+G_{11}
\end{array}\right)$$
with $G_{i j}$ the minor of $g_{i j}$, see [46]. Note that
$$\operatorname{det}\left(j_{2}(g, u, v)\right)=j_{1}(g, u, v) \cdot(\operatorname{det}(g))^{-1}$$
and that the transpose of the Jacobian of the action of $G^{+}(\mathbb{R})$ on $B$ is given by
$$j_{1}(g, u, v)^{-1} j_{2}(g, u, v)^{-1} .$$
Let $(j, k)$ be a pair of integers with $j \geq 0$. Define a slash operator on functions $f: B \rightarrow \operatorname{Sym}^{j}\left(\mathbb{C}^{2}\right)$ for $g \in G^{+}(\mathbb{R})$ via
$$\left(f_{\mid j, k} g\right)(u, v):=j_{1}(g, u, v)^{-k} \operatorname{Sym}^{j}\left(j_{2}(g, u, v)^{-1}\right) f(g \cdot(u, v)) .$$

For any finite index subgroup $\Gamma_{*}$ in $\Gamma$ and character $\chi$ of finite order on $\Gamma_{*}$, we define the vector space of modular forms of weight $(j, k)$ and character $\chi$ on $\Gamma_{*}$ by
$$M_{j, k}\left(\Gamma_{*}, \chi\right):=\left\{f: B \rightarrow \operatorname{Sym}^{j}\left(\mathbb{C}^{2}\right): f \text { holomorphic, } \forall g \in \Gamma_{*}, f_{\mid j, k} g=\chi(g) f\right\} .$$
The space of cusp forms of weight $(j, k)$ and character $\chi$ on $\Gamma_{*}$ will be denoted by $S_{j, k}\left(\Gamma_{*}, \chi\right)$. Only the characters that are a power of $\operatorname{det}(g)$ will be considered in this paper. We will just write $M_{j, k}\left(\Gamma_{*}\right)$, or $S_{j, k}\left(\Gamma_{*}\right)$, when $\chi$ is trivial. For more details we refer to [9] and the references therein.

Alternatively, we could define another automorphy factor
$$j_{3}(g, u, v):=\operatorname{det}(g)$$
and a new slash operator
$$\left(f_{\mid j, k, l} g\right)(u, v):=j_{1}(g, u, v)^{-k} \operatorname{Sym}^{j}\left(j_{2}(g, u, v)^{-1}\right) j_{3}(g, u, v)^{-l} f(g \cdot(u, v))$$
with corresponding spaces of modular forms $M_{j, k, l}\left(\Gamma_{*}\right)=M_{j, k}\left(\Gamma_{*}, \operatorname{det}^{l}\right)$ and cusp forms $S_{j, k, l}\left(\Gamma_{*}\right)=S_{j, k}\left(\Gamma_{*}, \operatorname{det}^{l}\right)$.

The group $\Gamma[\sqrt{-3}] / \Gamma_{1}[\sqrt{-3}] \cong \mu_{3}$ (generated by $\operatorname{diag}(1,1, \rho)$ ) acts on $M_{j, k}\left(\Gamma_{1}[\sqrt{-3}]\right)$. This action is reflected in a decomposition of $M_{j, k}\left(\Gamma_{1}[\sqrt{-3}]\right)$ as a sum of spaces of modular forms with character
$$M_{j, k}(\Gamma[\sqrt{-3}]) \oplus M_{j, k}(\Gamma[\sqrt{-3}], \operatorname{det}) \oplus M_{j, k}\left(\Gamma[\sqrt{-3}], \operatorname{det}^{2}\right) .$$

Remark 2.1. Note that $M_{j, k}\left(\Gamma_{1}[\sqrt{-3}]\right)=\{0\}$ if $j \not \equiv_{3} k$. Moreover, we have $M_{j, k}\left(\Gamma[\sqrt{-3}], \operatorname{det}^{\ell}\right)=S_{j, k}\left(\Gamma[\sqrt{-3}], \operatorname{det}^{\ell}\right)$ if $\ell \not \equiv_{3} j$, see [9, Prop. 5.1].

The rings of scalar-valued modular forms on $\Gamma[\sqrt{-3}]$ and $\Gamma_{1}[\sqrt{-3}]$ were determined by Holzapfel and Feustel ([27, 17]).

Proposition 2.2. We have
$$\oplus_{k=0}^{\infty} M_{0,3 k}(\Gamma[\sqrt{-3}])=\mathbb{C}\left[x_{1}, x_{2}, x_{3}, x_{4}\right] /\left(x_{1}+x_{2}+x_{3}+x_{4}\right),$$
where $x_{1}, x_{2}, x_{3}, x_{4}$ are modular forms of weight 3 , and the group $\mathfrak{S}_{4}$ acts on these modular forms by $\sigma: x_{i} \mapsto \operatorname{sgn}(\sigma) x_{\sigma(i)}$. The ring $\oplus_{k=0}^{\infty} M_{0,3 k}\left(\Gamma_{1}[\sqrt{-3}]\right)$ is the ring extension of $\oplus_{k=0}^{\infty} M_{0,3 k}(\Gamma[\sqrt{-3}])$ by the element
$$\zeta \in M_{0,6}(\Gamma[\sqrt{-3}], \operatorname{det})$$
satisfying the equation (2.1) and where $\mathfrak{S}_{4}$ acts on $\zeta$ by the sign representation.

Since $X_{\Gamma_{1}[\sqrt{-3}]}^{*} \cong \operatorname{Proj}\left(\oplus_{k=0}^{\infty} M_{0,3 k}\left(\Gamma_{1}[\sqrt{-3}]\right)\right)$ we retrieve the identification of $X_{\Gamma_{1}[\sqrt{-3}]}^{*}$ with $\mathbb{P}^{2}$ given at the end of Section 2.1, see [27]. We point out that the $x_{i}$ have $F$-integral Fourier-Jacobi expansions, see [18, 9].

Proposition 2.3. If $k<0$ and $j \geq 0$ then $\operatorname{dim} M_{j, k}\left(\Gamma_{1}[\sqrt{-3}]\right)=0$.
Proof. If one develops a vector-valued modular form $f \in M_{j, k}\left(\Gamma_{1}[\sqrt{-3}]\right)$ along the modular curve given in Section 2.1 then the first component of the vector $f(0, \sqrt{-3} \tau)$ is a modular form on $\Gamma_{1}(3) \subset \mathrm{SL}_{2}(\mathbb{Z})$ of weight $k$, see [9, Prop. 8.4], and hence it is zero. The same thing happens for other modular curves. Curves parametrized by $\mathfrak{H} \rightarrow B, \tau \mapsto(a, \sqrt{-3} \tau)$ with $a \in F$ yield modular curves and restricting modular forms $M_{j, k}\left(\Gamma_{1}[\sqrt{-3}]\right)$ leads to modular forms of negative weight on congruence subgroups of $\operatorname{SL}(2, \mathbb{Z})$, and these are zero. Since these curves lie dense, we see that the first component of $f(u, \sqrt{-3} \tau)$ is zero for all $u, \tau$. Applying the invariance of modular forms under the unipotent radical of a parabolic subgroup, see [9, Eq. 4], we find that all components vanish. \(\square\)

Remark 2.4. The proof can be easily adapted to show that the proposition holds for any finite index subgroup $\Gamma_{*}$ of $\Gamma$.
2.3. Hecke Operators. The Hecke rings for the arithmetic group $\Gamma_{1}$ and $\Gamma_{1}[\sqrt{-3}]$ were studied by Shintani [47] and Finis [18]. Outside the prime 3 these Hecke rings are the same and they are generated by elements $T(\nu)$, $T(\nu, \nu)$ for elements $\nu \in \mathcal{O}_{F}$ with norm $N(\nu)=p$ for primes $p \equiv_{3} 1$ and elements $T(p)$ and $T(p, p)$ for primes $p \equiv_{3} 2$. For $\Gamma_{1}$ we also have elements
$T(\sqrt{-3})$ and $T(\sqrt{-3}, \sqrt{-3})$. We refer to Finis' paper and to [9] for a description of the Hecke rings and the action on modular forms. Note that for a Hecke eigenform with eigenvalues $\lambda_{\nu}$ we have $\lambda_{\bar{\nu}}=\bar{\lambda}_{\nu}$.

We define for $\nu \in \mathcal{O}_{F}$ with norm a prime $p \equiv_{3} 1$ and given weight $(j, k)$ the polynomial
$$Q_{\nu}^{j, k}(X, \lambda)=1-\lambda X+\nu^{j+1} \bar{\nu}^{k-2} \bar{\lambda} X^{2}-\nu^{2 j+k} \bar{\nu}^{j+2 k-3} X^{3}$$
and for a prime $p \equiv_{3} 2$ we define $Q_{-p}^{j, k}(X, \lambda)$ by
$$\left(1-\left(\lambda-(p-1)(-p)^{j+k-3}\right) X+p^{2 j+2 k-2} X^{2}\right)\left(1-(-p)^{j+k-1} X\right)$$
The local factor of the $L$-function of a Picard modular form $f$ of weight $(j, k)$ that is an eigenform for the Hecke algebra with eigenvalue $\lambda_{\nu}(f)$ for $T(\nu)$ with $N(\nu)=p \equiv_{3} 1$ equals the inverse of $Q_{\nu}^{j, k}\left(N(\nu)^{-s}, \lambda_{\nu}(f)\right)$, while for a prime $p \equiv_{3} 2$ the local factor is the inverse of $Q_{-p}^{j, k}\left(N(p)^{-s}, \lambda_{-p}(f)\right)$.
2.4. Modular forms as sections of automorphic vector bundles. In this section we will realize our modular forms as sections of some vector bundles. We will use the interpretation of $B$ as the Grassmann variety of negative lines in $Z=V_{\mathbb{R}}$. This interpretation provides $B$ with two vector bundles $T$ and $S$ fitting in an exact sequence
$$0 \rightarrow T \rightarrow B \times Z \rightarrow S \rightarrow 0,$$
where $T$ is the tautological line bundle that associates to a point of $B$ the negative line it represents, and $S$ is the tautological quotient bundle of rank 2. The tangent bundle to $B$ is given by $\operatorname{Hom}(T, S)=S \otimes T^{-1}$, so the cotangent bundle $\Omega_{B}^{1}$ equals $S^{\vee} \otimes T$.

Let $\Gamma^{\prime}$ be a freely acting finite index subgroup of $\Gamma$. Put $X=X_{\Gamma^{\prime}}=$ $\Gamma^{\prime} \backslash B$. Let $X^{*}=X_{\Gamma^{\prime}}^{*}$ denote the Baily-Borel compactification of $X_{\Gamma^{\prime}}$ and $Y=Y_{\Gamma^{\prime}}$ its minimal resolution. The cotangent bundle $\Omega_{X}^{1}$ is then equal to the quotient $\Gamma^{\prime} \backslash\left(S^{\vee} \otimes T\right)$. Let $D$ denote the resolution divisor on $Y$ of the cusps of $X^{*}$. Mumford's canonical extension of $\Omega_{X}^{1}$ extends to $\Omega_{Y}^{1}(\log D)$ on $Y$, see [38, Prop. 3.4]. The bundle on $X$ defined by $\Gamma^{\prime} \backslash S^{\vee}$ will be denoted by $U$ and the bundle $\Gamma^{\prime} \backslash T$ by $L$. With abuse of notation their canonical extensions to $Y$ will be denoted with the same letters.

If we choose a base point $x_{0}=\left(u_{0}, v_{0}\right) \in B$, then $B$ can be identified with $G^{0}(\mathbb{R}) / K^{0}$, where the maximal compact subgroup $K^{0} \cong U(2) \times U(1)$ is the stabilizer of $x_{0}$. Choosing instead a line in $Z$ for which $h$ is negative definite, then if $K$ is the stabilizer in $G$ of the line spanned by $x_{0}$ we find that $K \cong \mathbb{C}^{*} \cdot K^{0}$ and that $B \cong G(\mathbb{R}) / K$.

For each finite-dimensional complex representation $\lambda: K \rightarrow \operatorname{GL}(W)$ we get an automorphic vector bundle $\mathcal{W}_{\lambda}$ by $G(\mathbb{R}) \times_{K} W \rightarrow B$ where $(g, w)$ is identified with $(g k, \lambda(k) w)$ for all $g \in G(\mathbb{R}), w \in W$ and $k \in K$. The group $G(\mathbb{R})$ acts naturally on the left by $g^{\prime} .(g, w)=\left(g^{\prime} g, v\right)$. After taking the quotient by $\Gamma^{\prime}$ we get an automorphic vector bundle $\mathcal{W}_{\lambda}$ on $X$. These
vector bundles extend canonically to $Y$, and will be denoted with the same letters.

Recall from Section 2.2 that an automorphy factor $J$, when restricted to $K \times x_{0}$, is a representation $\lambda$, and so $J$ determines a trivialization of $\mathcal{W}_{\lambda}$ by $\Phi_{J}: G(\mathbb{R}) \times_{K} W \rightarrow B \times W$ with $(g, w) \mapsto\left(g x_{0}, J\left(g, x_{0}\right) w\right)$. The global sections of the bundle $\mathcal{W}_{\lambda}$ on $Y$ can be identified with the modular forms transforming with the automorphy factor $J$. It follows directly from our definitions that the bundle $L$ comes with a trivialization given by the automorphy factor $j_{1}$. As mentioned in Section 2.1, the Jacobian of the action of $G(\mathbb{R})$ of $B$ is by $j_{1}^{-1} j_{2}^{-1}$. Taking the dual and tensoring with $L^{-1}$ gives that $U$ has a trivialization given by $j_{2}$. Finally, we find that the bundle $R:=\operatorname{det}(U)^{-1} \otimes L$ corresponds to the automorphy factor $j_{3}$. In summary, the relations between vector bundles and automorphy factors are as follows
$$L \leftrightarrow j_{1}, \quad U \leftrightarrow j_{2}, \quad R \leftrightarrow j_{3},$$
and moreover
$$\operatorname{det}(U)=L \otimes R^{-1}, \quad U^{\vee} \cong U \otimes L^{-1} \otimes R .$$

Definition 2.5. For integers $j, k, l$ with $j \geq 0$ we put
$$\mathcal{W}_{j, k, l}:=\operatorname{Sym}^{j}(U) \otimes L^{k} \otimes R^{l} .$$

We then get the following interpretation of modular forms.
Proposition 2.6. For integers $j, k, l$ with $j \geq 0$, we have that
$$M_{j, k, l}\left(\Gamma^{\prime}\right)=H^{0}\left(Y_{\Gamma^{\prime}}, \mathcal{W}_{j, k, l}\right),$$
and
$$S_{j, k, l}\left(\Gamma^{\prime}\right)=H^{0}\left(Y_{\Gamma^{\prime}}, \mathcal{W}_{j, k, l} \otimes \mathcal{O}(-D)\right) .$$

Furthermore, we have that $\Omega_{X}^{1}(\log D) \cong U \otimes L$. The canonical extension of the canonical bundle $\Omega_{X}^{2}$ equals on the one hand $\Omega_{Y}^{2}(D)$ and on the other hand, by a local calculation or since the canonical extension commutes with exterior products (see [16, p. 225]), it equals $\operatorname{det}\left(\Omega_{X}^{1}(\log D)\right)$. We thus find
$$\Omega_{Y}^{1}(\log D) \cong U \otimes L, \quad \Omega_{Y}^{2}(D) \cong L^{3} \otimes R^{-1} .$$

The subgroups of $\Gamma$ that we are mainly considering do not act freely on $B$. An automorphic vector bundle $\mathcal{W}_{\lambda}$ on $B$ will become a vector bundle on $X$ precisely if the stabilizer of any point $x \in B$ acts trivially on the fibre $\left(\mathcal{W}_{\lambda}\right)_{x}$. Let us consider the group $\Gamma_{1}[\sqrt{-3}]$. The center of $\Gamma_{1}[\sqrt{-3}]$ is generated by $\rho \cdot 1_{3}$, and since $j_{1}\left(\rho \cdot 1_{3}, u, v\right)=\rho, j_{2}\left(\rho \cdot 1_{3}, u, v\right)=\rho^{2} \cdot 1_{2}$, $j_{3}\left(\rho \cdot 1_{3}, u, v\right)=1$, a necessary condition for $\mathcal{W}_{j, k, l}$ to be vector bundle on $X_{\Gamma_{1}[\sqrt{-3}]}$ is that $j \equiv_{3} k$. The stabilizer of one the three singular points $x$ in $B$ is generated by a matrix $g_{x}$ with eigenvalues $1, \rho, \rho^{2}$ such that $j_{1}\left(g_{x}, x\right)=\rho$ and $j_{2}\left(g_{x}, x\right)=\operatorname{diag}(\rho, 1)$ and $j_{3}\left(g_{x}, x\right)=1$ so $\mathcal{W}_{\lambda}$ is only a vector bundle on $X_{\Gamma_{1}[\sqrt{-3}]}$ if $j=0$ and $k \equiv_{3} 0$.

To treat the cases of non-freely acting groups we can replace the group by a freely acting finite index normal subgroup and then take invariants. By the Koecher principle, these forms extend to holomorphic sections of $\operatorname{Sym}^{j}(U) \otimes L^{k} \otimes R^{l}$ over the cusp resolutions. Also the quotient singularities pose no problem. Therefore, the identities of (2.2), (2.3) still hold on $\Gamma[\sqrt{-3}]$ and $\Gamma_{1}[\sqrt{-3}]$.

Remark 2.7. Proposition 2.3 together with (2.3) shows that
$$H^{0}\left(Y_{\Gamma[\sqrt{-3}]}, \mathcal{W}_{j, k, l} \otimes \mathcal{O}(-D)\right)=0$$
for any $j, l \geq 0$ and $k<0$. This argument is easily generalizable to other Picard modular surfaces and other arithmetic subgroups. Compare with the vanishing results of [36, 37].

\section*{3. Cohomology of complex local systems}

In this section we introduce the local systems of interest to us and we use the BGG-complex to find information about the cohomology of these local systems.
3.1. Local systems and roots. A vector bundle $\mathcal{W}_{\lambda}$, as defined in the previous section, is a local system, i.e. locally constant, if the representation $\lambda$ is a restriction of a representation of $G(\mathbb{R})$.

We have the local system $\mathbb{W}$ on $X_{\Gamma_{*}}$ coming from the dual of the standard representation of $G(\mathbb{R})$ acting on $V_{\mathbb{R}}$, as in the beginning of Section 2.4. In terms of an automorphy factor $J$, the local systems are the ones for which $J(g, x)$ are independent of $x$. The bundle $R$ is thus a local system and we find that it is isomorphic to $\wedge^{3} \mathbb{W}$. It is constant for any $\Gamma_{*}$ that is a subgroup of $\Gamma_{1}$ and since $\Gamma_{1} / \Gamma \cong \mu_{6}$ we see that $\left(\wedge^{3} \mathbb{W}\right)^{6} \cong R^{6}$ is constant for subgroups of $\Gamma$.

The representation theory of $G$ and $K$ over the complex numbers in terms of roots and highest weights will be important for the construction of the BGG-complex which we will use in Section 3.2.

Note first that the base change of $G$ to $\mathbb{C}$ is isomorphic to $\operatorname{GL}(3, \mathbb{C}) \times \mathbb{G}_{m}$, where the last factor corresponds to the multiplier $\eta$.

Let $Q$ be a maximal parabolic subgroup and $Q=M \ltimes \mathcal{U}$ a Levi decomposition with $\mathcal{U}$ the unipotent radical of $Q$. The complexification of $K$, namely $\operatorname{GL}(2, \mathbb{C}) \times \operatorname{GL}(1, \mathbb{C})$, is conjugate to that of $M$.

Let $T$ be the maximal torus of $G$ of diagonal matrices $g=\operatorname{diag}\left(a_{1}, a_{2}, a_{3}\right)$ with $a_{i} \in F^{*}$ satisfying $a_{1} a_{2}^{\prime}=a_{1}^{\prime} a_{2}=a_{3} a_{3}^{\prime}=\eta(g) \in \mathbb{Q}^{*}$. We have the characters $L_{i}: g \mapsto a_{i}$. The roots are $\pm\left(L_{1}-L_{2}\right), \pm\left(L_{1}-L_{3}\right), \pm\left(L_{2}-L_{3}\right)$. We can view $\alpha=L_{1}-L_{2}$ and $\beta=L_{2}-L_{3}$ as two simple roots and a system of fundamental weights is $\gamma_{1}=L_{1}$ and $\gamma_{2}=L_{1}+L_{2}$ and $\gamma_{3}=L_{1}+L_{2}+L_{3}$.

Then $\Phi_{G}^{+}=\{\alpha, \beta, \alpha+\beta\}$ is a system of positive roots, occurring in the adjoint action on the unipotent radical $\mathcal{U}$ and we can take $\Phi_{M}^{+}=\{\alpha\}$.

The Weyl group $W_{G}$ of $G$ is generated by the reflections $s_{\alpha}$ and $s_{\beta}$ which act on the fundamental weights by
$$s_{\alpha}:\left\{\begin{array}{l}
\gamma_{1} \mapsto \gamma_{2}-\gamma_{1} \\
\gamma_{2} \mapsto \gamma_{2} \\
\gamma_{3} \mapsto \gamma_{3},
\end{array} \quad s_{\beta}:\left\{\begin{array}{l}
\gamma_{1} \mapsto \gamma_{1}, \\
\gamma_{2} \mapsto \gamma_{1}-\gamma_{2}+\gamma_{3} \\
\gamma_{3} \mapsto \gamma_{3} .
\end{array}\right.\right.$$
Then put $\theta=s_{\alpha} s_{\beta} s_{\alpha}=s_{\beta} s_{\alpha} s_{\beta}$ with $\theta(\alpha)=-\beta$ and $\theta(\beta)=-\alpha$ and
$$\theta\left(n_{1} \gamma_{1}+n_{2} \gamma_{2}+n_{3} \gamma_{3}\right)=-n_{2} \gamma_{1}-n_{1} \gamma_{2}+\left(n_{1}+n_{2}+n_{3}\right) \gamma_{3} .$$

The Weyl group $W_{M}$ equals $\left\langle s_{\alpha}\right\rangle$. Define
$$W^{M}:=\left\{w \in W_{G}: \Phi_{M}^{+} \subset w\left(\Phi_{G}^{+}\right)\right\} .$$
We find that $W^{M}=\left\{1, s_{\beta}, s_{\beta} s_{\alpha}\right\}$. Put $\delta:=\alpha+\beta=\gamma_{1}+\gamma_{2}-\gamma_{3}$, which is half the sum of the positive roots. We have an involution on $W^{M}$ given by $w \mapsto s_{\alpha} w \theta$ with $s_{\alpha}$ and $\theta$ the elements of longest length in $W_{M}$ and $W_{G}$.

For an element $w$ in the Weyl group and a weight $\lambda$ we define an action by
$$w * \lambda:=w(\lambda+\delta)-\delta .$$

For each weight $\lambda=n_{1} \gamma_{1}+n_{2} \gamma_{2}+n_{3} \gamma_{3}$ we get an irreducible finite-dimensional complex representation of $G$ with highest weight $\lambda$. The corresponding local system on $X_{\Gamma_{*}}$ will be denoted by $\mathbb{W}_{\lambda}=\mathbb{W}_{n_{1}, n_{2}, n_{3}}$ and it can be found inside
$$\operatorname{Sym}^{n_{1}}(\mathbb{W}) \otimes \operatorname{Sym}^{n_{2}}\left(\wedge^{2} \mathbb{W}\right) \otimes \operatorname{Sym}^{n_{3}}\left(\wedge^{3} \mathbb{W}\right) .$$
For the same weight $\lambda$ we get an irreducible finite-dimensional complex representation of $K$. To identify this representation we consider the automorphy factors for a diagonal matrix $g$, and we then find that $j_{1}$ corresponds to $\gamma_{1}$, $j_{3}$ corresponds to $\gamma_{3}$ and $j_{2}$ to $\gamma_{2}-\gamma_{3}$. The vector bundle correponding to $\lambda$ is thus $\mathcal{W}_{n_{2}, n_{1}, n_{2}+n_{3}}$ in the notation of Section 2.4. Note that the cotangent bundle $U \otimes L$ has highest weight $\delta=\alpha+\beta$. A weight $\lambda$ will be called regular if $n_{1}>0$ and $n_{2}>0$.

We will return to these local systems and vector bundles in terms of the moduli interpretation of our Picard modular surfaces in Section 7.
3.2. The BGG-complex. We will here apply the methods of Faltings and Chai [16, Ch. VI] to our situation, especially the theory exposed on pages 228 to 237. For a given local system one obtains a complex of vector bundles, called the dual BGG complex, with differentials that are differential operators between vector bundles. It is obtained as a direct summand of the de Rham complex of the local system.

Let $\Gamma_{*}$ be a finite index subgroup of $\Gamma$, and let $\Gamma^{\prime}$ be a normal finite index subgroup of $\Gamma_{*}$ that acts freely on $B$. As above, consider the surface $Y_{\Gamma^{\prime}}$ that is the minimal resolution of the cusp singularities of the Baily-Borel compactification of $X_{\Gamma^{\prime}}=\Gamma^{\prime} \backslash B$ with resolution divisor $D$. Let the inclusion of $X_{\Gamma^{\prime}}$ in $Y_{\Gamma^{\prime}}$ be denoted by $j$.

The BGG-complex that the methods of [16] give for a local system $\mathbb{W}_{\lambda}$ on $X_{\Gamma^{\prime}}$ is $K_{\lambda}^{\bullet}$ with
$$K_{\lambda}^{q}=\oplus_{w \in W^{M}, \ell(w)=q} \mathcal{W}_{w * \lambda}^{\vee} .$$
The vector bundles $\mathcal{W}_{\xi}$ extend canonically over the cusp resolutions and the differential operators do as well. We denote the resulting complex on $Y_{\Gamma^{\prime}}$ by $\bar{K}_{\lambda}^{\bullet}$.

Proposition 3.1. Let $\lambda=n_{1} \gamma_{1}+n_{2} \gamma_{2}+n_{3} \gamma_{3}$. The dual BGG-complex
$$\begin{aligned}
\operatorname{Sym}^{n_{1}}(U) \otimes L^{-n_{1}-n_{2}} \otimes R^{n_{1}+n_{2}+n_{3}} & \rightarrow \operatorname{Sym}^{n_{1}+n_{2}+1}(U) \otimes L^{-n_{1}+1} \otimes R^{n_{1}+n_{2}+n_{3}} \\
& \rightarrow \operatorname{Sym}^{n_{2}}(U) \otimes L^{n_{1}+3} \otimes R^{n_{2}+n_{3}-1} \rightarrow 0
\end{aligned}$$
is quasi-isomorphic to $R j_{*} \mathbb{W}_{\lambda}$. Similarly, $R j_{!} \mathbb{W}_{\lambda}$ is quasi-isomorphic to the dual $B G G$-complex tensored with $\mathcal{O}(-D)$.

Proof. This follows as in [16, Proposition 5.4]. Taking the dual corresponds to applying $-\theta$ to $\lambda$ and then $W_{M}$ changes to $W_{M^{\prime}}=\left\langle s_{\beta}\right\rangle$. We thus consider the triples representing $w *(-\theta(\lambda))$ for $w \in W^{M^{\prime}}$. These are $\left(n_{2}, n_{1},-n_{1}-\right.$ $\left.n_{2}-n_{3}\right),\left(-n_{2}-2, n_{1}+n_{2}+1,-n_{1}-n_{2}-n_{3}\right)$ and $\left(n_{1}-n_{2}-3, n_{2},-n_{2}-n_{3}+1\right)$. Taking the duals of the resulting $\mathcal{W}_{\mu}$ gives the result. \(\square\)

For the case $n_{1}=n_{2}=n_{3}=0$ we get the usual logarithmic de Rham complex $\Omega^{\bullet}(\log D)$.

Remark 3.2. The dual of $\mathbb{W}_{\lambda}$ with $\lambda=n_{1} \gamma_{1}+n_{2} \gamma_{2}+n_{3} \gamma_{3}$ corresponds to $-\theta(\lambda)=n_{2} \gamma_{1}+n_{1} \gamma_{2}+\left(-n_{1}-n_{2}-n_{3}\right) \gamma_{3}$. The Serre dual of $\mathcal{W}_{\mu}=$ $\operatorname{Sym}^{a}(U) \otimes L^{b} \otimes R^{c}$ is
$$\operatorname{Sym}^{a}(U) \otimes L^{-a-b+3} \otimes R^{a-c-1} \otimes \mathcal{O}(-D) .$$
The Serre duals of the terms occurring in the BGG complex for $j_{*} \mathbb{W}_{\lambda}$ occur in reverse order in the BGG complex of $j!\mathbb{W}_{-\theta(\lambda)}$.

Put $|\lambda|:=n_{1}+2 n_{2}+3 n_{3}$. From [16, Theorem 5.5] it follows that $H^{i}\left(X_{\Gamma^{\prime}}, \mathbb{W}_{\lambda}\right)$ has a Hodge structure of weight $\geq i+|\lambda|$ and the compactly supported cohomology $H_{c}^{i}\left(X_{\Gamma^{\prime}}, \mathbb{W}_{\lambda}\right)$ has a Hodge structure of weight $\leq$ $i+|\lambda|$. We also get the following.

Proposition 3.3. For $\lambda=n_{1} \gamma_{1}+n_{2} \gamma_{2}+n_{3} \gamma_{3}$, we have a Hodge filtration on $H_{c}^{i}\left(X_{\Gamma^{\prime}}, \mathbb{W}_{\lambda}\right)$ equal to
$$F^{n_{1}+n_{2}+n_{3}+2} \subset F^{n_{2}+n_{3}+1} \subset F^{n_{3}}$$
and the graded pieces can be identified with
$$\begin{aligned}
& H^{i-2}\left(Y_{\Gamma^{\prime}}, \operatorname{Sym}^{n_{2}}(U) \otimes L^{n_{1}} \otimes R^{n_{2}+n_{3}} \otimes \Omega_{Y}^{2}\right), \\
& H^{i-1}\left(Y_{\Gamma^{\prime}}, \operatorname{Sym}^{n_{1}+n_{2}}(U) \otimes L^{-n_{1}} \otimes R^{n_{1}+n_{2}+n_{3}} \otimes \Omega_{Y}^{1}\right), \\
& H^{i}\left(Y_{\Gamma^{\prime}}, \operatorname{Sym}^{n_{1}}(U) \otimes L^{-n_{1}-n_{2}} \otimes R^{n_{1}+n_{2}+n_{3}} \otimes \mathcal{O}(-D)\right) .
\end{aligned}$$

For $i=2$ we see that the first step of the Hodge filtration is isomorphic to the space of cusp forms
$$S_{n_{2}, n_{1}+3, n_{2}+n_{3}-1}\left(\Gamma^{\prime}\right) .$$
But note that we want this space of cusp forms to have Hodge weight $n_{1}+$ $n_{2}+2$ and the discrepancy is due to a "twisting" that will be described further in Section 7.3.1.

We define the inner cohomology $H_{!}^{i}\left(X_{\Gamma^{\prime}}, \mathbb{W}_{\lambda}\right)$ as the image under the natural map of $H_{c}^{i}\left(X_{\Gamma^{\prime}}, \mathbb{W}_{\lambda}\right)$ in $H^{i}\left(X_{\Gamma^{\prime}}, \mathbb{W}_{\lambda}\right)$. It follows that the inner cohomology will have a pure Hodge structure of weight $|\lambda|+i$. By results of Ragunathan, Li-Schwermer and Saper [42, 35, 43] for regular $\lambda$ (that is $n_{1}>0$ and $n_{2}>0$ ) we know that $H_{!}^{i}\left(X_{\Gamma^{\prime}}, \mathbb{W}_{\lambda}\right) \neq 0$ implies $i=2$.

Note that by taking invariants under $\Gamma_{*} / \Gamma^{\prime}$, all results in this section hold also for $\Gamma^{\prime}$ replaced by $\Gamma_{*}$. In particular they hold for $\Gamma_{*}$ equal to $\Gamma[\sqrt{-3}]$ or $\Gamma_{1}[\sqrt{-3}]$.
3.3. The neighborhood of a cusp. For a freely acting finite index normal subgroup $\Gamma^{\prime}$ of $\Gamma_{1}[\sqrt{-3}]$, each cusp of $X_{\Gamma^{\prime}}^{*}$ is resolved by an elliptic curve and the quotient group $\Gamma / \Gamma^{\prime}$ acts transitively on the set of cusps. Therefore it suffices to look at the cusp at infinity represented by $(1: 0: 0) \in B$. The isotropy group $\Gamma_{\infty}$ of this cusp in $\Gamma$ consists of elements in $\Gamma$ of the form
$$\left(\begin{array}{ccc}
t_{1} & & \\
& t_{2} & \\
& & t_{3}
\end{array}\right)\left(\begin{array}{ccc}
1 & x & -y^{\prime} \\
0 & 1 & 0 \\
0 & y & 1
\end{array}\right)$$
satisfying the conditions $t_{1} t_{2}^{\prime}=t_{3} t_{3}^{\prime}$ and $x+x^{\prime}=-y y^{\prime}$. For the groups $\Gamma$ and $\Gamma_{1}$ we have $x \in \sqrt{-3} \mathcal{O}_{F}$ and for $\Gamma$ (respectively $\Gamma_{1}$ ) we have $y \in \mathcal{O}_{F}$ (respectively $y \in \sqrt{-3} \mathcal{O}_{F}$. Hence $t_{i} \in \mu_{6}$ and it follows that $t_{1}=t_{2}=t_{3}$ and the diagonal matrix lies in the center.

Calculating the automorphy factors for an element of $\Gamma_{\infty}$ as in (3.1) gives
$$j_{1}=t_{2}, \quad j_{2}=\left(\begin{array}{cc}
1 / t_{3} & y^{\prime} / t_{3} \\
0 & 1 / t_{1}
\end{array}\right), \quad j_{3}=t_{1} t_{2} t_{3} .$$
In particular, for an element of $\Gamma_{\infty}^{\prime}$ as in (3.1) we find $j_{1}=1, j_{2}=\left(1, y^{\prime} ; 0,1\right)$ and $j_{3}=1$. In this case the restriction of $L$ and $R$ to an elliptic curve $E$ is trivial and $U$ restricted to $E$ is a unipotent bundle of rank 2, cf. [3]. This result also follows from the next proposition for which Thomas Peternell kindly provided us with a proof. We identify a neighborhood of $E$ with the total space of the normal bundle of $E$ in $Y_{\Gamma^{\prime}}$.

Proposition 3.4. If $E$ is an elliptic curve and $N$ is a line bundle on $E$ with total space $X$ then the rank 2 bundle $V=\Omega_{X}^{1}(\log E)$ restricted to $E$ is an extension of $\mathcal{O}_{E}$ by $\mathcal{O}_{E}$ and it is non-trivial if and only if $\operatorname{deg} N$ is non-trivial.

Corollary 3.5. For $\Gamma^{\prime}$ as above the restriction of $\operatorname{Sym}^{n}(U)$ to the elliptic curve $E$ is isomorphic to $F_{n+1}$, the unique indecomposible vector bundle of rank $n+1$ with a 1 -dimensional space of sections.
3.4. Eisenstein cohomology. The Eisenstein cohomology is the contribution to the cohomology coming from the boundary. The study of Eisenstein cohomology was initiated by Harder (see [22], [23]), who used the Borel-Serre compactification and topological methods to determine the Eisenstein cohomology in a closely related case. Here we use, as in [19], coherent cohomology to determine the Eisenstein cohomology.

Let $\Gamma^{\prime} \subset \Gamma_{1}[\sqrt{-3}]$ be a normal finite index subgroup that acts freely on $B$. Let $\mathbb{W}_{\lambda}$ be a local system on $X_{\Gamma^{\prime}}$. The full Eisenstein cohomology $e_{\text {Eis }, \mathrm{f}}\left(X_{\Gamma^{\prime}}, \mathbb{W}_{\lambda}\right)$ is defined as
$$e_{c}\left(X_{\Gamma^{\prime}}, \mathbb{W}_{\lambda}\right)-e\left(X_{\Gamma^{\prime}}, \mathbb{W}_{\lambda}\right),$$
where $e_{c}\left(X_{\Gamma^{\prime}}, \mathbb{W}_{\lambda}\right)$, respectively $e\left(X_{\Gamma^{\prime}}, \mathbb{W}_{\lambda}\right)$, stands for the Euler characteristics
$$\sum_{i}(-1)^{i}\left[H_{c}^{i}\left(X_{\Gamma^{\prime}}, \mathbb{W}_{\lambda}\right)\right], \text { respectively } \sum_{i}(-1)^{i}\left[H^{i}\left(X_{\Gamma^{\prime}}, \mathbb{W}_{\lambda}\right)\right],$$
where the square brackets refer to classes in the Grothendieck group of mixed Hodge structures. The compactly supported Eisenstein cohomology $e_{\text {Eis }}\left(X_{\Gamma^{\prime}}, \mathbb{W}_{\lambda}\right)$ is defined as
$$\sum(-1)^{i}\left[\operatorname{ker}\left(H_{c}^{i}\left(X_{\Gamma^{\prime}}, \mathbb{W}_{\lambda}\right) \rightarrow H^{i}\left(X_{\Gamma^{\prime}}, \mathbb{W}_{\lambda}\right)\right)\right] .$$
Note that there is a map $e_{\text {Eis }}\left(X_{\Gamma^{\prime}}, \mathbb{W}_{\lambda}\right) \rightarrow e_{\text {Eis, } \mathrm{f}}\left(X_{\Gamma^{\prime}}, \mathbb{W}_{\lambda}\right)$.
Lemma 3.6. Put $\mathcal{F}_{i}$, for $i=0,1,2$, equal to
$$\mathcal{W}_{n_{1},-n_{1}-n_{2}, n_{1}+n_{2}+n_{3}}, \quad \mathcal{W}_{n_{1}+n_{2}+1,-n_{1}+1, n_{1}+n_{2}+n_{3}}, \quad \mathcal{W}_{n_{2}, n_{1}+3, n_{2}+n_{3}-1} .$$
\begin{itemize}
\item[(i)] For any $\lambda=n_{1} \gamma_{1}+n_{2} \gamma_{2}+n_{3} \gamma_{3}$ we have
$$e_{\mathrm{Eis}, \mathrm{f}}\left(X_{\Gamma^{\prime}}, \mathbb{W}_{n_{1}, n_{2}, n_{3}}\right)=\sum_{i=0}^{2}(-1)^{i}\left(\left[H^{0}\left(D, \mathcal{F}_{i \mid D}\right)\right]-\left[H^{1}\left(D, \mathcal{F}_{i \mid D}\right)\right]\right) .$$
\item[(ii)] For any $\lambda=n_{1} \gamma_{1}+n_{2} \gamma_{2}+n_{3} \gamma_{3}$ such that $n_{1}+n_{2}>1$ we have
$$e_{\mathrm{Eis}}\left(X_{\Gamma^{\prime}}, \mathbb{W}_{n_{1}, n_{2}, n_{3}}\right)=-\left[H^{0}\left(D, \mathcal{F}_{0 \mid D}\right)\right]+\left[H^{1}\left(D, \mathcal{F}_{0 \mid D}\right)\right]+\left[H^{0}\left(D, \mathcal{F}_{1 \mid D}\right)\right] .$$
\end{itemize}

Proof. Put $Y=Y_{\Gamma^{\prime}}$. From [16, Theorem 5.5] it follows (compare the description of the BGG-complexes for $j_{*} \mathbb{W}_{\lambda}$ and $j_{!} \mathbb{W}_{\lambda}$ in Section 3.2) that
$$e_{\mathrm{Eis}, \mathrm{f}}\left(X_{\Gamma^{\prime}}, \mathbb{W}_{n_{1}, n_{2}, n_{3}}\right)=\sum_{i=0}^{2} \sum_{j=0}^{2}(-1)^{i+j}\left(\left[H^{i}\left(Y, \mathcal{F}_{j}(-D)\right)\right]-\left[H^{i}\left(Y, \mathcal{F}_{j}\right)\right]\right) .$$

For any locally free sheaf $\mathcal{F}$ on $Y_{\Gamma^{\prime}}$ we have an exact sequence
$$0 \rightarrow \mathcal{F}(-D) \rightarrow \mathcal{F} \rightarrow \mathcal{F}_{\mid D} \rightarrow 0 .$$
Taking the long exact sequence deduced from this sequence for the three cases $\mathcal{F}_{r}$, with $r=0,1,2$, statement (i) follows.

For (ii) we again use the BGG-complexes of Section 3.2 to conclude that
$$e_{\mathrm{Eis}}\left(X_{\Gamma^{\prime}}, \mathbb{W}_{n_{1}, n_{2}, n_{3}}\right)=\sum_{i=0}^{2} \sum_{j=0}^{2}(-1)^{i+j}\left[\operatorname{ker}\left(H^{i}\left(Y, \mathcal{F}_{j}(-D)\right) \rightarrow H^{i}\left(Y, \mathcal{F}_{j}\right)\right)\right] .$$
We now consider the three cases $r=0,1,2$ individually. For the case $r=$ 0 the vanishing of $H^{0}\left(Y, \mathcal{W}_{j, k, l}\right)$ for negative $k$ implies that the sequence reduces to
$$\begin{aligned}
0 \rightarrow H^{0}\left(D, \mathcal{F}_{0 \mid D}\right) & \rightarrow H^{1}\left(Y, \mathcal{F}_{0}(-D)\right) \rightarrow H^{1}\left(Y, \mathcal{F}_{0}\right) \rightarrow \\
H^{1}\left(D, \mathcal{F}_{0 \mid D}\right) & \rightarrow H^{2}\left(Y, \mathcal{F}_{0}(-D)\right) \rightarrow H^{2}\left(Y, \mathcal{F}_{0}\right) \rightarrow 0
\end{aligned}$$
We can identify the last three terms in the sequence with the Serre duals of
$$M_{n_{1}, n_{2}+3,-n_{2}-n_{3}-1}\left(\Gamma^{\prime}\right) \leftarrow S_{n_{1}, n_{2}+3,-n_{2}-n_{3}-1}\left(\Gamma^{\prime}\right) \leftarrow 0 .$$
It follows from Corollary 3.5 that $h^{0}\left(D, \mathcal{F}_{0}\right)$ equals the number $c$ of cusps of $X_{\Gamma^{\prime}}^{*}$. Possibly replacing $\Gamma^{\prime}$ by a finite index subgroup (and in the end taking invariants) there is, since $n_{1}+n_{2}>1$, an Eisenstein series for each cusp, see [9, Prop. 12.1]. Since both $U$ and $L$ have degree 0 when restricted to an elliptic curve in $D$, Riemann-Roch tells us that $h^{1}\left(D, \mathcal{F}_{0}\right)=h^{0}\left(D, \mathcal{F}_{0}\right)$. Finally, since
$$\operatorname{dim} M_{n_{1}, n_{2}+3,-n_{2}-n_{3}-1}\left(\Gamma^{\prime}\right)=c+\operatorname{dim} S_{n_{1}, n_{2}+3,-n_{2}-n_{3}-1}\left(\Gamma^{\prime}\right)$$
it follows that
$$H^{1}\left(D, \mathcal{F}_{0 \mid D}\right) \rightarrow H^{2}\left(Y, \mathcal{F}_{0}(-D)\right)$$
is injective.
For $\mathcal{F}_{1}$ we find that the sequence reduces to
$$0 \rightarrow H^{0}\left(D, \mathcal{F}_{1 \mid D}\right) \rightarrow H^{1}\left(Y, \mathcal{F}_{1}(-D)\right) \rightarrow H^{1}\left(Y, \mathcal{F}_{1}\right) \rightarrow H^{1}\left(D, \mathcal{F}_{1 \mid D}\right) \rightarrow 0,$$
again by the vanishing of $M_{j, k, l}\left(\Gamma^{\prime}\right)$ for $k<0$. Similarly to the case $r=0$, we can identify $H^{0}\left(D, \mathcal{F}_{2}\right)$ with a space of Eisenstein series, and hence with the cokernel of the second arrow in the exact sequence
$$\begin{aligned}
& 0 \rightarrow H^{0}\left(Y, \mathcal{F}_{2}(-D)\right) \rightarrow H^{0}\left(Y, \mathcal{F}_{2}\right) \rightarrow H^{0}\left(D, \mathcal{F}_{2}\right) \\
& \quad H^{1}\left(Y, \mathcal{F}_{2}(-D)\right) \rightarrow H^{1}\left(Y, \mathcal{F}_{2}\right) \rightarrow H^{1}\left(D, \mathcal{F}_{2}\right) \rightarrow 0 .
\end{aligned}$$
This finishes the proof of (ii). \(\square\)

Corollary 3.7. For any regular $\lambda=n_{1} \gamma_{1}+n_{2} \gamma_{2}+n_{3} \gamma_{3}$ we have
$$H^{1}\left(Y_{\Gamma^{\prime}}, \mathcal{F}_{0}\right)=0 .$$
Proof. As noted at the end of Section 3.2, since $\lambda$ is regular, $H_{!}^{1}\left(X, \mathbb{W}_{\lambda}\right)=0$. The result now follows directly from Remark 3.2 together with Proposition 3.3. \(\square\)

Definition 3.8. We write $\mathbf{s}_{\mu}$ for the irreducible representation of $\mathfrak{S}_{4}$ indexed in the usual way by $\mu$ a partition of 4. We then define the $\mathfrak{S}_{4}$-representations,
$$\gamma_{i}= \begin{cases}\mathbf{s}_{4}+\mathbf{s}_{3,1} & i \equiv_{6} 0 \\ \mathbf{s}_{14}+\mathbf{s}_{2,1^{2}} & i \equiv_{6} 3 \\ 0 & \text { else }\end{cases}$$

In the following proposition $\mathbb{L}^{i, j}$ will denote the motive corresponding to a Hecke character, see further in Section 7.1; it is 1-dimensional and has Hodge degree $(i, j)$.

Proposition 3.9. For regular $\lambda=n_{1} \gamma_{1}+n_{2} \gamma_{2}+n_{3} \gamma_{3}$ with $n_{1} \equiv_{3} n_{2}$ and $n_{1} \equiv_{2} n_{3}$, put $i=n_{2}+n_{3}$. Then $e_{\text {Eis }}\left(X_{\Gamma[\sqrt{-3}]}, \mathbb{W}_{\lambda}\right)$ consists of the following three contributions,
$$\left(-\gamma_{i} \mathbb{L}^{0,0}+\gamma_{i-n_{2}-1} \mathbb{L}^{n_{2}+1,0}+\gamma_{i+n_{1}+1} \mathbb{L}^{0, n_{1}+1}\right) \mathbb{L}^{n_{3}, n_{3}+i} .$$

As another approach to this Eisenstein cohomology is already in the literature [22, 23] we will only provide a sketch of proof. We will normalize the weights, which corresponds to removing the factor $\mathbb{L}^{n_{3}, n_{3}+i}$ in Proposition 3.9, see also further in Section 7.3.1.

For each elliptic curve $E$ occurring in the divisor $D$ each of the the contributions in Lemma 3.6 are either zero or 1-dimensional, see Corollary 3.5. We observe that the Hodge weights of the three contributions are 0, 0 and $n_{2}+1$. Interchanging $n_{1}$ and $n_{2}$ amounts to changing the complex structure by its complex conjugate. Hence this limits the Hodge types to (0, 0), $\left(n_{2}+1,0\right),\left(0, n_{1}+1\right)$ and $\left(n_{2}+1, n_{1}+1\right)$. But the last one can occur only in the dual of $e_{\text {Eis. }}$ So we find the Hodge types
$$(0,0),\left(n_{2}+1,0\right),\left(0, n_{1}+1\right)$$
for the three contributions.
We now specialize to the situation $\Gamma^{\prime}=\Gamma_{1}[\sqrt{-3}]$ where $\Gamma / \Gamma_{1}[\sqrt{-3}]=$ $\mathfrak{S}_{4} \times \mu_{6}$ acts on $Y_{\Gamma_{1}[\sqrt{-3}]}$ by permuting the cusps and the group $\mathfrak{S}_{4} \times \mu_{3}$ acts effectively. The group $\left\langle\rho 1_{3}\right\rangle$ sits in the center of $\Gamma[\sqrt{-3}]$ making the $\mathcal{F}_{i}$ orbifold bundles. We thus get contributions to the Eisenstein cohomology only if $n_{1} \equiv_{3} n_{2}$.

Since for each elliptic curve occuring in the divisor $D$ on $Y_{\Gamma_{1}[\sqrt{-3}]}$ the cohomology group $H^{i}\left(E, \mathcal{F}_{j}\right)$ is at most 1-dimensional and the stabilizer of such an elliptic curve is $\mathfrak{S}_{3} \times \mu_{3}$ it contributes either zero or a $\mathfrak{S}_{4}$-representation of the form
$$\operatorname{Ind}_{\mathfrak{S}_{3}}^{\mathfrak{S}_{4}} \mathbf{s}_{3}=\mathbf{s}_{4}+\mathbf{s}_{3,1} \quad \text { or } \quad \operatorname{Ind}_{\mathfrak{S}_{3}}^{\mathfrak{S}_{4}} \mathbf{s}_{1^{3}}=\mathbf{s}_{2,1^{2}}+\mathbf{s}_{1^{4}} .$$
Furthermore, the element $\gamma=\operatorname{diag}(1,1, \rho)$ acts by multiplication by $\rho$ on each resolution elliptic curve $E$. The Eisenstein cohomology for $\Gamma[\sqrt{-3}]$ corresponds to the invariant part under the action of $\gamma$.

\section*{4. The dimension of spaces of Picard modular forms}

In this section we are interested in the dimensions of spaces of modular forms and cusp forms on our groups $\Gamma_{1}[\sqrt{-3}]$ and $\Gamma[\sqrt{-3}]$. We dwell upon this since it provides important checks on the conjectures on the cohomology of local systems.

Recall that the space $M_{j, k}\left(\Gamma_{1}[\sqrt{-3}]\right)$ splits as
$$M_{j, k}\left(\Gamma_{1}[\sqrt{-3}]\right)=M_{j, k}(\Gamma[\sqrt{-3}]) \oplus M_{j, k}(\Gamma[\sqrt{-3}], \operatorname{det}) \oplus M_{j, k}\left(\Gamma[\sqrt{-3}], \operatorname{det}^{2}\right)$$
and similarly for the spaces of cusp forms $S_{j, k}\left(\Gamma_{1}[\sqrt{-3}]\right)$. Recall furthermore that the graded ring $\oplus_{k=0}^{\infty} M_{0,3 k}\left(\Gamma_{1}[\sqrt{-3}]\right)$ is a degree 3 extension of
$$\oplus_{k=0}^{\infty} M_{0,3 k}(\Gamma[\sqrt{-3}])=\mathbb{C}\left[x_{1}, x_{2}, x_{3}, x_{4}\right] /\left(x_{1}+x_{2}+x_{3}+x_{4}\right)$$
generated by $\zeta \in S_{6}\left(\Gamma[\sqrt{-3}]\right.$, det) satisfying the relation (2.1). Moreover, $\mathfrak{S}_{4}$ acts by $\sigma: x_{i} \mapsto \operatorname{sgn}(\sigma) x_{\sigma(i)}$ and by the sign on $\zeta$. We find (see Section 7 and Section 12 of [9] for more details) that $\operatorname{dim} M_{0,3 k}\left(\Gamma_{1}[\sqrt{-3}]\right)=(3 / 2) k(k-$ 1) +4 for $k \geq 2$ and $\operatorname{dim} M_{0,3}=3$; moreover, for $k \geq 2$
$$\operatorname{dim} S_{0,3 k}\left(\Gamma[\sqrt{-3}], \operatorname{det}^{\ell}\right)= \begin{cases}\left(k^{2}+3 k-6\right) / 2 & \ell=0 \\ \left(k^{2}-k\right) / 2 & \ell=1 \\ \left(k^{2}-5 k+6\right) / 2 & \ell=2 .\end{cases}$$
We now deduce a formula for the space of cusp forms on a freely acting finite index subgroup $\Gamma^{\prime}$ of $\Gamma_{1}[\sqrt{-3}]$. The surface $\Gamma^{\prime} \backslash B$ is smoothly compactified by adding a divisor $D$ consisting of disjoint elliptic curves.

Theorem 4.1. For $j \geq 0$ and $k>0$ we have
$$\operatorname{dim} S_{j, 3+k}\left(\Gamma^{\prime}\right)=\frac{1}{6}(j+1)(k+1)(j+k+2) \operatorname{vol}\left(\Gamma^{\prime} \backslash B\right)+\frac{1}{12}(j+1) D^{2}$$
with $\operatorname{vol}\left(\Gamma^{\prime} \backslash B\right)=c_{2}\left(\Gamma^{\prime} \backslash B\right)=3 c_{1}(L)^{2}$.
Remark 4.2. Note that the formula is symmetric in $j$ and $k$ up to the factor $j D^{2} / 12$. For a group $\Gamma^{\prime}$ acting on the ball with a compact quotient $\Gamma^{\prime} \backslash B$ one would get a formula symmetric in $j$ and $k$.

Before we give the proof we state a simple lemma.
Lemma 4.3. With $\gamma=c_{1}(L)$, the Chern character satisfies
$$\operatorname{ch}\left(\mathcal{W}_{a, b}\right)=(a+1)\left(1+(a / 2+b) \gamma+\left(b^{2} / 2+a b / 2-a / 4\right) \gamma^{2}\right) .$$
Proof. Since $\Gamma^{\prime}$ acts freely we have that $\mathcal{W}_{a, b}=\operatorname{Sym}^{a}(U) \otimes L^{b}$ and we know that $\operatorname{det}(U)=L$. Let $\alpha_{1}$ and $\alpha_{2}$ be the Chern roots of $U$. Then $\alpha_{1}+\alpha_{2}=$ $\gamma$ and by Hirzebruch-Mumford proportionality we have $c_{1}\left(\Omega^{1}(\log D)\right)^{2}=$ $3 c_{2}\left(\Omega^{1}(\log D)\right)$, hence $(3 \gamma)^{2}=3\left(\alpha_{1} \alpha_{2}+2 \gamma^{2}\right)$, so $\alpha_{1}+\alpha_{2}=\gamma$ and $c_{2}(U)=$ $\alpha_{1} \alpha_{2}=\gamma^{2}$. This implies $c_{1}\left(\operatorname{Sym}^{a}(U)\right)=(1 / 2) a(a+1) \gamma$ and
$$\operatorname{ch}_{2}\left(\operatorname{Sym}^{a}(U)\right)=\sum_{i=0}^{a}\left((a-i) \alpha_{1}+i\left(\alpha_{2}\right)\right)^{2} / 2=-a(a+1) \gamma^{2} / 4 .$$

The result easily follows from this. \(\square\)

Proof. We work on $Y=Y_{\Gamma^{\prime}}$. We denote the resolution divisor of the cusps by $D$. The canonical line bundle $K_{Y}$ is $L^{\otimes 3} \otimes \mathcal{O}(-D)$. In view of the vanishing of $h^{1}$ and $h^{2}$ (by Corollary 3.7 and Proposition 2.3) of $\mathcal{W}_{j, k} \otimes \Omega^{2}$ we have that
$$\operatorname{dim} S_{j, k+3}\left(\Gamma^{\prime}\right)=h^{0}\left(Y, \mathcal{W}_{j, k} \otimes \Omega_{Y}^{2}\right)=\chi\left(Y, \mathcal{W}_{j, k} \otimes \Omega_{Y}^{2}\right)$$
with $\chi$ denoting the Euler characteristic. By Serre duality we have
$$\chi\left(Y, \mathcal{W}_{j, k} \otimes \Omega_{Y}^{2}\right)=\chi\left(Y, \mathcal{W}_{j,-j-k}\right)$$
We apply the Hirzebruch-Riemann-Roch formula
$$\chi\left(Y, \mathcal{W}_{a, b}\right)=\left(\operatorname{ch}\left(\mathcal{W}_{a, b}\right) \cdot \operatorname{td}\right)[Y]$$
with td the Todd class $1-3 \gamma / 2+D / 2+\left(c_{1}^{2}+c_{2}\right)[Y] / 12$ and $c_{1}(Y)=-3 \gamma+D$, where again we write $\gamma=c_{1}(L)$ for the first Chern class of $L$.

Using $\chi\left(Y, \mathcal{O}_{Y}\right)=\left(c_{1}^{2}+c_{2}\right)[Y] / 12=\gamma^{2}+D^{2} / 12$ we now find
$$\begin{aligned}
\chi\left(Y, \mathcal{W}_{a, b}\right) & =(a+1)\left(\left(b^{2}+a b-2 a-3 b\right) \gamma^{2} / 2+\chi\left(Y, \mathcal{O}_{Y}\right)\right) \\
& \left.=(a+1)\left(\left(b^{2}+a b-2 a-3 b+2\right) \gamma^{2} / 2+D^{2} / 12\right)\right) .
\end{aligned}$$
Substituting $a=j$ and $b=-j-k$ gives
$$\left(j^{2} k+k^{2} j+j^{2}+4 j k+k^{2}+3 j+3 k+2\right) \gamma^{2} / 2+(j+1) D^{2} / 12 .$$ \(\square\)

Remark 4.4. For our group $\Gamma_{1}[\sqrt{-3}]$ we have $\operatorname{vol}\left(\Gamma_{1}[\sqrt{-3}] \backslash B\right)=1$ and for $\Gamma[\sqrt{-3}]$ we have $\operatorname{vol}(\Gamma[\sqrt{-3}] \backslash B)=1 / 3$.

For our group $\Gamma_{1}[\sqrt{-3}]$ we have the following dimension formula.
Proposition 4.5. For $j \geq 0$ and $k>0$ with $j \equiv_{3} k$ the dimension of $S_{j, k+3}\left(\Gamma_{1}[\sqrt{-3}]\right)$ is given by
$$\frac{1}{6}(j+1)(k+1)(j+k+2)-(j+1)+ \begin{cases}2 / 3 & j \equiv_{3} 0 \\ -2 / 3 & j \equiv_{3} 1 \\ 0 & j \equiv_{3} 2\end{cases}$$

Remark 4.6. We conjecture that the formulas above also hold for $k=0$ in all cases except when $j \equiv_{6} 0$ for which the dimension is $\left(j^{2}-3 j+6\right) / 6$. This is based upon computations of the numerical Euler characteristic in Section 9 and Conjecture 12.12.

Proof. The subgroup $\Gamma_{1}[3]$ of $\Gamma_{1}[\sqrt{-3}]$ acts freely and the formula of Theorem 4.1 holds with $\operatorname{vol}\left(\Gamma_{1}[3]\right)=81$ and $D$ consisting of $4 \cdot 27$ elliptic curves with self-intersection number -9. The quotient group $G^{\prime}=\Gamma_{1}[\sqrt{-3}] / \Gamma_{1}[3]$ is of order $3^{5}$, but its center $\langle\rho \mathrm{id}\rangle=\mu_{3}$ acts trivially. We will apply the holomorphic Lefschetz formula to the action of the group $G=G^{\prime} / \mu_{3}$ on $Y_{\Gamma_{1}[3]}$ and the vector bundle $\mathcal{W}_{j, k} \otimes \Omega_{Y_{\Gamma_{1}[3]}}^{2}$. The group $G$ is isomorphic to
$(\mathbb{Z} / 3 \mathbb{Z})^{4}$. The action of $G$ on $Y_{\Gamma[3]}$ has 3 • 27 fixed points lying over the quotient singularities of $X_{\Gamma_{1}[\sqrt{-3}]}$ and no other fixed points. We know that the quotient singularieties are of order 3 and type (1, 2). The holomorphic Lefschetz formula now says that for the action of $G$ on the manifold $Y=Y_{\Gamma_{1}[3]}$ and vector bundle $V$ we have
$$\sum_{i}(-1)^{i} \operatorname{dim} H^{i}(Y, V)^{G}=(1 / \# G) \sum_{g \in G} \chi(Y, V, g)$$
with $\chi(Y, V, g)=\operatorname{ch}(Y, V, g) \operatorname{td}(Y, g)\left[Y^{g}\right]$ with $\operatorname{td}(Y, g)$ the Todd class associated to $Y^{g}$. At a fixed point of a non-trivial element of $G$ the Todd class is $1 /\left(1-\rho^{2}\right)(1-\rho)=1 / 3$. The action on the fibre of $L^{3}$ over a fixed point is trivial, while on the fibre of $\Omega^{1}$ it acts by $\left(\rho, \rho^{2}\right)$. Hence on the fibre of $\mathcal{W}_{j, k}$ it acts by eigenvalues $\rho^{r} \rho^{2(j-r)}$ for $r=0, \ldots, j$. So one non-trivial element of $G$ yields for one fixed point a contribution
$$c(j)=(1 / 3) \sum_{r=0}^{j} \rho^{2 j-r}= \begin{cases}1 / 3 & j \equiv_{3} 0 \\ -1 / 3 & j \equiv_{3} 1 \\ 0 & j \equiv_{3} 2\end{cases}$$
In total the 81 fixed points are each fixed by 2 non-trivial elements, hence we get a contribution $(1 / 81) \cdot 81 \cdot 2 \cdot c(j)$. The identity element contributes $(j+1)(k+1)(j+k+2) / 6-(j+1)$. Together this proves the formula. □

Next we want a formula for the dimension $s_{j, k+3, l}$ of the space of modular forms $S_{j, k+3}\left(\Gamma[\sqrt{-3}], \operatorname{det}^{l}\right)$. Since we have a formula for
$$\sum_{l=0}^{2} s_{j, k+3, l}=\operatorname{dim} S_{j, k+3}\left(\Gamma_{1}[\sqrt{-3}]\right)$$
it suffices to calculate the trace of a generator $\gamma=\operatorname{diag}(1,1, \rho)$ of the group $\Gamma[\sqrt{-3}] / \Gamma_{1}[\sqrt{-3}] \cong \mathbb{Z} / 3 \mathbb{Z}$ on $S_{j, k+3}\left(\Gamma_{1}[\sqrt{-3}]\right)$. Indeed, for an operator $\gamma$ of order 3 acting on a complex vector space of dimension $n$ with with eigenspaces of dimension $m_{1}, m_{\rho}$ and $m_{\rho^{2}}$ for the eigenvalues $1, \rho$ and $\rho^{2}$ (with $n=m_{1}+m_{\rho}+m_{\rho^{2}}$ ) and with $\operatorname{trace}(\gamma)=a+b \rho$ with $a, b \in \mathbb{Z}$ we have $m_{1}=(n+2 a-b) / 3, m_{\rho}=(n-a+2 b) / 3$ and $m_{\rho^{2}}=(n-a-b) / 3$.

Theorem 4.7. If $j \not \equiv_{3} k$ then $\operatorname{dim} S_{j, k+3, l}(\Gamma[\sqrt{-3}])=0$. If $j \equiv_{3} k$ and $k>0$ we have
$$\operatorname{dim} S_{j, k+3, l}(\Gamma[\sqrt{-3}])=\frac{1}{18}(j+1)(k+1)(j+k+2)+A_{j, k, l},$$
with $A_{j, k, l}$ depending on the residue class of $(j, l)$ in $(\mathbb{Z} / 3 \mathbb{Z})^{2}$ as follows
$$\begin{array}{cccc} 
& l \equiv_{3} 0 & l \equiv_{3} 1 & l \equiv_{3} 2 \\
j \equiv_{3} 0 & 2 k / 3-10 / 9 & -j / 3-1 / 9 & -2 j / 3-2 k / 3+8 / 9 \\
j \equiv_{3} 1 & -j / 3-5 / 9 & 2 k / 3-14 / 9 & -2 j / 3-2 k / 3+4 / 9 \\
j \equiv_{3} 2 & 0 & 0 & -j-1
\end{array}$$

Remark 4.8. We conjecture that the formulas above also hold for $k=0$ in all cases except when $l=0$ and $j \equiv_{6} 0$, and then $A_{j, 0,0}=-1 / 9$. This is based upon the same evidence as in Remark 4.6.

Proof. We apply the holomorphic Lefschetz formula to the action of a representative $\gamma=\operatorname{diag}(1,1, \rho)$ of $\Gamma[\sqrt{-3}] / \Gamma_{1}[\sqrt{-3}] \cong \mathbb{Z} / 3 \mathbb{Z}$ on the surface $Y=Y_{\Gamma_{1}[\sqrt{-3}]}$ and the orbifold vector bundle $\Omega_{Y}^{2} \otimes \mathcal{W}_{j, k}$. We assume that $j \equiv_{3} k$ otherwise $M_{j, k}\left(\Gamma_{1}[\sqrt{-3}]\right)$ is zero. We can write
$$\Omega_{Y}^{2} \otimes \mathcal{W}_{j, k}=\Omega_{Y}^{2} \otimes \operatorname{Sym}^{j}(U \otimes L) \otimes L^{k-j},$$
where the center $\mu_{3}$ acts on all three factors trivially. The fixed point locus of $\gamma$ on the surface $Y_{\Gamma_{1}[\sqrt{-3}]}$ consists of the six curves $D_{i j}$ (see Section 2) and the three intersection points of the two resolution curves of the three quotient singularities on $X_{\Gamma_{1}[\sqrt{-3}]}$. Each of the $D_{i j}$ is a smooth rational curve which is an exceptional curve, the restriction of $\Omega_{Y}^{1}$ to $D_{i j}$ is $\mathcal{O}(2) \oplus \mathcal{O}(-1)$, with the first factor the cotangent bundle to $D_{i j}$ and the second the conormal bundle. And since the resolution divisor $D$ of the cusps intersects $D_{i j}$ transversally at two points, we find
$$\Omega^{1}(\log D)_{\mid D_{i j}}=\mathcal{O} \oplus \mathcal{O}(1) .$$
The action of $\gamma$ preserves the two factors. It acts trivially on the cotangent bundle of $D_{i j}$ and by $\rho^{2}$ on the conormal bundle since one $D_{i j}$ is given by $u=0$ and $\gamma$ acts by $(u, v) \mapsto(\rho u, v)$. Since $\Omega^{1}(\log D) \cong U \otimes L$ we get $U \otimes L_{\mid D_{i j}}=\mathcal{O} \oplus \mathcal{O}(1)$ with $\gamma$ acting by 1 on the first factor and by $\rho^{2}$ on the second one.

We need the Todd class along $D_{i j}$; if we write the first Chern class of $\mathcal{O}_{D_{i j}}(1)$ as $P$, the class of a point, then we find
$$\operatorname{td}\left(D_{i j}, \gamma\right)=\frac{2 P}{1-e^{-2 P}} \frac{1}{1-\rho^{2} e^{P}},$$
where the first factor comes from the tangent bundle and the second from the normal bundle resulting in
$$\operatorname{td}\left(D_{i j}, \gamma\right)=\frac{2+\rho}{3}-\frac{1+\rho}{3} P .$$
We have $L_{\mid D_{i j}}^{3}=\mathcal{O}(1)$ with $\gamma$ acting trivially. We need $\operatorname{ch}\left(\Omega_{Y}^{2} \otimes \mathcal{W}_{j, k} \mid D_{i j}\right)$ in the cohomology of $D_{i j}$ tensored with the representation ring of $\mu_{3}=\langle\gamma\rangle$. We thus write $\operatorname{ch}\left(\operatorname{Sym}^{j}(U \otimes L)_{\mid D_{i j}}\right)=r(j)+d(j) P$, where $P$ denotes the cohomology class of a point on $D_{i j}$ and we interpret $r(j)$ and $d(j)$ as elements of $\mathbb{Z}[\rho]$. Furthermore, $\operatorname{ch}\left(\Omega_{Y}^{2} \mid D_{i j}\right)=\rho^{2}(1-P)$. From the description just given we obtain:
$$\operatorname{ch}\left(\Omega^{2} \otimes \mathcal{W}_{j, k} \mid D_{i j}\right)=\left(r_{j}+d_{j} P\right)\left(\rho^{2}-\rho^{2} P\right)\left(\left(1+\left(\frac{k-j}{3}\right) P\right) .\right.$$

We have $r_{j}=\sum_{a=0}^{j} \rho^{2 a}$, and $d_{j}=\sum_{a=0}^{j} \rho^{2 a} a$ and we thus find
$$r(j)+d(j) P= \begin{cases}1+\frac{j}{3}(2+\rho) P & j \equiv_{3} 0 \\ -\rho+\left(\frac{j+2}{3}(-1-2 \rho)+\rho\right) P & j \equiv_{3} 1 \\ 0+\frac{j+1}{3}(\rho-1) P & j \equiv_{3} 2\end{cases}$$
The contribution of the six $D_{i j}$ is the coefficient of $P$ in
$$6 \rho^{2}(r(j)+d(j) P)\left(1+\left(\frac{k-j-3}{3}\right) P\right)\left(\frac{2+\rho}{3}-\frac{1+\rho}{3} P\right)$$
and this is
$$\begin{cases}(-2 k+2 j+6) / 3+(-4 k-2 j+6) \rho / 3 & j \equiv_{3} 0 \\ (-4 k-2 j+6) / 3+(-2 k+2 j+6) \rho / 3 & j \equiv_{3} 1 \\ 2(j+1)(1+\rho) & j \equiv_{3} 2\end{cases}$$
By adding to these three cases $-(j+1)$ (respectively $-(j+1) \rho$ and $(j+1) \rho^{2}$ ) as the contribution of the three isolated fixed points of $\gamma$ one finds for the trace
$$(2 k+j-3)(-1-2 \rho) / 3, \quad(2 k+j-3)(-2-\rho) / 3, \quad-(j+1) \rho^{2} .$$
This gives the desired traces. \(\square\)

We end this section with a definition.
Definition 4.9. The space $S_{j, k, l}(\Gamma[\sqrt{-3}])$ is a representation of $\mathfrak{S}_{4}$ and we denote by $S_{j, k, l}(\Gamma[\sqrt{-3}])^{\mu}$ the isotypic component corresponding to the irreducible representation indexed by $\mu$, a partition of 4. We then put
$$\operatorname{dim}_{\mathfrak{S}_{4}} S_{j, k, l}(\Gamma[\sqrt{-3}]):=\sum_{\mu \vdash 4} \frac{\operatorname{dim} S_{j, k, l}(\Gamma[\sqrt{-3}])^{\mu}}{\operatorname{dim} \mathbf{s}_{\mu}} \mathbf{s}_{\mu} .$$
In Section 10, we define a (conjectural) subset
$$S_{j, k, l}^{\text {gen }}(\Gamma[\sqrt{-3}]) \subset S_{j, k, l}(\Gamma[\sqrt{-3}])$$
of so-called genuine forms and we define $\operatorname{dim}_{\mathfrak{S}_{4}} S_{j, k, l}^{\text {gen }}(\Gamma[\sqrt{-3}])$ analogously to the above.

\section*{5. Moduli spaces of abelian threefolds with $\rho$-action}