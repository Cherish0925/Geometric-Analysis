---
retention_scope: session
part: 3
total_parts: 3
---

[Part 3/3 of: Seiberg–Witten and Gromov invariants for self-dual]

As explained in [27, §5.i.1], the map $\psi_{\mathcal{C}, r}$ in (4.4) satisfies
$$\left|\psi_{\mathcal{C}, r}-\times_{k^{\prime}} \psi_{\Lambda}^{\left(k^{\prime}\right)}\right| \leq \zeta r^{-1 / 2}$$
for some $r$-independent constant $\zeta$, where the norm on $\bigoplus_{k^{\prime}} \Lambda_{\left(k^{\prime}\right)}$ is the product of the $L^{2}$-norms on each of the factors. Here, we view $\psi_{\mathcal{C}, r}$ as a function restricted to $\times_{k^{\prime}} \mathcal{K}_{\Lambda}^{\left(k^{\prime}\right)}$ (which is diffeomorphic to $\mathcal{Y}_{\bar{z}, \bar{\eta}}$ ). Thus, it follows that
$$\prod_{k^{\prime}} r^{\prime}\left(C_{k^{\prime}}, d_{k^{\prime}}\right) \equiv\left|\psi_{\mathcal{C}, r}^{-1}(0) \cap \mathcal{Y}_{\bar{z}, \bar{\eta}}\right| \quad \bmod 2$$
for $r$ sufficiently large.
Step 2. Given the result of Step 1, it remains to show that $r^{\prime}\left(C_{k^{\prime}}, d_{k^{\prime}}\right)=r\left(C_{k^{\prime}}, d_{k^{\prime}}\right)$ in order to establish (4.7) and hence complete the general proof of Theorem 4.2.

Proposition 4.14. For generic $J$ as needed to make 1.6 well-defined, the weights $r^{\prime}(C, d)$ and $r(C, d)$ are equal for any $J$-holomorphic special curve $C$ with multiplicity $d$. In particular, their value is 1 when $C$ is a special plane.

Proof. If $C$ is a special torus then this is precisely the result of [29], Proposition 2.12, Proposition 2.15]. Similarly to the proof of [29, Proposition 2.12], if $C$ a special plane then $r^{\prime}(C, d)$ is unaffected by replacing $\mu_{C}$ in the definition of $\mathcal{Z}_{0}$ with $t \mu_{C}$ for any $t \in[0,1]$, noting that the resulting space $\mathcal{Z}_{0}^{t}$ of sections is still compact by Proposition 4.3. In particular, $r^{\prime}(C, d)$ is equal to the count of points of $\mathcal{Z}_{0}^{0}$. Similarly to the end of the proof of [29, Proposition 2.15], $\mathcal{Z}_{0}^{0}$ consists of a single regular point (namely, the constant map to the unique "symmetric" vortex) because the complex linear operator $\bar{\partial}+\nu_{C} \aleph$ has trivial kernel and cokernel. Thus, $r^{\prime}(C, d)=1$. \(\square\) \(\square\)

\section*{5 Relation of Seiberg-Witten counts}

The goal of this section is to finally prove Theorem 1.7 (and thus Theorem 1.2). It follows from Theorem 3.6 and Theorem 4.2 using $I=d(\mathfrak{s})$ that, for $r$ sufficiently large, the Gromov cycle $\Phi_{G r}$ (given by Definition 1.6) is chain-isomorphic over $\mathbb{Z} / 2 \mathbb{Z}$ to the Seiberg-Witten cocycle
$$\Phi_{S W}:=\sum_{\Theta} \mathfrak{M}_{\mathfrak{c}_{\Theta}} \mathfrak{c}_{\Theta} \in \widehat{C M}^{g(\mathfrak{s})}\left(-\partial X_{0}, \mathfrak{s}_{\xi_{0}}+1\right)$$
where the sum is over admissible orbit sets $\Theta$ in the grading $g(\mathfrak{s})$ with $[\Theta]=-\partial \tau_{\omega}(\mathfrak{s})$ and
$$\mathfrak{M}_{\mathfrak{c}_{\Theta}}:=\sum_{\mathfrak{d} \in \mathfrak{M}_{d(\mathfrak{s})}\left(\mathfrak{c}_{\Theta}, \varnothing ; \mathfrak{s}_{\mathfrak{s}}, \bar{z}, \bar{\eta}\right)} q(\mathfrak{d}) \in \mathbb{Z} / 2 \mathbb{Z}$$
The integer $G r_{X, \omega}(\mathfrak{s})\left(\left[\eta_{1}\right] \wedge \cdots \wedge\left[\eta_{p}\right]\right)$ is thus equal (modulo 2) to the coefficient of the class
$$\left[\Phi_{S W}\right] \in \bigotimes_{k=1}^{N} \widehat{H M}^{\left[\xi_{*}\right]}\left(S^{1} \times S^{2}, \mathfrak{s}_{\xi_{0}}+1\right) \cong \mathbb{Z}$$
as a multiple of the generator $\mathbb{1} \in \bigotimes_{k=1}^{N} \widehat{H M}^{\left[\xi_{*}\right]}\left(S^{1} \times S^{2}, \mathfrak{s}_{\xi_{0}}+1\right)$, where again we have anticipated $g(\mathfrak{s})=N\left[\xi_{*}\right]$. In fact, this coefficient is the corresponding Seiberg-Witten invariant:

Theorem 5.1. Fix $(X, \omega)$ and assume $\mathfrak{s} \in \operatorname{Spin}^{c}(X)$ is such that $E \cdot \tau_{\omega}(\mathfrak{s}) \geq-1$ for all $E \in \mathcal{E}_{\omega}$. Fix an integer $p$ such that $0 \leq p \leq d(\mathfrak{s})$ and $d(\mathfrak{s})-p$ is even, and fix an ordered set of homology classes $[\bar{\eta}]:=\left\{\left[\eta_{i}\right], \ldots,\left[\eta_{p}\right]\right\} \subset H_{1}(X ; \mathbb{Z}) /$ Torsion . Then
$$G r_{X, \omega}(\mathfrak{s})\left(\left[\eta_{1}\right] \wedge \cdots \wedge\left[\eta_{p}\right]\right) \equiv S W_{X}(\mathfrak{s})\left(\left[\eta_{1}\right] \wedge \cdots \wedge\left[\eta_{p}\right]\right) \quad \bmod 2$$
and $g(\mathfrak{s})=N\left[\xi_{*}\right]$ as an absolute grading of the $N$-fold tensor product of $\widehat{H M}^{*}\left(S^{1} \times S^{2}\right)$.
Before we prove this theorem we make the following remarks. The work of Kronheimer-Mrowka (specifically, [16, Proposition 27.4.1]) recovers the Seiberg-Witten invariants of $X$ using their monopole Floer (co)homologies, explicitly by removing two copies of the 4-ball $B^{4}$ from $X$ and counting certain ${ }^{27}$ SW instantons on the resulting cobordism $S^{3} \rightarrow S^{3}$. Although not provided in [16], the same result could have been obtained by removing two copies of $S^{1} \times B^{3}$, because both spaces ( $B^{4}$ and $S^{1} \times B^{3}$ ) have positive scalar curvature and a unique spin-c structure extending the fixed torsion spin-c structure on their boundary (see [16, Proposition 22.7.1]). ${ }^{28}$ There would necessarily be more work to do when using $S^{1} \times B^{3}$ because there exists a circle's worth of reducible monopoles on $S^{1} \times S^{2}$ (to the unperturbed Seiberg-Witten equations), compared with a single reducible monopole on $S^{3}$. ${ }^{29}$

In the proof of Theorem 5.1 we will remove $N$ copies of $S^{1} \times B^{3}$ from $X$, namely, the tubular neighborhoods of the zero-circles. This is a "neck stretching" argument along the contact hypersurfaces ( $S^{1} \times S^{2}, \lambda_{\mathfrak{s}}$ ) in $X$, and we analyze the Seiberg-Witten equations under this deformation.

\footnotetext{
${ }^{27}$ They build a "mixed" map $\overrightarrow{H M}^{\prime}: \widehat{H M}_{*}\left(S^{3}\right) \rightarrow \widehat{H M}^{*}\left(S^{3}\right)$ and pair the image of a generator $\mathbb{1} \in \widehat{H M}_{*}\left(S^{3}\right)$ with a generator $\check{1} \in \widehat{H M}^{*}\left(S^{3}\right)$. A homology orientation of the cobordism is identified with a homology orientation of $X$.
${ }^{28}$ It is important here to note that every self-diffeomorphism of $S^{1} \times S^{2}$ (and $S^{3}$ ) extends to $S^{1} \times B^{3}$ (and $B^{4}$ ).
${ }^{29}$ We must also choose a homology orientation of $S^{1} \times S^{2}$, i.e. an orientation of the vector space $H^{1}\left(S^{1} \times S^{2} ; \mathbb{R}\right) \cong \mathbb{R}$, in order to identify a homology orientation of $X$ with that on the cobordism.
}

It is important to note that on $X_{0}$ we can use Taubes' large perturbations to the Seiberg-Witten equations, for which there are no reducible solutions, but on each $S^{1} \times B^{3}$ we cannot do this because there is no symplectic form (or said another way, the near-symplectic form $\omega$ degenerates somewhere inside $S^{1} \times B^{3}$ ). We thus interpolate, on the "neck region" of $X$, between Taubes' large perturbations on $X_{0}$ and very small perturbations on each $S^{1} \times B^{3}$, where the small perturbations are chosen in such a way that we can understand the SW instantons on each $S^{1} \times B^{3}$ completely.

A final remark is that in this setup, we do not run into the usual difficulties that Kronheimer-Mrowka have when defining monopole Floer cobordism maps for cobordisms with disconnected and empty ends. These difficulties are ultimately due to the (stratified) space of reducible monopoles on the (positive and negative) boundary components of the cobordism, and are avoided in our setup thanks to Taubes' large perturbations.

Proof of Theorem 5.1. We closely follow the arguments in [16, §26, §27.4, §36.1] that recover the Seiberg-Witten invariant and establish the composition law for monopole Floer (co)homology. These arguments involve judicious choices of Riemannian metrics and abstract perturbations on $X$ to "stretch the neck" and compare the resulting moduli spaces of SW instantons.

Let $\mathbb{T}$ denote the circle $H^{1}\left(S^{1} \times S^{2} ; i \mathbb{R}\right) / H^{1}\left(S^{1} \times S^{2} ; 2 \pi i \mathbb{Z}\right) \cong S^{1}$ which parametrizes reducible monopoles to the unperturbed Seiberg-Witten equations over $S^{1} \times S^{2}$. In fact, all monopoles are reducible because $S^{1} \times S^{2}$ has a metric of positive scalar curvature (see [16, Proposition 22.7.1]). After fixing a reference connection $\mathbf{A}_{0}$ on $\operatorname{det} \mathbb{S}$ so that any other Hermitian connection can be written as $\mathbf{A}=\mathbf{A}_{0}+2 a$ for some $a \in \Omega^{1}(Y ; i \mathbb{R})$, there is a retraction map
$$p: \mathcal{B}\left(S^{1} \times S^{2}, \mathfrak{s}_{\xi_{0}}+1\right) \rightarrow \mathbb{T}$$
sending $\left[\mathbf{A}_{0}+2 a, \Psi\right]$ to the equivalence class of the harmonic part $a_{\text {harm }}$ of $a$ (see [16, §11.1]).
Let $f$ be the "height" Morse function on $\mathbb{T}$ with two critical points, and let $f_{1}=f \circ p$ be the corresponding function on $\mathcal{B}\left(S^{1} \times S^{2}, \mathfrak{s} \xi_{0}+1\right)$. The gradient of $f_{1}$ is an abstract perturbation $\mathfrak{q}_{f}:=\operatorname{grad} f_{1}$ (assumed small by re-scaling $f$ ), and the reducible critical points of $\operatorname{grad} \mathcal{L}_{\text {CSD }}+\mathfrak{q}_{f}$ are the maximum and minimum critical points $\{\alpha, \beta\}$ of $f$ on $\mathbb{T}$. The perturbed Dirac operators associated with $\alpha$ and $\beta$ in the blow-up $\mathcal{B}^{\sigma}\left(S^{1} \times S^{2}, \mathfrak{s}_{\xi_{0}}+1\right)$ do not have kernel, but to guarantee that their spectrums are simple we add a further small perturbation to $\mathfrak{q}_{f}$ (still denoted $\mathfrak{q}_{f}$ ) which vanishes on $\mathcal{B}^{\text {red }}\left(S^{1} \times S^{2}, \mathfrak{s}_{\xi_{0}}+1\right)$. Label the corresponding critical points in $\mathcal{B}^{\sigma}\left(S^{1} \times S^{2}, \mathfrak{s}_{\xi_{0}}+1\right)$ as $\mathfrak{a}_{i}$ and $\mathfrak{b}_{i}$ in increasing order of the index, where $\mathfrak{a}_{0}$ and $\mathfrak{b}_{0}$ correspond to the first positive eigenvalues of the perturbed Dirac operator at $\alpha$ and $\beta$ (the critical points are boundary-stable for $i \geq 0$ and boundary-unstable for $i<0$ ).

Consider a component $\mathcal{N}_{k} \approx S^{1} \times B^{3}$ of $\mathcal{N}=\bigsqcup_{k=1}^{N} \mathcal{N}_{k}$, equipped with a metric having positive scalar curvature and containing a collar region of its boundary in which the metric is cylindrical. Choose a small perturbation $\mathfrak{p}_{\mathcal{N}}$ on $\overline{\mathcal{N}_{k}}$ equal to $\mathfrak{q}_{f}$ on the end, so that the corresponding moduli spaces $M\left(\varnothing, \mathcal{N}_{k}, \mathfrak{a}_{i} ; \mathfrak{s}\right)$ and $M\left(\varnothing, \mathcal{N}_{k}, \mathfrak{b}_{i} ; \mathfrak{s}\right)$ are regular (this is possible by [16, Proposition 24.4.7]). Here, $\mathfrak{s}$ on $\mathcal{N}_{k}$ is the unique spin-c structure which extends $\mathfrak{s}_{\xi_{0}}+1$ on its boundary $S^{1} \times S^{2}$.

Let $X(T)$ be the closed manifold (diffeomorphic to $X$ ) obtained by attaching, for each end of $X_{0}$, two copies of the cylinder $[0, T] \times S^{1} \times S^{2}$ and one copy of another cylinder $[0,1] \times S^{1} \times S^{2}$ and the $k$ th component $\mathcal{N}_{k}$ of $\mathcal{N}$ (see Figure 3):
$$X(T):=\mathcal{N} \cup \bigcup_{k=1}^{N}\left(\left([0, T] \times S^{1} \times S^{2}\right) \cup\left([0,1] \times S^{1} \times S^{2}\right) \cup\left([0, T] \times S^{1} \times S^{2}\right)\right) \cup X_{0}$$

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/d787d2b4-e9c9-4ab7-9c05-44a3a9f294e2-38.jpg?height=206&width=686&top_left_y=247&top_left_x=724}
\captionsetup{labelformat=empty}
\caption{Figure 3: "Stretching the necks" of $X$, depicted in gray}
\end{figure}

The perturbed Seiberg-Witten equations on $X(T)$ carry the following perturbations:
\begin{itemize}
\item[-] Taubes' perturbation $\mathfrak{p}_{\omega}$ on $X_{0}$ which extends over the adjacent copies of $[0, T] \times S^{1} \times S^{2}$ using Taubes' perturbation $\mathfrak{q}_{\lambda}$ on $\partial X_{0}$,
\item[-] the perturbation $\mathfrak{p}_{\mathcal{N}}$ on each $\mathcal{N}_{k}$ which extends over the adjacent copies of $[0, T] \times S^{1} \times S^{2}$ using the perturbation $\mathfrak{q}_{f}$ on $\partial \mathcal{N}_{k}$,
\item[-] an "interpolating" perturbation $\mathfrak{p}_{\text {cyl }}$ on each copy of $[0,1] \times S^{1} \times S^{2}$ which agrees with $\mathfrak{q}_{\lambda}$ near $\{0\} \times S^{1} \times S^{2}$ and with $\mathfrak{q}_{f}$ near $\{1\} \times S^{1} \times S^{2}$.
\end{itemize}
To simplify notation we write $\mathcal{I}_{k}$ for the $k$ th copy of $[0,1] \times S^{1} \times S^{2}$ and $\mathcal{I}:=\bigsqcup_{k=1}^{N} \mathcal{I}_{k}$. Consider the moduli space $\mathfrak{M}(X(T), \mathfrak{s})$ for the manifold equipped with this perturbation. As $T \in[0, \infty)$ varies, these form a parametrized moduli space
$$\mathcal{M}(X, \mathfrak{s}):=\bigcup_{T \in[0, \infty)}\{T\} \times \mathfrak{M}(X(T), \mathfrak{s})$$
This has a compactification
$$\mathcal{M}^{+}(X, \mathfrak{s}):=\bigcup_{T \in[0, \infty]}\{T\} \times \mathfrak{M}(X(T), \mathfrak{s})$$
formed by attaching a fiber at $T=\infty$, where $\mathfrak{M}(X(\infty), \mathfrak{s})$ is defined to be the set of quintuples $\left(\mathfrak{d}_{0}, \breve{\mathfrak{d}}_{1}, \mathfrak{d}_{2}, \breve{\mathfrak{d}}_{3}, \mathfrak{d}_{4}\right)$ such that
$$\begin{aligned}
& \mathfrak{d}_{0} \in M\left(\varnothing, \mathcal{N}, \mathfrak{c}_{i_{1}} ; \mathfrak{s}\right) \\
& \breve{\mathfrak{d}}_{1} \in \breve{M}^{+}\left(\mathfrak{c}_{i_{1}}, \mathfrak{c}_{i_{2}}\right) \\
& \mathfrak{d}_{2} \in M\left(\mathfrak{c}_{i_{2}}, \mathcal{I}, \mathfrak{c}_{i_{3}} ; \mathfrak{s}_{\xi_{0}}+1\right) \\
& \breve{\mathfrak{d}}_{3} \in \breve{M}^{+}\left(\mathfrak{c}_{i_{3}}, \mathfrak{c}_{i_{4}}\right) \\
& \mathfrak{d}_{4} \in \mathfrak{M}\left(\mathfrak{c}_{i_{4}}, X_{0}, \varnothing ; \mathfrak{s}_{\mathfrak{s}}\right)
\end{aligned}$$
The space $\mathcal{M}^{+}(X, \mathfrak{s})$ is stratified by manifolds, its codimesion-1 strata consisting of the fiber $\mathfrak{M}(X, \mathfrak{s})$ over $T=0$ and those strata over $T=\infty$ with $\mathfrak{c}_{i_{1}}=\mathfrak{c}_{i_{2}}$ and $\mathfrak{c}_{i_{3}}=\mathfrak{c}_{i_{4}}$ (so that $\breve{\mathfrak{d}}_{1}$ and $\mathfrak{d}_{3}$ belong to point moduli spaces). The latter strata are of the form
$$M\left(\varnothing, \mathcal{N}, \mathfrak{c}_{1} ; \mathfrak{s}\right) \times M\left(\mathfrak{c}_{1}, \mathcal{I}, \mathfrak{c}_{2} ; \mathfrak{s}_{\xi_{0}}+1\right) \times \mathfrak{M}\left(\mathfrak{c}_{2}, X_{0}, \varnothing ; \mathfrak{s}_{\mathfrak{s}}\right)$$
where each of $\mathfrak{c}_{1}=\left\{\mathfrak{c}_{1}^{k}\right\}_{1 \leq k \leq N}$ and $\mathfrak{c}_{2}=\left\{\mathfrak{c}_{2}^{k}\right\}_{1 \leq k \leq N}$ is a critical point over $S^{1} \times S^{2}$ associated with the perturbations $\mathfrak{q}_{f}$ and $\mathfrak{q}_{\lambda}$, respectively.

We now incorporate the point and loop constraints that are used to define the closed Seiberg-Witten invariant. Since the constraints $\bar{z} \cup \bar{\eta}$ sit inside $X_{0} \subset X$ and $X$ may be written as the composition of cobordisms ${ }^{30} X_{0} \circ \mathcal{I} \circ \mathcal{N}$, we may decompose the element
$$u:=U^{\frac{1}{2}(d(\mathfrak{s})-p)}\left[\eta_{1}\right] \wedge \cdots \wedge\left[\eta_{p}\right] \in \mathbb{A}(X)$$
as the product
$$u=R_{\mathcal{N}}^{*}(1) \smile R_{\mathcal{I}}^{*}(1) \smile R_{X_{0}}^{*}\left(u_{0}\right)$$
where each $R_{\square}: \mathcal{B}^{\sigma}(X) \rightarrow \mathcal{B}^{\sigma}(\square)$ is the partially-defined restriction map and the class $u_{0} \in$ $H^{d(\mathfrak{s})}\left(\mathcal{B}^{\sigma}\left(X_{0}\right) ; \mathbb{Z}\right)$ is induced by $\bar{z} \cup \bar{\eta}$. Here, the product operation is defined in [16, §23.2, §26.2] and given in terms of Čech cocycle representatives as follows. Fix suitable ${ }^{31}$ open covers $\left\{\mathcal{U}_{0}, \mathcal{U}_{\mathcal{I}}, \mathcal{U}_{\mathcal{N}}\right\}$ of $\left\{\mathcal{B}^{\sigma}\left(X_{0}\right), \mathcal{B}^{\sigma}(\mathcal{I}), \mathcal{B}^{\sigma}(\mathcal{N})\right\}$, fix a suitable refinement $\mathcal{V}$ of the open cover $[0, \infty] \times \mathcal{U}_{\mathcal{N}} \times \mathcal{U}_{\mathcal{I}} \times \mathcal{U}_{0}$ of $[0, \infty] \times \mathcal{B}^{\sigma}(\mathcal{N}) \times \mathcal{B}^{\sigma}(\mathcal{I}) \times \mathcal{B}^{\sigma}\left(X_{0}\right)$, let $\mathcal{B}^{\sigma}(X)^{o}$ be the domain on which each $R_{\square}$ is defined, and let $\mathcal{U}$ be the pull-back of $\mathcal{V}$ under the map $\mathcal{B}^{\sigma}(X)^{o} \rightarrow\{0\} \times \mathcal{B}^{\sigma}(\mathcal{N}) \times \mathcal{B}^{\sigma}(\mathcal{I}) \times \mathcal{B}^{\sigma}\left(X_{0}\right)$. After fixing a cocycle $\mathfrak{u}_{0}(\bar{z}, \bar{\eta}) \in \check{C}^{d(\mathfrak{s})}\left(\mathcal{U}_{0} ; \mathbb{Z} / 2 \mathbb{Z}\right)$ which represents the class $u_{0}$, the pull-back of the cocycle $1 \times 1 \times \mathfrak{u}_{0}(\bar{z}, \bar{\eta}) \in \check{C}^{d(\mathfrak{s})}(\mathcal{V} ; \mathbb{Z} / 2 \mathbb{Z})$ is a cocycle $\mathfrak{u} \in \check{C}^{d(\mathfrak{s})}(\mathcal{U} ; \mathbb{Z} / 2 \mathbb{Z})$ which represents the class $u$. We will specify the choice of $\mathfrak{u}_{0}(\bar{z}, \bar{\eta})$ momentarily.

There is a continuous map defined in [16, §26.1],
$$r: \mathcal{M}^{+}(X, \mathfrak{s}) \rightarrow[0, \infty] \times \mathcal{B}^{\sigma}(\mathcal{N}, \mathfrak{s}) \times \mathcal{B}^{\sigma}\left(\mathcal{I}, \mathfrak{s}_{\xi_{0}}+1\right) \times \mathcal{B}^{\sigma}\left(X_{0}, \mathfrak{s}_{\mathfrak{s}}\right)$$
which is given by $(T, \mathfrak{d}) \mapsto\left(T,\left.\mathfrak{d}\right|_{\mathcal{N}},\left.\mathfrak{d}\right|_{\mathcal{I}},\left.\mathfrak{d}\right|_{X_{0}}\right)$ for $T<\infty$, in particular. The image $r\left(\mathcal{M}^{+}(X, \mathfrak{s})\right)$ is also stratified by manifolds, and the only relevant strata which pair nontrivially with the cocycle $1 \times 1 \times \mathfrak{u}_{0}(\bar{z}, \bar{\eta})$ are determined by
$$\begin{aligned}
\operatorname{dim} M\left(\varnothing, \mathcal{N}_{k}, \mathfrak{c}_{1}^{k} ; \mathfrak{s}\right) & =0 \\
\operatorname{dim} M\left(\mathfrak{c}_{1}^{k}, \mathcal{I}_{k}, \mathfrak{c}_{2}^{k} ; \mathfrak{s}_{\xi_{0}}+1\right) & =0 \\
\operatorname{dim} \mathfrak{M}\left(\mathfrak{c}_{2}, X_{0}, \varnothing ; \mathfrak{s}_{\mathfrak{s}}\right) & =d(\mathfrak{s})
\end{aligned}$$
for each $k$. The dimensions of $M\left(\varnothing, \mathcal{N}_{k}, \mathfrak{c}_{1}^{k} ; \mathfrak{s}\right)$ are computed in Lemma 5.3 below, from which it follows that (5.2) forces $\mathfrak{c}_{1}^{k}=\mathfrak{a}_{-1}$. Then (5.3) forces $\left|\mathfrak{c}_{2}^{k}\right|=\left|\mathfrak{c}_{1}^{k}\right|$, which follows immediately from the definition of the grading (see [16, §22.3]), or less directly from the fact that such a product cobordism induces an isomorphism on all monopole Floer (co)homologies. As explained in [16, §36], $\widehat{H M}^{\left[\xi_{*}\right]}\left(S^{1} \times S^{2}, \mathfrak{s}_{\xi_{0}}+1\right)$ is isomorphic to $\widetilde{H M}_{\left[\xi_{*}\right]}\left(S^{1} \times S^{2}, \mathfrak{s}_{\xi_{0}}+1\right)$, with the former generated by $\mathfrak{a}_{-1}$ and the latter generated by $\mathfrak{b}_{0} .^{32}$ Thus, each $\mathfrak{c}_{2}^{k}$ must be one of the finitely many irreducible generators $\mathfrak{c} \in \widehat{C M}^{\left[\xi_{*}\right]}\left(S^{1} \times S^{2}, \mathfrak{s}_{\xi_{0}}+1, \mathfrak{q}_{\lambda}\right)$ satisfying (5.4), and hence $g(\mathfrak{s})=N\left[\xi_{*}\right]$.
Notation 5.2. Here and in what follows, we abuse notation by letting $\mathfrak{c}$ and $\mathfrak{a}_{-1}$ denote either the respective monopoles $\mathfrak{c}^{k}$ and $\mathfrak{a}_{-1}$ on a single component of $\partial X_{0}$ or the respective collections $\left\{\mathfrak{c}^{k}\right\}_{1 \leq k \leq N}$ and $\left\{\mathfrak{a}_{-1}\right\}_{1 \leq k \leq N}$. Also, we refer to $\mathfrak{c}$ as both a monopole and a cochain in $\widehat{C M}^{*}$ while $\hat{\mathfrak{c}}$ denotes the corresponding chain in $\widehat{C M}_{*}$ which pairs nontrivially with the cochain $\mathfrak{c}$, i.e. $\mathfrak{c}(\hat{\mathfrak{c}})=1$.

\footnotetext{
${ }^{30}$ There is no ambiguity in the resulting 4-manifold because every self-diffeomorphism of $S^{1} \times S^{2}$ extends to $S^{1} \times B^{3}$.
${ }^{31}$ The word "suitable" in this context means that the open covers are transverse (in the sense of [16, §21.2]) to all strata in all compactified moduli spaces under consideration.
${ }^{32}$ Both $\mathfrak{a}_{-1}$ and $\mathfrak{b}_{0}$ belong to the same absolute grading in $J\left(S^{1} \times S^{2}, \mathfrak{s}_{\xi_{0}}+1\right)$ because their $\mathbb{Z}$-grading difference is $\operatorname{gr}\left[\mathfrak{a}_{-1}, \mathfrak{b}_{0}\right]=0$ (see 16, Equation 16.9, Equation 36.1]).
}

As explained in [16, §21], there is a $\mathbb{Z} / 2 \mathbb{Z}$-pairing (denoted by $\langle\cdot, \cdot\rangle$ ) between Čech cochains and our moduli spaces. The version of Stokes' theorem in [16, §21], applied to the $\mathbb{Z} / 2 \mathbb{Z}$-pairing of $r\left(\mathcal{M}^{+}(X, \mathfrak{s})\right)$ with $\delta\left(1 \times 1 \times \mathfrak{u}_{0}(\bar{z}, \bar{\eta})\right)=0$, implies
$$\begin{aligned}
S W_{X}(\mathfrak{s})\left(\left[\eta_{1}\right] \wedge \cdots \wedge\left[\eta_{p}\right]\right) & =\langle u,[\mathfrak{M}(\mathfrak{s})]\rangle=\langle\mathfrak{u}, \mathfrak{M}(\mathfrak{s})\rangle \\
& =\sum_{\mathfrak{c} \in N\left[\xi_{*}\right]}\left\langle 1, M\left(\mathfrak{a}_{-1}, \mathcal{I}, \mathfrak{c} ; \mathfrak{s}_{\xi_{0}}+1\right)\right\rangle \cdot\left\langle\mathfrak{u}_{0}(\bar{z}, \bar{\eta}), \mathfrak{M}\left(\mathfrak{c}, X_{0}, \varnothing ; \mathfrak{s}_{\mathfrak{s}}\right)\right\rangle \\
& =: \sum_{\mathfrak{c} \in N\left[\xi_{*}\right]} \mathbb{M}_{\mathfrak{c}} \mathfrak{M}_{\mathfrak{c}}
\end{aligned}$$
where we use the fact (Lemma 5.3 below) that the moduli space $M\left(\varnothing, \mathcal{N}_{k}, \mathfrak{a}_{-1} ; \mathfrak{s}\right)$ is a single point. Here, $\mathbb{M}_{\mathfrak{c}}$ is the count of points in the 0-dimensional moduli space $M\left(\mathfrak{a}_{-1}, \mathcal{I}, \mathfrak{c} ; \mathfrak{s}_{\xi_{0}}+1\right)$, while $\mathfrak{M}_{\mathfrak{c}}$ is computed by specifying the choice of $\mathfrak{u}_{0}(\bar{z}, \bar{\eta})$. As explained in [17, §2.5.4], there is a choice such that $\mathfrak{M}_{\mathfrak{c}}$ is the count of points in $\mathfrak{M}_{d(\mathfrak{s})}\left(\mathfrak{c}, X_{0}, \varnothing ; \mathfrak{s}_{\mathfrak{s}}, \bar{z}, \bar{\eta}\right)$, i.e. the number defined by (5.1) (note that by Lemma 4.11, $\mathfrak{c}$ satisfies $E(\mathfrak{c})<2 \pi \rho_{\mathfrak{s}}$ and hence corresponds to an admissible orbit set).

We now reinterpret the sum in (5.5) to see that it equals the near-symplectic Gromov invariant. The $k$ th monopole Floer chain complex in grading $\left[\xi_{*}\right]$ is $\widehat{C M}_{\left[\xi_{*}\right]}\left(S^{1} \times S^{2}, \mathfrak{s}_{\xi_{0}}+1, \mathfrak{q}_{f}\right)=\mathbb{Z} / 2 \mathbb{Z}\left\langle\hat{\mathfrak{a}}_{-1}\right\rangle$. The cobordism $\mathcal{I}_{k}$ induces a chain map
$$\hat{m}_{k}: \widehat{C M}_{*}\left(S^{1} \times S^{2}, \mathfrak{s}_{\xi_{0}}+1, \mathfrak{q}_{f}\right) \rightarrow \widehat{C M}_{*}\left(S^{1} \times S^{2}, \mathfrak{s}_{\xi_{0}}+1, \mathfrak{q}_{\lambda}\right)$$
which is a quasi-isomorphism [16, Corollary 23.1.6], and in grading $\left[\xi_{*}\right]$ it is given by
$$\hat{\mathfrak{a}}_{-1} \mapsto \sum_{\mathfrak{c}^{k} \in\left[\xi_{*}\right]} \mathbb{M}_{\mathfrak{c}^{k}} \hat{\mathfrak{c}}^{k}$$
where $\mathbb{M}_{\mathfrak{c}^{k}}$ denotes the count of points in the 0-dimensional moduli space $M\left(\mathfrak{a}_{-1}, \mathcal{I}_{k}, \mathfrak{c}^{k} ; \mathfrak{s}_{\xi_{0}}+1\right)$. Thus, $\mathcal{I}$ induces the chain map
$$\hat{m}=\bigotimes_{k=1}^{N} \hat{m}_{k}: \bigotimes_{k=1}^{N} \widehat{C M}_{*}\left(S^{1} \times S^{2}, \mathfrak{s}_{\xi_{0}}+1, \mathfrak{q}_{f}\right) \rightarrow \bigotimes_{k=1}^{N} \widehat{C M}_{*}\left(S^{1} \times S^{2}, \mathfrak{s}_{\xi_{0}}+1, \mathfrak{q}_{\lambda}\right)$$
which is also a quasi-isomorphism, and in grading $N\left[\xi_{*}\right]$ it sends $\hat{\mathfrak{a}}_{-1}$ to $\sum_{\mathfrak{c} \in N\left[\xi_{*}\right]} \mathbb{M}_{\mathfrak{c}} \hat{\mathfrak{c}}$ because $\mathbb{M}_{\mathfrak{c}}=\prod_{k=1}^{N} \mathbb{M}_{\mathfrak{c}^{k}}$. Since $\left[\hat{m}\left(\hat{\mathfrak{a}}_{-1}\right)\right]$ is the generator of $\bigotimes_{k=1}^{N} \widehat{H M}_{\left[\xi_{*}\right]}\left(S^{1} \times S^{2}, \mathfrak{s}_{\xi_{0}}+1\right) \cong \mathbb{Z} / 2 \mathbb{Z}$, the near-symplectic Gromov invariant is the evaluation of the Seiberg-Witten cocycle $\Phi_{S W} \in$ $\bigotimes_{k=1}^{N} \widehat{C M}^{\left[\xi_{*}\right]}\left(S^{1} \times S^{2}, \mathfrak{s}_{\xi_{0}}+1, \mathfrak{q}_{\lambda}\right)$ at the cycle $\hat{m}\left(\hat{\mathfrak{a}}_{-1}\right)$,
$$G r_{X, \omega}(\mathfrak{s})\left(\left[\eta_{1}\right] \wedge \cdots \wedge\left[\eta_{p}\right]\right) \equiv_{(2)} \Phi_{S W}\left(\sum_{\mathfrak{c} \in N\left[\xi_{*}\right]} \mathbb{M}_{\mathfrak{c}} \hat{\mathfrak{c}}\right)=\sum_{\mathfrak{c} \in N\left[\xi_{*}\right]} \mathbb{M}_{\mathfrak{c}} \mathfrak{M}_{\mathfrak{c}}$$
This number is precisely that in (5.5), so the proof is complete. \(\square\)

Lemma 5.3. For sufficiently small perturbations $\mathfrak{p}_{\mathcal{N}}$ and $\mathfrak{q}_{f}$ specified in the proof of Theorem 5.1, the moduli spaces $M\left(\varnothing, S^{1} \times B^{3}, \mathfrak{a}_{i} ; \mathfrak{s}\right)$ and $M\left(\varnothing, S^{1} \times B^{3}, \mathfrak{b}_{i} ; \mathfrak{s}\right)$ are empty for $i \geq 0$. The moduli space $M\left(\varnothing, S^{1} \times B^{3}, \mathfrak{a}_{-i} ; \mathfrak{s}\right)$ has dimension $2 i-2$ for $i \geq 1$, such that $M\left(\varnothing, S^{1} \times B^{3}, \mathfrak{a}_{-1} ; \mathfrak{s}\right)$ is a point, and the moduli space $M\left(\varnothing, S^{1} \times B^{3}, \mathfrak{b}_{-i} ; \mathfrak{s}\right)$ has dimension $2 i-1$ for $i \geq 1$.

Proof. We mimic the analogous proof for a 4-ball $B^{4}$ in [16, Lemma 27.4.2]. The key point is that both $S^{1} \times B^{3}$ and $B^{4}$ have metrics of positive scalar curvature and have trivial 2nd (co)homology. We have already discussed the $\mathfrak{q}_{f}^{\sigma}$-perturbed SW monopoles over $\left(S^{1} \times S^{2}, \mathfrak{s}_{\xi_{0}}+1\right)$ at the beginning of Theorem 5.1, and we continue to use that notation.

With respect to the unperturbed Seiberg-Witten equations (without blowing up) over $\overline{S^{1} \times B^{3}}$, there are no solutions with nonzero spinor $\Phi$ that decay to zero on the cylindrical end $[0, \infty) \times S^{1} \times S^{2}$ because the scalar curvature is positive (see the integration-by-parts trick of [16, Proposition 4.6.1]). For $\mathfrak{p}_{\mathcal{N}}$ sufficiently small the reducible solutions persist and are asymptotic to $\alpha=\left[\mathbf{A}_{\alpha}, 0\right]$ or $\beta=\left[\mathbf{A}_{\beta}, 0\right]$.

Now, the restriction of a reducible solution $\mathfrak{d} \in M\left(\varnothing, S^{1} \times B^{3}, \mathfrak{a}_{i} ; \mathfrak{s}\right)$ to the cylindrical end is a path
$$\check{\mathfrak{d}}(t)=\left[\mathbf{A}_{\mathfrak{a}}, 0, \psi(t)\right]$$
with $\psi(t)$ approaching the $S^{1}$-orbit of $\psi_{i}$ as $t \rightarrow \infty$, where $\mathfrak{a}_{i}=\left[\mathbf{A}_{\alpha}, 0, \psi_{i}\right]$. Following the argument of [16, Proposition 14.6.1], we would then obtain a nonzero solution to the perturbed Dirac equation on $S^{1} \times B^{3}$ with asymptotics $C e^{-\lambda_{i} t} \psi_{i}$ (nonzero constant $C$ ) as $t \rightarrow \infty$ on the cylindrical end. If $\lambda_{i}>0$ then we just argued that such spinors cannot exist, so $M\left(\varnothing, S^{1} \times B^{3}, \mathfrak{a}_{i} ; \mathfrak{s}\right)$ is empty. If $\lambda_{-i}<0$ then, as in [16, Proposition 14.6.1], such spinors with growth bound $C e^{-\lambda_{-i} t}$ have the form
$$\sum_{k=-i}^{-1} c_{k} e^{-\lambda_{k} t} \psi_{k}$$
on the cylindrical end. Thus, $\operatorname{dim} M\left(\varnothing, S^{1} \times B^{3}, \mathfrak{a}_{-i} ; \mathfrak{s}\right)=2(i-1)$ and $M\left(\varnothing, S^{1} \times B^{3}, \mathfrak{a}_{-1} ; \mathfrak{s}\right)$ is a single point.

On the other hand, the restriction of a reducible solution $\mathfrak{d} \in M\left(\varnothing, S^{1} \times B^{3}, \mathfrak{b}_{i} ; \mathfrak{s}\right)$ to the cylindrical end is a path
$$\check{\mathfrak{d}}(t)=[\mathbf{A}(t), 0, \psi(t)]$$
with $\mathbf{A}(t)$ a trajectory lying over a Morse flowline of $f$ on $\mathbb{T} \subset \mathcal{B}\left(S^{1} \times S^{2}, \mathfrak{s}_{\xi_{0}}+1\right)$ and asymptotic to $\mathbf{A}_{\beta}$. We compute $\operatorname{dim} M\left(\varnothing, S^{1} \times B^{3}, \mathfrak{b}_{-i} ; \mathfrak{s}\right)$ for $i \geq 1$ indirectly, thanks to the formal dimension formula
$$\operatorname{dim} M\left(\varnothing, S^{1} \times B^{3}, \mathfrak{b}_{-i} ; \mathfrak{s}\right)=\operatorname{dim} M\left(\varnothing, S^{1} \times B^{3}, \mathfrak{a}_{-i} ; \mathfrak{s}\right)+\operatorname{gr}\left[\mathfrak{a}_{-i}, \mathfrak{b}_{-i}\right]$$
given by [16, Proposition 24.4.6]. Since $\operatorname{gr}\left[\mathfrak{a}_{-i}, \mathfrak{b}_{-i}\right]=\operatorname{ind}_{f}(\alpha)-\operatorname{ind}_{f}(\beta)=1$, the dimension of $M\left(\varnothing, S^{1} \times B^{3}, \mathfrak{b}_{-i} ; \mathfrak{s}\right)$ must be $2(i-1)+1$. Finally, by [16, Proposition 24.4.3] we see that $M\left(\varnothing, S^{1} \times B^{3}, \mathfrak{b}_{i} ; \mathfrak{s}\right)$ must be empty for $i \geq 0$ because $\mathfrak{b}_{i}$ is boundary-stable and there are no irreducible $\mathfrak{p}_{\mathcal{N}}$-perturbed SW instantons over $S^{1} \times B^{3}$. \(\square\)

Remark 5.4. The following heuristic was suggested by Mrowka and can be made precise. The holonomy map
$$\text { hol : } \mathfrak{M}(X, \mathfrak{s}) \rightarrow \prod_{k=1}^{N} U(1)$$
along the $N$ zero-circles of $\omega$ is cobordant (in some sense) to the restriction map
$$\operatorname{res}: M\left(X_{0}, \mathfrak{s}_{\mathfrak{s}}\right) \rightarrow \prod_{k=1}^{N} \mathcal{B}^{\text {red }}\left(S^{1} \times S^{2}, \mathfrak{s}_{\xi_{0}}+1\right)$$
where $M\left(X_{0}, \mathfrak{s}_{\mathfrak{s}}\right)$ is the moduli space of Seiberg-Witten solutions to the unperturbed equations on $X_{0}$ without blowing up. Here, $\mathcal{B}^{\text {red }}\left(S^{1} \times S^{2}, \mathfrak{s}_{\xi_{0}}+1\right)$ is identified with $U(1)$ by taking the holonomy of a flat connection along the $S^{1}$-factor of $S^{1} \times S^{2}$.

\section*{Acknowledgements}

The author is indebted to his advisor Michael Hutchings as well as Clifford Taubes - their roles in this work are evident, and their guidance pivotal. The author also thanks Tomasz Mrowka for helping to understand certain aspects of monopole Floer homology, and the anonymous referee for suggesting many clarifications/corrections to the original draft of this paper. This paper forms part of the author's Ph.D. thesis. The author was partially supported by NSF grants DMS-1406312, DMS-1344991, DMS-0943745, and DMS-1708899.

\section*{A Appendix: some explanation to Taubes' analysis}

This paper can be viewed as a sort of amalgam of [31] and [28]. There was a complicated feature of [28] that did not arise in [31], and a complicated feature of [31] that did not arise in [28], and both features appeared in this paper. Namely, the multiply covered tori in [28] had to be delicately counted and the map to the Seiberg-Witten moduli space required the use of Kuranishi structures, and $\mathbb{R}$-invariance in [31] played a complicating role for the analysis associated with non- $\mathbb{R}$-invariant holomorphic curves. This latter complication came from the existence of multiple ends of a curve hitting the same orbit, or a single end hitting an orbit with multiplicity. An elaboration is given in [31, §5.c.1], and a slightly different elaboration is given below.

In the compact scenario, in order to build a Seiberg-Witten solution from a pseudoholomorphic curve $C$ with multiplicity $n$, an $n$-vortex solution is "grafted" into the normal bundle $N_{C}$, and a disk-subbundle of $N_{C}$ is embedded into the ambient 4-manifold. In the noncompact scenario, if we were to mimic the previous sentence for a pseudoholomorphic curve $C$ with $n>1$ ends approaching a single orbit $\gamma$, then a 1-vortex solution would be "grafted" into $N_{C}$ for each end of $C$. But to ensure embeddedness of a disk-subbundle the radii of its disk-fibers would need to shrink as $\gamma$ is approached. Subsequently, the Dirac operator evaluated at the corresponding spinor would involve derivatives of the radial coordinate of the fibers, and this would ultimate prevent us from getting the appropriate bounds on the spinor (as needed to obtain a nearby Seiberg-Witten solution).

To resolve this issue, a 1-vortex solution is not "grafted" into $N_{C}$ for each of its $n$ ends. Instead, consider the normal bundle $N_{\mathbb{R} \times \gamma}$ of the cylinder $\mathbb{R} \times \gamma$. Then $N_{C}$ and $N_{\mathbb{R} \times \gamma}$ are "nearby" to each other along the ends of $C$ and $\mathbb{R} \times \gamma$, and objects defined on them can be compared using cutoff-functions and a change of variables. The (ends of the) curve $C$ intersects any given fiber of $N_{\mathbb{R} \times \gamma}$ in $n$ points, and an $n$-vortex solution is "grafted" into each fiber of $N_{\mathbb{R} \times \gamma}$ whose zeros are those $n$ points. This solution is then compared to the would-be solution from the original approach, and is seen to be approximately the same except for the worry of varying radial coordinates.

The methodology of the previous paragraph is inspired by the following fact in vortex theory: Given two 1 -vortices spaced far apart in $\mathbb{R}^{2}$ and one 2 -vortex in $\mathbb{R}^{2}$ whose zeros are located at the two 1-vortices, the difference between the pair of 1-vortices and the single 2-vortex is exponentially small with respect to the distance between the two 1-vortices. See Figure 4 for a qualitative visual.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/d787d2b4-e9c9-4ab7-9c05-44a3a9f294e2-43.jpg?height=276&width=638&top_left_y=251&top_left_x=742}
\captionsetup{labelformat=empty}
\caption{Figure 4: Zeros of a single 2-vortex with different separations (Adapted from [21])}
\end{figure}

\section*{References}
\begin{itemize}
\item[] [1] E. Calabi, An intrinsic characterization of harmonic one-forms, Papers in Honor of K. Kodaira, Princeton University Press, Princeton, NJ, 1969, pp. 101-117.
\item[] [2] D. Cristofaro-Gardiner, The absolute gradings on embedded contact homology and Seiberg-Witten Floer cohomology, Alg. Geom. Topol. 13 (2013), 2239-2260.
\item[] [3] C. Gerig, Taming the pseudoholomorphic beasts in $\mathbb{R} \times\left(S^{1} \times S^{2}\right)$, Geom. Topol. 24 (2020), no. 4, 1791-1839.
\item[] [4] $\_\_\_\_$, Circle-valued Morse theory and Seiberg-Witten invariants of 3-manifolds, in preparation.
\item[] [5] R. Gompf, Handlebody construction of Stein surfaces, Annals of Mathematics 148 (1998), no. 2, 619-693.
\item[] [6] K. Honda, A note on Morse theory of harmonic 1-forms, Topology 38 (1998), no. 1, 223-233.
\item[] [7] $\_\_\_\_$, Transversality theorems for harmonic forms, Rocky Mountain J. Math. 34 (2004), no. 2, 629-664.
\item[] [8] M. Hutchings, Reidemeister torsion in generalized Morse theory, Forum Math. 14 (2002), 209-244.
\item[] [9] $\_\_\_\_$, The embedded contact homology index revisited, New perspectives and challenges in symplectic field theory, CRM Proc. Lecture Notes, vol. 49, Amer. Math. Soc., Providence, RI, 2009, pp. 263-297. Erratumibid. Erratum to "The ECH index revisited", blog post https://floerhomology.wordpress.com/2014/07/09/erratum-to-the-ech-index-revisited/ (version: 2014-07-09).
\item[] [10] $\_\_\_\_$, Embedded contact homology as a (symplectic) field theory, in preparation.
\item[] [11] M. Hutchings and Y. J. Lee, Circle-valued Morse theory, Reidemeister torsion, and Seiberg-Witten invariants of 3-manifolds, Topology 38(4) (1999), 861-888.
\item[] [12] $\_\_\_\_$, Circle-valued Morse theory and Reidemeister torsion, Geom. Topol. 3 (1999), 369-396.
\item[] [13] M. Hutchings and C. Taubes, Proof of the Arnold chord conjecture in three dimensions II, Geom. Topol. 17 (2013), 2601-2688.
\item[] [14] A. Jaffe and C. Taubes, Vortices and monopoles. Structure of static gauge theories, Progress in Physics 2, Birkhäuser, Boston, 1980.
\item[] [15] P. Kronheimer, T. Mrowka, P. Ozsváth, and Z. Szabó, Monopoles and lens space surgeries, Annals of Mathematics 165 (2007), 457-546.
\item[] [16] P. Kronheimer and T. Mrowka, Monopoles and three-manifolds, New Mathematical Monographs, vol. 10, Cambridge University Press, Cambridge, 2007.
\item[] [17] C. Kuthulan, Y.-J. Lee, and C. Taubes, HF=HM V: Seiberg-Witten Floer homology and handle additions, Geom. Topol. 24 (2020), no. 7, 3471-3748.
\item[] [18] C. LeBrun, Yamabe constants and the perturbed Seiberg-Witten equations, Comm. Anal. Geom. 5 (1997), no. 3, 535-553.
\item[] [19] T. Li and A. Liu, The equivalence between $S W$ and $G r$ in the case where $b^{+}=1$, IMRN 7 (1999), 335-345.
\item[] [20] K. Luttinger and C. Simpson, A normal form for the birth/fight of closed selfdual 2-form degeneracies, unpublished (1996).
\item[] [21] N. Manton and P. Sutcliffe, Topological Solitons, Cambridge University Press, New York, 2004.
\item[] [22] C. Okonek and A. Teleman, 3-dimensional Seiberg-Witten invariants and non-Kählerian geometry, Math. Ann. 312 (1998), 261-288.
\end{itemize}
[23] P. Ozsváth and Z. Szabó, The symplectic Thom conjecture, Annals of Mathematics 151 (2000), no. 1, 93-124.
[24] D. Salamon, Seiberg-Witten invariants of mapping tori, symplectic fixed points, and Lefschetz numbers, Proceedings of 6th Gökova Geometry-Topology Conference, 1999, pp. 117-143.
[25] C. Taubes, Counting pseudo-holomorphic submanifolds in dimension 4, J. Diff. Geom. 44 (1996), no. 4, 818-893.
[26] $\_\_\_\_$, SW ⇒ Gr: from the Seiberg-Witten equations to pseudo-holomorphic curves, J. Amer. Math. Soc. 9 (1996), no. 3, 845-918.
[27] $\_\_\_\_$, Gr ⇒ SW: from pseudo-holomorphic curves to Seiberg-Witten solutions, J. Diff. Geom. 51 (1999), 203-334.
[28] $\_\_\_\_$, Seiberg-Witten and Gromov invariants for symplectic 4-manifolds, First International Press Lecture Series, vol. 2, International Press, Somerville, MA, 2000. Edited by Richard Wentworth.
[29] $\_\_\_\_$, Gr = SW: counting curves and connections, Seiberg Witten and Gromov invariants for symplectic 4-manifolds, 2000, pp. 275-401.
[30] $\_\_\_\_$, Arbitrary $N$-Vortex Solutions to the First Order Ginzburg-Landau Equations, Commun. Math. Phys. 72 (1980).
[31] $\_\_\_\_$, Embedded contact homology and Seiberg-Witten Floer cohomology I, Geom. Topol. 14 (2010), no. 5, 2497-2581.
[32] $\_\_\_\_$, Embedded contact homology and Seiberg-Witten Floer cohomology II, Geom. Topol. 14 (2010), no. 5, 2583-2720.
[33] $\_\_\_\_$, Embedded contact homology and Seiberg-Witten Floer cohomology III, Geom. Topol. 14 (2010), no. 5, 2721-2817.
[34] $\_\_\_\_$, Embedded contact homology and Seiberg-Witten Floer cohomology IV, Geom. Topol. 14 (2010), no. 5, 2819-2960. Erratum-ibid. Correction to a lemma in: Embedded contact homology and Seiberg-Witten Floer cohomology IV, preprint arXiv:1801.07556
[35] $\_\_\_\_$, Embedded contact homology and Seiberg-Witten Floer cohomology V, Geom. Topol. 14 (2010), no. 5, 2961-3000.
[36] V. Turaev, A combinatorial formulation for the Seiberg-Witten invariants of 3-manifolds, Math. Res. Lett. 5 (1998), 583-598.
[37] $\_\_\_\_$, Torsion invariants of Spin ${ }^{c}$-structures on 3-manifolds, Math. Res. Lett. 4 (1997), 679-695.
[38] C. Wendl, Automatic transversality and orbifolds of punctured holomorphic curves in dimension four, Comment. Math. Helv. 85 (2010), no. 2, 347-407.

Department of Mathematics, UC Berkeley, CA 94720, USA
E-mail address: cgerig@berkeley.edu