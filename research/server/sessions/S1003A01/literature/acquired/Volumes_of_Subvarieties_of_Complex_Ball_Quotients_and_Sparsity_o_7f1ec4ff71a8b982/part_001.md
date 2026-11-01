---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Volumes of Subvarieties of Complex Ball Quotients and Sparsity of Rational Points]

---
source_file: 2310_08060.pdf
converter: mathpix
format: mmd
---

\title{
Volumes of Subvarieties of Complex Ball Quotients and Sparsity of Rational Points
}

\author{
Soheil Memariansorkhabi
}

\begin{abstract}
Let $X=\Gamma \backslash \mathbb{B}^{n}$ be an $n$-dimensional complex ball quotient by a torsion-free non-uniform lattice $\Gamma$ whose parabolic subgroups are unipotent. We prove that the volumes of subvarieties of $X$ are controlled by the systole of $X$, which is the length of a shortest closed geodesic of $X$.

There are a number of arithmetic and geometric consequences: the systole of $X$ controls the growth rate of rational points on $X$, uniformly in the field of definition. Also, we obtain effective global generation and very ampleness results for multiples of the canonical bundle $K_{\bar{X}}$, where $\bar{X}$ is the toroidal compactification of $X$. These follow from the bound we find for the Seshadri constant of $K_{\bar{X}}$ in terms of the systole.
\end{abstract}

\section*{1. Introduction}

Let $X=\Gamma \backslash \mathbb{B}^{n}$ be an $n$-dimensional complex ball quotient by a torsion-free lattice $\Gamma$. The complex ball has an intrinsic Hermitian metric (Bergman metric) which induces a Kähler form on $X$. This Kähler form also induces a Kähler form on a subvariety $V$ of $X$. The volume of $V$ with respect to the induced Kähler form on $X$ will be called the induced Kähler volume and will be denoted by $\operatorname{vol}_{X}(V)$.

The main goal of this paper is to find a uniform lower bound for the induced Kähler and canonical volumes of all subvarieties of a non-compact ball quotient $X$ in terms of a geometric quantity of $X$ :

Theorem A. (Theorem 5.2) Let $X=\Gamma \backslash \mathbb{B}^{n}$ be a complex ball quotient by a torsion-free non-uniform lattice $\Gamma$ whose parabolic stabilizers are unipotent. Let $V \subset X$ be an irreducible subvariety of dimension $m>0$. Then,
$$\operatorname{vol}_{X}(V) \geq \frac{(4 \pi)^{m}}{m!} \sinh ^{2 m}(\operatorname{sys}(X) / 2),$$
where $\operatorname{vol}_{X}(V)$ is the volume of $V$ induced by the Bergman metric on $V$ and $\operatorname{sys}(X)$ is the length of a shortest closed geodesic on $X$.

When $X$ is a compact ball quotient, inequality (1.1) was proved by Hwang and To [HT99]. Their inequality bounds the induced Kähler volume of subvarieties in terms of the injectivity radius of $X$. While the injectivity radius is a positive real number for compact $X$, for non-compact $X$, it is zero, as the injectivity radius becomes arbitrarily small near the cusps. We generalize their inequality for non-compact $X$, under a mild assumption on the parabolic stabilizer of $\Gamma$, by replacing the injectivity radius with half of the systole. For compact $X$, the injectivity radius is half of the systole. However, for non-compact $X$, the systole is non-zero (see Proposition 3.9) and can be estimated using the absolute value of the trace of hyperbolic elements in $\Gamma$ (see Lemma 3.5).

Note that the assumption that the parabolic stabilizers of the lattice are unipotent is mild, as it holds for every neat lattice, and any lattice $\Gamma$ admits a finite index subgroup with this property (see Selberg's lemma [Rat06, page 331]). With this assumption, the variety $X$ admits a smooth projective toroidal compactification $\bar{X}$ whose boundary divisor $D=\bar{X} \backslash X$ is a disjoint union of abelian varieties with ample conormal bundle ([Mok12]). Bakker and Tsimerman [BT18] proved that if the uniform depth of cusps of $X$ is sufficiently large, then the canonical bundle of the toroidal compactification $K_{\bar{X}}$ is ample. We prove in Theorem 3.14 that the systole of $X$ bounds the uniform depth of cusps from below. Therefore, if $\operatorname{sys}(X)$ is sufficiently large, then $K_{\bar{X}}$ is ample.

For a subvariety $V \subset \bar{X}$ of dimension $m>0$, we denote the degree of $V$ with respect to the line bundle $K_{\bar{X}}$ by $\operatorname{deg}_{\bar{X}}(V)$ :
$$\operatorname{deg}_{\bar{X}}(V):=K \frac{m}{X} \cdot V .$$
Also, we study the canonical volume of a subvariety $V$ which is an intrinsic quantity of $V$ and a priori does not depend on the ambient space $\bar{X}$. Let $V^{\prime}$ be a smooth variety birational to $V$ with a canonical bundle $K_{V^{\prime}}$. The canonical volume of the variety $V$ is
$$\widetilde{\operatorname{vol}_{V}}:=\underset{b \rightarrow \infty}{\limsup } \frac{h^{0}\left(V^{\prime}, b K_{V^{\prime}}\right)}{b^{m} / m!},$$
which does not depend on the choice of $V^{\prime}$. In particular, if $V$ is an integral curve, that is, a reduced and irreducible algebraic curve, then the canonical volume of $V$ is $2 g-2$, where $g$ denotes the genus of the curve. The canonical volume of $V$ measures the asymptotic growth rate of the pluricanonical linear series $\left|b K_{V^{\prime}}\right|$. The canonical volume is a non-negative real number and it is positive if and only if the linear system $\left|b K_{V^{\prime}}\right|$ embeds $V^{\prime}$ birationally in a projective space for a large enough $b$, i.e., $V$ is of general type.

We prove that the systole controls both the canonical volume of $V$ and its degree with respect to $K_{\bar{X}}$ in the following sense:

Theorem B. (Theorem 5.7+ Theorem 5.9) With the same assumption on $X$ as Theorem A, let $\bar{X}$ be the toroidal compactification of $X$ and let $V \subset \bar{X}$ be a subvariety of dimension $m>0$ with $X \cap V \neq \varnothing$. Suppose that $\operatorname{sys}(X) \geq 4 \ln \left(5 n+(8 \pi)^{4}\right)$. Then the following inequalities hold:
$$\begin{aligned}
\widetilde{\operatorname{vol}}_{V} & >\left(\frac{m}{4 \pi}\right)^{m} e^{m \operatorname{sys}(X) / 16}, \\
\operatorname{deg}_{\bar{X}}(V) & >\left(\frac{n}{4 \pi}\right)^{m} e^{m \operatorname{sys}(X) / 16} .
\end{aligned}$$

Note that systole cannot decrease in a cover and for every $X$ there exists a finite cover $X^{\prime}$ such that $\operatorname{sys}\left(X^{\prime}\right)$ is sufficiently large (see Proposition 3.21). As a byproduct of Theorem B, we observe that in a cofinal normal tower of coverings of $X$ (see Definition 3.20), the canonical volume of subvarieties can be made arbitrarily large by going sufficiently far up the tower (see Proposition 3.21).

Application I: sparsity of rational points. A smooth toroidal compactification $\bar{X}$ of $X$ can be defined over a number field $F$ provided that $\Gamma$ is neat and arithmetic (see [Fal84]). Combining Theorem A and Theorem B with the determinant method (in particular [BM22, Theorem 3.4]), we get that $\operatorname{sys}(X)$ controls the growth rate of rational points:

Corollary C. (Corollary 8.4) Suppose $\bar{X}$ is defined on the number field $F$. Let $\epsilon$ be a positive number and $B$ any number such that $B \geq \epsilon[F: \mathbb{Q}]$.
\begin{itemize}
\item[(i)] Let $L_{1}=K_{\bar{X}}+D$. Then, there exists a constant $c_{1}$ depending on $X, F$ and $\epsilon$ such that:
$$\#\left\{x \in X(F) \mid \mathrm{H}_{L_{1}}(x) \leq B\right\} \leq c_{1} B^{\delta},$$
where
$$\delta=\frac{[F: \mathbb{Q}] n(n+3)}{\sinh ^{2}(\operatorname{sys}(X) / 2)(n+1)}(1+\epsilon),$$
and $H_{L_{1}}$ is the multiplicative height (see equation (8.2) for the definition of multiplicative height).
\item[(ii)] Let $L_{2}=K_{\bar{X}}$ and assume that $\operatorname{sys}(X) \geq 4 \ln \left(5 n+(4 \pi)^{4}\right)$. Then, there exists a constant $c_{2}$ depending on $X, F$ and $\epsilon$ such that
$$\#\left\{x \in X(F) \mid \mathrm{H}_{L_{2}}(x) \leq B\right\} \leq c_{2} B^{\delta},$$
where
$$\delta=\frac{4 \pi[F: \mathbb{Q}](n+3)}{e^{\operatorname{sys}(X) / 16}}(1+\epsilon),$$
and $H_{L_{2}}$ is the multiplicative height.
\end{itemize}

Corollary C tells us that if we fix $n$ and $[F: \mathbb{Q}]$, then the growth rate of $F$-rational points decreases as sys $(X)$ gets larger. This aligns with the philosophy in Diophantine geometry that geometric constraints naturally govern the arithmetic properties of a variety.

Application II: effective very ampleness and Seshadri constant. Combining Theorem B with the results in the adjunction theory proved by Angehrn-Siu [AS95], Kollar [Ko197] and Ein-Lazersfeld-Nakamaye [ELN96] gives effective results in global generation, very ampleness and separation of jets:

Corollary D. (Corollary 6.14) With the same $X$ and $\bar{X}$ as Theorem B, suppose that
$$\operatorname{sys}(X) \geq 20 \max \left\{n \ln ((1+2 n+n!)(n+1)), \ln \left(5 n+(8 \pi)^{4}\right)\right\} .$$

Then, the following hold
\begin{itemize}
\item[(i)] $2 K_{\bar{X}}$ is globally generated and very ample modulo $D$.
\item[(ii)] $3 K_{\bar{X}}$ is very ample.
\end{itemize}

Another implication of Theorem B is the following bound on the Seshadri constant of $K_{\bar{X}}$ :
Corollary E. (Theorem 6.9) Suppose that
$$\operatorname{sys}(X) \geq 20 \max \left\{n \ln ((1+2 n+n!)(n+s)), \ln \left(5 n+(8 \pi)^{4}\right)\right\} .$$
Then $2 K_{\bar{X}}$ separates any $s$-jets and in particular for every $x \in X$, we have
$$\epsilon\left(K_{\bar{X}}, x\right) \geq s / 2,$$
where $\epsilon\left(K_{\bar{X}}, x\right)$ is the Seshadri constant of $K_{\bar{X}}$ at $x$, as defined in Definition 6.8.

As the boundary divisor $D$ is a disjoint union of abelian varieties, the adjunction formula gives that $K_{\bar{X} \mid D}$ is isomorphic to the conormal bundle $O_{D}(-D)$, which is always an ample bundle due to [Mok12]. It is classical that every ample line bundle on an abelian variety determines a positive definite Hermitian form on that abelian variety. Let $\operatorname{sys}(D)$ be the length of a shortest closed geodesic on $D$ with respect to the metric induced by the ample line bundle $K_{\bar{X} \mid D}$. Assuming that both sys( $X$ ) and $\operatorname{sys}(D)$ are sufficiently large relative to $n$, we get that the bicanonical bundle $2 K_{\bar{X}}$ is very ample:

Corollary F. (Corollary 7.3) With the same $X$ and $\bar{X}$ as Theorem A, suppose that sys( $D$ ) > $2 \sqrt{2 n / \pi}$ and that
$$\operatorname{sys}(X) \geq 20 \max \left\{n \ln (5 n(1+2 n+n!)), \ln \left(5 n+(8 \pi)^{4}\right)\right\} .$$
Then, for every $x \in \bar{X}$ we have
$$\epsilon\left(K_{\bar{X}}, x\right) \geq 2 n,$$
and in particular $2 K_{\bar{X}}$ is very ample.
Previous results and comparison. Besides the results mentioned above, the central purposes of our paper are the following technical advancements on the subject:
\begin{itemize}
\item[-] Corollary C does not follow from the main results of Ellenberg-Lawrence-Venkatesh [ELV23] or Brunebarbe-Maculan [BM22] or Chiu [Chi22] on the growth rate of integral points. In general, bounding the growth rate of rational points on a quasiprojective variety is more difficult than bounding the growth rate of integral points. For example, on $X=\mathbb{P}_{F}^{1} \backslash\{0,1, \infty\}$, there are infinitely many $F$-rational points; however, there are only finitely many integral points on $X$ because of the famous theorem of Siegel (see [BM22, Remark 3.3]).
It is observed in [ELV23, BM22] that if one has a control on the degree of all subvarieties, the bound on the growth rate of rational points improves in the strategy of Bombieri-Pila [BP89] and Heath-Brown [HB02]. However, to get the lower bound on the degree of subvarieties, they passed to an étale cover and this restricts them to get results only on the integral points, rather than rational points. The point is that when one pulls back rational points along finite étale maps on quasi-projective variety, the field of definition cannot be controlled, but for integral points, it can be. Our intrinsic approach has the advantage that it does not require passage to a cover to raise the degree of subvarieties and hence we can get the bound on the growth rate of rational points.
\item[-] Our results show that the hyperbolicity properties of a non-compact ball quotient can be controlled by its systole, and hence the injectivity radius of the interior and depth of cusps need not to be dealt with separately (see for example [Won18] for the other approach). In our paper, this is achieved by proving that the systole gives a lower bound for both the uniform depth of cusps (Theorem 3.14) and injectivity radius of the thick part (section 4).
\item[-] Our results depend intrinsically on $X$, and it is not required to pass to a cover of $X$ to apply them. In particular, our results apply even in the case that $X$ is not a normal cover of another variety (see for example [Yeu12, Theorem 5] and [DCL21, Corollary 1.6.] in which the passage to a cover of $X$ is required. Indeed, these results
\end{itemize}
\begin{itemize}
\item[] are about a cover of $X$ rather than $X$ itself). Note that when $\Gamma$ is a maximal lattice, $X$ is not a finite cover of other locally symmetric domain.
\item[-] The systole can be estimated by estimating the absolute values of traces of hyperbolic elements (see Lemma 3.5). Especially when the coverings arise from congruence relations (see Proposition 3.22 for an example), estimating the traces of hyperbolic elements is possibly within reach, and our results then allow one to conclude the increasing hyperbolicity behavior.
\end{itemize}

This kind of increasing hyperbolicity behavior has been extensively studied for locally symmetric spaces in towers of coverings arising from congruence relations, with high ramification at the cusps (see for example [Nad89, Bru20a, Bru20b, AVA18, AVA17, Rou16]). However, our approach does not require high ramification of cusps, and our results apply even in cases where some cusps do not ramify. A typical example is the covering of modular curves $X_{1}(p) \rightarrow X(1)$, which has $(p-1) / 2$ cusps that do not ramify (see [Shi71, page 26] and [Ogg72] for more details). We see their higher-dimensional analogue in Proposition 3.22, where the systole tends to infinity as $p \rightarrow \infty$.

The following are some of the previous effective results for pluricanonical bundles:
\begin{itemize}
\item[(i)] Yeung proved in [Yeu12] that for a quasi-projective variety $M$, there exists a finite normal cover $M^{\prime}$ such that $L^{2}$-holomorphic sections of $K_{M^{\prime}}$ give rise to a holomorphic immersion of $M^{\prime}$ into some projective space.
\item[(ii)] Di Cerbo and Lombardi proved in [DCL21, Corollary 1.6.] that for a smooth projective $X$ with ample $K_{X}$ and large fundamental group, there exists a normal cover $X^{\prime}$ such that $2 K_{X^{\prime}}$ is very ample. In [DCDC15, Theorem 1.3], Di Cerbo and Di Cerbo also proved an effective result for the multiple of the log canonical bundle $K_{\bar{X}}+D$ of the toroidal compactification of ball quotient: If $m \geq(\mathrm{n}+1)^{3}$, then $m\left(K_{\bar{X}}+D\right)$ is ample modulo $D$.
\item[(iii)] Hwang proved in [Hwa05, Proposition 2.1.] that for a non-compact ball quotient $X$, the sections of the line bundle $\frac{n^{2}+3 n+4}{2} K_{X^{*}}$ separate any two points of Siu-Yau compactification $X^{*}$.
\item[(iv)] For various compact locally symmetric spaces, effective very ampleness has been studied in [HT99, Yeu18, Yeu01, Yeu17, Yeu00, Wan15].
\end{itemize}

Strategy of proof. To prove Theorem A, we decompose $X=\Gamma \backslash \mathbb{B}^{n}$ into two disjoint parts. The first part is the thin neighborhoods around the cusps. This part consists of all points on $X$ which have a displacement less than $\operatorname{sys}(X) / 2$ with respect to a parabolic element in $\Gamma$. The second part is the complement of the first part, which we call the thick part. In Proposition 4.2 we prove that the thick part is not empty. Moreover, We prove in Theorem 4.4 that every subvariety of $\bar{X}$ which is not entirely contained in the boundary $D$ contains a point from the thick part. Therefore, using the inequality proved by Hwang-To we conclude that the volume of a subvariety $V$ of $X$ is controlled by the systole.

To prove Theorem B, the main new ingredient needed is that we show that the uniform depth of cusps is controlled by the systole in Theorem 3.14. Combining this with an inequality proved in [Mem22], it follows that the canonical volume of a subvariety of $\bar{X}$ which intersects with $X$ is also controlled by the systole. The bounds on the degree of a subvariety with
respect to $K_{\bar{X}}$ follow from Theorem A and the previous result of Bakker-Tsimerman in [BT18], which is restated in Theorem 5.4.

\section*{Acknowledgements}

I would like to thank my advisor Jacob Tsimerman for many enlightening discussions and for his comments on an earlier draft of this paper. I also thank Sai-kee Yeung for useful conversations around the effective very ampleness problem. Finally, I am grateful to the anonymous referee for several helpful comments that clarified the text and the proofs in this paper.

\section*{2. Background and notation}

In this section, we collect the necessary background and notation which will be used frequently in the sequel. We refer to [Gol99, Par98, Kap22, BT18] for a much fuller account.
2.1. Geometry of complex ball quotients. The complex unit ball $\mathbb{B}^{n}$ is defined as
$$\mathbb{B}^{n}=\left\{\left.z \in \mathbb{C}^{n}| | z\right|^{2}<1\right\} .$$
The complex ball $\mathbb{B}^{n}$ has an intrinsic Hermitian metric called Bergman metric. The holomorphic isometry group of $\mathbb{B}^{n}$ with respect to this metric is the projective unitary group
$$G:=\mathrm{PU}(n, 1)=\frac{\mathrm{U}(n, 1)}{\mathrm{Z}(\mathrm{U}(n, 1))},$$
where the center $\mathrm{Z}(\mathrm{U}(n, 1))$ can be identified with the circle group $\{\mu I:|\mu|=1\}$. The group $G$ acts transitively on $\mathbb{B}^{n}$ and acts doubly transitively on the boundary sphere $\partial \mathbb{B}^{n}$. The stabilizer of the center of $\mathbb{B}^{n}$ is $\mathrm{U}(n)$. Every isometry $g \in G$ is continuous on the closed ball $\overline{\mathbb{B}^{n}}$ and it follows from Brouwer's fixed point theorem that $g$ has a fixed point on the closed ball $\overline{\mathbb{B}^{n}}$. Moreover, if there is no fixed point on $\mathbb{B}^{n}$, there can be at most two fixed points on the boundary sphere $\partial \mathbb{B}^{n}$. Accordingly, an isometry $g \in G$ is classified as follows:
\begin{itemize}
\item[(i)] Elliptic: $g$ has a fixed point $z$ in $\mathbb{B}^{n}$. After conjugating $g$ via $h \in G$ which sends $z$ to $0, h g h^{-1} \in \mathrm{U}(n)$, and therefore all eigenvalues of $g$ are roots of unity.
\item[(ii)] Parabolic: $g$ has a unique fixed point in $\overline{\mathbb{B}^{n}}$ and this fixed point is on the boundary $\partial \mathbb{B}^{n}$. Equivalently,
$$\inf _{z \in \mathbb{B}^{n}} d(z, g z)=0,$$
where $d(\cdot, \cdot)$ denotes the Bergman metric. This infimum is not realized for a parabolic $g$.
\item[(iii)] Hyperbolic: $g$ has exactly two fixed points in $\overline{\mathbb{B}^{n}}$ and both are in $\partial \mathbb{B}^{n}$. In particular, $g$ preserves the unique geodesic connecting these two fixed points in $\mathbb{B}^{n}$ and acts as a translation along this geodesic. This geodesic is called the axis of $g$. The length of a hyperbolic isometry $g \in G$ is
$$\ell(g):=\inf _{z \in \mathbb{B}^{n}} d(z, g z) .$$
This infimum is not zero and is realized by any point on the axis of $g$. The work of Chen-Greenberg on the conjugacy classification of elements of $\mathrm{U}(n, 1)$ (see [CG74, Theorem 3.4.1]) implies that a hyperbolic isometry $g$ has two eigenvalues $r e^{i \theta}$ and $r^{-1} e^{i \theta}$ with $r>1$ and $n-1$ eigenvalues with norm 1.
\end{itemize}

Let $\Gamma \subset \operatorname{PU}(n, 1)$ be a torsion-free lattice whose parabolic elements are unipotent (Selberg's lemma [Rat06, page 331] tells us that every lattice in $\operatorname{PU}(n, 1)$ has a finite index subgroup with this property). With this property, an element $g \in \Gamma$ is hyperbolic if and only if $g$ is semi-simple. Therefore, we will denote the set of the hyperbolic elements in $\Gamma$ by $\Gamma_{s}$.

Let $X=\Gamma \backslash \mathbb{B}^{n}$. The systole of $X$ is the length of a shortest closed geodesic with respect to the Bergman metric:
$$\operatorname{sys}(X):=\inf _{g \in \Gamma_{s}} \ell(g)=\inf _{g \in \Gamma_{s}}\left\{d(z, g z) \mid z \in \mathbb{B}^{n}\right\} .$$
Equivalently, the systole of $X$ is the length of a shortest hyperbolic element in $\Gamma$. The systole sys $(X)$ is always positive (see Proposition 3.9) and the infimums in (2.1) are attained as minimums (see Remark 3.19).

Consider $x \in X$ with stabilizer $\Gamma_{x}$ in $\Gamma$. Choose a fiber $\tilde{x} \in \mathbb{B}^{n}$. The injectivity radius of $x$ in $X$ is defined to be
$$\operatorname{inj}_{x}(X):=\frac{1}{2} \inf _{\gamma \in \Gamma \backslash \Gamma_{x}} d(\tilde{x}, \gamma \cdot \tilde{x}),$$
which is independent of choice of $\tilde{x}$. The injectivity radius of $X$ is $\operatorname{inj}(X):=\inf _{x \in X} \operatorname{inj}_{x}(X)$. In the case that $X$ is compact, $\Gamma$ only has semi-simple elements and hence $\operatorname{sys}(X)=\operatorname{inj}(X) / 2$. However, this relation does not hold for a non-compact $X$ because of the parabolic elements in $\Gamma$.

Remark 2.1. Since $\operatorname{PU}(n, 1)$ acts on the unit ball $\mathbb{B}^{n}$ by isometries, every lattice $\Gamma$ in $\operatorname{PU}(n, 1)$ acts discontinuously: for every $z \in \mathbb{B}^{n}$ there exists a neighborhood $U$ of $z$ such that
$$\{\gamma \in \Gamma \mid \quad \gamma U \cap U \neq \varnothing\}$$
is finite. This fact is well known to hold for any discrete subgroup of the isometry group, but we will only use it for lattices (see for example [Rat06, Theorem 5.3.5]).
2.2. Siegel domain model. The half-plane model of the 1-dimensional complex ball quotient is generalized by the Siegel domain model in higher dimensions. In horospherical coordinates, the Siegel domain of (complex) dimension $n$ is $\mathbb{S}=\mathbb{C}^{n-1} \times \mathbb{R} \times \mathbb{R}^{+}$. The points of $\mathbb{S}$ are written as $(\zeta, v, u) \in \mathbb{C}^{n-1} \times \mathbb{R} \times \mathbb{R}^{+}$. The boundary of $\mathbb{S}$ is $H_{0} \cup\left\{q_{\infty}\right\}$, where $q_{\infty}$ is a distinguished point at infinity and $H_{0}=\mathbb{C}^{n-1} \times \mathbb{R} \times\{0\}$. The point with coordinates $(0,0,0) \in H_{0}$ will be denoted by $q_{0}$.

To describe the topology of the boundary, we first introduce neighborhoods of $q_{\infty}$. A neighborhood of $q_{\infty}$ is $q_{\infty}$ together with all points $(\zeta, v, u) \in \mathbb{S}$ with $u>\tilde{u}$ for some $\tilde{u}>0$. For a general boundary point $q \in H_{0}$, there exists $g \in \mathrm{PU}(n, 1)$ such that $q=g\left(q_{\infty}\right)$. The neighborhoods of $q$ are then defined as the images under $g$ of neighborhoods of $q_{\infty}$. This construction provides a basis for the topology of the boundary $H_{0} \cup\left\{q_{\infty}\right\}$.

We follow [Par98] in describing $\operatorname{PU}(n, 1)$ via the embedding of the Siegel domain as a paraboloid in $\mathbb{P}\left(\mathbb{C}^{n, 1}\right)$. To do so, we should choose a Hermitian form of signature $(n, 1)$ on $\mathbb{P}\left(\mathbb{C}^{n, 1}\right)$. Let
$$J_{0}:=\left[\begin{array}{ccc}
0 & 0 & 1 \\
0 & I_{n-1} & 0 \\
1 & 0 & 0
\end{array}\right],$$
and $Q(z, w):=w^{*} J_{0} z$, where $z$ and $w$ are column vectors in $\mathbb{P}\left(\mathbb{C}^{n, 1}\right)$ and * is the Hermitian transpose, that is, transpose the matrix and complex conjugate each of its entries.

Consider the map $\psi: \overline{\mathbb{S}} \rightarrow \mathbb{P}\left(\mathbb{C}^{n, 1}\right)$ given by
$$\psi:(\zeta, v, u) \longrightarrow\left[\begin{array}{c}
\frac{1}{2}\left(-\|\zeta\|^{2}-u+i v\right) \\
\zeta \\
1
\end{array}\right], \text { for }(\zeta, v, u) \in \overline{\mathbb{S}} \backslash\left\{q_{\infty}\right\} ; \psi: q_{\infty} \longrightarrow\left[\begin{array}{l}
1 \\
0 \\
0
\end{array}\right] .$$
The image of this map is the set of points in $\mathbb{P}\left(\mathbb{C}^{n, 1}\right)$, where the Hermitian form $Q$ is negative. Also $\psi$ is a homeomorphism of $\partial \mathbb{S}$ onto the set of points where $Q$ is zero.

Let $\mathrm{U}(Q)$ be the unitary group preserving the Hermitian form $Q$ (see [FW09, Section 3]):
$$\mathrm{U}(Q):=\left\{h \in \mathrm{GL}_{n+1}(\mathbb{C}) \mid Q(h z, h w)=Q(z, w) \text { for all } z, w \in \mathbb{C}^{n+1}\right\} .$$
The condition $Q(h z, h w)=Q(z, w)$ is equivalent to $h^{*} J_{0} h=J_{0}$, so $h \in \mathrm{U}(Q)$ if and only if $h^{-1}=J_{0} h^{*} J_{0}$. In particular, $h \in \mathrm{GL}_{n+1}(\mathbb{C})$ lies in $\mathrm{U}(Q)$ if and only if $h$ and its inverse have the form
$$h=\left[\begin{array}{ccc}
a & \tau^{*} & b \\
\alpha & A & \beta \\
c & \delta^{*} & e
\end{array}\right], \quad h^{-1}=\left[\begin{array}{ccc}
\bar{e} & \beta^{*} & \bar{b} \\
\delta & A^{*} & \tau \\
\bar{c} & \alpha^{*} & \bar{a}
\end{array}\right],$$
where $A$ is an $(n-1) \times(n-1)$ matrix, $a, b, c, e \in \mathbb{C}$, and $\tau, \delta, \alpha, \beta$ are column vectors in $\mathbb{C}^{n-1}$ (see [Par98, page 438]) .

The projective unitary group is defined by
$$\mathrm{PU}(Q):=\mathrm{U}(Q) / \mathrm{Z}(\mathrm{U}(Q)),$$
where the center $\mathrm{Z}(\mathrm{U}(Q))$ can be identified with the circle group $\{\mu I:|\mu|=1\}$. Every element of $\operatorname{PU}(Q)$ is represented by a matrix in $\operatorname{U}(Q)$, uniquely determined up to multiplication by a scalar $\mu \in \mathbb{C}$ with $|\mu|=1$.

The holomorphic isometry group of $\mathbb{S}^{n}$ with respect to the Bergman metric is $\operatorname{PU}(Q)$. Its action is given by matrix multiplication of a representative in $\mathrm{U}(Q)$ on the paraboloid model of the Siegel domain, embedded in $\mathbb{P}\left(\mathbb{C}^{n, 1}\right)$ via the map (2.2).

The following lemma easily follows:
Lemma 2.2. Let $\gamma$ be an element of $\operatorname{PU}(Q)$.
\begin{itemize}
\item[(i)] ([Par97, page 7]) If $\gamma$ swaps $q_{\infty}$ and $q_{0}$, then it has a representative $h \in \mathrm{U}(Q)$ of the form
$$h=\left[\begin{array}{ccc}
0 & 0 & 1 / \bar{c} \\
0 & A & 0 \\
c & 0 & 0
\end{array}\right],$$
where $A \in \mathrm{U}(n-1)$ and $c \in \mathbb{C}$. Consequently, $h$ acts on the horospherical coordinates $(\zeta, u, v)$ via:
$$T_{h}:(\zeta, u, v) \longrightarrow\left(\frac{-2 A \zeta}{c\left(\|\zeta\|^{2}+u-i v\right)}, \frac{-4 v}{\left.|c|^{2}| ||\zeta|\right|^{2}+u-\left.i v\right|^{2}}, \frac{4 u}{\left.|c|^{2}| ||\zeta|\right|^{2}+u-\left.i v\right|^{2}}\right) .$$
\item[(ii)] If $\gamma$ fixes both $q_{\infty}$ and $q_{0}$, then it must have a representative $h \in \mathrm{U}(Q)$ of the form
$$h=\left[\begin{array}{ccc}
a & 0 & 0 \\
0 & A & 0 \\
0 & 0 & 1 / \bar{a}
\end{array}\right],$$
where $A \in \mathrm{U}(n-1)$ and $a \in \mathbb{C}$.
\end{itemize}
2.3. Bergman metric. For any pair of points $z_{1}=\left(\zeta_{1}, v_{1}, u_{1}\right)$ and $z_{2}=\left(\zeta_{2}, v_{2}, u_{2}\right)$ in $\mathbb{S}$, the Bergman metric is given by:
$$d\left(z_{1}, z_{2}\right)=2 \cosh ^{-1}\left(\frac{1}{2 \sqrt{u_{1} u_{2}}}\left|\left\|\zeta_{1}-\zeta_{2}\right\|^{2}+u_{1}+u_{2}+i v_{1}-i v_{2}+2 i \operatorname{Im}\left\langle\zeta_{1}, \zeta_{2}\right\rangle\right|\right),$$
where $\langle.,$.$\rangle denotes the standard positive definite Hermitian form on \mathbb{C}^{n-1}$. Since $\cosh ^{-1}(x)$ is increasing, the following lower bound can be obtained for the metric :
$$d\left(\left(\zeta_{1}, v_{1}, u_{1}\right),\left(\zeta_{2}, v_{2}, u_{2}\right)\right) \geq 2 \cosh ^{-1}\left(\frac{\left|u_{1}+u_{2}\right|}{2 \sqrt{u_{1} u_{2}}}\right)$$
The holomorphic sectional curvature of this metric is -1 and the sectional curvature of this metric varies on $\left[-1,-\frac{1}{4}\right]$ (see [Gol99]). It follows that the holomorphic bisectional curvature of this metric is bounded above by $-\frac{1}{2}$ because the holomorphic bisectional curvature always can be written as the sum of two sectional curvatures.
2.4. Toroidal compactification. The complex ball quotient $X$ has a unique toroidal compactification $\bar{X}$, which is a smooth projective variety (see [Mok12]). The boundary divisor of this compactification $D:=\bar{X} \backslash X$ is a disjoint union of abelian varieties with ample conormal bundle. The Kähler form of the Bergman metric on $\mathbb{S}$ is given by
$$\omega_{\mathbb{S}}:=-2 i \partial \bar{\partial} \log (u)$$
(see [BT18, Lemma 2.1]). Let $\omega_{X}$ be the Kähler form induced by the Kähler form $\omega_{\mathbb{S}}$. It follows from Mumford's work on the singular Hermitian metric [Mum77] that the Bergman metric on $X$ extends as a good Hermitian metric to $\bar{X}$. Integration against $\omega_{X}$ on the open part represents (as a current) a multiple of the first Chern class
$$\mathrm{c}_{1}\left(K_{\bar{X}}+D\right)=\frac{1}{2 \pi} \frac{n+1}{2}\left[\omega_{X}\right] \in H^{1,1}(\bar{X}, \mathbb{R}),$$
where $K_{\bar{X}}$ is the canonical bundle of $\bar{X}$ (see [BT18]).
2.5. Stabilizer of cusps. We denote the parabolic stabilizer of $q_{\infty}$ in $G$ by $G_{\infty}$. With our choice of Hermitian form, the matrices corresponding to elements of $G_{\infty}$ are upper triangular. There is an equivalent way to identify these matrices:

Lemma 2.3. ([Par98]) Let $\gamma$ be an element of $\operatorname{PU}(Q)$. Let $h \in \mathrm{U}(Q)$ be a representative of $\gamma$ written in the form (2.4). Then, $\gamma$ fixes $q_{\infty}$ if and only if the $c$ entry of $h$ is 0.

Proof. Note that
$$h \cdot q_{\infty}=\left[\begin{array}{ccc}
a & \tau^{*} & b \\
\alpha & A & \beta \\
c & \delta^{*} & e
\end{array}\right]\left[\begin{array}{l}
1 \\
0 \\
0
\end{array}\right]=\left[\begin{array}{l}
a \\
\alpha \\
c
\end{array}\right],$$
and therefore $\gamma$ fixes $q_{\infty}$ projectively if and only if $c=0$ and $\alpha=0$. Note that if the $c$ entry of $h$ is 0, the multiplication of the matrix of $h$ and $h^{-1}$ in the form (2.4) yields that $\alpha$ (and also $\delta$ ) must be 0. \(\square\)

The group $G_{\infty}$ is generated by Heisenberg isometries $I_{\infty}$ and a one-dimensional torus $T$. Heisenberg isometries consist of Heisenberg Rotations $\mathrm{U}(n-1)$ and Heisenberg translations $\mathfrak{N}$. Heisenberg Rotations $\mathrm{U}(n-1)$ act on $\zeta$-coordinates of $\mathbb{S}$ in the usual way, namely by linear isometries preserving the standard Hermitian form. Heisenberg translations $\mathfrak{N} \cong \mathbb{C}^{n-1} \times \mathbb{R}$ act on $\zeta$ and $v$ coordinates of $\mathbb{S}$ via
$$(\tau, t):(\zeta, v, u) \longrightarrow(\zeta+\tau, v+t+2 i \operatorname{Im}\langle\tau, \zeta\rangle, u) .$$

The element $(0, t) \in \mathfrak{N}$ will be called the vertical translation by $t$, and the subgroup of $G_{\infty}$ generated by vertical translations, which is isomorphic to $\mathbb{R}$, will be denoted by $V_{\infty}$. The vertical translation $V_{\infty}$ is the center of $G_{\infty}$ and the quotient $V_{\infty} \backslash I_{\infty}$ is isomorphic to the group of unitary transformations of $\mathbb{C}^{n-1}$.

A Heisenberg translation $(\tau, t) \in \mathfrak{N}$ fixing $q_{\infty}$ has a representative $g_{\infty} \in \mathrm{U}(Q)$ and a Heisenberg translation $(\sigma, s) \in \mathfrak{N}$ fixing $q_{0}$ has a representative $g_{0} \in \mathrm{U}(Q)$, where
$$g_{\infty}=\left[\begin{array}{ccc}
1 & -\tau^{*} & -(|\tau|+i t) / 2 \\
0 & I & \tau \\
0 & 0 & 1
\end{array}\right], \quad g_{0}=\left[\begin{array}{ccc}
1 & 0 & 0 \\
\sigma & I & 0 \\
-(|\sigma|+i s) / 2 & -\sigma^{*} & 1
\end{array}\right] .$$
With our assumption on $\Gamma$, all parabolic stabilizers of $q_{\infty}$ in $\Gamma$, i.e., $\Gamma_{\infty}:=\Gamma \cap G_{\infty}$ are Heisenberg translations.

The following statement is classical, but we include it here for completeness.
Lemma 2.4. The group $\Gamma_{\infty}$ contains a shortest vertical translation.
Proof. Note that the group of Heisenberg translations is $\mathfrak{N} \cong \mathbb{C}^{n-1} \times \mathbb{R}$. When $n=1$, all Heisenberg translations are vertical, so we may assume $n \geq 2$. If $g_{1}=\left(\tau_{1}, t_{1}\right)$ and $g_{2}=\left(\tau_{2}, t_{2}\right)$, then their product in the Heisenberg translation is $g_{1} g_{2}=\left(\tau_{1}+\tau_{2}, t_{1}+t_{2}+\right.$ $\left.2 \operatorname{Im}\left\langle\tau_{1}, \tau_{2}\right\rangle\right)$. Therefore, their commutator is $\left[g_{1}, g_{2}\right]=\left(0,4 \operatorname{Im}\left\langle\tau_{1}, \tau_{2}\right\rangle\right)$, which is a vertical translation. Note that Heisenberg translations form a non-abelian (2-step nilpotent) group when $n \geq 2$. Since $\Gamma_{\infty}$ must contain $2 n-1$ generators, it necessarily contains nontrivial commutators, which correspond to vertical translations.

Moreover, because the lattice is discrete, there exists a neighborhood of the identity containing no nontrivial lattice elements. This implies the existence of a shortest nontrivial vertical translation in the parabolic stabilizer. \(\square\)

The following fact is also well known, but we include a proof for completeness:
Lemma 2.5. There is no hyperbolic element of $\Gamma$ fixing $q_{\infty}$.
Proof. Suppose there exists a hyperbolic element $h \in \Gamma$ fixing $q_{\infty}$. Let $g$ be a vertical translation fixing $q_{\infty}$. Using (2.4), Lemma 2.3 and (2.9), we can choose representatives $\widetilde{h}$ and $\widetilde{g}$ of $h$ and $g$ in $\mathrm{U}(Q)$ given by
$$\widetilde{g}=\left[\begin{array}{ccc}
1 & 0 & -i t / 2 \\
0 & I & 0 \\
0 & 0 & 1
\end{array}\right], \quad \widetilde{h}=\left[\begin{array}{ccc}
a & \tau^{*} & b \\
0 & A & \beta \\
0 & 0 & e
\end{array}\right], \quad \widetilde{h}^{-1}=\left[\begin{array}{ccc}
\bar{e} & \beta^{*} & \bar{b} \\
0 & A^{*} & \tau \\
0 & 0 & \bar{a}
\end{array}\right],$$
where $t \in \mathbb{R}, A$ is an $(n-1) \times(n-1)$ matrix, $a, b, e \in \mathbb{C}$, and $\tau, \beta$ are column vectors in $\mathbb{C}^{n-1}$. Since $\widetilde{h}$ and $\widetilde{h}^{-1}$ are inverses, we have $a \bar{e}=1$, and as $h$ is hyperbolic, $|a| \neq 1$. A direct
computation shows that for every $m \in \mathbb{Z}$,
$$\widetilde{h}^{m} \widetilde{g} \widetilde{h}^{-m}=\left[\begin{array}{ccc}
1 & 0 & -i|a|^{m} t / 2 \\
0 & I & 0 \\
0 & 0 & 1
\end{array}\right],$$
so that if $|a|>1$ taking $m \rightarrow \infty$ (or if $|a|<1$ taking $m \rightarrow-\infty$ ) leads to $\widetilde{h}^{m} \widetilde{g} \widetilde{h}^{-m} \rightarrow I$, contradicting the fact that $\Gamma$ is discrete. \(\square\)
2.6. Neighborhood of cusps. A horoball centered at $q_{\infty}$ with height $\tilde{u}$ is the open set
$$B_{\infty}(\tilde{u}):=\{(\zeta, v, u) \in \mathbb{S} \mid u>\tilde{u}\} .$$
The height coordinate $u$ on $\mathbb{S}$ is invariant under the action of Heisenberg rotations $\mathrm{U}(n-1)$ and Heisenberg translations $\mathfrak{N}$, and hence the horoball is invariant under these groups.

Two points on $\partial \mathbb{S}$ are considered equivalent if they lie in the same $\Gamma$-orbit. A cusp of $X$ is the equivalence class of a point on $\partial \mathbb{S}$ fixed by a parabolic element of $\Gamma$. Thus, the cusps of $X$ are in one-to-one correspondence with the $\Gamma$-orbits of parabolic fixed points on $\partial \mathbb{S}$.

The complex ball quotient $X$ has finitely many cusps, and every cusp of $X$ can, possibly after a change of coordinates, be represented by the equivalence class of $q_{\infty}$. More precisely, if a cusp corresponds to the class of another point on $\partial \mathbb{S}$, the transitivity of the action of $\operatorname{PU}(n, 1)$ on the boundary allows us to move that point to $q_{\infty}$, which amounts to replacing $\Gamma$ by its conjugate in $\operatorname{PU}(n, 1)$.

Let $c_{i}$ be a cusp of $X$ corresponding to the equivalence class of $q_{\infty}$, and let $\Gamma_{i} \subset \Gamma$ denote the parabolic stabilizer of $c_{i}$. The smallest $\tilde{u}$ such that
$$\Gamma_{i} \backslash B_{\infty}(\tilde{u})$$
injects into $X$ is called the height of the cusp $c_{i}$, denoted by $u_{i}$. By Parker's generalization of Shimizu's lemma [Par98], for sufficiently large $\tilde{u}$ the set $\Gamma_{i} \backslash B_{\infty}(\tilde{u})$ injects into $X$. With our identification of $c_{i}$ with the $\Gamma$-orbit of $q_{\infty}$, we have $\Gamma_{i}=\Gamma_{\infty}$. For every $\tilde{u}<u_{i}$, the horoball around the cusp $c_{i}$ with height $\tilde{u}$ is defined as
$$B_{i}(\tilde{u}):=\Gamma_{i} \backslash B_{\infty}(\tilde{u}) .$$

Let $t_{i}$ be the length of a shortest vertical translation in $\Gamma_{i}$ (see Lemma 2.4). The number $d_{i}=t_{i} / u_{i}$ is called the depth of the cusp $c_{i}$. Note that this quantity is invariant under conjugating $\Gamma$, and hence is well-defined independently of the choice of coordinates.

Definition 2.6. ([BT18, Definition 3.7.]) The uniform depth of the cusps of $X$ is the largest $d$ satisfying the following properties:
\begin{itemize}
\item[(i)] for every $i, d \leq d_{i}$ (this gives that $\Gamma_{i} \backslash B_{i}\left(t_{i} / d\right)$ injects into $X$ ).
\item[(ii)] all $\Gamma_{i} \backslash B_{i}\left(t_{i} / d\right)$ are pairwise disjoint.
\end{itemize}

\section*{3. Systole and depth of cusps}

Let $X=\Gamma \backslash \mathbb{B}^{n}$, where $\Gamma \subset \operatorname{PU}(n, 1)$ is a torsion-free lattice whose parabolic stabilizers are unipotent. In this section we frequently use the content and notation introduced in section 2. The main goal of this section is to prove Theorem 3.14, where we show that the systole $\operatorname{sys}(X)$ bounds the uniform depth of cusps $d$ of $X$ from below.

To see the relation between the systole and depth of cusps, we first prove that the length of a hyperbolic element in $\Gamma$ only depends on its non-unit eigenvalues:
Proposition 3.1. Suppose $h \in \Gamma$ is a hyperbolic element. Let $\hat{h} \in \mathrm{U}(Q)$ be a representative of $h$ with non-unit eigenvalues $r e^{i \theta}$ and $r^{-1} e^{i \theta}$. Then,
$$\ell(h)=2|\ln (r)| .$$
Proof. Since $h$ is hyperbolic, it fixes two distinct points $x_{1}$ and $x_{2}$ on the boundary $\partial \mathbb{S}$. As $\mathrm{PU}(Q)$ acts doubly transitive on the boundary, there exists $P \in \mathrm{PU}(Q)$ such that $P\left(x_{1}\right)=q_{0}$ and $P\left(x_{2}\right)=q_{\infty}$. Now we can write
$$d(x, h x)=d\left(P x, P h P^{-1} P x\right)=d\left(x^{\prime}, P h P^{-1} x^{\prime}\right),$$
where $x^{\prime}=P x$. Suppose $x^{\prime}=\left(\zeta_{1}, v_{1}, u_{1}\right)$, and $\operatorname{Ph} P^{-1} x^{\prime}=\left(\zeta_{2}, v_{2}, u_{2}\right)$. Since $\operatorname{Ph} P^{-1}$ fixes both $q_{0}$ and $q_{\infty}$, it follows from Lemma 2.2 that it has a representative $\widetilde{h} \in \mathrm{U}(Q)$ such that
$$\widetilde{h}=\left[\begin{array}{ccc}
a & 0 & 0 \\
0 & A & 0 \\
0 & 0 & 1 / \bar{a}
\end{array}\right],$$
for a complex number $a$ and $A \in \mathrm{U}(n-1)$. Therefore, in horospherical coordinates, using the map (2.2), we obtain the following:
$$\widetilde{h} \cdot x^{\prime}=\left[\begin{array}{ccc}
a & 0 & 0 \\
0 & A & 0 \\
0 & 0 & 1 / \bar{a}
\end{array}\right]\left[\begin{array}{c}
\frac{1}{2}\left(-\left\|\zeta_{1}\right\|^{2}-u_{1}+i v_{1}\right) \\
\zeta_{1} \\
1
\end{array}\right]=\left[\begin{array}{c}
\frac{a}{2}\left(-\left\|\zeta_{1}\right\|^{2}-u_{1}+i v_{1}\right) \\
A \zeta_{1} \\
1 / \bar{a}
\end{array}\right] .$$
This gives $\zeta_{2}=\bar{a} A \zeta_{1}$ and
$$\frac{1}{2}\left(-\left\|\zeta_{2}\right\|^{2}-u_{2}+i v_{2}\right)=\frac{|a|^{2}}{2}\left(-\left\|\zeta_{1}\right\|^{2}-u_{1}+i v_{1}\right) .$$
Therefore, $u_{2}=|a|^{2} u_{1}$ and $v_{2}=|a|^{2} v_{1}$. Note that as conjugation does not change the eigenvalues, we have that $|a|^{2}=r^{2}$ or $\frac{1}{r^{2}}$. On the other hand, inequality (2.6) yields that
$$\begin{aligned}
d\left(x^{\prime}, P h P^{-1} x^{\prime}\right) & \geq 2 \cosh ^{-1}\left(\frac{\left|u_{1}+u_{2}\right|}{2 \sqrt{u_{1} u_{2}}}\right) \\
& \geq 2 \cosh ^{-1}\left(\frac{1}{2}\left(r+\frac{1}{r}\right)\right) .
\end{aligned}$$

Since this lower bound is realized at $\zeta_{1}=0, v_{1}=0$, and $\cosh ^{-1}\left(\frac{1}{2}\left(r+\frac{1}{r}\right)\right)=|\ln (r)|$, we can conclude that the equality holds. \(\square\)

Definition 3.2. Let $\gamma \in \Gamma \subset \operatorname{PU}(Q)$ and choose a lift $\widetilde{\gamma} \in \operatorname{U}(Q)$ representing it.
\begin{itemize}
\item[(i)] The absolute trace of $\gamma$ is defined as
$$|\operatorname{tr}(\gamma)|:=|\operatorname{tr}(\widetilde{\gamma})| .$$
\item[(ii)] The absolute $c$-entry of $\gamma$ is defined as the absolute value of the lower-left entry of the matrix $\widetilde{\gamma}$, written in the form (2.4).
\end{itemize}

Both notions are well-defined, since any two lifts differ by a scalar in U(1), which does not affect the absolute value of either the trace or the $c$-entry. For $\gamma \notin \Gamma_{\infty}$, we know by Lemma 2.3 that the absolute $c$-entry cannot be zero.

Definition 3.3. For a torsion-free lattice $\Gamma \subset \operatorname{PU}(Q)$, we call the infimum of the absolute $c$-entries (see Definition 3.2 (ii)) among all $\gamma \in \Gamma \backslash \Gamma_{\infty}$ the infimum $c$-entry of $\Gamma$, and we denote it by $c_{\text {inf }}$.

Parker's generalization of Shimizu's lemma gives the following:
Remark 3.4. By [Par98, Theorem 2.3], one has $c_{\text {inf }}>\frac{4}{t_{\infty}}$, where $t_{\infty}$ is the length of a shortest vertical translation fixing $q_{\infty}$.

Lemma 3.5. Let $\gamma \in \operatorname{PU}(Q)$ be a hyperbolic element. Then
$$\ell(\gamma) \geq 2 \ln \left(\frac{1}{2}(|\operatorname{tr}(\gamma)|-n+1)\right) .$$
Proof. Let $\widetilde{\gamma}$ be any lift of $\gamma$ to $\mathrm{U}(Q)$. Suppose $r e^{i \theta}$ and $r^{-1} e^{i \theta}$ are the non-unit eigenvalues of $\widetilde{\gamma}$ with $r>1$. Since $\widetilde{\gamma}$ has $n-1$ remaining eigenvalues, all of which are units, we obtain
$$2 r \geq r+\frac{1}{r} \geq|\operatorname{tr}(\widetilde{\gamma})|-n+1 .$$
Finally, since $|\ln (x)|$ is increasing for $x>1$, we conclude from Proposition 3.1 that the desired inequality holds. \(\square\)

Lemma 3.5 tells us that if for every hyperbolic element $\gamma \in \Gamma$ the quantity $|\operatorname{tr}(\gamma)|$ is sufficiently large, then the systole sys( $X$ ) will also be large; in other words, the systole $\operatorname{sys}(X)$ can be estimated by estimating the absolute values of the traces of hyperbolic elements (see Proposition 3.22 for an example of this estimation).

We recall a lemma from Parker's version of Shimizu's lemma:
Lemma 3.6. (see [Par98, Lemma 2.6]) Let $g_{\infty}=(0, t)$ be a vertical translation fixing $q_{\infty}$ and let $h$ be an element of $\operatorname{PU}(Q)$ whose absolute $c$-entry is $c_{h}$. Then,
$$\left|\operatorname{tr}\left[g_{\infty}, h\right]\right|=n+1+\frac{1}{4}\left|c_{h} t\right|^{2} .$$
Proof. Let $\widetilde{g}$ and $\widetilde{h}$ be representatives of $g_{\infty}$ and $h$ in $\mathrm{U}(Q)$, given by
$$\widetilde{g}=\left[\begin{array}{ccc}
1 & 0 & -i \frac{t}{2} \\
0 & I & 0 \\
0 & 0 & 1
\end{array}\right], \widetilde{h}=\left[\begin{array}{ccc}
a & \tau^{*} & b \\
\alpha & A & \beta \\
c & \delta^{*} & e
\end{array}\right], \widetilde{h}^{-1}=\left[\begin{array}{ccc}
\bar{e} & \beta^{*} & \bar{b} \\
\delta & A^{*} & \tau \\
\bar{c} & \alpha^{*} & \bar{a}
\end{array}\right],$$
where (2.4) was used to find the inverse of $\widetilde{h}$, and necessarily $|c|=c_{h}$. As noted after the definition of the absolute trace (3.2), to compute $\left|\operatorname{tr}\left[g_{\infty}, h\right]\right|$ it suffices to evaluate $|\operatorname{tr}[\widetilde{g}, \widetilde{h}]|$ (it does not depend on the choice of representatives).

To find $|\operatorname{tr}[\widetilde{g}, \widetilde{h}]|$, note that
$$\widetilde{g} \widetilde{h}=\left[\begin{array}{ccc}
a-\frac{i}{2} c t & \tau^{*}-\frac{i}{2} t \delta^{*} & b-\frac{i}{2} t e \\
\alpha & A & \beta \\
c & \delta^{*} & e
\end{array}\right], \widetilde{g}^{-1} \widetilde{h}^{-1}=\left[\begin{array}{ccc}
\bar{e}+\frac{i}{2} \bar{c} t & \beta^{*}+\frac{i}{2} t \alpha^{*} & \bar{b}+\frac{i}{2} t \bar{a} \\
\delta & A^{*} & \tau \\
\bar{c} & \alpha^{*} & \bar{a}
\end{array}\right] .$$

Therefore, using the relation given by equation (2.4) it follows that
$$\begin{aligned}
\operatorname{tr}[\widetilde{g}, \widetilde{h}]= & a \bar{e}+\frac{1}{4}|c t|^{2}-\frac{i t}{2}(c \bar{e}-\bar{c} a)+\delta \tau^{*}-\frac{i}{2} t|\delta|^{2}+b \bar{c}-\frac{i}{2} t e \bar{c} \\
& +\alpha \beta^{*}+\frac{i}{2} t|\alpha|^{2}+A A^{*}+\beta \alpha^{*}+c \bar{b}+\frac{i}{2} t \bar{a} c+\delta^{*} \tau+e \bar{a} \\
= & n+1+\frac{1}{4}|c t|^{2} .
\end{aligned}$$ \(\square\)

We prove a lemma which will help us to see the relation between the depth of a cusp in terms of the trace of the hyperbolic elements in $\Gamma$ :

Lemma 3.7. Let $\gamma \in \Gamma \backslash \Gamma_{\infty}$ have absolute $c$-entry $c_{\gamma}$. For every $z \in \mathbb{S}$ the following inequality holds:
$$u(z) u(\gamma \cdot z) \leq \frac{4}{\left|c_{\gamma}\right|^{2}} .$$
Proof. There are unique Heisenberg transformations $h_{1}, h_{2}$ such that $h_{1}\left(q_{0}\right)=\gamma\left(q_{\infty}\right)$ and $h_{2}^{-1}\left(q_{0}\right)=\gamma^{-1}\left(q_{\infty}\right)$. Consider $\hat{\gamma}=h_{1}^{-1} \gamma h_{2}^{-1}$ and note that as the Heisenberg translations are stabilizers of the $u$-coordinate, we have that $u(\gamma z)=u(\hat{\gamma} z)$. Because both $h_{1}^{-1}$ and $h_{2}^{-1}$ fix $q_{\infty}$, it follows from Lemma 2.3 that the absolute $c$-entries of $\gamma$ and $\hat{\gamma}$ coincide. Moreover, since both $h_{1}^{-1}$ and $h_{2}^{-1}$ fix $q_{\infty}$, the element $\hat{\gamma}$ swaps $q_{\infty}$ and $q_{0}$. Therefore, Lemma 2.2 tells us that $\hat{\gamma}$ has a representative $\tilde{\gamma} \in \mathrm{U}(Q)$ such that its acts on the horospherical coordinates $(\zeta, u, v)$ via:
$$T_{\tilde{\gamma}}:(\zeta, v, u) \longrightarrow\left(\frac{A \zeta r_{\gamma}^{2}}{\|\zeta\|^{2}+u-i v}, \frac{-v r_{\gamma}^{4}}{\left|\|\zeta\|^{2}+u-i v\right|^{2}}, \frac{u r_{\gamma}^{4}}{\left|\|\zeta\|^{2}+u-i v\right|^{2}}\right),$$
where $A \in \mathrm{U}(n-1)$ and $r_{\tilde{\gamma}}=\sqrt{\frac{2}{\left|c_{\gamma}\right|}}$. This gives that
$$u(z) u(\gamma \cdot z)=u(z) u(\tilde{\gamma} \cdot z)=\frac{u^{2}}{\|\left.|\zeta|\right|^{2}+u-\left.i v\right|^{2}} \cdot\left|\frac{2}{c_{\gamma}}\right|^{2} \leq \frac{4}{\left|c_{\gamma}\right|^{2}} .$$ \(\square\)

Lemma 3.7 implies the following:
Proposition 3.8. Let $c_{\text {inf }}$ be the infimum of the absolute values of the $c$-entries of $\Gamma$, as defined in Definition 3.3. The horoball $B_{\infty}\left(2 / c_{\text {inf }}\right)$ injects into $X$, and therefore the depth of a cusp associated with the equivalence class of $q_{\infty}$ is at least $\frac{t_{\infty} \cdot c_{\text {inf }}}{2}$.

Proof. Let $\gamma \in \Gamma \backslash \Gamma_{\infty}$, and consider the horoball centered at $q_{\infty}$ with height $2 / c_{\text {inf }}$ :
$$U_{\infty}=\left\{z \in \mathbb{S} \left\lvert\, u(z)>\frac{2}{\left|c_{\mathrm{inf}}\right|}\right.\right\} .$$
By Lemma 3.7, for every $z \in \mathbb{S}$ we have
$$u(z) u(\gamma \cdot z) \leq \frac{4}{\left|c_{\text {inf }}\right|^{2}} .$$

Hence, the sets $U_{\infty}$ and $\gamma U_{\infty}$ are disjoint. This implies that the horoball $B_{\infty}\left(2 / c_{\text {inf }}\right)=$ $\Gamma_{\infty} \backslash U_{\infty}$ injects into $X$. By the definition of the depth of a cusp, the depth of the cusp associated with the equivalence class of $q_{\infty}$ is at least $\frac{t_{\infty} \cdot c_{\text {inf }}}{2}$. \(\square\)

Now we will show that the systole is always positive:
Proposition 3.9. The systole, as defined in (2.1), is always positive.
Proof. Suppose not. Then there would exist a sequence of hyperbolic elements $\left\{h_{m}\right\}_{m=1}^{\infty}$ in $\Gamma$ such that $\ell\left(h_{m}\right) \rightarrow 0$ as $m \rightarrow \infty$. Let $r_{m} e^{i \theta_{m}}$ be the eigenvalue of a representative of $h_{m}$ in $\mathrm{U}(Q)$ with $r_{m}>1$. It follows from Proposition 3.1 that $r_{m} \rightarrow 1$ as $m \rightarrow \infty$. By the definition of the infimum, there exists $z_{m} \in \mathbb{B}^{n}$ such that
$$d\left(z_{m}, h_{m} \cdot z_{m}\right) \leq \ell\left(h_{m}\right)+\frac{1}{m} .$$
Therefore $d\left(z_{m}, h_{m} \cdot z_{m}\right) \rightarrow 0$ as $m \rightarrow \infty$. Since $\overline{\mathbb{B}^{n}}$ is compact, there exists a subsequence of $\left\{z_{m}\right\}_{m=1}^{\infty}$, again denoted by $\left\{z_{m}\right\}_{m=1}^{\infty}$, which converges to a point $z \in \overline{\mathbb{B}^{n}}$. By the triangle inequality,
$$d\left(z, h_{m} \cdot z\right) \leq d\left(z, z_{m}\right)+d\left(z_{m}, h_{m} \cdot z_{m}\right)+d\left(h_{m} \cdot z_{m}, h_{m} \cdot z\right),$$
and since $d\left(h_{m} \cdot z_{m}, h_{m} \cdot z\right)=d\left(z_{m}, z\right)$, we get $d\left(z, h_{m} \cdot z\right) \rightarrow 0$ as $m \rightarrow \infty$.
Now consider two cases:
\begin{itemize}
\item[(i)] $z \in \mathbb{B}^{n}$ : In this case, the set $\left\{h_{m} \cdot z\right\}_{m=1}^{\infty}$ has an accumulation point in the interior of the unit ball, contradicting the fact that $\Gamma$ acts discontinuously on $\mathbb{B}^{n}$ (see Remark 2.1).
\item[(ii)] $z \in \partial \mathbb{B}^{n}$ : Since $\operatorname{PU}(n, 1)$ acts transitively on the boundary, there exists $g \in \operatorname{PU}(n, 1)$ such that $g \cdot z=q_{\infty}$. Consider the sequences $\left\{h_{m}^{\prime}:=g h_{m} g^{-1}\right\}$ in the lattice $g \Gamma g^{-1}$ and set $z_{m}^{\prime}:=g \cdot z_{m}$. Note that $z_{m}^{\prime} \rightarrow q_{\infty}$ and $d\left(z_{m}^{\prime}, h_{m}^{\prime} \cdot z_{m}^{\prime}\right) \rightarrow 0$ as $m \rightarrow \infty$; hence, $u\left(z_{m}^{\prime}\right) \rightarrow \infty$ and $u\left(h_{m}^{\prime} \cdot z_{m}^{\prime}\right) \rightarrow \infty$. Let $c_{m}$ be the absolute $c$-entry of $h_{m}^{\prime}$. Note that Lemma 2.5 tells us that every non-identity element in a cusp stabilizer is parabolic, therefore, none of the $h_{m}^{\prime}$ fixes $q_{\infty}$. By Lemma 2.3, we have $c_{m} \neq 0$, and by Remark 3.4, $c_{m} \geq 4 / t_{\infty}$ for all $m$, where $t_{\infty}$ is the length of a shortest vertical translation around $q_{\infty}$. Then Lemma 3.7 gives
$$u\left(z_{m}^{\prime}\right) u\left(h_{m}^{\prime} \cdot z_{m}^{\prime}\right) \leq \frac{4}{\left|c_{m}\right|^{2}} \leq \frac{t_{\infty}}{4} .$$
This inequality contradicts the fact that both $u\left(z_{m}^{\prime}\right)$ and $u\left(h_{m}^{\prime} \cdot z_{m}^{\prime}\right)$ tend to infinity as $m \rightarrow \infty$.
\end{itemize} \(\square\)

Consider the set
$$S_{\Gamma}:=\{\gamma \in \Gamma \| \operatorname{tr}(\gamma) \mid>n+1\},$$
associated to $\Gamma$. It follows from the classification of isometries that if $\gamma \in \Gamma$ has $|\operatorname{tr}(\gamma)|>n+1$, then $\gamma$ must be hyperbolic. Hence, all elements of $S_{\Gamma}$ are hyperbolic. Also note that Lemma 3.6 tells us that $S_{\Gamma}$ is not empty. We associate the number
$$\lambda_{\Gamma}:=\inf _{\gamma \in S_{\Gamma}}|\operatorname{tr}(\gamma)|,$$
to $\Gamma$. Since $S_{\Gamma}$ is nonempty, it follows that $\lambda_{\Gamma} \geq n+1$. The quantity $\lambda_{\Gamma}$ will play a role as an intermediate quantity to relate the systole of $X$ to the depth of cusps of $X$. Specifically, we can see how $\operatorname{sys}(X)$ gives a lower bound for $\lambda_{\Gamma}$ :

Proposition 3.10. The following inequality holds: $\lambda_{\Gamma}>1-n+e^{\operatorname{sys}(X) / 2}$.
Proof. Consider $\gamma \in S_{\Gamma}$. Let $\widetilde{\gamma}$ be a representative of $\gamma$ in $\mathrm{U}(Q)$. Let $r e^{i \theta}$ and $r^{-1} e^{i \theta}$ be eigenvalues of $\widetilde{\gamma}$ which are not units. As sys $(X)$ is the length of a shortest geodesic, Proposition 3.1 implies that $2|\ln (r)| \geq \operatorname{sys}(X)$. Since the other $n-1$ eigenvalues of $\widetilde{\gamma}$ have norm 1, the desired inequality follows from the triangle inequality. \(\square\)

Now, we can show the relation between the quantity $\lambda_{\Gamma}$ and depth of each cusps of $X$ :
Proposition 3.11. The depth of each cusp of $X=\Gamma \backslash \mathbb{B}^{n}$ is at least $\sqrt{\lambda_{\Gamma}-n-1}$.
Proof. Since both the depth of cusps and $\lambda_{\Gamma}$ are invariant under the conjugation by an element of $\operatorname{PU}(n, 1)$, it is sufficient to prove the lemma for a cusp $c_{i}$ associated with the equivalence class of $q_{\infty}$. Let $g_{\infty}=\left(0, t_{\infty}\right)$ be a shortest vertical translation in $\Gamma_{\infty}$. Suppose that $h \in \Gamma$ is an element which does not fix $q_{\infty}$. Let $c$ be the absolute $c$-entry of $h$, which is not zero by Lemma 2.3. It follows from Lemma 3.6 that
$$\left|\operatorname{tr}\left[g_{\infty}, h\right]\right|=n+1+\left|\frac{t_{\infty} c}{2}\right|^{2} .$$
Since $c \neq 0$, we have that $\left[g_{\infty}, h\right] \in S_{\lambda}$. This implies that
$$\left|\frac{t_{\infty} c}{2}\right| \geq \sqrt{\lambda_{\Gamma}-n-1} .$$
Since this inequality holds for every $h \in \Gamma \backslash \Gamma_{\infty}$, we can conclude that
$$\left|\frac{t_{\infty} c_{\mathrm{inf}}}{2}\right| \geq \sqrt{\lambda_{\Gamma}-n-1} .$$
Hence, Proposition 3.8 implies $d_{i} \geq \sqrt{\lambda_{\Gamma}-n-1}$, where $d_{i}$ is the depth of cusp $c_{i}$. \(\square\)

To pass from the individual depth of cusps to the uniform depth of cusps we will use this lemma:

Lemma 3.12. ([Par98, Lemma 2.5]) Let $B_{0}\left(\tilde{u}_{0}\right)$ be the horoball of height $\tilde{u}_{0}$ based at $q_{0}$, and let $B_{\infty}\left(\tilde{u}_{\infty}\right)$ be the horoball of height $\tilde{u}_{\infty}$ based at $q_{\infty}$. These two horoballs are disjoint if and only if
$$\tilde{u}_{0} \cdot \tilde{u}_{\infty} \geq 4 .$$

Proposition 3.13. Let $d$ be the uniform depth of cusps of $X$. Then,
$$d \geq \min \left\{\left(\lambda_{\Gamma}-n-1\right)^{\frac{1}{4}},\left(\lambda_{\Gamma}-n-1\right)^{\frac{1}{2}}\right\} .$$
Proof. Let $d^{\prime}=\min \left\{\left(\lambda_{\Gamma}-n-1\right)^{\frac{1}{4}},\left(\lambda_{\Gamma}-n-1\right)^{\frac{1}{2}}\right\}$. We will show that the horoballs $\Gamma_{i} \backslash B_{i}\left(t_{i} / d^{\prime}\right)$ inject into $X$ and they are disjoint. Since the uniform depth of cusps is the largest number satisfying these properties, the claim follows.

By Proposition 3.11 we know that the depth of each cusp is at least $\left(\lambda_{\Gamma}-n-1\right)^{\frac{1}{2}}$, therefore the horoballs $\Gamma_{i} \backslash B\left(t_{i} / d^{\prime}\right)$ inject into $X$. Hence, it is enough to show that for $i \neq j$, the horoballs $\Gamma_{i} \backslash B\left(t_{i} / d^{\prime}\right)$ and $\Gamma_{j} \backslash B\left(t_{j} / d^{\prime}\right)$ are disjoint.

Since $\operatorname{PU}(Q)$ acts doubly transitively on the boundary, we can, with a change of coordinates if necessary (i.e., by conjugating the lattice), assume that $q_{i}=q_{\infty}$ and $q_{j}=q_{0}$. Note that as both $\lambda_{\Gamma}$ and $d$ are invariant under conjugation, this change of coordinates does not change them. Let $g_{0}=\left(0, t_{0}\right)$ be the shortest vertical translation based at $q_{0}$ with $t_{0}>0$ and $g_{\infty}=\left(0, t_{\infty}\right)$ be the shortest vertical translation based at $q_{\infty}$ with $t_{\infty}>0$. Let $\widetilde{g}_{\infty}$ and $\widetilde{g}_{0}$ be the representatives of $g_{\infty}$ and $g_{0}$ in $\mathrm{U}(Q)$ written in the form (2.9):
$$\widetilde{g}_{0}=\left[\begin{array}{ccc}
1 & 0 & 0 \\
0 & I & 0 \\
-i t_{0} / 2 & 0 & 1
\end{array}\right], \quad \widetilde{g}_{\infty}=\left[\begin{array}{ccc}
1 & 0 & -i t_{\infty} / 2 \\
0 & I & 0 \\
0 & 0 & 1
\end{array}\right] .$$
Lemma 3.6 implies that $\left|\operatorname{tr}\left[g_{\infty}, g_{0}\right]\right|=n+1+\left|\frac{t_{0} t_{\infty}}{4}\right|^{2}$. Therefore, $\left[g_{\infty}, g_{0}\right] \in S_{\lambda}$ and it follows that
$$t_{0} t_{\infty} \geq 4 \sqrt{\lambda_{\Gamma}-n-1} .$$
Consider $\tilde{u}_{0}:=\frac{t_{0}}{\left(\lambda_{\Gamma}-n-1\right)^{\frac{1}{4}}}$ and $\tilde{u}_{\infty}:=\frac{t_{\infty}}{\left(\lambda_{\Gamma}-n-1\right)^{\frac{1}{4}}}$. The inequality above implies that
$$\tilde{u}_{0} \cdot \tilde{u}_{\infty} \geq 4,$$
and therefore it follows from Lemma 3.12 that the horoball centered at $q_{0}$ with height $\tilde{u}_{0}$ and the horoball centered at $q_{\infty}$ with height $\tilde{u}_{\infty}$ are disjoint. Therefore, since $d^{\prime} \leq\left(\lambda_{\Gamma}-n-1\right)^{\frac{1}{4}}$, the horoballs $\Gamma_{i} \backslash B\left(t_{i} / d^{\prime}\right)$ and $\Gamma_{j} \backslash B\left(t_{j} / d^{\prime}\right)$ are disjoint. \(\square\)

We finally conclude that the systole gives a lower bound for the uniform depth from below:
Theorem 3.14. Let $d$ be the uniform depth of cusps of $X$. Then,
$$d \geq \min \left\{\left(-2 n+s^{\prime}\right)^{\frac{1}{4}},\left(-2 n+s^{\prime}\right)^{\frac{1}{2}}\right\},$$
where $s^{\prime}=e^{\operatorname{sys}(X) / 2}$.
Proof. Combining Proposition 3.10 with Proposition 3.13 implies the claim. \(\square\)

Direct computation gives the following corollary which will be used later to bound the uniform depth of cusps in terms of $\operatorname{sys}(X)$ :

Corollary 3.15. If $\operatorname{sys}(X) \geq 4 \ln \left(5 n+(4 \pi)^{4}\right)$, then
$$d>e^{\operatorname{sys}(X) / 16}>4 \pi .$$

Additionally, if $\operatorname{sys}(X) \geq 4 \ln \left(5 n+(8 \pi)^{4}\right)$, then
$$d>e^{\operatorname{sys}(X) / 16}>8 \pi .$$

Systole in coverings. In this subsection, we study the behavior of the systole under finite étale coverings. In Proposition 3.9, we proved that the systole is always positive for non-uniform lattices. In Proposition 3.21, we show that it is possible to increase the systole by passing to a suitable cover. We also give an example in Proposition 3.22 to illustrate that this behavior is not limited to normal covers. To establish these results, we first provide a few preliminary lemmas

Parker's generalization of Shimizu's lemma [Par98, Page 442] tells us that for a torsion-free lattice, the uniform depth of cusps is at least 2. Hence, the horoball $\Gamma_{i} \backslash B_{i}\left(t_{i} / 2\right)$ is called
the canonical horoball around the cusp $c_{i}$. In particular, if the cusp $c_{i}$ corresponds to the equivalence class of $q_{\infty}$, then the canonical horoball
$$\Gamma_{\infty} \backslash\left\{(\zeta, v, u) \mid u>t_{\infty} / 2\right\}$$
injects into $X$. The core of $X$ is the set obtained by removing the canonical horoballs from $X$, and we denote it by $X_{\text {core }}$. Note that since $X$ is connected and the canonical horoballs are disjoint, the core of $X$ must be nonempty.

Lemma 3.16. Every closed geodesic of $X$ intersects $X_{\text {core }}$.
Proof. Suppose not. Then there exists a semisimple element $\gamma \in \Gamma$ corresponding to a closed geodesic that does not intersect $X_{\text {core }}$. Since the canonical horoballs around cusps are disjoint open sets and the geodesic is connected, it must be fully contained in a canonical horoball around a cusp. Pull back the closed geodesic to the (Siegel model of) complex ball $\mathbb{B}^{n}$. By conjugating the lattice if necessary, we may assume this canonical horoball is the one around $q_{\infty}$.

Let $c_{\gamma}$ denote the absolute $c$-entry of $\gamma$ as defined in Definition 3.2(ii). It follows from Lemma 2.5 that $q_{\infty}$ has only a parabolic stabilizer in the lattice. Therefore, Lemma 2.3 implies that $c_{\gamma} \neq 0$. Let $z$ be a point in the canonical horoball around $q_{\infty}$ such that both $z$ and $\gamma z$ lie in this horoball. By Lemma 3.7 and Remark 3.4, we obtain
$$u(z) u(\gamma z) \leq \frac{4}{\left|c_{\gamma}\right|^{2}} \leq \frac{t_{\infty}^{2}}{4} .$$
This contradicts the fact that both $z$ and $\gamma z$ lie in the canonical horoball $\{(\zeta, v, u) \mid u>$ $\left.t_{\infty} / 2\right\}$. \(\square\)

Lemma 3.17. Let $z_{0} \in \mathbb{B}^{n}$ and let $R>0$. Then $\left\{\gamma \in \Gamma \mid d\left(z_{0}, \gamma \cdot z_{0}\right) \leq R\right\}$ is finite.
Proof. Suppose not. Then there exists a sequence $\left\{\gamma_{m}\right\}_{m=1}^{\infty}$ with $d\left(z_{0}, \gamma_{m} \cdot z_{0}\right) \leq R$. Since the closed ball of radius $R$ is compact, there exists a subsequence, which we again denote by $\left\{\gamma_{m}\right\}_{m=1}^{\infty}$, such that the set $\left\{\gamma_{m} \cdot z_{0}\right\}_{m=1}^{\infty}$ has an accumulation point $z \in \mathbb{B}^{n}$. This contradicts the discontinuity of the action of $\Gamma$ (see Remark 2.1). \(\square\)

Proposition 3.18. For every $L>0$, there are only finitely many $\Gamma$-conjugacy classes of $\Gamma$ corresponding to closed geodesics of length less than $L$.

Proof. Fix a fundamental domain $\Sigma$ for $X$ in the universal cover $\mathbb{B}^{n}$. Pull back the canonical horoballs to the universal cover and consider the part of $\Sigma$ lying outside them. Denote this set by $\Sigma_{\text {core }}$. Note that $\Sigma_{\text {core }}$ maps to $X_{\text {core }}$, therefore it has to be nonempty. Also, since we removed the neighborhoods of the cusps, this set is bounded. Fix a base point $z_{0} \in \Sigma_{\text {core }}$ and let $D=\sup \left\{d\left(z_{0}, z\right) \mid z \in \Sigma_{\text {core }}\right\}$ be the maximal distance from $z_{0}$ to a point in $\Sigma_{\text {core }}$.

Let $\gamma \in \Gamma_{s}$ with $\ell(\gamma) \leq L$, and let $A_{\gamma} \subset \mathbb{B}^{n}$ denote its axis. The projection of $A_{\gamma}$ to $X$ is a closed geodesic of length $\ell(\gamma) \leq L$, hence it meets $X_{\text {core }}$ by Lemma 3.16. Therefore there exists $g \in \Gamma$ such that the axis of the conjugate $g \gamma g^{-1}$ meets $\Sigma_{\text {core }}$; in particular we may choose a point $p \in A_{g \gamma g^{-1}} \cap \Sigma_{\text {core }}$. Consider the displacement of $z_{0}$ by $g \gamma g^{-1}$. Join $z_{0}$ to $p$, move along the axis by at most $\ell(\gamma)$ (the translation length of $g \gamma g^{-1}$ ), and then join the endpoint back to $g \gamma g^{-1} z_{0}$. By the triangle inequality we obtain
$$d\left(z_{0}, g \gamma g^{-1} z_{0}\right) \leq d\left(z_{0}, p\right)+d\left(p, g \gamma g^{-1} p\right)+d\left(g \gamma g^{-1} p, g \gamma g^{-1} z_{0}\right) \leq 2 D+L,$$
since $d\left(g \gamma g^{-1} p, g \gamma g^{-1} z_{0}\right)=d\left(p, z_{0}\right) \leq D$ and $d\left(p, g \gamma g^{-1} p\right)=\ell(\gamma) \leq L$.

Set $R=2 D+L$ and define $S_{R}:=\left\{\gamma \in \Gamma \mid d\left(z_{0}, \gamma z_{0}\right) \leq R\right\}$. By Lemma 3.17, the set $S_{R}$ is finite. Hence every $\gamma \in \Gamma$ with $\ell(\gamma) \leq L$ is conjugate to some element of the finite set $S_{R}$. It follows that there are only finitely many conjugacy classes in $\Gamma$ with translation length at most $L$. \(\square\)

Remark 3.19. Fix $\epsilon>0$. Applying Proposition 3.18 with $L:=\operatorname{sys}(X)+\epsilon$ shows that there are only finitely many lengths of closed geodesics in $X$ not exceeding $L$; that is, the set
$$\left\{\ell(\gamma) \mid \gamma \in \Gamma_{s}, \ell(\gamma) \leq L\right\}$$
is finite. Therefore, the infimum in the definition of the systole (2.1) is realized.
Definition 3.20. A cofinal normal tower of $X$ is a sequence $\left\{X_{i}\right\}_{i=1}^{\infty}$ of finite étale Galois coverings of $X=X_{1}$, corresponding to a nested sequence of lattices $\left\{\Gamma_{i}\right\}_{i=1}^{\infty}$, where each $\Gamma_{i}$ is a normal subgroup of $\Gamma_{1}$,
$$\Gamma_{i+1} \subset \Gamma_{i} \quad \text { and } \quad \bigcap_{i=1}^{\infty} \Gamma_{i}=\{1\} .$$

Since every lattice in $\operatorname{PU}(n, 1)$ is finitely generated [GR70, Theorem 0.9], Malcev's theorem $\left[\mathrm{M}^{+} 65\right]$ (see [Rat06, Theorem 7.6.8]) implies that the lattice $\Gamma$ is residually finite. In particular, there exists a cofinal normal tower for $X$.

Proposition 3.21. For every $X$, there exists a finite cover $X^{\prime}$ of $X$ such that $\operatorname{sys}\left(X^{\prime}\right)$ is sufficiently large. Moreover, in any cofinal normal tower of coverings $\left\{X_{i}\right\}_{i=1}^{\infty}$ with $X_{1}=X$, we have
$$\operatorname{sys}\left(X_{i}\right) \longrightarrow \infty \quad \text { as } i \rightarrow \infty .$$

Proof. Fix $L>0$. Let $\left\{X_{i}\right\}_{i=1}^{\infty}$ be a cofinal normal tower of $X_{1}=X$ with fundamental groups $\left\{\Gamma_{i}\right\}_{i=1}^{\infty}$. By Proposition 3.18, there are only finitely many conjugacy classes in $\Gamma$ corresponding to closed geodesics of length less than $L$. Choose representatives $\gamma_{1}, \ldots, \gamma_{m} \in$ $\Gamma$ of these classes.

Since $\bigcap_{i=1}^{\infty} \Gamma_{i}=\{1\}$ and $\Gamma$ is residually finite, there exists $i_{0}>0$ such that for all $i>i_{0}$, the subgroup $\Gamma_{i}$ contains none of the elements $\gamma_{1}, \ldots, \gamma_{m}$. Because each $\Gamma_{i}$ is normal in $\Gamma$, it also avoids all of their conjugates. Thus, for such $i$, every nontrivial element of $\Gamma_{i}$ has a translation length of at least $L$, and hence $\operatorname{sys}\left(X_{i}\right) \geq L$. Since $L$ was arbitrary, we conclude that $\operatorname{sys}\left(X_{i}\right) \rightarrow \infty$ as $i \rightarrow \infty$.

The existence of some $X^{\prime}$ with sufficiently large sys( $X^{\prime}$ ) follows from the fact that $\Gamma$ is residually finite and therefore admits a cofinal normal tower. \(\square\)

We emphasize that the phenomenon of the systole becoming arbitrarily large is not limited to coverings from normal cofinal towers. It is enough that the traces of hyperbolic elements become arbitrarily large (see Lemma 3.5). To illustrate this, we provide an example of covers that are not normal but for which the systole tends to infinity:

Proposition 3.22. Let $K=\mathbb{Q}(i)$ with ring of integers $\mathcal{O}_{K}=\mathbb{Z}[i]$, and fix the embedding $\iota: K \hookrightarrow \mathbb{C}$ with $\iota(i)=i$. From now on, we regard $\mathcal{O}_{K}$ as a subring of $\mathbb{C}$ via $\iota$.

Let $q \equiv 3(\bmod 4)$ be prime, so $(q) \subset O_{K}$ is a prime ideal; set $\mathfrak{p}=(q)$. We will use the group $\mathrm{U}(Q)$ introduced in the equation (2.3). We will write an element $h \in \mathrm{U}(Q)$ in the
form (2.4):
$$h=\left[\begin{array}{ccc}
a & \tau & b \\
\alpha & f & \beta \\
c & \delta & e
\end{array}\right] \quad \text { with } a, b, c, e \in K, \quad \tau, \alpha, \beta, \delta \in K, \quad f \in K^{*} .$$
Consider the group $\mathrm{U}(Q)\left(\mathcal{O}_{K}\right):=\mathrm{U}(Q) \cap \mathrm{GL}_{3}\left(\mathcal{O}_{K}\right)$ and define its subgroups by
$$\widetilde{\Gamma}_{1}(\mathfrak{p}):=\left\{h \in \mathrm{U}(Q)\left(\mathcal{O}_{K}\right): h \equiv\left[\begin{array}{ccc}
1 & * & * \\
0 & 1 & * \\
0 & 0 & 1
\end{array}\right] \quad(\bmod \mathfrak{p})\right\} .$$
Let $\pi: \mathrm{U}(Q) \rightarrow \mathrm{PU}(Q)=\mathrm{U}(Q) /\{\mu I:|\mu|=1\}$ be the natural projection, and set
$$\Gamma_{1}(\mathfrak{p}):=\pi\left(\widetilde{\Gamma}_{1}(\mathfrak{p})\right) \subset \operatorname{PU}(Q) .$$
Then we define the Picard modular surface at level $\mathfrak{p}$ as
$$X_{1}(\mathfrak{p}):=\Gamma_{1}(\mathfrak{p}) \backslash \mathbb{B}^{2},$$
which is a finite cover of $X(1):=\pi\left(\mathrm{U}(Q)\left(\mathcal{O}_{K}\right)\right) \backslash \mathbb{B}^{2}$. Then the following hold:
\begin{itemize}
\item[(i)] The covering $X_{1}(\mathfrak{p}) \rightarrow X(1)$ is not normal.
\item[(ii)] If $\gamma \in \Gamma_{1}(\mathfrak{p})$ is hyperbolic, then
$$|\operatorname{tr}(\gamma)| \geq q-3,$$
where the absolute trace of $\gamma$ is understood as in Definition 3.2.
\item[(iii)] sys $\left(X_{1}(\mathfrak{p})\right) \rightarrow \infty$ as $q \rightarrow \infty$.
\end{itemize}

Proof. (i) Let
$$g=\left[\begin{array}{lll}
1 & 0 & i \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right] \in \widetilde{\Gamma}_{1}(\mathfrak{p}), \quad h=\left[\begin{array}{lll}
0 & 0 & 1 \\
0 & 1 & 0 \\
1 & 0 & 0
\end{array}\right] \in \mathrm{U}(Q)\left(\mathcal{O}_{K}\right) .$$
Then
$$h g h^{-1}=\left[\begin{array}{lll}
1 & 0 & 0 \\
0 & 1 & 0 \\
i & 0 & 1
\end{array}\right],$$
whose lower-left entry is a unit modulo $\mathfrak{p}$. Hence $h g h^{-1} \notin \widetilde{\Gamma}_{1}(\mathfrak{p})$, and therefore its image under $\pi$ does not lie in $\Gamma_{1}(\mathfrak{p})$. This shows that $\Gamma_{1}(\mathfrak{p})$ is not normal in $\pi\left(\mathrm{U}(Q)\left(\mathcal{O}_{K}\right)\right)$.
\begin{itemize}
\item[(ii)] Let $\gamma \in \Gamma_{1}(\mathfrak{p})$ be hyperbolic, and choose a lift $\widetilde{\gamma} \in \widetilde{\Gamma}_{1}(\mathfrak{p})$ of $\gamma$. By the definition of $\widetilde{\Gamma}_{1}(\mathfrak{p})$ we have $\operatorname{tr}(\widetilde{\gamma}) \equiv 3(\bmod \mathfrak{p})$, so $t:=\operatorname{tr}(\widetilde{\gamma})-3 \in \mathfrak{p}$. Since $\gamma$ is hyperbolic, $\widetilde{\gamma}$ is not unipotent and thus $t \neq 0$. Because $\mathfrak{p}=(q)$ with $q \equiv 3(\bmod 4)$ is prime in $\mathcal{O}_{K}=\mathbb{Z}[i]$, we may write $t=q w$ with $w \in \mathbb{Z}[i] \backslash\{0\}$. Taking complex absolute values yields
$$|\operatorname{tr}(\widetilde{\gamma})-3|=|t|=q|w| \geq q,$$
since $|w| \geq 1$ for every nonzero $w \in \mathbb{Z}[i]$. This implies that: $|\operatorname{tr}(\gamma)|=|\operatorname{tr}(\widetilde{\gamma})| \geq q-3$.
\item[(iii)] This follows from the second part and Lemma 3.5.
\end{itemize} \(\square\)

\section*{4. Thick-thin decomposition}

In this section, we introduce a version of the thick-thin decomposition relative to the systole, which differs from Margulis' decomposition as it depends on the lattice $\Gamma$. The main goal of this section is to prove Theorem 4.4, which states that the thin part of $X$ contains no subvariety (by a subvariety of $X$ we mean the intersection of a closed, irreducible, positive-dimensional algebraic subvariety of the projective variety $\bar{X}$ with $X$, such that the intersection is nonempty).

Let $c_{i}$ be a cusp of $X$ with unipotent stabilizer $\Gamma_{i}$. Fix $\epsilon>0$. Consider the set
$$\tilde{U}_{i, \epsilon}=\left\{x \in \mathbb{B}^{n} \mid \exists g \in \Gamma_{i}, d(x, g \cdot x)<\epsilon\right\} .$$
We define the $\epsilon$-thin neighborhood around the cusp $c_{i}$ as the set $U_{i, \epsilon}:=\Gamma_{i} \backslash \tilde{U}_{i, \epsilon}$. Also, we fix $\rho=\operatorname{sys}(X) / 2$ and define the thin part of $X$ as the union of all $\rho$-thin neighborhood around cusps of $X$ :
$$X_{\text {thin }}:=\cup_{i=1}^{k} U_{i, \rho},$$
where $k$ is the number of cusps. The following Proposition shows that $X_{\text {thin }}$ is actually the disjoint union of the $\rho$-thin neighborhood around cusps:

Proposition 4.1. If $\epsilon<\operatorname{sys}(X) / 2$, then $U_{i, \epsilon} \cap U_{j, \epsilon}=\varnothing$ for $i \neq j$.
Proof. For the sake of the contradiction assume that $x \in U_{i, \epsilon} \cap U_{j, \epsilon}$. This means that there exist $\gamma_{1} \in \Gamma_{i}$ and $\gamma_{2} \in \Gamma_{j}$ such that $d\left(\tilde{x}, \gamma_{1} \cdot \tilde{x}\right)<\epsilon$ and $d\left(\tilde{x}, \gamma_{2} \cdot \tilde{x}\right)<\epsilon$, where $\tilde{x} \in \mathbb{B}^{n}$ is a fiber of $x$. This in particular implies that $d\left(\tilde{x}, \gamma_{1}^{-1} \cdot \tilde{x}\right)<\epsilon$.

Since $\operatorname{PU}(Q)$ acts doubly transitively on the boundary, we can, if necessary, change coordinates (i.e., by conjugating the lattice) to identify $c_{i}$ and $c_{j}$ with the equivalence classes of points $q_{\infty}$ and $q_{0}$ on the boundary $\partial \mathbb{S}$. Note that the systole is invariant under this change of coordinates.