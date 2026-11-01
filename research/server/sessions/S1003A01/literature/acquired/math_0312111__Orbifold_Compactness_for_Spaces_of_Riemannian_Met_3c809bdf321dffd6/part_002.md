---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: [math/0312111] Orbifold Compactness for Spaces of Riemannian Metrics and Applications]

The hypotheses (1.8) and (1.9) in Theorem 1.2 are scale invariant and we need to first choose a scale and base points at which to begin the analysis. Thus, in the following, we assume that any $(N, g)$ is scaled, and a base point $x_{0} \in(N, g)$ is chosen, so that
$$\int_{B_{x_{0}}(1)}|R|^{n / 2}=\delta_{0}, \text { and } \int_{B_{x}(1)}|R|^{n / 2} \leq \delta_{0}, \forall x \in N .$$
It follows from the small curvature estimate (1.5) that the curvature of $(N, g)$ is uniformly bounded.
The initial step is then identical to the procedure above, giving a limit $\left(N^{0}, g^{0}, x^{0}\right)$ associated with radii $R_{i}^{1} \rightarrow \infty$. The first rescaling to obtain the limit $\left(V^{1}, g^{1}\right)$ is also identical within small a small ball $B\left(\mu_{0}\right)$ about the orbifold singularity $\{0\}$. However, the curvature of $g_{i}^{1}$ may not be uniformly bounded outside $B\left(\mu_{0}\right)$. Nevertheless, we claim that this just corresponds to formation of new orbifold singular points on the limit $V^{1}$. For suppose the curvature of $g_{i}^{1}$ blows up at points
$y_{i}$ within finite distance to $x_{i}$ w.r.t. $g_{i}^{1}$. By perturbing $y_{i}$ slightly if necessary, we may assume that curvature is more concentrated in $L^{n / 2}$ norm at $y_{i}$ than at nearby points. The metric $g_{i}^{1}$ may then be rescaled to $\widetilde{g}_{i}^{1}$, based at $y_{i}$ so that, with respect to $\widetilde{g}_{i}^{1}$,
$$\int_{B_{y_{i}}(1)}|R|^{n / 2}=\delta_{0}, \text { and } \int_{B_{y}\left(\frac{1}{2}\right)}|R|^{n / 2} \leq \delta_{0}$$
for all $y$ within $\widetilde{g}_{i}^{1}$ bounded distance to $y_{i}$. Note that by (2.56), distances w.r.t. the metric $\widetilde{g}_{i}^{1}$ are no larger than distances w.r.t. the original metric $g_{i}$. One may now repeat the analysis carried out above at $x_{i}$ at $y_{i}$ in place of $x_{i}$. It follows that $y_{i}$ converges, (as always in a subsequence of the original sequence) to an orbifold singularity $p \in V^{1}$. Thus, the limit $\left(V^{1}, g^{1}\right)$ is a complete orbifold, with a bounded number of singular points, (depending on $\Lambda$ ). As before, $V^{1}$ has a bounded number $\kappa^{1}$ of ends, each ALE, and has a maximal volume ratio $\mathcal{V}^{1}$.

With this modification of orbifold limits in place of manifold limits, the remainder of the proof is then exactly the same as above in the case (2.53) holds. This completes the proof of Theorem 1.2. \(\square\)

Remark 2.8. As in Remark 2.7, it is clear from the proof above that Theorem 1.2 also holds for orbifolds with a bounded number of cones at each singular point in place of smooth manifolds. It would be of interest to have a direct proof of this result, without the use of a contradiction.
§2.3. In this section, we complete the proof of Theorem 1.1.
Proof of Theorem 1.1.
Given the work done in the prior subsections, this is now quite simple. Thus, let $\left(M_{i}, g_{i}\right)$ be a sequence of $n$-manifolds satisfying (1.3)-(1.5). We claim that
$$\operatorname{vol} B_{x}(r)<\mathcal{V} r^{n},$$
for some constant $\mathcal{V}=\mathcal{V}\left(\nu_{0}, \Lambda, \delta_{0}, C_{0}\right)$, where $B_{x}(r)$ is any geodesic $r$-ball in $\left(M_{i}, g_{i}\right)$. For $r$ sufficiently small, (depending on $i$ ), one has, for any $x \in\left(M_{i}, g_{i}\right), \operatorname{vol} B_{x}(r) \sim \omega_{n} r^{n}$, since the metric is nearly Euclidean on sufficiently small scales. Suppose (2.57) fails, so that on some sequence of balls $B_{x_{i}}\left(r_{i}\right) \subset\left(M_{i}, g_{i}\right), \operatorname{vol} B_{x_{i}}\left(r_{i}\right) \geq \mathcal{V}_{i} r_{i}^{n}$, where $\mathcal{V}_{i} \rightarrow \infty$ as $i \rightarrow \infty$. Let $s_{i}$ be the smallest radius such that, for some $y_{i} \in\left(M_{i}, g_{i}\right)$,
$$\operatorname{volB}_{y_{i}}\left(s_{i}\right) \geq 2 V_{0} s_{i}^{n},$$
where $V_{0}$ is the $V_{0}$ from Theorem 1.2. If $s_{i}=\operatorname{diam}\left(M, g_{i}\right)$, then (2.57) holds, (with $\mathcal{V}=2 V_{0}$ ), and so there is nothing to prove. In fact, if $s_{i}$ is bounded away from 0 , independent of $i$, then again there is nothing to prove. For in this situation, one has
$$v o l B_{x}(r) \leq 2 V_{0} r^{n},$$
for all $r \leq s_{0} \leq s_{i}$, for some fixed $s_{0}>0$. Since $\operatorname{vol} M_{i}=1$, this gives an upper bound on the diameter of $\left(M_{i}, g_{i}\right)$ and hence (2.57) holds for all $r \leq \operatorname{diam} M$, (with $\mathcal{V}=C V_{0}$, for a definite $C=C\left(s_{0}\right)$ ). Thus, we may assume that $s_{i} \rightarrow 0$ as $i \rightarrow \infty$. Hence, most of volume of $\left(M_{i}, g_{i}\right)$ lies outside $B_{y_{i}}\left(s_{i}\right)$. In terms of the decomposition (2.3)-(2.4) of $\left(M_{i}, g_{i}\right)$, note that one must have $y_{i} \in B_{i}^{r}$, for all $i$, and for some $r$ small, tending to 0 as $i \rightarrow \infty$.

Now the scale invariant estimate (2.59) holds on all balls of radius $r \leq s_{i}$. Rescale the metrics $g_{i}$ by setting $\widetilde{g}_{i}=K^{2}\left(s_{i}\right)^{-2} g_{i}$, so that the ball $B_{y_{i}}\left(s_{i}\right)$ becomes a ball of radius $K$ w.r.t. $\widetilde{g}_{i}$. Here $K$ is a fixed large number. Hence, the maximal volume ratio is bounded by $2 V_{0}$ in all balls of $\widetilde{g}_{i}$-radius at most $K$. It follows from §2.1, or the proof of Theorem 1.2 above, that a subsequence of $\left(M_{i}, \widetilde{g}_{i}, y_{i}\right)$ converges to a complete limit orbifold $\left(V_{\infty}, \widetilde{g}_{\infty}, y_{\infty}\right)$, satisfying the bounds (1.3)-(1.5). Theorem 1.2 then implies that the maximal volume ratio of $\left(V_{\infty}, \widetilde{g}_{\infty}\right)$ is $V_{0}$. However, we have $\operatorname{volB}_{y_{\infty}}(K)=2 V_{0} K^{n}$. This is a contradiction, which thus proves that (2.57) holds.

Given (2.57), the remainder of the proof of Theorem 1.1 has already been completed in §2.1. \(\square\)

Remark 2.9. It is worthwhile to discuss some simple examples illustrating Theorem 1.1. As in Remark 2.6, let $p_{j}, j=1, \ldots, \kappa$, be a finite collection of points in a compact Riemannian manifold $(M, g)$ so that
$$\widetilde{g}=\left(\sum_{j=1}^{\kappa} \frac{1}{\widetilde{r}_{j}^{4}}\right) g,$$
is an AE metric on $M \backslash\left\{p_{j}\right\}$. Choose a sequence $\varepsilon_{i} \rightarrow 0$ as $i \rightarrow \infty$, and consider the metrics
$$\widetilde{g}_{i}=\varepsilon_{i}^{2} \widetilde{g} .$$
As $\varepsilon_{i} \rightarrow 0$, these metrics converge, in the Gromov-Hausdorff topology, to a union of $\kappa$ cones $C\left(S^{n-1}\right)$ on $S^{n-1}$, i.e. $\kappa$ balls $B^{n}$, joined at the vertex $\{0\}$. The limit metric $g_{\infty}$ is just the flat metric on each ball. The boundary of this collection of balls is a collection of $\kappa$ spheres $S^{n-1}$, to which one may glue on $\kappa$ balls $B^{n}$ to obtain a closed orbifold $V$. Then $V$ is clearly a collection of $\kappa$ spheres $S^{n}$, joined at a single vertex. The limit flat metric $g_{\infty}$ may be conformally bent, and extended across its boundary spheres $S^{n-1}$ to give a smooth metric $g_{\infty}^{\prime}$ on the orbifold $V$. Similarly, the sequence of metrics $\widetilde{g}_{i}$ may easily be modified and extended to give a sequence of smooth metrics $\widetilde{g}_{i}^{\prime}$ on $M \#\left(\#_{1}^{\kappa} S^{n}\right)=M$, converging to $g_{\infty}^{\prime}$ in the Gromov-Hausdorff topology,
$$\left(M \#\left(\#_{1}^{\kappa} S^{n}\right), g_{i}^{\prime}\right) \rightarrow\left(\vee_{1}^{\kappa} S^{n}, g_{\infty}^{\prime}\right) .$$
It is easily seen that the sequence $\widetilde{g}_{i}^{\prime}$ satisfies all the hypotheses of Theorem 1.1.
Observe that any non-trivial topology of $M$ has disappeared in the limit $V$. It is clear that this construction can be generalized so that any closed orbifold $V$ is the limit of a sequence of metrics on suitable manifolds $M$ satisfying the hypotheses of Theorem 1.1. The only restriction on the topology of $M$ is that the regular part $V_{0}$ of $V$ embeds as a domain in $M$, with boundary a union of spherical space-forms. The topology of the complement $M \backslash V_{0}$ may otherwise be arbitrary, (for $\Lambda$ sufficiently large).

Remark 2.10. As outlined in Remark 2.1(ii), one can completely describe the structure of the degeneration of $\left(M_{i}, g_{i}\right)$ near the orbifold singularities. We give this description here, but refer to [B] or [AC] for more details. The description closely resembles the proof of Theorem 1.2.

Let $\left(M_{i}, g_{i}\right) \rightarrow\left(V, g_{\infty}\right)$ and let $q$ be a singular point of $V$. Then there is sequence of scales $r_{i}=r_{i}^{1} \rightarrow 0$ such that the rescalings $\left(M_{i}, r_{i}^{-2} g_{i}, x_{i}\right)$ with $x_{i} \rightarrow q$, converge in the pointed Gromov-Hausdorff topology to a complete, non-compact ALE orbifold $\left(V^{1}, g^{1}\right)$ with a finite number of singular points, and
$$\int_{V^{1}}|R|^{n / 2} \geq \delta_{0} .$$
If $\left(V^{1}, g^{1}\right)$ is not a smooth manifold, then there are second level scales $\left\{r_{i}^{2}\right\}$ associated with each singular point of $V^{1}$; (the scales $r_{i}^{2}$ depend on the choice of singular point in $V^{1}$ ). Rescaling $r_{i}^{-2} g_{i}$ further by such factors at base points converging to the singular points of $V^{1}$ gives a collection of second level ALE orbifolds $\left\{\left(V^{2}, g^{2}\right)\right\}$ associated with each singular point of $\left(V^{1}, g^{1}\right)$. Each iteration of this process satisfies (2.61), and hence this process terminates at a finite stage. At the last stage, corresponding to the smallest scales, the resulting blow-up limits are non-flat smooth manifolds. The topology of the original manifolds $M_{i}$ may then be reconstructed from that of $V$, and the scale of orbifolds associated with each singular point $q \in V$ and its predecessors in $V^{j-1}$.

Each orbifold is of uniformly bounded topological type, with bounds depending only on $\Lambda, \nu_{o}$, $\delta_{0}$ and $C_{0}$, and hence there is a bound $K=K\left(\Lambda, \nu_{o}, \delta_{0}, C_{0}\right)$ on the number of topological types of
$\left\{M_{i}\right\}$. In particular, the homology groups of $M_{i}$ are determined, (by the Mayer-Vietoris sequence), by the homology of $V$ and the homology of the collection of ALE orbifold spaces $\left\{V^{j}\right\}$.

Remark 2.11. In a certain sense, the bound on $\sup _{B(r / 2)}|R|$ in the small curvature estimate (1.5) is a stronger assumption than the bound on the Ricci curvature in (1.2). For the applications of Theorem 1.1 in §3, this turns out to be irrelevant. However, it is perhaps worth noting that the bound on $\sup _{B(r / 2)}|R|$ can be replaced by bound on $\sup _{B(r / 2)} \mid$ Ric $\mid$, so that (1.5) may be replaced by the weaker condition
$$\sup _{B(r / 2)}|\operatorname{Ric}| \leq\left(\frac{C_{0}}{\operatorname{volB}_{x}(r)} \int_{B_{x}(r)}|R|^{n / 2} d V_{g}\right)^{2 / n},$$
in Theorem 1.1. We outline a proof of this, but do not give all the details, since this result is not used.

To see that (2.62) may be used in place of (1.5), observe that (1.5) is used in the proof of Theorem 1.1 in exactly two ways. First, it is used in the local version of the $C^{1, \alpha} \cap L^{2, p}$ Gromov compactness theorem. However, as in the proof of orbifold compactness under the bounds (1.2), under a smallness condition on the $L^{n / 2}$ norm of the curvature $R$ and a lower volume bound as in (1.4), such a compactness result holds with a bound on $\mid$ Ric $\mid$ in place of $|R|$, cf. [An3].

Second, the estimate on $\sup |R|$ is used in the proof of Theorem 1.2 (Steps 1 and 2) to obtain upper bounds on $\Delta r$ and $D^{2} r$ via comparison geometry. These estimates do require a bound on the full curvature $|R|$, not just on the Ricci curvature. However, given the bound (1.9) on the $L^{n / 2}$ norm of $R$ on ( $N, g$ ), the estimate (2.62) implies that $r^{2} \sup _{A(r, 2 r)} \mid$ Ric $\mid \rightarrow 0$ as $r \rightarrow \infty$ on ( $N, g$ ). Consequently, the $L^{2, p}$ harmonic radius $\rho$, (cf. (3.11) below), satisfies $\rho(x) \sim r(x)$ for $r(x)$ large. This means that the rescaled metrics $g_{r}$ are locally close to the flat metric in the $C^{1, \alpha}$ and weak $L^{2, p}$ topology on balls of uniform size. One may then smooth the metric, for instance by convolution with a smooth mollifier, to produce a nearby metric for which the estimate (1.5) holds. These local smoothings may then be patched together, via a partition of unity, to define a new metric $(N, \widetilde{g})$ on which (1.5) then holds. Applying Theorem 1.2 to $(N, \widetilde{g})$ gives then the same conclusion for the original metric $(N, g)$.

With these two modifications, the rest of the proof of Theorem 1.1 proceeds in exactly the same way. In fact, this discussion shows that (2.62) can be weakened even further, if desired. For example, it may be replaced by the bound
$$\left(\frac{1}{v o l B_{x}(r / 2)} \int_{B_{x}(r / 2)}|R i c|^{p} d V_{g}\right)^{1 / p} \leq\left(\frac{C_{0}}{v o l B_{x}(r)} \int_{B_{x}(r)}|R|^{n / 2} d V_{g}\right)^{2 / n}$$
for a fixed $p>n / 2$. One then obtains orbifold compactness in $C^{1, \alpha}$ and weak $L^{2, p}$, where $\alpha<2-\frac{n}{p}$.
Remark 2.12. From the proofs of Theorems 1.1 and 1.2, it is apparent that Theorem 1.1 holds for spaces of orbifolds satisfying the bounds (1.3)-(1.5).

\section*{3. Applications to Moduli of Critical Metrics.}

In this section, we prove Theorem 1.3 and related results on metrics which are critical points of natural Riemannian functionals on the space of metrics. For clarity, we divide this section into two subsections. In §3.1, we discuss some general results regarding the hypotheses of Theorem 1.1. In §3.2, we discuss Theorem 1.3, i.e. moduli of Bach-flat metrics as well as moduli of selfdual (or anti-selfdual) metrics on 4-manifolds, and remark on analogous results for critical metrics of other natural functionals on the space of metrics.
§3.1. This subsection is concerned with some general results relating to the hypotheses of Theorem 1.1.

Given a closed Riemannian $n$-manifold $(M, g)$, let $c_{S}$ be the Sobolev constant for the embedding $L^{2 n / n-2} \rightarrow L^{1,2}$ of Sobolev spaces; thus $c_{S}$ is the constant such that
$$c_{S}\left(\int_{M}|f|^{2 n / n-2}\right)^{n / n-2} \leq \int_{M}|d f|^{2}+\frac{c_{S}}{v o l M^{2 / n}} \int_{M} f^{2},$$
for any smooth function $f$ on $(M, g)$. Note that $c_{S}$ is scale-invariant. Recall also that a metric $\gamma$ on $M$ is a Yamabe metric if it minimizes the total scalar curvature functional restricted to the conformal class $[\gamma]$ of $\gamma$; this is equivalent to the statement that, for $n \geq 3$,
$$s_{\gamma} v o l M^{2 / n}\left(\int_{M}|f|^{2 n / n-2}\right)^{n / n-2} \leq \int_{M} c_{n}|d f|^{2}+\int_{M} s_{\gamma} f^{2},$$
for all smooth functions $f$ on $M$, where $c_{n}=4 \frac{n-1}{n-2}$ and $s_{\gamma}$ is the scalar curvature of $\gamma$.
Lemma 3.1. Let $g$ be a unit volume Yamabe metric on a closed $n$-manifold $M$, with scalar curvature $s_{g} \geq s_{0}>0$. Then there is a constant $\nu_{0}$, depending only on $n$ and $s_{0}$, such that
$$\begin{aligned}
& c_{S} \geq s_{0} / c_{n}, \quad \text { and } \\
& \operatorname{volB}_{x}(r) \geq \nu_{0} r^{n},
\end{aligned}$$
for all $r \leq \frac{1}{2} d i a m M$.
Proof: Both of these facts are standard and well-known. The estimate (3.3) follows trivially from (3.1)-(3.2). The estimate (3.4), while less trivial, is also easy to prove, cf. [Ak] for example. \(\square\)

Of course the estimate (3.4) corresponds to the non-collapse assumption (1.4) in Theorem 1.1. Regarding the global curvature bound in (1.4), one has the following, also standard, result.

Lemma 3.2. Let ( $M, g$ ) be a closed (oriented) Riemannian 4-manifold. Then
$$\begin{gathered}
\frac{1}{8 \pi^{2}} \int_{M}|R|^{2}=\chi(M)+\frac{1}{2 \pi^{2}} \int_{M}|z|^{2} \\
\frac{1}{16 \pi^{2}} \int_{M}|z|^{2}=-\chi(M)+\frac{1}{8 \pi^{2}} \int_{M}|W|^{2}+\frac{1}{8 \pi^{2}} \int_{M} \frac{s^{2}}{24}
\end{gathered}$$
and
$$\frac{1}{12 \pi^{2}} \int_{M}\left|W^{+}\right|^{2}-\left|W^{-}\right|^{2}=\tau(M) .$$
Here $R, W$ and $s$ are the Riemann, Weyl and scalar curvature, $z$ is the trace-free Ricci curvature, $z=$ Ric $-\frac{s}{4} g$, and $W^{ \pm}$are the selfdual and anti-selfdual parts of the Weyl curvature; $\chi(M)$ and $\tau(M)$ are the Euler characteristic and signature.

Proof: These statements (3.5)-(3.6) are just two related versions of the Chern-Gauss-Bonnet theorem in dimension 4. The equation (3.7) is a combination of the Chern-Weil theorem and the Hirzebruch signature formula, cf. [Be]. \(\square\)

We also recall Aubin's estimate on the scalar curvature of any unit volume Yamabe metric $g$ on any $M$ :
$$s_{g} \leq S_{0}=n(n-1) \sigma_{n}^{2 / n}$$
where $\sigma_{n}$ is the volume of the unit $n$-sphere in $\mathbb{R}^{n+1}$.
The estimate (3.5) implies an upper bound on the $L^{2}$ norm of the curvature $R$ of a metric on a 4 -manifold $M$, depending only on an upper bound on $\chi(M)$ and an $L^{2}$ bound on $z$; for Einstein metrics, one thus obtains an upper bound depending only on $\chi(M)$. Similarly, substituting (3.6) in
(3.5) and using (3.8) gives an upper bound for the $L^{2}$ norm of $R$ on a unit volume Yamabe metric, in terms of an upper bound for the $L^{2}$ norm of $W$ and a lower bound for $\chi(M)$.

Next we derive an $L^{p}$ analogue of the small curvature estimate (1.5).
Lemma 3.3. Let $B(1)$ be a geodesic ball centered at $x_{0}$ in a smooth Riemannian $n$-manifold $(M, g)$, and suppose the Ricci curvature of $g$ satisfies the inequality
$$\Delta|\operatorname{Ric}| \geq-d_{0}|R||\operatorname{Ric}|,$$
for some constant $d_{0}$, where $R$ is the curvature tensor of ( $M, g$ ). Then there is a constant $\delta_{0}$, depending only on $n$ and the Sobolev constant $c_{S}$ in (3.1), such that if $\left(\int_{B(1)}|R|^{n / 2}\right)^{2 / n} \leq \delta_{0}$, then
$$\left(\int_{B\left(\frac{1}{2}\right)}|R|^{p}\right)^{1 / p} \leq C_{0} \delta_{0}$$
where $C_{0}$ depends only on $n, p, d_{0}$ and $c_{S}$.
Proof: We assume $n, p, d_{0}$ are chosen, and that $c_{S}$ has a uniform lower bound. If $n=3$, then the Ricci curvature is algebraically equivalent to the full curvature $R$, and the proof is much easier in this case, cf. Remark 3.4 below. Thus, we assume $n \geq 4$.

Let $\rho=\rho^{2, p}$ be the $L^{2, p}$ harmonic radius of $B(1) \subset(M, g)$, cf. [An3]; basically, $\rho$ is the largest radius such that on any geodesic ball $B(\rho) \subset B(1)$, one has harmonic coordinates in which the metric components $g_{i j}$ are bounded by a fixed constant $Q$ in $L^{2, p}$ norm, in that
$$\begin{gathered}
Q^{-1} \delta_{i j} \leq g_{i j} \leq Q \delta_{i j}, \text { as bilinear forms, } \\
\rho^{2 p-n} \int_{B(\rho)}\left|\partial^{2} g_{i j}\right|^{p} d V \leq Q
\end{gathered}$$
where $Q$ is a fixed constant, $Q>1$. Thus, $\rho$ is small when the curvature is large in $L^{p}$ on $B(\rho)$. The radius $\rho$ scales as a distance. Let also $t(x)=\operatorname{dist}_{g}(x, \partial B(1))$.

Consider the minimal value $\mu$ of the (scale invariant) ratio $\rho / t$. The estimate (3.10) clearly holds if $\mu$ is uniformly bounded below, i.e. $\rho / t \geq \mu_{0}$, where $\mu_{0}=\mu_{0}\left(n, p, d_{0}\right)$. Thus, suppose $\rho(x) \ll t(x)$ for some $x \in B(1)$, so that the $L^{p}$ norm of the curvature becomes large near $x$. The minimal value $\mu$ is then achieved at some interior point $y_{0} \in B(1)$, and we rescale the metric $g$ at $y_{0}$ to a metric $g^{\prime}$ so that $\rho^{\prime}\left(y_{0}\right)=1$, where $\rho^{\prime}$ is the harmonic radius w.r.t. $g^{\prime}$. Then $t^{\prime}\left(y_{0}\right) \gg 1$, so that the $g^{\prime}$-distance of $y_{0}$ to the boundary is large. Moreover, the minimality property of $y_{0}$ then also gives
$$\rho^{\prime}(y) \geq \frac{1}{2}, \quad \forall y \in\left(B_{y_{0}}(2), g^{\prime}\right) .$$

The equation (3.9) and hypothesis on the $L^{n / 2}$ norm of $R$ are scale invariant, and so remain valid in the scale $g^{\prime}$. For simplicity, we drop the prime from the notation, so that one now has $\rho\left(y_{0}\right)=$ 1 , and $\rho(y)>\frac{1}{2}$, for all $y$ within distance 2 to $y_{0}$.

Since the metric is thus uniformly controlled in $L^{2, p} \subset C^{1, \alpha}$ on $B(2)$ a standard application of the DeGiorgi-Nash-Moser estimate for non-negative solutions of the elliptic inequality (3.9), cf. [GT,Thm.8.17], implies that
$$\sup _{B\left(\frac{3}{2}\right)}|\operatorname{Ric}|^{2} \leq C \int_{B(2)}|\operatorname{Ric}|^{2}+C\left(\int_{B\left(\frac{3}{2}\right)}|R|^{q}\right)^{2 / q}$$
where $q$ is any fixed number with $q>n / 2$ and $C=C\left(q, c_{S}\right)$. All balls are now centered at $y_{0}$. A standard interpolation inequality, cf. [GT, (7.10)], gives for $n / 2<q<p$
$$\|R\|_{L^{q}\left(B\left(\frac{3}{2}\right)\right)} \leq \varepsilon\|R\|_{L^{p}\left(B\left(\frac{3}{2}\right)\right)}+\varepsilon^{-\sigma}\|R\|_{L^{n / 2}\left(B\left(\frac{3}{2}\right)\right)},$$
for any $\varepsilon>0$, where $\sigma=(2 / n-1 / q) /(1 / q-1 / p)$. Also, from the fact that $\rho \geq \frac{1}{2}$ in B(2), we have
$$\|R\|_{L^{p}\left(B\left(\frac{3}{2}\right)\right)} \leq C\|R\|_{L^{p}(B(1))},$$
for a fixed constant $C$.
On the other hand, the Ricci curvature controls the metric in harmonic coordinates, and one also has the elliptic estimate
$$\|R\|_{L^{p}(B(1))} \leq C_{1}\left(\|\operatorname{Ric}\|_{L^{\infty}\left(B\left(\frac{3}{2}\right)\right)}+\|R\|_{L^{n / 2}\left(B\left(\frac{3}{2}\right)\right)}\right) .$$
coming from the well-known elliptic equation $(R i c)_{i j}=-\frac{1}{2} \Delta g_{i j}+Q(g, \partial g)$, (cf. [An3,(2.7)ff]). Choosing $\varepsilon$ small in (3.14), the combined equations (3.13)-(3.16) give the estimate
$$\|R\|_{L^{p}(B(1))} \leq C_{2}\left(\|R i c\|_{L^{2}(B(2))}+\|R\|_{L^{n / 2}\left(B\left(\frac{3}{2}\right)\right)}\right),$$
for some fixed constant $C_{2}$. Now the last term in (3.17) is bounded by $C_{2} \cdot \delta_{0}$. Similarly, since $\mid$ Ric $\left|\leq|R|\right.$, and since $n \geq 4$, the $L^{2}$ norm of the Ricci curvature is bounded by the $L^{n / 2}$ norm of the full curvature $R$. Thus (3.17) implies
$$\|R\|_{L^{p}(B(1))} \leq C_{3} \delta_{0} .$$
However, the $L^{p}$ norm of $R$ on $B(1)$ is on the order of $Q$ from (3.11). Hence, one has a contradiction if $\delta_{0}$ is sufficiently small. \(\square\)

Remark 3.4. If instead of (3.9) one has the inequality $\Delta|R| \geq-d_{0}|R|^{2}$, then (3.10) also holds. The proof in this case is a direct consequence of the DeGiorgi-Nash-Moser theorem, cf. [An1], [BKN]. Such an estimate holds for the curvature tensor of Einstein metrics, or more generally metrics with harmonic curvature, cf. [Be].
(ii). The same proof shows that (3.10) if the hypothesis on the $L^{n / 2}$ norm is replaced by other scale invariant bounds on the curvature. For example, the proof also holds in case one assumes
$$\sup _{B(r) \subset B(1)} \frac{1}{r^{n-2 s}} \int_{B(r)}|R|^{s} \leq \delta_{0}$$
for $2 \leq s \leq n / 2$.
Lemma 3.3 leads to the following strong or smooth version of the small curvature estimate (1.5).
Proposition 3.5. Let $B(1)$ be a geodesic ball in a smooth Riemannian $n$-manifold $(M, g)$ and suppose the Ricci curvature of $g$ satisfies an equation of the form
$$D^{*} D R i c=R * R i c,$$
where $R$ is the curvature tensor and $*$ denotes any algebraic operation of $R$ or its (irreducible) components on symmetric bilinear forms. Suppose in addition that $\left(\int_{B(1)}|R|^{n / 2}\right)^{2 / n} \leq \delta_{0}$, where $\delta_{0}$ is small, depending only on $n$ and $c_{S}$.

Then there is an $r_{0}=r_{0}\left(n, c_{S}\right)$ and harmonic coordinates on $B\left(r_{0}\right)$ such that
$$\|g\|_{C^{m, \alpha}\left(B\left(r_{0}\right)\right)} \leq K,$$
where $K$ depends only on $n, m, \alpha$, and $c_{S}$.
Proof: Taking the inner product of (3.20) with Ric gives
$$\frac{1}{2} \Delta|R i c|^{2}=|D R i c|^{2}+\langle R * R i c, R i c\rangle .$$
A simple application of the Cauchy-Schwartz inequality then implies
$$\Delta|\operatorname{Ric}| \geq-d_{0}|R||\operatorname{Ric}|,$$
for a constant $d_{0}$ depending only on the algebraic operator *. From Lemma 3.3, one thus has a uniform lower bound on the $L^{2, p}$ and therefore $C^{1, \alpha}$ harmonic radius. In particular, (3.21) holds with $m=1$.

Next, since the curvature is uniformly bounded in $L^{p}$ on $B\left(\frac{1}{2}\right)$, standard elliptic regularity, [GT, Ch.8] applied to the operator (3.20) expressed in local harmonic coordinates on $B\left(r_{0}\right)$, (in which the metric is $L^{2, p}$ ) implies that Ric is bounded in $L^{4, p / 2}$ on $B\left(r_{0} / 2\right)$. This, together with the fact that the $L^{2, p}$ harmonic radius is bounded below by $r_{0}$ implies that the $L^{4, p / 2}$ harmonic radius is bounded below by $r_{0} / 2$. It follows that the metric is controlled in $L^{4, p / 2}$, and so in $C^{3, \alpha}$ on $B\left(r_{0} / 2\right)$. By taking a suitable covering, it follows that the metric is controlled in $C^{3, \alpha}$ on $B\left(r_{0}\right)$. This process is then continued inductively to obtain (3.21). \(\square\)

Finally, we conclude with a remark on the Sobolev inequality. The Sobolev inequality implies a lower bound on the volume ratio of geodesic balls, as in (3.4). As is well-known, the converse is not true in general. This has the following consequence:

Proposition 3.6. Suppose $\left(M_{i}, g_{i}\right)$ satisfy hypotheses of Theorem 1.1, with (1.4) replaced by a lower bound on the Sobolev constant $c_{S}$. Let $V$ be a limit orbifold of $\left(M_{i}, g_{i}\right)$, so that any spherical space form $S^{n-1} / \Gamma_{j}$ in a cone $C\left(S^{n-1} / \Gamma_{j}\right)$ near a singular point $q \in V$ embeds in $M_{i}$, for $i$ large.

If some space-form $S^{n-1} / \Gamma$ near $q$ bounds a domain $U_{i} \subset M_{i}$, then the orbifold singularity $q$ is irreducible, so that $C\left(S^{n-1} / \Gamma\right)$ is the only cone at $q$ in $V$.

Proof: The proof is standard, although we include a proof for completeness. In the following, we assume that $i$ is sufficiently large, but drop the index $i$ from the notation. Since $(M, g)$ is close to $V$, and $S^{n-1} / \Gamma$ separates $M$, one has a decomposition $M=U_{1} \cup U_{2}$, where the union is along a neck region $A(\varepsilon, 2 \varepsilon)$ whose geometry, when scaled by $\varepsilon^{-1}$ is close to that of a standard annulus $A(1,2)$ in a standard cone $C\left(S^{n-1} / \Gamma\right)$. In particular, $\operatorname{vol} A(\varepsilon, 2 \varepsilon) \sim \varepsilon^{n}$. Let $v_{1}=\operatorname{vol} U_{1}, v_{2}=\operatorname{vol} U_{2}$ and assume $v_{1} \leq v_{2}$, so that $v_{1} \leq \frac{1}{2}$. Let $f$ be a function on $M$ with $f=1$ on $U_{1} \backslash A(\varepsilon, 2 \varepsilon), f=0$ on $U_{2} \backslash A(\varepsilon, 2 \varepsilon)$, with $|d f| \sim \varepsilon^{-1}$ on $A(\varepsilon, 2 \varepsilon)$. Using $f$ as a test function in the Sobolev inequality (3.1) gives
$$c_{S} v_{1}^{(n-2) / n} \leq c \varepsilon^{n-2}+c_{S} v_{1} .$$
Since $v_{1} \leq \frac{1}{2}, v_{1} \leq(1 / 2)^{2 / n} v_{1}^{(n-2) / n}$, and hence one has
$$c_{S} v_{1}^{(n-2) / n}\left(1-\left(\frac{1}{2}\right)^{2 / n}\right) \leq c \varepsilon^{n-2} .$$
Since $\varepsilon$ may be chosen to be arbitrarily small, (for $i$ sufficiently large), $v_{1}$ is arbitrarily small, for $i$ sufficiently large. It follows easily that $V$ contains only a single cone at $q$. \(\square\)

The hypothesis that $S^{n-1} / \Gamma$ bounds a domain in $M$ (or $M_{i}$ ) is automatically the case if for instance the Betti number $b_{n-1}(M)=0$, or equivalently $b_{1}(M)=0$, by Poincaré duality.

Remark 3.7. A lower bound on the Ricci curvature bound and upper and lower bounds on the volume of $(M, g)$ imply a lower bound on the Sobolev constant, cf. [Cr], [Ga]. Hence, these bounds imply irreducibility of all orbifold limits in Theorem 1.1. On the other hand, Remark 2.9 shows that in general, one may have many cones joined at a single orbifold singularity.

An interesting example illlustrating the fact that $S^{n-1} / \Gamma$ must bound a domain in Proposition 3.6 is the following. Let $M=M_{i}=S^{n-1} \times S^{1}$. There exists a sequence of conformally flat, unit volume Yamabe metrics $g_{i}$ on $M$ which satisfy the hypotheses of Theorem 1.1 and whose scalar curvatures tend to the maximal value $S_{0}$ in (3.8), cf. [Ko], [Sc]. Hence, there is a uniform Sobolev inequality on $\left(M, g_{i}\right)$ The limit $\left(V, g_{\infty}\right)$ is the round unit volume metric on $S^{n}$, with two antipodal points identified $\{q\} \sim\{-q\}$; at this point, one then has an orbifold singularity, consisting of two cones, each a ball, identified at the origin.
§3.2. We now apply the results above to critical metrics for natural functionals on the space of metrics.

Proof of Theorem 1.3.
Let $\mathcal{C}^{+}$be the space of unit volume Bach-flat Yamabe metrics on a given 4-manifold $M$, with scalar curvature $s_{g} \geq s_{0}$. Theorem 1.3 follows from Theorem 1.1 if we show that the hypotheses of the latter are satisfied.

First, the non-collapse estimate (1.4) follows from (1.14) and (3.4). The global curvature bound (1.3) follows from the bound (1.15) on the Weyl curvature, together the expression
$$\frac{1}{8 \pi^{2}} \int_{M}|R|^{2}=-7 \chi(M)+\frac{1}{\pi^{2}} \int_{M}|W|^{2}+\frac{1}{\pi^{2}} \int_{M} \frac{s^{2}}{24},$$
valid on any closed 4-manifold $(M, g)$, obtained by combining (3.5)-(3.6). The volume is normalized to 1 , and so the scalar curvature satisfies (3.8).

To obtain the small curvature estimate, observe that Bach-flat Yamabe metrics satisfy an equation of the form (3.20). Namely, the Bach equation (1.13) together with the Weitzenbock formula on vector valued 2-forms gives the equivalent equation
$$D^{*} D R i c+\frac{1}{3} D^{2} s+\frac{1}{6} \Delta s \cdot g+\mathcal{R}=0$$
where $\mathcal{R}=R * R i c$. This equation is conformally invariant. However, in the Yamabe normalization, $s=$ const , so the Hessian and Laplace terms vanish, so that
$$D^{*} D R i c+\mathcal{R}=0,$$
i.e. (3.20) holds for Bach-flat Yamabe metrics. The small curvature estimate (1.5) is then a consequence of Proposition 3.5. Theorem 1.3 is thus a consequence of Theorem 1.1. ■

Remark 3.8. With some further work, it can probably be shown that a Bach-flat Yamabe metric extends smoothly ( $C^{\infty}$ ) over $\{0\}$ in a local uniformization $B^{n} \backslash\{0\}$ of $C\left(S^{n-1} / \Gamma\right) \backslash\{q\}$. By means of a standard cutoff function argument, it is straightforward to see that $g$ is a weak solution of the equation (3.21) on the full ball $B^{n}$.

It is clear that Theorem 1.3 also holds if one allows the manifold $M$ to vary, provided, via (3.22), one assumes a uniform lower bound on the Euler characteristic of $M$. Again, we point out that the $L^{2}$ norm $\mathcal{W}$ of $W$ is constant on components of moduli spaces of Bach-flat metrics. Also, by Proposition 3.6, the limit orbifold is necessarily irreducible if $b_{1}(M)=0$, for instance if $M$ is simply connected. (Needless to say, Theorem 1.3 also holds for Bach-flat Yamabe metrics of non-positive scalar curvature, provided one assumes the bound (1.4)).

Examples of Bach-flat metrics, besides Einstein metrics, (which are necessarily Yamabe by Obata's theorem, cf. [Be,Ch.4]), are conformally flat metrics, and half-conformally flat metrics. A considerable theory for the existence of half-conformally flat metrics has been developed by Le-Brun, Taubes, and others, cf. [Le], [Ta] and references therein. Theorem 1.3 may be used to study aspects of the moduli spaces of such metrics.

For conformally flat metrics, (3.22) gives an upper bound on $L^{2}$ norm of $R$, depending only on a lower bound for $\chi(M)$. Hence, one has orbifold compactness, just depending on a lower bound for $\chi(M)$. A similar result holds for selfdual (or anti-selfdual) metrics. Thus suppose $W=W^{+}$, so that $W^{-}=0$. Substituting (3.7) in (3.22) then gives, for selfdual metrics,
$$\frac{1}{8 \pi^{2}} \int_{M}|R|^{2}=-7 \chi(M)+12 \tau(M)+\frac{1}{\pi^{2}} \int_{M} \frac{s^{2}}{24} .$$
Thus, one again has an upper bound on the $L^{2}$ norm of curvature, depending only on an upper bound for $-7 \chi(M)+12 \tau(M)$.

The formulas (3.5)-(3.7) have analogues for complete, non-compact ALE manifolds, (or orbifolds) $(N, g)$ satisfying the volume growth condition (1.8). All such ALE spaces which arise as blow-up limits of degenerating Bach-flat Yamabe metrics are necessarily scalar-flat. For simplicity, we thus state the formulas for scalar-flat ALE manifolds:
$$\begin{gathered}
\frac{1}{8 \pi^{2}} \int_{N}|R|^{2}=-7 \chi(N)+\frac{1}{\pi^{2}} \int_{N}|W|^{2}+7 \sum_{k=1}^{\kappa} \frac{1}{\left|\Gamma_{k}\right|} \\
\frac{1}{12 \pi^{2}} \int_{N}\left|W^{+}\right|^{2}-\left|W^{-}\right|^{2}=\tau(M)+\sum_{k=1}^{\kappa} \eta\left(S^{3} / \Gamma_{k}\right)
\end{gathered}$$
and, in the selfdual case
$$\frac{1}{8 \pi^{2}} \int_{N}|R|^{2}=-7 \chi(N)+12 \tau(N)+7 \sum_{k=1}^{\kappa} \frac{1}{\left|\Gamma_{k}\right|}+12 \sum_{k=1}^{\kappa} \eta\left(S^{3} / \Gamma_{k}\right) .$$

Corollary 3.9. Let $g$ be a complete self-dual, scalar-flat, metric on $\mathbb{R}^{4}$ satisfying
$$\int_{N}|R|^{2}<\infty, \quad \operatorname{vol} B_{x}(r) \geq \nu_{0} r^{4} .$$
Then $g$ is flat.
Proof: The metric $\left(\mathbb{R}^{4}, \mathrm{~g}\right)$ satisfies all the hypotheses of Theorem 1.2, and hence (3.28) holds. Since in this case $\kappa=1, \chi\left(\mathbb{R}^{4}\right)=1, \tau\left(\mathbb{R}^{4}\right)=0$ and $\Gamma=\{e\}$, the result follows. An alternate proof is to use (3.27) to see that $g$ is conformally flat. The Liouville theorem implies that a scalar-flat conformally flat metric on $\mathbb{R}^{4}$ is flat. \(\square\)

This result can be viewed as an analogue of the well-known result, (which follows from (3.7)) that the only self-dual metric on $S^{4}$ is the conformal class of the round metric. The condition (3.29) on the volume growth is necessary. For example, the Taub-NUT metric [Be,Ch.13] is a complete finite action selfdual Ricci-flat metric on $\mathbb{R}^{4}$ which is not flat.

Remark 3.10. Versions of Theorem 1.3 also hold for other natural functionals on the space of metrics. For example, in dimension 4, the Euler-Lagrange equations for the $L^{2}$ norms of the full curvature $R$, the Ricci curvature Ric or the trace-free Ricci curvature $z$,
$$\mathcal{R}^{2}=\int_{M}|R|^{2} d V, \quad \mathcal{R} i c^{2}=\int_{M}|\operatorname{Ric}|^{2} d V, \quad \mathcal{Z}^{2}=\int_{M}|z|^{2} d V,$$
are all of the form (3.20), cf. [Be,Ch.4]. Hence, any metric which is a critical point of such a functional satisfies the small curvature estimate (1.5). Such critical metrics also have constant scalar curvature; however, it is unknown if they are Yamabe metrics. Thus, it is not known if the lower volume bound (1.4) follows from a positive lower bound on the scalar curvature, and so (1.4) must be assumed. The bound (1.3) on the $L^{2}$ norm of the curvature follows from a bound on any of these functionals via (3.5). Under these hypotheses then, Theorem 1.3 also holds for moduli spaces of critical metrics of the functionals (3.30).

It is an interesting open problem whether Theorem 1.3 can be extended toward an understanding of the degeneration of Bach-flat Yamabe metrics with non-positive scalar curvature. This will necessarily include collapsing families of metrics, in the sense of Cheeger-Gromov, and the formation of limits with cusp-like ends. For Einstein metrics, such a study was carried out in [An4].

\section*{References}
\begin{itemize}
\item[] [Ak] K. Akutagawa, Convergence for Yamabe metrics of positive scalar curvature with integral bounds on curvature, Pacific Jour. Math. 175, (1996), 307-335.
\item[] [An1] M. Anderson, Ricci curvature bounds and Einstein metrics on compact manifolds, Jour. Amer. Math. Soc., 2, (1989), 455-490
\item[] [An2] M. Anderson, Short geodesics and gravitational instantons, Jour. Diff. Geom., 31, (1990), 265-275.
\item[] [An3] M. Anderson, Convergence and rigidity of manifolds under Ricci curvature bounds, Invent. Math. 97, (1990), 429-445.
\item[] [An4] M. Anderson, The $L^{2}$ structure of moduli spaces of Einstein metrics, Geom and Funct. Analysis, 2, (1992), 29-89.
\item[] [AC] M. Anderson and J. Cheeger, Diffeomorphism finiteness for manifolds with Ricci curvature and $L^{n / 2}$-norm of curvature bounded, Geom. and Funct. Analysis, 1, (1991), 231-252.
\item[] [B] S. Bando, Bubbling out of Einstein manifolds, Tohoku Math. Jour. 42, (1990), 205-216 and 587-588.
\item[] [BKN] S. Bando, A. Kasue and H. Nakajima, On a construction of coordinates at infinity on manifolds with fast curvature decay and maximal volume growth, Invent. Math, 97, (1989), 313-349.
\item[] [BL] D. Barden and H. Le, Some consequences of the nature of the distance function on the cut locus in a Riemannian manifold, Jour. London Math. Soc. 56, (1997), 369-383.
\item[] [Be] A. Besse, Einstein Manifolds, Springer Verlag, New York, 1987.
\item[] [CH] G. Carron and M. Herzlich, The Huber theorem for non-compact conformally flat manifolds, Comm. Math. Helv. 77, (2002), 192-220.
\item[] [CQY] S-Y. A. Chang, J. Qing and P.C. Yang, Compactification of a class of conformally flat 4-manifold, Invent. Math. 142, (2000), 65-93.
\item[] [C] J. Cheeger, Finiteness theorems for Riemannian manifolds, Amer. Jour. Math., 92, (1970), 61-74.
\item[] [CGl] J. Cheeger and D. Gromoll, The splitting theorem for manifolds of non-negative Ricci curvature, Jour. Diff. Geom. 6, (1971), 119-128.
\item[] [CG] J. Cheeger and M. Gromov, Collapsing Riemannian manifolds while keeping their curvature bounded I, II, Jour. Diff Geom, 23, (1986), 309-346, and 32, (1990), 269-298.
\item[] [Cr] C. Croke, Some isoperimetric inequalities and consequences, Ann. Sci. Ecole Norm. Sup, 13, (1980), 419-435.
\item[] [Ga] S. Gallot, Inégalites isopérimetriques, courbure de Ricci et invariants géométriques, C.R. Acad. Sci. Paris, 296, (1983), 365-368.
\item[] [GT] D. Gilbarg and N. Trudinger, Elliptic Partial Differential Equations of Second Order, 2nd Edition, Springer Verlag, New York, (1983).
\item[] [GW] R. Greene and H. Wu, Gap theorems for noncompact Riemannian manifolds, Duke Math. Journal, 49, (1982), 731-756.
\item[] [G] M. Gromov, Structures Metriques pour les Varietes Riemanniennes, Cedic-Fernand Nathan, Paris (1981).
\item[] [IT] J. Itoh and M. Tanaka, The Lipschitz continuity of the distance function to the cut locus, Trans. Amer. Math. Soc. 353, (2000), 21-40.
\item[] [Ka] A. Kasue, A Laplacian comparison theorem and function theoretic properties of a complete Riemannian manifold, Japan Jour. Math.8, (1982), 309-341.
\item[] [Ko] O. Kobayashi, Scalar curvature of a metric of unit volume, Math. Annalen, 279, (1987), 253-275.
\item[] [Le] C. LeBrun, Anti-self-dual metrics and Kähler geometry, Proc. Int. Cong. Math. (Zürich 1994), Birkäuser Verlag, Basel, (1995), 498-507.
\item[] [Lo] J. Lott, Manifolds with quadratic curvature decay and fast volume growth, Math. Annalen, 325, (2003), 525-541.
\item[] [PT] A. Petrunin and W. Tuschmann, Asymptotically flat manifolds and cone structure at infinity, Math. Annalen, 321, (2001), 775-788.
\item[] [Sc] R. Schoen, Variational theory for the total scalar curvature functional for Riemannian metrics and related topics, Springer Lecture Notes in Math., 1365, (1987), 120-154.
\item[] [SY] Y. T. Siu and S.T. Yau, Complete Kähler manifolds with nonpositive curvature of faster than quadratic decay, Annals of Math. 105, (1977), 225-264.
\item[] [Ta] C. Taubes, The existence of anti-self-dual metrics, Jour. Diff. Geom. 36, (1992), 163-253.
\item[] [Th] W. Thurston, The Geometry and Topology of Three-Manifolds, Vol. 1, Princeton University Press, (1997): see also online version at: http://www.msri.org/ publications/books/gt3m/
\item[] [TV] G. Tian and J. Viaclovsky, Bach-flat asymptotically locally Euclidean metrics, (preprint, Oct. 03), math.DG/0310302.
\item[] [TV2] G. Tian and J. Viaclovsky, Moduli spaces of critical Riemannian metrics in dimension four, (preprint, Dec. 03), math.DG/0312318
\end{itemize}

December, 2003/January, 2004
Department of Mathematics
SUNY at Stony Brook
Stony Brook, NY 11794-3651
anderson@math.sunysb.edu