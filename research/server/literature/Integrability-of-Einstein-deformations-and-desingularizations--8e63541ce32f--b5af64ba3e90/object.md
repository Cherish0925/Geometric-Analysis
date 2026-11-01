# Integrability of Einstein deformations and desingularizations

- Category: papers
- Identity: arxiv:2105.13193
- Content status: fulltext_ok

---

---
source_file: 2105_13193.pdf
converter: mathpix
format: mmd
---

\title{
INTEGRABILITY OF EINSTEIN DEFORMATIONS AND DESINGULARIZATIONS
}

\author{
Tristan Ozuch \\ Massachusetts Institute of Technology
}

\begin{abstract}
We study the question of the integrability of Einstein deformations and relate it to the question of the desingularization of Einstein metrics. Our main application is a negative answer to the long-standing question of whether or not every Einstein 4-orbifold (which is an Einstein metric space in a synthetic sense) is limit of smooth Einstein 4-manifolds. We more precisely show that spherical and hyperbolic 4-orbifolds with the simplest singularities cannot be Gromov-Hausdorff limits of smooth Einstein 4metrics without relying on previous integrability assumptions. For this, we analyze the integrability of deformations of Ricci-flat ALE metrics through variations of Schoen's Pohozaev identity. Inspired by Taub's preserved quantity in General Relativity, we also introduce preserved integral quantities based on the symmetries of Einstein metrics. These quantities are obstructions to the integrability of infinitesimal Einstein deformations "closing up" inside a hypersurface - even with change of topology. We show that many previously identified obstructions to the desingularization of Einstein 4-metrics are equivalent to these quantities on Ricci-flat cones. In particular, all of the obstructions to desingularizations bubbling out Eguchi-Hanson metrics are recovered. This lets us further interpret the obstructions to the desingularization of Einstein metrics as a defect of integrability.
\end{abstract}

\section*{Contents}

Introduction
Completion of the moduli space of Einstein 4-manifolds
Preserved quantities and integrability
Einstein deformations of Ricci-flat cones
Vanishing of the obstructions in dimension 4
Obstruction to the desingularization of Einstein 4-manifolds
Desingularization of spherical and hyperbolic orbifolds
Acknowledgements
1. Symmetries of Einstein metrics and integrability
1.1. Gauge and reparametrization properties
1.2. Taub's preserved quantities and obstructions
1.3. Integrability of Einstein deformations
2. Preserved quantities on Ricci-flat cones and integrability
2.1. A preserved quantity on $\mathbb{R}^{d}$ and other Ricci-flat cones
2.2. Deformations with constant scalar curvature
2.3. Einstein metrics closing-up inside a hypersurface
3. The 4-dimensional situation
3.1. Notations
3.2. Asymptotic curvature of 4-dimensional Ricci-flat ALE metrics
4. Obstruction to the desingularization of Einstein metrics
4.1. Infinitesimal Einstein deformations of Ricci-flat ALE metrics
4.2. Obstructions to the desingularization
4.3. Spherical and hyperbolic orbifolds
4.4. Higher dimensional Einstein orbifolds with isolated singularities
Appendix A. Development of Einstein 4-metrics
A.1. A local gauge for Einstein metrics
A.2. Vanishing of the obstructions to Einstein deformations
Appendix B. Function spaces and analyticity on ALE spaces
B.1. Function spaces
B.2. Real-analytic dependence of Einstein modulo obstructions metrics
References

Introduction
An Einstein metric g satisfies, for some real number $\Lambda$, the equation
$$\operatorname{Ric}(\mathbf{g})=\Lambda \mathbf{g} .$$
In dimension 4, these metrics are considered optimal due to the homogeneity of their Ricci curvature but also as critical points of the Einstein-Hilbert functional with fixed volume, $g \mapsto \int_{M} \mathrm{R}_{g} d v_{g}$, and more importantly as minimizers of the $L^{2}$-norm of the Riemann curvature tensor, $g \mapsto \int_{M}\left|\operatorname{Rm}_{g}\right|^{2} d v_{g}$ often interpreted as an energy.

From dimension 4, even under natural assumptions of bounded diameter (compactness) and lower bound on the volume (non-collapsing) Einstein metrics can develop singularities. This first issue means that the set of unit-volume Einstein metrics is not complete for the usual Gromov-Hausdorff distance. Moreover, it has been proven that some infinitesimal Einstein deformations may not integrate into curves of actual Einstein metrics in dimension higher than 4. This second issue shows that the moduli space of Einstein metrics itself might have singularities.

In this article, we exhibit links between the two seemingly unrelated above issues and apply the resulting analogy to the question of the desingularization of Einstein 4-manifolds.

Completion of the moduli space of Einstein 4-manifolds. One major goal for 4-dimensional geometry is to understand the structure of the compactification of the moduli space of Einstein metrics on a differentiable manifold $M^{4}$ which is defined as
$$\mathbf{E}\left(M^{4}\right):=\left\{\left(M^{4}, \mathbf{g}\right) \mid \exists \Lambda \in \mathbb{R}, \operatorname{Ric}(\mathbf{g})=\Lambda \mathbf{g}, \operatorname{Vol}\left(M^{4}, \mathbf{g}\right)=1\right\} / \mathcal{D}\left(M^{4}\right),$$
where $\mathcal{D}\left(M^{4}\right)$ is the group of diffeomorphisms of $M^{4}$ acting on metrics by pull-back. This space is classically equipped with the Gromov-Hausdorff distance, $d_{G H}$. The metric spaces which are limits of Einstein 4-manifolds with uniformly controlled diameter and volume, as well as the associated singularity models, have been understood for a long time in the Gromov-Hausdorff sense [And89, BKN89]: they are respectively Einstein orbifolds and Ricci-flat ALE orbifolds. The metric completion of $\left(\mathbf{E}\left(M^{4}\right), d_{G H}\right)$ is
$$\mathbf{E}\left(M^{4}\right) \cup \partial_{o} \mathbf{E}\left(M^{4}\right),$$
where $\partial_{o} \mathbf{E}\left(M^{4}\right)$ is the set of $d_{G H}$-limits with bounded diameter (i.e. at finite $d_{G H}$-distance) of Einstein metrics on $M^{4}$.

The elements of $\partial_{o} \mathbf{E}\left(M^{4}\right)$ are Einstein orbifolds and a question which we answer here is the converse. Quoting Anderson [And10]: "It has long been an open question whether Einstein orbifold metrics can be resolved to smooth Einstein metrics close to them in the Gromov-Hausdorff topology." We will prove that this resolution is not possible for some of the simplest Einstein orbifolds: the spherical an hyperbolic ones. These orbifolds should therefore not really be considered as singular Einstein metrics. In order to prove this, we
use the analogy between such a resolution and an Einstein deformation of a flat cone, and we study the potential nonintegrability of Ricci-flat ALE deformations.

Preserved quantities and integrability. Let $\mathbf{g}$ be an Einstein manifold on an open subset $\mathcal{U}$ of a manifold. We say that $h$ is an infinitesimal Einstein deformation of $\mathbf{g}$ on $\mathcal{U}$ if the perturbation $t \mapsto \mathbf{g}+t h$ satisfies (1) at the infinitesimal level as $t \rightarrow 0$. We say that $h$ is an integrable Einstein deformation if on any compact in $\mathcal{U}$, there exists a smooth curve $t \in[0,1] \mapsto \mathbf{g}_{t}$ such that
\begin{itemize}
\item[-] $\mathbf{g}_{0}=\mathbf{g}$,
\item[-] $\partial_{t} \mathbf{g}_{t \mid t=0}=h$, and
\item[-] for any $t, \mathbf{g}_{t}$ satisfies (1) with constant $\Lambda(t) \in \mathbb{R}$.
\end{itemize}
It is clear that an integrable Einstein deformation is an infinitesimal Einstein deformation, but the converse is a very delicate question and is not always true. Counter-examples were found in [Koi82] in dimension strictly higher than 4.

The question of integrability of Einstein deformations is crucial in understanding the structure of the moduli space of Einstein metrics, and a major question is whether or not such a moduli space can be really singular, see [Bes87, 12.10]. It is also crucial for the behavior of Ricci flow near Einstein metrics: in the compact situation, having integrable deformations ensures optimal rates of convergence or divergence, see for instance [Has12, HM14]. In the noncompact situation, this moreover seems to be a necessary condition for the dynamical stability of Ricci-flat ALE metrics, see [KP20, DO20, DO21].

In the Lorentzian context of General Relativity, it has been proven that the question of integrability of Einstein deformations was completely ruled by the presence of symmetries.

Let us denote $\mathrm{E}_{\mathrm{g}}^{(2)}(h, h)$ the quadratic terms terms in the development of the Einstein tensor $h \mapsto \mathrm{E}(\mathbf{g}+h):=\operatorname{Ric}(\mathbf{g}+h)-\frac{\mathrm{R}(\mathbf{g}+h)}{2}(\mathbf{g}+h)$. For any Killing vector field $X$, a hypersurface $\Sigma$ with a unit normal $n_{\Sigma}$ and any infinitesimal Einstein deformation $h$, we define Taub's preserved quantity:
$$\mathcal{T}_{X}^{\Sigma}(h, h):=\int_{\Sigma}\left(\mathrm{E}_{\mathbf{g}}^{(2)}(h, h)\right)\left(X, n_{\Sigma}\right) d v_{\Sigma} .$$
The link with the integrability of $h$ is that if $h$ is an integrable Ricci-flat deformation, then $\mathcal{T}_{X}^{\Sigma}(h, h)$ has to vanish. In this sense, Taub's preserved quantities for all Killing vector fields $X$ are obstructions to the integrability of $h$.

A remarkable and beautiful result is that in the Lorentzian context, the above obstructions are the only obstructions to the integrability of $h$, see [FMM80, AMM82]. Namely, if they vanish, then, under mild assumptions, one can construct a smooth curve of Ricci-flat metrics starting at g whose first jet is $h$. The hyperbolic nature of the Einstein equations in the Lorentzian context is an important aspect of the proof.

Einstein deformations of Ricci-flat cones. Let $\left(C(S), \mathbf{g}_{C(S)}\right)=\left(\mathbb{R}^{+} \times S, d r^{2}+r^{2} \mathbf{g}_{S}\right)$ be a $d$-dimensional Ricci-flat cone with link $\left(S, \mathbf{g}_{S}\right)$ satisfying $\operatorname{Ric}\left(\mathbf{g}_{S}\right)=(d-2) \mathbf{g}_{S}$. Such cones model the asymptotics of Einstein metrics at given points or at infinity. We will mostly focus on the usual Euclidean cone $\left(\mathbb{R}^{d}, \mathbf{e}\right)=\left(C\left(\mathbb{S}^{d-1}\right), \mathbf{g}_{C\left(\mathbb{S}^{d-1}\right)}\right)$ and its quotients.

We extend the obstructions given by Taub's preserved quantities on the hypersurface $\Sigma=S$ to general Einstein deformations (not necessarily Ricci-flat this time). The condition rewrites: for any Killing vector field $X$ of $\left(S, \mathbf{g}_{S}\right)$, if $h$ is integrable, then one has
$$\mathcal{T}_{X}^{S}(h, h)=\int_{S}\left(\operatorname{Ric}_{\mathbf{g}_{C(S)}}^{(2)}(h, h)\right)\left(X, \partial_{r}\right) d v_{S}=0$$
where Ric is the traceless part of Ric and Ric ${ }^{(2)}$ its second order variations.

We moreover introduce a similar quantity based on the conformal Killing vector field $r \partial_{r}$ on the cone $C(S)$.

Theorem 0.1 (Informal, Proposition 2.3). Let $h$ be an infinitesimal Einstein deformation of the Ricci-flat cone $\left(C(S), \mathbf{g}_{C(S)}\right)$. Assume that $h$ is either defined and bounded on the interior of $S$ or on its exterior and decaying at infinity. Then, we have the following identity:
$$\int_{S}\left(\operatorname{Ric}_{\mathbf{g}_{C(S)}}^{(2)}(h, h)\right)\left(r \partial_{r}, \partial_{r}\right) d v_{S}+\text { other terms }=0 .$$
In all of our situations of interest, we are able to find convenient gauges for $h$ in which these other terms vanish thanks to some variations of Schoen's Pohozaev formula from [Sch88].

Remark 0.2. In the above case, we do not need to assume that $h$ is integrable. This should rather be thought of as an obstruction to the existence of an Einstein metric which closes up inside $S$, that is the existence of an Einstein deformation on a compact domain whose only boundary is $S$.

As is well-known, a difficulty when considering deformations of cones is verifying that the resulting curve of metric is complete, see [BL20] where this is discussed for hyperkähler deformations of cones. The main challenge is that such deformations typically require changes of topology. When allowing a change of topology, just as in the desingularization of Einstein 4-manifolds, one needs to consider deformations of $\mathbb{R}^{4} / \Gamma$ with topology $N=\left(\mathbb{R}^{4} /\right.$ $\Gamma) \backslash\{0\} \cup \Sigma$ for some lower dimensional manifold $\Sigma$. The prototypical example is that of the Eguchi-Hanson metric which can be seen as an Einstein deformation of $\mathbb{R}^{4} / \mathbb{Z}_{2}$ on $T^{*} \mathbb{S}^{2}=\left(\mathbb{R}^{4} / \mathbb{Z}_{2}\right) \backslash\{0\} \cup \mathbb{S}^{2}$. Here, we may see the Euclidean metric e on $\mathbb{R}^{4} / \mathbb{Z}_{2}$ as living on $T^{*} \mathbb{S}^{2}$ while being degenerate on $\mathbb{S}^{2}$, that is the restriction of $\mathbf{e}$ to the submanifold $\mathbb{S}^{2}$ vanishes.

In Section 2.3, we discuss the situation of an Einstein metric coming out of $\mathbb{R}^{4} / \mathbb{Z}_{2}$ and closing-up inside with topology $T^{*} \mathbb{S}^{2}$. Assume that there exists a smooth curve of nondegenerate Einstein metrics $t \in[0,1] \mapsto \mathbf{g}_{t}$ on $\left(B_{\mathbf{e}}(0,1) \backslash\{0\}\right) \cup \mathbb{S}^{2} \subset T^{*} \mathbb{S}^{2}$ with $\mathbf{g}_{0}=\mathbf{e}$ and $\partial_{t \mid t=0} \mathbf{g}_{t}=h$ outside $\mathbb{S}^{2}$ in well-chosen coordinates. Then we have the obstructions:
$$\int_{\mathbb{S}^{3} / \mathbb{Z}_{2}}\left(\operatorname{Ric}_{\mathbf{e}}^{(2)}(h, h)\right)\left(r \partial_{r}, \partial_{r}\right) d v_{\mathbb{S}^{3} / \mathbb{Z}_{2}}=0,$$
and the similar ones from Killing vector fields. In that situation, an Eguchi-Hanson metric bubbles-out of the cone $\mathbb{R}^{4} / \mathbb{Z}_{2}$ and the link with the question of desingularization becomes clear. For some related results about hyperkähler metrics on manifolds with boundaries, see [FLS17, Biq19].

A natural question would be whether one could find similar obstructions on typical cones of dimension higher than 4 with codimension 4 singularities.

Question 0.3. Can we find similar obstructions for Einstein deformations of cones on singular Einstein orbifolds like $\mathbb{R}^{k} \times\left(\mathbb{R}^{4} / \mathbb{Z}_{2}\right)$ for $k \geqslant 1$ ?

Vanishing of the obstructions in dimension 4. We then test the conditions (5) and (6) considering simple Einstein deformations coming from two situations: the rescaling of Einstein metrics at a given point, and the rescaling of Ricci-flat ALE metrics at infinity, and show that they vanish for arbitrary deformations.

The vanishing of the obstructions is not surprising in the case of Einstein metrics around a given point: it has been shown that for any curvature satisfying the Einstein condition at the given point, there exists a germ of Einstein metric with the corresponding curvature
in [Gas82]. It implies that the obstructions (5) and (7) in this situation actually vanish in any dimension.

These results in Section 3 and the Appendix A can also be seen as consequences of [And08]. Their proofs have the merit to introduce natural systems of coordinates in which the computations of the quadratic terms of Ricci curvature are convenient (and where the other terms of (7) are vanishing), we note that the ALE coordinates considered are based on [BH19]. These coordinates are crucial for the next case of the desingularization of an Einstein orbifold, where the obstructions do not vanish.

Obstruction to the desingularization of Einstein 4-manifolds. We finally study the degeneration of Einstein 4-manifolds, that is the $d_{G H-\text { convergence of metrics in }} \mathbf{E}(M)$ to the boundary $\partial_{o} \mathbf{E}(M)$, and its reverse operation: the desingularization. Given an element in $\partial_{o} \mathbf{E}(M)$, the desingularization consists in finding a $d_{G H}$-approximating sequence of metrics in $\mathbf{E}(M)$.

Any smooth Einstein 4-manifold close to a compact Einstein orbifold in a mere Gromov-Hausdorff sense has been recently been produced by a gluing-perturbation procedure [Ozu19a, Ozu19b]. Here, this lets us understand the obstructions to the $d_{G H}$-desingularization of an Einstein orbifold through obstructions similar to (5) and (7).

Theorem 0.4 (Theorem 4.6). Assume that there exists a sequence of Einstein metrics $\left(M, \mathbf{g}_{n}\right)_{n}$ converging in the Gromov-Hausdorff sense to an Einstein orbifold $\left(M_{o}, \mathbf{g}_{o}\right)$ with a singularity $\mathbb{R}^{4} / \Gamma$ at $p$ and satisfying $\operatorname{Ric}\left(\mathbf{g}_{o}\right)=\Lambda \mathbf{g}_{o}$. Assume that there exist numbers $t_{n}>$ 0 such that at $p,\left(M, \mathbf{g}_{n} / t_{n}\right)_{n}$ converges to a Ricci-flat ALE manifold $\left(N, \mathbf{g}_{b}\right)$ asymptotic to $\mathbb{R}^{4} / \Gamma$ with integrable infinitesimal deformations. Consider the following asymptotics in well-chosen gauges (in a so-called volume gauge for $\mathbf{g}_{b}$ ):
$$\mathbf{g}_{o}=\mathbf{e}+H_{2}+\mathcal{O}\left(r^{3}\right) \quad \text { and } \quad \mathbf{g}_{b}=\mathbf{e}+H^{4}+\mathcal{O}\left(r^{-5}\right),$$
for $\left|H_{2}\right|_{\mathbf{e}} \sim r^{2}$ and $\left|H^{4}\right|_{\mathbf{e}} \sim r^{-4}$.
Then, the following obstructions analogous to (5) and (7) hold: for any $Y$ Killing vector field of $\mathbb{R}^{4} / \Gamma$ :
$$\int_{\mathbb{S}^{3} / \Gamma}\left(\operatorname{Ric}_{\mathbf{e}}^{(2)}\left(H^{4}, H_{2}\right)\right)\left(Y, \partial_{r}\right) d v_{\mathbb{S}^{3} / \Gamma}=0$$
and
$$\int_{\mathbb{S}^{3} / \Gamma}\left(\operatorname{Ric}_{\mathbf{e}}^{(2)}\left(H^{4}, H_{2}\right)\right)\left(r \partial_{r}, \partial_{r}\right) d v_{\mathbb{S}^{3} / \Gamma}=0$$

Comparing (5) to (8) and (7) to (9), we therefore interpret the obstructions to the desingularization of an Einstein orbifold as a defect of integrability of the infinitesimal Einstein deformation $h=H_{2}+H^{4}$. The proof of these different obstructions actually relies on the control of the same integration by parts as Theorem 0.1 once one notices that in so-called volume gauge, the vector field $r \partial_{r}$ is $\mathbf{g}_{b}$-harmonic at an order higher than expected.

Remark 0.5. Denote $\mathcal{V}\left(\mathbf{g}_{b}\right)<0$ the reduced volume of $\left(N, \mathbf{g}_{b}\right)$ introduced in [BH19], as well as $W_{\mathbf{g}_{o}}^{ \pm}$the Weyl curvatures of $\mathbf{g}_{o}$ at $p$ and $W_{\mathbf{g}_{b}}^{ \pm}$the asymptotic Weyl curvatures (the part decaying like $r^{-6}$ ) of $\mathbf{g}_{b}$, then (9) may rewrite as:
$$\Lambda \mathcal{V}\left(\mathbf{g}_{b}\right)+Q\left(W_{\mathbf{g}_{b}}^{+}, W_{\mathbf{g}_{o}}^{-}\right)+Q\left(W_{\mathbf{g}_{b}}^{-}, W_{\mathbf{g}_{o}}^{+}\right)=0$$
for some explicit quadratic form $Q$. A similar rewriting of (8) yields $Q^{\prime}\left(W_{\mathbf{g}_{b}}^{+}, W_{\mathbf{g}_{o}}^{-}\right)+$ $Q^{\prime}\left(W_{\mathbf{g}_{b}}^{-}, W_{\mathbf{g}_{o}}^{+}\right)=0$ for some other explicit quadratic form $Q^{\prime}$.

Remark 0.6. For $\mathbf{g}_{o}$ either spherical of hyperbolic, one has $\Lambda \neq 0$ and $W_{\mathbf{g}_{o}}^{ \pm}=0$. The obstruction (10) is therefore never satisfied. We also recover that the obstruction vanishes
for the gluing of a hyperkähler ALE to a hyperkähler ALE since $\Lambda=0, W_{\mathbf{g}_{o}}^{+}=0$ and $W_{\mathbf{g}_{b}}^{+}=0$.

We recover all of the obstructions to the desingularization by Eguchi-Hanson metrics identified in [Biq13], see Corollary 4.10 and an extension to higher dimension yields the obstruction of [MV16] as well, see Corollary 4.17. In these articles, the obstructions were purely analytical as projections on the cokernel of the linearized operator. Theorem 0.4 gives a new maybe more geometric interpretation of them.

Remark 0.7. There are higher order obstructions to the existence of Einstein deformations with asymptotic developments $\mathbf{g}_{t}=\mathbf{g}+t h_{1}+t^{2} h_{2}+\ldots$ for small $t$ which are very similar to the obstructions (9) and (8).

Question 0.8. Can these higher order obstructions recover the higher order obstructions of [Ozu20]? Can they help compute even higher order obstructions?

Desingularization of spherical and hyperbolic orbifolds. We next get to the main application of this article. We answer negatively the classical question of whether or not all Einstein 4-orbifolds can be $d_{G H}$-desingularized by smooth Einstein 4-manifolds.
Theorem 0.9. A spherical or hyperbolic 4-orbifold with at least one singularity $\mathbb{R}^{4} / \mathbb{Z}_{2}$ cannot be limit of smooth Einstein metrics in the Gromov-Hausdorff sense.
Example 0.10. Consider $\mathbb{S}^{4} \subset \mathbb{R}^{5}$ and the quotient by $\mathbb{Z}_{2}$ given by $\left(x_{1}, x_{2}, x_{3}, x_{4}, x_{5}\right) \sim$ $\left(x_{1},-x_{2},-x_{3},-x_{4},-x_{5}\right)$. We will denote this space $\mathbb{S}^{4} / \mathbb{Z}_{2}$ which is an Einstein orbifold with two $\mathbb{R}^{4} / \mathbb{Z}_{2}$ singularities. It is often called the American football metric. It is a synthetic Einstein space in the sense of [Nab13] for instance. By the above Theorem 0.9, it cannot be a Gromov-Hausdorff limit of smooth Einstein metrics.

Theorem 0.9 was conjectured in the author's PhD thesis [Ozu20t] where it was proven under a technical assumption of integrability for the Ricci-flat ALE spaces. The main remaining difficulty here is thus to deal with the potential non integrability of these deformations. We more precisely prove that Theorem 0.4 holds without the integrability assumption on the Ricci-flat ALE spaces. Remark 0.6 then lets us conclude.

Remark 0.11. It is often conjectured that the only Ricci-flat ALE metrics are Kähler, hence integrable. However, the motivation of this conjecture formulated in [BKN89] for instance, seems to be the analogous conjecture for the selfduality of Yang-Mills connections on SU (2) bundles over $\mathbb{S}^{4}$. This analogous conjecture was disproved the same year in [SSU89].

Let us present the main step of the proof of Theorem 0.9 which is of independent interest. Let $\left(N, \mathbf{g}_{b}\right)$ be a Ricci-flat ALE orbifold asymptotic to $\mathbb{R}^{4} / \Gamma$ for $\Gamma \subset S O(4)$. Its space of $L^{2}$-infinitesimal deformations which are traceless and in divergence-free gauge is denoted $\mathbf{O}\left(\mathbf{g}_{b}\right)$. There are particular elements in $\mathbf{O}\left(\mathbf{g}_{b}\right)$ coming from the symmetries of the asymptotic cone $\mathbb{R}^{4} / \Gamma$. According to [Ozu20t]:
\begin{itemize}
\item[-] there exists $X$ a harmonic vector field on $\left(N, \mathbf{g}_{b}\right)$ asymptotic to the conformal Killing vector field $r \partial_{r}$, and $\left(\mathcal{L}_{X} \mathbf{g}_{b}\right)^{\circ} \in \mathbf{O}\left(\mathbf{g}_{b}\right)$, where for a symmetric 2-tensor $h$, $(h)^{\circ}$ denotes the traceless part of $h$,
\item[-] for any Killing vector field $Y$ there exists $Y^{\prime}$ a harmonic vector field on $\left(N, \mathbf{g}_{b}\right)$ asymptotic to $Y$, and $\mathcal{L}_{Y^{\prime}} \mathbf{g}_{b} \in \mathbf{O}\left(\mathbf{g}_{b}\right)$.
\end{itemize}

The main step in the proof of Theorem 0.9 is to show that these deformations which are elements of the kernel of the linearization of the Ricci curvature should not be thought of as elements of the cokernel when dealing with Ricci-flat ALE deformations, at least at leading order. More precisely, for $v \in \mathbf{O}\left(\mathbf{g}_{b}\right)$, let us consider $g_{v}$ the unique solution to:
$$\boldsymbol{\Phi}_{\mathbf{g}_{b}}\left(g_{v}\right)=\mathrm{E}\left(g_{v}\right)+\delta_{\mathbf{g}_{b}}^{*} \delta_{\mathbf{g}_{b}} g_{v} \in \mathbf{O}\left(\mathbf{g}_{b}\right) .$$
satisfying $g_{v}-\left(\mathbf{g}_{b}+v\right) \perp_{L^{2}\left(\mathbf{g}_{b}\right)} \mathbf{O}\left(\mathbf{g}_{b}\right)$. We call Einstein modulo obstructions metrics such deformations which have been constructed in [Ozu19b] (see also [Koi83] in the smooth compact case). We study the leading order of the obstruction along curves $s \mapsto g_{s v}$ for $s \in(-1,1)$ at $s=0$.

Proposition 0.12. Let $\left(N, \mathbf{g}_{b}\right)$ be a Ricci-flat ALE metric which has nonintegrable Ricciflat $A L E$ deformations. Then, for any $v \in \mathbf{O}\left(\mathbf{g}_{b}\right)$, there exists $l \geqslant 2$ such that $\partial_{s^{k} \mid s=0}^{k} \boldsymbol{\Phi}_{\mathbf{g}_{b}}\left(g_{s v}\right)=$ 0 for all $k \leqslant l-1$ and $\partial_{s^{l} \mid s=0}^{l} \boldsymbol{\Phi}_{\mathbf{g}_{b}}\left(g_{s v}\right) \neq 0$. The leading order obstruction $\partial_{s^{l} \mid s=0}^{l} \boldsymbol{\Phi}_{\mathbf{g}_{b}}\left(g_{s v}\right)$ is $L^{2}\left(\mathbf{g}_{b}\right)$-orthogonal to the vector subspace of $\mathbf{O}\left(\mathbf{g}_{b}\right)$ spanned by the above elements $\left(\mathcal{L}_{X} \mathbf{g}_{b}\right)^{\circ}$ and $\mathcal{L}_{Y^{\prime}} \mathbf{g}_{b}$.

The proof relies on careful integrations by parts similar to that of the proof of Theorem 0.1.

Acknowledgements. The author would like to thank Olivier Biquard and Hans-Joachim Hein for inspiring discussions and for sharing some of their early results which lead to [BH19].

\section*{1. Symmetries of Einstein metrics and integrability}

In this section, we recall well-known properties of the two first derivatives of the Einstein operator and apply them to define the so-called Taub's preserved quantity as introduced in [Tau70]. It is a central quantity in the study of the integrability of Einstein deformations in the Lorentzian context.

Note 1.1. All along the article, we will denote by $F_{g}^{(m)}$ the $m$-linear terms of the development of a functional $h \mapsto F(g+h)$ at 0, we more precisely have (at least formally) for any small enough 2-tensor $h$ :
$$F(g+h)=\sum_{m \in \mathbb{N}} F_{g}^{(m)} \underbrace{(h, \ldots, h)}_{m \text { times }} .$$
1.1. Gauge and reparametrization properties. Let us start by recalling various consequences of the Bianchi identity: for any Riemannian metric $g$, one has
$$B_{g}(\operatorname{Ric}(g))=0 .$$
where for any 2-tensor $h$, we defined the Bianchi operator $B_{g}=\delta_{g}\left(h-\frac{1}{2} \operatorname{tr}(h) g\right)=\delta_{g}+$ $\frac{1}{2} d \operatorname{tr}(h)$, where $\delta_{g}$ is the divergence with the convention that in coordinates, for a 1-form $\omega, \delta_{g} \omega:=-g^{i j} \nabla_{j} \omega_{i}$ and for a symmetric 2-tensor $h,\left(\delta_{g} h\right)_{k}:=-g^{i j} \nabla_{j} h_{i k}$. Denoting the Einstein tensor $\mathrm{E}(g):=\operatorname{Ric}(g)-\frac{\mathrm{R}_{g}}{2} g$, the equation (12) rewrites
$$\delta_{g}(\mathrm{E}(g))=0 .$$

Proposition 1.2 ([FMM80]). Let us assume that $\mathbf{g}$ is a Ricci-flat metric on some open domain $\mathcal{U}$ of a Riemannian manifold $M$, and let $h$ be a symmetric 2-tensor on $\mathcal{U}$. We have the following gauge properties:
\begin{itemize}
\item[-] without assumption, one has
$$B_{\mathbf{g}}\left(\operatorname{Ric}_{\mathbf{g}}^{(1)}(h)\right)=0, \text { and } \delta_{\mathbf{g}}\left(\mathrm{E}_{\mathbf{g}}^{(1)}(h)\right)=0,$$
\item[-] if $\operatorname{Ric}_{\mathrm{g}}^{(1)}(h)=\Lambda g$ for $\Lambda \in \mathbb{R}$ or equivalently $\mathrm{E}_{\mathrm{g}}^{(1)}(h)+\lambda g=0$ for $\lambda \in \mathbb{R}$, then one has
$$B_{\mathbf{g}}\left(\operatorname{Ric}_{\mathbf{g}}^{(2)}(h, h)\right)=0, \text { and } \delta_{\mathbf{g}}\left(\mathrm{E}_{\mathbf{g}}^{(2)}(h, h)\right)=0 .$$
\end{itemize} \(\square\)

Let us continue with some identities when $g$ is perturbed in the direction of a Lie derivative. These come from differentiation of the following identity: for any diffeomorphism $\phi: M \rightarrow M$ and any metric $g$ on M
$$\operatorname{Ric}\left(\phi^{*} g\right)=\phi^{*}(\operatorname{Ric}(g)) \text { and } \mathrm{E}\left(\phi^{*} g\right)=\phi^{*}(\mathrm{E}(g)) .$$

Proposition 1.3 ([FMM80]). Let us assume that $g$ is a Riemannian metric on some bounded open domain $\mathcal{U}$ of a Riemannian manifold $M$, let $h$ be a symmetric 2-tensor on $\mathcal{U}$ and $X$ be a vector field on $\mathcal{U}$. We have the following reparametrization properties for the derivatives of Ric: without assumption, one has
$$\begin{gathered}
\operatorname{Ric}_{g}^{(1)}\left(\mathcal{L}_{X} g\right)=\mathcal{L}_{X}(\operatorname{Ric}(g)) \text { and } \mathrm{E}_{g}^{(1)}\left(\mathcal{L}_{X} g\right)=\mathcal{L}_{X}(\mathrm{E}(g)) \\
\operatorname{Ric}_{g}^{(2)}\left(h, \mathcal{L}_{X} g\right)+\operatorname{Ric}_{g}^{(1)}\left(\mathcal{L}_{X} h\right)=\mathcal{L}_{X}\left(\operatorname{Ric}_{g}^{(1)}(h)\right)
\end{gathered}$$
and
$$\mathrm{E}_{g}^{(2)}\left(h, \mathcal{L}_{X} g\right)+\mathrm{E}_{g}^{(1)}\left(\mathcal{L}_{X} h\right)=\mathcal{L}_{X}\left(\mathrm{E}_{g}^{(1)}(h)\right)$$ \(\square\)
1.2. Taub's preserved quantities and obstructions. Let us start by stating the following classical integrations by parts which are at the core of our proofs.

Lemma 1.4. Let $g$ be a metric on an open set $\mathcal{U}, T$ be a divergence-free symmetric 2tensor, and let $X$ be a vector field on $\mathcal{U}$. Then for any smooth compact subset $\Omega \subset \mathcal{U}$ with boundary, we have:
$$\int_{\partial \Omega} T(X, n) d v_{g_{\mid \partial \Omega}}=\int_{\Omega}\left\langle T, \delta_{g}^{*} X\right\rangle_{g} d v_{g}=\frac{1}{2} \int_{\Omega}\left\langle T, \mathcal{L}_{X} g\right\rangle_{g} d v_{g}$$
where $n$ is the outward unit normal to $\partial \Omega$, and where $\delta_{g}^{*} X:=\frac{1}{2} \mathcal{L}_{X} g$ is the formal adjoint of the divergence $\delta_{g}$.

We also have the following identity close to Schoen's Pohozaev equality [Sch88]. Denote $\stackrel{\circ}{h}$ or $(h)^{\circ}$ the traceless part of a symmetric 2-tensor $h$. If $T$ is divergence-free, then we have:
$$\begin{aligned}
\int_{\partial \Omega} \stackrel{\circ}{T}(X, n) d v_{g_{\mid \partial \Omega}} & =\frac{1}{2} \int_{\Omega}\left(\left\langle\stackrel{\circ}{T}, \mathcal{L}_{X} g\right\rangle_{g}-\frac{\mathcal{L}_{X}\left(\operatorname{tr}_{g} T\right)}{d}\right) d v_{g} \\
& =\frac{1}{2} \int_{\Omega}\left(\left\langle T,\left(\mathcal{L}_{X} g\right)^{\circ}\right\rangle_{g}-\frac{\mathcal{L}_{X}\left(\operatorname{tr}_{g} T\right)}{d}\right) d v_{g}
\end{aligned}$$

Remark 1.5. We will often abusively apply our operators to vector fields or 1 -forms indifferently, the identification will always be done thanks to the metric involved in the operator. More precisely, a vector field $X$ is identified with the 1 -form $g(X,$.$) .$

Proof. The key to this formula is the identity:
$$\delta_{g}(T(X))=\delta_{g}(T)(X)-\left\langle T, \delta_{g}^{*} X\right\rangle_{g}=\delta_{g}(T)(X)-\frac{1}{2}\left\langle T, \mathcal{L}_{X} g\right\rangle_{g}$$
which may be proven in coordinates using the symmetry of $T$. From the identity (22), using the fact that $T$ is divergence-free and the divergence theorem, we find the result by the divergence theorem.

The second equality (21) then follows by noting that
$$\int_{\Omega} \frac{\operatorname{tr}_{g} T}{n}\left\langle g, \mathcal{L}_{X} g\right\rangle_{g} d v_{g}=-\frac{1}{n} \int_{\Omega}\left(\operatorname{tr}_{g} T\right) \delta_{g}(X) d v_{g}=-\int_{\Omega} \mathcal{L}_{X}\left(\operatorname{tr}_{g} T\right) d v_{g}+\int_{\partial \Omega}\left(\operatorname{tr}_{g} T\right) g(X, n) .$$ \(\square\)

Let $\mathbf{g}$ be an Einstein metric on an open subset $\mathcal{U}$. For a vector field $X$, a closed orientable hypersurface $\Sigma \subset \mathcal{U}$ and symmetric 2-tensors $h$ and $k$ on $\mathcal{U}$ we define the following quantity:
$$\mathcal{B}_{X}^{\Sigma}(h):=\int_{\Sigma}\left(\mathrm{E}_{\mathbf{g}}^{(1)}(h)\right)\left(X, n_{\Sigma}\right) d v_{\Sigma}$$
where $n_{\Sigma}$ is the normal to $\Sigma$. We also define the so-called Taub's preserved quantity introduced in [Tau70]:
$$\mathcal{T}_{X}^{\Sigma}(h, k):=\int_{\Sigma}\left(\mathrm{E}_{\mathbf{g}}^{(2)}(h, k)\right)\left(X, n_{\Sigma}\right) d v_{\Sigma} .$$
Together with the gauge properties of Proposition 1.2, we use Lemma 1.4 to prove the following properties for $\mathcal{T}$ and $\mathcal{B}$.

Proposition 1.6. Let $\mathbf{g}$ be an Einstein metric on an open subset $\mathcal{U}, X$ be a Killing vector field, $h$ a 2 -tensor on $\mathcal{U}$, and $\Sigma$ and $\Sigma^{\prime}$ two closed hypersurfaces in $\mathcal{U}$ bounding an open subset $\Omega \subset \mathcal{U}$. Then, we have the following properties:
\begin{itemize}
\item[(1)] without additional assumption,
$$\mathcal{B}_{X}^{\Sigma}(h)=0$$
\item[(2)] if $\mathrm{E}_{\mathrm{g}}^{(1)}(h)=0$, then one has: $\mathcal{T}_{X}^{\Sigma^{\prime}}(h, h)=\mathcal{T}_{X}^{\Sigma}(h, h)$
\item[(3)] if $\mathrm{E}_{\mathbf{g}}^{(1)}(h)=0$, and for any vector field $Y$ on $\mathcal{U}$, we have $\mathcal{T}_{X}^{\Sigma}\left(h+\mathcal{L}_{Y} \mathbf{g}, h+\mathcal{L}_{Y} \mathbf{g}\right)=$ $\mathcal{T}_{X}^{\Sigma}(h, h)$.
\end{itemize}

Proof. Consider $\chi$ a cut-off function vanishing in the neighborhood of $\Sigma^{\prime}$ and equal to 1 on a neighborhood of $\Sigma$. We can therefore apply (20) on $\Omega$ bounded by $\Sigma$ and $\Sigma^{\prime}$ to the Killing vector field $X$ and $T=\mathrm{E}^{(1)}(\chi h)$ which is divergence-free by (14) to find:
$$\mathcal{B}_{X}^{\Sigma}(h)=\int_{\partial \Omega}\left(\mathrm{E}^{(1)}(\chi h)\right)(X, n) d v_{\partial \Omega}=0$$
See [FMM80] for the other equalities. \(\square\)
1.3. Integrability of Einstein deformations. In the Lorentzian context, it is a remarkable result that the quantities $\mathcal{T}_{\Sigma}^{X}(h, h)$ for the different Killing vector fields $X$ of $\mathbf{g}$ and $h$ satisfying $\mathrm{E}_{\mathbf{g}}^{(1)}(h)=0$ completely characterize the integrability of the infinitesimal Einstein deformation $h$.

Definition 1.7 (Integrable 2-tensor). Let $\mathbf{g}$ be an Einstein metric on $\mathcal{U}$. A 2-tensor $h$ is integrable if on any compact $K \subset \mathcal{U}$, there exists a smooth curve of Einstein metrics $t \in[0,1] \mapsto \mathbf{g}_{t}$ on $K$ satisfying $\partial_{t} \mathbf{g}_{t \mid t=0}=h$.

The link between the integral quantity $\mathcal{T}_{\Sigma}^{X}(h, h)$ and the integrability of $h$ is given by the following proposition.

Proposition 1.8 ([FMM80, Proposition 1.7]). Assume that $\mathbf{g}$ is a Ricci-flat metric on an open subset $\mathcal{U}$, that $h$ is an integrable 2-tensor which is the first jet of a curve of Ricci-flat metrics and $X$ is a Killing vector field. Then, for any compact hypersurface $\Sigma \subset \mathcal{U}$, one has
$$\mathcal{T}_{X}^{\Sigma}(h, h)=0 .$$
Proof. Let $K$ be a compact subset of $\mathcal{U}$ and $t \in[0,1] \mapsto \mathbf{g}_{t}$ a smooth curve of Einstein metrics on $K$ with $\mathbf{g}_{0}=\mathbf{g}$ satisfying $\partial_{t} \mathbf{g}_{t \mid t=0}=h$ with $\mathrm{E}\left(\mathbf{g}_{t}\right)=0$ for all $t \in[0,1]$. We have $0=\partial_{t}\left(\mathrm{E}\left(\mathbf{g}_{t}\right)\right)_{\mid t=0}=\mathrm{E}_{\mathrm{g}}^{(1)}(h)$, and if we denote $k:=\partial_{t^{2}}^{2} \mathbf{g}_{t \mid t=0}$, then we have
$$0=\partial_{t^{2}}^{2}\left(\mathrm{E}\left(\mathbf{g}_{t}\right)\right)_{\mid t=0}=\mathrm{E}_{\mathbf{g}}^{(1)}(k)+\mathrm{E}_{\mathbf{g}}^{(2)}(h, h) .$$

In particular, we have: $\mathcal{T}_{X}^{\Sigma}(h, h)=-\mathcal{B}_{X}^{\Sigma}(k)=0$ by (25). \(\square\)

We add an extension to Einstein but not necessarily Ricci-flat deformation of a Ricciflat metric. This time we need to assume that the Killing vector field is tangent to our hypersurface. This will always be satisfied in our applications.

Proposition 1.9. Assume that $\mathbf{g}$ is a Ricci-flat metric on an open subset $\mathcal{U}$, that $h$ is a 2-tensor which is the first jet of a smooth curve of Einstein metrics starting at $\mathbf{g}$ and $X$ is a Killing vector field for $\mathbf{g}$. Then, for any compact hypersurface $\Sigma \subset \mathcal{U}$ for which $X$ is tangent to $\Sigma$ once restricted to $\Sigma$, one has
$$\int_{\Sigma}\left(\operatorname{Ric}_{\mathbf{g}}^{(2)}(h, h)\right)\left(X, n_{\Sigma}\right) d v_{\Sigma}=0 .$$
Proof. Let $K \subset \mathcal{U}$ be a compact and $t \in[0,1] \mapsto \mathbf{g}_{t}$ a smooth curve of Einstein metrics on $K$ with $\mathbf{g}_{0}=\mathbf{g}$ satisfying $\partial_{t} \mathbf{g}_{t \mid t=0}=h$ with $\mathrm{E}\left(\mathbf{g}_{t}\right)+\lambda(t) \mathbf{g}_{t}=0$ for a smooth function $t \in[0,1] \mapsto \lambda(t) \in \mathbb{R}$ for all $t \in[0,1]$. We have
$$0=\partial_{t}\left(\mathrm{E}\left(\mathbf{g}_{t}\right)+\lambda(t) \mathbf{g}_{t}\right)_{\mid t=0}=\mathrm{E}_{\mathbf{g}}^{(1)}(h)+\lambda^{\prime}(0) \mathbf{g},$$
and if we denote $k:=\partial_{t^{2}}^{2} \mathbf{g}_{t \mid t=0}$, then we find
$$0=\partial_{t^{2}}^{2}\left(\mathrm{E}\left(\mathbf{g}_{t}\right)+\lambda(t) \mathbf{g}_{t}\right)_{\mid t=0}=\mathrm{E}_{\mathbf{g}}^{(1)}(k)+\mathrm{E}_{\mathbf{g}}^{(2)}(h, h)+\lambda^{\prime \prime}(0) \mathbf{g}+2 \lambda^{\prime}(0) h .$$
In particular, since for any metric $g$, one has $\operatorname{Ric}(g)=\mathrm{E}(g)-\frac{\operatorname{tr}_{g} \mathrm{E}(g)}{d} g$ in dimension $d$, we find:
$$\begin{aligned}
\operatorname{Ric}_{\mathbf{g}}^{(2)}(h, h) & =\mathrm{E}_{\mathbf{g}}^{(2)}(h, h)-\frac{1}{d}\left((\operatorname{tr} \mathrm{E})_{\mathbf{g}}^{(2)}(h, h)\right) \mathbf{g}-\frac{2}{d} \operatorname{tr}_{\mathbf{g}} \mathrm{E}_{\mathbf{g}}^{(1)}(h) h \\
& =\mathrm{E}_{\mathbf{g}}^{(2)}(h, h)-\frac{1}{d}\left((\operatorname{tr} \mathrm{E})_{\mathbf{g}}^{(2)}(h, h)\right) \mathbf{g}+2 \lambda^{\prime}(0) h
\end{aligned}$$
We consequently have: $\int_{\Sigma}\left(\operatorname{Ric}_{\mathbf{g}}^{(2)}(h, h)\right)\left(X, n_{\Sigma}\right) d v_{\Sigma}=-\int_{\Sigma}\left(\mathrm{E}_{\mathbf{g}}^{(1)}(k)\right)\left(X, n_{\Sigma}\right) d v_{\Sigma}=0$ because $\mathbf{g}\left(X, n_{\Sigma}\right)=0$ by assumption and thanks to (25). \(\square\)

Question 1.10. Can we recover the obstructions to integrability of [Koi82] (or new ones) thanks to the above criterion?

\section*{2. Preserved quantities on Ricci-flat cones and integrability}

We introduce another quantity similar to Taub's adapted to perturbations of Ricci-flat cones $\left(C(\Sigma), d r^{2}+r^{2} g_{\Sigma}\right)$. We will mostly work with the Euclidean case $\Sigma=\mathbb{S}^{d-1}$.
2.1. A preserved quantity on $\mathbb{R}^{d}$ and other Ricci-flat cones. Let us now introduce a functional similar to Taub's preserved quantity dealing this time with conformal Killing vector fields with constant conformal factor. The main example for us will be the vector field $r \partial_{r}$ on the Euclidean space $\left(\mathbb{R}^{d}, \mathbf{e}\right)$, where $r:=d_{\mathbf{e}}(0,$.$) .$

Proposition 2.1. Let $h$ be a symmetric 2-tensor on an open subset $\mathcal{U} \subset \mathbb{R}^{d}$ containing $\mathbb{S}^{d-1}$. Then, we have the following identity:
$$\int_{\mathbb{S}^{d-1}}\left(\mathrm{E}_{\mathbf{e}}^{(1)}(h)\right)\left(r \partial_{r}, \partial_{r}\right)+\frac{d-2}{2}\left(-\delta_{\mathbf{e}} h-d \operatorname{tr}_{\mathbf{e}} h\right)\left(\partial_{r}\right) d v_{\mathbb{S}^{d-1}}=0$$
Moreover, assume that we have $\mathrm{R}_{\mathrm{e}}^{(1)}(h)=0$ and $h$ bounded on $B_{\mathbf{e}}(1+\epsilon)$. Then we have:
$$\int_{\mathbb{S}^{d-1}}\left(\mathrm{E}_{\mathbf{e}}^{(1)}(h)\right)\left(r \partial_{r}, \partial_{r}\right)=0 .$$

Remark 2.2. One recognizes (up to a constant) the integrand of the ADM mass in the term $\int_{\mathbb{S}^{d-1}}\left(-\delta_{\mathbf{e}} h-d \operatorname{tr}_{\mathbf{e}} h\right)\left(\partial_{r}\right) d v_{\mathbb{S}^{d-1}}$. This is not surprising from the proof and can be seen as a first order version of the proof of the equality between the mass and the so-called Ricci version of the mass given in [Her16].

Proof. As in the proof of the first point in Proposition 1.6, without changing the value of the integral on $\mathbb{S}^{d-1}$, we replace $h$ by another 2-tensor equal to $h$ in a neighborhood of $\mathbb{S}^{d-1}$ and vanishing in a neighborhood of the sphere $(1-\epsilon) \mathbb{S}^{d-1} \subset \mathcal{U}$ for $\epsilon>0$ small enough. We denote $\Omega$ the open subset bounded by $\mathbb{S}^{d-1}$ and $(1-\epsilon) \mathbb{S}^{d-1}$.

From the identity (14) and Lemma 1.4, we can use the divergence theorem and the equality $\delta_{\mathbf{e}}^{*}\left(r \partial_{r}\right)=\mathbf{e}$ to find the identity:
$$\int_{\mathbb{S}^{d-1}}\left(\mathrm{E}_{\mathbf{e}}^{(1)}(h)\right)\left(r \partial_{r}, \partial_{r}\right) d v_{\mathbb{S}^{d-1}}=\int_{\Omega} \operatorname{tr}_{\mathbf{e}} \mathrm{E}_{\mathbf{e}}^{(1)}(h) d v_{\mathbf{e}}$$
Now, one recognizes that $\operatorname{tr}_{\mathbf{e}} \mathrm{E}_{\mathbf{e}}^{(1)}(h)=\frac{2-d}{2} \mathrm{R}_{\mathbf{e}}^{(1)}(h)$ by definition of the scalar curvature $\mathrm{R}_{g}=\operatorname{tr}_{g} \operatorname{Ric}_{g}$ and since $\mathrm{E}_{\mathbf{e}}=0$. From the first variation of the scalar curvature at a Euclidean metric:
$$\mathrm{R}_{\mathbf{e}}^{(1)}(h)=\delta_{\mathbf{e}}\left(\delta_{\mathbf{e}}(h)+d \operatorname{tr}_{\mathbf{e}}(h)\right),$$
using the divergence theorem, we find the stated formula.
Finally, if $h$ is defined on $B_{\mathbf{e}}(1+\epsilon)$ for some $\epsilon>0$ and satisfies $\mathrm{R}_{\mathbf{e}}^{(1)}(h)=0$ then one has $\int_{\mathbb{S}^{d-1}}\left(\mathrm{E}_{\mathbf{e}}^{(1)}(h)\right)\left(r \partial_{r}, \partial_{r}\right) d v_{\mathbb{S}^{d-1}}$ by (31). \(\square\)

One finds an obstruction similar to that of Proposition 1.8 for the second order variation of the metric direction.

Proposition 2.3. Let $h$ be a symmetric 2-tensor on an open subset $\mathcal{U} \subset \mathbb{R}^{d}$ containing $\mathbb{S}^{d-1}$ and $B_{\mathbf{e}}(1)$ satisfying $\mathrm{E}_{\mathbf{e}}^{(1)}(h)=0$. Then, we have the following identity:
$$\begin{aligned}
\int_{\mathbb{S}^{d-1}} & \left(\mathrm{E}_{\mathbf{e}}^{(2)}(h, h)\right)\left(r \partial_{r}, \partial_{r}\right) \\
& +\frac{2-d}{2}\left[\left((\delta+d \operatorname{tr})_{\mathbf{e}}^{(1)}(h)\right)(v)+\frac{\operatorname{tr}_{\mathbf{e}} h}{2}\left(\delta_{\mathbf{e}} v+d \operatorname{tr}_{\mathbf{e}} v\right)\right]\left(\partial_{r}\right) d v_{\partial \Omega}=0
\end{aligned}$$
The same result is true if $h$ is defined on an open subset $\mathcal{U} \subset \mathbb{R}^{d}$ containing $\mathbb{S}^{d-1}$ and $\mathbb{R}^{d} \backslash B_{\mathbf{e}}(1)$ and if it additionally satisfies the decay assumption: $r^{k}\left|\nabla_{\mathbf{e}}^{k} h\right|_{\mathbf{e}} \leqslant r^{-\frac{d-2}{2}}$ for $k \in\{0,1,2\}$.

Remark 2.4. For $h$ and $k$ symmetric 2-tensors, we have
$$\left[\left(\delta_{\mathbf{e}}^{(1)}(h)\right)(k)\right]\left(\partial_{r}\right)=-\delta_{\mathbf{e}}(h \times k)\left(\partial_{r}\right)-\frac{1}{2} k\left(d \operatorname{tr}_{\mathbf{e}} h, \partial_{r}\right)+\frac{1}{2}\left\langle k, \nabla_{\partial_{r}} h\right\rangle_{\mathbf{e}}$$
where $h \times k$ is the 2-tensor obtained from the composition of the endomorphisms associated to $h$ and $k$ and
$$\left[\left(d \operatorname{tr}_{\mathbf{e}}^{(1)}(h)\right)(k)\right]\left(\partial_{r}\right)=-d\left(\langle h, k\rangle_{\mathbf{e}}\right)\left(\partial_{r}\right),$$
see [Cox11] for instance. We will try not to use these formulas whenever possible and focus on situations for which this additional boundary term vanishes.

Remark 2.5. The two situations of Proposition 2.3 model Einstein manifolds or orbifolds at a given point or Einstein metrics asymptotic to a quotient of $\mathbb{R}^{d}$ at infinity. The decay condition on $h$ is not strong as any $h$ decaying at any rate at infinity and in divergence-free gauge (or Bianchi gauge) which satisfies $\mathrm{E}_{\mathbf{e}}^{(1)}(h)=0$ automatically satisfies $r^{k}\left|\nabla_{\mathbf{e}}^{k} h\right|_{\mathbf{e}} \leqslant$ $r^{-d+1}$ by [CT94].

Proof. Let us assume that $\mathrm{E}_{\mathbf{e}}^{(1)}(h)=0$ on an open set containing $B_{\mathbf{e}}(1)$. Using the formula (20) with $T=\mathrm{E}_{\mathbf{e}}^{(2)}(h, h)$ and $\Omega=B_{\mathbf{e}}(1)$, we find the equality:
$$\int_{\mathbb{S}^{d-1}}\left(\mathrm{E}_{\mathbf{e}}^{(2)}(h, h)\right)\left(r \partial_{r}, \partial_{r}\right) d v_{\mathbb{S}^{d-1}}=\int_{\Omega} \operatorname{tr}_{\mathbf{e}} \mathrm{E}_{\mathbf{e}}^{(2)}(h, h) d v_{\mathbf{e}}$$
where we used $\delta_{\mathbf{e}}^{*}\left(r \partial_{r}\right)=\mathbf{e}$ and the fact that there is only one nonvanishing boundary term at $\mathbb{S}^{d-1}$.

There remains to understand the term $\int_{\Omega} \operatorname{tr}_{\mathbf{e}} \mathrm{E}_{\mathbf{e}}^{(2)}(h, h) d v_{\mathbf{e}}$ as a boundary term. Since $\mathrm{E}_{\mathbf{e}}^{(1)}(h)=0$, then, $\operatorname{tr}_{\mathbf{e}} \mathrm{E}_{\mathbf{e}}^{(2)}(h, h)=\frac{2-d}{2} \mathrm{R}_{\mathbf{e}}^{(2)}(h, h)$ where we recall that the formula for $\mathrm{R}^{(1)}$ is given by $\mathrm{R}_{g}^{(1)}(v)=\delta_{g}\left(\delta_{g} v+d \operatorname{tr}_{g} v\right)-\langle v, \operatorname{Ric}(g)\rangle$ for a general metric $g$ and a deformation $v$. This implies that one generally has:
$$\int_{\Omega} \mathrm{R}_{g}^{(1)}(v) d v_{g}=-\int_{\partial \Omega}\left(\delta_{g} v+d \operatorname{tr}_{g} v\right)\left(\partial_{r}\right) d v_{\partial \Omega}-\int_{\Omega}\langle v, \operatorname{Ric}(g)\rangle d v_{g}$$

By differentiating (34) with $\Omega=B_{\mathbf{e}}(1)$ at $g=\mathbf{e}$ in the direction $h$ and for $v$ satisfying $\mathrm{E}_{\mathbf{e}}^{(1)}(v)=\operatorname{Ric}_{\mathbf{e}}^{(1)}(v)=0$ we obtain:
$$\int_{B_{\mathbf{e}}(1)} \mathrm{R}_{\mathbf{e}}^{(2)}(h, v) d v_{\mathbf{e}}=-\int_{\mathbb{S}^{d-1}}\left[\left((\delta+d \operatorname{tr})_{\mathbf{e}}^{(1)}(h)\right)(v)+\frac{\operatorname{tr}_{\mathbf{e}} h}{2}\left(\delta_{\mathbf{e}} v+d \operatorname{tr}_{\mathbf{e}} v\right)\right]\left(\partial_{r}\right) d v_{\mathbb{S}^{d-1}}$$
Using (35) with $v=h$ yields the result.
The proof is exactly the same when $\Omega=\mathbb{R}^{d} \backslash B_{\mathbf{e}}(1)$ if we assume that $r^{k}\left|\nabla_{\mathbf{e}}^{k} h\right|_{\mathbf{e}}=$ $o\left(r^{-\frac{d-2}{2}}\right)$ for $k \leqslant 2$ as this condition ensures that the boundary terms vanish at infinity and one simply has to deal with the boundary $\mathbb{S}^{d-1}$. \(\square\)

Remark 2.6. Just as in Proposition 1.6, the left-hand side of (32) has invariance properties on the hypersurface or action by diffeomorphism. The invariance by hypersurface is again a consequence of the divergence theorem, and the invariance by Lie derivative is comes from Proposition 1.3.

Remark 2.7. The conformal Killing vector field $r \partial_{r}$ is present for any Ricci-flat cone. One can therefore define a similar integral quantity which has to vanish with the exact same proof.
2.2. Deformations with constant scalar curvature. In our situations of interest, as we will see later, we will consider Einstein deformations for which the second variation of the scalar curvature is constant. In this case, the obstruction becomes much simpler as we may drop the additional boundary term.

Proposition 2.8. Let $h$ and $k$ be infinitesimal Einstein deformations of $\mathbf{e}$ on $B_{\mathbf{e}}(1+\epsilon)$ or $\mathbb{R}^{d} \backslash B_{\mathbf{e}}(1-\epsilon)$ satisfying
\begin{itemize}
\item[(1)] $\delta_{\mathbf{e}} h=\delta_{\mathbf{e}} k=0$
\item[(2)] $\mathrm{E}_{\mathbf{e}}^{(1)}(h)+\lambda \mathbf{e}=0$ and $\mathrm{E}_{\mathbf{e}}^{(1)}(k)+\mu \mathbf{e}=0$,
\item[(3)] and $\mathrm{R}_{\mathrm{e}}^{(2)}(h, k)$ is constant.
\end{itemize}
Then, we have the obstruction:
$$\int_{\mathbb{S}^{d-1}}\left(\operatorname{Ric}_{\mathbf{e}}^{(2)}(h, k)\right)\left(r \partial_{r}, \partial_{r}\right) d v_{\mathbb{S}^{d-1}}=0$$
and for any Killing vector field $Y$
$$\int_{\mathbb{S}^{d-1}}\left(\operatorname{Ric}_{\mathbf{e}}^{(2)}(h, k)\right)\left(Y, \partial_{r}\right) d v_{\mathbb{S}^{d-1}}=0$$
where Ric is the traceless part of the Ricci curvature.

Remark 2.9. The first assumption is a gauge-fixing condition which we will always be able to assume up to acting by a diffeomorphism. Moreover it will always be satisfied if $h=k$ is an integrable Einstein deformation which is not Ricci-flat. Indeed, differentiating $\mathrm{E}\left(g_{t}\right)+\lambda(t)=0$ starting at $g_{0}=\mathbf{e}$ with $\partial_{t \mid t=0} g_{t}=h$, and $\partial_{t^{2} \mid t=0}^{2} g_{t}=h^{\prime}$ twice yields
$$\mathrm{E}_{\mathbf{e}}^{(1)}\left(h^{\prime}\right)+\mathrm{E}_{\mathbf{e}}^{(2)}(h, h)+\lambda^{\prime \prime}(0) \mathbf{e}+2 \lambda^{\prime}(0) h=0$$
where every term but maybe $2 \lambda^{\prime}(0) h=2 \lambda h$ is divergence-free by Lemma 1.2.
Remark 2.10. The second assumption just means that we consider infinitesimal Einstein deformations. We will see how to ensure that the third assumption is satisfied in dimension 4 in the next sections.

Proof. For this situation, we use Schoen's Pohozaev identity (21) applied to the 2-tensor $\mathrm{E}_{\mathbf{e}}^{(2)}(h, k)$ which is divergence-free because $h$ and $k$ are infinitesimal Einstein deformations, see Lemma 1.2:
$$\int_{\partial \Omega}\left(\mathrm{E}_{\mathbf{e}}^{(2)}(h, k)\right)^{\circ}\left(r \partial_{r}, n\right) d v_{\mathbf{e}_{\mid \partial \Omega}}=-\frac{1}{2 d} \int_{\Omega} \mathcal{L}_{r \partial_{r}} \operatorname{tr}_{\mathbf{e}}\left(\mathrm{E}_{\mathbf{e}}^{(2)}(h, k)\right) d v_{\mathbf{e}}$$
Let us now express both $\left(\mathrm{E}_{\mathbf{e}}^{(2)}(h, k)\right)^{\circ}$ and $\operatorname{tr}_{\mathbf{e}}\left(\mathrm{E}_{\mathbf{e}}^{(2)}(h, k)\right)$ in terms of $\operatorname{Ric}^{(2)}(h, k)$ and $\mathrm{R}_{\mathrm{e}}^{(2)}(h, k)$. For this, we first note that since $\operatorname{tr}_{g} \mathrm{E}_{g}=\frac{2-d}{2} \mathrm{R}_{g}$ for any $g$, we have:
$$\operatorname{tr}_{\mathbf{e}}\left(\mathrm{E}_{\mathbf{e}}^{(2)}(h, k)\right)=\frac{2-d}{2} \mathrm{R}_{\mathbf{e}}^{(2)}(h, k)-\lambda \operatorname{tr}_{\mathbf{e}} k-\mu \operatorname{tr}_{\mathbf{e}} h,$$
and then, by (28), we find:
$$\left(\mathrm{E}_{\mathrm{e}}^{(2)}(h, k)\right)^{\circ}=\mathrm{Ric}^{\circ}(2)(h, k)-\lambda \stackrel{\circ}{k}-\mu \stackrel{\circ}{h} .$$
Finally, since by assumption $\delta_{\mathbf{e}} h=\delta_{\mathbf{e}} k=0$, we can again use (21):
$$\int_{\partial \Omega} \stackrel{\circ}{h}\left(r \partial_{r}, n\right) d v_{\mathbf{e}_{\mid \partial \Omega}}=-\frac{1}{2 d} \int_{\Omega} \mathcal{L}_{r \partial_{r}}\left(\operatorname{tr}_{\mathbf{e}} h\right) d v_{\mathbf{e}} \text { and } \int_{\partial \Omega} \stackrel{\circ}{k}\left(r \partial_{r}, n\right) d v_{\mathbf{e}_{\mid \partial \Omega}}=-\frac{1}{2 d} \int_{\Omega} \mathcal{L}_{r \partial_{r}}\left(\operatorname{tr}_{\mathbf{e}} k\right) d v_{\mathbf{e}}$$
Putting (38), (39), (40) and (41), we find
$$\int_{\partial \Omega} \operatorname{Ric}^{(2)}(h, k)\left(r \partial_{r}, n\right) d v_{\mathbf{e}_{\mid \partial \Omega}}=-\frac{2-d}{4 d} \int_{\Omega} \mathcal{L}_{r \partial_{r}}\left(\mathrm{R}_{\mathbf{e}}^{(2)}(h, k)\right) d v_{\mathbf{e}}$$
and since $\mathrm{R}_{\mathrm{e}}^{(2)}(h, k)$ is assumed to be constant, we find the stated equality. The easier case of a Killing vector field $Y$ is treated similarly. \(\square\)
2.3. Einstein metrics closing-up inside a hypersurface. Let us consider a topology $N=\left(\mathbb{R}^{4} / \Gamma\right) \backslash\{0\} \cup \Sigma$ for $\Sigma$ a lower dimensional submanifold "closing up" $N$ where $\{0\}$ should be. This should be the topology of a general Ricci-flat ALE, see [And92]. We see that $\left(\mathbb{R}^{4} / \Gamma, \mathbf{e}\right)$ is isometric to a degenerate metric on $N$ which we still denote e for which $\mathbf{e}_{\mid \Sigma}=0$ (meaning the induced metric on $\Sigma$, not the restriction of $\mathbf{e}$ at $\Sigma$ ), the vector field $r \partial_{r}$ also extends to $N$ and vanishes on $\Sigma$.

The typical situation is that of a minimal resolution of $\mathbb{C}^{2} / \Gamma$ for $\Gamma \subset \operatorname{SU}(2)$, for instance: $T^{*} \mathbb{S}^{2}=\left(\mathbb{R}^{4} / \mathbb{Z}_{2}\right) \backslash\{0\} \cup \mathbb{S}^{2}$ is the topology of the Eguchi-Hanson metric:
$$\mathbf{e h}:=\sqrt{\frac{r^{4}}{1+r^{4}}}\left(d r^{2}+r^{2} \alpha_{1}^{2}\right)+\sqrt{1+r^{4}}\left(\alpha_{2}^{2}+\alpha_{3}^{2}\right) .$$
with metric $\alpha_{2}^{2}+\alpha_{3}^{2}$ on $\mathbb{S}^{2}$. Let us restrict ourselves to this situation and keep our discussion at a somewhat informal level as the last section of the article will prove these obstructions rigorously. Assume that there exists a smooth curve of Einstein metrics $t \in[0,1] \mapsto$ $\mathbf{g}_{t}$ on $N=T^{*} \mathbb{S}^{2}$ with $\mathbf{g}_{t}$ nondegenerate for $t>0$ and with $\mathbf{g}_{0}=\mathbf{e}$. This implies by
[And89, BKN89, Nak90] that some rescaling of $\mathbf{g}_{t}$ converges to the Eguchi-Hanson metric (42) where, schematically, one has in the coordinates of (42):
$$\mathbf{e h}=\mathbf{e}+H^{4}+\ldots$$
with $\left|H^{4}\right|_{\mathbf{e}} \sim r^{-4}$, while another rescaling of $\mathbf{g}_{t}$ converges to an Einstein orbifold
$$\mathbf{g}_{o}=\mathbf{e}+H_{2}+\ldots$$
with $\left|H_{2}\right|_{\mathbf{e}} \sim r^{2}$, and with singularity $\mathbb{R}^{4} / \mathbb{Z}_{2}$. Up to some gauge conditions, we are therefore in the situation of Theorem 4.6 but we may use the integration by parts of Proposition 2.8 to interpret this as an obstruction to the existence of an Einstein metric "closing-up" inside the hypersurface $\mathbb{S}^{3} / \mathbb{Z}_{2}$.

By [Ozu20], up to rescaling and reparametrizing the curve $t \mapsto \mathbf{g}_{t}$ in well-chosen coordinates, we have a development $\mathbf{g}_{t}=\mathbf{e}+H_{2}+t^{2} H^{4}+t^{2} H_{2}^{4}+\ldots$ with $H_{2}^{4}=\mathcal{O}\left(r^{-2}\right)$ with remaining term negligible in a region where $\sqrt{t} \ll r \ll 1$, hence in particular for $r$ close to $t^{1 / 4}$ for small $t$. We again consider the integration by parts
$$\begin{aligned}
\int_{\left\{r=t^{1 / 4}\right\}} & \left(\mathrm{E}^{(1)}\left(H_{2}^{4}\right)+\mathrm{E}_{\mathbf{e}}^{(2)}\left(H_{2}, H^{4}\right)+\lambda H^{4}\right)\left(r \partial_{r}, \partial_{r}\right) d v_{t^{1 / 4} \mathbb{S}^{3} / \mathbb{Z}_{2}} \\
& =\int_{\left\{r<t^{1 / 4}\right\}} \operatorname{tr}_{\mathbf{e}}\left(\mathrm{E}^{(1)}\left(H_{2}^{4}\right)+\mathrm{E}_{\mathbf{e}}^{(2)}\left(H_{2}, H^{4}\right)+\lambda H^{4}\right) d v_{\mathbf{e}}
\end{aligned}$$
It was proven in [Ozu20] that in the coordinates of (42), one actually has $H_{2}^{4}=0$. This yields:
$$\int_{\left\{r=t^{1 / 4}\right\}}\left(\operatorname{Ric}_{\mathbf{e}}^{(2)}\left(H_{2}, H^{4}\right)\right)\left(r \partial_{r}, \partial_{r}\right) d v_{t^{1 / 4} \mathbb{S}^{3} / \mathbb{Z}_{2}}=\frac{2-d}{2} \int_{\left\{r<t^{1 / 4}\right\}} \mathrm{R}_{\mathbf{e}}^{(2)}\left(H_{2}, H^{4}\right) d v_{\mathbf{e}}$$
Now, by Corollary 3.7 proven below, one has $\mathrm{R}_{\mathbf{e}}^{(2)}\left(H_{2}, H^{4}\right)=0$ because $H^{4}$ is anti-selfdual, and we recover the obstruction (36) in this situation. The other obstructions with Killing vector fields are recovered in the same way.

Remark 2.11. The coordinates of (42) correspond to the volume gauge of Definition 3.12 below and one of their properties is that the vector field $r \partial_{r}$ is harmonic, hence $\mathcal{L}_{r \partial_{r}} \mathbf{e h}$ is an infinitesimal Einstein deformation - up to a trace term.

\section*{3. The 4-dimensional situation}

Let us now specialize our discussion to the dimension $d=4$ where most of our applications are. In this section, we will test the obstruction to the integrability of infinitesimal Einstein deformations on the development of Einstein 4-manifolds at the infinity of a Ricci-flat ALE metric. See Appendix A for the case of a neighborhood of a given point of an Einstein manifold or orbifold. We will see that the obstructions always vanish and do not add any restriction.

In order to show this, we will prove the existence of good gauges in which the quadratic term of $h \mapsto \operatorname{Ric}(\mathbf{e}+h)$ are easily computable. This is an important step towards the next Section 4 where obstructions to the desingularization of some Einstein metrics are found.
3.1. Notations. In dimension 4, the space of 2-forms decomposes into selfdual and antiselfdual 2-forms which are elements of the eigenspaces of Hodge star operator * (which satisfies $*^{2}=\mathrm{Id}$ ) respectively associated to the eigenvalues 1 and -1 . We denote $\Omega^{+}$and $\Omega^{-}$the associated eigenspaces.

Denote $\left(x_{1}, x_{2}, x_{3}, x_{4}\right)$ coordinates in an orthonormal basis of $\mathbb{R}^{4}$. We define the 2-forms
$$\omega_{1}^{ \pm}:=d x^{1} \wedge d x^{2} \pm d x^{3} \wedge d x^{4}$$
and similarly $\omega_{2}^{ \pm}$and $\omega_{3}^{ \pm}$by cyclic permutations. The $\omega_{i}^{+}$form an orthogonal basis of the space of selfdual 2-forms, $\Omega^{+}$, and the $\omega_{i}^{-}$form an orthogonal basis of the space of anti-selfdual 2-forms, $\Omega^{-}$.

Thanks to them, we define the following basis of the Killing vector fields preserving 0 on $\mathbb{R}^{4}$ :
$$Y_{i}^{ \pm}:=\omega_{i}^{ \pm}\left(r \partial_{r}\right) .$$
The other Killing vector fields of $\mathbb{R}^{4}$ are given by constant vector fields representing translations. Note that those will not be $\Gamma$-invariant for any $\Gamma \subset S O(4)$ with $\Gamma \neq\{\mathrm{Id}\}$.

Note that in each orientation, the frame ( $r \partial_{r}, Y_{1}^{ \pm}, Y_{2}^{ \pm}, Y_{3}^{ \pm}$) is dual to the coframe $\left(d r / r, \alpha_{1}^{ \pm}, \alpha_{2}^{ \pm}, \alpha_{3}^{ \pm}\right)$where we define $\alpha_{i}^{ \pm}:=\omega_{i}^{ \pm}(d r / r)$. We also define the following 2-forms which also form bases of the spaces of selfdual or anti-selfdual 2-forms:
$$\theta_{1}^{\mp}:=r d r \wedge \alpha_{1}^{ \pm} \mp r^{2} \alpha_{2}^{ \pm} \wedge \alpha_{3}^{ \pm},$$
and similarly $\theta_{2}^{\mp}$ and $\theta_{3}^{\mp}$ by cyclic permutations.
Remark 3.1. The notation $\theta_{i}^{+}$meant something else in [Ozu20].
For the above 2-forms, we have the following formula: for $x=\left(x_{1}, x_{2}, x_{3}, x_{4}\right)$
$$\theta_{i}^{\mp}(x)=\sum_{j=1}^{3} \frac{x^{T}\left(\omega_{i}^{ \pm} \circ \omega_{j}^{\mp}\right) x}{|x|^{2}} \omega_{j}^{\mp}=-\frac{\left\langle Y_{i}^{ \pm}, Y_{j}^{\mp}\right\rangle}{r^{2}} \omega_{j}^{\mp},$$
where $\omega_{i}^{ \pm} \circ \omega_{j}^{\mp}$ is the symmetric traceless matrix given by the (commuting) product of the antisymmetric matrices associated to $\omega_{i}^{ \pm}$and $\omega_{j}^{\mp}$, and where $x^{T}$ is the transpose of $x$. We also have the following equalities: $\omega_{1}^{ \pm}=r d r \wedge \alpha_{1}^{ \pm} \pm r^{2} \alpha_{2}^{ \pm} \wedge \alpha_{3}^{ \pm}$and similar equalities for $\omega_{i}^{ \pm}$for $i \in\{2,3\}$ by cyclic permutations.
3.1.1. Orbifolds and ALE spaces. We will be interested in two types of geometries: Einstein orbifolds and Ricci-flat ALE metrics. They respectively correspond to the singular limits and the singularity models of the degeneration of Einstein 4-manifolds.

Definition 3.2 (Orbifold (with isolated singularities)). We will say that a metric space $\left(M_{o}, g_{o}\right)$ is an orbifold of dimension $d \geqslant 2$ if there exists $\epsilon_{0}>0$ and a finite number of points $\left(p_{k}\right)_{k}$ of $M_{o}$ called singular such that we have the following properties:
\begin{itemize}
\item[(1)] the space $\left(M_{o} \backslash\left\{p_{k}\right\}_{k}, g_{o}\right)$ is a manifold of dimension $d$,
\item[(2)] for each singular point $p_{k}$ of $M_{o}$, there exists a neighborhood of $p_{k}, U_{k} \subset M_{o}$, a finite subgroup acting freely on $\mathbb{S}^{d-1}, \Gamma_{k} \subset S O(n)$, and a diffeomorphism $\Phi_{k}$ : $B_{\mathbf{e}}\left(0, \epsilon_{0}\right) \subset \mathbb{R}^{d} / \Gamma_{k} \rightarrow U_{k} \subset M_{o}$ for which, the pull-back of $\Phi_{k}^{*} g_{o}$ on the covering $\mathbb{R}^{d}$ is smooth.
\end{itemize}

Remark 3.3. Note that smooth Einstein metrics are Einstein orbifolds. Einstein orbifold metrics are smooth up to taking a finite local cover at the singular point as seen in [BKN89].

Definition 3.4 (ALE orbifold (with isolated singularities)). An ALE orbifold of dimension $d \geqslant 4,\left(N, g_{b}\right)$ is a metric space for which there exists $\epsilon_{0}>0$, singular points $\left(p_{k}\right)_{k}$ and a compact $K \subset N$ for which we have:
\begin{itemize}
\item[(1)] $\left(N, g_{b}\right)$ is an orbifold of dimension $d$,
\item[(2)] there exists a diffeomorphism $\Psi_{\infty}:\left(\mathbb{R}^{d} / \Gamma_{\infty}\right) \backslash \overline{B_{\mathbf{e}}\left(0, \epsilon_{0}^{-1}\right)} \rightarrow N \backslash K$ such that we have $r^{l}\left|\nabla^{l}\left(\Psi_{\infty}^{*} g_{b}-\mathbf{e}\right)\right|_{\mathbf{e}} \leqslant C_{l} r^{-d}$.
\end{itemize}

Note 3.5. We will often identify $\mathbb{R}^{d} / \Gamma$ and its cover $\mathbb{R}^{d}$ when writing $A L E$ of orbifold spaces in coordinates.
3.1.2. Curvature of Einstein 4-manifolds. Thanks to the direct sum of selfdual and antiselfdual 2-forms, the symmetric endomorphism on 2-forms, $\mathbf{R}$ given by the Riemannian curvature decomposes into blocks,
$$\mathbf{R}=:\left[\begin{array}{ll}
\mathbf{R}^{+} & \text {Ric } \\
\text { Ric } & \mathbf{R}^{-}
\end{array}\right],$$
where the Ric is the traceless part of the Ricci curvature, and where $\mathbf{R}^{ \pm}$are the selfdual and anti-selfdual parts of the curvature.

Let us do a quick recap on the curvature of Einstein perturbations of the Euclidean space $\left(\mathbb{R}^{4}, \mathbf{e}\right)$. The starting point is the identification of the set of traceless symmetric 2-tensors $\operatorname{Sym}_{0}^{2} T M$ with $\Omega^{+} \otimes \Omega^{-}$thanks to the map:
$$\omega^{+} \otimes \omega^{-} \in \Omega^{+} \otimes \Omega^{-} \mapsto \omega^{+} \circ \omega^{-}=\omega^{-} \circ \omega^{+} \in \operatorname{Sym}_{0}^{2} T M$$
where $\omega^{+} \circ \omega^{-}$is the 2-tensor associated to the composition of the anti-symmetric endomorphisms of $T M$ associated to $\omega^{+}$and $\omega^{-}$by the metric. Therefore, any 2 -tensor $h$ on $\left(\mathbb{R}^{4}, \mathbf{e}\right)$ has unique decompositions:
$$h=\lambda \mathbf{e}+\sum_{i} \phi_{i}^{-} \circ \omega_{i}^{+}=\lambda \mathbf{e}+\sum_{j} \phi_{j}^{+} \circ \omega_{j}^{-}$$
for a scalar function $\lambda$, and $\phi_{i}^{-} \in \Omega^{-}$and $\phi_{j}^{+} \in \Omega^{+}$. According to [Biq16], the Bianchi gauge condition for $h$ rewrites:
$$d \lambda+\sum_{i=1}^{3} *\left(\omega_{i}^{+} \wedge\left(* d \phi_{i}^{-}\right)\right)=d \lambda+\sum_{j=1}^{3} *\left(\omega_{j}^{-} \wedge\left(* d \phi_{j}^{+}\right)\right)=0 .$$
Extending the computations of [Biq16], we prove the following result.
Proposition 3.6. Let $h$ be a symmetric 2-tensor on $\mathbb{R}^{4}$ decomposed as:
$$h=\lambda \mathbf{e}+\sum_{i} \phi_{i}^{-} \circ \omega_{i}^{+}=\lambda \mathbf{e}+\sum_{j} \phi_{j}^{+} \circ \omega_{j}^{-}$$
and satisfying the condition (46).
Then, defining $a_{\mathbf{e}}^{+,(1)}(h)=\sum_{i} * d \phi_{i}^{-} \otimes \omega_{i}^{+}$and $a_{\mathbf{e}}^{-,(1)}(h)=\sum_{j} * d \phi_{j}^{+} \otimes \omega_{j}^{-}$the infinitesimal variations of connections, we have:
\begin{itemize}
\item[-] $\mathbf{R}_{\mathbf{e}}^{+,(1)}(h)=-d_{+} a_{\mathbf{e}}^{+,(1)}(h)=-\sum_{i} d_{+} * d \phi_{i}^{-} \otimes \omega_{i}^{+}$where $d_{+}$is the exterior differential composed with the projection on $\Omega^{+}$,
\item[-] $\mathbf{R}_{\mathbf{e}}^{-,(1)}(h)=-d_{-} a_{\mathbf{e}}^{-,(1)}(h)=-\sum_{i} d_{-} * d \phi_{i}^{+} \otimes \omega_{i}^{-}$where $d_{-}$is the exterior differential composed with the projection on $\Omega^{-}$, and
\item[-] $\operatorname{Ric}_{\mathbf{e}}^{(1)}(h)=d_{-} a_{\mathbf{e}}^{+,(1)}(h)=d_{+} a_{\mathbf{e}}^{-,(1)}(h)$ and in particular, $h$ is an infinitesimal Einstein deformation if and only if for all $i \in\{1,2,3\}, d_{-} * d \phi_{i}^{-}=0$ or equivalently if and only if for all $j \in\{1,2,3\}, d_{+} * d \phi_{j}^{+}=0$.
\end{itemize}
Moreover, if $h$ is an infinitesimal Einstein deformation, then we have:
\begin{itemize}
\item[-] $\mathbf{R}_{\mathbf{e}}^{+,(2)}(h, h)=-\frac{1}{2}\left[a_{\mathbf{e}}^{+,(1)}(h), a_{\mathbf{e}}^{+,(1)}(h)\right]_{+}$,
\item[-] $\mathbf{R}_{\mathbf{e}}^{-,(2)}(h, h)=-\frac{1}{2}\left[a_{\mathbf{e}}^{-,(1)}(h), a_{\mathbf{e}}^{-,(1)}(h)\right]_{-}$and
\end{itemize}
- defining linear maps $\phi^{-}: \Omega^{+} \rightarrow \Omega^{-}$and $\phi^{+}: \Omega^{-} \rightarrow \Omega^{+}$by for any $i$ and $j$ in $\{1,2,3\}, \phi^{-}\left(\omega_{i}^{+}\right)=\phi_{i}^{-}$and $\phi^{+}\left(\omega_{j}^{-}\right)=\phi_{j}^{+}$, we have
$$\begin{aligned}
\operatorname{Ric}_{\mathbf{e}}^{(2)}(h, h) & =\frac{1}{2}\left[a_{\mathbf{e}}^{+,(1)}(h), a_{\mathbf{e}}^{+,(1)}(h)\right]_{-}+\sum_{i} \phi^{-}\left(\mathbf{R}_{\mathbf{e}}^{+,(1)}(h)\left(\omega_{i}^{+}\right)\right) \otimes \omega_{i}^{+} \\
& =\frac{1}{2}\left[a_{\mathbf{e}}^{-,(1)}(h), a_{\mathbf{e}}^{-,(1)}(h)\right]_{+}+\sum_{j} \phi^{+}\left(\mathbf{R}_{\mathbf{e}}^{-,(1)}(h)\left(\omega_{j}^{-}\right)\right) \otimes \omega_{j}^{-} .
\end{aligned}$$
Proof. The only points that are not proven in [Biq16] are the values of $\mathbf{R}_{\mathbf{e}}^{ \pm,(2)}(h, h)$. For this, we recall that $\mathbf{R}^{+}$is the opposite of the curvature $d a^{+}+\frac{1}{2}\left[a^{+}, a^{+}\right]$of the bundle $\Omega^{+}$. The origin of the term $-\frac{1}{2}\left[a_{\mathbf{e}}^{+,(1)}(h), a_{\mathbf{e}}^{+,(1)}(h)\right]_{+}$is therefore clear. There is another source of variation of $\mathbf{R}^{+}$which are the variations of $\Omega^{+}$and $\Omega^{-}$at $\mathbf{e}$ in the direction $h=\lambda \mathbf{e}+\sum_{i} \phi_{i}^{-} \circ \omega_{i}^{+}=\lambda \mathbf{e}+\sum_{j} \phi_{j}^{+} \circ \omega_{j}^{-}$. According to Biq16, by blocks given by the direct sum $\Omega_{\mathbf{e}}^{+} \oplus \Omega_{\mathbf{e}}^{-}$, the variation of the bases $\left(\omega_{i}^{ \pm}\right)_{i}$ as bases of $\Omega^{ \pm}$rewrites:
$$\omega_{i, \mathbf{e}}^{ \pm,(1)}(h)=\left[\begin{array}{cc}
\lambda & -\phi^{-} \\
-\phi^{+} & \lambda
\end{array}\right] \omega_{i}^{+},$$
and therefore, the conjugation by $\mathrm{Id}+\left[\begin{array}{cc}\lambda & -\phi^{-} \\ -\phi^{+} & \lambda\end{array}\right]+\mathcal{O}\left(|h|_{\mathbf{e}}^{2}\right)$ of the first order curvature $\operatorname{variation}\left[\begin{array}{cc}\mathbf{R}_{\mathbf{e}}^{+,(1)}(h) & 0 \\ 0 & \mathbf{R}_{\mathbf{e}}^{-,(1)}(h)\end{array}\right]$ leaves at second order term: $\left[\begin{array}{cc}0 & \phi^{-}\left(\mathbf{R}_{\mathbf{e}}^{+,(1)}(h)\right) \\ \phi^{+}\left(\mathbf{R}_{\mathbf{e}}^{-,(1)}(h)\right) & 0\end{array}\right]$, which yields the result. \(\square\)
3.1.3. An application to the variation of scalar curvature. Let $h=\lambda \mathbf{e}+\sum_{i} \phi_{i}^{-} \circ \omega_{i}^{+}$and $k=\mu \mathbf{e}+\sum_{i} \psi_{i}^{-} \circ \omega_{i}^{+}$for $\lambda$ and $\mu$ scalar functions and $\phi_{i}^{-}, \psi_{i}^{-} \in \Omega_{-}$.

Corollary 3.7. Assume that $h$ and $k$ are infinitesimal Einstein deformations satisfying (46) and assume moreover that $h$ is anti-selfdual in the sense that $a_{\mathbf{e}}^{+,(1)}(h)=0$.

Then, we have: $\mathbf{R}_{\mathbf{e}}^{+,(2)}(h, k)=0$, and moreover:
$$\operatorname{Ric}_{\mathbf{e}}^{(2)}(h, k)=\sum_{i} \phi_{i}^{-}\left(\mathbf{R}_{\mathbf{e}}^{+,(1)}(k)\left(\omega_{i}^{+}\right)\right) \otimes \omega_{i}^{+} .$$
3.2. Asymptotic curvature of 4 -dimensional Ricci-flat ALE metrics. Let us now study the infinity of Ricci-flat ALE metrics of dimension 4.
3.2.1. Development of Ricci-flat ALE metrics. Let us start by understanding the asymptotic terms of Ricci-flat ALE metrics.

Let $\left(N, \mathbf{g}_{b}\right)$ be a 4-dimensional Ricci-flat ALE orbifold asymptotic to $\left(\mathbb{R}^{4} / \Gamma, \mathbf{e}\right)$ for $\Gamma \subset$ $S O(4)$, and let $\left(\Sigma_{s}\right)_{s>s_{0}}$ for some $s_{0}>0$ be a CMC (Constant Mean Curvature) foliation of $\left(N, \mathbf{g}_{b}\right)$ in a neighborhood of infinity as in [CEV17, BH19] where the mean curvature of $\Sigma_{s}$ is equal to $\frac{3}{s}$ (like a sphere of radius $s$ in $\left(\mathbb{R}^{4} / \Gamma, \mathbf{e}\right)$ ).
Definition 3.8 (CMC gauge). Then, by [BH19] there exist a compact $K \subset N, s_{0}>0$ and a local diffeomorphism: $\Phi:\left(\mathbb{R}^{4} \backslash B_{\mathbf{e}}\left(0, s_{0}\right)\right) / \Gamma \mapsto N \backslash K$ with:
\begin{itemize}
\item[-] for all $s>s_{0}, \Phi\left(S_{\mathbf{e}}(s)\right)=\Sigma_{s}$,
\item[-] $\Phi^{*} \mathbf{g}_{b}-\mathbf{e}=H^{4}+\mathcal{O}\left(r^{-5}\right)$ at infinity for $\left|H^{4}\right|_{\mathbf{e}} \sim r^{-4}$,
\item[-] $\delta_{\mathbf{e}} H^{4}=0, \operatorname{tr}_{\mathbf{e}} H^{4}=0, H^{4}\left(\partial_{r}, \partial_{r}\right)=0$
\item[-] and one can even arrange $\Phi$ so that $H^{4}$ is more precisely of the form:
$$H^{4}=\frac{\sum_{i j} h_{i j}^{+} \theta_{i}^{-} \circ \omega_{j}^{+}+\sum_{k l} h_{k l}^{-} \theta_{k}^{+} \circ \omega_{l}^{-}}{r^{4}} .$$
with $\sum_{i} h_{i i}^{+}=0$ and $\sum_{k} h_{k k}^{-}=0$.
\end{itemize}

We call these coordinates a CMC gauge.
Remark 3.9. Instead of that last point, in [BH19], another decomposition is used with so-called reduced Kronheimer's terms which are projections of the terms $\theta_{i}^{\mp} \circ \omega_{j}^{ \pm}$on their part without $d r$ using some gauge terms of the form $\mathcal{L}_{V}$ for $V=\frac{1}{r^{4}} L(x)$ for $L$ either proportional to the identity or skew-symmetric.

Denote $\Omega_{s}$ the interior of the hypersurface $\Sigma_{s}$. The limit:
$$\mathcal{V}\left(N, \mathbf{g}_{b}\right):=\lim _{s \rightarrow \infty} \operatorname{Vol}_{\mathbf{g}_{b}} \Omega_{s}-\operatorname{Vol}_{\mathbf{e}}\left(B_{\mathbf{e}}(s) / \Gamma\right) \leqslant 0$$
exists and is called the renormalized volume of $\left(N, \mathbf{g}_{b}\right)$ in [BH19]. It is vanishing if and only if $\left(N, \mathbf{g}_{b}\right)$ is flat.

Remark 3.10. An interesting remark of Hans-Joachim Hein is the following. There are examples of Kronheimer's instantons of [Kro89a] described in Remark 4.8 below for which one has $H^{4}=0$ in CMC gauge. It is a way to see that the notion of reduced volume is not an asymptotic quantity. It essentially does not tell anything about the asymptotics of Ricci-flat ALE metric at infinity which at this point could vanish at any order. It is a global and subtle quantity. This reduced volume is the core quantity of the obstruction (54) proven later.

We will also need a particular gauge very close to one introduced by Biquard and Hein in some unpublished notes which led to [BH19]. This is a so-called volume gauge in which the volume form of the ALE metric is asymptotically equal to that of the asymptotic flat cone.

Example 3.11. The volume form of the Eguchi-Hanson metric in its usual form (42) is equal to that of the asymptotic cone $\mathbb{R}^{4} / \mathbb{Z}_{2}$ with its flat metric $d r^{2}+r^{2}\left(\alpha_{1}^{2}+\alpha_{2}^{2}+\alpha_{3}^{2}\right)$.

Precomposing the above local diffeomorphism $\Phi$ of Definition 3.8 with the flow of $r^{-3} \partial_{r}$ for an adapted amount of time $t=C(\Gamma) \mathcal{V}\left(N, \mathbf{g}_{b}\right)$ for $C(\Gamma)>0$, one may choose another diffeomorphism $\Psi$ between neighborhoods of infinities with the following properties.

Definition 3.12 (Volume gauge). There exist a compact $K^{\prime} \subset N, r_{0}^{\prime}>0$ and a local diffeomorphism: $\Psi:\left(\mathbb{R}^{4} / \Gamma\right) \backslash B_{\mathbf{e}}\left(0, r_{0}^{\prime}\right) \mapsto N \backslash K^{\prime}$ with:
\begin{itemize}
\item[-] $\Psi^{*} \mathbf{g}_{b}-\mathbf{e}=H^{4}+\mathcal{O}\left(r^{-5}\right)$ at infinity for $\left|H^{4}\right|_{\mathbf{e}} \sim r^{-4}$,
\item[-] Denoting $\Omega_{s}^{\prime}$ the interior of $\Psi^{*}\left(s S^{3} / \Gamma\right)$,
$$\lim _{s \rightarrow \infty} \operatorname{Vol}_{\mathbf{g}_{b}} \Omega_{s}^{\prime}-\operatorname{Vol}_{\mathbf{e}}\left(B_{\mathbf{e}}(s) / \Gamma\right)=0,$$
\item[-] $\delta_{\mathbf{e}} H^{4}=0, \operatorname{tr}_{\mathbf{e}} H^{4}=0, H^{4}\left(\partial_{r}, \partial_{r}\right)=c(\Gamma) \mathcal{V}\left(N, \mathbf{g}_{b}\right)$ for $c(\Gamma)>0$.
\item[-] more precisely,
$$H^{4}=\frac{\sum_{i j} h_{i j}^{+} \theta_{i}^{-} \circ \omega_{j}^{+}+\sum_{k l} h_{k l}^{-} \theta_{k}^{+} \circ \omega_{l}^{-}}{r^{4}} .$$
with $\sum_{i} h_{i i}^{+}+\sum_{k} h_{k k}^{-}=c(\Gamma) \mathcal{V}\left(N, \mathbf{g}_{b}\right) \leqslant 0$ as in the previous point.
\end{itemize}

As in Proposition A. 1 in the Appendix, we see the term $H^{4}$ in this volume gauge as only determined by the curvature at infinity and the reduced volume.

Proposition 3.13. Let $\left(N, \mathbf{g}_{b}\right)$ be a non flat Ricci-flat $A L E$ orbifold asymptotic to $\mathbb{R}^{4} / \Gamma$ for $\Gamma \subset S O(4)$ with reduced volume $\mathcal{V}\left(N, \mathbf{g}_{b}\right)<0$.

Then, in volume gauge as in Definition 3.12, up to changing the bases $\left(\omega_{i}^{+}\right)_{i}$ and $\left(\omega_{k}^{-}\right)_{k}$ to diagonalize the curvature, one has the asymptotic $\mathbf{g}_{b}=\mathbf{e}+H^{4}+\mathcal{O}\left(r^{-5}\right)$ with
$$H^{4}=-\frac{\sum_{i} h_{i i}^{+} \theta_{i}^{-} \circ \omega_{i}^{+}+\sum_{k} h_{k k}^{-} \theta_{k}^{+} \circ \omega_{l} k-}{r^{4}}$$
with $\sum_{i} h_{i i}^{+}+\sum_{k} h_{k k}^{-}=-c(\Gamma) \mathcal{V}\left(N, \mathbf{g}_{b}\right)>0$ and the induced asymptotic curvature in the basis $\left(\theta_{i}^{ \pm}\right)_{i}$ satisfies
$$\mathbf{R}_{\mathbf{e}}^{\mp,(1)}\left(H^{4}\right)=\frac{8}{r^{6}}\left[\begin{array}{ccc}
2 h_{11}^{ \pm}-h_{22}^{ \pm}-h_{33}^{ \pm} & 0 & 0 \\
0 & -h_{11}^{ \pm}+2 h_{22}^{ \pm}-h_{33}^{ \pm} & 0 \\
0 & 0 & -h_{11}^{ \pm}-h_{22}^{ \pm}+2 h_{33}^{ \pm}
\end{array}\right] .$$

Remark 3.14. It is possible that the curvature of $\left(N, \mathbf{g}_{b}\right)$ is decaying faster than $r^{-6}$. In this case, the $H^{4}$ term is purely a gauge term of the form:
$$\frac{1}{r^{4}} \sum_{i} \theta_{i}^{-} \circ \omega_{i}^{+}=\frac{1}{r^{4}} \sum_{k} \theta_{k}^{+} \circ \omega_{k}^{-}=\frac{3 d r^{2}-r^{2} g_{\mathbb{S}^{3}}}{r^{4}}=\frac{1}{2} \operatorname{Hess}_{\mathbf{e}}\left(r^{-2}\right) .$$
See Remark 4.8 below for an example.
Proof. We first check that $H_{+}^{4}:=-\sum_{i} h_{i i}^{+} \frac{\theta_{i}^{-} \circ \omega_{i}^{+}}{r^{4}}$ only induces anti-selfdual curvature at the first order. The linearization at e of the induced connection on $\Omega^{+}$is actually zero since $d\left(\frac{\theta_{i}^{+}}{r^{4}}\right)=0$ and therefore the induced selfdual curvature vanishes as well. This also shows that the term is in Bianchi gauge.

In order to compute the induced curvature, one uses Kronheimer's examples. In particular the curvature of the Eguchi-Hanson metric which with $H^{4}=-\frac{\theta_{1}^{-} \circ \omega_{1}^{+}}{2 r^{4}}$ induces the curvature
$$\mathbf{R}_{\mathbf{e}}^{\mp,(1)}\left(H^{4}\right)=\frac{4}{r^{6}}\left[\begin{array}{ccc}
2 & 0 & 0 \\
0 & -1 & 0 \\
0 & 0 & -1
\end{array}\right] .$$
by [EH78]. By linearity, one attains any $H^{4}$ as above, and the result follows. \(\square\)

In the CMC gauge of Definition 3.8, we find a simpler expression.
Corollary 3.15. Let $\left(N, \mathbf{g}_{b}\right)$ be a Ricci-flat ALE orbifold asymptotic to $\mathbb{R}^{4} / \Gamma$ for $\Gamma \subset$ $S O(4)$. Then, in $C M C$ gauge as in Definition 3.8, up to changing the bases $\left(\omega_{i}^{+}\right)_{i}$ and $\left(\omega_{k}^{-}\right)_{k}$ to diagonalize the curvature, one has $\mathbf{g}_{b}=\mathbf{e}+H^{4}+\mathcal{O}\left(r^{-5}\right)$ with
$$H^{4}=-\frac{\sum_{i} h_{i i}^{+} \theta_{i}^{-} \circ \omega_{i}^{+}+\sum_{k} h_{k k}^{-} \theta_{k}^{+} \circ \omega_{l} k-}{r^{4}}$$
with $\sum_{i} h_{i i}^{ \pm}=0$ and the induced asymptotic curvature satisfies in the basis $\left(\theta_{i}^{ \pm}\right)_{i}$
$$\mathbf{R}_{\mathbf{e}}^{\mp,(1)}\left(H^{4}\right)=\frac{24}{r^{6}}\left[\begin{array}{ccc}
h_{11}^{ \pm} & 0 & 0 \\
0 & h_{22}^{ \pm} & 0 \\
0 & 0 & h_{33}^{ \pm}
\end{array}\right] .$$
3.2.2. (Anti-)Selfdual Einstein deformations.

Proposition 3.16. If $H^{4}$, the $r^{-4}$-asymptotic term of a Ricci-flat ALE metric only induces an anti-selfdual (or selfdual) curvature, then it satisfies the obstructions (26) and (32).

Proof. By [BH19] or Proposition 3.13, up to a gauge term, we can assume that $H^{4}$ is a linear combination of $\frac{\theta_{i}^{-} \circ \omega_{i}^{+}}{r^{4}}$ terms.

Thanks to Kronheimer's examples, we can reach any term of the form $-\sum_{i} h_{i i}^{+} \frac{\theta_{i}^{-} \omega_{i}^{+}}{r^{4}}$ with $h_{i i}^{+} \geqslant 0$. This condition $h_{i i}^{+} \geqslant 0$ can always be arranged up to adding a gauge term as in Remark 3.14. Since gauge terms do not matter in satisfying the obstructions (26) and (32) by Proposition 1.6, we obtain the result. \(\square\)
3.2.3. General deformations.

Proposition 3.17. Let $\left(N, \mathbf{g}_{b}\right)$ be a Ricci-flat ALE metric whose asymptotic term in CMC gauge is: $H_{+}^{4}+H_{-}^{4}$ where
$$H_{+}^{4}:=-\sum_{i} h_{i i}^{+} \frac{\theta_{i}^{-} \circ \omega_{i}^{+}}{r^{4}} \text { and } H_{-}^{4}:=-\sum_{k} h_{k k}^{-} \frac{\theta_{k}^{+} \circ \omega_{k}^{-}}{r^{4}} .$$
Then, the obstructions (27) and (32) are satisfied.
Proof. Let us consider $H_{+}^{4}:=-\sum_{i} h_{i i}^{+} \frac{\theta_{i}^{-} \circ \omega_{i}^{+}}{r^{4}}$ and $H_{-}^{4}:=-\sum_{k} h_{k k}^{-} \frac{\theta_{k}^{+} \circ \omega_{k}^{-}}{r^{4}}$ satisfying $\sum_{i} h_{i i}^{+}=$ $\sum_{k} h_{k k}^{-}=0$. Recall that these terms only induce a nonvanishing connection respectively in the anti-selfdual and selfdual orientation and the formula
$$\theta_{i}^{ \pm}=\sum_{k}\left\langle\omega_{i}^{\mp}\left(\partial_{r}\right), \omega_{l}^{ \pm}\left(\partial_{r}\right)\right\rangle \omega_{l}^{ \pm} .$$
From the formula (48) and Corollary 3.15, we therefore find:
$$\operatorname{Ric}_{\mathbf{e}}^{(2)}\left(H_{+}^{4}, H_{-}^{4}\right)=24 \sum_{i} \sum_{k} h_{i i}^{+} h_{k k}^{-} \frac{\left\langle\omega_{k}^{-}\left(\partial_{r}\right), \omega_{i}^{+}\left(\partial_{r}\right)\right\rangle \theta_{i}^{-} \circ \theta_{k}^{+}}{r^{10}}$$

Now, using the fact that $\theta_{i}^{\mp}\left(\partial_{r}\right)=\omega_{i}^{\mp}\left(\partial_{r}\right)$, we see that the obstruction of Proposition 2.8 is proportional to
$$\sum_{i, k} h_{i i}^{+} h_{k k}^{-} \int_{\mathbb{S}^{3}}\left\langle\omega_{k}^{-}\left(\partial_{r}\right), \omega_{i}^{+}\left(\partial_{r}\right)\right\rangle_{\mathbf{e}^{2}}^{2} d v_{\mathbb{S}^{3}}$$
Since both $\sum_{i} h_{i i}^{+}=0$ and $\sum_{k} h_{k k}^{-}=0$, the obstruction (37) is satisfied. The proof is similar for the other obstructions (36). \(\square\)

\section*{4. Obstruction to the desingularization of Einstein metrics}

We finally recover the obstructions of [Biq13] to the desingularization of Einstein metrics and many of the additional obstructions of [Ozu19b] (but not the higher order obstructions of [Ozu20]). We conclude this section by proving that some Einstein orbifolds cannot be desingularized by smooth Einstein manifolds.
4.1. Infinitesimal Einstein deformations of Ricci-flat ALE metrics. On $\left(\mathbb{R}^{4} / \Gamma, g_{\mathbf{e}}\right)$, the vector field $r \partial_{r}$ is a conformal Killing vector field. It is moreover half of the gradient of the function $u:=r^{2}$ which is a solution to $-\nabla_{\mathbf{e}}^{*} \nabla_{\mathbf{e}} u=8$, and we have $\frac{1}{2} \mathcal{L}_{\nabla_{\mathbf{e}} u} \mathbf{e}=$ $\operatorname{Hess}_{\mathbf{e}} u=2 \mathbf{e}$. On a Ricci-flat ALE orbifold we can extend this situation on the whole space as follows.

Proposition 4.1 ([BH19, Ozu19b]). Let $\left(N, \mathbf{g}_{b}\right)$ be a Ricci-flat ALE orbifold asymptotic to $\mathbb{R}^{4} / \Gamma$. Then, there exists a unique vector field $X$ on ( $N, \mathbf{g}_{b}$ ) such that $\Phi^{*} X=r \partial_{r}+$ $o(r)$, and $\nabla_{\mathbf{g}_{b}}^{*} \nabla_{\mathbf{g}_{b}} X=0$. We actually have $X=\frac{1}{2} \nabla_{\mathbf{g}_{b}} u$, where $u$ is the unique solution of $-\nabla_{\mathbf{g}_{b}}^{*} \nabla_{\mathbf{g}_{b}} u=8$, such that $u=r^{2}+o(1)$. Moreover, $\left(\mathcal{L}_{X} \mathbf{g}_{b}\right)^{\circ}=\mathcal{L}_{X} \mathbf{g}_{b}-2 \mathbf{g}_{b}$, the traceless part of $\mathcal{L}_{X} \mathbf{g}_{b}$ is an infinitesimal Ricci-flat deformation of $\mathbf{g}_{b}$ which is trace-free and divergence-free. \(\square\)

Proposition 4.2 ([BH19, Section 4]). Let $\left(N, \mathbf{g}_{b}\right)$ be a Ricci-flat ALE orbifold asymptotic to $\mathbb{R}^{4} / \Gamma$. Then for any Killing vector field $Y$ on $\mathbb{R}^{4} / \Gamma$, there exists a unique vector field $Y^{\prime}$ on $\left(N, \mathbf{g}_{b}\right)$ such that $Y^{\prime}=Y+o(r)$. Moreover the infinitesimal deformation $\mathcal{L}_{Y^{\prime}} \mathbf{g}_{b}$ is divergence-free and trace-free. It vanishes if and only if $Y^{\prime}$ is a Killing vector field of $\mathbf{g}_{b}$. \(\square\)

Remark 4.3. All of the infinitesimal Einstein deformations of the Eguchi-Hanson metric (42) are of the above types.
4.2. Obstructions to the desingularization. Let us now show that we recover the obstructions of [Biq13, Ozu19b] and find another expression for them. This new expression will further highlight the link between these obstructions and the lack of integrability of Einstein desingularizations of [Ozu20t, Chapter 4].

Lemma 4.4. Let $\left(N, \mathbf{g}_{b}\right)$ be a Ricci-flat ALE metric in volume gauge as in Definition 3.12. And consider its development at infinity in this gauge: $\mathbf{g}_{b}=\mathbf{e}+H^{4}+o\left(r^{-4}\right)$. Then, for $\left(\mathcal{L}_{X} \mathbf{g}_{b}\right)^{\circ} \in \mathbf{O}\left(\mathbf{g}_{b}\right)$ defined in Proposition 4.1, we have:
$$\left(\mathcal{L}_{X} \mathbf{g}_{b}\right)^{\circ}=-2 H^{4}+o\left(r^{-4}\right)$$
Proof. Let us denote $\Omega_{s}^{\prime}$ the open interior of the hypersurface $\Psi\left(s \mathrm{~S}^{3} / \Gamma\right)$ for the volume gauge diffeomorphism $\Psi:\left(\mathbb{R}^{4} / \Gamma\right) \backslash B_{\mathbf{e}}\left(s_{0}\right) \mapsto N$ of Definition 3.12 for $s_{0}$ large enough. All along the proof we will abusively omit the diffeomorphism $\Psi$ when pulling back tensors on the infinity of $N$ to $\mathbb{R}^{4} / \Gamma$. By Definition 3.12, we have as $s \rightarrow \infty$
$$\operatorname{Vol}_{\mathbf{e}}\left(B_{\mathbf{e}}(s) / \Gamma\right)=\operatorname{Vol}_{\mathbf{g}_{b}} \Omega_{s}^{\prime}+o(1)$$

The first step in order to find the asymptotic of $\left(\mathcal{L}_{X} \mathbf{g}_{b}\right)^{\circ}$ is to recall that $X=\frac{1}{2} \nabla_{\mathbf{g}_{b}} u$ where $u$ satisfies $\Delta_{\mathbf{g}_{b}} u=8$ with $u=r^{2}+\frac{b}{r^{2}}+o\left(r^{-2}\right)$ for some $b \in \mathbb{R}$ similarly to [BH19]. We determine $b$ by integrating by parts $\Delta_{\mathbf{g}_{b}} u=8$ as in [BH19]:
$$\begin{aligned}
8 \operatorname{Vol}_{\mathbf{e}}\left(B_{\mathbf{e}}(s) / \Gamma\right) & =8 \operatorname{Vol}_{\mathbf{g}_{b}} \Omega_{s}^{\prime}+o(1) \\
& =\int_{\Omega_{s}^{\prime}} \Delta_{\mathbf{g}_{b}} u d v_{\mathbf{g}_{b}}+o(1) \\
& =8 \operatorname{Vol}_{\mathbf{e}}\left(B_{\mathbf{e}}(s) / \Gamma\right)-2 b\left|\mathbb{S}^{3} / \Gamma\right|-2 r H^{4}\left(\partial_{r}, \partial_{r}\right)+o(1)
\end{aligned}$$
which gives us $b=-r^{4} H^{4}\left(\partial_{r}, \partial_{r}\right)$ again mimicking computations of [BH19] in our slightly different coordinates.

Remark 4.5. This is consistent with eh for which $X=r \partial_{r}=\frac{1}{2} \nabla_{\mathbf{e h}} \sqrt{1+r^{4}}$ where $u=\sqrt{1+r^{4}}$ satisfies $\Delta_{\mathbf{e h}} u=8$, and $\sqrt{1+r^{4}}=r^{2}+\frac{1}{2 r^{2}}+o\left(r^{-2}\right)$. We moreover have Hess ${ }_{\mathbf{e h}} \sqrt{1+r^{4}}=2\left(\mathbf{e h}+\left(\mathcal{L}_{X} \mathbf{e h}\right)^{\circ}\right)$ according to [Biq13, Proof of Proposition 2.1].

As in the case of eh in (42), where $\nabla_{\mathbf{e h}} \sqrt{1+r^{4}}=2 r \partial_{r}$, developing $\nabla_{\mathbf{g}_{b}}=\nabla_{\mathbf{e}}+$ $\nabla_{\mathbf{e}}^{(1)}\left(H^{4}\right)+\ldots$, we find $\nabla_{\mathbf{g}_{b}} u=2 r \partial_{r}+o\left(r^{-4}\right)$. This implies that at infinity, we have the stated result, namely:
$$\left(\mathcal{L}_{X} \mathbf{g}_{b}\right)^{\circ}=\mathcal{L}_{r \partial_{r}} H^{4}+o\left(r^{-4}\right)=-2 H^{4}+o\left(r^{-4}\right) .$$ \(\square\)

This lets us state the following obstruction result.
Theorem 4.6. Let ( $M_{o}, \mathbf{g}_{o}$ ) be an Einstein orbifold with a singularity $\mathbb{R}^{4} / \Gamma$ and let ( $N, \mathbf{g}_{b}$ ) be a Ricci-flat ALE manifold with integrable Ricci-flat ALE deformations asymptotic to $\mathbb{R}^{4} / \Gamma$. Let us denote $H^{4}$ the asymptotic term of $\mathbf{g}_{b}$ in volume gauge as in Definition 3.12: $\mathbf{g}_{b}=\mathbf{e}+H^{4}+\mathcal{O}\left(r^{-5}\right)$, and let $H_{2}$ be the quadratic terms of $\mathbf{g}_{o}=\mathbf{e}+H_{2}+\mathcal{O}\left(r^{3}\right)$ in a coordinate system in which $B_{\mathbf{e}}\left(H_{2}\right)=0$.

Assume that there exists a sequence of Einstein metrics, $\left(M, \mathbf{g}_{n}\right)_{n}, d_{G H}$-converging to $\left(M_{o}, \mathbf{g}_{o}\right)$ and such that there exists a sequence $\left(t_{n}\right)_{n \in \mathbb{N}}$ with $t_{n}>0$ satisfying: $\left(M, \frac{\mathbf{g}_{n}}{t_{n}}\right) \xrightarrow[G H]{ }$ $\left(N, \mathbf{g}_{b}\right)$. Then, we have the following obstructions:
\begin{itemize}
\item[-] for any Killing vector field $Y_{i}^{ \pm}$,
$$\int_{\mathbb{S}^{3}}\left(\operatorname{Ric}_{\mathbf{e}}^{(2)}\left(H_{2}, H^{4}\right)\right)\left(Y_{i}^{ \pm}, \partial_{r}\right) d v_{\mathbb{S}^{3}}=0$$
\item[-] for the conformal Killing vector field $r \partial_{r}$, we have
$$\int_{\mathbb{S}^{3}}\left(\operatorname{Ric}_{\mathbf{e}}^{(2)}\left(H_{2}, H^{4}\right)\right)\left(r \partial_{r}, \partial_{r}\right) d v_{\mathbb{S}^{3}}=0 .$$
\end{itemize}

Remark 4.7. As we will see in Corollary 4.11 proven later, the obstruction (54) is never trivial if $\left(N, \mathbf{g}_{b}\right)$ is not flat. That is, if $\left(N, \mathbf{g}_{b}\right)$ is not flat, then there are some $H_{2}$ as above for which (54) is not satisfied.

Remark 4.8. By [Auv18], the asymptotic terms of Kronheimer's instantons in volume gauge are generally of the form: $H^{4}=-\sum_{i, j}\left\langle\zeta_{i}, \zeta_{j}\right\rangle \frac{\theta_{i}^{-} \circ \omega_{j}^{+}}{2 r^{4}}$ for $\zeta_{1}, \zeta_{2}, \zeta_{3} \in \mathbb{R}^{k}$ for some $k$ arbitrarily large depending on the group at infinity ( $k=1$ for the Eguchi-Hanson metric). For $k \geqslant 3$ we can construct $\zeta_{1}, \zeta_{2}, \zeta_{3} \in \mathbb{R}^{k}$ with $\left\langle\zeta_{i}, \zeta_{j}\right\rangle=\delta_{i j}$ and we check that the obstructions (53) vanishes for any $H_{2}$.

Proof. Let us come back to the origin of the obstructions of [Ozu19b, Ozu20t]. They are the obstructions to solving:
$$\left\{\begin{aligned}
\operatorname{Ric}_{\mathbf{g}_{b}}^{(1)}\left(h_{2}\right) & =0 \\
h_{2} & =H_{2}+H_{2}^{4}+\mathcal{O}\left(r^{-3+\epsilon}\right),
\end{aligned}\right.$$
where $\left|H_{2}^{4}\right|_{\mathbf{e}} \sim r^{-2}$, see [Ozu20].
Let us consider the harmonic vector field $X=r \partial_{r}+\mathcal{O}\left(r^{-3}\right)$ and the harmonic vector fields $Y_{i}^{\prime}=Y_{i}+\mathcal{O}\left(r^{-3}\right)$ defined in Section 4.1. Following the computation of [Biq13, Ozu19b], noting that in volume gauge, we have $\left(\mathcal{L}_{X} \mathbf{g}_{b}\right)^{\circ}=-2 H^{4}+o\left(r^{-4}\right)$ by Lemma 4.4 and we moreover have:
$$\begin{aligned}
0 & =\frac{1}{2} \lim _{R \rightarrow+\infty} \int_{\{r \leqslant R\}}\left\langle\operatorname{Ric}_{\mathbf{g}_{b}}^{(1)}\left(h_{2}\right),\left(\mathcal{L}_{X} \mathbf{g}_{b}\right)^{\circ}\right\rangle_{\mathbf{g}_{b}} d v_{\mathbf{g}_{b}} \\
& =2 \int_{\mathbb{S}^{3} / \Gamma} 3\left\langle H_{2}, H^{4}\right\rangle+H^{4}\left(B_{\mathbf{e}} H_{2}, \partial_{r}\right) d v_{\mathbb{S}^{3} / \Gamma}
\end{aligned}$$
which is manifestly linear in $H^{4}$. Similarly, for any Killing vector field $Y_{i}$ and its harmonic extension $Y_{i}^{\prime}$, we find the obstructions:
$$\int_{\mathbb{S}^{3} / \Gamma} 3\left\langle H_{2}, \mathcal{L}_{Y_{i}} H^{4}\right\rangle+\mathcal{L}_{Y_{i}} H^{4}\left(B_{\mathbf{e}} H_{2}, \partial_{r}\right) d v_{\mathbb{S}^{3} / \Gamma}=0$$

Now, the interpretation of Biq13, Biq16 of the obstruction tells us that for some $C=C(\Gamma) \neq 0$, for any $k, l \in\{1,2,3\}$
$$\int_{\mathbb{S}^{3} / \Gamma}\left\langle H_{2}, \frac{\theta_{k}^{\mp} \circ \omega_{l}^{ \pm}}{r^{4}}\right\rangle d v_{\mathbb{S}^{3} / \Gamma}=C\left\langle\mathbf{R}_{\mathbf{e}}^{ \pm,(1)}\left(H_{2}\right)\left(\omega_{k}^{ \pm}\right), \omega_{l}^{ \pm}\right\rangle .$$
By linearity, this lets us compute the obstruction for any $H^{4}$ coming from a volume gauge.
On the other hand, let us use the formalism of [Biq16] and compute the second variation $\operatorname{Ric}_{\mathbf{e}}^{(2)}\left(H_{2}, H^{4}\right)$ when $B_{\mathbf{e}}\left(H_{2}\right)=0$. For the quadratic terms $H_{2}$ of the orbifold, we decompose
$$\mathbf{R}_{\mathbf{e}}^{+,(1)}\left(H_{2}\right)=\sum_{i j} R_{i j}^{+} \omega_{i}^{+} \otimes \omega_{j}^{+},$$
and we will consider another term of the form $H^{4}=\frac{\theta_{l}^{-} \circ \omega_{k}^{+}}{r^{4}}$. Using the formula (48) for the second variation of the traceless part of the Ricci curvature denoted Ric applied to the hyperkähler flat metric e in the direction $H^{4}+H_{2}$, we find
$$\operatorname{Ric}_{\mathbf{e}}^{(2)}\left(H^{4}, H_{2}\right)=\sum_{j} R_{k j}^{+} \frac{\theta_{l}^{-} \circ \omega_{j}^{+}}{r^{4}} .$$
Now, this lets us compute the obstruction (53). For any $i \in\{1,2,3\}$, define $(i l) \in\{1,2,3\}$ by $\omega_{i}^{+} \circ \omega_{(i l)}^{+}= \pm \omega_{l}^{+}$. We find the following value for (53) with Killing vector field $Y_{(i l)}^{+}=$ $\omega_{(i l)}^{+}\left(r \partial_{r}\right)$ :
$$\begin{aligned}
0 & =\sum_{j} R_{k j}^{+} \int_{\mathbb{S}^{3}}\left\langle\theta_{l}^{-}\left(\partial_{r}\right), \omega_{j}^{+}\left(\omega_{(i l)}^{+}\left(r \partial_{r}\right)\right)\right\rangle_{\mathbf{e}} d v_{\mathbb{S}^{3}} \\
& = \pm R_{k i}^{+} \int_{\mathbb{S}^{3}}\left\langle Y_{l}^{-}, Y_{l}^{-}\right\rangle_{\mathbf{e}} d v_{\mathbb{S}^{3}}
\end{aligned}$$
We therefore see that if (57) with $Y_{(i l)}^{+}$, is satisfied, then, one has (53) satisfied thanks to (58). Similarly, from the obstruction (54), we find:
$$\begin{aligned}
0 & =\sum_{j} R_{k j}^{+} \int_{\mathbb{S}^{3}}\left\langle\theta_{l}^{-}\left(\partial_{r}\right), \omega_{j}^{+}\left(r \partial_{r}\right)\right\rangle_{\mathbf{e}} d v_{\mathbb{S}^{3}} \\
& =\sum_{j} R_{k j}^{+} \int_{\mathbb{S}^{3}}\left\langle Y_{l}^{+}, Y_{j}^{+}\right\rangle_{\mathbf{e}} d v_{\mathbb{S}^{3}} \\
& =R_{k l}^{+} \int_{\mathbb{S}^{3}}\left\langle Y_{l}^{+}, Y_{l}^{+}\right\rangle_{\mathbf{e}} d v_{\mathbb{S}^{3}}
\end{aligned}$$
and we consequently see that the condition (54) is the same as (56) thanks to (58). \(\square\)

Remark 4.9. It might seem like the proof of Theorem 4.6 is completely disjoint from the obstruction of Theorem 2.8 or those of Section 2.3. We illustrate below that they actually build on estimates of the exact same quantity but rely on different integrations by parts. Indeed, as noticed along the proof of Lemma 4.4 a special feature of the volume gauge is that $\nabla_{\mathbf{g}_{b}} u \sim r \partial_{r}$ at an order higher than expected.

Let us illustrate this with the Eguchi-Hanson metric eh which was already discussed in Section 2.3. Coming back to the integral quantity in (56) and integrating by parts in the other direction thanks to (20), we find:
$$\begin{aligned}
0 & =\lim _{R \rightarrow+\infty} \int_{\{r=R\}}\left(\operatorname{Ric}_{\mathbf{e h}}^{(1)}\left(h_{2}\right)\right)\left(r \partial_{r}, \partial_{r}\right) d v_{\mathbf{e h} \mid\{r=R\}} \\
& =\frac{1}{2} \lim _{R \rightarrow+\infty} \int_{\{r \leqslant R\}}\left\langle\left(\operatorname{Ric}_{\mathbf{e h}}^{(1)}\left(h_{2}\right)\right), \mathcal{L}_{r \partial_{r}} \mathbf{e h}\right\rangle_{\mathbf{e h}} d v_{\mathbf{e h}} \\
& =\frac{1}{2} \lim _{R \rightarrow+\infty} \int_{\{r \leqslant R\}}\left\langle\left(\operatorname{Ric}_{\mathbf{e h}}^{(1)}\left(h_{2}\right)\right),\left(\mathcal{L}_{r \partial_{r}} \mathbf{e h}\right)^{\circ}\right\rangle_{\mathbf{e h}} d v_{\mathbf{e h}}
\end{aligned}$$
The left-hand side term of (62) has the following limit as $R \rightarrow+\infty$ :
$$\begin{aligned}
0 & =\int_{\mathbb{S}^{3} / \mathbb{Z}_{2}}\left(\mathrm{E}_{\mathbf{e}}^{(1)}\left(H_{2}^{4}\right)+\mathrm{E}_{\mathbf{e}}^{(2)}\left(H^{4}, H_{2}\right)+\lambda H^{4}\right)\left(r \partial_{r}, \partial_{r}\right) d v_{\mathbb{S}^{3} / \mathbb{Z}_{2}} \\
& =\int_{\mathbb{S}^{3} / \mathbb{Z}_{2}}\left(\mathrm{E}_{\mathbf{e}}^{(1)}\left(H_{2}^{4}\right)\right)\left(r \partial_{r}, \partial_{r}\right) d v_{\mathbb{S}^{3} / \mathbb{Z}_{2}}+\int_{\mathbb{S}^{3} / \mathbb{Z}_{2}}\left(\operatorname{Ric}_{\mathbf{e}}^{(2)}\left(H^{4}, H_{2}\right)\right)\left(r \partial_{r}, \partial_{r}\right) d v_{\mathbb{S}^{3} / \mathbb{Z}_{2}}
\end{aligned}$$
which is exactly the quantity obtained in (43). As in Section 2.3, we may use $H_{2}^{4}=0$.

We recover all of the obstructions of [Biq13].
Corollary 4.10. With the assumptions of Theorem 4.6 with $\left(N, \mathbf{g}_{b}\right)=\left(T^{*} \mathbb{S}^{2}, \mathbf{e h}\right)$ defined in (42) with $H^{4}=-\frac{\theta_{1}^{-} \circ \omega_{1}^{+}}{2 r_{\mathbf{e}}^{4}}$ and any $H_{2}$ satisfying $B_{\mathbf{e}}\left(H_{2}\right)=0$, the following propositions are equivalent:
\begin{itemize}
\item[(1)] $\mathbf{R}_{\mathbf{e}}^{+,(1)}\left(H_{2}\right) \omega_{1}^{+}=0$,
\item[(2)] $\int_{\mathbb{S}^{3} / \mathbb{Z}_{2}}\left(\operatorname{Ric}_{\mathbf{e}}^{(2)}\left(H^{4}, H_{2}\right)\right)\left(r \partial_{r}, \partial_{r}\right) d v_{\mathbb{S}^{3} / \mathbb{Z}_{2}}=0$, and for any $i \in\{2,3\}$ for the Killing vector field $Y_{i}^{+}, \int_{\mathbb{S}^{3} / \mathbb{Z}_{2}}\left(\operatorname{Ric}_{\mathbf{e}}^{(2)}\left(H^{4}, H_{2}\right)\right)\left(Y_{i}^{+}, \partial_{r}\right) d v_{\mathbb{S}^{3} / \mathbb{Z}_{2}}=0$,
\item[(3)] there is a solution $h_{2}$ to the equation (55),
\item[(4)] $\int_{\mathbb{S}^{3} / \mathbb{Z}_{2}}\left\langle H_{2}, H^{4}\right\rangle d v_{\mathbb{S}^{3} / \mathbb{Z}_{2}}=0$, and $i \in\{2,3\}: \int_{\mathbb{S}^{3} / \mathbb{Z}_{2}}\left\langle H_{2}, \mathcal{L}_{Y_{i}^{+}} H^{4}\right\rangle d v_{\mathbb{S}^{3} / \mathbb{Z}_{2}}=0$.
\end{itemize}
4.3. Spherical and hyperbolic orbifolds. Using the above new interpretation of the obstruction to the desingularization of Einstein 4-manifolds as well as the integration by parts (20), we prove one of the main conjectures of [Ozu19b, Ozu20t] and answer the longstanding question of whether or not Einstein orbifolds can always be $d_{G H}$-desingularized by smooth Einstein metrics.

The starting point is that the obstruction (54) never vanishes when the orbifold is spherical or hyperbolic.

Corollary 4.11. If the obstruction (54) vanishes, then, the orbifold $\left(M_{o}, \mathbf{g}_{o}\right)$ is not spherical or hyperbolic.

Proof. Let us consider $H^{4}=\sum_{i j} h_{i j}^{+} \frac{\theta_{i}^{-} \circ \omega_{j}^{+}}{r^{4}}+\sum_{k l} h_{k l}^{-} \frac{\theta_{k}^{+} \circ \omega_{l}^{-}}{r^{4}}$. From (59), by linearity, we have the following expression:
$$\operatorname{Ric}_{\mathbf{e}}^{(2)}\left(H^{4}, H_{2}\right)=\sum_{i j m} h_{i j}^{+} R_{j m}^{+} \frac{\theta_{i}^{-} \circ \omega_{m}^{+}}{r^{4}}+\sum_{k l n} h_{k l}^{-} R_{l n}^{-} \frac{\theta_{k}^{+} \circ \omega_{n}^{-}}{r^{4}},$$
hence, the obstruction (54) rewrites:
$$\sum_{i j} h_{i j}^{+} R_{j i}^{+}+\sum_{k l} h_{k l}^{-} R_{l k}^{-}=0 .$$
Denoting $\Lambda=\sum_{i} R_{i i}^{+}=\sum_{k} R_{k k}^{-},\left(W_{i j}^{ \pm}\right)_{i j}$ the traceless part of $\left(R_{i j}^{ \pm}\right)_{i j}$, and $\stackrel{\circ}{h}_{i j}^{ \pm}$the traceless part of $\left(h_{i j}^{ \pm}\right)_{i, j \in\{1,2,3\}}$ (note that the $\stackrel{\circ}{h}_{i j}^{ \pm}$are proportional to the asymptotic curvature of $\mathbf{g}_{b}$ by Proposition 3.13) and recall that $\sum_{i} h_{i i}^{+}+\sum_{k} h_{k k}^{-}=c(\Gamma) \mathcal{V}\left(N, \mathbf{g}_{b}\right)<0$. We therefore write (64) as
$$0=\Lambda c(\Gamma) \mathcal{V}\left(N, \mathbf{g}_{b}\right)+\sum_{i j} \stackrel{\circ}{h}_{i j}^{+} W_{j i}^{+}+\sum_{k l} \stackrel{\circ}{h}_{k l}^{-} W_{l k}^{-}$$
In the case of a spherical or hyperbolic orbifold, we have $W^{ \pm}=0$ and $\Lambda \neq 0$, therefore, since $c(\Gamma) \mathcal{V}\left(N, \mathbf{g}_{b}\right)<0$, the obstruction (65) is not satisfied. \(\square\)
4.3.1. Cokernel of the linearization of E at a Ricci-flat ALE metric. Let us consider a Ricci-flat ALE orbifold ( $N, \mathbf{g}_{b}$ ), the operator
$$g \mapsto \mathbf{\Phi}_{\mathbf{g}_{b}}(g):=\mathrm{E}(g)+\delta_{\mathbf{g}_{b}}^{*} \delta_{\mathbf{g}_{b}} g,$$
and $\mathbf{O}\left(\mathbf{g}_{b}\right)$ the $L^{2}\left(\mathbf{g}_{b}\right)$-kernel of $\boldsymbol{\Phi}_{\mathbf{g}_{b}}^{(1)}$, the linearization of $\boldsymbol{\Phi}_{\mathbf{g}_{b}}$ at $\mathbf{g}_{b}$. Note that the elements of $\mathbf{O}\left(\mathbf{g}_{b}\right)$ are traceless and divergence-free, see [Ozu19b] for instance. According to [Ozu19b, Ozu20t], for any small enough $v \in \mathbf{O}\left(\mathbf{g}_{b}\right)$, there exists a unique metric $g_{v}$ which satisfies both
$$\boldsymbol{\Phi}_{\mathbf{g}_{b}}\left(g_{v}\right)=\mathrm{E}\left(g_{v}\right)+\delta_{\mathbf{g}_{b}}^{*} \delta_{\mathbf{g}_{b}} g_{v} \in \mathbf{O}\left(\mathbf{g}_{b}\right) \text { and } g_{v}-\left(\mathbf{g}_{b}+v\right) \perp_{L^{2}\left(\mathbf{g}_{b}\right)} \mathbf{O}\left(\mathbf{g}_{b}\right) .$$

We will use the following Lemma in order to prove Proposition 0.12.

Lemma 4.12. Assume that for all $k \leqslant l-1, \partial_{s^{k} \mid s=0}^{k} \boldsymbol{\Phi}_{\mathbf{g}_{b}}\left(g_{s v}\right)=0$. Then, we have
\begin{itemize}
\item[(1)] for all $k \leqslant l-1$, we have: $\partial_{s^{k} \mid s=0}^{k} \mathrm{E}\left(g_{s v}\right)=0$, and for all $k \leqslant l$, we have $\delta_{\mathbf{g}_{b}} \partial_{s^{k} \mid s=0}^{k} g_{s v}=0$,
\item[(2)] $\delta_{\mathbf{g}_{b}}\left(\partial_{s^{l} \mid s=0}^{l} \boldsymbol{\Phi}_{\mathbf{g}_{b}}\left(g_{s v}\right)-\boldsymbol{\Phi}_{\mathbf{g}_{b}}^{(1)}\left(\partial_{s^{l} \mid s=0}^{l} g_{s v}\right)\right)=0$, and
\item[(3)] for some multilinear function $Q_{g}^{(l)}\left(h_{1}, \ldots, h_{l}\right)=\sum_{m \geqslant 2} \sum_{j_{1}, \ldots, j_{m} \geqslant 1}^{l} \nabla_{g} h_{j_{1}} * h_{j_{2}} * \ldots *$ $h_{j_{m}}$, where $*$ denotes various contractions of the tensors, we have:
$$\int_{\Omega}\left\langle\mathbf{g}_{b}, \partial_{s^{l} \mid s=0}^{l} \boldsymbol{\Phi}_{\mathbf{g}_{b}}\left(g_{s v}\right)-\boldsymbol{\Phi}_{\mathbf{g}_{b}}^{(1)}\left(\partial_{s^{l} \mid s=0}^{l} g_{s v}\right)\right\rangle_{\mathbf{g}_{b}} d v_{\mathbf{g}_{b}}=\int_{\partial \Omega} Q^{(l)}\left(\partial_{s \mid s=0} g_{s v}, \ldots, \partial_{s^{l-1} \mid s=0}^{l-1} g_{s v}\right) .$$
\end{itemize}

Proof. Let us show these three properties in order.
\begin{itemize}
\item[(1)] Notice that for any $k, \partial_{s^{k}}^{k} \boldsymbol{\Phi}_{\mathbf{g}_{b}}\left(g_{s v}\right)=\partial_{s^{k} \mid s=0}^{k} \mathrm{E}\left(g_{s v}\right)+\delta_{\mathbf{g}_{b}}^{*} \delta_{\mathbf{g}_{b}}\left(\partial_{s^{k} \mid s=0}^{k} g_{s v}\right)$. Therefore, since $\delta_{\mathbf{g}_{b}} \boldsymbol{\Phi}\left(g_{s v}\right)=0$ because $\boldsymbol{\Phi}\left(g_{s v}\right) \in \mathbf{O}\left(\mathbf{g}_{b}\right)$, then one has:
$$\delta_{\mathbf{g}_{b}}\left(\partial_{s^{k} \mid s=0}^{k} \mathrm{E}\left(g_{s v}\right)+\delta_{\mathbf{g}_{b}}^{*} \delta_{\mathbf{g}_{b}}\left(\partial_{s^{k} \mid s=0}^{k} g_{s v}\right)\right)=0 .$$
If we moreover assume $\partial_{s^{j}}^{j} \mathrm{E}\left(g_{s v}\right)=0$ for all $j \leqslant k-1$, we find $\delta_{\mathbf{g}_{b}} \delta_{\mathbf{g}_{b}}^{*} \delta_{\mathbf{g}_{b}}\left(\partial_{s^{k} \mid s=0}^{k} g_{s v}\right)=$ 0 since $0=\partial_{s^{k} \mid s=0}^{k}\left(\delta_{g_{s v}} \mathrm{E}\left(g_{s v}\right)\right)=\delta_{\mathbf{g}_{b}} \partial_{s^{k} \mid s=0}^{k} \mathrm{E}\left(g_{s v}\right)$. Since $\delta_{\mathbf{g}_{b}} \delta_{\mathbf{g}_{b}}^{*}$ is invertible on vector fields (or 1-forms) decaying at infinity by [Biq13, Ozu19b], we find $\delta_{\mathbf{g}_{b}}\left(\partial_{s^{k} \mid s=0}^{k} g_{s v}\right)=0$, but that means that $\partial_{s^{k} \mid s=0}^{k} \mathrm{E}\left(g_{s v}\right)=\partial_{s^{k} \mid s=0}^{k} \boldsymbol{\Phi}_{\mathbf{g}_{b}}\left(g_{s v}\right)-\delta_{\mathbf{g}_{b}}^{*} \delta_{\mathbf{g}_{b}}\left(\partial_{s^{k} \mid s=0}^{k} g_{s v}\right)=$ 0 . We can iterate this up to $k=l-1$ since by assumption $\partial_{s^{k} \mid s=0}^{k} \boldsymbol{\Phi}_{\mathbf{g}_{b}}\left(g_{s v}\right)=0$ for all $k \leqslant l-1$. This lets us also find $\delta_{\mathbf{g}_{b}}\left(\partial_{s^{l} \mid s=0}^{l} g_{s v}\right)=0$.
\item[(2)] For the equality $\delta_{\mathbf{g}_{b}}\left(\partial_{s^{l} \mid s=0}^{l} \boldsymbol{\Phi}_{\mathbf{g}_{b}}\left(g_{s v}\right)-\boldsymbol{\Phi}_{\mathbf{g}_{b}}^{(1)}\left(\partial_{s^{l} \mid s=0}^{l} g_{s v}\right)\right)=0$, we first see that
$$\partial_{s^{l} \mid s=0}^{l} \boldsymbol{\Phi}_{\mathbf{g}_{b}}\left(g_{s v}\right)-\boldsymbol{\Phi}_{\mathbf{g}_{b}}^{(1)}\left(\partial_{s^{l} \mid s=0}^{l} g_{s v}\right)=\partial_{s^{l} \mid s=0}^{l} \mathrm{E}\left(g_{s v}\right)-\mathrm{E}_{\mathbf{g}_{b}}^{(1)}\left(\partial_{s^{l} \mid s=0}^{l} g_{s v}\right)$$
because $\boldsymbol{\Phi}=\mathrm{E}+\delta_{\mathbf{g}_{b}}^{*} \delta_{\mathbf{g}_{b}}$. We conclude by noticing as above that
$$\delta_{\mathbf{g}_{b}} \partial_{s^{l} \mid s=0}^{l} \mathrm{E}\left(g_{s v}\right)=\partial_{s^{l} \mid s=0}^{l}\left(\delta_{g_{s v}} \mathrm{E}\left(g_{s v}\right)\right)=0$$
because $\partial_{s^{k} \mid s=0}^{k} \mathrm{E}\left(g_{s v}\right)=0$ for all $k \leqslant l-1$ and $\delta_{\mathbf{g}_{b}} \mathrm{E}_{\mathbf{g}_{b}}^{(1)}\left(\partial_{s^{l} \mid s=0}^{l} g_{s v}\right)=0$ by Proposition 1.2.
\item[(3)] The first remark is that
$$\begin{aligned}
\partial_{s^{l} \mid s=0}^{l} \boldsymbol{\Phi}_{\mathbf{g}_{b}}\left(g_{s v}\right)= & \left(\partial_{s^{l} \mid s=0}^{l} \boldsymbol{\Phi}_{\mathbf{g}_{b}}\left(g_{s v}\right)-\boldsymbol{\Phi}_{\mathbf{g}_{b}}^{(1)}\left(\partial_{s^{l} \mid s=0}^{l} g_{s v}\right)\right) \\
& +\mathrm{E}_{\mathbf{g}_{b}}^{(1)}\left(\partial_{s^{l} \mid s=0}^{l} g_{s v}\right) \\
& +\delta_{\mathbf{g}_{b}}^{*} \delta_{\mathbf{g}_{b}} \partial_{s^{l} \mid s=0}^{l} g_{s v}
\end{aligned}$$
and we will treat separately each of these terms.
We then show, using (34), that the integral of the trace of $\mathrm{E}_{\mathbf{g}_{b}}^{(1)}\left(\partial_{s^{l} \mid s=0}^{l} g_{s v}\right)$ is a boundary term:
$$\begin{aligned}
\frac{2}{2-d} \int_{\Omega} & \left\langle\mathbf{g}_{b}, \mathrm{E}_{\mathbf{g}_{b}}^{(1)}\left(\partial_{s^{l} \mid s=0}^{l} g_{s v}\right)\right\rangle_{\mathbf{g}_{b}} d v_{\mathbf{g}_{b}} \\
& =-\int_{\partial \Omega}\left(\delta_{\mathbf{g}_{b}} \partial_{s^{l} \mid s=0}^{l} g_{s v}+d \operatorname{tr}_{\mathbf{g}_{b}} \partial_{s^{l} \mid s=0}^{l} g_{s v}\right)\left(n_{\partial \Omega}\right) d v_{\mathbf{g}_{b \mid \partial_{\Omega}}} .
\end{aligned}$$
\end{itemize}

Let us now turn to the remaining linear term $\delta_{\mathbf{g}_{b}}^{*} \delta_{\mathbf{g}_{b}} \partial_{s^{l} \mid s=0}^{l} g_{s v}$ in the expression of $\boldsymbol{\Phi}_{\mathbf{g}_{b}}^{(1)}\left(\partial_{s^{l} \mid s=0}^{l} g_{s v}\right)$. By integration by parts, denoting $V=\delta_{\mathbf{g}_{b}} \partial_{s^{l} \mid s=0}^{l} g_{s v}$, we get:
$$\int_{\Omega}\left\langle\mathbf{g}_{b}, \delta_{\mathbf{g}_{b}}^{*} V\right\rangle_{\mathbf{g}_{b}} d v_{\mathbf{g}_{b}}=-2 \int_{\Omega} \delta_{\mathbf{g}_{b}} V d v_{\mathbf{g}_{b}}=2 \int_{\partial \Omega}\langle V, n\rangle_{\mathbf{g}_{b}} d v_{\mathbf{g}_{b} \mid \partial \Omega},$$
which is again a boundary term.
Noticing that
$$\partial_{s^{l} \mid s=0}^{l} \boldsymbol{\Phi}_{\mathbf{g}_{b}}\left(g_{s v}\right)-\boldsymbol{\Phi}_{\mathbf{g}_{b}}^{(1)}\left(\partial_{s^{l} \mid s=0}^{l} g_{s v}\right)=\partial_{s^{l} \mid s=0}^{l} \mathrm{E}\left(g_{s v}\right)-\mathrm{E}_{\mathbf{g}_{b}}^{(1)}\left(\partial_{s^{l} \mid s=0}^{l} g_{s v}\right),$$
we can therefore focus on showing that the integral of $\partial_{s^{l} \mid s=0}^{l} \mathrm{E}_{\mathbf{g}_{b}}\left(g_{s v}\right)$ against $\mathbf{g}_{b}$ is equal to a boundary term. Since the $l-1$ first derivatives vanish, we have:
$$\begin{aligned}
\frac{2}{2-d} \int_{\Omega}\left\langle\mathbf{g}_{b}, \partial_{s^{l} \mid s=0}^{l} \mathrm{E}\left(g_{s v}\right)\right\rangle_{\mathbf{g}_{b}} d v_{\mathbf{g}_{b}}= & \frac{d^{l}}{d s^{l}}{ }_{\mid s=0} \int_{\Omega} \mathrm{R}\left(g_{s v}\right) d v_{g_{s v}} \\
= & -\frac{d^{l-1}}{d s^{l-1}}{ }_{\mid s=0} \int_{\Omega}\left\langle\mathrm{E}\left(g_{s v}\right), \partial_{s} g_{s v}\right\rangle_{g_{s v}} d v_{g_{s v}} \\
& -\frac{d^{l-1}}{d s^{l-1}}{ }_{\mid s=0} \int_{\partial \Omega}\left(\delta_{g_{s v}}\left(\partial_{s} g_{s v}\right)+d \operatorname{tr}_{g_{s v}}\left(\partial_{s} g_{s v}\right)\right)\left(n_{\partial \Omega}\right) d v_{g_{s v \mid \partial_{\Omega}}}
\end{aligned}$$
where the first term vanishes because $\partial_{s^{k} \mid s=0}^{k} \mathrm{E}\left(g_{s v}\right)=0$ for all $k \leqslant l-1$ by the first point. Together with (66), this proves the result. \(\square\)

The point of Lemma 4.12 is that if the different $\partial_{s^{k} \mid s=0}^{k} g_{s v}$ decay faster than $r^{-2+\epsilon}$ at infinity for some small $\epsilon>0$ in dimension 4, then, the boundary term
$$\lim _{r \rightarrow \infty} \int_{r \mathfrak{S}^{3} / \Gamma} Q^{(l)}\left(\partial_{s \mid s=0} g_{s v}, \ldots, \partial_{s^{l-1} \mid s=0}^{l-1} g_{s v}\right)$$
which will appear in the following proof will always vanish.
Proof of Proposition 0.12. Using the results of Appendix B. 2 (very close to the proof of [Koi83]), we know that for any $v \in \mathbf{O}\left(\mathbf{g}_{b}\right)$ small enough, the map $s \in(-1,1) \mapsto g_{s v}$ is real-analytic in the so-called $C_{\beta}^{2, \alpha}\left(\mathbf{g}_{b}\right)$-topology defined in Appendix B. 1 for $0<\beta<2$ close to 2 , say $\beta=1.9$. We mainly use the following consequence. We have a $C_{\beta}^{2, \alpha}\left(\mathbf{g}_{b}\right)$ -converging development $g_{s v}=\mathbf{g}_{b}+s v+\sum_{k \geqslant 2} s^{k} w_{k}$ around $s=0$ where for any $k$, there exists $C=C(k)>0$ with for $l \in\{0,1,2\}$ :
$$r^{1.9+l}\left|\nabla_{\mathbf{g}_{b}}^{l} w_{k}\right|_{\mathbf{g}_{b}} \leqslant C .$$
This induces a $C_{\beta+2}^{\alpha}$-converging development (see again Appendix B):
$$\begin{aligned}
\mathbf{\Phi}_{\mathbf{g}_{b}}\left(g_{s v}\right)= & s^{2}\left(\mathbf{\Phi}_{\mathbf{g}_{b}}^{(1)}\left(w_{2}\right)+\mathbf{\Phi}_{\mathbf{g}_{b}}^{(2)}(v, v)\right) & & \in \mathbf{O}\left(\mathbf{g}_{b}\right) \\
& +s^{3}\left(\mathbf{\Phi}_{\mathbf{g}_{b}}^{(1)}\left(w_{3}\right)+\left(2 \mathbf{\Phi}_{\mathbf{g}_{b}}^{(2)}\left(w_{2}, v\right)+\mathbf{\Phi}_{\mathbf{g}_{b}}^{(2)}(v, v, v)\right)\right. & & \in \mathbf{O}\left(\mathbf{g}_{b}\right) \\
& +\ldots & & \in \mathbf{O}\left(\mathbf{g}_{b}\right) \\
& +\frac{s^{l}}{l!} \partial_{s^{l} \mid s=0}^{l} \mathbf{\Phi}_{\mathbf{g}_{b}}\left(g_{s v}\right) & & \in \mathbf{O}\left(\mathbf{g}_{b}\right) \\
& +\ldots & & \in \mathbf{O}\left(\mathbf{g}_{b}\right)
\end{aligned}$$

Now, by the analysis of the Fredholm properties of $\mathbf{\Phi}_{\mathbf{g}_{b}}$ in [Ozu19b], we know that the $\boldsymbol{\Phi}_{\mathbf{g}_{b}}^{(1)}\left(w_{l}\right)=\frac{1}{l!} \boldsymbol{\Phi}_{\mathbf{g}_{b}}^{(1)}\left(\partial_{s^{l} \mid s=0}^{l} g_{s v}\right)$ are $L^{2}\left(\mathbf{g}_{b}\right)$-orthogonal to $\mathbf{O}\left(\mathbf{g}_{b}\right)$, hence we need to study the $L^{2}\left(\mathbf{g}_{b}\right)$-projection of $\partial_{s^{l} \mid s=0}^{l} \boldsymbol{\Phi}_{\mathbf{g}_{b}}\left(g_{s v}\right)-\boldsymbol{\Phi}_{\mathbf{g}_{b}}^{(1)}\left(\partial_{s^{l} \mid s=0}^{l} g_{s v}\right)$ on $\mathbf{O}\left(\mathbf{g}_{b}\right)$.

If $\boldsymbol{\Phi}_{\mathbf{g}_{b}}\left(g_{s v}\right)$ is identically vanishing, then we are done. If not, assume that $\partial_{s^{k} \mid s=0}^{k} \boldsymbol{\Phi}_{\mathbf{g}_{b}}\left(g_{s v}\right)=$ 0 for all $k \leqslant l-1$, but $\partial_{s^{l} \mid s=0}^{l} \boldsymbol{\Phi}_{\mathbf{g}_{b}}\left(g_{s v}\right)=: \mathbf{o}_{v} \neq 0$. We want to show that $\mathbf{o}_{v} \perp\left(\mathcal{L}_{X} \mathbf{g}_{b}\right)^{\circ}$ and $\mathbf{o}_{v} \perp \mathcal{L}_{Y^{\prime}} \mathbf{g}_{b}$ for $Y^{\prime}$ harmonic vector field asymptotic to a Killing vector field.

Let us now apply our integration by parts formula (20) to the divergence-free 2-tensor $S^{(l)}(v):=\partial_{s^{l} \mid s=0}^{l} \boldsymbol{\Phi}_{\mathbf{g}_{b}}\left(g_{s v}\right)-\boldsymbol{\Phi}_{\mathbf{g}_{b}}^{(1)}\left(\partial_{s^{l} \mid s=0}^{l} g_{s v}\right)$, this gives
$$\begin{aligned}
0= & \lim _{r \rightarrow \infty} \int_{r \mathbb{S}^{3} / \Gamma} S^{(l)}(v)\left(X, \partial_{r}\right) d v_{r \mathbb{S}^{3} / \Gamma} \\
= & \frac{1}{2} \int_{N}\left\langle S^{(l)}(v),\left(\mathcal{L}_{X} \mathbf{g}_{b}\right)^{\circ}\right\rangle_{\mathbf{g}_{b}} d v_{\mathbf{g}_{b}} \\
& +\int_{N} \operatorname{tr}_{\mathbf{g}_{b}} S^{(l)}(v) d v_{\mathbf{g}_{b}}
\end{aligned}$$
where the first boundary term vanishes because it is a finite linear combination of terms of the form $\mathrm{E}_{\mathbf{g}_{b}}^{(k)}\left(\partial_{s^{j_{1}}}^{j_{1}} g_{s v}, \ldots, \partial_{s^{j_{k}}}^{j_{k}} g_{s v}\right)$ with $k \geqslant 2$ and $j_{i} \geqslant 1$. Indeed, we know from the results of Section B. 2 in the appendix (or (68)) that $\partial_{s^{j}}^{j} g_{s v} \in C_{1.9}^{2, \alpha}$ for every $j \geqslant$ 1, which implies that for any $a \in\{0,1,2\}, r^{a+1.9}\left|\nabla^{a} \partial_{s^{j}}^{j} g_{s v}\right| \leqslant C_{j}$ for some $C_{j}>0$. This gives: $\mathrm{E}_{\mathbf{g}_{b}}^{(k)}\left(\partial_{s^{j_{1}}}^{j_{1}} g_{s v}, \ldots, \partial_{s^{j_{k}}}^{j_{k}} g_{s v}\right)=\mathcal{O}\left(r^{-2-k \cdot 1.9}\right)=o\left(r^{-4}\right)$. Similarly, the last term $\int_{N} \operatorname{tr}_{\mathbf{g}_{b}} S^{(l)}(v) d v_{\mathbf{g}_{b}}$ is a boundary term of the same type by Lemma 4.12 and it vanishes for the same reason.

The proof for the different $\mathcal{L}_{Y^{\prime}} \mathbf{g}_{b}$ is similar and easier because there is no trace term to deal with. \(\square\)

Remark 4.13. Again, the proof is very close to that of Theorem 2.8 because in volume gauge, one has $\nabla_{\mathbf{g}_{b}} u \sim r \partial_{r}$ at an order higher than expected.
4.3.2. Obstruction to the desingularization of spherical and hyperbolic orbifolds. Let us now prove our main result.

Proof of Theorem 0.9. Let us assume that there exists a sequence of Einstein metrics $\left(M, \mathbf{g}_{n}\right)_{n}$ converging to an Einstein orbifold $\left(M_{o}, \mathbf{g}_{o}\right)$ with $\mathrm{E}\left(\mathbf{g}_{o}\right)+\lambda \mathbf{g}_{o}=0$. Then, according to [Ozu19a, Ozu19b, Ozu20], up to taking a subsequence, there exist $\left(t_{n}\right)_{n}, t_{n}>0$, $\left(v_{n}\right)_{n}, v_{n} \in \mathbf{O}\left(\mathbf{g}_{b}\right)$ such that $\left(M, \mathbf{g}_{n} / t_{n}\right)_{n}$ is close to $\left(N, \mathbf{g}_{b}\right)$ in the following sense: for all $r \ll t_{n}^{-\frac{1}{2}}$, we have for some $0<\beta<1$
$$(1+r)^{k+\beta}\left|\nabla_{\mathbf{g}_{b}}^{k}\left(\frac{\mathbf{g}_{n}}{t_{n}}-\left(g_{v_{n}}+t_{n} h_{2}\right)\right)\right|_{\mathbf{g}_{b}}=o\left(t_{n}\right)$$
where $h_{2}$ is a solution to the following equation:
$$\boldsymbol{\Phi}_{\mathbf{g}_{b}}^{(1)}\left(h_{2}\right)+\lambda \mathbf{g}_{b} \in \mathbf{O}\left(\mathbf{g}_{b}\right) .$$

It was shown in [Ozu19b] that the first obstruction against $\left(\mathcal{L}_{X} \mathbf{g}_{b}\right)^{\circ}$ to the desingularization is:
$$\int_{N}\left\langle\boldsymbol{\Phi}_{\mathbf{g}_{b}}\left(\mathbf{g}_{n} / t_{n}\right)+t_{n} \lambda\left(\mathbf{g}_{n} / t_{n}\right), \chi_{t_{n}}\left(\mathcal{L}_{X} \mathbf{g}_{b}\right)^{\circ}\right\rangle_{\mathbf{g}_{b}} d v_{\mathbf{g}_{b}}=0$$
Or goal is to show that it cannot be satisfied when desingularizing a spherical or hyperbolic orbifold.

Recall from Proposition 0.12 that one has $\boldsymbol{\Phi}\left(g_{v_{n}}\right)=\mathbf{o}_{v_{n}}+\mathcal{O}\left(\left\|v_{n}\right\|_{L^{2}\left(\mathbf{g}_{b}\right)}\left\|\mathbf{o}_{v_{n}}\right\|_{L^{2}\left(\mathbf{g}_{b}\right)}\right) \in$ $\mathbf{O}\left(\mathbf{g}_{b}\right)$. If $\mathbf{o}_{v_{n}}=0$, then we are done by [Ozu20t], let us assume that it is not satisfied. The obstruction against the deformation $\mathbf{w}_{v_{n}}:=\frac{\mathbf{o}_{v_{n}}}{\left\|\mathbf{o}_{v_{n}}\right\|_{L^{2}\left(\mathbf{g}_{b}\right)}}$ is
$$\int_{N}\left\langle\boldsymbol{\Phi}_{\mathbf{g}_{b}}\left(\mathbf{g}_{n} / t_{n}\right)+t_{n} \lambda\left(\mathbf{g}_{n} / t_{n}\right), \chi_{t_{n}} \mathbf{w}_{v_{n}}\right\rangle_{\mathbf{g}_{b}} d v_{\mathbf{g}_{b}}=0$$

Let us now estimate (71). We use the control (69) which tells us that:
$$\boldsymbol{\Phi}_{\mathbf{g}_{b}}\left(\mathbf{g}_{n} / t_{n}\right)+t_{n} \lambda\left(\mathbf{g}_{n} / t_{n}\right)=\boldsymbol{\Phi}_{\mathbf{g}_{b}}\left(g_{v_{n}}\right)+t_{n} \boldsymbol{\Phi}_{\mathbf{g}_{b}}^{(1)}\left(h_{2}\right)+t_{n} \lambda \mathbf{g}_{b}+o\left(t_{n}(1+r)^{-2-\beta}\right) .$$
We will therefore decompose (71) and estimate each part of the integral.
\begin{itemize}
\item[(1)] For the first integral $\int_{N}\left\langle\mathbf{\Phi}\left(g_{v_{n}}\right), \chi_{t_{n}}\left(\mathcal{L}_{X} \mathbf{g}_{b}\right)^{\circ}\right\rangle_{\mathbf{g}_{b}} d v_{\mathbf{g}_{b}}$ we use the estimate
$$\int_{N}\left\langle\mathbf{\Phi}\left(g_{v_{n}}\right),\left(\mathcal{L}_{X} \mathbf{g}_{b}\right)^{\circ}\right\rangle_{\mathbf{g}_{b}} d v_{\mathbf{g}_{b}}=\mathcal{O}\left(\left\|v_{n}\right\|_{L^{2}}\left\|\mathbf{o}_{v_{n}}\right\|_{L^{2}}\right)$$
together with $\boldsymbol{\Phi}\left(g_{v_{n}}\right)=\mathcal{O}\left(\left\|\mathbf{o}_{v_{n}}\right\|_{L^{2}} r^{-4}\right)$, which gives
$$\begin{aligned}
\int_{N}\left\langle\boldsymbol{\Phi}\left(g_{v_{n}}\right),\left(1-\chi_{t_{n}}\right)\left(\mathcal{L}_{X} \mathbf{g}_{b}\right)^{\circ}\right\rangle_{\mathbf{g}_{b}} d v_{\mathbf{g}_{b}} & =\mathcal{O}\left(\int_{t_{n}^{-} \frac{1}{4}}^{\infty}\left\|\mathbf{o}_{v_{n}}\right\|_{L^{2}} r^{-6} r^{-4} r^{3} d r\right) \\
& =\mathcal{O}\left(t_{n}\left\|\mathbf{o}_{v_{n}}\right\|_{L^{2}}\right)
\end{aligned}$$
We finally find
$$\int_{N}\left\langle\boldsymbol{\Phi}\left(g_{v_{n}}\right), \chi_{t_{n}}\left(\mathcal{L}_{X} \mathbf{g}_{b}\right)^{\circ}\right\rangle_{\mathbf{g}_{b}} d v_{\mathbf{g}_{b}}=\mathcal{O}\left(\left(\left\|v_{n}\right\|_{L^{2}}+t_{n}\right)\left\|\mathbf{o}_{v_{n}}\right\|_{L^{2}}\right),$$
\item[(2)] let us denote $\lambda_{1}:=\int_{N}\left\langle\mathbf{\Phi}_{\mathbf{g}_{b}}^{(1)}\left(h_{2}\right)+\lambda \mathbf{g}_{b},\left(\mathcal{L}_{X} \mathbf{g}_{b}\right)^{\circ}\right\rangle_{\mathbf{g}_{b}} d v_{\mathbf{g}_{b}}$. We find:
$$t_{n} \int_{N}\left\langle\mathbf{\Phi}_{\mathbf{g}_{b}}^{(1)}\left(h_{2}\right)+\lambda \mathbf{g}_{b}, \chi_{t_{n}}\left(\mathcal{L}_{X} \mathbf{g}_{b}\right)^{\circ}\right\rangle_{\mathbf{g}_{b}} d v_{\mathbf{g}_{b}}=t_{n} \lambda_{1}+o\left(t_{n}\right),$$
\item[(3)] for the error term, we have $o\left(t_{n}\right) \int_{N}\left\langle(1+r)^{-2-\beta}, \chi_{t_{n}}\left(\mathcal{L}_{X} \mathbf{g}_{b}\right)^{\circ}\right\rangle_{\mathbf{g}_{b}} d v_{\mathbf{g}_{b}}=o\left(t_{n}\right)$.
\end{itemize}

From (71), we finally find the estimate:
$$0=t_{n} \lambda_{1}+\mathcal{O}\left(\left\|v_{n}\right\|_{L^{2}}\left\|\mathbf{o}_{v_{n}}\right\|_{L^{2}}\right)+o\left(t_{n}\right) .$$
Similarly, using again (73), we then estimate (72) in three parts:
\begin{itemize}
\item[(1)] For the first integral $\int_{N}\left\langle\boldsymbol{\Phi}\left(g_{v_{n}}\right), \chi_{t_{n}} \mathbf{w}_{v_{n}}\right\rangle_{\mathbf{g}_{b}} d v_{\mathbf{g}_{b}}$, we use Proposition 0.12 which implies that
$$\int_{N}\left\langle\boldsymbol{\Phi}\left(g_{v_{n}}\right), \mathbf{w}_{v_{n}}\right\rangle_{\mathbf{g}_{b}} d v_{\mathbf{g}_{b}}=\left\|\mathbf{o}_{v_{n}}\right\|_{L^{2}\left(\mathbf{g}_{b}\right)}+\mathcal{O}\left(\left\|v_{n}\right\|_{L^{2}\left(\mathbf{g}_{b}\right)}\left\|\mathbf{o}_{v_{n}}\right\|_{L^{2}\left(\mathbf{g}_{b}\right)}\right) .$$
Since $\boldsymbol{\Phi}\left(g_{v_{n}}\right)=\mathcal{O}\left(\left\|\mathbf{o}_{v_{n}}\right\|_{L^{2}} r^{-4}\right)$, we estimate the difference
$$\begin{aligned}
\int_{N}\left\langle\boldsymbol{\Phi}\left(g_{v_{n}}\right),\left(1-\chi_{t_{n}}\right) \mathbf{w}_{v_{n}}\right\rangle_{\mathbf{g}_{b}} d v_{\mathbf{g}_{b}} & =\mathcal{O}\left(\int_{t_{n}^{-\frac{1}{4}}}^{\infty}\left\|\mathbf{o}_{v_{n}}\right\|_{L^{2}} r^{-6} r^{-4} r^{3} d r\right) \\
& =\mathcal{O}\left(t_{n}\left\|\mathbf{o}_{v_{n}}\right\|_{L^{2}}\right)
\end{aligned}$$
and finally
$$\int_{N}\left\langle\mathbf{\Phi}\left(g_{v_{n}}\right), \chi_{t_{n}} \mathbf{w}_{v_{n}}\right\rangle_{\mathbf{g}_{b}} d v_{\mathbf{g}_{b}}=\left\|\mathbf{o}_{v_{n}}\right\|_{L^{2}}+\mathcal{O}\left(\left(t_{n}+\left\|v_{n}\right\|_{L^{2}}\right)\left\|\mathbf{o}_{v_{n}}\right\|_{L^{2}}\right),$$
\item[(2)] let us denote $\mu_{v_{n}}:=\int_{N}\left\langle\boldsymbol{\Phi}_{\mathbf{g}_{b}}^{(1)}\left(h_{2}\right)+\lambda \mathbf{g}_{b}, \mathbf{w}_{v_{n}}\right\rangle_{\mathbf{g}_{b}} d v_{\mathbf{g}_{b}}$. We find:
$$t_{n} \int_{N}\left\langle\mathbf{\Phi}_{\mathbf{g}_{b}}^{(1)}\left(h_{2}\right)+\lambda \mathbf{g}_{b}, \chi_{t_{n}} \mathbf{w}_{v_{n}}\right\rangle_{\mathbf{g}_{b}} d v_{\mathbf{g}_{b}}=t_{n} \mu_{v_{n}}+o\left(t_{n}\right),$$
\end{itemize}
(3) for the error term, we have $o\left(t_{n}\right) \int_{N}\left\langle(1+r)^{-2-\beta}, \chi_{t_{n}} \mathbf{w}_{v_{n}}\right\rangle_{\mathbf{g}_{b}} d v_{\mathbf{g}_{b}}=o\left(t_{n}\right)$. From (72), we finally find the estimate
$$0=\left\|\mathbf{o}_{v_{n}}\right\|_{L^{2}\left(\mathbf{g}_{b}\right)}+t_{n} \mu_{v_{n}}+o\left(t_{n}+\left\|\mathbf{o}_{v_{n}}\right\|_{L^{2}\left(\mathbf{g}_{b}\right)}\right) .$$
which gives $\left\|\mathbf{o}_{v_{n}}\right\|_{L^{2}\left(\mathbf{g}_{b}\right)}=\mathcal{O}\left(t_{n}\right)$ because $\mu_{v_{n}}$ is bounded since $\mathbf{O}\left(\mathbf{g}_{b}\right)$ is finite-dimensional.
Finally by plugging $\left\|\mathbf{o}_{v_{n}}\right\|_{L^{2}\left(\mathbf{g}_{b}\right)}=\mathcal{O}\left(t_{n}\right)$ in (75), we find $\left|\lambda_{1}\right|=\mathcal{O}\left(\left\|v_{n}\right\|_{L^{2}}\right)$. Now, since $\lambda_{1}$ is a constant, and since $\left(t_{n}, v_{n}\right) \rightarrow 0$, we obtain $\lambda_{1}=0$. It is impossible to satisfy if $H_{2}$ is the quadratic term of the development of a spherical or hyperbolic orbifold by Corollary 4.11. \(\square\)

Remark 4.14. The above proof applies indifferently to other Einstein orbifolds and to the other deformations $\mathcal{L}_{Y^{\prime}} \mathbf{g}_{b}$. In particular, it shows that the integrability assumption in Theorem 4.6 is superfluous.

We believe that the result should hold for spherical and hyperbolic orbifolds with more general singularities than $\mathbb{R}^{4} / \mathbb{Z}_{2}$, but this requires dealing with trees of singularities. The main difficulty is that it is not known whether the projection on the obstruction is a real-analytic map or not in this degenerate situation.

Conjecture 4.15. Let $\left(M_{o}, \mathbf{g}_{o}\right)$ be a singular spherical or hyperbolic compact orbifold. Then, it is not limit of smooth Einstein metrics in the Gromov-Hausdorff sense.
4.4. Higher dimensional Einstein orbifolds with isolated singularities. The work of [Ozu19a, Ozu19b] extends almost verbatim to the degeneration of Einstein $d$-manifolds $(d \geqslant 5)$ satisfying the (non natural) assumption that the $L^{\frac{d}{2}}$-norm of its curvature is bounded. It shows that, exactly like in dimension 4, the possible Gromov-Hausdorff limits are Einstein orbifolds with isolated singularities and the singularity models are Ricci-flat ALE orbifolds. Indeed the results of [Ozu19a, Ozu19b, Ozu20t] only use the fact that the dimension is 4 to obtain a bound on the $L^{2}$-norm of the Riemannian curvature from the noncollapsedness assumption.

An obstruction to the desingularization under essentially the same assumptions as [Biq13] was proven in [MV16] for higher dimensional desingularizations. Namely, one considers the desingularization by the so-called Calabi metric denoted $\mathbf{g}_{\text {cal }}$ which is $2 d$ -dimensional, Ricci-flat ALE and asymptotic to $\mathbb{R}^{2 d} / \mathbb{Z}_{d}$.
Lemma 4.16. The kernel $\mathbf{O}\left(\mathbf{g}_{\text {cal }}\right)$ is 1-dimensional and spanned by $\left(\mathcal{L}_{X} \mathbf{g}_{\text {cal }}\right)^{\circ}$, where $X$ is a harmonic vector field asymptotic to $r \partial_{r}$.
Proof. The proof that $\mathbf{O}\left(\mathbf{g}_{\text {cal }}\right)$ is 1-dimensional is found in [MV16]. We therefore simply have to prove the existence of $X$ and the fact that $\left(\mathcal{L}_{X} \mathbf{g}_{\text {cal }}\right)^{\circ}$ is divergence-free.

Like in [Ozu20t, BH19], we consider the unique function $u=r^{2}+\mathcal{O}\left(r^{-2 d+2}\right)$ satisfying $\Delta_{\mathbf{g}_{\text {cal }}} u=2 d$. One then defines $X=\frac{1}{2} \nabla_{\mathbf{g}_{\text {cal }}} u=r \partial_{r}+\mathcal{O}\left(r^{-2 d+1}\right)$ which satisfies
$$\delta_{\mathbf{g}_{c a l}}\left(\mathcal{L}_{X} \mathbf{g}_{c a l}\right)^{\circ}=0$$
by construction.
A last step is to ensure that $\left(\mathcal{L}_{X} \mathbf{g}_{\text {cal }}\right)^{\circ} \neq 0$ following [BH19]. If $\left(\mathcal{L}_{X} \mathbf{g}_{\text {cal }}\right)^{\circ}=0$, then since $\Delta_{\mathrm{g}_{\text {cal }}} u=2 d, X$ would generate 1-parameter group of homotheties. By considering the maximum of the curvature tensor, this is impossible for the non flat metric $\mathbf{g}_{\text {cal }}$. \(\square\)

This implies that the obstruction found in [MV16] is of the same type.
Corollary 4.17. Let $\left(M_{o}, \mathbf{g}_{o}\right)$ be an Einstein orbifold with a singularity $\mathbb{R}^{2 d} / \mathbb{Z}_{d}$ at $p_{o}$. The obstruction to the desingularization of $\left(M_{o}, \mathbf{g}_{o}\right)$ at $p_{o}$ by $\mathbf{g}_{\text {cal }}$ found in [MV16], namely
$$d \cdot\left\langle\mathbf{R}_{\mathbf{g}_{o}}\left(p_{o}\right) \omega, \omega\right\rangle+2(d-2) \mathrm{R}_{\mathbf{g}_{o}}\left(p_{o}\right)=0$$
is equivalent to the obstruction against $\left(\mathcal{L}_{X} \mathbf{g}_{b}\right)^{\circ}$.

\section*{Appendix A. Development of Einstein 4-metrics}

Let $\left(M_{o}, \mathbf{g}_{o}\right)$ be an Einstein orbifold (smooth or singular) and assume that at a point $p$, it has a development: $\mathbf{g}_{o}=\mathbf{e}+H_{2}+\mathcal{O}\left(r^{3}\right)$. We start by showing that up to a gauge term, the term $H_{2}$ has a good correspondence with the curvature.

\section*{A.1. A local gauge for Einstein metrics.}

Proposition A.1. Let $H_{2}$ be a quadratic symmetric 2-tensor satisfying $\operatorname{Ric}_{\mathbf{e}}^{(1)}\left(H_{2}\right)=\Lambda \mathbf{e}$, for $\Lambda \in \mathbb{R}$ and such that:
$$\mathbf{R}_{\mathbf{e}}^{ \pm,(1)}\left(H_{2}\right)=\frac{\Lambda}{3} \sum_{i} \omega_{i}^{ \pm} \otimes \omega_{i}^{ \pm}+\sum_{i j} W_{i j}^{ \pm} \omega_{i}^{ \pm} \otimes \omega_{j}^{ \pm}$$
where we identified $\Omega_{\mathbf{e}}^{+} \otimes \Omega_{\mathbf{e}}^{+} \sim\left(\Omega_{\mathbf{e}}^{+}\right)^{*} \otimes \Omega_{\mathbf{e}}^{+} \sim \operatorname{End}\left(\Omega_{\mathbf{e}}^{+}\right)$and where the $W_{i j}^{ \pm}$are the coefficients of the (anti-)selfdual Weyl curvature.

Then, there exists a cubic vector field $V_{3}$ such that
$$H_{2}=-\frac{\Lambda}{9} r^{4} g_{\mathbb{S}^{3}}+\frac{r^{2}}{6}\left(\sum_{i j} W_{i j}^{+} \theta_{i}^{-} \circ \omega_{j}^{+}+\sum_{k l} W_{k l}^{-} \theta_{k}^{+} \circ \omega_{l}^{-}\right)+\mathcal{L}_{V_{3}} \mathbf{e} .$$
where $g_{\mathbb{S}^{3}}$ is the usual round metric on the unit 3-sphere.
Proof. Let us first show that the infinitesimal curvature induced by
$$\tilde{H}_{2}:=-\frac{\Lambda}{9} r^{4} g_{\mathbb{S}^{3}}+\frac{r^{2}}{6}\left(\sum_{i j} W_{i j}^{+} \theta_{i}^{-} \circ \omega_{j}^{+}+\sum_{k l} W_{k l}^{-} \theta_{k}^{+} \circ \omega_{l}^{-}\right)$$
is the same as that of $H_{2}$. For the spherical metric in geodesic coordinates, $g_{\mathbb{S}^{4}}$ with $\Lambda=3$, one has the development:
$$g_{\mathbb{S}^{4}}=\mathbf{e}-\frac{1}{3} r^{4} g_{\mathbb{S}^{3}}+\mathcal{O}\left(r^{3}\right),$$
and therefore, by linearity of $H_{2} \mapsto \mathbf{R}_{\mathbf{e}}^{ \pm,(1)}\left(H_{2}\right)$, we just have to deal with Ricci-flat deformations and their Weyl curvature. We rely on the formalism of [Biq16] for this computation.

We first note that each term $r^{2} \theta_{i}^{\mp} \circ \omega_{j}^{ \pm}$is traceless and harmonic, hence is in the kernel of $\operatorname{Ric}_{\mathbf{e}}^{(1)}$. We have the following formula $d\left(r^{2} \theta_{i}^{-}\right)=6 r d r \wedge \theta_{i}^{-}$, hence
$$* d\left(r^{2} \theta_{i}^{-}\right)=-6 r^{2} \alpha_{i}^{+} .$$
From this, we see that the term is in the Bianchi gauge (46) since $W_{i j}^{+}=W_{j i}^{+}$, and $-\frac{r^{2}}{6} \sum_{i} W_{i i}^{+}\left(-6 \omega_{i}^{+}\left(\alpha_{i}^{+}\right)\right)=-r \sum_{i} W_{i i}^{+} d r=0$ because $r \omega_{i}^{+}\left(\alpha_{i}^{+}\right)=-d r$ and $\sum_{i} W_{i i}^{+}=0$.

From (80), we moreover obtain:
$$-d * d\left(r^{2} \theta_{i}^{-}\right)=6 \omega_{i}^{+},$$
and therefore we have the following curvature induced by $H_{2}^{+}:=\frac{r^{2}}{6} \sum_{i j} W_{i j}^{+} \theta_{i}^{-} \circ \omega_{j}^{+}$:
\begin{itemize}
\item[-] $\operatorname{Ric}_{\mathbf{e}}^{(1)}\left(H_{2}^{+}\right)=0$,
\item[-] $\mathbf{R}_{\mathrm{e}}^{+,(1)}\left(H_{2}^{+}\right)=\left[\begin{array}{lll}W_{11}^{+} & W_{12}^{+} & W_{13}^{+} \\ W_{21}^{+} & W_{22}^{+} & W_{23}^{+} \\ W_{31}^{+} & W_{32}^{+} & W_{33}^{+}\end{array}\right]$.
\end{itemize}

Let us now prove that the induced anti-selfdual curvature $\mathbf{R}_{\mathbf{e}}^{-,(1)}\left(H_{2}^{+}\right)$vanishes. On the other hand that seeing, e as a hyperkähler metric with the opposite orientation, we have the expression $r^{2} \theta_{i}^{-}=\sum_{l}\left\langle\omega_{i}^{+}\left(r \partial_{r}\right), \omega_{l}^{-}\left(r \partial_{r}\right)\right\rangle \omega_{l}^{-}$, hence
$$r^{2} \theta_{i}^{-} \circ \omega_{j}^{+}=\sum_{l}\left\langle\omega_{i}^{+}\left(r \partial_{r}\right), \omega_{l}^{-}\left(r \partial_{r}\right)\right\rangle \omega_{l}^{-} \circ \omega_{j}^{+},$$
and we also find
$$d\left(\sum_{l}\left\langle\omega_{i}^{+}\left(r \partial_{r}\right), \omega_{l}^{-}\left(r \partial_{r}\right)\right\rangle \omega_{l}^{-}\right)=-\sum_{l}\left(\omega_{l}^{-} \circ \omega_{i}^{+}\left(r d_{r}\right)\right) \wedge \omega_{j}^{+} .$$
Now, recall that for any 1-form $\beta, *\left(\beta \wedge \omega_{j}^{+}\right)=\omega_{j}^{+}(\beta)$, where we identify $\omega_{j}^{+}$and the associated endomorphism by the metric. By (82), this gives
$$* d\left(\sum_{l}\left\langle\omega_{i}^{+}\left(r \partial_{r}\right), \omega_{l}^{-}\left(r \partial_{r}\right)\right\rangle \omega_{j}^{+}\right)=-\sum_{l} \omega_{j}^{+} \circ \omega_{i}^{+} \circ \omega_{l}^{-}\left(r d_{r}\right) .$$
From the expression of $\mathbf{R}_{\mathbf{e}}^{-,(1)}\left(H_{2}^{+}\right)\left(\omega_{l}^{-}\right)$and using that $W_{i j}^{+}=W_{j i}^{+}, \omega_{j}^{+} \circ \omega_{i}^{+}=-\omega_{i}^{+} \circ \omega_{j}^{+}$ as well as $\sum_{i} W_{i i}^{+}=0$, we find: $\mathbf{R}_{\mathbf{e}}^{-,(1)}\left(H_{2}^{+}\right)=0$. The proof is exactly the same for the rest of the tensor coming from $W^{-}$.

Let us now show that a quadratic 2-tensor satisfying $\mathbf{R}_{\mathbf{e}}^{(1)}\left(H_{2}^{\prime}\right)=0$ is necessarily of gauge type, that is: $H_{2}^{\prime}=\mathcal{L}_{V_{3}} \mathbf{e}$ for some cubic vector field $V_{3}$. According to Biq13, (28)], there exists $V_{3}$ such that $H_{2}^{\prime \prime}:=H_{2}^{\prime}-\mathcal{L}_{V_{3}} \mathbf{e}$ is radial, that is $H_{2}^{\prime \prime}\left(\partial_{r},.\right)=0$, and in particular, there exist $H_{i j}$ with
$$H_{2}^{\prime \prime}=r^{4} \sum_{i j} H_{i j} \alpha_{i}^{+} \alpha_{j}^{+}$$
and still $\mathbf{R}_{\mathbf{e}}^{(1)}\left(H_{2}^{\prime \prime}\right)=0$. We now need to prove that $H_{2}^{\prime \prime}=0$.
Now according to [Biq13, (38)], from (83), one has:
$$0=\mathbf{R}_{\mathbf{e}}^{+,(1)}\left(H_{2}^{\prime \prime}\right)=-6 \sum_{i j} H_{i j} \omega_{i}^{+} \otimes \omega_{j}^{+}+\left(H_{11}+H_{22}+H_{33}\right) \operatorname{Id}_{\Omega_{\mathbf{e}}^{+}} .$$
We therefore directly find $H_{i j}=0$ when $i \neq j$, and taking the trace of (84), we get $0=-6\left(H_{11}+H_{22}+H_{33}\right)+3\left(H_{11}+H_{22}+H_{33}\right)$ and consequently $H_{11}+H_{22}+H_{33}=0$. Finally, we see that $H_{2}^{\prime \prime}=0$ and this ends the proof. \(\square\)
A.2. Vanishing of the obstructions to Einstein deformations. Let us first deal with the case of Einstein deformations.

Proposition A.2. For any quadratic 2-tensor $H_{2}$ on $\left(\mathbb{R}^{4}, \mathbf{e}\right)$ with: $\operatorname{Ric}_{\mathbf{e}}\left(H_{2}\right)=\Lambda \mathbf{e}$ for $\Lambda \in \mathbb{R}$, the obstructions (26) and (32) vanish.

Remark A.3. The result is true from Propositions 1.8 and 2.3 and by [Gas82]. We however prefer to give another much simpler way to see that it holds.

Sketch of proof. We only sketch the proof as the result can essentially be found by bilinearity of the obstructions (32) and (27) and thanks to the curvature of the known examples of Einstein metrics.

Let us use the bilinear nature of our obstructions and decompose any quadratic 2tensor as in Proposition A.1, that is as $H_{2}=H_{\mathrm{R}}+H_{W_{+}}+H_{W_{-}}+H_{0}$ where $H_{\mathrm{R}}=\frac{\Lambda r^{4}}{9} g_{\mathbb{S}^{3}}$, $H_{W_{ \pm}}=\frac{r^{2}}{6} \sum W_{i j}^{ \pm} \theta_{i}^{\mp} \circ \omega_{j}^{ \pm}$and $H_{0}=\mathcal{L}_{V} \mathbf{e}$ for some vector field $V$ satisfying $|V|_{\mathbf{e}} \sim r^{3}$.

Note that any term combined with a gauge term $H_{0}$ will make the obstructions vanish by invariance, see Proposition 1.6 and Remark 2.6, There remain several situations which can be settled thanks to the known examples of Einstein metrics:
\begin{itemize}
\item[-] the obstructions for $\left(H_{\mathrm{R}}, H_{\mathrm{R}}\right)$ vanish because they do on the sphere,
\item[-] the obstructions of the form $\left(H_{\mathrm{R}}, H_{W_{ \pm}}\right)$vanish by bilinearity and because of the examples of (anti-)selfdual Kähler-Einstein metrics such as the Fubini-Study metric on $\mathbb{C} P^{2}$,
\item[-] the obstructions of the form $\left(H_{W_{ \pm}}, H_{W_{ \pm}}\right)$vanish by bilinearity and because of the examples of orbifold hyperkähler metrics such as the ones produced in [Ozu20], where it is clear that the (anti-)selfdual curvature can take arbitrary values,
\item[-] lastly, the obstructions of the form $\left(H_{W_{ \pm}}, H_{W_{\mp}}\right)$ vanish by bilinerarity and because of the examples of non selfdual Einstein metrics, like the Euclidean Schwarzschild metric or the product metric $\mathbb{S}^{2} \times \mathbb{S}^{2}$. \(\square\)
\end{itemize}

Remark A.4. One can also use the expression of the quadratic terms of the Ricci curvature directly from (48). The computations are not straightforward but the different terms remarkably cancel out as expected.

\section*{Appendix B. Function spaces and analyticity on ALE spaces}

In this appendix, we define function spaces from [Ozu20t] and use it to show the analytic dependence of Einstein modulo obstructions deformations of Ricci-flat ALE metrics needed in the last section of the article. The proofs in the compact situation can be found in [Koi83] and [Ozu20t, Chapter 1, Section 3.1].
B.1. Function spaces. For a tensor $s$, a point $x, \alpha>0$ and a Riemannian manifold $(M, g)$. The Hölder seminorm is defined as
$$[s]_{C^{\alpha}(g)}(x):=\sup _{\left\{y \in T_{x} M,|y|<\operatorname{inj}_{g}(x)\right\}}\left|\frac{s(x)-s\left(\exp _{x}^{g}(y)\right)}{|y|^{\alpha}}\right|_{g} .$$

For ALE manifolds, we will consider a norm which is bounded for tensors decaying at infinity. Denote $r$ a smooth positive function equal to the parameter $d_{\mathbf{e}}(0,$.$) in a$ neighborhood of infinity where ( $N, \mathbf{g}_{b}$ ) has ALE coordinates.

Definition B. 1 (Weighted Hölder norms on an ALE manifold). Let $\beta \in \mathbb{R}, k \in \mathbb{N}$, $0<\alpha<1$ and $\left(N, g_{b}\right)$ be an ALE manifold. Then, for any tensor $s$ on $N$, we define
$$\|s\|_{C_{\beta}^{k, \alpha}}:=\sup _{N}(1+r)^{\beta}\left(\sum_{i=0}^{k}(1+r)^{i}\left|\nabla_{g_{b}}^{i} s\right|_{g_{b}}+(1+r)^{k+\alpha}\left[\nabla_{g_{b}}^{k} s\right]_{C^{\alpha}\left(g_{b}\right)}\right) .$$

Lemma B. 2 ([Biq13, Lemma 2.1], [Ozu20t]). Let $\left(N, \mathbf{g}_{b}\right)$ be an ALE orbifold. Then, for any $\beta \in(0,2) \cup(2,4)$ there exists $C>0$ such that for any $h \in C_{\beta}^{2, \alpha}, h \perp \mathbf{O}\left(\mathbf{g}_{b}\right)$, we have
$$\|h\|_{C_{\beta}^{2, \alpha}} \leqslant C\left\|\boldsymbol{\Phi}_{\mathbf{g}_{b}}^{(1)} h\right\|_{C_{\beta+2}^{\alpha}} .$$
B.2. Real-analytic dependence of Einstein modulo obstructions metrics. Let us consider $\beta \in(0,2)$ to ensure that the kernel and cokernel of the linearization of $\mathbf{\Phi}_{\mathbf{g}_{b}}$ is reduced to $\mathbf{O}\left(\mathbf{g}_{b}\right)$. The map $g \in C_{\beta}^{2, \alpha} \mapsto \boldsymbol{\Phi}_{\mathbf{g}_{b}}(g) \in C_{\beta+2}^{\alpha}$ is a real-analytic map between Banach spaces because the "weights" $(1+r)^{\beta}$ or $(1+r)^{2+\beta}$ in both the starting and target spaces are larger than 1 . This condition on the weight ensures that multilinear operations are continuous in this topology, see the theory of [Pal68] for the source of this requirement and Biq13, Proof of Lemma 8.2] for a discussion of the weight larger than 1 in the case of weighted Hölder norms.

We can therefore apply the implicit function theorem to the following analytic map: $\boldsymbol{\Psi}: C_{\beta}^{2, \alpha} \times \mathbf{O}\left(\mathbf{g}_{b}\right) \times \mathbf{O}\left(\mathbf{g}_{b}\right) \mapsto C_{\beta+2}^{\alpha} \times C_{\beta}^{2, \alpha}$ defined by
$$\boldsymbol{\Psi}(g, \mathbf{o}, v) \mapsto\left(\boldsymbol{\Phi}_{\mathbf{g}_{b}}(g)+\mathbf{o}, \pi_{\mathbf{O}\left(\mathbf{g}_{b}\right)}\left(g-\mathbf{g}_{b}-v\right)\right),$$
where $\pi_{\mathbf{O}\left(\mathbf{g}_{b}\right)}$ is the $L^{2}\left(\mathbf{g}_{b}\right)$-projection on $\mathbf{O}\left(\mathbf{g}_{b}\right)$ which is linear (hence real-analytic).
The map $\boldsymbol{\Psi}$ is real-analytic between Banach spaces and it satisfies the assumptions of the implicit function theorem for real-analytic maps between Banach spaces of [Whi65] about $\mathbf{g}_{b}$. Namely, it satisfies:
\begin{itemize}
\item[(1)] $\boldsymbol{\Psi}\left(\mathbf{g}_{b}, 0,0\right)=0$, and
\item[(2)] the linearization $(g, \mathbf{o}) \mapsto \boldsymbol{\Psi}(g, \mathbf{o}, 0)$ is a homeomorphism by construction.
\end{itemize}
We conclude that for any $v \in \mathbf{O}\left(\mathbf{g}_{b}\right)$ small enough, there exists a unique $\left(\bar{g}_{v}, \overline{\mathbf{o}}_{v}\right) \in\left(\mathbf{g}_{b}+\right.$ $\left.C_{\beta}^{2, \alpha}\right) \times \mathbf{O}\left(\mathbf{g}_{b}\right)$ satisfying:
$$\boldsymbol{\Psi}\left(\bar{g}_{v}, \overline{\mathbf{o}}_{v}, v\right)=0$$
and that $v \mapsto\left(\bar{g}_{v}, \overline{\mathbf{o}}_{v}\right)$ is real-analytic.

\section*{References}
[And89] M.T. Anderson, Ricci Curvature Bounds and Einstein Metrics on Compact Manifolds J. Amer. Math. Soc. 2 (1989), no. 3, 455-490.
[And92] M. T. Anderson, The $L^{2}$ structure of moduli spaces of Einstein metrics on 4-manifolds, Geometric and Functional Analysis, March 1992, Volume 2, Issue 1, pp 29-89
[And08] M.T. Anderson, On boundary value problems for Einstein metrics. Geometry \& Topology, 12(4), pp.2009-2045.
[And10] M.T. Anderson, A survey of Einstein metrics on 4-manifolds. Handbook of geometric analysis, No. 3, 1-39, Adv. Lect. Math. (ALM), 14, Int. Press, Somerville, MA, 2010.
[AMM82] J. Arms ; J. Marsden ; V. Moncrief, The structure of the space of solutions of Einstein's equations II: several Killing fields and the Einstein-Yang-Mills equations, Annals of Physics Volume 144, Issue 1, November 1982, Pages 81-106
[Art68] Michael Artin, On the Solutions of Analytic Equations, Inventiones mathematicae 5 (1968): 277-291
[Auv18] H. Auvray, From ALE to ALF gravitational instantons. Compos. Math. 154 (2018), no. 6, 1159-1221.
[BKN89] S. Bando ; A. Kasue ; H. Nakajima, On a construction of coordinates at infinity on manifolds with fast curvature decay and maximal volume growth. Invent. Math. 97 (1989), no. 2, 313-349.
[Bes87] A.L. Besse, Einstein manifolds, Ergebnisse der Mathematik und ihrer Grenzgebiete (3) [Results in Mathematics and Related Areas (3)], 10. Springer-Verlag, Berlin, 1987.
[BL20] R. Bielawski and L. Foscolo, Deformations of hyperkähler cones, arXiv preprint, arXiv:2012.14895 [math.DG].
[Biq13] O. Biquard, Désingularisation de métriques d'Einstein. I Invent. Math. 192 (2013), no. 1, 197-252.
[Biq16] O. Biquard, Désingularisation de métriques d'Einstein. II. Invent. Math. 204(2), (2016), 473-504.
[Biq19] O. Biquard, Métriques hyperkählériennes piées.Bull. Soc. Math. France 147 (2019) 303-340.
[BH19] O. Biquard ; H. Hein, The renormalized volume of a 4-dimensional Ricci-flat ALE space. arXiv:1901.03647 [math.DG]
[CT94] J. Cheeger ; G. Tian, On the cone structure at infinity of Ricci flat manifolds with Euclidean volume growth and quadratic curvature decay. Invent. Math. 118 (1994), no. 3, 493-571.
[CEV17] O. Chodosh ; M. Eichmair ; A. Volkmann, Isoperimetric structure of asymptotically conical manifolds. J. Differ. Geom. 105 (2017), 1-19.
[Cox11] G. Cox, Scalar Curvature Rigidity Theorems for the Upper Hemisphere. PhD thesis.
[DO20] A. Deruelle ; T. Ozuch, A Łojasiewicz inequality for $A L E$ metrics. arXiv:2007.09937 [math.DG]
[DO21] A. Deruelle ; T. Ozuch, Dynamical (in)stability of Ricci-flat ALE metrics along the Ricci flow. arXiv:2104.10630 [math.DG]
[EH78] T. Eguchi ; A. Hanson, Asymptotically flat selfdual solutions to Euclidean gravity, Physics Letters B74, 249-251 (1978)
[Fin11] J. Fine, A gauge theoretic approach to the anti-selfdual Einstein equations, arXiv:1111.5005, 2011.
[FLS17] J. Fine ; J.D Lotay ; M Singer, The space of hyperkhler metrics on a 4-manifold with boundary, Forum Math Sigma 5 (2017) e6, 50 pp.
[FMM80] A. Fischer ; J. Marsden ; V. Moncrief, The structure of the space of solutions of Einstein's equations. I. One Killing field, Ann. Inst. Henri Poincare, 33 (1980), pp. 147-194
[Gas82] J. Gasqui, Sur la résolubilité locale des équations d'Einstein, Compositio Math. 47 (1982), no. 1, 43-69.
[Has11] R. Haslhofer, A renormalized Perelman-functional and a lower bound for the ADM-mass. J. Geom. Phys., 61(11):2162-2167, 2011.
[Has12] R. Haslhofer, Perelman's lambda-functional and the stability of Ricci-flat metrics, Calc. Var. PDE 45(3-4):481-504, 2012
[HM14] R. Haslhofer ; R. Müller, Dynamical stability and instability of Ricci-flat metrics, Math. Ann. 360(1-2):547-553, 2014
[Her16] M. Herzlich, Computing asymptotic invariants with the Ricci tensor on asymptotically flat and asymptotically hyperbolic manifolds, Ann. Henri Poincaré 17 (2016), no. 12, 3605-3617. MR 3568027
[KP20] K. Kroencke, O. Lindblad Petersen, $L^{p}$-stability and positive scalar curvature rigidity of Ricciflat ALE manifolds, preprint, arXiv:2009.11854 [math.DG]
[Kro89a] P.B. Kronheimer, The construction of ALE spaces as hyper-Kähler quotients. J. Differential Geom. Volume 29, Number 3 (1989), 665-683.
[Koi82] N. Koiso, Rigidity and infinitesimal deformability of Einstein metrics. Osaka J. Math. 19 (1982), no. 3, 643-668
[Koi83] N. Koiso, Einstein Metrics and Complex Structures. Invent. Math. 73 (1983), no. 1, 71-106.
[MV16] P. Morteza ; J. Viaclovsky, The Calabi metric and desingularization of Einstein orbifolds. J. Eur. Math. Soc. 22 (2020), 1201-1245.
[Nab13] A. Naber, Characterizations of Bounded Ricci Curvature on Smooth and NonSmooth Spaces. preprint, arXiv:1306.6512 [math.DG]
[Nak90] H. Nakajima, Self-Duality of ALE Ricci-Flat 4-Manifolds and Positive Mass Theorem. Adv. Stud. Pure Math. Recent Topics in Differential and Analytic Geometry, T. Ochiai, ed. (Tokyo: Mathematical Society of Japan, 1990), 385-396
[Ozu19a] T. Ozuch, Noncollapsed degeneration of Einstein 4-manifolds I. preprint, arXiv:1909.12957 [math.DG].
[Ozu19b] T. Ozuch, Noncollapsed degeneration of Einstein 4-manifolds II. preprint, arXiv:1909.12960 [math.DG].
[Ozu20t] T. Ozuch, Complétion de l'espace de modules des métriques d'Einstein en dimension 4. École Normale Supérieure (Paris), 2020. Français. 〈tel-03137993〉
[Ozu20] T. Ozuch, Higher order obstructions to the desingularization of Einstein metrics . preprint, arXiv:2012.13316 [math.DG].
[Pal68] R. Palais, Foundations of global non-linear analysis, W. A. Benjamin, Inc., New York-Amsterdam 1968
[Sch88] R. Schoen, The existence of weak solutions with prescribed singular behaviour for a conformally invariant scalar equation. Commun. Pure Appl. Math. 41, 317-392 (1988)
[SSU89] L. M. Sibner ; R. J. Sibner ; K. Uhlenbeck, Solutions to Yang-Mills equations that are not self-dual Proc. Natl. Acad. Sci. USA. 1989 Nov ; 86(22) : 8610-8613.
[Tau70] A. Taub, Variational principles in general relativity, ed. C. Cattanes (Lectures at the Centro Internazionale Matematico Estiud, Bressanone), Edizioni Cremonese, Rome, 1970, p. 206-300.
[Whi65] E. F. Whittlesey, Analytic Functions in Banach Spaces, Proc. Amer. Math. Soc. 16 (1965), 1077-1083.

MIT, Dept. of Math., 77 Massachusetts Avenue, Cambridge, MA 02139-4307.
E-mail address, ozuch@mit.edu
