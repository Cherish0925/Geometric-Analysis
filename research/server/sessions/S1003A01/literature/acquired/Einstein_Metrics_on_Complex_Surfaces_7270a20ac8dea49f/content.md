---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: dg-ga_9506012.pdf
converter: mathpix
format: mmd
---

\title{
Einstein Metrics on Complex Surfaces
}

\author{
Claude LeBrun * \\ SUNY Stony Brook
}

June, 1995

\section*{1 Introduction}

Suppose $M$ a compact manifold which admits an Einstein metric $g$ which is Kähler with respect to some complex structure $J$. Is every other Einstein metric $h$ on $M$ also Kähler-Einstein? If the complex dimension of $(M, J)$ is $\geq 3$, the answer is generally no; for example, $\mathbf{C P}_{3}$ admits both the Fubini-Study metric, which is Kähler-Einstein, and a non-Kähler Einstein metric [2] obtained by appropriately squashing the fibers of the twistor projection $\mathbf{C P}_{3} \rightarrow S^{4}$. Iterated Cartesian products with $\mathbf{C P}_{1}$ then provide counterexamples in all higher dimensions.

However, if $M$ is a 4-manifold, so that $(M, J)$ is a compact complex surface, there is reason to hope that the anwer to the above question might be yes. Indeed, Hitchin [12] was able to answer the question in the affirmative for complex surfaces which admit Ricci-flat Kähler metrics; his argument hinges on the fact that any 4-dimensional Einstein manifold satisfies
$$2 \chi+3 \tau=\frac{1}{4 \pi^{2}} \int\left(2\left|W_{+}\right|^{2}+\frac{s^{2}}{24}\right) d \mu$$
where $s$ is the scalar curvature and $W_{+}$is the self-dual Weyl curvature, and on the observation that $\left|W_{+}\right|^{2}=s^{2} / 24$ for any Kähler surface. Much more recently, Seiberg-Witten theory [13, 24] has provided new insights when our

\footnotetext{
*Supported in part by NSF grant DMS-92 .
}

Kähler-Einstein metric has $s<0$; in this case the Kähler-Einstein metrics are absolute minima of the Riemannian functional $\int s^{2} d \mu$, and a close cousin of Hitchin's argument therefore implies [15] the desired result for compact quotients $M=\mathbf{C H}_{2} / \Gamma$ of the unit ball in $\mathbf{C}^{2}$.

While the answer to the above question regarding Einstein 4-manifolds still remains elusive, a related, narrower problem is much more tractable. Namely, suppose that $(M, J)$ is a compact complex surface with Hermitian metric $h$; that is, it is supposed that the Riemannian metric $h$ is $J$-invariant. If $h$ is an Einstein metric, is it necessarily Kähler with respect to $J$ ? In general, the answer is no; the Page metric [19, 2] on $\mathbf{C P}_{2} \# \overline{\mathbf{C P}}_{2}$ is a counterexample. However, as will be demonstrated in this note, this counter-example is nearly unique:

Theorem A Let $\left(M^{4}, J\right)$ be a compact complex surface which admits an Einstein metric $h$ which is Hermitian but not Kähler with respect to $J$. Then $(M, J)$ is obtained from $\mathbf{C P}_{2}$ by blowing up one, two, or three points in general position. Moreover, the isometry group of $h$ contains a 2-torus.

In the one-point case, the proof will also show that $(M, h)$ is precisely the Page metric, up to isometry and rescaling.

The proof of this result hinges upon the fact that if a Hermitian metric on a complex surface is Einstein, it must be conformally Kähler; this follows from the combined results of Goldberg-Sachs [10] and Derdzinski [7]. Note that the anologous statement is false for complex manifolds of higher dimension, as is demonstrated by the the "squashed" Einstein metric on $\mathbf{C P}_{3}$.

Specializing our initial question, we might now ask whether a compact complex surface $(M, J)$ can admit both a Kähler-Einstein metric and an Einstein Hermitian metric which is not Kähler. The answer is no, unless perhaps if $M=\mathbf{C P}_{2} \# 3 \overline{\mathbf{C P}}_{2}$. This follows because one- and two-point point blow-ups of $\mathbf{C P}_{2}$ have non-reductive automorphism groups, and hence [14, 2] do not carry Kähler-Einstein metrics. The concluding section of this article will describe a computional method of determining whether every Einstein Hermitian metric on $\mathbf{C P}_{2} \# 3 \overline{\mathbf{C P}}_{2}$ is actually Kähler-Einstein. The same method may be applied to the existence problem for Einstein Hermitian metrics on $\mathbf{C P}_{2} \# 2 \overline{\mathbf{C P}}_{2}$.
Acknowedgement. The author warmly thanks Jerzy Lewandowski for stimulating his interest in the problem.

\section*{2 Einstein Hermitian Metrics}

In this section, we will study Einstein metrics which are Hermitian with respect to some integrable complex structure on a compact complex surface. These will, for the sake of brevity, sometimes be referred to as Einstein Hermitian metrics, so it is worth warning the reader that these are not $a$ priori Hermite-Einstein in the sense of the theory of holomorphic vector bundles.

Let us begin with a local result concerning the conformal curvature of Hermitian Einstein metrics:

Lemma 1 (Goldberg-Sachs) Let $(M, h)$ be an oriented Einstein 4-manifold. Assume that there is an orientation-compatible integrable complex structure $J$ on $M$ such that $h$ is $J$-invariant. Then the self-dual Weyl curvature $W_{+}$ of $g$ is also $J$-invariant. In particular, $W_{+}: \wedge^{+} \rightarrow \wedge^{+}$has at most 2 distinct eigenvalues at every point of $M$.

A Lorentzian analogue of this result was first discovered by Goldberg and Sachs [10], but two decades then elapsed before it was realized [20, 5] that the same calculation concerning null involutive sub-bundles of the complex tangent bundle proves a theorem concerning Riemannian signature metrics. For a transparent spinorial proof, cf. [21] or [18].

The self-dual Weyl curvature may be identified with a symmetric tracefree endomorphism of the bundle $\wedge^{+}$of self-dual 2-forms on our Riemannian 4-manifold, and so has 3 eigenvalues at each point. Under the action $\mathbf{Z}_{2}$ action generated an oriented orthogonal complex structure $J$, however, the rank-3 bundle $\wedge^{+}$decomposes into irreducible sub-bundles of rank 1 and 2, and two of the eigenvalues of a $J$-invariant $W_{+}$must therefore coincide. The following result of Derdzinski [7, Theorem 2], however, deals with Einstein manifolds with precisely this property.

Lemma 2 (Derdzinski) Let $(M, h)$ be a connected oriented Einstein manifold such that $W_{+}$has at most 2 eigenvalues at each point. Then either $W_{+} \equiv 0$, or else $W_{+}$has exactly 2 distinct eigenvalues at each point. In the latter case, moreover, the conformally related metric $g=2 \sqrt[3]{3}\left|W_{+}\right|^{2 / 3} h$ is locally Kähler, and is locally compatible with exactly one pair $\pm J$ of oriented complex structures. The scalar curvature $s$ of $g$ is then nowhere zero, and $h=s^{-2} g$.

The case in which our Hermitian metric $g$ satisfies $W_{+} \equiv 0$ may easily be handles by invoking the work of Boyer:

Lemma 3 Let $(M, J, h)$ be an Einstein Hermitian surface with $W_{+} \equiv 0$. Then $h$ is Ricci-flat and Kähler with respect to $J$.

Proof. Since $(M, J, h)$ is Hermitian anti-self-dual, a result of Boyer [4] tells us that either $h$ is conformal to a scalar-flat Kähler metric, or else that $b_{1}(M)=1$ and the conformal class $[g]$ has positive Yamabe constant. The latter case, however, can be excluded because our Einstein metric $h$ would have to have positive scalar curvature, and hence positive Ricci curvature; but this would imply that $b_{1}(M)=0$ by Bochner's theorem [3, 2], and so lead to a contradiction. Hence $h$ is conformal to a scalar-flat Kähler metric, and, since it is the Yamabe metric in its conformal class, it must therefore itself be scalar-flat and Kähler. \(\square\)

Combining these known facts now yields the following:
Proposition 1 Let $(M, J, h)$ be a compact Einstein Hermitian manifold of complex dimension 2. Then either $(M, J, h)$ is a Kähler-Einstein manifold, or else there is an extremal Kähler metric $g$ on $(M, J)$ with non-constant scalar curvature $s>0$ such that $h=s^{-2} g$.

Proof. If $W_{+} \equiv 0$, Lemma 3 tells us that $h$ is Kähler, and we are done. Otherwise, Lemma 2 asserts that the metric $g$ of is locally Kähler with respect to exactly 2 complex structures, namely the two almost-complex structures with respect to which $W_{+}$is invariant; and by Lemma 1, the globally-defined complex structure $J$ is one of these. Thus $(M, J, g)$ is a Kähler manifold. But since $g$, being conformal to Einstein, is a critical point of the conformally invariant functional $\int\left|W_{+}\right|^{2} d \mu=6 \pi^{2} \tau(M)+\frac{1}{2} \int|W|^{2} d \mu$, and since $\int\left|W_{+}\right|^{2} d \mu=\frac{1}{24} \int s^{2} d \mu$ for any Kähler metric, it follows that $g$ is an extremal Kähler metric in the sense of Calabi. Thus $\xi=J \operatorname{grad}_{g} s$ is a Killing field of $g$, and hence of $h=s^{-2} g$. Now a result of Bochner [3, 2] says that a compact manifold of non-positive Ricci curvature can have a Killing field only if the field is parallel; but $\xi$ has a zero at the minimum of $s^{2}$, and thus can be parallel only if it is zero. Thus we either have $s=$ const , in which case $h$ is Kähler-Einstein, or else the Einstein metric $h$ has positive scalar curvature.

But if the latter happens, the fact that $g$ is in the same conformal class as $h$ implies that its scalar curvature $s \neq 0$ must also be positive. \(\square\)

While much of the above was already known to Derdzinski, the next observation appears to be new:

Proposition 2 Let $\left(M^{4}, J\right)$ be a compact complex surface which admits an Einstein metric h which is Hermitian but not Kähler with respect to J. Then the anti-canonical line bundle $K^{-1}$ of $(M, J)$ is ample.

Proof. Let $r$ denote the Ricci curvature of the Kähler metric $g$, and let $\hat{r}=\frac{k}{4} h$ denote the Ricci curvature of the Einstein metric $h=s^{-2} g$; here the constant $k=\hat{s}$ is the scalar curvature of $h$. The standard formula [2] for the effect of a conformal change $g \mapsto \psi^{2} g$ on the Ricci curvature tells us that
$$\hat{r}_{a b}-r_{a b}=2 \psi \nabla_{a} \nabla_{b} \psi^{-1}-\left(\psi \Delta \psi^{-1}+3|d \log \psi|^{2}\right) g_{a b},$$
where the length of 1 -forms is measured with respect to $g$; in our case, we therefore have
$$\frac{k}{4} h_{a b}=r_{a b}+2 s^{-1} \nabla_{a} \nabla_{b} s-\left(s^{-1} \Delta s+3|d \log s|^{2}\right) g_{a b}$$
and hence
$$s^{-1} \Delta s+2|d \log s|^{2}=\frac{s-k s^{-2}}{6}$$
It follows that
$$r_{a b}+2 s^{-1} \nabla_{a} \nabla_{b} s=\left(\frac{2 s+k s^{-2}}{12}+|d \log s|^{2}\right) g_{a b} .$$
Since both the Kähler metric $g$ and its Ricci curvature $r$ are invariant under the action of $J$ on the tangent space, this implies, in particular, that the Hessian of $s$ is also $J$-invariant:
$$\nabla_{a} \nabla_{b} s=J_{a}{ }^{c} J_{b}{ }^{d} \nabla_{c} \nabla_{d} s .$$
(We remark in passing that (2) is exactly equivalent to Calabi's extremal Kähler metric condition
$$\left.\nabla_{\bar{\mu}} \nabla^{\nu} s=0 .\right)$$

Now $2 \pi c_{1}=2 \pi c_{1}\left(K^{-1}\right)$ is the de Rham class of the Ricci form $\rho$ of our Kähler metric $g$, and this 2-form is related to the Ricci curvature by
$$r_{a b}=\rho_{a c} J_{b}^{c} .$$
Because the scalar curvature $s$ is a smooth positive function on $M$, yet another de Rham representative of $2 \pi c_{1}\left(K^{-1}\right)$ is the (1, 1)-form $\hat{\rho}$ defined by
$$\begin{aligned}
\hat{\rho} & =\rho+2 i \partial \bar{\partial} \log s \\
& =\rho+d J d \log s .
\end{aligned}$$
But the (1, 1)-form $\hat{\rho}$ is 'positive,' in the sense that the symmetric tensor field $q$ defined by
$$q_{a b}=\hat{\rho}_{a c} J_{b}{ }^{c}$$
is everywhere positive-definite. Indeed,
$$\begin{aligned}
\hat{\rho}_{a b} & =\rho_{a b}+2 \nabla_{[a} J^{c}{ }_{b]} \nabla_{c} \log s \\
& =\rho_{a b}-J_{b}{ }^{c} \nabla_{a} \nabla_{c} \log s+J_{a}{ }^{c} \nabla_{b} \nabla_{c} \log s,
\end{aligned}$$
so that
$$\begin{aligned}
q_{a b}= & \hat{\rho}_{a d} J_{b}{ }^{d} \\
= & r_{a b}+\nabla_{a} \nabla_{b} \log s+J_{a}{ }^{c} J_{b}{ }^{d} \nabla_{c} \nabla_{d} \log s \\
= & r_{a b}+s^{-1} \nabla_{a} \nabla_{b} s+s^{-1} J_{a}{ }^{c} J_{b}{ }^{d} \nabla_{c} \nabla_{d} s \\
& \quad-\left(\nabla_{a} \log s\right) \nabla_{b} \log s-J_{a}{ }^{c} J_{b}{ }^{d}\left(\nabla_{c} \log s\right) \nabla_{d} \log s .
\end{aligned}$$
Substitution from (1) and (2) thus yields
$$\begin{aligned}
q_{a b} & =r_{a b}+2 s^{-1} \nabla_{a} \nabla_{b} s-\left(\nabla_{a} \log s\right) \nabla_{b} \log s-J_{a}^{c} J_{b}^{d}\left(\nabla_{c} \log s\right) \nabla_{d} \log s \\
& =\frac{2 s+k s^{-2}}{12} g_{a b}+s^{-2}\left[|d s|^{2} g_{a b}-(d s)_{a}(d s)_{b}-(J d s)_{a}(J d s)_{b}\right]
\end{aligned}$$
which is manifestly positive-definite because $s$ and $k$ are both positive. Hence $c_{1}\left(K^{-1}\right)$ is represented by the positive (1,1)-form $\hat{\rho} / 2 \pi$, and the Kodaira embedding theorem [9] therefore tells us that $K^{-1}$ is ample. \(\square\)

This immediately implies the following:

Theorem 1 Let $\left(M^{4}, J\right)$ be a compact complex surface which admits an Einstein metric $h$ which is Hermitian but not Kähler with respect to $J$. Then $(M, J)$ is obtained from $\mathbf{C P}_{2}$ by blowing up one, two, or three points in general position. Moreover, the isometry group of $h$ contains a 2-torus.

Here 'general position' means that no two points coincide and no three are collinear. After a projective-linear transformation of $\mathbf{C P}_{2}$, we may therefore assume that our collection of points is a subset of $\{[1: 0: 0],[0: 1: 0],[0:$ $0: 1]\}$. There are thus only 3 possible biholomorphism types for $(M, J)$.
Proof. Since the anti-canonical line bundle of $(M, J)$ is ample, surface classification [1, 11] tells us that $(M, J)$ is either $\mathbf{C P}_{1} \times \mathbf{C P}_{1}$ or else is obtained from $\mathbf{C P}_{2}$ by blowing up $k$ distinct points in general position, $0 \leq k \leq 8$. However, we also know that $(M, J)$ carries an extremal Kähler metric $g$ of non-constant scalar curvature, so the Lie algebra of holomorphic vector fields must be non-semi-simple (and in particular non-trivial). This eliminates $\mathbf{C P}_{2}, \mathbf{C P}_{1} \times \mathbf{C P}_{1}$ and the $k$-point general-position blow-ups of $\mathbf{C P}_{2}$ for which $4 \leq k \leq 8$.

Thus $(M, J)$ must be obtained from $\mathbf{C P}_{2}$ by blowing up 1, 2, or 3 points in general position. Choose homogeneous coördinates on $\mathbf{C P}_{2}$ so that the points in question are elements of $\{[1: 0: 0],[0: 1: 0],[0: 0: 1]\}$, and observe that the $U(1) \times U(1)$ action defined on $\mathbf{C P}_{2}$ by
$$\left[\begin{array}{ccc}
e^{i \theta} & & \\
& e^{i \phi} & \\
& & 1
\end{array}\right]$$
then lifts to the blow-up $M$; thus the automorphism group of $(M, J)$ contains the compact subgroup $U(1) \times U(1)$. But [6] the identity component of the isometry group of an extremal Kähler metric is a maximal compact subgroup of the identity component of the complex automorphism group; and since the maximal compact is unique up to conjugation, a suitable change of homogeneous coördinates will make the extremal Kähler metric $g$ invariant under above torus action. Since any isometry of $g$ is also an isometry of $h=s^{-2} g$, it follows that the isometry group of $h$ also contains $U(1) \times U(1)$. \(\square\)

If $(M, g)$ is a compact oriented Einstein 4-manifold with holonomy $S O(4)$ for which $W_{+}$has at most 2 eigenvalues at each point, Lemma 2 thus implies that $M$ is diffeomorphic to $\mathbf{C P}_{2} \# \overline{\mathbf{C P}}_{2},\left(\mathbf{C P}_{2} \# \overline{\mathbf{C P}}_{2}\right) / \mathbf{Z}_{2}, \mathbf{C P}_{2} \# 2 \overline{\mathbf{C P}}_{2}$, or $\mathbf{C P}_{2} \# 3 \overline{\mathbf{C P}}_{2}$.

\section*{3 Critical Kähler Classes}

In the last section, we saw that that a non-Kähler Einstein Hermitian surface must be of the form $\left(M, J, s^{-2} g\right)$, where $(M, J)$ is obtained from $\mathbf{C P}_{2}$ by blowing up 1, 2, or 3 points in general position, and where $g$ is an extremal Kähler metric of non-constant scalar curvature $s>0$. In the one-point case, $h=s^{-2} g$ must be the Page metric, up to isometry and rescaling, because the isometry group of the extremal Kähler metric $g$ necessarily contains $U(2)$. In the other cases, we can learn a bit more by asking which Kähler class might contain such a metric $g$.

Let $[\omega]$ denote the Kähler class of our putative metric $g$. Since $g$ is extremal, there is an open neighborhood of $[\omega] \in H^{1,1}(M)=H^{2}(M)$ of classes which are represented by extremal Kähler metrics obtained as deformations of $g$. On this open set, consider the functional $\mathcal{A}$ which assigns to each cohomology class the integral $\int s^{2} d \mu$ of the square of the scalar curvature of the corresponding extremal Kähler metric. Then $[\omega]$ is a critical point of this functional, since $\int s^{2} d \mu=24 \int\left|W_{+}\right|^{2} d \mu$ for any Kähler metric, and the conformally Einstein metric $g$ is a critical point of $\int\left|W_{+}\right|^{2} d \mu$, considered as a functional on the space of all Riemannian metrics.

This would be a useless observation were it not for the fact that $\mathcal{A}$ has an invariant meaning. Indeed, if $[\omega]$ is the Kähler class of an arbitrary extremal Kähler metric, we have
$$\mathcal{A}=s_{0}^{2} \int d \mu+\int\left(s-s_{0}\right)^{2} d \mu=32 \pi^{2} \frac{\left(c_{1} \cdot[\omega]\right)^{2}}{[\omega]^{2}}-\mathcal{F}(\xi,[\omega])$$
where $s_{0}$ is the average value of the scalar curvature, $\mathcal{F}$ denotes the Futaki functional, and $\xi=\operatorname{grad}^{1,0} s$ is the extremal vector field of the class $[\omega]$. The latter, moreover, may be determined up to conjugation even [8] without knowing the extremal metric explicitly. It is enough, in fact, to be able to calculate the Futaki invariant explicitly, and this has been done elsewhere [16] for the blow-up of $\mathbf{C P}_{2}$ at three points in general position.

Let $(M, J)$ be the blow-up of $\mathbf{C P}_{2}$ at the points $[1: 0: 0],[0: 1: 0]$, and $[0: 0: 1]$. The three blown-up points and the proper transforms of the lines joining them form a hexagon of (-1)-curves in $M$ :
![](https://cdn.mathpix.com/cropped/5794d21a-de1c-4407-8bf5-47774239a4af-09.jpg?height=307&width=1081&top_left_y=466&top_left_x=489)
Since $b_{2}(M)=4$, there are two relations between these six curves- namely, the three differences between opposite sides are homologous. Thus, while the the areas $\alpha, \beta$ and $\gamma$ of the three blow-up curves are independent, the only remaining free parameter is the difference $\delta$ between the areas of opposite sides of the hexagon. By performing a Cremona transformation
$$\left[z_{0}: z_{1}: z_{2}\right] \mapsto\left[1 / z_{0}: 1 / z_{1}: 1 / z_{2}\right]$$
if necessary, we may arrange that $\delta \geq 0$, and we will assume henceforth that this has been done.

Let us consider the hyperplane $P \subset H^{2}\left(\mathbf{C P}_{2} \# 3 \overline{\mathbf{C P}}_{2}\right)$ of Kähler classes defined by the condition $\beta=\gamma$ :
![](https://cdn.mathpix.com/cropped/5794d21a-de1c-4407-8bf5-47774239a4af-09.jpg?height=307&width=455&top_left_y=1388&top_left_x=734)
Since $\mathcal{A}$ is invariant under the $\mathbf{Z}_{2}$-action induced by
$$\left[z_{0}: z_{1}: z_{2}\right] \mapsto\left[z_{0}: z_{2}: z_{1}\right],$$
and because $P$ is exactly the fixed point set of this action, any critical point of $\left.\mathcal{A}\right|_{P}$ is necessarily a critical point of $\mathcal{A}$, though the converse of course need not be true. Now it turns out that $\left.\mathcal{A}\right|_{P}$ is rather easier to compute that $\mathcal{A}$, and we shall therefore only consider this restricted functional in the following discussion. It should be emphasized, however, that this restriction is completely ad hoc, and would have to be eliminated in order to obtain a definitive treatment of the problem.

For any Kähler class in $P$, the extremal Kähler vector field $\xi$ must be invariant under $\left[z_{0}: z_{1}: z_{2}\right] \mapsto\left[z_{0}: z_{2}: z_{1}\right]$, and so must be a multiple
of the generator $\Xi$ of the $\mathbf{C}^{\times}$-action $\left[z_{0}: z_{1}: z_{2}\right] \mapsto\left[\zeta z_{0}: z_{1}: z_{2}\right]$. Now $\Xi=\operatorname{grad}^{1,0} t$ for a real-valued function $t$ which, by the methods of [16], and preferably with the aid of a symbolic-manipulation program such as Maple, can be shown to satisfy
$$\begin{aligned}
{[12 \pi \omega]^{2} \int\left(t-t_{0}\right)^{2} d \mu=} & 360 \beta^{3} \alpha \delta^{2}+193 \beta^{3} \alpha^{2} \delta+276^{4} \alpha \delta+216 \beta^{2} \delta^{3} \alpha \\
& +60 \beta \delta^{4} \alpha+48 \beta \delta^{3} \alpha^{2}+\delta^{6}+12 \beta^{6}+96 \beta^{4} \alpha^{2} \\
& +72 \beta^{5} \alpha+144 \beta^{2} \delta^{2} \alpha^{2}+120 \beta^{3} \delta^{3}+138 \beta^{4} \delta^{2} \\
& +72 \beta^{5} \delta+54 \beta^{2} \delta^{4}+12 \beta \delta^{5}+6 \delta^{5} \alpha+6 \delta^{4} \alpha^{2}
\end{aligned}$$
where $t_{0}$ is the average value of $t$. On the other hand, it was shown in [16] that
$$[\omega]^{2} \mathcal{F}(\Xi,[\omega])=4(\beta-\alpha) \delta\left[\frac{\delta^{2}}{3}+\beta \delta+\beta^{2}\right] .$$
Since $\mathcal{F}(\Xi,[\omega])=-\int\left(t-t_{0}\right)\left(s-s_{0}\right) d \mu$, an explicit formula for $\left.\mathcal{A}\right|_{P}$ can now be deduced by setting $\left(s-s_{0}\right)=\lambda\left(t-t_{0}\right)$ and solving for $\lambda$. The upshot is that $\left(\left.\mathcal{A}\right|_{P}\right) / 96 \pi^{2}$ is the quotient of two homogeneous sextics with integer coefficients, namely
$$\begin{aligned}
& 32 \beta^{6}+160 \beta^{5} \alpha+176 \beta^{5} \delta+318 \beta^{4} \delta^{2}+136 \beta^{4} \alpha^{2}+536 \beta^{4} \alpha \delta \\
& +32 \beta^{3} \alpha^{3}+280 \beta^{3} \delta^{3}+696 \beta^{3} \alpha \delta^{2}+320 \beta^{3} \alpha^{2} \delta+440 \beta^{2} \delta^{3} \alpha \\
& +276 \beta^{2} \delta^{2} \alpha^{2}+48 \beta^{2} \alpha^{3} \delta+132 \beta^{2} \delta^{4}+32 \beta \delta^{5}+104 \beta \delta^{3} \alpha^{2} \\
& +24 \beta \alpha^{3} \delta^{2}+136 \beta \delta^{4} \alpha+4 \alpha^{3} \delta^{3}+14 \delta^{4} \alpha^{2}+16 \delta^{5} \alpha+3 \delta^{6}
\end{aligned}$$
divided by the right-hand side of (3). Notice that $\left.\mathcal{A}\right|_{P}$ in particular has homogeneity 0, as it must be since $\int s^{2} d \mu$ is scale-invariant in dimension 4.

To double-check our fomulæ, let us first revisit the case of $\mathbf{C P}_{2} \# \overline{\mathbf{C P}}_{2}$. This can be done by simply setting $\beta=0$ in the above expressions, so that
$$\frac{1}{4 \pi^{2}} \int_{\mathbf{C P}_{2} \# \overline{\mathbf{C P}}_{2}} \frac{s^{2}}{24} d \mu=\frac{4+14 x+16 x^{2}+3 x^{3}}{x\left(6+6 x+x^{2}\right)},$$
where $x=\delta / \alpha$. For $x>0$, this has a unique critical point, its absolute minimum, when $x=2.183933404$... The Page metric must be conformal to an extremal Kähler metric in this class, for which the area of a projective line is 3.183933404 . . . times that of the exceptional divisor. This agrees with the figure obtained by more direct calculation; cf. [2, p.338].

Next we consider the 2-point blow-up $\mathbf{C P}_{2} \# 2 \overline{\mathbf{C P}}_{2}$ by instead setting $\alpha=0$ in our formula for $\left.\mathcal{A}\right|_{P}$. This gives us
$$\frac{1}{4 \pi^{2}} \int_{\mathbf{C P}_{2} \# 2 \overline{\mathbf{C P}}_{2}} \frac{s^{2}}{24} d \mu=\frac{32+176 y+318 y^{2}+280 y^{3}+132 y^{4}+32 y^{5}+3 y^{6}}{12+72 y+138 y^{2}+120 y^{3}+54 y^{4}+12 y^{5}+y^{6}}$$
where $y=\delta / \beta$. For $y>0$, this also has a unique critical point, an absolute minimum, at $y=0.9577128052 \ldots$ and for this critical Kähler class, the area of a projective line is 2.9577128052 . . . times that of either exceptional divisor. While it is unknown at present whether this Kähler class is represented by an extremal metric, the trace-free part of the Ricci tensor of such a metric would have to be rather small, since one would then have
$$\frac{1}{4 \pi^{2}} \int_{\mathbf{C P}_{2} \# \overline{\mathbf{C P}}_{2}}\left(2\left|W_{+}\right|^{2}+\frac{s^{2}}{24}\right) d \mu=\frac{3}{4 \pi^{2}} \int_{\mathbf{C P}_{2} \# \overline{\mathbf{C P}}_{2}} \frac{s^{2}}{24} d \mu=7.136474469 \ldots$$
and the metric would thus satisfy
$$\frac{1}{8 \pi^{2}} \int\left|\mathrm{r}_{0}\right|^{2} d \mu=0.136474469 \ldots$$
by the Gauss-Bonnet formula for $2 \chi+3 \tau=7$. It would thus seem that there is at least a chance that such a metric might in fact be conformal to Einstein.

Finally, we consider $\mathbf{C P}_{2} \# 3 \overline{\mathbf{C P}}_{2}$. In the region $\alpha, \beta>0, \delta \geq 0$, it appears that $\left.\mathcal{A}\right|_{P}$ has no critical points other than an absolute minimum at $\alpha=\beta$, $\delta=0$, which corresponds to multiples of the anti-canonical class. Thus, at least if the symmetry condition $\beta=\gamma$ is imposed, it seems that the only Einstein Hermitian metrics on $\mathbf{C P}_{2} \# 3 \overline{\mathbf{C P}}_{2}$ are the Kähler-Einstein metrics found by Siu [22]; cf. [23]. If this continues to hold even when $\beta \neq \gamma$, the uniqueness conjecture of §1 will have survived an important test.

\section*{References}
\begin{itemize}
\item[] [1] W. Barth, C. Peters, and A. Van de Ven, Compact Complex Surfaces, Springer-Verlag, 1984.
\item[] [2] A. Besse, Einstein Manifolds, Springer-Verlag, 1987.
\item[] [3] S. Bochner, Vector Fields and Ricci Curvature, Bull. Am. Math. Soc. 52 (1946) 776-797.
\item[] [4] C. Boyer, Conformal Duality and Compact Complex Surfaces, Math. Ann. 274 (1986) 517-526.
\item[] [5] C. Boyer, Self-Dual and Anti-Self-Dual Hermitian Einstein Metrics on Compact Complex Surfaces, Contemp. Math. 71 (1988) 105-114.
\item[] [6] E. Calabi, Extremal Kähler Metrics, in Seminar on Differential Geometry (ed. S.-T. Yau), Princeton, 1982.
\item[] [7] A. Derdzinski, Self-Dual Kähler Manifolds and Einstein Manifolds of Dimension Four, Comp. Math. 49 (1983) 405-433.
\item[] [8] A. Futaki and T. Mabuchi, Bilinear Forms and Extremal Kähler Vector Fields Associated with Kähler Classes, Math. Ann. 301 (1995) 199-210.
\item[] [9] P. Griffiths and J. Harris, Principles of Algebraic Geometry, Wiley-Interscience, 1978.
\item[] [10] J. Goldberg and R. Sachs, A Theorem on Petrov Types, Acta Phys. Pol. Suppl. 22 (1962) 13-23.
\item[] [11] N. Hitchin, On the Curvature of Rational Surfaces, Proc. Symposia Pure Math. 27, pp 65-80, 1975.
\item[] [12] N. Hitchin, On Compact Four-Dimensional Einstein Manifolds, J. Diff. Geom. 9 (1974) 435-442.
\item[] [13] P. Kronheimer, T. Mrowka, The Genus of Embedded Surfaces in the Complex Projective Plane, Math. Res. Letts. 1 (1994), 797-808.
\end{itemize}
\begin{itemize}
\item[] [14] Y. Matsushima, Sur la Structure du Groupe d'Homéomorphismes d'une Certaine Varieté Kählérienne, Nagoya Math. Journ. 11 (1957) 145-150.
\item[] [15] C. LeBrun, Einstein Metrics and Mostow Rigidity, Math. Res. Letts. 2 (1995), 1-8.
\item[] [16] C. LeBrun and S. Simanca, Extremal Kähler Metrics and Complex Deformation Theory, Geom. Func. Analysis 4(1994) 298-336.
\item[] [17] C. LeBrun and S. Simanca, On the Kähler Classes of Extremal Metrics, in Geometry and Global Analysis, Kotake, Nishikawa and Schoen, eds. pp. 255-271, Tohoku University, 1994.
\item[] [18] P. Nurrowski, Einstein Equations and Cauchy-Riemann Geometry, SISSA Ph.D. Thesis.
\item[] [19] D. Page, A Compact Rotating Gravitational Instanton, Phys. Lett. 79B (1979) 235-238.
\item[] [20] M. Przanowski and B. Broda, Locally Kähler Gravitational Instantons, Acta Phys. Pol. B 14 (1983) 637-661.
\item[] [21] R. Penrose and W. Rindler, Spinors and Space-Time, vol. 2, Cambridge University Press, 1986.
\item[] [22] Y.T. Siu, The Existence of Kähler-Einstein Metrics on Manifolds with Positive Anti-Canonical Line Bundle and Suitable Finite Symmetry Group, Ann. Math. 127 (1988) 585-627.
\item[] [23] G. Tian and S.T. Yau, Kähler-Einstein Metrics on Complex Surfaces with $\mathbf{c}_{1}>0$, Comm. Math. Phys. 112 (1987) 175-203.
\item[] [24] E. Witten, Monopoles and Four-Manifolds, Math. Res. Letts. 1 (1994), 769-796.
\end{itemize}