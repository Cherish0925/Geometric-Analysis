---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: The Yamabe invariants of orbifolds and cylindrical manifolds, and 𝐿^2-harmonic spinors]

Proof of Theorem 4.1. For $\ell \geq 1$, let $h \in \mathcal{R i e m}^{*}\left(Z_{\ell}\right)$ be a metric which is homotopic to $h_{\Gamma_{\ell}}$ in $\mathcal{R}_{i e m}{ }^{*}\left(Z_{\ell}\right)$. By Fact 4.1.(2), it is easy to construct a cylindrical metric $\bar{g}$ on $X$ satisfying $R_{\bar{g}}>0$ on $X_{\ell}(1)=X_{\ell} \backslash\left(Z_{\ell} \times(1, \infty)\right)$, $\bar{g}=h+d t^{2}$ on $Z_{\ell} \times[2, \infty)$ and $[\bar{g}]=\left[h+d t^{2}\right]$ on $Z_{\ell} \times[1, \infty)$. Then, from [3] Proposition 4.6, Theorem 4.7], we also obtain that
$$Y_{[\bar{g}]}^{c y \ell}\left(X_{\ell}\right) \geq \min \left\{Y_{1}, Y_{2}\right\}>0,$$
and hence $Y^{h-c y \ell}\left(X_{\ell}\right)>0$. Here $Y_{1}=Y_{\left[\left.\bar{g}\right|_{X_{\ell}(1)}\right]}\left(X_{\ell}(1), \partial X_{\ell}(1) ;\left[\left.\bar{g}\right|_{\partial X_{\ell}(1)}\right]\right)>0$ denotes the relative Yamabe constant of $\left(X_{\ell}(1), \partial X_{\ell}(1) ;\left[\left.\bar{g}\right|_{X_{\ell}(1)}\right]\right)$ (see [1]) and
$$\begin{aligned}
Y_{2} & =Y_{\left[\left.\bar{g}\right|_{Z_{\ell} \times[1, \infty)} ^{c y \ell}\right.}\left(Z_{\ell} \times[1, \infty), Z_{\ell} \times\{1\} ;\left[\left.\bar{g}\right|_{Z_{\ell} \times\{1\}}\right]\right) \\
& =Y_{\left[h+d t^{2}\right]}^{c y \ell}\left(Z_{\ell} \times[1, \infty), Z_{\ell} \times\{1\} ;\left[\left.\bar{g}\right|_{Z_{\ell} \times\{1\}}\right]\right)>0
\end{aligned}$$
denotes the relative cylindrical Yamabe constant of $\left(Z_{\ell} \times[1, \infty), Z_{\ell} \times\{1\} ;[h+\right.$ $d t^{2}$ ]) (see [3, Section 4.1]), respectively. ¿From Theorem 3.8, Corollary 3.9 and Fact 4.1.(3), in order to prove the assertion (1), it is enough to show that there exists a characteristic element $a \in H^{2}\left(X_{\ell} ; \mathbf{Z}\right) \cap \operatorname{Im}\left[H_{c}^{2}\left(X_{\ell} ; \mathbf{R}\right) \rightarrow H^{2}\left(X_{\ell} ; \mathbf{R}\right)\right]$ satisfying the assumption A1 for the cylindrical metric $\bar{g}_{0} \in \mathcal{R i e m}^{c y \ell}\left(X_{\ell}\right)$ in Fact 4.1. (2) and $a^{2}=\frac{(\ell+2)^{2}}{\ell}$.

Note that $X_{\ell}$ has a natural complex structure. Then let
$$a_{0} \in H^{2}\left(X_{\ell} ; \mathbf{Z}\right) \cap \operatorname{Im}\left[H_{c}^{2}\left(X_{\ell} ; \mathbf{R}\right) \rightarrow H^{2}\left(X_{\ell} ; \mathbf{R}\right)\right] \cong \mathbf{Z}$$
be the generator satisfying $c_{1}\left(X_{\ell}\right)=(\ell+2) a_{0}$, and set $a:=(\ell+2) a_{0}$. It is easy to see that $a \equiv w_{2}\left(X_{\ell}\right) \bmod 2$. Then, there exist the $L_{\bar{g}_{0}}^{2}$-harmonic 2-form $\zeta \in \mathcal{H}_{\bar{g}_{0}}^{2}\left(X_{\ell}\right)=\mathcal{H}_{\bar{g}_{0}}^{2,+}\left(X_{\ell}\right)$ and a sequence of closed 2-forms $\left\{\zeta_{j}\right\} \subset \Omega_{\mathrm{c}}^{2}\left(X_{\ell}\right)$ such that
$$\left\{\begin{array}{l}
{\left[\zeta_{j}\right]=[\zeta]=a \in H^{2}\left(X_{\ell} ; \mathbf{Z}\right)} \\
\zeta_{j} \rightarrow \zeta \text { in } L_{\bar{g}_{0}}^{k, 2} \text {-topology for any } k \geq 1
\end{array}\right.$$

Now we consider the determinant $\mathbf{C}$-line bundle $\operatorname{det}(a)$ and the associated plus/minus spin bundle $\mathrm{S}_{\mathrm{C}}^{ \pm}(a)=\mathrm{S}_{\mathrm{C}}^{ \pm} \otimes \operatorname{det}(a)^{1 / 2}$. Then we may assume that, as Hermitian vector bundles,
$$\left.\operatorname{det}(a)\right|_{Z_{\ell} \times[1, \infty)}=P_{Z_{\ell}}^{*}\left(\left.\operatorname{det}(a)\right|_{Z_{\ell} \times\{1\}}\right),\left.\quad \mathrm{S}_{\mathbf{C}}^{ \pm}(a)\right|_{Z_{\ell} \times[1, \infty)}=P_{Z_{\ell}}^{*}\left(\left.\mathrm{~S}_{\mathbf{C}}^{ \pm}(a)\right|_{Z_{\ell} \times\{1\}}\right),$$
where $P_{Z_{\ell}}: Z_{\ell} \times[1, \infty) \rightarrow Z_{\ell} \times\{1\}$ denotes the canonical projection. Moreover, there exist $U(1)$-connections $A_{j} \in \mathcal{A}(\operatorname{det}(a))$ with compact support such that $\frac{\sqrt{-1}}{2 \pi} F_{A_{j}}=\frac{\sqrt{-1}}{2 \pi} d A_{j}=\zeta_{j}$. Now we denote by
$$\not \supset_{A_{j}}:=\not \varnothing_{A_{j}, \bar{g}_{0}}^{+}: \Gamma\left(\mathrm{S}_{\mathbf{C}}^{+}(a)\right) \longrightarrow \Gamma\left(\mathrm{S}_{\mathbf{C}}^{-}(a)\right)$$
the corresponding twisted Dirac operator. Recall that $\partial_{\infty} \bar{g}_{0}=h_{\Gamma_{\ell}} \in \mathcal{R} i e m\left(Z_{\ell}\right)$, and hence $\lambda\left(\mathcal{L}_{h_{\Gamma_{\ell}}}\right)>0$. Then the Hirzebruch signature formula (cf. 25, Example 4.1.9]) combined with $\lambda\left(\mathcal{L}_{h_{\Gamma_{\ell}}}\right)>0$ gives
$$\begin{aligned}
L^{2} \text {-ind } \not \not ⺄_{A_{j}} & =\operatorname{dim}_{\mathbf{C}}\left(L^{2}-\operatorname{Ker} \not \partial_{A_{j}, \bar{g}_{0}}^{+}\right)-\operatorname{dim}_{\mathbf{C}}\left(L_{\mathrm{ext}}^{2}-\operatorname{Ker} \not \nearrow_{A_{j}, \bar{g}_{0}}^{-}\right) \\
& =\frac{1}{8} \int_{X_{\ell}} c_{1}\left(A_{j}\right) \wedge c_{1}\left(A_{j}\right)-\frac{1}{8} \int_{X_{\ell}} \frac{1}{3} p_{1}\left(\nabla^{\bar{g}_{0}}\right)-\frac{1}{2} \eta\left(h_{\Gamma_{\ell}}\right) .
\end{aligned}$$
Here $\eta\left(h_{\Gamma_{\ell}}\right)$ stands for the eta invariant of the Dirac operator
$$\left(\frac{\partial}{\partial t}\right) \cdot \not \varnothing_{\left(Z_{\ell}, h_{\Gamma_{\ell}}\right)}: \Gamma\left(\left.\mathrm{S}_{\mathbf{C}}^{+}\right|_{Z_{\ell} \times\{1\}}\right) \longrightarrow \Gamma\left(\left.\mathrm{S}_{\mathbf{C}}^{+}\right|_{Z_{\ell} \times\{1\}}\right)$$
and $\not \partial_{\left(Z_{\ell}, h_{\Gamma_{\ell}}\right)}$ the spin Dirac operator on ( $Z_{\ell} \cong Z_{\ell} \times\{1\}, h_{\Gamma_{\ell}}$ ), respectively.
Claim $4.2 L^{2}$-ind $\nsucc_{A_{j}}=1$.
Proof. Indeed, we have
$$\left\{\begin{array}{l}
\int_{X_{\ell}} c_{1}\left(A_{j}\right) \wedge c_{1}\left(A_{j}\right)=\frac{(\ell+2)^{2}}{\ell} \text { and } \\
\int_{X_{\ell}} \frac{1}{3} p_{1}\left(\nabla^{\bar{g}_{0}}\right)=\tau\left(X_{\ell}\right)+\eta_{\operatorname{sign}}\left(h_{\Gamma_{\ell}}\right)=1+\eta_{\operatorname{sign}}\left(h_{\Gamma_{\ell}}\right),
\end{array}\right.$$
where $\eta_{\operatorname{sign}}\left(h_{\Gamma_{\ell}}\right)$ is the signature defect (see [5] or [25, (4.1.34)]). Note that $4 \cdot \eta\left(h_{\Gamma_{\ell}}\right)+\eta_{\operatorname{sign}}\left(h_{\Gamma_{\ell}}\right)=-\frac{4(\ell-1)}{\ell}+\ell-1$ (see [24] or [25] Example 4.1.27]). Then we have
$$\begin{aligned}
L^{2} \text {-ind } \not Ə_{A_{j}} & =\frac{1}{8}\left[\frac{(\ell+2)^{2}}{\ell}-1-\left(4 \cdot \eta\left(h_{\Gamma_{\ell}}\right)+\eta_{\operatorname{sign}}\left(h_{\Gamma_{\ell}}\right)\right)\right] \\
& =\frac{1}{8 \ell}\left(\ell^{2}+4 \ell+4-4 \ell+4-\ell^{2}\right)=1 .
\end{aligned}$$ \(\square\)
We also note that $a^{2}=\int_{X_{\ell}} \zeta \wedge \zeta=\frac{(\ell+2)^{2}}{\ell}$ by the choice of $a$. This completes the proof of the assertion (1).

By the Remark after [3, Proposition 6.5],
$$Y_{\left[h_{\Gamma_{\ell}}^{c y \ell}+d t^{2}\right]}^{c y \ell}\left(Z_{\ell} \times \mathbf{R}\right)=\frac{Y\left(S^{4}\right)}{\left|\Gamma_{\ell}\right|^{1 / 2}}=8 \sqrt{\frac{6}{\ell}} \pi .$$
¿From the continuity of Yamabe constants [4] Proposition 3.4], Remark 4.1-(4), and that $Y_{\left[h_{S}+d t^{2}\right]}^{c y \ell}\left(S^{3} \times \mathbf{R}\right)=Y\left(S^{4}\right)=8 \sqrt{6} \pi>12 \sqrt{2} \pi$, we obtain that
$$Y^{h-c y \ell}\left(X_{\ell}\right) \leq \begin{cases}12 \sqrt{2} \pi=Y\left(\mathbf{C P}^{2}\right) & \text { if } \quad \ell=1, \\ Y_{\left[h+d t^{2}\right]}^{c y \ell}\left(Z_{\ell} \times \mathbf{R}\right) & \text { if } \quad \ell \geq 2\end{cases}$$
for any metric $h \in \mathcal{R}$ iem $\left(Z_{\ell}\right)$ which is sufficiently $C^{2}$-close to $h_{\Gamma_{\ell}}$. This completes the proof of the assertion (2). \(\square\)

Corollary 4.3 (cf. [14, Theorem B]) Set $X_{\ell, k, m}=X_{\ell} \# k \mathbf{C P}^{2} \# m\left(S^{1} \times S^{3}\right)$. For any integers $\ell \geq 1$ and $k, m \geq 0$,
$$0<Y^{h-c y \ell}\left(X_{\ell, k, m}\right) \leq \min \left\{4 \pi \sqrt{2\left(k+\frac{(\ell+2)^{2}}{\ell}\right)}, Y_{\left[h+d t^{2}\right]}^{c y \ell}\left(Z_{\ell} \times \mathbf{R}\right)\right\}$$
for any metric $h \in \mathcal{R i e m}^{*}\left(Z_{\ell}\right)$ homotopic to $h_{\Gamma_{\ell}}$ in $\operatorname{Riem}^{*}\left(Z_{\ell}\right)$.
Remark 4.2 We note that $4 \pi \sqrt{2\left(k+\frac{(\ell+2)^{2}}{\ell}\right)}<Y\left(S^{4}\right)=8 \sqrt{6} \pi \quad$ if $k<$ $12-\frac{(\ell+2)^{2}}{\ell} \leq 4$.

Proof of Corollary 4.3. There exists a metric $\tilde{g} \in \mathcal{R i e m}^{c y \ell}\left(X_{\ell, k, m}\right)$ such that $R_{\tilde{g}}>0$ and $\partial_{\infty} \tilde{g}=h_{\Gamma_{\ell}}$. Then, similarly to the case of $X_{\ell}$, we obtain that $Y^{h \text {-cyl }}\left(X_{\ell, k, m}\right)>0$ for any metric $h \in \mathcal{R i e m}^{*}\left(Z_{\ell}\right)$ homotopic to $h_{\Gamma_{\ell}}$ in $\mathcal{R} \mathrm{iem}^{*}\left(Z_{\ell}\right)$. Note that
$$\begin{aligned}
& \mathcal{H}_{\tilde{g}}^{2,+}\left(X_{\ell, k, m}\right) \cap H^{2}\left(X_{\ell, k, m} ; \mathbf{Z}\right)=\mathcal{H}_{\tilde{g}}^{2}\left(X_{\ell, k, m}\right) \cap H^{2}\left(X_{\ell, k, m} ; \mathbf{Z}\right) \\
& \quad \cong\left(\mathcal{H}_{\tilde{g}}^{2}\left(X_{\ell}\right) \cap H^{2}\left(X_{\ell} ; \mathbf{Z}\right)\right) \oplus H^{2}\left(\mathbf{C P}^{2} ; \mathbf{Z}\right)^{\oplus k} \cong \mathbf{Z} \oplus \mathbf{Z}^{\oplus k} .
\end{aligned}$$
Then we choose $\tilde{a}=(a, 1, \cdots, 1) \in \mathbf{Z} \oplus \mathbf{Z}^{\oplus k}$. Similarly to the case of $X_{\ell}$, we also obtain that $L^{2}$-ind $\not \partial_{\tilde{A}}=1$, where $\not \partial_{\tilde{A}}$ denotes the corresponding Dirac operator on $\mathrm{S}_{\mathrm{C}}^{+}(\tilde{a})$ (see the argument given in [14]). Note that $2 \tilde{a}^{2}=$ $2\left(k+\frac{(\ell+2)^{2}}{\ell}\right)$, and hence Theorem 3.8 implies the estimate (4.1). \(\square\)
4.2. Example 2. Let consider the open 4-manifold $S^{2} \times \mathbf{R}^{2}$ with tame end $\left(S^{2} \times S^{1}\right) \times[0, \infty)$ and the connected sum $X=\mathbf{C P}^{2} \sharp\left(S^{2} \times \mathbf{R}^{2}\right)$. We first note that
$$H^{2}(X ; \mathbf{Z}) \cap \operatorname{Im}\left[H_{c}^{2}(X ; \mathbf{R}) \rightarrow H^{2}(X ; \mathbf{R})\right] \cong H^{2}\left(\mathbf{C} \mathbf{P}^{2} ; \mathbf{Z}\right) \cong \mathbf{Z} .$$
Let $h_{0}=h_{S}+d \tau^{2}$ denote a product metric on $S^{2} \times S^{1}$, where $h_{S}$ denotes the standard metric on $S^{2}$ of constant curvature one. Similarly to Theorem 4.1 we also obtain the following.

Proposition 4.4 With the above understood,
$$0<Y^{h-c y \ell}(X) \leq \min \left\{12 \sqrt{2} \pi, Y_{\left[h+d t^{2}\right]}^{c y \ell}\left(\left(S^{2} \times S^{1}\right) \times \mathbf{R}\right)\right\}$$
for any metric $h \in \mathcal{R i e m}^{*}\left(S^{2} \times S^{1}\right)$ homotopic to $h_{0}$ in $\operatorname{Riem}^{*}\left(S^{2} \times S^{1}\right)$.
Remark 4.3 It is not clear for us whether a metric $h \in \mathcal{R i e m}^{*}\left(S^{2} \times S^{1}\right)$ homotopic to $h_{0}$ in $\mathcal{R i e m}^{*}\left(S^{2} \times S^{1}\right)$ satisfies the inequality
$$Y_{\left[h+d t^{2}\right]}^{c y \ell}\left(\left(S^{2} \times S^{1}\right) \times \mathbf{R}\right)>12 \sqrt{2} \pi\left(=Y\left(\mathbf{C} \mathbf{P}^{2}\right)\right) .$$
Let $h_{r}=h_{S}+d \tau^{2}$ denote the standard product metric on $S^{2} \times S^{1}(r)$, where $S^{1}(r)$ stands for the circle of radius $r>0$. Then we note that (cf. [27])
$$0<Y_{\left[h_{S}+g_{0}\right]}\left(S^{2} \times \mathbf{R}^{2}\right)=\lim _{r \nearrow \infty} Y_{\left[h_{r}+d t^{2}\right]}^{c y \ell}\left(S^{2} \times S^{1} \times \mathbf{R}\right),$$
where $g_{0}$ denotes the Euclidean metric on $\mathbf{R}^{2}$ and
$$Y_{\left[h_{S}+g_{0}\right]}\left(S^{2} \times \mathbf{R}^{2}\right):=\inf _{u \in C_{c}^{\infty}\left(S^{2} \times \mathbf{R}^{2}\right)} Q_{h_{S}+g_{0}}(u)$$
(cf. [30]). If $Y_{\left[h_{S}+g_{0}\right]}\left(S^{2} \times \mathbf{R}^{2}\right)>12 \sqrt{2} \pi$, then the estimate $Y^{h_{r}-c y \ell}(X) \leq$ $12 \sqrt{2} \pi$ (coming from Theorem 3.8) is effective for sufficiently large $r>0$.

\section*{References}
\begin{itemize}
\item[] [1] K. Akutagawa, B. Botvinnik, The relative Yamabe invariant, Comm. Anal. Geom. 10 (2002), 925-954.
\item[] [2] K. Akutagawa, B. Botvinnik, Manifolds of positive scalar curvature and conformal cobordism theory, Math. Ann. 324 (2002), 817-840.
\item[] [3] K. Akutagawa, B. Botvinnik, Yamabe metrics on cylindrical manifolds, to appear in Geom. Funct. Anal.
\item[] [4] K. Akutagawa, B. Botvinnik, O. Kobayashi, H. Seshadri, The Weyl functional near the Yamabe invariant, J. Geom. Anal. 13 (2003), 1-20.
\item[] [5] M. Atiyah, V. Patodi, I. Singer, Spectral asymmetry and Riemannian geometry. I, Math. Proc. Cambridge Philos. Soc. 77 (1975), 43-69.
\item[] [6] T. Aubin, Some nonlinear problems in Riemannian geometry, Springer Monographs in Math., Springer-Verlag, 1998.
\item[] [7] A. Besse, Einstein manifolds, Springer-Verlag, 1987.
\item[] [8] B. Booss-Bavnbek, K. Wojciechowski, Elliptic boundary problems for Dirac operators, Birkhäuser, 1993.
\item[] [9] J. Dodziuk, Sobolev spaces of differential forms and de Rham-Hodge isomorphism, J. Diff. Geom. 16 (1981), 63-73.
\end{itemize}
\begin{itemize}
\item[] [10] J. Dodziuk, $L^{2}$-harmonic forms on complete manifolds, Seminar on Differential Geometry (ed. by S.-T. Yau), Ann. of Math. Stud. 102, 291-300, Princeton Univ. Press, 1982.
\item[] [11] J. J. Duistermaat, The heat kernel Lefschetz fixed point formula for the spin-c Dirac operator, Progress in Nonlinear Differential Equations and Their Applications 18, Birkhäuser, 1996.
\item[] [12] J. Escobar, Uniqueness theorems on conformal deformation of metrics, Sobolev inequalities, and an eigenvalue estimate, Comm. Pure Appl. Math. 43 (1990), 857-883.
\item[] [13] M. Gursky, Four-manifolds with $\delta W^{+}=0$ and Einstein constants of the sphere, Math. Ann. 318 (2000), 417-431.
\item[] [14] M. Gursky, C. LeBrun, Yamabe invariants and spin ${ }^{c}$ structures, Geom. Funct. Anal. 8 (1998), 965-977.
\item[] [15] O. Hijazi, A conformal lower bound for the smallest eigenvalue of the Dirac operator and Killing spinors, Comm. Math. Phys. 104 (1986), 151-162.
\item[] [16] N. Hitchin, Harmonic spinors, Adv. in Math. 14 (1974), 1-55.
\item[] [17] M. Kapovich, Hyperbolic manifolds and discrete groups, Progress in Math. 183, Birkhäuser, 2001.
\item[] [18] J. Kazdan, F. Warner, Scalar curvature and conformal deformation of Riemannian structure, J. Diff. Geom. 10 (1975), 113-134.
\item[] [19] T. Kawasaki, The index of elliptic operators over $V$-manifolds, Nagoya Math. J. 84 (1981), 135-157.
\item[] [20] O. Kobayashi, Scalar curvature of a metric with unit volume, Math. Ann. 279 (1987), 253-265.
\item[] [21] R. Kobayashi, Einstein-Kähler $V$-metrics on open Satake $V$-surfaces with isolated quotient singularities, Math. Ann. 272 (1985), 385-398.
\item[] [22] C. LeBrun, Yamabe constants and the perturbed Seiberg-Witten equations, Comm. Anal. Geom. 5 (1997), 535-553.
\item[] [23] J. Lott, Eigenvalue bounds for the Dirac operator, Pacific J. Math. 125 (1986), 117-126.
\item[] [24] L. Nicolaescu, Seiberg-Witten invariants of lens spaces, Canad. J. Math. 53 (2001), 780-808.
\item[] [25] L. Nicolaescu, Notes on Seiberg-Witten theory, Graduate Studies in Math. 28, Amer. Math. Soc., Providence, RI, 2000.
\item[] [26] M. Obata, Certain conditions for a Riemannian manifold to be isometric with a sphere, J. Math. Soc. Japan 14 (1962), 333-340.
\item[] [27] J. Petean, Best Sobolev constants and manifolds with positive scalar curvature metrics, Ann. Global Anal. Geom. 20 (2001), 231-242.
\item[] [28] I. Satake, The Gauss-Bonnet theorem for $V$-manifolds, J. Math. Soc. Japan 9 (1957), 464-492.
\item[] [29] R. Schoen, Variational theory for the totatl scalar curvature functional for Riemannian metrics and related topics, Topics in calculus of variations (Montecatini Terme, 1987), 120-154, Lecture Notes in Math. 1365, Springer-Verlag, 1989.
\end{itemize}
\begin{itemize}
\item[] [30] R. Schoen, S.-T. Yau, Conformally flat manifolds, Kleinian groups and scalar curvature, Invent. Math. 92 (1988), 47-71.
\end{itemize}

Kazuo Akutagawa, Shizuoka University, Shizuoka, Japan
e-mail: smkacta@ipc.shizuoka.ac.jp
Boris Botvinnik, University of Oregon, Eugene, USA
e-mail: botvinn@math.uoregon.edu