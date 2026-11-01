---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Conformal Dirichlet-Neumann Maps and Poincaré-Einstein Manifolds]

---
source_file: Conformal_Dirichlet-Neumann_Maps_and_Poincaré-Einstein_Manifolds_6f434516318a.pdf
converter: mathpix
format: mmd
---

\title{
Conformal Dirichlet-Neumann Maps and Poincaré-Einstein Manifolds*
}

\author{
A. Rod GOVER \\ Department of Mathematics, The University of Auckland, Private Bag 92019, Auckland 1, New Zealand \\ E-mail: gover@math.auckland.ac.nz \\ URL: http://www.math.auckland.ac.nz/~gover/
}

Received October 07, 2007; Published online October 21, 2007
Original article is available at http://www.emis.de/journals/SIGMA/2007/100/

\begin{abstract}
A conformal description of Poincaré-Einstein manifolds is developed: these structures are seen to be a special case of a natural weakening of the Einstein condition termed an almost Einstein structure. This is used for two purposes: to shed light on the relationship between the scattering construction of Graham-Zworski and the higher order conformal Dirichlet-Neumann maps of Branson and the author; to sketch a new construction of non-local (Dirichlet-to-Neumann type) conformal operators between tensor bundles.
\end{abstract}

Key words: conformal differential geometry; Dirichlet-to-Neumann maps
2000 Mathematics Subject Classification: 58J40; 53A30; 58J32

\section*{1 Introduction}

A Poincaré-Einstein manifold is a compact manifold with boundary equipped with a negative scalar curvature Einstein metric that is "conformally compact"; that is, it has a certain conformal scale singularity at the boundary. The model that this generalises is the dimension $n+1$ hyperbolic ball with the sphere $\mathbb{S}^{n}$ as the conformal boundary at infinity. As in the model case, the Poincaré-Einstein boundary has a conformal structure and a central theme in the study of these is to relate this to the Riemannian geometry of the interior. Much of the motivation has come from physics, in particular in connection with the so-called AdS/CFT (Anti-de Sitter/Conformal Field Theory) correspondence suggested by Maldacena [41, 49]. A number of purely geometric questions arise and these have generated significant mathematical interest, see for example [1, 2, 14].

In the seminal work [34] Graham and Zworski developed the scattering theory for (asymptotically) Poincaré-Einstein manifolds and its use for describing conformal objects on the boundary. This exploited the available picture for the scattering theory of infinite volume hyperbolic quotients (see e.g. [45] and references therein), and for asymptotically hyperbolic manifolds (e.g. [39]) as well as the results for the spectrum of the Laplacian on these due to Mazzeo and Mazzeo-Melrose [42, 43, 44].

A focus of [34] was to extract and study, via the scattering machinery, the conformal Laplacian type operators of [32] as well as Branson's $Q$-curvature [5]. However the scattering operator they construct is an essentially global object and, as they point out, may be viewed as a generalised Dirichlet-to-Neumann map. This picture of the operator is especially relevant for certain real values of the spectral parameter and this is a point we wish to underscore here. In particular one aim here is to shed light on the relationship between the Graham-Zworski construction

\footnotetext{
${ }^{\star}$ This paper is a contribution to the Proceedings of the 2007 Midwest Geometry Conference in honor of Thomas P. Branson. The full collection is available at http://www.emis.de/journals/SIGMA/MGC2007.html
}
and the conformal Dirichlet-to-Neumann maps constructed by Branson with the author [6]. In the spirit of the standard Dirichlet-to-Neumann construction the latter are based around elliptic source problems and target problems; the interior operators are conformal Laplacian type operators of the form $\Delta^{k}$ + lower order terms, developed with Eastwood [20], and the the boundary operators are derived from the conformal tractor calculus of hypersurface type submanifolds. Both the scattering operator and the Dirichlet-to-Neumann maps of [6] are conformally invariant. In the homogeneous setting this translates to the fact that they intertwine principal series representations and so, by naturality and the uniqueness of the intertwinors concerned [8], it would seem that in this setting they should agree. Here we make steps toward an explicit matching of the constructions. As background, the basic conformal machinery is revised in the next section and then, in Section 3, we outline the construction of the conformal Dirichlet-to-Neumann operators from [6].

Let $M$ be a compact smooth manifold with boundary $\Sigma=\partial M$. A metric $g_{+}$on the interior $M_{+}$of $M$ is said to be conformally compact if it extends (with some specified regularity) to $M$ by $g=x^{2} g_{+}$where $g$ is non-degenerate up to the boundary, and $x$ is a non-negative defining function for the boundary (i.e. $\Sigma$ is the zero set for $x$, and $d x$ is non-vanishing on $\Sigma$ ). In this situation the metric $g_{+}$is complete and the restriction of $g$ to $T \Sigma$ in $\left.T M\right|_{\Sigma}$ determines a conformal structure that is independent of the choice of defining function $x$; the latter is termed the conformal infinity of $M_{+}$. If the defining function is chosen so that $|d x|=1$ (with respect to $g$ ) along $\Sigma$ then the sectional curvatures tend to -1 at infinity [42] and the structure is said to be asymptotically hyperbolic. The manifold is said to be a Poincaré-Einstein structure if, in addition, the interior metric $g_{+}$is Einstein, with $\operatorname{Ric}\left(g_{+}\right)=-n g_{+}$. For simplicity of presentation, we shall treat all structures as smooth. It is straightforward to adapt the results to the case of limited regularity. We shall also confine our discussion to metrics and conformal structures of positive definite signature.

Since the "boundary singularity" of the metric $g_{+}$is conformal in nature, it is natural to explore the meaning of the Poincaré-Einstein structure in terms of the conformal geometry of $M$. An elegant picture emerges, and this is the subject of Section 4. The equation controlling whether or not a metric is conformally Einstein is a second order overdetermined partial differential equation, see expression (8). A solution of this determines an Einstein metric only if it is non-vanishing. In fact any solution is non-vanishing on an open dense set [23] and so we say that, when equipped with such a solution, a conformal, or (pseudo-)Riemannian, manifold is almost Einstein [21]. This notion is given a geometric interpretation via the conformal tractor calculus. The conformal tractor connection [48] is a canonical and conformally invariant vector bundle connection; it is equivalent [10] to the conformal Cartan connection of [9]. From the development of the tractor connection as a prolonged differential system in [4] we see that a manifold is almost Einstein if and only if there is a parallel section of the standard tractor bundle. (A link between the Cartan connection and Einstein metrics has been known for some time [46]). We establish in Section 4.2 that a Poincaré-Einstein structure is simply a special case of such a structure where the solution $x$ to (8) is a defining function for boundary, in fact a special defining function in the sense of Graham-Lee [33, 30]. We shall show that along the boundary the parallel tractor recovers the normal tractor from [4] which controls the relationship between the boundary and interior conformal geometry; further details will follow in [25]. From this we recover the (well known) total umbillicity of the boundary as an immediate consequence. Finally in section 4.3 we describe the flat model of this picture as a hyperbolic hemisphere with the equator as boundary. In this setting we see, for example, that $\mathrm{SO}(n+1,1)$, which acts transitively on the interior of the homogeneous model, arises as an isotropy subgroup of the conformal group acting on the sphere; it is exactly the subgroup fixing the parallel tractor.

In Section 5 we discuss the specialisation to Poincaré-Einstein manifolds of the Dirichlet-to-Neumann machinery. Except in the simplest case (and there following Guillarmou and Guil-
lopé [37]), the picture is incomplete and so this should be viewed as an exploration and development of an emerging picture. We see in Section 5.1 that the Laplacian operator $(\Delta-s(n-s))$, which controls the scattering construction in [34], arises from a conformal operator on the almost Einstein structure. On the other hand on the Poincaré-Einstein interior we find that the GJMS conformal powers of the Laplacian of [32] are compositions of such Laplacians (see expression (15)). This suggests a relationship between the scattering construction and Dirichlet-to-Neumann operators along the lines of [6], but where the interior operator is a GJMS operator $P_{k}$. The main link is developed in Section 5.3, we see in Proposition 7 that on a Poincaré-Einstein space, the solution space for these is a direct sum of Laplacian (generalised) eigenspaces.

In Section 6 we sketch some new ideas for a construction of Dirichlet-to-Neumann type operators between tensor bundles. This is partly inspired by related ideas involving the "curved translation principle" for the construction of invariant differential operators, that arose in the pioneering article [18] of Eastwood and Rice. This idea has been significantly developed and adapted over the years [17, 13, 29, 47].

Finally it should be pointed out that many of the ideas and contructions developed below generalise, with some weakening, to the case of conformally compact manifolds which are only asymptotically Einstein, or with further weakening to asymptotically hyperbolic structures. Here we have specialised to Poincaré-Einstein structures since in this case the picture seems especially appealing.

\section*{2 Tractor calculus and hypersurfaces}

Let $M$ be a smooth manifold. To simplify the discussion we shall assume throughout that $d \geq 4$ (with minor modifications the treatment can extended to include $d=3$ ). It will be convenient to use some standard structures from conformal geometry, further details and background may be found in [11, 24]. Recall that a (Riemannian) conformal structure on $M$ is a smooth ray subbundle $\mathcal{Q} \subset S^{2} T^{*} M$ whose fibre over $p$ consists of conformally related positive definite metrics at the point $p$. Sections of $\mathcal{Q}$ are metrics $g$ on $M$. So we may equivalently view the conformal structure as the equivalence class $[g]$ of these conformally related metrics. The principal bundle $\pi: \mathcal{Q} \rightarrow M$ has structure group $\mathbb{R}_{+}$, and so each representation $\mathbb{R}_{+} \ni t \mapsto$ $t^{-w / 2} \in \operatorname{End}(\mathbb{R})$ induces a natural line bundle on $(M,[g])$ that we term the conformal density bundle $\mathcal{E}[w]$. In general each vector bundle and its space of smooth sections will be denoted in the same way.

We write $\boldsymbol{g}$ for the conformal metric, that is the tautological section of $S^{2} T^{*} M[2]:=S^{2} T^{*} M \otimes$ $\mathcal{E}[2]$ determined by the conformal structure. This will be henceforth used to identify $T M$ with $T^{*} M[2]$. For example, with these conventions the Laplacian $\Delta$ is given by $\Delta=-\boldsymbol{g}^{a b} \nabla_{a} \nabla_{b}=$ $-\nabla^{b} \nabla_{b}$ where ∇ (or sometimes we will write $\nabla^{g}$ ) is the Levi-Civita connection for some choice of metric $g$ from the conformal class. Note $\mathcal{E}[w]$ is trivialised by a choice of metric, and we write ∇ (or again sometimes $\nabla^{g}$ ) for the connection corresponding to this trivialisation. It follows immediately that the (coupled) connection $\nabla_{a}$ preserves the conformal metric. The conformal metric $\boldsymbol{g}$ and its inverse will henceforth be the default object used used to contract indices on tensors even when we have fixed a metric from the conformal class.

The Riemann curvature tensor $R_{a b}{ }^{c}{ }_{d}$ is given by
$$\left(\nabla_{a} \nabla_{b}-\nabla_{b} \nabla_{a}\right) V^{c}=R_{a b}{ }^{c}{ }_{d} V^{d}, \quad \text { where } \quad V^{c} \in \mathcal{E}^{c} .$$
This can be decomposed into the totally trace-free Weyl curvature $W_{\text {abcd }}$ and the symmetric Schouten tensor $P_{a b}$ according to
$$R_{a b c d}=W_{a b c d}+2 g_{c[a} P_{b] d}+2 g_{d[b} P_{a] c} .$$

Thus $P_{a b}$ is a trace modification of the Ricci tensor $\operatorname{Ric}_{a b}=R_{c a}{ }^{c}{ }_{b}$. We write $J$ for the conformal metric trace of $P_{a b}$.

For a given choice of metric $g$, the tractor bundle $\mathcal{T}$, or using an obvious abstract index notation $\mathcal{T}^{A}$, may be identified with a direct sum
$$\mathcal{T}^{A} \stackrel{g}{=} \mathcal{E}[1] \oplus \mathcal{E}_{a}[1] \oplus \mathcal{E}[-1] .$$
Thus a section $U$ of $\mathcal{T}$ may be identified with a triple $\left(\sigma, \mu_{a}, \rho\right)$; we will write simply $U^{A}=$ $\left(\sigma, \mu_{a}, \rho\right)$. The conformal transformation of these components is described in, for example, [4] and [22]. From this, for example, one sees that the map $\mathcal{T}^{A} \rightarrow \mathcal{E}[1]$ is conformally invariant and may be regarded as a preferred element $X_{A} \in \Gamma \mathcal{T}_{A}[1]$ so that, with $U^{A}$ again as above, we have $\sigma=U^{A} X_{A}$. It also describes the invariant injection $\mathcal{E}[-1] \rightarrow \mathcal{T}_{A}$ according to $\rho \mapsto \rho X_{A}$. In computations, it is often useful to introduce the remaining 'projectors' from $\mathcal{T}^{A}$ to the components $\mathcal{E}_{a}$ [1] and $\mathcal{E}[-1]$ which are determined by a choice of scale. They are denoted by $Z_{A a} \in \mathcal{E}_{A a}[1]$ and $Y_{A} \in \mathcal{T}_{A}[-1]$, where $\mathcal{E}_{A a}[w]=\mathcal{T}_{A} \otimes \mathcal{E}_{a} \otimes \mathcal{E}[w]$, etcetera.

We describe any tensor product (or symmetric tensor product etcetera) of the tractor bundle and its dual as tractor bundles. If such a bundle is tensored with some bundle of densities $\mathcal{E}[w]$ then we shall describe the result as a weighted tractor bundle. In many cases we wish to indicate a weighted tractor bundle without being specific about the indices of the bundle or any symmetry these may possess. Thus we write $\mathcal{T}^{*}[w]$ to mean a weighted tractor bundle which is the tensor product of $\mathcal{E}[w]$ with any tractor bundle. Finally, repeated tractor indices indicate a contraction, just as for tensor indices.

The bundle $\mathcal{T}^{A}$ carries an invariant signature ( $d+1,1$ ) tractor metric $h_{A B}$, and a connection $\nabla_{a}$ which preserves this. For $U^{A}$ as above, this metric is given by
$$h_{A B} U^{A} U^{B}=2 \rho \sigma+\mu^{a} \mu_{a} .$$
As a point on notation, we may also write $h(U, U)$ for the expression in the display. The tractor metric will be used to raise and lower indices without further mention. In terms of the metric $g$ from the conformal class, the connection is given explicitly by the following formula for $\nabla_{a} U^{B}$ :
$$\nabla_{a}\left(\begin{array}{c}
\sigma \\
\mu^{b} \\
\rho
\end{array}\right)=\left(\begin{array}{c}
\nabla_{a} \sigma-\mu_{a} \\
\nabla_{a} \mu^{b}+\delta_{a}^{b} \rho+P_{a}^{b} \sigma \\
\nabla_{a} \rho-P_{a c} \mu^{c}
\end{array}\right) .$$
Of course this may be extended to a connection on any tractor bundle in the obvious way. The use of the same symbol ∇ as for the Levi-Civita connection is intentional. More generally, we shall use ∇ to mean the coupled Levi-Civita-tractor connection: this enables us, for example, to apply ∇ to weighted tractor bundles or tensor-tractor. Although in this case it is not conformally invariant it enables us to, for example, compute the covariant derivative of the tractor projectors $X, Y$ and $Z$.

As discussed in [4], there is an invariant second order operator between weighted tractor bundles due to T.Y. Thomas,
$$D_{A}: \mathcal{T}^{*}[w] \rightarrow \mathcal{T}^{*}[w-1],$$
by
$$D_{A} V:=(d+2 w-2) w Y_{A} V+(d+2 w-2) Z^{a} \nabla_{a} V+X^{A}(\Delta-w \mathrm{~J}) V,$$
where J is the conformal metric trace of the Schouten tensor, i.e. $\mathrm{J}=\boldsymbol{g}^{a b} P_{a b}$. For an invariant construction of this see [20]. Notice that, from the conformal invariance of $D$, it follows that the tractor twisting of the Yamabe operator $\square:=\Delta-(1-n / 2) \mathrm{J}$ is conformally invariant as an operator $\square: \mathcal{T}^{*}[1-n / 2] \rightarrow \mathcal{T}^{*}[-1-n / 2]$. Thus as observed in [20] one obtains conformal Laplacian operators as follows.

Proposition 1. The operators
$$\square_{k}: \mathcal{E}^{*}\left[\frac{k-d}{2}\right] \rightarrow \mathcal{E}^{*}\left[-\frac{k+d}{2}\right], \quad \text { where } k \geq 2 \text { is even },$$
defined by
$$\square_{k}:=D^{A} \cdots D^{B} \square \underbrace{D_{B} \cdots D_{A}}_{(k-2) / 2}$$
are conformally invariant differential operators. These take the form (up to a non-zero constant scale factor)
$$\Delta^{k / 2}+\text { lower order terms, }$$
except when $d$ is even and $d \leq k$.
The facts concerning the leading term follow easily by calculating directly from the definition, or there is a simple argument essentially avoiding computation in [20]. Note that, via (3), this proposition gives an explicit formula for these operators.

\subsection*{2.1 Conformal hypersurfaces}

Let us first recall some facts concerning a general hypersurface $\Sigma$ in a conformal manifold $\left(M^{d},[g]\right)$. By restriction of the ambient conformal structure, a conformal structure is induced on $\Sigma$. We write $\left(\Sigma^{n},\left[g_{\Sigma}\right]\right)(n+1=d)$ for this and shall refer to it as the intrinsic conformal structure of $\Sigma$. Note that the intrinsic conformal density bundles may be identified in an obvious way with the restriction of the ambient bundles carrying the same weight. We shall write $\mathcal{E}^{\Sigma}[w]=\left.\mathcal{E}[w]\right|_{\Sigma}$.

Since $d \geq 4$ we have $n \geq 3$ and so the manifold $\Sigma$ has its own intrinsic tractor bundles, connections and so forth. We shall denote the intrinsic tractor bundle of $\Sigma$ by $\mathcal{T}_{\Sigma}$. The relationship between this and $\left.\mathcal{T}\right|_{\Sigma}$ can be described in terms of a section of $\left.\mathcal{T}\right|_{\Sigma}$ that we term the normal tractor. Let $n_{a} \in \mathcal{E}_{a}[1]$ be a conormal field on $\Sigma$ such that (along $\Sigma$ ) we have $|n|_{\boldsymbol{g}}^{2}:=\boldsymbol{g}^{a b} n_{a} n_{b}=1$. Note that this is conformally invariant since $\boldsymbol{g}^{-1}$ has conformal weight -2. Now in the scale $g$ (from $[g]$ ) the mean curvature of $\Sigma$ is given by
$$H^{g}=\frac{1}{d-1}\left(\nabla_{a} n^{a}-n^{a} n^{b} \nabla_{a} n_{b}\right),$$
as a conformal -1-density. This is independent of how $n_{a}$ is extended off $\Sigma$. Now under a conformal rescaling, $g \mapsto \widehat{g}=e^{2 \omega} g, H$ transforms to $\widehat{H}=H+n^{a} \nabla_{a} \omega$. This is exactly the transformation required so that
$$N:=\left(\begin{array}{c}
0 \\
n_{a} \\
-H
\end{array}\right),$$
is a conformally invariant section $N$ of $\left.\mathcal{T}\right|_{\Sigma}$. Observe that, from (1), $h(N, N)=1$ along $\Sigma$. Obviously $N$ is independent of any choices in the extension of $n_{a}$ off $\Sigma$. This is the normal tractor of [4] and may be viewed as a tractor bundle analogue of the unit co-normal field from the theory of Riemannian hypersurfaces.

Recall that a point $p$ in a hypersurface is an umbillic point if the second fundamental form is trace free (with respect to the first fundamental form) at $p$. This is a conformally invariant condition and the hypersurface is totally umbillic if this holds at all points. Differentiating $N$ tangentially along $\Sigma$ using the tractor connection, we obtain the following result directly from (2).

Proposition 2. If the normal tractor $N$ is constant along a hypersurface $\Sigma$ then the hypersurface $\Sigma$ is totally umbillic.

In fact constancy of $N$ along a hypersurface is equivalent to total umbillicity. This is (Proposition 2.9) from [4].

It is straightforward to verify that the intrinsic tractor bundle to $\Sigma$ may be identified with the conformally invariant subbundle $\mathcal{T}_{\Sigma}^{A}$ of $\left.\mathcal{T}^{A}\right|_{\Sigma}$ which is orthogonal to the normal tractor $N^{A}$ [6] (an observation which generalises, see [3]). Thus we have an invariant splitting
$$\left.\mathcal{T}^{A}\right|_{\Sigma}=\mathcal{T}_{\Sigma}^{A} \oplus \mathcal{N}^{A}$$
given by
$$v^{A} \mapsto\left(v^{A}-N^{A} N_{B} v^{B}\right)+N^{A} N_{B} v^{B} .$$
for $v^{A} \in \Gamma\left(\mathcal{T}^{A}\right)$. Of course this generalises easily to tensor products of these bundles, and we shall always view the intrinsic tractor bundles of $\Sigma$ in this way; that is, as subbundles of the restrictions to $\Sigma$ of ambient tractor bundles, the sections of which are completely orthogonal to $N^{A}$. As a result, we need only one type of tractor index.

We shall use the symbol $P_{\Sigma}$ to indicate the orthogonal projection from any ambient weighted tractor bundle, restricted to $\Sigma$, to the corresponding intrinsic-to- $\Sigma$ weighted tractor bundle. For example, $P_{\Sigma}\left(\left.\mathcal{T}^{A}\right|_{\Sigma}\right)=\mathcal{T}_{\Sigma}^{A}$. In fact we shall henceforth drop the explicit restriction to $\Sigma$ and regard this as implicit in the definition of $P_{\Sigma}$. Thus we shall write, for example, $P_{\Sigma}\left(\mathcal{T}_{A B}[w]\right)=$ $\mathcal{T}_{A B}^{\Sigma}[w]$; any section $f_{A B}$ of this bundle has the property that $f_{A B} N^{A}=0=f_{A B} N^{B}$. The intrinsic-to- $\Sigma$ tractor-D operator will be denoted $D_{A}^{\Sigma}$. We may similarly denote by $X_{A}^{\Sigma}$ the tautological tractor belonging to the intrinsic structure of $\Sigma$. But note that $P_{\Sigma}\left(X_{A}\right)=\left.X_{A}\right|_{\Sigma}$, and it follows from the definition of $X_{A}^{\Sigma}$ that in fact $X_{A}^{\Sigma}=\left.X_{A}\right|_{\Sigma}$. A useful consequence of these observations (and using the formula (2)) is that if $f \in \mathcal{T}_{\Sigma}^{*}[w]$, then, on $\Sigma$,
$$D_{\Sigma}^{A} X_{A} f=(n+2 w+2)(n+w) f=(d+2 w+1)(d+w-1) f .$$

\section*{3 The conformal Dirichlet-Neumann operators of [6]}

\subsection*{3.1 Boundary operators}

The Dirichlet-to-Neumann maps of [6] are based around a pair of boundary problems. The operators of Proposition 1 are to be used for the interior operator, compatible with these we need suitable boundary operators. The basic prototype is the conformally invariant Robin operator $\delta: \mathcal{E}[w] \rightarrow \mathcal{E}[w-1]$ given in a conformal scale $g$ by $\delta f=n^{a} \nabla_{a}^{g} f-w H^{g} f$ (e.g. [15]). In fact it is easily verified that this is strongly invariant; twisting by another connection does not destroy conformal invariance. In particular we may twist this with tractor bundles by using the coupled Levi-Civita-tractor connection in the formula for $\delta$ :
$$\delta: \mathcal{T}^{*}[w] \rightarrow \mathcal{T}^{*}[w-1]$$
is conformally invariant. In fact on $\mathcal{T}^{*}[w]$, and for $w \neq 1-d / 2$, we have
$$\delta=c \cdot N^{A} D_{A}$$
for a non-zero constant $c$.
Further candidates for conformal boundary operators can be proliferated using the machinery of the previous section, as follows.

Definition. For each positive integer $\ell$ there is a conformally invariant differential operator along $\Sigma, \delta_{\ell}$, which maps $\mathcal{T}^{*}[w]$ to $\mathcal{T}_{\Sigma}^{*}[w-\ell]$, given by $\delta_{1}=\delta$, and
$$\delta_{\ell} u=\left\{\begin{array}{l}
D_{\Sigma}^{B} \cdots D_{\Sigma}^{A} P_{\Sigma}(\underbrace{D_{A} \cdots D_{B}}_{\ell / 2} u) \text { for } 2 \leq \ell \text { even }, \\
D_{\Sigma}^{B} \cdots D_{\Sigma}^{A} P_{\Sigma}(\underbrace{D_{A} \cdots D_{B}}_{(\ell-1) / 2} u) \text { for } 3 \leq \ell \text { odd. }
\end{array}\right.$$

For their use in boundary problems one needs information about the order of the $\delta_{\ell}$ in directions transverse to $\Sigma$. Suppose that $p \in \Sigma$ and in a neighbourhood of a point $p, \Sigma$ is given by the vanishing of a defining function $x$. We say that a differential operator $B: \mathcal{F} \rightarrow \mathcal{G}$ has normal order $r_{N}$ at $p \in \Sigma$ if there exists a section $\phi$ of $\mathcal{F}$ such that $B\left(x^{r_{N}} \phi\right)(p) \neq 0$ but for any section $\phi^{\prime}$ of $\mathcal{F}, B\left(x^{r_{N}+1} \phi^{\prime}\right)(p)=0$. For our current purposes we only really need the $\delta_{\ell}$ as follows.

Proposition 3. Let $k$ be a positive even integer. On a hypersurface $\Sigma$ in a manifold of dimension $d$ the conformally invariant differential operators along $\Sigma$,
$$\delta_{\ell}: \mathcal{T}^{*}\left[\frac{k-d}{2}\right] \rightarrow \mathcal{T}_{\Sigma}^{*}\left[\frac{k-d-2 \ell}{2}\right],$$
have properties as follows. If $d$ is odd then the $\delta_{\ell}$ have order and normal order $r=r_{N}=\ell$ for all $\ell \in \mathbb{Z}_{+}$. If $d$ is even then the $\delta_{\ell}$ have order and normal order $r=r_{N}=\ell$ if $\ell+1 \leq k \leq d-2$ or $\ell+2 \leq k=d$.

This follows easily from the identity (4) and the definition of of the tractor-D operator.
It turns out that appropriate combinations of the operators $\delta_{\ell}$ lead to good elliptic problems (and in particular problems which satisfy the so-called Lopatinski-Shapiro conditions which signal well-posedness for boundary problems) with the operator $\square_{k}$ (from Proposition 1), which itself is properly elliptic. See Proposition 7.1 in [6]. A key but technical point of that work with Branson is that there are modifications of the operators $\delta_{\ell}$ to similar conformal boundary operators $\delta_{i}^{\prime}$ (each of the same respective normal order as $\delta_{j}$ ) so that we may maintain the ellipticity properties but in addition achieve formally self-adjoint boundary problems. Let us simply summarise; the reader is referred to [6, 35, 40] for details and background.

Proposition 4. For $d$ even let $k \in\{0,2, \ldots, d-2\}$ and for $d$ odd let $k \in 2 \mathbb{Z}_{+}$. For each such $k$ and each of $\mathbf{m}=\mathbf{m}_{\mathrm{D}}=(0,2, \ldots, k-2), \mathbf{m}=\mathbf{m}_{\mathrm{N}}=(1,3, \ldots, k-1)$, and $\mathbf{m}=\mathbf{m}_{0}:=$ $(0,1, \ldots, k / 2-1)$ there exist conformally invariant normal boundary operators $\delta_{\mathbf{m}}^{\prime}$ such that $\left(\square_{k}, \delta_{\mathbf{m}}^{\prime}\right)$ is formally self-adjoint and satisfies the Lopatinski-Shapiro conditions.

\subsection*{3.2 The Dirichlet-to-Neumann maps}

Let $M$ be an $d$-dimensional conformal manifold of positive definite metric signature, with smooth boundary $\Sigma$. Suppose that $k$ is even and, if $d$ is even, suppose that $k<d$. Let $\mathbf{m}=\mathbf{m}_{\mathrm{D} \text { or } \mathrm{N}}$, and suppose that the problem $\left(\square_{k}, \delta_{\mathbf{m}}^{\prime}\right)$ has vanishing null space. Take a density $u$ on $\Sigma$, and boundary data
$$\delta_{m_{j}}^{\prime} u=U_{\mathrm{o}}, \quad \delta_{m_{i}}^{\prime} u=0 \quad \text { for all } \quad i \neq j,$$
on $\Sigma$, where $j$ is a chosen element of $\{1, \ldots, k / 2\}$. Let $E_{k, m_{j}}$ be the solution operator for the system $\square_{k} u=0$ with (6); by elliptic regularity the range of $E_{k, m_{j}}$ is smooth and by construction it is an invariant operator carrying $\mathcal{E}_{\Sigma}\left[\frac{k-d-2 m_{j}}{2}\right]$ to $\mathcal{E}\left[\frac{k-d}{2}\right]$. We can now take $E_{k, m_{j}} u$ and apply $\delta_{\ell}^{\prime}$ (or $\delta_{\ell}$ ). ( $\ell$ need not be one of the normal orders in m.) Composing,
$$\mathcal{E}_{\Sigma}\left[\frac{k-d-2 m_{j}}{2}\right] \xrightarrow{E_{k, m_{j}}} \mathcal{E}\left[\frac{k-d}{2}\right] \xrightarrow{\delta_{\ell}^{\prime}} \mathcal{E}_{\Sigma}\left[\frac{k-d-2 \ell}{2}\right],$$
we obtain invariant operators
$$P_{k, \mathbf{m}, m_{j}, \ell}: \mathcal{E}_{\Sigma}\left[\frac{k-d-2 m_{j}}{2}\right] \rightarrow \mathcal{E}_{\Sigma}\left[\frac{k-d-2 \ell}{2}\right] .$$
Note that for this construction to make sense, as given, we need the source problem $E_{k, m_{j}}$ : $\mathcal{E}_{\Sigma}\left[\frac{k-d-2 m_{j}}{2}\right] \rightarrow \mathcal{E}\left[\frac{k-d}{2}\right]$ to be uniquely solvable. The second part of the construction $\mathcal{E}\left[\frac{k-d}{2}\right] \rightarrow$ $\mathcal{E}_{\Sigma}\left[\frac{k-d-2 \ell}{2}\right]$ is related to a complementary target problem, but its solvability properties are not required.

From elementary representation theory and the invariance of the construction, it is straightforward to show that when $m_{j}+\ell \neq k-1$ the operators $P_{k, \mathbf{m}, m_{j}, \ell}$ vanish for the standard conformal class on the unit ball. Equivalently they vanish on the unit hemisphere, which is in the conformal class of the unit ball, and this is a convenient homogeneous setting for exploiting the spherical harmonics in order to study this and related issues [6, Theorem 8.4]. In particular there one also sees that $P_{k, \mathbf{m}, m_{j}, k-1-m_{j}}$ has principal part $\left(-\Delta_{\Sigma}\right)^{\left(k-1-2 m_{j}\right) / 2}$, up to multiplication by a non-zero universal constant. In addition, by construction, the operators $P_{k, \mathbf{m}, m_{j}, k-1-m_{j}}$ are formally self-adjoint on any conformal manifold [6, Theorem 8.5].

Writing $P_{k, \mathbf{m}, m_{j}}:=P_{k, \mathbf{m}, m_{j}, k-1-m_{j}}$, in summary we have the following:
Theorem 1. Let $M^{d=n+1}$ be a conformal manifold of positive definite metric signature, with smooth boundary $\Sigma$. Suppose that $k$ is even and, in case $d$ is even, suppose that $k<d$. Let $\mathbf{m}=\mathbf{m}_{\mathrm{D} \text { or } \mathrm{N}, \text { or } 0}$, and suppose that the problem $\left(\square_{k}, \delta_{\mathbf{m}}^{\prime}\right)$ has vanishing null space. Then there exist canonical conformally invariant operators
$$P_{k, \mathbf{m}, m_{j}}: \mathcal{E}_{\Sigma}\left[\frac{k-n-2 m_{j}-1}{2}\right] \rightarrow \mathcal{E}_{\Sigma}\left[\frac{-k-n-2 m_{j}+1}{2}\right], \quad m_{j} \in \mathbf{m},$$
with principal part $\Delta^{\left(k-1-2 m_{j}\right) / 2}$.

\section*{4 Poincaré-Einstein Manifolds and generalisations}

We give here a conformal development of Poincaré-Einstein manifolds.

\subsection*{4.1 Almost Einstein manifolds}

The Schouten tensor $P$ (or $P^{g}$ ), introduced earlier, is related to the Ricci tensor by
$$\text { Ric }=(d-2) P+J g,$$
where $J$ is the metric trace of $P$. The metric $g$ is conformally Einstein if and only if there is a non-vanishing solution $x \in C^{\infty}(M)$ to the equation
$$\text { trace }- \text { free }(\nabla \nabla x+P x)=0 ;$$
if $x$ is such a solution then it follows easily from the conformal transformation of $P$ that the metric $\widehat{g}=x^{-2} g$ is Einstein [4].

Note that the requirement that $x$ be non-vanishing is critical if we want a solution $x$ to be a genuine conformal factor: $\widehat{g}=x^{-2} g$ will blow up conformally at points where $x$ vanishes. Nevertheless, let us relax this and allow any solution. Following [21] we will say that $(M, g)$ is almost Einstein if there is a solution $x \in C^{\infty}(M)$ to the equation (8).

It turns out that the almost Einstein condition is a useful weakening of the Einstein equations. First observe that the equation (8) is conformally well behaved. If we replace $x$ with a conformal density of weight $1, \sigma \in \mathcal{E}[1]$, then it is easily verified that (8) is actually conformally invariant;
it descends to a well defined equation on the conformal structure ( $M,[g]$ ). In a scale we may write the equivalent equation on $\sigma$ in the form
$$\nabla_{a} \nabla_{b} \sigma+P_{a b} \sigma+\boldsymbol{g}_{a b} \rho=0,$$
where the section $\rho \in \mathcal{E}[-1]$ captures the trace part. The next crucial observation is that by inspection of the formula (2) we see that the equation for a parallel section of standard tractor bundle $\mathcal{T}$ is just the prolonged system for this equation. Informally stated the first equation from (2) equates the variable $\mu_{a}$ to the derivative of $\sigma$. Then the middle equation from (2) just is $\nabla_{a} \nabla_{b} \sigma+P_{a b} \sigma+\boldsymbol{g}_{a b} \rho=0$, while $\nabla_{a} \rho=P_{a c} \mu^{c}$ is a differential consequence of this. From that system it follows that if $I \xlongequal{g}\left(\sigma, \mu_{a}, \rho\right)$ is a parallel section for $\nabla^{\mathcal{T}}$ then necessarily
$$\left(\sigma, \mu_{a}, \rho\right)=\left(\sigma, \nabla_{a} \sigma, \frac{1}{d}(\Delta \sigma-\mathrm{J} \sigma)\right) .$$
That is $I=\frac{1}{n} D_{A} \sigma$, where $D$ is Thomas tractor-D operator introduced in (3). Now by construction $D$ is differential and, on the other hand, parallel transport between two points along any curve gives an isomorphism of the vector bundle fibres over those points. It follows immediately that if $I$ is parallel and $\sigma$ vanishes on any neighbourhood then $I$ vanishes everywhere. Equivalently, if $I \neq 0$ is parallel then $\sigma:=h(X, I)$ is non-vanishing on an open dense set; this is the key. Summarising, we have the following.

Theorem 2. An almost Einstein structure is a conformal manifold ( $M,[g]$ ) equipped with a parallel (standard) tractor $I \neq 0$. The mapping from non-trivial solutions of (9) to paral-lel tractors is by $\sigma \mapsto \frac{1}{n} D \sigma$ with inverse $I \mapsto \sigma:=h(I, X)$, and $\sigma$ is non-vanishing on an open dense set $M \backslash \Sigma$. On this set $g_{+}:=\sigma^{-2} \boldsymbol{g}$ is Einstein.

From the theorem we see that an almost Einstein manifold just is a conformal manifold with a parallel standard tractor $I$ and we write $(M,[g], I)$ to indicate this. The set $\Sigma$, where the almost Einstein "scale" $\sigma=h(X, I)$ vanishes, is called the scale singularity set. Although it is not essential for our current discussion, we note that on Riemannian signature manifolds the possibilities for this are severely restricted as follows [25]. We write $|I|^{2}$ as a shorthand for $h(I, I)$.
Theorem 3. Let $(M,[g], \sigma)$ be an almost Einstein structure and write $I:=\frac{1}{n} D \sigma$. If $|I|^{2}<0$ then $\Sigma$ is empty and $\left(M, \sigma^{-2} \boldsymbol{g}\right)$ is Einstein with positive scalar curvature; If $|I|^{2}=0$ then $\Sigma$ is either empty or consists of isolated points, and $\left(M \backslash \Sigma, \sigma^{-2} \boldsymbol{g}\right)$ is Ricci-flat; if $|I|^{2}>0$ then the scale singularity set $\Sigma$ is either empty or else is a totally umbillic hypersurface, and $\left(M \backslash \Sigma, \sigma^{-2} \boldsymbol{g}\right)$ is Einstein of negative scalar curvature.

For the special case of Poincaré-Einstein manifolds, we shall see the result concerning total umbillicity in Corollary 1 below. Almost Einstein metrics turn up in the classifications by Derdzinski and Maschler of Kähler metrics which are almost everywhere conformal to Einstein, see e.g. [16] and references therein.

\subsection*{4.2 Poincaré-Einstein spaces}

Recall that a Poincaré-Einstein structure is a compact manifold $\left(M^{d=n+1}, g\right)$ with boundary $\Sigma=\partial M$. There is a defining function $x$ for $\Sigma$ so that $\left(M_{+}, g_{+}\right)$is Einstein with $\operatorname{Ric}^{g_{+}}=-n g_{+}$, where $M_{+}:=M \backslash \Sigma$ and, on this, $g_{+}:=x^{-2} g$.

Proposition 5. Poincaré-Einstein manifolds are scalar negative almost Einstein structures. Conversely on a compact manifold $M$ with boundary $\Sigma$, an almost Einstein structure $(M,[g], I)$ with $|I|^{2}=1$, and such that the scale singularity set is the boundary $\Sigma$, is a Poincaré-Einstein metric.

Proof. If $M$ is a Poincaré-Einstein manifold then, by definition, there is a defining function $x$ for the boundary so that $g_{+}:=x^{-2} g$ is Einstein. Thus $x$ is a smooth function that solves (8) on the interior and so, by continuity, also to the boundary. This gives the result. In the tractor picture we may equivalently observe that, on the interior, $I:=\frac{1}{n} D \sigma$ is parallel with $\sigma=x \tau$ where $\tau \in \mathcal{E}[1]$ is the scale giving $g$, that is $g=\tau^{-2} \boldsymbol{g}$. So we have $g_{+}=\sigma^{-2} \boldsymbol{g}$. By continuity $I$ is parallel to the boundary. Obviously the function $h(I, I)$ is constant. Off the zero set $\Sigma$, and calculating in the scale $g_{+}=\sigma^{-2} \boldsymbol{g}$, we have $\nabla^{g_{+}} \sigma=0$. Thus from (1) and (10) we have $|I|^{2}=-\frac{2}{d} J^{g_{+}}$where $J^{g_{+}}$is the $g_{+}$-trace of the Schouten tensor $P^{g_{+}}$. From the relationship between the Schouten and Ricci tensors it follows immediately that the normalisation $\operatorname{Ric}\left(g_{+}\right)=-n g_{+}$is exactly the condition $|I|^{2}=1$.

The converse direction is essentially clear from the last observations. If $I$ is parallel with $|I|^{2}=1$ then off the zero set of $\sigma:=h(X, I)$ we have $\operatorname{Ric}\left(g_{+}\right)=-n g_{+}$where $g_{+}:=\sigma^{-2} \boldsymbol{g}$. On the other hand along $\Sigma$ we have $\sigma=0$ and so, since $|I|^{2}=1$, it follows from (10) and (1) that $\boldsymbol{g}^{-1}(\nabla \sigma, \nabla \sigma)=1$. In particular $\nabla \sigma$ is non-vanishing along $\Sigma$ and so $\sigma$ is a "defining density" for $\Sigma$. Choosing a metric $g$ for $M$ we have $g=\tau^{-2} \boldsymbol{g}$ for some non-vanishing weight 1 density $\tau$. We set $x:=\sigma / \tau$ and note that $\Sigma$ is the zero set of $x$. Since $\Sigma$ is the boundary of $M$ (by a suitable sign choice for $\tau$ ) we may assume without loss of generality that $x$ is a non-negative function. In terms of $g$, the result $\boldsymbol{g}^{-1}(\nabla \sigma, \nabla \sigma)=1$ is equivalent to $|d x|_{g}^{2}=1$, and so $x$ is a defining function for the boundary $\Sigma$. (In fact $x$ is a special defining function in the sense of [30, Lemma 2.1] and [33].) On the other hand the Einstein metric $g_{+}$is $x^{-2} g$ and this completes the case. \(\square\)

From the Proposition we see that by specifying the almost Einstein structure ( $M,[g], I$ ) we have an essentially conformal description of a Poincaré-Einstein structure. We next see that $I$ encodes more than simply the Einstein scale. Recall the notion of a normal tractor, for a hypersurface or boundary, as introduced in Section 2.1.

Proposition 6. Let $(M,[g], I)$ be a Poincaré-Einstein manifold. Along the boundary $\Sigma$ we have $I_{A}=N_{A}$ where $N_{A}$ is the normal tractor for $\Sigma$.

Proof. First note that since $I_{A}$ has (conformally invariant) length 1 everywhere this is in particular true along $\Sigma$. (Of course $N_{A}$ has this property along $\Sigma$.)

Now
$$I_{A}=\frac{1}{d} D_{A} \sigma \stackrel{g}{=}\left(\begin{array}{c}
\sigma \\
\nabla_{a} \sigma \\
\frac{1}{d}(\Delta \sigma-\mathrm{J} \sigma)
\end{array}\right) .$$
Let us write $n_{a}:=\nabla_{a} \sigma$. Along $\Sigma$ we have $\sigma=0$, and so
$$\left.I_{A}\right|_{\Sigma} \stackrel{g}{=}\left(\begin{array}{c}
0 \\
n_{a} \\
\frac{1}{d} \Delta \sigma
\end{array}\right) .$$
Note that from (1) and $|I|^{2}=1$ we have that $\boldsymbol{g}^{a b} n_{a} n_{b}=1$ on $\Sigma$, and $n_{a}$ is seen to be a weight 1 unit co-normal for $\Sigma$.

Next we calculate the mean curvature $H$ in terms of $\sigma$. Recall that the second fundamental form of $\Sigma$ is $\Pi_{a b}=\Pi_{a}^{c} \Pi_{b}^{d} \nabla_{c} n_{b}$ (along $\Sigma$ ) where $\Pi$ is the orthogonal projection operator given by
$$\Pi_{a}^{c}=\delta_{a}^{c}-n^{c} n_{a} .$$
By construction this is independent of how $n_{a}$ is extended off $\Sigma$. Thus along $\Sigma$ we have
$$(d-1) H=\nabla^{a} n_{a}-n^{a} n^{b} \nabla_{b} n_{a} .$$

Now since $I_{A}$ is parallel we have
$$\nabla_{b} n_{a}=\nabla_{b} \nabla_{a} \sigma=-P_{a b} \sigma-\frac{1}{d} \boldsymbol{g}_{a b}(\Delta \sigma-\mathrm{J} \sigma) .$$
Along $\Sigma$ this simplifies to $\nabla_{b} n_{a}=-\frac{1}{d} \boldsymbol{g}_{a b} \Delta \sigma$, and so $\nabla^{a} n_{a}=-\Delta \sigma$. Thus we have
$$(d-1) H=-\left(1-\frac{1}{d}\right) \Delta \sigma \quad \Rightarrow \quad H=-\frac{1}{d} \Delta \sigma,$$
whence
$$\left.I_{A}\right|_{\Sigma} \stackrel{\tilde{g}}{=}\left(\begin{array}{c}
0 \\
n_{a} \\
-H
\end{array}\right),$$
as required. \(\square\)

Using Proposition 2, the following is an immediate consequence of the Proposition.
Corollary 1. If $(M,[g], I)$ is a Poincaré-Einstein manifold then the boundary $\Sigma=\partial M$ is totally umbillic.

\subsection*{4.3 The Poincaré-Einstein model space}

We shall construct here a model for the Poincaré-Einstein space, a model which fits with the conformal picture developed above.

Consider $\mathbb{R}^{d+2}$ equipped with a non-degenerate bilinear form $\mathcal{H}$ of signature $(d+1,1)$. The null cone $\mathcal{N}$ of zero-length vectors forms a quadratic variety and (projectivising this picture) the corresponding quadric in $\mathbb{P}_{d+1}$ is topologically a sphere $\mathbb{S}^{d}$. Let us write $\mathcal{N}_{+}$for the forward part of $\mathcal{N} \backslash\{0\}$ and write $\pi$ for the natural submersion $\mathcal{N}_{+} \rightarrow \mathbb{S}^{d}$. Each point $p \in \mathcal{N}_{+}$determines a positive definite inner product on $T_{x=\pi p} \mathbb{S}^{d}$ by $g_{x}(u, v)=\mathcal{H}_{p}\left(u^{\prime}, v^{\prime}\right)$ where $u^{\prime}, v^{\prime} \in T_{p} \mathcal{N}_{+}$are lifts of $u, v \in T_{x} \mathbb{S}^{d}$. For a given vector $u \in T_{x} \mathbb{S}^{d}$ two lifts to $p \in \mathcal{N}_{+}$differ by a vertical vector field. Since any vertical vector is normal (with respect to $\mathcal{H}$ ) to the cone it follows that $g_{x}$ is independent of the choices of lifts. Clearly then, each section of $\pi$ determines a metric on $\mathbb{S}^{d}$ and by construction this is smooth if the section is. Now, viewed as a metric on $T \mathbb{R}^{d+2}, \mathcal{H}$ is homogeneous of degree 2 with respect to the standard Euler vector field $E$ on $\mathbb{R}^{d+2}$, that is $\mathcal{L}_{E} \mathcal{H}=2 \mathcal{H}$, where $\mathcal{L}$ denotes the Lie derivative. In particular this holds on the cone, which we note is generated by $E$. On the other hand if a vector field on $\mathbb{R}^{d+2} \backslash\{0\}$ is the lift of a vector field on $\mathbb{S}^{d}$ then it is necessarily homogeneous of degree 0. It follows that that two different sections of $\pi: \mathcal{N}_{+} \rightarrow \mathbb{S}^{d}$ determine conformally related metrics. (We have stated this globally, but of course the same holds locally over neighbourhoods of $\mathbb{S}^{d}$.) We will see shortly that the standard sphere metric is in the conformal class. Thus $\mathbb{S}^{d}$ is equipped canonically with the standard conformal structure for the sphere (but not with a preferred metric from this class). This is the standard model of a homogeneous "flat" conformal structure. Evidently we may identify $\mathcal{N}_{+}$as the (total space) of the $\mathbb{R}_{+}$-ray-bundle of metrics over $\mathbb{S}^{d}$; the bundle consisting of metrics from this conformal class.

We can construct a Poincaré-Einstein metric over a cap of the sphere $\mathbb{S}^{d}$ as follows. Take a covector $I \in\left(\mathbb{R}^{d+2}\right)^{*}$ of length 1 and by the standard parallel transport (of $\mathbb{R}^{d+2}$ viewed as an affine structure) view this as a constant section of $T^{*} \mathbb{R}^{d+2}$. Then, writing $X^{A}$ for the standard coordinates on $\mathbb{R}^{d}$, the intersection of the hyperplane $I_{A} X^{A}=1$ with $\mathcal{N}_{+}$, which we shall denote $S_{+}$, is a section of $\pi$ over an open cap $C_{+}$of the sphere. Let us write $g_{+}$for the metric $S_{+}$gives on $C_{+}$. On the other hand the hyperplane $I_{A} X^{A}=0$ (parallel to the previous)
intersects $\mathcal{N}_{+}$in a cone of one lower dimension. The image of this under $\pi$ is a copy of $\mathbb{S}^{n}$ embedded in $\mathbb{S}^{d}$ (where as usual $d=n+1$ ). With respect to the given manifold structure on $\mathbb{S}^{d}$, this $\mathbb{S}^{n}$ is a boundary for its union with $C_{+}$which we denote by $C$. This follows because any null line though the origin and parallel to the $I_{A} X^{A}=1$ hyperplane lies in the hyperplane $I_{A} X^{A}=0$, whereas every other null line through the original meets the $I_{A} X^{A}=1$ hyperplane. The open cap $C_{+}$parametrises those null lines which meeting this hyperplane in the forward null cone (i.e. at a point of $S_{+}$). Note that the boundary $\mathbb{S}^{n}=\partial C$ canonically has no more than a conformal structure. This may obviously be viewed as arising as a restriction of the conformal structure on $\mathbb{S}^{d}$. Equivalently we may view its conformal structure as arising in the same way as the conformal structure on $\mathbb{S}^{d}$, except in this case by the restriction of $\pi$ to the sub-cone $I_{A} X^{A}=0$ in $\mathcal{N}_{+}$, and from $\mathcal{H}$ along this sub-cone. Note that any metric from the conformal class on $\mathbb{S}^{d}$ determines a metric on $C$ by restriction. Denoting one such by $g$ note that on $C^{+}$ this is conformally related to $g_{+}$.

Write $\boldsymbol{g}$ for the restriction of $\mathcal{H}$ to vector fields in $T \mathcal{N}_{+}$which are the lifts of vector fields on $\mathbb{S}^{d}$. Then for any pair $u, v \in \Gamma\left(T \mathbb{S}^{d}\right)$, with lifts $u^{\prime}, v^{\prime}, \boldsymbol{g}\left(u^{\prime}, v^{\prime}\right)$ is a function on $\mathcal{N}_{+}$homogeneous of degree 2, and which is independent of how the vector fields were lifted. Since $\mathcal{N}_{+}$may be identified with the (total space of the) bundle of conformal metrics, $\boldsymbol{g}\left(u^{\prime}, v^{\prime}\right)$ may be identified with a conformal density of weight 2 on $\mathbb{S}^{d}$. This construction determines a section of $S^{2} T^{*} \mathbb{S}^{d} \otimes$ $E[2]$ that we shall also denote by $\boldsymbol{g}$. This is the usual conformal metric for the sphere. Let us henceforth identify, without further mention, each function on $\mathcal{N}_{+}$which is homogeneous of degree $w \in \mathbb{R}$ with the corresponding conformal density of weight $w$. With $\sigma:=I_{A} X^{A}$, as above, note that $\sigma^{-2} \boldsymbol{g}$ is homogeneous of degree 0 on $\mathcal{N}_{+}$and agrees with the restriction of $\mathcal{H}$ along $S_{+}$. Thus on $C_{+}, \sigma^{-2} \boldsymbol{g}=g_{+}$, the metric determined by $S_{+}$. Similarly on $C$ we have $g=\tau^{-2} \boldsymbol{g}$, where $\tau$ is a non-vanishing conformal density of weight 1 . So on $C_{+}, g_{+}=x^{-2} g$ where $x$ is the function $\sigma / \tau$.

We may now put these observations into a more general context via the tractor bundle on $\mathbb{S}^{d}$. Let us write $\rho^{t}$ for the natural action of $\mathbb{R}_{+}$on $\mathcal{N}_{+}$and then $\rho_{*}^{t}$ for the derivative of this. Now modify the latter action on $T \mathbb{R}^{d+2}$ by rescaling: we write $t^{-1} \rho_{*}^{t}$ for the action of $\mathbb{R}_{+}$on $T \mathbb{R}^{d+2}$ which takes $u \in T_{p} \mathbb{R}^{d+2}$ to $t^{-1}\left(\rho_{*}^{t} u\right) \in T_{\rho^{t}(p)} \mathbb{R}^{d+2}$. Note that $u$ and $t^{-1}\left(\rho_{*}^{t} u\right)$ are parallel, according to the standard affine structure on $\mathbb{R}^{d+2}$. It is easily verified that the quotient of $T \mathbb{R}^{d+2} \mid \mathcal{N}_{+}$by the $\mathbb{R}_{+}$action just defined is a rank $d+2$ vector bundle $\mathcal{T}$ on $M$. Obviously the parallel transport of $\mathbb{R}^{d+2}$ determines a parallel transport on $\mathcal{T}$, that is a connection ∇ . Since $\mathbb{R}^{d+2}$ is totally parallel this connection is flat. The twisting of $\rho_{*}^{t}$ to $t^{-1} \rho_{*}^{t}$ is designed so that the metric $\mathcal{H}$ on $\mathbb{R}^{d+2}$ also descends to give a (signature $(d+1,1)$ ) metric $h$ on $\mathcal{T}$ and clearly this is preserved by the connection. In fact $(\mathcal{T}, h, \nabla)$ is the usual normal standard tractor bundle. This is proved under far more general circumstances in [11] (see also [24]); it is shown there that the tractor bundle arises from the Fefferman-Graham ambient metric by an argument generalising that above. In this picture the Euler vector field $E=X^{A} \partial / \partial X^{A}$ (using the summation convention), which generates the fibres of $\pi$, descends to the canonical tractor field $X \in \mathcal{T}[1]$.

It follows from these observations that, since the vector field $I$ is parallel on $\mathbb{R}^{d+2}$, its restriction to $\mathcal{N}_{+}$is equivalent to a parallel section of $\mathcal{T}$; we shall also denote this by $I$. So this is an almost Einstein structure on $\mathbb{S}^{d}$ and hence (by restriction) on $C ;|I|^{2}=1$ means that the almost Einstein structure we recover has $\operatorname{Ric}\left(g_{+}\right)=-n g_{+}$on $C_{+}$. Evidently the conformally invariant "top slot" of the tractor $I$ is $\sigma=X^{A} I_{A}=h(I, E)$ (as a homogeneous function - but as mentioned above homogeneous functions on $\mathcal{N}$ may be identified with conformal densities on $C$ ). The zero set $\Sigma$ for this is exactly $\mathbb{S}^{n}=\partial C$; recall any null line of $\mathcal{N}_{+}$that does not lie in the $I_{A} X^{A}=0$ hyperplane meets the $I_{A} X^{A}=1$ hyperplane (where, viewing $\sigma$ as a homogeneous function, we have $\sigma=1$ ). So now it follows from Proposition 5 that $(C,[g], I)$ is a Poincaré-Einstein space.

Of course this result may easily be verified by direct calculation, but such a calculation would only obscure this simple geometric picture. Note, for example, that Proposition 6 is realised geometrically here as the fact that the same constant ambient vector $I_{A}$ defines both the section $S_{+}$, that gives the metric on $C_{+}$, and the boundary manifold $\Sigma$ via the subcone where $\mathcal{N}_{+}$meets $I_{A} X^{A}=0$.

Finally we should say that in fact $I$ and the cone $\mathcal{N}$ determine a scalar negative almost Einstein structure on the entire sphere [25]. The Poincaré-metric is just the $\sigma \geq 0$ part of this. A similar construction using a constant vector with norm satisfying $|I|^{2}=-1$ gives the standard (Einstein) metric on the sphere, while a Euclidean (i.e. metric flat away from the scale singularity point) almost Einstein structure on the sphere minus a point is obtained by using a null constant vector $I$. Note that the group $\operatorname{SO}(h) \cong \operatorname{SO}(d+1,1)$ acts transitively on $\mathcal{N}_{+}$. Thus, in each case, the isotropy group of the constant vector $I$ is a subgroup of $\operatorname{SO}(h)$ which acts transitively on the corresponding almost Einstein interior. For example in the original case, with $|I|^{2}=1$, the isotropy group is isomorphic to $\operatorname{SO}(d, 1)$ and acts transitively on the hyperbolic cap $C_{+}$. Similarly in the other cases: if we take $I$ such that $|I|^{2}=-1$ then the isotropy group is a copy of $\operatorname{SO}(d+1)$ which acts transitively on the copy of the sphere that $I$ determines; for null $I$ the isotropy group is the Euclidean group fixing $I$ (and is a subgroup of the parabolic stabilising the line generated by $I$ ).

\section*{5 The Dirichlet-Neumann machinery on Poincaré-Einstein manifolds}

Here we wish to discuss the specialisations of certain key differential operators to Poincaré-Einstein manifolds and the implications for a Dirichlet-to-Neumann construction along the lines of that in [6]. Throughout this section we take $\left(M^{d},[g], I\right)$ to be a Poincaré-Einstein manifold with boundary $\Sigma^{n}=\partial M$. We write $\boldsymbol{g}$ for the conformal metric on $M$ and $\sigma \in \mathcal{E}[1]$ for the almost Einstein scale $h(X, I)$, that is $g_{+}:=\sigma^{-2} \boldsymbol{g}$ is Einstein of negative scalar curvature on the interior $M_{+}$.

First we make some elementary observations concerning the conformal calculus.

\subsection*{5.1 The scattering Laplacian}

Recall that $I_{A}=\frac{1}{d} D_{A} \sigma$ is the parallel tractor corresponding to the Einstein scale. First observe that from (5) and Proposition 6 it follows that $I^{A} D_{A}$ gives the conformal Robin operator $\delta$ along $\Sigma$ (at least on densities or tractors of weight $w \neq 1-d / 2$ ). Here we expose the further role of $I^{A} D_{A}$.

For $u \in \mathcal{E}[w]$ in $M$ we wish to calculate $I^{A} D_{A} u$ on the interior $M_{+}$. In particular let us express this in terms of the interior Einstein metric $g_{+}$. We have $\nabla^{g_{+}} \sigma=0$, and so
$$I_{A} D^{A} u=\sigma\left(\begin{array}{lll}
-\mathrm{J} / d & 0 & 1
\end{array}\right)\left(\begin{array}{c}
w(d+2 w-2) u \\
(d+2 w-2) \nabla^{g+} u \\
\Delta u-w Ј u
\end{array}\right),$$
where on the right-hand-side $I$ and $D^{A}$ are expressed in terms of the metric $g_{+}$, but we are still allowing the tensorial objects to be density valued. So we obtain
$$I^{A} D_{A} u=\sigma\left(\Delta u-\frac{2}{d} \mathrm{~J}(d+w-1) w u\right) .$$

Now let us use $d=n+1$ to replace $d$ and, for reasons that will shortly be clear, set $s:=n+w$.

Then we obtain
$$I^{A} D_{A} u=\sigma\left(\Delta+\frac{2 \mathrm{~J}}{d} s(n-s)\right) u .$$
Here $\Delta$ and J are (density-valued with weight (-2)) and $\Delta^{g_{+}}=\sigma^{2} \Delta, J^{g_{+}}=\sigma^{2} \mathrm{~J}$. But for the Einstein metric $g_{+}$with $\operatorname{Ric}\left(g_{+}\right)=-n g_{+}$we have $J^{g_{+}}=-d / 2$ and so this simplifies to
$$\sigma I^{A} D_{A} u=\left(\Delta^{g_{+}}-s(n-s)\right) u,$$
which agrees with the Laplacian controlling the scattering construction of Graham-Zworski, see (3.2) of [34]. For convenience let us refer to this as the scattering Laplacian.

\subsection*{5.2 The GJMS operators on a Poincaré-Einstein manifold}

Using the Fefferman-Graham ambient metric Graham-Jenne-Mason-Sparling (GJMS) constructed in [32] a large family of conformally invariant operators $P_{k}$ between density bundles. These take the form
$$P_{k}=\Delta^{k / 2}+\text { lower order terms. }$$
In fact $P_{2}$ is the usual conformal Laplacian from physics and, in the case of Riemannian signature, as we have here, is often termed the Yamabe operator. $P_{4}$ is due to S. Paneitz, while $P_{6}$ was constructed by V. Wünsch. Except at these low orders, the explicit details of the GJMS operators are complicated [24], and no general formula is available. For these and other related reasons the operators $\square_{k}$, with their explicit and manifestly formally self-adjoint formulae as in Proposition 1, were preferred for the construction of Dirichlet-to-Neumann operators in [6].

However the GJMS operators simplify dramatically on Einstein manifolds; from [19, Proposition 7.9] or [22, Theorem 1.2] on an Einstein manifold ( $M^{d}, g_{+}$) we have
$$P_{k}=\prod_{\ell=1}^{k / 2}\left(\Delta^{g_{+}}+\lambda_{\ell}\right),$$
where $\lambda_{\ell}=\mathrm{Sc}^{g_{+}}(d+2 \ell-2)(d-2 \ell) /(4 d(d-1))$ and $\Delta^{g_{+}}=-\nabla^{a} \nabla_{a}$ is the Laplacian for $g_{+}$. This generalises the situation on the sphere, as observed some time ago by Branson [5].

It will be useful for us to know where (13) comes from in the tractor picture. On a conformally Einstein manifold ( $M,[g]$ ) if $\sigma$ is an Einstein scale, with corresponding metric $g_{+}$and parallel tractor $I_{A}:=\frac{1}{d} D_{A} \sigma$, then we may form the operator $P_{k}^{g_{+}}: \mathcal{E}\left[\frac{k-n}{2}\right] \rightarrow \mathcal{E}\left[-\frac{k+n}{2}\right](k \in 2 \mathbb{N})$ by
$$P_{k}^{g_{+}} u=\sigma^{1-k / 2} I^{A_{2}} \cdots I^{A_{k / 2}} \square D_{A_{2}} \cdots D_{A_{k / 2}} u .$$
By construction this depends on $g_{+}$. Surprisingly if $g_{+}^{\prime}$ is another Einstein metric in the conformal class $g_{+}$then $P_{k}^{g_{+}}=P_{k}^{g_{+}^{\prime}}$ (see [22, Theorem 3.1]). So for any $k \in 2 \mathbb{N}, P_{k}^{g_{+}}$is a canonical operator on conformally Einstein manifolds. Thus if the conformal class is fixed we may omit the $g_{+}$in $P_{k}^{g_{+}}$. This is not a clash of notation since in fact on conformally Einstein manifolds, and for the $k$ where the GJMS operators $P_{k}$ are defined, they agree with the operator (14) [22, Theorem 3.3].

The factorisation in (13) arises as follows. Using that $I$ is parallel, we may rewrite (14) as
$$P_{k} u=\sigma^{-k / 2}\left(I^{A_{k / 2}} D_{A_{k / 2}}\right) \circ \cdots \circ\left(I^{A_{2}} D_{A_{2}}\right) \circ\left(I^{A_{1}} D_{A_{1}}\right) u .$$
As we observed below (11), provided we work in an Einstein scale $g_{+}$, then each factor $\left(I^{A_{i}} D_{A_{i}}\right)$ may be re-expressed in the form $\sigma^{-1}\left(\Delta^{g_{+}}+\lambda_{i}\right)$. The value of the constant $\lambda_{i}$ reflects the
conformal weight of terms to its right. The scale $\sigma$, which gives $g_{+}=\sigma^{-2} \boldsymbol{g}$, is parallel for the Levi-Civita connection $\nabla_{+}^{g}$, and so the factors of $\sigma$ cancel, at least after also replacing the density $u$, as well as the density-valued operators and curvature J with their unweighted equivalents. We arrive at (13). We will term (14) a GJMS operator including for the high $k$ in even dimensions where the GJMS operators were not defined.

Specialising to a Poincaré-Einstein manifold we use the observation in (12) to suggestively re-express $P_{k} u\left(u \in \mathcal{E}\left[\frac{k-n}{2}\right]\right)$ as a composition of scattering Laplacians
$$P_{k} f=\left(\Delta^{g_{+}}-s_{k / 2}\left(n-s_{k / 2}\right)\right) \circ \cdots \circ\left(\Delta^{g_{+}}-s_{2}\left(n-s_{2}\right)\right) \circ\left(\Delta^{g_{+}}-s_{1}\left(n-s_{1}\right)\right) f,$$
where $f=\sigma^{\frac{n-k}{2}} u$ is the function equivalent to $u$ in the trivialisation of $\mathcal{E}\left[\frac{k-n}{2}\right]$ afforded by $\sigma$. Since $u$ has weight $w_{0}:=(k-n) / 2$, and each factor $I^{A} D_{A}$ lowers weight by 1 unit, we have $s_{i}=n+w_{0}+1-i=(k+n) / 2+1-i$, for $i=1, \ldots, k$.

\subsection*{5.3 Algebraic decompositions}

We digress briefly to recall some rather general considerations from the work [26] with Šilhan. Let $\mathcal{V}$ denote a vector space over a field $\mathbb{F}$. Suppose that $\mathcal{P}: \mathcal{V} \rightarrow \mathcal{V}$ is a linear operator that may be expressed as a composition
$$\mathcal{P}=\mathcal{P}_{0} \mathcal{P}_{1} \cdots \mathcal{P}_{l},$$
where the linear operators $\mathcal{P}_{i}: \mathcal{V} \rightarrow \mathcal{V}, i=0, \ldots, \ell$, are mutually commuting. One might hope that we can characterise the range space $\mathcal{R}(\mathcal{P})$ and null space $\mathcal{N}(\mathcal{P})$ of $\mathcal{P}$ in terms of data for the factors $\mathcal{P}_{i}$. This is straightforward if the $\mathcal{P}_{i}$ are each invertible, but in fact far weaker conditions suffice to make significant progress in this direction. One situation which is particularly useful is as follows. Suppose that we there are linear operators $Q_{i}: \mathcal{V} \rightarrow \mathcal{V}, i=0,1, \ldots, \ell$, that yield a decomposition of the identity,
$$i d_{V}=Q_{0} \mathcal{P}^{0}+\cdots+Q_{\ell} \mathcal{P}^{\ell},$$
where $\mathcal{P}^{i}:=\Pi_{i \neq j=0}^{j=\ell} \mathcal{P}_{i}, i=0, \ldots, \ell ;$ and the $\mathcal{P}_{i} \mathrm{~s}$ and the $Q_{j} \mathrm{~s}$ are mutually commuting in that
$$\mathcal{P}_{i} Q_{j}=Q_{j} \mathcal{P}_{i}, \quad i, j \in\{0, \ldots, \ell\} .$$
This is sufficient to give a 1-1 relationship between solutions $u \in \mathcal{V}$ of the inhomogeneous problem $\mathcal{P} u=f$ and solutions $\left(u_{0}, \ldots, u_{\ell}\right) \in \oplus^{\ell+1} \mathcal{V}$ of the problem
$$\mathcal{P}_{0} u_{0}=f, \quad \ldots, \quad \mathcal{P}_{\ell} u_{\ell}=f,$$
see [26, Theorem 2.2]. Thus for example the range of $\mathcal{P}$ is exactly the intersection of the range spaces for the components $\mathcal{P}_{i}$. The map from $u$, solving $\mathcal{P} u=f$, to solutions of the system is obvious:
$$u \mapsto\left(\mathcal{P}^{0} u, \ldots, \mathcal{P}^{\ell} u\right) .$$
One key point is that (16) gives an inverse by
$$\left(u_{0}, \ldots, u_{\ell}\right) \mapsto \sum_{i=0}^{i=\ell} Q_{i} u_{i} .$$

Important for us here is that, given the situation above, then for each $i \in\{0, \ldots, \ell\}$, we have
$$Q_{i} P^{i}: \mathcal{N}(\mathcal{P}) \rightarrow \mathcal{N}\left(\mathcal{P}_{i}\right)$$
and this is a projection. Thus we obtain a direct decomposition of the null space $\mathcal{N}(\mathcal{P})$. In applying these results in the case that the $\mathcal{P}_{i}$ are partial differential operators we should expect that in general the $Q_{i}$, when they exist, will be pseudo-differential operators. However remarkably there are a large class of situations where we can solve (16) algebraically. For example, for the case of partial differential operators $\mathcal{P}_{i}$ it can be that the $Q_{j}$ are again differential and obtained algebraically from the formulae for the $\mathcal{P}_{i}$. The very simplest situation of this is in fact exactly what we need here and is as follows. This is a special case from Theorem 1.1 of [26].

Theorem 4. Let $\mathcal{V}$ be a vector over the field $\mathbb{F}$. Suppose that $E$ is a linear endomorphism on $\mathcal{V}$, and $P=P[E]: \mathcal{V} \rightarrow \mathcal{V}$ is a linear operator polynomial in $E$ which factors as
$$P[E]=\left(E-\mu_{1}\right) \cdots\left(E-\mu_{p}\right),$$
where the scalars $\mu_{1}, \ldots, \mu_{p} \in \mathbb{F}$ are mutually distinct. Then the solution space $\mathcal{V}_{P}$, for $P$, admits a canonical and unique direct sum decomposition
$$\mathcal{V}_{P}=\oplus_{i=0}^{\ell} \mathcal{V}_{\mu_{i}},$$
where, for each $i$ in the sum, $\mathcal{V}_{\mu_{i}}$ is the solution space for $E-\mu_{i}$. The projection $\operatorname{Proj}_{i}: \mathcal{V}_{P} \rightarrow \mathcal{V}_{\mu_{i}}$ is given by the formula
$$\operatorname{Proj}_{i}=Q_{i} \prod_{i \neq j=1}^{j=p}\left(E-\mu_{j}\right), \quad \text { where } \quad Q_{i}=\prod_{i \neq j=1}^{j=p} \frac{1}{\mu_{i}-\mu_{j}} .$$

On Einstein manifolds that are not Ricci flat it is easily verified that the constants $\lambda_{i}$, appearing in the expression (13) for $P_{k}$, satisfy $\left(\lambda_{i}=\lambda_{j}\right) \Rightarrow(i=j), i, j \in\{1, \ldots, k / 2\}$. Thus we have exactly the situation of the Theorem above, and it follows that the solution space for $P_{k}$ decomposes directly. (See [26] for further details and [27] for applications as well as a similar treatment of operators on differential forms.) In particular, from the Theorem and (15), we have the following.

Proposition 7. On the interior $M_{+}$of a Poincaré-Einstein manifold we have
$$\mathcal{N}\left(P_{k}\right)=\oplus_{i=1}^{k / 2} \mathcal{N}\left(\Delta^{g_{+}}-s_{i}\left(n-s_{i}\right)\right),$$
where $s_{i}=\frac{k+n+1-2 i}{2}$, for $i=1, \ldots, k$.

\subsection*{5.4 Dirichlet-Neumann maps from $\boldsymbol{P}_{\boldsymbol{k}}$}

We consider the situation first for the standard conformal Dirichlet-to-Robin operator. That is, for the source problem we use the Yamabe Dirichlet problem $\left(P_{2}, \delta_{0}\right)$, while for the second part of the construction (7) we use the conformal Robin operator $\delta=n^{a} \nabla_{a}^{g}+\frac{n-1}{2} H^{g}$, from Section 3.1.

Recall that the Einstein scale $\sigma$ is a defining density for the boundary $\Sigma$, and along $\Sigma$ we have $n^{a} \nabla_{a}^{g} \sigma=n^{a} n_{a}=1$. It follows easily [6] from the conformal transformation of the mean curvature that one can choose the metric $g$ on $M$ so that $H^{g}=0$ (so then $\Sigma$ is totally geodesic). Let us henceforth use $g$ to mean such a metric. Consider a possible solution $u$ to
$$P_{2} u=0 \quad \text { of the form } \quad u=U_{\mathrm{o}}+\sigma U_{\mathrm{i}},$$
where $U_{\mathrm{o}}$ and $U_{\mathrm{i}}$ are smooth and $\left.\delta U_{\mathrm{o}}\right|_{\Sigma}=0$. Note that $\delta \sigma=1$ along $\Sigma$. Given unique solvability of the source problem, such a solution $u$ would reveal a conformal Dirichlet-to-Neumann map, from Theorem 1, with $P_{2, \mathbf{m}_{0}, 0}(f)=\left.U_{\mathrm{i}}\right|_{\Sigma}$ where $f=\left.U_{\mathrm{o}}\right|_{\Sigma}$.

Suppose that $\tau$ is the scale determining $g$, i.e. $g=(\tau)^{-2} \boldsymbol{g}$. And set $x:=\sigma / \tau$. From Proposition 7 it follows that, in terms of the scale $g_{+}$, the problem (19) is equivalent to
$$\left(\Delta^{g_{+}}-s(n-s)\right) u^{g_{+}}=0 \quad \text { with } \quad u^{g_{+}}=x^{n-s} U_{\mathrm{o}}^{g}+x^{s} U_{\mathrm{i}}^{g},$$
where $s=\frac{n+1}{2}$. Here $u^{g_{+}}$is the function equivalent to the density $u$ with respect to the trivialisation of $\left.\mathcal{E}\left[\frac{1-n}{2}\right]\right|_{M_{+}}$afforded by $\sigma$, that is $u^{g_{+}}=\sigma^{(n-1) / 2} u$. On the other hand $U_{\mathrm{o}}^{g}$ and $U_{\mathrm{i}}^{g}$ are the functions equivalent, via the scale $g$ to, respectively, $U_{\mathrm{o}}$ and $U_{\mathrm{i}}$. For example $U_{\mathrm{o}}^{g}=\tau^{(n-1) / 2} U_{\mathrm{o}}$. Now according to [37] (using [36, 34]), provided $s(n-s)$ is not an $L^{2}$ eigenvalue of $\Delta^{g_{+}}$, the Dirichlet problem here is uniquely solved by solutions of this form and so $\left.U_{\mathrm{o}}^{g}\right|_{\Sigma} \mapsto$ $\left.U_{\mathrm{i}}^{g}\right|_{M_{+}}$is the scattering map of Graham-Zworski [34]. So this is seen to agree with the map $f \mapsto P_{2, \mathbf{m}_{0}, 0}(f)$ of Theorem 1. In fact in [37] they make exactly this point: that for $s=(n+1) / 2$ the scattering map agrees with a Dirichlet-to-Neumann map.

This situation for the higher order GJMS operators is partly similar as follows. Consider Dirichlet-Neumann operators constructed as in [6], i.e. as in Theorem 1, except using a GJMS operator $P_{k}$ as the interior operator (rather than $\square_{k}$ ). There is the question of whether there are suitable boundary operators for $P_{k}$, to replace the $\delta_{\mathbf{m}}^{\prime}$, of Proposition 4 and Theorem 1. Rather than confront this possibly difficult issue at this point, let us simply assume that there are such operators and denote these also by $\delta_{\mathbf{m}}^{\prime}$. That is we will assume that we have all the conditions required for Theorem 1, with now $P_{k}$ everywhere replacing $\square_{k}$ in that Theorem. This assumption is not totally outrageous: For $P_{2}$, as above, we have $P_{2}=\square_{2}$ and similarly for $P_{4}$, provided $d \neq 4$, this is satisfied as $P_{4}$ is a non-zero multiple of $\square_{4}$. Similarly on conformally flat manifolds also this is satisfied for all $k$ in the range covered in Theorem 1, as again we have that $P_{k}$ and $\square_{k}$ agree. (See [24] for these last facts.)

It will shortly be clear that for comparison with [34], the source problem $\left(P_{k}, \delta_{\mathbf{m}_{0}}^{\prime}\right)$ (termed the generalised Dirichlet problem in [6]) is relevant. So suppose that this uniquely solvable. (Note from (18) this requires that $s_{i}\left(n-s_{i}\right)$ is not an $L^{2}$ eigenvalue of $\Delta^{g_{+}}$, for $s_{i}$ as in Proposition 7.) Then with Dirichlet boundary data as in (6) we get a Dirichlet-to-Neumann map akin to $P_{k, \mathbf{m}, m_{j}}$. According to Proposition 7, any solution $u$ is a direct sum $u=u_{1}+u_{2}+\cdots+u_{k / 2}$, where $\left(\Delta^{g_{+}}-s_{\ell}\left(n-s_{\ell}\right)\right) u_{\ell}^{g_{+}}=0$. However from this perspective it is not immediately clear how, in general, to relate the boundary data from the $P_{k}$ problem to boundary data for the solution $u_{\ell}^{g_{+}}$ of the scattering Laplacian. There are several difficulties here. For example, according to Theorem 4, the projections $u \mapsto u_{\ell}$ are administered by differential operators which, as given, do not make sense on $\Sigma$.

In the other direction, suppose we have a solution $u^{g_{+}}$to $\left(\Delta^{g_{+}}-s_{j}\left(n-s_{j}\right)\right)(j \in\{1, \ldots, k / 2\})$ of the form
$$u^{g_{+}}=x^{n-s_{j}} U_{\mathrm{o}}^{g}+x^{s_{j}} U_{\mathrm{i}}^{g}$$
with $s_{j}=\frac{k+n-1-2 m_{j}}{2}$ and $m_{j} \in \mathrm{~m}_{0}$. (Since $2 s_{\ell}-n$ is odd and the Poincaré-Einstein metric is suitably even, in the sense described pp. 108-109 of [34], it follows that the coefficient of $G$ in [34, Proposition 3.5] vanishes. See the proof of Proposition 4.2 in [34], or Lemma 4.1 in [36]. Thus we expect solutions of the above form provided that $s_{\ell}\left(n-s_{\ell}\right)$ is not an $L^{2}$ eigenvalue of $\Delta^{g_{+}}$.) Then using that $x=\sigma / \tau$ we may re-express the solution in terms of densities:
$$u=\sigma^{m_{j}} U_{\mathrm{o}}+\sigma^{k-1-m_{j}} U_{\mathrm{i}},$$
with (using (15)) $u \in \mathcal{E}\left[\frac{k-d}{2}\right]$ solving $P_{k} u=0$ and $U_{\mathrm{o}} \in \mathcal{E}\left[\frac{k-n-2 m_{j}-1}{2}\right]$ and $U_{\mathrm{i}} \in \mathcal{E}\left[\frac{-k-n+2 m_{j}+1}{2}\right]$. Thus $\left.U_{\mathrm{o}}^{g}\right|_{\Sigma}$ is the function equivalent to the conformal density $\left.U_{\mathrm{o}}\right|_{\Sigma}=\left.c \cdot \delta_{m_{j}}^{\prime} u\right|_{\Sigma}$, for some non-zero constant $c$. We also clearly have that $\left.\delta_{m_{i}}^{\prime} u\right|_{\Sigma}=0$ for integers $i, 0 \leq i<j$, and $\left.\delta_{k-1-m_{j}}^{\prime}\left(\sigma^{k-1-m_{j}} U_{\mathrm{i}}\right)\right|_{\Sigma}$ is a nonzero constant times $\left.U_{\mathrm{i}}\right|_{\Sigma}$. For example if $j=k / 2-1$, then $u$ is
the unique solution to the $\left(P_{k}, \delta_{\mathbf{m}_{0}}^{\prime}\right)$ problem with $\left.\delta_{m_{j}}^{\prime} u\right|_{\Sigma}$ prescribed to agree with $\left.c^{-1} \cdot U_{\mathrm{o}}\right|_{\Sigma}$. However we cannot in general say more to compare the scattering map with the Dirichlet-to-Neumann map without considerable explicit information about the asymptotics of $u$.

It is also clear that this comparison will be sensitive to the details of the boundary operators $\delta_{r}^{\prime}$ used. The observation at the beginning of Section 5.1, that for most weights $I^{A} D_{A}$ recovers the conformal Robin operator $\delta$, suggests the idea that there are likely to be higher order analogues of $\delta$ (i.e. variants of the $\delta_{r}^{\prime}$ ) that are well adapted to the GJMS operators on Poincaré-Einstein manifolds. Since such operators could significantly simplify the conformal Dirichlet-to-Neumann construction and its relationship to the the scattering map it seems that investigating this possibility should be the next step in the programme.

\section*{6 New directions: translating}