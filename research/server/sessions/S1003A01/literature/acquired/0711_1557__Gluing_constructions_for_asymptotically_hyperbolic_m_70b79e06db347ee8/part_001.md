---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: [0711.1557] Gluing constructions for asymptotically hyperbolic manifolds with constant scalar curvature]

---
source_file: 0711_1557.pdf
converter: mathpix
format: mmd
---

\title{
GLUING CONSTRUCTIONS FOR ASYMPTOTICALLY HYPERBOLIC MANIFOLDS WITH CONSTANT SCALAR CURVATURE
}

\author{
PIOTR T. CHRUŚCIEL AND ERWANN DELAY
}

\begin{abstract}
We show that asymptotically hyperbolic initial data satisfying smallness conditions in dimensions $n \geq 3$, or fast decay conditions in $n \geq 5$, or a genericity condition in $n \geq 9$, can be deformed, by a deformation which is supported arbitrarily far in the asymptotic region, to ones which are exactly Kottler ("Schwarzschild- adS") in the asymptotic region.
\end{abstract}

Contents
\begin{itemize}
\item[1.] Introduction
\item[2.] Definitions, notations and conventions
\item[3.] A uniform estimate for $P^{*}$
\item[4.] The gluing construction on a moving annulus
\item[5.] The gluing construction on a fixed annulus
\item[6.] $b$-conformal deformations near infinity
\item[] Appendix A. The asymptotics of $P^{*}$
\item[A.] 1. Conformally compact metrics
\item[A.] 2. The $(C, k, \sigma)$-asymptotically hyperbolic case
\item[] Appendix B. Proof of Lemma 3.6
\item[] References
\end{itemize}

\section*{1. Introduction}

One of the key problems in mathematical general relativity is the understanding of the space of solutions of the vacuum constraint equations. In this context an important gluing method has been introduced by Corvino and Schoen [12, 13] for vacuum data with vanishing cosmological constant. The object of this paper is to present related gluing results when the cosmological constant $\Lambda$ is negative. The question we address is the possibility of deforming an asymptotically hyperbolic Riemannian manifold of constant scalar curvature, and hence a time-symmetric vacuum initial data set, to one with a Kottler metric (sometimes known as Schwarzschild - anti de Sitter metric) outside of a compact set. We establish deformation or extension theorems in dimensions $n \geq 3$ under a smallness condition for metrics sufficiently close to (generalized) Kottler metrics, or under smallness and parity

\footnotetext{
Date: April 21, 2022.
}
conditions for metrics close to a standard hyperbolic metric, or assuming a rapid decay condition in dimensions $n \geq 5$.

More precisely, we consider $n$-dimensional manifolds containing asymptotic ends
$$M_{\mathrm{ext}}:=\left(r_{0}, \infty\right) \times N,$$
where $N$ is a compact manifold. We are interested in constant scalar curvature metrics which asymptote, as $r$ goes to infinity, to a background metric $b$ of the form ${ }^{1}$
$$b=\frac{d r^{2}}{r^{2}+k}+r^{2} \widehat{b},$$
where $k \in\{0, \pm 1\}$, and where $\widehat{b}$ is a ( $r$-independent) metric on $N$ satisfying $\operatorname{Ric}(\widehat{b})=k(n-2) \widehat{b}$. A family of examples is provided by the (generalized) Kottler metrics,
$$b_{m}=\frac{d r^{2}}{r^{2}+k-\frac{2 m}{r^{n-2}}}+r^{2} \widehat{b}$$
Note that $b_{0}=b$, with $b$ as in (1.2).
For the purpose of the next theorem define the manifold $M$ to be
$$M=\left(r_{0}, r_{2}\right] \times N,$$
and suppose that $g$ is a constant negative scalar curvature metric on $M$ close to $b$, or to $b_{m}$. There are two natural questions:

First, choose $r_{1}$ satisfying $r_{0}<r_{1}<r_{2}$, can one deform $g$, keeping the scalar curvature fixed, so that the resulting metric coincides with $g$ on $\left(r_{0}, r_{1}\right] \times N$, and with $b_{m}$, for some $m$, near $\left\{r_{2}\right\} \times N$ ? In this case we set $M^{\prime}=\left(r_{0}, r_{1}\right] \times N, M^{\prime \prime}=\left[r_{2}, \infty\right) \times N$, and we refer to this case as the deformation problem.

Next, let $r_{3}>r_{2}$, can one extend $g$ to a new metric of constant scalar curvature on $\left(r_{0}, \infty\right) \times N$ so that the extended metric coincides with $b_{m}$, for some $m$, on $\left[r_{3}, \infty\right) \times N$ ? In this case we set $M^{\prime}=M, M^{\prime \prime}=\left[r_{3}, \infty\right) \times N$, and we refer to this case as the extension problem. It is shown in [8, Section 8.6] how to reduce this problem to the deformation one.

Our aim here is to show that those problems can always be solved when $g$ is sufficiently close to $b$, except perhaps when $(N, \widehat{b})$ is a round sphere and $m=0$, in which case we need to impose a restrictive condition: For $(r, q) \in M$ let $\psi(r, q)=(r, \phi(q))$, where $\phi$ is the antipodal map of the sphere. A metric $g$ on $M$ will be said to be parity-symmetric if $\psi^{*} g=g$. At the end of Section 5 we prove:

Theorem 1.1. Let $n \geq 3, \mathbb{N} \ni \ell>\left\lfloor\frac{n}{2}\right\rfloor+4, \lambda \in(0,1), m \in \mathbb{R}$. If $(N, \widehat{b})$ is a round sphere and $m=0$, we suppose moreover that $g$ is parity-symmetric. There exists $\varepsilon>0$ such that if $\left\|g-b_{m}\right\|_{C^{\ell, \lambda}(M)}<\varepsilon$, then there exists on $M_{\text {ext }}$ a $C^{\ell, \lambda}$ metric of constant negative scalar curvature which coincides with $g$ on $M^{\prime}$, and which is a Kottler metric on $M^{\prime \prime}$. If $g$ is smooth, then so is the solution of the deformation problem.

\footnotetext{
${ }^{1}$ The constant $k$ in (1.2)-(1.3) is of course unrelated to the order of differentiability $k$ used elsewhere, we hope that this will not confuse the reader.
}

We emphasize that $g$ and $b_{m}$ are only required to be close to each other on an "annulus" as above, and in fact $b_{m}$ is not even defined throughout the original manifold.

We can also prove a result without smallness assumptions which, however, excludes dimensions three and four. Moreover the decay rates are undesirably restrictive in dimensions five, six and seven; they are satisfactory, but not as weak as one would wish, in higher dimensions.

Let $g$ be an asymptotically hyperbolic metric as defined in Section 2, and let $p_{(\mu)}^{0}$ be the momentum vector of $g$, obtained by passing to the limit as $r$ goes to infinity of the integral (5.1) below over submanifolds $r=$ const. Let $b_{p_{(\mu)}}$ denote a (generalized, boosted) Kottler metric with momentum vector $p_{(\mu)}$. Suppose that
$$n \geq 5, \quad \alpha>\left\{\begin{array}{cc}
8, & n=5,6,7 \\
\frac{8+n}{2}, & n \geq 8 .
\end{array}\right.$$
(This can be compared with the conditions $\alpha>n / 2, n \geq 3$, needed for $p_{(\mu)}^{0}$ to be well-defined, or $\alpha=n$, which holds for Kottler metrics.) For $\alpha \leq n$ we assume that $g$ has the following asymptotic behaviour
$$|g-b|_{b}+|\stackrel{\circ}{D}(g-b)|_{b}+\ldots+\left|\stackrel{\circ}{D}^{(k+2)}(g-b)\right|_{b}=O\left(\rho^{\alpha}\right),$$
where $\stackrel{\circ}{D}$ is the covariant derivative operator of $b$. For $\alpha>n$, if $(N, \widehat{b})$ is a round sphere, we assume that the momentum vector $p_{(\mu)}^{0}$ of $g$ is timelike, ${ }^{2}$ so that an associated (perhaps boosted) Kottler metric $b_{p_{(\mu)}^{0}}$ exists. Whether or not $(N, \widehat{b})$ is a round sphere, for $\alpha>n$ instead of (1.5) we suppose that
$$\left|g-b_{p_{(\mu)}^{0}}\right|_{b}+\left|\stackrel{\circ}{D}\left(g-b_{p_{(\mu)}^{0}}\right)\right|_{b}+\ldots+\left|\stackrel{\circ}{D}^{(k+2)}\left(g-b_{p_{(\mu)}^{0}}\right)\right|_{b}=O\left(\rho^{\alpha}\right) ;$$
in fact, (1.6) is equivalent to (1.5) if $\alpha \leq n$.
Letting $M_{\delta}$ be as in (2.1), and $A_{\delta, 4 \delta}$ as in (2.2), in Section 4 we prove:
Theorem 1.2. Let $n \geq 5, \mathbb{N} \ni \ell>\left\lfloor\frac{n}{2}\right\rfloor+4, \lambda \in(0,1)$, and let $\alpha>0$ satisfy (1.4). Let $g$ be a $C^{\ell, \lambda}$ asymptotically hyperbolic metric with constant negative scalar curvature satisfying (1.6) with $k=\ell-4$. We furthermore assume that (1.6) holds with $k=\ell-2$ and $\alpha=0$, and that the energymomentum vector is timelike if $(N, \widehat{b})$ is a round sphere. There exists $\delta_{0}>0$ such that for all $0<\delta \leq \delta_{0}$ the metric $g$ can be deformed across an annulus $A_{\delta, 4 \delta}$ to a constant scalar curvature metric, of $C^{\ell, \lambda}$ differentiability class, which coincides with $g$ on $M \backslash M_{4 \delta}$ and with a Kottler metric $b_{p_{(\mu)}}$ on $M_{\delta}$. The solution is smooth if $g$ is.

A key role in our analysis is played by the kernel of the operator $P_{g}^{*}$ given by (2.6) below; it is known that this kernel is trivial for any open subset of $M$ for generic metrics [4]. Deforming first the metric as in Section 6, and applying Theorem 1.2 to the new metric one concludes:

Corollary 1.3. Let $n \geq 9$. Under the remaining hypotheses of Theorem 1.2, suppose instead of (1.4) that $\alpha>n / 2$. If there are no neighbourhoods of the conformal boundary at infinity on which $P_{g}^{*}$ has a kernel, then the conclusions of Theorem 1.2 hold.

\footnotetext{
${ }^{2}$ Both past and future pointing $p_{(\mu)}^{0}$ are allowed.
}

It might be helpful to the reader to recall briefly the Corvino-Schoen method, as adapted to our setting. We work on an end $\left(r_{0},+\infty\right) \times N$, where we have a metric $g$ asymptotic to a background metric $b$. We also have a $d$-parameter family of references metrics $b_{p}$, all asymptotic to $b$, all having the same, constant scalar curvature. The gluing is performed on an annulus $A_{R}=\{R<r<4 R\}$, with $R \gg 1$, in four steps:

Step 1): Do a scaling in order to work on a fixed annulus $A_{1}$,
Step 2): Establish a weighted estimate of the form $\left|P^{*} u\right|_{L^{2}} \geq c|u|_{H^{2}}$, where $P^{*}$ is the adjoint of the linearized scalar curvature operator $P$ and $u$ is orthogonal to the $d$-dimensional kernel $K$ of $P^{*}$. The constant $c$ has to be uniform in the family of metrics under consideration, with controlled dependence upon $R$. In fact, in previous applications $c$ was $R$-independent.

Step 3): By step 2), and up to weighting functions, the operator $L=P P^{*}$ is an isomorphism modulo projections onto $K^{\perp}$. By the inverse function theorem, for $R \gg 1$, the gluing of $g$ with any $b_{p}$ can be done modulo weighted $L^{2}$-projection onto $K^{\perp}$.

Step 4): Estimate the projection onto $K$ and show that you can adjust the parameter $p$ to obtain a solution.

So, the overall strategy is the same as in [8,12,13]. However, in our case essential new difficulties arise: the scaling transformation in the asymptotically flat case leads to a family of uniformly equivalent operators on a fixed annulus, while this is not the case anymore for negative $\Lambda$. To handle this we prove a sharp estimate on the family of operators which arise in our context; unfortunately the estimate degenerates as the gluing annuli recede to infinity, as the sharp constant $c$ in step 2) above goes to zero. This results in the undesirable restrictions described above. A possible approach to improve this state of affairs could be to devise a method which, first, deforms any asymptotically hyperbolic metric to one for which our Theorem 1.2 (or some variation thereof) applies. Alternatively, a completely different method of approaching the problem is needed.

Our work has been largely motivated by [1], to remove the sign condition on the mass aspect function imposed there. Our deformation produces a metric with a constant mass aspect without a priori assuming such a sign in dimensions larger than eight; our result is, however, irrelevant for the main result in [1], which has only been proved so far for $n \leq 7$.

\section*{2. Definitions, notations and conventions}

Let $\bar{M}$ be a smooth, compact $n$-dimensional manifold with boundary $\partial M$. Let $M:=\bar{M} \backslash \partial M$, a non-compact manifold without boundary. In our context the boundary $\partial M$ will play the role of a conformal boundary at infinity of $M$. We will choose a defining function $\rho$ for $\partial M$, that is a non-negative smooth function on $\bar{M}$, vanishing precisely on $\partial M$, with $d \rho$ never vanishing there.

We will work near the infinity of $M$, so it is convenient to define, for small $\varepsilon>0$, the manifold
$$M_{\varepsilon}=\{x \in M, \rho(x)<\varepsilon\} .$$
We also define for small $\varepsilon>\delta>0$, the "annulus"
$$A_{\delta, \varepsilon}:=M_{\varepsilon} \backslash \overline{M_{\delta}} .$$
We continue by defining a class of background metrics of interest. For $k$ equal to -1, 0 or 1, let $\widehat{b}$ be a metric on $\partial M$ satisfying $\operatorname{Ric}(\widehat{b})=k(n-2) \widehat{b}$. For $\rho_{0}$ such that $1-k\left(\frac{\rho}{2}\right)^{2}$ has no zeros on ( $0, \rho_{0}$ ), consider the metric
$$b=\rho^{-2}\left(d \rho^{2}+\frac{\left(4-k \rho^{2}\right)^{2}}{16} \widehat{b}\right)=: \rho^{-2} \bar{b}$$
defined on $\left(0, \rho_{0}\right) \times \partial M$. Then $b$ is Einstein, $\operatorname{Ric}(b)=-(n-1) b$, in particular it has constant scalar curvature $R(b)=-n(n-1)$, and in fact provides initial data for a static solution of the vacuum Einstein equations with a negative cosmological constant. These are of course identical to (1.2) (use $r=\rho^{-1}\left[1-k\left(\frac{\rho}{2}\right)^{2}\right]$ ). The basic example of such a background is the standard hyperbolic metric. In that case $M$ is the unit ball of $\mathbb{R}^{n}$, with
$$b=\omega^{-2} \delta,$$
$\delta$ is the Euclidean metric, $\omega(x)=\frac{1}{2}\left(1-|x|_{\delta}^{2}\right)$.
A metric $g$ will be called asymptotically hyperbolic if $g$ tends to a background metric as in (2.3) when approaching $\partial M$. The precise decay rates will be indicated whenever needed. The terminology is motivated by the fact that the sectional curvatures of $g$ tend to -1 as $\rho$ approaches zero; cf., e.g., [17]. One should, however, keep in mind that $b$ does not necessarily have constant sectional curvature in space-time dimension other than four. Moreover, metrics which asymptote to hyperbolic metrics in cuspidal ends do not necessarily belong to our class.

An important class of asymptotically hyperbolic metrics is given by the (generalized) Kottler metrics [14] (compare [5]) as given by (1.3). In the coordinate system of (2.3) they read
$$\begin{aligned}
b_{m}= & \rho^{-2}\left\{\left[1-2 m \rho^{n}\left(1-k\left(\frac{\rho}{2}\right)^{2}\right)^{2-n}\left(1+k\left(\frac{\rho}{2}\right)^{2}\right)^{-2}\right]^{-1} d \rho^{2}\right. \\
& \left.+\left(1-k\left(\frac{\rho}{2}\right)^{2}\right)^{2} \widehat{b}\right\} \\
= & \rho^{-2}\left[\bar{b}+2 m \rho^{n}\left(1+O\left(\rho^{2}\right)\right) d \rho^{2}\right],
\end{aligned}$$
where, as before, $\widehat{b}$ is a fixed metric on the boundary at infinity $N$ satisfying $\operatorname{Ric}(\widehat{b})=k(n-2) \widehat{b}$. Those metrics satisfy $R\left(b_{m}\right)=-n(n-1)$, and again provide initial data for static Einstein metrics.

If $\widehat{b}$ is not the round metric on a sphere, the only energy-like Hamiltonian invariant of $b_{m}$ is $m$, see e.g. [6] and references therein. Otherwise $b$ is the standard hyperbolic metric, and the energy-momentum vector of $b_{m}$, say $p_{(\mu)}$ (as defined in [10] or [22], see (4.18) with $r \rightarrow+\infty$ )), is proportional to $(m, \overrightarrow{0})$. Under isometries of hyperbolic space, $p_{(\mu)}$ transforms as a Lorentz vector, and a metric with any timelike $p_{(\mu)}$ can be obtained by applying such an isometry to some $b_{m}$.

In this way we generate a family of metrics with any timelike $p_{(\mu)}$, as needed for the Brouwer fixed point argument when compensating for the cokernel below. (On the other hand we are not aware of existence of such metrics with non-timelike non-zero $p_{(\mu)}$, whence the restriction of timelikeness in our results when $(N, \widehat{b})$ is a round sphere.) We denote by $b_{p_{(\mu)}}$ the resulting metrics, and we will refer to them as Kottler metrics, or boosted Kottler metrics when ambiguities are likely to occur.

Recall that the linearized scalar curvature operator $P=P_{g}$ is
$$P_{g} h:=D R(g) h=-\nabla^{k} \nabla_{k}\left(t r_{g} h\right)+\nabla^{k} \nabla^{l} h_{k l}-R^{k l} h_{k l},$$
so that its $L^{2}$ formal adjoint reads
$$P_{g}^{*} f=[D R(g)]^{*} f=-\nabla^{k} \nabla_{k} f g+\nabla \nabla f-f \operatorname{Ric}(g) .$$
(We use the summation convention, indices are lowered with $g_{i j}$ and raised with its inverse $g^{i j}$.) We note that
$$\operatorname{Tr} P_{g}^{*} f=(n-1) \nabla^{*} \nabla f-R f .$$

Let
$$b_{\delta}:=z^{-2}\left(d z^{2}+\delta^{-2} \widehat{b}(\delta z)\right)$$
be a hyperbolic metric scaled up in $\rho$ from $A_{\delta, 4 \delta}$ to
$$A \equiv A_{(1,4)}:=(1,4) \times \partial M .$$
We have $\operatorname{Ric}\left(b_{\delta}\right)=-(n-1) b_{\delta}$, thus
$$P_{b_{\delta}}^{*} u:=\nabla \nabla u+\left((n-1) u-\nabla^{k} \nabla_{k} u\right) b_{\delta},$$
where ∇ is associated with the metric $b_{\delta}$.
It is well known that the kernel of $P^{*}$ has dimension at most $n+1$, see [12] for instance. For the hyperbolic metric $b$ on the unit $n$-dimensional ball $B^{n}(1) \subset \mathbb{R}^{n}$, in the representation (2.4), the kernel of $P_{b}^{*}$ is spanned by the following functions,
which are the restrictions to the hyperboloid $\mathbb{H}^{n}$ of the coordinates functions in Minkowski $\mathbb{R}^{n, 1}$ :
$$\begin{aligned}
V_{(0)} & :=\frac{1+|x|^{2}}{1-|x|^{2}}=\rho^{-1}\left(1+\left(\frac{\rho}{2}\right)^{2}\right) \\
V_{(k)} & :=-\frac{2 x^{k}}{1-|x|^{2}}=-\rho^{-1}\left(1-\left(\frac{\rho}{2}\right)^{2}\right) \frac{x^{k}}{|x|},
\end{aligned}$$
with $\rho=2(1-|x|) /(1+|x|)$. We can also rewrite (2.4) as
$$b=\rho^{-2}\left(d \rho^{2}+\widehat{b}(\rho)\right),$$
with $\widehat{b}(\rho)=\left(1-\left(\frac{\rho}{2}\right)^{2}\right)^{2} \widehat{b}(0)$, where $\widehat{b}(0)$ is the round unit metric on $S^{n}$. Setting $\rho=\delta z$, defining
$$V_{\delta,(\mu)}(z, \theta)=V_{(\mu)}(\delta z, \theta),$$
and letting $\delta$ tend to zero, the functions $\delta V_{\delta,(\mu)}$ tend to
$$u_{(0)}:=z^{-1}, \quad u_{(k)}:=-z^{-1} \frac{x^{k}}{|x|} .$$

For nonspherical boundary metrics $\widehat{b} \equiv \widehat{b}(0)$ we still write $\left\{V_{(\mu)}\right\}$ for any basis of $\operatorname{Ker} P_{b}^{*}$, and then $V_{\delta,(\mu)}$ is defined by (2.13). By hypothesis the scalar curvature of $\widehat{b}$ is constant, so that we can invoke a theorem of Obata [20] (see also [15] Theorem 24) to conclude that the only Riemannian manifold $(\widehat{M}, \widehat{b})$ of dimension $n-1$ with non-constant solutions $v$ to the equation $D D v+\frac{D^{*} D v}{n-1} \widehat{b}=0$ is a round sphere. For metrics of the form (2.3) with $\widehat{b}$ different from a round sphere, this implies (compare appendix A) that $\operatorname{dim} \operatorname{Ker} P^{*}=1$, and $V_{(0)}=V_{(0)}(\rho)$, with the $u_{(\mu)}$ 's proportional to $u_{(0)}=$ $z^{-1}$ (compare (3.19) and (3.20)).

Definition 2.1. Let $k \in \mathbb{N}, C, \sigma \geq 0$. Let $b$ be a of the form (2.3), with $\widehat{b}$ an Einstein metric on $\partial M$ with scalar curvature $(n-1)(n-2) \kappa, \kappa \in\{0, \pm 1\}$, and with $\rho \in\left(0,2 \rho_{0}\right]$. We will say that $g$ is $(C, k, \sigma)$-asymptotically hyperbolic if we have
$$|g-b|_{b}+|\nabla g|_{b}+\ldots+\left|\nabla^{(k)} g\right|_{b} \leq C \rho^{\sigma},$$
where the norm and covariant derivatives are defined by $b$. For $\alpha \in(0,1)$ we will say that $g$ is $(C, k+\alpha, \sigma)$-asymptotically hyperbolic if the derivatives of order $k$ of $g-b$ further satisfy a weighted Hölder condition of order $\alpha$, as in [16].

Let $g$ be a Riemannian metric on $M$, recall that $(M, g)$ is conformally compact if there exists on $\bar{M}$ a smooth defining function $\rho$ for $\partial M$ (that is $\rho \in C^{\infty}(\bar{M}), \rho>0$ on $M, \rho=0$ on $\partial M$ and $d \rho$ nowhere vanishing on $\partial M$; the symbol $\rho$ will be used throughout this work to denote such a function) such that $\bar{g}:=\rho^{2} g$ is a Riemannian metric on $\bar{M}$, we will denote by $\widehat{g}$ the metric induced on $\partial M$. The background metrics $b$ considered above are conformally compact in this sense.

It is well know that, near infinity, for any sufficiently differentiable conformally compact metric $g$ we may choose the defining function $\rho$ to be the $\bar{g}$-distance to the boundary. Thus, if $\varepsilon$ is small enough, $M_{\varepsilon}$ can be identified with $(0, \varepsilon) \times \partial M$ equipped with the metric
$$g=\rho^{-2}\left(d \rho^{2}+\widehat{g}(\rho)\right)=\rho^{-2}\left(d \rho^{2}+\widehat{g}_{A B}(\rho) d \theta^{A} d \theta^{B}\right)$$
where $\{\widehat{g}(\rho)\}_{\rho \in(0, \varepsilon)}$ is a family of smooth, uniformly equivalent, metrics on $\partial M$, with $\widehat{g}(0)=\widehat{g}$. However, the introduction of this system of coordinates might lead to a loss of up to two derivatives of the metric. This can be circumvented for $(C, k, \sigma)$-asymptotically hyperbolic metrics by introducing a coordinate system as in [2, Appendix B] in which $g$ takes the form
$$g=\rho^{-2}\left(\left(1+O\left(\rho^{k+\sigma}\right)\right) d \rho^{2}+\widehat{g}_{A B}(\rho) d \theta^{A} d \theta^{B}+O\left(\rho^{k+\sigma}\right)_{A} d \rho d \theta^{A}\right)$$
with all metric coefficients of original differentiability class.
If $g$ is $(C, k, \sigma)$-asymptotically hyperbolic with $k \geq 2$ and $\sigma>0$, we have (2.18)
$$P_{g}^{*} u:=\nabla \nabla u-\nabla^{k} \nabla_{k} u g-u \operatorname{Ric}(g)=\nabla \nabla u+\left((n-1) u-\nabla^{k} \nabla_{k} u\right) g+O\left(\rho^{\sigma}\right) u,$$
where the covariant derivatives are related to $g$, and the $O\left(\rho^{\sigma}\right)$ term is bounded (in $b$-norm) together with its $b$-derivatives up to order $k-2$, by $\rho^{\sigma}$ times a constant depending on $C$ and $k$.

\section*{3. A uniform estimate for $P^{*}$}

Let $y$ be the function on $A$ defined by:
$$\begin{array}{cccc}
y: & (1,4) \times \partial M & \longrightarrow & \mathbb{R}, \\
(z, \theta) & \mapsto & \frac{4}{3}\left(1-\frac{z}{4}\right)(z-1) .
\end{array}$$
We claim that:
Proposition 3.1. Let $c_{0}, \sigma>0$ and $s \geq 0$. There exist constants $c_{1}=c_{1}\left(n, s, c_{0}, \sigma\right)>0$ and $\delta_{0}=\delta_{0}\left(n, s, c_{0}, \sigma\right)>0$ such that for all $\left(c_{0}, 4, \sigma\right)$ asymptotically hyperbolic metrics $g$, for all $0<\delta \leq \delta_{0}$, and for all $u$ satisfying
$$\forall \mu=0, \ldots, k \quad \int_{A} e^{-s / y} u u_{(\mu)} d \mu_{b_{\delta}}=0$$
where $k=n$ if $b$ is the standard hyperbolic metric, and $k=0$ otherwise, we have
$$\int_{A} e^{-s / y} y^{8}\left|P_{g_{\delta}}^{*} u\right|_{g_{\delta}}^{2} d \mu_{g_{\delta}} \geq c_{1} \delta^{4} \int_{A} e^{-s / y}\left(y^{8}|\nabla \nabla u|_{g_{\delta}}^{2}+y^{4}|\nabla u|_{g_{\delta}}^{2}+u^{2}\right) d \mu_{g_{\delta}}$$
provided that the right-hand-side is finite. Similarly (3.3) holds (with perhaps a different constant $c_{1}$ ) if
$$\forall \mu=0, \ldots, k \quad \int_{A} e^{-s / y} u V_{\delta,(\mu)} d \mu_{g_{\delta}}=0,$$
or if in (3.2) the measure $z^{-n} d z d \mu_{\widehat{b}(0)}$ is used.
Remark 3.2. There is little doubt that the result remains valid for $\left(c_{0}, 2, \sigma\right)$ asymptotically hyperbolic metrics, or for those conformally compact metrics which are $C^{2}$ up-to-boundary after the conformal rescaling, by using coordinates as in (2.17). For simplicity of calculations we assume (2.16), since our main gluing results require $\left(c_{0}, 4, \sigma\right)$ asymptotically hyperbolic metrics anyway.

Remark 3.3. The power of $\delta$ in (3.3) cannot be improved, which can be seen by considering a function of the form $u(z, \theta)=v(\theta) / z$, with a nontrivial $v$ of vanishing integral on $\partial M$, such that $D D v+\frac{D^{*} D v}{n-1} \widehat{b}(0) \neq 0$, where $D$ is the covariant derivative operator of $\widehat{b}(0)$, and such that $v$ is $L^{2}(\partial M, \widehat{b}(0))$ orthogonal to the kernel of $P_{\widehat{b}(0)}^{*}$ (see (3.15) below).

Proof: In some of the calculations of this proof the reader might find it convenient to use the coordinate system of (2.16). Without loss of generality we can assume that $\sigma \leq 1$. Let us define $d \nu_{g_{\delta}}=\delta^{n-1} d \mu_{g_{\delta}}$, and note that the measure $d \mu_{g_{\delta}}$ can be replaced by $d \nu_{g_{\delta}}$ in (3.2)-(3.4); e.g., (3.2) can be replaced by
$$\forall \mu=0, \ldots, k \quad \int_{A} e^{-s / y} u u_{(\mu)} d \nu_{g_{\delta}}=0 .$$
Suppose that (3.3) with $d \mu_{g_{\delta}}$ there replaced by $d \nu_{g_{\delta}}$ does not hold, then there exist sequences $\delta_{n} \rightarrow 0, g^{(n)}$ and $u_{n}$ satisfying (3.2) (respectively (3.4)) such
that the right-hand-side equals one, while the reverse inequality to (3.3) holds with $c_{1}$ replaced by $1 / n$ :
$$\begin{gathered}
\int_{A} e^{-s / y} y^{8}\left|P_{\delta_{n}}^{*} u_{n}\right|_{g_{n}}^{2} d \nu_{g_{n}} \leq \frac{\delta_{n}^{4}}{n} \\
\int_{A} e^{-s / y}\left(y^{8}\left|\nabla \nabla u_{n}\right|_{g_{n}}^{2}+y^{4}\left|\nabla u_{n}\right|_{g_{n}}^{2}+u_{n}^{2}\right) d \nu_{g_{n}}=1
\end{gathered}$$
where we have set
$$g_{n}:=g_{\delta_{n}}^{(n)} \quad \text { and } \quad P_{\delta_{n}}^{*} \equiv P_{g_{n}}^{*} .$$
Let $y$ be the function on $A$ defined in (3.1). Using (2.18) to express $\nabla \nabla u_{n}$ in terms of $P_{g_{n}}^{*} u_{n}$ and $u_{n}$ one obtains (compare (3.22) below)
$$\begin{aligned}
\int_{A} e^{-s / y} y^{8}\left|\nabla \nabla u_{n}\right|_{g_{n}}^{2} d \nu_{g_{n}} & \leq C \int_{A} e^{-s / y}\left(y^{8}\left|P_{\delta_{n}}^{*}\right|_{g_{n}}^{2}+u_{n}^{2}\right) d \nu_{g_{n}} \\
& \leq C\left(\frac{\delta_{n}^{4}}{n}+\int_{A} e^{-s / y} u_{n}^{2}\right) d \nu_{g_{n}}
\end{aligned}$$
which together with (3.7) implies that there exists $c>0$ such that
$$\int_{A} e^{-s / y}\left(y^{4}\left|\nabla u_{n}\right|_{g_{n}}^{2}+u_{n}^{2}\right) d \nu_{g_{n}} \geq c$$
Now,
$$\left|\nabla u_{n}\right|_{g_{n}}^{2}=z^{2}\left(\left|\partial_{z} u_{n}\right|^{2}+\delta_{n}^{2}\left|\partial_{\theta} u_{n}\right|_{\widehat{g}_{n}}^{2}\right),$$
where $|\cdot| \widehat{g}_{n}$ denotes the norm of a tensor field on $\partial M$ with respect to the metric
$$\widehat{g}_{n}(z):=\widehat{g}^{(n)}\left(\delta_{n} z\right) .$$
Note that, decreasing the constant $\rho_{0}$ of Definition 2.1 if necessary, all the $\widehat{g}_{n}$ 's are uniformly equivalent to $\widehat{b}(0)$. From (3.9) we obtain
$$\int_{A} e^{-s / y}\left(y^{4}\left|\partial_{z} u_{n}\right|^{2}+u_{n}^{2}\right) d \nu_{g_{n}} \geq c$$
for some $c>0$.
Clearly the trace of $P_{g_{n}}^{*} u$ satisfies an estimate of the form (3.6) (compare Appendix A
$$\int_{A} e^{-s / y} y^{8}\left|\Delta_{g_{n}} u_{n}-n u_{n}+O\left(\delta_{n}^{\sigma}\right) u_{n}\right|^{2} d \nu_{g_{n}} \leq C \frac{\delta_{n}^{4}}{n} .$$
Let
$$E:=\nabla \nabla u_{n}-\frac{\Delta_{g_{n}} u_{n}}{n} g_{n}=\nabla \nabla u_{n}-u_{n} g_{n}+\text { error },$$
where the error term is bounded, after integration, as in (3.12). From (3.6) and (3.12) we conclude that
$$\int_{A} e^{-s / y} y^{8}\left|E+O\left(\delta_{n}^{\sigma}\right) u_{n}\right|_{g_{n}}^{2} d \nu_{g_{n}} \leq C \frac{\delta_{n}^{4}}{n}$$
Since $E$ is trace-free we have $E_{z z}=-\delta_{n}^{-2} \widehat{g}_{n}^{C D} E_{C D}$, so that
$$|E|_{g_{n}}^{2}=z^{4}\left(\left(1+\frac{\delta_{n}^{4}}{n-1}\right)\left|E_{z z}\right|^{2}+2 \delta_{n}^{2}\left|E_{z A}\right|_{\widehat{g}_{n}}^{2}+\delta_{n}^{4}\left|E_{A B}-\widehat{g}_{n}^{C D} E_{C D} \widehat{g}_{n A B}\right|_{\widehat{g}_{n}}^{2}\right),$$
which together with the formulae in Appendix A (recall we have assumed $\sigma<1$ ) leads to
$$\begin{aligned}
& \int_{A} e^{-s / y} y^{8}\left(\left|\partial_{z}^{2} u_{n}+z^{-1} \partial_{z} u_{n}-z^{-2} u_{n}+O\left(\delta_{n}^{\sigma}\right) u_{n}\right|^{2}\right. \\
& \quad+\delta_{n}^{2}\left|\partial_{z} \partial_{A} u_{n}+z^{-1} \partial_{A} u_{n}+O\left(\delta_{n} \partial_{\theta} u_{n}\right)+O\left(\delta_{n}^{\sigma}\right) u_{n}\right|_{\widehat{g}_{n}}^{2} \\
& \left.\delta_{n}^{4}\left|D_{A} D_{B} u_{n}-\widehat{g}^{(n)}\left(\delta_{n}\right)^{C D} D_{C} D_{D} u_{n}\left(\widehat{g}_{n}\right)_{A B}+O\left(\delta_{n}^{\sigma}\right) u_{n}\right|_{\widehat{g}_{n}}^{2}\right) d \nu_{g_{n}} \leq C \frac{\delta_{n}^{4}}{n} .
\end{aligned}$$
Next, (3.6) together with the formula for $\left(P_{g_{\delta}}^{*} u\right)_{z z}$ in Appendix A gives
$$\begin{aligned}
\int_{A} e^{-s / y} y^{8} \mid\left[(n-1) z+O\left(\delta_{n}^{\sigma}\right)\right] \partial_{z} u_{n}+\left[(n-1)+O\left(\delta_{n}^{\sigma}\right)\right] u_{n} & \\
& -\left.\delta_{n}^{2} \Delta_{\widehat{g}_{\delta_{n}}} u_{n}\right|^{2} d \nu_{g_{n}} \leq C \frac{\delta_{n}^{4}}{n}
\end{aligned}$$
Choose $\delta_{n_{0}} \neq 0$ and let $H^{1}$ and $H^{2}$ be the Hilbert spaces with norms defined by the left-hand-sides of (3.9) and (3.7) with $n=n_{0}$, and norms, covariant derivatives and measures related to $b_{\delta_{n_{0}}}$ :
$$\begin{gathered}
\|u\|_{H^{1}}:=\int_{A} e^{-s / y}\left(y^{4}|\nabla u|_{b_{\delta_{n_{0}}}}^{2}+u^{2}\right) d \nu_{b_{\delta_{n_{0}}}} \\
\|u\|_{H^{2}}:=\int_{A} e^{-s / y}\left(y^{8}|\nabla \nabla u|_{b_{\delta_{n_{0}}}}^{2}+y^{4}|\nabla u|_{b_{\delta_{n_{0}}}}^{2}+u^{2}\right) d \nu_{b_{\delta_{n_{0}}}} .
\end{gathered}$$

Now, (3.7) shows that $u_{n}$ and $y^{2} \partial_{z} u_{n}$ are bounded in $L^{2}=$ $L^{2}\left(A, e^{-s / y} d \nu_{b_{\delta_{0}}}\right)$. Equation (3.12) proves that $y^{4}$ times the Laplacian of $u_{n}$ is bounded in $L^{2}$. Further, (3.15) establishes that $y^{4} \partial_{z}^{2} u_{n}$ is bounded in $L^{2}$. Simple algebra gives then that $y^{4}$ times the tangential Laplacian of $u_{n}$ is bounded in $L^{2}$. Coming back to (3.15) we obtain that all tangential derivatives of $u_{n}$ are $L^{2}$-bounded, when multiplied by relevant powers of $y$. Standard interpolation gives an $L^{2}$-bound for $y^{2}$ times the first tangential derivatives of $u_{n}$. But (3.15) shows now that the functions $y^{4} \partial_{z} \partial_{A} u_{n}$ are $L^{2}$-bounded. Finally, an interpolation will bound every (weighted) first derivatives of $u_{n}$.

So, the sequence $u_{n}$ is bounded in $H^{2}$, therefore there exists a subsequence, still denoted by $u_{n}$, which converges strongly in $H^{1}$. But (3.8) with $u_{n}$ replaced by $u_{n}-u_{m}$ shows that $u_{n}$ is Cauchy in $H^{2}$, hence there exists $u \in H^{2}$ such that $u_{n}$ converges to $u$ in $H^{2}$. From (3.15) we infer that
$$\begin{aligned}
\mid \partial_{z}^{2} u+z^{-1} \partial_{z} u & -\left.z^{-2} u\right|^{2}+\left|\partial_{z} \partial_{A} u+z^{-1} \partial_{A} u\right|_{b_{\delta_{0}}}^{2} \\
& +\left|D_{A} D_{B} u-\widehat{b}(0)^{C D} D_{C} D_{D} u \widehat{b}(0)_{A B}\right|_{b_{\delta_{n_{0}}}}^{2}=0,
\end{aligned}$$
while (3.16) implies
$$z \partial_{z} u+u=0 .$$
Solving (3.19)-(3.20), we conclude that $u$ is a linear combination of the $u_{(\mu)}$ 's as given by (2.14) for a standard hyperbolic metric, while $u=\operatorname{const} / z$ otherwise. But the integral in (3.5) is continuous on $H^{2}$, which implies
that (3.2) is satisfied in the limit. Similarly, $\delta^{n}$ times the integral (3.4) is continuous on $H^{2}$. Recalling that the family $\left\{u_{(\mu)}\right\}$ is orthogonal with respect to the scalar product defined by the integral in (3.2), we obtain $u=0$. This contradicts (3.9), and proves the result. \(\square\)

Let $\psi=e^{-s / 2 y}, \phi=y^{2}$. We will use spaces $H_{\delta}^{k} \equiv H_{g_{\delta}}^{k}$ of tensor fields on $A$ (compare [8]) for which the norms
$$\|u\|_{H_{\delta}^{k}}:=\left(\int_{A}\left(\sum_{i=0}^{k} \phi^{2 i}\left|\nabla^{(i)} u\right|_{g_{\delta}}^{2}\right) \psi^{2} \delta^{(n-1)} d \mu_{g_{\delta}}\right)^{\frac{1}{2}}$$
are finite, where $\nabla^{(i)}$ stands for the tensor $\underbrace{\nabla \ldots \nabla}_{i \text { times }} u$, with ∇ - the Levi- Civita covariant derivative of $g_{\delta}$; we assume throughout that the metric is at least $W_{\text {loc }}^{1, \infty}$; higher differentiability will be usually indicated whenever needed. The factor $\delta^{(n-1)}$ in front of the measure $d \mu_{g_{\delta}}$ has been included so that $\delta^{(n-1)} d \mu_{g_{\delta}}$ is equivalent to the Lebesgue coordinate measure $d z d \theta$, uniformly in $\delta$.

Note that $H_{g_{\delta}}^{0}$ involves weights, but $L^{2}$ does not.
An equivalent norm, and therefore the same space, is obtained if $g_{\delta}$ in (3.21) is replaced by $b_{\delta}$.

We will need the following:
Lemma 3.4. Let $c_{0}, \sigma>0$ and $s \geq 0$. There exist constants $C=$ $C\left(n, \ell, s, c_{0}, \sigma\right)>0$ and $\delta_{0}=\delta_{0}\left(n, \ell, s, c_{0}, \sigma\right)>0$ such that for all $\left(c_{0}, \ell+2, \sigma\right)$-asymptotically hyperbolic metrics $g$ and for all $0<\delta \leq \delta_{0}$
$$\|u\|_{H_{g_{\delta}}^{\ell+2}} \leq C\left(\left\|\phi^{2} P_{g_{\delta}}^{*} u\right\|_{H_{g_{\delta}}^{\ell}}+\|u\|_{H_{g_{\delta}}^{0}}\right) .$$
Proof: For $\ell=0$ the result has been established in the course of the proof of Proposition 3.1, see the first line of (3.8). For $\ell=1$ we start the calculation that follows with $k=2$ and we stop at the second line, invoking weighted interpolation and the result for $\ell=0$ to conclude. Otherwise, suppose that the result is true for $k-1 \leq \ell_{0}$ with $\ell_{0} \geq 1$. Using [8, Equation (A.4)]
(one can check that the constants in equations (A.2) and (A.3) there, thus also in (A.4), do not depend on $\delta$ ) to control the first term when passing from the second to the third line below, we find for $2 \leq k-1+2 \leq \ell_{0}+2$
$$\begin{aligned}
\left\|\phi^{k+1} \nabla^{(k-1)}\left(\nabla^{(2)} u-\Delta u g_{\delta}\right)\right\|_{H_{g_{\delta}}^{0}}= & \left\|\phi^{k+1} \nabla^{(k-1)}\left(P^{*} u-(n-1) u+O\left(\delta^{\sigma}\right) u\right)\right\|_{H_{g_{\delta}}^{0}} \\
\leq & \left\|\phi^{k+1} \nabla^{(k-1)} P^{*} u\right\|_{H_{g_{\delta}}^{0}} \\
& +C_{1}\|\underbrace{\phi^{2}}_{\leq C} \phi^{k-1} \nabla^{(k-1)}\left[\left(1+O\left(\delta^{\sigma}\right)\right) u\right]\|_{H_{g_{\delta}}^{0}} \\
\leq & C(\left\|\phi^{2} P^{*} u\right\|_{H_{g_{\delta}}^{k-1}}+C_{2} \underbrace{\|u\|_{H_{g_{\delta}}^{k-1}}}_{\leq C\left(\left\|\phi^{2} P^{*} u\right\|_{H_{g_{\delta}}^{k-3}}+\|u\|_{H_{g_{\delta}}^{0}}\right)}) \\
\leq & C\left(1+C C_{2}\right)\left\|\phi^{2} P^{*} u\right\|_{H_{g_{\delta}}^{k-1}}+C^{2} C_{2}\|u\|_{H_{g_{\delta}}^{0}} .
\end{aligned}$$

This is the desired inequality, to see this set
$$T:=\nabla^{(k+1)} u, \quad S:=\nabla^{(k-1)}\left(\nabla^{2} u-\Delta u g_{\delta}\right),$$
or, in index notation,
$$\begin{gathered}
T_{i_{1} \ldots i_{k-1} j k}:=\nabla_{i_{1}} \cdots \nabla_{i_{k-1}} \nabla_{j} \nabla_{k} u \\
S_{i_{1} \ldots i_{k-1} j k}:=\nabla_{i_{1}} \cdots \nabla_{i_{k-1}} \nabla_{j} \nabla_{k} u-\nabla_{i_{1}} \cdots \nabla_{i_{k-1}} \nabla^{\ell} \nabla_{\ell} u\left(g_{\delta}\right)_{j k},
\end{gathered}$$
straightforward algebra shows that
$$|T|_{g_{\delta}}^{2} \leq|S|_{g_{\delta}}^{2},$$
and the Lemma follows. \(\square\)

As in [8] we set
$$L_{g_{\delta}}:=\psi^{-2} P_{g_{\delta}} \phi^{4} \psi^{2} P_{g_{\delta}}^{*}$$
and
$$K_{b_{\delta}}=\operatorname{ker} P_{b_{\delta}}^{*} .$$
The proof of [8, Theorem 3.6] shows that
$$L_{g_{\delta}}^{-1}: H_{g_{\delta}}^{k} \cap K_{\delta}^{\perp_{H_{g_{\delta}}^{0}}^{0}} \rightarrow H_{g_{\delta}}^{k+4}$$
exists for $\delta$ small enough. However, uniform boundedness in $\delta$ of $L_{g_{\delta}}^{-1}$ does not hold in our case, instead we have:

Corollary 3.5. Let $k \in \mathbb{N}, c_{0}, \sigma>0$ and $s \geq 0$. There exist constants $C=C\left(n, k, s, c_{0}, \sigma\right)>0$ and $\delta_{0}=\delta_{0}\left(n, k, s, c_{0}, \sigma\right)>0$ such that for all $\left(c_{0}, k+4, \sigma\right)$-asymptotically hyperbolic metrics $g$, for all $0<\delta \leq \delta_{0}$, and for all $u$ satisfying (3.2) or (3.4)
$$\left\|L_{g_{\delta}}^{-1} u\right\|_{H_{g_{\delta}}^{k+4}} \leq C\left(\|u\|_{H_{g_{\delta}}^{k}}+\delta^{-4}\|u\|_{H_{g_{\delta}}^{0}}\right) .$$
Proof: By Proposition 3.1 we have (recall that $H^{0}$ is weighted but $L^{2}$ is not)
$$\begin{aligned}
c \delta^{4}\|u\|_{H_{g_{\delta}}^{2}}^{2} & \leq\left\|\phi^{2} P_{g_{\delta}}^{*} u\right\|_{H_{g_{\delta}}^{0}}^{2} \\
& =\left\langle\psi^{2} \phi^{2} P_{g_{\delta}}^{*} u, \phi^{2} P_{g_{\delta}}^{*} u\right\rangle_{L_{g_{\delta}}^{2}}=\langle\psi^{2} u, \underbrace{\psi^{-2} P_{g_{\delta}} \phi^{4} \psi^{2} P_{g_{\delta}}^{*}}_{L_{g_{\delta}}} u\rangle_{L_{g_{\delta}}^{2}} \\
& =\left\langle\psi u, \psi L_{g_{\delta}} u\right\rangle_{L_{g_{\delta}}^{2}} \leq\left\|\psi L_{g_{\delta} u}\right\|_{L_{g_{\delta}}^{2}}\|\psi u\|_{L_{g_{\delta}}^{2}}=\left\|L_{g_{\delta}} u\right\|_{H_{g_{\delta}}^{0}}\|u\|_{H_{g_{\delta}}^{0}} .
\end{aligned}$$
Replacing $u$ by $L_{g_{\delta}}^{-1} u$ we conclude that
$$c \delta^{4}\left\|L_{g_{\delta}}^{-1} u\right\|_{H_{g_{\delta}}^{2}} \leq\|u\|_{H_{g_{\delta}}^{0}} .$$
In order to finish the proof we will use the following elliptic estimate, which is standard except for the uniformity in $\delta$; the proof can be found in Appendix B:

Lemma 3.6. Under the conditions of Corollary 3.5, there exists a constant $C$, independent of $g$ and $\delta$, such that for $\delta$ small
$$\|u\|_{H_{g_{\delta}}^{k+4}} \leq C\left(\left\|L_{g_{\delta}} u\right\|_{H_{g_{\delta}}^{k}}+\|u\|_{H_{g_{\delta}}^{0}}\right) .$$ \(\square\)

Returning to the proof of Corollary 3.5, we replace $u$ by $L_{g_{\delta}}^{-1} u$ in (3.26) to obtain
$$\left\|L_{g_{\delta}}^{-1} u\right\|_{H_{g_{\delta}}^{k+4}} \leq C\left(\|u\|_{H_{g_{\delta}}^{k}}+\left\|L_{g_{\delta}}^{-1} u\right\|_{H_{g_{\delta}}^{0}}\right),$$
and the Corollary follows from (3.25). \(\square\)

Summarizing, we have proved:
Theorem 3.7. Let $k \in \mathbb{N}, \sigma>0, c_{0}>0$ and $s \geq 0$. There exist constants $C=C\left(n, s, \sigma, c_{0}\right)>0$ and $\delta_{0}=\delta_{0}\left(n, s, \sigma, c_{0}\right)>0$ such that for all $\left(c_{0}, k+\right.$ $4, \sigma)$-asymptotically hyperbolic metrics $g$, for all $0<\delta \leq \delta_{0}$ and for any $u \in H_{g_{\delta}}^{k+4} \cap K_{b_{\delta}}^{\perp g_{\delta}}$,
$$C \delta^{4}\|u\|_{H_{g_{\delta}}^{k+4}} \leq\left\|L_{g_{\delta}} u\right\|_{H_{g_{\delta}}^{k}} .$$
In particular the operator $\Pi_{K_{b_{\delta}}^{\perp g_{\delta}}} L_{g_{\delta}}$, where $\Pi_{K_{b_{\delta}}^{\perp g_{\delta}}}$ denotes orthogonal projection on $K_{b_{\delta}}^{\perp_{g_{\delta}}}$ in $H_{g_{\delta}}^{0}$, is an isomorphism from $H_{g_{\delta}}^{k+4} \cap K_{b_{\delta}}^{\perp_{g_{\delta}}}$ to $H_{g_{\delta}}^{k} \cap K_{b_{\delta}}^{\perp_{g_{\delta}}}$ such that the norm of its inverse is bounded by $C^{-1} \delta^{-4}$. \(\square\)

At this point, we have established Step 2) of the Introduction, as well as some elements of Step 3). We continue with further details of Step 3).

\section*{4. The gluing construction on a moving annulus}

In this section we prove Theorem 1.2. We set $k=\ell-4$. We consider conformally compact asymptotically hyperbolic metrics $g$ which asymptote, with $k+2$ derivatives, to a fixed AH metric $b$. We fix a small $\delta_{0}>0$ and define the space $W_{b}^{k+4, \infty}\left(M_{4 \delta_{0}}\right)$ of symmetric two tensors with $k+4 b$-covariant derivatives bounded on $M_{4 \delta_{0}}$, relatively to the norm of $b$. Following [8], we assume that $g-b$ is close to zero in $W_{b}^{k+4, \infty}\left(M_{4 \delta_{0}}\right)$.

Similarly to (2.7), we denote by $g_{\delta}$ the metric on $A_{1,4}$ obtained by restricting $g$ to $A_{\delta, 4 \delta}$, and rescaling the $\rho$ coordinate to $A_{1,4}$. Unless explicitly specified otherwise, covariant derivatives on $A_{1,4}$ are related to $g_{\delta}$.

As in [8], consider the map
$$\begin{array}{rll}
f_{g_{\delta}}: & \psi^{2} \phi^{2} H_{\delta}^{k+2} & \longrightarrow H_{\delta}^{k} \cap K_{b_{\delta}}^{\perp} \\
h & \longmapsto \Pi\left\{\psi^{-2}\left[R\left(g_{\delta}+h\right)-R\left(g_{\delta}\right)\right]\right\},
\end{array}$$
where $K_{b_{\delta}}=\operatorname{Ker} P_{b_{\delta}}^{*}$, where $P_{b_{\delta}}^{*}$ is as in (2.9), and $\Pi$ is the $H_{\delta}^{0}$ projection onto $K_{b_{\delta}}^{\perp}$, the $H_{\delta}^{0}$-orthogonal of $K_{b_{\delta}}$; all the spaces here are spaces of tensors on $A_{1,4}$.

One should keep in mind that we are interested in $h$ 's of the form $h=$ $\psi^{2} \phi^{4} P^{*} u, u \in H_{\delta}^{k+4} \cap K_{b_{\delta}}^{\perp}$, with $u$ small in the last space.

Near $h=0$ the map $f_{g_{\delta}}$ is a smooth map between Hilbert spaces. We consider now [8, Proposition G.1] with $x=g_{\delta}$ so that $f_{x}$ there equals $f_{g_{\delta}}$ here. One checks that $f$ satisfies conditions (2) and (3) of [8, Proposition G.1] with the set $A$ there being
$$A=\left\{g_{\delta}, 0<\delta \leq \delta_{0},(g-b) \text { sufficiently small in } W_{b}^{k+4, \infty}\left(M_{4 \delta_{0}}\right)\right\} .$$
Furthermore,
$$V_{x}=\psi^{2} \phi^{2} H_{\delta}^{k+2}, \quad W_{x}=H_{\delta}^{k} \cap K_{b_{\delta}}^{\perp} .$$

Now, $f_{g_{\delta}}$ satisfies a modified version of condition (1) there: here, by Theorem 3.7, we have that $D f_{x}(0)$ has a right inverse $\psi^{2} \phi^{4} P_{g_{\delta}}^{*} L_{g_{\delta}}^{-1}$ bounded by $C_{1} \delta^{-4}$, where $C_{1}$ does not depend upon $x \in A$. For the sake of notational legibility we present the argument without using the smoothing operators of [9]; the latter provide what is needed to obtain the differentiability claimed. Note that we haven't assumed any uniformity in $\delta$ on the modulus of the Hölder continuity of $g$, as the solution will exist, and will have Hölder regularity, without any such assumptions. Any further hypotheses about uniformity of that modulus would be reflected in associated uniformity for the metrics obtained by the gluing procedure, but such uniformity is irrelevant for our purposes.

A repetition of the proof of Proposition G. 1 of [8] with $C_{1}$ there replaced with $C_{1} \delta^{-4}$ yields:

Theorem 4.1. There exist constants $\varepsilon>0$ and $C>0$ such that for all $\delta$ sufficiently small and for all functions $f \in H_{\delta}^{k}$ with
$$\|f\|_{H_{\delta}^{k}} \leq \varepsilon \delta^{4},$$
there exists a unique $h=\psi^{2} \phi^{4} P_{g_{\delta}}^{*} u$, with $\left\|\psi^{-2} \phi^{-2} h\right\|_{H_{\delta}^{k+2}}$ close to zero, satisfying $f_{g_{\delta}}(h)=\Pi f$ and
$$\left\|\psi^{-2} \phi^{-2} h\right\|_{H_{\delta}^{k+2}} \leq C^{\prime}\|u\|_{H_{\delta}^{k+4}} \leq C \delta^{-4}\|f\|_{H_{\delta}^{k}} \leq C \varepsilon .$$

We will use Theorem 4.1 to glue an AH metric $g$, with timelike energymomentum vector, with a Kottler one $b_{p_{(\mu)}}$, on an annulus $A_{\delta, 4 \delta}$. Let $\chi$ be a cutoff function equal to zero on $A_{1,2}$ and to one on $A_{3,4}$. We define a first glued metric on $A_{1,4}$ as
$$g_{\delta, p_{(\mu)}}:=\chi g_{\delta}+(1-\chi) b_{\delta, p_{(\mu)}} .$$
It is clear that the metric $g_{\delta, p_{(\mu)}}$ belongs to the set $A$ of (4.1). Set
$$f:=\psi^{-2}\left[R\left(b_{\delta}\right)-R\left(g_{\delta, p_{(\mu)}}\right)\right]=\psi^{-2}\left[R\left(b_{\delta, p_{(\mu)}}\right)-R\left(g_{\delta, p_{(\mu)}}\right)\right] .$$
Let $p_{(\mu)}^{0}$ be the momentum vector of $g$. We will assume that $g$ has the following asymptotic behaviour
$$\left|g-b_{p_{(\mu)}^{0}}\right| b+\left|\stackrel{\circ}{D}\left(g-b_{p_{(\mu)}^{0}}\right)\right|_{b}+\ldots+\left|\stackrel{\circ}{D}^{(k+2)}\left(g-b_{p_{(\mu)}^{0}}\right)\right|_{b}=O\left(\rho^{\alpha}\right),$$
for some $\alpha>0$, to be restricted shortly; here $\stackrel{\circ}{D}$ is the covariant derivative of $b$. Recall that
$$\left|b_{p_{(\mu)}}-b\right|_{b}+\left|\stackrel{\circ}{D} b_{p_{(\mu)}}\right|_{b}+\ldots+\left|\stackrel{\circ}{D}^{(k+2)} b_{p_{(\mu)}}\right|_{b}=O\left(\rho^{n}\right) .$$
Under (4.4) we have
$$\left|g_{\delta, p_{(\mu)}}-b_{\delta, p_{(\mu)}^{0}}\right| b_{\delta}+\left|\nabla\left(g_{\delta, p_{(\mu)}}-b_{\delta, p_{(\mu)}^{0}}\right)\right|_{b_{\delta}}+\ldots+\left|\nabla^{(k+2)}\left(g_{\delta, p_{(\mu)}}-b_{\delta, p_{(\mu)}^{0}}\right)\right|_{b_{\delta}}=O\left(\delta^{\alpha}\right),$$
where the norm and covariant derivatives are defined by $b_{\delta}$. This implies
$$\begin{aligned}
\left|g_{\delta, p_{(\mu)}}-b_{\delta, p_{(\mu)}}\right| b_{\delta} & \leq\left|g_{\delta, p_{(\mu)}}-b_{\delta, p_{(\mu)}^{0}}\right|_{b_{\delta}}+\left|b_{\delta, p_{(\mu)}}-b_{\delta, p_{(\mu)}^{0}}\right| b_{\delta} \\
& =O\left(\delta^{\alpha}\right)+O\left(\left|p_{(\mu)}-p_{(\mu)}^{0}\right| \delta^{n}\right) \\
& =O\left(\delta^{\alpha}\right)+O\left(\delta^{\beta+n}\right)
\end{aligned}$$
provided that $p_{(\mu)}$ is assumed to satisfy
$$\left|p_{(\mu)}-p_{(\mu)}^{0}\right|=O\left(\delta^{\beta}\right),$$
for some $\beta>0$. An inequality similar to (4.7) holds for derivatives of order up to $k+2$. It follows that the function $f$ defined in (4.3) satisfies
$$\|f\|_{H_{\delta}^{k}}=O\left(\delta^{\alpha}\right)+O\left(\delta^{\beta+n}\right) .$$
By Theorem 4.1 if
$$\alpha>4, \quad \beta+n>4,$$
then for all $\delta$ small enough there exists a solution $h_{\delta, p_{(\mu)}}$ to the equation
$$f_{g_{\delta, p}(\mu)}\left(h_{\delta, p_{(\mu)}}\right)=\Pi f$$
with
$$\left\|\psi^{-2} \phi^{-2} h_{\delta, p_{(\mu)}}\right\|_{H_{\delta}^{k+2}}=O\left(\delta^{\alpha-4}\right)+O\left(\delta^{\beta+n-4}\right) .$$
Summarizing, for all $p_{(\mu)}$, we have constructed a solution $h_{\delta, p_{(\mu)}}$, modulo kernel, to the equation
$$R\left(g_{\delta, p_{(\mu)}}+h_{\delta, p_{(\mu)}}\right)-R(b)=0$$
satisfying (4.10). This finishes Step 3) of the Introduction.
We now proceed to Step 4). Set
$$\widetilde{g}_{\delta, p_{(\mu)}}=g_{\delta, p_{(\mu)}}+h_{\delta, p_{(\mu)}}$$
We consider now the projection onto the kernel as follows. For all $\delta$ small, and for all $p_{(\mu)}$ satisfying (4.8), we define
$$I_{\delta}\left(p_{(\mu)}\right)=\frac{1}{\delta^{n}} \pi\left[\psi^{-2}\left(R\left(\widetilde{g}_{\delta, p_{(\mu)}}\right)-R\left(b_{\delta}\right)\right)\right]$$
where $\pi$ is the $H_{\delta}^{0}$ orthogonal projection onto $K_{b_{\delta}}$. We want to show that we can choose $p_{(\mu)}$ such that $I_{\delta}\left(p_{(\mu)}\right)=0$. We need the following identity, from [10]:
$$\sqrt{\operatorname{det} g} \stackrel{\circ}{N}\left(R_{g}-R_{b}\right)=\partial_{i}\left(\mathbb{U}^{i}(\stackrel{\circ}{N})\right)+\sqrt{\operatorname{det} g}(\rho+Q),$$
where
$$\begin{aligned}
\mathbb{U}^{i}(\stackrel{\circ}{N}) & :=2 \sqrt{\operatorname{det} g}\left(\stackrel{\circ}{N}^{i[k} g^{j] l} \stackrel{\circ}{D}_{j} g_{k l}+D^{[i} \stackrel{\circ}{N}^{j] k} e_{j k}\right) \\
\rho: & \left(-\stackrel{\circ}{N} \operatorname{Ric}(b)_{i j}+\stackrel{\circ}{D}_{i} \stackrel{\circ}{D}_{j} \stackrel{\circ}{N}-\Delta_{b} \stackrel{\circ}{N} b_{i j}\right) g^{i k} g^{j \ell} e_{k \ell} \\
Q & :=\stackrel{\circ}{N}\left(g^{i j}-b^{i j}+g^{i k} g^{j \ell} e_{k \ell}\right) \operatorname{Ric}(b)_{i j}+Q^{\prime}
\end{aligned}$$
Brackets over a symbol denote anti-symmetrisation, with an appropriate numerical factor (1/2 in the case of two indices), and $\stackrel{\circ}{D}$ denotes the covariant derivative operator of the metric $b$; note that $\rho$ here should not be confused with the defining function of the boundary. Here $Q^{\prime}$ denotes an expression which is bilinear in
$$e \equiv e_{i j} d x^{i} d x^{j}:=\left(g_{i j}-b_{i j}\right) d x^{i} d x^{j}$$
and in $\stackrel{\circ}{D}_{k} e_{i j}$, linear in $\stackrel{\circ}{N}, d \stackrel{\circ}{N}$ and Hess $\stackrel{\circ}{N}$, with coefficients which are constants in any ON frame for $b$. The key is that $\rho$ vanishes when $\stackrel{\circ}{N}$ is in the kernel of $P_{b}^{*}$, and then $Q$ is at least quadratic in $e$ near $e=0$. Indeed, the
first term at the right-hand-side of (4.15) does not contain any terms linear in $e_{i j}$ when Taylor expanded at $g_{i j}=b_{i j}$.

The integral of $\mathbb{U}$ at the boundary at infinity provides the momentum vector, and we need to know how fast the limit is approached. The simplest case arises when $g$ is a Kottler metric $b_{m}$ with mass parameter $m$, so that (see (1.2) and (1.3))
$$b_{m}=\frac{d r^{2}}{W^{2}}+r^{2} \stackrel{\circ}{h}, \quad b=\frac{d r^{2}}{\stackrel{\circ}{W}^{2}}+r^{2} \stackrel{\circ}{h},$$
where $\stackrel{\circ}{h}$ is the unit round metric on the sphere $\mathbb{S}^{n-1}$. If $\{r\} \times \mathbb{S}^{n-1}$ is positively oriented, a calculation gives
$$\int_{\{r\} \times \mathbb{S}^{n-1}} \mathbb{U}^{i} d S_{i}=2 \omega_{n-1}(n-1) \stackrel{\circ}{W} W^{-1} m=2 \omega_{n-1}(n-1) m+O\left(r^{-n}\right)$$
where $\omega_{n-1}$ is the volume of $\mathbb{S}^{n-1}$. An identical formula, with $\omega_{n-1}$ replaced by the $\widehat{b}$-volume of $N$, holds for the non-spherical Kottler metrics (2.5). Next, assume that $|g-b|_{b}=O\left(r^{-\alpha}\right)$, where $r$ is a coordinate for $b$ as in (4.16), and $\stackrel{\circ}{h}$ is an ( $r$-independent) metric on the compact conformal boundary $N$, with the same decay rate for first derivatives, and with $R(g)=R(b)$. Integrating (4.12) over $[r, \infty) \times N$ one finds, for $\alpha>n / 2$,
$$\int_{\{r\} \times N} \mathbb{U}^{i}\left(V_{(\mu)}\right) d S_{i}=p_{(\mu)}+O\left(r^{n-2 \alpha}\right)$$
which coincides of course with (4.17) if $\alpha=n$; we note that $\alpha=n$ is the appropriate rate for Kottler metrics, whether boosted or not.

To calculate (4.11) explicitly, let $V_{\delta,(\mu)}$ be a basis of $K_{b_{\delta}}$, the vanishing of (4.11) is then equivalent to the vanishing of the collection of integrals $J_{\delta}(p)=\left(J_{\delta,(\nu)}\right)$, where $p=\left(p_{(\mu)}\right)$ and
$$J_{\delta,(\nu)}:=\int_{A_{1,4}} \psi^{2} \psi^{-2}\left(R\left(\widetilde{g}_{\delta, p_{(\mu)}}\right)-R\left(b_{\delta}\right)\right) V_{\delta,(\nu)} d \mu_{b_{\delta}}$$
In order to use (4.12) we need to change the measure $d \mu_{b_{\delta}}$ to $d \mu_{\widetilde{g}_{\delta, p(\mu)}}$, the following estimates are useful for that:
$$\begin{aligned}
& R\left(\widetilde{g}_{\delta, p_{(\mu)}}\right)-R\left(b_{\delta}\right)=O\left(\delta^{\alpha}\right)+O\left(\delta^{n+\beta}\right) \\
d \mu_{b_{\delta}}= & \left(1+O\left(\delta^{\alpha-4}\right)+O\left(\delta^{n+\beta-4}\right)+O\left(\delta^{n}\right)\right) d \mu_{\widetilde{g}_{\delta, p(\mu)}}
\end{aligned} .$$
Keeping in mind that $V_{\delta,(\nu)}$ behaves as $\delta^{-1}$, and that the volume form grows as $\delta^{1-n}$, this leads to
$$\begin{aligned}
J_{\delta,(\nu)}= & \int_{A_{1,4}} \psi^{2} \psi^{-2}\left(R\left(\widetilde{g}_{\delta, p_{(\mu)}}\right)-R\left(b_{\delta}\right)\right) V_{\delta,(\nu)} d \mu_{\widetilde{g}_{\delta, p}(\mu)} \\
& +O\left(\delta^{2 \alpha-4-n}\right)+O\left(\delta^{2(\beta+n)-4-n}\right)+O\left(\delta^{\alpha}\right)+O\left(\delta^{n+\beta}\right) \\
= & p_{(\nu)}^{0}-p_{(\nu)}+O\left(\delta^{2(\alpha-4)-n}\right)+O\left(\delta^{2(\beta+n-4)-n}\right)+O\left(\delta^{n}\right)+O\left(\delta^{2 \alpha-n}\right) \\
= & \delta^{\beta}\left(\frac{p_{(\nu)}^{0}-p_{(\nu)}}{\delta^{\beta}}+O\left(\delta^{2 \alpha-8-n-\beta}\right)+O\left(\delta^{\beta+n-8}\right)+O\left(\delta^{n-\beta}\right)+O\left(\delta^{2 \alpha-\beta-n}\right)\right) .
\end{aligned}$$

Here the terms $O\left(\delta^{2(\alpha-4)-n}\right)$ and $O\left(\delta^{2(\beta+n-4)-n}\right)$ in the third line arise from the terms quadratic in (4.12) and from the first two terms in the second line, while the terms $O\left(\delta^{n}\right)$ and $O\left(\delta^{2 \alpha-n}\right)$ arise from the difference between the boundary term and its limit (namely $p_{(\mu)}^{0}-p_{(\mu)}$ ) when $\delta$ goes to zero, compare (4.17) and (4.18), and also contain the last two terms in the second line. To close the argument all error terms should go to zero as $\delta$ tends to zero, thus
$$2 \alpha-8-n-\beta>0, \quad \beta+n-8>0, \quad n-\beta>0 .$$
(Note that (4.9) does not impose any further restrictions.) This is equivalent to
$$n \geq 5, \quad \alpha>\frac{8+n+\beta}{2}, \quad \max (8-n, 0)<\beta<n .$$
So $\beta$ can be chosen consistently with those bounds provided that (1.4) holds.
If the kernel of $P_{b}^{*}$ is one-dimensional, with $p_{(\mu)}^{0}=m_{0}$, then for $\delta$ small, using the intermediate value theorem, there exists $p_{(0)}=m$ in an interval $\left[-m_{0}, 2 m_{0}\right]$ such that $J_{\delta}(m)=0=I_{\delta}(m)$, proving existence of a solution.

Otherwise, under (4.20), we can use a Brouwer fixed point theorem as in Lemma 3.18 of [8] with:
\begin{itemize}
\item[-] $U$ : a bounded open ball of centre 0 in $\mathbb{R}^{n+1}$;
\item[-] $G=I d: q_{(\mu)} \mapsto q_{(\mu)}$,
\item[-] $V=U$,
\item[-] $\lambda=1 / \delta$ and $G_{\lambda}=G_{1 / \delta}=\delta^{-\beta} J_{\delta}\left(p_{(\mu)}^{0}+\delta^{\beta} q_{(\mu)}\right)$,
\item[-] $y=0$.
\end{itemize}
This shows that for small $\delta$, we can choose $p_{(\mu)}$ so that $I_{\delta}\left(p_{(\mu)}\right)=0$, which again proves existence of a solution.

Regularity follows from [9, Theorem 4.9]. This completes the proof of Theorem 1.2. \(\square\)

\section*{5. The gluing construction on a fixed annulus}

The question addressed in Theorem 1.1 is a special case of the following: In dimension $n \geq 3$, consider an $n$-dimensional submanifold $M \subset M_{\text {ext }}$, where $M_{\text {ext }}$ has been defined in (1.1), with compact, connected, nonempty boundary $\partial M$ which separates $M_{\text {ext }}$ into two components, one of which is bounded. We further suppose that $M$ is included in the bounded component, and that $M$ is equipped with a metric $g \in C^{\ell, \lambda}, \ell>\left\lfloor\frac{n}{2}\right\rfloor+4, \lambda \in(0,1)$, of constant negative scalar curvature.

Let $M_{1} \subset M$ be a one-sided collar neighbourhood of $\partial M$ contained in $M$, we will refer to $M_{1}$ as the interior collar.

Let $M_{2} \subset M_{\text {ext }}$ be a one-sided collar neighbourhood of $\partial M$ which lies in the unbounded component of $M_{\text {ext }}$, we refer to $M_{2}$ as the exterior collar.

The extension problem is to find a constant scalar curvature metric on $M \cup M_{2}$ which coincides with $g$ on $M$, and which coincides with a Kottler metric near $\partial M_{2} \backslash \partial M$. In this case we set $M^{\prime}=M$ and $M^{\prime \prime}=M \cup M_{2}$. In this problem one would presumably want $M_{2}$ to be small: a solution with a small $M_{2}$ provides a solution for any bigger one.

The deformation problem is to find a constant scalar curvature metric on $M$ which coincides with $g$ on $M \backslash M_{1}$, and which coincides with a Kottler
metric near $\partial M$. In this case we set $M^{\prime}=M \backslash M_{1}$ and $M^{\prime \prime}=M$. Similarly to the previous problem, one would presumably want $M_{1}$ to be small.

Let $p_{(\mu)}^{0}$ denote the energy-momentum vector of $\partial M$, defined as:
$$p_{(\mu)}^{0}=\int_{\partial M} \mathbb{U}^{i}\left(V_{(\mu)}\right) d S_{i}$$
with $\mathbb{U}$ as in (4.13), and $V_{(\mu)}$ defined in Section 2. If $(N, \widehat{b})$ is the round sphere, then $p_{(\mu)}^{0}$ is a vector in $\mathbb{R}^{n+1}$. Otherwise $p_{(\mu)}^{0}$ is simply a number, say $m_{0}$.

Denote by
$$\psi_{\partial M}: b_{p_{(\mu)}} \mapsto \int_{\partial M} \mathbb{U}^{i}\left(V_{(\mu)}\right) d S_{i}$$
the map which to a Kottler metric $b_{p_{(\mu)}}$ associates the energy-moment vector of $\partial M$, where $\mathbb{U}^{i}$ is calculated using (4.13) with $g$ there replaced by $b_{p_{(\mu)}}$.
Remark 5.1. As an illustration, assume that $\partial M=\{r\} \times N$ for some $r$. Suppose that $(N, \widehat{b})$ is not a round sphere, then $\psi_{\partial M}^{-1}$ is a smooth diffeomorphism between an interval of masses around $m_{0}$ and its image; this follows immediately from the (non-spherical equivalent of the) first equality in (4.17). The result remains true in the spherical case when one restricts $\psi_{\partial M}$ to the standard, unboosted Kottler metrics $b_{m}$ as given by (1.2).

Similarly, consider $\partial M=\{r\} \times N$ for some $r$, with $(N, \widehat{b})$ - a round sphere, and assume moreover that $p_{(\mu)}^{0}$ lies in the image of $\psi_{\partial M}$. It is then easily seen from (4.18) that $\psi_{\partial M}^{-1}$ provides a smooth diffeomorphism between a neighbourhood of $p_{(\mu)}^{0}$ and its image provided that $r$ is large enough.

We have the following:
Theorem 5.2. Let $n \geq 3, \mathbb{N} \ni \ell>\left\lfloor\frac{n}{2}\right\rfloor+4, \lambda \in(0,1)$. Assume that the map $\psi_{\partial M}^{-1}$ is a homeomorphism of a neighbourhood of $p_{(\mu)}^{0}$ and its image. There exists $\varepsilon>0$ such that if
$$\left\|g-b_{\psi^{-1}\left(p_{(\mu)}^{0}\right)}^{0}\right\|_{C^{\ell, \lambda}(M)}<\varepsilon,$$
then there exists a $C^{\ell, \lambda}$ metric of constant negative scalar curvature which coincides with $g$ on $M^{\prime}$, and which is a Kottler metric on the unbounded component of $M_{\text {ext }} \backslash \partial M$ away from $M^{\prime \prime}$. If $g$ is smooth, then so is the solution of the deformation problem.

Proof: We proceed as in [8, Section 8.6] but we use the refined versions of Theorem 5.6 and Proposition 5.7 of [8] used there, as given by Theorems 3.1 and 4.9 of [9] (compare Section 6.3 of [9]). The gluing is done on the collar neighbourhood $[0,1] \times \partial M$, with $g_{0}$ there being $b_{p_{(\mu)}}, K=\delta J=0, g$ there equal to $\chi g+(1-\chi) b_{p_{(\mu)}}$ where $\chi$ is a cutoff function which vanishes near $\partial M$, which we identify with $\{1\} \times \partial M$; finally, $p_{(\mu)}$ is close to $\psi_{\partial M}^{-1}\left(p_{(\mu)}^{0}\right)$. One thus obtains a solution modulo kernel (note that for the estimates on pp. 53-54 of [8], we have to replace $\rho$ there with $R+n(n-1)$ ). For the kernel projection (see [8, Equation (8.24), p. 55]) we proceed as in [8], p. 55, where $Q$ there is replaced by $p$ here. By [11, Lemma 3.3] the kernel at $b_{\psi^{-1}\left(p_{(\mu)}^{0}\right)}$ is
one-dimensional except in the spherical case with $b_{\psi^{-1}\left(p_{(\mu)}^{0}\right)}=b$, so except for this last case this is a straightforward continuity argument by varying masses in an interval around $m_{0}$. The Hölder regularity of the final metric follows from Theorem 4.9 of [9]. \(\square\)

Proof of Theorem 1.1: The result follows immediately from Theorem 5.2 and Remark 5.1 except in the spherical case with $b_{\psi^{-1}\left(p_{(\mu)}^{0}\right)}=b$. In this last situation, the supplementary hypothesis of parity insures that all constructions can be made within the class of parity symmetric metrics. The kernel within this class is one-dimensional, and the solution can be adjusted by changing $b_{m}$ in the exterior region within the family of unboosted Kottler metrics; compare the proof of Theorem 2.1 in [7]. \(\square\)

\section*{6. $b$-CONFORMAL DEFORMATIONS NEAR INFINITY}

Let $\bar{M}$ be a compact manifold with boundary, set $M=\bar{M} \backslash \partial M$, and let $\rho$ be a defining function for $\partial M$. Let $\bar{b}$ be a $C^{k+2, \alpha}$ metric on $\bar{M}$. Let $h$ be covariant symmetric two tensor field such that $g=b+h$ is positive definite, and for functions $v>-1$ set $u=1+v$. For $\delta>0$ and $h \in C_{\delta}^{k+2, \alpha}$ we consider the function $F_{g}$ defined on a neighbourhood of zero in $C_{\delta}^{k+2, \alpha}$ to $C_{\delta}^{k, \alpha}$ as
$$F_{g}(v)=-4 \frac{n-1}{n-2} \nabla^{k} \nabla_{k} u+R(g) u+n(n-1) u^{\frac{n+2}{n-2}},$$
where covariant derivatives are related to $g=b+h$, with the spaces $C_{\delta}^{k, \alpha}$ of tensors fields or functions as in [16]. Note that $F_{g}(v)=0$ if and only if the scalar curvature of $u^{\frac{4}{n-2}} g$ equals $-n(n-1)$. The map $F_{g}$ is smooth near zero and, if $R(g)=-n(n-1)$, the derivative at $v=0$ given by
$$F_{g}^{\prime}(0) w=4 \frac{n-1}{n-2}\left(-\nabla^{k} \nabla_{k}+n\right) w .$$
The map $F_{g}^{\prime}(0)$ is an isomorphism from $C_{\delta}^{k+2, \alpha}$ to $C_{\delta}^{k, \alpha}$ when $\delta \in(-1, n)$ [2, Theorem 7.2.1], so in particular when $\delta \in(0, n)$. The implicit function theorem then shows:

Proposition 6.1. Let $k \in \mathbb{N}, \delta \in(0, n), \alpha \in(0,1)$, and for $\stackrel{\circ}{h}^{\circ} \in C_{\delta}^{k+2, \alpha}$ let $\stackrel{\circ}{g}=b+\stackrel{\circ}{h}$ be a metric on $M$ as described above with constant scalar curvature $-n(n-1)$. There exists $\varepsilon>0$ and a constant $C$ such that for any $h \in C_{\delta}^{k+2, \alpha}$ with norm less than $\varepsilon$ there exists a unique $v \in C_{\delta}^{k+2, \alpha}$ satisfying
$$F_{\dot{g}+h}(v)=0, \quad v>-1, \quad\|v\|_{C_{\delta}^{k+2, \alpha}} \leq C\|h\|_{C_{\delta}^{k+2, \alpha}},$$
so that the tensor field $u^{\frac{4}{n-2}}(\stackrel{\circ}{g}+h)$ defines a Riemannian metric with constant scalar curvature $-n(n-1)$. The map $h \mapsto v$ is smooth near zero.

Given a Riemannian metric $\stackrel{\circ}{g}$ as in the statement of Proposition 6.1, we will use that Proposition to construct metrics which are arbitrarily close to $\stackrel{\circ}{g}$ on compact sets, and which are conformal to the background $b$ near infinity, as follows. Let $0<\delta<\sigma, \delta<n$, and let $g_{a}$ be the metric interpolating between $\stackrel{\circ}{g}$ and $b$ on the annulus $A_{a, 4 a}$, as in (4.2). Then $g_{a}=\stackrel{\circ}{g}+h_{a}$,
where $h_{a} \in C_{\sigma}^{k+2, \alpha} \subset C_{\delta}^{k+2, \alpha}$, with $\left\|h_{a}\right\|_{C_{\delta}^{k+2, \alpha}}$ going to zero when $a$ does. Proposition 6.1 shows that for all $a$ small enough there exists $v_{a} \in C_{\delta}^{k+2, \alpha}$ satisfying $v_{a}>-1$ such that the metric
$$\widehat{g}_{a}:=\left(1+v_{a}\right)^{\frac{4}{n-2}} g_{a}$$
has scalar curvature $-n(n-1)$, and $v_{a}$ goes to zero in $C_{\delta}^{k+2, \alpha}$ when $a$ does. In particular, $v_{a}$ goes to zero with $(k+2, \alpha)$ derivatives uniformly on any compact subset of $M$.

The metric $\widehat{g}_{a}$ is conformal to $b$ near the conformal boundary at infinity. If we assume that $\rho^{2} b$ is smooth up to boundary at $\partial M$, then the conformal factor $u$ is polyhomogeneous at the conformal boundary [2, 3] . Further [3], the asymptotic expansion of $u_{a}=1+v_{a}$ is identical to that of the background metric $b$ up to terms $O\left(\rho^{n}\right)$. This implies that $u_{a}$ is in fact smooth up to boundary and, for small $\rho$,
$$\left|\widehat{g}_{a}-b\right|_{b}=O\left(\rho^{n}\right) .$$

If $b$ has the form (1.2), with $\widehat{b}$ - Einstein, and if $\sigma>n / 2$, then the energymomentum vector $p_{(\mu)}$ of $\stackrel{\circ}{g}$ is well defined. We can then choose $\delta>n / 2$, in which case it immediately follows from the definition of $p_{(\mu)}$ and from (4.12)-(4.15) that the energy-momentum vector of $\left(1+v_{a}\right)^{\frac{4}{n-2}} g_{a}$ tends to that of $\dot{g}$ as $a$ goes to zero.

As we have seen, the construction can be done rather generally, resulting in a small conformal deformation of the metric on compact sets. It turns out that the deformation can be localized to the asymptotic region if one supposes, moreover, that $\stackrel{\circ}{g}$ is not static in the asymptotic region; by this we mean that $P_{\dot{g}}^{*}$ has no kernel on $M_{\varepsilon}$ for all $\varepsilon$ small enough. Then the deformation can be localized to the exterior region, in the sense that for any $\varepsilon>0$ we can find a constant scalar curvature metric $\tilde{g}_{\varepsilon}$ which coincides with $\dot{g}$ on $M \backslash M_{\varepsilon}$, with $M_{\varepsilon}$ as in (2.1), and which is conformal to $b$ near the conformal boundary. The construction goes as follows: By the arguments in [4] there exists a sequence of annuli $A_{a_{i}, 4 a_{i}}$ on which $P_{\dot{g}}^{*}$ has no kernel. Choose $a_{i_{0}}<\varepsilon / 4$, for all $a<a_{i_{o}}$ small enough let $\widehat{g}_{a}$ be as in (6.1), then $\widehat{g}_{a}$ restricted to $A_{a_{i_{0}}, 4 a_{i_{0}}}$ approaches zero in $C^{k+2, \alpha}$. By the gluing results of [8, 9], for $k>\left\lfloor\frac{n}{2}\right\rfloor+2$ and for $a$ small enough $\widehat{g}_{a}$ can be deformed within $A_{a_{i_{0}}, 4 a_{i_{0}}}$ to a metric $\tilde{g}_{\varepsilon}$ with constant scalar curvature which coincides with $\dot{g}$ on $M \backslash M_{4 a_{i_{0}}} \subset M \backslash M_{\varepsilon}$, and which coincides with $\widehat{g}_{a}$ on $M_{a_{i_{0}}}$, hence is conformal to $b$ near the conformal boundary at infinity. In particular $\tilde{g}_{\varepsilon}$ approaches $b$ as $O\left(\rho^{n}\right)$ by (6.2).

Summarizing, we have proved the following result, somewhat reminiscent of [21, Proposition 4.1]:

Proposition 6.2. Let $\operatorname{dim} M=n \geq 3, C, \sigma>0, \ell \in \mathbb{N}, \ell \geq 2, \alpha \in(0,1)$ and suppose that $\stackrel{\circ}{g}=b+\stackrel{\circ}{h}$ is a Riemannian metric with scalar curvature $-n(n-1)$ with $\rho^{2} b \in C^{l, \alpha}(\bar{M})$ and $\stackrel{\circ}{h} \in C_{\sigma}^{l, \alpha}$. Then:
\begin{itemize}
\item[(1)] For all $\varepsilon>0$ there exists a metric $\dot{g}_{\varepsilon}$ with scalar curvature $-n(n-1)$, conformal to $\stackrel{\circ}{g}$ away from $M_{\varepsilon}$, and conformal to $b$ near the conformal boundary.
\end{itemize}
\begin{itemize}
\item[(2)] Furthermore $\stackrel{\circ}{g}_{\varepsilon}$ converges to $\stackrel{\circ}{g}$ in $C^{\ell, \alpha}(\mathscr{U})$ topology on any relatively compact open subset $\mathscr{U}$ of $M$.
\item[(3)] If $\rho^{2} b$ is sufficiently differentiable at the conformal boundary (e.g., smooth), then the metrics $\stackrel{\circ}{g}_{\varepsilon}$ approach $b$ as $O\left(\rho^{n}\right)$ for small $\rho$.
\item[(4)] If $b$ is of the form (1.2) with $\widehat{b}$ Einstein, and if $\sigma>n / 2$, then the energy-momentum of $\stackrel{\circ}{g}_{\varepsilon}$ approaches that of $\stackrel{\circ}{g}$ as $\varepsilon$ tends to zero.
\item[(5)] If $\ell>\left\lfloor\frac{n}{2}\right\rfloor+4$ and if there exists $\varepsilon_{0}>0$ such that $P_{\dot{g}}^{*}$ has no kernel on $A_{\varepsilon_{0} / 4, \varepsilon_{0}}$, then $\stackrel{\circ}{g}_{\varepsilon}$ can be chosen to coincide with $\stackrel{\circ}{g}$ away from $M_{\varepsilon_{0}}$, but then the convergence of point (2) to $\stackrel{\circ}{g}$ is in $C^{\ell-2, \alpha}(\mathscr{U})$ topology only.
\end{itemize}

\section*{Appendix A. The asymptotics of $P^{*}$}
A.1. Conformally compact metrics. In this section, we study the behaviour of the operator $P_{g}^{*}$, when rescaled from $A_{\delta, 4 \delta}$ to $A_{1,4}$, with $\delta$ tending to zero, for conformally compact metric, asymptotically hyperbolic in the sense of [18]. We consider on $M_{4 \delta}$ a metric of the form
$$g=\rho^{-2}\left(d \rho^{2}+\widehat{g}(\rho)\right)=: \rho^{-2} \bar{g} .$$
This metric is conformally compact and $|d \rho|_{\bar{g}}=1$ at infinity, so
$$\operatorname{Ric}(g)=-(n-1) g+O(\rho),$$
where $O(\rho)$ is a symmetric covariant two tensor with $g$-norm of order $O(\rho)$ (equivalently $\bar{g}$-norm of order $O\left(\rho^{-1}\right)$ ).

We study the metric on $A_{\delta, 4 \delta}$, of course this calculation is valid for $g=b$ with $b$ as is (2.3) or (1.3). This can be pulled-back to $A=A_{1,4}$ using the change of variable $\rho=\delta z$ to
$$g_{\delta}=z^{-2}\left(d z^{2}+\delta^{-2 \delta} \widehat{g}(z)\right),$$
where $\delta \widehat{g}(z)=\widehat{g}(\delta z)$. The determinant reads
$$\operatorname{det}\left(g_{\delta}\right)=z^{-2 n} \delta^{-2(n-1)} \operatorname{det}\left({ }^{\delta} \widehat{g}\right) .$$
The non-trivial Christoffel symbols of $g_{\delta}$ are
$$\begin{gathered}
\delta \Gamma_{z z}^{z}=-z^{-1}, \\
{ }^{\delta} \Gamma_{A B}^{z}=-\frac{z^{2}}{2}\left(-2 z^{-3} \delta^{-2}{ }^{\delta} \widehat{g}_{A B}+z^{-2} \delta^{-2} \partial_{z}{ }^{\delta} \widehat{g}_{A B}\right), \\
{ }^{\delta} \Gamma_{A z}^{C}={ }^{\delta} \Gamma_{z A}^{C}=\frac{1}{2}\left(-2 z^{-1} \delta_{A}^{C}+{ }^{\delta} \widehat{g}^{B C} \partial_{z}{ }^{\delta} \widehat{g}_{A B}\right), \\
{ }^{\delta} \Gamma_{A B}^{C}=\Gamma_{A B}^{C}\left({ }^{\delta} \widehat{g}\right)=:{ }^{\delta} \widehat{\Gamma}_{A B}^{C} .
\end{gathered}$$
We note that $\partial_{z}{ }^{\delta} \widehat{g}_{A B}(z)=\delta \partial_{\rho} \widehat{g}_{A B}(\delta z)=O(\delta)$. The Hessian of a function $u$ takes the form
$$\begin{gathered}
\delta \nabla_{z} \partial_{z} u=\partial_{z}^{2} u+z^{-1} \partial_{z} u \\
\delta \nabla_{z} \partial_{A} u=\partial_{z} \partial_{A} u+\left(z^{-1} \delta_{A}^{C}+O(\delta)_{A}^{C}\right) \partial_{C} u \\
{ }^{\delta} \nabla_{A} \partial_{B} u={ }^{\delta} \widehat{\nabla}_{A} \partial_{B} u-\left(z^{-1} \delta^{-2 \delta} \widehat{g}_{A B}+O\left(\delta^{-1}\right)_{A B}\right) \partial_{z} u,
\end{gathered}$$
thus
$${ }^{\delta} \nabla^{k} \partial_{k} u=z^{2} \partial_{z}^{2} u-[(n-2) z+O(\delta)] \partial_{z} u+z^{2} \delta^{2 \delta} \widehat{\nabla}^{A} \partial_{A} u .$$
This gives
$$\left(P_{g_{\delta}}^{*} u\right)_{z z}=\left[(n-1) z^{-1}+O(\delta)\right] \partial_{z} u-u \operatorname{Ric}\left(g_{\delta}\right)_{z z}-\delta^{2 \delta} \widehat{\nabla}^{A} \partial_{A} u,$$
$$\begin{aligned}
&\left(P_{g_{\delta}}^{*} u\right)_{z A}=\partial_{z} \partial_{A} u+\left(z^{-1} \delta_{A}^{C}+O(\delta)_{A}^{C}\right) \partial_{C} u-u \operatorname{Ric}\left(g_{\delta}\right)_{z A} \\
&\left(P_{g_{\delta}}^{*} u\right)_{A B}={ }^{\delta} \widehat{\nabla}_{A} \partial_{B} u-{ }^{\delta} \widehat{\nabla}^{C} \partial_{C} u^{\delta} \widehat{g}_{A B}-\delta^{-2} \partial_{z}^{2} u^{\delta} \widehat{g}_{A B} \\
&+\left[(n-3) z^{-1} \delta^{-2 \delta} \widehat{g}_{A B}+O\left(\delta^{-1}\right)_{A B}\right] \partial_{z} u-u \operatorname{Ric}\left(g_{\delta}\right)_{A B} .
\end{aligned}$$

Now, recall that $\operatorname{Ric}(g)=-(n-1) g+\rho^{-1} T$, where $T$ is $\bar{g}$ bounded. As $\bar{g}=d \rho^{2}+\widehat{g}(\rho)=\delta^{2} d z^{2}+\delta^{\delta} \widehat{g}(z)$, we have that $T_{z z}=O\left(\delta^{2}\right), T_{z A}=O(\delta)$ and $T_{A B}=O(1)$, thus the coordinate components of $P_{g_{\delta}}^{*} u$ are
$$\begin{gathered}
\left(P_{g_{\delta}}^{*} u\right)_{z z}=\left[(n-1) z^{-1}+O(\delta)\right] \partial_{z} u+\left[(n-1) z^{-2}+O(\delta)\right] u-\delta^{2} \widehat{\nabla}^{A} \partial_{A} u, \\
\left(P_{g_{\delta}}^{*} u\right)_{z A}=\partial_{z} \partial_{A} u+\left(z^{-1} \delta_{A}^{C}+O(\delta)_{A}^{C}\right) \partial_{C} u-u O(1)_{z A}, \\
\left(P_{g_{\delta}}^{*} u\right)_{A B}=\delta^{\delta} \widehat{\nabla}_{A} \partial_{B} u-{ }^{\delta} \widehat{\nabla}^{C} \partial_{C} u{ }^{\delta} \widehat{g}_{A B}-\delta^{-2} \partial_{z}^{2} u \widehat{g}_{A B} \\
+\left[(n-3) z^{-1} \delta^{-2 \delta} \widehat{g}_{A B}+O\left(\delta^{-1}\right)_{A B}\right] \partial_{z} u \\
+u(n-1)\left(z^{-2} \delta^{-2 \delta} \widehat{g}_{A B}+O\left(\delta^{-1}\right)_{A B}\right) .
\end{gathered}$$
A.2. The $(C, k, \sigma)$-asymptotically hyperbolic case. In this section we compare the behaviour of the operator $P_{g}^{*}$ with that of $P_{b}^{*}$, when rescaled from $A_{\delta, 4 \delta}$ to $A_{1,4}$, for $(C, k, \sigma)$-asymptotically hyperbolic metrics of the form (A.1). We also give an explicit formula for $P_{b}^{*}$ and its kernel for metrics of the form (2.3).

If $k \in \mathbb{N}, \sigma>0$, and $g$ is $(C, k, \sigma)$-asymptotically hyperbolic with $b$ of the form (2.3), we have
$$\operatorname{Ric}(g)=\operatorname{Ric}(b)+O\left(\rho^{\sigma}\right)=-(n-1) b+O\left(\rho^{\sigma}\right)=-(n-1) g+O\left(\rho^{\sigma}\right),$$
where $O\left(\rho^{\sigma}\right)$ is a symmetric covariant two tensor with $g$-norm (or $b$-norm) of order $O\left(\rho^{\sigma}\right)$ (equivalently $\bar{g}$-norm of order $O\left(\rho^{\sigma-2}\right)$ ).