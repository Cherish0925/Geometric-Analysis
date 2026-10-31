# ENTROPIES, VOLUMES, AND EINSTEIN METRICS

- Category: papers
- Identity: doi:10.1007/978-3-642-22842-1_2
- Content status: fulltext_ok

---

---
source_file: PDF__arXiv_math_0410215v2__math_DG__28_Jan_2013_b86d723cad0a.pdf
converter: mathpix
format: mmd
---

\title{
ENTROPIES, VOLUMES, AND EINSTEIN METRICS
}

\author{
D. KOTSCHICK
}

\begin{abstract}
We survey the definitions and some important properties of several asymptotic invariants of smooth manifolds, and discuss some open questions related to them. We prove that the (non-)vanishing of the minimal volume is a differentiable property, which is not invariant under homeomorphisms. We also formulate an obstruction to the existence of Einstein metrics on four-manifolds involving the volume entropy. This generalizes both the Gromov-Hitchin-Thorpe inequality proved in [23], and Sambusetti's obstruction [36].
\end{abstract}

\section*{1. Introduction}

In his seminal paper on bounded cohomology [16], Gromov introduced both the simplicial volume and the minimal volume of manifolds. While the definition of the simplicial volume belongs to quantitative algebraic topology, that of the minimal volume belongs to asymptotic Riemannian geometry, in that one takes an infimum of a certain quantity over the space of all Riemannian metrics on a fixed manifold. The simplicial volume provides a lower bound for the minimal volume, via the relations of these quantities to another asymptotic invariant, the minimal volume entropy of a manifold. This invariant is an asymptotic one in two ways: first one considers the asymptotics at infinity of a quantity on a non-compact manifold, and then one takes an infimum over all metrics, in the same way as for the definition of the minimal volume.

In Section 2 of this paper we survey several asymptotic invariants, including the three mentioned above. The invariants we discuss are related to each other by an interesting chain of inequalities that we explain, with the simplicial volume at the bottom, and the minimal volume at the top. We shall also discuss the nature of these invariants. Several of the asymptotic Riemannian invariants actually turn out to be rather crude topological invariants, by the recent work of Brunnbauer [11], who completed and generalized earlier work of Babenko [1, 2, 3]. This is not so for the minimal volume, since Bessières [7] has given examples of high-dimensional manifolds that are homeomorphic but have different minimal volumes, both of them positive. In Section 5 of this paper we exhibit another way in which the minimal volume fails to be invariant under homeomorphisms: there are pairs of homeomorphic four-manifolds for which the minimal volume is zero for one, and is positive for the other. As the vanishing of the minimal volume implies the vanishing of all real characteristic numbers, such examples cannot be simply connected. In fact, our examples are parallelizable and exhibit for the first time the existence of exotic smooth structures on parallelizable closed fourmanifolds.

In Section 3 of this paper we discuss two further asymptotic invariants that can be used to bound the volume entropy, and, therefore, the minimal volume, from below. These invariants, based on spectral and isoperimetric quantities, are more complicated than the invariants defined in

\footnotetext{
This work is part of the project Asymptotic invariants of manifolds, supported by the Schwerpunktprogramm Globale Differentialgeometrie of the Deutsche Forschungsgemeinschaft.
Published in: C. Bär et al. (eds.), Global Differential Geometry, pp. 39-54, Springer Proceedings in Mathematics 17, Springer Verlag 2012, DOI 10.1007/978-3-642-22842-1_2.
}

Section 2, and it is as yet unclear whether Brunnbauer's results [11] about topological invariance can be adapted for them.

In Section 4 we give an application of the discussion of asymptotic invariants to (non-)existence of Einstein metrics on four-manifolds. We prove that a closed oriented four-manifold $X$ admitting an Einstein metric must satisfy the inequality
$$\chi(X) \geq \frac{3}{2}|\sigma(X)|+\frac{1}{108 \pi^{2}} \lambda(X)^{4},$$
where $\chi(X)$ denotes the Euler characteristic, $\sigma(X)$ the signature, and $\lambda(X)$ the volume entropy. Using a recent rigidity result for the entropy due to Ledrappier and Wang [27] we characterize the case of equality.

Whenever one has a positive lower bound for the volume entropy, the above inequality implies a particular improvement of the classical Hitchin-Thorpe inequality [19]
$$\chi(X) \geq \frac{3}{2}|\sigma(X)| .$$
Two specific cases of lower bounds for the entropy which we discuss in Section 4 are the following. First, from Section 2, the spherical volume and the simplicial volume give lower bounds for the entropy. In the case of the simplicial volume this leads to
$$\chi(X) \geq \frac{3}{2}|\sigma(X)|+\frac{1}{162 \pi^{2}}\|X\|,$$
which improves on our result in [23]. Second, using the lower bound for the entropy arising from the existence of maps to locally symmetric spaces of rank one proved by Besson-Courtois-Gallot [9], we deduce the results of Sambusetti [36]. Thus, our obstruction to the existence of Einstein metrics subsumes all the known obstructions which are homotopy invariant. See [22, 24] for obstructions which are not homotopy invariant.

\section*{2. Entropies and volumes}

Let $M$ be a connected closed oriented manifold of dimension $n$. In this section we discuss the following chain of inequalities between its topological invariants:
$$\frac{n^{n / 2}}{n!}\|M\| \leq 2^{n} n^{n / 2} T(M) \leq \lambda(M)^{n} \leq h(M)^{n} \leq(n-1)^{n} \operatorname{MinVol}(M) .$$
This chain appears in [34], without $T(M)$, and with an unspecified constant in front of $\|M\|$. The inequalities involving $T(M)$ are from [8], where $T(M)$ was defined.

We now explain the terms in (1), and the sources for the different inequalities.
2.1. Simplicial volume. The simplicial volume was introduced by Gromov [16]. Let $c=\Sigma_{i} r_{i} \sigma_{i}$ be a chain with real coefficients $r_{i}$, where $\sigma_{i}: \Delta^{k} \rightarrow X$ are singular $k$-simplices in $M$. One defines the norm of $c$ to be
$$\|c\|=\Sigma_{i}\left|r_{i}\right| .$$
If $\alpha \in H_{k}(M, \mathbb{R})$, set
$$\|\alpha\|=\inf \{\|c\| \mid c \text { a cycle representing } \alpha\},$$
where the infimum is taken over all cycles representing $\alpha$. This is a seminorm on the homology.
The simplicial volume is defined to be the norm of the fundamental class, and is denoted
$$\|M\|=\|[M]\| .$$

Gromov [16] has shown that the simplicial volume of $M$ is determined by the image of its fundamental class under the classifying map $f: M \rightarrow B \pi_{1}(M)$ of the universal covering.

This motivates the following definition.
Definition 1. An invariant $I$ of closed oriented manifolds $M$ is said to be homologically invariant if it depends only on $f_{*}[M] \in H_{*}\left(B \pi_{1}(M)\right)$.

Homological invariance implies that $I$ is homotopy-invariant, and that it is a bordism invariant of $[M, f] \in \Omega_{n}\left(B \pi_{1}(M)\right)$.
2.2. Spherical volume. The spherical volume was introduced by Besson-Courtois-Gallot [8].

Let $\tilde{M}$ be the universal covering of $M$. Fix a positive $\pi_{1}(M)$-invariant measure $\tilde{\mu}$ on $\tilde{M}$ that is absolutely continuous with respect to Lebesgue measure. Denote by $\left(S^{\infty}, c a n\right)$ the unit sphere in the Hilbert space $L^{2}(\tilde{M}, \tilde{\mu})$ endowed with the metric induced by the scalar product. For every $\pi_{1}(M)$-equivariant immersion $\Phi: \tilde{M} \rightarrow S^{\infty}$ we have an induced metric $\Phi^{*}(c a n)$ which descends to $M$, and we write $\operatorname{vol}(\Phi)$ for $\operatorname{Vol}\left(M, \Phi^{*}(\operatorname{can})\right)$.

The spherical volume of $M$ is defined to be
$$T(M)=\inf \left\{\operatorname{vol}(\Phi) \mid \Phi \text { a } \pi_{1}(M)-\text { equivariant immersion } \tilde{M} \rightarrow S^{\infty}\right\} .$$
This does not depend on the choice of measure $\tilde{\mu}$, see [8].
Brunnbauer [11] has proved that the spherical volume is homologically invariant in the sense of Definition 1. In particular it is homotopy-invariant.

Besson, Courtois and Gallot proved the first inequality in (1) as Theorem 3.16 in [8].
2.3. Volume entropy. For a Riemannian metric $g$ on $M$ consider the lift $\tilde{g}$ to the universal covering $\tilde{M}$. For an arbitrary basepoint $p \in \tilde{M}$ consider the limit
$$\lambda(M, g)=\lim _{R \rightarrow \infty} \frac{\log \operatorname{Vol}(B(p, R))}{R},$$
where $B(p, R)$ is the ball of radius $R$ around $p$ in $\tilde{M}$ with respect to $\tilde{g}$, and the volume is taken with respect to $\tilde{g}$ as well. After earlier work by Efremovich, Shvarts, Milnor [30] and others, Manning [28] showed that the limit exists and is independent of $p$. It follows from [30] that $\lambda(M, g)>0$ if and only if $\pi_{1}(M)$ has exponential growth.

We call $\lambda(M, g)$ the volume entropy of the metric $g$, and define the volume entropy of $M$ to be
$$\lambda(M)=\inf \{\lambda(M, g) \mid g \in \operatorname{Met}(M) \text { with } \operatorname{Vol}(M, g)=1\} .$$
This sometimes vanishes even when $\lambda(M, g)>0$ for every $g$. The normalization of the total volume is necessary because of the scaling properties of $\lambda(M, g)$.

Any metric on $M$ can be scaled so that Ric $_{g} \geq-\frac{1}{n-1} g$. By the Bishop volume comparison theorem, cf. [10], this implies $\lambda(M, g) \leq 1$. Setting
$$\hat{g}=\frac{1}{\operatorname{Vol}(M, g)^{2 / n}} g$$
we have $\operatorname{Vol}(M, \hat{g})=1$ and $\lambda(M, \hat{g})=\operatorname{Vol}(M, g)^{1 / n} \lambda(M, g) \leq \operatorname{Vol}(M, g)^{1 / n}$, implying
$$\lambda(M)=\inf \{\lambda(M, \hat{g})\} \leq \inf \left\{\operatorname{Vol}(M, g)^{1 / n} \mid g \in \operatorname{Met}(M) \text { s.t. } \operatorname{Ric}_{g} \geq-\frac{1}{n-1} g\right\} .$$
This is not an equality because the Bishop estimate is not sharp, except for metrics of constant sectional curvature.

Babenko has shown that the volume entropy $\lambda(M)$ is homotopy invariant [1], and is also an invariant of the bordism class $[M, f] \in \Omega_{n}\left(B \pi_{1}(M)\right)$, cf. [3]. These results were sharpened by Brunnbauer [11], who proved the homological invariance of $\lambda(M)$. Although these results show that $\lambda(M)$ is a rather crude invariant which is understandable in many situations, there are still many open questions about this invariant. For example, its behavior under taking finite coverings is not understood. We do not even know whether the vanishing of $\lambda$ on a finite covering of $M$ implies the vanishing on $M$ itself. This question came up in [20].

The second inequality in (1) follows from Theorem 3.8 of Besson-Courtois-Gallot [8].
2.4. Topological entropy. For a Riemannian metric $g$ on $M$ consider the topological entropy $h(M, g)$ of its geodesic flow as a dynamical system on the unit sphere bundle, cf. [28]. The topological entropy of $M$ is defined to be
$$h(M)=\inf \{h(M, g) \mid g \in \operatorname{Met}(M) \text { with } \operatorname{Vol}(M, g)=1\} .$$
Here again the normalization of the total volume is necessary because of scaling properties.
It seems to be unkown what exactly the minimal topological entropy depends on, e.g. the homotopy type, the homeomorphism type, or the diffeomorphism type. It is not clear whether this is a subtle invariant, or a crude one like the minimal volume entropy and the spherical volume.

Manning [28] proved $\lambda(M, g) \leq h(M, g)$ for all closed $M$. Taking the infimum over all metrics with normalized volume yields the third inequality in (1).
2.5. Minimal volume. The minimal volume was introduced by Gromov [16]. It is defined by
$$\operatorname{MinVol}(M)=\inf \left\{\operatorname{Vol}(M, g) \mid g \in \operatorname{Met}(M) \text { with }\left|K_{g}\right| \leq 1\right\},$$
where $K_{g}$ denotes the sectional curvature of $g$.
It is known that the minimal volume is a very sensitive invariant of $M$, which depends on the smooth structure in an essential way. Bessières [7] has given examples of pairs of high-dimensional manifolds which are homeomorphic, but have different positive minimal volumes. In Section 5 we shall use Seiberg-Witten theory to show that the vanishing of the minimal volume is not invariant under homeomorphisms. This represents a more dramatic failure of topological invariance than Bessières' result, since it shows that there are homeomorphic manifolds such that one collapses with bounded sectional curvature, and the other one does not.

Manning [29] proved that for a closed Riemannian manifold with sectional curvature bounded by $\left|K_{g}\right| \leq k$ the topological entropy is bounded by
$$h(M, g) \leq(n-1) \sqrt{k} .$$
By rescaling, this implies the last of the inequalities in (1), cf. [32] p. 129.

\section*{3. Isoperimetric constants and minimal eigenvalues}

One of Gromov's original motivations for introducing the simplicial volume was to obtain lower bounds for the minimal volume. However, the lower bounds given by the simplicial volume via (1) are usually rather weak. In particular, there seems to be no known example of a manifold with $T(M)>0$ for which the inequality
$$\frac{n^{n / 2}}{n!}\|M\| \leq 2^{n} n^{n / 2} T(M)$$
is sharp. All the other inequalities in (1) are sharp for surfaces of genus $g \geq 2$, where
$$4(g-1)=\left\|\Sigma_{g}\right\|<8 T\left(\Sigma_{g}\right)=\lambda\left(\Sigma_{g}\right)^{2}=h\left(\Sigma_{g}\right)^{2}=\operatorname{MinVol}\left(\Sigma_{g}\right)=4 \pi(g-1) .$$
One approach to understanding and quantifying the failure of (3) to be sharp is to consider intermediate invariants which may interpolate between the simplicial and the spherical volumes. In fact, a candidate for such an intermediate invariant, based on the minimal eigenvalue of the Laplacian on the universal covering, occurs in the work of Besson-Courtois-Gallot [8]. We now elaborate on this to discuss the following alternative to (1):
$$I(M)^{n} \leq 2^{n} \Lambda_{0}(M)^{n / 2} \leq 2^{n} n^{n / 2} T(M) \leq \lambda(M)^{n} \leq h(M)^{n},$$
where we can also continue on the right with the same minimal volume term as in (1). Only the first two terms and the first two inequalities on the left need any explanation, as the rest has been explained already in the previous section.
3.1. Minimal eigenvalue. Given a closed Riemannian manifold ( $M, g$ ), we consider the Riemannian universal cover $(\tilde{M}, \tilde{g})$, and define
$$\lambda_{0}(\tilde{M}, \tilde{g})=\inf _{f \in C_{0}^{\infty}} \frac{\int_{\tilde{M}} f \cdot \Delta f d v o l_{\tilde{g}}}{\int_{\tilde{M}} f^{2} d v o l_{\tilde{g}}},$$
where $C_{0}^{\infty}$ denotes the smooth compactly supported functions on $\tilde{M}$. Extending the Laplacian to $L^{2}$-functions, $\lambda_{0}(\tilde{M}, \tilde{g})$ is the greatest lower bound for its spectrum. It is tempting now to define the minimal eigenvalue of $M$ as
$$\inf \left\{\lambda_{0}(\tilde{M}, \tilde{g}) \mid g \in \operatorname{Met}(M) \text { with } \operatorname{Vol}(M, g)=1\right\},$$
which would be the naive generalization of the definition of the minimal volume entropy. However, this definition always gives zero, cf. [37]. The correct definition of an invariant of $M$ derived from the minimal eigenvalue is the following. First, we define an invariant of a conformal class $[g]$ by setting
$$\Lambda_{0}(M,[g])=\sup \left\{\lambda_{0}\left(\tilde{M}, \tilde{g}^{\prime}\right) \mid g^{\prime} \in[g] \text { with } \operatorname{Vol}\left(M, g^{\prime}\right)=1\right\},$$
and then define
$$\Lambda_{0}(M)=\inf \left\{\Lambda_{0}(M,[g]) \mid[g] \in \operatorname{Conf}(M)\right\}$$
as an infimum over conformal classes.
This is a meaningful invariant, which for surfaces of genus $g \geq 2$ can be shown to equal $\pi(g-$ 1), cf. [37]. The work of Besson-Courtois-Gallot [8] implies the second inequality in (4) in all dimensions $n$. It is sharp for surfaces.
3.2. Isoperimetric constant. Cheeger's isoperimetric constant of $(M, g)$ is defined to be
$$i(\tilde{M}, \tilde{g})=\inf _{N} \frac{\operatorname{Vol}_{n-1}(\partial N)}{\operatorname{Vol}_{n}(N)},$$
where $N \subset \tilde{M}$ ranges over all compact connected subsets with smooth boundary, say. Again one would naively define the isoperimetric constant of $M$ to be
$$\inf \{i(\tilde{M}, \tilde{g}) \mid g \in \operatorname{Met}(M) \text { with } \operatorname{Vol}(M, g)=1\},$$
but this always gives zero, cf. [37]. The definition has to be modified in the same way as for the minimal eigenvalue. First we define an invariant of a conformal class $[g]$ by setting
$$I(M,[g])=\sup \left\{i\left(\tilde{M}, \tilde{g}^{\prime}\right) \mid g^{\prime} \in[g] \text { with } \operatorname{Vol}\left(M, g^{\prime}\right)=1\right\},$$
and then we take the infimum over conformal classes:
$$I(M)=\inf \{I(M,[g]) \mid[g] \in \operatorname{Conf}(M)\} .$$

Cheeger's inequality $i(\tilde{M}, \tilde{g})^{2} \leq 4 \lambda_{0}(M)$, see [13], implies the first inequality in (4).
For both the minimal eigenvalue $\Lambda_{0}(M)$ and for the isoperimetric constant $I(M)$ it is not immediately clear what they depend on. One could try to use Brunnbauer's axiomatic approach [11] to prove that these are homological invariants of manifolds. However, because of the complicated definitions, using a supremum within each conformal class before taking the infimum over conformal classes, it is hard to verify the required axioms for these invariants. Because of this difficulty we do not yet know how subtle these invariants are.

The chain (4) shows that one can use the minimal eigenvalue and the isoperimetric constant instead of the simplicial volume to obtain lower bounds for the minimal volume entropy and the minimal volume.

A very important outstanding problem is to decide whether there is an upper bound for the simplicial volume in terms of the isoperimetric constant. More precisely, one would like to know whether the inequality
$$\frac{n^{n / 2}}{n!}\|M\| \leq I(M)^{n}$$
holds. If this were the case, then we could insert (4) into (1), and we could hope to measure the gap between the simplicial volume and the spherical volume. Potentially this could lead to an improvement of (1), by improving the constant in front of the simplicial volume to close the gap between the simplicial and spherical volumes in (1).

\section*{4. Einstein metrics on four-manifolds}

We now prove the following constraint on the topology of four-manifolds admitting Einstein metrics.

Theorem 1. Let $X$ be a closed oriented Einstein 4-manifold. Then
$$\chi(X) \geq \frac{3}{2}|\sigma(X)|+\frac{1}{108 \pi^{2}} \lambda(X)^{4},$$
where $\chi(X)$ denotes the Euler characteristic, $\sigma(X)$ the signature, and $\lambda(X)$ the volume entropy.
Equality in (5) occurs if and only if every Einstein metric on $X$ is flat, is non-flat locally Calabi-Yau, or is of constant negative sectional curvature.

Remark 1. Note that the right-hand side of (5) is an invariant of the cobordism class $[X, f] \in$ $\Omega_{4}\left(B \pi_{1}(X)\right)$, where $f: X \rightarrow B \pi_{1}(X)$ is the classifying map of the universal covering. For the signature this is due to Thom, and for the volume entropy it was proved by Babenkd ${ }^{1}$ in [3]. Rationally, one has the well-known isomorphism
$$\Omega_{4}\left(B \pi_{1}(X)\right) \otimes \mathbb{Q}=H_{4}\left(B \pi_{1}(X) ; \Omega_{0}(\star) \otimes \mathbb{Q}\right) \oplus H_{0}\left(B \pi_{1}(X) ; \Omega_{4}(\star) \otimes \mathbb{Q}\right) .$$
The second summand is responsible for the signature term (=first Pontryagin number) and the first one for the entropy term in (5). Indeed, Brunnbauer's homological invariance result for the entropy [11] shows that $\lambda(X)$ depends only on $f_{*}[X] \in H_{4}\left(B \pi_{1}(X)\right)$.

\footnotetext{
${ }^{1}$ His paper assumes that manifolds are of dimension $\geq 5$, but that is not important here; cf. [11].
}

Proof of Theorem 1. By the Gauss-Bonnet theorem the Euler characteristic of a closed oriented Riemannian 4-manifold ( $X, g$ ) is
$$\chi(X)=\frac{1}{8 \pi^{2}} \int_{X} \frac{1}{24} s_{g}^{2}+|W|^{2}-\mid \text { Ric }\left._{0}\right|^{2} d \text { vol }_{g}$$
where $s_{g}$ is the scalar curvature, $W$ is the Weyl tensor, and $R i c_{0}$ is the trace-less Ricci tensor of $g$. For an Einstein metric this reduces to
$$\chi(X)=\frac{1}{8 \pi^{2}} \int_{X} \frac{1}{24} s_{g}^{2}+|W|^{2} d \operatorname{vol}_{g}$$
Thus $\chi(X) \geq 0$, with equality if and only if every Einstein metric on $X$ is flat.
If the scalar curvature of an Einstein metric is positive, then $\pi_{1}(X)$ is finite by Myers's theorem and the volume entropy vanishes, so that (5) reduces to the Hitchin-Thorpe inequality obtained by comparing (6) with the Chern-Weil formula
$$\sigma(X)=\frac{1}{12 \pi^{2}} \int_{X}\left|W_{+}\right|^{2}-\left|W_{-}\right|^{2} d \operatorname{vol}_{g} .$$

If the scalar curvature is zero, then the Cheeger-Gromoll splitting theorem implies that either the fundamental group is finite, or the Euler characteristic vanishes. In the latter case the Einstein metric is flat and the volume growth is only polynomial, so that in both cases the volume entropy vanishes and we are done as before.

If the scalar curvature is negative, we scale the metric so that $R i c_{g}=-\frac{1}{3} g$.
Using the Chern-Weil formula (7) the second term in (6) is
$$\left.\frac{1}{8 \pi^{2}} \int_{X}|W|^{2} d \operatorname{vol}_{g} \geq\left.\frac{1}{8 \pi^{2}}\left|\int_{X}\right| W_{+}\right|^{2}-\left|W_{-}\right|^{2} d \operatorname{vol}_{g}\left|=\frac{3}{2}\right| \sigma(X) \right\rvert\, .$$

The first term in (6) is
$$\frac{1}{8 \pi^{2}} \frac{1}{24}\left(-\frac{4}{3}\right)^{2} \operatorname{Vol}(X, g)=\frac{1}{108 \pi^{2}} \operatorname{Vol}(X, g) .$$
Now using the Bishop estimate to bound the volume entropy $\lambda(X, g)$ from above by 1 (see (2)) we find
$$\frac{1}{8 \pi^{2}} \frac{1}{24}\left(-\frac{4}{3}\right)^{2} \operatorname{Vol}(X, g) \geq \frac{1}{108 \pi^{2}} \operatorname{Vol}(X, g) \lambda(X, g)^{4} \geq \frac{1}{108 \pi^{2}} \lambda(X)^{4} .$$
This completes the proof of (5). Equality cannot hold in the case of positive scalar curvature because in this case we threw away the scalar curvature term in (6). In the case of zero scalar curvature the entropy vanishes and the discussion of equality reduces to the corresponding discussion for the Hitchin-Thorpe inequality, see Hitchin [19]. The conclusion is that every Einstein metric is flat or (up to choosing the orientation suitably) locally Calabi-Yau but non-flat. For negative scalar curvature equality in (5) implies equality in (9), so that $\lambda(X)>0$ and every Einstein metric on $X$ has to be entropy-minimizing. Moreover, the Einstein metric must have entropy $\lambda(X, g)=1$, and so by the recent rigidity theorem of Ledrappier and Wang [27] it has constant negative sectional curvature ${ }^{2}$. Thus these are the only candidates for equality. They do indeed give equality because

\footnotetext{
${ }^{2}$ Our scaling normalization for the lower Ricci curvature bound is different from the one used in [27], so entropy $=1$ in our case corresponds to entropy $=n-1$ in [27].
}
they are conformally flat and therefore (8) is an equality for them, and they are entropy-minimizing by the celebrated result of Besson-Courtois-Gallot [9]. \(\square\)

Remark 2. The three cases giving rise to equality in (5) correspond to the vanishing of all three terms in (5) for flat manifolds, to the vanishing of $\lambda(X)$ only for Calabi-Yaus, and to the vanishing of $\sigma(X)$ only in the hyperbolic case. After earlier, unpublished, work of Calabi, Charlap-Sah, and Levine, the closed orientable flat four-manifolds were classified by Hillman [18] and by Wagner [38], who showed that there are 27 distinct ones. By Bieberbach's theorems, all these manifolds are finite quotients of $T^{4}$. In the locally Calabi-Yau case, Hitchin [19] showed that the only possible manifolds are the $K 3$ surface and its quotients by certain free actions of $\mathbb{Z}_{2}$ and of $\mathbb{Z}_{2} \times \mathbb{Z}_{2}$. In the hyperbolic case there are of course infinitely many manifolds.

Combining (4) with Theorem 1 we obtain:
Corollary 1. Let $X$ be a closed oriented Einstein 4-manifold. Then we have the following lower bounds for the Euler characteristic of $X$ :
$$\begin{aligned}
\chi(X) & \geq \frac{3}{2}|\sigma(X)|+\frac{64}{27 \pi^{2}} T(X), \\
\chi(X) & \geq \frac{3}{2}|\sigma(X)|+\frac{4}{27 \pi^{2}} \Lambda_{0}(X)^{2}, \\
\chi(X) & \geq \frac{3}{2}|\sigma(X)|+\frac{1}{108 \pi^{2}} I(X)^{4} .
\end{aligned}$$
In all cases, equality occurs if and only if every Einstein metric on $X$ is flat, is non-flat locally Calabi-Yau, or is of constant negative sectional curvature.

The point of the last statement is that equality in one of these estimates implies equality in (5).
Combining (1) with Theorem 1 we obtain the following improvement of the Gromov-Hitchin-Thorpe inequality proved in [23]:

Corollary 2. Let $X$ be a closed oriented Einstein 4-manifold. Then
$$\chi(X) \geq \frac{3}{2}|\sigma(X)|+\frac{1}{162 \pi^{2}}\|X\| .$$

Note that this is not sharp in any interesting cases with non-vanishing simplicial volume term, because the lower bound for the entropy in terms of the simplicial volume is not optimal.

Theorem 1 together with the work of Besson-Courtois-Gallot [9] implies the following:
Corollary 3 (Sambusetti [36]). Let $X$ be a closed oriented Einstein 4-manifold.
If $X$ admits a map of non-zero degree $d$ to a real hyperbolic manifold $Y$, then
$$\chi(X) \geq \frac{3}{2}|\sigma(X)|+|d| \cdot \chi(Y),$$
with equality only if $X$ is also real hyperbolic.
If $X$ admits a map of non-zero degree $d$ to a complex hyperbolic manifold $Y$, then
$$\chi(X)>\frac{3}{2}|\sigma(X)|+|d| \cdot \frac{32}{81} \chi(Y) .$$

Proof. To prove (14) we combine (5) with the inequality
$$\lambda(X)^{4} \geq d \cdot \lambda(Y)^{4}=d \cdot 3^{4} \operatorname{Vol}\left(Y, g_{0}\right)$$
from [9]. Here $g_{0}$ is the hyperbolic metric on $Y$ normalized so that $K=-1$. With this normalization the Gauss-Bonnet formula (6) gives $\operatorname{Vol}\left(Y, g_{0}\right)=\frac{4 \pi^{2}}{3} \chi(Y)$ so that $3^{4} \operatorname{Vol}\left(Y, g_{0}\right)=$ $108 \pi^{2} \chi(Y)$.

In the case of equality $X$ must itself be hyperbolic, by the equality case of Theorem 1.
For maps to complex hyperbolic manifolds one uses the corresponding statement from [9]. Again $\lambda(X)^{4} \geq d \cdot \lambda(Y)^{4}$ and the hyperbolic metric on $Y$ is entropy-minimizing. Thus one only has to check the proportionality factors between the fourth power of the entropy and the Euler characteristic, and the weak form of (15) follows. By Theorem 1 equality cannot occur in this case. \(\square\)

It would be interesting to know whether (5) remains true if we replace the volume entropy $\lambda$ by the topological entropy $h$, cf. (1). The results of Paternain and Petean [33, 34] are very suggestive in this regard. While the volume entropy can only be positive for manifolds with fundamental groups of exponential growth, the topological entropy may be positive even for simply connected manifolds. Unlike the volume entropy, the topological entropy is not known to be homotopy invariant. Notice that we can definitely not replace $\lambda^{4}$ by a positive multiple of MinVol, because the K3 surface satisfies $\chi(K 3)=\frac{3}{2}|\sigma(K 3)|$, and has positive MinVol as its Euler characteristic and signature are non-zero. We will show in the next section that the non-vanishing of the minimal volume depends in an essential way on the smooth structure. That the existence of an Einstein metric depends on the smooth structure was first shown in [22]. Recently Brunnbauer, Ishida and Suárez-Serrato [12] have constructed some interesting examples showing that the smooth obstructions to the existence of Einstein metrics are completely independent of those provided by Theorem 1.

To end this section, we briefly discuss the history of Theorem 1. The Hitchin-Thorpe inequality $\chi(X) \geq \frac{3}{2}|\sigma(X)|$ was, for a long time, the only known obstruction to the existence of Einstein metrics on four-manifolds. This changed when Gromov [16] gave a lower bound for the Euler number by a multiple of the simplicial volume. For many years after that, the Hitchin-Thorpe inequality and the "Gromov obstruction" were treated as separate, unrelated obstructions; see for example the discussion in [6, 9, 36]. In 1997, trying to understand Gromov's argument, I found that the signature term of the Hitchin-Thorpe inequality and the simplicial volume term of Gromov's inequality can actually be combined, to obtain an inequality like (13); see [23]. That inequality still has the flaw that it is not sharp in any interesting cases, because the simplicial volume term is too weak. Thinking about the chain (1), I found the sharp Theorem 1 in 2004, wrote it down in [25], and also explained that it subsumes all the known homotopy-invariant obstructions to Einstein metrics. That paper has remained unpublished, because various referees claimed that Theorem 1 was not interesting, or that it was the same as the result of [23], or that it was known to the authors of [9, 36]. What the referees did not notice, and I myself only noticed recently, is that the discussion of the limiting case in [25] was actually incomplete. The only way I know how to characterize the limiting case, is through the recent rigidity result of Ledrappier and Wang [27], as used in the proof of Theorem 1 given above. In particular there seems to be no way of obtaining the desired conclusion from [9, 36].

\section*{5. Minimal volumes and smooth structures}

In this section we show that vanishing of the minimal volume is a property of the smooth structure, which is not invariant under homeomorphisms. The proof below actually shows that one can change the smooth structure of a manifold with a smooth free circle action so that for the new smooth structure any smooth circle action must have fixed points.

Theorem 2. For every $k \geq 0$ the manifold $X_{k}=k\left(S^{2} \times S^{2}\right) \#(1+k)\left(S^{1} \times S^{3}\right)$ with its standard smooth structure has zero minimal volume.

If $k$ is odd and large enough, then there are infinitely many pairwise non-diffeomorphic smooth manifolds $Y_{k}$ homeomorphic to $X_{k}$, all of which have strictly positive minimal volume.

Proof. Note that $X_{0}=S^{1} \times S^{3}$ has obvious free circle actions, and therefore collapses with bounded sectional curvature. To see that all $X_{k}$ have vanishing minimal volume it suffices to construct fixed-point-free circle actions on them.

The product $S^{2} \times S^{2}$ has a diagonal effective circle action which on each factor is rotation around the north-south axis. It has four fixed pints, and the linearization of the action induces one orientation at two of the fixed points, and the other orientation at the remaining two. The induced action on the boundary of an $S^{1}$-invariant small ball around each of the fixed points is the Hopf action on $S^{3}$. By taking equivariant connected sums at fixed points, pairing fixed points at which the linearizations give opposite orientations, we obtain effective circle actions with $2+2 k$ fixed points on the connected sum $k\left(S^{2} \times S^{2}\right)$ for every $k \geq 1$. Now we have $1+k$ fixed points at which the linearization induces one orientation, and $1+k$ at which it induces the other orientation. Then making equivariant self-connected sums at pairs of fixed points with linearizations inducing opposite orientations we finally obtain a free circle action on $X_{k}=k\left(S^{2} \times S^{2}\right) \#(1+k)\left(S^{1} \times S^{3}\right)$.

If $k$ is odd and large enough, then there are symplectic manifolds $Z_{k}$ homeomorphic (but not diffeomorphic) to $k\left(S^{2} \times S^{2}\right)$, see for example [17]. By the construction given in [17], we may assume that $Z_{k}$ contains the Gompf nucleus of an elliptic surface. By performing logarithmic transformations inside this nucleus, we can vary the smooth structures on the $Z_{k}$ in such a way that the number of Seiberg-Witten basic classes with numerical Seiberg-Witten invariant $= \pm 1$ becomes arbitrarily large, cf. Theorem 8.7 of [14] and Example 3.5 of [24].

Consider $Y_{k}=Z_{k} \#(1+k)\left(S^{1} \times S^{3}\right)$. This is clearly homeomorphic to $X_{k}$. Although the numerical Seiberg-Witten invariants of $Y_{k}$ must vanish, cf. [26, 21], we claim that each of the basic classes with numerical Seiberg-Witten invariant $= \pm 1$ on $Z_{k}$ gives rise to a monopole class on $Y_{k}$, that is the characteristic class of a $\operatorname{Spin}^{c}$-structure for which the monopole equations have a solution for every Riemannian metric on $Y_{k}$. There are two ways to see this. One can extract our claim from the connected sum formula [4] for the stable cohomotopy refinement of Seiberg-Witten invariants introduced by Bauer and Furuta [5], cf. [15]. Alternatively, one uses the invariant defined by the homology class of the moduli space of solutions to the monopole equations, as in [21]. This means that the first homology of the manifold is used, and here this is enough to obtain a non-vanishing invariant. Using this invariant, our claim follows from Proposition 2.2 of Ozsváth-Szabó [31].

As $Y_{k}$ has non-torsion monopole classes $c$ with $c^{2}=2 \chi\left(Z_{k}\right)+3 \sigma\left(Z_{k}\right)=4+4 k>0$, the bound
$$c^{2} \leq \frac{1}{32 \pi^{2}} \int_{Y_{k}} s_{g}^{2} d \mathrm{vol}_{g}$$
where $s_{g}$ is the scalar curvature of any Riemannian metric $g$, shows that $Y_{k}$ cannot collapse with bounded scalar curvature, cf. [24]. A fortiori it cannot collapse with bounded sectional curvature, and so its minimal volume is strictly positive.

The monopole classes we constructed on $Y_{k}$ are all generic monopole classes in the sense of [24]. By Lemma 2.4 of loc. cit. each manifold has at most finitely many such classes. As we can change the smooth structure to make the number of generic monopole classes arbitrarily large, we have infinitely many distinct smooth structures we can choose for $Y_{k}$. \(\square\)

The above proof also gives the following:
Corollary 4. There are pairs of homeomorphic closed manifolds such that one collapses with bounded sectional curvature and the other one cannot collapse even with bounded scalar curvature.

Remark 3. That connected sums of manifolds with vanishing minimal volumes may have nonvanishing minimal volumes is immediate by looking at connected sums of tori. The manifolds $X_{k}$ discussed above have the property that their minimal volumes vanish, although they are connected sums of manifolds with non-vanishing minimal volumes. Thus the minimal volume, and even its (non-)vanishing, does not behave in a straightforward manner under connected sums.

This remark was motivated by the recent paper [35] of Paternain and Petean. After Theorem 2 appeared on the arXiv in [25], these authors remarked on the complicated behaviour of the minimal volume under connected sums based on some 6-dimensional examples, see Remark 3.1 in [35].

\section*{References}
\begin{itemize}
\item[1.] I. K. Babenko, Asymptotic invariants of smooth manifolds, Izv. Ross. Akad. Nauk. Ser. Mat. 56 (1992), 707-751 (Russian); Engl. transl. in Russian Acad. Sci. Izv. Math. 41 (1993), 1-38.
\item[2.] I. K. Babenko, Asymptotic volumes and simply connected surgeries of smooth manifolds, Izv. Ross. Akad. Nauk. Ser. Mat. 58 (1994), 218-221 (Russian); Engl. transl. in Russian Acad. Sci. Izv. Math. 44 (1995), 427-430.
\item[3.] I. K. Babenko, Extremal problems of geometry, surgery on manifolds, and problems in group theory, Izv. Ross. Akad. Nauk. Ser. Mat. 59 (1995), 97-108 (Russian); Engl. translation in Izv. Math. 59 (1995), 321-332.
\item[4.] S. Bauer, A stable cohomotopy refinement of Seiberg-Witten invariants: II, Invent. math. 155 (2004), 21-40.
\item[5.] S. Bauer and M. Furuta, A stable cohomotopy refinement of Seiberg-Witten invariants: I, Invent. math. 155 (2004), 1-19.
\item[6.] A. L. Besse, Einstein Manifolds, Springer Verlag 1987.
\item[7.] L. Bessières, Un théorème de rigidité différentielle, Comment. Math. Helv. 73 (1998), 443-479.
\item[8.] G. Besson, G. Courtois et S. Gallot, Volume et entropie minimale des espaces localement symétriques, Invent. math. 103 (1991), 417-445.
\item[9.] G. Besson, G. Courtois et S. Gallot, Entropies et rigidités des espaces localement symétriques de courbure strictement négative, Geom. Func. Analysis (GAFA) 5 (1995), 731-799.
\item[10.] R. L. Bishop and R. J. Crittenden, Geometry of Manifolds, Academic Press, New York 1964; reprinted by AMS Chelsea Publishing, Providence 2001.
\item[11.] M. Brunnbauer, Homological invariance for asymptotic invariants and systolic inequalities, Geom. Func. Analysis (GAFA) 18 (2008), 1087-1117.
\item[12.] M. Brunnbauer, M. Ishida and P. Suárez-Serrato, An essential relation between Einstein metrics, volume entropy, and exotic smooth structures, Math. Research Letters 16 (2009), 503-514.
\item[13.] J. Cheeger, A lower bound for the smallest eigenvalue of the Laplacian, in Problems in analysis (Papers dedicated to Salomon Bochner, 1969), pp. 195-199. Princeton Univ. Press, Princeton, N. J., 1970.
\item[14.] R. Fintushel and R. J. Stern, Rational blowdowns of smooth 4-manifolds, J. Differential Geometry 46 (1997), 181-235.
\end{itemize}
15. M. Furuta, Private communication, 2003.
16. M. Gromov, Volume and bounded cohomology, Publ. Math. I.H.E.S. 56 (1982), 5-99.
17. B. Hanke, D. Kotschick and J. Wehrheim, Dissolving four-manifolds and positive scalar curvature, Math. Zeit. 245 (2003), 545-555.
18. J. A. Hillman, Flat 4-manifold groups, New Zealand J. Math. 24 (1995), 29-40.
19. N. J. Hitchin, Compact four-dimensional Einstein manifolds, J. Differential Geometry 9 (1974), 435-441.
20. J. Kedra, D. Kotschick and S. Morita, Crossed flux homomorphisms and vanishing theorems for flux groups, Geom. Func. Analysis (GAFA) 16 (2006), 1246-1273.
21. D. Kotschick, The Seiberg-Witten invariants of symplectic four-manifolds, Séminaire Bourbaki, 48ème année, 1995-96, no. 812, Astérisque 241 (1997), 195-220.
22. D. Kotschick, Einstein metrics and smooth structures, Geometry \& Topology 2 (1998), 1-10.
23. D. Kotschick, On the Gromov-Hitchin-Thorpe inequality, C. R. Acad. Sci. Paris 326 (1998), 727-731.
24. D. Kotschick, Monopole classes and Einstein metrics, Intern. Math. Res. Notices 2004 no. 12 (2004), 593-609.
25. D. Kotschick, Entropies, volumes, and Einstein metrics, Preprint arXiv:math/0410215 v1 [math.DG] 8 Oct 2004.
26. D. Kotschick, J. W. Morgan and C. H. Taubes, Four-manifolds without symplectic structures but with non-trivial Seiberg-Witten invariants, Math. Research Letters 2 (1995), 119-124.
27. F. Ledrappier and X. Wang, An integral formula for the volume entropy with applications to rigidity, J. Differential Geometry 85 (2010), 461-477.
28. A. Manning, Topological entropy for geodesic flows, Ann. of Math. 110 (1979), 567-573.
29. A. Manning, More topological entropy for geodesic flows, In: Dynamical Systems and Turbulence, Springer LNM 898 (1981), 234-249.
30. J. Milnor, A note on curvature and the fundamental group, J. Differential Geometry 2 (1968), 1-7.
31. P. Ozsváth and Z. Szabó, Higher type adjunction inequalities in Seiberg-Witten theory, J. Differential Geometry 55 (2000), 385-440.
32. G. P. Paternain, Geodesic Flows, Progress in Mathematics vol. 180, Birkäuser Verlag 1999.
33. G. P. Paternain and J. Petean, Einstein manifolds of non-negative sectional curvature and entropy, Math. Research Letters 7 (2000), 503-515.
34. G. P. Paternain and J. Petean, Minimal entropy and collapsing with curvature bounded from below, Invent. math. 151 (2003), 415-450.
35. G. P. Paternain and J. Petean, Collapsing manifolds obtained by Kummer-type constructions, Trans. Amer. Math. Soc. 361 (2009), 4077-4090.
36. A. Sambusetti, An obstruction to the existence of Einstein metrics on 4-manifolds, Math. Ann. 311 (1998), 533-547.
37. R. Schmidt, Spectral geometry, asymptotic invariants, and geometric group theory, Diplomarbeit München 2009.
38. M. Wagner, Über die Klassifikation flacher Riemannscher Mannigfaltigkeiten, Diplomarbeit Basel 1997.

Mathematisches Institut, lmu München, Theresienstr. 39, 80333 München, Germany
E-mail address: dieter@member.ams.org
