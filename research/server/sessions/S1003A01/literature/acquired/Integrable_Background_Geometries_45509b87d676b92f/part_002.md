---
retention_scope: session
part: 2
total_parts: 3
---

[Part 2/3 of: Integrable Background Geometries]

For simplicity, I focus on the case of diagonal Bianchi IX metrics. Such a metric may be written in the form
$$g=w_{1} w_{2} w_{3} \mathrm{~d} t^{2}+\frac{w_{2} w_{3}}{w_{1}} \sigma_{1}^{2}+\frac{w_{3} w_{1}}{w_{2}} \sigma_{2}^{2}+\frac{w_{1} w_{2}}{w_{3}} \sigma_{3}^{2},$$
where $\sigma_{1}, \sigma_{2}, \sigma_{3}$ are the usual left-invariant 1-forms on SU(2) and $w_{1}, w_{2}, w_{3}$ are functions of $t$. If $X_{1}, X_{2}, X_{3}$ are the dual vector fields to $\sigma_{1}, \sigma_{2}, \sigma_{3}$, then the vector fields $\partial_{t}, \varphi_{1}=w_{1} X_{1}$, $\varphi_{2}=w_{2} X_{2}$ and $\varphi_{3}=w_{3} X_{3}$ form a conformal frame. Notice that $\dot{\varphi}_{1}-\left[\varphi_{2}, \varphi_{3}\right]$ is the multiple $\dot{w}_{1}-w_{2} w_{3}$ of $X_{1}$, where the dot denotes the derivative with respect to $t$. The other two components are similar. Following [47, 53], write
$$\begin{aligned}
& \dot{w}_{1}=w_{2} w_{3}-w_{1}\left(A_{2}+A_{3}\right), \\
& \dot{w}_{2}=w_{3} w_{1}-w_{2}\left(A_{3}+A_{1}\right), \\
& \dot{w}_{3}=w_{1} w_{2}-w_{3}\left(A_{1}+A_{2}\right) .
\end{aligned}$$
Comparing with equation (2.4), observe that the matrix $\mathcal{B}$ is diagonal, with eigenvalues $-\left(A_{2}+\right.$ $\left.A_{3}\right),-\left(A_{3}+A_{1}\right),-\left(A_{1}+A_{2}\right)$. In the approach of the previous section, the conformal gauge freedom is used to set $A_{1}+A_{2}+A_{3}=0$, so that $\mathcal{B}$ is traceless with eigenvalues $A_{1}, A_{2}, A_{3}$. This is not usually done in the literature, because by working with an arbitrary compatible metric, additional (non-conformally-invariant) equations can be imposed. In particular, vacuum metrics - and more generally, Kähler metrics (with antiselfdual complex structure) - are scalarflat. Hence scalar-flatness is often used as a gauge condition, in which case the following well-known system, originating in work of Brioschi, Chazy, Darboux, and Halphen, is obtained:
$$\begin{aligned}
& \dot{A}_{1}=A_{2} A_{3}-A_{1}\left(A_{2}+A_{3}\right), \\
& \dot{A}_{2}=A_{3} A_{1}-A_{2}\left(A_{3}+A_{1}\right), \\
& \dot{A}_{3}=A_{1} A_{2}-A_{3}\left(A_{1}+A_{2}\right) .
\end{aligned}$$
Joyce's lemma explains the remarkable fact that this system depends only on $w_{1}, w_{2}, w_{3}$ through the functions $A_{1}, A_{2}, A_{3}$. The trace of this system is the scalar-flat gauge condition: $\dot{A}_{1}+\dot{A}_{2}+$ $\dot{A}_{3}=-A_{2} A_{3}-A_{3} A_{1}-A_{1} A_{2}$, while the traceless part is the selfduality equation for the Weyl curvature - the latter condition is independent of the choice of conformal gauge, and may be rewritten as a matrix Riccati equation in the following way:
$$\begin{aligned}
& \mathcal{B}=\frac{1}{3}\left[\begin{array}{ccc}
2 A_{1}-A_{2}-A_{3} & 0 & 0 \\
0 & 2 A_{2}-A_{3}-A_{1} & 0 \\
0 & 0 & 2 A_{3}-A_{1}-A_{2}
\end{array}\right], \\
& \dot{\mathcal{B}}-a \mathcal{B}=2\left(\mathcal{B}^{2}\right)_{0},
\end{aligned}$$
where
$$a=-\frac{2}{3}\left(A_{1}+A_{2}+A_{3}\right) .$$
In other words, the matrix Riccati equation is obtained by separating the diagonal matrix $\mathcal{B}+a$ id, with eigenvalues $-\left(A_{2}+A_{3}\right),-\left(A_{3}+A_{1}\right),-\left(A_{1}+A_{2}\right)$, into its trace (which defines the connection $D=\partial_{t}+a$ on the one-dimensional quotient geometry), and its traceless part (which is $\mathcal{B}$ ).

One advantage of this geometric interpretation is that different gauge conditions can be easily compared. Evidently the condition $a=0$ fixes $t$ up to affine transformations. In order to interpret the scalar-flat gauge condition $\dot{a}=\frac{2}{3}\left(A_{2} A_{3}+A_{3} A_{1}+A_{1} A_{2}\right)$, it is natural and illuminating to express the right hand side in terms of $a$ and $\operatorname{tr} \mathcal{B}^{2}$. The result is
$$\dot{a}-\frac{1}{2} a^{2}=-\frac{1}{3} \operatorname{tr} \mathcal{B}^{2} .$$
Note that $\left(\partial_{t}-\frac{1}{2} a\right)\left(\partial_{t}+\frac{1}{2} a\right)=\partial_{t}^{2}+\frac{1}{2} \dot{a}-\frac{1}{4} a^{2}$, so that on sections of $L^{1 / 2}, D^{2}=\partial_{t}^{2}-\frac{1}{6} \operatorname{tr} \mathcal{B}^{2}$. Hence the scalar-flat gauge condition may be interpreted as fixing $t$ to be a projective coordinate with respect to the projective structure $D^{2}+\frac{1}{6} \operatorname{tr} \mathcal{B}^{2}$; this determines $t$ up to a projective transformation.

\section*{4 The gauge field equations}

Let ∇ be a $G$-connection, on a vector bundle $E$ over a conformal manifold $M$, which is invariant under an action of a group $H$ of conformal transformations. Infinitesimally, the generators form a Lie algebra $\mathfrak{h}$ of conformal vector fields on $M$ and there is an action of these vector fields by Lie derivative on sections of $E$ such that $\mathcal{L}_{\xi} \nabla=0$ for all $\xi \in \mathfrak{h}$. Each $\xi \in \mathfrak{h}$ therefore determines a Higgs field $S_{\xi}$ in the associated Lie algebra bundle $\mathfrak{g}_{M} \leqslant \operatorname{End}(E)$ defined by $S_{\xi} s=\mathcal{L}_{\xi} s-\nabla_{\xi} s$. (Note the unusual sign convention, which is necessary for consistency later.) Since $\mathcal{L}_{\xi} \nabla=0$ and $\left[\mathcal{L}_{\xi}, \mathcal{L}_{\chi}\right]=\mathcal{L}_{[\xi, \chi]}$, it follows that
$$\mathcal{L}_{\xi}\left(S_{\chi}\right)=S_{[\xi, \chi]}$$
and so $S: M \times \mathfrak{h} \rightarrow \mathfrak{g}_{M}$ is $H$-equivariant. Part of the curvature $F^{\nabla}$ of ∇ is determined by the Higgs fields - one readily computes that for any $\xi \in \mathfrak{h}$ and any vector field $X$,
$$F^{\nabla}(\xi, X)=\nabla_{X}\left(S_{\xi}\right) .$$
In particular, for two vector fields $\xi, \chi$ in $\mathfrak{h}$,
$$F^{\nabla}(\xi, \chi)=\left[S_{\xi}, S_{\chi}\right]_{\mathfrak{g}}-S_{[\xi, \chi]},$$
where the first bracket is the Lie bracket in $\mathfrak{g}_{M}$.
Now suppose that $H$ acts freely on $M$ with nondegenerate conformal metrics on the orbits, and define $(\alpha, \varphi)$ as in Section 2. The bundle $E$ is the pullback of a bundle, also denoted $E$, over $Q$. Since ∇ is $H$-invariant, it descends to a connection $A$ over $Q$. The Higgs fields are also $H$ -invariant; hence setting $\Phi(U)=S_{\varphi(U)}$ defines a bundle map $\Phi: \mathcal{V} \rightarrow \mathfrak{g}_{Q}$ over $Q$. Next introduce a conformal connection $D$ on $\mathcal{V}$. Then $\nabla_{X}\left(S_{\xi}\right)=\left(D_{X}^{A} \Phi\right)\left(\varphi^{-1}(\xi)\right)-\Phi\left(\varphi^{-1}\left(D_{X}^{\alpha} \varphi\right) \varphi^{-1}(\xi)\right)$ and a simple computation of the curvature of ∇ yields the following equations:
$$\begin{aligned}
& F^{\nabla}(U, V)=[\Phi(U), \Phi(V)]_{\mathfrak{g}}-\Phi\left(\varphi^{-1}[\varphi(U), \varphi(V)]_{\mathfrak{h}}\right), \\
& F^{\nabla}(U, X)=\left(D_{X}^{A} \Phi\right)(U)-\Phi\left(\varphi^{-1} D_{X}^{\alpha} \varphi(U)\right), \\
& F^{\nabla}(X, Y)=F^{A}(X, Y)-\Phi\left(\varphi^{-1} F^{\alpha}(X, Y)\right) .
\end{aligned}$$
This formulation makes manifest the analogy between $(A, \Phi)$ and $(\alpha, \varphi)$ : the former is a $G$ -connection and $\mathfrak{g}_{Q}$-valued section of $\mathcal{V}^{*}$, while the latter is an $H$-connection and $\mathfrak{h}_{Q}$-valued section of $\mathcal{V}^{*}$.

Furthermore, these formulae for $F^{\nabla}$ are closely analogous to the formulae (2.1)-(2.3) for $T^{\mathcal{D}}$ obtained in the previous section: adding torsion terms to the above equations yields
$$\begin{aligned}
& \left(F^{\nabla}+\Phi \circ T^{\mathcal{D}}\right)(U, V)=[\Phi(U), \Phi(V)]_{\mathfrak{g}}, \\
& \left(F^{\nabla}+\Phi \circ T^{\mathcal{D}}\right)(U, X)=\left(D_{X}^{A} \Phi\right)(U)-\Phi(\langle\mathcal{C}(U), X\rangle), \\
& \left(F^{\nabla}+\Phi \circ T^{\mathcal{D}}\right)(X, Y)=F^{A}(X, Y)-\Phi(\psi(X, Y)) .
\end{aligned}$$
Assuming that $T^{\mathcal{D}}$ is selfdual (which can always be arranged, using the choice of $D$, by the work of Section 2), the selfduality of $F^{\nabla}$ is now equivalent to the selfduality of the right hand sides of (4.1)-(4.3).

This reduced gauge field equation is easy to compute in each dimension (and equivalent calculations have already been used in Section 2). Notice that no assumption of selfduality on $M$ is needed for these computations: just as the selfdual Yang-Mills equation makes sense on any oriented conformal 4-manifold, so also the generalized Bogomolny equation is defined on any Weyl space, and the same is true on the one and two-dimensional geometries. However,
the principal dogma underlying this work is that the natural backgrounds for the gauge field equations are selfdual spaces, Einstein-Weyl spaces, spinor-vortex spaces and Riccati spaces. There are two reasons for this: first, the Ward correspondence predicts that the reduced gauge field equations on these backgrounds will be integrable; second, it will soon be apparent, if not already, that the gauge field equations and background equations are intimately related.

\subsection*{4.1 Generalized Nahm equations on Riccati spaces}

The reduction to one dimension is straightforward, since there is no curvature. Hence the connection $A$ on $\mathfrak{g}_{C}$ can be assumed trivial, and the gauge field equation for $\Phi \in \mathrm{C}^{\infty}\left(C, \mathcal{E}^{*} \otimes \mathfrak{g}_{C}\right)$ is
$$D \Phi-*[\Phi, \Phi]_{\mathfrak{g}}=\mathcal{B} \cdot \Phi,$$
where $\mathcal{B} \cdot \Phi=\Phi \circ \mathcal{B}$ and the Lie bracket pairing $[\Phi, \Phi]_{\mathfrak{g}} \in \mathrm{C}^{\infty}\left(C, \wedge^{2} \mathcal{E}^{*} \otimes \mathfrak{g}_{C}\right)$ is interpreted as a section of $T^{*} C \otimes \mathcal{E}^{*} \otimes \mathfrak{g}_{C}$ using the Hodge star and conformal structure on $\mathcal{E}$, together with the identifications $L_{\mathcal{E}}^{1}=L_{C}^{1}=T C$. When $\mathcal{B}=0$, this is the Nahm equation.

\subsection*{4.2 Generalized Hitchin equations on spinor-vortex spaces}

For the reduction to two dimensions, it is natural, as before, to reinterpret $\Phi$ as a complex linear map from $\mathcal{W}$ to $\mathfrak{g}_{N} \otimes \mathbb{C}$. Then the gauge field equations for $(A, \Phi)$ are
$$F^{A}-[\Phi, \bar{\Phi}]_{\mathfrak{g}}=\psi \wedge \bar{\Phi}+\bar{\psi} \wedge \Phi, \quad \bar{\partial}^{a, A} \Phi=\mathcal{C} \bar{\Phi} .$$
When $\mathcal{C}=\psi=0$ and $\mathcal{W}=T N$, with the induced holomorphic structure, these are Hitchin's equations.

To adapt the gauge field equations to spinor-vortex spaces in general signature (when there are background fields $\mathcal{C}, \widetilde{\mathcal{C}}, \psi, \widetilde{\psi}$ ), replace $\bar{\Phi}$ by an additional field $\widetilde{\Phi}$, satisfying the analogous $\partial^{a, A}$-equation. The Lorentzian reality condition $(\Phi, \widetilde{\Phi}$ real) provides a generalized chiral model, while a generalization of the harmonic map equation is obtained by introducing the crucial sign change $\widetilde{\Phi}=-\bar{\Phi}$ (recall also that $\widetilde{\psi}=-\bar{\psi}$ in this case).

\subsection*{4.3 Generalized Bogomolny equations on Einstein-Weyl spaces}

The reduction to three dimensions gives the natural generalization to Weyl geometry of the Bogomolny equation for magnetic monopoles
$$* D^{A} \Phi=F^{A} .$$
The Euclidean, hyperbolic or spherical Bogomolny equation arises when the Einstein-Weyl structure is given by a metric of constant curvature.

\section*{Addenda: twisted flat pencils and projective pairs}

The same methodology as in the nondegenerate cases yields gauge field equations over the null reductions, using the equations (2.10)-(2.12) for the torsion $T^{\mathcal{D}}$.

In the background geometry $(a, \phi, \psi)$ on $(Q, \mathcal{L})$ obtained by reduction along an $\alpha$-surface foliation, the gauge fields consist of a $G$-connection $A$ and a 1-form $\Phi$ with values in $\mathcal{L}^{2} \otimes \mathfrak{g}_{Q}$, and the gauge field equations are
$$F^{A}=\psi \wedge \Phi, \quad \mathrm{d}^{a, A} \Phi=0, \quad \frac{1}{2}[\Phi \wedge \Phi]=\chi \wedge \Phi .$$

If $\psi=\chi=0$ (so $a$ is flat, and $\mathcal{L}$ may be trivialized) then these are the equations for a pencil of flat connections $\mathrm{d}^{A}+\lambda \Phi$ on a surface (also known as the topological chiral model). Thus solutions of (4.5) may be called twisted flat pencils. The special case $\psi=0$ has been studied by Tafel and Wójcik in [52].

On a projective surface $(Q,[D])$ obtained by reduction along a $\beta$-surface foliation, the gauge fields consist of a $G$-connection $A$ and a 1-form $\Phi$ with values in $\mathcal{O}_{Q}(2) \otimes \mathfrak{g}_{Q}$ (where $\mathcal{O}_{Q}(3)=$ $\wedge^{2} T Q$ ), and the gauge field equations are
$$D^{A} \Phi=\frac{1}{2} \mathrm{~d}^{D, A} \Phi .$$
Solutions ( $A, \Phi$ ) were referred to (somewhat unimaginatively) as projective pairs in [65].
The special case of reductions of the selfdual Yang-Mills equation on $\mathbb{R}^{2,2}$ (or $\mathbb{C}^{4}$ ) by null translations was considered already by Mason and Woodhouse [41]: the $\alpha$-plane reduction (yielding flat pencils) is denoted $H_{S D}$, while the $\beta$-plane reduction (yielding projective pairs) is denoted $H_{A S D}$.

\section*{5 Interlude: spinor-vortex spaces and Hitchin's equations}

In [30], Hitchin considered solutions of the selfdual Yang-Mills equation on $\mathbb{R}^{4}$ invariant under two translations. He observed that the Yang-Mills connection could be decomposed into a connection over $\mathbb{R}^{2}$ and two Higgs fields. He combined these Higgs fields into a complex Higgs field and then noticed that, remarkably, the reduced Yang-Mills equation becomes conformally invariant provided this complex Higgs field is interpreted as a 1-form rather than a scalar. This was a surprise, because although the selfdual Yang-Mills equation is conformally invariant, the notion of translation-invariance is not. Furthermore, conformal invariance in two dimensions implies an infinite-dimensional symmetry group.

The reduction process described here provides a simple explanation of this phenomenon: $W^{-}=0$ is conformally invariant, and so is the notion of torus symmetry. Hence the equations for $\left(\bar{\partial}^{a}, \psi, \mathcal{C}, \alpha, \varphi\right)$ are conformally invariant on a fixed Riemann surface with a complex line bundle $\mathcal{W}$ and a Hermitian metric on $\mathcal{W}^{-1} T N$. In particular, it is clear that the equations (2.6)-(2.8) for $\left(\bar{\partial}^{a}, \psi, \mathcal{C}\right)$ are conformally invariant.

If $\mathcal{C}$ is not identically zero, then (on the open set where $\mathcal{C}$ is nonvanishing) the freedom in the holomorphic structure on $\mathcal{W}$ can be fixed by declaring that $\mathcal{C}$ is an identification of $\mathcal{W}^{2}$ with $T N$. The length of $\mathcal{C}$ now defines a gauge, breaking conformal invariance. More precisely, given a Weyl derivative $D$, the Chern connection on $\mathcal{W}$ only agrees with the connection induced from $T N$ if $D=D^{g}$, where $g$ is the metric induced by $|\mathcal{C}|$. Equation (2.8) becomes $\frac{1}{2} s^{g}=-2+4|\psi|_{g}^{2}$; in particular, if $\psi$ is zero, then $g$ has constant negative curvature, which is the case studied by Joyce [37], the hyperbolic spinor-vortex geometry.

On the other hand if $\mathcal{C}$ is identically zero, then $\psi$ is holomorphic, so if $\psi$ is not identically zero, then (on the open set where $\psi$ is nonvanishing), $\psi$ trivializes $\mathcal{W}$. Again this breaks conformal invariance by introducing a natural gauge, $|\psi|$; the corresponding metric has constant positive curvature $\left(s^{g}=4\right)$. This is the spherical spinor-vortex geometry.

Finally if $\mathcal{C}$ and $\psi$ both vanish, then the holomorphic structure can be fixed by setting $\mathcal{W}=$ $T N$, so that the Chern connection on $\mathcal{W}^{-1} T N$ is trivial. This trivial spinor-vortex geometry does not break conformal invariance.

The Yang-Mills equation is reduced to two dimensions by interpreting the Higgs fields as a section $\Phi$ of $\mathcal{W}^{-1} \otimes_{\mathbb{R}} \operatorname{End}(V)$, using $\varphi$. The resulting gauge field equations are independent of $(\alpha, \varphi)$, i.e., they are intrinsic to the spinor-vortex space. On a trivial spinor-vortex space, $\mathcal{W}=T N$, so $\Phi$ becomes an endomorphism-valued 1-form, and, as remarked already, the gauge field equations for $(A, \Phi)$ are Hitchin's equations. Thus it is the isomorphism $\varphi$, and the geometry
of the trivial spinor-vortex space that are responsible for the interpretation of the Higgs fields as a 1-form, rather than as scalars.

\section*{6 Selfdual spaces from gauge fields}

In Sections 2 and 4, background geometries and gauge field equations were found by reducing the selfduality equation for conformal structures and Yang-Mills fields respectively. In the approach taken, the symmetry group $H$, and the pair $(\alpha, \varphi)$ defining the reduction, decoupled from the construction, and the reduced background geometry and gauge field equations were found to be independent of these data.

In some sense, this was a sleight of hand, since $(\alpha, \varphi)$ were used to define the data on the quotient which make up the background geometry (i.e., $D, \psi$ and $\mathcal{C}$ ). However, the procedure may be turned around: starting with the background geometry, these definitions, originally obtained by imposing selfduality on the torsion $T^{\mathcal{D}}$, may be viewed as equations for the pair $(\alpha, \varphi)$. Indeed, applying $\varphi$ to the formulae (2.1)-(2.3) for $T^{\mathcal{D}}$ gives:
$$\begin{aligned}
& \left(\varphi \circ T^{\mathcal{D}}\right)(U, V)=[\varphi(U), \varphi(V)]_{\mathfrak{h}}, \\
& \left(\varphi \circ T^{\mathcal{D}}\right)(U, X)=\left(D_{X}^{\alpha} \varphi\right)(U)-\varphi(\langle\mathcal{C}(U), X\rangle), \\
& \left(\varphi \circ T^{\mathcal{D}}\right)(X, Y)=F^{\alpha}(X, Y)-\varphi(\psi(X, Y)) .
\end{aligned}$$
The right hand sides of these formulae correspond precisely to the right hand sides of (4.1)-(4.3). Hence the selfduality equation for $T^{\mathcal{D}}$ coincides with the gauge field equation for $(\alpha, \varphi)$ on the background geometry.

This leads immediately to an inverse construction of selfdual spaces with symmetry from gauge fields with $\ell$-dimensional gauge group on $k$-dimensional background geometries, where $k+\ell=4$. However, the construction can be generalized further by noting that the selfduality of $T^{\mathcal{D}}$ is implied by the gauge field equation as long as $\varphi: \mathcal{V} \rightarrow \mathfrak{h}_{Q}$ is injective. I will now explain this generalized construction.

Let $P \rightarrow Q$ be a principal $H$-bundle with an $H$-connection $\alpha$ and a Higgs field $\varphi: \mathcal{V} \rightarrow \mathfrak{h}_{Q}$, where $\mathfrak{h}_{Q}=P \times_{H}$ h. Suppose that $H$ acts transitively on an $\ell$-manifold $\Sigma^{\ell}$, where $Q$ has dimension $k=4-\ell$, so that the associated fibre bundle $P \times_{H} \Sigma^{\ell}$ is four-dimensional.

The basic example is the case that the action of $H$ is also free, in which case $\Sigma^{\ell}$ is a principal homogeneous space for $H$ and therefore there is a commuting free transitive action of a Lie group $\tilde{H}$ isomorphic to $H$. Choosing a basepoint on $\Sigma^{\ell}$ identifies $\tilde{H}$ and $\Sigma^{\ell}$ with $H$ and the two actions are the left and right regular actions. However, it can be useful to distinguish between the structure group $H$, and the symmetry group $\tilde{H}$ : if $P$ is a principal $H$-bundle over $Q$, then $P \times{ }_{H} \Sigma^{\ell}$ is a principal $\tilde{H}$-bundle.

For general $\Sigma^{\ell}$, there is still an associated bundle $\pi: P \times{ }_{H} \Sigma^{\ell} \rightarrow Q$, but this does not have any symmetries in general, since there is no longer a commuting right action of $\tilde{H}$ on $\Sigma^{\ell}$. However, the fibre of $\mathfrak{h}_{Q}=P \times_{H} \mathfrak{h}$ is still a Lie algebra of vertical vector fields on $P \times_{H} \Sigma^{\ell}$, which will be called "invariant", but for consistency with the case $\Sigma^{\ell}=H$, the Lie bracket of these vector fields is opposite to the Lie bracket in $\mathfrak{h}_{Q}$. The map $\varphi: \mathcal{V} \rightarrow \mathfrak{h}_{Q}$ therefore induces a map $\widehat{\varphi}$ from $\pi^{*} \mathcal{V}$ to the vertical bundle of $P \times_{H} \Sigma^{\ell}$. These bundles both have rank $\ell$, so let $M$ be an open subset of $P \times_{H} \Sigma^{\ell}$ where $\widehat{\varphi}$ is an isomorphism. Note that $\widehat{\varphi}$ sends basic sections to "invariant" vector fields.

Equip $T M \cong\left(\left.\pi\right|_{M}\right)^{*}(\mathcal{V} \oplus T Q)$ with the direct sum conformal structure, so that a conformal connection $D$ on $\mathcal{V}$ induces a conformal connection on $T M$. As before, a modified conformal connection $\mathcal{D}$ can be constructed, using the pullbacks of $\psi$ and $\mathcal{C}$ : the torsion of this connection will be vertical-valued, and will satisfy (6.1)-(6.3). Since $\varphi$ is injective, the torsion will be selfdual if $(\alpha, \varphi)$ satisfy the gauge field equation on $Q$. The calculation of the curvature of $\mathcal{D}$
carries over immediately to this more general setting, hence Joyce's Lemma can be applied to establish the following result.

Theorem 6.1. Let $H$ be a transitive group of diffeomorphisms of an $\ell$-manifold $\Sigma^{\ell}$. Suppose that $(\alpha, \varphi)$ is a solution of the gauge field equation (i.e., the Nahm, Hitchin or Bogomolny equation) on a principal $H$-bundle $P \rightarrow Q$, where $Q$ is a $(4-\ell)$-dimensional background geometry (i.e., an Einstein-Weyl, spinor-vortex or Riccati space). Then on the open subset $M$ of $\pi: P \times{ }_{H} \Sigma^{\ell} \rightarrow Q$ where $\widehat{\varphi}$ is an isomorphism, $(\alpha, \varphi)$ identifies $T M$ with $\pi^{*}(\mathcal{V} \oplus T Q)$, and the direct sum conformal structure is selfdual.

For later work, it will be useful to have a more explicit description of the construction of this theorem. Choose a local conformal frame $e_{i}$ for $T Q \oplus \mathcal{V}$ over $Q$ compatible with the direct sum decomposition, and a local section of $P$. Then, by identifying $M$ locally with $Q \times \Sigma^{\ell}$ and viewing the connection $\alpha$ as a $\operatorname{Vect}\left(\Sigma^{\ell}\right)$-valued 1-form on $Q$, the components of $(\alpha, \varphi)$ with respect to $e_{i}$ define four vector fields $X_{i}$ on $\Sigma^{\ell}: X_{1}, \ldots X_{k}$ are the components of the connection and $X_{k+1}, \ldots X_{4}$ are the components of $\varphi$. Since $e_{i}$ is a conformal frame on $T Q \oplus \mathcal{V}$, the conformal structure on $M$ is clearly represented contravariantly by the metric
$$\left(e_{1}-X_{1}\right)^{2}+\cdots+\left(e_{k}-X_{k}\right)^{2}+X_{k+1}^{2}+\cdots+X_{4}^{2} .$$
This is a metric on $T^{*} M$. The covariant metric on $T M$ is dual to this, and will be discussed in Section 8. In fact it is sometimes more convenient to use contravariant metrics, since they push forward easily.

Remarks 6.2.
\begin{itemize}
\item[(i)] Note that the calculations leading to this theorem are entirely formal and so, at least for local considerations, $H$ need not be finite-dimensional, but could be any subgroup of $\operatorname{Diff}\left(\Sigma^{\ell}\right)$. Hence the conformal aspects of Ward's construction [62] are included in the theorem when the background geometry is trivial.
\item[(ii)] Theorem 6.1 provides a new interpretation of the switch map [41, 43]. Let $M$ be a selfdual conformal 4-manifold with freely acting $\ell$-dimensional symmetry group $H$. Then the local quotient $Q=M / H$ is an background geometry of dimension $4-\ell$. An invariant selfdual Yang-Mills field (on a principal bundle $P$ ) with $\ell$-dimensional gauge group $G$ descends to a solution of the gauge field equation on $Q$, from which a new selfdual space $\tilde{M}$ may be constructed.
![](https://cdn.mathpix.com/cropped/c46dd08a-362a-481e-81e9-d664e136643a-22.jpg?height=247&width=263&top_left_y=1807&top_left_x=953)
Note the following features of this interpretation.
\begin{itemize}
\item[-] The construction avoids considering the $(4+\ell)$-dimensional manifold $P$ explicitly.
\item[-] The procedure decomposes into two steps of independent interest: the construction of gauge fields on $Q$ from $H$-invariant selfdual Yang-Mills fields on $M$, and the construction of selfdual spaces from gauge fields on $Q$.
\item[-] The group $G$ need not be $\ell$-dimensional, so long as it acts transitively on an $\ell$ -manifold. Hence the constructions of [19] fit into the same framework.
\end{itemize}
\item[(iii)] In the case that $\Sigma^{\ell}=H, M$ has symmetry group $H$, but enlarging the group $H$ acting on $\Sigma^{\ell}$ gives less symmetry, rather than more symmetry, since there are fewer diffeomorphisms
\end{itemize}
of $\Sigma^{\ell}$ commuting with the $H$-action. In general there will be none, and $M$ will have no symmetry. In other words, the group $H$ is a structure group rather than a symmetry group: only in the case of $H$ acting freely does it happen that the commuting symmetry group is (isomorphic to) $H$.

Selfdual conformal manifolds with symmetry groups which do not act freely are rather special: for instance they are foliated by the surfaces of equal isotropy group, and the curvature must be invariant under the isotropy representation. Some examples arise as very special cases of the constructions of this paper. More precisely, if $G$ is a (not necessarily free or transitive) group of diffeomorphisms of $\Sigma^{\ell}$, then $G$ will be a symmetry group of $M$ provided there is a representation of $G$ on $\mathcal{V}$ such that $\varphi$ and $\alpha$ are $G$-invariant. In the case that $G$ acts trivially on $\mathcal{V}$, this means that the structure group $H$ reduces to the group of diffeomorphisms of $\Sigma^{\ell}$ commuting with $G$. On the other hand, there are interesting examples where $G$ acts nontrivially on $\mathcal{V}$, see for instance [33].

The use of structure groups rather than symmetry groups also turns out to be natural when partial reductions are considered in view of the following remark. If $H$ acts freely on $M$ and $K$ is a subgroup of $H$, then $K$ also acts freely on $M$ and the structure group of $M / K$ is $H / K_{0}$ acting on $H / K$, where $K_{0}$ is the maximal normal subgroup of $H$ lying in $K$. For example, if $\operatorname{SU}(2)$ acts freely on $M$ then SO(3) acting on $S^{2}$ will be the induced structure group for $M / \mathrm{U}(1)$. In Section 8, it will be shown that such partial reductions $M / K$ arise directly from gauge fields on $M / H$ with gauge group $H / K_{0}$.

\section*{Addenda: generalized constructions from null reductions}

The same principles may be applied to null reductions to obtain constructions of selfdual 4-manifolds from twisted flat pencils and projective pairs, where the gauge group is a transitive group of diffeomorphisms of a surface $\Sigma^{2}$. The only change needed, relative to the nondegenerate case, is that the conformal structure on $M$ is obtained from the natural pairing between $V M$ and $\pi^{*} T Q$, rather than conformal structures on each summand.

The construction of selfdual conformal structures from flat pencils of connections on a surface is not at all new: as discussed in the following Interlude, it underpins Plebanski's heavenly equations and interpretations of hypercomplex and hyperkähler structures as topological chiral models. On the other hand, the construction of selfdual conformal structures from twisted flat pencils with gauge group $\operatorname{Diff}\left(\Sigma^{2}\right)$ has not been studied, as far as I am aware.

The analogous story for projective pairs on a projective surface underpins the Dunajski-West construction of selfdual conformal manifolds with a null Killing vector [72]. In [65], their construction is shown to be a reduction of gauge group from $\operatorname{Diff}\left(\Sigma^{2}\right)$ to the subgroup commuting with a nonvanishing vector field.

\section*{7 Interlude: hypercomplex and hyperkähler structures}

From the point of view of integrable systems, hypercomplex and hyperkähler 4-manifolds are considerably simpler than the general selfdual space.

Recall that a hypercomplex structure consists of a triple $I, J, K$ of integrable complex structures, satisfying the quaternionic relation $I J=K$. It is well known that a hypercomplex manifold comes equipped with a unique torsion-free connection $D$ with $D I=D J=D K=0$, called the Obata connection [45].

A hypercomplex 4-manifold possesses a canonical conformal structure, defined by requiring that $(X, I X, J X, K X)$ is a conformal frame for any nonzero tangent vector $X$. The Obata connection preserves this conformal structure, and is thus a Weyl connection. Since $I, J, K$
are anticommuting orthogonal complex structures, their (weightless) Kähler forms are either all selfdual or all antiselfdual: I fix the orientation by requiring that they are antiselfdual. Therefore $D$ is flat on $L^{2} \wedge_{-}^{2} T^{*} M$, and in particular, $M$ is a selfdual conformal manifold. The hypercomplex structure is hyperkähler if and only if $D$ is exact, i.e., the Obata connection preserves a length scale, and hence a metric in the conformal class.

The simplicity of the hypercomplex condition manifests itself in the following local description of hypercomplex 4-manifolds.

Theorem 7.1. Let $V_{0}, V_{1}, V_{2}, V_{3}$ be linearly independent vector fields on a 4-manifold $M$ and let $\eta_{0}, \eta_{1}, \eta_{2}, \eta_{3}$ be the dual coframe of 1-forms (with $\eta_{i}\left(V_{j}\right)=\delta_{i j}$ ). Define almost complex structures $I, J, K$ by
$$I V_{0}=V_{1}, \quad I V_{2}=V_{3}, \quad J V_{0}=V_{2}, \quad J V_{3}=V_{1}, \quad K V_{0}=V_{3}, \quad K V_{1}=V_{2} .$$
Then the following are equivalent.
\begin{itemize}
\item[1.] The frame $V_{i}$ satisfies the equations
$$\begin{aligned}
& {\left[V_{0}, V_{1}\right]+\left[V_{2}, V_{3}\right]=0,} \\
& {\left[V_{0}, V_{2}\right]+\left[V_{3}, V_{1}\right]=0,} \\
& {\left[V_{0}, V_{3}\right]+\left[V_{1}, V_{2}\right]=0 .}
\end{aligned}$$
\item[2.] For each $i, \mathrm{~d} \eta_{i}$ is selfdual with respect to the conformal structure represented by the metric $g=\eta_{0}^{2}+\eta_{1}^{2}+\eta_{2}^{2}+\eta_{3}^{2}$ (where $I, J, K$ are antiselfdual).
\item[3.] $(I, J, K)$ is hypercomplex with Obata connection $D$ and $\operatorname{div}^{D} \eta_{i}=0$ for all $i$.
\end{itemize}

Any hypercomplex 4-manifold $M$ arises locally in this way, and is hyperkähler if and only if the vector fields $V_{i}$ all preserve a volume form $\nu$.

The hyperkähler version of this theorem is due to Mason-Newman [40], following a construction of Ashtekar-Jacobson-Smolin [2] which will be described below. The hyperkähler case is simpler, because for $D$ exact, the $\eta_{i}$ are divergence-free with respect to $D$ if and only if the $V_{i}$ preserve a volume form - see (7.4).

The general construction was first written explicitly by Joyce [37], but the fact that all four-dimensional hypercomplex structures arise in this way is due to Dunajski [17]. The description I have given differs slightly from these references, and owes a great deal to the approaches of Hitchin [33] (see below) and Grant-Strachan [26]. Since the role of the divergence condition has perhaps not been fully elucidated before, and will be useful later, I give a complete proof.

Proof. Since
$$\eta_{i}\left(\left[V_{j}, V_{k}\right]\right)=-\mathrm{d} \eta_{i}\left(V_{j}, V_{k}\right)$$
for all $i, j, k$, it is manifest that (i) and (ii) are equivalent formulations of the same equations. Also, (7.2) and (7.3) clearly imply that $I$ is integrable since they may be rewritten as
$$\left[V_{0}+\boldsymbol{i} V_{1}, V_{2}+\boldsymbol{i} V_{3}\right]=\left[V_{0}, V_{2}\right]-\left[V_{1}, V_{3}\right]+\boldsymbol{i}\left(\left[V_{0}, V_{3}\right]+\left[V_{1}, V_{2}\right]\right)=0 .$$
Similarly (7.3) and (7.1) imply that $J$ is integrable, and (7.1) and (7.2) imply that $K$ is integrable. Now note that for any 1 -form $\eta$ on a hypercomplex manifold $\mathrm{d} \eta$ is selfdual if and only if it is orthogonal to the weightless Kähler forms of $I, J, K$. Since $D I=D J=D K=0$, this is equivalent to $I \eta, J \eta$ and $K \eta$ being divergence-free with respect to $D$ (for instance, $\operatorname{div}^{D}(I \eta)=$ $\sum_{i}\left\langle\varepsilon^{i}, I D_{e_{i}} \eta\right\rangle$, and $I$ is skew). Hence (iii) is equivalent to (i) and (ii).

On any hypercomplex manifold, the conditions $\operatorname{div}^{D} \eta=0$ and $\mathrm{d} \eta^{-}=0$ form a determined first-order linear system for a 1-form $\eta$, which therefore admits local (non-null) solutions: $(\eta, I \eta, J \eta, K \eta)$ is then a divergence-free conformal coframe.

It remains to characterize the hyperkähler case in terms of volume forms - or length scales. Suppose that $\mu=e^{f} \mu_{g}$ is a length scale; then $\mu^{-4} V_{i}=\mu^{-4} \mu_{g}^{2} \eta_{i}=e^{-2 f} \mu^{-2} \eta_{i}$ and so
$$\operatorname{div}\left(\mu^{-4} V_{i}\right)=\operatorname{div}^{D}\left(e^{-2 f} \mu^{-2} \eta_{i}\right)=\left\langle D\left(e^{-2 f} \mu^{-2}\right), \eta_{i}\right\rangle+e^{-2 f} \mu^{-2} \operatorname{div}^{D} \eta_{i} .$$
Since $\operatorname{div}^{D} \eta_{i}=0, D$ preserves the length scale $e^{f} \mu=e^{2 f} \mu_{g}$ if and only if the $V_{i}$ all preserve the volume form $\nu=\mu^{-4}$ (note that $\wedge^{4} T^{*} M \cong L^{-4}$, using the orientation of $M$ ). \(\square\)

There is an equivalent way to describe the divergence-free condition on the coframe, using spinors [17, 41]. Recall that any conformal 4-manifold locally admits (weightless) spin bundles $\$^{ \pm}$, which are $\operatorname{SL}(2, \mathbb{C})$ bundles such that $\$^{+} \otimes \$^{-}$is isomorphic to the complexified weightless cotangent bundle $L T^{*} M \otimes \mathbb{C}$ with the metric induced by the two area forms. The conventions are chosen so that $L^{2} \wedge_{-}^{2} T^{*} M \otimes \mathbb{C}=S^{2} \$^{-}$. On a hypercomplex manifold $D$ induces a flat connection on $\$^{-}$preserving the area form.

For Euclidean reality conditions, the real structure on the $L T^{*} M \otimes \mathbb{C}$ is induced by (parallel) quaternionic structures on $\$^{ \pm}$. If frames $\left(\rho_{0}, \rho_{1}\right)$ for $L^{-1} \$^{+}$and $\left(\sigma_{0}, \sigma_{1}\right)$ for $\$^{-}$are chosen so that the quaternionic structure sends $\rho_{0}$ to $\rho_{1}$ and $\sigma_{0}$ to $\sigma_{1}$, then
$$\begin{array}{rlr}
\eta_{0}+\boldsymbol{i} \eta_{1} & =\rho_{0} \otimes \sigma_{0}, & \eta_{2}+\boldsymbol{i} \eta_{3} \\
\eta_{0}-\boldsymbol{i} \eta_{1} & =\rho_{1} \otimes \sigma_{1} \otimes \sigma_{1}, & \eta_{2}-\boldsymbol{i} \eta_{3} \\
& =-\rho_{1} \otimes \sigma_{0}
\end{array}$$
defines a real conformal coframe $\left(\eta_{0}, \eta_{1}, \eta_{2}, \eta_{3}\right)$.
Proposition 7.2. Suppose that $M$ is hypercomplex with Obata connection $D$ and that $\left(\sigma_{0}, \sigma_{1}\right)$ is a $D$-parallel frame for $\$^{-}$.
\begin{itemize}
\item[1.] Let $\rho$ be a section of $L^{-1} \$^{+}$. Then $\rho \otimes \sigma_{0}$ and $\rho \otimes \sigma_{1}$ are divergence-free with respect to $D$ if and only if $\rho$ satisfies the Dirac-Weyl equation $\sum_{i} \varepsilon_{i} \cdot D_{e_{i}} \rho=0$.
\item[2.] Let $\eta$ be a 1-form. Then $\eta \cdot \sigma_{0}$ and $\eta \cdot \sigma_{1}$ satisfy the Dirac-Weyl equation if and only if $\operatorname{div}^{D} \eta=0$ and $\mathrm{d} \eta^{-}=0$.
\end{itemize}

Here the dot denotes the natural (Clifford) action $T^{*} M \otimes L^{w} \$^{ \pm} \rightarrow L^{w-1} \$^{\mp}$.
Proof. These are direct calculations:
\begin{itemize}
\item[(i)] For $A=0,1, \operatorname{div}^{D}\left(\rho \otimes \sigma_{A}\right)=\sum_{i} \varepsilon^{i}\left(D_{e_{i}} \rho \otimes \sigma_{A}\right)=\omega^{-}\left(\sum_{i} \varepsilon^{i} \cdot D_{e_{i}} \rho, \sigma_{A}\right)$.
\item[(ii)] For $A=0,1, \sum_{i} \varepsilon^{i} \cdot D_{e_{i}}\left(\eta \cdot \sigma_{A}\right)=\sum_{i} \varepsilon^{i} \cdot\left(D_{e_{i}} \eta\right) \cdot \sigma_{A}=\left(\operatorname{div}^{D} \eta\right) \sigma_{A}+\mathrm{d} \eta \cdot \sigma_{A}$.
\end{itemize}
In (i) $\omega^{-}$is the area form on $\$^{-}$, and in (ii) the Clifford action of $\mathrm{d} \eta^{+}$is trivial. \(\square\)

An important class of solutions to the equations $\operatorname{div}^{D} \eta=0$ and $\mathrm{d} \eta^{-}=0$ is obtained by taking $\eta=\mathrm{d} r$ where $\Delta^{D} r:=\operatorname{div}{ }^{D} \mathrm{~d} r=0$. Evidently the equation $\Delta^{D} r=0$ admits local solutions on any hypercomplex 4-manifold. Hence the following result is obtained, which is the original construction of Ashtekar-Jacobson-Smolin [2] in the hyperkähler case, and is due to Hitchin [33] in general.

Theorem 7.3. Let $\Phi$ be a solution of the Nahm equation (on a trivial Riccati space) with gauge group $\operatorname{Diff}\left(\Sigma^{3}\right)$ for some 3-manifold $\Sigma^{3}$. Then the selfdual space constructed from $\Phi$ is hypercomplex. Any hypercomplex 4-manifold arises locally in this way, and is hyperkähler if and only if there is a reduction to the gauge group $\operatorname{SDiff}\left(\Sigma^{3}\right)$.

Proof. Let $r$ be an affine coordinate on a trivial Riccati space $C$, choose a conformal trivialization of $\mathcal{E}$, and write the components of $\Phi$, which are vector fields on $\Sigma^{3}$, as $\left(V_{1}, V_{2}, V_{3}\right)$. Then the vector fields $\left(\partial_{r}, V_{1}, V_{2}, V_{3}\right)$ on $M \subset C \times \Sigma^{3}$ satisfy (7.1)-(7.3) as a consequence of the Nahm equation, and so the dual frame $\left(\mathrm{d} r, \eta_{1}, \eta_{2}, \eta_{3}\right)$ has $\mathrm{d} \eta_{i}$ selfdual (note that I use the opposite orientation to [33]). Conversely any hypercomplex manifold arises locally in this way by letting $r$ be a solution of $\Delta^{D} r=0$ and setting $\left(\eta_{1}, \eta_{2}, \eta_{3}\right)=(I \mathrm{~d} r, J \mathrm{~d} r, K \mathrm{~d} r)$.

Finally note that $\partial_{r}$ and $V_{i}$ preserve a volume form $e^{-4 f} \mathrm{~d} r \wedge \eta_{1} \wedge \eta_{2} \wedge \eta_{3}$ if and only if
$$\mathcal{L}_{\partial_{r}}\left(e^{-4 f} \eta_{1} \wedge \eta_{2} \wedge \eta_{3}\right)=0 \quad \text { and } \quad \mathrm{d} r \wedge \mathcal{L}_{V_{i}}\left(e^{-4 f} \eta_{1} \wedge \eta_{2} \wedge \eta_{3}\right)=0 .$$
Here I use the fact that $\mathrm{d} r\left(V_{i}\right)=0, \mathrm{~d} r\left(\partial_{r}\right)=1$ and that $\iota_{\partial_{r}}\left(e^{-4 f} \eta_{1} \wedge \eta_{2} \wedge \eta_{3}\right)=0$. The first equation says that $e^{-4 f} \eta_{1} \wedge \eta_{2} \wedge \eta_{3}$ is an $r$-independent volume element on $\Sigma^{3}$ (i.e., a parallel volume form on $C \times \Sigma^{3} \rightarrow C$ ), and the second equation says that the $V_{i}$ are volume-preserving vector fields for each fixed $r$ (i.e., on each fibre of $C \times \Sigma^{3} \rightarrow C$ ). This is exactly what it means to have a reduction to $\operatorname{SDiff}\left(\Sigma^{3}\right)$. \(\square\)

As this construction involves taking $\mathrm{d} \eta_{0}=0$, it is natural to ask if one can find divergencefree coframes with $\mathrm{d} \eta_{0}=0=\mathrm{d} \eta_{1}$ and hence formulate the hypercomplex equations as Hitchin equations on a trivial spinor-vortex space.

A number of constructions of four-dimensional hyperkähler metrics from two-dimensional integrable models are known, due to Park [46], Ward [62] and (later) Husain [34]: see [58] for a review. Unfortunately, it is not always clear in these constructions whether all hyperkähler metrics are obtained, what choices are needed to obtain the integrable model from a hyperkähler metric, and if they are compatible with Euclidean reality conditions. In particular, as far as I can tell, none of these works establish an equivalent formulation of the Euclidean hyperkähler condition as a Euclidean two-dimensional integrable model.

Indeed, the usual approach is to use the equation $\left[V_{0}+\boldsymbol{i} V_{1}, V_{2}+\boldsymbol{i} V_{3}\right]=0$ to introduce coordinates $(x, y, u, v)$ such that $V_{0}+\boldsymbol{i} V_{1}=\partial_{x}$ and $V_{2}+\boldsymbol{i} V_{3}=\partial_{y}$. There are several variations on this theme, since the meaning of $\partial_{x}$ and $\partial_{y}$ in $(x, y, u, v)$ coordinates depends on $u$ and $v$, leading to different forms for $V_{0}-\boldsymbol{i} V_{1}$ and $V_{2}-\boldsymbol{i} V_{3}$. This procedure tends to obscure the nature of the choice made to obtain the frame, making it more difficult to argue that any hyperkähler metric admits such a frame.

Fortunately there is an alternative approach, which clarifies the choice of frame, is easily made compatible with any reality conditions, and generalizes to the hypercomplex case. The following elementary observation is very well known, at least in the hyperkähler case.

Proposition 7.4. Let $z$ be a complex function on a hypercomplex 4-manifold $(M, D)$ which is holomorphic with respect to one of the complex structures. Then $\Delta^{D} z=0$, so that $\mathrm{d} z$ is a complex null 1 -form which is divergence-free with respect to $D$.

Proof. If $z$ is $I$-holomorphic, then $I \mathrm{~d} z:=-\mathrm{d} z \circ I=-\boldsymbol{i} \mathrm{d} z$. Now $I$ is skew and $D I=0$, so $\operatorname{div}^{D}(I \mathrm{~d} z)=\sum_{i}\left\langle\varepsilon^{i}, I D_{e_{i}} \mathrm{~d} z\right\rangle=0$ since $\mathrm{d}^{2} z=0$. Hence $\Delta^{D} z=\operatorname{div}^{D}(\mathrm{~d} z-\boldsymbol{i} I \mathrm{~d} z)=0$. \(\square\)

Remark 7.5. I have presented this observation using language adapted to Euclidean signature manifolds. In Kleinian signature, some of the complex structures are imaginary, so that $\boldsymbol{i} I$ (say) is a real involution, inducing a decomposition $T M=T^{+} M \oplus T^{-} M$ into its ±1 eigenspaces. These distributions are integrable, and the analogue of a holomorphic function is a function constant on one of the families of integral surfaces - such functions can of course be real valued. Note that the orientation 2-forms of these integral surfaces are the (weightless) Kähler forms of the null complex structures $J \pm i K$, which are decomposable (and up to rotation, $J$ and $i K$ are real).

The Euclidean and Kleinian cases can be considered together by first working on a complexified hypercomplex manifold, then imposing reality conditions. The above proposition applies equally in the complexified setting. Other, more Kleinian, arguments are also available (cf. [13, 50]).

Before discussing the non-null reduction to two dimensions, I will briefly discuss the null reduction (closely related to Plebanski's heavenly equations [50]) which is used in the literature to relate the selfdual vacuum equation to a topological chiral model [46, 62]. I present the generalizations to the hypercomplex case, following [17, 26].

\section*{Topological models and heavenly equations}

Choose independent functions $(w, z)$, both holomorphic with respect to $I$; then $\mathrm{d} w, \mathrm{~d} z$ are null 1-forms with $\langle\mathrm{d} w, \mathrm{~d} z\rangle=0$, and one can take these to be $\eta_{0}+\boldsymbol{i} \eta_{1}$ and $\eta_{2}+\boldsymbol{i} \eta_{3}$. This can be done compatibly with Kleinian reality conditions by taking $i I$ and $(w, z)$ real, but is incompatible with Euclidean reality conditions.

Locally, $M$ is a bundle of null surfaces over a quotient surface $N$ with coordinates $w, z$. Choosing fibre coordinates amounts to choosing a local trivialization of this bundle, and locally one can take $M=N \times \Sigma^{2}$. Then $V_{0}-i V_{1}=\partial_{w}-\alpha, V_{2}-i V_{3}=\partial_{z}-\beta, V_{0}+i V_{1}=\phi, V_{2}+i V_{3}=\psi$, where $\alpha, \beta, \phi, \psi$ are vector fields tangent to the fibres. The equations (7.1)-(7.3) now read:
$$\left[\partial_{w}-\alpha, \partial_{z}-\beta\right]=0, \quad[\phi, \psi]=0, \quad\left[\partial_{z}-\alpha, \phi\right]+\left[\partial_{w}-\beta, \psi\right]=0,$$
which are the equations for a pencil of flat connections $\mathrm{d}+A+\lambda \Phi$ with gauge group $\operatorname{Diff}\left(\Sigma^{2}\right)$, where $A=-\alpha \mathrm{d} w-\beta \mathrm{d} z$ and $\Phi=-\psi \mathrm{d} z+\phi \mathrm{d} w$. (This is also known as a topological chiral or sigma model.)

Plebanski's first and second heavenly equations [50], and their generalizations to the hypercomplex case (due to Grant-Strachan [26] and Dunajski [17] respectively) are obtained by fixing the gauge freedom in different ways.
- First, since $\mathrm{d}+A$ is flat, one can set $A=0$ (i.e., $\alpha=\beta=0$ ), then integrate the equation $\mathrm{d} \Phi=0$ (i.e., $\phi_{z}+\psi_{w}=0$ ) to get $V_{0}-\boldsymbol{i} V_{1}=\partial_{w}, V_{2}-\boldsymbol{i} V_{3}=\partial_{z}, V_{0}+\boldsymbol{i} V_{1}=U_{w}, V_{2}+\boldsymbol{i} V_{3}=-U_{z}$ for a vector field $U$ tangent to the fibres (with $U_{z}$ and $U_{w}$ linearly independent). The remaining equation is $\left[U_{w}, U_{z}\right]=0$. If $U$ is area preserving on the fibres, with local hamiltonian $\Omega$, then Plebanski's first equation $\left\{\Omega_{w}, \Omega_{z}\right\}=1$ is obtained, where $\{\cdot, \cdot\}$ denotes the Poisson bracket with respect to a suitably scaled area form on the fibres.
- Second, since $[\phi, \psi]=0$, one can choose the fibre coordinates $(x, y)$ so that $\phi=\partial_{x}$ and $\psi=-\partial_{y}$, then integrate the equation $\alpha_{x}-\beta_{y}=0$ to give $V_{0}-\boldsymbol{i} V_{1}=\partial_{w}-\gamma_{y}, V_{2}-\boldsymbol{i} V_{3}=\partial_{z}-\gamma_{x}$, $V_{0}+\boldsymbol{i} V_{1}=\partial_{x}, V_{2}+\boldsymbol{i} V_{3}=-\partial_{y}$. The remaining equation is $\gamma_{x w}-\gamma_{y z}=\left[\gamma_{x}, \gamma_{y}\right]$. Again the area preserving condition reduces everything to a single function $\Theta$, satisfying Plebanski's second heavenly equation $\Theta_{x w}+\Theta_{y z}=\left\{\Theta_{x}, \Theta_{y}\right\}$.

All complexified hypercomplex and hyperkähler metrics are obtained from these constructions, but information about Euclidean real slices is lost.

\section*{Hypercomplex structures from the Hitchin equations}

In order to obtain a formulation compatible with Euclidean reality conditions, take $z$ to be $I$-holomorphic and $\tilde{z}$ to be $(-I)$-holomorphic. Then $\mathrm{d} z$ and $\mathrm{d} \tilde{z}$ are null and so $\mathrm{d} z+\mathrm{d} \tilde{z}$ and $I(\mathrm{~d} z+\mathrm{d} \tilde{z})=-\boldsymbol{i}(\mathrm{d} z-\mathrm{d} \tilde{z})$ are orthogonal, closed, divergence-free 1-forms of the same length. Generically, this length will be nonzero on a dense open set, and one can take $\eta_{0}+\boldsymbol{i} \eta_{1}=\mathrm{d} z$ and $\eta_{0}-\boldsymbol{i} \eta_{1}=\mathrm{d} \tilde{z}$. Euclidean reality conditions are easily obtained by setting $\tilde{z}=\bar{z}$ for $I$ real.

Theorem 7.6. Let $(A, \Phi)$ be a solution to the Hitchin equations (on a trivial spinor-vortex space), with gauge group $\operatorname{Diff}\left(\Sigma^{2}\right)$ for some 2 -manifold $\Sigma^{2}$. Then the selfdual space constructed from $(A, \Phi)$ is hypercomplex. Any hypercomplex 4-manifold arises locally in this way, and is hyperkähler if and only if there is a reduction to the gauge group $\operatorname{SDiff}\left(\Sigma^{2}\right)$.

Proof. Choose conformal coordinates $z=x+\boldsymbol{i} y, \tilde{z}=x-\boldsymbol{i} y$ on a trivial spinor-vortex space and write $A=\alpha \mathrm{d} z+\widetilde{\alpha} \mathrm{d} \tilde{z}, \Phi=\phi \mathrm{d} z+\widetilde{\phi} \mathrm{d} \tilde{z}$, where $\alpha, \widetilde{\alpha}, \phi, \widetilde{\phi}$ are complex vector fields on $\Sigma^{2}$. Then the Hitchin equations become
$$\left[\partial_{z}-\alpha, \widetilde{\phi}\right]=0, \quad\left[\partial_{\tilde{z}}-\widetilde{\alpha}, \phi\right]=0, \quad\left[\partial_{z}-\alpha, \partial_{\tilde{z}}-\widetilde{\alpha}\right]-[\phi, \widetilde{\phi}]=0,$$
and so the vector fields $V_{0}-\boldsymbol{i} V_{1}=\partial_{z}-\alpha, V_{0}+\boldsymbol{i} V_{1}=\partial_{\tilde{z}}-\widetilde{\alpha}, V_{2}-\boldsymbol{i} V_{3}=\widetilde{\phi}$ and $V_{2}+\boldsymbol{i} V_{3}=\phi$ satisfy equations (7.1)-(7.3). Hence the selfdual space is hypercomplex, with a divergencefree coframe $\left(\eta_{0}, \eta_{1}, \eta_{2}, \eta_{3}\right)$ such that $\eta_{0}+\boldsymbol{i} \eta_{1}=\mathrm{d} z$ and $\eta_{0}-\boldsymbol{i} \eta_{1}=\mathrm{d} \tilde{z}$ so that $\eta_{0}$ and $\eta_{1}$ are closed. Conversely, any hypercomplex 4-manifold admits such a divergence-free coframe, so the distribution generated by $V_{2}$ and $V_{3}$ (i.e., annihilated by $\eta_{0}$ and $\eta_{1}$ ) is integrable. Under this assumption the form of the vector fields given above is entirely general, and so any hypercomplex structure arises in this way.

The characterization of the hyperkähler case is entirely analogous to Theorem 7.3: $V_{i}$ preserve a volume form $e^{-4 f} \mathrm{~d} z \wedge \mathrm{~d} \tilde{z} \wedge \eta_{2} \wedge \eta_{3}$ if and only if the area form $e^{-4 f} \eta_{2} \wedge \eta_{3}$ is parallel with respect to the connection $A=\alpha \mathrm{d} z+\widetilde{\alpha} \mathrm{d} \tilde{z}$, and the vector fields $\phi, \widetilde{\phi}$ are area-preserving (on each fibre), which is exactly what it means to have a reduction to $\operatorname{SDiff}\left(\Sigma^{2}\right)$. \(\square\)

Remark 7.7. This result can also be interpreted in Kleinian signature, when the Hitchin equations are replaced by harmonic maps into a Lie group or the principal chiral model. The latter is the context for Husain's formulation [34]. The non-null reduction (in the hyperkähler case) is also discussed briefly by Ward [62] and Ueno [58].

Although this discussion has been local, there are intriguing connections with the global geometry of elliptically fibred K3 surfaces. Yau's solution of the Calabi problem shows that on any K3 surface there is a unique hyperkähler metric in each Kähler class, but no explicit description is known. Any such hyperkähler metric will correspond to a solution of the $\operatorname{SDiff}\left(\Sigma^{2}\right)$ Hitchin equations, once a holomorphic function is chosen on a suitable open subset of the K3 surface to define the dimensional reduction. Now there are K3 surfaces which admit fibrations over $\mathbb{C P}^{1}$ (meromorphic functions) with elliptic curves as fibres, and, generically, 24 singular fibres. On the complement of the singular fibres, there is therefore a dimensional reduction to the Hitchin equations (on $\mathbb{C P}^{1}$ minus 24 points) with gauge group $\operatorname{SDiff}\left(T^{2}\right)$. The work of Gross and Wilson [27] shows that this solution is well approximated by an Abelian solution (gauge group $T^{2}$ ) defining a 'semi-flat' metric.

Remark 7.8. Continuing the development of this section, it is natural to ask if the hypercomplex equations are equivalent to the $\operatorname{Diff}\left(S^{1}\right)$ Bogomolny equation on $\mathbb{R}^{3}$. In fact, it is shown in [8] that the selfdual space constructed from a solution of the $\operatorname{Diff}\left(S^{1}\right)$ generalized Bogomolny equation on an Einstein-Weyl space $B$ is hypercomplex if $B$ is "hyperCR" (see Section 9). However, not all hypercomplex structures arise this way, since for the hyperkähler case in particular, $\operatorname{SDiff}\left(S^{1}\right)=\mathrm{U}(1)$ and only metrics with symmetry are obtained.

Remark 7.9. The Mason-Newman-Dunajski-Joyce construction of Theorem 7.1 also has a gauge-theoretic interpretation, of course: the $V_{i}$ satisfy gauge field equations on a trivial zero-dimensional geometry (!) with gauge group $\operatorname{Diff}\left(\Sigma^{4}\right)$ for some 4-manifold $\Sigma^{4}$. It has been observed in many places (in particular [40]) that these equations are the reduction of the selfdual Yang-Mills equations on $\mathbb{R}^{4}$ by four translations, and it would therefore be natural to extend the integrable
background geometries programme to the zero-dimensional case. The background geometry is a four-dimensional conformal vector space $\mathcal{M}$ together with an element $\mathcal{Y}$ of $\wedge_{-}^{2} \mathcal{M}^{*} \otimes \mathcal{M}$ which acts as a right hand side for equations (7.1)-(7.3). The background equation is an unpleasant quadratic condition on $\mathcal{Y}$, which I have left as an exercise for the enthusiastic reader: including all the constructions involving this zero-dimensional geometry would have added unnecessarily to the length of this paper.

\section*{8 Background geometries from gauge fields}

Theorem 6.1 admits the following generalization.
Theorem 8.1. Let $H$ be a transitive group of diffeomorphisms of an $\ell$-manifold $\Sigma^{\ell}$. Suppose that $(\alpha, \varphi)$ is a solution of the gauge field equation on a principal $H$-bundle $P \rightarrow Q$, where $Q$ is a $k$-dimensional background geometry and $k+\ell \leqslant 4$. Then the open subset of $\pi: P \times{ }_{H} \Sigma^{\ell} \rightarrow Q$ where $\widehat{\varphi}$ is surjective carries naturally the structure of a $(k+\ell)$-dimensional background geometry.

Proof. The idea is to apply Theorem 6.1 using the group $H \times \mathbb{R}^{4-k-\ell}$ acting on $\Sigma^{\ell} \times \mathbb{R}^{4-k-\ell}$. Suppose that $\widehat{\varphi}$ is surjective at some point $x$ of the fibre of $P \times{ }_{H} \Sigma^{\ell}$ over $q \in Q$. Let $K \leqslant \mathcal{V}$ be the kernel of $\widehat{\varphi}$ at $x$. Then there exists a solution $\left(\alpha_{0}, \varphi_{0}\right)$ of the gauge field equation, with gauge group $\mathbb{R}^{4-k-\ell}$, defined on a neighbourhood of $q$, such that $\operatorname{ker} \varphi_{0} \cap K=\{0\}$ at $q$ : the linear gauge field equation can be solved with any initial condition. The pair $\left(\widehat{\varphi}, \widehat{\varphi}_{0}\right)$ is therefore an isomorphism on a neighbourhood $M=U \times \mathbb{R}^{4-k-\ell}$ of $\{x\} \times \mathbb{R}^{4-k-\ell}$ in $\left(P \times{ }_{H} \Sigma^{\ell}\right) \times \mathbb{R}^{4-k-\ell}$.

The resulting selfdual conformal structure on $M$ clearly admits $\mathbb{R}^{4-k-\ell}$ as a symmetry group. Hence the quotient $U \subseteq P \times_{H} \Sigma^{\ell}$ is a $(k+\ell)$-dimensional background geometry by the results of Section 2. However, the conformal metric on this quotient is clearly independent of the choice of $\left(\alpha_{0}, \varphi_{0}\right)$, since the pushforward of the inverse metric (6.4) from $\Sigma^{\ell} \times \mathbb{R}^{4-k-\ell}$ to $\Sigma^{\ell}$ kills the components of the vector fields $X_{i}$ in $\mathbb{R}^{4-k-\ell}$. Hence the conformal metric is uniquely defined wherever $\widehat{\varphi}$ is surjective. One also sees that the other fields defining the background geometry are well defined, but the details here depend on the geometry and are rather complicated. The general formulae are given in the following subsections: these will complete the proof, since they are manifestly well defined. \(\square\)

I now give some explicit formulae, using the notation $(A, \Phi)$ for the gauge fields, rather than $(\alpha, \varphi)$. From the above description it is clear at least that the conformal metric on the $(k+\ell)$-dimensional background geometry may be represented contravariantly by
$$\left(e_{1}-X_{1}\right)^{2}+\cdots+\left(e_{k}-X_{k}\right)^{2}+X_{k+1}^{2}+\cdots+X_{4}^{2},$$
but note that $X_{k+1}, \ldots X_{4}$ are $4-k$ vector fields on an $\ell$-manifold $\Sigma^{\ell}$ with $\ell \leqslant 4-k$, so inverting this metric is only straightforward when $k+\ell=4$. It will be convenient therefore to introduce a volume form $\nu$ on $\Sigma^{\ell}$ and hence present the explicit formulae in an 'SDiff-gauge'. This will also make it easy to understand the volume-preserving case.

\subsection*{8.1 Riccati space constructions}

First suppose that $\Phi$ is a generalized Nahm field with values in $\operatorname{Vect}\left(\Sigma^{3}\right)$ and that $\nu$ is a volume form on $\Sigma^{3}$. Then the contravariant metric
$$\partial_{r}^{2}+\langle\Phi, \Phi\rangle \quad \text { is dual to } \quad \mathrm{d} r^{2}+\langle\eta, \eta\rangle,$$
where
$$\eta=\frac{\nu(\Phi \times \Phi, \cdot)}{\nu(\Phi \times \Phi \times \Phi)}$$
is a section of $\mathcal{E}^{*}$ with values in $\Omega^{1}\left(\Sigma^{3}\right)$ (the space of 1-forms). Here and in the following × denotes the cross product $\mathcal{E}^{*} \otimes \mathcal{E}^{*} \rightarrow L^{-1} \mathcal{E}^{*}$ (given by the wedge product and Hodge star operator): the $\operatorname{Vect}\left(\Sigma^{3}\right)$ values of $\Phi$ are then contracted into the entries of the volume form $\nu$. $\mathrm{d} r^{2}+\langle\eta, \eta\rangle$ is the covariant form of the selfdual conformal structure obtained from $\Phi$.

Now suppose that $\Phi$ is a generalized Nahm field with values in $\operatorname{Vect}\left(\Sigma^{2}\right)$ and that $\nu$ is an area form on $\Sigma^{2}$. Let $F$ be an Abelian Nahm field acting on $\mathbb{R}$ with coordinate $\theta$. Then $\Phi+F \partial_{\theta}$ is a generalized Nahm field with values in $\operatorname{Vect}\left(\Sigma^{2} \times \mathbb{R}\right)$ and $\nu \wedge \mathrm{d} \theta$ is a volume form on $\Sigma^{2} \times \mathbb{R}$. The selfdual conformal structure is therefore represented by $\mathrm{d} r^{2}+\langle\eta, \eta\rangle$ where now
$$\eta=\frac{\nu(\Phi \times \Phi) \mathrm{d} \theta+F \times \nu(\Phi, \cdot)}{\langle F, \nu(\Phi \times \Phi)\rangle} .$$
Straightforward manipulations and triple cross product identities may be used to rediagonalize the conformal metric
$$\begin{aligned}
\mathrm{d} r^{2}+\langle\eta, \eta\rangle= & \mathrm{d} r^{2}+\frac{|\nu(\Phi \times \Phi)|^{2} \mathrm{~d} \theta^{2}+2\langle\nu(\Phi \times \Phi), F \times \nu(\Phi, \cdot)\rangle \mathrm{d} \theta+|F \times \nu(\Phi, \cdot)|^{2}}{\langle F, \nu(\Phi \times \Phi)\rangle^{2}} \\
= & \mathrm{d} r^{2}+\frac{|\nu(\Phi \times \Phi)|^{2}|F \times \nu(\Phi, \cdot)|^{2}-\langle\nu(\Phi \times \Phi), F \times \nu(\Phi, \cdot)\rangle^{2}}{|\nu(\Phi \times \Phi)|^{2}\langle F, \nu(\Phi \times \Phi)\rangle^{2}} \\
& +\frac{|\nu(\Phi \times \Phi)|^{2}}{\langle F, \nu(\Phi \times \Phi)\rangle^{2}}\left(\mathrm{~d} \theta+\frac{\langle\nu(\Phi \times \Phi), F \times \nu(\Phi, \cdot)\rangle}{|\nu(\Phi \times \Phi)|^{2}}\right)^{2} \\
= & \mathrm{d} r^{2}+\frac{\langle\nu(\Phi, \cdot), \nu(\Phi, \cdot)\rangle}{|\nu(\Phi \times \Phi)|^{2}}+\frac{|\nu(\Phi \times \Phi)|^{2}}{\langle F, \nu(\Phi \times \Phi)\rangle^{2}}\left(\mathrm{~d} \theta+\frac{\langle\nu(\Phi \times \Phi), F \times \nu(\Phi, \cdot)\rangle}{|\nu(\Phi \times \Phi)|^{2}}\right)^{2} .
\end{aligned}$$
Hence the conformal structure on the quotient by $\partial_{\theta}$ is represented by the metric
$$\mathrm{d} r^{2}+\frac{\langle\nu(\Phi, \cdot), \nu(\Phi, \cdot)\rangle}{|\nu(\Phi \times \Phi)|^{2}},$$
which is, of course, inverse to $\partial_{r}^{2}+\langle\Phi, \Phi\rangle$ : note in particular that $\langle\nu(\Phi \times \Phi), \Phi\rangle=0$, expressing the fact that neither the components of $\Phi$, nor the dual 1-form components of $\nu(\Phi, \cdot)$ are linearly independent (pointwise on $\Sigma^{2}$ ).

I want to give the Weyl structure in an SDiff-gauge, with representative metric
$$|\nu(\Phi \times \Phi)|^{2} \mathrm{~d} r^{2}+\langle\nu(\Phi, \cdot), \nu(\Phi, \cdot)\rangle .$$
This metric can be conveniently diagonalized as
$$g=|\nu(\Phi \times \Phi) \mathrm{d} r+\nu(\Phi, \cdot)|^{2}$$
using the fact that $\langle\nu(\Phi \times \Phi), \nu(\Phi, \cdot)\rangle=0$. It takes quite a bit of calculation to compute the Jones-Tod Weyl structure $\omega$ in this gauge (i.e., $D=D^{g}+\omega$ ), but the result is
$$\omega=\frac{\left\langle 2 \mathcal{B}(\nu(\Phi \times \Phi))-\nu(\Phi \times \Phi) \times \operatorname{div}_{\nu} \Phi, \nu(\Phi \times \Phi) \mathrm{d} r+\nu(\Phi, \cdot)\right\rangle}{|\nu(\Phi \times \Phi)|^{2}} .$$
Writing $\nu=\mathrm{d} p \wedge \mathrm{~d} q$ and expanding the cross products in components gives a fuller expression
$$\begin{aligned}
& g=\eta_{1}^{2}+\eta_{2}^{2}+\eta_{3}^{2}, \\
& \omega=\frac{2 \sum_{j, k} \mathcal{B}_{j k} \nu_{j} \eta_{k}-\sum_{i, j, k} \varepsilon_{i j k} \nu_{i}\left(\phi_{p}^{j}+\psi_{q}^{j}\right) \eta_{k}}{\nu_{1}^{2}+\nu_{2}^{2}+\nu_{3}^{2}},
\end{aligned}$$
where
$$\begin{aligned}
& \eta_{i}=\nu_{i} \mathrm{~d} r+\phi^{i} \mathrm{~d} q-\psi^{i} \mathrm{~d} p \\
& \nu_{1}=\phi^{2} \psi^{3}-\phi^{3} \psi^{2}, \quad \nu_{2}=\phi^{3} \psi^{1}-\phi^{1} \psi^{3}, \quad \nu_{3}=\phi^{1} \psi^{2}-\phi^{2} \psi^{1},
\end{aligned}$$
and
$$\Phi=\left(\phi^{1}, \phi^{2}, \phi^{3}\right) \partial_{p}+\left(\psi^{1}, \psi^{2}, \psi^{3}\right) \partial_{q} .$$
Well, nobody said it was going to be easy! The reward is the knowledge that this Weyl structure is Einstein-Weyl if $\mathcal{B}$ satisfies the matrix Riccati equation and $\Phi$ is a generalized Nahm field on this Riccati space.

The construction of spinor-vortex spaces from Riccati spaces is perhaps the most awkward to make explicit, because of the gauge freedom in the bundle $\mathcal{W}$ on a spinor-vortex space. If $\Phi$ is a generalized Nahm field on a Riccati space with values in $\operatorname{Vect}\left(\Sigma^{1}\right)$ for a 1 -manifold $\Sigma^{1}$ with coordinate $t$, then the only natural way to proceed is to take $\mathcal{W}$ to be the kernel of $\Phi$ in the pullback of $\mathcal{E}$ to $C \times \Sigma^{1}$. This kernel is not preserved, in general, by the connection $D$ on $\mathcal{E}$, but is preserved by the conformal connection
$$\nabla=D+\frac{\Phi_{r} \triangle \Phi \mathrm{~d} r+\dot{\Phi} \triangle \Phi \mathrm{d} t}{|\Phi|^{2}},$$
where an affine coordinate $r$ and a $D$-parallel trivialization of $\mathcal{E}$ have been introduced. The complex structure on $\mathcal{W}$ is given by cross product with $\Phi /|\Phi|$, while the holomorphic structure is defined using the connection
$$\nabla+\frac{\langle\mathcal{B} \Phi, \Phi\rangle \mathrm{id}}{|\Phi|^{2}} \mathrm{~d} r$$
on $\mathcal{W}$. The other two fields on the spinor-vortex space are
$$\begin{aligned}
\mathcal{C} & =\mathcal{B}-\frac{\mathcal{B} \Phi \otimes \Phi+\Phi \otimes \mathcal{B} \Phi}{|\Phi|^{2}}+\frac{\langle\mathcal{B} \Phi, \Phi\rangle}{2|\Phi|^{2}}\left(\mathrm{id}+\frac{\Phi \otimes \Phi}{|\Phi|^{2}}\right) \\
\psi & =\frac{\Phi \times(2 \mathcal{B} \Phi+\Phi \times \dot{\Phi})}{|\Phi|^{2}} .
\end{aligned}$$
These fields satisfy the spinor-vortex equations if $\Phi$ is a generalized Nahm field on a Riccati space. (Since $\Phi /|\Phi|$ is $D$-parallel, it is reasonably straightforward to check (2.6)-(2.7) directly, although (2.8) is harder.)

\subsection*{8.2 Spinor-vortex space constructions}

The approach here is the same as in the previous subsection, and the details are slightly less complicated. For explicitness, introduce conformal coordinates $z=x+\boldsymbol{i} y, \tilde{z}=x-\boldsymbol{i} y$ on $N$ and let $\nu$ be an area form on $\Sigma^{2}$. First suppose that $(\Phi, \widetilde{\Phi}, \alpha \mathrm{d} z+\widetilde{\alpha} \mathrm{d} \tilde{z})$ is a generalized Hitchin field with values in $\operatorname{Vect}\left(\Sigma^{2}\right)$. Then the contravariant metric
$$4\left(\partial_{z}-\alpha\right)\left(\partial_{\tilde{z}}-\widetilde{\alpha}\right)+4\langle\Phi, \widetilde{\Phi}\rangle \quad \text { is dual to } \quad \mathrm{d} z \mathrm{~d} \tilde{z}+\langle\eta, \widetilde{\eta}\rangle,$$
where
$$\eta=\frac{\nu(\Phi, \cdot)+\nu(\Phi, \alpha) \mathrm{d} z+\nu(\Phi, \widetilde{\alpha}) \mathrm{d} \tilde{z}}{\nu(\Phi, \widetilde{\Phi})} \quad \text { and } \quad \widetilde{\eta}=\frac{\nu(\widetilde{\Phi}, \cdot)+\nu(\widetilde{\Phi}, \alpha) \mathrm{d} z+\nu(\widetilde{\Phi}, \widetilde{\alpha}) \mathrm{d} \tilde{z}}{\nu(\widetilde{\Phi}, \Phi)} .$$

Now suppose that $\left(\Phi \otimes \partial_{t}, \widetilde{\Phi} \otimes \partial_{t},(\alpha \mathrm{~d} z+\widetilde{\alpha} \mathrm{d} \tilde{z}) \otimes \partial_{t}\right)$ is a generalized Hitchin field with values in $\operatorname{Vect}\left(\Sigma^{1}\right)$ and that $\left(F \partial_{\theta}, \widetilde{F} \partial_{\theta},(\beta \mathrm{d} z+\widetilde{\beta} \mathrm{d} \tilde{z}) \otimes \partial_{\theta}\right)$ is an Abelian Hitchin field acting on $\mathbb{R}$ with coordinate $\theta$. Adding these together produces a generalized Hitchin field with values in $\operatorname{Vect}\left(\Sigma^{1} \times \mathbb{R}\right)$ and $\mathrm{d} t \wedge \mathrm{~d} \theta$ is an area form on $\Sigma^{1} \times \mathbb{R}$. Direct substitution gives
$$\begin{aligned}
& \eta=\frac{F(\mathrm{~d} t+\alpha \mathrm{d} z+\widetilde{\alpha} \mathrm{d} \tilde{z})-\Phi(\mathrm{d} \theta+\beta \mathrm{d} z+\widetilde{\beta} \mathrm{d} \tilde{z})}{F \widetilde{\Phi}-\Phi \widetilde{F}}, \\
& \widetilde{\eta}=\frac{\widetilde{F}(\mathrm{~d} t+\alpha \mathrm{d} z+\widetilde{\alpha} \mathrm{d} \tilde{z})-\widetilde{\Phi}(\mathrm{d} \theta+\beta \mathrm{d} z+\widetilde{\beta} \mathrm{d} \tilde{z})}{\widetilde{F} \Phi-\widetilde{\Phi} F} .
\end{aligned}$$
It is straightforward to rediagonalize $\langle\eta, \widetilde{\eta}\rangle$ to obtain the metric
$$\begin{aligned}
\mathrm{d} z \mathrm{~d} \tilde{z} & +\frac{(\mathrm{d} t+\alpha \mathrm{d} z+\widetilde{\alpha} \mathrm{d} \tilde{z})^{2}}{4 \Phi \widetilde{\Phi}} \\
& -\frac{\Phi \widetilde{\Phi}}{(F \widetilde{\Phi}-\Phi \widetilde{F})^{2}}\left(\mathrm{~d} \theta+\beta \mathrm{d} z+\widetilde{\beta} \mathrm{d} \tilde{z}-\frac{F \widetilde{\Phi}+\Phi \widetilde{F}}{2 \Phi \widetilde{\Phi}}(\mathrm{~d} t+\alpha \mathrm{d} z+\widetilde{\alpha} \mathrm{d} \tilde{z})\right)^{2}
\end{aligned} .$$
As in the Riccati space construction, the conformal structure is easy to obtain, and is dual to $4\left(\partial_{z}-\alpha\right)\left(\partial_{\tilde{z}}-\widetilde{\alpha}\right)+4 \Phi^{2} \partial_{t}^{2}$, while more work is required to compute the Jones-Tod Weyl structure $\omega$. The result, again in an SDiff-gauge (i.e., the gauge given by $\mathrm{d} t$ ) is reasonably simple, however,
$$\begin{aligned}
& g=4 \Phi \widetilde{\Phi} \mathrm{~d} z \mathrm{~d} \tilde{z}+(\mathrm{d} t+\alpha \mathrm{d} z+\widetilde{\alpha} \mathrm{d} \tilde{z})^{2}, \\
& \omega=\left(\dot{\alpha}-\frac{2 \widetilde{\mathcal{C}} \Phi}{\widetilde{\Phi}}\right) \mathrm{d} z+\left(\dot{\tilde{\alpha}}-\frac{2 \mathcal{C} \widetilde{\Phi}}{\Phi}\right) \mathrm{d} \tilde{z}-\frac{1}{2}\left(\frac{\psi+\dot{\Phi}}{\Phi}+\frac{\widetilde{\psi}+\dot{\tilde{\Phi}}}{\widetilde{\Phi}}\right)(\mathrm{d} t+\alpha \mathrm{d} z+\widetilde{\alpha} \mathrm{d} \tilde{z}) .
\end{aligned}$$
This Weyl structure is Einstein-Weyl if $(\Phi, \widetilde{\Phi}, \alpha \mathrm{d} z+\widetilde{\alpha} \mathrm{d} \tilde{z})$ is a generalized Hitchin field on a spinor-vortex space.

\subsection*{8.3 Einstein-Weyl constructions}

For completeness, I record here the explicit form of the generalized Jones-Tod construction of selfdual spaces from Einstein-Weyl spaces [36, 8]. The conformal structure on $M$ is obtained from the $\operatorname{Diff}\left(\Sigma^{1}\right)$ monopole $(A, \Phi) \partial_{t}$ on $B$ by the formula
$$\mathrm{c}=\mathrm{c}_{B}+\Phi^{-2}(\mathrm{~d} t+A)^{2},$$
where $t$ is a coordinate on $\Sigma^{1}$. Compatible metrics for c are easily obtained by introducing a compatible metric $g_{B}=\mu^{-2} \mathrm{c}_{B}$ on $B$ and writing $\Phi=V \mu^{-1}$. Then $g_{B}+V^{-2}(\mathrm{~d} t+A)^{2}$, $V g_{B}+V^{-1}(\mathrm{~d} t+A)^{2}$ and $V^{2} g_{B}+(\mathrm{d} t+A)^{2}$ are all possibilities. The latter may be written more invariantly as $\Phi^{2} \mathrm{c}_{B}+(\mathrm{d} t+A)^{2}$ : it is the SDiff-gauge determined by $\mathrm{d} t$.

\section*{Addendum: null and non-null reductions}

Unlike the preceding addenda, the main observation here is a negative one: the methods of this section do not extend readily to relate nondegenerate background geometries to the $\alpha$ and $\beta$ surface reductions. One might hope to obtain closer links by considering intermediate null reductions, in which the radical of $V M$ is both proper and nontrivial. However, this is beyond the scope of this paper.

\section*{9 Interlude: the Diff(1) Hitchin equation}

\section*{HyperCR Einstein-Weyl spaces}

An important class of Einstein-Weyl spaces are the hyperCR Einstein-Weyl spaces [22]. In [56], Paul Tod presented a way of reducing the hyperCR Einstein-Weyl equation to a single second-order differential equation for a complex function of three variables. Since the equation is expected to be integrable, he posed the problem of identifying it. In this section, I will follow a similar approach to Tod and identify the hyperCR Einstein-Weyl equation with the $\operatorname{Diff}\left(S^{1}\right)$ Hitchin equation on a trivial spinor-vortex space.

An Einstein-Weyl structure $(\mathrm{c}, D)$ on $B$ is said to be hyper $C R$ if it admits an orthonormal frame $\chi_{1}, \chi_{2}, \chi_{3}$ for the weightless (co)tangent bundle $L T^{*} B \cong L^{-1} T B$ such that $D \chi_{i}=\kappa * \chi_{i}$ for some section $\kappa$ of $L^{-1}$ and each $i$ - indeed any $\chi$ in the unit sphere generated by $\chi_{1}, \chi_{2}, \chi_{3}$ satisfies the same equation; these $\chi$ 's are called the hyperCR congruences of $B$.

Since the Weyl connection is torsion-free and conformal, it is easy to see that these equations are implied by their skew parts
$$\begin{aligned}
& \mathrm{d}^{D} \chi_{1}=2 \kappa \chi_{2} \wedge \chi_{3}, \\
& \mathrm{~d}^{D} \chi_{2}=2 \kappa \chi_{3} \wedge \chi_{1}, \\
& \mathrm{~d}^{D} \chi_{3}=2 \kappa \chi_{1} \wedge \chi_{2} .
\end{aligned}$$
Tod noticed that $\chi_{i}$ satisfying (9.1)-(9.3) determine the Einstein-Weyl space: the conformal metric is $\chi_{1}^{2}+\chi_{2}^{2}+\chi_{3}^{2}$ and the Einstein-Weyl equation follows from (9.1)-(9.3) - see also [10, 22]. Now introduce a gauge $\mu$ with $D \mu=\omega \mu$ and define 1-forms $\alpha_{i}=2 \mu^{-1} \chi_{i}$. Then the equations (9.1)-(9.3) may be rewritten in the form given by Tod [56]:
$$\begin{aligned}
& \mathrm{d} \alpha_{1}=-\omega \wedge \alpha_{1}+\kappa \alpha_{2} \wedge \alpha_{3}, \\
& \mathrm{~d} \alpha_{2}=-\omega \wedge \alpha_{2}+\kappa \alpha_{3} \wedge \alpha_{1}, \\
& \mathrm{~d} \alpha_{3}=-\omega \wedge \alpha_{3}+\kappa \alpha_{1} \wedge \alpha_{2} .
\end{aligned}$$
These equations are easier to interpret after complexification, so that the conformal structure is determined by its null lines, which form a bundle of conics in $P\left(T^{*} B\right)$. This bundle is trivial, since $T^{*} B$ is trivialized by $\alpha_{1}, \alpha_{2}, \alpha_{3}$. The pullback of the tautological 1-form on $P\left(T^{*} B\right)$ by a constant section is a constant linear combination of $\alpha_{1}, \alpha_{2}$ and $\alpha_{3}$, which is null for a section of the bundle of conics. Then (9.4)-(9.6) are equivalent to the integrability of the distributions defined by these null 1-forms, i.e., to the integrability of a rank 2 distribution $\mathcal{H}$ on the bundle of conics. The integral surfaces are the null surfaces which motivated Cartan [12] to study 3-dimensional Einstein-Weyl geometry, and the quotient of the bundle of conics by $\mathcal{H}$ is the minitwistor space $\mathcal{S}$ of $B$ [29].