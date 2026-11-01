---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 1908_01881.pdf
converter: mathpix
format: mmd
---

\title{
Einstein Manifolds, Self-Dual Weyl Curvature, and Conformally Kähler Geometry
}

\author{
Claude LeBrun* \\ Stony Brook University
}

\begin{abstract}
Peng Wu [22] recently announced a beautiful characterization of conformally Kähler, Einstein metrics of positive scalar curvature on compact oriented 4-manifolds via the condition $\operatorname{det}\left(W^{+}\right)>0$. In this note, we buttress his claim by providing an entirely different proof of his result. We then present further consequences of our method, which builds on techniques previously developed in [16].
\end{abstract}

\section*{1 Introduction}

Recall that a Riemannian metric $h$ is said to be Einstein if it has constant Ricci curvature. This is equivalent to saying that it solves the Einstein equation
$$r=\lambda h,$$
where $r$ is the Ricci tensor of $h$, and where the real constant $\lambda$ (which is not specified in advance) is called the Einstein constant of $h$. Given a smooth compact manifold $M$, it is a fundamental problem of modern Riemannian geometry to completely understand the moduli space
$$\mathscr{E}(M)=\{\text { Solutions of }(1)\} /\left(\operatorname{Diff}(M) \times \mathbb{R}^{\times}\right),$$
of Einstein metrics on $M$, where the diffeomorphism group $\operatorname{Diff}(M)$ of course acts on solutions of (1) via pull-backs, while the group of positive reals $\mathbb{R}^{+}$ acts on solutions by constant rescalings. One key goal of this paper is to study this problem for a specific class of 4-manifolds $M$.

Our focus on dimension four reflects the degree to which this dimension seems to represent a sort of "Goldilocks zone" for the Einstein equation (1).

\footnotetext{
*Supported in part by NSF grant DMS-1906267 and a Simons Fellowship.
}

In lower dimensions, Einstein metrics necessarily have constant sectional curvature, making them locally boring - albeit still globally interesting. In higher dimensions, on the other hand, Einstein metrics turn out to exist in surprising profusion, leading to wildly disconnected Einstein moduli spaces on even the most familiar manifolds [5, 6, 21]. But, by contrast, dimension four seems "just right" for (1), because four-dimensional Einstein metrics display such a remarkably well-balanced combination of local flexibility and global rigidity that their geometry often seems to be optimally adapted to the manifold where they reside. For example, if $M^{4}$ is a compact quotient of real or complex-hyperbolic space, or a 4-torus, or $K 3$, then the Einstein moduli space $\mathscr{E}(M)$ is actually explicitly known, and in each case actually turns out to be connected [2, 4, 10, 12].

Unfortunately, however, there are very few other 4-manifolds $M$ whose Einstein moduli spaces $\mathscr{E}(M)$ are both non-empty and completely understood. In particular, we still only partially understand the Einstein moduli spaces of the smooth compact 4-manifolds that arise as del Pezzo surfaces. Recall that a compact complex 2 -manifold $\left(M^{4}, J\right)$ is called a del Pezzo surface iff it has ample anti-canonical line bundle. Up to diffeomorphism, there are exactly ten such manifolds, namely $S^{2} \times S^{2}$ and the nine connected sums $\mathbb{C P}_{2} \# m \overline{\mathbb{C P}}_{2}, m=0,1, \ldots, 8$. These are exactly [7] the oriented smooth compact 4-manifolds that admit both an Einstein metric with $\lambda>0$ and an orientation-compatible symplectic structure. However, on any of these spaces, every known Einstein metric is conformally Kähler. In most cases, these currently-known Einstein metrics are actually Kähler-Einstein [17, 20], but in exactly two cases they are instead constructed [7, 15] as nontrivial conformal rescalings of extremal Kähler metrics. This situation has prompted the author to elsewhere characterize the known Einstein metrics on del Pezzo surfaces by means of two different non-Kähler criteria. First, they are [14] the only $\lambda>0$ Einstein metrics on compact 4-manifolds that are Hermitian with respect to an integrable complex structure. Perhaps more compellingly, they are also the only Einstein metrics on compact oriented 4-manifolds for which the self-dual Weyl curvature $W^{+}$is everywhere positive in the direction of a global self-dual harmonic 2-form 16]. Because the latter characterization merely depends on the Einstein metric belonging to an explicit open set in the space of Riemannian metrics, it in particular allows one to prove that, on any del Pezzo $M^{4}$, the known Einstein metrics exactly sweep out a single connected component in the Einstein moduli space $\mathscr{E}(M)$.

Still, both of these previous characterizations suffer from the defect of not being formulated in terms of a purely local condition on the curvature
tensor. It is for this reason that a new characterization recently announced by Peng Wu [22], formulated purely in terms of a property of the self-dual Weyl curvature, represents an important advance in the subject.

To explain Wu's criterion, let us first recall that the bundle $\Lambda^{2}$ of 2-forms over an oriented Riemannian 4-manifold $(M, h)$ naturally decomposes, in a conformally invariant way, as a direct sum
$$\Lambda^{2}=\Lambda^{+} \oplus \Lambda^{-}$$
of the $( \pm 1)$-eigenspaces $\Lambda^{ \pm}$of the Hodge star operator. Here, sections of $\Lambda^{+}$are called self-dual 2-forms, while sections of $\Lambda^{-}$are called anti-self-dual 2-forms. But since the Riemann curvature tensor may be identified with a self-adjoint linear map
$$\mathcal{R}: \Lambda^{2} \rightarrow \Lambda^{2}$$
it can therefore be decomposed into irreducible pieces
$$\mathcal{R}=\left(\begin{array}{c|c}
W^{+}+\frac{s}{12} I & \stackrel{\circ}{r} \\
\hline \stackrel{\circ}{r} & W^{-}+\frac{s}{12} I
\end{array}\right)$$
where $s$ is the scalar curvature, $\stackrel{\circ}{r}=r-\frac{s}{4} g$ is the trace-free Ricci curvature, and where $W^{ \pm}$are the trace-free pieces of the appropriate blocks. The corresponding pieces $W^{ \pm a}{ }_{b c d}$ of the Riemann curvature tensor are both conformally invariant, and are respectively called the self-dual and anti-self-dual Weyl curvature tensors.

Wu observes that the self-dual Weyl curvature $W^{+}: \Lambda^{+} \rightarrow \Lambda^{+}$of any conformally Kähler, Einstein metric on any del Pezzo surface satisfies $\operatorname{det}\left(W^{+}\right)>0$. He then offers a rather terse and cryptic proof that the converse is also true. One main purpose of this article is to provide an entirely different proof of Wu's beautiful result:

Theorem A. Let $(M, h)$ be a simply-connected compact oriented Einstein 4-manifold, and suppose that its self-dual Weyl curvature $W^{+}: \Lambda^{+} \rightarrow \Lambda^{+}$ satisfies $\operatorname{det}\left(W^{+}\right)>0$ at every point of $M$. Then $h$ is conformal to an orientation-compatible extremal Kähler metric $g$ on $M$.

With [13] and [16], this now immediately implies the following:

Corollary. Any simply-connected compact oriented Einstein 4-manifold with $\operatorname{det}\left(W^{+}\right)>0$ is orientedly diffeomorphic to a del Pezzo surface. Conversely, the underlying smooth oriented 4-manifold $M$ of any del Pezzo surface carries Einstein metrics $h$ with $\operatorname{det}\left(W^{+}\right)>0$, and these sweep out exactly one connected component of the moduli space $\mathscr{E}(M)$ of Einstein metrics on $M$.

Note that the simple-connectivity hypothesis is essential in Theorem A. Otherwise, a counter-example would be given by $\left(S^{2} \times S^{2}\right) / \mathbb{Z}_{2}$, obtained by dividing the Riemannian product of two round, unit-radius 2-spheres by the simultaneous action of the antipodal map on both factors. However, Proposition 2.3 below shows that this example is typical, in the following sense: for a compact oriented Einstein manifold with $\operatorname{det}\left(W^{+}\right)>0$, the only possible fundamental groups are \{1\} and \{±1\}. Thus, one can always reduce to the simply-connected case by at worst passing to a double cover.

While the method of proof used here is quite different from Wu's, both approaches are deeply indebted to the pioneering work of Derdziński [8]. In fact, the method developed here also naturally yields results about more general 4-manifolds with harmonic self-dual Weyl curvature:

Theorem B. Let $(M, h)$ be a compact oriented Riemannian 4-manifold whose self-dual Weyl curvature $W^{+}$is harmonic, in the sense that
$$\delta W^{+}:=-\nabla \cdot W^{+}=0 .$$
Suppose moreover that $b_{+}(M) \neq 0$, and that $h$ satisfies $\operatorname{det}\left(W^{+}\right)>0$ at every point of $M$. Then $M$ admits an orientation-compatible Kähler metric $g$ of scalar curvature $s>0$ such that $h=s^{-2} g$.

Conversely, if $\left(M^{4}, g, J\right)$ is a Kähler surface of scalar curvature $s>0$, Derdziński discovered that $h=s^{-2} g$ then satisfies both $\delta W^{+}=0$ and $\operatorname{det}\left(W^{+}\right)>0$. This makes it completely straightforward to classify the smooth compact oriented 4-manifolds that carry metrics $h$ of the type covered by Theorem B. Indeed, if a compact complex surface $(M, J)$ admits Kähler metrics $g$ with $s>0$, it is necessarily rational or ruled [23], and, conversely, any rational or ruled surface has arbitrarily small deformations that admit such metrics [11, 19]. Up to oriented diffeomorphism, the complete list of the 4-manifolds $M$ that admit such metrics $h$ therefore exactly consists of $\mathbb{C P}_{2},\left(\Sigma^{2} \times S^{2}\right) \# k \overline{\mathbb{C P}}_{2}$, and $\Sigma^{2} \varkappa S^{2}$, where $\Sigma$ is any compact orientable 2 -manifold, $k$ is any non-negative integer, and $\Sigma^{2} \varkappa S^{2}$ is the non-trivial oriented 2-sphere bundle over $\Sigma$. Notice, however, that the moduli space of such metrics on any of these manifolds is always infinite-dimensional, in marked contrast to the Einstein case.

We should also point out that dropping the $b_{+}(M) \neq 0$ hypothesis in Theorem B only changes the story very slightly. Indeed, as is shown in Proposition 2.2 below, any compact oriented $\left(M^{4}, h\right)$ with $\delta W^{+}=0$, $\operatorname{det}\left(W^{+}\right)>0$, and $b_{+}(M)=0$ has a double-cover $\hat{M} \rightarrow M$ with $b_{+}(\hat{M})=1$. Theorem B therefore applies to the pull-back of $h$ to this double cover.

These results are all proved in §2 below. Finally, in §3, we then prove a generalization that does not explicitly require $\operatorname{det}\left(W^{+}\right)$to be positive:

Theorem C. Let $(M, h)$ be a compact oriented Riemannian 4-manifold that satisfies $\delta W^{+}=0$. If
$$W^{+} \neq 0 \quad \text { and } \quad \operatorname{det}\left(W^{+}\right) \geq-\frac{5 \sqrt{2}}{21 \sqrt{21}}\left|W^{+}\right|^{3}$$
everywhere on $M$, then actually $\operatorname{det}\left(W^{+}\right)>0$. Thus, after at worst passing to a double cover $\hat{M} \rightarrow M, h$ becomes conformally Kähler, in the manner described by Theorem B. In particular, if $(M, h)$ is a simply-connected Einstein manifold, it actually falls under the purview of Theorem A.

\section*{2 The Proofs of Theorems A and B}

Let $(M, h)$ be a compact oriented Riemannian 4-manifold with $\operatorname{det}\left(W^{+}\right)>0$ everywhere. Since $W^{+}: \Lambda^{+} \rightarrow \Lambda^{+}$is self-adjoint, we can diagonalize $W^{+}$ at any point of $M$ as
$$W^{+}=\left[\begin{array}{lll}
\alpha & & \\
& \beta & \\
& & \gamma
\end{array}\right],$$
by choosing a suitable orthonormal basis for $\Lambda^{+}$; and, after re-ordering our basis if necessary, we may arrange that $\alpha \geq \beta \geq \gamma$ at our given point. However, by its very definition, the self-dual Weyl curvature $W^{+}: \Lambda^{+} \rightarrow \Lambda^{+}$ automatically satisfies $\operatorname{trace}\left(W^{+}\right)=0$, and this of course means that
$$\alpha+\beta+\gamma=0 .$$
It thus follows that $\alpha>0$ and $\gamma<0$ as long as $W^{+} \neq 0$ at the point in question. We therefore immediately see that $\operatorname{det} W^{+}=\alpha \beta \gamma$ always has the same sign as minus the middle eigenvalue $\beta$. Consequently, our assumption that $\operatorname{det} W^{+}>0$ is equivalent to saying that exactly one of the eigenvalues, namely $\alpha$, is positive at each point, while both the other two are negative. In particular, the positive eigenvalue $\alpha$ always has multiplicity one, so that
$\alpha: M \rightarrow \mathbb{R}$ is always the unique positive solution of the characteristic equation $\operatorname{det}\left(W^{+}-\alpha I\right)=0$, and so is a smooth positive function on $M$. Since the $\alpha$-eigenspace of $W^{+}$is exactly the kernel of $\left(W^{+}-\alpha I\right): \Lambda^{+} \rightarrow \Lambda^{+}$, this eigenspace moreover varies smoothly from point to point. Thus, our assumption that $\operatorname{det} W^{+}>0$ implies that the unique positive eigenspace of $W^{+}$defines a smooth real line sub-bundle $L \subset \Lambda^{+}$. Up to bundle isomorphism, it follows that $L$ is intrinsically classified by
$$w_{1}(L) \in H^{1}\left(M, \mathbb{Z}_{2}\right)=\operatorname{Hom}\left(\pi_{1}(M), \mathbb{Z}_{2}\right),$$
and so will necessarily be trivial if $M$ is simply-connected - or, indeed, if $\pi_{1}(M)$ merely does not contain a subgroup of index 2 .

Since the condition $\operatorname{det}\left(W^{+}\right)>0$ is conformally invariant, the above discussion similarly applies to any metric $g=f^{-2} h$ arising by conformal rescaling $h$, using a smooth positive function $f: M \rightarrow \mathbb{R}^{+}$. On the other hand, the endomorphism $W^{+}: \Lambda^{+} \rightarrow \Lambda^{+}$is explicitly given by
$$\varphi_{a b} \longmapsto\left[W^{+}(\varphi)\right]_{c d}:=\frac{1}{2} W^{+a b}{ }_{c d} \varphi_{a b},$$
so constructing it out of the conformal-weight-zero tensor field $W^{+a}{ }_{b c d}$ involves raising an index. Thus, replacing $h$ with $g=f^{-2} h$ rescales the top eigenvalue by a factor of $f^{2}$ :
$$\alpha_{g}=f^{2} \alpha_{h} .$$
We will henceforth impose the interesting choice
$$f=\alpha_{h}^{-1 / 3}$$
of the conformal factor $f$, because this then has the nice property that
$$\alpha_{g}=f^{2} \alpha_{h}=\alpha_{h}^{1 / 3}=f^{-1} .$$
It then follows that $\alpha:=\alpha_{g}$ satisfies
$$\alpha f \equiv 1$$
for this preferred conformal rescaling $g=f^{-2} h$ of the original metric.
With respect to this conformally altered metric $g$, there exist, at each point, exactly two self-dual 2-forms $\omega$ which satisfy
$$W_{g}^{+}(\omega)=\alpha_{g} \omega, \quad|\omega|_{g}^{2}=2 .$$

Since these both belong to the real line bundle $L \subset \Lambda^{+}$, and differ by sign, we can find a global self-dual 2-form $\omega$ on $M$ satisfying these requirements everywhere if and only if $L$ is trivial, which happens precisely in the case where $w_{1}(L)=0$. On the other hand, if this class is non-zero, we can then just pass to the double cover $\varpi: \hat{M} \rightarrow M$ given by the elements of norm $\sqrt{2}$ in $L$, and we then instead obtain a tautological global self-dual 2-form on $\hat{M}$ satisfying (4) with respect to the pulled-back metric $\hat{g}=\varpi^{*} g$. In this case, notice that the connected Riemannian manifold $(\hat{M}, \hat{g})$ admits an isometric involution $\sigma: \hat{M} \rightarrow \hat{M}$ induced by scalar multiplication by -1 in $L$, and that this involution satisfies $\sigma^{*} \omega=-\omega$ by construction.

Our stipulation that $|\omega|_{g}^{2}=2$ has been imposed so that $\omega$ can be put in the point-wise normal form
$$\omega=e^{1} \wedge e^{2}+e^{3} \wedge e^{4}$$
by choosing an appropriate oriented orthonormal frame at any given point. Thus, whether on $M$ or on $\hat{M}$, our global 2-form $\omega$ will give rise to a unique orientation-compatible almost-complex structure $J$ defined by
$$\omega=g(J \cdot, \cdot) .$$
In other words, the tensor-field $J$ explicitly obtained from $\omega$ by index-raising
$$J_{a}{ }^{b}=\omega_{a c} g^{c b}$$
with respect to $g$ will then automatically satisfy
$$J_{a}^{b} J_{b}^{c}=-\delta_{a}^{c},$$
thus making it a $g$-compatible almost-complex structure on $M$ or $\hat{M}$.
Our main argument will hinge on a few simple facts about self-dual 2-forms and the Weyl curvature, starting with the following:

Lemma 1. Let $(M, h)$ be an oriented Riemannian 4-manifold for which $\operatorname{det}\left(W^{+}\right)>0$ everywhere. Also suppose that the top eigenspace $L \subset \Lambda^{+}$of $W^{+}$is trivial as a real line bundle $L \rightarrow M$. Let $g=f^{-2} h$ be some conformal rescaling of $h$, and let $\omega$ then be a self-dual 2-form on $M$ that satisfies (4) everywhere. Then
$$W^{+}\left(\nabla^{a} \omega, \nabla_{a} \omega\right) \leq 0,$$
everywhere, where all terms are to be computed with respect to $g$.
Proof. The covariant derivative $\nabla \omega$ of $\omega$ belongs to $\Lambda^{1} \otimes \omega^{\perp} \subset \Lambda^{1} \otimes \Lambda^{+}$ because $\omega$ has constant norm with respect to $g$. The result therefore follows from the fact that $W^{+}(\phi, \phi) \leq 0$ for any $\phi \in \omega^{\perp} \subset \Lambda^{+}$. \(\square\)

Secondly, we will need the following standard algebraic observation:
Lemma 2. At any point $p$ of an oriented 4-manfold $(M, g)$,
$$\left|W^{+}\right|^{2} \geq \frac{3}{2} \alpha^{2}$$
where $\alpha=\alpha_{g}$ is the the top eigenvalue of $W_{g}^{+}$at $p$.
Proof. Because trace $W^{+}=0$,
$$\left|W^{+}\right|^{2}=\alpha^{2}+\beta^{2}+(-\alpha-\beta)^{2}=\frac{3}{2} \alpha^{2}+2\left(\beta+\frac{1}{2} \alpha\right)^{2} \geq \frac{3}{2} \alpha^{2}$$
where $\beta$ is the middle eigenvalue of $W_{g}^{+}$at $p$. \(\square\)

Finally, we remind the reader of the Weitzenböck formula
$$\left(d+d^{*}\right)^{2} \omega=\nabla^{*} \nabla \omega-2 W^{+}(\omega)+\frac{s}{3} \omega$$
for the Hodge Laplacian on self-dual 2-forms.
We are now finally ready to see what all this means when $h$ is an Einstein metric. But our discussion will actually pertain to the much larger class of oriented 4-manifolds $(M, h)$ which have harmonic self-dual Weyl curvature, in the sense that
$$\delta W^{+}:=-\nabla \cdot W^{+}=0 .$$
When $h$ is Einstein, (8) holds as a consequence of the second Bianchi identity; but the reader should keep in mind that (8) is actually much weaker than the Einstein condition. The reason (8) will be so useful for our purposes is that it displays a weighted conformal invariance [18] under conformal changes of metric. Namely, if $h$ satisfies $\delta W^{+}=0$, then any conformal rescaling $g=f^{-2} h$ will instead have the property that $\delta\left(f W^{+}\right)=0$. This then implies the useful Weitzenböck formula
$$0=\nabla^{*} \nabla\left(f W^{+}\right)+\frac{s}{2} f W^{+}-6 f W^{+} \circ W^{+}+2 f\left|W^{+}\right|^{2} I$$
for $f W^{+}$with respect to $g$. For other applications of this fact, see [8, 9, 16].
Theorem 2.1. Let $(M, h)$ be a compact oriented Riemannian manifold with $\delta W^{+}=0$ and $\operatorname{det}\left(W^{+}\right)>0$. Also suppose that the positive eigenspace $L \subset \Lambda^{+}$of $W^{+}$is trivial as a real line bundle $L \rightarrow M$. Then the conformally rescaled metric $g=f^{-2} h$ defined by (2) is an orientation-compatible Kähler metric on $M$.

Proof. Since $L \rightarrow M$ is trivial, we can choose a global self-dual 2-form $\omega$ on $M$ which satisfies (4) at every point. Always working henceforth with respect to $g$, we now take the inner product of (9) with $\omega \otimes \omega$, and then integrate on $M$. Integrating by parts, and using (3), (5), (6), and (7), we then have
$$\begin{aligned}
0 & =\int_{M}\left\langle\left(\nabla^{*} \nabla f W^{+}+\frac{s}{2} f W^{+}-6 f W^{+} \circ W^{+}+2 f\left|W^{+}\right|^{2} I\right), \omega \otimes \omega\right\rangle d \mu_{g} \\
& =\int_{M}\left[\left\langle W^{+}, \nabla^{*} \nabla(\omega \otimes \omega)\right\rangle+\frac{s}{2} W^{+}(\omega, \omega)-6\left|W^{+}(\omega)\right|^{2}+2\left|W^{+}\right|^{2}|\omega|^{2}\right] f d \mu_{g} \\
& =\int_{M}\left[-2 W^{+}\left(\nabla_{e} \omega, \nabla^{e} \omega\right)-2 W^{+}\left(\omega, \nabla^{e} \nabla_{e} \omega\right)\right. \\
& \left.\quad+\frac{s}{2} \alpha|\omega|^{2}-6 \alpha^{2}|\omega|^{2}+2\left|W^{+}\right|^{2}|\omega|^{2}\right] f d \mu_{g} \\
& \geq \int_{M}\left[-2 \alpha\left\langle\omega, \nabla^{e} \nabla_{e} \omega\right\rangle+\frac{s}{2} \alpha|\omega|^{2}-6 \alpha^{2}|\omega|^{2}+3 \alpha^{2}|\omega|^{2}\right] f d \mu_{g} \\
& =\int_{M}\left[2\left\langle\omega, \nabla^{*} \nabla \omega\right\rangle+\frac{s}{2}|\omega|^{2}-3 \alpha|\omega|^{2}\right](\alpha f) d \mu_{g} \\
& =\int_{M}\left[\frac{1}{2}\left\langle\omega, \nabla^{*} \nabla \omega\right\rangle+\frac{3}{2}\left\langle\omega, \nabla^{*} \nabla \omega\right\rangle+\frac{s}{2}|\omega|^{2}-3 W^{+}(\omega, \omega)\right] d \mu_{g} \\
& =\frac{1}{2} \int_{M}|\nabla \omega|^{2} d \mu_{g}+\frac{3}{2} \int_{M}\left\langle\omega, \nabla^{*} \nabla \omega-2 W^{+}(\omega)+\frac{s}{3} \omega\right\rangle d \mu_{g} \\
& =\frac{1}{2} \int_{M}|\nabla \omega|^{2} d \mu_{g}+\frac{3}{2} \int_{M}\left\langle\omega,\left(d+d^{*}\right)^{2} \omega\right\rangle d \mu_{g} \\
& =\frac{1}{2} \int_{M}|\nabla \omega|^{2} d \mu+3 \int_{M}|d \omega|^{2} d \mu \\
& \geq \frac{1}{2} \int_{M}|\nabla \omega|^{2} d \mu
\end{aligned}$$
This shows that $\nabla \omega \equiv 0$ with respect to our rescaled metric $g$. Since it of course also follows that $\nabla J \equiv 0$, we now see that $(M, g, J)$ is actually a Kähler manifold, with Kähler form $\omega$. In particular, this shows that the initial metric $h=f^{2} g$ is conformally Kähler. \(\square\)

On the other hand, because the curvature tensor of a Kähler surface $\left(M^{4}, g, J\right)$ belongs to $\odot^{2} \Lambda^{1,1}$, the fact that
$$\Lambda^{+}=\mathbb{R} \omega \oplus \Re e \Lambda^{2,0}$$
for $(M, g)$ implies that that its self-dual Weyl curvature takes the form
$$W^{+}=\left[\begin{array}{ccc}
s / 6 & & \\
& -s / 12 & \\
& & -s / 12
\end{array}\right]$$
in an orthonormal basis adapted to (10). In particular, $\operatorname{det}\left(W^{+}\right)=s^{3} / 3^{3} 2^{5}$, so a Kähler metric $g$ has $\operatorname{det}\left(W^{+}\right)>0$ if and only if its scalar curvature $s$ is positive. It follows that any Kähler metric conformal to a Riemannian metric $h$ with $\operatorname{det} W^{+}>0$ must necessarily have $s>0$. Moreover, we now see that the top eigenvalue $\alpha$ of $W^{+}$for any such metric $g$ is given by $s / 6$. Thus, when $h$ satisfies (8), we have succeeded in expressing it as $h=\alpha^{-2} g=36 s^{-2} g$ for a Kähler metric $g$ of positive scalar curvature $s$. However, when this happens, $\tilde{g}=6^{2 / 3} g$ is also a Kähler metric, and has scalar curvature $\tilde{s}=6^{-2 / 3} s$, and we therefore also have $h=\tilde{s}^{-2} \tilde{g}$ for a Kähler metric $\tilde{g}$ with positive scalar curvature $\tilde{s}$. This was the form preferred by Derdziński [3, 8], who discovered that, conversely, any Kähler surface ( $M^{4}, g, J$ ) of scalar curvature $s>0$ gives rise to a Riemannian metric $h$ on $M$ with $\delta W^{+}=0$ and $\operatorname{det} W^{+}>0$ via the ansatz $h=s^{-2} g$.

On the other hand, any compact Kähler surface $\left(M^{4}, g, J\right)$ of positive scalar curvature has geometric genus $h^{2,0}=0$ by an argument due to Yau [23]. But since $b_{+}(M)=1+2 h^{2,0}$ for any compact Kähler surface [1], this is equivalent to saying $b_{+}(M)=1$. Geometrically, this means that a self-dual 2-form on $(M, g)$ is harmonic if and only if it is a constant multiple of the Kähler form $\omega$. Of course, since the space of self-dual harmonic 2-forms is conformally invariant in dimension 4, we also see that the self-dual harmonic 2-forms on $(M, h)$ likewise consists of the constant multiples of $\omega$.

This now allows us to back-track a little, and finally deal with the case where the the real-line bundle $L \rightarrow M$ is non-trivial. In this setting, the conformal factor defined by (2) still defines a metric $g$ on $M$, but it is only when we pull it back to $\varpi: \hat{M} \rightarrow M$ that this rescaled metric can be associated with a global self-dual 2-form $\omega$ satisfying $W^{+}(\omega)=\alpha \omega$ and $|\omega|_{\varpi * g}=\sqrt{2}$. But now we can just apply Theorem 2.1 to $\left(\hat{M}, \varpi^{*} g\right)$, thereby showing that it is a Kähler manifold with Kähler form $\omega$ and positive scalar curvature. In particular, this implies that $b_{+}(\hat{M})=1$. Thus, any self-dual harmonic 2-form on $\left(\hat{M}, \varpi^{*} g\right)$ is a constant multiple of the Kähler form $\omega$. However, by construction, there is an involution $\sigma: \hat{M} \rightarrow \hat{M}$ with $\varpi \circ \sigma=\varpi$ and $\sigma^{*} \omega=-\omega$. It follows that $b_{+}(M)=0$, since a non-trivial self-dual harmonic form on $(M, g)$ would otherwise pull back to a $\sigma$-invariant self-dual harmonic form on $\left(\hat{M}, \varpi^{*} g\right)$; and this is impossible, because any
such form would also have to be a constant multiple of $\omega$, which is not $\sigma$-invariant. We have thus proved the following:

Proposition 2.2. Let $(M, h)$ be a compact oriented Riemannian 4-manifold with $\delta W^{+}=0$ and $\operatorname{det}\left(W^{+}\right)>0$. Then either
\begin{itemize}
\item[(i)] $b_{+}(M)=1$, and there is an orientation-compatible Kähler metric $g$ on $M$ of scalar curvature $s>0$, such that $h=s^{-2} g$; or else
\item[(ii)] $b_{+}(M)=0$, and there is a conformal rescaling $g$ of $h$ whose pull-back $\varpi^{*} g$ to a suitable double cover $\varpi: \hat{M} \rightarrow M$ is a positive-scalar curvature Kähler metric on $\hat{M}$ that is related to $\varpi^{*} h$ as in case (i).
\end{itemize}

Theorem B is now an immediate consequence of Proposition 2.2.
Notice that the conformally rescaled metric $g$ is globally well-defined on $M$ in both cases of Propostion 2.2: moreover, it has scalar curvature $s>0$, and may be renormalized so as to arrange that $h=s^{-2} g$. The distinction between the two cases is really a matter of holonomy; in the first case, the holonomy of $g$ is a subgroup of U(2), while in the second case it instead belongs to the larger group $\mathbf{U}(\mathbf{2}) \rtimes \mathbb{Z}_{2}$ of real-linear transformations of $\mathbb{C}^{2}$ generated by complex conjugation $\left(z^{1}, z^{2}\right) \mapsto\left(\bar{z}^{1}, \bar{z}^{2}\right)$ and the unitary transformations. Of course, the natural representation $\mathbf{U}(\mathbf{2}) \rtimes \mathbb{Z}_{2} \rightarrow \mathbb{Z}_{2}$ gives rise to a double cover $\hat{M} \rightarrow M$, and passing to this cover then simplifies matters by reducing to the case of U(2) holonomy.

Using [13] and the simple-connectivity of del Pezzos, we also now have:
Proposition 2.3. Let $(M, h)$ be a compact oriented Riemannian Einstein 4 -manifold with $\operatorname{det}\left(W^{+}\right)>0$. Then $(M, h)$ actually satisfies $\operatorname{det}\left(W^{+}\right)>0$ at every point. Moreover, either
\begin{itemize}
\item[(i)] $\pi_{1}(M)=0$, and $M$ admits an orientation-compatible complex structure $J$ that makes $(M, J)$ into a del Pezzo surface, and relative to which the Einstein metric $h$ becomes conformally Kähler; or else,
\item[(ii)] $\pi_{1}(M)=\mathbb{Z}_{2}$, and $M$ is doubly covered by a del Pezzo surface $(\hat{M}, J)$ of even signature on which the pull-back of the Einstein metric $h$ becomes conformally Kähler.
\end{itemize}

Theorem A now becomes an immediate corollary of Proposition 2.3.

\section*{3 The Proof of Theorem C}

The method used to prove Theorems A and B does not actually require $\operatorname{det} W^{+}$to be positive. Indeed, in this section, we will obtain essentially
the same results under the weaker assumption that the top and middle eigenvalues $\alpha$ and $\beta$ of $W^{+}$satisfy
$$4 \beta \leq \alpha \neq 0$$
everywhere. The following lemma will allow us to restate this hypothesis as an effective condition on $\operatorname{det}\left(W^{+}\right)$.

Lemma 3. Let $(M, h)$ be an oriented Riemannian 4-manifold, and let $p \in M$ be a point where $W^{+} \neq 0$. Let $\alpha$ and $\beta$ once again denote the highest and middle eigenvalues of $W^{+}$at $p$. Then
$$\beta \leq \frac{\alpha}{4} \Longleftrightarrow \operatorname{det}\left(W^{+}\right) \geq-\frac{5}{21} \sqrt{\frac{2}{21}}\left|W^{+}\right|^{3} .$$
Moreover, both of these equivalent statements are conformally invariant, in the sense that if either holds at $p$ for the metric $h$, then both necessarily hold at $p$ for every metric $g$ which is a conformal rescaling of $h$.

Proof. Let $x=\beta / \alpha$, and then notice that, because $\alpha \geq \beta \geq-\alpha-\beta$, we automatically have $x \in\left[-\frac{1}{2}, 1\right]$. Now set $y=1+x+x^{2}$, and notice that $x \mapsto y$ defines an increasing smooth map $\left[-\frac{1}{2}, 1\right] \rightarrow\left[\frac{3}{4}, 3\right]$ because $\frac{d y}{d x}=1+2 x$ is non-negative for $x \geq-\frac{1}{2}$. But this now makes it apparent that
$$\begin{aligned}
\frac{\operatorname{det} W^{+}}{\left|W^{+}\right|^{3}} & =\frac{\alpha \beta(-\alpha-\beta)}{\left(\alpha^{2}+\beta^{2}+(-\alpha-\beta)^{2}\right)^{3 / 2}} \\
& =-\frac{x+x^{2}}{2^{3 / 2}\left(1+x+x^{2}\right)^{3 / 2}} \\
& =-2^{-3 / 2}\left(y^{-1 / 2}-y^{-3 / 2}\right)
\end{aligned}$$
is a decreasing function of $x \in\left[-\frac{1}{2}, 1\right]$, since
$$\begin{aligned}
\frac{d}{d y}\left[-2^{-3 / 2}\left(y^{-1 / 2}-y^{-3 / 2}\right)\right] & =-2^{-3 / 2}\left(-\frac{1}{2} y^{-3 / 2}+\frac{3}{2} y^{-5 / 2}\right) \\
& =-(2 y)^{-5 / 2}(3-y)
\end{aligned}$$
is non-positive for $y \in\left[\frac{3}{4}, 3\right]$. As a consequence,
$$\frac{\beta}{\alpha} \leq \frac{1}{4} \Longleftrightarrow \frac{\operatorname{det} W^{+}}{\left|W^{+}\right|^{3}} \geq-\left.\frac{x+x^{2}}{2^{3 / 2}\left(1+x+x^{2}\right)^{3 / 2}}\right|_{x=\frac{1}{4}}=-\frac{5 \sqrt{2}}{21 \sqrt{21}} .$$
Moreover, since both $\operatorname{det}\left(W^{+}\right) /\left|W^{+}\right|^{3}$ and $x=\beta / \alpha$ are manifestly unaltered by conformal changes of the metric, the equivalence in question is obviously conformally invariant. \(\square\)

Most of the ideas we used in 82 merely depend on the assumption that the top eigenvalue $\alpha$ of $W^{+}$has multiplicity one everywhere. However, the key inequality (5) is quite different, and strongly depends on the assumption that $\operatorname{det}\left(W^{+}\right)>0$. Nonetheless, we can generalize this inequality as follows:

Lemma 4. Let $(M, h)$ be an oriented Riemannian 4-manifold on which the top eigenvalue $\alpha_{h}$ of $W_{h}^{+}$has multiplicity one everywhere, and so defines a smooth function $\alpha_{h}$ on $M$. Also suppose that the top eigenspace $L \subset \Lambda^{+}$of $W^{+}$is trivial as real line bundle $L \rightarrow M$. Let $g=f^{-2} h$ be some conformal rescaling of $h$, and let $\omega$ then be a self-dual 2 -form on $M$ that satisfies (4) everywhere. Let $\beta=\beta_{g}: M \rightarrow \mathbb{R}$ be the continuous function given by the middle eigenvalue of $W_{g}^{+}$at each point of $M$. Then
$$W^{+}\left(\nabla_{e} \omega, \nabla^{e} \omega\right) \leq \beta|\nabla \omega|^{2}$$
everywhere, where all terms are to be computed with respect to $g$.
Proof. The covariant derivative $\nabla \omega$ of $\omega$ belongs to $\Lambda^{1} \otimes \omega^{\perp} \subset \Lambda^{1} \otimes \Lambda^{+}$ because $\omega$ has constant norm with respect to $g$. The result therefore follows from the fact that $W^{+}(\phi, \phi) \leq \beta|\phi|^{2}$ for any $\phi \in \omega^{\perp}$. \(\square\)

With these lemmata in hand, a return visit to our previously-explored territory immediately reveals the following:

Theorem 3.1. Let $(M, h)$ be a compact oriented Riemannian manifold with $\delta W^{+}=0$. Assume that $W^{+} \neq 0$ everywhere, and that
$$\operatorname{det}\left(W^{+}\right) \geq-\frac{5}{21} \sqrt{\frac{2}{21}}\left|W^{+}\right|^{3}$$
at every point. Noting that this in particular implies that the top eigenvalue $\alpha_{h}: M \rightarrow \mathbb{R}^{+}$of $W_{h}^{+}$defines a smooth positive function on $M$, let us also now suppose that the real line bundle $L \rightarrow M$ given by the $\alpha_{h}$-eigenspace of $W_{h}^{+}$is trivial. Then the conformally rescaled metric
$$g=\alpha_{h}^{2 / 3} h$$
is an orientation-compatible Kähler metric of positive scalar curvature.
Proof. Let $\omega$ be a self-dual 2-form that satisfies (4) at every point of $M$ with respect to the rescaled metric $g$. Here we have once again arranged that $g=f^{-2} h$ has the property that $\alpha:=\alpha_{g}$ satisfies
$$\alpha f \equiv 1,$$
as in (3), by choosing $f$ according to (2). Now Lemma 3 tells us that our hypotheses imply that $\beta \leq \alpha / 4$, while Lemma 4 provides us with a crucial inequality (11) involving $\beta$. On the other hand, (6) and (7) are completely general facts about 4-dimensional geometry that in particular apply to our current situation. Assembling these pieces, we therefore have
$$\begin{aligned}
0 & =\int_{M}\left\langle\left(\nabla^{*} \nabla f W^{+}+\frac{s}{2} f W^{+}-6 f W^{+} \circ W^{+}+2 f\left|W^{+}\right|^{2} I\right), \omega \otimes \omega\right\rangle d \mu_{g} \\
& =\int_{M}\left[\left\langle W^{+}, \nabla^{*} \nabla(\omega \otimes \omega)\right\rangle+\frac{s}{2} W^{+}(\omega, \omega)-6\left|W^{+}(\omega)\right|^{2}+2\left|W^{+}\right|^{2}|\omega|^{2}\right] f d \mu_{g} \\
& =\int_{M}\left[-2 W^{+}\left(\nabla_{e} \omega, \nabla^{e} \omega\right)-2 W^{+}\left(\omega, \nabla^{e} \nabla_{e} \omega\right)\right. \\
& \left.\quad+\frac{s}{2} \alpha|\omega|^{2}-6 \alpha^{2}|\omega|^{2}+2\left|W^{+}\right|^{2}|\omega|^{2}\right] f d \mu_{g} \\
& \geq \int_{M}\left[-2 \beta|\nabla \omega|^{2}-2 \alpha\left\langle\omega, \nabla^{e} \nabla_{e} \omega\right\rangle+\frac{s}{2} \alpha|\omega|^{2}-6 \alpha^{2}|\omega|^{2}+3 \alpha^{2}|\omega|^{2}\right] f d \mu_{g} \\
& \geq \int_{M}\left[-\frac{\alpha}{2}|\nabla \omega|^{2}-2 \alpha\left\langle\omega, \nabla^{e} \nabla_{e} \omega\right\rangle+\frac{s}{2} \alpha|\omega|^{2}-3 \alpha^{2}|\omega|^{2}\right] f d \mu_{g} \\
& =\int_{M}\left[-\frac{1}{2}|\nabla \omega|^{2}+2\left\langle\omega, \nabla^{*} \nabla \omega\right\rangle+\frac{s}{2}|\omega|^{2}-3 \alpha|\omega|^{2}\right](\alpha f) d \mu_{g} \\
& =\int_{M}\left[\frac{3}{2}\left\langle\omega, \nabla^{*} \nabla \omega\right\rangle+\frac{s}{2}|\omega|^{2}-3 W^{+}(\omega, \omega)\right] d \mu_{g} \\
& =\frac{3}{2} \int_{M}\left\langle\omega, \nabla^{*} \nabla \omega-2 W^{+}(\omega)+\frac{s}{3} \omega\right\rangle d \mu_{g} \\
& =\frac{3}{2} \int_{M}\left\langle\omega,\left(d+d^{*}\right)^{2} \omega\right\rangle d \mu_{g} \\
& =3 \int_{M}|d \omega|^{2} d \mu
\end{aligned}$$
so the self-dual 2-form $\omega$ must actually be closed, and hence harmonic. However, since $\omega$ also has constant norm $\sqrt{2}$, this means that $\left(M^{4}, g, \omega\right)$ is an almost-Kähler manifold. But, by construction, $W^{+}(\omega, \omega)>0$ and $h=f^{2} g$ satisfies $\delta\left(W^{+}\right)=0$. Thus, by [16, Proposition 2], our almost-Kähler manifold is actually Kähler, and has positive scalar curvature. \(\square\)

However, a Kähler surface $(M, g, J)$ of positive scalar curvature necessarily satisfies $\operatorname{det}\left(W^{+}\right)>0$ at every point. Moreover, a result of Yau [23] guarantees that any such $(M, g, J)$ must have vanishing geometric genus, and so enjoys the topological property that $b_{+}(M)=1$. Applying Theorem 3.1 either to $M$ or to the double cover $\hat{M} \rightarrow M$ associated with the real line
bundle $L$, the same argument used to prove Proposition 2.2 now yields the following:

Proposition 3.2. Let $(M, h)$ be a compact oriented Riemannian 4-manifold with $\delta W^{+}=0$ that also satisfies
$$\operatorname{det}\left(W^{+}\right) \geq-\frac{5}{21} \sqrt{\frac{2}{21}}\left|W^{+}\right|^{3}$$
at every point. Then actually $\operatorname{det}\left(W^{+}\right)>0$ everywhere, and either
\begin{itemize}
\item[(i)] $b_{+}(M)=1$, and there is an orientation-compatible Kähler metric $g$ on $M$ of scalar curvature $s>0$, such that $h=s^{-2} g$; or else
\item[(ii)] $b_{+}(M)=0$, and there is a conformal rescaling $g$ of $h$ whose pull-back $\varpi^{*} g$ to a suitable double cover $\varpi: \hat{M} \rightarrow M$ is a positive-scalar curvature Kähler metric on $\hat{M}$ that is related to $\varpi^{*} h$ as in case (i).
\end{itemize}

Similarly, the same reasoning used to prove Proposition 2.3 now yields:
Proposition 3.3. Let $(M, h)$ be a compact oriented Einstein 4-manifold that also satisfies
$$\operatorname{det}\left(W^{+}\right) \geq-\frac{5}{21} \sqrt{\frac{2}{21}}\left|W^{+}\right|^{3}$$
at every point. Then $(M, h)$ satisfies $\operatorname{det}\left(W^{+}\right)>0$ everywhere, and either
\begin{itemize}
\item[(i)] $\pi_{1}(M)=0$, and $M$ admits an orientation-compatible complex structure $J$ that makes $(M, J)$ into a del Pezzo surface, and relative to which the Einstein metric $h$ becomes conformally Kähler; or else,
\item[(ii)] $\pi_{1}(M)=\mathbb{Z}_{2}$, and $M$ is doubly covered by a del Pezzo surface $(\hat{M}, J)$ of even signature on which the pull-back of the Einstein metric $h$ becomes conformally Kähler.
\end{itemize}

Theorem C is now an immediate corollary of these last Propositions.
Acknowledgments. The author would like to thank Peng Wu for bringing Theorem A to his attention. This work was carried out while the author was on sabbatical as a Simons Fellow in Mathematics, and was also supported in part by NSF grant DMS-1906267.

\section*{References}
\begin{itemize}
\item[] [1] W. Barth, C. Peters, and A. Van de Ven, Compact Complex Surfaces, vol. 4 of Ergebnisse der Mathematik und ihrer Grenzgebiete (3), Springer-Verlag, Berlin, 1984.
\item[] [2] M. Berger, Sur les variétés d'Einstein compactes, in Comptes Rendus de la IIIe Réunion du Groupement des Mathématiciens d'Expression Latine (Namur, 1965), Librairie Universitaire, Louvain, 1966, pp. 35-55.
\item[] [3] A. L. Besse, Einstein Manifolds, vol. 10 of Ergebnisse der Mathematik und ihrer Grenzgebiete (3), Springer-Verlag, Berlin, 1987.
\item[] [4] G. Besson, G. Courtois, and S. Gallot, Entropies et rigidités des espaces localement symétriques de courbure strictement négative, Geom. and Func. An., 5 (1995), pp. 731-799.
\item[] [5] С. Вӧнм, Inhomogeneous Einstein metrics on low-dimensional spheres and other low-dimensional spaces, Invent. Math., 134 (1998), pp. 145-176.
\item[] [6] C. P. Boyer, K. Galicki, and J. Kollár, Einstein metrics on spheres, Ann. of Math. (2), 162 (2005), pp. 557-580.
\item[] [7] X. X. Chen, C. LeBrun, and B. Weber, On conformally Kähler, Einstein manifolds, J. Amer. Math. Soc., 21 (2008), pp. 1137-1168.
\item[] [8] A. Derdziński, Self-dual Kähler manifolds and Einstein manifolds of dimension four, Compositio Math., 49 (1983), pp. 405-433.
\item[] [9] M. J. Gursky, Four-manifolds with $\delta W^{+}=0$ and Einstein constants of the sphere, Math. Ann., 318 (2000), pp. 417-431.
\item[] [10] N. J. Hitchin, Compact four-dimensional Einstein manifolds, J. Differential Geometry, 9 (1974), pp. 435-441.
\item[] [11] -, On the curvature of rational surfaces, in Differential geometry (Proc. Sympos. Pure Math., Vol. XXVII, Part 2, Stanford Univ., Stanford, Calif., 1973), Amer. Math. Soc., Providence, R. I., 1975, pp. 65-80.
\item[] [12] C. LeBrun, Einstein metrics and Mostow rigidity, Math. Res. Lett., 2 (1995), pp. 1-8.
\end{itemize}
\begin{itemize}
\item[] [13] $\_\_\_\_$, Einstein metrics on complex surfaces, in Geometry and Physics (Aarhus, 1995), vol. 184 of Lecture Notes in Pure and Appl. Math., Dekker, New York, 1997, pp. 167-176.
\item[] [14] $\_\_\_\_$, On Einstein, Hermitian 4-manifolds, J. Differential Geom., 90 (2012), pp. 277-302.
\item[] [15] $\_\_\_\_$, Einstein manifolds and extremal Kähler metrics, J. Reine Angew. Math., 678 (2013), pp. 69-94.
\item[] [16] $\_\_\_\_$, Einstein metrics, harmonic forms, and symplectic fourmanifolds, Ann. Global Anal. Geom., 48 (2015), pp. 75-85.
\item[] [17] Y. Odaka, C. Spotti, and S. Sun, Compact moduli spaces of del Pezzo surfaces and Kähler-Einstein metrics, J. Differential Geom., 102 (2016), pp. 127-172.
\item[] [18] R. Penrose and W. Rindler, Spinors and space-time. Vol. 2, Cambridge University Press, Cambridge, 1986. Spinor and twistor methods in space-time geometry.
\item[] [19] M.-H. Sung, Kähler surfaces of positive scalar curvature, Ann. Global Anal. Geom., 15 (1997), pp. 509-518.
\item[] [20] G. Tian, On Calabi's conjecture for complex surfaces with positive first Chern class, Invent. Math., 101 (1990), pp. 101-172.
\item[] [21] M. Y. Wang and W. Ziller, Einstein metrics on principal torus bundles, J. Differential Geom., 31 (1990), pp. 215-248.
\item[] [22] P. Wu, Einstein four-manifolds of nonnegative determinant half Weyl curvature. e-print arXiv:1903.11818 [math.DG].
\item[] [23] S. T. Yau, On the curvature of compact Hermitian manifolds, Invent. Math., 25 (1974), pp. 213-239.
\end{itemize}

Department of Mathematics, Stony Brook University (SUNY), Stony Brook, NY 11794-3651 USA
e-mail: claude@math.sunyb.edu
Keywords: Einstein metric, Del Pezzo surface, Weyl curvature, Kähler, conformal, self-dual.

MSC classification: 53C25 (Primary), 14J26, 32J15, 53C55.