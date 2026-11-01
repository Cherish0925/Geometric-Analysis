---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Selfdual spaces with complex structures, Einstein-Weyl geometry and geodesics]

Now suppose that $B$ is Einstein-Weyl and that $w$ is any nonvanishing monopole, and let $M$ be the corresponding selfdual conformal 4-manifold. Then each shear-free geodesic congruence $\chi$ induces on $M$ an invariant antiselfdual complex structure $J$. On the other hand if we fix $\chi$, then, as we have seen, its divergence and twist, $\tau$ and $\kappa$, are monopoles on $B$. Using these we can characterise special cases of the construction as follows.
\begin{itemize}
\item[(i)] $(M, J)$ is locally scalar-flat Kähler if and only if $\kappa=a w$ for some constant $a$, and if $a$ is nonzero, we may assume $a=1$, by normalising $w$.
\item[-] If $\kappa=0$ then $M$ is locally scalar-flat Kähler and $K$ is a holomorphic Killing field. If $\tau=b w$, then $M$ is locally hyperKähler [19], [20].
\item[-] If $\kappa=w$ then $M$ is locally scalar-flat Kähler and $K$ is a holomorphic homothetic vector field.
\item[(ii)] $(M, J)$ is locally hypercomplex if and only if $\tau=b w$ for some constant $b$, and if $b$ is nonzero, we may assume $b=1$, by normalising $w$.
\item[-] If $\tau=0$ then $M$ is locally hypercomplex and $K$ is a triholomorphic vector field. If $\kappa=a w$, then $M$ is locally hyperKähler (see [7], [12]).
\item[-] If $\tau=w$ then $M$ is locally hypercomplex and $K$ is a hypercomplex vector field.
\end{itemize}

Here we say a conformal vector field on a hypercomplex 4-manifold is hypercomplex if and only if $\mathcal{L}_{K} D=0$ where $D$ is the Obata connection. It follows that for each of the hypercomplex structures $I, \mathcal{L}_{K} I$ is a $D$-parallel antiselfdual endomorphism anticommuting with $I$. The map $I \mapsto \mathcal{L}_{K} I \perp I$
is therefore given by $I \mapsto[c J, I]$ for one of the hypercomplex structures $J$ and a real constant $c$. Consequently $K$ is holomorphic with respect to $\pm J$, and is triholomorphic if and only if $c=0$.

The twistorial interpretation of the above special cases is as follows. Firstly, if $\kappa=0$ on $B$ then the corresponding line bundle on $\mathcal{S}$ is trivial; hence so is its pullback to $Z$. On the other hand, if $\kappa=w$ then the line bundle on $\mathcal{S}$ is nontrivial, but we are pulling it back to (an open subset of) its total space. Such a pullback has a tautological section, and hence is trivial away from the zero section. The story for $\tau$ is similar.

We now combine these observations with the mini-Kerr theorem.
4.3. Theorem. - Let $B$ be an arbitrary three dimensional Einstein-Weyl space.
(i) $B$ may be obtained (locally) as the quotient of a scalar-flat Kähler 4-manifold by a holomorphic homothetic vector field.
(ii) It may also be obtained as the quotient of a hypercomplex 4-manifold by a hypercomplex vector field.
(iii) $B$ is locally the quotient of a hyperKähler 4-manifold by a holomorphic homothetic vector field if and only if it admits a shear-free geodesic congruence with linearly dependent divergence and twist.

Proof. - By the mini-Kerr theorem $B$ admits a shear-free geodesic congruence. The divergence $\tau$ and twist $\kappa$ are monopoles on $B$, which may be used to construct the desired hypercomplex and scalar-flat Kähler spaces wherever they are nonvanishing. The hyperKähler case was characterised above by the constancy of $\tau_{0}$ and $\kappa_{0}$. On $B$, this implies that $\tau$ and $\kappa$ are linearly dependent, i.e., $c_{1} \tau+c_{2} \kappa=0$ for constants $c_{1}$ and $c_{2}$. Conversely given an Einstein-Weyl space with a shear-free geodesic congruence $\chi$ whose divergence and twist satisfy this condition, any nonvanishing monopole $w$ with $\kappa=a w$ and $\tau=b w$ gives rise to a hyperKähler metric (and this $w$ is unique up to a constant multiple unless $\tau=\kappa=0$ ). \(\square\)

Maciej Dunajski and Paul Tod [8] have recently obtained a related description of hyperKähler metrics with homothetic vector fields by reducing Plebanski's equations.

The following diagram (Fig. 1) conveniently summarises the various Weyl derivatives involved in the constructions of this section, together with the 1-forms translating between them.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/2f68b6dd-6e06-42d9-a8ed-04b5eeba303b-30.jpg?height=334&width=754&top_left_y=269&top_left_x=314}
\captionsetup{labelformat=empty}
\caption{Figure 1}
\end{figure}

The Weyl derivatives in the right hand column are so labelled because on $B$ we have $D^{L W} \xrightarrow{+\tau \chi} D^{\chi} \xrightarrow{+\tau \chi} D^{B}$, where $D^{B}$ is Einstein-Weyl, $D^{\chi}$ is the Weyl derivative canonically associated to the congruence $\chi$, and, in the case that $\kappa=0, D^{L W}$ is the LeBrun-Ward gauge. The central role played by $D^{\text {sd }}$ in these constructions explains the frequent occurrence of the Ansatz $g=V g_{B}+V^{-1}(d t+A)^{2}$ for selfdual metrics with symmetry. In particular, if $g_{B}$ is the LeBrun-Ward gauge of a LeBrun-Ward geometry and $V$ is a monopole in this gauge, then $g$ is a scalar-flat Kähler metric.

\section*{5. Selfdual Einstein 4-manifolds with symmetry.}

In this section we combine results of Tod [31] and Pedersen and Tod [27] to show that the constructions of the previous section cover essentially all selfdual Einstein metrics with symmetry.
5.1. Proposition (cf. [27]). - Let $g$ be a four dimensional Einstein metric with a conformal vector field $K$. Then one of the following must hold:
\begin{itemize}
\item[(i)] $K$ is a Killing field of $g$;
\item[(ii)] $g$ is Ricci-flat and $K$ is a homothetic vector field (i.e., $\mathcal{L}_{K} D^{g}=0$ );
\item[(iii)] $g$ is conformally flat.
\end{itemize}

Now suppose $g$ is a selfdual Einstein metric with nonzero scalar curvature and a conformal vector field $K$. Then, except in the conformally flat case, $K$ is a Killing field of $g$ and so we may apply the following.
5.2. Theorem (cf. [31]). - Let $g$ be a selfdual Einstein metric with nonzero scalar curvature and $K$ a Killing field of $g$. Then the antiselfdual
part of $D^{g} K$ is nonzero, and is a pointwise multiple of an integrable complex structure $J$. The corresponding Kähler-Weyl structure is Kähler, and $K$ is also a Killing field for the Kähler metric.

If, on the other hand, scal ${ }^{g}$ is zero, then $g$ itself is (locally) a hyperKähler metric and, unless $g$ is conformally flat, $\mathcal{L}_{K} D^{g}=0$, and so $K$ is a hypercomplex vector field. In the conformally flat case, $K$ may not be a homothety of $g$, but it is at least a homothety with respect to some compatible flat metric. Thus, in any case, the conformal vector field $K$ is holomorphic with respect to some Kähler structure on $M$.

We end this section by noting that in the case of selfdual Einstein metrics with Killing fields, Tod's work [31] shows how to recover the Einstein metric from the LeBrun-Ward geometry. More precisely, if $M$ is a selfdual Einstein 4-manifold with a Killing field, and $B$ is the LeBrun-Ward quotient of the corresponding scalar-flat Kähler metric, then either $B$ is flat, or the monopole defining $M$ is of the form
$$w=\left(a\left(1-\frac{1}{2} z u_{z}\right)+\frac{1}{2} b u_{z}\right) \mu_{L W}^{-1},$$
where $u(x, y, z)$ is the solution of the $\operatorname{SU}(\infty)$ Toda field equation, and $a, b \in \mathbb{R}$ are not both zero. Conversely, for any LeBrun-Ward geometry (given by $u$ ), the section $\left(a\left(1-\frac{1}{2} z u_{z}\right)+\frac{1}{2} b u_{z}\right) \mu_{L W}^{-1}$ of $L^{-1}$ is a monopole for any $a, b \in \mathbb{R}$, and if $g_{K}$ is the corresponding Kähler metric, then $(a z-b)^{-2} g_{K}$ is Einstein with scalar curvature -12a. When $a=0$, we reobtain the case of hyperKähler metrics with Killing fields, while if $a \neq 0$, one can set $b=0$ by translating the $z$ coordinate (although $u$ will be a different function of the new $z$ coordinate).

\section*{6. Einstein-Weyl structures from $\mathbb{R}^{4}$.}

Our aim in the remaining sections is to unify and extend many of the examples of Kähler-Weyl structures with symmetry studied up to the present, using the framework developed in Sections 2-4. We discuss both the simplest and most well known cases and also more complicated examples which we believe are new. We begin with $\mathbb{R}^{4}$.

A conformally flat 4-manifold is both selfdual and antiselfdual, so when we apply the Jones and Tod construction we have the freedom to reverse the orientation. Consequently, not only is $D^{B}=D^{|K|}+\omega$ Einstein-Weyl, but so is $\widetilde{D}^{B}=D^{|K|}-\omega$. Therefore
$$0=\operatorname{sym}_{0}\left(D^{B} \omega+\omega \otimes \omega\right)=\operatorname{sym}_{0} D^{|K|} \omega=\operatorname{sym}_{0}\left(\widetilde{D}^{B} \omega-\omega \otimes \omega\right) .$$

Since $|K|^{-1}$ is a monopole, $g=|K|^{-2} \boldsymbol{c}_{B}$ (the gauge in which the monopole is constant) is a Gauduchon metric in the sense that $\omega$ is divergence-free with respect to $D^{g}=D^{|K|}$. It follows that $\omega$ is dual to a Killing field of $g$. Furthermore, the converse is also true: that is, if $D^{B}=D^{g}+\omega$ is Einstein-Weyl and $\omega$ is dual to a Killing field of $g$, then $\widetilde{D}^{B}=D^{g}-\omega$ is also Einstein-Weyl, and therefore the 4-manifold $M$ given by the monopole $\mu_{g}^{-1}$ is both selfdual and antiselfdual, hence conformally flat.

The condition that an Einstein-Weyl space admits a compatible metric $g$ such that $D=D^{g}+\omega$ with $\omega$ dual to a Killing field of $g$ is of particular importance because it always holds in the compact case: on any compact Weyl space there is a Gauduchon metric $g$ unique up to homothety [9], and $g$ has this additional property when the Weyl structure is Einstein-Weyl [28]. Consequently, the local quotients of conformally flat 4-manifolds exhaust the possible local geometries of compact Einstein-Weyl 3-manifolds. These geometries were obtained in [26] as local quotients of $S^{4}$. Now any conformal vector field $K$ on $S^{4}$ has a zero and is a homothetic vector field with respect to the flat metric on $\mathbb{R}^{4}$ given by stereographic projection away from any such zero. Hence we can view these Einstein-Weyl geometries as local quotients of the flat metric on $\mathbb{R}^{4}$ by a homothetic vector field and use the constructions of Section 4 to understand some of their properties.

Suppose first that $K$ vanishes on $\mathbb{R}^{4}$ and let the origin be such a zero. Then $K$ generates one parameter group of linear conformal transformations of the flat metric $g$. This is case 1 of [26] and we may choose coordinates such that
$$\begin{aligned}
g & =d r^{2}+\frac{1}{4} r^{2}\left(d \theta^{2}+\sin ^{2} \theta d \phi^{2}+(d \psi+\cos \theta d \phi)^{2}\right) \\
K & =a r \frac{\partial}{\partial r}-(b+c) \frac{\partial}{\partial \phi}-(b-c) \frac{\partial}{\partial \psi} .
\end{aligned}$$
Note that $K$ is also a homothety of the flat metric $\tilde{g}=r^{-4} g$ obtained from $g$ by the orientation reversing conformal transformation $r \mapsto \tilde{r}=1 / r$. With a fixed orientation,
$$\begin{aligned}
& D^{g} K=a \mathrm{id}+\frac{1}{2}(b+c) J^{+}+\frac{1}{2}(b-c) J^{-}, \\
& D^{\tilde{g}} K=-a \mathrm{id}+\frac{1}{2}(b-c) \widetilde{J}^{+}+\frac{1}{2}(b+c) \widetilde{J}^{-},
\end{aligned}$$
where $J^{ \pm}$are $D^{g}$-parallel complex structures on $\mathbb{R}^{4}$, one selfdual, the other antiselfdual, and, similarly, $\widetilde{J}^{ \pm}$are $D^{\tilde{g}}$-parallel. The Weyl structures
$D^{|K|} \pm \omega$ are Einstein-Weyl on the quotient $B$, where
$$\begin{aligned}
\omega & =\frac{(b+c) g\left(J^{+} K, .\right)-(b-c) g\left(J^{-} K, .\right)}{g(K, K)} \\
& =\frac{(b-c) \tilde{g}\left(\widetilde{J}^{+} K, .\right)-(b+c) \tilde{g}\left(\widetilde{J}^{-} K, .\right)}{\tilde{g}(K, K)} .
\end{aligned}$$
Without loss of generality, we consider only $D^{B}=D^{|K|}+\omega$. By Theorem 4.2, $J^{-} K$ and $\widetilde{J}^{-} K$ generate shear-free geodesic congruences with $\tau^{-}=(b+c)|K|^{-1}, \tilde{\tau}^{-}=(b-c)|K|^{-1}$ and $\kappa^{-}=a|K|^{-1}=-\tilde{\kappa}^{-}$.

If $b^{2}=c^{2}$, then $K$ is triholomorphic, and so the quotient geometry is hyperCR: it is the Berger sphere family. If we take $b=c$ then $J^{-}$is no longer unique, and the hyperCR structure is given by the congruences associated to $J K$, where $J$ ranges over the parallel antiselfdual complex structures of $g ; \widetilde{J}^{-} K$, by contrast, is the geodesic symmetry $\partial / \partial \phi$ of $B$. In addition, the antiselfdual rotations all commute with $K$, so $B$ has a four dimensional symmetry group, locally isomorphic to $S^{1} \times S^{3}$.

If $b c=0$, then although $K$ is not a Killing field on $\mathbb{R}^{4}$ unless $a=0$, it is Killing with respect to the product metric on $S^{2} \times \mathcal{H}^{2}$ which is scalar flat Kähler (where the hyperbolic metric on $\mathcal{H}^{2}$ has equal and opposite curvature to the round metric on $S^{2}$ ) and conformal to $\mathbb{R}^{4} \backslash \mathbb{R}$. Hence these quotients are Toda.

If $a=0$, then $K$ is a Killing field, and so the (local) quotient geometry is also Toda, simply because it is the quotient of a flat metric by a Killing field.

If $b^{2}=c^{2}$ and $b c=0$ then $b=c=0$ and the quotient is the round 3-sphere, while if $a=0$ and $b c=0$ it turns out to be the hyperbolic metric. If $a=0$ and $b^{2}=c^{2}$, the quotient geometry is the flat Weyl space: the hyperCR congruences become the translational symmetries, and (for $b=c$ ) $\widetilde{J}^{-} K$ is the radial symmetry.

We now briefly consider the case that $K$ does not vanish on $\mathbb{R}^{4}$ (and so is not linear with respect to any choice of origin). This is case 2 of [26], and we may choose a flat metric $g$ with respect to which $K$ is a transrotation. Since $K$ is a Killing field, the quotient Einstein-Weyl space is Toda. For $b=0$, it is flat, while for $c=0$ we obtain $\mathcal{H}^{3}$.

\section*{7. HyperKähler metrics with triholomorphic Killing fields.}

If $M$ is a hyperKähler 4-manifold and $K$ is a triholomorphic Killing field, then $\tau$ and $\kappa$ both vanish, so the corresponding Einstein-Weyl space is flat and the congruence consists of parallel straight lines. HyperKähler 4-manifolds with triholomorphic Killing fields therefore correspond to nonvanishing solutions of the Laplace equation on an open subset of $\mathbb{R}^{3}$, or some discrete quotient. This is the Gibbons-Hawking Ansatz for selfdual Euclidean vacua [13].

In [33], Ward used this Ansatz to generate new Toda Einstein-Weyl spaces from axially symmetric harmonic functions. The idea is beautifully simple: since the harmonic function is preserved by a Killing field on $\mathbb{R}^{3}$, the Gibbons-Hawking metric admits a two dimensional family of commuting Killing fields; one of these is triholomorphic, but the others need not be, and so they have other Toda Einstein-Weyl spaces with symmetry as quotients.

Let us carry out this procedure explicitly. In cylindrical polar coordinates $(\eta, \rho, \phi)$, the flat metric is $d \eta^{2}+d \rho^{2}+\rho^{2} d \phi^{2}$ and the generator of the axial symmetry is $\partial / \partial \phi$. An invariant monopole (in the gauge determined by the flat metric) is a function $W(\rho, \eta)$ satisfying $\rho^{-1}\left(\rho W_{\rho}\right)_{\rho}+W_{\eta \eta}=0$. Note that if $W$ is a solution of this equation, then so is $W_{\eta}$, and $W_{\eta}$ determines $W$ up to the addition of $C_{1} \log \left(C_{2} \rho\right)$ for some $C_{1}, C_{2} \in \mathbb{R}$. This provides a way of integrating the equation $d * d W=0$ to give $* d W=d A$ : if we write $W=V_{\eta}$, then we can take $A=\rho V_{\rho} d \phi$. This choice of integral determines the lift of $\partial / \partial \phi$ to the 4-manifold. The hyperKähler metric is
$$g=V_{\eta}\left(d \eta^{2}+d \rho^{2}+\rho^{2} d \phi^{2}\right)+V_{\eta}^{-1}\left(d \psi+\rho V_{\rho} d \phi\right)^{2} .$$
In order to take the quotient by $\partial / \partial \phi$, we rediagonalise:
$$\begin{aligned}
g=V_{\eta}\left(d \rho^{2}+d \eta^{2}+\frac{1}{V_{\eta}^{2}+V_{\rho}^{2}}\right. & \left.d \psi^{2}\right) \\
& \quad+\frac{\rho^{2}\left(V_{\eta}^{2}+V_{\rho}^{2}\right)}{V_{\eta}}\left(d \phi+\frac{V_{\rho}}{\rho\left(V_{\eta}^{2}+V_{\rho}^{2}\right)} d \psi\right)^{2} .
\end{aligned}$$
We now recall that the hyperKähler metric lies midway between the constant length gauge of $\partial / \partial \phi$ and the LeBrun-Ward gauge of the quotient.

Consequently we find that $D^{B}=D^{L W}+\omega$ where
$$\begin{aligned}
g_{L W} & =\rho^{2}\left(V_{\eta}^{2}+V_{\rho}^{2}\right)\left(d \rho^{2}+d \eta^{2}\right)+\rho^{2} d \psi^{2} \\
& =\rho^{2}\left(d V^{2}+d \psi^{2}\right)+\left(\rho V_{\rho} d \eta-\rho V_{\eta} d \rho\right)^{2} \\
\omega & =\frac{2 V_{\eta}}{\rho^{2}\left(V_{\eta}^{2}+V_{\rho}^{2}\right)}\left(\rho V_{\rho} d \eta-\rho V_{\eta} d \rho\right)
\end{aligned}$$
Note that $d\left(\rho V_{\rho} d \eta-\rho V_{\eta} d \rho\right)=0$. This can be integrated by writing $V=U_{\eta}$, with $U(\rho, \eta)$ harmonic. Then $z=\rho U_{\rho}$ parameterises the hypersurfaces orthogonal to the shear-free twist-free congruence, and isothermal coordinates on these hypersurfaces are given by $x=U_{\eta}$, $y=\psi$. Hence, although the Einstein-Weyl space is completely explicit, the solution $e^{u}=\rho^{2}$ of the $\operatorname{SU}(\infty)$ Toda field equation is only given implicitly. Nevertheless, we have found the congruence, the isothermal coordinates and the monopole $u_{z} \mu_{L W}^{-1}$.

The symmetry $\partial / \partial \psi$, like the axial symmetry $\partial / \partial \phi$ on $\mathbb{R}^{3}$, generates a congruence which is divergence-free and twist-free, although it is not geodesic. For this reason it is natural to say that Ward's spaces are Einstein-Weyl with an axial symmetry. They are studied in more detail in [4].

Ward's construction can be considerably generalised. First of all, one can obtain new Toda Einstein-Weyl spaces by considering harmonic functions invariant under other Killing fields. The general Killing field on $\mathbb{R}^{3}$ may be taken, in suitably chosen cylindrical coordinates, to be of the form $b \partial / \partial \phi+c \partial / \partial \eta$ for $b, c \in \mathbb{R}$. By introducing new coordinates $\zeta=(b \eta-c \phi) / \sqrt{b^{2}+c^{2}}$ and $\theta=(b \phi+c \eta) / \sqrt{b^{2}+c^{2}}$, so that the Killing field is a multiple of $\partial / \partial \theta$, one can carry out the same procedure as before to obtain the following Toda Einstein-Weyl spaces:
$$\begin{aligned}
g_{L W}= & G(\rho, \zeta)\left(d \rho^{2}+F(\rho) d \zeta^{2}\right)+\rho^{2} F(\rho)^{-1} \beta^{2} \\
= & \rho^{2}\left(d V^{2}+\frac{1}{b^{2}+c^{2}}\left(c\left[\rho V_{\rho} d \zeta-F(\rho)^{-1} \rho V_{\zeta} d \rho\right]+b d \psi\right)^{2}\right) \\
& \quad+\frac{1}{b^{2}+c^{2}}\left(b\left[\rho V_{\rho} d \zeta-F(\rho)^{-1} \rho V_{\zeta} d \rho\right]-c d \psi\right)^{2}, \\
\omega= & \frac{2 b V_{\zeta}}{\left(b^{2}+c^{2}\right) G(\rho, \zeta)}\left(b\left[\rho V_{\rho} d \zeta-F(\rho)^{-1} \rho V_{\zeta} d \rho\right]-c d \psi\right),
\end{aligned}$$
where
$$\begin{aligned}
F(\rho) & =\frac{\left(b^{2}+c^{2}\right) \rho^{2}}{b^{2} \rho^{2}+c^{2}}, \quad G(\rho, \zeta)=\frac{\left(b^{2} \rho^{2}+c^{2}\right) V_{\zeta}^{2}+\left(b^{2}+c^{2}\right) \rho^{2} V_{\rho}^{2}}{b^{2}+c^{2}} \\
\beta & =d \psi-\frac{b c\left(1-\rho^{2}\right)}{b^{2} \rho^{2}+c^{2}}\left[\rho V_{\rho} d \eta-F(\rho)^{-1} \rho V_{\eta} d \rho\right]
\end{aligned}$$
Note that the symmetry $\partial / \partial \psi$ is twist-free if and only if $b c=0$. When $b=0$, the Toda Einstein-Weyl space is just $\mathbb{R}^{3}$ (the only Einstein-Weyl space with a parallel symmetry), while $c=0$ is Ward's case.

A further generalisation of this procedure is obtained by observing that the flat Weyl structure on $\mathbb{R}^{3}$ is preserved not just by Killing fields, but by homothetic vector fields. Now, for a section $w$ of $L^{-1}$, invariance no longer means that the function $w \mu_{\mathbb{R}^{3}}$ is constant along the flow of the homothetic vector field, since the length scale $\mu_{\mathbb{R}^{3}}$ is not invariant. Hence it is better to work in a gauge in which the homothetic vector field is Killing. To do this we may choose spherical polar coordinates $(r, \theta, \phi)$ such that the flat Weyl structure on $\mathbb{R}^{3}$ is
$$g_{0}=r^{-2} d r^{2}+d \theta^{2}+\sin ^{2} \theta d \phi^{2}, \quad \omega_{0}=r^{-1} d r$$
and the homothetic vector field is a linear combination of $r \partial / \partial r$ and $\partial / \partial \phi$. For simplicity, we shall only consider here the case of a pure dilation $X=r \partial / \partial r$. If $w=W \mu_{0}^{-1}$ is an invariant monopole (where $\mu_{0}$ is the length scale of $g_{0}$ ) then $W_{r}=0$ and $W(\theta, \phi)$ is a harmonic function on $S^{2}$. We write $g_{S^{2}}=\sigma_{1}^{2}+\sigma_{2}^{2}$ and $W=\frac{1}{2}(h+\bar{h})$ with $h$ holomorphic on an open subset of $S^{2}$. Then the hyperKähler metric is
$$g=\frac{r(h+\bar{h})}{2|h|^{2}}\left(|h|^{2}\left(\sigma_{1}^{2}+\sigma_{2}^{2}\right)+\beta^{2}\right)+\frac{2|h|^{2}}{(h+\bar{h}) r}(d r+i(h+\bar{h}) r \beta)^{2},$$
where $\beta$ is a 1-form on $S^{2}$ with $d \beta=\frac{1}{2}(h+\bar{h}) \sigma_{1} \wedge \sigma_{2}$. One easily verifies that the quotient space is the Einstein-Weyl space with geodesic symmetry given by the holomorphic function $H=1 / h$.

The computation for the general homothetic vector field is more complicated, but one obtains Gibbons-Hawking metrics admitting holomorphic conformal vector fields which are neither triholomorphic or Killing, and therefore, as quotients, explicit examples of Einstein-Weyl spaces (with symmetry) which are neither hyperCR, nor Toda, yet they admit a shearfree geodesic congruence with linearly dependent divergence and twist.

\section*{8. Congruences and monopoles on $\mathcal{H}^{\mathbf{3}}, \mathbb{R}^{\mathbf{3}}$ and $\boldsymbol{S}^{\mathbf{3}}$.}

An important special case of the theory presented in this paper is the case of monopoles on spaces of constant curvature. Since each shear-free geodesic congruence on these spaces induces a complex structure on the selfdual space associated to any monopole, it is interesting to find such congruences.

The twist-free case has been considered by Tod [29]. In this case we have a LeBrun-Ward space of constant curvature, given by a solution $u$ of the Toda field equation with $u_{z} d z$ exact. This happens precisely when $u(x, y, z)=v(x, y)+w(z)$. The solutions, up to changes of isothermal coordinates, are given by
$$\mathrm{e}^{u}=\frac{4\left(a z^{2}+b z+c\right)}{\left(1+a\left(x^{2}+y^{2}\right)\right)^{2}}$$
where $a, b, c$ are constants constrained by positivity. As shown in [29], there are essentially six cases: three on hyperbolic space $\left(b^{2}-4 a c>0\right)$, two in flat space $\left(b^{2}-4 a c=0\right)$, and one on the sphere $\left(b^{2}-4 a c<0\right)$. One of the congruences in each case is a radial congruence, orthogonal to distance spheres. The other two types of congruences on hyperbolic space are orthogonal to horospheres and hyperbolic discs respectively, while the other type of congruence on flat space is translational. Only the radial congruences have singularities, and in the flat case, even the radial congruence is globally defined on $S^{1} \times S^{2}$. We illustrate the congruences in the diagrams of Figure 2.

The congruences on hyperbolic space $\mathcal{H}^{3}$ have been used by LeBrun (see [19], [20]) to construct selfdual conformal structures on complex surfaces. The first type of congruence gives scalar-flat Kähler metrics on blow ups of line bundles over $\mathbb{C} P^{1}$. The second type gives asymptotically Euclidean scalar-flat Kähler metrics on blow-ups of $\mathbb{C}^{2}$ and hence selfdual conformal structures on $k \mathbb{C} P^{2}$ and closed Kähler-Weyl structures on blowups of Hopf surfaces. The final type of congruence descends to quotients by discrete subgroups of $\mathrm{SL}(2, \mathbb{R})$ and leads to scalar-flat Kähler metrics on ruled surfaces of genus $\geq 2$.

If we look instead for hyperCR structures (i.e., divergence-free congruences), we have, in addition to the translational congruences on $\mathbb{R}^{3}$, two such structures on $S^{3}$ : the left and right invariant congruences, but this exhausts the examples on spaces of constant curvature. Of course

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/2f68b6dd-6e06-42d9-a8ed-04b5eeba303b-38.jpg?height=727&width=939&top_left_y=322&top_left_x=209}
\captionsetup{labelformat=empty}
\caption{Figure 2}
\end{figure}
there is still an abundance of congruences which are neither twist-free nor divergence-free. For instance, on $\mathbb{R}^{3}$, a piece of a minitwistor line and its conjugate define a congruence on some open subset: if the line is real then this is a radial congruence, but in general, we get a congruence of rulings of a family of hyperboloids (figure 3).

This congruence is globally defined on the nontrivial double cover of $\mathbb{R}^{3} \backslash S^{1}$. Its divergence and twist are closely related to the Eguchi-Hanson I metric as we shall see below.

In general, a holomorphic curve in the minitwistor space of $\mathbb{R}^{3}$ corresponds to a null curve in $\mathbb{C}^{3}$ and the associated congruence consists of the real points in the tangent lines to the null curve. Since null curves may be constructed from their real and imaginary parts, which are conjugate minimal surfaces in $\mathbb{R}^{3}$, this shows that more complicated congruences are associated with minimal surfaces.

Turning now to monopoles, we have two simple and explicit types of solutions of the monopole equation: the constant solutions and the fundamental solutions. Linear combinations of these give rise to an interesting family of selfdual conformal structures whose properties are

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/2f68b6dd-6e06-42d9-a8ed-04b5eeba303b-39.jpg?height=482&width=369&top_left_y=322&top_left_x=650}
\captionsetup{labelformat=empty}
\caption{Figure 3}
\end{figure}
given by the above congruences. Since such monopoles are spherically symmetric, these selfdual conformal structures will admit local $\mathrm{U}(2)$ or $S^{1} \times \operatorname{SO}(3)$ symmetry.

The 3 -metric with constant curvature $c$ is
$$g_{c}=\frac{4}{\left(1+c r^{2}\right)^{2}}\left(d r^{2}+r^{2} g_{S^{2}}\right)$$
and the monopoles of interest are $a+b z$, where $z=\left(1-c r^{2}\right) / 2 r$ is the fundamental solution centred at $r=0$. The fundamental solution is the divergence of the radial congruence, and if we use the coordinate $z$ in place of $r$, we obtain
$$g_{c}=\left(\frac{d z}{z^{2}+c}\right)^{2}+\frac{1}{z^{2}+c} g_{S^{2}} .$$
Rescaling by $\left(z^{2}+c\right)^{2}$ gives the Toda solution
$$g_{L W}=\left(z^{2}+c\right) g_{S^{2}}+d z^{2}, \quad \omega_{L W}=-\frac{2 z}{z^{2}+c} d z .$$
In the LeBrun-Ward gauge, the monopoles of interest are
$$w=(a+b z) /\left(z^{2}+c\right) .$$
If $c \neq 0$ then $w=a c^{-1}\left(1-\frac{1}{2} z u_{z}\right)+\frac{1}{2} b u_{z}$ and so we may apply Tod's prescription for the construction of Einstein metrics with symmetry. Rescaling by $\left(a^{2}+c^{2}\right) / c$ gives the Einstein metric
$$g=\frac{a^{2}+c^{2}}{(a z-b c)^{2}}\left(\frac{a+b z}{z^{2}+c}\left(d z^{2}+\left(z^{2}+c\right) g_{S^{2}}\right)+\frac{z^{2}+c}{a+b z}(d \psi+A)^{2}\right)$$
of scalar curvature $-12 a c /\left(a^{2}+c^{2}\right)$, where $d A=* D w=b \operatorname{vol}_{S^{2}}$. This is easily integrated by $A=-b \cos \theta d \phi$ where $g_{S^{2}}=d \theta^{2}+\sin ^{2} \theta d \phi^{2}$. These metrics are also well-defined when $c=0$ when they become Taub-NUT metrics with triholomorphic Killing field $\partial / \partial \psi$. They are also Gibbons-Hawking metrics for $a=0$, when we obtain the Eguchi-Hanson I and II metrics: this time $\partial / \partial \phi$ (and the other infinitesimal rotations of $S^{2}$ ) is a triholomorphic Killing field. To relate the metrics to those of [24], one can set $z=1 / \rho^{2}$ and rescale by a further factor $\frac{1}{4}$. Then
$$\begin{aligned}
g=\frac{a^{2}+c^{2}}{\left(a-b c \rho^{2}\right)^{2}}( & \frac{a \rho^{2}+b}{1+c \rho^{4}} d \rho^{2} \\
& \left.+\frac{1}{4} \rho^{2}\left[\left(a \rho^{2}+b\right) g_{S^{2}}+\frac{1+c \rho^{4}}{a \rho^{2}+b}(d \psi-b \cos \theta d \phi)^{2}\right]\right)
\end{aligned}$$
is Einstein with scalar curvature $-48 a c /\left(a^{2}+c^{2}\right)$. Up to homothety, this is really only a one parameter family of Einstein metrics, since the original constant curvature metric and the monopole $w$ can be rescaled. However, the use of three parameters enables all the limiting cases to be easily found.

These metrics are all conformally scalar-flat Kähler via the radial Toda congruences [18]. The metrics over $\mathcal{H}^{3}$ are also conformal to other scalar-flat Kähler metrics, via the horospherical and disc-orthogonal congruences. The translational congruences on $\mathbb{R}^{3}$ correspond to the hyperKähler structures associated with the Ricci-flat $c=0$ metrics. The metrics coming from $S^{3}$ admit two hypercomplex structures (coming from the hyperCR structures), which explains an observation of Madsen [22]. In particular when $a=0$, the Eguchi-Hanson I metric has two additional hypercomplex structures with respect to which $\partial / \partial \psi$ is triholomorphic. On the other hand, although $\partial / \partial \phi$ is triholomorphic with respect to the hyperKähler metric, it only preserves one complex structure from each of these additional families. The corresponding congruences on $\mathbb{R}^{3}$ are the two rulings of the families of hyperboloids, which have the same divergence but opposite twist. The monopole giving Eguchi-Hanson I must be the divergence of this congruence.

In [27], it is claimed that the above constructions give all the Einstein metrics over $\mathcal{H}^{3}$. This is not quite true, because we have not yet considered the Einstein metrics associated to the horospherical and disc-orthogonal congruences. These turn out to give Bianchi type $\mathrm{VII}_{0}$ and VIII analogues of the above Bianchi type IX metrics (by which we mean, the SU(2) symmetry group is replaced by $\operatorname{Isom}\left(\mathbb{R}^{2}\right)$ and $\operatorname{SL}(2, \mathbb{R})$ respectively-see [30]). This
omission from [27] was simply due to the nowhere vanishing conformal vector fields on hyperbolic space being overlooked.

\section*{9. Kähler-Weyl spaces with torus symmetry.}

On an Einstein-Weyl space with symmetry, an invariant shearfree geodesic congruence and an invariant monopole together give rise to a selfdual Kähler-Weyl structures, possessing, in general, only two continuous symmetries. Many explicit examples of such Einstein-Weyl spaces with symmetry were given in Section 7. Being quotients of Gibbons-Hawking metrics, these spaces already come with invariant congruences, and solutions of the monopole equation can be obtained by introducing an additional invariant harmonic function on $\mathbb{R}^{3}$, lifting it to the Gibbons-Hawking space, and pushing it down to the Einstein-Weyl space. Carrying out this procedure in full generality would take us too far afield, so we confine ourselves to the two simplest classes of examples: the Einstein-Weyl spaces with axial symmetry, and the Einstein-Weyl spaces with geodesic symmetry.

We first consider the case of axial symmetry, when the Kähler-Weyl structure is (locally) scalar flat Kähler. In [17], Joyce constructs such torus symmetric scalar-flat Kähler metrics from a linear equation on hyperbolic 2 -space. In this way he obtains selfdual conformal structures on $k \mathbb{C} P^{2}$, generalising (for $k \geq 4)$ those of LeBrun [19]. Joyce does not consider the intermediate Einstein-Weyl spaces in his construction, but one easily sees that his linear equation is equivalent to the equation for axially symmetric harmonic functions, and that the associated Einstein-Weyl spaces are precisely the ones with axial symmetry [4].

Let us turn now to the spaces with geodesic symmetry, where a monopole invariant under the symmetry is given by a nonvanishing holomorphic function on an open subset of $S^{2}$. Indeed, if we write (as before)
$$g=|H|^{-2}\left(\sigma_{1}^{2}+\sigma_{2}^{2}\right)+\beta^{2}, \quad \omega=\frac{i}{2}(H-\bar{H}) \beta$$
with $\beta$ dual to the symmetry, then an invariant monopole in this gauge is given by the pullback $V$ of a harmonic function on an open subset of $S^{2}$, as one readily verifies by direct computation. Hence $V=\frac{1}{2}(F+\bar{F})$ for some holomorphic function $F$. The selfdual space constructed from $V$ will admit a Kähler-Weyl structure (coming from the geodesic symmetry) and
also a hypercomplex structure (coming from the hyperCR structure). By Proposition 3.11, the geodesic symmetry preserves the hyperCR congruences, and so it lifts to a triholomorphic vector field of the hypercomplex structure. Since 3.11 is a characterisation, we immediately deduce the following result.
9.1. Theorem. - Let $M$ be a hypercomplex 4-manifold with a two dimensional family of commuting triholomorphic vector fields. Then the quotient of $M$ by any of these vector fields is Einstein-Weyl with a geodesic symmetry, and so the conformal structure on $M$ depends explicitly on two holomorphic functions of one variable.

There are two special choices of monopole on such an Einstein-Weyl space: the $\kappa$ and $\tau$ monopoles of the geodesic symmetry. The $\kappa$ monopole $(F=H)$ leads us back to the Gibbons-Hawking hyperKähler metric, but the $\tau$ monopole $(F=i H)$ is more interesting. In this case, the Kähler-Weyl structure given by the geodesic symmetry is hypercomplex and so these torus symmetric selfdual spaces are hypercomplex in two ways. The symmetries are both triholomorphic with respect to the first hypercomplex structure, but only one of them is triholomorphic with respect to the additional hypercomplex structure. If we take the quotient by the bitriholomorphic symmetry, we obtain an Einstein-Weyl space with two hyperCR structures, which must be $S^{3}$. Hence the spaces with geodesic symmetry, as well as coming from invariant monopoles on $\mathbb{R}^{3}$, also come from invariant monopoles on $S^{3}$.

We end by discussing a third situation in which the spaces with geodesic symmetry occur. This involves some explicit new solutions [6] of the $\mathrm{SU}(\infty)$ Toda field equation generalising the solutions on $S^{3}$ described earlier. The corresponding LeBrun-Ward geometries are:
$$g=(z+h)(z+\bar{h})\left(\sigma_{1}^{2}+\sigma_{2}^{2}\right)+d z^{2}, \quad \omega=-\frac{2 z+h+\bar{h}}{(z+h)(z+\bar{h})} d z$$
where $h$ is an arbitrary nonvanishing holomorphic function on an open subset of $S^{2}$. These spaces have no symmetries and so one obtains from them Einstein metrics with a one dimensional isometry group. However, $\partial / \partial z$ does lift to a shear-free congruence on the Einstein space, and a generalised Jones and Tod construction may be used to show that the quotient by this conformal submersion is the Einstein-Weyl space with geodesic symmetry given by $H=1 / h$ (see [6]). In fact this was how these interesting Einstein-Weyl spaces were found.

\section*{BIBLIOGRAPHY}
\begin{itemize}
\item[] [1] V. Apostolov, P. Gauduchon, The Riemannian Goldberg-Sachs theorem, Int. J. Math., 8 (1997), 421-439.
\item[] [2] A.L. Besse, Einstein Manifolds, Ergeb. Math. Grenzgeb., vol. 10, Springer, Berlin, 1987.
\item[] [3] C.P. Boyer, J.D. Finley, Killing vectors in self-dual Euclidean Einstein spaces, J. Math. Phys., 23 (1982), 1126-1130.
\item[] [4] D.M.J. Calderbank, The geometry of the Toda equation, Edinburgh Preprint MS-99-003, 1999, to appear in J. Geom. Phys.
\item[] [5] D.M.J. Calderbank, H. Pedersen, Einstein-Weyl geometry, in Essays on Einstein Manifolds (eds. C.R. LeBrun and M. Wang), Surveys in Differential Geometry, vol. V, International Press.
\item[] [6] D.M.J. Calderbank, K.P. Tod, Einstein metrics, hypercomplex structures and the Toda field equation, Edinburgh Preprint MS-98-011, 1998, to appear in Diff. Geom. Appl.
\item[] [7] T. Chave, K.P. tod, G. Valent, $(4,0)$ and $(4,4)$ sigma models with a triholo-morphic Killing vector, Phys. Lett., B 383 (1996), 262-270.
\item[] [8] M. Dunajski, K.P. Tod, Einstein-Weyl structures from hyper-Kähler metrics with conformal Killing vectors, Preprint ESI 739, Vienna, 1999.
\item[] [9] P. Gauduchon, La 1-forme de torsion d'une variété hermitienne compacte, Math. Ann., 267 (1984), 495-518.
\item[] [10] P. Gauduchon, Structures de Weyl et théorèmes d'annulation sur une variété conforme autoduale, Ann. Sci. Norm. Sup. Pisa, 18 (1991), 563-629.
\item[] [11] P. Gauduchon, Structures de Weyl-Einstein, espaces de twisteurs et variétés de type $S^{1} \times S^{3}$, J. reine angew. Math., 469 (1995), 1-50.
\item[] [12] P. Gauduchon, K.P. Tod, Hyperhermitian metrics with symmetry, J. Geom. Phys., 25 (1998), 291-304.
\item[] [13] G.W. Gibbons, S.W. Hawking, Gravitational multi-instantons, Phys. Lett., 78 B (1978), 430-432.
\item[] [14] N.J. Hitchin, Complex manifolds and Einstein equations, in Twistor Geometry and Non-linear Systems (eds H.D. Doebner and T.D. Palev), Primorsko 1980, Lecture Notes in Math., vol. 970, Springer, Berlin, 1982, 79-99.
\item[] [15] S.A. Huggett, K.P. Tod, An Introduction to Twistor Theory, Cambridge University Press, Cambridge, 1985.
\item[] [16] P.E. Jones, K.P. Tod, Minitwistor spaces and Einstein-Weyl spaces, Class. Quantum Grav., 2 (1985), 565-577.
\item[] [17] D.D. Joyce, Explicit construction of self-dual 4-manifolds, Duke Math. J., 77 (1995), 519-552.
\item[] [18] C.R. LeBrun, Counterexamples to the generalized positive action conjecture, Comm. Math. Phys., 118 (1988), 591-596.
\item[] [19] C.R. LEBRUN, Explicit self-dual metrics on $\mathbb{C} P^{2} \# \cdots \# \mathbb{C} P^{2}$, J. Diff. Geom., 34 (1991), 223-253.
\item[] [20] C.R. LEBRUN, Self-dual manifolds and hyperbolic geometry, in Einstein Metrics and Yang-Mills Connections (eds. T. MAbuchi and S. Mukai), Sanda 1990, Lecture Notes in Pure and Appl. Math., vol. 145, Marcel Dekker, New York, 1993, 99-131.
\end{itemize}
\begin{itemize}
\item[] [21] H.-C. LEE, A kind of even-dimensional differential geometry and its application to exterior calculus, Amer. J. Math., 65 (1943), 433-438.
\item[] [22] A.B. Madsen, Einstein-Weyl structures in the conformal classes of LeBrun metrics, Class. Quantum Grav., 14 (1997), 2635-2645.
\item[] [23] L.J. Mason, N.M.J. Woodhouse, Integrability, Self-duality and Twistor Theory, Clarendon Press, Oxford, 1996.
\item[] [24] H. Pedersen, Einstein metrics, spinning top motions and monopoles, Math. Ann., 274 (1986), 35-39.
\item[] [25] H. Pedersen, A. Swann, Riemannian submersions, four-manifolds and Einstein-Weyl geometry, Proc. London Math. Soc., 66 (1993), 381-399.
\item[] [26] H. Pedersen, K.P. Tod, Three-dimensional Einstein-Weyl geometry, Adv. Math., 97 (1993), 74-109.
\item[] [27] H. Pedersen, K.P. Tod, Einstein metrics and hyperbolic monopoles, Class. Quantum Grav., 8 (1991), 751-760.
\item[] [28] K.P. TOD, Compact 3-dimensional Einstein-Weyl structures, J. London Math. Soc., 45 (1992), 341-351.
\item[] [29] K.P. TOD, Scalar-flat Kähler and hyper-Kähler metrics from Painlevé-III, Class. Quantum Grav., 12 (1995), 1535-1547.
\item[] [30] K.P. Tod, Cohomogeneity-one metrics with self-dual Weyl tensor, in Twistor Theory (ed. S. Huggett), Lecture Notes in Pure and Appl. Math., vol. 169, Marcel Dekker, Plymouth, 1995, 171-184.
\item[] [31] K.P. Tod, The $\mathrm{SU}(\infty)$-Toda field equation and special four-dimensional metrics, in Geometry and Physics (eds. J.E. Andersen, J. Dupont, H. Pedersen and A. Swann), Lecture Notes in Pure and Appl. Math., vol. 184, Marcel Dekker, Aarhus, 1995, 307-312.
\item[] [32] I. Vaisman, On locally conformal almost Kähler manifolds, Israel J. Math., 24 (1976), 338-351.
\item[] [33] R.S. WARD, Einstein-Weyl spaces and $\mathrm{SU}(\infty)$ Toda fields, Class. Quantum Grav., 7 (1990), L95-L98.
Manuscrit reçu le 30 août 1999,
accepté le 2 novembre 1999.
D.M.J. CALDERBANK,
University of Edinburgh
Department of Mathematics and Statistics
King's Buildings, Mayfield Road
Edinburgh EH9 3JZ (Scotland).
davidmjc@maths.ed.ac.uk
\&
H. PEDERSEN,
SDU Odense University
Department of Mathematics and Computer Science
Campusvej 55
DK-5230 Odense M (Denmark).
henrik@imada.sdu.dk
\end{itemize}