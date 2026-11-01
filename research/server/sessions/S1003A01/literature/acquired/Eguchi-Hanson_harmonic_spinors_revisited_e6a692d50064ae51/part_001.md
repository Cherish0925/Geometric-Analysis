---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Eguchi-Hanson harmonic spinors revisited]

---
source_file: 2309_08453.pdf
converter: mathpix
format: mmd
---

\title{
EGUCHI-HANSON HARMONIC SPINORS REVISITED
}

\author{
GUIDO FRANCHETTI AND KIRILL KRASNOV
}

\begin{abstract}
We revisit the problem of determining the zero modes of the Dirac operator on the Eguchi-Hanson space. It is well known that there are no normalisable zero modes, but such zero modes do appear when the Dirac operator is twisted by a $U(1)$ connection with $L^{2}$ normalisable curvature. The novelty of our treatment is that we use the formalism of spin- $c$ spinors (or spinors as differential forms), which makes the required calculations simpler. In particular, to compute the Dirac operator we never need to compute the spin connection. As a result, we are able to reproduce the known normalisable zero modes of the twisted Eguchi-Hanson Dirac operator by relatively simple computations. We also collect various different descriptions of the Eguchi-Hanson space, including its construction as a hyperkähler quotient of $\mathbb{C}^{4}$ with the flat metric. The latter illustrates the geometric origin of the connection with $L^{2}$ curvature used to twist the Dirac operator. To illustrate the power of the formalism developed, we generalise the results to the case of Dirac zero modes on the Ricci-flat Kähler manifolds obtained by applying Calabi's construction to the canonical bundle of $\mathbb{C} P^{n}$.
\end{abstract}

Contents
1. Introduction ..... 2
2. Eguchi-Hanson space as a Kähler and hyperkähler manifold ..... 3
2.1. EH as a line bundle ..... 4
2.2. Equal standing coordinates ..... 5
2.3. Harmonic 2-forms ..... 6
2.4. $U(1)$ connection with $L^{2}$ harmonic curvature ..... 7
2.5. Hyperkähler quotient ..... 8
3. Dirac zero modes on the Eguchi-Hanson space ..... 9
3.1. No Dirac zero modes on EH ..... 9
3.2. The canonical spin- $c$ structure ..... 10
3.3. Computing the action of the Dirac operator on spin- $c$ spinors ..... 11
3.4. Computation of $\partial^{*}$ ..... 11
3.5. Spin- $c$ Dirac operator on a Kähler manifold ..... 12
3.6. Practical way of computing the Dirac operator on a Kähler manifold ..... 12
3.7. Zero modes of the twisted Dirac operator on EH ..... 13
3.8. Normalisability ..... 14
4. The general case ..... 14
4.1. Calabi's metric on $\mathcal{O}(-n-1)$ ..... 14
4.2. Rewriting in terms of "svmmetrical" coordinates ..... 15
4.3. $U(1)$ connection with $L^{2}$ harmonic curvature ..... 17
4.4. Zero modes of the twisted Dirac operator on $\mathcal{O}(-n-1)$ ..... 19
5. Discussion ..... 20
Acknowledgements ..... 21
Appendix A. The geometry of $\mathbb{C}^{2}$ ..... 21
A.1. The geometry of $S U(2)$ ..... 21
A.2. The geometry of $\mathbb{C}^{2}$ ..... 22
Appendix B. Calabi's construction ..... 26
B.1. The Chern connection ..... 26
B.2. Calabi's construction ..... 26
References ..... 29

\section*{1. Introduction}

The Dirac operator and its spectrum, in particular the spectrum of its zero modes, are of great importance and interest in both differential geometry and theoretical physics. In relation to the former, the vanishing theorem due to Lichnerowicz states that there are no harmonic spinors on compact manifolds with positive scalar curvature. When the dimension of the space of harmonic spinors is not zero, it turns out to depend on the metric, [12], and is not a topological invariant of the manifold. There are also beautiful results pertaining to eigenvalue estimates for the Dirac operator and the relation between this and Killing spinors, see e.g. [6] for an authoritative exposition of all these results. In physics, harmonic spinors are important in the context of the Kaluza-Klein programme, see e.g. [18], [19], where harmonic spinors on the internal space correspond to massless particles in the physical space. For all these reasons, harmonic spinors have been studied extensively, and there is a great body of literature available on the subject.

In the context of Riemannian geometry, one is usually interested in spinors and harmonic spinors defined on compact Riemannian manifolds. However, one can also consider non-compact spaces, in particular gravitational instantons, as is the case in this paper. In this case the relevant notion is that of normalisable, more precisely square integrable, also known as $L^{2}$, harmonic spinors. The non-compact case has also been studied, and appropriate index formulae have been developed, see in particular [16]. More recently, there has been a renewed interest in such a setup, see [13] and [4], in the context of geometric models of matter [1].

In this paper we revisit the problem of determining the zero modes of the (twisted) Dirac operator on the Eguchi-Hanson (EH) space [3]. This problem has been explicitly solved, as a subcase of a more general computation, in [4]. The novelty of our treatment in this paper is that, given that EH is a Kähler manifold, we can describe spinors as spin- $c$ spinors. Indeed, any almost complex manifold $M$ carries a canonical spin- $c$ structure, in which the bundle of spinors is identified with the space of differential forms $\Lambda^{0, \bullet}(M)$. The natural Dirac operator on $M$ is $\sqrt{2}\left(\bar{\partial}+\bar{\partial}^{*}\right)$. On a Kähler manifold, this operator coincides with the Dirac operator defined by the lift of the Levi-Civita connection to the spinor bundle. This fact allows us to reduce the necessary computations to elementary operations involving the action of $\bar{\partial}, \bar{\partial}^{*}$ on the space $\Lambda^{0, \bullet}(M)$.

The operator $\sqrt{2}\left(\bar{\partial}+\bar{\partial}^{*}\right)$ on EH admits no normalisable zero modes, so to get an interesting problem it needs to be further twisted by a $U(1)$ connection. Up to integer multiples, there is a unique $U(1)$ connection with square integrable curvature, and it is this connection that we use for the twisting. To elucidate the geometric meaning of this connection, we illustrate how it arises from the construction of EH as a hyperkähler reduction of $\mathbb{H}^{2}$, which we review and further detail in this paper. One of the main results of this paper is the simple explicit expression (3.41) for the EH zero modes. This should be compared with the much more involved expressions in the literature [4]. The computations that lead to this result are also quite elementary, and take not more than a page of text, again in a favourable contrast with the other existing treatments.

To illustrate the power of the formalism that we have developed, we study the generalisation of the problem to the case of the Calabi metric on the total space of the line bundle $\mathcal{O}(-n-1)$ over $\mathbb{C P}^{n}$. As it is well known, the EH metric is the simplest metric in this family and corresponds to $n=1$. We find it interesting to observe that most of the properties of EH extend to the general case, and that the latter can be handled with essentially the same techniques as those used for EH.

Another intriguing result obtained here is that, for all values of $n$, the $U(1)$ connection with $L^{2}$ curvature used to twist the Dirac operator coincides with the simplest Dirac zero mode of the untwisted operator. The corresponding relation in the EH case is (2.49). Of course it is only possible to appreciate this fact by making use of the formalism of spinors as differential forms as we do here.

The organisation of this paper is as follows. We start, in Section 2, by giving several descriptions of EH as a Kähler and eventually as a hyperkähler manifold. We first describe it as the space obtained from the Calabi construction of a Ricci flat metric on the total space of the canonical line bundle over a Kähler manifold with non-zero scalar curvature. We then perform
a change of coordinates that puts the base and fibre coordinates of the Calabi construction on equal footing. This puts the EH metric in the form (2.25), which is the most convenient one for spinor computations. We then discuss various harmonic 2-forms on EH, and in particular the unique (up to scale) harmonic 2-form with $L^{2}$ curvature, as well as its potential. We show that this 2-form is intimately related to the exterior derivative of the (metric dual of the) Killing vector field generating the $U(1)$ isometric action on the fibres. Finally, we describe the EH metric as the hyperkähler quotient of the flat metric on $\mathbb{H}^{2}=\mathbb{C}^{4}$. We were unable to find the details of this construction, in the amount necessary to compare to our other description (2.25), in the literature, so we spell them out here. We find that the $U(1)$ connection on EH with $L^{2}$ curvature arises naturally as the $U(1)$ connection on the total space of a circle bundle over EH obtained as the level set of the hyperkähler reduction.

In Section 3 we determine the zero modes of the twisted Dirac operator on the EH space. We first recall why the untwisted operator admits no normalisable zero modes and review, to the extent necessary for our purposes, results about spin- $c$ spinors and their relation to the usual Dirac spinors. We then explain how to calculate the spin-c Dirac operator in practice. The key point here is that on a Kähler manifold, by using the spinors as differential forms approach, it is never necessary to compute derivatives of the metric. Instead, computations only involve taking exterior derivatives and metric contractions of the relevant differential forms. This method is much more efficient than the usual approach, where spinors are treated as column vectors on which the $\gamma$-matrices act, and which requires the explicit computation of the spin connection. Finally, we solve the problem of finding the Dirac zero modes on the EH space, and obtain the explicit simple expression (3.41) for the resulting harmonic spinors.

In section 4 we generalise our results to the case of spinors on the total space of the canonical bundle over $\mathbb{C P}^{n}$. We close the paper with some concluding remarks as well as two Appendices. In the first one we review the description of $\mathbb{C}^{2}$ as the total space of a line bundle over $\mathbb{C P}^{1}$. The second one reviews Calabi's construction.

\section*{2. Eguchi-Hanson space as a Kähler and hyperkähler manifold}

The Eguchi-Hanson (EH) metric is a hyperkähler metric defined on a 4-manifold diffeomorphic to the cotangent bundle of $S^{2}$. It was introduced in [3], where the metric is given in bi-axial Bianchi IX form
$$g=\left(1-\frac{\kappa}{r^{4}}\right)^{-1} \mathrm{~d} r^{2}+\frac{r^{2}}{4}\left(1-\frac{\kappa}{r^{4}}\right) \eta_{3}^{2}+\frac{r^{2}}{4}\left(\eta_{1}^{2}+\eta_{2}^{2}\right) .$$
Here $\left(\eta_{i}\right)$ are left-invariant 1-forms on $\operatorname{SU}(2)$, see (A.1), and the parameter $\kappa$ is a positive constant. Substituting $u^{2}=r^{2}\left(1-\left(\frac{\kappa}{r^{4}}\right)\right)$ shows that the metric is regular at $r=\kappa^{1 / 4}$ provided that $\psi \in[0,2 \pi), \theta \in[0, \pi], \phi \in[0,2 \pi)$. The topology of a hypersurface $\Sigma_{r}$ of fixed $r>\kappa^{1 / 4}$ is that of a circle bundle, with the circle fibre parametrised by $\psi$ and the base $S^{2}$ parametrised by $(\theta, \phi)$. If $\psi$ had its usual range of $4 \pi, \Sigma_{r}$ would be the total space $S^{3}$ of the Hopf fibration, but due to the reduced range we have instead $\Sigma_{r} \simeq S^{3} / \mathbb{Z}_{2}$. The level set $r=\kappa^{1 / 4}$ is a 2-sphere known as a bolt [8]. Asymptotically $g$ approaches the ( $\mathbb{Z}_{2}$-quotient of the) metric of Euclidean 4-space. Therefore, EH gives a resolution of the singularity of the $\mathbb{R}^{4} / \mathbb{Z}^{2}=\mathbb{C}^{2} / \mathbb{Z}^{2}$ orbifold. In general, a metric with an asymptotic volume growth equal to that of $E^{4}$ is known as asymptotically locally Euclidean, or ALE.

The form (2.1) emphasises the structure of EH as a real manifold with cohomogeneity one under the action of $S U(2) / \mathbb{Z}_{2}$. There are several other useful descriptions of EH, which emphasise its complex structure. We are going to review the ones that are important for our purposes.

First, EH is a Kähler-Einstein manifold. One description that makes this clear describes EH as the total space of a complex line bundle over $\mathbb{C P}^{1}$, with complex coordinates $(w, \zeta)$ parametrising the base and fibre. Such a construction is a special case of the more general construction in [2] of a Ricci-flat Kähler metric on the total space of the canonical line bundle over a Kähler-Einstein manifold. A second description that we need trades the "asymmetrical" $(w, \zeta)$ coordinates for coordinates $\left(z_{1}, z_{2}\right)$ of equal standing, which play a similar role to the global coordinates of $\mathbb{C}^{2}$ and make the similarities between the two manifolds apparent. For
comparison, the analogous descriptions of $\mathbb{C}^{2}$ as a real cohomogeneity one manifold and as a line bundle are reviewed in Appendix A. Finally we review (and make explicit) the description of EH as a hyperkähler quotient of $\mathbb{C}^{4}$ with its flat metric. This is of interest to us because it exhibits the $U(1)$ connection with $L^{2}$ curvature that we use for the twist of the Dirac operator as arising geometrically, in the total space of a certain line bundle over EH. The 5-dimensional total space in question is the level set of the hyperkähler quotient construction.
2.1. EH as a line bundle. The paper [2] describes two constructions leading to Kähler-Einstein metrics on the total space of a complex line bundle over a Kähler manifold. Applied to $\mathbb{C} P^{n}$, the first construction leads to a family of Ricci-flat Kähler metrics on the total space of the canonical line bundle $K=\mathcal{O}(-n-1) \rightarrow \mathbb{C} P^{n}$, the second one to a family of hyperkähler metrics on $T^{*} \mathbb{C} P^{n}$. For $n=1, \mathcal{O}(-2) \simeq T^{*} \mathbb{C} P^{1}$ and both constructions result in the same metric, which is in fact the EH one. The first construction is reviewed in Appendix B.2. Here we apply it to the case of the canonical bundle $K$ over $M=\mathbb{C} P^{1}$ with the Fubini-Study metric. In this case $K$ is simply the cotangent bundle $\Lambda^{1,0}\left(\mathbb{C} P^{1}\right)$. It is well known that line bundles over $\mathbb{C} P^{1}$ are classified by their Chern number and $K$ has Chern number -2.

In terms of the inhomogeneous coordinate $w$, the Fubini-Study metric on $\mathbb{C} P^{1}$ takes the form
$$g_{\mathbb{C} P^{1}}=\frac{4|\mathrm{~d} w|^{2}}{\left(1+|w|^{2}\right)^{2}},$$
and is isometric to the round metric on the 2-sphere of unit radius. The corresponding Kähler form is
$$\omega_{\mathbb{C} P^{1}}=\frac{2 i \mathrm{~d} w \wedge \mathrm{~d} \bar{w}}{\left(1+|w|^{2}\right)^{2}}=\frac{i}{2} e \wedge \bar{e}=\text { vol }$$
where vol is the Riemannian volume element with the natural orientation as a complex manifold, and $e$ is the unitary section of $K$ given by
$$e=\frac{2 \mathrm{~d} w}{1+|w|^{2}}$$

The metric (2.2) is Einstein with scalar curvature $s=2$, hence the Ricci form $\rho_{\mathbb{C} P^{1}}$, Kähler form $\omega_{\mathbb{C} P^{1}}$ and curvature $\mathrm{d} \alpha$ of the Chern connection $\alpha$ on $K$, see Appendix B.1, are related by
$$\rho_{\mathbb{C} P^{1}}=\omega_{\mathbb{C} P^{1}}=-i \mathrm{~d} \alpha .$$
It is convenient to set
$$\alpha=2 i a,$$
where
$$a=\frac{1}{2 i} \frac{\bar{w} \mathrm{~d} w-w \mathrm{~d} \bar{w}}{1+|w|^{2}}=\operatorname{Im}\left(\frac{\bar{w} \mathrm{~d} w}{1+|w|^{2}}\right) .$$

We now apply the construction of [2], as described in [17]. Thus, as shown in Appendix B.2, if $\zeta$ is a coordinate on the fibres of $K$ and we define
$$\begin{aligned}
\theta & =\mathrm{d} \zeta+2 i \zeta a \\
\omega & =2\left(u \omega_{\mathbb{C} P^{1}}+i u^{\prime} \theta \wedge \bar{\theta}\right)
\end{aligned}$$
where $u$ is a function of $|\zeta|^{2}$ only, then $K$ with Kähler form (2.9) is Ricci-flat Kähler provided that
$$2 u u^{\prime}=1 \Rightarrow u=\sqrt{\kappa+|\zeta|^{2}},$$
for $\kappa$ an integration constant. The associated Kähler form and metric are
$$\begin{aligned}
\omega & =2 u \omega_{\mathbb{C} P^{1}}+i u^{-1} \theta \wedge \bar{\theta} \\
g & =2 u g_{\mathbb{C} P^{1}}+2 u^{-1}|\theta|^{2}
\end{aligned}$$

It is convenient to rescale $\zeta \rightarrow \zeta / 8, \kappa \rightarrow \kappa / 64$, getting
$$\begin{aligned}
\omega & =\frac{i}{8}\left(\left(|\zeta|^{2}+\kappa\right)^{1 / 2} e \wedge \bar{e}+\left(|\zeta|^{2}+\kappa\right)^{-1 / 2} \theta \wedge \bar{\theta}\right) \\
g & =\left(|\zeta|^{2}+\kappa\right)^{1 / 2} \frac{|\mathrm{~d} w|^{2}}{\left(1+|w|^{2}\right)^{2}}+\left(|\zeta|^{2}+\kappa\right)^{-1 / 2} \frac{1}{4}|\mathrm{~d} \zeta+2 i \zeta a|^{2}
\end{aligned}$$

Equation (2.14) clearly displays EH as a non-trivial complex line bundle over $\mathbb{C} P^{1}$ with a twisted product metric on the total space. The $S U(2)$ and line bundle structure of equations (2.1), (2.14) should be compared with the corresponding expressions for $\mathbb{C}^{2}$, given by (A.10) and (A.28). We now check that (2.14) is indeed the same metric as (2.1). Switching to polar coordinates $\zeta=R e^{i \chi}$ in the fibres gives
$$g=\left(R^{2}+\kappa\right)^{1 / 2} \frac{|\mathrm{~d} w|^{2}}{\left(1+|w|^{2}\right)^{2}}+\frac{1}{\left(R^{2}+\kappa\right)^{1 / 2}} \frac{R^{2}}{4}\left(\frac{\mathrm{~d} R^{2}}{R^{2}}+(\mathrm{d} \chi+2 a)^{2}\right) .$$
Making the coordinate change $r^{2}=R$ shows that (2.15) asymptotically becomes the flat metric on $\mathbb{C}^{2} / \mathbb{Z}_{2}$, cfr. (A.33). This suggests defining
$$r^{2}=\left(R^{2}+\kappa\right)^{1 / 2},$$
which gives
$$g=\left(1-\frac{\kappa}{r^{4}}\right)^{-1} \mathrm{~d} r^{2}+r^{2} \frac{|\mathrm{~d} w|^{2}}{\left(1+|w|^{2}\right)^{2}}+\frac{r^{2}}{4}\left(1-\frac{\kappa}{r^{4}}\right)(\mathrm{d} \chi+2 a)^{2} .$$
Further setting $w=\cot \left(\frac{\theta}{2}\right) \mathrm{e}^{i \phi}$,
$$\chi=\psi-\phi,$$
gives
$$\frac{|\mathrm{d} w|^{2}}{\left(1+|w|^{2}\right)^{2}}=\frac{\eta_{1}^{2}+\eta_{2}^{2}}{4}, \quad a=\left(\frac{1+\cos \theta}{2}\right) \mathrm{d} \phi, \quad \mathrm{~d} \chi+2 a=\eta_{3}$$
so that we recover (2.1). The difference between (2.18) and (A.35) is due to the different range $\psi \in[0,4 \pi)$ for the $S U(2)$ orbits in $\mathbb{C}^{2}$ and $\psi \in[0,2 \pi)$ for the $S U(2) / \mathbb{Z}_{2}$ orbits in EH .

If we introduce the frame
$$e_{1}=\frac{1}{2}\left(\kappa+|\zeta|^{2}\right)^{1 / 4} e, \quad e_{2}=\frac{1}{2}\left(\kappa+|\zeta|^{2}\right)^{-1 / 4} \theta,$$
the metric and Kähler form take the flat-space form
$$\begin{aligned}
\omega & =\frac{i}{2}\left(e_{1} \wedge \bar{e}_{1}+e_{2} \wedge \bar{e}_{2}\right), \\
g & =\left|e_{1}\right|^{2}+\left|e_{2}\right|^{2} .
\end{aligned}$$
2.2. Equal standing coordinates. The simplest expression for the $\mathbb{C}^{2}$ metric is of course $\left|\mathrm{d} z_{1}\right|^{2}+\left|\mathrm{d} z_{2}\right|^{2}$ where the two coordinates $\left(z_{1}, z_{2}\right)$ have equal standing. In the case of $\mathbb{C}^{2}$ the bundle coordinates $(w, \zeta)$ are related to $\left(z_{1}, z_{2}\right)$ by (A.26). Essentially, $w=z_{1} / z_{2}$ is an inhomogeneous coordinate on the base of the line bundle $\mathbb{C}^{2} \backslash\{0\} \rightarrow \mathbb{C} P^{1}$ while $\zeta$ parametrises the $\mathbb{C}$ fibre. In the case of $\mathbb{C}^{2}$ we have $|\zeta|=\sqrt{\left|z_{1}\right|^{2}+\left|z_{2}\right|^{2}}=r$, while for $\mathrm{EH}|\zeta|=R \approx r^{2}$. This suggests to define
$$\left(z_{1}, z_{2}\right)=\frac{\sqrt{\zeta}}{\sqrt{1+|w|^{2}}}(w, 1), \quad(w, \zeta)=\left(\frac{z_{1}}{z_{2}},\left(\left|z_{1}\right|^{2}+\left|z_{2}\right|^{2}\right) \frac{z_{2}}{\bar{z}_{2}}\right) .$$
One calculates
$$2 \mathrm{~d} z_{1}=\frac{\sqrt{\zeta}}{\sqrt{1+|w|^{2}}} e+\frac{w}{\sqrt{\zeta} \sqrt{1+|w|^{2}}} \theta, \quad 2 \mathrm{~d} z_{2}=\frac{1}{\sqrt{\zeta} \sqrt{1+|w|^{2}}} \theta-\frac{\bar{w} \sqrt{\zeta}}{\sqrt{1+|w|^{2}}} e$$
with inverse
$$e=\frac{2}{|\zeta|} \frac{\bar{z}_{2}}{z_{2}}\left(z_{2} d z_{1}-z_{1} d z_{2}\right), \quad \theta=2 \frac{z_{2}}{\bar{z}_{2}}\left(\bar{z}_{1} d z_{1}+\bar{z}_{2} d z_{2}\right)$$
leading to
$$g=\frac{1}{s}\left(F\left|z_{1} \mathrm{~d} z_{2}-z_{2} \mathrm{~d} z_{1}\right|^{2}+F^{-1}\left|\bar{z}_{1} \mathrm{~d} z_{1}+\bar{z}_{2} \mathrm{~d} z_{2}\right|^{2}\right)$$
where we have set
$$s=|\zeta|=\left|z_{1}\right|^{2}+\left|z_{2}\right|^{2}, \quad F(s)=\sqrt{1+\frac{\kappa}{s^{2}}} .$$

The metric (2.25) should be compared with the $\mathbb{C}^{2}$ metric in the form (A.22), that is
$$g_{\mathbb{C}^{2}}=\frac{1}{s}\left[\left|z_{1} \mathrm{~d} z_{2}-z_{2} \mathrm{~d} z_{1}\right|^{2}+\left|\bar{z}_{1} \mathrm{~d} z_{1}+\bar{z}_{2} \mathrm{~d} z_{2}\right|^{2}\right],$$
which (2.25) reduces to for $\kappa=0$. For later usage we note that in components (2.25) becomes
$$\begin{aligned}
& g_{z_{1} \bar{z}_{1}}=\frac{1}{s}\left(F\left|z_{2}\right|^{2}+F^{-1}\left|z_{1}\right|^{2}\right), \quad g_{z_{2} \bar{z}_{2}}=\frac{1}{s}\left(F\left|z_{1}\right|^{2}+F^{-1}\left|z_{2}\right|^{2}\right), \\
& g_{z_{1} \bar{z}_{2}}=\bar{g}_{z_{2} \bar{z}_{1}}=\frac{1}{s}\left(F^{-1}-F\right) z_{2} \bar{z}_{1}
\end{aligned}$$
and, since $g$ has unit determinant,
$$\begin{aligned}
& g_{z_{1} \bar{z}_{1}}^{-1}=\frac{1}{s}\left(F\left|z_{1}\right|^{2}+F^{-1}\left|z_{2}\right|^{2}\right), \quad g_{z_{2}}^{-1}=\frac{1}{s}\left(F\left|z_{2}\right|^{2}+F^{-1}\left|z_{1}\right|^{2}\right), \\
& g_{z_{1} \bar{z}_{2}}^{-1}=\bar{g}_{z_{2} \bar{z}_{1}}^{-1}=\frac{1}{s}\left(F-F^{-1}\right) \bar{z}_{1} z_{2} .
\end{aligned}$$

Writing
$$Z=\binom{z_{1}}{z_{2}}, \quad J=\left(\begin{array}{cc}
0 & 1 \\
-1 & 0
\end{array}\right),$$
we obtain
$$g=\frac{1}{s}\left(F\left|Z^{T} J \mathrm{~d} Z\right|^{2}+F^{-1}\left|Z^{T} \mathrm{~d} \bar{Z}\right|^{2}\right) .$$
Clearly $s$ and $Z^{T} \mathrm{~d} \bar{Z}$ are invariant under $Z \mapsto G Z$ for any $G \in U(2)$, while $Z^{T} J \mathrm{~d} Z$ is invariant for $G \in \operatorname{Sp}(2, \mathbb{C})=S L(2, \mathbb{C})$. However $\left|Z^{T} J \mathrm{~d} Z\right|$ is invariant for any $G \in G L(2, \mathbb{C}):|\operatorname{det} G|=1$, hence (2.31) shows that the isometry group of EH is $U(2)$.
2.3. Harmonic 2-forms. With respect to the $\left(z_{1}, z_{2}\right)$ coordinates, the frame (2.20) becomes
$$\begin{aligned}
& e_{1}=\sqrt{\frac{F}{s}} \frac{\bar{z}_{2}}{z_{2}}\left(z_{2} d z_{1}-z_{1} d z_{2}\right)=\frac{1}{2}(F s)^{1 / 2} e \\
& e_{2}=\frac{1}{\sqrt{F s}} \frac{z_{2}}{\bar{z}_{2}}\left(\bar{z}_{1} d z_{1}+\bar{z}_{2} d z_{2}\right)=\frac{1}{2}(F s)^{-1 / 2} \theta
\end{aligned}$$
Since
$$\begin{aligned}
* e_{1} & =\frac{1}{2} e_{1} \wedge e_{2} \wedge \bar{e}_{2}, \quad * e_{2} \\
*\left(e_{1} \wedge \bar{e}_{1}\right) & =\frac{1}{2} e_{2} \wedge e_{1} \wedge \bar{e}_{1}, \\
* \bar{e}_{2}, \quad *\left(e_{2} \wedge \bar{e}_{2}\right) & =e_{1} \wedge \bar{e}_{1},
\end{aligned}$$
the combination $e_{1} \wedge \bar{e}_{1}+e_{2} \wedge \bar{e}_{2}$ is self-dual. In fact, it is essentially the Kähler form $\omega$ on EH, see (2.21). Of course $\omega$ is also closed, hence harmonic, but not $L^{2}$. Using (2.32) $\omega$ can be rewritten in the form
$$\omega=2 i\left[F\left(\mathrm{~d} z_{1} \wedge \mathrm{~d} \bar{z}_{1}+\mathrm{d} z_{2} \wedge \mathrm{~d} \bar{z}_{2}\right)+\frac{1}{s}\left(F^{-1}-F\right)\left(\bar{z}_{1} \mathrm{~d} z_{1}+\bar{z}_{2} \mathrm{~d} z_{2}\right) \wedge\left(z_{1} \mathrm{~d} \bar{z}_{1}+z_{2} \mathrm{~d} \bar{z}_{2}\right)\right] .$$
Since $F$ satisfies
$$F^{\prime} s=F^{-1}-F=-\frac{\kappa}{s \sqrt{\kappa+s^{2}}}=-\frac{\kappa}{F s^{3}}$$
we can write the Kähler form as the exterior derivative of a local potential,
$$\omega=2 i \mathrm{~d}\left(F\left(z_{1} \mathrm{~d} \bar{z}_{1}+z_{2} \mathrm{~d} \bar{z}_{2}\right)\right) .$$

Consider now the anti self-dual combination $e_{1} \wedge \bar{e}_{1}-e_{2} \wedge \bar{e}_{2}$. It is not closed so we look for a closed multiple of it,
$$\tilde{\omega}=\frac{i}{2} f\left(e_{1} \wedge \bar{e}_{1}-e_{2} \wedge \bar{e}_{2}\right),$$
where $f$ is a function of $s$ only. Since $\omega$ is closed, $\mathrm{d}(s F e \wedge \bar{e})=-\mathrm{d}\left((s F)^{-1} \theta \wedge \bar{\theta}\right)$, so using (B.18) we have
$$\mathrm{d} \tilde{\omega}=\left(2 f(s F)^{\prime}+(s F) f^{\prime}\right) \wedge(\zeta \bar{\theta}+\bar{\zeta} \theta) \wedge e \wedge \bar{e},$$
showing that $\tilde{\omega}$ is closed provided that
$$f=\frac{1}{(s F)^{2}}$$
Therefore the form
$$\tilde{\omega}=\frac{1}{(s F)^{2}} \frac{i}{2}\left(e_{1} \wedge \bar{e}_{1}-e_{2} \wedge \bar{e}_{2}\right)$$
is anti self-dual and closed, hence harmonic. It is also $L^{2}$ since
$$|\tilde{\omega}|^{2} \operatorname{vol}=-\tilde{\omega} \wedge \tilde{\omega}=-\frac{1}{4}(s F)^{-4} e_{1} \wedge \bar{e}_{1} \wedge e_{2} \wedge \bar{e}_{2} \Rightarrow|\tilde{\omega}|^{2}=(s F)^{-4}$$
which has a finite integral over EH. Being closed, $\tilde{\omega}$ can also be written as the exterior derivative of a local potential, and a computation shows that
$$\tilde{\omega}=2 i \mathrm{~d}\left[\frac{1}{F s^{2}}\left(z_{1} \mathrm{~d} \bar{z}_{1}+z_{2} \mathrm{~d} \bar{z}_{2}\right)\right] .$$

It is well known that the harmonic cohomology of EH is non-trivial only in dimension two, and that the space of harmonic $L^{2}$ 2-forms is 1-dimensional [9]. As we have just seen it is generated by $\tilde{\omega}$.

It is interesting to compare the expressions of $\omega, \tilde{\omega}$ with that of $\mathrm{d} \theta_{3}$, for $\theta_{3}$ the metric dual with respect to the EH metric of the Killing vector field $X_{3}$,
$$\theta_{3}=X_{3}^{b}=\frac{i}{2 F}\left(z_{1} \mathrm{~d} \bar{z}_{1}+z_{2} \mathrm{~d} \bar{z}_{2}-\bar{z}_{1} \mathrm{~d} z_{1}-\bar{z}_{2} \mathrm{~d} z_{2}\right)=\frac{1}{F} \operatorname{Im}\left(\bar{z}_{1} \mathrm{~d} z_{1}+\bar{z}_{2} \mathrm{~d}_{2}\right) .$$
Since $X_{3}$ is a Killing vector field and EH is Ricci-flat, $\mathrm{d} \theta_{3}$ is harmonic. One calculates
$$2 \mathrm{~d} \theta_{3}=\frac{i}{2}\left[e_{1} \wedge \bar{e}_{1}+e_{2} \wedge \bar{e}_{2}-\kappa\left(\frac{e_{1} \wedge \bar{e}_{1}-e_{2} \wedge \bar{e}_{2}}{(s F)^{2}}\right)\right]=\omega-\kappa \tilde{\omega},$$
hence $\kappa \tilde{\omega}$ represents the same cohomology class as $\omega$, which generates of $H_{\mathrm{dR}}^{2}(\mathrm{EH})$. We can also see that $\mathrm{d} \theta_{3}$ is harmonic but not $L^{2}$ and, interestingly, that $\omega, \kappa \tilde{\omega}$ are the self-dual and anti self-dual parts of $\mathrm{d} \theta_{3}$,
$$\omega=* \mathrm{~d} \theta_{3}+\mathrm{d} \theta_{3}, \quad \kappa \tilde{\omega}=* \mathrm{~d} \theta_{3}-\mathrm{d} \theta_{3} .$$
Using (2.36) and (2.42) we see that $\mathrm{d} \theta_{3}$ can also be written in the form
$$\mathrm{d} \theta_{3}=i \mathrm{~d}\left[\frac{1}{F}\left(z_{1} \mathrm{~d} \bar{z}_{1}+z_{2} \mathrm{~d} \bar{z}_{2}\right)\right] .$$
2.4. $U(1)$ connection with $L^{2}$ harmonic curvature. In Section 3.1 we will consider the Dirac operator on EH twisted by a $U(1)$ connection $\mathcal{A}$ with $L^{2}$ harmonic curvature $\mathrm{d} \mathcal{A}$. As we just discussed, $\mathrm{d} \mathcal{A}$ is necessarily some constant multiple of $\tilde{\omega}$ and by (2.42) we can take $\mathcal{A}$ to be some multiple of
$$\frac{1}{s^{2} F}\left(z_{1} \mathrm{~d} \bar{z}_{1}+z_{2} \mathrm{~d} \bar{z}_{2}-\bar{z}_{1} \mathrm{~d} z_{1}-\bar{z}_{2} \mathrm{~d} z_{2}\right) .$$
In order for $\mathrm{d} \mathcal{A}$ to be the curvature of a connection we need to impose the quantisation condition
$$\frac{i}{2 \pi} \int_{\mathbb{C} P^{1}} \mathrm{~d} \mathcal{A}=\ell \in \mathbb{Z}$$
obtaining
$$\mathcal{A}=\ell(A-\bar{A}), \quad A=\frac{\sqrt{\kappa}}{2 s^{2} F}\left(z_{1} \mathrm{~d} \bar{z}_{1}+z_{2} \mathrm{~d} \bar{z}_{2}\right)=\frac{1}{2} \partial \sinh ^{-1}(\sqrt{\kappa} / s) .$$
2.5. Hyperkähler quotient. It is well known, see e.g. [11], that EH can be obtained as the hyperkähler quotient of $\mathbb{H}^{2}$, but we were unable to find anywhere in the literature the details of this construction in the amount sufficient for comparison with the two descriptions given above. We spell it out here ${ }^{1}$

The first part of this construction is standard and appears in many references. Identify $\mathbb{H}^{2}$ with $\mathbb{C}^{4}$ via the isomorphism $\mathbb{H}=\mathbb{C}^{2}+\mathbb{C}^{2} \mathbf{j}, q_{i}=Z_{i}+W_{i} \mathbf{j}, i=1,2, q_{i} \in \mathbb{H}, Z_{i}, W_{i} \in \mathbb{C}$, and equip $\mathbb{H}^{2}$ with the flat metric and the Kähler forms
$$\begin{aligned}
& \omega_{R}=\frac{i}{2}\left(\mathrm{~d} Z_{1} \wedge \mathrm{~d} \bar{Z}_{1}+\mathrm{d} Z_{2} \wedge \mathrm{~d} \bar{Z}_{2}+\mathrm{d} W_{1} \wedge \mathrm{~d} \bar{W}_{1}+\mathrm{d} W_{2} \wedge \mathrm{~d} \bar{W}_{2}\right)=\frac{i}{2} \partial \bar{\partial}\left(|Z|^{2}+|W|^{2}\right) \\
& \omega_{C}=\omega_{2}+i \omega_{3}=\mathrm{d} W_{1} \wedge \mathrm{~d} Z_{1}+\mathrm{d} W_{2} \wedge \mathrm{~d} Z_{2}
\end{aligned}$$
where $Z=\left(Z_{1}, Z_{2}\right)^{T}, W=\left(W_{1}, W_{2}\right)^{T},|Z|^{2}=\left|Z_{1}\right|^{2}+\left|Z_{2}\right|^{2}$.
The right $U(1)$ action
$$(Z, W) \mapsto(Z, W) \mathrm{e}^{\mathrm{i} t}=\left(\mathrm{e}^{\mathrm{i} t} Z, \mathrm{e}^{-\mathrm{i} t} W\right),$$
which corresponds to translation along the U(1) fibres of the Hopf fibration $S^{1} \hookrightarrow S^{7} \rightarrow \mathbb{C} P^{3}$, is Hamiltonian and isometric. It is convenient to take the associated moment maps to be
$$\mu_{R}=|Z|^{2}-|W|^{2}-2 \sqrt{\kappa}, \quad \mu_{C}=Z^{T} W=Z_{1} W_{1}+Z_{2} W_{2} .$$
The level set $\mu^{-1}(0)=\mu_{R}^{-1}(0) \cap \mu_{C}^{-1}(0)$ is a smooth real 5-manifold. Further quotienting by the $U(1)$ action (2.51) we get the hyperkähler quotient
$$\mathbb{H}^{2} / / U(1)=\mu^{-1}(0) / U(1) .$$

To compare to our previous description (2.25) of EH, we need to parametrise this level set by coordinates related to $z_{1}, z_{2}$, as well as some coordinate for the $S^{1}$ fibre. This is something we were unable to find in the literature. To proceed, let $h \in U(2)$ act on $\mathbb{C}^{2}$ by ordinary matrix multiplication. Then the isometric left $U(2)$ action on $\mathbb{C}^{4}$ given by
$$h \cdot(Z, W)=(h Z, \bar{h} W)$$
commutes with (2.51) and preserves $\mu$ level sets, so it descends to an isometric action on the quotient. In quaternionic notation, the moment map is
$$\mu\left(q_{1}, q_{2}\right)=\frac{1}{2} \sum_{a=1,2} q_{a} \mathbf{i} \bar{q}_{a}-\sqrt{\kappa} \mathbf{i}$$
and (2.54) corresponds to
$$h \cdot\left(q_{1}, q_{2}\right)=\left(q_{1}, q_{2}\right) h^{T}$$
where on the rhs we have ordinary matrix multiplication.
The isometric $U(2)$ action on the quotient just introduced should match the one described in the paragraph following (2.31). This is achieved by setting
$$\begin{aligned}
Z_{1} & =z_{1} e^{i \psi} f^{1 / 2}, & Z_{2} & =z_{2} e^{i \psi} f^{1 / 2} \\
W_{1} & =-z_{2} e^{-i \psi} f^{-1 / 2}, & W_{2} & =z_{1} e^{-i \psi} f^{-1 / 2}
\end{aligned}$$
where $f$ is some function of $z_{1}, z_{2}$ to be determined. This ansatz automatically satisfies $\mu_{C}(Z, W)=0$, while the condition $|Z|^{2}-|W|^{2}=2 \sqrt{\kappa}$ becomes
$$\left(\left|z_{1}\right|^{2}+\left|z_{2}\right|^{2}\right)\left(f-f^{-1}\right)=2 \sqrt{\kappa},$$
which is solved by
$$f=\sqrt{1+\frac{\kappa}{s^{2}}}+\frac{\sqrt{\kappa}}{s} .$$

We note the useful identities
$$f-f^{-1}=\frac{2 \sqrt{\kappa}}{s}, \quad f+f^{-1}=2 \sqrt{1+\frac{\kappa}{s^{2}}}=2 F,$$

\footnotetext{
${ }^{1}$ One of us (KK) benefited from a discussion with Daniel Platt in relation to the material described in this subsection.
}
as well as
$$\frac{1}{f^{1 / 2}} \frac{\mathrm{~d} f^{1 / 2}}{\mathrm{~d} s}=\frac{1}{2 f} \frac{\mathrm{~d} f}{\mathrm{~d} s}=-\frac{\sqrt{\kappa}}{2 s^{2} F} .$$

We now pull-back the flat metric on $\mathbb{C}^{4}$ to $\mu^{-1}(\mathbf{i} \sqrt{\kappa})$ as parametrised by (2.57). We have
$$\begin{aligned}
\mathrm{d} Z_{1} & =z_{1} e^{i \psi} f^{1 / 2}\left(\frac{\mathrm{~d} z_{1}}{z_{1}}+i \mathrm{~d} \psi-\frac{\sqrt{\kappa}}{2 s^{2} F} \mathrm{~d} s\right), \quad \mathrm{d} Z_{2}=z_{2} e^{i \psi} f^{1 / 2}\left(\frac{\mathrm{~d} z_{2}}{z_{2}}+i \mathrm{~d} \psi-\frac{\sqrt{\kappa}}{2 s^{2} F} \mathrm{~d} s\right), \\
\mathrm{d} W_{1} & =-z_{2} e^{-i \psi} f^{-1 / 2}\left(\frac{\mathrm{~d} z_{2}}{z_{2}}-i \mathrm{~d} \psi+\frac{\sqrt{\kappa}}{2 s^{2} F} \mathrm{~d} s\right), \quad \mathrm{d} W_{2}=z_{1} e^{-i \psi} f^{-1 / 2}\left(\frac{\mathrm{~d} z_{1}}{z_{1}}-i \mathrm{~d} \psi+\frac{\sqrt{\kappa}}{2 s^{2} F} \mathrm{~d} s\right),
\end{aligned}$$
giving
$$\begin{aligned}
\left|\mathrm{d} Z_{1}\right|^{2}+\left|\mathrm{d} Z_{2}\right|^{2} & =f\left(\left|\mathrm{~d} z_{1}\right|^{2}+\left|\mathrm{d} z_{2}\right|^{2}\right)+s f \mathrm{~d} \psi^{2}+i f \mathrm{~d} \psi\left(z_{1} \mathrm{~d} \bar{z}_{1}-\bar{z}_{1} \mathrm{~d} z_{1}+z_{2} \mathrm{~d} \bar{z}_{2}-\bar{z}_{2} \mathrm{~d} z_{2}\right) \\
& +f \frac{\kappa(\mathrm{~d} s)^{2}}{4 s^{3} F^{2}}-f \frac{\sqrt{\kappa}(\mathrm{~d} s)^{2}}{2 s^{2} F} \\
\left|\mathrm{~d} W_{1}\right|^{2}+\left|\mathrm{d} W_{2}\right|^{2} & =f^{-1}\left(\left|\mathrm{~d} z_{1}\right|^{2}+\left|\mathrm{d} z_{2}\right|^{2}\right)+s f^{-1} \mathrm{~d} \psi^{2}-i f^{-1} \mathrm{~d} \psi\left(z_{1} \mathrm{~d} \bar{z}_{1}-\bar{z}_{1} \mathrm{~d} z_{1}+z_{2} \mathrm{~d} \bar{z}_{2}-\bar{z}_{2} \mathrm{~d} z_{2}\right) \\
& +f^{-1} \frac{\kappa(\mathrm{~d} s)^{2}}{4 s^{3} F^{2}}+f^{-1} \frac{\sqrt{\kappa}(\mathrm{~d} s)^{2}}{2 s^{2} F}
\end{aligned}$$
This means that the pull-back of (half) the flat metric on $\mathbb{C}^{4}$ is
$$\begin{aligned}
& \frac{1}{2}\left(\left|\mathrm{~d} Z_{1}\right|^{2}+\left|\mathrm{d} Z_{2}\right|^{2}+\left|\mathrm{d} W_{1}\right|^{2}+\left|\mathrm{d} W_{2}\right|^{2}\right)=F\left(\left|\mathrm{~d} z_{1}\right|^{2}+\left|\mathrm{d} z_{2}\right|^{2}\right)+s F \mathrm{~d} \psi^{2} \\
& +i \mathrm{~d} \psi \frac{\sqrt{\kappa}}{s}\left(z_{1} \mathrm{~d} \bar{z}_{1}-\bar{z}_{1} \mathrm{~d} z_{1}+z_{2} \mathrm{~d} \bar{z}_{2}-\bar{z}_{2} \mathrm{~d} z_{2}\right)-\frac{\kappa(\mathrm{d} s)^{2}}{4 s^{3} F}
\end{aligned}$$
We now complete the square getting
$$\frac{1}{2}\left(\left|\mathrm{~d} Z_{1}\right|^{2}+\left|\mathrm{d} Z_{2}\right|^{2}+\left|\mathrm{d} W_{1}\right|^{2}+\left|\mathrm{d} W_{2}\right|^{2}\right)=g+s F(\mathrm{~d} \psi+i(A-\bar{A}))^{2},$$
where
$$\begin{aligned}
g & =F\left(\left|\mathrm{~d} z_{1}\right|^{2}+\left|\mathrm{d}_{2}\right|^{2}\right)+\frac{1}{s}\left(F^{-1}-F\right)\left|\bar{z}_{1} \mathrm{~d} z_{1}+\bar{z}_{2} \mathrm{~d} z_{2}\right|^{2} \\
A & =\frac{\sqrt{\kappa}}{2 s^{2} F}\left(z_{1} \mathrm{~d} \bar{z}_{1}+z_{2} \mathrm{~d} \bar{z}_{2}\right)
\end{aligned}$$
Using the identity
$$s\left(\left|\mathrm{~d} z_{1}\right|^{2}+\left|\mathrm{d} z_{2}\right|^{2}\right)=\left|z_{1} \mathrm{~d} z_{2}-z_{2} \mathrm{~d} z_{1}\right|^{2}+\left|\bar{z}_{1} \mathrm{~d} z_{1}+\bar{z}_{2} \mathrm{~d} z_{2}\right|^{2}$$
we see that (2.66) is the EH metric in the form (2.25). We recognise $A$ for the $(0,1)$ part of the U(1) connection (2.49), whose curvature is anti-self-dual and $L^{2}$. Therefore, the natural connection $A-\bar{A}$ on EH arises as the connection in the 5-dimensional fibered space $\mu^{-1}(\mathbf{i} \sqrt{\kappa})$ obtained in the process of a hyperkähler reduction of $\mathbb{H}^{2}$.

\section*{3. Dirac zero modes on the Eguchi-Hanson space}
3.1. No Dirac zero modes on EH. Let $D$ be the Dirac operator on EH and $\sigma$ be a spinor. Since the scalar curvature $s$ of EH vanishes, Lichernowicz's identity
$$D^{2} \sigma=\nabla^{*} \nabla \sigma+\frac{s}{4} \sigma$$
implies that EH admits no $L^{2}$ Dirac zero modes. In order to obtain a non-trivial problem it is necessary to twist the spinor bundle by a complex line bundle equipped with a connection $\mathcal{A}$. Equivalently, we need to replace the spin structure on EH by a spin- $c$ structure. Lichernowicz's identity then becomes
$$D_{\mathcal{A}}^{2} \sigma=\nabla^{*} \nabla \sigma+\frac{s}{4} \sigma+\mathrm{d} \mathcal{A} \cdot \sigma,$$
where • denotes Clifford multiplication, and for a suitable choice of $\mathcal{A}$ it is possible to obtain nontrivial solutions of the twisted Dirac equation $D_{\mathcal{A}} \sigma=0$. Twisting by an arbitrary connection does not make for an interesting problem, but taking $\mathcal{A}$ so that $\mathrm{d} \mathcal{A}$ is $L^{2}$ harmonic is a natural choice. As we already discussed, in the case of EH any such connection $\mathcal{A}$ takes the form (2.49). Therefore, we want to find $L^{2}$ solutions of the equation $D_{\mathcal{A}} \sigma=0$ for $\mathcal{A}$ given by (2.49). Working on the spinor bundle, viewed as rank four Spin(4) module, this problem has been considered in [4].
3.2. The canonical spin- $c$ structure. However, since EH is a Kähler manifold, there is a more convenient approach in terms of complex differential forms. In fact, any almost complex manifold carries a canonical spin- $c$ structure. Let us recall the necessary background. We follow [6], section 3.4.

We have the following proposition:
Proposition 1. The spinor bundle $S$ of an Hermitian manifold of complex dimension $k$ (with respect to an arbitrary spin-c structure) is isomorphic to
$$S=\left(\Lambda^{0,0} \oplus \ldots \oplus \Lambda^{0, k}\right) \otimes S_{0}=\left(\Lambda^{0,0} \oplus \ldots \oplus \Lambda^{k, 0}\right) \otimes S_{k},$$
where
$$S_{0}=\{\sigma \in S: \omega \sigma=i k \sigma\}, \quad S_{k}=\{\sigma \in S: \omega \sigma=-i k \sigma\},$$
and $\omega$ is the Kähler form, acting on a spinor by Clifford multiplication. In particular $S_{0}=$ $\Lambda^{k, 0} \otimes S_{k}$ and $S_{k}=\Lambda^{0, k} \otimes S_{0}$.

The anti-canonical spin-c structure on an Hermitian manifold $M, J$ is the one for which the bundle $S_{0}$ is trivial and $S_{k}$ coincides with the canonical bundle $K=\Lambda^{k}\left(T^{*}\right)$ of $M$. We have the following proposition, see [6] and also [15].

Proposition 2. Let $(M, J)$ be a Kähler manifold equipped with the anti-canonical spin-c structure. Then
$$S \simeq \Lambda^{0,0} \oplus \ldots \oplus \Lambda^{0, k}$$
and the Dirac operator defined by the Levi-Civita connection coincides with
$$\sqrt{2}\left(\bar{\partial}+\bar{\partial}^{*}\right) .$$

For reasons that will become clear in the next subsections, we will consider instead the Dirac operator
$$D=\bar{\partial}-\bar{\partial}^{*},$$
which has the same kernel as $\bar{\partial}+\bar{\partial}^{*}$, with the Clifford action given by
$$v \cdot \sigma=v^{0,1} \wedge \sigma+\iota_{v^{\sharp}} \sigma .$$

We discussed above how the spin structure on EH admits no $L^{2}$ harmonic spinors. The same holds for the (anti-)canonical spin- $c$ structure. In fact the spinor bundle is isomorphic to $W=\Lambda^{0} \oplus \Lambda^{0,1} \oplus \Lambda^{0,2}$ and harmonic spinors correspond to forms $\sigma \in W$ such that
$$D \sigma=\left(\bar{\partial}-\bar{\partial}^{*}\right) \sigma=0 .$$
On a complete Kähler manifold
$$D \sigma=0 \Leftrightarrow D^{2} \sigma=0 \Leftrightarrow\left(\mathrm{dd}^{*}+\mathrm{d}^{*} \mathrm{~d}\right) \sigma=0 \Leftrightarrow \mathrm{~d} \sigma=0=\mathrm{d}^{*} \sigma .$$
Thus harmonic spinors in $\Lambda^{0}$ are constant functions and $\alpha \in \Lambda^{2}$ is harmonic if and only if $* \alpha$ is a constant function. Neither is $L^{2}$. As for 1 -forms, by the Bochner identity
$$\triangle \sigma=\nabla^{*} \nabla \sigma+\operatorname{Ric}(\sigma) .$$
Since EH is Ricci-flat, any harmonic form has to be parallel, hence cannot be $L^{2}$. The result is not surprising since the Chern connection on the canonical bundle of a Ricci-flat manifold has zero curvature, so the Dirac operator associated to the canonical spin- $c$ structure on EH is equivalent to the one associated to the spin structure.
3.3. Computing the action of the Dirac operator on spin- $c$ spinors. In four dimensions, the two chiralities of spin- $c$ spinors are identified with
$$W^{+}=\Lambda^{0}+\Lambda^{0,2}, \quad W^{-}=\Lambda^{0,1}$$
and the spin- $c$ Dirac operator is
$$D=\bar{\partial}-\bar{\partial}^{*} .$$
Here $\bar{\partial}$ is the $(0,1)$ projection of the exterior derivative d, and $\bar{\partial}^{*}$ its adjoint. The use of the minus sign here rather than plus is a convention that is more suitable for our purposes, because it leads to a very simple way of computing $D$, which we will explain below.

The action of $\bar{\partial}$ on $\Lambda^{0}, \Lambda^{0,1}$ is very simple
$$\begin{array}{r}
\bar{\partial}: \Lambda^{0} \ni \alpha \rightarrow \partial_{\bar{z}_{1}} \alpha d \bar{z}_{1}+\partial_{\bar{z}_{2}} \alpha d \bar{z}_{2} \in \Lambda^{0,1} \\
\bar{\partial}: \Lambda^{0,1} \ni \beta d \bar{z}_{1}+\gamma d \bar{z}_{2} \rightarrow\left(\partial_{\bar{z}_{1}} \gamma-\partial_{\bar{z}_{2}} \beta\right) d \bar{z}_{1} \wedge d \bar{z}_{2} \in \Lambda^{0,2}
\end{array}$$
Here $\alpha, \beta, \gamma$ are functions of $z_{1}, \bar{z}_{1}, z_{2}, \bar{z}_{2}$. The action of $\bar{\partial}^{*}$ involves the metric and is more complicated. However, on a Kähler manifold there is a very simple set of rules to be followed. We derive these rules after $\bar{\partial}^{*}$ is computed.
3.4. Computation of $\bar{\partial}^{*}$. We first compute the action of $\bar{\partial}^{*}$ on $\Lambda^{0,1}$. For the sake of generality, we do the computation for a general Hermitian metric on $\mathbb{C}^{2}$. The Hermitian pairing of $\bar{\partial} \alpha \in \Lambda^{0,1}$ with an arbitrary element $\beta d \bar{z}_{1}+\gamma d \bar{z}_{2} \in \Lambda^{0,1}$ is given by
$$\begin{array}{r}
\left\langle\bar{\partial} \alpha, \beta d \bar{z}_{1}+\gamma d \bar{z}_{2}\right\rangle=g^{-1}\left(\partial_{\bar{z}_{1}} \alpha d \bar{z}_{1}+\partial_{\bar{z}_{2}} \alpha d \bar{z}_{2}, \bar{\beta} d z_{1}+\bar{\gamma} d z_{2}\right)= \\
\partial_{\bar{z}_{1}} \alpha \bar{\beta} g_{z_{1} \bar{z}_{1}}^{-1}+\partial_{\bar{z}_{1}} \alpha \bar{\gamma} g_{z_{2} \bar{z}_{1}}^{-1}+\partial_{\bar{z}_{2}} \alpha \bar{\beta} g_{z_{1} \bar{z}_{2}}^{-1}+\partial_{\bar{z}_{2}} \alpha \bar{\gamma} g_{z_{2} \bar{z}_{2}}^{-1}
\end{array}$$
We now multiply this by the volume factor, which is $v_{g}\left|d z_{1}\right|^{2}\left|d z_{2}\right|^{2}$, and integrate by parts. This gives
$$v_{g}\left\langle\alpha, \bar{\partial}^{*}\left(\beta d \bar{z}_{1}+\gamma d \bar{z}_{2}\right)\right\rangle=-\alpha \overline{\partial_{z_{1}}\left(g_{z_{1} \bar{z}_{1}}^{-1} v_{g} \beta\right)}-\alpha \overline{\partial_{z_{1}}\left(g_{z_{1} \bar{z}_{2}}^{-1} v_{g} \gamma\right)}-\alpha \overline{\partial_{z_{2}}\left(g_{z_{2} \bar{z}_{1}}^{-1} v_{g} \beta\right)}-\alpha \overline{\partial_{z_{2}}\left(g_{z_{2}}^{-1} \bar{z}_{2} \gamma\right)},$$
which is an identity that only holds modulo surface terms (which we assume to vanish). We can simplify this expression using the fact that the components of the inverse metric times the volume form give the components of the original metric. Doing so we get
$$v_{g} \bar{\partial}^{*}\left(\beta d \bar{z}_{1}+\gamma d \bar{z}_{2}\right)=-\partial_{z_{1}}\left(g_{z_{2} \bar{z}_{2}} \beta\right)+\partial_{z_{1}}\left(g_{z_{2} \bar{z}_{1}} \gamma\right)+\partial_{z_{2}}\left(g_{z_{1} \bar{z}_{2}} \beta\right)-\partial_{z_{2}}\left(g_{z_{1} \bar{z}_{1}} \gamma\right) \in \Lambda^{0} .$$

The computation of $\bar{\partial}^{*}$ on $\Lambda^{0,2}$ is similar. We have
$$\begin{array}{r}
\left\langle\left(\partial_{\bar{z}_{1}} \gamma-\partial_{\bar{z}_{2}} \beta\right) d \bar{z}_{1} \wedge d \bar{z}_{2}, \delta d \bar{z}_{1} \wedge d \bar{z}_{2}\right\rangle= \\
g^{-1}\left(\left(\partial_{\bar{z}_{1}} \gamma-\partial_{\bar{z}_{2}} \beta\right)\left(d \bar{z}_{1} \otimes d \bar{z}_{2}-d \bar{z}_{2} \otimes d \bar{z}_{1}\right), \bar{\delta}\left(d z_{1} \otimes d z_{2}\right)\right)= \\
\left(\partial_{\bar{z}_{1}} \gamma-\partial_{\bar{z}_{2}} \beta\right) v_{g}^{-1} \bar{\delta}
\end{array}$$
We now multiply by $v_{g}$ and integrate by parts to get
$$v_{g}\left\langle\beta d \bar{z}_{1}+\gamma d \bar{z}_{2}, \bar{\partial}^{*}\left(\delta d \bar{z}_{1} \wedge d \bar{z}_{2}\right)\right\rangle=-\gamma \overline{\partial_{z_{1}} \delta}+\beta \overline{\partial_{z_{2}} \delta} .$$
Since we want to rewrite $\bar{\partial}^{*}\left(\delta d \bar{z}_{1} \wedge d \bar{z}_{2}\right)$ in the form
$$v_{g} \bar{\partial}^{*}\left(\delta d \bar{z}_{1} \wedge d \bar{z}_{2}\right)=A d \bar{z}_{1}+B d \bar{z}_{2}$$
we need to match
$$-\gamma \overline{\partial_{z_{1}} \delta}+\beta \overline{\partial_{z_{2}} \delta}=\beta \bar{A} g_{z_{1} \bar{z}_{1}}^{-1}+\beta \bar{B} g_{z_{2}}^{-1} \bar{z}_{1}+\gamma \bar{A} g_{z_{1}}^{-1} \bar{z}_{2}+\gamma \bar{B} g_{z_{2}}^{-1} \bar{z}_{2}$$
which gives
$$A=g_{z_{1} \bar{z}_{1}} \partial_{z_{2}} \delta-g_{z_{2} \bar{z}_{1}} \partial_{z_{1}} \delta, \quad B=g_{z_{1} \bar{z}_{2}} \partial_{z_{2}} \delta-g_{z_{2} \bar{z}_{2}} \partial_{z_{1}} \delta$$

Collecting the above results, we obtain the two chiral halves of the Dirac operator. Abusing the notation, we still denote by $D: W^{+} \rightarrow W^{-}$one of the two chiral parts, and by $D^{\dagger}: W^{-} \rightarrow$ $W^{+}$the other one. Their action is
$$\begin{aligned}
D\left(\alpha+\delta d \bar{z}_{1} \wedge d \bar{z}_{2}\right) & =\left(\partial_{\bar{z}_{1}} \alpha-v_{g}^{-1} g_{z_{1} \bar{z}_{1}} \partial_{z_{2}} \delta+v_{g}^{-1} g_{z_{2}} \bar{z}_{1} \partial_{z_{1}} \delta\right) d \bar{z}_{1} \\
& +\left(\partial_{\bar{z}_{2}} \alpha-v_{g}^{-1} g_{z_{1} \bar{z}_{2}} \partial_{z_{2}} \delta+v_{g}^{-1} g_{z_{2} \bar{z}_{2}} \partial_{z_{1}} \delta\right) d \bar{z}_{2}
\end{aligned}$$
$$\begin{array}{r}
D^{\dagger}\left(\beta d \bar{z}_{1}+\gamma d \bar{z}_{2}\right)=\left(\partial_{\bar{z}_{1}} \gamma-\partial_{\bar{z}_{2}} \beta\right) d \bar{z}_{1} \wedge d \bar{z}_{2} \\
+v_{g}^{-1} \partial_{z_{1}}\left(g_{z_{2} \bar{z}_{2}} \beta\right)-v_{g}^{-1} \partial_{z_{1}}\left(g_{z_{2} \bar{z}_{1}} \gamma\right)-v_{g}^{-1} \partial_{z_{2}}\left(g_{z_{1} \bar{z}_{2}} \beta\right)+v_{g}^{-1} \partial_{z_{2}}\left(g_{z_{1} \bar{z}_{1}} \gamma\right) .
\end{array}$$
3.5. Spin- $c$ Dirac operator on a Kähler manifold. So far we have computed the Dirac operator only assuming that the metric is Hermitian. If the metric is also Kähler, thanks to the identities
$$\partial_{z_{1}} g_{z_{2} \bar{z}_{1}}=\partial_{z_{2}} g_{z_{1} \bar{z}_{1}}, \quad \partial_{z_{1}} g_{z_{2} \bar{z}_{2}}=\partial_{z_{2}} g_{z_{1} \bar{z}_{2}},$$
the terms involving derivatives of the metric in (3.20) cancel among each other. As a result, we obtain the following simplified expression for the chiral Dirac operator on $W^{-}$,
$$\begin{array}{r}
D^{\dagger}\left(\beta d \bar{z}_{1}+\gamma d \bar{z}_{2}\right)=\left(\partial_{\bar{z}_{1}} \gamma-\partial_{\bar{z}_{2}} \beta\right) d \bar{z}_{1} \wedge d \bar{z}_{2} \\
+v_{g}^{-1} g_{z_{2} \bar{z}_{2}} \partial_{z_{1}} \beta-v_{g}^{-1} g_{z_{2} \bar{z}_{1}} \partial_{z_{1}} \gamma-v_{g}^{-1} g_{z_{1} \bar{z}_{2}} \partial_{z_{2}} \beta+v_{g}^{-1} g_{z_{1} \bar{z}_{1}} \partial_{z_{2}} \gamma .
\end{array}$$
3.6. Practical way of computing the Dirac operator on a Kähler manifold. The computations above illustrate that there is a very simple method for computing the Dirac operator on a Kähler manifold. The method consists in taking any differential form in question, and then first computing its full exterior derivative, including the terms not belonging to $\Lambda^{0, k}$. One then uses the metric pairing to map the latter terms from $\Lambda^{1, k}$ to $\Lambda^{0, k-1}$. Let us see how this works in practice.

We start with the spinor in $W^{-}=\Lambda^{0,1}$. We have
$$\begin{array}{r}
\mathrm{d}\left(\beta \mathrm{~d} \bar{z}_{1}+\gamma \mathrm{d} \bar{z}_{2}\right)=\partial_{z_{1}} \beta \mathrm{~d} z_{1} \wedge \mathrm{~d} \bar{z}_{1}+\partial_{z_{2}} \beta \mathrm{~d} z_{2} \wedge \mathrm{~d} \bar{z}_{1}+\partial_{z_{1}} \gamma \mathrm{~d} z_{1} \wedge \mathrm{~d} \bar{z}_{2}+\partial_{z_{2}} \gamma \mathrm{~d} z_{2} \wedge \mathrm{~d} \bar{z}_{2} \\
+\left(\partial_{\bar{z}_{2}} \gamma-\partial_{\bar{z}_{1}} \beta\right) \mathrm{d} \bar{z}_{1} \wedge \mathrm{~d} \bar{z}_{2}
\end{array}$$
The second line here is in $\Lambda^{0,2}$, and so a spinor in $W^{+}$, but the first line lies in $\Lambda^{1,1}$ and is not a spinor. However, we can use the metric pairing to map it into $\Lambda^{0}$. Denoting this projection by $g^{-1}$ we have
$$\begin{array}{r}
g^{-1}\left(\mathrm{~d}\left(\beta \mathrm{~d} \bar{z}_{1}+\gamma \mathrm{d} \bar{z}_{2}\right)\right)=g_{z_{1} \bar{z}_{1}}^{-1} \partial_{z_{1}} \beta+g_{z_{2} \bar{z}_{1}}^{-1} \partial_{z_{2}} \beta+g_{z_{1} \bar{z}_{2}}^{-1} \partial_{z_{1}} \gamma+g_{z_{2} \bar{z}_{2}}^{-1} \partial_{z_{2}} \gamma \\
+\left(\partial_{\bar{z}_{2}} \gamma-\partial_{\bar{z}_{1}} \beta\right) \mathrm{d} \bar{z}_{1} \wedge \mathrm{~d} \bar{z}_{2}
\end{array}$$
Taking into account the relation between the metric and its inverse we can write this as
$$\begin{array}{r}
g^{-1}\left(\mathrm{~d}\left(\beta \mathrm{~d} \bar{z}_{1}+\gamma \mathrm{d} \bar{z}_{2}\right)\right)=v_{g}^{-1} g_{z_{2} \bar{z}_{2}} \partial_{z_{1}} \beta-v_{g}^{-1} g_{z_{1} \bar{z}_{2}} \partial_{z_{2}} \beta-v_{g}^{-1} g_{z_{2} \bar{z}_{1}} \partial_{z_{1}} \gamma+v_{g}^{-1} g_{z_{1} \bar{z}_{1}} \partial_{z_{2}} \gamma \\
+\left(\partial_{\bar{z}_{2}} \gamma-\partial_{\bar{z}_{1}} \beta\right) \mathrm{d} \bar{z}_{1} \wedge \mathrm{~d} \bar{z}_{2}
\end{array}$$
which is the correct expression (3.22) for the chiral Dirac operator on $W^{-}$.
Completely analogous computations give the other chiral Dirac operator: we first apply the full exterior derivative to $\Lambda^{0,2}$
$$\mathrm{d}\left(\delta \mathrm{~d} \bar{z}_{1} \wedge \mathrm{~d} \bar{z}_{2}\right)=\partial_{z_{1}} \delta \mathrm{~d} z_{1} \wedge \mathrm{~d} \bar{z}_{1} \wedge \mathrm{~d} \bar{z}_{2}+\partial_{z_{2}} \delta \mathrm{~d} z_{2} \wedge \mathrm{~d} \bar{z}_{1} \wedge \mathrm{~d} \bar{z}_{2} .$$
We now do all possible metric pairings to map this into $\Lambda^{0,1}$. We have
$$g^{-1}\left(\mathrm{~d}\left(\delta \mathrm{~d} \bar{z}_{1} \wedge \mathrm{~d} \bar{z}_{2}\right)\right)=g_{z_{1} \bar{z}_{1}}^{-1} \partial_{z_{1}} \delta \mathrm{~d} \bar{z}_{2}-g_{z_{1} \bar{z}_{2}}^{-1} \partial_{z_{1}} \delta \mathrm{~d} \bar{z}_{1}+g_{z_{2} \bar{z}_{1}}^{-1} \partial_{z_{2}} \delta \mathrm{~d} \bar{z}_{2}-g_{z_{2} \bar{z}_{2}}^{-1} \partial_{z_{2}} \delta \mathrm{~d} \bar{z}_{1} .$$
Again using the relation between the metric and its inverse and collecting terms we have
$$g^{-1}\left(\mathrm{~d}\left(\delta \mathrm{~d} \bar{z}_{1} \wedge \mathrm{~d} \bar{z}_{2}\right)\right)=v_{g}^{-1}\left(g_{z_{2} \bar{z}_{1}} \partial_{z_{1}} \delta-v_{g}^{-1} g_{z_{1} \bar{z}_{1}} \partial_{z_{2}} \delta\right) \mathrm{d} \bar{z}_{1}+v_{g}^{-1}\left(g_{z_{2} \bar{z}_{2}} \partial_{z_{1}} \delta-v_{g}^{-1} g_{z_{1} \bar{z}_{2}} \partial_{z_{2}} \delta\right) \mathrm{d} \bar{z}_{2},$$
which is exactly the $\delta$-dependent part of (3.19). All in all, this is a very simple way of computing the spin- $c$ Dirac operator for a Kähler metric, which involves nothing more complicated than taking the exterior derivative, and then doing metric contractions. It is in order to have such a simple recipe for computing $D$ that we have taken the minus sign in our definition $D=\bar{\partial}-\bar{\partial}^{*}$ of the Dirac operator.

To summarise, the spinor $D \sigma$ can be obtained by first calculating $\mathrm{d} \sigma \in \Lambda^{0, q+1} \oplus \Lambda^{1, q}$. The $\Lambda^{0, q+1}$ component corresponds to $\bar{\partial} \sigma$ while contracting with the (inverse) metric maps the $(1, q)$ component to $-\bar{\partial}^{*} \sigma \in \Lambda^{0, q-1}$.

Similarly, when considering the twisted operator
$$D_{\mathcal{A}}=D+\mathcal{A},$$
the action of $\mathcal{A}$ is given by (3.5) so we first calculate $\mathcal{A} \wedge \sigma \in \Lambda^{1, q} \oplus \Lambda^{0, q+1}$ and then contract the $(1, q)$ part with the inverse metric to obtain a form of degree $(0, q-1)$. This gives very simple computational rules, allowing to compute the twisted Dirac operator with minimal effort. In particular, we never need to compute the spin connection for EH. Nor do we ever need to compute the derivatives of the metric components. This is, of course, part of the magic of Kähler geometry.
3.7. Zero modes of the twisted Dirac operator on EH. We now proceed with the calculation using the EH metric in the form (2.25) and the connection (2.49). Write
$$W^{+}=\mathbb{C} \oplus \Lambda^{0,2}, \quad W^{-}=\Lambda^{0,1}$$
for the even and odd part of $\Lambda^{0, \bullet}$. A generic spinor $\sigma=\sigma_{+}+\sigma_{-}, \sigma_{ \pm} \in W^{ \pm}$, has the form
$$\sigma_{+}=\alpha+\delta \mathrm{d} \bar{z}_{1} \wedge \mathrm{~d} \bar{z}_{2}, \quad \sigma_{-}=\beta \mathrm{d} \bar{z}_{1}+\gamma \mathrm{d} \bar{z}_{2},$$
with $\alpha, \beta, \gamma, \delta$ functions of $z_{i}, \bar{z}_{i}, i=1,2$. However, we are twisting by a connection whose curvature is anti-self-dual, see (2.42). Such anti-self-dual curvature can only Clifford act nontrivially in (3.2) on spinors of one chirality. It can be checked that this are the spinors in $W^{-}$. This means that there are no non-trivial $L^{2}$ harmonic spinors in $W^{+}$. Hence we take
$$\sigma=\sigma_{-}=\beta \mathrm{d} \bar{z}_{1}+\gamma \mathrm{d} \bar{z}_{2} .$$
We calculate
$$\begin{aligned}
\mathrm{d} \sigma_{-} & =\partial_{z_{1}} \beta \mathrm{~d} z_{1} \wedge \mathrm{~d} \bar{z}_{1}+\partial_{z_{2}} \beta \mathrm{~d} z_{2} \wedge \mathrm{~d} \bar{z}_{1}+\partial_{z_{1}} \gamma \mathrm{~d} z_{1} \wedge \mathrm{~d} \bar{z}_{2}+\partial_{z_{2}} \gamma \mathrm{~d} z_{2} \wedge \mathrm{~d} \bar{z}_{2} \\
& +\left(\partial_{\bar{z}_{1}} \gamma-\partial_{\bar{z}_{2}} \beta\right) \mathrm{d} \bar{z}_{1} \wedge \mathrm{~d} \bar{z}_{2}
\end{aligned}$$
The second line belongs to $W^{+}$while, as discussed, we need to contract the first line with the inverse metric, getting
$$D \sigma_{-}=g_{z_{1} \bar{z}_{1}}^{-1} \partial_{z_{1}} \beta+g_{z_{2} \bar{z}_{1}}^{-1} \partial_{z_{2}} \beta+g_{z_{1} \bar{z}_{2}}^{-1} \partial_{z_{1}} \gamma+g_{z_{2} \bar{z}_{2}}^{-1} \partial_{z_{2}} \gamma+\left(\partial_{\bar{z}_{1}} \gamma-\partial_{\bar{z}_{2}} \beta\right) \mathrm{d} \bar{z}_{1} \wedge \mathrm{~d} \bar{z}_{2} .$$
Substituting (2.29) we obtain
$$\begin{aligned}
D \sigma_{-} & =\frac{1}{s}\left(F\left|z_{1}\right|^{2}+F^{-1}\left|z_{2}\right|^{2}\right) \partial_{z_{1}} \beta+\frac{1}{s}\left(F-F^{-1}\right)\left(\bar{z}_{1} z_{2} \partial_{z_{2}} \beta+\bar{z}_{2} z_{1} \partial_{z_{1}} \gamma\right)+\frac{1}{s}\left(F\left|z_{2}\right|^{2}+F^{-1}\left|z_{1}\right|^{2}\right) \partial_{z_{2}} \gamma \\
& +\left(\partial_{\bar{z}_{1}} \gamma-\partial_{\bar{z}_{2}} \beta\right) \mathrm{d} \bar{z}_{1} \wedge \mathrm{~d} \bar{z}_{2}
\end{aligned}$$
which can be rewritten in the form
$$D \sigma_{-}=\left(\frac{F-F^{-1}}{s}\right)\left(z_{1} \partial_{z_{1}}+z_{2} \partial_{z_{2}}\right)\left(\bar{z}_{1} \beta+\bar{z}_{2} \gamma\right)+F^{-1}\left(\partial_{z_{1}} \beta+\partial_{z_{2}} \gamma\right)+\left(\partial_{\bar{z}_{1}} \gamma-\partial_{\bar{z}_{2}} \beta\right) \mathrm{d} \bar{z}_{1} \wedge \mathrm{~d} \bar{z}_{2} .$$
Consider now the action of the connection (2.49). We calculate
$$\mathcal{A} \cdot \sigma_{-}=\frac{\ell \sqrt{\kappa}}{2 F s^{2}}\left(z_{1} \gamma-z_{2} \beta\right) \mathrm{d} \bar{z}_{1} \wedge \mathrm{~d} \bar{z}_{2}-\frac{\ell \sqrt{\kappa}}{2 s^{2}}\left(\bar{z}_{1} \beta+\bar{z}_{2} \gamma\right) .$$
Putting all together, the twisted Dirac equation is
$$\begin{aligned}
D_{\mathcal{A}} \sigma_{-} & =\left(\left(\frac{F-F^{-1}}{s}\right)\left(z_{1} \partial_{z_{1}}+z_{2} \partial_{z_{2}}\right)-\frac{\ell \sqrt{\kappa}}{2 s^{2}}\right)\left(\bar{z}_{1} \beta+\bar{z}_{2} \gamma\right)+F^{-1}\left(\partial_{z_{1}} \beta+\partial_{z_{2}} \gamma\right) \\
& +\left(\partial_{\bar{z}_{1}} \gamma-\partial_{\bar{z}_{2}} \beta+\frac{\ell \sqrt{\kappa}}{2 F s^{2}}\left(z_{1} \gamma-z_{2} \beta\right)\right) \mathrm{d} \bar{z}_{1} \wedge \mathrm{~d} \bar{z}_{2}=0
\end{aligned}$$

We take the ansatz, which solves the $\Lambda^{0,2}$ part of (3.35),
$$\beta=z_{1}^{N-m+1} z_{2}^{N+m} h(s), \quad \gamma=z_{1}^{N-m} z_{2}^{N+m+1} h(s)$$
for $h(s)$ an function of $s$ to be determined below. Here $N \geq 0$ is such that $2 N \in \mathbb{Z}, m=$ $\{-N,-N+1, \ldots, N\}$. The reason for this particular ansatz is that, since the left $S U(2)$ action on $\left(z_{1}, z_{2}\right)$ is an isometry, spinors can be decomposed into irreducible $S U(2)$ representations. By taking $\beta, \gamma$ as in (3.36) we have
$$\sigma_{-}=h z_{1}^{N-m} z_{2}^{N+m}\left(\bar{z}_{1} \mathrm{~d} z_{1}+\bar{z}_{2} \mathrm{~d} z_{2}\right),$$
where $h\left(\bar{z}_{1} \mathrm{~d} z_{1}+\bar{z}_{2} \mathrm{~d} z_{2}\right)$ is $S U(2)$-invariant and the space of homogeneous polynomials in $z_{1}, z_{2}$ of degree $2 N$ gives the $S U(2)$ irrep of dimension $2 N+1$.

The $\Lambda^{0}$ part of (3.35) now reduces to
$$F^{2}\left(2 N h+(h s)^{\prime}\right)+h=\frac{\ell}{2} \sqrt{\kappa} \frac{h F}{s},$$
which is solved by
$$h=\left(\frac{1}{F s^{2 N+2}}\right) \frac{1}{f^{\ell}},$$
where
$$f=\sqrt{1+\frac{\kappa}{s^{2}}}+\frac{\sqrt{\kappa}}{s}$$
is the same function as (2.59). Thus, we have found the following zero modes
$$\sigma_{-}=\frac{z_{1}^{N-m} z_{2}^{N+m}}{F s^{2 N+2} f^{\ell}}\left(z_{1} \mathrm{~d} \bar{z}_{1}+z_{2} \mathrm{~d} \bar{z}_{2}\right) .$$
3.8. Normalisability. Let us discuss normalisability. Using (2.29) we calculate
$$\left|z_{1} \mathrm{~d} \bar{z}_{1}+z_{2} \mathrm{~d} \bar{z}_{2}\right|^{2}=\left|z_{1}\right|^{2} \frac{F\left|z_{1}\right|^{2}+F^{-1}\left|z_{2}\right|^{2}}{s}+\left|z_{2}\right|^{2} \frac{F\left|z_{2}\right|^{2}+F^{-1}\left|z_{1}\right|^{2}}{s}+2 \frac{F-F^{-1}}{s}\left|z_{1}\right|^{2}\left|z_{2}\right|^{2}=F s,$$
hence
$$\left|\sigma_{-}\right|^{2}=\frac{\left|z_{1}\right|^{2(N-m)}\left|z_{2}\right|^{2(N+m)}}{F s^{4 N+3} f^{2 \ell}} .$$
As discussed previously, EH asymptotically approaches the flat metric on $\mathbb{C}^{2} / \mathbb{Z}_{2}$ with radial coordinate $r=\sqrt{s}=\sqrt{\left|z_{1}\right|^{2}+\left|z_{2}\right|^{2}}$ and volume element $\sim r^{3} \mathrm{~d} r$. We need to check the $L^{2}$ condition for small and large $r$. For large $r, f \sim F \sim 1$ hence
$$\left|\sigma_{-}\right|^{2} r^{3} \sim \frac{1}{r^{4 N+3}}$$
and the $L^{2}$ condition gives $N>-1 / 2$, which is satisfied by any non-negative half-integer $N$. For small $r, f \sim F \sim r^{-2}$, hence
$$\left|\sigma_{-}\right| r^{3} \sim r^{2 \ell-4 N-1},$$
hence a normalisable spinor needs to satisfy $2 N<\ell$.
In conclusion, harmonic spinors belong to $S U(2)$ representations of dimension $2 N+1$. A spinor is normalisable if and only if
$$1 \leq 2 N+1 \leq \ell$$
where $\ell \in \mathbb{Z}$ is the flux of the curvature 2-form $\mathrm{d} \mathcal{A}$. Here we have assumed $\ell>0$, the case $\ell<0$ can be treated similarly. As we already knew, in the untwisted case $\ell=0$ there are no normalisable zero modes. For $\ell=1$ we have only the singlet zero mode, for $\ell=2$ we have both the singlet and doublet, and so on, for a total of $\ell(\ell+1) / 2$ zero modes for general $\ell$.

\section*{4. The general case}
4.1. Calabi's metric on $\mathcal{O}(-n-1)$. We now apply Calabi's construction to the canonical bundle $K=\mathcal{O}(-n-1) \rightarrow \mathbb{C} P^{n}$ over $\mathbb{C} P^{n}$ equipped with the Fubini-Study metric. Applying the construction of Appendix B. 2 to $M=\mathbb{C} P^{n}$ we get, for $\lambda \neq 0, \kappa>0$ arbitrary constants,
$$\begin{aligned}
\omega & =\lambda u \omega_{\mathbb{C} P^{n}}+i(n+1)(\lambda u)^{-n} \theta \wedge \bar{\theta}, \\
g & =\lambda u g_{\mathbb{C} P^{n}}+2(n+1)(\lambda u)^{-n}|\theta|^{2} .
\end{aligned}$$
Here
$$u=\left(c|\zeta|^{2}+\kappa\right)^{\frac{1}{n+1}},$$
and, for $\zeta$ a complex coordinate on the fibres,
$$\theta=\mathrm{d} \zeta+\alpha \zeta$$
with $\alpha$ the Chern connection on $K$. Its curvature $\mathrm{d} \alpha$ satisfies
$$-i \mathrm{~d} \alpha=\frac{s_{\mathbb{C}} P^{n}}{2 n} \omega_{\mathbb{C} P^{n}},$$
where $s_{\mathbb{C} P^{n}}$ is the scalar curvature of the FS metric. The constants $c$ and $\lambda$ are related by
$$c=\frac{s_{\mathbb{C} P^{n}}(n+1)^{2}}{2 n \lambda^{n+1}} .$$

Let $\left(w_{i}\right), i=1, \ldots, n$, be inhomogeneous coordinates on $\mathbb{C} P^{n}$. With respect to the local Kähler potential
$$\mathcal{K}=\frac{C}{2} \log \left(1+|w|^{2}\right),$$
where $|w|^{2}=\left|w_{1}\right|^{2}+\cdots+\left|w_{n}\right|^{2}, C \in \mathbb{R}^{\times}$is some constant, the FS metric and Kähler form take the form $\left(g_{\mathbb{C} P^{n}}\right)_{\mu \bar{\nu}}=\partial_{\mu} \partial_{\bar{\nu}} \mathcal{K},\left(\omega_{\mathbb{C} P^{n}}\right)_{\mu \bar{\nu}}=i\left(g_{\mathbb{C} P^{n}}\right)_{\mu \bar{\nu}}$. The scalar curvature is related to $C$ by
$$s_{\mathbb{C} P^{n}}=\frac{4 n(n+1)}{C} .$$
Since
$$\partial \mathcal{K}=\frac{C}{2} \frac{\bar{w} \mathrm{~d} w}{1+|w|^{2}}, \quad \bar{\partial} \mathcal{K}=\overline{\partial \mathcal{K}}$$
the Kähler form of $\mathbb{C} P^{n}$ can be written
$$\omega_{\mathbb{C} P^{n}}=\frac{i}{2}(\partial \bar{\partial} \mathcal{K}-\bar{\partial} \partial \mathcal{K})=\frac{i}{2} \mathrm{~d}(\bar{\partial} \mathcal{K}-\partial \mathcal{K}),$$
so that
$$\mathrm{d} \alpha=-\left(\frac{n+1}{C}\right) \mathrm{d}(\bar{\partial} \mathcal{K}-\partial \mathcal{K}) .$$
Hence up to the addition of a closed form
$$\alpha=2 i\left(\frac{n+1}{2}\right) \frac{\operatorname{Im}(\bar{w} \mathrm{~d} w)}{1+|w|^{2}} .$$
Note that $\alpha$ is purely imaginary. As we did for $n=1$ we write
$$\alpha=2 i a, \quad a=\frac{1}{2 i}\left(\frac{n+1}{2}\right)\left(\frac{\bar{w} \mathrm{~d} w-w \mathrm{~d} \bar{w}}{1+|w|^{2}}\right) .$$
4.2. Rewriting in terms of "symmetrical" coordinates. Introducing the homogeneous coordinates $\left(z_{i}\right), i=1, \ldots, n+1$, related to $\left(z_{i}\right)$ by $w_{i}=\frac{z_{i}}{z_{n+1}}$, the FS metric on $\mathbb{C} P^{n}$ can also be written as (the pullback along a holomorphic section of)
$$g_{\mathbb{C} P^{n}}=\frac{1}{s^{2}} \sum_{1 \leq i<j \leq n+1}\left|z_{i} \mathrm{~d} z_{j}-z_{j} \mathrm{~d} z_{i}\right|^{2}$$
where
$$s=\left|z_{1}\right|^{2}+\cdots+\left|z_{n+1}\right|^{2} .$$
We will also need the analogous of the identity (2.68), which for general $n$ reads
$$s|\mathrm{~d} z|^{2}=|\bar{z} \mathrm{~d} z|^{2}+\sum_{1 \leq i<j \leq n+1}\left|z_{i} \mathrm{~d} z_{j}-z_{j} \mathrm{~d} z_{i}\right|^{2} .$$
We are using the notation $z=\left(z_{1}, \ldots z_{n+1}\right)$ and denoting the dot product by juxtaposition so that e.g.
$$\bar{z} \mathrm{~d} z=\bar{z}_{1} \mathrm{~d} z_{1}+\cdots+\bar{z}_{n+1} \mathrm{~d} z_{n+1}=\partial s .$$

Having collected all the ingredients, we would like to rewrite the Calabi metric in term of the complex coordinates $\left(z_{i}\right)$. The base-fibre coordinates $\left(w_{i}, \zeta\right)$ are related to the more "symmetrical" coordinates $\left(z_{i}\right)$ by
$$w_{i}=\frac{z_{i}}{z_{n+1}}, i=1, \ldots, n, \quad \zeta=s^{\frac{n+1}{2}}\left(\frac{z_{n+1}}{\bar{z}_{n+1}}\right)^{\frac{n+1}{2}},$$
with inverse
$$z_{i}=w_{i} \frac{\zeta^{\frac{1}{n+1}}}{\sqrt{1+|w|^{2}}}, i=1, \ldots, n, \quad z_{n+1}=\frac{\zeta^{\frac{1}{n+1}}}{\sqrt{1+|w|^{2}}}$$

One calculates
$$\bar{z} \mathrm{~d} z=|\zeta|^{\frac{2}{n+1}} \frac{1}{2}\left(\frac{\bar{w} \mathrm{~d} w-w \mathrm{~d} \bar{w}}{1+|w|^{2}}\right)+\left(\frac{1}{n+1}\right) \frac{\bar{\zeta} \mathrm{d} \zeta}{|\zeta|^{\frac{2 n}{n+1}}},$$
so that, using (4.13), we have
$$(n+1) \bar{z} \mathrm{~d} z=\frac{\bar{\zeta}}{|\zeta|^{\frac{2 n}{n+1}}}(\mathrm{~d} \zeta+\alpha \zeta)=\frac{\bar{\zeta}}{|\zeta|^{\frac{2 n}{n+1}}} \theta$$
It follows
$$|\theta|^{2}=(n+1)^{2} s^{n-1}|\bar{z} \mathrm{~d} z|^{2} .$$
Note that, since $\alpha$ is purely imaginary, taking the real and imaginary part of (4.21) we get
$$\mathrm{d} s=\mathrm{d}\left(|\zeta|^{2}\right)^{\frac{1}{1+n}},$$
in agreement with (4.18), and
$$(n+1) \operatorname{Im}(\bar{z} \mathrm{~d} z)=|\zeta|^{\frac{2}{n+1}} \alpha+\frac{\operatorname{Im}(\bar{\zeta} \mathrm{d} \zeta)}{|\zeta|^{\frac{2 n}{n+1}}}$$

We can now rewrite 4.2 in terms of the coordinates $\left(z_{i}\right)$. Using (4.16) we have
$$\begin{aligned}
g & =\lambda u g_{\mathbb{C} P^{n}}+2(n+1)(\lambda u)^{-n}|\theta|^{2}=\frac{2 \lambda u}{s_{1 \leq i<j \leq n+1}^{2}} \sum_{i}\left|z_{i} \mathrm{~d} z_{j}-z_{j} \mathrm{~d} z_{i}\right|^{2}+2(n+1)(\lambda u)^{-n}|\theta|^{2} \\
& =\frac{2 \lambda u}{s^{2}}\left(s|\mathrm{~d} z|^{2}-|\bar{z} \mathrm{~d} z|^{2}\right)+2(n+1)(\lambda u)^{-n}|\theta|^{2}
\end{aligned}$$
We now rescale $\zeta \rightarrow \frac{\zeta}{(n+1)^{3 / 2}}$, so that by (4.22),
$$|\theta|^{2} \rightarrow \frac{|\theta|^{2}}{(n+1)^{3}}=\frac{s^{n-1}}{n+1}|\bar{z} \mathrm{~d} z|^{2}$$
hence
$$g=2\left[\frac{\lambda u}{s}|\mathrm{~d} z|^{2}+\left(\frac{s^{n-1}}{(\lambda u)^{n}}-\frac{\lambda u}{s^{2}}\right)|\bar{z} \mathrm{~d} z|^{2}\right] .$$
We are going to drop the overall factor of 2 . Using the relation $|\zeta|=s^{\frac{n+1}{2}}$ to rewrite $u$ as a function of $s$ we obtain
$$\frac{\lambda u}{s}=\lambda c^{\frac{1}{n+1}}\left(1+\frac{\kappa}{c s^{n+1}}\right)^{\frac{1}{n+1}} .$$
Rescaling $\kappa \rightarrow c \kappa$ and choosing $c=\lambda^{-(n+1)}$ we define
$$F(s)=\frac{\lambda u}{s}=\left(1+\frac{\kappa}{s^{n+1}}\right)^{\frac{1}{n+1}},$$
so that
$$F^{\prime}=\frac{1-F^{n+1}}{F^{n} s}=\frac{s^{n-1}}{(\lambda u)^{n}}-\frac{\lambda u}{s^{2}} .$$
Therefore, the Calabi metric on $\mathcal{O}(-n-1)$ is given in terms of the coordinates $\left(z_{i}\right)$ by
$$g=F|\mathrm{~d} z|^{2}+F^{\prime}|\bar{z} \mathrm{~d} z|^{2} .$$
Since $F$ only depends on $s$, it is clear that the metric is invariant under the left action of $U(n+1)$ on $\mathbb{C}^{n+1}$. The Kähler form corresponding to (4.31) is
$$\omega=2 i\left(F \mathrm{~d} z \wedge \mathrm{~d} \bar{z}+F^{\prime} \bar{z} \mathrm{~d} z \wedge z \mathrm{~d} \bar{z}\right)=2 i \mathrm{~d}(F z \mathrm{~d} \bar{z}) .$$

For small $s, F \sim s$ and $\operatorname{Re}(F z \mathrm{~d} \bar{z}) \sim \frac{1}{2} \mathrm{~d} \log s$, so $F z \mathrm{~d} \bar{z}$ is not well-defined for $s=0$ and $\omega$ is not exact. Note that for $n=1$ (4.31) reduces to
$$g=F|\mathrm{~d} z|^{2}+\frac{1}{s}\left(\frac{1}{F}-F\right)|\bar{z} \mathrm{~d} z|^{2}, \quad F=\sqrt{1+\frac{\kappa}{s^{2}}}$$
and we recover (2.66).
The function $F$ satisfies the identity
$$F^{\prime}=\frac{1}{s}\left(\frac{1}{F^{n}}-F\right) \quad \Leftrightarrow \quad F^{n}(s F)^{\prime}=1 .$$
In components
$$g_{\mu \bar{\nu}}=\partial_{\mu}\left(F z_{\nu}\right)=F^{\prime} \bar{z}_{\mu} z_{\nu}+F \delta_{\mu \nu},$$
with determinant
$$\operatorname{det}\left(g_{\mu \bar{\nu}}\right)=F^{n}(F s)^{\prime}=1,$$
as it should be since the metric is Ricci-flat. The inverse of the matrix $g_{\mu \bar{\nu}}$ has components
$$g^{\rho \bar{\nu}}=\frac{\delta^{\rho \nu}}{F}+\frac{\kappa}{s^{n+2} F} \bar{z}^{\rho} z^{\nu} .$$
4.3. $U(1)$ connection with $L^{2}$ harmonic curvature. The canonical spin- $c$ structure on $K$ admits no non-trivial $L^{2}$ harmonic spinor, hence to get non-trivial zero modes we need to twist by a line bundle equipped with a $U(1)$ connection $\mathcal{A}$. The curvature $\mathrm{d} \mathcal{A}$ is a purely imaginary form of degree $(1,1)$ which we also want to be $L^{2}$ harmonic.

The space of $L^{2}$ harmonic forms on $K$ is 1-dimensional. In fact, in the setting of [5], the Calabi metric on $K$ is a scattering metric, with $K$ viewed as a fibration with trivial fibre and $X=\bar{L}$. By Theorem 1A of [5], the space $L^{2} \mathcal{H}^{k}$ of $L^{2}$ harmonic $k$-forms is
$$L^{2} \mathcal{H}^{k}(K)= \begin{cases}H^{k}(K, \partial K) & \text { if } k<n+1 \\ \operatorname{Im}\left(H^{k}(K, \partial K) \rightarrow H^{k}(K)\right) & \text { if } k=n+1 \\ H^{k}(K) & \text { if } k>n+1\end{cases}$$
where $H^{k}(K, \partial K) \rightarrow H^{k}(K)$ is the inclusion map. We have
$$H^{k}(K) \simeq H^{k}\left(\mathbb{C} P^{n}\right)=\left\{\begin{array}{lc}
\mathbb{R} & \text { if } k=0,2,4, \ldots, 2 n \\
0 & \text { otherwise }
\end{array}\right.$$
and, using Poincaré duality,
$$H^{k}(K, \partial K) \simeq H_{c}^{k}(K) \simeq H^{2 n+2-k}(K)=\left\{\begin{array}{lc}
\mathbb{R} & \text { if } k=2,4, \ldots, 2 n+2, \\
0 & \text { otherwise } .
\end{array}\right.$$
Finally the inclusion
$$\iota: H_{c}^{n+1}(K) \rightarrow H^{n+1}(K) .$$
is the zero map for $n$ even, as $H_{c}^{n+1}(K)=0$, and an isomorphism for $n$ odd. In conclusion
$$L^{2} \mathcal{H}^{k}(K)= \begin{cases}\mathbb{R} & \text { if } k=2,4, \ldots, 2 n, \\ 0 & \text { otherwise } .\end{cases}$$
In particular, $L^{2} \mathcal{H}^{2}(K)$ is 1-dimensional.
We now show that we can write a generator $\tilde{\omega}$ of $L^{2} \mathcal{H}^{2}(K)$ in the form $\tilde{\omega}=2 i \mathrm{~d} \beta$ for $\beta \in$ $\Lambda^{0,1}(K)$ a Dirac zero mode. This extends the phenomenon observed in the case of the Calabi metric for $\mathbb{C P}^{1}$, where we had $\tilde{\omega}=2 i \mathrm{~d} \beta$ with $\beta$ given by (2.42). Furthermore, the explicit form (3.41) of the zero modes of the twisted Dirac operator shows that $\beta$ is the $N=0$ zero mode of the untwisted Dirac operator, something which also holds for general $n$.

By the local $\partial \bar{\partial}$ lemma we can write $\tilde{\omega}=2 i \partial \bar{\partial} \phi$ for some locally defined real function $\phi$. Set
$$\beta=\bar{\partial} \phi .$$