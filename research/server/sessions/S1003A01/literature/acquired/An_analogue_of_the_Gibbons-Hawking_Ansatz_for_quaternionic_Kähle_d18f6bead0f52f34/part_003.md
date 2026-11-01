---
retention_scope: session
part: 3
total_parts: 3
---

[Part 3/3 of: An analogue of the Gibbons-Hawking Ansatz for quaternionic Kähler spaces]

From them, we can transition back to a vectorial formalism by writing
$$h^{I}-2 \rho^{I} \theta=\mathscr{U}^{I J}\left(d \psi_{J}+\mathscr{A}_{J}+2 \mathscr{U}_{J K} \vec{\rho}^{K} \cdot \vec{\theta}\right)+d \vec{\rho}^{I}-2 \theta_{0} \vec{\rho}^{I}+2 \vec{\theta} \times \vec{\rho}^{I}$$
which then, upon substitution into the two formulas above, gives us the equivalent-and also most explicit - expressions
$$\begin{aligned}
s \vec{\omega}= & -\frac{1}{2 \mathscr{U}} \mathscr{U}_{I J}\left(d \vec{\rho}^{I}-2 \theta_{0} \vec{\rho}^{I}+2 \vec{\theta} \times \vec{\rho}^{I}\right) \wedge\left(d \vec{\rho}^{J}-2 \theta_{0} \vec{\rho}^{J}+2 \vec{\theta} \times \vec{\rho}^{J}\right) \\
& -\frac{1}{\mathscr{U}}\left(d \vec{\rho}^{I}-2 \theta_{0} \vec{\rho}^{I}+2 \vec{\theta} \times \vec{\rho}^{I}\right) \wedge\left(d \psi_{I}+\mathscr{A}_{I}+2 \mathscr{U}_{I K} \vec{\rho}^{K} \cdot \vec{\theta}\right) \\
s g= & \frac{1}{2 \mathscr{U}} \mathscr{U}_{I J}\left(d \vec{\rho}^{I}-2 \theta_{0} \vec{\rho}^{I}+2 \vec{\theta} \times \vec{\rho}^{I}\right) \cdot\left(d \vec{\rho}^{J}-2 \theta_{0} \vec{\rho}^{J}+2 \vec{\theta} \times \vec{\rho}^{J}\right) \\
+ & \frac{1}{2 \mathscr{U}} \mathscr{U}^{I J}\left(d \psi_{I}+\mathscr{A}_{I}+2 \mathscr{U}_{I K} \vec{\rho}^{K} \cdot \vec{\theta}\right)\left(d \psi_{J}+\mathscr{A}_{J}+2 \mathscr{U}_{J L} \vec{\rho}^{L} \cdot \vec{\theta}\right)
\end{aligned}$$

The 1 -forms $\theta_{0}$ and $\vec{\theta}$ are given in turn by the formulas (149) and (151). In this formulation, in particular, it is straightforward to see that the vector fields $\partial_{\psi_{I}}$ generate an isometric $\mathbb{R}^{n+1}$-action with Galicki-Lawson moment map
$$\partial_{\psi_{I}} \longmapsto \vec{\nu}^{I}=\frac{\vec{\rho}^{I}}{\mathscr{U}} .$$

In the next subsection we compile for easy reference and present in an intrinsic geometric language the quaternionic Kähler construction which emerged from these considerations, in a form mirroring our earlier presentation of the extended Gibbons-Hawking hyperkähler construction.

\subsection*{3.5. The quaternionic Kähler Ansatz.}

Consider a principal $\mathbb{R}^{n+1}$-bundle $M$ over an open subset $\mathscr{S}$ of $\operatorname{Im} \mathbb{H} \mathbb{P}^{n}$ and, alongside it, the restrictions to $\mathscr{S}$ of the associated $\mathbb{H}^{\times} / \mathbb{Z}_{2}$-bundles $E^{(\text {rep })}$ over $\operatorname{Im} \mathbb{H P}^{n}$ defined in subsection 3.3, which we denote with the same symbols.
![](https://cdn.mathpix.com/cropped/700f600f-dee0-402c-926d-8ee49fb86e62-40.jpg?height=173&width=365&top_left_y=1052&top_left_x=888)
Let $\vec{\nabla}_{I}$ denote the connections induced on the latter bundles by the trivial connection $\vec{\partial}_{I}$ on $\mathbb{R}^{n+1} \otimes \mathbb{R}^{3}$.

In this setup we want to formulate two sets of field equations. For the first one let us assume that we have either

Ia. a section $\mathscr{U}_{I J}$ of the bundle $\operatorname{Sym}(M \otimes M) \otimes E^{(-1,1)}$ over $\mathscr{S}$ satisfying the firstorder differential constraints
$$\vec{\nabla}_{I} \mathscr{U}_{K J}=\vec{\nabla}_{J} \mathscr{U}_{K I}$$
or, alternatively,
Ib. a section $\mathscr{U}$ of the line bundle $E^{(+1,1)}$ over $\mathscr{S}$ satisfying the second-order differential constraints
$$\vec{\nabla}_{I} \times \vec{\nabla}_{J} \mathscr{U}=\overrightarrow{0} .$$
For which one of these conditions we opt is immaterial because
Lemma 16. The two conditions are equivalent, with the maps between them given, respectively, by
$$\mathscr{U}=2 \mathscr{U}_{I J} \vec{\rho}^{I} \cdot \vec{\rho}^{J} \quad \text { and } \quad \mathscr{U}_{I J}=\frac{1}{4} \vec{\nabla}_{I} \cdot \vec{\nabla}_{J} \mathscr{U} .$$
This follows immediately from Proposition 15 by reduction. One can in fact give a completely intrinsic proof of this result simply by mimicking the proof of Proposition 15 in covariant calculus language and noticing that the symmetry constraints there show up here in the guise of section type constraints.

On the other hand, for the second set of field equations let us assume that we have, in addition,
II. a principal connection on $M$ with curvature 2-form $\left(\mathscr{F}_{K}\right)_{K=0, \ldots, n}$ determined by the Higgs field through the following Bogomolny-like condition:
$$\mathscr{F}_{K}=\frac{1}{2} \vec{\nabla}_{I} \mathscr{U}_{K J} \cdot\left(d \vec{\rho}^{I} \wedge d \vec{\rho}^{J}\right) .$$

Based on the previous considerations we can now state the following
Theorem 17. Let $\left(\mathscr{U}_{I J}, \mathscr{F}_{K}\right)$ or, equivalently, $\left(\mathscr{U}, \mathscr{F}_{K}\right)$ be a set of solutions to the above field equations, and assume that we can adjust the open subset $\mathscr{S}$ of $\operatorname{Im} \mathbb{H P}^{n}$ on which they are defined in such a way as to have both $\operatorname{det}\left(\mathscr{U}_{I J}\right) \neq 0$ and $\mathscr{U} \neq 0$ everywhere on it. On the total space of the $\mathbb{R}^{n+1}$-bundle $M$ we associate to this solution the triplet of 1-forms
$$\vec{\theta}=-\mathscr{W}_{I J} \vec{\nu}^{J} \times d \vec{\nu}^{I}-\vec{\nu}^{I}\left(d \psi_{I}+\mathscr{A}_{I}\right)$$
and triplet of 2-forms
$$\begin{aligned}
s \vec{\omega}= & -\frac{1}{2} \mathscr{W}_{I J}\left(d \vec{\nu}^{I}+2 \vec{\theta} \times \vec{\nu}^{I}\right) \wedge\left(d \vec{\nu}^{J}+2 \vec{\theta} \times \vec{\nu}^{J}\right) \\
& -\left(d \vec{\nu}^{I}+2 \vec{\theta} \times \vec{\nu}^{I}\right) \wedge\left(d \psi_{I}+\mathscr{A}_{I}+2 \mathscr{W}_{I K} \vec{\nu}^{K} \cdot \vec{\theta}\right)
\end{aligned}$$
expressed here in a local coordinate trivialization, with $\psi_{I}$ coordinates on the fibers and $\vec{\rho}^{I}$ inhomogeneous coordinates on the base; by definition, $s$ is a non-vanishing real constant, $\mathscr{A}_{K}$ is a local connection 1-form with curvature $d \mathscr{A}_{K}=\mathscr{F}_{K}$,
$$\mathscr{W}_{I J}=\mathscr{U} \mathscr{U}_{I J} \quad \text { and } \quad \vec{\nu}^{I}=\frac{\vec{\rho}^{I}}{\mathscr{U}} .$$
These then form a quaternionic Kähler structure on $M$, with quaternionic Kähler metric
$$\begin{aligned}
s g & =\frac{1}{2} \mathscr{W}_{I J}\left(d \vec{\nu}^{I}+2 \vec{\theta} \times \vec{\nu}^{I}\right) \cdot\left(d \vec{\nu}^{J}+2 \vec{\theta} \times \vec{\nu}^{J}\right) \\
& +\frac{1}{2} \mathscr{W}^{I J}\left(d \psi_{I}+\mathscr{A}_{I}+2 \mathscr{W}_{I K} \vec{\nu}^{K} \cdot \vec{\theta}\right)\left(d \psi_{J}+\mathscr{A}_{J}+2 \mathscr{W}_{J L} \vec{\nu}^{L} \cdot \vec{\theta}\right)
\end{aligned}$$
possessing an isometric locally free $\mathbb{R}^{n+1}$-action generated by the vector fields $\partial_{\psi_{I}}$, with corresponding Galicki-Lawson moment map images $\vec{\nu}^{I}$.

Conversely, any $4 n$-dimensional quaternionic Kähler manifold with an isometric locally free $\mathbb{R}^{n+1}$-action arises locally in this way.

The direct claim encapsulates the results of the previous subsection. Our arguments there have yielded in fact three more equivalent sets of formulas for the quaternionic Kähler connection 1-forms, 2-forms and metric, which we list by reference number in Table 2.

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|}
\hline & $\theta$ & $s \omega$ & $s g$ & Formalism \\
\hline 1. & eq. (147) & eq. (148) & eq. (148) & quaternionic \\
\hline 2. & eq. (147) & eq. (156) & eq. (156) & quaternionic \\
\hline 3. & eqs. (149) \& (151) & eq. (158) & eq. (159) & vectorial \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 2. Alternative expressions for the quaternionic Kähler connection 1 -forms, 2 -forms and metric.}
\end{table}

For the converse statement, if we assume that we have a $4 n$-dimensional quaternionic Kähler space $M$ with an isometric locally free $\mathbb{R}^{n+1}$-action, then by Theorem 13 this action lifts to an $\mathbb{R}^{n+1}$-action on the $4(n+1)$-dimensional Swann bundle $\mathcal{U}(M)$. Bielawski's Proposition 2.1 from [10] guarantees then that the hyperkähler structure on $\mathcal{U}(M)$ is given
locally by an extended Gibbons-Hawking construction. In particular, corresponding to these actions, the quaternionic Kähler moment maps are lifted to hyperkähler moment maps in accordance with the rule (82), and so we conclude that the canonical $\mathbb{H}^{\times} / \mathbb{Z}_{2}$-action on $\mathcal{U}(M)$ acts on the base of the extended Gibbons-Hawking fibration by what we have called collective transformations. We find ourselves therefore within the bounds of Proposition 14, which means that we can repeat ad litteram the reduction procedure of subsection §3.4 to obtain an explicit local description of the quaternionic Kähler structure on $M$ in the precise same category as the one above, proving thus the generality of this construction.

The theorem encompasses the range of both definite and indefinite signature metrics. The construction it describes is in a very clear sense a quaternionic Kähler analogue of the extended Gibbons-Hawking hyperkähler Ansatz. The role of hyperkähler moment map is played here by Galicki and Lawson's concept of quaternionic Kähler moment map; however, unlike in the Gibbons-Hawking case, the moment map images do not define coordinates (for which purpose they would be too many) but, rather, they are related to these through a scaling factor. Another, more surprising departure from the extended Gibbons-Hawking case is the existence of a dual description implying that the quaternionic Kähler structure is, quite remarkably, completely determined locally in all dimensions by a single real-valued potential $\mathscr{U}$ satisfying a set of linear differential constraints. The linearity, in particular, means that in a very definite sense one can superpose two such quaternionic Kähler structures to obtain a third.

\subsection*{3.6. The case of four dimensions.}

We end this section with a closer look at the four-dimensional (i.e. $n=1$ ) specialization of this construction. In this case, $M$ is the four-dimensional avatar of a quaternionic Kähler space - namely, a self-dual Einstein space with non-vanishing scalar curvature-possessing two linearly independent commuting Killing vector fields. The local geometry of this class of spaces was described explicitly by Calderbank and Pedersen in [13] in terms of an eigenfunction of the Laplacian on the Poincaré half-plane, following an intrinsic, four-dimensional analysis based on previous work by Joyce [34], Ward [48] and Tod [47], among others. We will now show that our results reproduce theirs in this dimension, while also offering a few additional bonuses. In this sense, therefore, the construction of Theorem 17 may be viewed as a higher-dimensional generalization of the Calderbank-Pedersen construction-similarly, although much less trivially, to the way in which, in hyperkähler context, the extended Gibbons-Hawking construction of [32, 41] can be viewed as a higher-dimensional generalization of the original four-dimensional Gibbons-Hawking one.

First, let us observe that for $n=1$ the space $\operatorname{Im} \mathbb{H P}^{1}$ is isomorphic to the upper-half plane $\mathscr{H}^{2}$ and can be covered by a single inhomogeneous coordinate chart. We choose the inhomogeneous coordinates as in the Example in §3.3.1 to be given by
$$\begin{aligned}
& \vec{\rho}^{0}=\mathbf{i} \\
& \vec{\rho}^{1}=\rho_{1} \mathbf{i}+\rho_{2} \mathbf{j}
\end{aligned}$$
with $\rho_{2}>0$, where, for simplicity, we drop the now inessential upper index 1 from the notation of the components of the second vector. As argued subsequently in §3.3.2, a choice of inhomogeneous coordinates fixes completely the form of the covariant connections induced on bundles $E^{(\mathfrak{r e p})} \rightarrow \operatorname{Im} \mathbb{H} \mathbb{P}^{1}$ by the trivial connection on, in this case, $\mathbb{R}^{2} \otimes \mathbb{R}^{3}$. To
determine these, we need both the connection coefficients $\left(\mathfrak{A}_{I i}\right)_{I=0,1}$, which are already listed in (123), and the operators $\left(\mathfrak{D}_{I i}\right)_{I=0,1}$, which in this case can be worked out to be
$$\begin{aligned}
& \overrightarrow{\mathfrak{D}}_{0}=-\mathbf{i}\left(\rho_{1} \partial_{\rho_{1}}+\rho_{2} \partial_{\rho_{2}}\right)+\mathbf{j}\left(\rho_{2} \partial_{\rho_{1}}-\rho_{1} \partial_{\rho_{2}}\right) \\
& \overrightarrow{\mathfrak{D}}_{1}=\mathbf{i} \partial_{\rho_{1}}+\mathbf{j} \partial_{\rho_{2}} .
\end{aligned}$$

Note that for this choice of inhomogeneous coordinates the only non-vanishing contribution on the right-hand side of the second reduced Bogomolny equation (165) comes possibly from the term $\nabla_{13} \mathscr{U}_{K 1} d \rho_{1} \wedge d \rho_{2}$. However, this covariant derivative vanishes, too, and the equation becomes simply
$$\mathscr{F}_{K}=0 .$$
This means that in four dimensions we can consistently set in the formulas, which are locally defined, $\mathscr{A}_{K}=0$.

In fact, a simple inspection shows that for this choice of inhomogeneous coordinates any covariant derivative $\nabla_{I i}$ with $i=3$ of no matter what section vanishes. The second-order differential constraints (163) reduce therefore to a single one, which reads
$$\rho_{2}\left(\mathscr{U}_{\rho_{1} \rho_{1}}+\mathscr{U}_{\rho_{2} \rho_{2}}\right)=\mathscr{U}_{\rho_{2}}$$
with the indices indicating derivatives. To obtain this result it is important to recall that $\mathscr{U}$ is a section of the bundle $E^{(1, \mathbf{1})}$, and so $\nabla_{I i} \mathscr{U}$ is a section of the bundle $M^{*} \otimes E^{(0, \mathbf{3})}$. The calculation of covariant derivatives of both such sections has been described in detail in §3.3.5. The constraint can be equivalently recast in the form
$$\Delta_{\mathscr{H}^{2}}\left(\frac{\mathscr{U}}{\sqrt{\rho_{2}}}\right)=\frac{3}{4} \frac{\mathscr{U}}{\sqrt{\rho_{2}}}$$
where $\Delta_{\mathscr{H}^{2}}=\rho_{2}^{2}\left(\partial_{\rho_{1}}^{2}+\partial_{\rho_{2}}^{2}\right)$ is the Laplacian corresponding to the Poincaré metric
$$g_{\mathscr{H}^{2}}=\frac{d \rho_{1}^{2}+d \rho_{2}^{2}}{4 \rho_{2}^{2}}$$
on the upper half-plane. We retrieve thus a first key result of Calderbank and Pedersen.
Let us define now the following 1-forms supported on the $\mathbb{R}^{2}$-fibers
$$\lambda_{i}=2 \rho_{i}^{I} d \psi_{I}=2\left(\begin{array}{r}
d \psi_{0}+\rho_{1} d \psi_{1} \\
\rho_{2} d \psi_{1} \\
0
\end{array}\right)$$
and similarly fiberwise acting commuting vector fields
$$v_{i}=\nabla_{I i} \mathscr{U} \partial_{\psi_{I}}=\left(\begin{array}{r}
\left(\mathscr{U}-\rho_{1} \mathscr{U}_{\rho_{1}}-\rho_{2} \mathscr{U}_{\rho_{2}}\right) \partial_{\psi_{0}}+\mathscr{U}_{\rho_{1}} \partial_{\psi_{1}} \\
\left(\rho_{2} \mathscr{U}_{\rho_{1}}-\rho_{1} \mathscr{U}_{\rho_{2}}\right) \partial_{\psi_{0}}+\mathscr{U}_{\rho_{2}} \partial_{\psi_{1}} \\
0
\end{array}\right) .$$
The third component vanishes in each case. The remaining components, $\lambda_{1}, \lambda_{2}$ and $v_{1}, v_{2}$, form a local coframe and frame, respectively, for the $\mathbb{R}^{2}$-fibers. By resorting to the relation (150), we obtain then that
$$\mathscr{U}_{I J} \rho_{i}^{I} \rho_{j}^{J}=\frac{1}{4} \iota_{v_{j}} \lambda_{i}=\frac{1}{2}\left(\begin{array}{rrr}
\mathscr{U}-\rho_{2} \mathscr{U}_{\rho_{2}} & \rho_{2} \mathscr{U}_{\rho_{1}} & 0 \\
\rho_{2} \mathscr{U}_{\rho_{1}} & \rho_{2} \mathscr{U}_{\rho_{2}} & 0 \\
0 & 0 & 0
\end{array}\right) .$$

Again, all components along the third direction vanish, leaving a two-dimensional nonvanishing square block. Since in this case the Higgs field matrix $\left(\mathscr{U}_{I J}\right)_{I, J=0,1}$ is also two-dimensional, this relation can be used to determine it explicitly through a straightforward exercise in linear algebra. One obtains the same result, although at a greater expense of calculational effort, from the second relation (164), upon use of the constraint (172), which serves to eliminate the second derivatives of $\mathscr{U}$.

Knowledge of the Higgs field and principal $\mathbb{R}^{2}$-connection allows us now to work out explicitly the geometric structure on $M$ given by Theorem 17. Upon substitution, the formula (151) yields, on one hand,
$$\vec{\theta}=-\frac{1}{2 \mathscr{U}}\left[\lambda_{1} \mathbf{i}+\lambda_{2} \mathbf{j}+\left(\mathscr{U}_{\rho_{1}} d \rho_{2}-\mathscr{U}_{\rho_{2}} d \rho_{1}\right) \mathbf{k}\right] .$$
To formulate the remaining results it is useful to define the quaternionic-valued 1-form
$$\xi=\frac{d \rho_{1} \mathbf{i}+d \rho_{2} \mathbf{j}}{2 \rho_{2}}+\frac{\varepsilon\left(v_{1}, d \psi\right)+\varepsilon\left(v_{2}, d \psi\right) \mathbf{k}}{\varepsilon\left(v_{1}, v_{2}\right)}$$
where $\varepsilon=d \psi_{0} \wedge d \psi_{1}$ is the standard symplectic form on the $\mathbb{R}^{2}$-fibers and $\varepsilon\left(v_{i}, d \psi\right)$ are the same thing as $\iota_{v_{i}} \varepsilon$. The formulas (158) and (159) reduce then, on the other hand, following an extended calculation, to the simple expressions
$$\begin{aligned}
s \omega & =\frac{\rho_{2} \varepsilon\left(v_{1}, v_{2}\right)}{\mathscr{U}^{2}} \bar{\xi} \wedge \xi \\
s g & =\frac{\rho_{2} \varepsilon\left(v_{1}, v_{2}\right)}{\mathscr{U}^{2}}|\xi|^{2} .
\end{aligned}$$
One can easily verify that this metric coincides indeed, up to a function redefinition, with the one found by Calderbank and Pedersen in [13] or, rather, with the version given by formula (2.4) from [14]. The structure it describes is that of an $\mathbb{R}^{2}$-fibration over the Poincaré upper half-plane, conformally rescaled. In particular, this form makes it clear that, as observed in [13], if we assume that $g$ is positive definite, the sign of the scalar curvature is dictated by the sign of the factor $\varepsilon\left(v_{1}, v_{2}\right)=\mathscr{U}_{\mathscr{U}_{\rho_{2}}}-\rho_{2}\left(\mathscr{U}_{\rho_{1}}^{2}+\mathscr{U}_{\rho_{2}}^{2}\right)$.

\section*{4. Hyperkähler cones via the Legendre transform construction}

\subsection*{4.1. The Legendre transform construction.}

Translating into geometric terms insights derived from a supersymmetric quantum field-theoretic problem [38], Hitchin, Karlhede, Lindström and Roček introduced in [32] a method of constructing hyperkähler metrics of extended Gibbons-Hawking type known as the Legendre transform construction. In this approach, the metric information is stored in a single real-valued function $L$ defined on some open subset $S$ of $\mathbb{R}^{m} \otimes \mathbb{R}^{3}$, satisfying the linear second-order differential constraints
$$\vec{\partial}_{I} \cdot \vec{\partial}_{J} L=0 \quad \text { and } \quad \vec{\partial}_{I} \times \vec{\partial}_{J} L=\overrightarrow{0} .$$
This function is associated to a choice of direction in $\mathbb{R}^{3}$, which we take here to be the direction of the i-axis. Accordingly, it is convenient to view the space $\mathbb{R}^{m} \otimes \mathbb{R}^{3}$ as $\mathbb{C}^{m} \times \mathbb{R}^{m}$ and work with the complex linear combinations $z^{I}=\frac{1}{2}\left(x_{2}^{I}+i x_{3}^{I}\right), x^{I}=x_{1}^{I}, \bar{z}^{I}=\frac{1}{2}\left(x_{2}^{I}-i x_{3}^{I}\right)$ of the real coordinates $x_{i}^{I}$. In terms of these, the differential constraints take the form
$$L_{x^{I} x^{J}}=-L_{z^{I} \bar{z}^{J}} \quad \text { and } \quad L_{x^{I} z^{J}}=L_{x^{J} z^{I}} .$$

The hyperkähler geometric structure is then extracted from $L$ based on the following two properties:
\begin{itemize}
\item[1)] The (flipped-sign) Legendre transform
$$\kappa(z, \bar{z}, u, \bar{u})=\left\langle L(z, \bar{z}, x)-2 \operatorname{Im} u_{I} x^{I}\right\rangle_{x}$$
of the function $L$ with respect to the $x^{I}$-variables, where one assumes that the Legendre constraints $L_{x^{I}}=2 \operatorname{Im} u_{I}$ can be implicitly solved to give unequivocally $x^{I}=x^{I}(z, \bar{z}, u, \bar{u})$, yields a Kähler potential for the hyperkähler symplectic form $\Omega_{1}$ along the chosen direction, together with a complete set of coordinates $z^{I}$ and $u_{I}$ holomorphic with respect to the corresponding complex structure $I_{1}$.
\item[2)] These coordinates are, simultaneously, complex Darboux coordinates for the transversal complex symplectic form, that is,
$$\Omega_{+} \equiv \frac{1}{2}\left(\Omega_{2}+i \Omega_{3}\right)=d u_{I} \wedge d z^{I} .$$
\end{itemize}
The two conditions suffice to determine all three hyperkähler symplectic forms $\Omega_{1}, \Omega_{2}, \Omega_{3}$, and hence also the hyperkähler metric $G$. And indeed, one can verify that these are of extended Gibbons-Hawking type, with
$$\begin{aligned}
U_{I J} & =-\frac{1}{2} L_{x^{I} x^{J}} \\
A_{I} & =\operatorname{Im}\left(L_{x^{I} z^{J}} d z^{J}\right)+d \phi_{I}
\end{aligned}$$
and also $\psi_{I}=\operatorname{Re} u_{I}-\phi_{I}$, where $\phi_{I}$ is an arbitrary real shift. The last relation can be combined with the Legendre constraints to give
$$u_{I}=\psi_{I}+\phi_{I}+\frac{i}{2} L_{x^{I}} .$$
The differential constraints (182) guarantee moreover that these connection 1-forms and Higgs field satisfy as required the extended Bogomolny field equations.

This construction is general, in the sense that any hyperkähler manifold of extended Gibbons-Hawking type is locally given by such a Legendre transform construction for some potential $L$ (see Proposition 2.1 in [10]).

\subsection*{4.2. Hyperkähler cone structure conditions.}
4.2.1. Let us work out now how hyperkähler cone structures are described in this approach, or, in other words, how the conditions of subsection 3.2 translate in terms of the potential $L$.

Consider the following two complex linear combinations of the generators of the collective $\mathbb{H}^{\times} / \mathbb{Z}_{2}$-action on the space $\mathbb{R}^{m} \otimes \mathbb{R}^{3}$ :
$$\begin{aligned}
& L_{1}+i L_{0}=i\left(2 \bar{z}^{I} \partial_{\bar{z}^{I}}+x^{I} \partial_{x^{I}}\right) \\
& L_{2}+i L_{3}=i\left(2 z^{I} \partial_{x^{I}}-x^{I} \partial_{\bar{z}^{I}}\right) .
\end{aligned}$$
On the domain of definition of $L$, the differential constraints (182) imply the relations
$$\begin{aligned}
& \left(L_{1}+i L_{0}\right)\left(L_{x^{I}}\right)=-\left(L_{2}-i L_{3}\right)\left(L_{\bar{z}^{I}}\right) \\
& \left(L_{2}+i L_{3}\right)\left(L_{x^{I}}\right)=\left(L_{1}-i L_{0}\right)\left(L_{\bar{z}^{I}}\right) .
\end{aligned}$$

Observe now, on one hand, that from the expression (185) for the Higgs field we have that
$$\begin{aligned}
\left(L_{1}+i L_{0}\right) U_{I J} & =-\frac{1}{2} \partial_{x^{I}} \partial_{x^{J}}\left[\left(L_{1}+i L_{0}\right)(L)-i L\right]-i U_{I J} \\
\left(L_{2}-i L_{3}\right) U_{I J} & =-\frac{1}{2} \partial_{z^{I}} \partial_{x^{J}}\left[\left(L_{1}+i L_{0}\right)(L)-i L\right] .
\end{aligned}$$
The first equality is simply an identity. To obtain the second one we have made use of the differential constraints of $L$ as follows:
$$\begin{aligned}
\left(L_{2}-i L_{3}\right) U_{I J}= & -\frac{1}{2}\left(L_{2}-i L_{3}\right) \underbrace{L_{x^{I} x^{J}}}_{\|}=\frac{1}{2} \partial_{z^{I}} \underbrace{\left.L_{2}-i L_{3}\right)\left(L_{\bar{z}^{J}}\right)}_{\|} \\
& -L_{z^{I} \bar{z}^{J}} \quad-\left(L_{1}+i L_{0}\right)\left(L_{x^{J}}\right) \\
= & -\frac{1}{2} \partial_{z^{I}} \partial_{x^{J}}\left[\left(L_{1}+i L_{0}\right)(L)-i L\right]
\end{aligned}$$
where in the last step we have used the commutation property $\left[L_{1}+i L_{0}, \partial_{x^{J}}\right]=-i \partial_{x^{J}}$. Note that both equalities hold in full generality, for any hyperkähler space of extended Gibbons-Hawking type. In view of these considerations the criterion of Proposition 14 can then be equivalently rephrased as follows:

Proposition 18. The collective $\mathbb{H}^{\times} / \mathbb{Z}_{2}$-action on the base of an extended Gibbons-Hawking hyperkähler space $N$ with potential $L$ can be lifted to a hyperkähler cone structure on $N$ if and only if $L$ satisfies the condition
$$L_{1}(L)+i\left(L_{0}(L)-L\right) \in \bigcap_{I, J}\left[\operatorname{ker}\left(\partial_{x^{I}} \partial_{x^{J}}\right) \cap \operatorname{ker}\left(\partial_{z^{I}} \partial_{x^{J}}\right)\right] .$$
An immediate corollary is then that a sufficient set of constraints for that to happen is given by [33]
$$L_{1}(L)=0 \quad \text { and } \quad L_{0}(L)=L .$$

On another hand, from the Legendre transform approach expression for the connection 1 -forms $A_{I}$ we obtain the following identities
$$\begin{aligned}
& \iota_{L_{1}+i L_{0}} A_{I}+U_{I J}\left(x_{1}^{J}+i x_{0}^{J}\right)=\left(L_{1}+i L_{0}\right)\left(\phi_{I}+\frac{i}{2} L_{x^{I}}\right) \\
& \iota_{L_{2}+i L_{3}} A_{I}+U_{I J}\left(x_{2}^{J}+i x_{3}^{J}\right)=\left(L_{2}+i L_{3}\right)\left(\phi_{I}+\frac{i}{2} L_{x^{I}}\right)
\end{aligned}$$
where, of course, $x_{0}^{J}=0$. We stress that these are indeed identities, with no constraints whatsoever being needed for their derivation. In the light of formula (187) it is clear then that

Lemma 19. The connection 1-forms (186) satisfy the gauge-fixing condition (108) if and only if there exist shifts $\phi_{I}$ such that
$$u_{I} \in \operatorname{ker}\left(L_{1}+i L_{0}\right) \cap \operatorname{ker}\left(L_{2}+i L_{3}\right)$$
for all values of $I$.
4.2.2. Let us assume now that the function $L$ satisfies the linear differential constraints (193). One can then check that with these conditions its Legendre transform is both invariant at collective rotations and scales with weight 1 under the action of $L_{0}$. That is to say, the Legendre transform gives us in this case not just a Kähler potential, but in fact a hyperkähler potential. Accordingly, we write
$$\kappa=U .$$
As we have discussed at the end of §3.2.1, when the gauge-fixing condition (108) holds, the collective $\mathbb{H}^{\times} / \mathbb{Z}_{2}$-action on $S$ lifts trivially to the hyperkähler cone as its standard quaternionic action. In our case it can be shown that its (complexified) generators assume in holomorphic coordinates the form
$$\begin{aligned}
& L_{1}+i L_{0}=2 i \bar{z}^{I} \frac{\partial}{\partial \bar{z}^{I}} \\
& L_{2}+i L_{3}=\frac{\partial U}{\partial \bar{u}_{I}} \frac{\partial}{\partial \bar{z}^{I}}-\frac{\partial U}{\partial \bar{z}^{I}} \frac{\partial}{\partial \bar{u}_{I}} .
\end{aligned}$$
4.2.3. So far, what we have done was simply to rephrase the description of a hyperkähler cone structure on an extended Gibbons-Hawking space in the language of the Legendre transform approach. Ultimately, though, we are interested in determining the quaternionic Kähler metric on the base of the hyperkähler cone. To achieve that, we combine the results of this and the previous section into the following procedure:
\begin{itemize}
\item[1.] Given a function $L$ satisfying the differential conditions (182), usually although not necessarily in the form of a contour integral, one should first test whether it satisfies also the conditions of Proposition 18. In case it does, one is then guaranteed that the ensuing metric through the Legendre transform construction will be of hyperkähler cone type.
\item[2.] The second partial derivatives of $L$ with respect to the $x^{I}$-variables give the Higgs field $U_{I J}$ via the formula (185).
\item[3.] More challengingly, one must also solve the differential conditions of Lemma 19 to find shift functions $\phi_{I}$ for which the connection 1-forms $A_{I}$ satisfy the gaugefixing condition (108). As we shall see in the next example, depending on the particularities of the case, additional symmetry considerations might need to be taken into account as well.
\item[4.] Once the Higgs field and the appropriately gauge-fixed connection 1-forms on the hyperkähler cone are determined, one should then substitute in them the change of variables (117) for some choice of restricted configuration $\vec{\rho}^{I}$. The outcomes should be amenable to the form (137) and (140), respectively, from which one can then read off the reduced Higgs field $\mathscr{U}_{I J}$ and induced connection 1-forms $\mathscr{A}_{I}$. This is effectively a quotienting procedure which takes us from the hyperkähler cone down to its base.
\item[5.] The Ansatz of Theorem 17, or any one of the equivalent Ansätze listed in Table 2, gives us eventually the quaternionic Kähler metric and structure on the base.
\end{itemize}

\section*{5. An example: the local c-map}

As an application of this procedure and, more generally, of the ideas that we have developed in this article, we present an explicit construction of a quaternionic Kähler
metric known as the Ferrara-Sabharwal metric [23]. This metric emerged in physics from the construction known as the local c-map (or, sometimes, the projective or supergravity $c$-map) [15], a map derived from a duality of the moduli spaces of type IIA and type IIB string theories, which yields a quaternionic Kähler manifold of real dimension $4 n$ for each projective special Kähler manifold of real dimension $2 n-2$. The approach we pursue was initiated by Roček, Vafa and Vandoren in [43, 44]. The idea is as follows: the $4 n$ -dimensional quaternionic Kähler manifold has an associated $4 n+4$-dimensional Swann bundle which, in turn, as a hyperkähler space, has a $4 n+6$-dimensional twistor space. The twistor space, these authors posit, is characterized as a complex space by a certain holomorphic gluing function (in physics terms, this is related to a projective superspace lagrangian density). The challenge is then to extract the metric from this holomorphic function by coming down first two real dimensions, to describe the geometry of the Swann bundle, and then another four real dimensions, to the quaternionic Kähler base. Here we fill in a number of critical details in the arguments of [43, 44], which were further developed in [40], and use our previous considerations to perform what these papers refer to as a superconformal quotient - i.e. the descent from the hyperkähler cone to the quaternionic Kähler base-explicitly as well as equivariantly.
5.0.1. In close analogy with the Legendre transform construction of the rigid c-map metric (also known as the affine c-map or semi-flat metric), the $L$-potential of the Swann bundle $N_{c}$ over the quaternionic Kähler image of the local c-map was shown in [43, 44] to be given by the following contour integral:
$$L=\frac{1}{2 \pi} \oint \frac{d \zeta}{\zeta}\left(\frac{F(\eta(\zeta))}{\eta^{0}(\zeta)}-\frac{\bar{F}(\eta(\zeta))}{\eta^{0}(\zeta)}\right)$$
where
\begin{itemize}
\item[-] the $\eta^{I}(\zeta)$ variables are so-called tropical components of sections of an $\mathcal{O}(2)$ line bundle over the twistor space of the Swann bundle, that is,
$$\eta^{I}(\zeta)=\frac{z^{I}}{\zeta}+x^{I}-\bar{z}^{I} \zeta ;$$
\item[-] $F(\eta(\zeta)) \equiv F\left(\eta^{1}(\zeta), \ldots, \eta^{n}(\zeta)\right)$ is a holomorphic function called prepotential, assumed to be homogeneous of degree two in its variables;
\item[-] the integration contour wraps around the two roots of $\eta^{0}(\zeta)$ : anti-clockwise around $\zeta_{+}^{0}$ for the first term, and clockwise around $\zeta_{-}^{0}$ for the second one, where
$$\zeta_{ \pm}^{0}=\frac{x^{0} \mp r^{0}}{2 \bar{z}^{0}}=-\frac{2 z^{0}}{x^{0} \pm r^{0}},$$
with $r^{0}=\left|\vec{x}^{0}\right|$, correspond to antipodally opposite points on the twistor Riemann sphere.
\end{itemize}

The integrand can be understood as a twistor space holomorphic symplectic gluing function [32]. Its holomorphic dependence on $\mathcal{O}(2)$ sections guarantees that the contour integral satisfies automatically the generalized Laplace equations (182). Moreover, the specific manner in which it depends on these-namely, the fact that it only depends on $\zeta$ implicitly through the variables $\eta^{I}(\zeta)$ and the fact that it scales with weight 1 at a scaling of the $\eta^{I}(\zeta)$ 's-implies that the integral satisfies the two constraints (193), and it is thus indeed, as claimed, the $L$-potential of a hyperkähler cone.

The contour integral can be computed explicitly with Cauchy's residue theorem. Using the homogeneity property of the prepotential we obtain
$$L=2 r^{0} \operatorname{Im} F(\chi)$$
where, by definition,
$$\chi^{A}=\frac{\eta^{A}\left(\zeta_{+}^{0}\right)}{r^{0}} \quad \text { and } \quad \bar{\chi}^{A}=\frac{\eta^{A}\left(\zeta_{-}^{0}\right)}{r^{0}} .$$
Note that the twistor sections $\zeta \mapsto \eta^{A}(\zeta)$ take antipodally conjugated variables to complex conjugated ones. Here and throughout this section we use the following index notation conventions:

\begin{tabular}[t]{|l|l|}
\hline Indices & Range \\
\hline $I, J, \ldots$ & $0, \ldots, n$ \\
\hline $A, B, \ldots$ & $1, \ldots, n$ \\
\hline
\end{tabular}
5.0.2. Before we continue, we pause for a moment to list for future reference a number of properties that these variables satisfy. First, direct evaluation gives us the expression
$$\chi^{A}=\frac{x^{A}}{r^{0}}-\frac{x^{0}}{r^{0}} \operatorname{Re} \frac{z^{A}}{z^{0}}-i \operatorname{Im} \frac{z^{A}}{z^{0}} .$$
This can be equivalently recast in the vectorial form
$$\chi^{A}=\frac{\left(\vec{x}^{0} \times \vec{x}^{A}\right) \cdot\left(\vec{x}^{0} \times \mathbf{i}\right)-i\left|\vec{x}^{0}\right| \vec{x}^{0} \cdot\left(\vec{x}^{A} \times \mathbf{i}\right)}{\left|\vec{x}^{0}\right|\left|\vec{x}^{0} \times \mathbf{i}\right|^{2}} .$$
Proceeding in the same vein, we can then show that the following two properties hold:
$$\begin{aligned}
\chi^{A} \bar{\chi}^{B} & =\frac{\left(\vec{x}^{0} \times \vec{x}^{A}\right) \cdot\left(\vec{x}^{0} \times \vec{x}^{B}\right)-i\left|\vec{x}^{0}\right| \vec{x}^{0} \cdot\left(\vec{x}^{A} \times \vec{x}^{B}\right)}{\left|\vec{x}^{0} \times \mathbf{i}\right|^{2}} \\
\frac{\chi^{A}}{\chi^{B}} & =\frac{\left(\vec{x}^{0} \times \vec{x}^{A}\right) \cdot\left(\vec{x}^{0} \times \vec{x}^{B}\right)-i\left|\vec{x}^{0}\right| \vec{x}^{0} \cdot\left(\vec{x}^{A} \times \vec{x}^{B}\right)}{\left|\vec{x}^{0} \times \vec{x}^{B}\right|^{2}} .
\end{aligned}$$
The last one, in particular, makes it clear that ratios of $\chi^{A}$ 's are invariant under collective transformations and thus descend naturally to functions on the base of the hyperkähler cone.

In order to present the next property in a concise manner it will be convenient to introduce a number of temporarily notations. Thus, if we denote the parameters of the $\mathcal{O}(2)$ -bundle sections by $\eta_{+1}^{I}=z^{I}, \eta_{0}^{I}=x^{I}, \eta_{-1}^{I}=-\bar{z}^{I}$ such that we have $\eta^{I}(\zeta)=\sum_{m=-1}^{1} \eta_{m}^{I} \zeta^{-m}$ (this is sometimes called the complex spherical basis), then in terms of these the various derivatives of $\chi^{A}$ can be summarized in the formula
$$d \chi^{A}=\frac{1}{r^{0}} \sum_{m=-1}^{1}\left(\zeta_{+}^{0}\right)^{-m}\left[d \eta_{m}^{A}+\left(m \chi^{A}-\frac{\vec{x}^{0} \cdot \vec{x}^{A}}{\vec{x}^{0} \cdot \vec{x}^{0}}\right) d \eta_{m}^{0}\right] .$$

In view of the imminent application of Lemma 19 it would be useful to have a list of elementary functions belonging to the intersection of kernels from the condition (195). And indeed, such a list exists and reads as follows:
$$\left\{\psi_{0}, \psi_{A}, \frac{z^{A}}{z^{0}}, \frac{x^{0}+r^{0}}{2 r^{0}} \chi^{A}, \frac{x^{0}-r^{0}}{2 r^{0}} \bar{\chi}^{A}\right\} \subset \operatorname{ker}\left(L_{1}+i L_{0}\right) \cap \operatorname{ker}\left(L_{2}+i L_{3}\right) .$$

For the first three elements membership in the list follows immediately from a cursory survey of the formulas (188). For the last two, however, this is a little less obvious. One can verify it directly, which is rather tedious, or by observing successively that
$$\left(L_{1}+i L_{0}\right)\left(\zeta_{ \pm}^{0}\right)=-i \zeta_{ \pm}^{0} \quad\left(L_{2}+i L_{3}\right)\left(\zeta_{ \pm}^{0}\right)=i\left(\zeta_{ \pm}^{0}\right)^{2}$$
and, using these facts in the definitions (200), that
$$\begin{array}{ll}
\left(L_{1}+i L_{0}\right)\left(\chi^{A}\right)=0 & \left(L_{2}+i L_{3}\right)\left(\chi^{A}\right)=i \zeta_{+}^{0} \chi^{A} \\
\left(L_{1}+i L_{0}\right)\left(\bar{\chi}^{A}\right)=0 & \left(L_{2}+i L_{3}\right)\left(\bar{\chi}^{A}\right)=i \zeta_{-}^{0} \bar{\chi}^{A} .
\end{array}$$
The remaining gap in the verification can then be bridged by a very simple calculation.
Lastly, let us also make a note of the following identity:
$$\frac{z^{A}}{z^{0}}+\frac{x^{0}+r^{0}}{2 r^{0}} \chi^{A}+\frac{x^{0}-r^{0}}{2 r^{0}} \bar{\chi}^{A}=\frac{\vec{x}^{0} \cdot \vec{x}^{A}}{\vec{x}^{0} \cdot \vec{x}^{0}} .$$
The manifestly invariant expression on the right-hand side, the same one which shows up in the differentiation formula (206), will play an important role in the considerations to come.
5.0.3. In order to compute the Legendre transform of $L$ one needs to compute first its partial derivatives with respect to the variables $x^{I}$. The components with $m=0$ of the differentiation formula (206) give us promptly, on one hand,
$$L_{x^{A}}=2 \operatorname{Im} F_{A}(\chi)$$
and on the other,
$$\left(\vec{x}^{0} \cdot \vec{x}^{I}\right) L_{x^{I}}=x^{0} L .$$
This last relation can be used to determine $L_{x^{0}}$. With the help of these formulas one can then show that the Legendre transform of $L$ yields the hyperkähler potential
$$U=-\frac{4\left|z^{0}\right|^{2}}{r^{0}} \operatorname{Im}\left[\bar{\chi}^{A} F_{A}(\chi)\right] .$$
In addition, by using the homogeneity property of the prepotential to replace $F_{A}(\chi)$ with $F_{A B}(\chi) \chi^{B}$, and then the formula (204), we get also the alternative expression
$$U=-\frac{\left(\vec{x}^{0} \times \vec{x}^{A}\right) \cdot\left(\vec{x}^{0} \times \vec{x}^{B}\right)}{\left|\vec{x}^{0}\right|^{3}} \operatorname{Im} F_{A B}$$
where it is understood that $F_{A B}$ refers to $F_{A B}(\chi)$.
One calls dualization the result of replacing the prepotential function $F$ in the definition of $L$ with (minus) its Legendre transform. In the ensuing formulas, this operation results in the replacement of $F(\chi)$ with $F(\chi)-\chi^{A} F_{A}(\chi)$, of $\chi^{A}$ with $F_{A}(\chi)$, and of the latter with $-\chi^{A}$; similar statements hold also for the complex conjugated quantities. On the other hand, the zero-indexed variables such as $x^{0}, z^{0}, \bar{z}^{0}$ are inert under dualization.

The first expression above for the hyperkähler potential is the one best suited for an analysis of its dualization properties. From it, one can see immediately that the hyperkähler potential is self-dual. This strongly suggests that one might be able to lift dualization to a symmetry of the metric, which, we shall see, will indeed be the case.

The second expression of the hyperkähler potential brings instead to the fore its collective transformation properties. Note that since the function $F_{A B}(\chi)$ is homogeneous of degree zero, and since ratios of $\chi^{A}$ 's are invariant under collective transformations, it follows that
so is the Hessian $F_{A B}(\chi)$. It is then evident that the hyperkähler potential is, as required, invariant under collective rotations and scales with weight 1 under the action of $L_{0}$.
5.0.4. Following [40], let us consider on $N_{c}$ the vector fields
$$\begin{aligned}
& Q^{A}=\frac{\partial}{\partial u_{A}}+\text { c.c. } \\
& P_{A}=z^{0} \frac{\partial}{\partial z^{A}}-u_{A} \frac{\partial}{\partial u_{0}}+\text { c.c. } \\
& W=2 z^{0} \frac{\partial}{\partial z_{0}}+z^{A} \frac{\partial}{\partial z^{A}}-2 u_{0} \frac{\partial}{\partial u_{0}}-u_{A} \frac{\partial}{\partial u_{A}}+\text { c.c. } .
\end{aligned}$$
where c.c. means the complex conjugate of the preceding expression. They are manifestly real-holomorphic with respect to the hyperkähler complex structure $I_{1}$ and, moreover, satisfy the following graded Heisenberg algebra:
$$\begin{gathered}
{\left[P_{A}, Q^{B}\right]=\delta_{A}^{B} I} \\
{\left[P_{A}, P_{B}\right]=0 \quad\left[Q^{A}, Q^{B}\right]=0} \\
{\left[W, P_{A}\right]=P_{A} \quad\left[W, Q^{A}\right]=Q^{A} \quad[W, I]=2 I .}
\end{gathered}$$

Observe now that, out of these, the vector fields $Q^{A}$ and $I$ are entirely vertical with respect to the $\mathbb{R}^{n+1}$-fibration structure. On the other hand, the vector fields $P_{A}$ and $W$ have non-trivial horizontal components given by the horizontal lifts of the vector fields
$$\mathcal{P}_{A}=\vec{x}^{0} \cdot \frac{\partial}{\partial \vec{x}^{A}} \quad \text { and } \quad \mathcal{W}=2 \vec{x}^{0} \cdot \frac{\partial}{\partial \vec{x}^{0}}+\vec{x}^{A} \cdot \frac{\partial}{\partial \vec{x}^{A}}$$
living on the base of the $\mathbb{R}^{n+1}$-fibration. Note incidentally that by resorting to the contourintegral representation of $L$ one can easily see that we have
$$\mathcal{P}_{A}(L)=0 \quad \text { and } \quad \mathcal{W}(L)=0 \text {. }$$
Furthermore, from the definition of the $\chi^{A}$-variables we get successively:
$$\begin{aligned}
& P_{A}\left(\chi^{B}\right)=\mathcal{P}_{A}\left(\chi^{B}\right)=\frac{\mathcal{P}_{A}\left(\eta^{B}\left(\zeta_{+}^{0}\right)\right)}{r^{0}}=\frac{\delta_{A}^{B} \eta^{0}\left(\zeta_{+}^{0}\right)}{r^{0}}=0 \\
& W\left(\chi^{A}\right)=\mathcal{W}\left(\chi^{A}\right)=-\chi^{A} .
\end{aligned}$$
Corresponding statements hold for the complex conjugated variables as well.
In light of these facts one can then readily infer using the expression (213) for the hyperkähler potential that this is preserved by all of the generators of the graded Heisenberg algebra:
$$Q^{A}(U)=0 \quad I(U)=0 \quad P_{A}(U)=0 \quad W(U)=0 .$$

Let us recall now the following general result:
Lemma 20. A real-holomorphic vector field on a Kähler manifold preserves the Kähler form if and only if it preserves locally Kähler potentials up to pluriharmonic functions.

A hyperkähler manifold can be viewed as a Kähler manifold with respect to any one of its hyperkähler complex structures. In our case, each one of the vector fields $Q^{A}, P_{A}, I$ and $W$ satisfies the conditions of this Lemma when one regards the hyperkähler space $N_{c}$ as a Kähler space with respect to the complex structure $I_{1}$, with Kähler form $\Omega_{1}$. Indeed, they are real-holomorphic with respect to $I_{1}$ and, as we have shown, preserve the hyperkähler
potential, which is in particular a Kähler potential for $\Omega_{1}$. By the Lemma, they all must then preserve as well the Kähler form $\Omega_{1}$. Moreover, a straightforward check using their defining formulas shows that they preserve also both the transversal symplectic form (184) and its complex conjugate. We are then entitled to conclude that $Q^{A}, P_{A}, I$ and $W$ are all tri-Hamiltonian vector fields.

What is more, they also commute with the generators of the standard quaternionic action on the hyperkähler cone. This can be seen using the holomorphic coordinate expressions (215) and (197), while taking also into account, once again, the invariance properties (220) of the hyperkähler potential function $U$. By Theorem 13 they descend therefore to the quaternionic Kähler base.

These considerations suggest that in holomorphic coordinates the dualization map takes the form
$$\begin{array}{ll}
\tilde{u}^{A}=\frac{z^{A}}{z^{0}} & \tilde{z}_{A}=-z^{0} u_{A} \\
\tilde{u}_{0}=u_{0}+\frac{z^{A}}{z^{0}} u_{A} & \tilde{z}^{0}=z^{0} .
\end{array}$$
Indeed, this represents a holomorphic symplectomorphism with respect to the complex symplectic form $\Omega_{+}$, which preserves moreover the graded Heisenberg algebra by mapping $Q^{A}$ to $P_{A}$ and the latter to $-Q^{A}$ while keeping $I$ and $W$ unchanged. Notice also that the double dual of a non-zero-indexed coordinate returns minus that coordinate, whereas the double dual of a zero-indexed one returns it trivially, without any sign change.
5.0.5. In order to be able to compute explicitly the connection 1-forms $A_{I}$ we need to choose a set of shift functions $\phi_{I}$ for which the conditions of Lemma 19 are satisfied. This is perhaps the most difficult step in the construction of a hyperkähler cone in the Legendre transform approach. Fortunately, in our case we can use the duality symmetry as a guide. In other words, rather than solve these conditions directly, in what follows we shall exploit duality to find a convenient set of such functions, and then verify a posteriori that they provide indeed a solution to the required conditions.

Note to begin with, that in view of the expression (211), the Legendre transform construction formula (187) takes in this case for non-zero values of the index the form
$$u_{A}=\psi_{A}+\phi_{A}+i \operatorname{Im} F_{A}(\chi) .$$
Dualization then yields
$$\tilde{\psi}^{A}+\tilde{\phi}^{A}=\operatorname{Re} \frac{z^{A}}{z^{0}}=\frac{\vec{x}^{0} \cdot \vec{x}^{A}}{\vec{x}^{0} \cdot \vec{x}^{0}}-\frac{x^{0}}{r^{0}} \operatorname{Re} \chi^{A}$$
where the second equality is the real part of the identity (210). This shows that if we take
$$\phi_{A}=\frac{x^{0}}{r^{0}} \operatorname{Re} F_{A}(\chi) \quad \text { such that } \quad \tilde{\phi}^{A}=-\frac{x^{0}}{r^{0}} \operatorname{Re} \chi^{A}$$
then we get [40]
$$\tilde{\psi}^{A}=\frac{\vec{x}^{0} \cdot \vec{x}^{A}}{\vec{x}^{0} \cdot \vec{x}^{0}}$$
which is manifestly invariant under collective transformations, in agreement with the expectation that dualization should commute with the hyperkähler cone quaternionic action.

For this choice the initial formula becomes
$$u_{A}=\psi_{A}+\frac{x^{0}+r^{0}}{2 r^{0}} F_{A}(\chi)+\frac{x^{0}-r^{0}}{2 r^{0}} \bar{F}_{A}(\bar{\chi})$$
that is, precisely the dual of the identity (210). Since the functions $F_{A}$ are holomorphic and homogeneous of degree 1, then in light of the list (207) it is clear that these $u_{A}$ 's satisfy the condition of Lemma 19. This check validates the above choice of shift functions $\phi_{A}$.

On another hand, let us observe that the relation (212) can be equivalently stated as
$$\operatorname{Im}\left(u_{0}+\tilde{\psi}^{A} u_{A}\right)=\frac{x^{0}}{2\left(r^{0}\right)^{2}} L .$$
By noticing then that the function $L$ is anti-self-dual, i.e. that $\tilde{L}=-L$, we can infer from this that $\operatorname{Im}\left(u_{0}+\tilde{u}_{0}+\tilde{\psi}^{A} u_{A}-\psi_{A} \tilde{u}^{A}\right)=0$. This suggests that we choose a shift $\phi_{0}$ by setting
$$\psi_{0}=\frac{1}{2}\left(u_{0}+\tilde{u}_{0}+\tilde{\psi}^{A} u_{A}-\psi_{A} \tilde{u}^{A}\right)$$
which is thus real and, moreover, explicitly self-dual. This is the same as having [40]
$$u_{0}=\psi_{0}+\frac{1}{2}\left(\psi_{A} \tilde{u}^{A}-\tilde{\psi}^{A} u_{A}\right)-\frac{1}{2} u_{A} \tilde{u}^{A} .$$
Each elementary component of the expression on the right-hand side belongs to the set $\operatorname{ker}\left(L_{1}+i L_{0}\right) \cap \operatorname{ker}\left(L_{2}+i L_{3}\right)$, which then by way of the Leibniz rule implies that the same is true for $u_{0}$. From this formula one can read off the shift $\phi_{0}$, which can then be shown to satisfy
$$\phi_{0}+\tilde{\psi}^{A} \phi_{A}=\frac{1}{2}\left(\frac{x^{0}}{r^{0}}\right)^{2} \operatorname{Re} \chi^{A} \operatorname{Re} F_{A}(\chi)-\frac{1}{2} \operatorname{Im} \chi^{A} \operatorname{Im} F_{A}(\chi)-\frac{1}{2} \tilde{\psi}^{A} \psi_{A} .$$
A rather unusual feature of this choice of shift, imposed on us by the requirements of manifest duality, is that it has an explicit linear dependence on the $\psi_{A}$-variables.
5.0.6. So far we have used two coordinate systems on $N_{c}$ : the extended Gibbons-Hawking coordinates $\psi_{I}$ and $\vec{x}^{I}$ (with a closely related complexified variant given by $\psi_{I}, x^{I}, z^{I}, \bar{z}^{I}$ ), and the Legendre transform-related holomorphic coordinates $u_{I}$ and $z^{I}$. The first system is adapted to the $\mathbb{R}^{n+1}$-fibration structure. The second one is adapted to the transversal complex symplectic structure which is holomorphic with respect to $I_{1}$. For the current construction, however, it is useful to introduce yet a third system of coordinates, adapted to its duality symmetry this time, given by
$$\left\{\psi_{0}, x^{0}, z^{0}, \bar{z}^{0}, \psi_{A}, \tilde{\psi}^{A}, \chi^{A}, \bar{\chi}^{A}\right\} .$$

The generators of the Heisenberg algebra take in these coordinates the form
$$\begin{gathered}
Q^{A}=\frac{\partial}{\partial \psi_{A}}+\frac{1}{2} \tilde{\psi}^{A} \frac{\partial}{\partial \psi_{0}} \quad P_{A}=\frac{\partial}{\partial \tilde{\psi}^{A}}-\frac{1}{2} \psi_{A} \frac{\partial}{\partial \psi_{0}} \\
I=\frac{\partial}{\partial \psi_{0}}
\end{gathered}$$
and, moreover, the grading generator $W$ scales the non-zero-indexed coordinates with weight -1 and the zero-indexed ones with weight 2, except for $\psi_{0}$, which it scales with weight -2.

The advantage of this coordinate system becomes apparent when one tries to compute the connection 1-forms $A_{I}$. For the shift choices (224) and (230), from the Legendre transform formula (186) we obtain following a rather laborious computation the relatively simple expressions
$$\begin{aligned}
& A_{A}=\operatorname{Re} F_{A B} d \tilde{\psi}^{B}-\operatorname{Im} F_{A B}\left[\operatorname{Im} \chi^{B} d x_{\diamond}^{0}+4 \operatorname{Re} \chi^{B} \operatorname{Im}\left(\bar{z}_{\diamond}^{0} d z_{\diamond}^{0}\right)\right] \\
& A_{0}+\tilde{\psi}^{A} A_{A}=2 \operatorname{Im} F_{A B}\left[\left|z_{\diamond}^{0}\right|^{2} \operatorname{Im}\left(\bar{\chi}^{A} d \chi^{B}\right)+\bar{\chi}^{A} \chi^{B} x_{\diamond}^{0} \operatorname{Im}\left(\bar{z}_{\diamond}^{0} d z_{\diamond}^{0}\right)\right]-\frac{1}{2} d\left(\tilde{\psi}^{A} \psi_{A}\right)
\end{aligned}$$
where, for simplicity, we have used the notations $x_{\diamond}^{0}=x^{0} / r^{0}$ and $z_{\diamond}^{0}=z^{0} / r^{0}$.
5.0.7. The Higgs field, on the other hand, can be computed with significantly less effort. By taking derivatives with respect to $x^{A}$ and $x^{0}$ of the equation (212) we obtain, respectively,
$$\begin{aligned}
& \left(\vec{x}^{0} \cdot \vec{x}^{I}\right) L_{x^{I} x^{A}}=0 \\
& \left(\vec{x}^{0} \cdot \vec{x}^{I}\right) L_{x^{I} x^{0}}=U
\end{aligned}$$
(recall the index notation convention (201)!). Moreover, from the preceding expression for the derivative $L_{x^{A}}$ we can easily compute the second derivative $L_{x^{A} x^{B}}$. Together with the relations above this gives us
$$U_{I J}=-\frac{1}{r^{0}}\left(\begin{array}{c|c}
R+\tilde{\psi}^{C} \operatorname{Im} F_{C D} \tilde{\psi}^{D} & -\tilde{\psi}^{C} \operatorname{Im} F_{C B} \\
\hline-\operatorname{Im} F_{A D} \tilde{\psi}^{D} & \operatorname{Im} F_{A B}
\end{array}\right)$$
where, by definition,
$$R=\frac{U}{2 r^{0}} .$$
5.0.8. We are now ready to perform the reduction and descend from the hyperkähler cone down to its quaternionic Kähler base. In practice, this step consists of substituting into the formulas for the Higgs field $U_{I J}$ and connection 1-forms $A_{I}$ the change of variables (117) for some choice of restricted configuration with position vectors $\vec{\rho}^{I}$, and then reading off from the result the reduced Higgs field $\mathscr{U}_{I J}$ and reduced connection 1-forms $\mathscr{A}_{I}$.

In the case of the Higgs field, this is rather straightforward. Recall, on one hand, that the variables $\tilde{\psi}^{A}$ and, as argued before, the functions $F_{A B}(\chi)$ are invariant at collective transformations, and hence at the particular collective transformation represented by the equation (117). On another hand, from the multiplicative property of the quaternionic norm we have $r^{0}=\left|\vec{x}^{0}\right|=|q|^{2}\left|\vec{\rho}^{0}\right|$, and from the representation (214) for the hyperkähler potential, $U=|q|^{2} \mathscr{U}$. These last two properties entail in particular that $R$ is also invariant at collective transformations, and so, like $\tilde{\psi}^{A}$ and $F_{A B}(\chi)$, descends naturally on the base of the hyperkähler cone. It is obvious then that if we substitute into the above Higgs field matrix the relation (117) we find as expected from general arguments that this is of the form (137), with the reduced Higgs field matrix given by
$$\mathscr{U}_{I J}=-\frac{1}{\left|\vec{\rho}^{0}\right|}\left(\begin{array}{c|c}
R+\tilde{\psi} N \tilde{\psi} & -(\tilde{\psi} N)_{B} \\
\hline-(N \tilde{\psi})_{A} & N_{A B}
\end{array}\right) .$$
Aside from the overall factor, this matrix is precisely the same as the one in the equation (235); however, here we have introduced the shorthand notations $N_{A B}=\operatorname{Im} F_{A B}$,
$(N \tilde{\psi})_{A}=N_{A B} \tilde{\psi}^{B}$, a.s.o. Let us also record here for subsequent use that the inverse of this matrix is
$$\mathscr{U}^{I J}=-\frac{\left|\vec{\rho}^{0}\right|}{R}\left(\begin{array}{c|c}
1 & \tilde{\psi}^{B} \\
\hline \tilde{\psi}^{A} & \tilde{\psi}^{A} \tilde{\psi}^{B}+R N^{A B}
\end{array}\right)$$
with $N^{A B}$ representing the matrix inverse of $N_{A B}$.
In the case of the connection 1-forms $A_{I}$, if we consider a restricted configuration with
$$\vec{\rho}^{0}=\text { constant }$$
then the change of variables (117) yields, after a rather more strenuous calculation, a result of the form (140), with the reduced connection 1-forms given by
$$\begin{aligned}
& \mathscr{A}_{A}=\operatorname{Re} F_{A B} d \tilde{\psi}^{B} \\
& \mathscr{A}_{0}+\tilde{\psi}^{A} \mathscr{A}_{A}=\frac{1}{2} \operatorname{Im} F_{A B} \frac{\vec{\rho}^{0} \cdot\left(\vec{\rho}^{A} \times d \vec{\rho}^{B}\right)}{\left(\rho^{0}\right)^{3}}-\frac{1}{2} d\left(\tilde{\psi}^{A} \psi_{A}\right) .
\end{aligned}$$
5.0.9. Let us specialize now further to the particular choice of restricted configuration considered in (116). For this we then have, via the formulas (225) and (205),
$$\tilde{\psi}^{A}=\rho_{1}^{A} \quad \text { and } \quad \frac{\chi^{A}}{\chi^{B}}=\frac{\rho_{2}^{A}+i \rho_{3}^{A}}{\rho_{2}^{B}+i \rho_{3}^{B}}$$
suggesting we should define also the variables
$$\mathcal{X}^{A}=\frac{1}{2}\left(\rho_{2}^{A}+i \rho_{3}^{A}\right) .$$
These are all complex, with the exception of $\mathcal{X}^{1}$, which is real and positive. The reality condition is important for the coordinate count: in what follows we will coordinatize the quaternionic Kähler space by means of the variables $\psi_{0}, \psi_{A}, \tilde{\psi}^{A}$ and $\mathcal{X}^{A}$, which would not be possible if the total number of their real components were not equal to $4 n$.

Note that since the function $F_{A B}$ is homogeneous of degree zero, one can argue that $F_{A B}(\chi)=F_{A B}(\mathcal{X})$, which then allows us to pass from the variables $\chi^{A}$ to the $\mathcal{X}^{A}$ ones. With obvious notations, the hyperkähler potential formula (214) gives us in this case
$$R=-2(\overline{\mathcal{X}} N \mathcal{X})=-2 \operatorname{Im}\left[\overline{\mathcal{X}}^{A} F_{A}(\mathcal{X})\right] .$$
This satisfies, incidentally, the differential identity
$$\left(\theta_{0}=\right) \frac{d R}{2 R}=\frac{\operatorname{Im}(\overline{\mathcal{X}} N d \mathcal{X})}{(\overline{\mathcal{X}} N \mathcal{X})}$$
a consequence of the holomorphicity property of the prepotential.
5.0.10. Knowledge of the reduced Higgs field and connection 1-forms allows us to finally compute the quaternionic Kähler metric explicitly. To this end, observe first that from the expression (151) for the $S O(3)$ connection 1-forms and with the above definitions we obtain in this case
$$\begin{aligned}
\theta_{1} & =-\frac{1}{2 R}\left[\alpha+\operatorname{Re}\left(\overline{\mathcal{X}}^{A} d F_{A}(\mathcal{X})-F_{A}(\mathcal{X}) d \overline{\mathcal{X}}^{A}\right)\right] \\
\frac{1}{2}\left(\theta_{2}+i \theta_{3}\right) & =-\frac{1}{2 R}\left[\mathcal{X}^{A} d \psi_{A}+F_{A}(\mathcal{X}) d \tilde{\psi}^{A}\right]
\end{aligned}$$
where we have used the notation
$$\alpha=d \psi_{0}+\frac{1}{2}\left(\tilde{\psi}^{A} d \psi_{A}-\psi_{A} d \tilde{\psi}^{A}\right) .$$
The metric itself can be most conveniently worked out from the version (148) of the metric Ansatz, in which one can make use of the above formulas for the $S O(3)$ connection 1-forms. In the end, using among other things the identity (244), we arrive as predicted in [43, 44] at the Ferrara-Sabharwal metric [23]
$$2 s g=g_{P S K}-\left(\frac{d R}{2 R}\right)^{2}-\frac{g_{T}}{R}-\frac{\alpha^{2}}{R^{2}}$$
where
$$g_{P S K}=\frac{(\overline{\mathcal{X}} N \mathcal{X})(d \overline{\mathcal{X}} N d \mathcal{X})-(d \overline{\mathcal{X}} N \mathcal{X})(\overline{\mathcal{X}} N d \mathcal{X})}{(\overline{\mathcal{X}} N \mathcal{X})^{2}}$$
is the so-called projective special Kähler metric and
$$g_{T}=\frac{1}{2}(\operatorname{Im} \tau)^{-1 A B}\left(d \psi_{A}+\tau_{A C} d \tilde{\psi}^{C}\right)\left(d \psi_{B}+\bar{\tau}_{B D} d \tilde{\psi}^{D}\right)$$
is a complex $n$-torus metric with period matrix [21]
$$\tau_{A B}=F_{A B}(\mathcal{X})-2 i \frac{(N \overline{\mathcal{X}})_{A}(N \overline{\mathcal{X}})_{B}}{(\overline{\mathcal{X}} N \overline{\mathcal{X}})} .$$
Under a duality transformation this undergoes the modular transformation $\tau_{A B} \mapsto-\left(\tau^{-1}\right)^{A B}$ and, furthermore, we have
$$(\operatorname{Im} \tau)^{-1 A B}=N^{A B}-\frac{\overline{\mathcal{X}}^{A} \mathcal{X}^{B}+\mathcal{X}^{A} \overline{\mathcal{X}}^{B}}{(\overline{\mathcal{X}} N \mathcal{X})} .$$
5.0.11. To make the junction with the usual formulation found in the literature we need to perform one final change of coordinates. Letting
$$Z^{A}=\frac{\mathcal{X}^{A}}{\mathcal{X}^{1}}$$
we replace the subset of coordinates $\left\{\mathcal{X}^{A}\right\}_{A=1, \ldots, n}$ with the complex inhomogeneous coordinates $\left\{Z^{A^{\prime}}\right\}_{A^{\prime}=2, \ldots, n}$ plus $R$. The projective special Kähler metric $g_{P S K}$ can be understood then as the Kähler metric corresponding to the Kähler potential
$$\mathscr{K}=\ln \operatorname{Im}\left[\bar{Z}^{A} F_{A}(Z)\right]=\ln (\bar{Z} N Z)$$
with $Z^{A^{\prime}}$ as complex holomorphic coordinates. (A more geometric definition of projective special Kähler metrics can be found in [24, 3].) The formulas are straightforward to reexpress in the new coordinates due to their homogeneity properties. We leave the details to the reader as an exercise.

The $4 n$-dimensional Ferrara-Sabharwal metric has $2 n+2$ isometries descending from the corresponding tri-Hamiltonian isometries on the hyperkähler cone and satisfying the same graded Heisenberg algebra (216). In the above inhomogeneous coordinate frame their generating vector fields take the form [22]
$$\begin{gathered}
\mathscr{Q}^{A}=\frac{\partial}{\partial \psi_{A}}+\frac{1}{2} \tilde{\psi}^{A} \frac{\partial}{\partial \psi_{0}} \quad \mathscr{P}_{A}=\frac{\partial}{\partial \tilde{\psi}^{A}}-\frac{1}{2} \psi_{A} \frac{\partial}{\partial \psi_{0}} \\
\mathscr{I}=\frac{\partial}{\partial \psi_{0}}
\end{gathered}$$
$$\mathscr{W}=-\psi_{A} \frac{\partial}{\partial \psi_{A}}-\tilde{\psi}^{A} \frac{\partial}{\partial \tilde{\psi}^{A}}-2 \psi_{0} \frac{\partial}{\partial \psi_{0}}-2 R \frac{\partial}{\partial R} .$$

Finally, let us also mention for the sake of completeness the well-known fact that if the prepotential function $F$ is such that $N_{A B}=\operatorname{Im} F_{A B}$ has Lorentzian signature $(1, n-1)$, then on the open complex domain given by the condition $(\bar{Z} N Z)>0$, where we have $R<0$, both $g_{P S K}$ and $g_{T}$ are negative definite (the first statement is straightforward, the second one was shown in [18] by an ingenious argument based on the so-called inverse Cauchy-Schwarz inequality), and therefore $s g$ is negative definite. In other words, in this case one can choose the metric to be positive definite, and this metric will have a negative scalar curvature.
5.0.12. The local c-map has been studied extensively in both the physics and mathematics literature. In particular, a different and very interesting geometric construction, starting from the rigid c-map and based on the so-called hyperkähler/quaternionic Kähler correspondence, has been given in [4] (see also the preceding work of [31] and [6]). Global aspects of the Ferrara-Sabharwal metric have been considered in [17, 39], and completeness issues have been discussed in [16, 17]. Further considerations such as quantum perturbative and instanton corrections have been explored in [7, 42, 6].

\section*{References}
1. D. V. Alekseevsky, Riemannian spaces with unusual holonomy groups, Funcktional. Anal. i Priložen 2 (1968), no. 2, 1-10, (English translation: Funct. Anal. Appl., 2, 97-105, 1968). MR 0231313
2. D. V. Alekseevsky, E. Bonan, and S. Marchiafava, On some structure equations for almost quaternionic Hermitian manifolds, Complex structures and vector fields (Pravetz, 1994), World Sci. Publ., River Edge, NJ, 1995, pp. 114-134. MR 1376149
3. D. V. Alekseevsky, V. Cortés, and C. Devchand, Special complex manifolds, J. Geom. Phys. 42 (2002), 85-105.
4. D. V. Alekseevsky, V. Cortés, M. Dyckmanns, and T. Mohaupt, Quaternionic Kähler metrics associated with special Kähler manifolds, J. Geom. Phys. 92 (2015), 271-287.
5. D. V. Alekseevsky and S. Marchiafava, Quaternionic structures on a manifold and subordinated structures, Ann. Mat. Pura Appl. (4) 171 (1996), 205-273. MR 1441871
6. S. Alexandrov, D. Persson, and B. Pioline, Wall-crossing, Rogers dilogarithm, and the QK/HK correspondence, JHEP 12 (2011), 027.
7. L. Anguelova, M. Roček, and S. Vandoren, Quantum corrections to the universal hypermultiplet and superspace, Phys. Rev. D70 (2004), 066001.
8. W. Ballmann, Homogeneous structures, (2007), Lecture notes, available online.
9. E. Bergshoeff, S. Cucu, T. de Wit, J. Gheerardyn, S. Vandoren, and A. Van Proeyen, The map between conformal hypercomplex/hyper-Kähler and quaternionic(-Kähler) geometry, Comm. Math. Phys. 262 (2006), no. 2, 411-457. MR 2200267
10. R. Bielawski, Complete hyper-Kähler 4n-manifolds with a local tri-Hamiltonian $\mathbb{R}^{n}$-action, Math. Ann. 314 (1999), no. 3, 505-528. MR 1704547
11. C. P. Boyer and J. D. Finley, III, Killing vectors in self-dual, Euclidean Einstein spaces, J. Math. Phys. 23 (1982), no. 6, 1126-1130. MR 660020
12. R. L. Bryant, S. S. Chern, R. B. Gardner, H. L. Goldschmidt, and P. A. Griffiths, Exterior differential systems, Mathematical Sciences Research Institute Publications, vol. 18, Springer-Verlag, New York, 1991. MR 1083148
13. D. M. J. Calderbank and H. Pedersen, Selfdual Einstein metrics with torus symmetry, J. Diff. Geom. 60 (2002), no. 3, 485-521. MR 1950174
14. D. M. J. Calderbank and M. A. Singer, Toric self-dual Einstein metrics on compact orbifolds, Duke Math. J. 133 (2006), no. 2, 237-258. MR 2225692
\begin{itemize}
\item[15.] S. Cecotti, S. Ferrara, and L. Girardello, Geometry of Type II Superstrings and the Moduli of Superconformal Field Theories, Int. J. Mod. Phys. A4 (1989), 2475.
\item[16.] V. Cortés, M. Dyckmanns, and S. Suhr, Completeness of projective special Kähler and quaternionic Kähler manifolds, Special metrics and group actions in geometry, Springer INdAM Ser., vol. 23, Springer, Cham, 2017, pp. 81-106. MR 3751963
\item[17.] V. Cortés, T. Mohaupt, and H. Xu, Completeness in supergravity constructions, Comm. Math. Phys. 311 (2012), 191-213.
\item[18.] E. Cremmer, C. Kounnas, A. Van Proeyen, J. P. Derendinger, S. Ferrara, B. de Wit, and L. Girardello, Vector Multiplets Coupled to $N=2$ Supergravity: SuperHiggs Effect, Flat Potentials and Geometric Structure, Nucl. Phys. B250 (1985), 385-426.
\item[19.] B. de Wit, B. Kleijn, and S. Vandoren, Superconformal hypermultiplets, Nucl. Phys. B 568 (2000), no. 3, 475-502. MR 1744865
\item[20.] B. de Wit, M. Roček, and S. Vandoren, Hypermultiplets, hyper-Kähler cones and quaternion-Kähler geometry, JHEP (2001), no. 2. MR 1825214
\item[21.] B. de Wit and A. Van Proeyen, Potentials and Symmetries of General Gauged $N=2$ Supergravity: Yang-Mills Models, Nucl. Phys. B245 (1984), 89-117.
\item[22.] \_\_\_\_, Symmetries of dual quaternionic manifolds, Phys. Lett. B252 (1990), 221-229.
\item[23.] S. Ferrara and S. Sabharwal, Quaternionic Manifolds for Type II Superstring Vacua of Calabi-Yau Spaces, Nucl. Phys. B332 (1990), 317-332.
\item[24.] D. S. Freed, Special Kähler manifolds, Comm. Math. Phys. 203 (1999), no. 1, 31-52. MR 1695113
\item[25.] K. Galicki, A generalization of the momentum mapping construction for quaternionic Kähler manifolds, Comm. Math. Phys. 108 (1987), no. 1, 117-138. MR 872143
\item[26.] K. Galicki and H. B. Lawson, Jr., Quaternionic reduction and quaternionic orbifolds, Math. Ann. 282 (1988), no. 1, 1-21. MR 960830
\item[27.] G. W. Gibbons and S. W. Hawking, Gravitational Multi-Instantons, Phys. Lett. 78B (1978), 430.
\item[28.] G. W. Gibbons and P. Rychenkova, Cones, tri-Sasakian structures and superconformal invariance, Phys. Lett. B 443 (1998), no. 1-4, 138-142. MR 1663805
\item[29.] A. Gray, A note on manifolds whose holonomy group is a subgroup of $\operatorname{Sp}(n) \cdot \operatorname{Sp}(1)$, Michigan Math. J. 16 (1969), 125-128. MR 0244913
\item[30.] N. J. Hitchin, The self-duality equations on a Riemann surface, Proc. London Math. Soc. (3) 55 (1987), no. 1, 59-126. MR 887284
\item[31.] \_\_\_\_, Quaternionic Kähler moduli spaces, Riemannian topology and geometric structures on manifolds, Progr. Math., vol. 271, Birkhäuser Boston, Boston, MA, 2009, pp. 49-61. MR 2494168
\item[32.] N. J. Hitchin, A. Karlhede, U. Lindström, and M. Roček, Hyper-Kähler metrics and supersymmetry, Comm. Math. Phys. 108 (1987), no. 4, 535-589. MR 877637
\item[33.] R. A. Ionaş and A. Neitzke, A Note on conformal symmetry in projective superspace, (2008).
\item[34.] D. Joyce, Explicit construction of self-dual 4-manifolds, Duke Math. J. 77 (1995), no. 3, 519-552. MR 1324633
\item[35.] S. Kobayashi and K. Nomizu, Foundations of differential geometry. Vol I, Interscience Publishers, a division of John Wiley \& Sons, New York-London, 1963. MR 0152974
\item[36.] \_\_\_\_, Foundations of differential geometry. Vol. II, Interscience Publishers John Wiley \& Sons, Inc., New York-London-Sydney, 1969. MR 0238225
\item[37.] B. Kostant, Holonomy and the Lie algebra of infinitesimal motions of a Riemannian manifold, Trans. Amer. Math. Soc. 80 (1955), 528-542. MR 0084825
\item[38.] U. Lindström and M. Roček, Scalar Tensor Duality and $N=1, N=2$ Nonlinear Sigma Models, Nucl. Phys. B222 (1983), 285-308.
\item[39.] O. Macia and A. Swann, Twist geometry of the c-map, Comm. Math. Phys. 336 (2015), no. 3, 1329-1357. MR 3324146
\item[40.] A. Neitzke, B. Pioline, and S. Vandoren, Twistors and black holes, JHEP 04 (2007), 038.
\item[41.] H. Pedersen and Y. S. Poon, Hyper-Kähler metrics and a generalization of the Bogomolny equations, Comm. Math. Phys. 117 (1988), no. 4, 569-580. MR 953820
\item[42.] D. Robles-Llana, M. Roček, F. Saueressig, U. Theis, and S. Vandoren, Nonperturbative corrections to $4 D$ string theory effective actions from $S L(2, Z)$ duality and supersymmetry, Phys. Rev. Lett. 98 (2007), 211602.
\item[43.] M. Roček, C. Vafa, and S. Vandoren, Hypermultiplets and topological strings, JHEP 02 (2006), 062.
\end{itemize}
\begin{itemize}
\item[44.] \_\_\_\_, Quaternion-Kähler spaces, hyperkähler cones, and the c-map, (2006).
\item[45.] S. Salamon, Quaternionic Kähler manifolds, Invent. Math. 67 (1982), no. 1, 143-171. MR 664330
\item[46.] A. Swann, Hyper-Kähler and quaternionic Kähler geometry, Math. Ann. 289 (1991), no. 3, 421-450. MR 1096180
\item[47.] K. P. Tod, The $\operatorname{SU}(\infty)$-Toda field equation and special four-dimensional metrics, Geometry and physics (Aarhus, 1995), Lecture Notes in Pure and Appl. Math., vol. 184, Dekker, New York, 1997, pp. 307-312. MR 1423177
\item[48.] R. S. Ward, Einstein-Weyl spaces and $\mathrm{SU}(\infty)$ Toda fields, Class. Quant. Grav. 7 (1990), no. 4, L95-L98. MR 1045295
\end{itemize}

Radu A. Ionaș
C. N. Yang Institute for Theoretical Physics
Stony Brook University, Stony Brook, NY 11794, U.S.A.