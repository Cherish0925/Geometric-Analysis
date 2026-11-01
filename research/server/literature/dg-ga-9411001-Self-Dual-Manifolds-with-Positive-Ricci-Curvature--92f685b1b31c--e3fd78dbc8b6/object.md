# [dg-ga/9411001] Self-Dual Manifolds with Positive Ricci Curvature

- Category: papers
- Identity: arxiv:dg-ga/9411001
- Content status: fulltext_ok

---

---
source_file: dg-ga_9411001.pdf
converter: mathpix
format: mmd
---

\title{
Self-Dual Manifolds with Positive Ricci Curvature
}

\author{
Claude LeBrun* \\ Department of Mathematics \\ State University of New York \\ Stony Brook, NY 11794, USA \\ Shin Nayatani \\ Max-Planck-Institut für Mathematik \\ Gottfried-Claren-Straße 26 \\ D-53225 Bonn, Germany and \\ Mathematical Institute \\ Tôhoku University \\ Sendai 980, Japan \\ Takashi Nitta \\ Department of Mathematics \\ Mie University \\ Tsu 514, Japan
}

\begin{abstract}
We prove that the connected sums $\mathbf{C P}_{2} \# \mathbf{C P}_{2}$ and $\mathbf{C P}_{2} \# \mathbf{C P}_{2} \# \mathbf{C P}_{2}$ admit self-dual metrics with positive Ricci curvature. Moreover, every self-dual metric of positive scalar curvature on $\mathbf{C P}_{2} \# \mathbf{C P}_{2}$ is conformal to a metric with positive Ricci curvature.
\end{abstract}

\footnotetext{
*Supported in part by NSF grant DMS-9204093
}

\section*{Introduction.}

An oriented Riemannian 4 -manifold $(M, g)$ is said to be self-dual if its Weyl curvature $W$, thought of as a bundle-valued 2-form, satisfies $W=\star W$, where ★ denotes the Hodge star operator. Because both $W$ and ★ are unchanged if the metric is multiplied by a positive function, this property is conformally invariant, and the term self-dual is thus often used to describe the conformal class $[g]:=\left\{u g \mid u: M \xrightarrow{C^{\infty}} \mathbf{R}^{+}\right\}$rather than the metric $g$ which represents it.

Two familiar examples of compact self-dual manifolds are provided by the symmetric spaces $S^{4}=S O(5) / S O(4)$ and $\mathbf{C P}_{2}=S U(3) / U(2)$. For many years, these were the only known examples of compact simply-connected self-dual manifolds with positive scalar curvature, and it was therefore a major breakthrough when Poon [15] constructed a one-parameter family of positive-scalar-curvature self-dual metrics on $\mathbf{C P}_{2} \# \mathbf{C P}_{2}$; here the connected sum operation \# is carried out by deleting balls from the given manifolds and then identifying the resulting boundaries in a manner compatible with the given orientations. Motivated by this discovery, Donaldson-Friedman [6] and Floer [7] abstractly proved the existence of self-dual metrics on the $n$-fold connected sum
$$n \mathbf{C P}_{2}:=\underbrace{\mathbf{C P}_{2} \# \cdots \# \mathbf{C P}_{2}}_{n}$$
for every $n$. The first author [12] then realized that such metrics on $n \mathbf{C P}_{2}$ can be constructed explicitly by means of the so-called "hyperbolic ansatz" reviewed below in §2. This last method has the added advantage that each of the conformal classes so constructed can be seen to contain a representative of positive scalar curvature.

On the other hand, the examples provided by $S^{4}$ and $\mathbf{C P}_{2}$ actually have positive Ricci curvature, and, in light of the work of Cheeger [4], Anderson [1] and Sha-Yang [16], it is natural to ask whether there are other compact 4-manifolds which admit selfdual metrics with this property. Our objective here is to show that the answer to this question is yes. We will accomplish this (§4) by explicitly constructing such metrics on $n \mathbf{C P}_{2}$ when $n=2$ and 3; moreover, it will turn out that each of Poon's conformal classes on $2 \mathbf{C P}_{2}$ contains such a metric. On the other hand, it is rather easy (§1) to see that a compact self-dual manifold with positive Ricci curvature must be homeomorphic to $n \mathbf{C P}_{2}$ for some $n \geq 0$, where by convention $0 \mathbf{C P}_{2}:=S^{4}$. This raises the fascinating question, left unanswered here, of whether $n \mathbf{C P}_{2}$ admits such metrics when $n \geq 4$.

On a related front, Gauduchon [8] has studied self-dual manifolds with non-negative Ricci operator (cf. §1), and asked whether $2 \mathbf{C P}_{2}$ and $3 \mathbf{C P}_{2}$ admit such metrics. Our metrics on $2 \mathbf{C P}_{2}$ will be seen to satisfy both this condition and another, which we call strongly positive Ricci curvature.

In order to prove these positivity results, we will first (§2) need to compute the Ricci curvature of the general self-dual metric of hyperbolic-ansatz type. Our results will then follow once we have introduced a suitable choice of conformal gauge, motivated (§3) by a re-examination of the Fubini-Study metric of $\mathbf{C P}_{2}$.

Acknowledgements. The present article grew out of a series of conversations at the Mathematical Sciences Research Institute and the Mathematics Department of UC Berkeley; we are thus greatly indebted to these institutions for their hospitality and financial support. The first and second author would also like to respectively thank the Erwin Schrödinger Institute (Vienna) and the Max-Planck-Institut für Mathematik (Bonn) for their financial support and hospitality. Finally, the third author would like to thank Prof. S. Kobayashi for sponsoring his visit to Berkeley.

\section*{1 Topological Preliminaries}

The present article is largely motivated by the following easy observation:
Proposition 1.1 Let $(M, g)$ be a compact self-dual 4-manifold with positive Ricci curvature. Then $M$ is homeomorphic to $n \mathbf{C P}_{2}$ for some $n \geq 0$. Moreover, $M$ is diffeomorphic to $n \mathbf{C P}_{2}$ if $n \leq 4$.

Proof. Let the universal cover $\widetilde{M}$ of $M$ be equipped with the pull-back metric. Since the Ricci curvature of $\widetilde{M}$ is then bounded below by a positive constant, Myers' theorem tells us that $\widetilde{M}$ is compact, and $\widetilde{M} \rightarrow M$ is therefore a finite-sheeted covering. However, a simple Bochner-Weitzenböck argument [3, 11] implies that a compact self-dual 4-manifold with positive scalar curvature must have $b_{-}=0$. Thus for both $M$ and $\widetilde{M}$, we have $b_{1}=b_{-}=0$, and hence both have $\chi-\tau=2\left(1-b_{1}+b_{-}\right)=2$, where $\chi$ is the Euler characteristic and $\tau$ is the signature. But $\chi-\tau$ is multiplicative under finite coverings because it can be computed from a Gauss-Bonnet formula. Hence $\widetilde{M} \rightarrow M$ is the trivial covering, and $M$ is simply connected. It now follows from the work of Donaldson [5] and Freedman that $M$ is homeomorphic to $n \mathbf{C P}_{2}$ for some $n \geq 0$. On the other hand, a self-dual manifold with positive scalar curvature, $b_{1}=0$, and $\tau \leq 4$ must [14] be diffeomorphic to $n \mathbf{C P}_{2}$ because its twistor space contains a rational hypersurface of degree 2. \(\square\)

It is now natural to ask whether, conversely, the manifolds $n \mathbf{C P}_{2}$ admit self-dual metrics with positive Ricci curvature. For small values of $n$ we shall see that the answer is in fact affirmative.

Rather than merely asking for the Ricci curvature Ric to be positive, one might ask for its trace-free part Ric ${ }_{0}$ to be small enough with respect to its scalar curvature $s>0$ so as to guarantee a priori that Ric > 0. This motivates the following definition:

Definition 1.1 Let $(M, g)$ be a Riemannian 4-manifold. Then we will say that $M$ has strongly positive Ricci curvature if, at each point of $M$, we have
$$\left|\operatorname{Ric}_{0}\right|<\frac{s}{2 \sqrt{3}} .$$
Similarly, we will say that $M$ has strongly non-negative Ricci curvature if $s>0$ and
$$\mid \text { Ric }_{0} \left\lvert\, \leq \frac{s}{2 \sqrt{3}}\right.$$
at every point of $M$.
Observe that strongly positive Ricci curvature implies positive Ricci curvature. Indeed, if $\left(\lambda_{1}, \ldots, \lambda_{4}\right)$ are the eigenvalues of Ric $/ s$, then, in the 3 -plane $\lambda_{1}+\cdots+\lambda_{4}=1$, positive Ricci curvature corresponds to the tetrahedron with corners $(1,0,0,0), \ldots,(0,0,0,1)$, whereas strongly positive Ricci curvature corresponds to the ball of radius $1 / 2 \sqrt{3}$ around $\left(\frac{1}{4}, \ldots, \frac{1}{4}\right)$, and this ball just fills the in-sphere of the tetrahedron. By the same argument, we also see that strongly non-negative Ricci curvature implies non-negative Ricci curvature.

Proposition 1.2 Let $(M, g)$ be a self-dual 4-manifold with strongly positive Ricci curvature. Then $M$ is diffeomorphic to $n \mathbf{C P}_{2}$, where $0 \leq n \leq 3$.

Proof. The Gauss-Bonnet formulae for the signature and Euler characteristic of a compact oriented Riemannian 4-manifold $(M, g)$ are
$$\tau(M)=\frac{1}{12 \pi^{2}} \int_{M}\left(\left|W_{+}\right|^{2}-\left|W_{-}\right|^{2}\right) v_{g}$$
and
$$\chi(M)=\frac{1}{8 \pi^{2}} \int_{M}\left(\left|W_{+}\right|^{2}+\left|W_{-}\right|^{2}-\frac{\left|\mathrm{Ric}_{0}\right|^{2}}{2}+\frac{s^{2}}{24}\right) v_{g},$$
where $v_{g}$ is the metric volume form. Thus any compact self-dual 4-manifold satisfies
$$(2 \chi-3 \tau)(M)=\frac{1}{8 \pi^{2}} \int_{M}\left(\frac{s^{2}}{12}-\left|\operatorname{Ric}_{0}\right|^{2}\right) v_{g},$$
and the right-hand side is manifestly positive if the Ricci curvature is strongly positive. Now $M$ is homeomorphic to $n \mathbf{C P}_{2}$ by Proposition 1.1, and even diffeomorphic if $n \leq 4$. But the inequality $2 \chi-3 \tau>0$ implies that $n<4$, as desired. \(\square\)

Rather than focusing on the Ricci tensor of a Riemannian 4-manifold $(M, g)$, one may instead choose [8] to consider an algebraically equivalent object Ric, called the Ricci operator, which is defined as the full curvature operator minus its Weyl component. If we let Q denote Schouten's modified Ricci tensor
$$\mathrm{Q}=\operatorname{Ric}-\frac{s}{6} g$$
the Ricci operator is explicitly given by
$$\operatorname{Ric}(X \wedge Y)=\frac{1}{2}\left(\mathrm{Q}^{\sharp}(X) \wedge Y+X \wedge \mathrm{Q}^{\sharp}(Y)\right),$$
where $\mathrm{Q}^{\sharp}$ is the endomorphism of $T M$ corresponding to Q and $X, Y$ are any tangent vectors. It follows that the Ricci operator is positive (respectively, non-negative) if and only if the sum of the lowest two eigenvalues of Q is positive (respectively, non-negative). In terms of $\lambda_{1}, \ldots, \lambda_{4}$, this corresponds to requiring that
$$\frac{2}{3}>(\text { resp. } \geq) \lambda_{i}+\lambda_{j}>(\text { resp. } \geq) \frac{1}{3} \quad \forall i \neq j$$
which is to say that $\left(\lambda_{1}, \cdots, \lambda_{4}\right)$ is a point of the open (respectively, closed) cube with corners $\left(\frac{1}{3}, \frac{1}{3}, \frac{1}{3}, 0\right), \ldots,\left(0, \frac{1}{3}, \frac{1}{3}, \frac{1}{3}\right),\left(\frac{1}{6}, \frac{1}{6}, \frac{1}{6}, \frac{1}{2}\right), \ldots,\left(\frac{1}{2}, \frac{1}{6}, \frac{1}{6}, \frac{1}{6}\right)$. Since this cube is contained in the in-sphere, we therefore have
positive Ricci operator ⇒
strongly positive Ricci curvature ⇒
positive Ricci curvature,
and
non-negative Ricci operator and $s>0 \Rightarrow$
strongly non-negative Ricci curvature ⇒
non-negative Ricci curvature.
Moreover, non-negative Ricci operator and $s>0$ fail to imply that the Ricci curvature is strongly positive only when $\left(\lambda_{1}, \ldots, \lambda_{4}\right)$ is a corner of the cube. Using this observation, we now prove a slightly sharpened version of a result discovered by Gauduchon [8], using different methods.

Theorem 1.3 Let $(M, g)$ be a compact self-dual 4-manifold with positive scalar curvature and non-negative Ricci operator. Then either $M$ is diffeomorphic to $n \mathbf{C P}_{2}$, $0 \leq n \leq 3$, or else the universal cover of ( $M, g$ ) is the Riemannian product $\mathbf{R} \times S^{3}$.

Proof. Since the Ricci curvature is strongly non-negative,
$$(2 \chi-3 \tau)(M)=\frac{1}{8 \pi^{2}} \int_{M}\left(\frac{s^{2}}{12}-\left|\operatorname{Ric}_{0}\right|^{2}\right) v_{g} \geq 0$$
with equality iff $\left|\operatorname{Ric}_{0}\right| \equiv s / 2 \sqrt{3}$. If the inequality is strict, $2 \chi-3 \tau>0$. Thus $b_{1}(M)=0$ and $\tau(M)<4$. The proof of Proposition 1.1 thus implies that $M \approx n \mathbf{C P}_{2}$ for $n<4$.

If equality holds, $\left(\lambda_{1}, \ldots, \lambda_{4}\right)$ must everywhere be one of the corners of the previously mentioned cube, and Ric therefore has exactly two eigenvalues at each point of $M$, one with multiplicity 3 and one with multiplicity 1. It follows that there is a line subbundle of $T M$, and $\chi(M)=0$. Moreover, $b_{+}(M)=\tau(M)=\frac{3}{2} \chi(M)=0$, so that $b_{2}(M)=b_{+}(M)=0$. Hence $0=\chi(M)=2-2 b_{1}(M)$, and $b_{1}(M)=1$. Since $M$ has nonnegative Ricci curvature, the classical Bochner argument [2] now says that $M$ admits a parallel 1-form, and thus locally splits as the Riemannian product of $\mathbf{R} \times N$, where $N$ is a 3-manifold. But since Ric everywhere has a positive eigenvalue of multiplicity 3, $N$ is an Einstein 3-manifold of positive scalar curvature. Thus $N$ has positive constant sectional curvature, and the universal cover of $M$ is $\mathbf{R} \times S^{3}$. \(\square\)

\section*{2 Ricci Curvature and the Hyperbolic Ansatz}

In this section, we shall compute the Ricci curvature of those self-dual metrics which arise from the following "hyperbolic ansatz" construction:

Proposition 2.1 [12] Let $\left(\mathcal{H}^{3}, h\right)$ denote hyperbolic 3-space, which we equip with a fixed orientation, and let $V$ be a positive harmonic function on some open set $\mathcal{V} \subset \mathcal{H}^{3}$. Suppose that the cohomology class of $\frac{1}{2 \pi} \star d V$ is integral, where ★ is the Hodge star operator of $\mathcal{H}^{3}$. Let $\mathcal{M} \rightarrow \mathcal{V}$ be a circle bundle with a connection 1-form $\theta$ whose curvature is $\star d V$. Then the conformal class
$$[g]=\left[V h+V^{-1} \theta^{2}\right]$$
of Riemannian metrics on $\mathcal{M}$ is self-dual with respect to the orientation determined by $\theta \wedge v_{h}$, where $v_{h}$ is the volume form of $\mathcal{H}^{3}$.

We now wish to calculate the Ricci curvature of metrics in these self-dual conformal classes. With the most obvious choice of conformal factor, the answer turns out to be surprisingly simple:

Proposition 2.2 For any positive harmonic function $V$ on a region of $\mathcal{H}^{3}$, the Ricci curvature of the self-dual metric $g=V h+V^{-1} \theta^{2}$ is $\operatorname{Ric}_{g}=-2 h$.

The $V$-independence of this Ricci curvature is analogous to the Ricci-flatness of the metrics produced via the Gibbons-Hawking ansatz [9].

While this answer is beguilingly simple, it is also depressingly negative! Fortunately, the picture will become less bleak once we conformally rescale our metric:

Proposition 2.3 Let $f$ and $V$ be respectively a smooth function and a positive harmonic function on a domain $\mathcal{V} \subset \mathcal{H}^{3}$. Then the Ricci curvature of the corresponding self-dual metric $g=e^{2 f}\left(V h+V^{-1} \theta^{2}\right)$ is given by
$$\begin{aligned}
\operatorname{Ric}_{g}= & \left(-2-\triangle f-2|d f|^{2}-V^{-1}\langle d V, d f\rangle\right) h \\
& -2 D d f+2(d f)^{2}+2 V^{-1} d V \odot d f \\
& +\left(-\triangle f-2|d f|^{2}+V^{-1}\langle d V, d f\rangle\right)\left(V^{-1} \theta\right)^{2} \\
& -2 V^{-1} \star(d V \wedge d f) \odot V^{-1} \theta
\end{aligned}$$
Here D, △, and ★ are respectively the Levi-Cività connection, negative Laplace-Beltrami operator, and Hodge star operator of hyperbolic 3-space $\left(\mathcal{H}^{3}, h\right)$, while $|\cdot|$ and $\langle\cdot, \cdot\rangle$ are the corresponding norm and inner product on 1-forms.

To prove these statements, let us first observe that (2.1) is valid iff it holds for some particular $f$; in particular, Propositions 2.2 and 2.3 are logically equivalent. Indeed, if $g_{0}=V h+V^{-1} \theta^{2}$ and $g=e^{2 f} g_{0}$, the standard formula [2] governing the alteration of curvature by conformal rescaling yields
$$\operatorname{Ric}_{g}=\operatorname{Ric}_{g_{0}}-2 \nabla d f+2(d f)^{2}-\left(\Delta f+2|d f|_{g_{0}}^{2}\right) g_{0}$$
where ∇ and $\Delta$ are respectively the Levi-Cività connection and negative Laplace-Beltrami operator of $g_{0}$. Now since
$$\begin{aligned}
\nabla d f & =\frac{1}{2} £_{\operatorname{grad}_{g_{0}} f} g_{0} \\
& =\frac{1}{2} £_{\operatorname{grad}_{g_{0}} f} V h+\frac{1}{2} £_{\operatorname{grad}_{g_{0}} f} V^{-1} \theta^{2} \\
& \left.=\frac{1}{2} £_{V^{-1} \operatorname{grad}_{h} f} V h+\frac{1}{2}\left(£_{V^{-1} \operatorname{grad}_{h} f} V^{-1}\right) \theta^{2}+V^{-1} \theta \odot\left(V^{-1} \operatorname{grad}_{h} f\right\lrcorner d \theta\right) \\
& =\frac{1}{2}\left(£_{V^{-1} \operatorname{grad}_{h} f} V\right) h+V \operatorname{symm}\left(D V^{-1} d f\right)-\frac{\langle d V, d f\rangle}{2 V^{3}} \theta^{2}+\frac{\left.\theta \odot\left(\operatorname{grad}_{h} f\right\lrcorner \star d V\right)}{V^{2}} \\
& =D d f-\frac{d V \odot d f}{V}+\frac{\langle d V, d f\rangle}{2 V} h-\frac{\langle d V, d f\rangle}{2 V^{3}} \theta^{2}+\frac{\theta \odot \star(d V \wedge d f)}{V^{2}},
\end{aligned}$$
it follows that
$$\Delta f=V^{-1} \triangle f,$$
and we therefore have
$$\begin{aligned}
\operatorname{Ric}_{g}= & \operatorname{Ric}_{g_{0}}-2 D d f+2 V^{-1} d V \odot d f-V^{-1}\langle d V, d f\rangle h \\
& +V^{-3}\langle d V, d f\rangle \theta^{2}-2 V^{-2} \theta \odot \star(d V \wedge d f)+2(d f)^{2} \\
& -\left(V^{-1} \triangle f+2 V^{-1}|d f|^{2}\right)\left(V h+V^{-1} \theta^{2}\right) \\
= & \operatorname{Ric}_{g_{0}}-\left(\triangle f+2|d f|^{2}+V^{-1}\langle d V, d f\rangle\right) h \\
& -2 D d f+2(d f)^{2}+2 V^{-1} d V \odot d f \\
& +\left(-\triangle f-2|d f|^{2}+V^{-1}\langle d V, d f\rangle\right)\left(V^{-1} \theta\right)^{2} \\
& -2 V^{-2} \theta \odot \star(d V \wedge d f) .
\end{aligned}$$
But this will coincide with (2.1) for any particular $f$ iff $\operatorname{Ric}_{g_{0}}=-2 h$.
We now complete our proof by verifying (2.1) for a slightly peculiar choice of $f$, best described in terms of the upper-half-space model
$$h=\frac{d x^{2}+d y^{2}+d z^{2}}{z^{2}}, \quad z>0,$$
of $\mathcal{H}^{3}$. We will now set $f=\log z$ because [13, §3] the corresponding metric
$$g=z^{2}\left(V h+V^{-1} \theta^{2}\right)$$
is Kähler with respect to the integrable almost-complex structure
$$d x \mapsto d y, \quad d z \mapsto \frac{z}{V} \theta,$$
with Ricci form
$$P=-d\left(V^{-1} \theta\right)=-\frac{\star d V}{V}+\frac{d V \wedge \theta}{V^{2}} .$$
The Ricci curvature of this metric is therefore
$$\begin{aligned}
\operatorname{Ric}_{g}= & \frac{V_{z}}{z V}\left[-d x^{2}-d y^{2}+d z^{2}+\left(\frac{z}{V} \theta\right)^{2}\right]+\frac{2 V_{x}}{z V}\left[d x \odot d z+d y \odot \frac{z}{V} \theta\right] \\
& +\frac{2 V_{y}}{z V}\left[d y \odot d z-d x \odot \frac{z}{V} \theta\right] .
\end{aligned}$$
But, since $|d f|^{2}=1$,
$$D d f=\frac{1}{2} £_{\operatorname{grad}_{h} f} h=\frac{1}{2} £_{z \frac{\partial}{\partial z}}\left(\frac{d x^{2}+d y^{2}+d z^{2}}{z^{2}}\right)=-\frac{d x^{2}+d y^{2}}{z^{2}},$$
and $\triangle f=-2$, this is exactly the result predicted by (2.1) with $f=\log z$. Thus (2.1) holds for our particular $f$, and Propositions 2.2 and 2.3 therefore follow.

To conclude this section, let us point out that the scalar curvature $s_{g}$ and the modified Ricci tensor $\mathrm{Q}_{g}=\operatorname{Ric}_{g}-\frac{1}{6} s_{g} g$ are now respectively given by
$$s_{g}=6 e^{-2 f} V^{-1}\left(-1-\triangle f-|d f|^{2}\right)$$
and
$$\begin{aligned}
\mathrm{Q}_{g}= & \left(-1-|d f|^{2}-\langle\psi, d f\rangle\right) h \\
& -2 D d f+2(d f)^{2}+2 \psi \odot d f \\
& +\left(1-|d f|^{2}+\langle\psi, d f\rangle\right)\left(V^{-1} \theta\right)^{2} \\
& -2 \star(\psi \wedge d f) \odot V^{-1} \theta
\end{aligned}$$
where $\psi=V^{-1} d V=d \log V$. Notice that the sign of $s_{g}$ is independent of $V$; for applications, cf. [12, 10].

\section*{3 Choosing a Conformal Factor}

The hyperbolic ansatz described in the last section can be used [12] to construct selfdual metrics on $n \mathbf{C P}_{2}$. When $n=1$, this construction gives metrics conformal to the Fubini-Study metric on $\mathbf{C P}_{2}$, and our main tasks here will be to re-examine the type of conformal factor this entails.

Let $\left\{p_{1}, \ldots, p_{n}\right\}$ be an arbitrary collection of $n$ points in $\mathcal{H}^{3}$, and let
$$G_{j}=\frac{1}{2}\left(\operatorname{coth} r_{j}-1\right)$$
be the hyperbolic Green's function centered at $p_{j}$; here $r_{j}$ is the hyperbolic distance from $p_{j}$, and our normalization is chosen so that $d \star d G_{j}=-2 \pi \delta_{p_{j}}$. Thus
$$V:=1+\sum_{j=1}^{n} G_{j}=1+\frac{1}{2} \sum_{j=1}^{n}\left(\operatorname{coth} r_{j}-1\right)$$
is a positive harmonic function on $\mathcal{V}=\mathcal{H}^{3} \backslash\left\{p_{1}, \ldots, p_{n}\right\}$ satisfying the integrality condition of Proposition 2.1. Letting $(\mathcal{M}, \theta)$ be the circle bundle with connection 1-form as in Proposition 2.1, which is uniquely determined up to gauge equivalence since $\mathcal{V}$ is simply connected, we thus obtain a self-dual metric
$$g_{0}=V h+V^{-1} \theta^{2}$$
on $\mathcal{M}$. If we now use the Klein projective model to identify $\mathcal{H}^{3}$ with the interior of the closed 3-disk $D^{3}$, there is a smooth compactification $M$ of $\mathcal{M}$ such that the bundle
projection $\mathcal{M} \rightarrow \mathcal{H}^{3} \backslash\left\{p_{j}\right\}$ extends to a surjective smooth map $M \rightarrow D^{3}$, and $D^{3}$ is thereby identified with the orbit space of an $S^{1}$-action on $M$; in fact, $M \backslash \mathcal{M}$ is the set of fixed points of this action, and consists of a 2-sphere $\widehat{S}^{2}$, which projects diffeomorphically to $\partial D^{3}$, and $n$ isolated fixed points $\widehat{p}_{j}$, one for each $p_{j} \in \mathcal{H}^{3}$. Moreover, $g=e^{2 f} g_{0}$ extends to a self-dual metric on the compact manifold $M \approx n \mathbf{C P}_{2}$ whenever $f: \mathcal{H}^{3} \rightarrow \mathbf{R}$ is a smooth function which behaves like $-r$ near infinity, where $r$ is the hyperbolic distance from an arbitrary reference point. When $n=0,1$, this construction produces the conformal classes of the standard metrics on $S^{4}$ and $\mathbf{C P}_{2}$; when $n=2$, it instead yields the self-dual metrics on $2 \mathrm{CP}_{2}$ first discovered by Poon [15].

In the above discussion, we assumed for simplicity that $f$ was a smooth function on $\mathcal{H}^{3}$; and on $\mathcal{H}^{3} \backslash\left\{p_{j}\right\}$ smoothness is obviously needed to guarantee that $e^{2 f} g_{0}$ is smooth on $\mathcal{M}$. On the other hand, the derivative of the natural projection $M \rightarrow D^{3}$ vanishes at each $\widehat{p}_{j}$, and the pull-back of the function $r_{j}$ is consequently smooth on $M \backslash S^{2}$. Choices of $f$ with this sort of behavior near the $p_{j}$ are also allowable, and will in fact turn out to be crucial for our purposes.

To see why, let us look more closely at the $n=1$ case. In geodesic polar coordinates about $p=p_{1}$, the hyperbolic metric on $\mathcal{H}^{3} \backslash p$ can be written as
$$h=d r^{2}+\sinh ^{2} r g_{S^{2}},$$
where $g_{S^{2}}$ is the standard metric on the unit 2-sphere. Now the ansatz stipulates that $V=1+\frac{1}{2}(\operatorname{coth} r-1)=\left(1-e^{-2 r}\right)^{-1}$, and hence $\star d V=-\frac{1}{2} \omega$, where $\omega$ is the standard area form on the 2-sphere. In order to produce a circle bundle with this curvature, let $\mu: S^{3} \rightarrow S^{2}$ be the Hopf map, and let the unit 3-sphere $S^{3}=S p(1)$ be equipped with a left-invariant orthornomal coframe $\left\{\sigma_{1}, \sigma_{2}, \sigma_{3}\right\}$ such that $\mu^{*} g_{S^{2}}=4\left(\sigma_{1}{ }^{2}+\sigma_{2}{ }^{2}\right)$. Then $\mu^{*}\left(-\frac{1}{2} \omega\right)=-2 \sigma_{1} \wedge \sigma_{2}=d\left(-\sigma_{3}\right)$, and the desired circle bundle $\pi: \mathcal{M} \rightarrow \mathcal{H}^{3} \backslash p$ may be taken to be the pull-back of $\mu$, with connection form $\theta=-\sigma_{3}$, to $S^{2} \times \mathbf{R}^{+}$. Thus
$$\begin{aligned}
g_{0} & =V h+V^{-1} \theta^{2} \\
& =\frac{1}{1-e^{-2 r}}\left[d r^{2}+4 \sinh ^{2} r\left(\sigma_{1}{ }^{2}+\sigma_{2}{ }^{2}\right)\right]+\left(1-e^{-2 r}\right) \sigma_{3}{ }^{2}
\end{aligned}$$
Setting $\rho=\cos ^{-1}\left(e^{-r}\right)$, we now have
$$\begin{aligned}
e^{-2 r} g_{0} & =\cot ^{2} \rho\left[\tan ^{2} \rho d \rho^{2}+\tan ^{2} \rho \sin ^{2} \rho\left(\sigma_{1}^{2}+\sigma_{2}^{2}\right)\right]+\cos ^{2} \rho \sin ^{2} \rho \sigma_{3}^{2} \\
& =d \rho^{2}+\sin ^{2} \rho\left({\sigma_{1}}^{2}+{\sigma_{2}}^{2}+\cos ^{2} \rho \sigma_{3}^{2}\right)
\end{aligned}$$
which is exactly the Fubini-Study metric of $\mathbf{C P}_{2}$, expressed in geodesic polar coordinates. So far as positive Ricci curvature is concerned, the best possible choice of $f$ when $n=1$ is thus $f=-r$, and the challenge now facing us is to suitably generalize this for $n>1$.

Since we will still need $f \sim-r$ as $r \rightarrow \infty$, one obvious generalization is
$$f=-\frac{r_{1}+\cdots+r_{n}}{n} .$$
In the next section, we will see that this choice actually works surprisingly well when $n \leq 3$.

\section*{4 Positive Ricci Curvature}

In the previous section, we associated a conformal class of self-dual metrics on $n \mathbf{C P}_{2}$ to any configuration of points $\left\{p_{1}, \ldots, p_{n}\right\}$ in $\mathcal{H}^{3}$. We will henceforth denote this conformal class by $C_{p_{1}, \ldots, p_{n}}$.

Theorem 4.1 Each conformal class $C_{p_{1}, p_{2}}$ of self-dual metrics on $\mathbf{C P}_{2} \# \mathbf{C P}_{2}$ contains a metric with strongly positive Ricci curvature and non-negative Ricci operator.

In fact, the metric $g=e^{2 f}\left(V h+V^{-1} \theta^{2}\right)$ has these properties provided we set
$$f=-\frac{r_{1}+r_{2}}{2},$$
where $r_{1}$ and $r_{2}$ are respectively the hyperbolic distances from $p_{1}, p_{2} \in \mathcal{H}^{3}$. We will prove this by first showing that the Ricci operator is non-negative, and then observing that the Ricci curvature is still strongly positive at the points where the Ricci operator has non-trivial kernel.

On an open dense subset of $\mathcal{M} \subset M$, and with respect to the metric $V^{-1} g_{0}=$ $h+V^{-2} \theta^{2}$, we may define an oriented orthonormal coframe $\left\{\mathbf{e}^{1}, \ldots, \mathbf{e}^{4}\right\}$ by
$$\mathbf{e}^{1}=\frac{d r_{1}+d r_{2}}{\left|d r_{1}+d r_{2}\right|}, \quad \mathbf{e}^{2}=\frac{d r_{1}-d r_{2}}{\left|d r_{1}-d r_{2}\right|}, \text { and } \mathbf{e}^{4}=V^{-1} \theta .$$
Let $\varphi:=\sin ^{-1}\left\langle d r_{1}, \mathbf{e}^{1}\right\rangle$ be the oriented angle between $d r_{1}$ and $\mathbf{e}^{1}$. Then
$$d f=-(\cos \varphi) \mathbf{e}^{1},$$
$$\begin{aligned}
d V & =-\frac{1}{2}\left[\frac{d r_{1}}{\sinh ^{2} r_{1}}+\frac{d r_{2}}{\sinh ^{2} r_{2}}\right] \\
& =-\frac{1}{2}\left[\cos \varphi\left(\frac{1}{\sinh ^{2} r_{1}}+\frac{1}{\sinh ^{2} r_{2}}\right) \mathbf{e}^{1}+\sin \varphi\left(\frac{1}{\sinh ^{2} r_{1}}-\frac{1}{\sinh ^{2} r_{2}}\right) \mathbf{e}^{2}\right],
\end{aligned}$$
$$\begin{aligned}
D d f= & -\frac{1}{2}\left[\operatorname{coth} r_{1}\left(h-d r_{1}^{2}\right)+\operatorname{coth} r_{2}\left(h-d r_{2}^{2}\right)\right] \\
= & -\frac{1}{2}\left[\sin ^{2} \varphi\left(\operatorname{coth} r_{1}+\operatorname{coth} r_{2}\right)\left(\mathbf{e}^{1}\right)^{2}-2 \cos \varphi \sin \varphi\left(\operatorname{coth} r_{1}-\operatorname{coth} r_{2}\right) \mathbf{e}^{1} \odot \mathbf{e}^{2}\right. \\
& \left.+\cos ^{2} \varphi\left(\operatorname{coth} r_{1}+\operatorname{coth} r_{2}\right)\left(\mathbf{e}^{2}\right)^{2}+\left(\operatorname{coth} r_{1}+\operatorname{coth} r_{2}\right)\left(\mathbf{e}^{3}\right)^{2}\right] .
\end{aligned}$$

Plugging these expressions into (2.3), we see that the components of Q with respect to the dual frame $\left\{\mathbf{e}_{j}\right\}$ of $\left\{\mathbf{e}^{j}\right\}$ satisfy
$$\begin{aligned}
\mathrm{Q}_{11} & =(\alpha+1) \sin ^{2} \varphi+\beta \cos ^{2} \varphi \\
& >\sin ^{2} \varphi+\beta, \\
\mathrm{Q}_{22} & =(\alpha-\beta) \cos ^{2} \varphi-\sin ^{2} \varphi \\
& >-\sin ^{2} \varphi, \\
\mathrm{Q}_{33} & =(\alpha+1)-(\beta+1) \cos ^{2} \varphi \\
& >(\beta+1) \sin ^{2} \varphi, \\
\mathrm{Q}_{34} & =\mathrm{Q}_{43} \\
& =\gamma \sin \varphi \cos \varphi, \\
\mathrm{Q}_{44} & =\sin ^{2} \varphi+\beta \cos ^{2} \varphi, \\
\mathrm{Q}_{j k} & =0 \text { otherwise, }
\end{aligned}$$
where $\alpha:=\operatorname{coth} r_{1}+\operatorname{coth} r_{2}-2, \beta:=\frac{\operatorname{coth}^{2} r_{1}+\operatorname{coth}^{2} r_{2}-2}{\operatorname{coth} r_{1}+\operatorname{coth} r_{2}}$, and $\gamma:=\operatorname{coth} r_{1}-\operatorname{coth} r_{2}$ satisfy $\alpha>\beta>|\gamma|$.

Now since $\mathrm{Q}_{33}$ and $\mathrm{Q}_{44}$ both exceed $\sin ^{2} \varphi$, and since
$$\begin{aligned}
\left|\begin{array}{cc}
\mathrm{Q}_{33}-\sin ^{2} \varphi & \mathrm{Q}_{34} \\
\mathrm{Q}_{43} & \mathrm{Q}_{44}-\sin ^{2} \varphi
\end{array}\right| & >\left(\beta \sin ^{2} \varphi\right)\left(\beta \cos ^{2} \varphi\right)-\gamma^{2} \sin ^{2} \varphi \cos ^{2} \varphi \\
& =\left(\beta^{2}-\gamma^{2}\right) \sin ^{2} \varphi \cos ^{2} \varphi \\
& \geq 0,
\end{aligned}$$
the eigenvalues $\left[\mathrm{Q}_{j k}\right]$ in the $\mathbf{e}_{3} \mathbf{e}_{4}$-plane exceed $\sin ^{2} \varphi$. Hence three of the eigenvalues of $\left[\mathrm{Q}_{j k}\right]$ exceed $\sin ^{2} \varphi$, whereas the remaining eigenvalue $\mathrm{Q}_{22}$ is greater than $-\sin ^{2} \varphi$. The sum of the lowest two eigenvalues of Q, calculated with respect to any metric in the fixed conformal class, is therefore positive on the domain of our moving frame. But since this domain is actually dense, it follows that the Ricci operator is non-negative on the entirety of $M \approx 2 \mathrm{CP}_{2}$.

Since $\mathrm{Q}_{11}>\left(\mathrm{Q}_{33}+\mathrm{Q}_{44}\right) / 2=(\alpha / 2)+\sin ^{2} \varphi$, the largest two eigenvalues of $\left[\mathrm{Q}_{j k}\right]$ are at least $(\alpha / 2)+\sin ^{2} \varphi$ on the domain of our frame, and the sum of the lowest and third lowest eigenvalues of $\left[\mathrm{Q}_{j k}\right]$ therefore exceeds $\alpha / 2$ on this region. However, the frame $\left\{\mathbf{e}_{j}\right\}$ we have been using is only conformally orthonormal with respect to $g=e^{2 f} V\left(h+V^{-2} \theta^{2}\right)$. We now remedy this by introducing the $g$-orthonormal frame $\mathbf{e}_{j}^{\prime}:=e^{-f} V^{-1 / 2} \mathbf{e}_{j}$, with respect to which the components of Q become
$$\mathrm{Q}_{j k}^{\prime}=e^{-2 f} V^{-1} \mathrm{Q}_{j k}=\frac{2 e^{r_{1}+r_{2}}}{\operatorname{coth} r_{1}+\operatorname{coth} r_{2}} \mathrm{Q}_{j k} .$$

If $\mu_{1} \leq \mu_{2} \leq \mu_{3} \leq \mu_{4}$ are the eigenvalues of $\left[\mathrm{Q}_{j k}^{\prime}\right]$, we therefore have
$$\begin{aligned}
\mu_{1}+\mu_{3} & >\frac{\alpha e^{r_{1}+r_{2}}}{\operatorname{coth} r_{1}+\operatorname{coth} r_{2}}=e^{r_{1}+r_{2}} \frac{e^{2 r_{1}}+e^{2 r_{2}}-2}{e^{2\left(r_{1}+r_{2}\right)}-1} \\
& \geq e^{r_{1}+r_{2}} \frac{2 e^{r_{1}+r_{2}}-2}{e^{2\left(r_{1}+r_{2}\right)}-1}=\frac{2}{1+e^{-\left(r_{1}+r_{2}\right)}}>1
\end{aligned}$$
Because the domain of our frame is dense, the continuity of the spectrum therefore implies that the sum $\mu_{1}+\mu_{3}$ of the lowest and third lowest eigenvalues of Q, calculated with respect to $g$, is at least 1 on all of $M$. The sum $\mu_{1}+\mu_{2}$ of the two lowest eigenvalues of Q can thus vanish only at points at which Q does not have an eigenvalue of multiplicity 3, and the Ricci curvature of $g$ is therefore strongly positive on all of $M$.

Corollary 4.2 Any self-dual metric of positive scalar curvature on $\mathbf{C P}_{2} \# \mathbf{C P}_{2}$ is conformal to a metric of strongly positive Ricci curvature and non-negative Ricci operator.

Proof. Any self-dual conformal class on $\mathbf{C P}_{2} \# \mathbf{C P}_{2}$ with a representative of positive scalar curvature is [12, p. 251] of the form $C_{p_{1}, p_{2}}$. \(\square\)

With this success in hand, it seems reasonable, more generally, to investigate the Ricci curvature of metrics of the form $e^{2 f}\left(V h+V^{-1} \theta^{2}\right)$ on $n \mathbf{C P}_{2}$, where $V$ is defined by (3.1) and
$$f=-\frac{r_{1}+\cdots+r_{n}}{n} .$$
In fact, a rough picture is not difficult to obtain when the points $p_{1}, \ldots, p_{n} \in \mathcal{H}^{3}$ are extremely close together. Indeed, consider a sequence of configurations of $n$ distinct points in $\mathcal{H}^{3}$ which converges to the degenerate configuration consisting of a single point $p \in \mathcal{H}^{3}$ counted with multiplicity $n$. On the complement of any ball about $p$, the curvature of these metrics will converge uniformally to that of the orbifold metric corresponding to $V=1+n G$ and $f=-r$, where $r$ is the hyperbolic distance from $p$ and $G=(\operatorname{coth} r-1) / 2$. But (2.1) predicts that the Ricci tensor of this orbifold limit is
$$\operatorname{Ric}=\zeta\left[d r^{2}+\left(V^{-1} \theta\right)^{2}\right]+\eta\left(h-d r^{2}\right),$$
where
$$\begin{aligned}
\zeta & =\frac{\operatorname{coth} r-1}{2+n(\operatorname{coth} r-1)}(4+3 n \operatorname{coth} r-n), \\
\eta & =\frac{\operatorname{coth} r-1}{2+n(\operatorname{coth} r-1)}(8+3 n \operatorname{coth} r-5 n) .
\end{aligned}$$
Observe that $\eta$ is positive everywhere on $\mathcal{H}^{3}$ iff $n \leq 4$, and that $\lim _{r \rightarrow \infty} \eta / \zeta=0$ if $n=4$; moreover, we always have $\zeta \geq \eta$. Hence the Ricci curvature of this orbifold limit is
everywhere positive if and only if $n \leq 3$. (When $n=4$, it is still non-negative, but fails to be positive along $\widehat{S}^{2}$.) In short, the only encouraging news pertains to the $n=3$ case, where the above computation will help us to prove the following:

Theorem 4.3 If $p_{1}, p_{2}, p_{3} \in \mathcal{H}^{3}$ are nearly geodesically collinear and are sufficiently close to each other, then the conformal class $C_{p_{1}, p_{2}, p_{3}}$ of self-dual metrics on $3 \mathbf{C P}_{2}$ contains a metric with positive Ricci curvature.

To produce self-dual metrics with positive Ricci curvature on $3 \mathbf{C P}_{2}$, we start with the above singular model and pull the centers $p_{1}, p_{2}, p_{3}$ slightly apart, keeping them geodesically collinear. Outside a neighborhood of $p$, the Ricci curvature remains positive by our previous computation. Theorem 4.3 is thus implied by the following:

Lemma 4.4 There exists an $\varepsilon>0$ such that, for all collinear configurations $\left\{p_{1}, p_{2}, p_{3}\right\} \subset$ $\mathcal{H}^{3}$, the Ricci curvature of $g$ is positive on the inverse image of $\cup_{j=1}^{3} B_{\varepsilon}\left(p_{j}\right)$.

Proof. Ignoring bounded terms, $D d f \sim-\frac{1}{3} \sum_{j} \frac{1}{r_{j}}\left(h-d r_{j}{ }^{2}\right), \Delta f \sim-\frac{2}{3}\left(\frac{1}{r_{1}}+\frac{1}{r_{2}}+\frac{1}{r_{3}}\right)$, $V \sim \frac{1}{2}\left(\frac{1}{r_{1}}+\frac{1}{r_{2}}+\frac{1}{r_{3}}\right)$, and $d V \sim-\frac{1}{2}\left(\frac{d r_{1}}{r_{1}{ }^{2}}+\frac{d r_{2}}{r_{2}{ }^{2}}+\frac{d r_{3}}{r_{3}{ }^{2}}\right)$. Equation (2.1) therefore tells us that
$$\begin{aligned}
6 V \text { Ric } \sim & {\left[2\left(\frac{1}{r_{1}}+\frac{1}{r_{2}}+\frac{1}{r_{3}}\right)^{2}-\left\langle\frac{d r_{1}}{r_{1}^{2}}+\frac{d r_{2}}{r_{2}^{2}}+\frac{d r_{3}}{r_{3}^{2}}, d r_{1}+d r_{2}+d r_{3}\right\rangle\right] h } \\
& +2\left(\frac{1}{r_{1}}+\frac{1}{r_{2}}+\frac{1}{r_{3}}\right) \sum_{j} \frac{1}{r_{j}}\left(h-d r_{j}^{2}\right)+2\left(\frac{d r_{1}}{r_{1}^{2}}+\frac{d r_{2}}{r_{2}^{2}}+\frac{d r_{3}}{r_{3}^{2}}\right) \odot\left(d r_{1}+d r_{2}+d r_{3}\right) \\
& +\left[2\left(\frac{1}{r_{1}}+\frac{1}{r_{2}}+\frac{1}{r_{3}}\right)^{2}+\left\langle\frac{d r_{1}}{r_{1}^{2}}+\frac{d r_{2}}{r_{2}^{2}}+\frac{d r_{3}}{r_{3}^{2}}, d r_{1}+d r_{2}+d r_{3}\right\rangle\right]\left(V^{-1} \theta\right)^{2} \\
& -2 \star\left[\left(\frac{d r_{1}}{r_{1}^{2}}+\frac{d r_{2}}{r_{2}^{2}}+\frac{d r_{3}}{r_{3}^{2}}\right) \wedge\left(d r_{1}+d r_{2}+d r_{3}\right)\right] \odot V^{-1} \theta,
\end{aligned}$$
where ~ means that the difference between the left- and right-hand sides is of order $g_{0}=V h+V^{-1} \theta^{2}$ on $\cup_{j=1}^{3} B_{\varepsilon}\left(p_{j}\right)$. Letting $\widehat{R}$ denote the right-hand side of the above expression, it will thus suffice for us to show that $\widehat{R}$ dominates $V g_{0}=V^{2} h+\theta^{2}$, since Ric will then dominate $\frac{1-C V^{-1}}{6} g_{0}$ for some constant $C$, and so will be positive-definite on $\cup_{j=1}^{3} B_{\varepsilon}\left(p_{j}\right)$ for $\varepsilon$ sufficiently small.

Because we are only considering collinear configurations, $d r_{1}+d r_{2}+d r_{3} \neq 0$ on $\mathcal{H}^{3} \backslash\left\{p_{1}, p_{2}, p_{3}\right\}$, and we may let $\mathbf{e}^{1}$ be the unit covector in this direction. At any given point, choose $\mathbf{e}^{2}$ so that the $d r_{j}$ are all linear combinations of $\mathbf{e}^{1}$ and $\mathbf{e}^{2}$ :
$$d r_{j}=\cos \varphi_{j} \mathbf{e}^{1}+\sin \varphi_{j} \mathbf{e}^{2} .$$

Extend this to an oriented orthonormal coframe $\left\{\mathbf{e}^{1}, \mathbf{e}^{2}, \mathbf{e}^{3}\right\}$ for $h$, and set $\mathbf{e}^{4}=V^{-1} \theta$. Then, letting $\kappa:=\sum_{j} \cos \varphi_{j}$, the components of $\widehat{R}$ with respect to the dual frame $\left\{\mathbf{e}_{j}\right\}$ are
$$\begin{aligned}
\widehat{R}_{11} & =\sum_{j} \frac{1}{r_{j}^{2}}\left(2+\kappa \cos \varphi_{j}+2 \sin ^{2} \varphi_{j}\right)+2 \sum_{j<k} \frac{1}{r_{j} r_{k}}\left(2+\sin ^{2} \varphi_{j}+\sin ^{2} \varphi_{k}\right), \\
\widehat{R}_{22} & =\sum_{j} \frac{1}{r_{j}^{2}}\left(2-\kappa \cos \varphi_{j}+2 \cos ^{2} \varphi_{j}\right)+2 \sum_{j<k} \frac{1}{r_{j} r_{k}}\left(2+\cos ^{2} \varphi_{j}+\cos ^{2} \varphi_{k}\right), \\
\widehat{R}_{12} & =\widehat{R}_{21} \\
& =\sum_{j} \frac{1}{r_{j}^{2}}\left(\kappa-2 \cos \varphi_{j}\right) \sin \varphi_{j}-2 \sum_{j<k} \frac{1}{r_{j} r_{k}}\left(\cos \varphi_{j} \sin \varphi_{j}+\cos \varphi_{k} \sin \varphi_{k}\right), \\
\widehat{R}_{33} & =\sum_{j} \frac{1}{r_{j}^{2}}\left(4-\kappa \cos \varphi_{j}\right)+8 \sum_{j<k} \frac{1}{r_{j} r_{k}}, \\
\widehat{R}_{44} & =\sum_{j} \frac{1}{r_{j}^{2}}\left(2+\kappa \cos \varphi_{j}\right)+4 \sum_{j<k} \frac{1}{r_{j} r_{k}}, \\
\widehat{R}_{34} & =\widehat{R}_{43}=\sum_{j} \frac{1}{r_{j}^{2}} \kappa \sin \varphi_{j}, \\
\widehat{R}_{j k} & =0 \text { otherwise. }
\end{aligned}$$

We now just need to show that the eigenvalues of $\left[\widehat{R}_{j k}\right]$ are all bigger than $V^{2}$. To do this, first notice that $\sum_{k} \sin \varphi_{k}=0$, and so
$$\begin{aligned}
\kappa \cos \left(\varphi_{j}-2 \vartheta\right) & =\left(\sum_{k} \cos \varphi_{k}\right) \cos \left(\varphi_{j}-2 \vartheta\right)-\left(\sum_{k} \sin \varphi_{k}\right) \sin \left(\varphi_{j}-2 \vartheta\right) \\
& =\sum_{k} \cos \left(\varphi_{j}+\varphi_{k}-2 \vartheta\right)
\end{aligned}$$
for any $\vartheta$. Thus
$$\cos ^{2} \vartheta \widehat{R}_{11}+2 \cos \vartheta \sin \vartheta \widehat{R}_{12}+\sin ^{2} \vartheta \widehat{R}_{22}=\sum_{j} \frac{a_{j}(\vartheta)}{r_{j}{ }^{2}}+\sum_{j<k} \frac{a_{j k}(\vartheta)}{r_{j} r_{k}}$$
and
$$\cos ^{2} \vartheta \widehat{R}_{33}+2 \cos \vartheta \sin \vartheta \widehat{R}_{34}+\sin ^{2} \vartheta \widehat{R}_{44}=\sum_{j} \frac{b_{j}(\vartheta)}{r_{j}{ }^{2}}+\sum_{j<k} \frac{b_{j k}(\vartheta)}{r_{j} r_{k}},$$
where
$$\begin{aligned}
a_{j}(\vartheta):= & \cos ^{2} \vartheta\left(2+\kappa \cos \varphi_{j}+2 \sin ^{2} \varphi_{j}\right)+\sin ^{2} \vartheta\left(2-\kappa \cos \varphi_{j}+2 \cos ^{2} \varphi_{j}\right) \\
& +2 \cos \vartheta \sin \vartheta\left(\kappa-2 \cos \varphi_{j}\right) \sin \varphi_{j} \\
= & 3+\kappa \cos \left(\varphi_{j}-2 \vartheta\right)-\cos \left(2 \varphi_{j}-2 \vartheta\right) \\
= & 3+\sum_{k \neq j} \cos \left(\varphi_{j}+\varphi_{k}-2 \vartheta\right)
\end{aligned}$$
$$\begin{aligned}
& \geq 1, \\
b_{j}(\vartheta): & \cos ^{2} \vartheta\left(4-\kappa \cos \varphi_{j}\right)+2 \cos \vartheta \sin \vartheta \kappa \sin \varphi_{j}+\sin ^{2} \vartheta\left(2+\kappa \cos \varphi_{j}\right) \\
& =3+\cos 2 \vartheta-\kappa \cos \left(\varphi_{j}+2 \vartheta\right) \\
& =3-\sum_{k \neq j} \cos \left(\varphi_{j}-\varphi_{k}+2 \vartheta\right) \\
& \geq 1, \\
a_{j k}(\vartheta): & 2 \cos ^{2} \vartheta\left(2+\sin ^{2} \varphi_{j}+\sin ^{2} \varphi_{k}\right)+2 \sin ^{2} \vartheta\left(2+\cos ^{2} \varphi_{j}+\cos ^{2} \varphi_{k}\right) \\
& -4 \sin \vartheta \cos \vartheta\left(\cos \varphi_{j} \sin \varphi_{j}+\cos \varphi_{k} \sin \varphi_{k}\right) \\
& =6-\cos \left(2 \varphi_{j}-2 \vartheta\right)-\cos \left(2 \varphi_{k}-2 \vartheta\right) \\
& \geq 4>2, \\
b_{j k}(\vartheta): & 8 \cos ^{2} \vartheta+4 \sin ^{2} \vartheta=4+4 \cos ^{2} \vartheta \\
& \geq 4>2 .
\end{aligned}$$
Hence every eigenvalue of $\left[\widehat{R}_{j k}\right]$ exceeds $\sum_{j} \frac{1}{r_{j}{ }^{2}}+\sum_{j<k} \frac{2}{r_{j} r_{k}}=\left(\sum_{j} \frac{1}{r_{j}}\right)^{2}$, and hence exceeds $V^{2}$ on $\cup_{j} B_{\varepsilon}\left(p_{j}\right)$ for any $\varepsilon<\frac{1}{2}$. The result follows. \(\square\)

\section*{References}
\begin{itemize}
\item[] [1] M.T. Anderson, Short Geodesics and Gravitational Instantons, J. Diff. Geom. 31 (1990) 265-275.
\item[] [2] A.L. Besse, Einstein Manifolds, Springer, Berlin, 1987.
\item[] [3] J.-P. Bourguignon, Les Variétés de Dimension 4 à Signature Non-Nulle dont la Courbure est Harmonique sont d'Einstein, Invent. Math. 63 (1981) 263-286.
\item[] [4] J. Cheeger, Some Examples of Manifolds of Nonnegative Curvature, J. Diff. Geom. 8 (1973) 623-628.
\item[] [5] S.K. Donaldson, An Application of Gauge Theory to Four Dimensional Topology, J. Diff. Geom. 18 (1983) 279-315.
\item[] [6] S.K. Donaldson and R. Friedman, Connected Sums of Self-Dual Manifolds and Deformations of Singular Spaces, Nonlinearity 2 (1989) 197-239.
\item[] [7] A. Floer, Self-Dual Conformal Structures on $\ell C P^{2}$, J. Diff. Geom. 33 (1991) 551-573.
\end{itemize}
\begin{itemize}
\item[] [8] P. Gauduchon, Self-Dual Manifolds with Non-Negative Ricci Operator, in Global Differential Geometry and Global Analysis, D. Ferus et al. (eds.), Lect. Notes Math. 1481 (1991) 55-61.
\item[] [9] G.W. Gibbons and S.W. Hawking, Gravitational Multi-Instantons, Phys. Lett. B78 (1978) 430-432.
\item[] [10] J.-S. Kim, On the Scalar Curvature of Self-Dual Manifolds, Math. Ann. 297 (1993) 235-251.
\item[] [11] C.R. LeBrun, On the Topology of Self-Dual 4-Manifolds, Proc. Amer. Math. Soc. 98 (1986) 637-640.
\item[] [12] C.R. LeBrun, Explicit Self-Dual Metrics on $\mathbf{C P}_{2} \# \cdots \# \mathbf{C P}_{2}$, J. Diff. Geom. 34 (1991) 223-253.
\item[] [13] C.R. LeBrun, Anti-Self-Dual Hermitian Metrics on Blown-Up Hopf Surfaces, Math. Ann. 289 (1991) 383-392.
\item[] [14] H. Pedersen and Y.-S. Poon, Self-Duality and Differentiable Structures on the Connected Sum of Complex Projective Planes, Proc. Amer. Math. Soc. 121 (1994) 859-864.
\item[] [15] Y.-S. Poon, Compact Self-Dual Manifolds with Positive Scalar Curvature, J. Diff. Geom. 24 (1986) 97-132.
\item[] [16] J.-P. Sha and D.-G. Yang, Positive Ricci Curvature on Compact Simply Connected 4-Manifolds, in Differential Geometry, R. Greene and S.-T. Yau (eds.), Proc. Symp. Pure Math. 54, 3 (1993) 529-538.
\end{itemize}
