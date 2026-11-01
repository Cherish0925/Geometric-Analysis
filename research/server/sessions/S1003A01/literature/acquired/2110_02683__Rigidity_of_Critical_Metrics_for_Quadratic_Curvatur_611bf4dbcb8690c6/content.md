---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 2110_02683.pdf
converter: mathpix
format: mmd
---

\title{
RIGIDITY OF CRITICAL METRICS FOR QUADRATIC CURVATURE FUNCTIONALS
}

\author{
GIOVANNI CATINO, PAOLO MASTROLIA, AND DARIO D. MONTICELLI
}

\begin{abstract}
In this paper we prove new rigidity results for complete, possibly non-compact, critical metrics of the quadratic curvature functionals $\mathfrak{F}_{t}^{2}=\int\left|\operatorname{Ric}_{g}\right|^{2} d V_{g}+t \int R_{g}^{2} d V_{g}$, $t \in \mathbb{R}$, and $\mathfrak{S}^{2}=\int R_{g}^{2} d V_{g}$. We show that (i) flat surfaces are the only critical points of $\mathfrak{S}^{2}$, (ii) flat three-dimensional manifolds are the only critical points of $\mathfrak{F}_{t}^{2}$ for every $t>-\frac{1}{3}$, (iii) three-dimensional scalar flat manifolds are the only critical points of $\mathfrak{S}^{2}$ with finite energy and (iv) $n$-dimensional, $n>4$, scalar flat manifolds are the only critical points of $\mathfrak{S}^{2}$ with finite energy and scalar curvature bounded below. In case (i), our proof relies on rigidity results for conformal vector fields and an ODE argument; in case (ii) we draw upon some ideas of M. T. Anderson concerning regularity, convergence and rigidity of critical metrics; in cases (iii) and (iv) the proofs are self-contained and depend on new pointwise and integral estimates.
\end{abstract}

Key Words: Quadratic functionals, critical metrics, rigidity results
AMS subject classification: 53C21, 53C24, 53C25

\section*{1. Introduction}

It is a natural problem in Riemannian geometry to study canonical metrics arising as solutions of the Euler-Lagrange equations for curvature functionals. In [3], Berger commenced the study of Riemannian functionals which are quadratic in the curvature (see [4, Chapter 4] and [21], [10] for surveys). To fix the notation, let $M^{n}, n \geq 2$, be a $n$-dimensional smooth manifold without boundary. Given a Riemannian metric $g$ on $M^{n}$, we denote with $\operatorname{Riem}_{\mathrm{g}}, W_{g}, \operatorname{Ric}_{g}$ and $R_{g}$, respectively, the Riemann curvature tensor, the Weyl tensor, the Ricci tensor and the scalar curvature. Then a basis for the space of quadratic curvature functionals, defined on the space of smooth metrics on $M^{n}$, is given by
$$\mathfrak{W}^{2}=\int\left|W_{g}\right|^{2} d V_{g}, \quad \mathfrak{r}^{2}=\int\left|\operatorname{Ric}_{g}\right|^{2} d V_{g}, \quad \mathfrak{S}^{2}=\int R_{g}^{2} d V_{g} .$$
It is well known that the only quadratic functional in the case $n=2$ is given by $\mathfrak{S}^{2}$, while in dimension $n=3$ one only has $\mathfrak{S}^{2}$ and $\mathfrak{r}^{2}$. From the standard decomposition of the Riemann tensor, for every $n \geq 4$, one has
$$\Re^{2}=\int\left|\operatorname{Riem}_{\mathrm{g}}\right|^{2} d V_{g}=\int\left(\left|W_{g}\right|^{2}+\frac{4}{n-2}\left|\operatorname{Ric}_{g}\right|^{2}-\frac{2}{(n-1)(n-2)} R_{g}^{2}\right) d V_{g} .$$

\footnotetext{
Date: October 7, 2021.
}

All such functionals, which also arise naturally as total actions in certain gravitational fields theories in physics, have been deeply studied in the last years by many authors; they are also of great interest in the Kähler framework: in this case, restricting to metrics in a given cohomology class, it is possible to show that each one of the three basis functionals can be expressed affinely by any one of them (see the discussion in [4, Chapter 11.E.]).

In this paper we focus our attention on rigidity results for critical metrics of quadratic curvature functionals which do not depend on $\mathfrak{W}^{2}$, i.e. we will consider
$$\mathfrak{F}_{t}^{2}=\int\left|\operatorname{Ric}_{g}\right|^{2} d V_{g}+t \int R_{g}^{2} d V_{g},$$
defined for some $t \in \mathbb{R} \cup\{+\infty\}$, the case $t=+\infty$ formally corresponding to the functional $\mathfrak{S}^{2}$.

Using variations with compact support, one finds that the Euler-Lagrange equation for a critical metric of $\mathfrak{F}_{t}^{2}$ reads, in local coordinates, as
$$-\Delta R_{i j}+(1+2 t) \nabla_{i j}^{2} R_{g}-\frac{1+4 t}{2}\left(\Delta R_{g}\right) g_{i j}+\frac{1}{2}\left(\left|\operatorname{Ric}_{g}\right|^{2}+t R_{g}^{2}\right) g_{i j}-2 R_{i k j l} R_{k l}-2 t R_{g} R_{i j}=0,$$
which upon tracing yields
$$(n+4(n-1) t) \Delta R_{g}=(n-4)\left(\left|\operatorname{Ric}_{g}\right|^{2}+t R_{g}^{2}\right) .$$
In particular for $\mathfrak{S}^{2}$ we obtain
$$\begin{gathered}
R_{g} \operatorname{Ric}_{g}-\nabla^{2} R_{g}=\frac{3}{4(n-1)} R_{g}^{2} g, \\
\Delta R_{g}=\frac{n-4}{4(n-1)} R_{g}^{2},
\end{gathered}$$
It is clear that for $n=2$ and $n=3$ one expects stronger results, since the systems of equations (1.1) and (1.3) govern the full curvature of the manifold. On the other hand, in dimensions $n \geq 4$ one would surmise that information on the full Riemann tensor might be needed, at least to study system (1.1).

Since in dimensions different from four $\mathfrak{F}_{t}^{2}$ is not scale-invariant, when $M^{n}$ is compact it is natural to restrict the functional on $\mathcal{M}_{1}\left(M^{n}\right)$, the space of equivalence classes of Riemannian metrics on $M^{n}$ having unit volume. Equivalently, one can consider a modified functional properly normalized with the volume of the manifold. It was already observed in [4] that every Einstein metric is critical for $\mathfrak{F}_{t}^{2}$ on $\mathcal{M}_{1}\left(M^{n}\right)$, for every $t \in \mathbb{R}$. The converse in general is false, of course. For instance, in dimension four, every Bach-flat metric is critical for $\mathfrak{F}_{-1 / 3}^{2}$ and every Weyl and scalar flat metric is critical for $\mathfrak{F}_{-1 / 4}^{2}$ on $\mathcal{M}_{1}\left(M^{4}\right)$ (see [4, Chapter 4]). Moreover, Lamontagne in [18] constructed a homogeneous non-Einstein critical metric for $\Re=4 \mathfrak{F}_{-1 / 4}^{2}$ on $\mathcal{M}_{1}\left(\mathbb{S}^{3}\right)$. This construction can be generalized to the case when $t>-\frac{1}{2}$, see [14, section 7]. Other examples of compact critical metrics were constructed by Gursky and Viaclovsky in [15], where they considered a manifold $M^{4}$ which is the connected sum of some Einstein manifolds and constructed critical
metrics for $\mathfrak{F}_{t}^{2}$ on $\mathcal{M}^{1}\left(M^{4}\right)$, for $t$ "close" to a given value depending on the topology of the Einstein building blocks. It is then natural to ask under which conditions a critical metric for $\mathfrak{F}_{t}^{2}$ must be Einstein. Typically, one assumes some curvature conditions (of pointwise or integral type, positivity or negativity of the curvature, etc.) on the critical metric, in order to prove rigidity properties; for results in this direction see e.g. [1, 16, 7, 17, 8, 5].

The problem of studying critical metrics for quadratic curvature functionals in the non-compact setting has on the other hand received much less attention. It is easy to see that all Ricci-flat metrics are critical points of the functional $\mathfrak{F}_{t}^{2}$ when $t \in \mathbb{R}$, which are also global minima of the functional when $t \in\left[-\frac{1}{n},+\infty\right)$; similarly, scalar-flat metrics are global minima for $\mathfrak{S}^{2}$, and hence are critical.

Anderson in [2] proved that every complete three-dimensional critical metric for the functional $\mathfrak{F}_{t}^{2}$ with non-negative scalar curvature is flat, if $t=0$ or $t=-\frac{1}{3}$. As an auxiliary result, in Lemma 4.3 we observe that the same techniques allow to extend the result to include the case $t \in\left(-\frac{1}{3},+\infty\right)$. In [7] the first author showed a characterization of complete critical metrics for $\mathfrak{S}^{2}$ with non-negative scalar curvature, in any dimension $n \geq 3$. On the other hand, in [11], we showed that, in dimension three, flat metrics are the only complete metrics with non-negative scalar curvature which are critical for the $\sigma_{2}$-curvature functional $\mathfrak{F}_{-3 / 8}^{2}$. All these results rely heavily on the sign condition on the scalar curvature. We observe that, to the best of our knowledge, the only example of a smooth critical metric for a functional $\mathfrak{F}_{t}^{2}$ was constructed by Gursky and Viaclovsky in [16] when $n=3$ and $t=-\frac{3}{8}$; this example has strictly negative scalar curvature, and we note for later reference that it does not belong to any $L^{q}$ space.

We now proceed to describe our results. As already observed, when $n=2$ the only quadratic curvature functional is $\mathfrak{S}^{2}$; we then show that the only critical metrics for such functional are flat, without any further assumption. Indeed we have

Theorem 1.1. Let $\left(M^{2}, g\right)$ be a two-dimensional complete critical metric of $\mathfrak{S}^{2}$. Then $\left(M^{2}, g\right)$ is flat, and thus a global minimum of the functional.

The proof of this theorem relies on known results on gradient conformal solitons and on an ODE argument.

When $n=3$, we also prove the same result for critical metrics of the functional $\mathfrak{F}_{t}^{2}$, with $t \in\left(-\frac{1}{3},+\infty\right)$; hence we have

Theorem 1.2. Let $\left(M^{3}, g\right)$, be a three-dimensional complete critical metric of $\mathfrak{F}_{t}^{2}$ with
$$-\frac{1}{3}<t<+\infty .$$
Then $\left(M^{3}, g\right)$ is flat, and thus a global minimum of the functional.
For other values of $t$, in general this result may not hold, as the explicit example constructed by Gursky and Viaclovsky in [16] shows for $t=-\frac{3}{8}$. The proof of the theorem
follows essentially using arguments introduced by Anderson in [1, 2]. Notice that the result in Theorem 1.2 holds also for $t=-\frac{1}{3}$ under the additional assumption that the scalar curvature is non-negative, as it was shown by Anderson in [2].

We explicitly note that the rigidity results in Theorems 1.1 and 1.2 hold without any extra assumption on the manifold and its curvature.

For the case of the functional $\mathfrak{S}^{2}$ when $n=3$, which formally corresponds to $t=+\infty$, we need an integrability assumption on $R_{g}$. Indeed Anderson's techniques, which we used in the proof of Theorem 1.2, cannot be directly applied to this functional, as detailed in Remark 4.6.

Theorem 1.3. Let $\left(M^{3}, g\right)$, be a three-dimensional complete critical metric of $\mathfrak{S}^{2}$ with finite energy, i.e. $R_{g} \in L^{2}\left(M^{3}\right)$. Then $\left(M^{3}, g\right)$ is scalar flat, and thus a global minimum of the functional.
Remark 1.4. We actually prove a stronger result: let $\left(M^{3}, g\right)$ be a three-dimensional complete, non-compact, critical metric of $\mathfrak{S}^{2}$ with $R_{g} \in L^{q}\left(M^{3}\right)$ for some $q \in(1, \infty)$. Then $\left(M^{3}, g\right)$ is scalar flat, and thus a global minimum of the functional.

We explicitly note that here we do not assume any sign condition on the scalar curvature. In the compact case the result easily follows integrating the trace of the Euler-Lagrange equation of the functional. In the non-compact case the proof consists in two steps: first, using a test function argument, we show that under our hypotheses one must have that $R_{g} \geq 0$, then we conclude using a previous result for manifolds with non-negative scalar curvature by the first author, see [7].

In dimension $n=4$ the functionals $\mathfrak{F}_{t}^{2}$ and $\mathfrak{S}^{2}$ are scaling-invariant. In particular for $t=-\frac{1}{3}$ a metric is critical if and only if it is Bach-flat, and hence there are several well known examples of solutions in the literature, both in the compact and in the complete non-compact case, e.g. conformally Einstein metrics and (anti-)self-dual metrics. In particular, in [22] the authors study complete, non-compact Bach-flat metrics with finite energy. In case $t \neq-\frac{1}{3}$ or $t=+\infty$, from equations (1.2) and (1.4) one immediately sees that the metric has harmonic scalar curvature. In particular, in the compact case one has that $R_{g}$ must be constant. We note that examples of compact critical metrics of $\mathfrak{F}_{t}^{2}$ for some values of $t \neq-\frac{1}{3}$ which are not Einstein have been constructed in [15]. On the other hand, one can deduce from (1.3) that compact critical metrics of $\mathfrak{S}^{2}$ are Einstein. In the non-compact case a classical result of Yau [25] implies that a critical metric with $R_{g} \in L^{q}\left(M^{4}\right)$ for some $q \in(1,+\infty)$ must have constant scalar curvature; then $\left(M^{4}, g\right)$ is scalar flat or it has finite volume. Moreover from equation (1.3) one has that a critical metric for $\mathfrak{S}^{2}$ is either scalar flat or Einstein with negative curvature and finite volume.

Finally, in the case $n>4$, it is clear that one cannot hope to prove rigidity results for critical metrics of $\mathfrak{F}_{t}^{2}$ without assuming further conditions on the full curvature tensor of the metric. Therefore, we focus our attention on $\mathfrak{S}^{2}$ and we prove that all critical metrics are scalar flat, assuming that the scalar curvature is bounded below and that it satisfies an integrability condition.

Theorem 1.5. Let $\left(M^{n}, g\right), n>4$, be a complete critical metric of $\mathfrak{S}^{2}$ with finite energy, i.e. $R_{g} \in L^{2}\left(M^{n}\right)$, and with $R_{g}$ bounded from below on $M^{n}$. Then $\left(M^{n}, g\right)$ is scalar flat, and thus a global minimum of the functional.

Remark 1.6. Actually we prove a stronger result: there exists $q^{*}>2$ such that if $\left(M^{n}, g\right)$, $n>4$, is a complete critical metric of $\mathfrak{S}^{2}$ with $R_{g}$ bounded from below on $M^{n}$ and with $R_{g} \in L^{q}\left(M^{n}\right)$ for some $1<q<q^{*}$, then $\left(M^{n}, g\right)$ is scalar flat. See the proof of Theorem 1.5 and Remark 5.8.

We explicitly note that also in this case we do not assume any sign condition on $R_{g}$. The proof of the result does not rely on previous works on critical metrics for quadratic curvature functionals and is divided into three steps: first, using a test function argument, we show that under our assumptions $R_{g}$ must either vanish identically or be strictly negative on $M^{n}$; then we prove a gradient estimate for the function $R_{g}$, under the assumption that it is strictly negative on $M^{n}$, using the Omori-Yau maximum principle for the $f$-Laplace operator and the $f$-Laplacian comparison theorem for the function $f=-\log \left|R_{g}\right|$; the third and final step, which relies on the previous gradient estimate, consists in showing that the case $R_{g}<0$ on $M^{n}$ cannot occur, using another test function argument.

The rest of the paper is organized as follows: in Section 2 we derive the Euler-Lagrange equations associated to $\mathfrak{F}_{t}^{2}$ and to $\mathfrak{S}^{2}$, in any dimension; in Section 3 we consider the case $n=2$ and we prove Theorem 1.1; in Section 4 we study the case $n=3$ and we provide the proofs of Theorems 1.2 and 1.3 (including Remark 1.4); finally in Section 5 we consider the case when $n>4$ and we show Theorem 1.5 (including Remark 1.6).

Acknowledgments . The authors would like to thank Prof. M. T. Anderson for many helpful discussions.

The first and second authors are members of the GNSAGA, Gruppo Nazionale per le Strutture Algebriche, Geometriche e le loro Applicazioni of Indam. The third author is a member of GNAMPA, Gruppo Nazionale per l'Analisi Matematica, la Probabilità e le loro Applicazioni of Indam and has been partially supported by 2020 GNAMPA Project: Equazioni Ellittiche e Paraboliche in Analisi Geometrica.

\section*{2. Euler-Lagrange Equations}

From now on we will drop the subscript $g$ in the notation of geometric objects. In this section we will follow closely the presentation in [8] and [10].

We fix the index range $1 \leq i, j, \ldots \leq n$ and recall that the Einstein summation convention will be in force throughout. The standard decomposition of the (0, 4)-version of the

Riemann tensor is given by the formula
$$R_{i j k t}=W_{i j k t}+\frac{1}{n-2}\left(R_{i k} g_{j t}-R_{i t} g_{j k}+R_{j t} g_{i k}-R_{j k} g_{i t}\right)-\frac{R}{(n-1)(n-2)}\left(g_{i k} g_{j t}-g_{i t} g_{j k}\right),$$
where $g_{i j}, W_{i j k t}$ and $R_{i j}$ are the components, respectively, of the metric $g$, of the Weyl tensor W and of the Ricci tensor Ric, while $R$ is the scalar curvature. Note that $R_{i j}=$ $g^{k l} R_{i k j l}=R_{k i l j}$ and $R=g^{i j} R_{i j}$, where $g^{i j}$ are the components of the inverse of metric $g$, $g^{-1}$.

We consider the quadratic curvature functionals
$$\mathfrak{F}_{t}^{2}=\int|\operatorname{Ric}|^{2} d V+t \int R^{2} d V,$$
defined for some constant $t \in \mathbb{R}$ (with $t=+\infty$ formally corresponding to the functional $\mathfrak{S}$ ). Using formulas for the variations of the Ricci tensor and of the scalar curvature and integrating by parts (using compactly supported "directions" $h$ ), it is not difficult to show that the so-called gradients of the functionals $\mathfrak{r}^{2}$ and $\mathfrak{S}^{2}$ are given by (see also [4, Proposition 4.66])
$$\begin{gathered}
\left(\nabla \mathfrak{r}^{2}\right)_{i j}=-\Delta R_{i j}-2 R_{i k j l} R_{k l}+\nabla_{i j}^{2} R-\frac{1}{2}(\Delta R) g_{i j}+\frac{1}{2}|\operatorname{Ric}|^{2} g_{i j}, \\
\left(\nabla \mathfrak{S}^{2}\right)_{i j}=2 \nabla_{i j}^{2} R-2(\Delta R) g_{i j}-2 R R_{i j}+\frac{1}{2} R^{2} g_{i j} ;
\end{gathered}$$
hence, the gradient of $\mathfrak{F}_{t}^{2}$ reads
$$\left(\nabla \mathfrak{F}_{t}^{2}\right)_{i j}=-\Delta R_{i j}+(1+2 t) \nabla_{i j}^{2} R-\frac{1+4 t}{2}(\Delta R) g_{i j}+\frac{1}{2}\left(|\operatorname{Ric}|^{2}+t R^{2}\right) g_{i j}-2 R_{i k j l} R_{k l}-2 t R R_{i j},$$
and consequently the Euler-Lagrange equation for a critical metric of $\mathfrak{F}_{t}^{2}$ are given by
$$-\Delta R_{i j}+(1+2 t) \nabla_{i j}^{2} R-\frac{1+4 t}{2}(\Delta R) g_{i j}+\frac{1}{2}\left(|\operatorname{Ric}|^{2}+t R^{2}\right) g_{i j}-2 R_{i k j l} R_{k l}-2 t R R_{i j}=0 .$$
Tracing the equation $\left(\nabla \mathfrak{F}_{t}^{2}\right)=0$, we obtain
$$(n+4(n-1) t) \Delta R=(n-4)\left(|\operatorname{Ric}|^{2}+t R^{2}\right) .$$

Moreover, the Euler-Lagrange equation for a critical metric of $\mathfrak{S}^{2}$ is given by
$$2 R \text { Ric }-2 \nabla^{2} R+2 \Delta R g=\frac{1}{2} R^{2} g,$$
or, equivalently,
$$\begin{gathered}
R \text { Ric }-\nabla^{2} R=\frac{3}{4(n-1)} R^{2} g, \\
\Delta R=\frac{n-4}{4(n-1)} R^{2},
\end{gathered}$$
where equation (2.6) is just the trace of (2.5).

\section*{3. Critical surfaces}

Let $\left(M^{2}, g\right)$ be a two-dimensional complete critical metric of $\mathfrak{S}^{2}$. Since Ric $=\frac{1}{2} R g$, equation (2.5) reads
$$\nabla^{2} R=-\frac{1}{4} R^{2} g .$$
In particular $\left(M^{2}, g\right)$ is a special gradient conformal soliton with potential function $R$ and hence $\nabla R$ is a special conformal vector field. Complete Riemannian manifolds admitting a vector field $X$ satisfying
$$\mathcal{L}_{X} g=\lambda g$$
for some smooth function $\lambda$, were studied by many authors in the late 60's (see, for instance, the discussion in [13, 9]).

Proof of Theorem 1.1. First of all, if $M^{2}$ is compact, then the tracing equation (3.1) we get
$$\Delta R=-\frac{3}{4} R^{2},$$
thus, integrating over $M^{2}$ we get $R \equiv 0$ on $M^{2}$.
On the other hand, suppose that $M^{2}$ is non-compact and $g$ is not flat. By (3.1) the potential function $f:=R$ is non-constant. Let $\Sigma$ be a regular level set of the function $f: M^{2} \rightarrow \mathbb{R}$, i.e. $|\nabla f| \neq 0$ on $\Sigma$, which exists by Sard's Theorem (and the fact that $f$ is non-constant). Following [9] (see also [13]), one can easily show that, in a neighborhood $U$ of $\Sigma$ not containing any critical point of $f$, such potential function only depends on the signed distance $r$ to the hypersurface $\Sigma$. Moreover, the width of the neighborhood $U$ is uniform with respect to the points of $\Sigma$, namely we can assume $U=\left\{r_{*}<r<r^{*}\right\}$, for some maximal $r_{*} \in[-\infty, 0)$ and $r^{*} \in(0,+\infty]$. By the scalar invariance of equation (3.1), we can assume that $f^{\prime}(0)=1$, possibly changing the function $f$. Hence, in $U$, the metric can be written as
$$g=d r \otimes d r+f^{\prime}(r)^{2} g^{\Sigma},$$
where $g^{\Sigma}$ denotes the induced metric on the level set $\Sigma$. Since the hessian of $f$ is given by
$$\nabla^{2} f=f^{\prime \prime} d r \otimes d r+\left(f^{\prime}\right)^{2} f^{\prime \prime} g^{\Sigma},$$
from equation (3.1), we get that the potential function satisfies the following ODE
$$f^{\prime \prime}(r)=-\frac{1}{4}(f(r))^{2}, \quad r \in\left(r_{*}, r^{*}\right) .$$
It is then immediate to see that
$$\left(f^{\prime}(r)\right)^{2}+\frac{1}{6}(f(r))^{3}=\mathrm{const}, \quad r \in\left(r_{*}, r^{*}\right)$$
is a conserved quantity of the ODE (3.3). One can then carry out a standard phase-plane analysis and a qualitative study of the solutions of (3.3). Indeed one can rewrite (3.3) as a system
$$\left\{\begin{array}{l}
x^{\prime}=y \\
y^{\prime}=-\frac{1}{4} x^{2}
\end{array}\right.$$
with $f=x, f^{\prime}=y$, and note that by (3.4) all solutions must lie on level sets of the function $F(x, y)=y^{2}+\frac{1}{6} x^{3}$. Moreover one can estimate the maximal interval of existence of solutions of (3.3) by rewriting (3.4) as
$$\frac{d f}{\sqrt{c-\frac{1}{6} f^{3}}}= \pm d r$$
for $c \in \mathbb{R}$, and integrating. Then we see that all nontrivial solutions of the ODE can be divided into three families, according to their qualitative behavior.

Solutions in the first family are bounded above and have maximal domain that is a bounded open interval. If $f:\left(r_{*}, r^{*}\right) \rightarrow \mathbb{R}$ is one of these solutions, then
$$\lim _{r \rightarrow r_{*}} f(r)=\lim _{r \rightarrow r^{*}} f(r)=-\infty,$$
$f^{\prime}$ is strictly monotone decreasing with
$$\lim _{r \rightarrow r_{*}} f^{\prime}(r)=+\infty, \quad \lim _{r \rightarrow r^{*}} f^{\prime}(r)=-\infty,$$
$f$ has a unique critical point $r_{0}$ and $f\left(r_{0}\right)=\max f(r) \neq 0$.
Solutions in the second family are strictly negative and have maximal domain that is a half-line which is unbounded below, i.e. $r_{*}=-\infty$. If $f:\left(-\infty, r^{*}\right) \rightarrow \mathbb{R}$ is one of the solutions in this family, then
$$\lim _{r \rightarrow-\infty} f(r)=0, \quad \lim _{r \rightarrow r^{*}} f(r)=-\infty,$$
$f^{\prime}$ is strictly monotone decreasing with
$$\lim _{r \rightarrow-\infty} f^{\prime}(r)=0, \quad \lim _{r \rightarrow r^{*}} f^{\prime}(r)=-\infty$$
and $f$ has no critical points.
Finally, solutions of the third family are strictly negative and have maximal domain that is a half-line which is unbounded above, i.e. $r^{*}=+\infty$. If $f:\left(r_{*},+\infty\right) \rightarrow \mathbb{R}$ is one of these solutions, then
$$\lim _{r \rightarrow r_{*}} f(r)=-\infty, \quad \lim _{r \rightarrow+\infty} f(r)=0,$$
$f^{\prime}$ is strictly monotone decreasing with
$$\lim _{r \rightarrow r_{*}} f^{\prime}(r)=+\infty, \quad \lim _{r \rightarrow+\infty} f^{\prime}(r)=0$$
and $f$ also in this case has no critical points.
Now, if $f$ has no critical points, since $\left(M^{2}, g\right)$ is complete, non-compact, the width of the maximal neighborhood $U$ should be unbounded in both the negative and the positive direction of the signed distance $r$ (i.e. we should have $r_{*}=-\infty$ and $r^{*}=+\infty$ ). On the
other hand, if $f$ has only one critical point, since $\left(M^{2}, g\right)$ is complete, the width of the neighborhood $U$ should be unbounded in the positive or in the negative direction of the signed distance (i.e. we should have $r_{*}=-\infty$ or $r^{*}=+\infty$, while the other endpoint of the maximal domain should be finite). This is clearly in contradiction with the above qualitative study of the solutions of (3.3). Thus, we conclude that necessarily $f=R \equiv 0$ and $\left(M^{2}, g\right)$ is flat. \(\square\)

\section*{4. Dimension three}
4.1. Anderson's theory. On a three-dimensional manifold $M^{3}$ we consider the quadratic curvature functionals
$$\mathfrak{F}_{t}^{2}=\int|\operatorname{Ric}|^{2} d V+t \int R^{2} d V, \quad t \in \mathbb{R}$$
From Section 2 (see equation (2.3)), in dimension three, using $\mathrm{W}=0$ and the decomposition (2.1), we have
$$R_{i k j l} R_{k l}=\frac{3}{2} R R_{i j}+\left(|\operatorname{Ric}|^{2}-\frac{1}{2} R^{2}\right) g_{i j}-2 R_{i k} R_{k j} ;$$
thus, the Euler-Lagrange equation for a (smooth) critical metric of $\mathfrak{F}_{t}^{2}$ reads
$$-\Delta R_{i j}+(1+2 t) \nabla_{i j}^{2} R-\frac{1+4 t}{2}(\Delta R) g_{i j}-\frac{3}{2}|\operatorname{Ric}|^{2} g_{i j}+\frac{2+t}{2} R^{2} g_{i j}-(3+2 t) R R_{i j}+4 R_{i k} R_{k j}=0,$$
which upon tracing yields
$$(3+8 t) \Delta R=-\left(|\operatorname{Ric}|^{2}+t R^{2}\right) .$$
We will follow closely the theory developed by Anderson in [1]. We say that $g$ is a weak $L^{2,2}$ solution to the system (4.1)-(4.2) if, for every two-tensor $h \in L^{2,2}$ with compact support, we have
$$\int_{M}\left\langle\left(\nabla \mathfrak{F}_{t}^{2}\right)_{i j}, h_{i j}\right\rangle d V=\int_{M} \operatorname{tr}\left(\nabla \mathfrak{F}_{t}^{2}\right) \operatorname{tr}(h) d V=0,$$
where the $L^{2,2}$ topology on the space of metrics is given by the norm
$$\|h\|_{L^{2,2}}^{2}=\int_{M}\left(\left|\nabla^{2} h\right|^{2}+|\nabla h|^{2}+|h|^{2}\right) d V$$
(see [1, Section 1] for details). Of course here one must perform the appropriate (formal) integration by parts to obtain well defined integrals.

The proof of Theorem 1.2 is by contradiction: assuming a critical metric of $\mathfrak{F}_{t}^{2}$ is nonflat, one can construct another non-flat critical metric with bounded (Ricci) curvature. By the Omori-Yau maximum principle the solution has non-negative scalar curvature which in turn implies it must be flat, thus reaching a contradiction. The following lemmas are technical steps which are used for the proof of Theorem 1.2 and are extension of results
(regularity, blow-up argument and rigidity) proved by M. Anderson for specific values of the parameter $t$.

Lemma 4.1 ([1, Theorem 4.1, $t=-1 / 4]$ ). Let $t \neq-\frac{3}{8}, U$ be a domain in a three-dimensional manifold $M^{3}$ and suppose $g$ is a $L^{2,2}$ weak solution of the Euler-Lagrange equation $\nabla \mathfrak{F}_{t}^{2}=0$ on $U$, i.e. $g$ is an $L^{2,2}$ critical metric of $\mathfrak{F}_{t}^{2}$ on $U$. Then $g$ is smooth.

Proof (sketch). Due to the form of the system (4.1)-(4.2), the proof of this lemma is the same as in [1, Theorem 4.1] for the case $t=-1 / 4$ for every $t \in \mathbb{R}$ and $t \neq-\frac{3}{8}$. We note that, if $t=-\frac{3}{8}$, we cannot gain regularity from the traced equation (4.2) and the proof does not work. \(\square\)

Lemma 4.2 ([2, Lemma 2.1, $t=0$ ]). Let $\left(M^{3}, g\right)$ be a complete, non-flat, critical solution of $\mathfrak{F}_{t}^{2}$ for $t \neq-\frac{3}{8}$. Then there exists another complete, non-flat, critical solution of $\mathfrak{F}_{t}^{2}$, $\left(\bar{M}^{3}, \bar{g}\right)$, which has uniformly bounded curvature, i.e.
$$\left|\operatorname{Ric}_{\bar{g}}\right|_{\bar{g}} \leq 1 \quad \text { on } \bar{M}^{3} .$$
Proof (sketch). Given the local regularity result of Lemma 4.1, the proof of this lemma is exactly the same as in [2, Lemma 2.1] for the case $t=0$. \(\square\)

Lemma 4.3 ([2, Theorem 0.1, $t=0$ ]). Let $\left(M^{3}, g\right)$ be a complete critical solution of $\mathfrak{F}_{t}^{2}$ for
$$-\frac{1}{3}<t<+\infty$$
with non-negative scalar curvature. Then $\left(M^{3}, g\right)$ is flat.
Proof (sketch). The proof is (substantially) contained in [2]. The case $t=0$ is treated in full detail, whereas when $t=-\frac{1}{3}$ in [2, Proposition 5.4] the author highlights the differences between the two cases. An examination of the proof for the case $t=0$ (i.e. [2, Theorem 0.1]) shows that all the arguments remain valid also if $-\frac{1}{3}<t<+\infty$. First of all, from Lemma 4.1 and Lemma 4.2, local regularity of weak solutions and the possibility to use a solution with bounded curvature are guaranteed. The second important observation is that the traced equation (4.2) reads
$$(3+8 t) \Delta R=-\left(|\operatorname{Ric}|^{2}+t R^{2}\right)=-\left(|\operatorname{Ric}|^{2}+\frac{1+3 t}{3} R^{2}\right) \leq-\frac{1+3 t}{3} R^{2},$$
and therefore, if $t>-\frac{1}{3}$, all the proofs still work. Here $\stackrel{\circ}{\text { Ric }}=$ Ric $-\frac{1}{3} R g$. In particular, as observed also in the proof of [2, Proposition 5.4] for the case $t=-\frac{1}{3}$, the following two instances can be solved:
\begin{itemize}
\item[(i)] The passage from (2.7) to (2.8) in the proof of [2, Proposition 2.2]. In the general case, (2.7) and (2.8) should read as
$$\int \eta^{4}\left(|\operatorname{Ric}|^{2}+\frac{1+3 t}{3} R^{2}\right) \leq \mu \int \eta^{4} R^{2}+\mu^{-1} \int \eta^{2}\left(\eta^{\prime}\right)^{2}\left(H^{+}\right)^{2}+\mu^{-1} \int \eta^{2}\left(\eta^{\prime \prime}\right)^{2}$$
\end{itemize}
and
$$\int_{B(R)}\left(|\operatorname{Ric}|^{2}+\frac{1+3 t-3 \mu}{3} R^{2}\right) \leq c_{2} R^{-2} \int_{B(2 R)}\left(H^{+}\right)^{2}+c_{3} R^{-\varepsilon},$$
respectively. Therefore, if $t>-\frac{1}{3}$ and $\mu$ is sufficiently small, following the proof we obtain that $(N, g)$ satisfies
$$\stackrel{\circ}{\text { Ric }} \equiv R \equiv 0,$$
and therefore must be flat, as required.
\begin{itemize}
\item[(ii)] In the proof of [2, Lemma 2.9 (ii)], in our case, the condition $\Delta R\left(x_{i}\right) \rightarrow 0$ implies $|\operatorname{Ric}|\left(x_{i}\right) \rightarrow 0$ and also $R\left(x_{i}\right) \rightarrow 0$, since $t>-\frac{1}{3}$. Therefore the proof can be completed following the same steps.
\end{itemize} \(\square\)

Remark 4.4. The result is true also if $t=-1 / 3$ (see [2, Section 5.2]). Moreover, a similar result holds if $t=+\infty$, i.e. for critical solution of $\mathfrak{S}^{2}$, as it was shown in [7]. In this case $\left(M^{3}, g\right)$ must be scalar flat.

Proof of Theorem 1.2. Suppose that $\left(M^{3}, g\right)$ is a three-dimensional complete, non-flat, critical metric of $\mathfrak{F}_{t}^{2}$ with $-\frac{1}{3}<t<+\infty$. From Lemma 4.2 we can construct another complete, non-flat, critical solution of $\mathfrak{F}_{t}^{2},\left(\bar{M}^{3}, \bar{g}\right)$, which has uniformly bounded curvature, i.e.
$$\left|\operatorname{Ric}_{\bar{g}}\right|_{\bar{g}} \leq 1 \quad \text { on } \bar{M}^{3} .$$
In particular the Ricci curvature of $\bar{g}$ is bounded below. Therefore, we can apply the classical Omori-Yau maximum principle (see for instance [24]) to the scalar curvature of $\bar{g}$ which is bounded below and satisfies the differential inequality
$$(3+8 t) \Delta_{\bar{g}} R_{\bar{g}}=-\left(\left|\operatorname{Ric}_{\bar{g}}^{\circ}\right|_{\bar{g}}^{2}+\frac{1+3 t}{3} R_{\bar{g}}^{2}\right) \leq-\frac{1+3 t}{3} R_{\bar{g}}^{2},$$
obtaining
$$\inf _{\bar{M}} R_{\bar{g}} \geq 0 .$$
Lemma 4.3 applied to $\left(\bar{M}^{3}, \bar{g}\right)$ implies that $\left(\bar{M}^{3}, \bar{g}\right)$ must be flat, a contradiction. Therefore the critical solution $\left(M^{3}, g\right)$ is flat and Theorem 1.2 is proved. \(\square\)
4.2. Critical metrics of $\mathfrak{S}^{2}$. The proofs of Theorem 1.3 and Remark 1.4 rely upon an integral estimate for critical metrics of $\mathfrak{S}^{2}$, that we now prove in general dimension $n$. We recall that a complete Riemannian manifold $\left(M^{n}, g\right)$ is critical for $\mathfrak{S}^{2}$ if it satisfies (2.5) and (2.6), i. e.
$$R \operatorname{Ric}-\nabla^{2} R=\frac{3}{4(n-1)} R^{2} g .$$
and
$$\Delta R=\frac{n-4}{4(n-1)} R^{2} .$$

We have the following estimate:
Lemma 4.5. Let $\left(M^{n}, g\right)$ be a complete critical metric of $\mathfrak{S}^{2}$. Assume that there exists a point $O \in M^{n}$ such that $R(O)<0$ and, for $s>0$, define the open set
$$M_{s}^{-}=\left\{p \in M^{n} \mid R(p)<0\right\} \cap B_{s}(O),$$
where $B_{s}(O)$ is the geodesic ball of radius $s$ centered in $O$. Then, for every $0<s_{1}<s_{2}$ and every $\alpha>-1$, the following estimate holds:
$$\int_{M_{\overline{s_{1}}}^{-}}|\nabla R|^{2}|R|^{\alpha} d V_{g} \leq \frac{(n-4)}{2(n-1)(1+\alpha)} \int_{M_{s_{2}}^{-}}|R|^{\alpha+3} d V_{g}+\frac{4}{(1+\alpha)^{2}\left(s_{2}-s_{1}\right)^{2}} \int_{M_{s_{2}}^{-}}|R|^{\alpha+2} d V_{g} .$$
Proof. Let $\eta$ be a smooth cutoff function such that $\eta \equiv 1$ on $B_{s_{1}}(O), \eta \equiv 0$ on $B_{s_{2}}^{c}(O)$, $0 \leq \eta \leq 1$ on $M^{n}$ and $|\nabla \eta| \leq \frac{c}{s_{2}-s_{1}}, c>0$ independent of $s_{1}, s_{2}$. Integrating by parts one obtains
$$\begin{aligned}
\int_{M_{s_{2}}^{-}}|\nabla R|^{2}|R|^{\alpha} \eta^{2} d V_{g}= & \int_{M_{s_{2}}^{-}}\langle\nabla R, \nabla R\rangle(-R)^{\alpha} \eta^{2} d V_{g} \\
= & -\int_{M_{s_{2}}^{-}} R \Delta R(-R)^{\alpha} \eta^{2} d V_{g}-\alpha \int_{M_{s_{2}}^{-}}\langle\nabla R, \nabla R\rangle(-R)^{\alpha} \eta^{2} d V_{g} \\
& +2 \int_{M_{s_{2}}^{-}}\langle\nabla R, \nabla \eta\rangle(-R)^{\alpha+1} \eta d V_{g},
\end{aligned}$$
since the boundary terms vanish. Thus, from equation (2.6), we get
$$\begin{aligned}
\int_{M_{s_{2}}}|\nabla R|^{2}|R|^{\alpha} \eta^{2} d V_{g} & =-\frac{1}{1+\alpha} \int_{M_{s_{2}}^{-}} R \Delta R(-R)^{\alpha} \eta^{2} d V_{g}+\frac{2}{1+\alpha} \int_{M_{s_{2}}^{-}}\langle\nabla R, \nabla \eta\rangle|R|^{\alpha+1} \eta d V_{g} \\
& =\frac{n-4}{4(n-1)(1+\alpha)} \int_{M_{s_{2}}^{-}}|R|^{\alpha+3} \eta^{2} d V_{g}+\frac{2}{1+\alpha} \int_{M_{s_{2}}^{-}}\langle\nabla R, \nabla \eta\rangle|R|^{\alpha+1} \eta d V_{g}
\end{aligned}$$
On the other hand, Schwartz inequality implies
$$\frac{2}{1+\alpha} \int_{M_{s_{2}}^{-}}\langle\nabla R, \nabla \eta\rangle|R|^{\alpha+1} \eta d V_{g} \leq \frac{\varepsilon}{1+\alpha} \int_{M_{s_{2}}^{-}}|\nabla R|^{2}|R|^{\alpha} \eta^{2} d V_{g}+\frac{1}{\varepsilon(1+\alpha)} \int_{M_{s_{2}}^{-}}|R|^{\alpha+2}|\nabla \eta|^{2} d V_{g},$$
for every $\varepsilon>0$. Choosing $\varepsilon=(1+\alpha) / 2$ we get the result. \(\square\)

Proof of Theorem 1.3 and Remark 1.4. First of all, if $M^{3}$ is compact, then integrating (2.6) over $M^{3}$ we get $R \equiv 0$ on $M^{3}$.

On the other hand, suppose that $M^{3}$ is non-compact and let $1<q<\infty$. Using Lemma 4.5 with $n=3, s_{2}=2 s_{1}=2 s>0$ and $\alpha=q-2>-1$ we get
$$\int_{M_{s}^{-}}|\nabla R|^{2}|R|^{q-2} d V_{g} \leq \frac{4}{(q-1)^{2} s^{2}} \int_{M^{n}}|R|^{q} d V_{g} \longrightarrow 0 \quad \text { as } \quad s \rightarrow+\infty .$$

Hence we have that $\left(M^{3}, g\right)$ has non-negative scalar curvature. It follows from [7, Theorem $1.2]$ that $\left(M^{3}, g\right)$ has to be scalar flat, and Theorem 1.3 and Remark 1.4 in this case are proved. \(\square\)

Remark 4.6. We explicitly note that the strategy used in the proof of Theorem 1.2 cannot be applied in the case of critical metrics of $\mathfrak{S}^{2}$. More precisely, even if the rigidity result of Lemma 4.3 still holds (see Remark 4.4), the local regularity of $L^{2,2}$-weak solutions given by Lemma 4.1 could be proved (possibly with some effort, due to the presence of the boundary set $\Sigma=\{R=0\}$ ), and thus also the blow-up argument in Lemma 4.2 works, the contradiction in the proof of Theorem 1.2 cannot be achieved, since the solution $\left(\bar{M}^{3}, \bar{g}\right)$ must only be scalar flat.

\section*{5. Higher dimensions}

The aim of this section is to prove Theorem 1.5 and Remark 1.6. First of all, we show the following
Lemma 5.1. Let $\left(M^{n}, g\right), n>4$, be a complete, non-compact, critical metric of $\mathfrak{S}^{2}$ with $R \in L^{q}\left(M^{n}\right)$ for some $1<q<\infty$. Then ( $M^{n}, g$ ) has non-positive scalar curvature.
Proof. We prove this by contradiction. Assume that there exists a point $O \in M^{n}$ such that $R(O)>0$. For $s>0$, we define the open set
$$M_{s}^{+}=\left\{p \in M^{n} \mid R(p)>0\right\} \cap B_{s}(O),$$
where $B_{s}(O)$ is the geodesic ball of radius $s$ centered in $O$. Let $\eta$ be a smooth cutoff function such that $\eta \equiv 1$ on $B_{s}(O), \eta \equiv 0$ on $B_{2 s}^{c}(O), 0 \leq \eta \leq 1$ on $M^{n}$ and $|\nabla \eta| \leq \frac{c}{s}$, $c>0$ independent of $s$. From equation (2.6), an integration by part and an application of Young's inequality yield
$$\begin{aligned}
\int_{M_{2 s}^{+}} R^{q+1} \eta^{2} d V_{g}= & \frac{4(n-1)}{n-4} \int_{M_{2 s}^{+}} R^{q-1} \Delta R \eta^{2} d V_{g} \\
= & -\frac{4(n-1)(q-1)}{n-4} \int_{M_{2 s}^{+}}|\nabla R|^{2} R^{q-2} \eta^{2} d V_{g} \\
& -\frac{8(n-1)}{n-4} \int_{M_{2 s}^{+}}\langle\nabla R, \nabla \eta\rangle R^{q-1} \eta d V_{g} \\
\leq & \frac{4(n-1)}{(n-4)(q-1)} \int_{M_{2 s}^{+}} R^{q}|\nabla \eta|^{2} d V_{g} \\
\leq & \frac{4(n-1)}{(n-4)(q-1) s^{2}} \int_{M^{n}}|R|^{q} d V_{g} .
\end{aligned}$$
By letting $s \rightarrow+\infty$, we get that the set $M^{+}=\left\{p \in M^{n} \mid R(p)>0\right\}$ must have zero measure, so it must be empty: this is a contradiction, since $O \in M^{+}$. \(\square\)

Now, if $n>4$, then by (2.6) $R$ is subharmonic, therefore Lemma 5.1 and the strong maximum principle imply the following:

Corollary 5.2. Let $\left(M^{n}, g\right), n>4$, be a complete, non-compact critical metric of $\mathfrak{S}^{2}$ with $R \in L^{q}\left(M^{n}\right)$ for some $1<q<\infty$. Then ( $M^{n}, g$ ) is either scalar flat or it has negative scalar curvature.

From now on we will assume that $\left(M^{n}, g\right), n>4$, is a complete, non-compact, critical metric of $\mathfrak{S}^{2}$ with $R \in L^{q}\left(M^{n}\right)$ for some $1<q<\infty$ and with negative, bounded from below scalar curvature. Let $f=-\log (-R)$; one has
$$\nabla f=-\frac{\nabla R}{R} \quad \text { and } \quad \nabla^{2} f=-\frac{\nabla^{2} R}{R}+d f \otimes d f .$$
Hence, the structure equation (2.5) implies that the 1-Bakry-Emery Ricci tensor with potential function $f$, i.e. $\operatorname{Ric}_{f}^{1}=\operatorname{Ric}+\nabla^{2} f-d f \otimes d f$ (see e.g. [23]), satisfies
$$\operatorname{Ric}_{f}^{1}=-\frac{3}{4(n-1)} e^{-f} g .$$
We explicitly note that the (global) change of variable $f=-\log (-R)$, which is permitted by Corollary 5.2, allows to read a critical metric as a special Einstein-type manifold, in the sense of [12] (see also [10]). We now aim at proving gradient estimates for the function $f$, which satisfies the semilinear equation for the $f$-Laplacian
$$\Delta_{f} f=\Delta f-|\nabla f|^{2}=\frac{n-4}{4(n-1)} e^{-f}$$
that one obtains by tracing (5.1). It is well known that this kind of results for the standard, "unweighted" Laplacian can be obtained only assuming a lower bound on the Ricci tensor, which ensure, in particular, the validity of the Laplacian comparison and of the Omori-Yau maximum principle. Since $R$ is bounded from below (or, equivalently, $e^{-f}$ is bounded from above), we see that the "weighted" $\operatorname{Ric}_{f}^{1}$ tensor is bounded from below: this will allows us to obtain the following Lemmas 5.3 and 5.5.

Lemma 5.3. Let $\left(M^{n}, g\right), n>4$, be a complete, non-compact, critical metric of $\mathfrak{S}^{2}$ with negative, bounded from below scalar curvature. Then there exists a positive constant $C$, only depending on $n$ and the lower bound of the scalar curvature, such that, on $M^{n}$, there holds
$$|\nabla R|^{2} \leq C R^{2} .$$
Proof. Let $O \in M^{n}$ be some origin point, denote by $B_{s}$ the geodesic ball with radius $s>0$ centered in $O$ and let
$$Z_{s}^{2}:=\sup _{B_{s}} e^{-f} .$$
We will show that there exist three positive constants $c_{1}, c_{2}, c_{3}$, just depending on $n$, such that
$$|\nabla f|^{2}(p) \leq \frac{c_{1}}{s^{2}}+\left(\frac{c_{2}}{s}+c_{3} Z_{s}\right) Z_{s},$$
for every $s>0$ and every $p \in B_{s / 2}$. The global statement will follow by letting $s \rightarrow \infty$. Using (5.1), (5.2) and the Bochner formula applied to $f$ we get
$$\frac{1}{2} \Delta_{f}|\nabla f|^{2}=\left|\nabla^{2} f\right|^{2}+g\left(\nabla \Delta_{f} f, \nabla f\right)+\operatorname{Ric}_{f}^{1}(\nabla f, \nabla f)+|\nabla f|^{4} .$$
Now we use Newton inequalities and $\Delta f=\Delta_{f} f+|\nabla f|^{2}$ to obtain
$$\begin{aligned}
\frac{1}{2} \Delta_{f}|\nabla f|^{2} & =\left|\nabla^{2} f\right|^{2}-\frac{n-4}{4(n-1)} e^{-f}|\nabla f|^{2}-\frac{3}{4(n-1)} e^{-f}|\nabla f|^{2}+|\nabla f|^{4} \\
& =\left|\nabla^{2} f\right|^{2}-\frac{1}{4} e^{-f}|\nabla f|^{2}+|\nabla f|^{4} \\
& \geq \frac{1}{n}(\Delta f)^{2}-\frac{1}{4} e^{-f}|\nabla f|^{2}+|\nabla f|^{4} \\
& \geq\left(1+\frac{1}{n}\right)|\nabla f|^{4}-\frac{1}{4} e^{-f}|\nabla f|^{2},
\end{aligned}$$
and then we deduce
$$\Delta_{f}|\nabla f|^{2} \geq \frac{2 n+2}{n}|\nabla f|^{4}-\frac{1}{2} e^{-f}|\nabla f|^{2} .$$
We note that, on $B_{s}(O)$,
$$\operatorname{Ric}_{f}^{1}-\frac{3}{4(n-1)} e^{f} g \geq-\frac{3}{4(n-1)} Z_{s}^{2} g .$$
Now we proceed exactly as in Theorem 4 on [19]. We include here the details for the sake of completeness. Let $\rho(x):=\operatorname{dist}(O, x)$ : using the Calabi trick ([6] and [7] for details) we can suppose that $\rho$ is smooth and consider on $B_{s}(O)$ the function
$$F(x)=\left[s^{2}-\rho^{2}(x)\right]^{2}|\nabla f|^{2} .$$
If $|\nabla f| \equiv 0$ we have nothing to prove; if $|\nabla f| \not \equiv 0$, since $F \geq 0$ and $\left.F\right|_{\partial B(O, s)} \equiv 0$, there exists a point $x_{0} \in B(O, s)$ such that $F\left(x_{0}\right)=\frac{\max }{B_{s}(O)} F(x)>0$. At $x_{0}$ we then have
$$\begin{gathered}
\nabla F\left(x_{0}\right)=0, \\
\Delta_{f} F\left(x_{0}\right) \leq 0 .
\end{gathered}$$
A straightforward calculation shows that (5.7) is equivalent to
$$\frac{\nabla|\nabla f|^{2}}{|\nabla f|^{2}}=\frac{2 \nabla \rho^{2}}{s^{2}-\rho^{2}} \quad \text { at } x_{0},$$
while, using (5.9) condition (5.8) is equivalent to
$$0 \geq-2 \frac{\Delta_{f} \rho^{2}}{s^{2}-\rho^{2}}+\frac{\Delta_{f}|\nabla f|^{2}}{|\nabla f|^{2}}-24 \frac{\rho^{2}}{\left(s^{2}-\rho^{2}\right)^{2}} \quad \text { at } x_{0} .$$
From the $f$-Laplacian comparison theorem (see [20], [23]), on $B_{s}(O)$ we have
$$\Delta_{f} \rho^{2} \leq 2[(n+1)+n Y \rho],$$
where $Y^{2}:=\frac{3}{4 n(n-1)} Z_{s}^{2}$. Combining (5.5), (5.10) and (5.11) we find, at $x_{0}$,
$$0 \geq-4 \frac{[(n+1)+n Y \rho]}{s^{2}-\rho^{2}}+\frac{2 n+2}{n}|\nabla f|^{2}-\frac{1}{2} e^{-f}-24 \frac{\rho^{2}}{\left(s^{2}-\rho^{2}\right)^{2}},$$
which implies, multiplying through by $\left(s^{2}-\rho^{2}\right)^{2}$, that at $x_{0}$ we have
$$0 \geq-4[(n+1)+n Y \rho]\left(s^{2}-\rho^{2}\right)+\frac{2 n+2}{n} F-\frac{1}{2}\left(s^{2}-\rho^{2}\right)^{2} e^{-f}-24 \rho^{2} .$$
From this, claim (5.4) follows and this concludes the proof of the lemma. \(\square\)

Now we aim at improving the gradient estimate (5.3), and to obtain that under the same assumptions of Lemma 5.3 one has
$$|\nabla R|^{2} \leq C|R|^{3} \quad \text { on } M^{n}$$
for some positive constant $C$, only depending on $n$. We start with the following
Lemma 5.4. Let $\left(M^{n}, g\right)$ be $n$-dimensional Riemannian manifold and let $w \in C^{2}\left(M^{n}\right)$. Then, where $|\nabla w| \neq 0$, it holds
$$\left.\left|\nabla^{2} w\right|^{2} \geq \frac{1}{n-1}(\Delta w)^{2}-\left.\frac{1}{n-1} \frac{\Delta w}{|\nabla w|^{2}}\langle\nabla| \nabla w\right|^{2}, \nabla w\right\rangle .$$
Proof. Let $\left\{e_{1}, \ldots, e_{n}\right\}$ be a local orthonormal frame with $e_{1}=|\nabla w|^{-1} \nabla w$. Then
$$\begin{aligned}
\left|\nabla^{2} w\right|^{2} & \geq \sum_{i=2}^{n}\left(\nabla_{i i} w\right)^{2} \geq \frac{1}{n-1}\left(\sum_{i=2}^{n} \nabla_{i i} w\right)^{2}=\frac{1}{n-1}\left(\Delta w-\nabla_{11} w\right)^{2} \\
& \geq \frac{1}{n-1}(\Delta w)^{2}-\frac{2}{n-1} \Delta w \nabla_{11} w .
\end{aligned}$$
Now, noting that
$$\left.\nabla_{11} w=\nabla^{2} w\left(e_{1}, e_{1}\right)=\left.\frac{1}{2}|\nabla w|^{-2}\langle\nabla| \nabla w\right|^{2}, \nabla w\right\rangle,$$
we obtain the desired estimate. \(\square\)

We can now prove the following
Lemma 5.5. Let $\left(M^{n}, g\right), n>4$, be a complete, non-compact, critical metric of $\mathfrak{S}^{2}$ with negative, bounded from below scalar curvature. There exists a positive constant $C$, only depending on $n$, such that, on $M^{n}$, there holds
$$|\nabla R|^{2} \leq C|R|^{3} .$$

Proof. Let again $f=-\log (-R)$ and let $u=-R=e^{-f}$. By the Bochner formula, using (5.1), (5.2) and Lemma 5.4, we see that at those points of $M^{n}$ where $|\nabla f| \neq 0$ we have
$$\begin{aligned}
\frac{1}{2} \Delta_{f}|\nabla f|^{2}= & \left|\nabla^{2} f\right|^{2}+\left\langle\nabla \Delta_{f} f, \nabla f\right\rangle+\operatorname{Ric}_{f}^{1}(\nabla f, \nabla f)+|\nabla f|^{4} \\
\geq & \left.\frac{1}{n-1}(\Delta f)^{2}-\left.\frac{1}{n-1} \frac{\Delta f}{|\nabla f|^{2}}\langle\nabla| \nabla f\right|^{2}, \nabla f\right\rangle-\frac{3}{4(n-1)} u|\nabla f|^{2} \\
& +|\nabla f|^{4}-\frac{n-4}{4(n-1)} u|\nabla f|^{2} \\
= & \left.\frac{1}{n-1}\left(\frac{n-4}{4(n-1)} u+|\nabla f|^{2}\right)^{2}-\left.\frac{1}{n-1} \frac{\Delta f}{|\nabla f|^{2}}\langle\nabla| \nabla f\right|^{2}, \nabla f\right\rangle \\
& +|\nabla f|^{4}-\frac{1}{4} u|\nabla f|^{2} \\
= & \left.-\left.\frac{1}{n-1} \frac{\Delta f}{|\nabla f|^{2}}\langle\nabla| \nabla f\right|^{2}, \nabla f\right\rangle+\frac{(n-4)^{2}}{16(n-1)^{3}} u^{2}+\frac{n}{n-1}|\nabla f|^{4} \\
& -\frac{n^{2}-4 n+9}{4(n-1)^{2}} u|\nabla f|^{2}
\end{aligned}$$
Moreover
$$\frac{1}{2} \Delta_{f} u=-\frac{n-4}{8(n-1)} u^{2}+\frac{1}{2} u|\nabla f|^{2} .$$
Now let
$$v:=A u-|\nabla f|^{2},$$
where $A>0$ is a suitable constant to be chosen later. We claim that we can find $A>0$ such that $v \geq 0$ on $M$.

By the above calculations we have
$$\begin{aligned}
\frac{1}{2} \Delta_{f} v \leq & \left.-\frac{n-4}{8(n-1)} A u^{2}+\frac{A}{2} u|\nabla f|^{2}+\left.\frac{1}{n-1} \frac{\Delta f}{|\nabla f|^{2}}\langle\nabla| \nabla f\right|^{2}, \nabla f\right\rangle \\
& -\frac{(n-4)^{2}}{16(n-1)^{3}} u^{2}-\frac{n}{n-1}|\nabla f|^{4}+\frac{n^{2}-4 n+9}{4(n-1)^{2}} u|\nabla f|^{2}
\end{aligned}$$
By Lemma 5.3 we have that $v$ is bounded below. Since $u$ is bounded, by (5.1) we have that the 1-Bakry-Emery Ricci curvature, $\mathrm{Ric}_{f}^{1}$, is bounded below and hence the full Omori-Yau maximum principle holds for the operator $\Delta_{f}$, see e.g. [19] and references therein. Thus, there exists a sequence of points $\left\{x_{k}\right\}_{k} \subset M^{n}$ such that
$$v\left(x_{k}\right) \leq \inf v+\frac{1}{k}, \quad\left|\nabla v\left(x_{k}\right)\right| \leq \frac{1}{k}, \quad \Delta_{f} v\left(x_{k}\right) \geq-\frac{1}{k}, \quad \text { for all } k \in \mathbb{N} .$$

Since by Lemma 5.3 we have that $|\nabla f|$ is bounded, up to extracting a subsequence $\left\{y_{m}\right\}_{m} \subset\left\{x_{k}\right\}_{k}$ we can assume that
$$\lim _{m \rightarrow+\infty}\left|\nabla f\left(y_{m}\right)\right|=l,$$
with
$$v\left(y_{m}\right) \leq \inf v+o(1), \quad\left|\nabla v\left(y_{m}\right)\right| \leq o(1), \quad \Delta_{f} v\left(y_{m}\right) \geq-o(1), \quad \text { and } o(1)>0$$
as $m$ tends to $\infty$.
Then one has
$$A u\left(y_{m}\right)-\left|\nabla f\left(y_{m}\right)\right|^{2}=v\left(y_{m}\right) \leq \inf v+o(1)$$
as $m$ tends to $+\infty$. Since $u$ is positive on $M^{n}$, if $l=0$, passing to the limit as $m$ tends to $\infty$ in the above equation yields inf $v \geq 0$ (for any choice of $A>0$ ).

From now on we assume by contradiction that $l>0$, and without loss of generality that $\left|\nabla f\left(y_{m}\right)\right|>0$ for every $m \in \mathbb{N}$. Then, noting that
$$\nabla|\nabla f|^{2}=A \nabla u-\nabla v$$
and using (5.2), at $y_{m}$ we have
$$\begin{aligned}
\left.\left.\frac{1}{n-1} \frac{\Delta f}{|\nabla f|^{2}}\langle\nabla| \nabla f\right|^{2}, \nabla f\right\rangle & =\frac{1}{n-1} \frac{\Delta f}{|\nabla f|^{2}}(A\langle\nabla u, \nabla f\rangle-\langle\nabla v, \nabla f\rangle) \\
& =\frac{1}{n-1} \frac{1}{|\nabla f|^{2}}\left(\frac{n-4}{4(n-1)} u+|\nabla f|^{2}\right)\left(-A u|\nabla f|^{2}-\langle\nabla v, \nabla f\rangle\right) \\
& \leq-\frac{A}{n-1}\left(\frac{n-4}{4(n-1)} u^{2}+u|\nabla f|^{2}\right)+o(1)
\end{aligned}$$
as $m$ tends to $\infty$. Here we have used that $u$ is bounded, that $\left|\nabla f\left(y_{m}\right)\right|$ converges to $l>0$ and that $\left|\nabla v\left(y_{m}\right)\right| \leq o(1)$ as $m$ tends to $\infty$. Inserting the above inequality into (5.15), we obtain that at $y_{m}$
$$\begin{aligned}
\frac{1}{2} \Delta_{f} v \leq & -\frac{n-4}{16(n-1)^{3}}\left(2 A\left(n^{2}-1\right)+n-4\right) u^{2}-\frac{n}{n-1}|\nabla f|^{4} \\
& +\frac{1}{4(n-1)^{2}}\left(2 A(n-1)(n-3)+n^{2}-4 n+9\right) u|\nabla f|^{2}+o(1) \\
& =\left(-\alpha\left(\frac{u}{|\nabla f|^{2}}\right)^{2}+\beta \frac{u}{|\nabla f|^{2}}-\gamma\right)|\nabla f|^{4}+o(1),
\end{aligned}$$
with
$$\alpha=\frac{(n-4)\left(2 A\left(n^{2}-1\right)+n-4\right)}{16(n-1)^{3}}, \quad \beta=\frac{\left(2 A(n-1)(n-3)+n^{2}-4 n+9\right)}{4(n-1)^{2}}, \quad \gamma=\frac{n}{n-1},$$
$\alpha, \beta, \gamma>0$ for $n>4$. Now note that
$$\Delta_{1}=\beta^{2}-4 \alpha \gamma=\frac{1}{16(n-1)^{3}}\left(a A^{2}-b A+c\right),$$
with
$$a=4(n-1)(n-3)^{2}, \quad b=4\left(n^{3}+n^{2}-29 n+27\right), \quad c=n^{3}-11 n^{2}+55 n-81,$$
$a, b, c>0$ for $n>4$. Since for every $n>4$
$$\Delta_{2}=b^{2}-4 a c=64 n(n-1)(n-4)(n(5 n-26)+9)>0$$
we can choose $A>0$ such that $\Delta_{1}<0$. In particular, any $A$ satisfying
$$A \in\left(\frac{b-\sqrt{\Delta_{2}}}{2 a}, \frac{b+\sqrt{\Delta_{2}}}{2 a}\right)$$
will do, since $\frac{b-\sqrt{\Delta_{2}}}{2 a}>0$. For every $A$ satisfying (5.18) there exist a constant $\lambda>0$ such that
$$-\alpha t^{2}+\beta t-\gamma \leq-\lambda<0 \quad \text { for every } t \in \mathbb{R} .$$
Hence from (5.16) and (5.17) we deduce that
$$-o(1) \leq \frac{1}{2} \Delta_{f} v\left(y_{m}\right) \leq-\lambda\left|\nabla f\left(y_{m}\right)\right|^{4}+o(1),$$
which leads to the contradiction $0 \leq-\lambda l^{4}$ as $m$ tends to $\infty$, since we assumed $l>0$.
Thus for every $A$ satisfying (5.18) one has $l=0$ and hence $v \geq 0$ on $M^{n}$, which implies (5.14) with $C=A$. \(\square\)

Remark 5.6. As it is clear from the proof of Lemma 5.5, one has the gradient estimate (5.14) where $C$ can be chosen to be the infimum of the $A^{\prime} s$ for which the proof goes through, i.e.
$$C=\frac{b-\sqrt{\Delta_{2}}}{2 a}=\frac{4\left(n^{3}+n^{2}-29 n+27\right)-\sqrt{64 n(n-1)(n-4)(n(5 n-26)+9)}}{8(n-1)(n-3)^{2}}$$

As a corollary of the gradient estimate (5.14), we obtain the following decay estimate at infinity for $R$, which is the last technical result that we will need in the proof of Theorem 1.5.

Corollary 5.7. Let $\left(M^{n}, g\right), n>4$, be a complete, non-compact, Riemannian manifold satisfying (2.5) and (2.6) with $R<0$ on $M^{n}$. Let $O \in M^{n}$. For every $x \in M^{n}$ we have
$$R(x) \leq-\frac{c_{1}}{c_{2}+d_{g}(x, O)^{2}}$$
for some positive constants $c_{i}=c_{i}(n, u(O)), i=1,2$.
Proof. Let $u=-R$. Inequality (5.14) is equivalent to
$$\left|\nabla u^{-1 / 2}\right| \leq c$$
for some positive constant $c=c(n)$. Integrating along a geodesic, we get
$$u(x)^{-1 / 2} \leq u(O)^{-1 / 2}+c d_{g}(x, O),$$
i.e.
$$\frac{1}{u(x)} \leq\left(\frac{1}{u(O)^{1 / 2}}+c d_{g}(x, O)\right)^{2},$$
from which we immediately deduce (5.19). \(\square\)

Proof of Theorem 1.5 and Remark 1.6. First of all, if $M^{n}$ is compact, then integrating (2.6) over $M^{n}$ we get $R \equiv 0$ on $M^{n}$.

On the other hand, suppose that $M^{n}$ is non-compact. By Corollary 5.2 either $\left(M^{n}, g\right)$ is scalar flat, or $R<0$ on $M^{n}$. We assume by contradiction that $R<0$ and we recall that $u=-R$ satisfies
$$\Delta u=-\frac{n-4}{4(n-1)} u^{2} .$$
Let $\eta$ be a smooth cutoff function such that $\eta \equiv 1$ on $B_{s}(O), \eta \equiv 0$ on $B_{2 s}^{c}(O), 0 \leq \eta \leq 1$ on $M^{n}$ and $|\nabla \eta| \leq \frac{c}{s}$ for every $s \gg 1$ with $c>0$ independent of $s$. Then, using (5.14) we get
$$\begin{aligned}
\frac{n-4}{4(n-1)} \int_{M} u^{q} \eta^{2} d V_{g} & =-\int_{M} \Delta u u^{q-2} \eta^{2} d V_{g} \\
& =(q-2) \int_{M}|\nabla u|^{2} u^{q-3} \eta^{2} d V_{g}+2 \int_{M} u^{q-2}\langle\nabla u, \nabla \eta\rangle \eta d V_{g} \\
& \leq(q-2) C \int_{M} u^{q} \eta^{2} d V_{g}+\frac{c \sqrt{C}}{s} \int_{B_{2 s}(O) \backslash B_{s}(O)} u^{q-\frac{1}{2}} d V_{g},
\end{aligned}$$
with $C$ as in (5.14). By Corollary 5.7
$$\frac{n-4}{4(n-1)} \int_{M} u^{q} \eta^{2} d V_{g} \leq(q-2) C \int_{M} u^{q} \eta^{2} d V_{g}+c \sqrt{C} \frac{\left(1+s^{2}\right)^{\frac{1}{2}}}{s} \int_{B_{s}^{c}(O)} u^{q} d V_{g}$$
Thus, if $u \in L^{q}\left(M^{n}\right)$, we obtain
$$\left(\frac{n-4}{4(n-1)}-(q-2) C\right) \int_{M} u^{q} \eta^{2} d V_{g} \leq c \sqrt{C} \frac{\left(1+s^{2}\right)^{\frac{1}{2}}}{s} \int_{B_{s}^{c}(O)} u^{q} d V_{g} \longrightarrow 0 \quad \text { as } \quad s \rightarrow+\infty .$$
This yields $u \equiv 0$, if
$$\frac{n-4}{4(n-1)}-(q-2) C>0,$$
i.e. if
$$1<q<q^{*}=\frac{n-4}{4 C(n-1)}+2$$
with $C$ as in (5.14), a contradiction. Hence, the proofs of Theorem 1.5 and Remark 1.6 are complete. \(\square\)

Remark 5.8. Note that $q^{*}>2$, and that using Remark 5.6 we have
$$q^{*}=2+\frac{2(n-3)^{2}(n-4)}{4\left(n^{3}+n^{2}-29 n+27\right)-\sqrt{64 n(n-1)(n-4)(n(5 n-26)+9)}} .$$

\section*{References}
1. M.T. Anderson, Extrema of curvature functionals on the space of metrics on 3-manifolds, Calc. Var. and P.D.E. 5 (1997), 199-269.
2. \_\_\_\_, Extrema of curvature functionals on the space of metrics on 3-manifolds, II, Calc. Var. and P.D.E. 12 (2001), 1-58.
3. M. Berger, Quelques formules de variation pour une structure riemannienne, Ann. Sci. École Norm. Sup. (4) 3 (1970), 285-294.
4. A. L. Besse, Einstein manifolds, Springer-Verlag, Berlin, 2008.
5. M. Brozos-Vázquez, E. García-Río, and S. Caeiro-Oliveira, Three-dimensional homogeneous critical metrics for quadratic curvature functionals, Ann. Mat. Pura Appl. (4) 200 (2021), no. 1, 363-378. MR 4208095
6. E. Calabi, An extension of Hopf's maximum principle with an application to Riemannian geometry, Duke Math. J. 25 (1957), 45-56.
7. G. Catino, Critical metric of the $L^{2}$-norm of the scalar curvature, Proc. Amer. Math. So 142 (2014), 3981-3986.
8. \_\_\_\_, Some rigidity results on critical metrics for quadratic functionals, Calc. Var. Partial Differential Equations 54 (2015), no. 3, 2921-2937. MR 3412398
9. G. Catino, C. Mantegazza, and L. Mazzieri, On the global structure of conformal gradient solitons with nonnegative Ricci tensor, Commun. Contemp. Math. 14 (2012), no. 6, 1250045, 12. MR 2989649
10. G. Catino and P. Mastrolia, A perspective on canonical Riemannian metrics, Progress in Mathematics, vol. 336, Birkhäuser/Springer, Cham, [2020] ©2020. MR 4207078
11. G. Catino, P. Mastrolia, and D. D. Monticelli, A variational characterization of flat spaces in dimension three, Pacific J. Math. 282 (2016), no. 2, 285-292. MR 3478936
12. G. Catino, P. Mastrolia, D. D. Monticelli, and M. Rigoli, On the geometry of gradient Einstein-type manifolds, Pacific J. Math. 286 (2017), no. 1, 39-67. MR 3582400
13. J. Cheeger and T. H. Colding, Lower bounds on Ricci curvature and the almost rigidity of warped products, Ann. of Math. (2) 144 (1996), no. 1, 189-237.
14. M. Gursky and J. Viaclovsky, Rigidity and stability of Einstein metrics for quadratic curvature functionals, J. Reine Angew. Math. 700 (2015), 37-91. MR 3318510
15. M. J. Gursky and J. Viaclovsky, Critical metrics on connected sums of Einstein four-manifolds, Adv. Math. 292 (2016), 210-315. MR 3464023
16. M. J. Gursky and J. A. Viaclovsky, A new variational characterization of three-dimensional space forms, Invent. Math. 145 (2001), no. 2, 251-278.
17. F. Lamontagne, Une remarque sur la norme $L^{2}$ du tenseur de courbure, C. R. Acad. Sci. Paris Sér. I Math. 319 (1994), no. 3, 237-240.
18. \_\_\_\_, A critical metric for the $L^{2}$-norm of the curvature tensor on $S^{3}$, Proc. Amer. Math. Soc. 126 (1998), no. 2, 589-593.
19. P. Mastrolia and M. Rimoldi, Some triviality results for quasi-Einstein manifolds and Einstein warped products, Geom. Dedicata 169 (2014), 225-237. MR 3175246
20. Z. Qian, Estimates for weighted volumes and applications, Quart. J. Math. Oxford Ser. (2) 48 (1997), 235-242.
21. N. K. Smolentsev, Spaces of Riemannian metrics, J. Math. Sci. 142 (2007), no. 5, 2436-2519.
22. G. Tian and J. Viaclovsky, Bach-flat asymptotically locally Euclidean metrics, Invent. Math. 160 (2005), no. 2, 357-415. MR 2138071
23. G. Wei and W. Wylie, Comparison geometry for the Bakry-Emery Ricci tensor, J. Differential Geom. 83 (2009), no. 2, 377-405. MR 2577473
24. S.-T. Yau, Harmonic functions on complete Riemannian manifolds, Comm. Pure Appl. Math. 28 (1975), 201-228.
25. \_\_\_\_, Some function-theoretic properties of complete Riemannian manifolds and their applications to geometry, Indiana Math. J. 25 (1976), 659-670.
(Giovanni Catino) Dipartimento di Matematica, Politecnico di Milano, Piazza Leonardo da Vinci 32, 20133 Milano, Italy
Email address: giovanni.catino@polimi.it
(Paolo Mastrolia) Dipartimento di Matematica, Università degli Studi di Milano, Via Saldini 50, 20133 Italy.
Email address: paolo.mastrolia@unimi.it
(Dario Monticelli) Dipartimento di Matematica, Politecnico di Milano, Piazza Leonardo da Vinci 32, 20133 Milano, Italy
Email address: dario.monticelli@polimi.it