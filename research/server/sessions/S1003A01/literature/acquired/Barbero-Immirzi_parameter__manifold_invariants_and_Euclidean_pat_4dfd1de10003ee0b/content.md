---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 1111_6702.pdf
converter: mathpix
format: mmd
---

\title{
Barbero-Immirzi parameter, manifold invariants and Euclidean path integrals
}

\author{
Tomáš Liko* \\ Department of Mathematical and Statistical Sciences \\ University of Alberta \\ Edmonton, AB T6G 2G1, Canada
}

March 24, 2022

\begin{abstract}
The Barbero-Immirzi parameter $\gamma$ appears in the real connection formulation of gravity in terms of the Ashtekar variables, and gives rise to a oneparameter quantization ambiguity in Loop Quantum Gravity. In this paper we investigate the conditions under which $\gamma$ will have physical effects in Euclidean Quantum Gravity. This is done by constructing a well-defined Euclidean path integral for the Holst action with non-zero cosmological constant on a manifold with boundary. We find that two general conditions must be satisfied by the spacetime manifold in order for the Holst action and its surface integral to be non-zero: (i) the metric has to be non-diagonalizable; (ii) the Pontryagin number of the manifold has to be non-zero. The latter is a strong topological condition, and rules out many of the known solutions to the Einstein field equations. This result leads us to evaluate the on-shell first-order Holst action and corresponding Euclidean partition function on the Taub-NUT-ADS solution. We find that $\gamma$ shows up as a finite rotation of the on-shell partition function which corresponds to shifts in the energy and entropy of the NUT charge. In an appendix we also evaluate the Holst action on the Taub-NUT and Taub-bolt solutions in flat spacetime and find that in that case as well $\gamma$ shows up in the energy and entropy of the NUT and bolt charges. We also present an example whereby the Euler characteristic of the manifold has a non-trivial effect on black-hole mergers.
\end{abstract}

PACS: 04.20.Cv;04.20.Fy;04.70.Dy

\section*{1 Introduction}

Since its discovery within the context of canonical gravity [1], the Barbero-Immirzi parameter, denoted $\gamma$, has remained an elusive one-parameter quantization ambi-

\footnotetext{
*Electronic mail: tliko@math.ualberta.ca
}
guity in loop quantum gravity [2, 3]. For details, see [4-6]. This parameter can be fixed by comparing the quantum theory to the semi-classical theory. This procedure for fixing $\gamma$ has been done by matching the Bekenstein-Hawking entropy of black holes with spacetime topology $\mathbb{R}^{2} \times \mathbb{C}^{2}$, with $\mathbb{C}^{2}$ a compact two-manifold, to the corresponding isolated horizon quantum geometry [7-10]. It turns out that $\gamma$ has the same value regardless of the topology of the black hole.

The Einstein field equations admit more solutions in four dimensions than just the black holes whose event horizons have topology $\mathbb{R} \times \mathbb{C}^{2}$; in particular, the NUT-charged spacetimes [11, 12] have topologies that cannot be foliated by a time function and contain Misner strings with a non-zero entropy [13]. A comparison of the semi-classical and quantum geometry descriptions of NUT-charged spacetimes would be of interest in order to provide an independent determination of $\gamma$ that can be compared to the previous results for black holes [7-10].

Motivated by this interest, we want to know what effects, if any, $\gamma$ may have on the Euclidean path integral. In this paper we study the Euclidean Holst action [14] with non-zero cosmological constant, and derive the semi-classical energy and entropy of Taub-NUT-ADS spacetime in the presence of $\gamma$. This can only be done in first-order formalism. That said, we need to make sure that the first-order Holst-ADS action satisfies two important conditions in order that we may be able to evaluate the on-shell Euclidean Holst-ADS action: (I) The action has to have a well-posed action principle on a manifold with boundary; and (II) the action has to be finite.

Condition I leads us to consider the Dirichlet boundary value problem for a generic first-order action that includes curvature and torsion as functionals of the connection and coframe, and we present a general prescription for determining the corresponding surface terms for which the first variation of the action vanishes identically. We then present, in an example, a derivation of the surface terms that are necessary for a generalized Hilbert-Palatini action in four dimensions to be functionally differentiable; the form of this functional is motivated by requiring consistency with the Hamiltonian theory coupled to fermions when $\gamma=i$. A special case of this action is the Holst action with non-zero cosmological constant - the main focus of study in this paper. Some general properties of the Holst surface term are discussed in Section 3. Condition II is also addressed in Section 3. The ADS and Holst-ADS actions are finite without the need of adding infinite counter-terms to the boundary integral, as is normally done in the infinite subtraction method [15-17, 19-21].

Once the two conditions are shown to be satisfied by the Holst-ADS action, we are able to evaluate the Euclidean Holst action on solutions to the field equations, and obtain the corresponding on-shell partition functions. We find that generically $\gamma$ shows up in the Euclidean path integral as a finite rotation of the on-shell partition function, and this rotation corresponds to shifts in the energy and entropy of the
spacetime. This property of the Holst-ADS action is a result of a strong topological condition that we find: the Holst term and its surface term are non-zero if the Pontryagin number of the corresonding spacetime manifold is non-zero. We confirm these results by explicitly evaluating the Holst-ADS action and partition function on the Taub-NUT-ADS solution; $\gamma$ shows up as a finite shift in the energy and entropy of the NUT charge.

We also include two appendices. In Appendix 1 we evaluate the Euclidean Holst action on Taub-NUT spacetimes with zero cosmological constant. We show that $\gamma$ shows up as a shift in the energy and entropy of the NUT and bolt charges, just as for the Taub-NUT-ADS solution. In Appendix 2 we present an example which shows how a topological invariant of the manifold can have non-trivial physical effects in gravity. In particular, it is shown that the presence of the Euler characteristic of the manifold can lead to violations of the second law during a black-hole merging process.

\section*{2 First-order action principle: generalities}

In the first-order formulation of general relativity (see e.g. [4]), the configuration space $\mathscr{C}$ is the pair $\{e, A\}$, consisting of the coframe $e$ and a connection $A$ valued in $S O(D)$ or $S O(D-1,1)$ depending on the signature of spacetime. The coframe determines the spacetime metric $g_{a b}=\eta_{I J} e_{a}{ }^{I} \otimes e_{b}{ }^{J}$ and spacetime volume form $\boldsymbol{\epsilon}=e^{0} \wedge \cdots e^{D-1}$, where $\epsilon_{I_{1} \cdots I_{D}}$ is the totally antisymmetric Levi-Civita tensor. In this paper, spacetime indices $a, b, \ldots \in\{0, \ldots, D-1\}$ are raised and lowered using the metric $g_{a b}$ and internal indices $I, J, \ldots \in\{0, \ldots, D-1\}$ are raised and lowered using the flat metric $\eta_{I J}$. The connection determines the curvature twoform $\Omega^{I}{ }_{J}=d A^{I}{ }_{J}+A^{I}{ }_{K} \wedge A^{K}{ }_{J}=\frac{1}{2} R^{I}{ }_{J K L} e^{K} \wedge e^{L}$, with $R^{I}{ }_{J K L}$ the Riemann tensor. The Lagrangian density is denoted $\mathcal{L}$; this is a functional, by which we mean a map from the space of functions $(e, A)$ to $\mathbb{R}$. The functional derivative of $\mathcal{L}$ with respect to a function $\varphi=\varphi\left(x^{a}\right)$ is denoted $\boldsymbol{\Upsilon}_{\varphi} \equiv \delta \mathcal{L} / \delta \varphi$. The internal Hodge dual is denoted by ★. In this paper, we write differential forms without indices.

\subsection*{2.1 Functional differentiability of the generic first-order action}

Let us begin with the following.
Proposition 1. Let $\Omega=d A+A \wedge A$ and $T=d e+A \wedge e$ be (resp.) the curvature and torsion of a $D$-dimensional manifold $\mathcal{M}$ with boundary $\partial \mathcal{M}$, with $A$ the connection and e the coframe. Let $\mathcal{L}[e, A, \Omega, T]$ be the Lagrangian density, a $D$-form in spacetime. The first-order action for an arbitrary diffeomorphism invariant theory of pure gravity on the configuration space $\mathscr{C}=\{e, A\}$,
$$I=\frac{1}{16 \pi} \int_{\mathcal{M}} \mathcal{L}[e, A, \Omega, T]-\frac{(-1)^{D}}{16 \pi} \oint_{\partial \mathcal{M}} \boldsymbol{\Upsilon}_{\Omega} \wedge A+\boldsymbol{\Upsilon}_{T} \wedge e,$$
is functionally differentiable.
Proof. Take the variation of $\mathcal{L}$ :
$$\begin{aligned}
\delta \mathcal{L}= & \mathbf{\Upsilon}_{e} \wedge \delta e+\mathbf{\Upsilon}_{A} \wedge \delta A+\mathbf{\Upsilon}_{\Omega} \wedge \delta \Omega+\mathbf{\Upsilon}_{T} \wedge \delta T \\
= & \mathbf{\Upsilon}_{e} \wedge \delta e+\mathbf{\Upsilon}_{A} \wedge \delta A+\mathbf{\Upsilon}_{\Omega} \wedge(d \delta A+2 A \wedge \delta A)+\mathbf{\Upsilon}_{T} \wedge(d \delta e-e \wedge \delta A+A \wedge \delta e) \\
= & (-1)^{D} d\left(\mathbf{\Upsilon}_{\Omega} \wedge \delta A\right)+(-1)^{D} d\left(\mathbf{\Upsilon}_{T} \wedge \delta e\right)+\left[\mathbf{\Upsilon}_{e}+\mathbf{\Upsilon}_{T} \wedge A-(-1)^{D} d \mathbf{\Upsilon}_{T}\right] \wedge \delta e \\
& +\left[\mathbf{\Upsilon}_{A}+2 \mathbf{\Upsilon}_{\Omega} \wedge A-(-1)^{D} d \mathbf{\Upsilon}_{\Omega}-\mathbf{\Upsilon}_{T} \wedge e\right] \wedge \delta A .
\end{aligned}$$
The action will be functionally differentiable if the total derivative is cancelled, and the equations of motion
$$\begin{array}{r}
\boldsymbol{\Upsilon}_{e}+\boldsymbol{\Upsilon}_{T} \wedge A-(-1)^{D} d \boldsymbol{\Upsilon}_{T}=0 \\
\boldsymbol{\Upsilon}_{T} \wedge e+(-1)^{D} d \boldsymbol{\Upsilon}_{\Omega}-2 \boldsymbol{\Upsilon}_{\Omega} \wedge A-\boldsymbol{\Upsilon}_{A}=0
\end{array}$$
are satisfied. From the Fundamental Theorem of Exterior Calculus, the boundary term
$$I_{\partial \mathcal{M}}=\frac{(-1)^{D}}{16 \pi} \oint_{\partial \mathcal{M}} \boldsymbol{\Upsilon}_{\Omega} \wedge A+\boldsymbol{\Upsilon}_{T} \wedge e$$
follows. This completes the proof. \(\square\)

From the identity $d^{2}=0$, terms involving higher derivatives in the configuration variables $e$ and $A$ do not show up in the action (1). The action (1) is therefore generically first-order in derivatives of $e$ and $A$.

\subsection*{2.2 Example: Generalized Hilbert-Palatini action in four dimensions}

If we take the Wilsonian point of view on effective field theories, then we need to add all possible $D$-forms to the action for gravity that are diffeomorphism invariant. In four dimensions, this implies that in addition to the Hilbert-Palatini and cosmological terms, we should include in the action the Holst term $\theta_{1} \int e \wedge e \wedge \Omega$, as well as the characteristic classes: the Euler class $\theta_{2} \int \star \Omega \wedge \Omega$, the Pontryagin class $\theta_{3} \int \Omega \wedge \Omega$, and the Nieh-Yan class $\theta_{4} \int T \wedge T-e \wedge e \wedge \Omega$. See e.g. [22,23]. Here, $\theta_{1}=1 / \gamma$ with $\gamma$ a non-zero real constant - the so-called Barbero-Immirzi parameter [1].

It was pointed out in [24, 25], however, that in the case when fermions are coupled to gravity, the Holst term needs to be replaced with the Nieh-Yan term. This extension of the Holst term is necessary in the presence of non-zero torsion so that the corresponding Hamiltonian with arbitrary $\gamma$ reduces to the Ashtekar-Romano-Tate Hamiltonian [26] when $\gamma$ is set equal to the imaginary unit. Therefore we consider here the Nieh-Yan term in place of the Holst term in our action principle (with $\theta_{4}=1 / \gamma$ ). When torsion is zero the Nieh-Yan term reduces to the Holst term. This makes the topological origin of the Holst term in the first-order action manifest!

From Proposition 1, then, we have the following:
Corollary 2. The generalized Hilbert-Palatini action for general relativity with cosmological constant $\Lambda=3 \varepsilon / \ell^{2} \in \mathbb{R}(\varepsilon \in\{-1,1\})$, Barbero-Immirzi parameter $\gamma \in \mathbb{R} \backslash 0$ and $\theta_{2}, \theta_{3} \in \mathbb{R}$ on a four-dimensional manifold ( $\mathcal{M}, e, A$ ) with boundary $\partial \mathcal{M}$,
$$\begin{aligned}
I= & \frac{1}{16 \pi} \int_{\mathcal{M}} \star(e \wedge e) \wedge \Omega-2 \Lambda \boldsymbol{\epsilon}+\frac{1}{\gamma}(T \wedge T-e \wedge e \wedge \Omega)+\theta_{2} \star \Omega \wedge \Omega+\theta_{3} \Omega \wedge \Omega \\
& -\frac{1}{16 \pi} \oint_{\partial \mathcal{M}} \star(e \wedge e) \wedge A-\frac{1}{\gamma} e \wedge d e+2 \theta_{2} \star \Omega \wedge A+\theta_{3} \Omega \wedge A,
\end{aligned}$$
is functionally differentiable.
Proof. For the Nieh-Yan-Holst term, we find that $\boldsymbol{\Upsilon}_{T}=T$ and $\boldsymbol{\Upsilon}_{\Omega}=-e \wedge e$ so that the surface term has density $T \wedge e-e \wedge e \wedge A=d e \wedge e+A \wedge e \wedge e-A \wedge e \wedge e=d e \wedge e$. For the Euler term we find that $\boldsymbol{\Upsilon}_{\Omega}=2 \star \Omega$ so that the surface term has density $2 \star \Omega \wedge A$. For the Pontryagin term we find that $\mathbf{\Upsilon}_{\Omega}=\Omega$ so that the surface term has density $\Omega \wedge A$. The surface term in the action (5) follows. \(\square\)

The action (6), with $\theta_{1}=\theta_{2}=\theta_{3}=\theta_{4}=0$, was previously studied within the context of black-hole mechanics. In these works, the spacetimes under consideration include four-dimensional Einstein-Maxwell theory with zero cosmological constant [27, 28], non-trivial matter couplings [29-31], higher-dimensional flat and ADS spacetimes [32, 33], Gauss-Bonnet gravity [34] and supergravity with $p$ form matter couplings [35-37].

In this formalism, the topology of the boundary in the action principle is taken to be $\partial \mathcal{M} \cong M_{1} \cup M_{2} \cup \Delta \cup \mathcal{I}$, with $\Delta$ a $(D-1)$-dimensional null hypersurface equipped with a null normal and a degenerate metric with signature $(0+\ldots+)$. $M_{1}$ and $M_{2}$ are partial Cauchy surfaces that extend from $\Delta$ to the boundary $\mathcal{I}$ at infinity; $M_{1}$ and $M_{2}$ intersect $\Delta$ and $\mathcal{I}$ in $(D-2)$-surfaces $\mathbb{C}^{D-2}$. Adding the surface term $\oint_{\mathcal{I}} \star(e \wedge e) \wedge A$ to the action at $\mathcal{I}$ and fixing the geometry of $\Delta$ are sufficient conditions for the action to be functionally differentiable and for the zeroth and first laws of black-hole mechanics to be satisfied. In particular, all the conserved charges are defined locally at the horizon $\Delta$; these include the non-monopolar (dipole) charge of the five-dimensional black ring solution [37, 38].

Subsequently it was shown that the action is finite on asymptotically flat spacetimes [39, 40], and that a partition function can be given for Euclidean metrics [41] without having to add infinite counter-terms to the boundary [41]. It was then shown that the the Holst term and its surface term together are finite [42]. In this paper we further explore properties of the Holst action and corresponding Euclidean path integral on a manifold with boundary, in the presence of a non-zero cosmological constant.

\section*{3 Holst action with cosmological constant}

In this paper we will focus particular attention to ADS spacetimes with $\Lambda<0$, but the mathematical results obtained also apply to de Sitter spacetimes with $\Lambda>0$. Therefore we consider the Holst action in the presence of a non-zero cosmological constant $\Lambda=3 \varepsilon \ell^{-2} \in \mathbb{R} \backslash 0$, with $\varepsilon \in\{-1,1\}$ and $\ell$ is the de Sitter radius. Specifically, we consider the action (5) with $T=0$ and with $\theta_{2}=\theta_{3}=0$.

The first-order Holst action with cosmological constant $\Lambda=3 \varepsilon \ell^{-2} \in \mathbb{R} \backslash 0$ $(\varepsilon \in\{-1,1\})$ and Barbero-Immirzi parameter $\gamma \in \mathbb{R} \backslash 0$ on a four-dimensional manifold $(\mathcal{M}, e, A)$ with boundary $\partial \mathcal{M}$ is:
$$I=\frac{1}{16 \pi} \int_{\mathcal{M}}\left[\left(\star-\frac{1}{\gamma}\right)(e \wedge e)\right] \wedge \Omega+\frac{6 \varepsilon}{\ell^{2}} \epsilon-\frac{1}{16 \pi} \oint_{\partial \mathcal{M}} \star(e \wedge e) \wedge A-\frac{1}{\gamma} e \wedge d e .$$
From Corollary 2, this action is functionally differentiable. The surface term here is the same as the one that was previously found for the Holst action in flat spacetime [42]. This is because when $T=d e+A \wedge e=0$ we have $e \wedge d e=e \wedge e \wedge A$.

An important property of the Holst surface term $e \wedge d e$ is that it is identically zero for spacetimes with metrics that can be put into diagonal form. To see this, consider the tetrad in components: $e^{I}=e_{a}{ }^{I} d x^{a}$. Differentiating the tetrad gives $d e^{I}=\left(\partial e_{a}^{I} / \partial x^{b}\right) d x^{b} \wedge d x^{a}$. By direct substitution we get
$$e \wedge d e=\left[e_{0}\left(\frac{\partial e_{a}^{0}}{\partial x^{b}}\right)+e_{1}\left(\frac{\partial e_{a}^{1}}{\partial x^{b}}\right)+e_{2}\left(\frac{\partial e_{a}^{2}}{\partial x^{b}}\right)+e_{3}\left(\frac{\partial e_{a}^{3}}{\partial x^{b}}\right)\right] \wedge d x^{b} \wedge d x^{a}$$
If the metric is diagonal, then
$$\begin{aligned}
e \wedge d e= & e_{0}\left(\frac{\partial e_{0}^{0}}{\partial x^{b}}\right) \wedge d x^{b} \wedge d x^{0}+e_{1}\left(\frac{\partial e_{1}^{1}}{\partial x^{b}}\right) \wedge d x^{b} \wedge d x^{1} \\
& +e_{2}\left(\frac{\partial e_{2}^{2}}{\partial x^{b}}\right) \wedge d x^{b} \wedge d x^{2}+e_{3}\left(\frac{\partial e_{3}^{3}}{\partial x^{b}}\right) \wedge d x^{b} \wedge d x^{3}=0 .
\end{aligned}$$
Of particular interest in general relativity are spacetimes with a ' $t-\phi$ ' component in their corresponding metrics. For a general metric with $x^{0}-x^{3}$ cross term, $e \wedge d e$ can be written in component form such that
$$e \wedge d e=\left\{e_{00}\left(\frac{\partial e_{3}^{0}}{\partial x^{b}}\right)-e_{03}\left(\frac{\partial e_{0}^{0}}{\partial x^{b}}\right)\right\} d x^{0} \wedge d x^{b} \wedge d x^{3} .$$
In spherical coordinates $x^{a} \in\{\tau, r, \theta, \phi\}$, on a constant- $r$ hypersurface, the boundary term is:
$$e \wedge d e=\left\{e_{00}\left(\frac{\partial e_{3}^{0}}{\partial \theta}\right)-e_{03}\left(\frac{\partial e_{0}^{0}}{\partial \theta}\right)\right\} d \tau \wedge d \theta \wedge d \phi .$$
This expression can be used to evaluate the Holst surface term on solutions with a $t-\phi$ component in the metric.

For spacetimes with non-zero cosmological constant, another condition can be found on the Holst surface term. Let us first substitute the equation of motion
$d e+A \wedge e=0$ into the action (6) to eliminate the tetrad derivative in the surface term:
$$I=\frac{1}{16 \pi} \int_{\mathcal{M}}\left[\left(\star-\frac{1}{\gamma}\right)(e \wedge e)\right] \wedge \Omega+\frac{6 \varepsilon}{\ell^{2}} \epsilon-\frac{1}{16 \pi} \oint_{\partial \mathcal{M}} \star(e \wedge e) \wedge A-\frac{1}{\gamma} e \wedge e \wedge A .$$
Then with the equation of motion $e \wedge e=\left(\varepsilon \ell^{2} / 6\right) \Omega$ the boundary term becomes (with $\stackrel{!}{=}$ denoting equality on-shell)
$$-\frac{1}{16 \pi} \oint_{\partial \mathcal{M}} \star(e \wedge e) \wedge A-\frac{1}{\gamma} e \wedge e \wedge A \stackrel{!}{=}-\frac{\varepsilon \ell^{2}}{6 \cdot 16 \pi} \oint_{\partial \mathcal{M}} \star \Omega \wedge A-\frac{1}{\gamma} \Omega \wedge A .$$
From the Fundamental Theorem of Exterior Calculus, this boundary integral can be written as a bulk integral:
$$-\frac{\varepsilon \ell^{2}}{6 \cdot 16 \pi} \oint_{\partial \mathcal{M}} \star \Omega \wedge A-\frac{1}{\gamma} \Omega \wedge A \stackrel{!}{=}-\frac{\varepsilon \ell^{2}}{6 \cdot 16 \pi} \int_{\mathcal{M}} \star \Omega \wedge \Omega-\frac{1}{\gamma} \Omega \wedge \Omega .$$
Putting this in (11), we see that the Holst action can be written as a bulk integral:
$$I=\frac{1}{16 \pi} \int_{\mathcal{M}}\left[\left(\star-\frac{1}{\gamma}\right)(e \wedge e)\right] \wedge \Omega+\frac{6 \varepsilon}{\ell^{2}} \epsilon-\frac{\varepsilon \ell^{2}}{6} \star \Omega \wedge \Omega+\frac{\varepsilon \ell^{2}}{6 \gamma} \Omega \wedge \Omega .$$
Written this way, the surface terms appearing in the action (6) are invariants of the manifold $\mathcal{M}$. It follows from this form of the action that the Holst surface term is identically zero for manifolds that have zero Pontryagin number. In addition, the Holst term itself can be written purely in terms of the connection by using the equation of motion $e \wedge e=\left(\varepsilon \ell^{2} / 6\right) \Omega$ to eliminate the tetrad. We find that:
$$\frac{1}{\gamma} \int_{\mathcal{M}} e \wedge e \wedge \Omega \stackrel{!}{=} \frac{\varepsilon \ell^{2}}{6 \gamma} \int_{\mathcal{M}} \Omega \wedge \Omega$$
Therefore we see that on-shell the Holst term will be identically zero if the Pontryagin number of the manifold is zero.

The first-order Holst action with negative cosmological constant is finite. To see this, consider first the Einstein-Hilbert and cosmological terms only. Then, action (14) with $\varepsilon=-1$ is precisely the action that was shown to be finite for ADS spacetimes [43]. It was also shown in [42] that the Holst term and its surface term together are finite. Therefore, the action (14) is finite.

Let us briefly summarize this section. The Holst-ADS action is functionally differentiable and finite. In order for the Holst term and its surface term, and therefore $\gamma$ to be present in the on-shell action, the corresponding solution has to have a non-diagonalizable metric and a non-zero Pontryagin number. These are very restrictive conditions and rule out many of the known spacetimes that are critical points of the action. The Taub-NUT spacetime is known to have Pontryagin number 2 [44]. Therefore, in Section 4 and in Appendix 1, we evaluate the Euclidean on-shell Holst-ADS and Holst actions and partition functions (resp.) on the Taub-NUT-ADS spacetime with $\Lambda<0$ and the Taub-NUT and Taub-bolt spacetimes with $\Lambda=0$.

\section*{4 Euclidean path integrals and Taub-NUT-ADS spacetime}
4.1 Partition functions and thermodynamics

Let us consider the formal path integral
$$\mathcal{Z}=\int \mathcal{D}[\Psi] \exp \{-I[\Psi]\},$$
with $I[\Psi]$ the Euclidean action and $\Psi$ a generic field variable. Here, the measure $\mathcal{D}[\Psi]$ includes all fields and not just the classical fields $\widetilde{\Psi}$ that satisfy the equations of motion $\delta I[\widetilde{\Psi}]=0$. However, if the dominant contributions to the partition function come from fields that are close to the classical fields, then the action can be expanded in a Taylor series:
$$I[\widetilde{\Psi}+\delta \Psi]=I[\widetilde{\Psi}]+\delta I[\widetilde{\Psi}, \delta \Psi]+\delta^{2} I[\widetilde{\Psi}, \delta \Psi]+\ldots .$$
In order for the path integral $\mathcal{Z}$ to make sense, at least to second order in the Taylor series, we require that the first term $I[\widetilde{\Psi}]$ be finite and that the linear term $\delta I$ vanish identically. If these conditions are satisfied, then the on-shell partition function is approximated by
$$\widetilde{\mathcal{Z}}=\exp \{-I[\widetilde{\Psi}]\} ;$$
the average energy $\langle E\rangle$ and entropy $S$ are then given by
$$\langle E\rangle=-\frac{\partial \ln \widetilde{\mathcal{Z}}}{\partial \beta} \quad \text { and } \quad S=\beta\langle E\rangle+\ln \widetilde{\mathcal{Z}} .$$
The physical meaning of the energy may differ based on the boundary conditions that are used, i.e. holding the pressure or volume constant.

From Section 3, we know that the Holst-ADS action (6) is functionally differentiable and finite. Therefore we may consider the Holst-ADS partition function
$$\widetilde{\mathcal{Z}}=\exp \left\{-\frac{1}{16 \pi} \int_{\mathcal{M}}\left[\left(\star-\frac{1}{\gamma}\right)(e \wedge e)\right] \wedge \Omega+\frac{6 \varepsilon}{\ell^{2}} \epsilon-\frac{\varepsilon \ell^{2}}{6} \star \Omega \wedge \Omega+\frac{\varepsilon \ell^{2}}{6 \gamma} \Omega \wedge \Omega\right\}$$
for spacetimes with negative cosmological constant and non-zero Pontryagin number. Let us therefore proceed by evaluating the partition function (20) on the Taub-NUT-ADS spacetime.
4.2 Taub-NUT-ADS spacetime

Here we consider the Taub-NUT-ADS spacetime. The metric for four-dimensional Euclidean Taub-NUT spacetime, with negative cosmological constant $\Lambda=-3 \ell^{-2}$, has line element
$$\begin{aligned}
d s^{2} & =V(r)[d \tau+2 N \cos \theta d \phi]^{2}+\frac{d r^{2}}{V(r)}+\left(r^{2}-N^{2}\right)\left(d \theta^{2}+\sin ^{2} \theta d \phi^{2}\right), \\
V(r) & =\frac{r^{2}-2 M r+N^{2}+\left(r^{4}-6 N^{2} r^{2}-3 N^{4}\right) \ell^{-2}}{r^{2}-N^{2}},
\end{aligned}$$
with $N$ the NUT parameter. Regularity of the metric requires that the Euclidean time $\tau$ have a period $\beta=8 \pi N$.

A suitable tetrad of coframes for this spacetime is given by
$$\begin{aligned}
e^{0} & =\sqrt{V} d \tau+2 \sqrt{V} N \cos \theta d \phi, \quad e^{1}=\frac{1}{\sqrt{V}} d r, \quad e^{2}=\sqrt{r^{2}-N^{2}} d \theta, \\
e^{3} & =\sqrt{r^{2}-N^{2}} \sin \theta d \phi .
\end{aligned}$$
The Euclidean action for the Taub-NUT-ADS spacetime is then given by
$$I=I_{0}+\frac{64 \pi^{2} N^{2}}{\gamma}\left(1-\frac{2 N^{2}}{\ell^{2}}\right),$$
with $I_{0}$ the on-shell action of the Taub-NUT-ADS solution without the Holst term (i.e. contributions from the Einstein-Hilbert and cosmological terms only) [20,45]. Substituting this in (16) then gives the on-shell partition function
$$\widetilde{\mathcal{Z}}=\exp \left\{-I_{0}-\frac{64 \pi^{2} N^{2}}{\gamma}\left(1-\frac{2 N^{2}}{\ell^{2}}\right)\right\} .$$
Whence the thermodynamic quantities are given by
$$\langle E\rangle=\langle E\rangle_{0}+\frac{N\left(\ell^{2}-4 N^{2}\right)}{\gamma \ell^{2}} \quad \text { and } \quad S=S_{0}+\frac{4 \pi N^{2}}{\gamma}\left(1-\frac{N^{2}}{\ell^{2}}\right),$$
with $\langle E\rangle_{0}$ and $S_{0}$ denoting (resp.) the average energy and entropy of the Taub-NUT-ADS solution without the Holst term [20, 45].

We conclude that $\gamma$ appears in the thermodynamics of the Taub-NUT-ADS spacetime as a shift in the energy and entropy of the NUT charge (provided that $\gamma$ is finite and real). The quantities derived here are in agreement with previous results found by Mann [20] and Chamblin et al [45] but with a finite shift in the energy and entropy of the Taub-NUT-ADS spacetime; these shifts vanish in the limit when $\gamma$ is taken to infinity.

\section*{5 Summary and discussion}

Let us briefly summarize the main results that are presented in this paper. We studied the properties of the first-order Holst action with non-zero cosmological constant. In particular, we showed that the spacetimes for which $\gamma$ will be present in the on-shell action (14), and hence in the partition function (20), are the ones that have non-diagonalizable metrics and non-zero Pontryagin number. This led us to evaluate (20) on the Taub-NUT-ADS spacetime. It was found that $\gamma$ shifts the energy and entropy of the NUT charge. The analogous results for the case where $\Lambda=0$ are presented in Appendix 1. Some results regarding the Euler characteristic and black-hole mechanics are presented in Appendix 2.

The results found in this paper agree with recent results found by Durka and Kowalski-Glikman [46, 47]. Durka and Kowalski-Glikman derived the Noether-Wald
charges for solutions of a constrained $B F$ theory with $S O(3,2)$ symmetry, first introduced by Freidel and Starodubtsev [48]. They found that $\gamma$ shows up in the Noether-Wald charges of solutions that have $\partial_{\theta} g_{t \phi} \neq 0$. For the Taub-NUT-ADS solution, the energy and entropy are shifted by the same factor as found here, but with $1 / \gamma \rightarrow \gamma$. This is because, in the action that they studied, the Holst and Nieh-Yan terms appear seperately with different weight factors: the Holst term has coefficient $1 / \gamma$ while the Nieh-Yan term has coefficient $\left(\gamma^{2}+1\right) / \gamma$, so their action is fundamentally different. In particular, the limit $\gamma \rightarrow \infty$ cannot be taken in this action to recover the Einstein-Hilbert action. Apart from this minor difference, the two approaches are equivalent: $\gamma$ contributes to the on-shell partition function and to the Noether-Wald charges through the Pontryagin number of the spacetime.

In this paper we considered initially the Holst action with a generic cosmological constant, and in particular focused on the case when $\Lambda<0$. However, in light of cosmological data, it would be of interest to also study in detail the Holst action with $\Lambda>0$. The expression (20) is mathematically valid for any $\operatorname{sign} \varepsilon=\operatorname{sign}(\Lambda)$ of the cosmological constant. An important step toward determining how $\gamma$ affects e.g. the NUT-charged DS spacetimes [49, 50], is to first prove the finiteness of the Holst-DS action with $\varepsilon=1$. Then (20) will be a well-defined partition function for DS spacetimes with non-vanishing Pontryagin number. This approach may also reveal new insights regarding the Kodama wavefunction with arbitrary real values of $\gamma$ [51, 52].

In this paper we looked at the torsion-free case. This field will be non-zero in the presence of fermion couplings, and therefore should be included in the action. Torsion-squared Lagrangian densities in the first-order action have recently been studied in [53, 54]; these terms are all consistent with Corollary 2. Note that in the presence of fermion couplings, $\gamma$ will appear in the chiral anomaly [55]. Of particular interest would be to extend the formalism here to supergravity. To study the effects of $\gamma$ in supergravity, the supersymmetric Holst actions found by Kaul [56] have to be generalized to a manifold with boundary. In practice, however, finding supersymmetric boundary terms without imposing any boundary conditions on the fields is difficult. See [57-59] for details. Ideally we would like to have an action principle for supergravity that is invariant under the off-shell supersymmetry albegra; this suggests that we extend the supergravity action to a manifold with boundary in superspace; such an action without boundary has been recently found by Gates Jr. et al [60] where it was found that $\gamma$ shows up in superspace as the complex component of the gravitational constant.

It would also be of interest to determine the effects of $\gamma$ in quantum gravity by studying more general Euclidean path integrals. Because any topology may occur in classical and quantum gravity, one may have in general a partition function that sums over all possible inequivalent topologies [61-63]. In Section 3 we found that in order for $\gamma$ to be present in the partition function, the Pontryagin number of the
manifolds have to be non-zero, so only those manifolds will contribute to the formal sum. In the case of supergravity with fermion couplings, the existence of a spinor structure on $\mathcal{M}$ requires that the second Stiefel-Whitney class of the manifold be non-zero [64]. This condition places further restrictions on the formal sum.

\section*{Acknowledgements}

The author wishes to thank Remigiusz Durka and Jerzy Kowalski-Glikman for very useful correspondence, and for commenting on a draft of the manuscript. The author also thanks Abhay Ashtekar and David Sloan for discussions during the early stages of this project. This work was supported by NSERC. While at Penn State University, the author was also supported in part by NSF grant PHY0854743, The George A. and Margaret M. Downsbrough Endowment and the Eberly research funds of Penn State.

\section*{A Taub-NUT and Taub-bolt spacetimes}

Here we consider the Taub-NUT spacetime. The metric for four-dimensional $E u$ clidean Taub-NUT spacetime, with zero cosmological constant, has line element
$$\begin{aligned}
d s^{2} & =V(r)[d \tau+2 N \cos \theta d \phi]^{2}+\frac{d r^{2}}{V(r)}+\left(r^{2}-N^{2}\right)\left(d \theta^{2}+\sin ^{2} \theta d \phi^{2}\right), \\
V(r) & =\frac{r^{2}-2 M r+N^{2}}{r^{2}-N^{2}},
\end{aligned}$$
with $N$ the NUT parameter. Regularity of the metric requires that $\tau$ have a period $\beta=8 \pi N$.

A suitable tetrad of co-frames for this spacetime is given by
$$\begin{aligned}
e^{0} & =\sqrt{V} d \tau+2 \sqrt{V} N \cos \theta d \phi, \quad e^{1}=\frac{1}{\sqrt{V}} d r, \quad e^{2}=\sqrt{r^{2}-N^{2}} d \theta, \\
e^{3} & =\sqrt{r^{2}-N^{2}} \sin \theta d \phi .
\end{aligned}$$
Using (10), we find that the Euclidean action for the Taub-NUT spacetime is given by
$$I=4 \pi M N-\frac{2 \pi N^{2}}{\gamma} .$$
Substituting this in (18) then gives the on-shell partition function
$$\widetilde{\mathcal{Z}}=\exp \left(-4 \pi M N+\frac{2 \pi N^{2}}{\gamma}\right) .$$
The thermodynamic quantities can now be calculated. In particular, $M=N$ for the NUT charge and substituting this into (29) gives the average energy and entropy
$$\langle E\rangle=N\left(1-\frac{1}{2 \gamma}\right) \quad \text { and } \quad S=4 \pi N^{2}\left(1-\frac{1}{2 \gamma}\right),$$
while $M=5 N / 4$ for the bolt charge and substituting this into (29) gives the average energy and entropy
$$\langle E\rangle=\frac{5 N}{4}\left(1-\frac{2}{5 \gamma}\right) \quad \text { and } \quad S=5 \pi N^{2}\left(1-\frac{2}{5 \gamma}\right) .$$
Therefore, $\gamma$ appears in the thermodynamics of Taub-NUT and Taub-bolt solutions with zero cosmological constant as shifts in the energies and entropies of the NUT and bolt charges, just as we found for the NUT charge in the Taub-NUT-ADS solution.

\section*{B Euler characteristic and the second law}

In this Appendix, let us present an example that illustrates how a topological invariant of the spacetime manifold can have non-trivial physical effects on black-hole thermodynamics. In particular, we will derive an upper bound on $\theta_{2}$ that must be satisfied in order for the second law to hold when two black holes merge.

The bound presented here is general and holds for solutions to the Gauss-Bonnet field equations in arbitrary dimensions. We will consider four-dimensional asymptotically flat black holes as a special case; in this case the black holes must satisfy certain theorems and these can be used to put a tight upper bound on $\theta_{2}$ for the area theorem to hold when two Schwarzschild black holes merge [74].

For black holes of Gauss-Bonnet gravity with generic cosmological constant $\Lambda$, the first law of black-hole mechanics holds with an entropy that is given by [34, 65, 66]
$$\mathscr{S}=\frac{1}{4 \pi} \oint_{\mathbb{C}} \tilde{\epsilon}\left(1+2 \theta_{2} \mathcal{R}\right) ;$$
here $\mathcal{R}$ is the Ricci scalar of the horizon cross section $\mathbb{C}$ and $\tilde{\epsilon}$ is the area ( $D-2$ )-form on $\mathbb{C}$.

Let us consider the merging of two black holes - one with mass $m_{1}$ and the other with mass $m_{2}$. The entropies of these black holes are (resp.)
$$\mathscr{S}_{1}=\frac{1}{4}\left[\mathscr{A}_{1}+2 \theta_{2} X\left(\mathbb{C}_{1}\right)\right] \quad \text { and } \quad \mathscr{S}_{2}=\frac{1}{4}\left[\mathscr{A}_{2}+2 \theta_{2} X\left(\mathbb{C}_{2}\right)\right] ;$$
here we have defined the surface area $\mathscr{A}$ and correction term $X(\mathbb{C})$ via
$$\mathscr{A}=\oint_{\mathbb{C}} \tilde{\epsilon} \quad \text { and } \quad X(\mathbb{C})=\oint_{\mathbb{C}} \tilde{\epsilon} \mathcal{R} .$$
Before the black holes merge, the total entropy is
$$\mathscr{S}=\mathscr{S}_{1}+\mathscr{S}_{2}=\frac{1}{4}\left[\mathscr{A}_{1}+\mathscr{A}_{2}+2 \theta_{2}\left(X\left(\mathbb{C}_{1}\right)+X\left(\mathbb{C}_{2}\right)\right)\right] .$$
After the black holes merge, the total entropy of the resulting black hole is
$$\mathscr{S}^{\prime}=\frac{1}{4}\left[\mathscr{A}^{\prime}+2 \theta_{2} X\left(\mathbb{C}^{\prime}\right)\right] .$$

The area theorem will hold if and only if $\mathscr{S}^{\prime}>\mathscr{S}$. Thus we have the following bound:
$$\theta_{2}<\frac{-\left(\mathscr{A}_{1}+\mathscr{A}_{2}-\mathscr{A}^{\prime}\right)}{2\left[X(\mathbb{C})+X\left(\mathbb{C}_{2}\right)-X\left(\mathbb{C}^{\prime}\right)\right]} .$$
This bound for $\theta_{2}$ is general, and holds for spacetimes in all dimensions with generic values of $\Lambda$.

Without knowing more about the details of the black holes that are merging, nothing further can be said about the bound (37) because the topological structure of black holes is much richer in $D>4$ dimensions than in four dimensions. When $\Lambda \geq 0$ the topology of black holes in $D \geq 5$ dimensions can be any product manifold $\mathbb{R}^{2} \times \mathbb{C}^{D-2}$, with $\mathbb{C}^{D-2}$ a space of positive Yamabe type. For example, in five dimensions the topology of the event horizon has to be (a connected sum of) a three-sphere $\mathbb{C}^{3} \cong S^{3}$ or three-ring $\mathbb{C}^{3} \cong S^{2} \times S^{1}$. A complete discussion of black holes in higher dimensions is presented in [67]; topological properties are presented in [68-73].

For concreteness, then, let us consider the merging of two non-rotating black holes in four dimensions, with $\Lambda=0$. First, the Gauss-Bonnet theorem says that
$$X(\mathbb{C})=\oint_{\mathbb{C}} \tilde{\epsilon} \mathcal{R}=4 \pi \chi(\mathbb{C}),$$
with $\chi(\mathbb{C})$ the Euler characteristic of $\mathbb{C}$. Then the Hawking topology theorem says that the horizon cross sections can only be two-spheres so that $\mathbb{C} \cong S^{2}$, and then $\chi\left(S^{2}\right)=2$. It follows that
$$X\left(\mathbb{C}_{1}\right)=X\left(\mathbb{C}_{2}\right)=X\left(\mathbb{C}^{\prime}\right)=8 \pi .$$
Finally, the Birkhoff theorem says that the only static asymptotically flat solution to the field equations is the Schwarzschild solution. Since the surface area of a Schwarzschild black hole is related to its mass $m$ via $\mathscr{A}=16 \pi m^{2}$, the surface areas of the initial and final black-hole states are
$$\mathscr{A}_{1}=16 \pi m_{1}^{2}, \quad \mathscr{A}_{2}=16 \pi m_{2}^{2}, \quad \text { and } \quad \mathscr{A}^{\prime}=16 \pi\left(m_{1}+m_{2}-\alpha\right)^{2} .$$
In the above definition for $\mathscr{A}^{\prime}$ the parameter $\alpha \geq 0$ has been added which corresponds to any mass that may be carried away by gravitational radiation during merging. Whence the bound on $\theta_{2}$ :
$$\theta_{2}<2 m_{1} m_{2}-\alpha\left[2\left(m_{1}+m_{2}\right)-\alpha\right] .$$
Therefore, in four-dimensional asymptotically flat spacetimes, the second law will be violated if $\theta_{2}$ is greater than twice the product of the masses of two Schwarzschild black holes before merging minus a correction due to gravitational radiation. This is an important property because it shows that a non-zero Euler characteristic of the manifold with boundary can have physical effects in four dimensions.

\section*{References}
[1] Barbero G J F 1995 Phys. Rev. D 515501
[2] Immirzi G 1997 Real and complex conections for canonical gravity Class. Quant. Grav. 14 L177
[3] Rovelli C and Thiemann T 1997 Immirzi parameter in quantum general relativity Phys. Rev. D 571009
[4] Ashtekar A and Lewandowski J 2004 Background-independent quantum gravity: a progress report Class. Quantum Grav. 21 R53
[5] Rovelli C 2004 Quantum Gravity (Cambridge: Cambridge University Press)
[6] Thiemann T 2007 Modern Canonical Quantum General Relativity (Cambridge: Cambridge University Press)
[7] Ashtekar A, Baez J, Corichi A and Krasnov K 1998 Quantum geometry and black hole entropy Phys. Rev. Lett. 80904
[8] Ashtekar A, Baez J and Krasnov K 2000 Quantum geometry of isolated horizons and black hole entropy Adv. Theor. Math. Phys. 41
[9] Ashtekar A, Engle J, Pawlowski T and Van Den Broeck C 2005 Quantum horizons and black hole entropy: inclusion of distortion and rotation Class. Quantum Grav. 22 L27
[10] Kloster S, Brannlund J and DeBenedictis A 2008 Phase-space and black hole entropy of toroidal and higher-genus horizons in Loop Quantum Gravity Class. Quantum Grav. 25065008
[11] Newman E, Tamburino, L and Unti T 1963 Empty-space generalization of the Schwarzschild metric J. Math. Phys. 4915
[12] Misner C W 1963 The flatter regions of Newman, Unti and Tamburino's generelized Schwarzschild space J. Math. Phys. 4924
[13] Hawking S W and Hunter C J 1999 Gravitational entropy and global structure Phys. Rev. D 59044025
[14] Holst S 1996 Barbero's Hamiltonian derived from a generalized Hilbert-Palatini action Phys. Rev. D 535966
[15] Gibbons G W and Hawking S W 1977 Action integrals and partition functions in quantum gravity Phys. Rev. D 152752
\begin{itemize}
\item[] [16] Hawking S W 1979 The path-integral approach to quantum gravity Quantum Gravity. An Einstein Centenary Survey ed S W Hawking and W Israel (Cambridge: Cambridge University Press)
\item[] [17] Balasubramanian V and Kraus A 1999 A stress tensor for anti-de Sitter gravity Commun. Math. Phys. 208413
\item[] [18] Kraus P, Larsen F and Siebelink R 1999 The gravitational action in asymptotically ADS and flat spacetimes Nucl. Phys. B 563259
\item[] [19] Lau S R 1999 Light-cone reference for total gravitational energy Phys. Rev. D 60104034
\item[] [20] Mann R B 1999 Misner string entropy Phys. Rev. D 60104047
\item[] [21] Mann R B and Marolf D 2006 Holographic renormalization of asymptotically flat spacetimes Class. Quantum Grav. 2329277
\item[] [22] Freidel L, Minic, D and Takeuchi T 2005 Quantum gravity, torsion, parity violation, and all that Phys. Rev. D 72104002
\item[] [23] Rezende D J and Perez A 2009 Four-dimensional Lorentzian Holst action with topological terms Phys. Rev. D 79064026
\item[] [24] Mercuri S 2006 Fermions in the Ashtekar-Barbero connection formalism for arbitrary values of the Immirzi parameter Phys. Rev. D 73084016
\item[] [25] Mercuri S 2008 From the Einstein-Cartan to the Ashtekar-Barbero canonical constraints, passing through the Nieh-Yan functional Phys. Rev. D 77024036
\item[] [26] Ashtekar A, Romano J D and Tate R S 1989 New variables for gravity: inclusion of matter Phys. Rev. D 402572
\item[] [27] Ashtekar A, Fairhurst S and Krishnan B 2000 Isolated horizons: Hamiltonian evolution and the first law Phys. Rev. D 62104025
\item[] [28] Ashtekar A, Beetle C and Lewandowski J 2001 Mechanics of rotating isolated horizons Phys. Rev. D 64044016
\item[] [29] Ashtekar A and Corichi A 2000 Laws governing isolated horizons: inclusion of dilaton couplings Class. Quantum Grav. 171317
\item[] [30] Corichi A and Sudarsky D 2000 Einstein-Yang-Mills isolated horizons: phase space, mechanics, hair and conjectures Phys. Rev. D 62044046
\item[] [31] Ashtekar A, Corichi A and Sudarsky D 2003 Non-minimally coupled scalar fields and isolated horizons Class. Quantum Grav. 203413
\end{itemize}
\begin{itemize}
\item[] [32] Korzyński M, Lewandowski J and Pawlowski T 2005 Mechanics of multidimensional isolated horizons Class. Quantum Grav. 222
\item[] [33] Ashtekar A, Pawlowski T and Van Den Broeck C 2007 Mechanics of higher-dimensional black holes in asymptotically anti-de Sitter spacetimes Class. Quantum Grav. 24625
\item[] [34] Liko T and Booth I 2007 Isolated horizons in higher dimensional Einstein-Gauss-Bonnet gravity Class. Quantum Grav. 243769
\item[] [35] Liko T and Booth I 2008 Supersymmetric isolated horizons Class. Quantum Grav. 25105020
\item[] [36] Booth I and Liko T 2008 Supersymmetric isolated horizons in ADS spacetime Phys. Lett. B 67061
\item[] [37] Liko T 2009 Isolated horizons, $p$ form matter fields, topology and the blackhole/string correspondence principle Phys. Rev. D 79084038
\item[] [38] Copsey K and Horowitz G T 2006 Role of dipole charges in black hole thermodynamics Phys.Rev. D 73024015
\item[] [39] Ashtekar A, Engle J and Sloan D 2008 Asymptotics and Hamiltonians in a first-order formalism Class. Quantum Grav. 25095020
\item[] [40] Ashtekar A and Sloan D 2008 Action and Hamiltonians in higher dimensional general relativity: First order framework Preprint arXiv:0808.2069 [gr-qc]
\item[] [41] Liko T and Sloan D 2009 First-order action and Euclidean quantum gravity Class. Quantum Grav. 26145004
\item[] [42] Corichi A and Wilson-Ewing E 2010 Surface terms, asymptotics and thermodynamics of the Holst action Class. Quantum Grav. 27205015
\item[] [43] Aros R, Contreras M, Olea R, Troncoso R and Zanelli J 2000 Conserved charges for gravity with locally anti-de Sitter asymptotics Phys. Rev. Lett. 841647
\item[] [44] Hawking S W 1977 Gravitational instantons Phys.Lett. A 6081
\item[] [45] Chamblin A, Emparan R, Johnson C V and Myers R C 1999 Large N phases, gravitational instantons and the nuts and bolts of AdS holography Phys. Rev. D 59064010
\item[] [46] Durka R and Kowalski-Glikman J 2011 Gravity as a constrained BF theory: Noether charges and Immirzi parameter Phys.Rev. D 83124011
\item[] [47] Durka R 2012 Immirzi parameter and Noether charges in first order gravity $J$. Phys. Conf. Ser. 343012032
\end{itemize}
\begin{itemize}
\item[] [48] Freidel L and Starodubtsev A 2005 Quantum gravity in terms of topological observables arXiv Preprint hep-th/0501191
\item[] [49] Clarkson R, Ghezelbash M and Mann R 2004 Mass, action, and entropy of Taub-boltde Sitter spacetimes Phys. Rev. Lett. 91061301
\item[] [50] Clarkson R, Ghezelbash M and Mann R 2004 A review of the $N$-bound and the maximal mass conjectures using nut-charged DS spacetimes Int. J. Mod. Phys. A 193987
\item[] [51] Randono A 2007 Generalizing the Kodama state. I. Construction arXiv Preprint gr-qc/0611073
\item[] [52] Randono A 2007 Generalizing the Kodama state. II. Properties and physical interpretation arXiv Preprint gr-qc/0611074
\item[] [53] Diakonov D, Tumanov A G and Vladimirov A A 2011 Low-energy General Relativity with torsion: a systematic derivative expansion Preprint arXiv:1104.2432 [hep-th]
\item[] [54] Baekler P and Hehl F W 2011 Beyond Einstein-Cartan gravity: quadratic torsion and curvature invariants with even and odd parity including all boundary terms Class. Quantum Grav. 28215017
\item[] [55] Chandia O and Zanelli J 1997 Topological invariants, instantons, and the chiral anomaly on spaces with torsion Phys. Rev. D 557580
\item[] [56] Kaul R 2008 Holst actions for supergravity theories Phys. Rev. D 77045030
\item[] [57] van Nieuwenhuizen P and Belyaev D M 2008 Tensor calculus for supergravity on a manifold with boundary J. High Energy Phys. 0802047
\item[] [58] van Nieuwenhuizen P and Belyaev D M 2008 Rigid supersymmetry with boundaries J. High Energy Phys. 0804008
\item[] [59] van Nieuwenhuizen P and Belyaev D M 2008 Simple $d=4$ supergravity with a boundary J. High Energy Phys. 0809069
\item[] [60] Gates Jr. S J, Ketov S V and Yunes N 2009 Seeking the loop quantum gravity Barbero-Immirzi parameter and field in 4D, $N=1$ supergravity Phys. Rev. D 80065003
\item[] [61] Isham C J 1981 Topological $\theta$-sectors in canonically quantized gravity Phys. Lett. B 106188
\item[] [62] Hartle J B and Witt D M 1988 Gravitational $\theta$ states and the wave function of the universe Phys. Rev. D 372833
\end{itemize}
\begin{itemize}
\item[] [63] Carlip S 1998 Dominant topologies in Euclidean Quantum Gravity Class. Quant. Grav. 152629
\item[] [64] Isham C J and Pope C N 1982 A spinor field representation of the Stiefel-Whitney class Phys. Lett. B 114137
\item[] [65] Jacobson T, Kang G and Myers R C 1994 On black hole entropy Phys. Rev. D 496587
\item[] [66] Clunan T, Ross S F and Smith D J 2004 On Gauss-Bonnet black hole entropy Class. Quantum Grav. 213447
\item[] [67] Emparan R and Reall H S 2008 Black holes in higher dimensions Living Rev. Rel. 116
\item[] [68] Cai M and Galloway G J 2001 On the topology and area of higher-dimensional black holes Class. Quantum Grav. 182707
\item[] [69] Galloway G J and Schoen R 2006 A generalization of Hawking's topology theorem to higher dimensions Commun. Math. Phys. 266571
\item[] [70] Galloway G J 2006 Rigidity of outer horizons and the topology of black holes Preprint gr-qc/0608118
\item[] [71] Helfgott C, Oz Y and Yanay Y 2006 On the topology of stationary black hole event horizons in higher dimensions J. High Energy Phys. 02025
\item[] [72] Rácz I 2008 A Simple proof of the recent generalisations of Hawking's black hole topology theorem Class. Quant. Grav. 25162001
\item[] [73] Hollands S, Holland J and Ishibashi A 2011 Further restrictions on the topology of stationary black holes in five dimensions Annales Henri Poincare 12279
\item[] [74] Liko T 2008 Topological deformation of isolated horizons Physical Review D 77064004
\end{itemize}