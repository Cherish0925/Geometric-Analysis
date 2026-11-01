---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 1309_5516.pdf
converter: mathpix
format: mmd
---

\title{
ON THE CLASSIFICATION OF TOROIDAL COMPACTIFICATIONS WITH $3 \bar{c}_{2}=\bar{c}_{1}^{2}$ AND $\bar{c}_{2}=1$
}

\author{
LUCA FABRIZIO DI CERBO
}

\begin{abstract}
We classify the smallest finite volume complex hyperbolic surfaces with cusps which admit smooth toroidal compactifications and which are not birational to a bi-elliptic surface. Remarkably, there is only one such surface which appears to be the compactification of a Picard modular surface.
\end{abstract}

Contents
\begin{itemize}
\item[1.] Introduction
1
\item[1.1.] Preliminaries and main results
2
\item[2.] The case $\kappa \neq 0$
4
\item[3.] The case $\kappa=0$
7
\item[4.] Proof of the main theorem and conclusions
\end{itemize}

13
References
13

\section*{1. Introduction}

A fundamental problem in the theory of complex surfaces is the classification of all surfaces of general type with $3 c_{2}=c_{1}^{2}$ and smallest possible Euler number. Note that the Euler number of a surface of general type is positive and at least three. This nontrivial fact follows from the standard theory of surfaces of general type and the Bogomolov-Miyaoka-Yau inequality, for more details see for example Chapter VII in [BHPV04]. Moreover, by Yau's solution of Calabi conjecture [Yau78] any such surface is a quotient of the unit ball in $\mathbb{C}^{2}$ by a torsion free co-compact discrete subgroup of $\operatorname{PU}(2,1)$.

Thus, the problem of finding all surfaces of general type with
$$3 c_{2}=c_{1}^{2}, \quad c_{2}=3,$$
reduces to the classical and longstanding problem in geometric topology of finding all the compact complex hyperbolic surfaces with the smallest possible volume.

The first example of a surface as in 1 was given by Mumford in [Mum79]. Interestingly, the surface constructed by Mumford has vanishing first Betti number. Thus, it has the same Hodge diamond of the two dimensional complex projective space and it is then an example of a "fake projective plane". In the same paper Mumford raises the problem of enumerating all fake projective planes. This difficult problem was solved only recently by Prasad and Yeung in [PY07] with the addition of Cartwright and Steger [CS10]. Note that an important ingredient in [PY07]
and [CS10] is the fact that the fundamental groups $\Gamma \in \mathrm{PU}(2,1)$ of fake projective planes are necessarily arithmetic, see [Kli03] and [Yeu04]. Recall that nonarithmetic lattices are known to exist by the work of Mostow and Deligne-Mostow, see [DM93]. For a survey of this fascinating problem the interested reader may refer to the Bourbaki report [Rém04].

The natural question arises whether fake projective planes are the only surfaces of general type with Euler number equal to three. Surprisingly, this is not the case! In fact, Cartwright and Steger in [CS10] found an example of a surface as in 1 with first Betti number equal to two. Nevertheless, at the time of writing, there is evidence that fake projective planes and the Cartwright-Steger surface exhaust all surfaces of general type with Euler number three, see the paper of Yeung [Yeu13]. In conclusion, the classification of the smallest compact complex hyperbolic surfaces seems to be completed.

The main goal of this paper is to initiate an analogous program for cusped complex hyperbolic surfaces. More precisely, we classify the smallest finite volume complex hyperbolic surfaces with cusps which admit smooth toroidal compactifications which are not birational to a bi-elliptic surface. Remarkably, there is only one such surface and it is associated to an arithmetic lattice. The unique finite volume complex hyperbolic surfaces we find appears to be a surface first constructed by Hirzebruch in [Hir84] and later shown to be the compactification of a Picard modular surface, see [Hol86], [Sto11]. Thus, the group theoretical implications of our main classification result are obtained implicitly.

An outline of the paper follows. Section 1.1 starts with a short review of the geometry of smooth toroidal compactifications. The problem of finding the smallest toroidal compactifications is formulated in terms of logarithmic Chern numbers. More precisely, the smallest finite volume complex hyperbolic surfaces with cusps which admit smooth toroidal compactifications correspond to surfaces of logarithmic general type such that
$$3 \bar{c}_{2}=\bar{c}_{1}^{2}, \quad \bar{c}_{2}=1,$$
where by $\bar{c}_{i}, i=1,2$, we denote the logarithmic Chern numbers of the compactification. Finally, we state the main results of this paper.

In Section 2, we show that a toroidal compactification with $\bar{c}_{2}=1$ cannot be of Kodaira dimension equal to two, one or minus infinity. In light of the Kodaira-Enriques classification, we reduce the problem to the study of the case with Kodaira dimension equal to zero.

In Section 3, we study in detail the case with zero Kodaira dimension. It is shown that the minimal model of a toroidal compactification with $\bar{c}_{2}=1$, if it is not a bi-elliptic surface, then it must be must be the product of two elliptic curves with large automorphism group. Finally, an explicit example is constructed and its uniqueness is proved. Interestingly, the surface constructed already appears in a paper by Hirzebruch [Hir84].
1.1. Preliminaries and main results. The theory of compactifications of locally symmetric varieties has been extensively studied, see for example [BJ06]. Let $\mathcal{H}^{n}$
be the $n$-dimensional complex hyperbolic space. Finite volume complex hyperbolic manifolds then correspond to torsion free non-uniform lattices in $\operatorname{PU}(n, 1)$. Let then $\Gamma$ be any such lattice in $\operatorname{PU}(n, 1)$. It is well known that when the parabolic elements in $\Gamma$ have no rotational part, then the manifold $\mathcal{H}^{n} / \Gamma$ has a particularly nice compactification $(X, D)$ consisting of a smooth projective variety $X$ and an exceptional divisor $D$. More precisely, the divisor $D$ is the union of smooth disjoint Abelian varieties with negative normal bundle. The pair $(X, D)$ is referred as toroidal compactification of $\mathcal{H}^{n} / \Gamma$. For more details about this construction the interested reader may refer to [AMRT10] and Mok12. Note that in [Mok12] this construction is carried out without any arithmeticity assumption on $\Gamma$.

Let us now describe in more details the two dimensional case. Let $\mathcal{H}^{2} / \Gamma$ be a complex hyperbolic surface with cusps which admit a smooth toroidal compactification $(X, D)$. It is well known, see [Sak80] and Section 4 in [DiC12a], that $(X, D)$ is $D$-minimal of log-general type. We say that the pair ( $X, D$ ) is $D$-minimal if $X$ does not contain any exceptional curve $E$ of the first kind such that $D \cdot E \leq 1$. Moreover, by the Hirzebruch-Mumford proportionality [Mum77], we have
$$3 \bar{c}_{2}=\bar{c}_{1}^{2},$$
where $\bar{c}_{1}$ and $\bar{c}_{2}$ are the logarithmic Chern numbers of the pair $(X, D)$. For the standard properties of logarithmic Chern classes we refer to [Kaw78]. Recall that the $\bar{c}_{1}^{2}$ of the pair $(X, D)$ is equal to the self-intersection of the log-canonical divisor $K_{X}+D$, while $\bar{c}_{2}$ is simply the topological Euler characteristic of $X \backslash D$. Since $D$ consists of smooth disjoint elliptic curves, we have
$$\bar{c}_{2}(X)=\chi(X)-\chi(D)=\chi(X)=c_{2}(X) .$$
By construction $X \backslash D$ is equipped with a complete metric with pinched negative sectional curvature. For this class of metrics it is well known that the Pfaffian of the curvature matrix is pointwise strictly positive, see Section 2 in [DiC12a]. Thus, Gromov-Harder's generalization of Gauss-Bonnet [Gro82] implies that $\bar{c}_{2}$ has to be a strictly positive integer.

It is then interesting to look for toroidal compactifications with the smallest possible value for the second logarithmic Chern number, i.e., $\bar{c}_{2}=1$. Note how any such manifold will also provide an example of a cusped complex hyperbolic manifold with the smallest possible volume. The main purpose of this paper is to provide a complete classification of smooth toroidal compactifications with $3 \bar{c}_{2}=\bar{c}_{1}^{2}$ and $\bar{c}_{2}=1$ which are not birational to a bi-elliptic surface.

Theorem A. There exists a unique toroidal compactification with $3 \bar{c}_{2}=\bar{c}_{1}^{2}$ and $\bar{c}_{2}=1$ which not birational to a bi-elliptic surface.

It is interesting to notice that because of the logarithmic Bogomolov-Miyaoka-Yau inequality proved in [TY87], Theorem A provides the classification of logarithmic pairs $(X, D)$ of log-general type with $3 \bar{c}_{2}=\bar{c}_{1}^{2}$ and $\bar{c}_{2}=1$ for which $X$ is not birational to a bi-elliptic surface.

Here is an interesting corollary.

Theorem B. The lattice associated to a toroidal compactification with $3 \bar{c}_{2}=\bar{c}_{1}^{2}$ and $\bar{c}_{2}=1$ which is not birational to a bi-elliptic surfaces is arithmetic.

In other words, any torsion free lattice $\Gamma \in \operatorname{PU}(2,1)$ whose parabolic elements have no rotational part and with the smallest possible Euler characteristic must be arithmetic if the associated smooth compactification is not birational to a bielliptic surface. The proof of Theorem B is indirect. In fact, it relies on the fact that the toroidal compactification identified in Theorem A was already known to be associated to an arithmetic lattice, see [Hol86] and [Sto11]. Nevertheless, the arithmeticity result stated in Theorem B seems not to be known.

For what regards the bi-elliptic case the classification is in progress. I can currently construct an example, moreover Matthew Stover has informed me that he can construct a different example. The classification of these bi-elliptic examples will be included in the next version of this work.

Acknowledgements. I would like to thank Professor Mark Stern for his constant support and helpful discussions. Special thanks go to Gabriele Di Cerbo for countless discussions and encouragement. I also acknowledge useful discussions with Matthew Stover. Finally, I would like to thank the organizers of the conferences "Algebraic \& Hyperbolic Geometry - New Connections" and "Geometria Algebrica nella Capitale" where part of this work was carried out.

\section*{2. The case $\kappa \neq 0$}

In this section we show that a toroidal compactification with $\bar{c}_{2}=1$ must have Kodaira dimension equal to zero. Let us start by showing that $X$ cannot be of general type.

Lemma 2.1. Let $(X, D)$ be a toroidal compactification with $\bar{c}_{2}=1$. Then $X$ cannot have $\kappa(X)=2$.

Proof. Recall that, given a surface $Y$ and letting $B l_{k}(Y)$ be its blow up at $k$ points, the second Chern number of $\operatorname{Bl}_{k}(Y)$ is given by
$$c_{2}\left(B l_{k}(Y)\right)=k+c_{2}(Y) .$$
Now, it is well known that the Euler characteristic of a minimal surface of general type is strictly positive, see Chapter VII [BHPV04]. Since $c_{2}(X)=1$, we conclude that $X$ must be minimal. Next, let us observe that
$$\bar{c}_{1}^{2}=c_{1}^{2}-D^{2}=3 \bar{c}_{2}=3 c_{2}$$
so that
$$0<c_{1}^{2}<3 c_{2}$$
since $D^{2}<0$ and $c_{1}^{2}>0$ for any minimal surface of general type. We then have $c_{1}^{2} \in\{1,2\}$. But now for any complex surface we must have
$$c_{1}^{2}+c_{2}=0 \bmod$$
by Noether's formula, see page 9 in [Fri98]. We therefore conclude that $(X, D)$ cannot be such that $X$ is of general type. \(\square\)

Let us proceed by ruling out the case of Kodaira dimension one.
Lemma 2.2. Let $(X, D)$ be a toroidal compactification with $\bar{c}_{2}=1$. Then $X$ cannot have $\kappa(X)=1$.

Proof. Let us look for a moment at the minimal models of surfaces with Kodaira dimension one, for details see Chapter VI in BHPV04]. Thus given $X$, observe that there exists a unique minimal model $Y$ such that $c_{1}^{2}(Y)=0$ and $c_{2}(Y) \geq 0$. Now by Noether's formula we have
$$c_{2}(Y)=12 d$$
where $d \in \mathbb{Z}_{\geq 0}$. Since the Chern number $c_{1}^{2}+c_{2}$ is a birational invariant, we conclude that a surface with $\kappa(X)=1$ must satisfy
$$c_{2}(X)=12 d+k$$
with $d, k \in \mathbb{Z}_{\geq 0}$. Therefore, if we want $c_{2}(X)=1$, we must have $d=0$ and $k=1$. In other words, $X$ is the blow up at just one point of a minimal elliptic surface $Y$ with zero Euler number. For a minimal elliptic fibration
$$\pi: Y \longrightarrow E$$
with multiple fibers $F_{1}, \ldots, F_{k}$ of multiplicities $m_{1}, \ldots, m_{k}$ we have
$$K_{Y}=\pi^{*}\left(K_{E} \otimes L\right) \otimes \mathcal{O}_{Y}\left(\sum_{i=1}^{k}\left(m_{1}-1\right) F_{i}\right)$$
where $L=\left(R^{1} \pi_{*} \mathcal{O}_{Y}\right)^{-1}, d=\operatorname{deg}(L)$ and $c_{2}(Y)=12 d$. In the case under consideration, we have $d=0$ and then all the singular fibers of the elliptic fibration are multiple fibers with smooth reduction, see Corollary 17 page 177 in [Fri98]. Consider now
$$f: X \longrightarrow E$$
where $f=\pi \circ B l$ and $B l: X \longrightarrow Y$ is the blow up map. Let $D_{i}$ be an irreducible component of $D$. We then cannot have $f\left(D_{i}\right)=p_{i}$ for all $i$. If otherwise, there would exists a smooth elliptic curve in $X \backslash D$. We conclude that the image of at least one of the $D_{i}$ 's under the elliptic fibration is $E$. By the Hurwitz formula, the genus of $E$ must be 0 or 1 . Thus, if we want $\kappa(Y)=1$, we must assume the existence of multiple fibers. Now, denote by $(Y, C)$ the blow down configuration of $(X, D)$. Let us study the case $g(E)=1$ first. We then have that an irreducible component of $C$, say $\Sigma$, is a holomorphic $n$-section of the elliptic fibration. Moreover, $\Sigma$ is normalized by a smooth elliptic curve, say $C^{\prime}$, which is an irreducible component of $D$. Let us denote by $Y^{\prime}$ the fiber product $Y \times_{E} C^{\prime}$. Thus, $Y^{\prime} \longrightarrow Y$ is a $n$-covering map. Since $Y^{\prime}$ has a holomorphic 1-section, it cannot have multiple fibers. We then have $\kappa(Y)=0$.

Let us now assume $g(E)=0$. In this case $L$ is trivial since $\operatorname{deg}(L)=0$. Again, there is a holomorphic $n$-section $\Sigma$ which is normalized by a smooth elliptic curve $C^{\prime}$.

Following [Fri98] page 193, there is a finite cover $\pi^{\prime}: Y^{\prime} \longrightarrow C^{\prime}$ of $\pi: Y \longrightarrow E$ with a holomorphic 1-section and such that $L^{\prime}=\mathcal{O}_{C^{\prime}}$. We then have that $Y^{\prime}=C^{\prime} \times F$ for some elliptic curve $F$. Because of Theorem 7.4 page 29 in [BHPV04], the Kodaira dimension of $Y$ cannot be one. \(\square\)

Let us conclude by showing that $X$ cannot be birational to a rational or ruled surface.

Lemma 2.3. Let $(X, D)$ be a toroidal compactification with $\bar{c}_{2}=1$. Then $X$ cannot have $\kappa(X)=-\infty$.

Proof. Recall that the minimal models of surfaces with negative Kodaira dimension are $\mathbb{P}_{2}$, the Hirzebruch surfaces $X_{e}$ and ruled surfaces over Riemann surfaces of genus $g \geq 1$, see Chapter VI in BHPV04. Since
$$c_{2}\left(\mathbb{P}_{2}\right)=3, \quad c_{2}\left(X_{e}\right)=4,$$
a toroidal compactification with $\bar{c}_{2}=1$ cannot have these surfaces as minimal model. Moreover, since a negative elliptic curve must occur as a $n$-section of the ruling, the Hurwitz formula shows that $X$ has to be the blow up of a surface $Y$ ruled over an elliptic curve. In this case $c_{2}(Y)=0$. Thus, $X$ is the blow up of $Y$ at a single point. Since the rank of the Picard group of $X$ is three, by Proposition 3.8 in [DiC12] we have that $X$ can at most have two cusps. Let us denote by $(Y, C)$ the blow down configuration of $(X, D)$ and let us assume $C$ consists of one irreducible components only. We then have that $C$ must be a $n$-section of the ruling of $Y$. It is easily seen that $C$ cannot be a 1-section of the ruling. If otherwise, $X \backslash D$ contains a $\mathbb{P}_{1}$ with just one puncture. For the same reason, $C$ must be singular at a single point say $p$. Let $F$ be the fiber of the ruling of $Y$ passing through the point $p$. Now, assume that the tangent line of $F$ at $p$ does not coincide with any of the tangent lines of $C$ at $p$. Blowing up the point $p$, we obtain that the proper transform $\tilde{F}$ of $F$ in entirely contained in $X \backslash D$. This is clearly impossible as $\tilde{F} \simeq \mathbb{P}_{1}$.

We proceed in a similar way if the tangent line of $F$ at $p$ coincides with one of the tangent lines of $C$ at $p$. In this case, $\tilde{F}$ with one puncture is entirely contained in $X \backslash D$. This is again impossible.

Let us conclude by studying the case when $(X, D)$ has two cusps. In this situation $(Y, C)$ is such that $C$ consists of two irreducible components, say $C_{1}$ and $C_{2}$, intersecting in a point $p$. The irreducible components of $C$ might be singular at the point $p$ only, having an ordinary singular point there. Moreover, the tangents lines of $C_{1}$ and $C_{2}$ at $p$ must be all distinct. We can then proceed as in the one cusp case to get a contradiction. \(\square\)

Let us summarize the results of this section into a proposition.
Proposition 2.4. Let $(X, D)$ be a toroidal compactification with $\bar{c}_{2}=1$. Then the Kodaira dimension of $X$ is zero.

Of course, it remains to be seen if any such example actually exists. This problem is addressed in the next section.

\section*{3. The case $\kappa=0$}

In light of Proposition 2.4, a toroidal compactification with $\bar{c}_{2}=1$ must be birational to a minimal surface of zero Kodaira dimension. Recall that minimal surfaces with zero Kodaira dimension are given by:
\begin{itemize}
\item[-] K3 surfaces, $c_{2}=24 ;$
\item[-] Enriques surfaces, $c_{2}=12$;
\item[-] Abelian surfaces, $c_{2}=0$;
\item[-] bi-elliptic surfaces, $c_{2}=0$;
\end{itemize}
for details see again Chapter VI in BHPV04. Thus, let $(X, D)$ be a as in Proposition 2.4. Since $\bar{c}_{2}=c_{2}=1$, we have that $X$ is the blow up at just one point of an Abelian or bi-elliptic surface. Now, let $D_{1}, \ldots, D_{k}$ be the irreducible components of the divisor $D$. Since each $D_{i}$ is a smooth elliptic curve with negative self-intersection, we have
$$\bar{c}_{1}^{2}(X)=\left(K_{X}+\sum_{i} D_{i}\right)^{2}=K_{X}^{2}-\sum_{i} D_{i}^{2}=-1-\sum_{i} D_{i}^{2} .$$
But now $3 \bar{c}_{2}(X)=\bar{c}_{1}^{2}(X)$, which implies
$$-D_{1}^{2}-\ldots-D_{k}^{2}=4 .$$
Therefore, we have the following finite list of configurations:
\begin{itemize}
\item[-] 1 cusp, $D_{1}^{2}=-4$;
\item[-] 2 cusps, $D_{1}^{2}=-1, D_{2}^{2}=-3$ or $D_{1}^{2}=-2, D_{2}^{2}=-2$;
\item[-] 3 cusps, $D_{1}^{2}=-1, D_{2}^{2}=-1, D_{3}^{2}=-2$;
\item[-] 4 cusps, $D_{1}^{2}=D_{2}^{2}=D_{3}^{2}=D_{4}^{2}=-1$.
\end{itemize}

Now, let us denote by $(Y, C)$ the blow down configuration of $(X, D)$. Since $Y$ is an Abelian or bi-elliptic surface, we have $K_{Y}=0$. Thus, if $C_{i}$ is an irreducible component of $C$ in $Y$, we have
$$p_{a}\left(C_{i}\right)=1+\frac{C_{i}^{2}}{2} .$$
Note that $C_{i}^{2} \geq-2$. If $C^{2}=-2$, then $C_{i}$ is a smooth rational curve. This is impossible since $Y$ is covered by $\mathbb{C}^{2}$. If $C_{i}^{2}=0$, with $C_{i}$ non-smooth, then $C_{i}$ is a rational curve with a single node or a cusp. This is again impossible as, in both of these cases, $C_{i}$ is normalized by a $\mathbb{P}_{1}$. In conclusion, either $C_{i}$ is a smooth elliptic curve with trivial self-intersection, or $C_{i}$ has a singular point, say $p$, and $C_{i}^{2}=2 n$ with $n \geq 1$. Let us study the singular case first. Thus, let
$$\pi: X \longrightarrow Y$$
be the blow up map at $p$. We then have
$$\pi^{*} C_{i}=D_{i}+r E$$
where $D_{i}$ is the proper transform of $C_{i}$ in $X, E$ is the exceptional divisor and $r$ is the multiplicity of the singular point $p$. Moreover, we have $D_{i} \cdot E=r, D_{i}^{2}=C_{i}^{2}-r^{2}$ and
$$2 p_{a}\left(D_{i}\right)-2=2 p_{a}\left(C_{i}\right)-2-r(r-1) .$$

Now, if we want $D_{i}^{2} \leq-1$ with $C_{i}$ not smooth, we must have
$$D_{i}^{2}=2 n-r^{2}<-1 .$$
Since $D_{i}$ is a smooth elliptic curve, the equation given in 2 simplifies to the quadratic equation
$$r^{2}-r-2 n=0,$$
whose solutions are given by
$$r_{1,2}=\frac{1 \pm \sqrt{1+8 n}}{2} .$$
Since $r$ is a positive integer, we just have to consider the plus sign in the formula above. Thus, the self-intersection of $D_{i}$ is given by
$$2 n-\left(\frac{1+\sqrt{1+8 n}}{2}\right)^{2} \text {, }$$
for $n \geq 1$. This self-intersection is easily seen to be decreasing in $n$ and for $n \geq 7$ to be less than -4. All the possibilities for $1 \leq n \leq 6$ are then given by the following list:
$$\begin{array}{ll}
n=1, & C_{i}^{2}=2, \quad r=2 ; \\
n=3, & C_{i}^{2}=6, \quad r=3 ; \\
n=6, & C_{i}^{2}=12, \quad r=4 .
\end{array}$$

In conclusion, we then have to understand if on an Abelian or bi-elliptic surface we can find curves with just one singular point of multiplicities and self-intersections as in 3. Let us start by studying the case when $Y$ is an Abelian surface. First, we observe that the line bundle associated to a curve as in 3 must be ample.

Lemma 3.1. Let $C$ be an irreducible divisor on an Abelian surface $Y$ such that $C^{2}>0$. Then $L=\mathcal{O}_{Y}(C)$ is ample.

Proof. Let $E$ be any curve on $Y$, we would like to show that $C \cdot E>0$. Since $C^{2}>0$, we just need to study the curves $E \neq C$. For these curves we clearly have $C \cdot E \geq 0$. Assume then $C \cdot E=0$. Let us denote by $t_{y}(E)$ the translation of the curve $E$ by an element $y \in Y$. By appropriately choosing $y \in Y$, we can assume that $t_{y}(E) \cap C \neq\{0\}$. Since the curve $t_{y}(E)$ is numerically equivalent to $E$ we have then reached a contradiction. We therefore conclude that $L$ is a strictly nef line bundle with positive self-intersection. The lemma is now a consequence of Nakai's criterion for ampleness of divisors on surfaces, see Corollary 6.4 page 161 in [BHPV04]. \(\square\)

Next, we show that curves as in 3 cannot exist on an Abelian surface. The proof of this fact uses standard properties of theta functions. Recall that any effective divisor on a complex torus is the divisor of a theta function, see Théorème 3.1 page

43 in [Deb99]. Now, let $C$ be a reduced divisor as in Lemma 3.1. Then, if we let $V=\mathbb{C}^{2}$ and $\pi: V \longrightarrow V / \Gamma$ be the universal covering map, we have that
$$\pi^{*} C=(\theta)$$
for some theta function on $V$. More precisely, we can find a Hermitian form $H$, a character $\alpha: \Gamma \longrightarrow U(1)$ and a theta function satisfying 4 and the following "normalized" functional equation
$$\theta(z+\gamma)=\alpha(\gamma) e^{\pi H(\gamma, z)+\frac{\pi}{2} H(\gamma, \gamma)} \theta(z)=e_{\gamma}(z) \theta(z)$$
for any $z \in V$ and $\gamma \in \Gamma$. Note how $e_{\gamma}$ is the factor of holomorphy for the line bundle $L=\mathcal{O}_{Y}(C)$. There is then an identification between the space of sections of L and the vector space of theta functions of type $(H, \alpha)$ on $V$.

In light of the list obtained in 3, we are interested in the case when $C$ has a singular point only. Thus, let $C \in|L|$ be reduced divisor and let us denote by $C^{*}=C \backslash\{p\}$ the smooth part of $C$. For every $q \in C^{*}, T_{q} C$ is a well defined 1-dimensional subspace of $T_{q} Y$. Thus, if we let $z_{1}, z_{2}$ be coordinate functions for $V$, the equation for $T_{q} C$ is given by
$$\sum_{i=1}^{2} \partial_{z_{i}} \theta(q)\left(z_{i}-q_{i}\right)=0 .$$
We can then consider a Gauss type map
$$G: C^{*} \longrightarrow \mathbb{P}_{1}$$
where
$$G(q)=\left(\partial_{z_{1}} \theta(q): \partial_{z_{2}} \theta(q)\right) .$$
We claim that since $C$ is reduced and $L$ is ample, then the Gauss map cannot be constant. Let us proceed by contradiction. Say that the image of the Gauss map is the point $\left[x_{1}: x_{2}\right] \in \mathbb{P}_{1}$. If $x_{2} \neq 0$, let us define the derivation
$$\partial_{w}:=\partial_{z_{1}}-k \partial_{z_{2}}$$
where $k=x_{1} / x_{2}$. If $x_{2}=0$, let us simply consider the derivative along the second coordinate function, in other words $\partial_{w}=\partial_{z_{2}}$. By construction, we have $\partial_{w} \theta=0$ for all $q \in C^{*}$. Since $C$ is reduced, the function
$$f=\partial_{w} \theta / \theta$$
is holomorphic on $V$ except at the singular points of $\pi^{*} C$. By the Hartogs extension theorem, we know that $f$ can be extended to a holomorphic function on $V$. Because of the functional equation 5, we have
$$f(z+\gamma)-f(z)=\pi H(\gamma, v)$$
for any $\gamma \in \Gamma$, where
$$v=\partial_{w}\binom{z_{1}}{z_{2}} .$$

This implies
$$f(z)=\pi H(z, v)+K$$
for some constant $K$. Since $f$ is holomorphic and $H$ is anti-holomorphic in $z$, we have therefore reached a contradiction. To sum up, we have shown that for any derivation $\partial_{w}$, the function $\partial_{w} \theta$ cannot be identically zero on $C^{*}$.

Now, because of functional equation given in 4 the restriction of $\partial_{w} \theta$ to $\pi^{*} C$ can be considered as a section of the line bundle $L$ restricted to $C$. Thus, the intersection number $\left(\partial_{w} \theta\right) \cdot C$ coincides with the self-intersection $C^{2}$. Let us now consider a derivation $\partial_{w}$ with parameter $w$ determined by a generic point in the image of the Gauss map. Say that the multiplicity of the singular point $p$ is $r_{p}$. The intersection number of $\left(\partial_{w} \theta\right)$ and $C$ at the singular point $p$ is then computed by $r_{p}\left(r_{p}-1\right)$. Moreover, by construction $\partial_{w} \theta$ vanishes somewhere on $C^{*}$. We conclude that
$$C^{2} \geq r_{p}\left(r_{p}-1\right)+1 .$$

Now in all of the cases given in 3, we have
$$C_{i}^{2}=r(r-1)$$
so that, using 6, we can rule out the cases of one, two and three cusps.
Let us summarize these results into a lemma.
Lemma 3.2. Let $(X, D)$ be a toroidal compactification with $\bar{c}_{2}=1$ and $\kappa(X)=0$. If $X$ is not bi-rational to a bi-elliptic surface, then $X$ is the blow up of an Abelian surface. Moreover, $D$ consits of four disjoint smooth elliptic curves with $D_{1}^{2}=$ $D_{2}^{2}=D_{3}^{2}=D_{4}^{2}=-1$.

Thus, in light of Lemma 3.2, we have to classify the pairs $(Y, C)$ where $Y$ is an Abelian surface and $C$ consists of four smooth elliptic curves intersecting in just one point. We will show that, up to isomorphism, there is only one such pair. This result follows from few geometrical facts.

Fact 3.3. Let $Y=\mathbb{C}^{2} / \Gamma$ be an Abelian surface containing two smooth elliptic curves $C_{1}, C_{2}$ such that $C_{1} \cdot C_{2}=1$. Then $Y$ is isomorphic to the product $C_{1} \times C_{2}$.

Proof. By translating the curves $C_{1}$ and $C_{2}$, we can always assume that $C_{1} \cap C_{2}=$ $\{(0,0)\}$. The curves $C_{i}, i=1,2$, are then subgroups of $Y$. Thus, we can define the map
$$\varphi: C_{1} \times C_{2} \longrightarrow Y$$
which sends the point $(p, q) \in C_{1} \times C_{2}$ to $p-q \in Y$. The map $\varphi$ is clearly one-toone. \(\square\)

Fact 3.4. Let $Y=\mathbb{C}^{2} / \Gamma$ be an Abelian surface containing three smooth elliptic curves $C_{i}, i=1,2,3$, such that $C_{1} \cap C_{2} \cap C_{3}=\{(0,0)\}$ and such that $C_{i} \cdot C_{j}=1$ for any $i \neq j$. Then $Y$ is isomorphic to the product $C \times C$ where $C_{i}=C$ for any $i$.

Proof. By Fact 3.3, we have that $Y=C_{1} \times C_{2}$. Since $C_{3} \cdot C_{1}=1$, for $i=1,2$, we conclude that $C_{3}=C_{i}$ for $i=1,2$. The proof is complete. \(\square\)

Fact 3.5. Let $Y$ be an Abelian surface which is the product of two identical elliptic curves, say $C=\mathbb{C} / \Lambda$. Let $(w, z)$ be the natural product coordinates on $Y$. Then any smooth elliptic curve in $Y$, passing through the point $(0,0)$, is given by an equation of the form $w=\alpha z$, with $\alpha$ such that $\alpha \Lambda \subseteq \Lambda$.

Proof. A subgroup in $\mathbb{C}^{2}$ is given by an equation of the form $w=\alpha z$. Finally, this equation makes sense on $Y$ if $\alpha \Lambda \subseteq \Lambda$. \(\square\)

Fact 3.6. Let us denote by $C_{\alpha}$ the curve in $Y=C \times C$ given by the equation $w=\alpha z$ with $\alpha \Lambda \subseteq \Lambda$ and $\alpha \neq 0$. Then $C_{0} \cdot C_{\alpha}=1$ if and only if $\alpha \Lambda=\Lambda$.

Proof. The intersection $C_{0} \cap C_{\alpha}$ consists of $[\alpha \Lambda: \Lambda]$ distinct points, where by $[\alpha \Lambda: \Lambda]$ we denote the index of the subgroup $\alpha \Lambda$ in $\Lambda$. \(\square\)

Let us now go back to our original problem. We want to classify all the configurations of four elliptic curves $C_{i}, i=1,2,3,4$, in an Abelian surface $Y$ such that
$$C_{1} \cap C_{2} \cap C_{3} \cap C_{4}=\{p\}$$
for a point $p \in Y$ and
$$C_{i} \cdot C_{j}=1$$
for any $i \neq j \in\{1,2,3,4\}$. Any such configuration will be referred as good configuration. Now, by translating the $C_{i}^{\prime} \mathrm{s}$, we can assume the point $p$ to coincide with the origin in $Y$. Because of Facts 3.3 and 3.4, we can assume $Y=C \times C$ with the curves $C_{1}$ and $C_{2}$ being the factors in the splitting of $Y$. Because of Facts 3.5 and 3.6, we have to look for values of $\alpha$, say $\alpha_{1}$ and $\alpha_{2}$, such that
$$C_{3}=C_{\alpha_{1}}, \quad C_{4}=C_{\alpha_{2}} .$$
Now, for a generic elliptic curve $C=\mathbb{C} / \Lambda$, the only values of $\alpha$ such that $\alpha \Lambda=\Lambda$ are given by $\alpha= \pm 1$. If this is the case, note that $C_{1} \cap C_{-1}$ consists of four disjoint points. These points are exactly the two-torsion points of the lattice $\Lambda$. In conclusion, for a generic elliptic curve $C$, the Abelian surface $Y=C \times C$ cannot support a good configuration. It remains to treat the case of a non-generic elliptic curve $C$. Recall that there are only two elliptic curves with non-generic automorphism group. These elliptic curves correspond to the lattices $\Lambda_{(1, i)}=\mathbb{Z}+\mathbb{Z} i, \Lambda_{(1, \tau)}=\mathbb{Z}+\mathbb{Z} \tau$ where $\tau=e^{\frac{\pi i}{3}}$.

For the lattice $\Lambda_{(1, i)}$, we have four choices of the value of $\alpha$ so that $\alpha \Lambda_{(1, i)}=$ $\Lambda_{(1, i)}$ :
$$\alpha=1, i, i^{2}, i^{3} .$$
It turns out that none of the possible choices involving these parameters give a good configuration. To this aim, it suffices to observe that the configuration
$$w=0, \quad z=0, \quad w=z, \quad w=i z,$$
is such that
$$C_{1} \cap C_{i}=\{(0,0), \quad(1 / 2+i / 2,1 / 2+i / 2)\} .$$
Any other configuration is either isomorphic to the one above or fails to be a good configuration by completely analogous reasons.

For the lattice $\Lambda_{(1, \tau)}$, we have six choices of the value of $\alpha$ so that $\alpha \Lambda_{(1, \tau)}=\Lambda_{(1, \tau)}$ :
$$\alpha=1, \tau, \tau^{2}, \tau^{3}, \tau^{4}, \tau^{5} .$$
Let us observe that
$$w=0, \quad z=0, \quad w=z, \quad w=\tau z,$$
is a good configuration. In fact, the curves $C_{1}$ and $C_{\tau}$ intersect at the points whose z values satisfy the equality
$$(\tau-1) z=0 \quad \bmod \Lambda_{(1, \tau)} .$$
Since $(\tau-1)=\tau^{2}$, we conclude that
$$C_{1} \cap C_{\tau}=\{(0,0)\} .$$
We claim that this is the only configuration that does the job. First, let us try the configuration given by
$$w=0, \quad z=0, \quad w=z, \quad w=\tau^{2} z .$$
Observe that the curves $C_{1}$ and $C_{\tau^{2}}$, not only meet at the origin, but also in other two distinct points. These points are the two distinct zeros of the Weierstrass $\wp$-function associated to the lattice $\Lambda_{(1, \tau)}$. More precisely, we have
$$C_{1} \cap C_{\tau^{2}}=\left\{(0,0), \quad\left(\left(1-\tau^{2}\right) / 3,\left(1-\tau^{2}\right) / 3\right), \quad\left(\left(\tau^{2}-1\right) / 3,\left(\tau^{2}-1\right) / 3\right)\right\} .$$
As the reader can easily verify, any other configuration can be reduced to the two above or to the configuration
$$w=0, \quad z=0, \quad w=z, \quad w=-z,$$
which we already know not to be good. In conclusion, we have the following lemma.
Lemma 3.7. Let $(X, D)$ be a toroidal compactification with $\bar{c}_{2}=1$ and $\kappa(X)=0$ for which $X$ is not birational to a bi-elliptic surface. Then $X$ is the blow up of an Abelian surface $Y=\mathbb{C}^{2} / \Gamma$ with $\Gamma=\Lambda_{(1, \tau)} \times \Lambda_{(1, \tau)}$ and $\tau=e^{\frac{\pi i}{3}}$. Moreover, the blow down divisor $C$ of $D$ is given by
$$w=0, \quad z=0, \quad w=z, \quad w=\tau z,$$
where $(w, z)$ are the natural product coordinates on $Y$.

\section*{4. Proof of the main theorem and conclusions}

In this final section, we combine the results proved in Sections 2 and 3 to give a proof of Theorem A stated in Section 1.1.

Proof of Theorem A. Let $(X, D)$ be a toroidal compactification with $\bar{c}_{2}=1$ for which $X$ is not birational to a bi-elliptic surface. Because of Proposition 2.4, we know that $X$ is the blow up at just one point of a minimal surface $Y$ of zero Kodaira dimension. Moreover, by Lemma 3.2 we know that $Y$ is an Abelian surface. Then, Lemma 3.7 shows that $Y$ has to be the product of two identical elliptic curves associated to the lattice $\Lambda_{(1, \tau)}$, where $\tau=e^{\frac{\pi i}{3}}$. We can then appeal to the results contained in [Hol86] to conclude that the pair $(X, D)$ is indeed the compactification of a cusped complex hyperbolic surface. Alternatively, one can observe that, by construction, the pair $(X, D)$ given in Lemma 3.7 saturates the logarithmic Bogomolov-Miyaoka-Yau inequality. Then, because of the analytical results contained in [TY87], it must be the compactification of a ball quotient. □

It is worth mentioning that the pair $(Y, C)$ given in Lemma 3.7 is the starting point for an interesting construction of Hirzebruch, see [Hir84]. More precisely, the pair $(X, D)$ and other blow ups of $(Y, C)$ are used by Hirzebruch as bases for a clever branched cover construction which produces an infinite sequence of minimal surfaces of general type whose ratio $c_{1}^{2} / c_{2}$ tends to three. In the same paper, Hirzebruch conjectured many of the surfaces he constructed to be compactifications of Picard modular surfaces. This is indeed the case as shown by Holzapfel Hol86. For the particular surface given in Lemma 3.7, one can also refer to [Sto11]. In conclusion, the proof of Theorem B stated in Section 1.1 not only depends on Theorem A, but crucially relies on the fact that the pair given in Lemma 3.7 was already known to be the compactification of a Picard modular surface [Hol86], [Sto11].

\section*{References}
\begin{itemize}
\item[] [AMRT10] A. Ash, D. Mumford, M. Rapoport, Y.-S. Tai, Smooth compactifications of locally symmetric varieties. Second edition. Cambridge Mathematical Library. Cambridge University Press, Cambridge, 2010.
\item[] [BB66] W. L. Baily, A. Borel, Compactifications of arithmetic quotients of bounded symmetric domains, Ann. of Math., 84 (1966), no.2, 442-528.
\item[] [BJ06] A. Borel, L. Ji, Compactifications of locally symmetric spaces. Mathematics: Theory \& Applications, Birkäuser Boston, Inc. Boston, MA, 2006.
\item[] [BHPV04] W. P. Barth, K. Hulek, C. A. Peters, A. Van de Ven Compact complex surfaces, Ergebnisse der Mathematik und ihrer Grenzgebiete. 3. Folge. A Series of Modern Surveys in Mathematics, 4. Springer-Verlag, Berlin, 2004.
\item[] [CS10] D. I. Cartwright, T. Steger, Enumeration of the 50 fake projective planes. C. R. Math. Acad. Sci. Paris, 258 (2010), no.8, 2708-2713.
\item[] [Deb99] O. Debarre, Tores et variétés abéliennes complexes, Cours Spécializés, 6. Société Mathématique de France, Paris; EDP Sciences, Les Ulis, 1999.
\item[] [DM93] P. Deligne, G. Mostow, Commensurabilities among lattices in PU(1,n), Annals of Mathematics Studies 132, Princeton University Press, Princeton, NJ, 1993.
\item[] [DiC12] G. Di Cerbo, L. F. Di Cerbo, Effective results for complex hyperbolic manifolds, arXiv:1212.0501 [mathDG], 2012.
\end{itemize}
[DiC12a] L. F. Di Cerbo, Finite-volume complex-hyperbolic surfaces, their toroidal compactifications, and geometric applications. Pacific J. Math., 255 (2012), no.2, 305-315.
[Fri98] R. Friedman, Algebraic Surfaces and Holomorphic Vector Bundles, Univesitext. Springer-Verlag, New York 1998.
[Gro82] M. Gromov, Volume and bounded cohomology, Publ. Math. Inst. Hautes Et́udes Sci. 56 (1982), 5-99.
[Har77] R. Hartshorne, Algebraic Geometry, Springer-Verlag, New York 1977, Graduate Texts In Mathematics, No. 52.
[Hir84] F. Hirzebruch, Chern numbers of algebraic surfaces: an example. Math. Ann. 266 (1984), 351-356.
[Hol86] R. P. Holzapfel, Chern numbers of algebraic surfaces-Hirzebruch's examples are Picard modular surfaces. Math. Nachr., 126 (1986), 255-273.
[Hum98] C. Hummel, Rank one lattices whose parabolic isometries have no rotational part. Proc. Am. Math. Soc. 126 (1998), 2453-2458.
[Kaw78] Y. Kawamata, On deformations of compactifiable complex manifolds. Math. Ann., 235 (1978), no.3, 247-265.
[Kli03] B. Klingler, Sur la rigidité de certains groupes foundamentaux, l'arithméticité des réseaux hyperboliques complexes, et le "faux plans projectifs". Invent.Math., 153 (2003), no.1, 105-143.
[Mar84] G. Margulis, Arithmeticity of the irreducible lattices in semisimple groups of rank gretaer than 1. Invent. Math. 76 (1984), 93-120.
[Mok12] N. Mok, Projective algebraicity of minimal compactifications of complex-hyperbolic space forms of finite-volume. Perspective in analysis, geometry, and topology, 331-354, Prog. Math., 296, Birkhäuser/Springer, New York, 2012.
[Mum77] D. Mumford, Hirzebruch's Proportionality Theorem in the Non-Compact Case. Invent. Math. 42 (1977), 239-272.
[Mum79] D. Mumford, An Algebraic surface with $K$ ample, $\left(K^{2}\right)=9, p_{g}=q=0$. Amer. J. Math., 101 (1979), no.1, 233-244.
[Par98] J. R. Parker, On the volume of cusped, complex hyperbolic manifolds and orbifolds, Duke Math. J. 94 (1998), 433-464.
[PY07] G. Prasad, S.-K. Yeung, Fake projective planes. Invent. Math., 168 (2007), no.2, 321-370.
[Rém04] R. Rémy, Covolume des groupes $S$-arithmétiques et faux plans projectifs [d'après Mumford, Prasad, Klingler, Yeung, Prasad-Yeung]. Séminare Bourbaki, 60ème année, 2007-2008, no. 984.
[Sak80] F. Sakai, Semistable curves on algebraic surfaces and logarithmic pluricanonical maps. Math. Ann., 254 (1980), no.2, 89-120.
[SY82] Y. T. Siu, S. T. Yau, Compactification of negatively curved complete Kähler manifolds of finite volume, Seminars in Differential Geometry, pp. 363-380, Ann. of Math. Stud., Vol. 102, Princeton Univ. Press, Princeton, N. J., 1982.
[Sto11] M. Stover, Volumes of Picard modular surfaces. Proc. Amer. Math. Soc., 139 (2011), no.9, 3045-3056.
[TY87] G. Tian, S.-T. Yau, Existence of Kähler-Einstein metrics on complete Kähler manifolds and their applications to algebraic geometry. Mathematical aspects of string theory (San Diego, Calif., 1986), 574-628, Adv. Ser. Math. Phys., 1, World Sci. Publishing, Singapore, 1987.
[Wan72] H. C. Wang, Topics on totally discontinuous groups, Symmetric Spaces, 459-487, edited by W. B. Boothby and G. L. Weiss, Pure and Appl. Math. 8, Marcel Dekker, New York, 1972.
[Yau78] S.-T. Yau, On the Ricci curvature of a compact Kähler manifold and the complex Monge-Ampère equation. Comm. Pure Appl. Math. 31 (1978), 339-411.

ON THE CLASSIFICATION OF TOROIDAL COMPACTIFICATIONS WITH $3 \bar{c}_{2}=\bar{c}_{1}^{2}$ AND $\bar{c}_{2}=1 \overline{ }$
[Yeu04] S.-K. Yeung, Integrality and arithmeticity of co-compact lattice corresponding to certain complex two-ball quotients of Picard number one. Asian J. Math., 8 (2004), no.21, 107-129.
[Yeu13] S.-K. Yeung, Classification of surfaces of general type with Euler number 3. J. Reine Angew. Math., 679 (2013), 1-22.

Department of Mathematics, Duke University, Durham NC 27708-0320, USA
E-mail address: luca@math.duke.edu