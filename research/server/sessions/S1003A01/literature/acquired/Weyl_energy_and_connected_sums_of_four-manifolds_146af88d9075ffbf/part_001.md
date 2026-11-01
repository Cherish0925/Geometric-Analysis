---
retention_scope: session
part: 1
total_parts: 3
---

[Part 1/3 of: Weyl energy and connected sums of four-manifolds]

---
source_file: 2505_17752v1.pdf
converter: mathpix
format: mmd
---

\title{
Weyl energy and connected sums of four-manifolds
}

\author{
Andrea Malchiodi and Francesco Malizia*
}

\begin{abstract}
Given two closed, oriented Riemannian four-manifolds $\left(M, g_{M}\right)$ and $\left(Z, g_{Z}\right)$, which are not locally conformally flat and not both self-dual or both anti-self-dual, we prove that there exists a metric $g_{Y}$ on the connected sum $Y \cong M \# Z$ such that the Weyl energy of $g_{Y}$ is strictly smaller than the sum of Weyl energies of $g_{M}$ and $g_{Z}$.
\end{abstract}

Key Words: Weyl Functional, Conformal Geometry.
MSC 2020: 53C21, 58E11, 49J99.

\section*{Contents}
1 Introduction ..... 1
2 Preliminaries ..... 9
3 The connected sum setup ..... 13
4 Biharmonic interpolation ..... 16
5 Comparison of Weyl energies ..... 20
6 Proof of Theorem 1.1 ..... 33
A Appendix ..... 35
References ..... 37

\section*{1 Introduction}

One of the main goals of Riemannian geometry is to understand the relation between curvature and topology of smooth manifolds. In particular, when $M$ is a closed 4-dimensional manifold, one of the best kinds of metrics one can hope to have are Einstein metrics, that is, metrics $g$ satisfying
$$\operatorname{Ric}(g)=\lambda g,$$
for some real constant $\lambda$. In the Lorentzian context, Einstein metrics are solutions to the Einstein field equations (with cosmological constant) of General Relativity; even in the Riemannian setting, they are intensively studied because of the homogeneity of their Ricci curvature, which provides good (orbifold) compactness properties resulting in a nice description of their moduli space, see e.g. [And89], [BKN89]. Roughly speaking, the above Einstein condition corresponds, in a suitable gauge, to a determined

\footnotetext{
*Scuola Normale Superiore, Piazza dei Cavalieri 7, 56126 Pisa. e-mails: andrea.malchiodi@sns.it, francesco.malizia@sns.it
}
elliptic PDE system for the metric tensor ([Bes08, Chapter 5]), whereas other constant curvature conditions correspond to either underdetermined (scalar curvature) or overdetermined (Riemann curvature tensor) constraints, resulting in abundance or rareness of their respective associated metrics. Moreover, dimension 4 appears to be the critical one for the Einstein condition because of its flexibility: indeed, in dimensions 2 and 3 it implies that the manifold has constant sectional curvature, while in dimension 5 or higher there are no known obstructions to the existence of Einstein metrics and there might actually be too many of them, see [Gro00].

Einstein metrics have a variational characterization: a metric is Einstein on a 4-manifold $M$ if and only if it is a critical point for the normalized Einstein-Hilbert functional
$$\mathcal{E}(g)=\operatorname{Vol}(M, g)^{-\frac{1}{2}} \int_{M} R_{g} d V_{g}$$
where $R_{g}$ denotes the scalar curvature of $g$. One could then expect to obtain existence of Einstein metrics through variational methods; however, this is extremely difficult in practice: critical points of $\mathcal{E}$ possess infinitely many stable and unstable directions ([Sch89]).

Even worse, it is known that not all closed 4-manifolds do admit an Einstein metric: for instance, the Hitchin-Thorpe inequality [Tho69; Hit74],
$$2 \chi(M) \geq 3|\tau(M)|,$$
is a well-known necessary condition for the existence of Einstein metrics on a given oriented manifold; here $\chi$ is the Euler characteristic and $\tau$ is the signature of the intersection form, see e.g. [Bes08] for further information.

This leads us to ask whether it is possible to find other canonical metrics which are less obstructed than Einstein ones. Recall that, on closed 4-manifolds, the (0, 4)-curvature tensor admits the following $L^{2}$-orthogonal decomposition:
$$\operatorname{Riem}=W \oplus E \oplus g \oplus \frac{R_{g}}{12} g \oplus g ;$$
here ⊕ is the Kulkarni-Nomizu product (defined as in (2.1)), $E:=\operatorname{Ric}-\frac{R_{g}}{4} g$ denotes the traceless Ricci tensor and $W$ is the Weyl curvature tensor, which is the conformally covariant part of the Riemann tensor. Some interesting metrics are those arising as critical points of quadratic curvature functionals ([Bes08, Chapter 4]); in particular, in this paper we will focus on the Weyl functional
$$\mathcal{W}^{M}(g):=\int_{M}\left|W^{g}\right|^{2} d V_{g}$$
Critical points of (1.2) are called Bach-flat metrics, and they satisfy the Euler-Lagrange equation
$$B_{i j}:=-4\left(\nabla^{\alpha} \nabla^{\beta} W_{\alpha i j \beta}+\frac{1}{2} R^{\alpha \beta} W_{\alpha i j \beta}\right)=0,$$
where $B=B_{i j}$ is the so-called Bach tensor, see [Bac21], [Kob85]. One can directly check that all Einstein metrics are Bach-flat, and so are metrics conformal to an Einstein one. Other special examples of Bach-flat metrics are self-dual and anti-self-dual metrics (see Remark 1.2 (a) and (c) below), whose existence, however, is also obstructed on some manifolds (by the signature formula (1.10)). Notice also that there are very few known examples of Bach-flat metrics which are not of the two types mentioned above, see [AGS13] and the references therein.

Now, to the best of the authors' knowledge, there are no known obstructions to the existence of Bach-flat metrics on closed 4-manifolds. It is therefore tempting to try looking for critical points, in particular minima, of (1.2). However, this is by no means an easy task: like all other
curvature functionals, the Weyl functional is invariant under the action of the diffeomorphism group of $M$; moreover, it is also invariant under conformal transformations of the metric, so that actually $\mathcal{W}(g)=\mathcal{W}([g])$. This double invariance generates analytic difficulties, even locally, as the Bach operator $B$ is not elliptic in general: one has to consider, for instance, combinations like harmonic coordinates and constant scalar curvature conformal metric in order to (locally) turn $B$ into an elliptic operator, see e.g. [And05]. This has also repercussions for the parabolic Bach flow, for which short-time existence and uniqueness have been proved via a conformal adjustment that deals with the gauge invariances along the lines of DeTurck's trick, see [BH11], [BH15], [CLQ23].
In the global picture, the study of minimizing sequences for the Weyl functional, or, more realistically, for a suitable regularized/subcritical version of it, requires to deal with the possible occurrence of collapses with bounded curvature (in the sense of Cheeger and Gromov [CG86; CG90]) or formation of orbifold singularities, see the discussion in [And06]. In particular, similarly to Einstein metrics, we know that, under suitable bounds on the curvature and volume, sequences of Bach-flat metrics are, a priori, only orbifold precompact, see [And05], [TV05a], [TV05b], [TV08]. As a consequence, since general minimizing sequences will at least develop all the possible degenerations of the related moduli space of minima, it is necessary to understand under which assumptions it is possible to exclude the formation of orbifold singularities.

An instructive example of how to deal with some degeneration phenomena comes from the analysis of Willmore surfaces, that is, immersed surfaces $f: \Sigma^{\rho} \rightarrow \mathbb{R}^{n}$ which are critical for the Willmore energy
$$\mathbb{W}(f):=\frac{1}{4} \int_{\Sigma^{\rho}}|H|^{2} d \mu$$
where $H \in \mathbb{R}^{n}$ is the mean curvature vector, $\Sigma^{\rho}$ a closed surface of genus $\rho \in \mathbb{N}_{\geq 0}$ and $\mu$ the induced surface measure. In [Sim86; Sim93], Simon employed the direct method in the calculus of variations to minimize the Willmore energy among immersed surfaces of fixed genus $\rho \geq 1$. Although in the case $\rho=1$ he was able to prove the existence of a smooth minimal torus, the occurrence of topology degenerations in the limit was not excluded in the higher genus case $\rho \geq 1$. In other words, there was the possibility for a genus $\rho$ minimizing sequence to converge (in Hausdorff distance and weak measure sense) to a closed smooth embedding of lower genus $\rho_{0}<\rho$. In general, given $\rho>1$, Simon [Sim93, Theorem 3.1] proved that there exists a partition $\rho=\rho_{1}+\cdots+\rho_{m}$ (with $\rho_{1}, \ldots, \rho_{m} \geq 1$ ) such that, letting
$$\beta_{\rho}:=\inf \left\{\mathbb{W}(f) \mid f: \Sigma^{\rho} \rightarrow \mathbb{R}^{n}\right\},$$
then each $\beta_{\rho_{i}}$ is attained and one has $\beta_{\rho}-4 \pi=\beta_{\rho_{1}}+\cdots+\beta_{\rho_{m}}-4 \pi m$.
The occurrence of $m \geq 2$ was later ruled out by Bauer and Kuwert in [BK03] (see also [Kus96]) through the following strategy: they proved that, letting $f_{i}: \Sigma^{\rho_{i}} \rightarrow \mathbb{R}^{n}, i=1,2$ be two immersed surfaces which are both different from a round sphere, then it is possible to find an immersed surface $f: \Sigma^{\rho} \rightarrow \mathbb{R}^{n}$ with the topology of the connected sum (i.e. $\Sigma^{\rho} \cong \Sigma^{\rho_{1}} \# \Sigma^{\rho_{2}}$ ) satisfying
$$\mathbb{W}(f)<\mathbb{W}\left(f_{1}\right)+\mathbb{W}\left(f_{2}\right)-4 \pi .$$
With this result at hand, assuming e.g. $\beta_{\rho}=\beta_{\rho_{1}}+\beta_{\rho_{2}}-4 \pi$ in Simon's result and letting, for $i=1,2$, $f_{i}: \Sigma^{\rho_{i}} \rightarrow \mathbb{R}^{n}$ be two immersions minimizing $\mathbb{W}$, then (1.4) readily gives a contradiction. Therefore, for any genus $\rho \geq 0$, the infimum of Willmore's energy among immersions of $\Sigma^{\rho}$ into $\mathbb{R}^{n}$ is attained by a surface of genus $\rho$ (in case $\rho=0$ the infimum is achieved by the round sphere).

In this paper, we start an analogous program of studying the behavior of Weyl energy under the connected sum operation by establishing a partial analogue of (1.4). The result is as follows.

Theorem 1.1. Let $\left(M, g_{M}\right),\left(Z, g_{Z}\right)$ be two 4-dimensional closed, connected, oriented manifolds, and let $Y:=Z \# M$ denote their connected sum. Assume that $g_{M}, g_{Z}$ are not locally conformally flat and that they are not both self-dual or both anti-self-dual. Then there exists a metric $g_{Y}$ on $Y$ such that
$$\mathcal{W}^{Y}\left(g_{Y}\right)<\mathcal{W}^{M}\left(g_{M}\right)+\mathcal{W}^{Z}\left(g_{Z}\right) .$$

Before describing the strategy behind the proof of Theorem 1.1, we comment on its assumptions.
Remark 1.2. (a) On a closed oriented 4-manifold, the Weyl tensor $W$ decomposes into its self-dual (SD) part $W_{+}$and anti-self-dual (ASD) part $W_{-}$under the action of the Hodge * operator: $W=W_{+}+W_{-}$, see Section 2. As a consequence, $(M, g)$ is said to be self-dual (respectively, anti-self-dual) if $W \equiv W_{+}$on $M$ (respectively, $W \equiv W_{-}$). A metric is locally conformally flat (LCF) if $W \equiv 0$. Of course, LCF metrics are both SD and ASD; moreover, these three conditions are all invariant under conformal transformations.
\begin{itemize}
\item[(b)] As it will be clear from the proof, the key idea which allows us to decrease the Weyl energy on $Y$ is to take advantage of the interaction between the Weyl energies of $g_{M}$ and $g_{Z}$ in the gluing region; however, the interaction is always of higher order when the assumptions of Theorem 1.1 are not satisfied.
\item[(c)] In the particular case where both metrics are self-dual (respectively, anti-self-dual) and the second cohomology groups associated to their SD deformation complexes (respectively, ASD) are trivial,
$$H_{\mathrm{SD}}^{2}\left(M, g_{M}\right)=\{0\}, \quad H_{\mathrm{SD}}^{2}\left(Z, g_{Z}\right)=\{0\}$$
then there exists a SD (respectively, ASD) metric on $M \# Z$ by virtue of a theorem due to Donaldson and Friedman [DF89], which relies upon the deformation theory of compact complex spaces. See also the paper [Flo91] by Floer, who established the existence of SD metrics for connected sums of $\mathbb{C P}^{2}$ 's via gluing techniques. Since SD (and ASD) metrics are global minimizers for the Weyl functional ${ }^{1}$ and the techniques employed by Donaldson-Friedman and Floer are of perturbative nature, it follows that the infimum of Weyl energy is additive in such cases. In other words, there is no hope to extend the result of Theorem 1.1 to the general case in which both manifolds are SD or both ASD.
We also point out that there is a conjecture, attributed to Singer, which states that any SD manifold ( $M, g$ ) of positive Yamabe class, $Y(M,[g])>0$, actually satisfies $H_{\text {SD }}^{2}(M, g)=\{0\}$ (and same in ASD case); see [GG24] for an overview on this problem and related results.
\end{itemize}

We now briefly sketch the main ideas behind the proof of Theorem 1.1. The procedure is inspired by the one adopted by Bauer and Kuwert in [BK03] for the Willmore functional; broadly speaking, we perform a connected sum between $M$ and $Z$ along a very small neck in a way that decreases the energy. To begin, by the conformal invariance of Weyl functional, we can perform the following operations on $g_{M}$ and $g_{Z}$ without affecting the Weyl energy:
\begin{itemize}
\item[-] invert ${ }^{2}$ one manifold, say $M$, at a point $p$; denote by $\left(N=M \backslash\{p\}, g_{N}\right)$ the inverted manifold.
\item[-] Shrink $\left(N, g_{N}\right)$ into a manifold $\left(N, g_{a}\right)$ via the scaling $g_{a}:=a^{2} g_{N}$, for a small parameter $a \ll 1$.
\item[-] Enlarge $\left(Z, g_{Z}\right)$ into a manifold $\left(Z, g_{b}\right)$ via the scaling $g_{b}=b^{-2} g_{Z}:=\lambda^{-2} a^{-2} g_{Z}$, for some $\lambda>0$.
\end{itemize}

\footnotetext{
${ }^{1}$ This is an immediate consequence of the Hirzebruch signature formula (1.10), cf. [Via16, Proposition 5.12]; in particular, all these metrics are Bach-flat.
${ }^{2}$ While for the Willmore functional a spherical inversion is performed, here the inversion, also called conformal blow-up, is to be intended in (conformal) normal coordinates at a given point, see Section 3 for details.
}

We then consider two thick annuli of relative width $\gamma \ll 1$ (here by relative width we mean the ratio between inner radius and outer radius), one on the asymptotically flat (AF) end on $N$ and the other centered at a point $q \in Z$, and we glue them together, creating in this way a new manifold $Y \cong Z \# M$ (here we are discarding the region of the AF end of $N$ in the exterior of the annulus, as well as the ball centered at $q \in Z$ in the interior of the other annulus).

At this point, we define a new metric $g_{Y}$ on $Y$ which coincides with $g_{a}, g_{b}$ outside the gluing regions and which suitably interpolates between the two in the middle annulus. As in [BK03], it turns out that a nice way to interpolate between $g_{M}$ and $g_{Z}$ is by asking $g_{Y}$ to be biharmonic (with respect to the Euclidean metric and in suitable local coordinates) inside the gluing region. This is heuristically motivated as follows. After scaling, the metrics $g_{a}$ and $g_{b}$ are almost flat in the gluing regions, that is, we can regard them as first-order perturbations of the Euclidean metric $g_{E}$. Indeed, letting $t:=a^{2}$, one has
$$g_{a}=g_{E}+t F+O\left(t^{2}\right), \quad g_{b}=g_{E}+t \lambda^{2} H+O\left(t^{2}\right),$$
where $F$ and $H$ are transverse and traceless (TT) tensors. If we now expand the Weyl energy at the Euclidean metric (that is, at $t=0$ ), the first nonzero term is quadratic and depends upon the linearization of the Bach tensor, which, in this setting, is equal to the bilaplace operator, see (2.20) below (the additional terms in (2.20) are due to the presence of a boundary).

One then computes the energy balance $\mathcal{W}^{Y}\left(g_{Y}\right)-\mathcal{W}^{M}\left(g_{M}\right)-\mathcal{W}^{Z}\left(g_{Z}\right)$ between the glued metric and the starting ones; by construction, this difference will be equal to the Weyl energy of $g_{Y}$ in the annulus minus the Weyl energies of $g_{M}$ and $g_{Z}$ in the glued and cut out regions of $M$ and $Z$, respectively.

Looking at the first nonzero term in the expansion, we notice that its sign depends upon an interaction term between the Weyl energy of $M$ and that of $Z$ evaluated at their respective gluing points. To make a long story short, the energy balance is of the following type (cf. Proposition 5.13):
$$\mathcal{W}^{Y}\left(g_{Y}\right)-\mathcal{W}^{M}\left(g_{M}\right)-\mathcal{W}^{Z}\left(g_{Z}\right)=a^{4}\left(C-\frac{\pi^{2}}{9} \lambda^{2} W^{\bar{M}}(p) \circledast W^{Z}(q)+O\left(\lambda^{2} \gamma^{2}\right)\right)+\text { h.o.t., }$$
where $\bar{M}$ is the manifold $M$ with its opposite orientation (this switches the SD/ASD Weyl tensors, $\left.W_{ \pm}^{\bar{M}}=W_{\mp}^{M}\right), C$ is a constant depending upon $W^{\bar{M}}(p), \gamma$ is the aforementioned relative width of the gluing annulus and the interaction term has the form (cf. [GV16])
$$W^{\bar{M}}(p) \circledast W^{Z}(q):=\sum_{i, j, k, l} W_{k i j l}^{Z}(q)\left(W_{k i j l}^{\bar{M}}(p)+W_{l i j k}^{\bar{M}}(p)\right) .$$
After the gluing procedure, we are identifying $T_{p} \bar{M}$ with $T_{q} Z$, and we are expressing tensor components with respect to a common orthonormal basis. Notice that the right-hand side in (1.7) depends upon the identification of the two tangent spaces. Moreover, it clearly depends upon the basepoints themselves. This freedom will be crucially exploited in Section 6 in order to give (1.7) a positive sign, which allows to make (1.6) negative (for a large enough $\lambda$ ) and thus prove Theorem 1.1.

Remark 1.3. One actually has to be careful with the various parameters; in particular, in the end it will be necessary to choose $0<a \ll \gamma \ll \lambda^{-1}<1$, see the proof of Theorem 1.1.

Remark 1.4. Instead of working with a glued manifold $Y \cong M \# Z$, it will be easier in the next sections to perform a simpler gluing and consider $X \cong Z \# \bar{M}$, see Remarks 3.1 and 3.5.

Remark 1.5. The interaction term (1.7) plays a fundamental role also in the paper [GV16] by Gursky and Viaclovsky, from which we borrowed our notation. There, the authors construct critical metrics on connected sums of specific Einstein 4-manifolds by means of a gluing (in the sense of finite
dimensional reduction) procedure; the critical metrics in question are called $B^{t}$-flat by the authors, and are critical points for the functional
$$\mathcal{B}_{t}(g):=\int_{M}\left|W^{g}\right|^{2} d V_{g}+t \int_{M} R_{g}^{2} d V_{g}$$
In particular, (1.7) appears in [GV16] as a part of the coefficient (the other part is due to the scalar curvature and $t$ ) of the Kuranishi map corresponding to the infinitesimal kernel parameter given by the freedom of scaling one manifold while keeping the other fixed. Notice that, in the present paper, the interaction term (1.7) plays a similar role, as the parameter $\lambda$ in (1.6) describes indeed the relative scaling between the two manifolds. However, while Gursky and Viaclovsky do find critical points for the $\mathcal{B}_{t}$ functional above, here we are interested in obtaining estimates for the Weyl energy alone. Indeed, the non-vanishing of term in (1.7) seems to represent an obstruction to finding Bach-flat metrics on connected sums by gluing methods.

We now briefly comment on possible consequences of Theorem 1.1 to the study of the infimum of Weyl's functional and to the loss of topology or formation of orbifold singularities along minimizing sequences; we also mention some related works and future perspectives.

\section*{Infimum of the Weyl functional}

An interesting quantity to study is the infimum of Weyl functional among all Riemannian metrics on a given 4-manifold $M$ :
$$\mathcal{W}(M):=\inf _{g} \mathcal{W}^{M}(g)=\inf _{g} \int_{M}\left|W^{g_{M}}\right|^{2} d V_{g_{M}} .$$
In [Kob85], Osamu Kobayashi proved that the infimum of Weyl energy is subadditive with respect to the connected sum operation:
$$\mathcal{W}(M \# Z) \leq \mathcal{W}(M)+\mathcal{W}(Z) .$$

An immediate consequence of Theorem 1.1 is the following:
Corollary 1.6. Let $M, Z$ be two closed, oriented, connected 4-manifolds and let $Y:=Z \# M$ denote their connected sum. Assume that $\mathcal{W}(M), \mathcal{W}(Z)$ are strictly positive and that they are achieved at the conformal classes of $g_{M}$ and $g_{Z}$ respectively. Assume further that $g_{M}, g_{Z}$ are not both $S D$ or both ASD. Then
$$\mathcal{W}(Y)<\mathcal{W}(M)+\mathcal{W}(Z) .$$

Remark 1.7. The assumption $\mathcal{W}(M)>0$ implies that $M$ does not carry any locally conformally flat metric. On the other hand, notice that there are examples of closed 4-manifolds $M$ (e.g. $M=\mathbb{S}^{2} \times \mathbb{T}^{2}$ ) which do not carry any LCF metric while satisfying $\mathcal{W}(M)=0$, see [Kob85, p. 377]; in particular, the infimum of Weyl energy is never achieved on these manifolds.

Corollary 1.6 requires a priori the existence of minimizers on the manifolds $M$ and $Z$. Thus, it would be interesting to develop a variational theory for minimizing sequences of the Weyl energy.

After the work of Kobayashi, many results were obtained about the infimum of Weyl functional on manifolds admitting particular Riemannian metrics. One of the principal ones is due to Gursky, who proved a lower bound for the self-dual Weyl energy of positive Yamabe metrics over manifolds whose intersection form possesses at least one positive eigenvalue. Indeed, under these assumptions, the
following inequality holds (see [Gur98, Theorem 1]): for any conformal class $[g]$ with $Y(M,[g])>0$ (positive Yamabe class), one has ${ }^{3}$
$$\mathcal{W}_{+}^{M}(g):=\int_{M}\left|W_{+}\right|^{2} d V_{g} \geq \frac{16 \pi^{2}}{3}(2 \chi(M)+3 \tau(M))$$
with equality if and only if $[g]$ contains a (positive) Kähler-Einstein metric. Recall also that the study of the self-dual Weyl energy $\mathcal{W}_{+}$is equivalent to that of Weyl's energy (1.2) because of the Hirzebruch signature formula
$$48 \pi^{2} \tau(M)=\int_{M}\left(\left|W_{+}\right|^{2}-\left|W_{-}\right|^{2}\right) d V_{g}$$
indeed, $\mathcal{W}^{M}(g)=-48 \pi^{2} \tau(M)+2 \mathcal{W}_{+}^{M}(g)$. A variant of Gursky's result was later obtained by LeBrun in [LeB15], where, for some particular manifolds, (1.9) was shown to hold for other families of conformal classes which may also be of negative Yamabe type. See also [LeB23], where it is proved that the infimum of Weyl functional is small (in the sense that (1.9) fails) on many closed 4-manifolds which also possess metrics of positive Yamabe class; this means that Gursky's inequality does not provide a lower bound for the infimum of Weyl energy in these cases. Examples of such manifolds are $m\left(\mathbb{S}^{2} \times \mathbb{S}^{2}\right)$ (i.e. connected sums of $m$ copies of $\mathbb{S}^{2} \times \mathbb{S}^{2}$ ) for $m$ large enough, or $\left(m \mathbb{C P}^{2}\right) \#\left(n \overline{\mathbb{C P}}^{2}\right)$ for $m$ large and $n / m$ close to 1; here $\overline{\mathbb{C P}}^{2}$ denotes the complex projective plane endowed with the other orientation.

Remark 1.8. Since the product metric $g_{\mathbb{S}^{2} \times \mathbb{S}^{2}}$ on $\mathbb{S}^{2} \times \mathbb{S}^{2}$ is Kähler-Einstein, by Gursky's theorem one has
$$\int_{\mathbb{S}^{2} \times \mathbb{S}^{2}}\left|W_{+}\right|^{2} d V_{g_{\mathbb{S}^{2} \times \mathbb{S}^{2}}}=\frac{16 \pi^{2}}{3} 8=\frac{128}{3} \pi^{2}$$
so that, by repeated applications of Theorem 1.1, one would get that $\mathcal{W}_{+}\left(m\left(\mathbb{S}^{2} \times \mathbb{S}^{2}\right)\right)$ can be upper bounded by a number slightly below $\frac{128}{3} \pi^{2} m$ (this will be clear from the proof); on the other hand, LeBrun's Theorem A in [LeB23] implies the much stronger bound $\mathcal{W}_{+}\left(m\left(\mathbb{S}^{2} \times \mathbb{S}^{2}\right)\right)<\frac{64 \pi^{2}}{3}(1+m)$ for $m$ large enough.

Finally, we mention the paper [Tau92] by Taubes, where it is proved that, given any closed oriented 4-manifold $M$, then $M \# m \overline{\mathbb{C P}}^{2}$ carries an ASD metric for $m$ large enough. In order to show this, the first step consists in decreasing the ASD Weyl energy of a fixed metric $g$ on $M$ by connect summing $a$ lot of copies of $\overline{\mathbb{C P}}^{2}$. While it is possible to obtain a decrease of ASD Weyl energy by arguing as in the proof of Theorem $1.1^{4}$, it is less clear whether one could actually obtain a quantitative relative decrease as in Taubes's paper, where the gluing procedure is actually performed in a different way (with no use of biharmonic interpolations).

\section*{Obstructions to loss of topology and orbifold singularities along minimizing sequences}

In the same spirit of [BK03], we would like to employ the strategy of Theorem 1.1 to study the formation of orbifold singularities along minimizing sequences for the Weyl energy (or for sequences of energy-minimizing Bach-flat metrics). For what follows, we refer the reader to [TV05b] or [And05; And06] for all the definitions and precise statements of the orbifold precompactness results for critical metrics.

\footnotetext{
${ }^{3}$ Notice that we have a factor 4 of difference with the formula in [Gur98] because here we are considering the norm of $W_{+}$seen as a (0, 4)-tensor instead that as an operator $\widehat{W}_{+}$on 2-forms.
${ }^{4}$ By the signature formula (1.10) and under the assumptions of Theorem 1.1, the $L^{2}$ norms of $W_{+}$and $W_{-}$are both decreased in the gluing region.
}

Assume for instance to have the simplest possible degeneration, that is, a sequence of unit-volume Bach-flat energy minimizing metrics $\left(g_{i}\right)_{i}$ on a manifold $Y$ which is Gromov-Hausdorff converging to a Bach-flat manifold $\left(Z, g_{Z}\right)$ while developing a single bubble in the limit at some point $p \in Z$; here the bubble is a Bach-flat asymptotically flat manifold $\left(N, g_{N}\right)^{5}$ and $Y$ is diffeomorphic to $Z \# N$. By the results of [Str10] (see also [AV12]) and the rigidity statement of positive mass theorem, we know that $\left(N, g_{N}\right)$ is AF of order 2; moreover, the metric $g_{Z}$ extends smoothly at the (a priori) singular point $p$. Also, it holds
$$\mathcal{W}(Y)=\inf _{g} \mathcal{W}^{Y}(g)=\mathcal{W}^{Z}\left(g_{Z}\right)+\mathcal{W}^{N}\left(g_{N}\right),$$
cf. Theorems 4.10 and 4.11 in [And06]. In this setting, if we are able to glue back together $Z$ and $N$ in a way that saves energy, then we get an immediate contradiction, as the resulting metric on $Y$ would have Weyl energy strictly below $\mathcal{W}(Y)$. Hence the sequence $\left(g_{i}\right)_{i}$ cannot lose topology at $p$ in the first place.

In other words, we would like to apply Theorem 1.1 in order to obtain an obstruction to the loss of topology, but here the manifold $\left(N, g_{N}\right)$ is not closed. However, we can deal with this issue by arguing exactly as in [Str10, p. 1319]: indeed, the fact that $g_{N}$ is AF of order 2 allow us to conformally compactify $\left(N, g_{N}\right)$ into a closed smooth manifold $\left(M, g_{M}\right)$ satisfying $\mathcal{W}^{M}\left(g_{M}\right)=\mathcal{W}^{N}\left(g_{N}\right)$. At this point, we can apply Theorem 1.1 and obtain an obstruction on $\left(N, g_{N}\right)$ and $\left(Z, g_{Z}\right)$.

More generally, this procedure of conformal compactification can also be performed in the ALE case, but this time we are not free to move the basepoint of the gluing. Indeed, the compactification only allow us to choose inverted conformal normal coordinates, for which we have a good expansion of the metric. As a consequence, we only get an obstruction on the product of Weyl tensors at the orbifold points. This creates difficulties as the Weyl tensor (and some of its covariant derivatives) may in principle vanish at (a local lifting of) such points, leading to higher order obstructions. We plan to tackle these problems in future works.

Remark 1.9. In the Einstein orbifold case (where no conformal normal coordinates are available), a good gauge for expanding the ALE metric at infinity has been obtained by Biquard and Hein in [BH23]. Subsequently, it has been employed by Ozuch in [Ozu24] in order to show that not all Einstein 4-orbifolds can be obtained as Gromov-Hausdorff limits of smooth Einstein 4-manifolds; see also the previous works [Biq13], [Ozu22a], [Ozu22b]. However, the ALE singularity models in this case are Ricci-flat and they are known to be of order 4 by the work of Cheeger and Tian, [CT94, Theorem 5.103] (see also [KS24]). In particular, the obstructions obtained in [Ozu24] represent the lack of integrability of certain infinitesimal Einstein deformations ${ }^{6}$ along the ALE end; moreover, as said in [Ozu24, Remark 1.5], these obstructions can be rewritten as an expression involving an interaction term like (1.7) plus another quantity called renormalized volume (introduced, in this particular setting, by [BH23]). Since Einstein metrics are also absolute minimizers of the $L^{2}$-norm of the Riemann curvature tensor,
$$g \mapsto \int_{M}\left|\operatorname{Riem}_{g}\right|^{2} d V_{g},$$
(this follows from the Chern-Gauss-Bonnet formula), it is tempting to ask whether it is possible to recover the same obstructions by Ozuch via a suitable gluing procedure as for the case of Weyl energy.

We end this Introduction with a brief description of the contents of each Section. In Section 2 we fix the notation and recall some known facts and preliminary results; in particular, we derive a formula for the expansion of the Weyl functional in TT directions at the Euclidean metric. In Section

\footnotetext{
${ }^{5}$ We remark that this kind of behavior is ruled out in the Einstein case, where orbifold singularities are the only possible degeneration due to Bishop-Gromov's inequality.
${ }^{6}$ They are the sum of the first error terms in the expansion of the ALE metric at infinity and the orbifold metric near the singularity, all in suitable gauges.
}

3, we precisely describe how to perform the connected sum and we further derive the equations for the interpolating metric in the gluing annulus. After that, in Section 4 we explicitly solve the biharmonic interpolation system and in Section 5 we use this information to compute the energy balance between the starting metrics and the one on the connected sum. Finally, in Section 6 we study the sign of (1.7) and prove Theorem 1.1.

\section*{Acknowledgments}

The authors are supported by the PRIN Project 2022AKNSE4 Variational and Analytical aspects of Geometric PDE and are members of GNAMPA, as part of INdAM. A.M. is also supported by the project Geometric problems with loss of compactness from Scuola Normale Superiore. The authors are grateful to Matthew Gursky for some inspiring discussions and many helpful remarks.

\section*{2 Preliminaries}

We begin by fixing the notation and recalling some preliminary results.
Notation: throughout this paper, we will adopt the Einstein summation convention, but only for repeated indices appearing once as a subscript and once as a superscript. Thus, for instance, $\sum_{i} a_{i} b^{i}=a_{i} b^{i}$, but $\sum_{i} a_{i} b_{i} \neq a_{i} b_{i}$. This is important as, in many computations, we will have indices appearing as subscripts and superscripts together with other indices only appearing as subscripts or superscripts, so we forewarn the reader about this. Related to this, we will usually denote local coordinates of a vector $x \in \mathbb{R}^{n}$ as $x^{i}$, but sometimes we will use the notation $x_{i}$ to make clear the fact that we are not implicitly summing on the components.

The $(1,3)$ and $(0,4)$ versions of the curvature tensor are defined by
$$\begin{gathered}
R(X, Y) Z:=\nabla_{X} \nabla_{Y} Z-\nabla_{Y} \nabla_{X} Z-\nabla_{[X, Y]} Z, \\
R(X, Y, Z, W):=g(R(X, Y) Z, W) .
\end{gathered}$$
In local coordinates, the Riemann tensor will be written as $R_{i j k l}:=R\left(\partial_{i}, \partial_{j}, \partial_{k}, \partial_{l}\right)$ and the Ricci tensor as $R_{i j}$, while the scalar curvature of a metric $g$ will be denoted by $R_{g}$. Thus
$$R_{i j k l}=R_{i j k}{ }^{\alpha} g_{\alpha l}, \quad R_{i j}=R_{k i j l} g^{k l}=R_{i k l j} g^{k l}=R_{k i j}{ }^{k}, \quad R_{g}=R_{i j} g^{i j},$$
that is, the Ricci curvature is obtained by contracting the second and third components of the (0, 4)-tensor (or, equivalently, the first and fourth ones).

As mentioned in the Introduction, on a 4-manifold, the (0, 4)-curvature tensor admits the $L^{2}$ -orthogonal decomposition (1.1), see e.g. [Bes08]. In particular, © is the Kulkarni-Nomizu product, which takes two symmetric $(0,2)$ tensors as input and gives back a $(0,4)$ tensor with the same symmetries of the curvature tensor; it is defined by
$$(a \oplus b)(X, Y, V, W)=\frac{1}{2}[a(X, W) b(Y, V)+a(Y, V) b(X, W)-a(X, V) b(Y, W)-a(Y, W) b(X, V)] .$$
Notice that the $\frac{1}{2}$-factor in the definition is not a canonical choice.
The decomposition (1.1) implies that the Weyl tensor has all traces equal to zero.
The curvature tensor can be regarded as a symmetric endomorphisms on 2-forms called curvature operator:
$$\widehat{R}: \Lambda^{2}\left(T^{*} M\right) \rightarrow \Lambda^{2}\left(T^{*} M\right),$$
cf. [Via16, Lecture 5] or [Bes08]. Indeed, given a local frame $\left\{e_{1}, \ldots, e_{n}\right\}$ with local coframe $\left\{e^{1}, \ldots, e^{n}\right\}$, then the family $\left\{e^{i} \wedge e^{j}\right\}_{i<j}$ defines a local frame for $\Lambda^{2}\left(T^{*} M\right)$ and we can define
$$\widehat{R}\left(e^{i} \wedge e^{j}\right):=\frac{1}{2} R_{i j l k} e^{k} \wedge e^{l}=\sum_{i<j} R_{i j l k} e^{k} \wedge e^{l}$$
Notice the position reversal between $k$ and $l$. With this definition, $\widehat{R}$ coincides with the curvature operator on 2-forms defined e.g. in [Via16]: here there is no position reversal but the (0, 4)-curvature tensor has the opposite sign with respect to our convention.

In the same way, we can also regard the Weyl tensor $W$ as a symmetric trace-free endomorphism $\widehat{W}$ on $\Lambda^{2}\left(T^{*} M\right)$. In particular, if $n=4$ and $M$ is oriented, then the Hodge star operator acting on 2-forms, $*: \Lambda^{2}\left(T^{*} M\right) \rightarrow \Lambda^{2}\left(T^{*} M\right)$, satisfies $*^{2}=\mathrm{Id}$ and, under its action, $\Lambda^{2}$ decomposes into
$$\Lambda^{2}\left(T^{*} M\right)=\Lambda_{+}^{2}\left(T^{*} M\right) \oplus \Lambda_{-}^{2}\left(T^{*} M\right),$$
which are the ±1-eigenspaces of $*$ respectively and satisfy $\operatorname{dim}\left(\Lambda_{ \pm}^{2}\left(T^{*} M\right)\right)=3$. The Weyl curvature operator decomposes accordingly as follows:
$$\widehat{W}=\widehat{W}_{+}+\widehat{W}_{-}, \quad \widehat{W}_{ \pm}: \Lambda_{ \pm}^{2}\left(T^{*} M\right) \rightarrow \Lambda_{ \pm}^{2}\left(T^{*} M\right) .$$
$\widehat{W}_{+}, \widehat{W}_{-}$are called self-dual and anti self-dual Weyl curvatures respectively (as well as $W_{+}, W_{-}$ which are the associated (0, 4)-tensors).

Finally, notice that the norm of a $(0,4)$ curvature-type tensor $|T|^{2}=T^{i j k l} T_{i j k l}$ differs by a factor of 4 from the norm $\|\widehat{T}\|^{2}$ of $T$ seen as a symmetric endomorphism of $\Lambda^{2}\left(T^{*} M\right)$ :
$$|T|^{2}=4\|\widehat{T}\|^{2} .$$

\subsection*{2.1 Linearization of curvature tensors}

Here we recall the formulae for some linearized geometric quantities. The only one we really need is that of Weyl tensor, which however is obtained as a byproduct of the previous ones. These formulae are well-known in literature and we only recall them for the sake of completeness. Some references are, e.g., [Bes08] or [CM20], but beware of the fact that they both employ a different convention for the curvature in local coordinates.

Throughout this subsection, we will assume that $\left(g_{t}\right)_{t}$ is a smooth family of Riemannian metrics on a manifold $M$ with $g_{0}=g$ and we let $h=\left.\frac{d}{d t}\right|_{t=0} g_{t}$ denote the linearization of $g_{t}$ at $t=0$; by construction, $h$ is a symmetric (0, 2)-tensor. We then have the following formulae:
\begin{itemize}
\item[-] Inverse of metric tensor:
$$\left.\frac{d}{d t}\right|_{t=0} g_{t}^{i j}=-h^{i j}=-g^{\alpha i} g^{\beta j} h_{\alpha \beta} .$$
\item[-] Christoffel symbols:
$$\left.\frac{d}{d t}\right|_{t=0}{ }^{g_{t}} \Gamma_{i j}^{k}=\frac{1}{2} g^{k l}\left(\nabla_{i} h_{l j}+\nabla_{j} h_{i l}-\nabla_{l} h_{i j}\right) .$$
\item[-] (1, 3)-curvature tensor:
$$\left.\frac{d}{d t}\right|_{t=0}{ }_{g t} R_{i j k}{ }^{l}=\frac{1}{2} g^{s l}\left[\nabla_{i k}^{2} h_{j s}+\nabla_{j s}^{2} h_{i k}-\nabla_{i s}^{2} h_{j k}-\nabla_{j k}^{2} h_{i s}-R_{i j s}{ }^{r} h_{r k}-R_{i j k}{ }^{r} h_{s r}\right],$$
\end{itemize}
where $\nabla_{i j}^{2} h_{k l}=\left(\nabla^{2} h\right)_{i j k l}$. In order to prove this formula, we write down $R_{i j k}{ }^{l}$ in terms of Christoffel symbols and then we use (2.3) and the commutation formula
$$\nabla_{i j}^{2} T_{k l}-\nabla_{j i}^{2} T_{k l}=-R_{i j k}{ }^{s} T_{s l}-R_{i j l}{ }^{s} T_{k s} .$$
\begin{itemize}
\item[-] (0, 4)-curvature tensor:
$$\left.\frac{d}{d t}\right|_{t=0}{ }^{g_{t}} R_{i j k l}=\frac{1}{2}\left[\nabla_{i k}^{2} h_{j l}+\nabla_{j l}^{2} h_{i k}-\nabla_{i l}^{2} h_{j k}-\nabla_{j k}^{2} h_{i l}+R_{i j k}{ }^{s} h_{l s}-R_{i j l}{ }^{s} h_{s k}\right] .$$
To prove this, write $R_{i j k l}=R_{i j k}{ }^{s} g_{s l}$, linearize and use (2.4). Recall in particular that $\frac{d}{d t}$ does not commute with index raising or lowering.
\item[-] (0, 2)-Ricci tensor:
$$\left.\frac{d}{d t}\right|_{t=0}{ }^{g_{t}} R_{i j}=\frac{1}{2}\left[-\Delta h_{i j}-\nabla_{i j}^{2}(\operatorname{tr} h)+\nabla_{i}(\delta h)_{j}+\nabla_{j}(\delta h)_{i}+R_{i}{ }^{s} h_{s j}+R_{j}{ }^{s} h_{i s}-2 R_{i j}^{r}{ }^{s} h_{r s}\right] .$$
Here $\delta$ stands for the divergence operator, which we define as $(\delta h)_{i}:=\nabla^{k} h_{i k}$; moreover, we are using the shorthands $R_{i}{ }^{s} h_{s j}=g^{s t} R_{i s} h_{t j}$ and $R^{r}{ }_{i j}{ }^{s} h_{r s}=g^{r t} R_{r i j}{ }^{s} h_{t s}$. To get (2.6), utilize (2.4) and the definition of $R_{i j}$; in particular, notice that $\frac{d}{d t}$ does not commute with the trace operator.
\item[-] Scalar curvature:
$$\left.\frac{d}{d t}\right|_{t=0} R_{g_{t}}=-\Delta(\operatorname{tr} h)+\delta^{2}(h)-h^{i j} R_{i j} .$$
\end{itemize}
- Weyl tensor:
$$\begin{aligned}
\left.\frac{d}{d t}\right|_{t=0}{ }^{g_{t}} W_{i j k l} & =\frac{1}{2}\left[\nabla_{i k}^{2} h_{j l}+\nabla_{j l}^{2} h_{i k}-\nabla_{i l}^{2} h_{j k}-\nabla_{j k}^{2} h_{i l}\right] \\
& +\frac{1}{2(n-2)}\left\{\left[-\Delta h_{i k}-\nabla_{i k}^{2}(\operatorname{tr} h)+\nabla_{i}(\delta h)_{k}+\nabla_{k}(\delta h)_{i}\right] g_{j l}\right. \\
& +\left[-\Delta h_{j l}-\nabla_{j l}^{2}(\operatorname{tr} h)+\nabla_{j}(\delta h)_{l}+\nabla_{l}(\delta h)_{j}\right] g_{i k} \\
& -\left[-\Delta h_{i l}-\nabla_{i l}^{2}(\operatorname{tr} h)+\nabla_{i}(\delta h)_{l}+\nabla_{l}(\delta h)_{i}\right] g_{j k} \\
& \left.-\left[-\Delta h_{j k}-\nabla_{j k}^{2}(\operatorname{tr} h)+\nabla_{j}(\delta h)_{k}+\nabla_{k}(\delta h)_{j}\right] g_{i l}\right\} \\
& +\frac{1}{(n-1)(n-2)}\left(-\Delta(\operatorname{tr} h)+\delta^{2} h\right)\left(g_{j k} g_{i l}-g_{i k} g_{j l}\right) \\
& +\frac{1}{2}\left[R_{i j k}{ }^{s} h_{l s}-R_{i j l}{ }^{s} h_{s k}\right]+\frac{1}{n-2}\left(R_{i k} h_{j l}+R_{j l} h_{i k}-R_{i l} h_{j k}-R_{j k} h_{i l}\right) \\
& +\frac{1}{2(n-2)}\left\{\left[R_{i}^{r} h_{r k}+R_{k}^{r} h_{i r}-2 R_{i k}^{r} h_{r s}\right] g_{j l}+\left[R_{j}^{r} h_{r l}+R_{l}^{r} h_{j r}-2 R_{j l}^{r}{ }_{l r} h_{r s}\right] g_{i k}\right. \\
& \left.-\left[R_{i}^{r} h_{r l}+R_{l}^{r} h_{i r}-2 R_{i l}^{r} h_{r s}\right] g_{j k}-\left[R_{j}^{r} h_{r k}+R_{k}^{r} h_{j r}-2 R_{j k}^{r}{ }^{s} h_{r s}\right] g_{i l}\right\} \\
& -\frac{h^{i j} R_{i j}}{(n-1)(n-2)}\left(g_{j k} g_{i l}-g_{i k} g_{j l}\right)+\frac{R_{g}}{(n-1)(n-2)}\left(h_{j k} g_{i l}+g_{j k} h_{i l}-h_{i k} g_{j l}-g_{i k} h_{j l}\right) .
\end{aligned}$$
In order to obtain this formula, we write down the Weyl tensor in local coordinates using (1.1),
$$W_{i j k l}=R_{i j k l}-\frac{1}{n-2}\left(R_{j k} g_{i l}+R_{i l} g_{j k}-R_{i k} g_{j l}-R_{j l} g_{i k}\right)-\frac{R_{g}}{(n-1)(n-2)}\left(g_{j k} g_{i l}-g_{i k} g_{j l}\right),$$
and then we linearize, apply (2.5), (2.6) and (2.7) and regroup the terms as above.
Remark 2.1. Notice that formula (2.8) simplifies consistently when $h$ is TT (i.e. $\delta h=0$ and $\operatorname{tr} h=0$ ) or when the metric $g_{0}$ is flat. This will actually be the case in our later application.

\subsection*{2.2 Expansion of Weyl functional in TT directions at the Euclidean metric}

Let $\Omega \subset \mathbb{R}^{4}$ be an open, bounded, regular domain and consider $\left(g_{t}\right)_{t}$, a smooth family of metrics on $\Omega$, such that $g_{0}=g_{E}$ (Euclidean metric); let $h:=\left.\frac{d}{d t}\right|_{t=0} g_{t}$ be the linearization of $g_{t}$ at $t=0$. Assume moreover that $h$ is a transverse-traceless (TT) tensor. Taylor-expanding $\mathcal{W}\left(g_{t}\right)=\int_{\Omega}\left|W_{g_{t}}\right|^{2} d V_{g_{t}}$ at $t=0$ we get
$$\mathcal{W}\left(g_{t}\right)=\mathcal{W}\left(g_{E}\right)+\left.t \frac{d}{d t}\right|_{t=0} \mathcal{W}\left(g_{t}\right)+\left.\frac{t^{2}}{2} \frac{d^{2}}{d t^{2}}\right|_{t=0} \mathcal{W}\left(g_{t}\right)+O\left(t^{3}\right) .$$
But now $\mathcal{W}\left(g_{E}\right)=0$ and (see e.g. the proof of Proposition 3.1 in [Kob85])
$$\left.\frac{d}{d t}\right|_{t=0} \mathcal{W}\left(g_{t}\right)=d \mathcal{W}\left(g_{e}\right)[h]=-4 \int_{\Omega}\left(W_{\alpha i j \beta} \nabla^{\alpha} \nabla^{\beta} h^{i j}+\frac{1}{2} W_{\alpha i j \beta} R^{\alpha \beta} h^{i j}\right) d x=0,$$
where the last equality is due to the fact that $W=W_{g_{E}} \equiv 0$.
Remark 2.2. On a closed manifold $M$, assuming that $g_{0}$ is a critical point of $\mathcal{W}$, we can integrate (2.11) by parts and use the symmetry of $R^{\alpha \beta}$ to obtain
$$-4 \int_{M}\left(\nabla^{\alpha} \nabla^{\beta} W_{\alpha i j \beta}+\frac{1}{2} R^{\alpha \beta} W_{\alpha i j \beta}\right) h^{i j} d V_{g_{0}}=0 .$$
In particular, we see that the Bach tensor (1.3) is the Euler-Lagrange operator for $\mathcal{W}$. Since in our case we are dealing with a domain $\Omega$ with boundary, we stopped before integrating by parts.

In order to compute the second variation, we start from the first variation at a generic time $t$,
$$\frac{d}{d t} \mathcal{W}\left(g_{t}\right)=-4 \int_{\Omega}\left(W_{\alpha i j \beta} \nabla^{\alpha} \nabla^{\beta}\left(\partial_{t} g\right)^{i j}+\frac{1}{2} W_{\alpha i j \beta} R^{\alpha \beta}\left(\partial_{t} g\right)^{i j}\right) d V_{g_{t}},$$
from which we get
$$\left.\frac{d^{2}}{d t^{2}}\right|_{t=0} \mathcal{W}\left(g_{t}\right)=-4 \int_{\Omega} \dot{W}_{\alpha i j \beta} \partial^{\alpha} \partial^{\beta} h^{i j} d x$$
where $\dot{W}:=\left.\frac{d}{d t}\right|_{t=0} W_{g_{t}}$ denotes the linearized Weyl tensor at $t=0$. Notice that here the flatness of the Euclidean metric was crucial in order to get rid of the other terms. Using the formula (2.8) for $\dot{W}$ with $g=g_{E}$ and the fact that $h$ is TT, we now have
$$\dot{W}_{\alpha i j \beta}=\frac{1}{2}\left[\partial_{\alpha j}^{2} h_{i \beta}+\partial_{i \beta}^{2} h_{\alpha j}-\partial_{\alpha \beta}^{2} h_{i j}-\partial_{i j}^{2} h_{\alpha \beta}\right]+\frac{1}{4}\left[\delta_{\alpha \beta} \Delta h_{i j}+\delta_{i j} \Delta h_{\alpha \beta}-\delta_{i \beta} \Delta h_{\alpha j}-\delta_{\alpha j} \Delta h_{i \beta}\right],$$
thus, putting together (2.10), (2.11), (2.12) and (2.13), we obtain
$$\begin{aligned}
\mathcal{W}\left(g_{t}\right) & =t^{2} \int_{\Omega}\left(\partial_{\alpha \beta}^{2} h_{i j}+\partial_{i j}^{2} h_{\alpha \beta}-\partial_{\alpha j}^{2} h_{i \beta}-\partial_{i \beta}^{2} h_{\alpha j}\right) \partial^{\alpha} \partial^{\beta} h^{i j} d x \\
& +\frac{t^{2}}{2} \int_{\Omega}\left(\delta_{i \beta} \Delta h_{\alpha j}+\delta_{\alpha j} \Delta h_{i \beta}-\delta_{\alpha \beta} \Delta h_{i j}-\delta_{i j} \Delta h_{\alpha \beta}\right) \partial^{\alpha} \partial^{\beta} h^{i j} d x+O\left(t^{3}\right)
\end{aligned}$$
Being $h$ a TT tensor, we easily see that
$$\int_{\Omega}\left(\delta_{i \beta} \Delta h_{\alpha j}+\delta_{\alpha j} \Delta h_{i \beta}-\delta_{\alpha \beta} \Delta h_{i j}-\delta_{i j} \Delta h_{\alpha \beta}\right) \partial^{\alpha} \partial^{\beta} h^{i j} d x=-\int_{\Omega} \sum_{i, j}\left(\Delta h_{i j}\right)^{2} d x$$
For the other term of (2.14), after relabeling indices there holds
$$\begin{aligned}
\int_{\Omega}\left(\partial_{\alpha \beta}^{2} h_{i j}+\partial_{i j}^{2} h_{\alpha \beta}-\right. & \left.\partial_{\alpha j}^{2} h_{i \beta}-\partial_{i \beta}^{2} h_{\alpha j}\right) \partial^{\alpha} \partial^{\beta} h^{i j} d x \\
& =\int_{\Omega} \sum_{i, j}\left|\nabla^{2} h_{i j}\right|^{2} d x+\int_{\Omega}\left(\partial_{i j}^{2} h_{\alpha \beta}-2 \partial_{\alpha j}^{2} h_{i \beta}\right) \partial^{\alpha} \partial^{\beta} h^{i j} d x
\end{aligned}$$

Moreover, using Bochner's identity on $h_{i j}$ and integrating by parts we get
$$\int_{\Omega}\left|\nabla^{2} h_{i j}\right|^{2} d x=\int_{\Omega}\left(\Delta h_{i j}\right)^{2} d x+\sum_{\beta} \int_{\partial \Omega} \partial_{\alpha \beta}^{2} h_{i j} \partial_{\beta} h_{i j} \nu^{\alpha} d \sigma-\int_{\partial \Omega} \Delta h_{i j} \partial_{\alpha} h_{i j} \nu^{\alpha} d \sigma,$$
(here $\nu=\left(\nu^{1}, \ldots, \nu^{4}\right)$ is the exterior unit normal), while an integration by parts and the fact that $h$ is divergence free also gives
$$\int_{\Omega}\left(\partial_{i j}^{2} h_{\alpha \beta}-2 \partial_{\alpha j}^{2} h_{i \beta}\right) \partial^{\alpha} \partial^{\beta} h^{i j} d x=\int_{\partial \Omega}\left(\partial_{i j}^{2} h_{\alpha \beta}-2 \partial_{\beta j}^{2} h_{i \alpha}\right) \partial^{\beta} h^{i j} \nu^{\alpha} d \sigma$$
Substituting (2.15), (2.16), (2.17) and (2.18) inside (2.14) we obtain the following expansion for the Weyl energy:
$$\begin{aligned}
\mathcal{W}\left(g_{t}\right) & =\frac{t^{2}}{2} \sum_{i, j} \int_{\Omega}\left(\Delta h_{i j}\right)^{2} d x \\
& +t^{2} \sum_{i, j, \beta} \int_{\partial \Omega}\left[\left(\partial_{i j}^{2} h_{\alpha \beta}-2 \partial_{\beta j}^{2} h_{i \alpha}+\partial_{\alpha \beta}^{2} h_{i j}\right) \partial_{\beta} h_{i j}-\partial_{\beta \beta}^{2} h_{i j} \partial_{\alpha} h_{i j}\right] \nu^{\alpha} d \sigma+O\left(t^{3}\right)
\end{aligned}$$
Finally, integrating by parts twice the biharmonic energy we get
$$\int_{\Omega}\left(\Delta h_{i j}\right)^{2} d x=\int_{\Omega}\left(\Delta^{2} h_{i j}\right) h_{i j} d x-\int_{\partial \Omega} h_{i j} \partial_{\alpha}\left(\Delta h_{i j}\right) \nu^{\alpha} d \sigma+\int_{\partial \Omega} \Delta h_{i j} \partial_{\alpha} h_{i j} \nu^{\alpha} d \sigma$$
so that (2.19) rewrites as follows:
$$\begin{aligned}
\mathcal{W}\left(g_{t}\right) & =\frac{t^{2}}{2} \sum_{i, j} \int_{\Omega}\left(\Delta^{2} h_{i j}\right) h_{i j} d x-\frac{t^{2}}{2} \sum_{i, j, \beta} \int_{\partial \Omega} h_{i j} \partial_{\alpha \beta \beta}^{3} h_{i j} \nu^{\alpha} d \sigma \\
& +t^{2} \sum_{i, j, \beta} \int_{\partial \Omega}\left[\left(\partial_{i j}^{2} h_{\alpha \beta}-2 \partial_{\beta j}^{2} h_{i \alpha}+\partial_{\alpha \beta}^{2} h_{i j}\right) \partial_{\beta} h_{i j}-\frac{1}{2} \partial_{\beta \beta}^{2} h_{i j} \partial_{\alpha} h_{i j}\right] \nu^{\alpha} d \sigma+O\left(t^{3}\right)
\end{aligned}$$

\section*{3 The connected sum setup}

In this section we are going to describe how to define a suitable competitor metric on the connected sum of two closed 4-manifolds.

Remark 3.1. We notify the reader beforehand that, given two manifolds $M$ and $Z$, we will actually perform the connected sum in such a way that the resulting manifold $X$ will be diffeomorphic to $Z \# \bar{M}$, where $\bar{M}$ denotes the manifold $M$ endowed with its opposite orientation, see (3.8) and Remark 3.5. As a consequence, the biharmonic interpolation and energy balance will be performed in this setting. This is not exactly what we want as we aim to decrease the Weyl functional on $Z \# M$; however, since $\mathcal{W}^{M}=\mathcal{W}^{\bar{M}}$, in the end it will be sufficient to perform the same procedure with $\bar{M}$ in place of $M$ in order to prove Theorem 1.1.

To begin we recall that, given a closed manifold $(M, g)$ and a point $p \in M$, we got the following expansion of the metric $g$ in geodesic normal coordinates $\left\{z^{i}\right\}$ centered at $p$ :
$$g_{i j}(z)=\delta_{i j}-\frac{1}{3} R_{k i j l}(p) z^{k} z^{l}+O^{(3)}\left(|z|^{3}\right), \quad \text { as }|z| \rightarrow 0 .$$

Remark 3.2. Throughout this paper, we will use the symbol $O^{(\alpha)}\left(|z|^{\beta}\right)$ to denote a function $f$ (or tensor sometimes) which satisfies $\left|\nabla^{k} f\right|=O\left(|z|^{\beta-k}\right)$ as $z$ approaches 0 or infinity (depending on the situation) and for $k=0,1, \ldots, \alpha$.

For our purposes, it will be convenient to consider a refined expansion of the metric given by conformal normal coordinates; indeed, by the results in [LP87] (see the proof of their Theorem 5.1), there exists a conformal metric $\tilde{g} \in[g]$ such that, in geodesic normal coordinates for $\tilde{g}$ around $p$, one has
$$\tilde{g}_{i j}(z)=\delta_{i j}-\frac{1}{3} W_{k i j l}^{\tilde{g}}(p) z^{k} z^{l}+O^{(3)}\left(|z|^{3}\right), \quad \text { as }|z| \rightarrow 0 .$$
Now, being the Weyl functional conformally invariant, we get $\mathcal{W}(g)=\mathcal{W}([g])$, which means that, in our procedure, we are free to start with any metric in the conformal class of $g$. As a consequence, without loss of generality, we can assume that the metric expansions in normal coordinates for our manifolds are always of the type (3.1).

Remark 3.3. Looking at the proof of Theorem 5.1 in [LP87], we actually see that the conformal factor $f$ for the metric $\tilde{g}=e^{f} g$ satisfies $f(p)=0$; as a consequence, we also have $W_{\text {kijl }}^{\tilde{g}}(p)=e^{f} W_{\text {kijl }}^{g}(p)=$ $W_{k i j l}^{g}(p)$ by the conformal covariance of Weyl's tensor.

As already pointed out in the Introduction, in order to perform a connected sum which allows to reduce Weyl's energy, we want the manifolds to be almost flat in the gluing regions. To this purpose, following the approach adopted in [BK03] for the Willmore functional, we are going to invert one of the manifolds at a point and then glue its end to an enlarged copy of the other manifold.

Let $\left(M, g_{M}\right)$ be a closed 4-manifold. Consider a function $F: M \backslash\{p\} \rightarrow \mathbb{R}$ which is smooth, positive and such that $F(z)=|z|^{-2}$ in (conformal) normal coordinates around $p$ for $|z|$ small enough. Let now
$$\left(N, g_{N}\right):=\left(M \backslash\{p\}, F^{2} g_{M}\right)$$
be the conformal blow-up of $\left(M, g_{M}\right)$ through $F$; then the pointwise identity $\left|W^{g_{N}}\right|^{2} d V_{g_{N}}=$ $\left|W^{g_{M}}\right|^{2} d V_{g_{M}}$ on $M \backslash\{p\}$ implies that $\mathcal{W}^{M}\left(g_{M}\right)=\mathcal{W}^{N}\left(g_{N}\right)$.

Remark 3.4. If ( $M, g$ ) has positive scalar curvature, then ([LP87, Theorem 2.8]) there exists a unique Green's function $G$ for the conformal Laplacian $L_{g}=-c_{n} \Delta_{g}+R_{g}$, and one could consider the conformal blow-up of $M$ through $G$ as in [GV16]. However, here we do not assume positive scalar curvature of $g_{M}$ and, moreover, the lower-order terms in the expansion of the Green function generate second order corrections to the inverted metric which we want to avoid.

Let now $\left\{\bar{y}^{i}:=z^{i} /|z|^{2}\right\}$ denote the inverted (conformal) normal coordinates at $p$ and let $I: \mathbb{R}^{4} \backslash\{0\} \rightarrow \mathbb{R}^{4} \backslash\{0\}$ denote the inversion map, $I(z):=\frac{z}{|z|^{2}}$. Then the following expansion holds for $g_{N}$ :
$$\left(g_{N}\right)_{i j}(\bar{y})=\delta_{i j}-\frac{1}{3} W_{k i j l}^{M}(p) \frac{\bar{y}^{k} \bar{y}^{l}}{|\bar{y}|^{4}}+O^{(3)}\left(|\bar{y}|^{-3}\right), \quad \text { as }|\bar{y}| \rightarrow \infty ;$$
see the Appendix for a proof.
Let now $\left(Z, g_{Z}\right)$ be another closed oriented 4-manifold and let $q \in Z$; as above, we can assume without loss of generality that $g_{Z}$ has the following expansion in normal coordinates $\left\{\bar{x}^{i}\right\}$ around $q$ :
$$\left(g_{Z}\right)_{i j}(\bar{x})=\delta_{i j}-\frac{1}{3} W_{k i j l}^{Z}(q) \bar{x}^{k} \bar{x}^{l}+O^{(3)}\left(|\bar{x}|^{3}\right), \quad \text { as }|\bar{x}| \rightarrow 0 .$$

We now want to enlarge $Z$ and shrink $N$ before performing the connected sum; to this purpose, consider two small parameters $0<a, b \ll 1$ (to be further specified later on) and the rescaled manifolds
$$\left(N, a^{2} g_{N}\right), \quad\left(Z, b^{-2} g_{Z}\right) .$$
If $a, b$ are small enough, we can assume that the normal coordinates $\left\{x^{i}:=b^{-1} \bar{x}^{i}\right\}$ of the scaled metric $b^{-2} g_{Z}$ at $q$ are defined in an open set containing the open ball $B_{2}(0) \subset \mathbb{R}^{4}$, and that the inverted
normal coordinates $\left\{y^{i}:=a \bar{y}^{i}\right\}$ for $a^{2} g_{N}$ at $p$ are defined in $\mathbb{R}^{4} \backslash B_{1}(0)$. Then the following expansions hold:
$$\left(g_{b}\right)_{i j}(x)=\delta_{i j}-\frac{1}{3} b^{2} W_{k i j l}^{Z}(q) x^{k} x^{l}+\eta_{i j}^{b}(x), \quad \text { for }|x| \leq 2,$$
where $\eta_{i j}^{b}$ satisfies
$$\left|\eta_{i j}^{b}(x)\right||x|^{-3}+\left|\nabla \eta_{i j}^{b}(x)\right||x|^{-2}+\left|\nabla^{2} \eta_{i j}^{b}(x)\right||x|^{-1} \leq C b^{3}, \quad \text { for }|x| \leq 2,$$
and
$$\left(g_{a}\right)_{i j}(y)=\delta_{i j}-\frac{1}{3} a^{-2} W_{k i j l}^{M}(p) \frac{y^{k} y^{l}}{|y|^{4}}+\tilde{\zeta}_{i j}^{a}(y), \quad \text { for }|y| \geq 1,$$
where $\tilde{\zeta}_{i j}^{a}$ satisfies
$$\left|\tilde{\zeta}_{i j}^{a}(y)\right||y|^{3}+\left|\nabla \tilde{\zeta}_{i j}^{a}(y)\right||y|^{4}+\left|\nabla^{2} \tilde{\zeta}_{i j}^{a}(y)\right||y|^{5} \leq C a^{-3}, \quad \text { for }|y| \geq 1 .$$

Let now $\gamma>0$ be another small parameter to be fixed later on and such that $0<a, b \ll \gamma<1$. The gluing between $M$ and $Z$ is performed as follows: we remove from $\left(Z, g_{b}\right)$ the ball $\{x||x|<a\}$ centered at $q$ and from ( $N, g_{a}$ ) the region $\left\{y\left||y|>2 a^{-2}\right\}\right.$; we then identify the annular region $\{a \leq|x| \leq 2\} \subset Z$ with the annular region $\left\{a^{-1} \leq|y| \leq 2 a^{-2}\right\} \subset N$ using the map $i$ defined below:
$$i:\left\{a^{-1} \leq|y| \leq 2 a^{-2}\right\} \rightarrow\{a \leq|x| \leq 2\}, \quad x=i(y)=a^{2} y .$$
We denote by $X$ the new manifold obtained via this procedure.
Remark 3.5. By construction, the manifold $X$ will be diffeomorphic to $Z \# \bar{M}$, where $\bar{M}$ denotes the (oriented) manifold $M$ endowed with its opposite orientation. In particular, this is the same choice adopted in [GV16], see their Remark 9.1. The advantage over orientation-preserving identifications of the annular regions is due to the fact that here we have no permutations or sign reversals between the coordinates $\left\{y^{i}\right\}$ on $N$ and $\left\{x^{i}\right\}$ on $Z$.

We also notice that, in the new coordinates $x=a^{2} y$, the expansion (3.6) of $g_{a}$ becomes
$$\left(g_{a}\right)_{i j}(x)=\delta_{i j}-\frac{1}{3} a^{2} W_{k i j l}^{M}(p) \frac{x^{k} x^{l}}{|x|^{4}}+\zeta_{i j}^{a}(x), \quad \text { for }|x| \geq a^{2},$$
where now the error term $\zeta_{i j}^{a}(x):=\tilde{\zeta}_{i j}^{a}\left(a^{-2} x\right)$ satisfies
$$\left|\zeta_{i j}^{a}(x)\right||x|^{3}+\left|\nabla \zeta_{i j}^{a}(x)\right||x|^{4}+\left|\nabla^{2} \zeta_{i j}^{a}(x)\right||x|^{5} \leq C a^{3} \quad \text { for }|x| \geq a^{2}$$

At this point, it only remains to define a suitable metric $g_{X}$ on $X$ which interpolates between $g_{a}$ and $g_{b}$ in the gluing region. To this purpose, for a given $a>0$, we can consider a smooth cutoff function $\chi_{a} \in C^{\infty}(\mathbb{R})$ such that:
$$\chi_{a}(t)=\left\{\begin{array}{ll}
0 & \text { for } t \leq \frac{\sqrt{a}}{4} \\
1 & \text { for } t \geq \frac{3}{4} \sqrt{a},
\end{array} \quad\left|\chi_{a}\right|+\sqrt{a}\left|\chi_{a}^{\prime}\right|+a\left|\chi_{a}^{\prime \prime}\right| \leq C,\right.$$
where $C>0$ does not depend upon $a$. We can now use $\chi_{a}$ to cut off the higher order terms in the expansions (3.9), (3.4) of $g_{a}$ and $g_{b}$ (with respect to the coordinates $\left\{x^{i}\right\}$ ) and define the following
new metric $g_{X}$ in the outermost part of the gluing region (which we are now identifying with the region $\{a \leq|x| \leq 2\} \subset Z$ ):
$$\left(g_{X}\right)_{i j}(x):= \begin{cases}\delta_{i j}-\frac{1}{3} a^{2} W_{k i j l}^{M}(p) \frac{x^{k} x^{l}}{|x|^{4}}+\zeta_{i j}^{a}(x) \chi_{a}(\gamma-|x|) & \text { for } a \leq|x|<\gamma, \\ \delta_{i j}-\frac{1}{3} b^{2} W_{k i j l}^{Z}(q) x^{k} x^{l}+\eta_{i j}^{b}(x) \chi_{a}(|x|-1) & \text { for } 1 \leq|x| \leq 2 .\end{cases}$$
Notice that actually $g_{X}=g_{a}$ for $|x| \leq \gamma-\sqrt{a}$ and $g_{X}=g_{b}$ for $|x| \geq 1+\sqrt{a}$.
At this point, we look for a suitable interpolating metric in the annular region $\{\gamma<|x|<1\}$ : we define it to be the biharmonic interpolation between the two metrics with $C^{1}$ matching at the boundary. In other words, we define it as $\left(g_{X}\right)_{i j}:=w_{i j}$, where (using the shorthands $W_{\text {kijl }}^{M}, W_{\text {kijl }}^{Z}$ for $\left.W_{k i j l}^{M}(p), W_{k i j l}^{Z}(q)\right) w_{i j}$ is the unique solution to
$$\begin{cases}\Delta^{2} w_{i j}=0 & \text { in } \gamma<|x|<1 \\ w_{i j}=\delta_{i j}-\frac{1}{3} a^{2} W_{k i j l}^{M} \frac{x^{k} x^{l}}{|x|^{4}} & \text { in }|x|=\gamma \\ w_{i j}=\delta_{i j}-\frac{1}{3} b^{2} W_{k i j l}^{Z} x^{k} x^{l} & \text { in }|x|=1 \\ \partial_{r} w_{i j}=\frac{2}{3} a^{2} W_{k i j l}^{M} \frac{x^{k} x^{l}}{|x|^{5}} & \text { in }|x|=\gamma \\ \partial_{r} w_{i j}=-\frac{2}{3} b^{2} W_{k i j l}^{Z} \frac{x^{k} x^{l}}{|x|} & \text { in }|x|=1 .\end{cases}$$
Here $r=|x|$ and we notice that
$$\partial_{r}\left(W_{k i j l}^{M} \frac{x^{k} x^{l}}{|x|^{4}}\right)=-2 W_{k i j l}^{M} \frac{x^{k} x^{l}}{|x|^{5}}, \quad \partial_{r}\left(W_{k i j l}^{Z} x^{k} x^{l}\right)=2 W_{k i j l}^{Z} \frac{x^{k} x^{l}}{|x|} .$$
In particular, we are requiring $w_{i j}$ to coincide at the boundary with the metric $\left(g_{X}\right)_{i j}$ (defined in (3.12)) up to the first order. The crucial thing is that we are actually able to explicitly compute the solution $w=\left(w_{i j}\right)_{i, j}$ of (3.13), and this will allow us to compute the Weyl energy balance; we will solve (3.13) in Section 4.

We can now complete the definition of the metric $g_{X}$ on $X$ by setting
$$g_{X}:= \begin{cases}g_{b} & \text { in } Z \backslash\{x| | x \mid<2\} \\ g_{a} & \text { in } N \backslash\left\{y| | y \mid>a^{-1}\right\}=N \backslash\{x| | x \mid>a\} \\ w & \text { in }\{\gamma<|x|<1\} \\ \text { as in (3.12) } & \text { in the remaining region. }\end{cases}$$
We will compare $\mathcal{W}^{X}\left(g_{X}\right)$ to $\mathcal{W}^{N}\left(g_{a}\right)+\mathcal{W}^{Z}\left(g_{b}\right)=\mathcal{W}^{M}\left(g_{M}\right)+\mathcal{W}^{Z}\left(g_{Z}\right)$ in Section 5.
Remark 3.6. Notice that $g_{X}$ is not a smooth ( $C^{2}$ ) metric: indeed, the second derivatives of $g_{X}$ may be discontinuous at the boundary of the annulus $\{\gamma<|x|<1\}$. Nevertheless, the metric is globally $W^{2, \infty}$, so, if we are able to show that $\mathcal{W}^{X}\left(g_{X}\right)<\mathcal{W}^{N}\left(g_{a}\right)+\mathcal{W}^{Z}\left(g_{b}\right)$, then we can also find by density a smooth metric $\tilde{g}_{X}$ on $X$ satisfying the same inequality.

\section*{4 Biharmonic interpolation}

In this section we are going to explicitly compute the solution of system (3.13).
We begin by noticing that the boundary conditions of (3.13) can always be expressed as linear combinations of second spherical harmonics, which, by definition, are the restriction to $\mathbb{S}^{3}$ of homogeneous harmonic polynomials in $\mathbb{R}^{4}$ of degree 2 . Recall that there are 9 linearly independent second
spherical harmonics on $\mathbb{S}^{3}$ :
$$\begin{aligned}
& \varphi_{k, l}(x):=\text { restriction to } \mathbb{S}^{3} \text { of } x^{k} x^{l} \text { (6 functions) } \\
& \psi_{k, l}(x):=\text { restriction to } \mathbb{S}^{3} \text { of }\left(x^{k}\right)^{2}-\left(x^{l}\right)^{2} \text { (3 functions) }
\end{aligned}$$
Using the trace-free property and the symmetries of Weyl's tensor, we can rewrite system (3.13) as follows:
- if $i=j$, calling $s, t, u$ the remaining three indices in $\{1, \ldots, 4\}$ (so that $\{i, s, t, u\}$ are all distinct), we have
$$\begin{cases}\Delta^{2} w_{i i}=0 & \text { in } \gamma<|x|<1 \\ w_{i i}=1-\frac{1}{3} a^{2} \gamma^{-2}\left(2 W_{\text {siit }}^{M} \varphi_{s, t}+2 W_{\text {siiu }}^{M} \varphi_{s, u}+2 W_{\text {tiiu }}^{M} \varphi_{t, u}+W_{\text {siis }}^{M} \psi_{s, u}+W_{\text {tiit }}^{M} \psi_{t, u}\right) & \text { in }|x|=\gamma \\ w_{i i}=1-\frac{1}{3} b^{2}\left(2 W_{\text {siit }}^{Z} \varphi_{s, t}+2 W_{\text {siiu }}^{Z} \varphi_{s, u}+2 W_{\text {tiiu }}^{Z} \varphi_{t, u}+W_{\text {siis }}^{Z} \psi_{s, u}+W_{\text {tiit }}^{Z} \psi_{t, u}\right) & \text { in }|x|=1 \\ \partial_{r} w_{i i}=\frac{2}{3} a^{2} \gamma^{-3}\left(2 W_{\text {siit }}^{M} \varphi_{s, t}+2 W_{\text {siiu }}^{M} \varphi_{s, u}+2 W_{\text {tiiu }}^{M} \varphi_{t, u}+W_{\text {siis }}^{M} \psi_{s, u}+W_{\text {tiit }}^{M} \psi_{t, u}\right) & \text { in }|x|=\gamma \\ \partial_{r} w_{i i}=-\frac{2}{3} b^{2}\left(2 W_{\text {siit }}^{Z} \varphi_{s, t}+2 W_{\text {siiu }}^{Z} \varphi_{s, u}+2 W_{\text {tiu }}^{Z} \varphi_{t, u}+W_{\text {siis }}^{Z} \psi_{s, u}+W_{\text {tiit }}^{Z} \psi_{t, u}\right) & \text { in }|x|=1 .\end{cases}$$
This suggests to look for a solution of (4.2) of the type
$$w_{i i}=1+f_{s, t}(r) \varphi_{s, t}+f_{s, u}(r) \varphi_{s, u}+f_{t, u}(r) \varphi_{t, u}+\tilde{f}_{s, u}(r) \psi_{s, u}+\tilde{f}_{t, u}(r) \psi_{t, u},$$
where the $f$ 's and $\tilde{f}$ 's are purely radial functions $(r=|x|)$.
- if $i \neq j$, calling $s, t$ the remaining two indices in $\{1, \ldots, 4\}$, we have
$$\begin{cases}\Delta^{2} w_{i j}=0 & \text { in } \gamma<|x|<1 \\
w_{i j}=-\frac{1}{3} a^{2} \gamma^{-2}\left(W_{j i j i}^{M} \varphi_{j, i}+W_{j i j s}^{M} \varphi_{j, s}+W_{j i j t}^{M} \varphi_{j, t}+W_{s i j i}^{M} \varphi_{s, i}+W_{t i j i}^{M} \varphi_{t, i}\right. & \text { in }|x|=\gamma \\
\left.+\left(W_{s i j t}^{M}+W_{t i j s}^{M}\right) \varphi_{s, t}+W_{s i j s}^{M} \psi_{s, t}\right) & \\
w_{i j}=-\frac{1}{3} b^{2}\left(W_{j i j i}^{Z} \varphi_{j, i}+W_{j i j s}^{Z} \varphi_{j, s}+W_{j i j t}^{Z} \varphi_{j, t}+W_{s i j i}^{Z} \varphi_{s, i}+W_{t i j i}^{Z} \varphi_{t, i}\right. & \text { in }|x|=1 \\
\left.+\left(W_{s i j t}^{Z}+W_{t i j s}^{Z}\right) \varphi_{s, t}+W_{s i j s}^{Z} \psi_{s, t}\right) & \\
\begin{array}{r}
\partial_{r} w_{i j}=\frac{2}{3} a^{2} \gamma^{-3}\left(W_{j i j i}^{M} \varphi_{j, i}+W_{j i j s}^{M} \varphi_{j, s}+W_{j i j t}^{M} \varphi_{j, t}+W_{s i j i}^{M} \varphi_{s, i}+W_{t i j i}^{M} \varphi_{t, i}\right. \\
\left.+\left(W_{s i j t}^{M}+W_{t i j s}^{M}\right) \varphi_{s, t}+W_{s i j s}^{M} \psi_{s, t}\right)
\end{array} & \text { in }|x|=\gamma \\
\partial_{r} w_{i j}=-\frac{2}{3} b^{2}\left(W_{j i j i}^{Z} \varphi_{j, i}+W_{j i j s}^{Z} \varphi_{j, s}+W_{j i j t}^{Z} \varphi_{j, t}+W_{s i j i}^{Z} \varphi_{s, i}+W_{t i j i}^{Z} \varphi_{t, i}\right. & \text { in }|x|=1 . \\
\left.+\left(W_{s i j t}^{Z}+W_{t i j s}^{Z}\right) \varphi_{s, t}+W_{s i j s}^{Z} \psi_{s, t}\right) & \end{cases}$$
This suggests to look for a solution of (4.4) of the type
$$w_{i j}=f_{j, i}(r) \varphi_{j, i}+f_{j, s}(r) \varphi_{j, s}+f_{j, t}(r) \varphi_{j, t}+f_{s, i}(r) \varphi_{s, i}+f_{t, i}(r) \varphi_{t, i}+f_{s, t}(r) \varphi_{s, t}+\tilde{f}_{s, t}(r) \psi_{s, t},$$
where again the $f$ 's and $\tilde{f}$ 's are purely radial functions.
Consider now a general function $F$ on $B_{1} \backslash B_{\gamma} \subset \mathbb{R}^{4}$ of the form of (4.3), (4.5), namely
$$F(x)=\sum_{\alpha} f_{\alpha}(r) \varphi_{\alpha}(\vartheta)+C,$$
where $C$ is a constant, $r=|x|, \vartheta=\frac{x}{|x|} \in \mathbb{S}^{3}$ and the $\varphi_{\alpha}$ 's are second spherical harmonics (any type). Using the fact that each $\varphi_{\alpha}$ satisfies $\Delta_{\mathbb{S}^{3}} \varphi_{\alpha}=-8 \varphi_{\alpha}$, we see that
$$\Delta^{2} F=\sum_{\alpha} \varphi_{\alpha}(\vartheta) \underbrace{\left(f_{\alpha}^{(4)}(r)+\frac{6}{r} f_{\alpha}^{(3)}(r)-\frac{13}{r^{2}} f_{\alpha}^{\prime \prime}(r)-\frac{19}{r^{3}} f_{\alpha}^{\prime}(r)+\frac{64}{r^{4}} f_{\alpha}(r)\right)}_{=: T\left(f_{\alpha}\right)(r)},$$
and it is now easy to show that all the solutions to the ODE $T\left(f_{\alpha}\right)=0$ are of type
$$f_{\alpha}(r)=\frac{c_{1, \alpha}}{r^{4}}+\frac{c_{2, \alpha}}{r^{2}}+c_{3, \alpha} r^{2}+c_{4, \alpha} r^{4},$$
where $c_{1, \alpha}, c_{2, \alpha}, c_{3, \alpha}, c_{4, \alpha} \in \mathbb{R}$ are constants which depend upon the boundary data. In particular, in the situation described above we have:
- if $i=j$, for $(\alpha, \beta) \in\{(s, t),(s, u),(t, u)\}$,
$$\left\{\begin{array}{l}
f_{\alpha, \beta}(\gamma)=-\frac{2}{3} a^{2} \gamma^{-2} W_{\alpha i i \beta}^{M} \\
f_{\alpha, \beta}^{\prime}(\gamma)=\frac{4}{3} a^{2} \gamma^{-3} W_{\alpha i i \beta}^{M} \\
f_{\alpha, \beta}(1)=-\frac{2}{3} b^{2} W_{\alpha i i \beta}^{Z} \\
f_{\alpha, \beta}^{\prime}(1)=-\frac{4}{3} b^{2} W_{\alpha i i \beta}^{Z}
\end{array}\right.$$
while, for $(\alpha, \beta) \in\{(s, u),(t, u)\}$, one has
$$\left\{\begin{array}{l}
\tilde{f}_{\alpha, \beta}(\gamma)=-\frac{1}{3} a^{2} \gamma^{-2} W_{\alpha i i \alpha}^{M} \\
\tilde{f}_{\alpha, \beta}^{\prime}(\gamma)=\frac{2}{3} a^{2} \gamma^{-3} W_{\alpha i i \alpha}^{M} \\
\tilde{f}_{\alpha, \beta}(1)=-\frac{1}{3} b^{2} W_{\alpha i i \alpha}^{Z} \\
\tilde{f}_{\alpha, \beta}^{\prime}(1)=-\frac{2}{3} b^{2} W_{\alpha i i \alpha}^{Z}
\end{array}\right.$$

Writing now
$$\begin{aligned}
& f_{\alpha, \beta}(r)=\frac{c_{1, \alpha, \beta}}{r^{4}}+\frac{c_{2, \alpha, \beta}}{r^{2}}+c_{3, \alpha, \beta} r^{2}+c_{4, \alpha, \beta} r^{4} \\
& \tilde{f}_{\alpha, \beta}(r)=\frac{\tilde{c}_{1, \alpha, \beta}}{r^{4}}+\frac{\tilde{c}_{2, \alpha, \beta}}{r^{2}}+\tilde{c}_{3, \alpha, \beta} r^{2}+\tilde{c}_{4, \alpha, \beta} r^{4}
\end{aligned}$$
from the general formula (4.8) of $f_{\alpha, \beta}$ and (4.6) we obtain the following system:
$$\left\{\begin{array}{l}
\frac{c_{1, \alpha, \beta}}{\gamma^{4}}+\frac{c_{2, \alpha, \beta}}{\gamma^{2}}+c_{3, \alpha, \beta} \gamma^{2}+c_{4, \alpha, \beta} \gamma^{4}=-\frac{2}{3} a^{2} \gamma^{-2} W_{\alpha i i \beta}^{M} \\
-\frac{4 c_{1, \alpha, \beta}}{\gamma^{5}}-\frac{2 c_{2, \alpha, \beta}}{\gamma^{3}}+2 c_{3, \alpha, \beta} \gamma+4 c_{4, \alpha, \beta} \gamma^{3}=\frac{4}{3} a^{2} \gamma^{-3} W_{\alpha i i \beta}^{M} \\
c_{1, \alpha, \beta}+c_{2, \alpha, \beta}+c_{3, \alpha, \beta}+c_{4, \alpha, \beta}=-\frac{2}{3} b^{2} W_{\alpha i i \beta}^{Z} \\
-4 c_{1, \alpha, \beta}-2 c_{2, \alpha, \beta}+2 c_{3, \alpha, \beta}+4 c_{4, \alpha, \beta}=-\frac{4}{3} b^{2} W_{\alpha i i \beta}^{Z}
\end{array}\right.$$
which can be rewritten in the general matrix form
$$A_{\gamma} \mathbf{c}=a^{2} \mathbf{v},$$
where
$$A_{\gamma}:=\left(\begin{array}{cccc}
1 & \gamma^{2} & \gamma^{6} & \gamma^{8} \\
-4 & -2 \gamma^{2} & 2 \gamma^{6} & 4 \gamma^{8} \\
1 & 1 & 1 & 1 \\
-4 & -2 & 2 & 4
\end{array}\right),$$
and
$$\mathbf{c}=\mathbf{c}_{\alpha, \beta}=\left(\begin{array}{c}
c_{1, \alpha, \beta} \\
c_{2, \alpha, \beta} \\
c_{3, \alpha, \beta} \\
c_{4, \alpha, \beta}
\end{array}\right), \quad \mathbf{v}=\mathbf{v}_{\alpha, \beta}=\left(\begin{array}{c}
-\frac{2}{3} \gamma^{2} W_{\alpha i i \beta}^{M} \\
\frac{4}{3} \gamma^{2} W_{\alpha i i \beta}^{M} \\
-\frac{2}{3} b^{2} a^{-2} W_{\alpha i i \beta}^{Z} \\
-\frac{4}{3} b^{2} a^{-2} W_{\alpha i i \beta}^{Z}
\end{array}\right) .$$

Similarly, from formula (4.9) for $\tilde{f}_{\alpha, \beta}$ and the boundary datum (4.7) we obtain a system of type (4.10) with
$$\mathbf{c}=\tilde{\mathbf{c}}_{\alpha, \beta}=\left(\begin{array}{c}
\tilde{c}_{1, \alpha, \beta} \\
\tilde{c}_{2, \alpha, \beta} \\
\tilde{c}_{3, \alpha, \beta} \\
\tilde{c}_{4, \alpha, \beta}
\end{array}\right), \quad \mathbf{v}=\tilde{\mathbf{v}}_{\alpha, \beta}=\left(\begin{array}{c}
-\frac{1}{3} \gamma^{2} W_{\alpha i i \alpha}^{M} \\
\frac{2}{3} \gamma^{2} W_{\alpha i i \alpha}^{M} \\
-\frac{1}{3} b^{2} a^{-2} W_{\alpha i i \alpha}^{Z} \\
-\frac{2}{3} b^{2} a^{-2} W_{\alpha i i \alpha}^{Z}
\end{array}\right) .$$