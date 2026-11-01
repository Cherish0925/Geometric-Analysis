---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: On asymptotic behavior of the second Chern forms on degenerating Kähler-Einstein surfaces]

---
source_file: 2505_01773.pdf
converter: mathpix
format: mmd
---

\title{
ON ASYMPTOTIC BEHAVIOR OF THE SECOND CHERN FORMS ON DEGENERATING KÄHLER-EINSTEIN SURFACES
}

\author{
ITSUKI TAZOE
}

\begin{abstract}
We study an asymptotic behavior of the second Chern forms of canonical metrics on a degenerating family of Kähler surfaces with the central fibre having ADE-singularities. We investigate a function on the unit disc defined by fiber integrals of the forms with a smooth test function on the family. We show a lower bound of the Hölder exponent of the function at the origin. Our main results consists of two cases: one is a bound of Hölder exponent along a line for cscK-metrics, using Biquard-Rollin's a priori estimates for cscK-metrics, and the other is a bound of Hölder exponent at the origin for Ricci-flat metrics.
\end{abstract}

\section*{1. Introduction}

In [15], J.R.King studied behavior of flat proper family of analytic spaces as currents:

Theorem 1 (Theorem 3.3.2. in [15]). Let $f: X \rightarrow Y$ be a proper flat map of complex analytic spaces with irreducible fibers of dimension $d$. Then for a continuous $(d, d)$ form $\varphi$ on $X$, the function $\Phi: Y \rightarrow \mathbb{C}$ defined by
$$\Phi(y):=\int_{f^{-1}(y)} \varphi$$
is a continuous function on $Y$.
In [5], D. Barlet developed the behavior of the fibre integral for a one parameter degenerating family of manifolds with assumption on the smoothness of the integrant:

Theorem 2 (Théorème 1 in [5]). Let $\mathcal{X}$ be an irreducible and reduced analytic space of dimension $n+1$. Let $f: \mathcal{X} \rightarrow \Delta$ be a holomorphic surjection onto the unit disc $\Delta \subset \mathbb{C}$ and let $X_{t}:=f^{-1}(t) \subset \mathcal{X}$ be the fibre on $t \in \Delta$. Then for every compact subset $K \subset \mathcal{X}$, there are rational numbers $r_{1}, \ldots, r_{k} \in[0,2) \cap \mathbb{Q}$ such that for every smooth $(n, n)$-form $\phi$ on $\mathcal{X}$ supported on $K$, its fibre integration
$$F_{\phi}(t)=\int_{X_{t}} \phi$$
admits an asymptotic expansion
$$F_{\phi}(t) \sim \sum_{\substack{r=r_{1}, \ldots, r_{k} \\ j=1, \ldots, n \\(m, n) \in \mathbb{N}^{2}}} T_{m, n}^{r, j}(\phi) t^{m} \bar{t}^{n}|t|^{r}(\log (|t|))^{j}$$
as $t \rightarrow 0$, where $T_{m, n}^{r, j}$ are $(1,1)$-currents on $\mathcal{X}$.

\footnotetext{
Mathematics subject classification:53C26.
}

As a special case of the above theorem, we have asymptotic expansion of forms coming from a characteristic form of a metric on $\mathcal{X}$.

In the present paper, we study asymptotic behavior of fiber integrals without assumptions on regularity of the integrant a priori but taking the integrant canonically. Explicitly, we study asymptotic behavior of characteristic forms of a canonical metric on the relative tangent bundle $T \mathcal{X} / \Delta$ which is not necessarily coming from a smooth metric on $T \mathcal{X}$ and not necessarily smooth around the origin $0 \in \Delta$ a priori.

Studying canonical metrics on complex manifolds is one of the central problems in complex geometry. For Riemann surfaces, the most fundamental situation, we have a unique (up to constant multiplication) metric on every compact Riemann surface with constant Gauss curvature. For higher dimensional case, the existence theorems by Aubin and Yau [2][26], Yau[26], and Chen-Donaldson-Sun[9] guarantee existence of Kähler-Einstein metrics, i.e. Kähler metrics with constant Ricci curvatures, of general type, Calabi-Yau and (K-stable) Fano manifolds respectively.

It is natural to investigate degeneration of Kähler-Einstein metrics in an algebrogeometric setting. A pioneering work by R. Kobayashi and A. Todorov [17] investigated degeneration of polarized K3 surfaces, an important class of 2-dimensional Calabi-Yau manifold. In [17], it was proved that if polarized K3 surfaces converges to a polarized K3 surface possibly singular in an algebro-geometric sense, then they also converges to the same K3 surface in the Gromov-Hausdorff sense (see [17] Theorem 8 for the precise statement). Rather Riemannian Geometric context, Anderson [1], Nakajima [20], Bando-Kasue-Nakajima[4] etc. studied limits of 4-dimensional Einstein manifolds (see section 2.2 for more details). In [10][11], it was shown that if a convergent sequence of polarized Kähler manifolds with uniformly bounded volumes, diameters and Ricci curvatures satisfies a non-collapsing condition then its limit is a normal projective variety at worst klt singularities.

Two different type of canonical metrics are treated: One is constant scaler curvature Kähler metrics (cscK metrics for short) and the other is Ricci-flat metrics. The main results of the present paper are the following.

Theorem (Theorem 7 in section 3). Let $\left(\mathcal{X} \rightarrow \Delta,\left\{\Omega_{t}\right\}_{t \in \Delta}\right)$ be a smoothing family of compact surface $\left(X_{0}, \omega_{0}\right)$ with ADE-singularities (see section 2.3 for its precise meaning), where $\Delta \subset \mathbb{C}$ is the unit disc, and $f$ be a smooth function on $\mathcal{X}$ with its support containing only $x_{0} \in X_{0} \cong 0 \in \mathbb{C}^{2} / \Gamma$. Assume that the family admits a simultaneous resolution $\widetilde{\mathcal{X}} \rightarrow \Delta_{d}$ after taking a base change by the ramified covering $\Delta_{d} \rightarrow \Delta$ of degree $d$ and it is non-degenerate at $x_{0}$ along a real ray $\Delta \cap(0,1)$ (see definition 3). Furthermore, we assume that $X_{t}$ admits a cscK metric $g_{t}$ with its Kähler form $\omega_{t}$ in $\Omega_{t}$. Consider a function
$$F(t)=\int_{X_{t}} f_{t} c_{2}\left(g_{t}\right)$$
on $\Delta \cap(0,1)$, where $g_{t}$ is the cscK metric on $X_{t}$ with its Kähler class $\Omega_{t}, c_{2}\left(g_{t}\right)$ is the second Chern form of $g_{t}$ on $T X_{t}$ and $f_{t}=\left.f\right|_{X_{t}}$. Then $F$ extends to a Hölder continuous function on $\Delta \cap[0,1)$ with Hölder exponent at least $\frac{1}{d}$.

The above theorem is proven by using an a priori estimate of cscK metrics by Biquard-Rollin [7]. A family of Kähler metrics which approximates a family of cscK metrics with prescribed Kähler classes is constructed and the difference of the
approximating metrics and the cscK metrics are estimated by the a priori estimate of cscK equation in [7]. Using the results, the behavior of $c_{2}\left(g_{t}\right)$ can be investigated by using the approximating metrics and the a priori estimate.

In the above theorem, we only know asymptotic behavior of $c_{2}\left(g_{t}\right)$ along the real ray. To investigate asymptotic behavior on the hole disc, we further assume that the family is Kähler-Einstein. For a Kähler-Einstein case, we consider a family of polerized K3 surfaces $(\mathcal{X}, \mathcal{L}) \rightarrow \Delta$. For each fiber $\left(X_{t}, L_{t}\right)$, let $\hat{g}_{t}$ be the Ricci flat Kähler metric with its Kähler form $\hat{\omega}_{t} \in c_{1}\left(L_{t}\right)$. To study behavior of the second chern forms $c_{2}\left(\hat{g}_{t}\right)$, an almost Ricci flat Kähler metrics $\tilde{g}_{t}$ on $X_{t}$ which approximates $\hat{g}_{t}$ well are constructed (see section 4 for details). And then, the metric $\tilde{g}_{t}$ approximates $\hat{g}_{t}$ not only its metric structure, but also its Ricci curvature. Then the main theorem in section 4 is the following.

Theorem (Theorem 9 in section 4). Let $(\mathcal{X}, \mathcal{L}) \rightarrow \Delta$ be a flat proper family of polarized K3 surfaces over the unit disc $\Delta \subset \mathbb{C}$ such that the fibre $\left(X_{t}, L_{t}\right)$ on $t \in \Delta$ is smooth for $t \neq 0$ and singular for $t=0$ with ADE singularities. Assume that the family $\mathcal{X} \rightarrow \Delta$ admits the minimal simultaneous resolution after taking the base change $\Delta_{d} \rightarrow \Delta$ and non-degenerate at a singularity $x_{0} \in X_{0} \cong \mathbb{C}^{2} / \Gamma$. Then for any smooth function $f$ on $\mathcal{X}$ with its support around the singularity $x_{0} \in X_{0} \cong 0 \in$ $\mathbb{C}^{2} / \Gamma$, the function
$$F(t)=\int_{X_{t}} f_{t} c_{2}\left(\hat{g}_{t}\right)$$
on $\Delta \backslash\{0\}$ extends to a Hölder continuous function on $\Delta$ with Hölder exponent at least $\frac{1}{d}$.

In section 2, we recall some preliminary facts, the theory of Kronheimer's ALE gravitational instanton, non-collapsing limits of Einstein 4-manifolds and Biquard-Rollin's a priori estimate for constant scaler curvature equation for a family of surfaces. Section 3 is the proof of the main theorem for the cscK metric case. The main theorem for Ricci flat Kähler metrics on a family of polarized K3 surfaces is proven in section 4.

Acknowledgements. The author is grateful to Professor K.-I. Yoshikawa and Professor Y. Odaka, his supervisors, for their help and encouragement which lead him to complete this master thesis. The author is also grateful to E.Inoue and S.Katayama for suggestions on some technical problems.

\section*{2. Preliminaries}
2.1. ALE Gravitational Instanton. ALE Gravitational Instantons are families of 4-dimensional complete hyperkähler manifolds that play an important role in the study of Gromov-Hausdorff limits of Kähler-Einstein surfaces. They appear as bubbling limits of non-collapsing Gromov-Hausdorff limits of Kähler-Einstein surfaces (for details, see section 2.2).

Definition 1. Let $(X, g, I, J, K)$ be a 4-dimensional complete hyperkähler manifold. $(X, g, I, J, K)$ is an ALE gravitational instanton (of order 4) if there is a compact subset $K \subset X$ and a diffeomorphism
$$\phi:\left(\mathbb{R}^{4} \backslash B(0, R)\right) / \Gamma \rightarrow X \backslash K$$
for a suitable $R>0$ and a finite subgroup $\Gamma \subset \operatorname{SL}(2 ; \mathbb{C})$ such that
$$\begin{aligned}
\left\|\nabla^{k}\left(\phi^{*} g-g^{\text {Euc }}\right)\right\|_{g^{\text {Euc }}} & =O\left(r^{-4-k}\right), \\
\left\|\nabla^{k}\left(\phi^{*} \omega_{I}-\omega_{I}^{\text {Euc }}\right)\right\|_{g^{\text {Euc }}} & =O\left(r^{-4-k}\right), \\
\left\|\nabla^{k}\left(\phi^{*} \omega_{J}-\omega_{J}^{\text {Euc }}\right)\right\|_{g^{\text {Euc }}} & =O\left(r^{-4-k}\right), \\
\left\|\nabla^{k}\left(\phi^{*} \omega_{K}-\omega_{K}^{\text {Euc }}\right)\right\|_{g^{\text {Euc }}} & =O\left(r^{-4-k}\right)
\end{aligned}$$
as $r \rightarrow \infty$ for any $k \in \mathbb{N}$, where $r$ is the Euclidean distance from the origin.
Note that $\mathbb{C}^{2}$ admits a natural hyperkähler structure via an isomorphism
$$\begin{aligned}
\mathbb{H} & \rightarrow \mathbb{C}^{2} \\
a+b i+c j+d k & \mapsto(a+b i, c+d i) .
\end{aligned}$$
To state the classification theorem of ALE gravitational instantons by Kronheimer [18] [19], we review some properties of ADE singularities. Let $\Gamma \subset \operatorname{SL}(2 ; \mathbb{C})$ be a finite subgroup and let $Y$ denote the underlying differentiable manifold of the minimal resolution $\widetilde{\mathbb{C}^{2} / \Gamma}$ of the singularity $0 \in \mathbb{C}^{2} / \Gamma$ with the exceptional divisor $E=\bigcup_{i=1}^{n} E_{i}$. Then, it is well-known that the homology classes of the irreducible components $\left\{\left[E_{i}\right]\right\}_{i=1}^{n}$ forms a basis of $H_{2}(Y, \mathbb{Z})$ as a $\mathbb{Z}$-module. Furthermore, by the Poincaré-Lefschetz duality, we may define an intersection pairing on $H_{2}(Y, \mathbb{Z})$ which induces an isomorphism
$$H_{2}(Y, \mathbb{Z}) \cong H^{2}(Y, \mathbb{Z}) .$$
The lattice $H_{2}(Y, \mathbb{Z})$ is isometric to the lattice defined by a Dynkin diagram of one of the ADE-type. It is also important that $H_{2}(Y, \mathbb{Z})$ is isometric to the root lattice $\mathfrak{h}_{\mathbb{Z}}$ of the simple complex Lie algebra $\mathfrak{g}$ which corresponds to the same Dynkin diagram by a linear map sending $\left\{\left[E_{i}\right]\right\}$ to simple roots (see [24] for more details). Now, we can state the classification theorem that was proved in [18][19]:

Theorem 3 (Theorem 1.1, Theorem 1.2, Theorem 1.3 in [18][19]). (i) Let $\boldsymbol{\kappa}=$ $\left(\kappa_{1}, \kappa_{2}, \kappa_{3}\right)$ be a triple of elements in $H^{2}(Y, \mathbb{R})$ that satisfies the following property:
$$\text { for any } e \in H_{2}(Y, \mathbb{Z}) \text { with }(e, e)=-2, \kappa_{i}(e) \neq 0 \text { for at least one } i=1,2,3$$
Then there exists a quadruple $\left(g_{\boldsymbol{\kappa}}, I_{\boldsymbol{\kappa}}, J_{\boldsymbol{\kappa}}, K_{\boldsymbol{\kappa}}\right)$ such that $Y_{\boldsymbol{\kappa}}:=\left(Y, g_{\boldsymbol{\kappa}}, I_{\boldsymbol{\kappa}}, J_{\boldsymbol{\kappa}}, K_{\boldsymbol{\kappa}}\right)$ is an ALE gravitational instanton and
$$\left(\left[\omega_{I_{\kappa}}\right],\left[\omega_{J_{\kappa}}\right],\left[\omega_{K_{\kappa}}\right]\right)=\boldsymbol{\kappa},$$
where $\omega_{I_{\kappa}}, \omega_{J_{\kappa}}, \omega_{K_{\kappa}}$ are the Kähler forms of the three complex structures.
(ii) Any ALE gravitational instanton $Y^{\prime}$ is diffeomorphic to $\widetilde{\mathbb{C}^{2} / \Gamma}$ for some $\Gamma \subset$ $\operatorname{SL}(2 ; \mathbb{C})$ and the triple of the Kähler classes of $Y^{\prime}$ satisfies the property (6) in (i).
(iii) Let $\left(Y_{1}, g_{1}, I_{1}, J_{1}, K_{1}\right),\left(Y_{2}, g_{2}, I_{2}, J_{2}, K_{2}\right)$ be ALE gravitational instantons. If there is a diffeomorphism $Y_{1} \rightarrow Y_{2}$ which respects the triples of the Kähler classes, then $\left(Y_{1}, g_{1}, I_{1}, J_{1}, K_{1}\right)$ and $\left(Y_{2}, g_{2}, I_{2}, J_{2}, K_{2}\right)$ are isomorphic as hyperkähler manifolds, i.e. there exists a diffeomorphism $f: Y_{1} \rightarrow Y_{2}$ such that
$$f^{*} g_{2}=g_{1}, f^{*} \omega_{I_{2}}=\omega_{I_{1}}, f^{*} \omega_{J_{2}}=\omega_{J_{1}}, f^{*} \omega_{K_{2}}=\omega_{K_{1}} .$$

To state some basic properties of ALE gravitational instantons, following [18], we recall an outline of the construction of ALE gravitational instantons on $Y$. For
a finite subgroup $\Gamma \subset \operatorname{SL}(2 ; \mathbb{C})$, define $M$ as the $\Gamma$ invariant points of the tensor product $\mathbb{C}^{2} \otimes_{\mathbb{C}} \operatorname{End}(\mathbb{C}[\Gamma])$ :
$$M:=\left\{v \in \mathbb{C}^{2} \otimes_{\mathbb{C}} \operatorname{End}(\mathbb{C}[\Gamma]) \mid g \cdot v=v\right\} \subset \mathbb{C}^{2} \otimes_{\mathbb{C}} \operatorname{End}(\mathbb{C}[\Gamma]),$$
where $\mathbb{C}^{2}$ is viewed as the natural $\Gamma$ module (recall that $\Gamma$ is a subgroup of $\operatorname{SL}(2 ; \mathbb{C})$ ) and $\mathbb{C}[\Gamma]$ is the group ring of $\Gamma$. Then one can equip $M$ a hyperkähler structure and a Lie group action $F \curvearrowright M$ which preserves the hyperkähler structure, where $F$ is a suitable sub Lie group of $\mathrm{U}(\mathbb{C}[\Gamma])$ (see [18] for the definitions of $F$ and the action $F \curvearrowright M$ ). Also, one can construct a hyperkähler moment map
$$\mu: M \rightarrow \mathfrak{h}_{\mathbb{R}} \otimes \mathbb{R}^{3}$$
(see [18] section 2 for their concrete construction), where $\mathfrak{h}_{\mathbb{R}}=\mathfrak{h}_{\mathbb{Z}} \otimes \mathbb{R}$ is the real part of a Cartan subalgebra of the corresponding ADE type of $\Gamma$. In [18], it was shown that the quotient $Y_{\zeta}:=\mu^{-1}(\zeta) / F$ is non singular if $\zeta \in\left(\mathfrak{h}_{\mathbb{R}} \otimes \mathbb{R}^{3}\right)^{o}$, where
$$\left(\mathfrak{h}_{\mathbb{R}} \otimes \mathbb{R}^{3}\right)^{o}=\left(\mathfrak{h}_{\mathbb{R}} \otimes \mathbb{R}^{3}\right) \backslash \bigcup_{\theta \text { is a root }} H_{\theta} \otimes \mathbb{R}^{3} .$$
Here, $H_{\theta}:=\theta^{\perp} \subset \mathfrak{h}_{\mathbb{R}}$ denotes the hyperplane cut out by $\theta$ and $\theta \in \mathfrak{h}_{\mathbb{Z}}$ is a root, by definition, if $(\theta, \theta)=-2$. Hence, as the hyperkähler structure on $M$ is preserved by the group action $F \curvearrowright M$, the quotient $Y_{\zeta}=\mu^{-1}(\zeta) / F$ becomes a hyperkähler manifold. Let $\left(Y_{\zeta}, g_{\zeta}, I_{\zeta}, J_{\zeta}, K_{\zeta}\right)$ denote the hyperkähler structure on $Y_{\zeta}$. In the following, we regard $Y_{\zeta}$ as a complex surface by the complex structure $I_{\zeta}$ and identify $\mathfrak{h}_{\mathbb{R}} \otimes \mathbb{R}^{3} \cong\left(\mathfrak{h}_{\mathbb{R}}\right)^{\oplus 3}$ as $\mathfrak{h}_{\mathbb{R}} \oplus \mathfrak{h}_{\mathbb{C}}$ by
$$\begin{aligned}
\left(\mathfrak{h}_{\mathbb{R}}\right)^{\oplus 3} & \rightarrow \mathfrak{h}_{\mathbb{R}} \oplus \mathfrak{h}_{\mathbb{C}} \\
\left(\zeta_{1}, \zeta_{2}, \zeta_{3}\right) & \mapsto\left(\zeta_{1}, \zeta_{2}+\sqrt{-1} \zeta_{3}\right)=\left(\zeta_{r}, \zeta_{c}\right) .
\end{aligned}$$
In [18], it was also proved that the quotient $Y_{\left(0, \zeta_{c}\right)}$ becomes a (possibly singular) affine complex variety for any $\zeta_{c} \in \mathfrak{h}_{\mathbb{C}}$ and that, in particular, $Y_{(0,0)}$ is biholomorphic to $\mathbb{C}^{2} / \Gamma$. Furthermore, if $\zeta_{r} \in \mathfrak{h}_{\mathbb{R}}$ is not perpendicular to any root in $\mathfrak{h}_{\mathbb{Z}}$, there exists a holomorphic map
$$\lambda_{\zeta}: Y_{\left(\zeta_{r}, \zeta_{c}\right)} \rightarrow Y_{\left(0, \zeta_{c}\right)}$$
that gives the minimal resolution of $Y_{\left(0, \zeta_{c}\right)}$. For a given non-singular $Y_{\zeta}$, by a suitable choice of a coordinate of $\mathbb{R}^{3}$, we may assume that $\zeta_{1}$ is not perpendicular to any root. Then by using (12) repeatedly, we have the following:
$$Y_{\zeta} \xrightarrow{\lambda_{\zeta}} Y_{\left(\zeta_{1}, \zeta_{2}, 0\right)} \xrightarrow{\lambda_{\left(\zeta_{1}, \zeta_{2}, 0\right)}} Y_{\left(\zeta_{1}, 0,0\right)} \xrightarrow{\lambda_{\left(\zeta_{1}, 0,0\right)}} Y_{(0,0,0)} \cong \mathbb{C}^{2} / \Gamma .$$
Since $Y_{\left(\zeta_{1}, 0,0\right)}$ is naturally diffeomorphic to $Y$, we see that any non-singular $Y_{\zeta}$ is naturally diffeomorphic to $Y$. The diffeomorphism $Y_{\zeta} \cong Y$ induced by (13) depends on the choice of orthonormal basis of $\mathbb{R}^{3}$, however, we may choose the diffeomorphisms in a canonical way in the following sense:

Theorem 4 ([18] Section 3 and Section 4, namely from Corollary 3.12.). There exist identifications
$$\begin{aligned}
H_{2}(Y, \mathbb{Z}) & \cong \mathfrak{h}_{\mathbb{Z}}, \\
\Lambda_{\zeta}: Y & \rightarrow Y_{\zeta},
\end{aligned}$$
such that for any $\zeta \in\left(\mathfrak{h}_{\mathbb{R}} \otimes \mathbb{R}^{3}\right)^{o}, \Lambda_{\zeta}^{*}\left(\left[\omega_{i}\right]\right)=\zeta_{i} \in \mathfrak{h}_{\mathbb{R}}$, where $\left(\omega_{1}, \omega_{2}, \omega_{3}\right)=$ $\left(\omega_{I}, \omega_{J}, \omega_{K}\right)$ are the Kähler forms of $Y_{\zeta}$. Furthermore, $\left\{\left(\Lambda_{\zeta}^{*} g_{\zeta}, \Lambda_{\zeta}^{*} I_{\zeta}, \Lambda_{\zeta}^{*} J_{\zeta}, \Lambda_{\zeta}^{*} K_{\zeta}\right)\right\}_{\zeta \in\left(\mathfrak{h} \otimes \mathbb{R}^{3}\right)^{o}}$
is a family of hyperkähler structures on $Y$ depending on $\zeta$ smoothly (this is the hy-perkähler structure stated in Theorem 1).

Now, we are ready to state properties of $Y_{\zeta}$ which we will use in the paper:
\begin{itemize}
\item[-] ([18] Proposition 3.14. and its proof) any non-singular $Y_{\zeta}$ is an ALE gravitational instanton. Namely, by the composition
$$\rho_{\zeta}: Y_{\zeta} \xrightarrow{\Lambda_{\zeta}^{-1}} \widetilde{\mathbb{C}^{2} / \Gamma} \xrightarrow{\text { blow down }} \mathbb{C}^{2} / \Gamma$$
we have a diffeomorphism
$$\varphi_{\zeta}:\left(\mathbb{C}^{2} \backslash \overline{B(0 ; R)}\right) / \Gamma \rightarrow Y_{\zeta} \backslash K$$
for any $R>0$ and a suitable compact subset $K \subset Y_{\zeta}(B(0, R)$ is the open ball centered at the origin with diameter $R$ ). Under this diffeomorphism, we have the expansion of the hyperkähler metric $g_{\zeta}$ and its Kähler form $\omega_{I_{\zeta}}$ on $\mathbb{C}^{2} \backslash \overline{B(0, R)}$ :
$$\begin{gathered}
\varphi_{\zeta}^{*} g_{\zeta}=g^{\mathrm{Euc}}+\sum_{i=2}^{k-1} g_{\zeta}^{(i)} r^{-2 i}+O\left(r^{2 k}\right), \\
\varphi_{\zeta}^{*} \omega_{I_{\zeta}}=\omega^{\mathrm{Euc}}+\sum_{i=2}^{k-1} \omega_{I_{\zeta}}^{(i)} r^{-2 i}+O\left(r^{2 k}\right),
\end{gathered}$$
where $g_{\zeta}^{(i)}, \omega_{I_{\zeta}}^{(i)}$ are homogeneous polynomials of degree $i$ in $\zeta$ and $g^{\text {Euc }}, \omega^{\text {Euc }}$ are the standard Kähler metric and its Kähler form on $\mathbb{C}^{2}$ (where $r(x):=$ $d(0, x)$ is the radius function on $\mathbb{C}^{2}$ ).
\item[-] ([18] section 3 and 4)
$$\mathcal{Y}=\bigcup_{\zeta \in \mathfrak{h}_{\mathbb{C}}} Y_{(0, \zeta)}$$
admits a natural complex structure such that the natural projection $\mathcal{Y} \rightarrow \mathfrak{h}_{\mathbb{C}}$ is holomorphic. This family $\mathcal{Y} \rightarrow \mathfrak{h}_{\mathbb{C}}$ coincides with the base change of the versal deformation of the singularity $0 \in \mathbb{C}^{2} / \Gamma$ by the Weyl covering $\mathfrak{h}_{\mathbb{C}} \rightarrow \mathfrak{h}_{\mathbb{C}} / W$, where $W$ is the Weyl group of $\mathfrak{h}$. Furthermore, for any $\zeta_{r} \in \mathfrak{h}_{\mathbb{R}}$ that is not perpendicular to any roots of $\mathfrak{h}$ and for any family $\mathcal{Y}_{(0, \zeta)} \rightarrow \Delta$ over the unit disc defined by a holomorphic map $\zeta: \Delta \rightarrow \mathfrak{h}_{\mathbb{C}}$, the family
$$\mathcal{Y}_{\left(\zeta_{r}, \zeta\right)}=\bigcup Y_{\left(\zeta_{r}, \zeta(t)\right)} \rightarrow \Delta$$
(it also admits a natural complex structure) gives the minimal simultaneous minimal resolution of $\mathcal{Y}_{(0, \zeta)}$ (it is induced by applying (12) fiberwise).
\item[-] ([18] Proof of Corollary 3.12) The natural $\mathbb{R}_{>0}$-action on $M$
$$\begin{aligned}
M & \rightarrow M \\
v & \mapsto \alpha v
\end{aligned}$$
induces a morphism
$$H_{(\alpha, \zeta)}: Y_{\zeta} \rightarrow Y_{\alpha^{2} \zeta}$$
which induces an isomorphism
$$Y_{\zeta} \cong \frac{1}{\alpha^{2}} Y_{\alpha^{2} \zeta}=\left(Y, \frac{1}{\alpha^{2}} g_{\alpha^{2} \zeta}, I_{\alpha^{2} \zeta}, J_{\alpha^{2} \zeta}, K_{\alpha^{2} \zeta}\right)$$
\end{itemize}
\begin{itemize}
\item[] as hyperkähler manifolds. Furthermore, an open embedding $\left(\mathbb{C}^{2} \backslash\{0\}\right) / \Gamma \rightarrow$ $Y_{\zeta}$ induced by (15) is $\mathbb{R}_{>0}$ equivariant. Namely, for any $y \in Y_{\zeta}$ such that $r(y)>0$,
$$\rho_{\alpha^{2} \zeta} \circ H_{(\alpha, \zeta)}(y)=\alpha \rho_{\zeta}(y) .$$
In particular, if $f=O\left(r^{k}\right)$ on $Y$ as $r \rightarrow \infty, H_{(\alpha, \zeta)}^{*}(f)=O\left(\alpha^{k} r^{k}\right)$ as $r \rightarrow \infty$.
\item[-] ([18] section 4) The family $\mathcal{Y} \rightarrow \mathfrak{h}_{\mathbb{C}}$ (see (19)) admits an embedding
$$\iota: \mathcal{Y} \rightarrow \mathbb{C}^{3} \times \mathfrak{h}_{\mathbb{C}}$$
such that the projection $\mathcal{Y} \rightarrow \mathfrak{h}_{\mathbb{C}}$ is induced by the natural projection $\mathbb{C}^{3} \times \mathfrak{h}_{\mathbb{C}} \rightarrow \mathfrak{h}_{\mathbb{C}}$. Furthermore, this is $\mathbb{C}^{*}$ equivariant, i.e. there is a weighted $\mathbb{C}^{*}$-action on $\mathbb{C}^{3}$ with weight $k=\left(k_{1}, k_{2}, k_{3}\right)$ and a $\mathbb{C}^{*}$-action $H_{(\alpha, \zeta)}: Y_{\zeta} \rightarrow$ $Y_{\alpha^{2} \zeta}$ extending the $\mathbb{R}_{>0}$-action above such that $\iota \circ H_{(\alpha, \zeta)}(y)=\alpha \cdot \iota(y)$ (the weight of the $\mathbb{C}^{*}$-action on $\mathfrak{h}_{\mathbb{C}}$ is 2) for any $y \in Y_{\zeta} \subset \mathcal{Y}$.
\end{itemize}

In the rest of the paper, we fix a differentiable manifold $Y$ which underlies $\widetilde{\mathbb{C}^{2} / \Gamma}$ and identify $Y_{\zeta}$ as $\left(Y, \Lambda_{\zeta}^{*} g_{\zeta}, \Lambda_{\zeta}^{*} I_{\zeta}, \Lambda_{\zeta}^{*} J_{\zeta}, \Lambda_{\zeta}^{*} K_{\zeta}\right)$ (under this identification, we simply write $\left.Y_{\zeta}=\left(Y, g_{\zeta}, I_{\zeta}, J_{\zeta}, K_{\zeta}\right)\right)$. In particular, for a family $\mathcal{Y}_{\left(0, \zeta_{c}\right)} \rightarrow \Delta$, the simultaneous resolution $\mathcal{Y}_{\zeta} \rightarrow \mathcal{Y}_{\left(0, \zeta_{c}\right)}$ given by (20) yields a natural trivialization
$$Y \times \Delta \cong \mathcal{Y}_{\zeta}$$
as families of differentiable manifolds induced by the fiberwise identification (14) (c.f. Theorem 4). Also, we regard $H_{(\alpha, \zeta)}$ as a $\mathbb{R}_{>0}$ action on $Y$ parameterized by $\zeta \in\left(\mathfrak{h} \otimes \mathbb{R}^{3}\right)^{o}$. We fix these identifications (namely, identifications from (14) to (25)) in the rest of the paper.

The next proposition plays an important role for the proof of the main result. We also use $r$ for the pull-back on $Y$ of the radius function $r(p)=d(0, p)$ of $\mathbb{C}^{2}$.

Lemma 1. Regard $Y_{\zeta}$ as a complex manifold by the complex structure $I_{\zeta}$. Then for any $\zeta$ varying in a compact subset in $\left(\mathfrak{h}_{\mathbb{R}} \otimes \mathbb{R}^{3}\right)^{o}$, the following hold:
\begin{itemize}
\item[-]
$$I_{\zeta}=I_{0}+\sum_{i=2}^{k-1} I_{\zeta}^{(i)} r^{-2 i}+O\left(r^{-2 k}\right)$$
as $r \rightarrow \infty$, where $I_{\zeta}^{(i)}$ is a matrix valued homogeneous polynomial in $\zeta$ of degree $i$ under the trivialization of the tangent bundle by the standard coordinate $\left(z_{0}, w_{0}\right)$ on $\mathbb{C}^{2} \backslash\{(0,0)\}$,
\item[-] there is a system of frames $\left\{e_{\zeta}^{1}, e_{\zeta}^{2}\right\}$ of $T^{(1,0)} Y_{\zeta}$ on $\{y \in Y \mid r \geq 1\}$ satisfying the following estimates:
$$\begin{gathered}
e_{\zeta}^{1}=\frac{\partial}{\partial z_{0}}+O\left(r^{-4}\right), e_{\zeta}^{2}=\frac{\partial}{\partial w_{0}}+O\left(r^{-4}\right) \\
\left(e_{\zeta}^{1}\right)^{*}=d z_{0}+O\left(r^{-4}\right),\left(e_{\zeta}^{2}\right)^{*}=d w_{0}+O\left(r^{-4}\right)
\end{gathered}$$
where $\left(e_{\zeta}^{i}\right)^{*}$ is the dual frame of $e_{\zeta}^{i}$.
\end{itemize}

Proof. Let
$$\left.I_{\zeta}\right|_{r=1}=I_{0}+\sum_{\nu} I_{\nu} \zeta^{\nu}$$
be the expansion on the unit sphere in $\mathbb{C}^{2}$ with respect to $\zeta$ ( $\nu$ is a multi-index). Then we have $I_{\zeta}=H_{r^{-1}}^{*}\left(I_{0}+\sum_{\nu} I_{\nu} \zeta^{\nu}\right)=I_{0}+I_{\zeta}^{(2)} r^{-2}+O\left(r^{-4}\right)$, where $I_{\zeta}^{(2)}=$ $\sum_{|\nu|=1} I_{\nu} \zeta^{\nu}$. By the estimates (17) and (18), we have uniform estimates
$$\begin{aligned}
g_{\zeta} & =g^{\mathrm{Euc}}+O\left(r^{-4}\right), \\
\omega_{I_{\zeta}} & =\omega^{\mathrm{Euc}}+O\left(r^{-4}\right)
\end{aligned}$$
on a compact subset of $\left(\mathfrak{h} \otimes \mathbb{R}^{3}\right)^{o}$. As the complex structure $I_{\zeta}$ is characterized by a equality
$$g_{\zeta}\left(I_{\zeta} u, v\right)=\omega_{I_{\zeta}}(u, v)$$
for any tangent vectors $u, v, I_{\zeta}$ satisfies the estimate
$$I_{\zeta}=I_{0}+\sum_{i=2}^{k-1} I_{\zeta}^{(i)} r^{-2 i}+O\left(r^{-2 k}\right)$$
as desired. For the second claim, take $e_{\zeta}^{i}$ to be
$$e_{\zeta}^{1}=\frac{1}{2}\left(\frac{\partial}{\partial z_{0}}-\sqrt{-1} I_{\zeta} \frac{\partial}{\partial z_{0}}\right), e_{\zeta}^{2}=\frac{1}{2}\left(\frac{\partial}{\partial w_{0}}-\sqrt{-1} I_{\zeta} \frac{\partial}{\partial w_{0}}\right) .$$
Then, $\left\{e_{\zeta}^{1}, e_{\zeta}^{2}\right\}$ is a frame of $T^{(1,0)} Y_{\zeta}$ on the domain and satisfies the estimates (27) and (28) by its construction and the estimate (26) of the complex structure $I_{\zeta}$. \(\square\)
2.2. Non-collapsing limits of Kähler-Einstein surfaces. Let $\left\{\left(X_{i}, g_{i}\right)\right\}_{i=1}^{\infty}$ be a sequence of $n$-dimensional Riemannian manifolds. When we consider its limit, it is necessary to assume some boundedness conditions for the sequence. If the diameters and the Ricci curvatures of $\left\{\left(X_{i}, g_{i}\right)\right\}_{i=1}^{\infty}$ are uniformly bounded and there exists a constant $C>0$ such that $\operatorname{Vol}_{g_{i}}(B(p, r))>C r^{n}$ for any $p \in X_{i}, r>0$, we call the sequence non-collapsing sequence and its limit (if it exists) non-collapsing limit. A non-collapsing limit of polarized Kähler-Einstein manifolds is a normal algebraic variety which has at worst klt singularities [10][11]. In dimension two, by Anderson[1], Bando[3], Bando-Kasue-Nakajima[4], and Nakajima[20], a non-collapsing limit of compact hyperkähler surfaces has at worst quotient singularities, and its bubbling limits at singularities are ALE of order 4:

Definition 2. Let $\left\{\left(X_{i}, g_{i}\right)\right\}_{i=1}^{\infty}$ be a sequence of Riemannian manifolds that converges to a metric space $\left(X_{\infty}, d_{\infty}\right)$ in the Gromov-Hausdorff sense. Then its bubbling limit at $x_{\infty} \in X_{\infty}$ is a limit of a sequence $\left\{\left(X_{i}, r_{i} g_{i}, x_{i}\right)\right\}$ in the pointed Gromov-Hausdorff sense (take a suitable subsequence if necessary) where $\left\{r_{i}\right\}$ is a divergent sequence of positive real numbers and $\left\{x_{i}\right\}$ is a sequence of points such that $x_{i} \in X_{i}$ and $x_{i} \rightarrow x_{\infty}$.

Theorem 5 ([1], [20] for (i), [4] for (ii) and [3] for (iii)). (i) Let $\left\{\left(X_{i}, g_{i}\right)\right\}$ be a sequence of real 4-dimensional compact Einstein manifolds such that diameters and $L^{2}$-energies $\int_{X_{i}}\left\|\mathrm{Rm}_{g_{i}}\right\|_{g_{i}}^{2} \operatorname{Vol}_{g_{i}}$ are uniformly bounded from above and volumes are uniformly bounded from below. Then the sequence $\left\{\left(X_{i}, g_{i}\right)\right\}$ contains a convergent subsequence that converges to an Einstein orbifold $\left(X_{\infty}, g_{\infty}\right)$ in the following sense: For any compact subset $K \subset X_{\infty}^{\text {reg }}, k>0$ and $\varepsilon>0$, there exists $N \in \mathbb{N}$ such
that for any $i>N$, we have open immersions $\chi_{i}: U_{i} \rightarrow X_{i}$, where $U_{i}$ are open neighborhoods of $K$ in $X_{\infty}^{\text {reg }}$ such that $\left\|g_{\infty}-\chi_{i}^{*} g_{i}\right\|_{C^{k}(K)}<\varepsilon$.
\begin{itemize}
\item[(ii)] Let $\left\{\left(X_{i}, g_{i}\right)\right\}$ be a sequence of 4-dimensional Einstein manifolds with uniformly bounded diameters, $\int_{X_{i}}\left\|\mathrm{Rm}_{g_{i}}\right\|^{2} \operatorname{Vol}_{g_{i}}$ and volumes, which converges to an Einstein orbifold $\left(X_{\infty}, g_{\infty}\right)$. Then the set of isometric classes of bubbling limits at a singularity $x \in X_{\infty}$ is a finite set. Furthermore, if the sequence $\left\{\left(X_{i}, g_{i}\right)\right\}$ consists of Kähler (hyperkähler) manifolds, then $\left(X_{\infty}, g_{\infty}\right)$ is a Kähler (resp. hyperkähler) orbifold.
\item[(iii)] Under the same assumption as in (ii), one has the following formula:
$$\lim _{i \rightarrow \infty}\left\|\mathrm{Rm}_{g_{i}}\right\|^{2} \operatorname{Vol}_{g_{i}} \geq\left\|\mathrm{Rm}_{g_{\infty}}\right\|^{2} \operatorname{Vol}_{g_{\infty}}+\sum_{x \in X_{\infty}^{s i n g}} h_{x} \delta_{x}$$
as measures, where
$$\begin{aligned}
h_{x} & =\sum_{(M, g): b u b b l i n g \text { at } x} e_{\mathrm{orb}}(M), \\
e_{\mathrm{orb}}(M) & =\frac{1}{8 \pi^{2}} \int_{M}\left\|\mathrm{Rm}_{g}\right\|^{2} \operatorname{Vol}_{g} .
\end{aligned}$$
and $\delta_{x}$ is the Dirac measure at $x$. The precise meaning of the above limit is the following:
For any sequence $\left\{f_{i}\right\}$ of smooth functions $f_{i} \in C^{\infty}\left(X_{i}\right)$ that converges to a smooth function $f_{\infty}$ on $X_{\infty}$ (the convergence is defined by the completely same manner as in (i)),
$$\lim _{i \rightarrow \infty} \int_{X_{i}} f_{i}\left\|\mathrm{Rm}_{g_{i}}\right\|^{2} \operatorname{Vol}_{g_{i}} \geq \int_{X_{\infty}} f_{\infty}\left\|\mathrm{Rm}_{g_{\infty}}\right\|^{2} \operatorname{Vol}_{g_{\infty}}+\sum f_{\infty}(x) h_{x}$$
\end{itemize}
2.3. Biquard-Rollin's a priori estimate. In this section, we recall Biquard-Rollin's a priori estimate [7] for constant scaler curvature Kähler metrics (or, cscK-metrics for short) on a degenerating family of surfaces.

Set-ups: Let $\left(X_{0}, g_{0}\right)$ be a pair consisting of compact complex surface $X_{0}$ with ADE singularities and a cscK orbifold metric $g_{0}$ on $X_{0}$. Let $\omega_{0}$ denote the Kähler form of $g_{0}$. In order to state the a priori estimate, we need to define the notion of a non-degenerate smoothing of $\left(X_{0}, g_{0}\right)$ (this non-degeneracy condition is a terminology used only [7], not generally used). Let $\mathcal{X} \rightarrow \Delta$ be a flat deformation of $X_{0}$ over the unit disc of the complex plane. Assume that the fibers $X_{t}$ are smooth for $t \in \Delta^{*}=\Delta \backslash\{0\}$. Take a family of Kähler classes $\left\{\kappa_{t}\right\}_{t \in \Delta}$ such that:
\begin{itemize}
\item[-] $\kappa_{t}$ is a Kähler class on $X_{t}$,
\item[-] On a minimal simultaneous resolution $\widetilde{\mathcal{X}} \rightarrow \Delta_{d}$ with a suitable base change
$$\begin{aligned}
\Delta_{d} & \rightarrow \Delta \\
t & \mapsto t^{d},
\end{aligned}$$
the pull-back of $\left\{\kappa_{t}\right\}$ on $\widetilde{\mathcal{X}}$ defines a smooth curve in $H^{2}(X, \mathbb{R})$ converging to the pull-back of $\left[\omega_{0}\right]=: \kappa_{0}$, where $X$ is the differentiable manifold underlying the fibers of $\widetilde{\mathcal{X}} \rightarrow \Delta_{d}$. Here, $\Delta_{d}$ is also the unit disc in $\mathbb{C}$ and we use the subscript " $d$ " to distinguish the original family and its base change.
\end{itemize}
For each singularity $\left(x \in X_{0}\right) \cong\left(0 \in \mathbb{C}^{2} / \Gamma\right)$, by restricting the given family to a suitable neighbourhood $\mathcal{U}$ of $x \in \mathcal{X}$, we have a flat deformation of the ADE
singularity $x$. Hence we have a holomorphic map $\phi: \Delta \rightarrow \mathfrak{h}_{\mathbb{C}} / W$, where $\mathfrak{h}_{\mathbb{C}}$ is the complexification of the Cartan sub-algebra and $W$ is the Weyl group corresponding to $\Gamma$. Let $\pi: \mathcal{U}_{d} \rightarrow \Delta_{d}$ be the family obtained from $\mathcal{U} \rightarrow \Delta$ by the base-change $\Delta_{d} \rightarrow \Delta$, the ramified covering of degree $d$ ramified at the origin. Again, the family $\mathcal{U}_{d} \rightarrow \Delta_{d}$ is induced by a holomorphic map $\psi: \Delta_{d} \rightarrow \mathfrak{h}_{\mathbb{C}} / W$. Then, by the theory of deformations of ADE singularities, we have a holomorphic map
$$\zeta_{c}: \Delta_{d} \rightarrow \mathfrak{h}_{\mathbb{C}}$$
such that the following diagram is commutative:
![](https://cdn.mathpix.com/cropped/5560a88a-8112-4d9d-a6b3-3db74de545fb-10.jpg?height=200&width=291&top_left_y=785&top_left_x=916)
Here, the morphism $\Delta_{d} \rightarrow \Delta$ is the ramified covering from the unit disc to itself of degree d and the composition $\Delta_{d} \rightarrow \mathfrak{h}_{\mathbb{C}} \rightarrow \mathfrak{h}_{\mathbb{C}} / W$ is equal to $\psi$. The family $\mathcal{U}_{d} \rightarrow \Delta_{d}$ admits the minimal simultaneous resolution $\tilde{\pi}: \widetilde{\mathcal{U}} \rightarrow \Delta_{d}$. We may define a smooth map $\zeta_{r}: \Delta_{d} \rightarrow \mathfrak{h}_{\mathbb{R}}$ by $\zeta_{r}(t)=\left.\kappa_{t}\right|_{\widetilde{U}_{t}}$ under a suitable identification $H^{2}\left(\widetilde{U}_{t}, \mathbb{R}\right) \cong \mathfrak{h}_{\mathbb{R}}$, where $\widetilde{U}_{t}$ is the fiber of $\widetilde{\mathcal{U}}$ on $t \in \Delta_{d}$ (Note that $R^{2} \tilde{\pi}_{*} \mathbb{R}$ is trivial on $\Delta_{d}$ and is identified with the constant sheaf with stalk $\mathfrak{h}_{\mathbb{R}}$. See also Theorem 4).

Definition 3. In the same situation as above, the family $\left(\mathcal{X} \rightarrow \Delta,\left\{\kappa_{t}\right\}\right)$ is non-degenerate at $x$ along a real ray $\Delta_{d} \cap \mathbb{R}_{\geq 0}$ if $\zeta=\zeta_{r} \oplus \zeta_{c}: \Delta_{d} \rightarrow \mathfrak{h}_{\mathbb{R}} \oplus \mathfrak{h}_{\mathbb{C}}$ satisfies the following condition: as $\zeta(0)=0$, we can express
$$\zeta(t)=t^{p} \dot{\zeta}+O\left(t^{p+1}\right)$$
with $\dot{\zeta} \neq 0$. Then $\dot{\zeta} \in\left(\mathfrak{h}_{\mathbb{R}} \otimes \mathbb{R}^{3}\right)^{o}$ (cf. (10)) and $p \leq d$.
Example 1. For a given family $\left(\mathcal{X} \rightarrow \Delta,\left\{\kappa_{t}\right\}\right)$, assume that the central fiber $X_{0}$ has an $A_{n}$ type singularity $x \in X$. Then its flat deformation given by a suitable open neighborhood $\mathcal{U} \rightarrow \Delta$ is isomorphic to an open subset of
$$\left\{x y+z^{n+1}+a_{2}(t) z^{n-1}+\cdots+a_{n+1}(t)=0\right\} \subset \mathbb{C}_{(x, y, z)}^{3} \times \Delta$$
where $a_{i}(t)$ are analytic in $t$. Furthermore, $\mathcal{U}_{d} \rightarrow \Delta_{d}$ is isomorphic to an open subset of
$$\left\{x y+\prod_{i=1}^{n+1}\left(z-h_{i}(t)\right)=0\right\} \subset \mathbb{C}_{(x, y, z)}^{3} \times \Delta_{d}$$
where $h_{i}$ are analytic in $t$. For the family $\mathcal{U}_{d} \rightarrow \Delta_{d}$, we have
$$\zeta_{c}(t)=\left(h_{1}(t), \ldots, h_{n+1}(t)\right) \in \mathfrak{h}_{\mathbb{C}} .$$
For simplicity, take a family of Kähler classes such that $\zeta_{r} \in \mathfrak{h}_{\mathbb{R}}$ is identically zero (for example, take $\left(\mathcal{X} \rightarrow \Delta,\left\{\kappa_{t}\right\}\right)$ consisting of a family of K3 surfaces and the first Chern classes of an ample line bundle $\mathcal{L}$ on $\mathcal{X}$ and restrict the family to a suitable neighborhood $\mathcal{U}$ of a singularity $x \in X_{0}$ ). Then, the family is non-degenerate if and only if $\zeta_{c}(t)=t^{p}\left(\dot{h}_{1}(t), \ldots, \dot{h}_{n+1}(t)\right)$ with $p \leq d$ and $\left(\dot{h}_{1}(0), \ldots, \dot{h}_{n+1}(0)\right) \notin \bigcup_{i<j} H_{e_{i},-e_{j}}$, where $H_{e_{i}-e_{j}}$ is the hyperplane orthogonal to $e_{i}-e_{j}=(0, \ldots, \stackrel{i}{1}, \ldots,-1, \ldots, 0)$.

Let $\left(\mathcal{X} \rightarrow \Delta,\left\{\kappa_{t}\right\}\right)$ be a non-degenerate family. We construct a family of almost cscK-metrics as follows:
For simplicity, we assume that $X_{0}$ has only one singularity $\left(x \in X_{0}\right) \cong\left(0 \in \mathbb{C}^{2} / \Gamma\right)$. Take a diffeomorphism $\widetilde{\mathcal{X}} \cong X \times \Delta_{d}$ as families and let $J_{t}$ be the complex structure of $\tilde{X}_{t}$ (the fibre of $\tilde{\mathcal{X}}$ on $t$ ) such that $\tilde{X}_{t}=\left(X, J_{t}\right)$. Take a suitable open neighbourhood $x \in \mathcal{U} \subset \mathcal{X}$ with the following properties:
\begin{itemize}
\item[-] The central fiber $U_{0}$ of the family $\mathcal{U} \rightarrow \Delta$ admits a uniformization
$$q: \mathrm{B}(0 ; 1) \rightarrow U_{0}$$
on the unit ball $\mathrm{B}(0 ; 1)$ of $\mathbb{C}^{2}$ such that the standard coordinate $(z, w)$ is a normal coordinate with respect to $q^{*} g_{0}$, i.e. $q^{*} g_{0}=g^{\text {Euc }}+O\left(r^{2}\right)$ under this coordinate,
\item[-] $\mathcal{U} \rightarrow \Delta$ induces a smooth map $\zeta: \Delta_{d} \rightarrow \mathfrak{h}_{\mathbb{R}} \oplus \mathfrak{h}_{\mathbb{C}}$ as we described above (cf. (33) and Definition 3).
\item[-] The simultaneous resolution $\widetilde{\mathcal{X}} \rightarrow \mathcal{X}_{d}$ is induced by an embedding $\iota: \mathcal{U}_{d} \rightarrow$ $\mathcal{Y}_{\left(0, \zeta_{c}\right)}$ and the simultaneous resolution $\mathcal{Y}_{\left(\zeta_{0}, \zeta_{c}\right)} \rightarrow \mathcal{Y}_{\left(0, \zeta_{c}\right)}$ for some $\zeta_{0}$ which is not perpendicular to any root (cf. (20)).
\item[-] Let $U=\{y \in Y \mid r(y)<1\}$ be the pull-back of the unit disc $\Delta^{2} / \Gamma \subset \mathbb{C}^{2} / \Gamma$ by the resolution $Y \rightarrow \mathbb{C}^{2} / \Gamma$. Note that $U$ is naturally identified with an open subset of $X$. Then, the trivialization $\widetilde{\mathcal{X}} \cong X \times \Delta_{d}$ induces
$$\widetilde{\mathcal{U}} \cong U \times \Delta_{d}$$
as $C^{\infty}$ family. Recall that $r$ is the radius function on $Y$ (see section 2.1).
\end{itemize}

In the following, we identify $\mathcal{U}_{d}$ as an open subset of $\mathcal{Y}_{\left(0, \zeta_{c}\right)}, U \subset X$ as an open subset of $Y$ and we fix the trivializations of $\widetilde{\mathcal{X}}$ and $\widetilde{\mathcal{U}}$. Furthermore, by suitable rescaling or taking $\mathcal{U}$ sufficiently small if necessary, we assume that $U \subset Y$ satisfies that $U=\{y \in Y \mid r(y)<1\}$.

Under the above preparations, we construct a family of $J_{t}$-Hermitian metrics $h_{t}$ on $X_{t}=\left(X, J_{t}\right)$ parameterized by $t \in(0,1)$. For simplicity, we restrict the family along a real ray in $\Delta_{d}$ through the origin (hence identify a real number $t$ with a complex number $z=t e^{i \theta} \in \Delta_{d}$ with a fixed argument $\left.\theta\right)$. We introduce some parameters to construct metrics:
$$b=\varepsilon^{\beta}=t^{p \beta / 2}$$
where $\beta>\frac{1}{2}$ is any real number sufficiently close to 1/2, and $p$ is the order of vanishing of $\zeta$ at $0 \in \Delta_{d}$ (see (34)). Following Biquard-Rollin [7], we construct a family of Riemannian metrics $\tilde{h}_{t}$ on X by
$$\tilde{h}_{t}=\left\{\begin{array}{cc}
g_{0} & 4 b \leq r, \text { or on } X \backslash U \\
d d_{0}^{c}\left(r^{2}+\chi_{(2 b, 4 b)}(r) \eta\right) & 2 b \leq r \leq 4 b \\
d d_{0}^{c} r^{2}+\left(1-\chi_{(b, 2 b)}(r)\right) \varepsilon^{2} H_{\left(\varepsilon^{-1}, \zeta(t)\right)}^{*} \xi_{t} & b \leq r \leq 2 b \\
g_{\zeta(t)} & r \leq b
\end{array}\right.$$
where $g_{0}=d d_{0}^{c}\left(r^{2}+\eta\right)$ on the uniformization $\mathrm{B}(0 ; 1), g_{\varepsilon^{-2} \zeta(t)}=($ Euc.$)+\xi_{t}$ as $r \rightarrow \infty$ on $Y_{\zeta / \varepsilon^{2}}, d_{t}^{c}$ is the $d^{c}$ operator with respect to $J_{t}$ and $\chi_{x_{1}, x_{2}}(x): \mathbb{R} \rightarrow \mathbb{R}$ is a cut-off function defined by
$$\chi_{x_{1}, x_{2}}(x)=\chi\left(\frac{x-x_{1}}{x_{2}-x_{1}}\right)$$
for $\chi$, a non-deceasing and non-negative smooth function identically 0 on $x \leq 0$ and 1 on $1 \leq x$. Then the Hermitian metric $h_{t}$ on $T \tilde{X}_{t}$ is defined by
$$h_{t}(u, v)=\frac{\tilde{h}_{t}\left(J_{t} u, J_{t} v\right)+\tilde{h}_{t}(u, v)}{2} .$$
They are not Kähler in general. However, by Biquard-Rollin[7], we can find a Kähler metric $g_{t}$ in $\kappa_{t}$ sufficiently close to $h_{t}$.

Definition 4 ([7] Section 3.3). A weighted Hölder norm $\|\cdot\|_{C_{\delta}^{k, \alpha}\left(X, h_{t}\right)}$ on $X$ with respect to $h_{t}$ is defined as follows:
Takw a family of weight functions $\rho_{t}$ on $X$ so that
$$\rho_{t}=\left\{\begin{array}{cc}
\text { positive and smooth } & 1 \leq r \\
r & \varepsilon \leq r \leq 1 \\
\varepsilon & r \leq \varepsilon
\end{array} .\right.$$
Using it, the weighted $C_{\delta}^{k, \alpha}$-Hölder norm on $\left(X, h_{t}\right)$ is defined as
$$\|f\|_{C_{\delta}^{k, \alpha}\left(X, h_{t}\right)}:=\sum_{j=0}^{k} \sup \left|\rho_{t}^{j-\delta} \nabla^{j} f\right|_{h_{t}}+\left\|\rho_{t}^{k+\alpha-\delta} \nabla^{k} f\right\|_{\alpha},$$
where $\|\cdot\|_{\alpha}$ is the Hölder coefficient with exponent $\alpha$, i.e.
$$\|\phi\|_{\alpha}=\sup _{x \neq y} \frac{\|\phi(x)-\phi(y)\|_{h_{t}}}{d_{h_{t}}(x, y)^{\alpha}} .$$
Note that these norms are independent of the choice of $\rho_{t}$ up to equivalence of norms.

Proposition 1 ([7] Corollary 27. Proposition 30.). For the family of Hermitian metrics $\left\{h_{t}\right\}_{0<t<1}$ constructed above, there exists a family of Kähler metrics $\left\{g_{t}\right\}_{0<t<1}$ with Kähler classes $\left\{\kappa_{t}\right\}_{0<t<1}$ such that
$$\left\|h_{t}-g_{t}\right\|_{C_{\delta, t}^{2, \alpha}}=O\left(\varepsilon^{2}\right),$$
for any $\delta \in(-2,0)$ sufficiently close to -2.
The following a priori estimate of Biquard-Rollin plays an essential role in this paper:

Theorem 6 ([7] Corollary 35). Let $\left(\mathcal{X},\left\{\kappa_{t}\right\}\right)$ be a non-degenerate family with discrete $\operatorname{Aut}\left(X_{0}\right)$. For simplicity, we assume that $X_{0}$ admits only one singularity $x_{0}$. Let $\left\{g_{t}\right\}$ be the family of Kähler metrics as in Proposition 1. Then for any $t \neq 0$, there exists a unique cscK metric $g_{t}+d d_{t}^{c} \phi_{t}$ on $\tilde{X}_{t}(t \neq 0)$ with the following estimate:
$$\left\|\phi_{t}\right\|_{C_{\delta+2, t}^{4, \alpha}} \leq C \varepsilon^{2-\beta(\delta+2)}$$
where $\delta \in(-2,0)$ is any number sufficiently close to $-2, \beta=\frac{2}{2-\delta}>\frac{1}{2}$ and $C$ is a constant independent of $t$.

\section*{3. Main results}

In this section, we study behavior of the second Chern forms of cscK metrics on a family of complex surfaces. In particular, we prove its regularity as a current on the relative tangent bundle for a non-degenerate smoothing of an orbifold cscK metric with ADE singularity. Namely, for a smoothing family $\left(\mathcal{X},\left\{\kappa_{t}\right\}\right) \rightarrow \Delta$ of a complex surface $\left(X_{0}, g_{0}\right)$, we consider a function $F(t):=\left.\int_{X_{t}} f\right|_{X_{t}} c_{2}\left(g_{t}\right)$ on $\Delta$. Then, our main result is the following theorem.

Theorem 7. Let $\left(\mathcal{X} \rightarrow \Delta, \kappa_{t}\right)$ be a smoothing holomorphic proper family of compact orbifold cscK surface $\left(X_{0}, \omega_{0}\right)$ with ADE-singularities and $\operatorname{Aut}\left(X_{0}\right)$ discrete, and $f$ be a smooth function on $\mathcal{X}$ with compact support around $x_{0} \in X_{0} \cong 0 \in \mathbb{C}^{2} / \Gamma$. Assume that the family admits a simultaneous resolution $\widetilde{\mathcal{X}} \rightarrow \Delta_{d}$ after taking a base change by the ramified covering $\Delta_{d} \rightarrow \Delta$ of degree $d$ and it is non-degenerate at $x_{0}$ along a real ray $\Delta \cap(0,1)$. Consider a function
$$F(t)=\int_{X_{t}} f_{t} c_{2}\left(\hat{g}_{t}\right)$$
on $\Delta \cap(0,1)$, where $\hat{g}_{t}$ is the cscK metric on $X_{t}$ with its Kähler class $\kappa_{t}, c_{2}\left(\hat{g}_{t}\right)$ is the second Chern form of $\hat{g}_{t}$ on $T X_{t}$ and $f_{t}=\left.f\right|_{X_{t}}$. Then $F$ extends to a Hölder continuous function on $\Delta \cap[0,1)$ with Hölder exponent at least $\frac{1}{d}$.

We use the Biquard-Rollin's construction to describe $\hat{g}_{t}$. Recall that we have families of Hermitian metrics $h_{t}$, Kähler metrics $g_{t}$, and cscK metrics $\hat{\omega}_{t}=\omega_{t}+d d_{t}^{c} \phi_{t}$ with the following estimates along a real ray in $\Delta_{d}$ (see proposition 1 and theorem 6 in section 2.3):
$$\begin{aligned}
\left\|h_{t}-g_{t}\right\|_{C_{\delta, t}^{2, \alpha}} & =O\left(\varepsilon^{2}\right) \\
\left\|\phi_{t}\right\|_{C_{\delta+2, t}^{4, \alpha}} & =O\left(\varepsilon^{2-\beta(\delta+2)}\right) .
\end{aligned}$$

As $h_{t}$ and $\hat{g}_{t}$ are hermitian metrics on the same holomorphic vector bundle $T X_{t}$, we have the following equality by the Bott-Chern formula:
$$c_{2}\left(\hat{g}_{t}\right)=c_{2}\left(h_{t}\right)+d d_{t}^{c} \tau,$$
where $\tau$ is an explicitly given $(1,1)$ form (whose explicit description will be given later, see (83)). By (48) and the Stokes theorem, we can express $F$ as
$$F(t)=\int_{X_{t}} f_{t} c_{2}\left(\hat{g}_{t}\right)=\int_{X_{t}} f_{t} c_{2}\left(h_{t}\right)+\int_{X_{t}} d d_{t}^{c} f_{t} \wedge \tau .$$
Then, in the rest of the proof, we consider the two integrals
$$\int_{X_{t}} f_{t} c_{2}\left(h_{t}\right)$$
and
$$\int_{X_{t}} d d_{t}^{c} f_{t} \wedge \tau .$$

For the second integral (51), as $f$ is an arbitrary smooth function with compact support, it is sufficient to study an integral
$$\int_{X_{t}} \sigma_{t} \wedge \tau$$
for an arbitrary smooth (1, 1)-form $\sigma$ on $\mathcal{X}$ with compact support (i.e. a compactly supported smooth 2-form on the total space $\mathcal{X}$ such that its restrictions on fibers $X_{t}=\left(X, J_{t}\right)$ are (1, 1)-forms with respect to $J_{t}$ ). Here, smooth form on a singular analytic space is by definition a smooth form defined on $\mathcal{X}^{\text {reg }}$ which is a pullback by an embedding into the Euclidean space around a singularity. As in the construction of $h_{t}, g_{t}$ and $\phi_{t}$, we fix a ramified covering $\Delta_{d} \rightarrow \Delta$, a simultaneous resolution $\widetilde{\mathcal{X}} \rightarrow \mathcal{X}$ and an open neighbourhood $\mathcal{U} \ni x_{0}$ (see section 2.3 for precise description). Then, by considering the pull-back of $F$ on $\Delta_{d}$, the integrals can be expressed as integrals on $X$. We divide the integrals into five parts, integrals on the following five domains:
$$X=(X \backslash U) \cup U_{r \leq b} \cup U_{b \leq r \leq 2 b} \cup U_{2 b \leq r \leq 4 b} \cup U_{4 b \leq r \leq 1},$$
where
$$U_{r \leq b}=\{x \in U \mid r(x) \leq b\}$$
and the others are defined similarly.
![](https://cdn.mathpix.com/cropped/5560a88a-8112-4d9d-a6b3-3db74de545fb-14.jpg?height=895&width=1223&top_left_y=1223&top_left_x=446)

Division of domains.
Recall that $U$ is diffeomorphic to the minimal resolution of a suitable open neighbourhood of $x_{0} \in X_{0}$ with $r<1$ (see section 2.3). Let $\tilde{f}$ be the pull-back of $f$ on $\widetilde{\mathcal{X}}$ and $\tilde{f}_{t}$ be its restriction to $X \times\{t\}$.
Lemma 2. $\int_{X \backslash U} \tilde{f}_{t} c_{2}\left(h_{t}\right)=\int_{X \backslash U} \tilde{f}_{0} c_{2}\left(g_{0}\right)+O\left(t^{d}\right)$.

Proof. Recall that $\tilde{h}_{t}=g_{0}$ on $X \backslash U$. As $\left\|J_{0}-J_{t}\right\|=O\left(t^{d}\right)$ on the domain, we have $h_{t}=g_{0}+O\left(t^{d}\right)$. Then, $c_{2}\left(h_{t}\right)=c_{2}\left(g_{0}\right)+O\left(t^{d}\right)$. As $f$ is a smooth function on $X \times \Delta_{d}$, we have an expansion $\tilde{f}_{t}(z)=\tilde{f}_{0}(z)+\dot{f}_{0}(z) t^{d}+O\left(t^{2 d}\right)$ by Taylor's theorem with respect to $t$ (note that the family $\mathcal{X} \backslash \mathcal{U} \rightarrow \Delta$ admits a local trivialization near the origin $t=0$ as it is a family of smooth manifolds with boundaries). Then we have
$$\begin{aligned}
\int_{X \backslash U} \tilde{f}_{t} c_{2}\left(h_{t}\right) & =\int_{X \backslash U}\left(\tilde{f}_{0}+\dot{f}_{0} t^{d}+O\left(t^{2 d}\right)\right)\left(c_{2}\left(g_{0}\right)+O\left(t^{d}\right)\right) \\
& =\int_{X \backslash U} \tilde{f}_{0} c_{2}\left(g_{0}\right)+O\left(t^{d}\right) .
\end{aligned}$$ \(\square\)

Recall that $\mathcal{U}_{d} \rightarrow \Delta_{d}$ can be embedded into a family $\mathcal{Y}_{\left(0, \zeta_{c}\right)} \rightarrow \Delta_{d}$ whose fiber on $t \in \Delta_{d}$ is $Y_{\left(0, \zeta_{c}(t)\right)}$ by the construction of $\mathcal{U}$. In particular, $U_{t}=\left(U, J_{t}\right)$ can be identified with an open subset of $Y_{\left(0, \zeta_{c}(t)\right)}=\left(Y, I_{\left(0, \zeta_{c}(t)\right)}\right)$ such that $U=\{y \in Y \mid$ $r<1\}$ for $t \neq 0$. Under this identification, regard the local frame $\left\{e_{\zeta(t)}^{1}, e_{\zeta(t)}^{2}\right\}$ of Lemma 1 to be vector fields defined on $U$ (parameterized by $t$ ). In the rest of this section, we fix this identification. Also, note that we have a trivialization of $\mathcal{Y}_{\zeta}=\mathcal{Y}_{\left(\zeta_{0}, \zeta_{c}\right)}$ (hence, that of $\widetilde{\mathcal{U}}$ ) in (25), where $\zeta_{0} \in \mathfrak{h}_{\mathbb{R}}$ is any fixed vector which is not perpendicular to any root.

For an analysis of $\int_{U_{t}} \tilde{f}_{t} c_{2}\left(h_{t}\right)$, it is sufficient to study its pull-back by $H_{\left(\varepsilon, \zeta(t) / \varepsilon^{2}\right)}$. Namely, we investigate $\int_{Y_{r \leq 1 / \varepsilon}} H_{\left(\varepsilon, \zeta(t) / \varepsilon^{2}\right)}^{*}\left(\tilde{f}_{t}\right) H_{\left(\varepsilon, \zeta(t) / \varepsilon^{2}\right)}^{*}\left(c_{2}\left(h_{t}\right)\right)$ in the following. For $H_{\left(\varepsilon, \zeta(t) / \varepsilon^{2}\right)}^{*}\left(\tilde{f}_{t}\right)$, we have the following lemma.

Lemma 3. $H_{\left(\varepsilon, \zeta(t) / \varepsilon^{2}\right)}^{*}\left(\tilde{f}_{t}\right)=f\left(x_{0}\right)+O\left(\varepsilon^{k} r^{k}\right)$ on $Y_{r \leq 1 / \varepsilon}$ as $t \rightarrow 0$, where $k$ is an integer determined by the singularity and is greater than or equal to 2.

Proof. Let $\mathcal{Y}_{\left(0, \zeta_{c}\right)} \rightarrow \Delta_{d}$ be the analytic family defined by $\zeta_{c}: \Delta_{d} \rightarrow \mathfrak{h}_{\mathbb{C}}$ (see section 2.1). Then, by the general theory of deformations of ADE singularities, we have an embedding $\iota_{\zeta}: \mathcal{Y}_{\zeta} \rightarrow \mathbb{C}^{3} \times \Delta_{d}$ induced by the embedding $\iota: \mathcal{Y} \rightarrow \mathbb{C}^{3} \times \mathfrak{h}_{\mathbb{C}}$ (see also (24)). Assume that $\iota_{\zeta}$ maps the singularity $x_{0} \in Y_{(0,0)} \cong 0 \in \mathbb{C}^{2} / \Gamma$ to the origin: $\iota_{\zeta}\left(x_{0}\right)=(0,0)$. This embedding induces the following commutative diagram:
![](https://cdn.mathpix.com/cropped/5560a88a-8112-4d9d-a6b3-3db74de545fb-15.jpg?height=184&width=317&top_left_y=1892&top_left_x=902)
where $\mathbb{C}^{3} \times \Delta_{d} \rightarrow \mathbb{C}^{3} \times \Delta$ is given by $(x, t) \mapsto\left(x, t^{d}\right)$. As $f$ is a smooth function on $\mathcal{U}$, we have an extension $\mathfrak{f}$ of $f$ on $\mathbb{C}^{3} \times \Delta$. Let $\mathfrak{f}=F_{0}(x)+F_{1}(x) t+O\left(t^{2}\right)$ be the Taylor expansion with respect to $t$ along a real ray $\Delta \cap \mathbb{R}$. Then, by the commutative diagram (54), the pull-back of $f$ on $\left.\mathcal{U}_{d}\right|_{\Delta_{d} \cap(0,1)}$ is given by the restriction of
$$F_{0}(x)+F_{1}(x) t^{d}+O\left(t^{2 d}\right)$$
on $\left.\mathcal{U}_{d}\right|_{\Delta_{d} \cap(0,1)}$. We will show that $\left|\iota_{\zeta}(y)\right|=O\left(r^{k}\right)$ for sufficiently small $t$, where $k=\max \left\{k_{1}, k_{2}, k_{3}\right\} \geq 2$ is the weight of the weighted $\mathbb{C}^{*}$ action on $\mathbb{C}^{3}$ (see section
2.1 and [24] section 2.5 for details and their explicit values). In fact, $\left|\iota_{\zeta}(y)\right|=O\left(r^{k}\right)$ for $y \in \mathcal{Y}_{\zeta(0)}$ by its explicit form of embedding. For instance, if $\Gamma$ is the cyclic group of order $n$ (i.e. $A_{n-1}$-type case), $\mathbb{C}^{2} / \Gamma$ can be embedded into $\mathbb{C}^{3}$ by
$$\begin{aligned}
\mathbb{C}^{2} & \rightarrow \mathbb{C}^{3} \\
(u, v) & \mapsto\left(u^{n}, v^{n}, u v\right)
\end{aligned}$$
and the weight $k=\left(k_{1}, k_{2}, k_{3}\right)$ is $(n, n, 2)$, see [24] for $D_{n}$ and $E_{n}$ cases. For $y \in Y_{\zeta(t)}, t \neq 0$, if $r(y)=\alpha>1$, consider $y^{\prime}=H_{(1 / \alpha, \zeta)}(y) \in Y_{\zeta(t) / \alpha^{2}}$ which satisfies $r\left(y^{\prime}\right)=1$. Then, as $\iota$ is $\mathbb{R}_{>0}$ equivariant (cf. (24)), we have $\iota_{\zeta}(y)=$ $\iota_{\zeta}\left(H_{\left(\alpha, \zeta / \alpha^{2}\right)}\left(y^{\prime}\right)\right)=\alpha \cdot \iota_{\zeta / \alpha^{2}}\left(y^{\prime}\right)$, where $\iota_{\zeta / \alpha^{2}}: \mathcal{Y}_{\zeta / \alpha^{2}} \rightarrow \mathbb{C}^{3} \times \Delta_{d}$ is the embedding induced by $\zeta / \alpha^{2}: \Delta_{d} \rightarrow \mathfrak{h}_{\mathbb{C}}$. As $\bigcup_{\alpha>1} \iota_{\zeta / \alpha^{2}}(\{r \leq 1\})$ is relatively compact in $\mathbb{C}^{3} \times \Delta_{d}$, $\sup _{\alpha \leq 1, r(y)=1}\left|\iota_{\zeta / \alpha^{2}}(y)\right|$ is bounded. Therefore, we have $\left|\iota_{\zeta}(y)\right|=O\left(r^{k}\right)$. By the Taylor expansion of $F_{0}$, we have the following estimate for $f^{(d)}$, the pull-back of $f$ on $\mathcal{U}_{d}$,
$$f^{(d)}=F_{0}(0)+O\left(r^{k}\right)+O\left(r^{k}\right) t^{d}+O\left(t^{d}\right) .$$
In particular, $\tilde{f}$, the pull back of $f^{(d)}$ on $\tilde{\mathcal{U}}$, also satisfies the estimate (56). Therefore, we have
$$H_{\left(\varepsilon, \zeta / \varepsilon^{2}\right)}^{*}(\tilde{f})=f\left(x_{0}\right)+O\left(\varepsilon^{k} r^{k}\right) .$$ \(\square\)

The next lemma is also important for our analysis.
Lemma 4. $H_{\left(\varepsilon, \zeta / \varepsilon^{2}\right)}^{*}\left(\tilde{f}_{t}\right)=H_{\left(\varepsilon, \zeta / \varepsilon^{2}\right)}^{*}\left(\tilde{f}_{0}\right)+O(t)$ on $Y_{1<r<1 / \varepsilon}$.
Proof. Consider the composition
$$\Phi: U \times \Delta_{d} \rightarrow \tilde{\mathcal{U}} \rightarrow \mathcal{U}_{d} \rightarrow \mathbb{C}^{3} \times \Delta_{d},$$
where the trivialization $U \times \Delta_{d} \rightarrow \tilde{\mathcal{U}}$ is induced by the trivialization $Y \times \Delta_{d} \cong$ $\mathcal{Y}_{\left(\zeta_{0}, \zeta_{c}\right)}$ (cf. (25)) and the map $\mathcal{U}_{d} \rightarrow \mathbb{C}^{3} \times \Delta_{d}$ is given by $\iota_{\zeta}$. Let $\Phi(u, t)=(x(u, t), t)$. Then, by (55), $\tilde{f}$ can be represented as follows:
$$F_{0}(x(u, 0))+l(\dot{x}(u, 0)) t+O\left(t^{2}\right),$$
where $l$ is a linear form and $\dot{x}(u, 0)$ is the derivative with respect to $t$. Note that $F_{0}(x(u, 0))=\tilde{f}_{0}$. And, as $x(u, t)$ is a restriction of a smooth function on $Y$ (parameterized by $t$ smoothly) to $U,|\dot{x}(u, 0)|$ is bounded on $r<1$ i.e. on $U \subset Y$ (hence, its pull back by $H_{\left(\varepsilon, \zeta / \varepsilon^{2}\right)}$ is also bounded on $r<1 / \varepsilon$ ). Therefore we have the desired estimate. \(\square\)

By these lemmas, we can derive estimates of the first integral of (49) on $U$.
Lemma 5. $\int_{Y_{4 b \leq r \leq 1}} \tilde{f}_{t} c_{2}\left(h_{t}\right)=\int_{Y_{4 b \leq r \leq 1}} \tilde{f}_{0} c_{2}\left(g_{0}\right)+O(t)$.
Proof. Recall that $\tilde{h}_{t}=g_{0}$ on $U_{4 b \leq r \leq 1}$, and then $\tilde{h}_{t}$ is $I_{0}$-Hermitian on this domain. As the coordinate $\left(z_{0}, w_{0}\right)$ is $g_{0}$-adapted, we have
$$g_{0}=g^{\mathrm{Euc}}+O\left(r^{2}\right)$$
on $U_{4 b \leq r \leq 1}$. Hence, $H_{\left(\varepsilon, \zeta / \varepsilon^{2}\right)}^{*}\left(g_{0}\right)=\varepsilon^{2} g^{\text {Euc }}+O\left(\varepsilon^{4} r^{2}\right)$ on $Y_{4 b / \varepsilon \leq r \leq 1 / \varepsilon}$. Furthermore, as $I_{\zeta}=I_{0}+O\left(r^{-4}\right)$ on $Y$, we have
$$H_{\left(\varepsilon, \zeta / \varepsilon^{2}\right)}^{*}\left(h_{t}\right)=H_{\left(\varepsilon, \zeta / \varepsilon^{2}\right)}^{*}\left(g_{0}\right)+O\left(\varepsilon^{2} r^{-4}\right)$$
on $Y_{4 b / \varepsilon \leq r \leq 1 / \varepsilon}$. Therefore, we have
$$\left(H_{\left(\varepsilon, \zeta / \varepsilon^{2}\right)}^{*}\left(h_{t}\right)\right)^{-1}=\left(H_{\left(\varepsilon, \zeta / \varepsilon^{2}\right)}^{*}\left(g_{0}\right)\right)^{-1}+O\left(\varepsilon^{-2} r^{-4}\right),$$
$$\begin{aligned}
\partial_{t}\left(H_{\left(\varepsilon, \zeta / \varepsilon^{2}\right)}^{*}\left(h_{t}\right)\right) & =\left(1+O\left(r^{-4}\right)\right) \partial_{0}\left(H_{\left(\varepsilon, \zeta / \varepsilon^{2}\right)}^{*}\left(g_{0}\right)+O\left(\varepsilon^{2} r^{-4}\right)\right) \\
& =\partial_{0}\left(H_{\left(\varepsilon, \zeta / \varepsilon^{2}\right)}^{*}\left(g_{0}\right)\right)+O\left(\varepsilon^{2} r^{-5}\right),
\end{aligned}$$
and
$$\begin{aligned}
\partial_{t}^{2}\left(H_{\left(\varepsilon, \zeta / \varepsilon^{2}\right)}^{*}\left(h_{t}\right)\right) & =\left(\left(1+O\left(r^{-4}\right)\right) \partial_{0}\right)^{2}\left(H_{\left(\varepsilon, \zeta / \varepsilon^{2}\right)}^{*}\left(g_{0}\right)+O\left(\varepsilon^{2} r^{-4}\right)\right) \\
& =\partial_{0}^{2}\left(H_{\left(\varepsilon, \zeta / \varepsilon^{2}\right)}^{*}\left(g_{0}\right)\right)+O\left(\varepsilon^{2} r^{-6}\right),
\end{aligned}$$
where $\partial_{t}$ is any differentiation with respect to the frame $e_{\zeta(t)}^{i}$ on $Y_{4 b / \varepsilon \leq r \leq 1 / \varepsilon}$. Hence we have
$$\begin{gathered}
R_{j k \bar{l}}^{i}\left(H_{\left(\varepsilon, \zeta / \varepsilon^{2}\right)}^{*}\left(h_{t}\right)\right)=R_{j k \bar{l}}^{i}\left(H_{\left(\varepsilon, \zeta / \varepsilon^{2}\right)}^{*}\left(g_{0}\right)\right)+O\left(r^{-6}\right), \\
c_{2}\left(H_{\left(\varepsilon, \zeta / \varepsilon^{2}\right)}^{*}\left(h_{t}\right)\right)=c_{2}\left(H_{\left(\varepsilon, \zeta / \varepsilon^{2}\right)}^{*}\left(g_{0}\right)\right)+O\left(\varepsilon^{2} r^{-6}\right) \operatorname{Vol}_{\mathrm{Euc}}
\end{gathered}$$
on $Y_{4 b / \varepsilon \leq r \leq 1 / \varepsilon}$ under the trivialization by the frame $\left\{e_{\zeta(t)}^{1}, e_{\zeta(t)}^{2}\right\}$. Therefore,
$$\begin{aligned}
\int_{4 b \leq r \leq 1} \tilde{f}_{t} c_{2}\left(h_{t}\right) & =\int_{4 b / \varepsilon \leq r \leq 1 / \varepsilon} H_{\left(\varepsilon, \zeta / \varepsilon^{2}\right)}^{*}\left(\tilde{f}_{t}\right) c_{2}\left(H_{\left(\varepsilon, \zeta / \varepsilon^{2}\right)}^{*}\left(h_{t}\right)\right) \\
& =\int_{4 b / \varepsilon \leq r \leq 1 / \varepsilon} H_{\left(\varepsilon, \zeta / \varepsilon^{2}\right)}^{*}\left(\tilde{f}_{t}\right)\left(c_{2}\left(H_{\left(\varepsilon, \zeta / \varepsilon^{2}\right)}^{*}\left(g_{0}\right)\right)+O\left(\varepsilon^{2} r^{-6}\right) \operatorname{Vol}_{\mathrm{Euc}}\right) \\
& =\int_{4 b / \varepsilon \leq r \leq 1 / \varepsilon}\left(H_{\left(\varepsilon, \zeta / \varepsilon^{2}\right)}^{*}\left(\tilde{f}_{0}\right)+O(t)\right)\left(c_{2}\left(H_{\left(\varepsilon, \zeta / \varepsilon^{2}\right)}^{*}\left(g_{0}\right)\right)+O\left(\varepsilon^{2} r^{-6}\right) \operatorname{Vol}_{\mathrm{Euc}}\right) \\
& =\int_{4 b / \varepsilon \leq r \leq 1 / \varepsilon} H_{\left(\varepsilon, \zeta / \varepsilon^{2}\right)}^{*}\left(\tilde{f}_{0}\right) c_{2}\left(H_{\left(\varepsilon, \zeta / \varepsilon^{2}\right)}^{*}\left(g_{0}\right)\right)+O(t) \\
& =\int_{4 b \leq r \leq 1} \tilde{f}_{0} c_{2}\left(g_{0}\right)+O(t) .
\end{aligned}$$
Note that $g_{0}$ is an orbifold metric, hence the curvature of $g_{0}$ is uniformly bounded on this domain. \(\square\)

Lemma 6. $\int_{U_{2 b \leq r \leq 4 b}} \tilde{f}_{t} c_{2}\left(h_{t}\right)=\int_{U_{2 b \leq r \leq 4 b}} \tilde{f}_{0} c_{2}\left(g_{0}\right)+O\left(\varepsilon^{2}\right)$.
Proof. Recall that $\tilde{h}_{t}=d d_{0}^{c}\left(r^{2}+\chi_{(2 b, 4 b)}(r) \eta\right)$ on this domain where $g_{0}=d d_{0}^{c}\left(r^{2}+\eta\right)$ with respect to the coordinate $\left(z_{0}, w_{0}\right)$. Note that $\eta=O\left(r^{4}\right)$ on $U_{2 b \leq r \leq 4 b}$. Then, we have
$$\begin{aligned}
d d_{0}^{c}\left(r^{2}+\chi_{(2 b, 4 b)}(r) \eta\right) & =d d_{0}^{c} r^{2}+\frac{\chi_{(2 b, 4 b)}^{\prime}(r) \eta}{2 b} d d_{0}^{c} r+\frac{\chi_{(2 b, 4 b)}^{\prime \prime}(r) \eta}{4 b^{2}} d r \wedge d_{0}^{c} r \\
& +\frac{\chi_{(2 b, 4 b)}^{\prime}(r)}{2 b}\left(d \eta \wedge d_{0}^{c} r+d r \wedge d_{0}^{c} \eta\right)+\chi_{(2 b, 4 b)}(r) d d_{0}^{c} \eta .
\end{aligned}$$

Recall that $\eta=O\left(r^{4}\right), r=O(r)=O(b),\|d r\|_{g_{0}},\left\|d_{0}^{c} r\right\|_{g_{0}}=O\left(r^{0}\right),\left\|d d_{0}^{c} r\right\|_{g_{0}}=$ $O\left(r^{-1}\right)$ and $\chi^{\prime}, \chi^{\prime \prime}$ are bounded, we have
$$d d_{0}^{c}\left(r^{2}+\chi_{(2 b, 4 b)}(r) \eta\right)=g_{0}+O\left(r^{2}\right) .$$
Therefore,
$$\begin{aligned}
H_{\left(\varepsilon, \zeta / \varepsilon^{2}\right)}^{*}\left(h_{t}\right) & =H_{\left(\varepsilon, \zeta / \varepsilon^{2}\right)}^{*}\left(\tilde{h}_{t}\right)+O\left(\varepsilon^{2} r^{-4}\right) \\
& =H_{\left(\varepsilon, \zeta / \varepsilon^{2}\right)}^{*}\left(g_{0}\right)+O\left(\varepsilon^{4} r^{2}\right)+O\left(\varepsilon^{2} r^{-4}\right) \\
& =H_{\left(\varepsilon, \zeta / \varepsilon^{2}\right)}^{*}\left(g_{0}\right)+O\left(\varepsilon^{4} r^{2}\right)
\end{aligned}$$
on $Y_{2 b / \varepsilon \leq r \leq 4 b / \varepsilon}$. In particular, $h_{t}=H_{\left(\varepsilon^{-1}, \zeta\right)}^{*} H_{\left(\varepsilon, \zeta / \varepsilon^{2}\right)}^{*}\left(h_{t}\right)=g_{0}+O\left(r^{2}\right)$ on $U_{2 b \leq r \leq 4 b}$. Then, we have
$$\begin{aligned}
& \left(h_{t}\right)^{-1}=\left(g_{0}\right)^{-1}+O\left(r^{2}\right) \\
& \partial_{t}\left(h_{t}\right)=\left(\partial_{0}+O\left(r^{2}\right)\right)\left(g_{0}+O\left(r^{2}\right)\right)=\partial_{0}\left(g_{0}\right)+O(r) \\
& \partial_{t}^{2}\left(h_{t}\right)=\left(\partial_{0}+O\left(r^{2}\right)\right)^{2}\left(g_{0}+O\left(r^{2}\right)\right)=\partial_{0}^{2}\left(g_{0}\right)+O\left(r^{0}\right)
\end{aligned}$$
on $U_{2 b \leq r \leq 4 b}$, where $\partial_{t}$ is any differentiation by the frame $\left\{\varepsilon^{-1}\left(H_{\left(\varepsilon, \zeta / \varepsilon^{2}\right)}\right)_{*} e_{t}^{i}\right\}$. Then we have the following on $U_{2 b \leq r \leq 4 b}$ :
$$\begin{gathered}
R_{j k \bar{l}}^{i}\left(h_{t}\right)=R_{j k \bar{l}}^{i}\left(g_{0}\right)+O\left(r^{0}\right), \\
c_{2}\left(h_{t}\right)=c_{2}\left(g_{0}\right)+O\left(r^{0}\right) \operatorname{Vol}_{\mathrm{Euc}}
\end{gathered}$$
with respect to the frame $\left\{\varepsilon^{-1}\left(H_{\left(\varepsilon, \zeta / \varepsilon^{2}\right)}\right)_{*} e_{t}^{i}\right\}$. As the volume of the domain $U_{b \leq r \leq 2 b}$ is of order $b^{4}$ and $c_{2}\left(g_{0}\right)$ is bounded (note that $g_{0}$ is an orbifold metric) we have the following estimate:
$$\int_{U_{2 b \leq r \leq 4 b}} \tilde{f}_{t} c_{2}\left(h_{t}\right)=\int_{U_{2 b \leq r \leq 4 b}} \tilde{f}_{0} c_{2}\left(g_{0}\right)+O\left(b^{4}\right) .$$
As $b=\varepsilon^{\beta}$ for $\beta>\frac{1}{2}$, we see that $O\left(b^{4}\right)$ can be replaced by $O\left(\varepsilon^{2}\right)$. \(\square\)

Lemma 7. $\int_{U_{b \leq r \leq 2 b}} \tilde{f}_{t} c_{2}\left(h_{t}\right)=\int_{U_{b \leq r \leq 2 b}} \tilde{f}_{0} c_{2}\left(g_{0}\right)+O\left(\varepsilon^{2}\right)$.
Proof. Recall that $\tilde{h}_{t}=d d_{0}^{c} r^{2}+\left(1-\chi_{(b, 2 b)}(r)\right) \varepsilon^{2} H_{\left(\varepsilon^{-1}, \zeta\right)}^{*} \xi_{t}$ where $\xi_{t}=g_{\varepsilon^{-2} \zeta(t)}-g^{\text {Euc }}$ which satisfies $\xi_{t}=O\left(r^{-4}\right)$ on $Y_{b / \varepsilon \leq r \leq 2 b / \varepsilon}$, as $g_{\varepsilon^{-2} \zeta(t)}$ is an ALE metric. The estimates $\varepsilon^{2} H_{\left(\varepsilon^{-1}, \zeta\right)}^{*}\left(\xi_{t}\right)=O\left(\varepsilon^{4} r^{-4}\right)$ and $\chi_{(b, 2 b)}=O\left(r^{0}\right)$ on $U_{b \leq r \leq 2 b}$ imply that
$$\tilde{h}_{t}=d d_{0}^{c} r^{2}+O\left(\varepsilon^{4} r^{-4}\right)=g_{0}+O\left(r^{2}\right) .$$
Note that this is the same estimate as the case on $U_{2 b \leq r \leq 4 b}$, hence we obtain
$$\int_{U_{b \leq r \leq 2 b}} \tilde{f}_{t} c_{2}\left(h_{t}\right)=\int_{U_{b \leq r \leq 2 b}} f_{0} c_{2}\left(g_{0}\right)+O\left(\varepsilon^{2}\right) .$$ \(\square\)

Lemma 8. $\int_{U_{r \leq b}} \tilde{f}_{t} c_{2}\left(g_{\zeta(t)}\right)=f\left(x_{0}\right) \int_{Y_{\dot{\zeta}}} c_{2}\left(g_{\dot{\zeta}}\right)+O\left(\varepsilon^{2}\right)$.

Proof. Recall that $\tilde{h}_{t}=h_{t}=g_{\zeta(t)}$ on this domain. By the naturality of Chern forms, we have
$$\int_{U_{r \leq b}} \tilde{f}_{t} c_{2}\left(g_{\zeta(t)}\right)=\int_{Y_{r \leq b / \varepsilon}}\left(H_{\left(\varepsilon, \zeta / \varepsilon^{2}\right)}^{*} \tilde{f}_{t}\right) c_{2}\left(g_{\varepsilon^{-2} \zeta(t)}\right) .$$
By lemma 3, we have
$$\int_{Y_{r \leq b / \varepsilon}}\left(H_{\left(\varepsilon, \zeta / \varepsilon^{2}\right)}^{*} \tilde{f}_{t}\right) c_{2}\left(g_{\varepsilon^{-2} \zeta(t)}\right)=f\left(x_{0}\right) \int_{Y_{r \leq b / \varepsilon}} c_{2}\left(g_{\varepsilon^{-2} \zeta(t)}\right)+\int_{Y_{r \leq b / \varepsilon}} O\left(\varepsilon^{k} r^{k}\right) c_{2}\left(g_{\varepsilon^{-2} \zeta(t)}\right) .$$
As $g_{\varepsilon^{-2} \zeta(t)}$ is an ALE metric, we have $g_{\varepsilon^{-2} \zeta(t)}=g^{\text {Euc }}+O\left(r^{-4}\right)$ as $r \rightarrow \infty$. Hence $c_{2}\left(g_{\varepsilon^{-2} \zeta(t)}\right)=O\left(r^{-12}\right) \operatorname{Vol}_{\text {Euc }}$ as $r \rightarrow \infty$. Then,
$$\begin{aligned}
\int_{Y_{r \leq b / \varepsilon}} c_{2}\left(g_{\varepsilon^{-2} \zeta(t)}\right) & =\int_{Y_{\varepsilon^{-2} \zeta(t)}} c_{2}\left(g_{\varepsilon^{-2} \zeta(t)}\right)+O\left(\varepsilon^{8} / b^{8}\right) \\
\int_{Y_{r \leq b / \varepsilon}} O\left(\varepsilon^{k} r^{k}\right) c_{2}\left(g_{\varepsilon^{-2} \zeta(t)}\right) & =O\left(\varepsilon^{2}\right) .
\end{aligned}$$
Recall that the integral $\int_{Y_{\varepsilon}-2 \zeta(t)} c_{2}\left(g_{\varepsilon}-2 \zeta(t)\right)=e_{\text {orb }}\left(Y_{\dot{\zeta}}\right)$, the Euler number, is independent of $t$, hence we have
$$\int_{U_{r \leq b}} \tilde{f}_{t} c_{2}\left(g_{\zeta(t)}\right)=f\left(x_{0}\right) \int_{Y_{\dot{\zeta}}} c_{2}\left(g_{\dot{\zeta}}\right)+O\left(\varepsilon^{2}\right) .$$ \(\square\)

Summing them up, we obtain the following estimate:
$$\int_{X_{t}} \tilde{f}_{t} c_{2}\left(h_{t}\right)=\int_{X_{0}} \tilde{f}_{0} c_{2}\left(g_{0}\right)+f\left(x_{0}\right) e_{o r b}\left(Y_{\dot{\zeta}}\right)+O\left(\varepsilon^{2}\right) .$$

We calculate the second term
$$\int_{X_{t}} \sigma_{t} \wedge \tau$$
of (49) in the following. Recall that $\sigma$ is initially $d d^{c} f$, however, we consider a general 2-form $\sigma$ with bidegree $(1,1)$ on each $X_{t}$ in the following. Before we calculate the integral $\int_{X_{t}} \sigma_{t} \wedge \tau$, we recall the Bott-Chern formula to derive an explicit form of $\tau$. Let $\nabla_{t}, \nabla_{t}^{\prime}$ be the Chern connections of $h_{t}, g_{t}$ respectively. Take a family of hermitian metrics $\left\{k_{s}\right\}$ that connects $h_{t}$ and $g_{t}$ smoothly, say $k_{s}=h_{t}+s\left(g_{t}-h_{t}\right)$ here, parameterised by $s \in[0,1]$ and define $N_{s}$ by $\left(N_{s}\right)_{i, j}=\left(\dot{k}_{s}\right)_{i \alpha}\left(k_{s}\right)^{\alpha j}$ under a coordinate (the dot means a derivative with respect to $s$ ). Then Bott-Chern formula (see [8]) yields
$$c\left(h_{t}\right)-c\left(g_{t}\right)=d d^{c} \phi$$
for the total Chern forms, where $\phi$ is defined by
$$\phi=-\frac{1}{2 \pi} \int_{0}^{1} N_{s} \wedge\left(I-\frac{R_{s}}{2 \pi \sqrt{-1}}\right) d s$$
where $R_{s}$ is the curvature tensor of $k_{s}$. Under a trivialization, the right hand side becomes
$$\begin{aligned}
-\frac{1}{2 \pi} \int_{0}^{1} N_{s} \wedge\left(I-\frac{R_{s}}{2 \pi \sqrt{-1}}\right) d s & =-\frac{1}{2 \pi} \int_{0}^{1}\left(\operatorname{det}\left[\begin{array}{ll}
\left(N_{s}\right)_{11} & -\frac{\left(R_{s}\right)_{12}}{2 \pi \sqrt{-1}} \\
\left(N_{s}\right)_{21} & 1-\frac{\left(R_{s}\right)_{22}}{2 \pi \sqrt{-1}}
\end{array}\right]+\operatorname{det}\left[\begin{array}{cc}
1-\frac{\left(R_{s}\right)_{11}}{2 \pi \sqrt{-1}} & \left(N_{s}\right)_{12} \\
-\frac{\left(R_{s}\right)_{21}}{2 \pi \sqrt{-1}} & \left(N_{s}\right)_{22}
\end{array}\right]\right) d s \\
& =-\frac{1}{2 \pi} \int_{0}^{1}\left(N_{s}\right)_{11} d s+\frac{1}{4 \pi^{2} \sqrt{-1}} \int_{0}^{1}\left(N_{s}\right)_{11}\left(R_{s}\right)_{22}-\left(N_{s}\right)_{21}\left(R_{s}\right)_{12} d s \\
& +-\frac{1}{2 \pi} \int_{0}^{1}\left(N_{s}\right)_{22} d s+\frac{1}{4 \pi^{2} \sqrt{-1}} \int_{0}^{1}\left(N_{s}\right)_{22}\left(R_{s}\right)_{11}-\left(N_{s}\right)_{12}\left(R_{s}\right)_{21} d s
\end{aligned}$$
In particular, $\tau$, the $(1,1)$ component of $\phi$, can be written as
$$\tau=\frac{1}{4 \pi^{2} \sqrt{-1}} \int_{0}^{1}\left(N_{s}\right)_{11}\left(R_{s}\right)_{22}-\left(N_{s}\right)_{21}\left(R_{s}\right)_{12}+\left(N_{s}\right)_{22}\left(R_{s}\right)_{11}-\left(N_{s}\right)_{12}\left(R_{s}\right)_{21} d s .$$