---
retention_scope: session
part: 2
total_parts: 3
---

[Part 2/3 of: Degenerations of negative Kähler–Einstein surfaces]

We adopt the coordinates $u_{1}, u_{2}$ defined above so that the map $\pi: \mathcal{M}^{*} \rightarrow D \times$ $[-1,1 / 2] \backslash\{p\}$ is identified with the Hopf fibration. Define $\Theta_{0}$ by Equation 4.1, taking $a=T, J$ the natural complex structure on $\mathbb{C}_{u_{1}, u_{2}}^{2}$, and with $\pi_{H}$ given by $\pi$. Note also that by our choice of coordinates in Section 4.2, $r=r_{w}$. By Equations 3.26, 3.27, and 4.3, we have that near $p \in D \times[-1,1 / 2]$,
$$\begin{aligned}
\Gamma-d \Theta_{0} & =\partial_{z}\left(\tilde{\omega}-T^{-1} \omega_{0}\right)+d w \wedge d_{D}^{c}\left(\frac{h}{T}-\frac{1}{2 r_{w}}-T\right) \\
& =\partial_{z}\left(g^{2, \alpha}+w^{1}\right) \frac{i}{2} d y \wedge d \bar{y}+d w \wedge d_{D}^{c}\left(g^{2, \alpha}+w^{1}\right) \\
& =c_{1} d y \wedge d \bar{y}+c_{2} d w \wedge d y+c_{3} d w \wedge d \bar{y}
\end{aligned}$$
for some $c_{1} \in C^{1, \alpha}(U)+W^{0}(U)$ and $c_{2}, c_{3} \in C^{2, \alpha}(U)+W^{1}(U)$. Pulling back to $\mathcal{M}^{*}$, we have that with respect to the flat metric in $u_{1}, u_{2}$,
$$\pi^{*}\left(c_{1} d y \wedge d \bar{y}\right)=\left(g^{1, \alpha}+w^{0}\right) \mathcal{O}\left(s^{2}\right)=g^{1, \alpha}$$
while by the same argument the $c_{2}$ and $c_{3}$ term have higher regularity. Therefore we denote $\omega^{1, \alpha}=c_{1} d y \wedge d \bar{y}+c_{2} d w \wedge d y+c_{3} d w \wedge d \bar{y}$.

If we impose the gauge-fixing condition $d^{*} \theta=0$, then for some $\epsilon>0$, we can solve the elliptic system
$$\left\{\begin{array}{l}
d \theta=\omega^{1, \alpha} \\
d^{*} \theta=0 \\
\theta(\nu)=0 \text { on } \delta B_{\epsilon}(p)
\end{array}\right.$$
on $B_{\epsilon}(p)$, where $\nu$ is the unit normal to $B_{\epsilon}(p)$. The resulting one-form $\theta$ is smooth away from $\pi^{-1} p$ since $\omega^{1, \alpha}$ is, and since the system is $S^{1}$ invariant, $\theta$ can be chosen $S^{1}$-invariant by averaging. We also have that $\theta \in C^{2, \alpha}\left(B_{\epsilon}(p)\right)$, since
$$\Delta \theta=d^{*} \omega^{1, \alpha} \in C^{0, \alpha}\left(B_{\epsilon}(p)\right) .$$
Finally, $\theta\left(\partial_{t}\right)=0$. For by Cartan's formula, $d\left(\iota_{\partial_{t}} \theta\right)=-\iota_{\partial_{t}} \omega^{1, \alpha}=0$, so $\theta\left(\partial_{t}\right)$ is constant. But $\partial_{t} \rightarrow 0$ near $p$, so by the regularity of $\theta, \theta\left(\partial_{t}\right)=0$.

Now define $\Theta=\Theta_{0}+\theta$. Because $d \Theta=\Gamma=d \Theta^{\prime}$, there is a gauge transformation that takes $\Theta^{\prime}$ to $\Theta$. Since gauge transformations only rotate the fibers of the $S^{1}$ bundle, $\pi$ is still modelled on the Hopf fibration as in Equation 4.9. However, we will see in Section 5.9 by taking $\Theta$ as our connection, $\omega$ is asymptotic to the Taub-NUT metric near $p$. Therefore ( $\mathcal{M}, \omega$ ) is a $C^{2, \alpha}$ compactification of $\mathcal{M}^{*}$.

\section*{5. Limiting Behavior of the Approximate Solution}
5.1. Convergence of Riemannian manifolds. The space ( $\mathcal{M}, \omega_{T}$ ) we constructed in Sections 3 and 4 is Kähler, but since it solves the linearization of Equation 2.10 rather than the full equation, it is only approximately Einstein. We aim to argue that for large enough $T, \omega_{T}$ is sufficiently close to being Einstein that it can be perturbed to an Einstein metric. Several notions of the distance between metrics will be useful in making this argument. Our discussion in this section follows [16] Chapter 11.
5.1.1. Gromov-Hausdorff convergence. The weakeast notion of convergence we use is Gromov-Hausdorff convergence. The Gromov-Hausdorff distance quantifies the dissimilarity between metric spaces.

Definition 5.1. Let $\left(X, d_{X}\right)$ and $\left(Y, d_{Y}\right)$ be metric spaces and let $\mathcal{A}$ be the set of metrics on $X \cup Y$ that extend $d_{X}$ and $d_{Y}$. The Gromov-Hausdorff distance is defined as
$$d_{\mathrm{GH}}\left(\left(X, d_{X}\right),\left(Y, d_{Y}\right)\right)=\inf _{d \in \mathcal{A}} d(X, Y),$$
where for a metric $d$ on $X \cup Y, d(X, Y)=\inf \{\epsilon: \forall x \in X, \exists y \in Y: d(x, y)<\epsilon\}$.
In Riemannian geometry, the metric spaces will be Riemannian manifolds $(M, g)$ with the metric $d_{g}$ induced by distance in the Riemannian metric $g$. Thus we say that $\left(M_{i}, g_{i}\right)$ converges to $(M, g)$ in the Gromov-Hausdorff topology if
$$d_{\mathrm{GH}}\left(\left(M_{i}, d_{g_{i}}\right),\left(M, d_{g}\right)\right) \rightarrow 0$$
as $i \rightarrow \infty$. In such a situation, we may also informally say that $x_{i} \in M_{i} \rightarrow x \in M$ if there exists a sequence of metrics $d_{i} \in \mathcal{A}$ realizing the Gromov-Hausdorff convergence such that $d\left(x_{i}, x\right) \rightarrow 0$.

The Gromov-Hausdorff distance defines a complete, separable metric space on the set of equivalence classes under isometry of compact metric spaces (see [16] 11.1.18). On noncompact spaces, we instead consider pointed Gromov-Hausdorff convergence. Let $\left(X, d_{X}, x\right)$ and $\left(Y, d_{Y}, y\right)$ be metric spaces with distinguished points $x$ and $y$. We define
$$d_{\mathrm{GH}}\left(\left(X, d_{X}, x\right),\left(Y, d_{Y}, y\right)\right)=\inf _{d \in \mathcal{A}}(d(X, Y)+d(x, y)) .$$

Then $\left(X_{i}, d_{X_{i}}, x_{i}\right) \rightarrow\left(X, d_{X}, x\right)$ if for all $R>0,\left(\bar{B}_{R}\left(x_{i}\right), d_{X_{i}}, x_{i}\right) \rightarrow\left(\bar{B}_{R}(x), d_{X}, x\right)$ with respect to the pointed Gromov-Hausdorff distance.

Gromov-Hausdorff convergence on its own is a relatively weak notion. It does not imply the convergence of derivatives in any sense, and limits of manifolds may not be manifolds. In addition, a sequence of $n$-dimensional manifolds may converge to a manifold of any lower dimension (by collapsing) or higher dimension (by space-filling). With additional assumptions, however, Gromov-Hausdorff convergence can imply stronger convergence. For instance, Cheeger and Naber [5] proved that a sequence of manifolds with Ricci curvature uniformly bounded and local volume noncollapsing converges smoothly outside a singular set of real codimension at least 4.

The local volume noncollapsing assumption does not hold in our case, and we will see that if we rescale to a constant diameter, our spaces converge to a real interval. The usefulness of Gromov-Hausdorff convergence for our purposes is in allowing us to describe the limiting geometry of different parts of the neck region we are constructing. We will see that after an appropriate rescaling, some portions of the neck region collapse to lower-dimensional spaces. The notion of Gromov-Hausdorff convergence allows us to state the sense in which these lower-dimensional spaces occur as limits. Subsequent analysis will require passing to local universal covers to "un-collapse" these spaces and achieve $C^{k, \alpha}$ convergence.
5.1.2. Hölder regularity scales. It is often useful to discuss convergence of the derivatives of a sequence of metrics. For this purpose we measure the Hölder norms of these metrics in local coordinates. If we were to naively allow any choice of charts, however, we could "zoom in" to normal neighborhoods around each point and every smooth metric would look like the Euclidean metric. Therefore we must control the radius of the chart and the extent of magnification in our definition of the Hölder norm.

Definition 5.2. Let $(M, g)$ be a Riemannian manifold, $p \in M$ a distinguished point, and $r>0$. For any $k \in \mathbb{Z}_{\geq 0}$ and $\alpha \in(0,1),\|(M, g, p)\|_{C^{k, \alpha}, r}$ is defined as the supremum over constants $Q$ such that there exists a $C^{k+1, \alpha}$ chart $\phi:\left(B_{r}(0), 0\right) \subset$ $\mathbb{R}^{n} \rightarrow(U, p) \subset M$ satisfying the following conditions:
\begin{itemize}
\item[(1)] $|D \phi| \leq e^{Q}$ on $B_{r}(0)$ and $\left|D \phi^{-1}\right| \leq e^{Q}$ on $U$.
\item[(2)] For all multi-indices $I$ such that $|I| \leq k$,
$$r^{|I|+\alpha}\left\|\partial^{I} g_{l m}\right\|_{C^{0, \alpha}\left(B_{r}(0)\right)} \leq Q .$$
\end{itemize}
Then globally
$$\|(M, g)\|_{C^{k, \alpha}, r}=\sup _{p \in M}\|(M, g, p)\|_{C^{k, \alpha}, r} .$$

The Hölder norm computes the largest constant for which the metric can be controlled at a fixed scale $r$. Conversely, we can ask for the largest scale at which a fixed constant $Q$ controls the metric. This gives rise to the notion of a local regularity scale.

Definition 5.3. Fix $\epsilon>0$ and $r>0$. We say that a Riemannian manifold $(M, g)$ is $(r, k+\alpha, \epsilon)$-regular at $p \in M$ if $g$ is $C^{k, \alpha}$-regular on $B_{2 r}(p)$ and
$$\|(M, g, p)\|_{C^{k, \alpha}, r} \leq \epsilon .$$
We define the $C^{k, \alpha}$-regularity scale of $(M, g)$ at $p$ to be the supremum over the set of $r$ for which $(M, g)$ is $(r, k+\alpha, \epsilon)$-regular at $p$.

Intuitevely, the $C^{k, \alpha} \epsilon$-regularity scale at $p$ is the scale on which the $C^{k, \alpha}$ geometry of $M$ is " $\epsilon$-interesting." Thus it provides a choice of resolution that is in a sense uniform throughout $M$.
5.1.3. Hölder convergence and Einstein regularity. The $C^{k, \alpha}, r$ norm defined in Section 5.1.3 is useful for deriving compactness results but cannot be used to measure the distance between two metrics. For this purpose, we make use of the $C^{k, \alpha}$ topology on compact Riemannian manifolds. Instead of defining the norm locally, we use the Riemannian distance function to compute the denominator in the Hölder seminorms. Then we say that $\left(M_{i}, g_{i}, p_{i}\right) \rightarrow(M, g, p)$ in the pointed $C^{k, \alpha}$ topology if there exists a compact exhaustion $U_{j}$ of $M$ and a collection $F_{j, i}: U_{j} \rightarrow M_{i}$ of diffeomorphisms mapping $p$ to $p_{i}$ such that $F_{j, i}^{*} g_{i} \rightarrow g$ in the $C^{k, \alpha}$ topology on $U_{j}$.

Our use of the implicit function theorem to correct $\left(\mathcal{M}, \omega_{T}\right)$ to a Kähler-Einstein metric will only give $C^{0, \alpha}$ convergence. Happily, the following result of Anderson and Colding gives higher regularity without any additional work.

Theorem 5.4. [1, 4]Let $\left(M_{i}, g_{i}\right)_{i \in \mathbb{Z}}$ and $(M, g)$ be compact $n$-dimensional Riemannian manifolds such that Ric $g_{i}=\lambda_{i} g_{i}$ for $\left|\lambda_{i}\right| \leq n-1$. If $\left(M_{i}, g_{i}\right) \rightarrow(M, g)$ in the Gromov-Hausdorff topology, then $\left(M_{i}, g_{i}\right) \rightarrow(M, g)$ in $C^{k, \alpha}$ for any $k$ and $\alpha \in(0,1)$.
5.1.4. Regularity on local universal covers. We will see that Definition 5.3 and the notion of $C^{k, \alpha}$ convergence in Section 5.1.3 are too demanding for our family of spaces $\left(\mathcal{M}, \omega_{T}\right)$. This is because as $T \rightarrow \infty$, the size of the $S^{1}$ fiber, given by $h^{-1}$, collapses near the singular point, so charts in this region must be correspondingly small. However, the curvature is still uniformly bounded, and if we unroll the $S^{1}$ fiber by taking the universal cover in a neighborhood of a point that does not contain $p$, we will find that the regularity scale is bounded from below. Using this observation, we generalize the idea of $C^{k, \alpha}$ convergence. These definitions follow [19] 4.3.

Definition 5.5. Let $\left(M_{i}, g_{i}\right)$ be a sequence of Riemmanian manifolds of dimension $n$. For each $i$, a local universal cover of $\left(M_{i}, g_{i}\right)$ is the Riemannian universal cover $\left(\widetilde{B}_{r}\left(x_{i}\right), \tilde{g}_{i}\right)$ of $B_{r}\left(x_{i}\right) \subset M_{i}$ for any $x_{i} \in M_{i}$ and $r>0$. If $\left(M_{i}, g_{i}\right)$ converges in the Gromov-Hausdorff topology to $(M, g)$ a manifold such that $\operatorname{dim} M=n-1$, we say that $\left(M_{i}, g_{i}\right)$ converges to $\left(M \times \mathbb{R}, g \times g_{\mathbb{R}}\right)$ in $C^{k, \alpha}$ on local universal covers if whenever $x_{i} \rightarrow x \in M$, there exists $r>0$ such that $\widetilde{B}_{r}\left(x_{j}\right) \rightarrow B_{r}(x) \times \mathbb{R}$ in $C^{k, \alpha}$.

We can also update Definition 5.3 (see [19] Definition 4.22).
Definition 5.6. Fix $\epsilon>0$ and $r>0$. We say that a Riemannian manifold $(M, g)$ is $(r, k+\alpha, \epsilon)$-regular in the sense of universal covers at $p \in M$ if $g$ is $C^{k, \alpha}$-regular on $B_{2 r}(p)$ and
$$\left\|\left(\tilde{B}_{2 r}(\tilde{p}), \tilde{g}, \tilde{p}\right)\right\|_{C^{k, \alpha}, r} \leq \epsilon,$$
where $\left(\tilde{B}_{2 r}(\tilde{p}), \tilde{g}\right)$ is the Riemannian universal cover of $B_{2 r}(p)$ and $\tilde{p}$ is a preimage of $p$. We define the $C^{k, \alpha}$-regularity scale in the sense of universal covers of $(M, g)$ at $p$ to be the supremum over the set of $r$ for which $(M, g)$ is $(r, k+\alpha, \epsilon)$-regular in the sense of universal covers at $p$.

For the remainder of this paper, when we discuss regularity scales, we mean "in the sense of universal covers." However, when discussing convergence we will be explicit about whether we are referring to local universal covers or not.
5.2. Spaces of functions on $\left(\mathcal{M}, \omega_{T}\right)$. We return to our goal of perturbing $\left(\mathcal{M}, \omega_{T}\right)$ to an exact solution for large enough $T$. To achieve this, we must first prove a certain weighted Schauder estimate that is uniform in $T$. While in the previous section we discussed Hölder norms on families of manifolds, in this section we define Hölder spaces of functions on such families. The estimates we derive will establish the boundedness of the inverse in our use of the inverse function theorem in Section 6.

The global metric behavior of $\left(\mathcal{M}, g_{T}\right)$ as $T \rightarrow \infty$ is not simple to describe. However, we will only need to understand the geometry near a sequence of points $\left(x_{j}\right)$ where $x_{j} \in\left(\mathcal{M}, g_{T_{j}}\right)$ for some sequence $T_{j} \rightarrow \infty$. We will see that after passing to a subsequence and rescaling, a sequence of neighborhoods of these points converges in the Gromov-Hausdorff sense to one of four model spaces. Further, we can achieve $C^{2, \alpha}$ convergence by passing to the local universal cover. Therefore we will see that the existence of a weighted Schauder estimate on $\left(\mathcal{M}, g_{T}\right)$ reduces to a collection of statements about these model spaces.

To state the desired Schauder estimate, we must first define the weight function $\rho_{\delta, \nu, \mu}^{(k+\alpha)}: \mathcal{M} \rightarrow \mathbb{R}_{>0}$. In what follows, the functions $W$ and $\rho_{\delta, \nu, \mu}^{(k+\alpha)}$ depend on $T$, but we suppress this dependence for (relative) ease of notation. Pick $C_{3}>0$ such that $r_{w}$ is defined up to $C_{3}$ for all $T$ and let $W$ be a smooth and "reasonable" function such that
$$W(q, T)= \begin{cases}T^{-1} & r_{w} \leq T^{-1} \\ r_{w}(q) & 2 T^{-1} \leq r_{w} \leq \frac{C_{3}}{2} \\ 1 & r_{w} \geq C_{3} \text { or } r_{w} \text { is undefined. }\end{cases}$$
The significance of $W$ is that we will need to rescale $g_{T}$ by $W(q, T)$ to see nontrivial Gromov-Hausdorff convergence in a neighborhood of $q$.

Now for $k \in\{0,1,2\}$ define
$$\rho_{\delta, \nu, \mu}^{(k+\alpha)}(q)=(1+w(q))^{-\delta} W(q, T)^{\nu+k+\alpha} T^{\mu} .$$
The factor of $W(q, T)^{k+\alpha}$ will ensure that the weight function is compatible with differentiation in the proof of Proposition 5.10. The factor of $W(q, T)^{\nu}$ controls the behavior of functions at infinity from the vantage point of the singular point $p$. The factor of $(1+w(q))^{-\delta}$ controls the behavior of functions at infinity from the vantage point of the two boundary components. Finally, if $\mu$ is large enough then the factor of $T^{\mu}$ ensures that $\rho_{\delta, \nu+2, \mu}^{(0)}$ is bounded below, allowing us to take powers within the weighted Hölder space.

For carefully chosen parameters, $\rho_{\delta, \nu, \mu}^{(k+\alpha)}$ will give us an appropriate weight function to define weighted Hölder spaces on $\left(\mathcal{M}, g_{T}\right)$. As in Section 5.1.4, our definition of these Hölder spaces differs from the standard theory in that distances are measured on local universal covers.

Definition 5.7. Fix $T>0$. Let $K \subset \mathcal{M}$ be a compact subset and $\chi \in T^{r, s}(K)$ an $(r, s)$-tensor field. Let a tilde denote the lift of an object to the Riemannian universal cover of $B_{W(x, T)}(x)$. The weighted $C^{k, \alpha}$ seminorm is defined by
$$[\chi]_{C_{\delta, \nu, \mu}^{k, \alpha}(x)}=\sup _{\tilde{y} \in B_{W(x, T)}(\tilde{x})} \rho_{\delta, \nu, \mu}^{(k+\alpha)}(x) \frac{\left|\nabla^{k} \tilde{\chi}(\tilde{x})-\nabla^{k} \tilde{\chi}(\tilde{y})\right|}{\tilde{d}(\tilde{x}, \tilde{y})^{\alpha}} .$$

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/d4154eb1-3a30-4a5c-835a-c3559a1012ab-29.jpg?height=875&width=1419&top_left_y=288&top_left_x=322}
\captionsetup{labelformat=empty}
\caption{Figure 4. The weight function $\rho_{\delta, \nu, \mu}^{(2)}$ as a function of $z$ along two cross sections $(p, t) \in D \times I$ for $t \in(-1,0)$. In the first case, the cross section goes through the singular point $\left(p_{D}, 0\right)$, while in the second case, it takes the form $\{(q, t), t \in(-1,0)\}$ for some point $q \in D$ such that $r_{w}((q, 0))>C_{3}$. Parameters are chosen in accordance with Theorem 5.8, and in addition we are assuming that $\nu+2<\delta$, though the opposite may be true.}
\end{figure}
and
$$[\chi]_{C_{\delta, \nu, \mu}^{k, \alpha}(K)}=\sup _{x \in K}[\chi]_{C_{\delta, \nu, \mu}^{k, \alpha}(\mathcal{M})}(x) .$$
The difference $\left|\nabla^{k} \tilde{\chi}(\tilde{x})-\nabla^{k} \tilde{\chi}(\tilde{y})\right|$ is computed by parallel transporting $\nabla^{k} \tilde{\chi}(\tilde{y})$ to $\tilde{x}$. We also write
$$[\chi]_{C_{\delta, \nu, \mu}^{k}(K)}=\sup _{x \in K}[\chi]_{C_{\delta, \nu, \mu}^{k}(x)}=\sup _{x \in K}\left|\rho_{\delta, \nu, \mu}^{(k)} \nabla^{k} \chi\right| .$$
The weighted $C^{k, \alpha}$ norm of $\chi$ is then constructed from the seminorm in the usual way:
$$\|\chi\|_{C_{\delta, \nu, \mu}^{k, \alpha}(K)}=\sum_{m=0}^{k}[\chi]_{C_{\delta, \nu, \mu}^{m}(K)}+[\chi]_{C_{\delta, \nu, \mu}^{k, \alpha}(K)} .$$

We can now state the main theorem of this section.
Theorem 5.8. For each $T$, define the operator
$$\mathcal{L}_{T}=\Delta_{g_{T}}-1 .$$
There exists $\delta_{0}>0$ such that for all $\alpha \in(0,1)$, if $\nu \in(-2,-3 / 2), \delta \in\left(0, \delta_{0}\right)$, and $\mu \in(\max (\delta, \nu+2), 1)$, there exists $C>0$ such that for large enough $T$,
$$[u]_{C_{\delta, \nu, \mu}^{2, \alpha}(\mathcal{M})}+[u]_{C_{\delta, \nu, \mu}^{2}(\mathcal{M})}+\|u\|_{C_{\delta, \nu+2, \mu}^{0, \alpha}(\mathcal{M})} \leq C\left\|\mathcal{L}_{T} u\right\|_{C_{\delta, \nu+2, \mu}^{0, \alpha}(\mathcal{M})}$$
for all $u \in C^{2, \alpha}(\mathcal{M})$ such that $\left.\frac{\partial u}{\partial n}\right|_{\partial \mathcal{M}}=0$.

The operator $\mathcal{L}_{T}$ will arise in Section 6 as the linearization of a functional whose zeros are negative Kähler-Einstein metrics.
5.3. Local rescaled geometries. The key ingredient in the proof of Theorem 5.8 is the following characterization of the rescaled geometry of the model spaces $\left(\mathcal{M}, g_{T}\right)$.

Proposition 5.9. Let $\left(T_{j}\right)_{j=1}^{\infty}$ be a sequence of positive real numbers tending to infinity. If $\left(x_{j}\right)_{j=1}^{\infty}$ is a sequence of points with $x_{j} \in \mathcal{M}$, then there exists a subsequence (which we also call $j$ ) such that as $j \rightarrow \infty,\left(\mathcal{M}, W\left(x_{j}, T_{j}\right)^{-2} g_{T_{j}}, x_{j}\right)$ converges in the pointed Gromov-Hausdorff topology to one of the following spaces:
\begin{itemize}
\item[(1)] the Taub-NUT space $\mathbb{C}_{T N}^{2}$,
\item[(2)] the Riemannian product $\mathbb{C} \times \mathbb{R}$,
\item[(3)] the Riemannian cylinder $D \times \mathbb{R}$,
\item[(4)] the Calabi model space $\left(\mathcal{C}_{ \pm}, g_{\mathcal{C}_{ \pm}}\right)$.
\end{itemize}

In case 1, convergence is in the pointed $C^{2, \alpha}$ topology. In cases 2 and 3, convergence is in $C^{k, \alpha}$ on local universal covers away from $p$ for $k \geq 0$. In case 4, convergence is in the pointed $C^{k, \alpha}$ topology for $k \geq 0$.

Proof. Let $W_{j}=W\left(x_{j}, T_{j}\right)$ and define $r_{w}$ as in Section 3.3. We will also write $r_{w}$ for the pullback of $r_{w}$ by $\pi: \mathcal{M} \rightarrow D \times[-1,1 / 2]$. In addition, let $\hat{g}_{j}=W_{j}^{-2} g_{T_{j}}$ denote the rescaled metric and $\hat{B}_{R}(x)=B_{W_{j} R}(x)$ denote the $R$-ball around a point $x \in \mathcal{M}$ with respect to the rescaled metric.

We consider four possible behaviors of $\left(x_{j}\right)_{j=1}^{\infty}$ such that there must exist a subsequence falling into at least one of these categories.

Case 1. $\operatorname{Tr}_{w}\left(x_{j}\right) \rightarrow C<\infty$. Using the coordinates defined in Section 3.3 and writing $\omega_{\mathbb{C}}=\frac{i}{2} d y \wedge d \bar{y}$, we have by Equation 3.27 and the discussion in Section 4.3 that
$$\begin{aligned}
\omega_{T} & =\pi^{*} \chi \omega_{D}+d z \wedge \Theta \\
& =\pi^{*} \omega_{D}+\left(\frac{1}{2 T r_{w}}+\frac{1}{T}\left(g^{2, \alpha}+w^{1}\right)\right) \pi^{*} \omega_{\mathbb{C}}+\frac{1}{T} d w \wedge \Theta \\
& =\pi^{*} \omega_{D}+\left(\frac{1}{2 T r_{w}}+\frac{1}{T}\left(g^{2, \alpha}+w^{1}\right)\right) \pi^{*} \omega_{\mathbb{C}}+\frac{1}{T} d w \wedge\left(\Theta_{0}+\theta\right)
\end{aligned}$$
Meanwhile, since the projection $\pi: \mathcal{M} \rightarrow D \times[-1,1 / 2]$ is modelled on the Hopf fibration, we have by Equation 4.2 that
$$\frac{1}{T} \omega_{T N, T}=\left(\frac{1}{2 T r_{w}}+1\right) \pi^{*} \omega_{\mathbb{C}}+\frac{1}{T} d w \wedge \Theta_{0}$$
where $\omega_{T N, T}$ is the Taub-NUT metric in the complex-valued coordinates $u_{1}, u_{2}$ defined in Section 4.3 and with parameter $T$. Thus
$$\omega_{T}-\frac{1}{T} \omega_{T N, T}=\pi^{*}\left(\omega_{D}-\omega_{\mathbb{C}}\right)+\frac{1}{T}\left(g^{2, \alpha}+w^{1}\right) \pi^{*} \omega_{\mathbb{C}}+\frac{1}{T} d w \wedge \theta .$$

Now change coordinates such that $\underline{u}_{i}=\frac{1}{\sqrt{T} W} u_{i}, \underline{y}=\frac{1}{T W^{2}} y$, and $\underline{w}=\frac{1}{T W^{2}} w$. Then we let $\underline{s}^{2}=\frac{1}{T W^{2}} s^{2}=\left|\underline{u}_{1}\right|^{2}+\left|\underline{u}_{2}\right|^{2}$. By Equation 4.4, we have
$$\omega_{T N, T}=T W^{2} \underline{\omega}_{T N, T^{2} W^{2}} .$$

In addition, noting that $\pi^{*} d \underline{y}=\underline{u}_{1} d \underline{u}_{2}+\underline{u}_{2} d \underline{u}_{1}=\mathcal{O}(\underline{s})$ with respect to the flat metric on $\mathbb{C}_{\underline{u}_{1}, \underline{u}_{2}}^{2}$, we have that
$$\begin{aligned}
\pi^{*}\left(\omega_{D}-\omega_{\mathbb{C}}\right) & =\mathcal{O}\left(r_{w}^{2}\right) \pi^{*}(d y \wedge d \bar{y}) \\
& =\left(T W^{2}\right)^{4} \mathcal{O}\left(\underline{s}^{6}\right)
\end{aligned}$$
Similarly
$$\left(g^{2, \alpha}+w^{1}\right) \pi^{*} \omega_{\mathbb{C}}=\left(T W^{2}\right)^{2} \underline{g}^{2, \alpha} .$$
Therefore
$$\left\|W^{-2} \omega_{T}-\underline{\omega}_{T N, T^{2} W^{2}}\right\|_{C^{2, \alpha}}=\mathcal{O}\left(T^{-1}\right)$$
in $\mathbb{C}_{\underline{u_{1}}, \underline{u_{2}}}^{2}$ on any region where $\underline{s}$ is bounded. Since $\underline{s}$ is bounded on a ball of $\left(W_{j}^{-2} g_{T_{j}}\right)$ -radius $R$ around $x_{j}$ for any $R>0$, this gives pointed $C^{2, \alpha}$ convergence.

Case 2. $\operatorname{Tr}_{w}\left(x_{j}\right) \rightarrow \infty, r_{w}\left(x_{j}\right) \rightarrow 0$. Note that
$$g_{T}=\pi^{*} \tilde{g}+h_{T} d z^{2}+h_{T}^{-1} \Theta^{2},$$
is the Riemannian metric corresponding to $\omega_{T}$, where $\tilde{g}$ is the Riemannian metric corresponding to $\tilde{\omega}$. By Equation 5.1, $W_{j}=r_{w}\left(x_{j}\right)$ for sufficiently large $j$, so we study the regularity of $\hat{g}_{j}=r_{w}\left(x_{j}\right)^{-2} g_{T_{j}}$.

Integrating $h$ along $w$ shows that for any $q \in \mathcal{M}$,
$$\left|\operatorname{ArcSinh}\left(w\left(x_{j}\right)\right)-\operatorname{ArcSinh}(w(q))\right| \leq d_{g_{T_{j}}}\left(x_{j}, q\right)+\mathcal{O}\left(T^{-1 / 2}\right) .$$
Now take $q \in \hat{B}_{R}\left(x_{j}\right)=B_{r_{w}\left(x_{j}\right) R}\left(x_{j}\right)$. Since $w\left(x_{j}\right) \rightarrow 0$ and $d_{g_{T_{j}}}\left(x_{j}, q\right) \rightarrow 0, w(q)$ can be assumed arbitrarily small. This lower-bounds the derivative of ArcSinh, allowing us to conclude that
$$\left|w(q)-w\left(x_{j}\right)\right| \leq 2 r_{w}\left(x_{j}\right) R$$
for large enough $j$. Thus if for each $j$ we make the change of coordinates $\underline{w}=$ $r_{w}\left(x_{j}\right)^{-1} w, \underline{y}=r_{w}\left(x_{j}\right)^{-1} y$, and $\underline{u}_{i}=r_{w}\left(x_{j}\right)^{-1 / 2} u_{i}$, we have that $\underline{w}\left(x_{j}\right) \leq 1$ and $\left|\underline{w}(q)-\underline{w}\left(x_{j}\right)\right| \leq 2 R$.

Now assume $R>1$ and $q \in \hat{B}_{R}\left(x_{j}\right) \backslash \hat{B}_{\epsilon^{\prime}}(p)$ for some small $\epsilon^{\prime}>0$. Thus $r_{w}(q) \geq$ $C \epsilon^{\prime} r_{w}\left(x_{j}\right)$. By Equation 3.26,
$$h_{T}=\frac{T^{2}}{r_{w}\left(x_{j}\right)^{2} \underline{w}^{2}+1}+\frac{T}{2 r_{w}}+T\left(g^{2, \alpha}+w^{1}\right)$$
Thus
$$r_{w}\left(x_{j}\right)^{-2} h_{T} d z^{2}=\left(\frac{1}{r_{w}\left(x_{j}\right)^{2} \underline{w}^{2}+1}+\mathcal{O}\left(\left(T r_{w}\left(x_{j}\right)\right)^{-1}\right)\right) d \underline{w}^{2}$$
and so
$$\left|\pi^{*}\left(r_{w}\left(x_{j}\right)^{-2} h_{T} d z^{2}-d \underline{w}^{2}\right)\right| \rightarrow 0$$
pointwise uniformly on the annulus with respect to $\mathbb{C}_{\underline{u}_{1}, \underline{u}_{2}}^{2}$.
By analogous arguments, the growth of $h_{T}$ implies that
$$\left|r_{w}\left(x_{j}\right)^{-2} h_{T}^{-1} \Theta^{2}\right| \rightarrow 0,$$
with convergence as described in the previous paragraph. To analyze the $\tilde{g}$ term, we observe that by Equation 3.27,
$$r_{w}\left(x_{j}\right)^{-2} \pi^{*} \tilde{g}=\left(1+\frac{1}{2 T r_{w}}+T^{-1} \mathcal{O}(1)\right) \frac{i}{2} d \underline{y} \wedge d \underline{\bar{y}}=\frac{i}{2} d \underline{y} \wedge d \underline{\bar{y}}+\mathcal{O}\left(\left(T r_{w}\right)^{-1}\right) .$$

In summary,
$$\hat{g}_{T} \rightarrow \frac{i}{2} d \underline{y} \wedge d \underline{\bar{y}}+d \underline{w}^{2}=\pi^{*} g_{\mathbb{C}_{\underline{y}} \times \mathbb{R}}$$
on $\hat{B}_{R}\left(x_{j}\right) \backslash \hat{B}_{\epsilon^{\prime}}\left(x_{j}\right)$. A diagonal argument in $j$ and $\epsilon^{\prime}$ therefore gives Gromov-Hausdorff convergence $\hat{B}_{R}\left(x_{j}\right) \rightarrow B_{R}\left(x_{\infty}\right) \subset \mathbb{R}^{3}$.

Now pass to a local universal cover $\tilde{\hat{B}}_{\epsilon}(q)$ for $q \in \hat{B}_{R}\left(x_{j}\right) \backslash \hat{B}_{\epsilon^{\prime}}(p)$ and assume that $\hat{B}_{\epsilon}(q) \subset\left(\hat{B}_{\epsilon^{\prime}}(p)\right)^{c}$. If we choose a coordinate such that $\Theta=d t$, then locally
$$\tilde{\hat{B}}_{\epsilon}(q) \simeq U \times \mathbb{R}_{t}$$
for some $U \subseteq \mathbb{D} \times[-1,1 / 2]$. Since $T^{-2} h_{T} \rightarrow 1$, we can rescale the $t$ coordinate to $\underline{t}$ so that on the local universal cover
$$\hat{g}_{T} \rightarrow \pi^{*} g_{\mathbb{R}}^{3}+d \underline{t}^{2}$$
in $C^{\infty}$, since all terms are smooth away from $p$.
Case 3. $r_{w}\left(x_{j}\right) \nrightarrow 0, w\left(x_{j}\right) \nrightarrow \infty$. Assume that the limit of $r_{w}$ is such that $W_{j}=1$ and $\hat{g}_{j}=g_{T_{j}}$ for large enough $j$. Passing to a subsequence, we can assume that $w\left(x_{j}\right) \rightarrow w_{\infty}<\infty$ and $d\left(x_{j}, p\right) \rightarrow d_{\infty}<\infty$, since the diameter of $\tilde{\omega}(z)$ and the $S^{1}$ fiber are bounded.

Now fix $R>1$ and consider the domain $\hat{B}_{R}\left(x_{j}\right) \backslash \hat{B}_{\epsilon^{\prime}}(p)$ for some small $\epsilon^{\prime}$. As above, for any $q \in \hat{B}_{R}\left(x_{j}\right) \backslash \hat{B}_{\epsilon^{\prime}}(p)$ we can pass to a local universal cover $\tilde{\hat{B}}_{\epsilon}(q) \simeq U \times \mathbb{R}_{t}$ with coordinates $y, \bar{y}, w$ on $U$ and $d t=\Theta$. We analyze the metric on the universal cover as in the previous bullet, except there is no need to rescale by $W_{j}$.

Since we may assume $\hat{B}_{\epsilon}(q) \subset\left(\hat{B}_{\epsilon^{\prime}}(p)\right)^{c}, r_{w}$ is bounded below on $\tilde{\hat{B}}_{\epsilon}(q)$. Thus we have by Equation 3.27 and Proposition 3.6 that
$$\pi^{*} \tilde{g} \rightarrow \pi^{*} g_{D} .$$
in $C^{2, \alpha}$ in these coordinates. Similarly, by the discussion in Section 3.2.
$$h_{T} \rightarrow T^{2}\left(\frac{1}{w^{2}+1}+\mathcal{O}\left(T^{-1}\right)\right) .$$
Thus by a rescaling of $t$,
$$\hat{g}_{T} \rightarrow \pi^{*} g_{D}+\frac{1}{w^{2}+1} d w^{2}+\left(w^{2}+1\right) d t^{2}$$
in $C^{\infty}$ on the local universal cover. Meanwhile, since $h_{T}^{-1} \rightarrow 0$, this gives Gromov-Hausdroff convergence to $D \times \mathbb{R}$.

Case 4. $w\left(x_{j}\right) \rightarrow \infty$. In this case we must have that $z\left(x_{j}\right) \rightarrow z_{\infty} \in[-1,1 / 2]$, and again we have $\hat{g}_{j}=g_{T_{j}}$. Fix $R>0$ and take $q \in \hat{B}_{R}\left(x_{j}\right)$. Then
$$d\left(q, x_{j}\right) \sim\left|\operatorname{ArcSinh}(w(q))-\operatorname{ArcSinh}\left(w\left(x_{j}\right)\right)\right| \sim\left|\log (w(q))-\log \left(w\left(x_{j}\right)\right)\right|,$$
so
$$\inf _{q \in \hat{B}_{R}\left(x_{j}\right)} r_{w}(q) \rightarrow \infty$$
as $j \rightarrow \infty$.

First assume that $z_{\infty}=0$ and define $\underline{w}=\frac{w(q)}{w\left(x_{j}\right)}$. Then by the discussion in Section 3.2
$$h(q) d z^{2}=\left(\frac{k_{ \pm} z\left(x_{j}\right) \underline{w}(q)+1}{\frac{2}{3} k_{ \pm}\left(z\left(x_{j}\right) \underline{w}(q)\right)^{3}+\left(z\left(x_{j}\right) \underline{w}(q)\right)^{2}+T^{-2}}\right) z\left(x_{j}\right)^{2} d \underline{w}^{2} \rightarrow \frac{1}{\underline{w}^{2}} d \underline{w}^{2} .$$
By arguments similar to the previos section, the metric collapses to $D \times \mathbb{R}$, while
$$\hat{g}_{T} \rightarrow \pi^{*} g_{D}+\frac{1}{\underline{w}^{2}} d \underline{w}^{2}+\underline{w}^{2} d t^{2}$$
in $C^{\infty}$ on the local universal cover.
Now assume $z_{\infty}>0$. Take $q \in \hat{B}_{R}\left(x_{j}\right)$ with coordinates $y, \bar{y}, z$ and $t$ as above. As previously the discussion in Section 3.2 gives that for $z<0$,
$$h=\frac{k_{-} z+1}{\frac{2}{3} k_{-} z^{3}+z^{2}+T^{-2}}+\mathcal{O}\left(T^{-5} z^{-4}\right) .$$
Meanwhile, Remark 3.8 gives that
$$\delta \chi=\mathcal{O}\left(T^{-1}\right), \quad|w|=C_{2} .$$
Using Equations 2.11 and 3.20 to integrate $\delta \chi$ outside of this region, we find that
$$\chi=1+k_{ \pm} z+\mathcal{O}\left(T^{-1}\right) .$$
Thus
$$\hat{g}_{T} \rightarrow\left(1+k_{-} z\right) \pi^{*} g_{D}+\frac{k_{-} z+1}{\frac{2}{3} k_{-} z^{3}+z^{2}} d z^{2}+\frac{\frac{2}{3} k_{-} z^{3}+z^{2}}{k_{-} z+1} \Theta^{2},$$
in $C^{\infty}$, and this metric is recognized to be the Calabi model space metric described in Section 4.1.2 for $n=k_{-}$. The discussion is similar for $z>0$.

Note that the distance from $x_{j}$ to $\partial M$ is finite if $\left|z_{\infty}\right|>0$, since
$$\lim _{j \rightarrow \infty}\left(\operatorname{ArcSinh}\left(T_{j}\right)-\operatorname{ArcSinh}\left(w\left(x_{j}\right)\right)\right)=-\lim _{j \rightarrow \infty} \log \left(T_{j}^{-1} w\left(x_{j}\right)\right) .$$
Thus in this case a sufficiently large definite ball around $x_{\infty}$ will contain a portion of the boundary. \(\square\)
5.4. Schauder estimates on $\left(\mathcal{M}, \omega_{T}\right)$. The usefulness of Proposition 5.9 will become apparent in the proofs of Propositions 5.10 and 5.8. In the first proof, we will see that the proposition gives a lower bound on the regularity scale of $\left(\mathcal{M}, \omega_{T}\right)$, directly implying a local Schauder estimate. In the second proof, we will assume that a global Schauder estimate fails to hold and take a sequence of functions violating the estimate. After passing to a rescaled limit, the sequence will converge to a function whose behavior contradicts the properties of the spaces described in Proposition 5.9.

Proposition 5.10 is modeled on [19] Proposition 4.37.
Proposition 5.10. (Local weighted Schauder estimate). For $T \gg 0$ and $\left(\mathcal{M}, g_{T}\right)$ as constructed in Section 4, the following estimates hold:
\begin{itemize}
\item[(1)] (Interior estimate) For all $\alpha \in(0,1)$, there exists $C_{\alpha}>0$ such that for all $x \in \mathcal{M}^{o}, r \in\left(0, \frac{1}{8}\right]$, and $u \in C^{2, \alpha}\left(B_{2 r W(x)}(x)\right)$,
$$r^{2+\alpha}\|u\|_{C_{\delta, \nu, \mu}^{2, \alpha}\left(B_{r W(x)}(x)\right)} \leq C_{\alpha}\left(\left\|\mathcal{L}_{T} u\right\|_{C_{\delta, \nu+2, \mu}^{0, \alpha}\left(B_{2 r W(x)}(x)\right)}+\|u\|_{C_{\delta, \nu, \mu}^{0}\left(B_{2 r W(x)}(x)\right)}\right) .$$
\end{itemize}
\begin{itemize}
\item[(2)] (Boundary estimate) For all $\alpha \in(0,1)$, there exists $C_{\alpha}>0$ such that for all $x \in \partial \mathcal{M}, r \in\left(0, \frac{1}{8}\right]$, and $u \in C^{2, \alpha}\left(B_{2 r W(x)}(x)\right)$,
$$\begin{aligned}
r^{2+\alpha}\|u\|_{C_{\delta, \mu, \mu}^{2, \alpha}\left(B_{r W(x)}(x)\right)} \leq C_{\alpha} & \left(\left\|\mathcal{L}_{T} u\right\|_{C_{\delta, \nu+2, \mu}^{0, \alpha}\left(B_{2 r W(x)}(x)\right)}\right. \\
& \left.\quad+\|u\|_{C_{\delta, \mu, \mu}^{0}\left(B_{2 r W(x)}(x)\right)}+\left\|\frac{\partial u}{\partial n}\right\|_{C_{\delta, \nu+1, \mu}^{1, \alpha}\left(B_{2 r W(x)}(x)\right)}\right) .
\end{aligned}$$
Proof. Fix some small $\epsilon^{\prime}>0$. We observe that Proposition 5.9 demonstrates that the $C^{2, \alpha}, \epsilon^{\prime}$-regularity scale $r_{2, \alpha}(x)$ of $\left(\mathcal{M}, g_{T}\right)$ with respect to $\epsilon^{\prime}$ at $x$ is bounded below by a multiple of $W\left(x, T_{j}\right)$ :
$$r_{2, \alpha}(x) \geq C W\left(x, T_{j}\right) .$$
For arguing by contradiction, this is equivalent to saying that for any sequence $\left(x_{j}, T_{j}\right)_{j=1}^{\infty}$, the $C^{2, \alpha}$-regularity scale of $\left(\mathcal{M}, W\left(x_{j}, T_{j}\right)^{-2} g_{T}\right)$ is bounded below by a constant, not necessarily uniform across sequences, at $x_{j}$. This follows because $\left(\mathcal{M}, W\left(x_{j}, T_{j}\right)^{-2} g_{T}, x_{j}\right)$ converges to one of the four spaces in the proposition in $C^{2, \alpha}$ on the local universal cover.
Equation 5.11 allows us to apply the local Schauder estimates on Euclidean balls with respect to the metric $\hat{g}_{T}$. On any such ball $B=\hat{B}_{r}(x)$ with $2 B=\hat{B}_{2 r}(x)$,
$$\|u\|_{C^{2, \alpha}(B)} \leq C\left(\left\|\left(\Delta_{\hat{g}}-W^{2}\right) u\right\|_{C^{0, \alpha}(2 B)}+\|u\|_{C^{0}(2 B)}\right)$$
for $C$ uniform in $T$ because $W(x)$ is uniformly bounded above by 1 . Now we will demonstrate in the proof of Theorem 5.8 that for any fixed $r, \rho_{\delta, \nu, \mu}^{(0)}$ is equivalent to a constant on $B_{r W(x)}(x)=\hat{B}_{r}(x)$ uniformly in $x \in \mathcal{M}$ and $T \gg 0$. Therefore, multiplying through by $\rho_{\delta, \nu, \mu}^{(0)}(x)$ and rescaling $\hat{g}_{T} \rightarrow g_{T}$ yields that
$$\|u\|_{C_{\delta, \nu, \mu}^{2, \alpha}(B)} \leq C\left(\left\|\mathcal{L}_{T} u\right\|_{C_{\delta, \nu+2, \mu}^{0, \alpha}(2 B)}+\|u\|_{C_{\delta, \nu, \mu}^{0}(2 B)}\right) .$$
The proof of the boundary estimate is similar. \(\square\)
A global version of Proposition 5.10 follows from the local version and a covering argument.
Proposition 5.11. Let $\nu, \alpha$, and $\delta$ be parameters satisfying the conditions described in Theorem 5.8. Then there exists $C>0$ such that for all sufficiently large $T$ and $u \in C_{\delta, \nu, \mu}^{2, \alpha}(\mathcal{M})$,
$$\|u\|_{C_{\delta, \nu, \mu}^{2, \alpha}(\mathcal{M})} \leq C\left(\left\|\mathcal{L}_{T} u\right\|_{C_{\delta, \nu+2, \mu}^{0, \alpha}(\mathcal{M})}+\left\|\frac{\partial u}{\partial n}\right\|_{C_{\delta, \nu+1, \mu}^{1, \alpha}(\partial \mathcal{M})}+\|u\|_{C_{\delta, \nu, \mu}^{0}(\mathcal{M})}\right) .$$
We can now give the proof of Theorem 5.8.
Proof. (Theorem 5.8) If there is no such $C$, then there must be a sequence of $T_{j}$ and $C^{2, \alpha}$ functions $u_{j}$ with $\left.\frac{\partial u_{j}}{\partial n}\right|_{\partial \mathcal{M}}=0$ such that
$$\left[u_{j}\right]_{C_{\delta, \nu, \mu}^{2, \alpha}(\mathcal{M})}+\left[u_{j}\right]_{C_{\delta, \nu, \mu}^{2}(\mathcal{M})}+\left\|u_{j}\right\|_{C_{\delta, \nu+2, \mu}^{0, \alpha}(\mathcal{M})}=1$$
while
$$\left\|\mathcal{L}_{T_{j}} u_{j}\right\|_{C_{\delta, \nu+2, \mu}^{0, \alpha}(\mathcal{M})} \rightarrow 0 .$$
\end{itemize}

Then there must exist a sequence of points $\left(x_{j}\right)$ such that
$$\left[u_{j}\right]_{C_{\delta, \nu, \mu}^{2, \alpha}\left(x_{j}\right)}+\left[u_{j}\right]_{C_{\delta, \nu, \mu}^{2}\left(x_{j}\right)}+\left[u_{j}\right]_{C_{\delta, \nu+2, \mu}^{0, \alpha}\left(x_{j}\right)}+\left[u_{j}\right]_{C_{\delta, \nu+2, \mu}^{0}\left(x_{j}\right)}>\frac{1}{8} .$$

We will prove a contradiction by passing to the rescaled pointed Gromov-Hausdorff limit for the sequence $\left(x_{j}\right)_{j=1}^{\infty}$ and the rescaling factor $W\left(x_{j}, T\right)$. To preserve norms after rescaling the metric, we rescale both the functions $\left(u_{j}\right)$ and the weight functions $\rho_{\delta, \nu, \mu}^{(k+\alpha)}$. Recall that if $\hat{g}=\lambda^{2} g$ for any metric $g$ and $\lambda>0$, then formally,
$$\left\|\lambda^{k+\alpha} u\right\|_{C_{\hat{g}}^{k, \alpha}}=\|u\|_{C_{g}^{k, \alpha}}$$
on functions, and a similar equality holds for higher degree forms. In our case, since we are considering weighted Hölder norms, we have a choice of how to divide the scaling factor between the weight function $\rho_{\delta, \nu, \mu}^{(k+\alpha)}$ and the target function $u_{j}$, but we must ensure that the rescaled weight functions converge on the appropriate rescaled spaces. Thus let
$$\hat{\rho}_{\delta, \nu, \mu}^{k+\alpha}(q)=W\left(x_{j}\right)^{-(\nu+k+\alpha)} T_{j}^{-\mu} \rho_{\delta, \nu, \mu}^{k+\alpha}(q)=(1+w(q))^{-\delta}\left(\frac{W(q)}{W\left(x_{j}\right)}\right)^{\nu+k+\alpha}$$
and
$$\hat{u}_{j}(q)=W\left(x_{j}\right)^{\nu} T_{j}^{\mu} u_{j}(q) .$$
In what follows, whenever we take a Hölder norm of $\hat{u}_{j}$ or a related function, we take the weight to be $\hat{\rho}_{\delta, \nu, \mu}^{k+\alpha}$ and the metric to be $\hat{g}_{j}=W\left(x_{j}, T_{j}\right)^{-2} g_{T_{j}}$. Thus
$$\left[\mathcal{L}_{T_{j}} \hat{u}_{j}\right]_{C_{\delta, \nu+2, \mu}^{0, \alpha}(\mathcal{M})} \rightarrow 0$$
and
$$\left[\hat{u}_{j}\right]_{C_{\delta, \nu, \mu}^{2, \alpha}(\mathcal{M})}+\left[\hat{u}_{j}\right]_{C_{\delta, \nu, \mu}^{2}}^{2}(\mathcal{M})+\left\|\hat{u}_{j}\right\|_{C_{\delta, \nu+2, \mu}^{0, \alpha}(\mathcal{M})}=1$$
while
$$\left[\hat{u}_{j}\right]_{C_{\delta, \nu, \mu}^{2, \alpha}\left(x_{j}\right)}+\left[\hat{u}_{j}\right]_{C_{\delta, \nu, \mu}^{2}\left(x_{j}\right)}+\left[\hat{u}_{j}\right]_{C_{\delta, \nu+2, \mu}^{0, \alpha}\left(x_{j}\right)}+\left[\hat{u}_{j}\right]_{C_{\delta, \nu+2, \mu}^{0}\left(x_{j}\right)}>\frac{1}{8} .$$
As in the proof of Proposition 5.9, there must exist a subsequence of $\left(x_{j}\right)_{j=1}^{\infty}$ satisfying one of four behaviors.

Case 1. $\operatorname{Tr}_{w}\left(x_{j}\right) \rightarrow C<\infty$. By Proposition 5.9, we can view $\left(\hat{u}_{j}\right)_{j=1}^{\infty}$ as a sequence of functions on a neighborhood of a point $x_{\infty}$ in $\left(\mathbb{C}^{2}, g_{T N, a}\right)$ for some $a>1$. Now by Equation 5.14,
$$\hat{\rho}_{\delta, \nu, \mu}^{(k+\alpha)}(q)=\left(1+\mathcal{O}\left(T^{-1}\right)\right)\left(\frac{W(q)}{W\left(x_{j}\right)}\right)^{\nu+k+\alpha} .$$
But in the Taub-NUT region, $\frac{r_{w}(q)}{W\left(x_{j}\right)}$ converges to $d_{g_{T N, a}}^{2}(q, 0)$ (see Equation 4.11), so $\hat{\rho}_{\delta, \nu, \mu}^{(k+\alpha)}(q)$ is uniformly equivalent to a constant on $\hat{B}_{R}\left(x_{j}\right)$ for any fixed $R$ and large enough $j$. Thus by Equation 5.17, the unweighted local Schauder estimates discussed in the proof of Proposition 5.10, and the $C^{2, \alpha}$ convergence of the metrics,
$$\left\|\hat{u}_{j}\right\|_{C^{2, \alpha}\left(B_{R}\left(x_{\infty}\right)\right)} \leq C(R),$$
that is, $\hat{u}_{j}$ is bounded in the unweighted $C^{2, \alpha}$ toplogy on $B_{R}\left(x_{\infty}\right) \subset\left(\mathbb{C}^{2}, g_{T N, a}\right)$ (defined e.g. using Definition 5.5 with weight function $\rho_{\delta, \nu, \mu}^{(k+\alpha)} \equiv 1$ ) with bound depending on $R$, while
$$\hat{u}_{j}(q) \leq C d_{\hat{g}_{j}}(q, p)^{-2(\nu+2)}$$
for $C$ independent of $R$. Also, viewing $x_{j}$ as a point in $B_{R}\left(x_{\infty}\right)$ we have by Equation 5.18 that
$$\left[\hat{u}_{j}\right]_{C^{2, \alpha}\left(x_{j}\right)}+\left[\hat{u}_{j}\right]_{C^{2}\left(x_{j}\right)}+\left[\hat{u}_{j}\right]_{C^{0, \alpha}\left(x_{j}\right)}+\left[\hat{u}_{j}\right]_{C^{0}\left(x_{j}\right)}>\frac{1}{C}$$
for $C$ again independent of $R$. Equation 5.19 gives that for any $\beta<\alpha$ a subsequence converges in $C^{2, \beta}\left(B_{R}\left(x_{\infty}\right)\right)$ to a function $\hat{u}_{\infty}$, and by Equation 5.20,
$$\hat{u}_{\infty}(q) \leq C d_{g_{T N, a}}(q, 0)^{-2(\nu+2)}$$
for $C$ independent of $R$. Because we are rescaling the metric, $\mathcal{L}_{T}$ does not converge to $\Delta_{g_{T N}}-1$. Rather,
$$\begin{aligned}
\left\|\mathcal{L}_{T} \hat{u}_{j}\right\|_{C_{\delta, \nu+2, \mu}^{0, \alpha}\left(\hat{B}_{R}\left(x_{j}\right)\right)} & \geq\left\|W\left(x_{j}\right)^{-2} \Delta_{\hat{g}} \hat{u}_{j}\right\|_{C_{\delta, \nu+2, \mu}^{0, \alpha}\left(\hat{B}_{R}\left(x_{j}\right)\right)}-\left\|\hat{u}_{j}\right\|_{C_{\delta, \nu+2, \mu}^{0, \alpha}\left(\hat{B}_{R}\left(x_{j}\right)\right)} \\
& \geq C T^{2}\left\|\Delta_{\hat{g}} \hat{u}_{j}\right\|_{C_{\delta, \nu+2, \mu}^{0, \alpha}\left(\hat{B}_{R}\left(x_{j}\right)\right)}+\mathcal{O}(1)
\end{aligned}$$
Thus
$$\left\|\Delta_{\hat{g}} \hat{u}_{j}\right\|_{C^{0, \alpha}\left(\hat{B}_{R}\left(x_{\infty}\right)\right)}=\mathcal{O}\left(T^{-2}\right) .$$
By $C^{2, \beta}$ convergence, this implies that $\hat{u}_{\infty}$ is a $C^{2}$ harmonic function on $B_{R}\left(x_{\infty}\right)$. Also, standard Schauder estimates on $\hat{B}_{R}\left(x_{\infty}\right)$ now imply that $\hat{u}_{j}$ converges in $C^{2, \alpha}$.

Since $R$ was arbitrary, choosing a sequence of $R \rightarrow \infty$ gives a harmonic function on $\left(\mathbb{C}^{2}, g_{T N}\right)$. Since $\nu+2>0$, Equation 5.22 implies that $\hat{u}_{\infty}$ decays at infinity, so by the Cheng-Yau gradient estimate, $\hat{u}_{\infty}$ must vanish ([12] Proposition 6.6). But this contradicts Equation 5.21 by $C^{2, \alpha}$ convergence.

Case 2. $\operatorname{Tr}_{w}\left(x_{j}\right) \rightarrow \infty, r_{w}\left(x_{j}\right) \rightarrow 0$. By similar considerations as in the previous case, we have that $\hat{\rho}_{\delta, \nu, \mu}^{(k+\alpha)}(q)$ is uniformly constant on $\hat{B}_{R}\left(x_{j}\right) \backslash \hat{B}_{R^{-1}}(p)$. Now by Proposition 5.9. $\left(\mathcal{M}, \hat{g}_{j}, x_{j}\right)$ converges to $\left(\mathbb{R}^{3}, g_{\mathbb{R}^{3}}, x_{\infty}\right)$ in the pointed Gromov-Hausdorff topology. It is not immediate that $\hat{u}_{j}$ induces a function on $\mathbb{R}^{3}$. Instead, we observe that for each $j$,
$$\begin{gathered}
\left\|\hat{u}_{j}\right\|_{C^{2, \alpha}\left(\hat{B}_{R}\left(x_{j}\right) \backslash \hat{B}_{R^{-1}}(p)\right)} \leq C(R), \\
{\left[\hat{u}_{j}\right]_{C^{2, \alpha}\left(x_{j}\right)}+\left[\hat{u}_{j}\right]_{C^{2}\left(x_{j}\right)}+\left[\hat{u}_{j}\right]_{C^{0, \alpha}\left(x_{j}\right)}+\left[\hat{u}_{j}\right]_{C^{0}\left(x_{j}\right)}>\frac{1}{C},} \\
\left|\hat{u}_{j}(q)\right| \leq C\left(\frac{r_{w}\left(x_{j}\right)}{r_{w}(q)}\right)^{\nu+2},
\end{gathered}$$
and
$$\left\|\Delta_{\hat{g}} \hat{u}_{j}\right\|_{C^{0, \alpha}\left(\hat{B}_{R}\left(x_{j}\right)\right)} \rightarrow 0 .$$

Take $q \in B_{R}\left(x_{\infty}\right) \backslash\{0\}$ and assume that $q_{j} \in\left(\mathcal{M}, g_{T_{j}}\right) \rightarrow q$. Proposition 5.9 implies that there is $\epsilon>0$ such that $\left(\tilde{\hat{B}}_{\epsilon}\left(q_{j}\right), \hat{g}_{j}\right) \rightarrow\left(B_{R}(q) \times \mathbb{R}, g_{\mathbb{R}^{4}}\right)$ in $C^{2, \alpha}$. Pulling back to these covers, Equation 5.23 gives that $\hat{u}_{j}$ defines a sequence of functions converging to some $\hat{u}_{\infty}$ in $C^{2, \beta}\left(B_{R}(q) \times \mathbb{R}\right)$ for any $\beta<\alpha$. In addition, Equation 5.26 implies that $\hat{u}_{\infty}$ is $\Delta_{\mathbb{R}^{4}}$-harmonic.

Now since the $S^{1}$ fiber diameter vanishes as $j \rightarrow \infty$, Equation 5.23 implies that $\hat{u}_{\infty}$ is constant in the $t$ direction. Therefore $\hat{u}_{\infty}$ descends to a harmonic function on $\hat{B}_{\epsilon}(q)$. Repeating this near each point in $B_{R}\left(x_{\infty}\right)$ except the origin and then letting $R \rightarrow \infty$, we can take $\hat{u}_{\infty}$ to be defined on $\mathbb{R}^{3} \backslash\{0\}$. Finally, Equation 5.25 gives that
$$\left|\hat{u}_{\infty}(q)\right| \leq C d_{\mathbb{R}^{3}}(q, 0)^{-2(\nu+2)} .$$
Now $\nu+2 \in(0,1 / 2)$, so a harmonic function on $\mathbb{R}^{3} \backslash\{0\}$ which is bounded by $d_{\mathbb{R}^{3}}(q, 0)^{-2(\nu+2)}$ must vanish ([19] Lemma 5.7). As in the previous case, this implies that $\hat{u}_{\infty}=0$, contradicting Equation 5.24.

Case 3. $r_{w}\left(x_{j}\right) \nrightarrow 0, w\left(x_{j}\right) \nrightarrow \infty$. We can assume that $W\left(x_{j}\right)=1$ for large $j$. Since in this case $d_{g_{T_{j}}}\left(x_{j}, p\right) \rightarrow d_{\infty}<\infty$ and $\hat{g}_{j}=g_{T_{j}}$, we have that $\hat{\rho}_{\delta, \nu+2, \mu}^{(\alpha)}(q)$ is uniformly constant for $q \in \hat{B}_{R}\left(x_{j}\right) \backslash \hat{B}_{R^{-1}}(p)$. By similar arguments as in the previous case, we have that
$$\left\|\hat{u}_{j}\right\|_{C^{2, \alpha}\left(\hat{B}_{R}\left(x_{j}\right) \backslash \hat{B}_{R^{-1}}(p)\right)} \leq C(R),$$
while
$$\left[\hat{u}_{j}\right]_{C^{2, \alpha}\left(x_{j}\right)}+\left[\hat{u}_{j}\right]_{C^{2}\left(x_{j}\right)}+\left[\hat{u}_{j}\right]_{C^{0, \alpha}\left(x_{j}\right)}+\left[\hat{u}_{j}\right]_{C^{0}\left(x_{j}\right)}>\frac{1}{C}$$
and
$$\left|\hat{u}_{j}(q)\right| \leq C(1+w(q))^{\delta} r_{w}(q)^{-(\nu+2)}$$
for $C$ independent of $R$, and
$$\left\|\mathcal{L}_{T} \hat{u}_{j}\right\|_{C^{0, \alpha}\left(\hat{B}_{R}\left(x_{j}\right) \backslash \hat{B}_{R^{-1}}(p)\right)} \rightarrow 0 .$$
As in the previous bullet, $\hat{u}_{j}$ converges to an $S^{1}$ invariant function on each local universal cover, and these functions stitch to a function $\hat{u}_{\infty}$ on the punctured cylinder $D \times \mathbb{R} \backslash\{p\}$ such that $\left|\hat{u}_{\infty}(q)\right| \leq C(1+w(q))^{\delta}$ for $q$ away from $p$. Further, Equation 5.29 and Equation 5.30 give that $\hat{u}_{\infty}$ is a weak solution to $\mathcal{L}_{T} u=0$ on $D \times \mathbb{R}$. It is computed that
$$\Delta_{\hat{g}_{j}}=\pi^{*} \Delta_{g_{D}}+\left(1+w^{2}\right) \partial_{w}^{2}+2 w \partial_{w}+\frac{1}{1+w^{2}} \partial_{t}^{2}+\mathcal{O}\left(T^{-1}\right)$$
in coordinates on each local universal cover (see the proof of Proposition 5.9), so $u_{\infty}$ satisfies
$$\pi^{*} \Delta_{D} \hat{u}_{\infty}+\left(1+w^{2}\right) \partial_{w}^{2} \hat{u}_{\infty}+2 w \partial_{w} \hat{u}_{\infty}-\hat{u}_{\infty}=0$$
on $D \times \mathbb{R}$.
As above, we characterize this equation by separation of variables. Let $x=\frac{1}{2}(1+$ $i w)$. The resulting ODE is written
$$x(x-1) f_{x x}+(2 x-1) f_{x}-\left(1+\lambda^{2}\right) f=0 .$$
This is a hypergeometric equation with
$$\alpha(\lambda)=\frac{1+\sqrt{5+4 \lambda^{2}}}{2} \quad \beta(\lambda)=\frac{1-\sqrt{5+4 \lambda^{2}}}{2} \quad \gamma=1$$
in the notation of Section 3. As previously, the parameters satisfy the relation
$$\frac{\alpha(\lambda)+\beta(\lambda)+1}{2}=\gamma .$$

Therefore the arguments from Section 3 give that the two fundamental solutions $F(\alpha, \beta, \gamma ; x(z))$ and $F(\alpha, \beta, \gamma ; 1-x(z))$, each of which grows like $|w|^{-\beta}$ for large $|w|$. (Recall that we needed the inhomogeneous delta function term to achieve globally decaying solutions in Section 3.) Since $-\beta>\frac{\sqrt{5}-1}{2}$, choosing $\delta<\delta_{0}<\frac{\sqrt{5}-1}{2}$ gives that $u_{\infty}=0$, a contradiction.

Case 4. $w\left(x_{j}\right) \rightarrow \infty$. Recall that $d_{g_{T_{j}}}\left(x_{j}, \delta M\right) \rightarrow \infty$ if and only if $z_{\infty}=0$. First assume that this is the case. Now $d_{g_{T_{j}}}\left(x_{j}, p\right) \rightarrow \infty$, so $\hat{B}_{R}\left(x_{j}\right)$ converges to a ball in the Calabi model space in the rescaled coordinate $\underline{w}(q)=\frac{w(q)}{w\left(x_{j}\right)}$. We have by Equation 5.6 that
$$C e^{-R} \leq|\underline{w}(q)| \leq C e^{R} .$$

Now
$$\hat{\rho}_{\delta, \nu, \mu}^{(k+\alpha)}(q)=(1+w(q))^{-\delta}$$
on $\hat{B}_{R}\left(x_{j}\right)$ for any $R>0$ and large enough $j$. Thus if we define $\hat{v}_{j}=\left(1+w\left(x_{j}\right)\right)^{-\delta} \hat{u}_{j}$, then we have that
$$\begin{gathered}
\left\|\hat{v}_{j}\right\|_{C^{2, \alpha}\left(\hat{B}_{R}\left(x_{j}\right)\right)} \leq C(R), \\
{\left[\hat{v}_{j}\right]_{C^{2, \alpha}\left(x_{j}\right)}+\left[\hat{v}_{j}\right]_{C^{2}\left(x_{j}\right)}+\left[\hat{v}_{j}\right]_{C^{0, \alpha}\left(x_{j}\right)}+\left[\hat{v}_{j}\right]_{C^{0}\left(x_{j}\right)}>\frac{1}{C}} \\
\left|\hat{v}_{j}(q)\right| \leq C \frac{(1+w(q))^{\delta}}{\left(1+w\left(x_{j}\right)\right)^{\delta}} \leq C \underline{w}^{\delta}(q)
\end{gathered}$$
and
$$\left|\mathcal{L}_{T_{j}} \hat{v}_{j}(y)\right| \rightarrow 0 .$$
As above, we get an $S^{1}$-invariant limit function $\hat{v}_{\infty}$. Equation 5.33 implies that $\hat{v}_{\infty}=\mathcal{O}\left(\underline{w}^{\delta}\right)$. Using the expression we have derived for the metric in these coordinates and arguing as in the previous case, we have that
$$\pi^{*} \Delta_{D} \hat{v}_{\infty}+\underline{w}^{2} \partial_{\underline{w}}^{2} \hat{v}_{\infty}+2 \underline{w} \partial_{\underline{w}} \hat{v}_{\infty}-\hat{v}_{\infty}=0 .$$
Using separation of variables, the resulting ODE is
$$x^{2} f_{x x}+2 x f_{x}-\left(1+\lambda^{2}\right) f=0,$$
whose solutions are given by power functions in $\underline{w}$ with exponents contained in a discrete set. The decaying solutions blow up near $\underline{w}(q)=0$, so a global solution to the ODE must be growing like some definite power of $\underline{w}$. This contradicts Equation 5.33 for small enough $\delta$.

Now allow $z_{\infty}>0$, so for large enough $R, \hat{B}_{R}\left(x_{j}\right)$ contains a portion of the boundary. We have $\hat{v}_{\infty}$ as previously, but we cannot consider the behavior as $\underline{w}(q) \rightarrow \infty$ because $\underline{w}(q)$ is bounded. Instead, we argue that by Equation 5.35, the Hopf maximum principle, and the Neumann boundary condition on $u_{j}, \hat{v}_{\infty}$ cannot achieve its maximum on $\delta \mathcal{M}$. On the other hand, by Equation 5.33,
$$\hat{v}_{\infty}(q) \leq C\left(\frac{z(q)}{z_{\infty}}\right)^{\delta},$$
so since $\delta>0, \hat{v}_{\infty}(q)$ decays to zero away from the boundary of $\mathcal{C}$. Thus $\hat{v}_{\infty} \equiv 0$, contradicting $C^{2, \alpha}$ convergence and Equation 5.32. \(\square\)

\section*{6. Perturbation to an Exact Solution}
6.1. Implicit function theorem. Our last step is to apply the implicit function theorem in the following form.

Theorem 6.1. Let $\mathcal{F}: S_{1} \rightarrow S_{2}$ be a map between Banach spaces such that for all $v \in S_{1}$,
$$\mathcal{F}(v)-\mathcal{F}(0)=\mathcal{L}(v)+\mathcal{N}(v)$$
for operators $\mathcal{L}$ and $\mathcal{N}$ with the following properties:
\begin{itemize}
\item[(1)] (Bounded inverse) $\mathcal{L}$ is a linear isomorphism and there exists $C_{L}>0$ such that
$$\left\|\mathcal{L}^{-1}\right\|_{o p} \leq C_{L} .$$
\item[(2)] (Controlled nonlinear error) We have that $\mathcal{N}(0)=0$, and there exists $C_{N}>0$ and $r_{0} \in\left(0, \frac{1}{2 C_{N} C_{L}}\right)$ such that for all $v_{1}, v_{2} \in \overline{B_{r_{0}}(0)} \subset S_{1}$,
$$\left\|\mathcal{N}\left(v_{1}\right)-\mathcal{N}\left(v_{2}\right)\right\|_{S_{2}} \leq C_{N} r_{0}\left\|v_{1}-v_{2}\right\|_{S_{1}} .$$
\end{itemize}
(3) (Controlled initial error) The radius $r_{0}$ can be chosen such that
$$\|\mathcal{F}(0)\|_{S_{2}} \leq \frac{r_{0}}{4 C_{L}} .$$
Then there exists a unique $x \in B_{r_{0}}(0)$ such that
$$\mathcal{F}(x)=0 .$$
Further,
$$\|x\|_{S_{1}} \leq 2 C_{L}\|\mathcal{F}(0)\|_{S_{2}} .$$

In our case
$$S_{1}=\left\{\phi \in C^{2, \alpha}(\mathcal{M}), \phi \text { is } S^{1} \text { invariant and }\left.\frac{\partial \phi}{\partial n}\right|_{\partial M}=0\right\}$$
with the norm
$$\|\phi\|_{S_{1}}=[\phi]_{C_{\delta, \nu, \mu}^{2, \alpha}(\mathcal{M})}+[\phi]_{C_{\delta, \nu, \mu}^{2}(\mathcal{M})}^{2}+\|\phi\|_{C_{\delta, \nu+2, \mu}^{0, \alpha}(\mathcal{M})}$$
with $\delta, \nu$, and $\mu$ as in Theorem 5.8 and
$$S_{2}=\left\{f \in C_{\delta, \nu+2, \mu}^{0, \alpha}(\mathcal{M}): f \text { is } S^{1} \text {-invariant }\right\}$$
with the norm
$$\|f\|_{S_{2}}=\|f\|_{C_{\delta, \nu+2, \mu}^{0, \alpha}(\mathcal{M})} .$$
Note that these spaces depend on $T$.
For each $T$ we seek a function $\mathcal{F}_{T}: S_{1} \rightarrow S_{2}$ with the property that if $\mathcal{F}_{T}(v)=0$ then $\omega_{v}=\omega_{T}+i \partial \bar{\partial} v$ is Kähler-Einstein. Recall that in our notation
$$\operatorname{Ric} \omega_{T}=-i \partial \bar{\partial} \log \left(\frac{\chi}{h}\right)-\pi^{*} \omega_{D}$$
where $\omega_{T}$ is the solution constructed in Section 3 for a fixed $T$ and $\chi$ and $h$ implicitly depend on $T$. Now say there exists a Kähler potential $\phi$ such that
$$\omega_{T}=\pi^{*} \omega_{D}+i \partial \bar{\partial} \phi .$$
Then
$$\operatorname{Ric} \omega_{T}+\omega_{T}=-i \partial \bar{\partial}\left(\log \left(\frac{\chi}{h}\right)-\phi\right) .$$

For each $T$ we define the error function to be
$$\operatorname{Err}_{K E}=\frac{\chi}{h} e^{-\phi}-1,$$
so
$$\operatorname{Ric} \omega_{T}+\omega_{T}=-i \partial \bar{\partial} \log \left(1+\operatorname{Err}_{K E}\right) .$$
But
$$\begin{aligned}
\operatorname{Ric} \omega_{v}+\omega_{v} & =\operatorname{Ric} \omega_{v}-\operatorname{Ric} \omega_{T}+\operatorname{Ric} \omega_{T}+\omega_{T}-\omega_{T}+\omega_{v} \\
& =-i \partial \bar{\partial} \log \left(\frac{\omega_{v}^{2}}{\omega_{T}^{2}}\right)-i \partial \bar{\partial} \log \left(1+\operatorname{Err}_{K E}\right)+i \partial \partial v
\end{aligned}$$
We define
$$\mathcal{F}_{T}(v)=-v+\log \left(\frac{\omega_{v}^{2}}{\omega_{T}^{2}}\right)+\log \left(1+\operatorname{Err}_{K E}\right)$$
so that $\operatorname{Ric} \omega_{v}+\omega_{v}=-i \partial \bar{\partial} \mathcal{F}(v)$.
To linearize at 0, we take $\eta \in T \mathcal{S}^{1} \simeq \mathcal{S}^{1}$ and evaluate
$$\begin{aligned}
\mathcal{F}_{T}(t \eta)-\mathcal{F}(0) & =-t \eta+\log \left(1+\operatorname{Tr}_{\omega_{T}} i \partial \bar{\partial} t \eta+\mathcal{O}\left(t^{2}\right)\right) \\
& =t\left(-\eta+\Delta_{\omega_{T}} \eta+\mathcal{O}(t)\right)
\end{aligned}$$
Thus the derivative of $\mathcal{F}_{T}$ at 0 is $\Delta_{\omega_{T}}-1$. We write
$$\mathcal{L}_{T}(v)=\left(\Delta_{\omega_{T}}-1\right) v$$
and
$$\mathcal{N}_{T}(v)=\log \left(\frac{\omega_{v}^{2}}{\omega_{T}^{2}}\right)-\Delta_{\omega_{T}} v .$$

\subsection*{6.2. Error estimates.}
6.2.1. Nonlinear error estimate. First we examine the nonlinear error.

Proposition 6.2. There exists $C_{N}>0$ such that for all $T \gg 0$ and $\rho \in\left(0, \frac{1}{C_{N}}\right)$,
$$\left\|\mathcal{N}_{T}\left(v_{1}\right)-\mathcal{N}_{T}\left(v_{2}\right)\right\|_{S_{2}} \leq C_{N} \rho\left\|v_{1}-v_{2}\right\|_{S_{1}}$$
for all $v_{1}, v_{2} \in \overline{B_{\rho}(0)} \subset S_{1}$.
Proof. Note that for all choices of parameters satisfying the assumptions of Theorem 5.8, $\rho_{\delta, \nu+2, \mu}^{(0)}=\rho_{\delta, \nu, \mu}^{(2)}$ is bounded below on $\mathcal{M}$ independently of $T$. For if $|w|<1$, then since $W(q) \geq T^{-1}$,
$$\rho_{\delta, \nu+2, \mu}^{(0)} \geq 2^{-\delta} T^{\mu-(\nu+2)}$$
which is bounded below since $\mu>\nu+2$. On the other hand if $|w| \geq 1$, then
$$\rho_{\delta, \nu+2, \mu}^{(0)} \geq 2 T^{\mu-\delta},$$
which is bounded below since $\mu>\delta$. This bounds the Hölder norms of higher powers of functions in terms of the Hölder norms of lower powers.

Expanding Equation 6.5, we have that
$$\mathcal{N}_{T}(i \partial \bar{\partial} v)=\log \left(1+\Delta_{\omega_{T}} v+\frac{(i \partial \bar{\partial} v)^{2}}{\omega_{T}^{2}}\right)-\Delta_{\omega_{T}} v .$$

Now if $v_{i} \in B_{\rho}(0) \subset \mathcal{S}_{1}$ for small $\rho>0$, we have that
$$\begin{aligned}
\left\|\frac{\left(i \partial \bar{\partial} v_{1}\right)^{2}}{\omega_{T}^{2}}-\frac{\left(i \partial \bar{\partial} v_{2}\right)^{2}}{\omega_{T}^{2}}\right\|_{C_{\delta, \nu+2, \mu}^{0, \alpha}(\mathcal{M})} & \leq C\left(\left[\nabla^{2} v_{1}\right]_{C^{0}}+\left[\nabla^{2} v_{2}\right]_{C^{0}}\right)\left[v_{1}-v_{2}\right]_{C_{\delta, \nu, \mu}^{2, \alpha}(\mathcal{M})} \\
& \leq C\left(\rho_{\delta, \nu, \mu}^{(2)}\right)^{-1} \rho\left[v_{1}-v_{2}\right]_{C_{\delta, \nu, \mu}^{2, \alpha}(\mathcal{M})} \\
& \leq C \rho\left[v_{1}-v_{2}\right]_{C_{\delta, \nu, \mu}^{2, \alpha}(\mathcal{M})}
\end{aligned}$$
and
$$\begin{aligned}
\|\left(\Delta_{\omega_{T}} v_{1}+\frac{\left(i \partial \bar{\partial} v_{1}\right)^{2}}{\omega_{T}^{2}}\right)^{\ell} & -\left(\Delta_{\omega_{T}} v_{2}+\frac{\left(i \partial \bar{\partial} v_{2}\right)^{2}}{\omega_{T}^{2}}\right)^{\ell} \|_{C_{\delta, \mu+2, \mu}^{0, \alpha}(\mathcal{M})} \\
& \leq C^{\ell}\left(\left[\nabla^{2} v_{1}\right]_{C^{0}}+\left[\nabla^{2} v_{2}\right]_{C^{0}}\right)^{\ell-1}\left[v_{1}-v_{2}\right]_{C_{\delta, \nu, \mu}^{2, \alpha}}(\mathcal{M}) \\
& \leq C^{\ell}\left(\rho_{\delta, \nu, \mu}^{(2)}\right)^{1-\ell}(2 \rho)^{\ell-1}\left[v_{1}-v_{2}\right]_{C_{\delta, \nu, \mu}^{2, \alpha}(\mathcal{M})} \\
& \leq C^{\ell}(2 \rho)^{\ell-1}\left[v_{1}-v_{2}\right]_{C_{\delta, \nu, \mu}^{2, \alpha}(\mathcal{M})}
\end{aligned}$$
The constant $C$ in this inequality does not depend on $\rho, \ell$, or $T$. Here we have used the inequality
$$\left|a^{\ell}-b^{\ell}\right| \leq|a-b|(|a|+|b|)^{\ell-1} .$$
Now since
$$\begin{aligned}
\mathcal{N}_{T}\left(i \partial \bar{\partial} v_{1}\right)-\mathcal{N}_{T}\left(i \partial \bar{\partial} v_{2}\right)= & \frac{\left(i \partial \bar{\partial} v_{1}\right)^{2}}{\omega_{T}^{2}}-\frac{\left(i \partial \bar{\partial} v_{2}\right)^{2}}{\omega_{T}^{2}} \\
& +\sum_{\ell=2}^{\infty} \frac{(-1)^{\ell+1}}{\ell}\left(\left(\Delta_{\omega_{T}} v_{1}+\frac{\left(i \partial \bar{\partial} v_{1}\right)^{2}}{\omega_{T}^{2}}\right)^{\ell}-\left(\Delta_{\omega_{T}} v_{2}+\frac{\left(i \partial \bar{\partial} v_{2}\right)^{2}}{\omega_{T}^{2}}\right)^{\ell}\right),
\end{aligned}$$
this estimate gives that
$$\begin{aligned}
\| \mathcal{N}_{T}\left(i \partial \bar{\partial} v_{1}\right) & -\mathcal{N}_{T}\left(i \partial \bar{\partial} v_{2}\right) \|_{C_{\delta, \nu+2, \mu}^{0, \alpha}(\mathcal{M})} \\
& \leq C \rho\left[v_{1}-v_{2}\right]_{C_{\delta, \nu, \mu}^{2, \alpha}(\mathcal{M})}+C \rho\left(\sum_{\ell=0}^{\infty}(C \rho)^{\ell}\right)\left\|v_{1}-v_{2}\right\|_{S^{1}} \\
& \leq C \rho\left\|v_{1}-v_{2}\right\|_{S^{1}}
\end{aligned}$$
for small enough $\rho$. By the discussion above, the constant in this inequality and the bound on $\rho$ do not depend on $T$. \(\square\)
6.2.2. Deriving the Kähler potential. To understand the initial error, we must compute a Kähler potential for $\omega_{T}$. To do this, we follow [19] Section 4.2.2.

Such a potential should be an $S^{1}$-invariant function on the total space $\mathcal{M}$ such that
$$\pi^{*} \omega_{D}+\frac{1}{2} d d^{c} \phi=\omega_{T} .$$
Then $d^{c} \phi=d_{D}^{c} \phi+\phi_{z} h^{-1} \Theta$ by $S^{1}$ invariance and the definition of $\Theta$. Using Equation 2.1 and separating components as in Section 2.2, Equation 6.6 is equivalent to the system
$$\left\{\begin{array}{l}
2 \omega_{D}+d_{D} d_{D}^{c} \phi+\phi_{z} h^{-1} \partial_{z} \tilde{\omega}=2 \tilde{\omega} \\
d_{D}^{c} \phi_{z}-\phi_{z} h^{-1} d_{D}^{c} h=0 \\
d\left(\phi_{z} h^{-1}\right)=2 d z
\end{array}\right.$$

Integrating the last equation twice yields that
$$\phi_{z} h^{-1}=2 z+C^{\prime}$$
for a constant $C^{\prime}$, and so integrating again we find
$$\phi=\int_{z_{0}}^{z} h\left(2 u+C^{\prime}\right) d u+\phi_{0}$$
where $\phi_{0}$ is a function on $D$. Then the second equation is satisfied as well. Taking the $z$ derivative of the first equation gives the relation
$$\left(\Delta_{D} \phi_{z}\right) \omega_{D}+\left(\phi_{z} h^{-1}\right)_{z} \partial_{z} \tilde{\omega}+\left(\phi_{z} h^{-1}\right) \partial_{z}^{2} \omega=2 \partial_{z} \tilde{\omega} .$$
Using Equation 2.11 it is checked that the above choice of $\phi$ solves this equation. Therefore $\phi$ will be a solution if the first equation is satisfied at any $z$ away from $p$. Taking $z=1$, the equation yields
$$2 \omega_{D}+\left(\Delta_{D} \phi_{0}\right) \omega_{D}+\left(2+C^{\prime}\right) \partial_{z} \tilde{\omega}=2 \tilde{\omega} .$$
Since $\partial_{z}^{2} \tilde{\omega}=-\Delta_{D} h, \partial_{z}^{2} \int_{D} \tilde{\omega}=0$, and so
$$\int_{D} \tilde{\omega}(1)=\int_{D} \tilde{\omega}(0)+\int_{D} \partial_{z} \tilde{\omega}=\int_{D} \omega_{D}+\int_{D} \partial_{z} \tilde{\omega} .$$
This implies that $C^{\prime}=0$, i.e.
$$\phi_{z} h^{-1}=2 z .$$

Make the choice $z_{0}=0$. Then to determine $\phi_{0}$, we use Equation 3.27 to solve the first line of Equation 6.7 on the slice $z=0$. By Equation 6.6, we have that
$$\Delta_{D} \phi_{0}=\frac{1}{2 T|y|}+T^{-1} g^{0, \alpha} .$$
By elliptic regularity, this implies that
$$\phi_{0}=\frac{|y|}{2 T}+T^{-1} g^{2, \alpha} .$$
In summary,
$$\phi=\int_{0}^{z} 2 h u d u+\frac{|y|}{2 T}+T^{-1} g^{2, \alpha} .$$
6.2.3. Linear error estimate. Now we are ready to estimate $\mathcal{F}_{T}(0)=\log \left(1+\operatorname{Err}_{K E}\right)$. We show that $\operatorname{Err}_{K E}$ can be made arbitrarily small in $C_{\delta, \nu+2, \mu}^{0, \alpha}$ by taking $T$ large enough. The analysis looks different near and away from the singularity.

Proposition 6.3. For any $C_{L}>0$ and $\rho \in \mathbb{R}_{>0}$,
$$\left\|\mathcal{F}_{T}(0)\right\|_{C_{\delta, \nu+2, \mu}^{0, \alpha}(\mathcal{M})} \leq \frac{\rho}{4 C_{L}}$$
for large enough $T$.
Proof. By the discussion in Section 3.2, there exists $C_{2}$ independent of $T$ such that Equations 3.26 and 3.27 hold for all $|w|<C_{2}$ up to a smooth correction of order $\mathcal{O}(T)$ for $\delta h$ and $\mathcal{O}\left(T^{-1}\right)$ for $\delta \chi$. Thus we have that if $r_{w} \leq C_{2}$,
$$h=T^{2}\left(\frac{1}{1+(T z)^{2}}+\frac{1}{2 T r_{w}}+T^{-1} g^{0, \alpha}\right) .$$

Therefore by Equation 6.10,
$$\phi(z)=\frac{|y|}{2 T}+\log \left(1+(T z)^{2}\right)+T^{-1} g^{0, \alpha}+C^{\prime}$$
for some $C^{\prime}>0$. If we take $C^{\prime}=-\log \left(T^{2}\right)$, we find
$$\begin{aligned}
\frac{\chi}{h} e^{-\phi} & =\frac{1+\frac{1}{2 T r_{w}}+T^{-1} g^{0, \alpha}}{T^{2}\left(\frac{1}{1+(T z)^{2}}+\frac{1}{2 T r_{w}}+T^{-1} g^{0, \alpha}\right)} \frac{\operatorname{Exp}\left(-\frac{|y|}{2 T}-C^{\prime}+T^{-1} g^{0, \alpha}\right)}{1+(T z)^{2}} \\
& =\frac{1+\frac{1}{2 T r_{w}}+T^{-1} g^{0, \alpha}}{\frac{1}{1+(T z)^{2}}+\frac{1}{2 T r_{w}}+T^{-1} g^{0, \alpha}} \cdot \frac{1+T^{-1} g^{0, \alpha}}{1+(T z)^{2}} \\
& =\frac{1+\frac{1}{2 T r_{w}}+T^{-1} g^{0, \alpha}}{1+\frac{1}{2 T r_{w}}+T^{-1} g^{0, \alpha}}\left(1+T^{-1} g^{0, \alpha}\right) \\
& =1+T^{-1} g^{0, \alpha} .
\end{aligned}$$
The calculations when $r_{w} \geq C_{2}$ but still $|w| \leq C_{2}$ are simpler and give a similar estimate. Since $\rho_{\delta, \nu+2, \mu}^{(\alpha)}$ is uniformly bounded above by $T^{\mu}$, we therefore have that
$$\left\|\operatorname{Err}_{\mathrm{KE}}-1\right\|_{C_{\delta, \nu+2, \mu}^{0, \alpha}\left(\left\{|w| \leq C_{2}\right\}\right)}=\mathcal{O}\left(T^{\mu-1}\right)$$
But by our requirement that $\mu<1$, this last term decays in $T$.
Away from the singular point $\chi, h$, and $\phi$ are smooth, so it is sufficient to prove a $C^{0}$ bound. Integrating Equation 5.8, we find that for $z<0$
$$\begin{aligned}
\phi & =\phi\left(-\frac{C_{2}}{T}\right)+\int_{-\frac{C_{2}}{T}}^{z} 2 z h d z \\
& =\log \left(1+C_{2}^{2}\right)-\log \left(T^{2}\right)+\int_{-\frac{C_{2}}{T}}^{z} \frac{2 T^{2} z\left(k_{-} z+1\right)}{\frac{2 T^{2} k_{-} z^{3}}{3}+(T z)^{2}+1} d z+\mathcal{O}\left(T^{-1}\right) \\
& =\log \left(1+C_{2}^{2}\right)-\log \left(T^{2}\right)+\log \left(\frac{2 T^{2} k_{-} z^{3}}{3}+(T z)^{2}+1\right)-\log \left(1+C_{2}^{2}+\mathcal{O}\left(T^{-1}\right)\right)+\mathcal{O}\left(T^{-1}\right) \\
& =-\log \left(T^{2}\right)+\log \left(\frac{2 T^{2} k_{-} z^{3}}{3}+(T z)^{2}+1\right)+\mathcal{O}\left(T^{-1}\right)
\end{aligned}$$
Therefore by Equation 5.9.
$$\begin{aligned}
\frac{\chi}{h} e^{-\phi} & =\frac{1+k_{-} z+\mathcal{O}\left(T^{-1}\right)}{\frac{1+k_{-} z}{\frac{2 T^{2} k_{-} z^{3}}{3}+(T z)^{2}+1}+\mathcal{O}\left(T^{-5} z^{-4}\right)} \frac{1+\mathcal{O}\left(T^{-1}\right)}{\frac{2 T^{2} k_{-} z^{3}}{3}+(T z)^{2}+1} \\
& =1+\mathcal{O}\left(T^{-1}\right)
\end{aligned}$$
as desired. The calculations are similar for $z>0$ since $1+k_{+} z$ is bounded below for $z<1 / 2$. Note that the $\mathcal{O}\left(T^{-5} z^{-4}\right)$ decay of $\delta h$ provided by Proposition 3.6 is necessary for the last equality since this term must absorb an $\mathcal{O}\left(T^{2} z^{2}\right)$ term. \(\square\)
6.3. Proof of Theorems 1.1 and 1.2. Propositions 6.2 and 6.3 allow us to perturb $\left(\mathcal{M}, \omega_{T}\right)$ to a Kähler-Einstein surface for large enough $T$ via Theorem 6.1.

Proof. (Theorem 1.1) Fix $\epsilon>0, R>0$, and $\alpha<\mu-\max (\delta, \nu+2)$. The operator $\mathcal{L}_{T}: S_{1} \rightarrow S_{2}$ is invertible for all $T$ and Proposition 5.8 implies that the inverse is bounded by some $C_{L}$ independent of $T$. Proposition 6.2 gives the nonlinear error
control for all sufficiently small $r_{0}$ for some bound $C_{N}$ and large enough $T$. Fixing some $r_{0}<\min \left(\epsilon,\left(2 C_{N} C_{L}\right)^{-1}\right)$, Proposition 6.3 gives that
$$\|\mathcal{F}(0)\|_{C_{\delta, \nu+2, \mu}^{0, \alpha}(\mathcal{M})}<\frac{\epsilon}{4 C_{L}}$$
for large enough $T$. Finally, for fixed $x \in \partial \mathcal{M}$, Proposition 5.9 gives that for large enough $T, B_{R}(x) \subset\left(\mathcal{M}, \omega_{T}\right)$ is $\epsilon / 2$-close in $C^{0, \alpha}$ to a ball in $\left(\mathcal{C}_{ \pm}, g_{\mathcal{C}_{ \pm}}\right)$. Because the scaling of the cross-section $D$ is bounded in $T, T$ can be chosen uniformly over $\partial \mathcal{M}$.

Choosing $T$ large enough to satisfy all these requirements, Theorem 6.1 allows us to find $u$ such that
$$\omega=\omega_{T}+i \partial \bar{\partial} u$$
is Kähler-Einstein and
$$[u]_{C_{\delta, \nu, \mu}^{2, \alpha}(\mathcal{M})}<\frac{\epsilon}{2} .$$
Since
$$\rho_{\delta, \nu, \mu}^{(2+\alpha)} \geq C T^{\mu-(\max (\delta, \nu+2)+\alpha)},$$
our requirement that $\mu>(\max (\delta, \nu+2)+\alpha)$ implies that for any $x \in \partial \mathcal{M}$ and large enough $T, B_{R}(x)$ is $\epsilon$-close in $C^{0, \alpha}$ to a ball in $\left(\mathcal{C}_{ \pm}, g_{\mathcal{C}_{ \pm}}\right)$.

Since the $\omega_{\mathrm{KE}, T}$ are Kähler-Einstein with $\lambda=-1$, higher regularity follows from Theorem 5.4. \(\square\)

Proof. (Theorem 1.2) Let $\left(\mathcal{M}, \omega_{T_{j}}\right)$ be the approximate solution and $u_{j}$ the $S^{1}$ -invariant correction to a Kähler-Einstein metric, so
$$\omega_{\mathrm{KE}, T_{j}}=\omega_{T_{j}}+i \partial \bar{\partial} u_{j} .$$
The proof of Theorem 1.1 gives that
$$\left\|i \partial \bar{\partial} u_{j}\right\|_{C^{0, \alpha}(\mathcal{M})}=o(1) .$$
Thus
$$\left|W\left(x_{j}\right)^{-2} i \partial \bar{\partial} u_{j}(x)\right|_{W\left(x_{j}\right)^{-2} g_{T_{j}}}=o(1) .$$

Now by Proposition 5.9, the sequence $\left(\mathcal{M}, W\left(x_{j}\right)^{-2} g_{T_{j}}, x_{j}\right)$ subconverges in the pointed Gromov-Hausdorff topology to one of the four desired spaces $\left(X_{\infty}, g_{\infty}, x_{\infty}\right)$. This means that for any $\epsilon>0$ and $R>0$,
$$g_{\mathrm{GH}}\left(B_{R}\left(x_{j}\right), B_{R}\left(x_{\infty}\right)\right) \leq \frac{\epsilon}{2}$$
for large enough $j$. But by Equation 6.14, the correction by $i \partial \bar{\partial} u_{j}$ changes the distance between any two points by an arbitrarily small amount. For large enough $j$, this implies that
$$g_{\mathrm{GH}}\left(B_{R}\left(x_{j}\right), B_{R}\left(x_{\infty}\right)\right) \leq \epsilon .$$

In the noncollapsing cases (Taub-NUT and Calabi model space), smooth convergence follows from Theorem 5.4. In the collapsing cases ( $\mathbb{R}^{3}$ and $D \times \mathbb{R}$ ), we can make similar arguments to prove $C^{k, \alpha}$ convergence for any $k$ on local universal covers. Curvature is then bounded on the local universal cover, so it is also bounded under the Riemannian covering map, which is a local isometry. \(\square\)