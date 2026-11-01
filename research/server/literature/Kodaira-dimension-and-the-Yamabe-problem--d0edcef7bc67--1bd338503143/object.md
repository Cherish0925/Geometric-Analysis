# Kodaira dimension and the Yamabe problem

- Category: papers
- Identity: doi:10.4310/cag.1999.v7.n1.a5
- Content status: fulltext_ok

---

---
source_file: Kodaira_dimension_and_the_Yamabe_problem_1d6002bc01be.pdf
converter: mathpix
format: mmd
---

\title{
Kodaira Dimension and the Yamabe Problem
}

\author{
Claude LeBrun ${ }^{1}$
}

\begin{abstract}
The Yamabe invariant $Y(M)$ of a smooth compact manifold is roughly the supremum of the scalar curvatures of unit-volume constant-scalar-curvature Riemannian metrics $g$ on $M$. (To be absolutely precise, one only considers constant-scalar-curvature metrics which are Yamabe minimizers, but this does not affect the sign of the answer.) If $M$ is the underlying smooth 4-manifold of a complex algebraic surface $(M, J)$, it is shown that the sign of $Y(M)$ is completely determined by the Kodaira dimension $\operatorname{Kod}(M, J)$. More precisely, $Y(M)<0$ iff $\operatorname{Kod}(M, J)=2 ; Y(M)=0$ iff $\operatorname{Kod}(M, J)=0$ or 1; and $Y(M)>0$ iff $\operatorname{Kod}(M, J)=-\infty$.
\end{abstract}

\section*{1. Introduction.}

One may define an interesting and natural diffeomorphism invariant of a compact smooth $n$-manifold $M$ as the supremum of the scalar curvatures of unit-volume constant-scalar-curvature metrics on $M$. A minor refinement [14, 23] of this definition, which does not change the sign of the invariant but guarantees that it is finite, restricts the class of allowed constant-scalar-curvature metrics to the so-called Yamabe minimizers. We will refer to the resulting invariant as the Yamabe invariant $Y(M)$ of our manifold. For a more precise definition, see §2 below.

For 2-manifolds, this invariant is easy to compute; the classical Gauss-Bonnet theorem tells us that the Yamabe invariant of a smooth compact surface is just $4 \pi \chi$, where $\chi$ is the Euler characteristic. Many important complex-analytic invariants of compact complex curves are thus determined by the Yamabe invariant of the underlying smooth 2-manifold.

One of the most important invariants of a compact complex manifold $(M, J)$ is its Kodaira dimension $\operatorname{Kod}(M)$. If $M$ has complex dimension $m$, recall that the canonical line bundle $K \rightarrow M$ is $K=\wedge^{m, 0}$, so that the

\footnotetext{
${ }^{1}$ Supported in part by NSF grant DMS-9505744.
}
holomorphic sections of $K$ are exactly the holomorphic $m$-forms on $(M, J)$. One now defines the Kodaira dimension as
$$\operatorname{Kod}(M)=\limsup _{\ell \rightarrow \infty} \frac{\log h^{0}\left(M, K^{\otimes \ell}\right)}{\log \ell} .$$
This can be shown to coincide with the maximal complex dimension of the image of $M$ under pluri-canonical maps to complex projective space, so that $\operatorname{Kod}(M) \in\{-\infty, 0,1, \ldots, m\}$. A compact complex $m$-manifold is said to be of general type if $\operatorname{Kod} M=m$.

For Riemann surfaces, the trichotomy $\operatorname{Kod}(M)=-\infty, 0,1$, exactly coincides with that given by $Y(M)>0,=0,<0$. The purpose of this paper is to show that much the same thing happens for compact complex surfaces $\left(M^{4}, J\right)$. Our main result is

Theorem A. Let $M$ be the underlying 4-manifold of a compact complex surface $\left(M^{4}, J\right)$ with $b_{1}(M)$ even. Then
$$Y(M)= \begin{cases}Y(M)>0 & \text { iff } \operatorname{Kod}(M, J)=-\infty \\ Y(M)=0 & \text { iff } \operatorname{Kod}(M, J)=0 \text { or } 1 \\ Y(M)<0 & \text { iff } \operatorname{Kod}(M, J)=2 .\end{cases}$$

The hypothesis that $b_{1}(M) \equiv 0 \bmod 2$ is equivalent [3] to requiring that $(M, J)$ admit a Kähler metric. It is also equivalent to requiring that $(M, J)$ be a deformation of a complex algebraic surface. Many of the results contained in this article will also apply in the non-Kähler case, but the overall picture remains considerably less clear when $b_{1}$ is odd.

One of the main tools in the proof of the above result is Seiberg-Witten theory. One of the most striking consequences of this theory is that any two diffeomorphic complex algebraic surfaces must have the same Kodaira dimension [11, 12]. Since the Yamabe invariant is obviously a diffeomorphism invariant, Theorem A casts this result in an interesting new light. On the other hand, the Yamabe invariant does not by itself distinguish Kodaira dimension 0 from Kodaira dimension 1. The distinction between these cases instead only emerges when one asks a finer question: when is the Yamabe invariant actually the scalar curvature of some unit-volume metric?

Finally, it should be emphasized that, despite the cited analogy between complex dimensions 1 and 2, the phenomenon explored here does not persist in higher dimensions. For example, consider a non-singular complex hypersurface of degree $m+3$ in $\mathbb{C P}_{m+1}$, where $m \geq 3$. This complex $m$-manifold has ample canonical bundle, so its Kodaira dimension is $m$. However, the
underlying smooth manifold is simply connected, non-spin, and has real dimension $>4$, so a surgical construction of Gromov and Lawson [13] shows that it admits metrics of positive scalar curvature, and thus has $Y>0$. Thus the Yamabe invariant and Kodaira dimension are correlated only in complex dimensions 1 and 2.

\section*{2. Yamabe Invariants.}

This section is expository in nature, and is intended as a convenient summary of the Yamabe folklore which will be needed in the rest of the paper.

Let $M$ be a smooth compact manifold. A conformal class on $M$ is by definition a collection of smooth Riemannian metrics on $M$ of the form
$$[g]=\left\{v g \mid v: M \rightarrow \mathbb{R}^{+}\right\},$$
where $g$ is some fixed Riemannain metric. To each such conformal class, one can associate a number $Y_{[g]}$, called the Yamabe constant of the class, by
$$Y_{[g]}=\inf _{\hat{g} \in[g]} \frac{\int_{M} s_{\hat{g}} d \mu_{\hat{g}}}{\left(\int_{M} d \mu_{\hat{g}}\right)^{\frac{n-2}{n}}},$$
where $s_{\hat{g}}$ and $d \mu_{\hat{g}}$ respectively denote the scalar curvature and volume measure of $\hat{g}$. If $g$ is a Riemannian metric for which the scalar curvature is everywhere positive, or everywhere zero, or everywhere negative, one can show that $Y_{[g]}$ is correspondingly positive, zero, or negative.

While $Y_{[g]}$ has been defined as an infimum, we could have instead defined it as a minimum, for a remarkable theorem [2, 20, 22] of Yamabe, Trudinger, Aubin, and Schoen asserts that any conformal class $[g]$ contains a metric which actually minimizes the relevant functional. Such a metric will be called a Yamabe minimizer. Any Yamabe minimizer has constant scalar curvature; conversely, a constant-scalar-curvature metric $g$ with $s_{g} \leq 0$ is automatically a Yamabe minimizer. Aubin's piece of the proof hinges on the observation that any conformal class on any $n$-manifold automatically satisfies
$$Y_{[g]} \leq n(n-1)\left(V_{n}\right)^{2 / n},$$
where $V_{n}$ is the volume of the unit $n$-sphere $S^{n} \subset \mathbb{R}^{n+1}$.

Given any smooth compact $n$-manifold, we can therefore [14, 23] define an associated real number by
$$Y(M)=\sup _{[g]} Y_{[g]}=\sup _{[g]} \inf _{\hat{g} \in[g]} \frac{\int_{M} s_{\hat{g}} d \mu_{\hat{g}}}{\left(\int_{M} d \mu_{\hat{g}}\right)^{\frac{n-2}{n}}} .$$
By construction, this is a diffeomorphism invariant of $M$, and it will be called the Yamabe invariant of $M$ in this paper. Notice that $Y(M)>0$ iff $M$ admits a metric of positive scalar curvature. If $Y(M) \leq 0$, the invariant is simply the supremum of the scalar curvatures of unit-volume constant-scalar-curvature metrics on $M$, since any constant-scalar-curvature metric of non-positive scalar curvature is automatically a Yamabe minimizer.

The minimax definition of $Y(M)$ is rather unwieldy for many purposes. Fortunately, it can often be calculated in a simpler manner.

Lemma 1. Let [g] be any conformal class on a smooth compact $n$-manifold $M$. Then
$$\inf _{\hat{g} \in[g]} \int_{M}\left|s_{\hat{g}}\right|^{n / 2} d \mu_{\hat{g}}=\left|Y_{[g]}\right|^{n / 2}$$
Proof. If $n=2$, the Gauss-Bonnet theorem tells us that
$$\int|s| d \mu \geq\left|\int s d \mu\right|=|4 \pi \chi(M)|=\left|Y_{[g]}\right|$$
with equality iff $s$ does not change sign. We may therefore assume henceforth that $n \geq 3$. We will break this into two cases, depending on the sign of $Y_{[g]}$.

First suppose that $Y_{[g]} \geq 0$ and $n \geq 3$. The Hölder inequality tells us that each metric $\hat{g}$ satisfies
$$\left(\int_{M}\left|s_{\hat{g}}\right|^{n / 2} d \mu_{\hat{g}}\right)^{2 / n} \geq \frac{\int_{M} s_{\hat{g}} d \mu_{\hat{g}}}{\left(\int_{M} d \mu_{\hat{g}}\right)^{1-\frac{2}{n}}},$$
with equality iff $s_{\hat{g}}$ is a non-negative constant. Since the infimum of the right-hand side over $\hat{g} \in[g]$ is $Y_{[g]}$ and is achieved by a metric of constant scalar curvature $s \geq 0$, the claim follows.

Finally, we come to the case in which $Y_{[g]}<0$ and $n \geq 3$. Let $g \in[g]$ be a metric of constant negative scalar curvature, and express any other metric in $[g]$ as $\hat{g}=u^{\ell} g$, where $\ell=4 /(n-2)$ and $u$ is some smooth positive function. The scalar curvatures $s=s_{g}$ and $\hat{s}=s_{\hat{g}}$ are related by
$$\hat{s} u^{\ell+1}=s u+(n-1) \ell \Delta u$$
where $\triangle=d^{*} d$ is the positive Laplacian of $g$. Thus
$$\begin{aligned}
\int_{M} \hat{s} u^{\ell} d \mu & =\int_{M}\left(s+(n-1) \ell \frac{1}{u} d^{*} d u\right) d \mu \\
& =\int_{M}\left(s-(n-1) \ell \frac{|d u|^{2}}{u^{2}}\right) d \mu \\
& \leq \int_{M} s d \mu
\end{aligned}$$
where $d \mu=d \mu_{g}$. The Hölder inequality therefore implies
$$\begin{aligned}
\left(\int_{M}\left|\hat{s} u^{\ell}\right|^{n / 2} d \mu\right)^{2 / n}\left(\int_{M} d \mu\right)^{\frac{n-2}{n}} & \geq \int\left(-\hat{s} u^{\ell}\right) d \mu \\
& \geq-\int s d \mu \\
& =\left|Y_{[g]}\right|\left(\int_{M} d \mu\right)^{(n-2) / n} .
\end{aligned}$$
Hence
$$\int_{M}\left|s_{\hat{g}}\right|^{n / 2} d \mu_{\hat{g}}=\int_{M}\left|\hat{s} u^{\ell}\right|^{n / 2} d \mu \geq\left|Y_{[g]}\right|^{n / 2}$$
with equality iff $u$ is constant. The result follows. \(\square\)

This leads to a very useful reinterpretation of $Y(M)$; cf. [1, 5, 14, 23].
Proposition 1. Let $M$ be a smooth compact $n$-manifold, $n \geq 3$. Then
$$\inf _{g} \int_{M}\left|s_{g}\right|^{n / 2} d \mu_{g}= \begin{cases}0 & \text { if } Y(M) \geq 0 \\ |Y(M)|^{n / 2} & \text { if } Y(M) \leq 0 .\end{cases}$$
Here the infimum on the left-hand side is taken over all smooth Riemannian metrics $g$ on $M$.

Proof. By Lemma 1,
$$\inf _{g} \int_{M}\left|s_{g}\right|^{n / 2} d \mu_{g}=\inf _{[g]}\left|Y_{[g]}\right|^{n / 2} .$$
If $Y(M) \leq 0$, we have $Y_{[g]} \leq 0$ for all $[g]$, so the right-hand-side may be rewritten as $\left(-\sup Y_{[g]}\right)^{n / 2}=|Y(M)|^{n / 2}$, and we are done. On the other hand, any smooth manifold of dimension $\geq 3$ admits metrics of negative scalar curvature [4], and $Y_{[g]}$ depends continuously on $[g]$. Since the space of metrics is connected, $Y(M)>0$ implies there is a conformal class $[g]$ on $M$ with $Y_{[g]}=0$, and the infimum therefore vanishes. \(\square\)

\section*{3. Results from Seiberg-Witten Theory.}

It is easy to see that some complex surfaces of Kähler type carry metrics with positive scalar curvature.

Proposition 2. Let $M$ be the underlying 4-manifold of a Kähler-type complex surface with Kodaira dimension $-\infty$. Then $Y(M)>0$.

Indeed, the Kodaira-Enriques classification [3] tells us that any such complex surface is either $\mathbb{C P}_{2}$ or else is obtained from a $\mathbb{C P}_{1}$-bundle over a complex curve by blowing up points. Now $\mathbb{C P}_{2}$ carries the Fubini-Study metric, which has positive scalar curvature. Any $S^{2}$-bundle over another manifold also carries metrics of positive scalar curvature; namely, consider any Riemannian submersion metric with round, totally geodesic fibers, and then rescale the fibers to have very small diameter while keeping the metric on the base fixed. Finally, the blowing-up operation amounts differentiably to taking connect sums with copies of $\overline{\mathbb{C P}}_{2}$; all blow-ups of surfaces with positive-scalar-curvature metrics therefore themselves admit positive-scalar-curvature metrics because a result of Gromov and Lawson [13] tells us that the class of manifolds with positive-scalar-curvature metrics is closed under surgeries in codimension $\geq 3$.

On the other hand, it is a truly remarkable consequence of Seiberg-Witten theory that the converse of the above statement is also true:

Theorem 1. Let $M$ be the underlying 4-manifold of a complex surface of Kähler type with Kodaira dimension $\geq 0$. Then $Y(M) \leq 0$.

Remember, this is just a fancy way of saying that $M$ does not admit metrics of positive scalar curvature. When $b^{+}(M)>1$, this was first proved
by Witten [26]. In the $b^{+}=1$ case, this was proved for minimal surfaces in [16], and then in the non-minimal case by Friedman and Morgan [11].

The proof proceeds by first showing that for every metric $g$ on $M$, there must be a solution of the Seiberg-Witten equations
$$\begin{aligned}
D^{\theta} \Phi & =0 \\
F_{\theta}^{+} & =i \sigma(\Phi)
\end{aligned}$$
and an unknown unitary connection $\theta$ on some line bundle $L \rightarrow M$ and an unknown twisted spinor $\Phi \in \Gamma\left(S_{+} \otimes L^{1 / 2}\right)$. Here $D^{\theta}$ is the Dirac operator coupled to $\theta, F_{\theta}^{+}$is the projection of the curvature of $\theta$ to the bundle $\Lambda^{+}$ of $g$-self-dual 2-forms, and $\sigma: S_{+} \otimes L^{1 / 2} \rightarrow \Lambda^{+}$is the real-quadratic map induced by the natural isomorphism $\odot^{2} \mathbb{S}_{+}=\Lambda^{+} \otimes \mathbb{C}$. Moreover, $L$ can either be taken to be the anti-canonical line bundle of $(M, J)$ or its pull-back via some diffeomorphism $M \rightarrow M$. However, these equations imply the Weitzenböck formula
$$0=4 \nabla^{\theta *} \nabla^{\theta}+s \Phi+|\Phi|^{2} \Phi,$$
where $s$ is the scalar curvature of $g$. Taking the inner product with $\Phi$ and integrating, this tells us that
$$0=\int_{M}\left[\left|2 \nabla^{\theta} \Phi\right|^{2}+s|\Phi|^{2}+|\Phi|^{4}\right] d \mu$$
which is a contradiction if $s>0$.
Pushing this argument further yields a stronger result [18] for surfaces of general type:

Theorem 2. Let $M$ be the underlying 4-manifold of a complex surface with Kodaira dimension 2. Then $Y(M)<0$. Moreover, if $X$ is the minimal model of $M$, then $Y(M)=Y(X)=-4 \pi \sqrt{2 c_{1}^{2}(X)}$.
(Recall [3] that the minimal model $X$ is characterized by the fact that $M$ can be blown down to $X$, but that $X$ cannot be blown down any further. The minimal model $X$ of a surface $M$ of general type is unique, and $c_{1}^{2}(X)>0$.)

Indeed, applying the Schwarz inequality to the integrated Weitzenböck formula tells us that
$$\left(\int_{M} s^{2} d \mu\right)^{1 / 2}\left(\int_{M}|\Phi|^{4} d \mu\right)^{1 / 2} \geq \int_{M}(-s)|\Phi|^{2} d \mu \geq \int_{M}|\Phi|^{4} d \mu$$

We must therefore have
$$\int_{M} s^{2} d \mu \geq \int_{M}|\Phi|^{4} d \mu=8 \int_{M}\left|F_{\theta}^{+}\right|^{2} d \mu$$
for any metric. However [17],
$$\int_{M}\left|F_{\theta}^{+}\right|^{2} d \mu \geq 4 \pi^{2}\left(\left[c_{1}(L)\right]^{+}\right)^{2}$$
where $\left[c_{1}(L)\right]^{+}$is self-dual part of the $g$-harmonic deRham representative of $c_{1}(L)$. Moreover, for each $g$ one can show [18] that $L$ can be chosen so that $\left(\left[c_{1}(L)\right]^{+}\right)^{2} \geq c_{1}^{2}(X)$. This shows that
$$\int_{M} s^{2} d \mu \geq 32 \pi^{2} c_{1}^{2}(X)$$
for all metrics on $M$. But by gluing together Kähler-Einstein orbifolds, gravitional instantons, and standard metrics on the blow-up of $\mathbb{C}^{2}$ at the origin, one can also construct [18] sequences of metrics which show that this bound is actually sharp:
$$\inf _{g} \int_{M} s^{2} d \mu=32 \pi^{2} c_{1}^{2}(X)>0$$
Thus $Y(M)=-4 \pi \sqrt{2 c_{1}^{2}(X)}<0$ by Proposition 1.

\section*{4. Rational Elliptic Surfaces Revisited.}

A complex surface $\left(M^{4}, J\right)$ is said to be elliptic if it admits a holomorphic map $M \rightarrow \Sigma$ to a complex curve such that the regular fibers are elliptic curves $T^{2}$. While this notion is of greatest importance in the study of surfaces of Kodaira dimension 0 and 1, there are also elliptic surfaces of Kodaira dimension $-\infty$. One family of examples of the latter type are the rational elliptic surfaces treated this section.

The smooth oriented 4-manifold $\mathbb{C P}_{2} \# 9 \overline{\mathbb{C P}}_{2}$ may be concretely realized as the blow-up of $\mathbb{C P}_{2}$ at 9 points. One choice of these 9 points is to take them to be the points of intersection of a generic pair of elliptic (i.e. cubic) curves in the projective plane. There is then exactly a $\mathbb{C P}_{1}$ 's worth of cubics passing through the 9 points, corresponding to linear combinations of the defining equations of the original pair of curves. When $\mathbb{C P}_{2}$ is blown up at these 9 points, this pencil of cubics gives rise to a holomorphic projection $\mathbb{C P}_{2} \# 9 \overline{\mathbb{C P}}_{2} \rightarrow \mathbb{C P}_{1}$, the generic fiber of which is a smooth elliptic curve $E \approx$
$T^{2}$. The term rational elliptic surface is thus used to describe $\mathbb{C P}_{2} \# 9 \overline{\mathbb{C P}}_{2}$ equipped with the deformation class of this projection to $\mathbb{C P}_{1}$.

There is a useful way of constructing special rational elliptic surfaces by analogy to the Kummer construction of K3's. Let $\Lambda \cong \mathbb{Z} \oplus \mathbb{Z}$ be any lattice in $\mathbb{C}$, and let $E=\mathbb{C} / \Lambda$ be the corresponding elliptic curve. Recall that each such curve can be realized as a branched cover over $\mathbb{C P}_{1}$ because reflection $z \mapsto-z$ through the origin in $\mathbb{C}$ induces in an involution of $E$ with 4 fixedpoints ${ }^{2}$; the orbifold quotient $E / \mathbb{Z}_{2}$ can then be identified with a Riemann surface of genus 0, and this realizes $E$ as a branched cover $\wp: E \rightarrow \mathbb{C P}_{1}$. The involution of $E$ that occurs in this argument is called the Weierstrass involution of $E$, and will be denoted here by $\Phi: E \rightarrow E$. Notice that $\Phi$ is an isometry of the obvious flat metric on $E$.

Now let $\Psi: \mathbb{C P}_{1} \rightarrow \mathbb{C P}_{1}$ be the involution $\left[z_{0}: z_{1}\right] \mapsto\left[-z_{0}: z_{1}\right]$, which has two fixed points and amounts to a 180° rotation of $S^{2}$ around an axis. The product involution
$$\Phi \times \Psi: E \times \mathbb{C P}_{1} \rightarrow E \times \mathbb{C P}_{1}$$
then has 8 fixed points, and the quotient $E \times \mathbb{C P}_{1} / \mathbb{Z}_{2}$ is a complex orbifold with 8 singularities modeled on $\mathbb{C}^{2} / \pm 1$. Let $\tilde{M}$ be the blow-up of $E \times \mathbb{C P}_{1}$ at the 8 fixed points of $\Phi \times \Psi$, and let $M=\tilde{M} / \mathbb{Z}_{2}$. The non-singular complex surface $M$ is thus obtained from $E \times \mathbb{C P}_{1} / \mathbb{Z}_{2}$ by replacing each of the 8 singular points with a (-2)-curve.

Now consider the holomorphic map $\varpi: M \rightarrow \mathbb{C P}_{1}$ induced by following the second-factor projection $E \times \mathbb{C P}_{1} \rightarrow \mathbb{C P}_{1}$ with $\left[z_{0}: z_{1}\right] \mapsto\left[z_{0}^{2}: z_{1}^{2}\right]$. All but two fibers of $\varpi$ are copies of $E$; the only two exceptions are the fibers over the north and south poles [0 : 1] and [1 : 0]. Each of these two exceptional fibers consists of five (-2)-curves, linked together according to the Dynkin diagram $\tilde{D}_{4}$ :
![](https://cdn.mathpix.com/cropped/1ef4a67b-68c6-47a1-b726-7a1ec3c6a45f-09.jpg?height=160&width=159&top_left_y=1789&top_left_x=722)
These two exceptional fibers are of thus of Kodaira type $I_{0}^{*}\left(\tilde{D}_{4}\right)$.
Now $\varpi: M \rightarrow \mathbb{C P}_{1}$ is deformation equivalent to the above-described standard model of the rational elliptic surface. In fact, $M$ can be blown

\footnotetext{
${ }^{2}$ corresponding the half-lattice $\frac{1}{2} \Lambda$
}
down to $\mathbb{C P}_{1} \times \mathbb{C P}_{1}$ in such a way that the fibers of $\varpi$ are sent to the elliptic curves of the pencil
$$t_{0} x_{0}\left(x_{0}-x_{1}\right) y_{0}^{2}+t_{1} x_{1}\left(x_{0}-a x_{1}\right) y_{1}^{2}=0,$$
where the number $a$ is given in terms of the lattice $\Lambda$ by the Weierstrass $\partial$-function. Notice that for each $[t] \in \mathbb{C P}_{1}$ this locus is an element of the anti-canonical linear system $|\mathcal{O}(2,2)|$ on $\mathbb{C P}_{1} \times \mathbb{C P}_{1}$, and that each elliptic curve of the pencil passes through the points ([0 : 1], [0 : 1], ), ([1 : 1], [0 : 1]), ([a : 1], [1 : 0]), and ([1 : 0], [1 : 0]), and all are tangent to the second-factor $\mathbb{C P}_{1}$ at these points.

To see this explicitly, let us first consider $E \times \mathbb{C P}_{1}$ as a ruled surface over $E$, and blow it up at the 8 relevant points to obtain $\tilde{M}$ :
![](https://cdn.mathpix.com/cropped/1ef4a67b-68c6-47a1-b726-7a1ec3c6a45f-10.jpg?height=393&width=846&top_left_y=1035&top_left_x=437)
Dividing by $\Phi \times \Psi$ then gives us a non-minimal rational ruled surface:
![](https://cdn.mathpix.com/cropped/1ef4a67b-68c6-47a1-b726-7a1ec3c6a45f-10.jpg?height=396&width=854&top_left_y=1609&top_left_x=436)
(Note that $\varpi$, which is depicted horizontally in the above picture, is not the ruled-surface projection, which is here depicted vertically.) Contracting 8 exceptional curves in a judicious order,
![](https://cdn.mathpix.com/cropped/1ef4a67b-68c6-47a1-b726-7a1ec3c6a45f-11.jpg?height=396&width=756&top_left_y=316&top_left_x=626)
we get a rational ruled surface which can be recognized as $\mathbb{C P}_{1} \times \mathbb{C P}_{1}$ by inspecting self-intersections of holomorphic curves. Our pencil now becomes the sub-family of the linear system $|\mathcal{O}(2,2)|$ consisting of curves which are tangent to the second factor at 4 points in the claimed special position. It follows that $\varpi: M \rightarrow \mathbb{C P}_{1}$ is deformation equivalent to the standard model of the rational elliptic surface, since we may first deform our pencil into a generic sub-pencil of $|\mathcal{O}(2,2)|$, and then map $\mathbb{C P}_{1} \times \mathbb{C P}_{1}$ birationally to $\mathbb{C P}_{2}$ in the usual way, using one of the base points of the pencil as our center.

This leads to the following:

Proposition 3. Let $V$ be the (flat) 4-orbifold obtained from $\mathbb{R} \times T^{3}$ by dividing by the involution induced by $-1: \mathbb{R}^{4} \rightarrow \mathbb{R}^{4}$, let $B=\left(\mathbb{R} \times S^{1}\right) / \mathbb{Z}_{2}$ denote the analogous 2 -orbifold, and let $\pi: V \rightarrow B$ be the map induced by projection $\mathbb{R} \times T^{3} \rightarrow \mathbb{R} \times S^{1}$ to the first two coordinates. Then a smooth model of the rational elliptic surface $\mathbb{C P}_{2} \# 9 \overline{\mathbb{C P}}_{2} \rightarrow \mathbb{C P}_{1}$ may be obtained from $\pi: V \rightarrow B$ by replacing each of the 8 singular point of $V$ with a 2-sphere of self-intersection -2, forgetting the orbifold structure on $B$, and adding a smooth fiber at infinity in the obvious manner.

Proof. We have already seen that the rational elliptic surface can be viewed as a desingularization of $\left(S^{2} \times T^{2}\right) / \mathbb{Z}_{2}$. Now let $x \in S^{2}$ be some point which is not fixed by the involution, and let $x^{\prime} \neq x$ be its image under the involution. Identify $S^{2}-\left\{x, x^{\prime}\right\}$ with the cylinder $\mathbb{R} \times S^{1}$ in such a manner that the involution becomes simultaneous reflection in both factors. The result follows. \(\square\)

The orbifold $V$ comes equipped with a family of flat orbifold metrics. Replacing the singularities with gravitational instantons yields the main result of this section:

Proposition 4. Let $\tilde{V}$ denote the complement of a generic fiber in the rational elliptic surface $\mathbb{C P}_{2} \# 9 \overline{\mathbb{C P}}_{2} \rightarrow \mathbb{C P}_{1}$, let $\pi: \tilde{V} \rightarrow \mathbb{C}$ be the induced elliptic fibration, normalized so that all critical values are contained in the open unit disk $\Delta \subset \mathbb{C}$. Let $f$ be any given flat metric on the 2-torus $T^{2}$. Then there is a family $g_{t}, t \in[1, \infty)$ of Riemannian metrics on $\tilde{V}$ such that
\begin{itemize}
\item[-] the Ricci curvature of $g_{t}$ converges uniformly to 0 as $t \rightarrow \infty$;
\item[-] $\left(\pi^{-1}(\mathbb{C}-\Delta), g_{t}\right)$ is isometric to $\left([0, \infty) \times S^{1}, d x^{2}+d \theta^{2}\right) \times\left(T^{2}, f / t\right)$; and
\item[-] $\lim _{t \rightarrow \infty} \operatorname{Vol}\left(\pi^{-1}(\Delta), g_{t}\right)=0$.
\end{itemize}

Proof. The basic idea is to replace the singularities of of $V$ with Eguchi-Hanson metrics. The Eguchi-Hanson metric [9, 15] is a complete Ricci-flat metric on the $\mathcal{O}(-2)$ line bundle over $\mathbb{C P}_{1}$, or in other words on the blow-up of $\mathbb{C}^{2} /( \pm 1)$ at the origin. Essentially by introducing polar coordinates on $\left(\mathbb{R}^{4}-0\right) /( \pm 1)$, we may think of this as the completion of the metric on $(1, \infty) \times S O(3)$ given by
$$g_{E H}=\frac{d r^{2}}{1-\frac{1}{r^{4}}}+r^{2}\left(\sigma_{1}^{2}+\sigma_{2}^{2}+\left(1-\frac{1}{r^{4}}\right) \sigma_{3}^{2}\right)$$
where the left-invariant co-frame $\left\{\sigma_{j}\right\}$ is orthonormal for the curvature +1 bi-invariant metric. By rescaling and homothety, we can turn this into a 1 -parameter family
$$\frac{d r^{2}}{1-\frac{A}{r^{4}}}+r^{2}\left(\sigma_{1}^{2}+\sigma_{2}^{2}+\left(1-\frac{A}{r^{4}}\right) \sigma_{3}^{2}\right), \quad r>\sqrt[4]{A}$$
of Ricci-flat metrics which bubble off to the flat orbifold metric on $\mathbb{R}^{4} /( \pm 1)$ as $A \rightarrow 0$.

Let us now modify the Eguchi-Hanson metric. Let $\phi(t)$ be a smooth monotonely non-increasing function which is identically 1 on [0, 1] and identically 0 on $[2, \infty]$. For small values of the parameter $A$, the modified metric
$$\frac{d r^{2}}{1-\phi(r) \frac{A}{r^{4}}}+r^{2}\left(\sigma_{1}^{2}+\sigma_{2}^{2}+\left(1-\phi(r) \frac{A}{r^{4}}\right) \sigma_{3}^{2}\right), \quad r>\sqrt[4]{A}$$
then agrees with the Euclidean metric for $r>2$, is Ricci-flat when $r<1$, and has Ricci curvature $<C A$ for some constant $C$ independent of the small
parameter $A$. Making another homothety and rescaling, the metric
$$\frac{d r^{2}}{1-\phi(r / \varepsilon) \frac{A \varepsilon^{4}}{r^{4}}}+r^{2}\left(\sigma_{1}^{2}+\sigma_{2}^{2}+\left(1-\phi(r / \varepsilon) \frac{A \varepsilon^{4}}{r^{4}}\right) \sigma_{3}^{2}\right), \quad r>\varepsilon \sqrt[4]{A}$$
is Euclidean for $r>2 \varepsilon$, Ricci-flat for $r<\varepsilon$, and has Ricci curvature $<$ $C A / \varepsilon^{2}$. Thus the metrics
$$g_{\varepsilon}=\frac{d r^{2}}{1-\phi(r / \varepsilon) \frac{\varepsilon^{8}}{r^{4}}}+r^{2}\left(\sigma_{1}^{2}+\sigma_{2}^{2}+\left(1-\phi(r / \varepsilon) \frac{\varepsilon^{8}}{r^{4}}\right) \sigma_{3}^{2}\right), \quad r>\varepsilon^{2}$$
have Ricci curvature uniformly $O\left(\varepsilon^{2}\right)$ as $\varepsilon \searrow 0$. Notice that the volume form of $g_{\varepsilon}$ coincides with the Euclidean volume form $r^{3} d r \wedge \sigma_{1} \wedge \sigma_{2} \wedge \sigma_{3}$, but that the appropriate domain of integration is the $r>\varepsilon^{2}$ rather than $r>0$. Thus, smoothing a flat orbifold singularity modeled on $\mathbb{R}^{4} /( \pm 1)$ by gluing in the modified Eguchi-Hanson metric $g_{\varepsilon}$ reduces the total volume, namely by $\pi^{2} \varepsilon^{8} / 2$.

Now let $f$ be any fixed flat metric on the 2-torus, and let $\imath$ denote the injectivity radius of $\left(T^{2}, f\right)$, and set $\hat{\imath}=\min (\imath, \pi)$. Endow $\mathbb{R} \times T^{3}$ with the sequence of flat metrics $\hat{g_{t}}=d x^{2}+d \theta^{2}+f / t$, and push these down as flat orbifold metrics on $V=\left(\mathbb{R} \times T^{3}\right) / \mathbb{Z}_{2}$. For each $t$, let $\varepsilon_{t}=\hat{\imath} / 4 \sqrt{t}$, so that the balls of radius $2 \varepsilon_{t}$ centered at the orbifold singularities of $V$ are pairwise disjoint. On the blow-up $\tilde{V}$ of $V$, we can then define a metric $g_{t}$ as the $\hat{g}_{t}$ on the complement of these balls, and the modified Eguchi-Hanson metrics $g_{\varepsilon_{t}}$ on the blown-up interior of these balls . Since $\varepsilon_{t} \rightarrow 0$, the Ricci curvature of $g_{t}$ tends uniformly to zero. Moreover, the volume of the region $|x| \leq a$ in $\left(X, g_{t}\right)$ is less than $2 \pi a \alpha / t \rightarrow 0$, where $\alpha$ is the area of $\left(T^{2}, f\right)$, so the volume of the pre-image of any compact set in $\mathbb{C}$ tends to 0 as $t \rightarrow \infty$. □

\section*{5. Collapsing Elliptic Surfaces.}

Definition 1. Let $M$ be a smooth manifold. We will say that $M$ collapses with bounded scalar curvature if there is a sequence $g_{j}$ of smooth metrics on $M$ for which the absolute value of the scalar curvatures is uniformly bounded, but with total volume tending to zero:
$$\left|s_{g_{j}}\right|<\mathcal{B}, \quad \lim _{j \rightarrow \infty} \operatorname{Vol}\left(M, g_{j}\right)=0 .$$
Similarly, we say that $M$ collapses with bounded Ricci (respectively, sectional) curvature if there is a sequence $g_{j}$ of smooth metrics on $M$ with
uniformly bounded Ricci (respectively, sectional) curvature and total volume tending to zero.

This collection of definitions is loosely inspired by the work of Cheeger and Gromov [7], who studied sequences of metrics $g_{j}$ with bounded sectional curvature and injectivity radius tending to zero at all points. A standard comparison argument for the volume of small balls shows that a sequence of metrics with sectional curvature bounded above can have volume tending with to zero only if the point-wise injectivity radii uniformly tend to zero, too. Note, however, that a sequence of metrics $g_{j}$ with bounded sectional curvature and injectivity radius tending to zero may have volume bounded away from zero - as even happens for flat metrics on the 2-torus. Nonetheless, a remarkable result of Cheeger and Gromov [8] shows that if a compact manifold admits a sequence of metrics $g_{j}$ with bounded sectional curvature and injectivity radius uniformly tending to zero, there is typically another sequence $\tilde{g}_{j}$ with bounded sectional curvature for which the volume tends to zero as well. Thus the present definition of collapse with bounded sectional curvature is in rough accord with the definitions used by others.

Collapse with bounded scalar curvature is directly relevant to the computation of Yamabe invariants by virtue of the following result:

Proposition 5. Let $M$ be a smooth compact $n$-manifold, $n \geq 3$. Then the following are equivalent:
\begin{itemize}
\item[(i)] $M$ collapses with bounded scalar curvature;
\item[(ii)] $\inf _{g} \int_{M}\left|s_{g}\right|^{n / 2} d \mu_{g}=0$;
\item[(iii)] $Y(M) \geq 0$.
\end{itemize}

Proof. The implication (i) ⇒ (ii) is trivial, since $\int_{M}\left|s_{g_{j}}\right|^{n / 2} d \mu_{g_{j}} \rightarrow 0$ for any sequence of metrics with bounded scalar curvature and volume tending to zero. The implication (ii) ⇒ (iii) follows from Proposition 1. Finally, the implication (iii) ⇒ (i) follows from the fact [2] that any $n$-manifold, $n \geq 3$, admits of metrics of constant negative scalar curvature; if $Y(M) \geq 0$, there is a thus a sequence of unit-volume metrics with constant negative scalar curvature tending to 0 from below, and rescaling these metrics so they have $s \equiv-1$ then makes the volumes of the rescaled metrics tend to zero. \(\square\)

If $M$ is the underlying 4-manifold of a complex elliptic surface, these various notions of collapse can be completely understood.

Theorem 3. Let $M$ be the underlying 4-manifold of a complex elliptic surface. Then $M$ collapses with bounded scalar curvature.

Theorem 4. Let $M$ be the underlying 4-manifold of a complex elliptic surface. Then $M$ collapses with bounded Ricci curvature $\Leftrightarrow M$ is relatively minimal.

Theorem 5. Let $M$ be the underlying 4-manifold of a complex elliptic surface. Then $M$ collapses with bounded sectional curvature $\Leftrightarrow \chi(M)=0$.

In order to prove these results, we will need special diffeomorphic models [10, 21] of elliptic surfaces. These are built up in stages, starting with surfaces we shall call twisted products. Let $E$ be an elliptic curve, equipped with a compatible flat metric, let $o \in E$ be a chosen base-point, and let $G$ be the finite group of orientation-preserving isometries $E \rightarrow E$ which fix $o$. (Thus $G$ is a cyclic group of order 2, 4, or 6.) A twisted product surface is simply the total space $B$ of a fiber-bundle $B \rightarrow \Sigma$ over a compact complex curve, with fiber $E$ and structure group $G$.

Now let $B \rightarrow \Sigma$ be such a twisted product, and let a finite collection of points $x_{j} \in \Sigma$ be specified, and assign each of these points some integer multiplicity $m_{j}>1$. Give $\Sigma$ an obifold structure by introducinging orbifold local coordinates of the form $\hat{z}=z^{1 / m_{j}}$ near $x_{j}$, where $z$ is a local complex coordinate on $\Sigma$ with $z\left(x_{j}\right)=0$. A process called the logarithmic transform now allows us to delete the fiber $E_{j} \cong E$ over each $x_{j}$, and replace it with $E_{j} / \mathbb{Z}_{m_{j}}$, where the $\mathbb{Z}_{m_{j}}$-action is generated by any specified translation $\tau_{j}: E_{j} \rightarrow E_{j}$ of order $m_{j}$. Namely, let $\tau_{j}(t)$ be a 1-complex-parameter group of translations of $E_{x_{j}}$ with $\tau_{j}(1)=\tau_{j}$, let $\Delta \subset \mathbb{C}$ be a disk centered at 0 and contained in the range of the orbifold coordinate $\hat{z}$, and glue $\left(E_{j} \times \Delta\right) /\left\langle\left(\tau_{j}, e^{2 \pi i / m_{j}}\right)\right\rangle$ to $B-E_{x_{j}}$ by $[(y, \tilde{z})] \leftrightarrow\left(\tau_{j}\left(-m_{j} \log (\hat{z}) / 2 \pi i\right)(y), z:=\hat{z}^{m_{j}}\right)$.

With these constructions in mind, we can now prove

Lemma 2. Let $M$ be the underlying 4-manifold of any complex elliptic surface with Euler characteristic 0. Then there is a compact 2-orbifold $\Sigma$ and a smooth submersive map $\pi: M \rightarrow \Sigma$, such that for every orbifold metric $h$ on $\Sigma$ there is a Riemannian metric $g$ on $M$ for which $\pi$ becomes a Riemannian submersion with flat, totally geodesic fibers. Moreover, $\pi$ can be chosen so that its fibers over some open disk in $\Sigma$ are also regular fibers of the original elliptic fibration of $M$.

Proof. Any complex elliptic surface with Euler characteristic zero is $C^{\infty}$-deformation equivalent to some logarithmic transform of a twisted-product surface [10, Proposition 7.2]. But this model is an orbi-bundle over the 2 -orbifold $\Sigma$ with structure group equal to the isometry group of a flat 2-torus $E$. Starting from any orbifold metric $h$ on $\Sigma$, now construct a metric $g$ on $M$ by gluing together local product metrics with a partition of unity subordinate to a trivializing cover of $\Sigma$. Each fiber of $\pi: M \rightarrow \Sigma$ is then a flat quotient of $E$, and each fiber has vanishing second fundamental form because the orthogonal space of the fibers is the horizontal subspace of a connection with structure group equal to the isometry group of the fiber. \(\square\)

The ideas of Cheeger and Gromov [7] now immediately lead to a
Proof of Theorem 5. Consider the metrics
$$g_{t}=\frac{1}{t} g+\left(1-\frac{1}{t}\right) \pi^{*} h$$
on $M$ as $t \rightarrow \infty$. We have
$$\operatorname{Vol}\left(M, g_{t}\right)=\frac{1}{t} \operatorname{Vol}(M, g) \rightarrow 0$$
so it suffices to show that the components of the curvature tensor remain bounded in an orthonormal frame as $t \rightarrow \infty$. But this follows from O'Neill's Riemannian submersion formulas [4]. Indeed, the vertical sectional curvature is 0 for all $t$, and the horizontal sectional curvature is given by
$$K(H)=K(\Sigma)-\frac{3}{4} g_{t}(v, v) \rightarrow K(\Sigma),$$
while the sectional curvature of the 2-plane $P$ spanned by a vertical vector and a horizontal vector is
$$K(P)=\frac{1}{4} g_{t}\left(v^{\|}, v^{\|}\right) \rightarrow 0 .$$
Here $K(\Sigma)$ is the Gauss curvature of $(\Sigma, h)$, and $v$ is the ( $t$-independent) vertical component of $\left[w_{1}, w_{2}\right]$, where $w_{1}$ and $w_{2}$ are horizontal vectors which project to an oriented orthonormal frame on $\Sigma$, whereas $v^{\|}$is the orthogonal projection of $v$ into $P$. This shows that the point-wise norm of the curvature tensor, and hence all sectional curvatures, remain uniformly bounded as
$t \rightarrow \infty$. Any elliptic surface $M$ with $\chi(M)=0$ therefore collapses with bounded sectional curvature.

Conversely, if $M$ collapses with bounded sectional curvature, the Gauss-Bonnet formula tells one that $\chi(M)=0$. \(\square\)

The next operation we will need in order to create smooth models of elliptic surfaces is the fiber sum. The fiber sum of two elliptic surfaces is the smooth manifold obtained by removing a tubular neighborhood of a regular fiber in each and then then identifying the boundaries in a manner compatible with the orientations and given local trivializations. Any minimal complex elliptic surface $M$ is diffeomorphic [10, Corollary 2.17] to a fiber sum of an elliptic surface $\check{M}$ with Euler characteristic 0 and copies of the rational elliptic surface.

Proof of Theorem 4. Let us thus begin with some elliptic surface $\check{M}$ with $\chi(\check{M})=0$, and let $\pi: \check{M} \rightarrow \Sigma$ be a smooth submersion of the type used in the previous proof. Let $x_{1}, \ldots, x_{k} \in \Sigma$ be the points we will use as the centers of the fiber sum construction. Let $U_{1}, \ldots, U_{k}$ be disjoint disks around these points, chosen so that $M \rightarrow \Sigma$ may be trivialized over their closures, and identify each with the disk of radius 2 about $0 \in \mathbb{C}$. Choose $h$ so that its restriction to the annulus $|z| \in[1,2]$ is isometric to the cylinder $S^{1} \times[1,2]$, and now construct the family of metrics $g_{t}$ used above, with the stipulation $g$ is actually taken to be a product metric on $\pi^{-1}\left(U_{1}\right), \ldots, \pi^{-1}\left(U_{k}\right)$. Letting $\tilde{U}_{1} \subset U_{1}, \ldots, \tilde{U}_{k} \subset U_{k}$ each correspond to the unit sub-disk $|z|<1$, the Riemannian manifold-with-boundary $\left(M-\cup \pi^{-1}\left(\tilde{U}_{j}\right), g_{t}\right)$ has ends isometric to $\left([0,1] \times S^{1}, d t^{2}+d \theta^{2}\right) \times(E, f / t)$, where $f$ is a fixed flat metric on an elliptic curve $E$.

However, these cylindrical ends precisely match those of the metrics on $\tilde{V}$ constructed in Proposition 3, and we can therefore glue these objects together to obtain metrics with bounded Ricci curvature and volume tending to zero on the fiber sum $M$ of $\check{M}$ and $k$ rational elliptic surfaces. Since a diffeomorphic model of any minimal elliptic surface can be constructed in this way, it follows that any minimal elliptic surface collapses with bounded Ricci curvature, as claimed.

Conversely, suppose an oriented 4-manifold $M$ admits a sequence of metrics $g_{j}$ with bounded Ricci curvature $r$ and volume tending to zero. We then
have
$$\lim _{j \rightarrow \infty} \int_{M}\left[\frac{s_{g_{j}}^{2}}{24}-\frac{|\stackrel{\circ}{r}|_{g_{j}}^{2}}{2}\right] d \mu_{g_{j}}=0$$
where $\stackrel{\circ}{r}$ denotes the trace-free part of the Ricci curvature. But
$$\begin{aligned}
(2 \chi+3 \tau)(M) & =\frac{1}{4 \pi^{2}} \int_{M}\left[\left|W_{+}\right|_{g}^{2}+\frac{s_{g}^{2}}{24}-\frac{|\stackrel{\circ}{r}|_{g}^{2}}{2}\right] d \mu_{g} \\
& \geq \frac{1}{4 \pi^{2}} \int_{M}\left[\frac{s_{g}^{2}}{24}-\frac{|\stackrel{\circ}{r}|_{g}^{2}}{2}\right] d \mu_{g}
\end{aligned}$$
for any metric on $M$. It therefore follows that $(2 \chi+3 \tau)(M) \geq 0$. On the other hand, $2 \chi+3 \tau=c_{1}^{2} \leq 0$ if $M$ is an elliptic surface, and equality occurs if $M$ is relatively minimal [3]. Hence an elliptic surface $M$ must be minimal if it collapses with bounded Ricci curvature. \(\square\)

Finally, any elliptic surface is obtained from a minimal elliptic surface by blowing up an appropriate number of times. Recall that the blow-up of $\mathbb{C}^{2}$ at the origin is by definition the line bundle $\mathcal{O}(-1)$ over $\mathbb{C P}_{1}$. A point in an arbitrary complex surface can similarly be obtained by replacing a small ball with a tubular neighborhood of the zero section in this bundle. This procedure is then iterated as needed to produce the desired surface.

Proof of Theorem 3. The idea is to graft Burns metrics onto the previous examples. The Burns metric [15] is a scalar-flat Kähler metric on the blowup of $\mathbb{C}^{2}$ at the origin. By introducing polar coordinates, this can be viewed as the completion of the metric on $(1, \infty) \times S^{3}$ given by
$$g_{\mathrm{Burns}}=\frac{d r^{2}}{1-\frac{1}{r^{2}}}+r^{2}\left(\sigma_{1}^{2}+\sigma_{2}^{2}+\left(1-\frac{1}{r^{2}}\right) \sigma_{3}^{2}\right),$$
where $\left\{\sigma_{j}\right\}$ is an $S U(2)$-invariant orthonormal frame on $S^{3}$. By repeating the sequence of homotheties, rescalings, and cut-offs used in the proof of Proposition 3, the metric
$$g_{\epsilon}=\frac{d r^{2}}{1-\phi\left(\frac{r}{\epsilon}\right) \frac{\epsilon^{6}}{r^{2}}}+r^{2}\left(\sigma_{1}^{2}+\sigma_{2}^{2}+\left(1-\phi\left(\frac{r}{\epsilon}\right) \frac{\epsilon^{6}}{r^{2}}\right) \sigma_{3}^{2}\right), \quad r>\epsilon^{3}$$
is flat for $r>2 \epsilon$, scalar-flat for $r<\epsilon$, and has scalar curvature uniformly $O\left(\epsilon^{2}\right)$ as $\epsilon \searrow 0$. Moreover, blowing up a flat region by replacing a small ball by a copy of $g_{\epsilon}$ reduces its total volume, namely by $\pi^{2} \epsilon^{12} / 2$.

Any elliptic surface is an iterated blow-up of a minimal one. Up to diffeomorphism, we can therefore model any such surface by blowing up one of our previous models at distinct points. But the constructed metrics on the previous models can be taken to be flat in the neighborhood of certain fibers provided the orbifold metric $h$ on $\Sigma$ is also taken to be flat on certain regions. So let $\check{g}_{j}$ be a sequence of metrics with bounded Ricci curvature and Vol $\rightarrow 0$, each containing a Euclidean ball of radius $\varrho_{j}$, on a minimal elliptic surface $\check{M}$. On any blow-up $M=\check{M} \# \overline{\mathbb{C P}}_{2}$, we can then produce a sequence of metrics $g_{j}$, with bounded scalar curvature and Vol $\rightarrow 0$ by replacing $\ell$ disjoint, Euclidean $\left(2 \epsilon_{j}\right)$-balls with copies of $g_{\epsilon_{j}}$, where we may, for example, take $\epsilon_{j}=\varrho_{j} / 2 \ell$. \(\square\)

By Proposition 5, this immediately implies
Corollary 1. Any complex elliptic surface $M$ has $Y(M) \geq 0$.
The reader may prefer to deduce this corollary directly from Theorem 4 and the fact that $Y\left(\overline{\mathbb{C P}}_{2}\right)>0$ by citing a general result of [14]. At heart, however, this is much the same proof as is given above.

Combining this corollary with Theorem 1 now yields
Theorem 6. Let $M$ be a Kähler-type complex surface with $\operatorname{Kod}(M)=0$ or 1. Then $Y(M)=0$.

Proof. Any surface of Kodaira dimension 0 or 1 is deformation-equivalent to an elliptic surface [3, 11], and so has $Y(M) \geq 0$ by the previous result. But if $M$ is of Kähler type, Seiberg-Witten theory tells us that there is no metric of positive scalar curvature on $M$, so that $Y(M) \leq 0$. Hence $Y(M)=0$, as claimed. \(\square\)

Combining this with Proposition 2 and Theorem 2 now proves Theorem A.

\section*{6. Concluding Remarks.}

Theorem A does not allow one to distinguish between Kodaira dimensions 0 and 1 by comparing Yamabe invariants. Such a distinction arises
immediately, however, if one asks whether
$$Y(M)=\sup _{[g]} Y_{[g]}$$
is actually realized by the Yamabe constant of some conformal class.
Proposition 6. Let $M$ be the underlying 4-manifold of a complex algebraic surface of Kodaira dimension $\geq 0$. Then $M$ admits a Riemannian metric of scalar curvature 0 if $M$ is minimal and has Kodaira dimension 0. In particular, the Yamabe invariant $Y(M)$ is unachieved whenever $\operatorname{Kod}(M)=$ 1.

Proof. Any minimal Kähler-type complex surface with Kodaira dimension 0 has $c_{1}=0$ in real cohomology, and so carries a Ricci-flat Kähler metric by Yau's solution [27] of the Calabi conjecture. Such a metric has $s=0$, and so realizes $Y(M)=0$.

Conversely [4], if a manifold with $Y(M)=0$ admits a scalar-flat metric, the metric in question must be Ricci-flat, since otherwise it could be deformed into a metric of positive scalar curvature [4]. In dimension 4 , this implies that
$$2 \chi+3 \tau=\frac{1}{4 \pi^{2}} \int_{M}\left[2\left|W_{+}\right|^{2}+\frac{s^{2}}{24}-\frac{|\stackrel{\circ}{r}|^{2}}{2}\right] d \mu \geq 0$$
Our complex surface must therefore satisfy $c_{1}^{2} \geq 0$. If $c_{1}$ is not a torsion class, the Seiberg-Witten invariant of $(M,[J])$ is therefore both metric-independent and non-zero, even if $b^{+}(M)=1$. But the Seiberg-Witten estimate [17]
$$\int_{M} s^{2} d \mu \geq 32 \pi^{2}\left(c_{1}^{+}\right)^{2}$$
then forces $c_{1}$ to be anti-self-dual with respect to any scalar-flat metric; thus $c_{1}^{2} \leq 0$, with equality iff $c_{1}=0$ in real cohomology. Hence $c_{1}$ is a torsion class, and our surface must be a minimal surface of Kodaira dimension 0. □

While this makes a satisfactory distinction between minimal surfaces of Kodaira dimensions 0 and 1, it is still unsatisfactory for non-minimal surfaces. However, it is not hard to see that there are sequences of unit-volume constant-scalar-curvature metrics on any blow-up of, say, a K3 surface which
bubble off to any given Kähler-Einstein metric on the minimal model. The metrics in this sequence have uniformly bounded diameter. It seems plausible to conjecture that this does not happen in the case of Kodaira dimension 1:

Conjecture 1. Let $M$ be the underlying 4-manifold of a complex algebraic surface of Kodaira dimension $\geq 0$. Suppose that there is a sequence of unit-volume constant-scalar-curvature metrics on $M$ with uniformly bounded diameter and $s \nearrow 0$. Then $\operatorname{Kod}(M)=0$.

Of course, beyond simply knowing the sign of $Y(M)$, one would like to ask to know its actual value. When $b_{1}(M)$ is even and $\operatorname{Kod}(M) \geq 0$, this question is completely answered by Theorems 2 and 6. For algebraic surfaces with $\operatorname{Kod}(M)=-\infty$, however, the only case in which $Y(M)$ is actually known is for $M=\mathbb{C P}_{2}$, where $Y(M)$ is actually realized by the Fubini-Study metric [19]. It is, in particular, unclear whether blowing up leaves $Y(M)$ unchanged when $\operatorname{Kod}(M)=-\infty$, although this is what happens when the Kodaira dimension is larger.

There are a number of places in this paper where we have assumed that the surface in question has $b_{1}$ even in order to assure that there is a non-trivial Seiberg-Witten invariant. However, this is superfluous in Kodaira dimension 0 , since Kodaira surfaces are symplectic and so have non-trivial invariants by the work of Taubes [25]. For Kodaira dimension 1 the situation is less clear, but Biquard [6] has also shown that some non-Kähler surfaces in this class have non-trivial Seiberg-Witten invariants. Thus it would be surprising if the following were not true:

Conjecture 2. Let $M$ be the underlying 4-manifold of a compact complex manifold of Kodaira dimension 0 or 1. Then, even if $b_{1}(M)$ is odd, one still has $Y(M)=0$.

Even allowing for the case of $b_{1}$ odd, the following is an immediate consequence of the results proven here:

Theorem 7. Let $(M, J)$ be any compact complex surface. If $Y(M)<0$, then $M$ is either of general type or of type VII.

For all known surfaces of type $V I I$, however, one can check by hand that $Y \geq 0$. It therefore seems reasonable to make the following

Conjecture 3. Let $(M, J)$ be any compact complex surface. If $Y(M)<0$, then $M$ is of general type.

Finally, we have accidentally computed the infima of some other Riemannian functionals by showing that minimal elliptic surfaces collapse with bounded Ricci curvature.

Proposition 7. Let $M$ be the underlying 4-manifold of any complex elliptic surface. Then
$$\inf _{[g]} \int_{M}\left|W_{+}\right|^{2} d \mu=0 .$$
Here $W_{+}$denotes the self-dual Weyl tensor, and the infimum is over the set of all conformal classes of Riemannian metrics on $M$. As a consequence
$$\inf _{[g]} \int_{M}\left|W_{-}\right|^{2} d \mu=-12 \pi^{2} \tau(\dot{M})$$

Indeed, if $M$ is minimal, this follows from Theorem 4 and the Gauss-Bonnet formula for $(2 \chi+3 \tau)(M)=0$. Since the Burns metric is anti-self-dual, it is easy to extend this to the non-minimal case; cf. [24].

By Taubes' existence theorem [24] for anti-self-dual metrics, any complex surface, after being blown up sufficiently many times, admits metrics with $W_{+}=0$. The last result raises, once again, the fascinating question of determining precisely how many times a given complex surface must be blown up before this happens.

Acknowledgement. The author warmly thanks Michael Anderson, Peter Kronheimer, and Heberto del Rio for their helpful comments and suggestions.

\section*{References.}
\begin{itemize}
\item[] [1] M.T.Anderson, Extrema of Curvature Functionals on the Space of Metrics on 3-Manifolds, Calc. Var. Partial Diff. Eq., 5 (1997), 199-269.
\item[] [2] T.Aubin, Nonlinear Analysis on Manifolds. Monge-Ampère Equations, Springer-Verlag, 1982.
\item[] [3] W.Barth, C.Peters and A.Van de Ven, Compact Complex Surfaces, Springer-Verlag, 1984.
\item[] [4] A.Besse, Einstein Manifolds, Springer-Verlag, 1987.
\item[] [5] G.Besson, G.Courtois, and S.Gallot, Les Variétés Hyperboliques Sont des Minima Locaux de l'Entropie Topologique, Inv. Math. 117 (1994), 403-445.
\end{itemize}
\begin{itemize}
\item[] [6] O.Biquard, Les Équations de Seiberg-Witten sur une Surface Complexe Non Kählérienne, Comm. in Anal. Geom. 6 (1998), 173-197.
\item[] [7] J.Cheeger and M.Gromov, Collapsing Riemannian Manifolds While Keeping Their Curvature Bounded I, J. Diff. Geom. 23 (1986), 309-346.
\item[] [8] J.Cheeger and M.Gromov, Collapsing Riemannian Manifolds While Keeping Their Curvature Bounded II, J. Diff. Geom. 32 (1990), 269-298.
\item[] [9] T.Eguchi and A.J.Hanson, Asymptotically Flat Self-Dual Solutions to Euclidean Gravity, Phys. Lett. 74B (1978), 249-251.
\item[] [10] R.Friedman and J.Morgan, Smooth 4-Manifolds and Complex Surfaces, Springer-Verlag, 1994.
\item[] [11] R.Friedman and J.Morgan, Algebraic Surfaces and Seiberg-Witten Invariants, J. Alg. Goem. 6 (1997), 445-479.
\item[] [12] R.Friedman and Z.Qin, The Smooth Invariance of the Kodaira Dimension of a Complex Surface, Math. Res. Lett. 1 (1994), 369-376.
\item[] [13] M.Gromov and H.B.Lawson, The Classification of Simply Connected Manifolds of Positive Scalar Curvature, Ann. of Math. 111 (1980), 423-434.
\item[] [14] O.Kobayashi, Scalar Curvature of a Metric of Unit Volume, Math. Ann. 279 (1987), 253-265.
\item[] [15] C.LeBrun, Counter-Examples to the Generalized Positive Action Conjecture, Comm. Math. Phys. 118 (1988), 1205-1208.
\item[] [16] C.LeBrun, On the Scalar Curvature of Complex Surfaces, Geom. Func. An. 5 (1995), 619-628.
\item[] [17] C.LeBrun, Polarized 4-Manifolds, Extremal Kähler Metrics, and Seiberg-Witten Theory, Math. Res. Lett. 2 (1995), 653-662.
\item[] [18] C.LeBrun, Four-Manifolds without Einstein Metrics, Math. Res. Lett. 3 (1996), 133-147.
\item[] [19] C.LeBrun, Yamabe Constants and the Perturbed Seiberg-Witten Equations, Comm. An. Geom. 5 (1997), 535-553.
\item[] [20] J.Lee and T.Parker, The Yamabe Problem, Bull. Am. Math. Soc. 17 (1987), 37-91.
\item[] [21] Y.Matsumoto, Diffeomorphism Types of Elliptic Surfaces, Topology 25 (1986), 549-563.
\item[] [22] R.Schoen, Conformal Deformation of a Riemannian Metric to Constant Scalar Curvature, J. Diff. Geom. 20 (1984), 478-495.
\end{itemize}
\begin{itemize}
\item[] [23] R.Schoen, Variational Theory for the Total Scalar Curvature Functional for Riemannian Metrics and Related Topics, Lec. Notes Math. 1365 (1987), 120-154.
\item[] [24] C.H.Taubes, The Existence of Anti-Self-Dual Metrics, J. Diff. Geometry 36 (1992), 163-253.
\item[] [25] C.H.Taubes, The Seiberg-Witten Invariants and Symplectic Forms, Math. Res. Lett. 1 (1994), 809-822.
\item[] [26] E.Witten, Monopoles and Four-Manifolds, Math. Res. Lett. 1 (1994), 809-822.
\item[] [27] S.-T.Yau, On the Ricci-Curvature of a Complex Kähler Manifold and the Complex Monge-Ampère Equations, Comment. Pure Appl. Math. 31 (1978), 339-411.
\end{itemize}

Received February 19, 1997.

SUNY
Stony Brook
