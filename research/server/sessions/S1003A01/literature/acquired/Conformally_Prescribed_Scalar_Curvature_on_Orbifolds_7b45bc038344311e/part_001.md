---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Conformally Prescribed Scalar Curvature on Orbifolds]

---
source_file: 2112_05207v1.pdf
converter: mathpix
format: mmd
---

\title{
CONFORMALLY PRESCRIBED SCALAR CURVATURE ON ORBIFOLDS
}

\author{
TAO JU AND JEFF VIACLOVSKY
}

\begin{abstract}
We study the prescribed scalar curvature problem in a conformal class on orbifolds with isolated singularities. We prove a compactness theorem in dimension 4, and an existence theorem which holds in dimensions $n \geq 4$. This problem is more subtle than the manifold case since the positive mass theorem does not hold for ALE metrics in general. We also determine the U(2)-invariant Leray-Schauder degree for a family of negative-mass orbifolds found by LeBrun.
\end{abstract}

\section*{Contents}
\begin{itemize}
\item[1.] Introduction
\item[2.] Properties of the mass
\item[3.] Compactness preliminaries
\item[4.] Local blow-up analysis
\item[5.] Blow-up points must be isolated and simple
\item[6.] Variational methods
\item[7.] LeBrun metrics
\end{itemize}

References

\section*{1. Introduction}

To begin, we give the definition of a Riemannian orbifold.
Definition 1.1. We say that $(M, g)$ is a Riemannian orbifold of dimension $n$ if $M$ is a smooth manifold of dimension $n$ with a smooth Riemannian metric away from a finite singular set
$$\Sigma=\left\{\left(q_{1}, \ldots, q_{l}\right)\right\} .$$
Near each singular point $q_{j}$, there exists a neighborhood $U_{j}$ of $q_{j}$, a nontrivial finite subgroup $\Gamma_{j} \subset \mathrm{O}(n)$ acting freely on $\mathbb{R}^{n} \backslash\{0\}$ and a $\Gamma_{j}$-equivariant diffeomorphism
$$\varphi_{j}: \widetilde{U_{j}} \rightarrow B_{\sigma_{j}}(0),$$
where $\widetilde{U_{j}}$ is the completion (by adding a point $\tilde{q}_{j}$ ) of the universal cover of $U_{j} \backslash\left\{q_{j}\right\}$, and $B_{\sigma_{j}}(0)$ is a ball of radius $\sigma_{j}$ about the origin in $\mathbb{R}^{4}$. Furthermore, $\left(\varphi_{j}\right)_{*} \pi_{j}^{*} g$ extends to a smooth Riemannian metric on $B_{\sigma_{j}}(0)$, where $\pi_{j}: \widetilde{U_{j}} \backslash\left\{\tilde{q}_{j}\right\} \rightarrow U_{j} \backslash\left\{q_{j}\right\}$ is a universal covering map.

Our convention is that if $l=0$, then $\Sigma=\emptyset$, and $(M, g)$ is a smooth Riemannian manifold. But if $l \geq 1$, then there must be nontrivial singular points. We next define the meaning of a $C^{k}(M)$ function on a Riemannian orbifold $(M, g)$.

Definition 1.2. A function $f: M \rightarrow \mathbb{R}$ is in $C^{k}(M)$ if $f: M \backslash \Sigma \rightarrow \mathbb{R}$ is in $C^{k}(M \backslash \Sigma)$, and near each singularity, there exists a coordinate system $\varphi_{j}$ such that the function $f \circ \pi_{j} \circ \varphi_{j}^{-1}: B_{\sigma_{j}}(0) \rightarrow \mathbb{R}$ is in $C^{k}\left(B_{\sigma_{j}}(0)\right)$. We can also define the spaces $C^{\infty}(M), C^{k, \alpha}(M), C_{\text {loc }}^{k}(M)$ in a similar fashion.

\footnotetext{
The authors were partially supported by NSF Grants DMS-1811096 and DMS-2105478.
}

Note that since linear terms are never invariant under a nontrivial orbifold group, a $C^{1}$ function necessarily has a critical point at any nontrivial orbifold singularity. In other words, $\Sigma \subset \operatorname{Crit}(f)$, where $\operatorname{Crit}(f) \equiv\left\{x \in M \mid \nabla_{g} f(x)=0\right\}$.
Remark 1.3. In general, an orbifold can have higher-dimensional singular sets. So our definition is restrictive in that we only allow isolated quotient singularities.

Assume $(M, g)$ is a compact Riemannian $n$-orbifold with positive scalar curvature $R_{g}>0$. Let $K>0$ be a positive $C^{2}$ function on $M$. We will study the following equation
$$-\Delta_{g} u+c(n) R_{g} u=K u^{p},$$
where $c(n)=\frac{n-2}{4(n-1)}, 1<p \leq \frac{n+2}{n-2}$ and $\Delta_{g}$ is the Laplacian operator associated with $g$. Let $L_{g}=\Delta_{g}-c(n) R_{g}$ denote the conformal Laplacian of the metric $g$. When $p=\frac{n+2}{n-2}$, the solution of equation (1.3) corresponds to the prescribed scalar curvature problem. That is, the metric given by $\tilde{g}=u^{\frac{4}{n-2}} g$ has scalar curvature $R_{\tilde{g}}=\frac{4(n-1)}{n-2} K$.

The Yamabe problem on manifolds is well-understood, and we refer to [Aub98a, LP87, Sch84, Yam60, and references therein. The prescribed scalar curvature problem on $S^{n}$ and other manifolds has been studied in many works; see for example [BAA08, CGY93, CL01, Li95, Li96, Mal02, SZ96]. Prescribed scalar curvature on manifolds is studied for example in [BACCH96, MM20, May17]. More recently, the Yamabe problem on singular spaces has been of interest; see for example [AB03, AB04, ACM14, ACM19, CLV21, Mon17, Mon18, Via10, Via13].

Analogous to the generalization from manifolds to orbifolds, there is the following generalization of asymptotically flat (AF) metrics.

Definition 1.4. A complete Riemannian orbifold ( $X^{n}, g$ ) with finitely many singular points is called asymptotically locally Euclidean or ALE of order $\tau$ if it has finitely many ends and for each end there exists a finite subgroup $\Gamma \subset \mathrm{O}(n)$ acting freely on $\mathbb{R}^{n} \backslash\{0\}$ and a diffeomorphism $\psi: X \backslash K \rightarrow\left(\mathbb{R}^{n} \backslash \overline{B_{R}(0)}\right) / \Gamma$ where $K$ is a compact subset of $X$, and such that under this identification,
$$\begin{aligned}
\left(\psi_{*} g\right)_{i j} & =\delta_{i j}+O\left(\rho^{-\tau}\right), \\
\partial^{k}\left(\psi_{*} g\right)_{i j} & =O\left(\rho^{-\tau-|k|}\right),
\end{aligned}$$
for any partial derivative of order $|k|$, as $\rho \rightarrow \infty$, where $\rho$ is the distance to some fixed basepoint.
We will occasionally refer to an AF metric as an ALE metric, since AF is exactly the case of ALE with $\Gamma=\{e\}$. Next, we give the definition of the ADM mass on asymptotically locally Euclidean (ALE) orbifolds.
Definition 1.5. Given an $n$-dimensional ALE orbifold $(X, g)$ with asymptotic coordinates $\left\{z^{i}\right\}$ and quotient group $\Gamma$ near $\infty$, define the ADM mass as follows:
$$\left.m(g)=\frac{|\Gamma|}{V o l\left(S^{n-1}\right)} \lim _{r \rightarrow \infty} \int_{S_{r} / \Gamma} \sum_{i, j=1}^{n}\left(\partial_{i} g_{i j}-\partial_{j} g_{i i}\right)\left(\partial_{j}\right\lrcorner d V_{z}\right),$$
where $S_{r} / \Gamma$ is the hypersurface at $|z|=r$, and $d V_{z}$ is the Euclidean volume element.
Remark 1.6. Bartnik proved that in the AF case, if $\tau>(n-2) / 2$ then the mass is well-defined and independent of the choice of coordinates at infinity [Bar86]. A similar argument shows that the same result holds in the ALE case.

Remark 1.7. Note that if $|\Gamma|=\{e\}$ is the trivial group, the formula above defines the mass for AF orbifold ( $X, g$ ), which is consistent with [LP87, Definition 8.2]. Note also that if $\Gamma \neq\{e\}$, our coefficient differs from [HL16] due to the factor of $|\Gamma|$. Our convention has the advantage that it eliminates the need for writing extra factors of $|\Gamma|$ in several formulas.

For any Riemannian orbifold $(M, g)$ with positive scalar curvature, we can construct a scalar-flat ALE orbifold ( $X, \hat{g}$ ) by the following well-known procedure.
Definition 1.8. Take $g$-normal coordinates $\left\{x^{i}\right\}$ centered at point $\bar{x}$ and let $r=|x|$ denote the distance function. Let $\psi_{\bar{x}}>0$ be the Green's function of $L_{g}$ with leading term $r^{2-n}$ near $\bar{x}$. Then $\left(X_{\bar{x}}, \hat{g}_{\bar{x}}\right)=\left(M \backslash \bar{x}, \psi_{\bar{x}}^{4 /(n-2)} g\right)$ is a scalar flat ALE orbifold. We will refer to $\left(X_{\bar{x}}, \hat{g}_{\bar{x}}\right)$ as the conformal blow-up of $g$ at the point $\bar{x}$.

Of course, if $\bar{x}$ is a smooth point of $M$, then ( $X_{\bar{x}}, \hat{g}_{\bar{x}}$ ) is an AF orbifold, but if $\bar{x}$ is a singular point, then $\left(X_{\bar{x}}, \hat{g}_{\bar{x}}\right)$ is an ALE orbifold.
1.1. Positive Mass Theorem on AF orbifolds. Our first result is that the positive mass theorem does hold for AF orbifolds.

Theorem 1.9. Let $\left(X, g_{X}\right)$ be an asymptotically flat $(A F)$ n-dimensional Riemannian orbifold with finitely many isolated singular points, with $R\left(g_{X}\right) \geq 0$, and which is of order $\tau_{X}>\frac{n-2}{2}$. Then $\operatorname{mass}\left(g_{X}\right) \geq 0$. and $\operatorname{mass}\left(g_{X}\right)=0$ if and only if there are no nontrivial orbifold singularities, and $\left(X, g_{X}\right)$ is isometric to $\left(\mathbb{R}^{n}, g_{\text {Euc }}\right)$.

This is proved in Section 2. The basic idea is to use a certain Green's function for the Laplacian based at the orbifold points, which we use to reduce to the positive mass theorem for manifolds with concave boundary due to Hirsch-Miao [HM20] using the fundamental work of Schoen-Yau [SY79, SY81, SY17].
Remark 1.10. The positive mass theorem holds on ALE spaces only with some extra assumptions; see for example [Nak90]. In contrast, the positive mass theorem does not necessarily hold for arbitrary ALE metrics with nonnegative scalar curvature. The first examples were given in LeB88], and many more in [HL16]. Theorem 1.9 shows that the study of the Yamabe equation on orbifolds can be substantially different from the manifold case. In dimension 4, we can define a mass function $m: M \rightarrow \mathbb{R}$ by assigning the mass of the conformal blow-up at $\bar{x} \in M$. In the manifold case, this is a smooth function [Hab00]. However, the above result shows that if $(M, g)$ is an orbifold and the conformal blow-up has negative mass at $\bar{x} \in \Sigma$, then the mass function $m$ is necessarily discontinuous at $\bar{x}$; see Corollary 2.2 below.
1.2. Existence and compactness results. There is a long history of existence and compactness results for the Yamabe problem, which is the case when $K=$ constant . The fundamental idea for compactness was due to Schoen [Sch89b, Sch91, Sch89a]; compactness results for the Yamabe problem in low dimensions were then proved in [Dru03, KMS09, LZ05, LZ99, Mar05]. As mentioned above, existence and compactness results for variable $K$ have been studied in great detail on $S^{n}$ and on manifolds. Our next result generalizes many of these results in dimension four to the case of a Riemannian orbifold.

Theorem 1.11. Let $(M, g)$ be a compact Riemannian 4-dimensional orbifold with positive scalar curvature. Let $K \in C^{2}(M)$ satisfy
$$\begin{aligned}
& 0<\delta_{1} \equiv \inf _{M} K, \\
& 0<\delta_{2} \equiv \inf _{\bar{x} \in \operatorname{Crit}(K)}\left|m\left(\hat{g}_{\bar{x}}\right)+\frac{\Delta_{g} K(\bar{x})}{2 K(\bar{x})}\right| .
\end{aligned}$$
Then there exists some constant $C$ depending only on $M, g, \delta_{1}, \delta_{2},\|K\|_{C^{2}(M)}$ such that
$$1 / C \leq u \leq C \quad \text { and } \quad\|u\|_{C^{2, \alpha}(M)} \leq C$$
for all solutions $u$ of (1.3) with $p=3$, where $0<\alpha<1$. Moreover, if
$$0<\delta_{3} \equiv \inf _{\bar{x} \in \operatorname{Crit}(K)}\left(m\left(\hat{g}_{\bar{x}}\right)+\frac{\Delta_{g} K(\bar{x})}{2 K(\bar{x})}\right),$$
then (1.9) holds for all $1<1+\varepsilon<p \leq 3$ where $C$ in addition depends upon $\delta_{3}, \epsilon$. Consequently, in this case there exists a solution $u$ of (1.3) with $p=3$.

Theorem 1.11 will be proved in Sections 3, 4, and 5. One of the main difficulties is due to the "discontinuity" of conformal normal coordinates at an orbifold point. In Section 5, we will show that if concentration of a sequence $u_{k}$ happens at an orbifold point, then the local maxima of $u_{k}$ must occur exactly at the orbifold point for $k$ sufficiently large; see Condition 3.7 which is a generalization of the isolated simple blow-up condition. Once we prove that blow-up points satisfy Condition 3.7, we can then fix the coordinates to be centered at the orbifold point, and then there is a contribution only from the mass function at the blow-up point. Note: our argument does not need continuity of the mass function which, as pointed out above, is not true in general anyway.

Remark 1.12. We emphasize that under the assumption (1.8), we are only claiming compactness; we do not have the existence in this general case. The main reason is that the subcritical method only works under the stronger assumption (1.10). However, the compactness result does allow one to define the Leray-Schauder degree. We expect that by imposing extra assumptions on $K$, one should be able to prove this degree is non-zero in some cases where (1.10) does not hold, but we do not pursue this here. Results along this line in the manifold case can be found in [BACCH96, Li96, MM20, May17].
1.3. Variational methods. Next, we have another existence result in dimensions $n \geq 4$ which is proved using variational methods. Roughly, this says that if $K$ is not too large away from the orbifold points, then we need assumption (1.10) to hold at only one orbifold point.

Theorem 1.13. Let $(M, g)$ be a compact Riemannian $n$-dimensional orbifold with singularities $\Sigma_{\Gamma}=\left\{\left(q_{1}, \Gamma_{1}\right), \cdots,\left(q_{l}, \Gamma_{l}\right)\right\}$ and positive scalar curvature. Let $K$ be a positive smooth function on $M$. Assume that
$$\max _{1 \leq i \leq l}\left\{\left|\Gamma_{i}\right|^{\frac{2}{n-2}} K\left(q_{i}\right)\right\} \geq \sup K,$$
and
$$\begin{cases}m\left(\hat{g}_{q_{i_{0}}}\right)+\frac{\Delta_{g} K\left(q_{i_{0}}\right)}{2 K\left(q_{i_{0}}\right)}>0, & n=4, \\ \Delta_{g} K\left(q_{i_{0}}\right)>0, & n \geq 5,\end{cases}$$
for some $i_{0}$ such that $\left|\Gamma_{i_{0}}\right|^{\frac{2}{n-2}} K\left(q_{i_{0}}\right)=\max _{1 \leq i \leq l}\left\{\left|\Gamma_{i}\right|^{\frac{2}{n-2}} K\left(q_{i}\right)\right\}$, where $\hat{g}_{q_{i_{0}}}$ is as in Definition 1.8. Then there exists a positive smooth solution of equation (1.3) with $p=\frac{n+2}{n-2}$.

This will be proved in Section 6, which is closely related to [ES86, Theorem 2.1], [Aku12, Theorem 3.1] and [MM21, Proposition 5.1]. The analogue on manifolds is that (1.12) has to hold at one maximum point of $K$, which is only possible in dimension $n=4$. Hence the theorem is quite special to the orbifold case in dimensions $n \geq 5$. We next apply this to some examples.

Consider $S^{n} \subset \mathbb{R}^{n+1}$, and let $\Gamma \subset \operatorname{SO}(n)$ be a finite subgroup acting freely on $S^{n-1} \subset S^{n} \cap$ $\left\{x_{n+1}=0\right\}$. Then $S^{n} / \Gamma$ with the spherical metric $g_{S}$ is a Riemannian orbifold with 2 orbifold points $q_{1}$ and $q_{2}$.

Corollary 1.14 (Spherical football orbifold). With $\Gamma$ as above, let $K: S^{n} / \Gamma \rightarrow \mathbb{R}_{+}$be a smooth function and without loss a generality assume that $K\left(q_{1}\right) \geq K\left(q_{2}\right)$. If
$$\begin{aligned}
|\Gamma|^{\frac{2}{n-2}} K\left(q_{1}\right) & \geq \sup K, \\
\Delta_{g_{S}} K\left(q_{1}\right) & >0,
\end{aligned}$$
then there exists a positive smooth solution of equation (1.3) with $g=g_{S}$ and $p=\frac{n+2}{n-2}$.

We note that for $|\Gamma|=2$, this result also follows from [LZ14, Theorem 1.12]. Another non-trivial example to which Theorem 1.13 applies is to the Calabi metric $g_{C A L(n)}$, which is a $U(n)$-invariant Ricci-flat Kähler ALE metric on the total space $X_{n}$ of the line bundle $\mathcal{O}(-n) \rightarrow \mathbb{P}^{n-1}$. For details on the Calabi metric, see for example [MV20].
Corollary 1.15 (Calabi orbifold). For $n \geq 2$, take a $U(n)$-invariant conformal compactification $\left(\check{X}_{n}, \check{g}_{C A L(n)}\right)$ of the Calabi metric $\left(X_{n}, g_{C A L(n)}\right)$, such that the infinity of $g_{C A L(n)}$ is compactified to an orbifold point $\check{q}$, with quotient group $\mathbb{Z} / n \mathbb{Z}$. Let $K$ be a positive smooth function on $\check{X}_{n}$. Assume that
$$\begin{aligned}
n^{\frac{1}{n-1}} K(\check{q}) & \geq \sup K, \\
\Delta_{\check{g}_{C A L(n)}} K(\check{q}) & >0,
\end{aligned}$$
then there exists a positive smooth solution of equation (1.3) with $g=\check{g}_{C A L(n)}$ and $p=\frac{n+1}{n-1}$.
Remark 1.16. In this case, from Theorem 1.3 and Remark 4.7 in [Via10], we know that there is no solution with $K=$ constant $>0$, which certainly does not contradict with the condition on the Laplacian at the orbifold point. However, Corollary 1.15 implies that any sufficiently small perturbation of a constant satisfying $\Delta_{\check{g}_{C A L(n)}} K(\check{q})>0$ does admit a solution. So the case of $K=$ constant is right on the boundary of existence. Furthermore, if we take a sequence of functions $K_{k}$ satisfying (1.16), but converging to a positive constant in $C^{2}$ norm, then this gives an example where bubbling must occur as $k \rightarrow \infty$.

For $n=2,\left(X_{2}, g_{C A L(2)}\right)$ is also known as the Eguchi-Hanson metric, which is included in the family of LeBrun metrics, which we discuss next.
1.4. LeBrun metrics. In this subsection, we will use the previous results to analyze the prescribed scalar curvature problem on the family of orbifolds mentioned above: the LeBrun negative mass metrics on $\mathcal{O}_{\mathbb{P}^{1}}(-n)$. Note: these are 4-dimensional manifolds, so in this subsection the integer $n$ will instead be used to denote $-c_{1}$, where $c_{1}$ is the first Chern class of this line bundle. These metrics possess an isometric U(2)-action. As we will see below, we have some results in the general case, but our most complete results are under a U(2)-symmetry assumption.

In [LeB88], LeBrun presented the first known example of a scalar-flat ALE metric of negative ADM mass. For any $n \in \mathbb{N}^{*}$, define
$$g_{L E B(n)}=\frac{1+\hat{r}^{2}}{n+\hat{r}^{2}} d \hat{r}^{2}+\left(1+\hat{r}^{2}\right) \sigma_{1}^{2}+\left(1+\hat{r}^{2}\right) \sigma_{2}^{2}+\frac{\hat{r}^{2}\left(n+\hat{r}^{2}\right)}{1+\hat{r}^{2}} \sigma_{3}^{2},$$
where $\hat{r} \in(0, \infty)$ is the radial coordinate, and $\left\{\sigma_{1}, \sigma_{2}, \sigma_{3}\right\}$ is a left-invariant coframe on $S^{3}=S U(2)$. Attach a $\mathbb{P}^{1}$ at $\hat{r}=0$. After taking a quotient by $\Gamma_{n}=\mathbb{Z} / n \mathbb{Z}$, the metric extends smoothly over this $\mathbb{P}^{1}$. Furthermore, the metric is ALE with group action $\Gamma_{n}$ near $\hat{r}=\infty$ and the resulting manifold is diffeomorphic to $\mathcal{O}_{\mathbb{P}^{1}}(-n)$.

The mass term defined in [LeB88] differs from our Definition 1.5 by a scaling factor. With a modification of the mass computed in [LeB88], we obtain
$$m\left(g_{L E B(n)}\right)=-2(n-2) .$$
For any $n \in \mathbb{N}^{*}, g_{L E B(n)}$ is scalar-flat. Note that $g_{L E B(1)}$ is conformal to the Fubini-Study metric on $\mathbb{P}^{2}$, and is known as the Burns metric, which is AF and has positive mass. As pointed out above, $g_{L E B(2)}$ is the Eguchi-Hanson metric, which is Ricci-flat ALE and has zero mass. For any $n \geq 3, g_{L E B(n)}$ has negative mass. More details and properties of LeBrun metrics can be found in [DL16, LeB88, Via10].

We next choose an orbifold compactification by defining
$$\check{g}_{L E B(n)}=\frac{1}{\left(n+\hat{r}^{2}\right)^{2}} \cdot g_{L E B(n)} .$$

Then $\left(\check{\mathcal{O}}_{\mathbb{P}^{1}}(-n), \check{g}_{L E B(n)}\right)$ is a compact orbifold with singular point $\check{q}$ at $\hat{r}=\infty$ with quotient group $\Gamma_{n}$. Its scalar curvature is computed to be
$$R_{\check{g}_{L E B(n)}}=\frac{24 n\left(n+\hat{r}^{2}\right)}{1+\hat{r}^{2}}>0 .$$
In this case, Theorem 1.13 specializes to the following.
Theorem 1.17. Consider $\left(\check{\mathcal{O}}_{\mathbb{P}^{1}}(-n), \check{g}_{L E B(n)}\right)$ for $n \in \mathbb{N}^{*}$. Let $K$ be a positive smooth function such that
$$\begin{aligned}
\sup K & \leq n K(\check{q}), \\
4(n-2) K(\check{q}) & <\Delta_{\check{g}_{L E B(n)}} K(\check{q}) .
\end{aligned}$$
Then there exists a positive smooth solution of equation (1.3) with $g=\check{g}_{L E B(n)}$ and $p=3$.
Next, we turn to the U(2)-invariant problem. Define a function space $\mathcal{X}_{n}$
$$\mathcal{X}_{n}=\left\{K: \check{O}_{\mathbb{P}^{1}}(-n) \rightarrow \mathbb{R} \mid K \text { is smooth, } \mathrm{U}(2) \text {-invariant, and } K>0\right\} .$$
Given any $K \in \mathcal{X}_{n}$, we are asking whether there exists a solution $u \in \mathcal{X}_{n}$ of the equation
$$-\Delta_{\check{g}_{L E B(n)}} u+\frac{1}{6} R_{\check{g}_{L E B(n)}} u=K u^{3} .$$
Decompose $\mathcal{X}_{n}$ into three disjoint subsets
$$\begin{aligned}
& \mathcal{X}_{n,+}=\left\{K \in \mathcal{X}_{n}: \Delta_{\check{g}_{L E B(n)}} K(\check{q})-4(n-2) K(\check{q})>0\right\}, \\
& \mathcal{X}_{n, 0}=\left\{K \in \mathcal{X}_{n}: \Delta_{\check{g}_{L E B(n)}} K(\check{q})-4(n-2) K(\check{q})=0\right\}, \\
& \mathcal{X}_{n,-}=\left\{K \in \mathcal{X}_{n}: \Delta_{\check{g}_{L E B(n)}} K(\check{q})-4(n-2) K(\check{q})<0\right\} .
\end{aligned}$$
Define a function space
$$\Omega_{\Lambda, n}=\left\{u \in \mathcal{X}_{n}:\|u\|_{C^{2, \alpha}\left(\check{\mathcal{O}}_{\mathbb{P}}(-n)\right)}<\Lambda, u>\Lambda^{-1}\right\},$$
and a map
$$F_{p, K, n}: \bar{\Omega}_{\Lambda, n} \rightarrow C^{2, \alpha}\left(\check{\mathcal{O}}_{\mathbb{P}^{1}}(-n)\right) \text { by } F_{p, K, n}(u)=u+L_{\check{g}_{L E B(n)}}^{-1}\left(K u^{p}\right),$$
where $L_{\check{g}_{L E B(n)}}=\Delta_{\check{g}_{L E B(n)}}-\frac{1}{6} R_{\check{g}_{L E B(n)}}$. Similar to [Sch84, LZ05, LZ99, KMS09, Mar05], we can define the U(2)-invariant Leray-Schauder degree of $F_{p, K, n}$ in the region $\Omega_{\Lambda, n}$ with respect to $0 \in C^{2, \alpha}\left(\check{\mathcal{O}}_{\mathbb{P}^{1}}(-n)\right)$, which we denote by $\operatorname{deg}_{\mathrm{U}(2)}\left(F_{p, K, n}, \Omega_{\Lambda, n}, 0\right)$. Using Theorem 1.11 and some other special techniques, we present our last theorem, which gives a complete understanding of the U(2)-invariant Leray-Schauder degree.

Theorem 1.18. For any $n \in \mathbb{N}^{*}$, there exists a constant $C$, depending only on $\left(\check{\mathcal{O}}_{\mathbb{P}^{1}}(-n), \check{g}_{L E B(n)}\right)$ such that we have the following conclusions.
(1) For all $K \in \mathcal{X}_{n,+}$ and $\Lambda>C$, we have
$$\operatorname{deg}_{\mathrm{U}(2)}\left(F_{3, K, n}, \Omega_{\Lambda, n}, 0\right)=-1 .$$
Consequently, equation (1.23) admits at least one U(2)-invariant solution in $\mathcal{X}$.
(2) For all $K \in \mathcal{X}_{n,-}$ and $\Lambda>C$, we have
$$\operatorname{deg}_{\mathrm{U}(2)}\left(F_{3, K, n}, \Omega_{\Lambda, n}, 0\right)=0 .$$

Remark 1.19. We note that vanishing of the Leray-Schauder degree does not give any information regarding the existence of a solution. However, we can moreover show that there is no solution at all for a large class of functions in $\mathcal{X}_{n,-}$; see Theorem 7.3. In particular, there is no solution for $K=$ constant when $n \geq 2$. For $n=2$ and $K=$ constant, nonexistence of any solution (symmetric or non-symmetric) was proved in [Via10]. However, it is still an open question whether the case $K=$ constant possibly admits some non-symmetric solution when $n>2$.

Remark 1.20. For any $n \in \mathbb{N}^{*}$, the set $\mathcal{X}_{n, 0}$ can be viewed as a "wall" in the space of positive radial functions $\mathcal{X}_{n}$, and the Leray-Schauder degree jumps by 1 upon crossing this wall, which is a phenomenon observed in many other geometric PDE problems.

All of the above results regarding the LeBrun metrics are proved in Section 7.
1.5. Acknowledgements. The authors would like to thank Richard Schoen for suggesting to consider the Green's function on an AF orbifold to prove Theorem 1.9; this greatly simplified our original proof which was based on a resolution of singularities argument.

\section*{2. Properties of the mass}

In this section, we will prove Theorem 1.9. For simplicity, let us assume that there is exactly 1 orbifold point, which we denote as $q$, with orbifold group $\Gamma \subset \mathrm{O}(n)$ (the argument below easily generalizes to the case of multiple orbifold singularities). Let $r$ denote a positive smooth function which is the Euclidean distance in the AF coordinate system, and near $q$ is the distance to $q$. We will first prove a lemma showing existence of a certain harmonic function on $X \backslash\{q\}$.

Lemma 2.1. There exists a unique harmonic function $H: X \backslash\{q\} \rightarrow \mathbb{R}$ which satisfies $H>1$ and admits the expansion
$$H=\left\{\begin{array}{ll}
r^{2-n}+O\left(r^{4-n-\epsilon}\right) & \text { as } r \rightarrow 0 \\
1+A r^{2-n}+O\left(r^{2-n-\epsilon}\right) & \text { as } r \rightarrow \infty
\end{array},\right.$$
for $\epsilon>0$ sufficiently small, for some constant $A>0$.
Proof. Let $\phi$ be the cutoff function
$$\phi(t)=\left\{\begin{array}{ll}
1 & t \leq 1 \\
0 & t \geq 2
\end{array},\right.$$
and consider
$$h_{0}=\phi\left(r / r_{0}\right) r^{2-n},$$
for $r_{0}>0$ small. Since $h_{0}$ is harmonic with respect to the Euclidean metric near point $q$, by expanding $\Delta_{g}$ at the Euclidean metric, it is not hard to see that
$$\Delta_{g} h_{0}=\left\{\begin{array}{ll}
O\left(r^{2-n}\right) & r \rightarrow 0 \\
0 & r \geq 2 r_{0}
\end{array} .\right.$$
Denote $X_{q}=X \backslash\{q\}$. The argument below uses weighted Hölder space theory; for background we refer to [Bar86, LP87]. Consider the doubly weighted Hölder space $C_{\delta_{0}, \delta_{\infty}}^{k, \alpha}\left(X_{q}\right)$, which satisfies if $u \in C_{\delta_{0}, \delta_{\infty}}^{k, \alpha}\left(X_{q}\right)$ then
$$u=\left\{\begin{array}{ll}
O\left(r^{\delta_{0}}\right) & r \rightarrow 0 \\
O\left(r^{\delta_{\infty}}\right) & r \rightarrow \infty
\end{array} .\right.$$
For any $\epsilon>0$, from (2.4), we have
$$\Delta h_{0} \in C_{2-n-\epsilon,-n+\epsilon}^{k-2, \alpha} .$$
Consider the operator
$$\Delta_{g}: C_{4-n-\epsilon, 2-n+\epsilon}^{k, \alpha}\left(X_{q}\right) \rightarrow C_{2-n-\epsilon,-n+\epsilon}^{k-2, \alpha}\left(X_{q}\right) .$$
The adjoint operator has domain $\left(C_{2-n-\epsilon,-n+\epsilon}^{k-2, \alpha}\left(X_{q}\right)\right)^{*}$, and kernel elements lie in the doubly weighted space $C_{-2+\epsilon,-\epsilon}^{k, \alpha}\left(X_{q}\right)$. The removable singularity theorem then says that a kernel element $u$ in this
space extends to $X$, and then $u \in C_{-\epsilon}^{k, \alpha}(X)$ (the weighted space on $X$ with only a weight $\delta_{\infty}=-\epsilon$ at infinity), so $u \equiv 0$. Thus for $\epsilon>0$ sufficiently small, the operator in (2.7) is surjective, and we can solve for $\Delta h_{\epsilon}=\Delta_{g} h_{0}$, with $h_{\epsilon} \in C_{4-n-\epsilon, 2-n+\epsilon}^{k, \alpha}\left(X_{q}\right)$.

The function $h \equiv h_{0}-h_{\epsilon}$ satisfies $\Delta_{g} h=0$, and by the existence of a harmonic expansion near $\infty$, it admits the expansion.
$$h=\left\{\begin{array}{ll}
r^{2-n}+O\left(r^{4-n-\epsilon}\right) & r \rightarrow 0 \\
A r^{2-n}+O\left(r^{2-n-\epsilon}\right) & r \rightarrow \infty
\end{array},\right.$$
for some constant $A$. We then define $H=1+h$, which is harmonic. We have that $\lim _{r \rightarrow \infty} H=1$, and $\lim _{r \rightarrow 0} H=+\infty$. If $H$ were not strictly larger than 1, then it would have an interior minimum. The strong maximum principle would then imply that $H$ is constant, which is impossible. So $H>1$, which clearly implies that $A>0$. Obviously, $H$ is unique. \(\square\)

Proof of Theorem 1.9. For any constant $\delta>0$, we define
$$H_{\delta}=\delta H+(1-\delta),$$
which satisfies $\Delta_{g} H_{\delta}=0, H_{\delta}>1$, and admits the expansion
$$H_{\delta}=\left\{\begin{array}{ll}
\delta r^{2-n}+O\left(r^{4-n-\epsilon}\right) & r \rightarrow 0 \\
1+\delta A r^{2-n}+O\left(r^{2-n-\epsilon}\right) & r \rightarrow \infty
\end{array},\right.$$
for $\epsilon>0$ sufficiently small, for the fixed constant $A$ from Lemma 2.1.
Next, we consider the metric $\left(X_{q}, g_{\delta}\right)=\left(X \backslash\{q\}, H_{\delta}^{\frac{4}{n-2}} g_{X}\right)$. Near $r \sim \infty, g_{\delta}$ has a single AF end of order $\min \left\{\tau_{X}, n-2\right\}$. Since $q$ is an orbifold point, near $q, g_{\delta}$ has a single ALE end of order $\tau=2-\epsilon$. To see this, choose Riemannian normal coordinates $\left\{x^{i}\right\}$ for $g_{X}$ around $q$, then we have the expansions
$$\begin{aligned}
& g_{X}=d x^{2}+O\left(|x|^{2}\right) \\
& H_{\delta}=\delta|x|^{2-n}+O\left(|x|^{4-n-\epsilon}\right),
\end{aligned}$$
which yield the expansion
$$g_{\delta}=H_{\delta}^{\frac{4}{n-2}} g_{X}=\delta^{\frac{4}{n-2}}|x|^{-4}\left(1+O\left(|x|^{2-\epsilon}\right)\right)^{\frac{4}{n-2}}\left(d x^{2}+O\left(|x|^{2}\right)\right),$$
as $|x| \rightarrow 0$. Next, define coordinates $y$ by
$$y=\delta^{\frac{2}{n-2}} \frac{x}{|x|^{2}} .$$
A computation then shows that
$$g_{\delta}=d y^{2}+O\left(|y|^{-2+\epsilon}\right)$$
as $|y| \rightarrow \infty$, so $g_{\delta}$ is indeed ALE of order $\tau=2-\epsilon$. Note also that the scalar curvature of $g_{\delta}$ is given by
$$R\left(g_{\delta}\right)=c(n)^{-1} H_{\delta}^{-\frac{n+2}{n-2}}\left(-\Delta_{g} H_{\delta}+c(n) R_{g} H_{\delta}\right)=H_{\delta}^{-\frac{4}{n-2}} R_{g} \geq 0 .$$
Given $\delta>0$, we can choose a very large distance sphere $\Sigma_{\delta}$ in the ALE end of $g_{\delta}$ which is strictly concave with respect to the normal pointing to the AF end. Let $X_{\Sigma_{\delta}}$ be the manifold with boundary obtained by removing the ALE end outside of $\Sigma$, which is a manifold with strictly concave boundary with a single AF end. From [HM20, Theorem 1.5 and Remark 1.7], we conclude that
$$m\left(X_{\Sigma_{\delta}}, g_{\delta}\right) \geq 0 .$$
But an easy computation shows that
$$m\left(X_{\Sigma_{\delta}}, g_{\delta}\right)=m\left(X, g_{X}\right)+b(n) \delta A,$$
where $b(n)>0$ is a dimensional constant. Since this is true for any constant $\delta>0$, and $A$ is a fixed constant, we conclude that
$$m\left(X, g_{X}\right) \geq 0 .$$
Note that if $m\left(X, g_{X}\right)=0$, then we cannot conclude that $m\left(X_{\Sigma_{\delta}}, g_{\delta}\right)=0$, since $A>0$. Therefore we cannot directly use the equality case in [HM20, Theorem 1.5]. So to finish the proof, if $\operatorname{mass}\left(X, g_{X}\right)=0$ then we instead argue as in [LP87, Lemma 10.7] to conclude that $g_{X}$ is Ricci-flat (this argument is valid in our orbifold setting). Since $g_{X}$ is asymptotically flat, we have asymptotic equality in Bishop's volume inequality (which holds for orbifolds; see [Bor92]). This implies that $g_{X}$ is flat, which clearly implies that there can be no nontrivial orbifold singularities, and $\left(X, g_{X}\right)$ is isometric to $\left(\mathbb{R}^{n}, g_{E u c}\right)$. \(\square\)

As mentioned above, in dimension 4, there are examples of ALE spaces which have negative mass [LeB88, HL16]. So we note the following corollary of Theorem 1.9.

Corollary 2.2. If $(X, g)$ is a 4-dimensional Riemannian orbifold with negative mass at an orbifold point $q$, then the mass function $m: X \rightarrow \mathbb{R}$ is necessarily discontinuous at $q$.
2.1. Odd-dimensional cases. If the dimension $n$ is odd, we have the following.

Proposition 2.3. Let $(X, g)$ is a compact Riemannian orbifold with isolated singularities and odd-dimensional. Then any nontrivial orbifold point must have $\Gamma=\mathbb{Z} / 2 \mathbb{Z}$. Furthermore, ( $X, g$ ) is a good orbifold. That is, there is a $\mathbb{Z} / 2 \mathbb{Z}$ action on a compact manifold $\tilde{X}$ with finitely many fixed points such that $X=\tilde{X} /(\mathbb{Z} / 2 \mathbb{Z})$. Letting $\pi: \tilde{X} \rightarrow X$ denote the quotient mapping, then $\pi^{*} g$ is a smooth Riemannian metric on $\tilde{X}$.

Proof. For $n$ odd, any element $A \in \mathrm{O}(n)$ must have ±1 as an eigenvalue, so the only possibility for a nontrivial orbifold point is $\Gamma=\mathbb{Z} / 2 \mathbb{Z}$. Near any singular point $q$, a small distance sphere is homeomorphic to $\mathbb{R P}^{n-1}$, which is non-orientable if $n$ is odd. So if there is any nontrivial orbifold point, then $X$ contains a non-orientable 2-sided hypersurface, which implies that $X \backslash \Sigma$ is non-orientable, where $\Sigma$ is the finite set of singular points. Let $\pi: X^{\prime} \rightarrow X \backslash \Sigma$ denote the orientable double cover. Consider $\tilde{X}=X^{\prime} \cup\left\{\tilde{q}_{1}, \ldots, \tilde{q}_{j}\right\}$ where $\tilde{q}_{j}$ are points, and extend $\pi: \tilde{X} \rightarrow X$ by letting $\pi\left(\tilde{q}_{j}\right)=q_{j}$. We extend to $\mathbb{Z} / 2 \mathbb{Z}$ action to $\tilde{X}$ with fixed points at $\tilde{q}_{j}$, and endow $\tilde{X}$ with the quotient topology. It is then straightforward to show that $\tilde{X}$ is a smooth manifold and $\pi^{*} g$ extends as a smooth Riemannian metric to $\tilde{X}$. \(\square\)

Corollary 2.4. Let $(X, g)$ be a compact Riemannian orbifold with isolated singularities and odd-dimensional. Then the mass function $m: X \rightarrow \mathbb{R}$ satisfies $m>0$ everywhere, unless $(X, g)$ is conformal to $\left(S^{n}, g_{\text {round }}\right)$ or a "football" metric $S^{n} /(\mathbb{Z} / 2 \mathbb{Z})$ with exactly 2 singular points.

Proof. At any smooth point of $X$, the mass of the Green's function metric is positive by Theorem 1.9. If the mass at a smooth point were zero, then the Green's function metric would be Euclidean space, which would imply that $(X, g)$ is conformal to $\left(S^{n}, g_{\text {round }}\right)$. At a singular point $q$, by uniqueness of the Green's function metric, the Green's function metric at $q$ must be the $\mathbb{Z} / 2 \mathbb{Z}$ quotient of the Green's function of $\left(\tilde{X}, \pi^{*} g\right)$ at $\tilde{q}$. Since $\tilde{X}$ is a manifold, by the usual positive mass theorem, the Green's function metric upstairs must have non-negative mass, so the Green's function downstairs must also. If the mass at an orbifold point was 0, then the Green's function metric upstairs would have to be Euclidean space. This implies that the Green's function metric downstairs is a $\mathbb{Z} / 2 \mathbb{Z}$-quotient of Euclidean space, which implies that $(X, g)$ is conformal to a "football" metric $S^{n} /(\mathbb{Z} / 2 \mathbb{Z})$. \(\square\)

The above remarks show that the odd-dimensional case of the orbifold Yamabe problem is equivalent to the $\mathbb{Z} / 2 \mathbb{Z}$-equivariant Yamabe problem on the manifold $\tilde{X}$.

\section*{3. Compactness preliminaries}

Remarkable work in analyzing the blow-up points of equation (1.3) has been done in Mar05, [LZ05], [LZ99], [KMS09]. In this section, we are going to quote some of their definitions and local results on manifolds, which also appear to hold on orbifolds by modification of proofs.

In the following context, we will write $\mathbb{R}^{n} / \Gamma$ or $B_{r}(\bar{x}) / \Gamma$. If $\Gamma=\{e\}$ is the trivial group, it denotes the Euclidean space or a smooth ball; if $\Gamma \neq\{e\}$ is a finite nontrivial group in $O(n)$, it denotes the Euclidean cone or a quotient of a ball centered at a singular point $\bar{x}$.
3.1. Conformal scalar curvature equation. Instead of dealing with equation (1.3), we will study the following conformal scalar curvature equation. Let $\Omega \subset \mathbb{R}^{n} / \Gamma$ be an open neighborhood of the origin, and suppose $g$ is a Riemannian metric in $\Omega$. Suppose also $f$ is a positive $C^{1}$ function defined in $\Omega$. Consider a positive $C^{2}$ function $u$ satisfying
$$L_{g} u+K f^{-\tau} u^{p}=0,$$
where $K$ is a positive $C^{2}$ function, $1<p \leq \frac{n+2}{n-2}$ and $\tau=\frac{n+2}{n-2}-p$.
We note that (3.1) is scale invariant. To see this, let $u$ be a solution to equation (3.1). For any $s>0$, define the rescaled solution $v(y)=s^{\frac{2}{p-1}} u(s y)$. Then $L_{h} v+\tilde{K} \tilde{f}^{-\tau} v^{p}=0$, where $\tilde{K}(y)=K(s y), \tilde{f}(y)=f(s y)$ and the components in metric $h$ in normal coordinates are given by $h_{i j}(y)=g_{i j}(s y)$. Note that $v$ satisfies an equation of the same type as equation (3.1).

We also note that (3.1) is conformally invariant. To see this, suppose $\tilde{g}=\phi^{\frac{4}{n-2}} g$ is a metric conformal to $g$ and let $u$ be a solution to equation (3.1). Then $\phi^{-1} u$ satisfies $L_{\tilde{g}}\left(\phi^{-1} u\right)+$ $K(\phi f)^{-\tau}\left(\phi^{-1} u\right)^{p}=0$, which is again an equation of the same type.

These two properties, will be used later to take a rescaling of the coordinates and conformally map $g$ to some conformal normal metric, without changing the type of equation (3.1).
3.2. Pohozaev Identity. Suppose $u: B_{\sigma}(0) / \Gamma \rightarrow \mathbb{R}$ is a positive $C^{2}$ solution to the equation
$$a^{i j}(x) \partial_{i j} u+b^{i}(x) \partial_{i} u+c(x) u+K(x) u^{p}=0,$$
where $p \neq-1, K \in C^{1}$ and $a^{i j}, b^{i}, c$ are continuous functions, $1 \leq i, j \leq n$. Define
$$P(r, u)=\int_{\{|x|=r\} / \Gamma}\left(\frac{n-2}{2} u \frac{\partial u}{\partial \sigma}-\frac{r}{2}|\nabla u|^{2}+r\left|\frac{\partial u}{\partial r}\right|^{2}\right) d \sigma(r),$$
for $0<r<\sigma$. Then, we have the following lemma.
Lemma 3.1 ([Mar05] Lemma 2.1). For all $0<r<\sigma$,
$$\begin{aligned}
P(r, u)= & -\int_{\{|x| \leq r\} / \Gamma}\left(x \cdot \nabla u+\frac{n-2}{2} u\right)\left(\left(a^{i j}-\delta^{i j}\right) \partial_{i j} u+b^{i} \partial_{i} u\right) d x \\
& +\int_{\{|x| \leq r\} / \Gamma}\left(\frac{1}{2} x \cdot \nabla c+c\right) u^{2} d x-\frac{r}{2} \int_{\{|x|=r\} / \Gamma} c u^{2} d \sigma(r) \\
& +\frac{1}{p+1} \int_{\{|x| \leq r\} / \Gamma}(x \cdot \nabla K(x)) u^{p+1} d x \\
& +\left(\frac{n}{p+1}-\frac{n-2}{2}\right) \int_{\{|x| \leq r\} / \Gamma} K(x) u^{p+1} d x \\
& -\int_{\{|x|=r\} / \Gamma} \frac{1}{p+1} K(x) r u^{p+1} d \sigma(r) .
\end{aligned}$$
3.3. Isolated and isolated simple blow-up points. Let $\Omega=B_{\sigma}(\bar{x}) / \Gamma$ be (a quotient of) an open ball centered at point $\bar{x}$. Suppose $\left\{g_{k}\right\}$ is a sequence of Riemannian metrics in $\Omega$ converging, in the $C_{\text {loc }}^{2}$ topology, to a metric $g$. Let $R_{k}$ denote the scalar curvature of $g_{k}$ and $R_{g}$ denote the scalar curvature of the limit metric $g$. Suppose $\left\{f_{k}\right\}$ is a sequence of positive $C^{1}$ functions converging in the $C_{\text {loc }}^{1}$ topology to a positive function $f$. Also suppose $\left\{K_{k}\right\}$ is a sequence of positive $C^{2}$ functions converging in the $C_{\text {loc }}^{2}$ topology to a positive function $K_{\infty}$. Consider a sequence of positive $C^{2}$ functions $u_{k}$ satisfying
$$L_{g_{k}} u_{k}+K_{k} f_{k}^{-\tau_{k}} u_{k}^{p_{k}}=0 \text { in } \Omega,$$
where $1+\epsilon_{0}<p_{k} \leq \frac{n+2}{n-2}$ for some $\epsilon_{0}>0$ and $\tau_{k}=\frac{n+2}{n-2}-p_{k}$.
Definition 3.2. Suppose $u_{k}$ is a sequence of positive functions satisfying equation (3.5). If $\Gamma=\{e\}$, define $\bar{x}$ to be an isolated blow-up point for $u_{k}$ if there exists a sequence $x_{k} \in \Omega$, converging to $\bar{x}$, so that: 1) $x_{k}$ is a local maximum point of $u_{k}$; 2) $M_{k}:=u_{k}\left(x_{k}\right) \rightarrow \infty$ as $k \rightarrow \infty$; 3) there exist $r, C>0$ such that $u_{k}(x) \leq C d_{g_{k}}\left(x, x_{k}\right)^{-\frac{2}{p_{k}-1}}$ for every $x \in B_{r}\left(x_{k}\right) \subset \Omega$, where $B_{r}\left(x_{k}\right)$ denotes the geodesic ball of radius $r$, centered at $x_{k}$, with respect to the metric $g_{k}$.

If $\Gamma \neq\{e\}$, let $\pi: B_{\sigma}(\bar{x}) \rightarrow B_{\sigma}(\bar{x}) / \Gamma$ be the projection map. We say that $\bar{x}$ is an isolated blow-up point for $u_{k}$ if $\pi^{*}(\bar{x})=\bar{x}$ is an isolated blow-up point for $\pi^{*}\left(u_{k}\right)$ in the lifting-up space.

Define
$$U_{c}(y)=\left(\frac{n(n-2)}{c}\right)^{\frac{n-2}{4}}\left(1+|y|^{2}\right)^{\frac{2-n}{2}}$$
on $\mathbb{R}^{n} / \Gamma$, where $c$ is some positive constant. It is not hard to check that
$$\Delta U_{c}(y)+c U_{c}^{\frac{n+2}{n-2}}(y)=0 .$$

Remark 3.3. From now on, for each $k$, assume that we work in $g_{k}$-normal coordinates $\left\{x^{i}\right\}$ centered at point $x_{k}$. Then, we will simply write $u_{k}(x)$ instead of $u_{k}\left(\exp _{x_{k}}(x)\right)$ and $|x|$ instead of $d_{g_{k}}\left(x, x_{k}\right)$.

Moreover, by [LP87, Theorem 5.1], there exists a conformal factor $\phi_{k}$, such that $\tilde{g}_{k}=\phi_{k}^{\frac{4}{n-2}} g_{k}$ is the conformal normal metric with conformal normal coordinates $\left\{\tilde{x}^{i}\right\}$ centered at $x_{k}$. Let $\tilde{u}_{k}=$ $\phi_{k}^{-1} u_{k}$. By the property that equation (3.1) is conformally invariant as stated in Section 3.1, $u_{k}$ and $\tilde{u}_{k}$ satisfies the same type of conformal scalar curvature equation (3.1). Hence we may assume $g_{k}$ is already the conformal normal metric and $\left\{x^{i}\right\}$ is already the conformal normal coordiantes centered at $x_{k}$.

Consider the change of variables
$$y=M_{k}^{\frac{p_{k}-1}{2}} x,$$
and define the rescaled metric and functions
$$\begin{aligned}
& \left(h_{k}\right)_{i j}(y)=\left(g_{k}\right)_{i j}\left(M_{k}^{-\frac{p_{k}-1}{2}} y\right), v_{k}(y)=M_{k}^{-1} u_{k}\left(M_{k}^{-\frac{p_{k}-1}{2}} y\right), \\
& \tilde{f}_{k}(y)=f_{k}\left(M_{k}^{-\frac{p_{k}-1}{2}} y\right), \tilde{K}_{k}(y)=K_{k}\left(M_{k}^{-\frac{p_{k}-1}{2}} y\right) \text { and } \tilde{R}_{k}(y)=R_{k}\left(M_{k}^{-\frac{p_{k}-1}{2}} y\right),
\end{aligned}$$
for $|y|<M_{k}^{\frac{p_{k}-1}{2}} r$, where $r$ is as in Definition 3.2. Using the property that equation (3.1) is rescale invariant as stated in Section 3.1, the rescaled functions satisfy
$$L_{h_{k}} v_{k}+\tilde{K}_{k} \tilde{f}_{k}^{-\tau_{k}} v_{k}^{p_{k}}=0 .$$
The following property holds for an isolated blow-up point.

Proposition 3.4 ([Mar05] Proposition 4.3). Assume $u_{k}$ is a sequence of positive functions satisfying equation (3.5) and $x_{k} \rightarrow \bar{x}$ is an isolated blow-up point. Moreover, if $\Gamma \neq\{e\}$, we require $x_{k}=\bar{x}$ for all large $k$ 's. Assume $p_{k} \rightarrow \frac{n+2}{n-2}$, then there exist $R_{k}^{\prime} \rightarrow \infty$ and $\epsilon_{k} \rightarrow 0$, such that after passing to a subsequence,
$$\left\|v_{k}(y)-U_{K_{\infty}(\bar{x})}(y)\right\|_{C^{2}\left(B_{R_{k}^{\prime}}(0)\right) / \Gamma} \leq \epsilon_{k},$$
and
$$\frac{R_{k}^{\prime}}{\log \left(M_{k}\right)} \rightarrow 0,$$
as $k \rightarrow \infty$.
Proof. The case $K_{k}=$ constant is proved in [Mar05, Proposition 4.3]. For variable $K_{k}$, because $K_{k} \rightarrow K_{\infty}$ in the $C_{\text {loc }}^{0}$ norm, $\tilde{K}_{k} \rightarrow K_{\infty}(\bar{x})$ in the $C_{\text {loc }}^{0}$ norm. By equation (3.10) and the proof of [Mar05, Proposition 4.3], after passing to a subsequence, $v_{k} \rightarrow v>0$ in $C_{\text {loc }}^{2}$ norm, which satisfies
$$\left\{\begin{array}{l}
\Delta v(y)+K_{\infty}(\bar{x}) v(y)^{p}=0, \quad y \in \mathbb{R}^{n} / \Gamma \\
v(0)=1, \quad \nabla v(0)=0,
\end{array}\right.$$
where $p=\lim _{k \rightarrow \infty} p_{k}$ and $\Delta$ denotes the Euclidean Laplacian. By [CGS89], we must have $p=\frac{n+2}{n-2}$, and $v(y)=U_{K_{\infty}(\bar{x})}(y)$. The proof of (3.12) is the same as in [Mar05]. \(\square\)

Remark 3.5. Under the same assumptions as Proposition 3.4, we also have
$$\left\|v_{k}(y)-U_{K_{k}\left(x_{k}\right)}(y)\right\|_{C^{2}\left(B_{R_{k}^{\prime}}(0)\right) / \Gamma} \leq \epsilon_{k},$$
which is simply because $U_{K_{k}\left(x_{k}\right)} \rightarrow U_{K_{\infty}(\bar{x})}$ uniformly in $\mathbb{R}^{n} / \Gamma$.
Definition 3.6. Suppose $u_{k}$ is a sequence of positive functions satisfying equation (3.5) and $x_{k} \rightarrow \bar{x}$ is an isolated blow-up point. If $\Gamma=\{e\}$, define
$$\bar{u}_{k}(r)=\frac{1}{\operatorname{Vol}\left(S^{n-1}\right) r^{n-1}} \int_{\partial B_{r}\left(x_{k}\right)} u_{k} d \sigma(r),$$
where we are using $g_{k}$-normal coordinates and integrating with respect to the Euclidean volume form. We say $x_{k} \rightarrow \bar{x}$ is an isolated simple blow-up point if there exists a real number $0<\rho<r$ such that the functions
$$\hat{u}_{k}(r) \equiv r^{\frac{2}{p_{k}-1}} \bar{u}_{k}(r)$$
have exactly one critical point in the interval $(0, \rho)$, for $k$ large.
If $\Gamma \neq\{e\}$, let $\pi: B_{\sigma}(\bar{x}) \rightarrow B_{\sigma}(\bar{x}) / \Gamma$ be the projection map. We say that $\bar{x}$ is an isolated simple blow-up point for $u_{k}$ if $\pi^{*}(\bar{x})$ is an isolated simple blow-up point for $\pi^{*}\left(u_{k}\right)$ in the lifting-up space.

Next, we give the special blow-up condition that we will work on.
Condition 3.7. Assume $u_{k}$ is a sequence of positive functions satisfying equation (3.5) and $x_{k} \rightarrow \bar{x}$ is an isolated simple blow-up point. Moreover, if $\Gamma_{\bar{x}} \neq\{e\}$, then we require that $x_{k}=\bar{x}$ for all $k$ sufficiently large.

Remark 3.8. In Condition 3.7, the main reason why we require $x_{k}=\bar{x}$ for all $k$ sufficiently large in the singular point case $\Gamma \neq\{e\}$ is the following. By assuming so, for each $k$, the geodesic ball centered at $x_{k}$ will be $B_{r}(\bar{x}) / \Gamma$. Then, when we later analyze some local integrals and let $k \rightarrow \infty$, we will not run into the case that integrals over smooth balls converge to an integral over a quotient of a smooth ball. We also note that eventually, we will prove in Corollary 5.4 that if blow-up occurs at a singular point, then Condition 3.7 must hold.

From now on, assume we are working in dimension $n=4$. In the following context, we will use $C$ to denote various constants which only depend on the limit metric $g, \inf K_{\infty},\left\|K_{\infty}\right\|_{C^{2}}$ and possibly the chosen small radius $\rho_{1}, \delta$ and $\sigma$. The dependency is implied in the proof. Fix $\delta>0$, and define
$$\lambda_{k}=(2-\delta) \frac{p_{k}-1}{2}-1 .$$

Proposition 3.9 ([LZ99]). Assuming Condition 3.7, for sufficiently small $\delta>0$, there exists constants $0<\rho_{1}<\rho$ and $C>0$ such that
$$\begin{aligned}
M_{k}^{\lambda_{k}} u_{k}(x) & \leq C|x|^{-2+\delta}, \\
M_{k}^{\lambda_{k}}\left|\nabla u_{k}(x)\right| & \leq C|x|^{-3+\delta}, \\
M_{k}^{\lambda_{k}}\left|\nabla^{2} u_{k}(x)\right| & \leq C|x|^{-4+\delta},
\end{aligned}$$
for every $x$ satisfying
$$R_{k}^{\prime} M_{k}^{-\frac{p_{k}-1}{2}} \leq|x| \leq \rho_{1} .$$
As a consequence, it implies
$$\begin{aligned}
v_{k}(y) & \leq C M_{k}^{\delta \frac{p_{k}-1}{2}}(1+|y|)^{-2}, \\
\left|\nabla v_{k}(y)\right| & \leq C M_{k}^{\delta \frac{p_{k}-1}{2}}(1+|y|)^{-3}, \\
\left|\nabla^{2} v_{k}(y)\right| & \leq C M_{k}^{\delta \frac{p_{k}-1}{2}}(1+|y|)^{-4},
\end{aligned}$$
for every $y$ satisfying
$$|y| \leq \rho_{1} M_{k}^{\frac{p_{k}-1}{2}} .$$
Proof. The proof is the same as [LZ99, Lemma 7.3]. That proof was for $n=3$, but directly generalizes to higher dimensions. \(\square\)

Proposition 3.10. Assuming Condition 3.7, then there exists a constant $C$ such that
$$\left|\nabla K_{k}\left(x_{k}\right)\right| \leq C M_{k}^{-2+2 \delta},$$
as $k \rightarrow \infty$. Consequently,
$$\left|\nabla K_{\infty}(\bar{x})\right|=0 .$$
Proof. The proof is very similar to [LZ99, Lemma 7.8], we provide here only a brief outline. Recall that $\left\{x^{i}\right\}$ is the $g_{k}$-normal coordinates centered at point $x_{k}$. For some fixed positive small $\sigma$, let $\eta$ be a smooth cutoff function such that $\eta(x)=1$ for $|x| \leq \sigma / 2$ and $\eta(x)=0$ for $|x| \geq \sigma$. Multipying equation (3.5) by $\eta\left(\partial u_{k} / \partial x^{j}\right)$, integrating by parts on $\{|x| \leq \sigma\} / \Gamma$, we get
$$\begin{aligned}
& \int_{\{|x| \leq \sigma\} / \Gamma} \frac{\partial K_{k}}{\partial x^{j}} \eta f_{k}^{-\tau_{k}} u_{k}^{p_{k}+1} d x \\
\leq & C \int_{\{|x| \leq \sigma\} / \Gamma}\left(|\nabla \eta| \cdot\left|\nabla u_{k}\right|^{2}+\left|\frac{\partial\left(\eta R_{k}\right)}{\partial x^{j}}\right| u_{k}^{2}+\left|\frac{\partial\left(\eta f_{k}^{-\tau_{k}}\right)}{\partial x^{j}}\right| K_{k} u_{k}^{p_{k}+1}\right) d x .
\end{aligned}$$
Then, using Proposition 3.4 in the ball $|x| \leq R_{k}^{\prime} M_{k}^{-\frac{p_{k}-1}{2}}$ and Proposition 3.9 in the annuli $R_{k}^{\prime} M_{k}^{-\frac{p_{k}-1}{2}} \leq|x| \leq \sigma$, together with the assumption that $K_{k}$ converges to $K_{\infty}$ in the $C_{\text {loc }}^{0}$ norm, for large $k$ 's we have
$$\int_{\{|x| \leq \sigma\} / \Gamma} \frac{\partial K_{k}}{\partial x^{j}} u_{k}^{p_{k}+1} d x \leq C_{1} M_{k}^{-2+2 \delta}$$
where $C_{1}$ depends on $\inf K_{\infty},\left\|K_{\infty}\right\|_{C^{0}}$ and $\sigma$. Next, the power series expansion
$$\frac{\partial K_{k}}{\partial x^{j}}(x)=\frac{\partial K_{k}}{\partial x^{j}}(0)+\frac{\partial^{2} K_{k}}{\partial x^{j} \partial x^{i}}(0) \cdot x^{i}+O\left(|x|^{2}\right),$$
implies that
$$\left|\frac{\partial K_{k}}{\partial x^{j}}(0)\right| \leq\left|\frac{\partial K_{k}}{\partial x^{j}}(x)\right|+C_{2}|x|,$$
where $C_{2}$ depends on $\left\|K_{\infty}\right\|_{C^{2}}$. Multiplying by $u_{k}^{p_{k}+1}$, integrating over $\{|x| \leq \sigma\} / \Gamma$ and using inequality (3.25), we get
$$\left|\frac{\partial K_{k}}{\partial x^{j}}(0)\right| \int_{\{|x| \leq \sigma\} / \Gamma} u_{k}(x)^{p_{k}+1} d x \leq C\left(M_{k}^{-2+2 \delta}+\int_{\{|x| \leq \sigma\} / \Gamma}|x| u_{k}(x)^{p_{k}+1} d x\right) .$$
The integral on the left limits to the volume of the bubble which is a finite constant, the integral on the right can be estimated similarly as above using Proposition 3.4 and Proposition 3.9. Therefore, we have proved
$$\left|\nabla K_{k}\left(x_{k}\right)\right| \leq C M_{k}^{-2+2 \delta},$$
where $C$ is a constant depending on $\inf K_{\infty},\left\|K_{\infty}\right\|_{C^{2}}, g$ and $\sigma$. \(\square\)

Proposition 3.11 (Mar05 Proposition 4.5). Assuming Condition 3.7, then there exists a constant $C>0$ and $0<\rho_{1}<\rho$ such that
$$M_{k} u_{k}(x) \leq C d_{g_{k}}\left(x, x_{k}\right)^{-2}$$
for $x$ satisfying $d_{g_{k}}\left(x, x_{k}\right) \leq \rho_{1}$.
Proof. The proof is very similar to the proof of [Mar05, Proposition 4.5]. That proof was assuming $K_{k}=$ constant. For variable $K_{k}$, every step in the proof remains valid, except for Claim 2 of [Mar05, Proposition 4.5], which says that there exists $C>0$ such that
$$\tau_{k} \leq C M_{k}^{-2+2 \delta+o(1)} \log \left(M_{k}\right) \text { as } k \rightarrow \infty .$$
This estimate does not hold in our setting, however, a modification of his arguments shows that there exists a constant $C>0$ such that
$$\tau_{k} \leq C M_{k}^{-2+6 \delta+o(1)} \text { as } k \rightarrow \infty .$$
To verify this, note that when $K_{k}$ is a variable function, there will be an extra term on the left hand side of [Mar05, inequality (4.18)]. That extra term is
$$\begin{aligned}
& \frac{1}{p_{k}+1}\left|\int_{\left\{|x| \leq \frac{\rho_{1}}{2}\right\} / \Gamma}\left(\nabla K_{k}(x) \cdot x\right) u_{k}(x)^{p_{k}+1} d x\right| \\
\leq & \frac{1}{p_{k}+1} M_{k}^{3-p_{k}} \int_{\left\{|y| \leq \frac{\rho_{1}}{2} M_{k}^{\frac{p_{k}-1}{2}}\right\} / \Gamma}\left|\nabla_{x} K_{k}\left(M_{k}^{-\frac{p_{k}-1}{2}} y\right)\right| \cdot\left|M_{k}^{-\frac{p_{k}-1}{2}} y\right| v_{k}(y)^{p_{k}+1} d y .
\end{aligned}$$
For small $\rho_{1}$ and large $k$, when $|x| \leq \frac{\rho_{1}}{2}$, by power series expansion and Proposition 3.10, we have
$$\left|\nabla K_{k}(x)\right| \leq\left|\nabla K_{k}\left(x_{k}\right)\right|+C|x| \leq C\left(M_{k}^{-2+2 \delta}+|x|\right) .$$
Then for $|y| \leq \frac{\rho_{1}}{2} M_{k}^{\frac{p_{k}-1}{2}}$ and large $k$,
$$\begin{aligned}
\left|\nabla_{x} K_{k}\left(M_{k}^{-\frac{p_{k}-1}{2}} y\right)\right| \cdot\left|M_{k}^{-\frac{p_{k}-1}{2}} y\right| & \leq C\left(M_{k}^{-2-\frac{p_{k}-1}{2}+2 \delta}|y|+M_{k}^{-p_{k}+1}|y|^{2}\right) \\
& \leq C\left(\rho_{1} M_{k}^{-2+2 \delta}+M_{k}^{-p_{k}+1}\right)|y|^{2} \\
& \leq C M_{k}^{-2+2 \delta}|y|^{2} .
\end{aligned}$$

On the other hand, by Proposition 3.9, we know
$$v_{k}(y)^{p_{k}+1} \leq C M_{k}^{\delta \frac{p_{k}^{2}-1}{2}}(1+|y|)^{-2\left(p_{k}+1\right)} .$$
Therefore,
$$\begin{aligned}
& M_{k}^{3-p_{k}} \int_{\left\{|y| \leq \frac{\rho_{1}}{2} M_{k}^{\frac{p_{k}-1}{2}}\right\} / \Gamma}\left|\nabla_{x} K_{k}\left(M_{k}^{-\frac{p_{k}-1}{2}} y\right)\right| \cdot\left|M_{k}^{-\frac{p_{k}-1}{2}} y\right| v_{k}(y)^{p_{k}+1} d y \\
\leq & C M_{k}^{3-p_{k}} M_{k}^{-2+2 \delta} M_{k}^{\delta \frac{p_{k}^{2}-1}{2}} \int_{\left\{|y| \leq \frac{\rho_{1}}{2} M_{k}^{\frac{p_{k}-1}{2}}\right\} / \Gamma}(1+|y|)^{-2\left(p_{k}+1\right)}|y|^{2} d y \\
\leq & C M_{k}^{-2+6 \delta+o(1)} \int_{\mathbb{R}^{4} / \Gamma}(1+|y|)^{-8+o(1)}|y|^{2} d y \\
\leq & C M_{k}^{-2+6 \delta+o(1)} \text { as } k \rightarrow \infty .
\end{aligned}$$
Then (3.32) is proved following the same proof as in Claim 2 in [Mar05, Proposition 4.5]. \(\square\)

Corollary 3.12 ([Mar05] Corollary 4.6). Assuming Condition 3.7, after maybe passing to a subsequence, we have
$$M_{k} u_{k} \rightarrow h_{\bar{x}} \text { in } C_{l o c}^{2}\left(\left(B_{r}(\bar{x}) \backslash\{\bar{x}\}\right) / \Gamma\right),$$
where $M_{k}$ is as defined in Definition 3.2 and $h_{\bar{x}}=a G(\cdot, \bar{x})$ is a constant multiple of the standard Green function, i.e. $L_{g}(G(\cdot, \bar{x}))=\delta_{\bar{x}}$ is the Dirac delta function at point $\bar{x}$. (Here, $g$ stands for the limit metric.)

Proof. The proof of Marques remains valid for variable $K_{k}$. \(\square\)

Then, we have the following:
Proposition 3.13. Assuming Condition 3.7, then
$$\tau_{k} \leq C M_{k}^{-2},$$
and there exists $\delta>0$ such that
$$\begin{aligned}
\left|v_{k}(y)-U_{K_{k}\left(x_{k}\right)}(y)\right| & \leq C M_{k}^{-2}, \\
\left|\nabla\left(v_{k}-U_{K_{k}\left(x_{k}\right)}\right)(y)\right| & \leq C M_{k}^{-2}(1+|y|)^{-1}, \\
\left|\nabla^{2}\left(v_{k}-U_{K_{k}\left(x_{k}\right)}\right)(y)\right| & \leq C M_{k}^{-2}(1+|y|)^{-2},
\end{aligned}$$
for $|y| \leq \delta M_{i}^{\frac{p_{i}-1}{2}}$.
Proof. The proof for $K_{k}=$ constant is by [Mar05, Chapter 5]. We need to verify that Marques' proof is valid for variable $K_{k}$. When $K_{k}$ is a variable function instead of a fixed constant, every $U_{0}$ in [Mar05, Chapter 5] has to be replaced by $U_{K_{k}\left(x_{k}\right)}$, then [Mar05, equation (5.1)] will become
$$\begin{aligned}
Q_{k}(y)= & \Lambda_{k}^{-1}\left\{c(n) M_{k}^{-\left(p_{k}-1\right)} R_{g_{k}}\left(M_{k}^{-\frac{p_{k}-1}{2}} y\right) U_{K_{k}\left(x_{k}\right)}(y)+M_{k}^{-(1+N) \frac{p_{k}-1}{2}} O\left(|y|^{N}\right)|y|\left(1+|y|^{2}\right)^{-2}\right. \\
& \left.+\left(K_{k}\left(x_{k}\right) U_{K_{k}\left(x_{k}\right)}^{3}-\tilde{K}_{k}(y) \tilde{f}_{k}^{-\tau_{k}} U_{K_{k}\left(x_{k}\right)}^{p_{k}}\right)\right\},
\end{aligned}$$
where $\tilde{K}_{k}(y)=K_{k}\left(M_{k}^{-\frac{p_{k}-1}{2}} y\right)$ and $\tilde{f}_{k}(y)=f_{k}\left(M_{k}^{-\frac{p_{k}-1}{2}} y\right)$. Only the last term in (3.43) differs from the last term in [Mar05, equation (5.1)]. Denote it by
$$\mathbb{B}_{k}=K_{k}\left(x_{k}\right) U_{K_{k}\left(x_{k}\right)}^{3}-\tilde{K}_{k}(y) \tilde{f}_{k}^{-\tau_{k}} U_{K_{k}\left(x_{k}\right)}^{p_{k}} .$$

To analyze it, by power series expansion we obtain
$$\begin{aligned}
\left|\tilde{K}_{k}(y)-K_{k}\left(x_{k}\right)\right| & =\left|K_{k}\left(M_{k}^{-\frac{p_{k}-1}{2}} y\right)-K_{k}(0)\right| \\
& \leq\left|\nabla K_{k}(0)\right| M_{k}^{-\frac{p_{k}-1}{2}}|y|+C M_{k}^{-\left(p_{k}-1\right)}|y|^{2} .
\end{aligned}$$
By Proposition 3.9, $\left|\nabla K_{k}(0)\right|=\left|\nabla K_{k}\left(x_{k}\right)\right| \leq C M_{k}^{-2+2 \delta}$, hence
$$\begin{aligned}
\left|\tilde{K}_{k}(y)-K_{k}\left(x_{k}\right)\right| & \leq C\left(M_{k}^{-2-\frac{p_{k}-1}{2}+2 \delta}|y|+M_{k}^{-\left(p_{k}-1\right)}|y|^{2}\right) \\
& \leq C\left(M_{k}^{-3+2 \delta+o(1)}+M_{k}^{-2+\tau_{k}}|y|\right)|y| .
\end{aligned}$$
Then we have the estimate
$$\begin{aligned}
\mathbb{B}_{k} & \leq K_{k}\left(x_{k}\right) U_{K_{k}\left(x_{k}\right)}^{3}\left(1-\left(\tilde{f}_{k} U_{K_{k}\left(x_{k}\right)}^{3}\right)^{-\tau_{k}}\right)+\left|\tilde{K}_{k}(y)-K_{k}\left(x_{k}\right)\right| \tilde{f}_{k}^{-\tau_{k}} U_{K_{k}\left(x_{k}\right)}^{p_{k}} \\
& \leq C\left(\tau_{k} \log \left(\tilde{f}_{k} U_{K_{k}\left(x_{k}\right)}\right)\left(1+|y|^{2}\right)^{-3}+\left(M_{k}^{-3+2 \delta+o(1)}+M_{k}^{-2+\tau_{k}}|y|\right)|y|\left(1+|y|^{2}\right)^{-2}\right) .
\end{aligned}$$
Suppose
$$\Lambda_{k}^{-1} \max \left\{M_{k}^{-2}, \tau_{k}\right\} \rightarrow 0 \text { as } k \rightarrow \infty .$$
Note that (3.32) implies $\lim _{k \rightarrow \infty} M_{k}^{\tau_{k}}=1$, so $\lim _{k \rightarrow \infty} \Lambda_{k}^{-1} \mathbb{B}_{k} \rightarrow 0$. Thus $\left|Q_{k}\right| \rightarrow 0$ as $k \rightarrow 0$ and [Mar05, Lemma 5.1] can be proved following the rest of his proof. Also, [Mar05, Lemma 5.3] remains valid with a similar modification to the term $\tilde{Q}_{k}$ in his proof. Therefore, our proposition is proved for variable $K_{k}$. \(\square\)

\section*{4. Local blow-up analysis}
4.1. Application of Pohozaev Identity. Assuming Condition 3.7, recall that $g_{k}$ is the conformal normal metric with conformal normal coordinates $\left\{x^{i}\right\}$ centered at the point $x_{k}$. By [LP87, Chapter 5] and the explicit computations in [LZ05, Chapter 2], we have the following for each $k$. At $x=0$ (the point $x_{k}$ ), the scalar curvature satisfies
$$R_{k}(0)=0,\left(R_{k}\right)_{, i}(0)=0 .$$
Locally in a neighborhood of $x=0$, we have $\left(g_{k}\right)_{i j}=\delta_{i j}+O\left(r^{2}\right)$ and $\operatorname{det}\left(g_{k}\right)=1+O\left(r^{N}\right)$ for some $N \geq 5$. Write
$$\Delta_{g_{k}}=\frac{1}{\sqrt{\operatorname{det}\left(g_{k}\right)}} \partial_{i}\left(\sqrt{\operatorname{det}\left(g_{k}\right)}\left(g_{k}\right)^{i j} \partial_{j}\right)=\Delta_{0}+\left(b_{k}\right)_{i} \partial_{i}+\left(d_{k}\right)_{i j} \partial_{i j},$$
where $\partial_{i}=\frac{\partial}{\partial x^{i}}, \partial_{i j}=\frac{\partial^{2}}{\partial x^{i} \partial x^{j}}$ and $\Delta_{0}=\sum_{i=1}^{n} \frac{\partial^{2}}{\left(\partial x^{i}\right)^{2}}$, then
$$\left(b_{k}\right)_{i}=O\left(r^{2}\right) \text { and }\left(d_{k}\right)_{i j}=g^{i j}-\delta_{i j}=O\left(r^{2}\right) .$$
By the change of variables and the rescaled metric defined in (3.8) and (3.9), we have
$$\Delta_{h_{k}}=\bar{\Delta}_{0}+\left(\bar{b}_{k}\right)_{i} \bar{\partial}_{i}+\left(\bar{d}_{k}\right)_{i j} \bar{\partial}_{i j},$$
where
$$\begin{aligned}
& \left(\bar{b}_{k}\right)_{i}(y)=M_{k}^{-\frac{p_{k}-1}{2}}\left(b_{k}\right)_{i}\left(M_{k}^{-\frac{p_{k}-1}{2}} y\right), \quad\left(\bar{d}_{k}\right)_{i j}(y)=\left(d_{k}\right)_{i j}\left(M_{k}^{-\frac{p_{k}-1}{2}} y\right), \\
& \bar{\partial}_{i}=\frac{\partial}{\partial y^{i}}, \quad \bar{\partial}_{i j}=\frac{\partial^{2}}{\partial y^{i} \partial y^{j}} \text { and } \bar{\Delta}_{0}=\sum_{i=1}^{n} \frac{\partial^{2}}{\left(\partial y^{i}\right)^{2}} .
\end{aligned}$$
It follows that
$$\left|\left(\bar{b}_{k}\right)_{i}(y)\right|=M_{k}^{-\frac{3\left(p_{k}-1\right)}{2}} O(|y|)^{2}, \quad\left|\left(\bar{d}_{k}\right)_{i j}(y)\right|=M_{k}^{-\left(p_{k}-1\right)} O(|y|)^{2} .$$

Using the above notation, we rewrite equation (3.5) in the $\left\{x^{i}\right\}$ coordinates as following
$$\left(\left(d_{k}\right)_{i j}+\delta_{i j}\right) \partial_{i j} u_{k}+\left(b_{k}\right)_{i} \partial_{i} u_{k}-\frac{1}{6} R_{k} u_{k}+K_{k} f_{k}^{-\tau_{k}} u_{k}^{p_{k}}=0 .$$
For some small $\sigma$, apply Lemma 3.1 to the above equation in $\{|x| \leq \sigma\} / \Gamma$, to obtain
$$\begin{aligned}
P\left(\sigma, u_{k}\right)= & -\int_{\{|x| \leq \sigma\} / \Gamma}\left(x \cdot \nabla_{x} u_{k}+u_{k}\right)\left(\left(d_{k}\right)_{i j} \partial_{i j} u_{k}+\left(b_{k}\right)_{i} \partial_{i} u_{k}\right) \\
& -\frac{1}{12} \int_{\{|x| \leq \sigma\} / \Gamma}\left(x \cdot \nabla_{x} R_{k}+2 R_{k}\right) u_{k}^{2} \\
& +\frac{\sigma}{12} \int_{\{|x|=\sigma\} / \Gamma} R_{k} u_{k}^{2}+\frac{1}{p_{k}+1} \int_{\{|x| \leq \sigma\} / \Gamma}\left(x \cdot \nabla_{x}\left(K_{k} f_{k}^{-\tau_{k}}\right)\right) u_{k}^{p_{k}+1} \\
& +\frac{\tau_{k}}{p_{k}+1} \int_{\{|x| \leq \sigma\} / \Gamma} K_{k} f_{k}^{-\tau_{k}} u_{k}^{p_{k}+1}-\frac{\sigma}{p_{k}+1} \int_{\{|x|=\sigma\} / \Gamma} K_{k} f_{k}^{-\tau_{k}} u_{k}^{p_{k}+1} \\
= & \int_{\{|x|=\sigma\} / \Gamma}\left(u_{k} \frac{\partial u_{k}}{\partial \nu}-\frac{\sigma}{2}\left|\nabla u_{k}\right|^{2}+\sigma\left|\frac{\partial u_{k}}{\partial \nu}\right|^{2}\right) .
\end{aligned}$$
Denote $R_{k}^{\prime}=M_{k}^{\frac{p_{k}-1}{2}} \sigma$. Define the following
$$\begin{aligned}
I_{k, 1} & =-\frac{\sigma}{p_{k}+1} \int_{\{|x|=\sigma\} / \Gamma} K_{k} f_{k}^{-\tau_{k}} u_{k}^{p_{k}+1} d \sigma(x) \\
& =-\frac{\sigma}{p_{k}+1} M_{k}^{\frac{5-p_{k}}{2}} \int_{\left\{|y|=R_{k}^{\prime}\right\} / \Gamma} \tilde{K}_{k} \tilde{f}_{k}^{-\tau_{k}} v_{k}^{p_{k}+1} d \sigma(y),
\end{aligned}$$
$$\begin{aligned}
I_{k, 2}= & \int_{\{|x| \leq \sigma\} / \Gamma}\left(-\left(b_{k}\right)_{i} \partial_{i} u_{k}-\left(d_{k}\right)_{i j} \partial_{i j} u_{k}\right)\left(\nabla_{x} u_{k} \cdot x+u_{k}\right) d x \\
= & M_{k}^{\tau_{k}} \int_{\left\{|y| \leq R_{k}^{\prime}\right\} / \Gamma}\left(-\left(\bar{b}_{k}\right)_{i} \bar{\partial}_{i} v_{k}-\left(\bar{d}_{k}\right)_{i j} \bar{\partial}_{i j} v_{k}\right)\left(y \cdot \nabla_{y} v_{k}+v_{k}\right) d y
\end{aligned}$$
$$I_{k, 3}=\frac{\sigma}{12} \int_{\{|x|=\sigma\} / \Gamma} R_{k} u_{k}^{2} d \sigma(x)=\frac{\sigma}{12} M_{k}^{\frac{7-3 p_{k}}{2}} \int_{\left\{|y|=R_{k}^{\prime}\right\} / \Gamma} \tilde{R}_{k} v_{k}^{2} d \sigma(y),$$
$$\begin{aligned}
I_{k, 4}= & -\frac{1}{12} \int_{\{|x| \leq \sigma\} / \Gamma}\left(x \cdot \nabla_{x} R_{k}+2 R_{k}\right) u_{k}^{2} d x \\
& =-\frac{1}{12} M_{k}^{4-2 p_{k}} \int_{\left\{|y| \leq R_{k}^{\prime}\right\} / \Gamma}\left(y \cdot \nabla_{y} \tilde{R}_{k}+2 \tilde{R}_{k}\right) v_{k}^{2} d y,
\end{aligned}$$
$$\begin{aligned}
I_{k, 5}= & \frac{1}{p_{k}+1} \int_{\{|x| \leq \sigma\} / \Gamma}\left(x \cdot \nabla_{x}\left(K_{k} f_{k}^{-\tau_{k}}\right)\right) u_{k}^{p_{k}+1} d x \\
& =\frac{1}{p_{k}+1} M_{k}^{\tau_{k}} \int_{\left\{|y| \leq R_{k}^{\prime}\right\} / \Gamma}\left(y \cdot \nabla_{y}\left(\tilde{K}_{k} \tilde{f}_{k}^{-\tau_{k}}\right)\right) v_{k}^{p_{k}+1} d y,
\end{aligned}$$
$$I_{k, 6}=\frac{\tau_{k}}{p_{k}+1} \int_{\{|x| \leq \sigma\} / \Gamma} K_{k} f_{k}^{-\tau_{k}} u_{k}^{p_{k}+1} d x=\frac{\tau_{k}}{p_{k}+1} M_{k}^{\tau_{k}} \int_{\left\{|y| \leq R_{k}^{\prime}\right\} / \Gamma} \tilde{K}_{k} \tilde{f}_{k}^{-\tau_{k}} v_{k}^{p_{k}+1} d y,$$
$$\begin{aligned}
I_{k, 7} & =\int_{\{|x|=\sigma\} / \Gamma}\left\{\left(\left|\frac{\partial u_{k}}{\partial \nu_{x}}\right|^{2}-\frac{1}{2}\left|\nabla_{x} u_{k}\right|^{2}\right) \sigma+u_{k} \frac{\partial u_{k}}{\partial \nu_{x}}\right\} d \sigma(x) \\
& =M_{k}^{\tau_{k}} \int_{\left\{|y|=R_{k}^{\prime}\right\} / \Gamma}\left\{\left(\left|\frac{\partial v_{k}}{\partial \nu_{y}}\right|^{2}-\frac{1}{2}\left|\nabla_{y} v_{k}\right|^{2}\right) R_{k}^{\prime}+v_{k} \frac{\partial v_{k}}{\partial \nu_{y}}\right\} d \sigma(y)
\end{aligned}$$
Then (4.8) becomes
$$I_{k, 7}=I_{k, 1}+I_{k, 2}+I_{k, 3}+I_{k, 4}+I_{k, 5}+I_{k, 6} .$$
4.2. Main Estimates. By [CGS89], it is sufficient to consider the blow-up case as $p_{k} \rightarrow 3$, consequently $\tau_{k}=3-p_{k} \rightarrow 0$. Then we know $\lim _{k \rightarrow \infty} M_{k}^{\tau_{k}}=1$ from (3.32). We can estimate terms in the Pohozaev identity through the following lemmas. We will use $C, C_{1}$ to denote various positive constants independent of $k$ and $\sigma$. For notational simplicity, we will omit $d x, d y, d \sigma(x)$ and $d \sigma(y)$ terms in integrals.

Lemma 4.1. For small $\sigma>0$,
$$\lim _{k \rightarrow \infty} M_{k}^{2} I_{k, 1}=0 .$$
Proof. Using (3.5),
$$I_{k, 1}=\frac{\sigma}{p_{k}+1} \int_{\{|x|=\sigma\} / \Gamma}\left(L_{g_{k}} u_{k}\right) \cdot u_{k} .$$
By Corollary 3.12, $M_{k} u_{k} \rightarrow h$ in the $C_{\text {loc }}^{2}$ norm, hence for small $\sigma$,
$$\begin{aligned}
\lim _{k \rightarrow \infty} M_{k}^{2} I_{k, 1}= & \lim _{k \rightarrow \infty} \frac{\sigma}{p_{k}+1} \int_{\{|x|=\sigma\} / \Gamma}\left(L_{g_{k}}\left(M_{k} u_{k}\right)\right) \cdot\left(M_{k} u_{k}\right) \\
& =\frac{\sigma}{p_{k}+1} \int_{\{|x|=\sigma\} / \Gamma}\left(L_{g} h\right) \cdot h=0 .
\end{aligned}$$ \(\square\)

Lemma 4.2. For $\sigma \leq 1$, there exists some constant $C>0$ such that
$$\limsup _{k \rightarrow \infty} M_{k}^{2}\left|I_{k, 2}\right| \leq C \sigma^{2}$$
Proof. Because $U_{K_{k}\left(x_{k}\right)}(y)$ is a radial function and $\left\{y^{i}\right\}$ is a rescale of the conformal normal coordinates, we know
$$\left(\Delta_{h_{k}}-\bar{\Delta}_{0}\right) U_{K_{k}\left(x_{k}\right)}=\left(\left(\bar{b}_{k}\right)_{i} \bar{\partial}_{i}+\left(\bar{d}_{k}\right)_{i j} \bar{\partial}_{i j}\right) U_{K_{k}\left(x_{k}\right)} \equiv 0 .$$
Then, we have
$$\begin{aligned}
M_{k}^{2}\left|I_{k, 2}\right| & \leq M_{k}^{2+\tau_{k}} \int_{\left\{|y| \leq \sigma M_{k}^{\frac{p_{k}-1}{2}}\right\} / \Gamma}\left|\left(\left(\bar{b}_{k}\right)_{i} \partial_{i}+\left(\bar{d}_{k}\right)_{i j} \partial_{i j}\right) v_{k}\right| \cdot\left|\nabla_{y} v_{k} \cdot y+v_{k}\right| \\
& =M_{k}^{2+\tau_{k}} \int_{\left\{|y| \leq \sigma M_{k}^{\frac{p_{k}-1}{2}}\right\} / \Gamma}\left|\left(\left(\bar{b}_{k}\right)_{i} \partial_{i}+\left(\bar{d}_{k}\right)_{i j} \partial_{i j}\right)\left(v_{k}-U_{K_{k}\left(x_{k}\right)}\right)\right| \cdot\left|\nabla_{y} v_{k} \cdot y+v_{k}\right| .
\end{aligned}$$
For $\sigma \leq 1$, we have $|y| \leq \sigma M_{k}^{\frac{p_{k}-1}{2}} \leq M_{k}^{\frac{p_{k}-1}{2}}$, hence $M_{k}^{-1} \leq M_{k}^{-\frac{p_{k}-1}{2}} \leq C(1+|y|)^{-1}$ for large $k$. By (4.6) and Proposition 3.13, for large $k$, we have
$$\begin{aligned}
& \left|\left(\left(\bar{b}_{k}\right)_{i}(y) \bar{\partial}_{i}+\left(\bar{d}_{k}\right)_{i j}(y) \bar{\partial}_{i j}\right)\left(v_{k}(y)-U_{K_{k}\left(x_{k}\right)}(y)\right)\right| \\
\leq & C M_{k}^{-2} M_{k}^{-\left(p_{k}-1\right)}|y|^{2}(1+|y|)^{-1}\left(M_{k}^{-\frac{p_{k}-1}{2}}+(1+|y|)^{-1}\right) \\
\leq & C M_{k}^{-1-p_{k}}|y|^{2}(1+|y|)^{-2} \leq C M_{k}^{-1-p_{k}},
\end{aligned}$$
and
$$\begin{aligned}
\left|y \cdot \nabla_{y} v_{k}(y)+v_{k}(y)\right| & \leq\left|\nabla_{y} U_{K_{k}\left(x_{k}\right)}\right| \cdot|y|+\left|\nabla_{y}\left(v_{k}-U\right)\right| \cdot|y|+\left|v_{k}-U\right|+U \\
& \leq C\left(|y|^{2}\left(1+|y|^{2}\right)^{-2}+M_{k}^{-2}(1+|y|)^{-1}|y|+M_{k}^{-2}+\left(1+|y|^{2}\right)^{-1}\right) \\
& \leq C\left(\left(1+|y|^{2}\right)^{-1}+M_{k}^{-2}\right) \leq C\left(1+|y|^{2}\right)^{-1} .
\end{aligned}$$
Thus, for large $k$,
$$\begin{aligned}
M_{k}^{2}\left|I_{k, 2}\right| & \leq C M_{k}^{2+\tau_{k}} M_{k}^{-1-p_{k}} \int_{\left\{|y| \leq \sigma M_{k}^{\frac{p_{k}-1}{2}}\right\} / \Gamma}\left(1+|y|^{2}\right)^{-1} \\
& \leq C M_{k}^{1-p_{k}+\tau_{k}} \int_{0}^{\sigma M_{k}^{\frac{p_{k}-1}{2}}} r^{3}\left(1+r^{2}\right)^{-1} d r \\
& \leq C M_{k}^{1-p_{k}+\tau_{k}}\left(\left(\sigma M_{k}^{\frac{p_{k}-1}{2}}\right)^{2}+C_{1}\right) \\
& =C M_{k}^{\tau_{k}} \sigma^{2}+C C_{1} M_{k}^{1-p_{k}+\tau_{k}} \leq C \sigma^{2} \text { as } k \rightarrow \infty .
\end{aligned}$$ \(\square\)

Lemma 4.3. There exist constants $C>0$ and $0<\delta<1$ such that when $\sigma<\delta$,
$$\limsup _{k \rightarrow \infty} M_{k}^{2}\left|I_{k, 3}\right| \leq C \sigma^{2} .$$
Proof. Due to (4.1), there exist $C>0$ and $0<\delta<1$ such that when $\sigma<\delta$, on $|x|=\sigma$, by power series expansion, $\left|R_{k}(x)\right| \leq C|x|^{2}=C \sigma^{2}$. Hence $\left|\tilde{R}_{k}(y)\right| \leq C \sigma^{2}$ on $|y|=\sigma M_{k}^{\frac{p_{k}-1}{2}}$. On the other hand, on $|y|=\sigma M_{k}^{\frac{p_{k}-1}{2}} \leq M_{k}^{\frac{p_{k}-1}{2}}, M_{k}^{-1} \leq M_{k}^{-\frac{p_{k}-1}{2}} \leq|y|^{-1}$. By Proposition 3.13,
$$\begin{aligned}
v_{k}^{2}(y) & \leq\left[\left|v_{k}(y)-U_{K_{k}\left(x_{k}\right)}(y)\right|+U_{K_{k}\left(x_{k}\right)}(y)\right]^{2} \\
& \leq C\left[M_{k}^{-2}+\left(1+|y|^{2}\right)^{-1}\right]^{2} \leq C|y|^{-4} .
\end{aligned}$$
Then, we have the estimate
$$\begin{aligned}
M_{k}^{2}\left|I_{k, 3}\right| & \leq \frac{\sigma}{12} M_{k}^{\frac{11-3 p_{k}}{2}} \int_{\left\{|y|=\sigma M_{k}^{\frac{p_{k}-1}{2}}\right\} / \Gamma}\left|\tilde{R}_{k}\right| v_{k}^{2} \\
& \leq C \sigma^{3} M_{k}^{\frac{11-3 p_{k}}{2}} \int_{\left\{|y|=\sigma M_{k}^{\frac{p_{k}-1}{2}}\right\} / \Gamma}|y|^{-4} \\
& \leq C \sigma^{3} M_{k}^{\frac{11-3 p_{k}}{2}}\left(\sigma M_{k}^{\frac{p_{k}-1}{2}}\right)^{-1}=C \sigma^{2} M_{k}^{2 \tau_{k}} \leq C \sigma^{2} \text { as } k \rightarrow \infty .
\end{aligned}$$ \(\square\)

Lemma 4.4. There exist constants $C>0$ and $0<\delta<1$ such that when $\sigma<\delta$,
$$\limsup _{k \rightarrow \infty} M_{k}^{2}\left|I_{k, 4}\right| \leq C \sigma^{2} .$$
Proof. By (4.1), there exist $C>0$ and $0<\delta<1$ such that when $\sigma<\delta$, in the ball $|x| \leq \sigma$, by power series expansion, we have
$$\left|R_{k}(x)\right| \leq C|x|^{2}, \quad\left|\nabla_{x} R_{k}(x)\right| \leq\left|\nabla_{x} R_{k}(0)\right|+C|x| \leq C|x| .$$
The second inequality implies
$$\left|x \cdot \nabla_{x} R_{k}(x)\right| \leq|x| \cdot\left|\nabla_{x} R_{k}(x)\right| \leq C|x|^{2} .$$

It follows that in the ball $|y| \leq \sigma M_{k}^{\frac{p_{k}-1}{2}},\left|\tilde{R}_{k}(y)\right| \leq C M_{k}^{-\left(p_{k}-1\right)}|y|^{2}$, and
$$\left|y \cdot \nabla_{y} \tilde{R}_{k}(y)\right|=\left|\left(M_{k}^{-\frac{p_{k}-1}{2}} y\right) \cdot \nabla_{x} R_{k}\left(M_{k}^{-\frac{p_{k}-1}{2}} y\right)\right| \leq C M_{k}^{-\left(p_{k}-1\right)}|y|^{2} .$$
On the other hand, similar to (4.27), for $|y| \leq \sigma M_{k}^{\frac{p_{k}-1}{2}}$ and large $k, v_{k}^{2}(y) \leq C\left(1+|y|^{2}\right)^{-2}$. Then, for large $k$, we have the estimate
$$\begin{aligned}
M_{k}^{2}\left|I_{k, 4}\right| & \leq C M_{k}^{6-2 p_{k}} \int_{\left\{|y| \leq \sigma M_{k}^{\frac{p_{k}-1}{2}}\right\} / \Gamma}\left(\left|y \cdot \nabla_{y} \tilde{R}_{k}\right|+2\left|\tilde{R}_{k}\right|\right) v_{k}^{2} \\
& \leq C M_{k}^{6-2 p_{k}} M_{k}^{-\left(p_{k}-1\right)} \int_{\left\{|y| \leq \sigma M_{k}^{\frac{p_{k}-1}{2}}\right\} / \Gamma}|y|^{2}\left(1+|y|^{2}\right)^{-2} \\
& \leq C M_{k}^{7-3 p_{k}} \int_{0}^{\sigma M_{k}^{\frac{p_{k}-1}{2}}} r^{5}\left(1+r^{2}\right)^{-2} d r \\
& \leq C M_{k}^{7-3 p_{k}}\left(\left(\sigma M_{k}^{\frac{p_{k}-1}{2}}\right)^{2}+C_{1}\right)=C \sigma^{2} M_{k}^{2 \tau_{k}}+C C_{1} M_{k}^{7-3 p_{k}} \leq C \sigma^{2} \text { as } k \rightarrow \infty .
\end{aligned}$$ \(\square\)