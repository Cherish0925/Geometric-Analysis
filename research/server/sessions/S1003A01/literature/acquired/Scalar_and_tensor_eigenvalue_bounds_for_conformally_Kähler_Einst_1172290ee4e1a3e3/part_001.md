---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Scalar and tensor eigenvalue bounds for conformally Kähler Einstein four-manifolds]

---
source_file: Scalar_and_tensor_eigenvalue_bounds_for_conformally_Kähler_Einstein_four-manifol_c2ac9ec40c32.pdf
converter: mathpix
format: mmd
---

\title{
SCALAR AND TENSOR EIGENVALUE BOUNDS FOR CONFORMALLY KÄHLER EINSTEIN FOUR-MANIFOLDS
}

\author{
ANASS NIFA
}

\begin{abstract}
We prove scalar and tensor eigenvalue estimates for conformally Kähler Einstein fourmanifolds. For the Chen-LeBrun-Weber metric, Ric $_{g}=\Lambda g$, the first positive scalar eigenvalue satisfies $4 \Lambda / 3<\lambda_{1}^{\mathrm{sc}}(g)<1951 \Lambda / 1000$. Thus this metric admits a destabilizing conformal variation, as asserted in Hall-Murphy's Conjecture 5.3. The upper bound follows from boundary moments of an affine quotient on the moment polygon and a positive-coefficient polynomial identity. For any closed Einstein four-manifold conformal to a positive-scalar-curvature Kähler metric, put $m=b_{2}^{-}>0$ and $\rho=\max s_{k} / \min s_{k}$, using the complex orientation. We prove $\lambda_{m}^{\mathrm{TT}} \leq(4 \Lambda / 3)\left(1-\rho^{-3}\right)$ for the full Lichnerowicz operator, with strict inequality for a nonconstant conformal factor. For the Chen-LeBrun-Weber metric, this gives two TT eigenvalues below $7 \Lambda / 6$, proves the instability of its normalized Ricci-flat cone, and, together with the scalar bound, gives at least three positive directions for the entropy Hessian modulo diffeomorphisms and scaling. Finally, under det $W^{+} \geq 0$, the stable cones over closed oriented positive Einstein four-manifolds are precisely those over the round sphere and the Fubini-Study projective plane.
\end{abstract}

\section*{Contents}
1. Introduction ..... 1
2. A divergence penalty and the low TT spectrum ..... 5
3. Conformal harmonic forms and a spectral bound ..... 11
4. Scalar-curvature ratios from toric moments ..... 14
5. Affine moment potentials and the scalar spectrum ..... 16
6. An exact scalar bound for the Chen-LeBrun-Weber metric ..... 18
7. Conformal instability and the entropy index ..... 21
8. Compactly supported variations on the cone ..... 23
9. Quotients and the half-Weyl classification ..... 24
Appendix A. An algebraic proof of the scalar estimate ..... 27
Appendix B. Operator normalizations ..... 30
References ..... 31

\section*{1. Introduction}

The Hessian of the shrinker entropy at a positive Einstein metric has distinct restrictions to conformal and transverse-traceless variations. The first is expressed by the scalar Laplacian; the second by the Lichnerowicz operator. We estimate both spectra for the Chen-LeBrun-Weber metric and deduce conformal instability of the compact metric and instability of its normalized Ricci-flat cone.

Page constructed a non-Kähler Einstein metric on $\mathbb{C P}^{2} \# \overline{\mathbb{C P}}^{2}$ [27]. Derdziński related the Einstein equation of a conformally Kähler four-metric to the scalar curvature of its Kähler representative [11]. Chen-LeBrun-Weber subsequently constructed the Einstein metric on $\mathbb{C P}^{2} \# 2 \overline{\mathbb{C P}}^{2}$ by finding a bilaterally symmetric critical class of the extremal Calabi functional [8]. LeBrun's classification

\footnotetext{
2020 Mathematics Subject Classification. 53C25, 58J50, 53C55, 53C44.
Key words and phrases. Einstein metric, scalar Laplacian, Lichnerowicz Laplacian, conformal instability, toric Kähler metric, Ricci-flat cone.
}
shows that these are the only non-Kähler Einstein-Hermitian metrics on compact complex surfaces [23, Theorem A].

Hall-Haslhofer-Siepmann proved instability of the Page cone and posed the corresponding question for the Chen-LeBrun-Weber cone [14]. Hall-Murphy studied the scalar spectra [15, 16]. Their later numerical calculation identified a Rayleigh quotient below the conformal instability threshold in the exchange-anti-invariant subspace, and led to their Conjecture 5.3 [17]. Biquard-Ozuch proved compact instability by a harmonic-form construction with trace-free tensors [3]. The scalar estimate below is strictly less than $2 \Lambda$. The TT estimate, after normalization to Ric $=3 g$, is strictly less than the cone threshold 15/4.

The two calculations use different established identities. The tensor argument combines the divergence penalty of [25] with the conformal identities of Biquard-Ozuch. The scalar argument uses an affine quotient of moment functions and a specialization of the weighted toric integration formulas of Apostolov-Maschler [1]. Hall-Murphy had already used Donaldson's boundary formula for scalar spectral bounds and recorded Haslhofer's suggestion to apply it to the CLW spectrum [18]. Here the resulting quotient is bounded by a polynomial identity at the algebraic parameter of the conformally Einstein class.
1.1. The cohomological estimate. All manifolds and metrics are smooth. A closed manifold is compact and has no boundary. Let $\left(M^{n}, g\right)$ be closed and connected, with $\operatorname{Ric}_{g}=\Lambda g$. We use the curvature convention
$$R(X, Y) Z=\nabla_{X} \nabla_{Y} Z-\nabla_{Y} \nabla_{X} Z-\nabla_{[X, Y]} Z, \quad K(X, Y)=\langle R(X, Y) Y, X\rangle$$
for an orthonormal pair. The action on symmetric covariant tensors is
$$\left(\AA{ }^{\circ} T\right)(X, Y)=\sum_{i} T\left(R\left(e_{i}, X\right) Y, e_{i}\right) .$$
A local orthonormal frame is denoted by $\left(e_{i}\right)$. All tensor norms are induced by the metric; a two-form has squared norm $|\alpha|^{2}=\frac{1}{2} \sum_{i, j} \alpha_{i j}^{2}$. Integrals on an unoriented manifold use the Riemannian density. In particular, $\stackrel{\circ}{R}(g)=\operatorname{Ric}_{g}$. Put
$$\Delta=-\operatorname{div} \nabla, \quad(\delta T)_{j}=-\nabla^{i} T_{i j}, \quad L_{g}=\nabla^{*} \nabla+2 \Lambda I-2 \stackrel{\circ}{R} .$$
Thus $L_{g}$ is the full Lichnerowicz operator and $\mathcal{E}_{g}=L_{g}-2 \Lambda I$ is the Einstein operator. A tensor is transverse-traceless, or TT, if $\delta T=0$ and $\operatorname{tr}_{g} T=0$. Write $0=\lambda_{0}^{\mathrm{sc}}(g)<\lambda_{1}^{\mathrm{sc}}(g) \leq \cdots$ for the scalar spectrum, with multiplicities. The eigenvalues of $L_{g}$ on the closed $L^{2}$ TT space, counted with multiplicity, are written $\lambda_{j}^{\mathrm{TT}}(g)$ in increasing order. The realization of this operator is given in Lemma 2.2. An inequality involving $\lambda_{j}^{\mathrm{TT}}$ includes the existence of at least $j$ TT eigenvalues. For a quadratic form $q$ on a vector space, $\operatorname{ind}^{-}(q)$ denotes the supremum of the dimensions of linear subspaces on which $q$ is negative definite.

On an oriented four-manifold, $b_{2}^{+}$and $b_{2}^{-}$are the positive and negative indices of the real intersection form. When a Kähler metric is specified, the orientation is its complex orientation.

Theorem A. Let $\left(M^{4}, g\right)$ be closed and connected, with $\operatorname{Ric}_{g}=3 g$. Suppose $g=f_{0}^{2} k_{0}$, where $f_{0}>0$ is smooth and $k_{0}$ is Kähler with positive scalar curvature $s_{k_{0}}$. Set
$$m=b_{2}^{-}(M)>0, \quad \rho=\frac{\max _{M} s_{k_{0}}}{\min _{M} s_{k_{0}}} .$$
Then
$$\lambda_{m}^{\mathrm{TT}}(g) \leq 4-\frac{4}{\rho^{3}} .$$
If $f_{0}$ is nonconstant, the inequality is strict. If $f_{0}$ is constant, then
$$\operatorname{dim} \operatorname{ker}\left(\left.L_{g}\right|_{\mathrm{TT}}\right) \geq m .$$

The ratio in (1.4) is unchanged by a constant rescaling of $k_{0}$. For $\operatorname{Ric}_{g}=\Lambda g, \Lambda>0$, the corresponding bound is
$$\lambda_{m}^{\mathrm{TT}}(g) \leq \frac{4 \Lambda}{3}\left(1-\rho^{-3}\right) .$$
Indeed, $\widehat{g}=(\Lambda / 3) g$ has $\operatorname{Ric}_{\widehat{g}}=3 \widehat{g}$, and the Levi-Civita connections agree. With $c=\Lambda / 3$,
$$\operatorname{tr}_{\widehat{g}} T=c^{-1} \operatorname{tr}_{g} T, \quad \delta_{\widehat{g}} T=c^{-1} \delta_{g} T, \quad L_{\widehat{g}} T=c^{-1} L_{g} T .$$
Thus the TT subspaces agree and eigenvalues scale by $c^{-1}$.

\subsection*{1.2. The scalar estimate and conformal instability.}

Theorem B. Let $g$ be the Chen-LeBrun-Weber Einstein metric with $\operatorname{Ric}_{g}=\Lambda g, \Lambda>0$. Then
$$\frac{4}{3} \Lambda<\lambda_{1}^{\mathrm{sc}}(g)<\frac{1951}{1000} \Lambda<2 \Lambda .$$
For a first positive scalar eigenfunction $\psi$, the conformal variation $g_{t}=(1+t \psi) g$ satisfies $D^{2} v_{g}(\psi g, \psi g)>0$. In particular, $g$ is linearly conformally unstable as a shrinking Ricci soliton.

Here $v$ is Perelman's shrinker entropy; its normalization and the second-variation formula used in the proof are given in Section 7. The lower inequality in (1.9) is the strict Lichnerowicz-Obata bound. The upper inequality gives the conformal-instability assertion of [17, Conjecture 5.3], first stated in 2014. Its proof uses exact moments of the Einstein metric.

Choose the moment coordinates so that the Kähler representative has polygon (4.10), and use the homothetic Einstein metric $g=s^{-2} k$, where $s=\operatorname{Scal}_{k}$. For $q=x_{1}-x_{2}$, the function $q / s$ is smooth and has zero $g$-mean. With the four moments in (6.17), the exact identities are
$$\Lambda=\frac{K}{2 V}, \quad \frac{\mathcal{R}_{g}(q / s)}{\Lambda}=\frac{2 J V}{I K}-2<\frac{1951}{1000} .$$
The required integrals have rational primitives. The conformally Einstein parameter is isolated as the unique root in $(1, \infty)$ of an explicit degree-ten polynomial. Reduction modulo this polynomial, followed by a translation with positive coefficients, proves the strict inequality in (1.10); see Section 6 and Appendix A.

Hall-Murphy's approximate anti-invariant quotient was already below $2 \Lambda$ [17, Section 5]. The estimate below uses that antisymmetric subspace but does not identify the first eigenvalue or its multiplicity. It is an upper bound for the Einstein metric itself. The scalar-to-tensor operator is that of Cao-Hamilton-Ilmanen [5], written explicitly in [15, Definition 5.2 and Theorem 5.4].
1.3. The Page and Chen-LeBrun-Weber cones. Let $g_{\mathrm{P}}$ and $g_{\mathrm{CLW}}$ denote the Page and Chen-LeBrun-Weber metrics, normalized to have Einstein constant 3. Their existence and conformally Kähler descriptions are due to Page [27], Derdziński [11], and Chen-LeBrun-Weber [8].

Theorem C. The following inequalities hold:
$$\lambda_{1}^{\mathrm{TT}}\left(\mathrm{~g}_{\mathrm{P}}\right)<\frac{7}{2}, \quad \lambda_{2}^{\mathrm{TT}}\left(g_{\mathrm{CLW}}\right)<\frac{7}{2} .$$
Both Ricci-flat cones have infinite negative index on smooth TT tensors with compact support in the regular cone.

Hall-Haslhofer-Siepmann proved the instability of the Page cone and of the relevant Kähler-Einstein cones, and the stability of the Fubini-Study cone [14, Theorems 1.2-1.4]. In the preprint of 2011 they stated the Chen-LeBrun-Weber cone assertion as Conjecture 1.5. Conjecture 1.7 in the same paper concerns the compact metric as a Ricci shrinker. Biquard-Ozuch established the compact instability result [3, Theorem 7]; their conformal identities are used in the proof of Theorem A.

These two stability assertions require different bounds. With $\mathrm{Ric}_{g}=3 g$, a negative Einsteinoperator eigenvalue is equivalent to $\lambda^{\mathrm{TT}}\left(L_{g}\right)<6$, whereas a negative separated cone variation is obtained when $\lambda^{\mathrm{TT}}\left(L_{g}\right)<15 / 4$. The latter value is the Hardy threshold; see [21, Theorem 1.2] and Proposition 8.1. Thus (1.11) gives $15 / 4-\lambda_{j}^{\mathrm{TT}}>1 / 4$ for each of the asserted eigenvalues. It does not
assert that the full Lichnerowicz eigenvalues are negative. For the Chen-LeBrun-Weber metric it gives two Einstein-operator eigenvalues below -5/2.

Hall-Murphy obtained scalar Laplace estimates for these metrics [15, 16]. Their later numerical study also provided evidence for the cone inequality of [14, Section 7.2], by estimating the scalarcurvature derivative appearing in its sufficient condition [17, Section 5.1]. That computation is not used here. The estimate $\rho<2$ follows instead from polynomial identities for the affine scalar curvature on the moment polygon. The coefficients are compared explicitly with the corrected formulas of [16] in Section 4.2. Numerical scalar and TT spectra for the Page metric have also been studied by Hennigar-Kunduri-Sievers-Wang [19]; their numerical spectral computation is distinct from the estimates proved here.
1.4. Stable cones under a half-Weyl condition. We use the following definition of cone stability, with the same transversality requirement as [14]. If $G=d r^{2}+r^{2} g$, set
$$Q_{C}(H)=\int_{(0, \infty) \times M}\left(\left|\nabla^{G} H\right|_{G}^{2}-2\left\langle\stackrel{\circ}{R}_{G} H, H\right\rangle_{G}\right) d v_{G}$$
The cone is stable if $Q_{C}(H) \geq 0$ for every smooth compactly supported symmetric tensor with $\delta_{G} H=0$. All supports are contained in the regular cone. No boundary condition at its vertex is imposed or required.

Theorem D. Let $\left(M^{4}, g\right)$ be closed, connected and oriented, with
$$\operatorname{Ric}_{g}=3 g, \quad \operatorname{det} W_{g}^{+} \geq 0 .$$
Its Ricci-flat cone is stable if and only if $(M, g)$ is isometric, as a Remannian manifold, to the unit-round $S^{4}$ or to $\mathbb{C P}^{2}$ with the Fubini-Study metric of Einstein constant 3 . For every other metric satisfying (1.13), $\pi_{1}(M)$ is either $\{1\}$ or $\mathbb{Z} / 2$. Set
$$m(M)= \begin{cases}b_{2}(M)-1, & \pi_{1}(M)=1, \\ b_{2}(M)+1, & \pi_{1}(M)=\mathbb{Z} / 2 .\end{cases}$$
Then $m(M) \geq 1$ and
$$\lambda_{m(M)}^{\mathrm{TT}}(g)<\frac{7}{2} .$$
In the second case,
$$\operatorname{dim} \operatorname{ker}\left(\left.L_{g}\right|_{\mathrm{TT}}\right) \geq b_{2}(M)+1 .$$
Every unstable cone in this theorem has infinite compactly supported TT index.
The geometric classification in Theorem D is supplied by Wu's Theorem 1.3 [29], LeBrun's Einstein-Hermitian classification [23, Theorem A], and his anti-holomorphic double-cover theorem [24, Proposition 1 and Theorem B]. The half-conformally-flat case uses [2, Theorem 13.30]. The spectral estimate for a free anti-holomorphic quotient uses anti-invariant harmonic forms on the cover: their products with the anti-invariant Kähler form are invariant tensors and descend. The dimension of this space is $b_{2}(M)+1$; see Proposition 9.2.

Catino-Dameno have extended the conformally Kähler reduction under weaker conditions on the eigenvalues of $W^{+}$[7]. Their result concerns the geometry of the link, not the numerical TT estimate (1.5). We retain the hypothesis det $W^{+} \geq 0$ in Theorem D. No classification without a half-Weyl hypothesis is asserted.
1.5. The variational argument and its antecedents. The orthogonal decomposition of metric variations into conformal, diffeomorphism and TT parts has a long history; see Koiso [20] and Besse [2, Chapter 4]. The argument in Section 2 evaluates the full-Lichnerowicz quadratic form on these parts. For an Einstein $n$-manifold with $\operatorname{Ric}_{g}=\Lambda g, \Lambda>0$, define, on smooth trace-free tensors,
$$\mathcal{J}_{g}(T)=\left\langle L_{g} T, T\right\rangle_{L^{2}}-\frac{n}{n-1}\|\delta T\|_{L^{2}}^{2} .$$

For $\tau \leq n \Lambda /(n-1)$, the exact identity is
$$\operatorname{ind}^{-}\left(\mathcal{J}_{g}-\tau\|\cdot\|_{L^{2}}^{2}\right)=\#\left\{\lambda \in \operatorname{spec}\left(\left.L_{g}\right|_{\mathrm{TT}}\right): \lambda<\tau\right\},$$
where eigenvalues on the right are counted with multiplicity. This is the shifted divergence-penalty theorem of [25]. Its proof, including the spectral realization of the TT restriction, is reproduced in Section 2. No elliptic realization of the critically penalized operator on all trace-free tensors is assumed.

The conformal operator has separate antecedents. The Weitzenböck formula used by Biquard-Ozuch comes from Biquard-Rollin [4, (4.6)]. Delay established a conformal covariance formula on symmetric two-tensors [9]; Biquard-Ozuch give the four-dimensional formulation and the harmonicform identities used below [3, Sections 1-2]. The distinction between conformal covariance and preservation of the TT condition is essential: their weights are different. Related constructions of TT tensors by differential operators are discussed by Delay [10, pp. 27-29, 54-59]. None of these operator constructions is claimed here as a new conformal covariance theorem.

After a constant rescaling of the Kähler representative, write $g=f^{2} k$ with $s_{k}=6 / f$. If $\Omega_{k}$ is the Kähler form and $\omega$ is harmonic and anti-self-dual, the tensor $T_{\omega}=f\left(\omega{ }_{k} \Omega_{k}\right)$ is trace-free, and
$$\mathcal{J}_{g}\left(T_{\omega}\right)=\int_{M}\left(4-2 f^{-3}\right)\left|T_{\omega}\right|_{g}^{2} d v_{g}$$
The Einstein equation for the conformal factor yields
$$\Delta_{k} f=2 f^{3}-1, \quad \frac{1}{\operatorname{Vol}_{k}(M)} \int_{M} f^{3} d v_{k}=\frac{1}{2}$$
It follows that $f^{-3} \geq 2 / \rho^{3}$, with a uniform strict inequality when $f$ is nonconstant. Combining (1.18)-(1.20) on the $m$-dimensional harmonic-form space proves (1.5). The pointwise composition, conformal powers and strictness argument are given in Section 3.

The affine scalar curvatures of the Page and Chen-LeBrun-Weber Kähler representatives are established toric data [14, 15, 16]. Their determination uses Donaldson's boundary integration identity [12, Section 2]. Section 4 recomputes the needed moments and proves $\rho<2$ throughout the displayed parameter ranges. Neither the affine formulas nor the cone Hardy threshold are claimed as new results. The cone criterion and the broader tensor decomposition are treated in [21, 22]; Section 8 proves the quadratic-form identity for the compactly supported tensors used here.

The principal estimates are (1.5), with its cohomological multiplicity and strict form, and (1.9). The first gives a two-dimensional TT subspace on which $D^{2} v$ is positive definite. The second gives an orthogonal divergence-free representative of a conformal variation with positive second variation. Hence the positive entropy index modulo diffeomorphisms and scaling is at least three (Corollary 7.2). The cone consequence and the quotient dimension of the kernel lead to Theorem D. The geometric classification theorems, conformal covariance, weighted toric identities and entropy second variation are the quoted theorems specified in the corresponding proofs. The scalar identity is a specialization of existing toric formulas; its application gives the strict scalar bound for the CLW metric. For the wider deformation and stability theory, see the survey [28]. The paper concerns closed Einstein links and their regular Ricci-flat cones; it does not treat arbitrary Ricci-flat fillings or unrestricted positive Einstein four-manifolds.

\section*{2. A divergence penalty and the low TT spectrum}

In this section $n \geq 3, \operatorname{Ric}_{g}=\Lambda g$, and $\Lambda>0$. All pairings are real. The symbol $H^{r}(E)$ denotes the Sobolev space of sections of a metric vector bundle $E$, with derivatives of order at most $r$ in $L^{2}$. Unless indicated otherwise, norms and pairings use $g$. Put
$$Q(T)=\left\langle L_{g} T, T\right\rangle_{L^{2}}, \quad c_{n}=\frac{n}{n-1}, \quad \mathcal{J}(T)=Q(T)-c_{n}\|\delta T\|_{L^{2}}^{2} .$$

For smooth functions and one-forms, define
$$P v=\nabla^{2} v+\frac{\Delta v}{n} g, \quad \mathcal{K} \omega=\delta^{*} \omega+\frac{\delta \omega}{n} g, \quad\left(\delta^{*} \omega\right)_{i j}=\frac{1}{2}\left(\nabla_{i} \omega_{j}+\nabla_{j} \omega_{i}\right) .$$
Here $\delta \omega=-\nabla^{i} \omega_{i}$ and $\mathcal{K}(d v)=P v$. Both operators in (2.2) take values in the trace-free tensors.

\subsection*{2.1. Commutation identities.}

Lemma 2.1. Let $\Delta_{H}=d \delta+\delta d$ on one-forms. Then
$$\begin{aligned}
\Delta_{H} & =\nabla^{*} \nabla+\Lambda I, & \nabla^{*} \nabla(d v) & =d \Delta v-\Lambda d v, \\
2 \delta \delta^{*} \omega & =\nabla^{*} \nabla \omega+d \delta \omega-\Lambda \omega, & \delta P v & =d\left(\frac{n-1}{n} \Delta v-\Lambda v\right), \\
L_{g}(a g) & =(\Delta a) g, & L_{g} \delta^{*} \omega & =\delta^{*} \Delta_{H} \omega, \\
L_{g} P v & =P \Delta v, & L_{g} \mathcal{K} \omega & =\mathcal{K} \Delta_{H} \omega, \\
\operatorname{tr}\left(L_{g} T\right) & =\Delta(\operatorname{tr} T), & \delta L_{g} T & =\Delta_{H} \delta T .
\end{aligned}$$
Proof. Write $R^{p}{ }_{k i j}$ for the components of $R\left(\partial_{i}, \partial_{j}\right) \partial_{k}$. The covector commutator and its rank-two consequence are
$$\begin{aligned}
\left(\left[\nabla_{i}, \nabla_{j}\right] \omega\right)_{k} & =-R_{k i j}^{p} \omega_{p}, \\
\left(\left[\nabla_{i}, \nabla_{j}\right] T\right)_{k \ell} & =-R_{k i j}^{p} T_{p \ell}-R_{\ell i j}^{p} T_{k p} .
\end{aligned}$$
The first equality follows by applying the definition of curvature to the scalar pairing of a covector and a vector. Applying it to each factor of a covariant tensor gives the second equality. Contracting the first equality gives
$$\nabla^{i} \nabla_{j} \omega_{i}=\nabla_{j} \nabla^{i} \omega_{i}+\operatorname{Ric}_{j}{ }^{p} \omega_{p} .$$
Expansion of $d \delta \omega+\delta d \omega$ and substitution of (2.9) give the first identity in (2.3). Since $d^{2}=0$, $\Delta_{H} d=d \Delta$; its application to a function gives the second identity. Expansion of $\delta \delta^{*}$ gives
$$2\left(\delta \delta^{*} \omega\right)_{j}=-\nabla^{i} \nabla_{i} \omega_{j}-\nabla^{i} \nabla_{j} \omega_{i}=\left(\nabla^{*} \nabla \omega\right)_{j}+(d \delta \omega)_{j}-\Lambda \omega_{j} .$$
Applying this with $\omega=d v$ gives $\delta \nabla^{2} v=d \Delta v-\Lambda d v$. Since $\delta(a g)=-d a$, (2.4) follows.
For a variation $g+t T$, the derivative of the connection is
$$2 \dot{\Gamma}_{i j}^{k}=\nabla_{i} T_{j}^{k}+\nabla_{j} T_{i}^{k}-\nabla^{k} T_{i j} .$$
Put $B^{k}{ }_{i j}=\dot{\Gamma}_{i j}^{k}$. Differentiating
$$R_{k i j}^{\ell}=\partial_{i} \Gamma_{j k}^{\ell}-\partial_{j} \Gamma_{i k}^{\ell}+\Gamma_{i p}^{\ell} \Gamma_{j k}^{p}-\Gamma_{j p}^{\ell} \Gamma_{i k}^{p}$$
and using $\Gamma_{i j}^{p}=\Gamma_{j i}^{p}$ gives
$$(D R)_{g}(T)^{\ell}{ }_{k i j}=\nabla_{i} B^{\ell}{ }_{j k}-\nabla_{j} B^{\ell}{ }_{i k}, \quad(D \operatorname{Ric})_{g}(T)_{i j}=\nabla_{p} B^{p}{ }_{j i}-\nabla_{j} B^{p}{ }_{p i} .$$
In components,
$$\nabla_{i} B^{\ell}{ }_{j k}=\partial_{i} B^{\ell}{ }_{j k}+\Gamma_{i p}^{\ell} B^{p}{ }_{j k}-\Gamma_{i j}^{p} B^{\ell}{ }_{p k}-\Gamma_{i k}^{p} B^{\ell}{ }_{j p} .$$
Subtraction cancels the terms containing $\Gamma_{i j}^{p}$. Substitution of (2.11) gives
$$2(D \text { Ric })_{g}(T)_{i j}=\nabla^{p} \nabla_{j} T_{i p}+\nabla^{p} \nabla_{i} T_{j p}-\nabla^{p} \nabla_{p} T_{i j}-\nabla_{j} \nabla_{i} \operatorname{tr} T .$$
For the first contracted derivative, (2.8) gives
$$g^{p a}\left(\left[\nabla_{a}, \nabla_{j}\right] T\right)_{i p}=-g^{p a} R^{q}{ }_{i a j} T_{q p}-g^{p a} R^{q}{ }_{p a j} T_{i q} .$$
The curvature symmetries identify the two contractions as $-(\stackrel{\circ}{R} T)_{i j}$ and $\operatorname{Ric}_{j}{ }^{q} T_{i q}$, respectively. Thus
$$\nabla^{p} \nabla_{j} T_{i p}-\nabla_{j} \nabla^{p} T_{i p}=\operatorname{Ric}_{j}{ }^{p} T_{i p}-(\stackrel{\circ}{R} T)_{i j} .$$
Interchanging $i, j$ gives the other contracted derivative; the Hessian of $\operatorname{tr} T$ is symmetric. Hence
$$\begin{aligned}
2(D \operatorname{Ric})_{g}(T)_{i j}= & -\nabla^{p} \nabla_{p} T_{i j}+\nabla_{i} \nabla^{p} T_{p j}+\nabla_{j} \nabla^{p} T_{p i}-\nabla_{i} \nabla_{j} \operatorname{tr} T \\
& +\operatorname{Ric}_{i}{ }^{p} T_{p j}+\operatorname{Ric}_{j}{ }^{p} T_{p i}-2(\stackrel{\circ}{R} T)_{i j} .
\end{aligned}$$

Consequently
$$2(D \text { Ric })_{g}(T)=L_{g} T-2 \delta^{*} \delta T-\nabla^{2} \operatorname{tr} T .$$
Naturality under the flow of $\omega^{\#}$ gives $(D \text { Ric })_{g}\left(\delta^{*} \omega\right)=\Lambda \delta^{*} \omega$. Also $\operatorname{tr} \delta^{*} \omega=-\delta \omega$. Substitution in (2.16) yields
$$\begin{aligned}
L_{g} \delta^{*} \omega & =2 \Lambda \delta^{*} \omega+2 \delta^{*} \delta \delta^{*} \omega-\nabla^{2} \delta \omega \\
& =2 \Lambda \delta^{*} \omega+\delta^{*}\left(\nabla^{*} \nabla \omega+d \delta \omega-\Lambda \omega\right)-\nabla^{2} \delta \omega \\
& =\delta^{*}\left(\nabla^{*} \nabla+\Lambda\right) \omega .
\end{aligned}$$
The last equality uses $\delta^{*} d(\delta \omega)=\nabla^{2}(\delta \omega)$. The identity for ag follows from $\nabla g=0$ and $\stackrel{\circ}{R}(g)=\Lambda g$.
Taking $\omega=d v$ gives $L_{g} \nabla^{2} v=\nabla^{2} \Delta v$. Hence
$$\begin{aligned}
L_{g} P v & =\nabla^{2} \Delta v+\frac{\Delta^{2} v}{n} g=P \Delta v, \\
L_{g} \mathcal{K} \omega & =\delta^{*} \Delta_{H} \omega+\frac{\Delta \delta \omega}{n} g=\mathcal{K} \Delta_{H} \omega .
\end{aligned}$$
For the last equality, $\delta \Delta_{H}=\delta d \delta=\Delta \delta$ follows from $\delta^{2}=0$ and from the definition of the scalar Laplacian. For a test function $a$ and a test one-form $\omega$, formal self-adjointness and integration by parts give
$$\begin{aligned}
\left\langle\operatorname{tr}\left(L_{g} T\right), a\right\rangle_{L^{2}} & =\left\langle L_{g} T, a g\right\rangle_{L^{2}}=\langle T,(\Delta a) g\rangle_{L^{2}}=\langle\Delta \operatorname{tr} T, a\rangle_{L^{2}}, \\
\left\langle\delta L_{g} T, \omega\right\rangle_{L^{2}} & =\left\langle L_{g} T, \delta^{*} \omega\right\rangle_{L^{2}}=\left\langle T, \delta^{*} \Delta_{H} \omega\right\rangle_{L^{2}}=\left\langle\Delta_{H} \delta T, \omega\right\rangle_{L^{2}} .
\end{aligned}$$
These equalities prove (2.7). \(\square\)
2.2. The TT realization. The analytic results used in this subsection are stated explicitly. For a smooth strongly elliptic differential operator $A$ of order two on a vector bundle over a closed manifold, weak elliptic regularity and the global elliptic estimate give
$$u \in H^{1}, \quad A u \in H^{r} \quad \Longrightarrow \quad u \in H^{r+2}, \quad\|u\|_{H^{r+2}} \leq C_{r}\left(\|A u\|_{H^{r}}+\|u\|_{L^{2}}\right), \quad r \in \mathbb{Z}_{\geq 0} .$$
The equation is interpreted in distributions. We also use the compact embedding $H^{r+1} \hookrightarrow H^{r}$ on a closed manifold and the spectral theorem for compact self-adjoint operators. The compact embedding is [13, Lemma 1.3.4(a), p. 29]. For (2.20), the parametrix construction in [13, Lemma 1.3.5 and the vector-bundle extension, p. 30] gives an operator $E$ of order -2 and a smoothing operator $S$ such that $E A=I-S$. Hence, in distributions,
$$u=E(A u)+S u, \quad\|E(A u)\|_{H^{r+2}} \leq C_{r}\|A u\|_{H^{r}}, \quad\|S u\|_{H^{r+2}} \leq C_{r}\|u\|_{L^{2}} .$$
The mapping properties are [13, Lemma 1.3.4(c), pp. 29-30]. They prove both weak regularity and the estimate in (2.20). The compact self-adjoint spectral theorem is [13, Lemma 1.6.2, pp. 42-43]; its application to elliptic operators on vector bundles is [13, Lemma 1.6.3, pp. 43-45]. The page numbers refer to the 1984 edition.

Lemma 2.2. The restriction of $L_{g}$ to distributionally TT tensors is self-adjoint on
$$H^{2}\left(S^{2} T^{*} M\right) \cap \mathcal{T}, \quad \mathcal{T}=\left\{T \in L^{2}\left(S^{2} T^{*} M\right): \operatorname{tr} T=0, \delta T=0 \text { in distributions }\right\} .$$
It is bounded below and has compact resolvent. Its eigentensors are smooth. Its eigenvalues obey the min-max formula on smooth TT subspaces.

Proof. The trace is continuous from $L^{2}$ to $L^{2}$, and divergence is continuous from $L^{2}$ to $H^{-1}$. Thus $\mathcal{T}$ is closed. Write $L_{g}=\nabla^{\star} \nabla+V$, where $V=2 \Lambda I-2 \AA$ is a smooth self-adjoint bundle endomorphism. Set $C=\max _{M}|V|_{\text {op }}$ and choose $b>C+1$. Then, on $H^{1}\left(S^{2} T^{*} M\right)$,
$$q_{b}(T):=Q(T)+b\|T\|_{L^{2}}^{2} \geq\|\nabla T\|_{L^{2}}^{2}+\|T\|_{L^{2}}^{2} .$$
Here $Q$ is extended to $H^{1}$ by its integral formula, and $q_{b}(S, T)$ denotes the symmetric polarization of $q_{b}$. The integral formula gives $\left|q_{b}(S, T)\right| \leq C_{b}\|S\|_{H^{1}}\|T\|_{H^{1}}$. Together with (2.23), this verifies the continuity and coercivity hypotheses of Lax-Milgram. That theorem gives, for every $U \in L^{2}$, a unique weak solution $V_{U} \in H^{1}$ of $\left(L_{g}+b\right) V_{U}=U$. The principal symbol of $L_{g}+b$ is $|\xi|^{2} I$. Equation (2.20),
applied with $r=0$, gives $V_{U} \in H^{2}$. Pairing the weak equation with $V_{U}$ first yields $\left\|V_{U}\right\|_{H^{1}} \leq\|U\|_{L^{2}}$ by (2.23). The same regularity estimate then implies $\left\|V_{U}\right\|_{H^{2}} \leq C_{b}\|U\|_{L^{2}}$. Thus $A_{b}: U \mapsto V_{U}$ is a bounded map $L^{2} \rightarrow H^{2}$. The Rellich embedding $H^{2} \hookrightarrow L^{2}$ makes $A_{b}$ compact. For $U_{1}, U_{2} \in L^{2}$, the weak equations give
$$\left\langle A_{b} U_{1}, U_{2}\right\rangle_{L^{2}}=q_{b}\left(A_{b} U_{1}, A_{b} U_{2}\right)=\left\langle U_{1}, A_{b} U_{2}\right\rangle_{L^{2}} .$$
Moreover $\left\langle A_{b} U, U\right\rangle_{L^{2}}=q_{b}\left(A_{b} U\right)>0$ when $U \neq 0$. Consequently $A_{b}$ is self-adjoint, positive and injective. Its range is exactly $H^{2}$ : one inclusion follows from the estimate above; for $V \in H^{2}$, put $U=\left(L_{g}+b\right) V \in L^{2}$ and apply uniqueness of the weak solution to obtain $A_{b} U=V$. Moreover, $\left(\operatorname{ran} A_{b}\right)^{\perp}=\operatorname{ker} A_{b}=0$. Let $A_{b} e_{j}=\rho_{j} e_{j}$ be its compact-operator spectral resolution, where $\rho_{j}>0$. The inverse has domain
$$\operatorname{dom}\left(A_{b}^{-1}\right)=\left\{\sum_{j} a_{j} e_{j}: \sum_{j} \rho_{j}^{-2}\left|a_{j}\right|^{2}<\infty\right\}=\operatorname{ran} A_{b}=H^{2} .$$
In this basis $A_{b}^{-1}$ is multiplication by the real numbers $\rho_{j}^{-1}$, and is therefore self-adjoint on this domain. Thus $A_{b}^{-1}-b I$ is the self-adjoint realization of $L_{g}$.

If $U \in \mathcal{T}$ and $V=\left(L_{g}+b\right)^{-1} U$, then (2.7), interpreted weakly, gives
$$(\Delta+b) \operatorname{tr} V=0, \quad\left(\nabla^{*} \nabla+\Lambda+b\right) \delta V=0 .$$
Pairing with $\operatorname{tr} V$ and $\delta V$, respectively, gives
$$\|d \operatorname{tr} V\|_{L^{2}}^{2}+b\|\operatorname{tr} V\|_{L^{2}}^{2}=0, \quad\|\nabla \delta V\|_{L^{2}}^{2}+(\Lambda+b)\|\delta V\|_{L^{2}}^{2}=0 .$$
The second pairing is legitimate since $V \in H^{2}$ and $\delta V \in H^{1}$. Thus $V \in \mathcal{T}$. For $U \in \mathcal{T}^{\perp}$ and $Z \in \mathcal{T}$, $\left\langle A_{b} U, Z\right\rangle_{L^{2}}=\left\langle U, A_{b} Z\right\rangle_{L^{2}}=0$. Hence $A_{b}$ also preserves $\mathcal{T}^{\perp}$. Its restriction to $\mathcal{T}$ is compact, positive and injective, and
$$\operatorname{ran}\left(\left.A_{b}\right|_{\mathcal{T}}\right)=H^{2} \cap \mathcal{T} .$$
Indeed, the inclusion from left to right has been proved. If $V \in H^{2} \cap \mathcal{T}$, then $U=\left(L_{g}+b\right) V$ is TT by (2.7), and $A_{b} U=V$. The range is dense in $\mathcal{T}$, since its orthogonal complement is the kernel of $\left.A_{b}\right|_{\mathcal{T}}$. Let $\left.A_{b}\right|_{\mathcal{T}} e_{j}=\sigma_{j} e_{j}$ be its spectral resolution. Then $\sigma_{j}>0$, and
$$\operatorname{dom}\left(\left(\left.A_{b}\right|_{\mathcal{T}}\right)^{-1}\right)=\left\{\sum_{j} a_{j} e_{j}: \sum_{j} \sigma_{j}^{-2}\left|a_{j}\right|^{2}<\infty\right\}=H^{2} \cap \mathcal{T} .$$
The inverse acts by $\sigma_{j}^{-1}$ on $e_{j}$. Subtracting $b I$ gives the self-adjoint TT realization of $L_{g}$ and its orthonormal eigenbasis. The elliptic estimate
$$\|T\|_{H^{r+2}} \leq C_{r}\left(\left\|L_{g} T\right\|_{H^{r}}+\|T\|_{L^{2}}\right) \quad(r \geq 0)$$
iterated on an eigentensor gives smoothness. The orthogonal projection onto $\mathcal{T}$ commutes with $A_{b}$. It therefore commutes with $\left(L_{g}+b\right)^{1 / 2}$ on its domain. Since $q_{b}$ has domain $H^{1}$, the restricted form has domain $H^{1} \cap \mathcal{T}$. Its spectral partial sums converge in the $q_{b}$ norm, which is equivalent to the $H^{1}$ norm by (2.23) and the continuity bound above. Thus, if $\left(e_{j}\right)$ is an orthonormal TT eigenbasis and $H=\sum_{j} a_{j} e_{j} \in H^{1} \cap \mathcal{T}$, then
$$\|H\|_{L^{2}}^{2}=\sum_{j} a_{j}^{2}, \quad Q(H)=\sum_{j} \lambda_{j}^{\mathrm{TT}} a_{j}^{2} .$$
The second series is interpreted by the lower-bounded quadratic form. The span of $e_{1}, \ldots, e_{m}$ has maximal Rayleigh quotient $\lambda_{m}^{\mathrm{TT}}$. Every $m$-dimensional subspace contains a nonzero vector orthogonal to $e_{1}, \ldots, e_{m-1}$, whose Rayleigh quotient is at least $\lambda_{m}^{\mathrm{TT}}$. This proves the min-max formula on smooth TT subspaces. To identify the negative index, let $q$ be the number of TT eigenvalues strictly below $\tau$. It is finite: the corresponding resolvent eigenvalues satisfy $\rho_{j}>(b+\tau)^{-1}$ when $b+\tau>0$, and no such eigenvalues occur when $\tau \leq-b$. The span of these $q$ eigentensors is negative for $Q-\tau\|\cdot\|^{2}$. Any space of dimension greater than $q$ contains a nonzero vector orthogonal to them. Equation (2.30) makes the latter vector's shifted quadratic form nonnegative. Thus this index is exactly $q . \quad \square$

\subsection*{2.3. Orthogonal decomposition.}

Proposition 2.3. Every smooth trace-free symmetric tensor has a decomposition
$$T=H+P \psi+V, \quad H \in \mathrm{TT}, \quad V=\delta^{*} \eta, \quad \delta \eta=0 .$$
The three tensor summands are unique and depend linearly on $T$. They are pairwise orthogonal for the $L^{2}$ inner product and for the bilinear form induced by $Q$. Their divergences are also orthogonal. Moreover,
$$\begin{aligned}
Q(P \psi) & =c_{n}\|\delta P \psi\|_{L^{2}}^{2}+c_{n} \Lambda\|P \psi\|_{L^{2}}^{2}, \\
Q(V) & =2\|\delta V\|_{L^{2}}^{2}+2 \Lambda\|V\|_{L^{2}}^{2} .
\end{aligned}$$
Proof. On trace-free tensors, $\mathcal{K}^{*}=\delta$. By (2.4),
$$\mathcal{B}:=\delta \mathcal{K}=\frac{1}{2} \Delta_{H}-\Lambda I+\left(\frac{1}{2}-\frac{1}{n}\right) d \delta .$$
With the convention $\sigma\left(\partial_{j}\right)(\xi)=i \xi_{j}$, its principal symbol is
$$\sigma_{2}(\mathcal{B})(\xi)=\frac{1}{2}|\xi|^{2} I+\left(\frac{1}{2}-\frac{1}{n}\right) \xi \otimes \xi .$$
It has eigenvalue $|\xi|^{2} / 2$ on $\xi^{\perp}$ and $(n-1)|\xi|^{2} / n$ on $\mathbb{R} \xi$. It is therefore elliptic. Furthermore,
$$\langle\mathcal{B} \omega, \omega\rangle_{L^{2}}=\|\mathcal{K} \omega\|_{L^{2}}^{2}, \quad \operatorname{ker} \mathcal{B}=\operatorname{ker} \mathcal{K} .$$
For $\zeta \in \operatorname{ker} \mathcal{B},\langle\delta T, \zeta\rangle_{L^{2}}=\langle T, \mathcal{K} \zeta\rangle_{L^{2}}=0$. The elliptic spectral theorem for $\mathcal{B}$ on the closed manifold applies: its symbol is positive by (2.35), it is formally self-adjoint, and its form is nonnegative by (2.36). Let ( $\zeta_{j}$ ) be an orthonormal eigenbasis, $\mathcal{B} \zeta_{j}=\beta_{j} \zeta_{j}$, with $\beta_{j} \geq 0$. The orthogonality just proved permits the series
$$\omega=\sum_{\beta_{j}>0} \beta_{j}^{-1}\left\langle\delta T, \zeta_{j}\right\rangle_{L^{2}} \zeta_{j} .$$
Write $u_{j}=\left\langle\delta T, \zeta_{j}\right\rangle_{L^{2}}$ and $\beta_{*}=\min \left\{\beta_{j}: \beta_{j}>0\right\}>0$. Then
$$\sum_{\beta_{j}>0}\left|\beta_{j}^{-1} u_{j}\right|^{2} \leq \beta_{*}^{-2}\|\delta T\|_{L^{2}}^{2}, \quad \sum_{\beta_{j}>0} \beta_{j}^{2}\left|\beta_{j}^{-1} u_{j}\right|^{2}=\|\delta T\|_{L^{2}}^{2} .$$
Thus the series belongs to the operator domain, satisfies $\mathcal{B} \omega=\delta T$, and is orthogonal to ker $\mathcal{B}$. The elliptic regularity in (2.20), iterated with smooth right-hand side, gives $\omega \in C^{\infty}$. If two such solutions existed, their difference would belong to both $\operatorname{ker} \mathcal{B}$ and its orthogonal complement, and would be zero. Set $H=T-\mathcal{K} \omega$. Then $H$ is TT and is orthogonal to $\operatorname{im} \mathcal{K}$.

Since $\int_{M} \delta \omega d v_{g}=0$, solve $\Delta \psi=\delta \omega$ with $\int_{M} \psi d v_{g}=0$. The scalar Laplacian has kernel the constants, so this solution exists and is unique. Set $\eta=\omega-d \psi$. Then $\delta \eta=0$, and $\mathcal{K} \omega=P \psi+\delta^{*} \eta$. Equation (2.34) gives
$$\mathcal{B}(d v)=d\left(\frac{n-1}{n} \Delta v-\Lambda v\right), \quad \delta \mathcal{B} \omega=\left(\frac{n-1}{n} \Delta-\Lambda\right) \delta \omega \quad\left(\omega \in C^{\infty}\left(T^{*} M\right)\right) .$$
Indeed, $\delta \Delta_{H} \omega=\Delta \delta \omega$ and $\delta d \delta \omega=\Delta \delta \omega$; the coefficient of $\Delta \delta \omega$ is $1 / 2+(1 / 2-1 / n)=(n-1) / n$. In particular, $\delta \eta=0$ implies $\delta \mathcal{B} \eta=0$. Thus $\mathcal{B}$ preserves exact and coclosed one-forms. These spaces are orthogonal, since $\langle d u, \eta\rangle_{L^{2}}=\langle u, \delta \eta\rangle_{L^{2}}=0$. It follows that
$$\left\langle P \psi, \delta^{*} \eta\right\rangle_{L^{2}}=\langle d \psi, \mathcal{B} \eta\rangle_{L^{2}}=0, \quad\left\langle\delta P \psi, \delta \delta^{*} \eta\right\rangle_{L^{2}}=0 .$$
The identities $L_{g}(P v)=P \Delta v, L_{g}\left(\delta^{*} \eta\right)=\delta^{*} \Delta_{H} \eta$ and $\delta \Delta_{H} \eta=0$ show that $L_{g}$ preserves the last two spaces. Equation (2.7) gives preservation of the TT space. For summands $T_{i}, T_{j}$ in distinct spaces, $\left\langle L_{g} T_{i}, T_{j}\right\rangle_{L^{2}}=0$ because $L_{g} T_{i}$ remains in the space of $T_{i}$. This proves the asserted $Q$ orthogonality. If two decompositions exist, subtract them and pair with each of the three differences. Each difference has zero squared norm. This proves uniqueness of the tensor summands and therefore their linear dependence on $T$.

Put $\theta=(n-1) / n$ and $u=\theta \Delta \psi-\Lambda \psi$. Then $\delta P \psi=d u$ and
$$\|P \psi\|_{L^{2}}^{2}=\langle d u, d \psi\rangle_{L^{2}}, \quad Q(P \psi)=\langle P \psi, P \Delta \psi\rangle_{L^{2}}=\langle d u, d \Delta \psi\rangle_{L^{2}} .$$
Differentiation of the definition of $u$ gives $d \Delta \psi=c_{n}(d u+\Lambda d \psi)$, proving (2.32). For the coclosed part, (2.34) gives
$$\delta V=\mathcal{B} \eta=\frac{1}{2} \Delta_{H} \eta-\Lambda \eta, \quad\|V\|_{L^{2}}^{2}=\langle\eta, \mathcal{B} \eta\rangle_{L^{2}} .$$
Thus
$$Q(V)=\left\langle\Delta_{H} \eta, \mathcal{B} \eta\right\rangle_{L^{2}}=2\|\mathcal{B} \eta\|_{L^{2}}^{2}+2 \Lambda\langle\eta, \mathcal{B} \eta\rangle_{L^{2}},$$
which proves (2.33). \(\square\)

Theorem 2.4 (Shifted index identity). For every $\tau \leq c_{n} \Lambda$,
$$\operatorname{ind}^{-}\left(\mathcal{J}-\tau\|\cdot\|_{L^{2}}^{2}\right)=\#\left\{j: \lambda_{j}^{\mathrm{TT}}(g)<\tau\right\} .$$
The index on the left is the supremum of the dimensions of subspaces of smooth trace-free tensors on which the indicated form is negative definite.

Proof. Substitute (2.31) into (2.1). Orthogonality and (2.32)-(2.33) give
$$\begin{aligned}
\mathcal{J}(T)-\tau\|T\|_{L^{2}}^{2}= & Q(H)-\tau\|H\|_{L^{2}}^{2}+\left(c_{n} \Lambda-\tau\right)\|P \psi\|_{L^{2}}^{2} \\
& +\left(2-c_{n}\right)\|\delta V\|_{L^{2}}^{2}+(2 \Lambda-\tau)\|V\|_{L^{2}}^{2}
\end{aligned}$$
Since $n \geq 3, c_{n}<2$. Indeed, $2-c_{n}=(n-2) /(n-1)>0, c_{n} \Lambda-\tau \geq 0$, and $2 \Lambda-\tau \geq\left(2-c_{n}\right) \Lambda>0$. If $W$ is a negative subspace for the form on the left, the map $T \mapsto H$ is injective on $W$ : a nonzero element in its kernel would have nonnegative energy. Its image is negative for $Q-\tau\|\cdot\|_{L^{2}}^{2}$. Conversely, on TT tensors the two forms agree. Lemma 2.2 identifies the latter index with the right-hand side of (2.44). \(\square\)

Corollary 2.5. Suppose a space $\mathcal{V}$ of smooth trace-free tensors has dimension $m$ and, for some $\beta<c_{n} \Lambda$,
$$\mathcal{J}(T) \leq \beta\|T\|_{L^{2}}^{2} \quad(T \in \mathcal{V}) .$$
Then $\lambda_{m}^{\mathrm{TT}}(g) \leq \beta$. If the inequality in (2.46) is strict for every nonzero $T$, then $\lambda_{m}^{\mathrm{TT}}(g)<\beta$.
Proof. For every $\tau$ with $\beta<\tau<c_{n} \Lambda, \mathcal{V}$ is negative for $\mathcal{J}-\tau\|\cdot\|_{L^{2}}^{2}$. Theorem 2.4 gives at least $m$ TT eigenvalues below $\tau$. Letting $\tau \downarrow \beta$ gives the first conclusion. In the strict case, the set $\left\{T \in \mathcal{V}:\|T\|_{L^{2}}=1\right\}$ is compact. Let
$$\beta_{0}=\max _{\substack{T \in \mathcal{V} \\\|T\|_{L^{2}=1}}} \mathcal{J}(T) .$$
Continuity gives an attaining tensor $T_{0}$; the strict hypothesis at $T_{0}$ gives $\beta_{0}<\beta$. Homogeneity implies $\mathcal{J}(T) \leq \beta_{0}\|T\|_{L^{2}}^{2}$ on $\mathcal{V}$. The first conclusion, applied to $\beta_{0}$, yields $\lambda_{m}^{\mathrm{TT}} \leq \beta_{0}<\beta$. \(\square\)

Remark 2.6 (The critical coefficient). The coefficient $c_{n}$ cannot be increased while preserving finite negative index on the subspace $\operatorname{im} P$. Let $\Delta v=\mu v$ and $\|v\|_{L^{2}}=1$. Equation (2.3) gives $\left\|\nabla^{2} v\right\|^{2}=$ $\left\langle\nabla^{*} \nabla d v, d v\right\rangle=(\mu-\Lambda)\|d v\|^{2}=\mu(\mu-\Lambda)$. Since $\operatorname{tr} \nabla^{2} v=-\mu v$ and $|g|^{2}=n$, expansion of $P v$ gives
$$\|P v\|_{L^{2}}^{2}=\frac{n-1}{n} \mu^{2}-\Lambda \mu, \quad\|\delta P v\|_{L^{2}}^{2}=\left(\frac{n-1}{n} \mu-\Lambda\right)\|P v\|_{L^{2}}^{2} .$$
Consequently
$$Q(P v)-\gamma\|\delta P v\|_{L^{2}}^{2}=\left[\left(1-\gamma \frac{n-1}{n}\right) \mu+\gamma \Lambda\right]\|P v\|_{L^{2}}^{2} .$$
For $\gamma>c_{n}$ this coefficient is negative at every sufficiently large scalar eigenvalue. If $v_{i}, v_{j}$ are orthonormal scalar eigenfunctions with eigenvalues $\mu_{i}, \mu_{j}$, integration by parts gives
$$\begin{aligned}
\left\langle P v_{i}, P v_{j}\right\rangle_{L^{2}} & =\left(\frac{n-1}{n} \mu_{i}-\Lambda\right) \mu_{j}\left\langle v_{i}, v_{j}\right\rangle_{L^{2}}, \\
\left\langle\delta P v_{i}, \delta P v_{j}\right\rangle_{L^{2}} & =\left(\frac{n-1}{n} \mu_{i}-\Lambda\right)\left(\frac{n-1}{n} \mu_{j}-\Lambda\right) \mu_{j}\left\langle v_{i}, v_{j}\right\rangle_{L^{2}} .
\end{aligned}$$

Both pairings vanish for $i \neq j$. For all sufficiently large $i,\left\|P v_{i}\right\|^{2}>0$ by (2.48). Their finite spans have arbitrarily large negative dimension. No ellipticity assertion for the critically penalized operator on all trace-free tensors is used in Theorem 2.4.

\section*{3. Conformal harmonic forms and a spectral bound}
3.1. The conformal identity. For an oriented metric $k$ in dimension four, write $\Lambda^{2}=\Lambda^{+} \oplus \Lambda^{-}$. Associate to a two-form $\alpha$ the skew-adjoint endomorphism $A_{\alpha}$ defined by $k\left(A_{\alpha} X, Y\right)=\alpha(X, Y)$. For $\alpha \in \Lambda^{-}$and $\beta \in \Lambda^{+}$, put
$$\left(\alpha{ }_{\circ} k \beta\right)(X, Y)=k\left(A_{\alpha} A_{\beta} X, Y\right) .$$
The endomorphisms of opposite duality commute. Their product is self-adjoint and has zero trace. Use the bases
$$\begin{array}{llll}
\Lambda^{+}: & e^{12}+e^{34}, & e^{13}-e^{24}, & e^{14}+e^{23}, \\
\Lambda^{-}: & e^{12}-e^{34}, & e^{13}+e^{24}, & e^{14}-e^{23} .
\end{array}$$
Denote the associated matrices by $I_{a}^{+}$and $I_{b}^{-}$. Their entries are obtained from $\left(A_{\alpha}\right)^{i}{ }_{j}=\alpha_{j i}$, and multiplication gives
$$\left(I_{a}^{ \pm}\right)^{\top}=-I_{a}^{ \pm}, \quad I_{a}^{+} I_{b}^{-}=I_{b}^{-} I_{a}^{+}, \quad \operatorname{tr}\left(I_{a}^{+} I_{b}^{-}\right)=0 \quad(1 \leq a, b \leq 3) .$$
Expanding $A_{\alpha}$ and $A_{\beta}$ in these bases proves commutation and zero trace. Also $\left(A_{\alpha} A_{\beta}\right)^{\top}=A_{\beta} A_{\alpha}=$ $A_{\alpha} A_{\beta}$, which proves symmetry.

If $k$ is Kähler, its Kähler form $\Omega$ satisfies $A_{\Omega}=J, J^{2}=-I$, and $\nabla^{k} \Omega=0$. Therefore
$$\left|\omega{ }_{k} \Omega\right|_{k}^{2}=2|\omega|_{k}^{2} .$$
Indeed, multiplication by the orthogonal endomorphism $J$ preserves the Hilbert-Schmidt norm, and $\left|A_{\omega}\right|_{\mathrm{HS}}^{2}=2|\omega|_{k}^{2}$. Thus $\omega \mapsto \omega_{\circ} \Omega$ is injective.

We use the following conformal operator identity, independently of the TT projection in Section 2. Delay's conformally covariant tensor operator [9] precedes the construction used here. The conformal identities in the next proposition are those of Biquard-Ozuch. Its conformal covariance is the external input specified below.

Proposition 3.1 (Biquard-Ozuch). There is a natural second-order operator $\mathcal{P}_{k}$ on trace-free symmetric tensors over any oriented Riemannian four-manifold such that, for a positive function $f$,
$$\mathcal{P}_{f^{2} k}(T)=f^{-1} \mathcal{P}_{k}\left(f^{-1} T\right) .$$
If $g$ is Einstein, then
$$\frac{1}{2} \nabla_{g}^{*} \nabla_{g}-\stackrel{\circ}{R}_{g}=\boldsymbol{\mathcal { P }}_{g}+\frac{2}{3} \boldsymbol{\mathcal { K }}_{g} \delta_{g}-\frac{\mathrm{Scal}_{g}}{12} I .$$
If $k$ is Kähler and $\omega$ is a harmonic anti-self-dual two-form, then
$$\mathcal{P}_{k}\left(\omega \circ_{k} \Omega\right)=-\frac{s_{k}}{6}\left(\omega \circ_{k} \Omega\right), \quad \delta_{k}\left(\omega \circ_{k} \Omega\right)=0 .$$

Equations (3.5) and (3.6) are [3, Proposition 3 and equation (12)]. Their symbol $L$ denotes the operator on the left of (3.6), not $L_{g}$ in (1.3); their $\delta_{0}^{*}$ is $\mathcal{K}_{g}$. Let $d_{-}^{*}$ denote the adjoint of the covariant exterior derivative followed by anti-self-dual projection. It maps $\Lambda^{-} \otimes \Lambda^{+}$to $T^{*} M \otimes \Lambda^{+}$. Define
$$\begin{aligned}
\pi(\alpha \otimes \beta) & =\alpha \wedge \beta, & \sigma(\zeta) & \left.=\sum_{i} e^{i} \otimes\left(e_{i}\right\lrcorner \zeta\right)_{+}, \\
\mathcal{D}_{k} & =\left(I-\frac{2}{3} \sigma \pi\right) d_{-}^{*}, & \mathcal{P}_{k} & =\mathcal{D}_{k}^{*} \mathcal{D}_{k}-W_{k}^{+}
\end{aligned}$$
Here $\pi: T^{*} M \otimes \Lambda^{+} \rightarrow \Lambda^{3} T^{*} M$ and $\sigma: \Lambda^{3} T^{*} M \rightarrow T^{*} M \otimes \Lambda^{+}$. For a three-form $\zeta$,
$$\begin{aligned}
\pi \sigma \zeta & \left.\left.=\frac{1}{2} \sum_{i} e^{i} \wedge\left(e_{i}\right\lrcorner \zeta\right)+\frac{1}{2} \sum_{i} e^{i} \wedge *\left(e_{i}\right\lrcorner \zeta\right)=\frac{3}{2} \zeta, \\
\langle\sigma \zeta, \alpha \otimes \beta\rangle & =\langle\zeta, \alpha \wedge \beta\rangle \quad\left(\alpha \in T^{*} M, \beta \in \Lambda^{+}\right) .
\end{aligned}$$

The first sum is $3 \zeta$ before multiplication by $1 / 2$. The second is zero because $\left.*\left(e_{i}\right\lrcorner \zeta\right)=e^{i} \wedge * \zeta$. The second line proves $\sigma^{*}=\pi$. Hence $\Pi=I-\frac{2}{3} \sigma \pi$ satisfies $\Pi^{*}=\Pi, \Pi^{2}=\Pi, \pi \Pi=0$, and $\left.\Pi\right|_{\text {ker } \pi}=I$. It is the orthogonal projection onto ker $\pi$. The action of $W_{k}^{+}$on $\Lambda^{-} \otimes \Lambda^{+}$is on the second factor. These are the constructions in [3, equations (7)-(13)], transported by (3.1). On $\omega \otimes \Omega, d_{-}^{*}$ vanishes because $\delta \omega=0$ and $\nabla \Omega=0$. The Kähler curvature identity $W_{k}^{+}(\Omega)=\left(s_{k} / 6\right) \Omega$ therefore gives the first equality in (3.7); this is [3, equation (26)]. For the divergence, the chosen composition is $\left(\omega{ }^{\circ}{ }_{k} \Omega\right)_{i j}=\omega_{p i} J^{p}{ }_{j}$. Since $\nabla J=0$ and $\omega_{p i}=-\omega_{i p}$,
$$\left(\delta_{k}\left(\omega \circ_{k} \Omega\right)\right)_{j}=-\left(\nabla^{i} \omega_{p i}\right) J^{p}{ }_{j}=\left(\nabla^{i} \omega_{i p}\right) J^{p}{ }_{j}=0 .$$
The identity (3.5) applies to arbitrary Riemannian four-metrics, whereas (3.6) is used only for the Einstein metric $g$.
3.2. Normalization and the trial space. The conformal Kähler-Einstein normalization of Derdziński [11, Proposition 5], in the form [3, equation (22)], says that $f_{0} s_{k_{0}}$ is a positive constant. It includes the constant-conformal-factor case. If that constant is $c$, set
$$a=(c / 6)^{1 / 3}, \quad k=a^{2} k_{0}, \quad f=f_{0} / a .$$
Since $s_{a^{2} k_{0}}=a^{-2} s_{k_{0}}$, this choice gives $f s_{k}=a^{-3} f_{0} s_{k_{0}}=a^{-3} c=6$. Therefore
$$g=f^{2} k, \quad s_{k}=6 f^{-1}, \quad \frac{f_{\max }}{f_{\min }}=\frac{\max s_{k}}{\min s_{k}}=\rho .$$
The homothety in (3.11) changes neither the complex orientation nor the scalar-curvature ratio.
Let
$$\mathcal{H}_{k}^{-}=\left\{\omega \in C^{\infty}\left(\Lambda^{2} T^{*} M\right): d \omega=0, \delta_{k} \omega=0, *_{k} \omega=-\omega\right\} .$$
By the Hodge theorem, $\operatorname{dim} \mathcal{H}_{k}^{-}=b_{2}^{-}(M)$. Under a conformal change in dimension four the Hodge star on two-forms is unchanged: the factor for degree $p$ is $f^{4-2 p}$, which is one when $p=2$. A closed anti-self-dual two-form is coclosed because $\delta=-* d *$ on two-forms. Hence the space in (3.13) is the same for $k$ and $g$. For $\omega \in \mathcal{H}_{k}^{-}$define
$$\begin{gathered}
\widetilde{T}_{\omega}=\omega \circ k \Omega, \quad T_{\omega}=f \widetilde{T}_{\omega} . \\
\operatorname{tr}_{g} T_{\omega}=f^{-1} \operatorname{tr}_{k} \widetilde{T}_{\omega}=0, \quad\left|T_{\omega}\right|_{g}^{2}=f^{-2}\left|\widetilde{T}_{\omega}\right|_{k}^{2}=2 f^{-2}|\omega|_{k}^{2} .
\end{gathered}$$
Thus both tensors are trace-free and the map $\omega \mapsto T_{\omega}$ is injective.
Lemma 3.2. For every $\omega \in \mathcal{H}_{k}^{-}$,
$$\mathcal{P}_{g} T_{\omega}=-f^{-3} T_{\omega}$$
and
$$\mathcal{J}_{g}\left(T_{\omega}\right)=\int_{M}\left(4-2 f^{-3}\right)\left|T_{\omega}\right|_{g}^{2} d v_{g}$$
Here $\mathcal{J}_{g}=Q_{g}-\frac{4}{3}\left\|\delta_{g}(\cdot)\right\|_{L^{2}}^{2}$.
Proof. Apply (3.5) and (3.7) to (3.14). Since $s_{k} / 6=f^{-1}$,
$$\mathcal{P}_{g} T_{\omega}=f^{-1} \mathcal{P}_{k} \widetilde{T}_{\omega}=-f^{-2} \widetilde{T}_{\omega}=-f^{-3} T_{\omega} .$$
For $\operatorname{Ric}_{g}=3 g, \operatorname{Scal}_{g}=12$, and (3.6) becomes
$$L_{g}=2 \mathcal{P}_{g}+\frac{4}{3} \mathcal{K}_{g} \delta_{g}+4 I .$$
For trace-free tensors $T,\left\langle\mathcal{K}_{g} \delta_{g} T, T\right\rangle_{L^{2}}=\left\|\delta_{g} T\right\|_{L^{2}}^{2}$. Pair (3.19) with $T_{\omega}$ and use (3.16). Subtracting the divergence term gives (3.17). \(\square\)

Lemma 3.3. The function $f$ satisfies
$$\Delta_{k} f=2 f^{3}-1, \quad \frac{1}{\operatorname{Vol}_{k}(M)} \int_{M} f^{3} d v_{k}=\frac{1}{2} .$$
Consequently
$$f^{-3} \geq \frac{2}{\rho^{3}}$$
If $f$ is nonconstant, the inequality in (3.21) is strict at every point.
Proof. For $u=\log f$, the connection difference is
$$\nabla_{X}^{f^{2} k} Y-\nabla_{X}^{k} Y=d u(X) Y+d u(Y) X-k(X, Y) \nabla^{k} u .$$
In local coordinates, put $C_{i j}^{p}=\delta_{i}^{p} u_{j}+\delta_{j}^{p} u_{i}-k_{i j} u^{p}$ and $D_{k} u=\nabla^{p} \nabla_{p} u=-\Delta_{k} u$. Then
$$\begin{aligned}
\nabla_{p} C_{i j}^{p} & =2 \nabla_{i} \nabla_{j} u-k_{i j} D_{k} u, \quad \nabla_{j} C_{i p}^{p}=4 \nabla_{i} \nabla_{j} u, \\
C_{p q}^{p} C_{i j}^{q}-C_{j q}^{p} C_{i p}^{q} & =2 u_{i} u_{j}-2|d u|_{k}^{2} k_{i j} .
\end{aligned}$$
The curvature difference is the difference of the first two terms plus the last term. Thus
$$\operatorname{Ric}_{f^{2} k}=\operatorname{Ric}_{k}-2 \nabla_{k}^{2} u+2 d u \otimes d u+\left(\Delta_{k} u-2|d u|_{k}^{2}\right) k .$$
Take the $f^{2} k$ trace. This gives
$$\text { Scal }_{f^{2} k}=f^{-2}\left(s_{k}+6 \Delta_{k} u-6|d u|_{k}^{2}\right)=f^{-3}\left(6 \Delta_{k} f+s_{k} f\right) .$$
The second equality uses $\Delta_{k} \log f=f^{-1} \Delta_{k} f+f^{-2}|d f|_{k}^{2}$. Substitute $\operatorname{Scal}_{g}=12$ and $s_{k} f=6$, and integrate on the closed manifold. This proves (3.20). It follows that
$$f_{\min }^{3} \leq \frac{1}{2}, \quad f_{\max }^{3}=\rho^{3} f_{\min }^{3} \leq \frac{\rho^{3}}{2} .$$
This proves (3.21). If $f$ is nonconstant, choose $x_{0}$ with $f\left(x_{0}\right)>f_{\text {min }}$. Continuity gives an open neighborhood $U$ of $x_{0}$ and $d>0$ such that $f^{3}-f_{\text {min }}^{3} \geq d$ on $U$. Thus $\int_{M}\left(f^{3}-f_{\text {min }}^{3}\right) d v_{k} \geq d \operatorname{Vol}_{k}(U)>0$. The first inequality in (3.26) is then strict, as are the second and (3.21). \(\square\)

Proof of Theorem A. By Lemmas 3.2 and 3.3,
$$\mathcal{J}_{g}\left(T_{\omega}\right) \leq\left(4-\frac{4}{\rho^{3}}\right)\left\|T_{\omega}\right\|_{L^{2}}^{2} .$$
The tensors (3.14) form a space of dimension $m$. The coefficient in (3.27) is strictly less than $4=c_{4} \Lambda$. Corollary 2.5 proves (1.5). If $f$ is nonconstant, put
$$\epsilon=2 f_{\max }^{-3}-\frac{4}{\rho^{3}}>0$$
Equations (3.17) and (3.21) give $\mathcal{J}_{g}\left(T_{\omega}\right) \leq\left(4-4 / \rho^{3}-\epsilon\right)\left\|T_{\omega}\right\|^{2}$. Applying Corollary 2.5 proves the strict conclusion. If $f$ is constant, (3.20) gives $f^{3}=1 / 2$. Then $\delta_{g} T_{\omega}=0$, by (3.7) and constant rescaling, while (3.19) gives $L_{g} T_{\omega}=\left(4-2 f^{-3}\right) T_{\omega}=0$. Injectivity proves (1.6). \(\square\)

Corollary 3.4. Under the hypotheses of Theorem $A, \rho^{3}<16$ implies that the Ricci-flat cone is unstable. If $\rho<2$, then $\lambda_{m}^{\mathrm{TT}}(g)<7 / 2$.

Proof. The inequality $4-4 / \rho^{3}<15 / 4$ is equivalent to $\rho^{3}<16$. The separated cone calculation is Proposition 8.1. If $\rho<2$, then $4-4 / \rho^{3}<7 / 2$. \(\square\)

\section*{4. Scalar-curvature ratios from toric moments}

The two calculations in this section use moment polygons only. For a toric Kähler surface with affine scalar curvature, the affine scalar function, up to a positive constant depending on the angular-period convention, is characterized by
$$\int_{P} \ell p d x=\int_{\partial P} p d \sigma \quad \text { for every affine function } p .$$
Here $d \sigma$ is lattice boundary measure. The identity is Donaldson's integration formula, in the normalization of [14, Lemma 7.3]; its affine specialization is all that is used. A positive constant multiple of $\ell$ has the same ratio of extrema. Uniqueness in (4.1) follows because the difference of two solutions is affine and has zero squared integral over $P$.
4.1. The Page trapezoid. The Kähler metric conformal to the Page metric has moment polygon
$$T_{a}=\left\{\left(x_{1}, x_{2}\right): x_{1} \geq 0, x_{2} \geq 0, a \leq x_{1}+x_{2} \leq 1\right\}, \quad 0<a<1,$$
as in [14, Section 7.1]. Put $t=x_{1}+x_{2}$. Integration over $0 \leq x_{1} \leq t, a \leq t \leq 1$, gives
$$\int_{T_{a}} t^{j} d x=\frac{1-a^{j+2}}{j+2} \quad(j=0,1,2), \quad \int_{\partial T_{a}} d \sigma=3-a, \quad \int_{\partial T_{a}} t d \sigma=2 .$$
For the last two integrals the coordinate edges contribute $2(1-a)$ and $1-a^{2}$, respectively, while the edges $t=1$ and $t=a$ contribute $1+a$ and $1+a^{2}$. If the normalized affine function is $A_{0} t+B_{0}$, (4.1) gives
$$A_{0} \frac{1-a^{3}}{3}+B_{0} \frac{1-a^{2}}{2}=3-a, \quad A_{0} \frac{1-a^{4}}{4}+B_{0} \frac{1-a^{3}}{3}=2 .$$
Its solution is
$$A_{0}=\frac{24 a}{(1-a)\left(a^{2}+4 a+1\right)}, \quad B_{0}=\frac{6\left(1-3 a^{2}\right)}{(1-a)\left(a^{2}+4 a+1\right)} .$$
To verify both equations, write $D_{P}=(1-a)\left(a^{2}+4 a+1\right)$. After multiplication by $D_{P}$, their left sides are, respectively,
$$\begin{aligned}
& 8 a\left(1-a^{3}\right)+3\left(1-3 a^{2}\right)\left(1-a^{2}\right)=(3-a) D_{P}, \\
& 6 a\left(1-a^{4}\right)+2\left(1-3 a^{2}\right)\left(1-a^{3}\right)=2 D_{P} .
\end{aligned}$$
Each equality follows by multiplying the displayed polynomials. Since $D_{P}>0$ for $0<a<1$, these equations verify the solution. Uniqueness follows from (4.1). The scalar curvature is therefore a positive multiple of
$$\ell_{a}(t)=4 a t+1-3 a^{2} .$$
The slope is positive, so
$$\rho_{\mathrm{P}}=\frac{\ell_{a}(1)}{\ell_{a}(a)}=\frac{1+4 a-3 a^{2}}{1+a^{2}} .$$
The denominator is positive and
$$2\left(1+a^{2}\right)-\left(1+4 a-3 a^{2}\right)=5 a^{2}-4 a+1=5\left(a-\frac{2}{5}\right)^{2}+\frac{1}{5}>0 .$$
Therefore $\rho_{\mathrm{P}}<2$ for every $0<a<1$. No value of the conformally Einstein parameter is required.
4.2. The Chen-LeBrun-Weber pentagon. The Kähler representative of the Chen-LeBrun-Weber metric is bilaterally symmetric. Up to homothety, its polygon is
$$P_{a}=\operatorname{conv}\{(0,0),(a, 0),(a, 1),(1, a),(0, a)\}, \quad a>1 .$$
The existence and symmetry are part of [8]; the polygon normalization is [14, Section 7.2]. Symmetry and uniqueness in (4.1) give
$$\ell\left(x_{1}, x_{2}\right)=A\left(x_{1}+x_{2}\right)+B .$$
Write $I_{i j}=\int_{P_{a}} x_{1}^{i} x_{2}^{j} d x$.

Lemma 4.1. The moments needed for (4.1) are
$$\begin{aligned}
I_{00} & =\frac{a^{2}+2 a-1}{2}, & I_{10}=I_{01} & =\frac{a^{3}+3 a^{2}-1}{6}, \\
I_{20}=I_{02} & =\frac{a^{4}+4 a^{3}-1}{12}, & I_{11} & =\frac{a^{4}+4 a^{3}+6 a^{2}-4 a-1}{24} .
\end{aligned}$$
The boundary moments are
$$E_{0}=\int_{\partial P_{a}} d \sigma=1+3 a, \quad E_{1}=\int_{\partial P_{a}} x_{1} d \sigma=\int_{\partial P_{a}} x_{2} d \sigma=a^{2}+a$$
Proof. The polygon is the square $[0, a]^{2}$ minus the open triangle $x_{1}+x_{2}>a+1$. For nonnegative integers $i, j$,
$$I_{i j}=\frac{a^{i+j+2}}{(i+1)(j+1)}-\frac{1}{j+1} \int_{1}^{a} x^{i}\left[a^{j+1}-(a+1-x)^{j+1}\right] d x$$
For $j=0$, this is
$$I_{i 0}=\frac{a^{i+2}}{i+1}-\frac{a^{i+2}-1}{i+2}+\frac{a^{i+1}-1}{i+1} .$$
Substitution of $i=0,1,2$ gives $I_{00}, I_{10}, I_{20}$. For $i=j=1$, the removed integral is
$$\frac{1}{2} \int_{1}^{a} x\left[a^{2}-(a+1-x)^{2}\right] d x=\frac{5 a^{4}-4 a^{3}-6 a^{2}+4 a+1}{24} .$$
Subtracting this from $a^{4} / 4$ gives $I_{11}$. Interchange of coordinates gives $I_{01}$ and $I_{02}$.
The five edge measures are $a, 1, a-1,1, a$. On the diagonal edge $x_{2}=a+1-x_{1}$, the primitive normal is (1, 1), so its lattice measure is $d x_{1}$, not its Euclidean arclength. The corresponding contributions to the first $x_{1}$ moment are
$$\frac{a^{2}}{2}, \quad a, \quad \frac{a^{2}-1}{2}, \quad \frac{1}{2}, \quad 0 .$$
Their sum is $a^{2}+a$; the edge measures sum to $1+3 a$. \(\square\)

Proposition 4.2. For every $a>1$, the affine solution of (4.1) on $P_{a}$ is positive and satisfies
$$\frac{\max _{P_{a}} \ell}{\min _{P_{a}} \ell}<2 .$$
Proof. The tests $p=1, x_{1}$ give
$$2 I_{10} A+I_{00} B=E_{0}, \quad\left(I_{20}+I_{11}\right) A+I_{10} B=E_{1} .$$
Set $x=a-1>0$ and define
$$\begin{aligned}
& D(x)=x^{6}+12 x^{5}+54 x^{4}+120 x^{3}+138 x^{2}+72 x+12, \\
& U(x)=x^{5}+12 x^{4}+44 x^{3}+72 x^{2}+50 x+8, \\
& V(x)=x^{5}+8 x^{4}+24 x^{3}+36 x^{2}+26 x+8 .
\end{aligned}$$
Substitution of Lemma 4.1 gives the identities
$$\begin{aligned}
I_{00}\left(I_{20}+I_{11}\right)-2 I_{10}^{2} & =\frac{D(x)}{144}, \\
E_{1} I_{00}-E_{0} I_{10} & =-\frac{x\left(x^{2}+3 x+3\right)}{6}, \\
E_{0}\left(I_{20}+I_{11}\right)-2 E_{1} I_{10} & =\frac{U(x)}{24} .
\end{aligned}$$
Set $J=I_{20}+I_{11}$ and $\mathfrak{d}=I_{00} J-2 I_{10}^{2}=D(x) / 144>0$. Multiplying the second equation in (4.20) by $I_{00}$ and subtracting $I_{10}$ times the first gives $\mathfrak{d} A=E_{1} I_{00}-E_{0} I_{10}$. Multiplying the first by $J$ and subtracting $2 I_{10}$ times the second gives $\mathfrak{d} B=E_{0} J-2 E_{1} I_{10}$. Substitution of (4.25)-(4.26) yields
$$A=-\frac{24 x\left(x^{2}+3 x+3\right)}{D(x)}<0, \quad B=\frac{6 U(x)}{D(x)} .$$

The linear function $x_{1}+x_{2}$ has minimum 0 and maximum $a+1=x+2$ on $P_{a}$. Hence
$$\ell_{\max }=B=\frac{6 U(x)}{D(x)}, \quad \ell_{\min }=B+(x+2) A=\frac{6 V(x)}{D(x)} .$$
The last equality follows from
$$U(x)-4 x(x+2)\left(x^{2}+3 x+3\right)=V(x) .$$
All coefficients of $V$ are positive, so $\ell_{\text {min }}>0$. Finally,
$$2 V(x)-U(x)=x^{5}+4 x^{4}+4 x^{3}+2 x+8>0 .$$
Dividing by $V(x)>0$ proves (4.19). \(\square\)

Remark 4.3. The scalar curvature in the normalization of Hall-Murphy [16] is twice the affine function $\ell$ used above. In the parameter $a$, set
$$D_{a}=a^{6}+6 a^{5}+9 a^{4}+4 a^{3}-3 a^{2}-6 a+1 .$$
Expansion of $D(a-1)$ gives $D_{a}$. The coefficients above satisfy
$$\begin{aligned}
& 2 A=\frac{48\left(1-a^{3}\right)}{D_{a}}, \\
& 2 B=\frac{12\left(a^{5}+7 a^{4}+6 a^{3}+2 a^{2}-5 a-3\right)}{D_{a}} .
\end{aligned}$$
The first expression is the corrected coefficient in the published erratum. The second is its unchanged constant term. Multiplication by two leaves $\max \ell / \min \ell$ unchanged. Thus the scalar-ratio calculation uses the corrected affine data, independently of a numerical approximation to the Einstein metric.

Proof of the spectral assertion in Theorem C. In the complex orientations, the intersection forms of the Page and Chen-LeBrun-Weber manifolds are $\langle 1\rangle \oplus\langle-1\rangle$ and $\langle 1\rangle \oplus 2\langle-1\rangle$. Thus their values of $b_{2}^{-}$are 1 and 2. Equations (4.9) and (4.19) give $\rho<2$. Theorem A gives (1.11). \(\square\)

\section*{5. Affine moment potentials and the scalar spectrum}
5.1. Toric conventions. Let ( $M^{4}, k$ ) be a closed connected toric Kähler surface, with moment map $\mu: M \rightarrow P \subset \mathbb{R}^{2}$. The torus coordinates have period $2 \pi$. On the inverse image of the polygon interior,
$$k=u_{i j} d x_{i} d x_{j}+U^{i j} d \theta_{i} d \theta_{j}, \quad\left(U^{i j}\right)=\left(u_{i j}\right)^{-1}, \quad d v_{k}=d x_{1} d x_{2} d \theta_{1} d \theta_{2} .$$
The symplectic potential has boundary expression $u=\frac{1}{2} \sum_{\alpha} l_{\alpha} \log l_{\alpha}+v$, with $v$ smooth on $P$. Here $l_{\alpha}$ are the primitive affine defining functions of the facets. Lattice boundary measure on each facet is Euclidean arclength divided by the length of its primitive normal. In these conventions, Donaldson's integration identity is
$$\int_{P} U^{i j} \Phi_{i j} d x=2 \int_{\partial P} \Phi d \sigma-\int_{P} s_{k} \Phi d x \quad\left(\Phi \in C^{\infty}(\bar{P})\right)$$
We use [12, Section 2] in the normalization of [17, Proposition 2.1]; that proposition explicitly records the factor 2 associated with the factor 1/2 in $u$. In particular, the function $\ell$ in (4.1) is $s_{k} / 2$. The complement of the dense torus orbit is the union of the inverse images of the facets and vertices: the facet preimages are two-dimensional invariant submanifolds and the vertex preimages are points. There are finitely many. This complement has four-dimensional Riemannian measure zero. Thus integration of a torus-invariant function over $M$ is $(2 \pi)^{2}$ times its integral over $P$.

An affine function on $P$ will also denote its smooth pullback by $\mu$. Let $w$ be a positive affine function and set $h=w^{-2} k$. Assume that $h$ has constant scalar curvature $\kappa$. The Einstein condition is not imposed in the following proposition.

Proposition 5.1 (Weighted affine energy). For affine functions $q, r$ on $P$, put
$$\mathrm{A}(q, r)=\int_{P} q r w^{-6} d x, \quad \mathrm{~B}(q, r)=\int_{\partial P} q r w^{-4} d \sigma$$
Then
$$\begin{aligned}
\frac{1}{4 \pi^{2}} \int_{M}(q / w)(r / w) d v_{h} & =\mathrm{A}(q, r) \\
\frac{1}{4 \pi^{2}} \int_{M}\langle d(q / w), d(r / w)\rangle_{h} d v_{h} & =\mathrm{B}(q, r)-\frac{\kappa}{2} \mathrm{~A}(q, r)
\end{aligned}$$
Proof. Since $h=w^{-2} k$ in real dimension four,
$$d v_{h}=w^{-4} d v_{k}, \quad|d(q / w)|_{h}^{2} d v_{h}=w^{-2}|d(q / w)|_{k}^{2} d v_{k} .$$
Multiplication of the first equality by $(q / w)(r / w)$ and integration over the angular coordinates gives (5.4). Both sides of (5.5) are symmetric bilinear forms in $q, r$. Their equality follows from equality on the diagonal by $4 B(q, r)=B(q+r, q+r)-B(q-r, q-r)$. Define
$$\begin{aligned}
& A=\int_{P} w^{-4}|d q|_{k}^{2} d x, \quad B=\int_{P} q w^{-5}\langle d q, d w\rangle_{k} d x \\
& C=\int_{P} q^{2} w^{-6}|d w|_{k}^{2} d x, \quad T=\int_{P} s_{k} q^{2} w^{-4} d x
\end{aligned}$$
The squared norms in these integrals mean contraction with $U^{i j}$ on the polygon interior. They are integrable because the underlying functions are smooth on the compact manifold. Set $I=\mathrm{A}(q, q)$ and $J=\mathrm{B}(q, q)$. The energy divided by $4 \pi^{2}$ is $E=A-2 B+C$. Affineness of $q$ and $w$ gives
$$\left(q^{2} w^{-4}\right)_{i j}=2 w^{-4} q_{i} q_{j}-8 q w^{-5}\left(q_{i} w_{j}+w_{i} q_{j}\right)+20 q^{2} w^{-6} w_{i} w_{j} .$$
Apply (5.2) to $q^{2} w^{-4}$, which is smooth on $\bar{P}$ since $w>0$. The result is
$$2 A-16 B+20 C=2 J-T .$$
Write $D_{k}=\operatorname{div}_{k} \nabla=-\Delta_{k}$. Substituting $f=w^{-1}$ in (3.25) gives
$$\kappa=w^{2} s_{k}+6 w D_{k} w-12|d w|_{k}^{2} .$$
All factors in the vector field $q^{2} w^{-5} \nabla^{k} w$ are smooth on $M$. Since $M$ has no boundary,
$$\int_{M} \operatorname{div}_{k}\left(q^{2} w^{-5} \nabla^{k} w\right) d v_{k}=0$$
Multiply (5.10) by $q^{2} w^{-6}$ and integrate. Expanding the displayed divergence and dividing by $4 \pi^{2}$ gives
$$\int_{P} q^{2} w^{-5} D_{k} w d x=-\int_{P}\left\langle d\left(q^{2} w^{-5}\right), d w\right\rangle_{k} d x=-2 B+5 C$$
Consequently
$$\kappa I=T-12 B+18 C .$$
The two linear identities yield
$$E=A-2 B+C=J-\frac{1}{2} T+6 B-9 C=J-\frac{\kappa}{2} I .$$
Replace $q$ successively by $q+r$ and $q-r$, subtract the two identities, and divide by 4. This proves (5.5). \(\square\)

Remark 5.2. Proposition 5.1 is a specialization of the weighted toric integration identities of Apostolov-Maschler [1, equations (22), (30)-(31)]. Their formula in complex dimension two reads
$$\int_{P} w^{-3} U^{i j} \Phi_{i j} d x=2 \int_{\partial P} \Phi w^{-3} d \sigma-\kappa \int_{P} \Phi w^{-5} d x$$
For $F=q / w$ and $\Phi=q^{2} / w$, differentiation gives $\Phi_{i j}=2 w F_{i} F_{j}$. Thus (5.14) also proves (5.5). The proof above derives the same conclusion from the unweighted identity and the conformal scalar-curvature law.
5.2. A two-dimensional Rayleigh-Ritz problem. Let $\operatorname{Aff}(P)$ be the three-dimensional real vector space of affine functions on $P$, and put
$$\mathcal{A}_{0}=\left\{q \in \operatorname{Aff}(P): \int_{P} q w^{-5} d x=0\right\} .$$
The functional defining this kernel is nonzero: its value at $q=w$ is $\int_{P} w^{-4} d x>0$. Thus $\operatorname{dim} \mathcal{A}_{0}=2$. For $q \in \mathcal{A}_{0}, q / w$ has zero $h$-mean. A nonzero such function is not constant, since $q / w=c$ would give $c \int_{P} w^{-4} d x=0$ and hence $q=0$.

Corollary 5.3. Let $r_{1} \leq r_{2}$ be the two generalized eigenvalues of $\left(\mathrm{B}-\frac{\kappa}{2} \mathrm{~A}, \mathrm{~A}\right)$ on $\mathcal{A}_{0}$. Then $r_{1}, r_{2}>0$ and
$$\lambda_{j}^{\mathrm{sc}}(h) \leq r_{j} \quad(j=1,2) .$$
Moreover, if $V_{w}=\int_{P} w^{-4} d x$ and $K_{w}=\int_{\partial P} w^{-2} d \sigma$, then
$$\kappa=\frac{2 K_{w}}{V_{w}} .$$
Proof. The form A is positive definite on $\operatorname{Aff}(P)$ : an affine function with zero squared integral on a polygon with nonempty interior is zero. On $\mathcal{A}_{0}$, (5.5) identifies the other form with the Dirichlet energy of $q / w$. This energy vanishes only for constant functions on the connected manifold, which were excluded above. Choose an A-orthonormal eigenbasis $q_{1}, q_{2}$ of this symmetric pair, ordered by $r_{1} \leq r_{2}$. For real $a_{i}$, not all zero,
$$\mathcal{R}_{h}\left(\frac{\sum_{i=1}^{j} a_{i} q_{i}}{w}\right)=\frac{\sum_{i=1}^{j} r_{i} a_{i}^{2}}{\sum_{i=1}^{j} a_{i}^{2}} \leq r_{j}, \quad j=1,2 .$$
The map $q \mapsto q / w$ is injective, and its image here has zero mean. These $j$-dimensional spaces are admissible in scalar min-max, which gives (5.16). This principle follows from the compact scalar resolvent by the same eigenbasis argument as (2.30). Finally, insert $q=r=w$ in (5.5). Its left-hand side is zero, so $K_{w}=(\kappa / 2) V_{w}$. \(\square\)

\section*{6. An exact scalar bound for the Chen-LeBrun-Weber metric}
6.1. The Einstein class. In this section the Einstein metric is represented as
$$g=s^{-2} k, \quad s=\operatorname{Scal}_{k}>0, \quad \operatorname{Ric}_{g}=\Lambda g .$$
We fix the scale of $k$ by (4.10). This fixes the homothety class representative $g=s^{-2} k$ and its constant $\Lambda$; no numerical value of $\Lambda$ is imposed. If $k$ is multiplied by $t>0$, then $s$ is multiplied by $t^{-1}$ and $s^{-2} k$ by $t^{3}$. Both $\lambda_{1}^{\mathrm{sc}}(g)$ and $\Lambda$ are then multiplied by $t^{-3}$. Their ratio is unchanged.

Let $D_{a}$ be (4.31). By (4.32), write
$$\begin{aligned}
s_{a}(t) & =b(a)+c(a) t, \quad t=x_{1}+x_{2}, \\
c(a) & =\frac{48\left(1-a^{3}\right)}{D_{a}}, \\
b(a) & =\frac{12\left(a^{5}+7 a^{4}+6 a^{3}+2 a^{2}-5 a-3\right)}{D_{a}} .
\end{aligned}$$
The identities $c=2 A$ and $b=2 B$ follow from $s_{k}=2 \ell$ in (5.2). Proposition 4.2 implies $s_{a}>0$ on $P_{a}$ for all $a>1$.

View $M$ as the blow-up of $\mathbb{C P}^{1} \times \mathbb{C P}^{1}$ at a torus-fixed point. Write $F_{1}, F_{2}, E \in H^{2}(M ; \mathbb{Z})$ for the two ruling classes and the exceptional class, respectively. Their intersections are
$$F_{1}^{2}=F_{2}^{2}=0, \quad F_{1} \cdot F_{2}=1, \quad F_{1} \cdot E=F_{2} \cdot E=0, \quad E^{2}=-1 .$$

In the angular-period convention of (5.1), the area of a toric divisor is $2 \pi$ times its lattice edge length. This follows by integrating $d x \wedge d \theta$ along the edge, with $0 \leq \theta<2 \pi$. The two uncut edges of $P_{a}$ have length $a$, and the exceptional edge has length $a-1$. Pairing with $F_{1}, F_{2}, E$ therefore gives
$$\frac{\left[\omega_{k}\right]}{2 \pi}=a\left(F_{1}+F_{2}\right)-(a-1) E, \quad x=a-1>0 .$$
Indeed, if $\left[\omega_{k}\right] /(2 \pi)=u F_{1}+v F_{2}-w E$, its three pairings are $v, u, w$, respectively; the edge areas give $u=v=a$ and $w=a-1$. Thus the class in (6.4) is $(1+x)\left(F_{1}+F_{2}\right)-x E$, the class used in [8, Section 3]. The constant $2 \pi$ has no effect on the Calabi energy in real dimension four: $\operatorname{Scal}_{t k}=t^{-1} \operatorname{Scal}_{k}$ and $d v_{t k}=t^{2} d v_{k}$. The CLW construction supplies an extremal metric in a critical class of this family; see [8, Proposition 7, Corollary 8 and Theorem 27]. Since $d x / d a=1$, its parameter is a critical point of the function $\mathcal{C}(a)$ defined below. The moments of $t$ are
$$\begin{array}{ll}
M_{0}=\frac{a^{2}+2 a-1}{2}, & M_{1}=\frac{a^{3}+3 a^{2}-1}{3}, \\
M_{2}=\frac{3 a^{4}+12 a^{3}+6 a^{2}-4 a-3}{12} . &
\end{array}$$
They follow from $M_{0}=I_{00}, M_{1}=2 I_{10}$ and $M_{2}=2 I_{20}+2 I_{11}$. Define the affine Calabi function by
$$\mathcal{C}(a)=\int_{P_{a}} s_{a}^{2} d x=b^{2} M_{0}+2 b c M_{1}+c^{2} M_{2}=\frac{24 N(a)}{D_{a}}$$
where
$$N(a)=3 a^{6}+14 a^{5}+17 a^{4}+12 a^{3}-5 a^{2}-6 a-3 .$$
For an extremal metric with this polygon, $4 \pi^{2} \mathcal{C}(a)$ is its Calabi energy. The numerator of its derivative satisfies
$$N^{\prime}(a) D_{a}-N(a) D_{a}^{\prime}=4 \mathfrak{p}(a), \quad \mathcal{C}^{\prime}(a)=\frac{96 \mathfrak{p}(a)}{D_{a}^{2}},$$
where
$$\begin{aligned}
\mathfrak{p}(a)= & a^{10}+5 a^{9}+6 a^{8}-12 a^{7}-34 a^{6}-42 a^{5} \\
& +20 a^{3}+21 a^{2}-7 a-6 .
\end{aligned}$$
Thus the parameter of the CLW metric is a root of $\mathfrak{p}$ in $(1, \infty)$. Only this implication from the geometric construction is used.

Lemma 6.1. There is exactly one root $a_{*}$ of $\mathfrak{p}$ in $(1, \infty)$. It satisfies
$$\frac{231}{118}<a_{*}<2 .$$
Proof. For $z=a-1$, the binomial formula gives
$$\begin{aligned}
\mathfrak{p}(1+z)= & z^{10}+15 z^{9}+96 z^{8}+336 z^{7}+680 z^{6}+720 z^{5} \\
& +120 z^{4}-624 z^{3}-708 z^{2}-300 z-48 .
\end{aligned}$$
For $z>0$, divide by $z^{3}$ and put $H(z)=z^{-3} \mathfrak{p}(1+z)$. Then
$$\begin{aligned}
H^{\prime}(z)= & 7 z^{6}+90 z^{5}+480 z^{4}+1344 z^{3}+2040 z^{2}+1440 z+120 \\
& +708 z^{-2}+600 z^{-3}+144 z^{-4}>0
\end{aligned}$$
Moreover $\lim _{z \downarrow 0} H(z)=-\infty$ and $\lim _{z \rightarrow \infty} H(z)=+\infty$. Continuity and strict monotonicity give exactly one positive zero. At that zero, $(\mathfrak{p}(1+z))^{\prime}=z^{3} H^{\prime}(z)>0$, so the zero is simple. For the rational lower bound, evaluation gives
$$\mathfrak{p}(231 / 118)=-\frac{262235040278610439893}{118^{10}}<0, \quad \mathfrak{p}(2)=288>0 .$$
The first numerator is also obtained without rational division: write $\mathfrak{p}(a)=\sum_{j=0}^{10} p_{j} a^{j}$, set $r_{10}=1$, and put
$$r_{j}=231 r_{j+1}+p_{j} 118^{10-j} \quad(j=9, \ldots, 0) .$$