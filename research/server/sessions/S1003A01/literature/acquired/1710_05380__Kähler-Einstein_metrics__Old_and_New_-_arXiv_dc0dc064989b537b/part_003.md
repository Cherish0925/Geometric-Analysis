---
retention_scope: session
part: 3
total_parts: 3
---

[Part 3/3 of: [1710.05380] Kähler-Einstein metrics: Old and New - arXiv]

The right geometric notion of weak limits we need to consider is given by the so-called Gromov-Hausdorff topology. This is a very weak topology on the class of isomorphism class of compact metric spaces, which has the advantage to make precise what one means for convergence of a smooth Riemannian manifold to a (potentially) singular space. Thus, in the next section we will recall some of the basic definitions and properties of such notion.

The next sections can be understood as a geometric way to do a priori estimates and study regularity for our KE equations.
6.3. Gromov-Hausdorff basics ("weak limits"). Let $\left(X, d_{X}\right)$ and $\left(Y, d_{Y}\right)$ be two compact metric spaces. Define the following Gromov-Hausdorff (GH) (pseudo-)distance:
$$d_{G H}(X, Y)=\inf _{Z \hookleftarrow \mathrm{isom} X, Y} \inf \left\{\varepsilon \geq 0 \mid \mathcal{N}_{\varepsilon}^{Z}(X) \supseteq Y, \mathcal{N}_{\varepsilon}^{Z}(Y) \supseteq X\right\},$$
where $\mathcal{N}_{\varepsilon}^{Z}(-)$ denotes the $\varepsilon$-neighborhood of a set in $Z$. It can be easily shown that $d_{G H}(X, Y)=0$ implies that $X$ and $Y$ are isometric. Thus, the space of compact metric spaces modulo isometries is itself a metric space. Such "universal" space can be used to study degeneration of Riemannian
manifolds to singular spaces. A usual way to bound the GH distance to study convergence in such "weak" GH topology is by finding functions $f: X \rightarrow Y$ which are $\varepsilon$-dense and $\varepsilon$-isometries.

A crucial question is to find criteria of convergence in such GH topology (pre-compactness), i.e. given a sequence $\left(X_{i}\right)$ of compact metric spaces, find conditions which guarantee that such sequence subconverges to a compact metric space $X_{\infty}$.

The fundamental result is the Gromov's pre-compactness theorem. A set $\mathcal{X}$ of compact metric spaces is uniformally totally bounded (UTB) if:
\begin{itemize}
\item[-] $\exists D>0$ such that $\operatorname{diam}(X)<D$ for all $X \in \mathcal{X}$;
\item[-] $\forall \varepsilon>0, \exists N=N(\varepsilon)$ such that for all $X \in \mathcal{X}, \exists S_{X} \varepsilon$-dense set of cardinality at most $N$.
\end{itemize}

Theorem 6.4 (Gromov's pre-compactness). If $\mathcal{X}$ is UTB, then $\mathcal{X}$ is pre-compact.
The proof is simple (for more details and for more references on GH topology see [BBI01]). The idea is to uniformly discretize the spaces in the family, apply a diagonalization argument, and take a metric completion to get a compact limit space. More precisely, let $\mathcal{X} \in X_{n} \supseteq S_{n}:=$ $S_{n, 1} \cup S_{n, \frac{1}{2}} \cup \cdots=\left\{x_{i, n}\right\}_{i=1}^{\infty}$ where $S_{n, \frac{1}{j}}$ is a finite $\frac{1}{j}$-dense set with at most $N\left(\frac{1}{j}\right)$ points independent of $n$. Since $d_{i j}^{n}:=d_{X_{n}}\left(x_{i, n}, x_{j, n}\right)<D$, by diagonalization we can find a subsequence $n_{k}$ such that $d_{i j}^{n_{k}} \rightarrow d_{i j}$. Take $S$ a countable set and equip it with the pseudo-distance $d_{i j}$. Then its metric completion after identification between points of zero distance $X_{\infty}=\overline{S / d}$ is a compact metric space which is the GH limit of the sequence $X_{n_{k}}$.

Thus, given families of Riemannian manifolds, it becomes interesting to find conditions which will implies that the family is UTB in the GH distance. The idea is that if we have a uniform control of the volume of small balls, we may hope to control uniformly the number of them we need to cover a manifolds. It is in such consideration that the Ricci curvature enters the game! Recall that in normal coordinates centered at $p$, the Ricci tensor exactly measure the second order deviation of the volume form from the flat Euclidean measure:
$$d V_{g}=\left(1-\frac{1}{6} \sum_{i, j} \operatorname{Ric}_{i j}(p) x_{i} x_{j}+O\left(x^{3}\right)\right) d \underline{x} .$$
A global result on the behaviour of volume under Ricci lower bounds is given by the following crucial result. Let $H_{c}$ be the $n$-dimensional simply-connected space of constant sectional curvature equal to $c$. Then:

Theorem 6.5 (Bishop-Gromov monotonicity). If $\operatorname{Ric}(g) \geq(n-1) c g$, for $c \in \mathbb{R}$, then the function $\frac{\operatorname{Vol}\left(B_{g}(p, r)\right)}{\operatorname{Vol}\left(B_{H_{c}}(r)\right)}$ is non-increasing.

See [BBI01] for its proof. Its immediate consequence is:
Theorem 6.6 (Riemannian Gromov's precompactness). The set of $n$-dimensional Riemannian manifolds with $\operatorname{diam}(M, g) \leq D$ and $\operatorname{Ric}(g) \geq c(n-1) g$ is GH pre-compact.

Proof. It is sufficient to check the UTB property. Take $\left\{x_{i}\right\}$ a maximally $\varepsilon$-separated set, i.e. $\left\{x_{i}\right\}$ is $\varepsilon$-dense and $B\left(x_{i}, \frac{\varepsilon}{2}\right)$ are disjoint. Then, by monotonicity:
$$\left|\left\{x_{i}\right\}\right| \leq \frac{\operatorname{Vol}(M, g)}{\operatorname{Vol}\left(B_{g}\left(x_{i}, \frac{\varepsilon}{2}\right)\right)} \leq \frac{\operatorname{Vol}\left(B_{H_{c}}(D)\right)}{\operatorname{Vol}\left(B_{H_{c}}\left(\frac{\varepsilon}{2}\right)\right)} .$$
Since the last term in the above expression depends only on $c, D$, and $\varepsilon$, we are done. \(\square\)

If in the above theorem $c>0$, then the diameter is automatically bounded thanks to Myers' theorem. In particular, let us note that the set of $n$-dimensional KE Fano manifolds is GH precompact, i.e. given any sequence of them we can extract a subsequence converging to a compact metric space.

Remark 6.7. If the diameter bound does not hold, one still have pre-compactness in the pointed GH sense: by choosing a sequence of points $p_{i} \in M_{i}$, for all $r>0$, closed $r$-balls centered at $p_{i}$ sub-GH-converge to closed $r$-balls and center $p_{\infty}$ in a metric space $X_{\infty}$ (in general non-compact). In particular, this notion of convergence is important in the analysis of metric bubbles and tangent cones -both arising from "unbounded" rescalings (zoomings)- to study singularities of limits of compact Einstein spaces.

In our problem, we need to consider limits of conical KE metrics. It is still possible to show that one can take limit in the GH topology also in this case (for example, but it is not trivial, it is possible to show that the cone angle can be "smoothed out" to genuine Riemannian metrics with lower bounds on the Ricci curvature and with control on their diameter [CDS15, part I]). Thus we can assume that our sequence in the Donaldson's continuity path $\left(X, \omega_{\beta_{i}}\right)$ subconverge in GH to a compact metric space $X_{\infty}$. This is the "weak limit". Now we need to do some "regularity"!
6.4. Cheeger-Colding Theory ("smooth regularity"). In general, Cheeger-Colding(-Tian, for the Kähler case) theory, studies regularity of the GH limits $X_{\infty}$ of sequences of Riemannian manifolds with Ricci bounded below. See survey [Che01]. In our situation we can (essentially) restrict to the Einstein case with volume non-collapsing hypothesis $\operatorname{Vol}(B(p, 1))>C>0$ (observe that if Ricci is positive, this is a simple consequence of Bishop-Gromov monotonicity). We focus on the absolute case, i.e. no conical manifolds. This case is interesting in itself (e.g. moduli compactifications in the KE Fano case), and still central in the more technical case of conical KE.

From a historical perspective, such theory generalizes results of Andersen, Bando, Kazue, Nakajima, and Tian of the ends of the eighties for the real four dimensional case, based on Ulhenbeck's $\varepsilon$-regularity techniques. In particular, under the above assumptions, they were able to show orbifolds compactness: i.e. $X_{\infty}$ is a smooth Einstein space away from finitely many points which can be locally modeled on $\mathbb{R}^{4} / \Gamma_{p}$ (where $\Gamma_{p} \subset S O(4)$ is a finite subgroup acting freely on the 3 -sphere, so that the metric pull-back to a smooth tensor (orbifold smooth metric).

In Cheeger-Colding theory "almost rigidity" theorems are used to define stratification of the limit space $X_{\infty}$. A prototypical example of rigidity theorem in smooth Riemannian geometry is given by the Cheeger-Gromoll splitting theorem: a complete Riemannian manifold $(M, g)$ with non-negative Ricci containing a line (i.e. an infinity length geodesic $\gamma:(-\infty, \infty) \rightarrow M$, whose subsegments are always minimizing) must be isometric to the split product $M \simeq N \times \mathbb{R}$. The idea of the proof consists in considering Busemann functions $b_{\gamma^{ \pm}}(p):=\lim _{t \rightarrow \pm \infty} d\left(p, \gamma^{ \pm}(t)\right)-t$. Using Laplacian comparison for the distance function under the Ricci curvature bound hypothesis, one can show that $b_{\gamma^{ \pm}}$are sub-harmonic. Since $b_{\gamma^{+}}+b_{\gamma^{-}} \geq 0$ taking value zero exactly on the image of $\gamma$, by the maximum principle the function $b_{\gamma^{+}}=-b_{\gamma^{-}}$is harmonic. Finally, by Bochner's formula the unit length vector field $\nabla b_{\gamma^{+}}$must be parallel, and thus its flow gives the desired splitting.

By performing an analysis of "approximate Busemann functions" via integral estimates, Cheeger-Colding theory provides the following "quantitative" version of the above theorem, known as almost splitting theorem. Let
\begin{itemize}
\item[-] $\operatorname{Ric}(g) \geq-(n-1) \delta g(\operatorname{think} \delta \ll 1)$;
\item[-] $p, q^{+}, q^{-} \in M$, with $d\left(p, q^{ \pm}\right) \geq L \gg 1$ and $d\left(p, q^{+}\right)+d\left(p, q^{-}\right)-d\left(q^{+}, q^{-}\right) \leq \varepsilon \ll 1$.
\end{itemize}
Then $\exists$ a ball $B_{R} \subseteq \mathbb{R} \times X$, with $X$ length space, such that $d_{G H}\left(B(p, R), B_{R}\right) \leq \phi\left(\delta, L^{-1}, \varepsilon \mid R\right)$, i.e. for fixed $R, \phi \rightarrow 0$, as $\delta, L^{-1}, \varepsilon, \rightarrow 0$.

As a corollary one sees that, by rescaling, pointed GH limits of sequences $\left(M_{i}, g_{i}, p_{i}\right)$ with Ricci bounded below must split if they contain a line, since $\operatorname{Ric}\left(\lambda_{i} g_{i}\right) \rightarrow 0$ for $\lambda_{i} \rightarrow \infty$.

More generally, this result, combined with "volume cones are metric cones", is the basis of the following structural picture for GH limits $\left(M_{i}, g_{i}\right) \rightarrow X_{\infty}$ of manifolds with Ricci bounded below, bounded diameter and volume non-collapsing.

Take $p \in X_{\infty}$ and define a (non-necessarily unique!) metric tangent cone at $p$ to be $C_{p}\left(X_{\infty}\right):=$ $\lim _{p G H}\left(X_{\infty}, p, \lambda_{i} d_{\infty}\right)$ as $\lambda_{i} \rightarrow \infty$. Then $C_{p}\left(X_{\infty}\right)=\mathbb{R}^{k} \times C(Y)$ with $C(Y)$ a metric cone (i.e. $d\left(\left(r_{1}, y_{1}\right),\left(r_{2}, y_{2}\right)\right)=\sqrt{r_{1}^{2}+r_{2}^{2}-2 r_{1} r_{2} \cos \left(d_{Y}\left(y_{1}, y_{2}\right)\right)}$ of diameter less than $\pi$ and $n-k$ Hausdorff dimension. Note that the link $Y$ may be singular. Define the regular set
$$\mathcal{R}:=\left\{p \in X_{\infty} \mid \exists C_{p}\left(X_{\infty}\right) \cong \text { isom } \mathbb{R}^{n}\right\},$$
which do not need to be open, and the singular strata for $k \in \mathbb{N}$,
$$\mathcal{S}:=X_{\infty} \backslash \mathcal{R} \supseteq \mathcal{S}_{k}:=\left\{p \in X_{\infty} \mid \text { no tangent cones at } p \text { splits } \mathbb{R}^{k+1}\right\} .$$

Summarizing some of the main results of Cheeger-Colding theory:
Theorem 6.8. Let $\mathcal{S}_{0} \subseteq \cdots \subseteq \mathcal{S}_{n-2}=\mathcal{S} \subseteq X_{\infty}$ with Hausdorff dimension $\operatorname{dim}_{\mathcal{H}} \mathcal{S}_{k} \leq k$. If Ricci has two side bounds then $\mathcal{R}$ is open (actually a $\mathcal{C}^{1, \alpha}$ manifold, $\mathcal{C}^{\infty}$ if the metrics are Einstein). If $g_{i}$ are $K E$ then $S=S_{n-4}$ (Cheeger-Colding-Tian).

Let us go back to discuss in more details the Kähler situation.
6.5. Donaldson-Sun Theory ("algebraic regularity"). Let $X_{\infty}$ be a limit of smooth complex $n$-dimensional KE Fano manifolds $\left(M_{i}, g_{i}\right)$. The conical KE case is more technical, but part of the ideas can be already seen in this "absolute" situation. By Cheeger-Colding regularity we know that $\operatorname{dim}_{\mathcal{H}} X_{\infty}=2 n$, its singular set agrees with $\mathcal{S}_{2 n-4}$ stratum, the regular set is open and on it we can find a (incomplete) smooth KE metric $g_{\infty}$. Moreover, for all compact subset $K \subset \subset \mathcal{R}$ there exists diffeomorphisms onto their images $\psi_{i}: K \rightarrow M_{i}$ such that $\psi_{i}^{*} g_{i} \rightarrow g_{\infty}$ in $\mathcal{C}^{1, \alpha}$, and similarly for the complex structures $J_{i}$.

Not too surprisingly, the metric cones are now complex cones: $C_{p}\left(X_{\infty}\right) \cong_{\text {isom }} \mathbb{C}^{k} \times C(Y)$, with $C(Y)$ a Calabi-Yau cone, i.e. $\omega_{C(Y)}=\frac{\sqrt{-1}}{2} \partial \bar{\partial} r_{0}^{2}$ where $r_{0}$ is the distance from the apex of the cone, and $\operatorname{Ric}\left(\omega_{C Y}\right)=0$. The link $Y$ is a potentially singular (Sasaki)-Einstein space with positive scalar curvature.

The main results of Donaldson and Sun [DS14] says the following:
Theorem 6.9. The $G H$ limit $X_{\infty}$ is naturally homeomorphic to $W \subseteq \mathbb{C P}^{n}$ a singular Fano variety with $\mathcal{S}\left(X_{\infty}\right)=\operatorname{Sing}(W)$.

The rough (and very imprecise!) idea consists in proving a uniform Kodaira embedding using the pick sections method "near the singularities" ("on metric tangent cones"). The main technical result used in their proof is known as partial $\mathcal{C}^{0}$-estimates. Let $b_{k}^{K E}(p)=\sum_{i}\left|s_{i}(p)\right|_{h_{K E}^{k}}^{2}$ be the Bergman Kernel using holomorphic sections $L^{2}$-orthonormal with respect to KE metrics. Then

Proposition 6.10. $\exists k_{0}=k_{0}(n, V), b=b(n, V)$ so that $b_{k_{0}}^{K E} \geq b^{2}>0$ for all $K E X^{n}$ of volume $V$.
Then the identification of the GH limit with a complex variety follows by comparing the GH limit $X_{\infty}$ with the "flat limit" obtaining as limit of the image $T_{i}^{k}\left(X_{i}\right)$ via Tian's $L^{2}$ orthonormal embedding $T_{i}^{k}$, for a fixed bounded $k$.

To bound the Bergman's kernel, we need to construct a pick section at any $p$ (i.e. $s \in H^{0}\left(K_{X_{i}}^{-k_{0}}\right)$ non vanishing at $p$ ), also, and crucially, near the singularity formations, with some uniform control. The idea would be to trivialize the canonical on $U_{i}$ near $p$ with a local section $\sigma_{0}=1$. By cutting-off
$\sigma:=\chi \sigma_{0}$ we have a global smooth section picked at $p$ and holomorphic near $p$ and on the complement of $U_{i}$ (where is identically zero). Next we want to solve the $\bar{\partial}$-equation $\bar{\partial} \tau=\bar{\partial} \sigma$ with estimates (of Hörmander's $L^{2}$-type), so that $s:=\sigma-\tau$ will be fully holomorphic and picked. We need to find a nice $U_{i}$. The crucial idea is that, instead of working on $X_{i}$, we can work near the tip of a metric tangent cone, and then transplant the region on $X_{i}$ via the diffeomorphism $\phi_{i}$ provided by Cheeger-Colding theory. Working on such a region it is possible to construct a $\sigma_{0}$ on the tangent cone (as outlined above), whose $\bar{\partial}$ is small in $L^{2}$ (via a good cut of function). Define $\tau:=\bar{\partial}^{*} \Delta_{\bar{\partial}^{*}}^{-1} \bar{\partial} \phi_{i}^{*} \sigma_{0}$. Here $\Delta_{\bar{\partial}^{*}}$ is the Laplacian on $(1,0)$ forms valued the $k$-plurianticanonical bundle. It is uniformly invertible for $k$ big enough, since by Bochner's formula $\Delta_{\bar{\partial}^{*}}=\nabla^{*} \nabla+\frac{1}{k} \operatorname{Ric}(\omega)+1$, we have $\left(\Delta_{\bar{\partial}^{*}}(s), s\right)_{L_{k \omega}^{2}} \geq \frac{1}{2}|s|_{L_{k \omega}^{2}}^{2}$. Let $\sigma:=\phi_{i}^{*} \sigma_{0}-\tau$. Then it is holomorphic. Moreover $|\tau|_{2}^{2} \leq 2\left|\bar{\partial} \phi_{i}^{*} \sigma_{0}\right|_{2}^{2}$ which is small. By Moser's iteration its $\mathcal{C}^{1}$-norm is also small. Thus $\left|\sigma\left(\phi_{i}^{-1}(p)\right)\right| \geq C\left(k_{0}\right)>0$, for a $k_{0}$ bounded by the geometry independent of $i$. Since also $\nabla \sigma$ is bounded uniformly, $T_{i}$ are Lipschitz and converge to some continuous map $T_{\infty}$ which identifies the GH limit $X_{\infty}$ with the flat limit.

Remark 6.11. In reality, to get Theorem 6.9 from Proposition 6.10 is necessary to raise further (in a bounded way) the $k_{0}$ constant (in order to really separate points in the limit). Of course there are many other difficulties we haven't discussed in the oversimplified sketch given above.

Remark 6.12. • For the conical case, the limit is a Fano variety $W$ equipped with a (singular) limit divisors $D_{\infty}$ where, generically, the singular limit KE metric is going to have some cone angle singularities in the transverse directions to smooth point of $D_{\infty}$.
\begin{itemize}
\item[-] It can be proved that the singularities of the limit are Kawamata log terminal (klt), that is $K_{\hat{X}}=\phi^{*} K_{X}+\sum a_{i} E_{i}$, with $a_{i}>-1$ for any divisorial resolutions of the singularities (since this is essentially equivalent to say that near the singularity there is a (root) of a holomorphic volume form $\Omega$ such that $\int_{U} \Omega \wedge \bar{\Omega}<+\infty$ ). In dimension two these singularities coincide with quotient singularities, thus recovering the orbifold theory. However, in higher dimension this is not the case, e.g. the ODP singularity $\sum_{i=0}^{n} x^{2}=0$ is not of quotient type as long as $n \geq 3$. Moreover, the understanding of the metric near such singularities is much more subtle, but there are very important recent results in such direction [DS17]. .
\item[-] It can be shown that the singular limit KE metrics are weak KE in the pluripotential theory sense [EGZ09].
\end{itemize}
6.6. Summing-up: the idea of the proof. Let us now go back to the Donaldson continuity path and say that $X_{\infty}$ is the GH limit of a sequence of increasing conical KE $\left(M, \omega_{\beta_{i}}\right)$, with $\beta_{i} \nearrow \underline{\beta}$ solving (13). Then, by the above regularity theories, we can assume that $X_{\infty} \cong\left(W, D_{\infty}, \omega_{\underline{\beta}}\right)$ for a weak (log) KE Fano pair. We are now again in the domain of algebraic geometry! The main trick is now to use such $\left(W, D_{\infty}, \omega_{\underline{\beta}}\right)$ to construct a test configuration so that we can use the K-stability hypothesis.

The first step consists in extending the Donaldson-Futaki invariant to the pair setting: $(\mathcal{X}, \mathcal{D}) \rightarrow$ $\mathbb{C}$, with $D F((X,(1-\beta) D),(\mathcal{X},(1-\beta) D)):=D F(X, \mathcal{X})+(1-\beta) \tilde{F}(D)$ in a natural way: if $\left(X, D, \omega_{\beta}\right)$ is a singular space with a weak conical metric, then for a test configuration induced by holomorphic vector fields tangential to $D$, we have $D F(\mathcal{X},(1-\beta) D)=F_{D}(v)$, for the natural extension of the Futaki type invariant [LS14], as in Proposition 5.13. In particular, if $\omega_{\beta}$ is conical $\mathrm{KE}, D F(\mathcal{X},(1-\beta) D)=0$ for such test configurations. Note the linearity in $\beta$ of the conical (log) version of the Futaki invariant.

If $\left(W, D_{\infty}\right) \cong(M, D)$ we would have done by uniqueness of the KE metric. If not, then by Donaldson-Sun we know that $\left(W, D_{\infty}\right)$ is realized as a flat limit of $(M, D)$ with some "universal" projective space $\mathbb{C P}^{n_{k}}$, for fixed uniform $k$. In particular $\left(W, D_{\infty}\right) \in \overline{\operatorname{PGL}\left(n_{k}\right) .(M, D)}$. Since $\left(W, D_{\infty}, \omega_{\underline{\beta}}\right)$ is KE, by an extension of Matsushima's reductivity, we have that $\operatorname{Aut}\left(W, D_{\infty}\right)$ is
reductive. Hence, by the standard Luna's slice theorem for reductive groups, we can assume that there exists a $\mathbb{C}^{*} \hookrightarrow \operatorname{Aut}\left(W, D_{\infty}\right) \subseteq \operatorname{PGL}\left(n_{k}\right)$ so that $(W, D)=\lim _{t \rightarrow 0} t .(M, D)$, i.e. $(W, D)$ is the central fibre for a test configuration! In particular, for such test configuration the log Futaki invariant is zero for parameter $\underline{\beta}$ since the central fibre has a KE metric. By linearity of the Futaki invariant, this implies that the "absolute" Futaki invariant for $X$ has to be negative. But this contradicts our K-stability hypothesis. Thus only case one is indeed possible, and we can repeat the argument until $\underline{\beta}=1$, and finally construct a smooth KE metric on $X$ ! Be aware that the fact that cone angle metrics open up to usual smooth KE metrics is far from being a triviality, even if it is very intuitive.

This concludes the sketch of the arguments for proving Theorem 0.3.
Remark 6.13. • There are now different proofs of the equivalence between KE metric and K-stability: via the original Aubin's path [DS16], via Ricci flow [CSW15], via Calculus of Variations [BBJ15, Dem17].
\begin{itemize}
\item[-] Checking K-stability to construct new KE metric is still very hard (if not impossible at the present state-of-the art!) due to the too many test configurations which a priori needed to be checked. Understanding better this issue is definitely a crucial aspect of future investigations in the field.
\end{itemize}
6.7. KE moduli spaces and explicit examples. Let
$$\overline{\mathcal{E M}}^{G H}:={\overline{\left\{\left(X^{n}, \omega\right) \mid \omega \text { is KE Fano }\right\} / \text { biholo-isom }}}^{G H}$$
be the compactification of the moduli space of KE Fano manifolds obtained by adding the singular weak KE spaces coming from GH-degenerations. In some sense, these spaces can be thought as higher dimensional generalizations of the Deligne-Mumford moduli compactification in the curve case, but now for the positive KE case. Thus, it should be not too surprisingly that it can be shown that such GH compactifications admit a natural structure of complex variety. Sometime they are also known as K-moduli space $\mathcal{K} \mathcal{M}$, for obvious reasons. Can we find explicit examples of such $\overline{\mathcal{E M}}^{G H}$ ? This is important since testing K-stability, as we said, is still very hard: if we can explicitly described such moduli spaces in concrete situations, then we can understand exactly which Fano varieties in given families are indeed KE/K-polystable.

The idea to study such problem is via a "moduli continuity method": that is, given a family $\mathcal{X} \rightarrow H$ of Fano varieties, we would like to study the set of parameters for which the fibre variety $X_{t}$ admits a KE metrics. If we can prove that there exists at least one fibre which is KE, that the KE condition is essentially open (in ideal situations) and that abstract GH limits are actually naturally embedded in our starting family, it is possible to conclude (via "stability comparison") that $\overline{\mathcal{E M}}_{d}^{G H}=\mathcal{H}_{d} / / G$, where $d$ is some numerical parameter (as the volume/degree) and $G$ is a group acting on the parameter space giving a classical GIT quotient. In particular, K-stability would be equivalent to GIT for such family, and GIT stability can be in principle checked by hand. This strategy has been used for fully understanding the two dimensional case in [OSS16], extending results of [Tia90a, MM93].

For example one can study cubic surfaces in $\mathbb{C P}^{3}$. Their defining coefficient form a parameter space $\mathcal{H}_{3}=\mathbb{C P}^{19}$ on which the group $\operatorname{SL}(4, \mathbb{C})$ acts naturally by reparameterization. The Fermat cubic $x^{3}+y^{3}+z^{3}+t^{3}=0$ is know to have alpha invariant bigger than 2/3 and hence is KE. By implicit function theorem one can see that, among smooth cubic, the KE condition is open since they have only discrete automorphisms (actually, by [Tia90a] we also know that smooth ones are all KE). In any case let $X_{\infty} \cong W$ an abstract GH limit, which has only isolated orbifold singularities by the general regularity theory of degenerate limit recalled above. Then, by Bishop-Gromov inequality, we can compare the metric density at singular points with the total volume. This gives
that $3=c_{1}^{2}(W)<12 \sharp\left(\Gamma_{p}\right)^{-1}$. In particular, $\Gamma_{p} \cong \mathbb{Z}_{2}, \mathbb{Z}_{3}$. It can be shown that in such case only the $S U(2)$ representations survives (related to the notion of $\mathbb{Q}$-Gorenstein smoothability, which is a consequence of Donaldson-Sun theory). This means that $W$ has only $A_{k}$ singularities of the form $x^{2}+y^{2}=z^{k+1}$ with $k \leq 2$. It is a known result that two dimensional Fano varieties of degree three with such singularities have still very ample anti-canonical bundle, which thus provides embeddings $W \subseteq \mathbb{C P}^{3}$. By Berman results we know that $W$ is K-polystable (since singular KE). It is then easy to see in such case that K-polystability implies GIT-polystabilty for the essentially unique linearization of the $S L(4, \mathbb{C})$ action. Thus, with some further work, $\overline{\mathcal{E M}}_{3}^{G H} \cong \mathcal{H}_{3} / / S L(4, \mathbb{C})$. The study of such GIT problem goes back to Hilbert. In particular, it is known that cubics with at worse $A_{1}$-singularities are stable, and only (the orbit of) the toric $x y z=t^{3}$ (with $3 A_{2}$ singularities), is strictly polystable. Thus this classifies also all the cubics which are KE.

Remark 6.14. Very recently, new techniques (e.g. [Li15a, Liu16]) based on better understanding of the metric tangent cones in higher dimension and their relations with algebraic geometry, made possible to study in concrete situations such moduli spaces in higher dimensions too (e.g. [SS17, LX17]).

\section*{References}
[Aub76] Th. Aubin, Équations du type Monge-Ampère sur les variétés kähleriennes compactes, C. R. Acad. Sci. Paris Sér. A-B 283 (1976), no. 3, Aiii, A119-A121. (Cited on p. 2, 10)
[Aub78] Th. Aubin, Équations du type Monge-Ampère sur les variétés kählériennes compactes, Bull. Sci. Math. (2) 102 (1978), no. 1, 63-95. (Cited on p. 2, 10)
[Aub84] Th. Aubin, Réduction du cas positif de l'équation de Monge-Ampère sur les variétés kählériennes compactes à la démonstration d'une inégalité, J. Funct. Anal. 57 (1984), no. 2, 143-153. (Cited on p. 11)
[Aub98] Th. Aubin, Some nonlinear problems in Riemannian geometry, Springer Monographs in Mathematics, Springer-Verlag, Berlin, 1998. (Cited on p. 11, 13, 16)
[Bal06] W. Ballmann, Lectures on Kähler manifolds, ESI Lectures in Mathematics and Physics, European Mathematical Society (EMS), Zürich, 2006. (Cited on p. 3)
[BM87] S. Bando, T. Mabuchi, Uniqueness of Einstein Kähler metrics modulo connected group actions, in Algebraic geometry, Sendai, 1985, 11-40, Adv. Stud. Pure Math., 10, North-Holland, Amsterdam, 1987. (Cited on p. 23)
[Ber13] R. J. Berman, A thermodynamical formalism for Monge-Ampère equations, Moser-Trudinger inequalities and Kähler-Einstein metrics, Adv. Math. 248 (2013), 1254-1297. (Cited on p. 36)
[Ber16] R. J. Berman, K-polystability of $\mathbb{Q}$-Fano varieties admitting Kähler-Einstein metrics, Invent. Math. 203 (2016), no. 3, 973-1025. (Cited on p. 3, 34)
[BB17] R. J. Berman, B. Berndtsson, Convexity of the K-energy on the space of Kähler metrics and uniqueness of extremal metrics, J. Amer. Math. Soc. 30 (2017), no. 4, 1165-1196. (Cited on p. 23)
[BBJ15] R. Berman, S. Boucksom, M. Jonsson, A variational approach to the Yau-Tian-Donaldson conjecture, arXiv:1509.04561. (Cited on p. 28, 41)
[Bes87] A. L. Besse, Einstein manifolds, Reprint of the 1987 edition, Classics in Mathematics. Springer-Verlag, Berlin, 2008. (Cited on p. 8, 11, 16, 21)
[Bla56] A. Blanchard, Sur les variétés analytiques complexes, Ann. Sci. Ecole Norm. Sup. (3) 73 (1956), 157-202. (Cited on p. 19)
[Boc46] S. Bochner, Vector fields and Ricci curvature, Bull. Amer. Math. Soc. 52 (1946), 776-797. (Cited on p. 20)
[Bog78] F. A. Bogomolov, Holomorphic tensors and vector bundles on projective manifolds, Izv. Akad. Nauk SSSR Ser. Mat. 42 (1978), no. 6, 1227-1287, 1439. English translation in Math. USSR-Izv. 13 (1979), no. 3, 499-555. (Cited on p. 17)
[BBI01] D. Burago, Y. Burago, S. Ivanov, A course in metric geometry, Graduate Studies in Mathematics, 33, American Mathematical Society, Providence, RI, 2001. (Cited on p. 37, 38)
[CC95] L. A. Caffarelli, X. Cabré, Fully nonlinear elliptic equations, American Mathematical Society Colloquium Publications, 43, American Mathematical Society, Providence, RI, 1995. (Cited on p. 11)
[Cal54] E. Calabi, The space of Kähler metrics, Proc. Internat. Congress Math. Amsterdam 2 (1954), pp. 206-207. (Cited on p. 2)
[Cal57] E. Calabi, On Kähler manifolds with vanishing canonical class, in Algebraic geometry and topology. A symposium in honor of S. Lefschetz, pp. 78-89, Princeton University Press, Princeton, N. J., 1957. (Cited on p. 2, 11)
[CdS01] A. Cannas da Silva, Lectures on symplectic geometry, Lecture Notes in Mathematics, 1764, Springer-Verlag, Berlin, 2001. (Cited on p. 29)
[CL73] J. B. Carrell, D. I. Lieberman, Holomorphic Vector fields and Kaehler Manifolds, Invent. Math. 21 (1973), 303-309. (Cited on p. 19)
[Cat99] D. Catlin, The Bergman kernel and a theorem of Tian, in Analysis and geometry in several complex variables (Katata, 1997), 1-23, Trends Math., Birkhäuser Boston, Boston, MA, 1999. (Cited on p. 33)
[Che01] J. Cheeger, Degeneration of Riemannian metrics under Ricci curvature bounds, Lezioni Fermiane, Scuola Normale Superiore, Pisa, 2001. (Cited on p. 38)
[Che08] I. A. Chel'tsov, Log canonical thresholds of del Pezzo surfaces, Geom. Funct. Anal. 18 (2008), no. 4, 1118-1144. (Cited on p. 26)
[CS08] I. A. Chel'tsov, K. A. Shramov, Log-canonical thresholds for nonsingular Fano threefolds. With an appendix by J.-P. Demailly, Uspekhi Mat. Nauk 63 (2008), no. 5(383), 73-180; translation in Russian Math. Surveys 63 (2008), no. 5, 859-958. (Cited on p. 26)
[Che00] X.x. Chen, The space of Kähler metrics, J. Differential Geom. 56 (2000), no. 2, 189-234. (Cited on p. 23)
[CDS14] X.x. Chen, S. Donaldson, S. Sun, Kähler-Einstein metrics and stability, Int. Math. Res. Not. IMRN 2014 (2014), no. 8, 2119-2125. (Cited on p. 3)
[CDS15] X.x. Chen, S. Donaldson, S. Sun, Kähler-Einstein metrics on Fano manifolds. I: Approximation of metrics with cone singularities, II: Limits with cone angle less than $2 \pi$, III: Limits as cone angle approaches $2 \pi$ and completion of the main proof, J. Amer. Math. Soc. 28 (2015), no. 1, 183-197, 199-234, 235-278. (Cited on p. 3, 26, 35, 36, 38)
[CSW15] X.x. Chen, S. Sun, B. Wang, Kähler-Ricci flow, Kähler-Einstein metric, and K-stability, arXiv:1508.04397. (Cited on p. 41)
[CTW17] J. Chu, V. Tosatti, B. Weinkove, On the $C^{1,1}$ Regularity of Geodesics in the Space of Kähler Metrics, Ann. PDE 3 (2017), no. 2, 3-15. (Cited on p. 23)
[DL12] T. Darvas, L. Lempert, Weak geodesics in the space of Kähler metrics, Math. Res. Lett. 19 (2012), no. 5, 1127-1135. (Cited on p. 23)
[DS16] V. Datar, G. Székelyhidi, Kähler-Einstein metrics along the smooth continuity method, Geom. Funct. Anal. 26 (2016), no. 4, 975-1010. (Cited on p. 41)
[Deb01] O. Debarre, Higher-dimensional algebraic geometry, Universitext, Springer-Verlag, New York, 2001. (Cited on p. 17)
[DGMS75] P. Deligne, Ph. Griffiths, J. Morgan, D. Sullivan, Real homotopy theory of Kähler manifolds, Invent. Math. 29 (1975), no. 3, 245-274. (Cited on p. 6)
[Dem12] J.-P. Demailly, Complex Analytic and Differential Geometry, http://www-fourier.ujf-grenoble.fr/~demailly/manuscri 2012. (Cited on p. 3, 8, 9)
[Dem17] J.-P. Demailly, Variational approach for complex Monge-Ampère equations and geometric applications, Séminaire Bourbaki, Exposé 1112, Astérisque 390 (2017), 245-275. (Cited on p. 41)
[DK01] J.-P. Demailly, J. Kollár, Semi-continuity of complex singularity exponents and Kähler-Einstein metrics on Fano orbifolds, Ann. Sci. École Norm. Sup. (4) 34 (2001), no. 4, 525-556. (Cited on p. 36)
[Din88] W. Y. Ding, Remarks on the existence problem of positive Kähler-Einstein metrics, Math. Ann. 282 (1988), no. 3, 463-471. (Cited on p. 35)
[Dol53] P. Dolbeault, Sur la cohomologie des variétés analytiques complexes., C. R. Acad. Sci. Paris 236 (1953). 175-177. (Cited on p. 5)
[Don87] S. K. Donaldson, Infinite determinants, stable bundles and curvature, Duke Math. J. 54 (1987), no. 1, 231-247. (Cited on p. 2, 27)
[Don97] S. K. Donaldson, Remarks on gauge theory, complex geometry and 4-manifold topology, in Fields Medallists' lectures, 384-403, World Sci. Ser. 20th Century Math., 5, World Sci. Publ., River Edge, NJ, 1997. (Cited on p. 28)
[Don99] S. K. Donaldson, Symmetric spaces, Kähler geometry and Hamiltonian dynamics, in Northern California Symplectic Geometry Seminar, 13-33, Amer. Math. Soc. Transl. Ser. 2, 196, Adv. Math. Sci., 45, Amer. Math. Soc., Providence, RI, 1999. (Cited on p. 22, 23)
[Don01] S. K. Donaldson, Scalar curvature and projective embeddings. I, J. Differential Geom. 59 (2001), no. 3, 479-522. (Cited on p. 34)
[Don02a] S. K.Donaldson, Holomorphic discs and the complex Monge-Ampère equation, J. Symplectic Geom. 1 (2002), no. 2, 171-196. (Cited on p. 23)
[Don02b] S. K. Donaldson, Scalar curvature and stability of toric varieties, J. Differential Geom. 62 (2002), no. 2, 289-349. (Cited on p. 2, 3, 28)
[Don05] S. K. Donaldson, Lower bounds on the Calabi functional, J. Differential Geom. 70 (2005), no. 3, 453-472. (Cited on p. 2, 3, 34)
[Don12] S. K. Donaldson, Kähler metrics with cone singularities along a divisor, in Essays in mathematics and its applications, 49-79, Springer, Heidelberg, 2012. (Cited on p. 36)
[Don15] S. K. Donaldson, Algebraic families of constant scalar curvature Kähler metrics, in Surveys in differential geometry 2014. Regularity and evolution of nonlinear equations, 111-137, Surv. Differ. Geom., 19, Int. Press, Somerville, MA, 2015. (Cited on p. 10)
[DS14] S. K. Donaldson, S. Sun, Gromov-Hausdorff limits of Kähler manifolds and algebraic geometry, Acta Math. 213 (2014), no. 1, 63-106. (Cited on p. 40)
[DS17] S. K. Donaldson, S. Sun, Gromov-Hausdorff limits of Kähler manifolds and algebraic geometry, II, J. Differential Geom. 107 (2017), no. 2, 327-371. (Cited on p. 41)
[Eva82] L. C. Evans, Classical solutions of fully nonlinear, convex, second-order elliptic equations, Comm. Pure Appl. Math. 35 (1982), 333-363. (Cited on p. 12)
[EGZ09] Ph. Eyssidieux, V. Guedj, A. Zeriahi, Singular Kähler-Einstein metrics, J. Amer. Math. Soc. 22 (2009), no. 3, 607-639. (Cited on p. 41)
[Fig17] A. Figalli, The Monge-Ampère equation and its applications, Zurich Lectures in Advanced Mathematics. European Mathematical Society (EMS), Zürich, 2017. (Cited on p. 11)
[Fuj90] A. Fujiki, Moduli space of polarized algebraic manifolds and Kähler metrics [translation of Sûgaku 42 (1990), no. 3, 231-243], Sugaku Expositions 5 (1992), no. 2, 173-191. (Cited on p. 28)
[Fuj15] K. Fujita, Optimal bounds for the volumes of Kähler-Einstein Fano manifolds, arXiv:1508.04578. (Cited on p. 18, 35)
[Fuj16a] K. Fujita, A valuative criterion for uniform K-stability of $\mathbb{Q}$-Fano varieties, arXiv:1602.00901. (Cited on p. 35)
[Fuj16b] K. Fujita, K-stability of Fano manifolds with not small alpha invariants, arXiv:1606.08261. (Cited on p. 10, 26)
[Fut83] A. Futaki, An obstruction to the existence of Einstein Kähler metrics, Invent. Math. 73 (1983), no. 3, 437-443. (Cited on p. 2, 21)
[Gau15] P. Gauduchon, Calabi's extremal Kähler metrics: An elementary introduction, http://germanio.math.unifi.it/wp-content/uploads/2015/03/dercalabi.pdf. (Cited on p. 3, 4, 8, 11, 18, 20, 22)
[GT98] D. Gilbarg, N. S. Trudinger, Elliptic partial differential equations of second order, Reprint of the 1998 edition, Classics in Mathematics, Springer-Verlag, Berlin, 2001. (Cited on p. 11, 12, 16)
[GH78] Ph. Griffiths, J. Harris, Principles of algebraic geometry, Reprint of the 1978 original, Wiley Classics Library. John Wiley \& Sons, Inc., New York, 1994. (Cited on p. 3, 9, 13)
[LNM2038] Complex Monge-Ampère equations and geodesics in the space of Kähler metrics, Edited by Vincent Guedj, Lecture Notes in Mathematics, 2038, Springer, Heidelberg, 2012. (Cited on p. 11)
[GZ17] V. Guedj, A. Zeriahi, Degenerate complex Monge-Ampère equations, EMS Tracts in Mathematics, 26, European Mathematical Society (EMS), Zürich, 2017. (Cited on p. 11)
[Gue15] H. Guenancia, Kähler-Einstein metrics: from cones to cusps, arXiv:1504.01947. (Cited on p. 36)
[Huy05] D. Huybrechts, Complex geometry. An introduction, Universitext, Springer-Verlag, Berlin, 2005. (Cited on p. 3, 6)
[JMR16] T. Jeffres, R. Mazzeo, Y. A. Rubinstein, Kähler-Einstein metrics with edge singularities, Ann. of Math. (2) 183 (2016), no. 1, 95-176. (Cited on p. 37)
[Kob74] S. Kobayashi, On compact Kähler manifolds with positive definite Ricci tensor, Ann. of Math. (2) 74 (1961), 570-574. (Cited on p. 16)
[KN2] S. Kobayashi, K. Nomizu, Foundations of differential geometry. Vol. II, Reprint of the 1969 original, Wiley Classics Library, A Wiley-Interscience Publication. John Wiley \& Sons, Inc., New York, 1996. (Cited on p. 3, 17)
[Kod54] K. Kodaira, On Kähler varieties of restricted type (an intrinsic characterization of algebraic varieties), Ann. Math. (2) 60 (1954), 28-48. (Cited on p. 8, 9)
[Kod86] K. Kodaira, Complex manifolds and deformation of complex structures, Translated from the 1981 Japanese original by Kazuo Akao, Reprint of the 1986 English edition, Classics in Mathematics, Springer-Verlag, Berlin, 2005. (Cited on p. 3)
[Kol96] J. Kollár, Rational curves on algebraic varieties, Ergebnisse der Mathematik und ihrer Grenzgebiete, 3, Folge, A Series of Modern Surveys in Mathematics, 32, Springer-Verlag, Berlin, 1996. (Cited on p. 9)
[KMM92] J. Kollár, Y. Miyaoka, S. Mori, Rational Connectedness and Boundedness of Fano Manifolds, J. Diff. Geom. 36 (1992), 765-769. (Cited on p. 9)
[KM98] J. Kollár, S. Mori, Birational geometry of algebraic varieties, With the collaboration of C. H. Clemens and A. Corti, Translated from the 1998 Japanese original, Cambridge Tracts in Mathematics, 134, Cambridge University Press, Cambridge, 1998. (Cited on p. 17)
[Kry82] N. V. Krylov. Boundedly inhomogeneous elliptic and parabolic equations, Izv. Akad. Nauk SSSR Ser. Mat. 46 (1982), 487-523. (Cited on p. 12)
[LBS94] C. R. LeBrun, S. Simanca, Extremal Kähler metrics and complex deformation theory, Geom. Funct. Analysis 4 (1994), no. 3, 298-336. (Cited on p. 19)
[LV13] L. Lempert, L. Vivas, Geodesics in the space of Kähler metrics, Duke Math. J. 162 (2013), no. 7, 1369-1381. (Cited on p. 23)
[Li11] C. Li, Greatest lower bounds on Ricci curvature for toric Fano manifolds, Adv. Math. 226 (2011), no. 6, 4921-4932. (Cited on p. 23)
[Li15a] C. Li, Minimizing normalized volumes of valuations, arXiv:1511.08164. (Cited on p. 42)
[Li15b] C. Li, Remarks on logarithmic K-stability, Commun. Contemp. Math. 17 (2015), no. 2, 1450020, 17 pp.. (Cited on p. 23)
[LS14] C. Li, S. Sun, Conical Kähler-Einstein metrics revisited, Comm. Math. Phys. 331 (2014), no. 3, 927-973. (Cited on p. 36, 41)
[LX14] C. Li, C. Xu, Special test configuration and K-stability of Fano varieties, Ann. of Math. (2) 180 (2014), no. 1, 197-232. (Cited on p. 28)
[LY87] J. Li, S.-T. Yau, Hermitian-Yang-Mills connection on non-Kähler manifolds, in Mathematical aspects of string theory (San Diego, Calif., 1986), 560-573, Adv. Ser. Math. Phys., 1, World Sci. Publishing, Singapore, 1987. (Cited on p. 2, 27)
[Lic58] A. Lichnerowicz, Géométrie des groupes de transformation, Travaux et Recherches Mathématiques 3, Dunod (1958). (Cited on p. 20)
[Liu16] Y. Liu, The volume of singular Kḧler-Einstein Fano varieties, arXiv:1605.01034. (Cited on p. 42)
[LX17] Y. Liu, C. Xu, K-stability of cubic threefolds, arXiv:1706.01933. (Cited on p. 10, 42)
[Lu00] Z. Lu, On the lower order terms of the asymptotic expansion of Tian-Yau-Zelditch, Amer. J. Math. 122 (2000), no. 2, 235-273. (Cited on p. 33)
[LT95] M. Lübke, A. Teleman, The Kobayashi-Hitchin correspondence, World Scientific Publishing Co., Inc., River Edge, NJ, 1995. (Cited on p. 2, 27)
[Mab85] T. Mabuchi, A Functional Integrating Futaki's Invariant, Proc. Japan Acad. Ser. A 61 (1985), no. 4, 119-120. (Cited on p. 22)
[Mab87] T. Mabuchi, Some symplectic geometry on compact Kähler manifolds. I, Osaka J. Math. 24 (1987), no. 2, 227-252. (Cited on p. 22)
[Mab08] T. Mabuchi, K-stability of constant scalar curvature polarization, arXiv:0812.4093. (Cited on p. 3)
[MM93] T. Mabuchi, S. Mukai, Stability and Einstein-Kähler metric of a quartic del Pezzo surface, in Einstein metrics and Yang-Mills connections (Sanda, 1990), 133-160, Lecture Notes in Pure and Appl. Math., 145, Dekker, New York, 1993. (Cited on p. 42)
[MS06] D. Martelli, J. Sparks, Toric geometry, Sasaki-Einstein manifolds and a new infinite class of AdS/CFT duals, Comm. Math. Phys. 262 (2006), no. 1, 51-89. (Cited on p. 21)
[Mat57] Y. Matsushima, Sur la structure du groupe d'homéomorphismes analytiques d'une certaine variété kählérienne, Nagoya Math. J. 11 (1957), 145-150. (Cited on p. 2, 19, 20)
[Miy77] Y. Miyaoka, On the Chern numbers of surfaces of general type, Invent. Math. 42 (1977), 225-237. (Cited on p. 17)
[Mor79] S. Mori, Projective manifolds with ample tangent bundles, Ann. of Math. 110 (1979), 593-606. (Cited on p. 17)
[Mor07] A. Moroianu, Lectures on Kähler geometry, London Mathematical Society Student Texts, 69, Cambridge University Press, Cambridge, 2007. (Cited on p. 3)
[MK71] J. Morrow, K. Kodaira, Complex manifolds, Reprint of the 1971 edition with errata, AMS Chelsea Publishing, Providence, RI, 2006. (Cited on p. 3)
[Mos65] J. Moser, On the volume elements on a manifold, Trans. Amer. Math. Soc. 120 (1965), 286-294. (Cited on p. 29)
[Mum77] D. Mumford, Stability of projective varieties, Enseignement Math. (2) 23 (1977), no. 1-2, 39-110. (Cited on p. 29, 30)
[Mum79] D. Mumford, An algebraic surface with $K$ ample, $\left(K^{2}\right)=9, p_{g}=q=0$, Amer. J. Math. 101 (1979), no. 1, 233-244. (Cited on p. 18)
[MFK94] D. Mumford, J. Fogarty, F. Kirwan, Geometric invariant theory, Third edition, Ergebnisse der Mathematik und ihrer Grenzgebiete (2), 34, Springer-Verlag, Berlin, 1994. (Cited on p. 29, 30)
[MS39] S. B. Myers, N. E. Steenrod, The group of isometries of a Riemannian manifold, Ann. of Math. (2) 40 (1939), no. 2, 400-416. (Cited on p. 20)
[NN57] A. Newlander, L. Nirenberg, Complex analytic coordinates in almost complex manifolds, Ann. of Math. (2) 65 (1957), 391-404. (Cited on p. 4)
[New78] P. E. Newstead, Introduction to moduli problems and orbit spaces, Tata Institute of Fundamental Research Lectures on Mathematics and Physics, 51, Tata Institute of Fundamental Research, Bombay; by the Narosa Publishing House, New Delhi, 1978. (Cited on p. 29)
[OSS16] Y. Odaka, C. Spotti, S. Sun, Compact moduli spaces of del Pezzo surfaces and Kähler-Einstein metrics, J. Differential Geom. 102 (2016), no. 1, 127-172. (Cited on p. 42)
[Pag79] D. Page, A Compact Rotating Gravitational Instanton, Phys. Lett. B 79B (1979), 235-238. (Cited on p. 21)
[PT09] S. T. Paul, G. Tian, CM stability and the generalized Futaki invariant II, Astérisque 328 (2009) (2010), 339-354. (Cited on p. 32)
[PSS07] D. H. Phong, N. Sesum, J. Sturm, Multiplier ideal sheaves and the Kähler-Ricci flow, Comm. Anal. Geom. 15 (2007), no. 3, 613-632. (Cited on p. 15)
[RT07] J. Ross, R. Thomas, A study of the Hilbert-Mumford criterion for the stability of projective varieties, J. Algebraic Geom. 16 (2007), no. 2, 201-255. (Cited on p. 32)
[Rua98] W.-D. Ruan, Canonical coordinates and Bergmann metrics, Comm. Anal. Geom. 6 (1998), no. 3, 589-631. (Cited on p. 33)
[Sem92] S. Semmes, Complex Monge-Ampère and symplectic manifolds, Amer. J. Math. 114 (1992), no. 3, 495-550. (Cited on p. 22)
[Spo17] C. Spotti, Kähler-Einstein Metrics on $\mathbb{Q}$-Smoothable Fano Varieties, Their Moduli and Some Applications, in Complex and Symplectic Geometry, 211-229, Springer INdAM Series 21, Springer, 2017. (Cited on p. 31)
[SS17] C. Spotti, S. Sun, Explicit Gromov-Hausdorff compactifications of moduli spaces of Kähler-Einstein Fano manifolds, arXiv:1705.00377. (Cited on p. 10, 42)
[Sto09] J. Stoppa, K-stability of constant scalar curvature Kähler manifolds, Adv. Math. 221 (2009), no. 4, 1397-1408. (Cited on p. 3, 34)
[Szé11] G. Székelyhidi, Greatest lower bounds on the Ricci curvature of Fano manifolds, Compos. Math. 147 (2011), no. 1, 319-331. (Cited on p. 23)
[Szé14] G. Székelyhidi, An introduction to extremal Kähler metrics, Graduate Studies in Mathematics, 152, American Mathematical Society, Providence, RI, 2014. (Cited on p. 3, 6, 8, 12, 20, 22, 28, 33)
[Tho06] R. P. Thomas, Notes on GIT and symplectic reduction for bundles and varieties, Surveys in differential geometry. Vol. X, 221-273, Surv. Differ. Geom., 10, Int. Press, Somerville, MA, 2006. (Cited on p. 29)
[Thu82] W. P. Thurston, Three-dimensional manifolds, Kleinian groups and hyperbolic geometry, Bull. Amer. Math. Soc. (N.S.) 6 (1982), no. 3, 357-381. (Cited on p. 36)
[Tian87] G. Tian, On Kähler-Einstein metrics on certain Kähler manifolds with $C_{1}(M)>0$, Invent. Math. 89 (1987), no. 2, 225-246. (Cited on p. 2, 24, 25, 26)
[Tia90a] G. Tian, On Calabi's conjecture for complex surfaces with positive first Chern class, Invent. Math. 101 (1990), no. 1, 101-172. (Cited on p. 2, 10, 42)
[Tia90b] G. Tian, On a set of polarized Kähler metrics on algebraic manifolds, J. Differential Geom. 32 (1990), no. 1, 99-130. (Cited on p. 33)
[Tia92] G. Tian, On stability of the tangent bundles of Fano varieties, Internat. J. Math. 3 (1992), no. 3, 401-413. (Cited on p. 23)
[Tia94] G. Tian, The K-energy on hypersurfaces and stability, Comm. Anal. Geom. 2 (1994), no. 2, 239-265. (Cited on p. 3)
[Tia97] G. Tian, Kähler-Einstein metrics with positive scalar curvature, Invent. Math. 130 (1997), no. 1, 1-37. (Cited on p. 2, 3, 25, 28)
[Tia00] G. Tian, Canonical metrics in Kähler geometry, Notes taken by Meike Akveld, Lectures in Mathematics ETH Zürich, Birkhäuser Verlag, Basel, 2000. (Cited on p. 3, 6, 10, 11, 12, 15, 24, 25, 28)
[TY90] G. Tian, S.-T. Yau, Complete Kähler manifolds with zero Ricci curvature. I, J. Amer. Math. Soc. 3 (1990), no. 3, 579-609. (Cited on p. 36)
[TY91] G. Tian, S.-T. Yau, Complete Kähler manifolds with zero Ricci curvature. II, Invent. Math. 106 (1991), no. 1, 27-60. (Cited on p. 36)
[Tos17] V. Tosatti, Uniqueness of $\mathbb{C P}^{n}$, Expo. Math. 35 (2017), no. 1, 1-12. (Cited on p. 17)
[UY86] K. Uhlenbeck, S.-T. Yau, On the existence of Hermitian-Yang-Mills connections in stable vector bundles, Frontiers of the mathematical sciences: 1985 (New York, 1985), Comm. Pure Appl. Math. 39 (1986), no. S, suppl., S257--S293. (Cited on p. 2, 27)
[VdV66] A. Van de Ven, On the Chern numbers of certain complex and almost complex manifolds, Proc. Nat. Acad. Sci. U.S.A. 55 (1966), 1624-1627. (Cited on p. 17)
[Voi07] C. Voisin, Hodge theory and complex algebraic geometry. I, Translated from the French by Leila Schneps, Reprint of the 2002 English edition, Cambridge Studies in Advanced Mathematics, 76, Cambridge University Press, Cambridge, 2007. (Cited on p. 3, 5, 6, 9, 16)
[WZ04] X.-J. Wang, X. Zhu, Kähler-Ricci solitons on toric manifolds with positive first Chern class, Adv. Math. 188 (2004), no. 1, 87-103. (Cited on p. 2)
[Wel08] R. O. Wells, Differential analysis on complex manifolds, Third edition, With a new appendix by Oscar Garcia-Prada, Graduate Texts in Mathematics, 65, Springer, New York, 2008. (Cited on p. 3)
[Yau77] S.-T. Yau, Calabi's conjecture and some new results in algebraic geometry, Proc. Nat. Acad. Sci. U.S.A. 74 (1977), no. 5, 1798-1799. (Cited on p. 2, 8, 10, 16, 17)
[Yau78] S.-T. Yau, On the Ricci curvature of a compact Kähler manifold and the complex Monge-Ampère equation. I, Comm. Pure Appl. Math. 31 (1978), no. 3, 339-411. (Cited on p. 2, 8, 10, 17)
[Zel98] S. Zelditch, Szegő kernels and a theorem of Tian, Internat. Math. Res. Notices 1998 (1998), no. 6, 317-331. (Cited on p. 33)
(D. Angella) Dipartimento di Matematica e Informatica "Ulisse Dini", Università di Firenze, viale Morgagni 67/a, 50134 Firenze, Italy
E-mail address: daniele.angella@gmail.com
E-mail address: daniele.angella@unifi.it
(C. Spotti) QGM, Centre for Quantum Geometry of Moduli Spaces, Aarhus University, Ny Munkegade 118, 8000 Aarhus C, Denmark
E-mail address: cristiano.spotti@gmail.com
E-mail address: c.spotti@qgm.au.dk