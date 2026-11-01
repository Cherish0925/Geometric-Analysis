---
retention_scope: session
part: 1
total_parts: 4
---

[Part 1/4 of: [2012.13316] Higher order obstructions to the desingularization of Einstein metrics]

---
source_file: 2012_13316.pdf
converter: mathpix
format: mmd
---

\title{
HIGHER ORDER OBSTRUCTIONS TO THE DESINGULARIZATION OF EINSTEIN METRICS
}

\author{
Tristan Ozuch \\ Massachusetts Institute of Technology
}

\begin{abstract}
We find new obstructions to the desingularization of compact Einstein orbifolds by smooth Einstein metrics. These new obstructions, specific to the compact situation, raise the question of whether a compact Einstein 4-orbifold which is limit of Einstein metrics bubbling out Eguchi-Hanson metrics has to be Kähler. We then test these obstructions to discuss if it is possible to produce a Ricci-flat but not Kähler metric by the most promising desingularization configuration proposed by Page in 1981. We identify 84 obstructions which, once compared to the 57 degrees of freedom, indicate that almost all flat orbifold metrics on $\mathbb{T}^{4} / \mathbb{Z}_{2}$ should not be limit of Ricci-flat metrics with generic holonomy while bubbling out Eguchi-Hanson metrics. Perhaps surprisingly, in the most symmetric situation, we also identify a 14 -dimensional family of desingularizations satisfying all of our 84 obstructions.
\end{abstract}

Contents
Introduction
2
A new obstruction to the desingularization in the compact case 2
Is $\partial_{o} \mathbf{E}(M)$ a boundary or a filling? 4
Ricci-flat metrics and reduced holonomy 5
Construction of hyperkähler metrics by gluing-perturbation 5
A Ricci-flat but not locally hyperkähler metric? 5
Brendle-Kapouleas configuration 6
Partial answer to Page's question. 6
A configuration satisfying the first obstructions. 7
Acknowledgments 7
1. Main definitions 7
1.1. Einstein orbifolds and ALE spaces 7
1.2. Eguchi-Hanson metrics 9
1.3. Naïve desingularizations 12
2. New obstructions to the desingularization of Einstein orbifolds 14
2.1. Degeneration and obstructions 15
2.2. Approximate Einstein metrics and obstructions 22
2.3. A new obstruction to the desingularization of Einstein orbifolds 25
3. Ricci-flat modulo obstructions desingularizations of $\mathbb{T}^{4} / \mathbb{Z}_{2}$ 27
3.1. The orbifold $\mathbb{T}^{4} / \mathbb{Z}_{2}$ and its deformations 27
3.2. Partial hyperkähler desingularizations and estimates 28
3.3. Total desingularizations modulo obstructions 31
3.4. Obstruction to the total desingularization 41
4. Explicit obstructions to the desingularization of $\mathbb{T}^{4} / \mathbb{Z}_{2}$ 43
4.1. Equivalent obstructions 45
4.2. Some obstructed situations 46
4.3. A family of desingularizations satisfying the obstructions 47
Appendix A. Function spaces 49
A.1. Decoupling norms. 49
A.2. An application of the analysis on weighted spaces. References

\section*{Introduction}

An Einstein metric g satisfies, for some real number $\Lambda$, the equation
$$\operatorname{Ric}(\mathbf{g})=\Lambda \mathbf{g} .$$
In dimension 4, they are considered optimal due to the homogeneity of their Ricci curvature but also as critical points of the Einstein-Hilbert functional with fixed volume, $g \mapsto \int_{M} \mathrm{R}_{g}$ dvol $_{g}$, and more importantly as minimizers of the $L^{2}$-norm of the Riemann curvature tensor, $g \mapsto \int_{M}\left|\operatorname{Rm}_{g}\right|^{2} d v o l_{g}$.

From dimension 4, even under natural assumptions of bounded diameter (compactness) and lower bound on the volume (non-collapsing) Einstein metrics can develop singularities. One major goal for 4-dimensional geometry is therefore to understand the compactification of the moduli space of Einstein metrics on a differentiable manifold $M^{4}$ defined as
$$\mathbf{E}\left(M^{4}\right):=\left\{\left(M^{4}, \mathbf{g}\right) \mid \exists \Lambda \in \mathbb{R}, \operatorname{Ric}(\mathbf{g})=\Lambda \mathbf{g}, \operatorname{Vol}\left(M^{4}, \mathbf{g}\right)=1\right\} / \mathcal{D}\left(M^{4}\right)$$
where $\mathcal{D}\left(M^{4}\right)$ is the group of diffeomorphisms of $M^{4}$ acting on metrics by pull-back and to compactify it with a useful structure. The metric spaces which are limit of Einstein 4-manifolds with uniformly controlled diameter and volume as well as the associated singularity blow-ups have been understood for a long time in the Gromov-Hausdorff sense [And89, BKN89]: they are respectively Einstein orbifolds and Ricci-flat ALE orbifolds. The metric completion of $\left(\mathbf{E}\left(M^{4}\right), d_{G H}\right)$ is
$$\mathbf{E}\left(M^{4}\right) \cup \partial_{o} \mathbf{E}\left(M^{4}\right),$$
where $\partial_{o} \mathbf{E}\left(M^{4}\right)$ is the set of orbifold $d_{G H}$-limits with bounded diameter (i.e. at finite $d_{G H}$-distance) of Einstein metrics on $M^{4}$.

In the present article, we find new types obstructions to the desingularization of Einstein orbifolds which are special to the compact context. They motivate and indicate positive answers the following questions:
\begin{itemize}
\item[-] Assume that $\left(M_{o}^{4}, \mathbf{g}_{o}\right) \in \partial_{o} \mathbf{E}\left(M^{4}\right)$ where $M^{4}$ has the topology of $M_{o}^{4}$ desingularized by Eguchi-Hanson metrics. Is $\mathbf{g}_{o}$ Kähler-Einstein?
\item[-] Under the same assumptions, is $\partial_{o} \mathbf{E}\left(M^{4}\right)$ of codimension 2 in $\mathbf{E}\left(M^{4}\right)$ ?
\item[-] Can we desingularize a flat metric on $\mathbb{T}^{4} / \mathbb{Z}_{2}$ by smooth Ricci-flat metrics with generic holonomy thanks to Eguchi-Hanson metrics?
\end{itemize}

A new obstruction to the desingularization in the compact case. Any smooth Einstein 4-manifold close to a compact Einstein orbifold in a mere Gromov-Hausdorff sense has recently been produced by a gluing-perturbation procedure [Ozu19a, Ozu19b]. In the present paper, for simplicity, we will focus on an Einstein orbifold $\left(M_{o}, \mathbf{g}_{o}\right)$ with integrable Einstein deformations (like all known 4-dimensional examples) and consider only the simplest singularities modeled on $\mathbb{R}^{4} / \mathbb{Z}_{2} \sim \mathbb{C}^{2} / \mathbb{Z}_{2}$, whose minimal resolution has the topology $T^{*} \mathbb{S}^{2}$ of the Eguchi-Hanson metric [EH78].

Remark 0.1. This is conjectured to be the only possible topology for an Einstein desingularization of $\mathbb{R}^{4} / \mathbb{Z}_{2}$, see [BKN89].

Let us denote $M$ the differentiable manifold obtained by minimal resolution (in some orientation) of the $\mathbb{R}^{4} / \mathbb{Z}_{2} \approx \mathbb{C}^{2} / \mathbb{Z}_{2}$ singularities of $M_{o}$. Using [Ozu19a, Ozu19b], we know that if there exists a sequence of Einstein metrics on $M$ converging to $\left(M_{o}, \mathbf{g}_{o}\right)$ in the Gromov-Hausdorff sense, then an obstruction already noticed in [Biq13] is satisfied at every singular point of $M_{o}$. More precisely, denoting respectively $\mathbf{R}_{\mathbf{g}_{o}}^{+}(p)$ and $\mathbf{R}_{\mathbf{g}_{o}}^{-}(p)$ the selfdual and anti-selfdual parts of the curvature at a singular point $p \in M_{o}$ seen as an endomorphism on the space of 2-forms, we have either $\operatorname{det} \mathbf{R}_{\mathbf{g}_{o}}^{+}(p)=0$ or $\operatorname{det} \mathbf{R}_{\mathbf{g}_{o}}^{-}(p)=0$. This means that in some basis, we have either
$$\mathbf{R}_{\mathbf{g}_{o}}^{+}(p)=\left[\begin{array}{ccc}
0 & 0 & 0 \\
0 & * & * \\
0 & * & *
\end{array}\right] \text { or, } \mathbf{R}_{\mathbf{g}_{o}}^{-}(p)=\left[\begin{array}{ccc}
0 & 0 & 0 \\
0 & * & * \\
0 & * & *
\end{array}\right] \text {. }$$

We will first show that an additional obstruction holds under weaker assumptions than those of Biq13. Another physically motivated assumption is that of the stability of the Einstein metric. This condition essentially means that the linearization of the Ricci curvature has nonnegative spectrum, see Definition 1.11.

We are now ready to state the first main result of this paper:
Theorem 0.2. Let $\left(M_{o}^{4}, \mathbf{g}_{o}\right)$ be a compact Einstein orbifold with $\operatorname{Ric}\left(\mathbf{g}_{o}\right)=\Lambda \mathbf{g}_{o}$ for $\Lambda \in \mathbb{R}$, with integrable Einstein deformations and with singularities $\mathbb{R}^{4} / \mathbb{Z}_{2}$. Assume that we have $\left(M_{o}^{4}, \mathbf{g}_{o}\right) \in \overline{\mathbf{E}\left(M^{4}\right)}{ }_{G H}$ for $M=M_{o} \# T^{*} \mathbb{S}^{2} \# \ldots \# T^{*} \mathbb{S}^{2}$, where \# denotes a gluing in the positive or negative orientation and along the cone $\mathbb{R}^{4} / \mathbb{Z}_{2}$. Assume additionally one of the following properties:
\begin{itemize}
\item[(1)] there exists a sequence $\left(\mathbf{g}_{n}\right)_{n}$ of stable Ricci-flat (Definition 1.11) metrics in $\mathbf{E}\left(M^{4}\right)$ converging to $\mathbf{g}_{o}$ in the Gromov-Hausdorff sense, or,
\item[(2)] $M_{o}$ has only one singularity and is rigid (i.e. does not admit infinitesimal Einstein deformations).
\end{itemize}

Then, for any singular point $p$ of $M_{o}$, there exists a basis of the selfdual 2-forms or anti-selfdual 2 -forms in which we have (depending on the orientation of the gluing):
$$\mathbf{R}_{\mathbf{g}_{o}}^{+}(p)=\left[\begin{array}{ccc}
0 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & \Lambda
\end{array}\right] \quad \text { or } \quad \mathbf{R}_{\mathbf{g}_{o}}^{-}(p)=\left[\begin{array}{ccc}
0 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & \Lambda
\end{array}\right] .$$

Notice that a curvature of the form (4) is typical of Kähler-Einstein metrics.
Theorem 0.2 is specific to the compact case and is in sharp contrast with Biquard's desingularization Biq13 in the asymptotically hyperbolic case. Indeed, the degeneration of the asymptotically hyperbolic AdS Taub-Bolt metrics converges to an orbifold which is rigid and has one singularity $\mathbb{R}^{4} / \mathbb{Z}_{2}$ but does not satisfy (4), see Example 2.1.
Remark 0.3. Since the convergence is allowed to be only in the Gromov-Hausdorff sense, the assumptions of Theorem 0.2 are weaker than in [Biq13, Corollary 9.3], where the obstruction (3) at the singular point was first observed. Moreover, the present proof would also yield an obstruction for other Kleinian singularities by [Biq16, Lemme 9] and [Biq16, Lemme 12].

Another goal here is to obtain a new obstruction result under some technical assumption of existence of a sequence of metrics in $\mathbf{E}\left(M^{4}\right)$ sufficiently transverse to the boundary $\partial_{o} \mathbf{E}\left(M^{4}\right)$ of (2). We will say that a sequence of Einstein metrics is a transverse desingularization of the orbifold $\left(M_{o}, \mathbf{g}_{o}\right)$ if the sequence is almost orthogonal to $\partial_{o} \mathbf{E}(M)$, see Definition 1.29 and Figure 2. Almost all Einstein metrics obtained by gluing-perturbation are transverse, see [Top87a, Top87b, LS94, Don12, BK17]. Note that [Biq13, Biq16, Biq17] are notable exceptions. A weaker assumption than being transverse for an Einstein desingularization is being nondegenerate. We will say that a sequence of Einstein metrics is a
nondegenerate Einstein desingularization of $\left(M_{o}, \mathbf{g}_{o}\right) \in \partial_{o} \mathbf{E}(M)$ if the sequence approaches $\left(M_{o}, \mathbf{g}_{o}\right)$ without being "too tangent" to $\partial_{o} \mathbf{E}(M)$, see Definition 1.29 and Figure 1. This notion is in the spirit of the assumption of genericity of [Spo14] and nondegeneracy of [BR15].
Proposition 0.4. Let $\left(M_{o}^{4}, \mathbf{g}_{o}\right)$ be a compact Einstein orbifold with $\operatorname{Ric}\left(\mathbf{g}_{o}\right)=\Lambda \mathbf{g}_{o}$ for $\Lambda \in \mathbb{R}$, with integrable Einstein deformations and with singularities $\mathbb{R}^{4} / \mathbb{Z}_{2}$. Assume that we have $\left(M_{o}^{4}, \mathbf{g}_{o}\right) \in \overline{\mathbf{E}\left(M^{4}\right)}{ }_{G H}$ for $M=M_{o} \# T^{*} \mathbb{S}^{2} \# \ldots \# T^{*} \mathbb{S}^{2}$, where \# denotes a gluing in the positive or negative orientation and along the cone $\mathbb{R}^{4} / \mathbb{Z}_{2}$. Assume additionally one of the following properties:
\begin{itemize}
\item[(1)] there exists a transverse (Definition 1.29) sequence $\left(\mathbf{g}_{n}\right)_{n}$ of metrics in $\mathbf{E}\left(M^{4}\right)$ converging to $\mathbf{g}_{o}$ in the Gromov-Hausdorff sense,
\item[(2)] $\Lambda=0$ and there exists a nondegenerate (Definition 1.29) sequence $\left(\mathbf{g}_{n}\right)_{n}$ of metrics in $\mathbf{E}\left(M^{4}\right)$ converging to $\mathbf{g}_{o}$ in the Gromov-Hausdorff sense,
\item[(3)] $M_{o}$ has only one singularity and there exists a nondegenerate sequence $\left(\mathbf{g}_{n}\right)_{n}$ of metrics in $\mathbf{E}\left(M^{4}\right)$ converging to $\mathbf{g}_{o}$ in the Gromov-Hausdorff sense.
\end{itemize}

Then, for any singular point $p$ of $M_{o}, \mathbf{g}_{o}$ satisfies the obstruction (4).
Remark 0.5. The proof of Proposition 0.4 relies on the fact that our compact deformations add as many degrees of freedom as new obstructions to satisfy. The obstruction (4) is not satisfied by the orbifolds of the desingularizations of [Biq13, Biq16, Biq17] or Example 2.1, which rely on nondegenerate (but not transverse) Einstein deformations coming from the conformal infinity. These deformations from the conformal infinity add an infinite number of degrees of freedom without adding any obstruction.

It is somewhat expected that the completion $\mathbf{E}(M) \cup \partial_{o} \mathbf{E}(M)$ of the moduli space $\mathbf{E}(M)$ is real-analytic or real-subanalytic, see And10. This would imply that the orbifold metrics can be approached by curves of Einstein metrics. An initial intuition for Theorem 0.2 is Biq17 which shows that if $\Lambda \neq 0$ and the obstruction (4) is not satisfied, then the orbifold metrics cannot be approached by curves of Einstein metrics. Our proofs however do not use this fact and even work in the case when $\Lambda=0$. They rely heavily on the computations of the second variations of the Ricci curvature of [Biq16] and the formalism of [Fin11].

Is $\partial_{o} \mathbf{E}(M)$ a boundary or a filling? An interesting problem on which Theorem 0.2 sheds some light is the size of $\partial_{o} \mathbf{E}\left(M^{4}\right)$ the set of singular metrics in the completion (2) of the moduli space of Einstein metrics. Anderson proposes the following "optimistic" (in his own words) conjecture.

Conjecture 0.6 ([And10]). The subspace $\partial_{o} \mathbf{E}\left(M^{4}\right)$ is of codimension 2 in $\overline{\mathbf{E}\left(M^{4}\right)}{ }_{G H}$.
This conjecture means that we should not think of $\partial_{o} \mathbf{E}\left(M^{4}\right)$ as a boundary of $\mathbf{E}\left(M^{4}\right)$ but rather as a filling of missing pieces as it was pictured in [And92] in the case of $M^{4}=K 3$.

Remark 0.7. This is false in the asymptotically hyperbolic context where the desingularizations of Biq13 applied to the AdS Taub-Bolt orbifold (Example 2.1) show that $\partial_{o} \mathbf{E}\left(M^{4}\right)$ is of codimension 1 .

With our present vocabulary, Conjecture 0.6 means that given a compact Einstein orbifold $\left(M_{o}, \mathbf{g}_{o}\right) \in \partial_{o} \mathbf{E}\left(M^{4}\right)$, the space of Einstein desingularizations of $M_{o}$ which are transverse to $\partial_{o} \mathbf{E}\left(M^{4}\right)$ is at least 2-dimensional.

Theorem 0.2 can be seen as a step towards this conjecture in the situation where we desingularize by an Eguchi-Hanson metric. Indeed, its proof shows that:
\begin{itemize}
\item[-] if $\mathbf{R}_{\mathbf{g}_{o}}^{+}\left(p_{o}\right)$ is invertible, then there is no desingularization which is Einstein up to a $o(t)$ error,
\end{itemize}
\begin{itemize}
\item[-] if the kernel of $\mathbf{R}_{\mathbf{g}_{o}}^{+}\left(p_{o}\right)$ is of dimension 1, then there is no transverse desingularization which is Einstein up to a $o\left(t^{2}\right)$ error and there is exactly a one-dimensional set of desingularizations which are Einstein up to a $o(t)$ error,
\item[-] if the kernel of $\mathbf{R}_{\mathbf{g}_{o}}^{+}\left(p_{o}\right)$ is of dimension 2 or 3, then the transverse desingularizations which are Einstein up to a $o\left(t^{2}\right)$ error are of dimension 2 or 3 and in correspondence with the kernel of $\mathbf{R}_{\mathbf{g}_{o}}^{+}\left(p_{o}\right)$.
\end{itemize}

Finally, recall that Einstein metrics with a curvature tensor of the form (4) for $\Lambda=0$ at all points are locally hyperkähler metrics. Since we have only identified the first two obstructions of an infinite list, we might wonder if the remaining obstructions impose this condition at all points. We ask the following question.

Question 0.8. Let $\left(M_{o}^{4}, \mathbf{g}_{o}\right)$ be a Ricci-flat orbifold, and assume that it can be desingularized in the Gromov-Hausdorff sense by Einstein metrics $\left(M^{4}, \mathbf{g}_{n}\right)_{n \in \mathbb{N}^{*}}$ forming trees of Kähler Ricci-flat ALE metrics. Are the orbifold $\left(M_{o}^{4}, \mathbf{g}_{o}\right)$ and the smooth metrics $\left(M^{4}, \mathbf{g}_{n}\right)$ necessarily quotients of hyperkähler metrics?

A positive answer to the above question combined with the folklore conjecture that all Ricci-flat ALE orbifolds are Kähler indicates that it may not be possible to produce Ricciflat metrics which are not Kähler by gluing constructions on Ricci-flat orbifolds. This pessimistic perspective is related to one of the main issue in Riemannian geometry which is to understand the structure of Ricci-flat metrics on compact manifolds.

Ricci-flat metrics and reduced holonomy. For a long time, it was believed that compact Ricci-flat metrics should be flat. The resolution of Calabi's conjecture by Yau [Yau78] provided many counter-examples. These so-called Calabi-Yau metrics are the only currently known examples and they have reduced holonomy (that is different from the generic holonomy $S O(n)$ in dimension $n$ ). A lingering question since then is therefore the following one.

Question 0.9. Do all compact Ricci-flat manifolds have reduced holonomy?
A physically relevant additional property that one can ask from a Ricci-flat metric, is that of being stable, see [Ach19].

Question 0.10 ([Ach19]). Do all compact stable Ricci-flat manifolds have reduced holonomy?

Construction of hyperkähler metrics by gluing-perturbation. Compact non flat Ricci-flat metrics are not explicit at all, but a classical way to approach them and to obtain a more concrete picture is to produce them by gluing various explicit noncompact and singular blocks together into an approximate Ricci-flat metric and perturb it into an actual Ricci-flat metric.

Gibbons-Pope [GP79] and Page [Pag78] proposed a conjectural and physically motivated picture for some hyperkähler, hence Ricci-flat, metrics on some K3 surfaces. The idea was to desingularize the orbifold $\mathbb{T}^{4} / \mathbb{Z}_{2}$ which has 16 singularities of type $\mathbb{R}^{4} / \mathbb{Z}_{2}$ by gluing 16 Eguchi-Hanson metrics in the same orientation and to perturb the result to a hyperkähler metric. This was rigorously obtained for Eguchi-Hanson metrics glued at comparable scales by Topiwala [Top87a] Top87b] and Lebrun-Singer [LS94], see also [Don12]. The proof heavily relies on Kähler geometry arguments.

A Ricci-flat but not locally hyperkähler metric? In 1981, Page Pag81 asks a new question.

Question 0.11. Is it possible to perturb a gluing of Eguchi-Hanson metrics in different orientations to the orbifold $\mathbb{T}^{4} / \mathbb{Z}_{2}$ into a Ricci-flat metric?

Remark 0.12. It is often conjectured, see for instance [BKN89], that the only Ricci-flat metric asymptotic to $\mathbb{R}^{4} / \mathbb{Z}_{2}$ is the Eguchi-Hanson metric. This would therefore describe any possible Einstein desingularization of $\mathbb{T}^{4} / \mathbb{Z}_{2}$.

Having different orientations for the Eguchi-Hanson metrics prevents the use of Kähler geometry techniques. A positive answer to Question 0.11 would provide a Ricci-flat metric with generic holonomy and a negative answer to Question 0.9.

Brendle-Kapouleas configuration. In [BK17], Brendle and Kapouleas studied Question 0.11 in the most symmetric situation: the orbifold metric comes from the regular lattice $\mathbb{Z}^{4}$, the points where the gluing are done in the positive or negative orientation follow a so-called chessboard pattern, and the Eguchi-Hanson metrics in the same orientation are glued with the same $S O(4)$ or $O(4) \backslash S O(4)$ parameter and the same size. In this 1dimensional set of configurations, they exhibit one interaction between the bubbles glued in different orientation. They remarkably use this obstruction to construct an intriguing solution to the Ricci flow which exhibits a new behavior: it is an ancient Ricci-flow desingularizing the orbifold $\mathbb{T}^{4} / \mathbb{Z}_{2}$.

Partial answer to Page's question. In this article, we consider the general situation of the desingularization of a flat metric on $\mathbb{T}^{4} / \mathbb{Z}_{2}$ obtained from a lattice $L\left(\mathbb{Z}^{4}\right)$ for $L \in$ $G L(4, \mathbb{R})$ and desingularized by Eguchi-Hanson metrics glued in various directions, sizes and orientations. For each configuration of positively and negatively oriented Eguchi-Hanson metrics, this yields a 57-dimensional space of candidates to a Ricci-flat gluingperturbation as in [Ozu19b] and therefore of potential positive answers to Question 0.11.

We however identify a great number of interactions between these metrics which induce obstructions interpreted as curvature conditions similar to those of (3) and (4).

Theorem 0.13 (Informal, Corollaries 4.3 and 4.10). We have the following numbers of constraints in this 57-dimensional space of desingularization configurations.
\begin{itemize}
\item[(1)] For general parameters, there are 57 necessary polynomial equations that the gluing parameters of the Eguchi-Hanson metrics should satisfy for an Einstein desingularization to exist. 48 of these equations are analogous to the obstruction (3).
\item[(2)] For general parameters, there are 84 necessary polynomial equations that the gluing parameters should satisfy for a stable Ricci-flat desingularization to exist. 80 of these equations are analogous to the obstruction (4).
\item[(3)] For parameters corresponding to a nondegenerate desingularization, there are 84 necessary polynomial equations that the gluing parameters of the Eguchi-Hanson metrics should satisfy for an Einstein desingularization to exist. 80 of these equations are analogous to the obstruction (4).
\end{itemize}
The coefficients of these (quadratic and quartic) polynomial equations depend on the flat metric on $\mathbb{T}^{4} / \mathbb{Z}_{2}$ only.

This indicates that generic flat metrics on $\mathbb{T}^{4} / \mathbb{Z}_{2}$, should not be Gromov-Hausdorff limit of Einstein metrics bubbling out Eguchi-Hanson metrics in different orientations.

Remark 0.14. In the configuration proposed by Brendle and Kapouleas [BK17], none of the 57 obstructions of the first point is satisfied.

A simpler consequence is that a lot of configurations of positively and negatively oriented Eguchi-Hanson metrics are impossible. We in particular obtain the following obstruction under a topological assumption.

Theorem 0.15 (Theorem 4.11). There does not exist a sequence of Einstein metrics $d_{G H}$-converging to the regular torus (obtained from the lattice $\mathbb{Z}^{4}$ ) by bubbling out exactly
one positively oriented Eguchi-Hanson metric and 15 negatively oriented Eguchi-Hanson metrics.

Remark 0.16. It is likely that this result holds without assuming that the lattice is the usual $\mathbb{Z}^{4}$, see Conjecture 4.14.

Remark 0.17. The desingularization by stable Ricci-flat metrics is much more restrictive. A direct extension of the proof of Theorem 0.15 states that the desingularization is impossible with less than 3 positively oriented Eguchi-Hanson metrics and the rest of negatively oriented, see Corollary 4.15.

A configuration satisfying the first obstructions. Seeing the above obstruction results, one would be tempted to try and prove that it is impossible to obtain a Ricci-flat but not hyperkähler metric by gluing-perturbation of Eguchi-Hanson metrics to a flat $\mathbb{T}^{4} / \mathbb{Z}_{2}$. One would maybe expect that the above 84 obstructions should be enough to show that every configuration is obstructed.

Perhaps surprisingly, we find a set of solutions to our 84 equations. More precisely, there exists an explicit 14-dimensional set of configurations of gluing of Eguchi-Hanson metrics which satisfy the 84 above equations. The orientations of the Eguchi-Hanson metrics follow the chessboard pattern of [BK17], but their directions and sizes are not constrained.

Acknowledgments. The author would like to thank his PhD advisor, Olivier Biquard for his help and interest in the early stages of this project.

\section*{1. Main definitions}

Note 1.1. All along this article, when the name of a metric is in bold, then it is Einstein.
1.1. Einstein orbifolds and ALE spaces. For $\Gamma$ a finite subgroup of $S O(4)$ acting freely on $\mathbb{S}^{3}$, let us denote $\left(\mathbb{R}^{4} / \Gamma, \mathbf{e}\right)$ the flat orbifold obtained by the quotient of the Euclidean metric on $\mathbb{R}^{4}$ by the action of $\Gamma$, and $r_{\mathbf{e}}:=d_{\mathbf{e}}(., 0)$.

Definition 1.2 (Orbifold (with isolated singularities)). We will say that a metric space $\left(M_{o}, g_{o}\right)$ is an orbifold of dimension $n \geqslant 2$ if there exists $\epsilon_{0}>0$ and a finite number of points $\left(p_{k}\right)_{k}$ of $M_{o}$ called singular such that we have the following properties:
\begin{itemize}
\item[(1)] the space $\left(M_{o} \backslash\left\{p_{k}\right\}_{k}, g_{o}\right)$ is a manifold of dimension $n$,
\item[(2)] for each singular point $p_{k}$ of $M_{o}$, there exists a neighborhood of $p_{k}, U_{k} \subset M_{o}$, a finite subgroup acting freely on $\mathbb{S}^{n-1}, \Gamma_{k} \subset S O(n)$, and a diffeomorphism $\Phi_{k}$ : $B_{\mathbf{e}}\left(0, \epsilon_{0}\right) \subset \mathbb{R}^{n} / \Gamma_{k} \rightarrow U_{k} \subset M_{o}$ for which, the pull-back of $\Phi_{k}^{*} g_{o}$ on the covering $\mathbb{R}^{n}$ is smooth. Here, diffeomorphism is understood in the orbifold sense, i.e. it is a diffeomorphism between the cover $\mathbb{R}^{4}$ and the associated cover of $U_{k}$.
\end{itemize}

Remark 1.3. The analysis on an orbifold is exactly the same as the analysis on a manifold up to using finite local coverings at the singular points.

Definition 1.4 (The function $r_{o}$ on an orbifold). We define $r_{o}$, a smooth function on $M_{o}$ satisfying $r_{o}:=\left(\Phi_{k}\right)_{*} r_{\mathbf{e}}$ on each $U_{k}$, and such that on $M_{o} \backslash U_{k}$, we have $\epsilon_{0} \leqslant r_{o}<1$ (the different choices will be equivalent for our applications).

We will denote, for $0<\epsilon \leqslant \epsilon_{0}$,
$$M_{o}(\epsilon):=\left\{r_{o}>\epsilon\right\}=M_{o} \backslash\left(\bigcup_{k} \Phi_{k}\left(\overline{B_{\mathbf{e}}(0, \epsilon)}\right)\right) .$$

Let us now turn to ALE metrics.

Definition 1.5 (ALE orbifold (with isolated singularities)). An ALE orbifold of dimension $n \geqslant 4,\left(N, g_{b}\right)$ is a metric space for which there exists $\epsilon_{0}>0$, singular points $\left(p_{k}\right)_{k}$ and a compact $K \subset N$ for which we have:
\begin{itemize}
\item[(1)] $\left(N, g_{b}\right)$ is an orbifold of dimension $n$,
\item[(2)] there exists a diffeomorphism $\Psi_{\infty}:\left(\mathbb{R}^{n} / \Gamma_{\infty}\right) \backslash \overline{B_{\mathbf{e}}\left(0, \epsilon_{0}^{-1}\right)} \rightarrow N \backslash K$ such that
$$r_{\mathbf{e}}^{l}\left|\nabla^{l}\left(\Psi_{\infty}^{*} g_{b}-\mathbf{e}\right)\right|_{\mathbf{e}} \leqslant C_{l} r_{\mathbf{e}}^{-n} .$$
\end{itemize}

Definition 1.6 (The function $r_{b}$ on an ALE orbifold). We define $r_{b}$ a smooth function on $N$ satisfying $r_{b}:=\left(\Psi_{k}\right)_{*} r_{\mathbf{e}}$ on each $U_{k}$, and $r_{b}:=\left(\Psi_{\infty}\right)_{*} r_{\mathbf{e}}$ on $U_{\infty}$, and such that $\epsilon_{0} \leqslant r_{b} \leqslant \epsilon_{0}^{-1}$ on the rest of $N$ (the different choices are equivalent for our applications).

For $0<\epsilon \leqslant \epsilon_{0}$, we will denote
$$N(\epsilon):=\left\{\epsilon<r_{b}<\epsilon^{-1}\right\}=N \backslash\left(\bigcup_{k} \Psi_{k}\left(\overline{B_{\mathbf{e}}(0, \epsilon)}\right) \cup \Psi_{\infty}\left(\left(\mathbb{R}^{4} / \Gamma_{\infty}\right) \backslash B_{\mathbf{e}}\left(0, \epsilon^{-1}\right)\right)\right) .$$

Now, consider a subset $S_{o}$ of the singular points of $M_{o}$ (respectively $S$ of $N$ ).
Definition 1.7 (Functionals $r_{o, S_{o}}$ and $r_{b, S}$ ). We define the functional $r_{o, S_{o}}$ (respectively $r_{b, S}$ ) exactly like in Definitions 1.4 (respectively 1.6) by only considering the sets $U_{k}$ containing points of $S_{o}$ (respectively $S$ ).

A metric $g$ close to $\mathbf{g}_{o}$ (with some adapted decay at infinity in the noncompact case) is Einstein and is in Bianchi gauge with respect to $\mathbf{g}_{o}$, that is satisfies $B_{\mathbf{g}_{o}} g:=\left(\delta_{\mathbf{g}_{o}}+\right.$ $\left.\frac{1}{2} d \operatorname{tr}_{\mathbf{g}_{o}}\right) g=0$, if and only if it satisfies
$$\mathbf{\Phi}_{\mathbf{g}_{o}}(g):=\operatorname{Ric}(g)-\Lambda g+\delta_{g}^{*} B_{\mathbf{g}_{o}} g=0$$
see for instance [Biq13], Section 6]. The linearization of $\mathbf{\Phi}_{\mathbf{g}_{o}}$ at $\mathbf{g}_{o}$ is
$$P_{\mathbf{g}_{o}}:=\frac{1}{2} \nabla_{\mathbf{g}_{o}}^{*} \nabla_{\mathbf{g}_{o}}-\stackrel{\circ}{\mathrm{R}}_{\mathbf{g}_{o}},$$
where $\stackrel{\circ}{\mathrm{R}}$ is the action of curvature on symmetric 2-tensors: for an orthonormal basis $\left(e_{i}\right)_{i}$,
$$\stackrel{\circ}{\mathrm{R}}(h)(X, Y)=\sum_{i} h\left(\operatorname{Rm}\left(e_{i}, X\right) Y, e_{i}\right) .$$

Definition 1.8 (Infinitesimal Einstein deformations). For a compact or ALE Einstein orbifold ( $M, \mathbf{g}$ ) with $\operatorname{Ric}(\mathbf{g})=\Lambda \mathbf{g}$, we define $\mathbf{O}(\mathbf{g})$ as the kernel of $P_{\mathbf{g}}$ on $L^{2}(\mathbf{g})$.

Definition 1.9 (Einstein modulo obstructions deformations). According to [Ozu19b] (see also [Koi83]), there exists $\epsilon>0$ such that for any $v \in \mathbf{O}(\mathbf{g})$ with $\|v\|_{L^{2}(\mathbf{g})}<\epsilon$, there exists a unique metric $\bar{g}_{v}$ satisfying
\begin{itemize}
\item[(1)] $\boldsymbol{\Phi}_{\mathbf{g}}\left(\bar{g}_{v}\right) \in \mathbf{O}(\mathbf{g})$,
\item[(2)] $\bar{g}_{v}-(\mathbf{g}+v) \perp_{\mathbf{g}} \mathbf{O}(\mathbf{g})$,
\item[(3)] $\left\|\bar{g}_{v}-\mathbf{g}\right\|_{L^{2}(\mathbf{g})} \leqslant 2 \epsilon$.
\end{itemize}

All along this article, in order to simplify the exposition and for lack of nonintegrable examples, we will only consider Einstein metrics with integrable Einstein deformations.

Definition 1.10 (Einstein metric with integrable deformations). An Einstein metric g only has integrable infinitesimal Einstein deformations if for any $v \in \mathbf{O}(\mathbf{g})$, the metric $\bar{g}_{v}=\mathbf{g}_{v}$ actually satisfies
\begin{itemize}
\item[(1)] $\mathbf{\Phi}_{\mathbf{g}}\left(\mathbf{g}_{v}\right)=0$,
\item[(2)] $\mathbf{g}_{v}-(\mathbf{g}+v) \perp_{\mathbf{g}} \mathbf{O}(\mathbf{g})$,
\item[(3)] $\left\|\mathbf{g}_{v}-\mathbf{g}\right\|_{L^{2}(\mathbf{g})} \leqslant 2 \epsilon$.
\end{itemize}

An additional class of metrics we will be interested in is that of stable Ricci-flat metrics.

Definition 1.11 (Stable Ricci-flat metrics). We will say that $\mathbf{g}$ is a stable Ricci-flat metric if it is Ricci-flat and satisfies: for all smooth compactly supported symmetric 2-tensor $h$ :
$$\left\langle P_{\mathbf{g}} h, h\right\rangle_{L^{2}(\mathbf{g})} \geqslant 0 .$$

All of the known examples of compact Ricci-flat metrics are stable.
1.2. Eguchi-Hanson metrics. Let us describe the Eguchi-Hanson metric [EH78]. In this article, the Ricci-flat ALE metrics $\left(N, g_{b}\right)$ we will consider will almost always be homothetic transformations of the Eguchi-Hanson metric.

The Eguchi-Hanson metric, which we will denote eh, is defined on $T^{*} \mathbb{S}^{2}$. It is asymptotic to the flat cone $\mathbb{R}^{4} / \mathbb{Z}_{2}$. Denote $\left(x_{1}, x_{2}, x_{3}, x_{4}\right)$ coordinates in an orthonormal basis of $\mathbb{R}^{4}$, and define $r:=\sqrt{x_{1}^{2}+x_{2}^{2}+x_{3}^{2}+x_{4}^{2}}$, and a basis of invariant 1-forms on the sphere $\mathbb{S}^{3}$, $\left(\alpha_{1}, \alpha_{2}, \alpha_{3}\right)$ by
$$\alpha_{1}:=\frac{1}{r^{2}}\left(x_{1} d x_{2}-x_{2} d x_{1}+x_{3} d x_{4}-x_{4} d x_{3}\right)$$
and the other by cyclic permutation of the indices $\{2,3,4\}$.
Outside of the zero section of $T^{*} \mathbb{S}^{2}$ represented by $r=0$, the metric eh has the following expression (with the identification $T^{*} \mathbb{S}^{2} \backslash \mathbb{S}^{2} \approx\left(\mathbb{R}^{4} / \mathbb{Z}_{2}\right) \backslash\{0\}$ ):
$$\mathbf{e h}:=\sqrt{\frac{r^{4}}{1+r^{4}}}\left(d r^{2}+r^{2} \alpha_{1}^{2}\right)+\sqrt{1+r^{4}}\left(\alpha_{2}^{2}+\alpha_{3}^{2}\right) .$$
The metric extends to $T^{*} \mathbb{S}^{2}$ by adding the zero section $\mathbb{S}^{2}$ with metric $\alpha_{2}^{2}+\alpha_{3}^{2}$ at $r=0$. We will always denote $\mathbb{S}^{2}$ that zero-section of $T^{*} \mathbb{S}^{2}$.

This gives the asymptotic development at infinity
$$\mathbf{e h}=\mathbf{e}-\frac{1}{2 r^{4}}\left(d r^{2}+r^{2} \alpha_{1}^{2}-r^{2} \alpha_{2}^{2}-r^{2} \alpha_{3}^{2}\right)+\mathcal{O}\left(r^{-8}\right)$$
where $H^{4}:=-\frac{1}{2 r^{4}}\left(d r^{2}+r^{2} \alpha_{1}^{2}-r^{2} \alpha_{2}^{2}-r^{2} \alpha_{3}^{2}\right)$ is divergence-free and trace-free with respect to the Euclidean metric $\mathbf{e}=d r^{2}+r^{2}\left(\alpha_{1}^{2}+\alpha_{2}^{2}+\alpha_{3}^{2}\right)$.
1.2.1. Curvature of Eguchi-Hanson metrics. On $\mathbb{R}^{4}$, we define the 2 -forms
$$\theta_{1}^{ \pm}:=r d r \wedge \alpha_{1} \pm r^{2} \alpha_{2} \wedge \alpha_{3},$$
and similarly $\theta_{2}^{ \pm}$and $\theta_{3}^{ \pm}$by cyclic permutations, and we define the usual bases
$$\omega_{1}^{ \pm}:=d x_{1} \wedge d x_{2} \pm d x_{3} \wedge d x_{4}$$
and similarly $\omega_{2}^{ \pm}$and $\omega_{3}^{ \pm}$by cyclic permutations. The $\theta_{i}^{+}$and $\omega_{i}^{+}$are selfdual and the $\theta_{i}^{-}$ and $\omega_{i}^{-}$are anti-selfdual. Direct computations yield the following relation between them: $\theta_{i}^{+}=\omega_{i}^{+}$, and for $x \in \mathbb{R}^{4}$,
$$\theta_{i}^{-}(x)=\sum_{j=1}^{3} \frac{x^{T}\left(\omega_{i}^{+} \circ \omega_{j}^{-}\right) x}{|x|^{2}} \omega_{j}^{-},$$
where $\omega_{1}^{+} \circ \omega_{i}^{-}$is the symmetric traceless matrix given by the (commuting) product of the antisymmetric matrices associated to $\omega_{i}^{+}$and $\omega_{j}^{-}$, and where $x^{T}$ is the transpose of $x$.

Remark 1.12. The product $\omega_{i}^{+} \circ \omega_{j}^{-}=\omega_{i}^{-} \circ \omega_{j}^{+}$is a trace-free involution and therefore it is characterized by two planes of eigenvalues 1 and -1.

Remark 1.13. We will often use the identification of the traceless symmetric 2-tensors $\operatorname{Sym}_{0}^{2}(T M)$ and $\Omega^{+} \otimes \Omega^{-}$where $\left(\omega^{+}, \omega^{-}\right) \in \Omega^{+} \times \Omega^{-}$is associated to $\omega^{+} \circ \omega^{-}=\omega^{-} \circ \omega^{+}$.

For any $\zeta=\left(\zeta_{1}, \zeta_{2}, \zeta_{3}\right) \in \mathbb{R}^{3}$, we denote
$$\zeta^{ \pm}:=\zeta_{1} \omega_{1}^{ \pm}+\zeta_{2} \omega_{2}^{ \pm}+\zeta_{3} \omega_{3}^{ \pm} \in \Omega^{ \pm}$$

Definition 1.14. We define for any $x \in \mathbb{R}^{4}$ the linear transformation $\rho_{x}$ which to $\zeta=$ $\left(\zeta_{1}, \zeta_{2}, \zeta_{3}\right) \in \mathbb{R}^{3}$ associates $\rho_{x}(\zeta) \in \mathbb{R}^{3}$ whose $j$ 's coordinate is
$$\rho_{x}(\zeta)_{j}=\frac{x^{T}\left(\zeta^{+} \circ \omega_{j}^{-}\right) x}{|x|^{2}} .$$

Remark 1.15. Identifying $\mathbb{R}^{4}$ with the space of quaternions and $\mathbb{R}^{3}$ with the space of pure quaternions, for any $x \in \mathbb{R}^{4}$, the map $\rho_{x}: \mathbb{R}^{3} \rightarrow \mathbb{R}^{3}$ is exactly the rotation produced on the pure quaternionic part by conjugation by $x$. More precisely, identifying $\zeta \in \mathbb{R}^{3}$ with the pure quaternion $(0, \zeta)$ in the usual basis, we have
$$\left(0, \rho_{x}(\zeta)\right)=x \cdot(0, \zeta) \cdot x^{-1}$$

The metric eh is Ricci-flat, anti-selfdual and has the following anti-selfdual curvature:
$$\mathbf{R}^{-}(\mathbf{e h})=\frac{1}{r^{6}}\left[\begin{array}{ccc}
8 & 0 & 0 \\
0 & -4 & 0 \\
0 & 0 & -4
\end{array}\right]$$
in a basis asymptotic to the basis $\left(\theta_{i}^{-}\right)_{i}$, see [EH78]. We also remark that we have $H^{4}=$ $-\frac{\omega_{1}^{+} \circ \theta_{1}^{-}}{2 r^{4}}$ where $H^{4}$ is defined by $\mathbf{e h}=\mathbf{e}+H^{4}+\mathcal{O}\left(r^{-8}\right)$ at infinity and where $\omega_{1}^{+} \circ \theta_{1}^{-}$is the (commutating) composition of the antisymmetric matrices associated to $\omega_{1}^{+}$and $\theta_{1}^{-}$.

More generally, for any $\zeta=\left(\zeta_{1}, \zeta_{2}, \zeta_{3}\right) \in \mathbb{R}^{3} \backslash\{0\}$, consider $\left(\zeta_{(k)}^{+}\right)_{k \in\{1,2,3\}}$ an orthogonal basis of $\Omega^{+}$with constant length $\sqrt{2}=\left|\omega_{1}^{+}\right|$and $\zeta_{(k)}^{+}=\zeta^{+} /|\zeta|=\sqrt{2} \zeta^{+} /\left|\zeta^{+}\right|$. We may replace the above 1-forms $\alpha_{k}=\omega_{k}^{+}(d r)$ by the 1-forms $\zeta_{(k)}^{+}(d r)$. By a change of variables $u=\frac{r}{\sqrt{|\zeta|}}$, one checks that the metric
$$\mathbf{e h}_{\zeta^{+}}:=\sqrt{\frac{r^{4}}{|\zeta|^{2}+r^{4}}}\left(d r^{2}+r^{2} \zeta_{(1)}^{+}(d r)^{2}\right)+\sqrt{|\zeta|^{2}+r^{4}}\left(\zeta_{(2)}^{+}(d r)^{2}+\zeta_{(3)}^{+}(d r)^{2}\right)$$
is homothetic to eh and more precisely satisfies the following properties.
Proposition 1.16. Let $\zeta=\left(\zeta_{1}, \zeta_{2}, \zeta_{3}\right) \in \mathbb{R}^{3} \backslash\{0\}$ and denote $\zeta^{+}:=\zeta_{1} \omega_{1}^{+}+\zeta_{2} \omega_{2}^{+}+\zeta_{3} \omega_{3}^{+}$. We have the following properties:
\begin{itemize}
\item[(1)] at infinity, we have
$$\mathbf{e h}_{\zeta^{+}}=\mathbf{e}-\frac{\rho(\zeta)^{-} \circ \zeta^{+}}{2 r^{4}}+\mathcal{O}\left(|\zeta|^{4} r^{-8}\right)$$
\item[(2)] $\mathbf{e h}_{\zeta^{+}}$is isometric to $|\zeta| \cdot \mathbf{e h}$,
\item[(3)] $\mathbf{e h}_{(1,0,0)^{+}}=\mathbf{e h}$, and
\item[(4)] on $\mathbb{S}^{2}$, denoting $\left(\zeta_{(k)}^{+}\right)_{k \in\{1,2,3\}}$ a basis of the selfdual 2-forms of constant length with $\zeta_{(1)}^{+}=\zeta^{+} /|\zeta|$, the zero-section of $T^{*} \mathbb{S}^{2}$, the metric is $\left|\zeta^{+}\right|\left(\zeta_{(2)}^{+}(d r)^{2}+\zeta_{(3)}^{+}(d r)^{2}\right)$.
\end{itemize}
. \(\square\)

Remark 1.17. These metrics $\mathbf{e h}_{\zeta^{+}}$for $\zeta \in \mathbb{R}^{3} \backslash\{0\}$ reach all of the metrics obtained by orientation-preserving rotations and rescaling of eh up to isometry.

We will need to understand their curvature in the last sections of this article. From the computations of [EH78] and Proposition 1.16, we have the following result.

For $\zeta=\left(\zeta_{1}, \zeta_{2}, \zeta_{3}\right)$, denote $H^{4}\left(\zeta^{+}\right):=-\frac{\rho(\zeta)^{-} \circ \zeta^{+}}{2 r_{\mathbf{e}}^{4}}$. Then, the linearization of the curvature at $\mathbf{e}$ in the direction $H^{4}\left(\zeta^{+}\right)$is Ricci-flat anti-selfdual and we have
$$d_{\mathbf{e}} \mathbf{R}^{-}\left(H^{4}\left(\zeta^{+}\right)\right)=\frac{|\zeta|^{2}}{r^{6}}\left[\begin{array}{ccc}
8 & 0 & 0 \\
0 & -4 & 0 \\
0 & 0 & -4
\end{array}\right]$$
in any orthogonal basis with constant length of the anti-selfdual 2-forms of $\mathbb{R}^{4}$ whose first vector is $\frac{\rho(\zeta)^{-}}{|\zeta|}$.

Identifying the space of endomorphisms of $\Omega^{-}, \operatorname{End}\left(\Omega^{-}\right)$and $\Omega^{-} \otimes \Omega^{-}$, this can be rewritten as
$$d_{\mathbf{e}} \mathbf{R}^{-}\left(H^{4}\left(\zeta^{+}\right)\right)=\frac{12 \pi_{\operatorname{tr}}\left(\rho(\zeta)^{-} \otimes \rho(\zeta)^{-}\right)}{r^{6}}$$
where $\pi_{\mathrm{tr}} h:=h-\frac{\mathrm{tr} h}{3} \mathrm{I}_{3}$ is a projection on trace-free matrices.
Remark 1.18. In the constant basis ( $\omega_{1}^{-}, \omega_{2}^{-}, \omega_{3}^{-}$), the coefficients of $d_{\mathbf{e}} \mathbf{R}^{-}\left(H^{4}\left(\zeta^{+}\right)\right)$(seen as a 3 × 3 matrix) are harmonic by (8) as expected from [Biq16, Lemme 3].
1.2.2. Infinitesimal variations. The deformations of the Eguchi-Hanson metric are given by the variations of $\zeta$ in (10).

For $\zeta=(1,0,0)$, an orthogonal basis of the $L^{2}(\mathbf{e h})$-kernel of $P_{\mathbf{e h}}$ denoted O(eh) may be computed. Denote $\left(\mathbf{o}_{1}, \mathbf{o}_{2}, \mathbf{o}_{3}\right)$ given by the infinitesimal variations of $\zeta$ respectively in the directions (1, 0, 0), (0, 1, 0) and (0, 0, 1). They have the following developments in the coordinates of the above development (11),
$$\mathbf{o}_{k}=O_{k}^{4}+\mathcal{O}\left(r_{\mathbf{e}}^{-8}\right) \text { with } O_{k}^{4}=-\frac{\theta_{1}^{-} \circ \theta_{k}^{+}}{r^{4}} .$$

Remark 1.19. The symmetric 2-tensor $O_{1}^{4}$ is equal to twice to the asymptotic term $H^{4}$ of eh, see (11).

The infinitesimal deformations $\mathbf{o}_{1}, \mathbf{o}_{2}$ and $\mathbf{o}_{3}$ respectively induce the following infinitesimal changes of anti-selfdual curvature in the basis $\left(\theta_{1}^{-}, \theta_{2}^{-}, \theta_{3}^{-}\right)$:
$$\frac{1}{r^{6}}\left[\begin{array}{ccc}
8 & 0 & 0 \\
0 & -4 & 0 \\
0 & 0 & -4
\end{array}\right], \quad \frac{1}{r^{6}}\left[\begin{array}{ccc}
0 & 4 & 0 \\
4 & 0 & 0 \\
0 & 0 & 0
\end{array}\right], \quad \text { and } \quad \frac{1}{r^{6}}\left[\begin{array}{ccc}
0 & 0 & 4 \\
0 & 0 & 0 \\
4 & 0 & 0
\end{array}\right] .$$

For another $\zeta \in \mathbb{R}^{3} \backslash\{0\}$, let us consider, thanks to the second point of Proposition 1.16. a diffeomorphism $\phi$ such that $\phi^{*} \mathbf{e h}_{\zeta^{+}}=|\zeta| \cdot \mathbf{e h}$. Then, $\left(\mathbf{o}_{k}\left(\zeta^{+}\right)\right)_{k}:=\left(\phi_{*} \mathbf{o}_{k}\right)_{k}$ forms an orthogonal basis of $\mathbf{O}\left(\mathbf{e h}_{\zeta^{+}}\right)$with $\left\|\phi_{*} \mathbf{0}_{k}\right\|_{L^{2}\left(\mathbf{e h}_{\zeta^{+}}\right)}=\left\|\mathbf{o}_{k}\right\|_{L^{2}(\mathbf{e h})}$ since the $L^{2}$-norm of 2-tensors is invariant by rescaling in dimension 4. Recalling that in the same coordinates at infinity, the first $r_{\mathbf{e}}^{-4}$-terms of $|\zeta| \phi_{*} \mathbf{e h}$ and of $\mathbf{e h}_{\zeta^{+}}$coincide, we find
$$|\zeta| \cdot \phi_{*}\left(\frac{\omega_{1}^{+} \circ \theta_{1}^{-}}{2 r_{\mathbf{e}}^{4}}\right)=\frac{\zeta^{+} \circ \rho(\zeta)^{-}}{2 r_{\mathbf{e}}^{4}}$$
and therefore, denoting $\left(\zeta_{(k)}^{+}\right)_{k \in\{1,2,3\}}$ a basis of the selfdual 2-forms of constant length with $\zeta_{(1)}^{+}=\zeta^{+} /|\zeta|$, the development at infinity of the $\phi_{*} \mathbf{o}_{k}$ is
$$\mathbf{o}_{k}\left(\zeta^{+}\right)=\phi_{*} \mathbf{o}_{k}=\frac{\zeta_{(k)}^{+} \circ \rho(\zeta)^{-}}{r_{\mathbf{e}}^{4}}+\mathcal{O}\left(\left|\zeta^{+}\right|^{3} r_{\mathbf{e}}^{-8}\right) .$$

Remark 1.20. We check that $\mathbf{o}_{k}\left(\zeta^{+}\right)=\partial_{\zeta_{(k)}^{+}} \mathbf{e h}_{\zeta^{+}}$, where we denoted $\partial_{\zeta_{(k)}^{+}} \mathbf{e h}_{\zeta^{+}}$the differential of $\zeta^{+} \mapsto \mathbf{e h}_{\zeta^{+}}$at $\zeta^{+}$in the direction $\zeta_{(k)}^{+}$.
1.2.3. Negative orientation. We will also consider negatively oriented Eguchi-Hanson metrics. For $\zeta=\left(\zeta_{1}, \zeta_{2}, \zeta_{3}\right) \in \mathbb{R}^{3} \backslash\{0\}$, we define
$$\mathbf{e h}_{\zeta^{-}}:=\sqrt{\frac{r^{4}}{|\zeta|^{2}+r^{4}}}\left(d r^{2}+r^{2} \zeta_{(1)}^{-}(d r)^{2}\right)+\sqrt{|\zeta|^{2}+r^{4}}\left(\zeta_{(2)}^{-}(d r)^{2}+\zeta_{(3)}^{-}(d r)^{2}\right) .$$

It is isometric to $|\zeta| \cdot$ eh but has the opposite orientation. At infinity, we have the development
$$\mathbf{e h}_{\zeta^{-}}=\mathbf{e}-\frac{\zeta^{-} \circ \rho(\zeta)^{+}}{2 r^{4}}+\mathcal{O}\left(|\zeta|^{4} r^{-8}\right)$$
1.3. Naïve desingularizations. Let us now recall the definition of a naïve desingularization of an orbifold from [Ozu19a].

Gluing of ALE spaces to orbifold singularities. Let $0<2 \epsilon<\epsilon_{0}$ be a fixed constant, $t>0$, $\left(M_{o}, g_{o}\right)$ an orbifold and $\Phi: B_{e}\left(0, \epsilon_{0}\right) \subset \mathbb{R}^{4} / \mathbb{Z}_{2} \rightarrow U$ a local chart of Definition 1.2 around a singular point $p \in M_{o}$. Let also $\left(N, g_{b}\right)$ be an ALE metric asymptotic to $\mathbb{R}^{4} / \mathbb{Z}_{2}$, and $\Psi_{\infty}:\left(\mathbb{R}^{4} / \mathbb{Z}_{2}\right) \backslash B_{e}\left(0, \epsilon_{0}^{-1} t^{\frac{1}{2}}\right) \rightarrow N \backslash K$ a chart at infinity of Definition 1.5.

For $s>0$, define $\phi_{s}: x \in \mathbb{R}^{4} / \Gamma \rightarrow s x \in \mathbb{R}^{4} / \Gamma$. For $t<\epsilon_{0}^{4}$, we define $M_{o} \# N$ as $N$ glued to $M_{o}$ thanks to the diffeomorphism
$$\Phi \circ \phi_{\sqrt{t}} \circ \Psi^{-1}: \Psi\left(A_{\mathbf{e}}\left(\epsilon_{0}^{-1}, \epsilon_{0} t^{-1 / 2}\right)\right) \rightarrow \Phi\left(A_{\mathbf{e}}\left(\epsilon_{0}^{-1} \sqrt{t}, \epsilon_{0}\right)\right) .$$
Consider $\chi: \mathbb{R}^{+} \rightarrow \mathbb{R}^{+}$, a $C^{\infty}$ cut-off function supported on [0, 2] and equal to 1 on [0, 1].
Definition 1.21 (Naïve gluing of an ALE space to an orbifold). We define a naïve gluing of $\left(N, g_{b}\right)$ at scale $0<t<\epsilon^{4}$ to $\left(M_{o}, g_{o}\right)$ at the singular point $p$, which we will denote $\left(M_{o} \# N, g_{o} \#_{p, t} g_{b}\right)$ by putting $g_{o} \#_{p, t} g_{b}=g_{o}$ on $M \backslash U, g_{o} \#_{p, t} g_{b}=t g_{b}$ on $K$, and
$$g_{o} \#_{p, t} g_{b}=\chi\left(t^{-\frac{1}{4}} r_{e}\right) \Psi_{\infty}^{*} g_{b}+\left(1-\chi\left(t^{-\frac{1}{4}} r_{e}\right)\right) \Phi^{*} g_{o}$$
on $A_{\mathbf{e}}\left(\epsilon^{-1} \sqrt{t}, 2 \epsilon\right)$.
Definition 1.22 (Function $r_{D}$ on a naïve desingularization). On a naïve ( $M, g^{D}$ ), we define the function smooth function $r_{D}$ in the following way:
\begin{itemize}
\item[(1)] $r_{D}=r_{o}$ on $M_{o}\left(\epsilon_{0}\right)$ defined in (5),
\item[(2)] $r_{D}=\sqrt{t_{j}} r_{b_{j}}$ on each $N_{j}\left(\epsilon_{0}^{-1}\right)$ defined in (6) and
\item[(3)] $r_{D}=r_{\mathbf{e}}$ on $A_{\mathbf{e}}\left(\epsilon_{0}^{-1} \sqrt{t}, \epsilon_{0}\right)$.
\end{itemize}

Let us fix a notation for the desingularization by Eguchi-Hanson metrics.
Definition 1.23 (Naïve desingularization by Eguchi-Hanson metrics). Let $\left(M_{o}, \mathbf{g}_{o}\right)$ be a compact Einstein orbifold with integrable Einstein deformations (Definition 1.10) and $\mathbb{R}^{4} / \mathbb{Z}_{2}$ singularities at points $j \in S$, and let $v \in \mathbf{O}\left(\mathbf{g}_{o}\right)$ and $\zeta=\left(\zeta_{j}^{\epsilon_{j}}\right)_{j}$ with $\zeta_{j} \in \mathbb{R}^{3} \backslash\{0\}$ and $\epsilon_{j} \in\{+,-\}$. We define $g_{\zeta, v}^{D}$ the naïve gluing (as in Definition 1.21) of $\mathbf{e h}_{\zeta_{j}^{\epsilon_{j}}} /\left|\zeta_{j}\right|$ to $\mathbf{g}_{v}$ at scale $\left|\zeta_{j}\right|$ using the ALE coordinates of (10) and (17).

Definition 1.24 (Approximate obstructions $\tilde{\mathbf{O}}\left(g_{\zeta, v}^{D}\right)$ ). We define $\tilde{\mathbf{O}}\left(g_{\zeta, v}^{D}\right)$ the linear space spanned by the infinitesimal variations of $(v, \zeta) \mapsto g_{\zeta, v}^{D}$.

Remark 1.25. The space $\tilde{\mathbf{O}}\left(g_{\zeta, v}^{D}\right)$ is very close to the approximate obstruction space of [Ozu19b] and even yields better estimates. The results of [Ozu19b] therefore hold when using $\tilde{\mathbf{O}}\left(g_{\zeta, v}^{D}\right)$ instead of the similar space $\tilde{\mathbf{O}}\left(g^{D}\right)$ of [Ozu19b].

We next define the notion of nondegenerate sequence of naïve desingularizations in the spirit of [BR15] (see also the notion of generic smoothings in [Spo14]). It intuitively means that the desingularization sequence reaches an element $\partial_{o} \mathbf{E}(M)$ without being too tangent to $\partial_{o} \mathbf{E}(M)$.

Definition 1.26 (Nondegenerate naïve desingularization). We will say that a sequence of naïve desingularizations $\left(M, g_{t_{n}, v_{n}}^{D}\right)$ of a compact Einstein orbifold $\left(M_{o}, \mathbf{g}_{o}\right)$ is nondegenerate if, denoting $t_{n, \max }=\max t_{n, j}$ and $t_{n, \min }=\min t_{n, j}$, we have
\begin{itemize}
\item[(1)] $\lim _{n \rightarrow+\infty} \frac{t_{n, \text { min }}}{t_{n, \text { max }}}>0$ and
\item[(2)] $\frac{\left\|v_{n}\right\|_{L^{2}\left(\mathbf{g}_{o}\right)}^{2}}{t_{n, \text { min }}} \rightarrow 0$.
\end{itemize}

This technical definition essentially means that the gluing scales are comparable and the Einstein deformations of the orbifold are not too large. A stronger notion is that of transverse desingularization.

Definition 1.27 (Transverse naïve desingularization). We will say that a sequence of naïve desingularizations $\left(M, g_{t_{n}, v_{n}}^{D}\right)$ of a compact Einstein orbifold $\left(M_{o}, \mathbf{g}_{o}\right)$ is transverse if we have
\begin{itemize}
\item[(1)] $\lim _{n \rightarrow+\infty} \frac{t_{n, \text { min }}}{t_{n, \text { max }}}>0$ and
\item[(2)] $\frac{\left\|v_{n}\right\|_{L^{2}\left(\mathbf{g}_{o}\right)}}{t_{n, \text { min }}} \rightarrow 0$.
\end{itemize}

Remark 1.28. Usual desingularizations are transverse and often even orthogonal, with $v_{n}=0$. The desingularization of [Biq13] is a notable exception.

Let us finally recall that according to [Ozu19a, Ozu19b], for any Einstein orbifold $\left(M_{o}, \mathbf{g}_{o}\right)$, and any $\delta>0$, there exists $\epsilon=\epsilon\left(\left(M_{o}, \mathbf{g}_{o}\right), \delta\right)>0$ such that if an Einstein metric $(M, \mathbf{g})$ satisfies
$$d_{G H}\left(\left(M_{o}, \mathbf{g}_{o}\right),(M, \mathbf{g})\right)<\epsilon,$$
then, there exists a naïve desingularization $\left(M, g^{D}\right)$ of $\left(M_{o}, \mathbf{g}_{o}\right)$ and a diffeomorphism $\phi: M \rightarrow M$ with
$$\left\|\phi^{*} \mathbf{g}-g^{D}\right\|_{C_{\beta, *}^{2, \alpha}\left(g^{D}\right)}<\delta$$
where the weighted Hölder norms $C_{\beta, *}^{2, \alpha}\left(g^{D}\right)$ are defined in Section A in the Appendix.
We finally define the notions of nondegenerate and transverse sequence of Einstein metrics desingularizing the orbifold $\left(M_{o}, \mathbf{g}_{o}\right) \in \partial_{o} \mathbf{E}(M)$.

Definition 1.29 (Nondegenerate and transverse Einstein desingularization). Let $\left(M^{4}, \mathbf{g}_{n}\right)_{n \in \mathbb{N}}$ be a sequence of Einstein metrics $d_{G H}$-converging to a compact Einstein orbifold $\left(M_{o}, \mathbf{g}_{o}\right) \in$ $\partial_{o} \mathbf{E}\left(M^{4}\right)$. By [Ozu19a, Ozu19b], there exists a sequence of naïve desingularizations $\left(g_{t_{n}, v_{n}}^{D}\right)_{n}$ such that up to acting on $\mathbf{g}_{n}$ by a diffeomorphism, we have
\begin{itemize}
\item[(1)] $\left\|\mathbf{g}_{n}-g_{t_{n}, v_{n}}^{D}\right\|_{C_{\beta, *}^{2, \alpha}\left(g_{t_{n}, v_{n}}^{D}\right)} \leqslant \epsilon$ for some $\epsilon=\epsilon\left(\mathbf{g}_{o}\right)>0$ determined in [Ozu19b],
\item[(2)] $\mathbf{g}_{n}$ is in reduced divergence-free gauge (defined in Ozu19b]) with respect to $g_{t_{n}, v_{n}}^{D}$
\item[(3)] $\mathbf{g}_{n}-g_{t_{n}, v_{n}}^{D}$ is $L^{2}\left(g_{t_{n}, \zeta_{n}}^{D}\right)$-orthogonal to $\tilde{\mathbf{O}}\left(g_{t_{n}, \zeta_{n}}^{D}\right)$ of Definition 1.24
\end{itemize}

We will say that $\mathbf{g}_{n}$ is a nondegenerate (respectively transverse) Einstein desingularization of $\left(M_{o}, \mathbf{g}_{o}\right)$ if the sequence $\left(g_{\zeta_{n}, v_{n}}^{D}\right)_{n}$ is nondegenerate (respectively transverse) in the sense of Definitions 1.26 and 1.27.

\begin{figure}
\captionsetup{labelformat=empty}
\caption{Figure 1. A nondegenerate desingularization $\left(M, \mathbf{g}_{n}\right)_{n \in \mathbb{N}}$ approaches $\left(M_{o}, \mathbf{g}_{o}\right)$ without being "too tangent" to the boundary $\partial_{o} \mathbf{E}(M)$ : it stays in the I}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/67b4a74d-2d7c-424f-9fea-63309f824b2e-14.jpg?height=407&width=1071&top_left_y=416&top_left_x=496}
\end{figure}

\begin{figure}
\captionsetup{labelformat=empty}
\caption{Figure 2. A transverse desingularization $\left(M, \mathbf{g}_{n}\right)_{n \in \mathbb{N}}$ becomes almost orthogonal to the boundary $\partial_{o} \mathbf{E}(M)$ as it approaches $\left(M_{o}, \mathbf{g}_{o}\right)$ : it stays in the I}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/67b4a74d-2d7c-424f-9fea-63309f824b2e-14.jpg?height=329&width=1062&top_left_y=985&top_left_x=496}
\end{figure}

\section*{Transverse desingularization}

\section*{2. New obstructions to the desingularization of Einstein orbifolds}

We first deduce a new type of obstruction to the Gromov-Hausdorff desingularization of Einstein orbifolds which differs from the ones of [Biq13, Biq16, Ozu19b]. The goal of this section is to prove Theorem 0.2 and Proposition 0.4.

This obstruction is special to the compact case, or at least not present in the asymptotically hyperbolic (AH) context if one allows deformations of the conformal infinity (which are infinitely many new degrees of freedom which do not add obstructions).

Example 2.1. The AdS Taub-Bolt family of metrics constructed by Page-Pope [PP87] are asymptotically hyperbolic (AH) Einstein metrics and converge to an AH selfdual Einstein orbifold while bubbling out an Eguchi-Hanson metric (see [Ozu20t, Chapter B] for a precise description of the degeneration). This orbifold has only one singularity $\mathbb{R}^{4} / \mathbb{Z}_{2}$ at which we have $\operatorname{Ric}^{0}=0$ because it is Einstein, and in the usual bases of $\Omega^{ \pm}$, we have
$$\mathbf{R}^{-}=\left[\begin{array}{ccc}
-1 & 0 & 0 \\
0 & -1 & 0 \\
0 & 0 & -1
\end{array}\right],$$
because it is selfdual, and finally
$$\mathbf{R}^{+}=\left[\begin{array}{ccc}
0 & 0 & 0 \\
0 & -\frac{3}{2} & 0 \\
0 & 0 & -\frac{3}{2}
\end{array}\right],$$
only has a one-dimensional kernel.
The AdS Taub-Bolt orbifold is $L^{2}$-rigid. If we consider the Einstein deformations induced by the conformal changes at infinity, then, there exists an infinite dimensional space of nondegenerate Einstein desingularizations, see Biq13. This shows that the compactness assumption in Proposition 0.4 is necessary.
2.1. Degeneration and obstructions. Let ( $M_{o}, \mathbf{g}_{o}$ ) be a compact Einstein orbifold with integrable Einstein deformations (Definition 1.10) and with a $\mathbb{R}^{4} / \mathbb{Z}_{2}$ singularity at $p \in M_{o}$, and let ( $N$, eh) be an Eguchi-Hanson metric. At $p$, we can choose orbifold coordinates (Definition 1.2) in which the metric $\mathbf{g}_{o}$ is in Bianchi gauge with respect to the flat metric e (see [Ozu19b] for a proof in the more difficult case of neck regions), that is satisfies $B_{\mathbf{e}} \mathbf{g}_{o}=0$. Since the metric $\mathbf{g}_{o}$ is smooth in the above orbifold coordinates and because of the $\mathbb{Z}_{2}$-invariance, we have the following development,
$$\mathbf{g}_{o}=\mathbf{e}+H_{2}+H_{4}+\mathcal{O}\left(r_{\mathbf{e}}^{6}\right),$$
where the $H_{i}$ are homogeneous symmetric 2-tensors with $\left|H_{i}\right|_{\mathbf{e}} \sim r_{\mathbf{e}}^{i}$ with $B_{\mathbf{e}} H_{2}=0$. At the infinity of $N$, in the coordinates of (7), we have the following development,
$$\mathbf{e h}=\mathbf{e}+H^{4}+\mathcal{O}\left(r_{\mathbf{e}}^{-8}\right),$$
where $\left|H^{4}\right|_{\mathbf{e}} \sim r_{\mathbf{e}}^{-4}$ and with $B_{e} H^{4}=0$.
For a metric $g$, let us denote $Q_{g}^{(2)}$ the bilinear terms given by the second derivative of
$$h \mapsto \boldsymbol{\Phi}_{g}(h):=\operatorname{Ric}(h)+\delta_{h}^{*} B_{g} h$$
at $g$ (whose linearization is $P_{g}$ ). According to [Biq13] Section 3, Section 10 and Lemma 14.1], for any symmetric 2-tensors $\left|H_{2}\right|_{\mathbf{e}} \sim r_{\mathbf{e}}^{2}$ with $P_{\mathbf{e}} H_{2}=\Lambda \mathbf{e}$, and $\left|H_{4}\right|_{\mathbf{e}} \sim r_{\mathbf{e}}^{4}$ with $P_{\mathbf{e}} H_{4}=\Lambda H_{2}-Q_{\mathbf{e}}^{(2)}\left(H_{2}, H_{2}\right)$, there exist
\begin{itemize}
\item[(1)] a unique symmetric 2-tensor $\underline{h}_{2}$ and reals $\left(\lambda_{k}\right)_{k \in\{1,2,3\}}$ on $N$ satisfying:
$$\left\{\begin{aligned}
P_{\mathbf{e h}} \underline{h}_{2}= & \Lambda \mathbf{e h}+\sum_{k} \lambda_{k} \mathbf{o}_{k} \\
\underline{h}_{2}= & H_{2}+\mathcal{O}\left(r^{-2}\right) \\
\left.\int_{\mathbb{S}^{2}}\left\langle\underline{h}_{2}, \mathbf{o}_{k}\right\rangle_{\mathbf{e h}} d v_{\mathbf{e h}}\right|_{\mid \mathbb{S}^{2}}= & 0 \text { for all } k \in\{1,2,3\} .
\end{aligned}\right.$$
\item[(2)] and a symmetric 2-tensor $\underline{h}_{4}$ and real numbers $\left(\mu_{k}\right)_{k \in\{1,2,3\}}$ on $N$ satisfying:
$$\left\{\begin{aligned}
P_{\mathbf{e h}} \underline{h}_{4} & =\Lambda \underline{h}_{2}-Q_{\mathbf{e h}}^{(2)}\left(\underline{h}_{2}, \underline{h}_{2}\right)+\sum_{k} \mu_{k} \mathbf{o}_{k}, \\
\underline{h}_{4} & =H_{4}+\mathcal{O}\left(r^{\epsilon}\right), \\
\int_{\mathbb{S}^{2}}\left\langle\underline{h}_{4}, \mathbf{o}_{k}\right\rangle_{\mathbf{e h}} d v_{\mathbf{e h}_{\mid \mathbb{S}^{2}}} & =0 \text { for all } k \in\{1,2,3\} .
\end{aligned}\right.$$
for all $\epsilon>0$.
\end{itemize}

Remark 2.2. The above tensor $\underline{h}_{4}$ is not unique since there are 2 -tensors which are $\mathcal{O}(1)$ at infinity in the kernel of $P_{\mathbf{e h}}$. There will be a best choice of $\underline{h}_{4}$ in our construction which will ensure that the asymptotics on the orbifold and the ALE match, see Remark 2.11.
2.1.1. More precision on the first obstruction. Let $\zeta \in \mathbb{R}^{3} \backslash\{0\}$, and denote $\mathbf{o}_{k}\left(\zeta^{ \pm}\right)$the basis of $\mathbf{O}\left(\mathbf{e h}_{\zeta^{ \pm}}\right)$of (16). Since the metric $\mathbf{e h}_{\zeta^{ \pm}}$is homothetic to eh, we also find solutions $\underline{h}_{2}$ and $\underline{h}_{4}$ to
\begin{itemize}
\item[(1)] a unique symmetric 2-tensor $\underline{h}_{2}\left(\zeta^{ \pm}\right)$on $N$ satisfying the following equations
$$\left\{\begin{array}{c}
P_{\mathbf{e h}_{\zeta^{ \pm}}} \underline{h}_{2}\left(\zeta^{ \pm}\right)=\Lambda \mathbf{e h}_{\zeta^{ \pm}}+\sum_{k} \lambda_{k}\left(\zeta^{ \pm}\right) \mathbf{o}_{k}\left(\zeta^{ \pm}\right) \\
\underline{h}_{2}\left(\zeta^{ \pm}\right)=H_{2}+\mathcal{O}\left(r^{-2}\right) \\
\int_{\mathbb{S}^{2}}\left\langle\underline{h}_{2}\left(\zeta^{ \pm}\right), \mathbf{o}_{k}\left(\zeta^{ \pm}\right)\right\rangle_{\mathbf{e h}_{\zeta^{ \pm}}} d v_{\mathbf{e h}_{\zeta^{ \pm} \mid \mathbb{S}^{2}}}=0 \text { for all } k \in\{1,2,3\} .
\end{array}\right.$$
\end{itemize}
\begin{itemize}
\item[(2)] and a symmetric 2-tensor $\underline{h}_{4}\left(\zeta^{ \pm}\right)$on $N$ satisfying the following equations
$$\left\{\begin{array}{l}
P_{\mathbf{e h}_{\zeta} \pm} \underline{h}_{4}\left(\zeta^{ \pm}\right)=\Lambda \underline{h}_{2}\left(\zeta^{ \pm}\right)-Q_{\mathbf{e h}_{\zeta^{ \pm}}}^{(2)}\left(\underline{h}_{2}\left(\zeta^{ \pm}\right), \underline{h}_{2}\left(\zeta^{ \pm}\right)\right)+\sum_{k} \mu_{k}\left(\zeta^{ \pm}\right) \mathbf{o}_{k}\left(\zeta^{ \pm}\right) \\
\quad \underline{h}_{4}\left(\zeta^{ \pm}\right)=H_{4}+\mathcal{O}\left(r^{\epsilon}\right) \\
\int_{\mathbb{S}^{2}}\left\langle\underline{h}_{4}\left(\zeta^{ \pm}\right), \mathbf{o}_{k}\left(\zeta^{ \pm}\right)\right\rangle_{\mathbf{e h}_{\zeta^{ \pm}}} d v_{\mathbf{e h}_{\zeta^{ \pm} \mid \mathbf{S}^{2}}}=0 \text { for all } k \in\{1,2,3\}
\end{array}\right.$$
for all $\epsilon>0$.
\end{itemize}
We moreover have the following values for the $\lambda_{k}\left(\zeta^{ \pm}\right)$: for some $c>0$,
$$\lambda_{k}\left(\zeta^{ \pm}\right)=c\left\langle\mathbf{R}^{ \pm}\left(H_{2}\right) \zeta^{ \pm}, \zeta_{(k)}^{ \pm}\right\rangle,$$
where $\left(\zeta_{(k)}^{ \pm}\right)_{k \in\{1,2,3\}}$ is an orthogonal basis with $\left|\zeta_{(k)}^{ \pm}\right|=\sqrt{2}$ and $\zeta_{(1)}^{ \pm}=\zeta^{ \pm} /|\zeta|$.
We can be more precise about the first obstruction and the symmetric 2-tensor $\underline{h}_{2}$.
Lemma 2.3. Let $\underline{h}_{2}$ be one of the above solution of (22) (where we omit the dependence in $\zeta^{ \pm}$for simpler equations). Then, we have
$$\underline{h}_{2}=H_{2}+H_{2}^{4}+\mathcal{O}\left(r^{-4+\epsilon}\right) \text { for any } \epsilon>0 \text {, }$$
where $H_{2}^{4}$ is a homogeneous solution to
$$P_{\mathbf{e}} H_{2}^{4}=-Q_{\mathbf{e}}^{(2)}\left(H^{4}, H_{2}\right)+\Lambda H^{4}+\sum_{k} \lambda_{k} O_{k}^{4}, \text { with }\left|H_{2}^{4}\right|_{\mathbf{e}} \sim r_{\mathbf{e}}^{-2}$$
Moreover, when $\lambda_{k}=0$, then $H_{2}^{4}=0$.
Proof. At infinity, in ALE coordinates we have $\underline{h}_{2}=H_{2}+h^{\prime}$ with $h^{\prime}=\mathcal{O}\left(r_{\mathbf{e}}^{-2+\epsilon}\right)$ for all $\epsilon>0$. Since $\mathbf{e h}=\mathbf{e}+H^{4}+\mathcal{O}\left(r_{\mathbf{e}}^{-8}\right)$, we develop the equation (20) as:
$$P_{\mathbf{e}} H_{2}+P_{\mathbf{e}}\left(h^{\prime}\right)+Q_{\mathbf{e}}^{(2)}\left(H^{4}, H_{2}\right)+\mathcal{O}\left(r_{\mathbf{e}}^{-8+\epsilon}\right)=\Lambda \mathbf{e}+\Lambda H^{4}+\sum_{k} \lambda_{k} O_{k}^{4}+\mathcal{O}\left(r_{\mathbf{e}}^{-8+\epsilon}\right),$$
and using the assumption that $P_{\mathbf{e}} H_{2}=\Lambda \mathbf{e}$, we find
$$P_{\mathbf{e}}\left(h^{\prime}\right)+Q_{\mathbf{e}}^{(2)}\left(H^{4}, H_{2}\right)=\Lambda H^{4}+\sum_{k} \lambda_{k} O_{k}^{4}+\mathcal{O}\left(r_{\mathbf{e}}^{-8+\epsilon}\right) .$$
which is the stated equation. Now let us consider $H^{2}$ with $\left|H^{2}\right|_{\mathbf{e}} \sim r_{\mathbf{e}}^{-2}$ such that
$$P_{e} H^{2}=-Q_{\mathbf{e}}^{(2)}\left(H^{4}, H_{2}\right)+\Lambda H^{4}+\sum_{k} \lambda_{k} O_{k}^{4} .$$
It exists by Lemma A. 5 in the appendix (one checks that there is no log term). Then, we see that $P_{\mathbf{e}}\left(h^{\prime}-H^{2}\right)=\mathcal{O}\left(r_{\mathbf{e}}^{-8+\epsilon}\right)$ while $h^{\prime}=\mathcal{O}\left(r_{\mathbf{e}}^{-2+\epsilon}\right)$. By the theory of elliptic operators between weighted Hölder spaces (see for instance [PR78] or [LM85]), we therefore find that $h^{\prime}-H^{2}=\frac{K_{0}}{r_{\mathrm{e}}^{2}}+\mathcal{O}\left(r_{\mathbf{e}}^{-6+\epsilon}\right)$ for a constant symmetric 2-tensor $K_{0}$, and consequently
$$h^{\prime}=H_{2}^{4}+\mathcal{O}\left(r_{\mathbf{e}}^{-4+\epsilon}\right)=H^{2}+\frac{K_{0}}{r_{\mathbf{e}}^{2}}+\mathcal{O}\left(r_{\mathbf{e}}^{-4+\epsilon}\right)$$
which proves the stated result.
Let us now prove that if the obstructions $\lambda_{k}$ of (20) vanish, then $H_{2}^{4}=0$.

The idea is to use the uniqueness of $\underline{h}_{2}$, and show that $\mathcal{L}_{r \partial_{r}} \underline{h}_{2}$ satisfies the same equation. Indeed, we have:
$$\begin{aligned}
0=\mathcal{L}_{r \partial_{r}}\left(P_{\mathbf{e h}} \underline{h}_{2}-\Lambda \mathbf{e h}\right) & =Q_{\mathbf{e h}}^{(2)}\left(\mathcal{L}_{r \partial_{r}} \mathbf{e h}, \underline{h}_{2}\right)+P_{\mathbf{e h}} \mathcal{L}_{r \partial_{r}} \underline{h}_{2}-\Lambda \mathcal{L}_{r \partial_{r}} \mathbf{e h}, \\
& =P_{\mathbf{e h}} \mathcal{L}_{r \partial_{r}} \underline{h}_{2}-4 \Lambda \mathbf{e h} \\
& +Q_{\mathbf{e h}}^{(2)}\left(\mathcal{L}_{r \partial_{r}} \mathbf{e h}-2 \mathbf{e h}, \underline{h}_{2}\right)-\Lambda\left(\mathcal{L}_{r \partial_{r}} \mathbf{e h}-2 \mathbf{e h}\right)
\end{aligned}$$

Remark 2.4. In the last line, we used the fact that $Q_{\mathbf{e h}}^{(2)}\left(\mathbf{e h}, \underline{h}_{2}\right)+\Lambda \mathbf{e h}=0$, which comes from the (Bianchi-free version of) the identity $\operatorname{Ric}(s g)=\operatorname{Ric}(g)$ as 2-tensors for all $s>0$. This implies $D_{g} \operatorname{Ric}(g)=0$ for all $g$ and differentiating again at $g$ in the direction $h$ gives:
$$D_{g}^{2} \operatorname{Ric}(h, g)+D_{g} \operatorname{Ric}(h)=0 .$$
We use this formula with $g=\mathbf{e h}, h=\underline{h}_{2}$ and use the assumption that $D_{\mathbf{e h}} \operatorname{Ric}\left(\underline{h}_{2}\right)=$ $P_{\mathbf{e h}} \underline{h}_{2}=\Lambda \mathbf{e h}$ because the $\lambda_{k}$ vanish.

In (27), we recognize $-2 \mathbf{o}_{1}=\mathcal{L}_{r \partial_{r}} \mathbf{e h}-2 \mathbf{e h}$. Let us show that the last term vanishes. Using [Biq16, Lemme 3], we find for $c \neq 0$,
$$Q_{\mathbf{e h}}^{(2)}\left(\mathbf{o}_{1}, \underline{h}_{2}\right)-\Lambda \mathbf{o}_{1}=c \sum_{j} R_{1 j}^{+}\left(H_{2}\right) \mathbf{o}_{j}$$
and by [Biq13], if $\lambda_{1}=\lambda_{2}=\lambda_{3}=0$, then, $R_{11}^{+}\left(H_{2}\right)=R_{12}^{+}\left(H_{2}\right)=R_{13}^{+}\left(H_{2}\right)=0$, hence,
$$Q_{\mathbf{e h}}^{(2)}\left(\mathbf{o}_{1}, \underline{h}_{2}\right)-\Lambda \mathbf{o}_{1}=0 .$$
There remains $P_{\mathbf{e h}} \mathcal{L}_{r \partial_{r}} \underline{h}_{2}=4 \Lambda \mathbf{e h}$ in (27). Since $\mathcal{L}_{r \partial_{r}} \underline{h}_{2} \sim \mathcal{L}_{r \partial_{r}} H_{2}=4 H_{2}$ at infinity, we find the same first two equalities of (20) up to a constant 4 . Since $4 \underline{h}_{2}$ is the unique solution up to $\mathbf{O}(\mathbf{e h})$, we find that $\mathcal{L}_{r \partial_{r}} \underline{h}_{2}=4 \underline{h}_{2}+\mathcal{O}\left(r_{\mathbf{e}}^{-4}\right)$.

The point is that now $\mathcal{L}_{r \partial_{r}} H_{2}^{4}=0$ hence $\mathcal{L}_{r \partial_{r}} \underline{h}_{2}=4 H_{2}+\mathcal{O}\left(r_{\mathbf{e}}^{-4}\right)$, and consequently $\underline{h}_{2}=H_{2}+\mathcal{O}\left(r_{\mathbf{e}}^{-4}\right)$.

Remark 2.5. Let us note that the vanishing of $H_{2}^{4}$ is dependent on the coordinate system we consider for Eguchi-Hanson metric. It seems that the crucial property if these coordinates we use here is that the vector field $r \partial_{r}$ is harmonic. Since we will always take eh in the coordinates of (10), we will always have $H_{2}^{4}=0$ as long as the $\lambda_{k}$ vanish. \(\square\)

Later on, we will consider deformations of our orbifold as well and we will need to consider metrics which are not quite asymptotic to our target Euclidean metric, but a nearby one, i.e. $\mathbf{e}+H_{0}$ for some constant 2-tensor $H_{0}$.

Similarly, let us consider coordinates in which we have $\mathbf{g}_{o}=\mathbf{e}+H_{0}+H_{2}+\mathcal{O}\left(r_{\mathbf{e}}^{4}\right)$ for $H_{0}$ a traceless constant 2-tensor and let us denote $\psi: \mathbb{R}^{4} / \mathbb{Z}_{2} \rightarrow \mathbb{R}^{4} / \mathbb{Z}_{2}$ a linear isomorphism for which $\psi^{*} \mathbf{e}=\mathbf{e}+H_{0}$, in order to extend $H_{2}$ to $\psi^{*} \mathbf{e h}_{\zeta^{ \pm}}$.

Remark 2.6. Here, by $\psi^{*} \mathbf{e h}_{\zeta^{ \pm}}$, we really mean the same diffeomorphism applied to $\mathbf{e h}=$ $\mathbf{e}+\sum_{k \geqslant 2} \tilde{H}_{k}(\theta) r^{-2 k}$ in the polar coordinates $\theta \in \mathbb{R P}^{3}$ and $r \in[0,+\infty)$ as in Kro89a, Proposition 3.14], where $\left(\mathbb{R}^{4} / \mathbb{Z}_{2}, \mathbf{e}\right)=\left(\mathbb{R}^{+} \times \mathbb{R P}^{3}, d r^{2}+d r^{2} g_{\mathbb{R} \mathbb{P}^{3}}\right)$. The metric has to be "closed-up" by a different $\mathbb{S}^{2}$ at $\psi(0)=0$.

Then the obstructions are:
$$\lambda_{k}\left(\zeta^{ \pm}\right)=c\left\langle\mathbf{R}^{ \pm}\left(\psi_{*} H_{2}\right) \zeta^{ \pm}, \zeta_{(k)}^{ \pm}\right\rangle .$$

We will moreover need to extend constant 2-tensors to our Eguchi-Hanson metrics.

Lemma 2.7. Let $H_{0}$ be a constant 2 -tensor on $\mathbb{R}^{4} / \mathbb{Z}_{2}$, i.e. constant on $\mathbb{R}^{4}$. Then, there exists a unique 2-tensor $\underline{h}_{0}$ on $T^{*} \mathbb{S}^{2}$ satisfying:
$$\left\{\begin{array}{l}
P_{\mathbf{e h}} \underline{h}_{0}=0, \\
\underline{h}_{0}=H_{0}+H_{0}^{4}+\mathcal{O}\left(r^{-6+\epsilon}\right) \text { for all } \epsilon>0 \\
\underline{h}_{0} \perp_{L^{2}(\mathbf{e h})} \mathbf{O}(\mathbf{e h}) .
\end{array}\right.$$
Proof. Let $H_{0}=\mathcal{L}_{X_{1}} \mathbf{e}$ be a constant symmetric 2-tensor with $X_{1}$ a linear vector field. Then, since $P_{\mathbf{e}} H_{0}=0$, for $\chi$ a cut-off function supported in a neighborhood of infinity of eh, we have $P_{\mathbf{e h}}\left(\chi H_{0}\right)=\mathcal{O}\left(r_{\mathbf{e}}^{-6}\right)$, and an integration by parts against the $\mathbf{o}_{k}$ proves that $P_{\mathbf{e h}}\left(\chi H_{0}\right) \perp \mathbf{O}(\mathbf{e h})$ and there is no obstruction to finding $h^{\prime \prime}$ with $P_{\mathbf{e h}}\left(\chi H_{0}+h^{\prime \prime}\right)=0$ and $h^{\prime \prime}=\mathcal{O}\left(r_{\mathbf{e}}^{-4+\epsilon}\right)$ for all $\epsilon>0$, see [Biq13, Proposition 2.1]. This lets us find a solution $\underline{h}_{0}$ to
$$P_{\mathbf{e h}} \underline{h}_{0}=0, \text { with } \underline{h}_{0}=H_{0}+\mathcal{O}\left(r_{\mathbf{e}}^{-4}\right) .$$
with $B_{\mathbf{e h}} \underline{h}_{0}=0, \operatorname{tr}_{\mathbf{e h}} \underline{h}_{0}=0$ by the maximum principle since $\operatorname{tr}_{\mathbf{e h}} P_{\mathbf{e h}}=\frac{1}{2} \nabla_{\mathbf{e h}}^{*} \nabla_{\mathbf{e h}} \operatorname{tr}_{\mathbf{e h}}$ and $B_{\mathbf{e h}} P_{\mathbf{e h}}=B_{\mathbf{e h}} \delta_{\mathbf{e h}}^{*} B_{\mathbf{e h}}=\frac{1}{2} \nabla_{\mathbf{e h}}^{*} \nabla_{\mathbf{e h}} B_{\mathbf{e h}}$. We can make $\underline{h}_{0}$ unique by additionally assuming: $\underline{h}_{0} \perp \mathbf{O}(\mathbf{e h})$ and we find a development:
$$\underline{h}_{0}=H_{0}+H_{0}^{4}+\mathcal{O}\left(r_{\mathbf{e}}^{-6+\epsilon}\right) \text { with }\left|H_{0}^{4}\right|_{\mathbf{e}} \sim r_{\mathbf{e}}^{-4} .$$
The $L^{2}$-product between $\underline{h}_{0}$ and $\mathbf{o} \in \mathbf{O}(\mathbf{e h})$ is a priori ill-defined because $\mathbf{o}=\mathcal{O}\left(r^{-4}\right)$ and $\underline{h}_{0}=\mathcal{O}(1)$, but since the coefficients of the leading terms restricted to spheres $\{r=c s t\}$ belong to different eigenspaces of the Laplacian on $\mathbb{R P}^{3}$, this is therefore well-defined.

Remark 2.8. We can prove that we have $\underline{h}_{0}=\mathcal{L}_{\underline{x}_{1}}$ eh for some vector field $\underline{x}_{1}$ satisfying $0=B_{\mathbf{e h}} \mathcal{L}_{\underline{x}_{1}} \mathbf{e h}=\nabla_{\mathbf{e h}}^{*} \nabla_{\mathbf{e h}} \underline{x}_{1}$ and $\underline{x}_{1}=X_{1}+\mathcal{O}\left(r_{\mathbf{e}}^{-3+\epsilon}\right)$. We however do not have any application for this at the moment.