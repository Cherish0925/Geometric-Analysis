---
retention_scope: session
part: 2
total_parts: 4
---

[Part 2/4 of: Seiberg–Witten Monopoles on Seifert Fibered Spaces]

When the Inequality 5.30 is satisfied, then the moduli space of vortices is identified with a moduli space of divisors, which consist of pairs ( $B_{0}, \alpha_{0}$ ) satisfying only $\bar{\partial}_{B_{0}} \alpha_{0}=0$, modulo the action of $\operatorname{Map}\left(\Sigma, \mathbb{C}^{*}\right)$. This
identification is done by showing that for each divisor $\left(\bar{\partial}_{B_{0}}, \alpha_{0}\right)$, there is a unique real-valued function $u$ on $\Sigma$ such that $e^{u}\left(\bar{\partial}_{B_{0}}, \alpha_{0}\right)$ satisfies the curvature condition of Equation 5.13, by reexpressing this latter equation as a Kazdan-Warner equation for $u$. Properties of this equation guarantee the existence and uniqueness of $u$.

Finally, such a divisor is uniquely determined (as the name suggests) by the zero-set $|\alpha|^{-1}(0)$, with zeros counted with appropriate multiplicities. (Here $|\alpha|$ denotes the holomorphic section of the desingularization of $\left(E, \bar{\partial}_{B_{0}}\right)$.) Over a (one-dimensional) orbifold, the moduli space of divisors is always cut out transversally: it is cut out by a map whose linearization has kernel $H^{0}\left(\alpha^{-1}(0),\left.\mathcal{E}\right|_{\alpha^{-1}(0)}\right)$, and and cokernel $H^{1}\left(\alpha^{-1}(0),\left.\mathcal{E}\right|_{\alpha^{-1}(0)}\right)$. The cokernel, being the first cohomology group of a sheaf over a zero-dimensional space, must vanish, and the index of the operator is given by the difference
$$\chi(\Sigma, \mathcal{E})-\chi\left(\Sigma, \mathcal{O}_{\Sigma}\right)=e,$$
by the Riemann-Roch formula. \(\square\)

\subsection*{5.8. Reducibles.}

We now turn our attention to the reducible critical points in $Y$. Reducible critical points in the $\operatorname{Spin}_{\mathrm{c}}(3)$ structure determined by $E$ correspond to gauge equivalence classes of connections $B$ whose curvature form satisfies
$$2 F_{B}-F_{K_{\Sigma}}=0$$

Definition 5.13. A line bundle $E_{0}$ is called an orbi-spin bundle on $\Sigma$ if
$$2 \operatorname{deg}\left(E_{0}\right)=\operatorname{deg}\left(K_{\Sigma}\right),$$

Not every orbifold admits an orbi-spin bundle. For example, among the orbifolds with cyclic topological Picard group (i.e. orbifolds for which all the local invariants $\alpha_{i}$ are pairwise relatively prime), the ones which do admit an orbi-spin bundle are precisely those whose local invariants are all odd.

Proposition 5.14. A line bundle $E$ over $Y$ supports a reducible solution if and only if $E \cong \pi^{*}\left(E_{0}\right)$ for some orbifold line bundle $E_{0}$ over $\Sigma$. In this case, the space of reducibles in the $\operatorname{Spin}_{\mathrm{c}}(3)$ structure determined by $E$, denoted $\mathfrak{J}(E)$, is homeomorphic to the Jacobian torus $H^{1}(\Sigma ; \mathbb{R}) / H^{1}(\Sigma ; \mathbb{Z})$. A line bundle $E$ supports a reducible solution with trivial fiberwise holonomy if and only if $E \cong \pi^{*}\left(E_{0}\right)$ for an orbi-spin bundle $E_{0}$ over $\Sigma$.

Proof. Suppose $E \cong \pi^{*}\left(E_{0}\right)$. One can always find a constant curvature connection $B_{0}$ on $E_{0}$. Then, the connection
$$\pi^{*}\left(B_{0}\right)+i\left(\frac{\frac{1}{2} \operatorname{deg}\left(K_{\Sigma}\right)-\operatorname{deg}\left(E_{0}\right)}{\operatorname{deg}(N)}\right) \eta$$
satisfies Equation 5.31. Conversely, if $E$ supports a reducible solution, then it follows from Equation 5.31 and Theorem 2.13 that $c_{1}(E)$ is a torsion class, hence it must be isomorphic to $\pi^{*}\left(E_{0}\right)$ for an orbifold line bundle $E_{0}$ over $\Sigma$.

Any two connections $B_{1}, B_{2}$ in line bundles $E_{1}, E_{2}$ respectively, with the same curvature form must differ by tensoring with a flat line bundle. Thus, the identification of the reducibles with the Jacobian follows from Corollary 2.15.

The final statement is a direct consequence of Proposition 5.3. \(\square\)

We wish to investigate conditions under which the identification between $\mathfrak{J}(E)$ and the Jacobian torus of $\Sigma$ is naturally a diffeomorphism.

Definition 5.15. A point $[B, 0] \in \mathfrak{J}(E)$ is called a non-degenerate critical point if the kernel of the linearization of the Seiberg-Witten equations $D_{[B, 0]} \nabla \mathrm{cs}$ is isomorphic to the tangent space to the Jacobian torus. The reducible locus $\mathfrak{J}(E)$ is called non-degenerate when each reducible $[B, 0] \in \mathfrak{J}(E)$ is a non-degenerate critical point.

Around a reducible solution ( $B, 0$ ), the linearization of the Seiberg-Witten equations takes the form
$$D_{[B, 0]} \nabla \operatorname{cs}(b, \psi)=\left((* d+d *) b, \mathbf{D}_{B} \psi\right),$$
so its kernel is isomorphic to $H^{1}(Y ; \mathbb{R}) \oplus \operatorname{KerD}_{B} ;$ so $\mathfrak{J}(E)$ is non-degenerate when for all $[B, 0] \in \mathfrak{J}(E), \mathbf{D}_{B}$ has no kernel.

Proposition 5.16. Let $(E, B)$ be a line-bundle-with-connection over $Y$ whose curvature form pulls back from $\Sigma$. If $B$ has non-trivial fiberwise holonomy, then the Dirac operator $\mathbf{D}_{B}$ has no kernel. Otherwise, by Proposition 5.3, we can push $(E, B)$ forward to $\Sigma$, and we have a corresponding identification
$$\operatorname{Ker}\left(\mathbf{D}_{B}\right) \cong H^{0}\left(\Sigma, \pi_{*}(E, B)\right) \oplus H^{1}\left(\Sigma, \pi_{*}(E, B)\right) .$$

Proof. This follows from the Weitzenböck formula from Equation 5.8, together with the hypothesis that $F_{B}$ pulls back from $\Sigma$ and Lemma 5.8 give that the square of the Dirac operator splits as a pair of non-negative operators
$$\mathbf{D}_{B}^{2}=\left(\eta \cdot \nabla_{\frac{\partial}{\partial \varphi}}\right)^{2}+\left(\mathrm{D}_{2}\right)^{2},$$
so any kernel element must be fiberwise constant. Hence the first statement. The second follows from the complex interpretation of the Dirac operator, Equation 5.12. \(\square\)

It follows from the above Proposition that if a line bundle $E$ admits a reducible solution $B$ whose Dirac operator has a non-trivial kernel, then $E \cong \pi^{*}\left(E_{0}\right)$ for an orbi-spin bundle $E_{0}$. When $\Sigma$ has cyclic topological Picard group, the orbifold line bundles over $\Sigma$ are uniquely specified by their degree. Hence, there is at most one orbi-spin bundle, which we write as $K_{\Sigma}^{1 / 2}$.

Corollary 5.17. Suppose that $Y$ is a Seifert fibered space over an orbifold $\Sigma$ whose topological Picard group is cyclic, and $E$ is the line bundle corresponding to a $\operatorname{Spin}_{\mathrm{c}}(3)$-structure which supports reducible solutions. Then, the reducible locus $\mathfrak{J}(E)$ is not non-degenerate if and only if the following three conditions are satisfied:
\begin{itemize}
\item[1.] $\Sigma$ is orbi-spin,
\item[2.] $E \cong \pi^{*}\left(K^{1 / 2}\right)$, and
\item[3.] $g(\Sigma)>0$,
\end{itemize}

Proof. By Proposition 5.16, if $\mathbf{D}_{B}$ has non-trivial kernel, $B$ must have non-trivial fiberwise holonomy, so that $\pi_{*}(E, B)$ is a bundle-with-connection over $\Sigma$. Equation 5.31 then implies that $\pi_{*}(E, B)$ lives in an orbi-spin bundle on $\Sigma$, proving Conditions 1 and 2. The Seifert invariants of the orbi-spin $K^{1 / 2}$ bundle are
$$\left(g-1, \frac{\alpha_{1}-1}{2}, \ldots, \frac{\alpha_{n}-1}{2}\right)$$
(all these numbers are integers, since all the $\alpha_{i}$ are odd); and as $B$ ranges over all connections with a fixed curvature, $\pi_{*}(E, B)$ ranges over all possible complex structures on $K^{1 / 2}$. According to Proposition 5.16, together with Serre duality (Theorem 2.10), the question of whether there is a reducible
$B$ on $E$ with $\operatorname{ker} \mathbf{D}_{B} \neq 0$ is equivalent to the question of whether there is a complex structure on $K^{1 / 2}$ with holomorphic sections. This is in turn is topological question: $K^{1 / 2}$ has holomorphic sections if and only if its desingularization has non-negative degree (using Proposition 2.8 and the corresponding well-known fact for smooth curves), i.e. $g-1 \geq 0$. \(\square\)

Remark 5.18. If $g(\Sigma)=0$ and $\Sigma$ does not have a cyclic topological Picard group, $Y$ might admit a reducible solution $(B, 0)$ whose Dirac operator has non-trivial kernel. Let $\Sigma$ be the genus zero orbifold with three marked points, each having multiplicity 3. Since $\operatorname{deg}\left(K_{\Sigma}\right)=0$, the trivial bundle is an orbi-spin bundle with a holomorphic section.

\subsection*{5.9. The critical sets of the Chern-Simons functional.}

Combining Theorem 4, Theorem 5, and Proposition 5.14, we obtain the following refined version of Theorem 1.

Theorem 5.19. Let $\pi: Y=S(N) \rightarrow \Sigma$ be a Seifert fibered space corresponding to an orbifold line bundle $N$ with non-zero degree. The Seiberg-Witten moduli space for the $\operatorname{Spin}_{\mathrm{c}}(3)$ structure $E \otimes W_{c}$ is non-empty if and only if $E \cong \pi^{*}\left(E_{0}\right)$ for some orbifold line bundle $E_{0}$ over $\Sigma$. The moduli space $\mathcal{M}_{s w}\left(\pi^{*}\left(E_{0}\right) \otimes W_{c}\right)$ consists of one reducible component $\mathfrak{J}\left(\pi^{*}\left(E_{0}\right)\right)$, which is homeomorphic to the Jacobian torus of $|\Sigma|$, and a pair of components $\mathcal{C}^{ \pm}(E)$ for each isomorphism class of orbifold line bundles $E$ over $\Sigma$ with
$$0 \leq \operatorname{deg}(E)<\frac{\operatorname{deg}\left(K_{\Sigma}\right)}{2}$$
and
$$[E] \equiv\left[E_{0}\right] \quad(\bmod \mathbb{Z}[N])$$
in $\operatorname{Pic}^{t}(\Sigma)$. The component $\mathcal{C}^{+}(E) \cong \mathcal{C}^{-}(E)$ is naturally diffeomorphic to the moduli space of effective divisors in $E$.

Remark 5.20. In the above statement, $\mathcal{C}^{+}(E)$ is obtained as $\pi^{*}\left(\mathcal{M}_{v}^{+}(E)\right)$, while $\mathcal{C}^{-}\left(K_{\Sigma} \otimes E^{-1}\right)$ is $\pi^{*}\left(\mathcal{M}_{v}^{-}(E)\right)$. Sometimes (as in Section 1), we find it convenient to label the irreducible critical manifolds by Seifert data rather than isomorphism classes of line bundles (these data are equivalent, according to Proposition 2.12); i.e. $\mathcal{C}^{ \pm}(\mathbf{e})$ denotes $\mathcal{C}^{ \pm}(E)$, when e is the Seifert data for the line bundle $E$. Moreover, when it is clear from the context, we will drop the line bundle (indicating the $\operatorname{Spin}_{\mathrm{c}}(3)$ structure) from the notation for the reducible locus $\mathfrak{J}$.

Recall the following definition from Morse theory (which is the natural analogue of Definition 5.15 in the irreducible case).

Definition 5.21. A critical point $[B, \Psi] \in \mathcal{M}_{s w}^{*}(E)$ is called a non-degenerate critical point if there is a neighborhood of $[B, \Psi]$ which is a submanifold of of $\mathcal{B}(E)$, and
$$\operatorname{Ker} D_{[B, \Psi]} \nabla \mathrm{cs}=T_{[B, \Psi]} \mathcal{M}_{s w}^{*}(E) .$$
A component $\mathcal{C} \subset \mathcal{M}_{s w}^{*}(E)$ is called a non-degenerate critical manifold if every point $[B, \Psi] \in \mathcal{C}$ is a non-degenerate point.

Corollary 5.22. The irreducible critical manifolds $\mathcal{C}^{ \pm}(E)$ are all non-degenerate.

Proof. This follows from the fact that the moduli space of vortices is always a smooth manifold, cut out transversally according to Theorem 5, together with the identification of the kernels in Equation 5.21. \(\square\)

The Chern-Simons invariant, cs, of a solution depends only on the component of that solution in the moduli space. Moreover, since only torsion classes arise as the first Chern class of a $\operatorname{Spin}_{\mathrm{c}}(3)$ structure for which cs has critical values, we see that the Chern-Simons function is naturally a real-valued function (we are using here the assumption that $Y$ is associated to a line bundle with non-zero degree, see Remark 2.14).

Proposition 5.23. Suppose that the function cs is normalized so that $\operatorname{cs}(\mathfrak{J})=0$ for $\mathfrak{J}$ a reducible solution to the Seiberg-Witten equations. Then,
$$\operatorname{cs}\left(\mathcal{C}^{ \pm}(E)\right)=\frac{4 \pi^{2}}{\operatorname{deg}(N)}\left(\operatorname{deg}(E)-\frac{\operatorname{deg}\left(K_{\Sigma}\right)}{2}\right)^{2} .$$
Proof. Suppose $B$ is a Hermitian connection in a line bundle $E$ over $Y$. We define the $Y$-degree of $E, \operatorname{deg}_{Y}(B)$ by the formula
$$\operatorname{deg}_{Y}(B)=\frac{i}{4 \pi^{2}} \int F_{B} \wedge \eta .$$

Let $B_{1}, B_{2}$ be two Hermitian connections in a line bundle $E$ over $Y$ whose curvature forms pull up from $\Sigma$. (This condition is equivalent to
the condition that the fiberwise holonomy over the smooth locus of $\Sigma$ is constant, see the remarks preceding the proof of Proposition 5.3). We have that
$$\begin{aligned}
\int_{Y}\left(B_{1}-B_{2}\right) & \wedge \operatorname{Tr}\left(F_{B_{1} \otimes W_{c}+F_{B_{2} \otimes W_{c}}}\right) \\
& =\int_{Y}\left(B_{1}-B_{2}\right) \wedge \pi^{*}\left(2 F_{B_{1}}+2 F_{B_{2}}-2 F_{K_{\Sigma}}\right) \\
& =\int_{\Sigma} \pi_{*}\left(B_{1}-B_{2}\right)\left(2 F_{B_{1}}+2 F_{B_{2}}-2 F_{K_{\Sigma}}\right),
\end{aligned}$$
where
$$\pi_{*}: \Omega^{1}(Y) \rightarrow \Omega^{0}(\Sigma)$$
denotes the operation of integration along the fibers. Now, $\pi_{*}\left(B_{1}-B_{2}\right)$ is a constant function over $\Sigma$, since $\pi_{*}\left(B_{1}-B_{2}\right)$ measures the difference between the fiberwise holonomy of $B_{1}$ and the fiberwise holonomy of $B_{2}$, and both holonomies are constant. In fact,
$$\pi_{*}\left(B_{1}-B_{2}\right) \equiv \frac{2 \pi i\left(\operatorname{deg}_{Y}\left(B_{1}\right)-\operatorname{deg}_{Y}\left(B_{2}\right)\right)}{\operatorname{deg}(N)}$$
since
$$d \eta=-\frac{2 \pi \operatorname{deg}(N)}{\operatorname{Vol}(\Sigma)} \mu_{\Sigma}$$
so that
$$\begin{aligned}
\int_{\Sigma} \pi_{*}\left(B_{1}-B_{2}\right) \mu_{\Sigma} & =\int_{Y}\left(B_{1}-B_{2}\right) \pi^{*}\left(\mu_{\Sigma}\right) \\
& =-\frac{\operatorname{Vol}(\Sigma)}{2 \pi \operatorname{deg}(N)} \int_{Y}\left(B_{1}-B_{2}\right) \wedge d \eta \\
& =-\frac{\operatorname{Vol}(\Sigma)}{2 \pi \operatorname{deg}(N)} \int_{Y}\left(F_{B_{1}}-F_{B_{2}}\right) \wedge \eta \\
& =\frac{2 \pi i \operatorname{Vol}(\Sigma)}{\operatorname{deg}(N)}\left(\operatorname{deg}_{Y}\left(B_{1}\right)-\operatorname{deg}_{Y}\left(B_{2}\right)\right) .
\end{aligned}$$
Thus, we have that
$$\int_{Y}\left(B_{1}-B_{2}\right) \wedge \operatorname{Tr}\left(F_{B_{1} \otimes W_{c}}+F_{B_{2} \otimes W_{c}}\right)=\frac{8 \pi^{2}}{\operatorname{deg}(N)}\left(\operatorname{deg}_{Y}\left(B_{1}\right)-\operatorname{deg}_{Y}\left(B_{2}\right)\right)^{2} .$$

Equation 5.32 follows from this equation, since Chern-Weil theory gives us that for any line-bundle-with-connection $\left(E_{0}, C_{0}\right)$ over $\Sigma$,
$$\operatorname{deg}_{Y}\left(\pi^{*}\left(E_{0}, C_{0}\right)\right)=\operatorname{deg}\left(E_{0}\right)$$
and Equation 5.31 guarantees that for any reducible solution $(B, 0)$,
$$\operatorname{deg}_{Y}(B)=\frac{\operatorname{deg}\left(K_{\Sigma}\right)}{2} .$$ \(\square\)

\section*{6. Gradient Flow Lines.}

We now turn our attention to solutions to the Seiberg-Witten equations (Equations 4.7, 4.8) over the cylinder $R^{o} \cong \mathbb{R} \times Y$, given the metric
$$g_{c y l}=d t^{2}+g_{Y}$$
and $\operatorname{Spin}_{\mathrm{c}}(4)$ structure $p^{*}(W)$ induced by some given $\operatorname{Spin}_{\mathrm{c}}(3)$ structure ( $W, \rho$ ) over $Y$. The configuration space now is given by
$$\mathcal{B}\left(p^{*}(W)\right)=\mathcal{A}\left(p^{*}(W)\right) \times \Gamma\left(R^{o}, p^{*}(W)\right) / \operatorname{Map}\left(R^{o}, S^{1}\right),$$
where $\mathcal{A}\left(p^{*}(W)\right)$ is the affine space of spinorial connections in $p^{*}\left(W^{T}\right)$, meaning those connections ∇ which are spinorial with respect to the connection which is $\nabla_{\text {cyl }}=d \oplus{ }^{\circ} \nabla$ in terms of the splitting $T^{*} R^{o}=\mathbb{R}(d t) \oplus T^{*} Y$. By elliptic regularity, the topology induced on the Seiberg-Witten moduli space from the $\mathcal{C}^{\infty}$ topology on $\mathcal{B}\left(p^{*}(W)\right)$ is equivalent to the topology induced by the $L_{k}^{2}$ topology on the configuration space for any $k \geq 2$ (giving the gauge group $\operatorname{Map}\left(R^{o}, S^{1}\right)$ the $L_{k+1, \text { loc }}^{2}$ topology).

We will be interested in the moduli space of solutions to the Seiberg-Witten equations on the cylinder for which the Chern-Simons function cs has bounded variation along the slices $\{t\} \times Y$. In fact, arguments from from [27] show that for any solution ( $A, \Phi$ ) with bounded variation of cs along the slices, there are a pair of critical points $\left[B_{ \pm}, \Psi_{ \pm}\right]$for cs for which
$$\lim _{t \mapsto \pm \infty}\left[\left.(A, \Phi)\right|_{\{t\} \times Y}\right] \mapsto \pi^{*}\left[B_{ \pm}, \Psi_{ \pm}\right] .$$

This allows us to partition the moduli space into components labeled by pairs of critical sets $\mathcal{C}_{1}, \mathcal{C}_{2}$ for $\mathrm{cs}, \mathcal{M}\left(\mathcal{C}_{1}, \mathcal{C}_{2}\right)$, of solutions to the Seiberg-Witten equations over $\mathbb{R} \times Y$ which satisfy
$$\lim _{t \mapsto \pm \infty}\left[\left.(A, \Phi)\right|_{\{t\} \times Y}\right]=\pi^{*}\left[B_{ \pm}, \Psi_{ \pm}\right],$$
for some pair of critical points $\left[B_{-}, \Psi_{-}\right] \in \mathcal{C}_{1},\left[B_{+}, \Psi_{+}\right] \in \mathcal{C}_{2}$.
The following was observed in [19]:
Proposition 6.1. Given a pair of critical sets for $\mathrm{cs}, \mathcal{C}^{ \pm}$, there is an identification between the moduli space of parameterized gradient flow lines for cs from $\mathcal{C}^{-}$to $\mathcal{C}^{+}$in $\mathcal{B}(W)$ and $\mathcal{M}\left(\mathcal{C}^{+}, \mathcal{C}^{-}\right)$.

When $\pi: Y \rightarrow \Sigma$ is a Seifert fibered space, the cylinder $R^{o}$ can be given a complex structure as in Section 3. We recall the following basic result (see [34] and [22]) about the Seiberg-Witten equations on any complex surface.

Theorem 6.2. Let $X$ be an almost-complex surface with a Riemannian metric, and denote its associated $(1,1)$ form by $\omega$. The $\operatorname{Spin}_{\mathrm{c}}(4)$ structures on $X$ naturally correspond to isomorphism classes of Hermitian line bundles $E$ under the correspondence identifying
$$W^{+} \cong\left(\Lambda^{0,0} \oplus \Lambda^{0,2}\right) \otimes E \quad \text { and } \quad W^{-} \cong\left(\Lambda^{0,1}\right) \otimes E,$$
where $\Lambda^{0,0}$ (resp. $\Lambda^{0,2}$ ) is the $2 i$ (resp. - $2 i$ ) eigenbundle of Clifford multiplication by $\omega$. Let ∇ be a connection on $T^{*} X$ for which
$$\nabla \omega \equiv 0 .$$
Then the Seiberg-Witten equations for $\nabla$-spinorial connections and spinors in $W^{+}$reduce to the following equations for a compatible connection $A$ in the Hermitian line bundle $E$ and sections
$$\alpha, \beta \in \Omega^{0,0}(X, \mathbb{C}), \Omega^{0,2}(X, \mathbb{C}):$$
$$2 \Lambda F_{A}-\Lambda F_{K_{X}}=i\left(|\alpha|^{2}-|\beta|^{2}\right)$$
$$2 F_{A}^{0,2}-F_{K_{X}}^{0,2}=\alpha^{*} \otimes \beta$$
$$\bar{\partial}_{A} \alpha+\bar{\partial}_{A}^{*} \beta=0 .$$
In the above, $F_{K_{X}}$ denotes the curvature of the connection which ∇ induces on the canonical bundle, and
$$\Lambda: \Omega^{2}(X, \mathbb{C}) \rightarrow \Omega^{0}(X, \mathbb{C})$$
denotes the operation
$$F \mapsto\langle F, \omega\rangle .$$

Remark 6.3. For a proof of the above result, see [22]. Equations 6.3 and 6.4 hold for any complex four-manifold. Equation 6.5 follows from the identification of the Dirac operator with the rolled-up $\bar{\partial}$-operator, which is usually stated for Levi-Civita-spinorial connections on a Kähler manifold. However, the proof uses only the fact that Clifford multiplication by $\omega$ commutes with the Dirac operator, which follows from Equation 6.2.

For $\left(R^{o}, g_{\text {cyl }}\right)$ with its complex structure as in Section 3, the $(1,1)$ form is:
$$\omega=d t \wedge \eta+\pi^{*}\left(\mu_{\Sigma}\right),$$
which is evidently covariantly constant for the connection $\nabla_{\text {cyl }}$, so we can apply the above theorem. Moreover, note that the above decomposition of spinors in $W^{+}$is compatible with the decomposition of $W$ into $S^{ \pm}$(Equation 5.9), in the sense that
$$\pi^{*}\left(S^{+}\right) \cong \Lambda^{0,0}(E) \quad \text { and } \quad \pi^{*}\left(S^{-}\right) \cong \Lambda^{0,2}(E) .$$

In the compact, Kähler case one uses Theorem 6.2, together with an integration-by-parts argument to show a correspondence between solutions to the Seiberg-Witten equations and holomorphic data (see [34]). (This was also the structure of the proof of Theorem 4.) To perform this integration-by-parts argument on the cylinder, we need to know about the behavior at infinity our solution. To this end, we apply the standard exponential decay estimates ([27],[32]) adapted to the context of Seiberg-Witten monopoles:

Theorem 6.4. Given any pair of non-degenerate critical manifolds $\mathcal{C}_{-}, \mathcal{C}_{+}$ for cs (definition 5.21), there is a $\delta>0$ with the property that any flow line between these manifolds corresponds to a solution $(A, \Phi)$ to the Seiberg-Witten equations over $R^{o}$ in the $\operatorname{Spin}_{\mathrm{c}}(4)$ structure $\pi^{*}(W)$ for which there exist $\left[B_{ \pm}, \Psi_{ \pm}\right] \in \mathcal{C}_{ \pm}$, with
$$\begin{aligned}
\lim _{t \mapsto \pm \infty} e^{ \pm \delta t}\left(\left\|\nabla_{c y l}^{(k)}\left(A-\pi^{*}\left(B_{ \pm}\right)\right)\right\|_{\{t\} \times Y}\right. & \\
& \left.+\left\|\nabla_{\pi^{*}\left(B_{ \pm}\right)}^{(k)}\left(\Phi-\pi^{*}\left(\Psi_{ \pm}\right)\right)\right\|_{\{t\} \times Y}\right) \mapsto 0,
\end{aligned}$$
for all $k \in \mathbb{Z}$. The norms appearing above are $\mathcal{C}^{0}$ norms on $Y$.
We are now ready to apply the integration-by-parts argument, to obtain a correspondence between gradient flow lines and (certain) vortices over $R^{o}$.

Proposition 6.5. Gradient flow lines between regular critical manifolds of cs correspond to configurations
$$[A, \alpha, \beta] \in\left(\mathcal{A}\left(R^{o}, E\right) \times \Gamma\left(R^{o}, E\right) \times \Gamma\left(R^{o}, \pi^{*}\left(K_{\Sigma}^{-1}\right) \otimes E\right)\right) / \mathcal{G}\left(R^{o}\right)$$
which satisfy satisfy the decay condition Equation 6.7, together with the generalized vortex equations:
$$\begin{aligned}
2 \Lambda F_{A}-\Lambda \pi^{*} F_{K_{\Sigma}} & =i\left(|\alpha|^{2}-|\beta|^{2}\right) \mu_{\Sigma} \\
F_{A}^{0,2} & =0 \\
\bar{\partial}_{A} \alpha=0 & \text { and } \bar{\partial}_{A}^{*} \beta=0 \\
\alpha=0 & \text { or } \quad \beta=0 .
\end{aligned}$$
Proof. First notice that $\nabla_{\text {cyl }}=d \oplus d \oplus \pi^{*}\left(\widehat{\nabla}_{\Sigma}\right)$ with respect to the splitting
$$T^{*} R^{o} \cong \mathbb{R}(d t) \oplus \mathbb{R}(\eta) \oplus \pi^{*}\left(T^{*} \Sigma\right),$$
so that $F_{K_{R}}=\pi^{*} F_{\Sigma}$; in particular, $F_{K}^{0,2}=0$. Applying $\bar{\partial}_{A}$ to Equation 6.5, and then using Equation 6.5, we see that
$$0=F_{A}^{0,2} \alpha+\bar{\partial}_{A} \bar{\partial}_{A}^{*} \beta=|\alpha|^{2} \beta+\bar{\partial}_{A} \bar{\partial}_{A}^{*} \beta .$$
Taking the inner product with $\beta$, we get
$$0=|\alpha|^{2}|\beta|^{2}+\left\langle\bar{\partial}_{A} \bar{\partial}_{A}^{*} \beta, \beta\right\rangle .$$

By Stokes' theorem, for any $\gamma \in \Omega^{0,1}(Y, E), \beta \in \Omega^{0,2}(Y, E), T \in \mathbb{R}$,
$$\begin{aligned}
\int_{\{T\} \times Y} \gamma \wedge \bar{\beta}-\int_{\{-T\} \times Y} \gamma \wedge \bar{\beta} & =\int_{[-T, T] \times Y} d(\gamma \wedge \bar{\beta}) \\
& =\int_{[-T, T]} \bar{\partial}_{A} \gamma \wedge \bar{\beta}+\int_{[-T, T]} \gamma \wedge \overline{\bar{\partial}}_{A}^{*} \beta .
\end{aligned}$$
Applying this equation to the integral of Equation 6.8 over the region $[-T, T] \times Y$, we get
$$\begin{aligned}
0= & \int_{[-T, T] \times Y}|\alpha|^{2}|\beta|^{2}+\int_{[-T, T] \times Y}\left\langle\bar{\partial}_{A}^{*} \beta, \bar{\partial}_{A}^{*} \beta\right\rangle \\
& +\left.\int_{\{t\} \times Y} \bar{\partial}_{A}^{*} \beta \wedge \bar{\beta}\right|_{t=-T} ^{t=T}
\end{aligned}$$

But, applying Theorem 6.4 and Theorem 4, we get a convergance (of sections of $W$ over $Y$, in the $\mathcal{C}^{\infty}$ topology):
$$\begin{aligned}
\lim _{t \mapsto \infty} \bar{\partial}_{A_{T}}^{*} \beta_{T} & =\bar{\partial}_{A_{ \pm \infty}}^{*} \beta_{ \pm \infty} \\
& =0 .
\end{aligned}$$
Thus, the right hand side of Equation 6.9 is a sum of a priori non-negative terms and some terms which go to zero as $T \mapsto \infty$. Hence, the non-negative terms must vanish, proving the theorem. \(\square\)

Remark 6.6. It follows from the above result, along with the compatibility condition Equation 6.6, that there are no flow lines connecting critical manifolds of opposite sign, i.e. $\mathcal{C}^{ \pm}\left(\mathbf{e}_{1}\right)$ to $\mathcal{C}^{\mp}\left(E_{2}\right)$.

Remark 6.7. The Serre duality operator on $R^{o}$ induces an identification between the space of flows from $\mathcal{C}^{+}\left(E_{1}\right)$ to $\mathcal{C}^{+}\left(E_{2}\right)$ with the space of flows from $\mathcal{C}^{-}\left(E_{1}\right)$ to $\mathcal{C}^{-}\left(E_{2}\right)$. Similarly for flows between $\mathcal{C}^{ \pm}\left(E_{1}\right)$ and the reducible locus $\mathfrak{J}$.

\section*{7. Extending Holomorphic Data.}

Our goal in this section is to pass from the decaying vortex data over the cylinder $R^{o}$ from Proposition 6.5, to data over the closed ruled surface $R$.

In light of the duality between positive and negative vortices (Remark 6.7), we can assume without loss of generality that all Kähler vortices over curves are positive, i.e. vortices for which the $\alpha$-component does not vanish identically (hence $\beta \equiv 0$ ). We return to the reducible case in Section 10.

Let $E^{o} \rightarrow R^{o}$ be a (Hermitian) orbifold line bundle over the cylinder $\mathbb{R} \times Y$, and $E_{ \pm}$be a pair of Hermitian orbifold bundles over $\Sigma$, containing vortices ( $A_{ \pm}, \alpha_{ \pm}$).

Definition 7.1. A pair
$$(A, \alpha) \in \mathcal{A}\left(E^{o}\right) \times \Gamma\left(R^{o}, E^{o}\right)$$
is said to connect the vortex $\left(A_{-}, \alpha_{-}\right)$to $\left(A_{+}, \alpha_{+}\right)$if there are isomorphisms
$$j_{ \pm}:\left.\pi^{*}\left(E_{ \pm}\right)\right|_{R^{o} \rightarrow E^{o}}$$
and a real number $\delta>0$, so that for all $k \in \mathbb{Z}$ with $k \geq 0$,
$$\begin{aligned}
& \lim _{t \mapsto \pm \infty} e^{ \pm \delta t}\left(\left\|\nabla_{c y l}^{(k)}\left(j_{ \pm}^{*}(A)-\pi^{*}\left(A_{ \pm}\right)\right)\right\|_{\{t\} \times Y}\right. \\
&\left.+\left\|\nabla_{\pi^{*}\left(A_{ \pm}\right)}^{(k)}\left(j_{ \pm}^{*}(\alpha)-\pi^{*}\left(\alpha_{ \pm}\right)\right)\right\|_{\{t\} \times Y}\right) \mapsto 0 .
\end{aligned}$$

Definition 7.2. A pair $(A, \alpha)$ is called a generalized vortex if it satisfies:
$$\begin{aligned}
2 \Lambda F_{A}-\Lambda \pi^{*}\left(F_{K_{\Sigma}}\right) & =i|\alpha|^{2} \\
F_{A}^{0,2} & =0 \\
\bar{\partial}_{A} \alpha & =0 .
\end{aligned}$$

The moduli space of generalized vortices connecting $E_{-}$to $E_{+}$is obtained by dividing out the space of generalized vortex pairs which connect vortices in $E_{-}$to vortices in $E_{+}$by the action of the gauge group of Hermitian transformations whose derivatives exponentially decay to zero. When
$$0 \leq \operatorname{deg}\left(E_{ \pm}\right)<\frac{\operatorname{deg}\left(K_{\Sigma}\right)}{2},$$
results of Section 6, allow us to view this space as the moduli space of flows $\mathcal{M}\left(\mathcal{C}^{+}\left(E_{1}\right), \mathcal{C}^{+}\left(E_{2}\right)\right)$

Let $E$ be a Hermitian vector bundle over the closed ruled surface $R$, with
$$\left.E\right|_{\Sigma_{-}}=E_{-} \quad \text { and }\left.\quad E\right|_{\Sigma_{+}}=E_{+} .$$
Note that the isomorphism type of $E$ is uniquely determined by $E_{-}$and $E_{+}$.
Definition 7.3. A pair $(A, \alpha) \in \mathcal{A}(E) \times \Gamma(R, E)$ is called a holomorphic pair connecting $E_{-}$to $E_{+}$if it satisfies the equations
$$\begin{aligned}
& F_{A}^{0,2}=0, \\
& \bar{\partial}_{A} \alpha=0 .
\end{aligned}$$
The moduli space of effective divisors connecting $E_{-}$to $E_{+}$, denoted $\mathcal{D}\left(E_{-}, E_{+}\right)$, is obtained by dividing out the space of such holomorphic pairs by the natural action of the complex gauge group $\operatorname{Map}\left(R, \mathbb{C}^{*}\right)$.

Remark 7.4. Strictly speaking, the above definition endows the space of divisors with a topology, but not a deformation theory. The moduli space of
divisors can be given a deformation theory, locally modeling a neighborhood of the divisor $[A, \alpha]$ on the zeros of a map
$$H^{0}\left(\alpha^{-1}(0),\left.E\right|_{\alpha^{-1}(0)}\right) \rightarrow H^{1}\left(\alpha^{-1}(0),\left.E\right|_{\alpha^{-1}(0)}\right) .$$
We will return to this point in Section 9.
Definition 7.5. Given a subset $C \subset R$, a divisor $[A, \alpha] \in \mathcal{D}\left(E_{-}, E_{+}\right)$is said to contain $C$ if it is represented by a pair $(A, \alpha)$ for which $\left.c\right|_{C} \equiv 0$.

Theorem 7.6. There is a natural identification between the moduli space of generalized vortices connecting $E_{-}$to $E_{+}$, with the open subset of divisors in $\mathcal{D}\left(E_{-}, E_{+}\right)$which do not contain $\Sigma_{-}$or $\Sigma_{+}$.

We break this theorem up into two parts. First (Theorem 7.7), we show that a generalized vortex which connects the vortex $\left(A_{-}, \alpha_{-}\right)$to $\left(A_{+}, \alpha_{+}\right)$ completes canonically to a holomorphic pair interpolating between these two vortices. The methods are essentially in [15] and [3]. In fact, since the structure group in question here is $U(1)$ rather than $S U(2)$ bundles, the arguments are rather simpler; but we include them for completeness. Then, in Section 8, we will describe how to invert this operation.

The rest of this section will focus on the following analogue of Guo's theorem [15]:

Theorem 7.7. Let $(A, \alpha)$ be a generalized vortex in $R^{o}$ connecting ( $A_{-}, \alpha_{-}$) to $\left(A_{+}, \alpha_{+}\right)$. Then $(A, \alpha)$ admits a canonical extension to a holomorphic pair in $R$ which connects $\left(A_{-}, \alpha_{-}\right)$to $\left(A_{+}, \alpha_{+}\right)$.

First, we concentrate on the easier problem of canonically extending the section $\alpha$.

Lemma 7.8. Given a generalized vortex $(A, \alpha)$ in the line bundle $E^{o}$ over $R^{o}$ which connects vortices ( $A_{ \pm}, \alpha_{ \pm}$) in $E_{ \pm}$, there is a line bundle $\widehat{E}$ over $R$, a continuous section $\widehat{\alpha} \in \Gamma(R, \widehat{E})$, and an isomorphism
$$k:\left.\widehat{E}\right|_{R^{o}} \rightarrow E$$
with
$$k^{*}(\alpha)=\left.\widehat{\alpha}\right|_{R^{o}} .$$
The isomorphism class of the triple $(\widehat{E}, \widehat{\alpha}, k)$ is uniquely determined by the isomorphism class of the generalized vortex $(A, \alpha)$.

Proof. Let $\widehat{E}$ be the bundle obtained by gluing $\pi^{*}\left(E_{ \pm}\right)$to $E^{o}$ using the isomorphisms $j_{ \pm}$. The section is defined to be $\alpha$ away from $\Sigma_{ \pm}$and it is $\alpha_{ \pm}$ over $\Sigma_{ \pm}$. Continuity of $\widehat{\alpha}$ is an easy consequence of Equation 7.1.

To verify uniqueness of the construction, let $\left(A^{1}, \alpha^{1}\right),\left(A^{2}, \alpha^{2}\right)$ be a pair of generalized vortices in line bundles $E^{1}, E^{2}$ which connect vortices $\left(A_{ \pm}^{i}, \alpha_{ \pm}^{i}\right)$ $i=1,2$, and let $\left(\widehat{E}^{i}, \widehat{\alpha}^{i}, k^{i}\right) i=1,2$ be the respective extensions. Suppose moreover that $E^{1} \cong E^{2}$ via an isomorphism $\ell: E^{1} \rightarrow E^{2}$. Then there is a continuous isomorphism
$$\widehat{\ell}: \widehat{E}^{1} \rightarrow \widehat{E}^{2}$$
which extends the isomorphism
$$\left(k^{2}\right)^{-1} \circ \ell \circ k^{1}:\left.\left.\widehat{E}^{1}\right|_{R^{o}} \rightarrow \widehat{E}^{2}\right|_{R^{o}},$$
and is compatible with the sections, in the sense that
$$\widehat{\ell}^{*}\left(\widehat{\alpha}_{2}\right)=\widehat{\alpha}_{1} .$$

It suffices to prove that the bundle map
$$\left.\pi^{*}\left(E_{+}^{1}\right)\right|_{R^{o} \rightarrow \pi^{*}\left(E_{+}^{2}\right) \mid{ }_{R^{o}}}$$
defined by
$$\lambda=j_{2}^{-1} \circ \ell \circ j_{1}$$
extends continuously over $\Sigma_{+} \subset R$. Viewing $\lambda$ as a section of the Hermitian line bundle with connection $\pi^{*}\left(\left(E_{+}^{1}\right)^{*} \otimes E_{+}^{2}\right)$ (the connections induced by $\left.A_{+}^{i} i=1,2\right)$, Equation 7.1 implies that
$$\lim _{t \mapsto+\infty} e^{t \delta}\|\nabla \lambda\|_{\{t\} \times Y} \mapsto 0 .$$
This latter condition ensures that $\lambda$ extends as a continuous section over $R- \Sigma_{-}$. Repeating this construction over $\Sigma_{-}$, we get the required isomorphism $\widehat{\ell}$. The compatibility of the sections follows from the fact that $\widehat{\ell}^{*}\left(\widehat{\alpha}_{1}\right)$ and $\widehat{\alpha}_{2}$ are continuous sections which agree on the dense subset $R^{o} \subset R$. \(\square\)

We turn our attention to extending the holomorphic structure from from $E^{o}$ to $\widehat{E}$ in such a way as to make $\widehat{\alpha}$ holomorphic. Once again, this holomorphic structure is canonically determined by the original generalized vortex $(A, \alpha)$. Suppose that $\left(\widehat{E}_{1}, \widehat{\alpha}_{1}, k_{1}\right),\left(\widehat{E}_{2}, \widehat{\alpha}_{2}, k_{2}\right)$ are extensions of generalized vortices $\left(A_{1}, \alpha_{1}\right),\left(A_{2}, \alpha_{2}\right)$ in bundles $E_{1}, E_{2}$, which are identified by a bundle isomorphism
$$\widehat{\ell}: \widehat{E}_{1} \rightarrow \widehat{E}_{2} .$$

Then, $\widehat{\alpha}_{1}=\widehat{\ell}^{*}\left(\widehat{\alpha}_{2}\right)$ is holomorphic with respect to both connections $\widehat{A}_{1}$ and $\widehat{\ell}^{*}\left(\widehat{A}_{2}\right)$. Thus,
$$\left(\widehat{A}_{1}-\widehat{\ell}^{*}\left(\widehat{A}_{2}\right)\right)^{0,1} \otimes \widehat{\alpha}_{1}=0$$
forcing $\widehat{A}_{1}-\widehat{\ell}^{*}\left(\widehat{A}_{2}\right)=0$ on the dense open set where $\widehat{\alpha}_{1} \neq 0$, so that $\widehat{A}_{1}=\widehat{\ell}^{*}\left(\widehat{A}_{2}\right)$ everywhere.

For notational simplicity, we will discuss the extension from $R^{o} \cong Y \times_{S^{1}}$ $(\mathbb{C}-0)$ across its zero-section, $\Sigma_{-}$, to $Y \times_{S^{1}} \mathbb{C} \cong R-\Sigma_{+}$. (Though the discussion applies to both ends of $R^{o}$, giving the requisite extension to all of $R$.)

Let $g_{\circ}$ be the metric on on $\mathbb{R} \times Y$ given by the formula
$$g_{\circ}=r^{2}\left(d t^{2}+\eta^{2}\right)+g_{\Sigma},$$
where $r=e^{t}$. Let $\nabla_{\circ}$ be the connection on $T^{*} R^{o}$ characterized by the properties that
$$\begin{gathered}
\nabla_{\mathrm{o}} d t=-d t \otimes d t+\eta \otimes \eta, \\
\nabla_{\mathrm{o}} \eta=-d t \otimes \eta-\eta \otimes d t, \\
\nabla_{\mathrm{o}} \pi^{*} \theta=\pi^{*}\left(\nabla_{\Sigma} \theta\right) .
\end{gathered}$$
Then, we have the following:
Lemma 7.9. Under the natural holomorphic identification
$$R^{o} \cong Y \times_{S^{1}}(\mathbb{C}-0),$$
the metric $g_{\circ}$ and the compatible connection $\nabla_{\circ}$ extend as an orbifold metric and compatible connection over $T^{*}\left(Y \times_{S^{1}} \mathbb{C}\right)$, with orbifold singularities only at the orbifold points of $Y \times_{S^{1}} \mathbb{C}$.

Proof. The connection on $\pi: Y \rightarrow \Sigma$ induces an splitting
$$T_{y} Y \cong T_{\pi(y)} \Sigma \oplus T_{0} \mathbb{C} .$$
The metric $g_{\mathrm{o}}$ and connection $\nabla_{\mathrm{o}}$ are the metric and connection induced by this splitting. \(\square\)

Remark 7.10. There is a considerable amount of leeway in the choices here - there are many metrics and compatible connections which extend over $\Sigma$; we have made choices which require a minimum of calculation.

Given a $T \in \mathbb{R}$, let $\mathcal{N}_{T}$ denote subset of $R^{o}$ given by
$$\left.\mathcal{N}_{T}=\{(t, y) \mid t<T\}\right) .$$

Lemma 7.11. Given $k \in \mathbb{N}, T \in \mathbb{R}$, there is a constant $C$ such that for any $a \in \Omega^{1}\left(\mathcal{N}_{T}, \mathbb{C}\right)$, we have
$$\left|\nabla_{\circ}^{(k)} a\right|_{\circ} \leq C r^{-(k+1)}\left(\sum_{j=0}^{k}\left|\nabla_{c y l}^{(j)} a\right|_{c y l}\right) .$$
Here, $\|_{\circ}$ and $\|_{\text {cyl }}$ indicate the pointwise metrics $g_{\circ}$ and $g_{\text {cyl }}$ induce on the spaces of tensors, and
$$\nabla_{\circ}^{(j)}, \nabla_{c y l}^{(j)}: \Omega^{1}\left(\mathcal{N}_{T}, \mathbb{C}\right) \rightarrow \Gamma\left(\mathcal{N}_{T} ;\left(\Lambda^{1}\right)^{\otimes(j+1)}\right)$$
are the operators induced by iterating the covariant derivatives.

Proof. It is clear from the formulas for $g_{\text {cyl }}$ and $g_{\circ}$ that there exists a constant $C_{1}$ (depending on $j$ ) such that for any $a \in \Gamma\left(\mathcal{N}_{T} ;\left(\Lambda^{1}\right)^{\otimes(j)}\right)$, we have
$$|a|_{\circ} \leq C_{1} r^{-j}|a|_{c y l} .$$

We have that $\nabla_{\circ}-\nabla_{\text {cyl }}$ is a zeroth order operator
$$\Gamma\left(\mathcal{N}_{T} ;\left(\Lambda^{1}\right)^{\otimes(j)}\right) \rightarrow \Gamma\left(\mathcal{N}_{T} ;\left(\Lambda^{1}\right)^{\otimes(j+1)}\right) .$$
When $j=1$, the operator is given by
$$a \mapsto\langle a, d t\rangle_{c y l}(-d t \otimes d t+\eta \otimes \eta)+\langle a, \eta\rangle_{c y l}(-d t \otimes \eta-\eta \otimes d t) ;$$
so for any $j$ there is a constant $C_{2}$ such that for any $a \in \Gamma\left(\mathcal{N}_{T} ;\left(\Lambda^{1}\right)^{\otimes(j)}\right)$,
$$\left|\left(\nabla_{\circ}-\nabla_{c y l}\right) a\right|_{c y l} \leq C_{2}|a|_{c y l} .$$
Since $\eta$ and $d t$ are $\nabla_{\text {cyl }}$-constant forms, we see that there is a constant $C_{3}$ such that
$$\left|\left[\nabla_{c y l}, \nabla_{\circ}-\nabla_{c y l}\right] a\right|_{c y l} \leq C_{3}\left|\nabla_{c y l} a\right| .$$
Thus, we have
$$\begin{aligned}
\left|\nabla_{\circ}^{(k)} a\right|_{c y l} & =\left|\left(\nabla_{c y l}+\left(\nabla_{\circ}-\nabla_{c y l}\right)\right)^{(k)} a\right|_{c y l} \\
& \leq C_{4} \sum_{j=0}^{k}\left|\nabla_{c y l}^{(j)} a\right|_{c y l}
\end{aligned}$$

The formula now follows from this together with Equation 7.2. \(\square\)

Suppose for simplicity that $\Sigma$ has no marked points. The bundle structure of $\pi: Y \rightarrow \Sigma$ provides us with an open cover $\left\{U_{i}\right\}$ of $\Sigma$, a corresponding cover $\left\{\mathcal{U}_{i}\right\}$ of $Y \times_{S^{1}} \mathbb{C}$, and complex trivializations
$$\tau_{i}: U_{i} \times \mathbb{C} \rightarrow \mathcal{U}_{i} .$$
Consider now the $m$-fold branched cover
$$\phi_{m}: \mathcal{U}_{i}^{m} \rightarrow \mathcal{U}_{i},$$
where $\mathcal{U}_{i}^{m}$ is the complex space $U_{i} \times \mathbb{C}$, and $\phi_{m}$ is given by the formula
$$\phi_{m}(w, z)=\left(w, z^{m}\right) .$$
The space $U_{i} \times S^{1} \times \mathbb{R}$ admits two canonical metrics, a cylindrical metric given by the formula
$$g_{c y l}=d t^{2}+\left(\frac{1}{m} \phi_{m}^{*} \eta\right)^{2}+g_{\Sigma},$$
and a disk metric
$$g_{\circ}=r^{2}\left(d t^{2}+\left(\frac{1}{m} \phi_{m}^{*} \eta\right)^{2}\right)+g_{\Sigma},$$
which completes over $\mathcal{U}_{i}^{m}$ under the natural holomorphic identification
$$U_{i} \times S^{1} \times \mathbb{R} \cong U_{i} \times(\mathbb{C}-0) \subset \mathcal{U}_{i}^{m} .$$
Since $\phi_{m}^{*}(r)=r^{m}$, if $a \in \Omega^{1}\left(\mathcal{U}_{i}, \mathbb{C}\right)$, satisfies $a \in L_{k, \delta}^{2}$ with respect to the cylindrical metric for some real $\delta>0$ and integral $k \geq 0$, then $\phi_{m}^{*} a \in L_{k, m \delta}^{2}$. Thus, given any $k, a \in \Omega^{1}\left(R^{o}, \mathbb{C}\right)$, with
$$a \in L_{k, \delta}^{2},$$
Lemma 7.11 guarantees that we can find $m$ large enough that for each open set $\mathcal{U}_{i}^{m}$,
$$\phi_{m}^{*}(a) \in L_{k, l o c}^{2}\left(\Omega^{1}\left(\mathcal{U}_{i}^{m}, \mathbb{C}\right)\right) .$$
Moreover, when $k \geq 2, \phi_{m}^{*}(a)$ continuously extends over $U_{i} \times\{0\} \subset \mathcal{U}_{i}^{m}$ by vanishing on this subset, thanks the inclusion $L_{k, l o c}^{2} \subset \mathcal{C}^{0}$.

Recall the following version of the $\bar{\partial}$-Poincaré lemma:

Theorem 7.12. Let $X$ be a complex manifold. If $a \in L_{k}^{2}\left(\Omega^{1}(X, \mathbb{C})\right)$ for $k \geq \operatorname{dim}_{\mathbb{C}} X$ satisfies $\bar{\partial} a^{0,1}=0$, then there is an open cover $\left\{V_{j}\right\}$ of $X$ and a collection of invertible functions $\left\{g_{j} \in L_{k+1}^{2}\left(V_{j}\right)\right\}$ with the property that
$$\bar{\partial} g_{j}=-a^{0,1} g_{j} .$$
If $\Sigma \subset X$ is a complex submanifold with the property that $\left.a\right|_{\Sigma} \equiv 0$, then we can arrange that the $g_{i}$ satisfy
$$\left.g_{j}\right|_{\Sigma} \equiv 1 .$$
Proof. The existence of invertible functions $g_{j}$ satisfying Equation 7.3 is standard (see for example [6]). Since $\left.a\right|_{\Sigma}=0$, the $g_{j}$ are holomorphic over $\Sigma$, so we can find holomorphic functions $h_{j}$ defined over the $V_{j}$ which hit $\Sigma$ such that $h_{j}=g_{j}^{-1}$ over $\Sigma \cap V_{j}$. The functions $h_{j} g_{j}$ now satisfy both Equations 7.3 and 7.4. \(\square\)

Given the generalized vortex $(A, \alpha)$ from Theorem 7.7, we have that the difference one-form $a=j_{-}^{*}(A)-\pi^{*}\left(A_{-}\right)$lies in the Sobolev space $L_{k, \delta}^{2}\left(R^{o}\right)$ for any $k \in \mathbb{Z}$. Combining Lemma 7.11 (and the discussion following it), together with Theorem 7.12, we see that there is a natural number $m$, an open cover $\mathcal{U}_{i}$ of a neighborhood of $\Sigma$ (obtained by shrinking the original $\mathcal{U}_{i}$, and possibly reindexing), a collection of holomorphic maps
$$\phi_{m}: \mathcal{U}_{i}^{m} \rightarrow \mathcal{U}_{i},$$
which are $m$-fold branched covers branching over $\mathcal{U}_{i} \cap \Sigma$, and invertible functions
$$g_{i}: \mathcal{U}_{i}^{m} \rightarrow \mathbb{C}$$
satisfying
$$\bar{\partial} g_{i}=-a^{0,1} g_{i}$$
and
$$\left.g_{i}\right|_{\mathcal{U}_{i}^{m} \cap \Sigma} \equiv 1 .$$

The $\mathbb{Z} / m \mathbb{Z}$ action on the $\mathcal{U}_{i}^{m}$ lifts naturally to an action on $\phi_{m}^{*}(E)$; indeed, as the connections $A$ and $A_{-}$pull back from $\mathcal{U}_{i} \subset R$, both connections,
and their difference $a$, are invariant under the $\mathbb{Z} / m \mathbb{Z}$ action. So, replacing $g_{i}$ by its average
$$\frac{1}{m} \sum_{\gamma \in \mathbb{Z} / m \mathbb{Z}} \gamma^{*} g_{i},$$
we get a new collection of smooth functions, still denoted $g_{i}$, satisfying Equations 7.5 and 7.6, but which are now $\mathbb{Z} / m \mathbb{Z}$-invariant. By Equation 7.6, we see that, after perhaps shrinking the $\mathcal{U}_{i}$, we can arrange that these functions $g_{i}$ are invertible over $\mathcal{U}_{i}$. Since the $\mathbb{Z} / m \mathbb{Z}$-invariant continuous functions on $\mathcal{U}_{i}^{m}$ correspond to the continuous functions on the quotient $\mathcal{U}_{i}$, we can think of the $\left\{\left(\mathcal{U}_{i}^{m}, g_{i}\right)\right\}$ as defining a Čech cochain $\left\{\left(\mathcal{U}_{i}, \widehat{g}_{i}\right)\right\}$ defined over a neighborhood of $\Sigma \subset Y \times_{S^{1}} \mathbb{C} \subset R$ with values in the continuous invertible functions. Since the $\mathbb{Z} / m \mathbb{Z}$ action on $\mathcal{U}_{i}^{m}$ is free away from $\Sigma \cap \mathcal{U}_{i}^{m}$, we have that the $\widehat{g}_{i}$ are smooth away from $\mathcal{U}_{i} \cap \Sigma$. Equation 7.5 translates into the equation over $\mathcal{U}_{i}-\mathcal{U}_{i} \cap \Sigma$
$$\bar{\partial} \widehat{g}_{i}=-a \widehat{g}_{i}$$
and Equation 7.6 translates into
$$\left.\widehat{g}_{i}\right|_{\mathcal{U}_{i} \cap \Sigma} \equiv 1 .$$

Lemma 7.13. The coboundary of the cochain $\left\{\left(\mathcal{U}_{i}, \widehat{g}_{i}\right)\right\}$ takes values in the sheaf of invertible holomorphic functions, i.e.
$$\delta\left\{\left(\mathcal{U}_{i}, \widehat{g}_{i}\right)\right\} \in Z^{1}\left(\left\{\mathcal{U}_{i}\right\}, \mathcal{O}_{R}^{*}\right) .$$

Proof. The functions $\widehat{g}_{i, j}$
$$\widehat{g}_{i, j}=\widehat{g}_{i}^{-1} \widehat{g}_{j}$$
are holomorphic over all of $\mathcal{U}_{i} \cap \mathcal{U}_{j}$, because they are continuous, and they satisfy
$$\bar{\partial}\left(\widehat{g}_{i} \widehat{g}_{j}^{-1}\right)=0$$
over $\mathcal{U}_{i} \cap \mathcal{U}_{j} \cap(R-\Sigma)$, by Equation 7.7. So they are holomorphic over all of $\mathcal{U}_{i} \cap \mathcal{U}_{j}$ by the regularity of the $\bar{\partial}$ operator. \(\square\)

Thus, the cocycle $\delta\left\{\left(\mathcal{U}_{i}, \widehat{g}_{i}\right)\right\}$ naturally induces a holomorphic line bundle $F$ over $Y \times_{S^{1}} \mathbb{C}$, and the cochain $\left\{\left(\mathcal{U}_{i}, \widehat{g}_{i}\right)\right\}$ glues together to induce a continuous trivialization $\widehat{g}$ of $F$.

Lemma 7.14. The topological isomorphism
$$j_{-} \otimes \widehat{g}:\left.\pi^{*}\left(E_{-}\right) \otimes F\right|_{R^{o}} \rightarrow E^{o}$$
induces an isomorphism of holomorphic bundles
$$\left.\left(E, \bar{\partial}_{A}\right) \cong\left(\pi^{*}\left(E_{-}\right) \otimes F, \bar{\partial}_{\pi^{*}\left(A_{-}\right) \otimes F}\right)\right|_{R^{o}} .$$

Proof. This is an easy consequence of Equation 7.7:
$$\begin{aligned}
\widehat{g}_{j} \circ \bar{\partial}_{A_{-}} \circ \widehat{g}_{j}^{-1}-\bar{\partial}_{A} & =a^{0,1}+\widehat{g}_{j}\left(\bar{\partial} \widehat{g}_{j}^{-1}\right) \\
& =a^{0,1}-\left(\bar{\partial} \widehat{g}_{j}\right) \widehat{g}_{j}^{-1} \\
& =0 .
\end{aligned}$$ \(\square\)

The pull-back of $\widehat{\alpha}$ to $\pi^{*}\left(E_{-}\right) \otimes F$ via the isomorphism induced by $\widehat{g}$ is a continuous section of $\pi^{*}\left(E_{-}\right) \otimes F$ which is holomorphic away from $\Sigma_{-}$. The regularity of $\bar{\partial}_{A_{-} \otimes F}$, in fact, ensures that it is a holomorphic section over all of $Y \times_{S^{1}} \mathbb{C}$.

The above discussion easily generalizes in the presence of orbifold points on $\Sigma$. The key point is that the construction of the $\widehat{g}_{i}$ can be made $\mathbb{Z} / \alpha_{i} \mathbb{Z}$ -equivariantly, by averaging over this group.

This concludes the proof of Theorem 7.7. Our results can be rephrased as follows:

Theorem 7.15. Let $E_{1}, E_{2}$ be a pair of orbifold line bundles over $\Sigma$ with
$$0 \leq \operatorname{deg}\left(E_{i}\right)<\frac{\operatorname{deg}\left(K_{\Sigma}\right)}{2} .$$
The canonical extension procedure used in Theorem 7.7 induces a continuous map
$$\mathcal{M}\left(\mathcal{C}^{+}\left(E_{1}\right), \mathcal{C}^{+}\left(E_{2}\right)\right) \rightarrow \mathcal{D}\left(E_{1}, E_{2}\right) .$$
Proof. The fact that the map induces a well-defined map on the level of gauge equivalence classes follows immediately from the uniqueness statement in Theorem 7.7.

Continuity follows from a corresponding continuity statement in the solution to the $\bar{\partial}$-problem from Theorem 7.12. \(\square\)

\section*{8. Vortices over Cylinders.}

In Section 7, we showed how a generalized vortex could be canonically completed to give a divisor in the ruled surface $R$. Presently, we turn our attention to the converse problem:

Theorem 8.1. Let $E_{-}, E_{+}$be a pair of orbifold bundles over $\Sigma$, with
$$0 \leq \operatorname{deg}\left(E_{ \pm}\right)<\frac{\operatorname{deg}\left(K_{\Sigma}\right)}{2} .$$
Suppose that $(A, \alpha)$ is a holomorphic pair connecting $E_{-}$to $E_{+}$such that $\left.\alpha\right|_{\Sigma_{-}} \not \equiv 0$ and $\left.\alpha\right|_{\Sigma_{+}} \not \equiv 0$, then there is a complex gauge transformation, $g$, defined over $R^{o}$ which carries the restriction $\left.(A, \alpha)\right|_{R^{o}}$ to a generalized vortex connecting $E_{-}$to $E_{+}$. The complex gauge transformation $g$ is unique up to unitary gauge tranformations defined on the cylinder.

The first step in the proof is to show that a holomorphic pair as in the thoerem gives rise to a holomorphic pair on the cylinder which connects the corresponding vortices. Indeed, we can arrange, after a complex gauge transformation, that the restriction of $\left.(A, \alpha)\right|_{\Sigma_{ \pm}}$satisfies the Kähler vortex equations over $\Sigma_{ \pm}$, according to Theorem 5. Furthermore, any two such complex gauge transformation differ over $\Sigma_{ \pm}$by a unitary gauge transformation. The first step is completed by the following lemma.

Lemma 8.2. Let $(A, \alpha)$ be a pair in $E \rightarrow R$, whose restrictions $\left(A_{ \pm}, \alpha_{ \pm}\right)$to $\Sigma_{ \pm}$satisfy the Kähler vortex equations. Then there is a real number $\gamma>0$ such that the pair $\left.(A, \alpha)\right|_{R^{o}}$ connects $\left(A_{-}, \alpha_{-}\right)$to $\left(A_{+}, \alpha_{+}\right)$with exponent one.

Proof. This follows easily from Taylor's theorem. \(\square\)

Given a holomorphic pair $(A, \alpha)$ over $R^{o}$ which arises as above, we wish to find a real-valued function $u$ (defined over $R^{o}$ ) so that $e^{u}(A, \alpha)$ satisfies Equation 7.2. Watching how its terms transform under the action of $e^{u}$, we rewrite this equation as a second-order, Kazdan-Warner type equation for u:
$$-2 i \Delta_{c y l} u+2 \Lambda F_{A}-\Lambda \pi^{*}\left(F_{K_{\Sigma}}\right)=i e^{2 u}|\alpha|^{2},$$
where
$$\Delta_{c y l}=2 i \Lambda \bar{\partial} \partial,$$
and $\Lambda$ denotes the operation of inner product with the canonical $(1,1)$ form for the cylindrical metric on $R^{o}$. Theorem 8.1 follows immediately from the next proposition concerning the existence and uniqueness of such a $u$ after making the subsitutions $h=|\alpha|^{2}$ and $k=-2 i \Lambda F_{A}+i \Lambda \pi^{*}\left(F_{K_{\Sigma}}\right)-$ $h$. The hypotheses are satisfied thanks to the exponential convergence in Lemma 8.2.

Proposition 8.3. Suppose that $Y$ is oriented so that $\operatorname{deg}(Y)<0$. Let
$$h: R^{o} \rightarrow \mathbb{R}$$
be a smooth, bounded, non-negative function which converges exponentially as $t \mapsto \pm \infty$ to a pair of functions
$$h_{ \pm}: Y \rightarrow \mathbb{R}$$
with $h_{-} \not \equiv 0$, and let $\mathcal{N}$ be the operator defined by
$$\mathcal{N}(u)=\Delta_{\text {cyl }}(u)+h\left(e^{u}-1\right) .$$
Then, given any smooth function $k \in \mathcal{C}_{\gamma}^{\infty}$, with $\gamma>0$ there is an $\epsilon>0$ and a unique function $u \in \mathcal{C}_{\epsilon}^{\infty}\left(R^{o}\right)$ satisfying
$$\mathcal{N}(u)=k .$$

Remark 8.4. Recall that a smooth function $u: R^{o} \rightarrow \mathbb{R}$ is in $\mathcal{C}_{\epsilon}^{\infty}$ if for each $k$, the function $\left(\nabla^{(k)} f\right) e^{\epsilon|t|}$ is bounded.

Remark 8.5. If $Y$ is given the other orientation, Equation 8.1 can be solved when $h_{+} \not \equiv 0$. Thus, for the purposes of Theorem 8.1, the orientation is irrelevant.

Remark 8.6. The above proposition should be compared with [23], where a similar operator is solved over a closed manifold.

The operator $\Delta_{\text {cyl }}$ can be understood quite concretely, comparing it with the Laplacian for the Kähler metric on $\mathbb{R} \times Y$, see for example [15] or [20], where the following lemma is proved:

Lemma 8.7. The operator $\Delta_{\text {cyl }}$ can be written
$$\Delta_{c y l}=-e^{-2 \xi t} \frac{\partial}{\partial t} e^{2 \xi t} \frac{\partial}{\partial t}+\Delta_{Y},$$
where $\Delta_{Y}$ is the ordinary Laplacian on the three-manifold $Y$.

Here, $\xi$ is the constant defined in Equation 5.4.
First, we show uniqueness for the scale $u$ which carries the pair $(A, \alpha)$ to a generalized vortex, using a lemma which will be useful in the existence argument as well.

Lemma 8.8. Let $u$ and $v$ be smooth functions vanishing at infinity, with the property that
$$\mathcal{N}(u) \leq \mathcal{N}(v)$$
pointwise, then
$$u \leq v$$
pointwise, as well.

Proof. This follows easily from the maximum principle, together with the monotonicity of the exponential map. We wish to show that $u \leq v$ globally. If not, then there must be a point $x$ and a real number $\delta>0$ such that $u(x)-v(x)>\delta$. Consider the set
$$\Omega_{\delta}=\left\{x \in R^{o} \mid u-v \geq \delta\right\} .$$
Since $u-v$ vanishes at infinity, each $\Omega_{\delta}$ is a bounded set. Moreover, from its definition and the choice of $\delta$, we see that the function $u-v$ cannot achieve its maximum on the boundary of $\Omega_{\delta}$. The assumption that $\mathcal{N}(u) \leq \mathcal{N}(v)$ forces $\Delta_{\text {cyl }}(u-v) \leq 0$ on $\Omega_{\delta}$, hence by the maximum principle for the Laplace-type operator $\Delta_{\text {cyl }}$, the function $u-v$ must achieve its maximum on the boundary, a contradiction. \(\square\)

Of course, this lemma guarantees that for any function $k$, the equation $\mathcal{N}(u)=k$ can have at most one solution which vanishes at infinity.

The rest of this section is devoted to the proof of the existence statement in Proposition 8.3, using the continuity method. That is, we will show that for each $s \in[0,1]$, there is a solution $u_{s}$ to the equation
$$\mathcal{N}\left(u_{s}\right)=s k,$$
by showing the set of $s$ for which a solution $u_{s}$ exists is closed and open. Since the set is non-empty (at $s=0$, the function $u_{0} \equiv 0$ is clearly a solution), we conclude that our desired solution at $s=1$ exists.

We find it convenient to work in the Hilbert space $L_{3, \epsilon}^{2}$, a weighted Sobolev space. This space is defined as follows. Let
$$\tau: \mathbb{R} \rightarrow \mathbb{R}$$
be a positive, smooth function with
$$\tau(t)=|t| \quad \text { when } \quad|t|>1 .$$
Now, $L_{\ell, \epsilon}^{2}$ is by definition the completion of $C_{c}^{\infty}\left(R^{o}\right)$ under the norm
$$\|u\|_{L_{\ell, \epsilon}^{2}}=\int_{R^{o}}\left(|u|^{2}+|\nabla u|^{2}+\left|\nabla^{(2)} u\right|^{2}+\ldots+\left|\nabla^{(\ell)} u\right|^{2}\right) e^{\epsilon \tau} \mu_{R^{o} .}$$

Lemma 8.9. For all $\epsilon>0$, the operator $\mathcal{N}$ extends to a smooth operator
$$\mathcal{N}: L_{3, \epsilon}^{2} \rightarrow L_{1, \epsilon}^{2},$$
with derivative
$$D \mathcal{N}_{u}(v)=\left(\Delta_{c y l}+e^{u} h\right)(v) .$$
Proof. Let $g_{1}$ be the analytic function on $\mathbb{R}$ defined by the property that
$$u g_{1}(u)=e^{u}-1 .$$
We notice first that any function $u \in L_{3, \epsilon}^{2}$ must be continuous, and must vanish at infinity, by the continuity of the embedding
$$L_{3, \epsilon}^{2}(\Omega) \subset \mathcal{C}^{0}(\Omega),$$
valid for any bounded domain $\Omega \subset R^{o}$. In fact, the geometry of the cylinder gives us bounds.
$$\|u\|_{\mathcal{C}_{\epsilon / 2}^{0}}^{0} \leq C\|u\|_{L_{3, \epsilon}^{2}},$$
where the $\mathcal{C}_{\delta}^{\ell}$-norm is the weighted norm defined by
$$\|f\|_{\mathcal{C}_{\delta}^{\ell}}=\sum_{i=1}^{\ell} \sup _{R^{o}} e^{\delta|t|}\left|\nabla^{(i)} f\right| .$$
In particular, $g_{1}(u)$ must be globally bounded:
$$g_{1}(u) \leq \sup _{[-M, M]} g_{1},$$
where
$$M=C\|u\|_{L_{3, \epsilon}^{2}} .$$

Thus,
$$\left\|h\left(e^{u}-1\right)\right\|_{L_{0, \epsilon}^{2}}=\left\|u h g_{1}(u)\right\|_{L_{0, \epsilon}^{2}} \leq\|u\|_{L_{0, \epsilon}^{2}}\left\|h g_{1}(u)\right\|_{\mathcal{C}^{\mathrm{C}}},$$
and similarly
$$\left\|\nabla h\left(e^{u}-1\right)\right\|_{L_{0, \epsilon}^{2}} \leq\|u\|_{L_{0, \epsilon}^{2}}\left\|(\nabla h) g_{1}(u)\right\|_{\mathcal{C}^{0}}+\|\nabla u\|_{L_{0, \epsilon}^{2}}\left\|h e^{u}\right\|_{\mathcal{C}^{0}},$$
so that
$$u \mapsto h\left(e^{u}-1\right)$$
maps $L_{3, \epsilon}^{2}$ to $L_{1, \epsilon}^{2}$. Continuity follows at once from Inequality 8.4, together with the above $L_{0, \epsilon}^{2}$ estimates on $h\left(e^{u}-1\right)$ and its first derivative.

To verify the formula for the derivative, take one more term in the Taylor expansion of $e^{u}$, and use the same kinds of estimates. \(\square\)

Moreover, ellipticity guarantees that any solution lying in this space is smooth.

Lemma 8.10. Suppose $k$ is a $C^{\infty}$ function, and $u \in L_{3, \epsilon}^{2}$ satisfies
$$\mathcal{N}(u)=k,$$
then $u$ is also $C^{\infty}$.

Proof. This is a standard bootstrapping argument using the usual elliptic estimates on $\Delta_{\text {cyl }}$. We will see arguments of this nature in the proof of Lemma 8.12. \(\square\)

The maximum principle from Lemma 8.8, combined with the following lemma, ensure bounds of the form
$$u_{-} \leq u_{s} \leq u_{+},$$
for a pair of exponentially decaying functions $u_{-}$and $u_{+}$.
Lemma 8.11. Let $k \in \mathcal{C}_{\gamma}^{0}$, then there is some $\epsilon_{0}$ such that for all $0<\epsilon<\epsilon_{0}$, there are functions $u_{ \pm} \in \mathcal{C}_{\epsilon}^{\infty}$ with the property that for any $s \in[0,1]$
$$\mathcal{N}\left(u_{-}\right) \leq s k \leq \mathcal{N}\left(u_{+}\right) .$$

The proof of the above lemma is deferred until the end of the section.
Fixing an $\epsilon>0$ and functions $u_{ \pm}$as in the previous lemma, closedness of the set of $s \in[0,1]$ satisfying 8.3 now follows from the standard machinery of Sobolev spaces, as we see in the following lemma.

Lemma 8.12. Let $u_{i}$ be a sequence of functions in $L_{3, \epsilon}^{2}$ with $u_{-} \leq u_{i} \leq u_{+}$, and $u_{ \pm} \in \mathcal{C}_{\epsilon}^{\infty}$, with
$$\lim _{i \mapsto \infty} \mathcal{N}\left(u_{i}\right)=k ;$$
then there is a function $u \in L_{3, \epsilon}^{2}$, with
$$\mathcal{N}(u)=k .$$
Proof. Bootstrapping and compact inclusions of Sobolev spaces, along with the a priori estimates given by $u_{-} \leq u_{i} \leq u_{+}$, together with the equations allow us to extract an $L_{3, \text { loc }}^{2}$-convergent subsequence, which by continuity must solve $\mathcal{N}(u)=k$. Elliptic estimates applied to the equation for $u$ then allow us to conclude that $u$ has the appropriate decay properties. We give the details.

The Friedrich lemma states that for any pair $\Omega \subset \Omega^{\prime} \subset R^{o}$ of precompact open sets and positive integer $\ell$ there is a constant $C>0$ so that
$$\|u\|_{L_{\ell}^{2}(\Omega)} \leq C\left(\|u\|_{L^{2}\left(\Omega^{\prime}\right)}+\left\|\Delta_{c y l} u\right\|_{L_{\ell-2}^{2}\left(\Omega^{\prime}\right)}\right),$$
Moreover, we also have global estimates
$$\|u\|_{L_{\ell, \epsilon}^{2}} \leq C\left(\|u\|_{L_{\epsilon}^{2}}+\left\|\Delta_{c y l} u\right\|_{L_{\ell-2, \epsilon}^{2}}\right),$$
thanks to the $\mathbb{R}$-invariance of $\Delta_{\text {cyl }}$, and the geometry of the cylinder.
To be able to use compactness, we will first derive local uniform $L_{4}^{2}$ bounds on the sequence $u_{i}$. Fix a pair of pre-compact regions $\Omega \subset \Omega^{\prime} \subset R^{o}$. The equation for $u_{i}$ together with the elliptic estimate gives
$$\begin{aligned}
\left\|u_{i}\right\|_{L_{2}^{2}\left(\Omega^{\prime}\right)} & \leq C\left(\left\|u_{i}\right\|_{L^{2}}+\left\|\Delta_{c y l} u_{i}\right\|_{L^{2}}\right) \\
& =C\left(\left\|u_{i}\right\|_{L^{2}}+\left\|h\left(e^{u_{i}}-1\right)\right\|_{L^{2}}+\left\|k_{i}\right\|_{L^{2}}\right) .
\end{aligned}$$
Combining this with the uniform bound on the $\left\|k_{i}\right\|_{L^{2}}$ and the uniform pointwise bound on $u_{i}$ by $u_{ \pm}$, gives us a uniform bound on $\left\|u_{i}\right\|_{L_{2}^{2}\left(\Omega^{\prime}\right)}$.

The Rellich lemma then provides a subsequence of the $u_{i}$ which converges in $L_{1}^{2}\left(\Omega^{\prime}\right)$. Hence, using the equation again, together with another elliptic estimate,
$$\begin{aligned}
\left\|u_{i}\right\|_{L_{4}^{2}(\Omega)} & \leq C_{1}\left(\left\|u_{i}\right\|_{L^{2}\left(\Omega^{\prime}\right)}+\left\|\Delta_{c y l} u_{i}\right\|_{L_{2}^{2}\left(\Omega^{\prime}\right)}\right) \\
& \leq C_{2}\left(\left\|u_{i}\right\|_{L_{1}^{2}\left(\Omega^{\prime}\right)}+\left\|\left(\nabla^{(2)} u_{i}\right) h e^{u_{i}}\right\|_{L^{2}\left(\Omega^{\prime}\right)}+\left\|k_{i}\right\|_{L_{i}^{2}\left(\Omega^{\prime}\right)}\right),
\end{aligned}$$
which is uniformly bounded, as we have just established. Thus, by the Rellich lemma once again, we have a subsequence of the $u_{i}$, so that
$$u_{i} \mapsto u \in L_{3}^{2}(\Omega) .$$
The above method constructs a convergent subsequence over any precompact region $\Omega \subset R^{\circ}$. Exhausting $R^{\circ}$ by pre-compact regions, and extracting a diagonal subsequence, we find a subsequence $u_{i}$ converging in $L_{3, l o c}^{2}$ to a function $u$.

Thus, we have our function $u$; we must verify that it has the desired properties. Continuity of $\mathcal{N}$ on $L_{3, \text { loc }}^{2}$, gives
$$\mathcal{N}(u)=k .$$
Continuity of $L_{3}^{2} \hookrightarrow \mathcal{C}^{0}$, shows that the pointwise bounds $u_{-} \leq u_{i} \leq u_{+}$hold in the limit as well, and $u_{-} \leq u \leq u_{+}$. Thus, we get that $u \in \mathcal{C}_{\epsilon}^{0} \subset L_{0, \epsilon}^{2}$. Moreover, the map
$$v \mapsto e^{v}-1$$
clearly extends as a map from
$$\mathcal{C}_{\epsilon}^{0} \rightarrow \mathcal{C}_{\epsilon}^{0} .$$
These facts are enough to start the same bootstrap as above, only this time over the entire cylinder, to get $u \in L_{3, \epsilon}^{2}$ (and indeed, they are enough to get $u \in L_{\ell, \epsilon}^{2}$ for any $\ell$ ). \(\square\)

Openness follows from an application of the inverse function theorem:

Lemma 8.13. The set of $s \in[0,1]$ for which there is a $u_{s}$ solving Equation 8.3 is open.

Proof. Consider the linearization of $\mathcal{N}, D \mathcal{N}_{u}$, given by
$$v \mapsto \Delta_{c y l} v+\left(h e^{u}\right) v,$$
and viewed as a map
$$L_{3, \delta}^{2} \rightarrow L_{1, \delta}^{2},$$
where now $\delta$ is any weight with $0<\delta<\epsilon$. The kernel of the operator is zero by the maximum principle. Also, its cokernel is zero for all sufficiently small positive weights. To see this, note that the Fredholm theory of [24] says $D \mathcal{N}_{u}$ is Fredholm on the doubly-weighted spaces $L_{k, \delta_{-}, \delta_{+}}^{2}$ (i.e. where the weight function looks like $e^{\delta_{ \pm}|t|}$ for $\pm t>1$ ) for all weights $\delta_{-}$and $\delta_{+}$ satisfying
$$-2\left(\xi+\sqrt{\xi^{2}+\lambda_{-}}\right)<\delta_{-}<2\left(-\xi+\sqrt{\xi^{2}+\lambda_{-}}\right)$$
and
$$0<\delta_{+}<4 \xi,$$
where $\lambda_{-}$is the smallest non-zero eigenvalue of the positive operator
$$\Delta_{Y}+h_{-} .$$
So, provided that
$$\delta<\min \left(-\xi+\sqrt{\xi^{2}+\lambda_{-}}, 2 \xi\right),$$
we can connect the operator acting on $L_{\delta}^{2}=L_{\delta, \delta}^{2}$ to the same acting on $L_{\xi,-\xi}^{2}$ through a family of Fredholm operators. $D \mathcal{N}_{u}$ is easily seen to be self-adjoint on $L_{\xi,-\xi}^{2}$, so by the homotopy invariance of the index, $D \mathcal{N}_{u}$ on $L_{k, \delta}^{2}$ has index zero.

Thus, the inverse function theorem guarantees that around each $\sigma \in[0,1]$ for which there is some $u_{\sigma} \in L_{3, \epsilon}^{2}$ solving Equation 8.3, there is a real number $\delta \leq \epsilon$ and a neighborhood of values $s$ for which we can find $u_{s} \in L_{3, \delta}^{2}$ solving Equation 8.3. We must show that in fact each such $u_{s} \in L_{3, \epsilon}^{2} \subset L_{3, \delta}^{2}$.

But this follows from the a priori estimate $u_{-}<u_{s}<u_{+}$, which forces $u \in \mathcal{C}_{\epsilon}^{0} \subset L_{0, \epsilon}^{2}$. Now, we can proceed as in the end of the proof of Lemma 8.12. \(\square\)

The proof of Proposition 8.3 and hence Theorem 8.1 will be complete once we prove Lemma 8.11.

Proof. Fix a smooth, non-decreasing cut-off function $\lambda$ on $\mathbb{R}$ such that $\lambda(t)=$ 0 for $t \leq 0$ and $\lambda(t)=1$ for $t \geq 1$. and a smooth, non-negative function $b$ supported in $\left[0, \frac{1}{2}\right]$ with total integral 1.

We begin with two constructions which are used in the definition of $u_{-}$.
Construction 8.14. Given $M>0$, there is a function $\psi_{1} \in \mathcal{C}^{\circ \circ}(\mathbb{R})$ with
$$\begin{gathered}
\psi_{1} \leq 0 \\
-\left({\frac{\partial^{2}}{\partial t}}^{2}+2 \xi \frac{\partial}{\partial t}\right) \psi_{1} \leq 0
\end{gathered}$$
and
$$\psi_{1}(t)=\left\{\begin{array}{ll}
-\frac{M}{\xi} e^{-\xi t} & t \geq 0 \\
-\frac{M}{\xi}+M t & t \leq-1
\end{array} .\right.$$

The two functions we are attempting to glue together (the linear function and the exponential) agree up to first order at $t=0$. So, we smooth out the two derivatives using the bump function $\lambda$, and then integrate this smooth function to get $\psi_{1}$. Integrating the smoothing process decreases the value, which we compensate for by integrating the bump function $b$.

In terms of formulas, define
$$\psi_{1}(s, t)=-M \int_{t}^{\infty}\left(\lambda(s t+s) e^{-\xi t}+(1-\lambda(s t+s))\right) d t$$
For all $s>1$, we have that
$$\psi_{1}(s, t)=-\frac{M}{\xi}+M t-\delta(s),$$
where
$$\lim _{s \mapsto \infty} \delta(s)=0 .$$
So, for large enough $s$, we can arrange that
$$\delta(s)<\max \left(\frac{M}{\sup \left(\left(\frac{\partial}{\partial t}+2 \xi\right) b\right)}, \frac{M}{\sup (b)}\right) .$$
If $s>2$ is large enough to satisfy the above inequalities for $\delta(s)$, then
$$\psi_{1}(t)=\psi_{1}(s, t)+\delta(s) \int_{t}^{0} b(t+1)$$
satisfies all requisite properties.

Construction 8.15. Given $C, M, \epsilon$ positive reals, there is a function $\psi_{2} \in$ $\mathcal{C}^{\infty}(\mathbb{R})$ with
$$\begin{gathered}
\psi_{2}(t) \leq-C e^{\epsilon t}, \\
-\left({\frac{\partial^{2}}{\partial t}}^{2}+2 \xi \frac{\partial}{\partial t}\right) \psi_{2} \leq-\left({\frac{\partial^{2}}{\partial t}}^{2}+2 \xi \frac{\partial}{\partial t}\right)\left(-(C+1) e^{\epsilon t}\right)
\end{gathered}$$
and, for $t \geq 0$,
$$\psi_{2}(t)=-C+M t .$$

Given $\delta$, there is a unique value of $s$ such that the integral
$$-\int_{-\infty}^{t}\left(C \epsilon e^{\epsilon t}(1-\lambda(s t+s))+M \lambda(s t+s)\right) d t$$
satisfies the requirements for $\psi_{2}$.
Now, we make a few preliminary choices.
Letting $m=\sup _{Y} h_{-}$, we can find a function $f \in \mathcal{C}^{\infty}(Y)$ with the property that on the set where $h_{-} \leq \frac{3 m}{4}, \Delta_{\Sigma} f>5 \xi$. This can be done since $\Delta_{\Sigma}$ has a one-dimensional cokernel consisting of constant functions; we just have to find a function $g$ which is larger than $5 \xi$ on the given subset and has total integral 0 over $\Sigma$, and we can solve $f=\Delta_{\text {cyl }}{ }^{-1} g$. We can find such a function $g$ because we have assumed that $h_{-} \not \equiv 0$.

By translating towards $-\infty$, we can assume without loss of generality that
$$\left.\left(h-h_{-}\right)\right|_{(-\infty, 0] \times Y}<\frac{m}{4} .$$
Since $k \in \mathcal{C}_{\gamma}^{0}$, there is some constant $\kappa>0$ with the property that
$$|k| \leq \kappa e^{-\gamma|t|} .$$
Our goal is to construct a function $u_{-}$which satisfies
$$\mathcal{N}\left(u_{-}\right) \leq-\kappa e^{-\gamma|t|} \leq k .$$