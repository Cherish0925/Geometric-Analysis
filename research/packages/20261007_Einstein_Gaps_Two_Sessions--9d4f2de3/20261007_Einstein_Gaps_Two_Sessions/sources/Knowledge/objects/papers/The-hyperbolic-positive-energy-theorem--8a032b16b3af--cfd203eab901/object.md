# The hyperbolic positive energy theorem

- Category: papers
- Identity: arxiv:1901.05263
- Content status: fulltext_ok

---

---
source_file: 1901_05263.pdf
converter: mathpix
format: mmd
---

\title{
The hyperbolic positive energy theorem*
}

\author{
Piotr T. Chruściel ${ }^{\dagger \ddagger}$ \\ Erwann Delay ${ }^{\$}$
}

April 6, 2026

\begin{abstract}
We show that the causal-future-directed character of the energy-momentum vector of $n$-dimensional asymptotically hyperbolic Riemannian manifolds with spherical conformal infinity, $n \geq 3$, can be traced back to that of asymptotically Euclidean general-relativistic initial data sets satisfying the dominant energy condition.
\end{abstract}

\section*{Contents}
1 Introduction ..... 1
2 Definitions, notations and conventions ..... 3
2.1 Asymptotically hyperbolic manifolds ..... 3
2.2 Energy-momentum ..... 4
3 Localised "Maskit" gluings ..... 5
4 Positivity for asymptotically hyperbolic Riemannian manifolds ..... 9

\section*{1 Introduction}

An interesting global invariant of asymptotically hyperbolic general relativistic initial data sets is the energy-momentum vector $\mathbf{m} \equiv\left(m_{\mu}\right)[9,12,30]$ (compare [1, 13]). In the case of spherical conformal infinity, it is known that m is timelike future pointing under a spin condition [9, 10, 17, 24, 30]. The object of this work is to show how to remove this condition.

Our analysis will rely on the following rigidity conjecture:
Conjecture 1.1 Let $(M, g, K)$ be an $n$-dimensional general relativistic initial data set, $n \geq 3$, satisfying the dominant energy condition such that $g$ is flat

\footnotetext{
*Preprint UWThPh-2019-3
${ }^{\dagger}$ Beijing Institute of Mathematical Sciences and Applications, Huairou, and Center for Theoretical Physics of the Polish Academy of Sciences, Warsaw
${ }^{\ddagger}$ EmaIL piotr.chrusciel@univie.ac.at, URL homepage.univie.ac.at/piotr.chrusciel
${ }^{\text {§ }}$ Université d'Avignon, Laboratoire de Mathématiques d'Avignon (EA 2151), 301 rue Baruch de Spinoza, F-84916 Avignon, France
${ }^{1}$ Email erwann.delay@univ-avignon.fr, URL https://erwanndelay.wordpress.com/
}
outside of a compact set and $K$ vanishes there. Then $(M, g)$ can be isometrically embedded in Minkowski space-time so that $K$ is the second fundamental form of the embedded hypersurface.

A published proof of this conjecture in dimensions less than or equal to seven can be found in [15, 16, 20], building upon [26-28], and a preprint covering all dimensions is available as [23] (with the borderline cases covered in [20]). Conjecturally, this result also follows in all dimensions by reduction from the time-symmetric case addressed in the preprint [29].

In order to comply with the hypotheses of Conjecture 1.1, from now on the manifold $M$ will be assumed to be the union of a compact set and of an asymptotic end diffeomorphic to $[0, \infty) \times \mathbb{S}^{n-1}$, where $\mathbb{S}^{k}$ denotes a $k$-dimensional sphere. In other words, $M$ will be assumed to be a smooth, connected, non-compact manifold with one end diffeomorphic to $[0, \infty) \times \mathbb{S}^{n-1}$.

Remark 1.2 We note that the statement remains true with several asymptotically Euclidean ends, as large spheres in the remaining asymptotic ends provide barriers for the relevant constructions. (This shows in particular that orientability is not needed, as one can always pass to a double cover of the manifold; this introduces a second asymptotically Euclidean end which is innocuous for the problem at hand.) Similarly outer trapped, or marginally outer-trapped compact boundaries are allowed; these will carry over to the hyperbolic setting as in Remark 1.4 below. \(\square\)

Let $(M, g)$ denote an $n$-dimensional Riemannian manifold with the topology just-explained. We use the "exotic hyperbolic gluings" of [7], together with the deformation results of [8], to establish our main result here, which is new for all dimensions unless the manifold is spin:

Theorem 1.3 Assume that Conjecture 1.1 is true in some dimension $n \geq 3$. Consider an asymptotically hyperbolic manifold $(M, g)$ with spherical conformal infinity and well-defined energy-momentum vector $\mathbf{m}$. If
$$R(g) \geq-n(n-1),$$
then m is causal future directed or vanishes; in the last case $M$ is isometrically diffeomorphic to hyperbolic space.

Remark 1.4 In the asymptotically hyperbolic (AH) spin case, the timelike future-directed character of m has been established for manifolds which are complete with compact boundary, when the mean curvature $H$ of the boundary satisfies $H \leq n-1$ (cf., e.g., [9]). Our method, for reducing the Riemannian AH case to an asymptotically Euclidean (AE) one (which uses the replacement of $K$ by $K-g$, compare (4.1)-(4.2)), transforms such boundaries in the AH regime to ones satisfying $H \leq 0$ in the AE framework. This clarifies the somewhat mysterious AH condition $H \leq n-1$. \(\square\)

Remark 1.5 A precise set of asymptotic conditions needed for a well defined hyperbolic mass can be found e.g. in [9, Proposition 2.2]. It should be emphasised that these detailed asymptotic conditions are irrelevant for our proof in the following sense: given a metric with well defined energy-momentum, we start by
deforming the metric in the asymptotic region so that the energy-momentum is almost unchanged but the perturbed metric is smoothly conformally compactifiable. When the Ricci scalar $R$ satisfies $R \leq 0$ this can be done by repeating the arguments in [6, Section 6]. For metrics which fail to satisfy $R \leq 0$ one can use the argument of [6, Section 6] together with a compactly supported deformation of the metric which compensates for the kernel of the linearised Yamabe operator, as in the proof of [14, Lemma 4.2]. The deformed metric is then conformal to the hyperbolic metric in a neighborhood of the boundary, hence conformally smooth, with a smooth conformal factor by [3, Theorem 1.3]. This allows one to carry-out subsequent arguments basing on smoothly compactifiable metrics with well defined mass aspect function, cf. [8]. The fact that the glued metric used below to obtain a contradiction is likely to have less regularity at the conformal boundary does not affect the argument, as it can be slightly deformed again to a conformally smooth metric. \(\square\)

The proof of Theorem 1.3 proceeds by contradiction and uses perturbations of the metric. This approach prevents us from considering the borderline cases. However, it is shown in [19] how to use our conclusion to assert that m is timelike or vanishing, and vanishes only for hyperbolic space.

Let $\mathbb{H}^{n}$ denote $n$-dimensional hyperbolic space (with sectional curvatures normalised to -1). A step in the proof of Theorem 1.3, with some of interest of its own, is provided by the following:

Theorem 1.6 Assume that Conjecture 1.1 is true in some dimension $n \geq 3$, and consider an $n$-dimensional Riemannian manifold $(M, g)$ with scalar curvature $R(g)$ satisfying
$$R(g) \geq-n(n-1) .$$
If $(M, g)$ contains a region isometric to the complement of a compact set in $\mathbb{H}^{n}$, then $(M, g)$ is isometrically diffeomorphic to $\mathbb{H}^{n}$.

We note that Theorem 1.6 is already known to be true in dimensions $3 \leq$ $n \leq 7$ [2], where Conjecture 1.1 has already been established anyway, and for spin manifolds [4, 9, 22, 25, 30]). We do not assume that $M$ is spin, and our proof is different from that of [2].

We finish this introduction by noting that our analysis, together with Theorem 1.1 and an argument of Wang [31], implies uniqueness of higher-dimensional Anti de Sitter metric in the class of strictly static vacuum metrics with a negative cosmological constant and spherical conformal boundary at infinity.

\section*{2 Definitions, notations and conventions}

For the convenience of the reader we summarise our definitions and conventions, which are mostly as in [7].

\subsection*{2.1 Asymptotically hyperbolic manifolds}

We model hyperbolic space on the unit ball $B$ in $\mathbb{R}^{n}$, endowed with the metric
$$b=z^{-2} \delta,$$
where $\delta$ is the Euclidean metric and $z(x)=\frac{1}{2}\left(1-|x|_{\delta}^{2}\right)$.
Let $(M, \stackrel{\circ}{g})$ be a smooth $n$-dimensional Riemannian manifold without boundary such that, outside of a compact set, the manifold is diffeomorphic to $B$ minus a closed ball, and there the metric $\dot{g}$ equals $b$. The function $z$ is then extended to a smooth positive function on $M$, still denoted by $z$.

Let $\varphi$ be a smooth strictly positive function on $M$. For $k \in \mathbb{N}$ and $\alpha \in[0,1]$ we define $C_{\varphi}^{k, \alpha}$ to be the space of $C^{k, \alpha}$ functions or tensor fields for which the norm
$$\begin{aligned}
\|u\|_{C_{\varphi}^{k, \alpha}(\grave{g})}= & \sup _{x \in M} \sum_{i=0}^{k}\left(\left|\varphi \stackrel{\circ}{\nabla}^{(i)} u(x)\right|_{\grave{g}}\right. \\
& \left.+\sup _{0<d_{\hat{g}}(x, y) \leq 1 / 2} \varphi(x) \frac{\left|\stackrel{\circ}{\nabla}^{(i)} u(x)-\stackrel{\circ}{\nabla}^{(i)} u(y)\right|_{\hat{g}}}{d_{\stackrel{\circ}{g}}^{\alpha}(x, y)}\right)
\end{aligned}$$
is finite. Here the norm $|\cdot|_{\dot{g}}$ and the covariant derivative $\stackrel{\circ}{\nabla}$ are defined using $\stackrel{\circ}{g}$, and $d_{\dot{g}}(x, y)$ is the $\dot{g}$-distance between $x$ and $y$.

A metric $g$ on $M$ will be called asymptotically hyperbolic, or AH, (with spherical conformal infinity) if $g$ tends to $\stackrel{\circ}{g}$ in an appropriate function space. More precisely, given a function space $W$, an asymptotically hyperbolic metric $g$ will be said to be of $M_{\dot{g}+W}$ class if $g-\stackrel{\circ}{g} \in W$.

In our context one is typically interested in $M_{\dot{g}+W}$ metrics with $W=C_{z^{-\sigma}}^{k}$ with $\sigma>0$. In local coordinates as above such metrics decay to the model metric as $z^{\sigma-2}$, or as $z^{\sigma}$ in $\stackrel{\circ}{g}$-norm, with derivatives satisfying uniform weighted estimates near the boundary. Further, there exists then a constant $C$ such that
$$|g-\stackrel{\circ}{g}|_{\dot{g}}+|\stackrel{\circ}{\nabla} g|_{\dot{g}}+\ldots+\left|\stackrel{\circ}{\nabla}^{(k)} g\right|_{\dot{g}} \leq C z^{\sigma} .$$
For $\mathbb{R} \ni \sigma>k \geq 1, k \in \mathbb{N}$ and $g \in M_{\hat{g}+C_{1, z}^{k}-\sigma}$ the conformally rescaled metric $z^{2} g$ can be extended to the conformal boundary $\mathbb{S}^{n-1}$ of $M$, with the extension belonging to the $C^{\lfloor\sigma\rfloor}$-differentiability class.

\subsection*{2.2 Energy-momentum}

The definition of energy-momentum of an asymptotically hyperbolic manifold requires choosing a coordinate system in which the metric manifestly approaches the hyperbolic metric. Let us denote by $\phi$ the choice of such a coordinate system. In the case of spherical conformal infinity, which is of interest here, such structures can be parameterised by the conformal group of $\mathbb{S}^{n-1}$. Indeed, let us denote by $\phi$ a coordinate system $\left(r, \theta^{A}\right)$, with $\theta^{A}$ local coordinates on $\mathbb{S}^{n-1}$, in which $g$ takes the form
$$g \rightarrow_{r \rightarrow \infty} \frac{d r^{2}}{1+r^{2}}+r^{2} \underbrace{\stackrel{\circ}{h}_{A B}(\theta) d \theta^{A} d \theta^{B}}_{=: \grave{h}^{A}}=: b$$
with $\stackrel{\circ}{h}$ being the unit round metric on $\mathbb{S}^{n-1}$, where the asymptotics is understood by requiring the $b$-norm $|g-b|_{b}$ of $g-b$ to decay to zero as one recedes to infinity. (To have a well defined energy-momentum one also needs fall-off rates, as well as derivative-decay conditions [9, 11], which will be implicitly assumed whenever relevant). If $\hat{\phi}$ is another such coordinate system in which
$$g \rightarrow_{\hat{r} \rightarrow \infty} \frac{d \hat{r}^{2}}{1+\hat{r}^{2}}+\hat{r}^{2} \underbrace{\stackrel{\circ}{h}_{A B}(\hat{\theta}) d \hat{\theta}^{A} d \hat{\theta}^{B}}_{=: \hat{h}},$$
then there exists a conformal transformation $\Lambda$ of $\left(\mathbb{S}^{n-1}, \stackrel{\circ}{h}\right)$ so that $\hat{h}$ is obtained from $\stackrel{\circ}{h}$ by applying $\Lambda$ (cf., e.g., [9, 11]). We then write $\hat{\phi}=\Lambda \phi$, hoping that the reader will not get confused by our use, later, of the same notation for the action of the conformal group on vectors by Lorentz transformations.

We will write $(M, g, \phi)$ for an asymptotically hyperbolic metric $(M, g)$ with an asymptotic structure $\phi$.

Recall that static Killing Initial Data (KIDs) are solutions $V$ of the set of equations
$$\stackrel{\circ}{D}_{i} \stackrel{\circ}{D}_{j} V=\left(\operatorname{Ric}(b)_{i j}+n b_{i j}\right) V,$$
where $b$ is the hyperbolic metric and $\stackrel{\circ}{D}$ its covariant derivative operator. This is an $(n+1)$-dimensional vector space equipped with a natural Lorentzian scalar product.

Letting $\left\{V_{\mu}\right\}_{\mu=0}^{n}$ be an orthonormal basis of the space of static KIDs, the energy-momentum vector $\mathbf{m}=\left(m_{\mu}\right)$ can be defined as [18] (compare [5, Equation (IV.40)])
$$m_{\mu}=-\lim _{r \rightarrow \infty} \int_{\mathbb{S}^{n-1}(r)} D^{j} V_{\mu}\left(R_{j}^{i}-\frac{R}{n} \delta_{j}^{i}\right) d \sigma_{i},$$
where $R_{i j}$ is the Ricci tensor of the metric $g, R$ its trace, and we have ignored an overall dimension-dependent positive multiplicative factor.

Using the Poincaré-ball model, the $\mathbb{S}^{n-1}(r)$ 's can be taken to be coordinate spheres of Euclidean radius $1-1 / r$ accumulating at the conformal boundary $\mathbb{S}^{n-1}(+\infty)$ as $r$ tends to infinity.

The energy-momentum m is well defined e.g. when $k \geq 1, \sigma>\frac{n}{2}$, and $R+n(n-1)$, where $R$ is the curvature scalar of $g$, is in $L^{1}$; see [9]. In fact, rather weaker weighted-Sobolev conditions suffice.

On the other hand, the mass aspect function is well defined if, e.g., the conformally rescaled metric $\tilde{g}:=z^{-n} g$ is $C^{n}(\bar{M})$ in its own Gauss coordinates; this corresponds more or less to $\sigma \geq n$ and $k \geq n$.

\section*{3 Localised "Maskit" gluings}

The aim of this section is to analyse what happens with the energy-momentum under the localised Maskit-type gluings of asymptotically hyperbolic manifolds of [7, Section 3.5] for spherical conformal boundaries. It is clear that the analysis below can be adapted to the conformal gluings of Isenberg, Lee and Stavrov [21] in the spherical case, and we will not discuss this case any further. On the other hand it is not obvious how to adapt our calculations to non-spherical conformal boundaries, it would be of interest to settle this.

The gluing construction relevant for our purposes proceeds as follows: Consider points $p_{1}, p_{2}$, lying each on the conformal boundary of two asymptotically hyperbolic manifolds $\left(M_{1}, g_{1}\right)$ and $\left(M_{2}, g_{2}\right)$, each metric with scalar curvature larger than or equal $-n(n-1)$, with total energy-momentum vectors $\mathbf{m}^{1} \equiv\left(m_{\mu}^{1}\right)$ and $\mathbf{m}^{2} \equiv\left(m_{\mu}^{2}\right)$. We will assume that both $\left(M_{1}, g_{2}\right)$ and $\left(M_{2}, g_{2}\right)$ have spherical conformal infinity (by this we mean that the conformal class of the boundary metric is that of the canonical metric on the sphere), and have a well-defined
total energy-momentum. As shown in [7] for all $\varepsilon>0$ sufficiently small we can construct new metrics $\left(M_{i}, g_{i, \varepsilon}\right), i=1,2$, each with scalar curvature larger than or equal $-n(n-1)$, such that:
\begin{itemize}
\item[1.] the metrics coincide with the hyperbolic metric in coordinate half-balls $\mathscr{U}_{\varepsilon}^{1}$ of radius $\varepsilon$ (as measured with respect to the "compactified" metric) around $p_{1}$ and $\mathscr{U}_{\varepsilon}^{2}$ around $p_{2}$;
\item[2.] the new metrics coincide with the original ones outside of balls of radius $2 \varepsilon$;
\item[3.] the total energy-momenta of the new metrics tend to the original ones as $\varepsilon$ tends to zero.
\end{itemize}

Choose some asymptotic structures $\phi_{i}$ on $\left(M_{i}, g_{i}\right)$ and let
$$\mathbf{m}^{i, \varepsilon} \equiv\left(m_{\mu}^{i, \varepsilon}\right)$$
denote the energy-momenta of $\left(M_{i}, g_{i, \varepsilon}, \phi_{i}\right)$. As already mentioned, the construction in [7] guarantees that
$$m_{\mu}^{i, \varepsilon} \rightarrow_{\varepsilon \rightarrow 0} m_{\mu}^{i}, i=1,2 .$$
Remark 3.1 For our further purposes we need to complement (3.1) with a decay rate, which can be read-off from [7, Section 3.3]. We note that the background hyperbolic metric, denoted in the current work by $b$, is denoted by $\stackrel{\circ}{g}$ there (recall that $\stackrel{\circ}{g}$ is used here to denote a metric on $M$ which coincides with $b$ on the asymptotic end but not necessarily everywhere, e.g. because of a different topology of $M$ ), and that we use here $s$ instead of the symbol $b$ used in [7] for the rate of radial decay of the glued metrics. Let us thus assume that
$$|g-b|_{b}=O\left(r^{-\sigma}\right) \text { with } \sigma>(n-1) / 2+s$$
for some $s \in[n / 2,(n+1) / 2)$. By [7, Remark 3.6] and the comments at the end of Section 3.3 in [7], the $b$-norm of the correction $h_{\varepsilon}$ to the metric arising from the gluing procedure is then of order $o\left(\varepsilon^{\sigma-s} r^{-s}\right)$. Now recall that the mass is the limit, as $r$ tends to infinity, of an integral on a sphere of radius $r$ of a quantity, say $\mathbb{U}$ (cf. (2.6)). In this limit only the part of $\mathbb{U}$ linear in $e_{\varepsilon}=g_{\varepsilon}-b=g-b+h_{\varepsilon}=e+h_{\varepsilon}$ matters. This implies (cf. the last, unnumbered, equation in the proof of [7, Theorem 3.7])
$$m_{\mu}^{i, \varepsilon}-m_{\mu}^{i}=o\left(\varepsilon^{\sigma-s}\right), i=1,2 .$$
When working in weighted Hölder spaces, the decay rate $s>n / 2$ is needed for the final mass to be well defined, while one needs $\sigma \leq n$ for the initial mass to be non-zero. The resulting best approach rate $\sigma-s$ is as close as desired to, but smaller than, $n / 2$. In our positivity proof below, the decay rate $\sigma=n$ is obtained by invoking the density results of [14], independently of the decay rate of the metric under consideration. We will see that this suffices for the positivity theorem in space dimensions $n \geq 5$.

A more careful analysis, which provides
$$m_{\mu}^{i, \varepsilon}-m_{\mu}^{i}=o\left(\varepsilon^{n / 2}\right), i=1,2,$$
is needed when $n=4$. To obtain this estimate one notes that all the gluing results in [7] can be traced back to Theorem 3.3 there, where the solution of the problem at hand is constructed in weighted Sobolev spaces. In view of the already mentioned results in [14], in [7, Theorem 3.3] we can take $\sigma=n$, and choose $b$ there (which coincides with $s$ here) to be $n / 2$ (the mass still being well defined, the correction being in $H_{1, z^{-n / 2}}^{k+2}$ in the notation of [7]). This provides the improved decay rate (3.3); compare [7, Remark 3.4]. \(\square\)

Let
$$\mathscr{H} \subset \mathbb{H}^{n} \subset \mathbb{R}^{n}$$
denote the equatorial hyperplane in the Poincaré ball model. So $\mathscr{H}$ is a totally geodesic hypersurface which "cuts the hyperbolic space in half", and its conformal completion intersects the conformal boundary of $\mathbb{H}^{n}$ at the equator. We denote by $\mathbb{H}_{+}^{n}$ the part of $\mathbb{H}^{n}$ which lies "above" $\mathscr{H}$ and by $\mathbb{H}_{-}^{n}$ the part of $\mathbb{H}^{n}$ which lies "below" $\mathscr{H}$. More precisely, $\mathbb{H}_{+}^{n}$ is the part of $\mathbb{H}^{n}$ with the height coordinate larger than or equal zero, and $\mathbb{H}_{-}^{n}$ is the part of $\mathbb{H}^{n}$ with the height coordinate smaller than or equal zero. (While this is completely irrelevant at this stage, we note that for typographical reasons, related to the calculations in Equation (4.8) and following, it will be convenient to think of the height as being determined by the first coordinate in $\mathbb{R}^{n}$, thus the equator on the conformal boundary will be defined as the intersection of the unit coordinate sphere in $\mathbb{R}^{n}$ with the hyperplane $\left\{x^{1}=0\right\}$.)

Recall that the connected component of the group of conformal isometries of a sphere $\mathbb{S}^{n-1}$ is isomorphic to the component of the identity of the Lorentz group in dimension $n+1$ and the action, which we denote by $\Lambda \mathbf{m}$, of an element $\Lambda$ of the conformal group of the sphere on the energy-momentum vector $\mathbf{m}$, is the standard linear action of the Lorentz group on $\mathbb{R}^{1, n}$.

Let $D_{\varepsilon}^{i}$ denote the $(n-1)$-dimensional ball centered at $p_{i}$, contained in the conformal boundary, obtained by intersecting $\mathscr{U}_{\varepsilon}^{i}$ with the conformal boundary; see the middle figure in Figure 3.1. Let us denote by $\Lambda_{\varepsilon}^{1}$ the conformal transformation of the conformal boundary which maps $D_{\varepsilon}^{1}$ to the upper half-sphere. See the right figure in Figure 3.1.

In physics terminology, $\Lambda_{\varepsilon}^{1}$ is a boost in the direction of $-p_{1}$, when $\mathbb{S}^{n-1}$ is viewed as a coordinate sphere in $\mathbb{R}^{n}$; this can be seen e.g. from [8, Section 3.4]. The velocity parameter of the boost tends to the speed of light as $\varepsilon$ tends to zero.

After applying $\Lambda_{\varepsilon}^{1}$ we obtain a set $\left(M_{1}, g_{1, \varepsilon}, \Lambda_{\varepsilon}^{1} \phi_{1}\right)$ with energy-momentum vector $\Lambda_{\varepsilon}^{1} \mathbf{m}^{1, \varepsilon}$. $M_{1}$ contains a region, denoted by $\mathscr{V}_{\varepsilon}^{1}$, defined as the "half-hyperbolic-space" $\mathbb{H}_{+}^{n}$ in the coordinate system $\Lambda_{\varepsilon}^{1} \phi_{1}$. The boundary $\partial \mathscr{V}_{\varepsilon}^{1}$ corresponds in the local coordinates to $\mathscr{H}$, is totally geodesic, and the metric $g_{1, \varepsilon}$ is exactly hyperbolic throughout $\mathbb{H}_{+}^{n}$ and in a neighborhood of $\mathscr{H} \approx \partial \mathscr{V}_{\varepsilon}^{1}$. Thus
$$\mathbb{H}_{+}^{n} \approx \mathscr{V}_{\varepsilon}^{1} \subset \mathscr{U}_{\varepsilon}^{1} \subset M_{1},$$
where $\approx$ in (3.4) means "isometrically diffeomorphic to".
Letting, as before, $\left\{V_{\mu}\right\}_{\mu=0}^{n}$ be an orthonormal basis of the space of static KIDs, we have
$$\left(\Lambda_{\varepsilon}^{1} \mathbf{m}^{1, \varepsilon}\right)_{\mu}=-\lim _{r \rightarrow \infty} \int_{\mathbb{S}^{n-1}(r)} D^{j} V_{\mu}\left(R_{j}^{i}-\frac{R}{n} \delta_{j}^{i}\right) d \sigma_{i},$$

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/2ca93298-d0a2-4210-90d1-ffc285329a86-08.jpg?height=351&width=1221&top_left_y=432&top_left_x=465}
\captionsetup{labelformat=empty}
\caption{Figure 3.1: A small spherical cap $D_{\varepsilon}^{1} \subset \mathbb{S}^{n-1}$ (middle picture) is mapped to the upper-half sphere by the conformal transformation $\Lambda_{\varepsilon}^{1}$. The final metric coincides with the hyperbolic one in a region which includes the upper half-ball. We assume the topology of conformal infinity to be spherical, but the interior does not have to be topologically trivial. Thus, the topology inside the final upper half-sphere is that of a half-ball, with the boundary of the lower-half sphere (including the equatorial hyperplane) bounding the remaining topology of $M_{1}$.}
\end{figure}
where now $R_{i j}$ is the Ricci tensor of the metric $g_{1, \varepsilon}$.
Let $\mathbb{S}_{-}^{n-1}(r)$ denote the part of the sphere which lies under the equator, and $\mathbb{S}_{+}^{n-1}(r)$ the part above the equator. Since the trace-free part of the Ricci tensor of $g_{1, \varepsilon}$ vanishes on $\mathbb{H}_{+}^{n}$, only the integrals on $\mathbb{S}_{-}^{n-1}(r)$ contribute:
$$\left(\Lambda_{\varepsilon}^{1} \mathbf{m}^{1, \varepsilon}\right)_{\mu}=-\lim _{r \rightarrow \infty} \int_{\mathbb{S}_{-}^{n-1}(r)} D^{j} V_{\mu}\left(R_{j}^{i}-\frac{R}{n} \delta_{j}^{i}\right) d \sigma_{i} .$$

Similarly there exists a conformal transformation of the conformal boundary, which will be denoted by $\Lambda_{\varepsilon}^{2}$, which maps $D_{\varepsilon}^{2}$ to the lower half-sphere. See Figure 3.2. After applying this transformation, $M_{2}$ contains a region, which we denote by $\mathscr{V}_{\varepsilon}^{2}$, isometrically diffeomorphic to the half-hyperbolic-space $\mathscr{H}_{-}$, as well as its totally geodesic boundary $\mathscr{H}$, with the metric being exactly hyperbolic in a neighborhood of $\mathscr{H}$, and throughout $\mathscr{V}_{\varepsilon}^{2}$. Analogously to (3.4) we have
$$\mathbb{H}_{-}^{n} \approx \mathscr{V}_{\varepsilon}^{2} \subset \mathscr{U}_{\varepsilon}^{2} \subset M_{2} .$$
One also finds
$$\begin{aligned}
\left(\Lambda_{\varepsilon}^{2} \mathbf{m}^{2, \varepsilon}\right)_{\mu} & =-\lim _{r \rightarrow \infty} \int_{\mathbb{S}^{n-1}(r)} D^{j} V_{\mu}\left(R_{j}^{i}-\frac{R}{n} \delta_{j}^{i}\right) d \sigma_{i} \\
& =-\lim _{r \rightarrow \infty} \int_{\mathbb{S}_{+}^{n-1}(r)} D^{j} V_{\mu}\left(R_{j}^{i}-\frac{R}{n} \delta_{j}^{i}\right) d \sigma_{i},
\end{aligned}$$
where $R_{i j}$ is now the Ricci tensor of the metric $g_{2, \varepsilon}$.
Since the metric equals the hyperbolic metric near $\mathscr{H}$ in both manifolds, we can construct a new family of AH metrics $\left(M, g_{\varepsilon}\right)$ by gluing together $M_{1} \backslash \mathscr{V}_{\varepsilon}^{1}$ with $M_{2} \backslash \mathscr{V}_{\varepsilon}^{2}$ along $\mathscr{H}$, with the obvious asymptotic structure $\phi$ and the obvious smooth metric $g_{\varepsilon}$.

Denote by $\mathbf{m}^{\varepsilon} \equiv\left(m_{\mu}^{\varepsilon}\right)$ the total energy-momentum vector of $\left(M, g_{\varepsilon}, \phi\right)$. We

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/2ca93298-d0a2-4210-90d1-ffc285329a86-09.jpg?height=350&width=1219&top_left_y=432&top_left_x=466}
\captionsetup{labelformat=empty}
\caption{Figure 3.2: A small spherical cap $D_{\varepsilon}^{2} \subset \mathbb{S}^{n-1}$ (left picture) is mapped to the lower-half sphere by the conformal transformation $\Lambda_{\varepsilon}^{2}$. The final manifold $\left(M, g_{\varepsilon}\right)$ is obtained by gluing together the manifold from the right Figure 3.1 with the manifold from the middle figure here. The metric $g_{\varepsilon}$ coincides with $g_{1, \varepsilon}$ on the "lower half" of the final manifold and with $g_{2, \varepsilon}$ on the "upper half", except for two transition strips near the equatorial hyperplane, and is exactly hyperbolic in an overlapping strip enclosing the equatorial hyperplane shown in the right figure.}
\end{figure}
have
$$\begin{aligned}
m_{\mu}^{\varepsilon}= & -\lim _{r \rightarrow \infty} \int_{\mathbb{S}^{n-1}(r)} D^{j} V_{\mu}\left(R^{i}{ }_{j}-\frac{R}{n} \delta_{j}^{i}\right) d \sigma_{i} \\
= & -\lim _{r \rightarrow \infty} \int_{\mathbb{S}_{-}^{n-1}(r)} D^{j} V_{\mu}\left(R^{i}{ }_{j}-\frac{R}{n} \delta_{j}^{i}\right) d \sigma_{i} \\
& -\lim _{r \rightarrow \infty} \int_{\mathbb{S}_{+}^{n-1}(r)} D^{j} V_{\mu}\left(R_{j}^{i}-\frac{R}{n} \delta_{j}^{i}\right) d \sigma_{i} \\
= & \left(\Lambda_{\varepsilon}^{1} m^{1, \varepsilon}\right)_{\mu}+\left(\Lambda_{\varepsilon}^{2} m^{2, \varepsilon}\right)_{\mu} .
\end{aligned}$$
In other words,
$$\mathbf{m}^{\varepsilon}=\Lambda_{\varepsilon}^{1} \mathbf{m}^{1, \varepsilon}+\Lambda_{\varepsilon}^{2} \mathbf{m}^{2, \varepsilon} .$$

Thus, the energy-momentum is additive under the above Maskit-type gluing, in a sense made precise by (3.9).

\section*{4 Positivity for asymptotically hyperbolic Riemannian manifolds}

For the convenience of the reader we recall Conjecture 1.1:
Conjecture 4.1 Let $(M, g, K)$ be an $n$-dimensional general relativistic initial data set, $n \geq 3$, satisfying the dominant energy condition such that $g$ is flat outside of a compact set and $K$ vanishes there. Then $(M, g)$ can be isometrically embedded in Minkowski space-time so that $K$ is the second fundamental form of the embedded hypersurface.

We first deduce the following

Theorem 4.2 Consider an $n$-dimensional Riemannian manifold $(M, g), n \geq 3$, with scalar curvature $R(g)$ satisfying
$$R(g) \geq-n(n-1) .$$
Suppose that Conjecture 4.1 holds in this dimension. If $(M, g)$ contains a region isometric to the complement of a compact set in $\mathbb{H}^{n}$, then $(M, g)$ is isometrically diffeomorphic to $\mathbb{H}^{n}$.

Proof Consider an asymptotically hyperbolic manifold $(M, g)$ as in the statement of the theorem. The pair $(M, g)$ can be viewed as a general relativistic initial data set $(M, g, K \equiv 0)$ for Einstein equations with negative cosmological constant $\Lambda=-n(n-1) / 2$, with matter fields with positive energy density $\rho:=R(g)+n(n-1)$, and with vanishing matter current $J:=0$. But one can also view $(M, g)$ as an initial data set
$$\left(M, g_{1}:=g, K_{1}:=-g_{1}\right)$$
for Einstein equations with vanishing cosmological constant, with positive energy density $\rho_{1}=\rho$, and with vanishing matter current $J_{1} \equiv 0$. This follows immediately from the following trivial calculation
$$R\left(g_{1}\right) \equiv R(g)=\rho+2 \Lambda=\rho+\left|K_{1}\right|_{g_{1}}^{2}-\operatorname{tr}_{g_{1}}\left(K_{1}\right)^{2} .$$
Let us denote by $\mathscr{U} \subset M$ the region of $M$ where $g_{1} \equiv g$ is exactly hyperbolic. Then $\left(\mathscr{U}, g_{1}\right)$ can be embedded into $(n+1)$-dimensional Minkowski space-time $\mathbb{R}^{1, n}$ as a hyperboloid so that its second fundamental form coincides with $K_{1}$. By passing to a subset of $\mathscr{U}$ if necessary there exists $R>0$ so that $\mathscr{U}$ can be identified with
$$\mathscr{U}=\left\{t=-\sqrt{1+|\vec{x}|^{2}},|\vec{x}|>R\right\} .$$
Let $f$ be any smooth function which coincides with $-\sqrt{1+|\vec{x}|^{2}}$ for $R \leq|\vec{x}| \leq$ $R+1$, which is constant for large $|\vec{x}|$, and such that the graph of $f$ over the set $\{|\vec{x}| \geq R\}$ is spacelike. Let $M_{2}$ denote this graph, let $g_{2}$ be the metric induced by the Minkowski metric on the graph of $f$, and let $K_{2}$ be the second fundamental form of the graph. Let $\left(M_{3}, g_{3}, K_{3}\right)$ be obtained by taking the union of
$$(M \backslash \mathscr{U}, g,-g) \equiv\left(M \backslash \mathscr{U}, g_{1},-g_{1}\right)$$
with $\left(M_{2}, g_{2}, K_{2}\right)$ and identifying points at the joint boundary $|\vec{x}|=R$. Then $\left(M_{3}, g_{3}, K_{3}\right)$ is a smooth general relativistic initial data satisfying the dominant energy condition which is exactly flat at large distances. By Conjecture 4.1 the data set $\left(M_{3}, g_{3}, K_{3}\right)$ arises from Minkowski space-time, in particular $M_{3}$ is spin. The result follows now from [9, 30]. \(\square\)

We also note the following result: ${ }^{1}$
Theorem 4.3 Assume that Conjecture 4.1 is true in a dimension $n \geq 3$. Let $(M, g)$, be an $n$-dimensional manifold with scalar curvature $R[g] \geq-n(n-1)$ with a metric which is smoothly conformally compactifiable and with spherical

\footnotetext{
${ }^{1}$ The hypotheses have been chosen for simplicity, the result holds under much more general asymptotic conditions, compare Remark 1.5.
}
conformal infinity. Suppose that in the coordinates of (2.3) the metric $g$ approaches the hyperbolic metric $\dot{g}$ as $O\left(r^{-n}\right)$, and assume that $R[g]+n(n-1)=$ $O\left(r^{-n-1}\right)$. Then the total energy-momentum vector of $(M, g)$ cannot be timelike past-pointing.

Proof: Since every three dimensional manifold is spin, this is the usual AH Positive Energy Theorem [9, 30] when $n=3$.

Suppose, thus, that $n \geq 4$ and that the claim is wrong. By hypothesis the metric is conformally smooth, so that the asymptotic conditions of [8] are met. Using a deformation of the metric as in [8, Corollary 1.4] (one can alternatively invoke [6, Theorem 1.2] if $n \geq 8$ ), one obtains an AH metric $g_{1}$ with
$$R\left(g_{1}\right) \geq-n(n-1) \quad \text { and } \quad R\left(g_{1}\right) \not \equiv-n(n-1),$$
such that $g_{1}$ has negative mass aspect function. As explained in [2], one can now construct on $M$ a new metric $g_{2}$ which satisfies
$$R\left(g_{2}\right) \geq-n(n-1) \quad \text { and } \quad R\left(g_{2}\right) \not \equiv-n(n-1),$$
and which coincides with the hyperbolic metric $b$ in a neighborhood of the conformal boundary at infinity. This contradicts Theorem 4.2. \(\square\)

We are ready now to pass to the
Proof of Theorem 1.3: Suppose that there exists an AH manifold $\left(M_{1}, g_{1}\right)$ with spacelike or null past-pointing energy-momentum vector $\mathbf{m}^{1}$ with respect to an asymptotic structure $\phi_{1}$. We can make a deformation of the metric as in [6, Proposition 6.2] to achieve that $|g-\stackrel{\circ}{g}|_{\dot{g}}$ is $O\left(r^{-n}\right)$ in the coordinates of (2.3) while maintaining the space-like or past-directed causal character of the energy-momentum vector.

Changing $\phi_{1}$ (i.e., applying a conformal transformation at the conformal boundary) if necessary, we can choose the asymptotic structure $\phi_{1}$ so that
$$\mathbf{m}^{1} \equiv\left(m_{0}^{1}, \vec{m}^{1}\right) \in \mathbb{R} \times \mathbb{R}^{n}$$
satisfies
$$m_{0}^{1}<0 .$$
This follows from the fact that the connected component of the identity of the Lorentz group acts transitively on the set of spacelike vectors with given length.

Choose $p_{1} \in \mathbb{S}^{n-1}$ to be $-\vec{m}^{1}$.
Let $\left(M_{1}, g_{1, \varepsilon}, \phi_{1}\right)$ be a family as in Section 3, constructed by a gluing procedure which, in half-plane-model coordinates, replaces $g_{1}$ by the hyperbolic metric in a half-ball of radius $\varepsilon$ centred at $p_{1}$. Set
$$\left(M_{2}, g_{2, \varepsilon}, \phi_{2}\right):=\left(M_{1}, g_{1, \varepsilon}, \phi_{1}\right) .$$

Let $\left(M, g_{\varepsilon}, \phi\right)$, with energy-momentum $\mathbf{m}^{\varepsilon}$, be constructed as in Section 3 by gluing together $\left(M_{1}, g_{1, \varepsilon}, \phi_{1}\right)$ and $\left(M_{2}, g_{2, \varepsilon}, \phi_{2}\right)$.

The maps $\Lambda_{\varepsilon}^{1}$ of Section 3 act on $\mathbf{m}_{\varepsilon}^{1}$ as boosts in the direction of $\vec{m}^{1}$. Let $R_{\varepsilon}$ be a rotation of the sphere by $\pi$ around some arbitrarily chosen axis passing through the equator, thus $R_{\varepsilon}$ maps the north pole to the south pole. If we align
the coordinate system so that $\vec{m}^{1}$ points in the direction of the first coordinate axis, we can write
$$\Lambda_{\varepsilon}^{1}=\left(\begin{array}{cccc}
\gamma_{\varepsilon} & -\gamma_{\varepsilon} v_{\varepsilon} & 0 & 0 \\
-\gamma_{\varepsilon} v_{\varepsilon} & \gamma_{\varepsilon} & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & \mathrm{Id}
\end{array}\right), \quad R_{\varepsilon}=\left(\begin{array}{cccc}
1 & 0 & 0 & 0 \\
0 & -1 & 0 & 0 \\
0 & 0 & -1 & 0 \\
0 & 0 & 0 & \mathrm{Id}
\end{array}\right),$$
with $v_{\varepsilon} \in(0,1), \gamma_{\varepsilon}:=\left(1-v_{\varepsilon}^{2}\right)^{-1 / 2}$, and Id being the $(n-2) \times(n-2)$ identity matrix.

Let us choose $\Lambda_{\varepsilon}^{2}$ to be $R_{\varepsilon} \Lambda_{\varepsilon}^{1}$. Then the space-part of $\Lambda_{\varepsilon}^{2} \mathbf{m}^{2}=\Lambda_{\varepsilon}^{2} \mathbf{m}^{1}$ cancels out that of $\Lambda_{\varepsilon}^{1} \mathbf{m}^{1}$ :
$$\Lambda_{\varepsilon}^{1} \mathbf{m}^{1}+\Lambda_{\varepsilon}^{2} \mathbf{m}^{1}=\Lambda_{\varepsilon}^{1} \mathbf{m}^{1}+R_{\varepsilon} \Lambda_{\varepsilon}^{1} \mathbf{m}^{1}=2 \gamma_{\varepsilon}(\underbrace{m_{0}^{1}}_{<0}-v_{\varepsilon} \underbrace{m_{1}^{1}}_{>\left|m_{0}^{1}\right|>0}, \overrightarrow{0}) .$$
Hence,
$$\begin{aligned}
\mathbf{m}^{\varepsilon}= & \Lambda_{\varepsilon}^{1} \mathbf{m}^{1, \varepsilon}+\Lambda_{\varepsilon}^{2} \mathbf{m}^{2, \varepsilon}=\Lambda_{\varepsilon}^{1} \mathbf{m}^{1, \varepsilon}+R_{\varepsilon} \Lambda_{\varepsilon}^{1} \mathbf{m}^{1, \varepsilon} \\
= & \left(\Lambda_{\varepsilon}^{1}+R_{\varepsilon} \Lambda_{\varepsilon}^{1}\right)\left(\mathbf{m}^{1}+\mathbf{m}^{1, \varepsilon}-\mathbf{m}^{1}\right) \\
= & \gamma_{\varepsilon}(2(\underbrace{m_{0}^{1}-v_{\varepsilon} m_{1}^{1}}_{<0}, \overrightarrow{0})+ \\
& \gamma_{\varepsilon}^{-1} \Lambda_{\varepsilon}^{1}(\underbrace{\left(1+\left(\Lambda_{\varepsilon}^{1}\right)^{-1} R_{\varepsilon} \Lambda_{\varepsilon}^{1}\right)\left(\mathbf{m}^{1, \varepsilon}-\mathbf{m}^{1}\right)}_{=:(*)})) .
\end{aligned}$$
Keeping in mind that $\gamma_{\varepsilon}^{-1} \Lambda_{\varepsilon}^{1}$ has bounded entries, we wish to show that (*) goes to zero as $\varepsilon$ goes to zero. For this, we need to analyse the matrix $\left(\Lambda_{\varepsilon}^{1}\right)^{-1} R_{\varepsilon} \Lambda_{\varepsilon}^{1}$. Since $\left(\Lambda_{\varepsilon}^{1}\right)^{-1}$ coincides with $\Lambda_{\varepsilon}^{1}$ with $v_{\varepsilon}$ changed to its negative, we find
$$\left(\Lambda_{\varepsilon}^{1}\right)^{-1} R_{\varepsilon} \Lambda_{\varepsilon}^{1}=\left(\begin{array}{cccc}
\gamma_{\varepsilon}^{2}\left(1+v_{\varepsilon}^{2}\right) & -2 \gamma_{\varepsilon}^{2} v_{\varepsilon} & 0 & 0 \\
2 \gamma_{\varepsilon}^{2} v_{\varepsilon} & -\gamma_{\varepsilon}^{2}\left(1+v_{\varepsilon}^{2}\right) & 0 & 0 \\
0 & 0 & -1 & 0 \\
0 & 0 & 0 & \mathrm{Id}
\end{array}\right) .$$
If we view the sphere $\mathbb{S}^{n-1}$ as embedded in $\mathbb{R}^{n}$ with Euclidean coordinates $\left(x^{i}, x^{n}\right)$, with $-\vec{m}^{1}$ the north pole and $\vec{m}^{1}$ the south pole, then the Lorentz transformation $\Lambda_{\varepsilon}^{1}$ of (4.8) corresponds to the conformal transformation (cf., e.g., [8, Section 3.4])
$$\mathbb{S}^{n-1} \ni\left(x^{1}, x^{i}\right) \mapsto \frac{1}{\gamma_{\varepsilon}\left(1-v_{\varepsilon} x^{1}\right)}\left(\gamma_{\varepsilon}\left(x^{1}-v_{\varepsilon}\right), x^{i}\right) \in \mathbb{S}^{n-1} .$$
If we denote by $\theta$ the angle off the axis passing through the south pole and the north pole, then $v_{\varepsilon}$ has to be chosen so that $\varepsilon$ is mapped to $\pi / 2$. Equivalently, if $n^{i}$ is a unit vector in Euclidean $\mathbb{R}^{n-1}$, Equation (4.12) should give
$$\mathbb{S}^{n-1} \ni\left(\cos (\varepsilon), \sin (\varepsilon) n^{i}\right) \mapsto \frac{1}{\gamma_{\varepsilon}\left(1-v_{\varepsilon} \cos (\varepsilon)\right)}\left(0, \sin (\varepsilon) n^{i}\right) \in \mathbb{S}^{n-1},$$
i.e., $v_{\varepsilon}=\cos (\varepsilon)$, hence
$$\gamma_{\varepsilon}=\frac{1}{\sin (\varepsilon)}=\varepsilon^{-1}(1+O(\varepsilon))$$
for small $\varepsilon$. It follows that the term $(*)$ in (4.10) can be estimated as
$$\begin{aligned}
|(*)| & \equiv\left|\left(1+\left(\Lambda_{\varepsilon}^{1}\right)^{-1} R_{\varepsilon} \Lambda_{\varepsilon}^{1}\right)\left(\mathbf{m}^{1, \varepsilon}-\mathbf{m}^{1}\right)\right| \\
& \leq C\left(1+\varepsilon^{-2}\right)\left|\mathbf{m}^{1, \varepsilon}-\mathbf{m}^{1}\right| \leq C^{2} \varepsilon^{\frac{n}{2}-2},
\end{aligned}$$
where we used (3.2). So $(*)$ will tend to zero if $n \geq 5$. The case $n=4$ follows in the same way using (3.3). This implies that for $\varepsilon$ small enough the energy-momentum vector $\mathbf{m}^{\varepsilon}$ of $\left(M, g_{\varepsilon}, \phi\right)$ is timelike past pointing. One can perturb the metric slightly if needed (compare Remark 1.5) so that the asymptotic conditions of Theorem 4.3 are satisfied, with the energy-momentum remaining timelike past pointing, obtaining a contradiction with that theorem. We conclude that m is causal future-pointing, or vanishes. \(\square\)

Acknowledgements: We thank Michael Eichmair for useful discussions related to Theorem 1.1, and Greg Galloway for many useful comments. PTC was supported in part by the Austrian Science Fund (FWF) under project P29517-N27 and by the Polish National Center of Science (NCN) 2016/21/B/ST1/00940. ED was supported by the grant ANR-23-CE40-0010 (project EINSTEIN-PPF) and the grant ANR-24-CE40-0702 (project OrbiScar) of the French National Research Agency ANR.

\section*{References}
\begin{itemize}
\item[] [1] L.F. Abbott and S. Deser, Stability of gravity with a cosmological constant, Nucl. Phys. B195 (1982), 76-96.
\item[] [2] L. Andersson, M. Cai, and G.J. Galloway, Rigidity and positivity of mass for asymptotically hyperbolic manifolds, Ann. H. Poincaré 9 (2008), 1-33, arXiv:math.dg/0703259. MR MR2389888 (2009e:53054)
\item[] [3] L. Andersson, P.T. Chruściel, and H. Friedrich, On the regularity of solutions to the Yamabe equation and the existence of smooth hyperboloidal initial data for Einsteins field equations, Commun. Math. Phys. 149 (1992), 587-612. MR MR1186044 (93i:53040)
\item[] [4] L. Andersson and M. Dahl, Scalar curvature rigidity for asymptotically locally hyperbolic manifolds, Annals of Global Anal. and Geom. 16 (1998), 1-27, arXiv:dg-ga/9707017.
\item[] [5] H. Barzegar, P.T. Chruściel, and M. Hörzinger, Energy in higher-dimensional spacetimes, Phys. Rev. D 96 (2017), 124002, 25 pp., arXiv:1708.03122 [gr-qc].
\item[] [6] P.T. Chruściel and E. Delay, Gluing constructions for asymptotically hyperbolic manifolds with constant scalar curvature, Commun. Anal. Geom. 17 (2009), 343-381, arXiv:0711.1557[gr-qc]. MR 2520913 (2011a:53052)
\item[] [7] \_\_\_\_, Exotic hyperbolic gluings, Jour. Diff. Geom. 108 (2018), 243-293, arXiv:1511.07858 [gr-qc].
\end{itemize}
[8] P.T. Chruściel, G.J. Galloway, L. Nguyen, and T.-T. Paetz, On the massaspect function and positive energy theorems for asymptotically hyperbolic manifolds, Class. Quantum Grav. 35 (2018), 115015, arXiv:1801.03442 [grqc].
[9] P.T. Chruściel and M. Herzlich, The mass of asymptotically hyperbolic Riemannian manifolds, Pacific Jour. Math. 212 (2003), 231-264, arXiv:math/0110035 [math.DG]. MR MR2038048 (2005d:53052)
[10] P.T. Chruściel, J. Jezierski, and S. Lęski, The Trautman-Bondi mass of hyperboloidal initial data sets, Adv. Theor. Math. Phys. 8 (2004), 83-139, arXiv:gr-qc/0307109. MR MR2086675 (2005j:83027)
[11] P.T. Chruściel and G. Nagy, The Hamiltonian mass of asymptotically anti - de Sitter spacetimes, Class. Quantum Grav. 18 (2001), L61-L68, arXiv:hep-th/0011270.
[12] \_\_\_\_, The mass of spacelike hypersurfaces in asymptotically anti - de Sitter spacetimes, Adv. Theor. Math. Phys. 5 (2001), 697-754, arXiv:gr-qc/0110014.
[13] P.T. Chruściel and W. Simon, Towards the classification of static vacuum spacetimes with negative cosmological constant, Jour. Math. Phys. 42 (2001), 1779-1817, arXiv:gr-qc/0004032.
[14] M. Dahl and A. Sakovich, A density theorem for asymptotically hyperbolic initial data satisfying the dominant energy condition, Pure Appl. Math. Q. 17 (2015), 1669-1710, arXiv:1502.07487 [math.DG]. MR 4376092
[15] M. Eichmair, The Jang equation reduction of the spacetime positive energy theorem in dimensions less than eight, Commun. Math. Phys. 319 (2013), 575-593, arXiv:1206.2553 [math.dg]. MR 3040369
[16] M. Eichmair, L.-H. Huang, D.A. Lee, and R. Schoen, The spacetime positive mass theorem in dimensions less than eight, Jour. Eur. Math. Soc. (JEMS) 18 (2016), 83-121, arXiv:1110.2087 [math.DG]. MR 3438380
[17] G.W. Gibbons, S.W. Hawking, G.T. Horowitz, and M.J. Perry, Positive mass theorem for black holes, Commun. Math. Phys. 88 (1983), 295-308.
[18] M. Herzlich, Computing asymptotic invariants with the Ricci tensor on asymptotically flat and asymptotically hyperbolic manifolds, Ann. Henri Poincaré 17 (2016), 3605-3617, arXiv:1503.00508 [math.DG]. MR 3568027
[19] L.-H. Huang, H.C. Jang, and D. Martin, Mass rigidity for hyperbolic manifolds, Commun. Math. Phys. 376 (2019), 2329-2349, arXiv:1904.12010 [math.DG].
[20] L.-H. Huang and D.A. Lee, Equality in the spacetime positive mass theorem, Commun. Math. Phys. 376 (2020), 2379-2407, arXiv:1706.03732 [math.DG]. MR 4104553
[21] J. Isenberg, J.M. Lee, and I. Stavrov Allen, Asymptotic gluing of asymptotically hyperbolic solutions to the Einstein constraint equations, Ann. Henri Poincaré 11 (2010), 881-927, arXiv:0910.1875 [math-dg]. MR 2736526 (2012h:58037)
[22] D.A. Lee, Geometric relativity, Graduate Studies in Mathematics, vol. 201, AMS, Providence, RI, 2017.
[23] J. Lohkamp, The Higher Dimensional Positive Mass Theorem II, (2016), arXiv:1612.07505 [math.DG].
[24] D. Maerten, Positive energy-momentum theorem in asymptotically anti-de Sitter spacetimes, Ann. H.Poincaré 7 (2006), 975-1011, arXiv:math.DG/0506061. MR MR2254757 (2007d:83016)
[25] M. Min-Oo, Scalar curvature rigidity of asymptotically hyperbolic spin manifolds, Math. Ann. 285 (1989), 527-539.
[26] R. Schoen and S.-T. Yau, Complete manifolds with nonnegative scalar curvature and the positive action conjecture in general relativity, Proc. Nat. AcadŚci. U.S.A. 76 (1979), 1024-1025. MR MR524327 (80k:58034)
[27] \_\_\_\_, On the proof of the positive mass conjecture in general relativity, Commun. Math. Phys. 65 (1979), 45-76. MR MR526976 (80j:83024)
[28] \_\_\_\_, Proof of the positive mass theorem. II, Commun. Math. Phys. 79 (1981), 231-260. MR 612249
[29] \_\_\_\_, Positive scalar curvature and minimal hypersurface singularities, Surveys in Diff. Geom. 24 (1) (2017), arXiv:1704.05490 [math.DG].
[30] X. Wang, Mass for asymptotically hyperbolic manifolds, Jour. Diff. Geom. 57 (2001), 273-299. MR MR1879228 (2003c:53044)
[31] X. Wang, On the uniqueness of the AdS spacetime, Acta Math. Sin. (Engl. Ser.) 21 (2005), 917-922 (en), arXiv:math/0210165. MR 2156971
