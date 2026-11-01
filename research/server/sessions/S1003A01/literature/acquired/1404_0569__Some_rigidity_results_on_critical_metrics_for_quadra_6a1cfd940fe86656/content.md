---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 1404_0569.pdf
converter: mathpix
format: mmd
---

\title{
SOME RIGIDITY RESULTS ON CRITICAL METRICS FOR QUADRATIC FUNCTIONALS
}

\author{
GIOVANNI CATINO
}

\begin{abstract}
In this paper we prove rigidity results on critical metrics for quadratic curvature functionals, involving the Ricci and the scalar curvature, on the space of Riemannian metrics with unit volume. It is well-known that Einstein metrics are always critical points. The purpose of this article is to show that, under some curvature conditions, a partial converse is true. In particular, for a class of quadratic curvature functionals, we prove that every critical metric with non-negative sectional curvature must be Einstein.
\end{abstract}

\section*{1. Introduction}

Let $M^{n}$ be a closed smooth manifold of dimension $n \geq 3$ and let $\mathscr{M}_{1}\left(M^{n}\right)$ denote the space of equivalence classes of smooth Riemannian metrics of volume one on $M^{n}$. As usual, metrics are identified if they are related by the action of the diffeomorphism group. To fix the notation, we recall the decomposition of the Riemann curvature tensor of a metric $g$ into the Weyl, Ricci and scalar curvature component
$$R m=W+\frac{1}{n-2} R i c ~ \oslash g-\frac{1}{(n-1)(n-2)} R g \text { } \theta g,$$
where ( ) denotes the Kulkarni-Nomizu product. It is well known [9] that Einstein metrics are critical points for the Einstein-Hilbert functional
$$\mathcal{H}=\int R d V$$
on $\mathscr{M}_{1}\left(M^{n}\right)$. From this perspective, it is natural to study canonical metrics which arise as solutions of the Euler-Lagrange equations for more general curvature functionals. In [3], Berger commenced the study of Riemannian functionals which are quadratic in the curvature (see [4, Chapter 4] and [15] for surveys). A basis for the space of quadratic curvature functionals is given by
$$\mathcal{W}=\int|W|^{2} d V \quad \rho=\int|\operatorname{Ric}|^{2} d V \quad \mathcal{S}=\int R^{2} d V$$
and, from the decomposition of the Riemann tensor, one has
$$\mathcal{R}=\int|R m|^{2} d V=\int\left(|W|^{2}+\frac{4}{n-2}|\operatorname{Ric}|^{2}-\frac{2}{(n-1)(n-2)} R^{2}\right) d V .$$
We recall that, in dimension three, the Weyl curvature vanishes, and in dimension four, the Chern-Gauss-Bonnet formula
$$\int\left(|W|^{2}-2|R i c|^{2}+\frac{2}{3} R^{2}\right) d V=32 \pi^{2} \chi(M)$$
implies that the Weyl functional $\mathcal{W}$ can be written as a linear combination of the other two (with the addition of a topological term). All such functionals, which also arise naturally as
total actions in certain gravitational fields theories in physics, have been deeply studied in the last years by many authors. As it will be clear in Section 6, in dimension greater than four, the Euler-Lagrange equation of the Weyl functional $\mathcal{W}$ has a different structure in the zero order curvature terms. In particular, if $n>4$, it is not true that Einstein metrics are always critical points for this functional on $\mathscr{M}_{1}\left(M^{n}\right)$.

For these reasons, following the notation in [7], in the first part of the paper, we will consider only the curvature functional
$$\mathcal{F}_{t}=\int|R i c|^{2} d V+t \int R^{2} d V$$
defined for some constant $t \in \mathbb{R}$ (with $t=-\infty$ formally corresponding to the functional $\mathcal{S}$ ). Since in dimensions greater than four $\mathcal{F}_{t}$ is not scale-invariant, it is natural to restrict the functional on $\mathscr{M}_{1}\left(M^{n}\right)$. Equivalently, one can consider a modified functional properly normalized with the volume of the manifold (see [7]).

It was already observed in [4] that every Einstein metric is critical for $\mathcal{F}_{t}$ on $\mathscr{M}_{1}\left(M^{n}\right)$, for every $t \in \mathbb{R}$. The first basic question is whether all critical metrics are necessarily Einstein. Of course, generally this is false. For instance, in dimension four, every Bach-flat metric is critical for $\mathcal{F}_{-1 / 3}$ and every Weyl and scalar flat metric is critical $\mathcal{F}_{-1 / 4}$ on $\mathscr{M}_{1}\left(M^{4}\right)$ (see [4, Chapter 4]). Moreover, Lamontagne in [14] constructed a homogeneous non-Einstein critical metric for $\mathcal{R}=4 \mathcal{F}_{-1 / 4}$ on $\mathscr{M}_{1}\left(\mathbb{S}^{3}\right)$. From this point of view, it is natural to ask under which conditions a critical metric for $\mathcal{F}_{t}$ must be Einstein. Typically, one assume some curvature conditions (of pointwise or integral type, positivity or negativity of the curvature, etc.) on the critical metric in order to prove rigidity properties. For instance, for $\mathcal{S}$ on $\mathscr{M}_{1}\left(M^{3}\right)$ in [1, Proposition 1.1] the author assumed that the scalar curvature of the critical metric has definite sign (actually this holds in every dimension [5, Proposition 3.1]); for $\mathcal{F}_{-1 / 3}$ on $\mathscr{M}_{1}\left(M^{4}\right)$ (variationally equivalent to $\mathcal{R}$ ) in [13] it is proved that every critical metric with non-positive sectional curvature is Einstein; for $\mathcal{F}_{-1 / 3}$ on $\mathscr{M}_{1}\left(M^{3}\right)$ in [16] the author assumed a pointwise pinching condition on the Ricci curvature; finally, for $\mathcal{F}_{-3 / 8}$ on $\mathscr{M}_{1}\left(M^{3}\right)$ (variationally equivalent to the $\sigma_{2}$ -functional) in [6] the authors proved that every critical metric must be Einstein (hence a space form), just assuming an integral condition, namely $\mathcal{F}_{-3 / 8} \leq 0$ (this result was extended in dimension greater than four in the locally conformally flat case in [10]). As it will be clear from Corollary 2.3 and Corollary 2.4, for some specific values of the parameter $t$, critical metrics for $\mathcal{F}_{t}$ inherit additional properties from the Euler-Lagrange equation which implies more constraints on the variational solution. For instance, every critical metric has constant scalar curvature if $t \neq-1 / 3$ and $n=4$ and it has constant $\sigma_{2}$-curvature if $t=-n / 4(n-1)$ and $n \neq 4$. The results just quoted [13, 6, 10] belong to these cases.

In this paper we will prove some new rigidity results on critical metrics for $\mathcal{F}_{t}$ on $\mathscr{M}_{1}\left(M^{n}\right)$. Our first theorem characterizes critical metrics with non-negative sectional curvature.

Theorem 1.1. Let $M^{n}$ be a closed manifold of dimension $n \geq 3$. If $g$ is a critical metric for $\mathcal{F}_{t}$ on $\mathscr{M}_{1}\left(M^{n}\right)$ for some $t<-1 / 2$ with non-negative sectional curvature, then $g$ is an Einstein metric.

In the case $t=-1 / 2$, we can show the following result.
Theorem 1.2. Let $M^{n}$ be a closed manifold of dimension $n \geq 3$. If $g$ is a critical metric for $\mathcal{F}_{-1 / 2}$ on $\mathscr{M}_{1}\left(M^{n}\right)$ with non-negative sectional curvature, then $g$ is either Einstein or the following possibilities occur
\begin{itemize}
\item[(i)] If $n=3$, then the universal cover $\left(\tilde{M}^{3}, \tilde{g}\right)$ is isometric to $\left(\mathbb{S}^{2} \times \mathbb{R}, a g_{\mathbb{S}^{2}}+b g_{\mathbb{R}}\right)$, for some positive constant $a, b>0$.
\item[(ii)] If $n=4$, then the universal cover $\left(\tilde{M}^{4}, \tilde{g}\right)$ is either isometric to $\left(\mathbb{S}^{2} \times \mathbb{S}^{2}, a g_{\mathbb{S}^{2}}+b g_{\mathbb{S}^{2}}\right)$ or to $\left(\mathbb{S}^{2} \times \mathbb{R}^{2}, a g_{\mathbb{S}^{2}}+b g_{\mathbb{R}^{2}}\right)$, for some positive constant $a, b>0$.
\item[(iii)] If $n>4$, then the universal cover $\left(\tilde{M}^{n}, \tilde{g}\right)$ is isometric to $\left(\mathbb{S}^{2} \times \mathbb{R}^{n-2}, a g_{\mathbb{S}^{2}}+b g_{\mathbb{R}^{n-2}}\right)$, for some positive constant $a, b>0$.
\end{itemize}

Remark 1.3. We notice that the condition $t<-1 / 2$ in Theorem 1.1 is optimal. In fact, for every $t>-1 / 2$, following [14], one can construct non-Einstein critical metrics $g_{t}$ for $\mathcal{F}_{t}$ on $\mathscr{M}_{1}\left(\mathbb{S}^{3}\right)$ (see [7, Section 7]). It turns out that these metrics have non-negative sectional curvature if $-1 / 2<t \leq 3 / 4$. On the other hand, a condition on the sectional curvature is necessary too. In fact, recently Gursky and Viaclovsky in [8] constructed critical metrics for $\mathcal{F}_{t}$ on $\mathscr{M}_{1}\left(M^{4}\right)$ for $t$ "close" to a given value which depends on the topology of the Einstein building blocks. In particular, they found solutions for $t$ close to -1/2 and in some cases for $t<-1 / 2$ (for precise estimates on the critical values see [18]). As it is clear from the construction, all these metrics have changing sign sectional curvature.

Concerning critical metrics with non-positive sectional curvature, we can extend Lamontagne result [13] in dimension four, proving the following

Theorem 1.4. Let $M^{4}$ be a closed manifold of dimension four. If $g$ is a critical metric for $\mathcal{F}_{t}$ on $\mathscr{M}_{1}\left(M^{4}\right)$ for some $t \geq-1 / 4$ with non-positive sectional curvature, then $g$ is an Einstein metric.

In Section 5 we provide a rigidity result on critical metrics for $\mathcal{F}_{t}$ on $\mathscr{M}_{1}\left(M^{3}\right)$ for $t>-1 / 2$. As we have previously observed, one has to assume a stronger condition than non-negative sectional curvature to exclude the non-Einstein examples. Moreover, the estimates used in the proof of Theorem 1.1 are not sufficient in this regime of $t$, due to the presence of bad terms with the wrong sign. We were able to overcome this difficulties by "weighting" the Euler-Lagrange equation, and trying to compensate these quantities. Our result reads as follows

Theorem 1.5. Let $M^{3}$ be a closed manifold of dimension three. If $g$ is a critical metric for $\mathcal{F}_{t}$ on $\mathscr{M}_{1}\left(M^{3}\right)$ for some $-1 / 3 \leq t<-1 / 6$ with non-negative scalar curvature, then $g$ has constant positive sectional curvature if
$$|E|^{2}<\frac{(1+6 t)^{2}}{24} R^{2} .$$
Remark 1.6. In the cases $t=-1 / 3$ (trace-less Ricci functional) and $t=-5 / 16$ (Schouten functional), our result considerably improves the ones in [16] and in [11, Theorem 4.2], respectively. Moreover, for $t=-1 / 4$ (Riemann functional), Theorem 1.5 gives a first answer to a basic question posed by Anderson [1, Section 6] concerning the rigidity of critical metrics for the $L^{2}$-norm of the Riemann curvature tensor $\mathcal{R}$.

Remark 1.7. We notice that the result in Theorem 1.5 also holds when $t \leq-1 / 2$. In fact, the pinching assumption implies that $g$ has positive sectional curvature and Theorems 1.1 and 1.2 apply. Formally, in the case $t=-\infty$, we recover part of a result in [1] on critical metrics for $\mathcal{S}$.

In the last part of the paper (Section 6), we will compute the Euler-Lagrange equation satisfied by critical metrics for a general quadratic curvature functional of the form
$$\mathcal{F}_{t, s}=\int|\operatorname{Ric}|^{2} d V+t \int R^{2} d V+s \int|R m|^{2} d V$$
defined for some constants $t, s \in \mathbb{R}$. As we have already observed, from the variational point of view this functional differs from $\mathcal{F}_{t}$ only in dimension greater than four. As one would expect, space form metrics are critical for $\mathcal{F}_{t, s}$ on $\mathscr{M}_{1}\left(M^{n}\right)$, whereas, due to the presence of the full curvature tensor, in general Einstein metrics are not. Hence, a basic question would be to find variational characterization of space form metrics as critical points for $\mathcal{F}_{t, s}$ on $\mathscr{M}_{1}\left(M^{n}\right)$, in the spirit of the work of Gursky and Viaclovsky [6] on critical metrics for
$$\mathcal{F}_{-n / 4(n-1)}=-2(n-2)^{2} \int \sigma_{2}(A) d V$$
where $\sigma_{2}(A)$ denotes the second elementary symmetric function of the Schouten tensor (see [17]). As we have already observed (see Corollary 2.4), in dimension $n \neq 4$, a critical metric $g$ for this functional satisfy the Yamabe-type equation
$$\sigma_{2}\left(A_{g}\right)=\text { const } .$$
We will show in Corollay 6.4 that, for every $t \in \mathbb{R}$, the functional
$$\mathcal{F}_{t,-\frac{n+4(n-1) t}{4}}$$
naturally extend the $\sigma_{2}$-functional (which correspond exactly to the case $s=0$ ). More precisely, we will prove that for every $t \in \mathbb{R}$, a critical metric $g$ for $\mathcal{F}_{t,-\frac{n+4(n-1) t}{4}}$ on $\mathscr{M}_{1}\left(M^{n}\right)$, $n>4$, satisfies the Yamabe-type equation
$$(1+2(n-1) t) \sigma_{2}\left(A_{g}\right)-\frac{n+4(n-1) t}{16(n-2)}\left|W_{g}\right|^{2}=\text { const. }$$
We hope that this property could help in proving some new variational characterizations of space forms as critical metrics of these functionals.

To conclude, we mention that the problem of finding conditions that guarantee rigidity of critical metrics for quadratic curvature functionals also has a lot of interest in the non-compact setting. For instance, Anderson in [2] proved that every complete three-dimensional critical metric for the Ricci functional $\rho$ with non-negative scalar curvature is flat, whereas in [5] we showed a characterization of complete critical metrics for $\mathcal{S}$ with non-negative scalar curvature in every dimension.

\section*{2. The Euler-Lagrange equation for $\mathcal{F}_{t}$}

In this section we will compute the Euler-Lagrange equation satisfied by critical metrics for $\mathcal{F}_{t}$ on $\mathscr{M}_{1}\left(M^{n}\right)$ (see also [7]). The gradients of the functionals $\rho$ and $\mathcal{S}$ are given by (see [4, Proposition 4.66])
$$\begin{gathered}
(\nabla \rho)_{i j}=-\Delta R_{i j}-2 R_{i k j l} R_{k l}+\nabla_{i j}^{2} R-\frac{1}{2}(\Delta R) g_{i j}+\frac{1}{2}|R i c|^{2} g_{i j}, \\
(\nabla \mathcal{S})_{i j}=2 \nabla_{i j}^{2} R-2(\Delta R) g_{i j}-2 R R_{i j}+\frac{1}{2} R^{2} g_{i j} .
\end{gathered}$$

Hence, the gradient of $\mathcal{F}_{t}$ reads
$$\left(\nabla \mathcal{F}_{t}\right)_{i j}=-\Delta R_{i j}+(1+2 t) \nabla_{i j}^{2} R-\frac{1+4 t}{2}(\Delta R) g_{i j}+\frac{1}{2}\left(|R i c|^{2}+t R^{2}\right) g_{i j}-2 R_{i k j l} R_{k l}-2 t R R_{i j} .$$
Moreover, $g$ is critical for $\mathcal{F}_{t}$ on $\mathscr{M}_{1}\left(M^{n}\right)$ if and only if $\left(\nabla \mathcal{F}_{t}\right)=c g$, for some Lagrange multiplier $c \in \mathbb{R}$ (see [4]). Tracing this equation, we obtain
$$\frac{n-4}{2}\left(|R i c|^{2}+t R^{2}\right)-\frac{n+4(n-1) t}{2} \Delta R=n c .$$
From these, we get that $g$ is critical for $\mathcal{F}_{t}$ on $\mathscr{M}_{1}\left(M^{n}\right)$ if and only if
$$-\Delta R_{i j}+(1+2 t) \nabla_{i j}^{2} R-\frac{2 t}{n}(\Delta R) g_{i j}+\frac{2}{n}\left(|R i c|^{2}+t R^{2}\right) g_{i j}-2 R_{i k j l} R_{k l}-2 t R R_{i j}=0,$$
and
$$(n+4(n-1) t) \Delta R=(n-4)\left(|\operatorname{Ric}|^{2}+t R^{2}-\lambda\right),$$
where $\lambda=\mathcal{F}_{t}(g)$. Defining the tensor $E$ to be the trace-less Ricci tensor, $E_{i j}=R_{i j}-\frac{1}{n} R g_{i j}$, we obtain the Euler-Lagrange equation of critical metrics for $\mathcal{F}_{t}$ on $\mathscr{M}_{1}\left(M^{n}\right)$.

Proposition 2.1. Let $M^{n}$ be a closed manifold of dimension $n \geq 3$. A metric $g$ is critical for $\mathcal{F}_{t}$ on $\mathscr{M}_{1}\left(M^{n}\right)$ if and only if it satisfies the following equations
$$\begin{gathered}
\Delta E_{i j}=(1+2 t) \nabla_{i j}^{2} R-\frac{1+2 t}{n}(\Delta R) g_{i j}-2 R_{i k j l} E_{k l}-\frac{2+2 n t}{n} R E_{i j}+\frac{2}{n}|E|^{2} g_{i j}, \\
(n+4(n-1) t) \Delta R=(n-4)\left(|R i c|^{2}+t R^{2}-\lambda\right),
\end{gathered}$$
where $\lambda=\mathcal{F}_{t}(g)$.
In particular, it follows that Einstein metrics are critical (see [4, Corollary 4.67]).
Corollary 2.2. Any Einstein metric is critical for $\mathcal{F}_{t}$ on $\mathscr{M}_{1}\left(M^{n}\right)$.
From equation (2.3), if $n=4$ and $t \neq-1 / 3$, we immediately get the following result.
Corollary 2.3. Let $M^{4}$ be a closed manifold of dimension four. If $g$ is a critical metric for $\mathcal{F}_{t}$ on $\mathscr{M}_{1}\left(M^{4}\right)$ for some $t \neq-1 / 3$, then $g$ has constant scalar curvature.

Notice that, in dimension four, Gauss-Bonnet formula implies that $\mathcal{F}_{-1 / 3}$ is proportional (plus a constant term) to the Weyl functional $\mathcal{W}$. Hence, critical metrics are Bach-flat and, in general, do not have constant scalar curvature. On the other hand, if $t=-n / 4(n-1)$, one has
$$|R i c|^{2}-\frac{n}{4(n-1)} R^{2}=-2(n-2)^{2} \sigma_{2}(A),$$
where $\sigma_{2}(A)$ denotes the second elementary symmetric function of the Schouten tensor
$$A=\frac{1}{n-2}\left(\text { Ric }-\frac{1}{2(n-1)} R g\right) .$$
Hence, when $n \neq 4$ and $t=-n / 4(n-1)$, we have
$$\mathcal{F}_{-n / 4(n-1)}=-2(n-2)^{2} \int \sigma_{2}(A) d V$$
and equation (2.3) implies the following

Corollary 2.4. Let $M^{n}$ be a closed manifold of dimension $n \neq 4$. If $g$ is a critical metric for $\mathcal{F}_{-n / 4(n-1)}$ on $\mathscr{M}_{1}\left(M^{n}\right)$, then $g$ has constant $\sigma_{2}$-curvature.

Now, contracting equation (2.2) with $E$ we obtain the following Weitzenböck formula.
Proposition 2.5. Let $M^{n}$ be a closed manifold of dimension $n$. If $g$ is a critical metric for $\mathcal{F}_{t}$ on $\mathscr{M}_{1}\left(M^{n}\right)$, then the following formula holds
$$\frac{1}{2} \Delta|E|^{2}=|\nabla E|^{2}+(1+2 t) E_{i j} \nabla_{i j}^{2} R-2 R_{i k j l} E_{i j} E_{k l}-\frac{2+2 n t}{n} R|E|^{2} .$$

Corollary 2.6. Let $M^{n}$ be a closed manifold of dimension $n$. If $g$ is a critical metric for $\mathcal{F}_{t}$ on $\mathscr{M}_{1}\left(M^{n}\right)$, then
$$\int\left(|\nabla E|^{2}-\frac{(n-2)(1+2 t)}{2 n}|\nabla R|^{2}\right) d V=2 \int\left(R_{i k j l} E_{i j} E_{k l}+\frac{1+n t}{n} R|E|^{2}\right) d V .$$
Proof. We simply integrate by parts equation (6.4) and use the second Bianchi identity
$$\nabla_{i} E_{i j}=\nabla_{i} R_{i j}-\frac{1}{n} \nabla_{j} R=\frac{n-2}{2 n} \nabla_{j} R .$$ \(\square\)

\section*{3. Critical metrics with non-negative sectional curvature}

In this section we will prove Theorem 1.1 and Theorem 1.2. The first key observation is the following pointwise estimate which is satisfied by every metric with non-negative sectional curvature.

Proposition 3.1. Let $\left(M^{n}, g\right)$ be a Riemannian manifold of dimension $n \geq 3$ with non-negative sectional curvature. Then, the following estimate holds
$$R_{i k j l} E_{i j} E_{k l} \leq \frac{n-2}{2 n} R|E|^{2} .$$
Proof. Let $\left\{e_{i}\right\}, i=1, \ldots, n$, be the eigenvectors of $E$ and let $\lambda_{i}$ be the corresponding eigenvalues. Moreover, let $\sigma_{i j}$ be the sectional curvature defined by the two-plane spanned by $e_{i}$ and $e_{j}$. We want to prove that the quantity
$$R_{i k j l} E_{i j} E_{k l}-\frac{n-2}{2 n} R|E|^{2}=\sum_{i, j=1}^{n} \lambda_{i} \lambda_{j} \sigma_{i j}-\frac{n-2}{2 n} R \sum_{k=1}^{n} \lambda_{k}^{2}$$
is non-positive if $\sigma_{i j} \geq 0$ for all $i, j=1, \ldots, n$. The scalar curvature can be written as
$$R=g^{i j} g^{k l} R_{i k j l}=\sum_{i, j=1}^{n} \sigma_{i j}=2 \sum_{i<j} \sigma_{i j} .$$
Hence, one has the following
$$\begin{aligned}
\sum_{i, j=1}^{n} \lambda_{i} \lambda_{j} \sigma_{i j}-\frac{n-2}{2 n} R \sum_{k=1}^{n} \lambda_{k}^{2} & =2 \sum_{i<j} \lambda_{i} \lambda_{j} \sigma_{i j}-\frac{n-2}{n} \sum_{i<j} \sigma_{i j} \sum_{k=1}^{n} \lambda_{k}^{2} \\
& =\sum_{i<j}\left(2 \lambda_{i} \lambda_{j}-\frac{n-2}{n} \sum_{k=1}^{n} \lambda_{k}^{2}\right) \sigma_{i j} .
\end{aligned}$$

On the other hand, one has
$$\sum_{k=1}^{n} \lambda_{k}^{2}=\lambda_{i}^{2}+\lambda_{j}^{2}+\sum_{k \neq i, j} \lambda_{k}^{2}$$
Moreover, using the Cauchy-Schwarz inequality and the fact that $\sum_{k=1}^{n} \lambda_{k}=0$, we obtain
$$\sum_{k \neq i, j} \lambda_{k}^{2} \geq \frac{1}{n-2}\left(\sum_{k \neq i, j} \lambda_{k}\right)^{2}=\frac{1}{n-2}\left(\lambda_{i}+\lambda_{j}\right)^{2} .$$
Hence, the following estimate holds
$$\sum_{k=1}^{n} \lambda_{k}^{2} \geq \frac{n-1}{n-2}\left(\lambda_{i}^{2}+\lambda_{j}^{2}\right)+\frac{2}{n-2} \lambda_{i} \lambda_{j} .$$
Using this, since $\sigma_{i j} \geq 0$, it follows that
$$\begin{aligned}
\sum_{i, j=1}^{n} \lambda_{i} \lambda_{j} \sigma_{i j}-\frac{n-2}{2 n} R \sum_{k=1}^{n} \lambda_{k}^{2} & \leq \frac{n-1}{n} \sum_{i<j}\left(2 \lambda_{i} \lambda_{j}-\left(\lambda_{i}^{2}+\lambda_{j}^{2}\right)\right) \sigma_{i j} \\
& =-\frac{n-1}{n} \sum_{i<j}\left(\lambda_{i}-\lambda_{j}\right)^{2} \sigma_{i j} \leq 0 .
\end{aligned}$$
This concludes the proof of the proposition. \(\square\)

From Corollary 6.7, we have that if $g$ is a critical metric for $\mathcal{F}_{t}$ on $\mathscr{M}_{1}\left(M^{n}\right)$, then
$$\int\left(|\nabla E|^{2}-\frac{(n-2)(1+2 t)}{2 n}|\nabla R|^{2}\right) d V=2 \int\left(R_{i k j l} E_{i j} E_{k l}+\frac{1+n t}{n} R|E|^{2}\right) d V .$$
If $t \leq-1 / 2$, the left-hand side is nonnegative and is zero if and only if $|\nabla E|=0$. On the other hand, if $g$ has non-negative sectional curvature, Proposition 3.1, implies that
$$R_{i k j l} E_{i j} E_{k l}+\frac{1+n t}{n} R|E|^{2} \leq\left(t+\frac{1}{2}\right) R|E|^{2} .$$
In particular, if $g$ is a critical metric $g$ for $\mathcal{F}_{t}$ on $\mathscr{M}_{1}\left(M^{n}\right)$ with non-negative sectional curvature, we have
$$\int\left(|\nabla E|^{2}-\frac{(n-2)(1+2 t)}{2 n}|\nabla R|^{2}\right) d V \leq(1+2 t) \int R|E|^{2} d V .$$
Hence, if $t<-1 / 2$, then $g$ has to be scalar flat or Einstein. If $R \equiv 0$, then $g$ must be flat, since it has non-negative sectional curvature. This concludes the proof of Theorem 1.1.

If $t=-1 / 2$, we have that $\nabla E=0$ on $M^{n}$. In particular, $g$ has constant scalar curvature, and, from the de Rham decomposition theorem, is locally a product of Einstein metrics. Again, if $R \equiv 0$, then $g$ has to be flat. So, from now on, we will assume that $g$ has constant positive scalar curvature $R>0$. From the critical equation (2.1) we get
$$\frac{1}{n}\left(|R i c|^{2}-\frac{1}{2} R^{2}\right) g_{i j}-R_{i k j l} R_{k l}+\frac{1}{2} R R_{i j}=0$$
Moreover, since $g$ has parallel Ricci tensor, the commutation rule of covariant derivatives, implies
$$0=\nabla_{p} \nabla_{j} R_{i k}-\nabla_{j} \nabla_{p} R_{i k}=R_{l i j p} R_{k l}+R_{l k j p} R_{i l} .$$

Tracing with $g^{p k}$, we get $R_{i k j l} R_{k l}=R_{i k} R_{j k}$. Hence, the Ricci tensor satisfies the quadratic condition
$$\frac{1}{n}\left(2|R i c|^{2}-R^{2}\right) g_{i j}-2 R_{i k} R_{j k}+R R_{i j}=0$$
In particular, every eigenvalue $\mu$ of the Ricci tensor, satisfies the equation
$$\frac{1}{n}\left(2|R i c|^{2}-R^{2}\right)-2 \mu^{2}+R \mu=0,$$
which implies that
$$2 \mu^{2}-R \mu-\frac{2}{n}\left(|E|^{2}-\frac{n-2}{2 n} R^{2}\right)=0 .$$
Solving this equation, we get that every eigenvalue satisfies
$$\mu=\frac{1}{4} R \pm \sqrt{\frac{(n-4)^{2}}{16 n^{2}} R^{2}+\frac{1}{n}|E|^{2}} .$$
Now, let us assume that for some $\mathbb{N} \ni m \geq 1$, we have
$$\mu_{1}=\ldots=\mu_{m}=\frac{1}{4} R+\sqrt{\frac{(n-4)^{2}}{16 n^{2}} R^{2}+\frac{1}{n}|E|^{2}}$$
and
$$\mu_{m+1}=\ldots=\mu_{n}=\frac{1}{4} R-\sqrt{\frac{(n-4)^{2}}{16 n^{2}} R^{2}+\frac{1}{n}|E|^{2}}$$
Clearly, if $m=1$, we have that $\mu_{1}=0$ on $M^{n}$ and $\mu_{2}=\ldots=\mu_{n}=\frac{1}{2} R$. If this is the case, then $n=3$ and we are exactly in case (i) of Theorem 1.2. On the other hand, if $m=n$ then the metric is Einstein. So, from now on we will assume that $2 \leq m<n$. Moreover, by summing all the eigenvalues, we get the identity
$$\frac{n-4}{4} R=(n-2 m) \sqrt{\frac{(n-4)^{2}}{16 n^{2}} R^{2}+\frac{1}{n}|E|^{2}} .$$
Since $R>0$, we have that $m=2$ if $n=3$ or $n=4$, and $m<n / 2$ if $n>4$. Thus, if $n=4$, we have that
$$\mu_{1}=\mu_{2}=\frac{1}{4} R+\frac{1}{2}|E| \quad \text { and } \quad \mu_{3}=\mu_{4}=\frac{1}{4} R-\frac{1}{2}|E| .$$
On the other hand, if $n \neq 4$, one has
$$|E|^{2}=\frac{m(n-m)(n-4)^{2}}{4 n(n-2 m)^{2}} R^{2} .$$
Thus, if $n=3$, we have proved that
$$\mu_{1}=\mu_{2}=\frac{1}{2} R \quad \text { and } \quad \mu_{3}=0,$$
whereas, for $n>4$, one has that
$$\mu_{1}=\ldots=\mu_{m}=\frac{n-m-2}{2(n-2 m)} R \quad \text { and } \quad \mu_{m+1}=\ldots=\mu_{n}=\frac{2-m}{2(n-2 m)} R .$$
Since $g$ has non-negative Ricci curvature, if $n>4$ the only admissible case is $m=2$, so
$$\mu_{1}=\mu_{2}=\frac{1}{2} R \quad \text { and } \quad \mu_{3}=\ldots=\mu_{n}=0 .$$

In conclusion, as a consequence of the de Rham decomposition theorem, we have shown that if $g$ is a critical metric for $\mathcal{F}_{-1 / 2}$ on $\mathscr{M}_{1}\left(M^{n}\right)$ with non-negative sectional curvature, then $g$ is either Einstein or the following possibilities occur
\begin{itemize}
\item[(i)] If $n=3$, then the eigenvalues of the Ricci tensor are equal to $\mu_{1}=\mu_{2}=\frac{1}{2} R$ and $\mu_{3}=0$, where $R$ is a positive constant. In particular, the universal cover $\left(\tilde{M}^{3}, \tilde{g}\right)$ is isometric to $\left(\mathbb{S}^{2} \times \mathbb{R}, a g_{\mathbb{S}^{2}}+b g_{\mathbb{R}}\right)$, for some positive constant $a, b>0$.
\item[(ii)] If $n=4$, then the eigenvalues of the Ricci tensor are equal to $\mu_{1}=\mu_{2}=\frac{1}{4} R+\frac{1}{2}|E|$ and $\mu_{3}=\mu_{4}=\frac{1}{4} R-\frac{1}{2}|E|$, where $R$ and $|E|$ are positive constants. Now, there are two possibilities: either $\mu_{3}=\mu_{4}>0$ or $\mu_{3}=\mu_{4}=0$. Hence, the universal cover $\left(\tilde{M}^{4}, \tilde{g}\right)$ is either isometric to $\left(\mathbb{S}^{2} \times \mathbb{S}^{2}, a g_{\mathbb{S}^{2}}+b g_{\mathbb{S}^{2}}\right)$ or to $\left(\mathbb{S}^{2} \times \mathbb{R}^{2}, a g_{\mathbb{S}^{2}}+b g_{\mathbb{R}^{2}}\right)$, for some positive constant $a, b>0$.
\item[(iii)] If $n>4$, then the eigenvalues of the Ricci tensor are equal to $\mu_{1}=\mu_{2}=\frac{1}{2} R$ and $\mu_{3}=\ldots=\mu_{n}=0$, where $R$ is a positive constant. Since $g$ has non-negative sectional curvature, the Ricci flat part has to be flat. Hence, the universal cover $\left(\tilde{M}^{n}, \tilde{g}\right)$ is isometric to $\left(\mathbb{S}^{2} \times \mathbb{R}^{n-2}, a g_{\mathbb{S}^{2}}+b g_{\mathbb{R}^{n-2}}\right)$, for some positive constant $a, b>0$.
\end{itemize}

This concludes the proof of Theorem 1.2.

\section*{4. Critical metrics with non-positive sectional curvature}

In this section we will prove Theorem 1.4. First of all we show some useful estimates which hold for every $n$-dimensional Riemannian manifold. We recall the definition of the Cotton tensor
$$C_{i j k}=\nabla_{k} R_{i j}-\nabla_{j} R_{i k}-\frac{1}{2(n-1)}\left(\nabla_{k} R g_{i j}-\nabla_{j} R g_{i k}\right) .$$
We have the following formula (see [6, Section 4] for this formula in dimension three).
Proposition 4.1. Let $\left(M^{n}, g\right)$ be a Riemannian manifold of dimension $n \geq 3$. Then, the following integral formula holds
$$\int\left(|\nabla E|^{2}-\frac{(n-2)^{2}}{4 n(n-1)}|\nabla R|^{2}-\frac{1}{2}|C|^{2}\right) d V=\int\left(R_{i k j l} E_{i j} E_{k l}-E_{i j} E_{i k} E_{j l}-\frac{1}{n} R|E|^{2}\right) d V .$$
Proof. A simple computation shows that
$$\frac{1}{2}|C|^{2}=|\nabla E|^{2}-\frac{(n-2)^{2}}{4 n^{2}(n-1)}|\nabla R|^{2}-\nabla_{k} E_{i j} \nabla_{j} E_{i k} .$$
Integrating by parts the last term, we get
$$\begin{aligned}
\int \nabla_{k} E_{i j} \nabla_{j} E_{i k} d V & =-\int E_{i j} \nabla_{k} \nabla_{j} E_{i k} d V \\
& =-\int\left(E_{i j} \nabla_{j} \nabla_{k} E_{i k}+R_{k j i l} E_{i j} E_{k l}+E_{i j} E_{i k} E_{j l}+\frac{1}{n} R|E|^{2}\right) d V \\
& =-\int\left(\frac{n-2}{2 n} E_{i j} \nabla_{i} \nabla_{j} R-R_{i k j l} E_{i j} E_{k l}+E_{i j} E_{i k} E_{j l}+\frac{1}{n} R|E|^{2}\right) d V \\
& =\int\left(\frac{(n-2)^{2}}{4 n^{2}}|\nabla R|^{2}+R_{i k j l} E_{i j} E_{k l}-E_{i j} E_{i k} E_{j l}-\frac{1}{n} R|E|^{2}\right) d V .
\end{aligned}$$
Using this identity and integrating equation (4.1) we get the desired result. \(\square\)

Proposition 4.2. Let $\left(M^{n}, g\right)$ be a Riemannian manifold of dimension $n \geq 3$ with non-positive sectional curvature. Then, the following estimate holds
$$R_{i k j l} E_{i j} E_{k l}+\frac{1}{n} R|E|^{2}+E_{i j} E_{i k} E_{j l} \leq 0 .$$
Moreover, if $n=4$, equality occurs if and only if $|E|=0$.
Proof. As in the proof of Proposition 3.1, we let $\left\{e_{i}\right\}, i=1, \ldots, n$, be the eigenvectors of $E$ and Ric and let $\lambda_{i}$ and $\mu_{i}$ be the corresponding eigenvalues. Moreover, let $\sigma_{i j}$ be the sectional curvature defined by the two-plane spanned by $e_{i}$ and $e_{j}$. We want to prove that the quantity
$$R_{i k j l} E_{i j} E_{k l}+\frac{1}{n} R|E|^{2}+E_{i j} E_{i k} E_{j l}=\sum_{i, j=1}^{n} \lambda_{i} \lambda_{j} \sigma_{i j}+\frac{1}{n} R \sum_{k=1}^{n} \lambda_{k}^{2}+\sum_{k=1}^{n} \lambda_{k}^{3}$$
is non-positive if $\sigma_{i j} \leq 0$ for all $i, j=1, \ldots, n$. First of all, we notice that
$$\sum_{i, j=1}^{n} \lambda_{i} \lambda_{j} \sigma_{i j}+\frac{1}{n} R \sum_{k=1}^{n} \lambda_{k}^{2}+\sum_{k=1}^{n} \lambda_{k}^{3}=2 \sum_{i<j}^{n} \lambda_{i} \lambda_{j} \sigma_{i j}+\sum_{k=1}^{n} \mu_{k} \lambda_{k}^{2},$$
since $\mu_{k}=\lambda_{k}+\frac{1}{n} R$. Moreover, for every $k, \mu_{k}=\sum_{i \neq k} \sigma_{i k}$ and
$$\sum_{k=1}^{n} \mu_{k} \lambda_{k}^{2}=\sum_{i<j}\left(\lambda_{i}^{2}+\lambda_{j}^{2}\right) \sigma_{i j} .$$
Hence
$$\sum_{i, j=1}^{n} \lambda_{i} \lambda_{j} \sigma_{i j}+\frac{1}{n} R \sum_{k=1}^{n} \lambda_{k}^{2}+\sum_{k=1}^{n} \lambda_{k}^{3}=\sum_{i<j}\left(2 \lambda_{i} \lambda_{j}+\lambda_{i}^{2}+\lambda_{j}^{2}\right) \sigma_{i j}=\sum_{i<j}\left(\lambda_{i}+\lambda_{j}\right)^{2} \sigma_{i j} \leq 0,$$
since $\sigma_{i j} \leq 0$, and the inequality is proved.
Now we will analyze the equality case in dimension four. If equality occurs, then, choosing $(i, j, k, l)$ as a permutation of (1,2,3,4), we get
$$\begin{aligned}
0 & =\sum_{i, j=1}^{4}\left(\lambda_{i}+\lambda_{j}\right)^{2} \sigma_{i j}=\sum_{i, j=1}^{4}\left(\mu_{i}+\mu_{j}-\frac{1}{2} R\right)^{2} \sigma_{i j} \\
& =\sum_{i, j=1}^{4}\left(\frac{\mu_{i}+\mu_{j}}{2}-\frac{\mu_{k}+\mu_{l}}{2}\right)^{2} \sigma_{i j} \\
& =\sum_{i, j=1}^{4}\left(\sigma_{i j}-\sigma_{k l}\right)^{2} \sigma_{i j} \\
& =\left(\sigma_{12}-\sigma_{34}\right)^{2}\left(\sigma_{12}+\sigma_{34}\right)+\left(\sigma_{13}-\sigma_{24}\right)^{2}\left(\sigma_{13}+\sigma_{24}\right)+\left(\sigma_{14}-\sigma_{23}\right)^{2}\left(\sigma_{14}+\sigma_{23}\right) .
\end{aligned}$$
This implies that $\sigma_{12}=\sigma_{34}, \sigma_{13}=\sigma_{24}$ and $\sigma_{14}=\sigma_{23}$, since $g$ has non-positive sectional curvatures. Now, if we compute $\lambda_{1}$, we get
$$\lambda_{1}=\mu_{1}-\frac{1}{4} R=\sum_{j=2}^{4} \sigma_{1 j}-\frac{1}{2} \sum_{i<j} \sigma_{i j}=0 .$$
A similar argument shows that $\lambda_{i}=0$ for every $i$, so the metric must be Einstein. \(\square\)

Now we can prove Theorem 1.4. Let $M^{4}$ be a compact manifold of dimension four and $g$ be a critical metric for $\mathcal{F}_{t}$ on $\mathscr{M}_{1}\left(M^{4}\right)$ for some $t \geq-1 / 4$ with non-positive sectional curvature. By Corollary 2.3, we know that $g$ has constant scalar curvature. Moreover, since $g$ is critical, then, Corollary 6.7 implies that
$$\int|\nabla E|^{2} d V=2 \int\left(R_{i k j l} E_{i j} E_{k l}+\frac{1+4 t}{4} R|E|^{2}\right) d V \leq 2 \int R_{i k j l} E_{i j} E_{k l} d V,$$
since $R \leq 0$ and $t \geq 1 / 4$. Using Propositions 4.1, we obtain
$$\frac{1}{2} \int|C|^{2} d V \leq \int\left(R_{i k j l} E_{i j} E_{k l}+\frac{1}{n} R|E|^{2}+E_{i j} E_{i k} E_{j l}\right) d V .$$
From Proposition 4.2, it follows that the right hand side is non-positive, so it must be zero and the metric must be Einstein. This concludes the proof of Theorem 1.4.

\section*{5. Three dimensional critical metrics with positively pinched curvature}

In this section we will prove Theorem 1.5. Let $M^{3}$ be a closed manifold of dimension three and $g$ be a critical metric for $\mathcal{F}_{t}$ on $\mathscr{M}_{1}\left(M^{3}\right)$ for some $-1 / 3 \leq t<-1 / 6$. We will assume that $g$ has non-negative scalar curvature and it satisfies the piching condition
$$|E|^{2}<\frac{(1+6 t)^{2}}{24} R^{2} .$$
To prove that $g$ must be Einstein, i.e. a constant sectional curvature metric, one would like to follow the proof of Theorem 1.1. Unfortunately, it is easy to observe that, if $t>-1 / 2$, the left-hand side of the integral formula in Corollary 6.7 could be non-positive. This observation leads us to find a different strategy in order to deal with the gradient terms of the Euler-Lagrange equation. In dimension three, the Riemann curvature tensor decomposes as
$$R_{i k j l}=E_{i j} g_{k l}-E_{i l} g_{j k}+E_{k l} g_{i j}-E_{k j} g_{i l}+\frac{1}{6} R\left(g_{i j} g_{k l}-g_{i l} g_{j k}\right) .$$
Hence, the equation (6.4) for critical metrics reads
$$\frac{1}{2} \Delta|E|^{2}=|\nabla E|^{2}+(1+2 t) E_{i j} \nabla_{i j}^{2} R+4 E_{i j} E_{i k} E_{k j}-\frac{1+6 t}{3} R|E|^{2} .$$
Multiplying this latter with the scalar curvature $R$ and integrating by parts over $M^{3}$, we obtain
$$\begin{array}{r}
\left.\int\left(\left.\frac{1}{2}\langle\nabla| E\right|^{2}, \nabla R\right\rangle+R|\nabla E|^{2}-\frac{1+2 t}{6} R|\nabla R|^{2}-(1+2 t) E(\nabla R, \nabla R)\right) d V \\
=\int\left(\frac{1+6 t}{3} R^{2}|E|^{2}-4 R E_{i j} E_{i k} E_{k j}\right) d V
\end{array}$$
where we used the second Bianchi identity $\nabla_{i} E_{i j}=\nabla_{j} R / 6$. First of all we observe that, under the assumption of Theorem 1.5, the right-hand side is non-positive. In fact, since $E$ is a symmetric traceless two-tensor, then one has the following sharp inequality [6, Lemma 4.2]
$$\left|E_{i j} E_{i k} E_{k j}\right| \leq \frac{1}{\sqrt{6}}|E|^{3} .$$

Thus, since $R>0$, from the pinching assumption (5.1), we get
$$\frac{1+6 t}{3} R^{2}|E|^{2}-4 R E_{i j} E_{i k} E_{k j} \leq R|E|^{2}\left(\frac{1+6 t}{3} R-\frac{4}{\sqrt{6}}|E|\right) \leq 0 .$$
To conclude the proof, we have to estimate the left-hand side of equation (5.2). We have the following

Lemma 5.1. Under the assumption of Theorem 1.5, one has
$$\left.\int\left(\left.\frac{1}{2}\langle\nabla| E\right|^{2}, \nabla R\right\rangle+R|\nabla E|^{2}-\frac{1+2 t}{6} R|\nabla R|^{2}-(1+2 t) E(\nabla R, \nabla R)\right) d V \geq 0 .$$
Proof. From Bochner formula, one has
$$\begin{aligned}
\frac{1}{2} \Delta|\nabla R|^{2} & =\left|\nabla^{2} R\right|^{2}+\operatorname{Ric}(\nabla R, \nabla R)+\langle\nabla \Delta R, \nabla R\rangle \\
& =\left|\nabla^{2} R\right|^{2}+E(\nabla R, \nabla R)+\frac{1}{3} R|\nabla R|^{2}+\langle\nabla \Delta R, \nabla R\rangle .
\end{aligned}$$
Integrating by parts, we get
$$\begin{aligned}
\int E(\nabla R, \nabla R) d V & =-\int\left(\left|\nabla^{2} R\right|^{2}-|\Delta R|^{2}+\frac{1}{3} R|\nabla R|^{2}\right) d V \\
& \leq \int\left(\frac{2}{3}|\Delta R|^{2}-\frac{1}{3} R|\nabla R|^{2}\right) d V
\end{aligned}$$
where we have used the algebraic inequality $\left|\nabla^{2} R\right|^{2} \geq|\Delta R|^{2} / 3$. On the other hand, from the traced equation of critical metrics
$$\Delta R=-\frac{1}{3+8 t}\left(|\operatorname{Ric}|^{2}+t R^{2}-\lambda\right),$$
one has
$$\begin{aligned}
\int|\Delta R|^{2} d V & =\int R \Delta^{2} R d V=-\frac{1}{3+8 t} \int R \Delta|R i c|^{2} d V-\frac{t}{3+8 t} \int R \Delta R^{2} d V \\
& \left.=\int\left(\left.\frac{1}{3+8 t}\langle\nabla| R i c\right|^{2}, \nabla R\right\rangle+\frac{2 t}{3+8 t} R|\nabla R|^{2}\right) d V \\
& \left.=\int\left(\left.\frac{1}{3+8 t}\langle\nabla| E\right|^{2}, \nabla R\right\rangle+\frac{2+6 t}{3(3+8 t)} R|\nabla R|^{2}\right) d V .
\end{aligned}$$
Putting all together, we have showed that
$$\left.\int E(\nabla R, \nabla R) d V \leq \int\left(\left.\frac{2}{3(3+8 t)}\langle\nabla| E\right|^{2}, \nabla R\right\rangle-\frac{5+12 t}{9(3+8 t)} R|\nabla R|^{2}\right) d V .$$
We are now in the position to prove the lemma. We want to estimate the following quantity
$$\left.\int\left(\left.\frac{1}{2}\langle\nabla| E\right|^{2}, \nabla R\right\rangle+R|\nabla E|^{2}-\frac{1+2 t}{6} R|\nabla R|^{2}-(1+2 t) E(\nabla R, \nabla R)\right) d V .$$
Since $t \geq-1 / 3$, from the previous inequality, we obtain
$$\begin{gathered}
\left.\int\left(\left.\frac{1}{2}\langle\nabla| E\right|^{2}, \nabla R\right\rangle+R|\nabla E|^{2}-\frac{1+2 t}{6} R|\nabla R|^{2}-(1+2 t) E(\nabla R, \nabla R)\right) d V \\
\left.\quad \geq \int\left(\left.\frac{5+16 t}{6(3+8 t)}\langle\nabla| E\right|^{2}, \nabla R\right\rangle+R|\nabla E|^{2}+\frac{1+2 t}{18(3+8 t)} R|\nabla R|^{2}\right) d V .
\end{gathered}$$
Now, since $R>0$, then from Cauchy-Schwartz and Kato inequalities, we have
$$\begin{aligned}
\left.\left.\frac{5+16 t}{6(3+8 t)}\langle\nabla| E\right|^{2}, \nabla R\right\rangle & \geq-\frac{|5+16 t|}{3(3+8 t)}|E||\nabla E||\nabla R| \\
& \geq-\frac{|5+16 t|}{3(3+8 t)} \varepsilon R|\nabla R|^{2}-\frac{|5+16 t|}{12(3+8 t) \varepsilon} \frac{|E|^{2}}{R}|\nabla E|^{2},
\end{aligned}$$
for every $\varepsilon>0$. Choosing $\varepsilon=(1+2 t) /(6|5+16 t|)$, we have
$$\left.\left.\frac{5+16 t}{6(3+8 t)}\langle\nabla| E\right|^{2}, \nabla R\right\rangle \geq-\frac{1+2 t}{18(3+8 t)} R|\nabla R|^{2}-\frac{(5+16 t)^{2}}{2(1+2 t)(3+8 t)} \frac{|E|^{2}}{R}|\nabla E|^{2} .$$
Hence, the integrand we want to estimate is bounded by
$$\left.\left.\frac{5+16 t}{6(3+8 t)}\langle\nabla| E\right|^{2}, \nabla R\right\rangle+R|\nabla E|^{2}+\frac{1+2 t}{18(3+8 t)} R|\nabla R|^{2} \geq \frac{|\nabla E|^{2}}{R}\left(R^{2}-\frac{(5+16 t)^{2}}{2(1+2 t)(3+8 t)}|E|^{2}\right) .$$
Finally, using the pinching assumption (5.1), it is easy to prove that the right-hand side is non-negative, since
$$\frac{(1+6 t)^{2}}{24} \leq \frac{2(1+2 t)(3+8 t)}{(5+16 t)^{2}},$$
if $-1 / 3 \leq t<-1 / 6$. This concludes the proof of the lemma. \(\square\)

Combining this latter with equation (5.2) and inequality (5.3), under the assumption of Theorem 1.5, we have showed that
$$\int R|E|^{2}\left(\frac{1+6 t}{3} R-\frac{4}{\sqrt{6}}|E|\right) d V=0 .$$
Hence, $E \equiv 0$ on $M^{3}$ since $R>0$ and the pinching assumption (5.1) holds.
This concludes the proof of Theorem 1.5.

\section*{6. The Euler-Lagrange equation for $\mathcal{F}_{t, s}$}

In this section we will compute the Euler-Lagrange equation satisfied by critical metrics for
$$\mathcal{F}_{t, s}(g)=\int|\operatorname{Ric}|^{2} d V+t \int R^{2} d V+s \int|R m|^{2} d V$$
on $\mathscr{M}_{1}\left(M^{n}\right)$. As we have already observed in the introduction, this functional substantially differs from $\mathcal{F}_{t}$ only in dimension greater than four.

To compute the Euler-Lagrange equation for $\mathcal{F}_{t, s}$, we follow the computations in Section 2. The gradients of the functionals $\rho, \mathcal{S}$ and $\mathcal{R}$ are given by (see [4, Proposition 4.66] and [4, Proposition 4.70])
$$(\nabla \rho)_{i j}=-\Delta R_{i j}+\nabla_{i j}^{2} R-\frac{1}{2}(\Delta R) g_{i j}-2 R_{i k j l} R_{k l}+\frac{1}{2}|R i c|^{2} g_{i j},$$
$$(\nabla \mathcal{S})_{i j}=2 \nabla_{i j}^{2} R-2(\Delta R) g_{i j}-2 R R_{i j}+\frac{1}{2} R^{2} g_{i j},$$
and
$$(\nabla \mathcal{R})_{i j}=-4 \Delta R_{i j}+2 \nabla_{i j}^{2} R-2 R_{i k p q} R_{j k p q}+\frac{1}{2}|R m|^{2} g_{i j}-4 R_{i k j l} R_{k l}+4 R_{i k} R_{j k} .$$
Hence, the gradient of $\mathcal{F}_{t, s}$ reads
$$\begin{aligned}
\left(\nabla \mathcal{F}_{t, s}\right)_{i j}= & -(1+4 s) \Delta R_{i j}+(1+2 t+2 s) \nabla_{i j}^{2} R-\frac{1+4 t}{2}(\Delta R) g_{i j}-2 R_{i k j l} R_{k l}-2 t R R_{i j} \\
& +\frac{1}{2}\left(|R i c|^{2}+t R^{2}+s|R m|^{2}\right) g_{i j}-2 s R_{i k p q} R_{j k p q}-4 s R_{i k j l} R_{k l}+4 s R_{i k} R_{j k} .
\end{aligned}$$
Moreover, $g$ is critical for $\mathcal{F}_{t, s}$ on $\mathscr{M}_{1}\left(M^{n}\right)$ if and only if $\left(\nabla \mathcal{F}_{t, s}\right)=c g$, for some $c \in \mathbb{R}$. Tracing this equation, we obtain
$$\frac{n-4}{2}\left(|R i c|^{2}+t R^{2}+s|R m|^{2}\right)-\frac{n+4(n-1) t+4 s}{2} \Delta R=n c .$$
From these, we get that $g$ is critical for $\mathcal{F}_{t, s}$ on $\mathscr{M}_{1}\left(M^{n}\right)$ if and only if
$$\begin{aligned}
& -(1+4 s) \Delta R_{i j}+(1+2 t+2 s) \nabla_{i j}^{2} R-\frac{2 t-2 s}{n}(\Delta R) g_{i j}+\frac{2}{n}\left(|R i c|^{2}+t R^{2}+s|R m|^{2}\right) g_{i j}+ \\
& \quad-2(1+2 s) R_{i k j l} R_{k l}-2 t R R_{i j}-2 s R_{i k p q} R_{j k p q}+4 s R_{i k} R_{j k}=0,
\end{aligned}$$
coupled with the scalar equation
$$(n+4(n-1) t+4 s) \Delta R=(n-4)\left(|R i c|^{2}+t R^{2}+s|R m|^{2}-\lambda\right),$$
where $\lambda=\mathcal{F}_{t, s}(g)$. Substituting $E_{i j}=R_{i j}-\frac{1}{n} R g_{i j}$, we obtain the Euler-Lagrange equation of critical metrics for $\mathcal{F}_{t, s}$ on $\mathscr{M}_{1}\left(M^{n}\right)$.

Proposition 6.1. Let $M^{n}$ be a closed manifold of dimension $n \geq 3$. A metric $g$ is critical for $\mathcal{F}_{t, s}$ on $\mathscr{M}_{1}\left(M^{n}\right)$ if and only if it satisfies the following equations
$$\begin{aligned}
(1+4 s) \Delta E_{i j}= & (1+2 t+2 s) \nabla_{i j}^{2} R-\frac{1+2 t+2 s}{n}(\Delta R) g_{i j}-2(1+2 s) R_{i k j l} E_{k l} \\
& -\frac{2+2 n t-4 s}{n} R E_{i j}+\frac{2}{n}\left(|E|^{2}+s|R m|^{2}\right) g_{i j}-2 s R_{i k p q} R_{j k p q}+4 s E_{i k} E_{j k},
\end{aligned}$$
$$(n+4(n-1) t+4 s) \Delta R=(n-4)\left(|\operatorname{Ric}|^{2}+t R^{2}+s|R m|^{2}-\lambda\right),$$
where $\lambda=\mathcal{F}_{t, s}(g)$.
In particular, any Einstein critical metric must satisfy the following pointwise condition (see also [4, Corollary 4.67])

Corollary 6.2. An Einstein metric is critical for $\mathcal{F}_{t, s}$ on $\mathscr{M}_{1}\left(M^{n}\right)$ if and only if it satisfies
$$R_{i k p q} R_{j k p q}=\frac{1}{n}|R m|^{2} g_{i j} .$$

Corollary 6.3. Any space form metric is critical for $\mathcal{F}_{t, s}$ on $\mathscr{M}_{1}\left(M^{n}\right)$.

In the case $n \neq 4$ and
$$s=-\frac{n+4(n-1) t}{4}$$
one has the constancy of the following quantity
$$|R i c|^{2}+t R^{2}-\frac{n+4(n-1) t}{4}|R m|^{2} .$$
Since the norm of the Riemann curvature tensor is given by
$$|R m|^{2}=|W|^{2}+\frac{4}{n-2}|R i c|^{2}-\frac{2}{(n-1)(n-2)} R^{2},$$
we obtain the following
Corollary 6.4. Let $M^{n}$ be a closed manifold of dimension $n>4$. If $g$ is a critical metric $g$ for $\mathcal{F}_{t,-\frac{n+4(n-1) t}{4}}$ on $\mathscr{M}_{1}\left(M^{n}\right)$, then the quantity
$$-\frac{n+4(n-1) t}{4}|W|^{2}+4(n-2)(1+2(n-1) t) \sigma_{2}(A)$$
is constant on $M^{n}$.
Moreover, we notice that, when $t=s=-1 / 4$, Corollary 6.4 applies, In this case, the integrand of the curvature functional $\mathcal{F}_{-\frac{1}{4},-\frac{1}{4}}$ vanishes if $n=3$ and it corresponds (in fact, it is proportional) to the Gauss-Bonnet integrand if $n=4$. Furthermore, it follows from equation (6.2) that all the second order terms in the Euler-Lagrange equation vanish. More precisely, one has the following remarkable fact, which, in part, was already observed by Berger in [3, Section 7] (see also [12]).

Corollary 6.5. Let $M^{n}$ be a closed manifold of dimension $n>4$. A metric $g$ is critical for $\mathcal{F}_{-\frac{1}{4},-\frac{1}{4}}$ on $\mathscr{M}_{1}\left(M^{n}\right)$ if and only if it satisfies the following equation.
$$-R_{i k j l} E_{k l}+\frac{n-6}{2 n} R E_{i j}+\frac{1}{2 n}\left(4|E|^{2}-|R m|^{2}\right) g_{i j}+\frac{1}{2} R_{i k p q} R_{j k p q}-E_{i k} E_{j k}=0 .$$
Moreover, the quantity
$$|W|^{2}+2(n-2)(n-3) \sigma_{2}(A)$$
is constant on $M^{n}$.
As already suggested by Berger, it will be interesting to have a complete classification of these critical metrics. For the sake of completeness, we compute the pointwise and integral Weitzenböck formulas of critical metrics for $\mathcal{F}_{t, s}$.

Proposition 6.6. Let $M^{n}$ be a closed manifold of dimension $n>4$. If $g$ is a critical metric $g$ for $\mathcal{F}_{t}$ on $\mathscr{M}_{1}\left(M^{n}\right)$, then the following formula holds
$$\begin{aligned}
\frac{1+4 s}{2} \Delta|E|^{2}= & (1+4 s)|\nabla E|^{2}+(1+2 t+2 s) E_{i j} \nabla_{i j}^{2} R-2(1+2 s) R_{i k j l} E_{i j} E_{k l} \\
& -\frac{2+2 n t-4 s}{n} R|E|^{2}-2 s E_{i j} R_{i k p q} R_{j k p q}+4 s E_{i j} E_{i k} E_{j k} .
\end{aligned}$$

Integrating by parts and using second Bianchi identity, we obtain

Corollary 6.7. Let $M^{n}$ be a closed manifold of dimension $n>4$. If $g$ is a critical metric for $\mathcal{F}_{t, s}$ on $\mathscr{M}_{1}\left(M^{n}\right)$, then
$$\begin{aligned}
& \int\left((1+4 s)|\nabla E|^{2}-\frac{(n-2)(1+2 t+2 s)}{2 n}|\nabla R|^{2}\right) d V= \\
& 2 \int\left((1+2 s) R_{i k j l} E_{i j} E_{k l}+\frac{1+n t-2 s}{n} R|E|^{2}+s E_{i j} R_{i k p q} R_{j k p q}-2 s E_{i j} E_{i k} E_{j k}\right) d V .
\end{aligned}$$
In particular, if $g$ is a critical metric for $\mathcal{F}_{t,-\frac{n+4(n-1) t}{4}}$ on $\mathscr{M}_{1}\left(M^{n}\right)$, then
$$\begin{aligned}
& -(n-1)(1+4 t) \int\left(|\nabla E|^{2}-\frac{(n-2)^{2}}{4 n(n-1)}|\nabla R|^{2}\right) d V= \\
& 2 \int\left(-\frac{n-2+4(n-1) t}{2} R_{i k j l} E_{i j} E_{k l}+\frac{n+2+2(3 n-2) t}{2 n} R|E|^{2}+\right. \\
& \left.-\frac{n+4(n-1) t}{4} E_{i j} R_{i k p q} R_{j k p q}+\frac{n+4(n-1) t}{2} E_{i j} E_{i k} E_{j k}\right) d V .
\end{aligned}$$

Acknowledgments. The author is members of the Gruppo Nazionale per l'Analisi Matematica, la Probabilità e le loro Applicazioni (GNAMPA) of the Istituto Nazionale di Alta Matematica (INdAM).

\section*{References}
\begin{itemize}
\item[1.] M. T. Anderson, Extrema of curvature functionals on the space of metrics on 3-manifolds, Calc. Var. Partial Differential Equations 5 (1997), no. 3, 199-269.
\item[2.] \_\_\_\_, Extrema of curvature functionals on the space of metrics on 3-manifolds. II, Calc. Var. Partial Differential Equations 12 (2001), no. 1, 1-58.
\item[3.] M. Berger, Quelques formules de variation pour une structure riemannienne, Ann. Sci. École Norm. Sup. (4) 3 (1970), 285-294.
\item[4.] A. L. Besse, Einstein manifolds, Springer-Verlag, Berlin, 2008.
\item[5.] G. Catino, Critical metric of the $L^{2}$-norm of the scalar curvature, arXiv preprint server - http://arxiv.org, to appear on Proc. Amer. Math. Soc., 2012.
\item[6.] M. J. Gursky and J. A. Viaclovsky, A new variational characterization of three-dimensional space forms, Invent. Math. 145 (2001), no. 2, 251-278.
\item[7.] \_\_\_\_, Rigidity and stability of Einstein metrics for quadratic curvature functionals, arXiv preprint server - http://arxiv.org, to appear on J. Reine Angew. Math., 2011.
\item[8.] \_\_\_\_, Critical metrics on connected sums of Einstein four-manifolds, arXiv preprint server - http://arxiv.org, 2013.
\item[9.] D. Hilbert, Die Grundlagen der Physik, Ann. Sci. École Norm. Sup. (4) (1915), 461-472.
\item[10.] Z. Hu and H. Li, A new variational characterization of n-dimensional space forms, Trans. Amer. Math. Soc. 356 (2003), no. 8, 3005-3023.
\item[11.] Z. Hu, S. Nishikawa, and U. Simon, Critical metrics of the Schouten functional, J. Geom. 98 (2010), no. 1-2, 91-113.
\item[12.] M.-L. Labbi, Variational properties of the Gauss-Bonnet curvatures, Calc. Var. Partial Differential Equations 32 (2008), no. 2, 175-189.
\item[13.] F. Lamontagne, Une remarque sur la norme $L^{2}$ du tenseur de courbure, C. R. Acad. Sci. Paris Sér. I Math. 319 (1994), no. 3, 237-240.
\end{itemize}
14. \_\_\_\_, A critical metric for the $L^{2}$-norm of the curvature tensor on $S^{3}$, Proc. Amer. Math. Soc. 126 (1998), no. 2, 589-593.
15. N. K. Smolentsev, Spaces of Riemannian metrics, J. Math. Sci. 142 (2007), no. 5, 2436-2519.
16. S. Tanno, Deformations of Riemannian metrics on 3-dimensional manifolds, Tôhoku Math. J. (2) 27 (1975), no. 3, 437-444.
17. J. A. Viaclovsky, Conformal geometry, contact geometry, and the calcu- lus of variations, Duke Math. J. 101 (2000), no. 2, 283-316.
18. \_\_\_\_, The mass of the product of spheres, arXiv preprint server - http://arxiv.org, 2013.
(Giovanni Catino) Dipartimento di Matematica, Politecnico di Milano, Piazza Leonardo da Vinci 32, 20133 Milano, Italy
E-mail address: giovanni.catino@polimi.it