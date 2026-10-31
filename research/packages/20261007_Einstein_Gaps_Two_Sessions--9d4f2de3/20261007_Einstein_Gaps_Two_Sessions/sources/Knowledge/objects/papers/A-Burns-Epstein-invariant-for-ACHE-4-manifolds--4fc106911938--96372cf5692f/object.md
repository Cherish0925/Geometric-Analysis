# A Burns-Epstein invariant for ACHE 4-manifolds

- Category: papers
- Identity: doi:10.1215/s0012-7094-04-12612-0
- Content status: fulltext_ok

---

---
source_file: A_Burns-Epstein_invariant_for_ACHE_4-manifolds_81967cbdd3b6.pdf
converter: mathpix
format: mmd
---

\title{
A BURNS-EPSTEIN INVARIANT FOR ACHE 4-MANIFOLDS
}

\author{
OLIVIER BIQUARD AND MARC HERZLICH
}

\begin{abstract}
We define a renormalized characteristic class for Einstein asymptotically complex hyperbolic (ache) manifolds of dimension 4: for any such manifold, the polynomial in the curvature associated to the characteristic class $\chi-3 \tau$ is shown to converge. This extends a work of Burns and Epstein in the Kähler-Einstein case.

We also define a new global invariant for any compact 3-dimensional pseudoconvex CR manifold, by a renormalization procedure of the $\eta$ invariant of a sequence of metrics which approximate the CR structure.

Finally, we get a formula relating the renormalized characteristic class to the topological number $\chi-3 \tau$ and the invariant of the CR structure arising at infinity.
\end{abstract}

\section*{1. Introduction}

In [BE90], Burns and Epstein showed that, for complete Kähler-Einstein metrics on bounded domains in $\mathbb{C}^{m}$ or in a complex manifold, the local integrands of some (precisely known) combinations of the Chern classes had convergent integrals, thus providing interesting invariants of bounded domains. In some cases, they were also able to compute renormalized Chern-Gauss-Bonnet formulas by relating the total integral of such characteristic polynomials with the expected characteristic numbers and some invariants of the CR-structure at infinity.

For instance, in (complex) dimension $m=2$, the integral of the characteristic polynomial
$$3 c_{2}-\left(c_{1}\right)^{2}$$
in the curvature tensor $R$ of the complete Kähler-Einstein metric of a pseudoconvex domain $\Omega$ in $\mathbb{C}^{2}$ is shown to converge, and it is the only one to behave

\footnotetext{
1991 Mathematics Subject Classification. 53C55, 58J37, 58J60 (primary), 32V15, 58J28 (secondary).
Key words and phrases. Asymptotically symmetric Einstein metrics, characteristic classes, complete Kähler-Einstein metrics, CR structures, Burns-Epstein invariant.
Both authors are members of the edge Research Training Network hprn-ct-2000-00101 of the European Union. The second author is also supported in part by an ACI program of the French Ministry of Research.
}
this way. Moreover, one can prove that
$$\int_{\Omega}\left(c_{2}-\frac{1}{3}\left(c_{1}\right)^{2}\right)(R)=\chi(\Omega)+\mu(\partial \Omega)$$
where $\chi$ is the Euler characteristic and $\mu$ is the Burns-Epstein invariant of the CR-structure of $\partial \Omega$ [BE88].

In [Biq00], the first author showed that a lot of not necessarily integrable pseudoconvex CR-structures on odd-dimensional spheres $\mathbb{S}^{2 m-1}$ (including a neigh-borhood of the standard structure) may be filled in by complete Einstein metrics on the ball $\mathbb{B}^{2 m}$. Manifolds of (real) dimension 3 (i.e. $m=2$, as above) have the special feature that there is no integrability condition for CR-structures. However, it is well-known that a lot of such structures, even close to the standard one, cannot be obtained as the boundary of a complex domain, and hence, even in this dimension the filling Einstein metrics cannot be reduced to the classical complete Kähler-Einstein metrics of pseudo-convex domains [CY80].

Nevertheless, the integrability of the CR structure at infinity supports the idea that, in (real) dimension $2 m=4$, the asymptotically complex hyperbolic Einstein metrics (ACHE, in short) of [Biq00] should retain some of the features of the Kähler situation. In this paper, we show that this is indeed the case as far as renormalized characteristic classes are concerned. More precisely, for any asymptotically complex hyperbolic Einstein manifold $(M, g)$ of (real) dimension 4, the special combination of the norms of various parts of its curvature
$$\frac{1}{8 \pi^{2}}\left(3\left|W^{-}\right|^{2}-\left|W^{+}\right|^{2}+\frac{1}{24} \text { Scal }^{2}\right)$$
has convergent integral. Of course, this is the integrand of the characteristic class $\chi-3 \tau$ (where $\chi$ is the Euler characteristic and $\tau$ the signature) which, in Kähler-Einstein geometry, may be rewritten as $3 c_{2}-\left(c_{1}\right)^{2}$. Thus, our main result reads:
1.1. Theorem. Let $(M, g)$ be an asymptotically complex hyperbolic, Einstein, manifold of dimension 4. Then
$$\frac{1}{8 \pi^{2}} \int_{M}\left(3\left|W^{-}\right|^{2}-\left|W^{+}\right|^{2}+\frac{1}{24} \mathrm{Scal}^{2}\right)$$
converges, and provides an invariant of the asymptotically complex hyperbolic Einstein metric, which we call the Burns-Epstein invariant of $g$.

Furthermore, one can hope to relate its values to the characteristic numbers and to some invariants of the CR structure of the boundary at infinity $\partial_{\infty} M$. We define such an invariant, proving:
1.2. Theorem. There is a global invariant $\nu(X)$ defined for any compact strictly pseudoconvex 3-dimensional CR manifold $X$, such that if $X=\partial_{\infty} M$ is the CR
structure at infinity induced by an asymptotically complex hyperbolic, Einstein, metric on $M$, then
$$\frac{1}{8 \pi^{2}} \int_{M}\left(3\left|W^{-}\right|^{2}-\left|W^{+}\right|^{2}+\frac{1}{24} \mathrm{Scal}^{2}\right)=\chi(M)-3 \tau(M)+\nu(X) .$$

We now relate our invariant $\nu$ to the Burns-Epstein invariant $\mu$. Remind that $\mu(J)$ is defined only in the case where the CR structure $J$ on $X$ has trivial holomorphic bundle. In the case where $M$ is Kähler-Einstein, and $\partial_{\infty} M$ has trivial holomorphic bundle, one has the Burns-Epstein formula [BE90]
$$\int_{M} c_{2}-\frac{1}{3} c_{1}^{2}=\chi(M)-\frac{1}{3} \bar{c}_{1}(M)^{2}+\mu\left(\partial_{\infty} M\right),$$
where $\bar{c}_{1}(M)$ is a lifting of $c_{1}(M)$ in $H^{2}\left(M, \partial_{\infty} M\right)$. The LHS is precisely one third the LHS in formula (1.5), but there is no clear relation between the topological terms on the right, so we can only deduce that in that case $\nu(J)-3 \mu(J)$ is given by some topological term depending of the filling. Of course, for the boundary $X$ of a domain in $\mathbb{C}^{2}$, we get immediately $\nu(X)=3 \mu(X)+2$.

This problem can be avoided by considering the relative version $\mu\left(J, J^{\prime}\right)$ introduced by Cheng and Lee [CL90], defined now for any CR structures $J$ and $J^{\prime}$, and such that $\mu\left(J, J^{\prime}\right)=\mu(J)-\mu\left(J^{\prime}\right)$ when $J$ and $J^{\prime}$ have trivial holomorphic bundle. Then one can prove the following result.
1.3. Theorem. For any CR structures $J$ and $J^{\prime}$ on $X^{3}$ with the same underlying contact structure, one has
$$\nu(J)-\nu\left(J^{\prime}\right)=3 \mu\left(J, J^{\prime}\right) .$$

This is a result which depends only the variations on the invariants $\mu$ and $\nu$, and these variations are given by integration of local terms.

By contrast, the invariant $\nu$ itself is defined as a "renormalization" of the $\eta$ invariants of $X$ for a sequence of metrics converging to the Carnot-Carathéodory metric defined by the CR structure, hence involving non local terms. This explains why it is difficult to relate it to the $\mu$ invariant of Burns-Epstein when the latter is defined.

It would be interesting to have a direct definition of $\nu$ on the CR manifold, analogous to the spectral definition of the $\eta$ invariant, instead of the definition by this limiting process. Once this issue has been settled, our theorem 1.2 will stand as an analogue of the signature formula proven by N. Hitchin for asymptotically real hyperbolic Einstein metrics in dimension 4 [Hit97]. A not-so-close analogue is the Gauss-Bonnet formula discovered by M. T. Anderson in the real case, which includes a contribution of the so-called renormalized volume, a non-local interior contribution And01.

The situation is by far less clear in higher dimension, as there is less proximity between the general asymptotically complex hyperbolic case and the very
special Kähler-Einstein situation. If renormalized characteristic classes were to exist, it seems difficult to extend the methods of proof used in this paper to that case, as they use heavily the integrability of the CR-structure at infinity and the connection this implies with complex geometry.

The paper is organized as follows. In section 2, we study the asymptotics of an asymptotically hyperbolic metric, various adapted connections and their curvatures. This is used to refine our model at infinity, using Kähler geometry: in section 3, given a CR-structure on any manifold $X^{3}$, we construct an explicit approximate metric, which is Kähler-Einstein up to a high order. This involves generalizing the classical Fefferman procedure [Fef76] for complex domains to the abstract CR setting. In section 4, we compare an arbitrary asymptotically complex hyperbolic Einstein metric $g$ with the approximate Kähler-Einstein metric $\bar{g}$ built in the previous sections from the same CR-structure at infinity. Up to gauge modification (action of the diffeomorphism group), the former is shown to be a good approximation of the latter, up to a precise order; this is done in section 5. A useful output is the explicit derivation of all the formally determined terms in the asymptotic expansion of an asymptotically complex hyperbolic Einstein metric in dimension 4.

Unfortunately, this is not good enough to show that the characteristic polynomial (1.3) in the curvature of $g$ has convergent integral since the highest-order term in the difference between $g$ and $\bar{g}$ might cause divergence. In section 6, we show that the integrals converge by a direct method. The Einstein condition implies that both half-Weyl tensors are harmonic. Thus, its negative part has fast enough decay to imply convergence of the $\left|W^{-}\right|^{2}$-term, whereas the positive part can be compared to the positive part of the neighboring approximately Kähler-Einstein metric $\bar{g}$. As $\left|W^{+}\right|^{2}-\frac{1}{24}$ Scal ${ }^{2}$ vanishes at least to high order for such a metric, the integral of the same term for $g$ can be shown to converge.

In the following section 7, we attack the task of computing the value of the integral. We transform it into a boundary integral by using the formulas for characteristic classes of manifolds with boundary and we consider the effect of the highest order term in $g-\bar{g}$. Although it might contribute in the limit at infinity, a careful computation shows it is not the case. Our main result is then that the boundary term may be computed by using the formally determined terms of the Kähler-Einstein metric $\bar{g}$ rather than the asymptotically complex hyperbolic Einstein metric $g$. This enables us to define the invariant $\nu\left(\partial_{\infty} M\right)$ at infinity in full generality, for any CR structure on a 3-dimensional manifold, and to prove theorem 1.2. Finally, in section 8, we investigate the relations between our invariant and the Burns-Epstein invariant $\mu$. We compute the variation of $\nu$ with respect to the complex structure and compare it to that of $\mu$, leading to the proof of theorem 1.3.

Notations. We shall consider hereafter noncompact Riemannian manifolds, usually denoted as $(M, g)$. Their covariant (Levi-Civita) derivatives on any tensor bundle will be denoted by the symbol ∇ and the Riemann, Ricci and scalar curvatures by $R^{g}, \operatorname{Ric}^{g}$ and Scal ${ }^{g}$ (the superscript being sometimes dropped if there is no possible confusion). The sign convention on curvature is $R_{X, Y}=$ $\left[\nabla_{X}, \nabla_{Y}\right]-\nabla_{[X, Y]}$. The divergence $\nabla^{*}=-\operatorname{tr} \nabla$ is the adjoint of ∇ , and the (rough) Laplacian operator on functions or tensors is then $\Delta^{g}=\nabla^{*} \nabla$.

\section*{2. Asymptotics of ACH metrics}

On the 3-sphere $S^{3} \subset \mathbb{R}^{4}$, we denote by $\eta_{0}$ the standard contact form, and $\gamma_{0}$ the metric induced on the contact distribution $\operatorname{ker} \eta$. The complex hyperbolic metric on $\mathbb{C H}^{2}$, with holomorphic sectional curvature normalized to -1, is given in polar coordinates by
$$g_{\mathbb{C} \mathbf{H}^{2}}=d r^{2}+4 \sinh ^{2}(r) \eta^{2}+4 \sinh ^{2}\left(\frac{r}{2}\right) \gamma .$$

More generally, given any pseudo-convex CR-structure on a 3-manifold $X^{3}$, a choice of compatible contact form $\eta$ induces a choice of metric $\gamma(\cdot, \cdot)=d \eta(\cdot, J \cdot)$; from this one can build an asymptotically complex hyperbolic metric on a neighborhood $M=[R, \infty) \times X$ of $X$,
$$g_{0}=d r^{2}+\mathrm{e}^{2 r} \eta^{2}+\mathrm{e}^{r} \gamma .$$
As explained in [Biq00, I.1.B], the curvature of $g_{0}$ is approximated by the curvature of $g_{\mathbb{C} \mathbf{H}^{2}}$ up to order $O\left(\mathrm{e}^{-r / 2}\right)$. This motivates the terminology asymptotically complex hyperbolic metric (ACH in short); a more general and precise definition will be given at the end of the current section. Note here the order $O\left(\mathrm{e}^{-r / 2}\right)$ instead of $O\left(\mathrm{e}^{-r}\right)$ in [Biq00], because we have normalized the holomorphic sectional curvature to -1 instead of -4.

We will need later some calculations on the asymptotics of the metric $g_{0}$. We let $R$ be the Reeb vector field of the contact form $\eta$, defined by
$$R\lrcorner \eta=1, \quad R\lrcorner d \eta=0,$$
and consider some unit vector field $h$ in the contact distribution $H=\operatorname{ker} \eta$. The CR-structure yields an almost complex structure $J$ on $H$, which can be extended to an almost complex structure on $M$ by taking $J \partial_{r}=\mathrm{e}^{-r} R$. We may then consider an adapted $g_{0}$-orthonormal frame $\left(\partial_{r}, \mathrm{e}^{-r} R, \mathrm{e}^{-r / 2} h, \mathrm{e}^{-r / 2} J h\right)$. Finally, we denote by $\nabla^{W}$ the Webster connection on $X$ determined by the choice of the contact form $\eta$. Its torsion induces a trace-free symmetric endomorphism of $H$,
$$T_{R, \cdot}=\left(\begin{array}{cc}
\alpha & \beta \\
\beta & -\alpha
\end{array}\right) .$$

We can extend the Webster connection to $M$ as a $g_{0}$-unitary connection $\widetilde{\nabla}^{W}$ by defining
$$\widetilde{\nabla}^{W} \partial_{r}=\widetilde{\nabla}^{W} \mathrm{e}^{-r} R=0, \quad \widetilde{\nabla}_{\partial_{r}}^{W} \mathrm{e}^{-\frac{r}{2}} h=0 \text { for } h \in H .$$
2.1. Lemma. The Levi-Civita connection of $g_{0}$ is $\nabla=\widetilde{\nabla}^{W}+a$, where $a$ is a 1-form with values in the endomorphisms of $T M$ defined in the $g_{0}$-adapted frame $\left(\partial_{r}, \mathrm{e}^{-r} R, \mathrm{e}^{-r / 2} h, \mathrm{e}^{-r / 2} J h\right)$ by
$$\begin{aligned}
a_{\partial_{r}} & =0, \quad a_{\mathrm{e}^{-r} R}=\left(\begin{array}{cccc}
0 & -1 & & \\
1 & 0 & & \\
& & 0 & -\frac{1}{2} \\
& & \frac{1}{2} & 0
\end{array}\right), \\
a_{\mathrm{e}^{-\frac{r}{2}} h} & =\left(\begin{array}{cccc} 
& -\frac{1}{2} & & 0 \\
\frac{1}{2} & \mathrm{e}^{-r} \alpha & -\mathrm{e}^{-r} \alpha & -\frac{1}{2}-\mathrm{e}^{-r} \beta \\
0 & \frac{1}{2}+\mathrm{e}^{-r} \beta & &
\end{array}\right), \\
a_{\mathrm{e}^{-\frac{r}{2} J h}} & =\left(\begin{array}{ccc} 
& 0 & -\frac{1}{2} \\
0 & -\frac{1}{2}+\mathrm{e}^{-r} \beta & \frac{1}{2}-\mathrm{e}^{-r} \beta \\
\frac{1}{2} & -\mathrm{e}^{-r} \alpha &
\end{array}\right) .
\end{aligned}$$
2.2. Remark. The result of the previous lemma may be re-expressed in the following way:
$$a=a_{0}+\mathrm{e}^{-r} a_{1}$$
where $a_{0}$ is a 1-form having the same coefficients as it has in $\mathbb{C} \mathbf{H}^{2}$ (in particular, $a_{0}$ commutes with $J$ ); the correction term $a_{1}$ depends on the torsion of the Webster connection. This stands also true for all derivatives.

Proof. - The proof is a straightforward calculation, using the fact that, for an orthonormal frame $\left(\xi_{i}\right)$, the Levi-Civita connection can be computed by the formula
$$\left\langle\xi_{k}, \nabla_{\xi_{j}} \xi_{i}\right\rangle=-\frac{1}{2}\left(\left\langle\left[\xi_{i}, \xi_{k}\right], \xi_{j}\right\rangle+\left\langle\left[\xi_{j}, \xi_{k}\right], \xi_{i}\right\rangle+\left\langle\left[\xi_{i}, \xi_{j}\right], \xi_{k}\right\rangle\right) .$$
All the brackets can be expressed in terms of the Webster connection and its torsion, since for $h, h^{\prime} \in H$, one has
$$T_{h, h^{\prime}}=d \eta\left(h, h^{\prime}\right) R,$$
and the other components of the torsion are given by (2.3). \(\square\)

It is proven in [Biq00] that the curvature of $g_{0}$ is approximated up to order $O\left(\mathrm{e}^{-r / 2}\right)$ by the curvature of the model space $\mathbb{C} \mathbf{H}^{2}$; therefore, Ric ${ }^{g_{0}}=-\frac{3}{2} g_{0}+$ $O\left(\mathrm{e}^{-r / 2}\right)$, hence $g_{0}$ is a first approximation solution to the Einstein equation.

More is actually true: the correction term in lemma 2.1 is better than expected and decays like $O\left(\mathrm{e}^{-r}\right)$ instead of $O\left(\mathrm{e}^{-r / 2}\right)$. In order to see this, we first deduce from the previous Lemma:
2.3. Corollary. The Levi-Civita connection of $g_{0}$ and the Webster connection are related by $\nabla=\widetilde{\nabla}^{W}+a$, with
$$\widetilde{\nabla}^{W} a=O\left(\mathrm{e}^{-r}\right),$$
where $O\left(\mathrm{e}^{-r}\right)$ is taken with respect to $g_{0}$. The same is true for all derivatives: they all are of order $O\left(\mathrm{e}^{-r}\right)$.

Proof. - From the decomposition (2.4) of $a$, the only thing to prove is $\widetilde{\nabla}^{W} a_{0}=0$. Actually one can give more intrinsic formulas for $a_{0}$. Denote by $\widetilde{g}$ the hermitian product on $T M$ induced by $g_{0}$ and $J$, which is $\mathbb{C}$-antilinear in its first variable. Then
$$\left(a_{0}\right)_{\mathrm{e}^{-r} R}\left|\left\langle\partial_{r}, \mathrm{e}^{-r} R\right\rangle=J, \quad\left(a_{0}\right)_{\mathrm{e}^{-r} R}\right|_{H}=\frac{1}{2} J,$$
and for any $h \in H$,
$$\left(a_{0}\right)_{\mathrm{e}^{-r / 2} h} \xi=\frac{1}{2}\left(\widetilde{g}\left(\partial_{r}, \xi\right) \mathrm{e}^{-r / 2} h-\widetilde{g}\left(\mathrm{e}^{-r / 2} h, \xi\right) \partial_{r}\right) .$$
Since $J$ is parallel for $\widetilde{\nabla}^{W}$, it follows that $a_{0}$ is parallel too, and this ends the proof. \(\square\)
2.4. Corollary. The curvature of the metric $g_{0}$ defined by (2.2) is approximated up to order $O\left(\mathrm{e}^{-r}\right)$ by that of the complex hyperbolic space ; in particular, one has
$$\operatorname{Ric}^{g}=-\frac{3}{2} g+O\left(\mathrm{e}^{-r}\right) .$$
2.5. Remark. Actually one can compute explicitely the term of order $\mathrm{e}^{-r}$ : it depends on the Webster scalar curvature and on the torsion. From this one may write down a first correction (at order $\mathrm{e}^{-r}$ ) to $g$ in order to get an approximate Einstein metric up to a better order. In sections 3 and 5, we will prove an even better asymptotic expansion for a more precise choice of approximate Einstein metric.

Proof. - This is also a consequence of Lemma 2.1. Indeed, we can write the curvature of the Levi-Civita connection as
$$F=F\left(\widetilde{\nabla}^{W}\right)+d_{\widetilde{\nabla}^{W}} a+\frac{1}{2}[a, a] .$$
Notice first that $F\left(\widetilde{\nabla}^{W}\right)$ actually reduces to $F\left(\nabla^{W}\right)$ : since this is a smooth horizontal 2-form on the boundary, it means that, with respect to the metric $g_{0}$, we have
$$F\left(\widetilde{\nabla}^{W}\right)=O\left(\mathrm{e}^{-r}\right) .$$

Secondly, using (2.4) and corollary 2.3, we get
$$d_{\widetilde{\nabla}{ }^{W}} a+\frac{1}{2}[a, a]=a_{0}\left(T_{\mid H}^{W}\right)+\frac{1}{2}\left[a_{0}, a_{0}\right]+O\left(\mathrm{e}^{-r}\right)$$
where $T^{W}$ is the torsion of the Webster connection. Therefore, we conclude that
$$F=a_{0}\left(T_{\mid H}^{W}\right)+\frac{1}{2}\left[a_{0}, a_{0}\right]+O\left(\mathrm{e}^{-r}\right) .$$
The form $a_{0}$ has constant coefficients equal to those of the model: the term $a_{0}\left(T_{\mid H}^{W}\right)+\frac{1}{2}\left[a_{0}, a_{0}\right]$ actually represents the curvature of $\mathbb{C H}^{2}$, hence this formula implies that the curvature of $g_{0}$ is approximated by that of complex hyperbolic space up to order $O\left(\mathrm{e}^{-r}\right)$. \(\square\)

Laplacians. We close this section by another consequence of corollary 2.3. Given any tensorial bundle $E$ on $X$, we have on it transverse-Webster operators as $\nabla_{R}^{W}$, $\nabla_{h}^{W}$ (for $h$ section of $H$ ). For handling transverse regularity questions, it is important to understand the commutation of their extensions $\widetilde{\nabla}_{R}^{W}$ and $\widetilde{\nabla}_{h}^{W}$ with the standard Laplacian $\Delta_{g_{0}}$ for the metric $g_{0}$ on $M$.

Since $M$ is asymptotically complex hyperbolic, the unit balls in $M$ at infinity look like the unit balls in $\mathbb{C H}^{2}$, and this enables us to define in a standard way Hölder spaces $C^{k, \alpha}$ for the metric $g$. We also need the weighted versions
$$C_{\delta}^{k, \alpha}=\mathrm{e}^{-\delta r} C^{k, \alpha} .$$
Clearly, the Laplacian for $g$ defines an operator
$$\Delta: C_{\delta}^{k+2, \alpha} \rightarrow C_{\delta}^{k, \alpha},$$
and the tangential derivatives give operators
$$\widetilde{\nabla}_{h}^{W}: C_{\delta}^{k+1, \alpha} \rightarrow C_{\delta-\frac{1}{2}}^{k, \alpha}, \widetilde{\nabla}_{R}^{W}: C_{\delta}^{k+1, \alpha} \rightarrow C_{\delta-1}^{k, \alpha},$$
since the norm of $h$ for the metric $g$ is $\mathrm{e}^{r / 2}$, resp $\mathrm{e}^{r}$ for $R$. Hence the bracket $[\Delta, \mathcal{L}]$ loses a priori some weights if $\mathcal{L}$ is any of the above transverse-Webster operators. Although this might put us in a very bad shape, we shall see now that the case is actually better.

We denote by $\mathcal{Q}_{1}$ the algebra of differential operators generated by $\widetilde{\nabla}_{\partial_{r}}^{W}, \widetilde{\nabla}_{\mathrm{e}^{-r} R}^{W}$, $\widetilde{\nabla}_{\mathrm{e}^{-\frac{r}{2}} h}^{W}$ ( $h$ smooth section of $H$ on $X$ ), and linear (zero order) operators $f$ on $M$ such that, for any integer $k$ and sections $h_{1}, \ldots, h_{k}$ of $H, \widetilde{\nabla}_{h_{1}}^{W} \ldots \widetilde{\nabla}_{h_{k}}^{W} f$ is bounded and, for any $\ell>0, \widetilde{\nabla}_{h_{1}}^{W} \ldots \widetilde{\nabla}_{h_{k}}^{W}\left(\widetilde{\nabla}_{\partial_{r}}^{W}\right)^{\ell} f=O\left(\mathrm{e}^{-\frac{r}{2}}\right)$ (in all what follows, these will be series in $\mathrm{e}^{-\frac{r}{2}}$ whose coefficients are smooth functions on the boundary at infinity $X$ ). Let $\mathcal{Q}_{0}$ be the subspace of $\mathcal{Q}_{1}$ containing operators with only tangential derivatives and no zero order term. Clearly,
$$\mathcal{Q}=\mathcal{Q}_{0}+\mathrm{e}^{-\frac{r}{2}} \mathcal{Q}_{1}$$
is an algebra of differential operators. The main interest of this algebra lies in its commutation properties with the transverse-Webster operators or the metric Laplacian of $g_{0}$ :
2.6. Lemma. One has, for $h$ unit section of $H$ on $X$,
$$\begin{aligned}
& {\left[\widetilde{\nabla}_{\partial_{r}}^{W}, \widetilde{\nabla}_{h}^{W}\right]=0,\left[\widetilde{\nabla}_{\partial_{r}}^{W}, \widetilde{\nabla}_{R}^{W}\right]=0,} \\
& {\left[\widetilde{\nabla}_{h}^{W}, \widetilde{\nabla}_{\mathrm{e}^{-r} R}^{W}\right] \in \mathrm{e}^{-\frac{r}{2}} \mathcal{Q}_{1},} \\
& {\left[\widetilde{\nabla}_{h}^{W}, \widetilde{\nabla}_{\mathrm{e}^{-\frac{r}{2} J h}}^{W}\right]=-\widetilde{\nabla}_{\mathrm{e}^{-\frac{r}{2} R}}^{W} \quad \bmod \mathcal{Q} .}
\end{aligned}$$
As a consequence,
$$\left[\Delta_{g_{0}}, \widetilde{\nabla}_{R}^{W}\right] \in \mathcal{Q} \text { and }\left[\Delta_{g_{0}}, \widetilde{\nabla}_{h}^{W}\right]=-2 \nabla_{\mathrm{e}^{-\frac{r}{2}} J h} \widetilde{\nabla}_{\mathrm{e}^{-\frac{r}{2} R}}^{W} \bmod \mathcal{Q} .$$
Proof. - The first commutations properties can be easily checked from the form of the Webster curvature and contact properties of the distribution $H$. It remains to prove the (more interesting) commutation with the metric Laplacian. In a $g_{0}$-orthonormal frame $\left(e_{i}\right)=\left(\partial_{r}, \mathrm{e}^{-r} R, \mathrm{e}^{-\frac{r}{2}} h, \mathrm{e}^{-\frac{r}{2}} J h\right)$, the Laplacian is
$$\Delta=-\sum\left(\left(\nabla_{e_{i}}\right)^{2}-\nabla_{\nabla_{e_{i}} e_{i}}\right)$$
where the last line is obtained from Lemma 2.1: $\nabla=\widetilde{\nabla}^{W}+a_{0}+\mathrm{e}^{-r} a_{1}$ with $a_{1} \in \mathcal{Q}_{1}$ and $\widetilde{\nabla}^{W} a_{0}=0$. From the previous commutations, one sees that the only term outside $\mathcal{Q}$ in $\left[\widetilde{\nabla}_{h}^{W}, \Delta_{g_{0}}\right]$ is
$$\begin{aligned}
{\left[\widetilde{\nabla}_{h}^{W},-\left(\nabla_{\mathrm{e}^{-\frac{r}{2}} J h}\right)^{2}\right] } & =-\nabla_{\mathrm{e}^{-\frac{r}{2}} J h}\left[\widetilde{\nabla}_{h}^{W}, \nabla_{\mathrm{e}^{-\frac{r}{2}} J h}\right]-\left[\widetilde{\nabla}_{h}^{W}, \nabla_{\mathrm{e}^{-\frac{r}{2}} J h}\right] \nabla_{\mathrm{e}^{-\frac{r}{2}} J h} \\
& =\widetilde{\nabla}_{\mathrm{e}^{-\frac{r}{2}} R}^{W} \nabla_{\mathrm{e}^{-\frac{r}{2}} J h}+\nabla_{\mathrm{e}^{-\frac{r}{2}} J h} \widetilde{\nabla}_{\mathrm{e}^{-\frac{r}{2} R}}^{W} \bmod \mathcal{Q} \\
& =2 \nabla_{\mathrm{e}^{-\frac{r}{2}} J h} \widetilde{\nabla}_{\mathrm{e}^{-\frac{r}{2}} R}^{W}+\left[\nabla_{\mathrm{e}^{-\frac{r}{2}} R}, \widetilde{\nabla}_{\mathrm{e}^{-\frac{r}{2}} J h}^{W}\right] \bmod \mathcal{Q} \\
& =2 \nabla_{\mathrm{e}^{-\frac{r}{2}} J h} \widetilde{\nabla}_{\mathrm{e}^{-\frac{r}{2}} R}^{W} \bmod \mathcal{Q} .
\end{aligned}$$
The commutations with $\widetilde{\nabla}_{R}^{W}$ are similar, but easier. \(\square\)

General definition of ACH(E) metrics. We now close this introductory section with a general definition of the Riemannian manifolds which form the main objects of study of this paper. Let $\left(X^{3}, \eta, J\right)$ be a pseudo-convex CR manifold, with associated metric $\gamma$ on the contact distribution. Any metric $g$ on a 4-manifold $M$ such that the complement of a compact set $M-K$ is diffeomorphic to $[R,+\infty[\times X$ and such that
$$g-\left(d r^{2}+\mathrm{e}^{2 r} \eta^{2}+\mathrm{e}^{r} \gamma\right) \in C_{\delta}^{\infty}$$
for some $\delta>0$ will be called an asymptotically complex hyperbolic (ACH in short) manifold.

Moreover, $(M, g)$ is said to be ACHE if $g$ is an Einstein metric. To avoid any confusion, we insist on the fact that ACHE metrics actually are solutions of the Einstein equations; the word 'asymptotic' in the definition only refers to
the complex hyperbolic-like behavior at infinity: each should look like complex hyperbolic space.

From now on and for sake of simplicity, we shall restrict ourselves to smooth ACH metrics induced by smooth CR structures at infinity, and weighted decay control on all derivatives, as it is the case in the definition above. This is because we know from the work of the first author [Biq00] that such metrics can be obtained on the ball from any smooth CR structure close to the standard structure on $\mathbb{S}^{3}$. This provides us with a very large set of metrics to which our results can be applied. Their domain of validity may likely be pushed further to include finite differentiability assumptions only, although this might require a slightly more technical treatment.

\section*{3. Approximately Kähler-Einstein metrics}

Let us recall that any strictly pseudoconvex domain in $\mathbb{C}^{2}$ bears in its interior a complete Kähler-Einstein metric: the Cheng-Yau metric [CY80], whose asymptotics are similar to those of the complex hyperbolic metric (2.1). Fefferman [Fef76] has given a formal high order asymptotic expansion for such a metric, and Lee-Melrose [LM82] proved the complete asymptotic expansion.

More generally, given any CR-structure on a 3 -manifold $X^{3}$, we have at hand the asymptotically complex hyperbolic metric (2.2) of the previous section, given on a neighborhood $[R, \infty) \times X$ by
$$g=d r^{2}+\mathrm{e}^{2 r} \eta^{2}+\mathrm{e}^{r} \gamma .$$
We will now modify this metric in order to get a Kähler-Einstein metric, at least up to a very high order. As in general $X$ is not embedded in $\mathbb{C}^{2}$, we cannot use directly Fefferman's formal construction.

We begin by the construction of the complex structure. This is well-known, but we need the calculation of the first terms.
3.1. Proposition. Given any CR manifold $X^{3}$, one can construct in a neighborhood of $X$ a formal integrable complex structure $J$.

Proof. - Denote by $J_{0}$ the complex structure on the contact distribution, and $R$ the Reeb vector field associated to the contact form $\eta$. Moreover, let $H_{1,0}$ be the (1,0)-vectors in $H$ and $H^{0,1}$ be the (0,1)-forms.

We consider now $M=X \times[R, \infty)$, and we start from the initial almost complex structure on $M$ defined by the formulas
$$J_{0} \partial_{r}=\mathrm{e}^{-r} R,\left.\quad J_{0}\right|_{H}=J_{X} .$$
We now seek a complex structure $J$ differing from $J_{0}$ only on $H$ : the difference is parameterized by a tensor $\phi \in H^{0,1} \otimes H_{1,0}$, such that
$$T_{0,1}^{J}=\left\{X+\phi_{X}, X \in T_{0,1}^{J_{0}}\right\} .$$

The integrability condition $\left[T_{0,1}^{J}, T_{0,1}^{J}\right] \subset T_{0,1}^{J}$ becomes, in terms of $\phi$ and an arbitrary vector $h \in H_{0,1}$,
$$\left[\partial_{r}+i \mathrm{e}^{-r} R, h+\phi_{h}\right] \in(1+\phi) T_{0,1}^{J_{0}} .$$
We perform the calculation at a point $x \in X$, where we suppose that $\nabla^{W} h(x)=0$ for the Webster connection $\nabla^{W}$, and therefore $[R, h]=-T_{R, h}$, where $T$ is the torsion of the Webster connection. As $T_{R,}$ is anti- $J_{0}$-linear on $H$ and therefore defines a map $H_{0,1} \rightarrow H_{1,0}$, we get
$$\left[\partial_{r}+i \mathrm{e}^{-r} R, h+\phi_{h}\right]=-i \mathrm{e}^{-r} T_{R, h}+\partial_{r} \phi_{h}+i \mathrm{e}^{-r}\left[R, \phi_{h}\right] .$$
Using $\left[R, \phi_{h}\right]=\nabla_{R}^{W} \phi_{h}-T_{R, \phi_{h}}$, the integrability condition can be transformed into
$$-i \mathrm{e}^{-r} T_{R, h}+\partial_{r} \phi_{h}+i \mathrm{e}^{-r} \nabla_{R}^{W} \phi_{h}=-i \mathrm{e}^{-r} \phi_{T_{R, \phi},},$$
which we rewrite finally as
$$-\partial_{r} \phi_{h}=i \mathrm{e}^{-r}\left(-T_{R, h}+\nabla_{R}^{W} \phi_{h}+\phi_{T_{R, \phi_{h}}}\right) .$$

Now it becomes clear that we can solve (3.2) by a formal series $\phi=\sum_{j \geqslant 1} \phi_{j} \mathrm{e}^{-j r}$. Indeed, suppose we have a solution up to order $k-1$, then the r.h.s. of (3.2), computed for $\sum_{j<k} \phi_{j} \mathrm{e}^{-j r}$, is at least of order $k$, i.e. of the form $\sum_{j \geqslant k} \mathrm{e}^{-j r} \psi_{j}$, and we can solve the equation at order $k$ by letting
$$\phi_{k}=\frac{1}{k} \psi_{k}$$
and this proves our claim. \(\square\)
3.2. Remark. Formula (3.2) enables us to give easily an explicit formula for the first terms of $\phi$. For example, we have clearly $\phi_{1}=-i T_{R,}$. . Reintroducing this into (3.2), we get that $2 \phi_{2}=i \nabla_{R} \phi_{1}=\nabla_{R} T_{R, . .}$ As a result,
$$\phi=-i T_{R,}, \mathrm{e}^{-r}+\frac{1}{2} \nabla_{R} T_{R,} \mathrm{e}^{-2 r}+\cdots$$
yields the beginning of the series for the complex structure.
We will now construct the approximate Kähler-Einstein metric. Before stating the theorem, we need to recall some formalism for the Webster connection on the CR manifold $X$. We work in a local coframe $\left(\eta, \theta^{1}, \theta^{\overline{1}}\right)$ such that
$$d \eta=i \theta^{1} \wedge \theta^{\overline{1}} .$$
The Webster connection form is a purely imaginary 1-form $\omega_{1}^{1}$, and the Webster torsion $\tau^{1}=\tau_{\overline{1}}^{1} \theta^{\overline{1}}$ is a (0,1)-form: they are defined by
$$d \theta^{1}=\theta^{1} \wedge \omega_{1}^{1}+\eta \wedge \tau^{1} .$$
The Webster curvature $R$ is defined by
$$d \omega_{1}^{1}=R \theta^{1} \wedge \theta^{\overline{1}}+\tau_{, \overline{1}}^{\overline{1}} \wedge \eta-\tau_{, 1}^{1} \wedge \eta,$$
where $D_{, 1}$ (resp. $D_{, \overline{1}}$, or $D_{, 0}$ ) denotes covariant derivative (with respect to the Webster connection) of the tensor field $D$ in the direction of the $(1,0)$ vector dual to $\theta^{1}$ (resp. $\theta^{\overline{1}}$, or the contact form $\eta$ ). The canonical bundle of the CR structure (generated by $\theta^{1} \wedge \eta$ ) is a natural CR holomorphic bundle; it has a canonical connection with curvature $\Omega$ satisfying $\Omega \wedge \eta=0$. More precisely,
$$\Omega=\eta \wedge\left(\left(i R_{, 1} \theta^{1}+\tau_{, \overline{1}}^{\overline{1}}\right)+\left(i R_{, \overline{1}} \theta^{\overline{1}}-\tau_{, 1}^{1}\right)\right) .$$
From this point of view, the complex structure of the filling complex structure defined by (3.3) is determined by the (1,0)-forms
$$\begin{aligned}
& \vartheta^{0}=\mathrm{e}^{-r} d r+i \eta \\
& \left.\vartheta^{1}=\theta^{1}-\phi\right\lrcorner \theta^{1}=\theta^{1}+i \mathrm{e}^{-r} \tau^{1}-\frac{1}{2} \mathrm{e}^{-2 r} \tau_{, 0}^{1}+\cdots
\end{aligned}$$
Therefore, if we see $\Omega$ as a 2-form in the interior, the leading term of its (1,1)-part is
$$\Omega_{0}=\frac{i}{2}\left(\vartheta^{\overline{0}} \wedge\left(i R_{, 1} \theta^{1}+\tau_{, \overline{1}}^{\overline{1}}\right)-\vartheta^{0} \wedge\left(i R_{, \overline{1}} \theta^{\overline{1}}-\tau_{, 1}^{1}\right)\right) .$$
This form decreases as $O\left(\mathrm{e}^{-\frac{3}{2} r}\right)$, but is not closed, since an easy calculation gives
$$d \Omega_{0}=-\frac{i}{2}\left(\Delta R-i\left(\tau_{\overline{1}, 11}^{1}-\tau_{1, \overline{1} \overline{1}}^{\overline{1}}\right)\right) \mathrm{e}^{-r} d r \wedge d \eta+O\left(\mathrm{e}^{-\frac{5}{2} r}\right),$$
where $\Delta$ is the Webster Laplacian. This leads us to define a form
$$\tilde{\Omega}=\Omega_{0}-\frac{i}{2}\left(\Delta R-i\left(\tau_{\overline{1}, 11}^{1}-\tau_{1, \overline{1} \overline{1}}^{\overline{1}}\right)\right) \mathrm{e}^{-r} d \eta$$
which now satisfies
$$d \tilde{\Omega}=O\left(\mathrm{e}^{-\frac{5}{2} r}\right) .$$
3.3. Theorem. In a neighborhood of $X$ there exists a formal Kähler ACH metric $\bar{g}$, which is Einstein up to order $O\left(\mathrm{e}^{-\frac{5}{2} r}\right)$, that is
$$\operatorname{Ric}^{\bar{g}}=-\frac{3}{2} \bar{g}+O\left(\mathrm{e}^{-\frac{5}{2} r}\right) .$$
Moreover, the Kähler form $\omega$ of the metric is given explicitely, up to order $\frac{5}{2}$, by:
$$\omega=i \partial \bar{\partial} f+\frac{4}{3} i \tilde{\Omega}+O\left(\mathrm{e}^{-\frac{5}{2} r}\right),$$
and
$$f=2 r+R \mathrm{e}^{-r}-\frac{2}{3}\left(\frac{R^{2}}{4}-|\tau|^{2}-\frac{\Delta R}{6}+\frac{2 i}{3}\left(\tau_{\overline{1}, 11}^{1}-\tau_{1, \overline{1} \overline{1}}^{\overline{1}}\right)\right) \mathrm{e}^{-2 r} .$$
3.4. Corollary. Up to order $\frac{5}{2}$, one obtains explicitely
$$\begin{aligned}
\omega= & \mathrm{e}^{r}(d r \wedge \eta+d \eta)-\frac{R}{2} d \eta \\
& +\frac{4}{3} i \tilde{\Omega}+\frac{i}{2}\left(R_{, 1} \vartheta^{\overline{0}} \wedge \theta^{1}-R_{, \overline{1}} \vartheta^{0} \wedge \theta^{\overline{1}}\right)-\frac{\Delta R}{2} \mathrm{e}^{-r} d \eta \\
& -\frac{2}{3}\left(\frac{R^{2}}{4}-|\tau|^{2}-\frac{\Delta R}{6}+\frac{2 i}{3}\left(\tau_{\overline{1}, 11}^{1}-\tau_{1, \overline{1} \overline{1}}^{\overline{1}}\right)\right) \mathrm{e}^{-r}(d r \wedge \eta-d \eta),
\end{aligned}$$
where $\vartheta^{0}, \vartheta^{1}$ are defined in formulas (3.4).
3.5. Remark. Actually it is easy to prove that there is a formal development, determined up to order 3, for an additional potential for a solution, as in Fefferman's classical work [Fef76]. However, the development up to order $\frac{5}{2}$ obtained above will be enough for our needs.

Proof. - First we have $\bar{\partial}(2 r)=d r-i \mathrm{e}^{r} \eta$, and therefore
$$i \partial \bar{\partial}(2 r)=i d \bar{\partial}(2 r)=\mathrm{e}^{r}(d r \wedge \eta+d \eta) .$$
Hence the leading term for $g$ actually gives the ACH metric (3.1). Now continue the calculation:
$$d\left(R \mathrm{e}^{-r}\right)=\mathrm{e}^{-r}\left(-R d r+R_{, 0} \eta+R_{, 1} \theta^{1}+R_{, \overline{1}} \theta^{\overline{1}}\right) .$$
Remark that $\theta^{\overline{1}}=\vartheta^{\overline{1}}+O\left(\mathrm{e}^{-\frac{3}{2} r}\right)$, where of course the $O\left(\mathrm{e}^{-\frac{3}{2} r}\right)$ refers to the ACH metric (3.1). Therefore
$$\bar{\partial}\left(R \mathrm{e}^{-r}\right)=\frac{1}{2}\left(-R+i \mathrm{e}^{-r} R_{, 0}\right) \vartheta^{\overline{0}}+\mathrm{e}^{-r} R_{, \overline{1}} \theta^{\overline{1}}+O\left(\mathrm{e}^{-\frac{5}{2} r}\right) .$$
We deduce, keeping terms only up to order $\mathrm{e}^{-2 r}$,
$$\begin{aligned}
\partial \bar{\partial}\left(R \mathrm{e}^{-r}\right)=-\left(R_{, 0} \eta+R_{, \overline{1}} \theta^{\overline{1}}+R_{, 1} \theta^{1}\right) \frac{\vartheta^{\overline{0}}}{2}+\frac{R}{2} i d \eta+\frac{R_{, 0}}{2} \mathrm{e}^{-r}(-d r \wedge \eta+d \eta) \\
-\mathrm{e}^{-r} d r \wedge R_{, \overline{1}} \theta^{\overline{1}}+\mathrm{e}^{-r} R_{, \overline{1} 1} \theta^{1} \wedge \theta^{\overline{1}}+O\left(\mathrm{e}^{-\frac{5}{2} r}\right)
\end{aligned}$$
and therefore
$$\begin{aligned}
i \partial \bar{\partial}\left(R \mathrm{e}^{-r}\right)= & \frac{1}{2}\left(-R d \eta-i \vartheta^{0} \wedge R_{, \overline{1}} \theta^{\overline{1}}+i \vartheta^{\overline{0}} \wedge R_{, 1} \theta^{1}-\mathrm{e}^{-r}(\Delta R) d \eta\right) \\
& +O\left(\mathrm{e}^{-\frac{5}{2} r}\right)
\end{aligned}$$
We consider the metric Kähler metric $g_{0}$ with Kähler form
$$\omega_{0}=i \partial \bar{\partial}\left(2 r+R \mathrm{e}^{-r}\right) .$$
Let us calculate its Ricci tensor. We have a section
$$\sigma=\vartheta^{0} \wedge \vartheta^{1}$$
of the canonical bundle. Remark that
$$i \vartheta^{1} \wedge \vartheta^{\overline{1}}=i\left(\theta^{1} \wedge \theta^{\overline{1}}+\mathrm{e}^{-2 r} \tau^{1} \wedge \tau^{\overline{1}}\right)+O\left(\mathrm{e}^{-4 r}\right) .$$
It follows that, with respect to $g_{0}$, we have
$$|\sigma|^{2}=\mathrm{e}^{-2 r} \frac{1-\mathrm{e}^{-2 r}\left|\tau^{1}\right|^{2}}{e^{r}-\frac{1}{2}\left(R+\Delta R \mathrm{e}^{-r}\right)}\left(1+O\left(\mathrm{e}^{-\frac{5}{2} r}\right)\right),$$
and
$$\ln |\sigma|^{2}=-3 r+\frac{R}{2} \mathrm{e}^{-r}+\Phi \mathrm{e}^{-2 r}+O\left(\mathrm{e}^{-\frac{5}{2} r}\right), \quad \Phi=\frac{R^{2}}{4}-\left|\tau^{1}\right|^{2}+\frac{\Delta R}{2} .$$
On the other hand, we have
$$d \sigma=i d \eta \wedge \vartheta^{1}-\vartheta^{0} \wedge\left(d \theta^{1}+d\left(i \mathrm{e}^{-r} \tau^{1}-\frac{1}{2} \mathrm{e}^{-2 r} \tau_{, 0}^{1}\right)\right) ;$$
the first term is zero, and the second becomes, keeping only terms of type (2,1),
$$d \sigma=-\vartheta^{0} \wedge\left(\theta^{1} \wedge \omega_{1}^{1}+\eta \wedge \tau^{1}+i \mathrm{e}^{-r} d \tau^{1}\right)+O\left(\mathrm{e}^{-\frac{5}{2} r}\right) ;$$
replacing $\theta^{1}$ by $\vartheta^{1}-i \mathrm{e}^{-r} \tau^{1}+O\left(\mathrm{e}^{-\frac{5}{2} r}\right)$, we get
$$d \sigma=\left(-\omega_{1}^{1}-i \mathrm{e}^{-r} \tau_{, 1}^{1}+O\left(\mathrm{e}^{-\frac{5}{2} r}\right)\right) \wedge \sigma,$$
giving us a "connection" form
$$\omega_{K}=-\omega_{1}^{1}-i \mathrm{e}^{-r}\left(\tau_{, 1}^{1}+\tau_{, \overline{1}}^{\overline{1}}\right)+O\left(\mathrm{e}^{-\frac{5}{2} r}\right) .$$
One deduces easily:
$$d \omega_{K}=-R \theta^{1} \wedge \theta^{\overline{1}}+i \vartheta^{0} \wedge \tau_{, 1}^{1}+i \vartheta^{\overline{0}} \wedge \tau_{, \overline{1}}^{\overline{1}}-i \mathrm{e}^{-r} d\left(\tau_{, 1}^{1}+\tau_{, \overline{1}}^{\overline{1}}\right)+O\left(\mathrm{e}^{-\frac{5}{2} r}\right) .$$
Putting together (3.5), (3.6), (3.7) and (3.9), we calculate the Ricci form of the Kähler metric $g_{0}$ :
$$\begin{aligned}
\rho^{\omega_{0}}= & -i \bar{\partial} \partial \ln |\sigma|^{2}-i d \omega_{K} \\
= & -\frac{3}{2} \mathrm{e}^{r}(d r \wedge \eta+d \eta)+\frac{3}{4} R d \eta \\
& +\frac{1}{4}\left(-i \vartheta^{0} \wedge R_{, \overline{1}} \theta^{\overline{1}}+i \vartheta^{\overline{0}} \wedge R_{, 1} \theta^{1}-\mathrm{e}^{-r}(\Delta R) d \eta\right) \\
& +\Phi \mathrm{e}^{-r}(d r \wedge \eta-d \eta) \\
& +\vartheta^{0} \wedge \tau_{, 1}^{1}+\vartheta^{\overline{0}} \wedge \tau_{, \overline{1}}^{\overline{1}}-\mathrm{e}^{-r} d\left(\tau_{, 1}^{1}+\tau_{, \overline{1}}^{\overline{1}}\right)+O\left(\mathrm{e}^{-\frac{5}{2} r}\right)
\end{aligned}$$

Therefore
$$\begin{aligned}
\rho^{\omega_{0}}+\frac{3}{2} \omega_{0}= & -i \vartheta^{0} \wedge R_{, \overline{1}} \theta^{\overline{1}}+i \vartheta^{\overline{0}} \wedge R_{, 1} \theta^{1}-\mathrm{e}^{-r}(\Delta R) d \eta+\Phi \mathrm{e}^{-r}(d r \wedge \eta-d \eta) \\
& +\vartheta^{0} \wedge \tau_{, 1}^{1}+\vartheta^{\overline{0}} \wedge \tau_{\overline{,} \overline{1}}^{\overline{1}}-\mathrm{e}^{-r} d\left(\tau_{, 1}^{1}+\tau_{, \overline{1}}^{\overline{1}}\right)+O\left(\mathrm{e}^{-\frac{5}{2} r}\right) \\
= & -\vartheta^{0} \wedge\left(i R_{, \overline{1}} \theta^{\overline{1}}-\tau_{, 1}^{1}\right)+\vartheta^{\overline{0}} \wedge\left(i R_{, 1} \theta^{1}+\tau_{, \overline{1}}^{\overline{1}}\right) \\
& +\Phi \mathrm{e}^{-r}(d r \wedge \eta-d \eta)-\mathrm{e}^{-r}\left((\Delta R) d \eta+d\left(\tau_{, 1}^{1}+\tau_{, \overline{1}}^{\overline{1}}\right)\right)+O\left(\mathrm{e}^{-\frac{5}{2} r}\right) \\
= & -2 i \tilde{\Omega}+\Phi \mathrm{e}^{-r}(d r \wedge \eta-d \eta)+O\left(\mathrm{e}^{-\frac{5}{2} r}\right) .
\end{aligned}$$
From this formula, we see that $g_{0}$ is a Kähler metric, which is Einstein up to order $O\left(\mathrm{e}^{-\frac{3}{2} r}\right)$. The term of order $\frac{3}{2}$ does not come from a potential in general, since $\Omega$ represents the first Chern class of the canonical bundle of the boundary. However, we can modify easily $\omega_{0}$ in order to kill this term. Indeed, observe that the order $\frac{3}{2}$ term in $\tilde{\Omega}$, that is $\Omega_{0}$, is orthogonal to the leading term (3.5) of the Kähler form (and also to the term of order 1 in (3.6)). This implies that if we define a new Kähler form
$$\omega_{1}=\omega_{0}+\frac{4}{3} i \tilde{\Omega},$$
the metric on the canonical bundle is changed only at order $O\left(\mathrm{e}^{-2 r}\right)$ by the terms of order 2 in $\tilde{\Omega}$, hence Ricci is modified only at the same order. More precisely, we must add a term
$$-\frac{2}{3}\left(\Delta R-i\left(\tau_{\overline{1}, 11}^{1}-\tau_{1, \overline{1} \overline{1}}^{\overline{1}}\right)\right)$$
in formula (3.7) for $\ln |\sigma|^{2}$, which amounts to replace $\Phi$ by
$$\begin{aligned}
\Phi_{1} & =\Phi-\frac{2}{3}\left(\Delta R-i\left(\tau_{\overline{1}, 11}^{1}-\tau_{1, \overline{1} \overline{1}}^{\overline{1}}\right)\right) \mathrm{e}^{-r} \\
& =\frac{R^{2}}{4}-\left|\tau^{1}\right|^{2}-\frac{\Delta R}{6}+\frac{2 i}{3}\left(\tau_{\overline{1}, 11}^{1}-\tau_{1, \overline{1} \overline{1}}^{\overline{1}}\right) .
\end{aligned}$$
Putting things together, we now have
$$\rho^{\omega_{1}}+\frac{3}{2} \omega_{1}=\Phi_{1} \mathrm{e}^{-r}(d r \wedge \eta-d \eta)+O\left(\mathrm{e}^{-\frac{5}{2} r}\right) .$$

It remains to kill the terms of order 2. For this, observe that again the order 2 term $\Phi_{1} \mathrm{e}^{-r}(d r \wedge \eta-d \eta)$ is orthogonal to the leading term (3.5) of the Kähler form, meaning that if we take
$$\begin{aligned}
\omega_{2} & =\omega_{1}-\frac{2}{3} i \partial \bar{\partial}\left(\Phi_{1} \mathrm{e}^{-2 r}\right) \\
& =\omega_{1}-\frac{2}{3} \Phi_{1} \mathrm{e}^{-r}(d r \wedge \eta-d \eta)+O\left(\mathrm{e}^{-\frac{5}{2} r}\right),
\end{aligned}$$
then Ricci is unchanged at order 2, so we obtain
$$\rho^{\omega_{2}}+\frac{3}{2} \omega_{2}=O\left(\mathrm{e}^{-\frac{5}{2} r}\right) .$$

Summarize all the corrections we have done (modulo $O\left(\mathrm{e}^{-\frac{5}{2} r}\right)$ ) by the formula
$$\omega_{2}=\omega_{0}-\frac{2}{3}\left(\rho^{\omega_{0}}+\frac{3}{2} \omega_{0}-i \partial \bar{\partial}\left(\left(\Phi+\Phi_{1}\right) \mathrm{e}^{-2 r}\right)\right) .$$
This defines $\omega_{2}$ as a closed (1,1)-form, which is the Kähler form we were looking for. \(\square\)

\section*{4. Putting the Einstein metric in an adequate gauge}

The goal of this section is to prove that, starting with an asymptotically complex hyperbolic Einstein metric $g$ on a manifold $M^{4}$, with CR-structure $\left(\eta, H, J_{0}\right)$ at infinity $\partial_{\infty} M=X^{3}$, one can approach it by an approximate solution of the Kähler-Einstein equations built in the previous sections.

Let $(M, g)$ be an ACHE manifold in the sense explained at the end of section 2, so that
$$g-\left(d r^{2}+\mathrm{e}^{2 r} \eta^{2}+\mathrm{e}^{r} \gamma\right) \in C_{\delta}^{\infty} .$$
From the work done above, one may endow a collar neighborhood of infinity of the form $\left.X^{3} \times\right] R,+\infty[$ in $M$ with an (integrable at high order) almost complex structure, denoted by $J$. This provides us with an approximate Kähler-Einstein metric $\bar{g}$, up to the order $O\left(\mathrm{e}^{-3 r}\right)$ (or even higher, as already noticed) such that
$$\bar{g}-\left(d r^{2}+\mathrm{e}^{2 r} \eta^{2}+\mathrm{e}^{r} \gamma\right) \in C_{1}^{\infty} .$$
4.1. Lemma. Let $g$ be an asymptotically complex hyperbolic Einstein metric and $\bar{g}$ any highly approximate Kähler-Einstein metric induced around infinity by the same CR-structure. Then, for $R$ large enough, there exists a diffeomorphism $\varphi$ of $\left[R,+\infty\left[\times X\right.\right.$ inducing the identity at infinity such that $\widetilde{g}=\varphi^{*} g$ satisfies
$$\widetilde{g}-\bar{g} \in C_{\delta}^{\infty} \quad \text { and } \quad \delta^{\bar{g}} \varphi^{*} g+\frac{1}{2} d \operatorname{tr}_{\bar{g}} \varphi^{*} g=0 \quad \text { on } \quad[R,+\infty[\times X .$$
Proof. - First, letting $\chi$ be a cut-off function with value 1 in $B\left(R^{\prime}\right)$ and value 0 in $M-B\left(2 R^{\prime}\right)$, the $C_{\delta}^{k, \alpha}$-norm of
$$g-(\chi g+(1-\chi) \bar{g})$$
(for a given pair $k \in \mathbb{N}, \alpha \in] 0,1\left[\right.$ ) may be chosen very small if $R^{\prime}$ is chosen large enough. From now on, we denote by $\bar{g}$ the metric $\chi g+(1-\chi) \bar{g}$, which retains the crucial property of being approximately Kähler-Einstein around infinity, and (up to enlarging $R^{\prime}$ again) has strictly negative Ricci curvature. From [Biq00, Prop. I.4.6], there exists a unique diffeomorphism $\varphi$, approximated at infinity by the identity up to an element of regularity $C^{k+1}$ and order $O\left(\mathrm{e}^{-\delta r}\right)$, such that
$$\delta^{\bar{g}} \varphi^{*} g+\frac{1}{2} d \operatorname{tr}_{\bar{g}} \varphi^{*} g=0$$
and the Lemma is proved. \(\square\)

Together with the Einstein equation $\operatorname{Ric}^{g}+\frac{3}{2} g=0$ (which is of course preserved by the action of diffeomorphisms), $\widetilde{g}=\varphi^{*} g$ is a solution of an elliptic non-linear system of equations, which might be written as
$$\Phi^{\bar{g}}(\widetilde{g}):=\operatorname{Ric}^{\widetilde{g}}+\frac{3}{2} \widetilde{g}+\left(\delta^{\widetilde{g}}\right)^{*}\left(\delta^{\bar{g}} \widetilde{g}+\frac{1}{2} d \operatorname{tr}_{\bar{g}} \widetilde{g}\right)=0$$

The final step of this section is then achieved by showing the
4.2. Proposition. The difference $\widetilde{g}-\bar{g}$ lives in the weighted space
$$\bigcap_{\varepsilon>0} C_{2-\varepsilon}^{\infty} .$$
4.3. Remark. As all arguments below will concern behavior at infinity only, one may consider (e.g. by interpolating between the classical complex hyperbolic metric and $\bar{g}$ ) that both the reference metric $\bar{g}$ and the asymptotically complex hyperbolic Einstein metric $g$ have nonpositive sectional curvature. This has the sole effect that $g$ (hence $\widetilde{g}$ ) solves the Einstein equation, or, equivalently, equation (4.2), up to a compactly supported perturbation only. This convention will be in order throughout the remaining parts of this paper.

Proof. - The linearization of the map $\Phi^{\bar{g}}$ is computed in [Biq00, formula (I.1.9)] and reads:
$$d_{\bar{g}} \Phi^{\bar{g}}(h)=\frac{1}{2}\left(\nabla^{\bar{g}}\right)^{*} \nabla^{\bar{g}} h-\stackrel{\circ}{R}^{\bar{g}}(h)+\frac{1}{2}\left(\operatorname{Ric}^{\bar{g}} \circ h+h \circ \operatorname{Ric}^{\bar{g}}+12 h\right) .$$
From the main results of [Biq00, I.4.B], the basic isomorphism (Proposition I.2.5 of Biq00) shows that $d_{\bar{g}} \Phi^{\bar{g}}$ is an isomorphism in weighted Hölder spaces $C_{\delta}^{k, \alpha}$ for each $(k, \alpha)$, whenever $\bar{g}$ has nonpositive curvature and (in dimension 4) $0<\delta<2$. Moreover, since $\widetilde{g}-\bar{g}$ may be taken to have small norm in $C_{1}^{k, \alpha}$-topology, one may write
$$0=\Phi^{\bar{g}}(\widetilde{g})=\Phi^{\bar{g}}(\bar{g})+d_{\bar{g}} \Phi^{\bar{g}}(\widetilde{g}-\bar{g})+P_{1}(\widetilde{g}-\bar{g}),$$
where $P_{1}$ is a quadratic term in $g-\bar{g}$. From this we deduce
$$d_{\bar{g}} \Phi^{\bar{g}}(\widetilde{g}-\bar{g}) \in C_{2}^{k-2, \alpha} \text { and } \widetilde{g}-\bar{g} \in C_{\delta}^{k, \alpha} .$$
The isomorphism theorem shows then that $\widetilde{g}-\bar{g}$ lives in $C_{2-\varepsilon}^{k, \alpha}$ for each $(k, \alpha)$ and any $\varepsilon>0$. \(\square\)

\section*{5. High-order asymptotic expansion}

The goal of this section is to improve the previous asymptotic expansion for an asymptotically complex hyperbolic Einstein metric $g$. In the previous section, we have shown that, up to diffeomorphism action, its expansion up to order $\mathrm{e}^{-(2-\varepsilon) r}$
$(\varepsilon>0)$ is exactly the same as the one of the (approximately) Kähler-Einstein metric $\bar{g}$. We shall now study what happens at order $\mathrm{e}^{-2 r}$.

We denote by the same letter $g$ the metric that was denoted by $\widetilde{g}$ in the previous section. Hence it satisfies the conclusions of Lemma 4.1 and Proposition 4.2.

Let $u=g-\bar{g}$. From the previous section $u$ lives in the weighted space $C_{2-\varepsilon}^{\infty}$ for any (small) $\varepsilon>0$. Using the notations of the previous section, this shows $P_{1}(u)$ is in $C_{4-2 \varepsilon}^{\infty}$ hence
$$d_{\bar{g}} \Phi^{\bar{g}}(u)+\Phi^{\bar{g}}(\bar{g}) \in C_{2+\delta}^{\infty}, \quad \text { for some } \delta>0 .$$
Note also that the metric $\bar{g}$ is given by a series in $\mathrm{e}^{-\frac{k}{2} r}(k \in \mathbb{N})$ with coefficients smooth in the boundary variables, so that $\Phi^{\bar{g}}(\bar{g})$ may also be taken in $C_{2+\delta}^{\infty}$ with $\delta>0$ (in section 3, we took $\delta=\frac{1}{2}$ ) and this stands also true for all derivatives of any order $\left(\widetilde{\nabla}_{h}^{W}\right)^{k}\left(\widetilde{\nabla}_{R}^{W}\right)^{\ell} \Phi^{\bar{g}}(\bar{g})$.

It has been pointed out in section 2 (Lemma 2.6) that the metric Laplacian $\nabla^{*} \nabla$ of the 0-th order metric $g_{0}=d r^{2}+\mathrm{e}^{2 r} \eta^{2}+\mathrm{e}^{r} \gamma$ enjoys nice commutation properties with the (extended) Webster covariant derivatives $\widetilde{\nabla}^{W}$ in transverse directions. We shall now use this important piece of information to get a refined description of the asymptotic behaviour of $u$. Referring to Lemma 2.6 above, we begin by stating:
5.1. Lemma. Let $L(h)=\stackrel{\circ}{\mathrm{R}}^{\bar{g}}(h)-\frac{1}{2}\left(\operatorname{Ric}^{\bar{g}} \circ h+h \circ \operatorname{Ric}^{\bar{g}}+12 h\right)$. Then the operator $d_{\bar{g}} \Phi^{\bar{g}}=\frac{1}{2} \Delta_{\bar{g}}-L$ enjoys the same commutation properties as the metric Laplacian of $g_{0}$ with respect to the Webster covariant derivatives $\widetilde{\nabla}_{\partial_{r}}^{W}, \widetilde{\nabla}_{R}^{W}$, and $\widetilde{\nabla}_{h}^{W}, h$ being a $\gamma$-unit local section of $H$ on $X$.

Proof. - First of all, $\bar{g}-g_{0}$, hence $\Delta_{\bar{g}}-\Delta_{g_{0}}$, is in $e^{-r} \mathcal{Q}_{1}$. As a result, commutations properties shown for $\Delta_{g_{0}}$ remain valid for $\Delta_{\bar{g}}$. Moreover, the difference between $\frac{1}{2} \Delta_{\bar{g}}$ and $d_{\bar{g}} \Phi^{\bar{g}}$ is the 0-th order term $L$ whose coefficients involve the curvature of $\bar{g}$. From Corollary 2.3, Webster-derivatives of those are $O\left(\mathrm{e}^{-r}\right)$, whence are elements of $\mathrm{e}^{-r} \mathcal{Q}_{1} \subset \mathcal{Q}$. \(\square\)

We now prove the main result of this section:
5.2. Proposition. There exists a smooth section $k$ of the anti- $J_{0}$-invariant symmetric bilinear forms on the contact distribution $H$ on $X$ such that
$$g-\bar{g}-k \mathrm{e}^{-r} \in C_{2+\delta}^{\infty}$$
all for some $\delta>0$. The same is true for all Webster covariant derivatives of any order.

Checking decays at infinity, this result amounts to say that $u=g-\bar{g}$ is the sum of a smooth term of type $u_{\infty} \mathrm{e}^{-2 r}$ and remainder terms of extra decay at infinity (the reader is warned that, in the norms associated to $g$ or $\bar{g}$, any term of the type $k \mathrm{e}^{-r}$ with $k$ defined on $X$ as above is indeed of order $\mathrm{e}^{-2 r}$ ). The
main difficulty of the proof of the Proposition is getting the full $C^{\infty}$ regularity on either the leading term $u_{\infty} \mathrm{e}^{-2 r}$ or the remainder.
Proof. - We shall write $P$ for the linear operator $d_{\bar{g}} \Phi^{\bar{g}}$ and $f=\Phi^{\bar{g}}(\bar{g})$, so that
$$P u=f+P_{1} u \in C_{2+\delta}^{\infty} \text { for } \delta>0,$$
where $P_{1}$ is the non-linear part of the Einstein equations (with its extra gauge fixing terms). Moreover $\left(\widetilde{\nabla}_{R}^{W}\right)^{k}\left(\widetilde{\nabla}_{h}^{W}\right)^{\ell} f$ belongs to $C_{2+\delta}^{\infty}$ for any $k, \ell$, too.
5.3. Sub-lemma. Let $w \in C_{\alpha}^{\infty}$ for some $\alpha>0$. If $P w \in C_{2+\delta}^{\infty}$ then, for any $Q \in \mathcal{Q}$,
$$\left(\partial_{r}+2\right) w \in C_{2+\delta}^{0} \quad \text { and } \quad Q w \in C_{2+\delta}^{\infty} .$$
Proof of the Sub-lemma. - First of all, elementary weight considerations as above show that $w$ lies in $C_{2-\varepsilon}^{\infty}$ for every $\varepsilon>0$. From the commutations properties proved in Lemma 2.6, one has
$$P\left(\widetilde{\nabla}_{R}^{W} w\right)=\widetilde{\nabla}_{R}^{W}(P w)+\left[P, \widetilde{\nabla}_{R}^{W}\right] w \in C_{1+\delta}^{\infty}$$
for some $\delta>0$. Indeed, $\widetilde{\nabla}_{R}^{W}(P w)$ obviously lies in $C_{1+\delta}^{\infty}$ whereas the bracket term preserves weights as it belongs to $\mathcal{Q}$, a subset of the weight-preserving operators. We then get that
$$\widetilde{\nabla}_{R}^{W} w \in C_{1+\delta}^{\infty} .$$
Moreover, it exists $Q \in \mathcal{Q}$ such that, for every $\gamma$-unit $h$ in $H$
$$P\left(\widetilde{\nabla}_{h}^{W} w\right)=\widetilde{\nabla}_{h}^{W}(P w)-2 \widetilde{\nabla}_{\mathrm{e}^{-\frac{r}{2}} J h}^{W} \widetilde{\nabla}_{\mathrm{e}^{-\frac{r}{2}} R}^{W} w+Q w,$$
so that $P\left(\widetilde{\nabla}_{h}^{W} w\right)$, hence $\widetilde{\nabla}_{h}^{W} w$, belongs to $C_{3 / 2+\delta}^{\infty}$ (for both arguments, we recall that the critical weights of $P$ are 0 and 2). Obviously, this implies that $Q w$ lies in $C_{2+\delta}^{\infty}$ for each $Q$ in $\mathcal{Q}$.

Using this control on the transverse derivatives, the fact that $P w \in C_{2+\delta}^{\infty}$ now translates into
$$q(w)=\left(-\partial_{r}^{2}-2 \partial_{r}+A\right) w \in C_{2+\delta}^{\infty}$$
where $A$ is a linear operator on symmetric bilinear forms, obtained as the dominant term in the asymptotic expansion of the Laplace operator and the 0-th order terms in (4.3). This follows from the work done in [Biq00, Section I.2]. The exact expression of $A$ will be of no concern to our purposes; the following information is nonetheless crucial: from [Biq00, Section I.4.B], we know that the smallest eigenvalue of $A$ is equal to 0, and the associated eigen-subbundle is the bundle of anti- $J_{0}$-invariant symmetric bilinear forms on the contact distribution $H$, i.e. the quadratic forms $k$ on $T X$ such that
$$k(R, \cdot)=0, \quad k\left(J_{0} \cdot, J_{0} \cdot\right)=-k(\cdot, \cdot) .$$
The highest critical weights of $P$ are then 2 on this bundle and are larger on its orthogonal complement. This has two consequences: first of all, we get that all components of $w$ that are (pointwise) orthogonal to the eigen-subbundle are
elements of $C_{2+\delta}^{\infty}$ (for some $\delta>0$ ), whereas elementary ordinary differential equations analysis applied to the remaining component shows that there is a symmetric field $w_{\infty}$ on $X$ as above, such that
$$w-w_{\infty} \mathrm{e}^{-2 r} \in C_{2+\delta}^{0} .$$
More precisely, let us project the solution $w \in C_{2-\varepsilon}^{\infty}$ and the control $q(w) \in C_{2+\delta}^{\infty}$, on the eigenbundle of anti- $J_{0}$-invariant symmetric bilinear forms on $H$; using for sake of simplicity the same letters for the projections, we then have $q(w)=$ $-\partial_{r}^{2} w-2 \partial_{r} w$, so that we may write $w=w_{\infty} \mathrm{e}^{-2 r}+w^{\prime}$, with
$$w^{\prime}=e^{-2 r} \int_{\infty}^{r} e^{2 t} \int_{t}^{\infty} q(w) d s$$
obtained by integration along each ray $\{x\} \times\left[R_{0},+\infty\right)$. Then $w^{\prime}$ and $\partial_{r}^{k} w^{\prime}$ (for any $k$ ) are easily seen to be sections of $C_{2+\delta}^{0}$. The control on $\left(\partial_{r}+2\right) w=\left(\partial_{r}+2\right) w^{\prime}$ now follows. \(\square\)

Proof of Proposition 5.2 (continued). - It results from the previous analysis (applied to $w=u=g-\bar{g}$ ) that $u=\mathrm{e}^{-2 r} u_{\infty}+u^{\prime}$, but the tangential regularity on $u_{\infty}$ and $u^{\prime}$ is not yet known. We now prove by induction on $\left(\ell+\ell^{\prime}, \ell\right)$ the following assertion: let $h_{1}, \ldots, h_{\ell}$ be sections of $H$ on $X$, then, for any $Q \in \mathcal{Q}$
$$Q \widetilde{\nabla}_{h_{1}}^{W} \cdots \widetilde{\nabla}_{h_{\ell}}^{W}\left(\widetilde{\nabla}_{R}^{W}\right)^{\ell^{\prime}} u \in C_{2+\delta}^{\infty} .$$
Observe that the order of the derivations here is not important, since they commute up to introducing terms with less derivatives.

Before explaining the induction, let us observe how Proposition 5.2 is a consequence of the assertion. Indeed, it implies that the tangential derivatives of $P u$ are controlled, so that one has, for each $\ell, \widetilde{\nabla}_{h_{1}}^{W} \ldots \widetilde{\nabla}_{h_{\ell}}^{W} q(w) \in C_{2+\delta}^{\infty}$, so by (5.2) one gets $\widetilde{\nabla}_{h_{1}}^{W} \cdots \widetilde{\nabla}_{h_{\ell}}^{W}\left(\widetilde{\nabla}_{R}^{W}\right)^{\ell^{\prime}} u^{\prime} \in C_{2+\delta}^{\infty}$. The regularity of $u_{\infty}$ follows.

We now come back to the induction. The case $\ell+\ell^{\prime}=0$ is the Sub-lemma above. So now fix $\left(\ell, \ell^{\prime}\right)$ and suppose that the result is true for all $\left(\ell_{1}, \ell_{1}^{\prime}\right)$ such that $\ell_{1}+\ell_{1}^{\prime}<\ell+\ell^{\prime}$, or $\ell_{1}+\ell_{1}^{\prime}=\ell+\ell^{\prime}$ and $\ell_{1}<\ell$. Therefore, we control $\ell+\ell^{\prime}$ transverse derivatives for $u$ in $C_{1+\delta}^{\infty}$. As $P_{1}$ is quadratic-or-more with coefficients given by smooth functions on the boundary at infinity, we certainly have also a control of it in $C_{2+\delta}^{\infty}$ for $\ell+\ell^{\prime}$ transverse derivatives of $P_{1} u$. As $P u=f+P_{1} u$ and $f$ is controlled in the best way one can hope, it follows therefore that all $\ell+\ell^{\prime}$ transverse derivatives $P u$ also live in $C_{2+\delta}^{\infty}$. Letting $\xi_{i}=h_{i}$ for $i \leqslant \ell, \xi_{i}=R$ for $i>\ell$, and $\left(\widetilde{\nabla}_{\xi}^{W}\right)^{\ell+\ell^{\prime}}$ for $\widetilde{\nabla}_{\xi_{1}}^{W} \cdots \widetilde{\nabla}_{\xi_{\ell+\ell^{\prime}}}^{W}$, we can write
$$P\left(\left(\widetilde{\nabla}_{\xi}^{W}\right)^{\ell+\ell^{\prime}} u\right)=\left(\widetilde{\nabla}_{\xi}^{W}\right)^{\ell+\ell^{\prime}} P u+\sum_{i=1}^{\ell+\ell^{\prime}} \widetilde{\nabla}_{\xi_{1}}^{W} \cdots \widetilde{\nabla}_{\xi_{i-1}}^{W}\left[P, \widetilde{\nabla}_{\xi_{i}}^{W}\right] \widetilde{\nabla}_{\xi_{i+1}}^{W} \cdots \widetilde{\nabla}_{\xi_{\ell+\ell^{\prime}}}^{W} u .$$
We would like to argue that all the terms in the sum are in $C_{2+\delta}^{\infty}$. For this we have to distinguish two cases from the commutation rules for $P$ in Lemma 5.1, for bracket terms in (5.3),
(i) if $i>\ell$, then in this case $\xi_{i}=R$ and $\left[P, \widetilde{\nabla}_{R}^{W}\right] \in \mathcal{Q}$, so that the corresponding bracket term lies in $C_{2+\delta}^{\infty}$ by the induction hypothesis for $\ell+\ell^{\prime}-1$;
(ii) if $i \leqslant \ell$, then in this case $\xi_{i}=h_{i}$ and we know that
$$\left[P, \widetilde{\nabla}_{h_{i}}^{W}\right]=-2 \nabla_{\mathrm{e}^{-\frac{r}{2}} J h_{i}} \widetilde{\nabla}_{\mathrm{e}^{-\frac{r}{2}} R}^{W} \bmod \mathcal{Q}$$
so that, modulo $\mathcal{Q}$, the bracket term becomes
$$-2 \nabla_{\mathrm{e}^{-\frac{r}{2}} J h_{i}}\left(\widetilde{\nabla}_{\xi_{1}}^{W} \cdots \widetilde{\nabla}_{\xi_{i-1}}^{W} \widetilde{\nabla}_{\mathrm{e}^{-\frac{r}{2}} R}^{W} \widetilde{\nabla}_{\xi_{i+1}}^{W} \cdots \widetilde{\nabla}_{\xi_{\ell+\ell^{\prime}}}^{W} u\right)$$
and the induction hypothesis with $\ell+\ell^{\prime}$ unchanged but a smaller $\ell$ shows that this term has fast decay (remember that $\nabla_{\mathrm{e}^{-\frac{r}{2}} J h_{i}}$ is in $\mathcal{Q}$ ) and therefore the term under consideration in the right-hand side of (5.3) above is again in $C_{2+\delta}^{\infty}$.

We get at the end that each bracket term in (5.3) is in $C_{2+\delta}^{\infty}$, and it follows that $P \widetilde{\nabla}_{h_{1}}^{W} \ldots \widetilde{\nabla}_{h_{\ell}}^{W} u$ also is in $C_{2+\delta}^{\infty}$. Applying the Sub-lemma to $\left(\widetilde{\nabla}_{\xi}^{W}\right)^{\ell+\ell^{\prime}} u$ yields the desired induction statement for $\left(\ell+\ell^{\prime}, \ell\right)$. \(\square\)

When injecting the precise asymptotic expansion of the Kähler-Einstein metric $\bar{g}$, the final output is
5.4. Corollary (asymptotic expansion). Let $(M, g)$ be any asymptotically complex hyperbolic Einstein manifold of dimension 4 with CR-structure at infinity $\left(\eta, H, J_{0}\right)$ on a 3-manifold $X$, and $\bar{g}$ the approximate Kähler-Einstein metric determined by the CR-structure. Then, up to a $C^{k+1}$-diffeomorphism inducing the identity at infinity, $g$ has an asymptotic expansion of the form
$$g=\bar{g}+k \mathrm{e}^{-r}+\text { lower order terms }$$
where $k$ is a anti- $J_{0}$-invariant quadratic form on the contact distribution $H$. The value of $k$ is formally undetermined.

Together with the result of Corollary 3.4, this gives the asymptotic expansion promised in remark 2.5. Once again, the reader must take care of the fact that the term $k \mathrm{e}^{-r}$ grows like $\mathrm{e}^{-2 r}$.

\section*{6. Convergence of the integral}

In this section, we prove the convergence of our integral for any ACHE metric. We will prove the convergence of two terms, the first involving only the antiselfdual Weyl tensor, the second one involving the selfdual Weyl tensor and the scalar curvature. In the Kähler-Einstein case, only the first term occurs and the proof simplifies considerably, as shown by the following:
6.1. Lemma. If $(M, g)$ is an ACH Einstein manifold, then $\left|W^{-}\right|=O\left(\mathrm{e}^{-\delta r}\right)$ for any $\delta<2$. In particular,
$$\int\left|W^{-}\right|^{2}<\infty .$$
6.2. Remark. The behavior of $W^{-}$will be precised further in the course of the proof, see formula (6.2). We will show that the highest-order of the asymptotic expansion of $W^{-}$occurs at a decay $\mathrm{e}^{-2 r}$ and that this term belongs to a specific sub-bundle of the bundle of Weyl curvature tensors (notice that the existence of a an asymptotic expansion up to order $\mathrm{e}^{-\frac{5}{2} r}$ at least flows from the existence of the asymptotic expansion of the metric given in Corollary 5.4). As in the previous section, there are no "logarithmic terms" (or, rather $r^{k} \mathrm{e}-2 r$-terms in our context), as these would be formally determined. As the general CR case cannot be distinguished locally from the embeddable CR case, these terms would necessarily appear in the development of the Kähler-Einstein solution $\bar{g}$. But the critical weight of the complex Monge-Ampère is higher (it is equal to 3) [Fef76] and this prevents the appearance of any such terms at order 2.

Note moreover that a semi-explicit form of the highest-order term in $W^{-}$in the Kähler-Einstein case will be given in Proposition 6.5 after the current lemma.

Proof. - We use the fact that, for an Einstein metric, the Weyl tensor is harmonic as a 2-form with values in the endomorphism of $T M$. Therefore
$$\left(\left(d^{\nabla}\right)^{*} d^{\nabla}+d^{\nabla}\left(d^{\nabla}\right)^{*}\right) W^{-}=0 .$$
By [Biq00, proposition I.3.5], any such harmonic form which is $O\left(\mathrm{e}^{-\left(\delta_{-}+\varepsilon\right) r}\right)$ must be $O\left(\mathrm{e}^{-\delta r}\right)$ for any $\delta<\delta_{+}$, where
$$\delta_{ \pm}=1 \pm \sqrt{1+\lambda}$$
are the critical weights of the associated indicial operator and $\lambda$ is the smallest eigenvalue of the "zero order terms" of the operator $\left(d^{\nabla}\right)^{*} d^{\nabla}+d^{\nabla}\left(d^{\nabla}\right)^{*}$ at infinity (see [Biq00] or [DH01] for details).

This $\lambda$ does not depend on the particular conformal infinity $\gamma$, and can be calculated for the model $\mathbb{C} \mathbf{H}^{2}$. We now restrict to the case of a harmonic antiselfdual form $w$ with values in $\Omega_{-}^{2}$ on $\mathbb{C} \mathbf{H}^{2}$. There is a Weitzenböck formula expressing the difference between the Laplacians $\nabla^{*} \nabla$ and $\left(d^{\nabla}\right)^{*} d^{\nabla}+d^{\nabla}\left(d^{\nabla}\right)^{*}$ as an algebraic operator involving the curvatures of the manifold and of the bundle, see [BL81, theorem 3.10]; in our case, because $W^{-}\left(\mathbb{C H}^{2}\right)=0$, the term involving the curvature of the basis reduces to $\frac{\mathrm{Scal}}{3}$, so we get
$$\left(\left(d^{\nabla}\right)^{*} d^{\nabla}+d^{\nabla}\left(d^{\nabla}\right)^{*}\right) w=\nabla^{*} \nabla w+\frac{\text { Scal }}{3} w+\mathcal{R}(w),$$
where $\mathcal{R}(w)$ is the 2-form with values in the endomorphisms of $T M$ given by
$$\mathcal{R}(w)_{X, Y}=\sum_{1}^{4}\left(\left[R_{e_{j}, X}^{\nabla}, w_{e_{j}, Y}\right]-\left[R_{e_{j}, Y}^{\nabla}, w_{e_{j}, X}\right]\right) .$$
When $w$ takes its values in $\Omega_{-}^{2}$, only the antiselfdual part of the curvatures $R_{e_{j}, X}^{\nabla}$ may give a nonzero result in the equality, which means that only the scalar
curvature and $W^{-}$are involved. Since again $W^{-}\left(\mathbb{C} \mathbf{H}^{2}\right)=0$, this means that we can calculate $\mathcal{R}$ using the constant sectional curvature tensor
$$R_{X, Y}=-\frac{\text { Scal }}{12} X \wedge Y .$$
Now an easy explicit calculation using (6.1) gives actually, for a section $w$ of $\operatorname{Sym}_{0}^{2} \Omega_{-}^{2}$,
$$\mathcal{R}(w)=\frac{\text { Scal }}{6} w .$$

We now look at the Laplacian $\nabla^{*} \nabla$. To state the result of the computation for this term, we first need to decompose the bundle $\Omega_{-}^{2}$ over the boundary: we have the local orthonormal basis
$$\left(e_{1}=\partial_{r}, e_{2}=J e_{1}=\mathrm{e}^{-r} R, e_{3}=\mathrm{e}^{-\frac{r}{2}} h, e_{4}=J e_{3}=\mathrm{e}^{-\frac{r}{2}} J h\right),$$
and this induces a local decomposition
$$\Omega_{-}^{2}=\mathbb{R} \oplus \mathbb{C}$$
with $\mathbb{R}$ generated by $e^{1} e^{2}-e^{3} e^{4}$ (all wedge products are suppressed in the rest of this section), and $\mathbb{C}$ generated by $e^{1} e^{3}+e^{2} e^{4}$ and $e^{1} e^{4}-e^{2} e^{3}$; more intrinsically, $\mathbb{C}$ is isomorphic to the contact distribution $H$ of the boundary (or more precisely its dual $H^{*}$ ). Then inside $\operatorname{Sym}_{0}^{2} \Omega_{-}^{2}$ we find the real 2-dimensional subbundle $\operatorname{Sym}_{0}^{2} \mathbb{C}=\operatorname{Sym}_{0}^{2} H^{*}$, which consists of anti- $\mathbb{C}$-linear endomorphisms of $H^{*}$, or equivalently of $H$ : these are the infinitesimal deformations of the complex structure on $H$.
6.3. Notation. We will denote by $\mathcal{J}$ the bundle of infinitesimal deformations of the complex structure in $H$, seen as a subbundle of $\operatorname{Sym}_{0}^{2} \Omega_{-}^{2}$.
6.4. Claim. The smallest eigenvalue of the zero order term of $\nabla^{*} \nabla$ acting on $\operatorname{Sym}_{0}^{2} \Omega_{-}^{2}$ is $-\frac{\text { Scal }}{2}$. The corresponding eigenspace is $\mathcal{J}$.

First admit the claim: then the smallest eigenvalue of the zero order term of the Laplacian $\left(d^{\nabla}\right)^{*} d^{\nabla}+d^{\nabla}\left(d^{\nabla}\right)^{*}$ is finally
$$\lambda=\frac{\text { Scal }}{3}+\frac{\text { Scal }}{6}-\frac{\text { Scal }}{2}=0 .$$
Therefore $\delta_{+}=2$ and $\delta_{-}=0$, which means that a harmonic section of $\operatorname{Sym}_{0}^{2} \Omega_{-}^{2}$ which goes to 0 at infinity must actually decay as $O\left(\mathrm{e}^{-2 r}\right)$, and the term of order 2 lies in the subbundle $\mathcal{J}$. Apply this to the tensor $W^{-}$of an ACHE metric: for any ACH metric, we certainly have $\left|W^{-}\right|=O\left(\mathrm{e}^{-\varepsilon r}\right)$, and therefore
$$W^{-}=W_{2}^{-} \mathrm{e}^{-2 r}+O\left(\mathrm{e}^{-(2+\varepsilon) r}\right), \quad W_{2}^{-} \in \mathcal{J} .$$

It remains to prove the claim. One can represent the hyperbolic space as a quotient $U_{1,2} / U_{1} U_{2}$. By [Biq00, I,(2.12)], one has to calculate the action of a partial Casimir operator on the representation $\operatorname{Sym}_{0}^{2} \Omega_{-}^{2}$ of the group $U_{1} U_{2}$.

Analogous calculations are performed in [Biq00, I.4.B] or in [DH01], and the details of the present case are left to the reader. \(\square\)

The proof of the lemma is valid also for the approximate Kähler-Einstein metric $\bar{g}$. Therefore, we also have
$$W^{-}(\bar{g})=W_{2}^{-}(\bar{g}) \mathrm{e}^{-2 r}+O\left(\mathrm{e}^{-(2+\varepsilon) r}\right), \quad W_{2}^{-}(\bar{g}) \in \mathcal{J} .$$

Remark that the filling complex structure in $X \times] R,+\infty$ ) and the formally determined part of the Kähler-Einstein metric $\bar{g}$ depend only on the CR structure underlying the pseudohermitian one. Therefore, $W_{2}^{-}(\bar{g})$ is a CR local invariant. From the formula for the metric $\bar{g}$ in Corollary 3.4, we see that it depends only on four (horizontal) derivatives of the CR structure, and linearly only of the fourth derivatives.

By the classical work on CR geometry of Chern and Moser [CM74] (actually going back in that case to Cartan), the only such invariant is the Cartan curvature tensor $Q$, which can be seen also as a section of the bundle $\mathcal{J}$. Therefore we get:
6.5. Proposition. Let $Q$ be the Cartan tensor of the CR structure, seen as an anti-selfdual Weyl-type tensor. Then
$$W_{2}^{-}(\bar{g})=a Q+O\left(\mathrm{e}^{-(2+\varepsilon) r}\right) .$$

The constant $a$ can be determined from section 8. Of course one should also be able to calculate directly the curvature tensor of $\bar{g}$ from the formula of corollary 3.4: this would give another proof of the proposition, and also the value of the constant $a$.

We now turn to the $W^{+}$-term in the integral.
6.6. Lemma. If $(M, g)$ is an ACH Einstein metric, then
$$\int\left|W^{+}\right|^{2}-\frac{1}{24} \text { Scal }^{2}<\infty .$$
Proof. - In the Kähler-Einstein case, one has identically
$$\left|W^{+}\right|^{2}=\frac{1}{24} \mathrm{Scal}^{2}$$
and there is nothing to prove. In the general case, we will use the fact, from corollary 5.4, that an ACH Einstein metric differs from an asymptotically Kähler-Einstein metric $\bar{g}$ up to a term of order $\mathrm{e}^{-2 r}$, namely
$$g=\bar{g}+k \mathrm{e}^{-r}+O\left(\mathrm{e}^{-(2+\varepsilon) r}\right) .$$
Because the volume grows like $\mathrm{e}^{2 r}$, we need to look only at terms of order at most $\mathrm{e}^{-2 r}$. In particular, we can neglect the fact that $\bar{g}$ is Kähler-Einstein only up to order $\mathrm{e}^{-3 r}$ for example.

Because the term $k \mathrm{e}^{-r}$ is only a small perturbation near infinity, the difference between the Weyl tensors of $g$ and $\bar{g}$ depends on the difference $g-\bar{g}$ by a linear
part (the differential $d_{\bar{g}} W$ ) and a quadratic part which has a stronger decay. Therefore,
$$W^{+}(g)=W^{+}(\bar{g})+d_{\bar{g}} W^{+}\left(k \mathrm{e}^{-r}\right)+O\left(\mathrm{e}^{-(2+\varepsilon) r}\right),$$
and the lemma will be proved if we are able to prove that $d_{\bar{g}}\left|W^{+}\right|^{2}\left(k \mathrm{e}^{-r}\right)$ is $O\left(\mathrm{e}^{-(2+\varepsilon) r}\right)$. As the metric $\bar{g}$ is ACH, it is enough to compute $d_{\bar{g}} W^{+}$when $\bar{g}$ is the standard complex hyperbolic metric where of $\mathbb{C} \mathbf{H}^{2}$, the difference with the general terms giving only lower order terms (this is a consequence of Remark 2.2).

The differential of the Weyl tensor is well-known and we extract the following useful facts from [Gau93, 2.5]: for a path of metrics $g_{t}$, the symmetric endomorphism $u_{t}=\left(g_{0}^{-1} g_{t}\right)^{\frac{1}{2}}$ sends the metric $g_{0}$ to the metric $g_{t}$. If we consider the curvatures $R=R\left(g_{t}\right)$ as sections of $\Omega^{2} \otimes \Omega^{2}$, then
$$\dot{R}=\mathcal{R}+\frac{1}{2} \operatorname{ad}_{\dot{g}} R,$$
where $\mathcal{R}$ is the derivative of $u_{t}^{-1} R_{t}$, and
$$\left(\operatorname{ad}_{\dot{g}} R\right)\left(X_{1}, \cdots, X_{4}\right)=-\sum_{1}^{4} R\left(X_{1}, \cdots, \dot{g}\left(X_{i}\right), \cdots, X_{4}\right) .$$
As we are interested only in $d_{\bar{g}}\left|W^{+}\right|^{2}\left(k \mathrm{e}^{-r}\right)$, we will only need the value of the projection $w^{+}=\pi_{\mathcal{W}^{+}} \mathcal{R}$ of $\mathcal{R}$ on $\mathcal{W}^{+}=\operatorname{Sym}_{0}^{2} \Omega_{+}^{2}$ (as $d_{\bar{g}}\left|W^{+}\right|^{2}=d_{\bar{g}}\left|u_{t}^{-1} W^{+}\left(g_{t}\right)\right|^{2}$, the other terms do not contribute).

The variations of the Weyl tensors depend only on the deformation of the conformal structure. This is parameterized by the deformation of $\Omega_{-}^{2}$, given by some $u \in \Omega_{-}^{2} \otimes \Omega_{+}^{2}$, and from [Gau93, (2.5.8)-(2.5.12)],
$$w^{+}=-\frac{1}{2} \Pi d_{+}^{\nabla}\left(d^{\nabla}\right)^{*} u,$$
where $\left(d^{\nabla}\right)^{*} u$ belongs to $\Omega^{1} \otimes \Omega_{+}^{2}$, the operator $d_{+}^{\nabla}$ is the projection of $d^{\nabla}$ on selfdual 2-forms, and $\Pi$ is the projection $\Omega_{+}^{2} \otimes \Omega_{+}^{2} \rightarrow \operatorname{Sym}_{0}^{2} \Omega_{+}^{2}$.

We can now get explicitely this differential. Coming back to the calculation of the Levi-Civita connection in lemma 2.1, we use again the orthonormal frame
$$\left(e_{1}, e_{2}, e_{3}, e_{4}\right)=\left(\partial_{r}, \mathrm{e}^{-r} R, \mathrm{e}^{-r / 2} h, \mathrm{e}^{-r / 2} J h\right) .$$
We will use also the following basis of selfdual and antiselfdual 2-forms:
$$\begin{aligned}
& \omega_{ \pm}^{1}=e^{1} e^{2} \pm e^{3} e^{4}, \\
& \omega_{ \pm}^{2}=e^{1} e^{3} \mp e^{2} e^{4}, \\
& \omega_{ \pm}^{3}=e^{1} e^{4} \pm e^{2} e^{3} .
\end{aligned}$$
The tensor $k$ is given in the basis $\left(e_{3}, e_{4}\right)$ by the tracefree symmetric matrix
$$k=2 \mathrm{e}^{-r}\left(\begin{array}{cc}
a & b \\
b & -a
\end{array}\right) .$$

Infinitesimally, the orthonormal basis $\left(e^{j}\right)$ is transformed into
$$\left(e^{1}, e^{2}, e^{3}+\mathrm{e}^{-2 r}\left(a e^{3}+b e^{4}\right), e^{4}+\mathrm{e}^{-2 r}\left(b e^{3}-a e^{4}\right)\right) .$$
Let us calculate the modification of $\Omega_{-}^{2}$ : the form $\omega_{-}^{2}$ becomes
$$e^{1}\left(e^{3}+\mathrm{e}^{-2 r}\left(a e^{3}+b e^{4}\right)\right)+e^{2}\left(e^{4}+\mathrm{e}^{-2 r}\left(b e^{3}-a e^{4}\right)\right)=\omega_{-}^{2}+\mathrm{e}^{-2 r}\left(a \omega_{+}^{2}+b \omega_{+}^{3}\right),$$
and similarly $\omega_{-}^{3}$ is transformed into $\omega_{-}^{3}-\mathrm{e}^{-2 r}\left(a \omega_{+}^{3}+b \omega_{+}^{2}\right)$ and $\omega_{-}^{1}$ is unchanged; this means that the deformation $k \mathrm{e}^{-r}$ of the metric translates into the tensor
$$u=a \mathrm{e}^{-2 r}\left(\omega_{-}^{2} \omega_{+}^{2}-\omega_{-}^{3} \omega_{+}^{3}\right)+b \mathrm{e}^{-2 r}\left(\omega_{-}^{2} \omega_{+}^{3}+\omega_{-}^{3} \omega_{+}^{2}\right) .$$
From lemma 2.1, an easy calculation gives us the higher order terms of the covariant derivatives of the $\omega_{2}^{ \pm}$:
$$\begin{array}{ll}
\nabla \omega_{+}^{2}=\frac{3}{2} e^{2} \omega_{+}^{3}, & \nabla \omega_{-}^{2}=-\frac{1}{2} e^{2} \omega_{-}^{3}+e^{4} \omega_{-}^{1}, \\
\nabla \omega_{+}^{3}=-\frac{3}{2} e^{2} \omega_{+}^{2}, & \nabla \omega_{-}^{3}=\frac{1}{2} e^{2} \omega_{-}^{2}-e^{3} \omega_{-}^{1} .
\end{array}$$
Using these formulas, we can calculate $\left(d^{\nabla}\right)^{*} u=-\operatorname{tr} \nabla u$, keeping in mind that we can neglect derivatives along the boundary, because these give lower order terms: we get successively
$$\nabla\left(\omega_{-}^{2} \omega_{+}^{2}-\omega_{-}^{3} \omega_{+}^{3}\right)=e^{2}\left(-\omega_{-}^{2} \omega_{+}^{3}-\omega_{-}^{3} \omega_{+}^{2}\right)+e^{4} \omega_{-}^{1} \omega_{+}^{2}+e^{3} \omega_{-}^{1} \omega_{+}^{3},$$
which leads to
$$\left(d^{\nabla}\right)^{*}\left(\omega_{-}^{2} \omega_{+}^{2}-\omega_{-}^{3} \omega_{+}^{3}\right)=0,$$
and similarly,
$$\left(d^{\nabla}\right)^{*}\left(\omega_{-}^{2} \omega_{+}^{3}+\omega_{-}^{3} \omega_{+}^{2}\right)=0 .$$
Therefore it remains, because of the differentiation of $\mathrm{e}^{-2 r}$ with respect to $r$,
$$\begin{aligned}
\left(d^{\nabla}\right)^{*} u & =2 \operatorname{tr} e^{1} u \\
& =2 \mathrm{e}^{-2 r}\left(a\left(e^{3} \omega_{+}^{2}-e^{4} \omega_{+}^{3}\right)+b\left(e^{3} \omega_{+}^{3}+e^{4} \omega_{+}^{2}\right)\right) .
\end{aligned}$$
In a similar way, it is straightforward to calculate $d_{+}^{\nabla}\left(d^{\nabla}\right)^{*} u$. Still restricting to higher order terms, we give only the result:
$$d_{+}^{\nabla}\left(d^{\nabla}\right)^{*} u=3 \mathrm{e}^{-2 r}\left(a\left(-\left(\omega_{+}^{2}\right)^{2}+\left(\omega_{+}^{3}\right)^{2}\right)-b\left(\omega_{+}^{2} \omega_{+}^{3}+\omega_{+}^{3} \omega_{+}^{2}\right)\right) .$$
The important fact here is that $d_{+}^{\nabla}\left(d^{\nabla}\right)^{*} u$ lies in the orthogonal of
$$W^{+}=\frac{\text { Scal }}{6}\left(\omega_{+}^{1}\right)^{2}-\frac{\text { Scal }}{12}\left(\left(\omega_{+}^{2}\right)^{2}+\left(\omega_{+}^{3}\right)^{2}\right),$$
and from this fact we finally deduce that
$$\bar{g}\left(W^{+}, d_{\bar{g}} W^{+}\left(k \mathrm{e}^{-r}\right)\right)=O\left(\mathrm{e}^{(-2+\varepsilon) r}\right)$$
and this ends the proof. \(\square\)

\section*{7. The renormalized integral and the invariant at infinity}

In the previous sections, we showed that the metric $g$ differs from the approximate Kähler-Einstein metric $\bar{g}$ by a term of type $k \mathrm{e}^{-r}$ plus lower order terms living in $C_{2+\varepsilon}^{\infty}(\varepsilon>0)$. Moreover, $k$ is a section of the bundle of quadratic forms on the contact distribution $H$ that are $J_{0}$-anti-invariant, i.e.
$$k\left(J_{0} \cdot, J_{0} \cdot\right)=-k(\cdot, \cdot) .$$
This was the key step to prove that the integral
$$\frac{1}{8 \pi^{2}} \int_{M}\left(3\left|W^{-}\right|^{2}-\left|W^{+}\right|^{2}+\frac{1}{24} \mathrm{Scal}^{2}\right)$$
converges for any asymptotically complex hyperbolic Einstein metric $g$.
The goal of the present section is to make a few steps towards its computation, in terms of a new invariant of the CR structure at infinity, which will be defined below for any CR manifold (even without any filling by an Einstein metric).

Boundary terms of characteristic classes. It will be convenient to rewrite the integral (7.2) in terms of topological invariants together with boundary contributions. In order to do so, we shall need the formula relating the Euler characteristic and signature of a compact domain with boundary with the expected interior integral and local and non-local contributions of the boundary.

In the following formulas, $R$ will always denote the curvature of the 4 -dimensional manifold and, if $D$ is a bounded domain in $M$, the second fundamental form of $\partial D$ will always be defined as $\mathbb{I}=\nabla \mathrm{n}$, n being the outer unit normal, and seen here either as a vector-valued 1-form (rather than as an endomorphism) or as a quadratic form. For 1-forms $\alpha$ and $\beta$, we let $\alpha \wedge \beta=\alpha \otimes \beta-\beta \otimes \alpha$; if $\beta$ is a 2-form, $\alpha \wedge \beta(X, Y, Z)=\alpha(X) \beta(Y, Z)+\alpha(Y) \beta(Z, X)+\alpha(Z) \beta(X, Y)$. We define for a tensor $F$ in $\otimes^{3} T^{*} M$,
$$\mathfrak{S}(F)(X, Y, Z)=F(X, Y, Z)+F(Y, Z, X)+F(Z, X, Y),$$
hence $\alpha \wedge \beta=\mathfrak{S}(\alpha \otimes \beta)$. If $\mu$ and $\nu$ are forms with values in bundles $E$ and $F$, we decide that $\mu \wedge \nu$ is the obviously defined form with values in $E \otimes F$. Last, if $\rho \otimes \sigma$ is a 3-form with values in $\otimes^{3} T M$, we define
$$\mathcal{T}(\rho \otimes \sigma)=\left\langle d \operatorname{vol}_{\partial D}, \sigma\right\rangle \rho .$$
The desired formula for the Euler characteristic reads:
$$\begin{aligned}
\chi(D)= & \frac{1}{8 \pi^{2}} \int_{D}\left(|W|^{2}-\frac{1}{2}\left|\mathrm{Ric}_{0}\right|^{2}+\frac{1}{24} \mathrm{Scal}^{2}\right) d \mathrm{vol}_{D} \\
& +\frac{1}{12 \pi^{2}} \int_{\partial D} \mathcal{T}(\mathbb{I} \wedge \mathbb{I} \wedge \mathbb{I})-\frac{1}{4 \pi^{2}} \int_{\partial D} \mathcal{T}(\mathbb{I} \wedge R)
\end{aligned}$$
where, in the right-hand side, curvature or second forms must be seen as 1- or 2-forms with values in vectors or 2-vectors. The signature formula includes a non-local boundary contribution $\eta(\partial D)$, known as the $\eta$-invariant:
$$\tau(D)=\frac{1}{12 \pi^{2}} \int_{D}\left(\left|W^{+}\right|^{2}-\left|W^{-}\right|^{2}\right) d \operatorname{vol}_{D}+\frac{1}{12 \pi^{2}} \int_{\partial D} \mathfrak{S}(\mathbb{I}(., R(., .) \mathrm{n}))+\eta(\partial D)$$
where curvature is seen here as a 2-form with values in endomorphisms and the second form as a quadratic form.

Definition of the invariant at infinity $\nu(X)$. From the formulas recalled above, our integral in a compact domain $D_{r}$, whose boundary is the distance sphere $S_{r}=\{r\} \times X$ in the bulk manifold $M$, can be written as the sum of a topological contribution $\chi\left(D_{r}\right)-3 \tau\left(D_{r}\right)$ plus boundary integrals. As $r$ goes to infinity, the characteristic numbers remain constant (when $r$ is large enough) and our task will now be to study the sum
$$\begin{array}{rl}
\nu^{g}(r)=-\frac{1}{12 \pi^{2}} \int_{S_{r}} & \mathcal{T}(\mathbb{I} \wedge \mathbb{I} \wedge \mathbb{I})+\frac{1}{4 \pi^{2}} \int_{S_{r}} \mathcal{T}(\mathbb{I} \wedge R) \\
& +\frac{1}{4 \pi^{2}} \int_{S_{r}} \mathfrak{S}(\mathbb{I}(., R(., .) \mathrm{n}))+3 \eta\left(S_{r}, g\right)
\end{array}$$
as the sphere $S_{r}$ grows to infinity. Recall the tensor $R$ in the above formula is the curvature of the bulk manifold and n is the unit normal vector of slices of constant $r$. We know from the previous section that this term converges, but we will show that the limit depends only on the CR-structure on the boundary. More precisely:
7.1. Theorem. If $\bar{g}$ is the asymptotically Kähler-Einstein metric associated to CR-structure on $\partial_{\infty} M=X$, then one has
$$\lim _{r \rightarrow \infty} \nu^{g}(r)-\nu^{\bar{g}}(r)=0 .$$
In particular,
$$\nu(X)=\lim _{r \rightarrow \infty} \nu^{g}(r)=\lim _{r \rightarrow \infty} \nu^{\bar{g}}(r)$$
and the limit is an invariant which depends only on the CR-structure on the boundary at infinity.

This leads us to the general definition of the invariant $\nu$. Indeed, let $X$ be an arbitrary CR manifold of dimension 3 and let $\bar{M}=X \times] R,+\infty$ ) for some $R>0$. The work done in section 6 is independent of topology, or even completeness, of the filling Einstein metric, hence it shows that, if $\bar{g}$ is the approximate Kähler-Einstein metric (up to order $\frac{5}{2}$ ) on $\bar{M}$ constructed in the first sections, the quantity $\nu^{\bar{g}}(r)$ converges as the sphere $S_{r}$ grows to infinity, and the limit is a CR invariant of $X$. Hence we can define:
7.2. Definition. Let $X$ be an arbitrary compact, pseudoconvex CR manifold of dimension 3. Then
$$\nu(X)=\lim _{r \rightarrow \infty} \nu^{\bar{g}}(r),$$
defined with the approximate Kähler-Einstein metric $\bar{g}$ of Theorem 3.3, is an invariant of the CR structure.

Now we can state, as a consequence, the following result, proving Theorem 1.2.
7.3. Corollary. For any asymptotically complex hyperbolic Einstein metric $g$, inducing a CR-structure on the boundary at infinity $\partial_{\infty} M=X$, one has
$$\frac{1}{8 \pi^{2}} \int_{M}\left(3\left|W^{-}\right|^{2}-\left|W^{+}\right|^{2}+\frac{1}{24} \mathrm{Scal}^{2}\right)=\chi(M)-3 \tau(M)+\nu(X) .$$

Proof of theorem 7.1. If we denote by $B(g)$ the local boundary integrand in formula (7.7) computed with the metric $g$, we can write, for $r$ large enough,
$$\begin{aligned}
\int_{S_{r}} B(g)+3 \eta\left(S_{r}, g\right)= & \int_{S_{r}} B(\bar{g})+3 \eta\left(S_{r}, \bar{g}\right) \\
& +\int_{S_{r}}\left(d_{\bar{g}} B\right)(g-\bar{g})+3\left(d_{\bar{g}} \eta\right)(g-\bar{g}) \\
& +\int_{S_{r}} \mathcal{Q}(g-\bar{g}),
\end{aligned}$$
where, as usual, $\mathcal{Q}$ is a quadratic term, i.e. there exists a constant $C>0$ and some $\epsilon>0$ such that, for any $r$ large enough
$$\mathcal{Q}(g-\bar{g}) \leqslant C \mathrm{e}^{-(2+\epsilon) r} .$$
From the work by Burns and Epstein already quoted, the first two terms in the right hand side of (7.8) converge as they depend only on the (approximately) Kähler-Einstein metric $\bar{g}$. Moreover, as $\left|d \mathrm{vol}_{\bar{g}}\right|=O\left(\mathrm{e}^{-2 r}\right), \mathcal{Q}(g-\bar{g})$ has integrals converging to zero, and we are now reduced to show that, under the above assumptions for $g$ and $\bar{g}$,
$$\lim _{r \rightarrow \infty} \int_{S_{r}}\left(d_{\bar{g}} B\right)(g-\bar{g})+3\left(d_{\bar{g}} \eta\right)(g-\bar{g})=0$$
This will yield the proof of Theorem 7.1. To see that the invariant is indeed an invariant of the CR structure, we begin to check (as the reader can easily convince himself by a straightforward computation) that the boundary integral (7.7) for $\bar{g}$ only depends on the formally determined terms in the asymptotic expansion of $\bar{g}$ as the formally undetermined terms are always $O\left(\mathrm{e}^{-3 r}\right)$ and thus do not contribute at infinity. Moreover it is well-known that both the formally determined part of the Kähler-Einstein metric $\bar{g}$ and the complex structure in $X \times] R,+\infty$ ) are invariants of the CR structure at infinity only. The desired property is then proved.

The computations of the limit in Equation (7.10) will be broken into two parts. We consider first the case of the $\eta$-invariant.
7.4. Lemma. One has $\lim _{r \rightarrow \infty}\left(d_{\bar{g}} \eta\right)(g-\bar{g})=0$.

Proof. - The first variation of the $\eta$-invariant is the integral of a local quantity given by the scalar product of the metric variation $g-\bar{g}$ against a quadratic form $t^{\bar{g}}$ depending on the third derivatives of the metric $\bar{g}$ [APS76]:
$$\left(d_{\bar{g}} \eta\right)(g-\bar{g})=\int_{S_{r}}\left\langle t^{\bar{g}}, g-\bar{g}\right\rangle d \operatorname{vol}_{\left(S_{r}, \bar{g}\right)}$$
However, since $\bar{g}$ is asymptotically complex hyperbolic and $g-\bar{g}$ is of order $O\left(\mathrm{e}^{-2 r}\right)$, the only terms that will contribute at infinity are $k \mathrm{e}^{-r}$ ( $k$ as in section 5; recall this term is $\left.O\left(\mathrm{e}^{-2 r}\right)\right)$ and the highest order terms of $\bar{g}$ and $d \operatorname{vol}_{\left(S_{r}, \bar{g}\right)}$. As explained in Remark 2.2, these terms have exactly the same coefficients in a basis adapted to the CR-structure as they would have in the complex hyperbolic space $\mathbb{C} \mathbf{H}^{2}$. Furthermore, the distance spheres are homogeneous under $U(2)$ in the complex hyperbolic space, hence is any curvature quantity as $t^{\mathbb{C} \mathbf{H}^{2}}$. This implies that the restriction of $t^{\bar{g}}$ to the contact distribution $H$ at each point of $S_{r}$ should be (at first order) a multiple of $\gamma$. Its scalar product with $k$ then vanishes and the lemma is proved. \(\square\)

We now manage the local terms in formula (7.10).
7.5. Lemma. One has $\lim _{r \rightarrow \infty} \int_{S_{r}}\left(d_{\bar{g}} B\right)(g-\bar{g})=0$.

Proof. - For sake of simplicity, let $\dot{g}=g-\bar{g}$ and $\dot{R}=d_{\bar{g}} R(\dot{g})$. The first step is provided by the (obvious) computation:
$$\begin{aligned}
-12 \pi^{2}\left(d_{\bar{g}} B\right)(\dot{g})= & \int_{S_{r}}\left(d_{\bar{g}} \mathcal{T}\right)(\dot{g})\left(\mathbb{I}^{\bar{g}} \wedge \mathbb{I}^{\bar{g}} \wedge \mathbb{I}^{\bar{g}}\right)-3 \int_{S_{r}}\left(d_{\bar{g}} \mathcal{T}\right)(\dot{g})\left(\mathbb{I}^{\bar{g}} \wedge R^{\bar{g}}\right) \\
& +\int_{S_{r}} \mathcal{T}\left(\left(d_{\bar{g}} \mathbb{I}\right)(\dot{g}) \wedge \mathbb{I}^{\bar{g}} \wedge \mathbb{I}^{\bar{g}}\right)+\text { circ. permut. } \\
& -3 \int_{S_{r}} \mathcal{T}\left(\left(d_{\bar{g}} \mathbb{I}\right)(\dot{g}) \wedge R^{\bar{g}}\right)-3 \int_{S_{r}} \mathfrak{S}\left(\left(d_{\bar{g}} \mathbb{I}\right)(\dot{g})\left(\cdot, R_{., .}^{\bar{g}} \overline{\mathrm{n}}\right)\right. \\
& -3 \int_{S_{r}} \mathcal{T}\left(\mathbb{I}^{\bar{g}} \wedge \dot{R}\right)-3 \int_{S_{r}} \mathfrak{S}\left(\mathbb{I}\left(\cdot, \dot{R}_{., .} \overline{\mathrm{n}}\right)\right)
\end{aligned}$$
(note that the unit normals $\overline{\mathrm{n}}$ to the spheres $S_{r}$ do not change when passing from $\bar{g}$ to $g$ ). As in the proof of Lemma 7.4, decay considerations show that it is enough to treat every occurrence of $\dot{g}$ as $k \mathrm{e}^{-r}$ and to compute every term in $\bar{g}$ at highest order. Equivalently, one can consider that $\bar{g}$ is the standard complex hyperbolic metric and $k$ is a $J_{0}$-anti-invariant quadratic form on the contact distribution of the standard structure.

Now we perform the calculation using the same notations as in section 6, using the frame $\left(e_{i}\right)$ as in (6.4), the basis of 2-forms $\left(\omega_{ \pm}^{i}\right)$ as in (6.5), and the form (6.6) for $k$.

We shall now show that each of the integrands in formula (7.12) contributes pointwise as 0 in the limit. Two of them are handled easily:
(i) the map $\mathcal{T}$ depends only on the volume form. Since $k$ is tracefree, the first variation of $\mathcal{T}$ vanishes.
(ii) the variation of the second fundamental form (up to highest order term) is given by $-\frac{1}{2} \mathrm{e}^{-r} k$. An easy computation shows that all the terms involving $\left(d_{\bar{g}} \mathbb{I}\right)$ contribute as zero (as $\partial_{r}$ is the normal to the geodesic spheres for the model space as well as the modified metric, the variation of the second fundamental form only depends on the behavior of $k$ along the ray $] R,+\infty[\times\{p\})$.

It remains to study the terms containing first variations of the curvature, which deserve slightly more attention.

In the frame $\left(e_{i}\right)$ given by (6.4), so that $\partial_{r}=e_{1}$, one has
$$\mathbb{I}=e^{2} e_{2}+\frac{1}{2}\left(e^{3} e_{3}+e^{4} e_{4}\right) .$$
We may then explicit the terms involving $\dot{R}$ in (7.12): noting $v=e^{2} \wedge e^{3} \wedge e^{4}$, we obtain
$$\begin{aligned}
\mathcal{T}(\mathbb{I} \wedge \dot{R}) & =v\left\langle e^{2} \wedge e^{3} \wedge e^{4}, e_{2} \wedge \dot{R}_{e_{3}, e_{4}}+\frac{1}{2}\left(e_{3} \wedge \dot{R}_{e_{4}, e_{2}}+e_{4} \dot{R}_{e_{2}, e_{3}}\right)\right\rangle \\
& =v\left(\left\langle e^{3} \wedge e^{4}, \dot{R}_{e_{3}, e_{4}}\right\rangle+\frac{1}{2}\left(\left\langle e^{4} \wedge e^{2}, \dot{R}_{e_{4}, e_{2}}\right\rangle+\left\langle e^{2} \wedge e^{3}, \dot{R}_{e_{2}, e_{3}}\right\rangle\right)\right),
\end{aligned}$$
where here $\dot{R}$ is seen as a 2-form with values in 2-vectors. Similarly, one has
$$\begin{aligned}
\mathfrak{S}\left(\mathbb{I}\left(\cdot, \dot{R}_{., .} e_{1}\right)\right) & =v\left(\mathbb{I}\left(e_{2}, \dot{R}_{e_{3}, e_{4}} e_{1}\right)+\mathbb{I}\left(e_{3}, \dot{R}_{e_{4}, e_{2}} e_{1}\right)+\mathbb{I}\left(e_{4}, \dot{R}_{e_{2}, e_{3}} e_{1}\right)\right) \\
& =v\left(\left\langle e_{2}, \dot{R}_{e_{3}, e_{4}} e_{1}\right\rangle+\frac{1}{2}\left(\left\langle e_{3}, \dot{R}_{e_{4}, e_{2}} e_{1}\right\rangle+\left\langle e_{4}, \dot{R}_{e_{2}, e_{3}} e_{1}\right\rangle\right)\right),
\end{aligned}$$
where now $\dot{R}$ is seen as a 2-form with values in endomorphisms.
As in the previous section, we consider a path of metrics $g_{t}$, and compute with the help of the symmetric endomorphism $u_{t}=\left(g_{0}^{-1} g_{t}\right)^{\frac{1}{2}}$ which sends the metric $g_{0}$ to the metric $g_{t}$. Then one has (see for example [Gau93, 2.5] or the previous section)
$$\dot{R}=\mathcal{R}+\frac{1}{2} \operatorname{ad}_{\dot{g}} R,$$
where $\mathcal{R}$ is the derivative of $u_{t}^{-1} R_{t}$.
In our case, we deform the metrics as Einstein metrics, so that $\mathcal{R}$ reduces exactly to the variation $w$ of the Weyl tensor. Let us decompose $w=w^{+}+w^{-}$
with $w^{ \pm}=d W^{ \pm}(\dot{g})$. From section 6 we know that $w^{+}$lies in the subbundle generated by
$$\left(\omega_{+}^{2}\right)^{2}-\left(\omega_{+}^{3}\right)^{2}, \omega_{+}^{2} \omega_{+}^{3}+\omega_{+}^{3} \omega_{+}^{2} .$$
Moreover the variation $w^{-}$must be a section of the bundle $\mathcal{J}$ introduced in the previous section, as the highest order term of $W^{-}$should stay in the kernel bundle of $\left(d^{\nabla}\right)^{*} d^{\nabla}+d^{\nabla}\left(d^{\nabla}\right)^{*}$ when one passes from $\bar{g}$ to $g$. Hence $w^{-}$lives in the bundle generated by
$$\left(\omega_{-}^{2}\right)^{2}-\left(\omega_{-}^{3}\right)^{2}, \omega_{-}^{2} \omega_{-}^{3}+\omega_{-}^{3} \omega_{-}^{2} .$$

Now let us understand formula (7.13): in that formula, $\dot{R}$ is seen as a 2-form with values in 2-vectors, so we have to add to the variation (7.15) the variation of the musical isomorphism $\Omega^{2}=\Lambda^{2} T M$. Actually, as before, it is easy to check that the contribution of the variation of the musical isomorphism, as well as the contribution of $\operatorname{ad}_{\dot{g}} R$, vanish. Therefore we are reduced to check the vanishing of (7.13) for the tensor $w$, that is of the quantity
$$\left\langle e^{3} \wedge e^{4}, w_{e_{3}, e_{4}}\right\rangle+\frac{1}{2}\left(\left\langle e^{4} \wedge e^{2}, w_{e_{4}, e_{2}}\right\rangle+\left\langle e^{2} \wedge e^{3}, w_{e_{2}, e_{3}}\right\rangle\right) ;$$
since $w$ does not involve $\omega_{ \pm}^{1}$, one has $w_{e_{3}, e_{4}}=0$, and we are reduced to study
$$\begin{aligned}
\left\langle e^{4} \wedge e^{2}, w_{e_{4}, e_{2}}\right\rangle+\left\langle e^{2} \wedge e^{3}, w_{e_{2}, e_{3}}\right\rangle & =\frac{1}{4}\left(\sum_{2}^{3}\left\langle\omega_{+}^{i}, w\left(\omega_{+}^{i}\right)\right\rangle+\sum_{2}^{3}\left\langle\omega_{-}^{i}, w\left(\omega_{-}^{i}\right)\right\rangle\right) \\
& =0 .
\end{aligned}$$

In the same way, we attack formula (7.14): again, all terms vanish, except maybe the one induced by $w$, which we are now going to calculate: using the fact that $w$ is a 2-form with values in orthogonal endomorphisms, (7.14) becomes
$$-\left\langle e_{1}, w_{e_{3}, e_{4}} e_{2}+\frac{1}{2}\left(w_{e_{4}, e_{3}} e_{2}+w_{e_{2}, e_{3}} e_{4}\right)\right\rangle$$
which becomes, using the Bianchi identity for $w$,
$$-\frac{1}{2}\left\langle e_{1}, w_{e_{3}, e_{4}} e_{2}\right\rangle,$$
and this vanishes because $w$ does not involve $\omega_{ \pm}^{1}$. \(\square\)

\section*{8. Relations with the Burns-Epstein invariant}

In the Kähler-Einstein case, on a complex domain, Burns and Epstein [BE90] have identified the boundary term of the integral (1.2) as their invariant $\mu$ of the CR boundary, so that in this case one has
$$\nu=3 \mu+2 .$$

For general CR manifolds with trivial holomorphic bundle (where the Burns-Epstein invariant $\mu$ is still defined from [BE88]) this relation may not hold, and the difference $\nu-3 \mu$ seems difficult to calculate.

We shall give below a first step in this direction. We will prove that the variation of $\nu$ with respect to any deformation of the complex structure on the contact distribution at infinity, is equal to 3 times the variation of the Burns-Epstein invariant with respect to the same deformation. This proves that $\nu$ equals $3 \mu$ up to a constant whose determination involves delicate normalization problems, which are out of the scope of this paper.

Variations of the $\nu$-invariant. We now fix a contact structure $H$ on a manifold $X$ of dimension 3. The set of CR structures compatible to $H$ is contractible, hence one can always relate any two complex structures on $H$ by a path. Here we shall study the infinitesimal variation of $\nu(X)$ when the complex structure varies but the contact structure remains fixed.

We recall a notation: if $J_{0}$ is a complex structure on $H$, the set of deformations of $J_{0}$ is the set of sections of the bundle of anti- $\mathbb{C}$-linear endomorphisms of $\left(H, J_{0}\right)$, already encountered in section 6. Any element of this space may be described as a linear map sending the space of (0, 1)-vectors (for $J_{0}$ ) into the space of (1, 0)-vectors, extended on the whole of $T H \otimes \mathbb{C}$ by its conjugate. As a result, we will sometimes denote any such element $E$ in $\mathcal{J}$ as $E_{\overline{1}}^{1}$, its expression in any frame $Z_{1}$ of the (1, 0)-vectors in $H$ and the corresponding coframe $\vartheta^{1}$.
8.1. Theorem. Let $J_{0}$ a compatible complex structure on the contact distribution $H$ of a contact 3-manifold $X$. Then $\nu(X, H, J)$ is a smooth function in $J$ around $J_{0}$. Moreover, if $E$ is a section of $\mathcal{J}$ and $J(t)$ is a curve of complex structures on $H$ with $J(0)=J_{0}, J^{\prime}(0)=E$, then
$$\frac{d}{d t}(\nu(X, H, J(t)))_{\mid t=0}=-\frac{3}{8 \pi^{2}} \int_{X}\langle Q, E\rangle$$
where $Q$ is the Cartan tensor of the CR structure defined by ( $H, J$ ) and $\langle\cdot, \cdot\rangle$ the induced Hermitian scalar product.
8.2. Remark. As the Cheng-Lee relative invariant $\mu\left(J, J^{\prime}\right)$ has the same derivative (up to a factor 3), this result implies Theorem 1.3.
8.3. Remark. As the Cartan tensor is CR-covariant, the above expression depends a priori on the choice of a contact form only in a change of scale in the choice of the Hermitian metric on $H$, in the volume form $\eta \wedge d \eta$ and in the Cartan tensor $Q$. When put together, their behaviors with respect to the choice of $\eta$ exactly cancel, thus the integral provides a CR-invariant.

Proof. - Let $M=\left[R_{0},+\infty\right) \times X$ and for each $t \geqslant 0$, denote by $J(t)$ and $\bar{g}(t)$ the extended complex structure and Kähler-Einstein metric (formally determined up to order 2) defined on $] 2 R,+\infty) \times X$ by section 3. If $\hat{g}$ is a fixed metric on $\left[R_{0}, 2 R\right] \times X$, then one may find for each $t \geqslant 0$ a smooth metric $g(t)$ on $\left[R_{0},+\infty\right) \times X$ such that
$$\left.\left.g(t)=\hat{g} \text { on }\left[R_{0}, R\right] \times X \text { and } g(t)=\bar{g}(t) \text { on }\right] 2 R,+\infty\right) \times X .$$
Then, for each $t \geqslant 0$ and $r>2 R$,
$$\nu^{\bar{g}(t)}(r)=-(\chi-3 \tau)\left(\left[R_{0}, r\right) \times X\right)+\int_{\left[R_{0}, r\right) \times X} \beta(g(t))+F(\hat{g})$$
where $\beta(g(t))$ is the characteristic polynomial in the curvature of $g(t)$ corresponding to $\chi-3 \tau$ and $F(\hat{g})$ is a fixed boundary term depending only on the choice of $\hat{g}$ on $\left\{R_{0}\right\} \times X$. Hence,
$$\frac{d}{d t}\left(\nu^{\bar{g}(t)}(r)\right)_{\mid t=0}=\int_{\left[R_{0}, r\right) \times X} \frac{d}{d t} \beta(g(t)) .$$
From classical Chern-Weil theory, there exists an (explicitely known) 3-form $\alpha$ in the curvature of $g(0)$ and infinitesimal variation of the Levi-Civita connections of $g(t)$ at $t=0$ such that $\frac{d}{d t} \beta(g(t))=d \alpha$. As $g(t)$ is independent of $t$ on $\left[R_{0}, R\right] \times X$, this yields:
$$\frac{d}{d t}\left(\nu^{\bar{g}(t)}(r)\right)_{\mid t=0}=\int_{\{r\} \times X} \alpha .$$
As the form $\alpha$ is locally computable from $g(0)$ and $g^{\prime}(0)$ (and a finite number of derivatives thereof), the convergence as $r$ goes to infinity is uniform and
$$\frac{d}{d t}(\nu(X, H, J(t)))_{\mid t=0}=\lim _{r \rightarrow \infty} \int_{\{r\} \times X} \alpha$$
We now determine the precise form of $\alpha$ which will be suitable for our needs. As one takes $r>2 R, \alpha$ can be computed on $S_{r}$ from the characteristic polynomial for $3 c_{2}-\left(c_{1}\right)^{2}$ rather than from $\beta$ (this amounts to restrict polynomials on the Lie algebra $\mathfrak{s o}(4)$ to the smaller $\mathfrak{u}(2))$.

Using Newton's sums $s_{i}(A)=\operatorname{tr}\left(A^{i}\right)$, this polynomial is known to be equal to $\frac{1}{8 \pi^{2}}\left(3 s_{2}-\left(s_{1}\right)^{2}\right)$. Let $\Omega(t)_{i}^{j}$ be the $\mathfrak{u}(2)$-valued curvature 2-form of $g(t)$ in a local frame $\left(S_{0}, S_{1}\right)$, generating the (1, 0)-vectors for $J(t)$, obtained from Gram-Schmidt orthonormalization of $\left(\partial_{r}-i e^{-r} R, Z=X-i J(t) X\right)$. Then,
$$\beta(g(t))=\frac{1}{8 \pi^{2}}\left(3 \Omega(t)_{i}^{j} \wedge \Omega(t)_{j}^{i}-\Omega(t)_{i}^{i} \wedge \Omega(t)_{j}^{j}\right)$$
(with the usual summation conventions), and, letting $\Omega=\Omega(0)$,
$$\alpha=\frac{1}{4 \pi^{2}}\left(3 \phi_{i}^{j} \wedge \Omega_{j}^{i}-\phi_{i}^{i} \wedge \Omega_{j}^{j}\right)$$
where $\phi$ is the matrix-valued first variation at $t=0$ of the Levi-Civita connections.

The work done in sections 2 and 6 shows that the curvature of $\bar{g}(0)$ may be decomposed into 3 contributions: a dominant term given by the coefficients of the Riemann curvature tensor of $\mathbb{C} \mathbf{H}^{2}$ expressed in the orthonormal basis $\left(S_{0}, S_{1}\right)$, a first perturbation at order $\mathrm{e}^{-2 r}$ (originating from the term $W_{2}^{-}$in $W^{-}$studied in section 6), and further terms of decay $\mathrm{e}^{-\frac{5}{2} r}$ at least. In the meanwhile, analogous conclusions for the Levi-Civita connections, hence for $\phi$, may be dragged from Lemma 2.1 and Corollary 2.3 in section 2.

We now draw several useful conclusions from these remarks: first of all, the contribution in the limit (8.4) of the fastest-decay terms in the curvature form is zero. Moreover, as our metric is Kähler-Einstein, the expression (8.6) can be rewritten as
$$\alpha=\frac{1}{4 \pi^{2}}\left(3 \phi_{i}^{j} \wedge \Omega_{j}^{i}-\frac{3}{2} i \phi_{i}^{i} \wedge \omega\right)$$
where $\omega$ here stands for the Kähler form of $\bar{g}(0)$.
We can now study the contributions of the two other terms in the curvature $\Omega$. First of all, it is expected that the contribution of the highest order term in the curvature is zero, because the standard CR structure is a critical point of the Burns-Epstein invariant. As we expect our invariant to be strongly related to their, it would be no surprise that its derivative at the standard metric of the complex hyperbolic space is zero. This is indeed easily checked: the action of curvature of the complex hyperbolic space on (1, 0)-vectors is best described as
$$R_{\xi, \eta}^{\mathbb{C H}^{2}}=-M_{\xi, \eta}+\frac{1}{2} \omega \otimes i I d$$
where the endomorphism-valued 2-form $M$ is
$$Z \longmapsto M_{\xi, \eta}(Z)=\frac{1}{2}\left(g_{\mathbb{C} \mathbf{H}^{2}}(\eta, Z) \xi^{1,0}-g_{\mathbb{C} \mathbf{H}^{2}}(\xi, Z) \eta^{1,0}\right) .$$
Injecting into (8.7), it remains
$$\alpha=\frac{1}{4 \pi^{2}}\left(-3 \phi_{i}^{j} \wedge M_{j}^{i}+3 \phi_{i}^{j} \wedge\left(\Omega^{(2)}\right)_{j}^{i}\right)+o\left(\mathrm{e}^{-2 r}\right)$$
where $\Omega^{(2)}$ denotes the difference between the curvature $\Omega$ and the model curvature 2-form $\Omega^{\mathbb{C} \mathbf{H}^{2}}$ of the complex hyperbolic space, and $M_{i}^{j}$ is the endomorphism-valued 2-form $M$ seen in matrix form.

We now show that $\phi_{i}^{j} \wedge M_{j}^{i}$ yields an exact form, thus contributing as zero when integrating $\alpha$. Using a local coframe $\left(s^{0}, s^{1}\right)$ of $(1,0)$-forms dual to the orthonormal frame $\left(S_{0}, S_{1}\right)$, one gets
$$\phi_{i}^{j} \wedge M_{j}^{i}=\frac{1}{2}\left(\phi_{0}^{0} \wedge s^{0} \wedge s^{\overline{0}}+\phi_{1}^{1} \wedge s^{1} \wedge s^{\overline{1}}+\phi_{1}^{0} \wedge s^{1} \wedge s^{\overline{0}}+\phi_{0}^{1} \wedge s^{0} \wedge s^{\overline{1}}\right) .$$

This may be transformed as follows. For any metric in the family $\{\bar{g}(t)\}_{t \geqslant 0}$, one has
$$\left\{\begin{array}{l}
d s^{0}=\Phi_{0}^{0} \wedge s^{0}+\Phi_{1}^{0} \wedge s^{1} \\
d s^{1}=\Phi_{0}^{1} \wedge s^{0}+\Phi_{1}^{1} \wedge s^{1}
\end{array}\right.$$
where $\Phi$ is the antihermitian matrix-valued Levi-Civita connection 1-form of $\bar{g}(t)$. Notice then that $\phi_{i}^{j}=\left(\Phi_{i}^{j}\right)^{\prime}(0)$. Hence, taking the derivative of Equations (8.9) with respect to $t$ at $t=0$ yields expressions for any $\phi_{a}^{b} \wedge s^{a}$ in terms of $\dot{s}^{a}$ and $\Phi_{a}^{b} \wedge \dot{s}^{b}$, where $\dot{s}^{c}$ denotes $\left(s^{c}\right)^{\prime}(0)$. Easy computations using (8.9) a second time for barred indices (and the antihermitian character of $\Phi$ ) lend eventually to
$$-2 \phi_{i}^{j} \wedge M_{j}^{i}=\dot{s}^{0} \wedge s^{\overline{0}}+\dot{s}^{1} \wedge s^{\overline{1}}-d s^{\overline{0}} \wedge \dot{s}^{0}-d s^{\overline{1}} \wedge \dot{s}^{1}=d\left(\dot{s}^{0} \wedge s^{\overline{0}}+\dot{s}^{1} \wedge s^{\overline{1}}\right)$$
which is the expected exact term-the reader may check that this is a globally defined 3-form by chasing its variation under a frame change from $Z$ to $\mathrm{e}^{i u} Z$. Thus,
$$\alpha=\frac{3}{4 \pi^{2}} \phi_{i}^{j} \wedge\left(\Omega^{(2)}\right)_{j}^{i}+(\text { exact terms })+o\left(\mathrm{e}^{-2 r}\right) .$$
It then remains to study the contribution of the dominant term in $\Omega^{(2)}$, which we know to be the highest-order term in $W^{-}$. As this term is $O\left(\mathrm{e}^{-2 r}\right)$ and must be evaluated against $\phi$, only the zeroth-order terms in $\phi$ will contribute. Section 2 yields
$$\phi=\frac{i}{\sqrt{2}}\left(\begin{array}{cc}
0 & -E_{1}^{\overline{1}} \theta^{1} \\
E_{\overline{1}}^{1} \theta^{\overline{1}} & q_{1}^{1}
\end{array}\right)+o(1)$$
where the first row (column) is the $\left\{\partial_{r}, R\right\}$-complex line and the second one corresponds the $(1,0)$-part of $H$, generated by an orthonormal frame $Z_{1}$ with associated coframe $\theta^{1}$, and $q_{1}^{1}$ is the first variation of the Webster connection induced by the variation of $J$ at infinity. From the definition of $\mathcal{J}$, only the non-diagonal terms have a non-zero contribution against $W_{2}^{-}$. Since $W_{2}^{-}=a Q$ (where $Q$ is the Cartan tensor, see section 6), this finally proves
$$\lim _{r \rightarrow \infty} \int_{\{r\} \times X} \alpha=\text { const. } \int_{X}\langle Q, E\rangle .$$
The constant can be set by comparing with the case of a domain in $\mathbb{C}^{2}$. As every computation done above is local, one should not be able to distinguish this special case from the more general (ACHE) one. The previous work of Burns and Epstein [BE90] implies that variations of our invariant equal three times the variations of the Burns-Epstein invariant for domains, and the variations of the latter one with respect to the complex structure have been computed by in Cheng and Lee [CL90], from which the constant may be borrowed. This enables us to conclude the proof of Theorem 8.1. \(\square\)
8.4. Corollary. For each contact structure $H$ on $X$, there is a constant $a(H)$ such that $\nu(X, H, J)=3 \mu(X, H, J)+a(H)$.

We have proved above that $\nu$ equals $3 \mu$ up to an unknown constant in each component of the set of contact structures on all possible 3-dimensional oriented manifolds. Giving a better result might be a difficult task. To give an idea of the problem, one can describe our approach as a CR analogue of what the Atiyah-Patodi-Singer index theorem implies for the determination of the $\eta$-invariant, whereas Burns and Epstein's is linked to Chern-Simons theory. As is well-known, the $\eta$-invariant and its Chern-Simons counterpart (lifted from $\mathbb{R} / \mathbb{Z}$ to $\mathbb{R}$ ) differ by normalization constants whose determination is unclear. The constant appearing in the difference between $\nu$ and $\mu$ may be evidence of an analogous phenomenon.

Acknowledgments. The first author thanks M. Rumin for explaining him the subtleties of the Burns-Epstein invariant, the second author thanks G. Lebeau for his decisive comments, and both are grateful to G. Carron, V. Kharlamov and T.R. Ramadas for some useful discussions about this work.

\section*{References}
\begin{itemize}
\item[] [And01] M. T. Anderson, $L^{2}$ curvature and volume renormalization of AHE metrics on 4-manifolds, Math. Res. Lett. 8 (2001), 171-188.
\item[] [APS76] M. F. Atiyah, V. K. Patodi, and I. M. Singer, Spectral asymmetry and Riemannian geometry III, Math. Proc. Camb. Phil. Soc. 79 (1976), 71-99.
\item[] [BE88] D. M. Burns, Jr. and C. L. Epstein, A global invariant for three-dimensional CRmanifolds, Invent. Math. 92 (1988), 333-348.
\item[] [BE90] D. Burns and C. L. Epstein, Characteristic numbers of bounded domains, Acta Math. 164 (1990), 29-71.
\item[] [Bes87] A. L. Besse, Einstein manifolds, Springer-Verlag, Berlin, 1987.
\item[] [Biq00] O. Biquard, Métriques d'Einstein asymptotiquement symétriques, Astérisque, vol. 265, Soc. math. France, 2000.
\item[] [BL81] J.-P. Bourguignon and H. B. Lawson, Jr., Stability and isolation phenomena for Yang-Mills fields, Comm. Math. Phys. 79 (1981), no. 2, 189-230.
\item[] [Bla94] J. Bland, Contact geometry and CR structures on $S^{3}$, Acta Math. 172 (1994), no. 1, 1-49.
\item[] [CL90] J.-H. Cheng and J. M. Lee, The Burns-Epstein invariant and deformation of CR structures, Amer. J. Math. 60 (1990), 221-254.
\item[] [CY80] S. Y. Cheng and S. T. Yau, On the existence of a complete Kähler metric on noncompact complex manifolds and the regularity of Fefferman's equation, Comm. Pure Appl. Math. 33 (1980), no. 4, 507-544.
\item[] [CM74] S. S. Chern and J. Moser, Real hypersurfaces in complex manifolds, Acta Math. 133 (1974), 219-271; Erratum, Acta Math. 150 (1983), 297.
\item[] [DH01] E. Delay and M. Herzlich, Ricci curvature in the neighborhood of rank-one symmetric spaces, J. Geom. Anal. 11 (2001), 571-586.
\item[] [Eps92] C. L. Epstein, CR-structures on three-dimensional circle bundles, Invent. Math. 109 (1992), no. 2, 351-403.
\item[] [EMM91] C .L. Epstein, R. B. Melrose, and G. A. Mendoza, Resolvant of the Laplacian on strictly pseudoconvex domains, Acta Math. 167 (1991), 1-106.
\end{itemize}
[Fef76] C. L. Fefferman, Monge-Ampère equations, the Bergman kernel, and geometry of pseudoconvex domains, Ann. Math. (2) 103 (1976), 395-416.
[Gau93] P. Gauduchon, Variétés riemanniennes autoduales (d'après C. H. Taubes et al.), Astérisque (1993), no. 216, Exp. No. 767, 4, 151-186, Séminaire Bourbaki, Vol. 1992/93.
[Hit97] N. J. Hitchin, Einstein metrics and the eta-invariant, Boll. Un. Mat. Ital. B (7) 11 (1997), no. 2, suppl., 95-105.
[Lem92] L. Lempert, On three-dimensional Cauchy-Riemann manifolds, J. Amer. Math. Soc. 5 (1992), no. 4, 923-969.
[LM82] J. M. Lee and R. Melrose, Boundary behaviour of the complex Monge-Ampère equation, Acta Math. 148 (1982), 159-192.

IRMA, CNRS et Université Louis Pasteur, 7 rue René Descartes, F-67084 Strasbourg Cedex, France

Département des Sciences Mathématiques, Géométrie-Topologie et Algèbre, UMR 5030 CNRS et Université Montpellier II, Pl. E. Bataillon, F-34095 Montpellier Cedex 5, France
