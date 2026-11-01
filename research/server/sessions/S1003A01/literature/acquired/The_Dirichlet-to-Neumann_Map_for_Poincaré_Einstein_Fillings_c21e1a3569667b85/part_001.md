---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: The Dirichlet-to-Neumann Map for Poincaré–Einstein Fillings]

---
source_file: 2307_08470.pdf
converter: mathpix
format: mmd
---

\title{
THE DIRICHLET-TO-NEUMANN MAP FOR POINCARÉ-EINSTEIN FILLINGS
}

\author{
SAMUEL BLITZ ${ }^{\diamond}$, A. ROD GOVER ${ }$, JAROSŁAW KOPINSKI*, \& ANDREW WALDRON*
}

\begin{abstract}
We study the non-linear Dirichlet-to-Neumann map for the Poincaré-Einstein filling problem. For even dimensional manifolds the range of this non-local map is described in terms of a rank two "Dirichlet-to-Neumann tensor" along the boundary determined by the Poincaré-Einstein metric. This tensor is proportional to the variation of renormalized volume along a path of Poincaré-Einstein metrics. We construct natural "Dirichlet-to-Neumann hypersurface invariants" that are conformally invariant and recover all Dirichlet-to-Neumann tensors. We give an explicit formula for these hypersurface invariants and use a new vanishing result for odd order $T$-curvatures to show that they are the unique, natural conformal hypersurface invariant of transverse order equaling the boundary dimension. We also construct such conformally invariant Dirichlet-to-Neumann hypersurface invariants for Poincaré-Einstein fillings for odd dimensional manifolds with conformally flat boundary.
\end{abstract}

Keywords: Conformal geometry, Poincaré-Einstein manifolds, Dirichlet-to-Neumann map, renormalized volume.

\section*{1. Introduction}

A smooth Riemannian $d$-manifold $\left(M_{+}, g^{o}\right)$ is said to be conformally compact if $M_{+}$is the interior of a smooth manifold with boundary $M$, and the compactified metric
$$g_{s}=s^{2} g^{o}$$
extends smoothly to a metric on $M=\overline{M_{+}}$for some (and so any) smooth defining function $s \in C^{\infty} M$. By the latter we mean that $\mathrm{d} s$ is nowhere vanishing along $\Sigma:=s^{-1}(0)=\partial M$. Conformally compact manifolds for which the trace-free Ricci tensor vanishes, i.e.
$$\operatorname{Ric}_{(a b) \circ}^{g^{o}}=0,$$
are termed Poincaré-Einstein. Necessarily, Poincaré-Einstein manifolds have constant negative scalar curvature, which by convention, we choose to be $-d(d-1)$. A classical example is the Poincaré ball $M_{+}=\left\{\left.\vec{x} \in \mathbb{R}^{d}| | \vec{x}\right|^{2}<1\right\}$ with
$$g^{o}=\frac{4|d \vec{x}|^{2}}{\left(1-|\vec{x}|^{2}\right)^{2}}$$
In addition to myriad mathematical applications, Poincaré-Einstein and conformally compact structures have played a central rôle in the geometry of physical models relating boundary field theories to bulk gravitational ones (see for example [16, 28, 31, 11, 17] and 35, 32, 30], respectively).

Since $s^{2} g^{o}$ extends to the boundary for any defining function $s$, a conformally compact structure canonically determines a conformal class of boundary metrics $\boldsymbol{c}_{\Sigma}$ that are induced by a corresponding conformal class of metrics $\boldsymbol{c}$ on $M$. It turns out that the formal asymptotics of a Poincaré-Einstein metric $g^{o}$ provide an effective tool for the study of the conformal manifold $\left(\Sigma, \boldsymbol{c}_{\Sigma}\right)$ (see [16, 17]). We say that a conformally compact structure for which
$$\operatorname{Ric}_{(a b) \circ}^{g^{o}}=s^{k} Q_{(a b) \circ},$$

\footnotetext{
2020 Mathematics Subject Classification. 53C18, 53A55, 53C21, 58J32.
}
for some smooth tensor $Q_{a b}$ on $M^{d}$, is asymptotically Poincaré-Einstein of order $k$ and denote such data by $\mathrm{APE}_{k}^{d}$. We often drop the label $d$ when context makes it clear. We also adopt the notation $\mathcal{O}\left(s^{k}\right)$ for the right hand side of the above display and other such quantities. The case $k=d-2$ is distinguished in the sense that $g_{s}$, modulo terms of order $\mathcal{O}\left(s^{d}\right)$, is no longer determined solely by the boundary conformal manifold $\left(\Sigma, \boldsymbol{c}_{\Sigma}\right)$. This is exactly when the asymptotics of a global solution first probe the interior structure of $M_{+}$.

A key global conformal invariant of an even dimensional Poincaré-Einstein structure $\left(M_{+}, g^{o}\right)$ is its renormalized volume [32, 26, 24], which arises as follows. Firstly, a key result of Graham and Lee [29] (valid for both even or odd dimension parity) is that, for each choice of boundary metric representative $\bar{g}$ for $\boldsymbol{c}_{\Sigma}$, on a collar neighborhood of $\Sigma$ there exists a unique defining function $s_{\mathrm{GL}}$ such that this function returns the (minimal) geodesic distance $r$ to the boundary $\Sigma$ as measured by the compactified metric $g_{r}=r^{2} g^{o}$. Now consider the one-parameter $\varepsilon \in \mathbb{R}_{>0}$ family of Riemannian manifolds $M_{\varepsilon}$ determined by the metric $\bar{g}$ according to
$$M_{\varepsilon}:=\left\{p \in M_{+} \mid r(p)>\varepsilon\right\},$$
with Riemannian metric given by the restriction of the metric $g^{o}$. Then the renormalized volume is given, independently from the original choice of boundary metric $\bar{g}$ required to determine $s_{\mathrm{GL}}$ and when $d$ is even, by
$$\operatorname{Vol}^{\mathrm{ren}}\left(M_{+}, g^{o}\right):=\left.\frac{1}{(d-1)!} \frac{\mathrm{d}^{d-1}}{\mathrm{~d} \varepsilon^{d-1}}\left(\varepsilon^{d-1} \int_{M_{\varepsilon}} \mathrm{dVol}^{g^{o}}\right)\right|_{\varepsilon=0} .$$
For four-manifolds, a result of Anderson [5] is that
$$\operatorname{Vol}^{\mathrm{ren}}=\frac{4 \pi^{2}}{3} \chi-\frac{1}{24} \int_{M_{+}}\left|W^{g^{o}}\right|^{2} \mathrm{dVo} l^{g^{o}}$$
where $W$ denotes the Weyl tensor and $\chi$ is the Euler characteristic of $M_{+}$. Moreover, Anderson also established that the functional gradient of the renormalized volume, along a path of Poincaré-Einstein metrics, is given by
$$\frac{1}{6} \stackrel{\circ}{\top} C_{\hat{n}(a b)}^{g} .$$
Here $C$ denotes the Cotton tensor, $\hat{n}$ is the inward unit normal of $\Sigma \hookrightarrow(M, g)$, and ${ }^{\circ}$ denotes evaluation along $\Sigma$ as well as projection of $\left.\odot^{2} T^{*} M\right|_{\Sigma}$ to directions tangential to $\Sigma$ and removal of the trace part. The resulting section space is isomorphic to that of $\odot_{\mathrm{o}}^{2} T^{*} \Sigma$. Note that, since conformal transformations preserve angles (and metric tracelessness), this projection is independent of any choice of $g \in \boldsymbol{c}$. Throughout, we use a ○ to denote trace-free parts of a tensor.

As discussed above, picking a metric $\bar{g} \in \boldsymbol{c}_{\Sigma}$ and any $p$ in a suitable collar neighborhood of $\Sigma$, we may write the corresponding Graham-Lee defining function $s_{\mathrm{GL}}(p)=r(p)$ where $r(p)$ is the minimal geodesic distance between $p$ and $\Sigma$ as measured by the metric $g_{r}=r^{2} g^{o}$. In coordinates $(r, \vec{x})$ for which $g_{r}\left(\frac{\partial}{\partial r}, \frac{\partial}{\partial \vec{x}}\right)=0$, series in powers of $r$ are termed Fefferman-Graham expansions following their fruitful employment for the description of conformal invariants in [16]. In $d$ dimensions, terms of order $r^{d-1}$ in the expansion of the Graham-Lee compactified metric $g_{r}$ are of particular interest. In particular, in dimension $d=4$, the third Lie derivative of the compactified metric $g_{r}$ extracts the term of order $r^{3}$ and defines a tensor
$$\mathrm{DN}_{a b}^{(4)}:=\left.\left(\mathcal{L}_{\frac{\partial}{\partial r}}^{3} g_{r}\right)_{a b}\right|_{\Sigma} .$$
Remarkably, the above tensor satisfies
$$\mathrm{DN}_{a b}^{(4)} \propto \stackrel{\circ}{\top} C_{\hat{n}(a b)}^{g_{r}},$$
where $\propto$ denotes equality up to a non-zero constant. This tensor is interesting, especially for general relativity (see for example [20, 33]), and because it is the first odd order term in the Fefferman-Graham expansion of $g_{r}$. As shown in [16, 26], the tensor DN ${ }^{(4)}$ changes covariantly
when computed with respect to an expansion in a new geodesic coordinate $r^{\prime}$ corresponding to a different choice of $\bar{g}^{\prime} \in \boldsymbol{c}_{\Sigma}$. On the other hand, under a general conformal transformation of the metric
$$\stackrel{\circ}{\top} C_{\hat{n}^{\prime}(a b)}^{\Omega^{2} g}=\bar{\Omega}^{-1} \stackrel{\circ}{\top} C_{\hat{n}(a b)}^{g},$$
where $\hat{n}_{a}^{\prime}=\bar{\Omega} \hat{n}_{a}$, for $0<\Omega \in C^{\infty} M$ and $\bar{\Omega}:=\left.\Omega\right|_{\Sigma}$, so long as $g \in \boldsymbol{c}$ where $\boldsymbol{c}$ is a conformal class of metrics defined by a Poincaré-Einstein structure (see [9] for the generalization to arbitrary conformal structures). It therefore constitutes an example of what we shall later term a conformal hypersurface invariant of the conformal embedding $\Sigma \hookrightarrow(M, \boldsymbol{c})$, while the tensor $\mathrm{DN}^{(4)}$ defines a section of $\odot_{o}^{2} T^{*} \Sigma[-1]$. (This is the space of symmetric, rank 2, trace-free tensor-valued, weight -1 conformal densities; the latter are explained in Section 2 but here it suffices to view a weight $w$ tensor-valued density $T$ on a conformal manifold $M$ as an equivalence class $T=[g, t]=$ $\left[\Omega^{2} g, \Omega^{w} t\right]$ of metric-tensor pairs with respect to conformal rescalings.) In the same vein, the tensor $\stackrel{\circ}{\top} C_{\hat{n}(a b)}^{g}$ defines a section of $\left.\stackrel{\circ}{\top} \odot^{2} T^{*} M[-1]\right|_{\Sigma}$ that encodes the information of DN ${ }^{(4)}$.

Since the section of $\odot_{0}^{2} T^{*} \Sigma[-1]$ defined by the tensor $\mathrm{DN}^{(4)}$ is determined in terms of $g^{\circ}$, it is an invariant of the Poincaré-Einstein structure. However it is not determined by the local data of the boundary conformal class $\boldsymbol{c}_{\Sigma}$, again see [16]. Knowledge of $\mathrm{DN}^{(4)}$ requires information about the global Poincaré-Einstein metric $g^{o}$. Our point is that, in four dimensions, the tensor $\stackrel{\circ}{\top} C_{\hat{n}(a b)}^{g}$ captures the range of the global, non-linear, Dirichlet-to-Neumann map for Poincaré-Einstein metrics introduced by Graham in [27].

A natural tensor, such as $\stackrel{\circ}{\top} C_{\tilde{n}(a b)}^{g_{r}}$, which depends on $g_{r}$ through three (and possibly fewer) derivatives with respect to a coordinate $r$ transverse to $\Sigma$, is an example of what will be termed a natural hypersurface tensor of transverse order 3 (see Section 3). The natural hypersurface tensor ${ }^{\circ} C_{\hat{n}(a b)}^{g_{r}}$ is special, in that it obeys the conformal covariance property of Equation (1.1). Broadly, our aim is to construct conformally covariant, natural hypersurface tensors of transverse order $d-1$ in even dimensions $d$, that capture the Dirichlet-to-Neumann data $\mathrm{DN}^{(d)}$.

In arbitrary even dimensions $d$, the coefficient $\left.\left(\mathcal{L}_{\frac{\partial}{\partial r}}\right)^{d-1} g_{r}\right|_{\Sigma}$ in the Fefferman-Graham expansion of a Poincaré-Einstein metric also changes covariantly when computed with respect to a different choice of boundary metric representative $\bar{g} \in \boldsymbol{c}_{\Sigma}$, but once again is not determined by the boundary data $\left(\Sigma, \boldsymbol{c}_{\Sigma}\right)$ [26]. It therefore defines an invariant of the Poincaré-Einstein structure which we term a (Poincaré-Einstein) Dirichlet-to-Neumann tensor $\mathrm{DN}^{(d)}$. When it exists (meaning when the data of $\left(\Sigma, \boldsymbol{c}_{\Sigma}\right) \hookrightarrow M^{d}$ uniquely determines a corresponding Poincaré-Einstein structure, for example for boundary metrics suitably close to the round sphere [29]), the map
$$\boldsymbol{c}_{\Sigma} \mapsto \mathrm{DN}^{(d)} \in \Gamma\left(\odot_{\mathrm{o}}^{2} T^{*} \Sigma[3-d]\right)$$
is termed the (Poincaré-Einstein) Dirichlet-to-Neumann map; see [27]. The linearization of this map is studied in [37]. The data of the boundary conformal class of metrics $\boldsymbol{c}_{\Sigma}$ and the tensor $\mathrm{DN}^{(d)}$ determines the formal Fefferman-Graham asymptotics of $g_{r}$ to all orders [16].

A first result here is the existence of a unique natural tranverse order 5 tensor for dimension 6 Poincaré-Einstein structures that captures the Dirichlet-to-Neumann tensor.

Theorem 1.1. Let $\left(M_{+}^{6}, g^{o}\right)$ be a Poincaré-Einstein structure with conformal infinity $\Sigma$. Then the unique natural transverse order 5 section of $\left.\stackrel{\circ}{\top} \odot{ }^{2} T^{*} M[-3]\right|_{\Sigma}$ that is an invariant of the Poincaré-Einstein structure is given, up to a non-zero constant multiple, for a choice of $g$ in the conformal class $\boldsymbol{c}$ determined by $g^{o}$, by
$$\stackrel{\circ}{\mathrm{VI}}_{a b}^{\mathrm{DN}}:=\stackrel{\circ}{\top}\left(\left(\nabla_{\hat{n}}+2 H\right) B_{a b}\right)-4 \bar{C}_{c(a b)} \bar{\nabla}^{c} H .$$
Furthermore
$$\mathrm{VI}^{\mathrm{DN}} \simeq \mathrm{DN}^{(6)} .$$
The detailed notions of transverse order and natural tensors are described in Section 3. In the above, $B_{a b}$ denotes the Bach tensor, $H$ is the mean curvature of the embedding $\Sigma \hookrightarrow(M, g)$,
and bars are used to denote objects intrinsic to the hypersurface $\Sigma$. Also, since $\mathrm{VI}^{\mathrm{DN}}$ and DN ${ }^{(6)}$ live in differing section spaces, namely that of $\left.\stackrel{\circ}{\top} \odot^{2} T^{*} M[-3]\right|_{\Sigma}$ and $\stackrel{\circ}{\top} \odot^{2} T^{*} \Sigma[-3]$ respectively, we have employed a notation $\simeq$. For $\left.A \in \stackrel{\circ}{\top} \odot^{2} T^{*} M[3-d]\right|_{\Sigma}$ and $B \in \stackrel{\circ}{\top} \odot^{2} T^{*} \Sigma[3-d]$, we say
$$A \simeq B$$
if when given any $\bar{g} \in \boldsymbol{c}_{\Sigma}$ and its corresponding Graham-Lee compactified metric $g_{r}$, then their respective evaluations obey
$$A^{g_{r}} \propto B^{\bar{g}} .$$
Note that, as bundles, $\left.\stackrel{\circ}{\top} \odot^{2} T^{*} M[-3]\right|_{\Sigma}$ and $\stackrel{\circ}{\top} \odot^{2} T^{*} \Sigma[-3]$ are in fact isomorphic. However, on the one hand, the tensor $\mathrm{DN}^{(6)}$ is defined invariantly with respect to choices of $\bar{g} \in \boldsymbol{c}_{\Sigma}$, while $\mathrm{VI}^{\mathrm{DN}}$ is invariant with respect to choices of $g \in \boldsymbol{c}$. Therefore we will use both notations, rather than invoking this isomorphism. Also strictly, since $\stackrel{\circ}{\top}^{\circ}$ includes restriction to $\Sigma$ in its definition, we could drop the moniker $\left.\right|_{\Sigma}$, but shall not do so for reasons of emphasis. Theorem 1.1 can be proved by exhaustion; key details are provided in Appendix A.

A main point of this article is to both give a simple characterization of these maps and, in particular, compute conformal hypersurface invariants, denoted $\frac{\circ}{d}^{\mathrm{DN}}$ and termed Dirichlet-to-Neumann hypersurface invariants, that each capture the Dirichlet-to-Neumann tensor $\mathrm{DN}^{(d)}$ for dimensions $d \geqslant 4$. Critically, Dirichlet-to-Neumann tensors are natural and of transverse order $d-1$; see Proposition 3.1. I.e., we shall establish higher dimensional analogs of Theorem 1.1

These results dovetail nicely with a seminal physics conjecture of Deser and Schwimmer [15] that was proved by Alexakis [2, 3], as well as work on renormalized volumes by Anderson [5] and Chang, Qing and Yang [11]. The latter work builds on the former ones to show that general even dimensional renormalized volumes are a sum of an Euler characteristic term plus an integral over $M_{+}$whose integrand is a natural local conformal invariant. In principle, following Anderson, even dimensional Dirichlet-to-Neumann tensors could be computed by varying renormalized volumes [5]. The latter are intimately related to $Q$-curvature invariants, whose complexity in terms of Riemannian invariants explodes in eight and higher dimensions [21], so a more powerful method is required. Luckily, tractor calculus methods, and in particular recent results on conformally invariant normal operators [22] and conformal fundamental forms [9], yield a rather simple solution to this problem. This is a main theorem:

Theorem 1.2. Let $\left(M_{+}^{d}, g^{o}\right)$ be an even-dimensional Poincaré-Einstein structure with conformal infinity $\Sigma$ and $d \geqslant 6$. For $d=6$, we have that
$$\stackrel{\circ}{\mathrm{VI}}^{\mathrm{DN}}=\bar{q}^{* \circ} \stackrel{\circ}{\top} \delta_{R} W .$$
Also, for $d \geqslant 8$, set
$$\stackrel{\circ}{\underline{d}}^{\mathrm{DN}}:=\bar{q}^{*} \stackrel{\circ}{\top} \delta_{\frac{d-6}{2}, \frac{d-4}{2}} W .$$
Then, for $d \geqslant 6$,
$$\stackrel{\circ}{\underline{d}}^{\mathrm{DN}} \simeq \mathrm{DN}^{(d)} .$$
Moreover, $\frac{\circ}{d}^{\mathrm{DN}}$ has leading transverse order term
$$\stackrel{\circ}{\top}: \nabla_{\hat{n}}^{d-5}: B_{a b},$$
and is the unique (up to a non-zero constant multiple) natural conformal hypersurface invariant of transverse order $(d-1)$ in $\Gamma\left(\left.\stackrel{\circ}{\top} \cdot{ }^{2} T^{*} M[3-d]\right|_{\Sigma}\right)$ determined by the Poincaré-Einstein structure. Thus it is the functional gradient of the renormalized volume along a path of Poincaré-Einstein metrics.

Here we have employed a normal ordering notation $: \nabla_{\hat{n}}^{\ell}:$ for $\hat{n}^{a_{1}} \cdots \hat{n}^{a_{\ell}} \nabla_{a_{1}} \cdots \nabla_{a_{\ell}}$ (the composition of operators $\nabla_{\hat{n}} \circ \nabla_{\hat{n}}$ is ill-defined) while the above tractor calculus notions and notations, including the $W$-tractor $W$, are explained in Section 2. The normal operator $\delta_{\frac{d-6}{2}, \frac{d-4}{2}}$ acting on the $W$-tractor is an example of those constructed in [22] and generalized to act on tractors in [7], see Equation (2.6).

It is interesting to note that in the context of minimal submanifolds of Poincaré-Einstein manifolds, there is a natural analog of the Dirchlet-to-Neumann map studied here [4, 36], that is again linked to variations of renormalized volume. We expect there to be a version of our construction applicable to that setting.

The recently developed conformal fundamental forms of [9, 7], designed for the study of conformal hypersurface embeddings $\Sigma \hookrightarrow(M, \boldsymbol{c})$, play a key rôle in establishing our main theorems for the case $d$ is even. Given such an embedding, a $k^{\text {th }}$ conformal fundamental form $\stackrel{\circ}{\underline{\bar{k}}}$ is any section of $\left.\stackrel{\circ}{\top} \odot^{2} T^{*} M[3-k]\right|_{\Sigma}$ that is a natural conformal hypersurface invariant of transverse order $k-1$ (in many contexts the integer $k$ is denoted by Roman numerals). In the cases $2 \leqslant k \leqslant d-1, k^{\text {th }}$ conformal fundamental forms are obstructions to a $d$-dimensional conformally compact manifold being an $\mathrm{APE}_{d-3}$ structure. This generalizes an older result [34, 19] that the hypersurface embedding $\Sigma \hookrightarrow\left(M, s^{2} g^{o}\right)$ (for any defining function $s$ ) of a Poincaré-Einstein structure $\left(M_{+}, g^{o}\right)$ is necessarily umbilic-so the trace-free second fundamental form $\stackrel{\circ}{\Pi}$ vanishes. In fact, vanishing of all conformal fundamental forms for $2 \leqslant k \leqslant \ell$ with $\ell \leqslant d-1$ is in fact a both necessary and sufficient condition for a conformally compact structure to be $\mathrm{APE}_{\ell-2}$. Moreover, we have denoted Dirichlet-to-Neumann hypersurface invariants by $\frac{\circ}{d}^{\mathrm{DN}}$ because they may be viewed as critical order conformal fundamental forms, whose job is no longer to measure obstructions to the Poincaré-Einstein condition but rather to extract Dirichlet-to-Neumann data.

In dimension four a conformally invariant fourth fundamental form is [9, 20]
$$\stackrel{\circ}{\mathrm{I}}_{a b}:=C_{\hat{n}(a b)}^{\top}-\bar{\nabla}^{c} W_{c(a b) \hat{n}}^{\top}+H W_{\hat{n} a b \hat{n}} .$$
For conformal embeddings arising from an $\mathrm{APE}_{1}$ structure, the conformal hypersurface invariant IV restricts to IV ${ }^{\mathrm{DN}} \simeq \mathrm{DN}^{(4)}$. Importantly, unlike the tensor $\mathrm{DN}^{(4)}$, the fourth fundamental form is a natural conformal hypersurface invariant for any conformal hypersurface embedding, rather than only those embeddings arising as the boundary of a Poincaré-Einstein structure. An interesting question is whether there are $d^{\text {th }}$ conformal fundamental forms for more general conformal embeddings.

The case of odd dimensional Poincaré-Einstein structures is subtle. Firstly, no Andersontype formula for the renormalized volume is available, and in general this quantity depends on a choice of boundary metric representative $\bar{g} \in \boldsymbol{c}_{\Sigma}$. Concordantly, there is an obstruction to smoothness of the Fefferman-Graham expansion termed the obstruction tensor [16]. For general boundary conformal structures, the $r^{d-1}$ coefficient in the Fefferman-Graham expansion of a Poincaré-Einstein metric does not define a tensor-density valued in $\odot_{0}^{2} T^{*} \Sigma[3-d]$ independently of the choice of $\bar{g} \in \boldsymbol{c}_{\Sigma}$. Indeed the quantity $\left(\mathcal{L}_{\frac{\partial}{\partial r}}\right)^{d-1} g_{r}$ may not extend smoothly to the boundary $\Sigma$. When the Fefferman-Graham obstruction tensor vanishes we may then at least define $\mathrm{DN}^{(d)}:=\left.\left(\mathcal{L}_{\frac{\partial}{\partial r}}\right)^{d-1} g_{r}\right|_{\Sigma}$ for $d$ odd. However, this does not in general transform conformally covariantly as one changes the choice of boundary metric $\bar{g}$ required to determine the Graham-Lee compactified metric. But, when the boundary $\left(\Sigma, \boldsymbol{c}_{\Sigma}\right)$ is conformally flat, we can instead define a canonical section $\underline{\bar{d}}^{\mathrm{D} \mathrm{N}^{\mathrm{b}}}$ of $\left.\stackrel{\circ}{\top} \odot{ }^{2} T^{*} M[3-d]\right|_{\Sigma}$ which is an invariant of the Poincaré-Einstein structure.

Theorem 1.3. Let $\left(M_{+}^{5}, g^{o}\right)$ be a Poincaré-Einstein structure with (locally) conformally flat conformal infinity $\Sigma$. Then the unique (up to a non-zero constant multiple) natural transverse order 4 section of $\left.\stackrel{\circ}{\top}_{\odot} \odot_{0}^{2} T^{*} M[-2]\right|_{\Sigma}$ that is an invariant of the Poincaré-Einstein structure, is given, for a choice of $g \in \boldsymbol{c}$, by
$$\stackrel{\circ}{\mathrm{V}}^{\mathrm{DN}^{b}}:=B_{(a b) \circ}^{\top} .$$
Moreover, evaluated on the Graham-Lee compactified metric $g_{r}$ corresponding to a (locally) flat boundary metric,
$$\stackrel{\circ}{\mathrm{V}}^{\mathrm{DN}^{\mathrm{b}}} \simeq \mathrm{DN}^{(5)}$$
The above is an odd dimensional analog of Theorem 1.1 and the following is that of Theorem 1.2

Theorem 1.4. Let $\left(M_{+}^{d}, g^{o}\right)$ be an odd-dimensional Poincaré-Einstein structure with a (locally) conformally flat conformal infinity and $d \geqslant 5$. Then if $d=5$, we have that
$$\stackrel{\circ}{\mathrm{V}}^{\mathrm{DN}^{b}}=\stackrel{\circ}{\top} \circ q^{*}\left(\left.\left[\hat{n}^{a}: \nabla_{\hat{n}}: F_{a b}{ }^{A}{ }_{B}\right]\right|_{\Sigma}\right) .$$
For $d \geqslant 7$, set
$$\underline{\bar{d}}^{\mathrm{DN}^{\mathrm{b}}}:=\stackrel{\circ}{\top} \circ q^{*}\left(\left.\left[\hat{n}^{a}: \nabla_{\hat{n}}^{d-4}: F_{a b}{ }^{A} B\right]\right|_{\Sigma}\right) .$$
Then, evaluated on the Graham-Lee compactified metric $g_{r}$ corresponding to a (locally) flat boundary metric,
$$\underline{\circ}^{\mathrm{DN}^{\mathrm{b}}} \simeq \mathrm{DN}^{(d)} .$$
Moreover, $\mathrm{DN}^{(d)}:=\left.\left(\mathcal{L}_{\frac{\partial}{\partial r}}\right)^{d-1} g_{r}\right|_{\Sigma}$ defines an element of $\Gamma\left(\odot_{\diamond}^{2} T^{*} \Sigma[3-d]\right)$.
The article is structured as follows. Section 2 introduces the main technologies we require for handling conformal geometries and hypersurfaces embedded therein (tractor and hypersurface cognoscenti might safely leapfrog this section). Our main results are proved in Section 3.
1.1. Conventions. Throughout we take $M$ to be a smooth, for simplicity oriented, $d \geqslant 3$ -dimensional manifold, and throughout unless otherwise specified, all structures are taken to be smooth. The canonical $d$-form determined by a metric $g$ is denoted $\mathrm{dVol}^{g}$ and may be used when integrating over $M$; this is normalized such that in local coordinates it gives the measure $\sqrt{\operatorname{det} g} \mathrm{~d} x^{1} \cdots \mathrm{~d} x^{d}$ where $g$ here denotes the matrix of metric components. The tangent, cotangent, and tensor bundles of $M$ are denoted, respectively, by $T M, T^{*} M$, and $\mathbb{T} M$. Sections are often handled using an abstract index notation; for example $t^{a b}{ }_{c} \in \Gamma\left(\otimes^{2} T M \otimes T^{*} M\right)$, and the contraction $v(\omega)$ of a vector field $v$ and one-form field $\omega$ is denoted by $v^{a} \omega_{a}=v_{\omega}=\omega_{v} \in C^{\infty} M$. The inverse of a metric $g_{a b} \in \Gamma\left(\odot^{2} T^{*} M\right)$ is denoted $g^{a b}$ and can be used to "raise indices" in the standard way, for example $\omega^{a}=g^{a b} \omega_{b}$. The symmetric trace-free part of a tensor $X_{a b}$ is denoted $X_{(a b) \circ}:=\frac{1}{2}\left(X_{a b}+X_{b a}\right)-\frac{1}{d} g_{a b} X_{c}{ }^{c} \in \Gamma\left(\odot^{2} T^{*} M\right)$. Also, for a tensor $X_{a b c \ldots}$, we denote $|X|_{g}^{2}:=X_{a b c \cdots} X^{a b c \cdots}$. While we work solely in Riemannian signature, many results carry over mutatis mutandis to indefinite metric signatures.

The Levi-Civita connection of a metric is denoted $\nabla^{g}$ (or simply ∇ when context lends clarity; we will similarly drop the superscript $g$ on other Riemannian tensors). The Riemann tensor $R$ of $\nabla^{g}$ is defined by
$$(R(x, y) z)^{a}:=\left(\left(\nabla_{x} \nabla_{y}-\nabla_{y} \nabla_{x}-\nabla_{[x, y]}\right) z\right)^{a}=x^{c} y^{d} R_{c d}{ }^{a}{ }_{b} z^{b}=R_{x y}{ }^{a}{ }_{z} \in \Gamma(T M),$$
where $x, y, z \in \Gamma(T M)$ and $[x, y]$ is their Lie bracket. The Weyl, Cotton and Bach tensors are given by
$$\begin{aligned}
W_{a b c d} & :=R_{a b c d}-g_{a c} P_{b d}+g_{a d} P_{b c}+g_{b c} P_{a d}-g_{b d} P_{a c}, \\
C_{a b c} & :=\nabla_{a} P_{b c}-\nabla_{b} P_{a c}, \\
B_{a b} & :=\Delta P_{a b}-\nabla^{c} \nabla_{a} P_{b c}+P^{c d} W_{a c b d},
\end{aligned}$$
where the Schouten tensor $P_{a b}$ and its trace $J=P_{a}{ }^{a}$ are defined by the equation Ric $_{a b}:=$ $R_{c a}{ }^{c}{ }_{b}=(d-2) P_{a b}+g_{a b} J$, and $\Delta:=\nabla^{a} \nabla_{a}$ is the (negative) rough Laplacian. We will often place a symbol above an equals sign to qualify its domain of applicability, for example $A \stackrel{\Sigma}{=} B$ implies equality along the hypersurface $\Sigma$. We also rely on the canonical isomorphism between the projection of the bulk tangent bundle along a hypersurface and the hypersurface tangent bundle to employ the same abstract indices for hypersurface tensors as for their bulk counterparts.

\section*{2. Conformal Hypersurface Calculus}

A conformal manifold $(M, \boldsymbol{c})$ is a smooth manifold equipped with a conformal class of metrics $\boldsymbol{c}$, meaning that if $g, g^{\prime} \in \boldsymbol{c}$ then $g^{\prime}=\Omega^{2} g$ for some $0<\Omega \in C^{\infty} M$. A conformal hypersurface embedding $\Sigma \hookrightarrow(M, \boldsymbol{c})$ is a conformal manifold equipped with a smoothly embedded codimension 1 submanifold $\Sigma$. The data $(M, \boldsymbol{c})$ may be viewed as a ray subbundle of $\odot^{2} T^{*} M$ and in turn as an $\mathbb{R}_{+}$-principal bundle. The group action $t \mapsto s^{-w} t$ on $t \in \mathbb{R}$ (corresponding to
$g(p) \mapsto s^{2} g(p)$ ) for $w \in \mathbb{R}$ and $s \in \mathbb{R}_{+}$determines an associated line bundle $\mathcal{E} M[w]$ over $M$ called a weight $w$ conformal density bundle. Given any vector bundle $\mathcal{V} M$ over $M$, we denote $\mathcal{V} M[w]:=\mathcal{V} M \otimes \mathcal{E} M[w]$. It is also useful to define the operator $\underline{w}$ which acts by multiplication by $w$ on tensor-valued densities $\Phi$ of weight $w$, so that $\underline{w} \Phi=w \Phi$.

The tautological section $\boldsymbol{g} \in \Gamma\left(\odot^{2} T^{*} M[2]\right)$ determined by $\boldsymbol{c}$ is called the conformal metric. We may equally well label a conformal manifold $(M, \boldsymbol{c})$ by the pair $(M, \boldsymbol{g})$. The tractor bundle is defined by (see [13])
$$\mathcal{T} M:=\left(\bigsqcup_{g \in c} \mathcal{T}^{g} M\right) / \sim,$$
where
$$\mathcal{T}_{g} M:=\mathcal{E} M[1] \oplus T^{*} M[1] \oplus \mathcal{E} M[-1] .$$
The equivalence relation ~ on direct sum bundles is defined by the following relation on sections
$$\Gamma\left(\mathcal{T}_{g^{\prime}}\right) \ni\left(\tau, \mu+\Upsilon \tau, \rho-\Upsilon . \mu-\frac{1}{2} \Upsilon^{2} \tau\right) \sim(\tau, \mu, \rho) \in \Gamma\left(\mathcal{T}_{g}\right),$$
for $\Upsilon:=\mathrm{d} \log \Omega$. Here $\Upsilon . \mu:=\boldsymbol{g}^{-1}(\Upsilon, \mu)$ and $\Upsilon^{2}:=\boldsymbol{g}^{-1}(\Upsilon, \Upsilon)$. There is a canonical section $X$ of $\mathcal{T} M[1]$ given by
$$(0,0,1) \in \mathcal{T}_{g} M[1],$$
for any $g \in \boldsymbol{c}$, which is termed the canonical tractor. Also, there is an indefinite, conformally invariant, bundle metric $h \in \Gamma\left(\odot^{2} \mathcal{T}^{*} M\right)$ given, in an obvious matrix notation, by
$$\left(\begin{array}{ccc}
0 & 0 & 1 \\
0 & \boldsymbol{g}^{-1} & 0 \\
1 & 0 & 0
\end{array}\right),$$
and termed the tractor metric. Sections $T \in \Gamma(\mathcal{T} M)$ can be denoted in an abstract index notation by $T^{A}$, so the tractor metric is then $h_{A B}$ and will be used to raise and lower tractor indices in the standard way. For example, $h_{A B} X^{A} X^{B}$ is the zero section of $\mathcal{E} M[2]$.

On an oriented conformal hypersurface $\Sigma \hookrightarrow(M, \boldsymbol{c})$, there is a canonical section $N$ of $\left.\mathcal{T} M\right|_{\Sigma}$ given, for any $g \in \boldsymbol{c}$, by
$$(0, \hat{n},-H) \in \mathcal{T}_{g} M,$$
where $\hat{n}$ is the inward unit conormal of $g$ and $H$ its mean curvature (i.e., the average of the eigenvalues of the second fundamental form). This section is called the normal tractor [6] and is key for the study of conformally embedded hypersurfaces. The normal tractor and tractor metric allow us to define the tractor analog of the projection operator $\stackrel{\circ}{\top}$ in the obvious way; we recycle the same notation for this. There is a particularly useful relationship between $N$ and defining functions for $\Sigma$, but we first must introduce further tractor technology.

The tractor bundle $\mathcal{T} M$ comes equipped with a canonical connection $\nabla^{\mathcal{T}}$, termed the tractor connection, defined for any $g \in \boldsymbol{c}$, and $T \stackrel{\tau_{g}}{:=}(\tau, \mu, \rho) \in \Gamma\left(\mathcal{T}_{g} M\right)$ by
$$\nabla^{\mathcal{T}} T \stackrel{\mathcal{T}_{g}}{=}\left(\nabla \tau-\mu, \nabla \mu+P^{g} \tau+\boldsymbol{g} \rho, \nabla \rho-P^{g} \cdot \mu\right) .$$
We will adorn equal signs with the symbol $\tau_{g}$ to indicate that we have used the metric $g$ to decompose sections of (tensor products of) the tractor bundle into a direct sum of density valued sections according to Equation (2.1).

The curvature of $\nabla^{\mathcal{T}}$ is denoted by $F$, or $F_{a b}{ }^{A}{ }_{B}$ in an abstract index notation. In the above $P^{g} \cdot \mu:=P\left(\boldsymbol{g}^{-1}(\mu, \cdot), \cdot\right)$. Also, in the above, ∇ is the Levi-Civita connection $\nabla^{g}$ of $g$. If follows from our discussion of conformal densities that, given $v \in \Gamma(T M)$ and a weight $w$ density $\varphi=[g ; f]$, one has $\nabla_{v}^{g} \varphi=[g,(\mathrm{~d} f)(v)]$. Note that a conformal density $0<\tau \in \Gamma(\mathcal{E} M[1])$ defines a metric $g=\tau^{-2} \boldsymbol{g} \in \boldsymbol{c}$ and conversely a metric $g \in \boldsymbol{c}$ determines a strictly positive density $\tau_{g}:=\left(\mathrm{dVol}^{\boldsymbol{g}} / \mathrm{dVol}^{g}\right)^{\frac{1}{d}} \in \Gamma(\mathcal{E} M[1])$. We will term such a scale true. Thus, given $g \in \boldsymbol{c}$, we can define a canonical section
$$Z_{a}^{A}:=\tau_{g} \nabla_{a}^{\mathcal{T}}\left(\tau_{g}^{-1} X^{A}\right) \in \Gamma\left(T^{*} M \otimes \mathcal{T} M[1]\right) .$$

Tractor tensor bundles are defined in the standard way and sections of such can also be denoted by an abstract index notation, for example $T^{A B}{ }_{C} \in \Gamma\left(\otimes^{2} \mathcal{T} M \otimes \mathcal{T}^{*} M\right)$; we will often label a generic tractor tensor bundle by $\mathcal{T}^{\Phi} M$ (in general $\Phi$ is some representation of $S O(d+1,1)$ ). Then given a tractor $T \in \Gamma\left(\mathcal{T}^{\Phi} M[w]\right)$, the Thomas-D operator
$$D: \Gamma\left(\mathcal{T}^{\Phi} M[w]\right) \rightarrow \Gamma\left(\mathcal{T} M \otimes \mathcal{T}^{\Phi} M[w-1]\right),$$
is defined [6] acting on $T$, for any $g \in \boldsymbol{c}$, by
$$D T=\left(w(d+2 w-2) T,(d+2 w-2) \nabla^{\mathcal{T}} T,-\Delta^{\mathcal{T}} T-w \boldsymbol{g}^{a b} P_{a b}^{g} T\right) \in \Gamma\left(\mathcal{T}_{g} M \otimes \mathcal{T}^{\Phi} M[w-1]\right),$$
where $\Delta^{\mathcal{T}}:=\boldsymbol{g}^{a b} \nabla_{a}^{\mathcal{T}} \nabla_{b}^{\mathcal{T}}$ is the tractor Laplacian and $\nabla^{\mathcal{T}}$ denotes the tractor-Levi-Civita coupled connection. When $w \neq 1-\frac{d}{2}$, we define $\hat{D}:=(d+2 w-2)^{-1} D$.

There is a useful tractor analog of the Weyl tensor: the $W$-tractor is a canonical section of $\otimes^{4} \mathcal{T}^{*} M[-2]$, with Weyl-tensor symmetries, defined in dimensions $d \geqslant 5$ for any choice of $g \in \boldsymbol{c}$, by
$$W^{A B C D} \stackrel{\tau_{g}}{=} Z_{a}^{A} Z_{b}^{B} Z_{c}^{C} Z_{d}^{D} W^{a b c d}+4 Z_{a}^{[A} Z_{b}^{B]} Z_{c}^{[C} X^{D]} C^{a b c}+\frac{4}{d-4} Z_{a}^{[A} X^{B]} Z_{c}^{[C} X^{D]} B^{a c},$$
where $W_{a b c d}, C_{a b c}$ and $B_{a b}$ are, respectively, the Weyl, Cotton and Bach tensors of the metric $g$. Note that
$$F_{a b}{ }^{C D}=Z_{a}^{A} Z_{b}^{B} W_{A B}{ }^{C D}=Z_{c}^{C} Z_{d}^{D} W_{a b}{ }^{c d}+2 Z_{c}^{[C} X^{D]} C_{a b}{ }^{c} ;$$
see [18, 21, 9] for further details. Note that some authors define a $W$-tractor in dimensions $d \geqslant 5$ by multiplying the above definition by a factor $(d-4)$ so that it is defined in all dimensions $d \geqslant 3$.

Indeed there is a general notion termed the projecting part of a tractor, of which we only need special cases. In particular for a tractor $T \in \Gamma\left(\mathcal{T}^{\otimes 4} M[w]\right)$, given in a choice of $g \in \boldsymbol{c}$ by
$$T^{A B C D} \stackrel{\tau_{g}}{=} 4 Z_{a}^{[A} X^{B]} Z_{c}^{[C} X^{D]} t^{a c},$$
such that $t^{a b} \neq 0$, we can extract the projecting part $q^{*}\left(T^{A B C D}\right):=\left[g ; t_{a b}\right] \in \Gamma\left(\otimes^{2} T^{*} M[w]\right)$. Similarly for a tractor $T^{A B} \stackrel{\tau_{g}}{=} 2 Z_{b}^{[A} X^{B]} t^{b}$, we have that $q^{*}\left(T^{A B}\right)=\left[g ; t^{b}\right]$.

Given a conformal hypersurface embedding $\Sigma \hookrightarrow(M, \boldsymbol{c})$, we call $\sigma \in \Gamma(\mathcal{E} M[1])$ a defining density if $\sigma=s \tau$ for some $0<\tau \in \Gamma(\mathcal{E} M[1])$ and $s$ a defining function for $\Sigma$. Then we may define a metric
$$g^{o}=\sigma^{-2} \boldsymbol{g}$$
on $M_{+}=M \backslash \Sigma$. Because $g^{o}$ is not defined along $\Sigma=\partial M_{+}$, we refer to it as a singular metric. An important theorem of [19] is that $\left(M_{+}, g^{o}\right)$ is Poincaré-Einstein precisely when the scale tractor $I_{\sigma}:=\hat{D} \sigma$ is parallel with respect to the tractor connection $\nabla^{\mathcal{T}}$ and normalized, i.e.,
$$\nabla^{\mathcal{T}} I_{\sigma}=0=I_{\sigma}^{2}-1,$$
where $I_{\sigma}^{2}:=h\left(I_{\sigma}, I_{\sigma}\right)$. This allows us to label a Poincaré-Einstein structure by the data $(M, \boldsymbol{g}, \sigma)$, where the singular Einstein metric $g^{o}=\sigma^{-2} \boldsymbol{g}$. Note that, as was discussed in the introduction, the $k$ th order asymptotics of this data can be labeled by a representative triple ( $M^{d}, g_{k}, s$ ) for which $\boldsymbol{c}_{k}=\left[g_{k}\right]$ and $\sigma=\left[g_{k} ; s\right]$, and such that $\left(M_{+}, \sigma^{-2} g_{k}\right)$ is $\mathrm{APE}_{k}^{d}$. We recall that for $\mathrm{APE}_{k \geqslant 0}^{d}$ structures, the normal tractor to $\Sigma$ is given by [19]
$$N=\left.I_{\sigma}\right|_{\Sigma} .$$

The final piece of conformal hypersurface technology that we need is a generalization of the scalar normal operators of [22]. For the simplest of these, recall that, the conformal-Robin operator $\delta_{R}: \Gamma(\mathcal{E} M[w]) \rightarrow \Gamma(\mathcal{E} \Sigma[w-1])$ is defined along $\Sigma$, for any $g \in \boldsymbol{c}$, and $[g ; f] \in \Gamma(\mathcal{E} M[w])$ by [12]
$$\delta_{R} f=\left.\left(\nabla_{\hat{n}}-w H^{g}\right) f\right|_{\Sigma} .$$
This generalizes directly to tractors by replacing the Levi-Civita connection in the above by its tractor-coupled analog.

If $s$ is any defining function for $\Sigma$, we say that an operator $\mathrm{L}:\left.\Gamma\left(\mathcal{T}^{\Phi} M[w]\right) \rightarrow \Gamma\left(\mathcal{T}^{\Phi^{\prime}} M\left[w^{\prime}\right]\right)\right|_{\Sigma}$ has transverse order $k$ if
$$\mathrm{L}\left(s^{k+1} U\right)=0 \neq \mathrm{L}\left(s^{k} V\right),$$
for every smooth tractor $U$ and some smooth tractor $V$ in its domain. Clearly $\delta_{R}$ has transverse order 1. The normal operators $\delta_{k}$ defined by
$$\Gamma\left(\mathcal{T}^{\Phi} M[w]\right) \ni T \stackrel{\delta_{k}}{\longmapsto}:\left(N^{A} D_{A}\right)^{k}: T:=\left.N^{A_{k}} \cdots N^{A_{1}} D_{A_{1}} \cdots D_{A_{k}} T \in \Gamma\left(\mathcal{T}^{\Phi} M[w-k]\right)\right|_{\Sigma},$$
have transverse order $k$ for generic weights $w \notin\left\{\frac{2 k-d}{2}, \frac{2 k-1-d}{2}, \ldots, \frac{k+1-d}{2}\right\}[22]$. An improvement of these operators acting on densities was also produced in [22, Theorem 4.16], where the set of weights for which the transverse order is less than $k$ was shrunk. In [7, Theorem 3.4], these improved operators were generalized to act on arbitrary tractors. In particular, for even $d$ and integers $0<J$ and $0<k<d / 2$, it was shown that they give maps
$$\delta_{J, k}:\left.\Gamma\left(\mathcal{T}^{\Phi} M[w]\right) \rightarrow \Gamma\left(\mathcal{T}^{\Phi} M[w-k-J]\right)\right|_{\Sigma},$$
with transverse order $J+k$ also at the special weights $w=k-d / 2$. Importantly, these existence proofs are both constructive and algorithmic.

\section*{3. Dirichlet-to-Neumann Tensors}

Any Poincaré-Einstein structure $\left(M_{+}, g^{o}\right)$ determines a conformal embedding $\Sigma \hookrightarrow\left(\overline{M_{+}}, \boldsymbol{c}\right)$ of its boundary, where $\boldsymbol{c}$ is the conformal class of metrics on $M:=\overline{M_{+}}$determined by $g^{o}$. Moreover, this embedding must be umbilic [34, 19], so the corresponding trace-free second fundamental form $\stackrel{\circ}{\Pi}=0$. This tensor is an example of a natural conformal hypersurface invariant (see below). In fact, a slew of other natural conformal hypersurface invariants are also forced to vanish by the Einstein condition; this underlies the conformal fundamental forms construction of [9].

We next need to define natural conformal hypersurface invariants. First recall that a natural Riemannian invariant on a Riemannian manifold is any tensor-valued polynomial made from the metric, its inverse, the Riemann tensor, and covariant derivatives of the latter. Strictly, this is the class of "even invariants", meaning those that are unaffected by a change of orientation. It is clear that this type of invariant is all that will be required in our context. This definition extends in the obvious way to a Riemannian manifold equipped with any set of scalar functions. Extending these to natural conformal hypersurface invariants is discussed in detail in [25, Section 2.4]. Here we are interested in the same notion with some restrictions.

Consider triples ( $M, \boldsymbol{g}, \sigma$ ), where $\sigma$ is a defining density for a conformally embedded hypersurface $\Sigma \hookrightarrow(M, \boldsymbol{c})$. For any triple $(M, \boldsymbol{g}, \sigma)$, now consider a representative pair $(g, s)$ for $\sigma$. Then we can construct the natural Riemannian invariants $i(g, s)$ built from the metric $g$ and the scalar function $\hat{s}:=s /|\mathrm{d} s|_{g}$ (in some collar neighborhood of $\Sigma$ where the denominator is non-vanishing), and then restrict these to $\Sigma$. In turn we consider the special class of such objects $\left.\left[g ;\left.i(g, s)\right|_{\Sigma}\right] \in \Gamma(\mathbb{T} M)\right|_{\Sigma}$ for which
$$\left.\bar{\Omega}^{-w} i\left(\Omega^{2} g, \Omega s\right)\right|_{\Sigma}=\left.i(g, s)\right|_{\Sigma} \quad \text { and }\left.\quad i\left(g, e^{\varpi} s\right)\right|_{\Sigma}=\left.i(g, s)\right|_{\Sigma},$$
where $0<\Omega \in C^{\infty} M \ni \varpi, \bar{\Omega}=\left.\Omega\right|_{\Sigma}$ and $w \in \mathbb{R}$. The equivalence class $\left[g,\left.i(g, s)\right|_{\Sigma}\right]$ defines a (weight $w$ ) natural conformal hypersurface invariant. Upon dropping the conformal requirement imposed by the first equality displayed above, we employ the terminology natural Riemannian hypersurface invariant.

We use the same language to also refer to the larger class of natural Riemannian hypersurface invariants $i(g, s)$ that may only obey the requirements above when restricting to the subset of triples $(M, \boldsymbol{g}, \sigma)$ such that $\left(M_{+}, \sigma^{-2} \boldsymbol{g}\right)$ is Poincaré-Einstein. An example of such a natural conformal hypersurface invariant for Poincaré-Einstein structures is $\left.\left.\stackrel{\circ}{\top} C_{\hat{n}(a b)}\right|_{\Sigma} \in \Gamma\left(\stackrel{\circ}{\top} \odot{ }^{2} T^{*} M[-1]\right)\right|_{\Sigma}$ (see [20, 9]). For brevity, we often refer to such tensors as "natural" and list the relevant section spaces and underlying structures. In some contexts we additionally require that the boundary $(\Sigma, \bar{c})$ is conformally Einstein or conformally flat.

We employ the terminology preinvariant for any representative $i(g, s)$ of a natural conformal hypersurface invariant $I$ (see [25]). Examples of natural conformal hypersurface invariants include the unit conormal $\hat{n}$ and trace-free second fundamental form İ. Sample preinvariants for these are, respectively,
$$\mathrm{d} \hat{s}=\mathrm{d}\left(s /|\mathrm{d} s|_{g}\right), \quad\left(\mathrm{Id}-\mathrm{d} \hat{s} \otimes g^{-1}(\mathrm{~d} \hat{s}, \cdot)\right) \circ \nabla \mathrm{d} \hat{s} .$$

Consider a conformal hypersurface invariant $I$ that is represented by $i(g, s)$ and obeys
$$\left.i\left(g+s^{k} h, s\right)\right|_{\Sigma} \neq\left. i(g, s)\right|_{\Sigma}=\left.i\left(g+s^{k+1} h^{\prime}, s\right)\right|_{\Sigma}, \quad k \in \mathbb{Z}_{\geqslant 0},$$
for some $h$ and any $h^{\prime} \in \Gamma\left(\odot^{2} T^{*} M\right)$ such that $g+s^{k} h, g+s^{k+1} h^{\prime}$ are metrics on $M$. The number $k$ does not depend on the choice of $(g, s)$ used to construct $I$. Thus (in line with definition of Equation (2.4)) we then say that $I$ has transverse order $k$.

In fact, Dirichlet-to-Neumann tensors are natural hypersurface invariants:
Proposition 3.1. Let $\left(M_{+}^{d}, g^{o}\right)$ be a Poincaré-Einstein structure. In the case that $d$ is odd, also assume that the boundary $\Sigma$ is conformally flat. Then the Dirichlet-to-Neumann tensor $\mathrm{DN}^{(d)}$ is a natural hypersurface invariant.

Proof. First recall that, given a Riemannian hypersurface embedding $\Sigma \hookrightarrow(M, g)$ and any defining function $s$, it is always possible to improve $s$ to $s_{1}=f s$ such that
$$\left|d s_{1}\right|_{g}^{2}=1+\mathcal{O}\left(s^{\ell}\right)$$
for any integer $\ell$, and the smooth function $f$ is some local formula in terms of $s$ and $g$; see [25] (this is an asymptotic solution to the well-known eikonal problem). To (arbitrarily) high order, the improved defining function $s_{1}$ gives the geodesic distance to the hypersurface.

Now pick $\bar{g} \in \boldsymbol{c}_{\Sigma}$. This determines the corresponding Graham-Lee compactified metric $g_{r}$. Then applying the above eikonal construction to $g_{r}$, starting with any defining function $s$, at least to sufficiently high order for our purposes, we obtain an asymptotic formula $s_{\mathrm{GL}}^{(\ell)}$ for the Graham-Lee defining function $s_{\mathrm{GL}}$ as a natural formula in terms of $s$ and $g_{r}$ (this follows directly from the construction and uniqueness statement given in [25, Proposition 2.5]). Moreover, by picking large enough $\ell$, we have that $\hat{s}=s_{\mathrm{GL}}^{(\ell)} /\left|\mathrm{d} s_{\mathrm{GL}}^{(\ell)}\right|_{g_{r}}$ equals the geodesic normal coordinate function $r$ to any desired order. Thus we can ignore higher order corrections in what follows.

Now recall that given a vector $x \in \Gamma(T M)$ and a tensor $T \in \Gamma\left(\odot^{2} T^{*} M\right)$, one has
$$\mathcal{L}_{x} T_{a b}=x^{c} \nabla_{c} T_{a b}+\left(\nabla_{a} x^{c}\right) T_{c b}+\left(\nabla_{b} x^{c}\right) T_{a c} .$$
Note that the vector $\frac{\partial}{\partial r}$ determined by the normal form of the Graham-Lee compactified metric is natural because it solves the equation $g_{r}\left(\frac{\partial}{\partial r}, \cdot\right)=\mathrm{d} s_{\mathrm{GL}}$ and $s_{\mathrm{GL}}$ has a natural formula in terms of $s$. Because $\hat{s}=r$, we have $\mathcal{L}_{\frac{\partial}{\partial r}} g_{r}=2 \nabla^{g_{r}} \mathrm{~d} \hat{s}$. Similarly, higher Lie derivatives with respect to the vector $\frac{\partial}{\partial r}$ can also be expressed naturally in terms of $\mathrm{d} \hat{s}$, the metric $g_{r}$, its inverse and covariant derivatives. Hence we have by now expressed such Lie derivatives of the Graham-Lee compactified metric $g_{r}$ as a natural formula in $s$ and the metric $g_{r}$. The result follows upon remembering that for Poincaré-Einstein structures, the tensor $\mathrm{DN}^{(d)}$ is defined through $d-1$ Lie derivatives of the Graham-Lee compactified metric $g_{r}$ with respect to the vector $\frac{\partial}{\partial r}$. \(\square\) \(\square\)
3.1. $T$-curvatures. Before proving our main results we need the notion of a $T$-curvature and a result of [22]. Recall that the mean curvature $H^{g}$ behaves as follows under conformal rescalings
$$H^{\Omega^{2} g}=\Omega^{-1}\left(H^{g}+\delta_{1} \log \Omega\right),$$
where $\delta_{1}=\delta_{R}$ is the first of the sequence of operators defined in Equation (2.5) in the case where $w=0$ and $\Phi$ is the trivial representation (and also in the scale $g$ ). Each $T$-curvature is a higher order generalization of the mean curvature to a natural Riemannian hypersurface invariant $T_{k}^{g}$ with conformal variation
$$T_{k}^{\Omega^{2} g}=\Omega^{-k}\left(T_{k}^{g}+N_{k} \log \Omega\right),$$
where $N_{k}$ is any conformally invariant hypersurface operator with differential order $k$ and with leading symbol containing a term arising from an operator proportional to $: \nabla_{\hat{n}}^{k}$ : for some $k \geqslant 2$. The integer $k$ equals the transverse order of the $T$-curvature $T_{k}$, so we shall call $T_{k}$ a $T$-curvature of order $k$. For example, $T_{1}=H$ is the (up to an overall non-zero coefficient) first $T$-curvature and the scalar
$$T_{2}:=P_{\hat{n} \hat{n}}-\frac{1}{2} H^{2}-\frac{1}{d-3} \bar{J}$$
is also a $T$-curvature [22, Section 7.1]. Existence of $T$-curvatures of arbitrary order on any evendimensional conformal manifold with boundary was established in [22, Theorem 4.16]. Moreover, in that work, the following result was proved:

Proposition 3.2 ([22] Proposition 6.15). Let $\Sigma \hookrightarrow\left(M^{d}, \boldsymbol{c}\right)$ be a conformal hypersurface embedding with $d$ even. Then, for any finite set of $T$-curvatures $\left\{T_{1}^{g}, \ldots, T_{k}^{g}\right\}$, there exists a metric $g^{\prime} \in \boldsymbol{c}$ such that
$$T_{i}^{g^{\prime}}=0, \quad \forall i \in\{1, \ldots, k\} .$$

An example of how we plan to use the above proposition is as follows: The usual definition of the dimension $d \geqslant 4$ Fialkow tensor is (for some choice of $g \in \boldsymbol{c}$ )
$$F_{a b}:=P_{a b}^{\top}-\bar{P}_{a b}+H \stackrel{\circ}{\Pi}_{a b}+\frac{1}{2} \bar{g}_{a b} H^{2} \stackrel{\Sigma}{=} \frac{1}{d-3}\left(W_{\hat{n} a \hat{n} b}+\stackrel{\circ}{\Pi}_{a c} \stackrel{\circ}{\Pi}_{b}^{c}-\frac{1}{2(d-2)} \bar{g}_{a b}|\stackrel{\circ}{\Pi}|^{2}\right) .$$
The second equality above is a standard hypersurface identity establishing that the Fialkow tensor defines a conformally invariant section of $\left.\stackrel{\circ}{\top} \odot^{2} T^{*} M[0]\right|_{\Sigma}$. This equation can be equivalently rewritten as
$$R_{\hat{n} a \hat{n} b}^{\top} \stackrel{\Sigma}{=} \bar{P}_{a b}-\frac{1}{d-3} \bar{g}_{a b} \bar{J}+(d-2) F_{a b}-\stackrel{\circ}{\Pi}_{a c} \stackrel{\circ}{\Pi}_{b}^{c}+\frac{1}{2(d-2)} \bar{g}_{a b}|\stackrel{\circ}{\Pi}|^{2}-H \stackrel{\circ}{\Pi}_{a b}+\bar{g}_{a b} T_{2} .$$
Importantly both the trace-free Fialkow tensor and trace-free second fundamental form vanish for APE structures of sufficiently high order; they are the first two conformal fundamental forms discussed above (note also that the trace $F_{a}{ }^{a}=\frac{1}{2(d-2)}|\stackrel{\circ}{\Pi}|^{2}$ ). Thus for $\mathrm{APE}_{1}$ structures, the right hand side of Equation (3.2) reduces to the sum of an intrinsic tensor plus a $T$-curvature. Hence Proposition 3.2 can be used to establish that there exists a metric in the conformal class $\boldsymbol{c}$ such that $R_{\hat{n} a \hat{n} b}^{\top} \mid \Sigma$ is expressible in terms of intrinsic quantities alone when the structure is Poincaré-Einstein. The above decomposition into intrinsic curvatures, conformal fundamental forms, and $T$-curvatures applies generally to bulk curvatures and their derivatives, see [8] where a classification of certain hypersurface invariants was given (note that we in particular rely on Theorem 2.5 of that work which applies for $d$ even). It also underlies the strategy for the proof of Theorem 3.7, where it is used to show that derivatives of ambient curvatures can be re-expressed in terms of intrinsic invariants, conformal fundamental forms and $T$-curvatures. The last of these can be eliminated using Proposition 3.2.

In the case of Poincaré-Einstein structures there is a particularly simple $T$-curvature construction. This involves $\log$ densities given by $\log \tau$, where $\tau$ is a true scale. These are defined in [23], but the details are not important here. The key point is that the Laplace-Robin operator $I_{\sigma} . D$ acting on a log density returns a density of weight -1, according to
$$I_{\sigma} . D \log \tau=\frac{d-2}{\tau} I_{\sigma} . \hat{D} \tau+\frac{\sigma}{\tau^{2}}(\hat{D} \tau)^{2} \in \Gamma(\mathcal{E} M[-1]) .$$
Then, following [22], a $T$-curvature of order $k \leqslant\left\lfloor\frac{d}{2}\right\rfloor$ is given by
$$t_{k}^{g}:=\left.\delta_{R}\left(I_{\sigma} . D\right)^{k-1} \log \tau\right|_{\Sigma} .$$
Notice that $t_{1}=\left.\delta_{R} \log \tau\right|_{\Sigma}=-H$ because $\delta_{R}$ can here be replaced by $(d-2)^{-1} I_{\sigma} . D$ restricted to $\Sigma$.

When $d$ is even, a version of the above construction applies to $k>\frac{d}{2}$. This is based on a polynomial weight continuation of the operator $\delta_{R}\left(I_{\sigma} . D\right)^{k-1}$ acting on densities of weight $w$; again see [22]. Let us now explain; for simplicity take $k$ odd. Then one has
$$\delta_{R}\left(I_{\sigma} \cdot D\right)^{k-1}=\hat{P}_{k}(d+2 w-2 k+2)(d+2 w-2 k+4) \cdots(d+2 w-k-1),$$
where the operator $\hat{P}_{k}$ is conformally invariant, even when acting on weights $w$ such that any of the factors to its right vanish. It can be expressed in terms of bulk covariant derivatives, curvatures, the scale $\sigma$, and depends polynomially on $w$.

Remark 3.3. The operator $\hat{P}_{k}$ is proportional to the operator
$$\delta_{J, k-J}: \Gamma\left(\mathcal{E} M\left[k-J-\frac{d}{2}\right]\right) \rightarrow \Gamma\left(\mathcal{E} \Sigma\left[-J-\frac{d}{2}\right]\right),$$
for some $J \in\left\{1, \ldots, \frac{k-1}{2}\right\}$ and odd $k>\frac{d}{2}$, constructed in [22] (see Equation (2.6) above). This corresponds to removing a factor $(d+2 w-2 k+2 J)$ from the right hand side of Equation (3.4) and then continuing in $w$ to the critical value $w=k-J-\frac{d}{2}$. \(\square\)

The action of $\hat{P}_{k}$ on a log density is defined by replacing appearances of $w$ by the operator $\underline{w}$ placed on the far right of any term. Note that $\underline{w} \log \tau=1$. Based on [22], it is easy to show that
$$t_{k}:=\left.\hat{P}_{k} \log \tau\right|_{\Sigma}$$
defines a $T$-curvature for any odd $k>\frac{d}{2}$. (A very similar construction applies to even $k$ but is not important here.) We now characterize these $T$-curvatures for the Graham-Lee scale of a Poincaré-Einstein structure.

Proposition 3.4. Let $\left(M^{d}, \boldsymbol{g}, \sigma\right)$ be Poincaré-Einstein. Then if $g_{r}$ is the Graham-Lee compactified metric for some $\bar{g} \in \boldsymbol{c}_{\Sigma}$, then for any odd integer $k \leqslant\left\lfloor\frac{d}{2}\right\rfloor$,
$$t_{k}^{g_{r}}=0 .$$
Proof. It is well known that the mean curvature of $\Sigma \hookrightarrow\left(M, g_{r}\right)$ vanishes so $t_{1}^{g_{r}}=0$.
Now let $\tau$ be any true scale and $g$ the corresponding compactified metric and call $s=\sigma / \tau$. Then the quantity appearing in Equation (3.3) (divided by $d-2$ ) can be expressed as
$$\frac{I_{\sigma} \cdot \hat{D} \tau}{\tau}+\frac{1}{d-2} \frac{\sigma}{\tau^{2}}(\hat{D} \tau)^{2} \stackrel{g}{=}-\frac{\Delta^{g} s+J^{g} s}{d}-\frac{s}{d-2} J^{g}$$
Here we have placed a $g$ above the equality sign to indicate that we have trivialized the density bundle $\mathcal{E} M[-1]$ using the choice of metric $g$ to obtain the right hand side of the above display. This notational device will appear again in the below. Now, if we specialize the above formula to the Graham-Lee compactified metric $g_{r}$, then $s=r$ the geodesic distance to the boundary. Moreover the Graham-Lee metric has the normal form $g_{r}=d r^{2}+h(r)$. We shall say that a polyhomogeneous expansion in the variable $r$ is even/odd to order $m$ if there are no odd/even terms of order $m$ or less and there are no terms involving $r^{k} \log r$ for $k \leqslant m$. For a Poincaré-Einstein structure, $h(r)$ has an even expansion in the coordinate $r$ up to order $d-2$ [16]. Hence the above display has an odd expansion in $r$ to order $d-3$ (a slightly stronger statement is available when $d$ is even, see the proof of Proposition 3.5). Both the Laplace-Robin and conformal-Robin operator are odd operators with respect to $r$ to some order. Indeed, acting on a density of weight $w$, employing $r$ as a coordinate in a collar neighborhood of $\Sigma$, one has
$$I_{\sigma} \cdot D \stackrel{g_{r}}{=}(d+2 w-2) \partial_{r}-r \partial_{r}^{2}+\operatorname{odd}(r),$$
where (the operator) odd $(r)$ stands for terms that are odd to order $d-3$. Thus, acting at weight $w=0$ and in the Graham-Lee scale
$$\delta_{R}\left(I_{\sigma} . D\right)^{k-2}=\left(\partial_{r}+\operatorname{odd}(r)\right) \underbrace{\left((d-2 k+4) \partial_{r}-r \partial_{r}^{2}+\operatorname{odd}(r)\right) \cdots\left((d-2) \partial_{r}-r \partial_{r}^{2}+\operatorname{odd}(r)\right)}_{k-2 \text { terms }} .$$
Hence $\delta_{R}\left(I_{\sigma} . D\right)^{k-1} \log \tau$ is odd to order $d-2-k$ and hence clearly vanishes along $\Sigma$ when $k \leqslant\left\lfloor\frac{d}{2}\right\rfloor$ and $k$ is odd. \(\square\)

Specializing to even dimensions $d$ we have a stronger statement.
Proposition 3.5. Let $\left(M^{d}, \boldsymbol{g}, \sigma\right)$ be Poincaré-Einstein and let $d$ be even. Then if $g_{r}$ is the Graham-Lee compactified metric for some $\bar{g} \in \boldsymbol{c}_{\Sigma}$, then for any odd integer $k \leqslant d-1$,
$$t_{k}^{g_{r}}=0 .$$
Proof. The case when $k \leqslant \frac{d}{2}$ was dealt with in Proposition 3.4. Hence we consider the $T$ -curvatures defined in Equation (3.5). The Laplace-Robin operator is given for some choice of $g \in \boldsymbol{c}$ by
$$I_{\sigma} \cdot D=(d+2 w-2)\left(\nabla_{n}+w \rho\right)-\sigma(\Delta+w J),$$
where $\rho:=-\frac{1}{d}(\Delta \sigma+J \sigma)$. Hence we see that $\hat{P}_{k}$ can be expressed as a sum of words of length $k$ built partly from the four letters
$$\alpha:=\nabla_{n}, \quad \beta:=\rho, \quad \gamma:=\sigma \Delta, \quad \delta:=\sigma J .$$
We must also allow a fifth letter
$$\varepsilon:=\underline{w}$$
that may appear as many as $2 k-1$ times at the far right of any word. It is given by the weight operator $\underline{w}$ which returns a factor of $w$, the weight of a density, when acting on such. Also, recall that $\underline{w} \log \tau=1$ [23]. As an example, $I_{\sigma} . D$ is expressed as a sum of the words $\alpha, \alpha \varepsilon, \beta \varepsilon, \beta \varepsilon^{2}, \gamma$ and $\delta$. Viewed as operators, in the Graham-Lee scale, each of the four letters $\alpha, \beta, \gamma, \delta$ is odd up to high order, or more precisely can be expressed as a sum of terms
$$\partial_{r}, \quad r \partial_{r}^{2}, \quad \operatorname{odd}(r),$$
where $\operatorname{odd}(r)$ stands for terms odd in $r$ to order $d-3$. Also, in the Graham-Lee scale, one $\operatorname{has} \log \tau=0, \nabla_{n} \log \tau=0, \Delta \log \tau=0$, while in general $\underline{w} \log \tau=1$ and $\underline{w}^{\ell} \log \tau=0$ for $\ell \geqslant 2$. One can now apply the same parity argument as in proof of Proposition 3.4 to establish that $t_{k}$ vanishes for odd $k<d-1$. For the case $t_{d-1}$, we must also carefully examine the highest $r$-derivatives of the terms odd $(r)$. It not difficult to see that along $\Sigma$ (where $r=0$ ) the highest order term is $\left.\partial_{r}^{d-2} \operatorname{odd}(r)\right|_{r=0}$. Since this quantity is a scalar, a simple analysis of the operators appearing in $\alpha, \beta, \gamma, \delta$ shows that the above is proportional to
$$\left.\operatorname{tr}_{h(r)} \partial_{r}^{d-1} h(r)\right|_{r=0} .$$
This is precisely the boundary trace of the image of the Dirichlet-to-Neumann map. The latter is trace-free (see [17]). \(\square\)

A uniqueness argument establishes a vanishing result for odd order $T$-curvatures.
Theorem 3.6. Let $\left(M^{d}, \boldsymbol{g}, \sigma\right)$ be Poincaré-Einstein and $d$ be even. Then, if $g_{r}$ is the Graham-Lee compactified metric for some $\bar{g} \in \boldsymbol{c}_{\Sigma}$, any $T$-curvature of odd order $k \leqslant d-1$ vanishes.

Proof. We have established that the odd order $T$-curvatures $t_{k}$ vanish, so it only remains to establish uniqueness of odd order $T$-curvatures $T_{k \leqslant d-1}$ in the current setting.

On an even dimensional Riemannian manifold, every natural hypersurface invariant with transverse order $k$ may be expressed as a (partial) contraction polynomial in
$$\left\{\bar{g}, \bar{g}^{-1}, \bar{\nabla}, \bar{R}, \hat{n}, \stackrel{\circ}{\mathbb{I}}, \stackrel{\circ}{\top}: \nabla_{\hat{n}}: P, \ldots, \stackrel{\circ}{\top}: \nabla_{n}^{k-2}: P, H,\left.J\right|_{\Sigma}, \ldots,: \nabla_{\hat{n}}^{k-2}:\left.J\right|_{\Sigma}\right\} ;$$
see [8, Theorem 2.5]. Notably, on a Poincaré-Einstein manifold, when $k \leqslant d-2$, this family reduces to
$$\left\{\bar{g}, \bar{g}^{-1}, \bar{\nabla}, \bar{R}, \hat{n}, H,\left.J\right|_{\Sigma}, \ldots,: \nabla_{\hat{n}}^{k-2}:\left.J\right|_{\Sigma}\right\} .$$
To see this, firstly note that conformal fundamental forms exist up to $\overline{\mathrm{d}-1}$ for embeddings in even dimensional conformal manifolds [7, Proposition 3.6]. Moreover, normal derivatives of $P$ may be expressed in terms of these conformal fundamental forms as well as terms from the list directly above; see [8, Corollary 3.3]. However, on Poincaré-Einstein manifolds, all conformal fundamental forms up to and including $\frac{{ }^{\circ}-1}{\mathrm{~d}-1}$ (which has transverse order $d-2$ ) vanish [10,

Theorem 1.8]. We wish to consider transverse order as high as $k=d-1$, and so must in principle also include $\stackrel{+}{\top}: \nabla_{\hat{n}}^{d-3}: P$ in the above family of terms.

By the transverse order requirement for $T$-curvatures, the log term of Equation (3.1) must take the form
$$N_{k} \log \Omega=\Omega^{-1}: \nabla_{\hat{n}}^{k}: \Omega+\text { ltots },$$
where "ltots" stands for terms involving only lower transverse order operators acting on $\Omega$. Also, it follows from the conformal transformation rule for the Schouten tensor $P$, that
$$J^{\Omega^{2} g} \triangleq J^{g}-\Omega^{-1}: \nabla_{\hat{n}}^{2}: \Omega+\text { ltots } .$$
And so, for $2 \leqslant k \leqslant d-2$, the only term in our family with the correct transformation law (matching Equation (3.6)) at leading transverse order is $: \nabla_{\hat{n}}^{k-2}:\left.J\right|_{\Sigma}$. (Note that at order $k=$ $d-1$, the term $\stackrel{\circ}{\top}: \nabla_{\hat{n}}^{d-3}: P$ is precluded from appearing in the leading transverse order term of our putative $T$-curvature by a combination of its its tensor structure and a homogeneity argument.) This establishes that, on a Poincaré-Einstein manifold, any $T$-curvature $T_{k}$ has leading transverse-order term proportional to $: \nabla_{\hat{n}}^{k-2}:\left.J\right|_{\Sigma}$.

Under constant conformal transformations $g \mapsto \lambda^{2} g$, any $T$-curvature $T_{k}$ is homogeneous of weight $-k$. But $\bar{g}, \bar{g}^{-1}, \bar{\nabla}, \bar{R}$, and all even-order $T$-curvatures have even homogeneity. Thus, homogeneity implies that each subleading term in any odd $T$-curvature can be expressed in a form that contains at least one (lower-order) odd $T$-curvature. (Here we used a tensor plus weight argument to preclude terms involving $\hat{n}$.)

The proof is completed by induction in the order of $T$-curvatures. The base case relies on the fact that any first $T$-curvature $T_{1} \propto H$ which vanished in the Graham-Lee scale. Also, we have just shown that distinct odd order $T$-curvatures differ only by terms that can be expressed in terms of lower order $T$-curvatures. Consulting Proposition 3.5 completes the proof. \(\square\)
3.2. Even dimensional bulk. Here we focus on establishing Theorem 1.2 concerning evendimensional Poincaré-Einstein structures. The following theorem is key to the proof.

Theorem 3.7. Let $\Sigma \hookrightarrow\left(M^{d}, \boldsymbol{g}\right)$ be a conformal hypersurface embedding and $\left(M^{d}, \boldsymbol{g}, \sigma\right) \in$ $\mathrm{APE}_{k-2}$ with $2 \leqslant k \leqslant d-1$ and $d$ even. Moreover let $I \in \Gamma(\mathbb{T} \Sigma[w])$, with $w \in 2 \mathbb{Z}+1$, be a natural conformal hypersurface invariant with transverse order $0 \leqslant m \leqslant k-1$. Then, $I=0$.

Proof. We rely on the decomposition discussed above. By definition, natural hypersurface invariants are built from polynomials in Riemann curvatures, unit conormals, their (covariant and possibly tangential) derivatives, and metric contractions thereof. Since we are studying sections $I$ of $\mathbb{T} \Sigma$, we may always deal with expressions such that all (undifferentiated) unit conormals are contracted into Riemann curvatures and their derivatives (a pair of unit conormals can always be re-expressed as $\hat{n}_{a} \hat{n}_{b}=\left.g_{a b}\right|_{\Sigma}-\bar{g}_{a b}$ while no invariant proportional to an overall factor of a single $\hat{n}_{a}$ can live in $\Gamma(\mathbb{T} \Sigma)$ ).

We now analyze when $I$ can have a given transverse order. Consider first the tensor
$$X_{a b}^{(\ell)}:=\hat{n}^{c} \hat{n}^{d}: \nabla_{\hat{n}}^{\ell}:\left.R_{c a d b}\right|_{\Sigma} \in \Gamma(\mathbb{T} \Sigma) .$$
Clearly $X_{a b}^{(\ell)}$ clearly has transverse order at most $\ell+2$; this fits with Equation (3.2) because $T_{2}$ and the trace-free Fialkow tensor have transverse order 2. To see that the transverse order is exactly $\ell+2$, we study how $X_{a b}^{(\ell)}$ behaves upon replacing $g$ by $g+s^{q} h$. For that we consider the linearization of the Riemann tensor around $g$ for the perturbation $g+s^{q} h$, namely
$$\begin{aligned}
R_{a b c d}^{g+s^{q} h}-R_{a b c d}^{g} & =-\frac{1}{2}\left(\nabla_{a}^{g} \nabla_{c}^{g}\left(s^{q} h_{b d}\right)-\nabla_{b}^{g} \nabla_{c}^{g}\left(s^{q} h_{a d}\right)-\nabla_{a}^{g} \nabla_{d}^{g}\left(s^{q} h_{b c}\right)+\nabla_{b}^{g} \nabla_{d}^{g}\left(s^{q} h_{a c}\right)\right)+\mathcal{O}\left(s^{q-1}\right) \\
& =-\frac{q(q-1)}{2} s^{q-2}\left(\hat{n}_{a} \hat{n}_{c} h_{b d}-\hat{n}_{b} \hat{n}_{c} h_{a d}-\hat{n}_{a} \hat{n}_{d} h_{b c}+\hat{n}_{b} \hat{n}_{d} h_{a c}\right)+\mathcal{O}\left(s^{q-1}\right),
\end{aligned}$$
where the notation $\hat{n}$ has been recycled to denote any smooth extension of $\hat{n}$ to $M$, similarly below we will employ the notation $\top$ to denote any extension of the corresponding projector
to $M$. In turn we have
$$\top\left(\hat{n}^{c} \hat{n}^{d}: \nabla_{\hat{n}}^{\ell}:\left(R_{c a d b}^{g+s^{\ell+2} h}-R_{c a d b}^{g}\right)\right)=-\frac{(\ell+2)!}{2} h_{a b}^{\top}+\mathcal{O}(s) .$$
This establishes that $X_{a b}^{(\ell)}$ has transverse order $\ell+2$. Along similar lines, inspecting the (suitably manipulated) Codazzi and Gauß relations
$$\begin{aligned}
& R_{a b c \hat{n}}^{\top} \stackrel{\Sigma}{=} \bar{\nabla}_{a} \stackrel{\circ}{\Pi}_{b c}-\bar{\nabla}_{b} \stackrel{\circ}{\Pi}_{a c}+\bar{g}_{b c} \bar{\nabla}_{a} H-\bar{g}_{a c} \bar{\nabla}_{b} H, \\
& R_{a b c d}^{\top} \stackrel{\Sigma}{=} \bar{R}_{a b c d}-\stackrel{\circ}{\Pi}_{a c} \stackrel{\circ}{\Pi}_{b d}+\stackrel{\circ}{\Pi}_{a d} \stackrel{\circ}{\Pi}_{b c} \\
& \quad-H\left(\bar{g}_{a c} \stackrel{\circ}{\Pi}_{b d}-\bar{g}_{b c} \stackrel{\circ}{\Pi}_{a d}-\bar{g}_{a d} \stackrel{\circ}{\Pi}_{b a}+\bar{g}_{b d} \stackrel{\circ}{\Pi}_{a c}\right)-\left(\bar{g}_{a c} \bar{g}_{b d}-\bar{g}_{b c} \bar{g}_{c d}\right) H^{2},
\end{aligned}$$
shows that $Y_{a b c}^{(\ell)}:=\left(\hat{n}^{d}: \nabla_{\hat{n}}^{\ell}: R_{a b c d}\right)^{\top}$ and $Z_{a b c d}^{(\ell)}:=\left(: \nabla_{\hat{n}}^{\ell}: R_{a b c d}\right)^{\top}$ both have at most transverse order $\ell+1$. Indeed, a similar linearized Riemann argument to the above establishes that their transverse orders are exactly $\ell+1$; the tensors $X, Y, Z$, and the second fundamental form $\Pi$ are the basic atoms from which the invariant $I$ is produced via contractions and hypersurface derivatives. Equations (3.9) and (3.10) satisfy the same type of decomposition as outlined for Equation (3.2), namely into intrinsic, vanishing-for-APE ${ }_{k}$-structures ( $k$ sufficiently high), and (hypersurface derivatives of) $T$-curvatures.

We next need to show that the above decomposition property holds upon suitable application of normal derivatives $: \nabla_{\hat{n}}^{\ell}$ : required to construct $X, Y$ and $Z$. This has been established in a slightly different context in [8]. The argument is as follows: first we need to show that normal derivatives of the ambient Schouten tensor, or its trace, can be traded for conformal fundamental forms and $T$-curvatures at the cost of lower transverse order terms. Therefore we must express $X, Y$ and $Z$ in these terms. Indeed, a Bianchi identity maneuver can be employed to reduce expressions involving $Y$ and $Z$ (at leading transverse order) to ones involving $X$. Consider, for example (refering to [8] for the $Z$ case),
$$\begin{aligned}
& Y_{a b c}^{(\ell)}=\left(\hat{n}^{d} \hat{n}^{e}: \nabla_{\hat{n}}^{\ell-1}: \nabla_{e} R_{a b c d}\right)^{\top}=-\left(\hat{n}^{d} \hat{n}^{e}: \nabla_{\hat{n}}^{\ell-1}:\left(\nabla_{a} R_{b e c d}+\nabla_{b} R_{e a c d}\right)\right)^{\top} \\
& \quad=-\left(\nabla_{a}^{\top}\left(\hat{n}^{d} \hat{n}^{e}: \nabla_{\hat{n}}^{\ell-1}: R_{b e c d}\right)-\nabla_{b}^{\top}\left(\hat{n}^{d} \hat{n}^{e}: \nabla_{\hat{n}}^{\ell-1}: R_{e a c d}\right)\right)^{\top}+\text { ltots } \\
& \quad=-\bar{\nabla}_{a} X_{b c}^{(\ell-1)}+\bar{\nabla}_{b} X_{a c}^{(\ell-1)}+\text { ltots } .
\end{aligned}$$
Here "ltots" stands for lower transverse order tensors.
Now we can focus on $X^{(\ell)}$. The case $\ell=1$ has the desired decomposition by virtue of Equation (3.2). For higher $\ell$, we examine Equation (3.7), which can be re-expressed as
$$X_{a b}^{(\ell)}=\left(\hat{n}^{c} \hat{n}^{d}: \nabla_{\hat{n}}^{\ell}: W_{c a d b}+: \nabla_{\hat{n}}^{\ell}: P_{a b}\right)^{\top}+\bar{g}_{a b} \hat{n}^{c} \hat{n}^{d}: \nabla_{\hat{n}}^{\ell}: P_{c d}+\text { ltots } .$$
Next (remembering that identically $\nabla^{e} W_{\text {caeb }}=(d-3)\left(\nabla_{c} P_{a b}-\nabla_{a} P_{c b}\right)$ ), notice that
$$\begin{aligned}
\left(\hat{n}^{c} \hat{n}^{d}: \nabla_{\hat{n}}^{\ell}: W_{c a d b}\right)^{\top} & =\left(\hat{n}^{c}\left(g^{d e}-\bar{g}^{d e}\right): \nabla_{\hat{n}}^{\ell-1}: \nabla_{e} W_{c a d b}\right)^{\top} \\
& =(d-3)\left(\hat{n}^{c}: \nabla_{\hat{n}}^{\ell-1}:\left(\nabla_{c} P_{a b}-\nabla_{a} P_{c b}\right)\right)^{\top}+\text { ltots } \\
& =(d-3)\left(: \nabla_{\hat{n}}^{\ell}: P_{a b}\right)^{\top}+\text { ltots },
\end{aligned}$$
so that
$$X_{a b}^{(\ell)}=(d-2)\left(: \nabla_{\hat{n}}^{\ell}: P_{a b}\right)^{\top}+\bar{g}_{a b} \hat{n}^{c} \hat{n}^{d}: \nabla_{\hat{n}}^{\ell}: P_{c d}+\text { ltots } .$$
Now, the hypersurface trace-free part of the first term on the right hand side above can be reexpressed as an $(\ell+3)^{\text {th }}$ conformal fundamental form plus lower transverse order terms-again see [8, Corollary 3.3]. The trace as well as the second term above can be written in terms of $T$ curvatures modulo lower transverse order terms. To see that, we may focus on the hypersurface
trace
$$\begin{aligned}
\bar{g}^{a b} X_{a b}^{(\ell)} & =(d-2)\left(g^{a b}-\hat{n}^{a} \hat{n}^{b}\right): \nabla_{\hat{n}}^{\ell}: P_{a b}+(d-1) \hat{n}^{c} \hat{n}^{d}: \nabla_{\hat{n}}^{\ell}: P_{c d}+\text { ltots } \\
& =(d-2): \nabla_{\hat{n}}^{\ell}: J+\hat{n}^{a} \hat{n}^{b}: \nabla_{\hat{n}}^{\ell}: P_{a b}+\text { ltots } \\
& =(d-2): \nabla_{\hat{n}}^{\ell}: J+\hat{n}^{a} g^{b c}: \nabla_{\hat{n}}^{\ell-1}: \nabla_{c} P_{a b}+\text { ltots } \\
& =(d-1): \nabla_{\hat{n}}^{\ell}: J+\text { ltots } .
\end{aligned}$$
In the above we used $\nabla^{a} P_{a b}=\nabla_{b} J$. We have by now shown, at leading transverse order, that any tensor built from $X, Y, Z$, and $\Pi$ (as well as gradients thereof, and the hypersurface metric), can be expressed in terms of $H$, normal derivatives of $J$, conformal fundamental forms, and possibly intrinsic tensors. It remains to focus on normal derivatives of $J$. We know that $T$-curvatures are Riemannian hypersurface invariants built from $X, Y, Z$, II, covariant derivatives thereof, and hypersurface metrics. So from the above display, it must be that normal derivatives of $J$ can be expressed in terms of $T$-curvatures, conformal fundamental forms, and intrinsic tensors. Hence $X, Y$, and $Z$ themselves (and any tensor built therefrom) are also expressible (at leading order) in terms of conformal fundamental forms, $T$-curvatures, and possibly intrinsic tensors. By descent in the transverse order, it follows that this statement holds to all orders.