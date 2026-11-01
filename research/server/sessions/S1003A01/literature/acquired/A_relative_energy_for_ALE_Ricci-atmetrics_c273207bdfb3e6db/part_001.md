---
retention_scope: session
part: 1
total_parts: 4
---

[Part 1/4 of: A relative energy for ALE Ricci-atmetrics]

---
source_file: 2007_09937.pdf
converter: mathpix
format: mmd
---

\title{
A ŁOJASIEWICZ INEQUALITY FOR ALE METRICS
}

\author{
ALIX DERUELLE AND TRISTAN OZUCH
}

\begin{abstract}
We introduce a new functional inspired by Perelman's $\lambda$-functional adapted to the asymptotically locally Euclidean (ALE) setting and denoted $\lambda_{\text {ALE }}$. Its expression includes a boundary term which turns out to be the ADM-mass. We prove that $\lambda_{\text {ALE }}$ is defined and analytic on convenient neighborhoods of Ricci-flat ALE metrics and we show that it is monotonic along the Ricci flow. This for example lets us establish that small perturbations of integrable and stable Ricci-flat ALE metrics with nonnegative scalar curvature have nonnegative mass. We then introduce a general scheme of proof for a Łojasiewicz-Simon inequality on non-compact manifolds and prove that it applies to $\lambda_{\text {ALE }}$ around Ricci-flat metrics. We moreover obtain an optimal weighted Lojasiewicz exponent for metrics with integrable Ricci-flat deformations.
\end{abstract}

\section*{Contents}

Introduction
\begin{itemize}
\item[1.] A relative energy for ALE Ricci-flat metrics
\item[2.] First and second variations of $\lambda_{\text {ALE }}^{0}$
\item[3.] A functional defined on a $C_{\tau}^{2, \alpha}$-neighborhood of Ricci-flat ALE metrics
\item[4.] Energy estimates on the potential function
\item[5.] Fredholm properties of the Lichnerowicz operator in weighted spaces
\item[6.] Properties of $\lambda_{\text {ALE }}$ in the integrable case
\item[7.] A Lojasiewicz inequality for $\lambda_{\text {ALE }}$ : the general case
\item[8.] Deformation of Ricci-flat ALE metrics, scalar curvature and mass
\end{itemize}

Appendix A. Real analytic maps between Banach spaces
Appendix B. Divergence-free gauging of asymptotically conical spaces
Appendix C. First and second variations of geometric quantities
References

\section*{Introduction}

The understanding of Ricci-flat metrics is a classical issue in Riemannian geometry. When they are non-compact, these metrics have at most Euclidean volume growth by Bishop-Gromov inequality and those which exactly have Euclidean volume growth are asymptotically conical. In dimension 4, this implies that they are Asymptotically Locally Euclidean (ALE), that is they are asymptotic to some quotient of Euclidean space, see Definition 1.1.

The class of ALE Ricci-flat metrics models the formation of singularities in various noncollapsed situations, in particular for spaces with Ricci curvature bounds [And90, BKN89]. Moreover, these metrics model potential singularities of a 4-dimensional Ricci flow with bounded

\footnotetext{
Date: today.
}
scalar curvature [BZ17]. Even more recently however, it has been shown that Ricci flows on a closed Riemannian manifold of dimension less than 8 with bounded scalar curvature exist for all time: [BD20]. Finally, ALE Ricci flat metrics actually appear as finite-time blow-up limits of some Ricci flows App19. Their stability therefore becomes a crucial question for the Ricci flow.

Adapting Perelman's $\lambda$-functional to the ALE setting. In [Per02], Perelman introduced three functionals denoted $\lambda, \mu$ and $\nu$ of which the Ricci flow is the gradient flow. These functionals were the core of his spectacular proofs and revolutionized the understanding of the formation of singularities of the Ricci flow. In particular, recall that if $\left(M^{n}, g\right)$ is a closed smooth Riemannian manifold, Perelman's energy, denoted by $\lambda(g)$, is defined as follows:
$$\lambda(g):=\inf _{\|\varphi\|_{L^{2}}=1} \int_{M} 4\left|\nabla^{g} \varphi\right|_{g}^{2}+\mathrm{R}_{g} \varphi^{2} d \mu_{g}$$
In other terms, $\lambda(g)$ is the bottom of the spectrum of the Schrödinger operator $-4 \Delta_{g}+\mathrm{R}_{g}$. Then Perelman showed that $\lambda$ is monotone non-decreasing along the Ricci flow and it is constant on Ricci-flat metrics only.

Let us notice some major inconvenients to use the same definition (0.1) in a non-compact setting : if $\left(M^{n}, g\right)$ is an ALE metric in a neighborhood (with respect to some natural topology designed on polynomially decaying tensors at a certain rate) of a given ALE Ricci-flat metric then it can be shown that $\lambda(g)=0$. In other words, the $\lambda$-functional in its usual $L^{2}$ -constrained form is not well-suited because of the lack of non trivial minimizers.

Our goal here is twofold. On the one hand, we aim at defining a functional on suitable neighborhoods of any ALE Ricci-flat metrics which detects Ricci-flat metrics only. On the other hand, we wish to define an adequate notion of linear stability for an ALE Ricci-flat metric tied to our functional in order to study the relation between linear stability and dynamical stability along the Ricci flow. The second goal will be addressed in a forthcoming paper.

Our work relies on that of Haslhofer [Has11] who introduced a functional which we denote by $\lambda_{\text {ALE }}^{0}$ and where the minimization in (0.1) takes place among test functions $\varphi$ such that $\varphi-1$ is compactly supported. It is a convenient functional when the scalar curvature is nonnegative and integrable: in Has11, $\lambda_{\text {ALE }}^{0}(g)$ is compared to the ADM mass $m_{\text {ADM }}(g)$ of $g$ in order to give a quantitative version of the positive mass theorem on asymptotically flat manifolds (satisfying additional assumptions). Despite its good properties with respect to the Ricci flow or its link to the ADM mass, the functional $\lambda_{\text {ALE }}^{0}$ is only defined on a suitable neighborhood of metrics of a given ALE Ricci-flat metric $\left(N^{n}, g_{b}\right)$ whose scalar curvatures are either integrable or decay sufficiently fast at infinity. Such sets of metrics are not closed with respect to the topology induced by Hölder spaces modeled on polynomially decaying tensors with rate $\tau>\frac{n-2}{2}$. This classical restriction on the rate ensures that any deformation of the metric has its gradient lying in $L^{2}$. This observation is a major drawback to establish finer properties of the functional $\lambda_{\text {ALE }}^{0}$ such as a Lojasiewicz inequality we discuss below.

To remedy these issues, we refine the definition of $\lambda_{\text {ALE }}^{0}$ by substracting the ADM mass. It gives in turn a new functional called $\lambda_{\text {ALE }}$ and formally defined by:
$$\lambda_{\mathrm{ALE}}(g):=\lambda_{\mathrm{ALE}}^{0}(g)-m_{\mathrm{ADM}}(g) .$$
At first sight, the functional $\lambda_{\text {ALE }}$ still seems to require the integrability of the scalar curvature to make sense of each term: it turns out that (0.2) can be reinterpreted as the limit of the difference of two a priori divergent integrals: see Section 3 for a precise statement. Again, in
case a metric $g$ has integrable scalar curvature and lies in a neighborhood of an ALE Ricci-flat metric, the formula (0.2) makes sense and lets one to compute $\lambda_{\text {ALE }}$ more explicitly. We show that this functional fulfills our specifications: it is defined on a whole neighborhood of an ALE Ricci-flat metric whether its ADM mass is finite or not. Furthermore, it is analytic, its gradient vanishes on Ricci-flat ALE metrics only and the Ricci flow is moreover its gradient flow: see Section 3 for rigorous statements and proofs.

The second variation of $\lambda_{\text {ALE }}$ at an ALE Ricci-flat metric ( $N^{n}, g_{b}$ ) along divergence-free variations is half the Lichnerowicz operator $L_{g_{b}}:=\Delta_{g_{b}}+2 \operatorname{Rm}\left(g_{b}\right) *$, i.e. if $h$ is a smooth compactly supported 2-tensor on $N$,
$$\delta_{g_{b}}^{2} \lambda(h, h)=\frac{1}{2}\left\langle L_{g_{b}} h, h\right\rangle_{L^{2}}, \quad \operatorname{div}_{g_{b}} h=0 .$$
This fact alone strongly suggests that the linear stability of an ALE Ricci-flat metric $\left(N^{n}, g_{b}\right)$ should be defined in terms of the non-positivity of the associated Lichnerowicz operator $L_{g_{b}}$ restricted to divergence-free variations: this guess is not new and was investigated in the setting of Ricci-flat cones by Haslhofer-Hall-Siepmann [HHS14]. Linear stability actually gives some non trivial local information in the integrable case, i.e. in the case where the space of ALE Ricci-flat metrics in the neighborhood of a fixed ALE Ricci-flat metric is a smooth finite-dimensional manifold: see Proposition 6.6 for a formal statement.

Proposition 0.1. Any ALE Ricci-flat metric $\left(N^{n}, g_{b}\right)$ which is locally stable and integrable is a local maximum for the functional $\lambda_{\text {ALE }}$.

The statement of Proposition 0.1 echoes [Has12]: the proof is however technically different.
We also obtain in Section 8 new quantitative positive mass theorems in the same spirit of [Has11] for small metric perturbations of stable Ricci-flat ALE metrics: see Corollary 8.1. Note that the positive mass theorem generally does not hold on ALE manifolds [LeB88].

The positive mass theorem however holds for spin ALE manifolds, see [Nak90]. Pushing Nakajima's estimate further similarly to [Has11] in the asymptotically Euclidean setting, we prove the following global property satisfied by the functional $\lambda_{\text {ALE }}$ on spin manifolds.

Proposition 0.2 (Proposition 8.4). Let $\left(N^{4}, g\right)$ be an ALE metric of order $\tau>1=\frac{4}{2}-1$ on a spin manifold asymptotic to $\mathbb{R}^{4} / \Gamma$ for $\Gamma \subset \operatorname{SU}(2)$. Assume the scalar curvature $\mathrm{R}_{g}$ is integrable and non-negative. Then, we have
$$\lambda_{\mathrm{ALE}}(g) \leq 0,$$
that is
$$m_{\mathrm{ADM}}(g) \geqslant \lambda_{\mathrm{ALE}}^{0}(g) \geqslant 0,$$
with equality if and only if $\left(N^{4}, g\right)$ is one of Kronheimer's gravitational instantons [Kro89].
These well-known gravitational instantons are therefore the (only) maximizers of $\lambda_{A L E}$ with non negative and integrable scalar curvature.

A Łojasiewicz inequality for $\lambda_{\text {ALE }}$. A certain number of difficulties arises when it comes to study the dynamical stability of ALE Ricci-flat metrics along the Ricci flow. A first obstacle is the presence of a non-trivial kernel of the Lichnerowicz operator. This issue already occurs in the case of a closed Ricci-flat metric. The non-compactness of the underlying space is an additional source of trouble since 0 is not isolated in the spectrum of the linearized operator. This fact explains a polynomial-in-time convergence instead of an exponential rate in the case of an integrable Ricci-flat metric on a closed manifold, as it was demonstrated in [Has12].

One tool that has been quite popular to study the stability of fixed points of geometric evolution equations is the notion of Łojasiewicz-Simon inequalities. Its name comes from both the classical work of Lojasiewicz [Ło65] on finite dimensional dynamical systems of gradient type and that of L. Simon [Sim83] who extended systematically these inequalities to functionals defined on infinite dimensional spaces. The main geometric applications obtained in [Sim83] concern the uniqueness of tangent cones of isolated singularities of minimal surfaces in Euclidean space together with the uniqueness of tangent maps of minimizing harmonic maps with values into an analytic closed Riemannian manifold. These geometric equations have the advantage to be strongly elliptic. Notice that all these results do not hold true if one drops the assumption on the analyticity of the data under consideration.

Łojasiewicz-Simon inequalities have been extensively used these last years in the context of mean curvature flow, especially to prove the uniqueness of blow-ups [CM15].

In the compact setting, Łojasiewicz inequalities have been proved for Perelman's $\lambda$-functional in the neighborhood of compact Ricci-flat metrics in [Has12] in the integrable case, and in [HM14] in the general case, see also [Krö15] for Ricci solitons. They have been applied to characterize the stability and instability of the Ricci flow at compact Ricci-flat metrics.

Our main application is to prove a similar result for Ricci-flat ALE metrics. We provide a general scheme of proof for Łojasiewicz inequalities on non-compact manifolds based on the theory of elliptic operators between weighted Hölder spaces.

We first show how such an inequality can be proved "by hand" in the integrable and stable situation, but we realize that this only leads to an actual Lojasiewicz inequality in dimensions greater than or equal to 5. We introduce a general scheme of proof, based on that of [CM14], for weighted Łojasiewicz inequalities for ALE metrics which holds without integrability or stability assumption in dimensions greater than or equal to 4 and we provide an optimal exponent in the integrable case. By weighted Lojasiewicz inequalities, we mean that the norm of the gradient of the corresponding functional is a weighted $L^{2}$-norm. More specifically here, we consider the space $L_{\frac{n}{2}+1}^{2}$ which, roughly speaking, is the space of tensors $T$ such that $r \cdot T$ belongs to $L^{2}, r$ being the distance from a fixed point: see Definition 1.3 for a formal definition. The necessity of using such weighted norms rather than using the usual $L^{2}$ norm is explained below.

Our main result is that the functional $\lambda_{\text {ALE }}$ satisfies an $L_{\frac{n}{2}+1}^{2}$-Lojasiewicz inequality in a neighborhood of any ALE Ricci-flat metric with respect to the topology of weighted Hölder spaces $C_{\tau}^{2, \alpha}, \alpha \in(0,1)$, with polynomial decay of rate $\tau \in\left(\frac{n-2}{2}, n-2\right)$.

Theorem 0.3. Let $\left(N^{n}, g_{b}\right)$ be an ALE Ricci-flat manifold of dimension $n \geq 4$. Let $\alpha \in(0,1)$ and $\tau \in\left(\frac{n-2}{2}, n-2\right)$. Then there exist a neighborhood $B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right)$ of $g_{b}$, a constant $C>0$ and $\theta \in(0,1)$ such that for any metric $g \in B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right)$, we have the following $L_{\frac{n}{2}+1}^{2}$-Lojasiewicz inequality,
$$\left|\lambda_{\mathrm{ALE}}(g)\right|^{2-\theta} \leq C\left\|\nabla \lambda_{\mathrm{ALE}}(g)\right\|_{L_{\frac{n}{2}+1}^{2}}^{2} .$$
Moreover, if $\left(N^{n}, g_{b}\right)$ has integrable infinitesimal Ricci-flat deformations, then $\theta=1$.
In particular, if $n \geq 5$, one has the following $L^{2}$-Łojasiewicz inequality for integrable Ricciflat ALE metrics: if $\tau \in\left(\frac{n}{2}, n-2\right)$ then for any $0<\delta<\frac{2 \tau-(n-2)}{2 \tau-(n-4)}$, there exists $C>0$ such that for all $g \in B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \epsilon\right)$,
$$\left|\lambda_{\mathrm{ALE}}(g)\right|^{2-\theta_{L^{2}}} \leq C\left\|\nabla \lambda_{\mathrm{ALE}}(g)\right\|_{L^{2}}^{2}, \quad \theta_{L^{2}}:=2-\frac{1}{\delta} .$$

Here $\nabla \lambda_{\text {ALE }}$ denotes the gradient of $\lambda_{\text {ALE }}$ in the $L^{2}$ sense.
The fact that our spaces are non-compact induces quite a lot of new difficulties. In particular, the spectrum of the Lichnerowicz operator is not discrete anymore and 0 belongs to the essential spectrum. This explains the need of considering weighted Sobolev spaces different from $L^{2}$ for which the differential of $\nabla \lambda_{\text {ALE }}$ at a Ricci-flat ALE metric is Fredholm. We underline the fact that while Theorem 0.3 gives an optimal $L_{\frac{n}{2}+1}^{2}$-Lojasiewicz inequality, we cannot reach the usual optimal $L^{2}$-Lojasiewicz exponent $\theta_{L^{2}}=1$ (note that we approach it as $\tau$ is close to $n-2$ and the dimension tends to $+\infty$ ) in the integrable case: see also [HJ11, Theorem 2.1] for a proof of this fact in a general linear setting. This is consistent with the known fact that the DeTurck-Ricci flow only converges polynomially fast for perturbations of the Euclidean space: see for instance [SSS11] and [App18]. Indeed, an exponent $\theta_{L^{2}}=1$ implies that the convergence is exponential.

Remark 0.4. Most of the analysis of this article should apply to the Ricci-flat asymptotically conical case. However, the other classical asymptotics in dimension 4, namely ALF, ALG and ALH should require more involved arguments.

In a forthcoming article, we use the $L_{\frac{n}{2}+1}^{2}$-Lojasiewicz inequality (0.4) to investigate the dynamical stability of Ricci-flat ALE metrics.

Outline of paper. In Section 1, we begin by recalling the basics of ALE Ricci-flat metrics including the definitions of polynomially weighted Hölder and Sobolev function spaces. Next, Section 1.2 recalls the definition of the ADM-mass of an ALE Ricci-flat metric and discusses various topologies on the set of nearby metrics which appear in the literature on the study of the mass on ALE metrics. Section 1.3 introduces the $\lambda_{\text {ALE }}^{0}-$ functional and studies its basic properties in the previously mentioned topology: this is the content of Proposition 1.12. Section 2 is devoted to compute the first and second variations of $\lambda_{\text {ALE }}^{0}$ which are summarized in Propositions 2.3 and 2.7.

In Section 3, Proposition 3.4 proves that substracting the ADM-mass to $\lambda_{\text {ALE }}^{0}$ yields a much better-behaved and analytic functional that we denote $\lambda_{\text {ALE }}$. The second variation of $\lambda_{\text {ALE }}$ is computed in Proposition 3.7. Moreover, the monotonicity of $\lambda_{\text {ALE }}$ along the Ricci flow is established in Proposition 3.13. We also take the opportunity to define the linear stability of an ALE Ricci-flat metric: Lemma 3.18 gives two other equivalent ways of defining the notion of linear stability for such a class of metrics.

In Sections 4 and 5, we prove some technical results which are crucial for the rest of the paper. We first prove energy bounds for the potential function appearing in the definition of $\lambda_{\text {ALE }}$ in Proposition 4.1. We then give the Fredholm properties of the Hessian of $\lambda_{\text {ALE }}$, the Lichnerowicz Laplacian, in weighted Hölder and Sobolev spaces: this is the content of Proposition 5.1.

In Sections 6 and 7, we prove Lojasiewicz inequalities satisfied by the functional $\lambda_{\text {ALE }}$. We first consider a naïve proof "by hand" in the integrable and stable case in dimension greater than or equal to 5 in Section 6. More specifically, Section 6.1 starts with a precise description of neighborhoods of integrable ALE Ricci-flat metrics: see Proposition 6.2. Using it, we prove Proposition 0.1 reformulated more accurately in Proposition 6.6. In Section 6.2, a first attempt to prove a Lojasiewicz inequality for integrable ALE Ricci-flat metrics is given by following an idea due to Haslhofer [Has12]: Proposition 6.10 yields an infinitesimal version of the Lojasiewicz inequality for $\lambda_{\text {ALE }}$ with a non-trivial Lojasiewicz exponent $\theta$ in dimension
greater than or equal to 5. This can be interpreted as a preliminary step to the general case developed in Section 7.

We then prove a general Łojasiewicz inequality in Section 7 by extending the classical reduction to the finite-dimensional situation of [Sim83]: more precisely, we adapt the concise version of [CM14] to this non-compact setting in Sections 7.1 and 7.2. This requires the study of the Fredholm properties of the Lichnerowicz operator between weighted Hölder and Sobolev spaces. The proof of a general Łojasiewicz inequality (0.4) needs a priori energy estimates which are taken care by Proposition 7.10 in Section 7.3 as required by Proposition 7.1. Section 7.3 ends with the proof of Theorem 0.3 restated as Theorem 7.11 (the general case) and Theorem 7.12 in the integrable case.

In Section 8, we give some connections between the mass $m_{\text {ADM }}$ and the functional $\lambda_{\text {ALE }}$. We deduce that the positive mass theorem holds in neighborhoods of Ricci-flat ALE metrics which are local maximizers of $\lambda_{\text {ALE }}$. In particular, any compactly supported (or sufficiently decaying) deformation with nonnegative scalar curvature of a given integrable and locally stable Ricci-flat ALE metric is Ricci-flat: see Corollary 8.1. Proposition 8.4 shows that ALE Ricci-flat metrics on spin manifolds are global maximizers of $\lambda_{\text {ALE }}$.

We then recall some basic results about real analytic maps between Banach spaces in Appendix A, we prove a divergence-free gauge-fixing for ALE metrics in Appendix B. Finally, we also recall the variations of some geometric quantities in Appendix C.
0.1. Acknowledgements. The first author is supported by grant ANR-17-CE40-0034 of the French National Research Agency ANR (Project CCEM).

\section*{1. A relative energy for ALE Ricci-flat metrics}

Let us introduce a non-compact version of Perelman's $\lambda$-functional and study its properties on ALE metrics.

\subsection*{1.1. Main definitions.}

We start by defining the class of metrics as well as the function spaces we will be interested in.

Definition 1.1 (Asymptotically locally Euclidean (ALE) manifolds). We will call a Riemannian manifold ( $N^{n}, g$ ) asymptotically locally Euclidean (ALE) of order $\tau>0$ if the following holds: there exists a compact set $K \subset N$, a radius $R>0, \Gamma$ a subgroup of $S O(n)$ acting freely on $\mathbb{S}^{n-1}$ and a diffeomorphism $\Phi:\left(\mathbb{R}^{n} / \Gamma\right) \backslash B_{e}(0, R) \mapsto N \backslash K$ such that, if we denote $g_{e}$ the Euclidean metric on $\mathbb{R}^{n} / \Gamma$, we have, for all $k \in \mathbb{N}$,
$$\rho^{k}\left|\nabla^{g_{e}, k}\left(\Phi^{*} g-g_{e}\right)\right|_{e}=O\left(\rho^{-\tau}\right),$$
on $\left(\mathbb{R}^{n} / \Gamma\right) \backslash B_{e}(0, R)$, where $\rho=d_{e}(., 0)$.
If $g$ is an ALE metric on $N$, then we denote by $\rho_{g}$ any smooth positive extension of (the push-forward of) the radial distance on $\mathbb{R}^{n}, \Phi_{*} \rho$. In particular, we will use the fact that the level sets $\left\{\rho_{g}=R\right\}$ of $\rho_{g}$ are smooth closed connected hypersurfaces for sufficiently large height $R$ constantly.

We will study ALE metrics in a neighborhood of a Ricci-flat ALE metric. Let us start by defining this neighborhood thanks to weighted norms :

Definition 1.2 (Weighted Hölder norms for ALE metrics). Let $(N, g, p)$ be an ALE manifold of dimension $n, \beta>0$. For any tensor $s$, we define the following weighted $C_{\beta}^{k, \alpha}$-norm :
$$\|s\|_{C_{\beta}^{k, \alpha}}^{g}:=\sup _{N} \rho_{g}^{\beta}\left(\sum_{i=0}^{k} \rho_{g}^{i}\left|\nabla^{g, i} s\right|_{g}+\rho_{g}^{k+\alpha}\left[\nabla^{g, k} s\right]_{C^{0, \alpha}}\right) .$$

Definition 1.3 (Weighted Sobolev norms for ALE metrics). Let $\beta>0$, and $(N, g, p)$ an ALE manifold of dimension $n$. For any tensor $s$, we define the following weighted $L_{\beta}^{2}$-norm :
$$\|s\|_{L_{\beta}^{2}}^{g}:=\left(\int_{N}|s|^{2} \rho_{g}^{2 \beta-n} d \mu_{g}\right)^{\frac{1}{2}} .$$
We moreover define the $H_{\beta}^{k}$-norm of $s$ as
$$\|s\|_{H_{\beta}^{k}}^{g}:=\sum_{i=0}^{k}\left\|\nabla^{i} s\right\|_{L_{\beta+i}^{2}}^{g} .$$

Remark 1.4. The usual $L^{2}$ space equals $L_{\frac{n}{2}}^{2}$ with the above definition. The intuition behind these norms is that $\rho_{g}^{-\beta} \in C_{\beta}^{k, \alpha}$ and for all $\beta^{\prime}>\beta, \rho_{g}^{-\beta^{\prime}} \in H_{\beta}^{k}$.

Remark 1.5. Moreover, we have the following embeddings: for $k$ large enough depending on the dimension:
$$H_{\beta}^{k} \subset C_{\beta}^{0, \alpha},$$
and for $\beta<\beta^{\prime}$, we have
$$C_{\beta^{\prime}}^{k, \alpha} \subset H_{\beta}^{k},$$
see [Bar86, Theorem 1.2]. Notice that in [Bar86], $W_{\beta}^{k, 2}$ coincides with our space $H_{-\beta}^{k}$ for $\beta \in \mathbb{R}$.

Note 1.6. In the rest of this article, we will almost always work in a neighborhood of a fixed Ricci-flat metric with a given topology. Since the above definitions do not formally depend on the type of tensor, we will often abusively omit to mention these informations and simply denote these spaces $C_{\tau}^{k, \alpha}$ for instance.

Finally, we state a version of Hardy's inequality proved by Minerbe [Min09] for Riemannian metrics $\left(N^{n}, g\right)$ with nonnegative Ricci curvature and maximal volume growth, i.e. $\operatorname{AVR}(g):=$ $\lim _{r \rightarrow+\infty} r^{-n} \operatorname{Vol}_{g} B_{g}(p, r)>0$ for some point $p$ and hence for all points by Bishop-Gromov Theorem:

Theorem 1.7 (Minerbe's Hardy's inequality). Let $\left(N^{n}, g\right)$ be a complete Riemannian manifold such that $\operatorname{Ric}(g) \geq 0$ and $\operatorname{AVR}(g)>0$. Then for some point $p \in N$,
$$\int_{N} r_{p}^{-2} \varphi^{2} d \mu_{g} \leq C(n, \operatorname{AVR}(g)) \int_{N}\left|\nabla^{g} \varphi\right|_{g}^{2} d \mu_{g}, \quad \forall \varphi \in C_{c}^{\infty}(N),$$
where $r_{p}(x):=d_{g}(p, x)$ if $x \in N$.

\subsection*{1.2. The mass of an ALE metric.}

Next, we define the class of ALE metrics (with a finite amount of regularity at infinity) we will focus on at the beginning of this article: let $\left(N^{n}, g_{b}\right)$ be an ALE Ricci-flat metric and let us consider for $\tau>\frac{n-2}{2}$ and $\alpha \in(0,1)$, the following space of metrics
$$\mathcal{M}_{\tau}^{2, \alpha}\left(g_{b}\right):=\left\{g \text { is a metric on } N \mid g-g_{b} \in C_{\tau}^{2, \alpha}\left(S^{2} T^{*} N\right), \mathrm{R}_{g}=O\left(\rho_{g_{b}}^{-\tau^{\prime}}\right) \text { for some } \tau^{\prime}>n\right\} .$$
It turns out that this space is convex:
Lemma 1.8. We have the following characterization of the space $\mathcal{M}_{\tau}^{2, \alpha}\left(g_{b}\right)$ : a metric $g \in$ $\mathcal{M}_{\tau}^{2, \alpha}\left(g_{b}\right)$ if and only if $g-g_{b} \in C_{\tau}^{2, \alpha}\left(S^{2} T^{*} N\right)$ and the function $\operatorname{div}_{g_{b}} \operatorname{div}_{g_{b}}\left(g-g_{b}\right)-\Delta_{g_{b}} \operatorname{tr}_{g_{b}}(g-$ $g_{b}$ ) is in $C_{\tau^{\prime}}^{0}(N)$ for some $\tau^{\prime}>n$.

In particular, the space $\mathcal{M}_{\tau}^{2, \alpha}\left(g_{b}\right)$ is convex.
Proof. If $g_{1}$ and $g_{2}$ belong to $\mathcal{M}_{\tau}^{2, \alpha}\left(g_{b}\right)$, it is straightforward that any convex combination $\lambda_{1} g_{1}+\lambda_{2} g_{2}, \lambda_{i} \geq 0, i=1,2, \lambda_{1}+\lambda_{2}=1$, is again a metric on $N$ such that $\lambda_{1} g_{1}+\lambda_{2} g_{2}-g_{b} \in$ $C_{\tau}^{2, \alpha}\left(S^{2} T^{*} N\right)$. Now, by linearizing the scalar curvatures of the metrics $g_{i}=: g_{b}+h_{i}, i=1,2$ with respect to the metric $g_{b}$ thanks to [C.7, Lemma C.2], one gets:
$$\mathrm{R}_{g_{b}+h_{i}}=\mathrm{R}_{g_{b}}+\operatorname{div}_{g_{b}} \operatorname{div}_{g_{b}} h_{i}-\Delta_{g_{b}} \operatorname{tr}_{g_{b}} h_{i}+O\left(\rho_{g_{b}}^{-2 \tau-2}\right) .$$
Since $\mathrm{R}_{g_{b}+h_{i}}=O\left(\rho_{g_{b}}^{-\tau_{i}^{\prime}}\right)$, for some $\tau_{i}^{\prime}>n, i=1,2$, one concludes that
$$\operatorname{div}_{g_{b}} \operatorname{div}_{g_{b}} h_{i}-\Delta_{g_{b}} \operatorname{tr}_{g_{b}} h_{i}=O\left(\rho_{g_{b}}^{-\min \left\{2 \tau+2, \tau_{i}^{\prime}\right\}}\right) .$$
In particular, by summing the previous Taylor expansions of the scalar curvatures of $g_{b}+h_{i}$, $i=1,2$ together with (1.2), one observes that:
$$\begin{aligned}
\mathrm{R}_{g_{b}+\lambda_{1} h_{1}+\lambda_{2} h_{2}} & =\sum_{i=1}^{2} \lambda_{i}\left(\operatorname{div}_{g_{b}} \operatorname{div}_{g_{b}} h_{i}-\Delta_{g_{b}} \operatorname{tr}_{g_{b}} h_{i}\right)+O\left(\rho_{g_{b}}^{-2 \tau-2}\right) \\
& =O\left(\rho_{g_{b}}^{-\min \left\{2 \tau+2, \tau_{1}^{\prime}, \tau_{2}^{\prime}\right\}}\right) .
\end{aligned}$$
This proves the convexity of the space under consideration since $2 \tau+2>n$. \(\square\)

Remark 1.9. We already see the importance of the assumption $\tau>\frac{n-2}{2}$ which will be crucial all along this paper: it ensures that the nonlinear terms in the expansion of the Ricci or scalar curvature around a given ALE Ricci-flat metric decay faster than the linear ones and are integrable. When dealing with improper integrals for instance, only the linear terms have to be taken care of.

We endow the space $\mathcal{M}_{\tau}^{2, \alpha}\left(g_{b}\right)$ with the distance induced by the norm $\|\cdot\|_{C_{\tau}^{2, \alpha}}$ as a convex subspace of $C_{\tau}^{2, \alpha}\left(S^{2} T^{*} N\right)$ and write $\mathcal{M}_{\tau}^{2, \alpha}\left(g_{b}, \varepsilon\right)$ for $\mathcal{M}_{\tau}^{2, \alpha}\left(g_{b}\right) \cap B_{C_{\tau}^{2, \alpha}}\left(0_{S^{2} T^{*} N}, \varepsilon\right)$. Our choice of notations follow that of Dai-Ma [DM07], Lee-Parker [LP87] and Bartnik [Bar86] where they consider the more classical space of metrics
$$\mathcal{M}_{\tau}:=\left\{g \text { is a metric on } N\left|g-g_{b} \in C_{\tau}^{1, \alpha}\left(S^{2} T^{*} N\right)\right| \mathrm{R}_{g} \in L^{1}\right\},$$
on which the mass of an ALE metric is well-defined:
$$m_{\mathrm{ADM}}(g):=\lim _{R \rightarrow+\infty} \int_{\left\{\rho_{g_{b}}=R\right\}}\left\langle\operatorname{div}_{g_{b}}\left(g-g_{b}\right)-\nabla^{g_{b}} \operatorname{tr}_{g_{b}}\left(g-g_{b}\right), \mathbf{n}\right\rangle_{g_{b}} d \sigma_{g_{b}},$$
where n denotes the outward unit normal of the closed smooth hypersurfaces $\left\{\rho_{g_{b}}=R\right\}$ for $R$ large.

\subsection*{1.3. Definition of the functional $\lambda_{\mathrm{ALE}}^{0}$ and its main properties.}

We will use the renormalized Perelman's functional introduced by Haslhofer in [Has11] to study ALE metrics that are close to Ricci-flat metrics. It can be defined in the following way for ALE metrics.

Definition 1.10 ( $\lambda_{\text {ALE }}^{0}$, a first renormalized Perelman's functional). Let ( $N^{n}, g_{b}$ ) be an $A L E$ Ricci-flat metric and let $g \in \mathcal{M}_{\tau}^{2, \alpha}\left(g_{b}, \varepsilon\right)$. Define the $\mathcal{F}_{\text {ALE }}$-energy by:
$$\mathcal{F}_{\mathrm{ALE}}(w, g):=\int_{N}\left(4\left|\nabla^{g} w\right|_{g}^{2}+\mathrm{R}_{g} w^{2}\right) d \mu_{g}$$
where $w-1 \in C_{c}^{\infty}(N)$, where $C_{c}^{\infty}(N)$ is the space of compactly supported smooth functions. The $\lambda_{\text {ALE }}^{0}$-functional associated to the $\mathcal{F}_{\text {ALE }}$-energy is:
$$\lambda_{\mathrm{ALE}}^{0}(g):=\inf _{w} \mathcal{F}_{\mathrm{ALE}}(w, g),$$
where the infimum is taken over functions $w: N \rightarrow \mathbb{R}$ such that $w-1 \in C_{c}^{\infty}(N)$.
Remark 1.11. By testing the infimum condition with $w \equiv 1$, we get the upper bound
$$\lambda_{\mathrm{ALE}}^{0}(g) \leq \int_{N} \mathrm{R}_{g} d \mu_{g}$$

An assumption on the convergence rate $\tau$ and $\tau^{\prime}$ in the definition of the space $\mathcal{M}_{\tau}^{2, \alpha}\left(g_{b}\right)$ is crucial to make sense of the functional $\lambda_{\mathrm{ALE}}^{0}(g)$ : in particular, it ensures the integrability of the scalar curvature $\mathrm{R}_{g}$ of such an ALE metric $g$. The fact that $\lambda_{\text {ALE }}^{0}(g)>-\infty$ is not trivial will be established in the following section: it depends on Hardy's inequality (Theorem 1.7). See the proof of Proposition 1.12.

Let us now prove that the functional $\lambda_{\text {ALE }}^{0}$ has nice properties in sufficiently small neigh-borhoods of Ricci-flat ALE metrics. Let us mention that according to [BKN89, CT94], any $n$-dimensional Ricci-flat ALE metrics is ALE of order $n$.

Proposition 1.12. Let $\left(N^{n}, g_{b}\right)$ be an $A L E$ Ricci-flat metric asymptotic to $\mathbb{R}^{n} / \Gamma$, for some finite subgroup $\Gamma$ of $S O(n)$ acting freely on $\mathbb{S}^{n-1}$. Let $\tau \in\left(\frac{n-2}{2}, n-2\right)$ and $\alpha \in(0,1)$.

Then, there exists some positive $\varepsilon$ such that for any metric $g$ in a neighborhood $\mathcal{M}_{\tau}^{2, \alpha}\left(g_{b}, \varepsilon\right)=$ $\mathcal{M}_{\tau}^{2, \alpha}\left(g_{b}\right) \cap B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right)$ of $g_{b}$, the infimum defining the functional $\lambda_{\mathrm{ALE}}^{0}(g)$ is attained by the unique solution $w_{g}$ to the following equation,
$$\left\{\begin{array}{r}
-4 \Delta_{g} w_{g}+\mathrm{R}_{g} w_{g}=0, \\
w_{g}-1 \in C_{\tau}^{2, \alpha}(N) \cap C_{n-2}^{1, \alpha}(N) .
\end{array}\right.$$

Moreover, $w_{g}$ is positive on $N$ and we have the following expansion of $w_{g}$ at infinity :
$$w_{g}=1-\frac{\lambda_{\mathrm{ALE}}^{0}(g)|\Gamma|}{4(n-2) \operatorname{Vol} \mathbb{S}^{n-1}} \frac{1}{\rho_{g_{b}}^{n-2}}+O\left(\rho_{g_{b}}^{-n+2-\gamma}\right),$$
for some positive $\gamma$ and where $|\Gamma|$ is the cardinal of $\Gamma$.
Next, we have the equalities :
$$\lambda_{\mathrm{ALE}}^{0}(g)=\int_{N}\left(4\left|\nabla^{g} w_{g}\right|_{g}^{2}+\mathrm{R}_{g} w_{g}^{2}\right) d \mu_{g}=\int_{N} \mathrm{R}_{g} w_{g} d \mu_{g}$$
and,
$$\lambda_{\mathrm{ALE}}^{0}(g)=\lim _{R \rightarrow \infty} 4 \int_{\left\{\rho_{g_{b}}=R\right\}}\left\langle\nabla^{g} w_{g}, \mathbf{n}_{g_{b}}\right\rangle d \sigma_{g},$$
where $\mathbf{n}_{g_{b}}$ denotes the outward unit normal of $\left\{\rho_{g_{b}}=R\right\}$.
Finally, the map $g \in B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right) \rightarrow w_{g}-1 \in C_{\tau}^{2, \alpha}(N)$ is analytic in the sense of Definition A.1.

Proof. First of all, let us show that $\lambda_{\text {ALE }}^{0}(g)$ is finite, i.e. $\lambda_{\text {ALE }}^{0}(g)>-\infty$.
Since $\left(N^{n}, g_{b}\right)$ is a Ricci-flat ALE metric $\left(N^{n}, g_{b}\right)$, Theorem 1.7 ensures that the following Hardy inequality holds true:
$$C_{H} \int_{N} \frac{\varphi^{2}}{\rho_{g_{b}}^{2}} d \mu_{g_{b}} \leq \int_{N}\left|\nabla^{g_{b}} \varphi\right|_{g_{b}}^{2} d \mu_{g_{b}}, \quad \varphi \in C_{c}^{\infty}(N),$$
for some positive constant $C_{H}$ depending on $g_{b}$, the dimension $n$ and the base point $p \in N$ used in Definition 1.2 of $\rho_{g}$. Since the metrics $g$ and $g_{b}$ are equivalent, i.e. $C^{-1} g_{b} \leq g \leq C g_{b}$ for some positive constant depending on the neighborhood $B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right)$, the same Hardy inequality holds with a positive constant $C_{H}\left(g_{b}\right) / 2$ if $\varepsilon$ is chosen small enough. Moreover, (1.11) is valid for functions $w$ on $N$ such that $w-1 \in C_{\tau}^{2, \alpha}(N)$. This implies that:
$$\begin{aligned}
\int_{N} 4\left|\nabla^{g} w\right|_{g}^{2}+\mathrm{R}_{g} w^{2} d \mu_{g} & =\int_{N} 4\left|\nabla^{g}(w-1)\right|_{g}^{2}+\mathrm{R}_{g}(w-1+1)^{2} d \mu_{g} \\
& \geq 2 C_{H} \int_{N} \frac{(w-1)^{2}}{\rho_{g}^{2}} d \mu_{g}-\varepsilon \int_{N} \frac{(w-1)^{2}}{\rho_{g}^{2}} d \mu_{g}-c \int_{N}\left|\mathrm{R}_{g}\right| d \mu_{g} \\
& \geq-c \int_{N}\left|\mathrm{R}_{g}\right| d \mu_{g},
\end{aligned}$$
if $\varepsilon$ is chosen not greater than $2 C_{H}$ and where $c$ is a universal positive constant that may vary from line to line. This proves the finiteness of $\lambda_{\text {ALE }}^{0}(g)$ together with the fact that the operator $-4 \Delta_{g}+\mathrm{R}_{g}$ is non-negative and dominates $-\Delta_{g}$ in the $L^{2}$ sense, i.e. if $g \in B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right)$ then
$$\left\langle-4 \Delta_{g} \varphi+\mathrm{R}_{g} \varphi, \varphi\right\rangle \geq c\left\|\nabla^{g} \varphi\right\|_{L^{2}}^{2}, \quad \forall \varphi \in C_{c}^{\infty}(N) .$$
In particular, by density, inequality (1.12) holds for functions in $C_{\tau}^{2}(N)$ with $2 \tau>n-2$.
Claim 1. The operator $-4 \Delta_{g}+\mathrm{R}_{g}: C_{\tau}^{2, \alpha}(N) \rightarrow C_{\tau+2}^{0, \alpha}(N)$ is an isomorphism of Banach spaces for all $\alpha \in(0,1)$. Moreover, the map $g \in B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right) \mapsto\left(-4 \Delta_{g}+\mathrm{R}_{g}\right)^{-1} \mathrm{R}_{g} \in C_{\tau}^{2, \alpha}(N)$ is analytic.
Proof of Claim 1. Consider the map $\Psi: B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right) \times C_{\tau}^{2, \alpha}(N) \rightarrow C_{\tau+2}^{0, \alpha}(N)$ defined by $\Psi(g, v):=-4 \Delta_{g} v+\mathrm{R}_{g} v$. The map $\Psi$ is analytic in the sense of Definition A.1.

According to [Theorem 8.3.6 (a), Joy00], $\Delta_{g}: C_{\tau}^{2, \alpha}(N) \rightarrow C_{\tau+2}^{0, \alpha}(N)$ is an isomorphism of Banach spaces for all $\alpha \in(0,1)$. Fix $\alpha \in(0,1)$. Since $\mathrm{R}_{g}: C_{\tau}^{2, \alpha}(N) \rightarrow C_{\tau+2}^{0, \alpha}(N)$ is a compact operator, the operator $-4 \Delta_{g}+\mathrm{R}_{g}: C_{\tau}^{2, \alpha}(N) \rightarrow C_{\tau+2}^{0, \alpha}(N)$ is a Fredholm operator of index 0. In particular, it is an isomorphism if (and only if) it is injective. This in turn is ensured by (1.12) since $(N, g)$ has infinite volume. Therefore, the analytic version of the implicit function Theorem given by Lemma A. 2 applied to the map $\Psi$ gives us the expected result. \(\square\)

Now, let $\alpha \in(0,1)$ such that Claim 1 holds: since $\mathrm{R}_{g} \in C_{\tau+2}^{0, \alpha}(N)$, there exists a unique solution $v_{g} \in C_{\tau}^{2, \alpha}(N)$ to $-4 \Delta_{g} v_{g}+\mathrm{R}_{g} v_{g}=-\mathrm{R}_{g}$ and the map $g \in B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right) \rightarrow v_{g} \in$
$C_{\tau}^{2, \alpha}(N)$ is analytic. In particular, if $w_{g}:=1+v_{g}$ then $-4 \Delta_{g} w_{g}+\mathrm{R}_{g} w_{g}=0$. Let us show that this implies (1.9) and (1.10) by integrating by parts over sublevel sets $\left\{\rho_{g_{b}} \leq R\right\}$ of large radii $R$ whose boundary is $\left\{\rho_{g_{b}}=R\right\}$ :
$$\begin{aligned}
\int_{\left\{\rho_{g_{b}} \leq R\right\}} 4\left|\nabla^{g} w_{g}\right|^{2}+\mathrm{R}_{g} w_{g}^{2} d \mu_{g}= & \int_{\left\{\rho_{g_{b}} \leq R\right\}}-4 \Delta_{g} w_{g} \cdot w_{g}+\mathrm{R}_{g} w_{g} \cdot w_{g} d \mu_{g} \\
& +4 \int_{\left\{\rho_{g_{b}}=R\right\}}\left\langle\nabla^{g} w_{g}, \mathbf{n}_{g_{b}}\right\rangle \cdot w_{g} d \sigma_{g} \\
= & 0+4 \int_{\left\{\rho_{g_{b}}=R\right\}}\left\langle\nabla^{g} w_{g}, \mathbf{n}_{g_{b}}\right\rangle d \sigma_{g}+4 \int_{\left\{\rho_{g_{b}}=R\right\}}\left\langle\nabla^{g} w_{g}, \mathbf{n}_{g_{b}}\right\rangle \cdot v_{g} d \sigma_{g} \\
= & 4 \int_{\left\{\rho_{g_{b}}=R\right\}}\left\langle\nabla^{g} w_{g}, \mathbf{n}_{g_{b}}\right\rangle d \sigma_{g}+o(1),
\end{aligned}$$
as $R$ tends to $+\infty$. Similarly, by using (1.7):
$$\int_{\left\{\rho_{g_{b}} \leq R\right\}} \mathrm{R}_{g} w_{g} d \mu_{g}=4 \int_{\left\{\rho_{g_{b}} \leq R\right\}} \Delta_{g} w_{g} d \mu_{g}=4 \int_{\left\{\rho_{g_{b}}=R\right\}}\left\langle\nabla^{g} w_{g}, \mathbf{n}_{g_{b}}\right\rangle d \sigma_{g} .$$
Since $\mathrm{R}_{g}$ is integrable, taking a limit in the previous identity as $R$ tends to $+\infty$ is meaningful. To sum it up:
$$\int_{N} \mathrm{R}_{g} w_{g} d \mu_{g}=\lim _{R \rightarrow+\infty} 4 \int_{\left\{\rho_{g_{b}}=R\right\}}\left\langle\nabla^{g} w_{g}, \mathbf{n}_{g_{b}}\right\rangle d \sigma_{g}=\int_{N} 4\left|\nabla^{g} w_{g}\right|^{2}+\mathrm{R}_{g} w_{g}^{2} d \mu_{g}$$

Finally, to end the proof of (1.9) and (1.10), it suffices to show that:
$$\int_{N} 4\left|\nabla^{g}\left(w_{g}+\varphi\right)\right|_{g}^{2}+\mathrm{R}_{g}\left(w_{g}+\varphi\right)^{2} d \mu_{g} \geq \int_{N} 4\left|\nabla^{g} w_{g}\right|_{g}^{2}+\mathrm{R}_{g} w_{g}^{2} d \mu_{g}, \quad \forall \varphi \in C_{c}^{\infty}(N) .$$
This amounts to proving that:
$$\int_{N} 4\left|\nabla^{g} \varphi\right|_{g}^{2}+\mathrm{R}_{g} \varphi^{2} d \mu_{g}+2 \int_{N} 4\left\langle\nabla^{g} w_{g}, \nabla^{g} \varphi\right\rangle+\mathrm{R}_{g} w_{g} \varphi d \mu_{g} \geq 0, \quad \forall \varphi \in C_{c}^{\infty}(N) .$$
This is implied by (1.12) together with (1.7) after an integration by parts on the second integral of the lefthand side of the previous inequality (1.15).

We are left with proving the positivity of $w_{g}$ and the asymptotic expansion (1.8).
By Kato inequality, one can check that
$$\lambda_{\mathrm{ALE}}^{0}(g)=\mathcal{F}_{\mathrm{ALE}}\left(w_{g}, g\right) \geq \mathcal{F}_{\mathrm{ALE}}\left(\left|w_{g}\right|, g\right) .$$
Notice that (1.14) still holds for functions $\varphi \in H_{c}^{1}(N)$ (the completion of compactly supported functions for the $H^{1}$-norm), by taking the completion with respect to the norm $\varphi \rightarrow\left\|\nabla^{g} \varphi\right\|_{L^{2}}$. In particular, the function $\left|w_{g}\right|$ is a test function, i.e. $\left|w_{g}\right|-1 \in H_{c}^{1}(N)$ and it is a minimizer of $\lambda_{\text {ALE }}^{0}(g)$ by (1.16). As such, $\left|w_{g}\right|$ is a continuous weak solution to (1.7). Elliptic regularity together with elliptic Schauder estimates imply that $\left|w_{g}\right|$ is a $C_{l o c}^{2, \alpha}$-solution, so that $w_{g}$ has a sign and tends to 1 at infinity, i.e. $w_{g}$ is nonnegative. Now, $w_{g}$ is positive by the strong maximum principle for parabolic equations. Indeed, if
$$W_{g}(x, t):=\exp \left(\frac{\sup _{N} \mathrm{R}_{g}}{4} t\right) w_{g}(x),$$
for $x \in N$ and $t \in \mathbb{R}$, then $W_{g}$ is a super-solution to the heat equation:
$$\left(\partial_{t}-\Delta_{g}\right) W_{g} \geq 0 .$$

Therefore, the maximum principle leads to $W_{g}(x, t) \geq \int_{N} K(x, y, t) w_{g}(y) d \mu_{g}(y)>0$ for $t \geq 0$ where $K(x, y, t)$ denotes the positive heat kernel associated to $\Delta_{g}$.

Let us prove the asymptotic estimate (1.8).
Observe that if $w_{g}=1-c \rho_{g_{b}}^{2-n}+O\left(\rho_{g_{b}}^{2-n-\gamma}\right)$ for some $\gamma>0$ up to first order for some constant $c$ then (1.10) implies necessarily that
$$4 c(n-2) \operatorname{Vol}\left(\mathbb{S}^{n-1} / \Gamma\right)=\lim _{R \rightarrow+\infty} 4 \int_{\left\{\rho_{g_{b}}=R\right\}}\left\langle\nabla^{g} w_{g}, \mathbf{n}_{g_{b}}\right\rangle d \sigma_{g}=\lambda_{\mathrm{ALE}}^{0}(g)$$

Let us observe that $-4 \Delta_{g} v_{g}=-\mathrm{R}_{g} w_{g}=O\left(\rho_{g_{b}}^{-\tau^{\prime}}\right)$ with $\tau^{\prime}>n$. Therefore, by [Theorem 8.3.6 (b), Joy00], there exists a unique solution $u_{g} \in C_{n-2}^{1, \alpha}(N)$ to $-4 \Delta_{g} u_{g}=-\mathrm{R}_{g} w_{g}$ : here $\mathrm{R}_{g}$ is only assumed to lie in $C_{\tau^{\prime}}^{0}$ for some $\tau^{\prime}>n$ which does not ensure higher regularity on $u_{g}$ in $C_{n-2}^{2, \alpha}$. Moreover, it is shown that:
$$\begin{aligned}
u_{g} & =-\left(\frac{\mid \Gamma]}{4(n-2) \operatorname{Vol} \mathbb{S}^{n-1}} \int_{N} \mathrm{R}_{g} w_{g} d \mu_{g}\right) \rho_{g_{b}}^{2-n}+O\left(\rho_{g_{b}}^{2-n-\gamma}\right) \\
& =-\frac{\left.\lambda_{\mathrm{ALE}}^{0}(g) \mid \Gamma\right]}{4(n-2) \operatorname{Vol} \mathbb{S}^{n-1}} \rho_{g_{b}}^{2-n}+O\left(\rho_{g_{b}}^{2-n-\gamma}\right),
\end{aligned}$$
for some positive $\gamma$ where we used (1.17) together with the first equality of (1.13) in the second line. To conclude, one gets that $v_{g}-u_{g}$ is a harmonic function on $N$ that converges to 0 at infinity. These facts imply that $v_{g}=u_{g}$ by the maximum principle. \(\square\)

Remark 1.13. Under the assumptions of Proposition 1.12, the usual $L^{2}$-constrained $\lambda$ -functional, i.e. the bottom of the $L^{2}$-spectrum of the operator $-4 \Delta_{g}+\mathrm{R}_{g}$ is vanishing because the mass can escape to infinity, and therefore this functional does not give any information: indeed, by (1.12), $\lambda_{1}\left(-4 \Delta_{g}+\mathrm{R}_{g}\right) \geq c \lambda_{1}\left(-\Delta_{g}\right)=0$. One can then argue by contradiction as in [CY75] to show that if $\lambda_{1}\left(-4 \Delta_{g}+\mathrm{R}_{g}\right)$ were positive then geodesic balls of large radii would grow faster than any polynomial.

The functional $\lambda_{\text {ALE }}^{0}$ is moreover invariant by diffeomorphisms decaying at infinity.
Proposition 1.14. Let $\left(N^{n}, g_{b}\right)$ be an $A L E$ Ricci-flat metric asymptotic to $\mathbb{R}^{n} / \Gamma$, for some finite subgroup $\Gamma$ of $S O(n)$ acting freely on $\mathbb{S}^{n-1}$. Let $\alpha \in(0,1)$ and $\tau \in\left(\frac{n-2}{2}, n-2\right)$.

Let $g$ be a metric in $\mathcal{M}_{\tau}^{2, \alpha}\left(g_{b}, \varepsilon\right)$ and let $w_{g}$ be the minimizer of $\lambda_{\text {ALE }}^{0}(g)$ whose existence is ensured by Proposition 1.12. Consider $\phi$ a diffeomorphism close to the identity in the $C_{\tau-1}^{3, \alpha}(T N)$ topology. Then, we have $\lambda_{\text {ALE }}^{0}\left(\phi^{*} g\right)=\lambda_{\text {ALE }}^{0}(g)$ and $w_{\phi^{*} g}=\phi^{*} w_{g}$.
Proof. Let $g=: g_{b}+h$ be a metric such that $g_{b}+h \in \mathcal{M}_{\tau}^{2, \alpha}\left(g_{b}\right)$, and consider $w_{g}$ the minimizer of $\lambda_{\text {ALE }}^{0}(g)$. Let $\phi: N \rightarrow N$ be a diffeomorphism defined as $\phi: x \mapsto \exp _{x}^{g}(X(x))$ for a vector field $X \in C_{\tau-1}^{3, \alpha}(T N)$ close to $0_{T N}$. Consider $\phi^{*} g$ which is also a metric on $N$ of order $\tau$ lying in a small neighborhood of $g_{b}$ in the $C_{\tau}^{2, \alpha}$ topology. Moreover, since $\mathrm{R}_{\phi^{*} g}=\phi^{*} \mathrm{R}_{g}$, we still have $\mathrm{R}_{\phi^{*} g} \in C_{\tau^{\prime}}^{0}(N)$ for some $\tau^{\prime}>n$. Then, for any $w$ such that $w-1$ is compactly supported, $\phi^{*} w-1$ is also compactly supported and we clearly have $\mathcal{F}_{\mathrm{ALE}}\left(\phi^{*} w, \phi^{*} g\right)=\mathcal{F}_{\mathrm{ALE}}(w, g)$ by the change of variables Theorem. Therefore we have $\lambda_{\text {ALE }}^{0}\left(\phi^{*} g\right)=\lambda_{\text {ALE }}^{0}(g)$, and finally, Proposition 1.12 ensures that $w_{\phi^{*} g}=\phi^{*} w_{g}$. \(\square\)

We end this section by giving another sufficient condition to ensure the finiteness of $\lambda_{\text {ALE }}^{0}$ together with its behavior under scalings of the metrics:

Lemma 1.15. Let $\left(N^{n}, g\right)$ be a complete metric with $\mathrm{R}_{g} \in L^{1}(N)$ and non-negative scalar curvature. Then,
$$0 \leq \lambda_{\mathrm{ALE}}^{0}(g) \leq\left\|\mathrm{R}_{g}\right\|_{L^{1}} .$$

Moreover, in case ( $N^{n}, g$ ) is a complete metric such that $\lambda_{\mathrm{ALE}}^{0}(g)$ is finite then for any $s>0$, we have
$$\lambda_{\mathrm{ALE}}^{0}(s g)=s^{\frac{n-2}{2}} \lambda_{\mathrm{ALE}}^{0}(g) .$$
Proof. By testing the function $w \equiv 1$ in the definition of $\lambda_{\text {ALE }}^{0}(g)$, one gets the upper bound. Moreover, one has the straightforward inequality for any function $w$ such that $w-1 \in C_{c}^{\infty}(N)$ :
$$0 \leq \int_{N}\left|\nabla^{g} w\right|_{g}^{2} d \mu_{g} \leq \int_{N}\left|\nabla^{g} w\right|_{g}^{2}+\mathrm{R}_{g} w^{2} d \mu_{g}$$
By considering the infimum over such functions $w$, one gets the expected lower bound on $\lambda_{\text {ALE }}^{0}(g)$.

For any smooth $w$ such that outside a compact set we have $w \equiv 1, \mathcal{F}_{\mathrm{ALE}}(w, s g)=$ $s^{\frac{n}{2}-1} \mathcal{F}_{\text {ALE }}(w, g)$, because of the scaling behavior of the different operations: $\left|\nabla^{s g} f\right|^{2}{ }_{s g}=$ $s^{-1}\left|\nabla^{g} f\right|_{g}^{2}, \mathrm{R}_{s g}=s^{-1} \mathrm{R}_{g}$ and $d \mu_{s g}=s^{\frac{n}{2}} d \mu_{g}$. We therefore have $\lambda_{\text {ALE }}^{0}(s g)=s^{\frac{n}{2}-1} \lambda_{\text {ALE }}^{0}(g)$. \(\square\)

\section*{2. First and second variations of $\lambda_{\text {ale }}^{0}$}

In this section, we compute the first and second variations of the functional $\lambda_{\text {ALE }}^{0}$ introduced in Section 1. Before doing so, we define the notion of a potential function associated to a metric $g$ lying in a $C_{\tau}^{2, \alpha}$-neighborhood of an ALE Ricci-flat metric $g_{b}$.

Definition 2.1. For a metric $g$ in $B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right)$, with $\tau \in\left(\frac{n-2}{2}, n-2\right)$, let us define the potential function associated to $g$ by
$$f_{g}:=-2 \ln w_{g},$$
where $w_{g}$ is defined as in Proposition 1.12 .
Notice that $f_{g}$ is well-defined by the positivity of $w_{g}$ ensured by Proposition 1.12. Moreover, we sum up the properties shared by $f_{g}$ in the next proposition which follow in a straightforward way from Proposition 1.12:

Proposition 2.2. Let $\left(N^{n}, g_{b}\right)$ be an $A L E$ Ricci-flat metric asymptotic to $\mathbb{R}^{n} / \Gamma$, for some finite subgroup $\Gamma$ of $S O(n)$ acting freely on $\mathbb{S}^{n-1}$. Let $\tau \in\left(\frac{n-2}{2}, n-2\right)$ and $\alpha \in(0,1)$.

Then there exists some positive $\varepsilon$ such that $g \in B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right) \rightarrow f_{g} \in C_{\tau}^{2, \alpha}(N)$ is analytic and satisfies on $N$,
$$2 \Delta_{g} f_{g}-\left|\nabla^{g} f_{g}\right|_{g}^{2}+\mathrm{R}_{g}=0 .$$
Moreover, the asymptotic expansion holds true for $g \in \mathcal{M}_{\tau}^{2, \alpha}\left(g_{b}, \varepsilon\right)$,
$$f_{g}=\frac{\lambda_{\mathrm{ALE}}^{0}(g)|\Gamma|}{2(n-2) \operatorname{Vol} \mathbb{S}^{n-1}} \frac{1}{\rho_{g_{b}}^{n-2}}+O\left(\rho_{g_{b}}^{-n+2-\gamma}\right),$$
for some positive real number $\gamma$.

Finally, if $g \in \mathcal{M}_{\tau}^{2, \alpha}\left(g_{b}, \varepsilon\right)$,
$$\begin{aligned}
\lambda_{\mathrm{ALE}}^{0}(g) & =\int_{N}\left(\left|\nabla^{g} f_{g}\right|_{g}^{2}+\mathrm{R}_{g}\right) e^{-f_{g}} d \mu_{g} \\
& =2 \int_{N}\left(\left|\nabla^{g} f_{g}\right|_{g}^{2}-\Delta_{g} f_{g}\right) e^{-f_{g}} d \mu_{g} \\
& =-\lim _{R \rightarrow \infty} 2 \int_{\left\{\rho_{g_{b}}=R\right\}}\left\langle\nabla^{g} f_{g}, \mathbf{n}_{g_{b}}\right\rangle d \sigma_{g}
\end{aligned}$$

Before stating the first variation of $\mathcal{F}_{\mathrm{ALE}}$ for arbitrary variations, we introduce several notions associated to a smooth metric measure space $\left(N^{n}, g, \nabla^{g} f\right)$ where $f$ is a given $C_{\text {loc }}^{1}$ function on $N$. The weighted laplacian of a tensor $T$ on $N$ denoted by $\Delta_{f} T$ is defined by:
$$\Delta_{f} T:=\Delta_{g} T-\nabla_{\nabla^{g} f}^{g} T,$$
where $\Delta_{g}$ denotes the rough Laplacian associated to the Riemannian metric $g$.
The weighted divergence of a $C_{\text {loc }}^{1}$ vector field $X$ on $N$ is defined by:
$$\operatorname{div}_{f} X:=\Delta_{g} X-g\left(\nabla^{g} f, X\right) .$$
Finally, the weighted divergence of a $C_{\text {loc }}^{1}$ symmetric 2-tensor $T$ on $N$ is defined by:
$$\operatorname{div}_{f} T:=\operatorname{div}_{g} T-T\left(\nabla^{g} f\right) .$$

Proposition 2.3 (First variation of $\mathcal{F}_{\mathrm{ALE}}$ ). Let ( $N^{n}, g_{b}$ ) be an ALE Ricci-flat metric asymptotic to $\mathbb{R}^{n} / \Gamma$, for some finite subgroup $\Gamma$ of $S O(n)$ acting freely on $\mathbb{S}^{n-1}$. Let $\tau \in\left(\frac{n-2}{2}, n-2\right)$ and $\alpha \in(0,1)$.

The first variation of $\mathcal{F}_{\mathrm{ALE}}$ at a couple $(g, f) \in \mathcal{M}_{\tau}^{2, \alpha}\left(g_{b}, \varepsilon\right) \times C_{\tau}^{2}(N)$ along directions $(h, \varphi) \in C_{\tau}^{2}\left(S^{2} T^{*} N\right) \times C_{\tau}^{2}(N)$ such that $g+h \in \mathcal{M}_{\tau}^{2, \alpha}\left(g_{b}, \varepsilon\right)$ is
$$\begin{aligned}
\delta_{g, f} \mathcal{F}_{\mathrm{ALE}}(h, \varphi) & =-\int_{N}\left\langle h, \operatorname{Ric}(g)+\nabla^{g, 2} f\right\rangle_{g} e^{-f} d \mu_{g} \\
& +\int_{N}\left(2 \Delta_{g} f-\left|\nabla^{g} f\right|_{g}^{2}+\mathrm{R}_{g}\right)\left(\frac{\operatorname{tr}_{g} h}{2}-\varphi\right) e^{-f} d \mu_{g}+m_{\mathrm{ADM}}\left(g_{b}+h\right),
\end{aligned}$$
where $m_{\mathrm{ADM}}\left(g_{b}+h\right)$ is the mass of the metric $g_{b}+h$ defined in (1.4).
Finally, the first variation of $\lambda_{\text {ALE }}^{0}$ on a neighborhood of $\mathcal{M}_{\tau}^{2, \alpha}\left(g_{b}, \varepsilon\right)$ is:
$$\delta_{g} \lambda_{\mathrm{ALE}}^{0}(h)=-\int_{N}\left\langle h, \operatorname{Ric}(g)+\nabla^{g, 2} f_{g}\right\rangle_{g} e^{-f_{g}} d \mu_{g}+m_{\mathrm{ADM}}\left(g_{b}+h\right) .$$

Remark 2.4. Notice that (2.8) gives a link between the variation of the functional $\lambda_{\mathrm{ALE}}^{0}$, the mass of an ALE metric with integrable scalar curvature and its associated Bakry-Émery tensor.

Proof. We follow [Chapter 2, [CLN06]] closely by using (C.7) from Lemma C.2:
$$\begin{aligned}
\delta_{g, f}\left[\left(\left|\nabla^{g} f\right|_{g}^{2}+\mathrm{R}_{g}\right)\right. & \left.e^{-f} d \mu_{g}\right](h, \varphi) \\
= & \left(\operatorname{div}_{g}\left(\operatorname{div}_{g} h\right)-\Delta_{g} \operatorname{tr}_{g} h-\langle h, \operatorname{Ric}(g)\rangle-h\left(\nabla^{g} f, \nabla^{g} f\right)\right) e^{-f} d \mu_{g} \\
& +\left(2\left\langle\nabla^{g} f, \nabla^{g} \varphi\right\rangle+\left(\operatorname{R}_{g}+\left|\nabla^{g} f\right|_{g}^{2}\right)\left(\frac{\operatorname{tr}_{g} h}{2}-\varphi\right)\right) e^{-f} d \mu_{g} .
\end{aligned}$$

Now, by integrating by parts twice on the domain $\left\{\rho_{g_{b}} \leq R\right\}$ with $R$ sufficiently large such that $\left\{\rho_{g_{b}}=R\right\}$ is a smooth compact hypersurface:
$$\begin{aligned}
\int_{\left\{\rho_{g_{b}} \leq R\right\}} \operatorname{div}_{g}\left(\operatorname{div}_{g} h\right) e^{-f} d \mu_{g}= & \int_{\left\{\rho_{g_{b}} \leq R\right\}}\left(h\left(\nabla^{g} f, \nabla^{g} f\right)-\left\langle h, \nabla^{g, 2} f\right\rangle\right) e^{-f} d \mu_{g} \\
& +\int_{\left\{\rho_{g_{b}}=R\right\}}\left\langle\operatorname{div}_{g} h+h\left(\nabla^{g} f\right), \mathbf{n}_{g_{b}}\right\rangle e^{-f} d \sigma_{g}
\end{aligned}$$
Moreover,
$$\begin{aligned}
-\int_{\left\{\rho_{g_{b}} \leq R\right\}} \Delta_{g} \operatorname{tr}_{g} h e^{-f} d \mu_{g}= & -\int_{\left\{\rho_{g_{b}} \leq R\right\}}\left\langle\nabla^{g} \operatorname{tr}_{g} h, \nabla^{g} f\right\rangle e^{-f} d \mu_{g} \\
& -\int_{\left\{\rho_{g_{b}}=R\right\}}\left\langle\nabla^{g} \operatorname{tr}_{g} h, \mathbf{n}_{g_{b}}\right\rangle e^{-f} d \sigma_{g} \\
= & \int_{\left\{\rho_{g_{b}} \leq R\right\}}\left(\Delta_{g} f-\left|\nabla^{g} f\right|_{g}^{2}\right) \operatorname{tr}_{g} h e^{-f} d \mu_{g} \\
& -\int_{\left\{\rho_{g_{b}}=R\right\}}\left\langle\nabla^{g} \operatorname{tr}_{g} h, \mathbf{n}_{g_{b}}\right\rangle e^{-f} d \sigma_{g} \\
& -\int_{\left\{\rho_{g_{b}}=R\right\}} \operatorname{tr}_{g} h\left\langle\nabla^{g} f, \mathbf{n}_{g_{b}}\right\rangle e^{-f} d \sigma_{g}, \\
2 \int_{\left\{\rho_{g_{b}} \leq R\right\}}\left\langle\nabla^{g} f, \nabla^{g} \varphi\right\rangle e^{-f} d \mu_{g}= & -2 \int_{\left\{\rho_{g_{b}} \leq R\right\}}\left(\Delta_{g} f-\left|\nabla^{g} f\right|_{g}^{2}\right) \varphi e^{-f} d \mu_{g} \\
& +2 \int_{\left\{\rho_{g_{b}}=R\right\}} \varphi\left\langle\nabla^{g} f, \mathbf{n}_{g_{b}}\right\rangle e^{-f} d \sigma_{g} .
\end{aligned}$$
Therefore the expected result follows by summing the previous equalities and let $R$ go to $+\infty$ by using the asymptotics assumed on $h, f$ and $\varphi$ together with the definition of the mass of $g_{b}+h$ given in (1.4).

In order to compute the first variation of $\lambda_{\text {ALE }}^{0}$, one proceeds similarly by setting $\varphi:=\delta_{g} f(h)$ and by using (2.1) to cancel the second integral term on the righthand side of (2.7). By density of $C_{c}^{\infty}$ in $L_{\frac{n}{2}-1}^{2}$, notice that (2.8) still holds true for variations $h \in L_{\frac{n}{2}-1}^{2}$ since $\operatorname{Ric}(g)+\nabla^{g, 2} f_{g}=O\left(\rho_{g_{b}}^{-\tau-2}\right) \in L_{\frac{n}{2}+1}^{2}$. \(\square\)

As a first consequence of Proposition 2.3, we recover (in our non-compact setting) the fact stated in [Remark 4.6, [Has12]] that the weighted $L^{2}$-norm of the Bakry-Émery tensor $\operatorname{Ric}(g)+\nabla^{g, 2} f_{g}$ associated to the functional $\lambda_{\text {ALE }}^{0}$ is dominated by that of the Ricci curvature. More precisely, we have the following result:

Corollary 2.5. Let $\left(N^{n}, g_{b}\right)$ be an $A L E$ Ricci-flat metric asymptotic to $\mathbb{R}^{n} / \Gamma$, for some finite subgroup $\Gamma$ of $S O(n)$ acting freely on $\mathbb{S}^{n-1}$. Let $\tau \in\left(\frac{n-2}{2}, n-2\right)$ and $\alpha \in(0,1)$.

Then there exists $\varepsilon>0$ such that if $g \in B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right)$, the tensor $\operatorname{Ric}(g)+\nabla^{g, 2} f_{g}$ is weighted divergence-free, i.e.
$$\operatorname{div}_{f_{g}}\left(\operatorname{Ric}(g)+\nabla^{g, 2} f_{g}\right)=0 .$$

In particular, if $g \in B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right)$,
$$\left\|\operatorname{Ric}(g)+\nabla^{g, 2} f_{g}\right\|_{L^{2}\left(e^{-f_{g}} d \mu_{g}\right)} \leq\|\operatorname{Ric}(g)\|_{L^{2}\left(e^{-f_{g}} d \mu_{g}\right)} .$$

Notice that the quantitative version of the reverse inequality of (2.10) is more delicate to prove in general: see [Has12, Theorem C] for closed Ricci-flat metrics in the integrable case.

Proof. Let us prove that $\operatorname{Ric}(g)+\nabla^{g, 2} f_{g}$ is divergence-free in the (weighted) sense of (2.6):
$$\begin{aligned}
2 \operatorname{div}_{f_{g}}\left(\operatorname{Ric}(g)+\nabla^{g, 2} f_{g}\right) & =2 \operatorname{div}_{g}\left(\operatorname{Ric}(g)+\nabla^{g, 2} f_{g}\right)-2\left(\operatorname{Ric}(g)+\nabla^{g, 2} f_{g}\right)\left(\nabla^{g} f_{g}\right) \\
& =\nabla^{g} \operatorname{R}_{g}+\operatorname{div}_{g} \mathscr{L}_{\nabla^{g} f_{g}}(g)-2\left(\operatorname{Ric}(g)+\nabla^{g, 2} f_{g}\right)\left(\nabla^{g} f_{g}\right) \\
& =\nabla^{g} \operatorname{R}_{g}+\frac{1}{2} \nabla^{g} \operatorname{tr}_{g} \mathscr{L}^{g} f_{g}(g)+\Delta_{g} \nabla^{g} f_{g}+\operatorname{Ric}(g)\left(\nabla^{g} f_{g}\right) \\
& -2\left(\operatorname{Ric}(g)+\nabla^{g, 2} f_{g}\right)\left(\nabla^{g} f_{g}\right) \\
& =\nabla^{g}\left(\mathrm{R}_{g}+2 \Delta_{g} f_{g}-\left|\nabla^{g} f_{g}\right|_{g}^{2}\right) \\
& =0 .
\end{aligned}$$
Here, we have used the Bianchi identity (its traced version) in the second line together with the Bochner formula for vector fields in the third line and the one for functions in the fourth line. The last line comes from [(2.1), Proposition 2.2].

The proof of (2.10) is essentially due to (2.9). Indeed, if $X$ is any smooth vector field which is compactly supported (or decaying faster than $\rho_{g_{b}}^{-\frac{n}{2}+2}$ ) on $N$, then
$$\left\langle\operatorname{Ric}(g)+\nabla^{g, 2} f_{g}, \mathscr{L}_{X}(g)\right\rangle_{L^{2}\left(e^{-f_{g}} d \mu_{g}\right)}=0,$$
by integration by parts. In particular, by applying this fact to $X=\nabla^{g} f_{g}=O\left(\rho_{g_{b}}^{-\tau-1}\right)$ by Proposition 2.2, one gets,
$$\begin{aligned}
\left\|\operatorname{Ric}(g)+\nabla^{g, 2} f_{g}\right\|_{L^{2}\left(e^{-f_{g}} d \mu_{g}\right)}^{2}= & \|\operatorname{Ric}(g)\|_{L^{2}\left(e^{-f_{g}} d \mu_{g}\right)}^{2}+2\left\langle\operatorname{Ric}(g), \nabla^{g, 2} f_{g}\right\rangle_{L^{2}\left(e^{-f_{g}} d \mu_{g}\right)} \\
& +\left\|\nabla^{g, 2} f_{g}\right\|_{L^{2}\left(e^{-f_{g}} d \mu_{g}\right)}^{2} \\
= & \|\operatorname{Ric}(g)\|_{L^{2}\left(e^{-f_{g}} d \mu_{g}\right)}^{2}+2\left\langle\operatorname{Ric}(g)+\nabla^{g, 2} f_{g}, \nabla^{g, 2} f_{g}\right\rangle_{L^{2}\left(e^{-f_{g}} d \mu_{g}\right)} \\
& -\left\|\nabla^{g, 2} f_{g}\right\|_{L^{2}\left(e^{-f_{g}} d \mu_{g}\right)}^{2}\left\|\nabla^{g, 2} f_{g}\right\|_{L^{2}\left(e^{-f_{g}} d \mu_{g}\right)}^{2} \\
= & \|\operatorname{Ric}(g)\|_{L^{2}\left(e^{-f_{g}} d \mu_{g}\right)}^{2}-\|\operatorname{Ric}(g)\|_{L^{2}\left(e^{-f_{g}} d \mu_{g}\right)}^{2} .
\end{aligned}$$
All the integrals and integration by parts are justified here by the sufficiently fast decays at infinity satisfied by $\operatorname{Ric}(g)$ and $f_{g}$ and their covariant derivatives. \(\square\)

We are in a good position to compute the second variation of $\lambda_{\text {ALE }}^{0}$. We first need one more definition:

Definition 2.6. Let $\left(N^{n}, g\right)$ be a Riemannian metric. Then the Lichnerowicz operator associated to $g$ acting on symmetric 2-tensors, denoted by $L_{g}$, is defined by:
$$L_{g} h:=\Delta_{g} h+2 \operatorname{Rm}(g)(h)-\operatorname{Ric}(g) \circ h-h \circ \operatorname{Ric}(g), \quad h \in C_{\text {loc }}^{2}\left(S^{2} T^{*} N\right),$$
where $\Delta_{g}=-\nabla^{*} \nabla$ and where $\operatorname{Rm}(g)(h)(X, Y):=h\left(\operatorname{Rm}(g)\left(e_{i}, X\right) Y, e_{i}\right)$ for an orthonormal basis $\left(e_{i}\right)_{i=1}^{n}$ with respect to $g$. In particular, if ( $N^{n}, g$ ) is a Ricci-flat metric, then,
$$L_{g} h:=\Delta_{g} h+2 \operatorname{Rm}(g)(h), \quad h \in C_{\text {loc }}^{2}\left(S^{2} T^{*} N\right) .$$

With this definition in hand, we are able to identify the second variation of $\lambda_{\text {ALE }}^{0}$ at an ALE Ricci-flat metric as follows.

Proposition 2.7 (Second variation of $\lambda_{\text {ALE }}^{0}$ at a Ricci-flat metric). Let $\left(N^{n}, g_{b}\right)$ be an $A L E$ Ricci-flat metric asymptotic to $\mathbb{R}^{n} / \Gamma$, for some finite subgroup $\Gamma$ of $S O(n)$ acting freely on $\mathbb{S}^{n-1}$. Let $\tau \in\left(\frac{n-2}{2}, n-2\right)$ and $\alpha \in(0,1)$. Then the second variation of $\lambda_{\text {ALE }}^{0}$ at $g_{b}$ along a divergence-free variation $h \in S^{2} T^{*} N$ such that $g_{b}+h \in \mathcal{M}_{\tau}^{2, \alpha}\left(g_{b}, \varepsilon\right)$ is:
$$\delta_{g_{b}}^{2} \lambda_{\mathrm{ALE}}^{0}(h, h)=\frac{1}{2}\left\langle L_{g_{b}} h, h\right\rangle_{L^{2}} .$$
Proof. Recall by Lemma C. 2 that, if we denote the Bianchi operator $B_{g}(h):=\operatorname{div}_{g}(h-$ $\left.\frac{1}{2}\left(\operatorname{tr}_{g} h\right) g\right)$, we have
$$\begin{aligned}
\delta_{g_{b}}(-2 \text { Ric })(h) & =L_{g_{b}} h-\mathscr{L}_{B_{g_{b}}(h)}\left(g_{b}\right) \\
& =L_{g_{b}} h+\frac{1}{2} \mathscr{L}_{\nabla^{g_{b}} \operatorname{tr}_{g_{b}} h}\left(g_{b}\right),
\end{aligned}$$
if $\operatorname{div}_{g_{b}} h=0$. Since $f_{g_{b}}=0$ then, denoting $\delta_{g_{b}} f(h)$ the first order variation of $g \mapsto f_{g}$ at $g_{b}$ in the direction $h$, we have:
$$\delta_{g_{b}} \mathscr{L}_{\nabla^{g} f_{g}}(h)=\mathscr{L}_{\nabla^{g_{b}} \delta_{g_{b}} f(h)}\left(g_{b}\right) .$$
Therefore, according to Proposition 2.3,
$$2 \delta_{g_{b}}^{2} \lambda_{\mathrm{ALE}}^{0}(h, h)=\left\langle L_{g_{b}} h, h\right\rangle_{L^{2}}+\frac{1}{2}\left\langle\mathscr{L}_{\nabla^{g_{b}} \operatorname{tr}_{g_{b}} h}\left(g_{b}\right), h\right\rangle_{L^{2}}-\left\langle\mathscr{L}_{\nabla^{g_{b}}\left(\delta_{g_{b}} f(h)\right)}\left(g_{b}\right), h\right\rangle_{L^{2}} .$$
By integrating by parts:
$$\begin{aligned}
2 \delta_{g_{b}}^{2} \lambda_{\mathrm{ALE}}^{0}(h, h) & =\left\langle L_{g_{b}} h, h\right\rangle_{L^{2}}-\left\langle\nabla^{g_{b}} \operatorname{tr}_{g_{b}} h, \operatorname{div}_{g_{b}} h\right\rangle_{L^{2}}+2\left\langle\delta_{g_{b}} f(h), \operatorname{div}_{g_{b}} h\right\rangle_{L^{2}} \\
& =\left\langle L_{g_{b}} h, h\right\rangle_{L^{2}},
\end{aligned}$$
if $\operatorname{div}_{g_{b}} h=0$. \(\square\)

Remark 2.8. Notice that if $h$ is a symmetric 2-tensor $h$ on $N$ then by differentiating (2.1) at $g_{b}$ gives:
$$2 \Delta_{g_{b}}\left(\delta_{g_{b}} f_{g}(h)-\frac{\operatorname{tr}_{g_{b}} h}{2}\right)=-\operatorname{div}_{g_{b}}\left(\operatorname{div}_{g_{b}} h\right) .$$
Now, if $\operatorname{div}_{g_{b}} h=0$ then the function $\delta_{g_{b}} f_{g}(h)-\frac{\operatorname{tr}_{g_{b}} h}{2}$ is a harmonic function on $N$. In the setting of Proposition 2.7, the maximum principle applied to the previous function shows that it vanishes identically, i.e. the pointwise volume $e^{-f_{g}} d \mu_{g}$ is preserved under such a variation. On the other hand, if $B_{g_{b}}(h)=0$ then one gets by (2.16) that $\delta_{g_{b}} f_{g}(h)-\frac{\operatorname{tr}_{g_{b}} h}{4}=0$. This implies that the second variation of $\lambda_{\text {ALE }}^{0}$ at $g_{b}$ along $h \in B_{g_{b}}^{-1}(0)$ satisfies:
$$2 \delta_{g_{b}}^{2} \lambda_{\mathrm{ALE}}^{0}(h, h)=\left\langle L_{g_{b}} h, h\right\rangle_{L^{2}}+\frac{1}{2}\left\|\nabla^{g_{b}} \operatorname{tr}_{g_{b}} h\right\|_{L^{2}}^{2} .$$

This leaves us with a less tractable formula for the second derivative of $\lambda_{\mathrm{ALE}}^{0} \cdot$

\section*{3. A functional defined on a $C_{\tau}^{2, \alpha}$-neighborhood of Ricci-flat ALE metrics}
3.1. First and second variations of $\lambda_{\text {ALE }}$.

Let $\left(N^{n}, g_{b}\right)$ be an ALE Ricci-flat metric. We first recall that there exists a sequence of metrics $C_{\tau}^{2, \alpha}$-converging to $g_{b}$ while having unbounded mass and $\lambda_{\text {ALE }}^{0}$-functional.

Example 3.1. Denote for $A>0$ large enough, $\chi_{A}$ a cut-off function supported in $\left\{\rho_{g_{b}}>A\right\}$ where $g_{b}$ has ALE coordinates, and constant equal to 1 on $\left\{\rho_{g_{b}}>2 A\right\}$ and assume that for $c>0$ uniform and all $k \in\{1,2,3\}$, its $k$-th derivative is bounded by $c A^{-k}$. Let us define the metric
$$g_{A, m}:=\left(1+\chi_{A} \frac{m}{\rho_{g_{b}}^{n-2}}\right)^{\frac{4}{n-2}} g_{b},$$
whose scalar curvature vanishes on $\left\{\rho_{g_{b}}>2 A\right\}$ by the usual variation of the scalar curvature for conformal changes of metric.

Then, for some constant $C>0$ we have
$$\left\|g_{A, m}-g_{e}\right\|_{C_{\tau}^{2, \alpha}} \leq C|m| A^{\tau-(n-2)}$$
and for some $c_{n}>0$, we have $m_{\mathrm{ADM}}\left(g_{A, m}\right)=c_{n} m$. As a consequence, by choosing $m \rightarrow \pm \infty$ while $|m| A^{\tau-(n-2)} \rightarrow 0$, we get a sequence of metrics $C_{\tau}^{2, \alpha}$-converging to $g_{b}$ while its mass tends to $\pm \infty$.

The computation of the first variation of $\lambda_{\text {ALE }}^{0}$ in Proposition 2.3 motivates the study of the difference $\lambda_{\text {ALE }}^{0}-m_{\text {ADM }}$.

Definition 3.2 ( $\lambda_{\text {ALE }}$, a renormalized Perelman's functional). Let ( $N^{n}, g_{b}$ ) be an ALE Ricciflat metric and let $g \in \mathcal{M}_{\tau}^{2, \alpha}\left(g_{b}, \varepsilon\right)$ for $\tau>\frac{n-2}{2}$. We define
$$\lambda_{\mathrm{ALE}}(g):=\lambda_{\mathrm{ALE}}^{0}(g)-m_{\mathrm{ADM}}(g) .$$

Remark 3.3. This is reminiscent of the introduction of the mass in General Relativity in order to replace the Hilbert-Einstein functional $\int_{N} \mathrm{R}_{g} d \mu_{g}$ by $\int_{N} \mathrm{R}_{g} d \mu_{g}-m_{\mathrm{ADM}}(g)$ which is better-behaved in the setting of Asymptotically Euclidean metrics. Our functional $\lambda_{\text {ALE }}$ is moreover an approximation up to third order:
$$\int_{N} \mathrm{R}_{g_{b}+h} d \mu_{g_{b}+h}-m_{\mathrm{ADM}}\left(g_{b}+h\right)-\lambda_{\mathrm{ALE}}\left(g_{b}+h\right)=O\left(\|h\|_{C_{\tau}^{2, \alpha}}^{3}\right) .$$

Notice that Definition 3.2 only makes sense for metrics lying in $\mathcal{M}_{\tau}^{2, \alpha}\left(g_{b}, \varepsilon\right)$ a priori. The following proposition ensures the functional $\lambda_{\text {ALE }}$ is well-defined on a whole neighborhood of a given Ricci-flat ALE metric in the $C_{\tau}^{2, \alpha}$-topology.

Proposition 3.4. Let $\left(N^{n}, g_{b}\right)$ be an $A L E$ Ricci-flat metric asymptotic to $\mathbb{R}^{n} / \Gamma$, for some finite subgroup $\Gamma$ of $S O(n)$ acting freely on $\mathbb{S}^{n-1}$. Let $\tau \in\left(\frac{n-2}{2}, n-2\right)$ and $\alpha \in(0,1)$. Then, the functional $\lambda_{\text {ALE }}$, initially defined on $\mathcal{M}_{\tau}^{2, \alpha}\left(g_{b}, \varepsilon\right)$, extends to a $C_{\tau}^{2, \alpha}$-neighborhood of $g_{b}$ as an analytic functional
\begin{itemize}
\item[-] whose $L^{2}\left(e^{-f_{g}} d \mu_{g}\right)$-gradient at $g$ is $-\left(\operatorname{Ric}(g)+\nabla^{g, 2} f_{g}\right)$,
\item[-] and whose second variation at $g_{b}$ for divergence-free 2-tensors is $\frac{1}{2} L_{g_{b}}$.
\end{itemize}

Moreover, if $g \in B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right)$,
$$\begin{aligned}
\lambda_{\mathrm{ALE}}(g)=\lim _{R \rightarrow+\infty}\left(\int_{\left\{\rho_{g_{b}} \leq R\right\}}\right. & \left(\left|\nabla^{g} f_{g}\right|_{g}^{2}+\mathrm{R}_{g}\right) e^{-f_{g}} d \mu_{g} \\
& \left.-\int_{\left\{\rho_{g_{b}}=R\right\}}\left\langle\operatorname{div}_{g_{b}}(g)-\nabla^{g_{b}} \operatorname{tr}_{g_{b}}(g), \mathbf{n}_{g_{b}}\right\rangle_{g_{b}} d \sigma_{g_{b}}\right) .
\end{aligned}$$
Finally, the functional $\lambda_{\text {ALE }}$ is kept unchanged on $C_{\tau^{\prime}}^{2, \alpha^{\prime}}$-neighborhoods of $g_{b}$ for $\tau^{\prime} \in\left(\frac{n-2}{2}, \tau\right]$ and $\alpha^{\prime} \in(0, \alpha]$.

Before proving Proposition 3.4, we make a couple of remarks.
Remark 3.5. The largest definition space seems to be $h \in H_{\frac{n}{2}-1}^{2}$ where the first derivative $\left\langle h, \operatorname{Ric}_{g}+\nabla^{g, 2} f_{g}\right\rangle_{L^{2}\left(e^{-f_{g}} d \mu_{g}\right)}$ is well defined for $g-g_{b} \in H_{\frac{n}{2}-1}^{2}$. The second derivative $\frac{1}{2}\left\langle h, L_{g_{b}} h\right\rangle_{L^{2}\left(e^{-f_{g}} d \mu_{g}\right)}$ is also well defined for 2-tensors in $H_{\frac{n}{2}-1}^{2}$. However, it is not clear if the definition of the mass $m_{\mathrm{ADM}}$ is invariant by changes of coordinates under these assumptions.

Remark 3.6. As already noticed in the Introduction, $\lambda_{\text {ALE }}(g)$ is the limit of the difference of two integrals which could be divergent in general. However, if $g \in B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right)$ is such that its scalar curvature is integrable, then $\lambda_{\text {ALE }}(g)$ really is the difference of $\lambda_{\text {ALE }}^{0}(g)$ with the mass $m_{\text {ADM }}(g)$.
Proof of Proposition 3.4. Let us consider a small $h$ in $C_{\tau}^{2, \alpha}$ for $\tau>\frac{n-2}{2}$ such that $g_{b}+h$ is a metric on $N$. Thanks to [(C.7), Lemma C.2], we have
$$\begin{aligned}
\mathrm{R}_{g_{b}+h}= & \int_{0}^{1} \operatorname{div}_{g_{b}+t h}\left(\operatorname{div}_{g_{b}+t h} h-\nabla^{g_{b}+t h} \operatorname{tr}_{g_{b}+t h} h\right) d t \\
= & \operatorname{div}_{g_{b}}\left(\operatorname{div}_{g_{b}} h-\nabla^{g_{b}} \operatorname{tr}_{g_{b}} h\right) \\
& +\int_{0}^{1}\left[\left(\operatorname{div}_{g_{b}+t h}\left(\operatorname{div}_{g_{b}+t h}-\nabla^{g_{b}+t h} \operatorname{tr}_{g_{b}+t h}\right)\right)-\left(\operatorname{div}_{g_{b}}\left(\operatorname{div}_{g_{b}}-\nabla^{g_{b}} \operatorname{tr}_{g_{b}}\right)\right)\right](h) d t \\
= & : \operatorname{div}_{g_{b}}\left(\operatorname{div}_{g_{b}} h-\nabla^{g_{b}} \operatorname{tr}_{g_{b}} h\right)+Q_{g_{b}}(h),
\end{aligned}$$
where $Q_{g_{b}}: C_{\tau}^{2, \alpha} \rightarrow \mathbb{R}$ is analytic and satisfies for some positive constant $C$, for any two symmetric 2-tensors $h$ and $h^{\prime}$,
$$\left\|Q_{g_{b}}(h)-Q_{g_{b}}(h)\right\|_{C_{2 \tau+2}^{0, \alpha}} \leq C\left\|h-h^{\prime}\right\|_{C_{\tau}^{2, \alpha}}\left(\|h\|_{C_{\tau}^{2, \alpha}}+\left\|h^{\prime}\right\|_{C_{\tau}^{2, \alpha}}\right) .$$

For a symmetric 2-tensor $h \in B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right)$, denote $v_{g_{b}+h} \in C_{\tau}^{2, \alpha}$ to be the unique solution to
$$-4 \Delta_{g_{b}+h} v_{g_{b}+h}+\mathrm{R}_{g_{b}+h} v_{g_{b}+h}=-\mathrm{R}_{g_{b}+h}=-\operatorname{div}_{g_{b}}\left(\operatorname{div}_{g_{b}} h-\nabla^{g_{b}} \operatorname{tr}_{g_{b}} h\right)-Q_{g_{b}}(h) \in C_{\tau+2}^{0, \alpha} .$$
Its existence is ensured because $-4 \Delta_{g_{b}+h}+\mathrm{R}_{g_{b}+h}: C_{\tau}^{2, \alpha} \rightarrow C_{\tau+2}^{0, \alpha}$ is invertible: indeed, we are in the invertibility range $0<\tau<n-2$ of the Laplacian as already noticed in Claim 1.

We have already seen in (the proof of) Proposition 1.12 by integration by parts against $1+v_{g_{b}+h}$ that we actually have
$$\lambda_{\mathrm{ALE}}^{0}\left(g_{b}+h\right)=\int_{N}\left(1+v_{g_{b}+h}\right) \mathrm{R}_{g_{b}+h} d \mu_{g_{b}+h}$$
if $g_{b}+h \in \mathcal{M}^{2, \alpha}\left(g_{b}, \varepsilon\right)$.