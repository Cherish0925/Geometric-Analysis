---
retention_scope: session
part: 5
total_parts: 5
---

[Part 5/5 of: A continuous cusp closing process for negative Kähler- ...]

To prove that the numerator of $\lambda_{\sigma, s}$ changes sign, we bound $\left\langle s, \hat{v}_{\sigma}\right\rangle_{L^{2}},\left\langle f_{\sigma}, \hat{v}_{\sigma}\right\rangle_{L^{2}}$ and $\left\langle Q_{\sigma} \tilde{u}_{\sigma, s}, \hat{v}_{\sigma}\right\rangle_{L^{2}}$ separately. This is done in the following three steps.
(1) From Lemmas 2.31 and 4.8,
$$\left|\left\langle 1, \hat{v}_{\sigma}\right\rangle_{L^{2}}\right| \geqslant C^{-1}|T|^{-2} \geqslant C^{-1}|b|^{\frac{2}{3}},$$
i.e., we have a lower bound matching the upper bound (5.39) up to a constant. This is the good term that will enforce a sign change. Here we crucially use the fact that $\hat{v}$ has a sign, so that it suffices to integrate over a small neighborhood of the left endpoint $s=0$, and that $\hat{v}(0)=C_{0} \neq 0$.
(2) We have already proved in (5.13)-(5.14) that
$$\left|\left\langle f_{\sigma}, \hat{v}_{\sigma}\right\rangle_{L^{2}}\right| \leqslant C|b|^{\frac{3}{2}-\frac{5}{6} \alpha} .$$
(3) Lastly, we claim that
$$\left|\left\langle Q_{\sigma} \tilde{u}_{\sigma, s}, \hat{v}_{\sigma}\right\rangle_{L^{2}}\right| \leqslant C|b|^{\frac{5}{3}(1-\mathbf{a})-\frac{2}{3} \delta} .$$
To prove this, we first make a pointwise estimate using (5.36):
$$\begin{aligned}
\left|\nabla_{\omega_{g l u e, \sigma}}^{2} \tilde{u}_{\sigma, s}\right|_{\omega_{g l u e, \sigma}} & \leqslant\left\|\tilde{u}_{\sigma, s}\right\|_{C_{w}^{2, \bar{\alpha}}} \cdot \mathbf{r}_{\sigma}^{-2} w_{\sigma} \\
& \leqslant C|b|^{\frac{5}{6}(1-\mathbf{a})-\frac{\delta}{3}} \cdot \begin{cases}|T|^{-\delta} & \text { on } \Re_{1}, \\
|b|^{-\frac{1}{2}} \Psi_{\sigma}^{*}\left(\Phi_{\sigma}^{-1}\right)^{*}\left((t-T)^{-\frac{3}{2}-\delta}\right) & \text { on } \Re_{2} \cup \cdots \cup \Re_{6}, \\
|b|^{-\frac{1}{2}} & \text { on } \Re_{7} .\end{cases}
\end{aligned}$$

Thus, using again Lemmas 2.31 and 4.8,
$$\begin{aligned}
\left|\left\langle Q_{\sigma} \tilde{u}_{\sigma, s}, \hat{v}_{\sigma}\right\rangle_{L^{2}}\right| & \leqslant C|b|^{\frac{5}{3}(1-\mathbf{a})-\frac{2}{3} \delta} \cdot\left(|b| \cdot|b|^{-1}+|b| \cdot \int_{1}^{2|T|^{\alpha}}|b|^{-1} y^{-3-2 \delta} d y\right. \\
& \left.+|T|^{-2} \int_{2|T|^{\alpha-1}}^{1-\frac{\tau}{T}}|b|^{-1}(|T| s)^{-3-2 \delta} d s\right) .
\end{aligned}$$
All terms in the big parenthesis are uniformly bounded as $\sigma \rightarrow 0$, which proves (5.43).
Finally, let us prove the theorem using these estimates. Choosing $\alpha<\mathbf{a}$ we get
$$\frac{5}{6}(1-\mathbf{a})+\frac{2}{3}<\frac{3}{2}-\frac{5}{6} \alpha .$$
Thus, from (5.41) and (5.42) we have that
$$\left|\left\langle A, \hat{v}_{\sigma}\right\rangle_{L^{2}}\right| \gg\left|\left\langle f_{\sigma}, \hat{v}_{\sigma}\right\rangle_{L^{2}}\right| .$$
Similarly, if $\mathbf{a}<\frac{1}{5}$ and $\delta \ll 1$, then
$$\frac{5}{6}(1-\mathbf{a})+\frac{2}{3}<\frac{5}{3}(1-\mathbf{a})-\frac{2}{3} \delta,$$
so from (5.41) and (5.43),
$$\left|\left\langle A, \hat{v}_{\sigma}\right\rangle_{L^{2}}\right| \gg\left|\left\langle Q_{\sigma} \tilde{u}_{\sigma, s}, \hat{v}_{\sigma}\right\rangle_{L^{2}}\right| .$$
It is now clear from (5.40) that $\lambda_{\sigma, s}$ changes sign at the boundary of the interval $s \in[-A, A]$. \(\square\)

We now deduce the statements of the Main Theorem.
We begin by applying Theorem 5.4 with $\alpha<\mathbf{a}$ both very small and with $\bar{\alpha} \in(0,1)$ arbitrary. This yields that for all $0<|\sigma| \ll 1$ there exists an $s_{\sigma} \in[-A, A]$ such that $\lambda_{\sigma, s_{\sigma}}=0$, so $\tilde{u}_{\sigma, s_{\sigma}}$ coincides with the (unique) solution $u_{\sigma}$ to our Monge-Ampère equation. Thus, $u_{\sigma}$ satisfies estimate (5.36), i.e.,
$$\left\|u_{\sigma}\right\|_{C_{w}^{2, \bar{\alpha}}}=O_{\varepsilon}\left(|b|^{\frac{5}{6}-\varepsilon}\right)$$
for any $\varepsilon>0$. The first part of the Main Theorem concerns the behavior of $\omega_{K E, \sigma}=\omega_{\text {glue }, \sigma}+i \partial \bar{\partial} u_{\sigma}$ on the Tian-Yau cap, region $\Re_{7}$. The definition of $\Re_{7}$ depends on a parameter $R$ via the definition of $\Phi_{\sigma}$, (2.17). Up to replacing the $R$ of the Main Theorem by $R / C$ and assuming that this is $>C$ for some universal constant $C \gg 1$, the $R$ of the Main Theorem can be identified with the $R$ of (2.17). Fixing $R$, the weight function $w_{\sigma}$ equals 1 and the regularity scale $\mathbf{r}_{\sigma}$ equals $|b|^{1 / 4}$ on $\Re_{7}$. So it follows from (5.50) and from the definition of the weighted norm, (3.112), that
$$\sup _{\Re_{7}}\left|i \partial \bar{\partial} u_{\sigma}\right|_{\omega_{g l u e, \sigma}}=O\left(|b|^{-\frac{1}{2}}\right) \cdot O_{\varepsilon}\left(|b|^{\frac{5}{6}-\varepsilon}\right)=O_{\varepsilon}\left(|\log | \sigma| |^{-1+\varepsilon}\right) .$$
The left-hand side of (5.51) is invariant under diffeomorphisms and rescalings applied simultaneously to $\omega_{K E, \sigma}$ and $\omega_{\text {glue }, \sigma}$. This implies the first statement of the Main Theorem.

Remark 5.5. Given (5.51) and the estimate $\sup _{\Re_{7}}\left|u_{\sigma}\right|=O_{\varepsilon}\left(|b|^{(5 / 6)-\varepsilon}\right)$ that also follows from (5.50), the standard theory of the Monge-Ampère equation tells us that in fact, the $C^{1, \beta}\left(\Re_{7}, \omega_{\text {glue }, \sigma}\right)$ norm of $\omega_{K E, \sigma}-\omega_{\text {glue }, \sigma}$ goes to zero for $\beta<\frac{1}{3}$. Clearly, the optimal result would be to have this for all $\beta<1$ because $\omega_{\text {glue }, \sigma}$ is Ricci-flat on $\Re_{7}$ whereas $\omega_{K E, \sigma}$ has Ricci $=-1$. This suggests that the best possible exponent in (5.50) is 1 rather than $\frac{5}{6}$ (and $-\frac{3}{2}$ rather than -1 in (5.51) and in the Main Theorem).

Remark 5.6. Note the following subtlety related to the asymptotic expansion of $\omega_{K E, 0}$ in (2.54). As explained in Remark 2.15, we need to replace $\Psi_{\sigma}$ by scale $_{\lambda^{-1}} \circ \Psi_{\sigma}$ to be able to carry out our gluing construction, where $\lambda=e^{\mathfrak{s}}$ for the constant $\mathfrak{s}$ from (2.54), which is uniquely determined by the global geometry of $\left(\mathcal{X}_{0}^{\text {reg }}, \omega_{K E, 0}\right)$ but is not known explicitly. We have assumed that $\mathfrak{s}=0$ for simplicity, but
if $\mathfrak{s} \neq 0$ then $\mathfrak{s}$ or $\lambda$ could in principle appear in the statement of the Main Theorem. However, in the Main Theorem we consider the pullback $\left(m_{\sigma} \circ \Psi_{\sigma}\right)^{-*}\left(\omega_{K E, \sigma}\right)$, and $\omega_{K E, \sigma}$ is approximated by
$$\left(\operatorname{scale}_{\lambda^{-1}} \circ \Psi_{\sigma}\right)^{*}\left[\sqrt{2|b|}\left(m_{\sigma \lambda^{-3}}\right)^{*}\left(\omega_{T Y_{1}}\right)\right]$$
in the bubbling region. One easily checks that the unknown constant $\lambda$ cancels out.
As for the rest of the Main Theorem, the Euler numbers of $\mathcal{X}_{0}^{\text {reg }}$ and of $\mathcal{X}_{\sigma}(0<|\sigma| \ll 1)$ obviously differ by the Euler number of the Tian-Yau space. The Euler number of a smooth sextic in $\mathbb{C P}^{3}$ is 108 by a standard computation. As a smoothing of an isolated cubic cone singularity, the Tian-Yau space is homotopy equivalent to $\bigvee_{i=1}^{8} S^{2}$ and so has Euler number 9 [27, Thm 1]. The $L^{2}$-curvature identity follows from this by using the Chern-Gauß-Bonnet theorem for Einstein 4 -manifolds and the standard fact that the Chern-Gauß-Bonnet formula holds without boundary terms both on $\left(T Y_{1}, \omega_{T Y_{1}}\right)$ and on $\left(\mathcal{X}_{0}^{\text {reg }}, \omega_{K E, 0}\right)$. Because there is no loss of $L^{2}$-curvature, there cannot be any other bubbles.

\section*{References}
\begin{itemize}
\item[] [1] M. Anderson, Dehn filling and Einstein metrics in higher dimensions, J. Differ. Geom. 73 (2006), 219-261.
\item[] [2] T. Aubin, Équations du type Monge-Ampère sur les variétés kählériennes compactes, Bull. Sci. Math. 102 (1978), 63-95.
\item[] [3] R. Bamler, Construction of Einstein metrics by generalized Dehn filling, J. Eur. Math. Soc. 14 (2012), 887-909.
\item[] [4] R. Berman, H. Guenancia, Kähler-Einstein metrics on stable varieties and log canonical pairs, Geom. Funct. Anal. 24 (2014), 1683-1730.
\item[] [5] O. Biquard, H. Guenancia, Degenerating Kähler-Einstein cones, locally symmetric cusps, and the Tian-Yau metric, Invent. Math. 230 (2022), 1101-1163.
\item[] [6] O. Biquard, Y. Rollin, Smoothing singular constant scalar curvature Kähler surfaces and minimal Lagrangians, Adv. Math. 285 (2015), 980-1024.
\item[] [7] S.-Y. Cheng, S.-T. Yau, Differential equations on Riemannian manifolds and their geometric applications, Comm. Pure Appl. Math. 28 (1975), 333-354.
\item[] [8] S.-Y. Cheng, S.-T. Yau, Inequality between Chern numbers of singular Kähler surfaces and characterization of orbit space of discrete group of $S U(2,1)$, Complex differential geometry and nonlinear differential equations (Brunswick, ME, 1984), 31-44, Contemp. Math., 49, Amer. Math. Soc., Providence, RI, 1986.
\item[] [9] R. Conlon, H.-J. Hein, Asymptotically conical Calabi-Yau manifolds, I, Duke Math. J. 162 (2013), 2855-2902.
\item[] [10] V. Datar, X. Fu, J. Song, Kähler-Einstein metric near an isolated log canonical singularity, J. Reine Angew. Math. 797 (2023), 79-116.
\item[] [11] E. Di Nezza, V. Guedj, H. Guenancia, Families of singular Kähler-Einstein metrics, J. Eur. Math. Soc. 25 (2023), 2697-2762.
\item[] [12] S. Donaldson, S. Sun, Gromov-Hausdorff limits of Kähler manifolds and algebraic geometry, II, J. Differ. Geom. 107 (2017), 327-371.
\item[] [13] X. Fu, H.-J. Hein, X. Jiang, Asymptotics of Kähler-Einstein metrics on complex hyperbolic cusps, Calc. Var. PDE 63 (2024), Paper No. 6.
\item[] [14] M. Giaquinta, L. Martinazzi, An introduction to the regularity theory for elliptic systems, harmonic maps and minimal graphs, Edizioni della Normale, Pisa, 2005.
\item[] [15] U. Hamenstädt, F. Jäckel, Stability of Einstein metrics and effective hyperbolization in large Hempel distance, preprint (2022), arXiv:2206.10438.
\item[] [16] H.-J. Hein, Gravitational instantons from rational elliptic surfaces, J. Amer. Math. Soc. 25 (2012), 355-393.
\item[] [17] H.-J. Hein, S. Sun, Calabi-Yau manifolds with isolated conical singularities, Publ. Math. IHÉS 126 (2017), 73-130.
\item[] [18] H.-J. Hein, S. Sun, J. Viaclovsky, R. Zhang, Nilpotent structures and collapsing Ricci-flat metrics on the K3 surface, J. Amer. Math. Soc. 35 (2022), 123-209.
\item[] [19] H.-J. Hein, S. Sun, J. Viaclovsky, R. Zhang, Asymptotically Calabi metrics and weak Fano manifolds, preprint (2021), arXiv:2111.09287, to appear in Geom. Topol.
\item[] [20] H.-J. Hein, V. Tosatti, Higher-order estimates for collapsing Calabi-Yau metrics, Camb. J. Math. 8 (2020), 683-773.
\item[] [21] C. Hummel, V. Schroeder, Cusp closing in rank one symmetric spaces, Invent. Math. 123 (1996), 283-307.
\item[] [22] A. Kas, M. Schlessinger, On the versal deformation of a complex space with an isolated singularity, Math. Ann. 196 (1972), 23-29.
\end{itemize}
[23] R. Kobayashi, Einstein-Kaehler metrics on open algebraic surfaces of general type, Tohoku Math. J. 37 (1985), 43-77.
[24] J. Kollár, N. Shepherd-Barron, Threefolds and deformations of surface singularities, Invent. Math. 91 (1988), 299-338.
[25] S. Kovács, Answer to MathOverflow Question 56019, https://mathoverflow.net/questions/56019/degenerations-of-smooth-projective-varieties, 2011.
[26] H. Mandel, Degenerations of negative Kähler-Einstein surfaces, J. Lond. Math. Soc. 109 (2024), Paper e12818.
[27] J. Milnor, P. Orlik, Isolated singularities defined by weighted homogeneous polynomials, Topology 9 (1970), 385-393.
[28] T. Ozuch, Noncollapsed degeneration of Einstein 4-manifolds, II, Geom. Topol. 26 (2022), 1529-1634.
[29] H. Pinkham, Deformations of algebraic varieties with $G_{m}$ action, Astérisque, vol. 20, Soc. Math. de France, Paris, 1974.
[30] J. Ruppenthal, A $\bar{\partial}$-theoretical proof of Hartogs' extension theorem on Stein spaces with isolated singularities, J. Geom. Anal. 18 (2008), 1127-1132.
[31] K. Saito, Einfach-elliptische Singularitäten, Invent. Math. 23 (1974), 289-325.
[32] O. Savin, Small perturbation solutions for elliptic equations, Comm. Part. Differ. Eq. 32 (2007), 557-578.
[33] J. Song, Degeneration of Kähler-Einstein manifolds of negative scalar curvature, preprint (2017), arXiv:1706.01518.
[34] J. Song, J. Sturm, X. Wang, Continuity of the Weil-Petersson potential, preprint (2020), arXiv:2008.11215.
[35] C. Spotti, Deformations of nodal Kähler-Einstein del Pezzo surfaces with discrete automorphism groups, J. Lond. Math. Soc. 89 (2014), 539-558.
[36] W. Thurston, Three-dimensional manifolds, Kleinian groups and hyperbolic geometry, Bull. Amer. Math. Soc. (N.S.) 6 (1982), 357-381.
[37] G. Tian, S.-T. Yau, Existence of Kähler-Einstein metrics on complete Kähler manifolds and their applications to algebraic geometry, Mathematical aspects of string theory (San Diego, CA, 1986), 574-628, Adv. Ser. Math. Phys., 1, World Sci. Publishing, Singapore, 1987.
[38] G. Tian, S.-T. Yau, Complete Kähler manifolds with zero Ricci curvature, I, J. Amer. Math. Soc. 3 (1990), 579-609.
[39] S.-T. Yau, Harmonic functions on complete Riemannian manifolds, Comm. Pure Appl. Math. 28 (1975), 201-228.
[40] S.-T. Yau, On the Ricci curvature of a compact Kähler manifold and the complex Monge-Ampère equation, I, Comm. Pure Appl. Math. 31 (1978), 339-411.

School of Science, Institute for Theoretical Sciences, Westlake University, Hangzhou 310030, China
Email address: fuxin54@westlake.edu.cn
Mathematisches Institut, Universität Münster, 48149 Münster, Germany
Email address: hhein@uni-muenster.de
School of Sciences, Great Bay University, Dongguan 523000, China
Great Bay Institute for Advanced Study, Dongguan 523000, China
Email address: xjiang@gbu.edu.cn