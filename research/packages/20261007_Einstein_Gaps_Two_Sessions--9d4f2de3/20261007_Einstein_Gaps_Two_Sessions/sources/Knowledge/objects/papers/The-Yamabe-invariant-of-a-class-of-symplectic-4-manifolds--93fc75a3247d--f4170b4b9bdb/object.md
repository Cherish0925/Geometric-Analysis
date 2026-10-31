# The Yamabe invariant of a class of symplectic 4-manifolds

- Category: papers
- Identity: doi:10.1016/j.geomphys.2015.01.016
- Content status: fulltext_ok

---

---
source_file: 1410_1236.pdf
converter: mathpix
format: mmd
---

\title{
THE YAMABE INVARIANT OF A CLASS OF SYMPLECTIC 4-MANIFOLDS
}

\author{
I. ŞUVAINA
}

\begin{abstract}
We compute the Yamabe invariant for a class of symplectic 4-manifolds of general type obtained by taking the rational blowdown of Kähler surfaces. In particular, for any point on the half-Noether line we exhibit a simply connected minimal symplectic manifold for which we compute the Yamabe invariant.
\end{abstract}

\section*{1. Introduction}

The four dimensional case plays a special role in the smooth topology of manifolds. Unlike in other dimensions, a given topological 4-manifold may admit infinitely many smooth structures, with different geometric properties. The smooth structures can be distinguish via invariants, such as the Yamabe invariant. This is, roughly speaking, the supremum of the scalar curvature of constant scalar curvature metrics with unit volume. For 4-manifolds, the sign and the value of the Yamabe invariant can change when changing the smooth structure.

When the manifold admits a Kähler or symplectic structure of general type, the Yamabe invariant is negative. Moreover, the invariant also depends on the decomposability of the smooth structure, under the operation of connected sum with complex projective spaces with the reversed orientation. More precisely, given a Kähler surface $M$ of non-negative Kodaira dimension LeBrun shows [16] that the invariant is equal to the Yamabe invariant of the minimal model $X$ of $M$ and equals:
$$Y(M)=Y(X)=-4 \pi \sqrt{2 c_{1}^{2}(X)} .$$
The strategy of his proof is to find first an upper bound and then show that there exists a sequence of metrics that optimizes it. In the case when the manifold is a Kähler surface or a symplectic 4-manifold of Kodaira dimension 0, 1, or 2, LeBrun shows [16] that the Yamabe invariant has an upper bound in terms of the topological invariants of the minimal model $X$ of $M$ :
$$Y(M) \leq-4 \pi \sqrt{2 c_{1}^{2}(X)} \leq 0$$

This gives a strong evidence that the Yamabe invariant is closely related to a topological invariant of a minimal model, but there is no general result in this direction. One has to be especially careful in the case of positive Yamabe invariant, where such a minimal model is not unique. For example $\mathbb{C P}^{2} \# 2 \overline{\mathbb{C} \mathbb{P}^{2}}$ is diffeomorphic $\left(\mathbb{C P}^{1} \times \mathbb{C P}^{1}\right) \# \overline{\mathbb{C P}^{2}}$. For these spaces, the $Y\left(\mathbb{C P}^{2}\right)=12 \sqrt{2} \pi$, [17], but the value of the Yamabe invariant of $\mathbb{C P}^{1} \times \mathbb{C P}^{1}$ is still unknown.

\footnotetext{
Date: November 27, 2024.
2000 Mathematics Subject Classification. Primary: 53C21, 53D05; Secondary: 57R18, 57R57.
Key words and phrases. symplectic 4-manifolds, orbifolds,Yamabe invariant.
}

An explicit computation of the invariant for generic spaces continues to elude us. LeBrun raised the question when the Yamabe bound (1.1) is optimized. Based on the fact that equality on one of the key estimates is obtained only for constant scalar curvature Kähler metrics, he conjectured that the Yamabe bound is optimized only in the Kähler case. We show that there is a large class of symplectic manifolds of general type for which the Yamabe invariant can be computed, and it is the expected one.

Theorem A. Let $M$ be a complex surface containing $s$ linear chains $C_{i}$ of rational curves, associated to the minimal resolution of a singularity of type $\frac{1}{n_{i}^{2}}\left(1, n_{i} m_{i}-1\right)$, with $m_{i}<n_{i}$, and $n_{i}, m_{i}$ relatively prime integers. We denote by $\widehat{M}$ the complex orbifold surface obtained by collapsing the chains $C_{i}$. Furthermore, let $\widehat{M}^{\prime}$ be the orbifold surface obtained from $\widehat{M}$ by collapsing all the rational curves of self-intersection (-2) which do not pass through the singular points. Assume that the canonical sheaf $K_{\widehat{M}}$ is ample. Then, the symplectic manifold $N$ obtained by taking the generalized rational blowdown of the chains $C_{i}$ in $M$ is a minimal, symplectic 4-manifold of general type, and its Yamabe invariant $Y(N)$ is
$$Y(N)=-4 \pi \sqrt{2 c_{1}^{2}(N)}=Y^{o r b}(\widehat{M})=Y^{o r b}\left(\widehat{M}^{\prime}\right) .$$

Moreover, if $N^{\prime}=N \# l \overline{\mathbb{C P}^{2}}$ then $Y\left(N^{\prime}\right)=Y(N)$.
Remark 1.1. If $M$ as above is a complex surface of general type then $Y(M)<Y(N)<0$. More precisely, $Y(M)^{2}=Y(N)^{2}+32 \pi^{2}\left(\sum_{i=1}^{s}\left|C_{i}\right|\right)$, where $\left|C_{i}\right|$ denotes the length of the chain $C_{i}$. Nevertheless, $M$ can be a rational surface (see examples in [19, 25]), or an elliptic surface, as the family of examples in Sect. 4.

The geometry of symplectic 4-manifolds is much richer than that of Kähler surfaces. One can obtain new examples by considering different types of surgeries, along symplectic or Langrangian submanifolds. These surgeries can be performed within the symplectic category due to Darboux type theorems, which allow us to establish canonical symplectic structures in the neighborhood of these submanifolds. Unfortunately, these techniques are not compatible with the gluing of the Riemannian structures. In this paper, we only consider one such surgery, the generalized rational blowdown. In Sect. 2 we present an approach to the generalized rational blowdown surgery, which can be used in conjunction with a construction of preferred metrics. This allows us to compute the Yamabe invariant from Theorem A in Sect. 3.

In general, it is difficult to decide if the new symplectic manifold constructed in Theorem A admits an integrable complex structure. However, the non-existence of such an integrable complex structure follows if the numerical invariants do not satisfy either the Noether, or the Miyaoka-Bogomolov-Yau inequality. For minimal complex manifolds with even $c_{1}^{2}(M)$, the Noether inequality is $5 c_{1}^{2}(M)-c_{2}(M)+36 \geq 0$, or equivalently $c_{1}^{2}(M) \geq 2 \chi_{h}(M)-6$, where $\chi_{h}(M)$ is the Todd genus, and can be computed in terms of the other topological invariants as $\chi_{h}(M)=$ $\frac{1}{12}\left(c_{2}(M)+c_{1}^{2}(M)\right)$. The minimality of the manifold implies that $c_{1}^{2}(M)>0$. The half-Noether line is defined to be $y=x-3, y>0$ and any minimal manifold $M$ that satisfies $c_{1}^{2}(M)=$ $2 \chi(M)+3 \tau(M)=\chi_{h}(M)-3$ is necessarily non-complex. We compute the Yamabe invariant for symplectic 4-manifolds which lie at any point on the half-Noether line.

Theorem B. For every point on the half-Noether line there is a simply connected, minimal, symplectic 4-manifold of general type $M$, for which the Yamabe invariant is
$$Y(M)=-4 \pi \sqrt{2 c_{1}^{2}(M)} .$$
Moreover, if $M^{\prime}=M \# l \overline{\mathbb{C P}^{2}}$ then $Y\left(M^{\prime}\right)=Y(M)$.

The above results rely on a special feature of the linear chains of curves considered. The boundary of a neighborhood of the linear chain $C_{i}$ is the lens space $L\left(n_{i}^{2}, n_{i} m_{i}-1\right)$. Essential in the construction is the existence of a rational homology ball $B_{n_{i}, m_{i}}$ which also has boundary $L\left(n_{i}^{2}, n_{i} m_{i}-1\right)$ (for more details see Sect. 2). To simplify the notation, we denote by $B_{n, m}$ the rational homology ball with boundary $L(n, n m-1)$ used in the generalized rational blowdown surgery. On these spaces, the author has proved the existence of preferred metrics:

Theorem 1.2. [28] The rational homology ball $B_{n, m}$ admits an asymptotically locally Euclidean (ALE) Ricci flat Kähler metric $g_{n, m}$. Moreover, any ALE Ricci flat Kähler surface $(X, g)$ with Euler characteristic $\chi(X)=1$ is isomorphic, up to rescaling, to $\left(B_{n, m}, g_{n, m}\right)$, for some integers $0<m<n, \operatorname{gcd}(n, m)=1$.

To prove this theorem it was essential to require that metric is asymptotically locally Euclidean (see Sect. 2 for the exact definition). This property allows us to construct a one point conformal compactification of $B_{n, m}$, which has positive orbifold Yamabe invariant, which in turn is used to prove Theorem A. More precisely, we prove the following proposition which is of independent interest:

Proposition C. The rational homology ball ( $B_{n, m}, g_{n, m}$ ) admits a one-point conformal compactification $\left(\widehat{B}_{n, m}, \widehat{g}_{n, m}\right)$ with positive orbifold conformal Yamabe
$$Y^{o r b}\left(\widehat{B}_{n, m},\left[\widehat{g}_{n, m}\right]\right)=Y\left(S^{4}\right) / n=\frac{8 \pi \sqrt{6}}{n} .$$
Moreover, there is no solution to the orbifold Yamabe problem on $\left(\widehat{B}_{n . m},\left[\widehat{g}_{n, m}\right]\right)$, i.e. there is no conformal metric $\widetilde{g}=e^{f} \widehat{g}_{n, m}, f \in C^{\infty}\left(\widehat{B}_{n, m}\right)$ having constant scalar curvature.

This proposition is an extension of Viaclovsky's result on ALE hyperkähler 4-manifolds [32, Theorem 1.3].

Behind most of the results in this paper is the Seiberg-Witten theory. This is essential in the computation of the invariant in Theorem 3.2 and the curvature bound 1.1. For Propositions 2.3 and 2.4, where Seiberg-Witten theory can be used in the proofs, we give alternative, topological or differential geometric arguments.

At the time when this paper was written, Suárez-Serrato and Torres [27] have posted a result on the computation of the Yamabe invariant for symplectic 4-manifolds of Kodaira dimension 0 and 1.

\section*{2. The generalized rational blowdown surgery}

The (generalized) rational blowdown is a surgery construction specific to dimension 4 introduced by Fintushel and Stern [8]. It is the analog of the blow-down construction in algebraic geometry, and it is motivated by the study of the local structure of cyclic quotient singularities.

In complex dimension two, quotient singularities of finite cyclic groups and their minimal resolution are well understood. We denote by $\mathbb{C}^{2} / \frac{1}{p}(1, q)$ the quotient of $\mathbb{C}^{2}$ by the finite cyclic group of order $p$ acting diagonally with weights 1 and $q$, for $q<p$ relatively prime integers. We say that we have a singularity of type $\frac{1}{p}(1, q)$. Its minimal resolution consists of a connected chain of transversal rational curves $E_{1}, \cdots, E_{k}$, with the self-intersection $E_{i}^{2}=-e_{i}, e_{i} \geq 2$ given by the Hirzebruch-Jung continued fraction
$$\frac{p}{q}=e_{1}-\frac{1}{e_{2}-\cdots \frac{1}{e_{k}}} .$$
A neighborhood of infinity is of the form $L(p, q) \times(T, \infty)$, where $L(p, q)$ denotes the lens space associated to $\mathbb{C}^{2} / \frac{1}{p}(1, q)$ and $T \gg 0$. In the case when the singularity is of type $\frac{1}{n^{2}}(1, n m-1)$, with $n, m$ relatively prime integers, Kollár and Shepherd-Barron [14] exhibit a one-parameter smoothing for which the associated Milnor fiber is a rational homology ball $B_{n, m}$. The induced complex structure $J$ on $B_{n, m}$ has the property that the $\mathrm{n}^{\text {th }}$ tensor product of the canonical line bundle, $K_{B_{n, m}}^{n}$, is trivial.

Let $M$ be a 4-manifold containing a linear chain $C_{n, m}$ of embedded 2-spheres $E_{1}, \cdots, E_{k}$, which have negative self-intersections ( $-e_{1}, \cdots,-e_{k}$ ), where $e_{i}$ are obtained by the continued fraction expansion of $\frac{n^{2}}{n m-1}$. We construct a manifold $N$ by removing a small tubular neighborhood of the configuration of spheres, and gluing in the rational homology ball $B_{n, m}$, by identifying the two neighborhoods of infinity which are of the form $L\left(n^{2}, n m-1\right) \times\left(T, T^{\prime}\right) \subset L\left(n^{2}, n m-1\right) \times$ $(T, \infty)$. This surgery was introduced by Fintushel and Stern [8] in the case when $m=1$, and it is called the rational blowdown. In general, the construction is known as the generalized rational blowdown. Symington [29, 30] proved that when $M$ is a symplectic manifold and the chain $C_{n, m}$ is formed by symplectic submanifolds, than the new manifold $N$ admits a symplectic structure. Throughout this paper, we do not emphasize a particular choice of a symplectic structure. The existence of one such structure is sufficient to prove the curvature estimate (3.3).

One can also consider Kähler surfaces $M$ containing configurations of complex submanifolds given by linear chains of rational curves in one of the above arrangements. A third manifold which is associated in a natural way to this construction is obtained by collapsing the chains of curves to singular points. We denote this by $\widehat{M}$. Artin's Contractibility Criterion tells us that $\widehat{M}$ has a complex structure, and as we used preferred configurations, the singularities are of type $\frac{1}{n^{2}}(1, n m-1)$. Locally, the generalized rational blowdown can be described as the $\mathbb{Q}$-Gorenstein smoothing of the quotient singularity [24]. In general, it is difficult to determine if the associated manifold $N$ is Kähler or not. In particular cases, as the examples in [19, 25], one can show that a global $\mathbb{Q}$-Gorenstein smoothing of $\widehat{M}$ exists and conclude that the manifold $N$ is in fact Kähler. In

Sect. 4 we give a family of examples for both cases, when the surgery yields Kähler, or non-Kähler manifolds.

Next, we emphasize some of the relations between the properties of the three manifolds. Propositions 2.1, 2.3 and 2.4 are stated for $M$ and $\widehat{M}$ Kähler surfaces as this is sufficient for our purposes. Similar statements hold for symplectic 4- manifolds, with almost identical proofs.

Proposition 2.1. Let $M$ be a Kähler surface containing $k$ linear chain configurations of negative self-intersection rational curves $C_{i}, i=1, \cdots, s$, associated to singularities of type $\frac{1}{n_{i}^{2}}\left(1, n_{i} m_{i}-\right.$ 1), with $n_{i}>m_{i}$ and relatively prime. Let $N$ denote the symplectic manifold obtained from $M$ by taking the generalized rational blowdown of these configurations of curves. Let $\widehat{M}$ be the complex orbifold surface obtained by collapsing these configurations to orbifold points. Then:
$$c_{1}^{2}(\widehat{M})=c_{1}^{2}(N)$$
(2) If all the $m_{i}=1$ then
$$\begin{aligned}
& c_{1}^{2}(N)=c_{1}^{2}(M)+\left(\sum_{i=1}^{s}\left(n_{i}-1\right)\right), \\
& c_{2}(N)=c_{2}(M)-\left(\sum_{i=1}^{s}\left(n_{i}-1\right)\right)
\end{aligned}$$
Proof. (1) The square of the first Chern class can be computed in terms of the orbifold Euler characteristic and the orbifold signature:
$$c_{1}^{2}(\widehat{M})=2 \chi^{\text {orb }}(\widehat{M})+3 \tau^{\text {orb }}(\widehat{M}) .$$

Moreover, the orbifold Euler characteristic and signature are related to the topological ones as follows:
$$\chi^{\operatorname{orb}}(\widehat{M})=\chi^{\operatorname{top}}(\widehat{M})-\sum_{i=1}^{s} \frac{\left|\Gamma_{i}\right|-1}{\left|\Gamma_{i}\right|}$$
and
$$\tau^{o r b}(\widehat{M})=\tau^{t o p}(\widehat{M})+\sum_{i=1}^{s} \eta\left(S^{3} / \Gamma_{i}\right)$$
where $\Gamma_{i}$ is the local group associated to the singularity, and $\eta\left(S^{3} / \Gamma_{i}\right)$ is the eta-invariant of the link of the quotient singularity. In our case $\left|\Gamma_{i}\right|$ is $n_{i}^{2}$, and the eta-invariant of the singularity is computed by Park [22, Lemma 3.2] to be:
$$\eta\left(S^{3} / \frac{1}{n^{2}}(1, n m-1)\right)=\frac{2}{3}\left(1-\frac{1}{n^{2}}\right)$$
Hence:
$$c_{1}^{2}(\widehat{M})=2 \chi^{o r b}(\widehat{M})+3 \tau^{o r b}(\widehat{M})=2 \chi^{t o p}(\widehat{M})+3 \tau^{t o p}(\widehat{M})$$

As $N$ is obtained from $\widehat{M}$ by removing the singular points and gluing in rational homology spheres, the Mayers-Vietoris sequence and Novikov's Additivity Theorem imply that
$$\chi^{\text {top }}(\widehat{M})=\chi(N), \tau^{\text {top }}(\widehat{M})=\tau(N) .$$
We have immediately:
$$2 \chi^{\text {top }}(\widehat{M})+3 \tau^{\text {top }}(\widehat{M})=2 \chi(N)+3 \tau(N)=c_{1}^{2}(N) .$$
(2) In the case when $m_{i}=1$, we only consider quotients of the form $\frac{1}{n_{i}^{2}}\left(1, n_{i}-1\right)$ for which the minimal resolution is a chain of $n_{i}-1$ spheres of self-intersection $\left(-\left(n_{i}+2\right),-2, \cdots,-2\right)$. Hence, the rational blow-down of such a configuration increases $c_{1}^{2}=2 \chi+3 \tau$ by $n_{i}-1$ and decreases $c_{2}=\chi$ by $n_{i}-1$, for each configuration. \(\square\)

Recall that a symplectic 4-manifold is called minimal if it does not contain symplectically embedded 2-spheres of self-intersection (-1).

Definition 2.2 ([16, 21]). A minimal symplectic 4-manifold $(M, \omega)$ is called of general type if it satisfies:
$$c_{1}^{2}(M)>0 \text { and } c_{1}(M) \cdot[\omega]<0,$$
where $c_{1}(M)$ is the first Chern class of an almost complex structure compatible with $\omega$. Moreover, a symplectic 4-manifold is called of general type if it is the iterated blow-up of a minimal symplectic manifold of general type.

This definition extends the classical one from the complex surface case. The first condition in the definition is topological. The second condition only depends on the underlying smooth structure and it is independent of the choice of the symplectic structure [21, Theorem 2.4].

Proposition 2.3. With the above notations, if $\left(\widehat{M}, \omega_{\widehat{M}}\right)$ is an orbifold Kähler surface such that $c_{1}^{2}(\widehat{M})>0$ and $c_{1}(\widehat{M}) \cdot\left[\omega_{\widehat{M}}\right]<0$ then $N$ is a symplectic manifold of general type.

Proof. As $c_{1}^{2}(\widehat{M})>0$, then $c_{1}^{2}(N)=c_{1}^{2}(\widehat{M})>0$, and we only need to show that $c_{1}(N) \cdot\left[\omega_{N}\right]<0$, or equivalently $c_{1}\left(K_{N}\right) \cdot\left[\omega_{N}\right]>0$, for some choice of $\omega_{N}$.

In order to simplify the notations, we show that $c_{1}(N) \cdot\left[\omega_{N}\right]<0$ in the case when $M$ contains only one configuration of curves of type $C_{n, m}$. The computations extend trivially to $s$ configurations of this type.

Let $M_{0}$ be the open manifold such that:
$$\begin{aligned}
M & =M_{0} \bigcup_{L\left(n^{2}, n m-1\right)} N b d\left(C_{n, m}\right), \\
\widehat{M} & =M_{0} \bigcup_{L\left(n^{2}, n m-1\right)} \mathbb{C}^{2} / \frac{1}{n^{2}}(1, n m-1), \\
N & =M_{0} \bigcup_{L\left(n^{2}, n m-1\right)} B_{n, m} .
\end{aligned}$$

On $M$ we consider the Kähler structure obtained from the pull-back of the Kähler structure on $\widehat{M}$ and adding a sufficiently small multiple of a Kähler structure on the $N b d\left(C_{n, m}\right)$ which is diffeomorphic to the minimal resolution of $\mathbb{C}^{2} / \frac{1}{n^{2}}(1, n m-1)$. Let $c_{1}\left(K_{N}\right)$ and $\omega_{N}$ be the canonical class and the symplectic form on $N$, constructed by Symington [29, 30]. Moreover, Symington shows that there is a symplectomorphism $\psi:\left(M_{0}, \omega_{N} \mid M_{0}\right) \rightarrow\left(M_{0}, \omega_{\widehat{M}} \mid M_{0}\right)$. Since $H^{1}\left(L\left(n^{2}, n m-\right.\right.$ $1), \mathbb{Q})=H^{2}\left(L\left(n^{2}, n m-1\right), \mathbb{Q}\right)=0$, we have that $c_{1}\left(K_{N}\right)$ and $\omega_{N}$ decompose as
$$c_{1}\left(K_{N}\right)=\left.c_{1}\left(K_{N}\right)\right|_{M_{0}}+\left.c_{1}\left(K_{N}\right)\right|_{B_{n, m}} \text { and }\left[\omega_{N}\right]=\left[\left.\omega_{N}\right|_{M_{0}}\right]+\left[\left.\omega_{N}\right|_{B_{n, m}}\right]$$
and as $\left(\left.K_{M}\right|_{B_{n, m}}\right)^{n}$ is trivial, then:
$$\begin{aligned}
c_{1}\left(K_{N}\right) \cdot\left[\omega_{N}\right] & =\left.c_{1}\left(K_{N}\right)\right|_{M_{0}} \cdot\left[\left.\omega_{N}\right|_{M_{0}}\right]=\psi_{*}\left(\left.c_{1}(K)\right|_{M_{0}}\right) \cdot \psi_{*}\left(\left[\left.\omega_{N}\right|_{M_{0}}\right]\right) \\
& =c_{1}\left(K_{\widehat{M}}\right) \cdot\left[\omega_{\widehat{M}}\right]>0 .
\end{aligned}$$ \(\square\)

The structure of $N$ is in fact intimately related to the properties of $\widehat{M}$, and not necessarily to those of $M$.

Proposition 2.4. Consider the complex orbifold surface $\widehat{M}^{\prime}$ obtained from $\widehat{M}$ by collapsing all the rational curves of self-intersection (-2) which do not pass through the singular points of $\widehat{M}$. If the canonical sheaf of $\widehat{M}^{\prime}$ is ample then $N$ is a minimal symplectic surface of general type.

Proof. Since $\widehat{M}^{\prime}$ has ample canonical sheaf, we have $c_{1}^{2}\left(\widehat{M}^{\prime}\right)>0$. Moreover, by the positive solution to the Calabi Conjecture for orbifolds, due to Kobayashi [13], there exists a Kähler-Einstien metric $g^{\prime}$ such that $\rho_{g^{\prime}}=\lambda \omega_{g^{\prime}}$, where $\rho_{g^{\prime}}$ is the Ricci form associated to $g^{\prime}$ and $\lambda<0$ is the Einstein constant. Then we have
$$c_{1}\left(\widehat{M}^{\prime}\right)\left[\omega_{g^{\prime}}\right]=\left[\frac{1}{2 \pi} \rho_{g^{\prime}}\right]\left[\omega_{g^{\prime}}\right]=\frac{1}{2 \pi} \lambda\left[\omega_{g^{\prime}}\right]^{2}<0 .$$
The projection $p: \widehat{M} \rightarrow \widehat{M}^{\prime}$ collapses only self-intersection (-2) rational curves, and hence $K_{\widehat{M}}=p^{*}\left(K_{\widehat{M^{\prime}}}\right)$. This implies that $c_{1}(\widehat{M})^{2}=c_{1}\left(K_{\widehat{M}}\right)^{2}=c_{1}\left(K_{\widehat{M^{\prime}}}\right)^{2}>0$. We can also construct a Kähler form on $\widehat{M}$ by taking the pull-back of the Kähler form $\omega_{g^{\prime}}$ and adding a small multiple of a Kähler form $\omega_{0}$ on $\widehat{M}$ :
$$\omega:=p^{*}\left(\omega_{g^{\prime}}\right)+\epsilon \omega_{0}, \epsilon>0 \text { sufficiently small. }$$
Then
$$c_{1}(\widehat{M})[\omega]=\left[\frac{1}{2 \pi} p^{*}\left(\rho_{g^{\prime}}\right)\right]\left[p^{*}\left(\omega_{g^{\prime}}\right)+\epsilon \omega_{0}\right]=\frac{1}{2 \pi} \lambda\left[\omega_{g^{\prime}}\right]^{2}+\epsilon c_{1}(\widehat{M}) \omega_{0}<0$$
for $\epsilon$ sufficiently small. Then, by Proposition 2.3, the manifold $N$ is of general type.
One method to show that $N$ is a minimal surface is by using Seiberg-Witten theory to show that $N$ has a unique basic class up to sign, see [22]. We omit this proof here, and instead we give a different proof in Sect. 3, using curvature estimates. \(\square\)

\section*{3. The Yamabe invariant and curvature estimates}

Let $M$ be a closed 4-manifold. We first define the Yamabe constant, $Y(M,[g])$, as an invariant of the conformal class of a Riemannian metric $g$ on $M$ :
$$Y(M,[g])=\inf _{\widetilde{g} \in[g]} \frac{\int_{M} s_{\widetilde{g}} d \mu_{\widetilde{g}}}{\operatorname{Vol}(\widetilde{g})^{\frac{1}{2}}},$$
where $[g]=\left\{\widetilde{g}=e^{f} g \mid f: M \rightarrow \mathbb{R}\right.$ smooth $\}$.
The Yamabe invariant is a diffeomorphism invariant of the manifold and is defined [12, 26] as:
$$Y(M)=\sup _{[g]} Y(M,[g]) .$$

We use an alternative description in the non-positive case which helps us to compute the invariant.

Proposition 3.1. Let $M$ be a smooth compact 4-manifold.
\begin{itemize}
\item[(1)] [5] Let [g] be a conformal class with negative Yamabe constant. Then
$$\inf _{\widetilde{g} \in[g]} \int_{M} s_{\widetilde{g}}^{2} d \mu_{\widetilde{g}}=|Y(M,[g])|^{2}$$
and this infimum is precisely achieved by the metrics of constant scalar curvature.
\item[(2)] [12, 26] If $Y(M) \leq 0$ then
$$\inf _{g} \int_{M} s_{g}^{2} d \mu_{g}=|Y(M)|^{2}$$
where the infimum is taken over all smooth Riemanian metrics $g$ on $M$.
\end{itemize}

Using this description, LeBrun was able to compute the Yamabe invariant in the case of Kähler surfaces of non-negative Kodaira dimension. He shows that:

Theorem 3.2 ([16], [18]). Let $M$ be obtained from a minimal Kähler surface $X$ of Kodaira dimension 0, 1 or 2 by blowing up $l \geq 0$ points. Then the Yamabe invariant $Y(M)$ is independent of $l$, and
$$Y(M)=-4 \pi \sqrt{2 c_{1}^{2}(X)} .$$
Moreover, this invariant is not attained if $l>0$.
3.1. The orbifold Yamabe invariant. Orbifold spaces appear naturally in the study of the moduli space of metrics on smooth manifolds [31, 1]. We only consider spaces with isolated singular points, where there exists a neighborhood $(U, p)$ of the singular point $p$ modeled by
$$\psi:(U, p) \rightarrow\left(B_{r_{0}}(0) / \Gamma_{p}, 0\right),$$
where $B_{r_{0}}$ is a ball of radius $r_{0}$ in $\mathbb{R}^{4}$ and $\Gamma_{p}$ is a finite subgroup of $O(4)$ acting freely on $\mathbb{R}^{4} \backslash$ $\{0\}$. An orbifold metric $g$ on $M$ is a Riemannian metric on the smooth part of $M$ and such that the pull-back of $\psi_{*}(g)$ on $B_{r_{0}}(0) \backslash\{0\}$ extends to a smooth Riemannian metric on $B_{r_{0}}(0)$. We denote by $\mathcal{M}^{\text {orb }}(M)$ the space of orbifold metrics on $M$, and by $[g]_{\text {orb }}=[g] \cap \mathcal{M}^{\text {orb }}(M)$ the
orbifold conformal class of $g$. The orbifold Yamabe constant of a conformal class and the orbifold Yamabe invariant of $M$ can be defined in an analogous way to the smooth case (see [3] for detailed definitions and properties).

Let $B_{n, m}$ be one of the rational homology balls discussed in Sect 2. In [28, Proposition 3.3], the author shows that $B_{n, m}$ admits an ALE Ricci flat Kähler metric $g_{n, m}$. The ALE requirement means that there exists a diffeomorphism,
$$\phi: U_{\infty} \rightarrow\left(\mathbb{C}^{2} \backslash B_{T}(0)\right) / \frac{1}{n^{2}}(1, n m-1), T \gg 0$$
between a neighborhood of infinity in $B_{n, m}$ and a neighborhood of infinity in $\mathbb{C}_{\left(z_{1}, z_{2}\right)}^{2} / \frac{1}{n^{2}}(1, n m-$ 1), such that $\phi_{*}\left(g_{n, m}\right)=g_{\text {Eucl }}+O\left(R^{-4}\right)$, where $R$ denotes the Euclidean radius. Then if we consider the change of coordinates $x_{i}=z_{i} / R^{2}, i=1,2$, we see that the rational homology ball $\left(B_{n, m}, g_{n, m}\right)$ admits a $C^{1, \alpha}$ conformal compactification with one orbifold point of type $\mathbb{C}^{2} / \frac{1}{n^{2}}(1, n m-1)$. We denote by $\widehat{B}_{n, m}$ the compactification.

Next, we prove that the results in the hyperkähler 4-case [32, Theorem 1.3] extend to the orbifold compactification of the rational homology ball $B_{n, m}$.

Proof of Proposition C. Notice that the existence of a $C^{\infty}$-orbifold conformal compactification $\left(\widehat{B}_{n, m},\left[\widehat{g}_{n, m}\right]\right)$ follows directly from [6, Proposition 12]. Moreover, the arguments in the proof of [6, Proposition 13] tell us that we can choose a metric $g_{\infty}$ in the conformal class of $\widehat{g}_{n, m}$ which has strictly positive scalar curvature everywhere. We can now conclude that $Y\left(\widehat{B}_{n, m},\left[\widehat{g}_{n, m}\right]\right)>0$. We remark that in order to apply Propositions 12 and 13 from [6] we only need ALE scalar flat anti-self-dual metrics, which is a condition much weaker than the ALE Ricci-flat Kähler condition.

On the other hand, [3, Theorem B] tells us that the orbifold Yamabe invariant is bounded from above in terms of the Yamabe invariant of the 4-sphere and the order of the group of the singularity, $|\Gamma|=n^{2}$ :
$$Y^{o r b}\left(\widehat{B}_{n, m}\right) \leq \frac{Y\left(S^{4}\right)}{\sqrt{|\Gamma|}}=\frac{8 \sqrt{6} \pi}{n} .$$
Moreover, Akutagawa [2, Theorem 3.1] shows that if the bound is strict than there exists a metric $\widetilde{g} \in\left[\widehat{g}_{n, m}\right]$ which has constant scalar curvature. On the other hand $B_{n, m}$ has fundamental group $\mathbb{Z} / n \mathbb{Z}$, and its universal covering is the manifold $A_{n-1}$, diffeomorphic to the minimal resolution of $\mathbb{C}^{2} / \frac{1}{n}(1, n-1)$. Given the covering map $c: A_{n-1} \rightarrow B_{n, m}$, then $\left(A_{n-1}, c^{*}\left(g_{n, m}\right)\right.$ is a hyperkähler 4-manifold. Hence, the existence of a metric of constant scalar curvature $\widetilde{g} \in\left[\widehat{g}_{n, m}\right]$ implies the existence of a constant scalar curvature metric in the orbifold conformal compactification class of $c^{*}\left(g_{n, m}\right)$. But Viaclovsky shows that this is impossible [32, Section 4.1]. Hence the orbifold Yamabe invariant is the maximal one, and there is no metric of constant scalar curvature in the given conformal class. \(\square\)
3.2. Curvature estimates. There are well-know relations between the $L^{2}$-norms of the curvature components and the topological invariants of 4-manifolds given by the Gauss-Bonnet theorem, or the Hirzebruch Signature theorem. As we consider manifolds with special geometries, Kähler or symplectic manifolds, there are additional curvature estimates which depend on the differentiable
structure (see for example [16]). In this paper we use the following key scalar curvature bound, which relies on the existence of a nontrivial Seiberg-Witten invariant:

Theorem 3.3 ([16, Theorem 4]). Let $(X, \omega)$ be a symplectic manifold, and let $M=X \# l \overline{\mathbb{C P}^{2}}$. If $b^{+}=1$, assume that $c_{1}(X) \cdot[\omega]<0$. Then any Riemannian metric on $M$ satisfies
$$\int_{M} s^{2} d \mu \geq 32 \pi^{2} c_{1}^{2}(X)$$

This bound is sharp in the case of minimal complex surfaces of Kodaira dimension 0, 1, or 2 [18, 16]. In general, the class of symplectic manifolds is much larger than that of Kähler surfaces, and we do not expect that the bound is optimal for an arbitrary manifold. However, we show that this bound is also sharp for the class of symplectic manifolds constructed in Sect. 2.

Theorem 3.4. Let $M$ be a compact complex surface containing $s$ configurations of rational curves of type $C_{n_{i}, m_{i}}$, with $m_{i}<n_{i}$ and $\operatorname{gcd}\left(n_{i}, m_{i}\right)=1$. Let $\widehat{M}^{\prime}$ be the orbifold surface obtained by collapsing these chains and all the rational curves of self-intersection $(-2)$ which are disjoint from these configurations. Assume that the canonical sheaf of $\widehat{M}^{\prime}$ is ample. Let $N$ be the manifold obtained by taking the generalized rational blowdown of the configurations $C_{n_{i}, m_{i}}$ in $M$. Then there exists a family of metrics $g_{t}$ on $N$ such that
$$\lim _{t \rightarrow 0^{+}} \int_{N} s_{g_{t}}^{2} d \mu_{g_{t}}=32 \pi^{2} c_{1}^{2}(N)$$
Moreoever, if $N^{\prime}=N \# l \overline{\mathbb{C P}^{2}}$, then there exists a family $g_{t}^{\prime}$ of metrics on $N^{\prime}$ such that
$$\lim _{t \rightarrow 0^{+}} \int_{N^{\prime}} s_{g_{t}^{\prime}}^{2} d \mu_{g_{t}^{\prime}}=32 \pi^{2} c_{1}^{2}(N)$$
Proof. The singular points of $\widehat{M}^{\prime}$ are isolated, of either type $\frac{1}{n^{2}}(1, n m-1)$, when a configuration of type $C_{n, m}$ is collapsed, or rational double points, in the case when a connected configuration of (-2) curves is contracted. The singularities of the last type are of the form $\mathbb{C}^{2} / G$, with $G \subset S U(2)$ finite subgroup, acting freely on $\mathbb{C}^{2} \backslash\{0\}$, and are called $A D E$ singularities, in correspondence with the Dynkin diagram associated to the configuration of curves appearing in the minimal resolution. We refer to the minimal resolution as the $A D E$-space. Then the manifold $N$ is obtained from the orbifold surface $\widehat{M}^{\prime}$ by removing the singular points and gluing in rational homology balls or $A D E$-spaces, respectively.

The proof of the theorem follows the line of arguments in [16], where a family of metrics saturating the bound in Theorem 3.3 is constructed. We give the explicit construction of these metrics.

Since the orbifold surface $\widehat{M}^{\prime}$ has ample canonical sheaf, then the solution of the orbifold version of the Calabi Conjecture [13] endows $\widehat{M}^{\prime}$ with an orbifold Kähler-Einstein metric $\hat{g}$. The scalar curvature $s_{\hat{g}}$ and Ricci form $\hat{\rho}$ of $\hat{g}$ satisfy:
$$\int_{\widehat{M}^{\prime}} s_{\hat{g}}^{2} d \mu_{\hat{g}}=8 \int_{\widehat{M}^{\prime}} \hat{\rho}^{2}=32 \pi^{2} c_{1}^{2}\left(\widehat{M}^{\prime}\right)$$

Consider $\hat{g}$-geodesic coordinates around each orbifold point of $\widehat{M}^{\prime}$ such that the metric $\widehat{g}=$ $g_{\text {Eucl }}+O\left(r^{2}\right)$, where $g_{\text {Eucl }}$ and $r$ denote the Euclidean metric and the radius associated with the chart, respectively. Let $h_{1}=g_{\text {Eucl }}-\widehat{g} \in O\left(r^{2}\right)$.

On the complement of the open neighborhood of infinity $U_{\infty} \subset B_{n, m}$ we decompose the metric $g_{n, m}$ as $g_{E u c l}+h_{2}$, with $h_{2} \in O\left(R^{-4}\right)$. We change the coordinates of $U_{\infty} \cong\left(\mathbb{C}^{2} / \frac{1}{n^{2}}(1, n m-\right.$ $\left.1) \backslash B_{T}(0)\right)$ such that $U_{\infty} \cong\left(\mathbb{C}^{2} / \frac{1}{n^{2}}(1, n m-1) \backslash B_{\frac{t}{2}}(0)\right)$, and then rescale the metric. Then, on $B_{n, m}$ we have a family of charts at infinity defined for $r>\frac{t}{2}$ such that the ALE Ricci-flat Kähler metric is asymptotically of the form $g_{\text {Eucl }}+h_{2}^{\prime}$, with $h_{2}^{\prime} \in O\left(t^{2}\right)$. The volume of the compact set $B_{n, m} \backslash U_{\infty}$ is rescaled by a factor of $\left(\frac{t}{2 T}\right)^{4}$. The $A D E$-spaces have hyperkähler metrics $g_{h y p}$, with the same asymptotic description [15]. Hence, we can introduce a common notation for a neighborhood of infinity, and the metric decomposition in both cases. For the rest of the proof $\left(U_{\infty}, g_{\infty}\right)$ denotes a neighborhood of infinity in $B_{n, m}$ or in an $A D E$-space, which is isometric to $\left(\mathbb{C}^{2} / G \backslash B_{\frac{t}{2}}(0), g_{E u c l}+h_{2}^{\prime}\right)$, where $G$ is $\frac{1}{n^{2}}(1, n m-1) \subset U(2)$ or $G \subset S U(2)$, respectively.

In order to define a metric on $N$, we remove a ball of radius $t$ around each singularity in $\widehat{M}^{\prime}$ and glue in a rational homology ball $B_{n, m}$ or an $A D E$-space. The new metric interpolates between the metric $\widehat{g}$ and the rescaling of the metric $g_{n, m}$ or $g_{h y p}$ in the region $t<r<2 t$, for some small parameter $t$. As the gluing is done by identifying the region $\left\{z \in \mathbb{C}^{2} / G|t<|z|<2 t\} \subset U_{\infty}\right.$ to a region given by the same local coordinates in a neighborhood of a singular point in $\widehat{M}^{\prime}$, we can do the gluing on the covering $\left\{z \in \mathbb{C}^{2}|t<|z|<2 t\}\right.$.

Let $\phi:[0,4] \rightarrow \mathbb{R}$ be a non-negative smooth function such that $\phi$ is identically 1 on the interval [0,1] and identically 0 on the interval [2,4]. We define the metric $g_{t}$ on the larger collar $\{z \in$ $\mathbb{C}^{2}\left|\frac{t}{2}<|z|<4 t\right\}$ :
$$g_{t}:=\widehat{g}+\phi\left(\frac{r}{t}\right)\left(h_{1}+h_{2}\right) .$$
Then for $r>2 t$ the metric $g_{t}$ is identical to $\widehat{g}$, while for $\frac{t}{2}<r<t$ the metric is the rescaled metric $g_{\infty}$. Hence, we have defined a family of metrics $\left(N, g_{t}\right)$.

On the interpolation region $t<r<2 t$ we have the following uniform bounds:
$$\begin{aligned}
\left\|g_{t}-g_{E u c l}\right\| & \leq C t^{2} \\
\left\|D g_{t}\right\| & \leq C t \\
\left\|D^{2} g_{t}\right\| & \leq C
\end{aligned}$$
where $D$ is the Euclidean derivative operator associated with the given coordinate system, and the constant $C$ is independent of $t$. Then $s_{g_{t}}^{2}$ is uniformly bounded as $t \rightarrow 0$. Since the volume of the annular transition region goes to zero, we have:
$$\lim _{t \rightarrow 0^{+}} \int_{N} s_{g_{t}}^{2} d \mu_{g_{t}}=\int_{\widehat{M}} s_{\widehat{g}}^{2} d \mu_{\widehat{g}}=32 \pi^{2} c_{1}^{2}(\widehat{M})=32 \pi^{2} c_{1}^{2}(N)$$

The blow-up manifold, $N^{\prime}=N \# l \overline{\mathbb{C P}^{2}}$, can be obtained from $N$ by removing $l$ smooth points and gluing in the total space of $\mathcal{O}_{\mathbb{C P}^{1}}(-1)$, for each of the points. The total space of $\mathcal{O}_{\mathbb{C P}^{1}}(-1)$ admits an ALE scalar flat Kähler metric called the Burns metric. The family $g_{t}^{\prime}$ satisfying equation 3.5 can be obtained from the family of metrics $g_{t}$ using the explicit gluing in [16, Sect. 5]. \(\square\)

Remark 3.5. There is no a priori reason for the family of Riemannian metrics in the above construction to be compatible with an underlying symplectic structure.

Then, we immediately have that:
Corollary 3.6. For $N$ and $N^{\prime}$ given above we have:
$$\inf _{g} \int_{N} s_{g}^{2} d \mu_{g}=\inf _{g} \int_{N^{\prime}} s_{g}^{2} d \mu_{g}=32 \pi^{2} c_{1}^{2}(N),$$
(2) the Yamabe invariant $Y(N)=Y\left(N^{\prime}\right)=-4 \sqrt{2 c_{1}^{2}(N)}$.

Proof. Part (1) is a consequence of the above proposition and the curvature bound in Theorem 3.3. Part (2) follows from Proposition 3.1, and the fact that the symplectic manifolds of general type have negative Yamabe invariants [16]. \(\square\)

We can now give a proof for the second part of Proposition 2.4:
Proof of minimality in Proposition 2.4. Assume that the manifold $N$ is obtained by blowing up the symplectic manifold $X$ at $l^{\prime}>0$ points, $N=X \# l^{\prime} \overline{\mathbb{C} \mathbb{P}^{2}}$. Then $c_{1}^{2}(N)=c_{1}^{2}(X)-l^{\prime}$, and by Theorem 3.3:
$$\int_{N} s_{g}^{2} d \mu_{g} \geq 32 \pi^{2} c_{1}^{2}(X)=32 \pi^{2}\left(c_{1}^{2}(N)+l^{\prime}\right), l^{\prime}>0$$
for any metric $g$ on $N$. But this is in contradiction with Corollary 3.6. \(\square\)

Proof of Theorem A. Proposition 2.4 implies that $N$ is a minimal symplectic manifold of general type. Moreover, Corollary 3.6 and Proposition 2.1 tell us that:
$$Y(N)=Y\left(N^{\prime}\right)=-4 \pi \sqrt{2 c_{1}^{2}(N)}=-4 \pi \sqrt{2 c_{1}^{2}(\widehat{M})} .$$
Moreover, as $p^{*}\left(K_{\widehat{M^{\prime}}}\right)=K_{\widehat{M}}$, the above equality also equals $-4 \pi \sqrt{c_{1}^{2}\left(\widehat{M^{\prime}}\right)}$. We only need to show that the orbifold Yamabe invariants of $\widehat{M}$ and $\widehat{M}^{\prime}$ are the expected ones. In order to do this, we generalize Theorem B in [2] to include orbifolds which have singularities of type $\frac{1}{n^{2}}(1, n m-1)$.

We can give a second description of the manifold $N$ as the connected sum of the orbifold spaces $\widehat{M}$ and $\widehat{B}_{n_{i}, m_{i}}, i=1, \ldots, s$ at the singular points. Similarly, $\widehat{M}$ can be obtained by taking the connected sum of $\widehat{M}^{\prime}$ and the one-point compactifications of $A D E$-spaces.

In [2], Akutagawa considers the connected sum of two orbifold 4-spaces $M_{1}$ and $M_{2}$ at two isolated orbifold points of type $\mathbb{R}^{4} / \Gamma$ :
$$N:=M_{1} \#_{S^{3} / \Gamma} M_{2} .$$
He proves that if $Y(N)<0$ and $Y^{\text {orb }}\left(M_{2}\right)>0$ then $Y^{\text {orb }}\left(M_{1}\right) \leq Y(N) \leq 0$. Proposition C tells us that the one-point compactification $\left(\widehat{B}_{n, m},\left[\widehat{g}_{n, m}\right]\right)$ has positive Yamabe invariant. Applying Theorem A in [2] for $M_{1}=\widehat{M}$ and $M_{2}=\widehat{B}_{n, m}$ we see that $Y^{\text {orb }}(\widehat{M}) \leq Y(N)<0$.

The one point conformal compactification of an $A D E$-space has positive Yamabe invariant [32, Theorem 1.3], and similarly, we have $Y^{\text {orb }}\left(\widehat{M}^{\prime}\right) \leq Y^{\text {orb }}(\widehat{M})$.

On the other hand, $\widehat{M}^{\prime}$ admits a Kähler-Einstein metric $\widehat{g}$ given by the positive solution of the Calabi conjecture [13]. This is the Yamabe minimizer in its conformal class, and satisfies:
$$\frac{\int_{\widehat{M}^{\prime}} s_{\widehat{g}} d \mu_{\widehat{g}}}{\operatorname{Vol}^{\frac{1}{2}}(\widehat{g})}=s_{\widehat{g}}=-\sqrt{32 \pi^{2} c_{1}^{2}\left(\widehat{M}^{\prime}\right)}=-\sqrt{32 \pi^{2} c_{1}^{2}(N)}=Y(N) .$$
Then we have that $Y^{\text {orb }}\left(\widehat{M}^{\prime}\right)=Y(N)=-4 \pi \sqrt{2 c_{1}^{2}\left(\widehat{M}^{\prime}\right)}$, and so $Y^{\text {orb }}\left(\widehat{M}^{\prime}\right)=Y^{\text {orb }}(\widehat{M})$. \(\square\)

\section*{4. An explicit family of symplectic, non-Kähler examples}

The family of examples described in this section was first introduced by Fintushel and Stern [8], and later reconsidered by Y. Lee and J. Park [20]. In this paper, we follow the second description.

Let $E(n)$ be the relatively minimal, simply connected elliptic surfaces with sections, which have Euler characteristic $\chi(E(n))=12 n$. The diffeomorphism type of $E(n)$ is unique [10, Theorem 3.2.9], but the complex structure might vary. For $n \geq 4$, Lee and Park [20] exhibit such a preferred complex structure with two sections of self-intersection $(-n)$, which are part of two disjoint configurations of $(n-3)$ curves of type $(-n,-2, \cdots,-2)$. Let $\widehat{X}_{n}$ be the manifold obtained by contracting one chain of type $(-n,-2, \cdots,-2)$ to a singular point $P$ of type $\frac{1}{(n-2)^{2}}(1, n-3)$, and the $(n-4)$ spheres of self-intersection (-2) from the second chain to a singular point $Q$ of type $\frac{1}{n-3}(1, n-4)$. We have:

Proposition 4.1. For every $n \geq 4$, there exists an orbifold surface $\widehat{X}_{n}$ with two orbifold points of type $\frac{1}{(n-2)^{2}}(1, n-3)$ and $\frac{1}{n-3}(1, n-4)$, such that its canonical sheaf is ample and $c_{1}^{2}\left(\widehat{X}_{n}\right)=n-3$.

Proof. The first case, when $n=4$ appeared earlier in the work of Gompf [9], and the surface $\widehat{X}_{4}$ has only one orbifold point, which is of type $\frac{1}{4}(1,1)$. For clarity, we treat this case separately.

Let $\Sigma(4)=\mathbb{P}\left(\mathcal{O}_{\mathbb{C P}^{1}} \oplus \mathcal{O}_{\mathbb{C P}^{1}}(4)\right)$ be the Hirzebruch surface with a negative section of selfintersection (-4). We denote by $C_{0}$ the negative self-intersection section, and by $f$ a generic fiber. Let $D$ be a smooth complex curve in the linear system $\left|4\left(C_{0}+4 f\right)\right|$. The double cover of $\Sigma(4)$ branched along $D$ is the elliptic surface $E(4)$. As the branch locus $D$ is disjoint from $C_{0}$, the pullback of $C_{0}$ has two connected components, which are both sections of the elliptic fibration and have self-intersection (-4). We denote them by $C_{1}$ and $C_{2}$. Gompf shows that if we consider the rational blowdown of both $C_{1}$ and $C_{2}$ the new manifold admits a complex structure, and it is a Horikawa surface [4], while if we consider the rational blowdown of only one curve the new symplectic 4-manifold does not admit a complex structure. Let $\widehat{X}_{4}$ be the orbifold surface obtained by collapsing only $C_{2}$. Following the description of $E(4)$ as a double cover $d: E(4) \rightarrow$ $\Sigma(4)$, we can compute the canonical divisor [4, Lemma 17.1]:
$$\begin{aligned}
K_{\Sigma(4)} & =-2 C_{0}-6 f \\
K_{E(4)} & =d^{*}\left(K_{\Sigma(4)}+\frac{1}{2} D\right) \\
& =d^{*}\left(-2 C_{0}-6 f+2\left(C_{0}+4 f\right)\right)=d^{*}(2 f)=2 F,
\end{aligned}$$
where $F=d^{*}(f)$ is a generic fiber of the elliptic fibration. Let $\pi: E(4) \rightarrow \widehat{X}_{4}$ be the map given by collapsing the curve $C_{2}$ to an orbifold point of type $\frac{1}{4}(1,1)$, and let $f^{\prime}=\pi_{*}(F)$. Then the canonical divisor of $\widehat{X}_{4}$ is $K_{\widehat{X}_{4}}=2 f^{\prime}$. The pull-back of $f^{\prime}$ is $\pi^{*}\left(f^{\prime}\right)=F+\frac{1}{4} C_{2}$, which implies that
$$f^{\prime 2}=\left(\pi^{*}\left(f^{\prime}\right)\right)^{2}=F^{2}+\frac{1}{2} F \cdot C_{2}+\frac{1}{16} C_{2}^{2}=0+\frac{1}{2}-\frac{1}{4}=\frac{1}{4} .$$
As we can choose a representative of $f^{\prime}$ to pass through any point of $\widehat{X}_{4}$, the Nakai-Moishezon criterion implies that $f^{\prime}$ is an ample divisor and as a consequence $K_{\widehat{X}_{4}}$ is ample. Moreover, we have $K_{\widehat{X}_{4}}^{2}=4 f^{\prime 2}=1$.

For $n \geq 5$, we use the complex structure on $E(n)$ given by the construction in [20]. In the Hirzebruch surface $\Sigma(n)=\mathbb{P}\left(\mathcal{O}_{\mathbb{C P}^{1}} \oplus \mathcal{O}_{\mathbb{C P}^{1}}(n)\right)$, let $f_{0}$ be a fixed fiber and $C_{0}$ the negative section with $C_{0}^{2}=-n$. Lee and Park show [20] that the linear system $\left|4\left(C_{0}+n f\right)\right|$ contains a complex divisor, $D$, which has exactly two singular points $p$, and $q$, both lying on $f_{0}$. If $(x, y)$ are the local coordinates at $p$ (respectively at $q$ ), such that the fiber $f_{0}$ is given by ( $x=0$ ), then the equation of $D$ is given by $(y-x)(y+x)=0\left(\left(y-x^{n-4}\right)\left(y+x^{n-4}\right)=0\right.$, respectively). We resolve the singularities of $D$ by blowing up $\Sigma(n)$ at $p$ once, and $(n-4)$ times at $q$. We denote by $\Delta$ the proper transform of $D$. To be consistent with the notation in [20], we denote the first blowup by $E_{1}$, and proper transform of the blow-ups at $q$ by $U_{n-5}, \ldots, U_{1}, E_{2}$. Notice that $E_{1,2}$ are self-intersection ( -1 ) rational curves, while $U_{i}, i=1, \ldots, n-5$ have self-intersection ( -2 ). We denote by $U_{n-4}$ the proper transform of the special fiber $f_{0}$. This is also a self-intersection (-2) curve. Let $\pi: Z_{n} \rightarrow \Sigma(n)$ denote the above iterated blow-up of $\Sigma(n)$ at $(n-3)$ points. Then we have the following computations for the canonical divisors:
$$\begin{aligned}
K_{\Sigma(n)} & =-2 C_{0}-(n+2) f \\
K_{Z_{n}} & =\pi^{*}\left(K_{\Sigma(n)}\right)+E_{1}+U_{n-5}+2 U_{n-6}+\cdots+(n-5) U_{1}+(n-4) E_{2} .
\end{aligned}$$
Moreover, we have:
$$\begin{aligned}
f & =U_{n-4}+\cdots+U_{1}+E_{1}+E_{2} \\
\Delta & =4\left(U_{n-4}+n f\right)-2\left[E_{1}+(n-4) E_{2}+(n-5) U_{1}+\cdots+2 U_{n-6}+U_{n-5}\right],
\end{aligned}$$
where $f$ is the class of the proper transform of the generic fiber of $\Sigma(n)$ in $Z_{n}$. The double cover of $Z_{n}$ branched along $\Delta$ is the elliptic surface $E(n)$. Let $d: Z_{n} \rightarrow E(n)$ denote the branch cover, and $F$ the class of the proper transform of a generic fiber. The canonical divisor of $E(n)$ is
$$\begin{aligned}
K_{E(n)} & =d^{*}\left(K_{Z_{n}}+\frac{1}{2} \Delta\right) \\
& =d^{*}((n-2) f)=(n-2) F
\end{aligned}$$

As the branch locus is disjoint from the chain of curves $C_{0}, U_{n-4}, \cdots, U_{1}$, its preimage consists of two chains of curves which we denote by $C_{0}^{\prime}, U_{n-4}^{\prime}, \cdots, U_{1}^{\prime}$, and $C_{0}^{\prime \prime}, U_{n-4}^{\prime \prime}, \cdots, U_{1}^{\prime \prime}$. By Artin's criterion we can collapse the chain $C_{0}^{\prime}, U_{n-4}^{\prime}, \cdots, U_{1}^{\prime}$, and the chain $U_{n-4}^{\prime \prime}, \cdots, U_{1}^{\prime \prime}$ to obtain an orbifold surface with two singular points, which we denote by $\widehat{X}_{n}$. Then the Hirzebruch-Jung continued fraction tells us that the singularities are of type: $\frac{1}{(n-2)^{2}}(1, n-3)$ and $\frac{1}{n-3}(1, n-4)$,
respectively. Let $\widehat{\pi}: E(n) \rightarrow \widehat{X}_{n}$ be the projection map. The projection formula implies that:
$$K_{\widehat{X}_{n}}=(n-2) \widehat{F},$$
where we denote by $\widehat{F}=\widehat{\pi}(F)$. We can compute the self-intersection of $\widehat{F}$, by first computing
$$\begin{aligned}
\widehat{\pi}^{*}(\widehat{F}) & =F+a_{0} C_{0}^{\prime}+a_{1} U_{1}^{\prime}+\cdots+a_{n-4} U_{n-4}^{\prime}+b_{1} U_{1}^{\prime \prime}+\cdots+a_{n-4} U_{n-4}^{\prime \prime} \\
& =F+\frac{1}{(n-2)^{2}}\left[(n-3) C_{0}^{\prime}+(n-4) U_{1}^{\prime}+\cdots+1 \cdot U_{n-4}^{\prime}\right]
\end{aligned}$$
where the above coefficients are obtained by taking the intersection with the curves in the exceptional locus. Hence:
$$(\widehat{F})^{2}=\left(\widehat{\pi}^{*}(\widehat{F})\right)^{2}=\left(\widehat{\pi}^{*}(\widehat{F})\right) \cdot F=\frac{1}{(n-2)^{2}}(n-3)$$
and
$$K_{\widehat{X}_{n}}^{2}=(n-2)^{2} \widehat{F}^{2}=n-3$$

We use next the Nakai-Moishezon criterion to show that $K_{\widehat{X}_{n}}$ is ample. As $\widehat{F}$ is the proper transform of a generic fiber on $\Sigma(n)$, it will intersect any curve which does not lie on the total transform of the special fiber $f_{0}$ in a strictly positive number of points. So all we need to show is that the intersection of $\widehat{F}$ with the irreducible components in the class of the total transform of $f_{0}$ is strictly positive. These components are $\widehat{\pi}\left(C_{0}^{\prime \prime}\right), \widehat{\pi}\left(d^{-1}\left(E_{1}\right)\right), \widehat{\pi}\left(d^{-1}\left(E_{2}\right)\right)$, which, for simplicity, we denote by $\widehat{C}_{0}, \widehat{E}_{1}, \widehat{E}_{2}$. We have:
$$\begin{aligned}
\widehat{F} \cdot \widehat{C}_{0} & =\widehat{\pi}^{*}(\widehat{F}) \cdot \widehat{\pi}^{*}\left(\widehat{C}_{0}\right)=\widehat{\pi}^{*}(\widehat{F}) \cdot C_{0}^{\prime \prime}=F \cdot C_{0}^{\prime \prime}=1>0 \\
\widehat{F} \cdot \widehat{E}_{1} & =\widehat{\pi}^{*}(\widehat{F}) \cdot \widehat{\pi}^{*}\left(\widehat{E}_{1}\right)=\widehat{\pi}^{*}(\widehat{F}) \cdot E_{1}^{\prime \prime}=\frac{1}{(n-2)^{2}} U_{n-4}^{\prime} \cdot E_{1}^{\prime}=\frac{1}{(n-2)^{2}}>0 \\
\widehat{F} \cdot \widehat{E}_{2} & =\widehat{\pi}^{*}(\widehat{F}) \cdot \widehat{\pi}^{*}\left(\widehat{E}_{2}\right)=\widehat{\pi}^{*}(\widehat{F}) \cdot E_{2}^{\prime \prime}=\left(\frac{1}{(n-2)^{2}}(n-4) U_{1}^{\prime}\right) \cdot E_{2}^{\prime \prime} \\
& =\frac{1}{(n-2)^{2}}(n-4)>0
\end{aligned}$$
Hence, the canonical sheaf $K_{\widehat{X}_{n}}=(n-2) \widehat{F}$ is ample. \(\square\)

Proposition 4.2. The manifold $Y_{n}$ obtained by taking the rational blowdown of one chain of type $(-n,-2, \ldots,-2)$ in the elliptic surface $E(n)$ is a simply connected, minimal symplectic, non-Kähler manifold which lies on the half-Noether line.

Proof. Propositions 4.1 and 2.4 imply that $Y_{n}$ is a minimal symplectic surface of general type. Then by Proposition 2.1 its topological invariants are $c_{1}^{2}\left(Y_{N}\right)=n-3$ and $c_{2}\left(Y_{N}\right)=11 n+3$, and hence $\chi_{h}\left(Y_{n}\right)=n$. Then $Y_{n}$ lies on the half-Noether line $c_{1}^{2}\left(Y_{n}\right)=\chi_{h}\left(Y_{n}\right)-3$, and hence it is non-Kähler.

The fundamental group of the boundary $\pi_{1}\left(L\left(n^{2}, n m-1\right)\right)=\mathbb{Z} / n^{2} \mathbb{Z}$ surjects into the fundamental group of the rational homology ball $\pi_{1}\left(B_{n, m}\right)=\mathbb{Z} / n \mathbb{Z}$. We can then find a loop, which
represents a generator of the fundamental group of $B_{n, m}$, which is embedded in the proper transform of the exceptional divisor $E_{1}$, as the curve is transversal to the collapsed chain. Hence, the loop is homotopically equivalent to a constant loop in the complement of the configuration of spheres which is rational blowdown in $E(n)$. As $E(n)$ is simply connected then so must be $Y_{n}$. \(\square\)

Remark 4.3. An interesting fact is that if one takes the rational blowdown of both chains of type $(-n,-2, \ldots,-2)$ in $E(n)$, then the new manifold lies on the Noether line and admits a Kähler structure [20].

Theorem B follows immediately from Theorem A and Proposition 4.2.
Acknowledgements. The author would like to thank Claude LeBrun for interesting discussions on the subject. While writing this paper, the author was partially supported by the NSF grant DMS-1007114. The author gratefully acknowledges support from the Simons Center for Geometry and Physics, Stony Brook University and Institut des Hautes Études Scientifiques at which some of the research for this paper was performed.

\section*{References}
\begin{itemize}
\item[] [1] M.T. Anderson, Ricci curvature bounds and Einstein metrics on compact manifolds. J. Amer. Math. Soc. 2 (1989), no. 3, 455-490.
\item[] [2] K. Akutagawa, Computations of the orbifold Yamabe invariant. Math. Z. 271 (2012), no. 3-4, 611-625.
\item[] [3] K. Akutagawa, B. Botvinnik, The Yamabe invariants of orbifolds and cylindrical manifolds, and $L^{2}$-harmonic spinors. J. Reine Angew. Math. 574 (2004), 121-146.
\item[] [4] W. Barth, C. Peters, A. Van de Ven, Compact complex surfaces. Springer-Verlag, Berlin, 1984.
\item[] [5] G. Besson, G. Courtois, and S. Gallot, Les Variétés Hyperboliques Sont des Minima Locaux de l'Entropie Topologique, Inv. Math. 117 (1994) 403-445.
\item[] [6] X. Chen, C. Lebrun, B. Weber, Brian On conformally Kähler, Einstein manifolds. J. Amer. Math. Soc. 21 (2008), no. 4, 1137-1168.
\item[] [7] T. Eguchi, A. Hanson, Asymptotically flat solution to Euclidean gravity, Phys. Lett. 74 B (1978), 249-251.
\item[] [8] R. Fintushel, R. Stern, Rational blowdowns of smooth 4-manifolds. J. Differential Geom. 46 (1997), no. 2, 181-235.
\item[] [9] R. E. Gompf, A new construction of symplectic manifolds. Ann. of Math. (2) 142 (1995), no. 3, 527-595.
\item[] [10] R. E. Gompf, A. Stipsicz, 4-manifolds and Kirby calculus Graduate Studies in Mathematics, 20. American Mathematical Society, Providence, RI, 1999.
\item[] [11] G. Gibbons, S. Hawking, Gravitational multi-instantons, Phys. Lett. B 78 (1978), 430-432.
\item[] [12] O. Kobayashi, Scalar Curvature of a Metric of Unit Volume, Math. Ann. 279 (1987), 253-265.
\item[] [13] R. Kobayashi, Einstein-Kähler V-metrics on open Satake V-surfaces with isolated quotient singularities. Math. Ann. 272 (1985), no. 3, 385-398.
\item[] [14] J. Kollár, N. I. Shepherd-Barron, Threefolds and deformations of surface singularities, Invent. Math. 91 (1988), no. 2, 299-338.
\item[] [15] P. B. Kronheimer, The construction of ALE spaces as hyperkähler quotients, J. Differential Geom. 29 (1989), no. 3, 665-683.
\item[] [16] C. LeBrun, Four-manifolds without Einstein metrics. Math. Res. Lett. 3 (1996), no. 2, 133-147.
\item[] [17] C. LeBrun, Yamabe constants and the perturbed Seiberg-Witten equations. Comm. Anal. Geom. 5 (1997), no. 3, 535-553.
\item[] [18] C. LeBrun, Kodaira dimension and the Yamabe problem. Comm. Anal. Geom. 7 (1999), no. 1, 133-156.
\item[] [19] Y. Lee and J. Park. A simply connected surface of general type with $p_{g}=0$ and $K^{2}=2$. Invent. Math. 170 no. 3 (2007), 483-505.
\end{itemize}
[20] Y. Lee and J. Park. A construction of Horikawa surface via Q-Gorenstein smoothings. Math. Z. 267 (2011), no. 1-2, 15-25.
[21] T-J. Li, Symplectic 4-manifolds with Kodaira dimension zero. J. Differential Geom. 74 (2006), no. 2, 321-352.
[22] J. Park, Seiberg-Witten invariants of generalised rational blow-downs. Bull. Austral. Math. Soc. 56 (1997), no. 3, 363-384.
[23] J. Petean, The Yamabe invariant of simply connected manifolds. J. Reine Angew. Math. 523 (2000), 225-231.
[24] M. Manetti, On the moduli space of diffeomorphic algebraic surfaces. Invent. Math. 143 (2001), no. 1, 29-76
[25] R. Răsdeaconu, I. Şuvaina, Smooth structures and Einstein metrics on $\mathbb{C P}^{2} \# 5,6,7 \overline{\mathbb{C P}^{2}}$. Math. Proc. Cambridge Philos. Soc. 147 (2009), no. 2, 409-417.
[26] R. Schoen, Variational Theory for the Total Scalar Curvature Functional for Riemannian Metrics and Related Topics, Lec. Notes Math. 1365 (1987), 120-154.
[27] P. Suárez-Serrato, R. Torres A note on collapse, entropy, and vanishing of the Yamabe invariant of symplectic 4-manifolds preprint arXiv:1408.1586
[28] I. Şuvaina, ALE Ricci-flat Kähler metrics and deformations of quotient surface singularities. Ann. Global Anal. Geom. 41 (2012), no. 1, 109-123.
[29] M. Symington, Symplectic rational blowdowns. J. Differential Geom. 50 (1998), no. 3, 505-518.
[30] M. Symington, Generalized symplectic rational blowdowns. Algebr. Geom. Topol. 1 (2001), 503-518.
[31] G. Tian, J. Viaclovsky, Jeff Moduli spaces of critical Riemannian metrics in dimension four. Adv. Math. 196 (2005), no. 2, 346-372.
[32] J.A. Viaclovsky, Monopole metrics and the orbifold Yamabe problem. Ann. Inst. Fourier (Grenoble) 60 (2010), no. 7, 2503-2543 (2011)

Department of Mathematics, 1326 Stevenson Center, Vanderbilt University, Nashville, TN, 37240
E-mail address: ioana.suvaina@vanderbilt.edu
