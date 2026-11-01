---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: On the completeness of some Bianchi type A and related Kähler-Einstein metrics]

---
source_file: 2007_06471.pdf
converter: mathpix
format: mmd
---

\title{
ON THE COMPLETENESS OF SOME BIANCHI TYPE A AND RELATED KÄHLER-EINSTEIN METRICS
}

\author{
GIDEON MASCHLER AND ROBERT REAM
}

\begin{abstract}
We prove the existence of complete cohomogeneity one triaxial Kähler-Einstein metrics in dimension four under an action of the Euclidean group $E(2)$. We also demonstrate local existence of Ricci flat Kähler metrics of a related type that are given via generalized PDEs, and determine, under mild conditions, whether they are complete. The common framework for both metric types is a frame-dependent system of Lie bracket relations and generalized PDEs yielding a class of Kähler-Einstein metrics on 4-manifolds which includes all diagonal Bianchi type A metrics.
\end{abstract}

\section*{1. Introduction}

The study of complete curvature-distinguished metrics which are invariant under a cohomogeneity one group action have seen significant progress in recent decades, cf. [DW1], [DW2], [B], [BDW], [DHW], [W]. Much of this research centers on the case of compact groups. A significant portion of this paper concerns non-compact groups. See [L] for other work involving non-compact groups.

The class of examples we study includes four-dimensional unimodular cohomogeneity one Kähler-Einstein metrics, otherwise known as Bianchi type A Kähler-Einstein metrics. This class of metrics has been studied by mathematicians and physicists, see [BGPP], [Pd], [DS1], [DS2].

In the last two references, Dancer and Strachan prove that when the cohomogeneity one action is under the group $S U(2)$, there exist so-called triaxial complete cohomogeneity one Kähler-Einstein metrics. No similar results appear to be known for non-compact unimodular groups. In one of the main results given in the second part of this paper, we demonstrate the existence of complete triaxial cohomogeneity one Kähler-Einstein metrics under the action of the Euclidean plane group $E(2)$.

Theorem A. A cohomogeneity one E(2) 4-manifold with a discrete principal stabilizer admits complete Kähler-Einstein metrics, and all such solutions are classified.

See Theorem 3 for a precise statement. One part of the proof proceeds along similar lines to those in [DS1] for $S U(2)$. Another part is systematized via recent results of Verdiani and Ziller [VZ]. The final completeness argument involves Cauchy-Schwarz type estimates, a method that has been employed recently in [AM2] to prove completeness in the simpler case of biaxial metrics for a quotient of the Heisenberg group.

In the first part of this work, which is more foundational, we give a framework for the study of the existence problem for a class of Kähler-Einstein metrics in dimension four that includes the diagonal Bianchi type A class. Our framework is inspired by the references [AM1], [AM2], but does not share their Lorentzian geometric motivation.

Concretely, we describe a class of Kähler metrics via a set of Lie bracket relations on a given local frame, and impose the Kähler-Einstein condition as a set of generalized PDEs involving directional derivatives in the frame directions. See [AM2] for a precise definition of a generalized PDE.

For the case where the Einstein constant is nonzero, we show that the resulting system gives rise locally to a system of ODEs. The Bianchi type A metrics form examples for this case. On the other hand, in one of the Ricci flat subcases, an analogous process yields a small number of generalized PDEs with directional derivatives along a two-dimensional distribution.

These two derivations appear in the appendix, and in the rest of the paper we investigate each of these two cases. We have already mentioned the completeness result pertaining to the first case. For the Ricci flat subcase, there are additional well-known incomplete cohomogeneity one examples, but the fact that this case is characterized by PDEs rather than ODEs raises the question of whether there are additional examples. We show that there are no complete examples of a certain type, but prove local existence of additional solutions.

Theorem B. There exists a Kähler Ricci-flat metric $g$ on an open neighborhood of $\mathbb{R}^{4}$ admitting a totally-geodesic two-dimensional foliation whose leaves are isometric to a given model leaf-metric. The dimension of the Lie algebra of Killing fields of $g$ is at least 2.

See Theorem 5 for a precise statement.
Our method in the Ricci flat subcase is as follows. First, such a metric must possess a two-dimensional totally geodesic foliation. Aided by a theorem due to Yau [Y], we show that if the leaves are finitely connected and the leaf metric is not flat, it cannot be complete or even possess a completion obtained by adjoining one point to the leaf. This automatically proves incompleteness of the Kähler metric with a foliation of this type. We then show by an explicit construction that in dimension two, there exist metrics which possess the same properties as a leaf metric must have. The main such property is that the metric has positive Gauss curvature which, when used as a conformal factor, yields a metric with Gauss curvature -2. Then we show that using these leaf-like metrics as local data, constructing the Ricci-flat Kähler metric locally amounts to a collection of decoupled PDE problems, which are handled by elementary means.

Returning to our framework, the presentation of the problem in terms of a frame with Lie bracket relations can be considered dual to one given in terms of an exterior differential system (EDS). We note that a proof of the reduction of the problem in the non-Ricci-flat case to an ODE system via EDS methods would involve four prolongations to reach involutivity.

As a means for simplifying standard EDS methods for the purpose of constructing solutions, this reduction procedure is not particularly remarkable. But we find it greatly aids in maintaining geometric intuition for the problem. For example, one byproduct in the Kähler case is that integrability of the complex structure has a particularly appealing form in terms of conditions on the shears of the frame vector fields. Additionally, it is fairly straightforward to recast geometric problems in this form. In future work we plan to study the case of Ricci solitons for a similar system.

Section 2 contains preliminary material on shear and integrability of complex structures. Sections 3-5 introduce the system for Kähler-Einstein metrics, and Section 6 describes how to construct for it an ODE/PDE system as described above, with the proof in the appendix. In section 7 we specialize to diagonal cohomogeneity one metrics, and consider simple examples in sections 8-9. Section 10 is devoted to the case of the Euclidean group $E(2)$, and culminates in the proof of completeness of the appropriate Kähler-Einstein metrics. Section 11 is devoted to the incompleteness results in the Ricci-flat subcase. In section 12 local existence is shown first for the leaf metrics, and from that for the corresponding Ricci-flat Kähler metrics.

\section*{2. Shear and integrability}

Let $(M, g, J)$ be an almost hermitian 4-manifold. We fix a local oriented orthonormal frame denoted
$$\left\{e_{i}\right\}=\{\mathbf{k}, \mathbf{t}=J \mathbf{k}, \mathbf{x}, \mathbf{y}=J \mathbf{x}\} .$$
In the frame domain, we have an orthogonal decomposition of the tangent bundle:
$$T M=\mathcal{V} \oplus \mathcal{H}, \quad \text { with } \mathcal{V}=\operatorname{span}(\mathbf{k}, \mathbf{t}), \quad \mathcal{H}=\operatorname{span}(\mathbf{x}, \mathbf{y}) .$$
Let $\mathcal{U}$ stand for either $\mathcal{V}$ or $\mathcal{H}$, and $\pi_{\mathcal{U}^{\perp}}: T M \rightarrow \mathcal{U}^{\perp}$ denote the orthogonal projection. For a vector field $X \in \Gamma(\mathcal{U})$, consider the operator $\left.\pi_{\mathcal{U}^{\perp}} \circ \nabla X\right|_{\mathcal{U}^{\perp}}$ : $\Gamma\left(\mathcal{U}^{\perp}\right) \rightarrow \Gamma\left(\mathcal{U}^{\perp}\right)$, where ∇ is the Levi-Civita covariant derivative of $g$. Define the shear operator of $X$ by
$$S_{X}:=\text { trace-free symmetric part of }\left.\pi_{\mathcal{U} \perp} \circ \nabla X\right|_{\mathcal{U}^{\perp}} \text {. }$$
See [AM1] for background on the relation to the shear operator in general relativity.

Our purpose here is to give a condition equivalent to the integrability of $J$ in terms of shear operators.

Theorem 1. Given the above set-up, the almost complex structure $J$ is integrable in the frame domain if and only if
$$\begin{aligned}
\text { i) } & J S_{\mathrm{x}}=S_{\mathrm{y}} \text { on } \mathcal{V} \text {. } \\
\text { ii) } & J S_{\mathrm{k}}=S_{\mathrm{t}} \text { on } \mathcal{H} \text {. }
\end{aligned}$$

The proof is similar to [AM1, Theorem 1], and will be omitted. Its method is to translate the vanishing of the Nijenhuis tensor into the above two conditions.

This relies on the following expression of the matrix corresponding to the shear operator in a local oriented orthonormal frame $\left\{v_{1}, v_{2}\right\}$ on $\mathcal{U}^{\perp}$.
$$\left[S_{X}\right]_{v_{1}, v_{2}}=\left[\begin{array}{cc}
-\sigma_{1} & \sigma_{2} \\
\sigma_{2} & \sigma_{1}
\end{array}\right],$$
with shear coefficients:
$$\begin{aligned}
& 2 \sigma_{1}:=g\left(\left[X, v_{1}\right], v_{1}\right)-g\left(\left[X, v_{2}\right], v_{2}\right), \\
& 2 \sigma_{2}:=-g\left(\left[X, v_{1}\right], v_{2}\right)-g\left(\left[X, v_{2}\right], v_{1}\right) .
\end{aligned}$$

One simple case in which integrability holds by Theorem 1 is when all the shears vanish: $S_{e_{i}}=0, i=1, \ldots, 4$. We refer to this as the shear-free case. Our main results concern cases which are not shear-free.

\section*{3. Shear and Kähler metrics}

Let $(M, g)$ be a Riemannian 4-manifold admitting an orthonormal frame $\left\{e_{i}\right\}=\{\mathbf{k}, \mathbf{t}, \mathbf{x}, \mathbf{y}\}$, defined over an open $U \subset M$, which satisfies the Lie bracket relations
$$\begin{array}{ll}
{[\mathbf{k}, \mathbf{t}]=L(\mathbf{k}+\mathbf{t}),} & {[\mathbf{x}, \mathbf{y}]=N(\mathbf{k}+\mathbf{t}),} \\
{[\mathbf{k}, \mathbf{x}]=A \mathbf{x}+B \mathbf{y},} & {[\mathbf{k}, \mathbf{y}]=C \mathbf{x}+D \mathbf{y},} \\
{[\mathbf{t}, \mathbf{x}]=E \mathbf{x}+F \mathbf{y},} & {[\mathbf{t}, \mathbf{y}]=G \mathbf{x}+H \mathbf{y},}
\end{array}$$
for smooth functions $A, B, C, D, E, F, G, H, L, N$ on $U$ such that
$$\begin{aligned}
& A-D=F+G, \quad B+C=H-E, \\
& N=A+D=-(E+H) .
\end{aligned}$$
Define an almost complex structure $J=J_{g, e_{i}}$ by linearly extending the relations $J \mathbf{k}=\mathbf{t}, J \mathbf{t}=-\mathbf{k}, J \mathbf{x}=\mathbf{y}$ and $J \mathbf{y}=-\mathbf{x}$.

Proposition 3.1. $(M, g, J)$ defined as above is a Kähler structure on $U$.
Proof. $J$ clearly makes $g$ into an almost hermitian metric. To see that $J$ is integrable, we verify the conditions of Theorem 1 which, in view of (2), are expressed in terms of shear coefficients as $\sigma_{1}^{\mathbf{y}}=\sigma_{2}^{\mathbf{x}}, \sigma_{2}^{\mathbf{y}}=-\sigma_{1}^{\mathbf{x}}, \sigma_{1}^{\mathbf{t}}=\sigma_{2}^{\mathbf{k}}$, $\sigma_{2}^{\mathrm{t}}=-\sigma_{1}^{\mathrm{k}}$. Using (2) and the orthonormality of our frame, by (4), (5), the first pair of these equations each takes the form $0=0$, whereas the second pair is equivalent to the assumed relations (6).

To show that $g$ is Kähler, define a connection on $U$ by first setting
$$\nabla_{\mathbf{k}} \mathbf{k}=-L \mathbf{t}, \quad \nabla_{\mathbf{x}} \mathbf{x}=A \mathbf{k}+E \mathbf{t}, \quad \nabla_{\mathbf{x}} \mathbf{k}=-A \mathbf{x}+E \mathbf{y},$$
and then having all other covariant derivative expressions on frame fields determined by the requirement that ∇ be torsion-free and make $J$ parallel (here the definition of $J$ and relations (3)-(7) are used repeatedly). It is easily checked that ∇ is compatible with the metric $g$, so that it is its Levi-Civita connection and thus $J$ is $g$-parallel. This completes the proof. \(\square\)

\section*{4. The Ricci form}

The Ricci form of the Kähler metric $g$ in Proposition 3.1 is computed as follows. Denote by $w_{1}=\mathbf{k}-i \mathbf{t}, w_{2}=\mathbf{x}-i \mathbf{y}$ the corresponding complex-valued frame, and compute the four complex valued 1-forms $\Gamma_{i}^{j}, i, j=1,2$ for which $\nabla w_{i}=\Gamma_{i}^{j} \otimes w_{j}$, where here ∇ denotes the obvious complexification of the Levi-Civita connection of $g$. The formulas are deduced by computing the components $\nabla_{e_{\ell}} w_{i}$, where $e_{\ell}$ stands for one of the frame fields, using the covariant derivative frame formulas for the Levi-Civita connection ∇ , given in the proof of Proposition 3.1. Two of the four $\Gamma_{i}^{j}$ 's resulting from this calculation are
$$\Gamma_{1}^{1}=-i L(\hat{\mathbf{k}}+\hat{\mathbf{t}}), \quad \Gamma_{2}^{2}=-i(C-H) \hat{\mathbf{k}}-i(A-F) \hat{\mathbf{t}},$$
where the hatted quantities denote the non-metrically-dual coframe of $\left\{e_{\ell}\right\}$. Citing, for example, Lemma 4.2 in [DM], the Ricci form of $g$ is given by
$$\begin{aligned}
\rho=i\left(d \Gamma_{1}^{1}+d \Gamma_{2}^{2}\right)=L(d \hat{\mathbf{k}} & +d \hat{\mathbf{t}})+(C-H) d \hat{\mathbf{k}}+(A-F) d \hat{\mathbf{t}} \\
& +d L \wedge(\hat{\mathbf{k}}+\hat{\mathbf{t}})+d(C-H) \wedge \hat{\mathbf{k}}+d(A-F) \wedge \hat{\mathbf{t}} .
\end{aligned}$$

\section*{5. The Kähler-Einstein condition}

Suppose the metric $g$ of Sec. 3 is Kähler-Einstein, so that
$$\rho=\lambda \omega,$$
where $\omega=\hat{\mathbf{k}} \wedge \hat{\mathbf{t}}+\hat{\mathbf{x}} \wedge \hat{\mathbf{y}}$ is the Kähler form, and $\lambda$ is the Einstein constant. We wish to rewrite this equation in a different form. Applying to our coframe the formula $d \eta(a, b)=d_{a}(\eta(b))-d_{b}(\eta(a))-\eta([a, b])$, valid for any smooth 1-form $\eta$, we have
$$\begin{aligned}
& d \hat{\mathbf{k}}(\mathbf{x}, \mathbf{y})=-\hat{\mathbf{k}}([\mathbf{x}, \mathbf{y}])=-\hat{\mathbf{k}}(N(\mathbf{k}+\mathbf{t}))=-N=d \hat{\mathbf{t}}(\mathbf{x}, \mathbf{y}) \\
& d \hat{\mathbf{k}}(\mathbf{k}, \mathbf{t})=-L=d \hat{\mathbf{t}}(\mathbf{k}, \mathbf{t}), \quad d \hat{\mathbf{k}}(\mathbf{k}, \mathbf{x})=d \hat{\mathbf{k}}(\mathbf{k}, \mathbf{y})=d \hat{\mathbf{k}}(\mathbf{t}, \mathbf{x})=d \hat{\mathbf{k}}(\mathbf{t}, \mathbf{y})=0 .
\end{aligned}$$
Using this in (9) along with the expression for $\omega$ in the coframe, we immediately see that the Kähler-Einstein equation is equivalent to the system
$$\begin{aligned}
& \rho(\mathbf{x}, \mathbf{y})=-N(2 L+C-H+A-F)=\lambda, \\
& \rho(\mathbf{k}, \mathbf{t})=-L(2 L+C-H+A-F)+d_{\mathbf{k}-\mathbf{t}} L-d_{\mathbf{t}}(C-H)+d_{\mathbf{k}}(A-F)=\lambda, \\
& \rho(\mathbf{k}, \mathbf{x})=-d_{\mathbf{x}}(L+C-H)=0, \\
& \rho(\mathbf{k}, \mathbf{y})=-d_{\mathbf{y}}(L+C-H)=0, \\
& \rho(\mathbf{t}, \mathbf{x})=-d_{\mathbf{x}}(L+A-F)=0, \\
& \rho(\mathbf{t}, \mathbf{y})=-d_{\mathbf{y}}(L+A-F)=0,
\end{aligned}$$
where $d_{e_{\ell}}$ denotes the directional derivative with respect to $e_{\ell}$. As equations like (10) involve directional derivatives rather than partial derivatives, they were called generalized PDEs in [AM2], where a precise definition appears.

\section*{6. The ODE and generalized PDE systems}

In the appendix we prove Theorem 2 below, showing that Lie bracket conditions (3)-(7), together with the generalized PDEs (10) characterizing the Kähler-Einstein condition, determine when $\lambda \neq 0$, a locally defined system of five ODEs on six functions, while in one of the $\lambda=0$ subcases they give rise to a system of four generalized PDEs along a two-dimensional distribution. Our purpose in this section is to introduce these two systems.

We first describe a function that will eventually give rise to the independent variable for the ODE system we are trying to obtain. Assuming the setting of section 3, the Lie bracket relations (3)-(5) imply that the distribution spanned by $\mathbf{k}+\mathbf{t}, \mathbf{x}$ and $\mathbf{y}$ is integrable. Since this distribution is orthogonal to $\mathbf{k}-\mathbf{t}$, while the latter vector field has constant length and is easily seen to have geodesic flow, it follows that it is locally a gradient (cf. [ON, Cor. 12.33]). Thus, there exists a smooth function $\tau$ defined in some open set $V \subset U$, such that
$$\mathbf{k}-\mathbf{t}=\nabla \tau .$$
Consider now the six functions $P, Q, R, S, L, N$, where the last two are as in (3), and the first four are given in terms of four of the functions in (4)-(5) by
$$\begin{aligned}
P & =(B-C)+(F-G), & Q & =(B-C)-(F-G), \\
R & =\sqrt{(B+C)^{2}+(F+G)^{2}}, & S & =\tan ^{-1}\left(\frac{B+C}{F+G}\right),
\end{aligned}$$
where $S$ is only defined on the set $\{F+G\} \neq 0$.
Theorem 2. Let $(M, g)$ be a Riemannian 4-manifold admitting an orthonormal frame $\{\mathbf{k}, \mathbf{t}, \mathbf{x}, \mathbf{y}\}$ as in section 3, satisfying in particular relations (3)-(7). Assume also that (10) hold in the set $V \cap\{F+G \neq 0\}$, where $V$ is the domain of $\tau$ of (11).
\begin{itemize}
\item[(1)] Assume $\lambda \neq 0$.
Then $L, N, P, Q, R, S$ above are each a composition of a smooth realvalued function on the image of $\tau$. Additionally, abusing notation by still denoting the latter functions by the same respective letters as the former, they satisfy on $V \cap\{F+G \neq 0\}$ the ODE system
$$\begin{aligned}
N^{\prime} & =N^{2}-L N, & L^{\prime} & =L^{2}-N^{2}+N P / 4+R^{2} / 4, \\
R^{\prime} & =(P / 2+L) R, & P^{\prime} & =P L+R^{2}, \\
S^{\prime} & =-Q / 2 . & &
\end{aligned}$$
\item[(2)] Assume $\lambda=0$ and $N=0$.
Then $P, Q, R, S, L$ satisfy on $V \cap\{F+G \neq 0\}$ the system
\item[i)] $d_{\mathbf{k}-\mathbf{t}} R=R\left(d_{\mathbf{k}+\mathbf{t}} S+P+2 L\right)$, ii) $d_{\mathbf{k}+\mathbf{t}} R=-R\left(d_{\mathbf{k}-\mathbf{t}} S+Q\right)$,
\item[iii)] $d_{\mathbf{k}-\mathbf{t}} L=2 L^{2}+R^{2} / 2, \quad$ iv) $d_{\mathbf{k}-\mathbf{t}} P-d_{\mathbf{k}+\mathbf{t}} Q=2 L P+2 R^{2}$,
\end{itemize}
whereas all $d_{\mathbf{x}}, d_{\mathbf{y}}$ derivatives of these functions vanish.

We make the following remarks. If $F+G=0$ at $p$, but $B+C \neq 0$ at $p$, one can obtain similar systems of equations valid at $p$ simply by redefining $S$ to be $S+\tan ^{-1} k$ for a constant $k$. Thus $R \neq 0$ is the only invariant restriction on the domain, corresponding to considering the non-shear-free region where the shear operators $S_{\mathbf{k}}$ and $S_{\mathbf{t}}$ do not vanish.

Second, and relatedly, note that the last equation in (13) is decoupled from the others, so that one has the freedom to arbitrarily choose, say, $S$. Since $S$ is determined by $B+C$ and $F+G$, both of which appear in (6), this is a reflection of the fact that the shear coefficients are not invariant, and a rotation of, x, y in the plane they span will alter them, giving them, and hence $S$, arbitrary values, without changing the metric under consideration. One can similarly use such a rotation to simplify the form of equation (14), effectively eliminating in this case one of the variables $S, P$ and $Q$. We will employ such a choice in section 11.

One further point regarding case (1) of the theorem is that if $\lambda \neq 0$, the second equation in (13), for $L^{\prime}$, can be replaced by the constraint
$$2 \lambda=-N(4 L+2 N-P),$$
which allows one to eliminate one of the functions $L, N, P$, reducing the number of unknowns. See the appendix for the proof.

In the next three sections we discuss a large class of examples satisfying (3)-(7) and (10), under both assumptions regarding $\lambda$ and $N$ given in Theorem 2. We will not be employing case (1) of this theorem in those sections, as other presentations of the equations seem more amenable to exploring various issues, in particular completeness of the metrics. We expect equations (13) to be utilized in a future study of new types of metrics satisfying the system (3)-(7) and (10). On the other hand, in sections 11 and 12 we rely heavily on a version of equations (14) of case (2) of the theorem.

\section*{7. Cohomogeneity one examples}

In this section we begin the second part of this paper. We first discuss a notable class of examples of Kähler-Einstein metrics on 4-manifolds admitting a frame satisfying conditions (3)-(7).

Assume that $(M, g)$ is a 4-dimensional Riemannian manifold admitting a proper isometric action by a Lie group $\mathcal{G}$ with cohomogeneity one. Then there is a subgroup $\mathcal{H}<\mathcal{G}$ so that $\mathcal{G} / \mathcal{H}$ is the 3-dimensional principal orbit type. Let $p \in M$ be a point with isotropy group $\mathcal{K}$ satisfying $\mathcal{H}<\mathcal{K}<\mathcal{G}$. Then the orbit $\mathcal{G} \cdot p$ through $p$ is isomorphic to $\mathcal{G} / \mathcal{K}$. For the principal $\mathcal{K}$-bundle $\mathcal{G} \rightarrow \mathcal{G} / \mathcal{K}$, consider the associated bundle $\mathcal{G} \times_{\mathcal{K}} \nu_{p}$, where $\nu_{p}$ is the normal space to the orbit at $p$. The differential of the action mapping identifies this bundle with the full normal bundle $\nu$ to the orbit. On the other hand the normal exponential map $\exp _{p}^{\perp}$ at $p$ sends an $\varepsilon$-disk in $\nu_{p}$ to a slice for the action of $\mathcal{G}$
$$S^{\prime}=\left\{\exp _{p}(r X)|0 \leq r<\varepsilon,|X|=1, X \perp \mathcal{G} \cdot p\} .\right.$$
and induces, by the tubular neighborhood theorem, a map from a neighborhood of the zero section in $\nu$ to a neighborhood of the orbit. Putting these facts
together we obtain an equivariant diffeomorphism,
$$\mathcal{G} \times_{\mathcal{K}} D^{n+1} \cong \mathcal{G} \cdot S^{\prime},$$
where $n=\operatorname{dim} \mathcal{K}-\operatorname{dim} \mathcal{H}$ (cf. [Pt, Section 5.6]).
The isotropy action of $\mathcal{K}$ preserves length, so on $S^{\prime}$, we see that the spheres
$$S_{r}=\left\{\exp _{p}(r X)| | X \mid=1, X \perp \mathcal{G} \cdot p\right\}$$
are preserved by the induced action of $\mathcal{K}$. Since points on one of these spheres have isotropy type $\mathcal{H}$, we must have
$$\mathcal{K} / \mathcal{H} \cong \mathbb{S}^{n} .$$

Regarding the metric as residing on $\mathcal{G} \times_{\mathcal{K}} D^{n+1}$, it can be written in the form
$$d r^{2}+g_{r} .$$
We will assume from now on that $\mathcal{G}$ has dimension 3 with $\mathcal{H}$ a discrete principal stabilizer. In the case of a unimodular group, we will now consider the special case of a diagonal metric, in the form appearing, for example, in [DS1]. When $\mathcal{G}$ is unimodular, $g$ has Bianchi type A, and can be written as
$$g=(a b c)^{2} d t^{2}+a^{2} \sigma_{1}^{2}+b^{2} \sigma_{2}^{2}+c^{2} \sigma_{3}^{2},$$
for functions $a, b, c$ of $t$ and invariant 1-forms $\sigma_{1}, \sigma_{2}, \sigma_{3}$. This change of variables allows a more effective use of standard ODE theory, as will become evident in later sections.

The $\sigma_{i}$ satisfy, for some constants $p_{i}$
$$\begin{aligned}
& d \sigma_{1}=p_{1} \sigma_{2} \wedge \sigma_{3}, \\
& d \sigma_{2}=p_{2} \sigma_{3} \wedge \sigma_{1}, \\
& d \sigma_{3}=p_{3} \sigma_{1} \wedge \sigma_{2} .
\end{aligned}$$
In terms of the basis $\partial_{t}, X_{1}, X_{2}, X_{3}$ dual to $d t, \sigma_{1}, \sigma_{2}, \sigma_{3}$
$$\begin{aligned}
{\left[\partial_{t}, X_{i}\right] } & =0, \quad i=1, \ldots, 3, \\
{\left[X_{1}, X_{2}\right] } & =-p_{3} X_{3} \\
{\left[X_{2}, X_{3}\right] } & =-p_{1} X_{1} \\
{\left[X_{3}, X_{1}\right] } & =-p_{2} X_{2}
\end{aligned}$$
For the functions $w_{1}=b c, w_{2}=a c$, and $w_{3}=a b$, define functions $\alpha, \beta$, and $\gamma$ so that
$$\begin{aligned}
& w_{1}^{\prime}=p_{1} w_{2} w_{3}+\alpha w_{1}, \\
& w_{2}^{\prime}=p_{2} w_{1} w_{3}+\beta w_{2}, \\
& w_{3}^{\prime}=p_{3} w_{1} w_{2}+\gamma w_{3} .
\end{aligned}$$
Then, following Dancer and Strachan [DS1], we see that (modulo reordering the frame vectors) the only Kähler structures $(M, g, J)$ with $g$ of the form (17) have complex structure determined by
$$J \partial_{t}=a b X_{3} \quad \text { and } \quad J X_{1}=\frac{a}{b} X_{2},$$
and $\alpha, \beta$, and $\gamma$ satisfy
$$\alpha=\beta \quad \text { and } \quad \gamma=0 .$$
The Kähler form is then given by
$$\omega=a b c^{2} d t \wedge \sigma_{3}+a b \sigma_{1} \wedge \sigma_{2}=w_{1} w_{2} d t \wedge \sigma_{3}+w_{3} \sigma_{1} \wedge \sigma_{2},$$
and $w_{1}, w_{2}, w_{3}$ satisfy
$$\begin{aligned}
& w_{1}^{\prime}=p_{1} w_{2} w_{3}+\alpha w_{1}, \\
& w_{2}^{\prime}=p_{2} w_{1} w_{3}+\alpha w_{2}, \\
& w_{3}^{\prime}=p_{3} w_{1} w_{2} .
\end{aligned}$$
In terms of $a, b, c$ this implies
$$\begin{aligned}
2 a^{\prime} / a & =-p_{1} a^{2}+p_{2} b^{2}+p_{3} c^{2}, \\
2 b^{\prime} / b & =p_{1} a^{2}-p_{2} b^{2}+p_{3} c^{2}, \\
2 c^{\prime} / c & =p_{1} a^{2}+p_{2} b^{2}-p_{3} c^{2}+2 \alpha .
\end{aligned}$$

In the next subsection we derive the Einstein condition, after showing how this model fits within the framework of sections 3-5.
7.1. The frame \{k, t, x, y\}. In this subsection we show how the metric $g$ of the previous subsection gives rise to data satisfying (3)-(7) and (10). Consider the orthonormal frame and dual coframe
$$\begin{array}{ll}
\mathbf{k}=\frac{\sqrt{2}}{2}\left(\frac{1}{c} X_{3}+\frac{1}{a b c} \partial_{t}\right), & \hat{\mathbf{k}}=\frac{\sqrt{2}}{2}\left(c \sigma_{3}+a b c d t\right), \\
\mathbf{t}=\frac{\sqrt{2}}{2}\left(\frac{1}{c} X_{3}-\frac{1}{a b c} \partial_{t}\right), & \hat{\mathbf{t}}=\frac{\sqrt{2}}{2}\left(c \sigma_{3}-a b c d t\right), \\
\mathbf{x}=\frac{X_{1}}{a}, & \hat{\mathbf{x}}=a \sigma_{1}, \\
\mathbf{y}=\frac{X_{2}}{b}, & \hat{\mathbf{y}}=b \sigma_{2} .
\end{array}$$

It can easily be checked that this frame satisfies (3)-(5) for the functions
$$\begin{array}{ll}
A=-E=-\frac{a^{\prime}}{\sqrt{2} a^{2} b c}=-\frac{1}{a} \frac{d a}{d \tau}, & B=F=-\frac{b p_{2}}{\sqrt{2} a c}, \\
D=-H=-\frac{b^{\prime}}{\sqrt{2} a b^{2} c}=-\frac{1}{b} \frac{d b}{d \tau}, & C=G=\frac{a p_{1}}{\sqrt{2} b c}, \\
L=-\frac{c^{\prime}}{\sqrt{2} a b c^{2}}=-\frac{1}{c} \frac{d c}{d \tau}, & N=-\frac{c p_{3}}{\sqrt{2} a b} .
\end{array}$$

Here the prime denotes differentiation with respect to $t$, while the expressions in terms of $d / d \tau$ are justified as follows. We know that relations (3)-(5) imply that $\tau$ is locally defined and $d \tau=\hat{\mathbf{k}}-\hat{\mathbf{t}}$. Our metric can be written as
$$g=\hat{\mathbf{k}}^{2}+\hat{\mathbf{t}}^{2}+\hat{\mathbf{x}}^{2}+\hat{\mathbf{y}}^{2}=\frac{1}{2} d \tau^{2}+\frac{1}{2}(\hat{\mathbf{k}}+\hat{\mathbf{t}})^{2}+\hat{\mathbf{x}}^{2}+\hat{\mathbf{y}}^{2} .$$

This is a special case of (16) for $\tau=\sqrt{2} r$. Furthermore,
$$\begin{array}{ll}
\frac{\mathbf{k}-\mathbf{t}}{\sqrt{2}}=\frac{\partial_{t}}{a b c} & \frac{\hat{\mathbf{k}}-\hat{\mathbf{t}}}{\sqrt{2}}=a b c d t, \\
\frac{\mathbf{k}+\mathbf{t}}{\sqrt{2}}=\frac{X_{3}}{c} & \frac{\hat{\mathbf{k}}+\hat{\mathbf{t}}}{\sqrt{2}}=c \sigma_{3},
\end{array}$$
and
$$\hat{\mathbf{k}}-\hat{\mathbf{t}}=d \tau=\sqrt{2} a b c d t,$$
so that
$$\frac{d}{d \tau}=\frac{1}{\sqrt{2} a b c} \frac{d}{d t} .$$

We note that for our list of functions $A, \ldots, H, L, N$, the four relations in (6)-(7) that imply the Kähler condition impose only two additional relations here, say $A+D=N$ and $B+C=H-E$, giving
$$\begin{aligned}
& \frac{a^{\prime}}{a}+\frac{b^{\prime}}{b}=p_{3} c^{2}, \\
& \frac{b^{\prime}}{b}-\frac{a^{\prime}}{a}=p_{1} a^{2}-p_{2} b^{2}
\end{aligned}$$
These two are of course equivalent to (25)-(26).
Next we consider the Kähler-Einstein equations (10). The last four are satisfied automatically by virtue of the fact that our 10 functions are functions of ( $t$, hence) $\tau$, and $d_{\mathbf{x}} \tau=d_{\mathbf{y}} \tau=0$.

Now the second of equations (10) can be written in the form
$$-L(2 L+C-H+A-F)+\frac{d}{d \tau}(2 L+C-H+A-F)=\lambda .$$
To proceed further, consider the case $p_{3} \neq 0$. Then $N$ is nowhere vanishing, and using the first equation in (10), we can replace (31) by the equation for $\frac{d}{d \tau} N$ in (13). Checking, we easily find that the latter equation is equivalent to (29). Thus if $p_{3} \neq 0$, the only additional independent equation characterizing the Kähler-Einstein condition is the first equation in (10), which, after simplifying and using (29) takes the form
$$2 \frac{c^{\prime}}{c}=p_{1} a^{2}+p_{2} b^{2}-p_{3} c^{2}-\frac{2 \lambda}{p_{3}}(a b)^{2} .$$
Comparing with (27) we deduce the relation $\alpha=-\frac{\lambda}{p_{3}} a^{2} b^{2}$.
In the case where $p_{3}=0$, we have $N=0$. The first equation in (10) gives $\lambda=0$. The second equation in (10) is (31), which reads, via (27),
$$\begin{aligned}
\frac{c^{\prime}}{2(a b c)^{2}}(-2 \alpha) & =-\frac{1}{\sqrt{2} a b c}\left[\frac{1}{\sqrt{2} a b c}(-2 \alpha)\right]^{\prime} \\
& =-\frac{1}{\sqrt{2} a b c} \frac{1}{\sqrt{2} a b} \frac{-c^{\prime}}{c^{2}}(-2 \alpha)-\frac{1}{2(a b c)^{2}}\left(-2 \alpha^{\prime}\right),
\end{aligned}$$
where we have used the fact that $a b$ is constant, as follows from (24) since $p_{3}=0$. As the left hand side is equal to the first term on the right, we see that we must have $\alpha^{\prime}=0$.

To summarize, the Kähler conditions (6)-(7) are expressed as (29)-(30), while the Einstein condition can be summarized as
$$p_{3} \neq 0, \alpha=-\frac{\lambda}{p_{3}} w_{3}^{2}=-\frac{\lambda}{p_{3}} a^{2} b^{2} \quad \text { or } \quad p_{3}=0, \lambda=0, \alpha^{\prime}=0 .$$

Note that besides $p_{3}=0$, the condition $\alpha=0$ also yields $\lambda=0$. This is in line with Theorem 2, as $2 L+C-H+A-F$ is a multiple of $\alpha$.

Finally, the functions $P, Q, R, S$ are given below for completeness, as they will not be used further.
$$\begin{aligned}
P & =-\sqrt{2} \frac{a^{2} p_{1}+b^{2} p_{2}}{a b c}, & Q & =0, \\
R & =\frac{a^{2} p_{1}-b^{2} p_{2}}{a b c}, & S & =\frac{\pi}{4} .
\end{aligned}$$

\section*{8. Ricci Flat Metrics with $p_{3}=0$}

The next two sections describe some examples of the metrics in the previous section.

When $p_{3}=0$ the system can be solved explicitly. In terms of $w_{1}, w_{2}$, and $w_{3}$ we have
$$\begin{aligned}
& w_{1}^{\prime}=p_{1} w_{2} w_{3}+\alpha w_{1}, \\
& w_{2}^{\prime}=p_{2} w_{1} w_{3}+\alpha w_{2}, \\
& w_{3}^{\prime}=0, \quad \alpha^{\prime}=0 .
\end{aligned}$$
This can be written as
$$\begin{aligned}
& \left(e^{-\alpha t} w_{1}\right)^{\prime}=p_{1} w_{3} e^{-\alpha t} w_{2}, \\
& \left(e^{-\alpha t} w_{2}\right)^{\prime}=p_{2} w_{3} e^{-\alpha t} w_{1},
\end{aligned}$$
where $\alpha$ and $w_{3}$ are constant. This implies that
$$\left(e^{-\alpha t} w_{1}\right)^{\prime \prime}=p_{1} p_{2} w_{3}^{2}\left(e^{-\alpha t} w_{1}\right) .$$
The solution then splits into four cases: $p_{1} p_{2}<0$, two cases with $p_{1} p_{2}=0$, and $p_{1} p_{2}>0$.

Case 1: Poincaré Group $p_{1} p_{2}<0$. Assume that $p_{1}=1$ and $p_{2}=-1$, then we have
$$\left(e^{-\alpha t} w_{1}\right)^{\prime \prime}=-w_{3}^{2}\left(e^{-\alpha t} w_{1}\right) .$$
The solution is
$$\begin{aligned}
& w_{1}=k e^{\alpha\left(t-t_{0}\right)} \sin \left(w_{3}\left(t-t_{0}\right)\right), \\
& w_{2}=k e^{\alpha\left(t-t_{0}\right)} \cos \left(w_{3}\left(t-t_{0}\right)\right) .
\end{aligned}$$

Therefore
$$\begin{aligned}
a & =\sqrt{w_{3} \cot \left(w_{3}\left(t-t_{0}\right)\right)}, \\
b & =\sqrt{w_{3} \tan \left(w_{3}\left(t-t_{0}\right)\right)}, \\
c & =k e^{\alpha\left(t-t_{0}\right)} \sqrt{\frac{1}{2 w_{3}} \sin \left(2 w_{3}\left(t-t_{0}\right)\right)},
\end{aligned}$$
and the metric is
$$\begin{aligned}
g= & \frac{k^{2}}{2} e^{2 \alpha\left(t-t_{0}\right)} \sin \left(2 w_{3}\left(t-t_{0}\right)\right) w_{3}\left(d t^{2}+\frac{\sigma_{3}^{2}}{w_{3}^{2}}\right) \\
& +w_{3} \cot \left(w_{3}\left(t-t_{0}\right)\right) \sigma_{1}^{2}+w_{3} \tan \left(w_{3}\left(t-t_{0}\right)\right) \sigma_{2}^{2} .
\end{aligned}$$
The singular points $t=t_{0}, t_{0}+\frac{\pi}{2 w_{3}}$ are both at finite distance, so this metric is not complete.

Case 2: Abelian Group $T^{3} p_{1}=p_{2}=0$. Here the solution is
$$\begin{aligned}
a & =a_{0}, \\
b & =b_{0}, \\
c & =c_{0} e^{\alpha\left(t-t_{0}\right)}
\end{aligned}$$
The metric takes the form
$$g=\left(\frac{a_{0} b_{0} c_{0}}{\alpha}\right)^{2}\left(\left(d e^{\alpha\left(t-t_{0}\right)}\right)^{2}+\left(\frac{\alpha}{a_{0} b_{0}}\right)^{2} e^{2 \alpha\left(t-t_{0}\right)} \sigma_{3}^{2}\right)+a_{0}^{2} \sigma_{1}^{2}+b_{0}^{2} \sigma_{2}^{2}$$
This is a product of $T^{2}$ with a two dimensional cone metric, which gives a smooth flat metric when $\alpha=a_{0} b_{0}$.

Case 3: Heisenberg Group $p_{1} p_{2}=0$. Assume that $p_{1}=1$ and $p_{2}=0$. Then the solution is
$$\begin{aligned}
& w_{1}=k w_{3} e^{\alpha\left(t-t_{0}\right)}\left(t-t_{0}\right), \\
& w_{2}=k e^{\alpha\left(t-t_{0}\right)} .
\end{aligned}$$
Therefore
$$\begin{aligned}
a & =\frac{1}{\sqrt{t-t_{0}}}, \\
b & =w_{3} \sqrt{t-t_{0}}, \\
c & =k e^{\alpha\left(t-t_{0}\right)} \sqrt{t-t_{0}},
\end{aligned}$$
and the metric is
$$g=k^{2} w_{3}^{2} e^{2 \alpha\left(t-t_{0}\right)}\left(t-t_{0}\right) d t^{2}+\frac{1}{t-t_{0}} \sigma_{1}^{2}+w_{3}^{2}\left(t-t_{0}\right) \sigma_{2}^{2}+k^{2} e^{2 \alpha\left(t-t_{0}\right)}\left(t-t_{0}\right) \sigma_{3}^{2} .$$
The singular point $t=t_{0}$ is at finite distance, so this metric is not complete.

Case 4: Euclidean Group $p_{1} p_{2}>0$. Assume that $p_{1}=1$ and $p_{2}=1$, then we have
$$\left(e^{-\alpha t} w_{1}\right)^{\prime \prime}=w_{3}^{2}\left(e^{-\alpha t} w_{1}\right) .$$
The solution is
$$\begin{aligned}
& w_{1}=k e^{\alpha\left(t-t_{0}\right)} \sinh \left(w_{3}\left(t-t_{0}\right)\right), \\
& w_{2}=k e^{\alpha\left(t-t_{0}\right)} \cosh \left(w_{3}\left(t-t_{0}\right)\right),
\end{aligned}$$
Therefore
$$\begin{aligned}
a & =\sqrt{w_{3} \operatorname{coth}\left(w_{3}\left(t-t_{0}\right)\right)}, \\
b & =\sqrt{w_{3} \tanh \left(w_{3}\left(t-t_{0}\right)\right)}, \\
c & =k e^{\alpha\left(t-t_{0}\right)} \sqrt{\frac{1}{2 w_{3}} \sinh \left(2 w_{3}\left(t-t_{0}\right)\right)},
\end{aligned}$$
and the metric is
$$\begin{aligned}
g= & \frac{k^{2}}{2} e^{2 \alpha\left(t-t_{0}\right)} \sinh \left(2 w_{3}\left(t-t_{0}\right)\right) w_{3}\left(d t^{2}+\frac{\sigma_{3}^{2}}{w_{3}^{2}}\right) \\
& +w_{3} \operatorname{coth}\left(w_{3}\left(t-t_{0}\right)\right) \sigma_{1}^{2}+w_{3} \tanh \left(w_{3}\left(t-t_{0}\right)\right) \sigma_{2}^{2} .
\end{aligned}$$
The singular point $t=t_{0}$ is at finite distance, so this metric is not complete.
The Ricci-flat metrics with $p_{3} \neq 0$, but $p_{1} p_{2}=0$ are similar to those with $p_{3}=0$ and $\alpha=0$. The Ricci-flat metrics with $p_{1} p_{2} p_{3} \neq 0$ are addressed in [BGPP].

\section*{9. The Heisenberg Group with $p_{3} \neq 0$}

When $p_{1}=p_{2}=0, p_{3}=1$, and $\lambda=-1$ the Lie-algebra spanned by $X_{1}, X_{2}, X_{3}$ is the nilpotent Heisenberg Lie-algebra. The Kähler-Einstein equations are
$$\begin{aligned}
2 a^{\prime} / a & =c^{2}, \\
2 b^{\prime} / b & =c^{2}, \\
2 c^{\prime} / c & =-c^{2}+2 a^{2} b^{2} .
\end{aligned}$$
This has two first integrals
$$\begin{aligned}
\left(\frac{a}{b}\right)^{\prime} & =0, \\
\left(a b\left(c^{2}-\frac{2}{3} a^{2} b^{2}\right)\right)^{\prime} & =0 .
\end{aligned}$$
The first one implies that $a$ is a constant multiple of $b$. A metric with such a property was termed biaxial in [DS1], and triaxial if it does not have this property. In terms of shears, the biaxial case occurs in the shear-free case, and is generally simpler from the point of view of integrability of the solutions. It was shown in [AM2] that there is a complete Kähler-Einstein metric of this type on a manifold admitting a cohomogeneity one action of a quotient of the

Heisenberg group by a discrete subgroup. The metric was described in that reference via an orthonormal frame as in section 3.

For this reason, we will not go any further into the description of this metric. Of the remaining Bianchi type A cases with $p_{3} \neq 0$, the case of $S U(2)$ has been extensively studied. Of the remaining cases involving the noncompact groups $S L(2, \mathbb{R})$, the Poincare group and the Euclidean group, we describe complete metrics only for the latter, in the next section.

\section*{10. The Euclidean Group with $p_{3} \neq 0$}

In this section we describe a complete triaxial Kähler-Einstein metric with a cohomogeneity one action of the Euclidean group $E(2)$. The method follows in part the work in [DS1] and [DS2] which gives an analogous result for the case of the compact group $S U(2)$. Two main differences in method from those references are a systematic use of recent results of Verdiani and Ziller [VZ], and the establishment of Cauchy-Schwarz type estimates yielding completeness for this non-compact group.

We set $p_{2}=0, p_{1}=p_{3}=1$, and $\lambda=-1$. The Lie-algebra spanned by $X_{1}, X_{2}, X_{3}$ is the Lie-algebra of the Euclidean group. The Kähler-Einstein equations are
$$\begin{aligned}
2 a^{\prime} / a & =-a^{2}+c^{2}, \\
2 b^{\prime} / b & =a^{2}+c^{2}, \\
2 c^{\prime} / c & =a^{2}-c^{2}+2 a^{2} b^{2}
\end{aligned}$$
Note that the derivatives in this system are given by polynomials in the dependent variables, hence are locally Lipschitz, so that standard ODE theory applies. As for the symmetries of these equations, first, they are autonomous, so constant shifts in $t$ preserve solutions. Finally, the scaling symmetry
$$(a(t), b(t), c(t)) \rightarrow\left(k a\left(k^{2} t\right), b\left(k^{2} t\right), k c\left(k^{2} t\right)\right),$$
taking solutions to solutions, will play a role later on.
10.1. Linearization about Equilibria. The non-zero equilibrium solutions are $(q, 0, q)$ and $(0, q, 0)$. Then in terms of $a, b$, and $c$,
$$\begin{aligned}
a^{\prime} & =\frac{a}{2}\left(-a^{2}+c^{2}\right), \\
b^{\prime} & =\frac{b}{2}\left(a^{2}+c^{2}\right), \\
c^{\prime} & =\frac{c}{2}\left(a^{2}-c^{2}+2 a^{2} b^{2}\right) .
\end{aligned}$$
has linearization about $(q, 0, q)$
$$\begin{aligned}
a^{\prime} & =-q^{2} a+q^{2} c, \\
b^{\prime} & =q^{2} b, \\
c^{\prime} & =q^{2} a-q^{2} c .
\end{aligned}$$
which has one positive, one negative and one zero eigenvalue. The linearization about $(0, q, 0)$ has three zero eigenvalues.
Theorem 3. A solution of (33)-(35) yields a complete Kähler-Einstein metric of the form (17) on a cohomogeneity one $E(2)$-manifold if and only if it is a solution along an unstable curve of an equilibrium point $(q, 0, q), q>0$.
Proof. The proof is broken into three steps. First, in Proposition 10.2 we show that solutions with a maximal interval having a finite left endpoint do not give complete metrics. Then we show that solutions with maximal interval of the form $(-\infty, \eta)$ are the unstable curves of the equilibrium points $(q, 0, q), q>0$, and these solutions satisfy $0 \leq c^{2}-a^{2} \leq 2 a^{2} b^{2}$. Next, in Proposition 10.3 we show that $\eta$ is finite, but for curves on the manifold orthogonal to the orbits the endpoint corresponding to $\eta$ is infinitely far away, while the endpoint corresponding to $-\infty$ is at finite distance. To complete the proof that this gives us a complete Kähler-Einstein metric we show that $g$ and $\omega$ can be extended smoothly as $t \rightarrow-\infty$, and then finish the proof of completeness by showing all finite length curves remain inside some compact set. These are completed in Propositions 10.4 and 10.5, respectively. \(\square\)

We first record in a lemma some relations, easily verifiable via (33)-(35), which will be used later in the proof.
Lemma 10.1. For the system (33)-(35),
$$\begin{aligned}
(a b)^{\prime} & =a b c^{2}, \\
(b c)^{\prime} & =b c a^{2}\left(1+b^{2}\right), \\
(a c)^{\prime} & =a^{3} c b^{2}, \\
\left(\frac{a}{b}\right)^{\prime} & =-\frac{a^{3}}{b}, \\
\left(a^{2}\right)^{\prime} & =\left(a^{2}\right)\left(-a^{2}+c^{2}\right) \\
\left(a^{2}-c^{2}\right)^{\prime} & =-\left(a^{2}-c^{2}\right)\left(a^{2}+c^{2}\right)-2 a^{2} b^{2} c^{2} \\
-\left(c^{2}\right)^{\prime} & =-c^{2}\left(a^{2}-c^{2}\right)-2 a^{2} b^{2} c^{2}
\end{aligned}$$
10.2. Solutions.

Proposition 10.2. There are no complete metrics corresponding to solutions of (33)-(35) with maximal interval $(\xi, \eta)$, when $\xi$ is finite. Furthermore, the only solutions with maximal interval $(-\infty, \eta)$ are the unstable curves of the equilibrium points $(q, 0, q), q>0$, and these solutions satisfy $0 \leq c^{2}-a^{2} \leq$ $2 a^{2} b^{2}$.

Proof. For an initial time $t_{0}$, let $(\xi, \eta)$ be a maximal solution interval for the initial value problem for (33)-(35) with $a\left(t_{0}\right)=a_{0}, b\left(t_{0}\right)=b_{0}$, and $c\left(t_{0}\right)=c_{0}$.

Uniqueness of solutions to (33)-(35) implies that if any of $a, b$, or $c$ are zero anywhere in $(\xi, \eta)$ then it is zero everywhere. Accordingly we assume that $a$, $b$, and $c$ are all positive on $(\xi, \eta)$. Then we see from Lemma 10.1 and (34) that $a b, b c, a c$, and $b$ are all increasing on $(\xi, \eta)$.

We consider the following cases:

Case 1: $c_{0}^{2}-a_{0}^{2}<0$. We first make the following claim.
Claim: In this case $a \rightarrow \infty$ as $t \rightarrow \xi^{+}$.
Proof of claim: Since
$$\left(c^{2}-a^{2}\right)^{\prime}=-\left(c^{2}-a^{2}\right)\left(c^{2}+a^{2}\right)+2 a^{2} b^{2} c^{2},$$
if $c^{2}-a^{2}<0$ then $\left(c^{2}-a^{2}\right)^{\prime}>0$, thus $c^{2}-a^{2}<0$ for all $\xi<t<t_{0}$. Therefore,
$$\begin{aligned}
a^{\prime} & =\frac{a}{2}\left(c^{2}-a^{2}\right), \\
a^{\prime \prime} & =\frac{a}{4}\left[\left(c^{2}-a^{2}\right)^{2}-2\left(c^{2}-a^{2}\right)\left(c^{2}+a^{2}\right)+4 a^{2} b^{2} c^{2}\right],
\end{aligned}$$
showing that $a$ is decreasing and concave up on $\left(\xi, t_{0}\right)$. Next, we always have $b^{\prime}>0$, while
$$c^{\prime}=\frac{c}{2}\left(a^{2}-c^{2}+2 a^{2} b^{2}\right)>0,$$
shows that $c$ is increasing on $\left(\xi, t_{0}\right)$. Therefore $b$ and $c$ are bounded on $\left(\xi, t_{0}\right)$. Thus, as $(\xi, \eta)$ is the maximal solution interval, $a$ could be bounded as $t \rightarrow \xi^{+}$ only if $\xi=-\infty$. But since $a$ is concave up, $a \rightarrow \infty$ as $t \rightarrow \xi^{+}$even when $\xi=-\infty$. \(\square\)

Since $a b$ and $a c$ are increasing, they are bounded as $t \rightarrow \xi^{+}$and $a \rightarrow \infty$, so $b \rightarrow 0, c \rightarrow 0$, and $a b \rightarrow k$ for some constant $k$. Then as $t \rightarrow \xi^{+}$the equations will take the asymptotic form
$$\begin{aligned}
a^{\prime} & =-\frac{1}{2} a^{3} \\
b^{\prime} & =\frac{1}{2} b a^{2} \\
c^{\prime} & =\frac{1}{2} c\left(a^{2}+2 k^{2}\right)
\end{aligned}$$
the solution of which has asymptotic form
$$\begin{aligned}
a & \simeq(t-\xi)^{-\frac{1}{2}}, \\
b & \simeq b_{1}(t-\xi)^{\frac{1}{2}}, \\
c & \simeq c_{1}(t-\xi)^{\frac{1}{2}},
\end{aligned}$$
for some constants $b_{1}$ and $c_{1}$. This shows that $\xi$ is finite in this case and
$$\int_{\xi}^{t_{0}} a b c d t<\infty,$$
so the metric is not complete.

Case 2: $c_{0}^{2}-a_{0}^{2}>2 a_{0}^{2} b_{0}^{2}$. Here we have a similar claim.
Claim: In this case $c \rightarrow \infty$ as $t \rightarrow \xi^{+}$.
Proof of claim: Since
$$\left(c^{2}-a^{2}-2 a^{2} b^{2}\right)^{\prime}=-\left(c^{2}-a^{2}\right)\left(c^{2}+a^{2}\right)-2 a^{2} b^{2} c^{2},$$
if $c^{2}-a^{2}-2 a^{2} b^{2}>0$ then $\left(c^{2}-a^{2}-2 a^{2} b^{2}\right)^{\prime}<0$, thus in this case, $c^{2}-a^{2}>2 a^{2} b^{2}$ for all $\xi<t \leq t_{0}$. Therefore,
$$\begin{aligned}
c^{\prime} & =\frac{c}{2}\left(a^{2}-c^{2}+2 a^{2} b^{2}\right), \\
c^{\prime \prime} & =\frac{c}{4}\left[\left(a^{2}-c^{2}+2 a^{2} b^{2}\right)^{2}+2\left(c^{2}-a^{2}\right)\left(c^{2}+a^{2}\right)+4 a^{2} b^{2} c^{2}\right],
\end{aligned}$$
showing that $c$ is decreasing and concave up on $\left(\xi, t_{0}\right)$. Next, we always have $b^{\prime}>0$, while $a$ is increasing on $\left(\xi, t_{0}\right)$. Therefore $a$ and $b$ are bounded on $\left(\xi, t_{0}\right)$. Thus, as $(\xi, \eta)$ is the maximal solution interval, $c$ could be bounded as $t \rightarrow \xi^{+}$ only if $\xi=-\infty$. But since $c$ is concave up, $c \rightarrow \infty$ as $t \rightarrow \xi^{+}$even when $\xi=-\infty$. \(\square\)

Since $a c$ and $b c$ are increasing, they are bounded as $t \rightarrow \xi^{+}$and $c \rightarrow \infty$, so $a \rightarrow 0, b \rightarrow 0$. Then as $t \rightarrow \xi^{+}$the equations will take the asymptotic form
$$\begin{aligned}
& a^{\prime}=\frac{1}{2} a c^{2} \\
& b^{\prime}=\frac{1}{2} b c^{2} \\
& c^{\prime}=-\frac{1}{2} c^{3}
\end{aligned}$$
which has solution
$$\begin{aligned}
a & \simeq a_{1}(t-\xi)^{\frac{1}{2}} \\
b & \simeq b_{1}(t-\xi)^{\frac{1}{2}} \\
c & \simeq(t-\xi)^{-\frac{1}{2}}
\end{aligned}$$
for some constants $a_{1}$ and $b_{1}$. This shows that $\xi$ is finite in this case and
$$\int_{\xi}^{t_{0}} a b c d t<\infty,$$
so the metric is not complete.
If $c^{2}-a^{2}<0$ or $c^{2}-a^{2}>2 a^{2} b^{2}$ at any time, then a constant shift in $t$ will give one of the previous cases. In both previous cases, $\xi$ is finite, but we know that the unstable curve of the equilibrium points $(q, 0, q)$ must have $\xi=-\infty$. The existence of these curves is guaranteed by the center manifold theorem. Therefore we consider the final case:

Case 3: $0 \leq c^{2}-a^{2} \leq 2 a^{2} b^{2}$ for all $t \in(\xi, \eta)$. Here we have a different claim.
Claim: In this case $\xi=-\infty$.
Proof of claim: In this case $a, b$, and $c$ are all increasing, therefore they are all bounded on $\left(\xi, t_{0}\right)$. Since $(\xi, \eta)$ is the maximal solution interval $\xi=-\infty$. \(\square\)

As $a$, $b$, and $c$ are all increasing, it must be that they all approach finite non-negative limits as $t \rightarrow-\infty$. Thus $(a, b, c)$ must approach an equilibrium point. If $(a, b, c) \rightarrow(0, q, 0)$ with $q>0$, then $a / b \rightarrow 0$ as $t \rightarrow-\infty$, but $a / b$ is decreasing and positive (see Lemma 10.1), so this cannot happen.

Therefore, when $t \rightarrow-\infty$ we see that $(a, b, c) \rightarrow(q, 0, q)$ in this case, but we still need to rule out the possibility that $q=0$. For this we compute the variation of $a c$ with respect to $b$ :
$$\frac{d(a c)}{d b}=\frac{2\left(\frac{a}{c}\right)^{2}(a c) b}{\left(\frac{a}{c}\right)^{2}+1} .$$
Our assumption of an equilibrium point $(q, 0, q)$ implies that $a / c \rightarrow 1$ when $b \rightarrow 0$. Since in our case $c^{2}-a^{2} \geq 0$, we have
$$\frac{a}{c} \leq 1 .$$
Employing this in equation (36) yields
$$\frac{d(a c)}{d b} \leq(a c) b .$$
By Grönwall's inequality, if $a c \rightarrow 0$ when $b \rightarrow 0$ then $a c=0$ identically. As the latter is not possible (see the beginning of the proof), neither is $q=0$. \(\square\)

Proposition 10.3. Let $g$ be a Riemannian metric of the form (17) on a manifold $M$, with $a, b, c$ a solution to (33)-(35) along an unstable curve of an equilibrium point $(q, 0, q), q>0$, having maximal domain $I=(-\infty, \eta)$. Assume that the latter interval is also the range of the coordinate function $t$ on $M$. For a point $p_{0} \in M$ with orbit through $p_{0}$ of principal type and $M^{t}$ a level set of $t$,
$$\lim _{t \rightarrow-\infty} d_{g}\left(p_{0}, M^{t}\right)<\infty, \quad \lim _{t \rightarrow \eta} d_{g}\left(p_{0}, M^{t}\right)=\infty,$$
where $d_{g}$ is the distance function induced by $g$.
Proof. The union of the principal orbits forms an open dense set, $\tilde{M}$, so that $\tilde{M} / \mathcal{G}$ is a smooth manifold of dimension 1. The function $t$ is a smooth submersion from $\tilde{M}$ to $\tilde{M} / \mathcal{G}$. The metric
$$(a b c)^{2} d t^{2}$$
makes this into a Riemannian submersion. The level sets of $t$ are orbits of $\mathcal{G}$ and for $t_{0}=t\left(p_{0}\right)$
$$d_{g}\left(p_{0}, M^{t_{1}}\right)=d_{g}\left(M^{t_{0}}, M^{t_{1}}\right),$$
is the distance in the quotient manifold where
$$d_{g}\left(M^{t_{0}}, M^{t_{1}}\right)=\left|\int_{t_{0}}^{t_{1}} a b c d t\right| .$$

Asymptotically as $t \rightarrow-\infty$,
$$\begin{aligned}
& a \simeq q \\
& b \simeq k e^{q^{2} t} \\
& c \simeq q
\end{aligned}$$
This gives the asymptotic metric
$$g \simeq k^{2} q^{4} e^{2 q^{2} t} d t^{2}+q^{2} \sigma_{1}^{2}+k^{2} e^{2 q^{2} t} \sigma_{2}^{2}+q^{2} \sigma_{3}^{2},$$
and for $v=k e^{q^{2} t}$ this is just
$$g \simeq\left(d v^{2}+v^{2} \sigma_{2}^{2}\right)+q^{2}\left(\sigma_{1}^{2}+\sigma_{3}^{2}\right) .$$
In this coordinate, the endpoint $\xi=-\infty$ is at $v=0$, and we see that
$$\lim _{t \rightarrow-\infty} d_{g}\left(p_{0}, M^{t}\right)=\int_{-\infty}^{t_{0}} a b c d t=\int_{0}^{v_{0}} d v<\infty .$$

Now to understand the behavior at the $\eta$ side of the solution interval, we examine the derivative of $a / c$ with respect to $b$
$$\frac{d\left(\frac{a}{c}\right)}{d b}=\frac{2\left(\frac{a}{c}\right)}{b}\left(\frac{1-\left(\frac{a}{c}\right)^{2}\left(1+b^{2}\right)}{\left(\frac{a}{c}\right)^{2}+1}\right),$$
This equation has nullcline
$$\frac{a}{c}=\sqrt{\frac{1}{1+b^{2}}},$$
Since the nullcline is always decreasing, and our solution starts at $\frac{a}{c}=1$ when $b=0$, we have
$$\frac{a}{c} \geq \sqrt{\frac{1}{1+b^{2}}} .$$

To find a better upper bound than 1 for $a / c$, we consider the curve $\frac{a}{c}=$ $\sqrt{\frac{k^{2}}{k^{2}+b^{2}}}$ and plug its expression into the slope field. This gives slope
$$\frac{2 k^{2}+2 b^{2}}{2 k^{2}+b^{2}}\left(k^{2}-1\right) \frac{d}{d b} \sqrt{\frac{k^{2}}{k^{2}+b^{2}}} .$$
So for $k^{2}>2$, the slope of the solutions along this curve are less, i.e. more negative, than the slope of the curve. Since for our (non-equilibrium) solution, there is some $b_{p}$ in the range of $b$ for which one has $\left(\frac{a}{c}\right)\left(b_{p}\right)<1$, the graph of $a / c$ is below the graph of $\sqrt{\frac{k^{2}}{k^{2}+b^{2}}}$ for some $k=k_{p}>2$ at $b_{p}$, and hence for all $b \geq b_{p}$. Therefore for $b \geq b_{p}$
$$\sqrt{\frac{1}{1+b^{2}}} \leq \frac{a}{c} \leq \sqrt{\frac{k_{p}^{2}}{k_{p}^{2}+b^{2}}}$$
Next we deduce an estimate for $a c$ in terms of $b$, for $b>b_{p}$. Using (36) and the last inequalities, we have
$$\frac{2 b}{2+b^{2}} \leq \frac{d(\ln (a c)}{d b} \leq \frac{2 b k_{p}^{2}}{2 k_{p}^{2}+b^{2}},$$
and integrating this from $b=0$ to $b$, exponentiating and multiplying by $q^{2}$ gives
$$\ln \frac{2+b^{2}}{2} \leq \ln \frac{a c}{q^{2}} \leq k_{p}^{2} \ln \frac{2 k_{p}^{2}+b^{2}}{2 k_{p}^{2}} .$$
Therefore
$$q^{2} \frac{2+b^{2}}{2} \leq a c \leq q^{2}\left(\frac{2 k_{p}^{2}+b^{2}}{2 k_{p}^{2}}\right)^{k_{p}^{2}} .$$
Finally, these can be used to estimate $b$ as
$$b^{\prime}=\frac{b}{2}\left(a^{2}+c^{2}\right)=\frac{b}{2}(a c)\left(\frac{a}{c}+\frac{c}{a}\right) .$$
Therefore, for some positive constant $K_{1}$ and $b=b(t)>b_{p}$,
$$b^{\prime} \geq K_{1} b^{4},$$
showing that $\eta$ is finite, but for some constant $K_{2}>0$, using the notation $b_{0}:=\max \left\{b\left(t_{0}\right), b_{p}\right\}>0$, we have
$$\lim _{t \rightarrow \eta} d_{g}\left(p_{0}, M^{t}\right)=\int_{t_{0}}^{\eta} a b c d t \geq \int_{b_{0}}^{\infty} \frac{2}{\frac{a}{c}+\frac{c}{a}} d b \geq \int_{b_{0}}^{\infty} \frac{K_{2}}{b} d b=\infty .$$ \(\square\)
10.3. The Bolt. The phrase "attaching a bolt" refers to replacing a 4-manifold with a cohomogeneity one action with only regular fibers over an open interval with one admitting a similar action for the same group over a semi-closed interval with a two dimensional singular fiber (the bolt) over the endpoint of the interval. For the case at hand, the latter 4-manifold can be described as
$$E(2) \times_{S O(2)} \mathbb{R}^{2}=(0, \infty) \times E(2) \amalg\{0\} \times \mathbb{R}^{2},$$
where the right $S O(2)$-action is $(g,(T, x)) \rightarrow\left(T g, g^{-1} x\right)$.
Proposition 10.4. The metric and Kähler form corresponding to solutions of (33)-(35) along the unstable curves of the equilibrium points $(q, 0, q), q>0$, defined on $(-\infty, \eta)$, can be smoothly extended to $E(2) \times_{S O(2)} \mathbb{R}^{2}$, with the bolt fibering over $\xi=-\infty$.

Proof. Consider the manifold $M=E(2) \times_{S O(2)} \mathbb{R}^{2}$. This has a left action by $E(2)$ with regular orbit $E(2)$ and singular orbit $E(2) / S O(2)$. For any $E(2)$ invariant metric $g$ on $M$, with $r$ the distance along a geodesic perpendicular to the singular orbit,
$$g=d r^{2}+g_{r} .$$
For a metric $g$ of the form (17), let $r=\int_{-\infty}^{t} a(s) b(s) c(s) d s$, then
$$g=d r^{2}+a^{2} \sigma_{1}^{2}+b^{2} \sigma_{2}^{2}+c^{2} \sigma_{3}^{2} .$$

The ODE's (33)-(35) in this coordinate become
$$\begin{aligned}
& \frac{d a}{d r}=\frac{a}{2}\left(-\frac{a}{b c}+\frac{c}{a b}\right), \\
& \frac{d b}{d r}=\frac{1}{2}\left(\frac{a}{c}+\frac{c}{a}\right), \\
& \frac{d c}{d r}=\frac{c}{2}\left(\frac{a}{b c}-\frac{c}{a b}+2 \frac{a b}{c}\right) .
\end{aligned}$$
From these it is seen that $a, b$, and $c$ can be extended at $r=0$ so that $a$ and $c$ are even and $b$ is odd. Following the notations of Verdiani and Ziller [VZ], the tangent space for $r \neq 0$ splits as
$$T_{p} M=\mathbb{R} \partial_{r} \oplus \mathfrak{k} \oplus \mathfrak{m},$$
where
$$\begin{gathered}
\mathfrak{k}=\operatorname{span}\left\{X_{2}\right\}, \\
\mathfrak{m}=\operatorname{span}\left\{X_{1}, X_{3}\right\}=: \ell_{1},
\end{gathered}$$
and we set
$$V=\operatorname{span}\left\{\partial_{r}, X_{2}\right\}=: \ell_{-1}^{\prime} .$$
Since $\exp \left(\theta X_{2}\right)$ acts on both $V$ and $\mathfrak{m}$ as a rotation by $\theta$, we have weights $a_{1}=d_{1}=1$. The smoothness conditions for $V$ is that $b$ can be extended to an odd function and $b^{\prime}(0)=1$. Since we know that $b$ can be extended to be odd, we just check from (40) that
$$\left.\frac{d b}{d r}\right|_{r=0}=\frac{1}{2}\left(\frac{q}{q}+\frac{q}{q}\right)=1 .$$
Since $\ell_{-1}^{\prime}$ and $\ell_{1}$ are perpendicular, the smoothness conditions in table C of [VZ] are automatically satisfied, while those in table B there, are
$$\begin{aligned}
& a^{2}+c^{2}=\phi_{1}\left(r^{2}\right), \\
& a^{2}-c^{2}=r^{2} \phi_{2}\left(r^{2}\right),
\end{aligned}$$
for some smooth functions $\phi_{1}$ and $\phi_{2}$. Now to see that (42) is satisfied, note that
$$a^{2}+c^{2}=2 a c \frac{d b}{d r} .$$
Since $a, c$, and $\frac{d b}{d r}$ are even, it just remains to check (43). As $a, c$ are even while $b$ is odd, $a / c$ is even as a function of $b$. We have to second order
$$a^{2}-c^{2}=c^{2}\left(\frac{a^{2}}{c^{2}}-1\right) \propto b^{2} c^{2},$$
and since $b(0)=0$ and $\left.\frac{d b}{d r}\right|_{r=0}=1$, we get that $g$ extends to a smooth metric on $M$.

Finally we check that the Kähler form extends across the singular orbit at $r=0$. Following Verdiani and Ziller we analyze the eigenspaces for the action of $S O(2)$ on $T_{p} M$. We find that $\partial_{r}+\frac{i}{r} X_{2}$ is an eigenvector with eigenvalue $e^{i a_{1} \theta}$, and $X_{1}+i X_{3}$ is an eigenvector with eigenvalue $e^{i d_{1} \theta}$, and likewise for their complex conjugates. Dualizing gives eigenspaces of $T_{p}^{*} M: d r-i r \sigma_{2}$ has
eigenvalue $e^{i a_{1} \theta}$, and $\sigma_{1}-i \sigma_{3}$ has eigenvalue $e^{i d_{1} \theta}$. Thus the eigenspaces of $\Lambda^{2} T_{p}^{*} M$ are
$$\begin{aligned}
E_{1} & =\operatorname{span}\left\{r d r \wedge \sigma_{2}, \sigma_{1} \wedge \sigma_{3}\right\} \\
E_{e^{i\left(a_{1}-d_{1}\right) \theta}} & =\operatorname{span}\left\{d r \wedge \sigma_{1}+r \sigma_{2} \wedge \sigma_{3}+i\left(d r \wedge \sigma_{3}+r \sigma_{1} \wedge \sigma_{2}\right)\right\} \\
E_{e^{i\left(a_{1}+d_{1}\right) \theta}} & =\operatorname{span}\left\{d r \wedge \sigma_{1}-r \sigma_{2} \wedge \sigma_{3}+i\left(d r \wedge \sigma_{3}-r \sigma_{1} \wedge \sigma_{2}\right)\right\}
\end{aligned}$$
The smoothness condition is just the equivariance condition $\omega\left(e^{a_{1} \theta} p\right)=$ $\exp \left(\theta X_{2}\right)^{*} \omega$. This requires that the coefficient of
$$\begin{gathered}
E_{1} \text { is } \phi_{1}\left(r^{2}\right), \\
E_{e^{ \pm i\left(a_{1}-d_{1}\right) \theta}} \text { is } r^{\frac{\left|a_{1}-d_{1}\right|}{a_{1}}} \phi_{2}\left(r^{2}\right), \\
E_{e^{ \pm i\left(a_{1}+d_{1}\right) \theta}} \text { is } r^{\frac{\left|a_{1}+d_{1}\right|}{a_{1}}} \phi_{3}\left(r^{2}\right) .
\end{gathered}$$
Now we have
$$\begin{aligned}
\omega= & c d r \wedge \sigma_{3}+a b \sigma_{1} \wedge \sigma_{3} \\
= & \frac{c}{2}\left[\left(d r \wedge \sigma_{3}+r \sigma_{1} \wedge \sigma_{2}\right)+\left(d r \wedge \sigma_{3}-r \sigma_{1} \wedge \sigma_{2}\right)\right] \\
& +\frac{a b}{2 r}\left[\left(d r \wedge \sigma_{3}+r \sigma_{1} \wedge \sigma_{2}\right)-\left(d r \wedge \sigma_{3}-r \sigma_{1} \wedge \sigma_{2}\right)\right] \\
= & \frac{c r+a b}{2 r}\left(d r \wedge \sigma_{3}+r \sigma_{1} \wedge \sigma_{2}\right) \\
& +\frac{c r-a b}{2 r}\left(d r \wedge \sigma_{3}-r \sigma_{1} \wedge \sigma_{2}\right) .
\end{aligned}$$
Using $a_{1}=d_{1}=1$ in (45)-(46), the smoothness conditions can now be written as
$$\begin{aligned}
& c r+a b=r \phi_{2}\left(r^{2}\right) \\
& c r-a b=r^{3} \phi_{3}\left(r^{2}\right) .
\end{aligned}$$
The first of these is clear; for the second, expand to get $a / c=1+\alpha b^{2}+\mathcal{O}\left(b^{4}\right)$ for some constant $\alpha$ and $b=r+\mathcal{O}\left(r^{3}\right)$, so
$$\operatorname{cr}\left(1-\frac{a b}{c r}\right)=\operatorname{cr}\left(1-\frac{b+\alpha b^{3}+\mathcal{O}\left(b^{5}\right)}{r}\right)=r^{3} \phi_{3}\left(r^{2}\right) .$$
Therefore $\omega$ extends as a smooth form on all of $M$. \(\square\)

\subsection*{10.4. Completeness.}

Proposition 10.5. For the metrics of Proposition 10.4, all finite length curves remain inside some compact set.

Proof. For the Euclidean group
$$E(2)=\left\{\left.\left(\begin{array}{ccc}
\cos \theta & -\sin \theta & x \\
\sin \theta & \cos \theta & y \\
0 & 0 & 1
\end{array}\right) \right\rvert\, x, y, \theta \in \mathbb{R}\right\},$$
The left-invariant frame
$$X_{1}=\cos \theta \partial_{x}+\sin \theta \partial_{y}, X_{2}=\partial_{\theta}, X_{3}=-\sin \theta \partial_{x}+\cos \theta \partial_{y},$$
has dual co-frame
$$\sigma_{1}=\cos \theta d x+\sin \theta d y, \sigma_{2}=d \theta, \sigma_{3}=-\sin \theta d x+\cos \theta d y .$$
We note that in the coordinate system $(t, x, y, \theta)$ on $M=E(2) \times_{S O(2)} \mathbb{R}^{2}$, with $t \in(-\infty, \eta)$, a curve will leave every compact set only if along it, either $x$ or $y$ approach $\pm \infty$ or $t$ approaches $\eta$ (Proposition 10.4 is used to make this statement). Now a curve of finite length $\gamma: I \rightarrow M$ has length
$$L(\gamma)=\int_{I}\left|\gamma^{\prime}(u)\right| d u \geq \int_{I}\left|g\left(\gamma^{\prime}(u), v\right)\right| d u$$
for any unit vector field $v$. Employing the metric in the form (17), and choosing unit vector fields in the directions of the frame fields $\left\{\partial_{t}, X_{1}, X_{3}\right\}$ of (18), we have
$$\begin{aligned}
L(\gamma) & \geq \int_{I} a b c\left|t^{\prime}(u)\right| d u \geq\left|\int_{t(I)} a b c d t\right|, \\
L(\gamma) & \geq \int_{I} a\left|\cos (\theta(u)) x^{\prime}(u)+\sin (\theta(u)) y^{\prime}(u)\right| d u \\
& \geq q \int_{I}\left|\cos (\theta(u)) x^{\prime}(u)+\sin (\theta(u)) y^{\prime}(u)\right| d u \\
L(\gamma) & \geq \int_{I} c\left|-\sin (\theta(u)) x^{\prime}(u)+\cos (\theta(u)) y^{\prime}(u)\right| d u \\
& \geq q \int_{I}\left|-\sin (\theta(u)) x^{\prime}(u)+\cos (\theta(u)) y^{\prime}(u)\right| d u
\end{aligned}$$
Now equations (38) and (47) imply that along $\gamma, t$ is bounded away from $\eta$. Then, as $|\cos (\theta(u))| \leq 1$ and $|\sin (\theta(u))| \leq 1$, equations (48) and (49) give
$$\begin{aligned}
& L(\gamma) \geq q \int_{I}\left|\cos (\theta(u)) x^{\prime}(u)+\sin (\theta(u)) y^{\prime}(u)\right||\cos (\theta(u))| d u, \\
& L(\gamma) \geq q\left|\int_{I}\left[\cos ^{2}(\theta(u)) x^{\prime}(u)+\cos (\theta(u)) \sin (\theta(u)) y^{\prime}(u)\right] d u\right|, \\
& L(\gamma) \geq q \int_{I}\left[\cos ^{2}(\theta(u)) x^{\prime}(u)+\cos (\theta(u)) \sin (\theta(u)) y^{\prime}(u)\right] d u \geq-L(\gamma) .
\end{aligned}$$
Similarly,
$$L(\gamma) \geq q \int_{I}\left[\sin ^{2}(\theta(u)) x^{\prime}(u)-\cos (\theta(u)) \sin (\theta(u)) y^{\prime}(u)\right] d u \geq-L(\gamma) .$$

Summing these we get
$$q\left|\int_{I} x^{\prime}(u) d u\right| \leq 2 L(\gamma),$$
showing that $x$ is bounded along $\gamma$. A similar calculation shows that $y$ is bounded. Therefore $g$ is a complete metric on $M$. \(\square\)

\section*{11. Incompleteness in the Ricci flat case with $N=0$}

As mentioned in the comments of section 6, there exists a "gauge" freedom of rotating x, y in their span, which allows one to simplify the systems in Theorem 2. We now employ this for case (2) of that theorem. It can easily be shown that in the case of rotation by angle $\theta$ in $\mathcal{H}, S$ transforms to $S+2 \theta$. In this section and the next one we make the pointwise choice of the function $\theta$ that results in $S=\pi / 4$. With that choice we have the following rephrasing, but also strengthening, of part (2) of Theorem 2.

Theorem 4. Let $(M, g)$ be a Riemannian 4-manifold admitting an orthonormal frame \{k, t, x, y\} as in section 3, satisfying in particular relations (3)-(7) with $N=0$. Let $V$ be the domain of $\tau$ of (11). Then in the set $V \cap\{F+G \neq 0\}$, equations (10) hold with $\lambda=0$ if and only if, after a pointwise rotation of x, y by an appropriate angle, $P, Q, R, S, L$ of (12) satisfy the system
\begin{itemize}
\item[i)] $S=\pi / 4$,
\item[ii)] $d_{\mathbf{k}-\mathbf{t}} R=R(P+2 L), \quad$ iii) $d_{\mathbf{k}+\mathbf{t}} R=-R Q$,
\item[iv)] $d_{\mathbf{k}-\mathbf{t}} L=2 L^{2}+R^{2} / 2, \quad$ v) $d_{\mathbf{k}-\mathbf{t}} P-d_{\mathbf{k}+\mathbf{t}} Q=2 L P+2 R^{2}$,
\end{itemize}
and all $d_{\mathbf{x}}, d_{\mathbf{y}}$ derivatives of these functions vanish.
The proof of this theorem is contained in the appendix. We will also need the following lemma.

Lemma 11.1. Given vector fields $\mathbf{k}-\mathbf{t}, \mathbf{k}+\mathbf{t}$, and smooth functions $R, L$ on a given manifold, equations (50)ii)- v) hold for some smooth functions $P, Q$, and away from the zeros of $R$, if and only if (50)iv) and
$$3 R^{2}=d_{\mathbf{k}-\mathbf{t}}^{2} \log |R|+d_{\mathbf{k}+\mathbf{t}}^{2} \log |R|-2 L d_{\mathbf{k}-\mathbf{t}} \log |R|$$
hold there.
Proof. Away from the zeros of $R$, equation (51) is a direct consequence of (50)ii)-v). Conversely, given (50)iv), define $P$ and $Q$ so that (50)ii),iii) both hold whenever $R$ is nonzero. Then one easily verifies that (50)v) follows from (51) and (50)iv). \(\square\)

\subsection*{11.1. Laplace Operator.}

Proposition 11.2. For $(M, g)$ as in Theorem 4 with functions $P, Q, R, S, L$ satisfying (50), $R$ will satisfy away from its zeros
$$\Delta \log |R|=\frac{3}{2} R^{2},$$
where $\Delta$ is the Laplacian of $g$.

Proof. For a function $u$ satisfying $d_{\mathbf{x}} u=d_{\mathbf{y}} u=0$,
$$\nabla u=\left(d_{\mathbf{k}} u\right) \mathbf{k}+\left(d_{\mathbf{t}} u\right) \mathbf{t}$$
Then using $\mathcal{L}_{\mathbf{v}} d \mathrm{vol}=(\operatorname{div} \mathbf{v}) d \mathrm{vol}$ and (60) in the appendix, we get
$$\begin{aligned}
\mathcal{L}_{\nabla u} d_{\mathrm{vol}} & =d\left(\iota_{\nabla u} d_{\mathrm{vol}}\right) \\
& =d\left(\left(d_{\mathbf{k}} u\right) \hat{\mathbf{t}} \wedge \hat{\mathbf{x}} \wedge \hat{\mathbf{y}}-\left(d_{\mathbf{t}} u\right) \hat{\mathbf{k}} \wedge \hat{\mathbf{x}} \wedge \hat{\mathbf{y}}\right) \\
& =\left[d_{\mathbf{k}}^{2} u+\left(d_{\mathbf{k}} u\right)(-L-A-D)+d_{\mathbf{t}}^{2} u-\left(d_{\mathbf{t}} u\right)(-L+E+H)\right] d \mathrm{vol} \\
& =\left[d_{\mathbf{k}}^{2} u+d_{\mathbf{t}}^{2} u-\left(d_{\mathbf{k}-\mathbf{t}} u\right)(L+N)\right] d \mathrm{vol}
\end{aligned}$$
showing
$$\Delta u=d_{\mathbf{k}}^{2} u+d_{\mathbf{t}}^{2} u-\left(d_{\mathbf{k}-\mathbf{t}} u\right)(L+N)$$

But $N=0$, and Lemma 11.1 implies that $R$ satisfies away from its zeros the second order equation (51). \(\square\)
11.2. 2d Leaf Metrics. Since $\mathcal{V}=\operatorname{span}\{\mathbf{k}, \mathbf{t}\}$ is integrable, there is a foliation of $M$ with leaves tangent to $\mathcal{V}$. It is easily checked using (8) that the leaves are totally geodesic. Abusing notation, let $\hat{\mathbf{k}}$ and $\hat{\mathbf{t}}$ now be the forms pulled back to a leaf in this foliation. Then the metric induced on the leaf is just $\bar{g}=\hat{\mathbf{k}}^{2}+\hat{\mathbf{t}}^{2}$. To compute its Gauss curvature, note that
$$d\binom{\hat{\mathbf{k}}}{\hat{\mathbf{t}}}=-\binom{L \hat{\mathbf{k}} \wedge \hat{\mathbf{t}}}{L \hat{\mathbf{k}} \wedge \hat{\mathbf{t}}}=-\left(\begin{array}{cc}
0 & L(\hat{\mathbf{k}}+\hat{\mathbf{t}}) \\
-L(\hat{\mathbf{k}}+\hat{\mathbf{t}}) & 0
\end{array}\right) \wedge\binom{\hat{\mathbf{k}}}{\hat{\mathbf{t}}}$$
while (60) in the appendix implies
$$d(L(\hat{\mathbf{k}}+\hat{\mathbf{t}}))=d L \wedge(\hat{\mathbf{k}}+\hat{\mathbf{t}})-2 L^{2} \hat{\mathbf{k}} \wedge \hat{\mathbf{t}}=\left(d_{\mathbf{k}-\mathbf{t}} L-2 L^{2}\right) \hat{\mathbf{k}} \wedge \hat{\mathbf{t}},$$
showing that by (50)iv) the Gauss curvature of $\bar{g}$ is
$$K_{\bar{g}}=\frac{R^{2}}{2} .$$
This also gives the following corollary.
Corollary 11.3. A vertical leaf $(\Sigma, \bar{g})$ has Gauss curvature $K_{\bar{g}} \geq 0$ satisfying
$$\bar{\Delta} \log K_{\bar{g}}=6 K_{\bar{g}}$$
away from its zeros, where $\bar{\Delta}$ is the Laplacian of $\bar{g}$.
Proof. This holds because the leaf Laplacian is
$$\bar{\Delta} u=d_{\mathbf{k}}^{2} u+d_{\mathbf{t}}^{2} u-\left(d_{\mathbf{k}-\mathbf{t}} u\right) L .$$ \(\square\)
11.2.1. Prescribed Gauss Curvature. The conformal metric
$$e^{2 u} \bar{g}=e^{2 u}\left(\hat{\mathbf{k}}^{2}+\hat{\mathbf{t}}^{2}\right)$$
has Gauss curvature,
$$K_{e^{2 u} \bar{g}}=e^{-2 u}\left(K_{\bar{g}}-\bar{\Delta} u\right) .$$

Corollary 11.4. Whenever defined, the conformal metric $K_{\bar{g}} \bar{g}$ has constant curvature -2.

Proof. This follows immediately from the prescribed Gauss curvature equation (55) with $u=\frac{1}{2} \log K_{\bar{g}}$. \(\square\)

Proposition 11.5. Suppose that $(\Sigma, \bar{g})$ is a surface of non-negative Gauss curvature satisfying (53), then $\Sigma$ is not a complete non-flat finitely connected surface.

Proof. Suppose that $(\Sigma, \bar{g})$ is a finitely connected non-flat complete surface with $K_{\bar{g}}$ non-negative. By a result of Cecchini in [C] it is also integrable on $\tilde{\Sigma}$, and
$$\int_{\Sigma} K_{\bar{g}} d A_{\bar{g}} \leq 2 \pi .$$
But using (53), a result of Yau given in [Y, Thm. 1] implies $K_{\bar{g}}$ is not integrable, which contradicts (56). \(\square\)

The same argument would apply to any completion of $\Sigma$ by attaching a single point (corresponding to attaching a bolt to $M$ transverse to $\mathcal{V}$ ). Since the leaves are totally geodesic, if they are non-flat and finitely connected the Kähler metric on $M$ is not complete.

\section*{12. Local Ricci flat metrics with $N=0$}
12.1. Existence of leaf-like metrics. In subsection 11.2, two properties that a leaf metric was shown to have, were equation (53) for the Gauss curvature, and Corollary 11.4. We now construct metrics with these properties, which we call leaf-like metrics.

On an open set in $\mathbb{R}^{2}$, let $g_{0}$ be a flat metric, $\ell$ a positive function such that $\tilde{g}:=\ell g_{0}$ is a hyperbolic metric of constant curvature -2, and $h$ a harmonic function. Define
$$\bar{g}=\ell^{-1 / 2} e^{-h} g_{0} .$$
This metric has Gauss curvature
$$K_{\bar{g}}=\frac{\Delta_{0}\left(\log \left(\ell^{-1 / 2} e^{-h}\right)\right)}{-2 \ell^{-1 / 2} e^{-h}}=-\frac{1}{2} e^{h} \ell^{1 / 2}\left(\frac{-\Delta_{0} \log \ell}{2}\right)=-\frac{1}{2} e^{h} \ell^{1 / 2}(-2 \ell)=e^{h} \ell^{3 / 2} .$$
Thus $K_{\bar{g}}>0$ and $K_{\bar{g}} \bar{g}=\tilde{g}$ is the hyperbolic metric. On the other hand the standard formula relating the Laplacians of $\bar{g}$ and $g_{0}$ gives
$$\bar{\Delta} \log K_{\bar{g}}=\ell^{1 / 2} e^{h} \Delta_{0}\left(\log \left(e^{h} \ell^{3 / 2}\right)\right)=\frac{3}{2} \ell^{1 / 2} e^{h} \Delta_{0}(\log \ell)=\frac{3}{2} \ell^{1 / 2} e^{h}(4 \ell)=6 K_{\bar{g}} .$$

Our final theorem is as follows.

Theorem 5. Given a leaf-like metric $\bar{g}=\bar{g}\left(l, h, g_{0}\right)$, there exist a four-dimensional local Kähler Ricci-flat metric $g$ with a totally-geodesic two-dimensional foliation whose leaves are isometric to $\bar{g}$. The dimension of the Lie algebra of Killing fields of $g$ is at least 2.

The proof of this theorem will be given in the rest of this section. Note that we have already shown examples of such metrics in section 8, with a 3-dimensional Lie algebra of Killing fields. However for non-trivial harmonic functions $h$, or more precisely whenever $\ell^{-1 / 2} e^{-h}$ depends non-trivially on two coordinate functions, the dimension will drop to 2.
12.2. Coordinates for a leaf-like metric leading to equations (50). We introduce a coordinate representation for a given leaf metric in preparation for exhibiting a coordinate representation for $g$.

Let $\bar{g}$ be a leaf-like metric with Gauss curvature $K_{\bar{g}}$ on an open set in $\mathbb{R}^{2}$. Since $K_{\bar{g}}>0$, the metric $\bar{g}$ is locally embeddable in $\mathbb{R}^{3}$ and hence admits geodesic parallel coordinates. Choose a "homothetic" version $x, y$ of these coordinates with domain $U_{1}$, in which the metric takes the form:
$$\bar{g}=2\left(d x^{2}+c^{2} d y^{2}\right)$$
for some nowhere vanishing $c=c(x, y)$. Then $K_{\bar{g}}=-c_{x x} / c$, so define
$$R:=\sqrt{-2 c_{x x} / c} .$$
Next, define vector fields $\mathbf{k}, \mathbf{t}$ by the formulas $\mathbf{k}-\mathbf{t}:=\partial_{x}, \mathbf{k}+\mathbf{t}:=\frac{1}{c} \partial_{y}$, so that $\bar{g}=2\left(\widehat{\mathbf{k}-\mathbf{t}}^{2}+\widehat{\mathbf{k}+\mathbf{t}}^{2}\right)=\hat{\mathbf{k}}^{2}+\hat{\mathbf{t}}^{2}$.

Now let $L:=-c_{x} /(2 c)$. It is then easy to check that $[\mathbf{k}, \mathbf{t}]=\mathrm{L}(\mathbf{k}+\mathbf{t})$, and equation (50)iv) holds. Furthermore, as $R^{2} / 2=K_{\bar{g}}$ solves (53), and one can verify formula (54) for the Laplacian, it follows that equation (51) also holds in the coordinate domain $U_{1}$.

It thus follows from lemma 11.1 that equations (50) hold there as well, for $S=\pi / 4$ and $P, Q$ whose formulas in terms of $c$ are
$$P=\frac{1}{2}\left(\log \frac{-c_{x x}}{c}\right)_{x}+\frac{c_{x}}{c}, \quad Q=-\frac{1}{2 c}\left(\log \frac{-c_{x x}}{c}\right)_{y} .$$
12.3. Coordinates for $g$. For $P, Q, R$ as in (58), (57), set
$$\begin{array}{ll}
\alpha:=R / \sqrt{2}, & \beta:=Q / 2, \\
\nu:=P / 2+R / \sqrt{2}, & \chi:=-P / 2+R / \sqrt{2},
\end{array}$$
which are smooth functions in $U_{1}$.
Let $U_{2}$ be an open set in the plane with coordinates $u, v$ so that $M:=U_{1} \times U_{2}$ has coordinates $x, y, u, v$. Define on $M$ vector fields
$$\begin{array}{ll}
\mathbf{k}-\mathbf{t}=\partial_{x}, & \mathbf{k}+\mathbf{t}=(1 / c) \partial_{y}, \\
\mathbf{x}=a \partial_{u}+b \partial_{v}, & \mathbf{y}=r \partial_{u}+s \partial_{v},
\end{array}$$
where $c=c(x, y)$ is as in subsection 12.2, and $a, b, r, s$ are functions of $x, y$ which are solutions to the system
$$\begin{array}{ll}
a_{x}=\alpha a+\beta r, & r_{x}=-\beta a-\alpha r, \\
b_{x}=\alpha b+\beta s, & s_{x}=-\beta b-\alpha s, \\
a_{y} / c=\nu r, & r_{y} / c=\chi a, \\
b_{y} / c=\nu s, & s_{y} / c=\chi b .
\end{array}$$
We need to verify that solutions to this overdetermined elliptic system exist, and we will do so via elementary means. Note that the eight equations in (59) decouple in pairs, line by line, and partial integration of each pair is equivalent to solving at most a second order linear equation in one of the two unknowns of the pair. For example, for the first line in (59), if $\beta$ is nowhere vanishing the two equations resolve to $a_{x x}-\left(\beta_{x} / \beta\right) a_{x}+\left(\beta\left(\beta-\alpha^{2}\right)+\alpha \beta_{x} / \beta-\alpha_{x}\right) a=0$ and $r=\left(a_{x}+\alpha a\right) / \beta$. Regarding the former equation as an ODE for fixed $y$, its smooth coefficients guarantee local existence. Note that $\beta=0$, which is the case where $c$ depends only on $x$, examples of which have been given in section 8, is even simpler as $a$ and $r$ completely decouple.