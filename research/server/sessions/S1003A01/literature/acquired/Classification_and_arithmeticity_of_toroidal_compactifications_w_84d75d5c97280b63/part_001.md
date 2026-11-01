---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Classification and arithmeticity of toroidal
compactifications with 3c2=c12= 3]

---
source_file: 1505_01414.pdf
converter: mathpix
format: mmd
---

\title{
CLASSIFICATION AND ARITHMETICITY OF TOROIDAL COMPACTIFICATIONS WITH $3 \bar{c}_{2}=\bar{c}_{1}^{2}=3$
}

\author{
LUCA F. DI CERBO, MATTHEW STOVER
}

\begin{abstract}
We classify the minimum volume smooth complex hyperbolic surfaces that admit smooth toroidal compactifications, and we explicitly construct their compactifications. There are five such surfaces and they are all arithmetic, i.e., they are associated with quotients of the ball by an arithmetic lattice. Moreover, the associated lattices are all commensurable. The first compactification, originally discovered by Hirzebruch, is the blowup of an Abelian surface at one point. The others are bielliptic surfaces blown up at one point. The bielliptic examples are new, and are the first known examples of smooth toroidal compactifications birational to bielliptic surfaces.
\end{abstract}

Contents
\begin{itemize}
\item[1.] Introduction
1
\item[2.] Preliminaries
4
\item[3.] The case $\kappa \neq 0$
6
\item[4.] The case $\kappa=0$
9
\item[5.] The Bielliptic Case and Four More Examples
16
\item[6.] Recap of the Five Examples
34
\item[7.] Proof of Theorem 1.1
36
\end{itemize}

References
39

\section*{1. Introduction}

A classical and important problem in algebraic geometry is to classify surfaces of general type with given numerical invariants. For some aspects of this fascinating and long-standing problem we refer to the recent survey [BCP]. A situation that has attracted much recent interest is the case $c_{1}^{2}=3 c_{2}=9$, where $c_{1}^{2}$ is the self-intersection of the canonical bundle and $c_{2}$ the Euler number of the underlying surface. This problem is particularly interesting because of its connection with low-dimensional geometry. In fact, Hirzebruch proportionality, Yau's solution to the Calabi conjecture [Yau78] and the work of Miyaoka Miy77 imply that this is equivalent to classifying the minimum volume quotients of the unit ball in $\mathbb{C}^{2}$ by a
torsion-free cocompact lattice in $\operatorname{PU}(2,1)$. Most famously, this includes the classification of fake projective planes by Prasad-Yeung [PY07] and Cartwright-Steger [CS10]. Recall that Mumford constructed the first example of a fake projective plane by $p$-adic uniformization and explicitly raised the problem of classifying them [Mum79].

This paper considers the corresponding problem in the noncompact or logarithmic setting. For example, given $r, s$, one can ask for a classification of the smooth projective surfaces $X$ containing a normal crossings divisor $D$ for which the logarithmic Chern numbers satisfy
$$\bar{c}_{1}^{2}(X, D)=r \quad \bar{c}_{2}(X, D)=s,$$
where $\bar{c}_{1}^{2}(X, D)$ is the self-intersection of the log canonical divisor $K_{X}+D$ and $\bar{c}_{2}(X, D)$ is the Euler number of $X \backslash D$. We refer to [Sak80] for the foundation of the theory of logarithmic surfaces. For some more recent results see [Urz]. In this setting, $\bar{c}_{1}^{2}=3 \bar{c}_{2}$ now implies that $X \backslash D$ is a noncompact finite volume quotient of the ball by a torsion-free lattice [TY87], and $X$ is then a smooth toroidal compactification of a ball quotient. In fact, Tian-Yau derive a logarithmic Bogomolov-Miyaoka-Yau inequality for surfaces of log-general type and then characterize the pairs that attain equality as smooth toroidal compactifications of ball quotients.

In this paper, we classify all smooth toroidal compactifications with $\bar{c}_{1}^{2}=3 \bar{c}_{2}=3$. Equivalently, we classify the minimum volume complex hyperbolic surfaces that admit smooth toroidal compactifications. Our main result is the following.

Theorem 1.1. There are exactly five toroidal compactifications with $3 \bar{c}_{2}=\bar{c}_{1}^{2}=3$. One has underlying space an Abelian variety blown up at one point. The other four have underlying space a bielliptic surface blown up once. The associated lattices in $\operatorname{PU}(2,1)$ are arithmetic and commensurable.

The blown up Abelian surface in Theorem 1.1 was first studied by Hirzebruch in [Hir84], and later shown to be the compactification of a Picard modular surface by Holzapfel [Hol86]. The other four bielliptic examples are new, and are the first examples of smooth toroidal compactifications of ball quotients birational to bielliptic surfaces. All previously known examples not of general type (Hirzebruch's [Hir84] and an additional example found by Holzapfel [Hol04]) are birational to an Abelian surface. They are also the first completely explicit examples, in the sense that they are complements of a specific divisor on a given surface, not of Abelian type.

In contrast, we note that it is one of the central results in the study of toroidal compactifications that any lattice $\Gamma$ in $\operatorname{PU}(2,1)$ contains a subgroup $\Gamma^{\prime}$ of finite index such that the associated ball quotient admits a smooth toroidal compactification of general type [AMRT10, Thm. IV.1.4]. This result has been refined in [DiC12] where it is shown that, up to finite covers, all such compactifications
have ample canonical divisor. In fact, it was previously believed that any smooth toroidal compactification not of general type must be birational to an Abelian surface (see [Mo08], which unfortunately contains a critical error), and our results explicitly refute this. For applications of the existence of bielliptic smooth toroidal compactifications to problems on volumes of complex hyperbolic manifolds and group-theoretic properties of lattices in $\operatorname{PU}(2,1)$, see [DS17].

In light of the analytical results contained in [TY87], Theorem 1.1 implies the following result of interest for the geography of surfaces of log-general type.

Corollary 1.2. There are exactly five surfaces $(X, D)$ of log-general type satisfying $3 \bar{c}_{2}=\bar{c}_{1}^{2}=3$.

Theorem 1.1 has also the following corollary regarding the arithmeticity of the fundamental groups of minimum volume ball quotients. Recall that a noncompact ball quotient with finite volume admits a smooth toroidal compactification when the parabolic elements of its fundamental group have no rotational part (see §2).

Corollary 1.3. Let $\Gamma$ be a torsion-free lattice in $\operatorname{PU}(2,1)$ with minimum covolume. If the parabolic elements in $\Gamma$ have no rotational part, then $\Gamma$ is arithmetic.

This gives further evidence toward the folklore conjecture that minimum volume locally symmetric manifolds and orbifolds are arithmetic (see, e.g., [Bel14]). More precisely, Corollary 1.3 proves this conjecture for torsion-free nonuniform lattices in PU(2, 1) with rotation-free parabolic elements. In this language, Theorem 1.1 contributes to the wide literature on classification of minimal covolume lattices in semisimple Lie groups. For example, see the important very recent work of Gabai-Meyerhoff-Milley [GMM, Cor. 1.2] for the solution to the analogous problem for cusped hyperbolic 3-manifolds.

The proofs of the above results follow an algebro-geometric approach. More precisely, we fully exploit the implications of the Kodaira-Enriques classification for smooth toroidal compactifications of ball quotients with Euler number one, following a program outlined by the first author in [DiC13]. All five examples are associated with arithmetic lattices and they appear in the appendix to [Sto11], where the second author gave several examples of noncompact arithmetic ball quotients of Euler number one. We note that in [Sto11] there are three other ball quotients of Euler number one that do not admit smooth toroidal compactifications. See Section 7 for more on this.

We briefly touch upon an analogy between our work and the classification of fake projective planes [Kli03, PY07, CS10]. On the one hand, fake projective planes are the minimum volume closed complex hyperbolic 2-manifolds with first betti number zero. On the other hand, they are precisely the minimal surfaces of general type with irregularity 0 and $c_{1}^{2}=3 c_{2}=9$. The techniques used in this paper are different from
those used in the classification of fake projective planes. Crucial to the classification of fake projective planes is the proof that their fundamental groups are arithmetic [Kli03, Yeu04]. Recall that nonarithmetic lattices are known to exist by the work of Mostow and Deligne-Mostow (see [DM93]). From that point, fake projective planes are then classified by enumerating the torsion-free arithmetic lattices in $\operatorname{PU}(2,1)$ of the appropriate covolume. Our proof is of a completely different nature. We first classify the possible smooth toroidal compactifications using algebro-geometric techniques, then deduce arithmeticity from commensurability with Hirzebruch's ball quotient.

We now outline the organization of the paper. Section 2 starts with a short review of the geometry of smooth toroidal compactifications. The problem of finding the smallest toroidal compactifications is formulated in terms of logarithmic Chern numbers. In Section 3, we show that a toroidal compactification with $\bar{c}_{2}=1$ cannot have Kodaira dimension two, one, or $-\infty$. In light of the Kodaira-Enriques classification, this reduces the problem to the Kodaira dimension zero case.

In Section 4, we study the Kodaira dimension zero case in detail. It is shown that the minimal model of a toroidal compactification with $\bar{c}_{2}=1$ that is not a bielliptic surface must be the product of two elliptic curves with large automorphism group. Finally, an explicit example is constructed and its uniqueness is proved.

In Section 5, we then classify all toroidal compactifications with $\bar{c}_{2}=1$ that are birational to a bielliptic surface. There are exactly four of them. We briefly recap the constructions of the five examples in §6, and in §7 we show that they are commensurable and arithmetic.

Acknowledgments. The first author would like to thank the Mathematics Department at Notre Dame University for the nice research environment he enjoyed while carrying out most of this project. The first author was supported by the S.-S. Chern grant at ICTP. The second author was supported by the National Science Foundation under Grant Number NSF 1361000. The second author also acknowledges support from U.S. National Science Foundation grants DMS 1107452, 1107263, 1107367 "RNMS: GEometric structures And Representation varieties" (the GEAR Network). The authors also thank the referee for a very careful reading of the paper.

\section*{2. Preliminaries}

The theory of compactifications of locally symmetric varieties has been extensively studied. For example, see [BJ06]. Let $\mathcal{H}^{n}$ be $n$-dimensional complex hyperbolic space. Noncompact finite volume complex hyperbolic manifolds then correspond with conjugacy classes of torsion-free nonuniform lattices in $\operatorname{PU}(n, 1)$. Let $\Gamma$ be any such lattice. It is well-known that when the parabolic elements in $\Gamma$ have no
rotational part, the manifold $\mathcal{H}^{n} / \Gamma$ has a particularly nice compactification $(X, D)$ consisting of a smooth projective variety $X$ and boundary divisor $D$. In other words, we require the subgroup of $\mathbb{C}$ generated by the eigenvalues of parabolic elements of $\Gamma$ to be torsion-free. Under these assumptions the divisor $D$ is the union of smooth disjoint Abelian varieties, each having normal bundle of negative degree. The pair $(X, D)$ is referred as a toroidal compactification of $\mathcal{H}^{n} / \Gamma$. For more details about this construction, see [Hum98], [AMRT10], and Mok12. Note that in [Mok12] this construction is carried out without any arithmeticity assumption on $\Gamma$.

We now describe the two dimensional case in more detail. Let $\mathcal{H}^{2} / \Gamma$ be a complex hyperbolic surface with cusps that admits a smooth toroidal compactification $(X, D)$. It is known (see [Sak80] and [DiC12, §4]) that $(X, D)$ is $D$-minimal of log-general type, where $(X, D)$ is $D$-minimal if $X$ does not contain any exceptional curve $E$ of the first kind such that $D \cdot E \leq 1$. Moreover, by the Hirzebruch-Mumford proportionality principle [Mum77] we have
$$3 \bar{c}_{2}=\bar{c}_{1}^{2},$$
where $\bar{c}_{1}$ and $\bar{c}_{2}$ are the logarithmic Chern numbers of the pair $(X, D)$.
For the standard properties of logarithmic Chern classes we refer to [Kaw78]. Recall that $\bar{c}_{1}^{2}$ is equal to the self-intersection of the log-canonical divisor $K_{X}+D$, while $\bar{c}_{2}$ is simply the topological Euler characteristic of $X \backslash D$. Since $D$ consists of smooth disjoint elliptic curves, we have
$$\bar{c}_{2}(X)=\chi(X)-\chi(D)=\chi(X)=c_{2}(X) .$$
By construction, $X \backslash D$ is equipped with a complete metric with pinched negative sectional curvature. For this class of metrics it is well known that the Pfaffian of the curvature matrix is point-wise strictly positive (see [DiC12, §2]). Thus, Gromov-Harder's generalization of Gauss-Bonnet [Gro82] implies that $\bar{c}_{2}$ must be a strictly positive integer. In particular, we see that $\bar{c}_{2}=1$ is the minimum possible value, and hence the Chern-Gauss-Bonnet theorem implies that the smooth toroidal compactifications with $3 \bar{c}_{2}=\bar{c}_{1}^{2}=3$ are minimum volume complex hyperbolic 2-manifolds.

We close this section with the following fact that will be useful many times in the paper.

Theorem 2.1 (Thm. 3.18 [DiC15]). Let $(X, D)$ be a toroidal compactification of dimension $n \geq 2$. Let $q$ be the number of components of $D$. Then $q<\rho(X)$, where $\rho(X)$ is the Picard number of $X$.

In particular, the Picard number of $X$ strictly bounds the number of cusps from above. We briefly give the argument. The divisor $D$ gives $q$ disjoint elliptic curves of negative self-intersection, which, along with the class of an ample divisor, generate a subspace of dimension $q+1$ in the Néron-Severi group of $X$, and the result follows.

\section*{3. The case $\kappa \neq 0$}

In this section we show that a toroidal compactification $(X, D)$ with $\bar{c}_{2}=1$ must have Kodaira dimension $\kappa(X)$ equal to zero. Let us start by showing that $X$ cannot be of general type.

Lemma 3.1. Let $(X, D)$ be a toroidal compactification with $\bar{c}_{2}=1$. Then $X$ cannot have $\kappa(X)=2$.

Proof. Assume for a contradiction that such a pair $(X, D)$ exists. Recall that, given a surface $Y$ and $\operatorname{Bl}_{k}(Y)$ the blowup of $Y$ at $k$ points, the second Chern number of $B l_{k}(Y)$ is given by
$$c_{2}\left(B l_{k}(Y)\right)=c_{2}(Y)+k .$$
It is well known that the Euler number of a minimal surface of general type is strictly positive (see [BHPV04, Prop. VII.2.4]). Since $c_{2}(X)=1$, we conclude that $X$ must be minimal.

Next, observe that the adjunction formula implies that $K_{X} \cdot D=-D^{2}$, and so
$$\bar{c}_{1}^{2}=c_{1}^{2}-D^{2}=3 \bar{c}_{2}=3 c_{2},$$
which implies that
$$0<c_{1}^{2}<3 c_{2}$$
since $D^{2}<0$ and $c_{1}^{2}>0$ for any minimal surface of general type. We then have $c_{1}^{2} \in\{1,2\}$. However, for any complex surface we must have
$$c_{1}^{2}+c_{2} \equiv 0 \quad(\bmod 12)$$
by Noether's formula [Fri98, p. 9]. We therefore conclude that $(X, D)$ cannot have $X$ be of general type. \(\square\)

Now we rule out the case of Kodaira dimension one.
Lemma 3.2. Let $(X, D)$ be a toroidal compactification with $\bar{c}_{2}=1$. Then $X$ cannot have $\kappa(X)=1$.

Proof. Given $X$, there exists a unique minimal model $Y$ such that $c_{1}^{2}(Y)=0$ and $c_{2}(Y) \geq 0$ [BHPV04, Thm. VI.1.1]. Noether's formula then implies that
$$c_{2}(Y)=12 d$$
for some $d \in \mathbb{Z}_{\geq 0}$. It follows that a surface with $\kappa(X)=1$ must satisfy
$$c_{2}(X)=12 d+k$$
with $d, k \in \mathbb{Z}_{\geq 0}$. Therefore, if we want $c_{2}(X)=1$, we must have $d=0$ and $k=1$. In other words, $X$ is the blowup at just one point of a minimal elliptic surface $Y$ with Euler number zero.

For a minimal elliptic fibration
$$\pi: Y \longrightarrow B$$
with multiple fibers $F_{1}, \ldots, F_{k}$ of multiplicities $m_{1}, \ldots, m_{k}$ we have
$$K_{Y}=\pi^{*}\left(K_{B} \otimes L\right) \otimes \mathcal{O}_{Y}\left(\sum_{i=1}^{k}\left(m_{1}-1\right) F_{i}\right)$$
where $L=\left(R^{1} \pi_{*} \mathcal{O}_{Y}\right)^{-1}$. Note that $d=\operatorname{deg}(L)$ (see [Fri98, Cor. 16, p. 177]). In the case under consideration $c_{2}(Y)=0$, so all the singular fibers of the elliptic fibration are multiple fibers with smooth reduction [Fri98, Cor. 17, p. 177].

Now, consider
$$f: X \longrightarrow B,$$
where $f=\pi \circ B l$ and $B l: X \longrightarrow Y$ is the blowup map. We claim that some irreducible component $D_{i}$ of $D$ must map onto $B$ under $f$. If every $D_{i}$ were contained in a fiber, then there would be a general fiber of $f$ that does not meet the divisor $D$, which means that there would exist an irreducible smooth elliptic curve $E$ in $X \backslash D$. The existence of such a holomorphic curve $E$ is impossible because $X \backslash D$ is by construction hyperbolic. This proves the claim.

Since $f\left(D_{i}\right)=B$ for some $i$ and $D_{i}$ is an elliptic curve, the Hurwitz formula then implies that the genus of $B$ must be 0 or 1. Indeed, $D_{i}$ cannot be contained in a fiber of the fibration, since fibers are rational. Therefore the elliptic curve $D_{i}$ maps onto $B$, and so $B$ must have genus at most one. Equation (1) implies that if $\kappa(Y)=1$, we must assume the existence of multiple fibers. Indeed, otherwise $\kappa(Y)=-\infty$ when $g(B)=0$ and $\kappa(Y)=0$ when $g(B)=1$ (see [BHPV04, §V.12]).

Let $(Y, C)$ be the blow down configuration of $(X, D)$. We first study the case $g(B)=1$. We then have that some irreducible component $C_{i}$ of $C$ is a holomorphic $n$-section of the elliptic fibration, i.e., the map $C_{i} \rightarrow B$ is generically $n$-to-1. Moreover, $C_{i}$ is normalized by an irreducible component $D_{i}$ of $D$, which is a smooth elliptic curve. Let $Y^{\prime}$ be the fiber product $Y \times_{B} D_{i}$, so $Y^{\prime} \longrightarrow Y$ is an étale covering of degree $n$. However, $Y^{\prime}$ then has a holomorphic 1-section, which implies that $\kappa\left(Y^{\prime}\right)=0$, since there cannot be multiple fibers and all fibers are nonsingular. Then $\kappa(Y)=0$ by invariance of $\kappa$ under unramified coverings, which is a contradiction.

Now assume that $g(B)=0$. In this case $\operatorname{deg}(L)=0$, so $L$ is trivial. Again, there is a holomorphic $n$-section $C_{i}$ that is normalized by a smooth elliptic curve $D_{i}$. Following a base change argument as in the setup for the last exercise on [Fri98, p. 193], there is a finite unramified cover $\pi^{\prime}: Y^{\prime} \longrightarrow D_{i}$ of $\pi: Y \longrightarrow B$ with a holomorphic section and such that $L^{\prime}=\mathcal{O}_{D_{i}}$. We then have that $Y^{\prime}=D_{i} \times E$ for some elliptic curve $E$. By [BHPV04, Ch. VI, §1], the Kodaira dimension of $Y$ cannot be one. \(\square\)

We now show that $X$ cannot be birational to a rational or ruled surface.

Lemma 3.3. Let $(X, D)$ be a toroidal compactification with $\bar{c}_{2}=1$. Then $X$ cannot have $\kappa(X)=-\infty$.

Proof. Recall that the minimal models of surfaces with negative Kodaira dimension are $\mathbb{P}^{2}$, the Hirzebruch surfaces $X_{e}$, and ruled surfaces over Riemann surfaces of genus $g \geq 1$ [BHPV04, Ch. VI]. Since
$$c_{2}\left(\mathbb{P}^{2}\right)=3, \quad c_{2}\left(X_{e}\right)=4,$$
and $c_{2}$ only increases under blowup, a toroidal compactification with $\bar{c}_{2}=1$ must have minimal model a ruled surface with base of genus $g \geq 1$.

Then $c_{2}(X)=4(1-g)+k$, where $k$ is the number of blowup points, so $X$ must be the blowup at exactly one point of a surface $Y$ ruled over an elliptic curve. Indeed, similar to the argument in Lemma 3.2, any elliptic curve $D_{i}$ in the compactification must map onto the base, which has genus $g \geq 1$, and hence $g=1$. This fact combined with the formula for $c_{2}(X)$ given above implies that $k=1$. Therefore, $c_{2}(Y)=0$. Since the rank of the Picard group of $X$ is three, by Theorem 2.1 we have that $X$ can have at most two cusps.

Let $(Y, C)$ denote the blow down configuration of $(X, D)$, and assume that $C$ consists of exactly one irreducible component. We then have by an argument similar to the $\kappa=1$ case that $C$ must be an $n$-section of the ruling of $Y$. It is easily seen that $C$ cannot be a smooth $n$-section of the ruling for any $n \geq 1$, since this implies that $X \backslash D$ contains a $\mathbb{P}^{1}$ with just one puncture, namely the exceptional fiber of the blowup, which contradicts hyperbolicity of the metric on $X \backslash D$. This argument implies that $C$ must be singular at some point $p$. In fact, since $\bar{c}_{2}(X)=1, p$ must be the unique singular point, and hence $X$ is the blowup of $Y$ at $p$.

Consider the composition of the blowdown $X \rightarrow Y$ with the map of $Y$ to the base $B$ of the ruling. Then $D$ is a smooth elliptic curve on $X$ not contained in a fiber of the map to $B$, hence $D \rightarrow B$ is a surjective map between elliptic curves. Such a map must be étale, but it factors through the map from $D$ onto the singular curve $C$. This is a contradiction.

Let us conclude by studying the case when $(X, D)$ has two cusps. In this situation $(Y, C)$ is such that $C$ consists of two irreducible components, say $C_{1}$ and $C_{2}$, intersecting in a point $p$, where $p$ is the point of $Y$ blown up to obtain $X$. Considering the exceptional divisor of the blowup, if both $C_{1}$ and $C_{2}$ were smooth multisections then we would obtain a twice-punctured $\mathbb{P}^{1}$ in $X \backslash D$, which is impossible. They are also clearly not sections of the fibration, since their proper transform to $X$ would not be an elliptic curve. It follows that at least one of $C_{1}$ and $C_{2}$ must be singular at the blowup point $p$. Moreover, the tangents lines of $C_{1}$ and $C_{2}$ at $p$ must be all distinct for the proper transforms to be disjoint. We can then proceed as in the one cusp case to obtain a contradiction. \(\square\)

We summarize the results of this section as a proposition.

Proposition 3.4. Let $(X, D)$ be a toroidal compactification with $\bar{c}_{2}=1$. Then the Kodaira dimension of $X$ is zero.

Of course, it remains to be seen if any such example actually exists. The next two sections completely solve this problem.
\begin{itemize}
\item[4.] The case $\kappa=0$
\end{itemize}

In light of Proposition 3.4, a toroidal compactification with $\bar{c}_{2}=1$ must be birational to a minimal surface of Kodaira dimension zero. Recall that minimal surfaces with Kodaira dimension zero are given by:
\begin{itemize}
\item[-] K3 surfaces, $c_{2}=24$;
\item[-] Enriques surfaces, $c_{2}=12$;
\item[-] Abelian surfaces, $c_{2}=0$;
\item[-] bielliptic surfaces, $c_{2}=0$;
\end{itemize}
for details see [BHPV04, Ch. VI]. Thus, let $(X, D)$ be as in Proposition 3.4. Since $\bar{c}_{2}=c_{2}=1$, we have that $X$ is the blowup an Abelian or bielliptic surface at exactly one point.

Now, let $D_{1}, \ldots, D_{k}$ be the irreducible components of the compactifying divisor $D$. Since each $D_{i}$ is a smooth elliptic curve with negative self-intersection, adjunction implies that $K_{X} \cdot D=-D_{i}^{2}$, so we have
$$\bar{c}_{1}^{2}(X)=\left(K_{X}+\sum_{i} D_{i}\right)^{2}=K_{X}^{2}-\sum_{i} D_{i}^{2}=-1-\sum_{i} D_{i}^{2} .$$
Then $3 \bar{c}_{2}(X)=\bar{c}_{1}^{2}(X)$, which implies
$$-D_{1}^{2}-\cdots-D_{k}^{2}=4 .$$
Therefore, we have the following finite list of configurations:
\begin{itemize}
\item[-] 1 cusp, $D_{1}^{2}=-4$;
\item[-] 2 cusps, $D_{1}^{2}=-1, D_{2}^{2}=-3$ or $D_{1}^{2}=-2, D_{2}^{2}=-2$;
\item[-] 3 cusps, $D_{1}^{2}=-1, D_{2}^{2}=-1, D_{3}^{2}=-2$;
\item[-] 4 cusps, $D_{1}^{2}=D_{2}^{2}=D_{3}^{2}=D_{4}^{2}=-1$.
\end{itemize}

Let ( $Y, C$ ) denote the blow down configuration of ( $X, D$ ). Since $Y$ is an Abelian or bielliptic surface, $K_{Y}=0$. Thus, if $C_{i}$ is an irreducible component of $C$ in $Y$, adjunction implies that the arithmetic genus $p_{a}$ of $C_{i}$ satisfies
$$p_{a}\left(C_{i}\right)=1+\frac{C_{i}^{2}}{2},$$
see for example [Fri98, p. 13]. Note that $C_{i}^{2} \geq-2$ and it is even. If $C_{i}^{2}=-2$, then $C_{i}$ is a smooth rational curve, which is impossible since $Y$ has universal cover $\mathbb{C}^{2}$. If $C_{i}^{2}=0$, with $C_{i}$ nonsmooth, then the genus-degree formula implies that $C_{i}$ is a rational curve with a single node or a cusp. This is again impossible, since in both of these cases $C_{i}$ is normalized by $\mathbb{P}^{1}$. In conclusion, either $C_{i}$ is a smooth elliptic
curve with trivial self-intersection, or $C_{i}$ has a singular point $p$ and $C_{i}^{2}=2 n$ for some $n \geq 1$.

We study the singular case first. Let
$$\pi: X \longrightarrow Y$$
be the blowup map at $p$. We then have
$$\pi^{*} C_{i}=D_{i}+r E$$
where $D_{i}$ is the proper transform of $C_{i}$ in $X, E$ is the exceptional divisor, and $r$ is the multiplicity of the singular point $p$. Moreover, we have $D_{i} \cdot E=r, D_{i}^{2}=C_{i}^{2}-r^{2}$ and
$$2 p_{a}\left(D_{i}\right)-2=2 p_{a}\left(C_{i}\right)-2-r(r-1) .$$
If we want $D_{i}^{2} \leq-1$ with $C_{i}$ not smooth, we must have
$$D_{i}^{2}=2 n-r^{2} \leq-1 .$$

Since $D_{i}$ is a smooth elliptic curve, Equation (2) simplifies to the quadratic equation
$$r^{2}-r-2 n=0,$$
whose solutions are given by
$$r_{1,2}=\frac{1 \pm \sqrt{1+8 n}}{2} .$$
Since $r$ is a positive integer, we only need to consider the positive square root case in the above formula. Therefore, the self-intersection of $D_{i}$ is given by
$$2 n-\left(\frac{1+\sqrt{1+8 n}}{2}\right)^{2},$$
for $n \geq 1$. This self-intersection is easily seen to be decreasing in $n$ and less than -4 for $n \geq 7$. All the possibilities for $1 \leq n \leq 6$ are then given by the following list:
$$\begin{array}{lll}
n=1, & C_{i}^{2}=2, & r=2 ; \\
n=3, & C_{i}^{2}=6, & r=3 ; \\
n=6, & C_{i}^{2}=12, & r=4 .
\end{array}$$

In conclusion, we must understand whether or not an Abelian or bielliptic surface can support a curve with only one singular point of order $r$ and self-intersection as in (3).
4.1. The Abelian Case and the First Example. We now study the case when $Y$ is an Abelian surface in detail. First, observe that the line bundle associated with a curve as in (3) must be ample.

Lemma 4.1. Let $C$ be an irreducible divisor on an Abelian surface $Y$ such that $C^{2}>0$. Then $L=\mathcal{O}_{Y}(C)$ is ample.

Proof. For any curve $E$ on $Y$, we would like to show that $C \cdot E>0$. Since $C^{2}>0$, we need to study curves $E \neq C$. For these curves we clearly have $C \cdot E \geq 0$. Assume then that $C \cdot E=0$. Let $t_{y}(E)$ denote the translate of $E$ by an element $y \in Y$. Choosing $y \in Y$ appropriately, we can assume that $t_{y}(E) \cap C \neq\{0\}$. Since the curve $t_{y}(E)$ is numerically equivalent to $E$, we obtain a contradiction. We therefore conclude that $L$ is a strictly nef line bundle with positive self-intersection. The lemma is now a consequence of Nakai's criterion for ampleness of divisors on surfaces [BHPV04, Cor. 6.4, p. 161]. \(\square\)

Next, we show that curves as in (3) cannot exist on an Abelian surface. The proof of this fact uses standard properties of theta functions. Recall that any effective divisor on a complex torus is the divisor of a theta function [Deb99, Th. 3.1]. Let $C$ be a reduced divisor as in Lemma 4.1. Then, if we let $V=\mathbb{C}^{2}$ and $\pi: V \longrightarrow V / \Gamma$ be the universal covering map, we have that
$$\pi^{*} C=(\theta)$$
for some theta function $\theta$ on $V$.
More precisely, we can find a Hermitian form $H$, a character $\alpha: \Gamma \longrightarrow U(1)$, and a theta function satisfying (4) and the following "normalized" functional equation
$$\theta(z+\gamma)=\alpha(\gamma) e^{\pi H(\gamma, z)+\frac{\pi}{2} H(\gamma, \gamma)} \theta(z)=e_{\gamma}(z) \theta(z)$$
for any $z \in V$ and $\gamma \in \Gamma$. Note that $e_{\gamma}$ is the factor of holomorphy for the line bundle $L=\mathcal{O}_{Y}(C)$, and we use the convention that the first variable of $H$ is the antiholomorphic variable. Then there is an identification between the space of sections of $L$ and the vector space of theta functions of type $(H, \alpha)$ on $V$.

Considering the list obtained in (3), we are interested in the case when $C$ has exactly one singular point. Thus, let $C \in|L|$ be a reduced divisor and denote by $C^{*}=C \backslash\{p\}$ the smooth part of $C$. For every $q \in C^{*}, T_{q} C$ is a well defined 1-dimensional subspace of $T_{q} Y$. Therefore, if we let $z_{1}, z_{2}$ be coordinate functions for $V$, the equation for $T_{q} C$ is given by
$$\sum_{i=1}^{2} \partial_{z_{i}} \theta(q)\left(z_{i}-q_{i}\right)=0 .$$
We can then consider a Gauss type map
$$G: C^{*} \longrightarrow \mathbb{P}^{1}$$
where
$$G(q)=\left(\partial_{z_{1}} \theta(q): \partial_{z_{2}} \theta(q)\right) .$$

We claim that since $C$ is reduced and $L$ is ample, the Gauss map cannot be constant. We proceed by contradiction. Suppose that the image of the Gauss map is the point $\left[x_{1}: x_{2}\right] \in \mathbb{P}^{1}$. If $x_{2} \neq 0$, define the derivation
$$\partial_{w}:=\partial_{z_{1}}-k \partial_{z_{2}},$$
where $k=x_{1} / x_{2}$. If $x_{2}=0$, simply consider the derivative along the second coordinate function, in other words, $\partial_{w}=\partial_{z_{2}}$. By construction, we have $\partial_{w} \theta=0$ for all $q \in C^{*}$. Since $C$ is reduced, the function
$$f=\partial_{w} \theta / \theta$$
is holomorphic on $V$ except at the singular points of $\pi^{*} C$. By the Hartogs extension theorem, we know that $f$ can be extended to a holomorphic function on $V$. First, notice that
$$\begin{aligned}
\partial_{w} \theta(z+\gamma) & =\partial_{w} e_{\gamma}(z) \theta(z)+e_{\gamma}(z) \partial_{w} \theta(z) \\
& =\pi H(\gamma, v) e_{\gamma}(z) \theta(z)+e_{\gamma}(z) \partial_{w} \theta(z),
\end{aligned}$$
where
$$v=\partial_{w}\binom{z_{1}}{z_{2}} .$$
Therefore, the functional equation (5) implies that
$$f(z+\gamma)-f(z)=\pi H(\gamma, v)$$
for any $\gamma \in \Gamma$, which further implies that
$$f(z)=\pi H(z, v)+K$$
for some constant $K$. Since $f$ is holomorphic and $H$ is antiholomorphic in $z$, we have therefore reached a contradiction. To summarize, we have shown that for any derivation $\partial_{w}$, the function $\partial_{w} \theta$ cannot be identically zero on $C^{*}$.

Now, by the functional equation given in (4), the restriction of $\partial_{w} \theta$ to $\pi^{*} C$ can be considered as a section of the line bundle $L$ restricted to $C$. Thus, the intersection number $\left(\partial_{w} \theta\right) \cdot C$ coincides with the self-intersection $C^{2}$. Now consider a derivation $\partial_{w}$ with parameter $w$ determined by a generic point in the image of the Gauss map, and suppose that the multiplicity of the singular point $p$ is $r_{p}$. The intersection number of $\left(\partial_{w} \theta\right)$ and $C$ at the singular point $p$ is then $r_{p}\left(r_{p}-1\right)$. Moreover, by construction $\partial_{w} \theta$ vanishes somewhere on $C^{*}$. We conclude that
$$C^{2} \geq r_{p}\left(r_{p}-1\right)+1 .$$

Remark 4.2. The same argument shows that, if $C$ is an irreducible curve on an Abelian surface with $C^{2}>0$ and singular points $p_{j}$ of multiplicities $r_{j}$, then $C^{2}>\sum_{j} r_{j}\left(r_{j}-1\right)$.

Next, we observe that in all of the cases given in (3), we have
$$C_{i}^{2}=r(r-1)$$
so that, using (6), we can rule out the cases of one, two, and three cusps. Indeed, these are precisely the cases for which $C$ would contain an irreducible component that is forbidden by the above discussion. We summarize this as a lemma.

Lemma 4.3. Let $(X, D)$ be a toroidal compactification with $\bar{c}_{2}=1$ and $\kappa(X)=0$. If $X$ is not birational to a bielliptic surface, then $X$ is the blowup of an Abelian surface. Moreover, $D$ consists of four disjoint smooth elliptic curves with $D_{1}^{2}=$ $D_{2}^{2}=D_{3}^{2}=D_{4}^{2}=-1$.

Thus, by Lemma 4.3, we must classify the pairs $(Y, C)$ where $Y$ is an Abelian surface and $C$ consists of four smooth elliptic curves intersecting in just one point. We will show that, up to isomorphism, there is only one such pair. This result follows from few geometric facts.

Fact 4.4. Let $Y=\mathbb{C}^{2} / \Gamma$ be an Abelian surface containing two smooth elliptic curves $C_{1}, C_{2}$ such that $C_{1} \cdot C_{2}=1$. Then $Y$ is isomorphic to the product $C_{1} \times C_{2}$.

Proof. By translating the curves $C_{1}$ and $C_{2}$, we can always assume that $C_{1} \cap C_{2}=$ $\{(0,0)\}$. The curves $C_{i}, i=1,2$, are then subgroups of $Y$. Thus, we can define the map
$$\varphi: C_{1} \times C_{2} \longrightarrow Y$$
that sends the point $(p, q) \in C_{1} \times C_{2}$ to $p-q \in Y$. The map $\varphi$ is clearly one-toone. \(\square\)

Fact 4.5. Let $Y=\mathbb{C}^{2} / \Gamma$ be an Abelian surface containing three smooth elliptic curves $C_{i}, i=1,2,3$, such that $C_{1} \cap C_{2} \cap C_{3}=\{(0,0)\}$ and such that $C_{i} \cdot C_{j}=1$ for any $i \neq j$. Then $Y$ is isomorphic to the product $C \times C$ where $C_{i}=C$ for any $i$.

Proof. By Fact 4.4, we have that $Y=C_{1} \times C_{2}$. Since $C_{3} \cdot C_{1}=1$, for $i=1,2$, we conclude that $C_{3}=C_{i}$ for $i=1,2$. The proof is complete. \(\square\)

Fact 4.6. Let $Y$ be an Abelian surface that is the product of two identical elliptic curves, say $C=\mathbb{C} / \Lambda$. Let $(w, z)$ be the natural product coordinates on $Y$. Then any smooth elliptic curve in $Y$, passing through the point ( 0,0 ), is given by an equation of the form $w=\alpha z$, with $\alpha$ such that $\alpha \Lambda \subseteq \Lambda$.

Proof. A subgroup in $\mathbb{C}^{2}$ is given by an equation of the form $w=\alpha z$. This equation descends to $Y$ precisely when $\alpha \Lambda \subseteq \Lambda$. \(\square\)

Fact 4.7. Let $C_{\alpha}$ denote the curve in $Y=C \times C$ given by the equation $w=\alpha z$ with $\alpha \Lambda \subseteq \Lambda$ and $\alpha \neq 0$. Then $C_{0} \cdot C_{\alpha}=1$ if and only if $\alpha \Lambda=\Lambda$.

Proof. The intersection $C_{0} \cap C_{\alpha}$ consists of $[\Lambda: \alpha \Lambda]$ distinct points, where $[\Lambda: \alpha \Lambda]$ denotes the index of the subgroup $\alpha \Lambda$ in $\Lambda$. \(\square\)

Let us now return to our original problem of classifying all configurations of four elliptic curves $C_{i}, i=1,2,3,4$, on an Abelian surface $Y$ such that
$$C_{1} \cap C_{2} \cap C_{3} \cap C_{4}=\{p\}$$
for a point $p \in Y$ and
$$C_{i} \cdot C_{j}=1$$
for any $i \neq j \in\{1,2,3,4\}$. Any such configuration will be referred as good configuration. By translating the $C_{i}$, we can assume the point $p$ coincides with the origin in $Y$. By Facts 4.4 and 4.5, we can assume $Y=C \times C$ with the curves $C_{1}$ and $C_{2}$ being the factors in this splitting of $Y$. Then Facts 4.6 and 4.7 imply that we must look for values of $\alpha$, say $\alpha_{1}$ and $\alpha_{2}$, such that
$$C_{3}=C_{\alpha_{1}}, \quad C_{4}=C_{\alpha_{2}} .$$

For a generic elliptic curve $C=\mathbb{C} / \Lambda$, the only values of $\alpha$ such that $\alpha \Lambda=\Lambda$ are given by $\alpha= \pm 1$. If this is the case, note that $C_{1} \cap C_{-1}$ consists of four distinct points. These points are exactly the 2-torsion points of the lattice $\Lambda$. In conclusion, for a generic elliptic curve $C$, the Abelian surface $Y=C \times C$ cannot support a good configuration.

It remains to treat the case of a nongeneric elliptic curve $C$. Recall that there are only two elliptic curves with nongeneric automorphism group [Har77, §IV.4]. These elliptic curves correspond to the lattices $\mathbb{Z}[1, i]=\mathbb{Z}+\mathbb{Z} i, \mathbb{Z}[1, \zeta]=\mathbb{Z}+\mathbb{Z} \zeta$ where $\zeta=e^{\frac{\pi i}{3}}$.

For the lattice $\mathbb{Z}[1, i]$, we have four choices of the value of $\alpha$ so that $\alpha \mathbb{Z}[1, i]=$ $\mathbb{Z}[1, i]$ :
$$\alpha=1, i, i^{2}, i^{3} .$$
It turns out that none of the possible choices involving these parameters gives a good configuration. To see this, it suffices to observe that the configuration
$$w=0, \quad z=0, \quad w=z, \quad w=i z,$$
is such that
$$C_{1} \cap C_{i}=\{(0,0), \quad(1 / 2+i / 2,1 / 2+i / 2)\} .$$
Notice that $C_{1} \cap C_{i}$ is two points precisely because $1-i \in \mathbb{Z}[i]$ has norm 2. Any other configuration is either equivalent to the one above by a self-isomorphism of $Y$, or fails to be a good configuration by completely analogous reasons in the sense that some pair of curves will intersect in at least two points because the difference between their slopes will not be a unit of $\mathbb{Z}[i]$.

For the lattice $\mathbb{Z}[1, \zeta]$, we have six choices of the value of $\alpha$ so that $\alpha \mathbb{Z}[1, \zeta]=$ $\mathbb{Z}[1, \zeta]$ :
$$\alpha=1, \zeta, \zeta^{2}, \zeta^{3}, \zeta^{4}, \zeta^{5} .$$
Observe that
$$w=0, \quad z=0, \quad w=z, \quad w=\zeta z,$$
is a good configuration. In fact, the curves $C_{1}$ and $C_{\zeta}$ intersect at the points whose $z$-values satisfy
$$(\zeta-1) z=0 \quad \bmod \mathbb{Z}[1, \zeta] .$$
Since $(\zeta-1)=\zeta^{2}$, we conclude that
$$C_{1} \cap C_{\zeta}=\{(0,0)\} .$$

We claim that this is the only good configuration (note this is implicit in Hirzebruch's work [Hir84]). First, consider the configuration given by
$$w=0, \quad z=0, \quad w=z, \quad w=\zeta^{2} z .$$
Observe that the curves $C_{1}$ and $C_{\zeta^{2}}$, not only meet at the origin, but also in other two distinct points. These points are the two distinct zeros of the Weierstrass $\wp$-function associated with the lattice $\mathbb{Z}[1, \zeta]$. More precisely, we have
$$C_{1} \cap C_{\zeta^{2}}=\left\{(0,0), \quad\left(\left(1-\zeta^{2}\right) / 3,\left(1-\zeta^{2}\right) / 3\right), \quad\left(\left(\zeta^{2}-1\right) / 3,\left(\zeta^{2}-1\right) / 3\right)\right\} .$$
As the reader can easily verify by finding an explicit self-isomorphism of the abelian surface, any other configuration can be reduced to the above two or to the configuration
$$w=0, \quad z=0, \quad w=z, \quad w=-z,$$
which we already know not to be good.
In conclusion, we have the following result, which proves the uniqueness of Hirzebruch's example among Abelian surfaces that are a smooth toroidal compactification of a ball quotient of Euler number one.

Theorem 4.8. Let $(X, D)$ be a toroidal compactification with $\bar{c}_{2}=1$ and $\kappa(X)=0$ for which $X$ is not birational to a bielliptic surface. Then $X$ is the blowup of an Abelian surface $Y=\mathbb{C}^{2} / \Gamma$ with $\Gamma=\mathbb{Z}[1, \zeta] \times \mathbb{Z}[1, \zeta]$ and $\zeta=e^{\frac{\pi i}{3}}$. Moreover, up to a self-isomorphism of $Y$ the blowdown divisor $C$ of $D$ is given by
$$w=0, \quad z=0, \quad w=z, \quad w=\zeta z,$$
where $(w, z)$ are the natural product coordinates on $Y$. In other words, $(X, D)$ is the toroidal compactification with $\bar{c}_{2}=1$ described by Hirzebruch.

\section*{5. The Bielliptic Case and Four More Examples}

Recall that a bielliptic surface is a minimal surface of Kodaira dimension zero and irregularity one. As shown at the beginning of the last century by Bagnera and de Franchis [BdF07], all such surfaces are finite quotients of products of elliptic curves. More precisely, we have the following classification theorem. For a modern treatment we refer to [Bea96, Ch. VI].

Theorem 5.1 (Bagnera-de Franchis, 1907). Let $X$ be a bielliptic surface. Then there are elliptic curves $E_{\lambda}$ and $E_{\tau}$ associated with the lattices $\mathbb{Z}[1, \lambda]$ and $\mathbb{Z}[1, \tau]$ such that $X$ is biholomorphic to $\left(E_{\lambda} \times E_{\tau}\right) / G$, where $G$ is a group of translations of $E_{\tau}$ that acts on $E_{\lambda}$ with $E_{\lambda} / G=\mathbb{P}^{1}$. Moreover, $G$ has one of the following types:
\begin{itemize}
\item[(1)] $G=\mathbb{Z} / 2 \mathbb{Z}$ acting on $E_{\lambda}$ by $x \rightarrow-x$;
\item[(2)] $G=\mathbb{Z} / 2 \mathbb{Z} \times \mathbb{Z} / 2 \mathbb{Z}$ acting on $E_{\lambda}$ by
$$x \rightarrow-x \quad \text { and } \quad x \rightarrow x+\alpha_{2},$$
where $\alpha_{2}$ is a 2-torsion point;
\item[(3)] $G=\mathbb{Z} / 4 \mathbb{Z}$ acting on $E_{\lambda}$ by $x \rightarrow \lambda x$, where $\lambda=i$;
\item[(4)] $G=\mathbb{Z} / 4 \mathbb{Z} \times \mathbb{Z} / 2 \mathbb{Z}$ acting on $E_{\lambda}$ by
$$x \rightarrow \lambda x \quad \text { and } \quad x \rightarrow x+\frac{1+\lambda}{2},$$
where $\lambda=i$;
\item[(5)] $G=\mathbb{Z} / 3 \mathbb{Z}$ acting on $E_{\lambda}$ by $x \rightarrow \lambda x$, where $\lambda=e^{\frac{2 \pi i}{3}}$;
\item[(6)] $G=\mathbb{Z} / 3 \mathbb{Z} \times \mathbb{Z} / 3 \mathbb{Z}$ acting on $E_{\lambda}$ by
$$x \rightarrow \lambda x \quad \text { and } \quad x \rightarrow x+\frac{1-\lambda}{3},$$
where $\lambda=e^{\frac{2 \pi i}{3}}$;
\item[(7)] $G=\mathbb{Z} / 6 \mathbb{Z}$ acting on $E_{\lambda}$ by $x \rightarrow \zeta x$, where $\lambda=e^{\frac{2 \pi i}{3}}$ and $\zeta=e^{\frac{\pi i}{3}}$.
\end{itemize}

Note that the action of $G$ on $Y=E_{\lambda} \times E_{\tau}$ is clearly free, since $G$ acts on $E_{\tau}$ by translations, so the map $Y \rightarrow X$ is an étale cover. We now address the existence and uniqueness of toroidal compactifications of Euler number one that are birational to a bielliptic surface. First, observe that if such examples exist then they must be the blowup at just one point of a bielliptic surface by arguments in §4. Second, we have the following.

Lemma 5.2. Suppose that $X$ is the blowup of a bielliptic surface at exactly one point, and that $(X, D)$ is a smooth toroidal compactification of a complex hyperbolic manifold $M=X \backslash D$. Then $M$ has either one or two cusps.

Proof. From §4. $M$ has between one and four cusps. Since the Picard number of a bielliptic surface is two, the Picard number of the blowup is then three. Since the rank of the Picard group of $X$ is three, by Theorem 2.1 we have that $X$ can at most have two cusps. \(\square\)

The problem is then reduced to the study of the existence of certain singular elliptic curves $C_{i}$ as in Equation (3) on a bielliptic surface. Regarding these possibilities, let us observe the following, which will allow us to make further reductions.

Lemma 5.3. Let $Y$ be bielliptic and $\pi: E_{\lambda} \times E_{\tau} \rightarrow Y$ be the associated étale cover as in Theorem 5.1. Suppose that $C_{i}$ is a curve from Equation (3) with a unique regular singular point of order $r \geq 2$. Then $\pi^{-1}\left(C_{i}\right)$ is the union of distinct smooth elliptic curves, and exactly $r$ of them pass through each lift of the singular point of $C_{i}$. In fact, $\pi^{-1}\left(C_{i}\right)$ contains exactly $r$ distinct irreducible components, and the stabilizer $G_{C_{i}^{\prime}}$ of any irreducible component of $\pi^{-1}\left(C_{i}\right)$ has order $d / r$, where $d$ is the degree of $\pi$. In particular, $r$ divides $d$.

Proof. Let $d=|G|$ be the degree of $\pi$. Then there are exactly $d$ points on $E_{\lambda} \times E_{\tau}$ above the singular point $p$ of $C_{i}$. Consider an irreducible component $C_{i}^{\prime}$ of $\pi^{-1}\left(C_{i}\right)$. Then Remark 4.2 implies that $C_{i}^{\prime}$ cannot be singular. Since $C_{i}$ is normalized by an elliptic curve, we see that $C_{i}^{\prime}$ must be a smooth elliptic curve, hence $C_{i}^{\prime}$ is an étale cover of the normalization of $C_{i}$.

Smoothness of each $C_{i}^{\prime}$ implies there are exactly $r$ irreducible components of $\pi^{-1}\left(C_{i}\right)$ passing through any given point in $\pi^{-1}(p)$. To obtain a singularity of order exactly $r$ in the quotient, we see that the $G$-action on $E_{\lambda} \times E_{\tau}$ must identify exactly $r$ distinct smooth curves in each connected component of $\pi^{-1}\left(C_{i}\right)$. Thus, to prove the lemma, it suffices to show that $\pi^{-1}\left(C_{i}\right)$ is connected.

Since $C_{i}$ is an irreducible curve on $Y$ of positive self-intersection, it follows that $\pi^{-1}\left(C_{i}\right)$ has positive self-intersection. In fact, our assumption that $C_{i}$ has positive self-intersection, along with the fact that $\pi$ is étale, implies that $\pi^{-1}\left(C_{i}\right)$ is reduced and intersects each irreducible component $C_{i}^{\prime}$ positively. Then one sees exactly as in the proof of Lemma 4.1 that Nakai's criterion implies that $\pi^{-1}\left(C_{i}\right)$ is a reduced ample divisor. It follows that the support of $\pi^{-1}\left(C_{i}\right)$ must be topologically connected by Zariski's main theorem (e.g., applying [Har77, Cor. III.11.3] to the linear system determined by the ample divisor), which proves the lemma. \(\square\)

Now, we use the structure of the group $\operatorname{Num}(Y)$ of divisors modulo numerical equivalence to restrict the possible number of cusps even further. Let $Y$ be a bielliptic surface with associated group
$$G=\mathbb{Z} / s \mathbb{Z} \times \mathbb{Z} / t \mathbb{Z}$$
with $s \geq 2$ and $t \geq 1$. Set $d=|G|=s t$. Recall from [Ser90] that $\operatorname{Num}(Y)$ has a $\mathbb{Z}$-basis consisting of $\frac{1}{s} A$ and $\frac{1}{t} B$, where $A$ and $B$ are the general fibers of the two fibrations of $Y$ associated with the coordinate projections of the Abelian variety from Theorem 5.1. Note that one projection is onto $E_{\lambda} / G=\mathbb{P}^{1}$. Projection onto the elliptic curve $E_{\tau} / G$ is the Albanese fibration of $Y$ (see Bea96, Ch. V, VIII]).

Lemma 5.4. The case $C_{1}^{2}=C_{2}^{2}=2$ associated with $D_{1}^{2}=D_{2}^{2}=-2$ on a twocusped manifold cannot occur.

Proof. From the list given in Equation (3), we must have two curves $C_{1}$ and $C_{2}$ with self-intersection two, each with a singular point of order two. Since $C_{1}$ and $C_{2}$ only intersect at the singular point, which has order two on each, $C_{1} \cdot C_{2}=4$. Up to numerical equivalence, any curve $C_{i}$ in $Y$ can be written as $C_{i}=\frac{k_{1}}{s} A+\frac{k_{2}}{t} B$ with $k_{1}, k_{2} \in \mathbb{Z}$, and then
$$C_{i}^{2}=2 \frac{k_{1} k_{2}}{s t} A \cdot B=2 k_{1} k_{2} .$$
For $C_{i}^{2}=2$, the only possibility is then $k_{1}=k_{2}= \pm 1$, the negative case being excluded by $C_{i} \cdot A \geq 0$. Therefore, we must have
$$C_{1}=C_{2}=\frac{1}{s} A+\frac{1}{t} B$$
in $\operatorname{Num}(Y)$. Then $C_{1} \cdot C_{2}=2 \neq 4$, which is a contradiction. \(\square\)

Lemma 5.5. The case $C_{1}^{2}=0, C_{2}^{2}=6$ associated with $D_{1}^{2}=-1$ and $D_{2}^{2}=-3$ on a two-cusped manifold cannot occur unless 3 divides $|G|$.

Proof. In this case the curve $C_{2}$ has a regular singular point of order three. By Lemma 5.3, $\pi^{-1}\left(C_{2}\right)$ is the union of exactly $3 k$ smooth irreducible elliptic curves for some $k \geq 1$. Since $G$ must act transitively on these curves, the lemma follows. \(\square\)

Lemma 5.6. The case $C_{1}^{2}=12$ associated with $D_{1}^{2}=-4$ on a one-cusped manifold cannot occur unless $|G|$ is divisible by 4.

Proof. In this case the curve $C_{1}$ has a regular singular point of order four. The lemma follows exactly as Lemma 5.5. \(\square\)

This covers all three possible cases with one or two cusps. We now have two more lemmas that we prove useful.

Lemma 5.7. Let $Y$ be a bielliptic surface with associated group $G$, and let $C_{1}$ be a curve with a singular point $p$ of order $r$. Suppose that $\left(X, D_{1}\right)$ is a smooth toroidal compactification, where $X$ is the blowup of $Y$ at $p$ and $D_{1}$ is the proper transform of $C_{1}$. Choose generators $\frac{1}{s} A$ and $\frac{1}{t} B$ for $\operatorname{Num}(Y)$ as above. Given $\frac{k_{1}}{s} A+\frac{k_{2}}{t} B \in N u m(Y)$ representing the numerical class of a curve $C_{1}$ with a singular point $p$ of order $r$, we must have $k_{1}>\frac{r s}{|G|}$ and $k_{2}>\frac{r t}{|G|}$.

Proof. We have $A \cdot B=|G|$. Recall that $B$ is numerically equivalent to a general fiber of the Albanese map. Then, considering a fiber of the Albanese map through $p$,
$$C_{1} \cdot B=\frac{k_{1}|G|}{s} \geq r,$$
where $r$ is the order of the singular point.

Now consider the case of equality. There must be a smooth fiber $B_{0}$ (i.e., not a multiple fiber) of the Albanese map passing through $p$, and this fiber will intersect $C_{1}$ transversally with intersection number $r$, and $B_{0}$ is disjoint from $C_{1}$ away from $p$. Now, suppose that $\left(X, D_{1}\right)$ is a smooth toroidal compactification, where $X$ is the blowup of $Y$ at $p$ and $D_{1}$ is the proper transform of $C_{1}$. Then the proper transform $E_{0}$ of $B_{0}$ to $X$ is an elliptic curve disjoint from $C_{1}$ in $X$. In particular, it defines an elliptic curve on the complex hyperbolic manifold $X \backslash D$, which is a contradiction. The analogous argument for the fibration of the bielliptic surface over $\mathbb{P}^{1}$ gives the bound on $k_{2}$. \(\square\)

Now we proceed to analyze the remaining possibilities.
5.1. Initial reductions. In this section, we show that the only bielliptic surfaces whose blowup can produce a smooth toroidal compactification of Euler number one are associated with the groups $\mathbb{Z} / 3 \mathbb{Z}$ and $\mathbb{Z} / 3 \mathbb{Z} \times \mathbb{Z} / 3 \mathbb{Z}$. The first case is immediate from the above.

Corollary 5.8. No $\mathbb{Z} / 2 \mathbb{Z}$ bielliptic surface can produce a smooth toroidal compactification of Euler number one.

Proof. By Lemmas 5.4-5.6, we see that 3 or 4 divides $|G|$, which is not true. \(\square\)

We now proceed to rule out the remaining cases.
Proposition 5.9. No blowup of a $\mathbb{Z} / 4 \mathbb{Z}$ bielliptic surface leads to a smooth toroidal compactification of Euler number one.

Proof. By Lemmas 5.4-5.6, we must consider the one-cusped case. Here, the curve $C_{1}$ on $Y$ satisfies $C_{1}^{2}=12$, and has a regular singular point of order four. Write
$$C_{1}=\frac{k_{1}}{4} A+k_{2} B$$
as above. Then $C_{1}^{2}=2 k_{1} k_{2}$, so we have four possibilities:
$$\begin{array}{lll}
k_{1}=1, & k_{2}=6, & C_{1}=\frac{1}{4} A+6 B ; \\
k_{1}=2, & k_{2}=3, & C_{1}=\frac{1}{2} A+3 B ; \\
k_{1}=3, & k_{2}=2, & C_{1}=\frac{3}{4} A+2 B ; \\
k_{1}=6, & k_{2}=1, & C_{1}=\frac{3}{2} A+B .
\end{array}$$

All four cases are impossible by applying Lemma 5.7. More precisely, we apply the bound on $k_{1}$ to the first three cases and the bound on $k_{2}$ to the last case. This proves the proposition. \(\square\)

Proposition 5.10. No blowup of a $\mathbb{Z} / 6 \mathbb{Z}$ bielliptic surface defines a smooth toroidal compactification of Euler number one.

Proof. In this case, we must consider the case where there are two curves $C_{1}, C_{2}$ on $Y$ such that $C_{1}$ is a smooth elliptic curve with $C_{1}^{2}=0, C_{2}^{2}=6$, and $C_{2}$ has a regular singular point of order three. Write
$$C_{2}=\frac{k_{1}}{6} A+k_{2} B$$
with the above notation. Then, $C_{2}^{2}=2 k_{1} k_{2}$, so $C_{2}^{2}=6$ leaves us with the following possibilities:
$$\begin{array}{lll}
k_{1}=1, & k_{2}=3, & C_{2}=\frac{A}{6}+3 B \\
k_{1}=3, & k_{2}=1, & C_{2}=\frac{A}{2}+B .
\end{array}$$
The first case is impossible by Lemma 5.7.

In the second case $C_{2} \cdot B=3$. Thus, assume we can find a curve $C_{2}$ with a singular point of order three in the numerical class of $\frac{A}{2}+B$. Let $\pi: E_{\rho} \times E_{\tau} \rightarrow Y$ be the covering of degree six. Moreover, we can assume that the $\mathbb{Z} / 6 \mathbb{Z}$ action is given by the group generated by
$$\varphi(w, z)=\left(\zeta w, z+\frac{\gamma}{6}\right)$$
for some $\gamma \in \mathbb{Z}[1, \tau]$ and $\zeta=e^{\frac{\pi i}{3}}$.
Using Lemma 5.3, $\pi^{-1}\left(C_{2}\right)$ must consist of a union of smooth elliptic curves. Moreover, $\pi^{-1}\left(C_{2}\right)$ consists of three smooth elliptic curves $E_{1}, E_{2}, E_{3}$ intersecting in the six lifts of the points on $Y$ where $C_{1}$ and $C_{2}$ meet. Thus, the automorphism group $\mathbb{Z} / 6 \mathbb{Z}$ must act transitively on these elliptic curves with isotropy group $\left\{1, \varphi^{3}\right\}$. Next, observe that, since $C_{2} \cdot B=3$, we have that $E_{i} \cdot F=1$ for any $i=1,2,3$ and any fiber $F$ of the map $E_{\rho} \times E_{\tau} \rightarrow E_{\tau}$.

Therefore, for any $i=1,2,3$ we can write $E_{i}=\left\{w=\alpha_{i} z+a_{i}\right\}$ for some appropriate complex numbers $\alpha_{i}$ and $a_{i}$. We then must have $\varphi^{3} E_{1}=E_{1}$ which then implies that
$$\left(-\alpha_{1} z-a_{1}, z+\frac{\gamma}{2}\right)=\left(\alpha_{1}\left(z+\frac{\gamma}{2}\right)+a_{1}, z+\frac{\gamma}{2}\right) .$$
We then have $2 \alpha_{1} z=-\alpha_{1} \frac{\gamma}{2}-2 a_{1}$ modulo $\mathbb{Z}[1, \rho]$ for any $z \in E_{\tau}$, which is impossible unless $\alpha_{1}=a_{1}=0$. Reiterating this argument for the three elliptic curves we get that $\alpha_{i}=a_{i}=0$ for any $i=1,2,3$. This is impossible. \(\square\)

Proposition 5.11. No $\mathbb{Z} / 2 \mathbb{Z} \times \mathbb{Z} / 2 \mathbb{Z}$ bielliptic surface can determine a smooth toroidal compactification of Euler number one.

Proof. By Lemmas 5.4-5.6, it suffices to consider the one cusp case, where
$$C_{1}=\frac{k_{1}}{2} A+\frac{k_{2}}{2} B,$$
$C_{1}^{2}=12$, and $C_{1}$ has a regular singular point of order four. We have four possibilities:
$$\begin{array}{lll}
k_{1}=1, & k_{2}=6, & C_{1}=\frac{A}{2}+3 B \\
k_{1}=2, & k_{2}=3, & C_{1}=A+\frac{3 B}{2} ; \\
k_{1}=3, & k_{2}=2, & C_{1}=\frac{3 A}{2}+B ; \\
k_{1}=6, & k_{2}=1, & C_{1}=3 A+\frac{B}{2} .
\end{array}$$
The first three cases are eliminated by Lemma 5.7. For the fourth case we argue as follows. Note that in this case $C_{1} \cdot A=2$, which is a contradiction because we assumed that $C_{1}$ has a singular point of order four. \(\square\)

Proposition 5.12. No $\mathbb{Z} / 4 \mathbb{Z} \times \mathbb{Z} / 2 \mathbb{Z}$ bielliptic surface can determine a smooth toroidal compactification of Euler number one.

Proof. By Lemmas 5.4-5.6, it suffices to consider the one cusp case, where $C_{1}^{2}=12$ and it has a regular singular point of order four. If
$$C_{1}=\frac{k_{1}}{4} A+\frac{k_{2}}{2} B$$
with $C_{1}^{2}=12$, we have four possibilities:
$$\begin{array}{lll}
k_{1}=1, & k_{2}=6, & C_{1}=\frac{A}{4}+3 B ; \\
k_{1}=2, & k_{2}=3, & C_{1}=\frac{A}{2}+\frac{3 B}{2} ; \\
k_{1}=3, & k_{2}=2, & C_{1}=\frac{3 A}{4}+B ; \\
k_{1}=6, & k_{2}=1, & C_{1}=\frac{3 A}{2}+\frac{B}{2} .
\end{array}$$
The first two cases are impossible by Lemma 5.7, as is the fourth.
For the third case, let us observe that $C_{1} \cdot B=6$ so that the curve $C_{1}$ is a 6-section of the Albanese map $\pi_{2}: Y \rightarrow E_{\tau} /(\mathbb{Z} / 4 \mathbb{Z} \times \mathbb{Z} / 2 \mathbb{Z})$. Let $\pi: E_{i} \times E_{\tau} \rightarrow Y$ be the degree eight étale cover and observe that $\pi^{-1}(B)=8 E_{i}$ (here $i$ is a square root of -1). Next, let $H_{1}, H_{2}, H_{3}, H_{4}$ denote the irreducible components of $\pi^{-1}\left(C_{1}\right)$. Since the automorphism group $\mathbb{Z} / 4 \mathbb{Z} \times \mathbb{Z} / 2 \mathbb{Z}$ acts transitively on the $H_{j}$ and trivially on the numerical class of $E_{i}$, we obtain that for any $j=1,2,3,4$ the $H_{j}$ is a $s$-section for a fixed integer $s$. This implies the contradiction $4 s=6$. \(\square\)

This leaves us with only $\mathbb{Z} / 3 \mathbb{Z}$ and $\mathbb{Z} / 3 \mathbb{Z} \times \mathbb{Z} / 3 \mathbb{Z}$. In fact, both will produce examples of smooth toroidal compactifications. We now proceed to analyze these cases and completely classify the examples they determine.
5.2. The classification in the case of $\mathbb{Z} / 3 \mathbb{Z}$ quotients. Let $Y$ be a $\mathbb{Z} / 3 \mathbb{Z}$ bielliptic quotient. By Theorem 5.1, we can find two elliptic curves $E_{\rho}$ and $E_{\tau}$, associated with the lattices $\mathbb{Z}[1, \rho]$ and $\mathbb{Z}[1, \tau]$, respectively, such that
$$Y=\left(E_{\rho} \times E_{\tau}\right) /(\mathbb{Z} / 3 \mathbb{Z}) .$$
More precisely, $\rho=e^{\frac{2 \pi i}{3}}$ while $\tau$ is arbitrary, and the $\mathbb{Z} / 3 \mathbb{Z}$ group of automorphisms of $E_{\rho} \times E_{\tau}$ is generated by the automorphism $\varphi(w, z)=\left(\rho w, z+\frac{\gamma}{3}\right)$ for some $\gamma \in \mathbb{Z}[1, \tau]$.

Consider the group $\operatorname{Num}(Y)$ of divisors on $Y$ up to numerical equivalence. Given the bielliptic quotient $\pi: E_{\rho} \times E_{\tau} \rightarrow Y$, we have two elliptic fibrations
$$\begin{aligned}
& \pi_{1}: Y \rightarrow E_{\rho} /(\mathbb{Z} / 3 \mathbb{Z})=\mathbb{P}^{1} \\
& \pi_{2}: Y \rightarrow E_{\tau} /(\mathbb{Z} / 3 \mathbb{Z})
\end{aligned}$$
with generic fibers $A$ and $B$. Recall from above that, up to numerical equivalence, we can write any curve $C \in \operatorname{Num}(Y)$ as
$$C=\frac{k_{1}}{3} A+k_{2} B,$$
for $k_{1}, k_{2} \in \mathbb{Z}$. Notice that all of the fibers of $\pi_{2}$ are smooth and reduced and that this map is none other than the Albanese map. The class $\frac{1}{3} A$ represents a multiple fiber of the map $\pi_{1}$ counted with multiplicity one. Moreover, we have $A \cdot B=3$.

By Lemmas 5.4-5.6, the only possibility is a two-cusped manifold with $D_{1}^{2}=-1$ and $D_{2}^{2}=-3$, the latter of which determines a curve $C_{2}$ on $Y$ with $C_{2}^{2}=6$. Up to numerical equivalence, we have two possibilities:
$$\begin{array}{lll}
k_{1}=1, & k_{2}=3, & C_{2}=\frac{1}{3} A+3 B ; \\
k_{1}=3, & k_{2}=1, & C_{2}=A+B .
\end{array}$$
The first case is ruled out by Lemma 5.7.

It remains to discuss the case when the curve $C_{2}$ in $Y$ is numerically equivalent to $A+B$. Notice that in this case $C_{2} \cdot A=C_{2} \cdot B=3$. Let $E_{1}, E_{2}$, and $E_{3}$ denote the three smooth elliptic curves on $E_{\rho} \times E_{\tau}$ that are the irreducible components of $\pi^{-1}\left(C_{2}\right)$. Since $C_{2} \cdot A=3$, we have a one-to-one map from $E_{i}$ to $E_{\rho}$ for each $i=1,2,3$. Next, since $C_{2} \cdot B=3$ we also have a one-to-one map from each $E_{i}$ to $E_{\tau}$. Indeed, it follows that each $E_{i}$ has intersection number one with the general fiber of each factor projection. We therefore conclude that $E_{\rho} \cong E_{\tau}$ and $Y$ is a quotient of $E_{\rho} \times E_{\rho}$ by the group of automorphisms generated by the order three automorphism
$$\varphi(w, z)=\left(\rho w, z+\frac{\gamma}{3}\right)$$
for some $\gamma \in \mathbb{Z}[1, \rho]$.

The next step is to determine the admissible values for $\gamma$. First, observe that, up to a translation in the $w$-direction, we can assume that
$$E_{1}=\left(\alpha_{1} z, z\right), \quad E_{2}=\left(\alpha_{2} z+a_{2}, z\right), \quad E_{3}=\left(\alpha_{3} z+a_{3}, z\right)$$
where the $\alpha_{i}$ 's and $a_{i}$ 's are complex numbers to be determined. In particular, the $E_{i}$ cannot be three $\varphi$-translates of a curve with second coordinate zero, since they would project to a smooth curve on the quotient. Then, up to renumbering we have
$$\varphi\left(E_{1}\right)=E_{2}, \quad \varphi\left(E_{2}\right)=E_{3}, \quad \varphi\left(E_{3}\right)=E_{1} .$$
Analytically, this means that
$$\begin{aligned}
\rho \alpha_{1} z & =\alpha_{2}\left(z+\frac{1}{3} \gamma\right)+a_{2}, \\
\rho \alpha_{2} z+\rho a_{2} & =\alpha_{3}\left(z+\frac{1}{3} \gamma\right)+a_{3}, \\
\rho \alpha_{3} z+\rho a_{3} & =\alpha_{1}\left(z+\frac{1}{3} \gamma\right),
\end{aligned}$$
(recall that our coordinates are on the Abelian surface, so in $\mathbb{C}^{2}$ our equations must be taken modulo $\mathbb{Z}[1, \rho]$ ) and we then obtain:
$$\begin{aligned}
\rho \alpha_{1}=\alpha_{2}, \quad \rho \alpha_{2}=\alpha_{3}, \quad \rho \alpha_{3}=\alpha_{1} \\
\frac{\alpha_{2}}{3} \gamma+a_{2}=0, \quad \rho a_{2}=\frac{\alpha_{3}}{3} \gamma+a_{3}, \quad \rho a_{3}=\frac{\alpha_{1}}{3} \gamma .
\end{aligned}$$
It follows immediately that $\rho^{3}=1$, i.e., that $\rho$ is a cube root of unity.
Since each $E_{i}$ is a 1-section of the map $E_{\rho} \times E_{\rho} \rightarrow E_{\rho}$ that intersects $\{w=0\}$ in exactly one point, we have that $\left\{\alpha_{1}, \alpha_{2}, \alpha_{3}\right\} \in\left\{1, \zeta, \ldots, \zeta^{5}\right\}$, where $\zeta=e^{\frac{\pi i}{3}}$ (cf. Fact 4.7). We also want these three sections to intersect in three distinct points, so $\left\{\alpha_{1}, \alpha_{2}, \alpha_{3}\right\}$ is of the form $\left\{u, u \rho, u \rho^{2}\right\}$ for some $6^{\text {th }}$ root of unity $u$ (not necessarily primitive).

Since these choices of slopes all differ by an automorphism of the Abelian surface, namely complex multiplication by $u$ on the first factor, it suffices to consider the first choice, $\alpha_{1}=1, \alpha_{2}=\rho, \alpha_{3}=\rho^{2}$. Note that complex multiplication also changes the $a_{i}$, but that is also forced by the above relationship between the $\alpha_{i}$ and $a_{i}$. Next, we want the automorphism group generated by $\varphi$ not only to act transitively on the curves $E_{i}$, but also on their intersection points
$$E_{1} \cap E_{2} \cap E_{3}=\left\{\left(z_{1}, z_{1}\right),\left(z_{2}, z_{2}\right),\left(z_{3}, z_{3}\right)\right\} .$$
This is necessary because we want the curve $C_{2}$ in $Y$ to have a unique singular point. Therefore, we have
$$z_{2}-z_{1}=\frac{\gamma}{3}, \quad z_{3}-z_{2}=\frac{\gamma}{3}, \quad z_{3}-z_{1}=2 \frac{\gamma}{3} .$$
On the other hand, we have the identities
$$z_{1}=\rho z_{1}+a_{2}, \quad z_{2}=\rho z_{2}+a_{2}, \quad z_{3}=\rho z_{3}+a_{2}$$
which imply that
$$\rho\left(z_{2}-z_{1}\right)=z_{2}-z_{1}, \quad \rho\left(z_{3}-z_{1}\right)=z_{3}-z_{1}, \quad \rho\left(z_{3}-z_{2}\right)=z_{3}-z_{2} .$$
It follows that $\frac{\gamma}{3}=\frac{(1-\rho)}{3}$ or $\frac{\gamma}{3}=2 \frac{(1-\rho)}{3}$, since $z_{2}-z_{1}$ is a nonzero point on the elliptic curve $E_{\rho}$ stable under complex multiplication by $\rho$. We will later see that each choice gives an isomorphic quotient, so we assume for now that $\frac{\gamma}{3}=\frac{(1-\rho)}{3}$.

Using this information together with the previously derived formulas, we obtain
$$a_{2}=-\frac{(1-\rho)}{3}, \quad a_{3}=-2 \frac{(1-\rho)}{3} .$$
so that
$$E_{1}=(z, z), \quad E_{2}=\left(\rho z-\frac{(1-\rho)}{3}, z\right), \quad E_{3}=\left(\rho^{2} z-2 \frac{(1-\rho)}{3}, z\right) .$$
Next, we compute that
$$E_{1} \cap E_{2} \cap E_{3}=\left\{\left(\frac{2}{3}, \frac{2}{3}\right), \quad\left(\frac{2 \rho}{3}, \frac{2 \rho}{3}\right), \quad\left(\frac{2 \rho^{2}}{3}, \frac{2 \rho^{2}}{3}\right)=\left(\frac{1+\rho}{3}, \frac{1+\rho}{3}\right)\right\} .$$
In conclusion, the curves $E_{1}, E_{2}, E_{3}$ are uniquely determined. Thus, the bielliptic surface $Y$ and the curve $C_{2}$ are also uniquely determined. We now show that $Y$ is independent of our choice of the 3-torsion point.

Lemma 5.13. The bielliptic surface $Y$ and the curve $C_{2}$ described above are independent of the choice of $\frac{1}{3} \gamma$.

Proof. The two possibilities for the $\alpha_{i}$ and $\frac{1}{3} \gamma$ are:
\begin{itemize}
\item[-] $(z, z), \quad\left(\rho z-\frac{(1-\rho)}{3}, z\right), \quad\left(\rho^{2} z-2 \frac{(1-\rho)}{3}, z\right)$
\item[-] $(z, z), \quad\left(\rho z-2 \frac{(1-\rho)}{3}, z\right), \quad\left(\rho^{2} z-\frac{(1-\rho)}{3}, z\right)$
\end{itemize}
Let $X$ and $X^{\prime}$ be the bielliptic surfaces obtained by taking the quotient of $E_{\rho} \times E_{\rho}$ by the automorphism groups generated by
$$\begin{aligned}
\varphi(w, z) & =\left(\rho w, z+\frac{(1-\rho)}{3}\right) \\
\varphi^{\prime}(w, z) & =\left(\rho w, z+2 \frac{(1-\rho)}{3}\right),
\end{aligned}$$
respectively. The first configuration must be considered in $X$, while the latter must be considered in $X^{\prime}$. The self-isomorphism of $E_{\rho} \times E_{\rho}$ given by $\phi:(w, z) \rightarrow$ $(-w,-z)$ takes the first configuration to the second and descends to an isomorphism between $X$ and $X^{\prime}$. This proves that the two choices determine the same isomorphism class of bielliptic quotient $X$ with the same singular curve $C_{2}$. \(\square\)

Next, we must find the possible elliptic curves $C_{1}$ in $Y$ intersecting $C_{2}$ in its unique singular point such that $C_{1} \cdot C_{2}=3$ (see the list given in (3)). The first and most obvious choice is to let $C_{1}$ be the unique fiber $B$ of the Albanese map passing through the singular point of $C_{2}$. Notice that since $B \cdot C_{2}=3$, the intersection is
transverse. Thus, let $C_{1}=B$ and consider the pair $(Y, C)$, where $C=B+C_{2}$, and let $X$ denote the blowup of $Y$ at the singular point $p$ of $C_{2}$. Let $D_{i}$ be the proper transform of $C_{i}$ and $D=D_{1}+D_{2}$. We then claim that the pair $(X, D)$ is a smooth toroidal compactification. Indeed, it saturates the logarithmic Bogomolov-Miyaoka-Yau inequality:
$$\bar{c}_{1}^{2}=\left(K_{X}+D\right)^{2}=K_{X}^{2}-D_{1}^{2}-D_{2}^{2}=-1+3+1=3 \bar{c}_{2} .$$

Next, we can take $C_{1}^{\prime}$ as the unique fiber of $\pi_{2}$ passing through the singular point of $C_{2}$. Notice that this is not a multiple fiber and, since $C_{2} \cdot A=3$, the intersection is transverse. Consider the pair $\left(Y, C^{\prime}\right)$, where $C^{\prime}=C_{1}^{\prime}+C_{2}$, and blow up the singular point $p$ of $C_{2}$. Let $X$ denote the blowup of $Y, D_{1}^{\prime}, D_{2}$ denote the proper transforms of $C_{1}^{\prime}$ and $C_{2}$, respectively, and set $D^{\prime}=D_{1}^{\prime}+D_{2}$. Again, it is easy to check that it saturates the logarithmic Bogomolov-Miyaoka-Yau inequality, so the pair $\left(X, D^{\prime}\right)$ is a smooth toroidal compactification.

Finally, we argue that these are the unique smooth toroidal compactifications coming from a $\mathbb{Z} / 3 \mathbb{Z}$ bielliptic surface. If $\frac{k_{1}}{3} A+k_{2} B$ is another possible choice, it is a smooth elliptic curve of self-intersection zero, so $2 k_{1} k_{2}=0$. In other words, it must be a multiple of $\frac{1}{3} A$ or $B$. This curve also must have intersection number 3 with $C_{2}$, which leaves us only with the above two choices, $C_{1}$ and $C_{1}^{\prime}$.
5.3. Discussion of the Second and Third Examples. Let $(X, D)$ and $\left(X, D^{\prime}\right)$ be the toroidal compactification found in §5.2. We want to show that those compactifications are associated with two distinct complex hyperbolic surfaces. Assume this is not the case. There exists an automorphism $\Psi: X \rightarrow X$ sending $D_{1}^{\prime}+D_{2}$ to $D_{1}+D_{2}$, since the map of complex hyperbolic surfaces takes cusps to cusps. The first claim is that we necessarily must have $\Psi\left(D_{2}\right)=D_{2}$ and $\Psi\left(D_{1}^{\prime}\right)=D_{1}$. Observe that $X$ is the blowup at a single point of a bielliptic surface. Thus, inside $X$ there is a unique rational curve that is the exceptional divisor say $E$. This implies that $\Psi(E)=E$. Now $E \cdot D_{2}=3$ while $E \cdot D_{1}=E \cdot D_{1}^{\prime}=1$. The claim then follows.

Let $Y$ denote the bielliptic surface obtained by contracting the exceptional divisor $E$. Also, let $C_{1}, C_{1}^{\prime}$, and $C_{2}$ denote the blow down transform of the curves $D_{1}, D_{1}^{\prime}$, and $C_{2}$. Next, let $\psi: Y \rightarrow Y$ denote the automorphism on $Y$ induced by $\Psi$ on $X$, which exists since $\Psi$ must preserve the exceptional curve of the blowup. Observe that $\psi\left(C_{2}\right)=C_{2}$ and $\psi\left(C_{1}^{\prime}\right)=C_{1}$.

Fact 5.14. There exists no such automorphism of $X$.
Proof. Recall that $C_{1}$ is numerically equivalent to $B$ and $C_{1}^{\prime}$ is numerically equivalent to $A$. Let $\psi_{*}: \operatorname{Num}(Y) \rightarrow \operatorname{Num}(Y)$ be the induced automorphism. Since $\psi(A)=B$, we have
$$\psi_{*}\left(\frac{1}{3} A\right)=\frac{1}{3} B \notin \operatorname{Num}(Y),$$
which is a contradiction. \(\square\)
5.4. The classification in the case of $\mathbb{Z} / 3 \mathbb{Z} \times \mathbb{Z} / 3 \mathbb{Z}$ quotients. Let $Y$ be a $\mathbb{Z} / 3 \mathbb{Z} \times \mathbb{Z} / 3 \mathbb{Z}$ bielliptic quotient. By Theorem 5.1, we can find two elliptic curves $E_{\rho}$ and $E_{\tau}$, respectively associated with the lattices $\mathbb{Z}[1, \rho]$ and $\mathbb{Z}[1, \tau]$, such that
$$Y=\left(E_{\rho} \times E_{\tau}\right) /(\mathbb{Z} / 3 \mathbb{Z} \times \mathbb{Z} / 3 \mathbb{Z}) .$$
More precisely, $\rho=e^{\frac{2 \pi i}{3}}$ while $\tau$ is arbitrary, and the $\mathbb{Z} / 3 \mathbb{Z} \times \mathbb{Z} / 3 \mathbb{Z}$ group of automorphisms of $E_{\rho} \times E_{\tau}$ is generated by the commuting order three automorphisms
$$\varphi_{1}(w, z)=\left(\rho w, z+\frac{\gamma}{3}\right), \quad \varphi_{2}(w, z)=\left(w+k \frac{(1-\rho)}{3}, z+\frac{\gamma^{\prime}}{3}\right)$$
for some $\gamma, \gamma^{\prime} \in \mathbb{Z}[1, \tau]$ and $k=1$ or 2. Consider the group $\operatorname{Num}(Y)$ of divisors on $Y$ up to numerical equivalence. If $A$ and $B$ are the generic fibers of the two elliptic fibrations $\pi_{1}: Y \rightarrow \mathbb{P}^{1}=E_{\rho} /(\mathbb{Z} / 3 \mathbb{Z})$ and $\pi_{2}: Y \rightarrow E_{\tau} /(\mathbb{Z} / 3 \mathbb{Z})$, then $\frac{1}{3} A$ and $\frac{1}{3} B$ form a basis of $\operatorname{Num}(Y)$. Therefore, up to numerical equivalence we can write any curve $C$ as $\frac{k_{1}}{3} A+\frac{k_{2}}{3} B$ for $k_{1}, k_{2} \in \mathbb{Z}$. Notice that $\pi_{2}$ is the Albanese map, and all its fibers are generic. The class $\frac{1}{3} A$ represents a multiple fiber of the map $\pi_{1}$ with multiplicity one. Finally, we have $A \cdot B=9$.

As in the $\mathbb{Z} / 3 \mathbb{Z}$ case, it suffices to consider the case where $C_{1}$ is an elliptic curve of self-intersection zero and $C_{2}^{2}=6$. Up to numerical equivalence, we can write $C_{2}=\frac{k_{1}}{3} A+\frac{k_{2}}{3} B$ where $\frac{1}{3} A$ and $\frac{1}{3} B$ are the above basis of $\operatorname{Num}(Y)$. There are two possibilities:
$$\begin{array}{lll}
k_{1}=1, & k_{2}=3, & C_{2}=\frac{1}{3} A+B \\
k_{1}=3, & k_{2}=1, & C_{2}=A+\frac{1}{3} B .
\end{array}$$

Proposition 5.15. The case $C_{2}=A+\frac{B}{3}$ cannot occur.
Proof. In this case $C_{2} \cdot A=3$ and $C_{2} \cdot B=9$. Then $\pi^{*}\left(C_{2}\right)$ is numerically equivalent to $3 E_{\rho}+9 E_{\tau}$, and Lemma 5.3 implies that it has three irreducible components, each of which is a smooth elliptic curve. Let $E_{1}, E_{2}$ and $E_{3}$ denote the three elliptic curves. We have a one-to-one map from $E_{i}$ to $E_{\rho}$ and a three-to-one map from $E_{i}$ to $E_{\tau}$ for each $i=1,2,3$.

There are two cases to consider, associated with the two isomorphism classes of degree 3 quotients of $E_{\rho}$ :
$$E_{\rho} \times E_{\rho /(1-\rho)} \quad E_{\rho} \times E_{\rho / 3},$$
where $E_{\rho /(1-\rho)}$ is the quotient of $\mathbb{C}$ by $\frac{1}{1-\rho} \mathbb{Z}[1, \rho]$ and $E_{\rho / 3}$ denotes the quotient of $\mathbb{C}$ by $\mathbb{Z}[1, \rho / 3]$. In the first case, notice that $\mathbb{Z}[3,1-\rho]=(1-\rho) \mathbb{Z}[1, \rho]$ is an index 3 subring of $\mathbb{Z}[1, \rho]$, and $E_{\rho} \simeq E_{1-\rho}=\mathbb{C} / \mathbb{Z}[3,1-\rho]$ under its self-isogeny of degree 3. In order to simplify the computation we can replace $E_{\rho}$ with $E_{1-\rho}$, and the first case becomes $E_{1-\rho} \times E_{\rho}$. We first rule out that situation.

Claim. The case $E_{1-\rho} \times E_{\rho}$ cannot occur.