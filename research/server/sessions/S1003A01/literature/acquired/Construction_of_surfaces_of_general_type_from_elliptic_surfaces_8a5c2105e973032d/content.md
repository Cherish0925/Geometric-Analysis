---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 1008_1222.pdf
converter: mathpix
format: mmd
---

\title{
CONSTRUCTION OF SURFACES OF GENERAL TYPE FROM ELLIPTIC SURFACES VIA $\mathbb{Q}$-GORENSTEIN SMOOTHING
}

\author{
JONGHAE KEUM, YONGNAM LEE, AND HEESANG PARK
}

\begin{abstract}
We present methods to construct interesting surfaces of general type via $\mathbb{Q}$-Gorenstein smoothing of a singular surface obtained from an elliptic surface. By applying our methods to special Enriques surfaces, we construct new examples of a minimal surface of general type with $p_{g}=0, \pi_{1}=\mathbb{Z} / 2 \mathbb{Z}$, and $K^{2} \leq 4$.
\end{abstract}

\section*{1. Introduction}

A simply connected elliptic surface $S$ with a section is called an $E(n)$ surface if $\chi\left(\mathcal{O}_{S}\right)=n>0$ and $c_{1}^{2}(S)=0$. An $E(n)$ surface has topological Euler characteristic $c_{2}=12 n$. All $E(n)$ surfaces are diffeomorphic for fixed $n$, and an $E(n)$ surface is symplectically isomorphic to the fiber sum of $n$ copies of a rational elliptic surface $E(1)$. Recall that an $E(1)$ surface is obtained from $\mathbb{P}^{2}$ by blowing up the base points of a pencil of cubics, and an $E(2)$ surface is an elliptic K3 surface with a section.

Recently, Jongil Park and the second named author constructed a simply connected minimal surface of general type with $p_{g}=0$ and $K^{2}=2$ via $\mathbb{Q}$-Gorenstein smoothing of a singular rational surface [15]. This singular rational surface is obtained by contracting linear chains of rational curves in a blow-up of an $E(1)$ surface with singular fibers of special type. The other constructions of surfaces of general type with $p_{g}=0$ via $\mathbb{Q}$ -Gorenstein smoothing given in [16], [19], [20], [21], use different $E(1)$ surfaces, but all employ the same arguments as in [15] to prove the vanishing $H^{2}\left(T_{X}^{0}\right)=0$, which is a key ingredient to guarantee the existence of a $\mathbb{Q}$-Gorenstein smoothing.

We remark that several statements in [15] can be generalized to the case of $E(n)$ surfaces and to the case of elliptic surfaces without a section.
Question. Is it possible to construct an interesting complex surface via $\mathbb{Q}$-Gorenstein smoothing of a singular surface obtained by contracting linear chains of rational curves in a blow-up of an $E(n)$ surface with $n \geq 2$, or of an Enriques surface?

In this paper, we will treat mainly the case of Enriques surfaces. Since an Enriques surface has multiple fibres, the method of [15] for the case of an $E(1)$ surface cannot be applied directly to prove the existence of a global $\mathbb{Q}$-Gorenstein smoothing. We overcome this difficulty by passing to the K3-cover (an $E(2)$ surface) and then by showing that the obstruction space of the corresponding singular surface has trivial invariant part under the covering involution.

Using some special Enriques surfaces, we are able to construct minimal surfaces of general type with $p_{g}=0, \pi_{1}=\mathbb{Z} / 2 \mathbb{Z}$ and $K^{2}=1,2,3,4$. Each of our examples has

\footnotetext{
Date: Nov 14, 2010.
2000 Mathematics Subject Classification. Primary 14J29; Secondary 14J10, 14J17, 53D05.
Key words and phrases. $\mathbb{Q}$-Gorenstein smoothing, surface of general type, elliptic surface, Enriques surface.
}
ample canonical class, i.e., contains no (-2)-curve. There have been constructed several examples of a minimal surface of general type with $p_{g}=0, \pi_{1}=\mathbb{Z} / 2 \mathbb{Z}$ and $K^{2}=1$, by Barlow [1], by Inoue [9] and recently by Bauer and Pignatelli [3]. Each of these examples contains a $(-2)$-curve. We do not know if our example with $K^{2}=1$ is deformation equivalent to one of these examples. As for examples with $p_{g}=0, \pi_{1}=\mathbb{Z} / 2 \mathbb{Z}$ and $K^{2} \geq 2$, the existence is known only for $K^{2}=3$. In fact, Cartwright and Steger [4] recently found examples with $p_{g}=0, \pi_{1}=\mathbb{Z} / 2 \mathbb{Z}$ and $K^{2}=3$ by taking the minimal resolution of the quotient of a fake projective plane by an order 3 automorphism. By [10], the quotient of a fake projective plane by an order 3 automorphism has $p_{g}=0$, $K^{2}=3$, and 3 singular points of type $\frac{1}{3}(1,2)$. They computed the fundamental groups of all possible quotients to find that some quotients have $\pi_{1}=\mathbb{Z} / 2 \mathbb{Z}$. Our example with $K^{2}=3$ is different from any of their examples, but we do not know if ours is deformation equivalent to one of theirs. A minimal surface of general type with $p_{g}=0, K^{2}=2$ and $H_{1}=\mathbb{Z} / 2 \mathbb{Z}$ was constructed in [16], but it is not known if it actually has $\pi_{1}=\mathbb{Z} / 2 \mathbb{Z}$. Table 1 of [2] gives a list of minimal surfaces of general type with $p_{g}=0$ and $K^{2} \leq 7$ available in the literature.

We remark that our method cannot produce minimal surfaces of general type with $p_{g}=0$ and $K^{2} \geq 5$. The reason is that singular surfaces $X$ appearing in our construction satisfy the vanishing $H^{2}\left(T_{X}^{0}\right)=0$, which we need to ensure the existence of a global $\mathbb{Q}$ -Gorenstein smoothing. By the upper semi-continuity, the condition $H^{2}\left(T_{X}^{0}\right)=0$ implies $H^{2}\left(X_{t}, T_{X_{t}}\right)=0$ for a general member $X_{t}$ of a $\mathbb{Q}$-Gorenstein smoothing. Since
$$h^{1}\left(X_{t}, T_{X_{t}}\right)-h^{2}\left(X_{t}, T_{X_{t}}\right)=10 \chi\left(\mathcal{O}_{X_{t}}\right)-2 K_{X_{t}}^{2},$$
the dimension of the deformation space of $X_{t}$ is equal to $h^{1}\left(X_{t}, T_{X_{t}}\right)=10-2 K_{X_{t}}^{2}$, and hence there is no nontrivial deformation of $X_{t}$ if $K_{X_{t}}^{2} \geq 5$.

The case of $E(n)$ with $n \geq 4$ were worked out in [17] and [14]. The case of $E(3)$ will be treated in the last section. A key ingredient in the case of $E(n)$ is to show that there is a $\mathbb{Q}$-Gorenstein smoothing of singular points simultaneously even if there is an obstruction to $\mathbb{Q}$-Gorenstein smoothing for each singular point.

Throughout this paper, we follow Kodaira's notation for singular fibers of elliptic fibration [11], and we work over the field of complex numbers.

\section*{2. The case of elliptic K3 surfaces with a section}

In this section, we give a sufficient condition for the existence of a $\mathbb{Q}$-Gorenstein smoothing of a singular surface obtained from a K3 surface with a section. This will be used in our main construction in Section 3.

Let $Y$ be a K3 surface admitting an elliptic fibration with a section whose singular fibers are either reducible or of type $\mathrm{I}_{1}$ (nodal). Assume that it has a fibre of type $\mathrm{I}_{1}$, and let $F_{Y}$ be such a fibre. Let $\pi: Z \rightarrow Y$ be the blow-up at the node of $F_{Y}$. Let $F$ be the proper transform of $F_{Y}$ and $E$ the exceptional curve, i.e. the total transform of $F_{Y}$ is $F+2 E$. Let $S_{1}, \ldots, S_{\ell} \subset Z$ be the proper transform of sections in $Y$. They are (-2)-curves, not meeting $E$. Let $G_{1}, \ldots, G_{k}$ be (-2)-curves in the union of singular fibers. Assume that the support of $\cup_{i=1}^{k} G_{i}$ does not contain the support of a whole fiber, and that the sum $S_{1}+\cdots+S_{\ell}+G_{1}+\cdots+G_{k}+F+E$ is a normal crossing divisor.

Proposition 2.1. With the assumptions and the notation as above, assume further that $S_{1}, \ldots, S_{\ell}, G_{1}, \ldots, G_{k}, F, E$ are numerically independent in the Picard group of $Z$. Then $H^{2}\left(Z, T_{Z}\left(-\log \left(S_{1}+\cdots+S_{\ell}+G_{1}+\cdots+G_{k}+F\right)\right)\right)=0$.

Proof. We denote by $C$ the sum $S_{1}+\cdots+S_{\ell}+G_{1}+\cdots+G_{k}$, i.e., $C:=S_{1}+\cdots+S_{\ell}+G_{1}+$ $\cdots+G_{k}$. By the Serre duality, it is enough to show $H^{0}\left(Z, \Omega_{Z}^{1}\left(\log (C+F)\left(K_{Z}\right)\right)\right)=0$. Note that the canonical divisor $K_{Z}=E$, since $K_{Y}=\mathcal{O}_{Y}$. By an abuse of notation, we abbreviate $\mathcal{O}_{S_{1}} \oplus \cdots \oplus \mathcal{O}_{S_{\ell}} \oplus \mathcal{O}_{G_{1}} \oplus \cdots \oplus \mathcal{O}_{G_{k}}$ to $\mathcal{O}_{C}$.

The proof uses the following commutative diagram and the snake lemma.
![](https://cdn.mathpix.com/cropped/be0c5d68-724d-411f-b8a7-87b22a960622-03.jpg?height=400&width=1424&top_left_y=834&top_left_x=337)
where $\mathcal{K}$ is the cokernel of the map from $\Omega_{Z}^{1}(\log (C+F+E))$ to $\Omega_{Z}^{1}(\log (C+F))(E)$ and $p, q$ are intersection points of $F$ and $E$. We have the short exact sequence
$$0 \rightarrow \mathcal{O}_{E} \rightarrow \Omega_{Z}^{1}(E) \otimes \mathcal{O}_{E} \rightarrow \Omega_{E}^{1}(E) \rightarrow 0 .$$
Then by the snake lemma, we have the short exact sequence
$$0 \rightarrow \Omega_{E}^{1}(E) \rightarrow \mathcal{K} \rightarrow \mathbb{C}_{p} \oplus \mathbb{C}_{q} \rightarrow 0 .$$
and we get $\mathcal{K}=\mathcal{O}_{E}(-1)$. Since $H^{0}\left(Z, \Omega_{Z}^{1}\right)=0$ and the first Chern class map from $H^{0}\left(\mathcal{O}_{C} \oplus \mathcal{O}_{F} \oplus \mathcal{O}_{E}\right)$ to $H^{1}\left(Z, \Omega_{Z}^{1}\right)$ is injective by the assumption of $C$, we get the vanishing $H^{0}\left(Z, \Omega_{Z}^{1}(\log (C+F+E))\right)=0$. And then we have the vanishing $H^{0}\left(Z, \Omega_{Z}^{1}(\log (C+\right.$ $F))(E))=0$. \(\square\)

We can keep the vanishing of the cohomology under the process of blowing up at a point by the following standard fact: Let $V$ be a nonsingular surface and let $D$ be a simple normal crossing divisor in $V$. Let $f: V^{\prime} \rightarrow V$ be the blow-up of $V$ at a point p on $D$. Let $D^{\prime}$ be the reduced divisor of the total transform of $D$. Then $h^{2}\left(V^{\prime}, T_{V^{\prime}}\left(-\log D^{\prime}\right)\right)=$ $h^{2}\left(V, T_{V}(-\log D)\right)$. Therefore, we get

Proposition 2.2. With the same assumptions and notation as in Proposition 2.1, we denote $D_{Z}:=\sum_{i=1}^{\ell} S_{i}+\sum_{i=1}^{k} G_{i}+F$. Let $\tau^{\prime}: Z^{\prime} \rightarrow Z$ be a successive blowing-up of points on $D_{Z}$. Let $D_{Z^{\prime}}$ be the reduced divisor of the total transform of $D_{Z}$ or the reduced divisor of the total transform of $D_{Z}$ minus some $(-1)$-curves. Then $H^{2}\left(Z^{\prime}, T_{Z^{\prime}}\left(-\log D_{Z^{\prime}}\right)\right)=0$.

Note that an $E(2)$ surface can be constructed as a double cover of an $E(1)$ surface. By using the double covering $E(2) \rightarrow E(1)$, together with the methods developed in [15], one can produce simply connected minimal surfaces of general type with $p_{g}=1$ and $q=0$. For example, such surfaces with $1 \leq K^{2} \leq 6$ are constructed in [22].

\section*{3. Construction of surfaces of general type with $p_{g}=q=0$ and $\pi_{1}=\mathbb{Z} / 2 \mathbb{Z}$ from Enriques surfaces}

Recall that every Enriques surface admits an elliptic fibration, and every elliptic fibration on an Enriques surface has exactly two multiple fibers, both of which have multiplicity 2. Every smooth rational curve on an Enriques surface is a (-2)-curve.

A singular fibre $F$ of an elliptic fibration is said to be of additive type, if the group consisting of simple points of $F$ contains the additive group $\mathbb{C}$, and of multiplicative type, if the group consisting of simple points of $F$ contains the multiplicative group $\mathbb{C}^{*}$. In the Kodaira's notation for singular fibers of elliptic fibration, a fibre of type II, III, IV, IV*, III*, II*, $\mathrm{I}_{\mathrm{n}}^{*}(n \geq 0)$ is of additive type, and a fibre of type $\mathrm{I}_{\mathrm{n}}(n \geq 1)$ is of multiplicative type. An additive type fibre is always a non-multiple fibre, and a fibre of multiplicity $m \geq 2$ must be of type $m \mathrm{I}_{\mathrm{n}}(n \geq 0)$, i.e., its reduced structure must be of type $\mathrm{I}_{\mathrm{n}}(n \geq 0)$.

Let $W$ be an Enriques surface and $f: W \rightarrow \mathbb{P}^{1}$ be an elliptic fibration on it. A smooth rational curve on $W$ is called a 2-section, if it intersects a fibre of $f$ with multiplicity 2. Let $V$ be the K3 cover of $W$, and $g: V \rightarrow \mathbb{P}^{1}$ the elliptic fibration induced by the elliptic fibration $f: W \rightarrow \mathbb{P}^{1}$, i.e., the normalization of the fibre product of $f: W \rightarrow \mathbb{P}^{1}$ and the double cover $\mathbb{P}^{1} \rightarrow \mathbb{P}^{1}$ branched at the base points of the two multiple fibres of $f$. A fibre of $f$ is non-multiple iff it splits into two fibres of $g$ of the same type. A multiple fibre of $f$ of type $2 \mathrm{I}_{\mathrm{n}}$ does not split and gives a fibre of $g$ of type $\mathrm{I}_{2 \mathrm{n}}$.

Lemma 3.1. If an elliptic fibration on an Enriques surface has a 2-section $S$, then for each fibre $F, S$ passes through $F$ in two distinct smooth points, if $F$ is not a multiple fibre; one smooth point of $F_{\text {red }}$, if $F=2 F_{\text {red }}$ is a multiple fibre.

Proof. Let $W$ be an Enriques surface and $f: W \rightarrow \mathbb{P}^{1}$ be an elliptic fibration on it. Let $V$ be the K3 cover of $W$. Since the double cover $V \rightarrow W$ is unramified, the 2-section $S$ splits into two sections $S_{1}, S_{2}$ of the elliptic fibration $g: V \rightarrow \mathbb{P}^{1}$ induced by the elliptic fibration $f: W \rightarrow \mathbb{P}^{1}$. Each $S_{i}$ passes through each fibre of $g$ in a smooth point. This implies the result. \(\square\)

Lemma 3.2. If an elliptic fibration on an Enriques surface has a singular fiber of type $\mathrm{I}_{9}$ or $2 \mathrm{I}_{9}$, then it has three singular fibers of type $\mathrm{I}_{1}$ or $2 \mathrm{I}_{1}$. In particular, the fibration always has at least one singular fiber of type $\mathrm{I}_{1}$.

Proof. Let $W$ be an Enriques surface and $f: W \rightarrow \mathbb{P}^{1}$ be an elliptic fibration on it. Let $J(f): J(W) \rightarrow \mathbb{P}^{1}$ be the Jacobian fibration of $f$. This is an elliptic fibration with a section having singular fibres of the same type, without multiplicity, as those of $f: W \rightarrow \mathbb{P}^{1}$ ([5], Theorem 5.3.1). In particular, the surface $J(W)$ is an $E(1)$ surface. Now assume that $f$ has a singular fiber of type $\mathrm{I}_{9}$ or $2 \mathrm{I}_{9}$. Then, $J(f)$ has a singular fiber of type $\mathrm{I}_{9}$. The result follows from the following lemma. \(\square\)

Lemma 3.3. If an $E(1)$ surface has a singular fiber of type $\mathrm{I}_{9}$, then it has three singular fibers of type $\mathrm{I}_{1}$.

Proof. Note that an $E(1)$ surface has Picard number 10 and topological Euler characteristic $c_{2}=12$. Since the elliptic fibration has a singular fiber of type $\mathrm{I}_{9}$, all other singular fibres must be irreducible. On the other hand, in this case the Mordell-Weil group, i.e., the group of sections of the elliptic fibration has order 3. The homomorphism from the Mordell-Weil group to the group consisting of simple points of every singular
fibre is injective. A singular fibre contains a 3-torsion point iff it is of type IV* or IV or $\mathrm{I}_{\mathrm{n}}(n \geq 1)$. So an irreducible singular fibre containing a 3-torsion point must be of type $\mathrm{I}_{1}$. Finally, a singular fiber of type $\mathrm{I}_{\mathrm{n}}$ has Euler number $n$. \(\square\)

The following will be used in proving the ampleness of $K_{X}$ of a singular surface $X$ obtained by contracting chains of smooth rational curves on a smooth surface $Z$.

Lemma 3.4. Let $Y$ be a smooth surface and $Z$ a blow-up of $Y$ at points $p_{1}, \ldots, p_{k}$, possibly infinitely near. Let $C$ be an irreducible curve on $Z$. Assume that $C$ has 1-dimensional image $C^{\prime}$ in $Y$. Then $K_{Z} . C=K_{Y} . C^{\prime}+\sum m_{i}$, where $m_{i}$ is the multiplicity of $C^{\prime}$ at the point $p_{i}$. If in addition $Y$ is an Enriques surface, then $K_{Z} . C=\sum m_{i} \geq 0$.

Let $\bar{Y}$ be an Enriques surface admitting an elliptic fibration $f: \bar{Y} \rightarrow \mathbb{P}^{1}$ with a 2-section whose singular fibers are either reducible or of type $m \mathrm{I}_{1}$ ( $m=1$ or 2). Let $\bar{S}_{1}, \ldots, \bar{S}_{\ell}$ be 2 -sections. These are $(-2)$-curves. Let
$$C_{\bar{Y}}:=\bar{S}_{1}+\ldots+\bar{S}_{\ell}+\bar{G}_{1}+\ldots+\bar{G}_{k},$$
where $\bar{G}_{i}$ is a (-2)-curve contained in a non-multiple singular fiber. We assume that the support of $\cup_{i=1}^{k} \bar{G}_{i}$ does not contain the support of a whole singular fiber. We also assume that the elliptic fibration $f: \bar{Y} \rightarrow \mathbb{P}^{1}$ has a singular fiber $F_{\bar{Y}}$ of type $\mathrm{I}_{1}$. By Lemma 3.1, no component of $C_{\bar{Y}}$ passes through the node of $F_{\bar{Y}}$. Let
$$\pi: \bar{Z} \rightarrow \bar{Y}$$
be the blow-up of $\bar{Y}$ at the node of $F_{\bar{Y}}$. Let $\bar{F}$ be the proper transform of $F_{\bar{Y}}$ and $\bar{E}$ be the (-1)-curve. Let $C_{\bar{Z}}$ be the proper transform of $C_{\bar{Y}}$. Since the exceptional curve $\bar{E}$ does not meet the locus of $C_{\bar{Z}}$, we use the same notation $\bar{S}_{1}, \ldots, \bar{S}_{\ell}, \bar{G}_{1}, \ldots, \bar{G}_{k}$ for their proper transforms. That is,
$$C_{\bar{Z}}=\bar{S}_{1}+\cdots+\bar{S}_{\ell}+\bar{G}_{1}+\cdots+\bar{G}_{k} .$$
We consider the unramified double cover
$$p: Z \rightarrow \bar{Z}$$
induced by the line bundle $L$ of $\bar{Z}$,
$$L=(\text { one multiple fiber })_{\text {red }}-(\text { the other multiple fiber })_{\text {red }} .$$
Note that $L^{2}=\mathcal{O}_{\bar{Z}}$ and $K_{\bar{Z}}=\bar{E}+L$. Let $Y \rightarrow \bar{Y}$ be the K3 cover, and $g: Y \rightarrow \mathbb{P}^{1}$ be the elliptic fibration induced by $f$. The surface $Z$ is also obtained by blowing up $Y$ at the nodes of the two singular fibers of type $\mathrm{I}_{1}$ lying over $F_{\bar{Y}}$. Let $E_{1}, E_{2}$ be the two (-1)-curves on $Z$. Then
$$K_{Z}=p^{*}\left(K_{\bar{Z}}+L\right)=p^{*} \bar{E}=E_{1}+E_{2} .$$
Let $C_{Z}^{1}, C_{Z}^{2}$ be the inverse image of $C_{\bar{Z}}$ in $Z, F_{1}, F_{2}$ the inverse image of $\bar{F}, S_{i}^{1}, S_{i}^{2}$ the inverse image of $\bar{S}_{i}$, and $G_{i}^{1}, G_{i}^{2}$ the inverse image of $\bar{G}_{i}$. We note that $S_{i}^{1}, S_{i}^{2}$ are sections, and for $j=1,2$
$$C_{Z}^{j}=S_{1}^{j}+\cdots+S_{\ell}^{j}+G_{1}^{j}+\cdots+G_{k}^{j} .$$
Here we also use abuse of notation,
$$\mathcal{O}_{C_{\bar{Z}}}:=\mathcal{O}_{\bar{S}_{1}} \oplus \cdots \oplus \mathcal{O}_{\bar{S}_{\ell}} \oplus \mathcal{O}_{\bar{G}_{1}} \oplus \cdots \oplus \mathcal{O}_{\bar{G}_{k}},$$
and for $j=1,2$
$$\mathcal{O}_{C_{Z}^{j}}:=\mathcal{O}_{S_{1}^{j}} \oplus \cdots \oplus \mathcal{O}_{S_{\ell}^{j}} \oplus \mathcal{O}_{G_{1}^{j}} \oplus \cdots \oplus \mathcal{O}_{G_{k}^{j}} .$$

Assume that the divisor $C_{\bar{Z}}+\bar{F}+\bar{E}$ is a simple normal crossing divisor. Then so is the divisor $C_{Z}^{j}+F_{j}+E_{j}$ for $j=1,2$. We have
$$p_{*}\left(\Omega_{Z}^{1}\left(K_{Z}\right)\right)=p_{*}\left(p^{*} \Omega_{\bar{Z}}^{1}\left(K_{Z}\right)\right)=p_{*} p^{*}\left(\Omega_{\bar{Z}}^{1}\left(K_{\bar{Z}}+L\right)\right)=\Omega_{\bar{Z}}^{1}\left(K_{\bar{Z}}\right) \oplus \Omega_{\bar{Z}}^{1}\left(K_{\bar{Z}}+L\right) .$$
Tensoring with $K_{Z}$ the short exact sequence
$$0 \rightarrow \Omega_{Z}^{1} \rightarrow \Omega_{Z}^{1}\left(\log \left(C_{Z}^{1}+C_{Z}^{2}+F_{1}+F_{2}\right)\right) \rightarrow \mathcal{O}_{C_{Z}^{1}} \oplus \mathcal{O}_{C_{Z}^{2}} \oplus \mathcal{O}_{F_{1}} \oplus \mathcal{O}_{F_{2}} \rightarrow 0,$$
we get the short exact sequence
$$0 \rightarrow \Omega_{Z}^{1}\left(K_{Z}\right) \rightarrow \Omega_{Z}^{1}\left(\log \left(C_{Z}^{1}+C_{Z}^{2}+F_{1}+F_{2}\right)\right)\left(K_{Z}\right) \rightarrow \mathcal{O}_{C_{Z}^{1}} \oplus \mathcal{O}_{C_{Z}^{2}} \oplus \mathcal{O}_{F_{1}}\left(E_{1}\right) \oplus \mathcal{O}_{F_{2}}\left(E_{2}\right) \rightarrow 0$$
because all curves in the support of $C_{Z}^{1} \cup C_{Z}^{2}$ are smooth rational curves that do not meet $E_{1}$ and $E_{2}$. Similarly, we have two exact sequences of sheaves in $\bar{Z}$,
$$\begin{aligned}
0 \rightarrow \Omega_{\bar{Z}}^{1}\left(K_{\bar{Z}}\right) & \rightarrow \Omega_{\bar{Z}}^{1}\left(\log \left(C_{\bar{Z}}+\bar{F}\right)\right)\left(K_{\bar{Z}}\right) \rightarrow \mathcal{O}_{C_{\bar{Z}}} \oplus \mathcal{O}_{\bar{F}}(\bar{E}) \rightarrow 0, \\
0 \rightarrow \Omega_{\bar{Z}}^{1}\left(K_{\bar{Z}}+L\right) & \rightarrow \Omega_{\bar{Z}}^{1}\left(\log \left(C_{\bar{Z}}+\bar{F}\right)\right)\left(K_{\bar{Z}}+L\right) \rightarrow \mathcal{O}_{C_{\bar{Z}}} \oplus \mathcal{O}_{\bar{F}}(\bar{E}) \rightarrow 0 .
\end{aligned}$$
Since $p: Z \rightarrow \bar{Z}$ is an unramified double cover, $p_{*}$ is an exact functor. Therefore we have $p_{*}\left(\Omega_{Z}^{1}\left(\log \left(C_{Z}^{1}+C_{Z}^{2}+F_{1}+F_{2}\right)\right)\left(K_{Z}\right)\right)=\Omega_{\bar{Z}}^{1}\left(\log \left(C_{\bar{Z}}+\bar{F}\right)\right)\left(K_{\bar{Z}}\right) \oplus \Omega_{\bar{Z}}^{1}\left(\log \left(C_{\bar{Z}}+\bar{F}\right)\right)\left(K_{\bar{Z}}+L\right)$. By a similar argument as in the proof of Proposition 2.1, we have $H^{0}\left(Z, \Omega_{Z}^{1}\left(\log \left(C_{Z}^{1}+C_{Z}^{2}+F_{1}+F_{2}\right)\right)\left(E_{1}+E_{2}\right)\right)=H^{0}\left(Z, \Omega_{Z}^{1}\left(\log \left(C_{Z}^{1}+C_{Z}^{2}+F_{1}+F_{2}+E_{1}+E_{2}\right)\right)\right)$. The involution $\iota$ induced from the double cover $p: Z \rightarrow \bar{Z}$ acts on $H^{0}\left(Z, \Omega_{Z}^{1}\left(\log \left(C_{Z}^{1}+\right.\right.\right.$ $\left.\left.\left.C_{Z}^{2}+F_{1}+F_{2}+E_{1}+E_{2}\right)\right)\right)$ and the $\iota$-invariant subspace is isomorphic to $H^{0}\left(\bar{Z}, \Omega_{\bar{Z}}^{1}\left(\log \left(C_{\bar{Z}}+\right.\right.\right.$ $\bar{F}+\bar{E})))$. And the $\iota$-invariant subspace is isomorphic to $H^{0}\left(\bar{Z}, \Omega_{\bar{Z}}^{1}\left(\log \left(C_{\bar{Z}}+\bar{F}\right)\right)\left(K_{\bar{Z}}\right)\right)$, because $\iota$-invariant part of the decomposition of $p_{*}\left(\Omega_{Z}^{1}\left(\log \left(C_{Z}^{1}+C_{Z}^{2}+F_{1}+F_{2}\right)\right)\left(K_{Z}\right)\right)$ is $\Omega_{\bar{Z}}^{1}\left(\log \left(C_{\bar{Z}}+\bar{F}\right)\right)\left(K_{\bar{Z}}\right)$. Therefore, by the Serre duality we have the following proposition.
Proposition 3.1. We assume that
\begin{itemize}
\item[(1)] $\bar{S}_{1}, \ldots, \bar{S}_{\ell}, \bar{G}_{1}, \ldots, \bar{G}_{k}, \bar{F}, \bar{E}$ are numerically independent in the Picard group of $\bar{Z}$.
\item[(2)] The divisor $\bar{S}_{1}+\cdots+\bar{S}_{\ell}+\bar{G}_{1}+\cdots+\bar{G}_{k}+\bar{F}+\bar{E}$ is a simple normal crossing divisor on $\bar{Z}$.
\item[(3)] $\bar{G}_{1}, \ldots, \bar{G}_{k}, \bar{F}$ are disjoint from two multiple fibers of the elliptic fibration on $\bar{Z}$.
\item[(4)] 2-sections $\bar{S}_{1}, \ldots, \bar{S}_{\ell}$ do not meet the exceptional curve $\bar{E}$.
\end{itemize}
Then $H^{2}\left(\bar{Z}, T_{\bar{Z}}\left(-\log \left(\bar{S}_{1}+\cdots+\bar{S}_{\ell}+\bar{G}_{1}+\cdots+\bar{G}_{k}+\bar{F}\right)\right)\right)=0$.
By the same argument as in Section 2, we also get the following proposition.
Proposition 3.2. With the same assumptions as in Proposition 3.1, we denote $D_{\bar{Z}}:=$ $\sum_{i=1}^{\ell} \bar{S}_{i}+\sum_{i=1}^{k} \bar{G}_{i}+\bar{F}$. Let $\tau^{\prime}: \bar{Z}^{\prime} \rightarrow \bar{Z}$ be a successive blowing-up of points on $D_{\bar{Z}}$. Let $D_{\bar{Z}}$, be the reduced divisor of the total transform of $D_{\bar{Z}}$ or the reduced divisor of the total transform of $D_{\bar{Z}}$ minus some $(-1)$-curves. Then $H^{2}\left(\bar{Z}^{\prime}, T_{\bar{Z}^{\prime}}\left(-\log D_{\bar{Z}^{\prime}}\right)\right)=0$.

By Proposition 3.2, one can construct surfaces of general type with $p_{g}=q=0$ and $\pi_{1}=\mathbb{Z} / 2 \mathbb{Z}$ by using an Enriques surface admitting a special elliptic fibration and the methods developed in [15].

According to Kondō (Example II in [13]), there is an Enriques surface $\bar{Y}$ admitting an elliptic fibration with a singular fiber of type $\mathrm{I}_{9}$, a singular fiber of type $\mathrm{I}_{1}$, and two 2-sections $\bar{S}_{1}$ and $\bar{S}_{2}$. Indeed, we take the 9 curves $F_{1}, F_{2}, F_{3}, F_{5}, F_{6}, F_{7}, F_{9}, F_{10}, F_{11}$ in

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/be0c5d68-724d-411f-b8a7-87b22a960622-07.jpg?height=518&width=649&top_left_y=397&top_left_x=724}
\captionsetup{labelformat=empty}
\caption{Figure 1. Enriques surface}
\end{figure}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/be0c5d68-724d-411f-b8a7-87b22a960622-07.jpg?height=503&width=602&top_left_y=1044&top_left_x=748}
\captionsetup{labelformat=empty}
\caption{Figure 2. $K^{2}=1$}
\end{figure}

Fig. 2.4, p. 207 in [13], which form a singular fiber of type $\mathrm{I}_{9}$ (on the other hand, the 9 curves $F_{1}, F_{2}, F_{3}, F_{5}, F_{8}, F_{7}, F_{9}, F_{10}, F_{11}$ form a singular fiber of type $2 \mathrm{I}_{9}$ ). Then by Lemma 3.2, the elliptic fibration has a singular fiber of type $\mathrm{I}_{1}$. Let $F_{\bar{Y}}$ be a singular fiber of type $\mathrm{I}_{1}$. By Lemma 3.1, every 2-section does not pass through the node of $F_{\bar{Y}}$. Finally we take the two curves $F_{4}$ and $F_{8}$ as 2-sections $\bar{S}_{1}$ and $\bar{S}_{2}$. The configuration of singular fibers and 2-sections on $\bar{Y}$ is given in Figure 1. Here we rename the components of the I9 fibre as $\bar{G}_{1}, \bar{G}_{2}, \ldots, \bar{G}_{9}$.

Example 3.1. Construction of surfaces of general type with $p_{g}=0, K^{2}=1$, and $\pi_{1}=\mathbb{Z} / 2 \mathbb{Z}$.

Consider the Enriques surface $\bar{Y}$ in Figure 1. We blow up at $\bar{G}_{6} \cap \bar{S}_{1}, \bar{G}_{8} \cap \bar{S}_{1}, \bar{G}_{2} \cap \bar{S}_{2}$, $\bar{G}_{9} \cap \bar{S}_{2}$, and $\bar{G}_{8} \cap \bar{G}_{9}$, to obtain a surface $\tilde{Z}=\bar{Y} \# 5 \overline{\mathbb{C} \mathbb{P}^{2}}$ with four disjoint linear chains of $\mathbb{P}^{1}$ 's as shown in Figure 2.
$$\text { o }^{-4}-\text { o }^{-2}-\text { o }^{-3}-\text { o }^{-2}, \text { o }^{-4}-\text { o }^{-2}-\text { o }^{-3}, \text { o }^{-2},- \text { o }^{-4}$$

It is not hard to see $\bar{S}_{1}, \bar{S}_{2}, \bar{G}_{1}, \bar{G}_{2}, \bar{G}_{3}, \bar{G}_{5}, \bar{G}_{6}, \bar{G}_{7}, \bar{G}_{8}, \bar{G}_{9}$ are numerically independent in the Picard group of $\bar{Z}=\bar{Y}$ : Set $a_{1} \bar{G}_{1}+a_{2} \bar{G}_{2}+a_{3} \bar{G}_{3}+a_{4} \bar{G}_{5}+a_{5} \bar{G}_{6}+a_{6} \bar{G}_{7}+a_{7} \bar{G}_{8}+$ $a_{8} \bar{G}_{9}+a_{9} \bar{S}_{1}+a_{10} \bar{S}_{s}$. Intersecting with $\bar{G}_{i}, \bar{S}_{j}, \bar{F}$ gives $a_{i}=0$.

Let $f: \tilde{Z} \rightarrow X$ be the contraction of the four linear chains of $\mathbb{P}^{1}$ 's in $\tilde{Z}$. By applying Proposition 3.1, Proposition 3.2, and $\mathbb{Q}$-Gorenstein smoothing theory from [15] to the singular surface $X$, we construct a smooth complex surface $X_{t}$ of general type with $p_{g}=0$ and $K^{2}=1$. It is easy to check that the fundamental group of $X_{t}$ is $\mathbb{Z} / 2 \mathbb{Z}$ by the calculation based on Van Kampen's theorem (see [15]): note that the index of the singular point obtained by contracting $\stackrel{-4}{\circ}^{-4}$ is 2, and the index of the singular point obtained by contracting $\stackrel{-4}{\circ}^{-\stackrel{-2}{\circ}^{-}} \stackrel{{ }^{-3}}{\circ}-\stackrel{{ }_{\circ}}{\circ}$ is 3 . The two indices are relatively prime.

We claim that the canonical divisor $K_{X}$, which is $\mathbb{Q}$-Cartier, is ample. To see this, we need to check $\left(f^{*} K_{X}\right) . C>0$ for every irreducible curve $C \subset \tilde{Z}$, not contracted by $f$. The adjunction formula gives
$$\left(f^{*} K_{X}\right) \cdot C=K_{\tilde{Z}} \cdot C+\left(\sum D_{p}\right) \cdot C,$$
where $D_{p}$ is an effective $\mathbb{Q}$-divisor supported on $f^{-1}(p)$ for each singular point $p$. Since $C$ is not contracted by $f,\left(\sum D_{p}\right) . C \geq 0$. If $K_{\tilde{Z}} . C>0$, then by the adjunction formula, $\left(f^{*} K_{X}\right) . C>0$. If $K_{\tilde{Z}} . C<0$, then by Lemma 3.4. $C$ is an exceptional curve for the blowing-up $\tilde{Z} \rightarrow \bar{Y}$, hence a $(-1)$-curve. If $K_{\tilde{Z}} . C=0$ and $p_{a}(C) \geq 1$, then the image $C^{\prime}$ of $C$ in the Enriques surface $\bar{Y}$ is 1-dimensional and irreducible. By Lemma 3.4, $C^{\prime}$ passes through none of $p_{i}$ 's and $p_{a}\left(C^{\prime}\right)=p_{a}(C)$. If $p_{a}\left(C^{\prime}\right) \geq 2$, then by the Hodge index theorem, $C^{\prime}$ intersects the elliptic configuration $\bar{S}_{1}+\bar{G}_{6}+\bar{G}_{7}+\bar{G}_{8}$. If $p_{a}\left(C^{\prime}\right)=1$, then $C^{\prime}$ is a fibre or a half fibre of an elliptic pencil. If $C^{\prime}$ is linearly equivalent to $\bar{S}_{1}+\bar{G}_{6}+\bar{G}_{7}+\bar{G}_{8}$ or to $2\left(\bar{S}_{1}+\bar{G}_{6}+\bar{G}_{7}+\bar{G}_{8}\right)$, then $C^{\prime} . \bar{G}_{5}>0$. If not, $C^{\prime} .\left(\bar{S}_{1}+\bar{G}_{6}+\bar{G}_{7}+\bar{G}_{8}\right)>0$. In any case, $C$ meets at least one of the 4 chains, so $\left(\sum D_{p}\right) . C>0$, and hence by the adjunction formula, $\left(f^{*} K_{X}\right) . C>0$. It remains to check $\left(f^{*} K_{X}\right) . C>0$ for every (-1)-curve $C$ and (-2)-curve $C$ not contracted by $f$. It is easy to check that every (-2)-curve $C$ not contracted by $f$ meets at least one of the four chains; by Lemma 3.4, every (-2)-curve $C$ on $\tilde{Z}$ comes from a (-2)-curve $C^{\prime}$ on $\bar{Y}$, and if $C^{\prime}$ does not intersect the 10 curves $\bar{S}_{1}, \bar{S}_{2}, \bar{G}_{1}, \bar{G}_{2}, \bar{G}_{3}, \bar{G}_{5}, \bar{G}_{6}, \bar{G}_{7}, \bar{G}_{8}, \bar{G}_{9}$, then the 11 curves will be numerically independent, a contradiction. So $\left(\sum D_{p}\right) . C>0$ and hence, $\left(f^{*} K_{X}\right) . C>0$. For each of the five (-1)-curves, a direct computation of $D_{p}$ shows that $\left(\sum D_{p}\right) . C>1$, hence $\left(f^{*} K_{X}\right) . C>0$.

Finally, note that the ampleness is an open condition for a proper morphism (cf. Proposition 1.41 in [12]), so a general fiber of a $\mathbb{Q}$-Gorenstein smoothing of $X$ has ample canonical class.

Example 3.2. Construction of surfaces of general type with $p_{g}=0, K^{2}=2$, and $\pi_{1}=\mathbb{Z} / 2 \mathbb{Z}$.

Consider the Enriques surface $\bar{Y}$ again in Figure 1. We blow up at $P_{1}, P_{4}$, and three times at $P_{5}$, and $\bar{G}_{6} \cap \bar{G}_{7}$, and $\bar{G}_{8} \cap \bar{S}_{1}$. Then we get a surface $\tilde{Z}=\bar{Y} \# 7 \overline{\mathbb{C} \mathbb{P}^{2}}$ with three disjoint linear chains of $\mathbb{P}^{1}$ 's as shown in Figure 3.
$$\circ^{-6}-\circ^{-2}-\circ^{-2}, \quad \circ^{-7}-\circ^{-3}-\circ^{-2}-\circ^{-2}-\circ^{-2}-\circ^{-2}, \quad \circ^{-3}-\circ^{-3}$$

It is not hard to see $\bar{S}_{1}, \bar{G}_{2}, \bar{G}_{3}, \bar{G}_{4}, \bar{G}_{5}, \bar{G}_{6}, \bar{G}_{7}, \bar{G}_{8}, \bar{F}, \bar{E}$ are numerically independent in the Picard group of $\bar{Z}$, the blow-up of $\bar{Y}$ at the node $P_{1}$ of the nodal fibre: Set $a_{1} \bar{S}_{1}+a_{2} \bar{G}_{2}+a_{3} \bar{G}_{3}+a_{4} \bar{G}_{4}+a_{5} \bar{G}_{5}+a_{6} \bar{G}_{6}+a_{7} \bar{G}_{7}+a_{8} \bar{G}_{8}+a_{9} \bar{F}+a_{10} \bar{E}=0$. Intersecting with $\bar{G}_{i}, \bar{S}_{j}, \bar{F}$ gives $a_{i}=0$. By applying $\mathbb{Q}$-Gorenstein smoothing theory to the singular

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/be0c5d68-724d-411f-b8a7-87b22a960622-09.jpg?height=503&width=604&top_left_y=397&top_left_x=748}
\captionsetup{labelformat=empty}
\caption{Figure 3. $K^{2}=2$}
\end{figure}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/be0c5d68-724d-411f-b8a7-87b22a960622-09.jpg?height=507&width=602&top_left_y=1027&top_left_x=750}
\captionsetup{labelformat=empty}
\caption{Figure 4. $K^{2}=3$}
\end{figure}
surface $X$ obtained by contracting three linear chains of $\mathbb{P}^{1}$ 's in $\tilde{Z}$, we construct a complex surface of general type with $p_{g}=0$ and $K^{2}=2$. Similarly, one can check that the fundamental group of this surface is $\mathbb{Z} / 2 \mathbb{Z}$ : note that the curve $\bar{G}_{9}$ in Figure 3 meets only one end curve in a linear chain of $\mathbb{P}^{1}$ which is contracted.

By the same argument as in the case of $K^{2}=1$, a general fiber of a $\mathbb{Q}$-Gorenstein smoothing of $X$ has ample canonical class. In this case, it is simpler to check the ampleness of $K_{X}$, as we contract the proper transform of a fibre.

Example 3.3. Construction of surfaces of general type with $p_{g}=0, K^{2}=3$, and $\pi_{1}=\mathbb{Z} / 2 \mathbb{Z}$.

Again consider the Enriques surface $\bar{Y}$ in Figure 1. We blow up at $P_{1}, P_{2}, P_{3}$, six times at $P_{5}$, twice at $P_{4}$, and at one of the two intersection points between $S_{2}$ and the singular fiber of type $\mathrm{I}_{9}$, to get a surface $\tilde{Z}=\bar{Y} \# 12 \overline{\mathbb{C P}^{2}}$ with three disjoint linear chains of $\mathbb{P}^{1}$ 's as shown in Figure 4.
$$\stackrel{-5}{\circ}^{-2}, \stackrel{-9}{\circ}^{-9}-\stackrel{-2}{\circ}^{-2}-\stackrel{-2}{\circ}^{-2}-\stackrel{-2}{\circ}^{\circ}, \stackrel{-2}{\circ}^{\circ}-\text { ० }^{-9}-\text { ० }^{-2}-\text { ० }^{-2}-\text { ० }^{-2}-\text { ० }^{-2}-\text { ० }^{-3}$$

Similarly, we see that $\bar{S}_{1}, \bar{S}_{2}, \bar{G}_{2}, \bar{G}_{3}, \bar{G}_{4}, \bar{G}_{5}, \bar{G}_{6}, \bar{G}_{9}, \bar{F}, \bar{E}$ are numerically independent in the Picard group of $\bar{Z}$, the blow-up of $\bar{Y}$ at the node $P_{1}$ of the nodal fibre: Set
$a_{1} \bar{S}_{1}+a_{2} \bar{S}_{2}+a_{3} \bar{G}_{2}+a_{4} \bar{G}_{3}+a_{5} \bar{G}_{4}+a_{6} \bar{G}_{5}+a_{7} \bar{G}_{6}+a_{8} \bar{G}_{9}+a_{9} \bar{F}+a_{10} \bar{E}=0$. Intersecting with $\bar{G}_{7}$ gives $a_{7}=0$, then intersecting with $\bar{G}_{8}$ gives $a_{1}+a_{8}=0$. Intersecting with $\bar{G}_{1}$ gives $a_{3}+a_{8}=0$, and intersecting with $\bar{G}_{6}$ gives $a_{1}+a_{6}=0$ by using $a_{7}=0$. We have $-2 a_{8}+a_{2}=0$ by intersecting with $\bar{G}_{9}$. Then intersecting with $\bar{G}_{2}$ produces $a_{2}-2 a_{3}+a_{4}=0$, and intersecting with $\bar{G}_{3}$ gives $a_{3}-2 a_{4}+a_{5}=0$. Intersecting with $\bar{G}_{4}$ gives $a_{4}-2 a_{5}+a_{6}=0$. These relations give $a_{8}=a_{6}=-a_{1}, a_{3}=a_{1}, a_{2}=-2 a_{1}, a_{4}=$ $4 a_{1}, a_{5}=7 a_{1}$, and $a_{6}=10 a_{1}$, But intersecting with $\bar{G}_{5}$ gives $-2 a_{6}+a_{5}=0$. So $a_{1}=0$, and $a_{2}=a_{3}=a_{4}=a_{5}=a_{6}=a_{8}=0$. Finally intersecting with $\bar{S}_{1}$ gives $a_{9}=0$, and intersecting with $\bar{F}$ produces $a_{10}=0$.

By applying $\mathbb{Q}$-Gorenstein smoothing theory to the singular surface $X$ obtained by contracting three linear chains of $\mathbb{P}^{1}$ 's in $\tilde{Z}$, we construct a complex surface of general type with $p_{g}=0$ and $K^{2}=3$. It is easy to check that the fundamental group of this surface is $\mathbb{Z} / 2 \mathbb{Z}$ : note that the index of the singular point obtained by contracting $\stackrel{-5}{\circ^{-}} \stackrel{-2}{\circ}^{-2}$ is 3 , and the index of the singular point obtained by contracting $\stackrel{-9}{\circ}-\stackrel{-2}{\circ}-\stackrel{-2}{\circ}-\stackrel{-2}{\circ}-\stackrel{-2}{\circ}-\stackrel{-2}{\circ}$ is 7 . The two indices are relatively prime.

As in the previous cases, one can show that a general fiber of a $\mathbb{Q}$-Gorenstein smoothing of $X$ has ample canonical class.

Remark 3.1. One can use other Enriques surfaces. For example, take the Enriques surface, Example VII in [13]. On this Enriques surface $\bar{Y}$, there is an elliptic fibration with a singular fiber of type $\mathrm{I}_{9}$, a singular fiber of type $\mathrm{I}_{1}$, and two 2-sections. Indeed, we take the 9 curves $E_{1}, E_{2}, E_{3}, E_{4}, E_{5}, E_{6}, E_{7}, E_{8}, E_{9}$ in Fig. 7.7, p. 233 in [13]. These form a singular fiber of type $\mathrm{I}_{9}$, as it splits in the K3 cover of $\bar{Y}$ as we see in Fig.7.3, $p$. 230. Then by Lemma 3.2, the elliptic fibration has a singular fiber of type $\mathrm{I}_{1}$. Let $F_{\bar{Y}}$ be a singular fiber of type $\mathrm{I}_{1}$. By Lemma 3.1, every 2-section passes through two smooth points of $F_{\bar{Y}}$. Finally we take the two curves $E_{10}$ and $E_{11}$ as 2-sections. Let $E_{10} \cap E_{11}=\left\{P_{1}\right\}, E_{10} \cap F_{\bar{Y}}=\left\{P_{2}, P_{3}\right\}, E_{11} \cap F_{\bar{Y}}=\left\{P_{4}, P_{5}\right\}$. Blowing up once at $P_{1}, P_{2}, P_{3}, P_{4}$, the node of $F_{\bar{Y}}$, and 5 times at $P_{5}$, we get a surface $\tilde{Z}=\bar{Y} \# 10 \overline{\mathbb{C} \mathbb{P}^{2}}$ with three disjoint linear chains of $\mathbb{P}^{1}$ 's
$$\stackrel{-5}{\circ}-\stackrel{-}{\circ}_{\circ}, \quad \circ^{-9}-\text { ० }^{-2}-\text { ० }^{-2}-\text { ० }^{-2}-\text { ० }^{-2}-\text { ० }^{-2}, \quad \text { ० }^{-8}-\text { ० }^{-2}-\text { ० }^{-2}-\text { ० }^{-2}-\text { ० }^{-2},$$
which leads to a construction of surfaces of general type with $p_{g}=0, K^{2}=3$, and $\pi_{1}=\mathbb{Z} / 2 \mathbb{Z}$.

Example 3.4. Construction of surfaces of general type with $p_{g}=0, K^{2}=4$, and $\pi_{1}=\mathbb{Z} / 2 \mathbb{Z}$.

We blow up at $P_{1}, P_{2}, P_{3}, S_{1} \cap \bar{G}_{6}$, and three times at $P_{5}$, and eight times at $\bar{G}_{6} \cap \bar{G}_{7}$ on the Enriques surface $\bar{Y}$ in Figure 1. We then get a surface $\tilde{Z}=\bar{Y} \# 15 \overline{\mathbb{C P}^{2}}$ with two disjoint linear chains of $\mathbb{P}^{1}$ 's as shown in Figure 5.
$$\begin{aligned}
& -2-{ }^{-2}-\stackrel{-9}{\circ}^{-2}-\stackrel{-2}{\circ}^{-2}-\stackrel{-2}{\circ}^{\circ}-\stackrel{-2}{\circ}^{-4}-\stackrel{-4}{\circ}^{-2}, \\
& { }^{-2}-\stackrel{-2}{\circ}^{-7} \stackrel{-}{\circ}^{-6}-\stackrel{-2}{\circ}^{-3}-\stackrel{-2}{\circ}^{-2}-\stackrel{-2}{\circ}^{-2}-\stackrel{-4}{\circ}^{-4}
\end{aligned}$$
Similarly, we see that $\bar{S}_{1}, \bar{S}_{2}, \bar{G}_{2}, \bar{G}_{3}, \bar{G}_{4}, \bar{G}_{5}, \bar{G}_{6}, \bar{G}_{7}, \bar{G}_{8}, \bar{F}, \bar{E}$ are numerically independent in the Picard group of $\bar{Z}$, the blow-up of $\bar{Y}$ at the node $P_{1}$ of the nodal fibre.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/be0c5d68-724d-411f-b8a7-87b22a960622-11.jpg?height=556&width=640&top_left_y=400&top_left_x=730}
\captionsetup{labelformat=empty}
\caption{Figure 5. $K^{2}=4$}
\end{figure}

By applying $\mathbb{Q}$-Gorenstein smoothing theory as in [15] to the singular surface $X$ obtained by contracting two linear chains of $\mathbb{P}^{1}$ 's in $\tilde{Z}$, we construct a complex surface of general type with $p_{g}=0$ and $K^{2}=4$. It is easy to check that the fundamental group of this surface is $\mathbb{Z} / 2 \mathbb{Z}$ by the same method. And as in the previous cases, a general fiber of a $\mathbb{Q}$-Gorenstein smoothing of $X$ has ample canonical class.

Example 3.5. Construction of a symplectic 4-manifold with $b_{2}^{+}=1, K^{2}=5$, and $\pi_{1}=\mathbb{Z} / 2 \mathbb{Z}$.

We consider the Enriques surface in Figure 1. According to Kondō [13] the Enriques surface has two $I_{1}$-singular fibers as in Figure 6. We blow up five times totally at the five marked points • as in Figure 6. We blow up again three times and four times at the two marked points $\odot$, respectively. We then get a surface $Z=\bar{Y} \# 12 \overline{\mathbb{C} \mathbb{P}^{2}}$; Figure 7. There exist two disjoint linear chains of $\mathbb{C P}^{1}$ 's in $Z$ :
$$\begin{aligned}
& { }^{-6} \text { отото } \\
& { }^{\circ}-{ }^{\circ}= \\
& \circ
\end{aligned}$$

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/be0c5d68-724d-411f-b8a7-87b22a960622-11.jpg?height=505&width=662&top_left_y=1893&top_left_x=718}
\captionsetup{labelformat=empty}
\caption{Figure 6. The Enriques surface}
\end{figure}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/be0c5d68-724d-411f-b8a7-87b22a960622-12.jpg?height=535&width=698&top_left_y=397&top_left_x=700}
\captionsetup{labelformat=empty}
\caption{Figure 7. Symplectic $K^{2}=5$}
\end{figure}

We now perform a rational blow-down surgery of the surface $Z=\bar{Y} \# 12 \overline{\mathbb{C P}^{2}}$. The rational blow-down $\tilde{Z}$ is a symplectic 4-manifold. Thus we get a symplectic 4-manifold $\tilde{Z}$ with $b_{2}^{+}=1$ and $K^{2}=5$. It is easy to show that $\pi_{1}\left(Z_{151,4}\right)=\mathbb{Z} / 2 \mathbb{Z}$.
\begin{itemize}
\item[(1)] One can prove that the symplectic 4-manifold $\widetilde{Z}$ constructed above is minimal by using a technique in Ozsváth and Szabó [18].
\item[(2)] It is an intriguing question whether the symplectic 4-manifold $\widetilde{Z}$ admit a complex structure. Since the cohomology $H^{2}\left(T_{X}^{0}\right)$ is not zero in this case, it is hard to determine whether there exists a global $\mathbb{Q}$-Gorenstein smoothing. We leave this question for future research.
\end{itemize}

Remark 3.2. A surface $X$ of general type with $p_{g}=0, K^{2}=k(1 \leq k \leq 7)$, and $\pi_{1}=\mathbb{Z} / 2 \mathbb{Z}$ provides an exotic structure on $3 \mathbb{C P}^{2} \#(19-2 k) \overline{\mathbb{C} \mathbb{P}^{2}}$. The universal double cover $Y$ of $X$ is a simply connected surface of general type with $p_{g}=1, c_{2}=24-2 k$, $b_{2}^{+}=3, b_{2}^{-}=19-2 k$. Its index $\sigma=16-2 k$ is not divisible by 16, so by Rohlin's Theorem [23] the intersection form on $H^{2}(Y, \mathbb{Z})$ is odd and then by Freedman's Theorem [7] $Y$ is homeomorphic to $3 \mathbb{C P}^{2} \#(19-2 k) \overline{\mathbb{C P}^{2}}$. By a result of Donaldson [6] or by a result of Friedman and Qin [8], $Y$ is not diffeomorphic to $3 \mathbb{C} \mathbb{P}^{2} \#(19-2 k) \overline{\mathbb{C} \mathbb{P}^{2}}$.

\section*{4. The case of an $E(3)$ surface}

In this section, we give a sufficient condition for the existence of a $\mathbb{Q}$-Gorenstein smoothing of a singular surface obtained from an $E$ (3) surface (Proposition 4.1). We also show that if the singular surface is obtained by contracting two disjoint sections and other curves, then it always has non-trivial obstruction space (Proposition 4.2).

Let $Y$ be an $E$ (3) surface. Let $F$ be a general fiber of the elliptic fibration $f: Y \rightarrow \mathbb{P}^{1}$, which is a smooth elliptic curve. Let $C$ be a section (it is a (-3)-curve), and let $G_{1}, \ldots, G_{k}$ be $(-2)$-curves in the union of singular fibers. Assume that the support of $\cup_{i=1}^{k} G_{i}$ does not contain the support of a whole singular fiber. We note that $K_{Y}=F$. Set $G:=G_{1}+\cdots+G_{k}$, and $\mathcal{O}_{G}:=\mathcal{O}_{G_{1}} \oplus \cdots \oplus \mathcal{O}_{G_{k}}$ for abbreviation.

Proposition 4.1. With the assumptions and the notation as above, assume further that $G_{1}, \ldots, G_{k}, F, C$ are numerically independent in the Picard group of $Y$. Then $H^{0}\left(Y, \Omega_{Y}^{1}(\log (C+G))(F)\right)=0$.

Proof. The proof is also obtained by the following commutative diagram and the snake lemma.
![](https://cdn.mathpix.com/cropped/be0c5d68-724d-411f-b8a7-87b22a960622-13.jpg?height=400&width=1424&top_left_y=509&top_left_x=337)
where $\mathcal{K}$ is the cokernel of the map from $\Omega_{Y}^{1}(\log (C+G+F))$ to $\Omega_{Y}^{1}(\log (C+G))(F)$ and $p$ is the intersection point of $F$ and $C$.

We have a short exact sequence
$$0 \rightarrow \mathcal{O}_{F} \rightarrow \Omega_{Y}^{1}(F) \otimes \mathcal{O}_{F} \rightarrow \Omega_{F}^{1}(F) \rightarrow 0,$$
and then by the snake lemma, another short exact sequence
$$0 \rightarrow \Omega_{F}^{1}(F) \rightarrow \mathcal{K} \rightarrow \mathbb{C}_{p} \rightarrow 0 .$$
We get $\mathcal{K}=\omega_{F}(p)$. So, $h^{0}(\mathcal{K})=1$. By the same argument as in the proof of Lemma 2 of [15], we get $H^{0}\left(Y, \Omega_{Y}^{1}(F)\right)=0$. Therefore $H^{0}\left(F, \omega_{F}(F)\right) \cong H^{0}(F, \mathcal{K})$ maps injectively into $H^{1}\left(Y, \Omega_{Y}^{1}\right)$, and its image contains no non-zero vector of the image of $H^{0}\left(\mathcal{O}_{C} \oplus\right.$ $\left.\mathcal{O}_{G} \oplus \mathcal{O}_{F}\right)$. It implies that $H^{0}(F, \mathcal{K})$ maps injectively into $H^{1}\left(Y, \Omega_{Y}^{1}(\log (C+G+F))\right)$.

Since $H^{0}\left(Y, \Omega_{Y}^{1}\right)=0$ and the first Chern class map from $H^{0}\left(\mathcal{O}_{C} \oplus \mathcal{O}_{G} \oplus \mathcal{O}_{F}\right)$ to $H^{1}\left(Y, \Omega_{Y}^{1}\right)$ is injective by the assumption, we get the vanishing $H^{0}\left(Y, \Omega_{Y}^{1}(\log (C+G+\right.$ $F)))=0$. And then we have the vanishing $H^{0}\left(Y, \Omega_{Y}^{1}(\log (C+G))(F)\right)=0$. \(\square\)

By the Serre duality, $H^{2}\left(Y, T_{Y}(-\log (C+G))\right)=0$. But if we choose two disjoint sections $C_{1}$ and $C_{2}$, then $H^{0}\left(Y, T_{Y}\left(-\log \left(C_{1}+C_{2}+G\right)\right)\right) \neq 0$.

Proposition 4.2. $H^{0}\left(Y, \Omega_{Y}^{1}\left(\log \left(C_{1}+C_{2}\right)\right)(F)\right) \neq 0$.
Proof. Consider the following commutative diagram as before.
![](https://cdn.mathpix.com/cropped/be0c5d68-724d-411f-b8a7-87b22a960622-13.jpg?height=397&width=1480&top_left_y=1908&top_left_x=335)
where $\mathcal{K}$ is the cokernel of the map from $\Omega_{Y}^{1}\left(\log \left(C_{1}+C_{2}+F\right)\right)$ to $\Omega_{Y}^{1}\left(\log \left(C_{1}+C_{2}\right)\right)(F)$ and $p=F \cap C_{1}, q=F \cap C_{2}$.

We have a short exact sequence
$$0 \rightarrow \mathcal{O}_{F} \rightarrow \Omega_{Y}^{1}(F) \otimes \mathcal{O}_{F} \rightarrow \Omega_{F}^{1}(F) \rightarrow 0 .$$

Then by the snake lemma, we have another short exact sequence
$$0 \rightarrow \Omega_{F}(F) \rightarrow \mathcal{K} \rightarrow \mathbb{C}_{p} \oplus \mathbb{C}_{q} \rightarrow 0 .$$
and we get $\mathcal{K}=\omega_{F}(p+q)$. Then the 1-dimensional subspace of $H^{0}(F, \mathcal{K})$, induced by the kernel of the map from $H^{0}\left(\mathbb{C}_{p, q}\right)$ to $H^{1}\left(F, \Omega_{F}^{1}(F)\right)$, maps to 0 in $H^{1}\left(Y, \Omega_{Y}^{1}\left(\log \left(C_{1}+\right.\right.\right.$ $\left.\left.\left.C_{2}+F\right)\right)\right)$. Therefore, $H^{0}\left(\Omega_{Y}^{1}\left(\log \left(C_{1}+C_{2}\right)\right)(F)\right)$ is a 1-dimensional space. \(\square\)

By Proposition 4.2, we cannot obtain from an $E(3)$ surface a singular surface $X$ with $K_{X}$ big, if we impose the vanishing of the obstruction space of $X$. Thus, to construct a surface of general type with $p_{g}=2$ and $q=0$, one cannot impose the vanishing of the obstruction space, and need to find a singular surface with an automorphism such that the obstruction space has trivial invariant part.

Example 4.1. Construction of a surface of general type with $p_{g}=2$ and $q=0$.
Let $D_{1}, D_{2}$ be two smooth conics in $\mathbb{P}^{2}$ such that $D_{1}$ and $D_{2}$ meet transversally at four points $p_{1}, \ldots, p_{4}$. Let $T$ be a smooth plane curve of degree 4 meeting $D_{1}, D_{2}$ transversally at four points $p_{1}, \ldots, p_{4}$. Let $V$ be a $(\mathbb{Z} / 2 \mathbb{Z})^{2}$-cover of $\mathbb{P}^{2}$ branched over $D_{1}, D_{2}$, and $T$. Then $V$ has four $\frac{1}{4}(1,1)$ singularities over $p_{1}, \ldots, p_{4}$, and $p_{g}(V)=2$, $\chi\left(\mathcal{O}_{V}\right)=3, K_{V}^{2}=4$. Its minimal resolution is an $E(3)$ surface with an elliptic fibration induced by the double cover of the pencil of conics $D_{t}$ generated by $D_{1}$ and $D_{2}$ branched over the four intersection points of $D_{t}$ and $T$ away from the four points $p_{1}, \ldots, p_{4}$. Then by the same argument as in [14] one can construct minimal surfaces of general type with $p_{g}=2, q=0$, and $1 \leq K^{2} \leq 4$.

Acknowledgements. Yongnam Lee would like to thank Noboru Nakayama for valuable discussions during the workshop in June, 2009 at RIMS in Kyoto University. Yongnam Lee was supported by the WCU Grant funded by the Korean Government (R33-2008-000-10101-0), and partially supported by the Special Research Grant of Sogang University. JongHae Keum was supported by the National Research Foundation of Korea funded by the Ministry of EST (NRF-2007-C00002).

\section*{References}
\begin{itemize}
\item[] [1] R. Barlow, Some new surfaces with $p_{g}=0$, Duke Math. J. 51 (1984), no. 4, 889-904.
\item[] [2] I. Bauer, F. Catanese, and R. Pignatelli, Surfaces of general type with geometric genus zero: a survey, math.AG arXiv:1004.2583
\item[] [3] I. Bauer and R. Pignatelli, The classification of minimal product-quotient surfaces with $p_{g}=0$, math.AG arXiv:1006.3209
\item[] [4] D. Cartwright and T. Steger, Enumeration of 50 fake projective planes, C. R. Acad. Sci. Paris, Ser. I 348 (2010), 11-13.
\item[] [5] F. Cossec and I. Dolgachev, Enriques surfaces I, Progress in Math., 76, Birkhäuser, 1989.
\item[] [6] S. K. Donaldson, Irrationality and the $h$-cobordism conjecture, J. Diff. Geom. 24 (1986), 275-341.
\item[] [7] M. Freedman, The topology of four-manifolds, J. Diff. Geom. 17 (1982), 357-453.
\item[] [8] R. Friedman and Z. Qin, On complex surfaces diffeomorphic to rational surfaces, Invent. Math. 120 (1995), 81-117.
\item[] [9] M. Inoue, Some new surfaces of general type, Tokyo J. Math. 17 no. 2 (1994), 295-319.
\item[] [10] J. Keum, Quotients of fake projective planes, Geom. Topol. 12 (2008), 2497-2515.
\item[] [11] K. Kodaira, On compact analytic surfaces II, Ann. of Math. (2) 77 (1963), 563-626.
\item[] [12] J. Kollár and S. Mori, Birational geometry of algebraic varieties, Cambridge Tracts in Mathematics, 134, 1998.
\item[] [13] S. Kondō, Enriques surfaces with finite automorphism groups, Japan. J. Math. 12 no. 2 (1986), 191-282.
\end{itemize}
[14] Y. Lee, Complex structure on the rational blowdown of sections in $E(4)$, Advanced Studies in Pure Mathematics, 60 (2010), 258-269.
[15] Y. Lee and J. Park, A simply connected surface of general type with $p_{g}=0$ and $K^{2}=2$, Invent. Math. 170 (2007), 483-505.
[16] Y. Lee and J. Park, A complex surface of general type with $p_{g}=0, K^{2}=2$ and $H_{1}=\mathbb{Z} / 2 \mathbb{Z}$, Math. Res. Lett. 16 (2009), 323-330.
[17] Y. Lee and J. Park, A construction of Horikawa surface via Q-Gorenstein smoothings, to appear in Math. Z.
[18] P. Ozsváth and Z. Szabó, On Park's exotic smooth four-manifolds, Geometry and Topology of Manifolds, Fields Institute Communications 47 (2005), 253-260, Amer. Math. Soc., Province, RI.
[19] H. Park, J. Park, D. Shin, A simply connected surface of general type with $p_{g}=0$ and $K^{2}=3$, Geom. Topol. 13 (2009), 743-767.
[20] H. Park, J. Park, D. Shin, A complex surface of general type with $p_{g}=0, K^{2}=3$ and $H_{1}=Z / 2 Z$, arXiv:0803.1322.
[21] H. Park, J. Park, D. Shin, A simply connected surface of general type with $p_{g}=0$ and $K^{2}=4$, Geom. Topol. 13 (2009), 1483-1494.
[22] H. Park, J. Park, D. Shin, A construction of surfaces of general type with $p_{g}=1$ and $q=0$, arXiv:0906.5195.
[23] V. A. Rohlin, New results in the theory of four-dimensional manifolds, Doklady Akad. Nauk. SSSR (N.S.) 84 (1952), 221-224.

Korea Institute for Advanced Study, 207-43 Cheongnyangni-dong, Seoul 130-722, Korea E-mail address: jhkeum@kias.re.kr

Department of Mathematics, Sogang University, Sinsu-dong, Mapo-gu, Seoul 121-742, and Korea Institute for Advanced Study, 207-43 Cheongnyangni-dong, Seoul 130-722, Ko-REA

E-mail address: ynlee@sogang.ac.kr
Korea Institute for Advanced Study, 207-43 Cheongnyangni-dong, Seoul 130-722, Korea
E-mail address: hspark@kias.re.kr