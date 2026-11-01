---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Gluing Seiberg-Witten Monopoles]

---
source_file: Gluing_Seiberg-Witten_monopoles_cf9c173e2bc5.pdf
converter: mathpix
format: mmd
---

\title{
Gluing Seiberg-Witten Monopoles
}

\author{
Pedram Safari
}

\begin{abstract}
We establish a canonical gluing procedure for Seiberg-Witten monopoles on the two pieces of a closed, oriented four-manifold $X$ which is split along a 3-dimensional closed, oriented submanifold. We only assume that the (unperturbed) character variety is Kuranishi-smooth and the limiting maps are transversal - then we will be able to glue regular monopoles over the irreducible points of the character variety.
\end{abstract}

\section*{1. Introduction.}

The advent of Seiberg-Witten theory in 1994 led not only to a great simplification of the gauge-theoretic results obtained earlier by Donaldson, but also to new advances such as proofs for the Thom conjecture [6]. One of the advantages of the Seiberg-Witten theory is that the bubbling phenomenon does not occur, thus resulting in a compact moduli space for closed four-manifolds.

Naturally, finding methods to compute these invariants would be desirable. For symplectic manifolds, Taubes settled this question by relating the invariants to those of Gromov-Witten [14, 13]. Fintushel and Stern described how the Seiberg-Witten invariants change under certain surgeries over a knot [4]. In yet another direction, one could ask if it is possible to compute the Seiberg-Witten invariants of a four-manifold which is decomposed into two parts, given the relevant information on the pieces.

To make this more precise, let $X$ be a closed, oriented four-manifold, $Y$ a closed, oriented, embedded, dividing submanifold, and $X^{+}$and $X^{-}$, the two components of $X \backslash Y . X^{ \pm}$could be considered as cylindrical-end manifolds with ends isometric to $I \times Y$, where $I$ is an interval. If $X^{ \pm}$are equipped with Spin $^{c}$-structures agreeing on $Y$, then these structures give rise to a unique $S p i n^{c}$-structure on $X$. We are interested in the Seiberg-Witten moduli space of $X$ in terms of those of $X^{+}, X^{-}$and $Y$.

There have already been several partial results around this question; see [10, 11, 5, 1, 2, 3]. The main concern in those works is to explicitly find the solutions to the Seiberg-Witten equations by analytical means, mostly
dealing with some particular type of the boundary manifold $Y$, such as circle bundles over Riemann surfaces or Seifert fibered spaces.

Here, we develop a more general gluing scheme for Seiberg-Witten monopoles, thus setting the ground for a Mayer-Vietoris type theorem for Seiberg-Witten moduli spaces; this would be the subject of a forthcoming paper. Our approach is essentially based on Taubes' method for constructing glued-up ASD connections on connected sums, and is an adaptation of the work of Morgan and Mrowka in gluing ASD SU(2)-connections ([9]) in the context of Seiberg-Witten theory.

We will assume that the three-manifold $Y$ has no reducible point in its Seiberg-Witten moduli space. Otherwise, we would simply confine ourselves to the open set of irreducible points. This could also be achieved by a small perturbation in the Seiberg-Witten equations, which would relieve us from singular points as well, producing a zero-dimensional moduli space, but we are not heeding much this way. Instead, we would allow a positive-dimensional, "smooth" (in the sense of Kuranishi) moduli space, which is free from reducibles, while the obstruction spaces can be non-trivial. On $X^{ \pm}$, we would require the stronger condition of regularity for monopoles.

There are practical motives for this unperturbative approach - in many concrete examples, such as the case of Seifert fibered spaces, we explicitly know the solutions to the unperturbed equations on the three-manifold. However, our method should well work in the perturbative setup as well.

Below is a quick survey of the gluing procedure. We put complete metrics on the two pieces $X^{ \pm}$, thus taking them with infinite ends isometric to $[0, \infty) \times Y$. There is a limiting map which smoothly assigns a monopole on $Y$ to each finite-energy monopole on the the cylindrical-end manifold. We cut each infinite piece at place $\ell$ and glue the truncated manifolds $X_{\ell}^{ \pm}$ along $Y$. The resulting manifolds $X_{\ell}$ are diffeomorphic to $X$ and we try to successfully glue the monopoles on $X^{ \pm}$as the neck is elongated. We start naively by pasting together the monopoles using a partition of unity. Of course, we need to add a correction term to obtain an exact monopole; it would be the unique fixed point of a contraction mapping on a Hilbert space. In fact, if $\tilde{\boldsymbol{\xi}}_{\ell}$ is the approximate glued monopole and $\hat{\xi}$ is the correction term, then we want the left-hand side of the expansion
$$\operatorname{SW}\left(\tilde{\boldsymbol{\xi}}_{\ell}+\hat{\xi}\right)=\operatorname{SW}\left(\tilde{\boldsymbol{\xi}}_{\ell}\right)+\mathcal{D}^{1}(\hat{\xi})+Q(\hat{\xi})$$
to be zero. Here, $\mathcal{D}^{1}$ is the linearization of the SW map and $Q$ is its second order approximation, both depending on $\tilde{\boldsymbol{\xi}}_{\ell}$, of course. The equation can be re-written as
$$\mathcal{D}^{1}(\hat{\xi})=-\operatorname{SW}\left(\tilde{\boldsymbol{\xi}}_{\ell}\right)-Q(\hat{\xi}) .$$

Thus, if we can find a right inverse $\mathcal{R}$ for $\mathcal{D}^{1}$ and set $\hat{\xi}=\mathcal{R}(\hat{\zeta})$, then $\hat{\zeta}$ would be the fixed point of the map
$$\mathcal{F}(\zeta)=-\operatorname{SW}\left(\tilde{\boldsymbol{\xi}}_{\ell}\right)-Q(\mathcal{R}(\zeta)) .$$

In the construction of a right inverse for $\mathcal{D}^{1}$, we are led to consider two complementary subspaces - one being finite-dimensional - and work on each one separately. The main difficulty lies in right-inverting $\mathcal{D}^{1}$ on the finite-dimensional subspace; this is essentially due to the existence of obstruction spaces in the first place. We will make estimates on the norms of certain operators, obtained through Hodge theory, to eventually conclude that the desired full right inverse can be constructed for $\ell$ sufficiently large. The norm of this operator could grow exponentially in $\ell$; nevertheless, the perturbation term will decline exponentially and this conforms with the intuition that the approximate gluing is increasingly "better" as $\ell$ becomes larger.

The hard analysis culminates in the main theorem of this paper, whose proof is completed in Section 3.5. Use $\mathcal{M}$ to denote the Seiberg-Witten moduli space and let $\partial_{ \pm}: \mathcal{M}\left(X^{ \pm}\right) \rightarrow \mathcal{M}(Y)$ be the limiting map. Assume that $\mathcal{M}(Y)$ is Kuranishi-smooth and consider $\mathcal{M}^{i r r}(Y)$, the (smooth) irreducible part of the moduli space of $Y$. Let $\mathcal{M}^{*}\left(X^{ \pm}\right)$consist of the regular points of the inverse image of $\mathcal{M}^{i r r}(Y)$ under the limiting map. Note that this implies that $\mathcal{M}^{*}\left(X^{ \pm}\right)$is free from reducible points, too. We continue to use the same notation for the restriction of $\partial_{ \pm}$to $\mathcal{M}^{*}\left(X^{ \pm}\right)$.

Theorem. Under the preceding assumptions on $X^{ \pm}, Y$, and their moduli spaces, if the limiting maps $\partial_{ \pm}: \mathcal{M}^{*}\left(X^{ \pm}\right) \rightarrow \mathcal{M}^{i r r}(Y)$ are transversal, then there is an $L_{0}$ such that for each $\ell \geq 4 L_{0}$, the following holds. To any two regular monopoles $\boldsymbol{\xi}^{+}$and $\boldsymbol{\xi}^{-}$, respectively on $X^{+}$and $X^{-}$, with the same limiting value $\boldsymbol{\eta} \in \mathcal{M}^{i r r}(Y)$, one can smoothly assign a monopole $\boldsymbol{\xi}_{\ell}$ on $X_{\ell}$ obtained through a canonical gluing scheme.

\section*{2. Rudiments.}

Let us first review some basic facts of Seiberg-Witten theory and meanwhile set our notations along the way.

Let $X$ be a smooth, connected, oriented, riemannian four-manifold. We equip $X$ with a $\operatorname{Spin}^{c}$-structure $\mathfrak{s}$, that is a lifting of its principal tangent SO(4)-bundle $P$ to a principal $\operatorname{Spin}^{c}(4)$-bundle $\tilde{P}$. Such liftings always exist and correspond (non-canonically) to classes in $H^{2}(M, \mathbb{Z})$ - in fact, one can
twist $\tilde{P}$ with any given U(1)-bundle. Corresponding to Clifford representations of $\operatorname{Spin}^{c}(4)=\operatorname{SU}(2) \times \operatorname{SU}(2) \times \mathrm{U}(1) /\{ \pm 1\}$, we obtain the associated plus- and minus-spinor bundles $S^{+}$and $S^{-}$, which are 2-dimensional complex vector bundles with bundle group U(2), as well as the determinant line bundle $L=\operatorname{det} \tilde{P}=\operatorname{det} S^{+}=\operatorname{det} S^{-}$.

Any unitary connection $A$ on the U(1)-bundle $L$, in conjunction with the Levi-Cività connection on $X$, will induce connections on the lifting $\tilde{P}$, as well as on $S^{ \pm}$. Thus, a Dirac operator $\not \partial_{A}: \Gamma\left(S^{ \pm}\right) \rightarrow \Gamma\left(S^{\mp}\right)$ can be defined by
$$\not \partial_{A}(\Psi)=\sum_{j=1}^{n} e_{j} \cdot \nabla_{e_{j}}(\Psi),$$
where $\left\{e_{j}\right\}_{j=1}^{n}$ is an orthonormal frame for $T_{x} X$ and . denotes Clifford multiplication. The definition is frame-invariant.

The Seiberg-Witten equations, in two unknowns $A$ and $\Psi$, can now be written as
$$\left\{\begin{array}{l}
F_{A}^{+}=\left\{\Psi \otimes \Psi^{*}\right\} \\
\not \partial_{A}(\Psi)=0,
\end{array}\right.$$
where $\Psi$ is a plus-spinor and the brackets denote the trace-less part of an endomorphism. In other words, $\left\{\Psi \otimes \Psi^{*}\right\}$ denotes the quadratic $q(\Psi)=$ $\Psi \otimes \Psi^{*}-\frac{1}{2}|\Psi|^{2}$ I. In the same equation, $F_{A}^{+}$denotes the self-dual part of the curvature tensor under the Hodge $*$-operator. It defines a trace-free representation of the Clifford bundle $\mathbb{C l}_{0}^{+}$on $S^{+}$via Clifford multiplication, thus both sides of the first equation should be identified as trace-less sections of the bundle of endomorphisms of plus-spinors, $\operatorname{End}\left(S^{+}\right)$.

One can also consider the perturbed variant of the Seiberg-Witten equations
$$\left\{\begin{array}{l}
F_{A}^{+}=\left\{\Psi \otimes \Psi^{*}\right\}+i h \\
\not \partial_{A}(\Psi)=0,
\end{array}\right.$$
where $h$ is a real self-dual 2-form on $X$.
Sometimes, it is convenient to consider the Seiberg-Witten map on the configuration space $\mathcal{C}(X, \mathfrak{s})=\mathcal{A}(L) \times \Gamma\left(S^{+}\right)$consisting of a connection on the determinant line bundle and a plus-spinor. The map $\mathrm{SW}: \mathcal{A}(L) \times \Gamma\left(S^{+}\right) \rightarrow$ $\Omega_{+}^{2}(X) \times \Gamma\left(S^{-}\right)$is defined by
$$\operatorname{SW}(A, \Psi)=\left(F_{A}^{+}-q(\Psi), \not \partial_{A}(\Psi)\right) .$$
$\mathrm{SW}_{h}$ is defined similarly.
We will feel free to make various assumptions on the configuration spaces, for example by taking completions with respect to an appropriate norm, or
by considering only finite-energy configurations. That should be clear from the context and we would invariably use the same notation SW or $\mathrm{SW}_{h}$.

The gauge group $\mathcal{G}$, i.e. the group of bundle-automorphisms of $\tilde{P}$, corresponds to maps $X \rightarrow S^{1}$. It right-acts on the configuration space $\mathcal{C}(X, \mathfrak{s})$, as well as on the solutions to the Seiberg-Witten equations $\mathcal{S}(X, \mathfrak{s})$, by
$$(A, \Psi) \cdot g=\left(A+2 g^{-1} d g, S^{+}\left(g^{-1}\right)(\Psi)\right) .$$
The stabilizer of $(A, \Psi)$ is trivial iff $\Psi \neq 0$, in which case the point is called irreducible. Reducible solutions have the stabilizer $=S^{1}$. Dividing out the solution set by the action of the gauge group produces the Seiberg-Witten moduli space $\mathcal{M}(X, \mathfrak{s})=\mathcal{S}(X, \mathfrak{s}) / \mathcal{G}$.

A cohomological discussion of regularity is in order. To each point $\boldsymbol{\xi} \in$ $\mathcal{C}(X, \mathfrak{s})$ of the configuration space of a four-manifold $X$, one can assign the following diagram $\left.\mathcal{E}\right|_{\boldsymbol{\xi}}$
$$0 \longrightarrow \Omega_{3}^{0}(X ; i \mathbb{R}) \xrightarrow{\mathcal{D}^{0}} \Omega_{2}^{1}(X ; i \mathbb{R}) \oplus \Gamma_{2}\left(S^{+}\right) \xrightarrow{\mathcal{D}^{1}} \Omega_{+, 1}^{2}(X ; i \mathbb{R}) \oplus \Gamma_{1}\left(S^{-}\right) \longrightarrow 0,$$
where $\Omega_{k}^{m}(X ; i \mathbb{R})$ means the $L_{k}^{2}$-completion (or a completion in another appropriate Sobolev norm, for that matter) of purely imaginary $m$-forms with compact support and $\Gamma_{k}\left(S^{ \pm}\right)$denotes the $L_{k}^{2}$-completion of the compactly supported sections of the corresponding spinor bundles. $\mathcal{D}^{0}$ is the linearization of the action of the gauge group and $\mathcal{D}^{1}$ is the derivative of SW, both at the point $\boldsymbol{\xi}=(A, \Psi)$, i.e.
$$\begin{gathered}
\mathcal{D}^{0}=(2 d,-. \Psi) ; \\
\mathcal{D}^{1}=\left(\begin{array}{cc}
d^{+} & -\left.D q\right|_{\Psi} \\
. \frac{1}{2} \Psi & \not \varnothing_{A}
\end{array}\right) .
\end{gathered}$$
Note that SW and $\mathrm{SW}_{h}$ are non-linear maps with the same derivative $\mathcal{D}^{1}$, so $\left.\mathcal{E}\right|_{\boldsymbol{\xi}}$ remains unaltered with a perturbation of the equations.

Now, if $\boldsymbol{\xi}$ happened to be a solution of SW or $\mathrm{SW}_{h}$, then the diagram $\left.\mathcal{E}\right|_{\boldsymbol{\xi}}$ would be a complex; moreover, it would even be an elliptic complex if $X$ were closed, or had appropriate boundary conditions, so it would have finite-dimensional cohomologies. $H^{0}$ of such a complex turns out to be the tangent space to the stabilizer of the gauge group action, $H^{1}$ is the Zariski tangent space to the moduli space at $\boldsymbol{\xi}$ and $H^{2}$ is its obstruction space. By general Hodge theory, these groups can be identified with the 'harmonic forms'.

Recall that a solution $\boldsymbol{\xi}=(A, \Psi)$ is called irreducible if $\Psi$ is not identically zero; this is equivalent to $H^{0}\left(\left.\mathcal{E}\right|_{\boldsymbol{\xi}}\right)=0$. We call a solution regular
(in an algebraic sense) if the obstruction space at that point is trivial, i.e. $H^{2}\left(\left.\mathcal{E}\right|_{\boldsymbol{\xi}}\right)=0$. Note that according to the Kuranishi picture, an irreducible solution is a smooth point (in a geometric sense) if and only if the Kuranishi map vanishes, although the obstruction space may not be trivial.

We will use superscripts to denote the terms of $\mathcal{E}$. Depending on the emphasis, when all else is clear from the context, we might use combinations such as $\mathcal{E}(X),\left.\mathcal{E}(X, \mathfrak{s})\right|_{\boldsymbol{\xi}}$ and so on. Thus, for example,
$$\begin{aligned}
& \mathcal{E}^{0}(X)=\Omega_{3}^{0}(X ; i \mathbb{R}), \quad \mathcal{E}^{1}(X)=\Omega_{2}^{1}(X ; i \mathbb{R}) \oplus \Gamma_{2}\left(S^{+}\right), \\
& \mathcal{E}^{2}(X)=\Omega_{+, 1}^{2}(X ; i \mathbb{R}) \oplus \Gamma_{1}\left(S^{-}\right)
\end{aligned}$$
We will also use boldface Greek letters (corresponding to the base manifold) for points of the configuration space (for example, $\boldsymbol{\xi}$ is a point of $\mathcal{C}(X)$ ) while the same Greek letters are used for the vectors of the corresponding Zariski tangent spaces ( $\xi$ belongs to $H^{1}\left(\left.\mathcal{E}\right|_{\xi}\right)$ ).

It would be nice to review the setup for the case of a closed four-manifold $X$. If we complete the configuration space and the gauge group using the $L_{2}^{2}$ and $L_{3}^{2}$ Sobolev norms, respectively, then we obtain an affine Hilbert space on which a Hilbert Lie group is acting. The moduli space $\mathcal{M}(X, \mathfrak{s})$ happens to be Hausdorff, but it might have singularities, for example when the action is not free. It can be shown though that the solutions of a generic perturbation of the Seiberg-Witten equations are all irreducible and regular, therefore, resulting in a smooth moduli space $\mathcal{M}_{h}(X, \mathfrak{s})$. Using the Atiyah-Singer index theorem and Bochner's formula, we conclude that $\mathcal{M}_{h}$ is a finite-dimensional compact manifold of formal dimension $\frac{1}{4}\left(c_{1}(L)^{2}-2 \chi(M)-3 \sigma(M)\right)$, where $\chi$ is the Euler characteristic and $\sigma$ is the signature.

The basic reference for the material so far is [7].
One can mimic the preceding constructions on a three-manifold $Y$ with a $\operatorname{Spin}^{c}(3)$-structure $\mathfrak{t}$ to obtain analogs, where there is only one spinor bundle $S$ and no self-duality. Thus, for instance, one can define a map $\mathrm{SW}^{3}: \mathcal{A}(L) \times \Gamma(S) \rightarrow \Omega^{2}(Y) \times \Gamma(S)$ by
$$\operatorname{SW}^{3}(B, \Phi)=\left(F_{B}-q(\Phi), \not D_{B}(\Phi)\right) .$$
The moduli space for a closed three-manifold would generically be of formal dimension zero, as the index of an elliptic operator on an odd-dimensional closed manifold is zero.

Another case of particular interest is when $X=\mathbb{R} \times Y$ is a cylinder on a closed three-manifold $Y$ and $\boldsymbol{\xi}=\pi^{*}(\boldsymbol{\eta})$ is a translation-invariant solution. Then, the cohomologies of $\left.\mathcal{E}(X)\right|_{\boldsymbol{\xi}}$ can be identified in an obvious way with
the cohomologies of $\mathcal{E}(Y) \mid \boldsymbol{\eta}$ below. (This is not the elliptic complex that is officially associated to three-manifolds - it is not even elliptic - but it would be more fitting to our discussion here.)
$$0 \longrightarrow \Omega_{3}^{0}(Y ; i \mathbb{R}) \xrightarrow{\mathcal{D}^{0}} \Omega_{2}^{1}(Y ; i \mathbb{R}) \oplus \Gamma_{2}(S) \xrightarrow{\mathcal{D}^{1}} \Omega_{1}^{2}(Y ; i \mathbb{R}) \oplus \Gamma_{1}(S) \underset{(\mathcal{E}(Y) \mid \boldsymbol{\eta})}{0}$$
where
$$\begin{gathered}
\boldsymbol{\eta}=(B, \Phi) ; \\
\mathcal{D}^{0}=(2 d,-. \Phi) ; \\
\mathcal{D}^{1}=\left(\begin{array}{cc}
d & -\left.D q\right|_{\Phi} \\
. \frac{1}{2} \Phi & \not \partial_{B}
\end{array}\right) .
\end{gathered}$$

The situation is in general more complicated if $X$ is not closed, as we need controlling conditions near the boundary or infinity, so as to keep the ellipticity. Therefore, we work with configurations with finite energy when we deal with manifolds with cylindrical ends. So, we continue to consider a cylinder $I \times Y$, where $I=[c, d]$ is an interval. The solutions to the Seiberg-Witten equations on this four-manifold turn out to be the gradient flow lines of the so-called "Chern-Simons-Dirac" functional on $\mathcal{C}(Y, \mathfrak{t})$ :
$$\operatorname{CSD}(B, \Phi)=\int_{Y} F_{B_{0}} \wedge b+\frac{1}{2} \int_{Y} b \wedge d b+\int_{Y}\left\langle\Phi, \not \partial_{B} \Phi\right\rangle d \mathrm{vol}$$
where $b=B-B_{0}$ and $B_{0}$ is a fixed background connection [10]. The singular points of this vector field, i.e. the static solutions, correspond to solutions of $\mathrm{SW}^{3}$. There are analogs for perturbed equations, too.

The energy of a solution $(A, \Psi)$ on a cylinder is defined by any of the following equivalent formulas. We assume that $A$ is in temporal gauge and we write $(A, \Psi)=(B(t), \Phi(t))$, where $B(t)$ and $\Phi(t)$ are connections and spinors on the three-manifold.
$$\begin{aligned}
E(A, \Psi) & =\int_{I}\|\dot{B}\|^{2}+\|\dot{\Phi}\|^{2} \\
& =\int_{I}\|\nabla \operatorname{CSD}(B(t), \Phi(t))\|^{2} \\
& =\operatorname{CSD}(B(d), \Phi(d))-\operatorname{CSD}(B(c), \Phi(c)) .
\end{aligned}$$

The end of a manifold is, formally, the inverse limit of its co-compact subsets, ordered by inclusion. Intuitively, this is the place where the manifold extends to infinity. We call a riemannian manifold $Z$ a cylindrical-end manifold if its end is orientation-preserving isometric to $[0, \infty) \times Y$, where
$Y$ is an oriented, riemannian three-manifold. We fix a smooth "time coordinate" function $\tau: Z \rightarrow[-1, \infty)$ which agrees with the first coordinate of $[0, \infty) \times Y$ on the end and is negative on the complement. Given a positive real number $\ell>0$, let $Z_{\ell}=\tau^{-1}((-\infty, \ell])$. For a pair of positive real numbers $0<\ell<\ell^{\prime}$, let $Z_{\left[\ell, \ell^{\prime}\right]}=\tau^{-1}\left(\left[\ell, \ell^{\prime}\right]\right)$.

On cylindrical-end manifolds, we will exclusively work with solutions with finite energy on the ends for the sake of ellipticity.

\section*{3. The Gluing Theorem.}

\subsection*{3.1. Gluing Cylindrical-End Manifolds.}

Let us fix two connected, oriented, cylindrical-end riemannian fourmanifolds $X^{ \pm}$, each with a single end which is modeled on $[0, \infty) \times Y$. We will also consider the cylinder $X^{o}=\mathbb{R} \times Y$. The notation $X^{\#}$ will then be used to denote any of these three manifolds.

We will also introduce "time" coordinates $\tau$ on these manifolds as follows. On $X^{ \pm}$, take the first coordinate map on the end $[0, \infty) \times Y$ and choose any extension $\tau_{ \pm}: X^{ \pm} \rightarrow[-1, \infty)$ which is identically -1 outside a collar (the collar being identified with $(-1,0] \times Y)$. On $X^{o}=\mathbb{R} \times Y, \tau_{o}$ is essentially the absolute value function on the first coordinate, smoothed out at the origin. This will be made more precise further below.

We now form a family of four-manifolds $X_{\ell}, \ell>0$, as follows. First, truncate the manifolds $X^{ \pm}$at $\tau_{ \pm}=\ell$ to produce $X_{\ell}^{ \pm}$consisting of points with $\tau_{ \pm}(x) \leq \ell$. We then obtain $X_{\ell}$ by gluing $X_{\ell}^{+}$and $X_{\ell}^{-}$along their boundaries (see Figures 1 and 2). We are interested in $X_{\ell}$ for $\ell$ large and we would eventually assume $\ell>4 L_{0}$, where $L_{0}$ is a large, but fixed, positive number. The manifolds $X_{\ell}$ are just diffeomorphic versions of one and the same manifold $X$, being elongated along a tube. We will also re-parameterize the long cylinder $C_{\ell}=\operatorname{End}\left(X_{\ell}^{+}\right) \cup \operatorname{End}\left(X_{\ell}^{-}\right)$inside $X_{\ell}$, identifying it with $[-\ell, \ell] \times Y$ as in Figure 2. $C_{\ell^{\prime}}$ is then the chunk of $C_{\ell}$ parameterized as $\left[-\ell^{\prime}, \ell^{\prime}\right] \times Y$.

Now, we get back to our discussion of the time coordinate and, in the mean time, we also introduce a time-coordinate function $\tau_{\ell}$ on the manifold $X_{\ell}$. It is identical to $\tau_{+}$on $X_{\ell-1}^{+}$and to $\tau_{-}$on $X_{\ell-1}^{-}$, and smoothly interpolates between the two such that its value on $C_{1}$ is in the interval $[\ell-1, \ell]$. This choice of interpolation can be made independently of $\ell$ and therefore, the function $\ell-\tau_{\ell}$ converges, uniformly on compact subsets of $X^{o}$, to the function $\tau_{o}$ alluded to earlier. Outside of $C_{1}=[-1,1] \times Y$, we

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/c3d067ce-d69e-422c-be37-a370df27a3ab-09.jpg?height=824&width=1087&top_left_y=248&top_left_x=428}
\captionsetup{labelformat=empty}
\caption{Figure 1: Two cylindrical-end manifolds $X_{\ell}^{+}$and $X_{\ell}^{-}$}
\end{figure}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/c3d067ce-d69e-422c-be37-a370df27a3ab-09.jpg?height=419&width=1380&top_left_y=1219&top_left_x=348}
\captionsetup{labelformat=empty}
\caption{Figure 2: $X_{\ell}^{+}$and $X_{\ell}^{-}$glued together to form $X_{\ell}$}
\end{figure}
have $\tau_{o}(t, y)=|t|$.
We are also able to patch $\operatorname{Spin}^{c}$-structures $\mathfrak{s}^{ \pm}$(on $X^{ \pm}$) which agree on the ends. More precisely, there is a principal $\operatorname{Spin}^{c}(3)$-lifting $\tilde{Q}$ of the principal orthonormal tangent bundle of $Y$ such that $\left.\tilde{P}^{ \pm}\right|_{\operatorname{End}\left(X^{ \pm}\right)} \cong \mathbb{R} \times \pi^{*} \tilde{Q}$, where $\pi: I \times Y \rightarrow Y$ is the projection. Indeed, on $\operatorname{End}\left(X^{ \pm}\right)$, there is an embedding $\pi^{*} \tilde{Q} \hookrightarrow \tilde{P}^{ \pm}$, induced from the lift of the obvious embedding SO(3) ↪ SO(4).

See [10] for details. By fixing the isomorphism above, we can form a Spin ${ }^{c}$ -structure $\mathfrak{s}_{\ell}$ on $X_{\ell}$ which is compatible with the original $\operatorname{Spin}^{c}$-structures.

\subsection*{3.2. Approximate Gluing of Monopoles.}

Let $\boldsymbol{\xi}^{ \pm}=\left(A^{ \pm}, \Psi^{ \pm}\right)$be finite-energy solutions to the Seiberg-Witten equations SW on $X^{ \pm}$. Based on our earlier assumptions, $\boldsymbol{\xi}^{ \pm}$will be regular and irreducible.

By a result of Simon [8], "finite energy implies finite length" for the solution, which is now viewed as a gradient flow line for CSD on the cylindrical end. It further implies "exponential decay" to a solution $(B, \Phi)$ of $\mathrm{SW}^{3}$ on $Y$. See [8]. The exponent $\kappa$ in this exponential decay is less than half the minimum of the absolute value of the eigenvalues of the Hessian
$$\operatorname{Hess}(C S D)=\left(\begin{array}{cc}
* d & \left.D q\right|_{\Psi} \\
0 & \not \partial_{A}
\end{array}\right),$$
which is the linearization of the gradient flow at a critical point. Therefore, $\kappa$ has a bound which simply depends on the eigenvalues of $\Delta$ and $\not 力_{A}$.

We also assume that $\boldsymbol{\xi}^{ \pm}$converge to the same irreducible solution $\boldsymbol{\eta}$ on $Y$. This is tantamount to considering $\left(\boldsymbol{\xi}^{+}, \boldsymbol{\xi}^{-}\right)$as a point in the fiber product $\mathcal{M}^{*}\left(X^{+}\right) \times_{U} \mathcal{M}^{*}\left(X^{-}\right)$, defined as the pull-back of the diagram
![](https://cdn.mathpix.com/cropped/c3d067ce-d69e-422c-be37-a370df27a3ab-10.jpg?height=198&width=820&top_left_y=1305&top_left_x=737)
where $\partial_{ \pm}: \mathcal{M}^{*}\left(X^{ \pm}\right) \rightarrow \mathcal{M}^{i r r}(Y)$ are the limiting maps for the flow lines, $U$ an arbitrary (smooth) neighborhood of $\boldsymbol{\eta}$ in $\mathcal{M}^{i r r}(Y)$ and $\left.\mathcal{M}^{*}\left(X^{ \pm}\right)\right|_{U}=$ $\left(\partial_{ \pm}\right)^{-1}(U) . \mathcal{M}$ 's may denote any variant of the Seiberg-Witten moduli spaces, depending on the context.

We will later also need to assume a transversality condition at $\boldsymbol{\eta}$.
While passing from $X^{ \pm}$to $X_{\ell}^{ \pm}$, we truncate $\boldsymbol{\xi}^{ \pm}$to $\boldsymbol{\xi}_{\ell}^{ \pm}$as well. Then, we glue $X_{\ell}^{+}$and $X_{\ell}^{-}$together to form $X_{\ell}$ and our goal is to "glue" $\boldsymbol{\xi}_{\ell}^{+}$and $\boldsymbol{\xi}_{\ell}^{-}$ to construct a solution $\boldsymbol{\xi}_{\ell}$ to SW on the glued-up manifold $X_{\ell}$, for large $\ell$. To this end, our first step would be to construct an approximate solution $\tilde{\boldsymbol{\xi}}_{\ell}=\left(\tilde{A}_{\ell}, \tilde{\Psi}_{\ell}\right)$ of SW on $X_{\ell}$, using a partition of unity $\{\lambda, 1-\lambda\}$ which is constant outside of $C_{2 L_{0}}$. Thus, we can define an "approximate gluing map"
$$\tilde{\gamma}=\tilde{\gamma}_{\ell}: \mathcal{S}\left(X^{+}, \mathfrak{s}^{+}\right) \times \mathcal{S}\left(X^{-}, \mathfrak{s}^{-}\right) \rightarrow \mathcal{C}\left(X_{\ell}, \mathfrak{s}_{\ell}\right)$$
by $\tilde{\boldsymbol{\xi}}_{\ell}:=\tilde{\gamma}_{\ell}\left(\boldsymbol{\xi}^{+}, \boldsymbol{\xi}^{-}\right)=\lambda \boldsymbol{\xi}_{\ell}^{+}+(1-\lambda) \boldsymbol{\xi}_{\ell}^{-}$.
Due to technical problems arising from the presence of an obstruction space $H^{2}$, we shall use weighted Sobolev norms to allow some small exponential growth on forms and spinors. Let $\alpha$ be a $C^{\infty}$, compact supported $m$-form on a cylindrical-end manifold $Z, \tau$ the time coordinate on $Z, \nabla$ the Levi-Cività connection and $\delta$ a real number. Define the $L_{k,-\delta}^{2}$-norm of $\alpha$ as
$$\|\alpha\|_{k,-\delta}=\left(\sum_{j=0}^{k} \int_{Z} e^{-\delta \tau}\left|\nabla^{j} \alpha\right|^{2}\right)^{1 / 2} .$$
We will denote the $L_{k,-\delta}^{2}$-completion of the space of $C^{\infty}$, compact supported $m$-forms on $Z$ by $\Omega_{k,-\delta}^{m}(Z)$. Analogous terminology will also be used for spinor fields, except that a hermitian connection on the spinor bundle must be used instead of the Levi-Cività connection. On $X_{\ell}$, we can define the weighted norms similarly; $\tau_{\ell}$ is to be used instead of $\tau$. However, note that Sobolev norms with different weights are equivalent on a closed manifold.

We have the following estimate.
Proposition 3.1. For any $\delta \geq 0$ and any $\ell>4 L_{0}$,
$$\left\|\operatorname{SW}\left(\tilde{\boldsymbol{\xi}}_{\ell}\right)\right\|_{1,-\delta} \leq \tilde{C} e^{-\left(\kappa+\frac{\delta}{2}\right)\left(\ell-2 L_{0}\right)},$$
for some constant $\tilde{C}$ which is independent of $\ell$ and $L_{0}$.
$\operatorname{Proof} . \operatorname{SW}\left(\tilde{\boldsymbol{\xi}}_{\ell}\right)$ is zero when $\lambda$ is constant. So, we only need to estimate it on $C_{2 L_{0}}$. Using the fact that $\operatorname{SW}\left(\boldsymbol{\xi}^{+}\right)$and $\operatorname{SW}\left(\boldsymbol{\xi}^{-}\right)$are both zero, we get
$$\mathrm{SW}\left(\tilde{\boldsymbol{\xi}}_{\ell}\right)=\left(-d^{+}(\lambda a)-\lambda^{2} q(\psi)-D q\left(\Psi^{-}, \lambda \psi\right),-\nabla(\lambda) \psi\right),$$
where $a=A^{+}-A^{-}$and $\psi=\Psi^{+}-\Psi^{-}$on $C_{2 L_{0}}$. An easy computation shows that $|q(\psi)|=\frac{1}{2}|\psi|^{2}$ and that $\left|D q\left(\psi, \psi^{\prime}\right)\right| \leq 2|\psi|\left|\psi^{\prime}\right|$. Now, the fact that the solutions decay exponentially fast with exponent $\kappa$ gives the desired estimate. \(\square\)

Next, we deform $\tilde{\boldsymbol{\xi}}_{\ell}$ to a solution of $\operatorname{SW}\left(\boldsymbol{\xi}_{\ell}\right)=0$. For this, as was pointed out in Section 1, we will need a right inverse $\mathcal{R}$ for $\mathcal{D}^{1}$ in the following diagram at the point $\tilde{\boldsymbol{\xi}}_{\ell}=\left(\tilde{A}_{\ell}, \tilde{\Psi}_{\ell}\right)$.
$$\begin{aligned}
0 \longrightarrow \Omega_{3,-\delta}^{0}\left(X_{\ell} ; i \mathbb{R}\right) & \xrightarrow{\mathcal{D}^{0}} \Omega_{2,-\delta}^{1}\left(X_{\ell} ; i \mathbb{R}\right) \oplus \Gamma_{2,-\delta}\left(S^{+}\right) \\
& \xrightarrow{\mathcal{D}^{1}} \Omega_{+, 1,-\delta}^{2}\left(X_{\ell} ; i \mathbb{R}\right) \oplus \Gamma_{1,-\delta}\left(S^{-}\right) \longrightarrow 0
\end{aligned}$$

This diagram is not even a complex, since $\partial_{\tilde{A}_{\ell}}\left(\tilde{\Psi}_{\ell}\right) \neq 0$.
We will construct such an inverse using the chain homotopies that already exist between the complexes of each piece of our manifold and their cohomologies. Let $0<\delta<\kappa / 2$ and consider the following diagram of two copies of the complex $\mathcal{E}_{-\delta}\left(X^{ \pm}\right)$at $\boldsymbol{\xi}^{ \pm}$.
![](https://cdn.mathpix.com/cropped/c3d067ce-d69e-422c-be37-a370df27a3ab-12.jpg?height=219&width=915&top_left_y=539&top_left_x=690)
where
$$\begin{aligned}
& \mathcal{E}_{-\delta}^{0}\left(X^{ \pm}\right)=\Omega_{3,-\delta}^{0}\left(X^{ \pm} ; i \mathbb{R}\right), \\
& \mathcal{E}_{-\delta}^{1}\left(X^{ \pm}\right)=\Omega_{2,-\delta}^{1}\left(X^{ \pm} ; i \mathbb{R}\right) \oplus \Gamma_{2,-\delta}\left(S^{+}\right), \\
& \mathcal{E}_{-\delta}^{2}\left(X^{ \pm}\right)=\Omega_{+, 1,-\delta}^{2}\left(X^{ \pm} ; i \mathbb{R}\right) \oplus \Gamma_{1,-\delta}\left(S^{-}\right),
\end{aligned}$$
using weighted Sobolev completions. These are the complexes associated to solutions $\boldsymbol{\xi}^{ \pm}$of SW on $X^{ \pm}$. As $\boldsymbol{\xi}^{ \pm}$are regular and irreducible, the complexes above have no cohomology except possibly in degree one. $\Pi_{ \pm}^{1}$ is the projection onto this cohomology, represented by the harmonic 'one-forms', and the parametrices $\mathcal{L}_{ \pm}$and $\mathcal{R}_{ \pm}$are constructed using Hodge theory, so that
$$\left\{\begin{array}{l}
\mathcal{L}_{ \pm} \circ \mathcal{D}^{0}=\mathrm{I} \\
\mathcal{D}^{0} \circ \mathcal{L}_{ \pm}+\mathcal{R}_{ \pm} \circ \mathcal{D}^{1}=\mathrm{I}-\Pi_{ \pm}^{1} \\
\mathcal{D}^{1} \circ \mathcal{R}_{ \pm}=\mathrm{I} .
\end{array}\right.$$
Note that $\mathcal{R}_{ \pm}$are right inverses for $\mathcal{D}^{1}$ on the respective pieces.
Now, recall that the solutions $\boldsymbol{\xi}^{ \pm}$, considered now as gradient flow lines, both converge to the same static solution $\boldsymbol{\eta}$. Thus, similarly as above, consider the corresponding complex $\mathcal{E}_{\delta}\left(X^{o}\right)$ on the cylinder $X^{o}=\mathbb{R} \times Y$ at the constant solution (i.e. the pull-back of $\boldsymbol{\eta}$ to $X^{o}$ ), still denoted by $\boldsymbol{\eta}$.
![](https://cdn.mathpix.com/cropped/c3d067ce-d69e-422c-be37-a370df27a3ab-12.jpg?height=217&width=831&top_left_y=1691&top_left_x=732)
where, similarly,
$$\begin{aligned}
& \mathcal{E}_{\delta}^{0}\left(X^{o}\right)=\Omega_{3, \delta}^{0}\left(X^{o} ; i \mathbb{R}\right), \\
& \mathcal{E}_{\delta}^{1}\left(X^{o}\right)=\Omega_{2, \delta}^{1}\left(X^{o} ; i \mathbb{R}\right) \oplus \Gamma_{2, \delta}\left(S^{+}\right), \\
& \mathcal{E}_{\delta}^{2}\left(X^{o}\right)=\Omega_{+, 1, \delta}^{2}\left(X^{o} ; i \mathbb{R}\right) \oplus \Gamma_{1, \delta}\left(S^{-}\right),
\end{aligned}$$
and,
$$\left\{\begin{array}{l}
\mathcal{L}_{o} \circ \mathcal{D}^{0}=\mathrm{I} \\
\mathcal{D}^{0} \circ \mathcal{L}_{o}+\mathcal{R}_{o} \circ \mathcal{D}^{1}=\mathrm{I}-\Pi_{o}^{1} \\
\mathcal{D}^{1} \circ \mathcal{R}_{o}=\mathrm{I}-\Pi_{o}^{2} .
\end{array}\right.$$
Note here that $\Pi_{o}^{2}$ is an obstruction for $\mathcal{R}_{o}$ to be a right inverse to $\mathcal{D}^{1}$.
Once again, we will be using partitions of unity to splice these parametrices and projections together. We will pick a partition $\left\{\mu_{+}^{2}, \mu_{o}^{2}, \mu_{-}^{2}\right\}$ on $X_{\ell}$ such that each $\mu$ satisfies $\left|\nabla^{n} \mu\right| \leq\left(\frac{2}{L_{0}}\right)^{n}$. $\mu_{+}$is supported on $X_{\ell}^{+}$and is constant outside $X_{\left[-2 L_{0},-L_{0}\right]}$. (See Figure 3.) Symmetrically, $\mu_{-}$is supported on $X_{\ell}^{-}$and is constant outside $X_{\left[L_{0}, 2 L_{0}\right]} \cdot \mu_{o}$ is, therefore, supported on $C_{2 L_{0}}$.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/c3d067ce-d69e-422c-be37-a370df27a3ab-13.jpg?height=404&width=1285&top_left_y=859&top_left_x=348}
\captionsetup{labelformat=empty}
\caption{Figure 3: Graph of $\mu_{+}$. That of $\mu_{-}$(not drawn) is the mirror image of $\mu_{+}$ on the right.}
\end{figure}

Now, we paste the parametrices $\mathcal{R}_{\#}$ 's, $\mathcal{L}_{\#}$ 's and the projections $\Pi_{\#}$ 's on the pieces, using this partition of unity, to produce $\tilde{\mathcal{R}}, \tilde{\mathcal{L}}, \tilde{\Pi}^{1}$ and $\tilde{\Pi}^{2}$. As we will be more interested in $\tilde{\mathcal{R}}$ and $\tilde{\Pi}^{2}$, we will give their explicit definitions below - of course, $\tilde{\mathcal{L}}$ and $\tilde{\Pi}^{1}$ are defined in a similar way. For $\zeta \in \mathcal{E}_{-\delta}^{2}\left(X_{\ell}\right)$,
$$\begin{aligned}
& \tilde{\mathcal{R}} \zeta=\mu_{+} \mathcal{R}_{+}\left(\mu_{+} \zeta\right)+\mu_{o} \mathcal{R}_{o}\left(\mu_{o} \zeta\right)+\mu_{-} \mathcal{R}_{-}\left(\mu_{-} \zeta\right), \\
& \tilde{\Pi}^{2} \zeta=\mu_{o} \Pi_{o}^{2}\left(\mu_{o} \zeta\right) .
\end{aligned}$$

These glued operators approximately serve as their counterparts on each piece, in the sense of the following lemma. $\tilde{\mathcal{R}}=\tilde{\mathcal{R}}_{\ell}\left(\boldsymbol{\xi}^{+}, \boldsymbol{\xi}^{-}\right): \mathcal{E}_{-\delta}^{2}\left(X_{\ell}\right) \rightarrow$ $\mathcal{E}_{-\delta}^{1}\left(X_{\ell}\right)$ is supposed to be our first approximation of a right inverse for $\mathcal{D}^{1}: \mathcal{E}_{-\delta}^{1}\left(X_{\ell}\right) \rightarrow \mathcal{E}_{-\delta}^{2}\left(X_{\ell}\right)$.

Lemma 3.2. There is a constant $\tilde{K}$ such that
$$\left\{\begin{array}{l}
\left\|\tilde{\mathcal{L}} \circ \mathcal{D}^{0}-\mathrm{I}\right\| \leq \tilde{K} \\
\left\|\mathcal{D}^{0} \circ \tilde{\mathcal{L}}+\tilde{\mathcal{R}} \circ \mathcal{D}^{1}-\mathrm{I}+\tilde{\Pi}^{1}\right\| \leq \frac{\tilde{K}}{L_{0}} \\
\left\|\mathcal{D}^{1} \circ \tilde{\mathcal{R}}-\mathrm{I}+\tilde{\Pi}^{2}\right\| \leq \frac{\tilde{K}}{L_{0}} .
\end{array}\right.$$
Proof. We prove the last estimate; the others are proved similarly. Using the fact that $\mathcal{D}^{1} \circ \mathcal{R}_{ \pm}=\mathrm{I}$ and $\mathcal{D}^{1} \circ \mathcal{R}_{o}=\mathrm{I}-\Pi_{o}^{2}$, we can write, using operator commutators,
$$\begin{aligned}
\mathcal{D}^{1} \circ \tilde{\mathcal{R}}(\zeta)= & {\left[\mathcal{D}^{1}, \mu_{+}\right] \mathcal{R}_{+}\left(\mu_{+} \zeta\right)+\left[\mathcal{D}^{1}, \mu_{o}\right] \mathcal{R}_{o}\left(\mu_{o} \zeta\right)+\left[\mathcal{D}^{1}, \mu_{-}\right] \mathcal{R}_{-}\left(\mu_{-} \zeta\right) } \\
& +\mu_{+}^{2} \zeta+\mu_{o}^{2} \zeta+\mu_{-}^{2} \zeta-\mu_{o} \Pi_{o}^{2} \mu_{o} \zeta
\end{aligned}$$
for $\zeta \in \mathcal{E}_{-\delta}^{2}\left(X_{\ell}\right)$. Therefore,
$$\mathcal{D}^{1} \circ \tilde{\mathcal{R}}(\zeta)-\zeta+\tilde{\Pi}^{2}(\zeta)=\left[\mathcal{D}^{1}, \mu_{+}\right] \mathcal{R}_{+}\left(\mu_{+} \zeta\right)+\left[\mathcal{D}^{1}, \mu_{o}\right] \mathcal{R}_{o}\left(\mu_{o} \zeta\right)+\left[\mathcal{D}^{1}, \mu_{-}\right] \mathcal{R}_{-}\left(\mu_{-} \zeta\right) .$$
Thus, to estimate $\left\|\mathcal{D}^{1} \circ \tilde{\mathcal{R}}-\mathrm{I}+\tilde{\Pi}^{2}\right\|$, we should estimate the commutator norms. Note that $\mathcal{D}^{1}(f \xi)=f \mathcal{D}^{1}(\xi)+d f \wedge \xi$, where $f$ is a scalar function and for a one-form $\omega$ on $X_{\ell}, \omega \wedge(a, \psi)=\left((\omega \wedge a)^{+}, \omega \cdot \psi\right)$, where in the second component dot denotes Clifford multiplication. As a result, the commutator $\left[\mathcal{D}^{1}, \mu_{\#}\right] \mathcal{R}_{\#}\left(\mu_{\#} \zeta\right)$ is just $d \mu_{\#} \dot{\wedge} \mathcal{R}_{\#}\left(\mu_{\#} \zeta\right)$ and, using $|\nabla \mu| \leq \frac{2}{L_{0}}$, we obtain
$$\begin{aligned}
\left\|\left[\mathcal{D}^{1}, \mu_{\#}\right] \mathcal{R}_{\#}\left(\mu_{\#} \zeta\right)\right\| & =\left\|d \mu_{\#} \dot{\lambda} \mathcal{R}_{\#}\left(\mu_{\#} \zeta\right)\right\| \\
& \leq \frac{\tilde{K}^{\prime}}{L_{0}}\left\|\mathcal{R}_{\#}\left(\mu_{\#} \zeta\right)\right\| \\
& \leq \frac{K^{\prime}}{L_{0}}\left\|\mathcal{R}_{\#}\right\| \cdot\left\|\mu_{\#} \zeta\right\| \\
& \leq \frac{\tilde{K}^{\prime \prime}}{L_{0}}\left\|\mathcal{R}_{\#}\right\| \cdot\|\zeta\|,
\end{aligned}$$
where we have everywhere used the $L_{1,-\delta}^{2}$ weighted Sobolev norm. The last inequality is justified by the Sobolev embedding $L_{3,0}^{2} \otimes L_{1,-\delta}^{2} \hookrightarrow L_{1,-\delta}^{2}$. Now, take $\tilde{K}=\frac{\tilde{K}^{\prime \prime}}{L_{0}}\left\|\mathcal{R}_{\#}\right\|$. \(\square\)

Unfortunately, $\tilde{\Pi}^{2}$ is not a projection; however, it gets closer to one as $L_{0} \rightarrow \infty$ and it has a right inverse.

Lemma 3.3. The operator $\tilde{\Pi}^{2}$ satisfies $\left\|\tilde{\Pi}^{2}-\tilde{\Pi}^{2} \circ \tilde{\Pi}^{2}\right\|_{1,-\delta} \leq K_{2} e^{-\delta L_{0}}$ and has a right-inverse, defined on $\operatorname{Im}\left(\tilde{\Pi}^{2}\right)$, whose operator norm is at most $K_{2}$.

Proof. We are going to calculate $\tilde{\Pi}^{2} \circ \tilde{\Pi}^{2}$. For this, we first find an expression for $\Pi_{o}^{2}$, which is the projection $\mathcal{E}_{\delta}^{2}(\mathbb{R} \times Y) \rightarrow \mathcal{H}_{\delta}^{2}(\mathbb{R} \times Y)$ onto the harmonic forms. Let $h_{1}, \cdots, h_{n}$ be an orthonormal base for $\mathcal{H}^{1}(\mathcal{E}(Y))$. Using our notation $\dot{\wedge}$ from the previous lemma, we construct an isometry $\mathcal{H}^{1}(\mathcal{E}(Y)) \xrightarrow{\simeq} \mathcal{H}_{\delta}^{2}(\mathbb{R} \times Y)$ given by $\eta \mapsto c e^{-\delta \tau_{o}}(d t \dot{\wedge} \eta)$, where $c$ is a constant satisfying
$$c^{2} \int_{-\infty}^{\infty} e^{-\delta \tau_{o}} d t=2$$
(Recall that we identified spinors on $Y$ with plus-spinors on the cylinder $\mathbb{R} \times Y$. Clifford multiplication by $d t$ is just an isometry between plus- and minus-spinors on the cylinder.) Using this isomorphism, we can express
$$\Pi_{o}^{2}(\zeta)=c^{2} \sum_{i=1}^{n} e^{-\delta \tau_{o}}\left(d t \dot{\wedge} h_{i}\right) \int_{\mathbb{R} \times Y}\left\langle\zeta, d t \dot{\wedge} h_{i}\right\rangle$$
for $\zeta \in \mathcal{E}_{\delta}^{2}(\mathbb{R} \times Y)$. Using the facts above, a calculation shows that
$$\tilde{\Pi}^{2} \circ \tilde{\Pi}^{2} \zeta=\frac{c^{2}}{2}\left(\int_{\mathbb{R}} \mu_{o}^{2} e^{-\delta \tau_{o}}\right) \tilde{\Pi}^{2} \zeta .$$
Now, this formula, Equation 3.2 and the fact that $\mu_{o}=1$ on $C_{L_{0}}$ give the desired estimate. Finally, the right inverse can be constructed as follows. Choose a cut-off function $\beta$, depending only on $t$ and supported in $C_{1}$, such that $\int_{\mathbb{R}} \beta(t) d t=2$. Then, define the right-inverse $F$ by $F(\zeta)=\frac{\beta}{c^{2}} e^{\delta \tau_{o}} \zeta$. Since $\mu_{o}=1$ on the support of $\beta$, it is easy to see that $\tilde{\Pi}^{2}(F \zeta)=\zeta$ for all $\zeta$. Clearly, $\|F\|$ is independent of $\ell$ and $L_{0}$. \(\square\)

As a result, for $L_{0}$ large enough, $\operatorname{Im}\left(\tilde{\Pi}^{2}\right) \cap \operatorname{Ker}\left(\tilde{\Pi}^{2}\right)=0$ and we obtain a decomposition $\mathcal{E}_{-\delta}^{2}\left(X_{\ell}\right)=\operatorname{Im}\left(\tilde{\Pi}^{2}\right) \oplus \operatorname{Ker}\left(\tilde{\Pi}^{2}\right)$. To see this, fix $L_{0}$ to satisfy $K_{2}^{2} e^{-\delta L_{0}}<\frac{1}{2}$ (or any other number less than one, for that matter). Then, if $z \in \operatorname{Im}\left(\tilde{\Pi}^{2}\right) \cap \operatorname{Ker}\left(\tilde{\Pi}^{2}\right)$, then one can express $z$ as $z=\tilde{\Pi}^{2}(F z)$. Thus,
$$\begin{aligned}
\|z\|=\left\|z-\tilde{\Pi}^{2} z\right\|= & \left\|\tilde{\Pi}^{2}(F z)-\tilde{\Pi}^{2}\left(\tilde{\Pi}^{2}(F z)\right)\right\| \leq K_{2} e^{-\delta L_{0}}\|(F z)\| \\
& \leq K_{2}^{2} e^{-\delta L_{0}}\|z\|<\frac{1}{2}\|z\|,
\end{aligned}$$
which cannot happen unless $z=0$.
By the way, the above argument also shows that if $z \in \operatorname{Im}\left(\tilde{\Pi}^{2}\right)$, then $\| z-$ $\tilde{\Pi}^{2} z\left\|\leq \frac{1}{2}\right\| z \|$. Therefore, for such a $z,\|z\| \leq 2\left\|\tilde{\Pi}^{2} z\right\|$. This will be used below
in the proof of Lemma 3.4. Finally, the decomposition results from the fact that $\operatorname{Im}\left(\tilde{\Pi}^{2}\right)$ is finite-dimensional, being identified with $\operatorname{Im}\left(\Pi_{o}^{2}\right)=\mathcal{H}_{\delta}^{2}(\mathbb{R} \times Y)$.

Define a projection $\Pi^{2}: \mathcal{E}_{-\delta}^{2}\left(X_{\ell}\right) \longrightarrow \mathcal{E}_{-\delta}^{2}\left(X_{\ell}\right)$ onto $\operatorname{Im}\left(\tilde{\Pi}^{2}\right)$ corresponding to this decomposition. Thus, $\operatorname{Im}\left(\Pi^{2}\right)=\operatorname{Im}\left(\tilde{\Pi}^{2}\right)$ and $\operatorname{Ker}\left(\Pi^{2}\right)=\operatorname{Ker}\left(\tilde{\Pi}^{2}\right)$.

Lemma 3.4. $\left\|\Pi^{2}-\tilde{\Pi}^{2}\right\|_{1,-\delta} \leq K_{2}^{\prime} e^{-\delta L_{0}}$.

Proof. Decompose $\zeta=z+z_{0}$, where $z \in \operatorname{Im}\left(\tilde{\Pi}^{2}\right)$ and $z_{0} \in \operatorname{Ker}\left(\tilde{\Pi}^{2}\right)$. Then,
$$\Pi^{2} \zeta-\tilde{\Pi}^{2} \zeta=z-\tilde{\Pi}^{2} z=\tilde{\Pi}^{2}(F z)-\tilde{\Pi}^{2}\left(\tilde{\Pi}^{2}(F z)\right) .$$
Therefore, using Lemma 3.3,
$$\left\|\Pi^{2} \zeta-\tilde{\Pi}^{2} \zeta\right\| \leq K_{2} e^{-\delta L_{0}}\|F z\| \leq K_{2}^{2} e^{-\delta L_{0}}\|z\| \leq K_{2}^{2} K_{3} e^{-\delta L_{0}}\|\zeta\|,$$
where in the last inequality, we have used the following remark (3.5). \(\square\)

Remark 3.5. If $\zeta=z+z_{0}$ is a decomposition of $\zeta$, where $z \in \operatorname{Im}\left(\tilde{\Pi}^{2}\right)$ and $z_{0} \in \operatorname{Ker}\left(\tilde{\Pi}^{2}\right)$, then there is a constant $K_{3}$ such that $\|z\|+\left\|z_{0}\right\| \leq K_{3}\|\zeta\|$.

Proof. This is a subsequence of the fact alluded to earlier. Namely, we have
$$\begin{gathered}
\|z\| \leq 2\left\|\tilde{\Pi}^{2} z\right\|=2\left\|\tilde{\Pi}^{2} \zeta\right\| \leq 2\left\|\tilde{\Pi}^{2}\right\| .\|\zeta\|, \\
\left\|z_{0}\right\| \leq\|\zeta\|+\|z\| \leq\left(1+2\left\|\tilde{\Pi}^{2}\right\|\right)\|\zeta\| .
\end{gathered}$$ \(\square\)

We will explicitly identify $\operatorname{Im}\left(\tilde{\Pi}^{2}\right)=\operatorname{Im}\left(\Pi^{2}\right)$ with the Zariski tangent space of $\mathcal{M}^{3}(Y)$ (at $[\boldsymbol{\eta}]$ ), which is a finite-dimensional vector space.

Lemma 3.6. The linear map
$$\imath: H^{1}(\mathcal{E}(Y) \mid \boldsymbol{\eta}) \longrightarrow \operatorname{Im}\left(\Pi^{2}\right) \subset \mathcal{E}_{-\delta}^{2}\left(X_{\ell}\right)$$
given by
$$\imath(\eta)=c \mu_{o} e^{-\delta\left(\tau_{o}-\ell / 2\right)}(d t \dot{\lambda} \eta)$$
is an isomorphism. It approaches an isometry as $L_{0} \rightarrow \infty$. More precisely, we have the following estimate. For some constant $K_{\imath}$,
$$\left(1-K_{\imath} e^{-\delta L_{0} / 2}\right) \leq\|\iota\| \leq\left(1+K_{\imath} e^{-\delta L_{0} / 2}\right) .$$

We will later re-scale $\imath$ to fit it into an "almost-commutative" diagram. The last statement in the lemma will be used for estimating $\|e\|$ in $\left\|\mathcal{R}_{2}\right\|$ (see Proposition 3.10).

Proof. This is a straightforward estimate. Only note that on $C_{\ell} \subset X_{\ell}$, we are using $\tau_{\ell}$, while $\tau_{o}=\ell-\tau_{\ell}$ is used on $X^{o}=\mathbb{R} \times Y$. Comparing the two norms, therefore, we have $\|\eta\|_{-\delta}=e^{-\delta \ell / 2}\|\eta\|_{\delta}$, where the first norm is measured on $X_{\ell}$ and the second on $X^{o}$. We will also use the fact that $\mu_{o}=1$ on $C_{L_{0}}$. \(\square\)

Now, we head for constructing a right inverse for $\mathcal{D}^{1}$. This will be done in three steps. In the next subsection, we will construct a right inverse $\mathcal{R}_{1}$ for $\mathcal{D}^{1}$ on the finite-codimensional subspace $\operatorname{Ker}\left(\Pi^{2}\right)$. In Section 3.4, we construct a right inverse $\mathcal{R}_{2}$ for $\mathcal{D}^{1}$ on the transversal subspace $\operatorname{Im}\left(\Pi^{2}\right)$. There, we use a stronger assumption that the fiber product of the moduli spaces of the cylindrical end manifolds is smooth in (a neighborhood of) the point under consideration. This will be explained in more detail. Finally, We show how to deform $\mathcal{R}_{1}+\mathcal{R}_{2}$ to get a right inverse $\mathcal{R}$ for $\mathcal{D}^{1}$ on all of $\mathcal{E}_{-\delta}^{2}\left(X_{\ell}\right)=\operatorname{Im}\left(\Pi^{2}\right) \oplus \operatorname{Ker}\left(\Pi^{2}\right)$.

\subsection*{3.3. Right-Inverting $\mathcal{D}^{1}$ on Finite-Codimensional $\operatorname{Ker}\left(\Pi^{2}\right)$.}

Recall that we glued the three operators $\mathcal{R}_{+}, \mathcal{R}_{-}$and $\mathcal{R}_{o}$ to obtain $\tilde{\mathcal{R}}$. We will be slightly modifying this operator to establish the existence of a right inverse $\mathcal{R}_{1}$ for $\mathcal{D}^{1}$ on $\operatorname{Ker}\left(\Pi^{2}\right)$. We extend $\mathcal{R}_{1}$ by 0 on the complementary subspace $\operatorname{Im}\left(\Pi^{2}\right)$.

Proposition 3.7. If $L_{0}$ is chosen sufficiently large, there is a constant $C_{1}$ such that the following holds. For all $\ell>4 L_{0}$, there is an operator
$$\mathcal{R}_{1}=\mathcal{R}_{1}\left(\boldsymbol{\xi}^{+}, \boldsymbol{\xi}^{-}, \ell\right): \mathcal{E}_{-\delta}^{2}\left(X_{\ell}\right) \rightarrow \mathcal{E}_{-\delta}^{1}\left(X_{\ell}\right),$$
such that
\begin{itemize}
\item[1.] For all $\zeta \in \operatorname{Ker}\left(\Pi^{2}\right) \subset \mathcal{E}_{-\delta}^{2}\left(X_{\ell}\right)$,
$$\left(\mathrm{I}-\Pi^{2}\right) \mathcal{D}^{1} \mathcal{R}_{1}(\zeta)=\zeta .$$
\item[2.] For all $\zeta \in \operatorname{Im}\left(\Pi^{2}\right)$, we have
$$\mathcal{R}_{1}(\zeta)=0 .$$
\end{itemize}
\begin{itemize}
\item[3.] The operator norm of $\mathcal{R}_{1}$ is bounded by $C_{1}$, independent of $\ell$ and $L_{0}$.
\item[4.] Define $N_{1}=N_{1}\left(\boldsymbol{\xi}^{+}, \boldsymbol{\xi}^{-}, \ell\right)$ by setting $N_{1}=\Pi^{2} \mathcal{D}^{1} \mathcal{R}_{1}$. Then, $N_{1}^{2}=0$ and the norm of this operator satisfies
$$\left\|N_{1}\right\| \leq \frac{C_{1}}{L_{0}} .$$
\item[5.] Moreover, $\mathcal{R}_{1}$ is asymptotically close to $\tilde{\mathcal{R}}$ :
$$\left\|\mathcal{R}_{1}-\tilde{\mathcal{R}}\right\| \leq \frac{C_{1}}{L_{0}} .$$
\end{itemize}

Proof. We are going to estimate the norm of the following operator, restricted to $\operatorname{Ker}\left(\Pi^{2}\right)$,
$$\left(\mathrm{I}-\Pi^{2}\right) \mathcal{D}^{1} \tilde{\mathcal{R}}: \operatorname{Ker}\left(\Pi^{2}\right) \rightarrow \operatorname{Ker}\left(\Pi^{2}\right) .$$
Let $\zeta \in \operatorname{Ker}\left(\Pi^{2}\right)$ and decompose
$$\left(\mathcal{D}^{1} \tilde{\mathcal{R}}-\mathrm{I}\right)(\zeta)=\left(\mathrm{I}-\Pi^{2}\right)\left(\mathcal{D}^{1} \tilde{\mathcal{R}} \zeta-\zeta\right)+\Pi^{2}\left(\mathcal{D}^{1} \tilde{\mathcal{R}} \zeta\right),$$
where the terms on the right-hand side belong to $\operatorname{Ker}\left(\Pi^{2}\right)$ and $\operatorname{Im}\left(\Pi^{2}\right)$, respectively. Thus, according to Remark 3.5, we have
$$\left\|\left(\mathrm{I}-\Pi^{2}\right)\left(\mathcal{D}^{1} \tilde{\mathcal{R}} \zeta-\zeta\right)\right\| \leq K_{3}\left\|\left(\mathcal{D}^{1} \tilde{\mathcal{R}}-\mathrm{I}\right)(\zeta)\right\| .$$
Now, in this norm comparison inequality, the element on the left side is $\left(\mathrm{I}-\Pi^{2}\right) \mathcal{D}^{1} \tilde{\mathcal{R}} \zeta-\zeta$ and the one on the right is $\left(\mathcal{D}^{1} \tilde{\mathcal{R}}-\mathrm{I}+\tilde{\Pi}^{2}\right)(\zeta)$, whose norm, by Lemma 3.2, is bounded by $\frac{\tilde{K}}{L_{0}}\|\zeta\|$. Thus, we obtain $\left\|\left(\mathrm{I}-\Pi^{2}\right) \mathcal{D}^{1} \tilde{\mathcal{R}} \zeta-\zeta\right\| \leq$ $\frac{K_{3} \tilde{K}}{L_{0}}\|\zeta\|$ and
$$\left\|\left(\mathrm{I}-\Pi^{2}\right) \mathcal{D}^{1} \tilde{\mathcal{R}}-\mathrm{I}\right\| \leq \frac{K_{3} \tilde{K}}{L_{0}} .$$
Choose $L_{0}$ such that $\frac{K_{3} \tilde{K}}{L_{0}}<\frac{1}{2}$. Then, the operator introduced at the beginning of the proof has an inverse of the form $J_{1}=\mathrm{I}+j_{1}$, where $j_{1}: \operatorname{Ker}\left(\Pi^{2}\right) \rightarrow \operatorname{Ker}\left(\Pi^{2}\right)$ satisfies
$$\left\|j_{1}\right\| \leq \frac{2 K_{3} \tilde{K}}{L_{0}} .$$
Now, set $\mathcal{R}_{1}=\tilde{\mathcal{R}} \circ J_{1}$ and extend $\mathcal{R}_{1}$ by zero on $\operatorname{Im}\left(\Pi^{2}\right)$. The first three items are now immediate. To prove the fourth, notice that we only need to work on $\operatorname{Ker}\left(\Pi^{2}\right)$, since $\mathcal{R}_{1}$ vanishes on $\operatorname{Im}\left(\Pi^{2}\right)$. For $\zeta \in \operatorname{Ker}\left(\Pi^{2}\right)$, we have
$$N_{1} \zeta=\Pi^{2} \mathcal{D}^{1} \mathcal{R}_{1}(\zeta)=\mathcal{D}^{1} \mathcal{R}_{1}(\zeta)-\zeta=\mathcal{D}^{1} \tilde{\mathcal{R}} J_{1} \zeta-J_{1} \zeta+j_{1} \zeta .$$

The last term already satisfies the desired estimate. On $\operatorname{Ker}\left(\Pi^{2}\right)$, we also have
$$\begin{aligned}
\left\|\mathcal{D}^{1} \tilde{\mathcal{R}} J_{1}-J_{1}\right\| \leq\left\|\mathcal{D}^{1} \tilde{\mathcal{R}}-\mathrm{I}+\tilde{\Pi}^{2}\right\| .\left\|J_{1}\right\| & \leq \frac{\tilde{K}}{L_{0}}\left(1+\frac{2 K_{3} \tilde{K}}{L_{0}}\right) \\
& \leq \frac{2 K}{L_{0}},
\end{aligned}$$
which establishes the fourth estimate.
Finally, $\mathcal{R}_{1}-\tilde{\mathcal{R}}=\tilde{\mathcal{R}} J_{1}-\tilde{\mathcal{R}}=\tilde{\mathcal{R}} j_{1}$ has the desired decay. \(\square\)

\subsection*{3.4. Right-Inverting $\mathcal{D}^{1}$ on Finite-Dimensional $\operatorname{Im}\left(\Pi^{2}\right)$.}

Consider the following diagram $(D)$.
![](https://cdn.mathpix.com/cropped/c3d067ce-d69e-422c-be37-a370df27a3ab-19.jpg?height=220&width=919&top_left_y=885&top_left_x=510)
In this diagram,
$$\begin{gathered}
r\left(\xi_{+}, \xi_{-}\right)=r_{+}\left(\xi_{+}\right)-r_{-}\left(\xi_{-}\right), \\
\jmath\left(\xi_{+}, \xi_{-}\right)=\nu_{+} \xi_{+}+\nu_{-} \xi_{-},
\end{gathered}$$
where $\nu_{+}$and $\nu_{-}$are certain cut-off functions, to be defined below. First, define
$$\nu=\int_{-2 L_{0}}^{2 L_{0}} e^{-\delta \tau_{o}(s)} \mu_{o}(s) d s$$
Then, for $(t, y) \in \mathbb{R} \times Y$,
$$\begin{aligned}
& \nu_{-}(t, y)=\frac{1}{\nu} \int_{-2 L_{0}}^{t} e^{-\delta \tau_{o}(s)} \mu_{o}(s) d s, \\
& \nu_{+}(t, y)=\frac{1}{\nu} \int_{t}^{2 L_{0}} e^{-\delta \tau_{o}(s)} \mu_{o}(s) d s .
\end{aligned}$$
We have $\nu_{+}+\nu_{-}=1$ and these cut-off functions are constant outside $C_{2 L_{0}}$. We will show shortly (in Lemma 3.9) that $\jmath$ is a quasi-isometry. Also recall that the embedding $\imath$, whose image identified with $\operatorname{Im}\left(\Pi^{2}\right)$, was defined in Lemma 3.6 by
$$\imath(\eta)=c \mu_{o} e^{-\delta\left(\tau_{o}-\ell / 2\right)}(d t \dot{\wedge} \eta)$$
and $\mathcal{D}^{1}: \mathcal{E}_{-\delta}^{1}\left(X_{\ell}\right) \rightarrow \mathcal{E}_{-\delta}^{2}\left(X_{\ell}\right)$ is the differential of SW at $\tilde{\boldsymbol{\xi}}_{\ell}=\left(\tilde{A}_{\ell}, \tilde{\Psi}_{\ell}\right)$ given by the matrix
$$\mathcal{D}^{1}=\left(\begin{array}{cc}
d^{+} & -\left.D q\right|_{\tilde{\Psi}_{\ell}} \\
\cdot \frac{1}{2} \tilde{\Psi}_{\ell} & \emptyset_{\tilde{A}_{\ell}}
\end{array}\right) .$$
$\rho$ is a right inverse for $r$ and is essential in our construction. Of course, to ensure the existence of such a right inverse, we need the following

Transversality Assumption. The limiting maps $\partial_{+}: \mathcal{M}^{*}\left(X^{+}\right) \rightarrow$ $\mathcal{M}^{i r r}(Y)$ and $\partial_{-}: \mathcal{M}^{*}\left(X^{-}\right) \rightarrow \mathcal{M}^{i r r}(Y)$ are transversal at $\boldsymbol{\xi}^{+}$and $\boldsymbol{\xi}^{-}$, where $\partial_{+}\left(\boldsymbol{\xi}^{+}\right)=\partial_{-}\left(\boldsymbol{\xi}^{-}\right)=\boldsymbol{\eta}$. In other words, the fiber product $\mathcal{M}^{*}\left(X^{+}\right) \times_{U}$ $\mathcal{M}^{*}\left(X^{-}\right)$is smooth. Equivalently, the linear map
$$\begin{gathered}
r: H^{1}\left(\left.\mathcal{E}_{-\delta}\left(X^{+}\right)\right|_{\boldsymbol{\xi}^{+}}\right) \oplus H^{1}\left(\left.\mathcal{E}_{-\delta}\left(X^{-}\right)\right|_{\boldsymbol{\xi}^{-}}\right) \rightarrow H^{1}(\mathcal{E}(Y) \mid \boldsymbol{\eta}) \\
r\left(\xi^{+}, \xi^{-}\right)=r_{+}\left(\xi^{+}\right)-r_{-}\left(\xi^{-}\right)
\end{gathered}$$
is onto. $r_{+}$and $r_{-}$are the linearized versions of $\partial_{+}$and $\partial_{-}$, respectively.
Unfortunately, the diagram $(D)$ is not commutative; fortunately, it is close to one, in the sense of the following lemma.

Lemma 3.8. In diagram $(D)$, if $L_{0}$ is chosen large enough, there is a constant $K_{D}$ such that for all $\ell \geq 4 L_{0}$ we have
$$\left\|\left(\mathcal{D}^{1} \circ \jmath\right)-c_{\ell \cdot}(\imath \circ r)\right\|_{1,-\delta} \leq K_{D} e^{-\left(\frac{\kappa+\delta}{2}\right)\left(\ell-2 L_{0}\right)},$$
where $c_{\ell}=-\frac{1}{c \nu} e^{-\delta \ell / 2}$ is a re-scaling factor.

Proof. We start by computing $\mathcal{D}^{1} \circ \jmath\left(\xi_{+}, \xi_{-}\right)$, where $\xi_{ \pm}=\left(a_{ \pm}, \psi_{ \pm}\right)$. Note that this is supported on $C_{2 L_{0}}$. A component-wise calculation shows
$$\mathcal{D}^{1}\left(\nu_{+} \xi_{+}\right)=d \nu_{+} \dot{\wedge} \xi_{+}+\nu_{+} \mathcal{D}^{1} \xi_{+}$$
and the same equation holds for $\mathcal{D}^{1}\left(\nu_{-} \xi_{-}\right)$with all the +'s and -'s reversed. Now,
$$\begin{aligned}
\mathcal{D}^{1}\left(\nu_{+} \xi_{+}\right) & =\frac{-1}{\nu} e^{-\delta \tau_{o}} \mu_{o} d t \dot{\lambda} \xi_{+}+\nu_{+} \mathcal{D}^{1} \xi_{+} \\
& =\frac{-1}{\nu} e^{-\delta \tau_{o}} \mu_{o} d t \dot{\wedge} r_{+}\left(\xi_{+}\right)+\frac{-1}{\nu} e^{-\delta \tau_{o}} \mu_{o} d t \dot{\wedge}\left(\xi_{+}-r_{+}\left(\xi_{+}\right)\right)+\nu_{+} \mathcal{D}^{1} \xi_{+} .
\end{aligned}$$
We also get a similar formula for $\mathcal{D}^{1}\left(\nu_{-} \xi_{-}\right)$, except for the sign of the first two terms. Therefore,
$$\begin{aligned}
\left(\mathcal{D}^{1} \circ \jmath\right)\left(\xi_{+}, \xi_{-}\right)= & \frac{-1}{\nu} e^{-\delta \tau_{o}} \mu_{o} d t \dot{\wedge} r\left(\xi_{+}, \xi_{-}\right) \\
& +\frac{-1}{\nu} e^{-\delta \tau_{o}} \mu_{o}\left(d t \dot{\wedge}\left(\xi_{+}-r_{+}\left(\xi_{+}\right)\right)-d t \dot{\wedge}\left(\xi_{-}-r_{-}\left(\xi_{-}\right)\right)\right) \\
& +\nu_{+} \mathcal{D}^{1} \xi_{+}+\nu_{-} \mathcal{D}^{1} \xi_{-},
\end{aligned}$$
in which the first term on the right-hand side is just $c_{\ell} .(\imath \circ r)\left(\xi_{+}, \xi_{-}\right)$. Thus, we have obtained
$$\begin{aligned}
& \left(\left(\mathcal{D}^{1} \circ \jmath\right)-c_{\ell \cdot}(\imath \circ r)\right)\left(\xi_{+}, \xi_{-}\right) \\
& =\frac{-1}{\nu} e^{-\delta \tau_{o}} \mu_{o}\left(d t \dot{\wedge}\left(\xi_{+}-r_{+}\left(\xi_{+}\right)\right)-d t \dot{\wedge}\left(\xi_{+}-r_{+}\left(\xi_{+}\right)\right)\right) \\
& \quad+\nu_{+} \mathcal{D}^{1} \xi_{+}+\nu_{-} \mathcal{D}^{1} \xi_{-}
\end{aligned}$$
Now, the result follows from the exponential decay of solutions on $X_{\ell}^{ \pm}$
$$\left\|\xi_{ \pm}-r_{+}\left(\xi_{ \pm}\right)\right\| \leq e^{-\frac{\kappa}{2}\left(\ell-2 L_{0}\right)}\left\|\xi_{ \pm}\right\|$$
and the fact that $\mathcal{D}^{1} \xi_{ \pm}$can be expressed in terms of the partition of unity $\lambda$, the components of $\boldsymbol{\xi}_{ \pm}, \xi_{ \pm}$, and their derivatives. \(\square\)

Here is the analog of Lemma 3.6.
Lemma 3.9. The linear map
$$\jmath: H^{1}\left(\left.\mathcal{E}_{-\delta}\left(X^{+}\right)\right|_{\boldsymbol{\xi}^{+}}\right) \oplus H^{1}\left(\left.\mathcal{E}_{-\delta}\left(X^{-}\right)\right|_{\boldsymbol{\xi}^{-}}\right) \rightarrow \mathcal{E}_{-\delta}^{1}\left(X_{\ell}\right)$$
in diagram ( $D$ ) defined by $\jmath\left(\xi_{+}, \xi_{-}\right)=\nu_{+} \xi_{+}+\nu_{-} \xi_{-}$is a quasi-isometry, satisfies
$$\left(1-K_{\jmath} e^{-\delta L_{0}}\right) \leq\|\jmath\| \leq\left(1+K_{\jmath} e^{-\delta l_{0}}\right)$$
and approaches an isometry as $L_{0} \rightarrow \infty$. Here, $\xi_{+}$and $\xi_{-}$are harmonic representatives of the corresponding cohomologies.

Proof. Let us first define
$$\jmath_{1}: H^{1}\left(\left.\mathcal{E}_{-\delta}\left(X^{+}\right)\right|_{\boldsymbol{\xi}^{+}}\right) \oplus H^{1}\left(\left.\mathcal{E}_{-\delta}\left(X^{-}\right)\right|_{\boldsymbol{\xi}^{-}}\right) \rightarrow \mathcal{E}_{-\delta}^{1}\left(X_{\ell}\right)$$
by $\jmath_{1}\left(\xi_{+}, \xi_{-}\right)=\mu_{+} \xi_{+}+\mu_{-} \xi_{-}$. It is straightforward to see that $\jmath_{1}$ is an isomorphism onto $\operatorname{Im}\left(\tilde{\Pi}^{1}\right)$ and satisfies $1-K_{\jmath_{1}} e^{-\delta L_{0} / 2} \leq\left\|\jmath_{1}\right\| \leq 1+K_{\jmath_{1}} e^{-\delta L_{0} / 2}$. Moreover, a calculation shows that there is a constant $K_{J}$ such that for all $L_{0} \gg 0$ and all $\ell>4 L_{0}$, we have $\left\|\jmath-\jmath_{1}\right\| \leq K_{\jmath} e^{-\delta L_{0}}$. Thus, we get the desired estimate on $\|y\|$. \(\square\)

We are now in a position to state the main result of this section, which is the counterpart of Proposition 3.7.

Proposition 3.10. Suppose that the transversality assumption holds for $\boldsymbol{\xi}^{+}$and $\boldsymbol{\xi}^{-}$. Then, if $L_{0}$ is chosen large enough, there is a constant $C_{2}$ such that the following holds. For all $\ell>4 L_{0}$, there is an operator
$$\mathcal{R}_{2}=\mathcal{R}_{2}\left(\boldsymbol{\xi}^{+}, \boldsymbol{\xi}^{-}, \ell\right): \mathcal{E}_{-\delta}^{2}\left(X_{\ell}\right) \rightarrow \mathcal{E}_{-\delta}^{1}\left(X_{\ell}\right),$$
such that
\begin{itemize}
\item[1.] For all $\zeta \in \operatorname{Im}\left(\Pi^{2}\right) \subset \mathcal{E}_{-\delta}^{2}\left(X_{\ell}\right)$,
$$\Pi^{2} \mathcal{D}^{1} \mathcal{R}_{2}(\zeta)=\zeta .$$
\item[2.] For all $\zeta \in \operatorname{Ker}\left(\Pi^{2}\right)$ we have
$$\mathcal{R}_{2}(\zeta)=0 .$$
\item[3.] The operator norm of $\mathcal{R}_{2}$ satisfies
$$\left\|\mathcal{R}_{2}\right\| \leq C_{2} e^{\delta \ell / 2} .$$
\item[4.] Define $N_{2}=N_{2}\left(\boldsymbol{\xi}^{+}, \boldsymbol{\xi}^{-}, \ell\right)$ by setting $N_{2}=\left(\mathrm{I}-\Pi^{2}\right) \mathcal{D}^{1} \mathcal{R}_{2}$. Then, $N_{2}^{2}=$ 0 and the norm of this operator satisfies
$$\left\|N_{2}\right\| \leq C_{2} e^{-(\kappa-\delta) L_{0}} .$$
\end{itemize}

Proof. First, using the almost-commutative diagram $(D)$, define
$$\tilde{\mathcal{R}}_{2}:=\frac{1}{c_{\ell}}\left(\jmath \circ \rho \circ \imath^{-1}\right): \operatorname{Im}(\imath)=\operatorname{Im}\left(\Pi^{2}\right) \rightarrow \operatorname{Im}(\jmath) .$$
Then, it is easy to see that $\left\|\tilde{\mathcal{R}}_{2}\right\| \leq \tilde{C}_{2} e^{\delta \ell / 2}$ for some constant $\tilde{C}_{2}$ and that
$$\left\|\Pi^{2} \circ \mathcal{D}^{1} \circ \tilde{\mathcal{R}}_{2}-\mathrm{I}\right\| \leq K_{D} e^{-\left(\frac{\kappa+\delta}{2}\right)\left(\ell-2 L_{0}\right)} e^{\delta \ell / 2}\|\rho\| .\left\|c^{-1}\right\| .$$
Thus, one can choose $L_{0}$ sufficiently large so that for all $\ell>4 L_{0}$, we have
$$\left\|\Pi^{2} \circ \mathcal{D}^{1} \circ \tilde{\mathcal{R}}_{2}-\mathrm{I}\right\| \leq \frac{1}{2}$$
and therefore, $\Pi^{2} \circ \mathcal{D}^{1} \circ \tilde{\mathcal{R}}_{2}$ has an inverse $J_{2}$ of norm at most 2. Setting $\mathcal{R}_{2}=\tilde{\mathcal{R}}_{2} \circ J_{2}$ (and extending by zero to the complement of $\operatorname{Im}\left(\Pi^{2}\right)$ in $\left.\mathcal{E}_{-\delta}^{2}\left(X_{\ell}\right)\right)$ gives the desired right inverse. \(\square\)

Notice that the proposition above implies that $\mathcal{D}^{1} \circ \mathcal{R}_{2}=\mathrm{I}+N_{2}$ on $\operatorname{Im}\left(\Pi^{2}\right)$, where $N_{2}$ is a nilpotent operator. Proposition 3.7 implied a similar statement, that $\mathcal{D}^{1} \circ \mathcal{R}_{1}=\mathrm{I}+N_{1}$ on $\operatorname{Ker}\left(\Pi^{2}\right)$, with a nilpotent $N_{1}$. Both $N_{1}$ and $N_{2}$ depend on $\ell$, as well as on $\boldsymbol{\xi}^{+}$and $\boldsymbol{\xi}^{-}$, since $\mathcal{R}_{1}$ and $\mathcal{R}_{2}$ do.

\subsection*{3.5. Gluing Monopoles.}

It is easy now to construct a full right inverse for $\mathcal{D}^{1}$. To begin with, set $\mathcal{R}_{0}:=\mathcal{R}_{1}+\mathcal{R}_{2}$. For a sufficiently large $L_{0}$, both of the Propositions 3.7 and 3.10 hold and we have
$$\mathcal{D}^{1} \circ \mathcal{R}_{0}=\mathrm{I}+N_{1}+N_{2} .$$
(To check this identity, verify it on elements of $\operatorname{Ker}\left(\Pi^{2}\right)$ and $\operatorname{Im}\left(\Pi^{2}\right)$.) Since $N_{1}^{2}=N_{2}^{2}=0$,
$$\left(\mathrm{I}+N_{1}+N_{2}\right)\left(\mathrm{I}-N_{1}-N_{2}\right)=\mathrm{I}-N_{1} N_{2}-N_{2} N_{1}$$
and $\mathrm{I}+N_{1}+N_{2}$ has an inverse $J$ whenever $2\left\|N_{1}\right\| .\left\|N_{2}\right\|<1$. Moreover,
$$\|J\| \leq \frac{1+\left\|N_{1}\right\|+\left\|N_{2}\right\|}{1-2\left\|N_{1}\right\| .\left\|N_{2}\right\|} .$$
But $\left\|N_{1}\right\| .\left\|N_{2}\right\|$ is bounded by $\frac{C_{1} C_{2}}{L_{0}} e^{-(\kappa-\delta) L_{0}}$, which can be made arbitrarily small by choosing $L_{0}$ large enough, since we chose $\delta<\kappa$. So, an inverse $J$ with $\|J\|<2$ exists and we define $\mathcal{R}:=\mathcal{R}_{0} \circ J$. Then, $\mathcal{R}$ is a right inverse for $\mathcal{D}^{1}$ and we have

Proposition 3.11. Suppose that the transversality assumption holds for $\boldsymbol{\xi}^{+}$and $\boldsymbol{\xi}^{-}$. Then, the operator $\mathcal{D}^{1}=D(\mathrm{SW}): \mathcal{E}_{-\delta}^{1}\left(X_{\ell}\right) \rightarrow \mathcal{E}_{-\delta}^{2}\left(X_{\ell}\right)$ has a right inverse
$$\mathcal{R}=\mathcal{R}_{\ell}\left(\boldsymbol{\xi}^{+}, \boldsymbol{\xi}^{-}\right): \mathcal{E}_{-\delta}^{2}\left(X_{\ell}\right) \rightarrow \mathcal{E}_{-\delta}^{1}\left(X_{\ell}\right),$$
for each $\ell>4 L_{0}, L_{0} \gg 1$, whose norm satisfies $\|\mathcal{R}\| \leq C e^{\delta \ell / 2}$. \(\square\)

Remark. A review of the statements of this section shows that if $U \subset$ $\mathcal{M}(Y)$ is an open set whose closure contains no reducible points, then, in each statement, we can replace $\kappa$ by an exponent $\kappa(U)$ which works for all $\boldsymbol{\eta} \in U$. This includes, in particular, Propositions 3.1, 3.7, 3.10 and 3.11. Therefore, it makes sense to consider the derivatives of the operators in question and estimate their norms. It is not hard to see that, in each case, the derivatives decay (or grow) exponentially with the same exponent as the operators themselves.

It is time to introduce our contraction mapping, whose fixed point would be the correcting perturbation term for our approximately-glued monopole.

Lemma 3.12. The following self-map $\mathcal{F}=\mathcal{F}_{\ell}\left(\boldsymbol{\xi}^{+}, \boldsymbol{\xi}^{-}\right)$of the Hilbert space $\mathcal{E}_{-\delta}^{2}\left(X_{\ell}\right)$ is a contraction on a ball for $\ell>4 L_{0}, L_{0} \gg 1$, and therefore, has a unique fixed point $\hat{\zeta}=\hat{\zeta}_{\ell}\left(\boldsymbol{\xi}^{+}, \boldsymbol{\xi}^{-}\right)$.
$$\begin{gathered}
\mathcal{F}: \mathcal{E}_{-\delta}^{2}\left(X_{\ell}\right) \rightarrow \mathcal{E}_{-\delta}^{2}\left(X_{\ell}\right)=\Omega_{+, 1,-\delta}^{2}\left(X_{\ell} ; i \mathbb{R}\right) \oplus \Gamma_{1,-\delta}\left(S^{-}\right) \\
\mathcal{F}(\zeta)=-\operatorname{SW}\left(\tilde{\boldsymbol{\xi}}_{\ell}\right)+\left(q(\psi),-\frac{1}{2} a . \psi\right),
\end{gathered}$$
where $(a, \psi)=\mathcal{R}(\zeta)$ and
$$\mathcal{R}: \Omega_{+, 1,-\delta}^{2}\left(X_{\ell} ; i \mathbb{R}\right) \oplus \Gamma_{1,-\delta}\left(S^{-}\right) \rightarrow \Omega_{2,-\delta}^{1}\left(X_{\ell} ; i \mathbb{R}\right) \oplus \Gamma_{2,-\delta}\left(S^{+}\right)$$
is a right inverse of $\mathcal{D}^{1}$ as constructed before.
Moreover, we have the following estimates on the norm of the fixed point and its image.
$$\begin{aligned}
\|\hat{\zeta}\|_{1,-\delta} & \leq C^{\prime} e^{-\kappa\left(\ell-2 L_{0}\right)}, \\
\|\mathcal{R}(\hat{\zeta})\|_{2,-\delta} & \leq C^{\prime} e^{-\kappa\left(\ell-2 L_{0}\right)} e^{\delta L_{0}} .
\end{aligned}$$
Furthermore, $\hat{\zeta}$ varies smoothly with $\boldsymbol{\xi}^{+}$and $\boldsymbol{\xi}^{-}$, so that if $\boldsymbol{\xi}^{ \pm}(t)$ are smooth, one-parameter families in $\mathcal{C}\left(X^{ \pm}\right)$with the same irreducible limiting value, then $\hat{\zeta}(t)=\hat{\zeta}_{\ell}\left(\boldsymbol{\xi}^{+}(t), \boldsymbol{\xi}^{-}(t)\right)$ is also a smooth one-parameter family and if $\hat{\zeta}^{\prime}$ denotes $\left.\frac{d}{d t} \hat{\zeta}(t)\right|_{t=0}$, then we have
$$\left\|\mathcal{R}(\hat{\zeta})^{\prime}\right\|_{2,-\delta} \leq C^{\prime} e^{-\kappa\left(\ell-2 L_{0}\right)} e^{\delta L_{0}}\left(\left\|\left(\boldsymbol{\xi}^{+}\right)^{\prime}\right\|+\left\|\left(\boldsymbol{\xi}^{-}\right)^{\prime}\right\|\right) .$$

Note. The fact that the norm of $\mathcal{R}(\hat{\zeta})^{\prime}$ is exponentially decreasing despite the possible exponential growth of the operator norm of $\mathcal{R}$ is due to the quadratic nature of $\mathcal{F}(\zeta)$ in $\zeta$. This can be seen during the proof.

Proof. Let $B(0, R)$ denote the ball of radius $R$ around the origin in the Hilbert Space $\mathcal{E}_{-\delta}^{2}\left(X_{\ell}\right)=\Omega_{+, 1,-\delta}^{2}\left(X_{\ell} ; i \mathbb{R}\right) \oplus \Gamma_{1,-\delta}\left(S^{-}\right)$. We are going to show that there is a constant $G$ such that for all $\ell \geq 4 L_{0}$, the restriction $\mathcal{F} \mid$ : $B\left(0, G e^{-2 \delta \ell}\right) \rightarrow B\left(0, G e^{-2 \delta \ell}\right)$ to the ball of radius $G e^{-2 \delta \ell}$ is a $\frac{1}{2}$-contraction. First, we consider the norm of $\mathcal{F}(0)=-\operatorname{SW}\left(\tilde{\boldsymbol{\xi}}_{\ell}\right)$. By Proposition 3.1, there is a constant $\tilde{C}$ such that
$$\|\mathcal{F}(0)\|_{1,-\delta}=\left\|\mathrm{SW}\left(\tilde{\boldsymbol{\xi}}_{\ell}\right)\right\|_{1,-\delta} \leq \tilde{C} e^{-\left(\kappa+\frac{\delta}{2}\right)\left(\ell-2 L_{0}\right)} .$$
Now, let us estimate each of the components of
$$\mathcal{F}\left(\zeta_{1}\right)-\mathcal{F}\left(\zeta_{2}\right)=\left(q\left(\psi_{1}\right)-q\left(\psi_{2}\right),-\frac{1}{2}\left(a_{1} \cdot \psi_{1}-a_{2} \cdot \psi_{2}\right)\right) .$$