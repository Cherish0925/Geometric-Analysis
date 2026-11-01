---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Refined gluing for Vacuum Einstein constraint equations]

We start with the estimate of the error term. To simplify the notations we decompose $F_{\varepsilon}(v)$ as
$$F_{\varepsilon}(v)=F_{\varepsilon}^{(0)}+F_{\varepsilon}^{(1)}(v)+F_{\varepsilon}^{(2)}(v, v),$$
where the three summands on the right hand side correspond respectively to the zero order term of $F_{\varepsilon}(v)$, the terms which have a linear dependence on $v$ and to the terms which depend quadratically on $v$. Here the crucial part is the estimate of the pure error term
$$\begin{aligned}
F_{\varepsilon}^{(0)}:= & -c_{m}\left(R_{g_{1}}-R_{g_{\varepsilon}}\right) \chi_{1}+c_{m}\left(\left|\mu_{1}\right|_{g_{1}}^{2}-\left|\mu_{\varepsilon}\right|_{g_{\varepsilon}}^{2}\right) \chi_{1} \\
& -c_{m}\left(R_{g_{2}}-R_{g_{\varepsilon}}\right) \chi_{2}+c_{m}\left(\left|\mu_{2}\right|_{g_{2}}^{2}-\left|\mu_{\varepsilon}\right|_{g_{\varepsilon}}^{2}\right) \chi_{2} .
\end{aligned}$$
Recalling that the approximate solution metrics are the same used by the second author in [29], we recover from [29, Proposition 2] the estimate of the scalar curvature error. More precisely, we have that on the poly-neck region $\{\log \varepsilon \leq t \leq-\log \varepsilon\}$
$$\left|\chi_{1}\left(R_{g_{1}}-R_{g_{\varepsilon}}\right)+\chi_{2}\left(R_{g_{2}}-R_{g_{\varepsilon}}\right)\right| \leq C_{1} \varepsilon^{n-2} \rho_{\varepsilon}^{1-n},$$
for some positive constant $C_{1}>0$ independent of $\varepsilon \in(0,1)$. Now, using Proposition 5, we show that the same bound holds for the $T T$-tensor error. We claim that
$$\left|\chi_{1}\left(\left|\mu_{1}\right|_{g_{1}}^{2}-\left|\mu_{\varepsilon}\right|_{g_{\varepsilon}}^{2}\right)+\chi_{2}\left(\left|\mu_{2}\right|_{g_{2}}^{2}-\left|\mu_{\varepsilon}\right|_{g_{\varepsilon}}^{2}\right)\right| \leq C_{2} \varepsilon^{n-2} \rho_{\varepsilon}^{1-n},$$
for some positive constant $C_{2}>0$ independent of $\varepsilon \in(0,1)$. To see this fact, we focus on the first summand on the left hand side (since the reasoning can be repeated for the second one) and we observe that it is dominated by $\left|D_{g_{\varepsilon}} X\right|_{g_{\varepsilon}}^{2}+\left|\mu-\mu_{1}\right|_{g_{\varepsilon}}^{2}$, where $X$ solves $L_{g_{\varepsilon}} X=\sharp \operatorname{div}_{g_{\varepsilon}} \mu$. Since $\left|\mu-\mu_{1}\right|_{g_{\varepsilon}}^{2}$ is zero outside the boundary of the poly-neck and since it is clearly bounded in the middle, we can concentrate on the squared pointwise norm of $D_{g_{\varepsilon}} X$.

To keep this term under control, we recall from Proposition 5 that there exists a positive constant $C_{0}>0$ such that for sufficiently small $\varepsilon$ 's
$$\left|D_{g_{\varepsilon}} X\right|_{g_{\varepsilon}} \leq C_{0}\left\|\operatorname{div}_{g_{\varepsilon}} \mu\right\|_{E_{\delta-2}^{1}} \rho_{\varepsilon}^{\delta-1} .$$
At this point it is clear that if we show that $\left|D_{g_{\varepsilon}} X\right|_{g_{\varepsilon}}^{2} \leq C_{3} \varepsilon^{n-2} \rho_{\varepsilon}^{1-n}$, for some $C_{3}>0$, then our claim (36) will follows at once. Thus, thanks to the last inequality, it is sufficient to show that
$$\left\|\operatorname{div}_{g_{\varepsilon}} \mu\right\|_{E_{\delta-2}^{1}} \leq C_{4} \varepsilon^{\frac{n-2}{2}} \rho_{\varepsilon}^{\frac{3-n}{2}-\delta},$$
for some positive constant $C_{4}>0$. Since $2-n<\delta<(2-n) / 2$, this reduces to proving that
$$\left|\operatorname{div}_{g_{\varepsilon}} \mu\right|_{g_{\varepsilon}} \leq C_{5} \varepsilon^{\frac{1}{2}-\delta} \rho_{\varepsilon}^{\delta-2} \quad \text { and } \quad\left|\nabla \operatorname{div}_{g_{\varepsilon}} \mu_{\varepsilon}\right|_{g_{\varepsilon}} \leq C_{6} \varepsilon^{\frac{1}{2}-\delta} \rho_{\varepsilon}^{\delta-3} .$$
for some positive constants $C_{5}, C_{6}>0$. If we choose the constant $0<c<1$ which appears in the construction of $\mu$ in Section 2 to be $c=3 /(4-2 \delta)$, then both these conditions are satisfied and we get the desired bound for $\left|D_{g_{\varepsilon}} X\right|_{g_{\varepsilon}}^{2}$. The claim (36) is now proven and we can deduce that the pure error term can be estimated as
$$\left|F_{\varepsilon}^{(0)}\right| \leq C_{7} \varepsilon^{n-2} \rho_{\varepsilon}^{1-n} .$$
As a consequence, we immediately get the following estimate
$$\rho_{\varepsilon}^{2-\gamma}\left|F_{\varepsilon}(v)\right| \leq C_{8}\left(1+|v|+|v|^{2}\right) \varepsilon^{1-\gamma}(\cosh t)^{3-n-\gamma}+C_{9}|v|^{2} \varepsilon^{2-\gamma}(\cosh t)^{2-\gamma} .$$
Now suppose that $v$ lies in a ball of small radius $r_{\varepsilon}=\varepsilon^{\mu}$ in $C^{0}\left(M_{\varepsilon}\right)$, with $\mu>0$ to be determined, and combine the estimate above with (34) to obtain
$$\left\|\mathcal{L}_{g_{\varepsilon}}^{-1} \circ F_{\varepsilon}(v)\right\|_{F_{\gamma}^{0}} \leq C_{10}\left(1+r_{\varepsilon}+r_{\varepsilon}^{2}\right)\left[\varepsilon^{1-\gamma}+\varepsilon^{n-2}\right]+C_{11} r_{\varepsilon}^{2} .$$
The definition of the $\gamma$-weighted norm implies
$$\left|\mathcal{L}_{g_{\varepsilon}}^{-1} \circ F_{\varepsilon}(v)\right| \leq C_{12}\left(1+r_{\varepsilon}+r_{\varepsilon}^{2}\right)\left[\varepsilon+\varepsilon^{n-2+\gamma}\right]+C_{13} r_{\varepsilon}^{2} .$$
Now, it is sufficient to choose $a$ such that $0<a<\min \{1,(n-2)+\gamma\}$ to conclude that for $\varepsilon$ sufficiently small the mapping $\mathcal{L}_{g_{\varepsilon}}^{-1} \circ F_{\varepsilon}$ send the ball of radius $r_{\varepsilon}=\varepsilon^{a}$ centered at the origin of $C^{0}\left(M_{\varepsilon}\right)$ in itself. The fact that $\mathcal{L}_{g_{\varepsilon}}^{-1} \circ F_{\varepsilon}$ is also a contraction in this ball follows from a direct and easier computation, whose details are left to the reader.

Provided $\varepsilon$ is chosen in a sufficiently small range, we can apply the contraction mapping Theorem and we obtain a fixed point $v_{\varepsilon}$ for (31) and thus a solution $\tilde{u}_{\varepsilon}=1+v_{\varepsilon}$ to (28). The fact that $v_{\varepsilon}$ and hence $\tilde{u}_{\varepsilon}$ is smooth, follows from the elliptic regularity theory, using a standard boot strap argument. Since $v_{\varepsilon}$ lies in a ball of radius $r_{\varepsilon}=\varepsilon^{a}$ in $C^{0}\left(M_{\varepsilon}\right)$, we deduce at once that the new solutions of the constraint equations converge to hold ones on the compact sets of $M_{i} \backslash K, i=1,2$, with respect to the $C^{0}$-topology, as $\varepsilon \rightarrow 0$.

To obtain the smooth convergence claimed in the statement of Theorem 1, it is now sufficient to combine this $C^{0}$-bound with interior Schauder estimate. To see this fact we show how it is possible to obtain the $C^{2, \alpha}$-control on the compact subsets of $M_{1} \backslash K$. The same argument can be applied with minor changes in order to obtain $C^{k, \alpha}$-convergence on the compact subsets of $M_{i} \backslash K$, for $i=1,2$ and every $k \in \mathbb{N}$. We fix now a compact subset $Q \subset M_{1} \backslash K$ and thanks to [17, Proposition 6.2], we have that
$$\left\|v_{\varepsilon}\right\|_{C^{2, \alpha}(Q)}^{(0)} \leq A_{0}\left[\left\|F_{\varepsilon}\left(v_{\varepsilon}\right)\right\|_{C^{0, \alpha}(Q)}^{(2)}+\left\|v_{\varepsilon}\right\|_{C^{0}(Q)}\right],$$
where the interior norms $\|\cdot\|_{C^{k, \alpha}(Q)}^{(\sigma)}$ correspond to the interior norms $|\cdot|_{k, \alpha ; Q}^{(\sigma)}$ defined in [17]. From (38) we deduce that there exists a positive constant
$A_{1}>0$ such that
$$\begin{aligned}
\left\|v_{\varepsilon}\right\|_{C^{2, \alpha}(Q)}^{(0)} \leq & A_{1}\left[\left\|F_{\varepsilon}^{(0)}\right\|_{C^{1}(Q)}^{(2)}+\left\|v_{\varepsilon}\right\|_{C^{0}(Q)}+\sup _{Q} d_{p}^{2}\left|v_{\varepsilon}\right|^{2}\right. \\
& +\sup _{Q} d_{p}^{2}\left|v_{\varepsilon}\right|\left|R_{g_{1}}-R_{g_{\varepsilon}}\right|+\sup _{Q} d_{p}^{3}\left|v_{\varepsilon}\right|\left|\nabla\left(R_{g_{1}}-R_{g_{\varepsilon}}\right)\right| \\
& +\left.\sup _{Q} d_{p}^{2}\left|v_{\varepsilon}\right|| | \mu_{1}\right|_{g_{1}} ^{2}-\left|\mu_{\varepsilon}\right|_{g_{\varepsilon} \mid}^{2}\left|+\sup _{Q} d_{p}^{3}\right| v_{\varepsilon}| | \nabla\left(\left|\mu_{1}\right|_{g_{1}}^{2}-\left|\mu_{\varepsilon}\right|_{g_{\varepsilon}}^{2}\right) \mid \\
& +\sup _{Q} d_{p}^{3}\left|\nabla v_{\varepsilon}\right|\left|R_{g_{1}}-R_{g_{\varepsilon}}\right|+\left.\sup _{Q} d_{p}^{3}\left|\nabla v_{\varepsilon}\right|| | \mu_{1}\right|_{g_{1}} ^{2}-\left|\mu_{\varepsilon}\right|_{g_{\varepsilon} \mid}^{2} \mid \\
& \left.+\sup _{Q} d_{p}^{3}\left|\nabla v_{\varepsilon}\right|\left|v_{\varepsilon}\right|\right],
\end{aligned}$$
where $d_{p}$ is a short notation for the distance to the boundary of the compact set $Q$, namely $d_{p}:=\operatorname{dist}_{g_{1}}(p, \partial Q)$. Now it is easy to check that, except for the last three summands, the right hand side tends to zero, as $\varepsilon \rightarrow 0$. On the other hand, for $\varepsilon$ sufficiently small, these last three terms involving the first derivative of $v_{\varepsilon}$ can be absorbed by the left hand side. Hence, there exists a positive constant $A_{2}>0$ and there exists a real number $\varepsilon_{0}$, such that for every $\varepsilon \in\left(0, \varepsilon_{0}\right]$
$$\begin{aligned}
\left\|v_{\varepsilon}\right\|_{C^{2, \alpha}(Q)}^{(0)} \leq & A_{2}\left[\left\|F_{\varepsilon}^{(0)}\right\|_{C^{1}(Q)}^{(2)}+\left\|v_{\varepsilon}\right\|_{C^{0}(Q)}+\left\|v_{\varepsilon}\right\|_{C^{0}(Q)}^{(2)}\left\|v_{\varepsilon}\right\|_{C^{0}(Q)}\right. \\
& +\left\|R_{g_{1}}-R_{g_{\varepsilon}}\right\|_{C^{0}(Q)}^{(2)}\left\|v_{\varepsilon}\right\|_{C^{0}(Q)}+\left\|\left|\mu_{1}\right|_{g_{1}}^{2}-\left|\mu_{\varepsilon}\right|_{g_{\varepsilon}}^{2}\right\|_{C^{0}(Q)}^{(2)}\left\|v_{\varepsilon}\right\|_{C^{0}(Q)} \\
& +\| \nabla\left(R_{g_{1}}-R_{\left.g_{\varepsilon}\right)}\left\|_{C^{0}(Q)}^{(3)}\right\| v_{\varepsilon} \|_{C^{0}(Q)}\right. \\
& +\| \nabla\left(\left|\mu_{1}\right|_{g_{1}}^{2}-\left|\mu_{\varepsilon}\right|_{\left.g_{\varepsilon}\right)}^{2}\left\|_{C^{0}(Q)}^{(3)}\right\| v_{\varepsilon} \|_{C^{0}(Q)}\right] .
\end{aligned}$$
We deduce that $v_{\varepsilon} \rightarrow 0$ on the compact subset of $M_{1} \backslash K$ with respect to the $C^{2, \alpha}$-topology. As we have already observed, this argument can be easily modified in order to deduce the smooth convergence on the compact subsets of $M_{i} \backslash K, i=1,2$. This concludes the proof of Theorem 1.

\section*{6. Localized gluing}

In this section, we give the proof of Theorem 2. We will then show that the generalized conformal gluing procedure used in [31] for compact manifolds and here for AE and AH manifolds, can be, in a second hand, localized in order to keep the original data outside a small neighborhood of the neck. This technique, inspired by the Corvino Shoen method [14], was already employed in [11] to localize the gluing of Isenberg, Mazzeo and Pollack [21].

Proof. Let $\chi$ be a non negative smooth cut-off function equal to 1 in a neighborhood of $\partial K_{\varepsilon_{1}}^{i}$ and equal to zero in a neighborhood of $\partial K_{2 \varepsilon_{1}}^{i}$. On $\Gamma^{i}\left(\varepsilon_{1}, 2 \varepsilon_{1}\right)$ set
$$\begin{aligned}
\stackrel{\circ}{\Pi}_{\varepsilon} & =\chi \tilde{\Pi}_{\varepsilon}+(1-\chi) \Pi_{i}, \\
\stackrel{\circ}{g}_{\varepsilon} & =\chi \tilde{g}_{\varepsilon}+(1-\chi) g_{i} .
\end{aligned}$$
Then $\left(\stackrel{\circ}{g}_{\varepsilon}, \stackrel{\circ}{\Pi}_{\varepsilon}\right)$ coincides with the data $\left(\tilde{g}_{\varepsilon}, \tilde{\Pi}_{\varepsilon}\right)$ in a neighborhood of $\partial K_{\varepsilon_{1}}^{i}$, and coincides with the original data $\left(g_{i}, \Pi_{i}\right)$ in a neighborhood of $\partial K_{2 \varepsilon_{1}}^{i}$. It follows that $\rho\left(\stackrel{\circ}{g}_{t}, \stackrel{\circ}{\Pi}_{t}\right)$ and $J\left(\stackrel{\circ}{g}_{t}, \stackrel{\circ}{\Pi}_{t}\right)$ are supported away from the boundary in $\Gamma^{i}\left(\varepsilon_{1}, 2 \varepsilon_{1}\right)$. Since the data constructed in [31] or here in the AE and

AH case, converge uniformly, in any $C^{k, \alpha}$ norm, to the original ones on $\Gamma^{i}\left(\varepsilon_{1}, 2 \varepsilon_{1}\right)$ we will have
$$\lim _{\varepsilon \rightarrow 0} \rho\left(\stackrel{\circ}{K}_{\varepsilon}, \stackrel{\circ}{g}_{\varepsilon}\right)=0=\lim _{\varepsilon \rightarrow 0} J\left(\stackrel{\circ}{K}_{\varepsilon}, \stackrel{\circ}{g}_{\varepsilon}\right) .$$
Theorem 5.9 and Corollary 5.11 of [11] provides $0<\varepsilon_{2} \leq \varepsilon_{1}$ such that for all $0<\varepsilon \leq \varepsilon_{2}$ there exists a solution $\left(\hat{g}_{\varepsilon}, \hat{\Pi}_{\varepsilon}\right)$ of the vacuum constraint equations which is smoothly extended by $\left(\tilde{g}_{\varepsilon}, \tilde{\Pi}_{\varepsilon}\right)$ across $\partial K_{\varepsilon_{1}}^{i}$ and by $\left(g_{i}, \Pi_{i}\right)$ across $\partial K_{2 \varepsilon_{1}}^{i}$. \(\square\)

\section*{7. Constraint with cosmological constant and constant scalar curvature metrics}

The previous constructions (conformal and local gluing) can be adapted to the context of vacuum Einstein constraint equations with cosmological constant
$$\begin{aligned}
J(g, \Pi):=\operatorname{div}_{g} \Pi-d\left(\operatorname{tr}_{g} \Pi\right) & =0 \\
\rho(g, \Pi):=R_{g}-|\Pi|_{g}^{2}+\left(\operatorname{tr}_{g} \Pi\right)^{2} & =2 \Lambda .
\end{aligned}$$
As an interesting example we mention the case of the hyperbolic space $\mathbb{H}^{m}$ viewed as horizontal slice in AdS space time. In fact it is well known that this object satisfies the equations above with $\Lambda=-m(m-1) / 2$ and $\Pi=0$. To adapt our construction to this case it is sufficient to replace the condition $\tau=m$ (which is natural when $\mathbb{H}^{m}$ is viewed as a slice in Minkowsky spacetime) by $\tau=0$, as in the AE case.

Others interesting examples are given by constant scalar curvature Riemannian metrics. In fact these are time symmetric $(\Pi=0)$ solutions to the vacuum Einstein contraint with cosmological constant $\Lambda$. In [29] and [30] generalized connected sum of such metrics have been obtained by the second author. The adaptation of these conformal gluing to the non compact AE and AH context proceed exactly as in our proof of Theorem 1 and in fact it is easier. Also, the adaptation of the localized gluing proceed exactly as in Section 6, the no KID's condition being here that the adjoint $D R(g)^{*}$ of the linearized scalar curvature operator has no kernel on $\Gamma^{i}\left(\varepsilon_{1}, 2 \varepsilon_{1}\right)$.

\section*{8. Concluding remarks}

We have shown that the generalized connected sum of some class of solutions to the Einstein constraints equations can also be performed in natural non compact setting such as AE or AH manifolds, as far as the submanifold we cut around is compact. In addition, we have shown that whatever the manifold is compact or not, the conformal gluing procedure can be localized in a neighborhood of the poly-neck region.

To conclude, we list some open questions which will be the object of further investigation.
1) In the non compact setting it would be natural to consider the connected sum along non compact submanifold so :
a) It seems that the conformal gluing could be adapted to this situation, provided the submanifold itself present a suitable asymptotic behavior.
b) The 'localized gluing' need also to be understood in this case. A closely related question is the gluing along an horizontal band in the (half space
type) AH context. It seems to us that in this situation one could overcome some of the scaling difficulties encountered in [12].
2) So far, the localized gluing procedure can be applied only after the conformal one is performed. It will be interesting to understand under which hypothesis one can produce a localized gluing directly (see the unfortunate tentative in [9] section 5 withdraw in [10]).
3) It will be interesting to see if the generalized gluing can produce black hole with special topology.

Acknowledgements. The first author is grateful to the french ANR project 'GeomEinstein' for financial support. The second author is supported by the Italian project FIRB-IDEAS 'Analysis and Beyond' and he is grateful to the University of Avignon for the hospitality during the preparation of this work.

\section*{References}
\begin{itemize}
\item[] [1] L. Andersson and P.T. Chruściel, On asymptotic behavior of solutions of the constraint equations in general relativity with "hyperboloidal boundary conditions", Dissert. Math. 355 (1996), 1-100.
\item[] [2] T. Aubin, Some nonlinear Problems in Riemannian Geometry, Springer Monographs in Mathematics, Springer, (1998).
\item[] [3] R. Bartnik, The mass of an asymptotically flat manifold, Comm. Pure Appl. Math. 39 (1986), no. 5, 661-693.
\item[] [4] R. Bartnik and J. Isenberg, The constraint equations, The Einstein equationsand the large scale behavior of gravitational fields, eds. P. T. Chrusciel and H. Friedrich, Birkhäuser, Basel, (2004), 1-39.
\item[] [5] R. Beig, P. T. Chruściel and R. Schoen, KIDs are non-generic, Ann. Henri Poincaré 6 (2005), no. 1, 155-194.
\item[] [6] D. Christodoulou, Y. Choquet-Bruhat, Elliptic systems in $H_{s, \delta}$ spaces on manifolds which are Euclidean at infinity, Acta Math. 146 (1981), 129-150.
\item[] [7] D. Christodoulou, N. O'Murchada, The boost problem in general relativity, Commun. Math. Phys. 80 (1981), 171-300.
\item[] [8] Y. Choquet-Bruhat, Théorème d'existence pour certains systèmes d'équations aux dérivées partielles non linéaires, Acta Math. 88 (1952), 141-225.
\item[] [9] P. T. Chruściel, E. Delay, Existence of non-trivial, vacuum, asymptotically simple space-times, Class. Quantum Grav. 19 (2002), p.71-79, gr-qc/0203053
\item[] [10] P. T. Chruściel, E. Delay, Erratum: Existence of non-trivial, vacuum, asymptotically simple space-times, Class. Quantum Grav., 19 (2002), 3389.
\item[] [11] P. T. Chruściel, E. Delay, On mapping properties of the general relativistic constraints operator in weighted function spaces, with applications, Mémoires de la S.M.F., 2003, n ${ }^{0} 94$, 103p., gr-qc/0301073
\item[] [12] P. T. Chruściel, E. Delay, Gluing constructions for asymptotically hyperbolic manifolds with constant scalar curvature, Comm. Anal. Geom., vol. 17, no. 2, 2009, 39p, to appear, arXiv:0711.1557
\item[] [13] P. T. Chruściel, J. Isenberg, D. Pollack, Initial data engineering, Comm. Math. Phys. 257 (2005), 29-42.
\item[] [14] J. Corvino and R. Schoen, On the asymptotics for the vacuum Einstein constraint equations, gr-qc/0301071
\item[] [15] M. Giaquinta, L. Martinazzi, An introduction to the regularity thoery for elliptic systems, harmonic maps and minimal graphs, Edizioni della Normale (2005).
\item[] [16] R. Gicquaud, De l'équation de prescription de courbure scalaire aux équations de contrainte en relativité générale sur une variété asymptotiquement hyperbolique, (2008), 41p, arXiv:0802.3279.
\item[] [17] D. Gilbarg, N. Trudinger, Elliptic Partial Differential Equation of Second Order, Springer, (1997).
\end{itemize}
\begin{itemize}
\item[] [18] M. Gromov, H. B. Lawson The classification of simply connected manifolds of positive scalar curvature. Ann. of Math. (2) 111 (1980), no. 3, 423-434.
\item[] [19] D. Joyce Constant scalar curvature metrics on connected sums. Int. J. Math. Math. Sci. (2003), no. 7, 405-450.
\item[] [20] J. Isenberg, D. Maxwell, D. Pollack, A gluing construction for non vacuum solutions of the Einstein constraint equations, Adv. Theor. Phys. 9 (2005), 129-172.
\item[] [21] J. Isenberg, R. Mazzeo, D. Pollack, Gluing and wormholes for the Einstein constraint equations, Comm. Math. Phys. 231 (2002), 529-568.
\item[] [22] J.M. Lee, Fredholm operators and Einstein metrics on conformally compact manifolds, Memoirs AMS 183 (2006), no. 864, math.DG/0105046
\item[] [23] J. M. Lee, T. H. Parker, The Yamabe Problem, Bull. A.M.S. 17 (1987), 37-91.
\item[] [24] R. Mazzeo, Elliptic theory of differential edge operators, Comm. Part. Diff. Eqs. 16 (1991), 1615-1664.
\item[] [25] R. Mazzeo, F. Pacard, Constant scalar curvature metrics with isolated singularities, Duke Math. Journal 99 No. 3 (1999) 353-418.
\item[] [26] R. Mazzeo, F. Pacard, Constant mean curvature surfaces with Delaunay ends, Comm. Anal. Geom. 9 No. 1 (2001) 169-237.
\item[] [27] R. Mazzeo, F. Pacard, D. Pollack, Connected sums of constant mean curvature surfaces in Euclidean 3 space, J. Reine Angew. Math. 536 (2001), 115-165.
\item[] [28] R. Mazzeo, D. Pollack, K. Uhlenbeck, Connected sums constructions for constant scalar curvature metrics, Topological Method in Nonlinear Analysis 6 (1995), 207-233.
\item[] [29] L. Mazzieri Generalized connected sum construction for nonzero constant scalar curvature metrics, Communication in Partial Differential Equations 33 (2008), 1-17.
\item[] [30] L. Mazzieri Generalized connected sum construction for scalar flat metrics, Manuscripta Mathematica 129 (2009), 137-168.
\item[] [31] L. Mazzieri Generalized gluing for Einstein constraint equations, Calculus of Variations and Partial Differential Equations 34 (2009), 453-473.
\item[] [32] R. Schoen, S. T. Yau On the structure of manifolds with positive scalar curvature, Manuscripta Math. 28 (1979), no. 1-3, 159-183.
\item[] [33] M. Taylor Partial differential equations III: nonlinear equations, Appl. Math. Sci. 117, New York: Springer-Verlag, (1996).
\end{itemize}

Erwann Delay, Laboratoire d'analyse non linéaire et géométrie, Faculté des Sciences, 33 rue Louis Pasteur, 84000 Avignon, France
E-mail address: Erwann.Delay@univ-avignon.fr
URL: http://www.math.univ-avignon.fr/Delay
Lorenzo Mazzieri, SISSA - International School for Advanced Studies, via Beirut 2-4, I-34014 Trieste, Italy
E-mail address: mazzieri@sissa.it