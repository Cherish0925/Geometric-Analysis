# Weyl Curvature, Einstein Metrics, and Seiberg-Witten Theory

- Category: papers
- Identity: arxiv:math/9803093
- Content status: fulltext_ok

---

---
source_file: math_9803093v2.pdf
converter: mathpix
format: mmd
---

\title{
Weyl Curvature, Einstein Metrics, and Seiberg-Witten Theory
}

\author{
Claude LeBrun* \\ SUNY Stony Brook
}

March 20, 1998
Revised April 14, 1998

\begin{abstract}
We show that solutions of the Seiberg-Witten equations lead to nontrivial estimates for the $L^{2}$-norm of the Weyl curvature of a smooth compact 4-manifold. These estimates are then used to derive new obstructions to the existence of Einstein metrics on smooth compact 4-manifolds with a non-zero Seiberg-Witten invariant. These results considerably refine those previously obtained [21] by using scalar-curvature estimates alone.
\end{abstract}

\section*{1 Introduction}

A smooth Riemannian metric $g$ is said to be Einstein if its Ricci curvature $r$ is a constant multiple of the metric:
$$r=\lambda g .$$
Not every smooth compact oriented 4-manifold $M$ admits such a metric. Indeed, a well-known necessary condition is that $M$ must satisfy [10, 29, 3] the HitchinThorpe inequality $2 \chi(M) \geq 3|\tau(M)|$, where $\chi$ and $\tau$ respectively denote the signature and Euler characteristic. This is forced on one by the Gauss-Bonnetlike formula
$$(2 \chi \pm 3 \tau)(M)=\frac{1}{4 \pi^{2}} \int_{M}\left(2\left|W_{ \pm}\right|^{2}+\frac{s^{2}}{24}-\frac{|\stackrel{\circ}{r}|^{2}}{2}\right) d \mu$$
where $s, \stackrel{\circ}{r}, W_{+}$, and $W_{-}$respectively denote the scalar, trace-free Ricci, selfdual Weyl, and anti-self-dual Weyl curvatures of an arbitrary Riemannian metric $g$, whose point-wise norms $|\cdot|$ and volume form $d \mu$ also appear in the integral. The Hitchin-Thorpe inequality follows immediately because Einstein metrics are

\footnotetext{
*Supported in part by NSF grant DMS-9505744.
}
characterized by the vanishing of $\stackrel{\circ}{r}$, and $\stackrel{\circ}{r}$ makes the only negative contribution to the integrand.

One could obviously improve this result if one had, say, non-trivial lower bounds for the the scalar-curvature contribution to the integral. And indeed, this is precisely what has happened over the course of the past few years. For example, simplicial volume [9, 3] and entropy estimates [5, 24] lead to new obstructions for certain spaces with infinite fundamental group. In another direction, the Hitchin-Thorpe argument can be dramatically improved upon [19, 21] through the use of scalar-curvature estimates arising from the Seiberg-Witten equations [30, 14] if, for example, the smooth 4-manifold in question admits a symplectic form [27].

The present article will show that the Seiberg-Witten equations also give rise to a priori control of the $L^{2}$-norm of $W_{+}$. Our main result in this direction is as follows:

Theorem A Let $(M, g)$ be a compact oriented Riemannian 4-manifold with a non-trivial Seiberg-Witten invariant. Let $c_{1}(L) \in H^{2}(M, \mathbb{R})$ be the first Chern class of the corresponding spin ${ }^{c}$ structure on $M$, and let $c_{1}^{+} \neq 0$ denote its projection into the space of $g$-self-dual harmonic 2-forms. Then
$$\frac{1}{4 \pi^{2}} \int_{M}\left(2\left|W_{+}\right|^{2}+\frac{s^{2}}{24}\right) d \mu>\frac{32}{57}\left(c_{1}^{+}\right)^{2}$$

This leads to new obstructions to the existence of Einstein metrics. Recall that a complex surface $M$ of general type admits a Kähler-Einstein metric only if $M$ cannot be smoothly decomposed as a connected sum $X \# k \overline{\mathbb{C P}}_{2}, k>0$. If one instead wishes to consider Einstein metrics which are not necessarily Kähler, similar statements can be proved if one assumes that $k$ is sufficiently large. Indeed, Theorem A implies the following result:

Theorem B Let $X$ be a smooth compact oriented 4-manifold with $2 \chi+3 \tau>0$. Assume, moreover, that $X$ has a non-trivial Seiberg-Witten invariant. Then $X \# k \overline{\mathbb{C P}}_{2}$ does not admit Einstein metrics for any $k \geq \frac{25}{57}(2 \chi+3 \tau)(X)$.

This result should be compared to the main result of [21], where the same conclusion is reached for $k \geq \frac{2}{3}(2 \chi+3 \tau)(X)$. On the other hand, the Hitchin-Thorpe inequality merely excludes existence when $k \geq(2 \chi+3 \tau)(X)$. Since $\frac{25}{57}<\frac{4}{9}=\left(\frac{2}{3}\right)^{2}$, it seems fair to say that Theorem B improves on [21] by a bigger margin than that by which [21] improved upon its antecedent.

It should be emphasized that the obstructions studied here strongly depend on the given smooth structure. Indeed, Kotschick [13] recently pointed out infinitely many examples which do not admit Einstein metrics by [21], but which are nonetheless homeomorphic to 4-manifolds which do admit Einstein metrics. As we shall see in §4, Theorem B gives rise to a plethora of examples of this type which would have been unobtainable by previous methods.

\section*{2 Weyl Estimates}

Let $M$ be a smooth, compact, oriented 4-manifold. Each Riemannian metric $g$ on $M$ then determines a direct sum decomposition
$$H^{2}(M, \mathbb{R})=\mathcal{H}_{g}^{+} \oplus \mathcal{H}_{g}^{-},$$
where $\mathcal{H}_{g}^{+}$(respectively, $\mathcal{H}_{g}^{-}$) consists of those cohomology classes for which the harmonic representative is self-dual (respectively, anti-self-dual). The nonnegative integer $b_{+}(M)=\operatorname{dim} \mathcal{H}_{g}^{+}$is independent of $g$, and we will henceforth always assume it to be positive. It is thus natural to consider the set of metrics $g$ for which $\mathcal{H}_{g}^{+}=H$ for some fixed $b_{+}(M)$-dimensional subspace $H \subset H^{2}(M, \mathbb{R})$; such metrics will be said to be $H$-adapted. Assuming there is at least one $H$-adapted metric, we will then say that $H$ is a polarization of $M$, and [20] call the pair $(M, H)$ a polarized 4-manifold. Notice that the restriction of the intersection pairing
$$\smile: H^{2}(M, \mathbb{R}) \times H^{2}(M, \mathbb{R}) \rightarrow \mathbb{R}$$
to $H$ is then positive definite, and that $H \subset H^{2}$ is maximal among subspaces with this property.

Let $c$ be a $\operatorname{spin}^{c}$ structure on $M$. Then $c$ determines a Hermitian line-bundle $L \rightarrow M$ with
$$c_{1}(L) \equiv w_{2}(M) \bmod 2,$$
and for each metric $g$ we also have rank-2 complex vector bundles $V_{ \pm} \rightarrow M$ which formally satisfy
$$V_{ \pm}=\mathbb{S}_{ \pm} \otimes L^{1 / 2},$$
where $\mathbb{S}_{ \pm}$are the locally-defined left- and right-handed spinor bundles of $g$. Given a polarization $H$ on $M$, we will then use $c_{1}^{+}$to denote the orthogonal projection of $c_{1}(L)$ into $H$ with respect to the intersection form. If $g$ is a particular metric with $\mathcal{H}_{g}^{+}=H$, we will also freely use $c_{1}(L)$ to denote the $g$-harmonic 2-form representing the corresponding de Rham class, and use $c_{1}^{+}$ to denote its self-dual part. For example, if a choice of $H$-compatible metric $g$ has already been made, the number
$$\left|c_{1}^{+}\right|:=\sqrt{\left(c_{1}^{+}\right)^{2}}$$
may freely be identified with the $\mathrm{L}^{2}$-norm of the self-dual $g$-harmonic form denoted by $c_{1}^{+}$.

For each Riemannian metric $g$, the Seiberg-Witten equations [30]
$$\begin{aligned}
D_{A} \Phi & =0 \\
F_{A}^{+} & =i \sigma(\Phi)
\end{aligned}$$
are equations for an unknown Hermitian connection $A$ on $L$ and an unknown smooth section $\Phi$ of $V_{+}$. Here the canonical real-quadratic map $\sigma: V_{+} \rightarrow$
$\Lambda^{+}$is invariant under parallel transport, and satisfies $|\sigma(\Phi)|^{2}=|\Phi|^{4} / 8$. If a spin $^{c}$ structure satisfies $\left[c_{1}(L)\right]^{2}=(2 \chi+3 \tau)(M)$, and if $c_{1}^{+} \neq 0$ relative to the polarization $H=\mathcal{H}_{g}^{+}$, then the Seiberg-Witten invariant $n_{c}(M, H)$ can be defined [14, 30] as the number of solutions, modulo gauge transformations and counted with orientations, of a generic perturbation
$$\begin{aligned}
D_{A} \Phi & =0 \\
i F_{A}^{+}+\sigma(\Phi) & =\phi
\end{aligned}$$
of (2-3), where $\phi$ is a smooth self-dual 2-form of small $L^{2}$ norm. More generally, if $c$ is a spin ${ }^{c}$ structure for which $\ell=\left[c_{1}^{2}(L)-(2 \chi+3 \tau)(M)\right] / 4$ is non-negative and even, one can define [28] the perturbed Seiberg-Witten invariant $n_{c}(M, H)$ to be $\int_{Z} \eta^{\ell / 2}$, where $Z$ is the $\ell$-dimensional smooth compact moduli space of solutions of a generic small perturbation of the equations, and $\eta \in H^{2}(Z)$ is the first Chern class of the based moduli space, considered as an $S^{1}$-bundle over $Z$. For other values of $c_{1}^{2}(L)$, one simply sets $n_{c}(M, H)=0$ as a matter of definition. For our purposes, the point is simply that when $c_{1}^{+}$and $n_{c}(M, H)$ are both non-zero, (2-3) must have a solution with $\Phi \not \equiv 0$ for every $H$-adapted metric $g$. Moreover, these equations imply the Weitzenböck formula
$$4 \nabla_{A}^{*} \nabla_{A} \Phi+s \Phi+|\Phi|^{2} \Phi=0 .$$

Theorem 1 Let $(M, H)$ be a polarized smooth compact oriented 4-manifold, and let $c$ be a spin ${ }^{c}$ structure on $M$ for which the Seiberg-Witten invariant $n_{c}(M, H)$ is non-zero; let $c_{1}(L) \in H^{2}(M, \mathbb{R})$ denote the anti-canonical class of $c$, and let $c_{1}^{+} \neq 0$ be its orthogonal projection to $H$ with respect to the intersection form. Then every $H$-adapted Riemannian metric $g$ satisfies
$$\left(\int\left|W_{+}\right|^{2} d \mu\right)^{1 / 2} \geq\left(4-3 \beta^{1 / 2}\right) \frac{2 \pi}{\sqrt{3}}\left|c_{1}^{+}\right|,$$
where
$$\beta=\frac{\int s^{2} d \mu}{32 \pi^{2}\left(c_{1}^{+}\right)^{2}} \geq 1$$
Moreover, equality can occur only if $\beta=1$.

Proof. Recall that every every conformal class on $M$ contains [1, 23, 25] a Yamabe metric, and that such a metric minimizes $\int s^{2} d \mu$ in its conformal class [4, 21]. Now all such metrics have constant scalar curvature. Since $\int\left|W_{+}\right|^{2} d \mu$ is conformally invariant, the form of the desired inequality therefore allows us to assume henceforth that $g$ has constant scalar curvature. But because $\left(c_{1}^{+}\right)^{2} \neq 0$ and the Seiberg-Witten invariant $n_{c}(M, H)$ is assumed to be non-zero, $g$ cannot [20] have $s \geq 0$. We may thus assume henceforth that $g$ has constant scalar curvature $s<0$.

Now because $n_{c}(M, H) \neq 0$ by assumption, there must exist an irreducible solution of (2) and (3). But the Weitzenböck formula (4) tells us that
$$\begin{aligned}
8 \int_{M}\left|\nabla_{A} \Phi\right|^{2} d \mu & =2 \int\left(-s-|\Phi|^{2}\right)|\Phi|^{2} d \mu \\
& =\int\left(-s-|\Phi|^{2}\right)\left(-s+|\Phi|^{2}\right) d \mu-\int\left(-s-|\Phi|^{2}\right)^{2} d \mu \\
& =\|s\|_{2}^{2}-\|\Phi\|_{4}^{4}-\left\|\left(|s|-|\Phi|^{2}\right)\right\|_{2}^{2} \\
& \leq\|s\|_{2}^{2}-\|\Phi\|_{4}^{4}-\left(\|s\|_{2}-\|\Phi\|_{4}^{2}\right)^{2} \\
& =2\left(\|s\|_{2}-\|\Phi\|_{4}^{2}\right)\|\Phi\|_{4}^{2}
\end{aligned}$$
and hence
$$\frac{\left\|\nabla_{A} \Phi\right\|_{2}^{2}}{\|\Phi\|_{4}^{2}} \leq \frac{1}{4}\left(\|s\|_{2}-4 \sqrt{2} \pi\left|c_{1}^{+}\right|\right)=\left(\beta^{1 / 2}-1\right) \sqrt{2} \pi\left|c_{1}^{+}\right| .$$
Here we have used the observation that $|\Phi|^{4}=8\left|F_{A}^{+}\right|^{2}$, as is implied by (3), together with the fact that $2 \pi c_{1}^{+}$is the harmonic part of $F_{A}^{+}$.

Since we have assumed that $s$ is a negative constant, the Weitzenböck formula (4) also implies [14] the $C^{0}$ estimate
$$|\Phi|^{2} \leq|s| .$$
Since (2) implies that
$$\left|\nabla F_{A}^{+}\right|^{2} \leq \frac{1}{2}|\Phi|^{2}\left|\nabla_{A} \Phi\right|^{2}$$
it now follows that
$$\frac{\left\|\nabla F_{A}^{+}\right\|_{2}^{2}}{\left\|F_{A}^{+}\right\|_{2}} \leq \sqrt{2}|s| \frac{\left\|\nabla_{A} \Phi\right\|_{2}^{2}}{\|\Phi\|_{4}^{2}} \leq|s|\left(\beta^{1 / 2}-1\right) 2 \pi\left|c_{1}^{+}\right| .$$

Now any self-dual 2-form $\varphi$ on any oriented 4-manifold satisfies [6] the Weitzenböck formula
$$\left(d+d^{*}\right)^{2} \varphi=\nabla^{*} \nabla \varphi-2 W^{+}(\varphi, \cdot)+\frac{s}{3} \varphi,$$
where $W^{+}$is the self-dual Weyl tensor. It follows that
$$\int_{M}\left(-W^{+}\right)(\varphi, \varphi) \geq \int_{M}\left(-\frac{s}{6}\right)|\varphi|^{2} d \mu-\frac{1}{2} \int_{M}|\nabla \varphi|^{2} d \mu$$
On the other hand, $W^{+}$is a trace-free quadratic form on $\Lambda^{+}$, so that $\left|W^{+}\right||\varphi|^{2} \geq$ $\sqrt{\frac{3}{2}}\left(-W^{+}\right)(\varphi, \varphi)$. Again assuming that the scalar curvature $s$ of $g$ is a negative constant, we therefore have
$$\left(\int\left|W^{+}\right|^{2} d \mu\right)^{1 / 2}\left(\int|\varphi|^{4} d \mu\right)^{1 / 2} \geq \frac{|s|}{2 \sqrt{2}}\left[\frac{1}{\sqrt{3}}\|\varphi\|_{2}^{2}-\frac{\sqrt{3}}{|s|}\|\nabla \varphi\|_{2}^{2}\right]$$
and hence, assuming that $\varphi \not \equiv 0$, we have
$$\left(\int\left|W^{+}\right|^{2} d \mu\right)^{1 / 2} \geq \sqrt{\frac{s^{2}\|\varphi\|_{2}^{2}}{8\|\varphi\|_{4}^{4}}}\left[\frac{1}{\sqrt{3}}\|\varphi\|_{2}-\frac{\sqrt{3}}{|s|} \frac{\|\nabla \varphi\|_{2}^{2}}{\|\varphi\|_{2}}\right] .$$

We now apply this to $\varphi=F_{A}^{+}$. Because $\left|F_{A}^{+}\right|^{2}=\frac{1}{8}|\Phi|^{4} \leq \frac{s^{2}}{8}$, we have
$$\frac{s^{2}\left\|F_{A}^{+}\right\|_{2}^{2}}{8\left\|F_{A}^{+}\right\|_{4}^{4}}=\frac{\left(s^{2} / 8\right) \int\left|F_{A}^{+}\right|^{2} d \mu}{\int\left|F_{A}^{+}\right|^{4} d \mu} \geq 1$$
It follows that
$$\begin{aligned}
\left(\int\left|W^{+}\right|^{2} d \mu\right)^{1 / 2} & \geq \frac{1}{\sqrt{3}}\left\|F_{A}^{+}\right\|_{2}-\frac{\sqrt{3}}{|s|} \frac{\left\|\nabla F_{A}^{+}\right\|_{2}^{2}}{\left\|F_{A}^{+}\right\|_{2}} \\
& \geq \frac{1}{\sqrt{3}}\left\|F_{A}^{+}\right\|_{2}-\frac{\sqrt{3}}{|s|}|s|\left(\beta^{1 / 2}-1\right) 2 \pi\left|c_{1}^{+}\right| \\
& \geq \frac{2 \pi}{\sqrt{3}}\left|c_{1}^{+}\right|-\sqrt{3}\left(\beta^{1 / 2}-1\right) 2 \pi\left|c_{1}^{+}\right| \\
& =\left[1-3\left(\beta^{1 / 2}-1\right)\right] \frac{2 \pi}{\sqrt{3}}\left|c_{1}^{+}\right| \\
& =\left(4-3 \beta^{1 / 2}\right) \frac{2 \pi}{\sqrt{3}}\left|c_{1}^{+}\right| .
\end{aligned}$$
If equality holds, moreover, $F_{A}^{+}$must be harmonic and $\left|F_{A}^{+}\right|^{2} \equiv s^{2} / 8$, so that $\beta=1$, as claimed. \(\square\)

This immediately implies a new characterization of constant-scalar-curvature Kähler metrics; cf. [20].

Corollary 1 Let $(M, H)$ be a polarized smooth compact oriented 4-manifold, and let $c$ be a spin ${ }^{c}$ structure on $M$. Assume, moreover, that $c_{1}^{+} \neq 0$ and that the Seiberg-Witten invariant $n_{c}(M, H)$ is non-zero. Then every $H$-adapted Riemannian metric $g$ on $M$ satisfies
$$\frac{1}{4 \pi^{2}} \int_{M}\left(\frac{1}{3}\left|W_{+}\right|^{2}+\frac{s^{2}}{24}\right) d \mu \geq \frac{4}{9}\left(c_{1}^{+}\right)^{2}$$
with equality iff $g$ is Kähler (for a $c$-compatible complex structure) and has constant negative scalar curvature.

Proof. Let us set
$$\alpha=\frac{3}{2}(\beta-1)=\frac{3}{2}\left(\frac{\int s^{2} d \mu}{32 \pi^{2}\left(c_{1}^{+}\right)^{2}}-1\right) \geq 0$$
so that
$$\beta^{1 / 2} \leq 1+\frac{1}{3} \alpha .$$

Theorem 1 then tells us that
$$\left(\int_{M}\left|W_{+}\right|^{2} d \mu\right)^{1 / 2} \geq(1-\alpha) \frac{2 \pi}{\sqrt{3}}\left|c_{1}^{+}\right| .$$
But $x \geq 1-h \Longrightarrow x^{2} \geq 1-2 h$, since the parabola $y=x^{2}$ sits above its tangent line at $x=1$. We therefore have
$$\int_{M}\left|W_{+}\right|^{2} d \mu \geq(1-2 \alpha) \frac{4 \pi^{2}}{3}\left(c_{1}^{+}\right)^{2}=4 \pi^{2} \frac{4}{3}\left(c_{1}^{+}\right)^{2}-\frac{1}{8} \int s^{2} d \mu$$
which is to say that
$$\frac{1}{4 \pi^{2}} \int_{M}\left(\frac{1}{3}\left|W_{+}\right|^{2}+\frac{s^{2}}{24}\right) d \mu \geq \frac{4}{9}\left(c_{1}^{+}\right)^{2}$$

If equality is achieved, the metric is a Yamabe minimizer, and so has constant scalar curvature; moreover, $\nabla F_{A}^{+}=0$, and since $F_{A}^{+} \not \equiv 0$, it follows that the metric is Kähler. Conversely, the Seiberg-Witten invariant is non-zero for a Kähler surface with $c_{1} \cdot[\omega]<0$, where $[\omega]$ is the Kähler class; and since any Kähler metric satisfies $\left|W_{+}\right|^{2}=s^{2} / 24, \int s d \mu=4 \pi c_{1} \cdot[\omega]$, and $\int d \mu=[\omega]^{2} / 2$, the inequality is precisely saturated by Kähler metrics of constant negative scalar curvature. \(\square\)

Remark If $c_{1}^{+}=0$ and $b_{+}=1$, the Seiberg-Witten invariant is ill-defined. However, the relevant inequality
$$\frac{1}{4 \pi^{2}} \int_{M}\left(\frac{1}{3}\left|W_{+}\right|^{2}+\frac{s^{2}}{24}\right) d \mu \geq \frac{4}{9}\left(c_{1}^{+}\right)^{2}=0$$
has become a triviality in this case. Moreover, equality occurs precisely when the metric is scalar-flat and anti-self-dual, and, since we have assumed that $b_{+} \neq 0$, the Weitzenböck formula for 2-forms then shows [16, 17] that any such metric is scalar-flat Kähler. Much the same conclusion therefore holds in this case, albeit for slightly different reasons. \(\square\)

In another direction, recall that Taubes [26] has shown that for any smooth compact orientable $X^{4}$, there is an integer $k_{0}$ such that $M=X \# k \overline{\mathbb{C P}}_{2}$ admits metrics with $W_{+}=0$ provided that $k \geq k_{0}$. In particular, there are many anti-self-dual 4-manifolds with non-trivial Seiberg-Witten invariants. For such manifolds, we get an interesting scalar-curvature estimate.

Corollary 2 Let $(M, g)$ be a compact anti-self-dual 4-manifold with a non-zero Seiberg-Witten invariant. Then
$$\frac{1}{32 \pi^{2}} \int_{M} s^{2} d \mu>\frac{16}{9}\left(c_{1}^{+}\right)^{2}$$
where $c_{1}^{+}$is again the self-dual part of the first Chern class of the relevant spin ${ }^{c}$ structure.

Proof. By Theorem 1, one must have $\beta>\left(\frac{4}{3}\right)^{2}$ if $W_{+} \equiv 0$. \(\square\)

One may use this as a vanishing theorem. For example, it immediately implies that the Seiberg-Witten invariant must vanish for all those spin ${ }^{c}$ structure on a hyperbolic 4-manifold which satisfy $\left(c_{1}^{+}\right)^{2} \geq \frac{32}{3} \chi$. One might guess that all the Seiberg-Witten invariants of a hyperbolic 4-manifold must vanish, but there is very little hard evidence either for or against such a conjecture.

We now come to our main technical result, which, while certainly not sharp in the above sense, will yield better results in many interesting contexts:

Theorem A Let $(M, H, c)$ be as above. Then every $H$-adapted Riemannian metric $g$ satisfies
$$\frac{1}{4 \pi^{2}} \int_{M}\left(2\left|W_{+}\right|^{2}+\frac{s^{2}}{24}\right) d \mu>\frac{32}{57}\left(c_{1}^{+}\right)^{2}$$
Proof. Our definition (5) of $\beta$ has been chosen so that
$$\frac{1}{4 \pi^{2}} \int_{M} \frac{s^{2}}{24} d \mu=\beta \frac{\left(c_{1}^{+}\right)^{2}}{3}$$
If $\beta>\frac{16}{9}$, we therefore have
$$\frac{1}{4 \pi^{2}} \int_{M}\left(2\left|W_{+}\right|^{2}+\frac{s^{2}}{24}\right) d \mu>\frac{16}{27}\left(c_{1}^{+}\right)^{2}>\frac{32}{57}\left(c_{1}^{+}\right)^{2}$$
for trivial reasons. We may therefore assume henceforth that $\beta \in\left[1, \frac{16}{9}\right]$.
This assumption, however, guarantees that both sides of the inequality
$$\left(\int\left|W_{+}\right|^{2} d \mu\right)^{1 / 2} \geq\left(4-3 \beta^{1 / 2}\right) \frac{2 \pi}{\sqrt{3}}\left|c_{1}^{+}\right|$$
are non-negative. It then follows that
$$\frac{1}{4 \pi^{2}} \int\left|W_{+}\right|^{2} d \mu \geq\left(4-3 \beta^{1 / 2}\right)^{2} \frac{\left(c_{1}^{+}\right)^{2}}{3}$$
Hence
$$\begin{aligned}
\frac{1}{4 \pi^{2}} \int_{M}\left(2\left|W_{+}\right|^{2}+\frac{s^{2}}{24}\right) d \mu & \geq\left[\beta+2\left(4-3 \beta^{1 / 2}\right)^{2}\right] \frac{\left(c_{1}^{+}\right)^{2}}{3} \\
& =\left[19\left(\beta^{1 / 2}-\frac{24}{19}\right)^{2}+\frac{32}{19}\right] \frac{\left(c_{1}^{+}\right)^{2}}{3}
\end{aligned}$$
with equality only if $\beta=1$. Hence
$$\frac{1}{4 \pi^{2}} \int_{M}\left(2\left|W_{+}\right|^{2}+\frac{s^{2}}{24}\right) d \mu>\frac{32}{57}\left(c_{1}^{+}\right)^{2}$$
whenever the Seiberg-Witten invariant is non-zero. \(\square\)

Remark Kronheimer [15] recently showed that certain 4-manifolds with vanishing Seiberg-Witten invariants nonetheless have the remarkable property that there is a solution of the Seiberg-Witten equations (with fixed spin ${ }^{c}$ structure) for each and every metric. The present results manifestly also apply to such manifolds, since the above proofs stem directly from structure of the equations rather than from formal properties of the invariant. For our present purposes, however, this phenomenon does not yet seem to have any interesting ramifications; in particular, all of Kronheimer's examples have $2 \chi+3 \tau \leq 0$, and indeed can actually be collapsed to zero volume while keeping $s$ and $\left|W_{+}\right|$bounded. \(\square\)

\section*{3 Einstein Metrics}

Up until now, we have been discussing the Seiberg-Witten invariants of a polarized 4-manifold $(M, H)$. These are always well-defined for any spin ${ }^{c}$ structure with $c_{1}^{+} \neq 0$. When $b_{+}(M)>1$, moreover, they are even independent of the choice of $H$, since any two generic choices of polarization may be joined by a path for which $c_{1}^{+}$is always non-zero. When $b_{+}(M)=1$, however, a different feature emerges: the intersection form is of Lorentz type, and the value of the invariant depends on whether $c_{1}^{+}$is 'future pointing' or 'past pointing' with respect to a given time-orientation for $H^{2}(M)$. On the other hand, if our manifold has $2 \chi+3 \tau>0, c_{1}(L)$ is automatically time-like, and only one of these possibilities actually occurs. Thus it makes perfectly good sense to speak of the the Seiberg-Witten invariant of a 4-manifold with $b_{+}=1$ as long as $2 \chi+3 \tau>0$. Indeed, the same reasoning even applies if $2 \chi+3 \tau=0$, provided that $c_{1}(L)$ is not a torsion class.

The following observation [21, 13] is the work-horse to which our estimates will be harnessed:

Lemma 1 Let X be a smooth compact oriented 4-manifold with $2 \chi+3 \tau>0$. Assume, moreover, that some Seiberg-Witten invariant of $X$ is non-trivial. Let $k$ be any natural number, and let $H$ be any polarization of $M=X \# k \overline{\mathbb{C P}}_{2}$. Then there is a spin ${ }^{c}$ structure $c$ on $M$ such that $n_{c}(M, H) \neq 0$ and
$$\left(c_{1}^{+}\right)^{2} \geq(2 \chi+3 \tau)(X) .$$

Proof. Let $c_{1}(X)$ denote the first Chern class of a spin ${ }^{c}$ structure on $X$ for which the Seiberg-Witten invariant is non-zero, and notice that $\left(c_{1}(X)\right)^{2} \geq$ $(2 \chi+3 \tau)(X)>0$, because the relevant Seiberg-Witten moduli space must have non-negative virtual dimension. Pull $c_{1}(X)$ back to $M=X \# k \overline{\mathbb{C P}}_{2}$ via the canonical collapsing map, and, by a standard abuse of notation, let us also
use $c_{1}(X)$ to denote the pulled-back class. Thus, with respect to our given polarization,
$$\left(\left[c_{1}(X)\right]^{+}\right)^{2} \geq\left(c_{1}(X)\right)^{2} \geq(2 \chi+3 \tau)(X)>0 .$$
Now choose generators $E_{1}, \ldots, E_{k}$ for the pull-backs to $M$ of the $k$ relevant copies of $H^{2}\left(\overline{\mathbb{C P}}_{2}, \mathbb{Z}\right)$ so that
$$\left[c_{1}(X)\right]^{+} \cdot E_{j} \geq 0, \quad j=1, \ldots, k .$$
Then [8] there is a spin ${ }^{c}$ structure on $M$ with $n_{c}(M, H) \neq 0$ and
$$c_{1}(L)=c_{1}(X)+\sum_{j=1}^{k} E_{j} .$$
But one then has
$$\begin{aligned}
\left(c_{1}^{+}\right)^{2} & =\left(\left[c_{1}(X)\right]^{+}+\sum_{j=1}^{k} E_{j}^{+}\right)^{2} \\
& =\left(\left[c_{1}(X)\right]^{+}\right)^{2}+2 \sum_{j=1}^{k}\left[c_{1}(X)\right]^{+} \cdot E_{j}+\left(\sum_{j=1}^{k} E_{j}^{+}\right)^{2} \\
& \geq\left(\left[c_{1}(X)\right]^{+}\right)^{2} \\
& \geq(2 \chi+3 \tau)(X),
\end{aligned}$$
exactly as claimed. \(\square\)

Our main result now follows.
Theorem B Let X be a smooth compact oriented 4-manifold with $2 \chi+3 \tau>0$. Assume, moreover, that $X$ has a non-trivial Seiberg-Witten invariant. Then $X \# k \overline{\mathbb{C P}}_{2}$ does not admit an Einstein metric if $k \geq \frac{25}{57}(2 \chi+3 \tau)(X)$.

Proof. For any Einstein metric $g$ on $M$, equation (1) and Theorem A tell us that
$$(2 \chi+3 \tau)(M)=\frac{1}{4 \pi^{2}} \int_{M}\left(2\left|W_{+}\right|^{2}+\frac{s^{2}}{24}\right) d \mu>\frac{32}{57}\left(c_{1}^{+}\right)^{2}$$
for any $\operatorname{spin}^{c}$ structure with $n_{c}(M, H) \neq 0$, where $H=\mathcal{H}_{g}^{+}$. But Lemma 1 now asserts that $M=X \# k \overline{\mathbb{C P}}_{2}$ has such a spin ${ }^{c}$ structure with $\left(c_{1}^{+}\right)^{2} \geq$ $(2 \chi+3 \tau)(X)$. Thus
$$(2 \chi+3 \tau)(X)-k=(2 \chi+3 \tau)(M)>\frac{32}{57}(2 \chi+3 \tau)(X),$$
and hence
$$k<\frac{25}{57}(2 \chi+3 \tau)(X),$$
assuming that $M$ admits an Einstein metric. The result therefore follows by contraposition. \(\square\)

Corollary 3 Let $X$ be a minimal complex surface of general type, and let $M=$ $X \# k \overline{\mathbb{C P}}_{2}$ be obtained from $X$ by blowing up $k$ points. If $k \geq \frac{25}{57} c_{1}^{2}(X)$, then $M$ does not admit Einstein metrics.

One might instead ask whether $M=X \# k \overline{\mathbb{C P}}_{2}$ admits anti-self-dual Einstein metrics, since Taubes' theorem [26] tells us that anti-self-dual (but non-Einstein) metrics exist when $k$ is very large. Using Corollary 2 instead of Theorem A, Lemma 1 implies a slightly better estimate by essentially the same argument:

Proposition 1 Let X be a smooth compact oriented 4-manifold with $2 \chi+3 \tau>$ 0 and a non-trivial Seiberg-Witten invariant. Then $X \# k \overline{\mathbb{C P}}_{2}$ cannot admit anti-self-dual Einstein metrics if $k \geq \frac{11}{27}(2 \chi+3 \tau)(X)$.

\section*{4 Examples}

We will now examine some specific new examples of 4-manifolds without Einstein metrics given to us by Corollary 3.

Let us begin by considering a non-singular complex hypersurface $X_{\ell}$ of degree $\ell>4$ in $\mathbb{C P}_{3}$. This minimal complex surface of general type has $c_{1}^{2}=\ell(\ell-4)^{2}$ and $p_{g}=\binom{\ell-1}{3}$. If we blow up $X_{\ell}$ at at $k \geq \frac{25}{57} \ell(\ell-4)^{2}$ points, the result is a complex surface $M=X_{\ell} \# k \overline{\mathbb{C P}}_{2}$ which is not diffeomorphic to any Einstein manifold. In particular, $X_{9} \# 117 \overline{\mathbb{C P}}_{2}$ does not admit Einstein metrics. But this complex surface has $c_{1}^{2}=108$ and $p_{g}=56$, exactly like the the double-branched cover of $\mathbb{C P}_{1} \times \mathbb{C P}_{1}$ ramified over a curve of bidegree (6, 58). This so-called Horikawa surface [11], like $X_{9} \# 117 \overline{\mathbb{C P}}_{2}$, is simply connected, and both surfaces have $\tau=c_{1}^{2}-8\left(1+p_{g}\right)=-348 \not \equiv 0 \bmod 16$, so Freedman's classification theorem [7] tells us that both are homeomorphic to
$$113 \mathbb{C P}_{2} \# 461 \overline{\mathbb{C P}}_{2} .$$
Our Horikawa surface, however, has ample canonical line bundle, and so admits a Kähler-Einstein metric by the Aubin/Yau theorem [2, 31]. Thus, while $X_{9} \# 117 \overline{\mathbb{C P}}_{2}$ does not admit Einstein metrics, it is nonetheless homeomorphic to an Einstein manifold. Similar examples may be obtained by blowing up the hypersurface $X_{\ell}$ for any $\ell \geq 9$. The reader might wish to compare this with the results of [13], where the above class of examples was observed to be beyond the capabilities of the weaker non-existence result of [21].

One may construct more delicate examples by blowing up branched double covers $Y_{m}$ of $\mathbb{C P}_{2}$, with ramification locus a smooth curve of degree $2 m, m>$ 4. These are surfaces of general type with $c_{1}^{2}=2(m-3)^{2}$, and Corollary 3 yields new examples of 4-manifolds without Einstein metrics by considering their blow-ups. In particular, $Y_{27} \# 506 \overline{\mathbb{C P}}_{2}$, does not admit Einstein metrics, since $506>\frac{25}{57} 2 \cdot 24^{2}$. However, this simply connected complex surface has $c_{1}^{2}=646$ and $p_{g}=325$, and it follows that it is homeomorphic to a Horikawa surface [11] - e.g. the double branched cover of $\mathbb{C P}_{2} \# \overline{\mathbb{C P}}_{2}$, ramified over the proper transform of a curve of degree 330 in $\mathbb{C P}_{2}$ which is non-singular except
for 324 self-crossings at the blown up point. In the same way, one can show that for all $m \geq 27$, the double planes $Y_{m}$ have blow-ups which are homeomorphic to Einstein manifolds, but do not themselves admit Einstein metrics.

\section*{5 Minimality and Minimal Volumes}

Let us now turn to a discussion of minimal volume problems [9, 5, 21]. Given a compact smooth 4-manifold $M$, let $\mathcal{M}_{|r|}(M)$ and $\mathcal{M}_{s}(M)$ respectively denote the set of metrics on $M$ for which $3 g \geq r \geq-3 g$ and $s \geq-12$. Then we may define minimal volume invariants
$$\begin{aligned}
\operatorname{Vol}_{|r|}(M) & :=\inf _{g \in \mathcal{M}_{|r|}} \int_{M} d \mu_{g} \\
\operatorname{Vol}_{s}(M) & :=\inf _{g \in \mathcal{M}_{s}} \int_{M} d \mu_{g}
\end{aligned}$$
and our conventions have been chosen so that $\operatorname{Vol}_{|r|}(M) \geq \operatorname{Vol}_{s}(M)$ tautologically. If $M$ is a complex surface of general type and $X$ is its minimal model, it was observed in [21] that
$$\operatorname{Vol}_{s}(M)=\operatorname{Vol}_{s}(X)=\operatorname{Vol}_{|r|}(X)=\frac{2}{9} \pi^{2} c_{1}^{2}(X) .$$
If $M$ is non-minimal, however, we will now see that $\operatorname{Vol}_{|r|}(M)>\operatorname{Vol}_{s}(M)$.
Lemma 2 Let $(M, H)$ be a polarized smooth compact oriented 4-manifold, and let $c$ be a spin ${ }^{c}$ structure on $M$. Assume, moreover, that $c_{1}^{+} \neq 0$ and that the Seiberg-Witten invariant $n_{c}(M, H)$ is non-zero. Then every $H$-adapted Riemannian metric $g$ on $M$ satisfies
$$\frac{1}{8 \pi^{2}} \int_{M}\left|r_{g}\right|^{2} d \mu \geq \frac{8}{5}\left(c_{1}^{+}\right)^{2}-\frac{3}{5}(2 \chi+3 \tau)(M)$$
with equality iff the metric is Kähler-Einstein.

Proof. The Gauss-Bonnet formula (1) tells us that
$$\begin{aligned}
\frac{1}{8 \pi^{2}} \int_{M}|r|^{2} d \mu & =\frac{1}{8 \pi^{2}} \int_{M}\left(\frac{s^{2}}{4}+|\stackrel{\circ}{r}|^{2}\right) d \mu \\
& =\frac{1}{\pi^{2}} \int_{M}\left(\frac{s^{2}}{24}+\frac{1}{2}\left|W_{+}\right|^{2}\right) d \mu-(2 \chi+3 \tau)(M)
\end{aligned}$$
On the other hand, the same formula tells us that
$$\frac{1}{4 \pi^{2}} \int_{M}\left(\frac{s^{2}}{24}+2\left|W_{+}\right|^{2}\right) d \mu \geq(2 \chi+3 \tau)(M),$$
with equality iff the metric is Einstein. Meanwhile, Corollary 1 asserts that
$$\frac{1}{4 \pi^{2}} \int_{M}\left(\frac{s_{g}^{2}}{24}+\frac{1}{3}\left|W_{+}\right|_{g}^{2}\right) d \mu_{g} \geq \frac{4}{9}\left(c_{1}^{+}\right)^{2}$$
with equality iff the metric is constant-scalar-curvature Kähler. Taking a convex combination of these inequalities, we therefore have
$$\begin{aligned}
\frac{1}{4 \pi^{2}} \int_{M}\left(\frac{s_{g}^{2}}{24}+\frac{1}{2}\left|W_{+}\right|_{g}^{2}\right) d \mu_{g} & \geq \frac{9}{10} \cdot \frac{4}{9}\left(c_{1}^{+}\right)^{2}+\frac{1}{10}(2 \chi+3 \tau)(M) \\
& =\frac{2}{5}\left(c_{1}^{+}\right)^{2}+\frac{1}{10}(2 \chi+3 \tau)(M)
\end{aligned}$$
Hence
$$\begin{aligned}
\frac{1}{8 \pi^{2}} \int_{M}\left|r_{g}\right|^{2} d \mu_{g} & \geq \frac{8}{5}\left(c_{1}^{+}\right)^{2}+\frac{2}{5}(2 \chi+3 \tau)(M)-(2 \chi+3 \tau)(M) \\
& =\frac{8}{5}\left(c_{1}^{+}\right)^{2}-\frac{3}{5}(2 \chi+3 \tau)(M)
\end{aligned}$$
and, as claimed, equality holds precisely in the Kähler-Einstein case. \(\square\)

Now if $X$ is a minimal complex surface of general type, and if $M=X \# k \overline{\mathbb{C P}}_{2}$ is one of its blow-ups, Lemmata 1 and 2 assert that every metric on $M$ satisfies
$$\begin{aligned}
\frac{1}{8 \pi^{2}} \int_{M}\left|r_{g}\right|^{2} d \mu_{g} & \geq \frac{8}{5} c_{1}^{2}(X)-\frac{3}{5}\left[c_{1}^{2}(X)-k\right] \\
& =c_{1}^{2}(X)+\frac{3}{5} k
\end{aligned}$$
Since any metric with $-3 g \leq r \leq 3 g$ satisfies $|r|^{2} \leq 36$, this shows that every $g \in \mathcal{M}_{|r|}(M)$ has total volume
$$\begin{aligned}
\int_{M} d \mu_{g} & \geq \frac{8 \pi^{2}}{36}\left[c_{1}^{2}(X)+\frac{3}{5} k\right] \\
& =\frac{2}{9} \pi^{2} c_{1}^{2}(X)+\frac{2}{15} \pi^{2} k
\end{aligned}$$
so that
$$\begin{aligned}
\operatorname{Vol}_{|r|}(M) & \geq \frac{2}{9} \pi^{2} c_{1}^{2}(X)+\frac{2}{15} \pi^{2} k \\
& =\operatorname{Vol}_{s}(M)+\frac{2}{15} \pi^{2} k
\end{aligned}$$
This proves
Theorem 2 Let $X$ be a complex surface of general type. Then
$$\operatorname{Vol}_{|r|}(M)=\operatorname{Vol}_{s}(M) \Longleftrightarrow M \text { is minimal. }$$

The reader should note that, while Lemma 2 provides an effective means of proving Theorem 2, the relevant estimate is actually quite weak in practice. For instance, an argument parallel to the proof of Theorem A shows that
$$\frac{1}{4 \pi^{2}} \int_{M}\left(\frac{s_{g}^{2}}{24}+\frac{1}{2}\left|W_{+}\right|_{g}^{2}\right) d \mu_{g}>\frac{16}{33}\left(c_{1}^{+}\right)^{2}$$
whenever the Seiberg-Witten invariant is non-zero. On a non-minimal surface $M=X \# k \overline{\mathbb{C P}}_{2}$ of general type, every metric therefore satisfies
$$\frac{1}{8 \pi^{2}} \int_{M}|r|_{g}^{2} d \mu_{g}>\frac{31}{33} c_{1}^{2}(X)+k$$
so that
$$\operatorname{Vol}_{|r|}(M) \geq \frac{31}{33} \operatorname{Vol}_{s}(M)+\frac{2}{9} \pi^{2} k,$$
and this, of course, is a stronger estimate for all but the smallest values of $k$. On the other hand, there is every reason to expect that the actual value of $\operatorname{Vol}_{|r|}(M)$ might in fact be considerably larger than indicated by either of these estimates; after all, the definition of $\operatorname{Vol}_{|r|}(M)$ essentially involves the $C^{0}$ norm, rather than its $L^{2}$ norm, of $r$.

In light of the above discussion, it is natural to introduce some new smooth invariants of a smooth oriented 4-manifold $M$. For any real parameter $\varepsilon \geq 0$, let us set
$$\mathcal{I}_{\varepsilon}(M):=\inf _{g} \frac{1}{4 \pi^{2}} \int_{M}\left(\frac{s_{g}^{2}}{24}+\varepsilon\left|W_{+}\right|_{g}^{2}\right) d \mu_{g}$$
Thus, for example, the above discussion of $\operatorname{Vol}_{|r|}$ hinged on estimating $\mathcal{I}_{\frac{1}{2}}(M)$. On the other hand, $96 \pi^{2} \mathcal{I}_{0}(M)=[\min (Y(M), 0)]^{2}$, where $Y(M)$ is the Yamabe invariant (sigma constant) of $M$. When $\varepsilon$ is small, Corollary 1 actually allows us to compute this invariant exactly for most complex surfaces:

Theorem 3 Let $(M, J)$ be a complex surface of Kodaira dimension $\geq 0$, and let $(X, \tilde{J})$ be its minimal model. Then
$$\mathcal{I}_{\varepsilon}(M)=\frac{1+\varepsilon}{3}(2 \chi+3 \tau)(X)$$
for any $\varepsilon \in\left[0, \frac{1}{3}\right]$.
Proof. If $M$ has Kodaira dimension 0 or 1, it collapses [22] with $s$ and $\left|W_{+}\right|$ bounded, and hence $\mathcal{I}_{\varepsilon}(M)=0$ for all $\varepsilon \geq 0$. Since $(2 \chi+3 \tau)(X)=c_{1}^{2}(X)=0$ in this case, the result is established in Kodaira dimensions 0 and 1.

If, on the other hand, $M$ is a surface of general type, we can proceed as in [21], constructing metrics on $M$ by gluing gravitational instantons and Burns metrics onto a Kähler-Einstein orbifold, while changing the $L^{2}$-norms of $s$ and $W_{+}$as little as we like. In this way, we see that
$$\mathcal{I}_{\varepsilon}(M) \leq \frac{1+\varepsilon}{3} c_{1}^{2}(X)=\frac{1+\varepsilon}{3}(2 \chi+3 \tau)(X) \quad \forall \varepsilon \geq 0 .$$

Yet Corollary 1 and Lemma 1 tell us that any metric on $M$ satisfies
$$\frac{1}{4 \pi^{2}} \int_{M}\left(\frac{s_{g}^{2}}{24}+\frac{1}{3}\left|W_{+}\right|_{g}^{2}\right) d \mu_{g} \geq \frac{4}{9} c_{1}^{2}(X)$$
establishing the opposite inequalities when $\varepsilon=1 / 3$. However, the inequality
$$\frac{1}{4 \pi^{2}} \int_{M} \frac{s_{g}^{2}}{24} d \mu_{g} \geq \frac{1}{3} c_{1}^{2}(X)$$
was already proved in [21]. Taking convex combinations, we therefore have
$$\mathcal{I}_{\varepsilon}(M) \geq \frac{1+\varepsilon}{3} c_{1}^{2}(X)$$
for all $\varepsilon \in\left[0, \frac{1}{3}\right]$, and the result follows. \(\square\)

When the Kodaira dimension is zero, one can still read off $\mathcal{I}_{\varepsilon}$ for most complex surfaces. Indeed, if $M$ is the underlying 4-manifold of a ruled surface of genus $\geq 2$, then [18, 12] one can find scalar-flat anti-self-dual metrics on $M$, so that $\mathcal{I}_{\varepsilon}(M)=0$. If the base has genus 1, $M$ is diffeomorphic to an elliptic surface, so that it collapses with bounded $s$ and $W_{+}$as in [22], and hence has $\mathcal{I}_{\varepsilon}=0$. The same argument applies to the rational elliptic surface $\mathbb{C P}_{2} \# 9 \overline{\mathbb{C P}}_{2}$ and all of its blow-ups.

Now the above discussion covers all complex algebraic surfaces except for the rational surfaces with $2 \chi+3 \tau>0$. On the other hand, equation (1) implies that
$$\mathcal{I}_{\varepsilon}(M) \geq \min \left(1, \frac{\varepsilon}{2}\right)(2 \chi+3 \tau)(M)$$
We therefore have the following result:
Proposition 2 Let $\left(M^{4}, J\right)$ be a complex algebraic surface, and let $\varepsilon$ be any positive constant. Then $\mathcal{I}_{\varepsilon}(M)>0$ iff
\begin{itemize}
\item[-] $(M, J)$ is of general type; or
\item[-] $(M, J)$ is a deformation of a del Pezzo surface.
\end{itemize}

Acknowledgment. This work grew out of calculations carried out while the author was a visiting scholar at Harvard University. He would therefore like to thank the members of the Harvard Mathematics Department, and especially Cliff Taubes, for their hospitality during his stay.

\section*{References}
\begin{itemize}
\item[] [1] T. Aubin, Inégalités Concernant la Première Valeur Propre Non Nulle du Laplacien pour Certaines Variétés Riemanniennes, C. R. Acad. Sci. Paris 281 (1975) A979-A982.
\item[] [2] T. Aubin, Equations du Type Monge-Ampère sur les Variétés Kählériennes Compactes, C. R. Acad. Sci. Paris 283A (1976) 119-121.
\item[] [3] A. Besse, Einstein Manifolds, Springer-Verlag, 1987.
\item[] [4] G. Besson, G. Courtois, and S. Gallot, Volume et Entropie Minimale des Espaces Localement Symétriques, Invent. Math. 103 (1991) 417-445.
\item[] [5] G. Besson, G. Courtois, and S. Gallot, Entropies et Rigidités des Espaces Localement Symétriques de Courbure Strictement Négative, Geom. and Func. An. 5 (1995) 731-799.
\item[] [6] J.P. Bourguignon, Les Variétés de Dimension 4 à Signature Non Nulle dont la Courbure Est Harmonique Sont d'Einstein, Invent. Math. 63 (1981) 263-286.
\item[] [7] M. Freedman, On the Topology of 4-Manifolds, J. Diff. Geom. 17 (1982) 357-454.
\item[] [8] R. Fintushel and R. Stern, Immersed Spheres in 4-Manifolds and the Immersed Thom Conjecture, Turk. J. Math. 19 (1995) 145-157.
\item[] [9] M. Gromov, Volume and Bounded Cohomology, Publ. IHES 56 (1982) 5-99.
\item[] [10] N. Hitchin, Compact Four-Dimensional Einstein Manifolds, J. Diff. Geom. 9 (1974) 435-441.
\item[] [11] E. Horikawa, Algebraic Surfaces of General Type with Small $c_{1}^{2}$, I, Ann. Math. 104 (1976) 357-387.
\item[] [12] J.-S. Kim and M. Pontecorvo, A New Method of Constructing Scalar-Flat Kähler Surfaces, J. Differential Geom. 41 (1995) 449-477.
\item[] [13] D. Kotschick, Einstein Metrics and Smooth Structures, Geom. Topol. 2 (1998) 1-10.
\item[] [14] P. Kronheimer and T. Mrowka, The Genus of Embedded Surfaces in the Complex Projective Plane, Math. Res. Lett. 1 (1994) 797-808.
\item[] [15] P. Kronheimer, Minimal Genus in $S^{1} \times M^{3}$, Harvard preprint, 1997.
\item[] [16] J. Lafontaine, Remarques sur les Variétés Conformément Plates, Math. Ann. 259 (1982) 313-319.
\end{itemize}
\begin{itemize}
\item[] [17] C. LeBrun, On the Topology of Self-Dual 4-Manifolds, Proc. Am. Math. Soc. 98 (1986) 637-640.
\item[] [18] C. LeBrun, Scalar-Flat Kähler Metrics on Blown-Up Ruled Surfaces, J. reine angew. Math. 420 (1991) 161-177.
\item[] [19] C. LeBrun, Einstein Metrics and Mostow Rigidity, Math. Res. Lett. 2 (1995) 1-8.
\item[] [20] C. LeBrun, Polarized 4-Manifolds, Extremal Kähler Metrics, and Seiberg-Witten Theory, Math. Res. Lett. 2 (1995) 653-662.
\item[] [21] C. LeBrun, Four-Manifolds without Einstein Metrics, Math. Res. Lett. 3 (1996) 133-147.
\item[] [22] C. LeBrun, Kodaira Dimension and the Yamabe Problem, dg-ga archive e-print 9702012; to appear in Comm. An. Geom..
\item[] [23] J. Lee and T. Parker, The Yamabe Problem, Bull. Am. Math. Soc. 17 (1987) 37-91.
\item[] [24] A. Sambusetti, An Obstruction to the Existence of Einstein Metrics on 4-Manifolds, C. R. Acad. Sci. Paris 322 (1996) 1213-1218.
\item[] [25] R. Schoen, Conformal Deformation of a Riemannian Metric to Constant Scalar Curvature, J. Diff. Geom. 20 (1984) 479-495.
\item[] [26] C.H. Taubes, The Existence of Anti-Self-Dual Conformal Structures, J. Diff. Geom. 36 (1992) 163-253.
\item[] [27] C.H. Taubes, The Seiberg-Witten Invariants and Symplectic Forms, Math. Res. Lett. 1 (1994) 809-822.
\item[] [28] C.H. Taubes, The Seiberg-Witten and Gromov Invariants, Math. Res. Lett. 2 (1995) 221-238.
\item[] [29] J. Thorpe, Some Remarks on the Gauss-Bonnet Integral, J. Math. Mech. 18 (1969) 779-786.
\item[] [30] E. Witten, Monopoles and Four-Manifolds, Math. Res. Lett. 1 (1994) 809-822.
\item[] [31] S.-T. Yau, On the Ricci-Curvature of a Complex Kähler Manifold and the Complex Monge-Ampère Equations, Comment. Pure Appl. Math. 31 (1978) 339-411.
\end{itemize}
