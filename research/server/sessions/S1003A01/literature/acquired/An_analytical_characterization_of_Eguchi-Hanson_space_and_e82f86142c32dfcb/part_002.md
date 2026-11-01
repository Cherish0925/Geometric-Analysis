---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: An analytical characterization of Eguchi-Hanson space and ...]

Proposition 4.10. $\tilde{G}^{0} \cong S O(3)$ acts smoothly, isometrically, and effectively on $\left(\tilde{M}_{\infty}, \tilde{g}\right)$ with cohomogeneity two. The action preserves all CMC leaves $\left(\mathbb{S}^{3}, \tilde{g}_{\rho}\right)$, and restricts to act with cohomogeneity one on each leaf.

Corollary 4.11. (a) The action has principal isotropy subgroup $H \cong S O(2)$.
\begin{itemize}
\item[(b)] Each principal orbit is diffeomorphic to $\mathbb{S}^{2}$ and the metric on it is round.
\item[(c)] The induced metric on each CMC leaf $\left(\mathbb{S}^{3}, \tilde{g}_{\rho}\right)$ is of the form
$$d s^{2}+f(s)^{2} g_{\mathbb{S}^{2}}$$
where $s \in(0,1)$, and $f:(0,1) \rightarrow \mathbb{R}$ is a smooth positive function with $f(0)=f(1)=0$.
\end{itemize}

Proof. Since the principal orbits are 2-dimensional, the principal isotropy subgroup $H$ is a 1-dimensional closed Lie subgroup of $S O(3)$. The only ones up to conjugacy are $S O(2)$ and $O(2)$. If $H \cong O(2)$, then each principal orbit is an $S O(3) / O(2) \cong \mathbb{R P}^{2}$ embedded in a CMC leaf of $\tilde{M}_{\infty}$. But it is impossible for $\mathbb{R} \mathbb{P}^{2}$ to embed into $\mathbb{S}^{3}$. Hence, $H \cong S O(2)$ and part (a) follows. The principal orbits are then $S O(3) / S O(2) \cong \mathbb{S}^{2}$ equipped with $S O(3)$-invariant metrics, which are necessarily round. This proves (b). Finally, (c) follows by restricting to a CMC leaf where the action has cohomogeneity one, then applying the structure theory of cohomogeneity one metrics (e.g. [1, §6.3]). (This is similar to Proposition 3.12, except the orbit space is a closed interval in this case.) \(\square\)

Let $\tilde{M}_{\infty}^{\text {prin }} \subset \tilde{M}_{\infty}$ be the union of principal orbits with respect to the action of $\tilde{G}^{0}$. The orbit space $B:=\tilde{M}_{\infty}^{\text {prin }} / \tilde{G}^{0}$ is a connected Riemannian manifold [1, Theorem 3.82].

We claim that $B$ is diffeomorphic to $\mathbb{R}^{2}$. Indeed, Corollary 4.11 shows that each CMC leaf carries a cohomogeneity one $\tilde{G}^{0}$-action whose principal part quotients to an open interval (0, 1), while $\tilde{M}_{\infty}$ itself is foliated by these CMC leaves and is diffeomorphic to $\left(R_{0}, \infty\right) \times \mathbb{S}^{3}$. Thus, the orbit space $B$ of $\tilde{M}_{\infty}^{\text {prin }}$ is $\left(R_{0}, \infty\right) \times(0,1)$, which is diffeomorphic to $\mathbb{R}^{2}$.

For each $x \in \tilde{M}_{\infty}^{\text {prin }}$, we have
$$T_{x} \tilde{M}_{\infty}^{\text {prin }}=\mathcal{H}_{x} \oplus \mathcal{V}_{x},$$
where $\mathcal{V}_{x}$ is the tangent space to the $\mathbb{S}^{2}$ orbit and $\mathcal{H}_{x}=\mathcal{V}_{x}^{\perp}$ is its $\tilde{g}$-orthogonal complement. We call $\mathcal{H}_{x}$ and $\mathcal{V}_{x}$ the horizontal and vertical subspaces at $x$ respectively. Since $\tilde{G}^{0}$ acts isometrically, it preserves the subbundles $\mathcal{H}$ and $\mathcal{V}$. Restricting to the isotropy subgroup $H$ at $x$ gives the following.
\begin{itemize}
\item[-] $\mathcal{H}_{x}$ carries the slice representation of $H=S O(2)$. This is a trivial representation because the orbit of $x$ is principal [1, §3.4].
\item[-] $\mathcal{V}_{x}$ carries the isotropy representation of $H$, which is identified with the adjoint representation of $H$ on an $\operatorname{Ad}(H)$-invariant complement of $\mathfrak{h}$ in $\mathfrak{g}$. As one checks, this is isomorphic to the defining representation of $S O(2)$.
\end{itemize}
Let $(\cdot)^{\mathcal{H}}$ and $(\cdot)^{\mathcal{V}}$ denote orthogonal projections of tangent vectors to $\mathcal{H}$ and $\mathcal{V}$ respectively. Following O'Neill [41], we define tensor fields $A$ and $T$ by setting at each $x \in \tilde{M}_{\infty}^{\text {prin }}$
$$\begin{aligned}
A_{x}: \wedge^{2} \mathcal{H}_{x} \rightarrow \mathcal{V}_{x}, & A_{x}(X, Y)=\frac{1}{2}[\tilde{X}, \tilde{Y}]^{\mathcal{V}}, \\
T_{x}: \mathcal{V}_{x} \otimes \mathcal{V}_{x} \rightarrow \mathcal{H}_{x}, & T_{x}(Z, W)=\left(\nabla_{\tilde{Z}} \tilde{W}\right)^{\mathcal{H}},
\end{aligned}$$
where $\tilde{X}$ and $\tilde{Y}$ are local horizontal extensions of $X$ and $Y$, and $\tilde{Z}$ and $\tilde{W}$ are local vertical extensions of $Z$ and $W$. Vanishing of $A$ is equivalent to integrability of the horizontal distribution. Meanwhile, $T$ is the second fundamental form of the $\mathbb{S}^{2}$ orbits. It is straightforward to verify that for all $\phi \in \tilde{G}^{0}$,
$$A(d \phi(X), d \phi(Y))=d \phi(A(X, Y)), \quad T(d \phi(Z), d \phi(W))=d \phi(T(Z, W)) .$$
In particular, $A_{x}$ and $T_{x}$ are $H$-equivariant maps at each $x \in \tilde{M}_{\infty}^{\text {prin }}$.

Lemma 4.12. (a) $A \equiv 0$, i.e. the horizontal distribution $\mathcal{H} \subset T \tilde{M}_{\infty}^{\text {prin }}$ is integrable.
\begin{itemize}
\item[(b)] Each principal orbit is umbilic, i.e. $T_{x}(Z, W)=\tilde{g}_{x}(Z, W) \eta_{x}$ for all $Z, W \in \mathcal{V}_{x}$ where $\eta_{x} \in \mathcal{H}_{x}$ is the mean curvature vector.
\item[(c)] Each principal orbit is spheric, i.e. the mean curvature vector field $\eta$ along any principal orbit satisfies $\left(\nabla_{Z} \eta\right)^{\mathcal{H}}=0$ for all vertical vectors $Z \in \mathcal{V}_{x}$.
\end{itemize}

Proof. (a) Since $\mathcal{H}_{x}$ is a trivial $H$-module, so is $\wedge^{2} \mathcal{H}_{x}$. Also, $\mathcal{V}_{x}$ has no nonzero vectors fixed by $H$. Since $A_{x}$ is $H$-equivariant, these facts force $A_{x}=0$.
(b) Since $T_{x}$ is $H$-equivariant, and $\mathcal{H}_{x}$ is a trivial $H$-module, it follows that $T_{x}$ is $H$ -invariant. Take a basis $\left\{e_{1}, e_{2}\right\}$ for $\mathcal{H}_{x}$ and write $T_{x}(Z, W)=T_{x}^{(1)}(Z, W) e_{1}+T_{x}^{(2)}(Z, W) e_{2}$; then $T_{x}^{(i)}: \mathcal{V}_{x} \otimes \mathcal{V}_{x} \rightarrow \mathbb{R}$ is $H$-invariant for $i=1,2$. By Schur's lemma, the space of $H$-invariant symmetric 2-tensors on $\mathcal{V}_{x}$ is one-dimensional, spanned by $\tilde{g}_{x}$. Hence, $T_{x}^{(1)}$ and $T_{x}^{(2)}$ each are multiples of $\tilde{g}_{x}$, varying smoothly in $x$. Thus, $T_{x}(Z, W)=\tilde{g}_{x}(Z, W) \nu_{x}$ for some $\nu_{x} \in \mathcal{H}_{x}$. As $T_{x}$ is the second fundamental form of the orbit at $x$, we must have $\nu_{x}=\eta_{x}$.
(c) Using part (b) and (4.3), we see that $d \phi\left(\eta_{x}\right)=\eta_{\phi(x)}$ for each $\phi \in \tilde{G}^{0}$. Using this, one verifies that
$$d \phi\left(\left(\nabla_{Z} \eta\right)^{\mathcal{H}}\right)=\left(\nabla_{d \phi(Z)} \eta\right)^{\mathcal{H}} \quad \text { for all } \phi \in \tilde{G}^{0}, Z \in \mathcal{V}_{x} .$$
Restricting to $\phi \in H$, (4.4) implies that $(\nabla \eta)^{\mathcal{H}}: \mathcal{V}_{x} \rightarrow \mathcal{H}_{x}$ is $H$-equivariant. Again, by the triviality of $\mathcal{H}_{x}$ and the fact that $\mathcal{V}_{x}$ has no points fixed by $H$, this yields $(\nabla \eta)^{\mathcal{H}}=0$ at $x$. \(\square\)

Recall that $B=\tilde{M}_{\infty}^{\text {prin }} / \tilde{G}^{0}$ is a connected Riemannian manifold diffeomorphic to $\mathbb{R}^{2}$.
Proposition 4.13. $\left(\tilde{M}_{\infty}^{\text {prin }}, \tilde{g}\right)$ is isometric to a warped product $\left(B \times \mathbb{S}^{2}, h+\xi^{2} g_{\mathbb{S}^{2}}\right)$, where $h$ is a metric on $B$ and $\xi: B \rightarrow(0, \infty)$ is a smooth positive function.

Proof. By [1, Remark 3.99], the quotient map $\pi: \tilde{M}_{\infty}^{\text {prin }} \rightarrow B$ is a Riemannian submersion. By Corollary 4.11, the fibers are round 2-spheres. Fix a basepoint $b_{0} \in B$ and identify $\pi^{-1}\left(b_{0}\right)$ with $\mathbb{S}^{2}$. For any $b \in B$, any smooth path $\gamma:[0,1] \rightarrow B$ with $\gamma(0)=b_{0}$ and $\gamma(1)=b$, and any $\theta \in \mathbb{S}^{2}$, let $\tilde{\gamma}:[0,1] \rightarrow \tilde{M}_{\infty}^{\text {prin }}$ be the horizontal lift of $\gamma$ starting at $\theta$. Horizontal transport along $\tilde{\gamma}$ defines a diffeomorphism $P_{\gamma}: \mathbb{S}^{2} \cong \pi^{-1}\left(b_{0}\right) \rightarrow \pi^{-1}(b)$. Since the horizontal distribution $\mathcal{H}$ is integrable by Lemma 4.12(a), $P_{\gamma}$ depends only on the homotopy class of $\gamma$. But $B \cong \mathbb{R}^{2}$ is contractible, so $P_{\gamma}$ is independent of the path $\gamma$ joining $b_{0}$ to $b$. Thus, there is a well-defined smooth map $P_{b}: \mathbb{S}^{2} \rightarrow \pi^{-1}(b)$. A global diffeomorphism is given by
$$B \times \mathbb{S}^{2} \rightarrow \tilde{M}_{\infty}^{\text {prin }}, \quad(b, \theta) \mapsto P_{b}(\theta) .$$
Under this diffeomorphism, $\mathcal{H}$ is identified with $T B$ and $\mathcal{V}$ is identified with $T \mathbb{S}^{2}$. Since $A \equiv 0$, the submanifold $B \times\{\theta\} \subset B \times \mathbb{S}^{2}$ is totally geodesic for each $\theta \in \mathbb{S}^{2}$. Moreover, for each $b^{\prime} \in B$, the submanifold $\left\{b^{\prime}\right\} \times \mathbb{S}^{2}$ corresponds to a fiber of $\pi$, which by Lemma 4.12 is spheric. We now apply [43, Proposition 3(c)] to conclude that $\left(\tilde{M}_{\infty}^{\text {prin }}, \tilde{g}\right)$ is globally a warped product. \(\square\)

The next lemma shows that under a suitable identification of $\tilde{M}_{\infty}$ with $\mathbb{R}^{4} \backslash B_{R}(0)$, the action of $\tilde{G}^{0}$ asymptotes to Euclidean rotations fixing an axis. In Corollary 4.15, we draw some consequences of this.

Lemma 4.14. There is an asymptotically Euclidean diffeomorphism $\tilde{\Phi}: \tilde{M}_{\infty} \rightarrow \mathbb{R}^{4} \backslash B_{R}(0)$ of order 4 and class $C^{100}$ (i.e. (1.1) holds only for $k \leq 100$ ) with the following properties.
\begin{itemize}
\item[(a)] $\tilde{\Psi}$ maps CMC 3-spheres in $\tilde{M}_{\infty}$ to coordinate spheres in $\mathbb{R}^{4} \backslash B_{R}(0)$.
\end{itemize}
\begin{itemize}
\item[(b)] Let $\tilde{\Psi}$ be the action of $\tilde{G}^{0}$ on $\tilde{M}_{\infty} \stackrel{\tilde{\Phi}}{\cong} \mathbb{R}^{4} \backslash B_{R}(0)$, i.e.
$$\tilde{\Psi}: \tilde{G}^{0} \times\left(\mathbb{R}^{4} \backslash B_{R}(0)\right) \rightarrow \mathbb{R}^{4} \backslash B_{R}(0), \quad \tilde{\Psi}(\phi, x)=\tilde{\Phi}\left(\phi \cdot \tilde{\Phi}^{-1}(x)\right) .$$
Also view $\mathbb{S}^{3}$ as the unit sphere in $\mathbb{R}^{4}$, and for $\rho>R$ define the rescaled actions
$$\tilde{\Psi}_{\rho}: \tilde{G}^{0} \times \mathbb{S}^{3} \rightarrow \mathbb{S}^{3}, \quad \tilde{\Psi}_{\rho}(\phi, \theta)=\rho^{-1} \tilde{\Psi}(\phi, \rho \theta) .$$
Then as $\rho \rightarrow \infty$, we have $\tilde{\Psi}_{\rho} \rightarrow \tilde{\Psi}_{\infty}$ in $C^{80}$, where
$$\tilde{\Psi}_{\infty}: \tilde{G}^{0} \times \mathbb{S}^{3} \rightarrow \mathbb{S}^{3} .$$
is the standard $S O(3)$-action on $\mathbb{S}^{3}$ induced by Euclidean rotations of $\mathbb{R}^{4}$ fixing the $w$-axis, i.e. the span of (0, 0, 0, 1).
\end{itemize}

Proof. By [10, Theorem B], there is an ALE diffeomorphism $\Phi: M \backslash K \rightarrow\left(\mathbb{R}^{4} \backslash B_{R}(0)\right) / \mathbb{Z}_{2}$ of order 4 and class $C^{100}$ which maps CMC hypersurfaces to coordinate spheres $\left(\bmod \mathbb{Z}_{2}\right)$. Lifting $\Phi$ gives an asymptotically Euclidean diffeomorphism $\tilde{\Phi}: \tilde{M}_{\infty} \rightarrow \mathbb{R}^{4} \backslash B_{R}(0)$ of order 4 and class $C^{100}$ which maps CMC 3-spheres to coordinate spheres.

Using $\tilde{\Phi}$, we define $\tilde{\Psi}$ and $\tilde{\Psi}_{\rho}$ as in the lemma. Let $\tilde{X}_{1}, \tilde{X}_{2}, \tilde{X}_{3}$ be fundamental Killing fields on $\mathbb{R}^{4} \backslash B_{R}(0)$ generating the action $\tilde{\Psi}$ and satisfying the $\mathfrak{s o}(3)$ bracket relations:
$$\left[\tilde{X}_{1}, \tilde{X}_{2}\right]=2 \tilde{X}_{3}, \quad\left[\tilde{X}_{2}, \tilde{X}_{3}\right]=2 \tilde{X}_{1}, \quad\left[\tilde{X}_{3}, \tilde{X}_{1}\right]=2 \tilde{X}_{2} .$$
Since $\left\{\tilde{X}_{i}\right\}_{i=1}^{3}$ are also fundamental Killing fields for the action of $\tilde{G}$ on $\tilde{M}_{\infty}$, which in turn lifts the action of $G$ on $M$, it follows that $\left\{\tilde{X}_{i}\right\}_{i=1}^{3}$ are lifts of fundamental Killing fields $X_{1}, X_{2}, X_{3}$ for the action of $G$ on $M$.

Although $\Phi$ is not smooth, one checks that Proposition 3.8 still holds, provided we only assert control up to say, 81 derivatives in parts (d) and (e). Indeed, parts (a)-(c) only require a small number of derivatives of ALE decay in (1.1). Thus, Proposition 3.8(e) gives linearly independent Killing fields $\left\{X_{i, \infty}\right\}_{i=1}^{3}$ on $\left(\mathbb{R} \mathbb{P}^{3}, \bar{g}_{\infty}\right)$ and $\varepsilon \in\left(0, \frac{1}{2}\right)$ such that the restrictions $X_{i, \rho}=\left.X_{i}\right|_{\partial B_{\rho}(0)}$ satisfy
$$\left\|X_{i, \rho}-X_{i, \infty}\right\|_{C^{81}\left(\mathbb{R P}^{3}, \bar{g}_{\infty}\right)} \leq \mathcal{O}\left(\rho^{-3+\varepsilon}\right) .$$
Lifting, this gives linearly independent Killing fields $\left\{\tilde{X}_{i, \infty}\right\}_{i=1}^{3}$ on $\left(\mathbb{S}^{3}, \bar{g}_{\infty}\right)$ such that the restrictions $\tilde{X}_{i, \rho}=\left.\tilde{X}_{i}\right|_{\partial B_{\rho}(0)}$ satisfy
$$\left\|\tilde{X}_{i, \rho}-\tilde{X}_{i, \infty}\right\|_{C^{81}\left(\mathbb{S}^{3}, \bar{g}_{\infty}\right)} \leq \mathcal{O}\left(\rho^{-3+\varepsilon}\right) .$$
In particular, the $\tilde{X}_{i, \infty}$ satisfy the same Lie algebra relations as (4.5), so they generate a Lie subalgebra $\mathfrak{g}_{\infty}$ of $\mathfrak{I}\left(\mathbb{S}^{3}, \bar{g}_{\infty}\right)=\mathfrak{s o}(4)$ isomorphic to $\mathfrak{s o}(3)$. The convergence (4.6), combined with standard Grönwall-type arguments, implies that the maps $\left\{\tilde{\Psi}_{\rho}\right\}_{\rho>R}$ are uniformly Cauchy in $C^{80}$. Hence, there is a smooth effective action $\tilde{\Psi}_{\infty}: \tilde{G}^{0} \times \mathbb{S}^{3} \rightarrow \mathbb{S}^{3}$ such that
$$\tilde{\Psi}_{\rho} \rightarrow \tilde{\Psi}_{\infty} \text { in } C^{80}\left(\tilde{G}^{0} \times \mathbb{S}^{3}\right) .$$
Moreover, $\tilde{\Psi}_{\infty}$ acts by isometries with respect to $\bar{g}_{\infty}$. Thus $\tilde{\Psi}_{\infty}\left(\tilde{G}^{0}, \cdot\right)$ is a subgroup of $\mathcal{I}^{0}\left(\mathbb{S}^{3}, \bar{g}_{\infty}\right)$ isomorphic to $\operatorname{SO}(3)$. By Lemma 4.3, in particular the final line of Table 1, it follows that $\tilde{\Psi}_{\infty}\left(\tilde{G}^{0}, \cdot\right)$ acts by rotations of $\mathbb{S}^{3} \subset \mathbb{R}^{4}$ fixing an axis. By composing $\tilde{\Psi}$ with a Euclidean rotation, we may assume the axis of rotation is the $w$-axis, i.e. it is spanned by $(0,0,0,1) \in \mathbb{R}^{4}$. \(\square\)

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/e5382572-8a44-4c2b-90d1-484cbf98c8e8-21.jpg?height=838&width=926&top_left_y=378&top_left_x=597}
\captionsetup{labelformat=empty}
\caption{Figure 1. Limiting action $\tilde{\Psi}_{\infty}$ of $\tilde{G}^{0} \cong S O(3)$ on $\mathbb{R}^{4}$, viewed with $w$ vertical and $x, y, z$ in the horizontal plane. The limiting action is by rotations fixing the $w$-axis; the actual action $\tilde{\Psi}$ of $\tilde{G}^{0}$ on $\tilde{M}_{\infty}$ is asymptotic to this. Examples of orbits, as well as the cones $\mathcal{C}=\left\{x^{2}+y^{2}+z^{2} \leq w^{2}\right\}$ and $\mathcal{C}^{\prime}=\left\{x^{2}+y^{2}+z^{2} \leq 3 w^{2}\right\}$ used in the proof of Corollary 4.15, are shown.}
\end{figure}

Corollary 4.15. Fix $\tilde{\Phi}: \tilde{M}_{\infty} \rightarrow \mathbb{R}^{4} \backslash B_{R}(0)$ as in Lemma 4.14, and let
$$\mathcal{C}=\left\{(x, y, z, w) \in \mathbb{R}^{4}: x^{2}+y^{2}+z^{2} \leq w^{2}\right\}, \quad \Omega=\left(\mathbb{R}^{4} \backslash B_{R}(0)\right) \backslash \mathcal{C} .$$
Then after increasing $R$ sufficiently (i.e. restricting the diffeomorphism $\tilde{\Phi}$ ), we have:
\begin{itemize}
\item[(a)] $\tilde{\Phi}^{-1}(\Omega) \subset \tilde{M}_{\infty}^{\text {prin }}$.
\item[(b)] Let $\tilde{r}$ be the Riemannian distance from a point with respect to $\tilde{g}$. On $\tilde{\Phi}^{-1}(\Omega)$, we have $A^{-1} \tilde{r} \leq \xi \leq A \tilde{r}$ for some $A>0$, and $0 \neq|d \xi|=1+\mathcal{O}\left(\tilde{r}^{-4}\right)$.
\item[(c)] Viewing $\tilde{\Phi}^{-1}(\Omega) \subset B \times \mathbb{S}^{2}$ via Proposition 4.13, it contains an open set of the form $\Omega_{B} \times \mathbb{S}^{2}$, where $\Omega_{B} \subset B$ is an open neighborhood of a forward flow line of $\nabla \xi$.
\end{itemize}
Proof. Let $\tilde{\Phi}, \tilde{\Psi}$, and $\tilde{\Psi}_{\infty}$ be as in Lemma 4.14. Moreover, extend $\tilde{\Psi}_{\infty}$ radially to act on $\mathbb{R}^{4}$; this is depicted in Figure 1. By Lemma 4.14, the action $\tilde{\Psi}$ is asymptotic to $\tilde{\Psi}_{\infty}$.

Note that all singular (i.e. non-principal) orbits of $\tilde{\Psi}_{\infty}$ lie on the $w$-axis. Therefore, outside a sufficiently large ball, all singular orbits of $\tilde{\Psi}$ are contained in a uniform tubular neighborhood of the $w$-axis, hence in $\mathcal{C}$. Thus, after increasing $R$ sufficiently, $\Omega$ contains only principal orbits. This establishes part (a) of the corollary.

For each $p=(x, y, z, w) \in \mathbb{R}^{4} \backslash B_{R}(0)$, the orbit of $p$ under $\tilde{\Psi}_{\infty}$ is a round $\mathbb{S}^{2}$ of radius $\xi_{\infty}(p)=\sqrt{x^{2}+y^{2}+z^{2}}$. In particular, along any outward Euclidean ray not parallel to the $w$-axis, the orbit radius $\xi_{\infty}$ increases at a definite linear rate. Therefore, there exists $A>0$ such that $A^{-1}|p| \leq \xi_{\infty}(p) \leq A|p|$ for all $p \in \Omega$. Thus, the same is true for the orbit radius
function $\xi$ of $\tilde{\Psi}$ outside a sufficiently large ball. This proves the first claim of part (b). As for the second claim, we calculate the vertical and horizontal components of Ric $=0$ on $\left(\tilde{M}_{\infty}^{\text {prin }} \cong B \times \mathbb{S}^{2}, \tilde{g}=h+\xi^{2} g_{\mathbb{S}^{2}}\right)$ to be
$$\begin{aligned}
\operatorname{Ric}_{h} & =2 \xi^{-1}\left(\nabla^{h}\right)^{2} \xi \\
\xi \Delta^{h} \xi+|d \xi|^{2} & =1
\end{aligned}$$
(See e.g. [7, Proposition 9.106].) Tracing (4.7) with $h$ gives $\Delta^{h} \xi=\frac{1}{2} R_{h} \xi$, where $R_{h}$ is the scalar curvature of $h$. Plugging this into (4.8) yields
$$|d \xi|^{2}=1-\frac{1}{2} R_{h} \xi^{2} .$$
Note that $\left|R_{h}\right| \leq C\left|\operatorname{Rm}_{\tilde{g}}\right|_{\tilde{g}} \leq \mathcal{O}\left(\tilde{r}^{-6}\right)$ by Theorem 3.1. Therefore, using the fact that $A^{-1} \tilde{r} \leq \xi \leq A \tilde{r}$ on $\tilde{\Phi}^{-1}(\Omega)$, we obtain
$$|d \xi|^{2}=1+\mathcal{O}\left(\tilde{r}^{-4}\right),$$
which proves the second claim of (b).
Finally, let $\Omega^{\prime}=\left(\mathbb{R}^{4} \backslash B_{R}(0)\right) \backslash \mathcal{C}^{\prime} \subset \Omega$, where $\mathcal{C}^{\prime}$ is the widened cone
$$\mathcal{C}^{\prime}=\left\{(x, y, z, w) \in \mathbb{R}^{4}: x^{2}+y^{2}+z^{2} \leq 3 w^{2}\right\} .$$
Observe that $\Omega^{\prime}$ contains $\mathbb{S}^{2}$ orbits of $\tilde{\Psi}$ which can be chosen arbitrarily far from the origin. Take one such orbit, and flow it forwards by the vector field $\nabla \xi$, which behaves like the outward Euclidean radial vector field near infinity. If the orbit was chosen sufficiently far from the origin, then its image under the flow never exits $\Omega$. Part (c) follows from these observations. \(\square\)

Corollary 4.15 allows us to use $\xi$ as a coordinate on $\Omega_{B} \times \mathbb{S}^{2}$. Since $\xi$ is constant on $\mathbb{S}^{2}$, it descends to a coordinate on $\Omega_{B}$. We now complete this to a full coordinate system using well-known arguments from the study of spherically symmetric spacetimes.

Proposition 4.16. There is a domain $\Omega_{B}^{\prime} \subset B$ which contains a forward flow line of $\nabla \xi$, and admits a coordinate system $(\xi, t): \Omega_{B}^{\prime} \rightarrow \mathbb{R}^{2}$ mapping onto an open neighborhood $D \subset \mathbb{R}^{2}$ of $(R, \infty) \times\{0\}$ (for some large $R$ ). In this coordinate system, the metric $h$ can be written
$$h=E(\xi) d \xi^{2}+F(\xi) d t^{2}$$
for some smooth positive functions $E$ and $F$.
Proof. By Proposition 4.13, Ricci-flatness, and a local version of Birkhoff's theorem (e.g. [2, Proposition 2.1]), $K:=\left({ }_{\star} d \xi\right)^{\#}$ is a Killing field on $(B, h)$ satisfying $\langle K, \nabla \xi\rangle=0$. Since $d \xi$ is nonvanishing on the set $\Omega_{B} \subset B$ from Corollary 4.15, so is $K$.

By Corollary 4.15(c), $\Omega_{B}$ contains a forward flow line $\gamma$ of $\nabla \xi$. Around each point of $\gamma$, we can use the flow of $K$ to construct a local coordinate $t$ such that $K=\partial_{t}$ and $\nabla \xi(t)=0$. If two such coordinates $t_{\alpha}, t_{\beta}$ are defined on overlapping patches, then $u=t_{\alpha}-t_{\beta}$ satisfies $K u=\nabla \xi(u)=0$ on the overlap, which we may assume to be connected. Therefore, $u$ is a constant, so by adding a constant to $t_{\beta}$, it can be made to agree with $t_{\alpha}$ on the overlap. Therefore, there is a coordinate system $(\xi, t)$ for a neighborhood $\Omega_{B}^{\prime}$ of $\gamma$ which maps to a neighborhood of $(R, \infty) \times\{0\}$ in $\mathbb{R}^{2}$ (for some large $R$ ). Since $\left\langle\partial_{\xi}, \partial_{t}\right\rangle=\left\langle\frac{\nabla \xi}{|\nabla \xi|^{2}}, K\right\rangle=0$, we can write
$$h=E(\xi, t) d \xi^{2}+F(\xi, t) d t^{2}$$
for some positive functions $E$ and $F$. Since $K$ is a Killing field, $E$ and $F$ are independent of $t$. \(\square\)

Proposition 4.17. There is a nonempty open set $U \subset \tilde{M}_{\infty}^{\text {prin }}$ on which $\tilde{g}$ is flat.
Proof. Propositions 4.13 and 4.16 imply that
$$\tilde{g}=h+\xi^{2} g_{\mathbb{S}^{2}}=E(\xi) d \xi^{2}+F(\xi) d t^{2}+\xi^{2} g_{\mathbb{S}^{2}} \quad \text { on } D \times \mathbb{S}^{2}$$
where $D(\xi, t) \subset \mathbb{R}^{2}$ is an open neighborhood of $(R, \infty) \times\{0\}$. Rudimentary computations yield
$$\left(\left(\nabla^{h}\right)^{2} \xi\right)_{\xi \xi}=-\frac{E^{\prime}}{2 E}, \quad\left(\left(\nabla^{h}\right)^{2} \xi\right)_{t t}=\frac{F^{\prime}}{2 E} .$$
Meanwhile, since $B$ is 2-dimensional, (4.7) gives
$$\left(\nabla^{h}\right)^{2} \xi=\frac{1}{2} \xi \operatorname{Ric}_{h}=\frac{1}{4} \xi R_{h} h .$$
Combining this with (4.10) and then isolating $\frac{1}{2} \xi R_{h}$ in both equations, we obtain
$$\frac{F^{\prime}}{E F}=\frac{1}{2} \xi R_{h}=-\frac{E^{\prime}}{E^{2}} .$$
This implies $(\log (E F))^{\prime}=0$, so $E=\frac{c}{F}$ for some $c>0$. Thus, additionally defining $V(\xi)=F(\xi) / c$ and $\tau=\sqrt{c} t$, (4.9) becomes
$$\tilde{g}=\frac{1}{V(\xi)} d \xi^{2}+V(\xi) d \tau^{2}+\xi^{2} g_{\mathbb{S}^{2}} \quad \text { on } D^{\prime} \times \mathbb{S}^{2}$$
where $D^{\prime}(\xi, \tau) \subset \mathbb{R}^{2}$ is an open neighborhood of $(R, \infty) \times\{0\}$. Next, using [7, Proposition 9.106], along the spherical direction we have
$$\left.\operatorname{Ric}_{\tilde{g}}\right|_{T \mathbb{S}^{2}}=\left(1-\xi \Delta^{h} \xi-|\nabla \xi|^{2}\right) g_{\mathbb{S}^{2}} .$$
Straightforward computation using (4.11) gives $|\nabla \xi|^{2}=V$ and $\Delta^{h} \xi=V^{\prime}$. Inserting this into (4.12), imposing $\left.\operatorname{Ric}_{\tilde{g}}\right|_{T \mathbb{S}^{2}}=0$, and solving the resulting ODE gives
$$V(\xi)=1-\frac{2 \mu}{\xi} \quad \text { for some } \mu \in \mathbb{R}$$
Thus, $\tilde{g}$ is the Euclidean Schwarzschild metric with mass $\mu$ on $D^{\prime} \times \mathbb{S}^{2}$. Suppose $\mu \neq 0$. If we fix some $\theta \in \mathbb{S}^{2}$ and consider the curve $\xi \mapsto(\xi, 0, \theta) \in D^{\prime} \times \mathbb{S}^{2}$, then $\left|\operatorname{Rm}_{\tilde{g}}\right| \asymp \xi^{-3}$ as $\xi \rightarrow \infty$ (a standard fact about Euclidean Schwarzschild metrics with nonzero mass). By Corollary $4.15, \xi$ is comparable to the Riemannian distance $\tilde{r}$ from a point with respect to $\tilde{g}$. Thus, $\left|\operatorname{Rm}_{\tilde{g}}\right| \asymp \tilde{r}^{-3}$ along the same curve. However, recall from the discussion after Corollary 4.8 that $\tilde{g}$ is asymptotically Euclidean of order 4. So $\left|\operatorname{Rm}_{\tilde{g}}\right| \leq \mathcal{O}\left(\tilde{r}^{-6}\right)$, but this is a contradiction. Therefore $\mu=0$, which makes $\tilde{g}$ flat in $D^{\prime} \times \mathbb{S}^{2}$. \(\square\)

We may now finish off Case (B). By Proposition 4.17, the downstairs metric $g$ is flat in an open set of $M$. Since Ricci-flat metrics are real-analytic, unique continuation implies that $(M, g)$ is flat everywhere. Hence, $(M, g)$ must be the flat orbifold $\mathbb{R}^{4} / \mathbb{Z}_{2}$. This concludes Case (B) and hence the proof of Theorem 1.2.

\section*{5. A characterization of Calabi space}

In this section, we prove Theorem 1.4.
5.1. Homogeneous metrics on $\mathbb{S}^{2 m-1} / \mathbb{Z}_{m}$ and isometry groups. We begin by importing several facts from [34, §5] regarding homogeneous metrics on $\mathbb{S}^{2 m-1} / \mathbb{Z}_{m}$ and their isometry groups. Recall from §2.3 that $\mathbb{S}^{2 m-1} / \mathbb{Z}_{m}$ is the lens space obtained by quotienting $\mathbb{S}^{2 m-1}$ by a $\mathbb{Z}_{m}$ subgroup of Hopf rotations.

Lemma 5.1 ([34, Lemma 5.3]). If $\mathfrak{g}$ is a Lie subalgebra of $\mathfrak{u}(m)$ satisfying
$$\operatorname{dim} \mathfrak{g} \geq m^{2}-2 m+3,$$
then either $\mathfrak{g}=\mathfrak{s u}(m)$ or $\mathfrak{g}=\mathfrak{u}(m)$. If $m=4$ we also allow $\mathfrak{g}=\mathfrak{s p}(2) \oplus \mathfrak{u}(1)$ (up to conjugacy in $\mathfrak{u}(4)$ ).

For the next result, recall the definition of $d_{1}$ stated before Lemma 3.11. As before, $\bar{g}_{\infty}$ denotes the metric of constant sectional curvature 1.

Proposition 5.2 ([34, Proposition 5.4]). We have $d_{1}\left(\mathbb{S}^{2 m-1} / \mathbb{Z}_{m}, \bar{g}_{\infty}\right) \geq 2 m-3$.
Next, we recall the quotient-Berger metrics $\left\{g_{a, b}\right\}_{a, b>0}$ on $\mathbb{S}^{2 m-1} / \mathbb{Z}_{m}$ defined in §2.3. The following result characterizes such metrics on $\mathbb{S}^{2 m-1} / \mathbb{Z}_{m}$ in terms of isometry group dimensions.

Proposition 5.3 ([34, Proposition 5.5]). If $g$ is a homogeneous metric on $\mathbb{S}^{2 m-1} / \mathbb{Z}_{m}$ with
$$\operatorname{dim} \mathcal{I}\left(\mathbb{S}^{2 m-1} / \mathbb{Z}_{m}, g\right) \geq \begin{cases}m^{2}-2 m+3 & \text { if } m=3 \text { or } m \geq 5, \\ 14 & \text { if } m=4,\end{cases}$$
then $g=g_{a, b}$ for some $a, b>0$. Thus $\mathcal{I}^{0}\left(\mathbb{S}^{2 m-1} / \mathbb{Z}_{m}, g\right)=U(m) / \mathbb{Z}_{m}$, and the isotropy subgroup of its action is the image of $U(m-1) \times \mathbb{Z}_{m}$ under the quotient map $U(m) \rightarrow$ $U(m) / \mathbb{Z}_{m}$.

Lemma 5.4 ([34, obtained by combining Lemma 5.7 and Corollary 5.8]). If $K$ is a closed subgroup of $S U(m)$ containing $S\left(U(m-1) \times \mathbb{Z}_{m}\right)$, and $K / S\left(U(m-1) \times \mathbb{Z}_{m}\right)$ is diffeomorphic to a spherical space form of dimension $\ell \geq 0$, then $K$ is one of $S\left(U(m-1) \times \mathbb{Z}_{2 m}\right)$, $S(U(m-1) \times U(1))$, or $S U(m)$.

Lemma 5.5 ([34, Lemma 5.9]). Any $S U(m)$-invariant metric on $S U(m) / S\left(U(m-1) \times \mathbb{Z}_{m}\right) \cong$ $\mathbb{S}^{2 m-1} / \mathbb{Z}_{m}$ is equal to $g_{a, b}$ for some $a, b>0$.
5.2. Symmetry reduction and the flat case of Theorem 1.4. The next result was also proved in [34, §5] (specifically Corollary 5.6 there), but since it also depends on previous sections, we will write out the proof to avoid excessive cross-referencing.

Corollary 5.6. Let $\left(M^{2 m}, g, J\right)$ be a complete Ricci-flat Kähler ALE space of complex dimension $m \geq 3$ with group at infinity $\mathbb{Z}_{m}$ and satisfying (1.3). Then the group $S U(m)$ acts smoothly, almost effectively, and isometrically with cohomogeneity one on $(M, g)$. The principal isotropy subgroup is $S\left(U(m-1) \times \mathbb{Z}_{m}\right)$.
Proof. We have $\mathcal{I}^{0}\left(\mathbb{S}^{2 m-1} / \mathbb{Z}_{m}, \bar{g}_{\infty}\right)=U(m) / \mathbb{Z}_{m}$, whose dimension is $\bar{d}=m^{2}$. Thus, by Proposition 3.8 and the remarks after it, there is a Lie subalgebra $\mathfrak{g}$ of Killing fields on $(M, g)$ with
$$\operatorname{dim} \mathfrak{g} \geq \bar{d}-\operatorname{dim} \operatorname{ker}_{L^{2}}\left(\Delta_{L}\right) \geq \begin{cases}m^{2}-2 m+3 & \text { if } m=3 \text { or } m \geq 5, \\ 14 & \text { if } m=4,\end{cases}$$
which for large $\rho$ restricts to a Lie algebra $\mathfrak{g}_{\rho}$ of Killing fields on the CMC leaves $\left(\mathbb{S}^{2 m-1} / \mathbb{Z}_{m}, g_{\rho}\right)$. These Lie algebras integrate to connected Lie groups $G \subseteq \mathcal{I}^{0}(M, g)$ and $G_{\rho} \subseteq \mathcal{I}^{0}\left(\mathbb{S}^{2 m-1} / \mathbb{Z}_{m}, g_{\rho}\right)$ with dimensions also lower-bounded as in (5.1).

Proposition 5.2 implies $\operatorname{dim} \operatorname{ker}_{L^{2}}\left(\Delta_{L}\right) \leq d_{1}\left(\mathbb{S}^{2 m-1} / \mathbb{Z}_{m}, \bar{g}_{\infty}\right)$. Hence, Lemma 3.11 implies that $\mathfrak{g}_{\rho}$ spans the tangent space to $\mathbb{S}^{2 m-1} / \mathbb{Z}_{m}$ at any point if $\rho$ is sufficiently large. Hence, $\left(\mathbb{S}^{2 m-1} / \mathbb{Z}_{m}, g_{\rho}\right)$ is homogeneous with $\operatorname{dim} \mathcal{I}\left(\mathbb{S}^{2 m-1} / \mathbb{Z}_{m}, g_{\rho}\right)$ also lower bounded by (5.1).

By Proposition 5.3, we have $g_{\rho}=g_{a, b}$ for some $a, b>0$. Moreover, the transitive action of $\mathcal{I}^{0}\left(\mathbb{S}^{2 m-1} / \mathbb{Z}_{m}, g_{\rho}\right)=U(m) / \mathbb{Z}_{m}$ has isotropy subgroup given by the image of $U(m-1) \times \mathbb{Z}_{m}$ under the quotient map $U(m) \rightarrow U(m) / \mathbb{Z}_{m}$. Since $\mathfrak{g}_{\rho} \subseteq \mathfrak{I}\left(\mathbb{S}^{2 m-1} / \mathbb{Z}_{m}, g_{\rho}\right)=\mathfrak{u}(m)$ and the lower bound (5.1) holds for $\operatorname{dim} \mathfrak{g}_{\rho}$, Lemma 5.1 implies that $\mathfrak{g}_{\rho} \in\{\mathfrak{s} \mathfrak{u}(m), \mathfrak{u}(m)\}$ (the $\mathfrak{s p}(2) \oplus \mathfrak{u}(1)$ case when $m=4$ is excluded by dimension). Hence, the integrated subgroup $G_{\rho} \subseteq \mathcal{I}^{0}\left(\mathbb{S}^{2 m-1} / \mathbb{Z}_{m}, g_{\rho}\right)$ is the image of either $S U(m)$ or $U(m)$ under the quotient map $U(m) \rightarrow U(m) / \mathbb{Z}_{m}$. We consider these cases separately.

In the former case, $G_{\rho}$ still acts transitively on $\left(\mathbb{S}^{2 m-1} / \mathbb{Z}_{m}, g_{\rho}\right)$ with isotropy subgroup $H$ given by the image of $S\left(U(m-1) \times \mathbb{Z}_{m}\right)$ under the same quotient map. Then Lemma 3.10 shows that $G$ acts smoothly, isometrically, and effectively on $(M, g)$, and the restriction map $G \rightarrow G_{\rho}$ is an isomorphism. Transitivity of $G_{\rho}$ on $\left(\mathbb{S}^{2 m-1} / \mathbb{Z}_{m}, g_{\rho}\right)$ implies that $G$ acts by cohomogeneity one on $(M, g)$ with principal isotropy subgroup $H$. By undoing the $\mathbb{Z}_{m}$ quotients in the groups $G$ and $H$, the action of $G$ on $(M, g)$ becomes almost effective, and the corollary follows in this case.

In the latter case, $G_{\rho}$ acts transitively on $\left(\mathbb{S}^{2 m-1} / \mathbb{Z}_{m}, g_{\rho}\right)$ with isotropy subgroup $H$ given by the image of $U(m-1) \times \mathbb{Z}_{m}$ under the quotient map $U(m) \rightarrow U(m) / \mathbb{Z}_{m}$. As in the last paragraph, $G \cong G_{\rho}$ acts by cohomogeneity one on $(M, g)$ with principal isotropy subgroup $H$. Undoing the $\mathbb{Z}_{m}$ quotients, the corollary holds with $S U(m)$ replaced by $U(m)$ and $S\left(U(m-1) \times \mathbb{Z}_{m}\right)$ replaced by $U(m-1) \times \mathbb{Z}_{m}$. Nonetheless, by restricting this $U(m)$-action to $S U(m)$, the resulting action remains transitive on the CMC leaves. Therefore, the corollary still holds as stated. \(\square\)

We now sharpen Corollary 5.6; the following analysis is similar to that of §4.3.
Proposition 5.7. Let $\left(M^{2 m}, g, J\right)$ be a complete Ricci-flat Kähler ALE space of complex dimension $m \geq 3$ with group at infinity $\mathbb{Z}_{m}$, and with orbifold singular set of real codimension at least 4. Suppose also that (1.3) holds. Then exactly one of (A) or (B) below is true:
\begin{itemize}
\item[(A)] $M$ is diffeomorphic to the total space of the complex line bundle $\mathcal{O}_{\mathbb{C P}^{m-1}}(-m)$. Moreover, identifying the complement of the zero section with $(0, \infty) \times \mathbb{S}^{2 m-1} / \mathbb{Z}_{m}$, we have $g=d s^{2}+g_{a(s), b(s)}$ where $a$ and $b$ are positive analytic functions with boundary conditions $a(0)=0, a^{\prime}(0)=m, b(0)>0$, and $b^{\prime}(0)=0$.
\item[(B)] $(M, g, J)$ is biholomorphically isometric to the flat Kähler orbifold $\mathbb{C}^{m} / \mathbb{Z}_{m}$.
\end{itemize}

Proof. Let $G=S U(m)$ and $H=S\left(U(m-1) \times \mathbb{Z}_{m}\right)$. By Corollary 5.6 and Proposition 3.12, we get the following.
\begin{itemize}
\item[(i)] Outside a submanifold $X$, we can identify
$$(M \backslash X, g)=\left((0, \infty) \times G / H, d s^{2}+g(s)\right),$$
where $\{g(s)\}_{s>0}$ are $G$-invariant metrics on a fixed copy of $G / H \cong \mathbb{S}^{2 m-1} / \mathbb{Z}_{m}$.
\item[(ii)] There is a closed subgroup $K$ of $G$ strictly containing $H$ such that $X$ is diffeomorphic to $G / K$, and $K / H$ is diffeomorphic to a spherical space form of dimension $\ell \geq 0$.
\item[(iii)] From the description of $(M, g)$ as a bundle over $X$, the metric spaces $(G / H, g(s))$ converge in the Hausdorff sense to $X$ as $s \rightarrow 0$.
\end{itemize}
From (i) and Lemma 5.5, we have $g(s)=g_{a(s), b(s)}$ for some positive functions $a, b:(0, \infty) \rightarrow$ $(0, \infty)$. By Ricci-flatness, $a$ and $b$ must be analytic. By (ii) and Lemma 5.4, there are three possibilities for $K$ and $X \cong G / K$ :
\begin{itemize}
\item[(a)] $K=S\left(U(m-1) \times \mathbb{Z}_{2 m}\right)$ and $X \cong \mathbb{S}^{2 m-1} / \mathbb{Z}_{2 m}$.
\item[(b)] $K=S(U(m-1) \times U(1))$ and $X \cong \mathbb{C P}^{m-1}$.
\item[(c)] $K=S U(m)$ and $X$ is a point.
\end{itemize}
However, the first option is incompatible with (iii) because it is impossible for $\left(G / H, g_{a(s), b(s)}\right)$ to converge in the Hausdorff sense to a metric space homeomorphic to $\mathbb{S}^{2 m-1} / \mathbb{Z}_{2 m}$. Indeed, any change in topology must arise from sending $a(s)$ or $b(s)$ to zero, which necessarily results in a dimension drop. Hence we are left with two possibilities:
\begin{itemize}
\item[-] If $X \cong \mathbb{C P}^{m-1}$, then $M$ is a smooth manifold. Indeed, either all points in the orbit $X$ are orbifold points, or they are all smooth points. Since $\operatorname{codim}_{M}(X)=2$, and $M$ has orbifold singular set of codimension at least 4, the latter must be true. As the principal part $(0, \infty) \times G / H$ is already smooth, it follows that $M$ is smooth. By construction, $M$ is diffeomorphic to $\mathcal{O}_{\mathbb{C P}^{m-1}}(-m)$.
By (i) and the above discussion, the metric outside $X$ is $g=d s^{2}+g_{a(s), b(s)}$. For the metric to degenerate to an $X \cong \mathbb{C P}^{m-1}$ at $s=0$, we need $a(s) \rightarrow 0$ and $b(s) \rightarrow b(0)>0$ as $s \rightarrow 0$. For the metric to remain smooth at $X$, we require that $a^{\prime}(0)=m$ and $b^{\prime}(0)=0$. This gives part (a) of the proposition.
\item[-] If $X$ is a point, then $M$ is diffeomorphic to the orbifold $\mathbb{C}^{m} / \mathbb{Z}_{m}$. Its universal orbifold cover is a complete Ricci-flat Kähler asymptotically Euclidean manifold $\left(\mathbb{C}^{m}, \tilde{g}, \tilde{J}\right)$. By the sharp case of the Bishop-Gromov theorem, $\tilde{g}$ is the Euclidean metric. Kählerity then necessitates that $\left(\mathbb{C}^{m}, \tilde{g}, \tilde{J}\right)$ is biholomorphically isometric to the standard $\mathbb{C}^{m}$.
\end{itemize} \(\square\)

Case (B) of Proposition 5.7 establishes the flat $\mathbb{C}^{m} / \mathbb{Z}_{m}$ case of Theorem 1.4. It remains to characterize $(M, g, J)$ as the Calabi space in case (A). So far, the metric is of the correct form, but more needs to be said about the complex structure. We do this in the next subsection and then finish the proof of Theorem 1.4.
5.3. The non-flat case of Theorem 1.4. For the rest of this section, assume that $\left(M^{2 m}, g, J\right)$ is as in case (A) of Proposition 5.7. Thus, outside the central $\mathbb{C} \mathbb{P}^{m-1}$ we have
$$g=d s^{2}+g_{a(s), b(s)}=d s^{2}+a(s)^{2} \sigma \otimes \sigma+b(s)^{2} \pi^{*} g_{\mathrm{FS}},$$
where $a$ and $b$ are positive analytic functions on ( $0, \infty$ ). Write $M^{\text {prin }}=M \backslash \mathbb{C P}^{m-1}$. The projection $\pi: \mathbb{S}^{2 m-1} / \mathbb{Z}_{m} \rightarrow \mathbb{C P}^{m-1}$ induces a Riemannian submersion
$$\tilde{\pi}:\left(M^{\text {prin }}, g\right) \rightarrow\left((0, \infty) \times \mathbb{C} \mathbb{P}^{m-1}, d s^{2}+b(s)^{2} g_{\mathrm{FS}}\right) .$$
Let $\xi$ be the vector field algebraically dual to $\sigma$, so that $\sigma(\xi)=1$. Then $U=\frac{1}{a(s)} \xi$ is a unit vector field tangential to the Hopf fibers. Fixing a point $x \in M^{\text {prin }}$, we may decompose
$$T_{x} M=\mathcal{P}_{x} \oplus \mathcal{P}_{x}^{\perp},$$
where $\mathcal{P}_{x}=\tilde{\pi}^{*}\left(T_{\tilde{\pi}(x)} \mathbb{C} \mathbb{P}^{m-1}\right)$ is the horizontal lift of $T_{\tilde{\pi}(x)} \mathbb{C} \mathbb{P}^{m-1}$, and $\mathcal{P}_{x}^{\perp}=\operatorname{span}\left\{\partial_{s}, U\right\}$ is its orthogonal complement. Note that the horizontal subspace at $x$ of the Riemannian submersion $\tilde{\pi}$ is $\mathcal{P}_{x} \oplus \operatorname{span}\left\{\partial_{s}\right\}$, and the vertical subspace at $x$ is $\operatorname{span}\{U\}$.

Below, we denote by $I=\tilde{\pi}^{*} J_{\mathrm{FS}}$ the horizontal lift of the complex structure on $\mathbb{C P}^{m-1}$. Note that $I$ vanishes on $\partial_{s}$, so it restricts to a complex structure on $\mathcal{P}_{x}$. We will prove the following characterization of $J$ :

Lemma 5.8. At all points $x$ in a dense open subset of $M^{\text {prin }}$, we have $J=\varepsilon_{\mathcal{P}} I+\varepsilon_{\mathcal{P} \perp} J_{\perp}$ for some $\varepsilon_{\mathcal{P}}, \varepsilon_{\mathcal{P}^{\perp}} \in\{1,-1\}$, where $J_{\perp}$ is defined by
$$J_{\perp}\left(\partial_{s}\right)=U, \quad J_{\perp}(U)=-\partial_{s}, \quad J_{\perp}\left(\mathcal{P}_{x}\right)=0 .$$

This will be proved by commuting curvature operators with $J$. Below, for $X, Y \in T_{x} M$, the operator $X \wedge Y \in \mathfrak{s o}\left(T_{x} M\right)$ is defined by $(X \wedge Y)(Z)=\langle Y, Z\rangle X-\langle X, Z\rangle Y$.

Lemma 5.9. Let $x \in M^{\text {prin }}$. For each $X, Y, Z \in \mathcal{P}_{x}$, we have
$$\begin{aligned}
\operatorname{Rm}(X, Y) \partial_{s} & =\left(\frac{2 a b^{\prime}}{b^{3}}-\frac{2 a^{\prime}}{b^{2}}\right)\langle I X, Y\rangle U \\
\operatorname{Rm}(X, Y) U & =-\left(\frac{2 a b^{\prime}}{b^{3}}-\frac{2 a^{\prime}}{b^{2}}\right)\langle I X, Y\rangle \partial_{s}
\end{aligned}$$
$$\begin{aligned}
\operatorname{Rm}(X, Y) Z= & \frac{\left(b^{\prime}\right)^{2}-1}{b^{2}}(X \wedge Y)(Z)+\left(\frac{a^{2}}{b^{4}}-\frac{1}{b^{2}}\right)(I X \wedge I Y)(Z) \\
& +\left(\frac{2}{b^{2}}-\frac{2 a^{2}}{b^{4}}\right)\langle I X, Y\rangle I Z,
\end{aligned}$$
$$\operatorname{Rm}\left(\partial_{s}, U\right) \partial_{s}=-\frac{a^{\prime \prime}}{a} U,$$
$$\operatorname{Rm}\left(\partial_{s}, U\right) U=\frac{a^{\prime \prime}}{a} \partial_{s},$$
$$\operatorname{Rm}\left(\partial_{s}, U\right) X=\left(\frac{2 a b^{\prime}}{b^{3}}-\frac{2 a^{\prime}}{b^{2}}\right) I X .$$
In particular, $\operatorname{Rm}\left(\partial_{s}, U\right)$ and $\operatorname{Rm}(X, Y)$ both preserve the splitting $T_{x} M=\mathcal{P}_{x} \oplus \mathcal{P}_{x}^{\perp}$.
Proof. Let $X, Y, Z, W \in \mathcal{P}_{x}$. Applying O'Neill's formulae [41] to the Riemannian submersion $\tilde{\pi}$, we have
$$\begin{aligned}
\left\langle\operatorname{Rm}(X, Y) \partial_{s}, U\right\rangle & =\left\langle\left(\nabla_{\partial_{s}} A\right)_{X} Y, U\right\rangle+\left\langle A_{X} Y, T_{U} \partial_{s}\right\rangle-\left\langle A_{Y} \partial_{s}, T_{U} X\right\rangle-\left\langle A_{\partial_{s}} X, T_{U} Y\right\rangle, \\
\langle\operatorname{Rm}(X, Y) Z, U\rangle & =\left\langle\left(\nabla_{Z} A\right)_{X} Y, U\right\rangle+\left\langle A_{X} Y, T_{U} Z\right\rangle-\left\langle A_{Y} Z, T_{U} X\right\rangle-\left\langle A_{Z} X, T_{U} Y\right\rangle,
\end{aligned}$$
$$\begin{aligned}
& \left\langle\operatorname{Rm}(X, Y) Z, \partial_{s}\right\rangle=\left\langle\operatorname{Rm}^{\tilde{\pi}}(X, Y) Z, \partial_{s}\right\rangle-2\left\langle A_{X} Y, A_{Z} \partial_{s}\right\rangle+\left\langle A_{Y} Z, A_{X} \partial_{s}\right\rangle+\left\langle A_{Z} X, A_{Y} \partial_{s}\right\rangle, \\
& \langle\operatorname{Rm}(X, Y) Z, W\rangle=\left\langle\operatorname{Rm}^{\tilde{\pi}}(X, Y) Z, W\right\rangle-2\left\langle A_{X} Y, A_{Z} W\right\rangle+\left\langle A_{Y} Z, A_{X} W\right\rangle+\left\langle A_{Z} X, A_{Y} W\right\rangle,
\end{aligned}$$
where $\operatorname{Rm}^{\tilde{\pi}}(X, Y) Z=\tilde{\pi}^{*}\left(\operatorname{Rm}_{0}\left(\tilde{\pi}_{*} X, \tilde{\pi}_{*} Y\right) \tilde{\pi}_{*} Z\right)$ and $\operatorname{Rm}_{0}$ is the curvature of the base manifold of $\tilde{\pi}$. The tensors $A$ and $T$ are defined as follows: for $E, F \in \mathcal{P}_{x}$, we arbitrarily extend them to $\mathcal{P}$-valued vector fields around $x$ denoted by the same letters, and define
$$A_{E} F=\frac{1}{2}\langle[E, F], U\rangle U, \quad T_{U} E=\left\langle\nabla_{U} E, U\right\rangle U .$$
Meanwhile, we let
$$A_{E} \partial_{s}=\frac{1}{2}\left\langle\left[E, \partial_{s}\right], U\right\rangle U, \quad T_{U} \partial_{s}=\left\langle\nabla_{U} \partial_{s}, U\right\rangle U .$$
We will now compute all the $A$ and $T$ combinations appearing above. Below, we extend $X \in \mathcal{P}_{x}$ to a local $\mathcal{P}$-valued vector field by first extending in the $\partial_{s}$ direction with $\left[\partial_{s}, X\right]=0$,
then horizontally lifting in the $\xi$ direction so that $[\xi, X]=0$. It follows that
$$[U, X]=\frac{1}{a(s)}[\xi, X]-X\left(\frac{1}{a(s)}\right) \xi=0$$
We do the same for $Y, Z \in \mathcal{P}_{x}$.
Firstly, since $\left[X, \partial_{s}\right]=0$, we have
$$A_{X} \partial_{s}=0 .$$
Next, since $U=\frac{1}{a} \xi$ where $\xi$ is algebraically dual to $\sigma$, and $\sigma(X)=\sigma(Y)=0$, we have $A_{X} Y=\frac{a}{2} \sigma([X, Y]) U=-\frac{a}{2} d \sigma(X, Y) U$. Combined with the fact that $d \sigma=2 \pi^{*} \omega_{\mathrm{FS}}=$ $2 \pi^{*} g_{\mathrm{FS}}\left(J_{\mathrm{FS}}(\cdot), \cdot\right)$ for the Hopf fibration $\pi: \mathbb{S}^{2 m-1} / \mathbb{Z}_{m} \rightarrow \mathbb{C P}^{m-1}$, this implies
$$A_{X} Y=-\frac{a}{b^{2}}\langle I X, Y\rangle U$$
where we recall that $I:=\tilde{\pi}^{*} J_{\mathrm{FS}}$. Since $\left(\mathbb{C P}^{m-1}, g_{\mathrm{FS}}, J_{\mathrm{FS}}\right)$ is Kähler and $\tilde{\pi}$ is a Riemannian submersion, we have $\left\langle\left(\nabla_{Z} I\right) X, Y\right\rangle=0$. Differentiating (5.10) gives
$$\nabla_{Z}\left(A_{X} Y\right)=-\frac{a}{b^{2}}\left[\left\langle I\left(\nabla_{Z} X\right), Y\right\rangle U+\left\langle I X, \nabla_{Z} Y\right\rangle U+\langle I X, Y\rangle \nabla_{Z} U\right],$$
which implies that
$$\left(\nabla_{Z} A\right)_{X} Y=\nabla_{Z}\left(A_{X} Y\right)-A_{\nabla_{Z} X} Y-A_{X}\left(\nabla_{Z} Y\right)=-\frac{a}{b^{2}}\langle I X, Y\rangle \nabla_{Z} U .$$
Likewise, since $\nabla_{\partial_{s}} X=\frac{b^{\prime}}{b} X$ and $\nabla_{\partial_{s}} Y=\frac{b^{\prime}}{b} Y$, we compute
$$\left(\nabla_{\partial_{s}} A\right)_{X} Y=\nabla_{\partial_{s}}\left(A_{X} Y\right)=-\left(\frac{a}{b^{2}}\right)^{\prime}\langle I X, Y\rangle U-\frac{a}{b^{2}}\langle I X, Y\rangle \nabla_{\partial_{s}} U .$$
Next, since $[U, X]=0$ and $U$ has unit length, we have
$$T_{U} X=\left\langle\nabla_{U} X, U\right\rangle U=\left\langle\nabla_{X} U, U\right\rangle U=\frac{1}{2} X|U|^{2}=0 .$$
Meanwhile, since $\left[\xi, \partial_{s}\right]=0$ and $U=\frac{1}{a} \xi$, we have
$$T_{U} \partial_{s}=\frac{1}{a^{2}}\left\langle\nabla_{\xi} \partial_{s}, \xi\right\rangle U=\frac{1}{a^{2}}\left\langle\nabla_{\partial_{s}} \xi, \xi\right\rangle U=\frac{1}{2 a^{2}} \partial_{s}|\xi|^{2} U=\frac{a^{\prime}}{a} U .$$

We take all the computations between (5.9) and (5.11), and substitute them back into O'Neill's formulas stated at the beginning of the proof. We also use $\left\langle\nabla_{(\cdot)} U, U\right\rangle=0$ repeatedly since $U$ is a unit vector field. This gives
$$\begin{aligned}
\left\langle\operatorname{Rm}(X, Y) \partial_{s}, U\right\rangle= & \left(-\left(\frac{a}{b^{2}}\right)^{\prime}-\frac{a^{\prime}}{b^{2}}\right)\langle I X, Y\rangle=\left(\frac{2 a b^{\prime}}{b^{3}}-\frac{2 a^{\prime}}{b^{2}}\right)\langle I X, Y\rangle, \\
\langle\operatorname{Rm}(X, Y) Z, U\rangle= & 0, \\
\left\langle\operatorname{Rm}(X, Y) Z, \partial_{s}\right\rangle= & \left\langle\operatorname{Rm}^{\tilde{\pi}}(X, Y) Z, \partial_{s}\right\rangle=0, \\
\langle\operatorname{Rm}(X, Y) Z, W\rangle= & \left\langle\operatorname{Rm}^{\tilde{\pi}}(X, Y) Z, W\right\rangle-\frac{2 a^{2}}{b^{4}}\langle I X, Y\rangle\langle I Z, W\rangle \\
& +\frac{a^{2}}{b^{4}}\langle I Y, Z\rangle\langle I X, W\rangle+\frac{a^{2}}{b^{4}}\langle I Z, X\rangle\langle I Y, W\rangle .
\end{aligned}$$
The first three equations, together with the symmetries of the curvature tensor, imply (5.3), (5.4), and (5.8). Meanwhile, the last three equations imply
$$\operatorname{Rm}(X, Y) Z=\operatorname{Rm}^{\tilde{\pi}}(X, Y) Z-\frac{2 a^{2}}{b^{4}}\langle I X, Y\rangle I Z+\frac{a^{2}}{b^{4}}(I X \wedge I Y)(Z) .$$

Since the base manifold of (5.2) is itself a warped product, we use the formulae for the curvature of a warped product and the Fubini-Study metric (e.g. [30, §IX.7]) to get
$$\begin{aligned}
\operatorname{Rm}^{\tilde{\pi}}(X, Y) Z & =\tilde{\pi}^{*}\left(\operatorname{Rm}_{0}\left(\pi_{*} X, \pi_{*} Y\right) \pi_{*} Z\right)+\frac{\left(b^{\prime}\right)^{2}}{b^{2}}(X \wedge Y)(Z) \\
& =\left(\frac{\left(b^{\prime}\right)^{2}-1}{b^{2}}\right)(X \wedge Y)(Z)+\frac{2}{b^{2}}\langle I X, Y\rangle I Z-\frac{1}{b^{2}}(I X \wedge I Y)(Z) .
\end{aligned}$$
Combining (5.12) and (5.13), we arrive at (5.5).
Finally, the identities $\left[\xi, \partial_{s}\right]=0$ and $U=\frac{1}{a} \xi$ imply that $\left[U, \partial_{s}\right]=-\frac{a^{\prime}}{a} U$. Since $\nabla_{\partial_{s}} \partial_{s}=0$ and $\nabla_{\partial_{s}} X=\frac{b^{\prime}}{b} X$ is orthogonal to $U$, we get $\nabla_{\partial_{s}} U=0$. Thus, $\nabla_{U} \partial_{s}=-\left[\partial_{s}, U\right]=\frac{a^{\prime}}{a} U$. These identities yield (after simplification)
$$\operatorname{Rm}\left(\partial_{s}, U\right) \partial_{s}=\nabla_{U} \nabla_{\partial_{s}} \partial_{s}-\nabla_{\partial_{s}} \nabla_{U} \partial_{s}+\nabla_{\left[\partial_{s}, U\right]} \partial_{s}=-\frac{a^{\prime \prime}}{a} U,$$
which implies (5.6) and (5.7). \(\square\)

Note that $I$ turns $\mathcal{P}_{x} \cong T_{x} \mathbb{C} \mathbb{P}^{m-1}$ into a complex vector space, and together with the metric $g=\langle\cdot, \cdot\rangle$ it induces a Hermitian inner product $(X, Y) \mapsto\langle X, Y\rangle+i\langle X, I Y\rangle$. Denote by $U\left(\mathcal{P}_{x}, I, g\right)$ the group of linear transformations on the complex vector space $\left(\mathcal{P}_{x}, I\right)$ which preserve this Hermitian inner product, and $S U\left(\mathcal{P}_{x}, I, g\right)$ the subgroup of those with determinant 1 . Let $\mathfrak{u}\left(\mathcal{P}_{x}, I, g\right)$ and $\mathfrak{s} \mathfrak{u}\left(\mathcal{P}_{x}, I, g\right)$ be their Lie algebras.

Corollary 5.10. For all $x$ in a dense open subset of $M^{\text {prin }}$, there are Lie subalgebras $\mathfrak{h} \subset \mathfrak{k}$ of $\mathfrak{s o}\left(T_{x} M\right)$ such that
\begin{itemize}
\item[(i)] Each map in $\mathfrak{k}$ is a linear combination of maps of the form $\operatorname{Rm}(V, W)$ where $V, W \in$ $T_{x} M$.
\item[(ii)] Each map in $\mathfrak{k}$ preserves the decomposition $T_{x} M=\mathcal{P}_{x} \oplus \mathcal{P}_{x}^{\perp}$.
\item[(iii)] $\mathfrak{k}$ acts on $\mathcal{P}_{x}$ as the standard representation of $\mathfrak{u}\left(\mathcal{P}_{x}, I, g\right)$.
\item[(iv)] $\mathfrak{h}$ acts on $\mathcal{P}_{x}^{\perp}$ trivially, and acts on $\mathcal{P}_{x}$ as the standard representation of $\mathfrak{s} \mathfrak{u}\left(\mathcal{P}_{x}, I, g\right)$.
\end{itemize}

Proof. Let $\left\{e_{j}\right\}_{j=1}^{m-1}$ be a unitary orthonormal basis for $\left(\mathcal{P}_{x}, I\right)$, so that $\left\{e_{j}, I e_{j}\right\}_{j=1}^{m-1}$ is a $g$-orthonormal basis. Using Lemma 5.9, we compute for each $j \neq k$
$$\begin{aligned}
A_{j k} & :=\operatorname{Rm}\left(e_{j}, e_{k}\right)+\operatorname{Rm}\left(I e_{j}, I e_{k}\right)=\left(\frac{\left(b^{\prime}\right)^{2}}{b^{2}}-\frac{2}{b^{2}}+\frac{a^{2}}{b^{4}}\right)\left(e_{j} \wedge e_{k}+I e_{j} \wedge I e_{k}\right), \\
B_{j k} & :=\operatorname{Rm}\left(e_{j}, I e_{k}\right)-\operatorname{Rm}\left(I e_{j}, e_{k}\right)=\left(\frac{\left(b^{\prime}\right)^{2}}{b^{2}}-\frac{2}{b^{2}}+\frac{a^{2}}{b^{4}}\right)\left(e_{j} \wedge I e_{k}-I e_{j} \wedge e_{k}\right), \\
D_{j k}: & =\operatorname{Rm}\left(e_{j}, I e_{j}\right)-\operatorname{Rm}\left(e_{k}, I e_{k}\right)=\left(\frac{\left(b^{\prime}\right)^{2}}{b^{2}}-\frac{2}{b^{2}}+\frac{a^{2}}{b^{4}}\right)\left(e_{j} \wedge I e_{j}-e_{k} \wedge I e_{k}\right) .
\end{aligned}$$
Assume that the following are true at $x$; we will justify this later.
$$\frac{\left(b^{\prime}\right)^{2}}{b^{2}}-\frac{2}{b^{2}}+\frac{a^{2}}{b^{4}} \neq 0, \quad \frac{2 a b^{\prime}}{b^{3}}-\frac{2 a^{\prime}}{b^{2}} \neq 0 .$$
Then $A_{j k}, B_{j k}$, and $D_{j k}$ vanish on $\mathcal{P}_{x}^{\perp}$, while they act on $\mathcal{P}_{x}$ as nonzero scalar multiples of
$$\begin{aligned}
A_{j k}: & e_{j} \mapsto-e_{k}, \quad e_{k} \mapsto e_{j}, \quad I e_{j} \mapsto-I e_{k}, \quad I e_{k} \mapsto I e_{j}, \\
B_{j k}: & e_{j} \mapsto-I e_{k}, \quad e_{k} \mapsto-I e_{j}, \quad I e_{j} \mapsto e_{k}, \quad I e_{k} \mapsto e_{j}, \\
D_{j k}: & e_{j} \mapsto-I e_{j}, \quad e_{k} \mapsto I e_{k}, \quad I e_{j} \mapsto e_{j}, \quad I e_{k} \mapsto-e_{k} .
\end{aligned}$$

Thus, under the identification of complex vector spaces $\left(\mathcal{P}_{x}, I\right) \rightarrow\left(\mathbb{C}^{m-1}, i\right)$ defined by the $e_{i}$ 's, these operators correspond to a basis for $\mathfrak{s u}(m-1)$ as follows:
$$A_{j k} \mapsto E_{j k}-E_{k j}, \quad B_{j k} \mapsto-i\left(E_{j k}+E_{k j}\right), \quad D_{j k} \mapsto i\left(E_{k k}-E_{j j}\right),$$
where $E_{j k}$ is the $(m-1) \times(m-1)$ matrix with 1 in the $j k$-th entry and 0 elsewhere. We define
$$\mathfrak{h}:=\operatorname{span}\left\{A_{j k}, B_{j k}, D_{j k}\right\}_{j, k=1, \ldots, m-1 ; j \neq k} \subset \mathfrak{s o}\left(T_{x} M\right) .$$
By the above discussion, $\mathfrak{h}$ satisfies item (iv) of the corollary.
Next, let $C:=\operatorname{Rm}\left(\partial_{s}, U\right)$ and define
$$\mathfrak{k}:=\mathfrak{h} \oplus \operatorname{span}\{C\} \subset \mathfrak{s o}\left(T_{x} M\right) .$$
By (5.14) and Lemma 5.9, $C$ acts as a nonzero scalar multiple of $I$ on $\mathcal{P}_{x}$. In view of item (iv) of the corollary, this implies item (iii) of the corollary. By construction, $\mathfrak{k}$ also satisfies item (i) as well as (by Lemma 5.9) item (ii). Thus, the corollary is proved at points $x$ where (5.14) holds.

Therefore, it remains to show that (5.14) on a dense open subset of $M$. This is equivalent to asking that $\varphi:=b^{2}\left(b^{\prime}\right)^{2}-2 b^{2}+a^{2} \neq 0$ and $\psi:=2 a b^{\prime}-2 a^{\prime} b \neq 0$ on a dense open subset of $(0, \infty)$. Note that $\varphi$ is analytic on ( $0, \infty$ ) by Proposition 5.7, and the boundary conditions on $a$ and $b$ give $\lim _{s \rightarrow 0} \varphi(s)=-2 b(0)^{2}<0$. In particular, $\varphi$ is nonzero for sufficiently small $s$, so it is nonzero on a dense open set. The same reasoning shows that $\psi$ is nonzero on a dense open set. Thus, $\varphi$ and $\psi$ are both nonzero on a dense open set. \(\square\)

Proof of Lemma 5.8. Since $(M, g, J)$ is Kähler, we have $\nabla J=0$. Thus, $J$ commutes with all curvature operators $\operatorname{Rm}(X, Y): T_{x} M \rightarrow T_{x} M$. In particular, let $x \in M^{\text {prin }}$ and $\mathfrak{h} \subset \mathfrak{k} \subset \mathfrak{s o}\left(T_{x} M\right)$ be as in Corollary 5.10. Then $J$ commutes with both $\mathfrak{h}$ and $\mathfrak{k}$.

We have $J\left(\mathcal{P}_{x}^{\perp}\right) \subseteq \mathcal{P}_{x}^{\perp}$. Indeed, suppose to the contrary that for some $V \in \mathcal{P}_{x}^{\perp}$ we have $J V=V^{\prime}+W$, where $V^{\prime} \in \mathcal{P}_{x}^{\perp}$ and $W \in \mathcal{P}_{x} \backslash\{0\}$. By Corollary 5.10, we can find $T \in \mathfrak{h}$ such that $T(W) \neq 0$. Since $\mathfrak{h}$ is trivial on $\mathcal{P}_{x}^{\perp}$, we have $T(V)=T\left(V^{\prime}\right)=0$. Then
$$0=J(0)=J T(V)=T(J V)=T\left(V^{\prime}+W\right)=T(W) \neq 0,$$
a contradiction. Hence $J\left(\mathcal{P}_{x}^{\perp}\right) \subseteq \mathcal{P}_{x}^{\perp}$. Since $J$ is invertible and orthogonal, this implies $J\left(\mathcal{P}_{x}^{\perp}\right)=\mathcal{P}_{x}^{\perp}$ and $J\left(\mathcal{P}_{x}\right)=\mathcal{P}_{x}$, i.e. $J$ preserves the splitting $T_{x} M=\mathcal{P}_{x} \oplus \mathcal{P}_{x}^{\perp}$.

The commutant of $\mathfrak{u}(m-1)$ in $\operatorname{End}_{\mathbb{R}}\left(\mathbb{C}^{m-1}\right)$ consists precisely of complex scalar multiples of the identity. As $\mathfrak{k}$ acts as the standard representation of $\mathfrak{u}\left(\mathcal{P}_{x}, I, g\right) \cong \mathfrak{u}(m-1)$ on $\mathcal{P}_{x} \cong \mathbb{C}^{m-1}$, its commutant in $\operatorname{End}_{\mathbb{R}}\left(\mathcal{P}_{x}\right)$ also consists precisely of complex scalar multiples of the identity, where $I$ is the complex structure. Therefore, $\left.J\right|_{\mathcal{P}_{x}}$, which commutes with $\mathfrak{k}$, is of the form $(a+b I) \cdot$ Id for some $a, b \in \mathbb{R}$; since it squares to -Id , we must have $\left.J\right|_{\mathcal{P}_{x}}= \pm I$.

Meanwhile, since $\operatorname{dim}_{\mathbb{C}} \mathcal{P}_{x}^{\perp}=1$ and $\left.J\right|_{\mathcal{P}_{x}^{\perp}}$ is orthogonal, the only two possibilities are $\left.J\right|_{\mathcal{P}_{x}^{\perp}}=J_{\perp}$ and $\left.J\right|_{\mathcal{P}_{x}^{\perp}}=-J_{\perp}$, where $J_{\perp}$ is defined in the lemma. \(\square\)

We can now finish proving Theorem 1.4. The flat case was already handled in case (B) of Proposition 5.7, so it remains to analyze case (A). In this case, $(M, g, J)$ is diffeomorphic to $\mathcal{O}_{\mathbb{C P}^{m-1}}(-m)$, and
$$g=d s^{2}+g_{a(s), b(s)}=d s^{2}+a(s)^{2} \sigma \otimes \sigma+b(s)^{2} \pi^{*} g_{\mathrm{FS}}$$
on $M^{\text {prin }}=M \backslash \mathbb{C P}^{m-1}$, where $a$ and $b$ are positive analytic functions of $s \in(0, \infty)$. Using Lemma 5.8 and (5.15), we compute the Kähler form on a dense open subset of $M^{\text {prin }}$ to be
$$\omega=g(J(\cdot), \cdot)=\varepsilon_{\mathcal{P} \perp} a(s) d s \wedge \sigma+\varepsilon_{\mathcal{P}} b(s)^{2} \pi^{*} \omega_{\mathrm{FS}},$$
where $\omega_{\mathrm{FS}}$ is the Fubini-Study Kähler form, and $\varepsilon_{\mathcal{P}}, \varepsilon_{\mathcal{P}^{\perp}}$ are $\{1,-1\}$-valued functions. Since (5.16) holds in a dense open set of $M^{\text {prin }}$, and $\omega$ is continuous, (5.16) actually holds everywhere on $M^{\text {prin }}$. Moreover, since $M^{\text {prin }}$ is connected, the functions $\varepsilon_{\mathcal{P}}$ and $\varepsilon_{\mathcal{P}^{\perp}}$ are constant. By imposing the Kähler condition $d \omega=0$ and using that $d \sigma=2 \pi^{*} \omega_{\mathrm{FS}}$, we get
$$\left(-2 \varepsilon_{\mathcal{P}^{\perp}} a+2 \varepsilon_{\mathcal{P}} b b^{\prime}\right) d s \wedge \pi^{*} \omega_{\mathrm{FS}}=0$$
As $a, b>0$, and $b^{\prime}$ is positive outside a compact set due to the ALE condition, this implies $\varepsilon_{\mathcal{P}^{\perp}}=\varepsilon_{\mathcal{P}}$ outside a compact set and hence everywhere. Thus,
$$\omega= \pm\left(a(s) d s \wedge \sigma+b(s)^{2} \pi^{*} \omega_{\mathrm{FS}}\right)$$
globally on $M^{\text {prin }}$. Up to possible negation of the complex structure, which can be achieved by pulling back using an antiholomorphic isometry, we have arrived exactly at the Calabi ansatz; see §2.3, in particular (2.4). From the discussion there, it follows that $(M, g, J)$ is biholomorphically isometric to the Calabi space of dimension $m$. This completes the proof of Theorem 1.4.

Acknowledgements. The author wishes to thank his advisor, William Minicozzi, for his continual encouragement and support. He would also like to thank Dain Kim for feedback on an earlier draft of this paper. This work was carried out under the support of a Simons Dissertation Fellowship.

\section*{References}
\begin{itemize}
\item[] [1] M. M. Alexandrino and R. G. Bettiol, Lie groups and geometric aspects of isometric actions, Springer Cham, 2015.
\item[] [2] X. An and W. W. Y. Wong, Warped product space-times, Class. Quantum Grav. 35 (2018), 025011.
\item[] [3] M. T. Anderson, Ricci curvature bounds and Einstein metrics on compact manifolds, J. Amer. Math. Soc. 2 (1989), no. 3, 455-490.
\item[] [4] B. Araneda and J. Lucietti, All toric Hermitian ALE gravitational instantons, Preprint, arXiv:2510.09291 (2025).
\item[] [5] A. V. Bagaev and N. I. Zhukova, The isometry groups of Riemannian orbifolds, Sib. Math. J. 48 (2007), 579-592.
\item[] [6] S. Bando, A. Kasue, and H. Nakajima, On a construction of coordinates at infinity on manifolds with fast curvature decay and maximal volume growth, Invent. Math. 97 (1989), 313-349.
\item[] [7] A. L. Besse, Einstein manifolds, Classics in Mathematics, Springer Berlin, Heidelberg, 1987.
\item[] [8] M. Bianchi, F. Fucito, G. C. Rossi, and M. Martellini, ALE instantons in string effective theory, Nuclear Phys. B 440 (1995), no. 1-2, 129-170.
\item[] [9] O. Biquard, Désingularisation de métriques d'Einstein. I, Invent. Math. 192 (2013), 197-252.
\item[] [10] O. Biquard and H.-J. Hein, The renormalized volume of a 4-dimensional Ricci-flat ALE space, J. Differential Geom. 123 (2023), no. 3, 411-429.
\item[] [11] S. Brendle, Rotational symmetry of self-similar solutions to the Ricci flow, Invent. Math. 194 (2013), 731-764.
\item[] [12] S. Brendle and N. Kapouleas, Gluing Eguchi-Hanson metrics and a question of Page, Comm. Pure Appl. Math. 70 (2017), no. 7, 1366-1401.
\item[] [13] E. Calabi, Métriques kählériennes et fibrés holomorphes, Ann. Sci. École Norm. Sup. (4) 12 (1979), no. 2, 269-294.
\item[] [14] J. Cheeger and A. Naber, Regularity of Einstein manifolds and the codimension 4 conjecture, Ann. of Math. 182 (2015), no. 3, 1093-1165.
\item[] [15] J. Cheeger and G. Tian, On the cone structure at infinity of Ricci flat manifolds with Euclidean volume growth and quadratic curvature decay, Invent. Math. 118 (1994), no. 1, 493-571.
\item[] [16] O. Chodosh, M. Eichmair, and A. Volkmann, Isoperimetric structure of asymptotically conical manifolds, J. Differential Geom. 105 (2017), no. 1, 1-19.
\item[] [17] B. Dammermann, Diagonalizing cohomogeneity-one Einstein metrics, J. Geom. Phys. 59 (2009), no. 9, 1271-1284.
\end{itemize}
\begin{itemize}
\item[] [18] G. de Rham, Complexes à automorphismes et homéomorphie différentiable, Ann. Inst. Fourier 2 (1950), 51-67.
\item[] [19] S. K. Donaldson, Calabi-Yau metrics on Kummer surfaces as a model gluing problem, Advanced Lectures in Mathematics (ALM), vol. 21, International Press, 2012.
\item[] [20] M. R. Douglas, B. Fiol, and C. Römelsberger, The spectrum of BPS branes on a noncompact Calabi-Yau, J. High Energy Phys. 2005 (2005), no. 9, 057.
\item[] [21] T. Eguchi and A. J. Hanson, Asymptotically flat self-dual solutions to Euclidean gravity, Phys. Lett. B 74 (1978), no. 3, 249-251.
\item[] [22] G. W. Gibbons and S. W. Hawking, Gravitational multi-instantons, Phys. Lett. B 78 (1978), no. 4, 430-432.
\item[] [23] D. González Álvaro, Topological and geometric consequences of curvature and symmetry, Ph.D. thesis, Universidad Autónoma de Madrid, 2016. Available at https://dcain.etsin.upm.es/~david/tesis_main.pdf.
\item[] [24] S. W. Hawking, Gravitational instantons, Phys. Lett. A 60 (1977), no. 2, 81-83.
\item[] [25] N. J. Hitchin, Polygons and gravitons, Math. Proc. Cambridge Philos. Soc. 85 (1979), no. 3, 465-476.
\item[] [26] W.-Y. Hsiang and H. B. Lawson Jr, Minimal submanifolds of low cohomogeneity, J. Differential Geom. 5 (1971), 1-38.
\item[] [27] D. Joyce and S. Karigiannis, A new construction of compact torsion-free $G_{2}$-manifolds by gluing families of Eguchi-Hanson spaces, J. Differential Geom. 117 (2021), no. 2, 255-343.
\item[] [28] D. D. Joyce, Compact manifolds with special holonomy, Oxford University Press, 2000.
\item[] [29] S. Kobayashi, Transformation groups in differential geometry, Classics in Mathematics, Springer Berlin, Heidelberg, 1995.
\item[] [30] S. Kobayashi and K. Nomizu, Foundations of differential geometry, vol. 2, Wiley Classics Library, Wiley-Interscience, 1996.
\item[] [31] K. Kröncke and O. L. Petersen, Long-time estimates for heat flows on asymptotically locally Euclidean manifolds, Int. Math. Res. Not. IMRN 2022 (2022), no. 24, 19943-20003.
\item[] [32] K. Kröncke and Á. Szabó, Optimal coordinates for Ricci-flat conifolds, Calc. Var. Partial Differential Equations 63 (2024), no. 188.
\item[] [33] P. B. Kronheimer, The construction of ALE spaces as hyper-Kähler quotients, J. Differential Geom. 29 (1989), no. 3, 665-683.
\item[] [34] M. B. Law, On steady and expanding Ricci solitons with asymptotic symmetries, Preprint, arXiv:2505.20576 (2026).
\item[] [35] D. A. Lee, Geometric relativity, Graduate Studies in Mathematics, vol. 201, American Mathematical Society, 2019.
\item[] [36] M. Li, On 4-dimensional Ricci-flat ALE manifolds, Preprint, arXiv:2304. 01609 (2023).
\item[] [37] M. T. Lock and J. A. Viaclovsky, Quotient singularities, eta invariants, and self-dual metrics, Geom. Topol. 20 (2016), no. 3, 1773-1806.
\item[] [38] P. Morteza and J. A. Viaclovsky, The Calabi metric and desingularization of Einstein orbifolds, J. Eur. Math. Soc. 22 (2020), 1201-1245.
\item[] [39] P. S. Mostert, On a compact Lie group acting on a manifold, Ann. of Math. 65 (1957), no. 3, 447-455.
\item[] [40] H. Nakajima, Self-duality of ALE Ricci-flat 4-manifolds and positive mass theorem, Adv. Stud. Pure Math. 18 (1990), no. 1, 385-396.
\item[] [41] B. O'Neill, The fundamental equations of a submersion, Michigan Math. J. 13 (1966), no. 4, 459-469.
\item[] [42] T. Ozuch, Noncollapsed degeneration of Einstein 4-manifolds, I, Geom. Topol. 26 (2022), 1483-1528.
\item[] [43] R. Ponge and H. Reckziegel, Twisted products in pseudo-Riemannian geometry, Geom. Dedicata 48 (1993), 15-25.
\item[] [44] S. Salamon, Riemannian geometry and holonomy groups, Pitman Research Notes in Mathematics, Longman Science \& Technology, 1989.
\item[] [45] K. Sekigawa, 3-dimensional homogeneous Riemannian manifolds I, Sci. Rep. Niigata Univ. 14 (1977), 5-14.
\end{itemize}

MIT, Department of Mathematics, 77 Massachusetts Avenue, Cambridge, MA 02139, USA.
Email address: mikelaw@mit.edu