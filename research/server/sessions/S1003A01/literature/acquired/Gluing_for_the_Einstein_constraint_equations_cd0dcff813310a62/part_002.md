---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Gluing for the Einstein constraint equations]

For the rest of the section, we extend the summation convention to all pairs of repeated indices (even if both are down). Since in Cartesian coordinates, $D R_{\dot{g}}(h)=h_{i j, i j}-h_{i i, j j}$, we see that by simple expansion of the scalar curvature term
$$\begin{aligned}
\int_{\mathscr{A}_{1}}\left(R\left(\bar{g}_{R}\right)-2 \kappa\left|\bar{E}_{R}\right|_{\bar{g}_{R}}^{2}\right) \mathrm{d} x & =\int_{\partial \mathscr{A}_{1}}\left(\left(\tilde{g}_{R}\right)_{i j, i}-\left(\tilde{g}_{R}\right)_{i i, j}\right) \stackrel{\circ}{v}^{j} \mathrm{~d} \stackrel{\circ}{\sigma}+O\left(R^{-2}\right) \\
& =R^{-1} \int_{\partial \mathscr{A}_{R}}\left(\left(\hat{g}_{R}\right)_{i j, i}-\left(\hat{g}_{R}\right)_{i i, j}\right) \stackrel{\circ}{v}^{j} \mathrm{~d} \stackrel{\circ}{\sigma}^{2}+O\left(R^{-2}\right) \\
& =R^{-1} 16 \pi(m-m(g))+O\left(R^{-2}\right) .
\end{aligned}$$
So the projection is to leading order controlled by the mass $m$ of the Reissner-Nordström exterior.
The projection onto the linear elements requires a bit more attention. For the metric $g$, we find that for any $r>r_{0}>1$,
$$\int_{\left\{r_{0} \leq|x| \leq r\right\}} x^{k}\left(g_{i j, i j}-g_{i i, j j}\right) \mathrm{d} x=\left(\int_{\{|x|=r\}}-\int_{\left\{|x|=r_{0}\right\}}\right)\left(x^{k}\left(g_{i j, i}-g_{i i, j}\right)-\left(\delta_{i}^{k} g_{i j}-\delta_{j}^{k} g_{i i}\right)\right) \dot{v}^{j} \mathrm{~d} \dot{\sigma} .$$
Note that in the last terms of the integral on the right, we could replace the terms of the form $g_{\ell m}$ with $g_{\ell m}-\delta_{\ell m}$. Moreover, using the constraint equations, the integrand $\left(g_{i j, i j}-g_{i i, j j}\right)=O\left(|x|^{-4}\right)$, and so the left hand side is $O(\log r)$.

If instead the above is evaluated at the Reissner-Nordström data, by using the asymptotic parity and the fact that the center of mass does not appear in the $|x|^{-1}$ term in the expansion, we can show that for $|c| \leq r / 2$ and for $m$ bounded, $\int_{\{|x| \geq r\}} x^{k}\left(\left(g_{\mathrm{RN}}\right)_{i j, i j}-\left(g_{\mathrm{RN}}\right)_{i i, j j}\right) \mathrm{d} x=O\left(r^{-1}\right)$, on the one hand, while on the other
$$\lim _{r \rightarrow \infty} \int_{\{|x|=r\}}\left(x^{k}\left(\left(g_{\mathrm{RN}}\right)_{i j, i}-\left(g_{\mathrm{RN}}\right)_{i i, j}\right)-\left(\delta_{i}^{k}\left(g_{\mathrm{RN}}\right)_{i j}-\delta_{j}^{k}\left(g_{\mathrm{RN}}\right)_{i i}\right)\right) \dot{v}^{j} \mathrm{~d} \delta^{\circ}=16 \pi m c^{k} .$$

Assembling all of this, noting that the rescaled exterior is a Reissner-Nordström with center $\tilde{c}=c R^{-1}$, we obtain
$$\begin{aligned}
\int_{\mathscr{A}_{1}} & x^{k}\left(R\left(\bar{g}_{R}\right)-2 \kappa\left|\bar{E}_{R}\right|_{\bar{g}_{R}}^{2}\right) \mathrm{d} x \\
= & \int_{\partial \mathscr{A}_{1}} x^{k}\left(\left(\tilde{g}_{R}\right)_{i j, i}-\left(\tilde{g}_{R}\right)_{i i, j}\right) \stackrel{\circ}{v}^{j} \mathrm{~d} \stackrel{\circ}{\sigma}+O\left(R^{-2}\right) \\
= & R^{-2} \int_{\{|x|=2 R\}}\left(x^{k}\left(\left(g_{\mathrm{RN}}\right)_{i j, i}-\left(g_{\mathrm{RN}}\right)_{i i, j}\right)-\left(\delta_{i}^{k}\left(g_{\mathrm{RN}}\right)_{i j}-\delta_{j}^{k}\left(g_{\mathrm{RN}}\right)_{i i}\right)\right) \stackrel{\circ}{v}^{j} \mathrm{~d} \stackrel{\circ}{\sigma} \\
& -R^{-2} \int_{\{|x|=R\}}\left(x^{k}\left(g_{i j, i}-g_{i i, j}\right)-\left(\delta_{i}^{k} g_{i j}-\delta_{j}^{k} g_{i i}\right)\right) \stackrel{\circ}{v}^{j} \mathrm{~d} \stackrel{\circ}{\sigma}+O\left(R^{-2}\right) \\
= & R^{-1}\left(16 \pi m \tilde{c}^{k}+O\left(\frac{\log R}{R}\right)\right)+O\left(R^{-2}\right)
\end{aligned}$$
Thus we get a map
$$(m, \tilde{c}) \mapsto \frac{R}{16 \pi} \int_{\mathscr{A}_{1}}(1, x)\left(R\left(\bar{g}_{R}\right)-2 \kappa\left|\bar{E}_{R}\right|_{\bar{g}_{R}}^{2}\right) \mathrm{d} x=(m-m(g)+\xi(m, \tilde{c}), m \tilde{c}+\Xi(m, \tilde{c})),$$
where $\xi(m, \tilde{c})=O\left(R^{-1}\right)$ and $\Xi(m, \tilde{c})=O(\log R / R)$. Moreover, the construction is continuous with respect to $m$ and $\tilde{c}$, and so $\xi$ and $\Xi$ are continuous; this is fairly straightforward but cumbersome to prove (see, e.g. [17, Section A.7]). A fixed-point or degree argument can finish the proof from here. For example, the function
$$F(m, \tilde{c})=\left(m(g)-\xi(m, \tilde{c}),-\frac{\Xi(m, \tilde{c})}{m(g)-\xi(m, \tilde{c})}\right),$$
is readily seen to map $\{(m, \tilde{c}):|m-m(g)| \leq|m(g)| / 2,|\tilde{c}| \leq 1 / 2\}$ to itself, and the Brouwer fixed point theorem can then be applied. The fixed point gives parameters that solve the problem.

We remark that we did not assume the original metric $g$ enjoyed enough parity symmetry to admit a well-defined center of mass. If this were the case, we could argue that the resulting center $c=R \tilde{c}$ is close to that of the original, cf. [22,23].

\subsection*{3.2. Further applications of deformation}

Suppose the starting data, say $\left(g_{0}, E_{0}\right)$, is such that $D \Psi_{\left(g_{0}, E_{0}\right)}^{*}$ admits only trivial kernel in $\Omega$. The same perturbative analysis above can be applied, the only difference is that since there is no kernel to deal with, we do not need the projected operator, and so the technique yields a localized deformation result: given a compactly contained subdomain of $\Omega$ and sufficiently small compactly supported $S$ and $\sigma$, say, there are $h$ and $X$ which smoothly extend by zero across $\partial \Omega$ with $\Psi\left(g_{0}+h, E_{0}+X\right)=\Psi\left(g_{0}, E_{0}\right)+(S, \sigma)$. Similar comments apply to scalar curvature deformation [22], as well as for the general constraints case [23], though in the latter case maintaining the dominant energy condition at the borderline is somewhat subtle [55].

As mentioned earlier, one can combine conformal gluing and localized gluing to obtain connected sum constructions leaving the original data intact outside the gluing neck [21,24,25]. The additional assumption needed, beyond any needed for the conformal gluing, is that the corresponding operator for the localized gluing problem has trivial kernel. If you have a sequence of solutions of the nonlinear problem (vacuum constraints, or a scalar curvature equation, say) which converges to a solution for which the linearized adjoint has trivial kernel in $\Omega$, then you can glue back in the original data inside some appropriate subdomain, and use the localized perturbations (unobstructed in this case) to reimpose the nonlinear equation.

For an interesting application combining localized deformations of constraint data with conformal deformations, consider an asymptotically flat metric $g$ with nonnegative scalar curvature $R(g)$, which is not static outside of some bounded region $\Omega \subset \mathbb{R}^{3}$ (in the sense that the adjoint $D R_{g}^{*}$ of the linearization of the scalar curvature has trivial kernel in the exterior $\mathbb{R}^{3} \backslash \bar{\Omega}$ ). It is possible using localized deformations to find a compactly contained domain $V \subset R^{3} \backslash \bar{\Omega}$ such that for $S$ compactly supported in $V$, and for $\varepsilon>0$ sufficiently small, there is a metric $\bar{g}_{\varepsilon}$ with $R\left(\bar{g}_{\varepsilon}\right)=R(g)+\varepsilon S$, and $\bar{g}_{\varepsilon}-g=O(\epsilon)$ is supported in $V$. If $S \geq 0$ and is nontrivial, one can then use an elementary conformal transformation to bring the ADM mass down while keeping the scalar curvature nonnegative, with conformal factor $u_{\varepsilon}>0$ which is one in a neighborhood of $\bar{\Omega}$ [57]. In terms of asymptotically flat extensions of a given region, then, this shows that unless the data outside the region were static in the above sense, there would be extensions with nonnegative scalar curvature and lower ADM mass, and hence in particular the original configuration does not minimize the Bartnik mass. To summarize, a localized deformation is used to bump the scalar curvature up (adding energy density) in a compact set outside the region $\bar{\Omega}$, which does not change the ADM mass, and then a conformal deformation removes some of this scalar curvature and in so doing brings down the ADM mass, leaving the original geometry of $\bar{\Omega}$ intact.

Similar considerations hold for the general (non-time-symmetric) case, though maintaining the dominant energy condition seems to require a modification of the constraints operator to have trivial kernel [55, 58]. An interpretation of the kernel elements for the modified operator, akin to that in [51], and has been established in the recent work [59] on constraint deformations and the dominant energy condition, with striking applications to the Bartnik mass.

Another application is the gluing of initial data to interpolate their scalar curvatures [60], or more generally interpolating ( $\mu, J$ ) from the constraints operator [55]. As an interesting example, one can glue initial data for a Kerr solution (including Schwarzschild) to a different Kerr solution across an annular region where the dominant energy condition can be maintained (see Remark after Theorem 1.4 in [55]).

Finally, we discussed earlier the use of the conformal method to achieve solutions with certain prescribed asymptotic behavior, with stability for the Einstein evolution in mind. Motivated by questions about the asymptotics posed in [16], the work [61] proceeds to seed the desired asymptotics, and then correct to solutions of the constraints, but in a different manner than that of [47, 48], in part employing variational methods of the kind used in [16,23].

\subsection*{3.3. Alternate approach to solving the projected problem}

We review the steps in the procedure shown above for gluing to an asymptotically flat model family. We start by patching initial data to a member of the model family, with the following parameters at our disposal: $R$ (measuring the scale), the exterior mass $m$ and center of mass $c$; for the Einstein-Maxwell constraints, we match the electric charge $Q$. For large enough $R$ the patched data is sufficiently close to flat, and we solve the constraints up to a finite-dimensional obstruction space. To accomplish this, we iterate linear corrections, in spaces with suitable decay at the boundary of the annulus. The procedure is controlled using basic elliptic estimates, both integral and pointwise, and with suitable weights. The integral estimates for the timesymmetric case are relatively straightforward, while the weighted Schauder estimates follow from the standard interior estimates and scaling. From here, a topological argument using the finite-dimensional space of parameters allows us to cover the cokernel and solve the constraints. Similar comments apply in the non-time-symmetric case.

The main first step, then, is how to solve the relevant linear equations with compact support. For $g=\dot{g}+h$ with $h$ small, the scalar curvature to leading order is governed by a divergence:
$$R(\stackrel{\circ}{g}+h)=D R_{\stackrel{\circ}{g}}(h)+\mathscr{Q}(h)=\operatorname{div}_{\stackrel{\circ}{g}} \operatorname{div}_{\mathscr{g}}\left(h-\left(\operatorname{tr}_{\mathscr{g}} h\right) \stackrel{\circ}{g}\right)+\mathscr{Q}(h),$$
where $\mathscr{Q}(h)$ is a combination with bounded coefficients of terms of components of $h \otimes \partial^{2} h$ and $\partial h \otimes \partial h$. A similar expansion holds for the constraints operator. At the linear level, then, solving for a compactly supported perturbation for the constraints map near $(\AA, 0)$ amounts to being able to solve suitable divergence equations with compact support.

Recent works [62, 63] have indeed developed this approach near the flat data (with an extension to data near hyperbolic data obtained in [64]). For instance, to solve a double divergence equation, the authors use a Bogovskii-type operator as follows. Let $\Omega \subset \mathbb{R}^{3}$ be an open set, which for simplicity we take to be convex, and containing an open ball $B$, and let $\eta \in C_{c}^{\infty}(B)$ with $\int_{\mathbb{R}^{3}} \eta(x) \mathrm{d} x=1$. Then for any $f \in C_{c}^{\infty}\left(\mathbb{R}^{n}\right)$ we define the tensor $S f$ to have Cartesian components
$$(S f)^{i j}(x)=\int_{\mathbb{R}^{3}}\left(\int_{|x-y|}^{\infty} \eta\left(r \frac{x-y}{|x-y|}+y\right) r^{2} \mathrm{~d} r\right) \frac{(x-y)^{i}(x-y)^{j}}{|x-y|^{3}} f(y) \mathrm{d} y .$$
If $f \in C_{c}^{\infty}(\Omega)$, then $S f$ is supported in $\Omega$ as well, and moreover, if $\int_{\Omega} f(x) \mathrm{d} x=0=\int_{\Omega} x^{k} f(x) \mathrm{d} x$, for $k \in\{1,2,3\}$, then $\operatorname{div}_{g} \operatorname{div}_{g}(S f)=f$. The integral conditions are of course readily seen to be the orthogonality of $f$ to the cokernel of the double divergence. One can furthermore use a straightforward finite patching argument to handle more general domains such as the annuli used in gluing constructions.

As a remark related to this and to the Einstein-Maxwell equations, we recall the well-known procedure for solving the divergence equation $\operatorname{div}_{g} X=f$, with $f$ and the solution $X$ compactly supported (see, e.g. [65, Section 1.3]). Of course we assume that $\int_{\mathbb{R}^{n}} f(x) \mathrm{d} x=0$. In one dimension this is straightforward, as $X(x)=\int_{-\infty}^{x} f(t) \mathrm{d} t$ satisfies the required conditions. We can proceed inductively. Suppose $f$ is compactly supported in $D=D_{n} \times I \subset \mathbb{R}^{n+1}$, where $D_{n}$ is an open rectangle in $\mathbb{R}^{n}$ and $I \subset \mathbb{R}$ is an open interval. For $x \in \mathbb{R}^{n}$, we let $F(x)=\int_{\mathbb{R}} f(x, t) \mathrm{d} t$. By assumption, then $\int_{\mathbb{R}^{n}} F(x) \mathrm{d} x=0$, so by induction, there are $Y^{1}, \ldots, Y^{n}$ supported in $D_{n}$ with
$\partial_{i} Y^{i}(x)=F(x)$. If $\theta$ is supported in $I$ with $\int_{\mathbb{R}} \theta(t) \mathrm{d} t=1$, we let $X^{i}\left(x, x^{n+1}\right)=Y^{i}(x) \theta\left(x^{n+1}\right)$ for $i \in\{1, \ldots, n\}$ and
$$X^{n+1}\left(x, x^{n+1}\right)=\int_{-\infty}^{x^{n+1}}(f(x, t)-\theta(t) F(x)) \mathrm{d} t$$
The vector field $X$ with components $X^{1}, \ldots, X^{n+1}$ is supported in $D$ and has divergence $f$.
Returning to the constraints, one would still need to solve the nonlinear projected problem, which is essentially done by an iteration scheme. That said, one major benefit of the Bogovskiitype operator is that regularity is maintained when the data is in appropriate Sobolev spaces, a question which arises when considering the natural regularity for initial data for the evolution problem. Moreover the method has been extended beyond the asymptotically flat regime to give an asymptotically hyperboloidal construction [64], and this is certainly intriguing since the asymptotically hyperboloidal case proves to be more challenging (for instance the conformal infinity is not a point as it is for the asymptotically Euclidean case), see for example [66-68]. The Bogovskii-type operator method has also been used for other localization results such as Carlotto-Schoen type gravitational shielding constructions [62]. Finally, one often wants to connect the solutions of the Einstein constraints to the spacetimes they determine, whether in theory or numerically. Numerical implementation of gluing constructions seems quite challenging, and though there have been a handful of works in this direction [69-72], alternative methods to do gluing constructions could prove useful if they are more readily implemented numerically. It is natural to wonder if the Bogovskii-type operator approach of [63] might be helpful in this direction, and likewise for the characteristic gluing constructions of [11] involving transport-elliptic differential equations, which are of a different character than the spacelike gluing.

\section*{4. Further applications to spacetimes}

As mentioned earlier, one of the early goals for the gluing construction was to create vacuum initial data which would evolve to a vacuum spacetime that is asymptotically simply in the sense of Penrose conformal compactification, a purely radiative spacetime. Since work of Friedrich [32] the following was known: if one could construct a family of solutions to the vacuum constraints with small mass tending to zero, each of which is Schwarzschild in a uniform neighborhood of spacelike infinity, then for members of the family with sufficiently small mass, the spacetime evolution would be an asymptotically simple vacuum spacetime. The result in [22] on its own did not quite give such a construction. The main issue, as one can see from (25), is that as the mass $m$ tends to zero, the projection onto the linear directions is on the order of $m c$, and so for small mass, the center of mass may need to grow larger to accommodate. To control the center, Chruściel and Delay [30] restrict to a family of parity-symmetric metrics, for which the center of mass in the construction can always be taken to vanish. In [31], we construct a larger family of solutions to the constraints with small masses and controlled centers, by using the second variation of the mass at the Euclidean data [73,74] to control the mass from below in terms of the center. With either approach, the gluing to Schwarzschild at infinity then finishes the initial data construction.

In a completely different direction, Li and Yu [75] construct vacuum initial data, free of trapped surfaces, whose evolution will contain a trapped surface (cf. [76]). Of note, the solution contains an interior region of Minkowskian data, while the exterior is an exterior of a space-time slice of a Kerr spacetime. The construction builds on the monumental work of Christodoulou on formation of trapped surfaces in vacuum [77], from data on null hypersurfaces; in particular, the construction in [75] uses data given at past null infinity.

While we do not have the space and time to discuss any details here, there is one feature of the proof that we want to note. The construction uses gluing to Kerr exterior as in [23], but in a regime where the limiting data is not Minkowksian, but Kerrian. As such, the cokernel has smaller dimension than at the flat data, so the gluing is not quite as obstructed. This has been observed in other places, such as in initial data constructions with positive cosmological constant [78] and in more recent work on multi-localized initial data [17]. In the latter work, the relevant approximate kernel is that of a Schwarzschild, which is one-dimensional (for non-zero mass). The motivation for the multi-localized initial data constructed in [17] comes from the nonlinear stability result of Anderson and Pasqualotto [79]. The template for the construction is the Brill-Lindquist metric (5), and we glue ends on around each of the punctures in the set $\mathfrak{p}$ to make initial data on $\mathbb{R}^{3}$. Of note is that we are able to handle certain configurations where $\mathfrak{p}$ is infinite, and in particular, we construct smooth metrics on $\mathbb{R}^{3}$ with zero scalar curvature and infinitely many minimal spheres, each of them exterior to all the others.

As remarked earlier, in recent years characteristic gluing has been developed in a series of papers by Aretakis, Czimek and Rodnianski; for an overview and further references, see [11]. For the characteristic initial value problem, one specifies certain free data on what will be two transversely intersecting null hypersurfaces in the vacuum spacetime, after which one can appeal to local well-posedness results for the characteristic initial value problem for the Einstein vacuum equation [80,81]. For the characteristic gluing problem, one seeks to glue data on two spheres along a null hypersurface. As with the spacelike case, the relevant equations that must be satisfied arise from the vacuum Einstein equation together with the fundamental compatibility equations for an embedding, in this case the compatibility coming from a double null foliation. The resulting equations for metric and curvature components are the null structure equations, of transport-elliptic character along either the ingoing or outgoing null hypersurface. As is noted in [11], there are obstructions to gluing data from two spheres, such as a monotonicity deriving from the Raychaudhuri equation.

There are a number of noteworthy applications of their technique, and we just mention a few. Their methods can recover the asymptotic gluing to Kerr as in [23], as well as localized gluing from [16], and without loss of decay in the transition region. In [82], the method is employed to achieve obstruction-free gluing. The asymptotic gluing construction along the lines of [22,23] glues initial data with certain energy-momenta to Kerr data with energy-momenta which is close to the starting one, as we say above, tuned to cover the linear obstruction from the approximate cokernel. A natural question is whether one can glue pieces from spacetimes whose parameters are not necessarily close, and results in this direction have been obtained in [82].

The characteristic gluing construction has been employed by Kehle and Unger [83] to perform a specific event horizon gluing in the context of the Einstein-Maxwell charged scalar field system, in spherical symmetry. As an upshot, they produce a counterexample to the third law of black hole thermodynamics.

\section*{5. Conclusion}

Gluing methods for constructing solutions of the Einstein constraint equations have garnered a number of noteworthy achievements. While more than twenty years have passed since the gluing results of [22] and [20], new techniques and applications are still being developed and continue to highlight the interplay between initial data results and the evolution problem.

\section*{Dedication}

This article is dedicated to Mme. Yvonne Choquet-Bruhat, for giving so much to so many of us for so many years. The memory of Yvonne that is emblazoned upon me comes from over twenty
years ago at a workshop in Cargèse, Corsica, marking the fiftieth anniversary of her landmark paper on the initial-value problem. Walking back to the seminar room with a colleague, we encountered Yvonne taking a bit of respite from the sunshine under a tree; while it was not an apple tree, what sprung to my imagination was the universe (or the spirit of Sir Isaac Newton) willing one to fall and land in the palm of her hand.

\section*{Declaration of interests}

The authors do not work for, advise, own shares in, or receive funds from any organization that could benefit from this article, and have declared no affiliations other than their research organizations.

\section*{Acknowledgments}

The author would like to thank Farhan Abedin, David A. Maxwell and Iva Stavrov Allen for their comments on a draft manuscript. The author is supported in part by the AMS-Simons Research Enhancement Grant for PUI Faculty.

\section*{References}
\begin{itemize}
\item[] [1] Y. Choquet-Bruhat, General Relativity and the Einstein Equations, Oxford Mathematical Monographs, Oxford University Press, Oxford, 2009, xxvi + 785 pages.
\item[] [2] Y. Choquet-Bruhat, "The Cauchy problem", in Gravitation: An Introduction to Current Research (L. Witten, ed.), John Wiley \& Sons, Inc., New York-London, 1962, p. 130-168.
\item[] [3] Y. Choquet-Bruhat, J. W. York Jr, "The Cauchy problem", in General Relativity and Gravitation (A. Held, ed.), Plenum Press, New York-London, 1980, p. 99-172.
\item[] [4] Y. Choquet-Bruhat, "Beginnings of the Cauchy problem for Einstein's field equations", Surv. Differ. Geom. 20 (2015), p. 1-16.
\item[] [5] Y. Fourès-Bruhat, "Théorème d'existence pour certains systèmes d'équations aux dérivées partielles non linéaires", Acta Math. 88 (1952), p. 141-225.
\item[] [6] J. W. York Jr, "Gravitational degrees of freedom and the initial-value problem", Phys. Rev. Lett. 26 (1971), p. 1656-1658.
\item[] [7] D. Maxwell, "Initial data in general relativity described by expansion, conformal deformation and drift", Comm. Anal. Geom. 29 (2021), no. 1, p. 207-281.
\item[] [8] A. Lichnerowicz, "L'intégration des équations de la gravitation relativiste et le problème des $n$ corps", J. Math. Pures Appl. 23 (1944), no. 9, p. 37-63.
\item[] [9] P. Hintz, "Gluing small black holes along timelike geodesics I: formal solution", preprint, 2023, https://arxiv.org/abs/ 2306.07409.
\item[] [10] P. Hintz, "Gluing small black holes into initial data sets", Commun. Math. Phys. 405 (2024), no. 5, article no. 114.
\item[] [11] S. Aretakis, S. Czimek, I. Rodnianski, "The characteristic gluing problem for the Einstein equations and applications", preprint, 2022, https://arxiv.org/abs/2107.02441.
\item[] [12] P. T. Chruściel, J. Corvino, J. Isenberg, "Initial data for the relativistic gravitational $N$-body problem", Class. Quantum Gravity 27 (2010), no. 22, p. 6.
\item[] [13] P. T. Chruściel, R. Mazzeo, "On "many-black-hole" vacuum spacetimes", Class. Quantum Gravity 20 (2003), no. 4, p. 729-754.
\item[] [14] P. T. Chruściel, J. Corvino, J. Isenberg, "Construction of $N$-body time-symmetric initial data sets in general relativity", in Complex Analysis and Dynamical Systems IV. Part 2, Contemporary Mathematics, vol. 554, American Mathematical Society, Providence, RI, 2011, p. 83-92.
\item[] [15] P. T. Chruściel, J. Corvino, J. Isenberg, "Construction of $N$-body initial data sets in general relativity", Commun. Math. Phys. 304 (2011), no. 3, p. 637-647.
\item[] [16] A. Carlotto, R. Schoen, "Localizing solutions of the Einstein constraint equations", Invent. Math. 205 (2016), no. 3, p. 559-615.
\item[] [17] J. Anderson, J. Corvino, F. Pasqualotto, "Multi-localized time-symmetric initial data for the Einstein vacuum equations", J. Reine Angew. Math. (Crelle's Journal) 808 (2024), p. 67-110.
\item[] [18] C. Racine, Le problème des $N$ corps dans la théorie de la relativité, Thèse, Gauthier-Villars, Paris, 1934, http://www. numdam.org/item/THESE_1934_158_1_0.pdf.
\end{itemize}
[19] G. Darmois, "Les équations de la gravitation einsteinienne", Mémor. Sci. Math. 25 (1927), article no. 58.
[20] J. Isenberg, R. Mazzeo, D. Pollack, "Gluing and wormholes for the Einstein constraint equations", Commun. Math. Phys. 231 (2002), no. 3, p. 529-568.
[21] P. T. Chruściel, E. Delay, "On mapping properties of the general relativistic constraints operator in weighted function spaces, with applications", Mém. Soc. Math. Fr. (N.S.) 94 (2003), p. vi + 103.
[22] J. Corvino, "Scalar curvature deformation and a gluing construction for the Einstein constraint equations", Commun. Math. Phys. 214 (2000), no. 1, p. 137-189.
[23] J. Corvino, R. M. Schoen, "On the asymptotics for the vacuum Einstein constraint equations", J. Differential Geom. 73 (2006), no. 2, p. 185-217.
[24] P. T. Chruściel, J. Isenberg, D. Pollack, "Initial data engineering", Commun. Math. Phys. 257 (2005), no. 1, p. 29-42.
[25] J. Corvino, M. Eichmair, P. Miao, "Deformation of scalar curvature and volume", Math. Ann. 357 (2013), no. 2, p. 551-584.
[26] L. Mazzieri, "Generalized gluing for the Einstein constraint equations", Calc. Var. Partial Differ. Equ. 34 (2009), no. 4, p. 453-473.
[27] E. Delay, L. Mazzieri, "Refined gluing for the vacuum Einstein constraint equations", Geom. Dedicata 173 (2014), p. 393-415.
[28] J. Isenberg, R. Mazzeo, D. Pollack, "On the topology of vacuum spacetimes", Ann. Henri Poincaré 4 (2003), no. 2, p. 369-383.
[29] I. Stavrov Allen, "A gluing construction regarding point particles in general relativity", Ann. Henri Poincaré 10 (2010), no. 8, p. 1437-1486.
[30] P. T. Chruściel, E. Delay, "Existence of non-trivial, vacuum, asymptotically simple spacetimes", Class. Quantum Gravity 19 (2002), no. 9, p. L71-L79.
[31] J. Corvino, "On the existence and stability of the Penrose compactification", Ann. Henri Poincaré 8 (2007), no. 3, p. 597-620.
[32] H. Friedrich, "On the existence of $n$-geodesically complete or future complete solutions of Einstein's field equations with smooth asymptotic structure", Commun. Math. Phys. 107 (1986), p. 587-609.
[33] R. Bartnik, "Quasi-spherical metrics and prescribed scalar curvature", J. Differential Geom. 37 (1993), no. 1, p. 31-71.
[34] J. Isenberg, D. Maxwell, "A phase space approach to the conformal construction of non-vacuum initial data sets in general relativity", preprint, 2021, https://arxiv.org/abs/2106.15027v2.
[35] D. R. Brill, R. W. Lindquist, "Interaction energy in geometrostatics", Phys. Rev. (2) 131 (1963), p. 471-476.
[36] C. Sormani, I. Stavrov Allen, "Geometrostatic manifolds of small ADM mass", Comm. Pure Appl. Math. 72 (2019), no. 6, p. 1243-1287.
[37] C. W. Misner, "The method of images in geometrostatics", Ann. Phys. 24 (1963), p. 102-117.
[38] Y. Fourès-Bruhat, "Sur l'intégration des équations de la relativité génŕale", J. Ration. Mech. Anal. 5 (1956), no. 6, p. 951-966.
[39] N. Ó. Murchadha, J. W. York Jr, "Existence and uniqueness of solutions of the Hamiltonian constraint of general relativity on compact manifolds", J. Math. Phys. 14 (1973), no. 11, p. 1151-1557.
[40] N. Ó. Murchadha, J. W. York Jr, "Initial-value problem of general relativity. I. General formulation and physical formulation", Phys. Rev. D 10 (1974), no. 2, p. 428-436.
[41] D. Maxwell, "The conformal method and the conformal thin-sandwich method are the same", Class. Quantum Gravity 31 (2014), no. 14, article no. 145006.
[42] R. M. Schoen, S.-T. Yau, "The energy and the linear momentum of space-times in general relativity", Commun. Math. Phys. 79 (1981), no. 1, p. 47-51.
[43] R. Schoen, S. T. Yau, "On the proof of the positive mass conjecture in general relativity", Commun. Math. Phys. 65 (1979), no. 1, p. 45-76.
[44] H. L. Bray, "Proof of the Riemannian Penrose inequality using the positive mass theorem", J. Differential Geom. 59 (2001), p. 177-267.
[45] M. Eichmair, L.-H. Huang, D. A. Lee, R. M. Schoen, "The spacetime positive mass theorem in dimensions less than eight", J. Eur. Math. Soc. 18 (2016), p. 83-121.
[46] L.-H. Huang, "On the center of mass of isolated systems with general asymptotics", Class. Quantum Gravity 26 (2009), no. 1, article no. 015012.
[47] A. J. Fang, J. Szeftel, A. Touati, "Initial data for Minkowski stability with arbitrary decay", preprint, 2024, https: //arxiv.org/abs/2401.14353.
[48] A. J. Fang, J. Szeftel, A. Touati, "Spacelike initial data for black hole stability", preprint, 2024, https://arxiv.org/abs/ 2405.02071.
[49] A. E. Fischer, J. E. Marsden, "Deformations of the scalar curvature", Duke Math. J. 42 (1975), no. 3, p. 519-547.
[50] A. E. Fischer, J. E. Marsden, "Linearization stability of the Einstein equations", Bull. Am. Meteorol. Soc. 79 (1973), p. 997-1003.
[51] V. Moncrief, "Spacetime symmetries and linearization of the Einstein equations I", J. Math. Phys. 16 (1975), p. 493-498.
[52] J. Isenberg, D. Maxwell, D. Pollack, "A gluing construction for non-vacuum solutions of the Einstein constraint equations", Adv. Theor. Math. Phys. 9 (2005), no. 1, p. 129-172.
[53] L. Bieri, P. T. Chruściel, "Future-complete null hypersurfaces, interior gluing and the Trautman-Bondi mass", in Nonlinear Analysis in Geometry and Applied Mathematics (L. Bieri, P. T. Chruściel, S.-T. Yau, eds.), Harvard University Center of Mathematical Sciences and Applications Series in Mathematics, vol. 1, International Press, Somerville, MA, 2017, p. 1-31.
[54] P. T. Chruściel, "Long time existence from interior gluing", Class. Quantum Gravity 34 (2017), no. 14, article no. 145016.
[55] J. Corvino, L.-H. Huang, "Localized deformation for initial data sets with the dominant energy condition", Calc. Var. Partial Differ. Equ. 59 (2020), no. 1, article no. 42.
[56] A. Douglis, L. Nirenberg, "Interior estimates for elliptic systems of partial differential equations", Comm. Pure Appl. Math. 8 (1955), p. 503-538.
[57] J. Corvino, "A note on the Bartnik mass", in Nonlinear Analysis in Geometry and Applied Mathematics (L. Bieri, P. T. Chruściel, S.-T. Yau, eds.), Harvard University Center of Mathematical Sciences and Applications Series in Mathematics, vol. 1, International Press, Somerville, MA, 2017, p. 49-75.
[58] J. Corvino, "A short note on the Bartnik mass", Pure Appl. Math. Q. 15 (2019), no. 3, p. 827-838.
[59] L.-H. Huang, D. A. Lee, "Bartnik mass minimizing initial data sets and improvability of the dominant energy scalar", J. Differential Geom. 126 (2024), no. 2, p. 741-800.
[60] E. Delay, "Localized gluing of Riemannian metrics in interpolating their scalar curvature", Differ. Geom. Appl. 29 (2011), no. 3, p. 433-439.
[61] P. G. LeFloch, T.-C. Nguyen, "The seed-to-solution method for the Einstein constraints and the asymptotic localization problem", J. Funct. Anal. 285 (2023), no. 9, article no. 110106.
[62] Y. Mao, Z. Tao, "Localized initial data for Einstein equations", preprint, 2022, https://arxiv.org/abs/2210.09437.
[63] Y. Mao, S.-J. Oh, Z. Tao, "Initial data gluing in the asymptotically flat regime via solution operators with prescribed support properties", preprint, 2023, https://arxiv.org/abs/2308.13031.
[64] P. T. Chruściel, A. Cogo, A. Nützi, "A Bogovskiǐ-type operator for Corvino-Schoen hyperbolic gluing", preprint, 2024, https://arxiv.org/abs/2409.07502.
[65] L. Nirenberg, in Topics in Nonlinear Functional Analysis (Chapter 6 by E. Zehnder. Notes by R. A. Artino. Revised reprint of the 1974 original), Courant Lecture Notes in Mathematics, vol. 6, New York University, Courant Institute of Mathematical Sciences, New York; American Mathematical Society, Providence, RI, 2001, p. xii + 145.
[66] P. T. Chruściel, E. Delay, "Gluing constructions for asymptotically hyperbolic manifolds with constant scalar curvature", Comm. Anal. Geom. 17 (2009), no. 2, p. 343-381.
[67] J. Isenberg, J. M. Lee, I. Stavrov Allen, "Asymptotic gluing of asymptotically hyperbolic solutions to the Einstein constraint equations", Ann. Henri Poincaré 11 (2010), no. 5, p. 881-927.
[68] P. T. Allen, J. Isenberg, J. M. Lee, I. Stavrov Allen, "Asymptotic gluing of shear-free hyperboloidal initial data sets", Ann. Henri Poincaré 22 (2021), no. 3, p. 771-819.
[69] D. Giulini, G. Holzegel, "Corvino's construction using Brill waves", preprint, 2005, https://arxiv.org/abs/gr-qc/ 0508070.
[70] G. Doulis, O. Rinne, "Numerical construction of initial data for Einstein's equations with static extensions to spacelike infinity", Class. Quantum Gravity 33 (2016), no. 7, article no. 075014.
[71] B. Daszuta, J. Frauendiener, "Numerical initial data deformation exploiting a gluing construction: I. Exterior asymptotic Schwarzschild", Class. Quantum Gravity 36 (2019), no. 18, article no. 185008.
[72] D. Pook-Kolb, D. Giulini, "Numerical approach for Corvino-type gluing of Brill-Lindquist initial data", Class. Quantum Gravity 36 (2019), no. 4, article no. 045011.
[73] Y. Choquet-Bruhat, J. E. Marsden, "Solution of the local mass problem in general relativity", Commun. Math. Phys. 51 (1976), no. 3, p. 283-296.
[74] D. R. Brill, S. Deser, "Variational methods and positive energy in general relativity", Ann. Phys. 50 (1968), p. 548-570.
[75] J. Li, P. Yu, "Construction of Cauchy data of vacuum Einstein field equations evolving to black holes", Ann. Math. (2) 181 (2015), no. 2, p. 699-768.
[76] J. Li, H. Mei, "A construction of collapsing spacetimes in vacuum", Commun. Math. Phys. 378 (2020), no. 2, p. 1343-1389.
[77] D. Christodoulou, The Formation of Black Holes in General Relativity, EMS Monographs in Mathematics, European Mathematical Society (EMS), Zürich, 2009, x+589 pages.
[78] P. T. Chruściel, D. Pollack, "Singular Yamabe metrics and initial data with exactly Kottler-Schwarzschild-de Sitter ends", Ann. Henri Poincaré 9 (2008), no. 4, p. 639-654.
[79] J. Anderson, F. Pasqualotto, "Global stability for nonlinear wave equations with multi-localized initial data", Ann. PDE 8 (2022), no. 2, article no. 19.
\begin{itemize}
\item[] [80] A. D. Rendall, "Reduction of the characteristic initial value problem to the Cauchy problem and its application to the Einstein equations", Proc. R. Soc. Lond. A 427 (1990), no. 1872, p. 221-239.
\item[] [81] J. Luk, "On the local existence for the characteristic initial value problem in general relativity", Int. Math. Res. Not. IMRN 2012 (2012), no. 20, p. 4625-4678.
\item[] [82] S. Czimek, I. Rodnianski, "Obstruction-free gluing for the Einstein equations", preprint, 2022, https://arxiv.org/abs/ 2210.09663.
\item[] [83] C. Kehle, R. Unger, "Gravitational collapse to extremal black holes and the third law of black hole thermodynamics", preprint, 2022, https://arxiv.org/abs/2211.15742.
\end{itemize}