---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Monopole metrics and the orbifold Yamabe problem]

---
source_file: Monopole_metrics_and_the_orbifold_Yamabe_problem_75a6a8fcbfc3.pdf
converter: mathpix
format: mmd
---

\section*{ANNALES}

\section*{DE}

\title{
L'INSTITUT FOURIER
}

\author{
Jeff A. VIACLOVSKY
}

Monopole metrics and the orbifold Yamabe problem
Tome 60, n° 7 (2010), p. 2503-2543.
<http://aif.cedram.org/item?id=AIF_2010__60_7_2503_0>
© Association des Annales de l'institut Fourier, 2010, tous droits réservés.

L'accès aux articles de la revue « Annales de l'institut Fourier » (http://aif.cedram.org/), implique l'accord avec les conditions générales d'utilisation (http://aif.cedram.org/legal/). Toute reproduction en tout ou partie cet article sous quelque forme que ce soit pour tout usage autre que l'utilisation à fin strictement personnelle du copiste est constitutive d'une infraction pénale. Toute copie ou impression de ce fichier doit contenir la présente mention de copyright.

\title{
MONOPOLE METRICS AND THE ORBIFOLD YAMABE PROBLEM
}

\author{
by Jeff A. VIACLOVSKY (*)
}

\begin{abstract}
We consider the self-dual conformal classes on $n \not \prod^{-} \mathbb{C P}^{2}$ discovered by LeBrun. These depend upon a choice of $n$ points in hyperbolic 3-space, called monopole points. We investigate the limiting behavior of various constant scalar curvature metrics in these conformal classes as the points approach each other, or as the points tend to the boundary of hyperbolic space. There is a close connection to the orbifold Yamabe problem, which we show is not always solvable (in contrast to the case of compact manifolds). In particular, we show that there is no constant scalar curvature orbifold metric in the conformal class of a conformally compactified non-flat hyperkähler ALE space in dimension four.
\end{abstract}

RÉSUMÉ. - Nous considérons les classes conformes auto-duales sur $n \neq \mathbb{C P}^{2}$ introduites par LeBrun. Elles dépendent du choix de $n$ points dans l'espace hyperbolique de dimension 3, appelés points de monopôle. Nous étudions les limites de diverses métriques de courbure scalaire constante dans ces classes conformes lorsque ces points se rapprochent ou tendent vers le bord de l'espace hyperbolique. Il existe une relation étroite avec le problème de Yamabe sur les orbifolds qui n'admet pas toujours de solution (contrairement au cas des variétés compactes). En particulier, nous montrons qu'il n'existe pas de métrique d'orbifold de courbure scalaire constante dans la classe conforme d'un espace ALE hyperkählérien conformément compact en dimension 4.

\section*{Contents}
1. Introduction ..... 2504
2. Monopole metrics ..... 2510
3. The Yamabe invariant ..... 2514
4. The orbifold Yamabe invariant ..... 2517
5. Symmetric metrics ..... 2522
6. Integral formulas ..... 2526
7. Orbifold convergence ..... 2530
8. Questions ..... 2539
Bibliography ..... 2540

\footnotetext{
Keywords: Monopole Metrics, Orbifold Yamabe Problem.
Math. classification: 53C21, 53C25.
(*) Research partially supported by NSF Grant DMS-0804042.
}

\section*{1. Introduction}

There is an interesting history regarding the existence of self-dual metrics on $n \# \mathbb{C P}^{2}$ beginning with work of Yat-Sun Poon [39]. Using techniques from twistor theory, Poon proved the existence of a 1-parameter family of self-dual conformal classes on $\mathbb{C P}^{2} \# \mathbb{C P}^{2}$ and that any such conformal class with positive scalar curvature must be in this family. Examples for larger $n$ were found by Donaldson-Friedman [17] and Floer [18] using gluing methods. In 1991, Claude LeBrun [32] produced explicit examples with U(1)-symmetry on $n \# \mathbb{C P}^{2}$, using a hyperbolic ansatz inspired by the Gibbons-Hawking ansatz [19]. LeBrun's construction depends on the choice of $n$ points in hyperbolic 3-space $\mathcal{H}^{3}$. For $n=2$, the only invariant of the configuration is the distance between the monopole points, and LeBrun conformal classes are the same as the 1-parameter family found by Poon.

\subsection*{1.1. Limits of LeBrun metrics}

The first question we address in this paper: is there a nice compactification of the moduli space of LeBrun metrics on $n \neq \mathbb{C P}^{2}$ ? In general, as the monopole points limit towards each other, or if the points approach the boundary of hyperbolic space, some degeneration will occur. We emphasize that the LeBrun construction produces conformal classes on $n \not \prod^{-} \mathbb{P}^{2}$. To discuss convergence in the Cheeger-Gromov sense, one needs to choose a conformal factor. Of course, the limit will strongly depend on the particular choice of conformal metrics. Some degenerations were already described in [32] and [17], but these examples depended on a somewhat arbitrary choice of conformal factor.

The solution of the Yamabe problem provides one with a very natural metric in these conformal classes. However, the abstract existence theorem does not tell one what the actual minimizer looks like in any particular case, and other methods are needed to understand the geometry of minimizers. The main point of this paper is to describe the limiting behavior of the Yamabe minimizers in these conformal classes as they degenerate. In general, Yamabe minimizers are not necessarily unique; an example of nonuniqueness is given Theorem 1.1. We also examine the existence and limiting behavior of various non-minimizing constant scalar curvature metrics. Given a subgroup of the conformal automorphism group, Hebey-Vaugon have shown there is a minimizer of the Yamabe functional when restricted to the class of invariant functions (the equivariant Yamabe problem), and
these automorphisms will act as isometries on the minimizer [21]. Of course, a symmetric Yamabe minimizer can have higher energy than a Yamabe minimizer, and an example of this is seen in Theorem 1.1.

If $G \subset \operatorname{SO}(4)$ is a finite subgroup acting freely on $S^{3}$, then we let $G$ act on $S^{4} \subset \mathbb{R}^{5}$ acting as rotations around the $x_{5}$-axis. The quotient $S^{4} / G$ is then a orbifold, with two singular points, and the spherical metric $g_{S}$ descends to this orbifold. Near the singular points, the metric is asymptotic to a cone metric $\mathcal{C}\left(S^{3} / G\right)$, thus $S^{4} / G$ looks like a United States "football". In the following, $G \subset \operatorname{SU}(2)$ will be a certain cyclic subgroup $\mathbb{Z}_{m}$, see (2.2) below. For a smooth Riemannian manifold $(M, g)$, the Yamabe invariant of the conformal class is denoted by $Y(M,[g])$, see Section 3. If $(M, g)$ is an orbifold, then $Y_{\text {orb }}(M,[g])$ will denote the orbifold Yamabe invariant, see Section 4.

We first discuss the special case of $n=2$. To employ the equivariant Yamabe problem, one must first understand the group of conformal automorphisms: it was proved in [25] that the conformal group $G$ of Poon's metrics for $n=2$ is given by
$$G=(\mathrm{U}(1) \times \mathrm{U}(1)) \ltimes D_{4},$$
where $D_{4}$ is the dihedral group of order 8. There is the index 2 subgroup given by
$$K=(\mathrm{U}(1) \times \mathrm{U}(1)) \ltimes\left(\mathbb{Z}_{2} \oplus \mathbb{Z}_{2}\right),$$
which are exactly the lifts of hyperbolic isometries preserving the set of 2 monopole points. In contrast, for $n>2$, any conformal automorphism of a LeBrun metric is a lift of an isometry of $\mathcal{H}^{3}$. There is an "extra" involution when $n=2$, which is not a lift of any hyperbolic isometry, see [25]. Let $d_{H}(\cdot, \cdot)$ denote hyperbolic distance.

Theorem 1.1. - Let $(M, g)$ be a Poon-LeBrun metric on $\mathbb{C P}^{2} \# \mathbb{C P}^{2}$ with monopole points $p_{1}$ and $p_{2}$. The Yamabe invariant satisfies the sharp estimate
$$8 \pi \sqrt{3}=Y_{\text {orb }}\left(S^{4} / \mathbb{Z}_{2},\left[g_{S}\right]\right)<Y(M,[g])<Y\left(\mathbb{C P}^{2},\left[g_{F S}\right]\right)=12 \pi \sqrt{2} .$$
There exists a number $N$ large, such that if $d_{H}\left(p_{1}, p_{2}\right)>N$ then the following holds. There are two distinct Yamabe minimizers, each limiting to $g_{F S}$ on $\mathbb{C P}^{2}$ as $d_{H}\left(p_{1}, p_{2}\right) \rightarrow \infty$. In each case, there is one singular point of convergence at which a Burns metric bubbles off. The symmetric $K$-Yamabe minimizers limit to $\left(S^{4}, g_{S}\right)$ as $d_{H}\left(p_{1}, p_{2}\right) \rightarrow \infty$, with 2 antipodal singular points of convergence, with Burns metrics bubbling off at each of the singular points. There is a fourth constant scalar curvature metric, limiting
to $\mathbb{C P}^{2} \vee \mathbb{C P}^{2}$ (the wedge of two copies of $\mathbb{C P}^{2}$ with Fubini-Study metrics, touching at a single point) as $d_{H}\left(p_{1}, p_{2}\right) \rightarrow \infty$. In this case, a Euclidean Schwarzschild metric with two asymptotically flat ends bubbles off.

As $d_{H}\left(p_{1}, p_{2}\right) \rightarrow 0$, the limit of both the Yamabe minimizers and the symmetric $K$-Yamabe minimizers is the $S^{4} / \mathbb{Z}_{2}$-football with the round metric. In both cases, at each singular point an Eguchi-Hanson metric bubbles off.

These limits are illustrated in Figure 1.1. An important point is that the properties of being self-dual and having constant scalar curvature form an elliptic system [45]. In Tian-Viaclovsky [46, 47], it was shown that limits of such metrics may have at worst multi-fold singularities, provided that the sequence has bounded $L^{2}$-norm of curvature and does not collapse. The crucial ingredient of this theory is the upper volume growth estimate proved in [45]. For other results dealing with this type of convergence in various settings, see [1, 2, 6, 7, 10, 14, 16, 15, 37, 44]. In the situation considered in this paper, the $L^{2}$-curvature bound follows from the Chern-Gauss-Bonnet formula and Hirzebruch signature theorem. The non-collapsing condition will follow from uniform positivity of the Yamabe invariant.

As mentioned above, the LeBrun monopole construction depends upon the choice of $n$ points in hyperbolic space. An easy generalization of this construction allows one to assign integer multiplicities greater than one at the monopole points. The resulting space will have orbifold points. We call such a space a LeBrun orbifold. Next, for $n>2$, we present the following compactness theorem.

Theorem 1.2. - Let $(M, g)$ be a LeBrun self-dual conformal class on $n \# \mathbb{C P}^{2}$ with monopole points $\left\{p_{1}, \ldots, p_{n}\right\}$. Then
$$Y(M,[g]) \leqslant Y\left(\mathbb{C P}^{2},\left[g_{F S}\right]\right)=12 \pi \sqrt{2},$$
with strict inequality for $n \geqslant 2$, where $g_{F S}$ denotes the Fubini-Study metric. Next, assume that all monopole points are contained in a compact set $\mathcal{K} \subset \mathcal{H}^{3}$. Then there exists a constant $\delta_{n}$ depending only upon $n, \mathcal{K}$ such that
$$0<\delta_{n} \leqslant Y(M,[g]) .$$
Furthermore, any sequence of unit volume Yamabe minimizers in a sequence of LeBrun conformal classes (for fixed n) satisfying (1.5) has a subsequence which converges (in the Cheeger-Gromov sense) to either to (1) a compactified LeBrun orbifold metric with $1 \leqslant k \leqslant n$ points or (2) the round metric on $S^{4} / \mathbb{Z}_{m}$, for some $2 \leqslant m \leqslant n$. In addition, the estimate (1.5) is

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/50d7fd11-ad3f-44a7-acda-195a5ccbacd5-06.jpg?height=1060&width=1065&top_left_y=255&top_left_x=242}
\captionsetup{labelformat=empty}
\caption{Figure 1.1. The 5 limiting cases described in Theorem 1.1. The left side is as $d\left(p_{1}, p_{2}\right) \rightarrow \infty$. The top left is the symmetric $K$-Yamabe minimizer. The middle left are the two Yamabe minimizers. The lower left is the metric obtained by Joyce gluing. The right hand side is as $d\left(p_{1}, p_{2}\right) \rightarrow 0$. In this case, the Yamabe minimizers and the symmetric Yamabe minimizers have the same limiting behavior. Note that in each of the above cases, to obtain $\mathbb{C P}^{2} \# \mathbb{C P}^{2}$ topologically, the attaching map for one of the factors should be orientation reversing.}
\end{figure}
true for $n=2,3$ without the requirement that the points are contained in a compact set $\mathcal{K}$.

There can exist sequences of Yamabe minimizers with limiting behavior as in Case (1); this limit can occur when some of the monopole points limit to the boundary of $\mathcal{H}^{3}$, as seen in Theorem 1.1. Another example is given in

Theorem 1.5 below. There also can exist sequences limiting as in Case (2), as seen in Theorem 1.1.

The estimate for the lower bound in (1.5) is not explicit, this is proved by a contradiction argument in Section 7. It would be very interesting to find a sharp constant. We conjecture that $\delta_{n}=Y_{\text {orb }}\left(S^{4} / \mathbb{Z}_{n},\left[g_{S}\right]\right)$, without any requirement that the monopole points are contained in a compact set $\mathcal{K}$. For $n=2,3$, the uniform positivity of the Yamabe invariant holds for topological reasons, see Proposition 6.1.

We mention that the degeneration of the LeBrun conformal classes can also be studied using twistor theory. For this important perspective, we refer the reader to the recent paper of Nobuhiro Honda [24].

\subsection*{1.2. The orbifold Yamabe problem}

Akutagawa and Botvinnik considered the Yamabe problem on orbifolds in [4, 5] in which they proved several foundational results. We will describe this in more detail in Section 4. Since the limits described above are typically orbifolds, it is no surprise that there is a close connection with the orbifold Yamabe problem. In fact, an important tool in identifying the possible limit spaces above is the following nonexistence result.

Theorem 1.3. - Let $\left(X_{n}, g\right)$ be a hyperkähler ALE metric in dimension 4, with group $G$ of order $n>1$ at infinity, and let $(\hat{X},[\hat{g}])$ denote the orbifold conformal compactification. Then $Y_{\text {orb }}(\hat{X},[\hat{g}])=Y_{\text {orb }}\left(S^{4} / G,\left[g_{S}\right]\right)$, and there is no solution to the orbifold Yamabe problem on $(\hat{X},[\hat{g}])$. That is, there is no conformal metric $\tilde{g}=e^{2 u} \hat{g}$ having constant scalar curvature.

This will be proved in Section 4 along with some other remarks on the orbifold Yamabe problem. The ALE metrics above, can be viewed as the Green's function metrics $g_{p}=\Gamma_{p}^{2} \hat{g}$ of the orbifold compactification, where $\Gamma_{p}$ is the Green's function for the conformal Laplacian of $\hat{g}$ based at the orbifold point $p$. It is interesting that these ALE spaces have zero mass and their compactifications do not admit a solution of the orbifold Yamabe problem. This shows that the orbifold Yamabe problem is more subtle than in the case of smooth manifolds.

In Section 7, we will prove another nonexistence result regarding the negative mass ALE spaces found in [31].

Theorem 1.4. - If $(X, g)$ is a LeBrun negative mass ALE metric on $\mathcal{O}(-n)$ with $n>1$, then there is no symmetric solution of the orbifold Yamabe problem on $(\hat{X}, \hat{g})$ invariant under $\mathrm{SU}(2)$.

As a consequence, the symmetric Yamabe problem on orbifolds is not always solvable either. For $n=2$, this metric is the same as the compactified Eguchi-Hanson metric, which does not admit any constant scalar curvature metric by Theorem 1.3. We do not know if there is a non-symmetric solution on these orbifolds for $n \geqslant 3$.

Finally, we present an existence result for the orbifold Yamabe problem, which for simplicity we state here in only the case of total multiplicity 3 (see Corollary 4.4 for the general statement). The following theorem also shows that LeBrun orbifold metrics can in fact arise as a limit of smooth Yamabe metrics in LeBrun conformal classes, and also $k$ can be strictly less than $n$ in Case (1) of Theorem 1.2.

Theorem 1.5. - Let $(M,[g])$ be compact self-dual LeBrun orbifold corresponding to a monopole point $p_{1}$ of multiplicity 1 and a monpole point $p_{2}$ of multiplicity 2 , with $p_{1} \neq p_{2}$. Then there exists a radius $r>0$ such that if $d_{\mathcal{H}}\left(p_{1}, p_{2}\right)<r$, then $(M,[g])$ admits a solution to the orbifold Yamabe problem. Furthermore, let $\left(M_{1},\left[g_{j}\right]\right)$ be a self-dual LeBrun conformal class on $3 \# \mathbb{C P}^{2}$ corresponding to 3 distinct monopole points all of multiplicity one, with $p_{1}$ and $p_{2}$ fixed, and $p_{2}, p_{j, 3} \in B\left(p_{1}, r\right)$. Then as $p_{j, 3} \rightarrow p_{2}$, a subsequence of Yamabe minimizers on $\left(M_{1},\left[g_{j}\right]\right)$ converges to an orbifold Yamabe metric on $(M,[g])$. There is one singular point of convergence, at which an Eguchi-Hanson metric bubbles off.

Next, let $p_{1}$ and $p_{2}$ be fixed and let $p_{j, 3}$ limit to the boundary of $\mathcal{H}^{3}$ as $j \rightarrow \infty$. Then any sequence of Yamabe minimizers on ( $M_{1},\left[g_{j}\right]$ ) has a subsequence which converges to a Yamabe minimizer in the 2-pointed smooth LeBrun conformal class ( $2 \# \mathbb{C P}^{2},\left[\hat{g}_{L B}\left(p_{1}, p_{2}\right)\right]$ ). There is one singular point of convergence, at which a Burns metric bubbles off.

Remark 1.6. - It is possible that $r$ could be taken to be infinite in the above theorem, but this would require a much more involved estimate of the Yamabe invariant.

\subsection*{1.3. Acknowledgements}

The author would like to thank first and foremost, Claude LeBrun, for originally suggesting this problem and providing extremely helpful comments along the way. Peter Kronheimer and Clifford Taubes also provided very helpful suggestions early on. Nobuhiro Honda provided crucial assistance in understanding the conformal geometry of LeBrun metrics. The author held several valuable discussions with Kazuo Akutagawa regarding
the orbifold Yamabe problem. Denis Auroux, Simon Donaldson, Yat-Sun Poon, and Gang Tian also gave the author some important remarks that proved to be very useful when completing this work. Finally, thanks are given to the anonymous referee whose numerous remarks and suggestions greatly improved the exposition of the paper.

\section*{2. Monopole metrics}

We first recall some basic definitions.
Definition 2.1. - A Riemannian orbifold $\left(M^{n}, g\right)$ is a topological space which is a smooth manifold of dimension $n$ with a smooth Riemannian metric away from finitely many singular points. At a singular point $p, M$ is locally diffeomorphic to a cone $\mathcal{C}$ on $S^{n-1} / G$, where $G \subset S O(n)$ is a finite subgroup acting freely on $S^{n-1}$. Furthermore, at such a singular point, the metric is locally the quotient of a smooth $G$-invariant metric on $B^{n}$ under the orbifold group $G$.

A Riemannian multi-fold $M$ is a connected space obtained from a finite collection of Riemannian orbifolds by finitely many identifications of points. If there is only one cone at a singular point $p$, then $M$ is called irreducible at $p$, otherwise $M$ is called reducible at $p$.

We note that the notions of smooth orbifold, orbifold diffeomorphism, and orbifold Riemannian metric are well-defined, see [46] for background and references. Note also that our definition is very restrictive since we only allow isolated singular points.

Definition 2.2. - A smooth Riemannian manifold $\left(X^{n}, g\right)$ is called an asymptotically locally Euclidean (ALE) end of order $\tau$ if there exists a finite subgroup $G \subset S O(n)$ acting freely on $\mathbf{R}^{n} \backslash B(0, R)$ and a $C^{\infty}$ diffeomorphism $\Psi: X \rightarrow\left(\mathbf{R}^{n} \backslash B(0, R)\right) / G$ such that under this identification,
$$g_{i j}=\delta_{i j}+O\left(r^{-\tau}\right), \quad \partial^{|k|} g_{i j}=O\left(r^{-\tau-k}\right),$$
for any partial derivative of order $k$ as $r \rightarrow \infty$. A complete, noncompact Riemannian orbifold ( $X, g$ ) is called ALE if $X$ can be written as the disjoint union of a compact set and finitely many ALE ends. If all of the groups $G_{j}$ corresponding to the ends are trivial, then $(X, g)$ is called asymptotically flat (AF).

For an integer $m \geqslant 1$, we let $\mathbb{Z}_{m}=\mathbb{Z} / m \mathbb{Z} \subset S U(2)$ be the cyclic group of matrices
$$\left(\begin{array}{cc}
\exp ^{2 \pi i p / m} & 0 \\
0 & \exp ^{-2 \pi i p / m}
\end{array}\right), \quad 0 \leqslant p<m .$$
acting on $\mathbb{R}^{4}$, which is identified with $\mathbb{C}^{2}$ via the map
$$\left(x_{1}, y_{1}, x_{2}, y_{2}\right) \mapsto\left(x_{1}+i y_{1}, x_{2}+i y_{2}\right)=\left(z_{1}, z_{2}\right) .$$

\subsection*{2.1. Gibbons-Hawking ansatz}

We briefly review the construction of Gibbons-Hawking multi-Eguchi-Hanson metrics, from [19, 22], as presented in [8]. We also present a generalization to allow orbifold points, by taking Green's functions with integral weights.

Consider $\mathbb{R}^{3}$ with the flat metric $g_{\mathbb{R}^{3}}=d x^{2}+d y^{2}+d z^{2}$. Choose $n$ distinct points $P=\left\{p_{1}, \ldots, p_{n}\right\} \subset \mathbb{R}^{3}$. For each point $p_{i}$, we assign a multiplicity $m_{i}$, which is an integer satisfying $m_{i} \geqslant 1$, and let $N=\sum_{i=1}^{n} m_{i}$ be the total multiplicity.

Let $\Gamma_{p_{j}}$ denote the fundamental solution for the Euclidean Laplacian based at $p_{j}$ with normalization $\Delta \Gamma_{p_{j}}=-2 \pi \delta_{p_{j}}$, and let
$$V=\frac{1}{2} \sum_{i=1}^{n} m_{i} \Gamma_{p_{i}} .$$
Then $* d V$ is a closed 2-form on $\mathbb{R}^{3} \backslash P$, and $(1 / 2 \pi)[* d V]$ is an integral class in $H^{2}\left(\mathbb{R}^{3} \backslash P, \mathbb{Z}\right)$. Let $\pi: X_{0} \rightarrow \mathbb{R}^{3} \backslash P$ be the unique principal U(1)-bundle determined by the the above integral class. By Chern-Weil theory, there is a connection form $\omega \in H^{1}\left(X_{0}, i \mathbb{R}\right)$ with curvature form $i(* d V)$. The Gibbons-Hawking metric is defined by
$$g_{\mathrm{GH}}=V \cdot g_{\mathbb{R}^{3}}-V^{-1} \omega \odot \omega .$$
Note the minus sign appears, since by convention our connection form is imaginary valued. We define a larger manifold $X$ by attaching points $\tilde{p_{j}}$ over each $p_{j}$.

Remark 2.3. - Choosing a different connection form will result in the same metric, up to diffeomorphism.

We summarize the main properties of $\left(X, g_{\mathrm{GH}}\right)$ in the following proposition.

Proposition 2.4. - The Gibbons-Hawking multi-Eguchi-Hanson metric $\left(X_{0}, g_{\mathrm{GH}}\right)$ extends to $X$ as a smooth Riemannian orbifold metric. At a point $\tilde{p}_{i}$ with multiplicity $m_{i} \geqslant 1, X$ has an orbifold structure with group $\mathbb{Z} / m_{i} \mathbb{Z}$, acting as in (2.2). The space ( $X, g_{G H}$ ) is ALE with a single end of order 4 . The group at infinity is the cyclic group $\mathbb{Z} / N \mathbb{Z}$ acting as in (2.2), where $N$ is the total multiplicity.

Proof. - The smooth case is discussed in [8], and is straightforward to adapt to the orbifold case. \(\square\)

This metric will be denoted by $g_{G H}\left(m_{1} \cdot p_{1}, \ldots, m_{n} \cdot p_{n}\right)$. Note that a small sphere around a $\mathbb{Z}_{m}$-orbifold point is diffeomorphic to the Lens space $L(m, 1)$, and that $X$ is equipped with an isometric $S^{1}$ action, with fixed point set the finite set $\left\{\tilde{p}_{1}, \ldots, \tilde{p}_{n}\right\}$.

\subsection*{2.2. LeBrun hyperbolic ansatz}

We briefly review LeBrun's construction of Kähler scalar-flat metrics on the blow-up of $\mathbb{C}^{2}$ at $n$ points on a line from [32]. As in the Gibbons-Hawking case, we present a generalization which allows orbifold points.

The LeBrun construction [32] is similar to the Gibbons-Hawking construction above, by replacing $\mathbb{R}^{3}$ with the upper half-space model of hyperbolic space
$$\mathcal{H}^{3}=\left\{(x, y, z) \in \mathbb{R}^{3}, z>0\right\},$$
with the hyperbolic metric $g_{\mathcal{H}^{3}}=z^{-2}\left(d x^{2}+d y^{2}+d z^{2}\right)$. Choose $n$ distinct points $P=\left\{p_{1}, \ldots, p_{n}\right\} \subset \mathcal{H}^{3}$. For each point $p_{i}$, we assign a multiplicity $m_{i}$, which is an integer satisfying $m_{i} \geqslant 1$, and let $N=\sum_{i=1}^{n} m_{i}$ be the total multiplicity.

Let $\Gamma_{p_{j}}$ denote the fundamental solution for the hyperbolic Laplacian based at $p_{j}$ with normalization $\Delta \Gamma_{p_{j}}=-2 \pi \delta_{p_{j}}$, and let
$$V=1+\sum_{i=1}^{n} m_{i} \Gamma_{p_{i}} .$$
Then $* d V$ is a closed 2-form on $\mathcal{H}^{3} \backslash P$, and $(1 / 2 \pi)[* d V]$ is an integral class in $H^{2}\left(\mathcal{H}^{3} \backslash P, \mathbb{Z}\right)$. Let $\pi: X_{0} \rightarrow \mathcal{H}^{3} \backslash P$ be the unique principal U(1)-bundle determined by the the above integral class. By Chern-Weil theory, there is a connection form $\omega \in H^{1}\left(X_{0}, i \mathbb{R}\right)$ with curvature form $i(* d V)$. LeBrun's metric is defined by
$$g_{\mathrm{LB}}=z^{2}\left(V \cdot g_{\mathcal{H}^{3}}-V^{-1} \omega \odot \omega\right) .$$

We define a larger manifold $X$ by attaching points $\tilde{p_{j}}$ over each $p_{j}$, and by attaching an $\mathbb{R}^{2}$ at $z=0$. The space $X$ is non-compact, and has the topology of an asymptotically flat space. Adding the point at infinity will result in a compact manifold $\hat{X}$. We summarize the main properties of $\left(X, g_{\mathrm{LB}}\right)$ in the following proposition.

Proposition 2.5 (LeBrun [32]). - The metric $g_{\mathrm{LB}}$ extends to $X$ as a smooth orbifold Riemannian metric. At a point $\tilde{p}_{i}$ with multiplicity $m_{i} \geqslant 1$, $X$ has an orbifold structure with group $\mathbb{Z} / m_{i} \mathbb{Z}$, acting as in (2.2). The space $\left(X, g_{\mathrm{LB}}\right)$ is asymptotically flat Kähler scalar-flat with a single end of order 2. By adding one point, this metric conformally compactifies to a smooth self-dual conformal class on the compactification $\left(\hat{X},\left[\hat{g}_{\mathrm{LB}}\right]\right)$. If all points have multiplicity 1, then $\hat{X}$ is diffeomorphic to $n \not \mathbb{C C P}^{2}$.

Proof. - The smooth case is proved in [32]. Furthermore, the case of one point taken with multiplicity $n$ was also considered in [32, Section 5], and the generalization to several points with multiplicity is straightforward. \(\square\)

The non-compact AF metric will be denoted by $g_{\mathrm{LB}}\left(m_{1} \cdot p_{1}, \ldots, m_{n} \cdot p_{n}\right)$, while a metric on the compactification will typically be denoted by $\hat{g}_{\mathrm{LB}}$. Note that a small sphere around a $\mathbb{Z}_{m}$-orbifold point is diffeomorphic to the Lens space $L(m, 1)$, and that $\hat{X}$ is equipped with a conformal $S^{1}$ action, with fixed point set the finite set $\left\{\tilde{p}_{1}, \ldots, \tilde{p}_{n}\right\}$ together with an $S^{2}$ corresponding to the boundary of $\mathcal{H}^{3}$. For $n=0$, this construction gives the Euclidean metric on $\mathbb{R}^{4}$, and for $n=1$, it yields the Burns metric, which conformally compactifies to the Fubini-Study metric on $\mathbb{C P}^{2}$. In other words, the Burns metric is the Green's function asymptotically flat space associated to the Fubini-Study metric.

\subsection*{2.3. Negative mass metrics}

In [31], LeBrun presented the first known examples of scalar-flat ALE spaces of negative mass, which gave counterexamples to extending the positive mass theorem to ALE spaces. We briefly describe these as follows. Define
$$g_{O \mathrm{LB}}=\frac{d r^{2}}{1+A r^{-2}+B r^{-4}}+r^{2}\left[\sigma_{1}^{2}+\sigma_{2}^{2}+\left(1+A r^{-2}+B r^{-4}\right) \sigma_{3}^{2}\right],$$
where $r$ is a radial coordinate, and $\left\{\sigma_{1}, \sigma_{2}, \sigma_{3}\right\}$ is a left-invariant coframe on $S^{3}=\operatorname{SU}(2)$, and $A=n-2, B=1-n$. Redefine the radial coordinate to be $\hat{r}^{2}=r^{2}-1$, and attach a $\mathbb{C P}^{1}$ at $\hat{r}=0$. After taking a quotient by $\mathbb{Z}_{n}$,
the metric then extends smoothly over this $\mathbb{C P}^{1}$, is ALE at infinity, and is diffeomorphic to $\mathcal{O}(-n)$. The mass is computed to be $-4 \pi^{2}(n-2)$, which is negative when $n>2$. For $n=1$, this construction yields the Burns metric. For $n=2$, this space is Ricci-flat, and is exactly the metric of Eguchi-Hanson. There is a close connection with the hyperbolic monopole metrics: the conformal compactification of these ALE spaces are confomal to $\hat{g}_{L B}\left(n \cdot p_{1}\right)$, a compactified LeBrun hyperbolic monopole orbifold metric with a single monopole point of multiplicity $n$ [32, Section 5].

\section*{3. The Yamabe invariant}

The Yamabe Problem asks whether there exists a conformal metric with constant scalar curvature on any closed Riemannian manifold, and has been completely solved in the affirmative. We do not attempt to give a history of the Yamabe problem here, for this we refer the reader to [9, 41, 34]. In what follows, let $(M, g)$ be a Riemannian manifold, and let $R$ denote the scalar curvature of $g$. Writing a conformal metric as $\tilde{g}=v^{\frac{4}{n-2}} g$, the Yamabe equation takes the form
$$-4 \frac{n-1}{n-2} \Delta v+R \cdot v=\lambda \cdot v^{\frac{n+2}{n-2}},$$
where $\lambda$ is a constant (note: we use the analyst's Laplacian). These are the Euler-Lagrange equations of the Yamabe functional,
$$\mathcal{Y}(\tilde{g})=\operatorname{Vol}(\tilde{g})^{\frac{2-n}{n}} \int_{M} R_{\tilde{g}} \operatorname{dvol}_{\tilde{g}},$$
for $\tilde{g} \in[g]$, where $[g]$ denotes the conformal class of $g$. An important related conformal invariant is the Yamabe invariant of the conformal class $[g]$ :
$$Y(M,[g]) \equiv \inf _{\tilde{g} \in[g]} \mathcal{Y}(\tilde{g}) .$$
In dimension 4, Aubin's inequality states
$$Y(M,[g]) \leqslant Y\left(S^{4},\left[g_{S}\right]\right)=8 \pi \sqrt{6},$$
with equality if $(M, g)$ is conformally equivalent to $\left(S^{4}, g_{S}\right)$.

\subsection*{3.1. Upper estimate}

Next is an estimate from above on the Yamabe invariant of compactified LeBrun conformal classes. We begin with a short calculation.

Lemma 3.1. - The function $\rho(p)=d_{\mathcal{H}^{3}}(p,(0,0,1))$ satisfies
$$-2+\Delta \rho=4 e^{-2 \rho} V_{1},$$
where
$$V_{1}=1+\Gamma_{(0,0,1)}=1+\frac{1}{e^{2 \rho}-1}=\frac{1}{1-e^{-2 \rho}} .$$

Proof. - Since $\rho$ is the distance function of the hyperbolic metric,
$$\Delta \rho=2 \operatorname{coth} \rho,$$
which yields
$$-2+\Delta \rho=2(\operatorname{coth} \rho-1)=2\left(\frac{e^{\rho}+e^{-\rho}}{e^{\rho}-e^{-\rho}}-1\right)=\frac{4}{e^{2 \rho}-1}=4 e^{-2 \rho} V_{1} .$$ \(\square\)

For purposes of the Yamabe invariant, if $g$ is a $n$-pointed LeBrun metric, then we may assume that $p_{1}=(0,0,1)$. To see this, apply a hyperbolic isometry $\phi$ to arrange so that $p_{1}=(0,0,1)$. By [25, Section 2], there exists a lift of $\phi$ to $\Phi: X_{0} \rightarrow X_{0}$ preserving the connection form. The metric $\Phi^{*} g$ will be conformal to the original, so will have the same Yamabe invariant.

For $n=1$, the compactified LeBrun metric is conformal to $\mathbb{C P}^{2}$ with the Fubini-Study metric $g_{F S}$ [33, Section 3]. Consequently,
$$Y\left(\hat{M},\left[\hat{g}_{L B}\left(p_{1}\right)\right]\right)=12 \pi \sqrt{2}=Y\left(\mathbb{C P}^{2},\left[g_{F S}\right]\right) .$$
For $n>1$ we have the following estimate of the Yamabe invariant.
Theorem 3.2. - Let $\left(\hat{M},\left[\hat{g}_{L B}\right]\right)$ be a Lebrun conformal class on $n \not \mathbb{C P}^{2}$ with $n>1$. Without loss of generality assume that $p_{1}=(0,0,1)$. Then
$$Y\left(\hat{M},\left[\hat{g}_{L B}\right]\right)<12 \pi \sqrt{2}-\beta\left(p_{2}, \ldots p_{n}\right),$$
where $\beta: \mathcal{H}^{3} \times \cdots \mathcal{H}^{3} \rightarrow \mathbb{R}_{+}$, is a positive function, and approaches zero only if every point $p_{2}, \ldots, p_{n}$ approaches the boundary of $\mathcal{H}^{3}$.

Proof. - We consider conformal changes of the form
$$g=e^{2 f}\left(V \cdot g_{H}+V^{-1} \omega \odot \omega\right),$$
where $f: \mathcal{H}^{3} \rightarrow \mathbb{R}$. It is computed in [33] that
$$R_{g}=6 e^{-2 f} V^{-1}\left(-1-\Delta f-|\nabla f|^{2}\right) .$$
We will now take $f=-\rho$ as a test function in the Yamabe functional. The resulting metric $g$ will then be a smooth orbifold metric on the conformal
compactification. Let $V=V_{n}$ correspond to an $n$-pointed LeBrun metric, with $p_{1}=(0,0,1)$. From Lemma 3.1,
$$R_{g}=6 e^{2 \rho} V_{n}^{-1}(\Delta \rho-2)=24 V_{n}^{-1} V_{1}$$
(since $|\nabla \rho|=1$ ). The Yamabe functional evaluated at $g$ is then
$$\mathcal{Y}(g)=\int_{M} R_{g} d V_{g} \cdot\left(\int_{M} d V_{g}\right)^{-1 / 2}=\int_{M} 24 V_{n}^{-1} V_{1} d V_{g} \cdot\left(\int_{M} d V_{g}\right)^{-1 / 2} .$$
We next take a coordinate system $(x, y, z, \theta)$ where $\theta$ is an angular coordinate on the fiber for some trivialization. The volume element is
$$\sqrt{\operatorname{det}(g)}=e^{-4 \rho}\left(V^{3} z^{-6} V^{-1}\right)^{1 / 2}=e^{-4 \rho} V_{n} z^{-3} .$$
In coordinates we then have
$$\mathcal{Y}(g)=\int_{M} 24 V_{1} e^{-4 \rho} z^{-3} d V_{0} \cdot\left(\int_{M} V_{n} e^{-4 \rho} z^{-3} d V_{0}\right)^{-1 / 2},$$
where $d V_{0}=d x \wedge d y \wedge d z \wedge d \theta$. Since the integrand is independent of $\theta$, we may integrate with respect to $\theta$ to obtain
$$\mathcal{Y}(g)=24 \sqrt{2 \pi} \int_{\mathcal{H}^{3}} V_{1} e^{-4 \rho} d V_{\mathcal{H}^{3}} \cdot\left(\int_{\mathcal{H}^{3}} V_{n} e^{-4 \rho} d V_{\mathcal{H}^{3}}\right)^{-1 / 2} .$$
Since $n \geqslant 1$, we must have $V_{n} \geqslant V_{1}$ (with strict inequality for $n>1$ ) and we obtain the estimate
$$\mathcal{Y}(g) \leqslant 24 \sqrt{2 \pi}\left(\int_{\mathcal{H}^{3}} V_{1} e^{-4 \rho} d V_{\mathcal{H}^{3}}\right)^{1 / 2} .$$
Using radial coordinates on $\mathcal{H}^{3}$, we compute that
$$\begin{aligned}
\int_{\mathcal{H}^{3}} V_{1} e^{-4 \rho} d V_{\mathcal{H}^{3}} & =4 \pi \int_{0}^{\infty} \frac{1}{1-e^{-2 \rho}} e^{-4 \rho}(\sinh \rho)^{2} d \rho \\
& =\pi \int_{0}^{\infty}\left(e^{-2 \rho}-e^{-4 \rho}\right) d \rho=\frac{\pi}{4}
\end{aligned}$$
Substituting this into (3.18), we obtain
$$\mathcal{Y}(g) \leqslant 12 \pi \sqrt{2}=Y\left(\mathbb{C P}^{2},\left[g_{F S}[) .\right.\right.$$
If $n>1$, this inequality is strict, and the only way it can be close to saturation is if all the points $p_{i}$ are close to the hyperbolic boundary, since the only inequality used was $V_{1}<V_{n}$. The existence of the function $\beta$ follows easily. \(\square\)

\section*{4. The orbifold Yamabe invariant}

The orbifold Yamabe invariant of an orbifold conformal class is defined as in the smooth case:
$$Y_{o r b}(M,[g])=\inf _{\tilde{g} \in[g]} \operatorname{Vol}(\tilde{g})^{\frac{2-n}{n}} \int_{M} R_{\tilde{g}} d V_{\tilde{g}} .$$
The analogue of Aubin's estimate and basic existence result is as follows.
Theorem 4.1 (Akutagawa-Botvinik [5], Akutagawa [3]). - Let $(M, g)$ be a Riemannian orbifold with singular points $\left\{p_{1}, \ldots, p_{k}\right\}$, with orbifold groups $G_{i} \subset \operatorname{SO}(n), i=1 \ldots k$. Then
$$Y_{\text {orb }}(M,[g]) \leqslant Y\left(S^{n}\right) \min _{i}\left|G_{i}\right|^{-\frac{2}{n}} .$$
Furthermore, if this inequality is strict, then there exists a smooth conformal metric $\tilde{g}=u^{\frac{4}{n-2}} g$ which minimizes the Yamabe functional (and thus has constant scalar curvature).

We note that for the football $M=S^{4} / \mathbb{Z}_{n}$ (as defined in the introduction) with the round metric $g_{S}$, we have
$$Y_{o r b}\left(M,\left[g_{S}\right]\right)=Y\left(S^{4},\left[g_{S}\right]\right)|n|^{-\frac{1}{2}}=\frac{8 \pi \sqrt{6}}{\sqrt{n}} .$$

Given an orbifold with non-negative scalar curvature, one can use the Green's function for the conformal Laplacian to naturally associate with any point a scalar-flat ALE orbifold by
$$\left(M \backslash\{p\}, g_{p}=\Gamma_{p}^{\frac{4}{n-2}} g\right) .$$
An ALE coordinate system arises from using inverted normal coordinates in the metric $g$ in a neighborhood of the point $p$. If we choose $p$ to be $p_{k}$, one of the orbifold points, then the end of this ALE space will correspond exactly to the group $G_{k}$.

The positive mass theorem does not hold in general for ALE spaces as illustrated by LeBrun's negative mass examples discussed in Section 2.3. Nakajima has proved a version of the positive mass theorem for spin ALE spaces with group $G \subset \operatorname{SU}(2)$ [36], in which the zero mass spaces are exactly the hyperkähler ALE spaces classified by Kronheimer [29]. This makes the orbifold Yamabe problem more subtle than in the smooth case. Indeed, Schoen's test function from [41] will not prove strict inequality in (4.2) if the mass is non-positive.

By an orbifold compactification of an ALE space $(X, g)$, we mean choosing a conformal factor $u: X \rightarrow \mathbb{R}_{+}$such that $u=O\left(r^{-2}\right)$ as $r \rightarrow \infty$. The
space $\left(X, u^{2} g\right)$ then compactifies to a $C^{1, \alpha}$ orbifold. The next result states that the ALE spaces we will consider have smooth orbifold compactifications with strictly positive orbifold Yamabe invariant.

Proposition 4.2. - Let $(X, g)$ be either (i) a LeBrun hyperbolic monopole orbifold AF metric, or (ii) a Gibbons-Hawking orbifold ALE metric. Then there exists a $C^{\infty}$-orbifold conformal compactification $(\hat{X}, \hat{g})$ which satisfies $Y_{\text {orb }}([\hat{g}])>0$.

Proof. - The existence of a smooth orbifold compactification follows directly from [15, Proposition 12], the proof of which is based on twistor theory. A second proof, not using twistor theory, is obtained by locally solving the negative Yamabe problem near the orbifold point (which is a convex variational problem; this is solvable in the orbifold setting), and applying the removable singularity theorem for constant scalar curvature self-dual metrics [46, Theorem 6.4].

Next, one may find a conformal metric on the orbifold compactification whose scalar curvature does not change sign [5, Lemma 3.4]. The strict positivity of the scalar curvature then follows using the strong maximum principle, as in [15, Proposition 13]. Thus we must have $Y_{\text {orb }}([\hat{g}])>0$. We remark that it is not difficult to write down an explicit conformal factor on the compactification which has positive scalar curvature, but we leave this as an exercise for the interested reader. \(\square\)

We next have an estimate for the Yamabe invariant of LeBrun orbifold metrics.

Theorem 4.3. - Let $\left(\hat{M}, \hat{g}_{\mathrm{LB}}\left(m_{1} \cdot p_{1}, \ldots, m_{n} \cdot p_{n}\right)\right)$ be a conformally compactified LeBrun metric with total multiplicity $N=m_{1}+\cdots+m_{n}$. Without loss of generality, assume that $p_{1}=(0,0,1)$, and assume that all monopole points are contained in $B\left(p_{1}, r\right)$. Then
$$Y_{o r b}\left(\left[\hat{g}_{\mathrm{LB}}\right]\right) \leqslant \frac{12 \pi \sqrt{6}}{\sqrt{N+2}}+O(r),$$
as $r \rightarrow 0$.
Proof. - As in the proof of Theorem 3.2, we let $f=-\rho$, to obtain
$$\mathcal{Y}(g)=24 \sqrt{2 \pi} \int_{\mathcal{H}^{3}} V_{1} e^{-4 \rho} d V_{\mathcal{H}^{3}} \cdot\left(\int_{\mathcal{H}^{3}} V_{n} e^{-4 \rho} d V_{\mathcal{H}^{3}}\right)^{-1 / 2} .$$
Using (3.19), we obtain
$$\mathcal{Y}(g)=6 \sqrt{2} \pi^{3 / 2} \cdot\left(\int_{\mathcal{H}^{3}} V_{n} e^{-4 \rho} d V_{\mathcal{H}^{3}}\right)^{-1 / 2} .$$

Clearly,
$$V_{N}=1+\frac{N}{e^{2 \rho}-1}+O(r),$$
as $r \rightarrow 0$. Using radial coordinates, we calculate
$$\begin{aligned}
\int_{\mathcal{H}^{3}}\left(1+\frac{N}{e^{2 \rho}-1}\right) & e^{-4 \rho} d V_{\mathcal{H}^{3}} \\
& =4 \pi \int_{0}^{\infty}\left(1+\frac{N}{e^{2 \rho}-1}\right) e^{-4 \rho}(\sinh \rho)^{2} d \rho \\
& =\left.\frac{\pi}{12}\left(-6 e^{-2 t}-3(N-2) e^{-4 t}+2(N-1)\right)\right|_{0} ^{\infty} \\
& =\frac{(N+2) \pi}{12},
\end{aligned}$$
This yields
$$\mathcal{Y}(g)=6 \sqrt{2} \pi^{3 / 2}\left(\frac{N+2}{48}\right)^{-1 / 2}+O(r)=\frac{12 \pi \sqrt{6}}{\sqrt{N+2}}+O(r),$$
as $r \rightarrow 0$. \(\square\)

Corollary 4.4. - Let $\left(\hat{M}, \hat{g}_{L B}\right)$ be as in Theorem 4.3, and assume that the highest multiplicity at any point is strictly less than $4(N+2) / 9$. Then there exists a radius $r>0$ such that if all points $p_{1}, \ldots, p_{n} \in B\left(p_{1}, r\right)$, then there exists a solution of the orbifold Yamabe problem on $\left(\hat{M},\left[\hat{g}_{L B}\right]\right)$.

Proof. - Let $m$ be the greatest integer strictly less than $4(N+2) / 9$, and let $G$ be the cyclic group of order $m$, acting on $S^{4} \subset \mathbb{R}^{5}=\mathbb{R}^{4} \times \mathbb{R}^{1}$ as in (2.2). We have
$$\frac{12 \pi \sqrt{6}}{\sqrt{N+2}}=\frac{8 \pi \sqrt{6}}{\sqrt{4(N+2) / 9}}<\frac{8 \pi \sqrt{6}}{\sqrt{m}}=Y_{o r b}\left(S^{4} / G,\left[g_{S}\right]\right) .$$
Therefore, for $r$ sufficiently small, by Theorem 4.3,
$$Y_{o r b}\left(\hat{M},\left[\hat{g}_{L B}\right]\right) \lesssim \frac{12 \pi \sqrt{6}}{\sqrt{N+2}}<Y_{o r b}\left(S^{4} / G,\left[g_{S}\right]\right) .$$
If the highest multiplicity of any orbifold point is $m$, we see that estimate (4.2) will be satisfied for $r$ sufficiently small, and Theorem 4.1 then yields a solution of the orbifold Yamabe problem. \(\square\)

Remark 4.5. - For $N=3$, the highest multiplicity allowed is $[20 / 9]=2$. This allows multiplicity 2 points (but not a single multiplicity 3 point). This proves the existence statement in Theorem 1.5. The convergence statements in Theorem 1.5 will be proved later in Section 7.

\subsection*{4.1. Proof of Theorem 1.3}

First, adding a point $p$ at infinity, there exists a smooth orbifold conformal compactification $(\hat{X}, \hat{g})$ of $\left(X_{n}, g\right)$ by Proposition 4.2. Assume by contradiction that $\hat{g}$ is a constant scalar curvature metric on the compactification $\hat{X}$ in this conformal class. Letting $E$ denote the traceless Ricci tensor, we recall the transformation formula: if $g=\phi^{-2} \hat{g}$, then
$$E_{g}=E_{\hat{g}}+(m-2) \phi^{-1}\left(\nabla^{2} \phi-(\Delta \phi / m) \hat{g}\right),$$
where $m$ is the dimension, and the covariant derivatives are taken with respect to $\hat{g}$. Since $g$ is Ricci-flat and $m=4$, we have
$$E_{\hat{g}}=\phi^{-1}\left(-2 \nabla^{2} \phi+(\Delta \phi / 2) g\right) .$$
We next use the argument of Obata [38]; integrating on $\hat{X}$,
$$\begin{aligned}
\int_{\hat{X}} \phi\left|E_{\hat{g}}\right|^{2} d \hat{V} & =\int_{\hat{X}} \phi E_{\hat{g}}^{i j}\left\{\phi^{-1}\left(-2 \nabla^{2} \phi+(\Delta \phi / 2) g\right)_{i j}\right\} d \hat{V} \\
& =-2 \int_{\hat{X}} E_{\hat{g}}^{i j} \nabla^{2} \phi_{i j} d \hat{V} \\
& =-2 \lim _{\epsilon \rightarrow 0} \int_{\hat{X} \backslash B(p, \epsilon)} E_{\hat{g}}^{i j} \nabla^{2} \phi_{i j} d \hat{V} .
\end{aligned}$$
Since $g$ is the Green's function metric associated to $\hat{g}$ at $p$, we have
$$g=\phi^{-2} \hat{g}=G^{\frac{4}{m-2}} \tilde{g} \sim r^{-4} \tilde{g},$$
which implies that $\phi \sim r^{2}$ where $r$ is the distance to $p$ with respect to the metric $\hat{g}$. Continuing the above calculation, integration by parts yields
$$\begin{aligned}
& \int_{\hat{X}} \phi\left|E_{\hat{g}}\right|^{2} d \hat{V}= \\
& -2 \lim _{\epsilon \rightarrow 0}\left(\int_{\partial B(p, \epsilon)} E_{\hat{g}}^{i j}(\nabla \phi)_{i} \nu_{j} d \sigma-\int_{\hat{X} \backslash B(p, \epsilon)}\left(\nabla_{j} E_{\hat{g}}^{i j} \cdot \nabla_{i} \phi\right) d \hat{V}\right) .
\end{aligned}$$
The second term on the right hand side is zero since the scalar curvature of $\hat{g}$ is constant (by the Bianchi identity), and the first term on the right hand side limits to zero since the integrand is bounded. Indeed, since $\hat{g}$ is a smooth orbifold, the curvature is bounded near $p$, and $|\nabla \phi| \sim r$ near $p$. Consequently, $E_{\hat{g}} \equiv 0$, and $\hat{g}$ is Einstein.

Since we have two Einstein metrics in the conformal class, the complete manifold $(X, g)$ admits a nonconstant solution of the equation
$$\nabla^{2} \phi=\frac{\Delta \phi}{m} g .$$

Such a solution is called a concircular scalar field, and complete manifolds which admit a non-zero solution were classified by Tashiro [43] (see also [30]), who showed that $(X, g)$ must be conformal to one of the following: (A) a direct product $V \times J$, where $V$ is an $(m-1)$-dimensional complete Riemannian manifold and $J$ is an interval, (B) hyperbolic space $\mathcal{H}^{m}$, or (C) the round sphere $S^{m}$.

The hyperkähler ALE spaces under consideration have second homology generated by embedded 2-spheres with self-intersection -2, with intersection matrix given by the corresponding Dynkin diagram [29]. If such a space were diffeomorphic to a product $V^{3} \times J$, then any of the above spherical generators in $H_{2}$ would be homologous to a cycle in $V^{3}$, and would therefore have zero self intersection since such a cycle can be deformed to a disjoint cycle by translating it in the $J$ direction. Cases (B) and (C) obviously cannot happen since $\left(X_{n}, g\right)$ is not locally conformally flat for $n>1$. This is a contradiction, and the nonexistence is proved. Finally, the non-existence of a solution, together with Theorem 4.1, imply that the orbifold Yamabe invariant is maximal
$$Y_{o r b}\left(\hat{X}_{n},[\hat{g}]\right)=\frac{8 \pi \sqrt{6}}{\sqrt{n}} .$$
This completes the proof of Theorem 1.3.
Remark 4.6. - We point out that the Obata portion of the above proof does not hold if instead the compact manifold is assumed to be Einstein. For example, consider $\mathbb{C P}^{2}$ with the Fubini-Study metric $g_{F S}$, which is Einstein. The associated Green's function ALE space at any point is the Burns metric, which is scalar-flat but not Ricci-flat.

Remark 4.7. - It is clear from the above proof that Theorem 1.3 also holds for Ricci-flat ALE spaces in other dimensions, as long as they are not homeomorphic to a product $V^{m-1} \times J$, and not locally conformally flat.

We conclude this section by noting that the proof of Theorem 1.3 is also valid in case $X$ has non-trivial orbifold points.

Theorem 4.8. - Theorem 1.3 holds if $\left(X_{n}, g\right)$ is a Gibbons-Hawking multi-Eguchi-Hanson orbifold.

Proof. - As shown in Proposition 4.2, there exists a smooth conformal compactification $(\hat{X}, g)$. The proof of Theorem 1.3 above shows that any constant scalar curvature metric on $\hat{X}$ conformal to $\hat{g}$ must be Einstein. Consequently, there exists a concircular scalar field on $(X, g)$. An examination of Tashiro's proof shows that there are no orbifolds with isolated
singularities in case (A), since the product with an interval would create at least a 1-dimensional singular set. Cases (B) and (C) cannot occur either since these are locally conformally flat. \(\square\)

\section*{5. Symmetric metrics}

We begin with some elementary hyperbolic geometry. Fix the point $p_{0}=$ $(0,0,1) \in \mathcal{H}^{3}$, and let $\rho_{0}(\cdot)=d\left(p_{0}, \cdot\right)$ denote the hyperbolic distance to $p_{0}$. Let $u: \mathcal{H}^{3} \rightarrow \mathbb{R}_{+}$be defined by
$$u=\frac{\operatorname{sech}\left(\rho_{0}\right)}{z}=\frac{2}{1+x^{2}+y^{2}+z^{2}} .$$
To see the second equality in (5.1), recall the following formula
$$\cosh \left(d_{\mathcal{H}}\left(p_{1}, p_{2}\right)\right)=1+\frac{\left|p_{1}-p_{2}\right|^{2}}{2 z_{1} z_{2}},$$
where $p_{i}=\left(x_{i}, y_{i}, z_{i}\right)$, and the norm on the right is the Euclidean norm ([40, Theorem 4.6.1]). From this, we obtain
$$\cosh \left(\rho_{0}(p)\right)=1+\frac{x^{2}+y^{2}+(z-1)^{2}}{2 z}=\frac{x^{2}+y^{2}+z^{2}+1}{2 z} .$$

Lemma 5.1. - The function $u$ satisfies the equation
$$\Delta_{E u c} u+z^{-1} \partial_{z} u=-2 u^{3} .$$

Proof. - We define $\tilde{g}=u^{2}\left(d x^{2}+d y^{2}+d z^{2}+z^{2} d \theta^{2}\right)$. Letting $\hat{x}=$ $z \cos \theta, \hat{y}=z \sin \theta$, we obtain
$$\tilde{g}=\frac{4}{\left(1+x^{2}+y^{2}+\hat{x}^{2}+\hat{y}^{2}\right)^{2}}\left(d x^{2}+d y^{2}+d \hat{x}^{2}+d \hat{y}^{2}\right) .$$
The right hand side is the spherical metric on $S^{4}$ in coordinates arising from stereographic projection. Consequently, from (3.1),
$$\Delta u=-2 u^{3} .$$
Writing out the Laplacian in the $(x, y, z, \theta)$-coordinates, we obtain
$$-2 u^{3}=\Delta u=\frac{1}{z} \sum_{i} \partial_{i}\left(z \partial_{i} u\right)=\Delta_{E u c} u+z^{-1} \partial_{z} u .$$ \(\square\)

\subsection*{5.1. Symmetries for $\mathbf{n}=\mathbf{2}$}

In this subsection, we will only consider the LeBrun construction with two monopole points, $p_{1}$ and $p_{2}$. Without loss of generality, by applying a hyperbolic isometry, we may assume the points $p_{1}=\left(0,0, r_{0}\right)$, and $p_{2}=$ $\left(0,0, r_{0}^{-1}\right)$. It was shown in [25] that the automorphism group is
$$G \equiv(\mathrm{U}(1) \times \mathrm{U}(1)) \ltimes D_{4},$$
where $D_{4}$ is the dihedral group of order 8. There is the index 2 subgroup given by
$$K=(\mathrm{U}(1) \times \mathrm{U}(1)) \ltimes\left(\mathbb{Z}_{2} \oplus \mathbb{Z}_{2}\right),$$
which are exactly the lifts of hyperbolic isometries preserving the set of 2 monopole points.

For a metric to be $K$-invariant, it must in particular be invariant under the bundle U(1)-action. So we consider only metrics of the form $v^{2} g_{L B}$, where $v: H^{3} \rightarrow \mathbb{R}_{+}$. We refer the reader to [25, Section 2] for the details on lifting isometries of $\mathcal{H}^{3}$ to automorphisms of LeBrun metrics.

Proposition 5.2. - If the conformal automorphism $\Phi$ of $g_{L B}$ is the lift of an isometry of hyperbolic space $\phi$, then it is an isometry of the metric $v^{2} g_{L B}$ provided that
$$(z \circ \phi)^{2} \cdot(v \circ \phi)^{2}=z^{2} \cdot v^{2} .$$

Proof. - Using (2.8),
$$\Phi^{*}\left(v^{2} g_{L B}\right)=(v \circ \phi)^{2} \Phi^{*} g_{L B}=(v \circ \phi)^{2}\left(\frac{z \circ \phi}{z}\right)^{2} g_{L B}=v^{2} g_{L B} .$$ \(\square\)

Next, define the metric
$$\tilde{g}_{L B}=u^{2} \cdot g_{L B},$$
where $u$ is defined in (5.1). Let $\phi$ denote inversion in the unit sphere
$$\phi(x, y, z)=\frac{1}{x^{2}+y^{2}+z^{2}}(x, y, z) .$$

Proposition 5.3. - The map $\Phi$ acts as an isometry of $\tilde{g}_{L B}$.
Proof. - We check
$$\begin{aligned}
& (z \circ \phi)^{2}(u \circ \phi)^{2}= \\
& \quad \frac{z^{2}}{\left(x^{2}+y^{2}+z^{2}\right)^{2}} \cdot \frac{4}{\left(1+\frac{1}{x^{2}+y^{2}+z^{2}}\right)^{2}}=\frac{4 z^{2}}{\left(1+x^{2}+y^{2}+z^{2}\right)^{2}}=z^{2} u^{2}
\end{aligned}$$
so the result follows from Proposition 5.2. \(\square\)

Theorem 5.4. - For the LeBrun metric with 2 monopole points $p_{1}=$ $\left(0,0, r_{0}\right), p_{2}=\left(0,0, r_{0}^{-1}\right)$, with $r_{0}>1$, the $K$-symmetric Yamabe invariant satisfies
$$Y_{K}(\hat{M},[g])<8 \sqrt{6} \pi-\beta\left(r_{0}\right),$$
where $\beta:(1, \infty) \rightarrow(0, \infty)$ satisfies $\beta\left(r_{0}\right) \rightarrow 0$ as $r_{0} \rightarrow \infty$.
Proof. - The identity component U(1) × U(1) is generated by (the lifts of) rotations around the $z$-axis and the U(1) fiber rotation [25, Proposition 2.14]. By Proposition 5.2, these are isometries of the metric $\tilde{g}_{L B}$ defined in (5.12). The group $K$ is generated by the identity component, by the lift $\Phi$ of the inversion $\phi$, together with a lift of any reflection in the $(x, y)$-plane. The lift $\Phi$ acts as an isometry by Proposition 5.3. The lift of a reflection in the $(x, y)$-plane is also an isometry by Proposition 5.2. Consequently, $\tilde{g}_{L B}$ is a $K$-invariant metric. We next compute its Yamabe energy.

Take a coordinate system ( $x, y, z, \theta$ ) where $\theta$ is an angular coordinate system on the fiber for some trivialization. The volume element of $g_{L B}$ is
$$\sqrt{\operatorname{det}(g)}=\left(V^{3} z^{2} V^{-1}\right)^{1 / 2}=V z .$$
Since $u$ depends only upon the $(x, y, z)$ coordinates, using Lemma 5.1, we have for the Laplacian with respect to $g_{L B}$,
$$\Delta_{L B} u=\frac{1}{V z} \partial_{i}\left(V^{-1} u_{i} V z\right)=V^{-1}\left(\Delta_{E u c} u+z^{-1} u_{z}\right)=V^{-1}\left(-2 u^{3}\right) .$$
Since $g_{L B}$ is scalar-flat, from (3.1) we have
$$\tilde{R}=-6 u^{-3} \Delta u=12 V^{-1} .$$
The Yamabe energy in coordinates is then given by
$$\mathcal{Y}\left(\tilde{g}_{L B}\right)=\int_{U} z u^{4} d V_{0} \cdot\left(\int_{U} z V u^{4} d V_{0}\right)^{-1 / 2},$$
where $d V_{0}=d x \wedge d y \wedge d z \wedge d \theta$ is the coordinate volume element, and the region of integration is $U=\mathcal{H}^{3} \times(0,2 \pi)$. Since $n \geqslant 1$, we must have $V>1$, and we obtain the estimate
$$\mathcal{Y}\left(\tilde{g}_{L B}\right)<\left(\int z u^{4} d V_{0}\right)^{+1 / 2}=8 \sqrt{6} \pi=Y\left(S^{4},\left[g_{S}\right]\right) .$$
The middle equality follows since for $n=0, \tilde{g}$ is the spherical metric, as seen in the proof of Lemma 5.1. The existence of the function $\beta$ follows easily. \(\square\)

\subsection*{5.2. Proof of Theorem 1.4}

Recall the definition of LeBrun's negative mass metrics on $\mathcal{O}(-n)$ from Section 2.3 above. Since $g_{O L B}$ is scalar-flat, the Yamabe equation for a metric $\hat{g}=f^{2} g, f>0$, is
$$-6 \Delta f=\lambda \cdot f^{3},$$
where $\lambda>0$ is a constant (recall that from Proposition 4.2, there is a smooth conformal compactification $(\hat{X}, \hat{g})$ with strictly positive Yamabe invariant). We are interested in solutions which yield a smooth constant scalar curvature metric on the compactification. In particular, we must have
$$f=O\left(r^{-2}\right),|\nabla f|=O\left(r^{-3}\right),\left|\nabla^{2} f\right|=O\left(r^{-4}\right), \text { as } r \rightarrow \infty .$$
We are only interested in solutions for $r \in[1, \infty]$ which decay quadratically at $\infty$. Therefore, we make the change of coordinates $\hat{r}^{2}=r^{2}-1$. In these new coordinates, the metric takes the form
$$\begin{aligned}
& g_{O L B}= \\
& \quad\left(\frac{1+\hat{r}^{2}}{n+\hat{r}^{2}}\right) d \hat{r}^{2}+\left(1+\hat{r}^{2}\right)\left[\sigma_{1}^{2}+\sigma_{2}^{2}\right]+\frac{1}{1+\hat{r}^{2}} \hat{r}^{2}\left(n+\hat{r}^{2}\right)\left(\sigma_{3}^{2} / n^{2}\right)
\end{aligned}$$
To obtain the actual Kähler scalar-flat metric on $\mathcal{O}(-n)$, one needs to attach a $\mathbb{C P}^{1}$ at the origin, and quotient by $\mathbb{Z}_{n}$ (see [31]), but in the following we will just consider the metric to live on $\mathbb{R}_{+} \times S^{3} \simeq \mathbb{R}^{4} \backslash\{0\}$, using $\hat{r}$ as radial coordinate.

As shown in [31], the identity component of the isometry group of $g_{O L B}$ is U(2). Obviously, any conformal factor for which the conformal metric is invariant under the subgroup $\operatorname{SU}(2)$ must be radial. To yield a smooth metric on the compactification, $f$ must then satisfy the initial conditions
$$f(0)=1, f^{\prime}(0)=0 .$$

A computation shows that for radial $f$, the equation (5.20) takes the form
$$\left(\frac{n+(5-2 n) \hat{r}^{2}}{\hat{r}\left(1+\hat{r}^{2}\right)}\right) f_{\hat{r}}+\left(\frac{n+\hat{r}^{2}}{1+\hat{r}^{2}}\right) f_{\hat{r} \hat{r}}=-\lambda f^{3} .$$
If $n \geqslant 3$, then $5-2 n<0$. In this case, for $\hat{r}$ sufficiently large, the equation looks like
$$(\text { negative }) f_{\hat{r}}+(\text { positive }) f_{\hat{r} \hat{r}}=(\text { negative }) f^{3} .$$

Recall that $f \sim \hat{r}^{-2}$ for $\hat{r}$ large. Therefore, $f$ must be strictly decreasing for some $\hat{r}_{0}$ large, thus $f_{\hat{r}}\left(\hat{r}_{0}\right)<0$. Examining the signs in (5.25), we see that $f_{\hat{r} \hat{r}}\left(\hat{r}_{0}\right)<0$. Consequently, the derivative of $f$ is strictly decreasing at $\hat{r}_{0}$. This implies that $f_{\hat{r}}(\hat{r})<0$ for all $\hat{r} \geqslant \hat{r}_{0}$, and therefore $f_{\hat{r} \hat{r}}(\hat{r})<0$ for all $\hat{r} \geqslant \hat{r}_{0}$. This says that $f$ is concave, so $f$ must hit zero at some finite point, which is a contradiction.

Finally, it is shown in [31], that $g_{O L B}$ for $n=2$ is isometric to the Eguchi-Hanson metric, which is hyperkähler. Thus Theorem 1.3 can be applied to this case. This completes the proof of Theorem 1.4.

Remark 5.5. - For $n=1$, it is easy to check that
$$f(\hat{r})=\frac{1}{1+\hat{r}^{2}}$$
is a a solution of (5.24). This is not a surprise, since for $n=1, g_{O L B}$ is the Burns metric, and $\hat{g}=\left(1+\hat{r}^{2}\right)^{-2} g_{O \mathrm{LB}}=r^{-4} g_{O \mathrm{LB}}$ is the Fubini-Study metric [31].

\section*{6. Integral formulas}

For an ALE space $X$ with several ends $E_{i}$, and orbifold singularity points $p_{j}$, we have the signature formula
$$\begin{aligned}
& \text { 6.1) } \quad \tau(X)= \\
& \frac{1}{12 \pi^{2}}\left(\int_{X}\left|W_{g}^{+}\right|^{2} d V_{g}-\int_{X}\left|W_{g}^{-}\right|^{2} d V_{g}\right)-\sum_{i} \eta\left(S^{3} / G_{i}\right)+\sum_{j} \eta\left(S^{3} / G_{j}^{\prime}\right),
\end{aligned}$$
where $G_{i} \subset S O(4)$ is the group corresponding to the $i$ th end, $\eta\left(S^{3} / G_{i}\right)$ is the $\eta$-invariant, and $G_{j}^{\prime}$ are the groups corresponding to the orbifold points $p_{j}$. The Gauss-Bonnet formula in this context is
$$\begin{aligned}
& \chi(X)= \\
& \frac{1}{8 \pi^{2}}\left(\int_{X}\left|W_{g}\right|^{2} d V_{g}+4 \int_{X} \sigma_{2} d V_{g}\right)+\sum_{i} \frac{1}{\left|G_{i}\right|}+\sum_{j}\left(1-\frac{1}{\left|G_{j}^{\prime}\right|}\right),
\end{aligned}$$
where
$$4 \int_{X} \sigma_{2} d V_{g}=-\frac{1}{2} \int_{X}|E|^{2} d V_{g}+\frac{1}{24} \int_{X} R^{2} d V_{g}$$
and $E$ is the traceless Ricci tensor. See [23] for a nice discussion of these formulas. In this section, we will compute these for various examples.

\subsection*{6.1. Self-dual metric on $n \# \mathbb{C P}^{2}$}

In this case, we have $\chi(M)=n+2, \tau(M)=n$. Thus
$$12 \pi^{2} n=\int_{M}\left|W_{g}^{+}\right|^{2} d V_{g}$$
and
$$8 \pi^{2}(n+2)=\int_{M}\left|W_{g}^{+}\right|^{2} d V_{g}+4 \int_{M} \sigma_{2} d V_{g}$$
Combining these gives
$$4 \pi^{2}(4-n)=4 \int_{M} \sigma_{2} d V_{g}$$
This yields an estimate for the Yamabe invariant of positive self-dual metrics on $2 \# \mathbb{C P}^{2}$ and $3 \# \mathbb{C P}^{2}$.

Proposition 6.1. - Let $0 \leqslant n \leqslant 3$. If $g$ is a self-dual metric on $M=$ $n \# \mathbb{C P}^{2}$ with positive scalar curvature, then
$$Y(M,[g]) \geqslant 4 \pi \sqrt{6} \sqrt{(4-n)} .$$
Thus for $n=2, Y(M,[g]) \geqslant 8 \pi \sqrt{3}$, and for $n=3, Y(M,[g]) \geqslant 4 \pi \sqrt{6}$.
Proof. - Using the inequality $\sigma_{2} \leqslant R^{2} / 24$, we obtain
$$4 \pi^{2}(4-n) \leqslant \frac{1}{24} \int_{M} R^{2},$$
Since the self-duality condition is conformally invariant, we may conformally change to a Yamabe minimizer and obtain
$$4 \pi \sqrt{6} \sqrt{4-n} \leqslant Y(M,[g]) .$$ \(\square\)

Restricting to the class of monopole metrics, we have the following. For $n=0, \hat{g}_{\mathrm{LB}}$ is conformal to the round metric on $S^{4}$, so we have $Y(\hat{M},[\hat{g}])=$ $8 \pi \sqrt{6}$. For $n=1, \hat{g}_{\mathrm{LB}}$ is conformal to the Fubini-Study metric, so we have we have $Y(\hat{M},[\hat{g}])=12 \pi \sqrt{2}$. For $n=2$, we have the lower estimate on the Yamabe invariant stated in Theorem 1.1.

We also make the following observation
Proposition 6.2. - If $g$ is a self-dual metric on $2 \# \mathbb{C P}^{2}$ or $3 \# \mathbb{C P}^{2}$ with positive scalar curvature, then $g$ is conformal to a metric with positive Ricci curvature.

Proof. - From (6.6), we see that the conformal invariant $\int_{M} \sigma_{2}$ is positive when $n \leqslant 3$. It follows from [13] that there exists a conformal metric with $R>0$ and $\sigma_{2}>0$ pointwise (see also [20]). Such a metric necessarily has positive Ricci curvature. \(\square\)

This was proved in [33] for $n=2$, and for $n=3$ under certain conditions on the 3 monopole points. This was done by an explicit construction, as the result of Chang-Gursky-Yang was not known at the time. An interesting fact is that positive Ricci metrics exist for any positive scalar curvature self-dual metric on $3 \# \mathbb{C P}^{2}$, not only those obtained by the LeBrun hyperbolic ansatz.

\subsection*{6.2. Single monopole point with multiplicity}

We take a LeBrun metric with a single monopole point of multiplicity $n$, and compactify to a self-dual orbifold $\hat{M}$ with a single orbifold point of type $A_{n-1}$. It was shown in [32] that this is the same as the conformal compactification of LeBrun's ALE metrics on $\mathcal{O}(-n)$ found in [31]. The characteristic numbers are $\chi(\hat{M})=3, \tau(\hat{M})=1$, and (see [36])
$$\eta\left(S^{3} / G\right)=\frac{(n-1)(n-2)}{3 n} .$$
We thus have
$$1=\frac{1}{12 \pi^{2}} \int_{\hat{M}}\left|W_{g}^{+}\right|^{2} d V_{g}-\frac{(n-1)(n-2)}{3 n},$$
(the minus sign is due to reversed orientation), so
$$\int_{\hat{M}}\left|W_{g}^{+}\right|^{2} d V_{g}=\frac{n^{2}+2}{3 n} 12 \pi^{2} .$$
The Gauss-Bonnet formula yields
$$3=\frac{n^{2}+2}{2 n}+\frac{1}{8 \pi^{2}} 4 \int_{\hat{M}} \sigma_{2} d V_{g}+1-\frac{1}{n},$$
which simplifies to
$$4 \pi^{2}(4-n)=4 \int_{\hat{M}} \sigma_{2} d V_{g}$$

\subsection*{6.3. Gibbons-Hawking multi-Eguchi-Hanson}

For this example with $n$ points, we have $\tau(G H)=n-1, \chi(G H)=n$. Let $\hat{M}$ be the conformal compactification to a compact orbifold with a single $\mathbb{Z}_{n}$ singularity of type $A_{n-1}$. Reversing orientation, the metric is selfdual. We thus have $\tau(\hat{M})=n-1, \chi(\hat{M})=n+1$. The signature formula is
$$n-1=\frac{1}{12 \pi^{2}} \int_{\hat{M}}\left|W_{g}^{+}\right|^{2} d V_{g}+\frac{(n-1)(n-2)}{3 n},$$
which yields
$$\int_{\hat{M}}\left|W_{g}^{+}\right|^{2} d V_{g}=\frac{(n+1)(n-1)}{n} 8 \pi^{2} .$$

Remark 6.3. - Note that
$$\frac{(n+1)(n-1)}{n} 8 \pi^{2}+\frac{n^{2}+2}{3 n} 12 \pi^{2}=12 n \pi^{2},$$
which reflects the fact that the Lebrun metrics will degenerate to a generalized connect sum of a LeBrun orbifold and a compactified multi-Eguchi-Hanson space as the $n$ monopole points tend to a single point, as observed in [32]. This will be made more precise in Section 7.

Returning to the example, the Gauss-Bonnet formula yields
$$n+1=\frac{(n+1)(n-1)}{n}+\frac{1}{8 \pi^{2}} 4 \int_{\hat{M}} \sigma_{2} d V_{g}+1-\frac{1}{n},$$
which simplifies to
$$\frac{2}{n} 8 \pi^{2}=4 \int_{\hat{M}} \sigma_{2} d V_{g} .$$
This implies the inequality
$$\frac{2}{n} 8 \pi^{2} \leqslant \frac{1}{24} \int_{\hat{M}} R^{2} d V_{g}$$
If there existed a Yamabe minimizing metric $\hat{g}$ in the conformal class, then
$$\frac{8 \pi \sqrt{6}}{\sqrt{n}} \leqslant Y_{o r b}(\hat{M},[\hat{g}]) .$$
But the Akutagawa-Botvinnik inequality in Theorem 4.1 says the reverse, so we must have equality. Tracing through the inequalites, this says that $|E|=0$. This gives an alternative proof that any Yamabe minimizer would have to be Einstein (and therefore cannot exist, recall the proof of Theorem 1.3 above).

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/50d7fd11-ad3f-44a7-acda-195a5ccbacd5-29.jpg?height=415&width=965&top_left_y=268&top_left_x=293}
\captionsetup{labelformat=empty}
\caption{Figure 7.1. A bubble tree with several levels of scaling. The dotted circles enclose the regions of singularity formation, and are close to orbifold singularities (in the Cheeger-Gromov sense). The curved arrows represent these regions viewed through a powerful microscope.}
\end{figure}

\section*{7. Orbifold convergence}

We briefly describe the structure of "bubble-trees". Let $\left(M_{i}, h_{i}\right)$ be a sequence of metrics converging to an orbifold $\left(M_{\infty}, h_{\infty}\right)$ in the Cheeger-Gromov sense. At the first level of bubbling (the lowest level of rescaling), the ALE orbifolds $\left(X_{j}, g_{j}\right), j=1 \ldots k$, bubble off, with each orbifold $X_{j}$ corresponding to singular points of convergence $p_{j} \in M_{\infty}, j=1 \ldots k$, of the original sequence $\left(M_{i}, h_{i}\right) \rightarrow\left(M_{\infty}, h_{\infty}\right)$. Each $\left(X_{j}, g_{j}\right), j=1 \ldots k$, is a pointed rescaled Cheeger-Gromov limit of the original sequence, having singular points of convergence $p_{j, j^{\prime}} \in X_{j}, j^{\prime}=1 \ldots k_{j}$. At each singular point $p_{j, j^{\prime}}$, there is a further rescaling which converges to an ALE orbifold $\left(X_{j, j^{\prime}}, g_{j, j^{\prime}}\right)$, as above with singular points of convergence $p_{j, j^{\prime}, j^{\prime \prime}} \in X_{j, j^{\prime}}$, $j^{\prime \prime}=1 \ldots k_{j, j^{\prime}}$. This procedure is then repeated and terminates in finitely many steps, see Figure 7.1. We refer the reader to [46] for more details about this procedure and further references.

\subsection*{7.1. Bubble-tree structure for hyperbolic monopole metrics}

The following theorem describes the bubble formation for compactified LeBrun metrics.

Theorem 7.1. - Let $\left(M, g_{i}\right)$ be a sequence of $n$-pointed LeBrun metrics with monopole points $\left\{p_{i, 1}, \ldots, p_{i, n}\right\}$. Assume that as $i \rightarrow \infty$ that these points converge to
$$\left\{p_{i, 1}, \ldots, p_{i, n}\right\} \rightarrow\left\{m_{1} \cdot p_{\infty, 1}, \ldots, m_{k} \cdot p_{\infty, k}\right\},$$
as $i \rightarrow \infty$ with $p_{\infty, j} \in \mathcal{H}^{3}$ for $1 \leqslant j \leqslant k_{1}$ and $p_{\infty, j} \in \partial \mathcal{H}^{3}$ for $k_{1}<j \leqslant k$, allowing for multiplicity. Then there exist metrics $\hat{g}_{j}$ on the conformal compactification so that $\left(\hat{M}, \hat{g}_{j}\right)$ converges to the compactified LeBrun orbifold
$$\left(\hat{M}, \hat{g}_{j}\right) \rightarrow\left(M_{\infty}, \hat{g}_{\mathrm{LB}}\left(m_{1} \cdot p_{\infty, 1}, \ldots, m_{k_{1}} \cdot p_{\infty, k_{1}}\right)\right),$$
as $j \rightarrow \infty$ in the Cheeger-Gromov sense. There are finitely many bubbles, and the bubble-tree structure is as follows. For each subcollection of points limiting to a finite point with multiplicity greater than one, the bubbletree structure is a tree of Gibbons-Hawking multi-Eguchi-Hanson orbifold ALE spaces. For each subcollection of points limiting to a boundary point, then a LeBrun orbifold AF metric is the first bubble at that point, with subsequent bubbles being Gibbons-Hawking orbifolds as in the previous case. The neck regions are modeled on annuli in Euclidean spaces $\mathbb{R}^{4} / \mathbb{Z}_{k}$, with the group action as in (2.2).

Proof. - By a sequence of conformal transformations, we normalize the sequence so that $p_{i, 1}=(0,0,1)$. Choose a conformal factor $u: \mathcal{H}^{3} \rightarrow \mathbb{R}_{+}$so that $\hat{g}_{i}=u^{2} g_{i}$ is a sequence of smooth metrics on the compactification $\hat{M}$ as follows. Viewing $\mathcal{H}^{3}$ as the upper half space, without loss of generality we may assume that the limiting boundary points lie in some compact set of the $(x, y, 0)$-plane. We choose the compactifying conformal factor $u$ to be identically 1 on some open neighborhood $U$ containing this compact set and such that $U$ also contains all monopole points. Furthermore, choose $u$ to be asymptotic to (5.1) on $\partial \mathcal{H}^{3} \backslash U$, so that $\hat{g}_{i}$ is a smooth metric on the compactification. To understand the bubble structure, we can therefore ignore the compactifying conformal factor in the following argument.

We first consider the case of several points limiting to a higher multiplicity point, say $m_{1} \cdot p_{\infty, 1}$ with $m_{1}>1$. If all points limit to $p_{\infty, 1}$ at a uniform rate, then we rescale the metric so that the points are minimally seperated by distance 1. As in [32, page 237], this is equivalent to rescaling the hyperbolic metric to become the flat metric, and the function $V$ limiting to the sum of Euclidean Green's functions (without a constant). Thus the rescaled limit is a Gibbons-Hawking metric. If the points do not limit to $m_{1} \cdot p_{\infty, 1}$ at a uniform rate, then we do the following. Rescale the metric the smallest amount so that the maximum distance between these points is 1 . We will then see several "clusters" of points limiting to distinct points in a unit ball. Thus the limit will be a Gibbons-Hawking ALE orbifold. At each orbifold point $q$ of this limit, we return to the original sequence and rescale so that the maximum distance between the subcollection of points limiting to $q$ in the first rescaling is 1. At this scaling, we will then see
several new subclusters limiting to distinct points in a unit ball, so again we find Gibbons-Hawking orbifolds at a different scale.

Next, for a subcollection of points limiting to a boundary point, by a conformal transformation, we arrange so that this cluster of points is contained in a unit ball around some finite point in $\mathcal{H}^{3}$, say $p=(0,0,1)$. The pointed limit (based at $p$ ) of such rescaled metrics is a LeBrun hyperbolic monopole AF orbifold metric (since in this gauge, all other points will limit to $\partial \mathcal{H}^{3}$ ). This is conformally related to the original, but it is easy to see that in the original scaling, precisely this AF orbifold metric bubbles off. We will illustrate this in a simple case, the general argument is the same. Consider the case of 2 monopole points. Let $p_{j, 1}=(0,0,1), p_{j, 2}=\left(0,0, j^{-1}\right)$. Let $\phi_{j}(x, y, z)=(j x, j y, j z)$, this is a hyperbolic isometry. By [25, Section 2], there is a lift $\Phi_{j}$ of $\phi$ preserving the connection form. We then have
$$\Phi_{j}^{*}\left(g_{L B}\left(p_{j, 1}, p_{j, 2}\right)\right)=j^{2}\left(g_{L B}((0,0, j),(0,0,1))\right) .$$

In other words, we see that a scaling of the original metric is isometric to another LeBrun metric. Consequently, the bubble will be a LeBrun AF metric (in this case a Burns metric). In general, there could be clusters of points tending towards $\partial \mathcal{H}^{3}$, and then clearly all deeper bubbles at such points will be Gibbons-Hawking orbifold metrics, as in the first paragraph.

Since the number of monopole points is bounded by $n$, this procedure must terminate in finitely many steps, and thus there are finitely many non-trivial bubbles. A trivial bubble, or neck region, will arise at any intermediate scaling between a non-trivial ALE space, and the previous orbifold point onto which is it glued. All of the above ALE spaces are Kähler and have an ALE-coordinate system in which the group action is as in (2.2), so the structure of the neck regions is clearly as stated. \(\square\)

Remark 7.2. - To clarify, we explain the above procedure in two cases. Consider the case of 3 points, and normalize so that $p_{j, 1}=(0,0,1)$. Choose $p_{j, 2}$ and $p_{j, 3}$ to be at distance $j^{-2}$ from each other, but such that both of these are at distance $j^{-1}$ from $p_{j, 1}$. In this case, the original limit is a LeBrun metric with a single multiplicity 3 point. To see the first bubble, we rescale the picture so that the distance between $p_{j, 1}$ and $p_{j, 2}$ is 1. Thus the first bubble will be a Gibbons-Hawking orbifold with one point of multiplicity 1, and another point of multiplicity 2. The second, deepest, bubble will rescale so that $p_{j, 2}$ and $p_{j, 3}$ are at distance 1, and this bubble will be a Gibbons-Hawking metric with 2 points of multiplicity 1, which is none other than the classical Eguchi-Hanson metric.

For the next example, consider again the case of 3 points. Assume that $p_{j, 1}=(0,0,1)$, and choose $p_{j, 2}$ and $p_{j, 3}$ to limit to the boundary point (0, 0, 0). The limit of the original sequence will be a LeBrun metric with a single monopole point (which we know is conformal to the Fubini-Study metric). To understand the bubbling, apply a conformal transformation so that $p_{j, 2}$ and $p_{j, 3}$ limit to ( $0,0,1$ ) (and then $p_{j, 1}$ will limit to the boundary of hyperbolic space). The limit will now be a LeBrun AF metric with a single point of multiplicity 2. This AF space will be the first bubble. Upon further rescaling to separate these two points, we find the second deepest bubble to be an Eguchi-Hanson metric.

\subsection*{7.2. Sobolev constants and Yamabe invariants}