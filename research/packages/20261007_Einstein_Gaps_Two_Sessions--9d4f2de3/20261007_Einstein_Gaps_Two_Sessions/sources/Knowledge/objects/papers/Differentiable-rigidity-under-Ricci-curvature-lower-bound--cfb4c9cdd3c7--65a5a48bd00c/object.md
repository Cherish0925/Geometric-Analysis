# Differentiable rigidity under Ricci curvature lower bound

- Category: papers
- Identity: doi:10.1215/00127094-1507272
- Content status: fulltext_ok

---

---
source_file: 0805_3845.pdf
converter: mathpix
format: mmd
---

\title{
Differentiable Rigidity under Ricci curvature lower bound
}

\author{
L. Bessières, G. Besson, G. Courtois and S. Gallot
}

November 5, 2021

\begin{abstract}
In this article we prove a differentiable rigidity result. Let $(Y, g)$ and $\left(X, g_{0}\right)$ be two closed $n$-dimensional Riemannian manifolds $(n \geqslant 3)$ and $f: Y \rightarrow X$ be a continuous map of degree 1 . We furthermore assume that the metric $g_{0}$ is real hyperbolic and denote by $d$ the diameter of $\left(X, g_{0}\right)$. We show that there exists a number $\varepsilon:=\varepsilon(n, d)>0$ such that if the Ricci curvature of the metric $g$ is bounded below by $-n(n-1)$ and its volume satisfies $\operatorname{vol}_{g}(Y) \leqslant(1+\varepsilon) \operatorname{vol}_{g_{0}}(X)$ then the manifolds are diffeomorphic. The proof relies on Cheeger-Colding's theory of limits of Riemannian manifolds under lower Ricci curvature bound.
\end{abstract}

\section*{1 Introduction}

Let $Y$ and $X$ be two closed manifolds. The manifold $Y$ is said to dominate $X$ if there is a continuous map $f: Y \rightarrow X$ of degree one. An $n$-dimensional hyperbolic manifold $X$ has the smallest volume among the set of all Riemannian manifolds $(Y, g)$ such that $Y$ dominates $X$ and the metric $g$ has Ricci curvature $\operatorname{Ric}_{g} \geq-(n-1) g$. In dimension $n=2$ this is a consequence of the Gauss-Bonnet formula and in dimension $n \geq 3$ this follows from the

Theorem 1.1. [5] Let $\left(X, g_{0}\right)$ be an $n$-dimensional closed hyperbolic manifold and $Y$ a closed manifold which dominates $X$. Then, for any metric $g$ on $Y$ such that $\operatorname{Ric}_{g} \geq-(n-1) g$, one has $\operatorname{vol}_{g}(Y) \geq \operatorname{vol}_{g_{0}}(X)$, and equality happens if and only if $(Y, g)$ and $\left(X, g_{0}\right)$ are isometric.

The minimal volume of a closed manifold $Y$ is defined as
$$\operatorname{minvol}(Y)=\inf \left\{\operatorname{vol}_{g}(Y) / \quad\left|\mathrm{K}_{g}\right| \leq 1\right\}$$
where $\mathrm{K}_{g}$ is the sectional curvature of the Riemannian metric $g$. An $n$-dimensional hyperbolic manifold $X$ is characterized by its minimal volume among the set of all Riemannian manifolds $Y$ such that $Y$ is homotopy equivalent to $X$. Namely,

Theorem 1.2. [1] Let $X$ be an $n$-dimensional closed hyperbolic manifold and $Y$ a closed manifold which dominates $X$. Then, $\operatorname{minvol}(Y)=\operatorname{minvol}(X)$ if and only if $X$ and $Y$ are diffeomorphic.

The aim of this paper is to show the following gap result. It improves the above theorem 1.2 since we now require a lower bound on the Ricci curvature instead of a pinching of the sectional curvature; moreover, under the hypothesis, we prove that if the volume of $Y$ is close to the volume of $X$ then these two manifolds are diffeomorphic. More precisely,

Theorem 1.3. Given any integer $n \geq 3$ and $d>0$, there exists $\varepsilon(n, d)>0$ such that the following holds. Suppose that $\left(X, g_{0}\right)$ is an $n$-dimensional closed hyperbolic manifold with diameter $\leq d$ and that $Y$ is a closed manifold which dominates $X$. Then $Y$ has a metric $g$ such that
$$\begin{aligned}
\operatorname{Ric}_{g} & \geq-(n-1) g \\
\operatorname{vol}_{g}(Y) & \leq(1+\varepsilon) \operatorname{vol}_{g_{0}}(X)
\end{aligned}$$
if and only if $f$ is homotopic to a diffeomorphism.
In [15] the authors prove the existence of closed n-dimensional manifolds $Y$ which are homeomorphic to a closed n-dimensional hyperbolic manifold $\left(X, g_{0}\right)$ but not diffeomorphic to it. An immediate corollary of the above theorem is the following.

Corollary 1.4. With the above notations, there exists $\varepsilon>0$ depending on $n$ and on the diameter of $X$ with the property that for any such $Y$ and any Riemannian metric $g$ on $Y$ whose Ricci curvature is bounded below by $-(n-1)$ one has,
$$\operatorname{vol}(Y, g)>(1+\varepsilon) \operatorname{vol}\left(X, g_{0}\right) .$$
To be more precise in [15] the manifold $Y$ is obtained as follows:
$$Y=X \sharp \Sigma,$$
where $\Sigma$ is an exotic sphere. Not every closed hyperbolic manifold $X$ gives rise to such a $Y$ that is (obviously) homeomorphic but not diffeomorphic to $X$. Indeed, we may have to take a finite cover of $X$. But when we get one construction that works, it does on any finite cover $\bar{X}$ of $X$ as well. The authors also prove that by taking covers of arbitrary large degree we can put on $Y$ a metric whose sectional curvature is arbitrarily pinched around, say -1. The stronger the pinching, the larger the degree. Now assume that $\varepsilon$ could be taken independent of the diameter of $X$; applying the results of [5] one could show that the volumes of the two manifold are very close when the pinching on $Y$ is very sharp (close to -1). The volume of $Y$ endowed with this pinched metric could then be taken smaller than $(1+\varepsilon) \operatorname{vol}\left(X, g_{0}\right)$, by choosing a covering of large degree; the manifolds though are not diffeomorphic. This gives a contradiction and shows that "size" of $X$ has to be involved in the statement of the theorem, for example its diameter.

This work was supported by the grant ANR: ANR-07-BLAN-0251.

\subsection*{1.1 Sketch of the Proof}

We argue by contradiction. Suppose that there is a sequence $\left(X_{k}\right)_{k \in \mathbf{N}}$ of closed hyperbolic manifolds with diameter $\leq d$ and a sequence of closed manifolds $Y_{k}$, of degree one continuous maps $f_{k}: Y_{k} \rightarrow X_{k}$ and metrics $g_{k}$ on $Y_{k}$ satisfying the hypothesis (3) and (4) for some $\varepsilon_{k}$ going to zero. Since $f_{k}$ is of degree one and $X_{k}$ is hyperbolic, it is equivalent to say (thanks to Mostow's rigidity Theorem) that $f_{k}$ is homotopic to a diffeomorphism or simply that $X_{k}$ and $Y_{k}$ are diffeomorphic. We thus assume that $Y_{k}$ and $X_{k}$ are not diffeomorphic. One then shows that up to a subsequence, for large $k, Y_{k}$ is diffeomorphic to a closed manifold $Y, X_{k}$ is diffeomorphic to a closed manifold $X$, and $X$ and $Y$ are diffeomorphic. One argues as follows: by the classical finiteness results we get the sub-convergence of the sequence $\left\{X_{k}\right\}$. Indeed, the curvature is -1, the diameter is bounded by hypothesis, and there is a universal lower bound for the volume of any closed hyperbolic manifold of a given dimension, thanks to Margulis' Lemma (see [3]). Cheeger's finiteness theorem then applies. Moreover, on a closed manifold of dimension $\geq 3$, there is at most one hyperbolic metric, up to isometry. We can therefore suppose that $X_{k}=X$ is a fixed hyperbolic manifold. The inequality proved in theorem 1.1 provides a lower bound for the volume of $Y_{k}$ as it is explained below. We have no a priori bounds on the diameter of $\left(Y_{k}, g_{k}\right)$, but we can use Cheeger-Colding's theory to obtain sub-convergence in the pointed Gromov-Hausdorff topology to a complete metric space $(Z, d)$ with small singular set. To obtain more geometric control, the idea is to use the natural maps between $Y_{k}$ and $X$ (see [5]). One can show that they sub-convergence to a limit map between $Z$ and $X$, which is an isometry. Then $X$ is an $n$-dimensional smooth closed Riemannian manifold which is the Gromov-Hausdorff limit of the sequence ( $Y_{k}, g_{k}$ ) of Riemannian manifold of dimension $n$ satisfying the lower bound (3) on Ricci curvature, therefore $X$ and $Y_{k}$ are diffeomorphic for large $k$ by a theorem of J. Cheeger and T. Colding.

The paper is organised as follows. The construction and the properties of the natural maps are given in Section 2. In Section 3, we construct the limit space $Z$ and the limit map $F: Z \rightarrow X$. In Section 4, we prove that $F$ is an isometry and conclude.

\subsection*{1.2 Maps of arbitrary degree, scalar curvature}

For two closed manifolds $Y$ and $X$ we said above that $Y$ dominates $X$ if there exists a map of degree one from $Y$ onto $X$. We could have required that there exists a map $f: Y \rightarrow X$ of non-zero degree. The main theorem of [5] was stated and proved in this set up. More precisely, the following statement holds

Theorem 1.5. [5] Let $\left(X, g_{0}\right)$ be an $n$-dimensional closed hyperbolic manifold and $Y$ a closed manifold such that there exists a map $f: Y \rightarrow X$ with non-zero degree denoted $\operatorname{deg}(f)$. Then, for any metric $g$ on $Y$ such that $\operatorname{Ric}_{g} \geq-(n-1) g$, one has $\operatorname{vol}_{g}(Y) \geq|\operatorname{deg}(f)| \operatorname{vol}_{g_{0}}(X)$, and equality happens if and only if $f$ is homotopic to a Riemannian covering (i.e. locally isometric) of degree - deg $(f)$ - from $(Y, g)$ onto $\left(X, g_{0}\right)$.

With the technique developed in this article, the following result can be proved
Theorem 1.6. Given any integer $n \geq 3$ and $d>0$, there exists $\varepsilon(n, d)>0$ such that the following holds. Suppose that $\left(X, g_{0}\right)$ is an $n$-dimensional closed hyperbolic manifold with diameter $\leq d$ and that $Y$ is a closed manifold such that there exists a map $f: Y \rightarrow X$ with non-zero degree. Then $Y$ has a metric $g$ such that
$$\begin{aligned}
\operatorname{Ric}_{g} & \geq-(n-1) g \\
\operatorname{vol}_{g}(Y) & \leq(1+\varepsilon)|\operatorname{deg}(f)| \operatorname{vol}_{g_{0}}(X)
\end{aligned}$$
if and only if $f$ is homotopic to a covering of degree $|\operatorname{deg}(f)|$.
The proof is essentially the one described above; it uses the technique described below and the treatment of an arbitrary degree given in [1]. The fact that the degree can be, in absolute value, greater than one yields extra technicalities. For the sake of clarity we shall omit this proof in the present article and leave it to the reader. A corollary is,

Corollary 1.7. Let $\left(X, g_{0}\right)$ be a closed $n$-dimensional hyperbolic manifold, then there exists $\varepsilon>0$, such that, for any metric $g$ on the connected sum $X \sharp X$ satisfying that its Ricci curvature of $g$ is not smaller than $-(n-1)$,
$$\operatorname{vol}(X \sharp X, g) \geq 2(1+\varepsilon) \operatorname{vol}\left(X, g_{0}\right) .$$
We may now ask whether such a result could be true with a lower bound on the scalar curvature instead of a lower bound on the Ricci curvature. The situation in dimension 3, completely clarified by Perelman's work, shows that the answer to this question is negative. More precisely, if $\left(X, g_{0}\right)$ is a 3-dimensional closed hyperbolic manifolds, a consequence of [2, Inequality 2.10] is that,
$$\inf \{\operatorname{vol}(X \sharp X, g) / \operatorname{Scal}(g) \geq-6\}=2 \operatorname{vol}\left(X, g_{0}\right) .$$
In dimension greater or equal to 4, it follows from [16] and the solution to the Yamabe problem that,
$$\inf \{\operatorname{vol}(X \sharp X, g) / \operatorname{Scal}(g) \geq-6\} \leqslant 2 \operatorname{vol}\left(X, g_{0}\right) .$$

\section*{2 Some a priori control on $(Y, g)$}

Some a priori control on the metric $g$ will be needed in section 2 and 3. We give here the necessary results.

Let $\left(X, g_{0}\right)$ be an hyperbolic manifold and $Y$ be a manifold satisfying the assumptions of Theorem 1.3. For any riemannian metric $g$ on $Y$ satisfying the curvature assumption (3), one has the following inequality
$$\operatorname{vol}_{g}(Y) \geq \operatorname{vol}_{g_{0}}(X) .$$

It is a consequence of Besson-Courtois-Gallot's inequality (see [5])
$$h(g)^{n} \operatorname{vol}_{g}(Y) \geq h\left(g_{0}\right)^{n} \operatorname{vol}_{g_{0}}(X),$$
where $h(g)$ is the volume entropy, or the critical exponent, of the metric $g$, i.e.:
$$h(g)=\lim _{R \rightarrow+\infty} \frac{1}{R} \ln \left(\operatorname{vol}_{\tilde{g}}\left(B_{\tilde{g}}(x, R)\right)\right),$$
where $\tilde{g}$ is the lifted metric on $\tilde{Y}$. Indeed, any metric $g$ on $Y$ which satisfies (3), verifies, by Bishop's Theorem,
$$h(g) \leq h\left(g_{0}\right)=n-1 .$$
One can obtain a lower bound of the volume of some balls by Gromov's isolation Theorem (see [13, Theorem 0.5]). It shows that if the simplicial volume $\|Y\|$ - a topological invariant also called Gromov's norm- of $Y$ is non-zero, then for any riemannian metric $g$ on $Y$ satisfying the curvature assumption (3), there exists at least one point $y_{g} \in Y$ such that
$$\operatorname{vol}_{g}\left(B\left(y_{g}, 1\right)\right) \geq v_{n}>0 .$$
Here $B\left(y_{g}, 1\right)$ is the geodesic ball of radius 1 for the metric $g$ and $v_{n}$ is a universal constant. This theorem applies in our situation since, by an elementary property of the simplicial volume, $\|Y\| \geq\|X\|$ if there is a degree one map from $Y$ to $X$ (see [13]). On the other hand, $X$ has an hyperbolic metric and hence $\|X\|>0$ by Gromov-Thurston's Theorem (see [13]).
Given this universal lower bound for the volume of a unit ball $B\left(y_{g}, 1\right)$, the volume of any ball $B(y, r)$ is bounded from bellow in terms of $r$ and $d\left(y_{g}, y\right)$. Indeed, recall that under the curvature assumption (3), Bishop-Gromov's Theorem shows that for any $0<r \leq R$, one has
$$\frac{\operatorname{vol}_{g}(B(y, r))}{\operatorname{vol}_{g}(B(y, R))} \geq \frac{\operatorname{vol}_{\mathbf{H}^{n}}\left(\mathrm{~B}_{\mathbf{H}^{\mathrm{n}}}(\mathrm{r})\right)}{\left.\operatorname{vol}_{\mathbf{H}^{n}}\left(\mathrm{~B}_{\mathbf{H}^{\mathrm{n}}} \mathrm{R}\right)\right)},$$
where $\mathrm{B}_{\mathbf{H}^{\mathrm{n}}}(\mathrm{r})$ is a ball of radius $r$ in the hyperbolic space $\mathbf{H}^{n}$. As $B\left(y_{g}, 1\right) \subset B(y, 1+$ $\left.d\left(y_{g}, y\right)+r\right)$, one deduces from (9) that
$$\begin{aligned}
\operatorname{vol}_{g}(B(y, r)) & \geq \operatorname{vol}_{g}\left(B\left(y, 1+d\left(y_{g}, y\right)+r\right)\right) \frac{\operatorname{vol}_{\mathbf{H}^{n}}\left(\mathrm{~B}_{\mathbf{H}^{\mathrm{n}}}(\mathrm{r})\right)}{\operatorname{vol}_{\mathbf{H}^{n}}\left(\mathrm{~B}_{\mathbf{H}^{\mathrm{n}}}\left(1+\mathrm{d}\left(\mathrm{y}_{\mathrm{g}}, \mathrm{y}\right)+\mathrm{r}\right)\right)} \\
& \geq v_{n} \frac{\operatorname{vol}_{\mathbf{H}^{n}}\left(\mathrm{~B}_{\mathbf{H}^{\mathrm{n}}}(\mathrm{r})\right)}{\operatorname{vol}_{\mathbf{H}^{n}}\left(\mathrm{~B}_{\mathbf{H}^{\mathrm{n}}}\left(1+\mathrm{d}\left(\mathrm{y}_{\mathrm{g}}, \mathrm{y}\right)+\mathrm{r}\right)\right)} .
\end{aligned}$$
The curvature assumption (3) and the volume estimates (9) or (11) are those required to use the non-collapsing part of Cheeger-Colding's Theory, as we shall see in section 3.

\section*{3 The natural maps}

In the following sections 2.1 and 2.2 we recall the construction and the main properties of the natural maps defined in [5] (see also [6]).

\subsection*{3.1 Construction of the natural maps}

Suppose that $(Y, g)$ and $\left(X, g_{0}\right)$ are closed riemannian manifolds and that
$$f: Y \rightarrow X,$$
is a continuous map of degree one. For the sake of simplicity, we assume that $g_{0}$ is hyperbolic (the construction holds in a much more general situation). Then, for any $c>h(g)$ there exists a $C^{1}$ map
$$F_{c}: Y \longrightarrow X,$$
homotopic to $f$, such that for all $y \in Y$,
$$\left|\operatorname{Jac} F_{c}(y)\right| \leq\left(\frac{c}{h\left(g_{0}\right)}\right)^{n},$$
with equality for some $y \in Y$ if and only if $d_{y} F_{c}$ is an homothety of ratio $\frac{c}{h\left(g_{0}\right)}$.
Inequality (6) is then easily obtained by integration of (12) and by taking a limit when $c$ goes to $h(g)$. To obtain global rigidity properties, one has in general to study carefully the behaviour of $F_{c}$ as $c$ goes to $h(g)$.
The construction of the maps is divided in four steps. Let $\tilde{Y}$ and $\tilde{X}$ be the universal coverings of $Y$ and $X$ respectively, and $\tilde{f}: \tilde{Y} \rightarrow \tilde{X}$ a lift of $f$.
Step 1: For each $y \in \tilde{Y}$ and $c>h(g)$, let $\nu_{y}^{c}$ be the finite measure on $\tilde{Y}$ defined by
$$d \nu_{y}^{c}(z)=e^{-c . \rho(y, z)} \operatorname{dv}_{\tilde{\mathrm{g}}}(z)$$
where $z \in \tilde{Y}, \tilde{g}$ is the lifted metric on $\tilde{Y}$ and $\rho(.,$.$) is the distance function of (\tilde{Y}, \tilde{g})$.
Step 2: Fushing forward this measure gives a finite measure $\tilde{f}_{*} \nu_{y}^{c}$ on $\tilde{X}$. Let us recall that it is defined by
$$\tilde{f}_{*} \nu_{y}^{c}(U)=\nu_{y}^{c}\left(\tilde{f}^{-1}(U)\right) .$$

Step 3: One defines a finite measure $\mu_{y}^{c}$ on $\partial \tilde{X}$ by convolution of $\tilde{f}_{*} \nu_{y}$ with all visual probability measures $P_{x}$ of $\tilde{X}$. Recall that the visual probability measure $P_{x}$ at $x \in \tilde{X}$ is defined as follows: the unit tangent sphere at $x$ noted $U_{x} \tilde{X}$ projects onto the geometric boundary $\partial \tilde{X}$ by the map
$$v \in U_{x} \tilde{X} \xrightarrow{E_{x}} \gamma_{v}(\infty) \in \partial \tilde{X},$$
where $\gamma_{v}(t)=\exp _{x}(t v)$. The measure $P_{x}$ is then the push-forward by $E_{x}$ of the canonical probability measure on $U_{x} \tilde{X}$, i.e., for a Borel set $A \in \partial \tilde{X}, P_{x}(A)$ is the measure of the set of vectors $v \in U_{x} \tilde{X}$ such that $\gamma_{v}(+\infty) \in A$.

Then
$$\begin{aligned}
\mu_{y}^{c}(A) & =\int_{\tilde{X}} P_{x}(A) d \tilde{f}_{*} \nu_{y}^{c}(x) \\
& =\int_{\tilde{Y}} P_{\tilde{f}(z)}(A) d \nu_{y}^{c}(z)
\end{aligned}$$

One can identifies $\partial \tilde{X}$ with the unit sphere in $\mathbf{R}^{n}$, by choosing an origin $o \in \tilde{X}$ and using $E_{0}$. The density of this measure is given by (see [5])
$$d \mu_{y}^{c}(\theta)=\left(\int_{\tilde{Y}} e^{-h\left(g_{0}\right) B(\tilde{f}(z), \theta)} e^{-c \rho(y, z)} \mathrm{dv}_{\tilde{\mathrm{g}}}(z)\right) d \theta$$
where $\theta \in \partial \tilde{X}, d \theta$ is the canonical probability measure on $S^{n-1}$ and $B(., \theta)$ is a Busemann function on $\tilde{X}$ normalised to vanish at $x=o$. We will use the notation
$$p(x, \theta)=e^{-h\left(g_{0}\right) B(x, \theta)} .$$

Step 4: The map
$$F_{c}: \tilde{Y} \longrightarrow \tilde{X}$$
associates to any $y \in \tilde{Y}$ the unique $x \in \tilde{X}$ which minimizes on $\tilde{X}$ the function
$$x \rightarrow \mathcal{B}(x)=\int_{\partial \tilde{X}} B(x, \theta) d \mu_{y}^{c}(\theta)$$
(see Appendix A in [5]).
The maps $F_{c}$ are shown to be $\mathcal{C}^{1}$ and equivariant with respect to the actions of the fundamental groups of $Y$ and $X$ on their respective universal cover. The quotient maps, which are also denoted by $F_{c}: Y \rightarrow X$, are homotopic to $f$. Note that $F_{c}$ depends heavily on the metric $g$.

\subsection*{3.2 Some technical lemmas}

Let us give some definitions.
Definition 3.1. For $y \in \tilde{Y}$ let $\sigma_{y}^{c}$ be the probability measure on $\partial \tilde{X}$ defined by
$$\sigma_{y}^{c}=\frac{\mu_{y}^{c}}{\mu_{y}^{c}(\partial \tilde{X})} .$$
Let us remark that we have
$$\left\|\mu_{y}^{c}\right\|=\mu_{y}^{c}(\partial \tilde{X})=\int_{\tilde{Y}} e^{-c \rho(y, z)} \operatorname{dv}_{\tilde{\mathrm{g}}}(z)=\left\|\nu_{y}^{c}\right\| .$$
We consider two positive definite bilinear forms of trace equal to one and the corresponding symmetric endomorphisms.
Definition 3.2. For any $y \in \tilde{Y}, u, v \in T_{F_{c}(y)} \tilde{X}$,
$$\mathbf{h}_{\mathbf{y}}^{\mathbf{c}}(u, v)=\int_{\partial \tilde{X}} d B_{\left(F_{c}(y), \theta\right)}(u) d B_{\left(F_{c}(y), \theta\right)}(v) d \sigma_{y}^{c}(\theta)=g_{0}\left(\mathbf{H}_{\mathbf{y}}^{\mathbf{c}}(u), v\right) .$$
And, for any $y \in \tilde{Y}, u, v \in T_{y} \tilde{Y}$,
$$\mathbf{h}_{\mathbf{y}}^{\prime \mathbf{c}}(u, v)=\frac{1}{\mu_{y}^{c}(\partial \tilde{X})} \int_{\tilde{Y}} d \rho_{(y, z)}(u) d \rho_{(y, z)}(v) d \nu_{y}^{c}(z)=g\left(\mathbf{H}_{\mathbf{y}}^{\prime \mathbf{c}}(u), v\right) .$$

Lemma 3.3. For any $y \in \tilde{Y}, u \in T_{y} \tilde{Y}, v \in T_{F(y)} \tilde{X}$, one has
$$\left|g_{0}\left(\left(I-H_{y}^{c}\right) d_{y} F_{c}(u), v\right)\right| \leq c\left(g_{0}\left(H_{y}^{c}(v), v\right)\right)^{1 / 2}\left(g\left(H_{y}^{\prime c}(u), u\right)\right)^{1 / 2} .$$
Proof. Since $F_{c}(y)$ is an extremum of the function $\mathcal{B}$, one has
$$d_{F_{c}(y)} \mathcal{B}(v)=\int_{\partial \tilde{X}} d B_{\left(F_{c}(y), \theta\right)}(v) d \mu_{y}^{c}(\theta)=0$$
for each $v \in T_{F_{c}(y)} \tilde{X}$. By differentiating this equation in a direction $u \in T_{y} \tilde{Y}$, one obtains
$$\begin{aligned}
& \int_{\partial \tilde{X}} D d B_{\left(F_{c}(y), \theta\right)}\left(d_{y} F_{c}(u), v\right) d \mu_{y}^{c}(\theta)+\ldots \\
& \quad \cdots+\int_{\partial \tilde{X}} d B_{\left(F_{c}(y), \theta\right)}(v)\left(\int_{\tilde{Y}} p(\tilde{f}(z), \theta)\left(-c d \rho_{(y, z)}(u)\right) d \nu_{y}^{c}(z)\right) d \theta=0
\end{aligned}$$
Using Cauchy-Schwarz inequality in the second term, one gets
$$\begin{aligned}
& \left|\int_{\partial \tilde{X}} D d B_{\left(F_{c}(y), \theta\right)}\left(d_{y} F_{c}(u), v\right) d \mu_{y}^{c}(\theta)\right| \leq \\
& \int_{\partial \tilde{X}}\left|d B_{\left(F_{c}(y), \theta\right)}(v)\right|\left(\int_{\tilde{Y}} p(\tilde{f}(z), \theta) d \nu_{y}^{c}(z)\right)^{1 / 2}\left(\int_{\tilde{Y}} p(\tilde{f}(z), \theta)\left|c d \rho_{(y, z)}(u)\right|^{2} d \nu_{y}^{c}(z)\right)^{1 / 2} d \theta
\end{aligned}$$
which is, using Cauchy-Schwarz inequality again
$$\begin{aligned}
& \leq c\left(\int_{\partial \tilde{X}}\left|d B_{\left(F_{c}(y), \theta\right)}(v)\right|^{2} \int_{\tilde{Y}} p(\tilde{f}(z), \theta) d \nu_{y}^{c}(z) d \theta\right)^{1 / 2}\left(\int_{\partial \tilde{X}} \int_{\tilde{Y}} p(\tilde{f}(z), \theta)\left|d \rho_{(y, z)}(u)\right|^{2} d \nu_{y}^{c}(z) d \theta\right)^{1 / 2} \\
& =c\left(\int_{\partial \tilde{X}}\left|d B_{\left(F_{c}(y), \theta\right)}(v)\right|^{2} d \mu_{y}^{c}(\theta)\right)^{1 / 2}\left(\int_{\tilde{Y}}\left|d \rho_{(y, z)}(u)\right|^{2} d \nu_{y}^{c}(z)\right)^{1 / 2} \\
& =c \mu_{y}^{c}(\partial \tilde{X})\left(g_{0}\left(H_{y}^{c}(v), v\right)\right)^{1 / 2}\left(g\left(H_{y}^{\prime c}(u), u\right)\right)^{1 / 2}
\end{aligned}$$
It is shown in [5, Chapter 5] that $D d B=g_{0}-d B \otimes d B$ for an hyperbolic metric. The left term of the inequality is thus $\mu_{y}^{c}(\partial \tilde{X}) g_{0}\left(\left(I-H_{y}^{c}\right) d_{y} F_{c}(u), v\right)$. This proves the lemma. \(\square\)

Definition 3.4. Let $0<\lambda_{1}^{c}(y) \leq \ldots \leq \lambda_{n}^{c}(y)<1$ be the eigenvalues of $H_{y}^{c}$.
Proposition 3.5. There exists a constant $A:=A(n)>0$ such that, for any $y \in Y$,
$$\left|\operatorname{Jac} F_{c}(y)\right| \leq\left(\frac{c}{h\left(g_{0}\right)}\right)^{n}\left(1-A \sum_{i=1}^{n}\left(\lambda_{i}^{c}(y)-\frac{1}{n}\right)^{2}\right)$$
Proof. The proof is based on the two following lemmas.

Lemma 3.6. At each $y \in \tilde{Y}$,
$$\left|\operatorname{Jac} F_{c}(y)\right| \leq\left(\frac{c}{\sqrt{n}}\right)^{n} \frac{\operatorname{det}\left(H_{y}^{c}\right)^{1 / 2}}{\operatorname{det}\left(I-H_{y}^{c}\right)} .$$
Proof of lemma 3.6. Let $\left\{v_{i}\right\}$ be an orthonormal basis of $T_{F_{c}(y)} \tilde{X}$ which diagonalizes $H_{y}{ }^{c}$. We can assume that $d_{y} F_{c}$ is invertible otherwise the above inequality is obvious. Let $u_{i}^{\prime}=\left[\left(I-H_{y}{ }^{c}\right) \circ d_{y} F_{c}\right]^{-1}\left(v_{i}\right)$. The Schmidt orthonormalisation process applied to $\left(u_{i}^{\prime}\right)$ gives an orthonormal basis $\left(u_{i}\right)$ at $T_{y} \tilde{Y}$. The matrix of $\left(I-H_{y}{ }^{c}\right) \circ d_{y} F_{c}$ in the basis $\left(u_{i}\right)$ and $\left(v_{i}\right)$ is upper triangular, then
$$\operatorname{det}\left(I-H_{y}{ }^{c}\right) \operatorname{Jac} F_{c}(y)=\prod_{i=1}^{n} g_{0}\left(\left(I-H_{y}{ }^{c}\right) \circ d_{y} F_{c}\left(u_{i}\right), v_{i}\right),$$
which gives, with (13),
$$\begin{aligned}
\operatorname{det}\left(I-H_{y}{ }^{c}\right)\left|\operatorname{Jac} F_{c}(y)\right| & \leq c^{n}\left(\prod_{i=1}^{n} g_{0}\left(H_{y}{ }^{c}\left(v_{i}\right), v_{i}\right)\right)^{1 / 2}\left(\prod_{i=1}^{n} g\left(H_{y}^{\prime c}\left(u_{i}\right), u_{i}\right)\right)^{1 / 2} \\
& \leq c^{n} \operatorname{det}\left(H_{y}{ }^{c}\right)^{1 / 2}\left[\frac{1}{n} \sum_{i=1}^{n} g\left(H_{y}^{\prime c}\left(u_{i}\right), u_{i}\right)\right]^{n / 2},
\end{aligned}$$
this proves the desired inequality since $\operatorname{trace}\left(H_{y}^{\prime c}\right)=1$. \(\square\)

Lemma 3.7. Let $H$ a symmetric positive definite $n \times n$ matrix whose trace is equal to one then, if $n \geq 3$,
$$\frac{\operatorname{det}\left(H^{1 / 2}\right)}{\operatorname{det}(I-H)} \leq\left(\frac{n}{h\left(g_{0}\right)^{2}}\right)^{n / 2}\left(1-A \sum_{i=1}^{n}\left(\lambda_{i}-\frac{1}{n}\right)^{2}\right)$$
for some positive constant $A(n)$.
Proof of lemma 3.7. The proof is given in Appendix B5 of [5]. This is the point where the rigidity of the natural maps fails in dimension 2. This completes the proof of proposition 3.5. \(\square\) \(\square\)

\subsection*{3.3 Some nice properties}

We now show that when the volumes of $(Y, g)$ and $\left(X, g_{0}\right)$ are close then the natural maps $F_{c}$ have nice properties. In this section, we shall consider $F_{c}$ as a map from $(Y, g)$ to $\left(X, g_{0}\right)$. We suppose that the metric $g$ satisfies the curvature assumption (3) and the assumption on its volume (4) for some $\varepsilon>0$. Let us introduce some terminology.

Definition 3.8. Let $0<\alpha<1$. We say that a property holds $\alpha$-ae ( $\alpha$-almost everywhere) on a set $A$ if the set $A_{+}$of points of $A$ where the property holds has relative volume bigger or equal to $1-\alpha$, i.e. $\frac{\operatorname{vol}\left(A_{+}\right)}{\operatorname{vol}(A)} \geq 1-\alpha$.

We show that $d F_{c}$ is $\alpha$-close to be isometric $\alpha$-ae on $Y$ for some positive $\alpha(\varepsilon, c)$. Moreover $\alpha(\varepsilon, c) \rightarrow 0$ as $\varepsilon \rightarrow 0$ and $c \rightarrow h(g)$. On the other hand, given any radius $R>0$, one shows that $\left\|d F_{c}\right\|$ is uniformly bounded on balls $B\left(y_{g}, R\right)$, provided $c$ is close enough to $h(g)$. Recall that we have a lower bound for the volume of $(Y, g)$ but we do not have an upper bound for its diameter. The key point is to show that $H_{y}^{c}$ is $\alpha$-close to $\frac{1}{n} I d$ on a set of large volume, and is bounded on a ball of fixed radius, with respect to the parameters $\varepsilon, c$.

To estimate from above $c-h(g)$ we introduce a parameter $\delta>0$. We suppose that the volume entropy of $g$ satisfies the inequalities
$$h(g)<c \leq h(g)+\delta .$$
Observe that (7), (15) and (16) implies that
$$\left|\operatorname{Jac} F_{c}(y)\right| \leq\left(\frac{h(g)+\delta}{h\left(g_{0}\right)}\right)^{n} \leq\left(1+\frac{\delta}{n-1}\right)^{n-1},$$
for all $y \in Y$. The map $F_{c}$ is thus almost volume decreasing. On the other hand, as $\operatorname{vol}_{g}(Y)$ is close to $\operatorname{vol}_{g_{0}}(X)$, the set in $Y$ where $F_{c}$ decreases the volume a lot must have a small measure. Equivalently, $\left|\mathrm{Jac} F_{c}\right|$ must be close to 1 in $L^{1}$ norm. We now give a precise statement.

Lemma 3.9. If $\delta$ is small enough, there exists $\alpha_{1}=\alpha_{1}(\varepsilon, \delta)>0$ such that $\alpha_{1}$-ae on $Y$ one has,
$$1-\alpha_{1} \leq\left|\operatorname{Jac} F_{c}(y)\right|,$$
and for all $y \in Y$ one has
$$\left|\operatorname{Jac} F_{c}(y)\right| \leq 1+\alpha_{1} .$$
Moreover, $\alpha_{1}(\varepsilon, \delta) \rightarrow 0$ as $\varepsilon$ and $\delta \rightarrow 0$.
Proof. Let
$$\alpha=\max \left(\sqrt{\left(1+\frac{\delta}{n-1}\right)^{n-1}-1}, \sqrt{\varepsilon}\right) .$$
Thus $\left(1+\frac{\delta}{n-1}\right)^{n-1} \leq 1+\alpha^{2}$ and $\varepsilon \leq \alpha^{2}$. In particular, $\left|\operatorname{Jac} F_{c}(y)\right| \leq 1+\alpha^{2} \leq 1+\alpha$ for all $y \in Y$, if $\delta$ is small enough so that $\alpha$ is less than 1 (we also assume that $\varepsilon$ is small).

As $F_{c}$ has degree one, we have
$$\operatorname{vol}_{g_{0}}(X)=\int_{Y} F_{c}^{*}\left(\mathrm{dv}_{\mathrm{g}_{0}}\right)=\int_{Y} \operatorname{Jac} F_{c}(y) \mathrm{dv}_{\mathrm{g}}(y)$$

Denote by $Y_{\alpha_{1}}$ the set of points $y \in Y$ such that
$$\left|\operatorname{Jac} F_{c}(y)\right| \geq 1-\alpha .$$
We have
$$\begin{aligned}
\operatorname{vol}_{g_{0}}(X) & \leq \int_{Y}\left|\operatorname{Jac} F_{c}(y)\right| \operatorname{dv}_{\mathrm{g}}(y) \\
& =\int_{Y_{\alpha_{1}}}\left|\operatorname{Jac}_{c}(y)\right| \operatorname{dv}_{\mathrm{g}}(y)+\int_{Y \backslash Y_{\alpha_{1}}}\left|\operatorname{Jac} F_{c}(y)\right| \operatorname{dv}_{\mathrm{g}}(y) \\
& \leq\left(1+\alpha^{2}\right) \operatorname{vol}_{g}\left(Y_{\alpha_{1}}\right)+(1-\alpha) \operatorname{vol}_{g}\left(Y \backslash Y_{\alpha_{1}}\right) \\
& =\operatorname{vol}_{g}(Y)+\alpha^{2} \operatorname{vol}_{g}\left(Y_{\alpha_{1}}\right)-\alpha \operatorname{vol}_{g}\left(Y \backslash Y_{\alpha_{1}}\right)
\end{aligned}$$
Then, using the assumption (4) and the inequality (5) on the volume, we get
$$\begin{aligned}
\operatorname{vol}_{g}\left(Y \backslash Y_{\alpha_{1}}\right) & \leq \frac{\operatorname{vol}_{g}(Y)-\operatorname{vol}_{g_{0}}(X)}{\alpha}+\alpha \operatorname{vol}_{g}\left(Y_{\alpha_{1}}\right) \\
& \leq\left(\frac{\varepsilon}{\alpha}+\alpha\right) \operatorname{vol}_{g}(Y) \\
& \leq 2 \alpha \operatorname{vol}_{g}(Y)
\end{aligned}$$
Clearly, $1-2 \alpha \leq\left|\operatorname{Jac} F_{c}(y)\right|$ on $Y_{\alpha_{1}}$ and $\left|\operatorname{Jac} F_{c}(y)\right| \leq 1+2 \alpha$ on $Y$ which proves the lemma with $\alpha_{1}(\varepsilon, \delta)=2 \alpha$. \(\square\)

From this lemma, we deduce that $F_{c}$ is almost injective. Indeed, let $x \in X$, one defines $N\left(F_{c}, x\right) \in \mathbf{N} \cup\{\infty\}$ to be the number of preimages of $x$ by $F_{c}$. As $F_{c}$ has degree one, one has $N\left(F_{c}, x\right) \geq 1$ for all $x \in X$. We then define $X_{1}:=\left\{x \in X, N\left(F_{c}, x\right)=1\right\}$. Observe that $N\left(F_{c}, x\right) \geq 2$ on $X \backslash X_{1}$.

Lemma 3.10. There exists $\alpha_{2}=\alpha_{2}(\varepsilon, \delta)>0$ such that
$$\operatorname{vol}_{g_{0}}\left(X_{1}\right) \geq\left(1-\alpha_{2}\right) \operatorname{vol}_{g_{0}}(X)$$
and
$$\int_{X \backslash X_{1}} N\left(F_{c}, x\right) \mathrm{dv}_{\mathrm{g}_{0}}(x) \leq \alpha_{2}(\varepsilon, \delta) \mathrm{vol}_{g_{0}}(X) .$$
Moreover, $\alpha_{2}(\varepsilon, \delta) \rightarrow 0$ as $\varepsilon$ and $\delta \rightarrow 0$.
In particular, there exists $\alpha^{\prime}>0$ such that $N\left(F_{c}, x\right)=1 \alpha^{\prime}$-ae on $X$.
Proof. One defines
$$\alpha_{2}(\varepsilon, \delta)=2\left(\left(1+\frac{\delta}{n-1}\right)^{n}(1+\varepsilon)-1\right) .$$

From (15) and the area formula (see [14, 3.7]), we have
$$\begin{aligned}
\left(\frac{c}{h\left(g_{0}\right)}\right)^{n} \operatorname{vol}_{g}(Y) & \geq \int_{Y}\left|\operatorname{Jac} F_{c}(y)\right| \mathrm{dv}_{\mathrm{g}}(y) \\
& =\int_{X} N\left(F_{c}, x\right) \mathrm{dv}_{\mathrm{g}_{0}}(x) \\
& =\int_{X_{1}} N\left(F_{c}, x\right) \mathrm{dv}_{\mathrm{g}_{0}}(x)+\int_{X \backslash X_{1}}\left(N\left(F_{c}, x\right)-1+1\right) \mathrm{dv}_{\mathrm{g}_{0}}(x) \\
& =\operatorname{vol}_{g_{0}}(X)+\int_{X \backslash X_{1}}\left(N\left(F_{c}, x\right)-1\right) \mathrm{dv}_{\mathrm{g}_{0}}(x)
\end{aligned}$$
And
$$\begin{aligned}
\operatorname{vol}_{g_{0}}\left(X \backslash X_{1}\right) & \leq \int_{X \backslash X_{1}}\left(N\left(F_{c}, x\right)-1\right) \mathrm{dv}_{\mathrm{g}_{0}}(x) \\
& \leq\left(\frac{c}{h\left(g_{0}\right)}\right)^{n} \operatorname{vol}_{g}(Y)-\operatorname{vol}_{g_{0}}(X) \\
& \leq\left(\left(\frac{c}{h\left(g_{0}\right)}\right)^{n}(1+\varepsilon)-1\right) \operatorname{vol}_{g_{0}}(X) \\
& \leq \frac{\alpha_{2}(\varepsilon, \delta)}{2} \operatorname{vol}_{g_{0}}(X)
\end{aligned}$$
Thus, since $N\left(F_{c}, x\right) \leq 2\left(N\left(F_{c}, x\right)-1\right)$ on $X \backslash X_{1}$, we get
$$\operatorname{vol}_{g_{0}}\left(X \backslash X_{1}\right) \leq \int_{X \backslash X_{1}} N\left(F_{c}, x\right) \mathrm{dv}_{\mathrm{g}_{0}}(x) \leq \alpha_{2}(\varepsilon, \delta) \operatorname{vol}_{g_{0}}(X)$$
and this proves the lemma. \(\square\)

The following lemma says that $d F_{c}(y)$ is almost isometric at points $y$ where $\operatorname{Jac} F_{c}(y)$ is almost equal to 1.

Lemma 3.11. There exists $\alpha_{3}=\alpha_{3}(\varepsilon, \delta)>0$ such that the following holds. Let $Y_{\alpha_{1}}$ be the set of points where (18) holds, that is $1-\alpha_{1}(\varepsilon, \delta) \leq\left|\operatorname{Jac} F_{c}(y)\right|$. Let $y$ be a point in $Y_{\alpha_{1}}$ and $u \in T_{y} Y$, then
$$\left(1-\alpha_{3}\right)\|u\|_{g} \leq\left\|d_{y} F_{c}(u)\right\|_{g_{0}} \leq\left(1+\alpha_{3}\right)\|u\|_{g} .$$
Moreover, $\alpha_{3}(\varepsilon, \delta) \rightarrow 0$ as $\varepsilon, \delta \rightarrow 0$.
Proof. The inequality (15) implies that for all $y \in Y$
$$\left\|H_{y}^{c}-\frac{1}{n} \operatorname{Id}\right\|^{2} \leq \frac{1}{A}\left(1-\frac{\left|\operatorname{Jac} F_{c}(y)\right|}{\left(1+\frac{\delta}{n-1}\right)^{n}}\right) .$$
Let us define
$$\beta_{1}=\beta_{1}(\varepsilon, \delta)=\frac{1}{A^{1 / 2}}\left(1-\frac{1-\alpha_{1}(\varepsilon, \delta)}{\left(1+\frac{\delta}{n-1}\right)^{n}}\right)^{1 / 2} .$$
where $\alpha_{1}(\varepsilon, \delta)$ is the constant from Lemma 3.9. Clearly, $\beta_{1}(\varepsilon, \delta) \rightarrow 0$ as $\varepsilon$ and $\delta \rightarrow 0$. Let $Y_{\alpha_{1}}$ be the set of points where (18) holds. On $Y_{\alpha_{1}}$, one has
$$\left\|H_{y}^{c}-\frac{\mathrm{Id}}{n}\right\|^{2} \leq \beta_{1}^{2} .$$
Let $\left\{u_{i}\right\}_{i=1, \ldots, n}$ be an orthonormal basis of $T_{y} Y$ and $v_{i}=d_{y} F\left(u_{i}\right)$. Writing $\mathrm{Id}-H_{y}^{c}=$ $\frac{n-1}{n} \mathrm{Id}+\frac{1}{n} \mathrm{Id}-H_{y}^{c}$, one gets
$$\begin{aligned}
\left|g_{0}\left(\left(\operatorname{Id}-H_{y}^{c}\right) d_{y} F_{c}\left(u_{i}\right), d_{y} F_{c}\left(u_{i}\right)\right)\right| & \geq\left|g_{0}\left(\left(\frac{n-1}{n} \operatorname{Id}\right) d_{y} F_{c}\left(u_{i}\right), d_{y} F_{c}\left(u_{i}\right)\right)\right| \\
& -\left|g_{0}\left(\left(\frac{1}{n} \operatorname{Id}-H_{y}^{c}\right) d_{y} F_{c}\left(u_{i}\right), d_{y} F_{c}\left(u_{i}\right)\right)\right| \\
& \geq \frac{n-1}{n}\left\|d_{y} F_{c}\left(u_{i}\right)\right\|_{g_{0}}^{2}-\left\|\frac{1}{n} \operatorname{Id}-H_{y}^{c}\right\| .\left\|d_{y} F_{c}\left(u_{i}\right)\right\|_{g_{0}}^{2} \\
& \geq\left(\frac{n-1}{n}-\beta_{1}\right)\left\|d_{y} F_{c}\left(u_{i}\right)\right\|_{g_{0}}^{2}
\end{aligned}$$
Writing $H_{y}^{c}=\frac{1}{n} \mathrm{Id}+H_{y}^{c}-\frac{1}{n} \mathrm{Id}$, one has
$$\begin{aligned}
g_{0}\left(H_{y}^{c} d_{y} F_{c}\left(u_{i}\right), d_{y} F_{c}\left(u_{i}\right)\right)^{1 / 2} \leq & g_{0}\left(\left(\frac{1}{n} \operatorname{Id}\right) d_{y} F_{c}\left(u_{i}\right), d_{y} F_{c}\left(u_{i}\right)\right)^{1 / 2} \\
& +\left|g_{0}\left(\left(H_{y}^{c}-\frac{1}{n} \operatorname{Id}\right) d_{y} F_{c}\left(u_{i}\right), d_{y} F_{c}\left(u_{i}\right)\right)\right|^{1 / 2} \\
& \leq\left(\frac{1}{\sqrt{n}}+\beta_{1}^{1 / 2}\right)\left\|d_{y} F_{c}\left(u_{i}\right)\right\|_{g_{0}} .
\end{aligned}$$
Taking the trace of the right hand side of (13) and using the Cauchy-Schwarz inequality, one has
$$\begin{aligned}
\sum_{i=1}^{n} g_{0}\left(H_{y}^{c} d_{y} F_{c}\left(u_{i}\right), d_{y} F_{c}\left(u_{i}\right)\right)^{1 / 2} g\left(H_{y}^{\prime c}\left(u_{i}\right), u_{i}\right)^{1 / 2} & \leq\left(\frac{1}{\sqrt{n}}+\beta_{1}^{1 / 2}\right)\left(\sum_{i=1}^{n}\left\|d_{y} F_{c}\left(u_{i}\right)\right\|_{g_{0}}^{2}\right)^{1 / 2} \\
& \times\left(\sum_{i=1}^{n} g\left(H_{y}^{\prime c}\left(u_{i}\right), u_{i}\right)\right)^{1 / 2} \\
& =\left(\frac{1}{\sqrt{n}}+\beta_{1}^{1 / 2}\right)\left(\sum_{i=1}^{n}\left\|d_{y} F_{c}\left(u_{i}\right)\right\|_{g_{0}}^{2}\right)^{1 / 2}
\end{aligned}$$
By (13), the trace of (42) is not greater than the right hand side of (46) multiplied by $c$, hence
$$\left(\frac{n-1}{n}-\beta_{1}\right) \sum_{i=1}^{n}\left\|d_{y} F_{c}\left(u_{i}\right)\right\|_{g_{0}}^{2} \leq c\left(\frac{1}{\sqrt{n}}+\beta_{1}^{1 / 2}\right)\left(\sum_{i=1}^{n}\left\|d_{y} F_{c}\left(u_{i}\right)\right\|_{g_{0}}^{2}\right)^{1 / 2},$$
and
$$\left(\sum_{i=1}^{n}\left\|d_{y} F_{c}\left(u_{i}\right)\right\|_{g_{0}}^{2}\right)^{1 / 2} \leq c \frac{\frac{1}{\sqrt{n}}+\beta_{1}^{1 / 2}}{\frac{n-1}{n}-\beta_{1}} \leq \sqrt{n}\left(1+\frac{\delta}{n-1}\right) \frac{1+\sqrt{n} \beta_{1}^{1 / 2}}{1-\frac{n}{n-1} \beta_{1}} .$$
Let us define
$$\beta_{2}:=\beta_{2}(\varepsilon, \delta)=\left(1+\frac{\delta}{n-1}\right)^{2}\left(\frac{1+\sqrt{n} \beta_{1}^{1 / 2}}{1-\frac{n}{n-1} \beta_{1}}\right)^{2}-1 .$$
Clearly, $\beta_{2}(\varepsilon, \delta) \rightarrow 0$ as $\varepsilon$ and $\delta \rightarrow 0$. One has
$$\sum_{i=1}^{n}\left\|d_{y} F_{c}\left(u_{i}\right)\right\|_{g_{0}}^{2} \leq n\left(1+\beta_{2}\right) .$$
Let $L$ be the endomorphism of $T_{y} Y$ defined by $L=\left(d_{y} F_{c}\right)^{*} \circ d_{y} F_{c}$. We have
$$\operatorname{trace}(L)=\sum_{i=1}^{n} g\left(L\left(u_{i}\right), u_{i}\right)=\sum_{i=1}^{n} g\left(d_{y} F_{c}\left(u_{i}\right), d_{y} F_{c}\left(u_{i}\right)\right) \leq n\left(1+\beta_{2}\right) .$$
On the other hand
$$|1-\alpha|^{2} \leq\left|\operatorname{Jac} F_{c}(y)\right|^{2}=\operatorname{det}(L) \leq\left(\frac{\operatorname{trace}(L)}{n}\right)^{n} \leq\left(1+\beta_{2}\right)^{n},$$
which shows that there is almost equality in the arithmetico-geometric inequality. We then get that there exists some $\alpha_{3}(\varepsilon, \delta)>0$, with $\alpha_{3}(\varepsilon, \delta) \rightarrow 0$ as $\varepsilon, \delta \rightarrow 0$, such that
$$\|L-I d\| \leq \alpha_{3}(\varepsilon, \delta) .$$
Thus for any $y \in Y_{\alpha_{1}}$ and $u \in T_{y} Y$
$$\left(1-\alpha_{3}\right)\|u\| \leq\left\|d_{y} F_{c}(u)\right\|_{g_{0}} \leq\left(1+\alpha_{3}\right)\|u\|$$
and $d_{y} F_{c}$ is almost isometric. \(\square\)

We now prove that given a fixed radius $R>0$, the natural maps $F_{c}$ have uniformly bounded differential $d F_{c}$ on $B\left(y_{g}, R\right)$ if the parameters $\varepsilon, \delta$ are sufficiently small. Recall that the point $y_{g}$ has been chosen such that (8) holds, namely $\operatorname{vol}_{g}\left(B\left(y_{g}, 1\right)\right) \geq v_{n}$.

Lemma 3.12. Let $R>0$, then there exist $\varepsilon(R)>0$ and $\delta(R)>0$ such that for any $0<\varepsilon<\varepsilon(R)$ and $0<\delta<\delta(R)$, and for any $y \in B\left(y_{g}, R\right)$,
$$\left\|d_{y} F_{c}\right\| \leq 2 \sqrt{n}$$
Proof. We first prove that for all $y \in Y,\left\|d_{y} F_{c}\right\|$ is bounded from above by $\lambda_{n}^{c}(y)$, the maximal eigenvalue of $H_{y}^{c}$ (see Definition 3.4 ). Recall that $0<\lambda_{n}^{c}<1$. Let $u$ be a unit vector in $T_{y} \tilde{Y}$ and $v=d_{y} F_{c}(u)$. Equation(13) gives
$$\left(1-\lambda_{n}^{c}(y)\right)\left|g_{0}\left(d_{y} F_{c}(u), d_{y} F_{c}(u)\right)\right| \leq c \lambda_{n}^{c}(y)^{1 / 2} g_{0}\left(d_{y} F_{c}(u), d_{y} F_{c}(u)\right)^{1 / 2}$$
hence
$$\left\|d_{y} F_{c}(u)\right\|_{g_{0}} \leq \frac{c \sqrt{\lambda_{n}^{c}(y)}}{1-\lambda_{n}^{c}(y)} .$$
We thus have to show that $\lambda_{n}^{c}(y)$ is not close to 1 . More precisely, let $\beta>0$ such that $\frac{1}{n}+\beta<1$, one then defines
$$\gamma(\delta, \beta):=\left(\frac{n-1+\delta}{n-1-n \beta}\right) \sqrt{1+n \beta}-1>0 .$$
Clearly, $\gamma(\beta, \delta) \rightarrow 0$ as $\delta, \beta \rightarrow 0$. One can check that if $\lambda_{n}^{c}(y) \leq \frac{1}{n}+\beta$, then $\left\|d_{y} F_{c}(u)\right\|_{g_{0}} \leq$ $\sqrt{n}(1+\gamma)$. For our purpose, we may suppose that $\gamma \leq 1$. Now let $\delta_{n}>0$ and $\beta_{n}>0$ be such that if $0<\delta \leq 10 \delta_{n}$ and $0<\beta \leq 10 \beta_{n}$, then $\gamma(\delta, \beta) \leq 1$. Moreover we define $\varepsilon_{n}>0$ such that if $0<\varepsilon<\varepsilon_{n}$ and $0<\delta \leq 10 \delta_{n}$ then, with the notations (38) of Lemma $3.11 \beta_{1}(\varepsilon, \delta) \leq \beta_{n}$. In what follows, we suppose $\varepsilon$ and $\delta$ sufficiently small.
By (39) we have that $\left|\lambda_{n}^{c}(y)-\frac{1}{n}\right| \leq \beta_{1}(\varepsilon, \delta)$ on $Y_{\alpha_{1}}$. Recall that $Y_{\alpha_{1}}$ has a large relative volume in $Y$. The idea is first to estimate $\lambda_{n}^{c}$ on a neighbourhood of $Y_{\alpha_{1}}$ and then to show that this neighbourhood contains $B\left(y_{g}, R\right)$ if the parameters $\varepsilon$ and $\delta$ are sufficiently small relatively to $R$.

For this purpose we need to estimate the variation of $\lambda_{n}^{c}$. Recall that $H_{y}^{c}$ is defined by
$$g_{0}\left(H_{y}^{c}(u), v\right)=\int_{\partial \tilde{X}} d B_{\left(F_{c}(y), \theta\right)}(u) d B_{\left(F_{c}(y), \theta\right)}(v) d \sigma_{y}^{c}(\theta) .$$
Let $U, V$ be parallel vector fields near $F_{c}(y)$ extending unit tangent vectors at $F_{c}(y)$, $u$ and $v$. We compute the derivative of $g_{0}\left(H_{y}^{c}(U), V\right)$ in a direction $w \in T_{y} Y$ :
$$\begin{aligned}
& w . g_{0}\left(H_{y}^{c}(U), V\right)=\int_{\partial \tilde{X}} D d B_{\left(F_{c}(y), \theta\right)}\left(d_{y} F(w), U\right) d B_{\left(F_{c}(y), \theta\right)}(V) d \sigma_{y}^{c}(\theta)+ \\
& \quad \int_{\partial \tilde{X}} d B_{\left(F_{c}(y), \theta\right)}(U) D d B_{\left(F_{c}(y), \theta\right)}\left(d_{y} F(w), V\right) d \sigma_{y}^{c}(\theta)+\int_{\partial \tilde{X}} d B_{\left(F_{c}(y), \theta\right)}(U) d B_{\left(F_{c}(y), \theta\right)}(V) w . d \sigma_{y}^{c}(\theta)
\end{aligned}$$
The Buseman functions of the hyperbolic space satisfies $\|D d B\| \leq 1$ and $\|d B\| \leq 1$ and thus
$$\left|w \cdot g_{0}\left(H_{y}^{c}(U), V\right)\right| \leq 2\left\|d_{y} F_{c}(w)\right\|_{g_{0}}+\left|\int_{\partial \tilde{X}} w \cdot d \sigma_{y}^{c}(\theta)\right| .$$
Recall that
$$d \sigma_{y}^{c}(\theta)=\frac{d \mu_{y}^{c}(\theta)}{\mu_{y}^{c}(\partial \tilde{X})}=\frac{\int_{\tilde{Y}} p(\tilde{f}(z), \theta) e^{-c \rho(y, z)} \mathrm{dv}_{\tilde{\mathrm{g}}}(z)}{\int_{\tilde{Y}} e^{-c \rho(y, z)} \mathrm{dv}_{\tilde{\mathrm{g}}}(z)} d \theta .$$
Differentiating this formula yields
$$\begin{array}{r}
w . d \sigma_{y}^{c}(\theta)=\frac{\int_{\tilde{Y}} p(\tilde{f}(z), \theta)\left(-c . d \rho_{(y, z)}(w)\right) e^{-c \rho(y, z)} \mathrm{dv}_{\tilde{\mathrm{g}}}(z)}{\mu_{y}^{c}(\partial \tilde{X})} d \theta- \\
\frac{d \mu_{y}^{c}(\theta)}{\mu_{y}^{c}(\partial \tilde{X})^{2}} \cdot \int_{\tilde{Y}}\left(-c . d \rho_{(y, z)}(w)\right) e^{-c \rho(y, z)} \mathrm{dv}_{\tilde{\mathrm{g}}}(z) .
\end{array}$$

Since $\left|d \rho_{(y, z)}(w)\right| \leq\|w\|_{g}$, we have
$$\left|\int_{\partial \tilde{X}} w \cdot d \sigma_{y}^{c}(\theta)\right| \leq \int_{\partial \tilde{X}} 2 c\|w\|_{g} d \sigma_{y}^{c}(\theta)=2 c\|w\|_{g}$$
we gives that, $\left|w . g_{0}\left(H_{y}^{c}(U), V\right)\right| \leq 2\left\|d_{y} F_{c}(w)\right\|_{g_{0}}+2 c\|w\|_{g}$. If $w$ is a unit vector, (51) yields
$$\left|w \cdot g_{0}\left(H_{y}^{c}(U), V\right)\right| \leq 2 c\left(\frac{\sqrt{\lambda_{n}^{c}(y)}}{1-\lambda_{n}^{c}(y)}+1\right) .$$
Let us now consider small constants $\eta>\beta>0$ and define
$$r(\delta, \beta, \eta):=\frac{\eta-\beta}{2(n-1+\delta)\left(\frac{\sqrt{\frac{1}{n}+\eta}}{1-\left(\frac{1}{n}+\eta\right)}+1\right)}>0 .$$
Our goal is to prove that
$$\inf \left\{d\left(y_{0}, y_{1}\right) \mid y_{0}, y_{1} \in Y, \lambda_{n}^{c}\left(y_{0}\right) \leq \frac{1}{n}+\beta, \lambda_{n}^{c}\left(y_{1}\right) \geq \frac{1}{n}+\eta\right\} \geq r(\delta, \beta, \eta) .$$
Let $y_{0} \in Y$ so that $\lambda_{n}^{c}\left(y_{0}\right) \leq \frac{1}{n}+\beta$. Assume that there exists $y \in Y$ such that $\lambda_{n}^{c}(y) \geq \frac{1}{n}+\eta$. One defines
$$r:=\inf \left\{d\left(y_{0}, y\right) \mid y \in Y, \lambda_{n}^{c}(y) \geq \frac{1}{n}+\eta\right\} .$$
By continuity, there exists $y_{1} \in Y$ such that $\lambda_{n}^{c}\left(y_{1}\right)=\frac{1}{n}+\eta$ and $d\left(y_{0}, y_{1}\right)=r$. Let $\gamma:[0, r] \longrightarrow Y$ be a minimising geodesic from $y_{0}$ to $y_{1}$. We easily see that $\lambda_{n}^{c}(\gamma(t))<\frac{1}{n}+\eta$ for any $0 \leq t<r$. Let $U(t)$ be a parallel vector field in $X$ along $F_{c}(\gamma)$ such that $U(r)$ is a unit eigenvector of $H_{y_{1}}^{c}$. Then, using (55) with $\dot{\gamma} \cdot g_{0}\left(H_{\gamma(t)}^{c} U(t), U(t)\right)=\frac{d}{d t} g_{0}\left(H_{\gamma(t)}^{c} U(t), U(t)\right)$, one has
$$\begin{aligned}
\left|\lambda_{n}^{c}\left(y_{1}\right)-\lambda_{n}^{c}\left(y_{0}\right)\right| & \leq\left|g_{0}\left(H_{\gamma(r)}^{c} U(r), U(r)\right)-g_{0}\left(H_{\gamma(0)}^{c} U(0), U(0)\right)\right| \\
& =\left|\int_{0}^{r} \frac{d}{d t} g_{0}\left(H_{\gamma(t)}^{c} U(t), U(t)\right) d t\right| \\
& \leq 2 c \int_{0}^{r}\left(\frac{\sqrt{\lambda_{n}^{c}(\gamma(t))}}{1-\lambda_{n}^{c}(\gamma(t))}+1\right) d t \\
& \leq 2 c r\left(\frac{\sqrt{\frac{1}{n}+\eta}}{1-\left(\frac{1}{n}+\eta\right)}+1\right) .
\end{aligned}$$
As a consequence
$$r \geq \frac{\eta-\beta}{2(n-1+\delta)\left(\frac{\sqrt{\frac{1}{n}+\eta}}{1-\left(\frac{1}{n}+\eta\right)}+1\right)}=r(\delta, \beta, \eta)$$

We now set $\eta=2 \beta_{n}$ so that $\gamma(\delta, \eta) \leq 1$ for any $\delta \leq \delta_{n}$. One then defines $r_{n}:=r\left(\delta_{n}, \beta_{n}, 2 \beta_{n}\right)$. Let us recall that for $\varepsilon \leq \varepsilon_{n}$ and $\delta \leq \delta_{n}$, we have $\beta_{1}(\varepsilon, \delta) \leq \beta_{n}$. On $Y_{\alpha_{1}}$, one has $\lambda_{n}^{c}(y) \leq \frac{1}{n}+\beta_{1}(\varepsilon, \delta) \leq \frac{1}{n}+\beta_{n}$. Hence, if $\lambda_{n}^{c}\left(y_{1}\right) \geq \frac{1}{n}+2 \beta_{n}$, one has
$$d\left(y_{1}, Y_{\alpha_{1}}\right) \geq r\left(\delta, \beta_{1}(\varepsilon, \delta), 2 \beta_{n}\right) \geq r\left(\delta_{n}, \beta_{n}, 2 \beta_{n}\right)=r_{n} .$$
We thus have proved that in the $r_{n}$-neighbourhood of $Y_{\alpha_{1}}$, one has $\lambda_{n}^{c}(y) \leq \frac{1}{n}+2 \beta_{n}$. This implies that
$$\left\|d_{y} F_{c}\right\| \leq\left(1+\gamma\left(\delta, 2 \beta_{n}\right)\right) \sqrt{n} \leq 2 \sqrt{n} .$$
Let us denote by $V_{r_{n}}\left(Y_{\alpha_{1}}\right)$ the $r_{n}$-neighbourhood of $Y_{\alpha_{1}}$. It remains to show that $B\left(y_{g}, R\right) \subset V_{r_{n}}\left(Y_{\alpha_{1}}\right)$, if $\varepsilon \leq \varepsilon(R)$ and $\delta \leq \delta(R)$. Let us recall that $\frac{\operatorname{vol}_{g}\left(Y_{\alpha_{1}}\right)}{\operatorname{vol}_{g}(Y)} \geq 1-\alpha_{1}$, hence
$$\operatorname{vol}_{g}\left(Y \backslash Y_{\alpha_{1}}\right) \leq \alpha_{1} \operatorname{vol}_{g}(Y) \leq \alpha_{1}(1+\varepsilon) \operatorname{vol}_{g_{0}}(X):=v(\varepsilon, \delta) .$$
Clearly, $v(\varepsilon, \delta) \rightarrow 0$ when $\varepsilon, \delta \rightarrow 0$. On the other hand, by (11) for any $y \in B\left(y_{g}, R\right)$ we have
$$\operatorname{vol}_{g}\left(B_{g}\left(y, r_{0}\right)\right) \geq v_{n} \frac{\operatorname{vol}_{\mathbf{H}^{n}}\left(\mathrm{~B}_{\mathbf{H}^{n}}\left(\mathrm{r}_{0}\right)\right)}{\operatorname{vol}_{\mathbf{H}^{n}}\left(\mathrm{~B}_{\mathbf{H}^{n}}\left(1+\mathrm{R}+\mathrm{r}_{0}\right)\right)}:=v_{0}(R)>0 .$$
If $v_{0}(R)>v(\varepsilon, \delta)$, then for any $y \in B\left(y_{g}, R\right)$ one has $B_{g}\left(y, r_{n}\right) \not \subset Y \backslash Y_{\alpha_{1}}$, which means that $B_{g}\left(y, r_{n}\right)$ intersects $Y_{\alpha_{1}}$. This shows that $d\left(y, Y_{\alpha_{1}}\right)<r_{n}$ and $y \in V_{r_{n}}\left(Y_{\alpha_{1}}\right)$.
The lemma is proved if we define $\varepsilon=\varepsilon(R)>0$ and $\delta=\delta(R)>0$ to be sufficiently small constants such that $v(\varepsilon, \delta)<v_{0}(R)$. \(\square\)

We now prove that $F_{c}$ is almost 1-lipschitz.
Lemma 3.13. For any fixed $R>0$, there exists $\varepsilon_{2}(R)>0$ and $\delta_{2}(R)>0$ such that for every $0<\varepsilon<\varepsilon_{2}(R)$ and $0<\delta<\delta_{2}(R)$, there exists $\kappa=\kappa(\varepsilon, \delta, R)>0$ such that on $B_{g}\left(y_{g}, R\right)$ :
$$d_{g_{0}}\left(F_{c}\left(y_{1}\right), F_{c}\left(y_{2}\right)\right) \leq(1+\kappa) d_{g}\left(y_{1}, y_{2}\right)+\kappa .$$
Moreover, $\kappa(\varepsilon, \delta, R) \rightarrow 0$ as $\varepsilon, \delta \rightarrow 0$.
Proof. The idea goes as follows. We have proved that $d_{y} F_{c}$ is almost isometric on $Y_{\alpha_{1}}$. On the other hand, $\left\|d_{y} F_{c}\right\|$ is uniformly bounded in $B\left(y_{g}, R\right)$ if the parameters $\varepsilon$ and $\delta$ are chosen sufficiently small. To prove the lemma one computes the lengths of $F_{c}(\gamma)$ where $\gamma$ is a minimising geodesic in $B\left(y_{g}, R\right)$ whose intersection with $Y_{\alpha_{1}}$ is large. Existence of such geodesics follows from an integral geometry lemma due to T. Colding.

Fix some $R>0$. We define the following constants :
If $d>0$,
$$c_{1}(n, d):=\sup _{0<s / 2<r<s<d} \frac{\operatorname{vol}_{\mathbf{H}^{n}}\left(\partial B_{\mathbf{H}^{n}}(s)\right)}{\operatorname{vol}_{\mathbf{H}^{n}}\left(\partial B_{\mathbf{H}^{n}}(r)\right)} .$$
If $\tau>0, R>0$,
$$c_{2}(n, \tau, R):=c_{1}(n, 2 R)\left(2 \tau \operatorname{vol}_{\mathbf{H}^{n}}\left(\mathrm{~B}_{\mathbf{H}^{\mathrm{n}}}(\tau)\right) .\right.$$

If $\varepsilon>0, \delta>0$,
$$\theta(\varepsilon, \delta):=2 \alpha_{3}^{2}(\varepsilon, \delta) \operatorname{vol}_{g_{0}}(X)+2(4 n+1) \alpha_{1}(\varepsilon, \delta) \operatorname{vol}_{g_{0}}(X) .$$
Clearly, $\theta(\varepsilon, \delta) \rightarrow 0$ as $\varepsilon, \delta \rightarrow 0$.
Let $\tau(\varepsilon, \delta, R)>0$ be the function implicitely defined by
$$\operatorname{vol}_{\mathbf{H}^{n}}(\tau) \tau:=\theta(\varepsilon, \delta) \frac{2 c_{1}(n, 2 R) \operatorname{vol}_{\mathbf{H}^{n}}(1+R+1)^{2}}{v_{n}^{2}} .$$
Again, we easily see that, for fixed $R, \tau(\varepsilon, \delta, R) \rightarrow 0$ as $\varepsilon, \delta \rightarrow 0$. We also choose $\varepsilon_{2}(R)>0$ and $\delta_{2}(R)>0$ such that $\varepsilon_{2}(R) \leq \varepsilon(2 R), \delta_{2}(R)<\delta(2 R)$ and such that, if $0<\varepsilon \leq \varepsilon_{2}(R)$ and $0<\delta<\delta_{2}(R)$, then $\tau(\varepsilon, \delta, R) \ll 1$.
Finally, one defines $\kappa(\varepsilon, \delta, R):=\max (2 \sqrt{n} \sqrt{\tau}, 8 \sqrt{\tau})$. From the remarks above we can choose $\varepsilon_{2}(R)$ and $\delta_{2}(R)$ so that $\kappa(\varepsilon, \delta, R)<1 / R$ (for $0<\varepsilon \leq \varepsilon_{2}(R), 0<\delta<\delta_{2}(R)$ and $R$ big).

There are two cases.
Case i) Let $y_{1}, y_{2}$ in $B_{g}\left(y_{g}, R\right)$ such that $d\left(y_{1}, y_{2}\right) \leq \sqrt{\tau}$. Using (49), if $0<\varepsilon<\varepsilon(2 R)$, $0<\delta<\delta(2 R)$ one has
$$d\left(F_{c}\left(y_{1}\right), F_{c}\left(y_{2}\right)\right) \leq 2 \sqrt{n} \sqrt{\tau} \leq \kappa .$$

Case ii) : Let $y_{1}, y_{2}$ in $B_{g}\left(y_{g}, R\right)$ such that $d\left(y_{1}, y_{2}\right) \geq \sqrt{\tau}$. We will use the following theorem, due to J. Cheeger and T. Colding, cf. [9, Theorem 2.11] that we describe now in a particular case. We keep the notations of [9].
Let us define $A_{1}=B_{g}\left(y_{1}, \tau\right), A_{2}=B_{g}\left(y_{2}, \tau\right)$ and $W=B_{g}\left(y_{g}, 2 R\right)$ where $y_{1}$ and $y_{2}$ are points as above sitting on a complete riemannian manifold $(Y, g)$ with $\operatorname{Ric}_{g} \geq-(n-1) g$. For any $z_{1} \in A_{1}$ and any unit vector $v_{1} \in T_{z_{1}} Y$, the set $I\left(z_{1}, v_{1}\right)$ defined by
$$I\left(z_{1}, v_{1}\right)=\left\{t \mid \gamma(t) \in A_{2}, \gamma_{\mid[0, t]} \text { is minimal }, \gamma^{\prime}(0)=v_{1}\right\}$$
has a measure $\left|I\left(z_{1}, v_{1}\right)\right|$ bounded above by $2 \tau$. Thus
$$D\left(A_{1}, A_{2}\right):=\sup _{z_{1}, v_{1}}\left|I\left(z_{1}, v_{1}\right)\right| \leq 2 \tau,$$
and similarly, $D\left(A_{2}, A_{1}\right) \leq 2 \tau$. For any $z_{1} \in A_{1}$ and $z_{2} \in A_{2}$, let $\gamma_{z_{1} z_{2}}$ be a minimizing geodesic from $z_{1}$ to $z_{2}$. Clearly, $\gamma \subset B\left(y_{g}, 2 R\right)$. Then, by [9, Theorem 2.11], we have for any non negative integrable function $e$ defined on $Y$,
$$\begin{gathered}
\int_{A_{1} \times A_{2}} \int_{0}^{d\left(z_{1}, z_{2}\right)} e\left(\gamma_{z_{1}, z_{2}}\right)(s) d s \leq c_{1}(n, 2 R)\left(D\left(A_{1}, A_{2}\right) \operatorname{vol}\left(A_{1}\right)+D\left(A_{2}, A_{1}\right) \operatorname{vol}\left(A_{2}\right)\right) \\
\times \int_{W} e(y) \operatorname{dv}_{\mathrm{g}}(y)
\end{gathered}$$

By Bishop's Theorem, for $i=1,2$ we have
$$\operatorname{vol}_{g}\left(A_{i}\right) \leq \operatorname{vol}_{\mathbf{H}^{n}}\left(\mathrm{~B}_{\mathbf{H}^{\mathrm{n}}}(\tau)\right),$$
and thus
$$c_{1}(n, 2 R)\left(D\left(A_{1}, A_{2}\right) \operatorname{vol}\left(A_{1}\right)+D\left(A_{2}, A_{1}\right) \operatorname{vol}\left(A_{2}\right)\right) \leq c_{2}(n, \tau, R) .$$
Therefore, applying (63) to the function
$$e(y)=\sup _{u \in U_{y} Y}\left(\left\|d_{y} F_{c}(u)\right\|-\|u\|\right)^{2}$$
and using (37) on $W \cap Y_{\alpha_{1}}$ and (49) on $W \backslash Y_{\alpha_{1}}$, we get
$$\begin{aligned}
\int_{A_{1} \times A_{2}} \int_{0}^{d\left(z_{1}, z_{2}\right)} e\left(\gamma_{z_{1}, z_{2}}\right)(s) d s & \leq c_{2}(n, \tau, R)\left(\int_{W \cap Y_{\alpha_{1}}} e(y) \mathrm{dv}_{\mathrm{g}}(y)+\int_{W \backslash Y_{\alpha_{1}}} e(y) \mathrm{dv}_{\mathrm{g}}(y)\right) \\
& \leq c_{2}(n, \tau, R)\left(\alpha_{3}^{2} \cdot \operatorname{vol}_{g}(Y)+(4 n+1) \operatorname{vol}_{g}\left(Y \backslash Y_{\alpha_{1}}\right)\right) \\
& \leq c_{2}(n, \tau, R) \theta(\varepsilon, \delta)
\end{aligned}$$
Now, if we denote by $\gamma:=\gamma_{z_{1} z_{2}}$, we have
$$\begin{aligned}
\left|\ell\left(F_{c} \circ \gamma\right)-\ell(\gamma)\right| & =\left|\int_{0}^{d\left(z_{1}, z_{2}\right)}\left\|d_{\gamma(s)} F_{c}(\dot{\gamma})\right\|-\|\dot{\gamma}\| d s\right| \\
& \leq \int_{0}^{d\left(z_{1}, z_{2}\right)} \sup _{u \in T_{y} Y}\left|\left\|d_{\gamma(s)} F_{c}(u)\right\|-\|u\|\right| d s
\end{aligned}$$
Using Cauchy-Schwarz inequality we have
$$\begin{aligned}
\frac{\left|\ell\left(F_{c} \circ \gamma\right)-\ell(\gamma)\right|^{2}}{d\left(z_{1}, z_{2}\right)} & \leq \frac{\left(\int_{0}^{d\left(z_{1}, z_{2}\right)} \sup _{u}\left|\left\|d_{\gamma(s)} F_{c}(u)\right\|-\|u\|\right| d s\right)^{2}}{d\left(z_{1}, z_{2}\right)} \\
& \leq \int_{0}^{d\left(z_{1}, z_{2}\right)} e(\gamma(s)) d s
\end{aligned}$$
Integrating on $A_{1} \times A_{2}$, we deduce from (64) that
$$\int_{A_{1} \times A_{2}} \frac{\left|\ell\left(F_{c} \circ \gamma_{z_{1} z_{2}}\right)-\ell\left(\gamma_{z_{1} z_{2}}\right)\right|^{2}}{d\left(z_{1}, z_{2}\right)} \mathrm{dv}_{\mathrm{g}}\left(z_{1}\right) \mathrm{dv}_{\mathrm{g}}\left(z_{2}\right) \leq c_{2}(n, \tau, R) \theta(\varepsilon, \delta) .$$
By (11), for $i=1,2$ one has
$$\operatorname{vol}_{g}\left(A_{i}\right) \geq v_{n} \frac{\operatorname{vol}_{\mathbf{H}^{n}}\left(\mathrm{~B}_{\mathbf{H}^{n}}(\tau)\right)}{\operatorname{vol}_{\mathbf{H}^{n}}\left(\mathrm{~B}_{\mathbf{H}^{n}}(1+\mathrm{R}+\tau)\right)}:=v_{0}(\tau, R)>0 .$$
From the obvious inequality
$$c_{2}(n, \tau, R) \theta(\varepsilon, \delta) \leq \frac{1}{v_{0}(\tau, R)^{2}} \int_{A_{1} \times A_{2}} c_{2}(n, \tau, R) \theta(\varepsilon, \delta) \mathrm{dv}_{\mathrm{g}}\left(z_{1}\right) \mathrm{dv}_{\mathrm{g}}\left(z_{2}\right) .$$

We get
$$\int_{A_{1} \times A_{2}} \frac{\left|\ell\left(F_{c} \circ \gamma_{z_{1} z_{2}}\right)-\ell\left(\gamma_{z_{1} z_{2}}\right)\right|^{2}}{d\left(z_{1}, z_{2}\right)} \leq \int_{A_{1} \times A_{2}} \frac{c_{2}(n, \tau, R) \theta(\varepsilon, \delta)}{v_{0}(\tau, R)^{2}} .$$
As a consequence there exist $z_{1} \in A_{1}$ and $z_{2} \in A_{2}$ such that
$$\left|\ell\left(F_{c} \circ \gamma_{z_{1} z_{2}}\right)-\ell\left(\gamma_{z_{1} z_{2}}\right)\right|^{2} \leq d\left(z_{1}, z_{2}\right) \frac{c_{2}(n, \tau, R) \theta(\varepsilon, \delta)}{v_{0}(\tau, R)^{2}} .$$
On the other hand one can check that by definition of $\tau$,
$$\frac{c_{2}(n, \tau, R) \theta(\varepsilon, \delta)}{v_{0}(\tau, R)^{2}}=\theta(\varepsilon, \delta) \frac{2 c_{1}(n, 2 R) \operatorname{vol}_{\mathbf{H}^{n}}(1+R+1)^{2}}{v_{n}^{2} \operatorname{vol}_{\mathbf{H}^{n}}(\tau)} \tau=\tau^{2} .$$
This yields
$$\left|\ell\left(F_{c} \circ \gamma_{z_{1} z_{2}}\right)-\ell\left(\gamma_{z_{1} z_{2}}\right)\right|^{2} \leq d\left(z_{1}, z_{2}\right) \tau^{2},$$
and
$$d\left(F_{c}\left(z_{1}\right), F_{c}\left(z_{2}\right)\right) \leq \ell\left(F_{c} \circ \gamma_{z_{1} z_{2}}\right) \leq d\left(z_{1}, z_{2}\right)+\tau \sqrt{d\left(z_{1}, z_{2}\right)} .$$
Since $d\left(y_{i}, z_{i}\right)<\tau$ and $d\left(y_{1}, y_{2}\right) \geq \sqrt{\tau}$, we have
$$d\left(z_{1}, z_{2}\right) \leq d\left(y_{1}, y_{2}\right)+2 \tau \leq d\left(y_{1}, y_{2}\right)(1+2 \sqrt{\tau}) .$$
With our choice of $\tau$ very small compared to 1, we also have
$$d\left(z_{1}, z_{2}\right) \geq d\left(y_{1}, y_{2}\right)-2 \tau \geq \frac{\sqrt{\tau}}{2} .$$
We then have
$$\begin{aligned}
d\left(F_{c}\left(y_{1}\right), F_{c}\left(y_{2}\right)\right) & \leq d\left(F_{c}\left(y_{1}\right), F_{c}\left(z_{1}\right)\right)+d\left(F_{c}\left(z_{1}\right), F_{c}\left(z_{2}\right)\right)+d\left(F_{c}\left(z_{2}\right), F_{c}\left(y_{2}\right)\right) \\
& \leq 2 \sqrt{n} \tau+d\left(z_{1}, z_{2}\right)+\tau\left(d\left(z_{1}, z_{2}\right)\right)^{1 / 2}+2 \sqrt{n} \tau \\
& \leq 4 \sqrt{n} \tau+d\left(y_{1}, y_{2}\right) \frac{d\left(z_{1}, z_{2}\right)}{d\left(y_{1}, y_{2}\right)}\left(1+\tau\left(d\left(z_{1}, z_{2}\right)\right)^{-1 / 2}\right) \\
& \leq 4 \sqrt{n} \tau+d\left(y_{1}, y_{2}\right)(1+2 \sqrt{\tau})\left(1+\sqrt{2} \tau^{3 / 4}\right) \\
& \leq 4 \sqrt{n} \tau+d\left(y_{1}, y_{2}\right)(1+8 \sqrt{\tau}) .
\end{aligned}$$
We finally get
$$d\left(F_{c}\left(y_{1}\right), F_{c}\left(y_{2}\right)\right) \leq \kappa+(1+\kappa) d\left(y_{1}, y_{2}\right),$$
in case ii). \(\square\)

\section*{4 A limit map on the limit space}

In this section, we consider a sequence $\left(Y_{k}, g_{k}\right)_{k \in \mathbf{N}}$ of closed Riemannian $n$-manifolds satisfying the curvature bound (3) and the following assumption: we suppose that
there exist an closed hyperbolic $n$-manifold $\left(X, g_{0}\right)$, degree one maps $f_{k}: Y_{k} \rightarrow X$ and a sequence $\varepsilon_{k} \rightarrow 0$ such that
$$\operatorname{vol}_{g_{k}}\left(Y_{k}\right) \rightarrow \operatorname{vol}_{g_{0}}(X),$$
as $k$ goes to $+\infty$. From (8), for every $k \in \mathbf{N}$, there exists $y_{g_{k}} \in Y_{k}$ satisfying the local volume estimate, that is $\operatorname{vol}\left(B_{g_{k}}\left(y_{g_{k}}, 1\right)\right) \geq v_{n}>0$. For the sake of simplicity we shall use the notation $y_{k}$ instead of $y_{g_{k}}$.
Below, we prove that $\left(Y_{k}, g_{k}, y_{k}\right)$ sub-converges in the pointed Gromov-Haudorff topology to a limit metric space $\left(Y_{\infty}, d_{\infty}, z_{\infty}\right)$. Moreover, there exists a sequence of natural maps $F_{c_{k}}:\left(Y_{k}, g_{k}\right) \rightarrow\left(X, g_{0}\right)$, with suitably chosed parameters $c_{k}$, which sub-converges to a "natural map" $F: Y_{\infty} \longrightarrow X$.

Let us recall the definition of the Gromov-Hausdorff topology. For two subsets $A, B$ of a metric space $Z$ the Hausdorff distance between $A$ and $B$ is
$$\mathrm{d}_{\mathcal{H}}{ }^{Z}(A, B):=\inf \left\{\varepsilon>0 \mid B \subset V_{\varepsilon}(A) \text { and } A \subset V_{\varepsilon}(B)\right\} \in \mathbf{R} \cup\{\infty\} .$$
It is a distance on compact subsets of $Z$ (see [10]).
Definition 4.1 ([12]). Let $X_{1}, X_{2}$ be two metric spaces, then the Gromov-Hausdorff distance $\mathrm{d}_{\mathcal{G} \mathcal{H}}\left(X_{1}, X_{2}\right) \in \mathbf{R} \cup \infty$ is the infimum of the numbers
$$\left.\mathrm{d}_{\mathcal{H}}{ }^{Z}\left(f_{1}\left(X_{1}\right), f_{2}\left(X_{2}\right)\right)\right)$$
for all metric spaces $Z$ and all isometric embeddings $f_{i}: X_{i} \rightarrow Z$.
It is a distance on the space of isometry classes of compact metric spaces. One says that a sequence $\left(X_{i}\right)_{i \in \mathbf{N}}$ of metric spaces converges in the Gromov-Hausdorff topology to a metric space $X_{\infty}$ if $\mathrm{d}_{\mathcal{G} \mathcal{H}}\left(X_{i}, X_{\infty}\right) \rightarrow 0$ as $i \rightarrow \infty$. Let $x_{i} \in X_{i}$ and $x_{\infty} \in X_{\infty}$, one says that the sequence $\left(X_{i}, x_{i}\right)_{i \in \mathbf{N}}$ converges to $\left(X_{\infty}, x_{\infty}\right)$ in the pointed Gromov-Hausdorff topology if for any $R>0, \mathrm{~d}_{\mathcal{G H}}\left(B_{X_{i}}\left(x_{i}, R\right), B_{X_{\infty}}\left(x_{\infty}, R\right)\right) \rightarrow 0$ as $i \rightarrow+\infty$ (in fact this definition holds only for length spaces, which will be sufficient in our situation).

To deal with the Gromov-Hausdorff distance between $X_{1}$ and $X_{2}$, it is convenient to avoid the third space $Z$ by using $\varepsilon$-approximations between $X_{1}$ and $X_{2}$.

Definition 4.2. Given two metric spaces $X_{1}, X_{2}$ and $\varepsilon>0$, an $\varepsilon$-approximation (or $\varepsilon$-isometry) from $X_{1}$ to $X_{2}$ is a map $f: X_{1} \rightarrow X_{2}$ such that
\begin{itemize}
\item[1.] for any $x, x^{\prime} \in X_{1},\left|d_{X_{2}}\left(f(x), f\left(x^{\prime}\right)\right)-d_{X_{1}}\left(x, x^{\prime}\right)\right|<\varepsilon$.
\item[2.] the $\varepsilon$-neighbourhood of $f\left(X_{1}\right)$ is equal to $X_{2}$.
\end{itemize}

Then one can show (see [4, Corollary 7.3.28]) that $\mathrm{d}_{\mathcal{G} \mathcal{H}}\left(X_{1}, X_{2}\right)<\varepsilon$ if there exists a $2 \varepsilon$ -approximation from $X_{1}$ to $X_{2}$ and similarly an $\varepsilon$-approximation exists if $\mathrm{d}_{\mathcal{G} \mathcal{H}}\left(X_{1}, X_{2}\right)<$ $2 \varepsilon$. Let us insist on the fact that these approximations may be neither continuous nor even measurable.

Our goal is to prove the :

Proposition 4.3. Up to extraction and renumbering, the sequence $\left(Y_{k}, g_{k}, y_{k}\right)$ satisfies the following.
\begin{itemize}
\item[1.] There exists a complete pointed length space $\left(Y_{\infty}, d_{\infty}, y_{\infty}\right)$ such that $\left(Y_{k}, g_{k}, y_{k}\right)$ converges in the pointed Gromov-Hausdorff topology to a metric space $\left(Y_{\infty}, d_{\infty}, y_{\infty}\right)$. Moreover, $\left(Y_{\infty}, d_{\infty}\right)$ has Hausdorff dimension equal to $n$.
\item[2.] there exist sequences of positive numbers $\varepsilon_{k}, \delta_{k}$ going to $0, c_{k}$ such that $h\left(g_{k}\right)<$ $c_{k}<h\left(g_{k}\right)+\delta_{k}, R_{k}$ going to $+\infty$ such that $\varepsilon_{k} \leq \varepsilon\left(R_{k}\right)$ and $\delta_{k} \leq \delta\left(R_{k}\right)$. There also exist and $\alpha_{k}$-approximations $\psi_{k}: B_{d_{\infty}}\left(y_{\infty}, R_{k}\right) \rightarrow B_{g_{k}}\left(y_{g_{k}}, R_{k}\right)$ such that the following holds. Let
$$F_{c_{k}}:\left(Y_{k}, g_{k}\right) \rightarrow\left(X, g_{0}\right)$$
be the natural map as defined in section 2. Then $F_{c_{k}} \circ \psi_{k}$ converges uniformly on compact sets to a map
$$F: Y_{\infty} \longrightarrow X,$$
which is 1-lipschitz.
\end{itemize}

The proof is divided in two steps described in the following sections.

\section*{Existence of the limit and its properties}

Under the curvature bound (3) and the local volume estimate (11), (1) of Proposition 4.3 is a straightforward application of Gromov \& Cheeger-Colding compactness theorem, see [7, Theorem 1.6]. Before proving point (2) of Proposition 4.3, let us describe some features of the convergence and of the limit space which will be used later.

The continuity of the volume under the (pointed) Gromov-Hausdorff convergence is crucial for our purposes. For $\ell>0$, note $\mathcal{H}^{\ell}$ the $\ell$-dimensional Hausdorff measure of a metric space (see [4] definition 1.7.7).

Theorem 4.4 ([7], Theorem 5.9). Let $p_{i} \in Y_{i}$ and $p_{\infty} \in Y_{\infty}$ their limit, and let $R>0$. Then
$$\lim _{i \rightarrow+\infty} \operatorname{vol}_{g_{i}}\left(B\left(p_{i}, R\right)\right)=\mathcal{H}^{n}\left(B\left(p_{\infty}, R\right)\right) .$$
In particular, $Y_{\infty}$ satisfies the Bishop-Gromov inequalities (9) and the Bishop inequality. By definition, a tangent cone at $p \in Y_{\infty}$ is a complete pointed Gromov-Hausdorff limit, $\left\{Y_{\infty, p}, d_{\infty}, p_{\infty}\right\}$ of a sequence of rescaled space, $\left\{\left(Y_{\infty}, r_{i}^{-1} d, p\right)\right\}$, where $\left\{r_{i}\right\}$ is a positive sequence such that $r_{i} \rightarrow 0$. Indeed, by [11, Proposition 5.2], every such sequence has a convergent subsequence, but the limit might depend on the choice of the sub-sequence. Notice that this notion is different from the one described in [4, Chapter 8] where the authors require that the limit is unique (does not depend on the sub-sequence).

Definition 4.5. The regular set $\mathcal{R}$ consists of those points, $p \in Y_{\infty}$, such that every tangent cone at $p$ is isometric to $\mathbf{R}^{n}$. The complementary $\mathcal{S}=Y_{\infty} \backslash \mathcal{R}$ is the singular set.

Let $B_{0}^{n}(1) \subset \mathbf{R}^{n}$ be the unit ball.
Definition 4.6. The $\varepsilon$-regular set $\mathcal{R}_{\varepsilon}$ consists of those points, $p \in Y_{\infty}$, such that every tangent cone, $\left(Y_{\infty, p}, p_{\infty}\right)$, satisfies $d_{G H}\left(B\left(p_{\infty}, 1\right), B_{0}^{n}(1)\right)<\varepsilon$. A point in $Y_{\infty} \backslash \mathcal{R}_{\varepsilon}=\mathcal{S}_{\varepsilon}$ is called $\varepsilon$-singular,

Theorem 4.7 ([7], Theorem 5.14). There exists $\varepsilon_{n}>0$ such that for $\varepsilon \leq \varepsilon_{n}, \stackrel{\circ}{\mathcal{R}}_{\varepsilon}$ has a natural smooth manifold structure. Moreover, for this parametrization, the metric on $\stackrel{\circ}{\mathcal{R}}_{\varepsilon}$ is bi-hölder equivalent to a smooth Riemannian metric. The exponent $\alpha(\varepsilon)$ in this bi-hölder equivalence satisfies $\alpha(\varepsilon) \rightarrow 1$ as $\varepsilon \rightarrow 0$.

Theorem 4.8 ([7], Theorem 6.1).
$$\mathcal{H}^{n-2}(\mathcal{S})=0$$

Remark 4.9. Clearly, $\mathcal{R}=\cap_{\varepsilon>0} \mathcal{R}_{\varepsilon}$. The sets $\mathcal{R}_{\varepsilon}, \mathcal{R}$ are not necessarily open. However, for any $\varepsilon>0$, there is some $\varepsilon>\delta>0$ such that $\mathcal{R}_{\delta} \subset \stackrel{\circ}{\mathcal{R}}_{\varepsilon}$ (see [7, Appendix A.1.5]). In [8, Section 3], it is also proved that $\stackrel{\circ}{\mathcal{R}}_{\varepsilon}$ is path connected. This important fact will be used in the last part of this text.

We now study the density of the Hausdorff measure. A consequence of Bishop's inequality is that
$$\limsup _{r \rightarrow 0} \frac{\mathcal{H}^{n}(B(p, r))}{\operatorname{vol}_{\mathbf{R}^{n}}(r)} \leq 1$$

Definition 4.10. The density at $p$ of $Y_{\infty}$ is
$$\theta(p):=\liminf _{r \rightarrow 0} \frac{\mathcal{H}^{n}(B(p, r))}{\operatorname{vol}_{\mathbf{R}^{n}}(r)} .$$
A consequence of [7, A.1.5] is the existence of some positive function $\tau(\varepsilon)$, with $\tau(\varepsilon) \rightarrow 0$ as $\varepsilon \rightarrow 0$, such that for every $p \in \mathcal{R}_{\varepsilon}$,
$$\theta(p)>1-\tau(\varepsilon) .$$
Conversely, there exists a positive function $\varepsilon(\tau)$, satisfying $\varepsilon(\tau) \rightarrow 0$ as $\tau \rightarrow 0$ and such that
$$\theta(p) \geq 1-\tau \Longrightarrow p \in \mathcal{R}_{\varepsilon(\tau)} .$$

Remark 4.11. A point $p$ is regular if and only if $\theta(p)=1$. From now on, we consider $\varepsilon \leq \varepsilon_{0}$, where $\varepsilon_{0} \leq \varepsilon_{n}$ is sufficiently small so that $\tau\left(\varepsilon_{0}\right)<1 / 2$, the density is thus strictly greater than $1 / 2$ on $\mathcal{R}_{\varepsilon}$.

\section*{Existence of the natural map at the limit}

Let us now prove (2) of Proposition 4.3.
Proof. For every $k \in \mathbf{N}$ and $c>h\left(g_{k}\right)$, there exists a natural map $F_{c}:\left(Y_{k}, g_{k}\right) \rightarrow$ ( $X, g_{0}$ ), described in Section 2. We need to choose the values of $c$ for each $g_{k}$ in order that $F_{c}$ to satisfies some good properties. One argues as follows.

Given $m \in \mathbf{N}^{*}$, one chooses positive numbers $\varepsilon_{m} \leq \varepsilon_{2}(m)$ and $\delta_{m} \leq \delta_{2}(m)$ sufficiently small such that $\kappa\left(\varepsilon_{m}, \delta_{m}, m\right) \leq \frac{1}{m}$, where $\delta_{2}, \varepsilon_{2}$ and $\kappa$ are given by Lemma 3.13. One then defines
$$\alpha_{m}=\max \left\{\alpha_{1}\left(\varepsilon_{m}, \delta_{m}\right), \alpha_{2}\left(\varepsilon_{m}, \delta_{m}\right), \alpha_{3}\left(\varepsilon_{m}, \delta_{m}\right) \kappa\left(\varepsilon_{m}, \delta_{m}, m\right)\right\} .$$
We check that $\alpha_{m} \rightarrow 0$ as $m \rightarrow+\infty$. By the hypothesis (73), there exists $k_{1}(m) \in$ N such that for any $k \geq k_{1}(m), \operatorname{vol}_{g_{k}}\left(Y_{k}\right) \leq\left(1+\varepsilon_{m}\right) \operatorname{vol}_{g_{0}}(X)$. Since for $m$ fixed $B_{g_{k}}\left(y_{k}, m\right)$ converges to $B_{\infty}\left(y_{\infty}, m\right)$, there exists $k_{2}(m) \in \mathbf{N}$ such that for any $k \geq$ $k_{2}(m)$, there exists $\alpha_{m}$-approximations from $B_{\infty}\left(y_{\infty}, m\right)$ to $B_{g_{k}}\left(y_{k}, m\right)$. Define $k(m):=$ $\max \left\{k_{1}(m), k_{2}(m)\right\}$ and let $\psi_{m}: B_{\infty}\left(y_{\infty}, m\right) \longrightarrow B_{g_{k}}\left(y_{k(m)}, m\right)$ be an $\alpha_{m}$-approximation. One can assume that $\psi_{m}\left(y_{\infty}\right)=y_{g_{k(m)}}$. Choose $h\left(g_{k}\right)<c_{m}<h\left(g_{k}\right)+\delta_{m}$ and consider
$$F_{c_{m}} \circ \psi_{m}: B_{\infty}\left(y_{\infty}, m\right) \longrightarrow X .$$
Lemma 3.13 applies to $F_{c_{m}}$ on $B_{g_{k(m)}}\left(y_{k(m)}, m\right)$. Hence, for any $p, q \in B_{\infty}\left(y_{\infty}, m\right)$,
$$\begin{aligned}
d_{g_{0}}\left(F_{c_{m}} \circ \psi_{m}(p), F_{c_{m}} \circ \psi_{m}(q)\right) & \leq\left(1+\alpha_{m}\right) d_{g_{k}}\left(\psi_{m}(p), \psi_{m}(q)\right)+\alpha_{m} \\
& \leq\left(1+\alpha_{m}\right) d_{\infty}(p, q)+\left(1+\alpha_{m}\right) \alpha_{m}+\alpha_{m} .
\end{aligned}$$
Applying the same reasoning as in Ascoli's theorem, one can show that for any compact $K \subset Y_{\infty}$, there exists a sub-sequence of $F_{c_{m}}$ converging to a map $F_{K}: K \rightarrow X$. We denote it by $F_{c_{\phi(m)}}$. If one uses an exhaustion of $Y_{\infty}$ by compact sets and a standard diagonal process, one can extract a sub-sequence of $F_{c_{\phi(m)}} \circ \psi_{\phi(m)}$ which converges uniformly on any compact set to a map $F: Y_{\infty} \rightarrow X$. It is easy to see that the map $F$ is 1-lipschitz.
Then one renumbers the sub-sequences $Y_{k(\phi(m))}, \psi_{\phi(m)}$ and $F_{c_{\phi(m)}}$ such that, for any $m \in \mathbf{N}^{*}, \operatorname{vol}_{g_{m}}\left(Y_{m}\right) \leq\left(1+\varepsilon_{m}\right) \operatorname{vol}_{g_{0}}(X), h\left(g_{m}\right)<c_{m}<c_{m}+\delta_{m}$, the inequalities of Lemmas 3.5, 3.11 hold with $\alpha_{1}, \alpha_{2}, \alpha_{3}$ replaced by $\alpha_{m}$ and those of Lemmas 3.12, 3.13 hold on $B\left(y_{m}, m\right) \subset Y_{m}$ with $\kappa$ replaced by $\alpha_{m}$. For simplicity, the map $F_{c_{m}}$ will be denoted $F_{m}$. \(\square\)

\section*{5 The limit map $F: Y_{\infty} \longrightarrow X$ is isometric}

In this section we aim at proving that the limit map $F=\lim F_{k} \circ \psi_{k}$ is an isometry, i.e. it is distance preserving. We prove first that $F$ preserves the volume.

Lemma 5.1. Let $A \subset Y_{\infty}$ be a measurable subset. Then,
$$\operatorname{vol}_{g_{0}}(F(A))=\mathcal{H}^{n}(A) .$$

Proof. It suffices to prove the lemma when the set $A$ is an open ball. Indeed, let us assume that $F$ preserves the volume of balls and let $A$ be a measurable set included in a ball $B:=B_{\infty}(p, r)$. Since $F$ is contracting it does not increase the volumes (see [14, Proposition 3.5]). Now, if $\operatorname{vol}_{g_{0}}(A)<\mathcal{H}^{n}(A)$ and since we have $\operatorname{vol}_{g_{0}}(B \backslash A) \leq \mathcal{H}^{n}(B \backslash A)$ we have a contradiction with the preservation of the volume of $B$. Similarly, if $A$ is a measurable set of finite measure we can apply the same argument with $A$ and $B \backslash A$ for any ball $B$.

It is then enough to prove that for every $B_{\infty}(p, r) \subset Y_{\infty}, \operatorname{vol}_{g_{0}}\left(F\left(B_{\infty}(p, r)\right)\right) \geq \mathcal{H}^{n}\left(B_{\infty}(p, r)\right)$. By construction, $\overline{F\left(B_{\infty}(p, r)\right)}$ is the Hausdorff limit of $\overline{F_{k} \circ \psi_{k}\left(B_{\infty}(p, r)\right)}$.
We first show that this is also the Hausdorff limit of $\overline{F_{k}\left(B_{g_{k}}\left(\psi_{k}(p), r\right)\right)}$. Let $x \in$ $\overline{F\left(B_{\infty}(p, r)\right)}$ and $x_{k} \in F\left(B_{\infty}(p, r)\right)$ such that $x_{k} \rightarrow x$. Let $p_{k} \in B_{\infty}(p, r)$ such that $F\left(p_{k}\right)=x_{k}$. By definition of the $\alpha_{k}$-approximation, one has $d_{g_{k}}\left(\psi_{k}\left(p_{k}\right), \psi_{k}(p)\right)<$ $r+\alpha_{k}$. There exists $z_{k} \in B_{g_{k}}\left(\psi_{k}(p), r\right)$ such that $d_{g_{k}}\left(\psi_{k}\left(p_{k}\right), z_{k}\right)<\alpha_{k}$ (for example $z_{k}$ may be on the segment $\left[\psi_{k}\left(p_{k}\right), \psi_{k}(p)\right]$ ). Note that, by the triangular inequality, $d_{\infty}\left(p_{k}, y_{\infty}\right) \leq r+d_{\infty}\left(p, y_{\infty}\right)$ and recall that $\psi_{k}\left(y_{\infty}\right)=y_{g_{k}}$. Thus $\psi_{k}\left(p_{k}\right)$ remains at bounded distance from $y_{g_{k}}$. Then, applying Lemma 3.13 we have
$$\begin{aligned}
d_{g_{0}}\left(F_{k}\left(z_{k}\right), F_{k}\left(\psi_{k}\left(p_{k}\right)\right)\right. & \leq\left(1+\alpha_{k}\right) d_{g_{k}}\left(z_{k}, \psi_{k}\left(p_{k}\right)\right)+\alpha_{k} \\
& \leq\left(1+\alpha_{k}\right) \alpha_{k}+\alpha_{k} \\
& \underset{k \rightarrow+\infty}{\longrightarrow} 0 .
\end{aligned}$$
On the other hand, since $F_{k} \circ \psi_{k}$ converges uniformly to $F$ on compact sets, $F_{k}\left(\psi_{k}\left(p_{k}\right)\right)$ has the same limit as $F\left(p_{k}\right)=x_{k}$, that is $F_{k}\left(\psi_{k}\left(p_{k}\right)\right) \rightarrow x$. From the inequality above one deduces that $F_{k}\left(z_{k}\right) \rightarrow x$ which shows that $x \in \lim _{k \rightarrow \infty} F_{k}\left(B_{g_{k}}\left(\psi_{k}(p), r\right)\right)$. One has then proved that $\overline{F\left(B_{\infty}(p, r)\right)} \subset \lim _{k \rightarrow \infty} \overline{F_{k}\left(B_{g_{k}}\left(\psi_{k}(p), r\right)\right)}$. In order to prove the other inclusion one argues similarly. Given $x \in \lim _{k \rightarrow \infty} \overline{F_{k}\left(B_{g_{k}}\left(\psi_{k}(p), r\right)\right)}$, there exists $x_{k} \in F_{k}\left(B_{g_{k}}\left(\psi_{k}(p), r\right)\right)$ such that $x_{k} \rightarrow x$, with $x_{k}=F_{k}\left(z_{k}\right)$ where $z_{k} \in B_{g_{k}}\left(\psi_{k}(p), r\right)$. As $\psi_{k}$ is an $\alpha_{k}$-approximation from $B_{\infty}\left(y_{\infty}, k\right)$ to $B\left(y_{g_{k}}, k\right)$, one has the inclusion $B_{g_{k}}\left(\psi_{k}(p), r\right) \subset U_{\alpha_{k}} \psi_{k}\left(B_{\infty}\left(p, r+\alpha_{k}\right)\right)$ for large $k$, thus there exists $q_{k} \in B_{\infty}\left(p, r+\alpha_{k}\right)$ satisfying $d_{g_{k}}\left(z_{k}, \psi_{k}\left(q_{k}\right)\right)<\alpha_{k}$. As $Y_{\infty}$ is a length space, there exists $q_{k}^{\prime} \in B_{\infty}(p, r)$ such that $d_{\infty}\left(q_{k}^{\prime}, q_{k}\right)<\alpha_{k}$. Then $\left.d_{g_{k}}\left(\psi_{k}\left(q_{k}^{\prime}\right), z_{k}\right) \leq d_{g_{k}}\left(\psi_{k}\left(q_{k}^{\prime}\right), \psi_{k}\left(q_{k}\right)\right)+d_{g_{k}}\left(\psi_{k}\left(q_{k}\right), z_{k}\right)\right)<$ $3 \alpha_{k}$. Thus
$$\begin{aligned}
d_{g_{0}}\left(F_{k} \circ \psi_{k}\left(q_{k}^{\prime}\right), x_{k}\right)=d_{g_{0}}\left(F_{k} \circ \psi_{k}\left(q_{k}^{\prime}\right), F_{k}\left(z_{k}\right)\right) & \leq\left(1+\alpha_{k}\right) d_{g_{k}}\left(\psi_{k}\left(q_{k}^{\prime}\right), z_{k}\right)+\alpha_{k} \\
& \leq\left(1+\alpha_{k}\right) 3 \alpha_{k}+\alpha_{k} \rightarrow 0 .
\end{aligned}$$
Hence $d_{g_{0}}\left(F_{k} \circ \psi_{k}\left(q_{k}^{\prime}\right), x\right) \rightarrow 0$. As $F_{k} \circ \psi_{k}$ converges uniformly to $F$ on compact sets, one has $d_{g_{0}}\left(F\left(q_{k}^{\prime}\right), x\right) \rightarrow 0$ thus $x \in \overline{F\left(B_{\infty}(p, r)\right)}$. This shows that $x \in \overline{F\left(B_{\infty}(p, r)\right)}$ is the Hausdorff limit of $\overline{F_{k}\left(B_{g_{k}}\left(\psi_{k}(p), r\right)\right)}$.

In order to prove the lemma it is then sufficient to prove that
$$\liminf _{k \rightarrow+\infty} \operatorname{vol}_{g_{0}}\left(\overline{F_{k}\left(B_{g_{k}}\left(\psi_{k}(p), r\right)\right.}\right) \geq \liminf _{k \rightarrow+\infty} \operatorname{vol}_{g_{0}}\left(F_{k}\left(B_{g_{k}}\left(\psi_{k}(p), r\right)\right) \geq \mathcal{H}^{n}\left(B_{\infty}(p, r)\right) .\right.$$
Indeed, inequality (80) will imply that
$$\operatorname{vol}_{g_{0}}\left(F\left(\overline{B_{\infty}(p, r)}\right)\right) \geq \operatorname{vol}_{g_{0}}\left(\overline{F\left(B_{\infty}(p, r)\right)}\right) \geq \mathcal{H}^{n}\left(B_{\infty}(p, r)\right)$$
and thus $\operatorname{vol}_{g_{0}}\left(F\left(B_{\infty}(p, r)\right)\right) \geq \mathcal{H}^{n}\left(B_{\infty}(p, r)\right)$ since $F$ being Lipschitz, we have
$$\operatorname{vol}_{g_{0}}\left(F\left(\overline{B_{\infty}(p, r)}\right)\right)=\operatorname{vol}_{g_{0}}\left(F\left(B_{\infty}(p, r)\right)\right) .$$
Recall that $N\left(F_{k}, x\right)$ is the number of preimages of $x$ by $F_{k}$. We denote by $X_{k, 1}$ the set of $x \in X$ such that $N\left(F_{k}, x\right)=1$. The construction of the sequence $\left(F_{k}\right)$, Lemma 3.10 and our choice of the $\alpha_{k}$ 's imply that $\operatorname{vol}_{g_{0}}\left(X_{k, 1}\right) \geq\left(1-\alpha_{k}\right) \operatorname{vol}_{g_{0}}(X)$ and
$$\int_{X \backslash X_{k, 1}} N\left(F_{k}, x\right) \mathrm{dv}_{\mathrm{g}_{0}}(x) \leq \alpha_{k} \operatorname{vol}_{g_{0}}(X) .$$
We also denote by $Y_{k, \alpha_{k}}$ the set of $y \in Y_{k}$ such that
$$1-\alpha_{k} \leq\left|\operatorname{Jac} F_{k}(y)\right| \leq 1+\alpha_{k} .$$
Then Lemma 3.9 implies that $\operatorname{vol}_{g_{k}}\left(Y_{k, \alpha_{k}}\right) \geq\left(1-\alpha_{k}\right) \operatorname{vol}_{g_{k}}\left(Y_{k}\right)$, for $k$ large enough. We then have
$$\begin{aligned}
\operatorname{vol}_{g_{0}}\left(F_{k}\left(B_{g_{k}}\left(\psi_{k}(p), r\right)\right)\right) & =\int_{F_{k}\left(B_{g_{k}}\left(\psi_{k}(p), r\right)\right)} \mathrm{dv}_{\mathrm{g}_{0}} \\
& =\int_{F_{k}\left(B_{g_{k}}\left(\psi_{k}(p), r\right)\right) \cap X_{k, 1}} N\left(F_{k}, x\right) \mathrm{dv}_{\mathrm{g}_{0}}(x)+\operatorname{vol}_{g_{0}}\left(F_{k}\left(B_{g_{k}}\left(\psi_{k}(p), r\right)\right) \backslash X_{k, 1}\right) \\
& \geq \int_{B_{g_{k}}\left(\psi_{k}(p), r\right) \cap F_{k}^{-1}\left(X_{k, 1}\right) \cap Y_{k, \alpha}}\left|\operatorname{Jac}_{k}(y)\right| \operatorname{dv}_{g_{k}}(y) \\
& \geq\left(1-\alpha_{k}\right) \operatorname{vol}_{g_{k}}\left(B_{g_{k}}\left(\psi_{k}(p), r\right) \cap F_{k}^{-1}\left(X_{k, 1}\right) \cap Y_{k, \alpha_{k}}\right)
\end{aligned}$$
On the other hand, using (82) and (81) we have
$$\begin{aligned}
\operatorname{vol}\left(F_{k}^{-1}\left(X \backslash X_{k, 1}\right) \cap Y_{k, \alpha_{k}}\right) & \leq \int_{F_{k}^{-1}\left(X \backslash X_{k, 1}\right) \cap Y_{k, \alpha_{k}}} \frac{\left|\operatorname{Jac}_{k}\right|}{1-\alpha_{k}} \operatorname{dv}_{g_{k}} \\
& \leq \frac{1}{1-\alpha_{k}} \int_{X \backslash X_{k, 1}} N\left(F_{k}, x\right) \mathrm{dv}_{\mathrm{g}_{0}}(x) \\
& \leq \frac{\alpha_{k}}{1-\alpha_{k}} \operatorname{vol}_{g_{0}}(X)
\end{aligned}$$
consequently
$$\begin{aligned}
\operatorname{vol}_{g_{k}}\left(B_{g_{k}}\left(\psi_{k}(p), r\right) \cap F_{k}^{-1}\left(X_{k, 1}\right) \cap Y_{k, \alpha_{k}}\right) & =\operatorname{vol}_{g_{k}}\left(B_{g_{k}}\left(\psi_{k}(p), r\right) \cap Y_{k, \alpha_{k}}\right) \\
& -\operatorname{vol}_{g_{k}}\left(B_{g_{k}}\left(\psi_{k}(p), r\right) \cap F_{k}^{-1}\left(X \backslash X_{k, 1}\right) \cap Y_{k, \alpha_{k}}\right) \\
& \geq \operatorname{vol}_{g_{k}}\left(B_{g_{k}}\left(\psi_{k}(p), r\right)\right)-\alpha_{k} \operatorname{vol}_{g_{k}}\left(Y_{k}\right)-\frac{\alpha_{k}}{1-\alpha_{k}} \operatorname{vol}_{g_{0}}(X) .
\end{aligned}$$

Plugging this inequality in (83) one gets
$\operatorname{vol}_{g_{0}}\left(F_{k}\left(B_{g_{k}}\left(\psi_{k}(p), r\right)\right) \geq\left(1-\alpha_{k}\right) \operatorname{vol}_{g_{k}}\left(B_{g_{k}}\left(\psi_{k}(p), r\right)\right)-\left(1-\alpha_{k}\right) \alpha_{k} \operatorname{vol}_{g_{k}}\left(Y_{k}\right)-\alpha_{k} \operatorname{vol}_{g_{0}}(X)\right.$.
As $B_{g_{k}}\left(\psi_{k}(p), r\right)$ converges to $B_{\infty}(p, r)$ in the Gromov-Hausdorff topology, Theorem 4.4 implies that $\lim _{k \rightarrow \infty} \operatorname{vol}_{g_{k}}\left(B_{g_{k}}\left(\psi_{k}(p), r\right)\right)=\mathcal{H}^{n}\left(B_{\infty}(p, r)\right)$, hence
$$\liminf _{k \rightarrow \infty} \operatorname{vol}_{g_{0}}\left(F_{k}\left(B_{g_{k}}\left(\psi_{k}(p), r\right)\right) \geq \mathcal{H}^{n}\left(B_{\infty}(p, r)\right),\right.$$
which proves the lemma. \(\square\)

We now prove that $F$ is injective on the set of points where the density is larger than 1/2.

Lemma 5.2. The map $F$ is injective on $\mathcal{R}_{\varepsilon}$ for $\epsilon \leq \epsilon_{0}$.
Proof. Suppose that there are $p_{1}, p_{2} \in \mathcal{R}_{\varepsilon}$ such that $F\left(p_{1}\right)=F\left(p_{2}\right)$. As $F$ is 1 -lipschitz, we have for every $r>0$,
$$F\left(B_{\infty}\left(p_{1}, r\right) \cup B_{\infty}\left(p_{2}, r\right)\right) \subset B_{g_{0}}\left(F\left(p_{1}\right), r\right) .$$
By the previous lemma,
$$\begin{aligned}
\mathcal{H}^{n}\left(B_{\infty}\left(p_{1}, r\right) \cup B_{\infty}\left(p_{2}, r\right)\right) & =\operatorname{vol}_{g_{0}}\left(F\left(B_{\infty}\left(p_{1}, r\right) \cup B_{\infty}\left(p_{2}, r\right)\right)\right) \\
& \leq \operatorname{vol}_{g_{0}}\left(B_{\infty}\left(F\left(p_{1}\right), r\right)\right)
\end{aligned}$$
For $r<d\left(p_{1}, p_{2}\right) / 2$ the balls $B_{\infty}\left(p_{1}, r\right)$ and $B_{\infty}\left(p_{2}, r\right)$ are disjoint. Hence, dividing (84) by $\operatorname{vol}_{\mathbf{R}^{n}}(r)$, we get
$$\frac{\mathcal{H}^{n}\left(B_{\infty}\left(p_{1}, r\right)\right)}{\operatorname{vol}_{\mathbf{R}^{n}}(r)}+\frac{\mathcal{H}^{n}\left(B_{\infty}\left(p_{2}, r\right)\right)}{\operatorname{vol}_{\mathbf{R}^{n}}(r)} \leq \frac{\operatorname{vol}_{g_{0}}\left(B_{g_{0}}\left(F\left(p_{1}\right), r\right)\right)}{\operatorname{vol}_{\mathbf{R}^{n}}(r)} .$$
Taking the liminf as $r \rightarrow 0$ yields
$$\theta\left(p_{1}\right)+\theta\left(p_{2}\right) \leq \theta\left(F\left(p_{1}\right)\right)=1,$$
which is a contradiction, since $\theta>1 / 2$ on $\mathcal{R}_{\varepsilon}$ if $\varepsilon<\varepsilon_{0}$ (see remark 4.11). \(\square\)

Lemma 5.3. The map $F$ is open on $\stackrel{\circ}{\mathcal{R}}_{\varepsilon}$ for $\epsilon \leq \epsilon_{0}$.
Proof. Let $p \in \stackrel{\circ}{\mathcal{R}}_{\varepsilon}$. We have to prove that there exists $\eta>0$ such that $B_{g_{0}}(F(p), \eta) \subset$ $F\left(\stackrel{\circ}{\mathcal{R}}_{\varepsilon}\right)$. There exists $r>0$ such that $B_{\infty}(p, 2 r) \subset \stackrel{\circ}{\mathcal{R}}_{\varepsilon}$. For the sake of simplicity we shall note $B:=B_{\infty}(p, r)$. By the previous lemma, $F(p) \notin F(\partial B)$. Thus, by compactness of $\partial B$ and continuity of $F$, there exists $\eta>0$ such that $d_{g_{0}}(F(p), F(\partial B))>\eta$. Notice that, since $F$ is 1 -Lipschitz, $\eta<r$. Here, one could use the theory of local degree as in [5, Appendix C], however $Y_{\infty}$ is not, a priori a manifold and it may even be not locally lipschitz equivalent to $\mathbf{R}^{n}$. Let $R>2 r+d_{\infty}\left(y_{\infty}, p\right)$ be a fixed radius; it satisfies
$\psi_{k}\left(B_{\infty}(p, 2 r)\right) \subset B_{g_{k}}\left(y_{g_{k}}, R\right)$ for large $k$. Let $z_{k}=\psi_{k}(p)$ and $B_{k}:=B\left(z_{k}, r\right)$. The choice of $R$ and the fact that the $\psi_{k}$ 's are approximations shows that $B_{k} \subset B\left(y_{g_{k}}, R\right)$, for $k$ large enough. We choose $k$ large enough such that $\mathrm{d}_{\mathcal{H}}\left(F_{k}\left(\partial B_{k}\right), F(\partial B)\right) \leq \frac{\eta}{10}$. This is possible since $\mathrm{d}_{\mathcal{H}}\left(\psi_{k}(\partial B), \partial B_{k}\right)$ goes to zero, $F_{k} \circ \psi_{k}$ converges to $F$ and $F(p)$ is at distance from $F(\partial B)$ larger than $\eta$. Let $\mathcal{C}$ (resp. $\mathcal{C}_{k}$ ) be the connected component of $X \backslash F(\partial B)$ (resp. $X \backslash F_{k}\left(\partial B_{k}\right)$ ), which contains $F(p)$, (resp $F_{k}\left(z_{k}\right)$ ). Now the ball $B(F(p), \eta / 10)$ is included in $\mathcal{C}$ and for $k$ large enough $B\left(F_{k}\left(z_{k}\right), \eta / 10\right)$ is included in $\mathcal{C}_{k}$. On the other hand by Corollary 4.1.26 of [10], $\operatorname{deg}\left(F_{k} \mid B_{k}\right)$ is constant on $\mathcal{C}_{k}$, where, for a subset $A \subset Y_{k}$,
$$\operatorname{deg}\left(F_{k} \mid A\right)(x)=\sum_{y \in F_{k}^{-1}(x) \cap A} \operatorname{sign} \operatorname{Jac} F_{k}(y) .$$
We show that $\operatorname{deg}\left(F_{k} \mid B_{k}\right)=1$ on $\mathcal{C}_{k}$ as follows. We have to show that at least one point in $\mathcal{C}_{k}$ this degree is 1 since it is constant on this set. In order to do that, we shall show that the set of such points has positive measure. Denote again by $X_{k, 1} \subset X$ the set of $x \in X$ such that $N\left(F_{k}, x\right)=1$, that is $x$ has one preimage by $F_{k}$. By Lemma 3.10, $\operatorname{vol}_{g_{0}}\left(X_{k, 1}\right) \geq\left(1-\alpha_{k}\right) \operatorname{vol}_{g_{0}}(X)$. The intersection of $X_{k, 1}$ with $\mathcal{C}_{k}$ has a positive measure for $k$ large enough; indeed, $B\left(F_{k}\left(z_{k}\right), \frac{\eta}{10}\right) \subset \mathcal{C}_{k}$ and its volume is bounded below by (11) and $\operatorname{vol}\left(B\left(F_{k}\left(z_{k}\right), \frac{\eta}{10}\right) \backslash X_{k, 1}\right) \longrightarrow 0$ as $k \rightarrow+\infty$. Now, by Lemma 3.12 one has $F_{k}\left(B\left(z_{k}, \frac{\eta}{20 \sqrt{n}}\right)\right) \subset B\left(F_{k}\left(z_{k}\right), \frac{\eta}{10}\right)$ and $B\left(z_{k}, \frac{\eta}{20 \sqrt{n}}\right) \subset B_{k}$ for large $k$, and an argument similar to the one used in 80 shows that the volume of the image is bounded below. It thus intersects $X_{k, 1}$ on a set of positive measure for $k$ large enough. This proves that $\operatorname{deg}\left(F_{k} \mid B_{k}\right)=1$ on $\mathcal{C}_{k}$. Since $B\left(F_{k}\left(z_{k}\right), \eta / 10\right)$ converges to $B(F(p), \eta / 10)$, this last ball is included in $\mathcal{C}_{k}$ for $k$ large; hence, any point in $B\left(F(p), \frac{\eta}{10}\right)$ has a preimage by $F_{k}$ in $B_{k}$. By taking the limit when $k$ goes to $+\infty$, we get $B\left(F(p), \frac{\eta}{10}\right) \subset F(\overline{B(p, r)}) \subset F(B(p, 2 r)) \subset F\left(\stackrel{\circ}{\mathcal{R}}_{\varepsilon}\right)$. \(\square\)

Lemma 5.4. There exists $c(\varepsilon)>0$ such that $F: \stackrel{\circ}{\mathcal{R}}_{\varepsilon} \longrightarrow F\left(\stackrel{\circ}{\mathcal{R}}_{\varepsilon}\right) \subset X$ is locally $(1+c(\varepsilon))$ -bi-Lipschitz. Moreover, $c(\varepsilon) \rightarrow 0$ as $\varepsilon \rightarrow 0$.

Proof. The idea is the following: we already know that $F$ is 1 -lipschitz and volume preserving. In particular, a ball $B_{\infty}(p, r) \subset Y_{\infty}$ is sent into a ball $B_{g_{0}}(F(p), r) \subset X$. If the ball in $Y_{\infty}$ is in the almost regular part and has a small radius, its volume is close to the Euclidean one, so is the volume of the hyperbolic ball. One can then estimate how much the image of $B_{\infty}(p, r)$ is close to fill $B_{g_{0}}(F(p), r)$. If one considers the images of two disjoint balls, one can estimate how the corresponding hyperbolic balls overlapp, and thus the distance between their centers.
Let $p \in \stackrel{\circ}{\mathcal{R}}_{\varepsilon}$. Let $r(p, \varepsilon)>0$ be a radius such that for every $0<r \leq r(p, \varepsilon)$,
$$\frac{\mathcal{H}^{n}\left(B_{\infty}(p, r)\right)}{\operatorname{vol}_{\mathbf{R}^{n}}(r)} \geq 1-\tau(\varepsilon),$$
and let $r_{\varepsilon}=\min \{\varepsilon, r(p, \varepsilon)\}$. One can assume that $r_{\varepsilon}$ is smaller than the injectivity radius of $X$. Let $0<r<r_{\varepsilon}^{2}$ be such that $B_{\infty}(p, r) \subset \mathcal{R}_{\varepsilon}$. For every $q \in B_{\infty}(p, r)$,
$B_{\infty}\left(p, r_{\varepsilon}-r_{\varepsilon}^{2}\right) \subset B_{\infty}\left(q, r_{\varepsilon}\right)$. Thus,
$$\begin{aligned}
\mathcal{H}^{n}\left(B_{\infty}\left(q, r_{\varepsilon}\right)\right) & \geq \mathcal{H}^{n}\left(B_{\infty}\left(p, r_{\varepsilon}-r_{\varepsilon}^{2}\right)\right) \\
& \geq(1-\tau(\varepsilon)) \operatorname{vol}_{\mathbf{R}^{n}}\left(r_{\varepsilon}-r_{\varepsilon}^{2}\right) \\
& \geq(1-\tau(\varepsilon))\left(1-r_{\varepsilon}\right)^{n} \operatorname{vol}_{\mathbf{R}^{n}}\left(r_{\varepsilon}\right)
\end{aligned}$$
Suppose that there exists $p_{1}, p_{2} \in B_{\infty}(p, r), p_{1} \neq p_{2}$ and a number $0<\rho<1$ such that
$$d_{g_{0}}\left(F\left(p_{1}\right), F\left(p_{2}\right)\right) \leq \rho d_{\infty}\left(p_{1}, p_{2}\right) .$$
Define $r^{\prime}=d_{\infty}\left(p_{1}, p_{2}\right) / 2>0$ and notice that $r^{\prime}<r$. By (74) and the Bishop-Gromov inequality (9), for $i=1,2$ one has
$$\mathcal{H}^{n}\left(B_{\infty}\left(p_{i}, r^{\prime}\right)\right) \geq \mathcal{H}^{n}\left(B_{\infty}\left(p_{i}, r_{\varepsilon}\right)\right) \frac{\operatorname{vol}_{\mathbf{H}^{n}}\left(r^{\prime}\right)}{\operatorname{vol}_{\mathbf{H}^{n}}\left(r_{\varepsilon}\right)} .$$
Thus, by Lemma 5.1, (87) and Bishop-Gromov inequality we have
$$\begin{aligned}
\operatorname{vol}_{g_{0}}\left(F\left(B_{\infty}\left(p_{1}, r^{\prime}\right) \cup B_{\infty}\left(p_{2}, r^{\prime}\right)\right)\right) & =\mathcal{H}^{n}\left(B_{\infty}\left(p_{1}, r^{\prime}\right)\right)+\mathcal{H}^{n}\left(B_{\infty}\left(p_{2}, r^{\prime}\right)\right) \\
& \geq 2(1-\tau(\varepsilon))\left(1-r_{\varepsilon}\right)^{n} \frac{\operatorname{vol}_{\mathbf{H}^{n}}\left(r^{\prime}\right)}{\operatorname{vol}_{\mathbf{H}^{n}}\left(r_{\varepsilon}\right)} \operatorname{vol}_{\mathbf{R}^{n}}\left(r_{\varepsilon}\right) \\
& \geq 2(1-\tau(\varepsilon))\left(1-r_{\varepsilon}\right)^{n} \frac{\operatorname{vol}_{\mathbf{R}^{n}}(\varepsilon)}{\operatorname{vol}_{\mathbf{H}^{n}}(\varepsilon)} \operatorname{vol}_{\mathbf{R}^{n}}\left(r^{\prime}\right) \\
& \geq 2 \vartheta(\varepsilon) \operatorname{vol}_{\mathbf{R}^{n}}\left(r^{\prime}\right)
\end{aligned}$$
where $\vartheta(\varepsilon)=(1-\tau(\varepsilon))(1-\varepsilon)^{n} \frac{\operatorname{vol}_{\mathbf{R}^{n}}(\varepsilon)}{\operatorname{vol}_{\mathbf{H}^{n}}(\varepsilon)} \rightarrow 1$ as $\varepsilon \rightarrow 0$.
On the other hand,
$$F\left(B_{\infty}\left(p_{1}, r^{\prime}\right) \cup B_{\infty}\left(p_{2}, r^{\prime}\right)\right) \subset B_{g_{0}}\left(F\left(p_{1}\right), r^{\prime}\right) \cup B_{g_{0}}\left(F\left(p_{2}\right), r^{\prime}\right),$$
Hence
$$\begin{aligned}
\operatorname{vol}_{g_{0}}\left(F\left(B_{\infty}\left(p_{1}, r^{\prime}\right) \cup B_{\infty}\left(p_{2}, r^{\prime}\right)\right)\right) \leq \operatorname{vol}_{g_{0}} & \left(B_{g_{0}}\left(F\left(p_{1}\right), r^{\prime}\right)\right)+\operatorname{vol}_{g_{0}}\left(B_{g_{0}}\left(F\left(p_{2}\right), r^{\prime}\right)\right) \\
& -\operatorname{vol}_{g_{0}}\left(B_{g_{0}}\left(F\left(p_{1}\right), r^{\prime}\right) \cap B_{g_{0}}\left(F\left(p_{2}\right), r^{\prime}\right)\right) .
\end{aligned}$$
For any $x \in X$ and any $s>0$ smaller than the injectivity radius of $X$ one has $\operatorname{vol}_{g_{0}}(B(x, s))=\operatorname{vol}_{\mathbf{H}^{n}}(s)$. Let $x$ be the middle point of the segment $\left[F\left(p_{1}\right) F\left(p_{2}\right)\right]$. Then
$$B\left(x, r^{\prime}(1-\rho)\right) \subset B\left(F\left(p_{1}\right), r^{\prime}\right) \cap B\left(F\left(p_{2}\right), r^{\prime}\right) .$$
Indeed, if $x^{\prime} \in B\left(x, r^{\prime}(1-\rho)\right)$ then $d\left(x^{\prime}, F\left(p_{i}\right)\right) \leq d\left(x^{\prime}, x\right)+d\left(x, F\left(p_{i}\right)\right)<r^{\prime}(1-\rho)+\rho r^{\prime}=$ $r^{\prime}$ for $i=1,2$. Thus (92) gives
$$\begin{aligned}
\operatorname{vol}_{g_{0}}\left(F\left(B\left(p_{1}, r^{\prime}\right) \cup B\left(p_{2}, r^{\prime}\right)\right)\right) & \leq 2 \operatorname{vol}_{\mathbf{H}^{n}}\left(r^{\prime}\right)-\operatorname{vol}_{\mathbf{H}^{n}}\left(r^{\prime}(1-\rho)\right) \\
& \leq 2 \operatorname{vol}_{\mathbf{R}^{n}}\left(r^{\prime}\right) \frac{\operatorname{vol}_{\mathbf{H}^{n}}\left(r^{\prime}\right)}{\operatorname{vol}_{\mathbf{R}^{n}}\left(r^{\prime}\right)}-(1-\rho)^{n} \operatorname{vol}_{\mathbf{R}^{n}}\left(r^{\prime}\right) \\
& \leq 2 \operatorname{vol}_{\mathbf{R}^{n}}\left(r^{\prime}\right) \frac{\operatorname{vol}_{\mathbf{H}^{n}}(\varepsilon)}{\operatorname{vol}_{\mathbf{R}^{n}}(\varepsilon)}-(1-\rho)^{n} \operatorname{vol}_{\mathbf{R}^{n}}\left(r^{\prime}\right) \\
& =\left(2 \frac{\operatorname{vol}_{\mathbf{H}^{n}}(\varepsilon)}{\operatorname{vol}_{\mathbf{R}^{n}}(\varepsilon)}-(1-\rho)^{n}\right) \operatorname{vol}_{\mathbf{R}^{n}}\left(r^{\prime}\right) .
\end{aligned}$$

For the third inequality we have used Bishop-Gromov's inequality. From (91) and (96), we find
$$(1-\rho)^{n} \leq 2\left(\frac{\operatorname{vol}_{\mathbf{H}^{n}}(\varepsilon)}{\operatorname{vol}_{\mathbf{R}^{n}}(\varepsilon)}-\vartheta(\varepsilon)\right) \rightarrow 0,$$
therefore
$$\rho \geq 1-2^{1 / n}\left(\frac{\operatorname{vol}_{\mathbf{H}^{n}}(\varepsilon)}{\operatorname{vol}_{\mathbf{R}^{n}}(\varepsilon)}-\vartheta(\varepsilon)\right)^{1 / n}:=1-c(\varepsilon) \rightarrow 1,$$
as $\varepsilon \rightarrow 0$. One has proved that inside the ball $B(p, r)$,
$$d_{g_{0}}\left(F\left(p_{1}\right), F\left(p_{2}\right)\right) \geq\left(1-c_{1}(\varepsilon)\right) d_{\infty}\left(p_{1}, p_{2}\right),$$
and the proof of the lemma follows by choosing $c(\varepsilon)$ so that $1-c_{1}(\varepsilon) \geq(1+c(\varepsilon))^{-1}$. \(\square\)

Remark 5.5. On the connected (see Remark 4.9) open set $F\left(\mathcal{R}_{\varepsilon}\right) \subset X$, the metric $g_{0}$ induces a distance $\rho_{\varepsilon}$. The above lemma shows that $F:\left(\stackrel{\circ}{\mathcal{R}}_{\varepsilon}, d_{\infty}\right) \longrightarrow\left(F\left(\stackrel{\circ}{\mathcal{R}}_{\varepsilon}\right), \rho_{\varepsilon}\right)$ is a $(1+c(\varepsilon))$-bi-Lipschitz homeomorphism. If one can prove that $\rho_{\varepsilon}=d_{g_{0}}$, one deduces that $\mathcal{R}_{\varepsilon}$ has bounded diameter. One then concludes that $\mathrm{d}_{\mathcal{G} \mathcal{H}}\left(Y_{k}, Y_{\infty}\right) \rightarrow 0$ and that $F:$ $Y_{\infty} \rightarrow X$ is isometric.

More precisely, we prove the following proposition.
Proposition 5.6. The set $F\left(\stackrel{\circ}{\mathcal{R}}_{\varepsilon}\right)$ satisfies,
\begin{itemize}
\item[1.] For any $x_{1}, x_{2} \in F\left(\stackrel{\circ}{\mathcal{R}}_{\varepsilon}\right), d_{g_{0}}\left(x_{1}, x_{2}\right)=\rho_{\varepsilon}\left(x_{1}, x_{2}\right)$.
\item[2.] $\overline{F\left(\stackrel{\circ}{\mathcal{R}}_{\varepsilon}\right)}=X$.
\item[3.] $F:\left(Y_{\infty}, d_{\infty}\right) \longrightarrow\left(X, d_{g_{0}}\right)$ is an isometry.
\end{itemize}

Proof. Let $x_{1}, x_{2} \in F\left(\stackrel{\circ}{\mathcal{R}}_{\varepsilon}\right)$. Without loss of generality, one can suppose that $x_{2}$ is not in the image of the cut-locus of $x_{1}$. Clearly, $\rho_{\varepsilon}\left(x_{1}, x_{2}\right) \geq d_{g_{0}}\left(x_{1}, x_{2}\right)$. Let $\gamma:[0,1] \longrightarrow X$ be a $g_{0}$-minimal geodesic from $x_{1}$ to $x_{2}$. We do not know that $\gamma$ is in $F\left(\stackrel{\circ}{\mathcal{R}}_{\varepsilon}\right)$ we then prove that there exist paths in $F\left(\stackrel{\circ}{\mathcal{R}}_{\varepsilon}\right)$ arbitrarily close to $\gamma$. Let $r>0$ be a radius such that $B_{g_{0}}\left(x_{2}, r\right) \subset F\left(\stackrel{\circ}{\mathcal{R}}_{\varepsilon}\right)$. We consider geodesics with the origin $x_{1}$ and the extremity in $B\left(x_{2}, \delta\right)$, for a small $\delta>0$. More precisely, let $u=\dot{\gamma}(0)$, then for any $v \in U_{x_{1}} X$ such that and $u \perp v$, one defines $\gamma_{s, v}(t)=\exp _{x_{1}}\left(t(u+s . v) d\left(x_{1}, x_{2}\right)\right)$. There exists $r(\delta)>0$ such that $\gamma_{s, v}(1) \in B\left(x_{2}, \delta\right)$ if $|s| \leq r(\delta)$ and one can choose $r(\delta) \rightarrow 0$ as $\delta$ goes to 0.

We claim that for every $\delta>0$, there exists such $\gamma_{s, v}$ which is imbedded in $F\left(\stackrel{\circ}{\mathcal{R}}_{\varepsilon}\right)$.
Let us show that one can find such $\gamma_{s, v}$ disjoint from $F(\mathcal{S})$, where $\mathcal{S}$ is the singular set of $Y_{\infty}$ defined in 4.5. The idea is that if any $\gamma_{s, v}$ would hit $F(\mathcal{S})$ at least in one
point, then the Hausdorff dimension of $F(\mathcal{S})$ would be larger than $n-1$, which is a contradiction. More precisely, one considers a truncated cone $U_{\delta}$ defined as follows. Let
$$\Gamma:] 0, r(\delta)] \times\left(U_{x_{1}} X \cap u^{\perp}\right) \times[0,1] \rightarrow X$$
be defined by $\Gamma(s, v, t)=\gamma_{s, v}(t)$. If $\delta$ is sufficiently small, $\Gamma$ is an embedding. One defines $\left.\left.U_{\delta}=\Gamma(] 0, r(\delta)\right] \times\left(U_{x_{1}} X \cap u^{\perp}\right) \times[0,1]\right)$. Let us denote by $U_{\delta}(1 / 2)$ the hypersurface in $U_{\delta}$ defined as $\left.\left.\left.\Gamma(] 0, r(\delta)\right]\right) \times\left(U_{x_{1}} X \cap u^{\perp}\right) \times\{1 / 2\}\right)$.
![](https://cdn.mathpix.com/cropped/328003d9-9205-40c8-bd58-a3877268b784-31.jpg?height=336&width=1052&top_left_y=651&top_left_x=523)
Let $P: U_{\delta} \rightarrow U_{\delta}(1 / 2)$ be the projection along geodesics defined by $P\left(\gamma_{s, v}(t)\right)=\gamma_{s, v}(1 / 2)$. Since we are on a fixed Riemannian manifold, there exists a constant $C>0$ such that $P$ is $C$-lipschitz from $U_{\delta}$ to $X$. In particular, $P$ decreases the Hausdorff dimension,that is
$$\begin{aligned}
\operatorname{dim}_{\mathcal{H}}\left(P\left(U_{\delta} \cap F(\mathcal{S})\right)\right) & \leq \operatorname{dim}_{\mathcal{H}}\left(U_{\delta} \cap F(\mathcal{S})\right) \\
& \leq \operatorname{dim}_{\mathcal{H}}(\mathcal{S}) \\
& \leq n-2 \\
& <\operatorname{dim} U_{\delta}(1 / 2)=n-1 .
\end{aligned}$$
Hence, there exists $x \in U_{\delta}(1 / 2)$ such that $x \notin \Pi(F(\mathcal{S}))$. This implies that the geodesic $\gamma_{s, v}$ such that $x=\gamma_{s, v}(1 / 2)$ does not intersect $F(\mathcal{S})$.
We now prove that $\gamma_{s, v}$ is embedded in $F\left(\stackrel{\circ}{\mathcal{R}}_{\varepsilon}\right)$. Let $t_{0} \in(0,1]$ be maximal such that $\gamma_{s, v}\left(\left[0, t_{0}[) \subset F\left(\stackrel{\circ}{\mathcal{R}}_{\varepsilon}\right)\right.\right.$. By Lemma 5.4, the path $\beta=F^{-1} \circ \gamma_{s, v}$ is well-defined on $\left[0, t_{0}\left[\right.\right.$ and has a length bounded by $(1+c(\varepsilon)) d\left(x_{1}, x_{2}\right)$. Since $F$ is bi-Lipschitz, $d_{g_{k}}\left(\beta(t), \beta\left(t^{\prime}\right)\right) \geq C\left|t^{\prime}-t\right|$ and hence there exists a limit $p=\lim _{t \rightarrow t_{0}} \beta(t) \in Y_{\infty}$. By continuity of $F, F(p)=\gamma_{s, v}\left(t_{0}\right)$ and since $\gamma_{s, v}\left(t_{0}\right) \notin F(\mathcal{S})$ we have that $p \notin \mathcal{S}$. This implies that $p \in \mathcal{R}=\cap_{\varepsilon} \mathcal{R}_{\varepsilon}=\cap_{\varepsilon>0} \stackrel{\circ}{\mathcal{R}}_{\varepsilon}$ and consequently that $t_{0}=1$, because $\stackrel{\circ}{\mathcal{R}}_{\varepsilon}$ is open.

Hence
$$\begin{aligned}
\rho_{\varepsilon}\left(x_{1}, x_{2}\right) & \leq \ell\left(\gamma_{s, v}\right)+d_{0}\left(\gamma_{s, v}(1), x_{2}\right) \\
& \leq \sqrt{1+r^{2}(\delta)} d_{0}\left(x_{1}, x_{2}\right)+\delta
\end{aligned}$$
As $\delta$ was arbitrary, this gives $\rho_{\varepsilon}\left(x_{1}, x_{2}\right) \leq d_{0}\left(x_{1}, x_{2}\right)$.
The second assertion is proved in a similar way. Suppose there is a ball $B(x, r) \subset$ $X \backslash F\left(\stackrel{\circ}{\mathcal{R}}_{\varepsilon}\right)$ and consider a geodesic $\gamma$ from a point $x_{1}$ inside $F\left(\stackrel{\circ}{\mathcal{R}}_{\varepsilon}\right)$ to $x$. Then we
find another geodesic from $x_{1}$, close to $\gamma$, disjoint from $F(\mathcal{S})$ and with extremity in $X \backslash F\left(\stackrel{\circ}{\mathcal{R}}_{\varepsilon}\right)$. Arguing as above, we find a contradiction.
Now 3) is straightforward. Using the density of $\stackrel{\circ}{\mathcal{R}}_{\varepsilon}$ in $Y_{\infty}$ and of $F\left(\stackrel{\circ}{\mathcal{R}}_{\varepsilon}\right)$ in $X$, we find that $F:\left(Y_{\infty}, d_{\infty}\right) \longrightarrow\left(X, d_{0}\right)$ is a $(1+c(\varepsilon))$-bi-Lipschitz homeomorphism for any $0<\varepsilon<\varepsilon_{0}$ thus is isometric. \(\square\)

End of Proof of theorem 1.3. Proposition 5.6 implies that the diameter of $\left(Y, g_{k}\right)$ remains bounded. Thus, $\mathrm{d}_{\mathcal{G} \mathcal{H}}\left(\left(Y, g_{k}\right),\left(Y_{\infty}, d_{\infty}\right)\right) \rightarrow 0$ (for the non pointed convergence). As $\left(Y_{\infty}, d_{\infty}\right)$ is isometric to $\left(X ; g_{0}\right)$, one deduces that $\mathrm{d}_{\mathcal{G} \mathcal{H}}\left(\left(Y, g_{k}\right),\left(X, g_{0}\right)\right) \rightarrow 0$ as $k \rightarrow \infty$. By theorem A.1.12 of [7], $Y$ is diffeomorphic to $X$. The fact that $f$ is homotopic to a diffeomorphism is classic for hyperbolic manifolds. \(\square\)

\section*{References}
[1] Laurent Bessières, Un théorème de rigidité différentielle Comment. Math. Helv. 73, 1998, no.3, 443-479.
[2] Michaël Anderson, Canonical metrics on 3-manifolds and 4-manifolds Asian Journal of Math., vol. 10, (2006), 127-164.
[3] Yury Burago, Victor Zalgaller, Geometric inequalities. Translated from the Russian by A. B. Sosinski. Grundlehren der Mathematischen Wissenschaften [Fundamental Principles of Mathematical Sciences], 285. Springer Series in Soviet Mathematics. Springer-Verlag, Berlin, 1988. xiv+331 pp. ISBN: 3-540-13615-0
[4] Dmitri Burago, Yury Burago, Sergei Ivanov, A course in metric geometry Graduate Studies in Mathematics, 33. American Mathematical Society, Providence, RI, 2001. xiv+415 pp. ISBN: 0-8218-2129-6
[5] Gérard Besson, Gilles Courtois, Sylvain Gallot Entropies et rigidités des espaces localement symétriques de courbure strictement négative [Entropy and rigidity of locally symmetric spaces with strictly negative curvature] Geom. Funct. Anal. 5 (1995), no. 5, 731-799.
[6] Gérard Besson, Gilles Courtois, Sylvain Gallot, Minimal entropy and Mostow's rigidity theorem Ergodic Theory Dynam. Systems 16 (1996), no. 4, 623-649.
[7] Jeff Cheeger, Tobias Colding, On the structure of spaces with Ricci curvature bounded below I, J. Diff. Geom. 46 (1997), 406-480.
[8] Jeff Cheeger, Tobias Colding, On the structure of spaces with Ricci curvature bounded below II, J. Diff. Geom. 54 (2000), 13-35.
[9] Jeff Cheeger, Tobias Colding Lower bounds on Ricci curvature and the almost rigidity of warped products Ann. of Math. (2) 144 (1996), no. 1, 189-237.
\begin{itemize}
\item[] [10] Herbert Federer, Geometric measure theory Die Grundlehren der mathematischen Wissenschaften, Band 153 Springer-Verlag New York Inc., New York 1969 xiv+676 pp.
\item[] [11] Michaël Gromov, Jacques Lafontaine, Pierre Pansu, Structures métriques pour les variétés riemanniennes Cédic Fernand Nathan.
\item[] [12] Michaël Gromov, Metric structures for Riemannian and non-Riemannian spaces Based on the 1981 French original. With appendices by M. Katz, P. Pansu and S. Semmes. Translated from the French by Sean Michael Bates. Reprint of the 2001 English edition. Modern Birkhäuser Classics. Birkhäuser Boston, Inc., Boston, MA, 2007. xx+585 pp. ISBN: 978-0-8176-4582-3; 0-8176-4582-9 53C23 (53-02)
\item[] [13] Michael Gromov, Volume and bounded cohomology Inst. Hautes tudes Sci. Publ. Math. No. 56 (1982), 5-99 (1983).
\item[] [14] Frank Morgan, Geometric measure theory, A beginner's guide, Third edition. Academic Press, Inc., San Diego, CA, 2000. x+226 pp. ISBN: 0-12-506851-4
\item[] [15] Thomas F. Farrell, Lowell E. Jones, Negatively curved manifolds with exotic smooth structures J. Amer. Math. Soc. 2 (1989), no. 4, 899-908.
\item[] [16] Osamu Kobayashi, Scalar curvature of a Metric with Unit Volume, Math. Ann. 279, 253-265 (1987).
\end{itemize}
