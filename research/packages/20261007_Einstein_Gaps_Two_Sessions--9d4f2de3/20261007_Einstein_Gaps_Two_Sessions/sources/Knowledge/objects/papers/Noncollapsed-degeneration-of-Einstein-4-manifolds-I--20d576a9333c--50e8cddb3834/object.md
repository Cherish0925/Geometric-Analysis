# Noncollapsed degeneration of Einstein 4–manifolds, I

- Category: papers
- Identity: doi:10.2140/gt.2022.26.1483
- Content status: fulltext_ok

---

---
source_file: Noncollapsed_degeneration_of_Einstein_4_manifolds__I_0dfa8a49d97d.pdf
converter: mathpix
format: mmd
---

\title{
Noncollapsed degeneration of Einstein 4-manifolds, I
}

\author{
Tristan Ozuch
}

A theorem of Anderson and Bando-Kasue-Nakajima from 1989 states that to compactify the set of normalized Einstein metrics with a lower bound on the volume and an upper bound on the diameter in the Gromov-Hausdorff sense, one has to add singular spaces called Einstein orbifolds, and the singularities form as blow-downs of Ricci-flat ALE spaces.

This raises some natural issues, in particular: can all Einstein orbifolds be Gromov-Hausdorff limits of smooth Einstein manifolds? Can we describe more precisely the smooth Einstein metrics close to a given singular one?

In this first paper, we prove that Einstein manifolds sufficiently close, in the Gromov-Hausdorff sense, to an orbifold are actually close to a gluing of model spaces in suitable weighted Hölder spaces. The proof consists in controlling the metric in the neck regions thanks to the construction of optimal coordinates.

This refined convergence is the cornerstone of our subsequent work on the degeneration of Einstein metrics or, equivalently, on the desingularization of Einstein orbifolds in which we show that all Einstein metrics Gromov-Hausdorff close to an Einstein orbifold are the result of a gluing-perturbation procedure. This procedure turns out to be generally obstructed, and this provides the first obstructions to a Gromov-Hausdorff desingularization of Einstein orbifolds.

\section*{Contents}
1 Trees of singularities and naïve desingularizations ..... 8
1.1 Einstein orbifolds and Ricci-flat ALE orbifolds ..... 8
1.2 Naïve desingularizations of an orbifold by trees of singularities ..... 9
1.3 Coordinates on a naïve desingularization ..... 10
1.4 Coordinates on an Einstein metric ..... 11
2 First coordinates ..... 13
$2.1 \epsilon$-regularity in the neck regions ..... 14
2.2 Construction of the first coordinates ..... 15
2.3 Consequences of the existence of the first coordinates. ..... 19
3 Controls on constant mean curvature hypersurfaces in low curvature re- gions ..... 22
4 Perturbation of hypersurfaces with almost constant second fundamental form ..... 27
5 Construction of a foliation of the neck regions by constant mean curvature hypersurfaces ..... 33
5.1 Local foliation by constant mean curvature hypersurfaces ..... 33
5.2 Global foliation of the neck regions. ..... 35
6 Construction of coordinates and control on the metric ..... 37
6.1 Coordinates based on our constant mean curvature foliation ..... 38
6.2 Control of the metric in these coordinates ..... 39
6.3 Proximity between the Einstein metric and the naïve desingularization in weighted $C^{k}$-norm ..... 42
A Optimal $C^{k, \alpha}$-proximity to a round sphere ..... 44
Bibliography ..... 45
Introduction
A fundamental question in geometry and topology is the following: given a topology (a differentiable manifold, $M$ ), is there an optimal geometry (a Riemannian metric, $g$ ) with this topology?

An Einstein metric, $g$ satisfies, for some real $\Lambda$, the equation
$$\operatorname{Ric}(g)=\Lambda g$$
where Ric is the Ricci curvature. These metrics are considered optimal for the homogeneity of their Ricci curvature and as critical points of the Einstein-Hilbert functional with fixed volume: $g \mapsto \int_{M} \mathrm{R}_{g} d v o l_{g}$, where R is the scalar curvature, which is the spatial and directional mean value of the sectional curvatures.

In dimension 2 and 3 these metrics have constant sectional curvatures and are therefore well understood as they only have 3 different local behavior depending on the sign of the curvature (spherical, flat and hyperbolic). Their understanding was crucial for 2-dimensional geometry and topology thanks to the uniformization Theorem and in 3-dimensional geometry topology thanks to Thurston's geometrization.

In dimension 4, Einstein metrics are moreover optimal as minimizers of the $L^{2}$-norm of Riemann curvature tensor: $g \mapsto \int_{M}\left|\mathrm{Rm}_{g}\right|^{2} d$ vol $_{g}$. Indeed, By Chern-Gauss-Bonnet formula, we have
$$\int_{M}\left|\operatorname{Rm}_{g}\right|^{2} d v_{g}=8 \pi^{2} \chi(M)+\int_{M}\left|\operatorname{Ric}_{g}^{0}\right|^{2} d v_{g}$$
where $\chi$ is the Euler characteristic and where $\int_{M}\left|\operatorname{Ric}_{g}^{0}\right|^{2} d v_{g} \geqslant 0$ vanishes if and only if $g$ is Einstein. Notice that in this case, the quantity $\int_{M}\left|\operatorname{Rm}_{g}\right|^{2} d v_{g}=8 \pi^{2} \chi(M)$ is purely topological.

But from dimension 4, the Einstein condition also becomes flexible as it does not imply that the sectional curvatures are constant anymore. It is actually so flexible that Einstein metrics can develop singularities. One major goal for 4-dimensional geometry is therefore to understand the set of Einstein metrics and how they can degenerate, that is to compactify the set of Einstein metrics. In this paper, we will be interested in Einstein 4-manifolds which are noncollapsed, which means that they have their volume bounded from below. The basic tool for this kind of compactification question is Gromov's compactness theorem [Gro81] from which the usual goals are to obtain informations about the possible limit spaces, and to understand if the convergence happens in a stronger sense than for the Gromov-Hausdorff distance.

The description of the limit spaces was given by Anderson and Bando-Kasue-Nakajima.

Theorem 0.1 ([And89, BKN89]) Let $\left(M_{i}^{4}, g_{i}\right)_{i \in \mathbb{N}}$ be a sequence of Einstein 4-manifolds satisfying,
\begin{itemize}
\item[(1)] the diameters of the ( $M_{i}^{4}, g_{i}$ ) are uniformly bounded,
\end{itemize}
\begin{itemize}
\item[(2)] the volumes of the $\left(M_{i}^{4}, g_{i}\right)$ are uniformly bounded from below,
\item[(3)] the integrals $\mathcal{E}_{i}:=\int_{M_{i}^{4}}\left|\operatorname{Rm}\left(g_{i}\right)\right|_{g_{i}}^{2} d v_{g_{i}}$ are uniformly bounded.
\end{itemize}

Then, there exists a subsequence ( $M_{i}^{4}, g_{i}$ ) converging to an Einstein orbifold with isolated singularities (see Definition 1.1), $\left(M_{\infty}^{4}, g_{\infty}\right)$.

Moreover, for any singular point $p_{\infty} \in M_{\infty}$, there exists a sequence $\left(p_{i}\right)_{i \in \mathbb{N}}$ of points of $M_{i}^{4}$ with $\frac{1}{t_{i}}:=\left|\operatorname{Rm}\left(g_{i}\right)\right|\left(p_{i}\right) \rightarrow \infty$ such that $\left(M_{i}^{4}, \frac{g_{i}}{t_{i}}, p_{i}\right)$ converges in the pointed Gromov-Hausdorff sense to a Ricci-flat asymptotically locally Euclidean (ALE) manifold, see Definition 1.2.

Remark 1 The first hypothesis prevents the formation of cusps, and the second prevents our space to collapse to a lower dimensional space. The third hypothesis, which is actually a consequence of the two others by [CN15, Theorem 1.13], is a topological condition by Chern-Gauss-Bonnet formula.

This theorem leaves several questions open, in particular the following one.
Question 1 ([And10, 7.I.]) "It has long been an open question whether Einstein orbifold metrics can be resolved to smooth Einstein metrics in the Gromov-Hausdorff topology. The idea here would be to reverse the process of formation of orbifold singularities described in [Theorem 0.1]"

For example, a natural question is whether or not any Einstein orbifold can be desingularized by Einstein metrics, say with an expected topology.

\section*{Desingularization of Einstein 4-orbifolds and obstructions}

A natural technique to desingularize Einstein orbifolds is a gluing-perturbation procedure: we glue Ricci-flat ALE manifolds to the singularities of the orbifold to obtain an approximate Einstein metric, and then try to perturb it into an actual Einstein metric. The existence of such desingularizations in the real Einstein context, and therefore a partial answer to Anderson's question was proven by Biquard for nondegenerate (i.e. which do not have any $L^{2}$-infinitesimal Einstein deformation) asymptotically hyperbolic Einstein manifolds with one singularity $\mathbb{R}^{4} / \mathbb{Z}_{2}$. This is realized by a particular gluing procedure of an Eguchi-Hanson metric to the singularity, see [Biq13, Theorem 0.1].

Strikingly, this particular desingularization is only possible if an obstruction is satisfied: denoting R the Riemannian curvature seen as an endomorphism on 2-forms, the
orbifold must satisfy $\operatorname{det} \mathbf{R}=0$ at its singular point. This obstruction is restrictive, and for example not satisfied by hyperbolic orbifolds (which are rigid) which therefore cannot be desingularized by this particular procedure.

\section*{Description of the degeneration in suitable weighted Hölder spaces}

The main goal of this series of paper is to prove that the obstruction of [Biq13] holds under much less assumptions. The least satisfactory one is that the metrics of the sequence have to come from a particular gluing-perturbation procedure. It even turns out that a convergence in the function spaces of [Biq13] cannot be true in general if one drops any of the following assumption:
\begin{itemize}
\item[(1)] the orbifold is rigid (it does not admit infinitesimal Einstein deformations),
\item[(2)] there is only one singular point,
\item[(3)] the singularity is $\mathbb{R}^{4} / \mathbb{Z}_{2}$.
\end{itemize}

The reasons are the following:
\begin{itemize}
\item[(1)] the convergence speed towards the orbifold could be arbitrarily slow compared to the singularity formation,
\item[(2)] different singularities may form at different speed,
\item[(3)] there might be trees of singularities forming.
\end{itemize}

In this paper, we will prove the cornerstone result of our program which states that if an Einstein metric is sufficiently close to an Einstein orbifold in the Gromov-Hausdorff sense, then it is actually close to a glued metric in some weighted Hölder norms bounded on symmetric 2-tensors decaying in the neck regions. These spaces are necessarily different from [Biq13] by the above reasons. The main result is the following theorem.

Theorem 0.2 Let $D_{0}, v_{0}>0, l \in \mathbb{N}$, then, there exists $\delta=\delta\left(D_{0}, v_{0}, l\right)>0$ such that if $\left(M, g^{\mathcal{E}}\right)$ is an Einstein manifold satisfying
\begin{itemize}
\item[-] the volume is bounded below by $v_{0}>0$,
\item[-] the diameter is bounded by $D_{0}>0$,
\item[-] the Ricci curvature is bounded $\mid$ Ric $\mid \leq 3$.
\end{itemize}
and for which there exists an Einstein orbifold ( $M_{o}, g_{o}$ ) with
$$d_{G H}\left(\left(M, g^{\mathcal{E}}\right),\left(M_{o}, g_{o}\right)\right) \leqslant \delta,$$
then, $\left(M, g^{\mathcal{E}}\right)$ is the result of a gluing-perturbation procedure detailed in [Ozu19b].

Notice that we are exactly in the context of Theorem 0.1, and that no assumption is made about the possible singularity models, the number of singular points or the orbifold metric. The goal of the present paper is the construction of suitable coordinates in which we will compare our metrics and prove a decay in the neck regions.

Theorem 0.1 actually implies that there is a satisfactory $C^{\infty}$-convergence on compact regions of the orbifold and of the Ricci-flat ALE spaces (without their singular points) appearing. Our main concern here will be to analyze the neck regions linking them, and to prove that there is convergence in a weighted $C^{\infty}$-sense. The main idea is to foliate these neck regions by constant mean curvature hypersurfaces thanks to which we will construct coordinates in which we will finally control our Einstein metrics.

\section*{Obstructions to the Gromov-Hausdorff desingularization of Einstein orbifolds}

In the compact case, we do not expect to desingularize general Einstein orbifolds by smooth Einstein metrics as there are infinitely many global (expected) obstructions, but we can identify obstructions to such a desingularization. In particular, we will identify the only local obstruction, $\operatorname{det} \mathbf{R}=0$ at the singular points, to desingularizing orbifolds for a large class of manifolds.

There is a well-known family of Ricci-flat ALE spaces called gravitational instantons which have been classified by [Kro89] and the Kähler Ricci-flat ALE spaces which are quotients of gravitational instantons have been classified in [Suv11]. It is a famous conjecture that all Ricci-flat ALE spaces are Kähler. One of our main results is an obstruction to the desingularization by this conjecturally exhaustive list of candidates.

Theorem 0.3 ([Ozu19b]) Let $\left(M_{i}, g_{i}\right)$ be a sequence of Einstein manifolds converging in the Gromov-Hausdorff sense to an Einstein orbifold $\left(M_{o}, g_{o}\right)$, and assume that every singularity blow-up is a Kähler Ricci-flat ALE orbifold in the positive orientation.

Then, at any singular point $p$ of ( $M_{o}, g_{o}$ ), we have
$$\operatorname{det} \mathbf{R}_{g_{o}}(p)=0 .$$
The condition on the singularity model can be reformulated as a topological assumption by [Nak90] and we have the following example.

Example 1 ([Ozu19b]) Consider $\mathbb{S}^{4} / \mathbb{Z}_{2}$ the Einstein orbifold with two $\mathbb{R}^{4} / \mathbb{Z}_{2}$ singularities obtained as the quotient of $\mathbb{S}^{4}$ by $\{ \pm\}$ in a global geodesic chart. Then, there
exists a differentiable manifold $M^{4}$, such that for any $1 \leqslant p<\infty$, we can construct a sequence of metrics ( $M, g_{i}$ ) with both
$$\left\|\operatorname{Ric}\left(g_{i}\right)-3 g_{i}\right\|_{L^{p}\left(g_{i}\right)} \rightarrow 0, \text { and } \operatorname{Ric}\left(g_{i}\right) \geqslant 3 g_{i},$$
while
$$\left(M, g_{i}\right) \xrightarrow{G H}\left(\mathbb{S}^{4} / \mathbb{Z}_{2}, g_{\mathbb{S}^{4} / \mathbb{Z}_{2}}\right),$$
but there does not exist any sequence of Einstein metrics with
$$\operatorname{Ric}\left(g_{i}\right)=3 g_{i},$$
and
$$\left(M, g_{i}\right) \xrightarrow{G H}\left(\mathbb{S}^{4} / \mathbb{Z}_{2}, g_{\mathbb{S}^{4} / \mathbb{Z}_{2}}\right) .$$
Let us finally mention one more application in the context of spin manifolds.
Theorem 0.4 ([Ozu19b]) Let $\left(M_{i}, g_{i}\right)$ be a sequence of spin Einstein 4-manifolds converging in the Gromov-Hausdorff sense to an Einstein orbifold $\left(M_{o}, g_{o}\right)$. Then, $\left(M_{o}, g_{o}\right)$ is spin, and at each singular point with group in $S U(2)$, we have
$$\operatorname{det} \mathbf{R}_{g_{o}}=0 .$$

\section*{Outline of the paper}

In Section 1, we start by giving the principal needed definitions. We then precise the convergence in Theorem 0.1 thanks to the introduction of glued metrics which we call naïve desingularizations. The goal of this article is to prove that they approximate Einstein metrics which are Gromov-Hausdorff close to an orbifold in the sense of appropriate weighted Hölder norms. We finally identify the neck regions in Einstein manifolds which are Gromov-Hausdorff close to an orbifold. The rest of the paper will be focused on these regions, and in Section 2, we construct some first coordinates in these neck regions by $\epsilon$-regularity.

In Section 3, we motivate the use of constant mean curvature hypersurfaces and prove that they are well controlled by the ambient geometry.

We develop a perturbation technique in Section 4 which we use in Section 5 to foliate the neck regions by constant mean curvature hypersurfaces by perturbation of the spheres of the first coordinates of Section 2.

In Section 6, we finally construct coordinates based on the foliation of Section 5 and use them to control the metric at the scale of the curvature which decays by the results of [Ban90].

\section*{Acknowledgements}

I would like to thank my PhD advisor, Olivier Biquard, for introducing me to the questions motivating this series of articles and for his constant support and encouragement.

\section*{1 Trees of singularities and naïve desingularizations}

Let us start by giving some definitions and explaining why we can reduce our situation to the study of neck regions.

\subsection*{1.1 Einstein orbifolds and Ricci-flat ALE orbifolds}

The singular limit spaces in Theorem 0.1 are Einstein orbifolds (with isolated singularities).

Definition 1.1 (Orbifold (with isolated singularities)) We will say that a metric space ( $M_{o}, g_{o}$ ) is an orbifold of dimension $n \in \mathbb{N}$ if there exists $\epsilon_{0}>0$ and a finite number of points $\left(p_{k}\right)_{k}$ of $M_{o}$ called singular such that we have the following properties:
\begin{itemize}
\item[(1)] the space $\left(M_{o} \backslash\left\{p_{k}\right\}_{k}, g_{o}\right)$ is a manifold of dimension $n$,
\item[(2)] for each singular point $p_{k}$ of $M_{o}$, there exists a neighborhood of $p_{k}, U_{k} \subset M_{o}$, a finite subgroup acting freely on $\mathbb{S}^{n-1}, \Gamma_{k} \subset S O(n)$, and a diffeomorphism $\Phi_{k}: B_{e}\left(0, \epsilon_{0}\right) \subset \mathbb{R}^{n} / \Gamma_{k} \rightarrow U_{k} \subset M_{o}$ for which, the pull-back of $\Phi_{k}^{*} g_{o}$ on the covering $\mathbb{R}^{n}$ is smooth.
\end{itemize}

Remark 2 Orbifold metrics will most of the time be indexed by a little $o$ for orbifold.

Theorem 0.1 only describes the formation of singularities at the scale of the maximum of the curvature where a Ricci-flat ALE manifold appears as a blow up, but there might actually be other singularities forming at different scales. They are modeled on Ricciflat ALE orbifolds. The relevant model spaces for us are therefore Einstein orbifolds and Ricci-flat ALE orbifolds with isolated singularities.

Definition 1.2 (ALE orbifold (with isolated singularities)) An ALE orbifold of dimension $n \in \mathbb{N},\left(N, g_{b}\right)$ is a metric space for which there exists $\epsilon_{0}>0$, singular points $\left(p_{k}\right)_{k}$ and a compact $K \subset N$ for which we have:
\begin{itemize}
\item[(1)] $\left(N, g_{b}\right)$ is a orbifold of dimension $n$,
\end{itemize}
\begin{itemize}
\item[(2)] there exists a compact subset $K \subset N$ and a diffeomorphism $\Psi_{\infty}:\left(\mathbb{R}^{n} /\right.$ $\left.\Gamma_{\infty}\right) \backslash B_{e}\left(0, \epsilon_{0}^{-1}\right) \rightarrow N \backslash K$ such that we have
$$r_{e}^{l}\left|\nabla^{l}\left(\Psi_{\infty}^{*} g_{b}-g_{e}\right)\right|_{C^{2}\left(g_{e}\right)} \leqslant C_{l} r_{e}^{-n} .$$
\end{itemize}

Remark 3 ALE metrics will most of the time be indexed by a little $b$ for bubble.

\subsection*{1.2 Naïve desingularizations of an orbifold by trees of singularities}

By [Ban90], under the assumptions of Theorem 0.1, at each singular point, a tree of Ricci-flat orbifolds forms. We index them by $b_{j}$ for $j$-th bubble.

Definition 1.3 (Tree of singularities or desingularization pattern) Consider $\left(M_{o}, g_{o}\right)$ an Einstein orbifold and $S_{o}$ a subset of its singular points, and $\left(N_{j}, g_{b_{j}}\right)_{j}$ a family of Ricci-flat ALE spaces asymptotic at infinity to $\mathbb{R}^{4} / \Gamma_{j}$ and $\left(S_{b_{j}}\right)_{j}$ a subset of their singular points. Let us also assume that there is a one to one "gluing" map $p$ : $j \mapsto p_{j} \in S_{o} \cup \bigcup_{k} S_{b_{k}}$, where the singularity at $p_{j}$ is $\mathbb{R}^{4} / \Gamma_{j}$. We will call $D:=$ $\left(\left(M_{o}, g_{o}, S_{o}\right),\left(N_{j}, g_{b_{j}}, S_{b_{j}}\right)_{j}, p\right)$ a tree of singularities or a desingularization pattern for $\left(M_{o}, g_{o}\right)$ depending on the point of view.

Let us define metrics which will mimic the degeneration of Einstein manifolds of Theorem 0.1, they will be called naïve desingularizations and the main goal of this paper is to show that degenerations of Einstein manifolds are well approximated by these naïve desingularizations.

Let us start by defining the naïve gluing of an ALE space $\left(N, g_{b}\right)$ to a singularity of an Einstein orbifold $\left(M_{o}, g_{o}\right)$. Recall the constant $\epsilon_{0}>0$ of Definitions 1.1 and 1.2.

Let $0<2 \epsilon<\epsilon_{0}, 0<t<\epsilon^{4}$, and $\left(M_{o}, g_{o}\right)$ be an orbifold and $\Phi: B_{e}\left(0, \epsilon_{0}\right) \subset \mathbb{R}^{4} /$ $\Gamma \rightarrow U$ a local chart around a singular point $p \in M_{o}$ which satisfies $\Phi^{*} g_{o}=g_{e}+$ $\mathcal{O}\left(r_{e}^{2}\right)$. Let also $\left(N, g_{b}\right)$ be an ALE orbifold asymptotic to $\mathbb{R}^{4} / \Gamma$, and $\Psi_{\infty}:\left(\mathbb{R}^{4} /\right.$ $\left.\Gamma_{\infty}\right) \backslash B_{e}\left(0, \epsilon_{0}^{-1}\right) \rightarrow N \backslash K$ a chart at infinity in wich $\Psi_{\infty}^{*} g_{b}=g_{e}+\mathcal{O}\left(r_{e}^{-4}\right)$. Consider finally $\chi$ a $C^{\infty}$-function from $\mathbb{R}^{+}$to $\mathbb{R}^{+}$supported on [ 0,2 ] and equal to 1 on [ 0,1 ] and for all $s>0$, define $\phi_{s}: x \in \mathbb{R}^{4} / \Gamma \rightarrow s x \in \mathbb{R}^{4} / \Gamma$.

We then define the orbifold $M_{o} \# N$ as $N$ glued to $M_{o}$ thanks to the diffeomorphism $\Phi \circ \phi_{\sqrt{t}} \circ \Psi^{-1}: \Psi\left(A_{e}\left(\epsilon_{0}^{-1}, \epsilon_{0} t^{-1 / 2}\right)\right) \rightarrow \Phi\left(A_{e}\left(\epsilon_{0}^{-1} \sqrt{t}, \epsilon_{0}\right)\right)$ which identifies their annuli $\Phi\left(A_{e}\left(\epsilon_{0}^{-1} \sqrt{t}, \epsilon_{0}\right)\right)$ and $\Psi\left(A_{e}\left(\epsilon_{0}^{-1}, \epsilon_{0} t^{-1 / 2}\right)\right)$.

Definition 1.4 (Naïve gluing of an ALE space to an orbifold singularity) We define a naïve desingularization of an orbifold $\left(M_{o}, g_{o}\right)$ at a singular point $p$ by an ALE metric $\left(N, g_{b}\right)$ at scale $t$, which we will denote ( $M_{o} \# N, g_{o} \#_{p, t} g_{b}$ ) by putting $g_{o} \#_{p, t} g_{b}=g_{o}$ on $M_{o} \backslash U, g_{o} \#_{p, t} g_{b}=\operatorname{tg}_{b}$ on $K \subset N$, and
$$g_{o} \#_{p, t} g_{b}=\chi\left(t^{-1 / 4} r_{e}\right) \Phi^{*} g_{o}+\left(1-\chi\left(t^{-1 / 4} r_{e}\right)\right) \phi_{t^{1 / 2}, *} \Psi_{\infty}^{*} g_{b}$$
on $A(t, \epsilon):=A_{e}\left(\epsilon^{-1} \sqrt{t}, b \epsilon\right)$.

More generally, it is possible to desingularize iteratively by trees of Ricci-flat ALE orbifolds. Let $0<2 \epsilon<\epsilon_{0},\left(M_{o}, g_{o}\right)$ be an Einstein orbifold and $\left(N_{j}, g_{b_{j}}\right)_{j}$ be a tree of ALE Ricci-flat orbifolds such that $M=M_{o} \#_{j} N_{j}$ is the result of a desingularization pattern $D$, and let $0<t_{j}<\epsilon^{4}$ be relative gluing scales.

Definition 1.5 (Naïve desingularization of an orbifold by a tree or Ricci-flat orbifolds) The naïve desingularization metric $g_{t}^{D}$ on $M=M_{o} \#_{j} N_{j}$ is then the result of the following iterative construction.

Start with a deepest bubble ( $N_{j}, g_{b_{j}}$ ), that is, $j$ such that $S_{j}=\emptyset$. If $p_{j} \in N_{k}$ and we replace ( $N_{k}, g_{b_{k}}, S_{j}$ ) and ( $N_{j}, g_{b_{j}}, \emptyset$ ) by ( $N_{k} \# N_{j}, g_{b_{k}} \#_{p_{j}, t_{j}} g_{b_{j}}, S_{k} \backslash\left\{p_{j}\right\}$ ) and restrict $p$ as $l \rightarrow p_{l}$ for $l \neq j$ in $D$ and consider another deepest bubble, the same works if $p_{j} \in M_{o}$.

Moreover, if $N_{j}$ is glued to $p_{j} \in N_{j_{1}}$, and $N_{j_{1}}$ is glued to $p_{j_{1}} \in N_{j_{2}}, \ldots, N_{j_{k-1}}$ is glued to $N_{j_{k}}$, which is glued to $M_{o}$, we define $T_{j}:=t_{j_{1}} t_{j_{2}} \ldots t_{j_{k}}$. This way, on each $N_{j}(2 \epsilon)$, the metric is $T_{j} g_{b_{j}}$.

Remark 4 Our construction depends on a gauge choice: the diffeomorphisms used to glue the infinity of our ALE spaces to orbifold singularities can be composed with any isometry of $\mathbb{R}^{4} / \Gamma_{k}$. There is therefore a gluing gauge $\phi_{k} \in \operatorname{Isom}\left(\mathbb{R}^{4} / \Gamma_{k}\right)$ at each point. These choices are equivalent to gluing different ALE spaces and they lead to different metrics, hence we will not worry too much about this degree of freedom here.

\subsection*{1.3 Coordinates on a naïve desingularization}

The above metric $g_{t}^{D}$ on $M$ of Definition 1.5 has some well identified regions in which the metric is that of the orbifold, of one of the Ricci-flat ALE spaces or close to an annulus of a flat cone

Definition 1.6 (Coordinates on the model spaces: $M_{o}(\epsilon), N_{j}(\epsilon)$ and $A_{k}(t, \epsilon)$ ) With the notations of definitions 1.1 and 1.2, for $0<\epsilon \leqslant \epsilon_{0}$, we will denote
\begin{itemize}
\item[-] $M_{o}(\epsilon):=M_{o} \backslash\left(\bigcup_{k} \Phi_{k}\left(B_{e}(0, \epsilon)\right)\right) \subset M_{o}$,
\item[-] $N_{j}(\epsilon):=N_{j} \backslash\left(\bigcup_{k} \Psi_{k}\left(B_{e}(0, \epsilon)\right) \cup \Psi_{\infty}\left(\left(\mathbb{R}^{4} / \Gamma_{\infty}\right) \backslash B_{e}\left(0, \epsilon^{-1}\right)\right)\right) \subset N_{j}$,
\item[-] $A_{j}(t, \epsilon):=A_{e}\left(\epsilon^{-1} \sqrt{T_{j}} \sqrt{t_{j}}, \epsilon \sqrt{T_{j}}\right) \subset \mathbb{R}^{4} / \Gamma_{k}$.
\end{itemize}
We see that these sets naturally embed in our manifold $M$ thanks to the above naïve desingularization construction.

Remark 5 The sets $M_{o}(\epsilon)$ and $N_{j}(\epsilon)$ are the compact sets of the orbifolds minus their singular points which appear in [Ban90, Theorem A]. They are exhaustive as $\epsilon$ tends to zero.

They moreover form a covering of $M=M_{o} \#_{j} N_{j}$ adapted to a degeneration at relative scales $\left(t_{j}\right)_{j}$ :
$$M=\bigcup_{j}\left(N_{j}(\epsilon) \cup A_{j}(t, \epsilon)\right) \cup M_{o}(\epsilon) .$$

\subsection*{1.4 Coordinates on an Einstein metric}

The goal will be to identify each of these regions with a region of an Einstein manifold $(M, g)$ close enough to an Einstein orbifold $\left(M_{o}, g_{o}\right)$ in the Gromov-Hausdorff sense.

Definition 1.7 (Manifold $\epsilon$-approximated by a naïve desingularization) Let $\epsilon>0$, $l \in \mathbb{N}$ and fix $t=\left(t_{j}\right)_{j}$ with $t_{j}<\epsilon^{4}$ for all $j$. We will say that a Riemannian manifold $(M, g)$ is $\epsilon$-approximated in $C^{l}$-norm by a naïve desingularization $\left(M, g_{t}^{D}\right)$ of $\left(M_{o}, g_{o}\right)$, if there exists a diffeomorphism $\Phi: M \rightarrow M$ such that if we denote $\Phi\left(M_{o}(\epsilon)\right)=\mathcal{M}_{o}(\epsilon) \subset M$ and $\Phi\left(N_{j}(\epsilon)\right)=\mathcal{N}_{j}(\epsilon) \subset M$ and $\mathcal{A}_{k}(t, \epsilon)$ the region of $M \backslash \mathcal{M}_{o}(32 \epsilon) \cup \bigcup_{j} \mathcal{N}_{j}(32 \epsilon)$ with nonempty intersection with $\Psi_{\infty}\left(B_{e}\left(0, \epsilon^{-1}\right)\right) \subset \mathcal{N}_{k}(\epsilon)$ :
\begin{itemize}
\item[(1)] on $\mathcal{M}_{o}(\epsilon)$ in $M$, we have
$$\left\|\Phi^{*} g-g_{o}\right\|_{C^{l}\left(g_{o}\right)}=\left\|\Phi^{*} g-g^{D}\right\|_{C^{l}\left(g^{D}\right)} \leqslant \epsilon,$$
\item[(2)] on the zone $\mathcal{N}_{j}(\epsilon)$ in $M$, we have
$$\left\|\frac{\Phi^{*} g}{T_{j}}-g_{b_{j}}\right\|_{C^{l}\left(g_{b_{j}}\right)}=\left\|\Phi^{*} g-g^{D}\right\|_{C^{l}\left(g^{D}\right)} \leqslant \epsilon,$$
\item[(3)] and on $\mathcal{A}_{k}(t, \epsilon)$, we have
$$\int_{\mathcal{A}_{k}(t, \epsilon)}|\operatorname{Rm}|^{2} d v_{g}<\epsilon^{2} .$$
\end{itemize}

Proposition 1 Under the assumptions of Theorem 0.1, given a sequence $\left(M_{i}, g_{i}\right)_{i}$ of Einstein manifolds converging in the Gromov-Hausdorff sense to an Einstein orbifold $\left(M_{o}, g_{o}\right)$, there exist a subsequence still denoted $\left(M_{i}, g_{i}\right)_{i}$ and naïve desingularizations ( $M_{i}, g_{t_{i}}^{D}$ ) such that for all $\epsilon>0$ and $l \in \mathbb{N}$, for $i$ large enough, the manifold $\left(M_{i}, g_{i}\right)$ is $\epsilon$-approximated in $C^{l}$-norm by $\left(M_{i}, g_{t_{i}}^{D}\right)$.

Proof Let $\left(M_{i}, g_{i}\right) \xrightarrow[G H]{ }\left(M_{o}, g_{o}\right)$ be a sequence of manifolds satisfying the assumptions of Theorem 0.1. Up to taking a subsequence, for any singular point of $M_{o}$, there exists a sequence of scales $T_{i}>0$ and of points $p_{i}$ of $M_{i}^{4}$ of high curvature $\left|\operatorname{Rm}\left(g_{i}\right)\right|\left(p_{i}\right) \rightarrow \infty$ such that: $\left(M_{i}^{4}, \frac{g_{i}}{T_{i}}, p_{i}\right)$ converging smoothly on compact subsets to $\left(N, g_{b}, p\right)$ a Ricci-flat ALE orbifold without its singular points. The convergence is moreover smooth at a bounded from below distance from the singular points since we are considering Einstein metrics with bounded curvature and harmonic radii bounded from below.

Let $\epsilon>0$ and $l \in \mathbb{N}$, by considering the compact $N_{j}(\epsilon)$, there exists $i_{j} \in \mathbb{N}$ such that for all $i>i_{j}$, there is a diffeomorphism on its image $\Phi_{i}: N(\epsilon) \rightarrow M_{i}$ with $\left\|\frac{\Phi_{i}^{*} g_{i}}{T_{i}}-g_{b_{j}}\right\|_{C^{l}} \leq \epsilon$ and similarly, there exists a rank $i_{o}$ from which we have the $C^{l}$-closeness on $M_{o}(\epsilon)$. Since there are only finitely many scales in each tree of singularities, we can take the maximum of the ranks $i_{j}$ and $i_{o}$ to obtain the result.

The control of the $L^{2}$-norm of the Riemannian curvature is proven in [Ban90]. \(\square\)

The main objective of this paper will be to construct good coordinates in the neck regions $\mathcal{A}_{k}(t, \epsilon)$. These regions $\mathcal{A}_{k}(t, \epsilon)$ between $N_{k}$ and $N_{j}$ are included in metric annuli $A\left(\frac{1}{8} T_{k}^{\frac{1}{2}} \epsilon^{-1}, 8 T_{j}^{\frac{1}{2}} \epsilon\right)$ centered at $p_{k}$, and in $A\left(\frac{1}{8} t_{k}^{\frac{1}{2}} \epsilon^{-1}, 8 \epsilon\right)$ if $N_{k}$ is directly glued to $M_{o}$ (in this case, $t_{k}=T_{k}$ because it is the shallowest scale). Let us note that the volume growth is almost Euclidean on them.

Lemma 1.8 For any $0<\delta<1$, there exists $\epsilon>0$ such that if a manifold ( $M, g$ ) is $\epsilon$-approximated by a naïve desingularization $g_{t}^{D}$ in $C^{0}$-norm for $t<\epsilon^{4}$ with $\operatorname{Ric}(g) \geqslant$ $-3 g$, then, if $\mathcal{A}_{k}(t, \epsilon) \subset A\left(\frac{1}{8} T_{k}^{\frac{1}{2}} \epsilon^{-1}, 8 T_{j}^{\frac{1}{2}} \epsilon\right)=A\left(\rho_{1}, \rho_{2}\right)$, we have
$$\left|\frac{\operatorname{Vol}_{g}\left(B_{g}\left(\delta^{-1} \rho_{2}\right)\right)}{\operatorname{Vol}_{g}\left(B_{g}\left(\delta \rho_{1}\right)\right)}-\frac{\left(\delta^{-1} \rho_{2}\right)^{4}}{\left(\delta \rho_{1}\right)^{4}}\right| \leqslant \delta .$$

Proof Let us consider the case of an annular region $\mathcal{A}_{k}(t, \epsilon)$ between a Ricci-flat ALE $\left(N, g_{b}\right)$ and an orbifold $\left(M_{o}, g_{o}\right)$, which are asymptotic to $\mathbb{R}^{4} / \Gamma$, at scale $0<t<\epsilon^{4}$
for $\epsilon>0$ which we will choose small enough. By definition of an $\epsilon$-approximated metric, the ball $\left(B\left(\delta^{-1} \rho_{2}\right), g\right)$ is arbitrarily close in the Gromov-Hausdorff sense to the ball of radius $\delta^{-1} \epsilon$ of $\left(M_{o}, g_{o}\right)$ for $\epsilon$ arbitrarily small, and by definition of an orbifold metric, as $\delta^{-1} \epsilon \rightarrow 0$, we have
$$\frac{\operatorname{Vol}_{g_{o}}\left(B_{g_{o}}\left(\delta^{-1} \epsilon\right)\right)}{\left(\delta^{-1} \epsilon\right)^{4}} \rightarrow \frac{\omega_{4}}{|\Gamma|},$$
the volume of the unit ball of $\mathbb{R}^{4} / \Gamma$.
Similarly, the ball $\left(B_{g / t}\left(\delta \epsilon^{-1}\right), g / t\right)$ is arbitrarily close in the Gromov-Hausdorff sense to the ball of radius $\delta \epsilon^{-1}$ of ( $N, g_{b}$ ) whose volume satisfies for $\delta^{-1} \epsilon \rightarrow 0$
$$\frac{\operatorname{Vol}_{g_{b}}\left(B_{g_{b}}\left(\delta \epsilon^{-1}\right)\right)}{\left(\delta \epsilon^{-1}\right)^{4}} \rightarrow \frac{\omega_{4}}{|\Gamma|} .$$
As a consequence, by the continuity of volume for the Gromov-Hausdorff distance between manifolds with Ric $\geqslant-3 g$, [Col97], we have the stated result for $\epsilon$ small enough. \(\square\)

The goal is now to construct a diffeomorphism from a flat cone of $\left(\mathbb{R}^{n} / \Gamma, g_{e}\right)$ to our intermediate annulus. Thanks to the controls on the curvature of [Ban90, Proposition 3], we expect that a "natural" coordinate system must also have good enough controls. Here we choose to foliate our annuli by constant mean curvature hypersurfaces before constructing coordinates relying on them.

\section*{2 First coordinates}

The main difficulty here in constructing our coordinates when compared to the context of [BKN89] is that we do not have an asymptotic behavior of our metric on which we can base our construction. We will need to start by using a first set of local coordinates which is only partially satisfactory. The main goal of this section is the proof of the following proposition.

Proposition 2 For all $\delta>0, D_{0}>0, v_{0}>0, E>0$ and $l \in \mathbb{N}$, there exists $\epsilon_{2}>0$ such that if an Einstein manifold satisfies:
\begin{itemize}
\item[-] its diameter is bounded by $D_{0}>0$,
\item[-] its volume is bounded below by $v_{0}>0$,
\item[-] its Ricci curvature is bounded below by -3,
\end{itemize}
\begin{itemize}
\item[-] there exists an annulus $A\left(\rho_{1}, \rho_{2}\right)$ with $4 \rho_{1}<\rho_{2}$ satisfying:
$$\int_{A\left(\rho_{1}, \rho_{2}\right)}|\mathrm{Rm}|^{2} \leqslant \epsilon_{2}^{2}$$
and $\int_{B\left(\rho_{2}\right)}|\operatorname{Rm}|^{2} \leqslant E$,
\item[-] the volume growth in the annulus is almost Euclidean
$$\left|\frac{\operatorname{Vol}\left(B\left(\rho_{2}\right)\right)}{\operatorname{Vol}\left(B\left(\epsilon_{2} \rho_{1}\right)\right)}-\frac{\rho_{2}^{4}}{\left(\epsilon_{2} \rho_{1}\right)^{4}}\right| \leqslant \epsilon_{2} .$$
Then, for any $\rho \in\left[2 \rho_{1}, \frac{1}{4} \rho_{2}\right]$ there exists a region $\hat{A}(\rho, 2 \rho)$ close to the annulus $A(\rho, 2 \rho)$ in the following sense,
$$A((1+\delta) \rho,(2-\delta) \rho) \subset \hat{A}(\rho, 2 \rho) \subset A((1-\delta) \rho,(2+\delta) \rho),$$
such that there exists $\Gamma$ a finite subgroup of $S O(4)$ and a diffeomorphism
$$\Phi_{\rho}: A_{e}(1,2) \subset \mathbb{R}^{4} / \Gamma \rightarrow \hat{A}(\rho, 2 \rho) \subset M,$$
for which we have :
$$\left\|\frac{\Phi_{\rho}^{*} g}{\rho^{2}}-g_{e}\right\|_{C^{l}\left(A_{e}(1,2)\right)} \leqslant \delta$$
\end{itemize}

\section*{$2.1 \epsilon$-regularity in the neck regions}

Definition 2.1 (Hölder spaces) The $C^{k, \alpha}$-norms will be taken at the scale of the injectivity radius. Which means that we define the $C^{k, \alpha}$-norm of a tensor $s$ in the following way:
$$\|s\|_{C^{k, \alpha}}:=\|s\|_{C^{0}}+\ldots+\left\|\nabla_{g}^{k} s\right\|_{C^{0}}+\sup _{x}\left[\nabla_{g}^{k} s\right]_{C^{\alpha}(g)}(x),$$
where, for a tensor $u$, a point $x, \alpha>0$ and a metric $g$, if we denote exp ${ }_{x}$ the exponential map at $x$ whose injectivity radius is $\operatorname{inj}_{g}(x)$, we define the Hölder seminorm of $u$ on $M$ as
$$[u]_{C^{\alpha}(g)}(x):=\sup _{\left\{y \in T_{x} M,|y|<\operatorname{inj}_{g}(x)\right\}}\left|\frac{\exp _{x}^{*} u(0)-\exp _{x}^{*} u(y)}{|y|^{\alpha}}\right|_{\exp _{x}^{*} g} .$$
We will also sometimes use the harmonic radius which is defined at $x \in M$, as the supremum of the $r>0$ for which there exists a diffeomorphism $\Phi: B(x, r) \rightarrow \mathbb{R}^{n}$, $\Phi(y)=\left(h_{1}(y), \ldots, h_{n}(y)\right)$ such that for all $i \in\{1, \ldots, n\}$,
$$\Delta_{g} h_{i}=0,$$
and denoting $g_{i j}$ the push forward of $g$ by $\Phi$,
$$\left\|g_{i j}-\delta_{i j}\right\|_{C^{0}}+r^{1+\alpha}\left\|g_{i j}\right\|_{C^{1+\alpha}} \leqslant \frac{1}{100} .$$

Lemma 2.2 Under the assumptions of Proposition 2, there exists a constant $r_{0}>0$ only depending on $D_{0}$ and $v_{0}$, such that for all points of $A\left(2 \rho_{1}, \frac{1}{2} \rho_{2}\right)$ at distance $2 \rho_{1}<\rho<\frac{1}{2} \rho_{2}$ from the center, the injectivity radius and the harmonic radius are bounded below by $r_{0} \rho$.

Proof Let us consider a point $x$ at distance $\rho \in\left[2 \rho_{1}, \frac{1}{2} \rho_{2}\right]$ from the center of the annulus and the ball $B\left(x, \frac{\rho}{2}\right)$. Thanks to Bishop-Gromov inequality, the volume of $B\left(x, \frac{\rho}{2}\right)$ is bounded from below by $C_{1} \rho^{4}$ for a constant $C_{1}>0$ only depending on $v_{0}$ and $D_{0}$. To control the curvature, we use the following $\epsilon$-regularity theorem:

Lemma 2.3 ([Gao90, Theorems 4.8, 4.9 and 4.11]) In an Einstein manifold $(M, g)$ satisfying the assumptions of Proposition 2, for any $C_{0}>0$ there exists a constant $\epsilon=\epsilon\left(C_{0}, v_{0}, D_{0}\right)$ such that if at a point $x \in M$ and for $\rho>0$ we have $\operatorname{Vol}_{g}\left(B_{g}(x, \rho)\right)>$ $C_{0} \rho^{4}$ and
$$\int_{B(x, 2 \rho)}|\operatorname{Rm}(g)|^{2} d v(g)<\epsilon^{2}$$
then, we have
$$|\operatorname{Rm}(g)| \leqslant \frac{1}{\rho^{2}}$$
on $B(x, \rho)$.
Therefore for $\rho \in\left[4 \rho_{1}, \frac{1}{4} \rho_{2}\right]$, up to shrinking the constant $\epsilon_{2}$ of the statement to be smaller than $\epsilon\left(16 C_{1}\right)>0$, the ball $B\left(x, \frac{\rho}{2}\right)$ satisfies (2). Hence, the curvature at distance $\rho$ is smaller than $\frac{1}{\rho^{2}}$ by (3).

By [CGT82, Theorem 4.3], these controls on the curvature and the volume at scale $\rho$ imply that there exists a constant $r_{1}>0$ depending on the volume of the ball of radius $\rho$ and on a bound on the curvature at this scale such that at any point at distance $\rho$ from the center of the annulus, the injectivity radius is bounded below by $r_{1} \rho$. Since the curvature is bounded, there also exists $0<r_{0}<r_{1}$ depending on $r_{1}$ and the bound on the curvature such that the harmonic radius is bounded below by $r_{0} \rho$. \(\square\)

\subsection*{2.2 Construction of the first coordinates}

Let us start by constructing first coordinates which we will improve later.
The crucial tool to prove this result is the almost volume cone theorem of Cheeger and Colding.

Lemma 2.4 ([CC96, Theorem 4.85]) For all $\delta>0$, there exists $\kappa>0$ such that for any $r>0$, if $\left(M^{n}, g\right)$ satisfies, $\operatorname{Ric}(g) \geqslant-(n-1) \kappa r^{-2}$ and there exists a point $p \in M$ at which,
$$\frac{\operatorname{Vol}(B(p, \kappa r))}{v_{-\kappa r^{-2}}(\kappa r)}-\frac{\operatorname{Vol}(B(p, 2 r))}{v_{-\kappa r^{-2}}(2 r)}<\kappa,$$
where $v_{-\kappa r^{-2}}(s)$ is the volume of the ball of radius $s$ in the simply connected space with sectional curvatures constant equal to $-\kappa r^{-2}$, then, there exists a metric cone $\left(C(X), d_{C(X)}, 0\right)$ such that $\operatorname{diam}(X) \leqslant \pi$ and,
$$d_{G H}\left((B(p, r), p),\left(B_{C(X)}(0, r), 0\right)\right) \leq \delta r .$$
We can refine this result in the case of 4-dimensional Einstein manifolds.

Lemma 2.5 (Almost volume cone in a 4-dimensional Einstein manifold) For all $\delta>0, l \in \mathbb{N}, v_{0}>0$, and $E>0$, there exists $\kappa>0$ such that for all $r>0$, if $\left(M^{4}, g\right)$ satisfies $\operatorname{Ric}(g)=\Lambda g$ with, $|\Lambda| \leqslant 3 \kappa r^{-2}$ and if there exists a point $p \in M$ for which,
$$\begin{gathered}
\operatorname{Vol}(B(p, r)) \geqslant v_{0} r^{4}, \\
\frac{\operatorname{Vol}(B(p, \kappa r))}{v_{-\kappa r^{-2}}(\kappa r)}-\frac{\operatorname{Vol}(B(2 r))}{v_{-\kappa r^{-2}}(2 r)}<\kappa,
\end{gathered}$$
and
$$\int_{B(p, 2 r)}|\operatorname{Rm}|^{2} d v \leqslant E,$$
then, there exists a finite subgroup $\Gamma \subset \operatorname{SO}(4)$ (with order bounded in terms of $v_{0}$ ), and a diffeomorphism $\Phi: A_{e}(\delta,(1-\delta)) \rightarrow \hat{A}(\delta r,(1-\delta) r)$, where,
$$A(2 \delta r,(1-2 \delta) r) \subset \hat{A}(\delta r,(1-\delta) r) \subset A\left(\frac{1}{2} \delta r,\left(1-\frac{1}{2} \delta\right) r\right)$$
such that on the annulus $A_{e}(\delta r,(1-\delta) r)$, we have:
$$\left\|\frac{\Phi^{*} g}{r^{2}}-g_{e}\right\|_{C^{l}\left(g_{e}\right)} \leqslant \delta$$

Remark 6 The assumptions on the Riemannian curvature and the volume are there to bound the order of $\Gamma$. They prevent our Einstein manifolds to be too close to $\mathbb{R}^{4} / \Gamma_{i}$ where the order of $\Gamma_{i}$ goes to infinity. In such a situation, the sequence could converge to the cone $\mathbb{R}^{+}$. These hypotheses are moreover redundant by [CN15, Theorem 1.13], the hypotheses on the Ricci curvature and the volume imply a bound on the $L^{2}$-norm of the curvature.

Proof By rescaling we can restrict our attention to $r=1$ and assume towards a contradiction that there exist $\delta>0, E>0$ and $v_{0}>0$, and a sequence of counterexamples $\left(M_{i}^{4}, g_{i}, p_{i}\right)$ satisfying
\begin{itemize}
\item[-] $\operatorname{Vol}\left(B_{i}\left(p_{i}, 1\right)\right)>v_{0}>0$,
\item[-] $\int_{B_{i}\left(p_{i}, 2\right)}\left|\operatorname{Rm}_{i}\right|^{2} \mathrm{~d} v_{i} \leqslant E$,
\item[-] there exists $\kappa_{i} \rightarrow 0$ and $\Lambda_{i},\left|\Lambda_{i}\right| \leqslant 3 \kappa_{i}$ for which $\operatorname{Ric}\left(g_{i}\right)=\Lambda_{i} g_{i}$ and $\frac{\operatorname{Vol}\left(B_{i}\left(p_{i}, \kappa_{i}\right)\right)}{v_{-\kappa_{i}}\left(\kappa_{i}\right)}-\frac{\operatorname{Vol}\left(B_{i}\left(p_{i}, 2\right)\right)}{v_{-\kappa_{i}}(2)}<\kappa_{i}$,
\end{itemize}
but such that for any $\Gamma$ finite subgroup of $S O(4)$, there does not exist a diffeomorphism $\Phi: A_{e}(\delta,(1-\delta)) \rightarrow \hat{A}(\delta r,(1-\delta) r)$ where $\hat{A}(\delta r,(1-\delta) r)$ satisfies (4), and such that we have the control (5).

Since $\operatorname{Vol}\left(B_{i}\left(p_{i}, 1\right)\right)>v_{0}>0$ and $\operatorname{Ric}\left(g_{i}\right) \geqslant-3 g_{i}$, a subsequence of the balls $B_{i}\left(p_{i}, 1\right)$ converges to a metric space ( $Y, d_{Y}, p$ ) in the Gromov-Hausdorff sense. By Lemma 2.4, up to taking a subsequence, for all $i$, we can assume that $\kappa_{i}$ is small enough to have
$$d_{G H}\left(\left(B_{i}(p, 1), p_{i}\right),\left(B_{C\left(X_{i}\right)}(0,1), 0\right)\right) \leqslant \frac{1}{i},$$
for a particular metric cone $\left(C\left(X_{i}\right), d_{C\left(X_{i}\right)}, 0\right)$ with $\operatorname{diam}\left(X_{i}\right) \leqslant \pi$. By the triangular inequality, the sequence $\left(B_{C\left(X_{i}\right)}(0,1), 0\right)$ also converges to $\left(Y, d_{Y}, p\right)$ in the Gromov-Hausdorff sense. Now, since the $C\left(X_{i}\right)$ with the distances $d_{C\left(X_{i}\right)}((r, x),(s, y)):=$ $\sqrt{r^{2}+s^{2}-2 r s \cos \left(d_{X_{i}}(x, y)\right)}$ converge, we deduce by fixing $r$ and $s$ that the $\left(X_{i}, d_{X_{i}}\right)$ converge to $\left(X, d_{X}\right)$, and therefore that the limit is a metric cone, $\left(Y, d_{Y}, p\right)=$ $\left(C(X), d_{C(X)}, 0\right)$.

By the compactness theorem for noncollapsed Einstein metrics with bounded $L^{2}$-norm for the curvature [BKN89, And89], $\left(Y, d_{Y}, p\right)$ is an Einstein orbifold. The limit of $\left(B_{i}\left(p_{i}, 1\right), g_{i}, p_{i}\right)$ in the Gromov-Hausdorff sense is therefore both the radius 1 ball of a metric cone and of an Einstein orbifold of dimension 4. Since an Einstein orbifold has bounded curvature, the cone has to be flat. The limit is therefore $\mathbb{R}^{4} / \Gamma_{\infty}$ for $\Gamma_{\infty}$ a finite subgroup of $S O(4)$.

Now, the convergence of Einstein metrics is smooth on compact subsets of the complement of the singularities by [BKN89], and there is only one here at the singular point of $\mathbb{R}^{4} / \Gamma_{\infty}$, hence, there exists a diffeomorphism $\Phi: A_{e}(\delta,(1-\delta)) \rightarrow \hat{A}(\delta r,(1-\delta) r)$ satisfying (4) and (5), which is a contradiction. \(\square\)

We can now use these results to construct some coordinates in our annulus.

Proof of Proposition 2 Let $\delta>0, D_{0}>0, v_{0}>0, E>0, \Lambda \in[-3,3]$ and $l \in \mathbb{N}$, and a 4-dimensional manifold, $(M, g)$ satisfiying :
\begin{itemize}
\item[-] $\operatorname{Ric}(g)=\Lambda g$,
\item[-] the diameter is bounded by $D_{0}>0$,
\item[-] the volume is bounded below by $v_{0}>0$,
\item[-] there exists $p \in M$, and $\rho_{2}>0$, such that we have : $\int_{B\left(p, \rho_{2}\right)}|\operatorname{Rm}|^{2} \leqslant E$.
\end{itemize}
Let us first remark that these imply a control on $\Lambda \rho_{2}^{2}$ by Bishop-Gromov inequality
$$\begin{aligned}
E & \geqslant \int_{B\left(\rho_{2}\right)}|\operatorname{Rm}|^{2} \mathrm{~d} v \\
& \geqslant 6 \int_{B\left(\rho_{2}\right)}|\operatorname{Ric}|^{2} \mathrm{~d} v \\
& \geqslant 24 \Lambda^{2} \operatorname{Vol}\left(B\left(\rho_{2}\right)\right) \\
& \geqslant 24 v_{0} \Lambda^{2} \frac{\operatorname{Vol}_{g_{-|\Lambda|}}\left(B_{g_{-|\Lambda|}}\left(\rho_{2}\right)\right)}{\operatorname{Vol}_{g_{-|\Lambda|}}\left(B_{g_{-|\Lambda|}}\left(D_{0}\right)\right)} \\
& \geqslant 24 v_{0} \Lambda^{2} \frac{\operatorname{Vol}_{g_{-3}}\left(B_{g_{-3}}\left(\rho_{2}\right)\right)}{\operatorname{Vol}_{g-3}\left(B_{g-3}\left(D_{0}\right)\right)} \\
& \geqslant C\left(D_{0}, v_{0}\right) \Lambda^{2} \rho_{2}^{4}
\end{aligned}$$
hence $\Lambda \rho_{2}^{2} \leqslant \frac{E^{1 / 2}}{C\left(D_{0}, v_{0}\right)^{1 / 2}}=: C^{\prime}\left(E, D_{0}, v_{0}\right)$.
Let $l \in \mathbb{N}$, and denote $0<\kappa_{0}<\frac{1}{4}$ the constant of Lemma 2.5 associated to our constants $\delta, l$ et $E$. We are looking for $\epsilon_{2}>0$ small enough to satisfy the hypotheses of Lemma 2.5 with constant $\kappa_{0}>0$.

For any $0<4 \rho_{1} \leq \rho_{2}$ for which we have :
$$\int_{A\left(\rho_{1}, \rho_{2}\right)}|\mathrm{Rm}|^{2} \leqslant \epsilon_{2}^{2}$$
and
$$\left|\frac{\operatorname{Vol}\left(B\left(\rho_{2}\right)\right)}{\operatorname{Vol}\left(B\left(\epsilon_{2} \rho_{1}\right)\right)}-\frac{\rho_{2}^{4}}{\left(\epsilon_{2} \rho_{1}\right)^{4}}\right| \leqslant \epsilon_{2},$$
we actually have, thanks to Bishop-Gromov inequality, for $C^{\prime \prime}\left(E, D_{0}, v_{0}\right)>0$,
$$\left|\frac{\operatorname{Vol}\left(B\left(\rho_{2}\right)\right)}{\operatorname{Vol}\left(B\left(\rho_{1}\right)\right)}-\frac{\rho_{2}^{4}}{\rho_{1}^{4}}\right| \leqslant C^{\prime \prime}\left(E, D_{0}, v_{0}\right) \epsilon_{2},$$
and for any $\rho$ and $\kappa_{0}>0$ for which $\rho_{1}<\kappa_{0} \rho<2 \rho<\rho_{2}$,
$$\left|\frac{\operatorname{Vol}(B(2 \rho))}{\operatorname{Vol}\left(B\left(\kappa_{0} \rho\right)\right)}-\frac{(2 \rho)^{4}}{\left(\kappa_{0} \rho\right)^{4}}\right| \leqslant C^{\prime \prime}\left(E, D_{0}, v_{0}\right) \epsilon_{2} .$$

We can therefore assume that $\operatorname{Vol}\left(A\left(\rho_{1}, \rho_{2}\right)\right) \geqslant c\left(E, D_{0}, v_{0}\right) \rho_{2}^{4}$ for $4 \rho_{1}<\rho_{2}$ and $c\left(E, D_{0}, v_{0}\right)>0$ by choosing $\epsilon_{2}$ small enough. Let us then look for a bound on $\Lambda$ in order to verify the assumptions of Lemma 2.5. Since Ric $=\Lambda g$, we have
$$\begin{aligned}
\epsilon_{2}^{2} & \geqslant \int_{A\left(\rho_{1}, \rho_{2}\right)}|\operatorname{Rm}|^{2} \mathrm{~d} v \\
& \geqslant 6 \int_{A\left(\rho_{1}, \rho_{2}\right)}|\operatorname{Ric}|^{2} \mathrm{~d} v \\
& \geqslant 24 \Lambda^{2} \operatorname{Vol}\left(A\left(\rho_{1}, \rho_{2}\right)\right) \\
& \geqslant 24 c\left(E, D_{0}, v_{0}\right) \Lambda^{2} \rho_{2}^{4}
\end{aligned}$$
which rewrites $|\Lambda| \leqslant \epsilon_{2}\left(24 c\left(E, D_{0}, v_{0}\right)\right)^{-1 / 2} \rho_{2}^{-2}$. Therefore, for $\epsilon_{2}$ small enough, we verify the assumptions of Lemma 2.5 for any $\rho$ by choosing $\epsilon_{2}$ for which we have
$$\kappa_{0}=\epsilon_{2} \max \left(\left(24 c\left(E, D_{0}, v_{0}\right)\right)^{-1 / 2}, 1, C^{\prime \prime}\left(E, D_{0}, v_{0}\right)\right),$$
because we control the volume growth between $\kappa_{0} \rho$ and $2 \rho$ thanks to (8). The conclusion of Proposition 2 therefore holds for any $\rho_{1}<\rho<\frac{1}{4} \rho_{2}$ with $\delta\left(\kappa_{0}\right)>0$. \(\square\)

\subsection*{2.3 Consequences of the existence of the first coordinates.}

The diffeomorphism of Proposition 2 allows us to pull back our Einstein metric on a flat annulus $A_{e}\left(\rho_{1}, \rho_{2}\right) \subset \mathbb{R}^{4} / \Gamma$, where the Einstein metric $g$ is $C^{\infty}$-close to the flat metric $g_{e}$. This will let us construct hypersurfaces of almost constant second fundamental form for our Einstein metric.

Remark 7 Here and in the following, we will use the convention that our normal vectors point outwards, and we define the second fundamental form as
$$A^{\Sigma}(X, Y):=\left\langle X, \nabla_{Y} N^{\Sigma}\right\rangle,$$
which ensures that spheres in the Euclidean space have positive second fundamental form.

Lemma 2.6 For any $l \in \mathbb{N}$, there exists $C>0$ and $\delta_{0}>0$ such that if a metric $g$ on $A_{e}\left(\frac{1}{4}, 4\right)$ satisfies,
$$\left\|g-g_{e}\right\|_{C^{l+1}\left(A_{e}\left(\frac{1}{4}, 4\right)\right)} \leqslant \delta_{0},$$
we have, for all $s \in\left[\frac{1}{4}, 4\right]$, the sphere of radius $s$ of $\mathbb{R}^{n} / \Gamma, \mathcal{S}_{s}$, has a second fundamental form for $g, A_{g}^{\mathcal{S}_{s}}$, which satisfies
$$\left\|\frac{A_{g}^{\mathcal{S}_{s}}}{s}-\frac{g^{\mathcal{S}_{s}}}{s^{2}}\right\|_{C^{l}\left(\frac{g^{\mathcal{S}}}{s^{2}}\right)} \leqslant C\left\|g-g_{e}\right\|_{C^{l+1}\left(A_{e}\left(\frac{1}{4}, 4\right)\right)} .$$

We moreover have
$$\left\|\frac{g^{\mathcal{S}_{s}}}{s^{2}}-g^{\mathbb{S}^{n-1} / \Gamma}\right\|_{C^{l+1}\left(g^{\mathbb{S}^{n-1} / \Gamma}\right)} \leqslant C\left\|g-g_{e}\right\|_{C^{l+1}\left(A_{e}\left(\frac{1}{4}, 4\right)\right)}$$

Proof The second fundamental form involves one derivative of the metric which is controlled in $C^{l+1}$-norm by assumption. Since for $g_{e}$, the hypersurfaces $\mathcal{S}_{s}$ have a second fundamental form constant equal to $\frac{g^{s^{n-1} / \Gamma}}{s^{2}}$, we conclude that we indeed control their second fundamental form
$$\left\|\frac{A_{g}^{\mathcal{S}_{s}}}{s}-\frac{g^{\mathcal{S}_{s}}}{s^{2}}\right\|_{C^{l}\left(\frac{g^{\mathcal{S}_{s}}}{s^{2}}\right)} \leqslant C\left\|g-g_{e}\right\|_{C^{l+1}\left(A_{e}\left(\frac{1}{4}, 4\right)\right)} .$$
In a similar fashion, we get the control on the metric. \(\square\)

Given a smooth and orientable hypersurface, $\Sigma$, we define for $x \in \Sigma$ and $s \in \mathbb{R}$, $F^{g}(x, s):=\gamma_{x}^{g}(s)$, where $\gamma_{x}^{g}$ is the geodesic for $g$ such that $\gamma_{x}^{g}(0)=x$, and $\gamma_{x}^{\prime g}(0)$ is the normal to $\Sigma$ at $x$. We define the normal injectivity radius of $\Sigma$, denoted $\operatorname{inj}_{g}^{\perp}(\Sigma)$ as the supremum of the constants $r>0$ for which the map $F^{g}: \Sigma \times[-r, r] \rightarrow M$ is a diffeomorphism on its image.

Lemma 2.7 For all $l \in \mathbb{N}$ and $\epsilon>0$, there exists $C>0$ and $\delta>0$ such that if a metric $g$ satisfies $\left\|g-g_{e}\right\|_{C^{l+2}\left(A_{e}\left(\frac{1}{4}, 4\right)\right)} \leqslant \delta$, then for any hypersurface $\Sigma \subset A_{e}\left(\frac{1}{2}, 2\right)$ satisfying $\left\|A_{g_{e}}^{\Sigma}\right\|_{C^{l+1}} \leqslant 10$, we have the two following properties:
\begin{itemize}
\item[-] the normal injectivity radii of $\Sigma$ for $g \operatorname{inj}_{g}^{\perp}(\Sigma)$, and $g_{e}, \operatorname{inj}_{g_{e}}^{\perp}(\Sigma)$ satisfy
$$\left|\frac{\operatorname{inj}_{g}^{\perp}(\Sigma)}{\operatorname{inj}_{g_{e}}^{\perp}(\Sigma)}-1\right| \leqslant \epsilon$$
\item[-] the two normal exponential maps are also close to each other on the set
$$\Sigma \times\left[-(1-\epsilon) \operatorname{inj}_{g_{e}}^{\perp}(\Sigma),(1-\epsilon) \operatorname{inj}_{g_{e}}^{\perp}(\Sigma)\right]:$$
there exists a vector field $X$ on $\mathbb{R}^{n} / \Gamma,\|X\|_{C^{l+1}\left(g_{e}\right)}<\epsilon$, for which we have,
$$F^{g} \circ\left(F^{g_{e}}\right)^{-1}=\phi_{X},$$
where $\phi_{X}: p \mapsto \exp _{p}^{g_{e}}(X(p))$.
\end{itemize}

Proof The curves $F^{g}(x,)=.\gamma_{x}^{g}($.$) and F^{g_{e}}(x,)=.\gamma_{x}^{g_{e}}($.$) are respectively the solutions$ of the geodesic equation for $g$ and $g_{e}$,
$$\left\{\begin{array}{l}
\nabla_{\gamma_{x}^{\prime}} \gamma_{x}^{\prime}=0 \\
\gamma_{x}(0)=x \\
\gamma_{x}^{\prime}(0)=N_{x} .
\end{array}\right.$$
where $N_{x}^{g}$ and $N_{x}^{g_{e}}$ are the outwards normal to $\Sigma$ for the two metrics. By assumption, the metrics $g$ and $g_{e}$ are $C^{l+2}$-close. This implies that $N_{x}^{g}$ and $N_{x}^{g_{e}}$ are $C^{l+2}$-close, and that $\nabla^{g}$ and $\nabla^{g_{e}}$ are $C^{l+1}$-close.

By continuity with respect to the initial conditions and parameters of order 2 differential equations, given a fixed hypersurface $\Sigma$, for all $\epsilon>0$, there exists $\delta>0$ such that if $\left\|g-g_{e}\right\|_{C^{l+2}} \leqslant \delta$, then, the difference between the normal geodesics is small in the following $C^{l}$-sense since we work in local charts. There exists a vector field $X$ defined along each $\gamma_{x}^{g_{e}}$ such that
$$\gamma_{x}^{g}(s)=\phi_{X}\left(\gamma_{x}^{g_{e}}(s)\right):=\exp _{\gamma_{x}^{g_{e}}(s)}\left(X\left(\gamma_{x}^{g_{e}}(s)\right)\right),$$
and $\|X\|_{C^{l+1}\left(g_{e}\right)}<\epsilon$. Hence, the equality $\gamma_{x}^{g}(s)=\phi_{X}\left(\gamma_{x}^{g_{e}}(s)\right)$ rewrites:
$$F^{g}=\phi_{X} \circ F^{g_{e}}$$ \(\square\)

In particular, we deduce that if a hypersurface $\Sigma^{\prime}$ is a small normal perturbation of $\Sigma$ for the metric $g$, then, it is also a small normal perturbation of $\Sigma$ for the metric $g_{e}$, and conversely.

Corollary 1 For all $\epsilon_{0} l \in \mathbb{N}$, there exists $C>0$ and $\delta_{0}>0$, such that for any metric $g$ satisfying,
$$\left\|g-g_{e}\right\|_{C^{l+2}\left(A_{e}\left(\frac{1}{4}, 4\right)\right)} \leqslant \delta_{0},$$
and for any hypersurface $\Sigma \subset A_{e}\left(\frac{1}{2}, 2\right)$ satisfying $\left\|A_{g_{e}}^{\Sigma}\right\|_{C^{l+1}} \leqslant 10$, we have: for any function $w: \Sigma \rightarrow \mathbb{R}$ with $\|w\|_{C^{l}} \leqslant \epsilon_{0}$, and denoting $\Sigma(w):=\{F(x, w(x)), x \in \Sigma\}$,
\begin{itemize}
\item[(1)] there exists $w^{\prime}: \Sigma \rightarrow \mathbb{R}$ with $\left\|w^{\prime}\right\|_{C^{l}} \leqslant 2 \epsilon_{0}$ such that
$$\Sigma_{g_{e}}(w)=\Sigma_{g}\left(w^{\prime}\right),$$
\item[(2)] there exists $w^{\prime \prime}: \Sigma \rightarrow \mathbb{R}$ with $\left\|w^{\prime \prime}\right\|_{C^{l}} \leqslant 2 \epsilon_{0}$ such that
$$\Sigma_{g}(w)=\Sigma_{g_{e}}\left(w^{\prime \prime}\right) .$$
\end{itemize}

Proof According to Lemma 2.7, we have $F^{g}=\phi_{X} \circ F^{g_{e}}$, where $X$ is arbitrarily small in $C^{l+1}$-norm for $\delta_{0}$ arbitrarily small. Adding the assumption $\left\|A_{g_{e}}^{\Sigma}\right\|_{C^{l+1}} \leqslant 10$, ensures that for $\epsilon_{0}>0$, the metrics $g_{e}:=\left(F^{g_{e}}\right)^{*} g_{e}$ and $g_{p}:=\left(g_{e}\right)_{\mid \Sigma}+d s^{2}$ on $\Sigma \times\left[-2 \epsilon_{0}, 2 \epsilon_{0}\right]$, are arbitrarily close in $C^{l}$-norm for $\epsilon_{0}$ arbitrarily small. This implies that
$$\left[\left(F^{g_{e}}\right)^{-1} \circ \phi_{X} \circ F^{g_{e}}\right]=\phi_{X^{e}}^{e}$$
where $X^{e}$ is the pull-back of $X$ by $F^{g_{e}}$, and $\phi_{X^{e}}^{e}(p):=\exp _{p}^{g_{e}}\left(X^{e}(p)\right)$. Hence, we have $\left\|X^{e}\right\|_{C^{l+1}\left(g_{e}\right)} \leqslant \epsilon_{0}$ by the proximity of the metrics $g_{e}$ and $g_{p}, \phi_{X^{e}}^{e}=\left(\phi_{X_{\Sigma}^{p}}^{\Sigma}, \phi_{X_{\mathbb{R}}^{p}}^{\mathbb{R}}\right)$, where $\left\|X_{\Sigma}^{p}\right\|_{C^{l}\left(g^{\Sigma}\right)}+\left\|X_{\mathbb{R}}^{p}\right\|_{C^{l}\left(d s^{2}\right)} \leqslant 2 \epsilon_{0}$.
Now, for all $(x, s) \in \Sigma \times\left[-2 \epsilon_{0}, 2 \epsilon_{0}\right]$, we have
$$\begin{aligned}
F^{g}(x, s) & =F^{g_{e}} \circ\left[\left(F^{g_{e}}\right)^{-1} \circ \phi_{X} \circ F^{g_{e}}\right](x, s), \\
& =F^{g_{e}} \circ\left(\phi_{X_{\Sigma}^{p}}^{\Sigma}, \phi_{X_{\mathbb{R}}^{p}}^{\mathbb{R}}\right)(x, s) \\
& =F^{g_{e}}\left(\phi_{X_{\Sigma}^{p}}^{\Sigma}(x), \phi_{X_{\mathbb{R}}^{p}}^{\mathbb{R}}(s)\right) .
\end{aligned}$$
In particular, for all $w: \Sigma \rightarrow\left[-2 \epsilon_{0}, 2 \epsilon_{0}\right]$, we have
$$F^{g}(x, w(x))=\left(\phi_{X_{\Sigma}^{p}}^{\Sigma}(x), w^{\prime}\left(\phi_{X_{\Sigma}^{p}}^{\Sigma}(x)\right)\right),$$
where $w^{\prime}:=\phi_{X_{\mathbb{R}}^{p}}^{\mathbb{R}} \circ w \circ\left(\phi_{X_{\Sigma}^{p}}^{\Sigma}\right)^{-1}$. By the controls of $X_{\mathbb{R}}^{p}$ and $X_{\Sigma}^{p}$ which we can assume as small as wanted by choosing $\delta_{0}$ and $\epsilon_{0}$ small enough, we get the stated result. \(\square\)

\section*{3 Controls on constant mean curvature hypersurfaces in low curvature regions}

Let us motivate the use of constant mean curvature hypersurfaces. We control both the way they are embedded in our manifold and their intrinsic geometry thanks to the ambient curvature which we will control in our neck regions by [Ban90, Proposition 3].

Remark 8 All along this section, we will denote constant mean curvature hypersurfaces with a tilde to insist on their particularity.

Proposition 3 For all $k \in \mathbb{N}$ and $0<\alpha<1$, there exists $\epsilon>0$ and $C>0$ for which, if $\tilde{\Sigma}$ is a hypersurface of a manifold $\left(M^{n}, g\right)$ satisfying:
\begin{itemize}
\item[(1)] its mean curvature is constant equal to $n-1$,
\item[(2)] there exists $\Gamma$ a finite subgroup of $S O(n)$, and a diffeomorphism $\Phi: \mathbb{S}^{n-1} /$ $\Gamma \rightarrow \tilde{\Sigma}$ such that we have
$$\left\|\Phi^{*} g^{\tilde{\Sigma}}-g^{\mathbb{S}^{n-1} / \Gamma}\right\|_{C^{1, \alpha}\left(\mathbb{S}^{n-1} / \Gamma\right)} \leqslant \epsilon .$$
\item[(3)] the ambient curvature is small on $\tilde{\Sigma}$,
$$\|\operatorname{Rm}(g)\|_{C^{k}(g)} \leqslant \epsilon,$$
\end{itemize}
then:
\begin{itemize}
\item[-] the second fundamental form is almost constant at the scale of curvature,
$$\left\|A^{\tilde{\Sigma}}-g^{\tilde{\Sigma}}\right\|_{C^{k, \alpha}\left(g^{\tilde{\Sigma}}\right)} \leqslant C\|\operatorname{Rm}(g)\|_{C^{k}(g)},$$
\item[-] there exists a diffeomorphism $\Psi: \mathbb{S}^{n-1} / \Gamma \rightarrow \tilde{\Sigma}$ such that,
$$\left\|\Psi^{*} g^{\tilde{\Sigma}}-g^{\mathbb{S}^{n-1} / \Gamma}\right\|_{C^{k+1, \alpha}\left(\mathbb{S}^{n-1} / \Gamma\right)} \leqslant C\|\operatorname{Rm}(g)\|_{C^{k}(g)} .$$
\end{itemize}
Let us precise the notations we will use for this proof:
\begin{itemize}
\item[-] $\nabla^{\tilde{\Sigma}}$ : the Levi-Civita connection of the hypersurface,
\item[-] $\nabla$ : the Levi-Civita connection of the ambient space,
\item[-] $N^{\tilde{\Sigma}}$ : the outwards normal to the hypersurface,
\item[-] $A^{\tilde{\Sigma}}(X, Y):=\left\langle X, \nabla_{Y} N^{\tilde{\Sigma}}\right\rangle$ : the second fundamental form of the hypersurface which will be seen as a symmetric 2-tensor of the tangent space to $\tilde{\Sigma}$,
\item[-] $H^{\tilde{\Sigma}}$ : the mean curvature of the hypersurface,
\item[-] for $B$ a 1 -form on $\tilde{\Sigma}$ taking values in $T^{*} \tilde{\Sigma}$, we define
$$\left(d^{\nabla^{\tilde{\Sigma}}} B\right)(X, Y):=\nabla_{X}^{\tilde{\Sigma}} B(Y, .)-\nabla_{Y}^{\tilde{\Sigma}} B(X, .),$$
\item[-] we will denote $\delta^{\nabla^{\tilde{\Sigma}}}$ the formal adjoint of $d^{\nabla^{\tilde{\Sigma}}}$.
\end{itemize}
We have the following classical formulas (see for instance [Pet98, Chapter 4]) for the second formula for any hypersurface $\Sigma$ : for all vector fields $X, Y, Z$ on $\Sigma$,
$$d^{\nabla^{\Sigma}} A^{\Sigma}(X, Y, Z)=g\left(\operatorname{Rm}(X, Y) N^{\Sigma}, Z\right),$$
and
$$\delta^{\nabla^{\Sigma}} A^{\Sigma}(X)=\operatorname{Ric}\left(N^{\Sigma}, X\right)-d H(X) .$$
Denoting $A_{0}^{\tilde{\Sigma}}$ the trace-free part of $A^{\tilde{\Sigma}}$ for $g^{\tilde{\Sigma}}$, if $\tilde{\Sigma}$ is a constant mean curvature hypersurface, by the above formulas, we even have
$$d^{\nabla^{\tilde{\Sigma}}} A_{0}^{\tilde{\Sigma}}(X, Y, Z)=g\left(\operatorname{Rm}(X, Y) N^{\tilde{\Sigma}}, Z\right),$$
and
$$\delta^{\nabla^{\tilde{\Sigma}}} A_{0}^{\tilde{\Sigma}}(X)=\operatorname{Ric}\left(N^{\tilde{\Sigma}}, X\right) .$$
The right hand sides being well controlled, we control $A_{0}^{\tilde{\Sigma}}$ by noticing that the operator $d^{\nabla^{\tilde{\Sigma}}}+\delta^{\nabla^{\tilde{\Sigma}}}$ is elliptic.

Lemma 3.1 The operator $d^{\nabla^{\tilde{\Sigma}}}+\delta^{\nabla^{\tilde{\Sigma}}}$ acting on symmetric 2-tensors is elliptic. Moreover, for any metric $g$ sufficiently $C^{0}$-close to $g^{\mathbb{S}^{n-1}}$, the operator $d^{\nabla^{\mathbb{S}^{n-1}}}+\delta^{\nabla^{\mathbb{S}^{n-1}}}$ is injective on the symmetric 2-tensors which are traceless for $g$.

Proof It is well-known that the operator $d^{\nabla}+\delta^{\nabla}$ is elliptic. According to [Bes87, 12.69], the associated Laplacian: $-\hat{\Delta}:=\delta^{\nabla} d^{\nabla}+d^{\nabla} \delta^{\nabla}$ takes the following form for a symmetric 2-tensor $h$,
$$-\hat{\Delta}^{\tilde{\Sigma}} h=\left(\nabla^{\tilde{\Sigma}}\right)^{*} \nabla^{\tilde{\Sigma}} h-\mathrm{R}^{\tilde{\Sigma}} h+h \circ \operatorname{Ric}^{\tilde{\Sigma}},$$
where $\stackrel{\circ}{\mathrm{R}}$ is the action of curvature on symmetric 2-tensors: for an orthonormal basis $\left(e_{i}\right)_{i}$,
$$\stackrel{\circ}{\mathrm{R}}(h)(X, Y)=\sum_{i} h\left(\operatorname{Rm}\left(e_{i}, X\right) Y, e_{i}\right),$$
or $\stackrel{\circ}{\mathrm{R}}(h)_{i j}:=\mathrm{Rm}_{i k l j} h_{m n} g^{k m} g^{l n}$ in local coordinates. Hence, on the unit sphere of dimension $n-1$, we have $\operatorname{Rm}_{i k l j}^{\mathbb{S}^{n-1}}=g_{i j} g_{k l}-g_{i l} g_{k j}$, and therefore $\stackrel{\circ}{\mathrm{R}}^{\mathbb{S}^{n-1}}(h)_{i j}=$ $\operatorname{tr}(h) g_{i j}-h_{i j}$, and $\alpha \circ \operatorname{Ric}^{\mathbb{S}^{n-1}}=(n-2) \alpha$. This gives
$$-\hat{\Delta}^{\mathbb{S}^{n-1}} h=\left(\nabla^{\mathbb{S}^{n-1}}\right)^{*} \nabla^{\mathbb{S}^{n-1}} h+(n-1) h-\operatorname{tr}(h) \mathrm{Id} .$$
Let $h_{0}$ be a $C^{1, \alpha}\left(\mathbb{S}^{n-1}\right)$ symmetric 2-tensor whose trace for $g^{\mathbb{S}^{n-1}}$ vanishes and which is in the kernel of the operator. The trace of $h_{0}$ vanishes so we have,
$$\left(\nabla^{\mathbb{S}^{n-1}}\right)^{*} \nabla^{\mathbb{S}^{n-1}} h_{0}+(n-1) h_{0}=0 .$$
Integrating by parts against $h_{0}$ yields
$$\left\|\nabla h_{0}\right\|_{L^{2}}^{2}+(n-1)\left\|h_{0}\right\|_{L^{2}}^{2}=0,$$
and finally $h_{0}=0$. The operator $d^{\nabla^{\mathbb{S}^{n-1}}}+\delta^{\nabla^{\mathbb{S}^{n-1}}}$ is therefore injective on symmetric 2-tensors whose trace for $g^{\mathbb{S}^{n-1}}$ vanishes.

Let us now consider a metric $g$ close to $g^{\mathbb{S}^{n-1}}$, that is, assume that there exists $\epsilon>0$ which we will choose small enough such that
$$\left\|g-g^{\mathbb{S}^{n-1}}\right\|_{C^{0}\left(\mathbb{S}^{n-1}\right)} \leq \epsilon$$
We want to show that the operator $d^{\nabla^{\mathbb{S}^{n-1}}}+\delta^{\nabla^{\mathbb{S}^{n-1}}}$ is also invertible on tensors whose trace vanishes for $g$. Let $h$ be a symmetric 2-tensor which is traceless for $g$. By proximity of the metrics, for $\epsilon$ small enough, there exists $C=C(n)$ for which
$$\left|t r^{\mathbb{S}^{n-1}} h\right|_{\mathbb{S}^{n-1}} \leqslant C \epsilon|h|_{\mathbb{S}^{n-1}} .$$

We still have
$$-\hat{\Delta}^{\mathbb{S}^{n-1}} h=\left(\nabla^{\mathbb{S}^{n-1}}\right)^{*} \nabla^{\mathbb{S}^{n-1}} h+(n-1) h-t r^{\mathbb{S}^{n-1}}(h) \mathrm{Id},$$
and thanks to (13), if $\left(d^{\nabla^{\mathbb{S}^{n-1}}}+\delta^{\nabla^{\mathbb{S}^{n-1}}}\right) h=0$, then
$$0 \geqslant\left\|\nabla^{\mathbb{S}^{n-1}} h\right\|^{2}+(n-1-C \epsilon)\|h\|^{2},$$
which gives $h=0$ if $\epsilon$ is small enough to have $n-1>C \epsilon$. We finally conclude that $d^{\nabla^{\mathbb{S}^{n-1}}}+\delta^{\nabla^{\mathbb{S}^{n-1}}}$ is injective on symmetric 2-tensors whose trace for $g$ vanishes. \(\square\)

Corollary 2 For any $1 \leqslant p<+\infty$ and $l \in \mathbb{N}$, there exists $\epsilon>0$ such that if $\Sigma$ is a hypersurface of a Riemannian manifold $\left(M^{n}, g\right)$ for which there exists $\Gamma$ a finite subgroup of $S O(n)$, and a diffeomorphism $\Phi: \mathbb{S}^{n-1} / \Gamma \rightarrow \tilde{\Sigma}$ such that we have
$$\left\|\Phi^{*} g^{\tilde{\Sigma}}-g^{\mathbb{S}^{n-1} / \Gamma}\right\|_{W^{l+1, p}\left(\mathbb{S}^{n-1} / \Gamma\right)} \leqslant \epsilon,$$
then, there exists $C>0$ such that for any symmetric 2-tensor $u$ on $\tilde{\Sigma}$ whose $g^{\tilde{\Sigma}}$-trace vanishes, we have,
$$\|u\|_{W^{l+1, p}\left(\mathbb{S}^{n-1} / \Gamma\right)} \leqslant C\left(\left\|\delta^{\nabla^{\tilde{\Sigma}}} u\right\|_{W^{l, p}\left(\mathbb{S}^{n-1} / \Gamma\right)}+\left\|d^{\nabla^{\tilde{\Sigma}}} u\right\|_{W^{l, p}\left(\mathbb{S}^{n-1} / \Gamma\right)}\right) .$$

Proof We have the following control: for all $p \geqslant 1$, there exists a constant $C>0$ such that for all symmetric 2-tensor $u$ on $\mathbb{S}^{n-1}$ we have
$$\left\|\Phi^{*}\left(d^{\nabla^{\tilde{\Sigma}}}+\delta^{\nabla^{\tilde{\Sigma}}}\right) u-\left(d^{\nabla^{\mathbb{S}^{n-1}}}+\delta^{\nabla^{\mathbb{S}^{n-1}}}\right) u\right\|_{L^{p}\left(\mathbb{S}^{n-1} / \Gamma\right)} \leqslant C \epsilon\|u\|_{W^{1, p}\left(\mathbb{S}^{n-1} / \Gamma\right)} .$$
The conclusion comes then from estimates for injective Fredholm operators which are consequences of the open mapping theorem between Banach spaces. \(\square\)

Proof of Proposition 3 Let $0<\alpha<1$, and $p>\frac{n}{1-\alpha}$. Then, $W^{1, p}\left(g^{\tilde{\Sigma}}\right)$ embeds continuously in $C^{\alpha}\left(g^{\tilde{\Sigma}}\right)$, which means that there exists $C_{1}=C_{1}(p, \alpha, n)>0$ such that for all symmetric 2-tensor $u$, we have:
$$\|u\|_{C^{\alpha}\left(g^{\tilde{\Sigma}}\right)} \leq C_{1}\|u\|_{W^{1, p}\left(g^{\tilde{\Sigma}}\right)} \cdot$$
Define on $\mathbb{S}^{n-1}$ the operators, $P:=\delta^{\nabla^{\mathbb{S}^{n-1}}}+d^{\nabla^{\mathbb{S}^{n-1}}}$ and $P^{\prime}:=\Phi^{*}\left(\delta^{\nabla^{\tilde{\Sigma}}}+d^{\nabla^{\tilde{\Sigma}}}\right)$ between the Banach spaces $W^{1, p}\left(\mathbb{S}^{n-1}\right)$ and $L^{p}\left(\mathbb{S}^{n-1}\right)$. According to Lemma 3.1, $P$ is
injective on traceless symmetric 2-tensors. Thanks to the expressions (10) and (11) of the operator $\delta^{\nabla}+d^{\nabla}$ applied to $A_{0}^{\tilde{\Sigma}}$, by Corollary 2, we have,
$$\begin{aligned}
\left\|A_{0}^{\tilde{\Sigma}}\right\|_{W^{1, p}\left(g^{\tilde{\Sigma}}\right)} & \leqslant C\left(\left\|\delta^{\nabla^{\tilde{\Sigma}}} A_{0}^{\tilde{\Sigma}}\right\|_{L^{p}\left(g^{\tilde{\Sigma}}\right)}+\left\|d^{\nabla^{\tilde{\Sigma}}} A_{0}^{\tilde{\Sigma}}\right\|_{L^{p}\left(g^{\tilde{\Sigma}}\right)}\right) \\
& =C\left(\left\|\operatorname{Rm}(., .) N^{\tilde{\Sigma}}\right\|_{L^{p}\left(g^{\tilde{\Sigma}}\right)}+\left\|\operatorname{Ric}\left(N^{\tilde{\Sigma}}\right)\right\|_{L^{p}\left(g^{\tilde{\Sigma}}\right)}\right)
\end{aligned}$$
Since the hypersurface has bounded volume (actually close to the volume of $\mathbb{S}^{n-1} / \Gamma$ ), there exists $C_{2}=C_{2}(p, n)>0$ such that we have
$$\left\|\operatorname{Ric}\left(N^{\tilde{\Sigma}}\right)\right\|_{L^{p}\left(g^{\tilde{\Sigma}}\right)} \leqslant C_{2}\left\|\operatorname{Rm}(., .) N^{\tilde{\Sigma}}\right\|_{C^{0}\left(g^{\tilde{\Sigma}}\right)},$$
and
$$\left\|\operatorname{Rm}(., .) N^{\tilde{\Sigma}}\right\|_{L^{p}\left(g^{\tilde{\Sigma}}\right)} \leqslant C_{2}\left\|\operatorname{Rm}(., .) N^{\tilde{\Sigma}}\right\|_{C^{0}\left(g^{\tilde{\Sigma}}\right)} .$$
Hence, by continuous embedding of $W^{1, p}\left(g^{\tilde{\Sigma}}\right)$ in $C^{\alpha}\left(g^{\tilde{\Sigma}}\right)$, we have
$$\left\|A_{0}^{\tilde{\Sigma}}\right\|_{C^{\alpha}\left(g^{\tilde{\Sigma}}\right)} \leqslant 2 C_{1} C_{2} C\left\|\operatorname{Rm}(., .) N^{\tilde{\Sigma}}\right\|_{C^{0}\left(g^{\tilde{\Sigma}}\right)}$$
which is the stated result for $k=0$.

Let us finally explain how to control the higher levels of regularity by a bootstrap argument once we have found optimal coordinates on our hypersurface $\tilde{\Sigma}$. Assume that we have the following controls for $l \in \mathbb{N}$, on the hypersurface $\tilde{\Sigma}$ : there exists $C>0$ such that,
\begin{itemize}
\item[(1)] $\|\operatorname{Rm}(g)\|_{C^{l+1}(g)} \leqslant \epsilon$,
\item[(2)]
$$\left\|A^{\tilde{\Sigma}}-g^{\tilde{\Sigma}}\right\|_{C^{l, \alpha}\left(g^{\tilde{\Sigma}}\right)} \leqslant C\|\operatorname{Rm}(g)\|_{C^{l}(g)},$$
\item[(3)] there exists a diffeomorphism $\Psi: \mathbb{S}^{n-1} / \Gamma \rightarrow \tilde{\Sigma}$ with
$$\left\|\Psi^{*} g^{\tilde{\Sigma}}-g^{\mathbb{S}^{n-1} / \Gamma}\right\|_{C^{l+1, \alpha}\left(\mathbb{S}^{n-1} / \Gamma\right)} \leqslant C\|\operatorname{Rm}(g)\|_{C^{l}(g)} .$$
\end{itemize}
Notice that at this point, we have proven the estimates for $l=0$. Gauss equation gives:
$$\begin{aligned}
g\left(\operatorname{Rm}^{\tilde{\Sigma}}(X, Y) Z, W\right)= & g(\operatorname{Rm}(X, Y) Z, W) \\
& +A^{\tilde{\Sigma}}(X, Z) A^{\tilde{\Sigma}}(Y, W)-A^{\tilde{\Sigma}}(Y, Z) A^{\tilde{\Sigma}}(X, W) .
\end{aligned}$$
And controls 1 and 2 above imply therefore that there exists $C=C(\alpha, l, n)>0$ which gives
$$\left\|\operatorname{Ric}\left(g^{\tilde{\Sigma}}\right)-(n-1) g^{\tilde{\Sigma}}\right\|_{C^{l, \alpha}\left(g^{\tilde{\Sigma}}\right)} \leqslant C\|\operatorname{Rm}(g)\|_{C^{l+1}(g)},$$
and we can use Proposition 4 proven in the appendix.

Proposition 4 Let $\left(M, g_{0}\right)$ be an $n$-dimensional manifold with sectional curvatures equal to 1 , and $k \in \mathbb{N}$. Then, there exists $\delta>0$ and $C>0$, such that if a metric $g$ on $M$ satisfies:
$$\left\|g-g_{0}\right\|_{C^{1, \alpha}\left(g_{0}\right)} \leqslant \delta$$
then, there exists a diffeomorphism $\Phi: M \rightarrow M$, such that we have,
$$\left\|\Phi^{*} g-g_{0}\right\|_{C^{k+1, \alpha}\left(g_{0}\right)} \leqslant C\|\operatorname{Ric}(g)-(n-1) g\|_{C^{k-1, \alpha}\left(g_{0}\right)} .$$
Hence, in our case, there exists a diffeomorphism (independent of $l$ ) $\tilde{\Psi}_{\tilde{\Sigma}}: \mathbb{S}^{n-1} / \Gamma \rightarrow \tilde{\Sigma}$ with
$$\left\|\tilde{\Psi}_{\tilde{\Sigma}}^{*} g^{\tilde{\Sigma}}-g^{\mathbb{S}^{n-1} / \Gamma}\right\|_{C^{l+2, \alpha}\left(\mathbb{S}^{n-1} / \Gamma\right)} \leqslant C\|\operatorname{Rm}(g)\|_{C^{l+1}(g)} .$$
This diffeomorphism combined to the controls in $C^{l+1}$-norm on the curvature imply by Corollary 2 (just like in the proof with $k=0$ ) that there exists a constant $C^{\prime}=$ $C^{\prime}(l+1, \alpha, n)>0$ such that
$$\left\|A^{\tilde{\Sigma}}-g^{\tilde{\Sigma}}\right\|_{C^{l+1, \alpha}\left(g^{\tilde{\Sigma}}\right)} \leqslant C^{\prime}\|\operatorname{Rm}(g)\|_{C^{l+1}(g)} .$$
We therefore have the property for $l+1$ and the control on the metric $\tilde{\Psi}_{\tilde{\Sigma}}^{*} g^{\tilde{\Sigma}}$ improves thanks to Proposition 4 and we can iterate this argument for all $l \leqslant k-1$. \(\square\)

\section*{4 Perturbation of hypersurfaces with almost constant second fundamental form}

During all of our construction, without loss of generality by rescaling, we will always reduce our construction to the case where the mean curvature is constant equal to $n-1$. Let us first show that we can perturb a hypersurface with almost constant second fundamental form to a constant mean curvature hypersurface.

Proposition 5 For all $n \in \mathbb{N}$ and $0<r_{0}<\frac{1}{6}$, there exists $C>0$ and $0<\epsilon<\frac{r_{0}}{C}$ such that for any hypersurface $\Sigma$ diffeomorphic to $\mathbb{S}^{n-1} / \Gamma$, for $\Gamma \neq\{\mathrm{Id}\}$, of a manifold $(M, g)$ satisfying:
\begin{itemize}
\item[(1)] the normal injectivity radius of $\Sigma$ and the injectivity radius of the points of $\Sigma$ in $M$ are bounded below by $3 r_{0}$,
\item[(2)] $\left\|A^{\Sigma}-g^{\Sigma}\right\|_{C^{\alpha}\left(g^{\Sigma}\right)} \leqslant \epsilon$,
\item[(3)] on the annulus $\left\{x, d_{g}^{M}(x, \Sigma)<3 r_{0}\right\}$, we have $\|\operatorname{Rm}(g)\|_{C^{2}(g)}<\epsilon$,
\end{itemize}

Then, there exists a unique function $w$ satisfying $\|w\|_{C^{2, \alpha}\left(g^{\Sigma}\right)} \leqslant C \epsilon$ and such that we have
$$H^{\Sigma(w)} \equiv n-1,$$
where we denoted $\Sigma(w):=\left\{\gamma_{x}(w(x)), x \in \Sigma\right\}$, where $\gamma_{x}$ is the geodesic with $\gamma_{x}(0)=x$, and $\gamma_{x}^{\prime}(0)$ is the unit outwards normal to $\Sigma$. We moreover have the following control,
$$\|w\|_{C^{2, \alpha}\left(g^{\Sigma}\right)} \leqslant C\left\|H^{\Sigma}-(n-1)\right\|_{C^{\alpha}\left(g^{\Sigma}\right)} .$$

Remark 9 By adapting the arguments of Section 3, we know that a hypersurface satisfying the assumptions of Proposition 5 is arbitrarily close (up to a diffeomorphism) in the $C^{1, \alpha}$-topology to the round $\mathbb{S}^{n-1} / \Gamma$.

Remark 10 Recall that we defined our Hölder norms at the scale of the injectivity radius, see Definition 2.1. In our applications, the controls on the injectivity radius will be consequences of Lemma 2.2, and the different curvature controls will be consequences of the previous section.

In general, the construction of spheres with constant mean curvature can be tricky (see for example [Ye96, PX09]) because it is achieved by constructing a right-inverse for the operator $\Delta_{\mathbb{S}^{n-1}}+(n-1)$, where $\Delta_{\mathbb{S}^{n-1}}$ is the Laplace-Beltrami operator (with nonpositive eigenvalues) which is not invertible. In our case, our hypersurfaces are not close to $\mathbb{S}^{n-1}$, but to $\mathbb{S}^{n-1} / \Gamma$ for $\Gamma \neq\{\mathrm{Id}\}$. The crucial difference it makes is that $-(n-1)$ is not an eigenvalue anymore (see [CEV17] for the use of the same remark in the context of asymptotically conical manifolds). Indeed, the eigenfunctions with eigenvalue $-(n-1)$ are the restrictions of nonzero linear functions of $\mathbb{R}^{n}$ to the sphere which cannot be $\Gamma$-invariant.

Remark 11 Geometrically, this comes from the fact that given $\mathbb{S}^{n-1} \subset \mathbb{R}^{n}$, the translations provide constant mean curvature perturbations of the spheres. In the case of $\mathbb{S}^{n-1} / \Gamma \subset \mathbb{R}^{n} / \Gamma$, the center cannot move as it is the fixed point of the group action.

Normal geodesic coordinates. Let us first give some controls on the geometry of the hypersurfaces equidistant to a given hypersurface $\tilde{\Sigma}_{1}$.

Lemma 4.1 For all $n \in \mathbb{N}$ and $0<r_{0}<\frac{1}{6}$, there exists $C>0$ and $0<\epsilon<\frac{r_{0}}{C}$ such that if a hypersurface $\tilde{\Sigma}_{1}$ of a manifold $(M, g)$ satisfies:
\begin{itemize}
\item[-] the normal injectivity radius of $\tilde{\Sigma}_{1}$ and the injectivity radius of points of $\tilde{\Sigma}_{1}$ in $M$ are bounded below by $3 r_{0}$,
\end{itemize}
\begin{itemize}
\item[-] $H^{\tilde{\Sigma}_{1}} \equiv n-1$, and $\left\|A^{\tilde{\Sigma}_{1}}-g^{\tilde{\Sigma}_{1}}\right\|_{C^{\alpha}\left(g^{\tilde{\Sigma}_{1}}\right)}<\epsilon$,
\item[-] on the annulus $\left\{x, d_{g}^{M}(x, \Sigma)<3 r_{0}\right\}$, we have $\|\operatorname{Rm}\|_{C^{2}(g)} \leqslant \epsilon$,
\end{itemize}
then,
$$\begin{aligned}
\left\|\frac{A^{\Sigma_{s}}}{s}-\frac{g^{\Sigma_{s}}}{s^{2}}\right\|_{C^{\alpha}\left(\frac{g^{\Sigma_{s}}}{s^{2}}\right)} & \leqslant C\left(\left\|A^{\tilde{\Sigma}_{1}}-g^{\tilde{\Sigma}_{1}}\right\|_{C^{\alpha} g^{\tilde{\Sigma}_{1}}}+|s-1|\|\operatorname{Rm}\|_{C^{\alpha}(g)}+|s-1|^{2}\|\operatorname{Rm}\|_{C^{2}(g)}\right) \\
& \leqslant C\left(1+r_{0}^{2}\right) \epsilon
\end{aligned}$$
and
$$\left\|\frac{H^{\Sigma_{s}}}{s}-\frac{n-1}{s^{2}}\right\|_{C^{\alpha}\left(\frac{g^{\Sigma_{s}}}{s^{2}}\right)} \leqslant C\left(|s-1|\|\operatorname{Ric}\|_{C^{\alpha}(g)}+|s-1|^{2}\|\operatorname{Rm}\|_{C^{2}(g)}\right) \leqslant C\left(r_{0}+r_{0}^{2}\right) \epsilon .$$

Proof Given a hypersurface $\Sigma_{1}$ whose normal injectivity radius is larger than $3 r_{0}>0$, we define a vector field $N$ on the region $\left\{x, d_{g}^{M}(x, \Sigma)<3 r_{0}\right\}$ by setting $N(x)$, for $x \in \Sigma_{s}$, as the outwards normal vector of the hypersurface $\Sigma_{S}$.

Denoting, $S(X):=\nabla_{X} N$, for $X$ a vector field on $M$, we have
$$\left(\nabla_{N} S\right)(X)=-\left(S^{2}(X)+\operatorname{Rm}(X, N) N\right) .$$
Assuming $\left\|S_{\mid \Sigma_{1}}-\mathrm{Id}\right\|_{C^{\alpha}\left(g^{\Sigma_{1}}\right)}<\epsilon$ for $\epsilon>0$ small enough, we can follow $S$ along the normal geodesics, and integrating the previous Riccati equation (17), we find that there exits $C>0$ such that for $|s-1| \leqslant r_{0} \leqslant \frac{1}{6}$,
$$\left\|\frac{S_{\mid \Sigma_{s}}}{s}-\frac{\mathrm{Id}}{s^{2}}\right\|_{C^{\alpha}\left(g^{\Sigma_{s}}\right)} \leqslant\left\|S_{\mid \Sigma_{1}}-\mathrm{Id}\right\|_{C^{\alpha}\left(g^{\Sigma_{1}}\right)}+C|s-1|\left\|\operatorname{Rm}_{g}\right\|_{C^{\alpha}(g)}+C|s-1|^{2}\left\|\operatorname{Rm}_{g}\right\|_{C^{2}(g)} .$$
Denoting $\kappa_{i}(s)$ the eigenvalues of the second fundamental form of $\Sigma_{s}$, and $\left(e_{i}(s)\right)$ an associated orthonormal basis of eigenvectors, if we project (17) on $e_{i}(s)$, we get:
$$\kappa_{i}^{\prime}(s)=-\left(\kappa_{i}(s)^{2}+g\left(\operatorname{Rm}\left(N^{s}, e_{i}(s)\right) e_{i}(s), N^{s}\right)\right)$$
and finally, by summing on $i, H^{\prime}(s)=-\left(|A|^{2}(s)+\operatorname{Ric}\left(N^{s}, N^{s}\right)\right)$. With the initial condition $H(1) \equiv n-1$, we finally have the second stated estimate. \(\square\)

Let us now construct coordinates in the neighborhood of a hypersurface satisfying the assumptions of Proposition 5.

Lemma 4.2 Let $\Sigma$ be a hypersurface satisfying the assumptions of Proposition 5. Then, there exists a diffeomorphism $\Phi: A_{e}\left(1-2 r_{0}, 1+2 r_{0}\right) \rightarrow\left\{x, d(x, \Sigma)<2 r_{0}\right\}$ such that we have for $C>0$,
$$\left\|\Phi^{*} g-g_{e}\right\|_{C^{1, \alpha}\left(g_{e}\right)} \leqslant C \epsilon,$$
where $\epsilon>0$ is the constant of Proposition 5.

Proof Let us consider the diffeomorphism $F_{g}: \Sigma \times\left[-2 r_{0}, 2 r_{0}\right]$ obtained from the outwards normal geodesic of Σ.

We then use our controls on the second fundamental form and the ambient curvature and integrate the Riccati equation satisfied by the Jacobi fields generated by the infinitesimal change of starting point on the hypersurface $\Sigma$. We therefore obtain like in Lemma 4.1 the following control for $C=C\left(n, v_{0}\right)>0$, by noting $s$ the parameter of the geodesics vanishing on $\Sigma$ :
$$\left\|F_{g}^{*} g-\left(d s^{2}+s^{2} g^{\Sigma}\right)\right\|_{C^{1, \alpha}} \leqslant C \epsilon .$$
By the assumptions of Proposition 5, up to choosing $\epsilon$ arbitrarily small, the second fundamental form is arbitrarily close to being constant and the ambient curvature arbitrarily small. In particular, according to Gauss equation (14) together with Lemma A. 1 and Proposition 4, this implies that there exists $\Gamma \subset S O(4)$ such that, up to reparametrizing $\Sigma$, we have for some $C=C\left(n, v_{0}\right)>0$,
$$\left\|g^{\Sigma}-g^{\mathbb{S}^{n-1} / \Gamma}\right\|_{C^{1, \alpha}} \leqslant C \epsilon .$$
Combining this with the control (18), we get the stated result. \(\square\)

Normal perturbations of the hypersurface. Consider normal perturbations of a hypersurface $\Sigma$ of the form $\Sigma(w):=\left\{\gamma_{x}(w(x)), x \in \Sigma\right\}$. The computations of [PX09] adapted to our situation yield the following development of the mean curvature.

Lemma 4.3 For any $0<r_{0}<\frac{1}{6}$ and any smooth hypersurface $\Sigma \subset M$ whose injectivity radius and normal injectivity radius are larger than $3 r_{0}$, there exists $\epsilon>0$ such that for all $w: \Sigma \rightarrow \mathbb{R}$ such that $\|w\|_{C^{2, \alpha}\left(g^{\Sigma}\right)} \leqslant \epsilon$, the mean curvature of $\Sigma(w)$ has the development:
$$H(\Sigma(w))=H(\Sigma)-J_{\Sigma, M} w+Q_{\Sigma, M}(w),$$
where
$$J_{\Sigma, M}:=\Delta_{\Sigma}+\left|A^{\Sigma}\right|^{2}+\operatorname{Ric}^{M}(N, N)$$
is the Jacobi operator of the hypersurface, and where $Q_{\Sigma, M}$ is such that for a constant $C>0$ depending on the $C^{2}$-norm of the curvature and the $C^{1}$-norm of the second fundamental form and $r_{0}$, we have :
$$\left\|Q_{\Sigma, M}(w)-Q_{\Sigma, M}\left(w^{\prime}\right)\right\|_{C^{\alpha}\left(g^{\Sigma}\right)} \leqslant C\left\|w-w^{\prime}\right\|_{C^{2, \alpha}\left(g^{\Sigma}\right)}\left(\|w\|_{C^{2, \alpha}\left(g^{\Sigma}\right)}+\left\|w^{\prime}\right\|_{C^{2, \alpha}\left(g^{\Sigma}\right)}\right) .$$

Proof \(\square\)

Proposition 5 is then a consequence of the following Lemma applied to $\Sigma$.

Lemma 4.4 For any $r_{0}>0$, there exists $\epsilon>0$ such that if a metric $g$ on the annulus $A_{e}\left(1-r_{0}, 1+r_{0}\right) \subset \mathbb{R}^{n} / \Gamma$ for $\Gamma \subset \operatorname{SO}(n)$ with $\Gamma \neq\{\mathrm{Id}\}$ satisfies
\begin{itemize}
\item[-] $\left\|g-g_{e}\right\|_{C^{1, \alpha}\left(g_{e}\right)} \leqslant \epsilon$,
\item[-] on $S$ the unit sphere centered at zero in $S \subset \mathbb{R}^{n} / \Gamma$, we have
$$\left\|A_{g}^{S}-g_{\mid S}\right\|_{C^{\alpha}(S)} \leqslant \epsilon,$$
\item[-] on $A_{e}\left(1-r_{0}, 1+r_{0}\right)$, we have
$$\left\|\operatorname{Rm}_{g}\right\|_{C^{4}\left(g_{e}\right)} \leqslant \epsilon,$$
\end{itemize}
Then, there exists $\epsilon_{1}=\epsilon_{1}\left(r_{0}, \epsilon, n, \alpha\right)>0$ such that there exists a unique solution $w$ satisfiying $\|w\|_{C^{2, \alpha}(S)} \leqslant \epsilon_{1}$ to the equation
$$H_{g}(S(w)) \equiv n-1,$$
where $H_{g}$ is the mean curvature for $g$ and where $S(w)=\left\{\gamma_{x}(w(x)), x \in S\right\}$ for $\gamma_{x}$ the geodesic starting $x$ and outwards normal to $S$.

We moreover have the control:
$$\|w\|_{C^{2, \alpha}(S)} \leqslant C\left\|H_{g}(S)-(n-1)\right\|_{C^{\alpha}(S)} .$$

Proof This is a consequence of the following quantitative version of the inverse function theorem proven by Banach fixed point theorem.

Lemma 4.5 Let $\Phi: E \rightarrow F$, be a smooth map between Banach spaces and let $Q:=\Phi-\Phi(0)-d_{0} \Phi$.

Assume that there exist $q>0, r_{0}>0$ and $c>0$ such that
\begin{itemize}
\item[(1)] for all $x$ and $y$ in $B\left(0, r_{0}\right)$, we have the following control on the nonlinear terms
$$\|Q(x)-Q(y)\| \leqslant q(\|x\|+\|y\|)\|x-y\| .$$
\item[(2)] the linearization $d_{0} \Phi$ is an isomorphism, and more precisely, we have
$$\left\|\left(d_{0} \Phi\right)^{-1}\right\| \leq c .$$
If $r \leqslant \min \left(r_{0}, \frac{1}{2 q c}\right)$ and $\|\Phi(0)\| \leqslant \frac{r}{2 c}$, then, the equation $\Phi(x)=0$ admits a unique solution in $B(0, r)$.
\end{itemize}

We will equip $S$ with the Hölder norms given by the restriction of $g_{e}$ on $S$. Let us consider the operator $\Phi: C^{2, \alpha}(S) \rightarrow C^{0, \alpha}(S)$ defined by
$$\Phi: w \in C^{2, \alpha}(S) \mapsto H_{g}(S(w))-(n-1) \in C^{0, \alpha}(S),$$
and show that it satisfies the assumptions of Lemma 4.5, with $\Phi(0)=H_{g}(S)-(n-1)$, $d_{0} \Phi=J_{S, g}$.

Remark 12 In this proof, we will precise the metric instead of the manifold for the Jacobi operator and the nonlinear terms of the mean curvature variations.
\begin{itemize}
\item[(1)] The operator $J_{S, g}$ is invertible and has a bounded inverse for $\epsilon>0$ small enough. Indeed, $-(n-1)$ is not an eigenvalue of the Laplacian because $\Gamma \neq\{\mathrm{Id}\}$, therefore $J_{S, g_{e}}$ is invertible with a bounded inverse. Moreover, by proximity of the metrics and the control of the $C^{\alpha}(S)$-norm of the second fundamental form and the $C^{4}$-norm of the ambient curvature, there exists $C_{1}>0$ such that,
$$\left\|J_{S, g_{e}}-J_{S, g}\right\| \leqslant C_{1} \epsilon,$$
for the operator norm from $C^{2, \alpha}(S)$ to $C^{\alpha}(S)$. The operator $J_{S, g}$ is therefore invertible with a bounded inverse for $\epsilon$ small enough since this is an open condition.
\item[(2)] The nonlinear terms are controlled in a quadratic way. There exists a constant $C>0$ depending on $r_{0}, \alpha$ and $\epsilon$ :
$$\left\|Q_{S, g}(w)-Q_{S, g}\left(w^{\prime}\right)\right\|_{C^{\alpha}} \leqslant C\left\|w-w^{\prime}\right\|_{C^{2, \alpha}(S)}\left(\|w\|_{C^{2, \alpha}}+\left\|w^{\prime}\right\|_{C^{2, \alpha}(S)}\right) .$$
\item[(3)] Since the second fundamental form is almost constant, we have:
$$\left\|H_{g}(S)-(n-1)\right\|_{C^{\alpha}(S)} \leqslant \epsilon .$$
Therefore, there exists a unique solution $w$ to the equation $\Phi(w)=0$ such that $\|w\|_{C^{2, \alpha}(S)} \leqslant \epsilon_{1}:=\min \left(\frac{1}{2 C C_{1}}, 2 C_{1} \epsilon\right)$. This solution moreover satisfies for $C^{\prime}>0$,
$$\|w\|_{C^{2, \alpha}(S)} \leqslant C^{\prime}\left\|H_{g}(S)-(n-1)\right\|_{C^{\alpha}(S)} .$$ \(\square\)
\end{itemize}

Proof of Proposition 5 According to Lemma 4.2, under the assumptions of Proposition 5, then, there exists a diffeomorphism $\Phi: A_{e}\left(1-2 r_{0}, 1+2 r_{0}\right) \rightarrow\left\{x, d(x, \Sigma)<2 r_{0}\right\}$ such that we have for $C>0$,
\begin{itemize}
\item[-] the metrics are close,
$$\left\|\Phi^{*} g-g_{e}\right\|_{C^{1, \alpha}\left(g_{e}\right)} \leqslant C \epsilon,$$
\end{itemize}
\begin{itemize}
\item[-] for the unit-sphere centered at zero denoted $S \subset \mathbb{R}^{n} / \Gamma$, we have
$$\left\|A_{\Phi^{*} g}^{S}-\left(\Phi^{*} g\right)_{\mid S}\right\|_{C^{\alpha}} \leqslant \epsilon,$$
\item[-] for the curvature on $A_{e}\left(1-r_{0}, 1+r_{0}\right)$, we have
$$\left\|\operatorname{Rm}_{\Phi^{*} g}\right\|_{C^{4}} \leqslant \epsilon,$$
where $\epsilon>0$ is the constant in the assumptions of Proposition 5, for which the metric $\Phi^{*} g$ satisfies the assumptions of Lemma 4.4 with $S=\Phi^{*} \Sigma$ the unit-sphere of $\mathbb{R}^{n} / \Gamma$. Applying Lemma 4.4, we obtain the statement of Proposition 5. \(\square\)
\end{itemize}

For $\Sigma$ satisfying the assumptions of Proposition 5, let us define $\tilde{\Sigma}:=\Sigma(w)$, where $w$ is the unique solution given by the proof of Proposition 5.

\section*{5 Construction of a foliation of the neck regions by constant mean curvature hypersurfaces}

Let us now foliate our neck regions by constant mean curvature hypersurfaces.

\subsection*{5.1 Local foliation by constant mean curvature hypersurfaces}

We start by constructing our foliation locally.

Proposition 6 (Local foliation) For all $n \in \mathbb{N}$ and $0<r_{0}<\frac{1}{6}$, there exists $C>0$ and $0<\epsilon<\frac{r_{0}}{C}$ such that if a hypersurface $\tilde{\Sigma}_{1}$ diffeomorphic to $\mathbb{S}^{n-1} / \Gamma$, for $\Gamma \neq\{\mathrm{Id}\}$, of a manifold $(M, g)$ satisfies:
\begin{itemize}
\item[-] the normal injectivity radius of $\tilde{\Sigma}_{1}$ and the injectivity radius of the points $\tilde{\Sigma}_{1}$ in $M$ are bounded below by $3 r_{0}$,
\item[-] $H^{\tilde{\Sigma}_{1}} \equiv n-1$, and $\left\|A^{\tilde{\Sigma}_{1}}-g^{\tilde{\Sigma}_{1}}\right\|_{C^{\alpha}\left(g^{\tilde{\Sigma}_{1}}\right)}<\epsilon$,
\item[-] on the annulus $\left\{x, d_{g}^{M}(x, \Sigma)<3 r_{0}\right\}$, we have $\left\|\mathrm{Rm}_{g}\right\|_{C^{2}(g)} \leqslant \epsilon$.
\end{itemize}
Then, there exists a family of hypersurfaces $\tilde{\Sigma}_{s}, s \in\left[\frac{1}{1+2 r_{0}}, 1+2 r_{0}\right]$ with constant mean curvature $\frac{n-1}{s}$ foliating a region of the annulus $\tilde{A}\left(\frac{1}{1+2 r_{0}}, 1+2 r_{0}\right)$ satisfying:
$$\left\{x, d_{g}^{M}(x, \Sigma)<r_{0}\right\} \subset \tilde{A}\left(\frac{1}{1+2 r_{0}}, 1+2 r_{0}\right) \subset\left\{x, d_{g}^{M}(x, \Sigma)<3 r_{0}\right\} .$$

The construction we propose consists in perturbing normally the level sets of the distance function to the hypersurface $\tilde{\Sigma}_{1}$ in constant mean curvature hypersurfaces by Proposition 5.

Let us define the equidistant hypersurfaces $\Sigma_{s}:=\left\{\gamma_{x}(s-1), x \in \tilde{\Sigma}_{1}\right\}$ for $s>0$ small enough where $\gamma_{x}$ is the outwards normal geodesic to the hypersurface $\tilde{\Sigma}$ starting at $x$. These hypersurfaces foliate the annulus $\left\{x, d_{g}^{M}(x, \Sigma)<3 r_{0}\right\}$ by definition of the normal injectivity and their geometry is well controlled around $\tilde{\Sigma}_{1}$.

Proof of Proposition 6 Thanks to the controls (16), and (15), we can use Lemma 4.4 to perturb normally each hypersurface $\Sigma_{s}$ to a constant mean curvature hypersurface $\tilde{\Sigma}_{s}$. Hence, there exists a family of hypersurfaces $\left(\tilde{\Sigma}_{s}\right)_{s \in\left[\frac{1}{1+2 r_{0}}, 1+2 r_{0}\right]}$ with mean curvature constant equal to $\frac{n-1}{s}$ for each $s$. These hypersurfaces are defined from a unique function $w_{s}$ from $\tilde{\Sigma}_{1}$ to $\mathbb{R}$ by Proposition 5,
$$\tilde{\Sigma}_{s}=\Sigma\left(s\left(1+w_{s}\right)\right):=\left\{\gamma_{x}\left(s\left(1+w_{s}(x)\right)\right), x \in \tilde{\Sigma}_{1}\right\},$$
we moreover have the control
$$\left\|w_{s}\right\|_{C^{2, \alpha}\left(g^{\tilde{\Sigma}_{1}}\right)} \leqslant C \epsilon\left(|s-1|+|s-1|^{2}\right) .$$
Let us now show that this family actually foliates the annulus. More precisely, we will show that given $s$ and $s^{\prime} \in\left[\frac{1}{1+2 r_{0}}, 1+2 r_{0}\right]$, close enough and such that $s<s^{\prime}, \tilde{\Sigma}_{s^{\prime}}$ is a normal perturbation of $\tilde{\Sigma}_{s}$ by a strictly positive function $w_{s}^{s^{\prime}}: \tilde{\Sigma}_{s} \rightarrow \mathbb{R}$. They are indeed normal perturbation of each other because they are small (in $C^{2, \alpha}\left(g^{\tilde{\Sigma}_{1}}\right)$-norm) normal perturbations of the equidistant hypersurfaces from $\tilde{\Sigma}_{1}$.

By Lemma 4.4, for $s$ and $s^{\prime}$ close enough, the function $w_{s}^{s^{\prime}}$ satisfies $\left\|w_{s}^{s^{\prime}}\right\|_{C^{2, \alpha}\left(\left(g^{\Sigma_{s}}\right)\right)} \leqslant$ $2\left|s^{\prime}-s\right|$ and is a solution to
$$-J_{\tilde{\Sigma}_{s}, M}\left(w_{s}^{s^{\prime}}\right)=\frac{n-1}{s^{\prime}}-\frac{n-1}{s}+Q_{\tilde{\Sigma}_{s}, M}\left(w_{s}^{s^{\prime}}\right),$$
where there exists $C=C\left(\epsilon, n, \alpha, r_{0}\right)>0$ independent of $s$ such that for any functions $w$, and $w^{\prime}$, we have $\left\|Q_{\tilde{\Sigma}_{s}, M}(w)-Q_{\tilde{\Sigma}_{s}, M}\left(w^{\prime}\right)\right\|_{C^{\alpha}\left(g^{\tilde{\Sigma}_{s}}\right)} \leqslant C\left\|w-w^{\prime}\right\|_{C^{2, \alpha}}\left(\|w\|_{C^{2, \alpha}\left(g^{\tilde{\Sigma}_{s}}\right)}+\right.$ $\left.\left\|w^{\prime}\right\|_{C^{2, \alpha}\left(g^{\tilde{\Sigma}_{s}}\right)}\right)$.

We therefore get $\left\|Q_{\tilde{\Sigma}_{s}, M}\left(w_{s}^{s^{\prime}}\right)\right\|_{C^{\alpha}\left(g^{\tilde{\Sigma}_{s}}\right)} \leqslant 4 C\left|s^{\prime}-s\right|^{2}$, and since $s \tilde{\Sigma}_{s}$ is close to $\mathbb{S}^{n-1} / \Gamma$, for $\left|s^{\prime}-s\right|$ small enough, $J_{\tilde{\Sigma}_{s}, M}$ is close to $\Delta^{\mathbb{S}^{n-1} / \Gamma}+n-1$, and we have:
$$\left\|-\left(\Delta^{\mathbb{S}^{n-1} / \Gamma}+n-1\right)\left(w_{s}^{s^{\prime}}-\left(s^{\prime}-s\right)\right)\right\|_{C^{\alpha}\left(g^{\tilde{\Sigma}_{s}}\right)} \leqslant C\left(\left(s^{\prime}-s\right)^{2}+\epsilon\left(s^{\prime}-s\right)\right) .$$

Since $-\Delta^{\mathbb{S}^{n-1} / \Gamma}+n-1$ is invertible, there exists $C=C(\alpha, n)>0$ such that
$$\left\|w_{s}^{s^{\prime}}-\left(s^{\prime}-s\right)\right\|_{C^{2, \alpha}\left(g^{\tilde{\Sigma}_{s}}\right)} \leqslant C\left(\left(s^{\prime}-s\right)^{2}+\epsilon\left(s^{\prime}-s\right)\right) .$$
Finally, we have $w_{s}^{s^{\prime}}=\left(s^{\prime}-s\right)+\mathcal{O}\left(\left(s^{\prime}-s\right)^{2}+\epsilon\left(s^{\prime}-s\right)\right)$, and in particular, for $s^{\prime}-s>0$ and $\epsilon$ small enough (depending on $n$ and $\alpha$ ), we have $w_{s}^{s^{\prime}}>0$.

This implies that for all $s, s^{\prime} \in\left[\frac{1}{1+2 r_{0}}, 1+2 r_{0}\right]$, the hypersurfaces $\tilde{\Sigma}_{s}$ and $\tilde{\Sigma}_{s^{\prime}}$ are all disjoint and foliate the annulus. Indeed, we have just seen that for $s<s^{\prime}$ and $\left|s-s^{\prime}\right|$ small enough, the hypersurface $\tilde{\Sigma}_{s^{\prime}}$ is strictly included in one side of $\tilde{\Sigma}_{s}$. Recalling that for all $s, \tilde{\Sigma}_{s}=\tilde{\Sigma}_{1}\left(s\left(1+w_{s}\right)\right)$, this means that for all $x$, the function $s \mapsto\left(s\left(1+w_{s}(x)\right)\right)$ is strictly increasing, and therefore that we indeed have a foliation of the annulus. \(\square\)

Remark 13 It was not directly possible to ensure that two hypersurfaces $\tilde{\Sigma}_{s}$ and $\tilde{\Sigma}_{s^{\prime}}$ do not intersect for $s, s^{\prime} \in\left[\frac{1}{1+2 r_{0}}, 1+2 r_{0}\right]$ from our previous controls. Indeed, the control $\left\|w_{s}\right\|_{C^{2, \alpha}\left(g^{\tilde{\Sigma}_{1}}\right)} \leqslant C\left(\epsilon|s-1|+\epsilon|s-1|^{2}\right)$ is not enough to rule out $w_{s}(x)=w_{s^{\prime}}\left(x^{\prime}\right)$ when $s-1$ is much larger than $s-s^{\prime}$.

\subsection*{5.2 Global foliation of the neck regions.}

Let us come back to our applications and consider an Einstein manifold $(M, g)$ close to an Einstein orbifold $\left(M_{o}, g_{o}\right)$ in the Gromov-Hausdorff sense. According to Proposition 1, this manifold is $\epsilon$-approximated by a tree of Ricci-flat ALE orbifolds desingularizing the orbifold $\left(M_{o}, g_{o}\right)$. We have satisfactory coordinates on the regions $\mathcal{M}_{o}(\epsilon)$ and $\mathcal{N}_{k}(\epsilon)$ and want to find good coordinates in the annuli $\mathcal{A}_{k}(t, \epsilon)$. They are included in metric annuli $A\left(\rho_{1}, \rho_{2}\right)$ for $\rho_{1}:=\frac{1}{8} \epsilon^{-1} T_{k}^{\frac{1}{2}}$ and $\rho_{2}:=8 \epsilon T_{j}^{\frac{1}{2}}$ on which we have the following properties:
\begin{itemize}
\item[(1)] the curvature is controlled by [Ban90, Proposition 3]: for all $l \in \mathbb{N}$, there exists $C>0$ and $\beta_{1}, \beta_{2}>0$ depending on $g_{o}$ and the $g_{b_{j}}$ such that at distance $\rho \in\left[\frac{\rho_{1}}{2}, 2 \rho_{2}\right]$ from $p$, we have
$$\rho^{2+l}\left|\nabla^{l} \operatorname{Rm}\right| \leqslant \eta(\rho):=C \epsilon\left[\left(\frac{\rho_{1}}{\rho}\right)^{\beta_{1}}+\left(\frac{\rho}{\rho_{2}}\right)^{\beta_{2}}\right],$$
\end{itemize}

Remark 14 In [Ban90], the result is only stated for $l=0$, but the regularity of Einstein metrics, and in particular the fact that the curvature is harmonic (for the Hodge Laplacian) yields the estimate for higher derivatives by local elliptic estimates.
\begin{itemize}
\item[(2)] by Proposition 2, there exists $\delta(\epsilon)$ such that $\delta(\epsilon) \rightarrow 0$ as $\epsilon \rightarrow 0$ and for any $2 \rho_{1}<\rho<\frac{1}{4} \rho_{2}$, there exists a region $\hat{A}(\rho, 2 \rho)$ satisfiying
$$A((1+\delta) \rho,(2-\delta) \rho) \subset \hat{A}(\rho, 2 \rho) \subset A((1-\delta) \rho,(2+\delta) \rho),$$
$\Gamma$ a finite subgroup of $S O(4)$ and a diffeomorphism
$$\Phi_{\rho}: A_{e}(1,2) \subset \mathbb{R}^{4} / \Gamma \rightarrow \hat{A}(\rho, 2 \rho) \subset M,$$
for which we have,
$$\left\|\frac{\Phi_{\rho}^{*} g}{\rho^{2}}-g_{e}\right\|_{C^{l+2}\left(A_{e}(1,2)\right)} \leqslant \delta$$
\item[(3)] by Lemma 2.6, there exists a hypersurface $\Sigma_{\rho_{1}}$ whose second fundamental form satisfies $\left\|\frac{A_{g}^{\Sigma \rho_{1}}}{\rho_{1}}-\frac{g}{\rho_{1}^{2}}\right\|_{C^{l+1}\left(\frac{g}{\rho_{1}^{2}}\right)} \leqslant \delta$,
\item[(4)] by Lemma 2.2 and Lemma 2.7 there exists $r_{0}>0$ such that the injectivity radius at each point $x$ is bounded below by $r_{0} d(x, p)$, and the normal injectivity radius to $\Sigma_{\rho_{1}}$ by Lemma 2.6 is bounded below by $r_{0} \rho_{1}$.
\end{itemize}

The control (19) means that in the middle of the annulus, we have a much better control than initially expected since the classical $\epsilon$-regularity theorems [Gao90, BKN89, And89] would only give $\rho^{2}|\mathrm{Rm}| \leqslant C\|\mathrm{Rm}\|_{L^{2}\left(A\left(\rho_{1}, \rho_{2}\right)\right)}$. From the point of view of analysis, the difference is substantial as it allows one to do analysis in weighted Hölder spaces, and this will be heavily used in [Ozu19b].

Remark 15 Analogous estimates hold in any dimension $n$ by assuming some much less natural $L^{\frac{n}{2}}$-controls on the Riemann curvature.

The main difficulty in constructing good coordinates here is that the interior radius, $\rho_{1}$, is neglectible when compared to the radius at which our controls are optimal, $\bar{\rho}:=\left(\rho_{1}^{\beta_{1}} \rho_{2}^{\beta_{2}}\right)^{\frac{1}{\beta_{1}+\beta_{2}}}$ which minimizes $\eta$. Constant mean curvature hypersurfaces are convenient in this context as they can be constructed in the entire zone, and can be controlled by Proposition 3.

Proposition 7 For all $n \in \mathbb{N}$, there exists $\epsilon_{0}>0$, and $C>0$ such that for any $0<\epsilon<\epsilon_{0}$, we have the following property. Let $\mathcal{A}_{k}(t, \epsilon)$ be an intermediate annulus of an Einstein metric which is $\epsilon$-approximated by a naïve desingularization, and assume that it is included in a metric annulus $A\left(4 \rho_{1}, \frac{1}{4} \rho_{2}\right)$ with $\int_{A\left(\rho_{1}, \rho_{2}\right)}|\mathrm{Rm}|^{2} d v<\epsilon^{2}$. Then, there exists a foliation of a region $\tilde{A}\left(2 \rho_{1}, \frac{1}{2} \rho_{2}\right)$ bounded by two hypersurfaces of mean curvature respectively constant equal to $\frac{n-1}{2 \rho_{1}}$ and $\frac{n-1}{\frac{1}{2} \rho_{2}}$, with
$$\mathcal{A}_{k}(t, \epsilon) \subset A\left((2+C \epsilon) \rho_{1},\left(\frac{1}{2}-C \epsilon\right) \rho_{2}\right) \subset \tilde{A}\left(2 \rho_{1}, \frac{1}{2} \rho_{2}\right) \subset A\left((2-C \epsilon) \rho_{1},\left(\frac{1}{2}+C \epsilon\right) \rho_{2}\right),$$
by hypersurfaces denoted $\tilde{\Sigma}_{s}$ whose mean curvature equals $\frac{n-1}{s}$.

Proof Considering $\Phi_{2 \rho_{1}}$, the diffeomorphism of Proposition 2 at scale $2 \rho_{1}$, we define the hypersurface $\Sigma_{2 \rho_{1}}:=\Phi_{2 \rho_{1}, *} S \subset M$, where $S$ is the unit-sphere centered at zero of $\mathbb{R}^{4} / \Gamma$. According to Lemmata 2.6 and 2.7, and Corollary 1 , we satisfy the assumptions of Lemma 4.4. We can therefore perturb $\Sigma_{2 \rho_{1}}$ to a hypersurface $\tilde{\Sigma}_{2 \rho_{1}}$ whose mean curvature is constant equal to $\frac{n-1}{2 \rho_{1}}$.

According to Proposition 6, there exists a foliation by hypersurfaces $\tilde{\Sigma}_{s}$ whose mean curvature is constant equal to $\frac{n-1}{s}$ for all $2 \rho_{1}<s<\left(1+2 r_{0}\right) 2 \rho_{1}$. Moreover, for any $s$, there exists a constant $C=C(n, \alpha)>0$ such that if we recall the notation
$$\eta(s):=C \epsilon\left[\left(\frac{\rho_{1}}{s}\right)^{\beta_{1}}+\left(\frac{s}{\rho_{2}}\right)^{\beta_{2}}\right],$$
we have the following a priori controls on the $\tilde{\Sigma}_{s}$ thanks to Proposition 3:
\begin{itemize}
\item[-] the normal injectivity radius of $\tilde{\Sigma}_{s}$ and the injectivity radius of the points of $\tilde{\Sigma}_{s}$ in $M$ are bounded below by $3 s r_{0}$ according to Lemmata 2.2 and 2.7,
\item[-] $H^{\tilde{\Sigma}_{1}} \equiv \frac{n-1}{s}$, and $\left\|\frac{A^{\tilde{\Sigma}_{s}}}{s}-\frac{g^{\tilde{\Sigma}_{s}}}{s^{2}}\right\|_{C^{\alpha}}<C \eta(s)$,
\item[-] on the annulus $\left\{x, d_{g}^{M}\left(x, \tilde{\Sigma}_{1}\right)<3 s r_{0}\right\}$, we have $\left\|\operatorname{Rm}_{g}\right\|_{C^{4}(g)} \leqslant \frac{C \eta(s)}{s^{2}}$.
\end{itemize}
We can therefore apply Proposition 6 from the hypersurface $\tilde{\Sigma}_{2\left(1+2 r_{0}\right) \rho_{1}}$ in order to obtain a foliation by hypersurfaces with constant mean curvature equal to $\frac{n-1}{s}$ up to $s=2\left(1+2 r_{0}\right)^{2} \rho_{1}$. Once again, the a priori controls of Proposition 3 of order $C \eta(s)$ and the injectivity and normal injectivity controls of Lemmata 2.2 and 2.7 let us iterate this process in order to construct hypersurfaces $\tilde{\Sigma}_{s}$ with mean curvature constant equal to $\frac{n-1}{s}$ up to $s=2\left(1+2 r_{0}\right)^{k} \rho_{1}$ for any $k \in \mathbb{N}$ with $2\left(1+2 r_{0}\right)^{k} \rho_{1}<\frac{1}{2} \rho_{2}$ which is the stated result. \(\square\)

\section*{6 Construction of coordinates and control on the metric}

To construct a diffeomorphism, we will use the constant mean curvature hypersurface where our estimates are optimal and follow the gradient lines of the function $s:=\frac{n-1}{H\left(\Sigma_{s}\right)}$ whose level sets are the hypersurfaces $\tilde{\Sigma}_{S}$. The main result is the following Proposition:

Proposition 8 Under the same assumptions as Proposition 7, there exists $\beta_{1}>0$, $\beta_{2}>0, \Gamma \neq\{\mathrm{Id}\}$ a finite subgroup of $S O(4)$ such that for all $l \in \mathbb{N}$, there exists $C>0$, and a diffeomorphism:
$$\Phi: A_{e}\left(2 \rho_{1}, \frac{1}{2} \rho_{2}\right) \rightarrow \tilde{A}\left(2 \rho_{1}, \frac{1}{2} \rho_{2}\right),$$
such that for all $\rho \in\left[2 \rho_{1}, \frac{1}{4} \rho_{2}\right]$, denoting $\Phi_{\rho}:=\Phi \circ \phi_{\rho}: A_{e}(1,2) \rightarrow \tilde{A}\left(2 \rho_{1}, \frac{1}{2} \rho_{2}\right)$, where $\phi_{\rho}$ is the homothetic transformation of ratio $\rho$ on $\mathbb{R}^{4} / \Gamma$, we have:
$$\left\|\frac{\Phi_{\rho}^{*} g}{\rho^{2}}-g_{e}\right\|_{C^{l}\left(A_{e}(1,2)\right)} \leqslant C \epsilon\left(\left(\frac{\rho_{1}}{\rho}\right)^{\beta_{1}}+\left(\frac{\rho}{\rho_{2}}\right)^{\beta_{2}}\right) .$$

Remark 16 Our proofs again work in any dimension $n \in \mathbb{N}$ for metrics with a region close to a flat cone $\mathbb{R}^{n} / \Gamma$ (for $\Gamma \neq\{\mathrm{Id}\}$ ) where the curvature is small in $L^{\frac{n}{2}}$.

\subsection*{6.1 Coordinates based on our constant mean curvature foliation}

In the foliation constructed in Proposition 7, one particular hypersurface is better controlled than the others at its scale. It is $\tilde{\Sigma}_{\bar{\rho}}$ where $\eta(\bar{\rho})=\min _{\rho_{1}<\rho<\rho_{2}} \eta(\rho)$, which satisfies the following properties by (19) and Proposition 3:
\begin{itemize}
\item[(1)] there exists a diffeomorphism $\phi: \mathbb{S}^{n-1} / \Gamma \rightarrow \tilde{\Sigma}_{\bar{\rho}}$ such that: for all $k \in \mathbb{N}$ and $0<\alpha<1$, there exists $C=C\left(k, \alpha, n, r_{0}\right)>0$ for which,
$$\left\|\frac{\phi^{*} g^{\tilde{\Sigma}_{\bar{\rho}}}}{\bar{\rho}^{2}}-g^{\mathbb{S}^{n} / \Gamma}\right\|_{C^{k, \alpha}\left(g^{\mathbb{S}^{n} / \Gamma}\right)}<C \eta(\bar{\rho}),$$
\item[(2)] for all $k \in \mathbb{N}$ and $0<\alpha<1$, there exists $C=C(k, \alpha, n)>0$ such that
$$\left\|\frac{A^{\tilde{\Sigma}_{\bar{\rho}}}}{\bar{\rho}}-\frac{g^{\tilde{\Sigma}_{\bar{\rho}}}}{\bar{\rho}^{2}}\right\|_{C^{k, \alpha}\left(\frac{g^{\tilde{\Sigma}_{\bar{\rho}}}}{\bar{\rho}^{2}}\right)} \leqslant C \eta(\bar{\rho}) .$$
\item[(3)] for all $k \in \mathbb{N}$, there exists $C=C(k, n)>0$ such that on the annulus $\left[\frac{1}{2} \bar{\rho}, 2 \bar{\rho}\right]$ we have,
$$\bar{\rho}^{2+k}\left|\nabla^{k} \operatorname{Rm}\right|_{g} \leqslant C \eta(\bar{\rho}) .$$
We then define a diffeomorphism $\Phi:\left[\rho_{1}, \rho_{2}\right] \times \mathbb{S}^{n-1} / \Gamma \rightarrow \tilde{A}\left(\rho_{1}, \rho_{2}\right)$ in the following way: at $\bar{\rho}$,
$$\Phi(\bar{\rho}, x):=\phi(x),$$
where $\phi$ is the diffeomorphism of the above point 1 , and for all $s \in\left[\rho_{1}, \rho_{2}\right]$,
$$\partial_{s} \Phi(s, x)=u_{s}(x) N^{\tilde{\Sigma}_{s}}(\Phi(s, x))=-\frac{\nabla s}{|\nabla s|^{2}},$$
\end{itemize}
where $u_{s}$ is such that $\Phi\left(s, \mathbb{S}^{n-1} / \Gamma\right)=\tilde{\Sigma}_{s}$. This is a diffeomorphism on its image since two curves following the vector field $-\frac{\nabla s}{|\nabla s|^{2}}$, which never vanishes, cannot intersect if they are not equal.

\subsection*{6.2 Control of the metric in these coordinates}

In the coordinates given by $\Phi$, the metric has the following form,
$$\Phi^{*} g(s, x)=u_{s}(x)^{2} d s^{2}+s^{2} h_{s}(x),$$
where $h_{s}$ is a metric on $\mathbb{S}^{n-1} / \Gamma$.

Let us take the following notations for the rest of the section in which we will always work on $\mathbb{R}^{n} / \Gamma$ :
\begin{itemize}
\item[-] $\phi_{s}(x)=\Phi(s, x)$, which implies that $s^{2} h_{s}=\phi_{s}^{*} g^{\tilde{\Sigma}_{s}}$.
\item[-] $H(s)=\phi_{s}^{*} H^{\tilde{\Sigma}_{s}} \equiv \frac{n-1}{s}$,
\item[-] $A(s)=\phi_{s}^{*} A^{\tilde{\Sigma}_{s}}$,
\item[-] $N(s)=\phi_{s}^{*} N^{\tilde{\Sigma}_{s}}$
\item[-] $f_{i}(s)=d_{(s, .)} \Phi\left(0, e_{i}\right)$, where the $e_{i}$ form an orthonormal basis of $T_{x} \mathbb{S}^{n-1} / \Gamma$,
\item[-] $\nabla^{s}=\phi_{s}^{*} \nabla^{\tilde{\Sigma}_{s}}$,
\item[-] $\Delta^{s}=\phi_{s}^{*} \Delta^{\tilde{\Sigma}_{s}}$, where $\Delta^{\tilde{\Sigma}_{s}}$ is the Laplace-Beltrami operator associated to the metric $g^{\Sigma_{s}}$,
\item[-] grad ${ }^{s}$ is the gradient for the metric $s^{2} h_{s}$,
\item[-] $K(s)_{i}^{j}=g\left(\operatorname{Rm}_{g}\left(N(s), f_{i}(s)\right) f_{j}(s), N(s)\right)$.
\end{itemize}

We have the following variations for the different geometric quantities.
By [HP99, Theorem 3.2], given a variation $\partial_{s} \Phi(s, x)=u_{s} N^{\tilde{\Sigma}_{s}}$, we have the following variation formulas:
$$\begin{gathered}
\partial_{s}\left(s^{2} h_{s}\right)=2 u_{s} A(s), \\
\partial_{s} N(s)=\operatorname{grad}^{s} u_{s}, \\
\partial_{s} A(s)_{i j}=-\nabla_{i}^{s} \nabla_{j}^{s} u_{s}+\left(\sum_{k} A(s)_{i k} A(s)_{j}^{k}+K(s)_{i}^{j}\right), \\
\partial_{s} H(s)=-\left(\Delta^{s}+|A(s)|^{2}+\operatorname{Ric}(s)(N(s), N(s))\right) u_{s} .
\end{gathered}$$
Let us finally compare our Einstein metric to the flat metric in these coordinates.

Proposition 9 With the above notations, if we denote $g_{e}:=d s^{2}+s^{2} g^{\mathbb{S}^{n-1}}$, we have the following controls on $\Phi^{*} g$ : for all $l \in \mathbb{N}$, there exists $C\left(l, n, v_{0}, D_{0}\right)>0$ such that for all $s \in\left[\rho_{1}, \frac{\rho_{2}}{2}\right]$, on the annulus $[s, 2 s]$, we have
$$\|u-1\|_{C^{l}\left(g_{e}\right)} \leqslant C \eta(s),$$
and
$$\left\|h-g^{\mathbb{S}^{n-1} / \Gamma}\right\|_{C^{l}\left(g_{e}\right)} \leqslant C \eta(s),$$
and therefore, for all $s \in\left[\rho_{1}, \frac{\rho_{2}}{2}\right]$, on the annulus of radii $s$ and $2 s$,
$$\left\|\Phi^{*} g-g_{e}\right\|_{C^{l}\left(g_{e}\right)} \leqslant C \eta(s) .$$

Proof All along the proof, $C$ will denote a positive constant that may vary from line to line, but which only depends on the constants $n, v_{0}, D_{0}$ and the order of regularity $l \in \mathbb{N}, 0<\alpha<1$.

Let us start by noting that the equation (23) implies that for all $s, u_{s}$ satisfies the following equation
$$\frac{n-1}{s^{2}}=\left(\Delta^{s}+|A(s)|^{2}+\operatorname{Ric}(s)(N(s), N(s))\right) u_{s} .$$
Indeed, by following the normal perturbation $u_{S} N^{\tilde{\Sigma}_{s}}=-\frac{\nabla_{s}}{|\nabla s|^{2}}$, the variation of the mean curvature is exactly $-\frac{n-1}{s^{2}}$. In particular, for all $s$, we have
$$\left(\Delta^{s}+|A(s)|^{2}+\operatorname{Ric}(s)(N(s), N(s))\right)\left(u_{s}-1\right)=\frac{n-1}{s^{2}}-|A(s)|^{2}-\operatorname{Ric}(s)(N(s), N(s)),$$
According to Proposition 3, while $\left\|h_{s}-g^{\mathbb{S}^{n-1} / \Gamma}\right\|_{C^{1, \alpha}\left(g^{S^{n-1} / \Gamma}\right)}$ is sufficiently small, there exists $C=C(l)>0$ such that for all $s$,
$$\left\|\frac{A(s)}{s}-h_{s}\right\|_{C^{l, \alpha}\left(h_{s}\right)} \leqslant C \eta(s) .$$
Since $s^{2}|\operatorname{Ric}(s)(N(s), N(s))|<\eta(s)$, this implies that the right hand side of (25) satisfies: there exists $C=C(\alpha, n)>0$ such that for all $s$,
$$\left\|n-1-s^{2}|A(s)|^{2}-s^{2} \operatorname{Ric}(s)(N(s), N(s))\right\|_{C^{\alpha}\left(g^{\mathrm{S} n-1 / \Gamma}\right)} \leqslant C \eta(s) .$$
Likewise, for the left hand side, for any function $v: \mathbb{S}^{n-1} / \Gamma \rightarrow \mathbb{R}$ we have
$$\begin{aligned}
\| s^{2}\left(\Delta^{s}+|A(s)|^{2}+\operatorname{Ric}(s)(N(s), N(s))\right) v- & \left(\Delta^{\mathbb{S}^{n-1} / \Gamma}+n-1\right) v \|_{C^{\alpha}\left(g^{\mathbb{S}^{n-1} / \Gamma}\right)} \\
& \leqslant C \eta(s)\|v\|_{C^{2, \alpha}\left(g^{\mathrm{S} n-1 / \Gamma}\right)}
\end{aligned}$$

Since $\Delta^{\mathbb{S}^{n-1} / \Gamma}+n-1$ is invertible for $\Gamma \neq\{\mathrm{Id}\}$, we get by the inverse function theorem, Lemma 4.5, the following control: there exists $C=C(n, \alpha)>0$ such that for all $s$
$$\left\|u_{s}-1\right\|_{C^{2, \alpha}\left(g^{\mathbb{S}^{n-1} / \Gamma}\right)} \leqslant C \eta(s) .$$
Let us now show that for all $s \in\left[\rho_{1}, \rho_{2}\right],\left\|h_{s}-g^{\mathbb{S}^{n-1} / \Gamma}\right\|_{C^{1, \alpha}\left(g^{\mathrm{S} n-1} / \Gamma\right)}$ remains small. We will actually show that there exists $C=C(n, \alpha)>0$ such that $\left\|h_{s}-g^{\mathbb{S}^{n-1} / \Gamma}\right\|_{C^{1, \alpha}\left(g^{\mathbb{S}^{n-1} / \Gamma}\right)} \leqslant$ $C \eta(s)$. The expression (20) can be rewritten
$$\partial_{s}\left(h_{s}-g^{\mathbb{S}^{n-1} / \Gamma}\right)=\frac{2}{s}\left(u \frac{A^{s}}{s}-h_{s}\right),$$
but by the control (27), and Proposition 3, there exists $C=C(n, \alpha)>0$ such that we have $\left\|u \frac{A^{s}}{s}-h_{s}\right\|_{C^{1, \alpha}\left(g^{\mathrm{s} n-1} / \Gamma\right)} \leqslant C \eta(s)$. Recall that
$$\eta(s):=C \epsilon\left[\left(\frac{\rho_{1}}{s}\right)^{\beta_{1}}+\left(\frac{s}{\rho_{2}}\right)^{\beta_{2}}\right],$$
to deduce that for $\bar{\rho}<s_{0}<\rho_{2}$, we have
$$\begin{aligned}
\left\|h_{s_{0}}-g^{\mathbb{S}^{n-1} / \Gamma}\right\|_{C^{1, \alpha}\left(g^{\mathbb{S}^{n-1} / \Gamma}\right)} & \leqslant C\left(\eta(\bar{\rho})+\int_{\bar{\rho}}^{s_{0}} \frac{2}{s} \eta(s) d s\right) \\
& =C \eta(\bar{\rho})+\left(\frac{2 C \epsilon}{\rho_{2}^{\beta_{2}}} \int_{\bar{\rho}}^{s_{0}} s^{\beta_{2}-1} d s\right) \\
& =C \epsilon \frac{\bar{\rho}^{\beta_{2}}}{\rho_{2}^{\beta_{2}}}+\left(\frac{2 C \epsilon}{\rho_{2}^{\beta_{2}}}\left(s_{0}^{\beta_{2}}-\bar{\rho}^{\beta_{2}}\right)\right) \\
& \leqslant C \eta\left(s_{0}\right)
\end{aligned}$$
and similarly, for $\rho_{1}<s_{0}<\bar{\rho}$,
$$\left\|h_{s_{0}}-g^{\mathbb{S}^{n-1} / \Gamma}\right\|_{C^{1, \alpha}\left(g^{\mathbb{S}^{n-1} / \Gamma}\right)} \leqslant C \eta\left(s_{0}\right) .$$
To obtain controls on higher derivatives of $u$ and $h_{s}$, we use the other equalities of [HP99, Theorem 3.2]: according to (21), and the control (27), there exists $C=C(n, \alpha)$ such that for all $s$ we have
$$\left\|\partial_{s} N(s)\right\|_{C^{1, \alpha}\left(h_{s}\right)} \leqslant C \eta(s)$$
according to (22) and the controls (27), (26) and (28), and since the $l$-th derivatives of the curvature are bounded by $s^{-2-l} \eta(s)$, there exists $C=C(n, \alpha)>0$ such that for all $s$, we have:
$$\left\|\partial_{s}\left(\frac{A(s)}{s}\right)\right\|_{C^{\alpha}\left(h_{s}\right)} \leqslant C \eta(s) .$$

Differentiating the equality (23) with respect to $s$, and using the inequalities $\left\|\partial_{s} h_{s}\right\|_{C^{1, \alpha}\left(h_{s}\right)} \leqslant$ $C \eta(s)$, and (29), there exists $C=C(n, \alpha)>0$ such that for all $s$, we have:
$$\left\|\left(\Delta^{\mathbb{S}^{n-1} / \Gamma}+n-1\right) \partial_{s} u_{s}\right\|_{C^{\alpha}\left(h_{s}\right)} \leqslant C \eta(s) .$$
We can therefore conclude that for all $s,\left\|\partial_{s} u_{s}\right\|_{C^{2, \alpha}\left(h_{s}\right)} \leqslant C \eta(s)$.
Iterating this for higher derivatives in all directions, we obtain the stated controls. \(\square\)

\subsection*{6.3 Proximity between the Einstein metric and the naïve desingularization in weighted $C^{k}$-norm}

Now, to construct coordinates on the whole manifold $M$, we just "glue" the coordinates we have on each part together by using the local diffeomorphisms with the common asymptotic cone of each part. We obtain the following control for the metric.

Theorem 6.1 Let $D_{0}, v_{0}>0$ and $\left(M_{i}^{\mathcal{E}}, g_{i}^{\mathcal{E}}\right)$ a sequence of Einstein manifolds satisfying
\begin{itemize}
\item[-] the volume is bounded below by $v_{0}>0$,
\item[-] the diameter is bounded by $D_{0}$,
\item[-] the Ricci curvature is bounded $\mid$ Ric $\mid \leq 3$.
\end{itemize}
Then, there exists a subsequence with fixed topology $M=M_{i}^{\mathcal{E}}$ and a sequence of naïve desingularizations $\left(M, g_{t_{i}}^{D}\right)$ of an Einstein orbifold $\left(M_{o}, g_{o}\right)$ such that: for all $l \in \mathbb{N}$ and $i$ large enough, there exists $C\left(l, v_{0}, D_{0}\right)>0, \beta_{1}\left(v_{0}, D_{0}\right)>0$ and $\beta_{2}\left(v_{0}, D_{0}\right)>0$, $\epsilon_{i}>0, \epsilon_{i} \rightarrow 0$, and a diffeomorphism $\Phi_{i}: M \rightarrow M$ satisfying
\begin{itemize}
\item[(1)] on $\mathcal{M}_{o}\left(\epsilon_{i}\right)$, we have
$$\left\|\Phi_{i}^{*} g_{i}^{\mathcal{E}}-g_{o}\right\|_{C^{l}\left(g_{o}\right)} \leqslant C \epsilon_{i} .$$
\item[(2)] at the different scales $T_{i, j}$ (associated to $t_{i}$ ), on $\mathcal{N}_{j}\left(\epsilon_{i}\right)$ we have
$$\left\|\frac{\Phi_{i}^{*} g_{i}^{\mathcal{E}}}{T_{i, j}}-g_{b_{j}}\right\|_{C^{l}\left(g_{b_{j}}\right)} \leqslant C \epsilon_{i} .$$
\item[(3)] in the intermediate regions, $\mathcal{A}_{k}\left(t_{i}, \epsilon_{i}\right)$ included in a metric annulus of radii $\rho_{1}^{i, k}=$ $\frac{1}{8} T_{i, k}^{\frac{1}{2}} \epsilon_{i}^{-1}, \rho_{2}^{i, k}=8 T_{i, j}^{\frac{1}{2}} \epsilon_{i}$, for all $\rho_{1}^{i, k} \leqslant \rho \leqslant \frac{1}{2} \rho_{2}^{i, k}$, and denoting $\Phi_{i, \rho}=\Phi_{i} \circ \phi_{\rho}$, where $\phi_{\rho}$ is the homothetic transformation of ration $\rho$ on $\mathbb{R}^{4} / \Gamma_{k}$ with its flat metric $g_{e}$, we have
$$\left\|\frac{\Phi_{i, \rho}^{*} g_{i}^{\mathcal{E}}}{\rho^{2}}-g_{e}\right\|_{C^{l}\left(A_{e}(1,2)\right)} \leqslant C \epsilon_{i}\left[\left(\frac{\rho_{1}^{i, k}}{\rho}\right)^{\beta_{1}}+\left(\frac{\rho}{\rho_{2}^{i, k}}\right)^{\beta_{2}}\right] .$$
\end{itemize}

Remark 17 This is indeed much better than a $C^{\infty}$ convergence on compacts to a flat cone as we have $\left[\left(\frac{\rho_{1}^{i, k}}{\rho}\right)^{\beta_{1}}+\left(\frac{\rho}{\rho_{2}^{i, k}}\right)^{\beta_{2}}\right] \leqslant 2$, and a decay in the annulus.

\section*{A Optimal $C^{k, \alpha}$-proximity to a round sphere}

In this appendix, we are interested in metrics with pinched positive sectional curvatures and want to estimate how close to a round metric they have to be. To start with, a consequence of Cheeger-Gromov compactness is the following lemma, see [Pet98, Chapter 10] for instance.

Lemma A. 1 For all $n, 0<\alpha<1, \delta>0$ and $v_{0}>0$, there exists $\epsilon>0$ such that if $\left(M^{n}, g\right)$ satisfies
\begin{itemize}
\item[(1)] $1-\epsilon<\operatorname{Sec}(g)<1+\epsilon$,
\item[(2)] and $\operatorname{Vol}(M)>v_{0}$,
\end{itemize}
then, there exists $\Gamma$ a finite subgroup of $S O(n+1)$ (whose order is bounded by a function of $v_{0}$ ), and a diffeomorphism $\Phi: \mathbb{S}^{n} / \Gamma \rightarrow M$ for which:
$$\left\|\Phi^{*} g-g^{\mathbb{S}^{n} / \Gamma}\right\|_{C^{1, \alpha}\left(g^{\mathbb{S}^{n} / \Gamma}\right)} \leqslant \delta,$$
where $g^{\mathbb{S}^{n} / \Gamma}$ is a round metric on $\mathbb{S}^{n} / \Gamma$.
In this appendix, we will prove the following proposition.
Proposition 10 Let $\left(M, g_{0}\right)$ be a Riemannian manifold of dimension $n$ with sectional curvatures equal to 1 , and $k \in \mathbb{N}$. Then, there exists $\delta>0$ and $C>0$, such that if a metric $g$ on $M$ satisfies:
$$\left\|g-g_{0}\right\|_{C^{1, \alpha}\left(g_{0}\right)} \leqslant \delta,$$
then, there exists a diffeomorphism $\Phi: M \rightarrow M$, for which
$$\left\|\Phi^{*} g-g_{0}\right\|_{C^{k+1, \alpha}\left(g_{0}\right)} \leqslant C\|\operatorname{Ric}(g)-(n-1) g\|_{C^{k}\left(g_{0}\right)} .$$
As an immediate consequence of Lemma A. 1 and Proposition 10, we get the following statement.

Corollary 3 For all $n, 0<\alpha<1$ and $v_{0}>0$, there exists $\epsilon_{0}>0$ and $C>0$ such that for any $0<\epsilon<\epsilon_{0}$, if $\left(M^{n}, g\right)$ satisfies:
\begin{itemize}
\item[(1)] $1-\epsilon<\operatorname{Sec}(g)<1+\epsilon$,
\item[(2)] and $\operatorname{Vol}(M, g)>v_{0}$,
\end{itemize}
then, there exists $\Gamma$ a finite subgroup of $S O(n+1)$, and a diffeomorphism $\Phi: \mathbb{S}^{n} /$ $\Gamma \rightarrow M$ for which
$$\left\|\Phi^{*} g-g_{0}\right\|_{C^{1, \alpha}\left(g_{0}\right)} \leqslant C \epsilon .$$

Remark 18 The crucial part for us is that the $\epsilon$ in the final estimate is the same as in the assumption $1-\epsilon<\operatorname{Sec}(g)<1+\epsilon$.

Proof of Proposition 10 Let $\left(M^{n}, g_{0}\right)$ be a Riemannian manifold whose sectional curvatures are constant equal to 1 . For $\lambda:=\frac{(n-2)(n-1)}{2}$, define the operator
$$E_{g_{0}}(g):=\operatorname{Ric}(g)-\frac{\operatorname{R}(g)}{2} g+\lambda g+\delta_{g}^{*} \delta_{g_{0}} g .$$
Then, following [And10, Section 5], by [Ebi70] and by the Bianchi identity, there exists $\delta>0$ such that $E_{g_{0}}^{-1}(\{0\}) \cap B_{C^{1, \alpha}}(\delta)$ is exactly the set of Einstein metrics with constant $\Lambda$ which are in divergence-free gauge with respect to $g_{0}$ and have same volume.

Let $g$ be a metric on $M$ such that $\left\|g-g_{0}\right\|_{C^{k+1, \alpha}\left(g_{0}\right)} \leqslant \delta$ for $\delta>0$ a constant which we will choose small enough in the rest of the proof. According to [Ebi70], for $\delta$ small enough, there exists a diffeomorphism $\Phi: M \rightarrow M$ such that
$$\delta_{g_{0}} \Phi^{*} g=0 .$$
Hence, we have
$$\left\|E_{g_{0}}\left(\Phi^{*} g\right)\right\|_{C^{k}\left(g_{0}\right)} \leqslant\|\operatorname{Ric}(g)-(n-1) g\|_{C^{k}\left(g_{0}\right)} .$$
Now, by [Bes87, Corollary 12.72 (Bourguignon, unpublished)], the linearization of $E$ at $g_{0}$ is invertible (see again [And10, Section 5] for the adaptation to the operator $E$ ) and by the inverse function theorem Lemma 4.5 we deduce that for $\delta$ small enough, and for all $1 \leqslant p<+\infty$ and $k \in \mathbb{N}$ there exists $C>0$, such that we have
$$\left\|\Phi^{*} g-g_{0}\right\|_{W^{k+2, p}\left(g_{0}\right)} \leqslant C\left\|E_{g_{0}}\left(\Phi^{*} g\right)\right\|_{W^{k, p}\left(g_{0}\right)},$$
and finally, by (30), we have
$$\left\|\Phi^{*} g-g_{0}\right\|_{C^{k+1, \alpha}\left(g_{0}\right)} \leqslant C\|\operatorname{Ric}(g)-(n-1) g\|_{C^{k}\left(g_{0}\right)},$$
because on the sphere, for $p$ large enough, $W^{k+2, p}\left(g_{0}\right)$ embeds continuously in $C^{k+1, \alpha}\left(g_{0}\right)$, and so does $C^{k}\left(g_{0}\right)$ in $W^{k, p}\left(g_{0}\right)$. \(\square\)

\section*{References}
[And89] M.T. Anderson, Ricci Curvature Bounds and Einstein Metrics on Compact Manifolds. J. Amer. Math. Soc. 2 (1989), no. 3, 455\{490.
[And10] M.T. Anderson, A survey of Einstein metrics on 4-manifolds. Handbook of geometric analysis, No. 3, 1\{39, Adv. Lect. Math. (ALM), 14, Int. Press, Somerville, MA, 2010.
[BKN89] S. Bando ; A. Kasue ; H. Nakajima, On a construction of coordinates at infinity on manifolds with fast curvature decay and maximal volume growth. Invent. Math. 97 (1989), no. 2, 313\{349.
[Ban90] S. Bando, Bubbling out of Einstein manifolds. Tohoku Math. J. (2) 42 (1990), no. 2, 205\{216.
[Bes87] A.L. Besse, Einstein manifolds, Ergebnisse der Mathematik und ihrer Grenzgebiete (3) [Results in Mathematics and Related Areas (3)], 10. Springer-Verlag, Berlin, 1987.
[Biq13] O. Biquard, Désingularisation de métriques d'Einstein. I. Invent. Math. 192 (2013), no. 1, 197\{252.
[Biq16] O. Biquard, Désingularisation de métriques d'Einstein. II. Invent. Math. 204 (2016), no. 2, 473\{504.
[CC96] J. Cheeger ; T.H. Colding, Lower bounds on Ricci curvature and the almost rigidity of warped products. Ann. of Math. (2) 144 (1996), no. 1, 189\{237.
[CGT82] J. Cheeger ; M.Gromov ; M. Taylor, Finite propagation speed, kernel estimates for functinos of the laplace operator, and the geometry of complete Riemannian manifolds. J. Differential Geom. 17 (1982), no. 1, 15\{53.
[CN15] J. Cheeger; A. Naber, Regularity of Einstein Manifolds and the Codimension 4 Conjecture. Ann. of Math. (2) 182 (2015), no. 3, 1093\{1165.
[CEV17] O. Chodosh ; M. Eichmair ; A. Volkmann, Isoperimetric structure of asymptotically conical manifolds. J. Differ. Geom. 105 (2017), 1\{19.
[Cro80] C. Croke, Some isoperimetric inequalities and eigenvalue estimates. Ann. Sci. École Norm. Sup. (4) 13 (1980), no. 4, 419\{435.
[Col97] T.H. Colding, Ricci Curvature and Volume Convergence. Ann. of Math. (2) 145 (1997), no. 3, 477\{501.
[Ebi70] David G. Ebin, The manifold of Riemannian metrics, 1970 Global Analysis (Proc. Sympos. Pure Math., Vol. XV, Berkeley, Calif., 1968) pp. 11\{40 Amer. Math. Soc., Providence, R.I.
[Fol89] G.B. Folland, Harmonic analysis of the de Rham complex on the sphere. Reine Angew. Math. 398 (1989), 130\{143.
[Gao90] L. Gao, Einstein metrics. J. Diff. Geom. 32 (1990), 155-183.
[Gro81] M. Gromov, Structures métriques pour les variétés riemanniennes. Textes Mathématiques Paris (1981), 1-120. (rédigé par Lafontaine et Pansu). (in French)
[HP99] G. Huisken ; A. Polden, Geometric evolution equations for hypersurfaces. Calculus of variations and geometric evolution problems (Cetraro, 1996),45\{84. Lecture Notes in Math., 1713, Springer, Berlin, 1999
[Kro89] P.B. Kronheimer, The construction of ALE spaces as hyper-Kähler quotients. J. Differential Geom. Volume 29, Number 3 (1989), 665-683.
[Nak90] H. Nakajima, Self-Duality of ALE Ricci-Flat 4-Manifolds and Positive Mass Theorem. Adv. Stud. Pure Math. Recent Topics in Differential and Analytic Geometry, T. Ochiai, ed. (Tokyo: Mathematical Society of Japan, 1990), 385-396
[Ozu19b] T. Ozuch, Noncollapsed degeneration of Einstein 4-manifolds II. preprint.
[PX09] F. Pacard ; X. Xu, Constant mean curvature spheres in Riemannian manifolds. Manuscripta Mathematica. 128, 3 (2009), 275-295
[Pet98] P. Petersen, Riemannian geometry, New York Springer cop. 1998, Graduate texts in mathematics 171
[Suv11] I. Suvaina, ALE Ricci-flat Kähler metrics and deformations of quotient surface singularities. Ann. Global Anal. Geom. 41 (2012), no. 1, 109\{123.
[Ye96] R. Ye, Constant mean curvature foliation: singularity structure and curvature estimate. Pacific J. Math. Volume 174, Number 2 (1996), 569-587.

MIT, Dept. of Math., 77 Massachusetts Avenue, Cambridge, MA 02139-4307.
```
ozuch@mit.edu
https://tristanozuch.github.io/
```
