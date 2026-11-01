---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 1801_01575.pdf
converter: mathpix
format: mmd
---

\title{
PUNCTURED SPHERES IN COMPLEX HYPERBOLIC SURFACES AND BIELLIPTIC BALL QUOTIENT COMPACTIFICATIONS
}

\author{
LUCA F. DI CERBO, MATTHEW STOVER
}

\begin{abstract}
In this paper, we study punctured spheres in two dimensional ball quotient compactifications ( $X, D$ ). For example, we show that smooth toroidal compactifications of ball quotients cannot contain properly holomorphically embedded 3-punctured spheres. We also use totally geodesic punctured spheres to prove ampleness of $K_{X}+\alpha D$ for $\alpha \in\left(\frac{1}{4}, 1\right)$, giving a sharp version of a theorem of the first author with G. Di Cerbo. Finally, we produce the first examples of bielliptic ball quotient compactifications modeled on the Gaussian integers.
\end{abstract}

\section*{1. Introduction}

Throughout this paper, a ball quotient compactification will mean the smooth toroidal compactification of a quotient $\mathbb{B}^{2} / \Gamma$ of the unit ball in $\mathbb{C}^{2}$ with its Bergman metric. Here $\Gamma \subset \operatorname{PU}(2,1)$ is a torsion-free nonuniform lattice such that all parabolic elements are rotation-free. See [AMRT10] and [Mok12] for details.

The primary purpose of this paper is to study holomorphically immersed or embedded spheres in ball quotient compactifications. For instance, we will prove the following results.

Theorem 1.1. Let $X$ be a ball quotient compactification with compactification divisor $D$.
\begin{itemize}
\item[(1)] If $C_{0} \subset X \backslash D$ is a holomorphically immersed totally geodesic submanifold, then $C_{0}$ has an even number of cusps.
\item[(2)] There are no properly holomorphically embedded 3-punctured spheres on $X \backslash D$ arising from smooth rational curves on $X$.
\item[(3)] If $X \backslash D$ contains a totally geodesic 4-punctured $\mathbb{P}^{1}$, then $X$ is not minimal and the totally geodesic 4-punctured $\mathbb{P}^{1}$ determines one of the exceptional curves on $X$.
\item[(4)] If $X \backslash D$ contains a totally geodesic 6-punctured $\mathbb{P}^{1}$, then $K_{X}$ is not ample and the totally geodesic 6-punctured $\mathbb{P}^{1}$ determines a smooth rational (-2)-curve on $X$.
\end{itemize}

We prove these, along with a number of related results, in §2. The method of proof is by studying the restriction of the complex hyperbolic metric on $X \backslash D$ to a curve on $X$. One can prove part (1) using the Hirzebruch-Höfer relative proportionality principle [BHH87], but we give an elementary differential-geometric proof
for the sake of completeness. One should compare Theorem 1.1(2) with the well-understood case of 3-punctured spheres on finite-volume hyperbolic 3-manifolds. It is a theorem of Colin Adams [Ada05] that any properly embedded essential 3-punctured sphere in a hyperbolic 3-manifold must be isotopic to one that is totally geodesic. One can then produce many examples of complete finite-volume hyperbolic 3-manifolds containing totally geodesic 3-punctured spheres via knots in $S^{3}$. It would also be interesting to know whether or not any properly embedded essential 3-punctured sphere in a ball quotient must be real totally geodesic. We suspect one could determine this via the Toledo invariant.

One consequence of Theorem 1.1 is the following sharp version of the ampleness theorem of the first author and G. Di Cerbo [DD15, Thm. 1.1], which gave ampleness of $K_{X}+\alpha D$ for $\alpha \in\left(\frac{1}{3}, 1\right)$.

Theorem 1.2. Let $(X, D)$ be a smooth toroidal compactification of a ball quotient surface. Then $K_{X}+\alpha D$ is ample for all $\alpha \in\left(\frac{1}{4}, 1\right)$. Moreover, this ampleness range is sharp, i.e., there are ball quotient compactifications for which $K_{X}+\frac{1}{4} D$ is nef but not ample.

Key in constructing examples where $K_{X}+\frac{1}{4} D$ is nef but not ample is the existence of ball quotient compactifications for which $X$ is birational to either an Abelian or bielliptic surface. In particular, we exploit the fact that all such known examples contain a holomorphically embedded $\mathbb{P}^{1}$ defining a punctured curve on $X \backslash D$ that is totally geodesic in the complex hyperbolic metric. In fact, we will use Theorem 1.1 to show the following, which proves that this phenomenon is no coincidence.

Theorem 1.3. Let $(X, D)$ be a ball quotient compactification such that $X$ is birational to either an Abelian or bielliptic surface $Y$. Then $X$ is the blowup of $Y$ at $n$ distinct points for some $n \geq 1$. Every exceptional curve on $X$ meets $D$ transversally in four points and determines a totally geodesic 4-punctured $\mathbb{P}^{1}$ on $X \backslash D$. Conversely, every holomorphically embedded totally geodesic sphere on $X \backslash D$ is a 4-punctured $\mathbb{P}^{1}$ arising from the exceptional locus of the blowup.

We briefly recall the history of the existence of ball quotient compactifications birational to an Abelian or bielliptic surface. The first Abelian example was constructed by Hirzebruch [Hir84], and it is closely related to the arithmetic of the Eisenstein integers. Later, Holzapfel constructed an example based on the Gaussian integers [Hol04]. The first bielliptic ball quotient compactifications were discovered only very recently in [DS18]. These examples emerged in the study of minimal volume complex hyperbolic surfaces with cusps, and they are all modeled on the Eisenstein integers. See [DS16, DS17] for other applications.

Recall that bielliptic surfaces are the minimal projective surfaces with Kodaira dimension $\kappa=0$ and irregularity $q=1$. A classical result of Bagnera and de Franchis from 1907 classifies bielliptic surfaces into seven topological types, characterized by a finite group $G$ such that $X$ is the quotient of a product of two elliptic curves by a free action of $G$. Moreover, $G$ must be $\mathbb{Z} / 2, \mathbb{Z} / 3,(\mathbb{Z} / 3)^{2}, \mathbb{Z} / 4$,
$\mathbb{Z} / 4 \times \mathbb{Z} / 2,(\mathbb{Z} / 2)^{2}$, or $\mathbb{Z} / 6$ (see §3 for the precise classification). The examples in [DS18] are associated with the groups $\mathbb{Z} / 3$ and $(\mathbb{Z} / 3)^{2}$.

In §3 we construct the first examples of bielliptic ball quotient compactifications modeled on the Gaussian integers. In the Bagnera-de Franchis classification there are exactly four group actions associated with the Gaussian integers, and we construct examples for each of these four topological types. The associated ball quotients are not commensurable with those studied in [DS18], but are still of relatively small volume. We also discuss our examples in relation with Holzapfel's example of Abelian type [Hol04]. In terms of the classification of bielliptic surfaces, this gives the following.

Theorem 1.4. For each of the groups $\mathbb{Z} / 2,(\mathbb{Z} / 2)^{2}, \mathbb{Z} / 4$, and $\mathbb{Z} / 4 \times \mathbb{Z} / 2$, there exists a ball quotient compactification with minimal model a bielliptic surface of that type.

We conclude this introduction by addressing some topological aspects connected with the existence of ball quotient compactifications with Kodaira dimension zero. Smooth projective surfaces of Kodaira dimension zero are birational to Abelian surfaces, bielliptic surfaces, K3 surfaces, and Enriques surfaces [Bea96, Ch. VIII]. While much is now known about the existence of bielliptic and Abelian ball quotient compactifications, it remains unclear whether or not ball quotient compactifications birational to K3 or Enriques surfaces exist. We note however that one can use known examples of ball quotient compactifications birational to Abelian surfaces to construct ball quotient orbifolds whose underlying analytic space admits a compactification by a Kummer K3 surface. For example, see [Hol98, §5.5.4A].

This problem is connected with several topological problems regarding smooth toroidal compactifications. For example, it was previously claimed in the literature that ball quotient compactifications must have nonzero $1{ }^{\text {st }}$ Betti number. This would imply the nonexistence of ball quotient compactifications birational to K3 or Enriques surfaces. Unfortunately, this claim is also not true. In the Appendix, we describe a ball quotient compactification of general type with irregularity zero and Euler number 48, found using Magma Mag.

Acknowledgments. The authors thank the International Centre for Theoretical Physics (ICTP) for the excellent working environment during the early stages of this collaboration, and the referee for pertinent comments on the manuscript. The first author would like to thank Maria Beatrice Pozzetti for asking whether or not bielliptic ball quotient compactifications modeled on the Gaussian integers exist, and Gabriele Di Cerbo for asking whether an improved version of Theorem 1.1 in [DD15] could be proved in the case of surfaces. Finally, he would like to thank the Stony Brook University math department for generously encouraging him through the years and for providing an inspiring environment of brilliant math. The first author was partially supported by the S.-S. Chern Fellowship at ICTP. The second author was supported by the National Science Foundation under Grant Number NSF 1361000 and Grant Number 523197 from the Simons Foundation/SFARI.

\section*{2. Totally geodesic (and other) punctured spheres}

To start, we briefly recall the notion of a general ball quotient compactification. Let $X$ be a smooth projective surface with canonical divisor $K_{X}$ and $D \subset X$ be a reduced simple normal crossings divisor. Then one has the logarithmic Chern numbers
$$\begin{aligned}
& \bar{c}_{1}^{2}(X, D)=\left(K_{X}+D\right)^{2} \\
& \bar{c}_{2}(X, D)=e(X \backslash D),
\end{aligned}$$
where $e$ denotes the topological Euler number. When $K_{X}+D$ is big and nef one has the logarithmic Bogomolov-Miyaoka-Yau inequality $\bar{c}_{1}^{2} \leq 3 \bar{c}_{2}$ (henceforth $\log -B M Y)$. Moreover, equality occurs if and only if $X \backslash D$ is biholomorphic to the quotient $\mathbb{B}^{2} / \Gamma$, where $\Gamma$ is a torsion-free nonuniform lattice in $\operatorname{PU}(2,1)$ with all parabolic elements rotation-free acting by isometries on the unit ball $\mathbb{B}^{2}$ in $\mathbb{C}^{2}$ equipped with the symmetric Bergman metric. Finally, it can be shown that in this case $D$ is necessarily a disjoint union of reduced elliptic curves with negative self-intersection. One then says that $X$ is a smooth toroidal compactification of $\mathbb{B}^{2} / \Gamma$ with compactification divisor $D$. See [AMRT10], [Mok12], or [DS18] for the proofs of these statements and more details. In this paper we will shorten this to ball quotient compactification, as we will not consider any other type of compactification.

Let $X$ be a smooth projective variety with $D \subset X$ a divisor such that the pair $(X, D)$ is a ball quotient compactification, and let $\omega_{1}$ denote the locally symmetric metric on $X \backslash D$. When regarded as a current on $X$, this Kähler metric is proportional to the cohomology class of $K_{X}+D$ [Mum77].

Consider a smooth embedded irreducible complete curve $C \hookrightarrow X$ not contained in the boundary divisor $D$. We assume that $C$ and $D$ intersect transversally, set
$$\left\{p_{1}, \ldots, p_{k}\right\}=C \cap D,$$
and let $C_{k}$ denote the curve $C$ punctured at the points $p_{1}, \ldots, p_{k}$. The Bergman metric $\omega_{1}$ then induces a smooth finite-volume Kähler metric $\omega_{C_{k}}$ on the punctured curve $C_{k}$ with associated Ricci form $\rho_{C_{k}}$. By [KN96, Prop. IX.9.5], we have
$$\rho_{C_{k}}=-\left.\left(\omega_{1}\right)\right|_{C_{k}}-\mathcal{R},$$
where $\mathcal{R}$ is a semidefinite form that vanishes if and only if $C$ is embedded and totally geodesic.

Observe that $\omega_{C_{k}}$ has finite volume. The finite volume Gauss-Bonnet theorem then implies that
$$-\frac{1}{2 \pi} \int_{C_{k}} \rho_{C_{k}}=-\chi\left(C_{k}\right)=-\chi(C)+k=2 g(C)-2+k .$$
Next, recall that proportionality gives $c_{1}\left(K_{X}+D\right)=\frac{3}{4 \pi} \omega_{1}$. Thus (1) gives
$$-\frac{1}{2 \pi} \int_{C_{k}} \rho_{C_{k}}=2 g(C)-2+k \geq \frac{1}{2 \pi} \int_{C} \omega_{1}=\frac{2}{3}\left(K_{X}+D\right) \cdot C$$
with equality if and only if $C$ is an embedded totally geodesic curve. Thus we have:

Proposition 2.1. Let $C$ be an embedded curve in a ball quotient surface compactification $(X, D)$ such that $C$ intersects $D$ transversally in $k$ points. Then
$$3(g(C)-1)+\frac{k}{2} \geq K_{X} \cdot C$$
with equality if and only if $C_{k}$ is totally geodesic in $X \backslash D$ with respect to its locally symmetric metric $\omega_{1}$.

Proposition 2.1 can be alternatively formulated as follows.
Proposition 2.2. Let $C$ be an embedded curve in a ball quotient surface compactification $(X, D)$ such that $C$ intersects $D$ transversally. We then have
$$3 C^{2} \geq-\left(K_{X}+D\right) \cdot C$$
with equality if and only if $C \cap(X \backslash D)$ is totally geodesic in $X \backslash D$ with respect to $\omega_{1}$.

Proof. First, we have that
$$g(C)-1=\frac{K_{X} \cdot C+C^{2}}{2} .$$
Next, we have that $k=D \cdot C$. Thus, the inequality given in Proposition 2.1 becomes
$$\frac{3}{2}\left(K_{X} \cdot C+C^{2}\right)+\frac{D \cdot C}{2} \geq K_{X} \cdot C,$$
hence
$$3 C^{2} \geq-K_{X} \cdot C-D \cdot C,$$
which completes the proof. \(\square\)

This gives us the following consequence when $C$ is an exceptional curve on $X$.
Corollary 2.3. An exceptional curve of the first kind in a ball quotient compactification $X$ that intersects $D$ transversally must have at least four intersection points.

Proof. Let us denote the exceptional curve of the first kind in $X$ by $C$. Recall that $C \simeq \mathbb{P}^{1}$ and $K_{X} \cdot C=C^{2}=-1$. Next, observe that $C$ must intersect $D$ at least three times, as $X \backslash D$ has negative curvature. Using Proposition 2.1, we obtain $k \geq 4$ with equality if and only if $C_{k}$ is totally geodesic in $X \backslash D$ with respect to the Bergman metric. \(\square\)

We now show that Corollary 2.3 holds even without the transversality requirement. More precisely, let $C$ be an exceptional curve of the first kind in the smooth compactification $(X, D)$. Then, there are integers $m_{i} \geq 1$ such that
$$D \cap C=\sum_{i=1}^{k} m_{i} p_{i} .$$
Then $m_{i}=1$ if and only if $C$ meets $D$ transversally at $p_{i}$, and $m_{i} \geq 2$ otherwise. The generalized relative Hirzebruch-Höfer proportionality theorem given in Theorem 0.1 of [MVZ09] is
$$3 C^{2} \geq-K_{X} \cdot C+\sum_{i=1}^{k}\left(2 m_{i}-3\right)$$
with equality if and only if $C \backslash\left\{p_{1}, \ldots, p_{k}\right\}$ is totally geodesic with respect to the Bergman metric on $X \backslash D$.

Therefore, if $C$ is an exceptional curve of the first kind we have
$$C^{2}=K_{X} \cdot C=-1,$$
and then
$$-4 \geq \sum_{i=1}^{k}\left(2 m_{i}-3\right),$$
with equality if and only if $C \backslash\left\{p_{1}, \ldots, p_{k}\right\}$ is totally geodesic. We then have the following generalization of Corollary 2.3.

Proposition 2.4. An exceptional curve of the first kind in a ball quotient compactification $X$ must have at least four intersection points with the compactification divisor $D$. Moreover, it has exactly four intersection points if and only if it is totally geodesic.

We are now ready to prove Theorem 1.1.
Proof of Theorem 1.1. We first prove (1). Suppose that $C_{0}$ is a holomorphically immersed totally geodesic submanifold of $X \backslash D$. When $C_{0}$ is embedded, [Hol98, Lem. 4.4.8] gives that the compactification $C$ of $C_{0}$ in $X$ is smooth and that $C$ intersects $D$ transversally. The result is then immediate from Proposition 2.1. Indeed, we have
$$3(g(C)-1)+\frac{k}{2}=K_{X} \cdot C$$
with $3(g(C)-1)$ and $K_{X} \cdot C$ integers, hence $k$ is even.
We now argue that we can pass to an étale finite cover $X^{\prime} \backslash D^{\prime}$ of $X \backslash D$ such that $C_{0}$ lifts to an embedded totally geodesic $C_{0}^{\prime}$ in $X^{\prime} \backslash D^{\prime}$ with $k$ cusps. Then $X^{\prime}$ is a ball quotient compactification and $C_{0}^{\prime}$ is a $k$-cusped embedded totally geodesic $k$-punctured $\mathbb{P}^{1}$ in $X^{\prime} \backslash D^{\prime}$, which we have seen is impossible when $k$ is odd.

Indeed, it is well-known that totally geodesic immersions can be promoted to embeddings in finite covers. We sketch the argument. Let $C_{0}^{\prime}$ denote the $k$-punctured $\mathbb{P}^{1}$ so that there is a totally geodesic immersion $f: C_{0}^{\prime} \rightarrow X \backslash D$ with image $C_{0}$, and let $\widetilde{f}: \mathbb{B}^{1} \hookrightarrow \mathbb{B}^{2}$ be the associated totally geodesic embedding of universal coverings. Suppose
$$\Gamma=\pi_{1}(X \backslash D) \subset \operatorname{PU}(2,1)$$
and let $\Delta \subset \Gamma$ be the stabilizer in $\Gamma$ of $\widetilde{f}\left(\mathbb{B}^{1}\right)$. Then $\widetilde{f}\left(\mathbb{B}^{1}\right) / \Delta$ is homotopy equivalent to $C_{0}^{\prime}$. Now, $\Delta$ is separable in $\Gamma$, i.e., given $\gamma \in \Gamma$ with $\gamma \notin \Delta$, there exists a finite index subgroup $\Gamma^{\prime} \subset \Gamma$ such that $\Delta \subset \Gamma^{\prime}$ and $\gamma \notin \Gamma^{\prime}$. See the "Lemme Principal" on p. 113 of [Ber00].

Next, we apply the classic topological characterization of separability due to Peter Scott [Sco78] to obtain a finite étale covering $X^{\prime} \backslash D^{\prime}$ of $X \backslash D$ into which $C_{0}^{\prime}$ embeds as a holomorphic totally geodesic submanifold. Replace $(X, D)$ with $\left(X^{\prime}, D^{\prime}\right)$ and $C_{0}$ with its lift to $X^{\prime} \backslash D^{\prime}$, which is biholomorphic to $C_{0}^{\prime}$. Crucially, $C_{0}$ and $C_{0}^{\prime}$ have the same number of cusps $k$. Then the application of Proposition 2.1 that began the proof now applies to $C_{0}^{\prime}$, and hence $k$ cannot be odd.

Now, we prove (2). We must show that a ball quotient compactification contains no holomorphically embedded 3-punctured $\mathbb{P}^{1}$ arising from a smooth rational curve on $X$. Let $C$ be such a rational curve. Applying the adjunction formula to Equation (3) we have
$$2 C^{2}-2 \geq \sum_{i=1}^{3}\left(2 m_{i}-3\right) \geq-3$$
so that we necessarily have $C^{2} \geq 0$.
Then $K_{X} \cdot C<0$ by adjunction, hence $K_{X}$ is not nef. Since $C$ is not a -1 curve, it follows that the plurigenera of $X$ are all zero, hence $X$ is a ruled surface. If $C^{2} \geq 1$, then $C$ cannot be contained in a fiber of the ruling, so $X$ must be a rational ruled surface. Case-by-case analysis shows that the only rational ruled surface with a rational curve of positive self-intersection is $\mathbb{P}^{2}$. Clearly $\mathbb{P}^{2}$ is not a ball quotient compactification, since elliptic curves on $\mathbb{P}^{2}$ have positive self-intersection.

Next, suppose that $C^{2}=0$. We then have
$$-2 \geq \sum_{i=1}^{3}\left(2 m_{i}-3\right),$$
and the only possibility is $m_{1}=m_{2}=m_{3}=1$, so $C$ meets $D$ transversally in three points. We already saw that $X$ must be ruled over a curve $B$ and, since $X$ contains an elliptic curve, the Hurwitz formula implies that $B$ is rational or elliptic. Moreover, Zariski's lemma implies that $C$ must be a smooth fiber of the ruling.

We can rule out minimal ruled surfaces as in the proof of Theorem 2.3 in [DD15]. We briefly sketch the argument. If $X$ is a Hirzebruch surface, then all irreducible curves of negative self-intersection are rational, which is impossible since $X$ contains elliptic curves of negative self-intersection. If $X$ is ruled over an elliptic curve, then $D$ must consist of exactly one zero section of the ruling. One then finds a once-punctured $\mathbb{P}^{1}$ in $X \backslash D$, which is impossible since $X \backslash D$ admits a Kähler metric of negative curvature.

In other words, $X$ must be the blow up of a surface ruled over an elliptic or rational curve, hence there exists a fiber that contains at least one exceptional curve of the first kind. On the other hand, Proposition 2.4 shows that the compactifying divisor must meet an exceptional curve of the first kind in at least four distinct points. Note that no component of the compactifying divisor can be contained in a fiber. Now, let
$$F=E_{1}+\cdots+E_{j}$$
be a fiber containing at least one exceptional curve, which we assume is $E_{1}$. Fibers are numerically equivalent and the compactification divisor satisfies $D \cdot C=3$. We then have the contradiction
$$3=D \cdot C=D \cdot F \geq D \cdot E_{1} \geq 4,$$
which proves (2).
Finally we prove (3) and (4). Again by [Hol98, Lem. 4.4.8] we know that the compactification $C$ of the totally geodesic punctured $\mathbb{P}^{1}$ in $X$ is smooth and intersects $D$ transversally. If such a $\mathbb{P}^{1}$ is punctured 4 times, then Proposition 2.1
implies that
$$-3+2=K_{X} \cdot C,$$
so $K_{X} \cdot C=C^{2}=-1$. This shows that $C$ is indeed an exceptional divisor in $X$. Similarly, if $C$ is the compactification of a totally geodesic 6-punctured sphere in $X$, Proposition 2.1 implies that
$$-3+3=K_{X} \cdot C,$$
so $C^{2}=-2$ by adjuction. This completes the proof of the theorem. \(\square\)

We can now prove Theorem 1.2. First we briefly recall the notion of an extremal ray in the cone $\overline{\mathrm{NE}}(X)$ of numerically effective 1-cycles on $X$, along with its length. A ray $R$ in $\overline{\mathrm{NE}}(X)$ is extremal when $x+y \in R$ and $x, y \in \overline{\mathrm{NE}}(X)$ implies that $x, y \in R$. Suppose $R$ is a ray such that $K_{X} \cdot Z<0$ for any effective 1-cycle $Z \in R$. Then the length of $R$ is the minimum of $-K_{X} \cdot C$ for $C$ a rational curve in $R$.

Proof of Theorem 1.2. The proof is a combination of Mori's theory together with the generalized relative proportionality principle. More precisely, Theorem 2.3 in [DD15] implies that the length of an extremal ray in a smooth toroidal compactification of a ball quotient is at most one. Moreover, the associated contraction map is the blowup map at a codimension two smooth subvariety. See Corollary 2.8 in [DD15].

Therefore, in the case of surfaces we conclude that the extremal rays in a smooth ball quotient compactification with non-nef canonical divisor are exceptional curves of the first kind, that is, smooth rational curves $\left\{C_{i}\right\}$ in $X$ such that $K_{X} \cdot C_{i}=$ $C_{i}^{2}=-1$. By the cone theorem [Mat02, Thm. 10-2-1], we have that
$$\overline{\mathrm{NE}}(X)=\overline{\mathrm{NE}}(X)_{K_{X} \geq 0}+\sum \mathbb{R}_{\geq 0}\left[C_{i}\right],$$
where $\overline{\mathrm{NE}}(X)_{K_{X} \geq 0}$ are the points in $\overline{\mathrm{NE}}(X)$ that pair nonnegatively with $K_{X}$, and where the $\left\{C_{i}\right\}$ are the (possibly countably many) extremal rays. See [DD15, §2] for further details and references.

Then any curve $C$ on $X$ is numerically equivalent to
$$a_{1} C_{1}+\ldots+a_{k} C_{k}+F,$$
where the $a_{i}$ are positive real numbers, the $\left\{C_{i}\right\}$ are a finite collection of extremal rays, and $F$ is an effective divisor such that $K_{X} \cdot F \geq 0$. Thus, by Proposition 2.4, we conclude that $D \cdot C_{i} \geq 4$ for all $i$, with equality if and only if the punctured sphere defined by $C_{i}$ on $X \backslash D$ is totally geodesic.

Since $K_{X}+D$ is big and nef for any smooth ball quotient compactification, we also have that
$$\left(K_{X}+\alpha D\right) \cdot C \geq \sum_{i=1}^{k} a_{i}\left(K_{X}+\alpha D\right) C_{i} \geq \sum_{i=1}^{k} a_{i}(-1+4 \alpha),$$
for any curve $C$ in $X$, since $F$ is effective. Thus we also have that
$$\left(K_{X}+\alpha D\right) \cdot C>0$$
for any $\alpha \in\left(\frac{1}{4}, 1\right)$. This fact combined with the fact that $K_{X}+D$ is big immediately implies that $K_{X}+\alpha D$ is indeed an ample $\mathbb{R}$-divisor for any $\alpha \in\left(\frac{1}{4}, 1\right)$. Moreover, if $K_{X}+\frac{1}{4} D$ is nef but not ample then there must exist an exceptional curve of the first kind $C_{i}$ such that $D \cdot C_{i}=4$. By Proposition 2.4, we have that such a curve $C_{i}$ determines a totally geodesic 4-punctured $\mathbb{P}^{1}$ in $X \backslash D$.

In §3, we construct ball quotient compactifications with exceptional curves of the first kind intersecting the boundary divisor transversally in exactly four points. See [Hir84, Hol86, Hol04, DS18] for other examples. Pick one such ball quotient $(X, D)$. Then we have
$$\left(K_{X}+\frac{1}{4} D\right) \cdot E_{i}=0$$
for any of the exceptional divisors $\left\{E_{i}\right\}$ in $X$, so these exceptional divisors give totally geodesic 4-punctured $\mathbb{P}^{1}$. Clearly $K_{X}+\frac{1}{4} D$ is not ample. In conclusion, the ampleness range given by $\alpha \in\left(\frac{1}{4}, 1\right)$ cannot be improved in general and the result is indeed sharp as claimed. \(\square\)

We close this section with the proof of Theorem 1.3.
Proof of Theorem 1.3. Let $(X, D)$ be a ball quotient compactification such that $X$ is birational to an Abelian or bielliptic surface $Y$. Then there is sequence of blowups $\pi: X \rightarrow Y$. Moreover, $K_{X}$ is numerically equivalent to the blowup divisor
$$E=\sum_{i=1}^{n} \alpha_{i} E_{i},$$
where the $E_{i}$ are distinct smoothly embedded rational curves and each $\alpha_{i} \geq 1$ is an integer. Since Abelian and bielliptic surfaces have universal cover $\mathbb{C}^{2}$, every rational curve on $X$ is numerically equivalent to some $E_{i}$.

We then have
$$\begin{aligned}
\bar{c}_{1}^{2}(X, D) & =-n-D^{2} \\
3 \bar{c}_{2}(X, D) & =3 n,
\end{aligned}$$
so the log-BMY inequality gives $-D^{2}=4 n$. However, adjunction gives
$$-D^{2}=K_{X} \cdot D=\sum_{i=1}^{n} \alpha_{i} D \cdot E_{i} .$$
Theorem 1.1 then implies that $D \cdot E_{i} \geq 4$ for each $i$, hence $-D^{2} \geq 4 n$ with equality if and only if $D \cdot E_{i}=4$ and $\alpha_{i}=1$ for all $i$. This proves that every $E_{i}$ defines a 4-punctured $\mathbb{P}^{1}$ on $X$, and the associated punctured curve on $X \backslash D$ is therefore totally geodesic.

From our conclusion that $\alpha_{i}=1$ for all $i$, we claim that $X$ must be the blowup of $Y$ at $n$ distinct points, with the $E_{i}$ precisely the exceptional curves on $X$ of the first kind. Indeed, suppose that $\pi$ can be realized by the sequence of blowups
$$X_{n}=Y \rightarrow X_{n-1} \rightarrow \cdots \rightarrow X_{1} \rightarrow X_{0}=Y$$
with $\widehat{E}_{j}$ the exceptional divisor of the blowup $\sigma_{i}: X_{j} \rightarrow X_{j-1}$. We then have the canonical divisor formula
$$K_{X_{i}}=\sigma_{i}^{*} K_{X_{i-1}}+\widehat{E}_{i},$$
where $\sigma_{i}^{*}$ denotes the total transform. Since $K_{Y}$ is trivial, it is immediate that $K_{X}=\sum E_{i}$ when $X$ is the blowup of $Y$ at $n$ distinct points.

On the other hand, suppose that
$$K_{X_{j-1}}=\sum_{k=1}^{j-1} \beta_{k} \widetilde{E}_{k}$$
and that $\sigma_{j}$ is the blowup of $X_{j-1}$ at a point on $\widetilde{E}_{k}, 1 \leq k \leq j-1$. Then we have
$$\begin{aligned}
K_{X_{j}} & =\sigma^{*} K_{X_{j-1}}+\widehat{E}_{j} \\
& =2 \widehat{E}_{j}+\sum_{k=1}^{j-1} \beta_{k} \widetilde{E}_{k}^{\prime},
\end{aligned}$$
where $\widetilde{E}_{k}^{\prime}$ is the strict transform of $\widetilde{E}_{k}$. Indeed, the total transform of $\widetilde{E}_{k}$ is $\widetilde{E}_{k}^{\prime}+\widehat{E}_{j}$. Inducting on the length of the chain of blowups from $X$ to $Y$, it follows that $\alpha_{j} \geq 2$ in (6), and that $\alpha_{j}=1$ for all $j$ if and only if $X$ is the blowup of $Y$ at $n$ distinct points. This proves the claim, and therefore completes the proof of the theorem. \(\square\)

\section*{3. New bielliptic compactifications}

In this section, we construct our main new examples of a bielliptic ball quotient compactifications. First we briefly recall the classification of bielliptic surfaces.

One characterization is that bielliptic surfaces are the minimal smooth projective surfaces with Kodaira dimension 0 and irregularity 1 (i.e., $1^{\text {st }}$ Betti number 2). See [Bea96, Ch. VIII]. By the classical theorem of Bagnera and de Franchis Bea96, Thm. VI.20], a bielliptic surface is constructed as follows. Let $E_{1} \times E_{2}$ be a product of two elliptic curves and $G$ be a group of translations of $E_{2}$ that also acts on $E_{1}$ as a group of automorphisms with quotient $\mathbb{P}^{1}$. Then $X=\left(E_{1} \times E_{2}\right) / G$ is a bielliptic surface. More specifically:

Theorem 3.1 (Bagnera-de Franchis, 1907). Let $E_{\lambda}$ and $E_{\tau}$ be elliptic curves associated with the lattices $\mathbb{Z}[1, \lambda]$ and $\mathbb{Z}[1, \tau]$, respectively, and $G$ be a group of translations of $E_{\tau}$ acting on $E_{\lambda}$ such that $E_{\lambda} / G=\mathbb{P}^{1}$. Then every bielliptic surface is of the form $\left(E_{\lambda} \times E_{\tau}\right) / G$ where $G$ has one of the following types:
\begin{itemize}
\item[(1)] $G=\mathbb{Z} / 2$ acting on $E_{\lambda}$ by $x \rightarrow-x$;
\item[(2)] $G=\mathbb{Z} / 2 \times \mathbb{Z} / 2$ acting on $E_{\lambda}$ by
$$x \rightarrow-x \quad \text { and } \quad x \rightarrow x+\alpha_{2},$$
where $\alpha_{2}$ is a 2-torsion point;
\item[(3)] $G=\mathbb{Z} / 4$ acting on $E_{\lambda}$ by $x \rightarrow \lambda x$, where $\lambda=i$;
\item[(4)] $G=\mathbb{Z} / 4 \times \mathbb{Z} / 2$ acting on $E_{\lambda}$ by
$$x \rightarrow \lambda x \quad \text { and } \quad x \rightarrow x+\frac{1+\lambda}{2},$$
where $\lambda=i$;
\end{itemize}
\begin{itemize}
\item[(5)] $G=\mathbb{Z} / 3$ acting on $E_{\lambda}$ by $x \rightarrow \lambda x$, where $\lambda=e^{\frac{2 \pi i}{3}}$;
\item[(6)] $G=\mathbb{Z} / 3 \times \mathbb{Z} / 3$ acting on $E_{\lambda}$ by
$$x \rightarrow \lambda x \quad \text { and } \quad x \rightarrow x+\frac{1-\lambda}{3},$$
where $\lambda=e^{\frac{2 \pi i}{3}}$;
\item[(7)] $G=\mathbb{Z} / 6$ acting on $E_{\lambda}$ by $x \rightarrow \zeta x$, where $\lambda=e^{\frac{2 \pi i}{3}}$ and $\zeta=e^{\frac{\pi i}{3}}$.
\end{itemize}

Realizing $\mathbb{Z} / 2$.
To begin our construction, let $E$ be the elliptic curve associated with the Gaussian lattice $\mathbb{Z}[1, i]=\mathbb{Z}+\mathbb{Z} i$, where $i^{2}=-1$. In this section, we construct a $\mathbb{Z} / 2 \mathbb{Z}$ bielliptic ball quotient modeled on the Abelian surface $A=E \times E$. To this aim, consider the degree two automorphism $\varphi: A \rightarrow A$ given by
$$\varphi(w, z)=\left(-w+\frac{1+i}{2}, z+\frac{1+i}{2}\right) .$$
Note that $\varphi$ generates a free action of $\mathbb{Z} / 2$ on $A$. Let
$$\pi: A \rightarrow B=A /\langle\varphi\rangle$$
be the associated degree two étale quotient. This is a slightly different version of the "standard" $\mathbb{Z} / 2$-action appearing in the Bagnera-de Franchis classification. We adopt this one for computational convenience, and discuss the connection with the standard action below. In what follows, $(w, z)$ will denote coordinates on $A$ and $[w, z]$ the coordinates on $B$ for $\pi(w, z)$.

Next, we define elliptic curves
$$\begin{array}{ll}
E_{1}=(z, z) & E_{2}=\left(i z+\frac{1+i}{2}, z\right) \\
E_{3}=(-z, z) & E_{4}=\left(-i z+\frac{1+i}{2}, z\right)
\end{array}$$
on the Abelian surface $A$. These curves are constructed so that
$$\varphi\left(E_{1}\right)=E_{3} \quad \varphi\left(E_{2}\right)=E_{4} .$$
Moreover, one can easily check that:
$$\begin{aligned}
& E_{1} \cap E_{3}=\left\{(0,0),\left(\frac{1}{2}, \frac{1}{2}\right),\left(\frac{i}{2}, \frac{i}{2}\right),\left(\frac{1+i}{2}, \frac{1+i}{2}\right)\right\} \\
& E_{2} \cap E_{4}=\left\{\left(0, \frac{1+i}{2}\right),\left(\frac{1}{2}, \frac{1}{2}\right),\left(\frac{i}{2}, \frac{i}{2}\right),\left(\frac{1+i}{2}, 0\right)\right\} \\
& E_{1} \cap E_{2}=E_{1} \cap E_{4}=E_{2} \cap E_{3}=E_{3} \cap E_{4}=\left\{\left(\frac{1}{2}, \frac{1}{2}\right),\left(\frac{i}{2}, \frac{i}{2}\right)\right\}
\end{aligned}$$
Furthermore, consider the two vertical and two horizontal elliptic curves in $A$ defined by the equations:
$$\begin{array}{ll}
F_{1}=(w, 0) & F_{3}=(0, z) \\
F_{2}=\left(w, \frac{1+i}{2}\right) & F_{4}=\left(\frac{1+i}{2}, z\right)
\end{array}$$

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/962c7a8d-1484-46fe-97bc-936aaf9e3a23-12.jpg?height=884&width=896&top_left_y=414&top_left_x=612}
\captionsetup{labelformat=empty}
\caption{Figure 1. The arrangement of curves on the Abelian surface.}
\end{figure}
These curves satisfy
$$\varphi\left(F_{1}\right)=F_{2} \quad \varphi\left(F_{3}\right)=F_{4},$$
and we easily check that:
$$\begin{aligned}
& F_{1} \cap F_{3}=E_{1} \cap F_{1}=E_{1} \cap F_{3}=E_{3} \cap F_{1}=E_{3} \cap F_{3}=\{(0,0)\} \\
& F_{1} \cap F_{4}=E_{2} \cap F_{1}=E_{2} \cap F_{4}=E_{4} \cap F_{1}=E_{4} \cap F_{4}=\left\{\left(\frac{1+i}{2}, 0\right)\right\} \\
& F_{2} \cap F_{3}=E_{2} \cap F_{2}=E_{2} \cap F_{3}=E_{4} \cap F_{2}=E_{4} \cap F_{3}=\left\{\left(0, \frac{1+i}{2}\right)\right\} \\
& F_{2} \cap F_{4}=E_{1} \cap F_{2}=E_{1} \cap F_{4}=E_{3} \cap F_{2}=E_{3} \cap F_{4}=\left\{\left(\frac{1+i}{2}, \frac{1+i}{2}\right)\right\}
\end{aligned}$$
See Figure 1. Concluding, the curves $\left\{E_{j}\right\}_{j=1}^{4}$ and $\left\{F_{j}\right\}_{j=1}^{4}$ meet only in the following six points:
$$\mathcal{P}=\left\{(0,0),\left(\frac{1}{2}, \frac{1}{2}\right),\left(\frac{i}{2}, \frac{i}{2}\right),\left(\frac{1+i}{2}, 0\right),\left(0, \frac{1+i}{2}\right),\left(\frac{1+i}{2}, \frac{1+i}{2}\right)\right\}$$
Moreover, there are exactly four elliptic curves passing through each of these points.
Let be $Y$ the blowup of $A$ at the points in $\mathcal{P}$. Further, let $\left\{C_{j}\right\}_{j=1}^{4}$ and $\left\{D_{j}\right\}_{j=1}^{4}$ denote the proper transforms of the elliptic curves $\left\{E_{j}\right\}_{j=1}^{4}$ and $\left\{F_{j}\right\}_{j=1}^{4}$ to $Y$. Finally, set
$$\mathcal{D}_{0}=\sum_{j=1}^{4}\left(C_{j}+D_{j}\right) \subset Y .$$
We now have the following:

Lemma 3.2. The pair $\left(Y, \mathcal{D}_{0}\right)$ is the smooth toroidal compactification of a complex hyperbolic surface with eight cusps and Euler number six.

Proof. One easily computes that
$$\begin{aligned}
\bar{c}_{1}^{2}\left(Y, \mathcal{D}_{0}\right) & =K_{Y}^{2}-\mathcal{D}_{0}^{2} \\
& =-6+4+4+4+4+2+2+2+2 \\
& =18,
\end{aligned}$$
and clearly $e\left(Y \backslash \mathcal{D}_{0}\right)=6$, since $Y$ is the blowup of an Abelian surface at six points. Therefore $\bar{c}_{1}^{2}\left(Y, \mathcal{D}_{0}\right)=18=3 \bar{c}_{2}\left(Y, \mathcal{D}_{0}\right)$, hence we have equality in the log-BMY inequality. Since $K_{Y}+\mathcal{D}_{0}$ is visibly nef and big, the lemma follows. \(\square\)

We are now ready to construct the bielliptic example. Define the following curves on the bielliptic surface $B$ :
$$\begin{array}{ll}
G_{1}=\pi\left(E_{1}\right)=\pi\left(E_{3}\right) & G_{2}=\pi\left(E_{2}\right)=\pi\left(E_{4}\right) \\
H_{1}=\pi\left(F_{1}\right)=\pi\left(F_{2}\right) & H_{2}=\pi\left(F_{3}\right)=\pi\left(F_{4}\right)
\end{array}$$
Note that this is well defined by (8) and (9). We then have the following lemma.
Lemma 3.3. The curves $G_{1}, G_{2}$ are singular elliptic curves with exactly two nodes, and $H_{1}, H_{2}$ are smooth elliptic curves. Moreover, we have the following intersections:
$$\left\{\begin{array}{l}
G_{1} \cap G_{2}=\left\{\left[\frac{1}{2}, \frac{1}{2}\right]\right\} \\
H_{1} \cap H_{2}=\left\{[0,0],\left[\frac{1+i}{2}, 0\right]\right\} \\
G_{1} \cap H_{1}=G_{1} \cap H_{2}=\{[0,0]\} \\
G_{2} \cap H_{1}=G_{2} \cap H_{2}=\left\{\left[\frac{1+i}{2}, 0\right]\right\}
\end{array}\right.$$
Proof. The curves $E_{1}$ and $E_{3}$ meet transversally in four points, and these points are the disjoint union of two orbits under the action of $\varphi$. Thus, the irreducible curve $G_{1}$ has exactly two nodal singularities at the points $[0,0]$ and $\left[\frac{1}{2}, \frac{1}{2}\right]$. Similarly, $G_{2}$ has exactly two nodal singularities at the points $\left[\frac{1+i}{2}, 0\right]$ and $\left[\frac{1}{2}, \frac{1}{2}\right]$. Finally, the intersection points of the smooth curves $H_{1}, H_{2}$ are easily computed. \(\square\)

In conclusion, the curves $\left\{G_{j}\right\}_{j=1}^{2}$ and $\left\{H_{j}\right\}_{j=1}^{2}$ meet only in the following three points:
$$\left\{[0,0],\left[\frac{1+i}{2}, 0\right],\left[\frac{1}{2}, \frac{1}{2}\right]\right\} .$$
See Figure 2. Let $X$ denote the blowup of $B$ at the three points in (10), $A_{j}$ be the proper transform in $X$ of the singular elliptic curve $G_{j}$, and $B_{j}$ be the proper transform of the smooth elliptic curve $H_{j}(j=1,2)$. Note that $A_{j}$ is a smooth elliptic curve. Finally, let $\mathcal{D}$ be the divisor on $X$ determined by these four elliptic curves.

Lemma 3.4. The pair $(X, \mathcal{D})$ is the smooth toroidal compactification of a complex hyperbolic surface with four cusps and Euler number three.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/962c7a8d-1484-46fe-97bc-936aaf9e3a23-14.jpg?height=843&width=654&top_left_y=407&top_left_x=702}
\captionsetup{labelformat=empty}
\caption{Figure 2. The arrangement of curves on the bielliptic surface.}
\end{figure}
Proof. Exactly as in the proof of Lemma 3.2, we see that
$$\bar{c}_{1}^{2}(X, \mathcal{D})=9=3 \bar{c}_{2}(X, \mathcal{D})$$
with $K_{X}+\mathcal{D}$ nef and big, so the lemma follows. \(\square\)

Thus $X \backslash \mathcal{D}$ is a ball quotient with smooth toroidal compactification a $\mathbb{Z} / 2$ bielliptic surface.

\section*{Relationship with the standard bielliptic involution.}

We now briefly describe how to write the above example in terms of the standard bielliptic involution $\varphi_{1}: A \rightarrow A$ given by
$$\varphi_{1}(w, z)=\left(-w, z+\frac{1+i}{2}\right) .$$
To start, consider the automorphism
$$\begin{aligned}
\psi & : E \times E \rightarrow E \times E \\
\psi(w, z) & =\left(i w+\frac{1+3 i}{4}, z+\frac{3+i}{4}\right),
\end{aligned}$$
and observe that
$$\begin{aligned}
(\psi \circ \varphi)(w, z) & =\left(-i w+\frac{3+i}{4}, z+\frac{1+3 i}{4}\right) \\
\left(\varphi_{1} \circ \psi\right)(w, z) & =\left(-i w+\frac{3+i}{4}, z+\frac{1+3 i}{4}\right) .
\end{aligned}$$
We conclude that $\psi \circ \varphi \circ \psi^{-1}=\varphi_{1}$, and hence $\psi$ descends to a map $\psi_{1}: B \rightarrow B$.

One easily checks that:
$$\begin{array}{ll}
\psi\left(E_{1}\right)=\left(i z+\frac{1}{2}, z\right) & \psi\left(F_{1}\right)=\left(w, \frac{3+i}{4}\right) \\
\psi\left(E_{2}\right)=\left(-i z+\frac{i}{2}, z\right) & \psi\left(F_{2}\right)=\left(w, \frac{1+3 i}{4}\right) \\
\psi\left(E_{3}\right)=\left(-z+\frac{1+i}{2}, z\right) & \psi\left(F_{3}\right)=\left(\frac{1+3 i}{4}, z\right) \\
\psi\left(E_{4}\right)=(z, z) & \psi\left(F_{4}\right)=\left(\frac{3+i}{4}, z\right)
\end{array}$$
The intersections between these curves are at
$$\begin{gathered}
\left\{\left(\frac{1+i}{4}, \frac{1+i}{4}\right),\left(\frac{1+3 i}{4}, \frac{1+3 i}{4}\right),\left(\frac{1+3 i}{4}, \frac{3+i}{4}\right),\left(\frac{3+i}{4}, \frac{1+3 i}{4}\right),\right. \\
\left.\left(\frac{3+i}{4}, \frac{3+i}{4}\right),\left(\frac{3+3 i}{4}, \frac{3+3 i}{4}\right)\right\} .
\end{gathered}$$
Blowing up $A$ at these points, we obtain automorphisms $Y \rightarrow Y$ and $X \rightarrow X$ that we still denote by $\psi$ and $\psi_{1}$. Then, the pair $\left(Y, \psi\left(\mathcal{D}_{0}\right)\right)$ has $\psi\left(\mathcal{D}_{0}\right)$ stable under the standard bielliptic involution $\varphi_{1}$. It follows that the pairs $\left(Y, \psi\left(\mathcal{D}_{0}\right)\right)$ and $\left(X, \psi_{1}(\mathcal{D})\right)$ then determine ball quotient compactifications biholomorphic to those arising from $\left(Y, \mathcal{D}_{0}\right)$ and $(X, \mathcal{D})$, respectively.

\section*{Relationship with Holzapfel's Abelian example.}

In Hol04, §4.6], Holzapfel constructed an Abelian ball quotient compactification based on the Gaussian integers using the Abelian surface $A$ from above. His construction uses the curves:
$$\begin{array}{ll}
E_{1}^{\prime}=(z, z) & F_{1}^{\prime}=\left(w, \frac{1}{2}\right) \\
E_{2}^{\prime}=(-z, z) & F_{2}^{\prime}=\left(w, \frac{i}{2}\right) \\
E_{3}^{\prime}=(i z, z) & F_{3}^{\prime}=\left(\frac{1}{2}, z\right) \\
E_{4}^{\prime}=(-i z, z) & F_{4}^{\prime}=\left(\frac{i}{2}, z\right)
\end{array}$$
These are visibly equivalent to the arrangement $\mathcal{D}_{0}$ under translation by $\left(\frac{1}{2}, \frac{1}{2}\right)$.

Realizing $\mathbb{Z} / 4$.

Let $A^{\prime}$ be the Abelian surface defined by the subgroup $\mathbb{Z}[1, i] \times \mathbb{Z}[4, i]$ of index 4 in $\mathbb{Z}[1, i] \times \mathbb{Z}[1, i]$. Consider the lifts to $A^{\prime}$ of the eight curves on $A$ in §3 under the natural map $A^{\prime} \rightarrow A$. This is an arrangement of fourteen elliptic curves in $A^{\prime}$

\begin{table}
\begin{tabular}[t]{|l|l|}
\hline Point $(0 \leq j \leq 3)$ & Curves through that point \\
\hline $(0, j)$ & $E_{1}^{\prime}, E_{3}^{\prime}, F_{1, j}^{\prime}, F_{3}^{\prime}$ \\
\hline ( $\frac{1}{2}, \frac{1}{2}+j$ ) & $E_{1}^{\prime}, E_{2}^{\prime}, E_{3}^{\prime}, E_{4}^{\prime}$ \\
\hline $\left(\frac{i}{2}, \frac{i}{2}+j\right)$ & $E_{1}^{\prime}, E_{2}^{\prime}, E_{3}^{\prime}, E_{4}^{\prime}$ \\
\hline $\left(\frac{1+i}{2}, \frac{1+i}{2}+j\right)$ & $E_{1}^{\prime}, E_{3}^{\prime}, F_{2, j}^{\prime}, F_{4}^{\prime}$ \\
\hline $\left(\frac{1+i}{2}, j\right)$ & $E_{2}^{\prime}, E_{4}^{\prime}, F_{1, j}^{\prime}, F_{4}^{\prime}$ \\
\hline ( $0, \frac{1+i}{2}+j$ ) & $E_{2}^{\prime}, E_{4}^{\prime}, F_{2, j}^{\prime}, F_{3}^{\prime}$ \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 1. Intersection points on the Abelian surface for the $\mathbb{Z} / 4$ bielliptic.}
\end{table}
given by the equations:
$$\begin{array}{rlr}
E_{1}^{\prime} & =(z, z) & F_{2,0}^{\prime}=\left(w, \frac{1+i}{2}\right) \\
E_{2}^{\prime} & =\left(i z+\frac{1+i}{2}, z\right) & F_{2,1}^{\prime}=\left(w, \frac{3+i}{2}\right) \\
E_{3}^{\prime} & =(-z, z) & F_{2,2}^{\prime}=\left(w, \frac{5+i}{2}\right) \\
E_{4}^{\prime} & =\left(-i z+\frac{1+i}{2}, z\right) & F_{2,3}^{\prime}=\left(w, \frac{7+i}{2}\right) \\
F_{1,0}^{\prime} & =(w, 0) & F_{3}^{\prime}=(0, z) \\
F_{1,1}^{\prime} & =(w, 1) & F_{4}^{\prime}=\left(\frac{1+i}{2}, z\right) \\
F_{1,2}^{\prime} & =(w, 2) & \\
F_{1,3}^{\prime} & =(w, 3) &
\end{array}$$
It is easy to show that these curves meet in 24 points of $A^{\prime}$. More precisely, we have intersections as in Table 1.

If $Y^{\prime}$ is the blowup of $A^{\prime}$ at these 24 points, consider the divisor $\mathcal{D}_{0}^{\prime}$ determined by the proper transforms of the above curves. One has that $\bar{c}_{1}^{2}\left(Y^{\prime}, \mathcal{D}_{0}^{\prime}\right)=3 \bar{c}_{2}\left(Y^{\prime}, \mathcal{D}_{0}^{\prime}\right)$, which then implies that $Y^{\prime} \backslash \mathcal{D}_{0}^{\prime}$ is a ball quotient with fourteen cusps.

We now consider the map $\varphi: A^{\prime} \rightarrow A^{\prime}$ of order 4 given by
$$\varphi(w, z)=\left(i w+\frac{1+i}{2}, z+1\right) .$$
One checks directly that we have
$$\begin{aligned}
\varphi\left(E_{j}^{\prime}\right)=E_{j+1}^{\prime} & \varphi\left(F_{3}^{\prime}\right)=\varphi\left(F_{4}^{\prime}\right) \\
\varphi\left(F_{k, j}^{\prime}\right)=F_{k, j+1}^{\prime} & \varphi\left(F_{4}^{\prime}\right)=\varphi\left(F_{3}^{\prime}\right)
\end{aligned}$$
with $k=1,2$ and $j$ considered mod 4. Let $\pi: A^{\prime} \rightarrow B^{\prime}$ be the bielliptic quotient of $A^{\prime}$ associated with this $\mathbb{Z} / 4$ action, and define
$$\begin{array}{ll}
G_{1}=\pi\left(E_{j}^{\prime}\right) & G_{2}=\pi\left(F_{1, j}^{\prime}\right) \\
G_{3}=\pi\left(F_{2, j}^{\prime}\right) & G_{4}=\pi\left(F_{3}^{\prime}\right)=\pi\left(F_{4}^{\prime}\right) .
\end{array}$$
Observe that $G_{1}$ is singular elliptic curve with 4 nodal singularities and 2 singular points of degree four. On the other hand, the elliptic curves $G_{2}, G_{3}, G_{4}$ are smooth.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/962c7a8d-1484-46fe-97bc-936aaf9e3a23-17.jpg?height=823&width=1146&top_left_y=434&top_left_x=393}
\captionsetup{labelformat=empty}
\caption{Figure 3. The curves $G_{i}$ on the $\mathbb{Z} / 4$ bielliptic surface $B^{\prime}$.}
\end{figure}

See Figure 3 for the arrangement of curves and their intersection points. Now, let $X$ be the blowup of $B^{\prime}$ at the 6 points
$$\left\{[0,0],\left[\frac{1}{2}, \frac{1}{2}\right],\left[\frac{i}{2}, \frac{i}{2}\right],\left[\frac{1+i}{2}, 0\right],\left[0, \frac{1+i}{2}\right],\left[\frac{1+i}{2}, \frac{1+i}{2}\right]\right\}$$
and let $\left\{D_{j}\right\}_{j=1}^{4}$ be the proper transforms of the curves $\left\{G_{j}\right\}_{j=1}^{4}$. One easily computes
$$D_{1}^{2}=-16, D_{2}^{2}=-2, D_{3}^{2}=-2, D_{4}^{2}=-4 .$$
Thus, let $\mathcal{D}$ be the union of these four elliptic curves. Given the pair $(X, \mathcal{D})$, it is immediate to verify that $\bar{c}_{1}^{2}(X, \mathcal{D})=3 \bar{c}_{2}(X, \mathcal{D})$. Thus $X \backslash \mathcal{D}$ is a ball quotient with compactification that is by construction birational to a $\mathbb{Z} / 4$ bielliptic surface.

We briefly note that one can relate $\varphi$ to the standard action by translation on the first factor by $\frac{1+i}{2}$. Also, notice that this example is commensurable with the $\mathbb{Z} / 2$ example constructed above.

\section*{The proof of Theorem 1.4.}

Above we constructed examples associated with $\mathbb{Z} / 2$ and $\mathbb{Z} / 4$. It remains to consider $(\mathbb{Z} / 2)^{2}$ and $\mathbb{Z} / 4 \times \mathbb{Z} / 2$. We claim that any $\mathbb{Z} / 4$ bielliptic surface admits a finite étale cover by a bielliptic surface of type $\mathbb{Z} / 4 \times \mathbb{Z} / 2$ or $(\mathbb{Z} / 2)^{2}$. It follows immediately that one can find coverings of the above $\mathbb{Z} / 4$ ball quotient whose compactifications are bielliptic surfaces associated with the remaining two groups; see [DS16, Lem. 1.3]. We leave it to the motivated reader to work out these arrangements in coordinates.

To prove the claim, the fundamental group of any $\mathbb{Z} / 4$ bielliptic surface is isomorphic to the group of affine transformations of $\mathbb{C}^{2}$ generated by:
$$\begin{array}{lll}
a(w, z)=(w+1, z) & & b(w, z)=(w+i, z) \\
c(w, z)=(w, z+1) & & d(w, z)=(w, z+i) \\
& e(w, z)=\left(i w, z+\frac{1}{4}\right) &
\end{array}$$
This has abstract presentation
$$\begin{aligned}
G=\langle a, b, c, d, e| & {[a, b],[a, c],[a, d],[b, c],[b, d],[c, d] } \\
& \left.e a e^{-1}=b, e b e^{-1}=a^{-1},[e, c],[e, d], e^{4}=c\right\rangle .
\end{aligned}$$
One can easily connect this presentation to the $\mathbb{Z} / 4$-action on the Abelian surface associated with $\langle a, b, c, d\rangle$ via the exact sequence
$$1 \rightarrow\langle a, b, c, d\rangle \rightarrow G \rightarrow \mathbb{Z} / 4 \rightarrow 1$$
sending $e$ to a generator for $\mathbb{Z} / 4$. Note that the given bielliptic surface may not be biholomorphic to the quotient of $\mathbb{C}^{2}$ by this particular action, but all $\mathbb{Z} / 4$ bielliptic surfaces have isomorphic fundamental groups.

First, consider the subgroup $H$ of $G$ generated by $b a^{-1}, a^{-1} b^{-1}, c, d a^{-1}$, and $e$. This is clearly index two in $G$, and we claim that it determines a $\mathbb{Z} / 4 \times \mathbb{Z} / 2$ bielliptic. One can compute directly from the action on the abelian surface that a $\mathbb{Z} / 4 \times \mathbb{Z} / 2$ bielliptic has abstract fundamental group
$$\begin{aligned}
H^{\prime}=\langle x, y, u, v, r, s| & {[x, y],[x, u],[x, v],[y, u],[y, v],[u, v] } \\
& r x r^{-1}=y, r y r^{-1}=x^{-1},[r, u],[r, v], r^{4}=u \\
& {\left.[s, x],[s, y],[s, u],[s, v], r s r^{-1}=s x^{-1}, s^{2}=x y v\right\rangle . }
\end{aligned}$$
In order to derive this presentation, one can simply look at the $\mathbb{Z} / 4 \times \mathbb{Z} / 2$ bielliptic generated by the commuting automorphisms
$$r(w, z)=\left(i w, z+\frac{1}{4}\right), \quad s(w, z)=\left(w+\frac{1+i}{2}, z+\frac{i}{2}\right)$$
acting on the abelian surface $\mathbb{C}^{2} /(\mathbb{Z}[i] \times \mathbb{Z}[i])$ with coordinates $(w, z)$. This fits into an exact sequence
$$1 \rightarrow\langle x, y, u, v\rangle \rightarrow H^{\prime} \rightarrow \mathbb{Z} / 4 \times \mathbb{Z} / 2 \rightarrow 1,$$
sending $r$ to a generator for $\mathbb{Z} / 4$ and $s$ to a generator for $\mathbb{Z} / 2$. One can then identify $H^{\prime}$ with $H$ by:
$$\begin{aligned}
\langle x, y, u, v\rangle & \rightarrow\left\langle b a^{-1}, a^{-1} b^{-1}, c, d^{2}\right\rangle \\
r & \rightarrow e \\
s & \rightarrow d a^{-1}
\end{aligned}$$
This gives a $\mathbb{Z} / 4 \times \mathbb{Z} / 2$ bielliptic as a two-fold étale cover of a $\mathbb{Z} / 4$ bielliptic.
It is then easy to see that the subgroup of $H$ generated by $b a^{-1}, a^{-1} b^{-1}, c, d a^{-1}$, and $e^{2}$ has index two in $H$ and determines a two-fold étale covering of a $\mathbb{Z} / 4 \times \mathbb{Z} / 2$
bielliptic by a $(\mathbb{Z} / 2)^{2}$ bielliptic. We leave the details to the reader. This completes the proof of the claim, and hence the theorem. \(\square\)

\section*{Appendix: A ball quotient compactification with $q=0$.}

In this section, using the computer algebra software Magma Mag , we indicate that there exists a smooth toroidal compactification of a ball quotient with irregularity $q=0$. ${ }^{1}$ This shows that the previous belief that such an example cannot exist is incorrect, motivating further study of ball quotient compactifications of irregularity zero. In particular, it remains an interesting question whether a rational, K3, or Enriques surface could possibly be a ball quotient compactification.

Our group is a subgroup of the Picard modular group associated with the ring $\mathbb{Z}[i]$ of Gaussian integers. A presentation for this lattice, determined by Falbel, Francsics, and Parker [FFP] is
$$\Gamma=\left\langle i, q, t \mid i^{2}, q^{2},(i q)^{3},(i t)^{12},(i q t)^{8},\left[(i t)^{3}, t\right],[q, t]\right\rangle .$$
The associated ball quotient orbifold has Euler number 1/32 [FFP, §8.3]. Consider finite group
$$\begin{aligned}
F=\langle\alpha, \beta, \gamma| & \alpha^{2}, \beta^{2}, \gamma^{4},[\beta, \gamma],(\alpha \beta)^{3},[\alpha, \gamma]^{3},(\alpha \beta \gamma)^{8}, \\
& \left.\gamma^{-2} \beta \alpha \gamma^{-1} \beta \gamma^{-1} \alpha \gamma^{-2} \beta \alpha, \alpha \gamma \beta \gamma^{2} \beta \gamma \alpha \gamma^{4},\left(\alpha \gamma^{-1}\right)^{3}(\alpha \gamma)^{3}\right\rangle
\end{aligned}$$
of order 1536. Up to automorphisms of $F$ there is a unique homomorphism
$$\rho: \Gamma \rightarrow F .$$
Let $\Delta$ be the kernel of $\rho$. Magma shows $\Delta$ has finite abelianization $(\mathbb{Z} / 2)^{9} \times(\mathbb{Z} / 4)^{6}$. A presentation for $\Delta$ has 15 generators and 149 relations, which we omit.

Using [FFP, §8.3], one can explicitly determine the conjugacy classes of finite-order elements in $\Gamma$. Since $\Delta$ is normal in $\Gamma$, one can then check directly with Magma that $\Delta$ is torsion-free by verifying that $\Delta$ contains none of these representatives. Therefore, $\Delta$ is the fundamental group of a smooth noncompact ball quotient of Euler number $1536 / 32=48$.

To show that $\mathbb{B}^{2} / \Delta$ admits a smooth toroidal compactification, it suffices to show that all parabolic elements in $\Delta$ are rotation-free. The orbifold $\mathbb{B}^{2} / \Gamma$ has a unique cusp, hence a unique conjugacy class of parabolic subgroups. A representative $B$ for this group is described in [FFP, §8.2], which includes both an abstract presentation for $B$ and its generators as words in the generators for $\Gamma$.

Consider the quotient homomorphism
$$\rho: \Gamma \rightarrow F=\Gamma / \Delta .$$
Since $\mathbb{B}^{2} / \Delta$ is a Galois orbifold cover of $\mathbb{B}^{2} / \Gamma$ with group $F$, we see that $\mathbb{B}^{2} / \Gamma$ has $[F: \rho(B)]=24$ cusps, which all have fundamental group isomorphic to the subgroup $\operatorname{ker}\left(\left.\rho\right|_{B}\right)$ of $B$. Using the above abstract presentation for $B$ and knowing $\rho(r), \rho(q)$, and $\rho(t)$, Magma can compute that the kernel has presentation
$$\left\langle\delta_{1}, \delta_{2}, \delta_{3} \mid\left[\delta_{1}, \delta_{2}\right] \delta_{3}^{-4}\right\rangle .$$

\footnotetext{
${ }^{1}$ Code is available on the authors' webpages.
}

As in Hol98, Prop. 4.2.12], this shows that each cusp admits a smooth compactification by a smooth elliptic curve of self-intersection -4.

Let $X$ be the smooth toroidal compactification of $\mathbb{B}^{2} / \Delta$. Since $\Delta$ has finite abelianization, it follows that $q(X)=0$ (e.g., see [DS17]). Let $D$ be the compactifying divisor, so $X \backslash D=\mathbb{B}^{2} / \Delta$. Then, from $\bar{c}_{1}^{2}=3 \bar{c}_{2}$, we see that
$$K_{X}^{2}-D^{2}=3 c_{2}(X)=144 .$$
Since $D$ consists of 24 disjoint elliptic curves of self-intersection -4, we obtain $K_{X}^{2}=48$. It is then easy to complete the following table of characteristic numbers:
$$\begin{aligned}
c_{1}^{2}(X)=c_{2}(X) & =48 \\
\chi\left(\mathcal{O}_{X}\right) & =8 \\
p_{g}(X) & =7
\end{aligned}$$
It is not hard to see from here that $X$ has minimal model of general type, but we do not know if $X$ is minimal. It would be interesting to understand this surface better.

\section*{References}
\begin{itemize}
\item[] [Ada05] C. Adams, Thrice-punctured spheres in hyperbolic 3 manifolds. Trans. Amer. Math. Soc 287 (1985), no. 2, 645-656.
\item[] [AMRT10] A. Ash, D. Mumford, M. Rapoport, Y.-S. Tai, Smooth compactifications of locally symmetric varieties. Second edition. Cambridge Mathematical Library. Cambridge University Press, Cambridge, 2010.
\item[] [BHH87] G. Barthel, F. Hirzebruch, T. Höfer, Geradenkonfigurationen und Algebraische Flächen, Aspects of Mathematics, D4. Friedr. Vieweg \& Sohn, Braunschweig, 1987.
\item[] [Bea96] A. Beauville, Complex Algebraic Surfaces, Second Edition, London Mathematical Society Students Texts, 34. Cambridge University Press, Cambridge, 1996.
\item[] [Ber00] N. Bergeron, Premier nombre de Betti et spectre du laplacian de certaines variétés hyperboliques. L'Ensegnement Math. 46 (2000), 109-137.
\item[] [DD15] G. Di Cerbo, L. F. Di Cerbo, Effective results for complex hyperbolic manifolds. J. Lond. Math. Soc. (2) 91 (2015), 89-104.
\item[] [DS16] L. F. Di Cerbo, M. Stover, Multiple realizations of varieties as ball quotient compactifications. Michigan Math. J. 65 (2016), no. 2, 441-447.
\item[] [DS17] L. F. Di Cerbo, M. Stover, Bielliptic ball quotient compactifications and lattices in PU(2, 1) with finitely generated commutator subgroup. Ann. Inst. Fourier 67 (2017), no. 1, 315-328.
\item[] [DS18] L. F. Di Cerbo, M. Stover, Classification and arithmeticity of toroidal compactifications with $3 \bar{c}_{2}=\bar{c}_{1}^{2}=3$. Geom. Topol. 22 (2018), no. 4, 2465-2510.
\item[] [FFP] E. Falbel, G. Francsics, J. R. Parker, The geometry of the Gauss-Picard modular group. Math. Ann. 349 (2011), no. 2, 459-508.
\item[] [Hir84] F. Hirzebruch, Chern numbers of algebraic surfaces: an example. Math. Ann. 266 (1984), 351-356.
\item[] [Hol86] R. P. Holzapfel, Chern numbers of algebraic surfaces-Hirzebruch's examples are Picard modular surfaces. Math. Nachr., 126 (1986), 255-273.
\item[] [Hol98] R. P. Holzapfel, Ball and surface arithmetics. Aspects of Mathematics, 29. Friedr. Vieweg \& Sohn, 1998.
\item[] [Hol04] R.-P. Holzapfel, Complex hyperbolic surfaces of abelian type. Serdica Math. J. 30 (2004), no. 2-3, 207-238.
\end{itemize}
[KN96] S. Kobayashi, K. Nomizu, Foundations of differential geometry. Vol. II. Reprint of the 1969 original. Wiley Classic Library. A Wiley-Interscience Publication. John Wiley \& Sons, Inc., New York, 1996.
[Mag] W. Bosma, J. Cannon, C. Playoust, The Magma algebra system. I. The user language. J. Symbolic Comput., Computational algebra and number theory (London, 1993), 24 (1997), no. 3-4, 235-265.
[Mat02] K. Matsuki, Introduction to the Mori program. Universitext. Springer-Verlag, New York, 2002.
[Mok12] N. Mok, Projective algebraicity of minimal compactifications of complex-hyperbolic space forms of finite volume. Perspective in analysis, geometry, and topology, 331-354, Prog. Math., 296, Birkhäuser/Springer, New York, 2012.
[MVZ09] S. Müller-Stach, E. Viehweg, K. Zuo, Relative proportionality for subvarieties of moduli spaces of $K 3$ and abelian surfaces. Pure Appl. Math. Q. 5 (2009), no. 3, 1161-1199.
[Mum77] D. Mumford, Hirzebruch's Proportionality Theorem in the Non-Compact Case. Invent. Math., 42 (1977), 239-272.
[Sco78] P. Scott, Subgroups of surface groups are almost geometric. J. London Math. Soc. (2) 17 (1978), no. 3, 555-565.

Department of Mathematics, Stony Brook University, Stony Brook, NY 11794-3651
E-mail address: lucafabrizio.dicerbo@stonybrook.edu
Department of Mathematics 1805 N. Broad Street, Philadelphia, PA 10122, USA
E-mail address: mstover@temple.edu