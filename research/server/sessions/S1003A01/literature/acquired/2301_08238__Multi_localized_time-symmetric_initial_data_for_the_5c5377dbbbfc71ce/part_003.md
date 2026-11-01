---
retention_scope: session
part: 3
total_parts: 3
---

[Part 3/3 of: [2301.08238] Multi–localized time-symmetric initial data for the Einstein vacuum equations]

We just need to estimate the integrals in (A.21). This is easy, but the required expansion is cumbersome. Since $L_{g_{S}^{m}}^{*}\left(f^{m}\right)=0$, and $h\left(\gamma_{i}\right)$ vanishes along with derivatives at $\partial \Omega$, we obtain
$$\begin{aligned}
\int_{\Omega} & L_{\gamma_{2}}\left(h_{2}\right) f^{m} d \mu_{\gamma_{2}}-\int_{\Omega} L_{\gamma_{1}}\left(h_{1}\right) f^{m} d \mu_{\gamma_{1}} \\
= & \int_{\Omega} L_{\gamma_{2}}\left(h_{2}\right) f^{m}\left[d \mu_{\gamma_{2}}-d \mu_{g_{S}^{m}}\right]+\int_{\Omega}\left[L_{\gamma_{2}}-L_{g_{S}^{m}}\right]\left(h_{2}\right) f^{m} d \mu_{g_{S}^{m}}-\int_{\Omega} L_{\gamma_{1}}\left(h_{1}\right) f^{m} d \mu_{\gamma_{1}} \\
= & \int_{\Omega} L_{\gamma_{2}}\left(h_{2}-h_{1}\right) f^{m}\left[d \mu_{\gamma_{2}}-d \mu_{g_{S}^{m}}\right]+\int_{\Omega}\left[L_{\gamma_{2}}-L_{\gamma_{1}}\right]\left(h_{1}\right) f^{m}\left[d \mu_{\gamma_{2}}-d \mu_{g_{S}^{m}}\right] \\
& \quad+\int_{\Omega} L_{\gamma_{1}}\left(h_{1}\right) f^{m}\left[d \mu_{\gamma_{2}}-d \mu_{\gamma_{1}}\right]+\int_{\Omega}\left[L_{g_{S}^{m}}-L_{\gamma_{1}}\right]\left(h_{1}\right) f^{m} d \mu_{g_{S}^{m}} \\
& \quad+\int_{\Omega}\left[L_{\gamma_{2}}-L_{g_{S}^{m}}\right]\left(h_{2}\right) f^{m} d \mu_{g_{S}^{m}} \\
= & \int_{\Omega} L_{\gamma_{2}}\left(h_{2}-h_{1}\right) f^{m}\left[d \mu_{\gamma_{2}}-d \mu_{g_{S}^{m}}\right]+\int_{\Omega}\left[L_{\gamma_{2}}-L_{\gamma_{1}}\right]\left(h_{1}\right) f^{m}\left[d \mu_{\gamma_{2}}-d \mu_{g_{S}^{m}}\right] \\
& \quad+\int_{\Omega} L_{\gamma_{1}}\left(h_{1}\right) f^{m}\left[d \mu_{\gamma_{2}}-d \mu_{\gamma_{1}}\right]+\int_{\Omega}\left[L_{\gamma_{2}}-L_{\gamma_{1}}\right]\left(h_{1}\right) f^{m} d \mu_{g_{S}^{m}} \\
& \quad+\int_{\Omega}\left[L_{\gamma_{2}}-L_{g_{S}^{m}}\right]\left(h_{2}-h_{1}\right) f^{m} d \mu_{g_{S}^{m}}
\end{aligned}$$
Together with (A.21) this allows us to conclude
$$\begin{aligned}
\left|b\left(\gamma_{2}\right)-b\left(\gamma_{1}\right)\right| \leq C \| & \gamma_{1}-\gamma_{2} \|_{C^{2, \alpha}(\Omega)} \\
& +D\left\|h_{1}-h_{2}\right\|_{\mathcal{B}_{2}(\Omega)}\left(\left\|\gamma_{2}-g_{S}^{m}\right\|_{C^{2}(\Omega)}+\left\|\left(h_{1}, h_{2}\right)\right\|_{\mathcal{B}_{2}(\Omega)}\right) .
\end{aligned}$$
We obtain the same estimate in the $m=0$ case by integrating $\left.b\left(\gamma_{2}\right)-b\left(\gamma_{1}\right)\right) \zeta f^{0}=$ $R\left(\gamma_{2}+h_{2}\right)-R\left(\gamma_{1}+h_{1}\right)$ against each of the components of $f^{0}=\left\langle 1, x^{1}, x^{2}, x^{3}\right\rangle$, and estimating just as above.

Next, we estimate $\left\|f_{2}-f_{2}\right\|_{L_{\rho}^{2}\left(\Omega, \gamma_{1}\right)}$. To this end, multiply (A.16) by $\left(f_{2}-f_{1}\right)$ and integrate, using that $f_{i} \in S_{\gamma_{i}}$ along with the density of $C_{c}^{\infty}(\Omega)$ in $H_{\rho}^{2}(\Omega)$, to obtain
$$\left\|L_{\gamma_{1}}^{*}\left(f_{2}-f_{1}\right)\right\|_{L_{\rho}^{2}\left(\Omega, \gamma_{1}\right)}^{2}=\int_{\Omega}\left(f_{2}-f_{1}\right)\left(b\left(\gamma_{2}\right)-b\left(\gamma_{1}\right)\right) \zeta f^{m} d \mu_{\gamma_{1}}+\int_{\Omega}\left(f_{2}-f_{1}\right) \mathcal{E} d \mu_{\gamma_{1}}$$

We use this to estimate $f_{2}-f_{1}$. Observe that if $L_{\gamma_{1}}^{*}$ has trivial kernel, then by the same arguments in the proof of Proposition A.7, there is a constant $C_{1}$ so that for all $f \in H_{\rho}^{2}\left(\Omega, \gamma_{1}\right),\|f\|_{H_{\rho}^{2}\left(\Omega, \gamma_{1}\right)} \leq C_{1}\left\|L_{\gamma_{1}}^{*}(f)\right\|_{L_{\rho}^{2}\left(\Omega, \gamma_{1}\right)}$, which gives us an
estimate by setting $f=f_{2}-f_{1}$. In general, $f_{2}=\Pi_{\gamma_{1}}\left(f_{2}\right)+\widetilde{f}_{2}$, where for $m>0$,
$$\widetilde{f}_{2}=\frac{\left\langle f_{2}, \zeta f^{m}\right\rangle_{L^{2}\left(\Omega, \gamma_{1}\right)}}{\left\langle\zeta f^{m}, \zeta f^{m}\right\rangle_{L^{2}\left(\Omega, \gamma_{1}\right)}} \zeta f^{m}=\frac{\int_{\Omega} f_{2} \zeta f^{m}\left(d \mu_{\gamma_{1}}-d \mu_{\gamma_{2}}\right)}{\left\langle\zeta f^{m}, \zeta f^{m}\right\rangle_{L^{2}\left(\Omega, \gamma_{1}\right)}} \zeta f^{m},$$
and analogously for $m=0$. Hence $\widetilde{f_{2}}=a \zeta f^{m}$, where $\|a\| \leq C\left\|\gamma_{2}-\gamma_{1}\right\|_{C^{0}(\Omega)}$. Using this and (A.5) we have
$$\begin{aligned}
\left\|f_{2}-f_{1}\right\|_{H_{\rho}^{2}\left(\Omega, \gamma_{1}\right)} & \leq\left\|\Pi_{\gamma_{1}}\left(f_{2}\right)-f_{1}\right\|_{H_{\rho}^{2}\left(\Omega, \gamma_{1}\right)}+\left\|\widetilde{f}_{2}\right\|_{H_{\rho}^{2}\left(\Omega, \gamma_{1}\right)} \\
& \leq C\left\|L_{\gamma_{1}}^{*}\left[\Pi_{\gamma_{1}}\left(f_{2}\right)-f_{1}\right]\right\|_{L_{\rho}^{2}\left(\Omega, \gamma_{1}\right)}+\left\|\widetilde{f}_{2}\right\|_{H_{\rho}^{2}\left(\Omega, \gamma_{1}\right)} \\
& \leq C\left\|L_{\gamma_{1}}^{*}\left(f_{2}-f_{1}\right)\right\|_{L_{\rho}^{2}\left(\Omega, \gamma_{1}\right)}+C\left\|L_{\gamma_{1}}^{*}\left(\widetilde{f}_{2}\right)\right\|_{L_{\rho}^{2}\left(\Omega, \gamma_{1}\right)}+\left\|\widetilde{f}_{2}\right\|_{H_{\rho}^{2}\left(\Omega, \gamma_{1}\right)} \\
& \leq C\left\|L_{\gamma_{1}}^{*}\left(f_{2}-f_{1}\right)\right\|_{L_{\rho}^{2}\left(\Omega, \gamma_{1}\right)}+C^{\prime}\left\|\widetilde{f}_{2}\right\|_{H_{\rho}^{2}\left(\Omega, \gamma_{1}\right)} \\
& \leq C_{1}\left(\left\|L_{\gamma_{1}}^{*}\left(f_{2}-f_{1}\right)\right\|_{L_{\rho}^{2}\left(\Omega, \gamma_{1}\right)}+\left\|\gamma_{2}-\gamma_{1}\right\|_{C^{0}(\Omega)}\right) .
\end{aligned}$$

We thus conclude, using (A.23) together with (A.17), (A.19), (A.20) and (A.22),
$$\begin{aligned}
\left\|f_{2}-f_{1}\right\|_{H_{\rho}^{2}\left(\Omega, \gamma_{1}\right)}^{2} \leq & 2\left(C_{1}\right)^{2}\left(\left\|L_{\gamma_{1}}^{*}\left(f_{2}-f_{1}\right)\right\|_{L_{\rho}^{2}\left(\Omega, \gamma_{1}\right)}^{2}+\left\|\gamma_{2}-\gamma_{1}\right\|_{C^{0}(\Omega)}^{2}\right) \\
\leq & C_{2}\left\|f_{2}-f_{1}\right\|_{H_{\rho}^{2}\left(\Omega, \gamma_{1}\right)}\left(\left\|\gamma_{2}-\gamma_{1}\right\|_{C^{2, \alpha}(\Omega)}\right. \\
& \left.\quad+\left\|h_{2}-h_{2}\right\|_{\mathcal{B}_{2}(\Omega)}\left(\left\|\gamma_{2}-g_{S}^{m}\right\|_{C^{2}(\Omega)}+\left\|\left(h_{1}, h_{2}\right)\right\|_{\mathcal{B}_{2}(\Omega)}\right)\right) \\
& \quad+2 C_{1}^{2}\left\|\gamma_{2}-\gamma_{1}\right\|_{C^{0}(\Omega)}^{2} .
\end{aligned}$$
Noting for nonnegative $\beta$ and $\delta, w^{2} \leq \beta w+\delta^{2}$ implies $w \leq \beta+\delta$, we conclude
$$\begin{aligned}
\left\|f_{2}-f_{1}\right\|_{H_{\rho}^{2}\left(\Omega, \gamma_{1}\right)} \leq C( & \left\|\gamma_{2}-\gamma_{1}\right\|_{C^{2, \alpha}(\Omega)} \\
.26) & \left.\quad+\left\|h_{2}-h_{2}\right\|_{\mathcal{B}_{2}(\Omega)}\left(\left\|\gamma_{2}-g_{S}^{m}\right\|_{C^{2}(\Omega)}+\left\|\left(h_{1}, h_{2}\right)\right\|_{\mathcal{B}_{2}(\Omega)}\right)\right) .
\end{aligned}$$

We have the following, using (A.17), (A.18), (A.22), (A.26) and the weighted Schauder estimate (A.6) (where the constant " $C$ " can change from line to line)
$$\begin{aligned}
\left\|h_{2}-h_{1}\right\|_{\mathcal{B}_{2}(\Omega)}= & \left\|\rho L_{\gamma_{2}}^{*}\left(f_{2}\right)-\rho L_{\gamma_{1}}^{*}\left(f_{1}\right)\right\|_{\mathcal{B}_{2}(\Omega)} \\
\leq & \left\|\rho L_{\gamma_{1}}^{*}\left(f_{2}-f_{1}\right)\right\|_{\mathcal{B}_{2}(\Omega)}+\left\|\rho\left(L_{\gamma_{2}}^{*}-L_{\gamma_{1}}^{*}\right)\left(f_{2}\right)\right\|_{\mathcal{B}_{2}(\Omega)} \\
\leq & C\left\|f_{2}-f_{1}\right\|_{\mathcal{B}_{4}(\Omega)}+\left\|\rho\left(L_{\gamma_{2}}^{*}-L_{\gamma_{1}}^{*}\right)\left(f_{2}\right)\right\|_{\mathcal{B}_{2}(\Omega)} \\
\leq & C\left(\left\|f_{2}-f_{1}\right\|_{\mathcal{B}_{4}(\Omega)}+\left\|\gamma_{2}-\gamma_{1}\right\|_{C^{4, \alpha}(\Omega)}\left\|f_{2}\right\|_{\mathcal{B}_{4}(\Omega)}\right) \\
\leq & C\left(\left\|\rho^{-1} L_{\gamma_{1}}\left[\rho L_{\gamma_{1}}^{*}\left(f_{2}-f_{1}\right)\right]\right\|_{C_{\phi, \phi^{4+\frac{3}{2} \rho^{\frac{1}{2}}}}^{0, \alpha}}+\left\|f_{2}-f_{1}\right\|_{H_{\rho}^{2}(\Omega)}\right. \\
& \left.\quad+\left\|\gamma_{2}-\gamma_{1}\right\|_{C^{4, \alpha}(\Omega)}\left\|f_{2}\right\|_{\mathcal{B}_{4}(\Omega)}\right) \\
\leq & C\left(\left\|\rho^{-1}\left(b\left(\gamma_{2}\right)-b\left(\gamma_{1}\right)\right) \zeta f^{m}\right\|_{\phi, \phi^{4+\frac{3}{2} \rho^{\frac{1}{2}}}}+\left\|\rho^{-1} \mathcal{E}\right\|_{C_{\phi, \phi^{4+\frac{3}{2} \rho^{\frac{1}{2}}}}}\right. \\
& \left.\quad\left\|f_{2}-f_{1}\right\|_{H_{\rho}^{2}(\Omega)}+\left\|\gamma_{2}-\gamma_{1}\right\|_{C^{4, \alpha}(\Omega)}\left\|f_{2}\right\|_{\mathcal{B}_{4}(\Omega)}\right) \\
\leq & C\left(\left\|\gamma_{2}-\gamma_{1}\right\|_{C^{4, \alpha}(\Omega)}\right. \\
& \left.\quad+\left\|h_{2}-h_{1}\right\|_{\mathcal{B}_{2}(\Omega)}\left(\left\|\gamma_{2}-g_{S}^{m}\right\|_{C^{2}(\Omega)}+\left\|\left(h_{1}, h_{2}\right)\right\|_{\mathcal{B}_{2}(\Omega)}\right)\right) .
\end{aligned}$$

For $\gamma_{1}$ and $\gamma_{2}$ close enough to $g_{S}^{m}, R\left(\gamma_{i}\right)$ is close to zero, so that $\left\|h_{i}\right\|_{\mathcal{B}_{2}(\Omega)} \leq$ $C\left\|R\left(\gamma_{i}\right)\right\|$ is sufficiently small so that we can absorb the second term on the righthand side, to conclude $\left\|h_{2}-h_{1}\right\|_{\mathcal{B}_{2}(\Omega)} \leq C^{\prime}\left\|\gamma_{2}-\gamma_{1}\right\|_{C^{4, \alpha}(\Omega)}$, as desired. \(\square\)

Remark A.15. We observe that if $L_{\gamma_{1}}^{*}$ had non-trivial kernel, then as $R\left(\gamma_{1}\right)$ is constant ([21, Thm. 1], cf. [15, Prop. 2.3] or [18, Prop. 2.1]), it must vanish. In that case, $h_{1}=0$, and then $R(\gamma) \rightarrow 0$ in $\mathcal{B}_{0}(\Omega)$ for $\gamma \rightarrow \gamma_{1}$ in $C^{2, \alpha}(\bar{\Omega})$ and with $R(\gamma)$ supported in a fixed subset $\overline{\Omega^{\prime}} \subset \Omega$. Via Lemma A.13, we can then conclude $h(\gamma) \rightarrow 0=h_{1}$ in $\mathcal{B}_{2}(\Omega)$.

\section*{References}
\begin{itemize}
\item[] [1] John Anderson and Federico Pasqualotto. Global Stability for Nonlinear Wave Equations with Multi-Localized Initial Data. Ann. PDE, 8(2):Paper No. 19, 2022.
\item[] [2] Stefanos Aretakis, Stefan Czimek, and Igor Rodnianski. The characteristic gluing problem for the Einstein equations and applications, 2022. https://arxiv.org/abs/2107.02441.
\item[] [3] Robert Bartnik. The mass of an asymptotically flat manifold. Comm. Pure Appl. Math., 39(5):661-693, 1986.
\item[] [4] Robert Bartnik and Jim Isenberg. The constraint equations. In The Einstein equations and the large scale behavior of gravitational fields, pages 1-38. Birkhäuser, Basel, 2004.
\item[] [5] Robert Beig and Niall Ó Murchadha. Trapped surfaces due to concentration of gravitational radiation. Phys. Rev. Lett., 66(19):2421-2424, 1991.
\item[] [6] Dieter R. Brill and Richard W. Lindquist. Interaction energy in geometrostatics. Phys. Rev. (2), 131:471-476, 1963.
\item[] [7] Alessandro Carlotto and Richard Schoen. Localizing solutions of the Einstein constraint equations. Invent. Math., 205(3):559-615, 2016.
\item[] [8] Yvonne Choquet-Bruhat and Robert Geroch. Global aspects of the Cauchy problem in general relativity. Comm. Math. Phys., 14:329-335, 1969.
\item[] [9] Demetrios Christodoulou and Sergiu Klainerman. The global nonlinear stability of the Minkowski space, volume 41 of Princeton Mathematical Series. Princeton University Press, Princeton, NJ, 1993.
\item[] [10] Piotr T. Chruściel, Justin Corvino, and James Isenberg. Construction of $N$-body initial data sets in general relativity. Comm. Math. Phys., 304(3):637-647, 2011.
\item[] [11] Piotr T. Chruściel, Justin Corvino, and James Isenberg. Construction of $N$-body time-symmetric initial data sets in general relativity. In Complex analysis and dynamical systems IV. Part 2, volume 554 of Contemp. Math., pages 83-92. Amer. Math. Soc., Providence, RI, 2011.
\item[] [12] Piotr T. Chruściel and Erwann Delay. Existence of non-trivial, vacuum, asymptotically simple spacetimes. Classical Quantum Gravity, 19(9):L71-L79, 2002.
\item[] [13] Piotr T. Chruściel and Erwann Delay. On mapping properties of the general relativistic constraints operator in weighted function spaces, with applications. Mém. Soc. Math. Fr. (N.S.), (94):vi+103, 2003.
\item[] [14] Piotr T. Chruściel and Rafe Mazzeo. On "many-black-hole" vacuum spacetimes. Classical Quantum Gravity, 20(4):729-754, 2003.
\item[] [15] Justin Corvino. Scalar curvature deformation and a gluing construction for the Einstein constraint equations. Comm. Math. Phys., 214(1):137-189, 2000.
\item[] [16] Justin Corvino. A note on asymptotically flat metrics on $\mathbb{R}^{3}$ which are scalar-flat and admit minimal spheres. Proc. Amer. Math. Soc., 133(12):3669-3678, 2005.
\item[] [17] Justin Corvino. On the existence and stability of the Penrose compactification. Ann. Henri Poincaré, 8(3):597-620, 2007.
\item[] [18] Justin Corvino, Michael Eichmair, and Pengzi Miao. Deformation of scalar curvature and volume. Math. Ann., 357(2):551-584, 2013.
\item[] [19] Justin Corvino and Lan-Hsuan Huang. Localized deformation for initial data sets with the dominant energy condition. Calc. Var. Partial Differential Equations, 59(1):Paper No. 42, 43, 2020.
\item[] [20] Justin Corvino and Richard M. Schoen. On the asymptotics for the vacuum Einstein constraint equations. J. Differential Geom., 73(2):185-217, 2006.
\end{itemize}
\begin{itemize}
\item[] [21] Arthur E. Fischer and Jerrold E. Marsden. Deformations of the scalar curvature. Duke Math. J., 42(3):519-547, 1975.
\item[] [22] Y. Fourès-Bruhat. Théorème d'existence pour certains systèmes d'équations aux dérivées partielles non linéaires. Acta Math., 88:141-225, 1952.
\item[] [23] Gregory J. Galloway, Pengzi Miao, and Richard Schoen. Initial data and the Einstein constraint equations. In General relativity and gravitation, pages 412-448. Cambridge Univ. Press, Cambridge, 2015.
\item[] [24] David Gilbarg and Neil S. Trudinger. Elliptic partial differential equations of second order, volume 224 of Grundlehren der mathematischen Wissenschaften [Fundamental Principles of Mathematical Sciences]. Springer-Verlag, Berlin, second edition, 1983.
\item[] [25] S. Klainerman. Long time behavior of solutions to nonlinear wave equations. Proceedings of the International Congress of Mathematicians, Warsaw, (1983), pages 1209-1215, 1983.
\item[] [26] Junbin Li and Pin Yu. Construction of Cauchy data of vacuum Einstein field equations evolving to black holes. Ann. of Math. (2), 181(2):699-768, 2015.
\item[] [27] Joachim Lohkamp. Scalar curvature and hammocks. Math. Ann., 313(3):385-407, 1999.
\item[] [28] Yuchen Mao and Zhongkai Tao. Localized initial data for Einstein equations, 2022. https://arxiv.org/abs/2210.09437.
\item[] [29] Norman Meyers. An expansion about infinity for solutions of linear elliptic equations. J. Math. Mech., 12:247-264, 1963.
\item[] [30] Pengzi Miao. Asymptotically flat and scalar flat metrics on $\mathbb{R}^{3}$ admitting a horizon. Proc. Amer. Math. Soc., 132(1):217-222, 2004.
\item[] [31] Charles W. Misner. The method of images in geometrostatics. Ann. Physics, 24:102-117, 1963.
\item[] [32] Hans Ringström. The Cauchy problem in general relativity. ESI Lectures in Mathematics and Physics. European Mathematical Society (EMS), Zürich, 2009.
\item[] [33] Richard Schoen and Shing Tung Yau. On the proof of the positive mass conjecture in general relativity. Comm. Math. Phys., 65(1):45-76, 1979.
\item[] [34] Christina Sormani and Iva Stavrov Allen. Geometrostatic manifolds of small ADM mass. Comm. Pure Appl. Math., 72(6):1243-1287, 2019.
\end{itemize}

Department of Mathematics, Stanford University, Stanford, CA 94305, USA
Email address: jrlander@stanford.edu
Department of Mathematics, Lafayette College, Easton, PA 18042, USA
Email address: corvinoj@lafayette.edu
Department of Mathematics, UC Berkeley, Berkeley, CA 94720, USA
Email address: fpasqualotto@berkeley.edu