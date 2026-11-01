---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Conformal Kähler rigidity of Einstein four-manifolds]

Proof. First, we observe that the construction of the functions $\eta_{\delta, R}$ described in the proof of Theorem 1.9 applies without change in this setting: hence, we just need to verify the capacity condition at infinity, in order to apply Proposition 4.1. Let $\psi_{R}$ be the usual radial cutoff function supported in $B_{h}\left(p_{0}, 2 R\right)$, equal to 1 on $B_{h}\left(p_{0}, R\right)$, and with $\left|d \psi_{R}\right|_{h} \leq C R^{-1}$. On $A_{R}=B_{h}\left(p_{0}, 2 R\right) \backslash B_{h}\left(p_{0}, R\right)$, we can apply Hölder's inequality and use the fact that $\alpha_{h} \leq C\left|\mathrm{Rm}_{h}\right|$ in order to obtain
$$\begin{aligned}
\int_{X}\left|d \psi_{R}\right|_{g}^{2} d \mu_{g} & =\int_{A_{R}} \alpha_{h}^{2 / 3}\left|d \psi_{R}\right|_{h}^{2} d \mu_{h} \\
& \leq C R^{-2}\left(\int_{A_{R}}\left|\operatorname{Rm}_{h}\right|^{2} d \mu_{h}\right)^{1 / 3} \operatorname{Vol}_{h}\left(A_{R}\right)^{2 / 3}=o_{R}(1),
\end{aligned}$$
where the last equality comes from the fact that $\left|\mathrm{Rm}_{h}\right| \in L^{2}$ and the volume assumption. As we did in the proof of Theorem 1.9, we can similarly construct cutoff functions $\chi_{j}$ which satisfy the hypotheses of Proposition 4.1: therefore, after at worst passing to a double cover of $X$, we conclude that $g$ is a Kähler metric with positive scalar curvature on $X$ and, using again [16, Proposition 5(iv)], that $X=M$ as in Theorem 1.9. The classification now follows from the aforementioned classification result of conformally Kähler gravitational instantons due to Li [38, 39]. \(\square\)

Remark 6.4. The proof of Theorem 6.3 can be deduced directly from Theorem 1.9 combined with the curvature decay proved in [12]. Moreover, the proof uses only the bound $\operatorname{Vol}_{h}\left(B_{h}\left(p_{0}, R\right)\right) \leq C R^{3}$ and therefore also yields a rigidity statement for non-ALF collapsed gravitational instantons. Indeed, Li's classification [38] shows that every Type II gravitational instanton is, up to scaling, of ALE, ALF, or AF type. Consequently, if $(M, h)$ is of ALG, ALG*, ALH, or ALH* type and satisfies (1.2), then it must be of Type I and hence locally hyperkähler.

Remark 6.5. The same capacity proof can also be adapted to isolated quotientorbifold singularities. In local uniformizing charts the lifted metric is smooth, so isolated singular points have zero capacity for $\alpha_{h}^{2 / 3} h$; combining these local cutoffs with the annular cutoff at infinity gives the corresponding orbifold variants. We do not state these extensions here.

\section*{7. Sharpness of the spectral condition}

In this section, we provide examples of Ricci-flat four-manifolds $(M, h)$ such that, at a point $p, \alpha_{h}=\beta_{h} \neq 0$ : this shows that the uniform hypothesis on the eigenvalues in Theorems 1.4 and 1.9 is optimal.
7.1. Compact case: K3 surfaces. First, we recall that a hyperkähler manifold $(M, h)$ is a Riemannian manifold endowed with three Kähler structures $I, J$ and $K$, which satisfy the quaternionic relations:
$$I^{2}=J^{2}=K^{2}=I J K=-1 .$$
In dimension four, according to Kodaira's classification of complex surfaces, the only examples of compact hyperkähler manifolds are flat tori and K3 surfaces. It is well known that every K3 surface admits a Kähler metric: the resolution of the Calabi conjecture by Yau ensures that, given any Kähler metric $\hat{h}$ on $M$ with Kähler form $\hat{\omega}$, there exists a unique Kähler Ricci-flat metric $h$ with Kähler form $\omega \in[\hat{\omega}]$ [57]. Furthermore, by [16, Proposition 2], we know that all these metrics are also anti-self-dual with respect to the orientation induced by the hyperkähler structure (see also [27]), which means that the curvature operator is precisely $W_{h}^{-}$. Since the metrics constructed by Yau are not explicit, in general, no explicit formula for the curvature tensor is known. Every K3 surface is spin, and
$$\hat{A}(M)=-\frac{\tau(M)}{8}=2$$
with respect to the hyperkähler orientation. The Lichnerowicz formula therefore implies that a K3 surface does not admit a metric of positive scalar curvature [40]. Thus, after reversing the hyperkähler orientation, a nonflat Ricci-flat K3 metric cannot satisfy the conclusions of Theorems 1.2 and 1.4.

We show that, for certain K3 surfaces,
$$\sup _{\left\{W_{h}^{+} \neq 0\right\}} \rho=1$$
and that there is a point $p$ with $W_{h}^{+}(p) \neq 0$ and $\rho(p)=1$.
We want to look at holomorphic isometries of K3 surfaces: Lye showed that, if a hyperkähler manifold admits a holomorphic isometry of order at least 3 that fixes a subset of positive dimension, then the holomorphic sectional curvatures of $I, J$ and $K$ provide some information on the full Riemann tensor of the manifold [42].

In this setting, given a point $p \in M$, we define the holomorphic sectional curvatures $H_{I I}, H_{J J}, H_{K K}$ and the mixed-type curvatures $H_{I J}, H_{I K}, H_{J K}$ at $p$ as in (5.1): for instance, for every $v \in T_{p} M$ of unit norm,
$$H_{I I}(v)=h(R(v, I v) I v, v), \quad H_{I J}(v)=h(R(v, I v) J v, v)$$
and so on. It is not hard to show that $H_{I J}=H_{J I}, H_{I K}=H_{K I}$ and $H_{J K}=H_{K J}$; furthermore, since $h$ is Ricci-flat, we have
$$H_{I I}+H_{J J}+H_{K K}=0 .$$
Following [42, Theorem 4.6], if $(M, h)$ admits a holomorphic isometry of order at least 3 which fixes a subset $C$ of $M$ with positive dimension, then
$$H_{I J}(v)=H_{I K}(v)=H_{J K}(v)=0, \quad H_{J J}(v)=H_{K K}(v)=-\frac{1}{2} H_{I I}(v)$$
for every unit tangent vector $v \in T_{p} C, p \in C$ : in particular, this means that all six curvature quantities are uniquely determined by $H_{I I}$ along $C$. Assume that $\operatorname{dim} C=2$, i.e. $C$ is a surface inside ( $M, h$ ): since $C$ is fixed by an isometry of $h$, it is a (possibly non-connected) totally geodesic smooth submanifold with respect to the metric $\iota^{*}(h)$ induced by $h$ (see e.g. [29]) and, by [42, Corollary 4.8], for every $v \in T_{p} C$ of unit norm,
$$H_{I I}(w)=\left[\left(\alpha^{2}+\beta^{2}\right)^{2}+\left(\mu^{2}+\nu^{2}\right)^{2}-4\left(\alpha^{2}+\beta^{2}\right)\left(\mu^{2}+\nu^{2}\right)\right] \kappa(p),$$
where
$$w=\alpha v+\beta I v+\mu J v+\nu K v, \quad \alpha^{2}+\beta^{2}+\mu^{2}+\nu^{2}=1,$$
and $\kappa$ is the Gaussian curvature of $\left(C, \iota^{*} h\right)$. Now, let us choose a local orthonormal frame $\left\{e_{i}\right\}$ on an open chart of $(M, h)$ such that $e_{1}$ is tangent to $C$ and
$$\begin{aligned}
I\left(e_{1}\right) & =e_{2}, \quad I\left(e_{3}\right)=e_{4} \\
J\left(e_{1}\right) & =e_{3}, \quad J\left(e_{2}\right)=-e_{4} \\
K\left(e_{1}\right) & =e_{4}, \quad K\left(e_{2}\right)=e_{3}
\end{aligned}$$
Setting $R_{i j k l}=h\left(R\left(e_{i}, e_{j}\right) e_{l}, e_{k}\right)$, we can exploit (7.2) with $v=e_{1}$ and $(\alpha, \beta, \mu, \nu)=(1,0,0,0)$ to obtain, on $C$,
$$\begin{aligned}
& R_{1212}=H_{I I}\left(e_{1}\right)=\kappa \\
& R_{1313}=H_{J J}\left(e_{1}\right)=-\frac{1}{2} H_{I I}\left(e_{1}\right)=-\frac{1}{2} \kappa=R_{1414}
\end{aligned}$$
since $h$ is Ricci-flat and anti-self-dual, we have
$$\begin{aligned}
& R_{3434}=-R_{1234}=R_{1212}=\kappa \\
& R_{4242}=-R_{1342}=R_{1313}=R_{1414}=-R_{1423}=R_{2323}=-\frac{1}{2} \kappa .
\end{aligned}$$
Furthermore, by (7.1) and anti-self-duality, we obtain
$$H_{I J}\left(e_{1}\right)=H_{I K}\left(e_{1}\right)=H_{J K}\left(e_{1}\right)=0 \Longrightarrow R_{i j i k}=0$$
whenever $i, j, k$ are pairwise distinct. We now reverse the orientation on $M$ : since $h$ is Ricci-flat and self-dual in this orientation, its full curvature operator is $W_{h}^{+}$. A direct computation from the preceding curvature identities gives
$$W_{h}^{+}=\left(\begin{array}{ccc}
2 \kappa & 0 & 0 \\
0 & -\kappa & 0 \\
0 & 0 & -\kappa
\end{array}\right) .$$
If we assume that $M$ is compact, then $C$ is a compact surface with genus $g$ : if $g>1$, the Gauss-Bonnet Theorem implies that there exist points of $C$ where $\kappa<0$, which means that $\alpha_{h}=\beta_{h}$ at those points.

We observe that, in their classification of non-symplectic holomorphic automorphisms of order 3, Artebani and Sarti [2] proved the existence of K3 surfaces satisfying our hypotheses and such that the fixed point set of the automorphism is a surface of genus $g>1$, which proves our claim.

Furthermore, if we consider the hyperkähler orientation (i.e. the one for which $h$ is anti-self-dual), by (5.2), (7.3) and the previous discussion, we obtain that there exist points of $C$ at which $\Theta=2 / 3$.

Here we also provide an explicit example of an algebraic K3 surface where $\sup _{\left\{W_{h}^{+} \neq 0\right\}} \rho=1$. We consider a K3 surface $M$ as a branched double cover of $\mathbb{C P}^{2}$, defined in the weighted projective space $\mathbb{P}(1,1,1,3)$ : namely, using homogeneous coordinates $[x: y: z: w]$, we choose the K3 surface described by the equation
$$w^{2}=x^{6}+y^{6}+z^{6}$$
which is branched over the sextic curve $x^{6}+y^{6}+z^{6}=0$ in $\mathbb{C} \mathbb{P}^{2}$. The surface $M$ is a smooth complex submanifold of $\mathbb{P}(1,1,1,3)$. Indeed, the first-order partial derivatives of the defining polynomial do not have a common zero outside the origin of $\mathbb{C}^{4}$ and the unique singular point $[0: 0: 0: 1]$ of $\mathbb{P}(1,1,1,3)$ does not belong to $M$.

The weighted projective space $\mathbb{P}(1,1,1,3)$ admits an orbifold Kähler form (see e.g. [50]), whose restriction to $M$ is a smooth Kähler form $\widehat{\omega}$. We define
$$\phi([x: y: z: w])=\left[e^{2 \pi i / 3} x: y: z: w\right]:$$
it is clear that $\phi$ is a holomorphic automorphism of $M$ and that $\phi^{3}=\mathrm{Id}$. We set
$$\widehat{\omega}_{\mathrm{inv}}:=\frac{1}{3}\left(\widehat{\omega}+\phi^{*} \widehat{\omega}+\left(\phi^{2}\right)^{*} \widehat{\omega}\right) .$$
By construction, $\widehat{\omega}_{\text {inv }}$ is a $\phi$-invariant Kähler form on $M$ and, therefore, by Yau's theorem, its Kähler class contains a unique Ricci-flat Kähler form $\omega$ [57]. Since $\phi$ preserves the cohomology class $\left[\widehat{\omega}_{\text {inv }}\right]$ and $\omega \in\left[\widehat{\omega}_{\text {inv }}\right]$, the form $\phi^{*} \omega$ lies in the same class and is also Ricci-flat. Consequently, by uniqueness in Yau's Theorem, $\phi^{*} \omega=\omega$, so $\phi$ is an isometry of the Ricci-flat Kähler metric $h$ associated with $\omega$.

Now, we look for the fixed point set $\operatorname{Fix}(\phi)$ of $\phi$, i.e. for the points $[x: y: z: w]$ such that
$$\left(e^{\frac{2 \pi i}{3}} x, y, z, w\right)=\left(\lambda x, \lambda y, \lambda z, \lambda^{3} w\right),$$
for some $\lambda \in \mathbb{C} \backslash\{0\}$. If $\lambda=1$, a point $p=[x: y: z: w]$ lies in $\operatorname{Fix}(\phi)$ if and only if $x=0$, equivalently, if and only if $p \in C$, where $C$ is the complex curve defined by the equation $w^{2}=y^{6}+z^{6}$. On the other hand, if $\lambda \neq 1$, we immediately get that $\lambda=e^{\frac{2 \pi i}{3}}$ and that $y=z=0$ : using the equation which defines $M$, we obtain the isolated points
$$q_{1}=[1: 0: 0: 1], \quad q_{2}=[1: 0: 0:-1],$$
i.e. $\operatorname{Fix}(\phi)=C \cup\left\{q_{1}, q_{2}\right\}$.
Hence, the fixed point set of $\phi$ contains a submanifold of $(M, h)$ of dimension 2, which has to be totally geodesic. In order to compute the genus of $C$, we observe that $C$ can be seen as the double cover of the complex line $\{x=0\}$, which is a Riemann sphere $\mathbb{C P}^{1}$, branched over the six roots of the
polynomial $P(y, z)=y^{6}+z^{6}$ : by the classical Riemann-Hurwitz Theorem, we have
$$2 g_{C}-2=d\left(2 g_{\mathbb{C P}^{1}}-2\right)+B=-2 d+B,$$
where $d$ is the degree of the cover $C \longrightarrow \mathbb{C P}^{1}$ and $B$ is the total ramification. Since $d=2$ and $B=6$, we have $g_{C}=2$. Thus $C$ is a compact totally geodesic surface in $(M, h)$. Since $\chi(C)<0$, the Gauss-Bonnet theorem gives a point $p \in C$ with $\kappa(p)<0$. With respect to the hyperkähler orientation, the preceding calculation gives
$$\operatorname{spec}\left(W_{h}^{-}(p)\right)=\{2 \kappa(p),-\kappa(p),-\kappa(p)\} .$$
After reversing the orientation, this becomes the spectrum of $W_{h}^{+}(p)$; hence $\alpha_{h}(p)=\beta_{h}(p)>0$ and $\rho(p)=1$.

We also obtain examples showing that, without a uniform gap, one cannot conclude that $W_{h}^{+}$is either identically zero or nowhere zero. Certain K3 surfaces with Calabi-Yau metrics admit a holomorphic isometry of order at least 3 fixing an elliptic curve $C$ (see e.g. [2] and the Kummer surface studied in [42]). Since $C$ is totally geodesic and $\chi(C)=0$, the Gauss-Bonnet theorem implies that its Gaussian curvature vanishes somewhere. After reversing orientation, (7.3) therefore gives a point $p$ with $W_{h}^{+}(p)=0$. On the other hand, $W_{h}^{+} \not \equiv 0$, since a K3 surface admits no flat metric.
7.2. Noncompact case: the Gibbons-Hawking ansatz. In the late 1970s, Gibbons and Hawking developed an ansatz for constructing gravitational instantons [22,23]. Let $U \subset \mathbb{R}^{3}$ be an open set with $H^{2}(U ; \mathbb{R})=0$, endowed with the Euclidean metric $h_{\text {Eucl }}$, and let $V$ be a positive harmonic function on $U$. Since $*_{\mathbb{R}^{3}} d V$ is closed, there exists $\omega \in \Omega^{1}(U)$ such that
$$d \omega=*_{\mathbb{R}^{3}} d V .$$
Equivalently, $\omega$ satisfies the Bogomolny monopole equation
$$\nabla^{\text {Eucl }} \times \omega=\nabla^{\text {Eucl }} V .$$
On $M=U \times \mathbb{S}^{1}$, we can define a Riemannian metric $h$ which can be written as
$$h=V^{-1}(d \tau+\omega)^{2}+V h_{\mathrm{Eucl}},$$
where $\tau$ is a coordinate along $\mathbb{S}^{1}$. One has that $h$ is hyperkähler (see e.g. [39, Section 4.1]). Hence, with the orientation induced by the hyperkähler structure, $h$ is a Ricci-flat, anti-self-dual metric on $M$.

For simplicity, write $x^{1}:=x, x^{2}:=y$, and $x^{3}:=z$. We reverse the orientation on $M$ and choose the local orthonormal coframe given by
$$e^{0}:=V^{-1 / 2}(d \tau+\omega), \quad e^{i}=V^{1 / 2} d x^{i}, i=1,2,3 .$$
We recall that $\left\{d x^{i}\right\}$ is a local orthonormal coframe on $\mathbb{R}^{3}$, with respect to which the Hodge operator on $\mathbb{R}^{3}$ can be locally expressed as
$$*_{\mathbb{R}^{3}}(\eta)=\frac{1}{2} \eta_{k} \varepsilon_{i j k} d x^{i} \wedge d x^{j},$$
for every 1-form $\eta=\eta_{i} d x^{i}$, where $\varepsilon_{i j k}$ is the Levi-Civita symbol.
We can find the associated Levi-Civita connection forms $\left\{\omega_{j}^{i}\right\}$ by means of Cartan's first structure equations
$$d e^{\alpha}=-\omega_{\beta}^{\alpha} \wedge e^{\beta}:$$
by (7.4), a straightforward computation yields (see also [41, Lemma 2.2])
$$\begin{aligned}
\omega_{i}^{0} & =-\frac{1}{2} V^{-3 / 2}\left(\partial_{i} V e^{0}+\varepsilon_{i j k} \partial_{j} V e^{k}\right) \\
\omega_{j}^{i} & =\frac{1}{2} V^{-3 / 2}\left(\partial_{j} V e^{i}-\partial_{i} V e^{j}-\varepsilon_{i j k} \partial_{k} V e^{0}\right),
\end{aligned}$$
where $\partial_{i} V=\frac{\partial}{\partial x^{i}} V$. It is immediate to observe that
$$\omega_{j}^{i}=\varepsilon_{i j k} \omega_{k}^{0},$$
for every $i, j$. Now, we compute the curvature forms using Cartan's second structure equations
$$\frac{1}{2} R_{\beta \mu \nu}^{\alpha} e^{\mu} \wedge e^{\nu}=\Omega_{\beta}^{\alpha}=d \omega_{\beta}^{\alpha}+\omega_{\gamma}^{\alpha} \wedge \omega_{\beta}^{\gamma}:$$
by (7.6), (7.7) and the basic properties of the Levi-Civita symbol, it is immediate to show that
$$\Omega_{j}^{i}=\varepsilon_{i j k} \Omega_{k}^{0} .$$
Using the harmonicity of $V$ and the properties of $*_{\mathbb{R}^{3}}$, we obtain
$$\Omega_{i}^{0}=E_{i j}\left(e^{0} \wedge e^{j}+\frac{1}{2} \varepsilon_{j k l} e^{k} \wedge e^{l}\right),$$
where
$$E_{i j}:=\frac{1}{2}\left(V^{-2} \partial_{i} \partial_{j} V+V^{-3}|\nabla V|^{2} \delta_{i j}-3 V^{-3} \partial_{i} V \partial_{j} V\right) .$$
By our choice of orientation, $(M, h)$ is now self-dual and, since $h$ is Ricci-flat, the Riemann curvature operator coincides with $W_{h}^{+}$: choosing the standard orthogonal basis $\left\{\eta_{1}, \eta_{2}, \eta_{3}\right\}$ of $\Lambda^{+}$, where
$$\eta_{j}:=e^{0} \wedge e^{j}+\frac{1}{2} \varepsilon_{j k l} e^{k} \wedge e^{l},$$
we obtain
$$\Omega_{i}^{0}=E_{i j} \eta_{j}, \quad \Omega_{j}^{i}=\varepsilon_{i j k} E_{k l} \eta_{l} .$$
Hence, by the definition of the self-dual Weyl operator in $\Lambda_{h}^{+}$, we can immediately compute
$$W_{h}^{+}\left(\eta_{i}\right)=\Omega_{i}^{0}+\frac{1}{2} \varepsilon_{i j k} \Omega_{k}^{j}=\Omega_{i}^{0}+\frac{1}{2} \varepsilon_{i j k} \varepsilon_{j k l} \Omega_{l}^{0}=2 \Omega_{i}^{0}=2 E_{i j} \eta_{j},$$
i.e., viewing $W_{h}^{+}$as a matrix,
$$W_{h}^{+}=\frac{1}{V^{3}}\left[V \operatorname{Hess}_{\mathbb{R}^{3}}(V)+|\nabla V|^{2} h_{\mathrm{Eucl}}-3 d V \otimes d V\right] .$$

We now recall the multicentered Gibbons-Hawking construction. Fix distinct points $p_{1}, \ldots, p_{N} \in \mathbb{R}^{3}$ and set
$$U=\mathbb{R}^{3} \backslash\left\{p_{1}, \ldots, p_{N}\right\} .$$
We can find a smooth, positive harmonic function $V$ in $U$ defined as
$$V(x):=\varepsilon+\sum_{\alpha=1}^{N} \frac{m_{\alpha}}{\left|x-p_{\alpha}\right|},$$
where $\varepsilon \geq 0$ and $m_{\alpha}$ is the mass (or charge) at the point $p_{\alpha}$.
The product $U \times \mathbb{S}^{1}$ is replaced by a principal $U(1)$-bundle over $U$. Assume that all masses are equal to $m>0$ and normalize $\tau$ to have period $4 \pi m$. The Chern number over a small sphere surrounding each $p_{\alpha}$ is then $\pm 1$, so the restriction of the bundle is the Hopf fibration $\mathbb{S}^{3} \rightarrow \mathbb{S}^{2}$. After adding one point over each center, where the circle collapses, the Gibbons-Hawking metric extends to a smooth complete hyperkähler metric; see [24, Section 2.3], [41, Example 2.4], and [39, Section 4.1].

Since the bundle is generally nontrivial, the expression $d \tau+\omega$ in (7.5) must be globally replaced by a connection one-form $\Theta$ with curvature $\pi^{*}\left(*_{\mathbb{R}^{3}} d V\right)$. However, locally, one can choose $\tau$ and $\omega$ so that (7.5) and all the preceding computations remain valid. If $\varepsilon>0,(M, h)$ becomes an ALF manifold (such as the multi-Taub-NUT space), while if $\varepsilon=0$, we obtain an ALE manifold. In both cases $(M, h)$ is a gravitational instanton: as an example, if $\varepsilon=0$ and $N=2$, we can recover the Eguchi-Hanson metric on $T^{*} \mathbb{S}^{2}$ [18] (see e.g. [17, 41] for other examples). We highlight the fact that Anderson, Kronheimer and LeBrun generalized this construction to the case of countably many centers $p_{\alpha}$ [1].

From now on, we set $N=4$ and assume that $p_{1}, \ldots, p_{4}$ are vertices of a regular tetrahedron in $\mathbb{R}^{3}$ : namely, for a constant $R>0$, we define
$$\begin{array}{ll}
p_{1}:=\frac{R}{\sqrt{3}}(1,1,1), & p_{2}:=\frac{R}{\sqrt{3}}(1,-1,-1), \\
p_{3}:=\frac{R}{\sqrt{3}}(-1,1,-1), & p_{4}:=\frac{R}{\sqrt{3}}(-1,-1,1),
\end{array}$$
and we assume that $m_{\alpha}=1$ for every $\alpha$, for the sake of simplicity. One can easily observe that $\left|p_{\alpha}\right|=R$ for every $\alpha$ and that, by definition of the $p_{\alpha}$ 's, the following identities hold:
$$\sum_{\alpha=1}^{4} p_{\alpha}=0, \quad \sum_{\alpha=1}^{4} p_{\alpha} \otimes p_{\alpha}=\frac{4 R^{2}}{3} I .$$
First, we observe that there exists at least one point $p \in M$ such that $\left|W_{h}^{+}\right|(p)=0$ : indeed, we consider the barycenter $b=(0,0,0)$ of the tetrahedron and we can compute
$$\left.\nabla\left(\frac{1}{\left|p_{\alpha}-x\right|}\right)\right|_{x=0}=\frac{p_{\alpha}}{R^{3}},\left.\quad \operatorname{Hess}_{\mathbb{R}^{3}}\left(\frac{1}{\left|p_{\alpha}-x\right|}\right)\right|_{x=0}=\frac{3 p_{\alpha} \otimes p_{\alpha}-R^{2} I}{R^{5}} .$$

By (7.10) and (7.11), the previous identities imply
$$\nabla V(0)=\operatorname{Hess}_{\mathbb{R}^{3}} V(0)=0,$$
which immediately shows that $W_{h}^{+}=0$ for every point $p \in \pi^{-1}(b)$, by (7.9).
Now, let
$$r:=\{t \nu: t \in \mathbb{R}\}, \quad \nu:=\frac{1}{\sqrt{3}}(1,1,1)$$
be the line through the barycenter $b$ and $p_{1}$, and let $x=t \nu$ with $t<R$. Let $C_{3}=\left\{e, \phi, \phi^{2}\right\}$ be the cyclic group generated by $\phi$, the rotation of angle $2 \pi / 3$ around the axis $r$ : it is clear that $r$ is exactly the fixed locus of every isometry in $C_{3}$.

We choose a small, $C_{3}$-invariant open ball $B \subset U$ centered at $b$ such that $\pi^{-1}(B) \cong B \times \mathbb{S}^{1}$ and $p_{\alpha} \notin B$ for every $\alpha$. Since $V$ is $C_{3}$-invariant and the action preserves the Euclidean orientation, $*_{\mathbb{R}^{3}} d V$ is also $C_{3}$-invariant. It is important to observe that (7.4) does not admit a unique solution $\omega$ : by defining
$$\omega_{\mathrm{inv}}:=\frac{1}{3}\left(\omega+\phi^{*} \omega+\left(\phi^{2}\right)^{*} \omega\right),$$
we obtain $d \omega_{\text {inv }}=*_{\mathbb{R}^{3}} d V$ and that $\omega_{\text {inv }}$ is $C_{3}$-invariant. Renaming this new form $\omega$, we can extend $\phi$ to a local isometry $\widetilde{\phi}$ of the total space of the $U(1)$-bundle over $B$, i.e. we can define
$$\widetilde{\phi}(x, \tau)=(\phi(x), \tau),$$
which obviously generates a cyclic group of local isometries of the total space, which we call again $C_{3}$.

Now, we fix $p \in \pi^{-1}(r \cap B)$ : since $\widetilde{\phi}(p)=p$, its differential induces an isometry $\Phi$ of $T_{p}^{*} M$. Labeling the coordinates cyclically, its action is
$$\begin{array}{rlrlrl}
\Phi\left(e^{0}\right) & =e^{0}, & \Phi\left(e^{1}\right) & =e^{2}, & \Phi\left(e^{2}\right) & =e^{3}, \\
\Phi^{2}\left(e^{0}\right) & =e^{0}, & \Phi^{2}\left(e^{1}\right) & =e^{3}, & \Phi^{2}\left(e^{2}\right) & =e^{1}, \\
\Phi^{2}\left(e^{3}\right) & =e^{2}:
\end{array}$$
we point out that the form $e^{0}$ is fixed by all isometries since both $V$ and $\omega$ are $C_{3}$-invariant. Therefore, the natural action on $\Lambda_{p}^{+}$induced by $\Phi$ satisfies
$$\begin{aligned}
\Phi\left(\eta_{1}\right) & =\eta_{2}, & \Phi\left(\eta_{2}\right) & =\eta_{3}, & \Phi\left(\eta_{3}\right) & =\eta_{1}, \\
\Phi^{2}\left(\eta_{1}\right) & =\eta_{3}, & \Phi^{2}\left(\eta_{2}\right) & =\eta_{1}, & \Phi^{2}\left(\eta_{3}\right) & =\eta_{2}:
\end{aligned}$$
hence, $C_{3}^{\prime}=\left\{\mathrm{Id}, \Phi, \Phi^{2}\right\}$ acts by orientation-preserving isometries on $\left(\Lambda_{h}^{+}\right)_{p}$.
We can visualize $\Phi$ and $\Phi^{2}$ using their representative matrices with respect to the basis $\left\{\eta_{1}, \eta_{2}, \eta_{3}\right\}$ of $\left(\Lambda^{+}\right)_{p}$ as
$$\Phi \longleftrightarrow\left(\begin{array}{lll}
0 & 0 & 1 \\
1 & 0 & 0 \\
0 & 1 & 0
\end{array}\right), \quad \Phi^{2} \longleftrightarrow\left(\begin{array}{lll}
0 & 1 & 0 \\
0 & 0 & 1 \\
1 & 0 & 0
\end{array}\right) .$$
Now, since the elements of $C_{3}^{\prime}$ are isometries, the self-dual Weyl operator $W_{h}^{+}$commutes with all of them: since $W_{h}^{+}$is symmetric and trace-free, it is
easy to see that, for some $\lambda \in \mathbb{R}$,
$$W_{h}^{+}=\left(\begin{array}{ccc}
0 & \lambda & \lambda \\
\lambda & 0 & \lambda \\
\lambda & \lambda & 0
\end{array}\right)$$
at $p$. Its characteristic polynomial is
$$\operatorname{det}\left(W_{h}^{+}-s \operatorname{Id}\right)=-(s-2 \lambda)(s+\lambda)^{2} .$$
Thus, its eigenvalues are $2 \lambda,-\lambda,-\lambda$. In particular, at every point of $\pi^{-1}(r \cap$ $B)$ where $W_{h}^{+}$is nonzero, it has exactly two distinct eigenvalues. Our aim is to show that the ratio $\rho=\beta_{h} / \alpha_{h}$ does not admit a continuous extension on $\pi^{-1}(b)$. In order to do so, we exploit the conclusions drawn via the properties of the $C_{3}$-symmetry and consider the expansion of $V$ around $b$ : indeed, we will show that $W_{h}^{+}$does not admit other zeros on the fibers of points on the axis $t \nu$ close to $b$, and therefore, we prove that, for $t \rightarrow 0$, the limit of $\rho(t):=\rho(t \nu)$ does not exist. First, we can easily compute the following
$$\left.\nabla^{3}\left(\frac{1}{\left|p_{\alpha}-x\right|}\right)\right|_{x=0}=\frac{3\left(5 p_{\alpha} \otimes p_{\alpha} \otimes p_{\alpha}-3 R^{2} h_{\mathrm{Eucl}} \odot p_{\alpha}^{b}\right)}{R^{7}},$$
where $\nabla^{3}$ denotes the third covariant derivative with respect to $h_{\text {Eucl }}$ and $h_{\text {Eucl }} \odot p_{\alpha}^{b}$ denotes the symmetric part of $h_{\text {Eucl }} \otimes p_{\alpha}^{b}$; then, by definition of the $p_{\alpha}$ 's, we can compute, for every $x=\left(x_{1}, x_{2}, x_{3}\right) \in \mathbb{R}^{3}$,
$$\begin{aligned}
\sum_{\alpha=1}^{4}\left\langle p_{\alpha}, x\right\rangle^{3}= & \frac{R^{3}}{3 \sqrt{3}}\left[\left(x_{1}+x_{2}+x_{3}\right)^{3}+\left(x_{1}-x_{2}-x_{3}\right)^{3}\right. \\
& \left.+\left(-x_{1}+x_{2}-x_{3}\right)^{3}+\left(-x_{1}-x_{2}+x_{3}\right)^{3}\right]=\frac{8 R^{3}}{\sqrt{3}} x_{1} x_{2} x_{3} .
\end{aligned}$$
We consider the following expansion of $1 /\left|p_{\alpha}-x\right|$ centered at $b$ :
$$\begin{aligned}
\frac{1}{\left|p_{\alpha}-x\right|}= & \frac{1}{R}+\frac{\left\langle p_{\alpha}, x\right\rangle}{R^{3}}+\frac{3\left\langle p_{\alpha}, x\right\rangle^{2}-R^{2}|x|^{2}}{2 R^{5}} \\
& +\frac{5\left\langle p_{\alpha}, x\right\rangle^{3}-3 R^{2}|x|^{2}\left\langle p_{\alpha}, x\right\rangle}{2 R^{7}}+O\left(|x|^{4}\right) .
\end{aligned}$$
By (7.10), (7.11) and (7.15), since $V(0)=\varepsilon+4 / R$, we obtain the following
$$V(x)=\varepsilon+\frac{4}{R}+\frac{20}{\sqrt{3} R^{4}} x_{1} x_{2} x_{3}+O\left(|x|^{4}\right)$$
around $b$. By (7.9), it is clear that, for every $p \in \pi^{-1}\left(b^{\prime}\right)$, where $b^{\prime}$ is close to $b$,
$$W_{h}^{+}=\frac{20}{\sqrt{3} R^{4} V(0)^{2}}\left(\begin{array}{ccc}
0 & x_{3} & x_{2} \\
x_{3} & 0 & x_{1} \\
x_{2} & x_{1} & 0
\end{array}\right)+O\left(|x|^{2}\right) .$$
Indeed, the product of the first derivatives of $V$ is $O\left(|x|^{4}\right)$, so the leading term in (7.9) becomes $V^{-2} \operatorname{Hess}_{\mathbb{R}^{3}}(V)$.

Now, we restrict ourselves to $x=t \nu$ for some $t$, which means that
$$\lambda(t)=\frac{20}{3 R^{4} V(0)^{2}} t+O\left(t^{2}\right)$$
in (7.14). Putting $c=20 /\left(3 R^{4} V(0)^{2}\right)$, the eigenvalues of $W_{h}^{+}$are
$$2 c t+O\left(t^{2}\right), \quad-c t+O\left(t^{2}\right), \quad-c t+O\left(t^{2}\right):$$
by our previous discussion about the action of $C_{3}^{\prime}$, the two equal eigenvalues have exactly the same error term for every $t$. Consequently,
$$\rho(t)=\left\{\begin{array}{ll}
1, & t<0, \\
-\frac{1}{2}, & t>0,
\end{array} \text { for } 0<|t| \ll 1 .\right.$$
In particular,
$$\lim _{t \rightarrow 0^{+}} \rho(t)=-\frac{1}{2}, \quad \lim _{t \rightarrow 0^{-}} \rho(t)=1,$$
hence there is a degeneration phenomenon for $\rho$ on $\pi^{-1}(b)$ : this means that there exists no constant $\rho_{0}<1$ such that $\beta_{h} \leq \rho_{0} \alpha_{h}$ in $M$.

This shows that the conclusion of Theorem 1.9 can fail if the spectral hypothesis is omitted. The metric $h$ is a nonflat gravitational instanton with an ALE or ALF end and satisfies the volume-growth and curvaturedecay assumptions with $(\nu, q)=(4,4)$ in the ALE case and $(\nu, q)=(3,3)$ in the ALF case. Nevertheless, a Kähler metric of positive scalar curvature satisfies $\operatorname{det}\left(W_{g}^{+}\right)>0$ everywhere [16]. By conformal invariance, a Kähler representative of this type in $[h]$ would imply $\operatorname{det}\left(W_{h}^{+}\right)>0$, contradicting the vanishing of $W_{h}^{+}$in $\pi^{-1}(b)$.
Remark 7.1. The examples above show that the spectral hypotheses in Theorems 1.4 and 1.9 are sharp. We have not produced a compact example that exhibits the same loss of continuity of $\rho$ near a zero of $W_{h}^{+}$as in the Gibbons-Hawking example. Despite the lack of explicit formulas for Calabi-Yau metrics on K3 surfaces, they may provide such examples.

\section*{References}
\begin{itemize}
\item[] [1] M. T. Anderson, P. B. Kronheimer, C. LeBrun, Complete Ricci-flat Kähler manifolds of infinite topological type, Comm. Math. Phys. 125 (1989), no. 4, 637-642.
\item[] [2] M. Artebani, A. Sarti, Non-symplectic automorphisms of order 3 on K3 surfaces, Math. Ann. 342 (2008), no. 4, 903-921.
\item[] [3] S. Bando, A. Kasue, H. Nakajima, On a construction of coordinates at infinity on manifolds with fast curvature decay and maximal volume growth, Invent. Math. 97 (1989), no. 2, 313-349.
\item[] [4] C. Bär, Zero sets of solutions to semilinear elliptic systems of first order, Invent. Math. 138 (1999), no. 1, 183-202.
\item[] [5] M. Berger, Sur les variétés d'Einstein compactes, in Comptes Rendus de la IIIe Réunion du Groupement des Mathématiciens d'Expression Latine (Namur, 1965), pp. 35-55, Librairie Universitaire, Louvain.
\item[] [6] A. L. Besse, Einstein manifolds, reprint of the 1987 edition, Classics in Mathematics, Springer, Berlin, 2008.
\end{itemize}
[7] O. Biquard, P. Gauduchon, On toric Hermitian ALF gravitational instantons, Comm. Math. Phys. 399 (2023), no. 1, 389-422.
[8] O. Biquard, P. Gauduchon, and C. LeBrun, Gravitational instantons, Weyl curvature, and conformally Kähler geometry, Int. Math. Res. Not. IMRN 2024, no. 20, 13295-13311.
[9] S. Bochner, Curvature and Betti numbers. II, Ann. of Math. (2) 50 (1949), 77-93.
[10] J.-P. Bourguignon, Les variétés de dimension 4 à signature non nulle dont la courbure est harmonique sont d'Einstein, Invent. Math. 63 (1981), no. 2, 263-286.
[11] G. Catino, P. Mastrolia, A perspective on canonical Riemannian metrics, Progress in Mathematics, vol. 336, Birkhäuser/Springer, Cham, 2020.
[12] J. Cheeger, G. Tian, Curvature and injectivity radius estimates for Einstein 4-manifolds, J. Amer. Math. Soc. 19 (2006), no. 2, 487-525.
[13] G. Chen, X. Chen, Gravitational instantons with faster than quadratic curvature decay (I), Acta Math. 227 (2021), no. 2, 263-307.
[14] X. X. Chen, C. LeBrun, B. Weber, On conformally Kähler, Einstein manifolds, J. Amer. Math. Soc. 21 (2008), no. 4, 1137-1168.
[15] Y. Chen, E. Teo, A new AF gravitational instanton, Phys. Lett. B 703 (2011), no. 3, 359-362.
[16] A. Derdziński, Self-dual Kähler manifolds and Einstein manifolds of dimension four, Compositio Math. 49 (1983), no. 3, 405-433.
[17] M. Dunajski, Gravitational instantons, old and new, Acta Phys. Polon. B 55 (2024), no. 12, Paper No. A3, 18 pp.
[18] T. Eguchi, A. J. Hanson, Self-dual solutions to Euclidean gravity, Ann. Physics 120 (1979), no. 1, 82-106.
[19] L. C. Evans, R. F. Gariepy, Measure theory and fine properties of functions, revised ed., Textbooks in Mathematics, CRC Press, Boca Raton, FL, 2015.
[20] T. Friedrich, H. Kurke, Compact four-dimensional self-dual Einstein manifolds with positive scalar curvature, Math. Nachr. 106 (1982), 271-299.
[21] G. W. Gibbons, S. W. Hawking, Action integrals and partition functions in quantum gravity, Phys. Rev. D 15 (1977), 2752-2756.
[22] G. W. Gibbons, S. W. Hawking, Gravitational multi-instantons, Phys. Lett. B 78 (1978), no. 4, 430-432.
[23] G. W. Gibbons, S. W. Hawking, Classification of gravitational instanton symmetries, Comm. Math. Phys. 66 (1979), no. 3, 291-310.
[24] M. Gross, P. M. H. Wilson, Large complex structure limits of K3 surfaces, J. Differential Geom. 55 (2000), no. 3, 475-546.
[25] D. Guan, On bisectional nonpositively curved compact Kähler-Einstein surfaces, Pacific J. Math. 288 (2017), no. 2, 343-353.
[26] H. Guenancia, U. Hamenstädt, Kähler-Einstein metrics of negative curvature, preprint, arXiv:2503.02838v3, 2026.
[27] N. J. Hitchin, Compact four-dimensional Einstein manifolds, J. Differential Geom. 9 (1974), 435-441.
[28] N. J. Hitchin, Kählerian twistor spaces, Proc. London Math. Soc. (3) 43 (1981), no. 1, 133-150.
[29] S. Kobayashi, Fixed points of isometries, Nagoya Math. J. 13 (1958), 63-68.
[30] S. Kobayashi, K. Nomizu, Foundations of differential geometry. Vol. II, reprint of the 1969 original, Wiley Classics Library, Wiley-Interscience, Wiley, New York, 1996.
[31] P. B. Kronheimer, The construction of ALE spaces as hyper-Kähler quotients, J. Differential Geom. 29 (1989), no. 3, 665-683.
[32] P. B. Kronheimer, A Torelli-type theorem for gravitational instantons, J. Differential Geom. 29 (1989), no. 3, 685-697.
[33] C. LeBrun, On Einstein, Hermitian 4-manifolds, J. Differential Geom. 90 (2012), no. 2, 277-302.
[34] C. LeBrun, Einstein manifolds and extremal Kähler metrics, J. Reine Angew. Math. 678 (2013), 69-94.
[35] C. LeBrun, Einstein metrics, harmonic forms, and symplectic four-manifolds, Ann. Global Anal. Geom. 48 (2015), no. 1, 75-85.
[36] C. LeBrun, Einstein manifolds, self-dual Weyl curvature, and conformally Kähler geometry, Math. Res. Lett. 28 (2021), no. 1, 127-144.
[37] M. Li, On 4-dimensional Ricci-flat ALE manifolds, preprint, arXiv:2304.01609, 2023.
[38] M. Li, Classification results for conformally Kähler gravitational instantons, preprint, arXiv:2310.13197, 2023.
[39] M. Li, S. Sun, Geometry of gravitational instantons, to appear in Surveys in Differential Geometry, arXiv:2606.10443, 2026.
[40] A. Lichnerowicz, Spineurs harmoniques, C. R. Acad. Sci. Paris 257 (1963), 7-9.
[41] J. D. Lotay, G. Oliveira, Special Lagrangians, Lagrangian mean curvature flow and the Gibbons-Hawking ansatz, J. Differential Geom. 126 (2024), no. 3, 1121-1184.
[42] J. O. Lye, Geodesics on a K3 surface near the orbifold limit, Ann. Global Anal. Geom. 63 (2023), Paper No. 20.
[43] M. Matsumoto, S. Tanno, Kählerian spaces with parallel or vanishing Bochner curvature tensor, Tensor (N.S.) 27 (1973), 291-294.
[44] V. Minerbe, On the asymptotic geometry of gravitational instantons, Ann. Sci. Ècole Norm. Sup. (4) 43 (2010), no. 6, 883-924.
[45] Y. Odaka, C. Spotti, S. Sun, Compact moduli spaces of del Pezzo surfaces and Kähler-Einstein metrics, J. Differential Geom. 102 (2016), no. 1, 127-172.
[46] D. N. Page, Taub-NUT instanton with an horizon, Phys. Lett. B 78 (1978), no. 2, 249-251.
[47] D. N. Page, A compact rotating gravitational instanton, Phys. Lett. B 79 (1979), 235-238.
[48] R. Penrose, W. Rindler, Spinors and space-time. Vol. 2, Cambridge Monographs on Mathematical Physics, Cambridge University Press, Cambridge, 1986.
[49] A. Polombo, De nouvelles formules de Weitzenböck pour des endomorphismes harmoniques. Applications géométriques, Ann. Sci. Ècole Norm. Sup. (4) 25 (1992), no. 4, 393-428.
[50] J. Ross, R. P. Thomas, Weighted projective embeddings, stability of orbifolds, and constant scalar curvature Kähler metrics, J. Differential Geom. 88 (2011), no. 1, 109-159.
[51] Y.-T. Siu, P. Yang, Compact Kähler-Einstein surfaces of nonpositive bisectional curvature, Invent. Math. 64 (1981), no. 3, 471-487.
[52] S. Sun, R. Zhang, Collapsing geometry of hyperkähler four-manifolds and applications, Acta Math. 232 (2024), 325-424.
[53] S. Tachibana, On the Bochner curvature tensor, Natur. Sci. Rep. Ochanomizu Univ. 18 (1967), 15-19.
[54] G. Tian, On Calabi's conjecture for complex surfaces with positive first Chern class, Invent. Math. 101 (1990), no. 1, 101-172.
[55] F. Tricerri, L. Vanhecke, Curvature tensors on almost Hermitian manifolds, Trans. Amer. Math. Soc. 267 (1981), no. 2, 365-397.
[56] P. Wu, Einstein four-manifolds with self-dual Weyl curvature of nonnegative determinant, Int. Math. Res. Not. IMRN 2021, no. 2, 1043-1054.
[57] S.-T. Yau, On the Ricci curvature of a compact Kähler manifold and the complex Monge-Ampère equation. I, Comm. Pure Appl. Math. 31 (1978), no. 3, 339-411.

Dipartimento di Matematica, Politecnico di Milano, Italy
Email address: giovanni.catino@polimi.it
Dipartimento di Matematica "Giuseppe Peano", Università degli Studi di Torino, Italy
Email address: davide.dameno@unito.it