---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Positivity of Intersections and Tameness of Almost Complex 4-manifolds]

---
source_file: 2401_17381.pdf
converter: mathpix
format: mmd
---

\title{
Positivity of Intersections and Tameness of Almost Complex 4-manifolds
}

\author{
Spencer Cattalani*
}

July 10, 2026

\begin{abstract}
We prove that pseudoholomorphic curves intersect complex 2-cycles positively in almost complex 4-manifolds. This makes possible a general and conceptually simple proof that an almost complex 4-manifold with many curves admits a taming symplectic structure, as envisioned by Gromov. Furthermore, we prove that the positivity of intersections between pseudoholomorphic curves is stable, in a geometric sense.
\end{abstract}

\section*{Contents}
1 Introduction ..... 1
2 Discussion of results ..... 4
2.1 Sharpness ..... 4
2.2 Future directions ..... 6
3 Preliminaries: currents ..... 7
3.1 Integration along the fiber ..... 8
3.2 Structure currents ..... 12
4 Preliminaries: curves ..... 14
5 Construction of Poincaré dual ..... 16
6 Proofs of the main theorems ..... 20
A Proof of Proposition 4.1 ..... 21

\section*{1 Introduction}

Gromov's introduction of pseudoholomorphic curves to symplectic geometry revolutionized the field. Such techniques are particularly fruitful in dimension 4. Among the many results proved in this setting are the uniqueness of the symplectic structure on $\mathbb{C P}^{2}[24$, Theorem B ], the classification of rational and ruled symplectic manifolds [16], and the retractability of the symplectomorphism

\footnotetext{
*Partially supported by NSF grant DMS 1901979 and by the Simons Foundation
}
group of the Fubini-Study form on $\mathbb{C P}^{2}$ onto its isometry group [11, Remark 0.3.C]. A basic fact underlying this theory is that every symplectic form tames some almost complex structure. This paper is concerned with the converse: when does an almost complex manifold admit a taming symplectic form? Sullivan provided a framework for answering this question in terms of his notion of complex cycles:

Proposition 1.1 ([23, Theorem III.2]). Let $(X, J)$ be a closed almost complex manifold. If $[T] \neq 0 \in H_{2}(X, \mathbb{R})$ for every nonzero complex cycle $T$ on $X$, then ( $X, J$ ) is tamed by a symplectic form.

The definition and basic properties of complex cycles are recalled in Section 3.2. It is also shown in [23, Theorem III.2] that a closed almost complex manifold always contains nonzero complex cycles. They are studied in a similar context in [3]. Unfortunately, they are generally quite singular; see [12] for some pathological examples. One would therefore like to answer the above question in terms of more familiar objects, such as pseudoholomorphic curves.

Gromov proposed such an answer in [11, Remark 2.4.A']. This remark says that an almost complex 4-manifold with many pseudoholomorphic curves should admit a taming symplectic form. The argument presented therein comes from integral geometry. It is carried out in [18, Section 10]. Unfortunately, his reasoning requires the manifold to be swept out by smooth families of transversely intersecting curves. We prove that Gromov's prediction holds in general. All notions appearing in the statement of Theorem 1 below are recalled in Section 4.

Theorem 1. Let $(X, J)$ be a closed almost complex 4-manifold such that every pair of points can be joined by a closed connected pseudoholomorphic curve $C$. Suppose also that $(X, J)$ contains
\begin{itemize}
\item[(a)] a free pseudoholomorphic curve, or
\item[(b)] an immersed pseudoholomorphic curve of genus $g$ with $n$ nodes and self-intersection number at least $2 g+2 n$, or
\item[(c)] an embedded rational curve with nonnegative self-intersection number, or
\item[(d)] uncountably many embedded rational curves.
\end{itemize}

Then $(X, J)$ admits a taming symplectic form $\omega$.
In case (c) or (d) holds, it then follows from [16] and [27, Theorem A] that $\omega$ may be chosen so that $(X, \omega)$ is obtained by blowing up $\mathbb{C P}^{2}$ with the Fubini-Study form or a symplectic sphere bundle over a surface. We note that the curves $C$ in Theorem 1 are not assumed to be immersed or irreducible. Neither are they assumed to lie in smooth families or to intersect transversely. The sharpness of Theorem 1 is discussed in Section 2.

Theorem 1 is a consequence of the simple geometric principle of positivity of intersections. Classically, this states that two closed pseudoholomorphic curves which intersect in an almost complex 4-manifold either coincide on an irreducible component or have positive intersection number. We extend this principle to include the case of a pseudoholomorphic curve intersecting a complex cycle in an almost complex 4-manifold. Under the assumptions of Theorem 1, we are able to show that every nonzero complex cycle intersects some curve positively and is thus nontrivial in homology.

Theorem 1 then follows from Proposition 1.1.
It is nontrivial to extend even the statement of positivity of intersections to complex cycles, as the "irreducible components" of a complex cycle have not yet been defined in a suitable manner. To circumvent this difficulty, we use an alternative characterization in terms of a collection of test forms. Specifically, a 2-form $\varphi$ on an almost complex manifold $(X, J)$ is called semipositive if $\varphi(v, J v) \geq 0$ for any $v \in T X$. Hermitian forms, taming symplectic forms, and the form $i \mathrm{~d} z_{1} \mathrm{~d} \overline{z_{1}}$ on $\mathbb{C}^{n}$ are semipositive. They can be constructed locally quite easily, for instance by multiplying a Hermitian form by a nonnegative bump function. This makes them very good probes for the behavior of the tangent planes to holomorphic curves. For example, an irreducible curve $C$ is an irreducible component of a curve $S$ if and only if there is no semipositive form $\varphi$ such that $\int_{C} \varphi>0$ and $\int_{S} \varphi=0$. The assumption in the following theorem is directly inspired by this fact.

Theorem 2. Let $(X, J)$ be a closed almost complex 4-manifold. Let $C$ be a closed irreducible pseudoholomorphic curve in $X$ and $T$ be a complex cycle on $X$. If $C \cap \operatorname{supp}(T) \neq \emptyset$ and there is a semipositive form $\varphi$ such that
$$\int_{C} \varphi>0 \quad \text { and } \quad T(\varphi)=0$$
then $\langle[T],[C]\rangle>0$.
If $C \not \subset \operatorname{supp}(T)$, there is a nonnegative bump function $f$ which is positive somewhere on $C$ and is identically zero on $\operatorname{supp}(T)$. If $\omega$ is a Hermitian form on $X$, then $f \omega$ is a semipositive form satisfying the assumption in Theorem 2. Therefore, the following corollary holds.

Corollary 1.2. Let $(X, J)$ be a closed almost complex 4-manifold. Let $C$ be a closed irreducible pseudoholomorphic curve in $X$ and $T$ be a complex cycle on $X$. If $C \cap \operatorname{supp}(T) \neq \emptyset$ and $C \not \subset \operatorname{supp}(T)$, then $\langle[T],[C]\rangle>0$.

The difficulty in proving the positivity of intersections is that the curves can intersect at singular points. To resolve this issue, one deforms the curves locally to get a transverse intersection. The issues with singularities are magnified in the context of Theorem 2, as a complex cycle can be much more singular than any holomorphic curve. Therefore, we develop a refined deformation scheme, which is essentially founded on the Oka principle (alternatively, the $h$-principle); see the fourth and fifth paragraphs of Section 2.2. Our method also allows one to prove that the positivity of intersections is stable:

Theorem 3. Let $(X, J)$ be a closed almost complex 4-manifold, equipped with a metric. Let $C$ be a closed irreducible pseudoholomorphic curve in $X$. For every $\varepsilon>0$, there exists $\delta>0$ such that if $S \subset X$ is a closed pseudoholomorphic curve, $\langle[S],[C]\rangle \leq 0$, and at least one point of $S$ is $\delta$-close to $C$, then every point of $C$ is $\varepsilon$-close to $S$.

Only the equality case in Theorem 3 is new, because of the classical positivity of intersections. Broadly, Theorem 3 says that curves which almost intersect must almost coincide on an irreducible component. We thank the anonymous reviewer for stating the next corollary and the explanatory remark which follows it.

Corollary 1.3. Let $(X, J)$ be a closed almost complex 4-manifold, equipped with a metric. Let $C, S \subset X$ be closed pseudoholomorphic curves so that $C$ is irreducible and $\langle[S],[C]\rangle>0$. If $C \not \subset S$, then there exists $\delta>0$ such that every closed pseudoholomorphic curve $S^{\prime}$ which is $\delta$-close to $S$ in the Hausdorff metric satisfies $\left\langle\left[S^{\prime}\right],[C]\right\rangle>0$.

Corollary 1.3 is more difficult to prove than it might first appear. One is tempted to take a limit, but a Hausdorff limit does not generally preserve homology class, and a limit as currents without a bound on area will generally result in a (singular) complex cycle, not a curve.

We now briefly remark on the proof. If a pseudoholomorphic curve varies in a large family, then integration along the fiber allows one to define a well-behaved Poincaré dual 2-form, which would imply Theorems 1, 2, and 3 via Proposition 1.1. However, a pseudoholomorphic curve might not vary in a family of pseudoholomorphic curves. We resolve this issue by allowing the curves in the family to fail to be pseudoholomorphic on a small prescribed disk. This allows every pseudoholomorphic curve to vary in an arbitrarily large family, while retaining a great deal of control over the resulting Poincaré dual form. This argument is the key step in the proof of Proposition 5.3, which quickly implies all of the main results of this paper and should be of independent interest. In fact, one can prove Theorem 1 directly from Proposition 5.3 by adding together a suitable collection of Poincaré dual forms to yield a symplectic form; this method avoids the use of complex cycles.

The outline of the paper is as follows. In Section 2, we discuss possible extensions of the main results of this paper, as well as their connection to other work. In Section 3, we recall some basics from the theory of currents. In Section 4, we recall the deformation theory of pseudoholomorphic curves and state Proposition 4.1, which describes the flexibility of pseudoholomorphic curves with boundary. It is proved in the appendix. In Section 5, we prove Proposition 5.3, which constructs a Poincaré dual to a pseudoholomorphic curve. Theorems 1, 2, and 3 follow quickly from Proposition 5.3 and are proved in Section 6.

Acknowledgements. The author is thankful to Eric Bedford, Dennis Sullivan, Dror Varolin, and Scott Wilson for helpful conversations, to Ethan Addison for his comments on an earlier draft, and to Aleksey Zinger for his great help with the exposition, especially in the appendix. The author is also grateful to the anonymous reviewer for a thorough report that significantly improved the clarity of writing, particularly of the introduction and Section 5.

\section*{2 Discussion of results}

In this section, we explain some features of the main results and their proofs, pose Conjecture 2.5 generalizing Theorem 1, and indicate connections to related work.

\subsection*{2.1 Sharpness}

Theorem 1 is not sharp, as there are many tamed almost complex manifolds which admit no pseudoholomorphic curves at all (e.g. a general complex torus). However, Example 2.1 and Propositions 2.2 and 2.3 below show that the assumptions cannot be significantly weakened. First of all, Theorem 1 would not hold if $X$ were assumed only to have a pseudoholomorphic curve passing through each point, as demonstrated by the following example.

Example 2.1. Let $S:=\left(\mathbb{C}^{2}-\{0\}\right) /\{z \sim 2 z\}$ be the Hopf surface. It has a holomorphic curve through every point and satisfies (a) in Theorem 1, but $H^{2}(S, \mathbb{Z})=0$, so $S$ is not tamed.

One might hope that there is a topological condition on $X$ or a geometric condition concerning just one pseudoholomorphic curve (e.g. that it be sufficiently free) that would guarantee that $(X, J)$ is
tamed. By Proposition 2.2 below, there is no such condition.
Proposition 2.2. Let $(X, J)$ be an almost complex manifold of dimension at least 4. For every nonempty open $U \subset X$, there exists an almost complex structure $J^{\prime}$ on $X$ which is deformation equivalent to $J$, is equal to $J$ outside of $U$, and admits no taming symplectic structure.

Proof. First, we construct an almost complex structure $J^{\prime}$ on $\mathbb{C}^{n}$ for $n \geq 2$ so that $J^{\prime}$ equals the standard complex structure outside the unit ball and $\mathbb{C}^{n}$ contains a $J^{\prime}$-holomorphic embedded torus. Let $\mathbb{C}^{n}$ have complex coordinates $x_{1}+i y_{1}, \ldots, x_{n}+i y_{n}$ and $\mathbb{R}^{3}$ have real coordinates $x_{1}, y_{1}$, and $x_{2}$. Embed the 2-torus $T^{2}$ in the unit ball in $\mathbb{R}^{3}$. By the Gauss-Bonnet Theorem, the Gauss map $\nu: T^{2} \longrightarrow S^{2}$, defined by taking the unit normal vector, has degree zero (see [19, Lemma 6.3]) and is thus null-homotopic. Therefore, one can extend the map $\nu$ to the rest of the unit ball in $\mathbb{C}^{n}$, so that it remains in the span of $\frac{\partial}{\partial x_{1}}, \frac{\partial}{\partial y_{1}}$, and $\frac{\partial}{\partial x_{2}}$ and restricts to the constant vector field $\frac{\partial}{\partial x_{2}}$ on the unit sphere. Extend it to the rest of $\mathbb{C}^{n}$ as a constant vector field. Let $v$ be the resulting vector field and define a field of oriented planes $\pi$ on $\mathbb{C}^{n}$ by $v \wedge \frac{\partial}{\partial y_{2}}$. Define an almost complex structure $J^{\prime}$ on $\mathbb{C}^{n}$ via a rotation by a positive quarter turn in $\pi$, its orthogonal complement in the span of $\frac{\partial}{\partial x_{1}}$, $\frac{\partial}{\partial y_{1}}, \frac{\partial}{\partial x_{2}}$, and $\frac{\partial}{\partial y_{2}}$, and in each plane spanned by $\frac{\partial}{\partial x_{k}}$ and $\frac{\partial}{\partial y_{k}}$ for $2<k \leq n$. This $J^{\prime}$ equals the standard complex structure outside the unit ball and contains a $J^{\prime}$-holomorphic embedded torus.

Now, we modify $(X, J)$ using this local model. Deform $J$ on a nonempty open subset $U^{\prime} \subset U$ so that the resulting structure is integrable on $U^{\prime}$. Replace $J$ with the $J^{\prime}$ constructed above inside a complex coordinate chart. As $J^{\prime}$ is standard outside of the unit ball, this yields an almost complex structure $J^{\prime}$ on $X$. The manifold $X$ contains a null-homologous nonconstant $J^{\prime}$-holomorphic curve, so $J^{\prime}$ is not tamed by any symplectic structure. \(\square\)

As noted above, there are almost complex 4-manifolds which satisfy the conclusion, but not the assumptions of Theorem 1. However, Proposition 2.3 below shows that every almost complex 4-manifold satisfying the conclusion of Theorem 1 can be transformed into one which satisfies the assumptions of Theorem 1. In particular, it shows that Theorem 1 is sharp up to blowups and deformations.

Proposition 2.3. Let $(X, J)$ be a closed tamed almost complex 4-manifold. There are a taming symplectic form $\omega$ on $X$, a symplectic manifold $\left(X^{\prime}, \omega^{\prime}\right)$ obtained by symplectically blowing up $(X, \omega)$ at a finite number of points, and an almost complex structure $J^{\prime}$ on $X^{\prime}$ tamed by $\omega^{\prime}$ such that every pair of points of $X^{\prime}$ can be joined by a closed connected $J^{\prime}$-holomorphic curve $C$ and $X^{\prime}$ contains a free $J^{\prime}$-holomorphic curve.

Proof. Taming $J$ is an open and positive scaling invariant condition on symplectic forms. Therefore, if ( $X, J$ ) is tamed, it admits a taming symplectic form $\omega$ such that $[\omega] \in H^{2}(X, \mathbb{R})$ is the reduction of an integer cohomology class. Therefore, by [6, Theorem 2], $(X, \omega)$ admits a Lefschetz pencil such that the fibers are Poincaré dual to a multiple of $[\omega]$. Since $\omega$ has positive self-intersection, the base locus is nonempty. It follows from the definition of Lefschetz pencil that the base locus is finite and the fibers intersect transversely. Symplectically blowing up along the base locus of the pencil yields a symplectic manifold $\left(X^{\prime}, \omega^{\prime}\right)$ which admits a Lefschetz fibration; see [27, Chapter 3] for a full exposition of this construction.

An exceptional divisor of this blowup is an embedded symplectic sphere with self-intersection -1. There is an almost complex structure on $X^{\prime}$ tamed by $\omega^{\prime}$ in which the exceptional divisor is a
pseudoholomorphic curve. As it is a rational curve with self-intersection -1, it is regular by [13, Theorem 1]. Therefore, by Gromov's Compactness Theorem [11, Theorem 1.5.B], every almost complex structure on $X^{\prime}$ which is tamed by $\omega^{\prime}$ has a pseudoholomorphic curve in the class of the exceptional divisor. There is an almost complex structure $J^{\prime}$ tamed by $\omega^{\prime}$ on $X^{\prime}$ such that the fibers of the Lefschetz fibration are pseudoholomorphic curves; see the remark following Lemma 2.12 in [8]. The smooth fibers are free. Furthermore, there is an exceptional divisor intersecting each fiber, so every pair of points of $X^{\prime}$ can be joined by a closed connected $J^{\prime}$-holomorphic curve. \(\square\)

\subsection*{2.2 Future directions}

Our proof of Theorem 1 via the positivity of intersections is quite robust and many related statements can be proved in a similar manner. The main difficulty is in obtaining a closed semipositive form with which one can use Theorem 2. In our case, we use free curves to produce such forms. However, they can arise in other ways, for example via pullbacks and limits of symplectic forms. Proposition 2.4 below is a somewhat sharper version of Theorem 1, albeit with a more technical statement.

Proposition 2.4. Let $(X, J)$ be a closed almost complex 4-manifold. Suppose there exists a closed semipositive 2-form $\varphi$ such that, for every $x \in X$, there exist a closed connected pseudoholomorphic curve $C_{x}$ passing through $x$ such that $\int_{C_{x}} \varphi>0$. Then, $(X, J)$ admits a taming symplectic structure.

As in Proposition 2.3, the existence of a Lefschetz pencil shows that Proposition 2.4 is sharp up to deformation; blowing up is not required in this case. It is quite difficult (perhaps impossible) to construct an almost complex 4-manifold with many curves which does not also have closed semipositive forms. Ideally, one could avoid the assumption of semipositivity altogether and use only a homological positivity condition, as below. This means that the curves $C_{x}$ lie in an open cone in $H_{2}(X, \mathbb{R})$.

Conjecture 2.5. The word "semipositive" can be removed in Proposition 2.4.
Our method of using complex cycles allows one to leverage other geometric information to construct symplectic forms. For example, as complex cycles are normal currents, they are supported on a set of Hausdorff dimension at least 2; see [9, Theorem 8.5]. It follows that sets of lower dimension can be ignored in Theorem 1. It is not clear how one would see this other than through the perspective of complex cycles. Their geometry is also studied in [3]. Ultimately, a full understanding of complex cycles would elucidate the role of symplectic structures in almost complex geometry.

In the classical proof of the positivity of intersections, the main step is deforming a pseudoholomorphic curve on a small neighborhood. Our proof of Theorem 2 refines this by deforming the curve everywhere except on a small neighborhood. The fact that pseudoholomorphic curves can be deformed this way is a kind of semi-global flexibility. We expect that this point, which can be considered as a type of h-principle or Oka principle, should be of use in a variety of contexts.

We now explain a few different ways in which this semi-global flexibility can be understood. The deformations of a pseudoholomorphic curve are controlled by its deformation and obstruction bundles; see [14, Section 2]. In this paper, we arrange that the former is large and the latter is zero by choosing appropriate boundary conditions (Lemma 4.5) and using an automatic transversality result (Proposition 4.1). This argument is restricted to dimension 4, due to the use of automatic
transversality. Alternatively, we could add a family of perturbations to the Cauchy-Riemann equation that covers the obstruction bundle. Essentially by unique continuation, such a family can be chosen to be supported in an arbitrary open set; see [29, Lemma 4.1], for example. This technique works in any dimension to produce a family of surfaces which are pseudoholomorphic away from a small open set. There is also a complex-geometric interpretation. An open Riemann surface is Stein [26, Theorem 8.1.1]. It should then follow from Cartan's Theorem B [21, Théorème B] that the obstruction bundle vanishes. Therefore, a holomorphic curve with boundary in a complex manifold should deform in an arbitrarily large family.

We now briefly remark on connections to other work. The method for constructing compatible symplectic structures in [25] is quite similar to the integral-geometric method proposed in [11, Remark 2.4.A']. By [28], this method can be used to show that almost complex 4-manifolds with sufficiently well-distributed curves admit compatible symplectic structures, a stronger condition than just taming. By deforming curves, we avoid having to assume that they are well-distributed (formally, that they can be used to form a Taubes current), but we do not produce a compatible symplectic structure. We hope that our method, enriched with analytic estimates as in [25], could help produce compatible forms, and therefore make progress towards Donaldson's "tamed-to-compatible" conjecture [7]. With respect to Theorem 2, one might wish to understand intersections between two complex cycles. This is akin to the intersection theory of positive (1, 1)-currents in complex geometry, which is well-developed; see [1, 4], for example. Pluripotential theory is central to this development. Unfortunately, it seems that complex cycles do not always admit potential functions, which significantly hampers the use of pluripotential theory in our context.

\section*{3 Preliminaries: currents}

In this section, we recall the necessary background on currents. This plays an essential role in the proof of Proposition 5.3 in Section 5, which constructs a differential form with controlled geometry. We do this in two parts - on a large "good" set and a small "bad" set. The construction of the form in the good set uses integration along the fiber, which is the focus of Section 3.1. The construction on the bad set uses Sullivan's theory of structure currents, which is the focus of Section 3.2.

Let $X$ be a smooth $n$-manifold. For $k \in \mathbb{Z}^{\geq 0}$, we denote by $\Omega_{c}^{k}(X)$ the space of compactly supported differential $k$-forms on $X$. A $k$-current on an $n$-manifold $X$ is a linear functional on $\Omega_{c}^{k}(X)$ which is continuous in the strong $C^{\infty}$-topology on $\Omega_{c}^{k}(X)$. A sequence of forms converges in the strong $C^{\infty}$-topology if it converges in $C^{\infty}$ and all the forms are supported in the same compact set. We let $\left(\Omega_{c}^{k}(X)\right)^{*}$ denote the space of $k$-currents on $X$. The exterior derivative on forms induces a boundary operator,
$$\partial:\left(\Omega_{c}^{k}(X)\right)^{*} \longrightarrow\left(\Omega_{c}^{k-1}(X)\right)^{*}, \quad \partial T(\alpha):=T(\mathrm{~d} \alpha) .$$
A current $T$ on $X$ is called a cycle if $\partial T=0$. The support of a $k$-current $T$ on $X$, denoted $\operatorname{supp}(T)$, is the complement of the largest open subset $U \subset X$ such that $T(\alpha)=0$ for all $\alpha \in \Omega_{c}^{k}(U)$. If $\alpha \in \Omega^{k}(X)$ with $\operatorname{supp}(\alpha) \cap \operatorname{supp}(T)$ compact, then
$$T(\alpha):=T(\rho \alpha) \in \mathbb{R}$$
does not depend on the choice of $\rho \in C_{c}^{\infty}(X)$ such that $\rho$ is 1 on a neighborhood of $\operatorname{supp}(\alpha) \cap \operatorname{supp}(T)$. If $T$ is a $k$-current on $X$ and $U \subset X$ is an open subset, then the restriction of $T$ to $\Omega_{c}^{k}(U) \subset \Omega_{c}^{k}(X)$ is a $k$-current on $U$, which we denote by $\left.T\right|_{U}$.

Example 3.1. A dimension $k$ closed oriented submanifold $Y$ of $X$ defines a $k$-current
$$T_{Y}: \Omega_{c}^{k}(X) \longrightarrow \mathbb{R}, \quad T_{Y}(\alpha):=\int_{Y} \alpha .$$
In this case, $\operatorname{supp}\left(T_{Y}\right)=Y$.
Example 3.2. If $X$ is oriented, a degree $(n-k)$ differential form $\omega$ defines a $k$-current
$$T_{\omega}: \Omega_{c}^{k}(X) \longrightarrow \mathbb{R}, \quad T_{\omega}(\alpha):=\int_{X} \omega \wedge \alpha .$$
In this case, $\operatorname{supp}\left(T_{\omega}\right)=\operatorname{supp}(\omega)$. If $X$ is closed, the inclusion
$$\iota: \Omega^{k}(X) \longrightarrow\left(\Omega_{c}^{n-k}(X)\right)^{*}$$
induces an isomorphism from de Rham cohomology to the homology of currents; see [5, Chapter IV, Theorem 14]. The analogous statement in relative homology also holds.

Example 3.3. A $k$-multivector $v \in \bigwedge^{k} T X$ defines a $k$-current
$$T_{v}: \Omega_{c}^{k}(X) \longrightarrow \mathbb{R}, \quad T_{v}(\alpha):=\alpha(v) .$$
The current $T_{v}$ is called a Dirac current.
A current $T$ on $X$ is said to be smooth on an open set $U \subset X$ if $\left.T\right|_{U}=T_{\omega}$ for some differential form $\omega$ on $U$. We note that the current defined by a smooth submanifold of positive codimension, as in Example 3.1, is not smooth on any open subset intersecting $Y$.

The pullback operation on forms induces a pushforward on currents with compact support. For a smooth map $f: M \longrightarrow X$ and a compactly supported $k$-current $T$ on $M$,
$$f_{*} T: \Omega_{c}^{k}(X) \longrightarrow \mathbb{R}, \quad\left\{f_{*} T\right\}(\alpha):=T\left(f^{*} \alpha\right),$$
is a well-defined $k$-current on $X$.

\subsection*{3.1 Integration along the fiber}

In special cases, the pushforward of a smooth current is smooth. Such cases include integration along the fiber; see [2, Section 6] and the proof of Lemma 3.4 below.

Lemma 3.4. Let $f: M \longrightarrow X$ be a smooth map from an oriented $m$-manifold $M$ with boundary to an oriented $n$-manifold $X, k \in \mathbb{Z}^{\geq 0}$, and $\omega \in \Omega_{c}^{m-k}(M)$. If $x \in X-f(\partial M)$ is a regular value of $f$, $v \in \bigwedge^{n-k}\left(T_{x} X\right), \widetilde{v} \in \Gamma\left(f^{-1}(x) ; \bigwedge^{n-k} T M\right)$ is a lift of $v$ along $\mathrm{d} f$, and $\omega(-, \widetilde{v}) \in \Gamma\left(f^{-1}(x), \Lambda^{m-n} T^{*} M\right)$ is the contraction of $\omega$ with respect to $\widetilde{v}$ in the last $n-k$ inputs, then
$$\left\{f_{*} \omega\right\}_{x}(v):=\int_{f^{-1}(x)} \omega(-, \widetilde{v})$$
is independent of the choice of the lift of $v$. If $W \subset X-f(\partial M)$ is an open subset consisting of regular values of $f$, then the map
$$\left.\left\{f_{*} \omega\right\}\right|_{W}: W \longrightarrow \bigwedge^{n-k}\left(T^{*} W\right), \quad x \mapsto\left\{f_{*} \omega\right\}_{x},$$
defines a (smooth) differential form on $W$ and
$$\left.\left\{f_{*} T_{\omega}\right\}\right|_{W}=T_{\left.\left\{f_{*} \omega\right\}\right|_{W}} .$$
In particular, the $k$-current $f_{*} T_{\omega}$ is smooth on $W$.
Proof. We assume $m \geq n$ and show first that this result holds for the projection onto the last $n$ coordinates, $\pi: \mathbb{R}^{m} \longrightarrow \mathbb{R}^{n}$. Denote the first $m-n$ coordinates of $\mathbb{R}^{m}$ by $p_{1}, \ldots, p_{m-n}$ and the last $n$ coordinates by $x_{1}, \ldots, x_{n}$. It suffices to prove the result for simple forms, i.e. those of the form $f \mathrm{~d} p_{\alpha} \wedge \mathrm{d} x_{\beta}$, where $\alpha$ and $\beta$ are multi-indices. Let $g \mathrm{~d} x_{\gamma}$ be a form on $\mathbb{R}^{n}$, where $\gamma$ is a multi-index and $g \in C_{c}^{\infty}\left(\mathbb{R}^{n}\right)$. By Fubini's theorem,
$$\begin{aligned}
\left\{\pi_{*}\left(T_{f \mathrm{~d} p_{\alpha} \wedge \mathrm{d} x_{\beta}}\right)\right\}\left(g \mathrm{~d} x_{\gamma}\right) & :=\int_{\mathbb{R}^{m}} f \mathrm{~d} p_{\alpha} \wedge \mathrm{d} x_{\beta} \wedge \pi^{*}\left(g \mathrm{~d} x_{\gamma}\right)=\int_{\mathbb{R}^{m}} f \mathrm{~d} p_{\alpha} \wedge \mathrm{d} x_{\beta} \wedge(g \circ \pi) \mathrm{d} x_{\gamma} \\
& =\int_{\mathbb{R}^{n}}\left(\int_{\mathbb{R}^{m-n}} f \mathrm{~d} p_{\alpha}\right) \mathrm{d} x_{\beta} \wedge\left(g \mathrm{~d} x_{\gamma}\right)
\end{aligned}$$
Thus, $\pi_{*}\left(T_{f \mathrm{~d} p_{\alpha} \mathrm{d} x_{\beta}}\right)$ is equal to the current induced by the smooth form
$$\left(\int_{\mathbb{R}^{m-n}} f \mathrm{~d} p_{\alpha}\right) \mathrm{d} x_{\beta} .$$
Expressed in this way, it is also clear that it acts on multivectors as described in (3.2).
Now, we show the result in the general case. For $x \in W \subset X-f(\partial M)$, let $\rho$ be a nonnegative function on $X$ supported within $W$ and equal to 1 on a neighborhood $W^{\prime}$ of $x$. Let $\omega^{\prime}:=(\rho \circ f) \omega$. This form is compactly supported and
$$\left.\left\{f_{*} \omega^{\prime}\right\}\right|_{W^{\prime}}=\left.\left\{f_{*} \omega\right\}\right|_{W^{\prime}},\left.\quad\left\{f_{*} T_{\omega^{\prime}}\right\}\right|_{W^{\prime}}=\left.\left\{f_{*} T_{\omega}\right\}\right|_{W^{\prime}} .$$
As $f$ is a submersion on $f^{-1}(W)$, for each $p \in f^{-1}(W) \subset M$, there are open neighborhoods $V_{p} \subset M$ of $p$ and $W_{p} \subset W$ of $f(p)$ and diffeomorphisms
$$\varphi: \mathbb{R}^{m} \longrightarrow V_{p}, \quad \psi: W_{p} \longrightarrow \mathbb{R}^{n} \quad \text { such that } \quad \psi \circ f \circ \varphi=\pi: \mathbb{R}^{m} \longrightarrow \mathbb{R}^{n}$$
is the projection onto the last $n$ coordinates. By compactness, finitely many $V_{p}$ cover $\operatorname{supp}\left(\omega^{\prime}\right)$. Using a partition of unity, decompose $\omega^{\prime}$ as a sum of forms $\omega_{p}^{\prime}$ each supported in one of these $V_{p}$. Therefore,
$$\left.\left\{f_{*} \omega^{\prime}\right\}\right|_{W^{\prime}}=\left.\sum_{p}\left\{f_{*} \omega_{p}^{\prime}\right\}\right|_{W^{\prime}},\left.\quad\left\{f_{*} T_{\omega^{\prime}}\right\}\right|_{W^{\prime}}=\left.\sum_{p}\left\{f_{*} T_{\omega_{p}^{\prime}}\right\}\right|_{W^{\prime}}, \quad \text { and }\left.\quad\left\{f_{*} \omega_{p}^{\prime}\right\}\right|_{W^{\prime}}=\left.T_{\left\{f_{*} \omega_{p}^{\prime}\right\}}\right|_{W^{\prime}} \forall p ;$$
the last statement follows from the previous paragraph. Along with (3.3), this implies the claimed equality $\left.\left\{f_{*} T_{\omega}\right\}\right|_{W}=T_{\left.\left\{f_{*} \omega\right\}\right\}_{W}}$. \(\square\)

Integration along the fiber is our main method of constructing differential forms. We will apply it in the following general situation, which covers Example 3.8, Lemma 5.1, and Proposition 5.3. We have a manifold $X$, a moduli space $M_{0}$ of unmarked parameterized submanifolds in $X$ (in our setting, pseudoholomorphic curves), a moduli space $M_{1}$ of marked submanifolds in $X$, and the maps
$$\mathfrak{f}: M_{1} \longrightarrow M_{0} \quad \text { and } \quad \text { ev }: M_{1} \longrightarrow X$$
which forget the marked point and evaluate at the marked point, respectively. The map $\operatorname{ev}_{\left.\right|_{\mathfrak{f}}-1}(p)$ is then the parameterization of the submanifold corresponding to $p \in M_{0}$. If dvol is a volume form on $M_{0}$, then we think of the current $\mathrm{ev}_{*} T_{\mathrm{f}^{*} \mathrm{~d} \text { vol }}$ on $X$ as being given by the integral over dvol of the currents of integration of the submanifolds parameterized by $M_{0}$. The following lemma justifies this intuition.

Lemma 3.5. Let $X$ and $M_{0}$ be oriented manifolds and dvol be a compactly supported form of top degree on $M_{0}$. Let $M_{1}$ be an oriented manifold with boundary and
$$\mathfrak{f}: M_{1} \longrightarrow M_{0} \quad \text { and } \quad \text { ev }: M \longrightarrow X$$
be a proper submersion and a smooth map, respectively. For every form $\alpha$ of degree $\operatorname{dim} M_{1}-\operatorname{dim} M_{0}$ compactly supported in $X-\operatorname{ev}\left(\partial M_{1}\right)$,
$$\left\{\mathrm{ev}_{*} T_{\mathfrak{f}^{*} \mathrm{~d} v o l}\right\}(\alpha)=(-1)^{\left(\operatorname{dim} M_{0}\right)\left(\operatorname{dim} M_{1}-\operatorname{dim} M_{0}\right)} \int_{p \in M_{0}}\left(\int_{\mathfrak{f}^{-1}(p)} \operatorname{ev}^{*} \alpha\right) \mathrm{d} v o l .$$
Proof. By definition,
$$\left\{\mathrm{ev}_{*} T_{\mathfrak{f}^{*} \mathrm{~d} v o l}\right\}(\alpha)=\int_{M_{1}} \mathfrak{f}^{*} \mathrm{~d} v o l \wedge \mathrm{ev}^{*} \alpha=(-1)^{\left(\operatorname{dim} M_{0}\right)\left(\operatorname{dim} M_{1}-\operatorname{dim} M_{0}\right)} \int_{M_{1}} \mathrm{ev}^{*} \alpha \wedge \mathfrak{f}^{*} \mathrm{~d} v o l$$
Integration along the fibers of $\mathfrak{f}$ (or Fubini's theorem) yields
$$\int_{M_{1}} \operatorname{ev}^{*} \alpha \wedge \mathfrak{f}^{*} \mathrm{~d} v o l=\int_{p \in M_{0}}\left(\int_{\mathfrak{f}^{-1}(p)} \operatorname{ev}^{*} \alpha\right) \mathrm{d} v o l .$$
This equality does not follow directly from (3.2) because $\mathrm{ev}^{*} \alpha$ may not be compactly supported, so the pushforward of $T_{\mathrm{ev}^{*} \alpha}$ is not a priori well-defined. However, the form $\mathrm{ev}^{*} \alpha \wedge \mathfrak{f}^{*} \mathrm{~d} v o l$ is compactly supported in the interior of $M_{1}$ and the proof of Lemma 3.4 applies to this case without change. \(\square\)

Equation (3.4) gives geometric information about $\mathrm{ev}_{*} T_{f^{*} \mathrm{~d} v o l}$ as a current. By Lemma 3.4, $\mathrm{ev}_{*} T_{f^{*} \mathrm{~d} v o l}$ is smooth on the interior of $X-\operatorname{ev}\left(\partial M_{1}\right)$ if ev is a submersion. We would like to use Equation (3.4) to understand the associated differential form. This is the purpose of the following two lemmas, both of which follow from basic linear algebra.

Lemma 3.6. Let $(X, J)$ be an almost complex 4-manifold, $\omega$ be a 2-form on $X$, and $T_{\omega}$ be the associated current. If $T_{\omega}(\alpha)=0$ for every compactly supported $J$-anti-invariant 2-form $\alpha$, then $\omega$ is $J$-invariant.

Proof. If $\alpha$ is a $J$-anti-invariant 2-form and $\beta$ is a $J$-invariant 2-form, then $\alpha \wedge \beta=0$. For a 2-form $\omega$, define
$$\omega_{+}=\frac{\omega(-,-)+\omega(J-, J-)}{2} \quad \text { and } \quad \omega_{-}=\frac{\omega(-,-)-\omega(J-, J-)}{2} .$$
It is clear that $\omega_{+}$is $J$-invariant, $\omega_{-}$is $J$-anti-invariant, and $\omega=\omega_{+}+\omega_{-}$. If $\omega$ is not $J$-invariant, then $\omega_{-} \neq 0$. Therefore, there exists a 2-form $\alpha$ such that $\omega_{-} \wedge \alpha \neq 0$. By the above,
$$\omega \wedge \alpha_{-}=\omega_{-} \wedge \alpha_{-}=\omega_{-} \wedge \alpha \neq 0 .$$
Therefore, after multiplying by a suitable bump function $\rho, \rho \alpha_{-}$is a compactly supported $J$-anti-invariant 2-form such that $T_{\omega}\left(\rho \alpha_{-}\right) \neq 0$. \(\square\)

Lemma 3.7. Let $(X, J)$ be an almost complex 4-manifold with positive volume form d vol, $\omega$ be a 2-form on $X$, and $T_{\omega}$ be the associated current. If
$$T_{\omega}(\mathrm{d} \operatorname{vol}(\xi \wedge J \xi,-)) \geq 0 \quad \forall \xi \in \Gamma_{c}(X, T X),$$
then $\omega$ is semipositive. In particular, if $T_{\omega}(\alpha) \geq 0$ for every semipositive $\alpha$, then $\omega$ is semipositive.
Proof. We prove the contrapositive. Suppose there exists a vector $v$ such that $\omega(v, J v)<0$. Extend it to a compactly supported vector field $\xi$ on $X$ such that $\omega(\xi(x), J \xi(x)) \leq 0$ for every $x \in X$. Thus,
$$T_{\omega}(\mathrm{d} \operatorname{vol}(\xi(x) \wedge J \xi(x),-))=\int_{X} \omega \wedge \mathrm{~d} \operatorname{vol}(\xi(x) \wedge J \xi(x),-)=\int_{X} \omega(\xi(x), J \xi(x)) \mathrm{d} \operatorname{vol}<0,$$
as claimed. \(\square\)

Below, we prove a special case of Theorem 1 to demonstrate the use of Lemmas 3.4-3.7.
Example 3.8. Let $(X, J)$ be a closed almost complex 4-manifold and $G$ be a compact connected Lie group which acts transitively on $X$ preserving $J$. Let $u: \Sigma \longrightarrow X$ be a pseudoholomorphic map from a closed connected Riemann surface $\Sigma$. If $u_{*}[\Sigma]$ has positive self-intersection number, then ( $X, J$ ) is tamed by a symplectic form $\omega$ which is $G$-invariant, $J$-invariant, and Poincaré dual to $u_{*}[\Sigma]$.

Proof. Define
$$\begin{array}{rlrl}
\mathfrak{f}: G \times \Sigma \longrightarrow G, & & \mathfrak{f}(g, z) & =g, \\
\text { ev: } G \times \Sigma \longrightarrow X, & \operatorname{ev}(g, z) & =g(u(z)) .
\end{array}$$
Let $\mathrm{d} \mu$ be an invariant volume form on $G$ with $\int_{G} \mathrm{~d} \mu=1$ (i.e. the Haar measure). As $G$ acts transitively on $X$, ev is a submersion. By Lemma 3.4, $\omega:=\mathrm{ev}_{*} \mathrm{f}^{*}(\mathrm{~d} \mu)$ is a well-defined 2-form on $X$. Let $\alpha \in \Omega^{2}(X)$. By (3.2) and (3.4),
$$T_{\omega}(\alpha)=\int_{g \in G}\left(\int_{\Sigma}(g u)^{*} \alpha\right) \mathrm{d} \mu .$$
By (3.5) and the $G$-invariance of $\mathrm{d} \mu, \omega$ is $G$-invariant. By (3.5) and the pseudoholomorphicity of $g u$, $T_{\omega}(\alpha)=0$ if $\alpha$ is $J$-anti-invariant and $T(\alpha) \geq 0$ if $\alpha$ is semipositive. Therefore, by Lemmas 3.6 and 3.7, $\omega$ is $J$-invariant and semipositive. As $G$ is connected, the maps $g u$ are homotopic to $u$. Therefore, if $\alpha$ is closed,
$$\int_{g \in G}\left(\int_{\Sigma}(g u)^{*} \alpha\right) \mathrm{d} \mu=\left(\int_{\Sigma} u^{*} \alpha\right)\left(\int_{G} \mathrm{~d} \mu\right)=\int_{\Sigma} u^{*} \alpha .$$
Thus, $\omega$ is Poincaré dual to $u_{*}[\Sigma]$. Since $u_{*}[\Sigma]$ has positive self-intersection number, $\int_{X} \omega^{2}>0$, so $\omega$ has full rank at some point of $X$. As $\omega$ is $G$-invariant and $G$ acts transitively on $X, \omega$ has full rank everywhere. Therefore, it is a symplectic form taming $J$. \(\square\)

\subsection*{3.2 Structure currents}

In this section, we recall some basic facts from Sullivan's theory of structure currents. The primary reference is [23]. Structure currents are used in two distinct ways in this paper. The first is that complex cycles, which form the conceptual core of the present work, are structure currents. The second is that structure currents provide the necessary geometric control on the "bad" set appearing in the proof of Proposition 5.3.

A compact convex cone in a locally convex topological vector space $V$ is a convex cone $\Lambda$ so that there exists a linear functional $L$ on $V$ such that $L(\Lambda-0) \subset(0, \infty)$ and $L^{-1}(1) \cap \Lambda$ is compact. A cone structure on a manifold $X$ is a closed subset $A \subset X$ and a continuous family of compact convex cones $\Lambda_{x} \subset \bigwedge^{p}\left(T_{x} X\right)$ with $x \in A$ for some $p \in \mathbb{Z}^{\geq 0}$.

Definition 3.9. Let $\Lambda$ be a cone structure on a manifold $X$. A current $T$ on $X$ is a structure current with respect to $\Lambda$ or a $\Lambda$-current if it belongs to the closed convex cone generated by the Dirac currents associated to multivectors in $\Lambda$. A structure current $T$ is called a structure cycle if $\partial T=0$.

Remark 3.10. There is a subtlety in the above definition. The closure is taken with respect to the strong dual topology, not the (perhaps more familiar) weak topology. However, this does not actually present a problem, due to the following result of Schwartz [20, Chapitre III, Théorème XIII]: a sequence of currents converges in the strong topology if and only if it converges in the weak topology. That is, a sequence of $k$-currents $T_{i}$ converges to $T$ in the strong topology if $T_{i}(\alpha)$ converges to $T(\alpha)$ for every $k$-form $\alpha$. It is therefore often easy to check that a current is a structure current.
Remark 3.11. We refer to a cone structure $\Lambda^{\prime}$ as being slightly larger than another cone structure $\Lambda$ if $\Lambda-0$ is contained in the interior of $\Lambda^{\prime}$, as subsets of $\bigwedge^{p} T X$. This means, in particular, that the closed subset of $X$ on which $\Lambda^{\prime}$ is defined is larger than that for $\Lambda$. However, in the context of this paper, the underlying closed subsets are somewhat immaterial and this subtlety does not really make a difference.

If $(X, J)$ is a closed almost complex manifold and $\Lambda$ is the cone of complex bivectors, then Sullivan calls $\Lambda$-cycles complex cycles. For this specific type of structure cycle, we find it more convenient to use the following alternative definition. The proof of Proposition 1.1 carries through unchanged using Definition 3.12 (see [3, Proposition 1.7]).

Definition 3.12. A 2-form $\alpha$ on an almost complex manifold is strictly positive if $\alpha(v, J v)>0$ for all $v \neq 0 \in T_{x} X$ and $x \in X$. A 2-current $T$ on a compact almost complex manifold $X$ is a complex cycle if $\partial T=0$ and $T(\alpha)>0$ for all strictly positive 2-forms.

Example 3.13. A closed pseudoholomorphic curve gives rise to a complex cycle, as in Example 3.1. Such complex cycles are exceptionally well-behaved; see [12] for more pathological examples.

Adding an arbitrarily small positive form to a semipositive form results in a positive form, so every semipositive form is a limit of positive forms. Therefore, $T(\alpha) \geq 0$ for every complex cycle $T$ on $X$ and every semipositive form $\alpha$. This fact is used in the proof of Lemma 3.14 below.

Lemma 3.14. Let $\alpha$ be a semipositive form on $X$ and $T$ be a complex cycle on $X$. If $\alpha$ is strictly positive somewhere on $\operatorname{supp}(T)$, then $T(\alpha)>0$.

Proof. Suppose that $\alpha$ is strictly positive at $x \in \operatorname{supp}(T)$. Let $U \subset X$ be a precompact open neighborhood of $x$ such that $\alpha$ is strictly positive on $\bar{U}$. Choose a form $\beta \in \Omega_{c}^{2}(U)$ with $T(\beta)>0$. By the compactness of $\bar{U}$, there exists $\varepsilon>0$ such that $\alpha-\varepsilon \beta$ is a semipositive form on a neighborhood of $\operatorname{supp}(T)$. Therefore,
$$T(\alpha)=\varepsilon T(\beta)+T(\alpha-\varepsilon \beta)>0,$$
as claimed. \(\square\)

The rest of this section is devoted to some results about general structure currents. The following results are applied in this paper not to complex cycles, but to other structure cycles. It is well-known that every loop in Euclidean space bounds a 2-chain: one simply extends radially. The following lemma highlights a geometric aspect of this radial extension.

Lemma 3.15. Let $X$ be a smooth manifold, $\Lambda$ be a cone structure on $X$, and $\iota: \bar{D} \longrightarrow X$ be a smooth embedding of a closed disk such that the image of $\mathrm{d} \iota$ lies in $\Lambda$. Then, for any slightly larger cone structure $\Lambda^{\prime}$, there exists $\varepsilon>0$ such that, if $f: S^{1} \longrightarrow X$ is a smooth map $\varepsilon$-close to $\left.\iota\right|_{\partial \bar{D}}$ in $C^{1}$, then there is a $\Lambda^{\prime}$-current $T$ with $\partial T=f_{*}\left[S^{1}\right]$.

Proof. By taking appropriate coordinates, we may assume $\iota$ is the inclusion of the set
$$\bar{D}=\left\{\left(x_{1}, x_{2}, 0, \ldots, 0\right) \in \mathbb{R}^{n}: x_{1}^{2}+x_{2}^{2} \leq 1\right\} \subset \mathbb{R}^{n} .$$
In particular, $\iota(r x)=r \iota(x)$ for $x \in \bar{D}$ and $r \in[0,1]$. In polar coordinates, define
$$\widehat{f}: \bar{D} \longrightarrow \mathbb{R}^{n}, \quad \widehat{f}(r, \theta):=\operatorname{rf}(\theta) .$$
The map $\widehat{f}$ is smooth on $\bar{D}-0$. If $\left.\widehat{f}\right|_{\partial \bar{D}}:=f$ is $C^{1}$-close to $\left.\iota\right|_{\partial \bar{D}}$, then $\widehat{f}$ is $C^{1}$-close to $\iota$ on $\bar{D}-0$ by the scaling symmetry of $\widehat{f}$ and $\iota$. If $\widehat{f}$ is sufficiently close to $\iota$ in $C^{1}$ on $\bar{D}-0$, then the image of $\mathrm{d} \widehat{f}$ lies in $\Lambda^{\prime}$. For $r \in(0,1)$, let $A_{r}$ be the annulus resulting from removing a disk of radius $r$ from $\bar{D}$. As $\left.\widehat{f}\right|_{A_{r}}$ is smooth, the $\Lambda^{\prime}$-current
$$T_{r}: \Omega_{c}^{2}(X) \longrightarrow \mathbb{R}, \quad T_{r}(\alpha):=\int_{A_{r}} \widehat{f}^{*} \alpha,$$
is well-defined. Let $T:=\lim _{r \rightarrow 0} T_{r}$; it is a $\Lambda^{\prime}$-current. By Stokes' theorem, $\partial T=f_{*}\left[S^{1}\right]$. \(\square\)

Remark 3.16. As the space of $\Lambda^{\prime}$-currents is a closed convex cone, it follows from Lemma 3.15 that any current in the convex hull of the currents of integration over curves $\varepsilon$-close in $C^{1}$ to $\left.\iota\right|_{\partial \bar{D}}$ is the boundary of a $\Lambda^{\prime}$-current. This applies, for instance, to the integral over a measured family thereof, in the sense of Lemma 3.5.
The next lemma is essentially [23, Proposition I.9]. Although it is not emphasized, it is clear that the smoothing procedure described can be applied just on an open set, leaving the rest unchanged; i.e. smoothing can be done in a relative manner. That is the content of Lemma 3.17.

Lemma 3.17. Let $X$ be a smooth manifold, $K \subset X$ be compact, and $\Lambda$ be a cone structure on $X$. Let $T$ be a closed current such that $\left.T\right|_{\operatorname{int} K}$ is a $\Lambda$-current and $T$ is smooth on a neighborhood of $X-\operatorname{int} K$. For any slightly larger cone structure $\Lambda^{\prime}$, there is an exact current $S$ supported in $\operatorname{int} K$ such that $T+S$ is a smooth $\Lambda^{\prime}$-current.

The proof of the next lemma follows the same line as that of Lemma 3.7.

Lemma 3.18. Let $X$ be an oriented 4-manifold, dvol be a volume form on $X$, and $\Lambda$ be a cone structure on $X$. Let $\omega$ be a smooth 2-form such that $T_{\omega}$ is a $\Lambda$-current. If $x \in X$ and $v \in \bigwedge^{2}\left(T_{x} X\right)$ is a bivector such that $\mathrm{d} \operatorname{vol}(v, w)>0$ for every $w \in \Lambda_{x}$, then $\omega(v) \geq 0$.

Proof. Suppose $v$ satisfies $\omega(v)<0$ and $\mathrm{d} \operatorname{vol}(v, w)>0$ for every $w \in \Lambda_{x}$. Extend it to a compactly supported bivector field $\eta$ on $X$ such that $\omega(\eta(x)) \leq 0$ and $\mathrm{d} \operatorname{vol}(\eta(x), w) \geq 0$ for every $x \in X$ and every $w \in \Lambda$. As $\omega(v)<0$,
$$T_{\omega}(\mathrm{d} \operatorname{vol}(\eta(x),-))=\int_{X} \omega \wedge \mathrm{~d} \operatorname{vol}(\eta(x),-)=\int_{X} \omega(\eta(x)) \mathrm{d} \operatorname{vol}<0,$$
contradicting the fact that $T_{\omega}$ is a $\Lambda$-current. \(\square\)

\section*{4 Preliminaries: curves}

In this section, we recall the necessary perturbation theory for pseudoholomorphic curves. Proposition 4.1 below collects the input on the local structure of moduli spaces of $J$-holomorphic curves needed for our purposes. It is a variation on [13, Theorem 2] and [15, Lemma 1.5.1]. We deduce it from [13, 15, 22] in Appendix A.

Let $(X, J)$ be an almost complex manifold. We recall that a pseudoholomorphic curve is a pseudo-holomorphic map $u: \Sigma \longrightarrow X$ from a Riemann surface, considered up to reparameterization. If $\Sigma$ is connected, the curve is called irreducible. We call a half-dimensional submanifold $Y \subset X$ totally real if $T Y \cap J(T Y)=Y$. By the Carleman Similarity Principle [17, Theorem 2.3.5], a non-constant $J$-holomorphic map $u: \Sigma \longrightarrow X$ from a connected Riemann surface, possibly with boundary, determines a complex line subbundle $\mathcal{T} u \subset u^{*} T X$ containing $\mathrm{d} u(T \Sigma)$. We denote by
$$\mathcal{N} u:=\frac{u^{*} T X}{\mathcal{T} u} \longrightarrow \Sigma$$
the normal bundle of $u$. If $\left.u\right|_{\partial \Sigma}$ is an embedding with the image contained in a totally real submanifold $Y \subset X$, then the normal bundle
$$\mathcal{N}_{Y}(\partial u):=\frac{\left\{\left.u\right|_{\partial \Sigma}\right\}^{*} T Y}{\mathrm{~d} u(T(\partial \Sigma))} \longrightarrow \partial \Sigma$$
of $\partial u:=\left.u\right|_{\partial \Sigma}$ in $Y$ is a real subbundle of $\left.\mathcal{N} u\right|_{\partial \Sigma}$ (the embedding condition can be bypassed in general). If, in addition, $\Sigma$ is compact, we denote by $\mu_{Y}^{\mathcal{N}}(u)$ the Maslov index of the bundle pair $\left(\mathcal{N} u, \mathcal{N}_{Y}(\partial u)\right)$ over $(\Sigma, \partial \Sigma)$; see [17, Appendix C.3].

We define the genus $g(\Sigma)$ of a compact connected Riemann surface $\Sigma$ with $b$ boundary components by
$$2-2 g(\Sigma)=\chi(\Sigma)+b,$$
where $\chi(\Sigma)$ is the Euler characteristic of $\Sigma$. If $(X, J)$ is an almost complex manifold, $Y \subset X$ is a submanifold, and $g, b \in \mathbb{Z}^{\geq 0}$, we denote
\begin{itemize}
\item[-] by $\mathfrak{M}_{(g, b)}(X, Y)$ the moduli space of equivalence classes of non-constant $J$-holomorphic maps $u: \Sigma \longrightarrow X$ from compact connected genus $g$ Riemann surfaces with $b$ boundary components such that $u(\partial \Sigma) \subset Y$,
\end{itemize}
\begin{itemize}
\item[-] by $\mathfrak{M}_{(g, b), 1}(X, Y)$ the moduli space of equivalence classes of pairs $\left(u, z_{0}\right)$ with $u: \Sigma \longrightarrow X$ as above and $z_{0} \in \Sigma$, and
\item[-] by $\mathfrak{M}_{(g, b), 1}^{\circ}(X, Y) \subset \mathfrak{M}_{(g, b), 1}(X, Y)$ the subspace of pairs $\left[u, z_{0}\right]$ as above so that $z_{0} \notin \partial \Sigma$.
\end{itemize}
Define
$$\begin{aligned}
\mathfrak{f}: \mathfrak{M}_{(g, b), 1}(X, Y) & \longrightarrow \mathfrak{M}_{(g, b)}(X, Y), & \mathfrak{f}\left(\left[u, z_{0}\right]\right) & =[u], \\
\text { ev: } \mathfrak{M}_{(g, b), 1}(X, Y) & \longrightarrow X, & \operatorname{ev}\left(\left[u, z_{0}\right]\right) & =u\left(z_{0}\right) .
\end{aligned}$$

Proposition 4.1. Suppose $(X, J)$ is an almost complex 4-manifold, $Y \subset X$ is a totally real surface, $g, b \in \mathbb{Z}^{\geq 0}$, and $[u: \Sigma \longrightarrow X] \in \mathfrak{M}_{(g, b)}(X, Y)$. If $\left.u\right|_{\partial \Sigma}$ is an embedding and $\mu_{Y}^{\mathcal{N}}(u) \geq 4 g+2 b+1$, then
\begin{itemize}
\item[(1)] a neighborhood $\mathfrak{M}_{0}$ of $[u]$ in $\mathfrak{M}_{(g, b)}(X, Y)$ is a smooth manifold;
\item[(2)] the subspace $\mathfrak{M}_{1}:=\mathfrak{f}^{-1}\left(\mathfrak{M}_{0}\right)$ of $\mathfrak{M}_{(g, b), 1}(X, Y)$ is a smooth manifold with boundary and the maps
$$\mathfrak{f}: \mathfrak{M}_{1} \longrightarrow \mathfrak{M}_{0} \quad \text { and } \quad \text { ev: } \mathfrak{M}_{1}^{\circ}:=\mathfrak{M}_{1} \cap \mathfrak{M}_{(g, b), 1}^{\circ}(X, Y) \longrightarrow X-Y$$
are smooth submersions;
\item[(3)] for every $x_{0} \in X-Y$, the subspace $\mathfrak{M}_{1}^{\circ}\left(x_{0}\right):=\mathrm{ev}^{-1}\left(x_{0}\right) \cap \mathfrak{M}_{1}$ of $\mathfrak{M}_{1}^{\circ}$ is a smooth submanifold with
$$\operatorname{dim} \mathfrak{M}_{1}^{\circ}\left(x_{0}\right)=\operatorname{dim} \mathfrak{M}_{1}-2 ;$$
\item[(4)] for every $x_{0} \in X-Y$ and $v_{0} \in T_{x_{0}} X$ nonzero, the subspace $\mathfrak{M}_{1}^{\circ}\left(v_{0}\right) \subset \mathfrak{M}_{1}^{\circ}\left(x_{0}\right)$ of pairs $\left[u^{\prime}, z_{0}\right]$ such that $\left.v_{0} \in \mathcal{T} u^{\prime}\right|_{z_{0}}$ is a smooth submanifold with
$$\operatorname{dim} \mathfrak{M}_{1}^{\circ}\left(v_{0}\right)=\operatorname{dim} \mathfrak{M}_{1}-4 .$$
\end{itemize}
We note that the assumption that $X$ has dimension 4 is essential. In higher dimensions, no condition on the Maslov index alone is sufficient to guarantee that the conclusions of Proposition 4.1 hold; see [13, Remark (3)]. We also emphasize that a submersion is not necessarily surjective.

Definition 4.2. Let $(X, J)$ be an almost complex manifold. A closed pseudoholomorphic curve $C \subset X$ is free if it admits a pseudoholomorphic parameterization $u: \Sigma \longrightarrow X$ which satisfies (1) and (2) of Proposition 4.1 with $Y=\emptyset$.

Example 4.3. The lines in $\mathbb{C P}^{2}$ and the smooth fibers of a surface bundle over a surface are free.
If an immersed surface $S$ has $n$ points of self-intersection, all of which are positive transverse double points, then $S$ is said to have $n$ nodes. An immersed surface $S$ is said to have $n$ nodes if some arbitrarily small perturbation of $S$ has $n$ nodes. This notion is referred to as having $\delta$-invariant $n$ in some contexts in algebraic geometry.

Example 4.4. Let $(X, J)$ be an almost complex 4-manifold and $C \subset X$ be an immersed pseudoholomorphic curve of genus $g$ with $n$ nodes. Let $u: \Sigma \longrightarrow X$ be a pseudoholomorphic parameterization of $C$. It follows from the proof of Proposition 4.1 in Appendix A that $C$ is free if
$$4 g-1 \leq \mu_{\emptyset}^{\mathcal{N}}(u)=2\left\langle c_{1}(\mathcal{N} u),[\Sigma]\right\rangle .$$
This and the Adjunction Inequality [17, Theorem 2.6.4] imply that if $C$ has self-intersection number at least $2 g+2 n$, then it is free.

Proposition 4.1 shows that a pseudoholomorphic curve in an almost complex 4-manifold with sufficiently large Maslov index admits many deformations. Lemma 4.5 below shows that boundary conditions can be chosen to make the Maslov index arbitrarily large.

Lemma 4.5. Let $(X, J)$ be a closed almost complex 4-manifold and $u: \Sigma \longrightarrow X$ be a nonconstant pseudoholomorphic map from a closed connected Riemann surface. For any $M \in \mathbb{Z}^{\geq 0}$ and open subset $U \subset X$ such that $u(\Sigma) \cap U \neq \emptyset$, there exists a totally real surface $Y \subset U$ and a curve $\gamma$ bounding an open disk $D \subset \Sigma$ such that $u(\bar{D}) \subset U, u(\gamma) \subset Y$, and
$$\mu_{Y}^{\mathcal{N}}\left(\left.u\right|_{\Sigma-D}\right) \geq M .$$
Proof. Pick a simple closed curve $\gamma \subset u^{-1}(U)$ bounding an open disk $D \subset \Sigma$ so that $\left.u\right|_{\bar{D}}$ is an embedding. The normal bundle $\mathcal{N} u$ trivializes over $\bar{D}$. Associate $\left.\mathcal{N} u\right|_{\bar{D}}$ with a complement to $d u(T \bar{D})$ in $T X$. Take a section $\xi$ of $\mathcal{N} u$ along $\gamma$ such that the winding number around the zero section is $2\left\langle c_{1}(\mathcal{N} u),[\Sigma]\right\rangle-M$. Since $u$ is pseudoholomorphic, the subbundle of $T X$ generated by $\xi$ and $T \gamma$ is totally real. This is an open property, so flowing for a short time under the exponential map of $\xi$ yields a totally real surface $Y \subset U$. By [17, Theorem C.3.5],
$$2\left\langle c_{1}(\mathcal{N} u),[\Sigma]\right\rangle=\mu_{\emptyset}^{\mathcal{N}}(u)=\mu_{Y}^{\mathcal{N}}\left(\left.u\right|_{\Sigma-D}\right)+\mu_{Y}^{\mathcal{N}}\left(\left.u\right|_{\bar{D}}\right)=\mu_{Y}^{\mathcal{N}}\left(\left.u\right|_{\Sigma-D}\right)+\left(2\left\langle c_{1}(\mathcal{N} u),[\Sigma]\right\rangle-M\right) .$$
This gives (4.4). \(\square\)

\section*{5 Construction of Poincaré dual}

In this section, we use integration along the fiber to produce a well-behaved Poincaré dual to a pseudoholomorphic curve. The main result of this section is Proposition 5.3. Its proof is based on the proof of Lemma 5.1, but with additional complications. If the curve $C$ fails to be sufficiently flexible, we have to vary it as a curve with boundary. Lemma 4.5 shows that boundary conditions can be chosen to make the curve as flexible as one wishes. Integration along the fiber then produces a current which is well-behaved away from a small "bad" set. We then appeal to Lemma 5.2 to control the resulting current on this small set.

Lemma 5.1. Let $(X, J)$ be a closed almost complex 4-manifold and $C$ be a closed pseudoholomorphic curve on $X$. If $C$ is free, then it is Poincaré dual to a semipositive form $\omega$.

Proof. Let $u_{0}: \Sigma \longrightarrow X$ be a pseudoholomorphic parameterization of $C$. With notation as in Proposition 4.1, let
$$\mathfrak{f}: \mathfrak{M}_{1} \longrightarrow \mathfrak{M}_{0} \text { and ev : } \mathfrak{M}_{1}=\mathfrak{M}_{1}^{\circ} \longrightarrow X$$
be the forgetful and evaluation maps, respectively. Since $C$ is free, $\mathfrak{M}_{0}$ and $\mathfrak{M}_{1}^{\circ}$ are smooth manifolds and ev is a submersion. Let $\mathrm{d} \nu$ be a compactly supported nonnegative form on $\mathfrak{M}_{0}$ such that $\int_{\mathfrak{M}_{0}} \mathrm{~d} \nu=1$. By Lemma 3.4 with $U=X, \omega=\mathrm{ev}_{*} f^{*} \mathrm{~d} \nu$ is a well-defined (smooth) 2-form on $X$.

Let $\alpha \in \Omega^{2}(X)$. By (3.4),
$$T_{\omega}(\alpha)=\int_{u \in \mathfrak{M}_{0}}\left(\int_{\Sigma} u^{*} \alpha\right) \mathrm{d} \nu .$$
As $u$ is pseudoholomorphic for every $u \in \mathfrak{M}_{0}, T_{\omega}(\alpha) \geq 0$ for every semipositive 2-form $\alpha$. Therefore, $\omega$ is semipositive by Lemma 3.7. Since $u$ is homotopic to $u_{0}$ for all $u \in \mathfrak{M}_{0}$,
$$\int_{X} \omega \wedge \alpha=T_{\omega}(\alpha)=\int_{u \in \mathfrak{M}_{0}}\left(\int_{\Sigma} u^{*} \alpha\right) \mathrm{d} \nu=\left(\int_{C} \alpha\right)\left(\int_{\mathfrak{M}_{0}} \mathrm{~d} \nu\right)=\int_{\Sigma} u_{0}^{*} \alpha$$
if $\alpha$ is a closed 2-form on $X$. Therefore, $\omega$ is Poincaré dual to $C$. \(\square\)

Let $(X, J)$ be an almost complex 4-manifold with a Riemannian metric and
$$\eta:=\xi \wedge J \xi \in \Gamma\left(X, \bigwedge^{2} T X\right)$$
be a continuous field of unit complex bivectors, i.e. $|\eta|=1$. For $\delta \geq 0$, define
$$\Lambda_{\delta}:=\left\{w \in \bigwedge^{2} T_{x} X: x \in X, \quad|w-|w| \eta(x)| \leq \delta|w|\right\} \subset \bigwedge^{2} T X .$$
For any closed subset $A \subset X,\left.\Lambda_{\delta}\right|_{A}$ is a cone structure on $X$.
Lemma 5.2. Let $\varphi$ be a semipositive form on $X$ and $A \subset X$ be a compact subset so that $\varphi(\eta(x))>0$ for all $x \in A$. There exists $\delta>0$ such that for every 2-form $\omega$ so that $T_{\omega}$ is a $\left.\Lambda_{\delta}\right|_{A}$-current, there exists $K>0$ such that $\omega+K \varphi$ is a semipositive form on $X$.

Proof. Let dvol be the volume form on $X$ determined by the Riemannian metric and $J$. Define
$$\mathbb{G}_{2}^{+}(X):=\{u \wedge J u: u \in T X,|u \wedge J u|=1\} \subset \bigwedge^{2} T X .$$
If $\delta \geq 0$ and $x \in X$, then
$$\mathrm{d} \operatorname{vol}(v, w) \geq\left.(\mathrm{d} \operatorname{vol}(\eta(x), v)-\delta)|w| \quad \forall v \in \mathbb{G}_{2}^{+}(X)\right|_{x},\left.\quad w \in \Lambda_{\delta}\right|_{x} .$$
Since distinct elements of $\mathbb{G}_{2}^{+}(X)$ determine disjoint (except at 0) tangent 2-planes on $X$, the continuous functions
$$\mathbb{G}_{2}^{+}(X) \longrightarrow \mathbb{R}^{\geq 0}, \quad v \mapsto|v-\eta(x)|,\left.\mathrm{d} \operatorname{vol}(\eta(x), v) \quad \forall v \in \mathbb{G}_{2}^{+}(X)\right|_{x}, x \in X,$$
vanish only along $\eta$. Since $\left.\mathbb{G}_{2}^{+}(X)\right|_{A}$ is compact, it follows that for every $\varepsilon>0$, there exists $\delta>0$ such that
$$x \in A,\left.\quad v \in \mathbb{G}_{2}^{+}(X)\right|_{x}, \quad \mathrm{~d} \operatorname{vol}(\eta(x), v) \leq\left.\delta \Longrightarrow v \in \Lambda_{\varepsilon}\right|_{x} .$$
Along with (5.2), the last implication gives
$$x \in A,\left.\quad v \in \mathbb{G}_{2}^{+}(X)\right|_{x},\left.\quad w \in \Lambda_{\delta}\right|_{x}, \quad \mathrm{~d} \operatorname{vol}(v, w) \leq\left. 0 \Longrightarrow v \in \Lambda_{\varepsilon}\right|_{x} .$$
Since $\left.\mathbb{G}_{2}^{+}(X)\right|_{A}$ is compact and $\varphi>0$ on $\left.\Lambda_{0}\right|_{A}$, there exist $\varepsilon, c>0$ such that $\varphi \geq c$ on $\left.\Lambda_{\varepsilon} \cap \mathbb{G}_{2}^{+}(X)\right|_{A}$. Let $\delta>0$ be as in (5.3) and assume that $\omega$ is a 2-form on $X$ such that $T_{\omega}$ is a $\left.\Lambda_{\delta}\right|_{A}$-current. Let $x \in A$ and $v \in \mathbb{G}_{2}^{+}(X)$. By (5.3), either $\varphi(v) \geq c$ or $\mathrm{d} v o l(v, w)>0$ for all $\left.w \in \Lambda_{\delta}\right|_{x}$. By Lemma 3.18, $\omega(v) \geq 0$ in the latter case. Thus, for each $\left.v \in \mathbb{G}_{2}^{+}(X)\right|_{A}$, either $\varphi(v) \geq c$ or $\omega(v) \geq 0$.

Since $\left.\mathbb{G}_{2}^{+}(X)\right|_{A}$ is compact,
$$K:=-\inf _{\substack{\left.v \in \mathbb{G}_{+}^{+}(X)\right|_{A} \\ \omega(v)<0}} \frac{\omega(v)}{\varphi(v)}$$
is a finite positive number (if $\omega(v) \geq 0$ for all $\left.v \in \mathbb{G}_{2}^{+}(X)\right|_{A}$, simply take $K=0$ ). By the definition of $K$ and the semipositivity of $\varphi, \omega+K \varphi$ is nonnegative on $\left.\mathbb{G}_{2}^{+}(X)\right|_{A}$. Since the support of $\omega$ is contained in $A$ (because it is a $\left.\Lambda_{\delta}\right|_{A}$-current), it follows that $\omega+K \varphi$ is a semipositive form on $X$. \(\square\)

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/a52b6a2b-0ae6-445a-b314-32ddf532bd19-18.jpg?height=515&width=1616&top_left_y=294&top_left_x=252}
\captionsetup{labelformat=empty}
\caption{Figure 1: The construction of the form $\omega_{C}^{\prime}$ in the proof of Proposition 5.3. We start with a curve $C$ and an open set $U$ intersecting $C$. We remove a small disk from $C$ and vary it in a family of pseudoholomorphic curves with boundary. Integration over this family produces the current $T_{\varepsilon}$, the boundary of which is supported in $U$. We then fill in the boundary by a current $T$. Smoothing the current $T_{\varepsilon}+T$ results in the form $\omega_{C}^{\prime}$.}
\end{figure}

Proposition 5.3. Let $(X, J)$ be a closed almost complex 4-manifold. Let $C$ be a closed irreducible pseudoholomorphic curve in $X$ and $\varphi$ a semipositive form on $X$ such that
$$\int_{C} \varphi>0 .$$
Then, there exist a closed 2-form $\omega_{C}$ on $X$ and a constant $K>0$ such that
\begin{itemize}
\item[(1)] $\omega_{C}$ is Poincaré dual to $C$,
\item[(2)] $\omega_{C}$ is $J$-invariant on $X-\operatorname{supp}(\varphi)$,
\item[(3)] $\omega_{C}+K \varphi$ is a semipositive form, and
\item[(4)] $\omega_{C}+K \varphi$ is strictly positive on a neighborhood of $C$.
\end{itemize}
Proof. We show that there exist a closed 2-form $\omega_{C}^{\prime}$ and a constant $K^{\prime}>0$ such that $\omega_{C}^{\prime}+K^{\prime} \varphi$ is strictly positive on a neighborhood of $C-\operatorname{supp}(\varphi)$ and (1), (2), and (3) hold with $\omega_{C}$ and $K$ replaced by $\omega_{C}^{\prime}$ and $K^{\prime}$, respectively. In the last paragraph, we use this to prove the full claim.

Fix a Riemannian metric on $X$. Let $u_{0}: \Sigma \longrightarrow X$ be a pseudoholomorphic parameterization of $C$. As $C$ is irreducible, $\Sigma$ is connected. By [17, Lemma 2.4.1, Proposition 2.5.1], $u_{0}$ is an embedding away from a finite set of points. By assumption, there is an embedded point of $C$ at which $u_{0}^{*} \varphi>0$. Take a small contractible neighborhood $U \subset X$ of this point and a (continuous) field $\eta:=\xi \wedge J \xi$ of unit complex bivectors on $\bar{U}$ tangent to $C$ along $C$ so that $\varphi(\eta(x))>0$ for all $x \in \bar{U}$. With $\Lambda_{\delta} \subset \bigwedge^{2} T X$ as in (5.1), fix $\delta$ as in Lemma 5.2 with $A=\bar{U}$.

Let $g$ be the genus of $\Sigma$ and $M=4 g+3$. Let $D \subset \Sigma$ and $Y \subset U$ be as in Lemma 4.5 with $u=u_{0}$. With the notation as in Proposition 4.1 with $u=\left.u_{0}\right|_{\Sigma-D}$, let
$$\mathfrak{f}: \mathfrak{M}_{1} \longrightarrow \mathfrak{M}_{0} \text { and ev : } \mathfrak{M}_{1} \longrightarrow X$$
be the forgetful and evaluation maps, respectively; both maps are smooth, while $\mathfrak{f}$ is also a proper submersion. For each $\varepsilon>0$, let $\mathrm{d} \nu_{\varepsilon}$ be a nonnegative form of top degree on $\mathfrak{M}_{0}$ that is supported on curves $\varepsilon$-close in $C^{1}$ to $\left.u_{0}\right|_{\Sigma-D}$, is nonzero at $\left.u_{0}\right|_{\Sigma-D}$, and satisfies $\int_{\mathfrak{M}_{0}} \mathrm{~d} \nu_{\varepsilon}=1$.

Define the 2-current $T_{\varepsilon}:=\mathrm{ev}_{*}\left(\mathfrak{f}^{*} \mathrm{~d} \nu_{\varepsilon}\right)$ on $X$ as in (3.1) with $f=\mathrm{ev}$. By (3.4),
$$T_{\varepsilon}(\alpha)=\int_{u \in \mathfrak{M}_{0}}\left(\int_{\Sigma-D} u^{*} \alpha\right) \mathrm{d} \nu_{\varepsilon} \quad \forall \alpha \in \Omega^{2}(X) .$$
We now show that $T_{\varepsilon}$ is well-behaved on $X-U$. Since $\operatorname{ev}\left(\partial \mathfrak{M}_{1}\right) \subset Y \subset U, T_{\varepsilon}$ is smooth on a neighborhood $W_{\varepsilon} \subset X$ of $X-U$ by Lemma 3.4, i.e. $\left.T_{\varepsilon}\right|_{W_{\varepsilon}}=T_{\omega_{\varepsilon}}$ for some (smooth) 2-form $\omega_{\varepsilon}$ on $W_{\varepsilon}$. Since each map $u$ is $J$-holomorphic, (5.4) implies that $T_{\varepsilon}(\alpha)=0$ for $J$-anti-invariant $\alpha$. By Lemma 3.6, $\omega_{\varepsilon}$ is thus a $J$-invariant 2-form on $W_{\varepsilon}$.

Let $x_{0} \in W_{\varepsilon}$ and $v_{0} \in T_{x_{0}} X$. By (3.2),
$$\omega_{\varepsilon}\left(v_{0}, J v_{0}\right)=\int_{\mathrm{ev}^{-1}\left(x_{0}\right)}\left\{f^{*} \mathrm{~d} \nu_{\varepsilon}\right\}\left(-, \widetilde{v_{0}}, \widetilde{J v_{0}}\right),$$
where $\widetilde{v_{0}}, \widetilde{J v_{0}} \in \Gamma\left(\mathrm{ev}^{-1}\left(x_{0}\right) ; T \mathfrak{M}_{1}\right)$ are the lifts of $v_{0}$ and $J v_{0}$, respectively, along dev. The sign of $\omega_{\varepsilon}\left(v_{0}, J v_{0}\right)$ depends on the orientation of the fiber, which we now describe. The manifold $\mathfrak{M}_{0}$ is oriented so $\mathrm{d} \nu_{\varepsilon}$ is nonnegative and $\mathfrak{M}_{1}$ is oriented by giving the fibers of the forgetful map $\mathfrak{f}$ their complex orientations as Riemann surfaces. The manifold $X$ is oriented by the almost complex structure $J$. The orientation of the fiber of ev is determined by requiring that the wedge product of the lift of an orientation form on $X$ and an orientation form on $\mathrm{ev}^{-1}\left(x_{0}\right)$ gives a form along $\mathrm{ev}^{-1}\left(x_{0}\right)$ which agrees with the orientation on $\mathfrak{M}_{1}$. It follows that $\left.\left\{\mathfrak{f}^{*} \mathrm{~d} \nu_{\varepsilon}\right\}\left(-, \widetilde{v_{0}}, \widetilde{J v_{0}}\right)\right|_{T e \mathrm{v}^{-1}\left(x_{0}\right)}$ at a point $(u, z) \in \mathrm{ev}^{-1}\left(x_{0}\right)$ is zero if $\left.v_{0} \in \mathcal{T} u\right|_{z}$ and a positively oriented form in the top degree otherwise. Therefore, $\omega_{\varepsilon}\left(v_{0}, J v_{0}\right) \geq 0$, i.e. $\omega_{\varepsilon}$ is semipositive on $W_{\varepsilon}$.

Suppose, in addition, that $x_{0} \in u_{0}(\Sigma-\bar{D})$. By (4.2) and (4.3), there then exists a surface $u \in \mathfrak{M}_{0}$ arbitrarily close to $\left.u_{0}\right|_{\Sigma-D}$ passing through $x_{0}$ transverse to $v_{0} \wedge J v_{0}$. Therefore, $\omega_{\varepsilon}$ is a strictly positive form along $C-U$. As strict positivity is an open condition, $\omega_{\varepsilon}$ is strictly positive on a neighborhood $W_{\varepsilon}^{\prime} \subset W_{\varepsilon}$ of $C-U$.

We have shown that $\omega_{\varepsilon}$ is well-behaved on $X-U$. We now modify it on $U$ to produce a 2-form $\omega_{C}^{\prime}$ which is well-behaved everywhere. By (5.4) and Stokes' theorem,
$$\left\{\partial T_{\varepsilon}\right\}(\beta):=T_{\varepsilon}(\mathrm{d} \beta)=-\int_{u \in \mathfrak{M}_{0}}\left(\int_{\partial \bar{D}} u^{*} \beta\right) \mathrm{d} \nu_{\varepsilon} \quad \forall \beta \in \Omega^{1}(X) .$$
By Lemma 3.15 with $\Lambda=\Lambda_{\delta}$ and Remark 3.16, there exists a current $T$ supported in $U$ with $\partial T=-\partial T_{\varepsilon}$. For $\delta_{1} \in(0, \delta)$, if $\varepsilon$ is sufficiently small, both $T_{\varepsilon}$ and $T$ are $\Lambda_{\delta_{1}}$-currents in $\bar{U}$. Thus, $T_{\varepsilon}+T$ is a cycle which is a $\Lambda_{\delta_{1}}$-current on $\bar{U}$ and smooth on a neighborhood of $X-U$. Therefore, by Lemma 3.17, there exists an exact current $S$ supported in $U$ such that
$$T_{\varepsilon}^{\prime}:=T_{\varepsilon}+T+S$$
is a smooth, closed current that is a $\Lambda_{\delta}$-current on $\bar{U}$. Let $\omega_{C}^{\prime}$ be the 2-form on $X$ so that $T_{\varepsilon}^{\prime}=T_{\omega_{C}^{\prime}}$. By Lemma 5.2, there exists $K^{\prime}>0$ such that $\omega_{C}^{\prime}+K^{\prime} \varphi$ is semipositive on $\bar{U}$. As $\omega_{C}^{\prime}$ is equal to $\omega_{\varepsilon}$
on a neighborhood of $X-U, \omega_{C}^{\prime}$ is $J$-invariant on $X-U$ and $\omega_{C}^{\prime}+K^{\prime} \varphi$ is semipositive everywhere and strictly positive on a neighborhood of $C-U$.

The last property of $\omega_{C}^{\prime}$ that remains to be proved is that it is Poincaré dual to $C$. As the curves in $\mathfrak{M}_{0}$ are homologous relative to $U$, it follows from (5.4) that
$$T_{\varepsilon}(\alpha)=\int_{u \in \mathfrak{M}_{0}}\left(\int_{\Sigma-D} u^{*} \alpha\right) \mathrm{d} \nu_{\varepsilon}=\left(\int_{\Sigma-D} u_{1}^{*} \alpha\right)\left(\int_{\mathfrak{M}_{0}} \nu_{\varepsilon}\right)=\int_{\Sigma-D} u_{1}^{*} \alpha$$
for $\alpha \in \Omega^{2}(X)$ supported in $X-U$. This implies the second equality in
$$\left[\omega_{C}^{\prime}\right]=\left[T_{\varepsilon}\right]=u_{0 *}[\Sigma-D]=[C] \in H_{2}(X, U ; \mathbb{R}) .$$
As $U$ is contractible, the long exact sequence in relative homology implies that the equality $\left[\omega_{C}^{\prime}\right]=[C]$ in $H_{2}(X, U ; \mathbb{R})$ lifts to an equality $\left[\omega_{C}^{\prime}\right]=[C]$ in $H_{2}(X ; \mathbb{R})$. Thus, $\omega_{C}^{\prime}$ is Poincaré dual to $C$.

We have thus constructed a 2-form $\omega_{C}^{\prime}$ on $X$ and $K^{\prime}>0$ such that $\omega_{C}^{\prime}+K^{\prime} \varphi$ is positive on a neighborhood of $C-\operatorname{supp}(\varphi)$ and (1), (2), and (3) hold with $\omega$ replaced by $\omega_{C}^{\prime}$ and $K$ by $K^{\prime}$. We can decompose $\varphi$ as $\varphi=\varphi_{1}+\varphi_{2}+\varphi_{3}$, where $\varphi_{i}$ is semipositive for $i \in\{1,2,3\}, \int_{C} \varphi_{i}>0$ for $i \in\{1,2\}$, and $\operatorname{supp}\left(\varphi_{1}\right) \cap \operatorname{supp}\left(\varphi_{2}\right)=\emptyset$. Construct $\omega_{1}^{\prime}$ and $K_{1}^{\prime}>0$ with respect to $\varphi_{1}$ and $\omega_{2}^{\prime}$ and $K_{2}^{\prime}>0$ with respect to $\varphi_{2}$, as before. The form $\omega_{C}:=\frac{1}{2}\left(\omega_{1}^{\prime}+\omega_{2}^{\prime}\right)$ and the positive constant $K:=\frac{1}{2}\left(K_{1}^{\prime}+K_{2}^{\prime}\right)$ satisfy (1), (2), (3), and (4), as claimed. \(\square\)

\section*{6 Proofs of the main theorems}

In this section, we prove the results stated in Section 1. Proposition 5.3 implies Theorems 3 and 2. Theorem 2 then implies Theorem 1.