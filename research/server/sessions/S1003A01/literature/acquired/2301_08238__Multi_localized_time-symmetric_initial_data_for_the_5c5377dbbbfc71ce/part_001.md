---
retention_scope: session
part: 1
total_parts: 3
---

[Part 1/3 of: [2301.08238] Multi–localized time-symmetric initial data for the Einstein vacuum equations]

---
source_file: 2301_08238.pdf
converter: mathpix
format: mmd
---

\title{
MULTI-LOCALIZED TIME-SYMMETRIC INITIAL DATA FOR THE EINSTEIN VACUUM EQUATIONS
}

\author{
JOHN ANDERSON, JUSTIN CORVINO, FEDERICO PASQUALOTTO
}

\begin{abstract}
We construct a class of time-symmetric initial data sets for the Einstein vacuum equation modeling elementary configurations of multiple "almost isolated" systems. Each such initial data set consists of a collection of several localized sources of gravitational radiation, and lies in a family of data sets which is closed under scaling out the distances between the systems by arbitrarily large amounts. This class contains data sets which are not asymptotically flat, but to which nonetheless a finite ADM mass can be ascribed. The construction proceeds by a gluing scheme using the Brill-Lindquist metric as a template. Such initial data are motivated in part by a desire to understand the dynamical interaction of distant systems in the context of general relativity. As a by-product of the construction, we produce complete, scalar-flat initial data with trivial topology and infinitely many minimal spheres, as well as initial data with infinitely many Einstein-Rosen bridges.
\end{abstract}

\section*{Contents}
1. Introduction ..... 2
1.1. Statements ..... 3
1.2. Motivation ..... 5
1.3. $N$-body initial data sets ..... 6
1.4. Description of the proof ..... 7
1.5. Outline of the paper ..... 7
1.6. Acknowledgements ..... 8
2. Proof of Theorem 1.1 ..... 8
2.1. Preliminaries ..... 8
2.2. The nonlinear projected problem ..... 8
2.3. Proof of Theorem 1.1 ..... 9
3. Brill-Lindquist estimates ..... 10
4. Proof of Theorem 1.3 ..... 13
5. Vacuum initial data sets with infinitely many minimal spheres ..... 17
6. On the total mass ..... 21
6.1. On the Hamiltonian ..... 24
Appendix A. On the proof of Proposition 2.1 ..... 27
References ..... 39

\footnotetext{
2010 Mathematics Subject Classification. Primary 53C21, 83C99.
}

\section*{1. Introduction}

In this paper, we construct families of initial data sets for the Einstein vacuum equation. These data sets represent configurations of almost isolated and localized sources of gravitational radiation. The data we construct are motivated in part by studying the asymptotic stability of Minkowski spacetime relative to initial data perturbations living in these classes (see Section 1.2).

We shall focus on constructing time-symmetric initial data sets $(M, g)$, in which case the vacuum constraint equations reduce to the condition that the metric $g$ have vanishing scalar curvature. The constructions we consider are based on Brill-Lindquist metrics (see [6], cf. [31, 34]). These metrics are constructed by considering a (finite or countably infinite) sequence $\mathfrak{p}$ of distinct points $p_{i}$ in $\mathbb{R}^{3}$ and a corresponding sequence $\mathfrak{m}$ of positive numbers $m_{i}$ meant to represent masses. The Brill-Lindquist metric associated to these points and masses is then
$$\left(g_{B L}^{\mathfrak{m}, \mathfrak{p}}\right)_{i j}(x)=\left(1+\sum_{k} \frac{m_{k}}{2\left|x-p_{k}\right|}\right)^{4} \delta_{i j},$$
where $\left|x-p_{k}\right|$ denotes the Euclidean distance from the point $p_{k}$. We assume the series converges uniformly on compact subsets of $\mathbb{R}^{3} \backslash \mathfrak{p}$, so that it in fact defines a positive harmonic function here. The Brill-Lindquist metric is conformal to the Euclidean (flat) metric, and as the formula for the scalar curvature under a conformal change gives $R(g)=-8 u^{-5} \Delta u$ for $g_{i j}=u^{4} \delta_{i j}$, we have that the Brill-Lindquist metric has vanishing scalar curvature on $\mathbb{R}^{3} \backslash \mathfrak{p}$.

The main goal of this paper is to modify this metric locally near each of the points $p_{i}$ to yield a smooth metric with vanishing scalar curvature on $\mathbb{R}^{3}$, and we employ a gluing construction to accomplish this. Because we are interested in perturbations of the trivial initial data set $\left(\mathbb{R}^{3}, g_{i j}=\delta_{i j}\right)$, the masses $m_{i}$ will be taken to be small, and for a given $k \in \mathbb{Z}_{+}$, the modifications near the points $p_{i}$ will ensure that the new metric is $C^{k}$-close to the Euclidean metric. It is important to remark that given a suitable mass sequence $\mathfrak{m}$, we do not need to impose any symmetry requirements on the sequence of points $\mathfrak{p}$, only that they are at a sufficiently large distance from each other. Thus, we are constructing classes of $N$-body data sets, where the number $N$ is at most countable, and which can be construed as representing a sum of roughly spherically symmetric perturbations which are localized near distinct points.

In practice, we will first prove a basic gluing statement in the vicinity of a Schwarzschild metric (Theorem 1.1). We are then going to use this basic gluing construction to build examples in Theorem 1.3 of time-symmetric vacuum initial data sets on $\mathbb{R}^{3}$ obtained by filling in suitably chosen Brill-Lindquist metrics $g_{B L}^{\mathfrak{m}, \mathfrak{c}}$ with what we construe as "localized perturbations" of small mass $m_{i}$ near $c_{i}$. The theorem focuses on $\mathfrak{m}$ countably infinite, whereas the construction works in the finite case, as noted in Corollary 1.4. The construction applies for $\|\mathfrak{m}\|_{\ell^{\infty}}$ suitably small, and so the results include data sets as follows:
\begin{itemize}
\item[(1)] We will construct initial data sets with an arbitrary finite number $N$ of localized perturbations. In this case, each such initial data set is asymp-totically flat (albeit non-uniformly in the separation between the masses), with ADM mass $\sum_{i=1}^{N} m_{i}$. By increasing the number of localized pieces, we can achieve arbitrarily large ADM mass (see Remark 1.6).
\end{itemize}
\begin{itemize}
\item[(2)] If $\mathfrak{m} \in \ell^{1}$ with $\|\mathfrak{m}\|_{\ell^{\infty}}$ is sufficiently small, the constuction will yield data with a countably infinite number of localized perturbations whose mass sequence $\mathfrak{m}=\left(m_{i}\right)_{i \in \mathbb{Z}_{+}}$, with each $m_{i}>0$, has finite sum $\sum_{i=1}^{\infty} m_{i}<\infty$. There are data sets in this class with arbitrarily large $\|\mathfrak{m}\|_{\ell^{1}}$.
\item[(3)] If $\mathfrak{m} \in \ell^{\infty} \backslash \ell^{1}$ with $\|\mathfrak{m}\|_{\ell^{\infty}}$ sufficiently small, the construction will produce data with $\|\mathfrak{m}\|_{\ell^{1}}=\infty$. This includes cases in which $\sum_{i=1}^{\infty} m_{i}=\infty$, but just barely so, in the sense that $\sum_{i=1}^{\infty} \frac{m_{i}}{i^{\delta}}<\infty$ for some small $\delta>0$. In this case the resulting data is not asymptotically flat (see Section 6).
\end{itemize}

In the second case, it is not clear from our construction whether any such data sets are asymptotically flat, though certainly some data sets in this class are not asymptotically flat. As we will see, to make the data asymptotically flat would require choosing the masses for perturbations centered at large $\left|c_{i}\right|$ correspondingly small; that in turn affects a smallness condition in Theorem 1.1, which may then require the centers to be moved further apart, and it is thus not clear whether the argument can close. In any case, in Section 6, we argue that $\|\mathfrak{m}\|_{\ell^{1}}$ may provide a suitable notion of mass for the data sets we construct.

These constructions are perhaps intriguing because they give initial data sets which are (i) far from symmetric, (ii) not necessarily asymptotically flat, (iii) have arbitrarily large (or even infinite) $\|\mathfrak{m}\|_{\ell^{1}}$, but which nonetheless still seem reasonable as perturbations relative to which Minkowski spacetime will be stable as a solution to the Einstein vacuum equations. Indeed, the motivation for these constructions comes from the study of asymptotic stability for the initial value problem, as we describe in Section 1.2. As a consequence of the construction, we also show the existence of complete metrics with vanishing scalar curvature and with infinitely many minimal spheres.

We now provide precise statements of our results. The constructions extend mutatis mutandis to all $n \geq 3$, but for clarity of exposition, we give the statements and proofs for the case $n=3$, as the modifications for higher dimensions should be readily apparent.
1.1. Statements. For $m>0$, we let $g_{S}^{m}$ be the Schwarzschild metric in isotropic coordinates, defined on $\mathbb{R}^{3} \backslash\{0\}$ as follows:
$$\left(g_{S}^{m}\right)_{i j}(x)=\left(1+\frac{m}{2|x|}\right)^{4} \delta_{i j} .$$

We will work locally around each point in $\mathfrak{p}$, using the following general gluing statement.

Theorem 1.1. Let $\Omega=\left\{x \in \mathbb{R}^{3}: 1<|x|<2\right\}, \Omega_{\text {int }}:=\left\{x \in \mathbb{R}^{3}: 1<|x|<9 / 8\right\}$, $\Omega_{\text {ext }}:=\left\{x \in \mathbb{R}^{3}: 15 / 8<|x|<2\right\}$. Given $2 \leq N_{0} \in \mathbb{Z}_{+}$and $m>0$, and given $\varepsilon>0$, there exists a $\delta=\delta\left(m, \varepsilon, N_{0}\right)$ such that the following holds true. Consider a smooth metric $g_{\mathrm{ext}}$ defined on $\Omega$, with the following properties:
\begin{itemize}
\item[(i)] $g_{\text {ext }}$ has vanishing scalar curvature,
\item[(ii)] for all $x \in \Omega$, and all multi-indices $I$ with $0 \leq|I| \leq N_{0}+3$, we have
\end{itemize}
$$\left|\partial_{x}^{I}\left(\left(g_{\text {ext }}\right)_{i j}(x)-\left(g_{S}^{m}\right)_{i j}(x)\right)\right|<\delta .$$
Then there exists a metric $\widehat{g} \in \mathcal{C}^{N_{0}}(\Omega)$ and a number $\widehat{m}$, with $|m-\widehat{m}|<\min (m / 2, \varepsilon)$, such that the following properties hold true:
\begin{itemize}
\item[(1)] $\widehat{g}$ has vanishing scalar curvature,
\end{itemize}
\begin{itemize}
\item[(2)] $\widehat{g}=g_{S}^{\widehat{m}}$ for all $x \in \Omega_{\mathrm{int}}$,
\item[(3)] $\widehat{g}=g_{\mathrm{ext}}$ for all $x \in \Omega_{\mathrm{ext}}$,
\item[(4)] for all $x \in \Omega$, and all multi-indices $I$ with $0 \leq|I| \leq N_{0}$, we have
\end{itemize}
$$\left|\partial_{x}^{I}\left(\widehat{g}_{i j}(x)-\left(g_{S}^{\widehat{m}}\right)_{i j}(x)\right)\right|<\varepsilon .$$
Remark 1.2. We can clearly replace $g_{S}^{\widehat{m}}$ in the preceding estimate with $g_{S}^{m}$ or $g_{\text {ext }}$, since all these metrics can be made close. Furthermore, as we will recall later, the required assumption (1.2) can be stated as a smallness condition on $\left(g_{\text {ext }}-g_{S}^{m}\right)$ in $C^{N_{0}+2, \alpha}(\Omega)$, and the resulting estimate 1.3 on $\left(\widehat{g}-g_{S}^{\widehat{m}}\right)$ can be given in $C^{N_{0}, \alpha}(\Omega)$. For related extension statements for initial data sets, compare [13, Section 8.6].

As an application, we obtain the following statement concerning the existence of initial data sets with an arbitrarily large number of localized pieces.

Theorem 1.3. Let $N_{0} \in \mathbb{Z}_{+}$and $\varepsilon>0$. There exists $C>0$ and $0<\varepsilon_{0}<C^{-1} \varepsilon$ such that the following holds. For any sequence $\mathfrak{m}:=\left(m_{i}\right)_{i \in \mathbb{Z}_{+}}$such that for all $i \in$ $\mathbb{Z}_{+}, 0<m_{i} \leq \varepsilon_{0}$, there is a sequence $\mathfrak{p}=\left(p_{i}\right)_{i \in \mathbb{Z}_{+}}$of distinct points in $\mathbb{R}^{3}$, so that, for all $\lambda \geq 1$, there exists a complete smooth metric $g$ on $\mathbb{R}^{3}$ with vanishing scalar curvature and the following properties: for all $x \in \mathbb{R}^{3} \backslash \bigcup_{k \in \mathbb{Z}_{+}}\left\{x:\left|x-\lambda p_{k}\right| \leq 2\right\}$,
$$g_{i j}(x)=\left(1+\sum_{\ell \in \mathbb{Z}_{+}} \frac{m_{\ell}}{2\left|x-\lambda p_{\ell}\right|}\right)^{4} \delta_{i j},$$
while for all $k \in \mathbb{Z}_{+}$, and for all $x$ with $\left|x-\lambda p_{k}\right| \leq 2$, and for all multi-indices $I$ with $0 \leq|I| \leq N_{0},\left|\partial_{x}^{I}\left(g_{i j}(x)-\delta_{i j}\right)\right| \leq C m_{k}<\varepsilon$.

We make a few remarks about this statement.
\begin{itemize}
\item[-] This theorem states that we can construct data sets which look like localized perturbations around the points $c_{k}=\lambda p_{k}$.
\item[-] The dependence of the points $\mathfrak{p}$ on the masses $\mathfrak{m}$ derives from two considerations: (i) to ensure that the series defining the conformal factor will converge uniformly, and (ii) so that around each $\lambda p_{k}$, the metric in (1.4) is an admissible $g_{\text {ext }}$ to which we can apply Theorem 1.1.
\item[-] The parameter $\lambda$ in the statement reflects the fact that set of admissible choices of $\mathfrak{p}$ is closed under a rescaling of the location of the points by a factor $\lambda \geq 1$. This is important for future applications to the dynamics arising from these data sets because we want uniform estimates as the masses get farther apart.
\end{itemize}

From the proof of Theorem 1.3 and the calculations in Section 3, the following corollary will follow, yielding time-symmetric data containing a finite number $N$ localized perturbations about specified centers.

Corollary 1.4. Let $N_{0} \in \mathbb{Z}_{+}$. For any $\varepsilon>0$, there is a $\mu>0$ such that for any $N \in \mathbb{Z}_{+}$and any positive numbers $m_{1}, \ldots, m_{N}$ with $\max _{i \leq N} m_{i} \leq \mu$, there is a $\sigma>0$ so that for any $c_{1}, \ldots, c_{N} \in \mathbb{R}^{3}$ with $\min _{i \neq j}\left|c_{i}-c_{j}\right| \geq \sigma$, there is a smooth metric $g$ with vanishing scalar curvature on $\mathbb{R}^{3}$ with the following properties: on $\mathbb{R}^{3} \backslash \bigcup_{j \leq N}\left\{x:\left|x-c_{j}\right| \leq 2\right\}, g_{i j}(x)=\left(1+\sum_{k \leq N} \frac{m_{k}}{2\left|x-c_{k}\right|}\right)^{4} \delta_{i j}$, while for all $x$ in the set $\bigcup_{j \leq N}\left\{x:\left|x-c_{j}\right| \leq 2\right\}$, and all multi-indices $I$ with $0 \leq|I| \leq N_{0}$, $\left|\partial_{x}^{I}\left(g_{i j}(x)-\delta_{i j}\right)\right|<\varepsilon$.

Remark 1.5. We emphasize that we can fix masses $m_{1}, \ldots, m_{N}$ each of size at most $\mu$, and then the construction works with those same masses, for all choices of centers $c_{1}, \ldots, c_{N}$ with $\min _{i \neq j}\left|c_{i}-c_{j}\right|$ sufficiently large: each localized perturbation retains the same "strength" even if they are separated by a large distance.

Remark 1.6. By letting $\frac{\mu}{N^{\delta}} \leq m_{i} \leq \mu$ for $1 \leq i \leq N$ and for some $0<\delta<1$, for example, it follows from the corollary that there exist such configurations with $\sum_{i \leq N} m_{i}$ arbitrarily large.

The following is a direct corollary of the estimates in Section 3 along with Theorem 1.1. The Riemannian manifold $(\widehat{M}, \widehat{g})$ can be construed as vacuum initial data with infinitely many Einstein-Rosen bridges (see also [31] where an arbitrary finite number of Einstein-Rosen bridges are constructed).

Corollary 1.7. For any sequence $\mathfrak{m}$ with each $m_{i}>0$, there is a sequence $\mathfrak{p}$ as above such that for any $\lambda \geq 1$ and with $\mathfrak{c}=\lambda \mathfrak{p}$, there is a complete smooth metric $g$ on $\mathbb{R}^{3} \backslash \mathfrak{c}$ with vanishing scalar curvature, with $g=g_{B L}^{\mathfrak{m}, \mathfrak{c}}$ outside $\bigcup_{j \in \mathbb{Z}_{+}}\left\{x:\left|x-c_{j}\right| \leq 2\right\}$, while for $0<\left|x_{k}-c_{k}\right| \leq 1, g_{i j}(x)=\left(1+\frac{\widehat{m}_{k}}{2\left|x-c_{k}\right|}\right)^{4} \delta_{i j}=:\left(g_{S}^{\widehat{m}_{k}, p_{k}}\right)_{i j}(x)$, where $m_{k} / 2 \leq \widehat{m}_{k} \leq 3 m_{k} / 2$ for all $k \in \mathbb{Z}_{+}$. If $m_{k} \leq 4 / 3$, then the Schwarzschild end around $c_{k}$ includes the minimal sphere (horizon) $\Sigma_{k}:=\left\{x:\left|x-c_{k}\right|=\frac{\widehat{m}_{k}}{2}\right\}$.

By doubling $\left(\mathbb{R}^{3} \backslash \bigcup_{k \in \mathbb{Z}_{+}}\left\{x:\left|x-c_{k}\right| \leq \frac{\widehat{m}_{k}}{2}\right\}, g\right)$ over the totally geodesic boundary $\Sigma:=\bigcup_{k \in \mathbb{Z}_{+}} \Sigma_{k}$, we obtain a complete smooth Riemannian manifold $(\widehat{M}, \widehat{g})$ with vanishing scalar curvature.

The manifolds in this corollary have infinite topology, whereas with a bit more work, which we carry out in Section 5, we obtain the following result.

Proposition 1.8. There are complete smooth metrics on $\mathbb{R}^{3}$ with vanishing scalar curvature and infinitely many minimal spheres.
1.2. Motivation. In the context of the Einstein vacuum equation, an initial data set consists of a three-dimensional Riemannian manifold $(M, g)$ and a symmetric two-tensor field $K$ along $M$. Because $K$ will end up being the second fundamental form of an embedding of $(M, g)$ into a vacuum spacetime, the Gauss and Codazzi equations tell us that $g$ and $K$ cannot be chosen freely, but must satisfy certain compatibility conditions, the Einstein constraint equations. Under these constraints, the work of Choquet-Bruhat and Geroch (see [22] and [8]) guarantees the existence of a $3+1$-dimensional Lorentzian manifold $(\bar{M}, \bar{g})$ such that $(M, g)$ embeds isometrically in $\bar{M}$ as a Cauchy hypersurface with $K$ as its second fundamental form (see [32]). The properties of solutions of the Einstein constraint equations, including techniques such as the conformal method to construct solutions, have been the focus of intense study in mathematical physics and geometric analysis (see, for example, [4, 23] and references therein).

The class of data we construct is motivated by a desire to study the stability of the Minkowski spacetime (the trivial solution of the Einstein vacuum equation) relative to perturbations which are localized near several points separated by large distances. In the monumental work [9], Christodoulou-Klainerman showed that, relative to sufficiently small perturbations localized near a single point, the trivial solution is globally asymptotically stable. This means that the vacuum spacetimes arising from all such initial data sets do not form black holes, and in fact asymptotically
converge back to flat Minkowski spacetime in an appropriate sense by radiating away gravitational energy. The goal is to show that something similar happens in the context of these perturbations localized near several points, and in fact to show that the perturbations "decouple" from each other as they are taken farther and farther apart. This would allow us to probe, in the simplest setting, the interaction between several nearly isolated systems in the context of general relativity. These kinds of results also bring us closer to proving asymptotic stability for quasilinear equations in translation-invariant function spaces.

For the model case of systems of quasilinear wave equations satisfying Klainerman's [25] null condition (which models nonlinear structure found in the Einstein vacuum equation in an appropriate gauge), these kinds of statements were shown in [1]. The data there were comprised of a sum of roughly spherically symmetric functions supported near $N$ points. The main analytical difficulty arises from the fact that norms measuring the size of perturbations usually have radial weights away from some chosen center. These norms grow polynomially in the distance between the points, and thus, it is the large distance limit which we are interested in understanding. Moreover, since the analysis focused on systems of nonlinear wave equations, there was no need to construct appropriate classes of initial data. The data from [1] corresponds closely to one of the classes of data from Theorem 1.3 Thus, the main results of this paper construct data which are somewhat analogous to the ones considered in [1], and also provide some generalizations which may be interesting to consider in the context of asymptotic stability.
1.3 ✓-body initial data sets. We now compare the classes of data sets we construct with other $N$-body initial data set constructions. We focus on versions of statements involving a single end and vacuum data, as this is the case most closely related to the present work.

In [12, 13], Chruściel-Delay construct initial data sets containing any finite number of disconnected regions, in each of which the data agrees with that from a suitably chosen Schwarzschild or Kerr black hole. The work [14] of Chruściel-Mazzeo then proves that in the vacuum spacetime development of suitable members of the constructed family of initial data, the intersection of certain Cauchy hypersurfaces with the complement of the past of future null infinity has multiple connected components, i.e. these developments represent multiple black hole spacetimes. The works [11, 10] of Chruściel-Corvino-Isenberg employ similar gluing constructions to produce vacuum initial data sets with disconnected regions from any finite number of solutions of the constraints, allowing more general configurations than those above. In all these constructions, outside of a compact set, the solutions are given by initial data for a Kerr metric (reducing to Schwarzschild when time-symmetric).

A strikingly different configuration is produced in the work [7] of Carlotto-Schoen, which constructs $N$-body data sets glued inside any finite number of conical regions in $\mathbb{R}^{3}$. Outside of these cones, the metrics can be flat. Because of finite speed of propagation, these gravitational disturbances will not interact for some (potentially large) time, while the spacetime will contain a (potentially large) region isometric to a region in Minkowski spacetime. These kinds of data sets have also been constructed recently using other techniques. The work [2] of Aretakis-Czimek-Rodnianski employs characteristic gluing, while the work [28] of Mao-Tao constructs particular fundamental solutions to the linearized scalar curvature equation.

In contrast, the data sets constructed here are cooked up to look like sums of roughly spherically symmetric pieces centered at different points. In the spirit of [1], we are also interested in having constructions that are uniform as the separation between the points becomes infinite. Thus, the Brill-Lindquist metrics are natural template candidates to obtain the desired properties.

We now briefly comment on the proof strategy for the main gluing constructions in Theorem 1.1 and Theorem 1.3
1.4. Description of the proof. We use the kind of gluing construction originating in [15] (see also [20, 13] for the non-time-symmetric case).

We first focus on the proof of Theorem 1.1. We consider a smooth combination of $g_{\text {ext }}$ and $g_{S}^{\widetilde{m}}$ :
$$\widetilde{g}:=(1-\psi) g_{S}^{\widetilde{m}}+\psi g_{\mathrm{ext}},$$
where $\psi$ is a radial function which transitions from 0 to 1 in an annulus compactly contained in $\Omega=\left\{x \in \mathbb{R}^{3}: 1<|x|<2\right\}$, and we think of $\widetilde{m}$ as close to $m$.

The core of the argument is a Lyapunov-Schmidt reduction. We linearize the scalar curvature of $\widetilde{g}$ around $g_{S}^{m}$, and we consider the kernel of its formal adjoint $L_{g_{S}^{m}}^{*}$. This kernel is one-dimensional, spanned by a radial function $f^{m}$. It then follows (Proposition 2.1 that there exists a smooth tensor $h(\widetilde{g})$ supported on $\bar{\Omega}$ for which $\widetilde{g}+h(\widetilde{g})$ is a metric with
$$R(\widetilde{g}+h(\widetilde{g}))=\eta f^{m}$$
where $\eta$ is a multiple of a bump function. Moreover the map $g \mapsto h(g)$ is well-behaved, in the sense that it is continuous as a function of $g$, and $h(g)$ satisfies appropriate Hölder and Sobolev estimates.

As $\eta$ depends on $\widetilde{m}$, the final step is to show, by a continuity argument, that $\widetilde{m}$ can be modulated to a suitable $\widehat{m}$ to achieve $\eta=0$ in (1.5). This shows that we can "fill in" the metric $g_{\text {ext }}$ with an exact Schwarzschild initial data set.

Concerning the proof of Theorem 1.3 we use Theorem 1.1 setting $g_{\text {ext }}$ equal to a Brill-Lindquist metric:
$$g_{\mathrm{ext}}=g_{B L}^{\mathfrak{m}, \lambda \mathfrak{p}}:=\left(1+\sum_{k} \frac{m_{k}}{2\left|x-\lambda p_{k}\right|}\right)^{4} \delta_{i j} .$$
For suitable such metrics, Theorem 1.1 allows us to glue a piece of Schwarzschild in each annulus centered at $\lambda p_{k}$. To complete the construction, we need to cap this off with an "inner" region. These regular "inner" pieces of data will be constructed by rescaling the data sets constructed in [12, 17] (see Proposition 4.1) to exactly match the outer asymptotics given by the mass $\widehat{m}$ in the transition region.

We use the fact that the construction is done locally in each of the gluing regions. We thus need to take care so that the configuration allows one to apply the gluing construction to each individual annulus. This can be ensured by possibly enlarging the separation distance between each of the localized pieces of initial data in order to satisfy the hypotheses of Theorem 1.1.
1.5. Outline of the paper. In Section 2 we provide the proof of Theorem 1.1 (with additional details found in Appendix A). In Section 3, we prove some estimates on the Brill-Lindquist metric which will be necessary for appropriately applying the gluing construction from Theorem 1.1 in order to prove Theorem 1.3. In Section 4, we provide the proof of Theorem 1.3. In Section 5, we provide the
necessary modifications to prove Proposition 1.8, Finally, in Section 6, we discuss a notion of ADM mass for some of the data sets we construct.
1.6. Acknowledgements. JA gratefully acknowledges that this work was partly supported by the National Science Foundation under Grant No. 2103266.

\section*{2. Proof of Theorem 1.1}
2.1. Preliminaries. For $m>0$, we consider the Riemannian Schwarzschild metric in centered isotropic coordinates: $\left(g_{S}^{m}\right)_{i j}(x)=\left(1+\frac{m}{2|x|}\right)^{4} \delta_{i j}$ on $\mathbb{R}^{3} \backslash\{0\}$. The portion for $|x|>\frac{m}{2}$ is isometric to the metric $\left(1-\frac{2 m}{r}\right)^{-1} d r^{2}+r^{2} \stackrel{\circ}{g}_{\mathbb{S}^{2}}$ on the space $\{r: r>2 m\} \times \mathbb{S}^{2}$, where $\stackrel{\circ}{g}_{\mathbb{S}^{2}}$ is the round unit sphere metric.

Let $L_{g}$ be the linearized scalar curvature operator, given by the well-known formula $L_{g}(h)=-\Delta_{g}\left(\operatorname{tr}_{g} h\right)+\operatorname{div}_{g} \operatorname{div}_{g} h-\langle h, \operatorname{Ric}(g)\rangle_{g}$, with formal $L^{2}$ adjoint $L_{g}^{*} f=-\left(\Delta_{g} f\right) g+\operatorname{Hess}_{g} f-f \operatorname{Ric}(g)$. By explicit calculation, for metrics $\gamma$ and $\gamma+h, R(\gamma+h)=R(\gamma)+L_{\gamma}(h)+\mathcal{Q}_{\gamma}(h)$, where $\mathcal{Q}_{\gamma}(h)$ is expressed in coordinates as a homogeneous quadratic polynomial in $h_{i j}, h_{i j, k}$ and $h_{i j, k \ell}$, with coefficients that depend smoothly on $\gamma_{i j}, \gamma_{i j, k}, \gamma_{i j, k \ell}$, as well as $h_{i j}, h_{i j, k}$ and $h_{i j, k \ell}$.

Since $g_{S}^{m}$ has vanishing scalar curvature, any element $f$ in the kernel of $L_{g_{S}^{m}}^{*}$ satisfies $\operatorname{Hess}_{g_{S}^{m}}(f)=f \operatorname{Ric}\left(g_{S}^{m}\right)$ (this follows from taking the trace of the equation). A direct computation proves that a kernel element $f$ is a radial function (i.e. it only depends on $|x|$ ), and in fact the kernel of $L_{g_{S}^{m}}^{*}$ is spanned by, in isotropic coordinates, the function $f^{m}(x)=\frac{1-\frac{m}{2|x|}}{1+\frac{m}{2|x|}}$. If we change to coordinates for which $g_{S}^{m}=\left(1-\frac{2 m}{r}\right)^{-1} d r^{2}+r^{2} \stackrel{\circ}{g}_{\mathbb{S}^{2}}$, then the kernel is spanned by $\sqrt{1-\frac{2 m}{r}}$. Indeed, under this change of coordinates, $2|x|=r-m+\sqrt{r(r-2 m)}$, from which we conclude.

For a metric $g$, we will denote the volume measure by $d \mu_{g}$, and induced hypersurface measure by $d \sigma_{g}$; for the Euclidean metric, we may use to $d x$ and $d A$, respectively.
2.2. The nonlinear projected problem. Let $B=\left\{x \in \mathbb{R}^{3}:|x|<2\right\}$, and recall $\Omega=\left\{x \in \mathbb{R}^{3}: 1<|x|<2\right\}$.

Let $d(x)=d(x, \partial \Omega)$ : for $x \in \Omega, d(x)=\min (|x-1|,|x-2|)$. Let $\stackrel{\circ}{\zeta}: \mathbb{R} \rightarrow[0,1]$ be smooth and non-decreasing, $\stackrel{\circ}{\zeta}(t)=0$ for $t \leq \frac{1}{8}$, say, while $\stackrel{\circ}{\zeta}(t)=1$ for $t \geq \frac{1}{4}$. Define
$$\zeta(x)=\left\{\begin{array}{ll}
\dot{\zeta}(d(x)), & x \in \Omega \\
0, & x \in \mathbb{R}^{3} \backslash \Omega
\end{array} .\right.$$
We let $\stackrel{\circ}{\psi}: \mathbb{R} \rightarrow \mathbb{R}$ be a smooth nondecreasing function with $\stackrel{\circ}{\psi}(t)=0$ for $t \leq \frac{5}{4}$, while $\stackrel{\circ}{\psi}(t)=1$ for $t \geq \frac{7}{4}$. Let $\psi: \mathbb{R}^{3} \rightarrow \mathbb{R}$ be defined as $\psi(x)=\left\{\begin{array}{ll}\stackrel{\circ}{\psi}(|x|), & |x|<2 \\ 1, & x \in \mathbb{R}^{3} \backslash B\end{array} \quad\right.$.

As a first step to proving Theorem 1.1, we show we can perturb $\widetilde{g}$ on $\Omega$ to a metric with vanishing scalar curvature modulo a one-dimensional error. The Hölder norms in the next proposition can be computed at a (smooth) background metric, say, or at $\gamma$, and a similar remark holds for the proof of the theorem below.

Proposition 2.1. Let $0<\alpha<1$ and $\Omega^{\prime}:=\left\{x \in \mathbb{R}^{3}: 9 / 8<|x|<15 / 8\right\} \subset \Omega$. There is a constant $C_{0}>0$ such that for (smooth) metrics $\gamma$ sufficiently near $g_{S}^{m}$ in $C^{4, \alpha}(\bar{\Omega})$ and with scalar curvature $R(\gamma)$ supported in $\overline{\Omega^{\prime}}$, there exist a constant $b(\gamma)$
along with a smooth symmetric tensor $h(\gamma)$, which extends smoothly by 0 outside $\Omega$, such that $\gamma+h(\gamma)$ is a metric with
$$R(\gamma+h(\gamma))=b(\gamma) \zeta f^{m} .$$
Moreover, $\gamma \mapsto(h(\gamma), b(\gamma)): C^{4, \alpha}(\bar{\Omega}) \rightarrow C^{2, \alpha}(\bar{\Omega}) \times \mathbb{R}$ is continuous, and we have the estimate $\|h(\gamma)\|_{C^{2, \alpha}} \leq C_{0}\|R(\gamma)\|_{C^{0, \alpha}}$. In fact for $k \in \mathbb{Z}_{+}$, there is $C_{k}>0$ such that $\|h(\gamma)\|_{C^{k+2, \alpha}} \leq C_{k}\|R(\gamma)\|_{C^{k, \alpha}}$.

We postpone the proof, which follows along the lines of proofs of related results in [15, 20, 19], cf. [13], to Appendix A, where we will prove a more general statement, Proposition A.2. With this fact in hand, we are ready to prove Theorem 1.1.

\subsection*{2.3. Proof of Theorem 1.1.}

Proof. Let $\varepsilon>0$. For $\widetilde{m}>0$, we define
$$\widetilde{g}_{i j}(x)=(1-\psi(x))\left(g_{S}^{\widetilde{m}}\right)_{i j}(x)+\psi(x)\left(g_{\mathrm{ext}}\right)_{i j}(x) .$$
There is a $C^{4, \alpha}(\bar{\Omega})$-neighborhood $\mathcal{U}$ of $g_{S}^{m}$ and a $0<\xi<\min \left(\frac{m}{2}, \varepsilon, 1\right)$, such that for $J_{\xi}=[m-\xi, m+\xi]$ and for any $g_{\text {ext }} \in \mathcal{U}$ and $\widetilde{m} \in J_{\xi}, \widetilde{g}$ as above is sufficiently near $g_{S}^{m}$ to apply Proposition 2.1 with $\gamma=\widetilde{g}$ to solve for $h(\tilde{g})$, satisfying the conditions therein. Moreover there is a $\delta_{0}>0$ such that for metrics $g_{\text {ext }}$ satisfying (1.2) with $\delta<\delta_{0}, g_{\text {ext }} \in \mathcal{U}$. The constants in the estimates below are independent of $\widetilde{m} \in J_{\xi}$.

We then define $\widehat{h}$ to be the difference $\widehat{h}:=g_{\text {ext }}-g_{S}^{m}$, so that
$$\widetilde{g}=(1-\psi) g_{S}^{\widetilde{m}}+\psi g_{S}^{m}+\psi \widehat{h}=: g_{\psi}+\psi \widehat{h} .$$
Now, $R(\widetilde{g}+h(\widetilde{g}))$ vanishes precisely when
$$\int_{\Omega} f^{m} R(\widetilde{g}+h(\widetilde{g})) d \mu_{g_{S}^{m}}=0$$
We note that
$$\begin{aligned}
R(\widetilde{g}+h(\widetilde{g}))= & R\left((1-\psi) g_{S}^{\widetilde{m}}+\psi g_{S}^{m}\right)+L_{g_{\psi}}(\psi \widehat{h}+h(\widetilde{g}))+\mathcal{Q}_{g_{\psi}}(\psi \widehat{h}+h(\widetilde{g})) \\
= & R\left((1-\psi) g_{S}^{\widetilde{m}}+\psi g_{S}^{m}\right)+L_{g_{S}^{m}}(\psi \widehat{h}+h(\widetilde{g})) \\
& +\left(L_{g_{\psi}}-L_{g_{S}^{m}}\right)(\psi \widehat{h}+h(\widetilde{g}))+\mathcal{Q}_{g_{\psi}}(\psi \widehat{h}+h(\widetilde{g})) .
\end{aligned}$$

The integral of the term $f^{m} L_{g_{S}^{m}}(h(\widetilde{g}))$ vanishes because $f^{m}$ is in the kernel of $L_{g_{S}^{m}}^{*}$, and $h(\widetilde{g})$ and its derivatives vanish along the boundary.

We can estimate the term containing $L_{g_{S}^{m}}(\psi \widehat{h})$ : for some $C>0$,
$$\left|\int_{\Omega} f^{m} L_{g_{S}^{m}}(\psi \widehat{h}) d \mu_{g_{S}^{m}}\right| \leq C\|\widehat{h}\|_{C^{2}(\Omega)}$$

Moreover, there is a constant $C>0$ such that on $\bar{\Omega}$
$$\left|\mathcal{Q}_{g_{\psi}}(\psi \widehat{h}+h(\widetilde{g}))\right| \leq C\left(\|\widehat{h}\|_{C^{2}(\Omega)}^{2}+\|h(\widetilde{g})\|_{C^{2}(\Omega)}^{2}\right),$$
and
$$\left|\left(L_{g_{\psi}}-L_{g_{S}^{m}}\right)(\psi \widehat{h}+h(\widetilde{g}))\right| \leq C\left\|g_{S}^{m}-g_{S}^{\widetilde{m}}\right\|_{C^{2}(\Omega)} \cdot\left(\|\widehat{h}\|_{C^{2}(\Omega)}+\|h(\widetilde{g})\|_{C^{2}(\Omega)}\right) .$$

As for evaluating $\int_{\Omega} f^{m} R\left((1-\psi) g_{S}^{\widetilde{m}}+\psi g_{S}^{m}\right) d \mu_{g_{S}^{m}}$, it is actually more convenient to change the radial coordinate to the area radius $\rho$, as shown in [26]. In such
coordinates, $f^{m}=\sqrt{1-\frac{2 m}{\rho}}$, and so if we let $\stackrel{\circ}{g}_{\mathbb{S}^{2}}$ be the metric on the round unit sphere with area measure $d \stackrel{\circ}{\sigma}$, we have $g_{S}^{m}=\left(1-\frac{2 m}{\rho}\right)^{-1} d \rho^{2}+\rho^{2} \stackrel{\circ}{g}_{\mathbb{S}^{2}}$, and $f^{m} d \mu_{g_{S}^{m}}=\rho^{2} d \rho d \AA^{\circ}$. If we let $F(\rho)=\left((1-\psi)\left(1-\frac{2 \widehat{m}}{\rho}\right)^{-1}+\psi\left(1-\frac{2 m}{\rho}\right)^{-1}\right)$, we have $g_{\psi}=F(\rho) d \rho^{2}+\rho^{2} \stackrel{\circ}{g}_{\mathbb{S}^{2}}$. As in [26, p. 763], then $R\left(g_{\psi}\right)=-2 \rho^{-2} \frac{\partial}{\partial \rho}\left(\rho(F(\rho))^{-1}-\rho\right)$. From here it is easy to compute
$$\int_{\Omega} f^{m} R\left((1-\psi) g_{S}^{\widetilde{m}}+\psi g_{S}^{m}\right) d \mu_{g_{S}^{m}}=16 \pi(m-\widetilde{m})$$

With $0<\delta<\min \left(\delta_{0}, \xi^{2}\right)$, using (1.2) and applying Proposition 2.1 we have
$$\|\widehat{h}\|_{C^{N_{0}+2, \alpha}(\Omega)} \leq \delta, \quad\|h(\widetilde{g})\|_{C^{N_{0}, \alpha}(\Omega)} \leq C\|R(\widetilde{g})\|_{C^{N_{0}-2, \alpha}} \leq C^{\prime}(|m-\widetilde{m}|+\delta) .$$
Thus we conclude that there is a constant $C>0$ such that
$$\left|\int_{\Omega} f^{m} R(\widetilde{g}+h(\widetilde{g})) d \mu_{g_{S}^{m}}-16 \pi(m-\widetilde{m})\right| \leq C\left((m-\widetilde{m})^{2}+\delta\right)$$
By Proposition 2.1,
$$\widetilde{m} \mapsto \mathcal{I}(\widetilde{m}):=\int_{\Omega} f^{m} R(\tilde{g}+h(\tilde{g})) d \mu_{g_{S}^{m}}$$
is continuous for $\widetilde{m} \in J_{\xi}$. For $\xi$ sufficiently small, we then have by the above estimates that $\mathcal{I}(m-\xi) \cdot \mathcal{I}(m+\xi)<0$. Thus by continuity, for some $\widehat{m} \in J_{\xi}$, $\mathcal{I}(\widehat{m})=0$, as desired. \(\square\)

\section*{3. Brill-Lindquist estimates}

In order to prove Theorem 1.3 we show that for suitable $\mathfrak{m}$ and $\mathfrak{p}$, the series defining the metric $g_{B L}^{\mathfrak{m}, \mathfrak{p}}$ is well defined on $\mathbb{R}^{3} \backslash \mathfrak{p}$, and that it satisfies the estimates necessary to apply Theorem 1.1 near each point. We also want that the family of data sets we construct is closed under rescalings which move the points in $\mathfrak{p}$ away from each other. We thus begin with a discussion about sufficient conditions for both of these requirements to hold. In doing so, we shall see that the sufficient conditions we find are indeed closed under rescalings of the desired kind. We shall then construct points $\mathfrak{p}$ corresponding to an arbitrary sequence of masses $\mathfrak{m}$. The proof is rather straightforward, leveraging that near each $p_{k}$, the Brill-Lindquist metric is close to the corresponding Schwarzschild metric, with errors depending on the distance between the points in $\mathfrak{p}$.

We recall that $\mathfrak{m}=\left(m_{i}\right)_{i \in \mathbb{Z}_{+}}$, with each $m_{i}>0$, and $\mathfrak{p}=\left(p_{i}\right)_{i \in \mathbb{Z}_{+}}$, with $\left|p_{i}-p_{j}\right| \geq$ 5 for $i \neq j$. We now assume that $\mathfrak{p}$ are chosen such that for all $x$ a distance at least $0<\theta \leq 1$ away from each $p_{\ell}$, we have that $\sum_{\ell} \frac{m_{\ell}}{2\left|x-p_{\ell}\right|} \leq C \theta^{-1}(1+|x|)$. This is true whenever $\sum_{\ell} \frac{m_{\ell}}{1+\left|p_{\ell}\right|}$ is finite: given any such admissible $x$, we consider the (finite) set $P_{C}$ of points $p_{k} \in \mathfrak{p}$ a distance at most $10(1+|x|)$ from the origin, and let $P_{F}=\mathfrak{p} \backslash P_{C}$ be the set of remaining points. We have that
$$\sum_{\ell} \frac{m_{\ell}}{2\left|x-p_{\ell}\right|}=\sum_{p_{\ell} \in P_{C}} \frac{m_{\ell}}{2\left|x-p_{\ell}\right|}+\sum_{p_{\ell} \in P_{F}} \frac{m_{\ell}}{2\left|x-p_{\ell}\right|} .$$

The second sum is less than $\sum_{\ell} \frac{m_{\ell}}{1+\left|p_{\ell}\right|}$, because for all $p_{\ell} \in P_{F}, \frac{11}{10}\left|p_{\ell}\right| \geq 1+\left|p_{\ell}\right|$, so that $\left|x-p_{\ell}\right| \geq\left|p_{\ell}\right|-|x| \geq \frac{9}{10}\left|p_{\ell}\right| \geq \frac{9}{11}\left(1+\left|p_{\ell}\right|\right)$. The first sum is less than $6(1+|x|) \theta^{-1} \sum_{\ell} \frac{m_{\ell}}{1+\left|p_{\ell}\right|}$, since for $p_{\ell} \in P_{C}, 1+\left|p_{\ell}\right|<12(1+|x|)$, giving us the desired result. We thus have a uniformly convergent series on every compact subset of $\mathbb{R}^{3} \backslash \mathfrak{p}$, meaning that the series defines a harmonic function, and the metric $g_{B L}^{\mathfrak{m}, \mathfrak{p}}$ thus has vanishing scalar curvature. We note that the derivatives of the series also converge uniformly. All of this remains true after rescaling the positions of the points by some $\lambda \geq 1$, since for such $\lambda$,
$$\sum_{\ell} \frac{m_{\ell}}{1+\lambda\left|p_{\ell}\right|} \leq \sum_{\ell} \frac{m_{\ell}}{1+\left|p_{\ell}\right|} .$$

With Theorem 1.1 in mind, for positive integers $k$ and $N_{1}$, we estimate the difference $g_{B L}^{\mathfrak{m}, \mathfrak{p}}-g_{S}^{m_{k}, p_{k}}$ in $C^{N_{1}}$ on the set $\bar{\Omega}_{k}$ of points $x$ with $1 \leq\left|x-p_{k}\right| \leq 2$, ensuring these metrics are close enough depending on $m_{k}$. To this end we write
$$\begin{aligned}
\left(g_{\mathrm{BL}}^{\mathfrak{m}, \mathfrak{p}}\right)_{i j}(x) & =\left(1+\sum_{\ell=1} \frac{m_{\ell}}{2\left|x-p_{\ell}\right|}\right)^{4} \delta_{i j} \\
& =\left(1+\frac{m_{k}}{2\left|x-p_{k}\right|}\right)^{4}\left(1+\sum_{\ell \neq k} \Theta_{\ell k}(x)\right)^{4} \delta_{i j},
\end{aligned}$$
where for $\ell \neq k$,
$$\Theta_{\ell k}(x)=\frac{m_{\ell}}{\left|x-p_{\ell}\right|} \frac{\left|x-p_{k}\right|}{m_{k}+2\left|x-p_{k}\right|} .$$
Thus, for any multi-index $I$ and for any $x$ with $1 \leq\left|x-p_{k}\right| \leq 2$, we have that
$$\left|\partial_{x}^{I} \Theta_{\ell k}(x)\right| \leq C m_{\ell} \frac{1}{\left|p_{k}-p_{\ell}\right|},$$
where $C$ depends on $I$, but not on $\mathfrak{m}$ or $\mathfrak{p}$. We now define
$$\Theta_{k}(x)=\sum_{\ell \neq k} \Theta_{\ell k}(x) .$$
We want to compare the Brill-Lindquist metric with a Schwarzschild metric of mass $m_{k}$ near each point $p_{k}$. Given any sequence $\hat{\delta}_{k}>0$, we will pick the points $\mathfrak{p}$ such that for each $k$,
$$\sum_{\ell \neq k} \frac{m_{\ell}}{\left|p_{k}-p_{\ell}\right|} \leq \hat{\delta}_{k} .$$
Given $\delta_{k}>0$, by picking $\hat{\delta}_{k}=\hat{\delta}_{k}\left(\delta_{k}\right)$ sufficiently small, we see by explicit expansion of the metric components in (3.1) along with (3.3) that
$$\left\|\left(g_{B L}^{\mathfrak{m}, \mathfrak{p}}-g_{S}^{m_{k}, p_{k}}\right)_{i j}\right\|_{C^{N_{1}}\left(\bar{\Omega}_{k}\right)}<\delta_{k} .$$
This condition is closed under the appropriate rescaling, as
$$\sum_{\ell \neq k} \frac{m_{\ell}}{\lambda\left|p_{k}-p_{\ell}\right|} \leq \sum_{\ell \neq k} \frac{m_{\ell}}{\left|p_{k}-p_{\ell}\right|}$$
for $\lambda \geq 1$. We will apply this by letting $\delta_{k} \leq \frac{1}{2} \delta$ from (1.2) in Theorem 1.1 for gluing near the metric $g_{S}^{m_{k}}$. While the $p_{k}$ have not yet been explicitly chosen, we note
that $\delta_{k}$ depends only on $m_{k}$ and not on $p_{k}$. Furthermore, as $\left|p_{k}-p_{\ell}\right| \leq\left|p_{k}\right|+\left|p_{\ell}\right|$, we have
$$\sum_{\ell \neq k} \frac{m_{\ell}}{\left|p_{k}\right|+\left|p_{\ell}\right|} \leq \sum_{\ell \neq k} \frac{m_{\ell}}{\left|p_{k}-p_{\ell}\right|},$$
whence $\sum_{\ell} \frac{m_{\ell}}{1+\left|p_{\ell}\right|}$ converges, as desired.
Given a sequence $\mathfrak{m}$ of positive masses, it is now relatively straightforward to construct a sequence of points $\mathfrak{p}$ which will result in a metric $g_{B L}^{\mathfrak{m}, \mathfrak{p}}$ satisfying the required properties. One such construction is as follows.

First, we define quantities to capture how much "space" we have in the required estimates, and ensure we continue to have room to add successive points and maintain the estimates: for $k \geq 1$ and $1 \leq q \leq k$, let
$$\Xi_{q, k}=\hat{\delta}_{q}-\sum_{\ell \neq q}^{k} \frac{m_{\ell}}{\left|p_{q}-p_{\ell}\right|} .$$
In case $q=k$ we let $\Xi_{k}=\hat{\delta}_{k}-\sum_{\ell \leq k-1} \frac{m_{\ell}}{\left|p_{k}-p_{\ell}\right|}$. Observe that for $1 \leq q \leq k<k^{\prime}$, $\Xi_{q, k}>\Xi_{q, k^{\prime}}$.

We let $p_{1}=0$, and note $\Xi_{1}=\hat{\delta}_{1}$. Let $p_{2} \neq p_{1}$ be chosen such that
$$\left|p_{2}\right|=5+2 m_{2} \Xi_{1}^{-1}+2 \hat{\delta}_{2}^{-1} m_{1} .$$
Clearly $\left|p_{2}-p_{1}\right|=\left|p_{2}\right| \geq 5$, and
$$\begin{gathered}
\Xi_{2}=\hat{\delta}_{2}-\frac{m_{1}}{\left|p_{2}-p_{1}\right|}=\hat{\delta}_{2}-\frac{m_{1}}{\left|p_{2}\right|} \geq \frac{1}{2} \hat{\delta}_{2} \\
\Xi_{1,2}=\hat{\delta}_{1}-\frac{m_{2}}{\left|p_{1}-p_{2}\right|}=\hat{\delta}_{1}-\frac{m_{2}}{\left|p_{2}\right|} \geq \frac{1}{2} \hat{\delta}_{1} .
\end{gathered}$$

We now proceed recursively to define $\mathfrak{p}$ such that for all $k, \Xi_{k} \geq \frac{1}{2} \hat{\delta}_{k}$, and $\Xi_{q, k} \geq 2^{-(k-1)} \hat{\delta}_{q}$ for all $q<k$. These ensure that as we proceed in the recursion, the required estimates persist: as long as $\Xi_{k, k^{\prime}}$ is nonnegative for all $k<k^{\prime}$, (3.4) will be satisfied. As the recursion proceeds, we take care to choose $p_{k}$ so that it costs at most half of the remaining space for each of the $p_{q}$ with $q \leq k-1$. We will also arrange that for all $\ell \neq k,\left|p_{k}-p_{\ell}\right| \geq 5$. In fact, in order to obtain the estimates, we arrange that $\left|p_{q}-p_{\ell}\right| \geq \frac{1}{2}\left|p_{q}\right|$ for all $\ell<q$.

For $k \geq 3$, suppose we have $p_{1}, \ldots, p_{k-1}$, with $\Xi_{\ell} \geq \frac{1}{2} \hat{\delta}_{\ell}$ for $1 \leq \ell \leq k-1$, with $\Xi_{q, k-1} \geq 2^{-(k-2)} \hat{\delta}_{q}$ for $1 \leq q<k-1$, and with $\left|p_{q}-p_{\ell}\right| \geq \max \left(5, \frac{1}{2}\left|p_{q}\right|\right)$ for $\ell<q \leq k-1$. Observe that these conditions do hold for $k=3$.

To proceed, for $k \geq 3$, we pick $p_{k}$ to be an arbitrary point with
$$\left|p_{k}\right|=2\left|p_{k-1}\right|+4 m_{k} \max _{\ell \leq k-1} \Xi_{\ell, k-1}^{-1}+4 \hat{\delta}_{k}^{-1} \sum_{\ell \leq k-1} m_{\ell} .$$
Each summand is designed to achieve a required estimate. First, we readily see
$$\left|p_{k}-p_{k-1}\right| \geq\left|p_{k}\right|-\left|p_{k-1}\right| \geq\left|p_{k-1}\right|+4 m_{k} \max _{\ell \leq k-1} \Xi_{\ell, k-1}^{-1}+4 \hat{\delta}_{k}^{-1} \sum_{\ell \leq k-1} m_{\ell} \geq \frac{1}{2}\left|p_{k}\right|,$$
and in fact, since for $\ell<k,\left|p_{k}\right| \geq 2^{k-\ell}\left|p_{\ell}\right|$, we have
$$\left|p_{k}-p_{\ell}\right| \geq\left|p_{k}\right|-\left|p_{\ell}\right| \geq \frac{1}{2}\left|p_{k}\right| .$$
It also follows that $\left|p_{k}\right| \geq 10$ for $k \geq 3$, so that $\left|p_{k}-p_{\ell}\right| \geq 5$ for all $k \neq \ell$.

Proceeding further, we find
$$\begin{gathered}
\Xi_{k}=\hat{\delta}_{k}-\sum_{\ell \leq k-1} \frac{m_{\ell}}{\left|p_{k}-p_{\ell}\right|} \geq \hat{\delta}_{k}-\frac{2}{\left|p_{k}\right|} \sum_{\ell \leq k-1} m_{\ell} \geq \frac{1}{2} \hat{\delta}_{k}, \\
\Xi_{k-1, k}=\Xi_{k-1}-\frac{m_{k}}{\left|p_{k-1}-p_{k}\right|} \geq \Xi_{k-1}-\frac{2 m_{k}}{\left|p_{k}\right|} \geq \frac{1}{2} \Xi_{k-1} \geq 2^{-2} \hat{\delta}_{k-1},
\end{gathered}$$
while for for $q<k-1$,
$$\Xi_{q, k}=\Xi_{q, k-1}-\frac{m_{k}}{\left|p_{k}-p_{q}\right|} \geq \Xi_{q, k-1}-\frac{2 m_{k}}{\left|p_{k}\right|} \geq \frac{1}{2} \Xi_{q, k-1} \geq 2^{-(k-1)} \hat{\delta}_{q} .$$
Remark 3.1. For a given finite number of masses, there some $\sigma \geq 5$ such that it suffices just to pick $p_{k}$ so that $\left|p_{k}-p_{\ell}\right| \geq \sigma$ for $\ell \neq k$.

\section*{4. Proof of Theorem 1.3}

The last ingredient for the proof of the main theorem is the following proposition.
Proposition 4.1. For any $R_{0}>0$, and $k \in \mathbb{Z}_{+}$, there is a $\mu_{0}>0$ such that for each $0<m \leq \mu_{0}$, there is a smooth metric $g^{m}$ on $\mathbb{R}^{3}$ with vanishing scalar curvature, for which $g^{m}=g_{S}^{m}$ for $|x| \geq R_{0}$, and with $g^{m}$ converging in $C^{k}$ on compact subsets to the Euclidean metric $\stackrel{\circ}{g}$ as $m \searrow 0$.

Using this proposition, we can prove Theorem 1.3.
Proof of Theorem 1.3. Let $\mathfrak{m}$ be a sequence with $0<m_{i} \leq \mu_{1} \leq \mu_{0} / 2$, where $\mu_{0}$ is as in the preceding proposition. By the computations in the preceding section, there is a sequence $\mathfrak{p}$ for which for all $\lambda \geq 1$, in each annulus $\Omega_{k}=\left\{x: 1<\left|x-\lambda p_{k}\right|<2\right\}$, the metric $g_{B L}^{\mathfrak{m}, \lambda \mathfrak{p}}$ satisfies the requirements for $g_{\text {ext }}$ and $m=m_{k}$ and $\varepsilon>0$ from Theorem 1.1. As the construction for Theorem 1.1 is localized, applying it around each point gives a metric on $\mathbb{R}^{3} \backslash \lambda \mathfrak{p}$ which has vanishing scalar curvature, agrees with $g_{B L}^{\mathfrak{m}, \lambda \mathfrak{p}}$ at all $x$ with $\left|x-\lambda p_{k}\right| \geq 2$ for all $k$, and is identical to the Schwarzschild metric $g_{S}^{\widehat{m}_{k}, \lambda p_{k}}$ with mass $\widehat{m}_{k} \leq 3 \mu_{0} / 4$ in each $\left\{x: 0<\left|x-\lambda p_{k}\right|<1\right\}$; for $\mu_{0} \leq 3 / 4$, this metric contains an asymptotic end and a neighborhood of the minimal sphere (horizon), located at $\left|x-\lambda p_{k}\right|=\widehat{m}_{k} / 2 \leq 1 / 2$. The construction is completed by applying Proposition 4.1 with $R_{0}=3 / 4$, translated to $\left|x-\lambda p_{k}\right| \geq 3 / 4$, and $\mu_{1}$ sufficiently small depending on $\varepsilon$, and for which the Schwarzschild interiors will contain a large neighborhood of the minimal sphere) to obtain suitable metrics to fill in around each $\lambda p_{k}$. The estimate $\left|\partial_{x}^{I}\left(g_{i j}(x)-\delta_{i j}\right)\right| \leq C m_{k}$ for $\left|x-\lambda p_{k}\right| \leq 2$ follows from Theorem 1.1 and the following proof of Proposition 4.1 Completeness follows readily, since any sequence $x_{k}$ with $\left|x_{k}\right| \rightarrow \infty$ is readily seen to be unbounded in the metric $g$. \(\square\)

What remains is to prove Proposition 4.1 To do this, we show that the constructions in [12, 17] yield the existence of a family scalar-flat metrics parametrized by small $m>0$, converging to the Euclidean metric everywhere as $m \searrow 0$, and which outside a fixed ball agree with the Schwarzschild metric $g_{S}^{m}$. To be precise, the cited constructions give the existence of a sequence of small masses tending to zero, but with a modicum of extra care, we can show that a continuum of all sufficiently small masses are represented. The proof below extends to all $n \geq 3$, but we focus on the $n=3$ case for simplicity of exposition.

To carry out the proof of Proposition 4.1, we will want to effectively control the mass of a parametrized family of scalar-flat perturbations of the Euclidean metric. This is done by first considering a path of metrics parameterized by $\sigma$ passing through the flat metric at $\sigma=0$ and satisfying two additional properties: moving along this path does not change the scalar curvature to first order, on the one hand, while on the other hand it does change the mass to second order. We may then make the scalar curvature vanish identically using a further conformal change, and we get estimates on the conformal factor in terms of this mass. We can then apply Proposition A. 2 and modulate the mass in a gluing scheme to a Schwarzschild end in such a way that we effectively track the dependence of the scalar curvature on the parameter $\sigma$, the parameter $m$ of the end, and a scale parameter $R$. Continuity in $\sigma$ and $m$ allows us to conclude that we can achieve all positive masses in a sufficiently small neighborhood of 0.

Proof of Proposition 4.1. Let $\dot{g}$ be the Euclidean metric on $\mathbb{R}^{3}$ given by $\stackrel{\circ}{g}_{i j}(x)=\delta_{i j}$. To begin, with respect to the background Euclidean metric $\stackrel{\circ}{g}$, we construct a nontrivial smooth transverse-traceless (TT) (divergence-free and trace-free) symmetric tensor $h$ with compact support. One can readily construct such a tensor; for example a very concrete proof is given in [17] for a smooth TT tensor $\stackrel{\circ}{h}$ of compact support on Euclidean $\mathbb{R}^{n}$, and since the conditions are linear and closed under pullback by the parity operator $x \mapsto-x$, and under translation by a constant vector, for suitable $c$, we let $h$ be given in Cartesian components by $h_{i j}(x)=\stackrel{\circ}{h}_{i j}(x-c)+\stackrel{\circ}{h}_{i j}(-x-c)$, which is parity-symmetric; if $\stackrel{\circ}{h}$ were not parity-antisymmetric to start, we could take $c=0$. Note that the linearization of the scalar curvature operator at the Euclidean metric vanishes in the direction $h$ by the TT condition: $L h=-\Delta(\operatorname{tr}(h))+\operatorname{div}(\operatorname{div}(h))=0$.

For each $\sigma \in \mathbb{R}$ with $|\sigma|$ sufficiently small, consider the metric $\gamma^{\sigma}$ given in Cartesian coordinates as $\gamma_{i j}^{\sigma}=\delta_{i j}+\sigma h_{i j}$. For any $k$, there is a $C$ such that for all such $\sigma$ and all $|I| \leq k,\left|\partial_{x}^{I} R\left(\gamma^{\sigma}\right)\right| \leq C \sigma^{2}$. As such, for $|\sigma|$ small, we solve for $1+v^{\sigma}=u^{\sigma}>0$ and tending to 1 at infinity with $\Delta_{\gamma^{\sigma}} u^{\sigma}=\frac{1}{8} R\left(\gamma^{\sigma}\right) u^{\sigma}$, which means $R\left(\left(u^{\sigma}\right)^{4} \gamma^{\sigma}\right)=0$. (One can solve in appropriate weighted spaces such as in [3, 29]: the operator $\Delta_{\gamma^{\sigma}}$ is an isomorphism in such spaces, and $\Delta_{\gamma^{\sigma}}-\frac{1}{8} R\left(\gamma^{\sigma}\right)$ is a small perturbation, and hence is an isomorphism, for small $|\sigma|$, cf. Section 5.) By uniqueness and parity-symmetry, $u^{\sigma}(x)=u^{\sigma}(-x)$. Moreover, $u^{\sigma}$ is Euclideanharmonic at infinity, and as such possesses a spherical harmonic expansion,
$$u^{\sigma}(x)=1+\frac{m(\sigma)}{2|x|}+O\left(|x|^{-3}\right),$$
where coefficients of the parity-antisymmetric terms $x^{i}|x|^{-3}$ in the expansion must vanish. It is elementary to see that $\left(u^{\sigma}\right)^{4} \gamma^{\sigma}$ is asymptotically flat, and
$$16 \pi m(\sigma)=-\int_{\mathbb{R}^{3}} R\left(\gamma^{\sigma}\right) u^{\sigma} d \mu_{\gamma^{\sigma}}$$
Since $L h=0$, it is not hard to see $m^{\prime}(0)=0$ (which also follows from the Positive Mass Theorem) and an elementary calculation [17, Prop. 3.1] yields the second derivative $m^{\prime \prime}(0)=\frac{1}{32 \pi} \int_{\mathbb{R}^{3}}|\nabla h|^{2} d x$. Thus there are positive constants $c_{1}$ and $c_{2}$ such that for $|\sigma|$ small, $c_{1} \sigma^{2} \leq m(\sigma) \leq c_{2} \sigma^{2}$.

Let $\rho \geq 1$ be smooth, with $\rho(x)=|x|$ for $|x| \geq 2$ (alternatively, $\rho(x)=$ $\sqrt{1+|x|^{2}}$ ). By the above estimate of $R\left(\gamma^{\sigma}\right)$ and expansion using the fundamental solution of the Laplacian (cf., e.g., [29, Thm. 3]),
$$\sum_{|I| \leq k} \sup _{x \in \mathbb{R}^{3}} \rho(x)^{1+|I|}\left|\partial_{x}^{I} v^{\sigma}(x)\right| \leq C_{k} \sigma^{2} \leq C_{k} c_{1}^{-1} m(\sigma) .$$
In fact, by elementary expansion of the fundamental solution $|x-y|^{-1}$, and using that $h(y)$ is supported on some $|y| \leq K$, it follows that there is a constant $C$ such that for $R$ sufficiently large and $|x| \geq R$, and with $w^{\sigma}=v^{\sigma}-\frac{m(\sigma)}{2|x|}$,
$$|x|^{2}\left|w^{\sigma}(x)\right|+|x|^{3}\left|\partial_{x} w^{\sigma}(x)\right| \leq C \sigma^{2} .$$
In fact, by parity-symmetry we actually have another power of $|x|$ decay. Thus $\widehat{g}^{\sigma}:=\left(u^{\sigma}\right)^{4} \gamma^{\sigma}$ is uniformly close to the background Euclidean metric, on compact sets (and in fact in a weighted space globally). Moreover it is readily seen that $\widehat{g}^{\sigma}$ is smooth in $\sigma$ (measured in a Sobolev or Hölder norm, weighted as appropriate if desired). By explicit calculation,
$$\int_{\{|x|=R\}} \sum_{i, j=1}^{3}\left(\left(g_{S}^{m}\right)_{i j, i}-\left(g_{S}^{m}\right)_{i i, j}\right) \nu^{j} d A=16 \pi m+O\left(m^{2} R^{-1}\right)$$
so that using (4.1)-(4.2), we find
$$\int_{\{|x|=R\}} \sum_{i, j=1}^{3}\left(\left(\widehat{g}^{\sigma}\right)_{i j, i}-\left(\widehat{g}^{\sigma}\right)_{i i, j}\right) \nu^{j} d A=16 \pi m(\sigma)+O\left(\sigma^{2} R^{-1}\right)$$
The error estimates hold uniformly in $R$ large, and $(\sigma, m) \in J \times J^{\prime}$, where $J$ is an interval of the form $\left[-\sigma_{0}, \sigma_{0}\right]$, for $0<\sigma_{0}<1$ sufficiently small and $J^{\prime}$ is a bounded interval including 0.

We will patch our data over a large annulus $\{x: R<|x|<2 R\}$ to a Schwarzschild end with mass $m$, and then rescale to the unit annulus $\Omega=\{x: 1<|x|<2\}$, with an eye toward invoking Proposition A.2. We will thus have three parameters $(\sigma, m, R)$, and for $(\sigma, m) \in J \times J^{\prime}$, for sufficiently large $R$, we will be able to estimate the leading order behavior of various quantities up to sufficiently small errors. (As will become clear by the end of the proof, there are alternate ways to utilize the parameter space effectively, say fixing $R$ and scaling $\sigma$ and $m$ suitably, but the approach we take seems straightforward enough.)

To carry this out, for $R>0$, let $\phi_{R}: \mathbb{R}^{3} \rightarrow \mathbb{R}^{3}$ be given by $\phi_{R}(x)=R x$. Let $\psi_{R}(x)=\psi(x / R)$, and let $\tilde{g}:=\tilde{g}^{\sigma, m, R}$ be given by $\tilde{g}=R^{-2} \phi_{R}^{*}\left(\left(1-\psi_{R}\right) \widehat{g}^{\sigma}+\psi_{R} g_{S}^{m}\right)$. There is a constant $C>0$ depending on $k$ such that for large $R,(\sigma, m) \in J \times J^{\prime}$, $|I| \leq k$, and all $x \in \Omega,\left|\partial_{x}^{I}\left(\tilde{g}_{i j}(x)-\delta_{i j}\right)\right| \leq C R^{-1}$. As $\tilde{g}$ is uniformly close to the Euclidean metric, we can apply Proposition A. 2 to obtain $\tilde{h}:=\tilde{h}^{\sigma, m, R}$ smooth, with support on $\bar{\Omega}$, such that $R(\tilde{g}+\tilde{h}) \in \operatorname{span}\left\{\zeta, \zeta x^{1}, \zeta x^{2}, \zeta x^{3}\right\}$, where as above $\zeta$ is a rotationally symmetric bump function vanishing outside $\Omega$. Moreover, we have the estimate $\|\tilde{h}\|_{C^{2}} \leq C\|R(\tilde{g})\|_{C^{1}}$ for $C$ uniform in $(\sigma, m) \in J \times J^{\prime}$ and $R$ large; more precisely, for any $\alpha \in(0,1),\|\tilde{h}\|_{C^{2, \alpha}} \leq C\|R(\tilde{g})\|_{C^{0, \alpha}}$. On the other hand, by parity symmetry the components in the linear direction must vanish: $R\left(\tilde{g}^{\sigma, m, R}+\tilde{h}^{\sigma, m, R}\right)=b(\sigma, m, R) \zeta$. Furthermore, $\tilde{h}=\tilde{h}^{\sigma, m, R}$ and the coefficient $b$ are continuous in $(\sigma, m, R)$. As $\left\|\tilde{g}^{\sigma, m, R}-\tilde{g}^{\sigma, m^{\prime}, r}\right\|_{C^{4, \alpha}}=O\left(\left|m-m^{\prime}\right| / R\right)$ is readily
seen, then $\left\|\tilde{h}^{\sigma, m, R}-\tilde{h}^{\sigma, m^{\prime}, R}\right\|_{C^{2, \alpha}} \leq C\left|m-m^{\prime}\right| / R$ follows from the Lipschitz bound in Proposition A.2.
$R(\tilde{g})$ can be estimated by direct expansion. Indeed, $\tilde{g}$ is conformally flat, with $\tilde{g}_{i j}=U \delta_{i j}$, where $U(x)=(1-\psi(x))\left(1+v^{\sigma}(R x)\right)^{4}+\psi(x)\left(1+\frac{m}{2|R x|}\right)^{4}$. As such,
$$R(\tilde{g})=-2 U^{-2} \sum_{j=1}^{3} U_{, j j}+\frac{3}{2} U^{-3}|d U|^{2} .$$
Moreover $W(x):=U(x)-\left(1+\frac{m / R}{2|x|}\right)^{4}$ can be written
$$(1-\psi)\left(\left(v^{\sigma}(R x)-\frac{m / R}{2|x|}\right)\left(2+v^{\sigma}(R x)+\frac{m / R}{2|x|}\right)\left(\left(1+v^{\sigma}(R x)\right)^{2}+\left(1+\frac{m / R}{2|x|}\right)^{2}\right)\right),$$
so that using (4.1) we find a constant $C$ so that for all $(\sigma, m) \in J \times J^{\prime}$ and $R \geq 1$ sufficiently large (so that in particular $m R^{-1} \leq 1$ ),
$$\begin{aligned}
|W(x)|+|\partial W(x)|+\left|\partial^{2} W(x)\right| & \leq C\left(m+\sigma^{2}\right) R^{-1} \\
\left|\partial^{2} U\right| & \leq C\left(m+\sigma^{2}\right) R^{-1} \\
|\partial U|^{2} & \leq C\left(m^{2}+\sigma^{4}\right) R^{-2} .
\end{aligned}$$
We readily conclude $\|R(\tilde{g})\|_{C^{1}}=O\left(m+\sigma^{2}\right) R^{-1}$, and thus $\|\tilde{h}\|_{C^{2, \alpha}}=O\left(m+\sigma^{2}\right) R^{-1}$.
We let $\bar{g}=\bar{g}^{\sigma, m, R}=\tilde{g}^{\sigma, m, R}+\tilde{h}^{\sigma, m, R}=\tilde{g}+\tilde{h}$, and we make the following claim:
Lemma 4.2. $F(\sigma, m, R):=\int_{\Omega} R(\bar{g}) d x=16 \pi(m-m(\sigma)) R^{-1}+\mathcal{E}$, where for some constant $C>0, \mathcal{E}$ is continuous in $(\sigma, m, R)$, with $|\mathcal{E}| \leq C\left(m^{2}+\sigma^{2}\right) R^{-2}$. Moreover, we have $\left|\mathcal{E}(\sigma, m, R)-\mathcal{E}\left(\sigma, m^{\prime}, R\right)\right| \leq C\left|m-m^{\prime}\right| R^{-2}$.

Proof. The proof is a straightforward calculation using the above estimates. We begin with the expansion of the scalar curvature $R(\bar{g})=R(\tilde{g})+L_{\tilde{g}} \tilde{h}+\mathcal{Q}_{\tilde{g}}(\tilde{h})$. We include the $Q_{\tilde{g}}(\tilde{h})$-term in $\mathcal{E}$ by the estimate we have on $\tilde{h}$. As for $L_{\tilde{g}} \tilde{h}$, we write
$$\int_{\Omega} L_{\tilde{g}} \tilde{h} d x=\int_{\Omega} L_{\tilde{g}} \tilde{h}\left(d x-d \mu_{\tilde{g}}\right)$$
where we integrated by parts to get $\int_{\Omega} L_{\tilde{g}} \tilde{h} d \mu_{\tilde{g}}=0$. This can also put placed into $\mathcal{E}$ by estimating the difference of the measures:
$$\left|d x-d \mu_{\tilde{g}}\right| / d x=\left|1-U^{3 / 2}\right| \leq C\left(m+\sigma^{2}\right) R^{-1} .$$
Finally, we use (4.5)-(4.6) to replace $\int_{\Omega} R(\tilde{g}) d x$ by $\int_{\Omega} \sum_{i, j=1}^{3}\left(\tilde{g}_{i j, i j}-\tilde{g}_{i i, j j}\right) d x$, with the difference contributing another term to $\mathcal{E}$, and then we apply (4.3)-(4.4) to obtain the difference in the masses, up to an acceptable error term. We have $\left|\mathcal{E}(\sigma, m, R)-\mathcal{E}\left(\sigma, m^{\prime}, R\right)\right| \leq C\left|m-m^{\prime}\right| R^{-2}$ by the Lipschitz bound on $\tilde{h}^{\sigma, m, R}$. □

As such, $F$ is Lipschitz, and hence absolutely continuous in $m$, and so
$$F\left(\sigma, m_{2}, R\right)-F\left(\sigma, m_{1}, R\right)=\int_{m_{1}}^{m_{2}} \frac{\partial F}{\partial m} d m$$
As $\frac{\partial F}{\partial m}>0$ a.e. for $R$ sufficiently large, we conclude $F$ is increasing in $m$.
For each $\sigma \neq 0$, let $J_{\sigma}^{\prime}=[m(\sigma) / 2,2 m(\sigma)] \subset(0, \infty)$, and recall $c_{1} \sigma^{2} \leq m(\sigma)$. For any fixed $R$ sufficiently large, independent of $|\sigma|$ small, we have $F(\sigma, 2 m(\sigma), R)>0$,
while $F(\sigma, m(\sigma) / 2, R)<0$. By continuity, $F(\sigma, M(\sigma), R)=0$ for some $M(\sigma) \in J_{\sigma}^{\prime}$. By the monotonicity, this $M(\sigma)$ is uniquely determined. Moreover $\frac{\partial F}{\partial m} \geq c>0$, so that $\left|F\left(\sigma, M\left(\sigma^{\prime}\right), R\right)\right|=\left|\int_{M(\sigma)}^{M\left(\sigma^{\prime}\right)} \frac{\partial F}{\partial m} d m\right| \geq c\left|M\left(\sigma^{\prime}\right)-M(\sigma)\right|$. Letting $\sigma \rightarrow \sigma^{\prime}$, we see $M(\sigma) \rightarrow M\left(\sigma^{\prime}\right)$, since $F$ is continuous and $F\left(\sigma^{\prime}, M\left(\sigma^{\prime}\right), R\right)=0$.

The above scheme allows us to construct a metric which outside a ball of sufficiently large radius is identically Schwarzschild of mass $m$. By rescaling, we can accommodate any radius $R_{0}>0$. \(\square\)

\section*{5. Vacuum initial data sets with infinitely many minimal spheres}

In the previous section we completed the proof of Theorem 1.3 by smoothing out the punctured regions of Brill-Lindquist data with "small" data, and in so doing we removed any Schwarzschild horizons in $\left\{x:\left|x-c_{k}\right|<1\right\}$. In this section we prove Proposition 1.8 by modifying the above construction to obtain scalar-flat initial data on $\mathbb{R}^{3}$ with infinitely many minimal spheres. We will employ the method of Miao [30], who constructed such data with a single minimal sphere by a method different than that of Beig-Ó Murchadha [5]; Miao's method was extended to a finite number of minimal spheres in [16].

To prove Proposition 1.8, we first construct metrics which are flat in some ball, which agree with an exterior end of a Schwarzschild (including a neighborhood of the minimal sphere) outside of a larger ball, and have positive (and potentially large) scalar curvature in a transition region. Following Miao [30], we then use a result of Lohkamp [27, Thm. 1] in order to push the scalar curvature down to near 0 in the transition region. Adjusting the scalar curvature to be identically 0 is accomplished with a conformal change in a perturbative setting, as Lohkamp's result gives a change in metric which is small in $C^{0}$. As such, the resulting metric will still admit a minimal sphere near that of the original Schwarzschild end.

Because the scalar curvature of the resulting metric is identically 0, we can then follow the proof of Theorem 1.3, as we are now in a position to apply Theorem 1.1 We do so in order to conclude the proof, with the slight modification that we modulate using a rescaling parameter $\theta$ instead of the Schwarzschild mass directly.

For use in the proof, we recall the definition of weighted Sobolev spaces, following [3]. As we had earlier, let $\rho \geq 1$ be a smooth function on $\mathbb{R}^{3}$ for which $\rho(x)=|x|$ for $|x| \geq 2$. Then for $k$ a nonnegative integer, $\tau \in \mathbb{R}$ and $p>1$, we have weighted Sobolev spaces $W_{-\tau}^{k, p}=W_{-\tau}^{k, p}\left(\mathbb{R}^{3}\right)$ given by the norm
$$\|u\|_{W_{-\tau}^{k, p}}^{p}=\sum_{j=0}^{k} \sum_{|I|=j}\left|\partial^{I} u\right|^{p} \rho^{\tau p-3} d x$$
Proof of Proposition 1.8. Let $0<m<1$, so that the minimal sphere in $\left(g_{S}^{m}\right)_{i j}(x)=$ $\left(1+\frac{m}{2|x|}\right)^{4} \delta_{i j}$ is located at $|x|=\frac{m}{2}<\frac{1}{2}$. Fix some $0<r_{0}<\frac{1}{2}$, and consider the function
$$w(x)=\left\{\begin{array}{ll}
1+\frac{m}{2 r_{0}}, & |x|<r_{0} \\
1+\frac{m}{2|x|}, & |x| \geq r_{0}
\end{array} .\right.$$
Then $w$ is a Euclidean superharmonic function, and for small $\eta>0$, a mollification $w_{\eta}$ of $w$ by a rotationally symmetric mollifier with small enough support is then readily seen yield a smooth metric $w_{\eta}^{4} \delta_{i j}$ with positive scalar curvature in an annulus
$r_{0}-\eta<|x|<r_{0}+\eta$, and vanishing scalar curvature outside this region, agreeing with a flat metric near the origin, and with the original Schwarzschild metric in a neighborhood of $|x|>\frac{m}{2}$. As in [30], we now apply a result Lohkamp [27] which gives for any $\varepsilon>0$, a $C^{0}$-nearby smooth metric $g^{\varepsilon}$ with $-\varepsilon \leq R\left(g^{\varepsilon}\right) \leq 0$ on $r_{0}-\eta-\varepsilon<|x|<r_{0}+\eta+\varepsilon$, and with $g_{i j}^{\varepsilon}=w_{\eta}^{4} \delta_{i j}$ outside this region.

We make a slight twist on the argument of Miao at this point. For $\theta>0$ we consider the map $\varphi_{\theta}(x)=\theta x$, and let $g_{\theta}=\theta^{-2} \varphi_{\theta}^{*} g^{\varepsilon}$. We have $R\left(g_{\theta}\right)=\theta^{2} R\left(g^{\varepsilon}\right)$, so that $-\theta^{2} \varepsilon \leq R\left(g_{\theta}\right) \leq 0$, while for $|x|>\theta^{-1}\left(r_{0}+\eta+\varepsilon\right),\left(g_{\theta}\right)_{i j}(x)=\left(1+\frac{m / \theta}{2|x|}\right)^{4} \delta_{i j}$. Thus for $\eta+\varepsilon$ small and $\theta$ near 1 , $g_{\theta}$ agrees with $g_{S}^{m / \theta}$ on an open set which contains $\left\{x:|x| \geq \frac{m / \theta}{2}\right\} \supset\{x: 1 \leq|x| \leq 2\}=\bar{\Omega}$, so that in particular it contains the minimal sphere.

For $0<\tau<1$ and $p>1$, the operator $\Delta_{g_{\theta}}-\frac{1}{8} R\left(g_{\theta}\right): W_{-\tau}^{2, p} \rightarrow W_{-\tau-2}^{0, p}$ is a compact perturbation of the isomorphism $\Delta_{g_{\theta}}$, and as such it has Fredholm index zero [3]. If $w \in W_{-\tau}^{2, p}$ with $\left(\Delta_{g_{\theta}}-\frac{1}{8} R\left(g_{\theta}\right)\right)(w)=0$, multiplying by $w$ and integrating by parts we obtain
$$0=\int_{\mathbb{R}^{3}}\left(w \Delta_{g_{\theta}} w-\frac{1}{8} R\left(g_{\theta}\right) w^{2}\right) d \mu_{g_{\theta}}=-\int_{\mathbb{R}^{3}}\left(|\nabla w|_{g_{\theta}}^{2}+\frac{1}{8} R\left(g_{\theta}\right) w^{2}\right) d \mu_{g_{\theta}}$$
where the boundary term vanishes due to the decay of $w$. In fact since $R\left(g_{\theta}\right)=0$ for $|x| \geq r_{0}+\eta+\varepsilon$, on this region $\Delta w \in W_{-\tau-3}^{0, p}$. As such, it admits an expansion, for some constants $C, A$ and $\gamma>0$
$$\left|w(x)-\frac{A}{|x|}\right|+|x|\left|\partial\left(w(x)-\frac{A}{|x|}\right)\right| \leq C|x|^{-1-\gamma}$$
as in [3, Thm. 1.17] (with an additional step to get the decay of the derivative), cf. [33, Lemma 3.2] or [29, Thm. 2]. Applying the Hölder inequality, and the Sobolev inequality $\|w\|_{L^{6}}^{2} \leq C\|\nabla w\|_{L^{2}}^{2}$, with a uniform $C$ for $\varepsilon$ small and $\theta$ near 1 (recall that Lohkamp's deformation is $C^{0}$-small), we obtain
$$\|\nabla w\|_{L^{2}}^{2} \leq\left\|\frac{1}{8} R\left(g_{\theta}\right)\right\|_{L^{3 / 2}}\|w\|_{L^{6}}^{2} \leq C\left\|\frac{1}{8} R\left(g_{\theta}\right)\right\|_{L^{3 / 2}}\|\nabla w\|_{L^{2}}^{2} \leq C^{\prime} \theta^{2} \varepsilon\|\nabla w\|_{L^{2}}^{2} .$$
Thus for $\theta$ near 1 and $\varepsilon$ small, we conclude $w=0$, and hence that $\Delta_{g_{\theta}}-\frac{1}{8} R\left(g_{\theta}\right)$ is an isomorphism.

We want to solve for a positive function $u=u_{\theta}$ close to 1 , and so that $u(x)$ approaches 1 as $|x| \rightarrow \infty$, with $R\left(u^{4} g_{\theta}\right)=0$, i.e. $\Delta_{g_{\theta}} u-\frac{1}{8} R\left(g_{\theta}\right) u=0$. We let $v=u-1$, so that the equation becomes $\Delta_{g_{\theta}} v-\frac{1}{8} R\left(g_{\theta}\right) v=\frac{1}{8} R\left(g_{\theta}\right)$. Since the operator $\Delta_{g_{\theta}}-\frac{1}{8} R\left(g_{\theta}\right)$ is an isomorphism, we can solve for $v \in W_{-\tau}^{2, p}$. For $\theta$ near 1 and $\varepsilon$ sufficiently small, we show that $u$ is close to 1 in $C^{2}(\bar{\Omega})$, and a barrier argument as in [30] guarantees there is a minimal sphere in $\left(\Omega, u^{4} g_{\theta}\right)$.

We proceed to get estimates on $v=u-1$. Since $R\left(g_{\theta}\right)=0$ for $|x| \geq r_{0}+\eta+\varepsilon$ where the barrier argument is applied, on this region $(1+v(x))\left(1+\frac{m / \theta}{2|x|}\right)$ is a Euclidean harmonic function which tends to 1 as $|x| \rightarrow \infty$. As such, it admits an expansion in spherical harmonics:
$$(1+v(x))\left(1+\frac{m / \theta}{2|x|}\right)=1+\frac{m_{\theta}}{2|x|}+O\left(|x|^{-2}\right)$$
so that $v(x)=\frac{m_{\theta}-m / \theta}{2|x|}+O\left(|x|^{-2}\right)$ and $|\partial v(x)|=O\left(|x|^{-2}\right)$. Using these decay rates, we get integral estimates on $v$ by multiplying the differential equation by $v$
and integrating by parts as we did above, and applying Hölder's inequality (and the arithmetic-geometric mean inequality) to obtain for any $\delta>0$ (norms taken on $\left.\left(\mathbb{R}^{3}, d \mu_{g_{\theta}}\right)\right)$,
$$\begin{aligned}
\|\nabla v\|_{L^{2}}^{2} & \leq\left\|\frac{1}{8} R\left(g_{\theta}\right)\right\|_{L^{3 / 2}}\|v\|_{L^{6}}^{2}+\left\|\frac{1}{8} R\left(g_{\theta}\right)\right\|_{L^{6 / 5}}\|v\|_{L^{6}} \\
& \leq\left\|\frac{1}{8} R\left(g_{\theta}\right)\right\|_{L^{3 / 2}}\|v\|_{L^{6}}^{2}+\frac{1}{2 \delta}\left\|\frac{1}{8} R\left(g_{\theta}\right)\right\|_{L^{6 / 5}}^{2}+\frac{\delta}{2}\|v\|_{L^{6}}^{2} .
\end{aligned}$$
Applying the Sobolev inequality $\|v\|_{L^{6}}^{2} \leq C\|\nabla v\|_{L^{2}}^{2}$, with a uniform $C$ for $\varepsilon$ small and $\theta$ near 1 as above, for $\delta$ sufficiently small, we can absorb the $\|v\|_{L^{6}}^{2}$ terms to obtain, where $C$ and $C^{\prime}$ are uniform for $\varepsilon$ small and $\theta$ near 1:
$$\|v\|_{L^{6}} \leq C\left\|R\left(g_{\theta}\right)\right\|_{L^{6 / 5}} \leq C^{\prime} \theta^{2} \varepsilon .$$
By a DeGiorgi-Nash-Moser estimate [24, Thm, 8.17],
$$|v(x)| \leq C\left(\left\|R\left(g_{\theta}\right)\right\|_{L^{3}}+\|v\|_{L^{6}}\right) \leq C^{\prime} \theta^{2} \varepsilon .$$
The constant $C$ in the above estimate depends on ellipticity and boundedness constants for the divergence-form operators $\Delta_{g_{\theta}}$, which are uniform in $\varepsilon$ small and $\theta$ near 1, by the $C^{0}$-control on $g_{\theta}$. Since on a neighborhood of $\bar{\Omega}$ we have $\left(g_{\theta}\right)_{i j}=\left(1+\frac{m / \theta}{2|x|}\right)^{4} \delta_{i j}$, interior Schauder estimates (cf. [24, Thm. 6.2]) for $\Delta_{g_{\theta}} v=0$ yield $\|v\|_{C^{2, \alpha}(\bar{\Omega})} \leq C \theta^{2} \varepsilon$.

It is also not hard to show that $u=u_{\theta}=v_{\theta}+1$ depends continuously on $\theta$, as
$$\begin{aligned}
\Delta_{g_{\theta}}\left(u_{\tau}-u_{\theta}\right) & =\Delta_{g_{\tau}} u_{\tau}-\Delta_{g_{\theta}} u_{\theta}+\left(\Delta_{g_{\theta}}-\Delta_{g_{\tau}}\right) u_{\tau} \\
& =\frac{1}{8} R\left(g_{\tau}\right) u_{\tau}-\frac{1}{8} R\left(g_{\theta}\right) u_{\theta}+\left(\Delta_{g_{\theta}}-\Delta_{g_{\tau}}\right) u_{\tau} \\
& =\frac{1}{8} R\left(g_{\theta}\right)\left(u_{\tau}-u_{\theta}\right)+\frac{1}{8}\left(R\left(g_{\tau}\right)-R\left(g_{\theta}\right)\right) u_{\tau}+\left(\Delta_{g_{\theta}}-\Delta_{g_{\tau}}\right) u_{\tau}
\end{aligned}$$
so that
$$\left(\Delta_{g_{\theta}}-\frac{1}{8} R\left(g_{\theta}\right)\right)\left(v_{\tau}-v_{\theta}\right)=\frac{1}{8}\left(R\left(g_{\tau}\right)-R\left(g_{\theta}\right)\right) u_{\tau}+\left(\Delta_{g_{\theta}}-\Delta_{g_{\tau}}\right) u_{\tau} \text {. }$$
Repeating the integration-by-parts argument sketched above, allows us to conclude that $u_{\theta}$ varies continuously in $L^{6}\left(\mathbb{R}^{3}\right)$, and then by the elliptic estimates in $C^{2, \alpha}(\bar{\Omega})$.