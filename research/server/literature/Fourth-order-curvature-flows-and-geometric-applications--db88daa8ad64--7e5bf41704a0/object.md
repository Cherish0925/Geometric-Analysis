# Fourth order curvature flows and geometric applications

- Category: papers
- Identity: doi:10.48550/arxiv.1012.0342
- Content status: fulltext_ok

---

---
source_file: 1012_0342v1.pdf
converter: mathpix
format: mmd
---

\title{
Fourth order curvature flows and geometric applications
}

\author{
Vincent Bour*
}

December 2010

\begin{abstract}
We study a class of fourth order curvature flows on a compact Riemannian manifold, which includes the gradient flows of a number of quadratic geometric functionals, as for instance the $L^{2}$ norm of the curvature.

Such flows can develop a special kind of singularities, that could not appear in the Ricci flow, namely singularities where the manifold collapses with bounded curvature. We show that this phenomenon cannot occur if we assume a uniform positive lower bound on the Yamabe invariant.

In particular, for a number of gradient flows in dimension four, such a lower bound exists if we assume a bound on the initial energy. This implies that these flows can only develop singularities where the curvature blows up, and that blowing-up sequences converge (up to a subsequence) to a "singularity model", namely a complete Bach-flat, scalar-flat manifold.

We prove a rigidity result for those model manifolds and show that if the initial energy is smaller than an explicit bound, then no singularity can occur. Under those assumptions, the flow exists for all time, and converges up to a subsequence to the sphere or the real projective space.

This gives an alternative proof, under a slightly stronger assumption, of a result from Chang, Gursky and Yang asserting that integral pinched 4-manifolds with positive Yamabe constant are space forms.
\end{abstract}

\section*{1 Introduction}

The analysis of fourth and higher order partial differential equations is a subject of rising interest in Riemannian geometry. This interest is motivated by the successful resolution of a number of key issues involving second order equations, such as the Yamabe problem and the prescribed scalar curvature problem, which are linked to an elliptic second order equation, and evolution problems such as the Ricci flow, the mean curvature flow, or the Yamabe flow. These problems, which have motivated the development of geometric analysis, have higher order counterparts, and it is natural to wonder how far the known results extend. Moreover, if a number of second order equations are now very well understood in dimensions two and three, it seems that in higher dimensions, equations of higher order behave better, because they are more suited to the context, or carry more regularity. For example, it appears that a lot of second order issues are in some way related to the Einstein-Hilbert functional, a crucial invariant for surfaces. The Yamabe problem consists in minimizing this functional in a given conformal class, and the Ricci flow can be seen as its gradient flow, by adding extra dimensions or by keeping a measure fixed (see [CCD ${ }^{+}$10] and [Per02]).

\footnotetext{
*Institut Fourier, Université Grenoble 1
100 rue des Maths, BP 74, 38402 St Martin d'Hères, France
e-mail: vincent.bour@ujf-grenoble.fr
}

In the same spirit, fourth order equations often appear in relation with some quadratic curvature functional, linear combination of:
$$\mathcal{F}_{R m}(g)=\int_{M}\left|R m_{g}\right|^{2} d v_{g}, \quad \mathcal{F}_{R i c}(g)=\int_{M}\left|R i c_{g}\right|^{2} d v_{g} \quad \text { and } \quad \mathcal{F}_{R}(g)=\int_{M} R_{g}^{2} d v_{g},$$
or equivalently of:
$$\mathcal{F}_{W}(g)=\int_{M}\left|W_{g}\right|^{2} d v_{g}, \quad \mathcal{F}_{\text {Ric }}^{\circ}(g)=\int_{M}\left|\stackrel{\circ}{R i c_{g}}\right|^{2} d v_{g} \quad \text { and } \quad \mathcal{F}_{R}(g)=\int_{M} R_{g}^{2} d v_{g},$$
where $\mathrm{Rm}_{g}, \mathrm{~W}_{g}, \stackrel{\circ}{\mathrm{Ric}_{g}}$ and $\mathrm{Ric}_{g}$ are respectively the Riemann, Weyl, traceless Ricci and Ricci curvature tensors, $R_{g}$ is the scalar curvature, and the norms are taken by considering them as double-forms (see section 9.1), e.g. $|R m|^{2}=\frac{1}{4} R m_{i j k l} R m^{i j k l}$ and $|R i c|^{2}=R i c_{i j} R i c^{i j}$.

Let also define:
$$\mathcal{F}_{2}(g)=\frac{n}{8(n-1)} \mathcal{F}_{R}(g)-\frac{1}{2} \mathcal{F}_{R i c}(g)=\int_{M} \sigma_{2}\left(A_{g}\right) d v_{g},$$
where $A_{g}=\operatorname{Ric}_{g}-\frac{1}{2(n-1)} R_{g} g$ is the Weyl-Schouten tensor and $\sigma_{2}(h)=\frac{1}{2}\left(\operatorname{tr}(h)^{2}-|h|^{2}\right)$ is the second symmetric function of the eigenvalues of a symmetric 2-tensor $h$. The quantity $\sigma_{2}$ plays an important role in conformal geometry, see for example [Via06].

These functionals are particularly interesting in dimension four, as it is the only dimension for which they are scale invariant. Following Berger's idea of finding best metrics on a manifold $M$ by minimizing $\int_{M}|R m|^{\frac{n}{2}} d v_{g}$, LeBrun initiated the study of minimizers of $\mathcal{F}_{R m}$ in dimension four ([LeB04]). There has also been much work lately on critical metrics for these functionals, which are solutions of quasilinear fourth order equations. In dimension four, in particular, much attention is paid to the gradient of $\mathcal{F}_{W}$ known as the Bach tensor. Note that for this particular dimension, according to the Gauss-Bonnet formula:
$$\mathcal{F}_{W}-\frac{1}{2} \mathcal{F}_{R i c}+\frac{1}{24} \mathcal{F}_{R}=8 \pi^{2} \chi(M),$$
where $\chi(M)$ denotes the Euler-Poincaré characteristic of $M$, and it follows that $\mathcal{F}_{W}$ and $-\mathcal{F}_{2}$ only differ by a constant and are both conformal invariants. We can also write $\mathcal{F}_{2}(g)=\int_{M} Q_{g} d v_{g}$ where $\left.Q_{g}=\frac{1}{6} \Delta R_{g}+\frac{1}{6} R_{g}^{2}-\frac{1}{2} \right\rvert\,$ Ric $\left.\right|^{2}$ is the Q-curvature of Branson, which has good conformal properties (see [Cha04]).

If Einstein metrics are the only critical points for the normalized Einstein-Hilbert functional, there is another important class of metrics in dimension four, namely the scalar-flat anti-self-dual one, that are critical for quadratic functionals. It would suggest that those functionals do not carry as much rigidity as the Einstein-Hilbert one. However, in dimension three, Gursky and Viaclovsky proved that the critical points for $\mathcal{F}_{2}=\frac{3}{16} \mathcal{F}_{R}-\frac{1}{2} \mathcal{F}_{\text {Ric }}$ with $\mathcal{F}_{2}(g) \geq 0$ are exactly the constant curvature metrics ([GV01]).

In dimensions greater than five, there is no information to wait from minimizers, as there exists metrics of volume 1 on any manifold such that the functional $\mathcal{F}_{R m}$ is arbitrarily small (see [Ber02] section 11.3.3).

Given the spectacular advances made on the Ricci flow, a natural approach to obtain critical metrics consists in performing the gradient flow associated to the functional. Several higher order gradient flows have been successfully carried out during the last decade. In addition to the flows on curves and surfaces, Mantegazza has studied flows of four and higher order on immersed hypersurfaces in [Man02], Brendle has introduced a fourth order equivalent of the Yamabe conformal flow in [Bre03], Chen and He have obtained results for the Calabi flow on Kähler manifolds in [CH08]. As for the
gradient flows of the quadratic functionals we are interested in, Zheng has considered the gradient flow of $\mathcal{F}_{\text {Ric }}$ in dimension three in [Zhe03], and Streets has studied the gradient flow of $\mathcal{F}_{R m}$ in dimension four in [Str08].

The results obtained by Mantegazza in [Man02], where he was motivated by approximating singular flows by higher order ones, suggest that it is useful to increase the order of the equation with the dimension in order to get regularity. Indeed, for his class of flows, he showed that singularities cannot occur provided that the order of the equation is larger than $2([n / 2]+1)$.

In this paper, we study a class of fourth order flows on compact manifolds, which includes the gradient flows for quadratic curvature functionals whose gradient becomes strongly elliptic when the DeTurck trick is applied, and in particular, it includes the flows of Zheng and Streets.

Some of the ideas and tools used to study the Ricci flow naturally extend to these higher order flows. We prove short-time existence using the DeTurck trick, and prove Bando-Bernstein-Shi type estimates in order to study singularities. The lack of maximum principle for fourth order equations is overcome by an extensive use of integral estimates. Then $C^{0}$ estimates come from Sobolev inequalities.

Since we have to bound a Sobolev constant along the flow in order to get the estimates, a special kind of singularity can appear, where the injectivity radius goes to zero while the curvature stays bounded. This could not happen in the Ricci flow, for which the curvature blows up at any singularity.

This phenomenon of collapsing with bounded curvature can also appear for sequences of renormalized flows near a point where the curvature blows up. It has been ruled out for the Ricci flow by the non-collapsing result of Perelman (see [Per02]), that ensures that it is always possible to take a limit of such blowing-up sequences. But in our situation, we have no entropy similar to that of Perelman for the Ricci flow. Moreover, none of the methods used to study other higher order flows apply in this setting. For instance, the universal Sobolev-type inequality of Michael and Simon used by Mantegazza only works in the context of hypersurfaces.

The only situation in which it was possible to rule out collapsing with bounded curvature is when the flow starts very close (in the $L^{2}$ sense) to a flat metric or to the sphere:

Theorem 1.1 (Streets, [Str09]). For all positive constants $C$ and $K$, there exists a positive constant $\epsilon(C, K)$ such that if $(M, g)$ is a compact Riemannian 4-manifold with $\operatorname{Vol}_{g}(M)=1, C_{S}<C$, $\left|\nabla \mathcal{F}_{R m}\right|_{H_{1}^{2}} \leq K$ and $\mathcal{F}_{R m}(g) \leq \epsilon$, then the gradient flow of $\mathcal{F}_{R m}$ starting from $g$ exists for all time and converges exponentially fast to a flat metric.

In the theorem, $C_{S}$ denotes the Sobolev constant defined by:
$$C_{S}=\inf \left\{C \in \mathbb{R},|u|_{4} \leq C\left(|\nabla u|_{2}+\operatorname{Vol}_{g}(M)^{-\frac{1}{4}}|u|_{2}\right), \forall u \in H_{1}^{2}(M)\right\} .$$

We recall that if $(M, g)$ is a complete Riemannian $n$-manifold, $n \geq 3$, the Yamabe invariant of $(M,[g])([g]$ conformal class of $g)$ is defined by:
$$Y_{g}=\inf \left\{\int_{M}|\nabla u|_{g}^{2}+\frac{n-2}{4(n-1)} R_{g} u^{2} d v_{g}, u \in H_{1}^{2}(M),|u|_{\frac{2 n}{n-2}}=1\right\} .$$
If $M$ is compact, then $Y_{g}>-\infty$ and
$$Y_{g}=\frac{n-2}{4(n-1)} \inf \left\{\operatorname{Vol}_{g}(M)^{\frac{2-n}{n}} \int_{M} R_{\tilde{g}} d v_{\tilde{g}}, \tilde{g} \in[g]\right\} .$$

Theorem 1.2 (Streets, [Str10]). There exists a constant $\epsilon>0$ such that if $(M, g)$ is a compact Riemannian 4-manifold satisfying
$$Y_{g}>0 \quad \text { and } \quad \mathcal{F}_{W}(g)+\frac{1}{2} \mathcal{F}_{\text {Ric }}(g) \leq \epsilon \chi(M),$$
then the gradient flow of $\mathcal{F}_{R m}$ starting from $g$ exists for all time and converges exponentially fast to either the sphere or the real projective space.

In this paper, we deal with the issue of collapsing with bounded curvature by controlling the Yamabe invariant. When we assume a positive lower bound on it, the metric cannot collapse with bounded curvature. Moreover, if the curvature blows up, we show that we can apply a compactness result to a sequence of renormalized flows near a singularity, and prove that a subsequence converges to a "singularity model".

In particular, in dimension four, such a positive lower bound exists on the Yamabe invariant as soon as the Yamabe invariant and the mean Q-curvature are positive, as it was pointed out by Streets in [Str10]. We show that these conditions are uniformly satisfied for the gradient flows of a number of quadratic functionals, assuming a bound on the initial energy.

It implies that these flows only develop singularities where the curvature blows up, and that blowing-up sequences converge (up to a subsequence) to a "singularity model", namely a complete Bach-flat, scalar-flat manifold.

Moreover, we prove a rigidity result for those model manifolds and show that if the initial energy is less than an explicit bound, then no singularity can occur. Under those assumptions, the flow exists for all time, and converges up to a subsequence to the sphere or the real projective space.

In [CGY03], Chang, Gursky and Yang proved the following result for pinched 4-manifolds:
Theorem 1.3. Let $(M, g)$ be a compact Riemannian 4-manifold. If $Y_{g}>0$ and
$$\mathcal{F}_{W}(g)<4 \pi^{2} \chi(M),$$
then $M$ is diffeomorphic to $S^{4}$ or $\mathbb{R} P^{4}$.
Note that according to the Gauss-Bonnet formula, the pinching assumption in this theorem can also be written:
$$\mathcal{F}_{W}(g)+\frac{1}{2} \mathcal{F}_{R i c}(g)<\frac{1}{24} \mathcal{F}_{R}(g) .$$

This theorem is a "conformal" version of a result due to Margerin ([Mar98]). As a matter of fact, the assumptions in the theorem of Chang, Gursky and Yang do not depend on the metric we choose on the conformal class of the initial metric. This fact allows them to perform a conformal transformation on the initial metric in order to exhibit a metric in the same conformal class which satisfies the pointwise pinching of Margerin. This is done by using some fully nonlinear equations. Despite the fact that Margerin's result is based on the Ricci flow to produce a metric of constant curvature, Chang, Gursky and Yang don't provide a direct proof of the existence of such a metric.

In this article, we give a direct proof of the existence of a metric of constant curvature under slightly stronger assumptions (see Corollary 1.14). Our proof is more natural as it only relies on the study of a geometric flow.

The structure of the paper is the following. In the rest of the introduction, we present our results. In section 2, we prove short-time existence for the flows we introduce. In section 3, we show that the gradient flows of quadratic functionals belong to our class of equations. In section 4, we prove a rigidity result in dimension four for metrics that are critical for the functionals $\mathcal{F}^{\alpha}$ defined in the introduction. In section 5, we prove that collapsing with bounded curvature cannot occur if the Yamabe constant is bounded away from zero. In section 6, we prove Bando-Bernstein-Shi type estimates on the curvature. In section 7 we present a compactness result for the solutions of our flows. In section 8, we prove the main results of the paper. Finally, section 9 is devoted to some technical results, useful all along the paper, and which are not directly specific to geometric flows.

Acknowledgments: The author is grateful to Carlo Mantegazza, Zindine Djadli for his constant support and Thomas Richard for helpful discussions. Thanks also to the Scuola Normale Superiore di Pisa and the Centro di Ricerca di Matematica Ennio de Giorgi for the hospitality.

The author is partially supported by the ANR project "Flots et opérateurs géométriques" (FOG) ANR-07-BLAN-0251-01.

\subsection*{1.1 General results}

Let denote the space of symmetric (2,0)-tensors by $\mathcal{S}^{2}(M)$ and the space of metrics by $\mathcal{S}_{+}^{2}(M)$. Given a compact Riemannian $n$-manifold $\left(M, g_{0}\right)$, we consider evolution equations of the following type:
$$\left\{\begin{aligned}
\partial_{t} g & =P(g) \\
g(0) & =g_{0},
\end{aligned} \quad\left(E_{P}\left(g_{0}\right)\right)\right.$$
where $P: \mathcal{S}_{+}^{2}(M) \rightarrow \mathcal{S}^{2}(M)$ is a smooth map of the form
$$P(g)=\delta \tilde{\delta} R m_{g}+a \Delta R_{g} g+b \nabla^{2} R_{g}+R m_{g} * R m_{g},$$
with $a<\frac{1}{2(n-1)}$ and $b \in \mathbb{R}$
We write $\delta \tilde{\delta} R m_{g}$ for $\nabla^{\alpha} \nabla^{\beta} R m_{\alpha i \beta j}$ and $S * T$ denotes any linear combination (with coefficients independent of the metric) of terms obtained from $S \otimes T$ by taking tensor products with $g$ and $g^{-1}$, contracting and permuting indices.

The gradient flows for most of the quadratic functionals generated by those in (1) or (2) are of this type (see section 3 for details). The assumption $a<\frac{1}{2(n-1)}$ is necessary for $P$ to become strongly elliptic when the DeTurck trick is applied (see section 2).

For this class of flows, we first prove short-time existence and integral estimates:
Theorem 1.4 (Short-time existence). Let $\left(M, g_{0}\right)$ be a compact Riemannian manifold.
Let $P: \mathcal{S}_{+}^{2}(M) \rightarrow \mathcal{S}^{2}(M)$ be a smooth map of the form
$$P(g)=\delta \tilde{\delta} R m_{g}+a \Delta R_{g} g+b \nabla^{2} R_{g}+R m_{g} * R m_{g},$$
with $a<\frac{1}{2(n-1)}$ and $b \in \mathbb{R}$. There exists a unique maximal solution $\left(g_{t}\right)$ to $E_{P}\left(g_{0}\right)$ defined on an interval $[0, T)$, with $T$ positive.

Theorem 1.5 (Bando-Bernstein-Shi estimates). Let $\left(M, g_{0}\right)$ be a compact Riemannian $n$-manifold, $n \geq 3$. Let $P: \mathcal{S}_{+}^{2}(M) \rightarrow \mathcal{S}^{2}(M)$ be a smooth map of the form
$$P(g)=\delta \tilde{\delta} R m_{g}+a \Delta R_{g} g+b \nabla^{2} R_{g}+R m_{g} * R m_{g},$$
with $a<\frac{1}{2(n-1)}$ and $b \in \mathbb{R}$. Let $g_{t}, t \in[0, T)$, be a solution of $E_{P}\left(g_{0}\right)$ such that $\mid$ Rm $\left._{g_{t}}\right|_{\infty}$ is uniformly bounded by some constant $D$. For all $k \in \mathbb{N}$, there exists $C(n, P, k)$ such that for all $t$ in $(0, T)$ :
$$\int_{M}\left|\nabla^{2 k} R m_{g_{t}}\right|_{g_{t}}^{2} d v_{g_{t}} \leq \mathcal{F}_{R m}\left(g_{0}\right) \frac{e^{C(1+D)(1+D t)^{k+1}}}{t^{k}} .$$

When a singularity appears, there exists schematically two possibilities: either the curvature blows up, or the injectivity radius goes to zero while the curvature stays bounded. This was proven by Zheng and Streets for their respective flows.

We provide here a similar result for more general flows:
Definition 1.6. Let $\left(g_{i}\right)_{i \in I}$ be a family of complete metrics on a manifold $M$. We say that the family collapses with bounded curvature if it has a uniform $C^{0}$ bound on curvature and if it satisfies one of the three equivalent assertions:
\begin{itemize}
\item[(i)] $\quad \inf _{i \in I} \operatorname{inj}_{M}\left(g_{i}\right)=0$,
\item[(ii)] $\inf _{i \in I} \inf _{x \in M} \operatorname{Vol}_{g_{i}}\left(B_{x}(1)\right)=0$,
\item[(iii)] $\forall A \in \mathbb{R} \sup _{i \in I}\left(\mathcal{B}_{A}\left(g_{i}\right)\right)=\infty$.
\end{itemize}

Here $\mathcal{B}_{A}$ is the best second Sobolev constant relative to $A$ (See definition 5.1). See Proposition 5.3 for a proof of the equivalence.

Theorem 1.7. Let $\left(M, g_{0}\right)$ be a compact Riemannian $n$-manifold, $n \geq 3$.
Let $g_{t}, t \in[0, T)$ be the maximal solution of $E_{P}\left(g_{0}\right)$. One of the following situations occurs:
\begin{itemize}
\item[1.] The flow exists for all time (i.e. $T=\infty$ ).
\item[2.] A finite time singularity occurs, where the curvature blows up:
$$T<\infty \quad \text { and } \quad \varlimsup_{t \rightarrow T}\left|R m_{g_{t}}\right|_{\infty}=\infty,$$
\item[3.] A finite time singularity occurs, where the metric collapses with bounded curvature.
\end{itemize}

To rule out collapsing with bounded curvature, we want to control some Sobolev constant along the flow. This is possible when the Yamabe invariant remains uniformly positive:

Theorem 1.8. Let $\left(M, g_{0}\right)$ be a compact Riemannian $n$-manifold, $n \geq 3$.
Let $g_{t}, t \in[0, T)$ be the maximal solution of $E_{P}\left(g_{0}\right)$.
Suppose that there exists some $Y_{0}>0$ such that $Y_{g_{t}} \geq Y_{0}$ for all $t \in[0, T)$.
Then either the flow exists for all time, or the curvature blows up:
$$T<\infty \Rightarrow \varlimsup_{t \rightarrow T}\left|R m_{g_{t}}\right|_{\infty}=\infty .$$

Then, when a singularity occurs, we would like to zoom in a region where the curvature blows up and, as the assumption on the Yamabe constant implies that the injectivity radius remains positively bounded from below, to obtain a "singularity model" at the limit.

For the Ricci flow, as we can get pointwise estimates by the maximum principle, the curvature is bounded in $C^{k}$ norm as soon as it is in $C^{0}$ norm. Here, the use of integral estimates makes $C^{k}$ curvature bounds also depend on the initial $L^{2}$ norm of the curvature. This dependence becomes important when we apply the estimates to a sequence of renormalized solutions near a singular time. Indeed, in this case, the initial metrics of the solutions we consider are in fact scalings of metrics $g_{t}$ with $t$ going to $T$. This fact forces us to control $\mathcal{F}_{R m}$ in the following way along the flow:
$$\left|R m_{g_{t}}\right|_{2} \leq C\left(1+\left|R m_{g_{t}}\right|_{\infty}\right)^{1-\frac{n}{4}},$$
in order to get $C^{k}$ estimates on the curvature of such sequences, and then to apply a compactness theorem. This will put strong restrictions on the equations we can deal with. For example, we couldn't get the control for $P(g)=-\nabla \mathcal{F}_{W}+F(g) g$ where $F(g) g$ is a conformal term added to the Bach flow in order to get strong ellipticity. This also explains why we should restrict ourselves to low dimensions when it comes to study singularities, so that we only have to obtain a constant bound on $\mathcal{F}_{R m}$.

Theorem 1.9. Let $\left(M, g_{0}\right)$ be a compact Riemannian $n$-manifold, $n=3$ or 4 .
Let $g_{t}, t \in[0, T)$ be the maximal solution of $E_{P}\left(g_{0}\right)$.
Suppose that there exists some $Y_{0}>0$ and $C<\infty$ such that $Y_{g_{t}} \geq Y_{0}$ and $\left|R m_{g_{t}}\right|_{2} \leq C$ for all $t \in[0, T)$. Then one of the following situations occurs:
\begin{itemize}
\item[1.] The flow exists for all time with uniform $C^{k}$ curvature bounds and the metric doesn't collapse with bounded curvature.
Then, for all sequences ( $t_{i}, x_{i}$ ) with $t_{i} \rightarrow \infty$, we can extract a subsequence such that ( $M, g_{t_{i}}, x_{i}$ ) converges to a pointed manifold $\left(M_{\infty}, g_{\infty}, x_{\infty}\right)$ in the pointed $C^{\infty}$ topology.
\end{itemize}
\begin{itemize}
\item[2.] A finite or infinite time singularity occurs, where the curvature blows up: for all $p$ in $\left(\frac{n}{2}, \infty\right]$,
$$\varlimsup_{t \rightarrow T}\left|R m_{g_{t}}\right|_{p}=\infty .$$
Moreover, there exists a sequence $\left(t_{i}, x_{i}\right)_{i \geq 0}$ such that $t_{i} \rightarrow T$ and
$$\left(M,\left|R m_{g_{t_{i}}}\right|_{\infty} g_{t_{i}}, x_{i}\right)$$
converges to a non-flat complete Riemannian manifold in the pointed $C^{\infty}$ topology.
\end{itemize}

Remark 1.10. If $n=3$, we can replace the assumption $\left|R m_{g_{t}}\right|_{2} \leq C$ by the weaker one $\left|R m_{g_{t}}\right|_{2} \leq$ $C\left(1+\left|R m_{g_{t}}\right|_{\infty}\right)^{\frac{1}{4}}$.

\subsection*{1.2 Application to 4-dimensional gradient flows}

In dimension 4, the Yamabe invariant can be kept away from zero by a number of gradient flows, what prevents the metric from collapsing with bounded curvature. This fact allows us to describe the singularities by a "blow-up".

For $\alpha \geq 0$, let define:
$$\mathcal{F}^{\alpha}(g)=(1-\alpha) \mathcal{F}_{W}+\frac{\alpha}{2} \mathcal{F}_{\text {Ric }},$$
and
$$\left\{\begin{aligned}
\partial_{t} g & =-2 \nabla \mathcal{F}^{\alpha}(g) \\
g(0) & =g_{0}
\end{aligned} \quad\left(E_{4}^{\alpha}\left(g_{0}\right)\right)\right.$$

Short-time existence is supplied by Theorem 1.4 provided $\alpha>0$. The case $\alpha=1$ corresponds (according to the Gauss-Bonnet formula) to the gradient flow of $\mathcal{F}_{R m}$.

Theorem 1.11. Let $\alpha$ be in $(0,1)$. Let $\left(M, g_{0}\right)$ be a compact Riemannian 4-manifold such that $Y_{g_{0}}>0$ and $\mathcal{F}^{\alpha}\left(g_{0}\right) \leq(1-\alpha) 8 \pi^{2} \chi(M)$.

Let $g_{t}, t \in[0, T)$ be the maximal solution of $E_{4}^{\alpha}\left(g_{0}\right)$. Then one of the following situations occurs:
\begin{itemize}
\item[1.] The flow exists for all time with uniform $C^{k}$ curvature bounds and the metric doesn't collapse with bounded curvature.
Moreover, there exists a sequence $\left(t_{i}\right)$ with $t_{i} \rightarrow \infty$, such that $g_{t_{i}}$ converges in the $C^{\infty}$ topology to a metric $g_{\infty}$, which is critical for $\mathcal{F}^{\alpha}$ (i.e. $\nabla \mathcal{F}^{\alpha}\left(g_{\infty}\right)=0$ ).
\item[2.] A finite or infinite time singularity occurs, where the curvature blows up: for all $p$ in $(2, \infty]$,
$$\varlimsup_{t \rightarrow T}\left|R m_{g_{t}}\right|_{p}=\infty .$$
Moreover, there exists a sequence $\left(t_{i}, x_{i}\right)_{i \geq 0}$ such that $t_{i} \rightarrow T$ and
$$\left(M,\left|R m_{g_{t_{i}}}\right|_{\infty} g_{t_{i}}, x_{i}\right)$$
converges to a complete non-compact non-flat Bach-flat, scalar-flat Riemannian manifold in the pointed $C^{\infty}$ topology.
\end{itemize}

Note that the condition $\mathcal{F}^{\alpha}\left(g_{0}\right) \leq(1-\alpha) 8 \pi^{2} \chi(M)$ is equivalent to an integral pinching between the scalar curvature and the traceless Ricci tensor:
$$\mathcal{F}^{\alpha}\left(g_{0}\right) \leq(1-\alpha) 8 \pi^{2} \chi(M) \Leftrightarrow \int_{M}|\stackrel{\circ}{R i c}|^{2} d v_{g} \leq \frac{1-\alpha}{12} \int_{M} R^{2} d v_{g} .$$

When $\alpha=1$, the theorem remains true but becomes useless, as the assumption $\mathcal{F}^{1}\left(g_{0}\right) \leq(1-$ $\alpha) 8 \pi^{2} \chi(M)$ is only satisfied by Einstein metrics.

We prove the following rigidity result for the singularity models:
Theorem 1.12. Let $(M, g)$ be a complete Riemannian 4-manifold with positive Yamabe constant and let $\alpha$ be in $[0,1]$. Suppose that $R_{g}$ is in $L^{2}(M)$. If $\alpha=0$, suppose that $R_{g}$ is constant.

If $g$ is a critical metric of $\mathcal{F}^{\alpha}$ with
$$\mathcal{F}_{W}(g)+\frac{1}{4} \mathcal{F}_{\text {Ric }}(g)<\frac{3}{16} Y_{g}^{2},$$
then $g$ is of constant sectional curvature.
Particular cases of this theorem have already been given by Kim in [Kim10] when $\alpha=0$ and $M$ is not compact (i.e. for non-compact Bach-flat manifolds), and by Streets in [Str10] when $\alpha=1$ (see Gap Theorems I and II of his paper).

However, in these papers, the pinching hypothesis lies in the following form:
$$\mathcal{F}_{W}(g)+\frac{1}{2} \mathcal{F}_{\text {Ric }}(g) \leq \epsilon,$$
with $\epsilon$ a non-explicit constant depending on the Yamabe constant or the Sobolev constant. Here, we obtain such a result with an explicit pinching (and for a larger class of functionals).

Theorem 1.12 implies that if the initial energy is not too large, then no singularity can appear along the flow:

Theorem 1.13. Let $\left(M, g_{0}\right)$ be a compact Riemannian 4-manifold and let $\alpha$ be in (0, 1). If $Y_{g_{0}}>0$ and
$$\left\{\begin{array} { r l } 
{ \alpha } & { \leq \frac { 4 } { 1 3 } } \\
{ \mathcal { F } ^ { \alpha } ( g _ { 0 } ) } & { < 2 \alpha \pi ^ { 2 } \chi ( M ) }
\end{array} \quad \text { or } \quad \left\{\begin{array}{rl}
\alpha & \geq \frac{4}{13} \\
\mathcal{F}^{\alpha}\left(g_{0}\right) & <\frac{8}{9}(1-\alpha) \pi^{2} \chi(M),
\end{array}\right.\right.$$
then the solution of $E_{4}^{\alpha}\left(g_{0}\right)$ exists for all time and there exists a sequence $\left(t_{i}\right)$ such that $g_{t_{i}}$ converges in the $C^{\infty}$ topology to the sphere or the real projective space.

Taking $\alpha=\frac{4}{13}$ in the previous theorem, we obtain the following result:
Corollary 1.14. Let $\left(M, g_{0}\right)$ be a compact Riemannian 4-manifold. If $Y_{g_{0}}>0$ and
$$\mathcal{F}_{W}\left(g_{0}\right)+\frac{2}{9} \mathcal{F}_{\text {Ric }}\left(g_{0}\right)<\frac{8}{9} \pi^{2} \chi(M),$$
then $M$ is diffeomorphic to $S^{4}$ or $\mathbb{R} P^{4}$.
According to the Gauss-Bonnet formula, the pinching assumption is equivalent to:
$$\mathcal{F}_{W}\left(g_{0}\right)+\frac{5}{16} \mathcal{F}_{\stackrel{\circ}{R i c}}\left(g_{0}\right)<\frac{1}{8 \times 24} \mathcal{F}_{R}\left(g_{0}\right) .$$

Corollary 1.14 can also be reformulated in the following way, which has the nice property of being conformally invariant:

Corollary 1.15. Let $\left(M, g_{0}\right)$ be a compact Riemannian 4-manifold. If $Y_{g_{0}}>0$ and
$$\mathcal{F}_{W}\left(g_{0}\right)+\frac{6}{13} Y_{g_{0}}^{2}<\frac{40}{13} \pi^{2} \chi(M),$$
then $M$ is diffeomorphic to $S^{4}$ or $\mathbb{R} P^{4}$.

\subsection*{1.3 Application to 3-dimensional gradient flows}

For 3-dimensional manifolds, as $3>\frac{n}{2}, \mathcal{F}_{R m}$ strongly controls the geometry.
For $\alpha>0$, let define:
$$\mathcal{G}^{\alpha}(g)=\mathcal{F}_{\text {Ric }}+\alpha \mathcal{F}_{R},$$
and
$$\left\{\begin{aligned}
\partial_{t} g & =-\nabla \mathcal{G}^{\alpha}(g) \\
g(0) & =g_{0} .
\end{aligned} \quad\left(E_{3}^{\alpha}\left(g_{0}\right)\right)\right.$$

When $\alpha$ is positive, those functionals control the $L^{2}$ norm of the curvature, and as they decay along their gradient flows, the curvature cannot blow up. However, we have to assume a positive lower bound on the Yamabe constant along the flow to prevent collapsing with bounded curvature.

Theorem 1.16. Let $\left(M, g_{0}\right)$ be a compact Riemannian 3-manifold, let $\alpha>0$, and let $g_{t}, t \in[0, T)$, be the maximal solution of $E_{3}^{\alpha}\left(g_{0}\right)$.

Suppose that there exists some $Y_{0}>0$ such that $Y_{g_{t}} \geq Y_{0}$ for all $t \in[0, T)$.
Then $g_{t}$ develops no singularity, and there exists a sequence $\left(t_{i}, x_{i}\right)$ with $t_{i} \rightarrow \infty$ such that ( $M, g_{t_{i}}, x_{i}$ ) converges in the pointed $C^{\infty}$ topology to a manifold ( $M_{\infty}, g_{\infty}, x_{\infty}$ ) which is critical for $\mathcal{G}^{\alpha}$.

\section*{2 Short-time existence}

As it is invariant by diffeomorphisms, the differential operator $P$ is not elliptic. We use the DeTurck trick to fill the $n$-dimensional subspace in the kernel of $\sigma_{\xi} P_{g}^{\prime}$ induced by this geometric invariance.

We use the notation $\mathcal{T}^{(p, q)} M$ for the space of $(p, q)$-tensors. We will sometimes raise or lower indices in the following way:
$$T_{i_{1} \ldots i \ldots i_{p}}=g_{i j} T_{i_{1} \ldots i_{p}}{ }^{j},$$
to identify $\mathcal{T}^{(p+1, q)} M$ and $\mathcal{T}^{(p, q+1)} M$.
We say that a differential operator $F: \mathcal{S}_{+}^{2}(M) \rightarrow \mathcal{T}^{(p, q)} M$ is geometric if it is invariant by diffeomorphisms, i.e. if for all metrics $g$ and all diffeomorphisms $\phi: M \rightarrow M$,
$$F\left(\phi^{*} g\right)=\phi^{*} F(g) .$$

This is in particular the case for the curvature operators and their derivatives with respect to the Levi-Civita connection.

We recall that if $L: h \mapsto L_{k}\left(\nabla^{k} h\right)+\cdots+L_{0}(h)$ is a linear differential operator of order $k$, its principal symbol $\sigma_{\xi} L$ is defined for all $\xi$ in $T^{*} M$ by:
$$\sigma_{\xi} L(h)=L_{k}(\xi \otimes \cdots \otimes \xi \otimes h) .$$

We say that $L$ is elliptic if $\sigma_{\xi} L$ is an isomorphism for all $\xi \neq 0$.
We say that $L$ is strongly elliptic if $k=2 k^{\prime}$ and $(-1)^{k^{\prime}+1} \sigma_{\xi} L$ is uniformly positive, i.e. if there exists $\alpha>0$ such that for all $h$,
$$(-1)^{k^{\prime}+1}\left\langle\sigma_{\xi} L(h) \mid h\right\rangle \geq \alpha|\xi|^{k}|h|^{2} .$$

Proposition 2.1 (DeTurck trick). Let $\left(M, g_{0}\right)$ be a compact Riemannian manifold.
Let $P: \mathcal{S}_{+}^{2}(M) \rightarrow \mathcal{S}^{2}(M)$ and $V: \mathcal{S}_{+}^{2}(M) \rightarrow T M$ be geometric differential operators such that $\left(P-L_{V}\right)_{g_{0}}^{\prime}$ is strongly elliptic. Then
$$\left\{\begin{aligned}
\partial_{t} g & =P(g) \\
g(0) & =g_{0}
\end{aligned} \quad E_{P}\left(g_{0}\right)\right.$$
admits a unique maximal solution on an open interval $[0, T), T$ positive.
We will use the following lemma:
Lemma 2.2. Let $\left(g_{t}\right)$ be a smooth family of metrics and let $\left(\phi_{t}\right)$ be a smooth family of diffeomorphisms. Then
$$\partial_{t}\left(\phi_{t}^{*} g_{t}\right)=\phi_{t}^{*}\left(\partial_{t} g_{t}+L_{V_{t}} g_{t}\right),$$
where $V_{t}=\partial_{t} \phi_{t} \circ \phi_{t}^{-1}$.
Proof.
$$\begin{aligned}
\partial_{t}\left(\phi_{t}^{*} g_{t}\right)_{\left.\right|_{t_{0}}} & =\partial_{t}\left(\phi_{t_{0}}^{*} g_{t}\right)_{\left.\right|_{t_{0}}}+\partial_{t}\left(\phi_{t}^{*} g_{t_{0}}\right)_{\left.\right|_{t_{0}}} \\
& =\phi_{t_{0}}^{*}\left(\partial_{t} g_{t_{\left.\right|_{t_{0}}}}\right)+\phi_{t_{0}}^{*}\left(\partial_{t}\left(\phi_{t} \circ \phi_{t_{0}}^{-1}\right)^{*} g_{\left.t_{0}\right|_{t_{0}}}\right) \\
& =\phi_{t_{0}}^{*}\left(\partial_{t} g_{t_{\left.\right|_{t_{0}}}}+L_{\partial_{t} \phi_{t_{\left.\right|_{t_{0}}}} \circ \phi_{t_{0}}^{-1}} g_{t}\right) .
\end{aligned}$$ \(\square\)
Proof of the proposition. Since $\left(P-L_{V}\right)_{g_{0}}^{\prime}$ is strongly elliptic, it follows from the theory of parabolic equations that
$$\left\{\begin{aligned}
\partial_{t} g & =P(g)-L_{V_{g}} g \\
g(0) & =g_{0}
\end{aligned} \quad\left(D T\left(g_{0}\right)\right)\right.$$
admits is a unique maximal solution $\tilde{g}_{t}, t \in[0, T)$ with $T>0$ (see [MM10]).
Let $\phi_{t}, t \in[0, T)$ be the flow of $V\left(\tilde{g}_{t}\right)$ :
$$\left\{\begin{aligned}
\partial_{t} \phi_{t} & =V\left(\tilde{g}_{t}\right) \circ \phi_{t}, \\
\phi_{0} & =I d_{M} .
\end{aligned}\right.$$
Let show that:
$$\left(g_{t}\right)_{t \in\left[0, T_{1}\right)} \text { is a solution of } E_{P}\left(g_{0}\right) \Longleftrightarrow T_{1} \leq T \text { and } \forall t \in\left[0, T_{1}\right) g_{t}=\phi_{t}^{*} \tilde{g}_{t} .$$
It will gives short-time existence and uniqueness for $E_{P}\left(g_{0}\right)$.
Let $g_{t}=\phi_{t}^{*} \tilde{g}_{t}$. Then $g(0)=g_{0}$ and by Lemma 2.2, for all $t$ in $[0, T)$,
$$\partial_{t} g=\phi_{t}^{*}\left(\partial_{t} \tilde{g}+L_{V_{\tilde{g}}} \tilde{g}\right)=\phi_{t}^{*} P(\tilde{g})=P(g) .$$
So $g_{t}$ is solution of $E_{P}\left(g_{0}\right)$ on $[0, T)$.
Now, let $g_{t}$ be a solution of $E_{P}\left(g_{0}\right)$ on $\left[0, T_{1}\right)$. Let $\psi_{t}, t \in\left[0, T_{1}\right)$ be the flow of $-V_{g_{t}}$. Then $\psi_{t}^{*} g_{t}$ is solution of $\left(D T\left(g_{0}\right)\right)$ on $\left[0, T_{1}\right)$ :
$$\begin{aligned}
\partial_{t}\left(\psi_{t}^{*} g_{t}\right) & =\psi_{t}^{*}\left(\partial_{t} g-L_{V_{g}} g\right) \\
& \left.=\psi_{t}^{*} P(g)-\psi_{t}^{*} L_{V_{g}} g\right) \\
& =P\left(\psi_{t}^{*} g\right)-L_{V_{\psi_{t}^{*}} g} \psi_{t}^{*} g .
\end{aligned}$$

Therefore, $T_{1} \leq T$ and for all $t$ in $\left[0, T_{1}\right), \psi_{t}^{*} g_{t}=\tilde{g}_{t}$.
Moreover, for all $t$ in $\left[0, T_{1}\right), \psi_{t}^{-1}=\phi_{t}$ :
$$\partial_{t}\left(\psi_{t}^{-1}\right)=-\psi_{t}^{*}\left(-V_{g_{t}}\right) \circ \psi_{t}^{-1}=V_{\tilde{g}_{t}} \circ \psi_{t}^{-1},$$
and $\psi_{0}^{-1}=I d_{M}$, so $\psi_{t}^{-1}$ is the flow of $V_{\tilde{g}_{t}}$. It follows that $g_{t}=\phi_{t}^{*} \tilde{g}_{t}$. \(\square\)

Now, we compute the principal symbols of the operators we will deal with. If $g$ is a metric and $\xi$ is in $T^{*} M$, let define
$$R_{\xi}(g)=\xi \otimes \xi-|\xi|^{2} g .$$
If $g$ and $g_{0}$ are two metrics, let define
$$\left(\gamma_{g, g_{0}}\right)^{i}=\frac{1}{2} g^{\alpha \beta}\left(\Gamma_{\alpha \beta}^{i}(g)-\Gamma_{\alpha \beta}^{i}\left(g_{0}\right)\right) .$$

Proposition 2.3. For all metrics $g$ and all $\xi$ in $T^{*} M$, we have
$$\begin{aligned}
& \sigma_{\xi}\left(L_{V}\right)_{g}^{\prime}=\xi \otimes \sigma_{\xi} V_{g}^{\prime}+\sigma_{\xi} V_{g}^{\prime} \otimes \xi, \\
& \sigma_{\xi} R_{g}^{\prime}=\left\langle R_{\xi} \mid \cdot\right\rangle, \\
& \sigma_{\xi}\left(R i c-L_{\gamma_{\cdot, g_{0}}}\right)_{g}^{\prime}=-\frac{1}{2}|\xi|^{2} \operatorname{Id}_{\mathcal{S}^{2}(M)}, \\
& \sigma_{\xi}(\delta \mathrm{D}(R \cdot))_{g}^{\prime}=\left\langle R_{\xi} \mid \cdot\right\rangle R_{\xi}, \\
& \sigma_{\xi}\left(\delta \mathrm{D} \text { Ric }-L_{\Delta \gamma_{\cdot, g_{0}}+\frac{1}{4} \nabla R}\right)_{g}^{\prime}=\frac{1}{2}|\xi|^{4} \operatorname{Id}_{\mathcal{S}^{2}(M)} .
\end{aligned}$$
Where the operators $\delta$ and D are defined in section 9.1 and $V: \mathcal{S}_{+}^{2}(M) \rightarrow T M$ is any differential operator of degree at least one,

Proof. We recall that the Lie derivative of a metric is given by:
$$\left(L_{V} g\right)_{i j}=\nabla_{i} V_{j}+\nabla_{j} V_{i},$$
then by (12) in Proposition 9.7,
$$\left(L_{V}\right)_{g}^{\prime}(h)_{i j}=\nabla_{i} V_{g}^{\prime}(h)_{j}+\nabla_{j} V_{g}^{\prime}(h)_{i}+\nabla h * V,$$
and as $V$ is of degree at least one,
$$\sigma_{\xi}\left(L_{V}\right)_{g}^{\prime}(h)_{i j}=\xi_{i} \sigma_{\xi} V_{g}^{\prime}(h)_{j}+\xi_{j} \sigma_{\xi} V_{g}^{\prime}(h)_{i} .$$

By Proposition 9.5,
$$R_{g}^{\prime}(h)=\delta \tilde{\delta} h+\Delta \operatorname{tr} h-\langle\operatorname{Ric} \mid h\rangle,$$
then
$$\sigma_{\xi} R_{g}^{\prime}(h)=\langle\xi \otimes \xi \mid h\rangle-|\xi|^{2} \operatorname{tr} h=\left\langle R_{\xi} \mid h\right\rangle,$$
therefore, as $\delta \mathrm{D}\left(R_{g} g\right)=\Delta R_{g} g+\nabla^{2} R_{g}$ (Proposition 9.3),
$$\sigma_{\xi}\left(\delta \mathrm{D}(R \cdot)_{g}^{\prime}=\xi \otimes \xi \sigma_{\xi} R_{g}^{\prime}-|\xi|^{2} \sigma_{\xi} R_{g}^{\prime} g=\left\langle R_{\xi} \mid \cdot\right\rangle R_{\xi} .\right.$$

It follows of Proposition 9.4 that:
$$\begin{aligned}
\left(\gamma_{\cdot, g_{0}}\right)_{g}^{\prime}(h)^{i} & =\frac{1}{2}\left(\nabla^{\alpha} h_{\alpha}{ }^{i}-\frac{1}{2} \nabla^{i} \operatorname{tr} h\right)-\frac{1}{2} h^{\alpha \beta}\left(\Gamma_{\alpha \beta}^{i}(g)-\Gamma_{\alpha \beta}^{i}\left(g_{0}\right)\right), \\
\left(\gamma_{\cdot, g_{0}}\right)_{g}^{\prime}(h) & =-\frac{1}{2}\left(\delta h+\frac{1}{2} \tilde{\mathrm{D}} \operatorname{tr} h\right)+h *\left(\Gamma(g)-\Gamma\left(g_{0}\right)\right),
\end{aligned}$$
and by Proposition 9.5:
$$R i c_{g}^{\prime}(h)=\frac{1}{2}\left(\Delta h-\mathrm{D}\left(\delta h+\frac{1}{2} \tilde{\mathrm{D}} \operatorname{tr} h\right)\right)-\tilde{\mathrm{D}}\left(\tilde{\delta} h+\frac{1}{2} \operatorname{Dtr} h\right)+h * R m .$$
It follows that its principal symbol is
$$\sigma_{\xi} \operatorname{Ric}{ }_{g}^{\prime}(h)=-\frac{1}{2}|\xi|^{2} h+\xi \otimes \sigma_{\xi} \gamma_{g}^{\prime}(h)+\sigma_{\xi} \gamma_{g}^{\prime}(h) \otimes \xi,$$
so
$$\sigma_{\xi}\left(\operatorname{Ric}-L_{\gamma_{\cdot, g_{0}}}\right)_{g}^{\prime}=-\frac{1}{2}|\xi|^{2} I d_{\mathcal{S}^{2}(M)} .$$

Finally,
$$\begin{aligned}
\sigma_{\xi}(\Delta \operatorname{Ric})_{g}^{\prime}(h) & =-|\xi|^{2} \sigma_{\xi} \operatorname{Ric}_{g}^{\prime}(h) \\
& =-\frac{1}{2}|\xi|^{4} h+\xi \otimes\left(-|\xi|^{2} \sigma_{\xi} \gamma_{g}^{\prime}(h)\right)+\left(-|\xi|^{2} \sigma_{\xi} \gamma_{g}^{\prime}(h)\right) \otimes \xi,
\end{aligned}$$
and then, since $\delta \mathrm{D}$ Ric $_{g}=\Delta$ Ric $_{g}+\frac{1}{2} \nabla^{2} R_{g}+R m * R m$ (Proposition 9.3),
$$\sigma_{\xi}\left(\delta \mathrm{D} \text { Ric }-L_{\Delta \gamma+\frac{1}{4} \nabla R}\right)_{g}^{\prime}=\sigma_{\xi}\left(\Delta \text { Ric }-L_{\Delta \gamma}\right)_{g}^{\prime}=-\frac{1}{2}|\xi|^{4} I d_{\mathcal{S}^{2}(M)} .$$ \(\square\)

Proposition 2.4. Let $P: \mathcal{S}_{+}^{2}(M) \rightarrow \mathcal{S}^{2}(M)$ be smooth map of the form
$$P(g)=\delta \tilde{\delta} R m_{g}+a \Delta R_{g} g+b \nabla^{2} R_{g}+R m_{g} * R m_{g},$$
and let $V: \mathcal{S}_{+}^{2}(M) \rightarrow T M$ be defined by $V_{g}=-\Delta \gamma_{g, g_{0}}+\frac{2(b-a)-1}{4} \nabla R_{g}$. Then
$$\sigma_{\xi}\left(P-L_{V}\right)_{g}^{\prime}=-\frac{1}{2}|\xi|^{4} \operatorname{Id}_{\mathcal{S}^{2}(M)}+a\left\langle R_{\xi} \mid \cdot\right\rangle R_{\xi},$$
and
\begin{itemize}
\item[-] If $a<\frac{1}{2(n-1)}$, then $P-L_{V}$ is strongly elliptic.
\item[-] If $a=\frac{1}{2(n-1)}$, then $P-L_{W}$ is not elliptic, for any $W: \mathcal{S}_{+}^{2}(M) \rightarrow T M$.
\item[-] If $a>\frac{1}{2(n-1)}$, then $P-L_{W}$ is not strongly elliptic, for any $W: \mathcal{S}_{+}^{2}(M) \rightarrow T M$.
\end{itemize}

Proof. Since $\tilde{\delta} R m=-\mathrm{D} R i c$ (Proposition 9.2) and $\delta \mathrm{D}\left(R_{g} g\right)=\Delta R_{g} g+\nabla^{2} R_{g}$ (Proposition 9.3), we see that:
$$P-L_{V}=-\delta \mathrm{D} \text { Ric }+L_{\Delta \gamma, g_{0}+\frac{1}{4} \nabla R}+a \delta \mathrm{D}(R \cdot),$$
then Proposition 2.3 shows that
$$\sigma_{\xi}\left(P-L_{V}\right)_{g}^{\prime}=-\frac{1}{2}|\xi|^{4} \operatorname{Id}_{\mathcal{S}^{2}(M)}+a\left\langle R_{\xi} \mid \cdot\right\rangle R_{\xi} .$$

Let compute
$$\left.\left|R_{\xi}\right|^{2}=|\xi|^{4}-2\langle\xi \otimes \xi||\xi|^{2} g\right\rangle+n|\xi|^{4}=(n-1)|\xi|^{4} .$$
Moreover, for all $W: \mathcal{S}_{+}^{2}(M) \rightarrow T M$, the image of $\sigma_{\xi}\left(L_{W}\right)_{g}^{\prime}$ lies in $R_{\xi}^{\perp}$ :
$$\begin{aligned}
\left\langle\sigma_{\xi}\left(L_{W}\right)_{g}^{\prime} \mid R_{\xi}\right\rangle & \left.=\left\langle\xi \otimes \sigma_{\xi} W_{g}^{\prime}+\sigma_{\xi} W_{g}^{\prime} \otimes \xi\right| \xi \otimes \xi-|\xi|^{2} g\right\rangle \\
& =2|\xi|^{2}\left\langle\xi \mid \sigma_{\xi} W_{g}^{\prime}\right\rangle-2|\xi|^{2}\left\langle\xi \mid \sigma_{\xi} W_{g}^{\prime}\right\rangle \\
& =0 .
\end{aligned}$$
If $\mathbf{a}<\frac{\mathbf{1}}{\mathbf{2}(\mathbf{n}-\mathbf{1})}$, then
$$\begin{aligned}
-\left\langle\sigma_{\xi}\left(P-L_{V}\right)_{g}^{\prime}(h) \mid h\right\rangle & =\frac{1}{2}|\xi|^{4}|h|^{2}-a\left|\left\langle R_{\xi} \mid h\right\rangle\right|^{2} \\
& \geq \frac{1}{2}\left(1-2 a_{+}(n-1)\right)|\xi|^{4}|h|^{2},
\end{aligned}$$
and $P-L_{V}$ is strongly elliptic.
If $\mathbf{a}=\frac{\mathbf{1}}{\mathbf{2}(\mathbf{n}-\mathbf{1})}$, then $\sigma_{\xi}\left(P-L_{V}\right)_{g}^{\prime}$ is the orthogonal projection on $R_{\xi}^{\perp}$. In particular,
$$\begin{aligned}
\left\langle\sigma_{\xi}\left(P-L_{W}\right)_{g}^{\prime}(h) \mid R_{\xi}\right\rangle & =\left\langle\sigma_{\xi}\left(P-L_{V}\right)_{g}^{\prime}(h) \mid R_{\xi}\right\rangle+\left\langle\sigma_{\xi}\left(L_{V-W}\right)_{g}^{\prime}(h) \mid R_{\xi}\right\rangle \\
& =\frac{1}{2}|\xi|^{4}\left\langle R_{\xi} \mid h\right\rangle-a|\xi|^{2}\left|R_{\xi}\right|^{2}\left\langle R_{\xi} \mid h\right\rangle \\
& =0,
\end{aligned}$$
i.e. the image of $\sigma_{\xi}\left(P-L_{W}\right)_{g}^{\prime}$ is included in $R_{\xi}^{\perp}$, therefore $P-L_{W}$ is not elliptic.
If $\mathbf{a}>\frac{\mathbf{1}}{\mathbf{2}(\mathbf{n}-\mathbf{1})}$, then for $\xi \neq 0$ :
$$\begin{aligned}
-\left\langle\sigma_{\xi}\left(P-L_{W}\right)_{g}^{\prime}\left(R_{\xi}\right) \mid R_{\xi}\right\rangle & =-\left\langle\sigma_{\xi}\left(P-L_{V}\right)_{g}^{\prime}\left(R_{\xi}\right) \mid R_{\xi}\right\rangle+\left\langle\sigma_{\xi}\left(L_{V-W}\right)_{g}^{\prime}\left(R_{\xi}\right) \mid R_{\xi}\right\rangle \\
& =\frac{1}{2}(1-2 a(n-1))|\xi|^{4}\left|R_{\xi}\right|^{2} \\
& <0 .
\end{aligned}$$
Consequently, $P-L_{W}$ is not strongly elliptic. \(\square\)

Proof of Theorem 1.4 It is an immediate consequence of Propositions 2.4 and 2.1. \(\square\)

\section*{3 Gradient flows for geometric functionals}

If $T: \mathcal{S}_{+}^{2}(M) \rightarrow \mathcal{T}^{(p, q)} M$ is smooth, let define the functional
$$\mathcal{F}_{T}(g)=\int_{M}|T(g)|_{g}^{2} d v_{g}$$
and if $\mathcal{F}: \mathcal{S}_{+}^{2}(M) \rightarrow \mathbb{R}$ is a smooth functional, let define its gradient by
$$\mathcal{F}_{g}^{\prime}(h)=(\nabla \mathcal{F}(g) \mid h)_{L^{2}} .$$
Then the gradient flow of $\mathcal{F}$ starting from $g_{0}$ is the following evolution equation:
$$\left\{\begin{aligned}
\partial_{t} g & =-\nabla \mathcal{F}(g) \\
g(0) & =g_{0}
\end{aligned}\right.$$

As we immediately get $\partial_{t} \mathcal{F}\left(g_{t}\right)=-\int_{M}\left|\nabla \mathcal{F}\left(g_{t}\right)\right|^{2} d v_{g_{t}}$, we see that $\mathcal{F}$ decreases along the flow.
We recall that the curvature tensor has the following orthogonal decomposition:
$$R m_{g}=W_{g}+\frac{1}{n-2} \stackrel{\circ}{R i c_{g}} \wedge g+\frac{1}{2 n(n-1)} R_{g} g \wedge g,$$
where $\wedge$ is the Kulkarni-Nomizu product defined for $u$ and $v$ in $\mathcal{S}^{2}(M)$ by:
$$(u \wedge v)_{i j k l}=u_{i k} v_{j l}+u_{j l} v_{i k}-u_{i l} v_{j k}-u_{j k} v_{i l} .$$

It follows that
$$\mathcal{F}_{R m}(g)=\mathcal{F}_{W}(g)+\frac{1}{n-2} \mathcal{F}_{R i c}^{\circ}(g)+\frac{1}{2 n(n-1)} \mathcal{F}_{R}(g) .$$

The gradients of the quadratic curvature functionals are given by (see [Bes87], chapter 4.H):
$$\begin{aligned}
\nabla \mathcal{F}_{R m} & =-\delta \tilde{\delta} R m-\frac{1}{2} R m \vee R m+\frac{1}{2}|R m|^{2} g, \\
\nabla\left(\mathcal{F}_{\text {Ric }}-\frac{1}{4} \mathcal{F}_{R}\right) & =-\delta \tilde{\delta} R m-R i c \circ\left(R i c-\frac{1}{2} R g\right)-\stackrel{\circ}{R m}^{2}(R i c)+\frac{1}{2}\left(|R i c|^{2}-\frac{1}{4} R^{2}\right) g, \\
\nabla \mathcal{F}_{W} & =-\delta \tilde{\delta} W-\frac{1}{n-2} \stackrel{\circ}{W}(\text { Ric })-\frac{1}{2}\left(W \vee W-|W|^{2} g\right), \\
\nabla \mathcal{F}_{2} & =-\frac{1}{2} \delta \mathrm{D} A+\frac{1}{2} \stackrel{\circ}{W}(\text { Ric })+\frac{n-4}{2(n-2)}\left(A \circ\left(\text { Ric }-\frac{1}{2} R g\right)+\sigma_{2} g\right), \\
\nabla \mathcal{F}_{R} & =2 \delta \mathrm{D}(R g)-2 R\left(\text { Ric }-\frac{1}{4} R g\right),
\end{aligned}$$
where for a $(4,0)$ curvature tensor $T$ and an endomorphism $u$ we wrote:
$$(T \vee T)_{i j}=T_{\alpha \beta \gamma i} T^{\alpha \beta \gamma}{ }_{j} \quad \text { and } \quad(\stackrel{\circ}{T} u)_{i j}=T_{\alpha i \beta j} u^{\alpha \beta} .$$

From the relations between the derivatives of the curvature given in Propositions 9.2 and 9.3, it follows that for $\beta$ in [0, 1] and $a<\frac{1}{2(n-1)}$, the gradient flow of the functional
$$(1-\beta) \mathcal{F}_{R m}+\beta\left(\mathcal{F}_{\text {Ric }}-\frac{1}{4} \mathcal{F}_{R}\right)-\frac{a}{2} \mathcal{F}_{R}$$
is of the form $E_{P}$ with
$$P(g)=\delta \tilde{\delta} R m_{g}+a \Delta R_{g} g+a \nabla^{2} R_{g}+R m_{g} * R m_{g} .$$

For $n \geq 4$, we can also write that for $\beta$ in [0,1] and $\alpha>0$, the gradient flow of the functional
$$\frac{n-2}{n-3} \beta \mathcal{F}_{W}-2(1-\beta) \mathcal{F}_{2}+\frac{\alpha}{4(n-1)} \mathcal{F}_{R}$$
is of the form $E_{P}$ with
$$P(g)=\delta \tilde{\delta} R m_{g}+\frac{1-\alpha}{2(n-1)}\left(\Delta R_{g} g+\nabla^{2} R_{g}\right)+R m_{g} * R m_{g} .$$

In low dimensions, additional relations between the curvature tensors allow us to write it in an easier way:

In dimension 3: We have
$$\mathcal{F}_{W}(g)=0 \quad \text { and } \quad \mathcal{F}_{R m}=\mathcal{F}_{\text {Ric }}-\frac{1}{4} \mathcal{F}_{R} .$$
The gradient flow of $-2 \mathcal{F}_{2}+\frac{\alpha}{8} \mathcal{F}_{R}$ is of the form $E_{P}$ with
$$P(g)=\delta \tilde{\delta} R m_{g}+\frac{1-\alpha}{4}\left(\Delta R_{g} g+\nabla^{2} R_{g}\right)+R m_{g} * R m_{g} .$$
In dimension 4: The Gauss-Bonnet formula gives us another relation between the functionals:
$$\mathcal{F}_{R m}(g)-\mathcal{F}_{R i c}^{\circ}(g)=\mathcal{F}_{W}(g)+\mathcal{F}_{2}(g)=8 \pi^{2} \chi(M) .$$
It follows that
$$\nabla \mathcal{F}_{R m}=\nabla\left(\mathcal{F}_{\text {Ric }}-\frac{1}{4} \mathcal{F}_{R}\right) \quad \text { and } \quad \nabla \mathcal{F}_{W}(g)=-\nabla \mathcal{F}_{2}(g) .$$

If $\alpha>0$, the gradient flow of $2 \mathcal{F}_{W}+\frac{\alpha}{12} \mathcal{F}_{R}$ is the same as the gradient flow of $2(1-\alpha) \mathcal{F}_{W}+\alpha \mathcal{F}_{\text {Ric }}$ and is of the form $E_{P}$ with
$$P(g)=\delta \tilde{\delta} R m_{g}+\frac{1-\alpha}{6}\left(\Delta R_{g} g+\nabla^{2} R_{g}\right)+R m_{g} * R m_{g} .$$

Moreover, since $W \vee W-|W|^{2} g=0$ (see [Bes87]), the gradient of the Weyl functional $\mathcal{F}_{W}$, which is called the Bach tensor, takes the following shorter form:
$$\nabla \mathcal{F}_{W}=-\nabla \mathcal{F}_{2}=-\delta \tilde{\delta} W-\frac{1}{2} \stackrel{\circ}{W}(\stackrel{\circ}{R i c}) .$$

\section*{4 Rigidity results for critical metrics of $\mathcal{F}^{\alpha}$}

In this section, we prove Theorem 1.12 and a number of auxiliary results which will be necessary for the proof of Theorem 1.13. We begin with a rigidity result for metrics with harmonic Weyl tensor (i.e. $\delta W=0$ ).

Proposition 4.1. Let $(M, g)$ be a complete Riemannian 4-manifold with positive Yamabe constant, constant scalar curvature and harmonic Weyl tensor. If
$$\mathcal{F}_{W}(g)<\frac{25}{54} Y_{g}^{2},$$
then $W_{g}=0$.
Note that in the compact case, sharper results have been obtained by Gursky in [Gur00]. We will use the following Lemmas:

Lemma 4.2 (Weitzenböck formula, Derdziński ([Der83])). Let $(M, g)$ be a complete Riemannian 4-manifold with harmonic Weyl tensor. Then
$$\frac{1}{2} \Delta|W|^{2} \geq|\nabla W|^{2}+\frac{1}{2} R|W|^{2}-\sqrt{6}|W|^{3} .$$

Proof. Let choose a local orientation. Then the Weyl tensor can be written as $W=W^{+}+W^{-}$ according to the splitting $\Lambda^{2}(T M)=\Lambda_{+}^{2}(T M) \oplus \Lambda_{-}^{2}(T M)$.

Then the following Weitzenböck formula holds (see [Bes87], 16.73):
$$\frac{1}{2} \Delta\left|W^{ \pm}\right|^{2}=\left|\nabla W^{ \pm}\right|^{2}+\frac{1}{2} R\left|W^{ \pm}\right|^{2}-18 \operatorname{det} W^{ \pm}$$
And since the maximum of $\lambda_{1} \lambda_{2} \lambda_{3}$ under the constraints
$$\left\{\begin{array}{l}
\lambda_{1}+\lambda_{2}+\lambda_{3}=0 \\
\lambda_{1}^{2}+\lambda_{2}^{2}+\lambda_{3}^{2}=1
\end{array}\right.$$
is $\frac{1}{3 \sqrt{6}}$, we obtain:
$$\begin{aligned}
\frac{1}{2} \Delta\left|W^{ \pm}\right|^{2} & \geq\left|\nabla W^{ \pm}\right|^{2}+\frac{1}{2} R\left|W^{ \pm}\right|^{2}-\sqrt{6}\left|W^{ \pm}\right|^{3} \\
& \geq\left|\nabla W^{ \pm}\right|^{2}+\frac{1}{2} R\left|W^{ \pm}\right|^{2}-\sqrt{6}|W|\left|W^{ \pm}\right|^{2} .
\end{aligned}$$
Adding the two inequalities, we get:
$$\frac{1}{2} \Delta|W|^{2} \geq\left|\nabla W^{+}\right|^{2}+\left|\nabla W^{-}\right|^{2}+\frac{1}{2} R|W|^{2}-\sqrt{6}|W|^{3} .$$
And since the splitting $\Lambda^{2}(T M)=\Lambda_{+}^{2}(T M) \oplus \Lambda_{-}^{2}(T M)$ is parallel:
$$\frac{1}{2} \Delta|W|^{2} \geq|\nabla W|^{2}+\frac{1}{2} R|W|^{2}-\sqrt{6}|W|^{3} .$$ \(\square\)

Lemma 4.3 (Refined Kato inequality). Let $(M, g)$ be a complete Riemannian 4-manifold with harmonic Weyl tensor. Then in the distributional sense,
$$|\nabla| W \|^{2} \leq \frac{3}{5}|\nabla W|^{2} .$$
Proof. If we choose a local orientation, we have the following Kato inequality (see [GL99]):
$$\left.\left.|\nabla| W^{ \pm}\right|^{2}|=2| W^{ \pm}| | \nabla\left|W^{ \pm}\right|\left|\leq 2 \sqrt{\frac{3}{5}}\right| W^{ \pm}| | \nabla W^{ \pm} \right\rvert\,,$$
and then
$$\begin{aligned}
\left.|\nabla| W\right|^{2} \mid & \leq\left.|\nabla| W^{+}\right|^{2}\left|+|\nabla| W^{-}\right|^{2} \mid \\
& \leq 2 \sqrt{\frac{3}{5}}\left(\left|W^{+}\right|\left|\nabla W^{+}\right|+\left|W^{-}\right|\left|\nabla W^{-}\right|\right) \\
& \leq 2 \sqrt{\frac{3}{5}}\left(\left|W^{+}\right|^{2}+\left|W^{-}\right|^{2}\right)^{\frac{1}{2}}\left(\left|\nabla W^{+}\right|^{2}+\left|\nabla W^{-}\right|^{2}\right)^{\frac{1}{2}} \\
& =2 \sqrt{\frac{3}{5}}|W||\nabla W|,
\end{aligned}$$
and consequently,
$$|\nabla| W\left|\left|\leq \sqrt{\frac{3}{5}}\right| \nabla W\right| .$$ \(\square\)

Proof of the Proposition. 1) If $M$ is compact, then by integrating the inequality of Lemma 4.2, we see that:
$$\int_{M}\left(|\nabla W|^{2}+\frac{1}{2} R|W|^{2}\right) d v \leq \sqrt{6}|W|_{3}^{3}$$
Using the refined Kato inequality of Lemma 4.3, and the Hölder inequality, we obtain
$$\frac{5}{3} \int_{M}\left(\left.|\nabla| W\right|^{2}+\frac{1}{6} R|W|^{2}\right) d v+\frac{2}{9} \int_{M} R|W|^{2} d v \leq \sqrt{6}|W|_{2}|W|_{4}^{2}$$
thus
$$\frac{5}{3} Y|W|_{4}^{2}+\frac{2}{9} \int_{M} R|W|^{2} d v \leq \sqrt{6}|W|_{2}|W|_{4}^{2}$$
Since $R_{g}$ is a positive constant (as $Y_{g}>0$ ), we see that $W=0$ as soon as $\sqrt{6}|W|_{2} \leq \frac{5}{3} Y$, i.e. as soon as $|W|_{2}^{2} \leq \frac{25}{54} Y^{2}$.
\begin{itemize}
\item[2)] Now, if $M$ is not compact, let choose $r>0, x$ a point and $\phi$ a cut-off function such that:
$$\left\{\begin{array}{l}
\phi \equiv 1 \quad \text { on } B_{x}(r), \\
\phi \equiv 0 \quad \text { on } M \backslash B_{x}(2 r), \\
|\nabla \phi|_{\infty} \leq \frac{2}{r} .
\end{array}\right.$$
\end{itemize}
Let $u=|W| \phi$. For all $\epsilon>0$, we have:
$$|\nabla u|^{2}=|\phi \nabla| W|+|W| \nabla \phi|^{2} \leq\left.(1+\epsilon)|\nabla| W\right|^{2} \phi^{2}+\left(1+\frac{1}{\epsilon}\right)|W|^{2}|\nabla \phi|^{2} .$$
Consequently,
$$\begin{aligned}
Y|u|_{4}^{2} & \leq \int_{M}|\nabla u|^{2}+\frac{1}{6} R u^{2} d v \\
& \leq\left.(1+\epsilon) \int_{M}|\nabla| W\right|^{2} \phi^{2} d v+\frac{1}{6} \int_{M} R u^{2} d v+\left(1+\frac{1}{\epsilon}\right)|\nabla \phi|_{\infty}^{2}|W|_{2}^{2} \\
& \leq(1+\epsilon)\left(\int_{M}\left(\left.|\nabla| W\right|^{2}+\frac{1}{6} R|W|^{2}\right) \phi^{2} d v+\frac{1}{\epsilon}|\nabla \phi|_{\infty}^{2}|W|_{2}^{2}\right),
\end{aligned}$$
since $R$ is a nonnegative constant (as $Y>0$ ).
On the other hand, multiplying the inequality of Lemma 4.2 by $\phi^{2}$ and integrating, we obtain:
$$\begin{aligned}
\int_{M}\left(|\nabla W|^{2}+\frac{1}{2} R|W|^{2}\right) \phi^{2} d v & \leq \sqrt{6} \int_{M}\left(|W|^{3} \phi^{2}+\left.\frac{1}{2}\langle\nabla| W\right|^{2}\left|\nabla \phi^{2}\right\rangle\right) d v \\
& \leq \sqrt{6}|W|_{2}|u|_{4}^{2}+2|\nabla \phi|_{\infty}|W|_{2}\left(\left.\int_{M}|\nabla| W\right|^{2} \phi^{2} d v\right)^{\frac{1}{2}}
\end{aligned}$$
by the Hölder inequality. Then, using the refined Kato inequality,
$$\begin{aligned}
\frac{5}{3} \int_{M}\left(\left.|\nabla| W\right|^{2}+\frac{1}{6} R|W|^{2}\right) \phi^{2} d v & \leq \sqrt{6}|W|_{2}|u|_{4}^{2}+2|\nabla \phi|_{\infty}|W|_{2}\left(\left.\int_{M}|\nabla| W\right|^{2} \phi^{2} d v\right)^{\frac{1}{2}} \\
& \leq \sqrt{6}|W|_{2}|u|_{4}^{2}+\left.\epsilon \int_{M}|\nabla| W\right|^{2} \phi^{2} d v+\frac{1}{\epsilon}|\nabla \phi|_{\infty}^{2}|W|_{2}^{2}
\end{aligned}$$
thus
$$\left(\frac{5}{3}-\epsilon\right) \int_{M}\left(\left.|\nabla| W\right|^{2}+\frac{1}{6} R|W|^{2}\right) \phi^{2} d v \leq \sqrt{6}|W|_{2}|u|_{4}^{2}+\frac{1}{\epsilon}|\nabla \phi|_{\infty}^{2}|W|_{2}^{2} .$$

We finally obtain:
$$\frac{Y}{1+\epsilon}\left(\frac{5}{3}-\epsilon\right)|u|_{4}^{2} \leq \sqrt{6}|W|_{2}|u|_{4}^{2}+\frac{1}{\epsilon(1+\epsilon)}\left(\frac{8}{3}-\epsilon\right)|\nabla \phi|_{\infty}^{2}|W|_{2}^{2},$$
then
$$\left(\frac{Y}{1+\epsilon}\left(\frac{5}{3}-\epsilon\right)-\sqrt{6}|W|_{2}\right)\left(\int_{M}|W|^{4} \phi^{4} d v\right)^{\frac{1}{2}} \leq \frac{8}{3 \epsilon} \frac{4}{r^{2}}|W|_{2}^{2} .$$
We can choose $\epsilon$ small enough such that
$$\frac{Y}{1+\epsilon}\left(\frac{5}{3}-\epsilon\right)-\sqrt{6}|W|_{2}>0 .$$
Then, by letting $r$ go to infinity, we see that $W=0$. \(\square\)

Proposition 4.4. Let $(M, g)$ be a complete Riemannian 4-manifold. If $R_{g}$ is constant, then
$$\nabla \mathcal{F}^{\alpha}(g)=\frac{1}{2} \Delta \text { Ric } \left._{g}-{ }_{\left(W_{g}+\frac{1}{2} \text { Ric }_{g} \wedge g\right)}\left(\text { Ric }_{g}\right)+\frac{1}{4} \right\rvert\, \text { Ric }\left._{g}\right|^{2} g+\frac{2-\alpha}{12} R_{g} \text { Ric }_{g} .$$
Proof. We recall that $\mathcal{F}^{\alpha}=(1-\alpha) \mathcal{F}_{W}+\frac{\alpha}{2} \mathcal{F}_{\text {Ric }}$. According to the Gauss-Bonnet formula, we can also write: $\mathcal{F}^{\alpha}=\mathcal{F}_{W}+\frac{\alpha}{24} \mathcal{F}_{R}-\alpha 8 \pi^{2} \chi(M)$. Consequently (see section 3),
$$\nabla \mathcal{F}^{\alpha}(g)=-\delta \tilde{\delta} W_{g}-\frac{1}{2} \stackrel{\circ}{W}_{g}\left(\text { Ric }_{g}\right)+\frac{\alpha}{12} \delta \mathrm{D}\left(R_{g} g\right)-\frac{\alpha}{12} R_{g} \text { Ric }_{g} .$$
Moreover, by Propositions 9.2 and 9.3:
$$\begin{aligned}
-\delta \tilde{\delta} W & =\frac{1}{2} \delta \mathrm{D} A=\frac{1}{2} \delta D \text { Ric }^{-} \frac{1}{12} \delta D\left(R_{g} g\right) \\
& =\frac{1}{2} \Delta \text { Ric }_{g}+\frac{1}{4} \nabla^{2} R_{g}+\frac{1}{2} \text { Ric }_{g} \circ \text { Ric }_{g}-\frac{1}{2} \text { R }_{g}\left(\text { Ric }_{g}\right)-\frac{1}{12} \delta D\left(R_{g} g\right) \\
& =\frac{1}{2} \Delta \text { Ric }_{g}+\frac{1}{2} \text { Ric }_{g} \circ \text { Ric }_{g}-\frac{1}{2} \text { R }_{g}^{\circ}\left(\text { Ric }_{g}\right),
\end{aligned}$$
as we assumed that $R_{g}$ is constant. Using the relations
$$\langle\stackrel{\circ}{T} u \mid v\rangle=\langle T \mid u \wedge v\rangle \quad \text { and } \quad \overline{(u \wedge g)} v=\langle u \mid v\rangle g+\operatorname{tr} v u-u \circ v-v \circ u,$$
we easily get that:
$$\stackrel{\circ}{R m}\left(\text { Ric }_{g}\right)=\stackrel{\circ}{W}\left(\text { Ric }_{g}\right)-\text { Ric } \left._{g} \circ \stackrel{\circ}{R i c}_{g}+\frac{1}{2} \right\rvert\, \text { Ric }_{g} \left\lvert\, g-\frac{1}{12} R_{g}\right. \text { Ric }_{g} .$$
Finally,
$$\nabla \mathcal{F}^{\alpha}(g)=\frac{1}{2} \Delta \stackrel{\circ}{R i c}_{g}-\stackrel{\circ}{W}_{g}\left(\text { Ric }_{g}\right)+\text { Ric }_{g} \circ \text { Ric } \left._{g}-\frac{1}{4} \right\rvert\, \text { Ric }_{g} \left\lvert\, g+\frac{2-\alpha}{12} R_{g}\right. \text { Ric }_{g},$$
and we obtain the result by writing
$$\overline{\left(R_{i}^{\circ} c_{g} \wedge g\right)}\left(\text { Ric }_{g}\right)=\mid \text { Ric }_{g} \mid g-2 \stackrel{\circ}{R i c}_{g} \circ \stackrel{\circ}{R i c}_{g} .$$ \(\square\)

The following Lemma allows us to control the Yamabe constant from below when the quadratic functional is not too large:

Lemma 4.5 (Gursky, [Gur94], see also [Str10]). Let $(M, g)$ be a compact Riemannian 4-manifold. For all $\alpha \geq 0$
$$Y_{g}^{2} \geq \frac{2}{3}\left((1-\alpha) 8 \pi^{2} \chi(M)-\mathcal{F}^{\alpha}(g)\right) .$$
Proof. If $\tilde{g} \in[g]$ is a Yamabe metric, it has constant scalar curvature and we get
$$\begin{aligned}
Y_{\tilde{g}}^{2} & =\frac{1}{36} \operatorname{Vol}_{\tilde{g}}(M)^{-1}\left(\int_{M} R_{\tilde{g}} d v_{\tilde{g}}\right)^{2}=\frac{1}{36} \int_{M} R_{\tilde{g}}^{2} d v_{\tilde{g}} \\
& \geq \frac{2}{3}\left(\frac{1}{24} \mathcal{F}_{R}(\tilde{g})-\frac{1}{2} \mathcal{F}_{R i c}^{\bullet}(\tilde{g})\right)=\frac{2}{3} \mathcal{F}_{2}(\tilde{g})
\end{aligned}$$
Since $Y$ and $\mathcal{F}_{2}$ are conformal invariants, it follows that the inequality is still true for $g$. Then
$$\begin{aligned}
Y_{g}^{2} & \geq \frac{2}{3} \mathcal{F}_{2}(g) \\
& =\frac{2}{3}\left(\alpha \mathcal{F}_{2}(g)+(1-\alpha)\left(8 \pi^{2} \chi(M)-\mathcal{F}_{W}(g)\right)\right) \\
& \geq \frac{2}{3}\left((1-\alpha) 8 \pi^{2} \chi(M)-\mathcal{F}^{\alpha}(g)\right) .
\end{aligned}$$ \(\square\)

Proposition 4.6. Let $(M, g)$ be a compact Riemannian 4-manifold and let $\alpha$ be in (0, 1). If there exists $\epsilon>0$ such that
$$\left\{\begin{array} { r l } 
{ \alpha } & { \leq \frac { 4 } { 1 3 } } \\
{ \mathcal { F } ^ { \alpha } ( g ) } & { \leq 2 \alpha ( \pi ^ { 2 } \chi ( M ) - \epsilon ) }
\end{array} \quad \text { or } \quad \left\{\begin{array}{rl}
\alpha & \geq \frac{4}{13} \\
\mathcal{F}^{\alpha}(g) & \leq \frac{8}{9}(1-\alpha)\left(\pi^{2} \chi(M)-\epsilon\right),
\end{array}\right.\right.$$
then $g$ satisfies:
$$\mathcal{F}_{W}(g)+\frac{1}{4} \mathcal{F}_{\text {Ric }}(g) \leq \frac{3}{16} Y_{g}^{2}-\epsilon .$$
Proof. If $\alpha \leq \frac{4}{13}$, then $\frac{4}{13 \alpha} \geq \frac{9}{13(1-\alpha)}$, so using the assumption on $\mathcal{F}^{\alpha}$, we can write:
$$\frac{9}{13} \mathcal{F}_{W}+\frac{2}{13} \mathcal{F}_{\text {Ric }} \leq \frac{4}{13 \alpha} \mathcal{F}^{\alpha} \leq \frac{8}{13}\left(\pi^{2} \chi(M)-\epsilon\right) .$$
In the same way, if $\alpha \geq \frac{4}{13}$, then $\frac{9}{13(1-\alpha)} \geq \frac{4}{13 \alpha}$, and using the assumption on $\mathcal{F}^{\alpha}$, it follows that:
$$\frac{9}{13} \mathcal{F}_{W}+\frac{2}{13} \mathcal{F}_{\text {Ric }} \leq \frac{9}{13(1-\alpha)} \mathcal{F}^{\alpha} \leq \frac{8}{13}\left(\pi^{2} \chi(M)-\epsilon\right) .$$
Consequently,
$$\begin{aligned}
\mathcal{F}_{W}(g)+\frac{1}{4} \mathcal{F}_{\text {Ric }}(g) & \leq \frac{1}{8}\left(8 \pi^{2} \chi(M)-\mathcal{F}_{W}(g)\right)-\epsilon \\
& \leq \frac{3}{16} Y_{g}^{2}-\epsilon,
\end{aligned}$$
according to Lemma 4.5 with $\alpha=0$. \(\square\)

Finally, let prove the following estimate:
Lemma 4.7.
$$\left.\left\lvert\,\left\langle W_{g}+\frac{1}{2} \text { Ric }_{g} \wedge g\right|\right. \text { Ric }_{g} \wedge \text { Ric }_{g}\right\rangle\left|\leq \frac{2}{\sqrt{3}}\right| \text { Ric }\left._{g}\right|^{2}\left(\left.\left|W_{g}\right|^{2}+\frac{1}{4} \right\rvert\, \text { Ric }\left._{g}\right|^{2}\right)^{\frac{1}{2}} .$$
Proof. Let write the orthogonal decomposition
$$\operatorname{Ric}_{g} \wedge \operatorname{Ric}_{g}=T+V+U,$$
where
$$U=\frac{1}{24} \operatorname{tr}^{2}\left(\operatorname{Ric}_{g} \wedge \stackrel{\circ}{\operatorname{Ric}}_{g}\right) g \wedge g=-\frac{1}{12}\left|\operatorname{Ric}_{g}^{\circ}\right|^{2} g \wedge g,$$
and
$$\begin{aligned}
V & =\frac{1}{2}\left(\operatorname{tr}\left(\text { Ric }_{g} \wedge \text { Ric }_{g}\right)-\frac{1}{4} \operatorname{tr}^{2}\left(\text { Ric }_{g} \wedge \text { Ric }_{g}\right) g\right) \wedge g \\
& =-\left(\text { Ric }_{g} \circ \text { Ric } \left._{g}-\frac{1}{4} \right\rvert\, \text { Ric }\left._{g}\right|^{2} g\right) \wedge g .
\end{aligned}$$
Then
$$\begin{aligned}
\left.\left\lvert\,\left\langle W_{g}+\frac{1}{2} \text { Ric }_{g} \wedge g\right|\right. \text { Ric }_{g} \wedge \stackrel{\circ}{\text { Ric }}_{g}\right\rangle\left.\right|^{2} & =\left\lvert\,\left.\left\langle W_{g}+\frac{1}{2} \text { Ric }_{g} \wedge g \mid T+V\right\rangle\right|^{2}\right. \\
& =\left\lvert\,\left.\left\langle W_{g}+\frac{1}{2 \sqrt{2}} \text { Ric }_{g} \wedge g \mid T+\sqrt{2} V\right\rangle\right|^{2}\right. \\
& \leq \left\lvert\, W_{g}+\frac{1}{2 \sqrt{2}}\right. \text { Ric }\left._{g} \wedge g\right|^{2}|T+\sqrt{2} V|^{2} \\
& =\left(\left.\left|W_{g}\right|^{2}+\frac{1}{4} \right\rvert\, \text { Ric }\left._{g}\right|^{2}\right)\left(|T|^{2}+2|V|^{2}\right) .
\end{aligned}$$
And using the fact that $|u \wedge v|^{2}=|u|^{2}|v|^{2}+\langle u \mid v\rangle^{2}-2\langle u \circ u \mid v \circ v\rangle$, we obtain:
$$\begin{aligned}
\mid \text { Ric }_{g} \wedge \text { Ric }\left._{g}\right|^{2} & =2 \mid \text { Ric }\left._{g}\right|^{4}-2 \mid \text { Ric }_{g} \circ \text { Ric }\left._{g}\right|^{2}, \\
|U|^{2} & \left.=\frac{1}{6} \right\rvert\, \text { Ric }\left._{g}\right|^{4}, \\
|V|^{2} & =2 \mid \text { Ric }_{g} \circ \text { Ric } \left.\left._{g}\right|^{2}-\frac{1}{2} \right\rvert\, \text { Ric }\left._{g}\right|^{4} .
\end{aligned}$$
Therefore
$$|T|^{2}+2|V|^{2}=\mid \text { Ric }_{g} \wedge \text { Ric } \left.\left._{g}\right|^{2}+|V|^{2}-|U|^{2}=\frac{4}{3} \right\rvert\, \text { Ric }\left._{g}\right|^{4} .$$ \(\square\)

Proof of Theorem 1.12 As $\operatorname{tr}\left(\nabla F^{\alpha}\right)=\frac{\alpha}{4} \Delta R$, if $\alpha \neq 0$ and if $g$ is a critical point of $\mathcal{F}^{\alpha}$, then $R_{g}$ is harmonic.
1) If $M$ is compact, then $R_{g}$ is a positive constant (since $Y_{g}>0$ ). Moreover,
$$\begin{aligned}
Y|\operatorname{Ric}|_{4}^{2} & \leq \int_{M}|\nabla| \operatorname{Ric}| |^{2}+\frac{1}{6} R|\stackrel{\circ}{\text { Ric }}|^{2} d v \\
& \leq \int_{M}|\nabla \stackrel{\circ}{\text { Ric }}|^{2}+\frac{1}{6} R|\stackrel{\circ}{\text { Ric }}|^{2} d v
\end{aligned}$$
since, by the Kato inequality, $|\nabla| \stackrel{\circ}{\text { Ric }}^{\circ}| | \leq|\nabla \stackrel{\circ}{\text { Ric }}|$.
On the other hand, according to Proposition 4.4, and since $\langle\stackrel{\circ}{T} u \mid v\rangle=\langle T \mid u \wedge v\rangle$, we have:
$$0=\left\langle\nabla \mathcal{F}^{\alpha} \mid \stackrel{\circ}{\text { Ric }}\right\rangle=\frac{1}{2}\langle\Delta \stackrel{\circ}{\text { Ric }} \mid \stackrel{\circ}{\text { Ric }}\rangle-\left\langle\left. W+\frac{1}{2} \stackrel{\circ}{\text { Ric }} \wedge g \right\rvert\, \stackrel{\circ}{\text { Ric }} \wedge \stackrel{\circ}{\text { Ric }}\right\rangle+\frac{2-\alpha}{12} R|\stackrel{\circ}{\text { Ric }}|^{2},$$
thus
$$\int_{M}\left(|\nabla \stackrel{\circ}{R i c}|^{2}+\frac{2-\alpha}{6} R|\stackrel{\circ}{R i c}|^{2}\right) d v=2 \int_{M}\left\langle\left. W+\frac{1}{2} \stackrel{\circ}{R i c} \wedge g \right\rvert\, \stackrel{\circ}{R i c} \wedge \stackrel{\circ}{R i c}\right\rangle d v_{g} .$$
It follows from Lemma 4.7 and the Hölder inequality that
$$\int_{M}\left(|\nabla \stackrel{\circ}{R i c}|^{2}+\frac{2-\alpha}{6} R|\stackrel{\circ}{R i c}|^{2}\right) d v \leq \frac{4}{\sqrt{3}}\left(\int_{M}|W|^{2}+\frac{1}{4}|\stackrel{\circ}{R i c}|^{2} d v\right)^{\frac{1}{2}}|\stackrel{\circ}{R i c}|_{4}^{2} .$$
Consequently:
$$\left.\left(Y-\frac{4}{\sqrt{3}}\left(\mathcal{F}_{W}+\frac{1}{4} \mathcal{F}_{\text {Ric }}\right)^{\frac{1}{2}}\right) \right\rvert\, \text { Ric } \left._{4}^{2}+\frac{1-\alpha}{6} \int_{M} R \right\rvert\, \text { Ric }\left.\right|^{2} d v \leq 0 .$$
Since $\mathcal{F}_{W}+\frac{1}{4} \mathcal{F}_{\text {Ric }}<\frac{3}{16} Y^{2}$ and $R$ is a positive constant, it follows that $g$ is an Einstein metric.
2) If $M$ is not compact, since $R_{g}$ is harmonic and in $L^{2}(M)$, it is constant (see [Yau76], Theorem 3). As $Y_{g}>0$, it is nonnegative.

Let choose $r>0, x$ a point and $\phi$ a cut-off function such that:
$$\left\{\begin{array}{l}
\phi \equiv 1 \quad \text { on } B_{x}(r), \\
\phi \equiv 0 \quad \text { on } M \backslash B_{x}(2 r), \\
|\nabla \phi|_{\infty} \leq \frac{2}{r} .
\end{array}\right.$$

Let $u=\mid$ Ric $_{g} \mid \phi$. It satisfies:
$$|\nabla u|^{2}=|\phi \nabla| \text { Ric }_{g}|+| \text { Ric }_{g}|\nabla \phi|^{2} \leq(1+\epsilon)|\nabla| \text { Ric } \left._{g}^{\circ}| |^{2} \phi^{2}+\left(1+\frac{1}{\epsilon}\right) \right\rvert\, \text { Ric }\left._{g}^{\circ}\right|^{2}|\nabla \phi|^{2} .$$
Consequently,
$$\begin{aligned}
Y|u|_{4}^{2} & \leq \int_{M}|\nabla u|^{2}+\frac{1}{6} R u^{2} d v \\
& \leq(1+\epsilon) \int_{M}|\nabla| \text { Ric } \left.\left.^{2}\right|^{2} \phi^{2} d v+\frac{1}{6} \int_{M} R u^{2} d v+\left(1+\frac{1}{\epsilon}\right)|\nabla \phi|_{\infty}^{2} \right\rvert\, \text { Ric }_{2}^{2} \\
& \left.\leq(1+\epsilon) \int_{M}\left(|\nabla| \text { Ric } \left.| |^{2}+\frac{1}{6} R \right\rvert\, \text { Ric }\left.\right|^{2}\right) \phi^{2} d v+\left(1+\frac{1}{\epsilon}\right) \frac{4}{r^{2}} \right\rvert\, \text { Ric }\left.\right|_{2} ^{2} \\
& \leq(1+\epsilon)\left(\left.\int_{M}\left(\mid \nabla \text { Ric } \left.\left.\right|^{2}+\frac{1}{6} R \right\rvert\, \text { Ric }\left.\right|^{2}\right) \phi^{2} d v+\frac{4}{\epsilon r^{2}} \right\rvert\, \text { Ric }\left.\right|_{2} ^{2}\right),
\end{aligned}$$
by the Kato inequality.
According to Proposition 4.4 and by writing that $\int_{M}\left\langle\nabla \mathcal{F}^{\alpha}(g)\right|$ Ric $\left._{g}\right\rangle \phi^{2} d v_{g}=0$, we obtain:
$$\int_{M}\langle\Delta \stackrel{\circ}{\text { Ric }} \mid \stackrel{\circ}{\text { Ric }}\rangle \phi^{2} d v+\frac{2-\alpha}{6} \int_{M} R|\stackrel{\circ}{\text { Ric }}|^{2} \phi^{2} d v=2 \int_{M}\left\langle\left. W+\frac{1}{2} \stackrel{\circ}{\text { Ric }} \wedge g \right\rvert\, \stackrel{\circ}{\text { Ric }} \wedge \stackrel{\circ}{\text { Ric }}\right\rangle \phi^{2} d v .$$

For all $\epsilon>0$ :
$$\begin{aligned}
\left.\int_{M}\langle\Delta \stackrel{\circ}{\text { Ric }}| \text { Ric }\right\rangle \phi^{2} d v & =\int_{M} \mid \nabla \text { Ric }\left.\right|^{2} \phi^{2} d v+2 \int_{M}\langle\nabla \stackrel{\circ}{\text { Ric }} \mid \nabla \phi \otimes \stackrel{\circ}{\text { Ric }}\rangle \phi d v \\
& \geq \int_{M}|\nabla \stackrel{\circ}{\text { Ric }}|^{2} \phi^{2} d v-2|\nabla \phi|_{\infty} \mid \text { Ric }\left.\right|_{2}\left(\int_{M}|\nabla \stackrel{\circ}{\text { Ric }}|^{2} \phi^{2} d v\right)^{\frac{1}{2}} \\
& \left.\geq \int_{M}|\nabla \stackrel{\circ}{\text { Ric }}|^{2} \phi^{2} d v-\epsilon \int_{M}|\nabla \stackrel{\circ}{\text { Ric }}|^{2} \phi^{2} d v-\frac{1}{\epsilon}|\nabla \phi|_{\infty}^{2} \right\rvert\, \text { Ric }_{2}^{2} \\
& \geq(1-\epsilon) \int_{M}|\nabla \stackrel{\circ}{\text { Ric }}|^{2} \phi^{2} d v-\frac{4}{\epsilon r^{2}}|\stackrel{\circ}{\text { Ric }}|_{2}^{2} .
\end{aligned}$$
And on the other hand,
$$\begin{aligned}
\left.\int_{M}\left\langle W+\frac{1}{2} \text { Ric } \wedge g\right| \text { Ric } \wedge \text { Ric }\right\rangle \phi^{2} d v & \left.\leq \frac{2}{\sqrt{3}} \int_{M}\left(\left.|W|^{2}+\frac{1}{4} \right\rvert\, \text { Ric }\left.\right|^{2} d v\right)^{\frac{1}{2}} \right\rvert\, \text { Ric }\left.\right|^{2} \phi^{2} d v \\
& \leq \frac{2}{\sqrt{3}}\left(\mathcal{F}_{W}+\frac{1}{4} \mathcal{F}_{\text {Ric }}\right)^{\frac{1}{2}}|u|_{4}^{2} .
\end{aligned}$$
It follows that
$$(1-\epsilon)\left(\left.\int_{M}\left(\mid \nabla \text { Ric } \left.\left._{g}\right|^{2}+\frac{1}{6} R \right\rvert\, \text { Ric }\left._{g}\right|^{2}\right) \phi^{2} d v \leq \frac{4}{\sqrt{3}}\left(\mathcal{F}_{W}+\frac{1}{4} \mathcal{F}_{\text {Ric }}\right)^{\frac{1}{2}}|u|_{4}^{2}+\frac{4}{\epsilon r^{2}} \right\rvert\, \text { Ric }_{2}^{2} .\right.$$
Consequently,
$$\left.\frac{1-\epsilon}{1+\epsilon} Y|u|_{4}^{2} \leq \frac{4}{\sqrt{3}}\left(\mathcal{F}_{W}+\frac{1}{4} \mathcal{F}_{\text {Ric }}\right)^{\frac{1}{2}}|u|_{4}^{2}+\frac{8}{\epsilon r^{2}} \right\rvert\, \text { Ric }_{2}^{\circ},$$
thus
$$\left.\left(\frac{1-\epsilon}{1+\epsilon} Y-\frac{4}{\sqrt{3}}\left(\mathcal{F}_{W}+\frac{1}{4} \mathcal{F}_{\text {Ric }}\right)^{\frac{1}{2}}\right)\left(\int_{M} \mid \text { Ric }^{\circ} \phi^{4} d v\right)^{\frac{1}{2}} \leq \frac{8}{\epsilon r^{2}} \right\rvert\, \text { Ric }_{2}^{\circ} .$$
We can choose $\epsilon>0$ such that
$$\frac{1-\epsilon}{1+\epsilon} Y-\frac{4}{\sqrt{3}}\left(\mathcal{F}_{W}+\frac{1}{4} \mathcal{F}_{\text {Ric }}\right)^{\frac{1}{2}}>0 .$$
Then, letting $r$ go to infinity, we see that $g$ is Einstein.
It follows that $g$ has harmonic Weyl tensor $(-2 \delta W=\mathrm{D} A=\mathrm{D} \stackrel{\circ}{\text { Ric }}=0)$, and as it also satisfies $\mathcal{F}_{W}<\frac{3}{16} Y^{2}<\frac{25}{54} Y^{2}$, it is conformally flat according to Proposition 4.1. Hence, $g$ has constant sectional curvature. \(\square\)

\section*{5 Yamabe, Sobolev and collapsing}

Definition 5.1 (Best second Sobolev constant). Let $(M, g)$ be a complete Riemannian $n$-manifold, $n \geq 3$ and $A$ be a positive real number.

Let define the best second Sobolev constant relative to $A$ by:
$$\mathcal{B}_{A}(g)=\inf \left\{B \in \mathbb{R},|u|_{\frac{2 n}{n-2}} \leq A|\nabla u|_{2}+B|u|_{2}, \forall u \in H_{1}^{2}(M)\right\},$$
with the convention $\inf (\emptyset)=+\infty$
If $M$ is compact, $\mathcal{B}_{A}<\infty$ for all $A \geq Y_{S^{n}}^{-\frac{1}{2}}$.

Proposition 5.2. Let $n \geq 3$ be an integer, let $p$ be in $\left(\frac{n}{2} ; \infty\right]$ and let $A$ be a positive number. There exists $C(n, p)$ such that if $(M, g)$ is a complete Riemannian $n$-manifold with $Y_{g} \geq \frac{2}{A^{2}}$, then
$$\mathcal{B}_{A}(g) \leq\left(C A^{2}\left|R_{g}\right|_{p}\right)^{\frac{p}{2 p-n}} .$$
Proof. Let $u$ be in $H_{1}^{2}(M)$. Since $Y_{g} \geq \frac{2}{A^{2}}$, then using the Hölder inequality,
$$\begin{aligned}
|u|_{\frac{2 n}{n-2}}^{2} & \leq \frac{A^{2}}{2}\left(|\nabla u|_{2}^{2}+\frac{n-2}{4(n-1)} \int_{M} R_{g} u^{2} d v_{g}\right) \\
& \leq \frac{A^{2}}{2}\left(|\nabla u|_{2}^{2}+\frac{n-2}{4(n-1)}\left|R_{g}\right|_{p}|u|_{\frac{2 p}{p-1}}^{2}\right) \\
& \leq \frac{A^{2}}{2}\left(|\nabla u|_{2}^{2}+\frac{n-2}{4(n-1)}\left|R_{g}\right|_{p}|u|_{2}^{2\left(1-\frac{n}{2 p}\right)}|u|_{\frac{2 n}{n-2}}^{2 \frac{n}{2 p}}\right) \\
& \leq \frac{A^{2}}{2}|\nabla u|_{2}^{2}+\frac{1}{2}|u|_{\frac{2 n}{n-2}}^{2}+\left(1-\frac{n}{2 p}\right)\left(\frac{n}{p}\right)^{\frac{n}{2 p-n}}\left(\frac{n-2}{4(n-1)} \frac{A^{2}}{2}\left|R_{g}\right|_{p}\right)^{\frac{2 p}{2 p-n}}|u|_{2}^{2} \\
& \leq \frac{A^{2}}{2}|\nabla u|_{2}^{2}+\frac{1}{2}|u|_{\frac{2 n}{n-2}}^{2}+\frac{1}{2} C^{2}\left(A^{2}\left|R_{g}\right|_{p}\right)^{\frac{2 p}{2 p-n}}|u|_{2}^{2},
\end{aligned}$$
where $C$ only depends on $n$ and $p$. Consequently, we get
$$\begin{aligned}
|u|_{\frac{2 n}{n-2}}^{2} & \leq A^{2}|\nabla u|_{2}^{2}+C^{2}\left(A^{2}\left|R_{g}\right|_{p}\right)^{\frac{2 p}{2 p-n}}|u|_{2}^{2} \\
& \leq\left(A|\nabla u|_{2}+C\left(A^{2}\left|R_{g}\right|_{p}\right)^{\frac{p}{2 p-n}}|u|_{2}\right)^{2},
\end{aligned}$$
which proves the claim. \(\square\)

Proposition 5.3. Let $\left(g_{i}\right)_{i \in I}$ be a family of metrics on a manifold $M$ with a uniform $C^{0}$ curvature bound. Then the three following assertions are equivalent:
$$\begin{aligned}
& \text { (i) } \quad \inf _{i \in I} \operatorname{inj}_{M}\left(g_{i}\right)=0, \\
& \text { (ii) } \quad \inf _{i \in I} \inf _{x \in M} \operatorname{Vol}_{g_{i}}\left(B_{x}(1)\right)=0, \\
& \text { (iii) } \quad \forall A \in \mathbb{R} \sup _{i \in I}\left(\mathcal{B}_{A}\left(g_{i}\right)\right)=\infty .
\end{aligned}$$
We say that the family collapses with bounded curvature.
We will need the following lemmas:
Lemma 5.4 (Cheeger, see [Pet98], Lemma 4.5). For all $C>0$ and $v_{0}>0$ there exists $i_{0}\left(n, C, v_{0}\right)>0$ such that the following property is true:

If $(M, g)$ is a complete Riemannian $n$-manifold such that $\operatorname{vol}(B(x, 1)) \geq v_{0}$ for all $x$ in $M$ and $\left|R m_{g}\right|_{\infty} \leq C$, then $\operatorname{inj}_{g}(M) \geq i_{0}$.

Lemma 5.5 (Carron, see [Heb96], Lemma 3.2). Let $(M, g)$ be a complete Riemannian $n$-manifold. Then
$$\forall x \in M, \quad \operatorname{vol}(B(x, 1)) \geq\left(2^{\frac{n(n+4)}{2}} \max \left(A, \mathcal{B}_{A}\right)\right)^{-1} .$$
Proof of the Proposition. If $\operatorname{inj}_{x}\left(g_{i}\right) \geq i_{0}$, with $i_{0} \in(0,2)$, and if the sectional curvatures are bounded by $K>0$, then by the Bishop-Gromov comparison theorem,
$$\operatorname{Vol}_{g_{i}}\left(B_{x}(1)\right) \geq \operatorname{Vol}_{g_{i}}\left(B_{x}\left(\frac{i_{0}}{2}\right)\right) \geq \operatorname{Vol}_{K}\left(\frac{i_{0}}{2}\right),$$
where $\operatorname{Vol}_{K}\left(\frac{i_{0}}{2}\right)$ is the volume of a ball of radius $\frac{i_{0}}{2}$ in the space of constant curvature $K$.
Conversely, if the volume of unit balls is uniformly bounded from below, then by Lemma 5.4, so is the injectivity radius.

Finally, the equivalence between the existence of a lower bound on the volume of unit balls and an upper bound on the Sobolev constant comes from Theorem 3.14 of [Heb96] and Lemma 5.5. \(\square\)

Proposition 5.6. Let $M$ be a manifold. Let $\left(g_{i}\right)_{i \in I}$ be a family of complete metrics on $M$ with a uniform $C^{0}$ curvature bound. If
$$\inf _{i \in I}\left(Y_{g_{i}}(M)\right)>0,$$
then the family doesn't collapse with bounded curvature.
Proof. It results from Proposition 5.3 and Proposition 5.2 with $p=\infty$. \(\square\)

\section*{6 Bando-Bernstein-Shi estimates}

For tensors $T, T_{1}, \ldots, T_{j}$ and nonnegative integers $j$ and $k$, let write:
$$\begin{aligned}
\mathcal{P}^{k}\left(T_{1}, \ldots, T_{j}\right) & =\sum_{i_{1}+\cdots+i_{j}=k} \nabla^{i_{1}} T_{1} * \cdots * \nabla^{i_{j}} T_{j}, \\
\mathcal{P}_{j}^{k}(T) & =\sum_{i_{1}+\cdots+i_{j}=k} \nabla^{i_{1}} T * \cdots * \nabla^{i_{j}} T .
\end{aligned}$$

Proposition 6.1. Let $(M, g)$ be a compact Riemannian $n$-manifold.
Let $P: \mathcal{S}_{+}^{2}(M) \rightarrow \mathcal{S}^{2}(M)$ be a smooth map of the form
$$P(g)=\delta \tilde{\delta} R m_{g}+a \Delta R_{g} g+b \nabla^{2} R_{g}+R m_{g} * R m_{g} .$$
Then for all integers $k \geq 0$,
$$\begin{gathered}
\left(\left|\nabla^{k} R m\right|_{2}^{2}\right)_{g}^{\prime}\left(P_{g}\right)+\left|\nabla^{k+2} R m_{g}\right|_{2}^{2}-\frac{a}{2}\left|\nabla^{k+2} R_{g}\right|_{2}^{2}=\int_{M} \mathcal{P}_{3}^{2 k+2}\left(R m_{g}\right)+\mathcal{P}_{4}^{2 k}\left(R m_{g}\right) d v_{g}, \\
\left(\left|\nabla^{k} R\right|_{2}^{2}\right)_{g}^{\prime}\left(P_{g}\right)+(1-2 a(n-1))\left|\nabla^{k+2} R_{g}\right|_{2}^{2}=\int_{M} \mathcal{P}_{3}^{2 k+2}\left(R m_{g}\right)+\mathcal{P}_{4}^{2 k}\left(R m_{g}\right) d v_{g},
\end{gathered}$$
where the coefficients of the lower order terms only depend on $n, k$ and $P$.
Proof. We write $\operatorname{lot}_{k}(g)$ for any term of the form
$$\int_{M} \mathcal{P}_{3}^{2 k+2}\left(R m_{g}\right)+\mathcal{P}_{4}^{2 k}\left(R m_{g}\right) d v_{g}$$
and for any $(p, p)$ tensor $T$, we define the $(2,0)$ tensor $\nabla^{k} T \underline{\vee} \nabla^{k} T$ by:
$$\left(\nabla^{k} T \underline{\vee} \nabla^{k} T\right)(X, Y)=\sum_{j=1}^{k}\left\langle\nabla^{j-1} \nabla_{X} \nabla^{k-j} T \mid \nabla^{j-1} \nabla_{Y} \nabla^{k-j} T\right\rangle .$$

Then we have:
$$\begin{aligned}
\left(\int_{M}\left|\nabla^{k} R m\right|^{2} d v\right)_{g}^{\prime}\left(P_{g}\right)=2\left(\left(\nabla^{k} R m\right)_{g}^{\prime}\left(P_{g}\right) \mid \nabla^{k} R m_{g}\right)_{L^{2}} & \\
& -\left(P_{g} \mid \nabla^{k} R m_{g} \unrhd \nabla^{k} R m_{g}\right)_{L^{2}}+\frac{1}{2} \int_{M}\left|\nabla^{k} R m_{g}\right|^{2} \operatorname{tr}\left(P_{g}\right) d v_{g} .
\end{aligned}$$

Using (12) in Proposition 9.7, it follows that:
$$\left(\int_{M}\left|\nabla^{k} R m\right|^{2} d v\right)_{g}^{\prime}\left(P_{g}\right)=2\left(\nabla^{k} R m_{g}^{\prime}\left(P_{g}\right) \mid \nabla^{k} R m_{g}\right)_{L^{2}}+\operatorname{lot}_{k}(g),$$
then, by (14) in Proposition 9.7,
$$\left(\int_{M}\left|\nabla^{k} R m\right|^{2} d v\right)_{g}^{\prime}\left(P_{g}\right)=2\left(R m_{g}^{\prime}\left(P_{g}\right) \mid \Delta^{k} R m_{g}\right)_{L^{2}}+\operatorname{lot}_{k}(g),$$
using that $R m_{g}^{\prime}=-\frac{1}{2} \mathrm{D} \tilde{\mathrm{D}}+R m *$. (Proposition 9.5) and (15) in Proposition 9.8, we get:
$$\left(\int_{M}\left|\nabla^{k} R m\right|^{2} d v\right)_{g}^{\prime}\left(P_{g}\right)=-\left(\Delta^{2} R m_{g}+a \mathrm{D} \tilde{\mathrm{D}}\left(\Delta R_{g} g\right)+b \mathrm{D} \tilde{\mathrm{D}} \tilde{\mathrm{D}} R_{g} \mid \Delta^{k} R m_{g}\right)_{L^{2}}+\operatorname{lot}_{k}(g) .$$
It follows from (8) in Proposition 9.6 that:
$$\left(\int_{M}\left|\nabla^{k} R m\right|^{2} d v\right)_{g}^{\prime}\left(P_{g}\right)=-\left(R m_{g} \mid \Delta^{k+2} R m_{g}\right)_{L^{2}}-a\left(\Delta R_{g} \mid \operatorname{tr}\left(\tilde{\delta} \delta \Delta^{k} R m_{g}\right)\right)_{L^{2}}+\operatorname{lot}_{k}(g),$$
then by (14) in Proposition 9.7 and (18) in Proposition 9.8,
$$\left(\int_{M}\left|\nabla^{k} R m\right|^{2} d v\right)_{g}^{\prime}\left(P_{g}\right)=-\left(R m_{g} \mid \delta^{k+2} \nabla^{k+2} R m_{g}\right)_{L^{2}}-a\left(\Delta R_{g} \mid \Delta^{k} \tilde{\delta} \delta R i c_{g}\right)_{L^{2}}+l o t_{k}(g),$$
and by Proposition 9.2,
$$\left(\int_{M}\left|\nabla^{k} R m\right|^{2} d v\right)_{g}^{\prime}\left(P_{g}\right)=-\int_{M}\left|\nabla^{k+2} R m_{g}\right|^{2} d v_{g}+\frac{a}{2}\left(\Delta R_{g} \mid \Delta^{k+1} R_{g}\right)_{L^{2}}+\operatorname{lot}_{k}(g) .$$
Finally, by (14) in Proposition 9.7,
$$\left(\int_{M}\left|\nabla^{k} R m\right|^{2} d v\right)_{g}^{\prime}\left(P_{g}\right)=-\int_{M}\left|\nabla^{k+2} R m_{g}\right|^{2} d v_{g}+\frac{a}{2} \int_{M}\left|\nabla^{k+2} R_{g}\right|^{2} d v_{g}+l o t_{k}(g) .$$

On the other hand,
$$\begin{aligned}
\left(\int_{M}\left|\nabla^{k} R\right|^{2} d v\right)_{g}^{\prime}\left(P_{g}\right)=2\left(\left(\nabla^{k} R\right)_{g}^{\prime}\left(P_{g}\right) \mid\right. & \left.\nabla^{k} R_{g}\right)_{L^{2}} \\
& -\left(P_{g} \mid \nabla^{k} R_{g} \underline{\vee} \nabla^{k} R_{g}\right)_{L^{2}}+\frac{1}{2} \int_{M}\left|\nabla^{k} R\right|^{2} t r\left(P_{g}\right) d v_{g} .
\end{aligned}$$

Then by (12) and (14) of Proposition 9.7,
$$\left(\int_{M}\left|\nabla^{k} R\right|^{2} d v\right)_{g}^{\prime}\left(P_{g}\right)=2\left(R_{g}^{\prime}\left(P_{g}\right) \mid \Delta^{k} R_{g}\right)_{L^{2}}+\operatorname{lot}_{k}(g),$$
since $\delta \mathrm{D}\left(R_{g} g\right)=\Delta R_{g} g+\nabla^{2} R_{g}$ (Proposition 9.3) and $R_{g}^{\prime}=\operatorname{tr} \delta \mathrm{D}+R m *$ (Proposition 9.5), we get:
$$\left.\left(\int_{M}\left|\nabla^{k} R\right|^{2} d v\right)_{g}^{\prime}\left(P_{g}\right)=2\left(R_{g}^{\prime}\left(\delta \tilde{\delta} R m_{g}+a \delta \mathrm{D}\left(R_{g} g\right)\right)+(b-a) \operatorname{tr} \delta \mathrm{DD} \tilde{\mathrm{D}} R_{g}\right) \mid \Delta^{k} R_{g}\right)_{L^{2}}+\operatorname{lot}_{k}(g),$$
by (16) and (17) of Proposition 9.8 and by (8) of Proposition 9.6,
$$\left(\int_{M}\left|\nabla^{k} R\right|^{2} d v\right)_{g}^{\prime}\left(P_{g}\right)=-(1-2 a(n-1))\left(\Delta^{2} R_{g} \mid \Delta^{k} R_{g}\right)_{L^{2}}+\operatorname{lot}_{k}(g),$$
and finally, by (14) of Proposition 9.7,
$$\left(\int_{M}\left|\nabla^{k} R\right|^{2} d v\right)_{g}^{\prime}\left(P_{g}\right)=-(1-2 a(n-1)) \int_{M}\left|\nabla^{k+2} R_{g}\right|^{2} d v_{g}+\operatorname{lot}_{k}(g) .$$ \(\square\)

Proof of Theorem 1.5 Let define
$$\mathcal{R}_{k}=\int_{M}\left|\nabla^{k} R m\right|^{2} d v+\frac{a_{+}}{1-2 a_{+}(n-1)} \int_{M}\left|\nabla^{k} R\right|^{2} d v$$
and
$$c_{a}=\frac{1-2 a_{+}(n-1)}{2} .$$

Lemma 6.2. There exists $C(n, P, k)$ such that for all integers $k \geq 0$
$$\left(\mathcal{R}_{k}\right)_{g}^{\prime}\left(P_{g}\right)+c_{a} \mathcal{R}_{k+2}(g) \leq C\left|R m_{g}\right|_{\infty}^{k+2} \mathcal{R}_{0}(g) .$$
Proof.
$$\begin{aligned}
\left(\mathcal{R}_{k}\right)_{g}^{\prime}\left(P_{g}\right)+c_{a} \mathcal{R}_{k+2}(g) & =-\left(1-c_{a}\right)\left|\nabla^{k+2} R m_{g}\right|_{2}^{2}-\frac{1}{2}\left(a_{+}-a\right)\left|\nabla^{k+2} R_{g}\right|_{2}^{2}+\operatorname{lot}_{k}(g) \\
& \leq-\frac{1}{2}\left|\nabla^{k+2} R m_{g}\right|_{2}^{2}+\operatorname{lot}_{k}(g) \\
& \leq C\left|R m_{g}\right|_{\infty}^{k+2} \mathcal{F}_{R m}(g) \text { by Proposition } 9.15 \\
& \leq C\left|R m_{g}\right|_{\infty}^{k+2} \mathcal{R}_{0}(g) .
\end{aligned}$$ \(\square\)
Proof of the Theorem. Let define
$$f_{k}(t)=\sum_{j=0}^{k} \frac{c_{a}^{j} t^{j}}{j!} \mathcal{R}_{2 j}\left(g_{t}\right),$$
then
$$\begin{aligned}
f_{k}^{\prime}(t) & =\sum_{j=0}^{k-1} \frac{c_{a}^{j} t^{j}}{j!}\left(\left(\mathcal{R}_{2 j}\right)_{g_{t}}^{\prime}\left(P_{g_{t}}\right)+c_{a} \mathcal{R}_{2 j+2}\left(g_{t}\right)\right)+\frac{c_{a}^{k} t^{k}}{k!}\left(\left(\mathcal{R}_{2 k}\right)_{g_{t}}^{\prime}\left(P_{g_{t}}\right)\right. \\
& \leq \sum_{j=0}^{k} \frac{c_{a}^{j} t^{j}}{j!} C_{j}\left|R m_{g_{t}}\right|_{\infty}^{j+2} \mathcal{R}_{0}\left(g_{t}\right) \\
& \leq C^{\prime}\left|R m_{g_{t}}\right|_{\infty}^{2} \mathcal{R}_{0}\left(g_{t}\right)\left(1+\left|R m_{g_{t}}\right|_{\infty} t\right)^{k} \quad \text { with } C^{\prime}=C^{\prime}(n, P, k) \\
& \leq C^{\prime} D^{2} f_{k}(t)(1+D t)^{k} .
\end{aligned}$$

It follows that
$$\left(\ln f_{k}\right)^{\prime}(t) \leq C^{\prime} D^{2}(1+D t)^{k},$$
and therefore
$$f_{k}(t) \leq f_{k}(0) \exp \left(\frac{C^{\prime} D}{k+1}(1+D t)^{k+1}\right),$$
then
$$\begin{aligned}
\left|\nabla^{2 k} R m_{g_{t}}\right|_{2}^{2} & \leq \mathcal{R}_{2 k}\left(g_{t}\right) \\
& \leq \frac{k!}{c_{a}^{k} t^{k}} f_{k}(t) \\
& \leq \frac{k!}{c_{a}^{k} t^{k}} R_{0}\left(g_{0}\right) \exp \left(\frac{C^{\prime} D}{k+1}(1+D t)^{k+1}\right) \\
& \leq \frac{1}{t^{k}} \mathcal{F}_{R m}\left(g_{0}\right) \exp \left(C^{\prime \prime}+\frac{C^{\prime} D}{k+1}(1+D t)^{k+1}\right) \\
& \leq \frac{1}{t^{k}} \mathcal{F}_{R m}\left(g_{0}\right) \exp \left(C(1+D)(1+D t)^{k+1}\right) .
\end{aligned}$$ \(\square\)

\section*{7 Compactness of sets of solutions}

In order to make a "blow-up" at a singular time, we will need a compactness result for solutions of our equations. We can have a similar approach to that of Hamilton in [Ham95], consisting in using the derivative estimates on the curvature to apply the following theorem:

Theorem 7.1 (Hamilton, see [Ham95]). Let $\left(M_{i}, g_{i}, x_{i}\right)_{i \in I}$ be a sequence of pointed complete Riemannian manifolds with uniform $C^{0}$ bounds on all the derivatives of the curvature. If the injectivity radius inj $_{x_{i}}\left(g_{i}\right)$ is uniformly bounded from below by a positive constant, we can find a converging subsequence in the pointed $C^{\infty}$ topology.

However, as in [Str08], the compulsory use of integral estimates instead of pointwise ones forces us to add a few extra hypotheses. The proof of the following theorem is similar to that of Theorem 7.1 of [Str08]:

Theorem 7.2. Let $\left(g_{i}(t), x_{i}\right), t \in\left(-T_{1}, T_{2}\right)$ be pointed solutions of $E_{P}$ on a Riemannian manifold $M$.

Suppose that the family of metrics $\left(g_{i}(t)\right)_{i \in \mathbb{N}, t \in\left(-T_{1}, T_{2}\right)}$ has a uniform (in $i$ and $t$ ) $C^{0}$ bound on curvature and doesn't collapse with bounded curvature. Suppose also that there exists $C$ such that $\lim _{t \rightarrow-T_{1}}\left|R m_{g_{i}}\right|_{2} \leq C$. Then there exists a subsequence of $\left(M, g_{i}(t), x_{i}\right)$ converging in the pointed $C^{\infty}$ topology to a pointed solution $\left(M_{\infty}, g_{\infty}(t), x_{\infty}\right)$ of $E_{P}$.

\section*{8 Proofs of the main theorems}

Proof of Theorem 1.7 We have to show that if $T<\infty$ and if there exists $D<\infty$ such that $|R m|_{\infty}\left(g_{t}\right) \leq D$ for all $t$ in $[0 ; T)$, then the family $\left(g_{t}\right)$ collapses with bounded curvature.

Suppose that the family does not collapse with bounded curvature. Then by Proposition 5.3, there exists $A>0$ and $B<\infty$ such that $\mathcal{B}_{A}\left(g_{t}\right) \leq B$ for all $t$ in $[0 ; T)$.

The estimates (Theorem 1.5) show that all the derivatives of the curvature have uniform $L^{2}$ bounds on $[T / 2, T)$ :
$$\begin{aligned}
\left|\nabla^{2 k} R m_{g_{t}}\right|_{2}^{2} & \leq \mathcal{F}_{R m}\left(g_{0}\right) \frac{e^{C(1+D)(1+D t)^{k+1}}}{t^{k}} \\
& \leq C(n, k, P, T, D) \mathcal{F}_{R m}\left(g_{0}\right) .
\end{aligned}$$

Then, by Sobolev inequalities (Proposition 9.21), and as
$$\left|\nabla^{2 k+1} R m\right|_{2}^{2} \leq C\left|\nabla^{2 k} R m\right|_{2}\left|\nabla^{2 k+2} R m\right|_{2}$$
(Lemma 9.10), this shows that all the derivatives of the curvature have uniform $C^{0}$ bounds for the metric $g_{t}$ on $[T / 2, T)$ :
$$\begin{aligned}
\left|\nabla^{i} R m\right|_{\infty, g_{t}} & \leq C\left|\nabla^{i} R m\right|_{2}^{\frac{1}{n+1}}\left|\nabla^{i} R m\right|_{H_{1}^{2}(A)}^{\frac{n-2 k+1}{n+1}}\left|\nabla^{i} R m\right|_{H_{k}^{2}(A)}^{\frac{2 k-1}{n+1}} \\
& \leq C(n, i, P, T, A, B, D) \mathcal{F}_{R m}\left(g_{0}\right)^{\frac{1}{2}},
\end{aligned}$$
where $k=\left[\frac{n}{2}\right]+1$.
Then, by a classical argument, all the metrics $g_{t}$ are equivalent and the solution extends beyond $T$. This contradicts the maximality of the solution. \(\square\)

Proof of Theorem 1.8 The third case of Theorem 1.7 cannot occur. Indeed, if the Yamabe invariant is uniformly bounded from below by a positive constant, and if the curvature has a uniform $C^{0}$ bound, Proposition 5.6 assures that the family $\left(g_{t}\right)$ doesn't collapse with bounded curvature. \(\square\)

Proof of Theorem 1.9 1. If the curvature remains uniformly bounded by some constant $D$ along the flow, then by Theorem 1.8, $T=\infty$.

Moreover, as $\left|R m_{g_{t}}\right|_{2} \leq C\left(1+|R m|_{\infty}\right)^{1-\frac{n}{4}},\left|R m_{g_{t}}\right|_{2}$ also remains uniformly bounded.
We can now apply the estimates of Theorem 1.5 to $\left(g_{t}\right)_{t \in[N, N+2)}$, solution of $E_{P}(g(N))$ where $N$ is a nonnegative integer. It shows that for all $t \in(N, N+2)$
$$\int_{M}\left|\nabla^{2 k} R m_{g_{t}}\right| d v_{g_{t}} \leq \mathcal{F}_{R m}(g(N)) \frac{e^{C^{\prime}(1+D)(1+(t-N) D)^{k+1}}}{(t-N)^{k}},$$
then by using the assumption on $|R m|_{2}$, for all $t \in[N+1, N+2$ ):
$$\int_{M}\left|\nabla^{2 k} R m_{g_{t}}\right| d v_{g_{t}} \leq C(1+D)^{1-\frac{n}{4}} e^{C^{\prime}(1+D)(1+2 D)^{k+1}}$$
It follows that all the derivatives of the curvature have a uniform $L^{2}$ bound on $[0, \infty)$.
Furthermore, by Proposition 5.2 with $p=\infty$, there exists $A$ such that $\mathcal{B}_{A}$ has a uniform bound. Then the metric doesn't collapse with bounded curvature by Proposition 5.3, and the Sobolev inequality of Proposition 9.21 shows that the curvature has uniform $C^{k}$ bounds.

By compactness theorem 7.1, we can find a convergent subsequence of every sequence $\left(M, g\left(t_{i}\right), x_{i}\right)$.
\begin{itemize}
\item[2.] If $\varlimsup_{t \rightarrow T}\left|R m_{g(t)}\right|_{\infty}=\infty$, we can choose a sequence $\left(t_{i}\right)$ such that
$$\left|R m_{g\left(t_{i}\right)}\right|_{\infty}=\sup _{t \leq t_{i}}\left|R m_{g(t)}\right|_{\infty}, \quad t_{i} \rightarrow T \quad \text { and } \quad\left|R m_{g\left(t_{i}\right)}\right|_{\infty} \rightarrow \infty .$$
\end{itemize}

Let define $\alpha_{i}=\left|R m_{g\left(t_{i}\right)}\right|_{\infty}$ and
$$g_{i}(t)=\alpha_{i} g\left(t_{i}+\frac{t}{\alpha_{i}^{2}}\right) .$$

Then $g_{i}$ is a solution of $E_{P}$ on $\left[-\alpha_{i}^{2} t_{i}, \alpha_{i}^{2}\left(T-t_{i}\right)\right)$.
Let choose $T_{1}>0$. Then for $i$ big enough, $g_{i}$ are solutions of $E_{P}$ on $\left[-T_{1}, 0\right]$
The curvature of $g_{i}(t)$ is uniformly bounded by 1 , and its Yamabe invariant is uniformly bounded from below by $Y_{0}$ (as it is scale invariant). By Proposition 5.6, the family doesn't collapse with bounded curvature. Moreover, as $\left|R m_{g_{t}}\right|_{2} \leq C\left(1+\left|R m_{g_{t}}\right|_{\infty}\right)^{1-\frac{n}{4}}$, for $i$ big enough
$$\left|R m_{g_{i}\left(-T_{1}\right)}\right|_{2} \leq C\left(\frac{1}{\alpha_{i}}\left(1+\left|R m_{g\left(t_{i}-\frac{T_{1}}{\alpha_{i}^{2}}\right)}\right|_{\infty}\right)\right)^{1-\frac{n}{4}} \leq 2 C .$$

Let choose $x_{i}$ such that $\left|R m_{g\left(t_{i}\right)}\left(x_{i}\right)\right|=\alpha_{i}$.
Compactness theorem 7.2 applies, and shows that a subsequence of $\left(M, g_{i}(t), x_{i}\right)$ converges in the pointed $C^{\infty}$ topology to a pointed solution $\left(M_{\infty}, g_{\infty}(t), x_{\infty}\right)$.

Moreover, $\left|R m_{g_{\infty}(0)}\left(x_{\infty}\right)\right|=1$, so the limit manifold $\left(M_{\infty}, g_{\infty}(0)\right)$ is not flat.
Now, suppose that there exists some $p>\frac{n}{2}$ such that $\left|R m_{g(t)}\right|_{p}$ is uniformly bounded. Then $\left|R m_{g_{i}(0)}\right|_{p}=\alpha_{i}^{\frac{n}{2 p}-1}\left|R m_{g\left(t_{i}\right)}\right|_{p}$ tends to 0, so $g_{\infty}(0)$ is flat, a contradiction. \(\square\)

Proof of Theorem 1.11 We will need the following Lemma:
Lemma 8.1. If $(M, g)$ is a complete Riemannian manifold such that
$$\inf _{x \in M} \operatorname{Vol}_{g}\left(B_{x}(1)\right)>0,$$
then $M$ is compact if and only if $(M, g)$ has finite volume.
Proof. If $M$ is compact, it has finite volume. Suppose that $M$ is not compact and choose $x$ in $M$. We can find a sequence of points $\left(x_{k}\right)$ such that $x_{k}$ is in $B_{x}(k+1) \backslash B_{x}(k)$. Then the balls $B_{x_{3 k}}(1)$ are two by two disjoint, and thus
$$\operatorname{Vol}_{g}(M) \geq \sum_{k \geq 0} \operatorname{Vol}_{g}\left(B_{x_{3 k}}(1)\right)=\infty .$$ \(\square\)

Proof of the Theorem. We can suppose that $\mathcal{F}^{\alpha}\left(g_{0}\right)<(1-\alpha) 8 \pi^{2} \chi(M)$. Indeed, if the equality holds, as
$$\partial_{t} \mathcal{F}^{\alpha}\left(g_{t}\right)=-2 \int_{M}\left|\nabla \mathcal{F}^{\alpha}\left(g_{t}\right)\right|^{2} d v_{g_{t}},$$
either $g_{0}$ is a critical point of $\mathcal{F}^{\alpha}$, and the solution of $E_{P}\left(g_{0}\right)$ is constant, or the inequality becomes immediately strict for $t>0$. Then, $\mathcal{F}^{\alpha}$ being decreasing along its gradient flow, the inequality is preserved.

Lemma 4.5 shows that $Y_{g(t)} \geq Y_{0}$, with
$$Y_{0}=\left(\frac{2}{3}\left((1-\alpha) 8 \pi^{2} \chi(M)-\mathcal{F}^{\alpha}\left(g_{0}\right)\right)\right)^{\frac{1}{2}}>0 .$$

Because we chose $\alpha>0,|R m|_{2}$ is uniformly bounded along the flow. Indeed, since $\mathcal{F}^{\alpha}$ is decreasing, $\mathcal{F}^{\alpha}\left(g_{t}\right) \leq \mathcal{F}^{\alpha}\left(g_{0}\right)$. It follows that
$$\begin{aligned}
|W|_{2}^{2} & \leq \frac{1}{1-\alpha} \mathcal{F}^{\alpha}\left(g_{0}\right), \\
\mid \text { Ric }_{2}^{2} & \leq \frac{2}{\alpha} \mathcal{F}^{\alpha}\left(g_{0}\right), \\
|R|_{2}^{2} & =24 \mathcal{F}_{2}+12|\stackrel{\circ}{\text { Ric }}|_{2}^{2} \leq 24\left(8 \pi^{2} \chi(M)+\frac{1}{\alpha} \mathcal{F}^{\alpha}\left(g_{0}\right)\right) .
\end{aligned}$$

We can apply Theorem 1.9, and we only have to show that the limit manifold is non-compact, Bach-flat and scalar-flat when a singularity appears, and that we can choose $\left(t_{i}\right)$ such that the limit is diffeomorphic to $M$ and critical for $\mathcal{F}^{\alpha}$ when there is no singularity.

First note that the volume is constant along the flow:
$$\partial_{t} \operatorname{Vol}_{g}(M)=\int_{M} \frac{1}{2} \operatorname{tr}\left(P_{g}\right) d v_{g}=0$$
and that since $\left(g_{i}\right)$ is not collapsing with bounded curvature, the limit manifold satisfies
$$\inf _{x \in M} \operatorname{Vol}_{g}\left(B_{x}(1)\right)>0 .$$

In the first case, when the curvature remains bounded, this implies that the limit manifold $M_{\infty}$ has finite volume, then is compact by Lemma 8.1. By the definition of the pointed $C^{\infty}$ topology, this implies that $M_{\infty}$ is diffeomorphic to $M$.

In the second case, when a singularity occurs, as $\operatorname{Vol}_{g_{i}}(M)=\alpha_{i}^{\frac{n}{2}} \operatorname{Vol}_{g}(M)$ tends to infinity, the limit manifold cannot be compact, since it would be diffeomorphic to $M$ and of infinite volume.

Furthermore, for all $t$ in $[0, T)$,
$$\int_{0}^{t}\left|\nabla \mathcal{F}^{\alpha}\left(g_{s}\right)\right|_{2}^{2} d s=\mathcal{F}^{\alpha}\left(g_{0}\right)-\mathcal{F}^{\alpha}\left(g_{t}\right)$$
therefore
$$\int_{0}^{T}\left|\nabla \mathcal{F}^{\alpha}\left(g_{s}\right)\right|_{2}^{2} d s \leq \mathcal{F}^{\alpha}\left(g_{0}\right)<\infty$$

If there is no singularity, we get
$$\int_{0}^{\infty}\left|\nabla \mathcal{F}^{\alpha}\left(g_{s}\right)\right|_{2}^{2} d s<\infty$$
so there exists a sequence $t_{i} \rightarrow \infty$ such that $\left|\nabla \mathcal{F}^{\alpha}\left(g_{t_{i}}\right)\right|_{2} \rightarrow 0$. If we take this sequence in Theorem 1.9, any converging subsequence converges to a critical point of $\mathcal{F}^{\alpha}$.

At a singularity, by a change of variable:
$$\int_{-T_{1}}^{0}\left|\nabla \mathcal{F}^{\alpha}\left(g_{i}(t)\right)\right|_{2}^{2} d t=\int_{t_{i}-\frac{T_{1}}{\alpha_{i}^{2}}}^{t_{i}}\left|\nabla \mathcal{F}^{\alpha}(g(t))\right|_{2}^{2} d t$$
which goes to zero when $i$ goes to infinity. This shows that $\left|\nabla \mathcal{F}^{\alpha}\left(g_{\infty}(0)\right)\right|_{2}=0$, therefore $g_{\infty}$ is a critical point for $\mathcal{F}^{\alpha}$.

Taking the trace of $\nabla \mathcal{F}^{\alpha}\left(g_{\infty}(0)\right)=0$, we see that the scalar curvature of $g_{\infty}$ is harmonic, and since it has bounded $L^{2}$ norm, Theorem 3 of [Yau76] shows that it has to be constant. And since $\left(M, g_{\infty}\right)$ has infinite volume (by Lemma 8.1), the limit manifold is scalar-flat. Then $\nabla \mathcal{F}^{\alpha}\left(g_{\infty}(0)\right)=$ $\nabla \mathcal{F}_{W}\left(g_{\infty}(0)\right)$, so $g_{\infty}$ is also Bach-flat. \(\square\)

Proof of Theorem 1.13 We will need the following lemma:
Lemma 8.2. If $\left(M_{i}, g_{i}, x_{i}\right)$ converges to $\left(M_{\infty}, g_{\infty}, x_{\infty}\right)$ in the pointed $C^{\infty}$ topology, then
$$Y_{g_{\infty}} \geq \varlimsup_{i \rightarrow \infty} Y_{g_{i}} .$$
Proof. There exists diffeomorphisms $\phi_{i}: U_{i} \subset M_{\infty} \rightarrow V_{i} \subset M_{i}$, with $\left\{U_{i}\right\}$ an exhaustion, such that $\phi_{i}^{*} g_{i}$ converges to $g_{\infty}$.

Let $u$ be in $C_{c}^{\infty}\left(M_{\infty}\right)$ with $\int_{M}|u|^{\frac{2 n}{n-2}} d v_{g_{\infty}}=1$. Since it has compact support, $\operatorname{supp}(u) \subset U_{i}$ for $i$ big enough. Let define $u_{i}=u \circ \phi_{i}^{-1} \in H_{1}^{2}(M)$ (extended by 0 outside $V_{i}$ ).

Then,
$$\begin{aligned}
& \int_{M_{\infty}}|\nabla u|_{\phi^{*} g_{i}}^{2}+\frac{n-2}{4(n-1)} R_{\phi^{*} g_{i}} u^{2} d v_{\phi^{*} g_{i}} \\
= & \int_{M}\left|\nabla u_{i}\right|_{g_{i}}^{2}+\frac{n-2}{4(n-1)} R_{g_{i}} u_{i}^{2} d v_{g_{i}} \\
\geq & Y_{g_{i}}\left(\int_{M}\left|u_{i}\right|^{\frac{2 n}{n-2}} d v_{g_{i}}\right)^{\frac{n-2}{n}} \\
= & Y_{g_{i}}\left(\int_{M}|u|^{\frac{2 n}{n-2}} d v_{\phi^{*} g_{i}}\right)^{\frac{n-2}{n}},
\end{aligned}$$
therefore
$$\int_{M_{\infty}}|\nabla u|_{g_{\infty}}^{2}+\frac{n-2}{4(n-1)} R_{g_{\infty}} u^{2} d v_{g_{\infty}} \geq \varlimsup_{i \rightarrow \infty} Y_{g_{i}},$$
and since $C_{c}^{\infty}\left(M_{\infty}\right)$ is dense in $H_{1}^{2}\left(M_{\infty}, g_{\infty}\right)$, it follows that
$$Y_{g_{\infty}} \geq \varlimsup_{i \rightarrow \infty} Y_{g_{i}} .$$ \(\square\)

Proof of the Theorem. We want to use Theorem 1.11 to show that no singularity occurs. Suppose that $\varlimsup_{t \rightarrow T}\left|R m_{g_{t}}\right|_{\infty}=\infty$. We apply Theorem 1.12 to the limit manifold to obtain a contradiction.

Since $\mathcal{F}^{\alpha}(g)$ is decreasing along the flow, all the manifolds $\left(M, g_{t}\right)$ satisfy the bound
$$\mathcal{F}^{\alpha}\left(g_{t}\right) \leq \mathcal{F}^{\alpha}\left(g_{0}\right) \leq 2 \alpha\left(\pi^{2} \chi(M)-\epsilon\right) \quad \text { if } \alpha \leq \frac{4}{13}$$
or
$$\mathcal{F}^{\alpha}\left(g_{t}\right) \leq \mathcal{F}^{\alpha}\left(g_{0}\right) \leq \frac{8}{9} \alpha\left(\pi^{2} \chi(M)-\epsilon\right) \quad \text { if } \alpha \geq \frac{4}{13}$$
for some $\epsilon>0$.
Then, according to Proposition 4.6, all the manifolds $\left(M, g_{t}\right)$ satisfy the inequality:
$$\mathcal{F}_{W}\left(g_{t}\right)+\frac{1}{4} \mathcal{F}_{\text {Ric }}\left(g_{t}\right) \leq \frac{3}{16} Y_{g_{t}}^{2}-\epsilon,$$
and since $\mathcal{F}_{W}, \mathcal{F}_{\text {Ric }}^{\circ}$ and $Y$ are scale invariant, the rescaled manifolds $\left(M, g_{i}\right)$ (see the proof of Theorem 1.9) satisfy the same inequality.

Consequently, according to Lemma 8.2, the limit manifold $\left(M_{\infty}, g_{\infty}\right)$ satisfy:
$$\mathcal{F}_{W}\left(g_{\infty}\right)+\frac{1}{4} \mathcal{F}_{\text {Ric }}\left(g_{\infty}\right) \leq \varliminf_{i \rightarrow \infty}\left(\mathcal{F}_{W}\left(g_{t}\right)+\frac{1}{4} \mathcal{F}_{\text {Ric }}^{\circ}\left(g_{t}\right)\right) \leq \varlimsup_{i \rightarrow \infty}\left(\frac{3}{16} Y_{g_{i}}^{2}-\epsilon\right) \leq \frac{3}{16} Y_{g_{\infty}}^{2}-\epsilon .$$

But $\left(M_{\infty}, g_{\infty}\right)$ is non-flat, Bach-flat, scalar-flat, and satisfies
$$Y_{g_{\infty}} \geq \varlimsup_{i \rightarrow \infty} Y_{g_{i}} \geq Y_{0}>0,$$
and
$$\int_{M_{\infty}} R_{g_{\infty}}^{2} d v_{g_{\infty}} \leq 24\left(8 \pi^{2} \chi(M)+\frac{1}{\alpha} \mathcal{F}^{\alpha}\left(g_{0}\right)\right)$$
according to (5) in the proof of Theorem 1.11, so Theorem 1.12 with $\alpha=0$ asserts that it is flat, a contradiction.

Consequently, the flow exists for all time, and there exists a sequence $\left(t_{i}\right)$ such that $g_{t_{i}}$ converges to a metric $g_{\infty}$ critical for $\mathcal{F}^{\alpha}$, with
$$\mathcal{F}_{W}\left(g_{\infty}\right)+\frac{1}{4} \mathcal{F}_{\mathrm{Ric}}\left(g_{\infty}\right) \leq \frac{3}{16} Y_{g_{\infty}}^{2}-\epsilon,$$
and that satisfies:
$$Y_{g_{\infty}} \geq \varlimsup_{i \rightarrow \infty} Y_{g_{i}} \geq Y_{0}>0 .$$
According to Theorem 1.12, $g_{\infty}$ is a metric of positive constant sectional curvature (since $Y_{g_{\infty}}>0$ ), then $M$ is diffeomorphic to the sphere of the real projective space. \(\square\)

Proof of Corollary 1.15 As the assumptions are conformally invariant, we can suppose that $g_{0}$ is a Yamabe metric. Then
$$Y_{g_{0}}^{2}=\frac{1}{36} \mathcal{F}_{R}\left(g_{0}\right),$$
and it follows that
$$\mathcal{F}_{W}\left(g_{0}\right)+\frac{4}{13} \frac{1}{24} \mathcal{F}_{R}\left(g_{0}\right)<\frac{40}{13} \pi^{2} \chi(M) .$$
According to the Gauss-Bonnet formula, we get:
$$\frac{9}{13} \mathcal{F}_{W}\left(g_{0}\right)+\frac{2}{13} \mathcal{F}_{\text {Ric }}\left(g_{0}\right)<\frac{8}{13} \pi^{2} \chi(M),$$
then we can apply Corollary 1.14 to conclude. \(\square\)

Proof of Theorem 1.16 When $\alpha$ is positive, $\mathcal{G}^{\alpha}$ controls $\mathcal{F}_{R m}$, and as $\mathcal{G}^{\alpha}$ is decreasing along the flow, the $L^{2}$ norm of the curvature is bounded along the flow:
$$\begin{aligned}
\left|\operatorname{Ric}_{g}^{\circ}\right|_{2}^{2} & \leq \mathcal{G}^{\alpha}\left(g_{0}\right) \\
\left|R_{g}\right|_{2}^{2} & \leq \frac{1}{\alpha} \mathcal{G}^{\alpha}\left(g_{0}\right) .
\end{aligned}$$

Then, since $2>\frac{n}{2}$, no singularity can appear according to Theorem 1.9. Moreover,
$$\int_{0}^{\infty}\left|\nabla \mathcal{G}^{\alpha}\left(g_{t}\right)\right|_{2}^{2} d t \leq \mathcal{G}^{\alpha}\left(g_{0}\right)$$
therefore there exists a sequence $\left(t_{i}\right)$ such that $\left|\nabla \mathcal{G}^{\alpha}\left(g_{t_{i}}\right)\right|_{2}$ tends to zero. By Theorem 1.9, a subsequence of $g_{t_{i}}$ converges to a manifold $\left(M_{\infty}, g_{\infty}, x_{\infty}\right), g_{\infty}$ being critical for $\mathcal{G}^{\alpha}$. \(\square\)

\section*{9 Appendix}

\subsection*{9.1 Operators on double-forms}

We use the formalism of double-forms of Labbi (see [Lab08]) and define the following operators (we point out that our definition of $D$ and $\tilde{D}$ differs by a sign from that of [Lab08]):
$$\begin{aligned}
& \delta: \mathcal{T}^{(p+1, q)} M \rightarrow \mathcal{T}^{(p, q)} M \quad b y \quad(\delta T)_{i_{1} \ldots i_{p}}{ }^{j_{1} \ldots j_{q}}=-\nabla^{\alpha} T_{\alpha i_{1} \ldots i_{p}}{ }^{j_{1} \ldots j_{q}}, \\
& \tilde{\delta}: \mathcal{T}^{(p, q+1)} M \rightarrow \mathcal{T}^{(p, q)} M \quad b y \quad(\tilde{\delta} T)_{i_{1} \ldots i_{p}}{ }^{j_{1} \ldots j_{q}}=-\nabla_{\alpha} T_{i_{1} \ldots i_{p}}{ }^{\alpha j_{1} \ldots j_{q}}, \\
& \mathrm{D}: \mathcal{T}^{(p, q)} M \rightarrow \mathcal{T}^{(p+1, q)} M \quad b y \quad(\mathrm{D} T)_{i_{0} \ldots i_{p}}{ }^{j_{1} \ldots j_{q}}=\sum_{k=0}^{p}(-1)^{k} \nabla^{i_{k}} T_{i_{0} \ldots \hat{i}_{k} \ldots i_{p}}{ }^{j_{1} \ldots j_{q}}, \\
& \tilde{\mathrm{D}}: \mathcal{T}^{(p, q)} M \rightarrow \mathcal{T}^{(p, q+1)} M \quad \text { by } \quad(\tilde{\mathrm{D}} T)_{i_{1} \ldots i_{p}}{ }^{j_{0} \ldots j_{q}}=\sum_{k=0}^{p}(-1)^{k} \nabla_{j_{k}} T_{i_{1} \ldots i_{p}}{ }^{j_{0} \ldots \hat{j}_{k} \ldots j_{q}}, \\
& \mathrm{tr}: \mathcal{T}^{(p+1, q+1)} M \rightarrow \mathcal{T}^{(p, q)} M \quad b y \quad(\operatorname{tr} T)_{i_{1} \ldots i_{p}}{ }^{j_{1} \ldots j_{q}}=T_{\alpha i_{1} \ldots i_{p}}{ }^{\alpha j_{1} \ldots j_{q}} .
\end{aligned}$$

Definition 9.1. We say that $T \in \mathcal{T}^{(p, q)} M$ is a double-form if
\begin{itemize}
\item[-] For all $\zeta_{1}, \ldots, \zeta_{q}$ in $T^{*} M, T\left(\cdot, \ldots, \cdot, \zeta_{1}, \ldots, \zeta_{q}\right)$ is a $p$-form.
\item[-] For all $X_{1}, \ldots, X_{p}$ in $T M, T\left(X_{1}, \ldots, X_{p}, \cdot, \ldots, \cdot\right)$ is a $q$-form.
\end{itemize}

We note $\mathcal{D}^{(p, q)}$ the space of $(p, q)$ double-forms.
For example, endomorphisms seen as $(1,1)$ tensors and curvature operators seen as $(2,2)$ tensors are double-forms.

If $S$ and $T$ are in $\mathcal{D}^{(p, q)}$, let define their scalar product by
$$\langle S \mid T\rangle=\frac{1}{p!q!} g^{i_{1} j_{1}} \cdots g^{i_{p} j_{p}} g_{k_{1} l_{1}} \cdots g_{k_{q} l_{q}} S_{i_{1} \ldots i_{p}}^{k_{1} \ldots k_{q}} T_{j_{1} \ldots j_{p}}^{l_{1} \ldots l_{q}} .$$

The operators defined above preserve the double-forms. Moreover, in the space of double-forms, D is the adjoint of $\delta$ and $\tilde{\mathrm{D}}$ is the adjoint of $\tilde{\delta}$ for the scalar product $(S \mid T)_{L^{2}}=\int_{M}\langle S \mid T\rangle d v_{g}$.

We also write
$$\left\langle\nabla^{k} S \mid \nabla^{k} T\right\rangle=g^{i_{1} j_{1}} \cdots g^{i_{k} j_{k}}\left\langle\nabla_{i_{1}} \cdots \nabla_{i_{k}} S \mid \nabla_{j_{1}} \cdots \nabla_{j_{k}} T\right\rangle .$$

If $T$ is in $\mathcal{D}^{(p, q)}$, then
$$\operatorname{tr} \delta=(-1)^{p+q} \delta \operatorname{tr} .$$

On the space of double-forms:
$$\operatorname{tr} \mathrm{D}+\mathrm{D} \operatorname{tr}=-\tilde{\delta} \quad \operatorname{tr} \tilde{\mathrm{D}}+\tilde{\mathrm{D}} \operatorname{tr}=-\delta .$$

The second Bianchi identity leads to:
Proposition 9.2.
$$\begin{array}{lr}
\mathrm{D} R m_{g}=\tilde{\mathrm{D}} R m_{g}=0 & \tilde{\delta} R i c_{g}=-\frac{1}{2} \mathrm{D} R_{g}, \\
\tilde{\delta} R m_{g}=-\mathrm{D} R i c_{g} & \tilde{\delta} W_{g}=-\frac{n-3}{n-2} \mathrm{D} A_{g} .
\end{array}$$

Proposition 9.3.
$$\begin{aligned}
\delta \mathrm{D}\left(R_{g} g\right) & =\Delta R_{g} g+\nabla^{2} R_{g}, \\
\delta \mathrm{D} \text { Ric }_{g} & =\Delta \text { Ric }_{g}+\frac{1}{2} \nabla^{2} R_{g}+\text { Ric } \circ \text { Ric }-\stackrel{\circ}{\text { Rm }}(\text { Ric }) .
\end{aligned}$$
Proof. In coordinates,
$$\left(\mathrm{D}\left(R_{g} g\right)\right)_{i j k}=\nabla_{i} R_{g} g_{j k}-\nabla_{j} R_{g} g_{i k},$$
therefore,
$$\left(\delta \mathrm{D}\left(R_{g} g\right)\right)_{j k}=-\nabla^{\alpha} \nabla_{\alpha} R_{g} g_{j k}+\nabla_{k} \nabla_{j} R_{g} .$$

For the second one:
$$(\mathrm{D} R i c)_{i j k}=\nabla_{i} \text { Ric }_{j k}-\nabla_{j} \text { Ric }_{i k},$$
therefore,
$$\begin{aligned}
(\delta \mathrm{D} R i c)_{j k} & =-\nabla^{\alpha} \nabla_{\alpha} \operatorname{Ric}_{j k}+\nabla_{\alpha} \nabla_{j} \operatorname{Ric}_{\alpha k} \\
& =\Delta \operatorname{Ric}_{j k}-\nabla_{j}(\delta R i c)_{k}+\operatorname{Rm}_{\alpha j}{ }^{\alpha \beta} \operatorname{Ric}_{k \beta}+\operatorname{Rm}_{\alpha j k}{ }^{\beta} \operatorname{Ric}^{\alpha}{ }_{\beta} \\
& =\Delta \operatorname{Ric}_{j k}+\frac{1}{2} \nabla_{j} \nabla_{k} R+\left(\operatorname{Ric} \circ \operatorname{Ric}_{j k}-\operatorname{Rm}^{\circ}(\operatorname{Ric})_{j k} .\right.
\end{aligned}$$ \(\square\)

We recall that:
Proposition 9.4. For all $g$ in $\mathcal{S}_{+}^{2}(M)$ and $h$ in $\mathcal{S}^{2}(M)$,
$$\begin{aligned}
d v_{g}^{\prime}(h) & =\frac{1}{2} \operatorname{tr}(h) d v_{g}, \\
\left(g^{i j}\right)^{\prime}(h) & =-h^{i j}, \\
\Gamma_{g}^{\prime}(h)_{i j}^{k} & =\frac{1}{2} g^{k \alpha}\left(\nabla_{j} h_{\alpha i}+\nabla_{i} h_{\alpha j}-\nabla_{\alpha} h_{i j}\right) .
\end{aligned}$$

The first variation of the curvature tensors are given by:
Proposition 9.5. For all $g$ in $\mathcal{S}_{+}^{2}(M)$ and $h$ in $\mathcal{S}^{2}(M)$,
$$\begin{aligned}
R m_{g}^{\prime}(h)_{i j}{ }^{k l} & =-\frac{1}{2}\left(\tilde{\mathrm{D}} \mathrm{D} h_{i j}{ }^{k l}+R m_{\alpha j}{ }^{k l} h_{i}{ }^{\alpha}+R m_{i \alpha}{ }^{k l} h_{j}{ }^{\alpha}\right), \\
R i c_{g}^{\prime}(h) & =\frac{1}{2}(\delta \mathrm{D} h+\tilde{\mathrm{D}} \operatorname{tr} \mathrm{D} h-h \circ R i c-R m(h)), \\
R_{g}^{\prime}(h) & =\operatorname{tr}(\delta \mathrm{D} h)-\langle R i c \mid h\rangle=\delta \tilde{\delta} h+\Delta \operatorname{tr} h-\langle R i c \mid h\rangle .
\end{aligned}$$
Where $\mathrm{Rm}_{g}$ and $\mathrm{Ric}_{g}$ are seen as double-forms. We can also write:
$$R i c_{g}^{\prime}(h)=\frac{1}{2}\left(\Delta h-\mathrm{D}\left(\delta h+\frac{1}{2} \tilde{\mathrm{D}} \operatorname{tr} h\right)\right)-\tilde{\mathrm{D}}\left(\tilde{\delta} h+\frac{1}{2} \operatorname{Dtr} h\right)+h * R m .$$
Proof. See [Lab08] for $R m_{g}^{\prime}$. Then
$$\begin{aligned}
\operatorname{Ric}_{g}^{\prime}(h) & =\operatorname{tr} R m_{g}^{\prime}(h)=-\frac{1}{2}(\operatorname{tr} \tilde{\mathrm{D}} \mathrm{D} h+h \circ R i c+\stackrel{\circ}{R m}(h)) \\
& =\frac{1}{2}(\delta \mathrm{D} h+\tilde{\mathrm{D}} \operatorname{trD} h-h \circ R i c-R m(h))(\text { Since } \operatorname{tr} \tilde{\mathrm{D}}=-\tilde{\mathrm{D}} \operatorname{tr}-\delta) .
\end{aligned}$$

Then, by writing $\operatorname{tr} \mathrm{D}=-\operatorname{Dtr}-\tilde{\delta}$, we also have
$$\operatorname{Ric}_{g}^{\prime}(h)=\frac{1}{2}(\delta \mathrm{D} h-\tilde{\mathrm{D}} \tilde{\delta} h-\tilde{\mathrm{D}} \operatorname{Dtr} h-h \circ \operatorname{Ric}-\stackrel{\circ}{R m}(h)),$$
and since $\mathrm{D} \tilde{\mathrm{D}}(\operatorname{tr} h)=\tilde{\mathrm{D}} \mathrm{D}(\operatorname{tr} h)$ and $\Delta=\delta \mathrm{D}+\mathrm{D} \delta+R m * \cdot($ see Proposition 9.6 $)$,
$$R i c_{g}^{\prime}(h)=\frac{1}{2}\left(\Delta h-\mathrm{D}\left(\delta h+\frac{1}{2} \tilde{\mathrm{D}} \operatorname{tr} h\right)\right)-\tilde{\mathrm{D}}\left(\tilde{\delta} h+\frac{1}{2} \operatorname{Dtr} h\right)+h * R m .$$
By tracing the former equality, we obtain:
$$\begin{aligned}
R_{g}^{\prime}(h) & =\operatorname{tr} \operatorname{Ric}_{g}^{\prime}(h)=\frac{1}{2}(\operatorname{tr} \delta \mathrm{D} h+\operatorname{tr} \mathrm{D} \operatorname{tr} \mathrm{D} h)-\langle\operatorname{Ric} \mid h\rangle \\
& =\frac{1}{2}(\operatorname{tr} \delta \mathrm{D} h-\delta \operatorname{tr} \mathrm{D} h)-\langle\operatorname{Ric} \mid h\rangle \\
& =\operatorname{tr}(\delta \mathrm{D} h)-\langle\operatorname{Ric} \mid h\rangle, \text { since } \operatorname{tr} \delta(\mathrm{D} h)=-\delta \operatorname{tr}(\mathrm{D} h) .
\end{aligned}$$
And we also have
$$\begin{aligned}
R_{g}^{\prime}(h) & =-\delta \operatorname{trD} h-\langle\operatorname{Ric} \mid h\rangle \\
& =\delta \operatorname{Dtr} h+\delta \tilde{\delta} h-\langle\operatorname{Ric} \mid h\rangle(\text { because } \operatorname{trD}=-\operatorname{Dtr}-\tilde{\delta}) \\
& =\Delta \operatorname{tr} h+\delta \tilde{\delta} h-\langle\operatorname{Ric} \mid h\rangle .
\end{aligned}$$ \(\square\)

\subsection*{9.2 Derivative commuting}

Proposition 9.6. On the space of double-forms, the following identities hold:
$$\begin{array}{rlrl}
\mathrm{D} \tilde{\mathrm{D}} & =\tilde{\mathrm{D}} \mathrm{D}+R m * \cdot, & \delta \tilde{\delta} & =\tilde{\delta} \delta+R m * \cdot, \\
\tilde{\mathrm{D}} \delta & =\delta \tilde{\mathrm{D}}+R m * \cdot, & \mathrm{D} \tilde{\delta} & =\tilde{\delta} \mathrm{D}+R m * \cdot, \\
\mathrm{DD} & =R m * \cdot, & \tilde{\mathrm{D}} \tilde{\mathrm{D}} & =R m * \cdot, \\
\delta \delta & =R m * \cdot, & \tilde{\delta} \tilde{\delta} & =R m * \cdot, \\
\Delta & =\delta \mathrm{D}+\mathrm{D} \delta+R m * \cdot, & \Delta & =\tilde{\delta} \tilde{\mathrm{D}}+\tilde{\mathrm{D}} \tilde{\delta}+R m * \cdot, \\
& \operatorname{tr} \delta \mathrm{D} \delta \mathrm{D}=\Delta^{2} \operatorname{tr}-\Delta \operatorname{tr} \mathrm{D} \delta+\mathcal{P}^{2}\left(R m_{g}, \cdot\right) .
\end{array}$$
Proof. See [Lab08] for the first ones. For the last one:
$$\begin{aligned}
\operatorname{tr} \delta \mathrm{D} \delta \mathrm{D} & =\operatorname{tr} \Delta \delta \mathrm{D}+\mathcal{P}^{2}\left(R m_{g}, \cdot\right) \text { by (10) and (9) } \\
& =\operatorname{tr} \Delta^{2}-\operatorname{tr} \Delta \mathrm{D} \delta+\mathcal{P}^{2}\left(R m_{g}, \cdot\right) \text { by (10) } \\
& =\Delta^{2} \operatorname{tr}-\Delta \operatorname{tr} \mathrm{D} \delta+\mathcal{P}^{2}\left(R m_{g}, \cdot\right) .
\end{aligned}$$ \(\square\)

Proposition 9.7. For all positive integers $k$ and all tensors $T$,
$$\begin{aligned}
\left(\nabla^{k} T\right)_{g}^{\prime}(h) & =\nabla^{k} T_{g}^{\prime}(h)+\mathcal{P}^{k}(h, T), \\
\delta \Delta^{k} T & =\Delta^{k} \delta T+\mathcal{P}^{2 k-1}(R m, T), \\
\delta^{k+1} \nabla^{k+1} T & =\Delta^{k+1}+\mathcal{P}^{2 k}(R m, T) .
\end{aligned}$$

Proof. In coordinates, we have:
$$\nabla_{i} T_{i_{1} \ldots i_{p}}^{j_{1} \ldots j_{q}}=\partial_{i} T_{i_{1} \ldots i_{p}}^{j_{1} \ldots j_{q}}-\sum_{l=1}^{p} \Gamma_{i i_{l}}^{\alpha} T_{i_{1} \ldots \alpha_{\ldots} i_{p}}^{j_{1} \ldots j_{q}}+\sum_{l=1}^{q} \Gamma_{i \alpha}^{j_{l}} T_{i_{1} \ldots i_{p}}^{j_{1} \ldots \alpha_{1} \ldots j_{q}},$$
therefore,
$$\begin{aligned}
\nabla T_{g}^{\prime}(h)_{i i_{1} \ldots i_{p}}^{j_{1} \ldots j_{q}} & =\nabla_{i} T_{g}^{\prime}(h)_{i_{1} \ldots i_{p}}^{j_{1} \ldots j_{q}}-\sum_{l=1}^{p} \Gamma_{g}^{\prime}(h)_{i i_{l}}^{\alpha} T_{i_{1} \ldots \alpha_{\ldots} \ldots i_{p}}^{j_{1} \ldots j_{q}}+\sum_{l=1}^{q} \Gamma_{g}^{\prime}(h)_{i \alpha}^{j_{l}} T_{i_{1} \ldots i_{p}}^{j_{1} \ldots \alpha \ldots j_{q}} \\
& =\nabla_{i} T_{g}^{\prime}(h)_{i_{1} \ldots i_{p}}^{j_{1} \ldots j_{q}}+\nabla h * T,
\end{aligned}$$
then by induction, if $\left(\nabla^{k} T\right)_{g}^{\prime}(h)=\nabla^{k} T_{g}^{\prime}(h)+\mathcal{P}^{k}(h, T)$,
$$\begin{aligned}
\left(\nabla^{k+1} T\right)_{g}^{\prime}(h) & =\nabla\left(\nabla^{k} T\right)_{g}^{\prime}(h)+\nabla h * \nabla^{k} T \\
& =\nabla^{k+1} T_{g}^{\prime}(h)+\nabla \mathcal{P}^{k}(h, T)+\nabla h * \nabla^{k} T \\
& =\nabla^{k+1} T_{g}^{\prime}(h)+\mathcal{P}^{k+1}(h, T) .
\end{aligned}$$

In coordinates:
$$\begin{aligned}
\delta \Delta T_{i_{1} \ldots i_{p}} & =\nabla^{\alpha} \nabla_{\beta} \nabla^{\beta} T_{\alpha i_{1} \ldots i_{p}} \\
& =\nabla_{\beta} \nabla^{\alpha} \nabla^{\beta} T_{\alpha i_{1} \ldots i_{p}}+R m * \nabla T \\
& =\nabla_{\beta} \nabla^{\beta} \nabla^{\alpha} T_{\alpha i_{1} \ldots i_{p}}+\nabla(R m * T)+R m * \nabla T \\
& =\Delta \delta T_{i_{1} \ldots i_{p}}+\mathcal{P}^{1}(R m, T),
\end{aligned}$$
then by induction, if $\delta \Delta^{k} T=\Delta^{k} \delta T+\mathcal{P}^{2 k-1}(R m, T)$,
$$\begin{aligned}
\delta \Delta^{k+1} T & =\Delta \delta \Delta^{k} T+\mathcal{P}^{1}\left(R m, \Delta^{k} T\right) \\
& =\Delta^{k+1} \delta T+\Delta\left(\mathcal{P}^{2 k-1}(R m, T)\right)+\mathcal{P}^{1}\left(R m, \Delta^{k} T\right) \\
& =\Delta^{k+1} \delta T+\mathcal{P}^{2 k+1}(R m, \Delta T) .
\end{aligned}$$

Finally, by induction, if $\delta^{k} \nabla^{k} T=\Delta^{k}+\mathcal{P}^{2 k-2}(R m, T)$ for all tensors $T$, then
$$\begin{aligned}
\delta^{k+1} \nabla^{k+1} T & =\delta \Delta^{k} \nabla T+\delta \mathcal{P}^{2 k-2}(R m, \nabla T) \\
& =\Delta^{k} \delta \nabla T+\mathcal{P}^{2 k-1}(R m, \nabla T)+\delta \mathcal{P}^{2 k-2}(R m, \nabla T) \text { by (13) } \\
& =\Delta^{k+1} T+\mathcal{P}^{2 k}(R m, T) .
\end{aligned}$$ \(\square\)

Proposition 9.8.
$$\begin{aligned}
R m_{g}^{\prime}\left(\delta \tilde{\delta} R m_{g}\right) & =-\frac{1}{2} \Delta^{2} R m_{g}+\mathcal{P}_{2}^{2}\left(R m_{g}\right), \\
R_{g}^{\prime}\left(\delta \tilde{\delta} R m_{g}\right) & =-\frac{1}{2} \Delta^{2} R_{g}+\mathcal{P}_{2}^{2}\left(R m_{g}\right), \\
R_{g}^{\prime}\left(\delta \mathrm{D}\left(R_{g} g\right)\right) & =(n-1) \Delta^{2} R_{g}+\mathcal{P}_{2}^{2}\left(R m_{g}\right), \\
\operatorname{tr} \tilde{\delta} \delta \Delta^{k} R m_{g} & =-\frac{1}{2} \Delta^{k} R_{g}+\mathcal{P}_{2}^{2 k}\left(R m_{g}\right) .
\end{aligned}$$

Proof. Since $R m_{g}^{\prime}=-\frac{1}{2} \mathrm{D} \tilde{\mathrm{D}}+R m_{g} * \cdot($ Proposition 9.5$)$,
$$\begin{aligned}
R m_{g}^{\prime}\left(\delta \tilde{\delta} R m_{g}\right) & =-\frac{1}{2} \mathrm{D} \tilde{\mathrm{D}} \delta \tilde{\delta} R m_{g}+\mathcal{P}_{2}^{2}\left(R m_{g}\right) \\
& =-\frac{1}{2} \mathrm{D} \delta \tilde{\mathrm{D}} \tilde{\delta} R m_{g}+\mathcal{P}_{2}^{2}\left(R m_{g}\right) \text { by (7) in Proposition 9.6 } \\
& =-\frac{1}{2} \Delta \tilde{\mathrm{D}} \tilde{\delta} R m_{g}+\frac{1}{2} \delta \mathrm{D} \tilde{\mathrm{D}} \tilde{\delta} R m_{g}+\mathcal{P}_{2}^{2}\left(R m_{g}\right) \text { by (10) in Proposition 9.6 } \\
& =-\frac{1}{2} \Delta^{2} R m_{g}+\frac{1}{2} \delta \tilde{\mathrm{D}} \mathrm{D} \tilde{\delta} R m_{g}+\mathcal{P}_{2}^{2}\left(R m_{g}\right) \text { by (10) as } \tilde{\mathrm{D}} R m_{g}=0, \text { and by (6) in Proposition } 9.6 \\
& =-\frac{1}{2} \Delta^{2} R m_{g}+\mathcal{P}_{2}^{2}\left(R m_{g}\right) \text { by (7) in Proposition 9.6, as } \mathrm{D} R m=0 .
\end{aligned}$$
Using $R_{g}^{\prime}=\operatorname{tr} \delta \mathrm{D}+R m * \cdot($ Proposition 9.5 $)$,
$$\begin{aligned}
R_{g}^{\prime}\left(\delta \tilde{\delta} R m_{g}\right) & =\operatorname{tr} \delta \mathrm{D} \delta \tilde{\delta} R m_{g}+\mathcal{P}_{2}^{2}\left(R m_{g}\right) \\
& =-\operatorname{tr} \delta \mathrm{D} \delta \mathrm{D} R i c_{g}+\mathcal{P}_{2}^{2}\left(R m_{g}\right) \text { by Proposition } 9.2 \\
& =-\Delta^{2} \operatorname{tr} R i c_{g}+\Delta \operatorname{tr} \mathrm{D} \delta R i c_{g}+\mathcal{P}_{2}^{2}\left(R m_{g}\right) \text { by (11) in Proposition } 9.6 \\
& =-\Delta^{2} R_{g}+\frac{1}{2} \Delta \operatorname{trD} \mathrm{D} R_{g}+\mathcal{P}_{2}^{2}\left(R m_{g}\right) \text { by Proposition } 9.2 \\
& =-\frac{1}{2} \Delta^{2} R_{g}+\mathcal{P}_{2}^{2}\left(R m_{g}\right),
\end{aligned}$$
and
$$\begin{aligned}
R_{g}^{\prime}\left(\delta \mathrm{D}\left(R_{g} g\right)\right) & =\operatorname{tr} \delta \mathrm{D} \delta \mathrm{D}\left(R_{g} g\right)+\mathcal{P}_{2}^{2}\left(R m_{g}\right) \\
& =n \Delta^{2} R_{g}-\Delta \operatorname{tr} \mathrm{D} \delta\left(R_{g} g\right)+\mathcal{P}_{2}^{2}\left(R m_{g}\right) \text { by (11) in Proposition } 9.6 \\
& =n \Delta^{2} R_{g}+\Delta \operatorname{trD} \tilde{\mathrm{D}} R_{g}+\mathcal{P}_{2}^{2}\left(R m_{g}\right) \\
& =(n-1) \Delta^{2} R_{g}+\mathcal{P}_{2}^{2}\left(R m_{g}\right) .
\end{aligned}$$
Finally,
$$\begin{aligned}
\operatorname{tr} \tilde{\delta} \delta \Delta^{k} R m_{g} & =\operatorname{tr} \Delta^{k} \tilde{\delta} \delta R m_{g}+\mathcal{P}_{2}^{2 k}\left(R m_{g}\right) \text { by (13) in Proposition } 9.7 \\
& =\Delta^{k} \tilde{\delta} \delta R i c_{g}+\mathcal{P}_{2}^{2 k}\left(R m_{g}\right) \\
& =-\frac{1}{2} \Delta^{k+1} R_{g}+\mathcal{P}_{2}^{2 k}\left(R m_{g}\right) \text { by Proposition 9.2. }
\end{aligned}$$ \(\square\)

\subsection*{9.3 Interpolation inequalities}

Let define the $L^{p}$ norm of a tensor $T$ by
$$|T|_{p}=\left(\int_{M}|T|^{p} d v_{g}\right)^{\frac{1}{p}}$$

Proposition 9.9. Let $m$ be a positive integer and let $\alpha, \beta$ be in $[0,1]$, with $(\alpha, \beta) \neq(0,0)$. There exists a constant $C(n, m, \alpha, \beta)$ such that for all tensors $T$ and for all $0 \leq k \leq m$,
$$\left|\nabla^{k} T\right|_{\frac{1}{\gamma_{k}}} \leq C|T|_{\frac{1}{\alpha}}^{1-\frac{k}{m}}\left|\nabla^{m} T\right|_{\frac{1}{\beta}}^{\frac{k}{m}},$$
where $\gamma_{k}=\left(1-\frac{k}{m}\right) \alpha+\frac{k}{m} \beta$

We use the two following lemmas of Hamilton:
Lemma 9.10 ([Ham82] Theorem 12.1). Let $\alpha, \beta$ be in $[0,1]$, with $(\alpha, \beta) \neq(0,0)$, and let $\gamma=\frac{1}{2} \alpha+\frac{1}{2} \beta$. There exists $C(n, \gamma)>0$ such that for all tensors $T$,
$$|\nabla T|_{\frac{1}{\gamma}} \leq C|T|_{\frac{1}{\alpha}}\left|\nabla^{2} T\right|_{\frac{1}{\beta}} .$$

Lemma 9.11 ([Ham82] Corollary 12.5). Let $m$ be a positive integer.
If $f:\{0,1, \ldots, m\} \rightarrow \mathbb{R}$ satisfies
$$\forall 0<k<m \quad f(k) \leq C f(k-1)^{1 / 2} f(k+1)^{1 / 2},$$
where $C$ is a constant, then
$$\forall 0 \leq k \leq m \quad f(k) \leq C^{k(m-k)} f(0)^{1-\frac{k}{m}} f(m)^{\frac{k}{m}} .$$
Proof of the Proposition. Let define
$$f(k)=\left|\nabla^{k} T\right|_{\frac{1}{\gamma_{k}}} .$$

As $\gamma_{k}=\frac{1}{2} \gamma_{k-1}+\frac{1}{2} \gamma_{k+1}$, Lemma 9.10 show that there exists $C(n, m, \alpha, \beta)$ such that
$$f(k) \leq C f(k-1)^{1 / 2} f(k+1)^{1 / 2},$$
then Lemma 9.11 proves the proposition. \(\square\)

Proposition 9.12. Let $j \geq 2$ and $k \geq 1$ be two integers.
Let $F: \mathcal{T}^{(p, q)} M \rightarrow \mathbb{R}$ be a map such that for all tensors $T$,
$$F(T)=\mathcal{P}_{j}^{k}(T) .$$
For all integers $m \geq\left[\frac{k+1}{2}\right]$ and all real numbers $\alpha, \beta$ in [0,1] such that
$$\left(j-\frac{k}{m}\right) \alpha+\frac{k}{m} \beta=1,$$
there exists a constant $C(j, n, m, \alpha, \beta, F)$ such that for all tensors $T$,
$$\left|\int_{M} F(T) d v_{g}\right| \leq C|T|_{\frac{1}{\alpha}}^{j-\frac{k}{m}}\left|\nabla^{m} T\right|_{\frac{1}{\beta}}^{\frac{k}{m}} .$$

We will need the following lemma:
Lemma 9.13. For all tensors of the form $S * T$, there exists a constant $C$ depending only on the dimension and the coefficients in the expression such that
$$|S * T| \leq C|S||T| .$$
Proof. By Cauchy-Schwarz inequality, the norm of a tensor with contracted indices is not more than the norm of the tensor multiplied by a power of the dimension:
$$\left(g^{\alpha \beta} T_{\alpha \beta}\right)^{2} \leq n T_{\alpha \beta} T^{\alpha \beta} .$$

Then,
$$|S * T| \leq C(n)\left|S \otimes T \otimes g^{\otimes j} \otimes\left(g^{-1}\right)^{\otimes k}\right| \leq C(n) n^{\frac{j+k}{2}}|S||T| .$$ \(\square\)

Proof of the Proposition. Let consider one term in $F(T)$. We can write it as a contraction of
$$\nabla^{k_{1}} T \otimes \mathcal{P}_{j-1}^{l_{1}}(T),$$
with $k_{1}+l_{1}=k$. Since $F(T)$ is real, all indices are contracted.
Moreover we can suppose that $k_{1} \leq m$ and $k_{1} \leq m$. Indeed, with an integration by part, let show that we can write
$$\int_{M} \operatorname{contr} o f\left(\nabla^{k_{1}} T \otimes \mathcal{P}_{j-1}^{l_{1}}(T)\right) d v_{g}=\int_{M} \operatorname{contr} o f\left(\nabla^{k_{1}-1} T \otimes \mathcal{P}_{j-1}^{l_{1}+1}(T)\right) d v_{g}$$

Since all indices are contracted, the first index of $\nabla^{k_{1}} T$ is either contracted with an other one of $\nabla^{k_{1}} T$, or with one of $\mathcal{P}_{j-1}^{l_{1}}(T)$.

In the first case, we can write:
$$\int_{M} \operatorname{contr} o f\left(\nabla^{k_{1}} T \otimes \mathcal{P}_{j-1}^{l_{1}}(T)\right) d v_{g}=\int_{M} \operatorname{contr}^{o} o f\left(\nabla^{k_{1}-1} T \otimes \nabla \mathcal{P}_{j-1}^{l_{1}}(T)\right) d v_{g},$$
and in the second case, we can write:
$$\int_{M} \operatorname{contr} o f\left(\nabla^{k_{1}} T \otimes \mathcal{P}_{j-1}^{l_{1}}(T)\right) d v_{g}=\int_{M} \operatorname{contr}^{o} o f\left(\nabla^{k_{1}-1} T \otimes \delta \mathcal{P}_{j-1}^{l_{1}}(T)\right) d v_{g} .$$
So we can lower or increase $k_{1}$ until $k_{1}=l_{1}$ or $k_{1}=l_{1}+1$. Then $\left[\frac{k+1}{2}\right]=k_{1}$, thus $k_{1} \leq m$ and $l_{1} \leq k_{1} \leq m$.

Then, by Lemma 9.13 and the Hölder inequality,
$$\begin{aligned}
\left|\int_{M} \nabla^{k_{1}} T * \cdots * \nabla^{k_{j}} T d v_{g}\right| & \leq C^{\prime} \int_{M}\left|\nabla^{k_{1}} T\right| \cdots\left|\nabla^{k_{j}} T\right| d v_{g} \\
& \leq C^{\prime}\left|\nabla^{k_{1}} T\right|_{\frac{1}{\gamma_{k_{1}}}} \cdots\left|\nabla^{k_{j}} T\right|_{\frac{1}{\gamma_{k_{j}}}},
\end{aligned}$$
where $\gamma_{k_{i}}=\left(1-\frac{k_{i}}{m}\right) \alpha+\frac{k_{i}}{m} \beta$, since $\sum_{i=1}^{j} \gamma_{k_{i}}=\left(j-\frac{k}{m}\right) \alpha+\frac{k}{m} \beta=1$ and now, by Proposition 9.9, we get:
$$\left|\int_{M} \nabla^{k_{1}} T * \cdots * \nabla^{k_{j}} T d v_{g}\right| \leq C|T|_{\frac{1}{\alpha}}^{j-\frac{k}{m}}\left|\nabla^{m} T\right|_{\frac{1}{\beta}}^{\frac{k}{m}} .$$

Finally, $F(T)$ being a linear combination of such terms, the proposition is proved. \(\square\)

Corollary 9.14. There exists $C(n, k)$ such that for all tensors $T$
$$\begin{aligned}
\left|\int_{M} \mathcal{P}_{3}^{2 k+2}(T) d v_{g}\right| & \leq C|T|_{k+4}^{\frac{k+4}{k+2}}\left|\nabla^{k+2} T\right|_{2}^{\frac{2 k+2}{k+2}}, \\
\left|\int_{M} \mathcal{P}_{4}^{2 k}(T) d v_{g}\right| & \leq C|T|_{k+4}^{\frac{2 k+8}{k+2}}\left|\nabla^{k+2} T\right|_{2}^{\frac{2 k}{k+2}} .
\end{aligned}$$
Proof. It is an direct application of Proposition 9.12 with $\alpha=\frac{1}{2}, \beta=\frac{1}{k+4}, m=k+2, k^{\prime}=2 k+2$, $j=3$ and $k^{\prime}=2 k, j=4$. \(\square\)

Proposition 9.15. Let $F: \mathcal{T}^{(p, q)} M \rightarrow \mathbb{R}$ be a map such that
$$F(T)=\mathcal{P}_{3}^{2 k+2}(T)+\mathcal{P}_{4}^{2 k}(T) .$$
There exists $C(n, k)$ such that for all tensors $T$,
$$\left|\int_{M} F(T) d v_{g}\right| \leq \frac{1}{2}\left|\nabla^{k+2} T\right|_{2}^{2}+C|T|_{\infty}^{k+2} \mathcal{F}_{T} .$$

Proof. By Corollary 9.14,
$$\begin{aligned}
\left|\int_{M} \mathcal{P}_{3}^{2 k+2}(T) d v_{g}\right| & \leq C|T|_{k+4}^{\frac{k+4}{k+2}}\left|\nabla^{k+2} T\right|_{2}^{\frac{2 k+2}{k+2}} \\
& \leq \frac{1}{4}\left|\nabla^{k+2} T\right|_{2}^{2}+\frac{1}{k+2}\left(\frac{4(k+1)}{k+2}\right)^{k+1} C^{k+2}|T|_{k+4}^{k+4},
\end{aligned}$$
and
$$\begin{aligned}
\left|\int_{M} \mathcal{P}_{4}^{2 k}(T) d v_{g}\right| & \leq C|T|_{k+4}^{\frac{2 k+8}{k+2}}\left|\nabla^{k+2} T\right|_{2}^{\frac{2 k}{k+2}} \\
& \leq \frac{1}{4}\left|\nabla^{k+2} T\right|_{2}^{2}+\frac{2}{k+2}\left(\frac{4 k}{k+2}\right)^{\frac{k}{2}} C^{\frac{k+2}{2}}|T|_{k+4}^{k+4} .
\end{aligned}$$

It follows by adding the two inequalities that there exists $C(n, k)$ such that
$$\begin{aligned}
\left|\int_{M} F(T) d v_{g}\right| & \leq \frac{1}{2}\left|\nabla^{k+2} T\right|_{2}^{2}+C|T|_{k+4}^{k+4} \\
& \leq \frac{1}{2}\left|\nabla^{k+2} T\right|_{2}^{2}+C|T|_{\infty}^{k+2}|T|_{2}^{2} .
\end{aligned}$$ \(\square\)

\subsection*{9.4 Multiplicative Sobolev inequalities}

Proposition 9.16. Let $(M, g)$ be a complete Riemannian $n$-manifold, $n \geq 3$. Let $q \geq 2$. There exists $C$ such that for all $u \in H_{1}^{q}(M)$,
$$|u|_{p} \leq C|u|_{m}^{1-\alpha}\left(A|\nabla u|_{q}+\mathcal{B}_{A}(g)|u|_{q}\right)^{\alpha} .$$
With $2 \leq m \leq p$ and
$$\begin{array}{ll}
\text { if } q<n & p \leq \frac{n q}{n-q} \quad \text { and } \quad C=C(n, q), \\
\text { if } q=n & p<\infty \quad \text { and } \quad C=C(m, p), \\
\text { if } q>n & p \leq \infty \quad \text { and } \quad C=C(n, m, q)
\end{array}$$
and
$$\alpha=\frac{\frac{1}{m}-\frac{1}{p}}{\frac{1}{m}-\frac{1}{q}+\frac{1}{n}} .$$

We will need the following lemma:
Lemma 9.17. Let $(M, g)$ be a complete Riemannian $n$-manifold, $n \geq 3$. For all $\tau>0$ and $q>2$,
$$|u|_{(1+\tau) \frac{2 n}{n-2}} \leq(1+\tau)^{\frac{1}{1+\tau}}|u|_{\frac{2 q \tau}{q-2}}^{\frac{\tau}{1+\tau}}\left(A|\nabla u|_{q}+\mathcal{B}_{A}(g)|u|_{q}\right)^{\frac{1}{1+\tau}} .$$

Proof. Let consider the function $u^{1+\tau}$.
We have $\nabla u^{1+\tau}=(1+\tau) u^{\tau} \nabla u$, therefore $\left|\nabla u^{1+\tau}\right|_{2} \leq(1+\tau)\left|u^{\tau}\right|_{\frac{2 q}{q-2}}|\nabla u|_{q}$. It follows that
$$\begin{aligned}
\left|u^{1+\tau}\right|_{\frac{2 n}{n-2}} & \leq A(1+\tau)\left|u^{\tau}\right|_{\frac{2 q}{q-2}}|\nabla u|_{q}+\mathcal{B}_{A}\left|u^{1+\tau}\right|_{2} \\
& \leq(1+\tau)\left(A|u|_{\frac{2 q \tau}{q-2}}^{\tau}|\nabla u|_{q}+\mathcal{B}_{A}|u|_{2(1+\tau)}^{1+\tau}\right) \\
& \leq(1+\tau)|u|_{\frac{2 q \tau}{q-2}}^{\tau}\left(A|\nabla u|_{q}+\mathcal{B}_{A}|u|_{q}\right),
\end{aligned}$$
what gives the result by elevating to the power $\frac{1}{1+\tau}$. \(\square\)

Proof of the Proposition. For all $p \neq n$, let define $p^{*}=\frac{n p}{n-p}$.
If $\mathbf{q}<\mathbf{n}$ : Let choose if $q>2$
$$\tau=q^{*} \frac{q-2}{2 q}=\frac{\frac{1}{2}-\frac{1}{q}}{\frac{1}{q}-\frac{1}{n}} .$$
Then
$$1+\tau=\frac{\frac{1}{2}-\frac{1}{n}}{\frac{1}{q}-\frac{1}{n}}=\frac{q^{*}}{2^{*}}$$
and by Lemma 9.17:
$$|u|_{q^{*}} \leq(1+\tau)^{\frac{1}{1+\tau}}|u|_{q^{*}}^{\frac{\tau}{1+\tau}}\left(A|\nabla u|_{q}+\mathcal{B}_{A}(g)|u|_{q}\right)^{\frac{1}{1+\tau}} .$$
It follows that
$$|u|_{q^{*}} \leq \frac{q^{*}}{2^{*}}\left(A|\nabla u|_{q}+\mathcal{B}_{A}(g)|u|_{q}\right),$$
which is also true when $q=2$. Then, as $\frac{1}{p}=\frac{1-\alpha}{m}+\alpha\left(\frac{1}{q}-\frac{1}{n}\right)$, we have
$$|u|_{p} \leq|u|_{m}^{1-\alpha}|u|_{q^{*}}^{\alpha} \leq \frac{q^{*}}{2^{*}}|u|_{m}^{1-\alpha}\left(A|\nabla u|_{q}+\mathcal{B}_{A}(g)|u|_{q}\right)^{\alpha} .$$
If $\mathbf{q} \geq \mathbf{n}$ : Let define
$$\gamma=2^{*} \frac{q-2}{2 q}=\frac{\frac{1}{2}-\frac{1}{q}}{\frac{1}{2}-\frac{1}{n}} .$$
Let define a sequence $\left(\tau_{k}\right)$ by
$$\tau_{0}=m \frac{q-2}{2 q} \quad \text { and } \quad \tau_{k+1}=\gamma\left(1+\tau_{k}\right) .$$
Then by Lemma 9.17:
$$|u|_{\frac{2 q}{q-2} \tau_{k+1}}^{\tau_{k+1}} \leq\left(1+\tau_{k}\right)^{\gamma}|u|_{\frac{2 q}{q-2} \tau_{k}}^{\gamma \tau_{k}}\left(A|\nabla u|_{q}+\mathcal{B}_{A}(g)|u|_{q}\right)^{\gamma} .$$
It follows by induction that
$$|u|_{\frac{2 q}{q-2} \tau_{k+1}}^{\tau_{k+1}} \leq\left(1+\tau_{k}\right)^{\gamma} \cdots\left(1+\tau_{0}\right)^{\gamma^{k+1}}|u|_{m}^{\gamma^{k+1} \tau_{0}}\left(A|\nabla u|_{q}+\mathcal{B}_{A}(g)|u|_{q}\right)^{\gamma\left(1+\gamma+\cdots \gamma^{k}\right)} \text {. }$$

If $\mathbf{q}=\mathbf{n}$ : Then $\gamma=1, \tau_{k}=\tau_{0}+k$, and it follows that
$$|u|_{\frac{2 q}{q-2} \tau_{k}}^{\tau_{k}} \leq \tau_{k} \tau_{k-1} \cdots \tau_{0}|u|_{m}^{\tau_{0}}\left(A|\nabla u|_{n}+\mathcal{B}_{A}(g)|u|_{n}\right)^{k},$$
and thus
$$|u|_{\frac{2 q}{q-2} \tau_{k}} \leq \tau_{k}^{\frac{k+1}{\tau_{k}}}|u|_{m}^{\frac{\tau_{0}}{\tau_{k}}}\left(A|\nabla u|_{n}+\mathcal{B}_{A}(g)|u|_{n}\right)^{\frac{k}{\tau_{k}}} .$$

Now, choose a positive integer $k$ such that $p \frac{q-2}{2 q}<\tau_{0}+k \leq p$, and let $\theta=\frac{\tau_{k}}{k} \alpha$. Then $p \leq \frac{2 q}{q-2} \tau_{k}$ and
$$\frac{1}{p}=\frac{1-\alpha}{m}=\frac{1-\theta}{m}+\frac{\tau_{0}}{m} \frac{\theta}{\tau_{k}}=\frac{1-\theta}{m}+\frac{\theta}{\frac{2 q}{q-2} \tau_{k}},$$
thus
$$\begin{aligned}
|u|_{p} & \leq|u|_{m}^{1-\frac{\tau_{k}}{k} \alpha}|u|_{\frac{2 q}{q-2} \tau_{k}}^{\frac{\tau_{k}}{k} \alpha} \\
& \leq \tau_{k}^{\frac{k+1}{k} \alpha}|u|_{m}^{1-\alpha}\left(A|\nabla u|_{n}+\mathcal{B}_{A}(g)|u|_{n}\right)^{\alpha} \\
& \leq p^{2 \alpha}|u|_{m}^{1-\alpha}\left(A|\nabla u|_{n}+\mathcal{B}_{A}(g)|u|_{n}\right)^{\alpha} .
\end{aligned}$$
If $\mathbf{q}>\mathbf{n}$ : Then $\gamma>1, \tau_{k}=\gamma^{k}\left(\tau_{0}+\frac{\gamma}{\gamma-1}\right)-\frac{\gamma}{\gamma-1}$ and we can write:
$$|u|_{\frac{2 q}{q-2} \tau_{k+1}} \leq\left(\prod_{j=0}^{k}\left(1+\tau_{j}\right)^{\frac{\gamma^{k-j}}{1+\tau_{k}}}\right)|u|_{m}^{\frac{\gamma^{k+1} \tau_{0}}{\tau_{k+1}}}\left(A|\nabla u|_{q}+\mathcal{B}_{A}(g)|u|_{q}\right)^{\frac{\gamma}{\gamma-1} \frac{\gamma^{k+1}-1}{\tau_{k+1}}},$$
and since $\tau_{k} \sim c \gamma^{k}$, the product is convergent:
$$\ln \left(\prod_{j=0}^{k}\left(1+\tau_{j}\right)^{\frac{\gamma^{k-j}}{1+\tau_{k}}}\right)=\sum_{j=0}^{k} \frac{\gamma^{k-j}}{1+\tau_{k}} \ln \left(1+\tau_{j}\right) \leq \sum_{j=0}^{\infty} \frac{1}{\tau_{0} \gamma^{j}} \ln \left(\gamma^{j}\left(\tau_{0}+\frac{\gamma}{\gamma-1}\right)\right) .$$

By letting $k \rightarrow \infty$, we obtain:
$$|u|_{\infty} \leq C(n, m, q)|u|_{m}^{\frac{\tau_{0}}{\tau_{0}+\frac{\gamma}{\gamma-1}}}\left(A|\nabla u|_{q}+\mathcal{B}_{A}(g)|u|_{q}\right)^{\frac{\frac{\gamma}{\gamma-1}}{\tau_{0}+\frac{\gamma}{\gamma-1}}},$$
where $C(n, m, q)=\prod_{j=0}^{\infty}\left(1+\tau_{j}\right)^{\frac{\gamma^{k-j}}{1+\tau_{k}}}$ and we check that
$$\frac{\frac{\gamma}{\gamma-1}}{\tau_{0}+\frac{\gamma}{\gamma-1}}=\frac{1}{1+m\left(\frac{1}{n}-\frac{1}{q}\right)}=\frac{\frac{1}{m}}{\frac{1}{m}-\frac{1}{q}+\frac{1}{n}} .$$
This gives the result when $p=\infty$
Finally,
$$\begin{aligned}
|u|_{p} & \leq|u|_{m}^{\frac{m}{p}}|u|_{\infty}^{1-\frac{m}{p}} \\
& \leq C(n, m, q)|u|_{m}^{1-\frac{\frac{1}{m}-\frac{1}{p}}{\frac{1}{m}-\frac{1}{q}+\frac{1}{n}}}\left(A|\nabla u|_{q}+\left.\mathcal{B}_{A}(g)|u|_{q}\right|^{\frac{\frac{1}{m}-\frac{1}{p}}{\frac{1}{m}-\frac{1}{q}+\frac{1}{n}}}\right.
\end{aligned} .$$ \(\square\)

Let define the Sobolev $H_{k}^{p}(A)$-norm of a tensor $T$ by:
$$|T|_{H_{k}^{p}(A)}=A^{k}\left|\nabla^{k} T\right|_{p}+\mathcal{B}_{A}^{k}|T|_{p} .$$

Proposition 9.18. Let $(M, g)$ be a compact Riemannian $n$-manifold, $n \geq 3$. Let $q \geq 2$. There exists $C(n, k, m, p, q)$ such that for all tensors $T$
$$|T|_{H_{k}^{p}(A)} \leq C|T|_{H_{k}^{m}(A)}^{1-\alpha}|T|_{H_{k+1}^{q}(A)}^{\alpha},$$
with $2 \leq m \leq p$ and
$$\begin{array}{lll}
q<n & \text { if } & p \leq \frac{n q}{n-q}, \\
q=n & \text { if } & p<\infty, \\
q>n & \text { if } & p \leq \infty
\end{array}$$
and
$$\alpha=\frac{\frac{1}{m}-\frac{1}{p}}{\frac{1}{m}-\frac{1}{q}+\frac{1}{n}} .$$

We begin with two lemmas:
Lemma 9.19. The proposition is true for $k=0$.
Proof. Let $\epsilon$ be a positive number. Let define $u_{\epsilon}=\sqrt{|T|^{2}+\epsilon}$. Proposition 9.16 applies and show that
$$\left|u_{\epsilon}\right|_{p} \leq C\left|u_{\epsilon}\right|_{m}^{1-\alpha}\left(A\left|\nabla u_{\epsilon}\right|_{q}+\mathcal{B}_{A}(g)\left|u_{\epsilon}\right|_{q}\right)^{\alpha} .$$
Then, as $\epsilon \rightarrow 0,\left|u_{\epsilon}\right|_{p} \rightarrow|T|_{p},\left|u_{\epsilon}\right|_{m} \rightarrow|T|_{m}$ and
$$\left|\nabla u_{\epsilon}\right|=\frac{\langle T \mid \nabla T\rangle}{|T|^{2}+\epsilon} \leq|\nabla T| .$$
The inequality is obtained by making $\epsilon \rightarrow 0$. \(\square\)

Lemma 9.20. There exists $C(n, k, p)$ such that for all $0 \leq j \leq k$,
$$A^{j} \mathcal{B}_{A}^{k-j}(g)\left|\nabla^{j} T\right|_{p} \leq C|T|_{H_{k}^{p}(A)} .$$
Proof. By Proposition 9.9,
$$\left|\nabla^{j} T\right|_{p} \leq C(n, k, p)\left|\nabla^{k} T\right|_{p}^{\frac{j}{k}}|T|_{p}^{1-\frac{j}{k}},$$
then
$$\begin{aligned}
A^{j} \mathcal{B}_{A}^{k-j}(g)\left|\nabla^{j} T\right|_{p} & \leq C(n, k, p)\left(A^{k}\left|\nabla^{k} T\right|_{p}\right)^{\frac{j}{k}}\left(\mathcal{B}_{A}^{k}|T|_{p}\right)^{1-\frac{j}{k}} \\
& \leq C(n, k, p)|T|_{H_{k}^{p}} .
\end{aligned}$$ \(\square\)
Proof of the Proposition. Applying Lemma 9.19 to $\nabla^{k} T$, we obtain
$$\begin{aligned}
A^{k}\left|\nabla^{k} T\right|_{p} & \leq C\left(A^{k}\left|\nabla^{k} T\right|_{m}\right)^{1-\alpha}\left(A^{k+1}\left|\nabla^{k+1} T\right|_{q}+A \mathcal{B}_{A}^{k}(g)|\nabla T|_{q}\right)^{\alpha} \\
& \leq C\left(1+C^{\prime}(n, k, p)\right)^{\alpha}|T|_{H_{k}^{m}}^{1-\alpha}|T|_{H_{k+1}^{q}}^{\alpha} \text { by Lemma } 9.20 \\
\mathcal{B}_{A}^{k}|T|_{p} & \leq C\left(\mathcal{B}_{A}^{k}|T|_{m}\right)^{1-\alpha}\left(A \mathcal{B}_{A}^{k}|\nabla T|_{q}+\mathcal{B}_{A}^{k+1}(g)|T|_{q}\right)^{\alpha} \text { by Lemma } 9.19 \\
& \leq C\left(1+C^{\prime}(n, k, p)\right)^{\alpha}|T|_{H_{k}^{m}}^{1-\alpha}|T|_{H_{k+1}^{q}}^{\alpha} \text { by Lemma } 9.20 .
\end{aligned}$$
It follows that
$$|T|_{H_{k}^{p}} \leq 2 C\left(1+C^{\prime}(n, k, p)\right)|T|_{H_{k}^{m}}^{1-\alpha}|T|_{H_{k+1}^{q}}^{\alpha} .$$ \(\square\)

Proposition 9.21. Let $(M, g)$ be a compact Riemannian $n$-manifold, $n \geq 3$. Let $k=\left[\frac{n}{2}\right]+1$. There exists $C(n)$ such that for all tensors $T$
$$|T|_{\infty} \leq C|T|_{2}^{\frac{1}{n+1}}|T|_{H_{1}^{2}(A)}^{\frac{n-2 k+1}{n+1}}|T|_{H_{k}^{2}(A)}^{\frac{2 k-1}{n+1}} .$$

We will need the following lemma:

Lemma 9.22. Let $k$ and $l$ be nonnegative integers such that $k<\frac{n}{2}$. There exists $C(n, k, l)$ such that for all tensors $T$
$$|T|_{H_{l}^{\frac{2 n}{n-2 k}}(A)} \leq C|T|_{H_{k+l}^{2}(A)} .$$
Proof. By Proposition 9.18, as
$$\frac{2 n}{n-2 \frac{2 n}{n-2(k-1)}}=\frac{2 n}{n-2 k},$$
we have
$$|T|_{H_{l}^{\frac{2 n}{n-2 k}}} \leq C(n, k, l)|T|_{H_{1+l}^{\frac{2 n}{n-2(k-1)}}},$$
so the result holds by induction on $k$. \(\square\)

Proof of the Proposition. From Proposition 9.18, it follows that there exists $C_{1}(n)$ such that
$$|T|_{\infty} \leq C_{1}|T|_{2}^{\frac{1}{n+1}}|T|_{H_{1}^{2 n}}^{\frac{n}{n+1}} .$$

If $\mathbf{n}=\mathbf{2 k}-\mathbf{1}$ : Applying Lemma 9.22, we get:
$$|T|_{\infty} \leq C(n)|T|_{2}^{\frac{1}{n+1}}|T|_{H_{k}^{2}}^{\frac{n}{n+1}} .$$

If $\mathbf{n}=\mathbf{2 k}-\mathbf{2}$ : Applying Proposition 9.18, we get:
$$\begin{aligned}
|T|_{\infty} & \leq C_{2}(n)|T|_{2}^{\frac{1}{n+1}}|T|_{H_{1}^{2}}^{\frac{1}{n+1}}|T|_{H_{2}^{n}}^{\frac{n-1}{n+1}} \\
& \leq C(n)|T|_{2}^{\frac{1}{n+1}}|T|_{H_{1}^{2}}^{\frac{1}{n+1}}|T|_{H_{k}^{2}}^{\frac{n-1}{n+1}} \text { by Lemma 9.22. }
\end{aligned}$$ \(\square\)

\section*{References}
\begin{itemize}
\item[] [Ber02] M. Berger, A panoramic view of Riemannian Geometry, Springer, Berlin Heidelberg New York, 2002.
\item[] [Bes87] A. L. Besse, Einstein Manifolds, Springer, Berlin Heidelberg New York, 1987.
\item[] [Bre03] S. Brendle, Extrema of curvature functionals on the space of metrics on 3-manifolds, Annals of Mathematics 158 (2003), 323-343.
\item[] [CCD ${ }^{+}$10] M. Caldarelli, G. Catino, Z. Djadli, A. Magni, and C. Mantegazza, On Perelman's dilaton, Geometriae Dedicata 145 (2010), 127-137.
\item[] [CGY03] S.-Y. A. Chang, M. J. Gursky, and P. C. Yang, A conformally invariant sphere theorem in four dimensions, Publications Mathématiques de L'IHÉS 98 (2003), 105-143.
\item[] [CH08] X. X. Chen and W. Y. He, On the Calabi flow, American Journal of Mathematics 130 (2008), no. 2, 539-570.
\item[] [Cha04] S.-Y. A. Chang, Non-linear elliptic equations in conformal geometry, European Mathematical Society, Zurich, 2004.
\item[] [Der83] A. Derdziński, Self-dual Kähler manifolds and Einstein manifolds of dimension four, Compositio Mathematica 49 (1983), no. 3, 405-433.
\item[] [DeT83] D. DeTurck, Deforming metrics in the direction of their Ricci tensors, Journal of Differential Geometry 18 (1983), 157-162.
\item[] [GL99] M. J. Gursky and C. LeBrun, On Einstein Manifolds of Positive Sectional Curvature, Annals of Global Analysis and Geometry 17 (1999), 315-328.
\item[] [Gur94] M. J. Gursky, Locally conformally flat four- and six-manifolds of positive scalar curvature and positive Euler characteristic, Indiana University Mathematics Journal 43 (1994), no. 3, 747-774.
\end{itemize}
\begin{itemize}
\item[] [Gur00] \_\_\_\_, Four-manifolds with $\delta W^{+}=0$ and Einstein constants of the sphere, Mathematische Annalen 318 (2000), 417-431.
\item[] [GV01] M. J. Gursky and J. A. Viaclovsky, A new variational characterization of three-dimensional space forms, Inventiones Mathematicae 145 (2001), 251-278.
\item[] [Ham82] R. Hamilton, Three-manifolds with positive Ricci curvature, Journal of Differential Geometry 17 (1982), 255-306.
\item[] [Ham95] \_\_\_\_, A compactness property for solutions of the Ricci flow, American Journal of Mathematics 117 (1995), 545-572.
\item[] [Heb96] E. Hebey, Sobolev spaces on Riemannian manifolds, Lecture Notes in Mathematics 1635, Springer, Berlin Heidelberg New York, 1996.
\item[] [Kim10] S. Kim, Rigidity of noncompact complete Bach-flat manifolds, Journal of Geometry and Physics 60 (2010), no. 4, 637-642.
\item[] [Lab08] M.-L. Labbi, Variational properties of the Gauss-Bonnet curvatures, Calculus of Variations and Partial Differential Equations 32 (2008), no. 2, 175-189.
\item[] [LeB04] C. LeBrun, Curvature functionals, optimal metrics, and the differential topology of 4-manifolds, Different Faces of Geometry, Kluwer Academic/Plenum (2004).
\item[] [Man02] C. Mantegazza, Smooth geometric evolution of hypersurfaces, Geometric And Functional Analysis 12 (2002), 138-182.
\item[] [Mar98] C. Margerin, A sharp characterization of the smooth 4-sphere in curvature terms, Communications in Analysis and Geometry 6 (1998), 21-65.
\item[] [MM10] C. Mantegazza and L. Martinazzi, A Note on Quasilinear Parabolic Equations on Manifolds (2010), available at http://arxiv.org/abs/1010.0733.
\item[] [Per02] G. Perelman, The entropy formula for the Ricci flow and its geometric applications (2002), available at http://arxiv.org/abs/math.DG/0211159.
\item[] [Pet98] P. Petersen, Riemannian geometry, Springer, Berlin Heidelberg New York, 1998.
\item[] [Str08] J. D. Streets, The Gradient Flow of $\int_{M}|R m|^{2}$, Journal of Geometric Analysis 18 (2008), 249-271.
\item[] [Str09] \_\_\_\_, The gradient flow of $\int_{M}|R m|^{2}$ with small initial energy (2009), to appear in Journal of Geometric Analysis, available at http://www.math.princeton.edu/~jstreets/papers/StreetsL2gradflow2.pdf.
\item[] [Str10] \_\_\_\_, The gradient flow of the $L^{2}$ curvature energy near the round sphere (2010), available at http: //arxiv.org/abs/1003.1707v1.
\item[] [Via06] J. Viaclovsky, Conformal geometry and fully nonlinear equations, Inspired by S. S. Chern, Nankai Tracts in Mathematics 11 (2006), 435-460.
\item[] [Yau76] S. T. Yau, Some function-theoretic properties of complete Riemannian manifold and their applications to geometry, Indiana University Mathematics Journal 25 (1976), no. 7, 659-670.
\item[] [Zhe03] Zheng Yu, The negative gradient flow for the $L^{2}$-integral of Ricci curvature, Manuscripta Mathematica 111 (2003), no. 2, 163-186.
\end{itemize}
