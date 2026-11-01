---
retention_scope: session
part: 6
total_parts: 7
---

[Part 6/7 of: PU(2) Monopoles, I: Regularity, Uhlenbeck Compactness ...]

Because the connection $\left.A\right|_{U}$ is reducible with respect to the splitting $\left.E\right|_{U}=L_{1} \oplus L_{2}$, we can write $\left.A\right|_{U}=A_{1} \oplus A_{2}$, where $A_{1}, A_{2}$ are unitary connections on $L_{1}, L_{2}$, so $\left.F_{A}\right|_{U}=F_{A_{1}} \oplus F_{A_{2}}$ and
$$\left(F_{A}^{+}\right)_{0}=\left(\begin{array}{cc}
\frac{1}{2}\left(F_{A_{1}}^{+}-F_{A_{2}}^{+}\right) & 0 \\
0 & -\frac{1}{2}\left(F_{A_{1}}^{+}-F_{A_{2}}^{+}\right)
\end{array}\right)=\varpi \otimes \sigma_{1},$$
where $\varpi=-\frac{i}{2}\left(F_{A_{1}}^{+}-F_{A_{2}}^{+}\right) \in \Omega^{+}(U, \mathbb{R})$ and $\sigma_{1} \in \mathfrak{s u}(2)$ is one of the Pauli matrices (2.14). Hence, $\left(F_{A}^{+}\right)_{0}$ is rank one on $U$ and the equation $\left(F_{A}^{+}\right)_{0}=\left(\mathrm{id}+\tau_{0}\right) \rho^{-1}\left(\Phi \otimes \Phi^{*}\right)_{00}$ implies that $\left(\Phi \otimes \Phi^{*}\right)_{00}$ is rank one on $U$; Lemma 2.21 then implies that $\Phi$ is also rank one on $U$ and so $\left.\Phi\right|_{U}=\phi \otimes \xi$, for some $\phi \in C^{r} \Omega^{0}\left(U, W^{+}\right)$and $\xi \in C^{r} \Omega^{0}(U, E)$, and
$$\left(\Phi \otimes \Phi^{*}\right)_{00}=-i\left(\phi \otimes \phi^{*}\right)_{0} \otimes i\left(\xi \otimes \xi^{*}\right)_{0} .$$
Writing $\xi=\xi_{1}+\xi_{2}$ for $\xi_{j} \in C^{r} \Omega^{0}\left(U, L_{j}\right)$, we see that
$$\left(\xi \otimes \xi^{*}\right)_{0}=\left(\begin{array}{cc}
\frac{1}{2}\left(\left|\xi_{1}\right|^{2}-\left|\xi_{2}\right|^{2}\right) & \xi_{1} \otimes \xi_{2}^{*} \\
\xi_{2} \otimes \xi_{1}^{*} & -\frac{1}{2}\left(\left|\xi_{1}\right|^{2}-\left|\xi_{2}\right|^{2}\right)
\end{array}\right) .$$

Since $\left(\mathrm{id}+\tau_{0}\right) \rho^{-1}\left(\Phi \otimes \Phi^{*}\right)_{00}=-\left(\mathrm{id}+\tau_{0}\right) \rho^{-1}\left(i\left(\phi \otimes \phi^{*}\right)_{0}\right) \otimes i\left(\xi \otimes \xi^{*}\right)_{0}$, we have
$$\begin{aligned}
& \left(\mathrm{id}+\tau_{0}\right) \rho^{-1}\left(\Phi \otimes \Phi^{*}\right)_{00} \\
& \quad=-\left(\mathrm{id}+\tau_{0}\right) \rho^{-1}\left(i\left(\phi \otimes \phi^{*}\right)_{0}\right) \otimes\left(\begin{array}{cc}
\frac{i}{2}\left(\left|\xi_{1}\right|^{2}-\left|\xi_{2}\right|^{2}\right) & i\left(\xi_{1} \otimes \xi_{2}^{*}\right) \\
i\left(\xi_{2} \otimes \xi_{1}^{*}\right) & -\frac{i}{2}\left(\left|\xi_{1}\right|^{2}-\left|\xi_{2}\right|^{2}\right)
\end{array}\right),
\end{aligned}$$
and by comparison with our matrix expression for $\left(F_{A}^{+}\right)_{0}$ we see that $\xi_{1} \otimes \xi_{2}^{*}=0$ on $U$ and thus at each point of $U$, either $\xi_{1}=0$ or $\xi_{2}=0$. Since $\nabla_{A} \xi=\nabla_{A_{1}} \xi_{1} \oplus \nabla_{A_{2}} \xi_{2}$, and the perturbations vanish on $U$, the equation $\left(D_{A}+\vec{\vartheta} \cdot \overrightarrow{\mathfrak{m}}(A)\right) \Phi=0$ reduces to $\left(D_{A_{1}}+\rho\left(\vartheta_{0}\right)\right)\left(\phi \otimes \xi_{1}\right)=0$ and $\left(D_{A_{2}}+\rho\left(\vartheta_{0}\right)\right)\left(\phi \otimes \xi_{2}\right)=0$. The unique continuation result for the perturbed Dirac operator, Lemma 5.12, implies that if $\phi \otimes \xi_{1}$ vanishes on an open subset of $U$, then $\phi \otimes \xi_{1} \equiv 0$ on $U$, and similarly for $\phi \otimes \xi_{2}$. If $\xi_{1}$ is non-zero at a point and thus non-zero on an open neighborhood, $\xi_{2}$ vanishes on this open set and by unique continuation $\xi_{2} \equiv 0$ on all of the connected set $U$. Symmetrically, if $\xi_{2}$ is non-zero at a point, then $\xi_{1} \equiv 0$ on $U$. Thus, $\Phi=\phi \otimes \xi_{1}$ or $\Phi=\phi \otimes \xi_{2}$.

The stabilizer of $\left.A\right|_{U}$ is $S_{L_{1}}^{1} \times S_{L_{2}}^{1}$. If $\xi_{1}=0$, then $\operatorname{Stab}_{\left.\Phi\right|_{U}}=\operatorname{Map}\left(U, S_{L_{1}}^{1}\right)$ while if $\xi_{2}=0$, then $\operatorname{Stab}_{\left.\Phi\right|_{U}}=\operatorname{Map}\left(U, S_{L_{2}}^{1}\right)$. \(\square\)

We see that elements of the stabilizer of a pair cannot exhibit holonomy, in the sense of the following lemma.

Lemma 5.23. Suppose $(A, \Phi)$ is a $\mathrm{PU}(2)$ monopole with $\Phi \not \equiv 0$ and that $U_{1}, U_{2}$ are connected open subsets of $X$. If there are gauge transformations $u_{i} \in{ }^{\circ} \mathcal{G}_{E \mid U_{i}}, i=1,2$, such that $u_{i} \in \operatorname{Stab}_{\left.A\right|_{U_{i}}}, u_{i} \in \operatorname{Stab}_{\left.(A, \Phi)\right|_{U_{1} \cap U_{2}}}, u_{i} \neq \mathrm{id}$, and there is a point $x \in U_{1} \cap U_{2}$ such that $u_{1}=u_{2}$ on $\left.E\right|_{x}$, then $u_{1}=u_{2}$ on $\left.E\right|_{U_{1} \cap U_{2}}$.

Proof. Let $V \subset U_{1} \cap U_{2}$ be the dense open subset of points $\{\Phi \neq 0\} \cap U_{1} \cap U_{2}$. Because there is a gauge transformation $u_{i} \in{ }^{\circ} \mathcal{G}_{E \mid U_{i}}$ with $u_{i} \Phi=\Phi$ over $U_{i}$, then $\left.\Phi\right|_{U_{1} \cap U_{2}}$ must be rank one by Lemma 5.21 and there is an orthogonal decomposition $\left.E\right|_{V}=\operatorname{Im} \Phi \oplus(\operatorname{Im} \Phi)^{\perp}$. Since $u_{i} \Phi=\Phi$ on $V$, both $u_{i}$ respect this decomposition and must be the identity on $\left.\operatorname{Im} \Phi\right|_{V}$. Thus, on $V$ we can write
$$u_{i}=\left(\begin{array}{cc}
1 & 0 \\
0 & e^{i \theta_{i}}
\end{array}\right)$$
with respect to this decomposition. Now $\operatorname{det} u_{i}=e^{i \theta_{i}}$ and because $u_{i} \in{ }^{\circ} \mathcal{G}_{E \mid U_{i}}$, the function $\operatorname{det} u_{i}$ is constant on $U_{i}$ and $e^{i \theta_{i}} \in S^{1}$. Thus, if $u_{1}=u_{2}$ on $\left.E\right|_{x}$, then $u_{1}=u_{2}$ on all points in $V$ which can be connected to $x$ by a path in $U_{1}$ and a path in $U_{2}$ (note that these need not be the same paths). Because $U_{1}$ and $U_{2}$ are connected, $u_{1}=u_{2}$ over all of $V$. Now $V$ is dense in $U_{1} \cap U_{2}$ and the $u_{i}$ are continuous so $u_{1}=u_{2}$ over all of $U_{1} \cap U_{2}$. \(\square\)

Theorem 5.11 now follows from Proposition 5.19:
Proof of Theorem 5.11 given Proposition 5.19. Let $(A, \Phi)$ be a $C^{r}$ solution to the PU(2) monopole equations (2.27) with $\Phi \not \equiv 0$ and $A$ reducible on a non-empty
open set $U \subset X$. Let $J(A)=\left\{j: \beta_{j}[A] \neq 0\right\}$ and let $\bar{B}_{J}(A)=\cup_{j \in J(A)} \bar{B}\left(x_{j}, R_{0}\right)$. Let $U^{\circ}$ be a connected component of $U-\bar{B}_{J}(A)$. Lemma 5.22 then implies that $\operatorname{Stab}_{\left.(A, \Phi)\right|_{U^{\circ}}} \simeq S^{1} \neq S_{Z}^{1}$ and so there is a $C^{r+1}$ gauge transformation $u$ of $\left.E\right|_{U^{\circ}}$ such that $u(A, \Phi)=(A, \Phi)$ on $U^{\circ}$. Proposition 5.19 allows the extension of $u$ to open subsets of $X \backslash \bar{B}_{J}(A)$ containing $U^{\circ}$. To be explicit, let $x \in U^{\circ}$ and $r_{0}=\operatorname{dist}_{g}\left(x, \partial U^{\circ}\right)$ and choose $r_{1}>r_{0}$ such that $r_{1} \leq \frac{1}{2} \varrho$ and $r_{1} \leq \min _{j \in J(A)} \operatorname{dist}_{g}\left(x, B\left(x_{j}, R_{0}\right)\right)$. By Proposition 5.19 there is an extension of $u \in \operatorname{Stab}_{\left.(A, \Phi)\right|_{B\left(x, r_{0}\right)}}$ to an element $\hat{u} \in \operatorname{Stab}_{\left.(A, \Phi)\right|_{B\left(x, r_{1}\right)}}$. By Lemma 5.23 we have $\hat{u}=u$ on $U^{\circ} \cap B\left(x_{0}, r_{1}\right)$ and not just $B\left(x_{0}, r_{0}\right)$. This gives an extension of the stabilizer $u$ for $(A, \Phi)$ over $U^{\circ}$ to a stabilizer $\hat{u}$ over the slightly larger open set $U^{\circ} \cup B\left(x, r_{1}\right)$. Since we do not assume that $X$ is simply connected, we must check that the extension obtained by repeating this process yields a single-valued gauge transformation over $X-\bar{B}_{J}(A)$.

The consistency of two extensions follows from Lemma 5.23. Let $u_{i}, i=1,2$, be two extensions of $u$ to connected open sets $U_{i}^{\circ}$ containing $U^{\circ}$, so we have $u_{i} \in \operatorname{Stab}_{\left.(A, \Phi)\right|_{U_{i}^{\circ}}}$ with $u_{i}=u$ on $\left.E\right|_{U^{\circ}}$. Because $u_{1}=u=u_{2}$ on $\left.E\right|_{U^{\circ}}$, Lemma 5.23 implies that $u_{1}=u_{2}$ on $\left.E\right|_{U_{1}^{\circ} \cap U_{2}^{\circ}}$. Therefore, the extensions of $u \in \operatorname{Stab}_{\left.(A, \Phi)\right|_{U^{\circ}}}$ fit together to form a global gauge transformation $\hat{u} \in \operatorname{Stab}_{A, \Phi}$ on $X-\bar{B}_{J}(A)$ such that $\hat{u}=u$ on $\left.E\right|_{U^{\circ}}$.

Thus, given that $A$ is reducible on an open set $U$ containing $\bar{B}_{J}(A)$, the above argument produces an element $u \in \operatorname{Stab}_{\left.(A, \Phi)\right|_{X-\bar{B}_{J}(A)}}$ with $u \notin S_{Z}^{1}$. Then Lemma 2.6 implies that $A$ is reducible on $X-\bar{B}_{J}(A)$. For $j=1, \ldots, N_{b}$, let $V_{j}$ be an open, connected subset of $U \cap B\left(x_{j}, 2 R_{0}\right)$ containing $\bar{B}\left(x_{j}, R_{0}\right)$, such that $V_{j} \cap\left(X-B_{J}(A)\right)$ is connected and set
$$X_{1}=X-\bar{B}_{J}(A) \quad \text { and } \quad X_{j}=\left(X-\bar{B}_{J}(A)\right) \cup \bigcup_{1 \leq k \leq j-1} V_{k}, \quad 2 \leq j \leq N_{b}+1 .$$
Each subset $X_{j}$ and $V_{j} \cap X_{j}$ is connected and $X_{1} \subset X_{2} \subset \cdots \subset X_{N_{b}+1}=X$. We extend $u \in \operatorname{Stab}_{\left.(A, \Phi)\right|_{X-\bar{B}_{J}(A)}}$ inductively over each $X_{j}$. Plainly, we have $u \in \operatorname{Stab}_{\left.A\right|_{V_{j} \cap X_{j}}}$ and $\operatorname{Stab}_{\left.A\right|_{V_{j}}} \subset \operatorname{Stab}_{\left.A\right|_{V_{j} \cap X_{j}}}$, so we first check that $\operatorname{Stab}_{\left.A\right|_{V_{j}}}=\operatorname{Stab}_{\left.A\right|_{V_{j} \cap X_{j}}}$. By hypothesis, $\left.A\right|_{U}$ is reducible and so for each subset $V_{j} \subset U$, we have that $\left.A\right|_{V_{j}}$ is reducible. Because $\left.\Phi\right|_{V_{j} \cap X_{j}} \not \equiv 0$ and thus $F_{A} \not \equiv 0$ on $V_{j} \cap X_{j}$ by (2.27) - so $\left.A\right|_{V_{j} \cap X_{j}}$ is not flat - then Lemma 2.6 implies that $\operatorname{Stab}_{\left.A\right|_{V_{j} \cap X_{j}}} \simeq T^{2}$. The same argument yields $\operatorname{Stab}_{\left.A\right|_{V_{j}}} \simeq T^{2}$. (We use the assumptions on the connectedness of $V_{j}$ and $V_{j} \cap X_{j}$ here: If the sets were not connected, the stabilizers would be $\oplus T^{2}$, a direct sum over connected components.) Thus $\operatorname{Stab}_{\left.A\right|_{V_{j}}}=\operatorname{Stab}_{\left.A\right|_{V_{j} \cap X_{j}}} \simeq T^{2}$.

Hence, there is an element $u^{\prime \prime} \in \operatorname{Stab}_{\left.A\right|_{V_{j}}}$ such that $u^{\prime \prime}=u^{\prime}$ on $V_{j} \cap X_{j}$, where $u^{\prime} \in \operatorname{Stab}_{\left.(A, \Phi)\right|_{X_{j}}}$ with $u^{\prime} \neq \mathrm{id}$. Together, $u^{\prime}$ and $u^{\prime \prime}$ give an element $u \in \operatorname{Stab}_{\left.A\right|_{X_{j+1}}}$ which is not in $S_{Z}^{1}$. The connection $A$ is then reducible on $X_{j+1}$, which implies that all the holonomy perturbations vanish on $X_{j+1}$. Lemma 5.22 then shows that the pair $(A, \Phi)$ is reducible on $X_{j+1}$ and we obtain a stabilizer $u \in \operatorname{Stab}_{\left.(A, \Phi)\right|_{X_{j+1}}}$, with
$u \neq \mathrm{id}$. The construction of $u \in \operatorname{Stab}_{A, \Phi}, u \neq \mathrm{id}$, is then completed by induction on $j$. \(\square\)

Remark 5.24. The analogue of Theorem 5.11 (namely, that local reducibility implies global reducibility) does not hold for anti-self-dual connections without further restrictions on the topology of $X$. For example, in [30] it is assumed that the fourmanifold $X$ is simply connected (see Lemma 4.3.21). As described by Kronheimer and Mrowka in [47] one can have locally reducible anti-self-dual connections (called 'twisted reducibles' in [47]); see their Lemma 2.4 for a sharp version of the Freed-Uhlenbeck generic metrics theorem (Corollaries 4.3.15, 4.3.18, and 4.3.19 in [20]) which holds when the requirement that $X$ be simply connected is dropped. In our case, we see from the proof of Theorem 5.11 that globally irreducible, locally reducible solutions $(A, \Phi)$ to (2.27) do not exist (at least when $\Phi \not \equiv 0$ ) because the stabilizer $u \in \operatorname{Stab}_{A, \Phi}$ must stabilize the section $\Phi$ and not just the connection $A$.

The proof of Proposition 5.19 takes up the remainder of this section.
5.3.1. The Agmon-Nirenberg unique continuation theorem. As in the case of the anti-self-dual equation [20, Lemma 4.3.21], our proof of the unique continuation property for PU(2) monopoles in radial gauge relies on the following special case of a more general result due to Agmon and Nirenberg for an ordinary differential equation on a Hilbert space [4]:

Theorem 5.25. [4, Theorem 2 (ii)] Let $\mathfrak{H}$ be a Hilbert space and let $\mathcal{P}: \operatorname{Dom}(\mathcal{P}(r)) \subset$ $\mathfrak{H} \rightarrow \mathfrak{H}$ be a family of symmetric linear operators for $r \in\left[r_{0}, R\right)$. Suppose that $\eta \in C^{1}\left(\left[r_{0}, R\right), \mathfrak{H}\right)$ with $\eta(r) \in \operatorname{Dom}(\mathcal{P}(r))$ and $\mathcal{P} \eta \in C^{0}\left(\left[r_{0}, R\right), \mathfrak{H}\right)$ such that
$$\left\|\frac{d \eta}{d r}-\mathcal{P}(r) \eta(r)\right\| \leq c_{1}\|\eta(r)\|,$$
for some positive constant $c_{1}$ and all $r \in\left[r_{0}, R\right)$. If the function $r \mapsto(\eta(r), \mathcal{P}(r) \eta(r))$ is differentiable for $r \in\left[r_{0}, R\right)$ and satisfies
$$\frac{d}{d r}(\eta, \mathcal{P} \eta)-2 \operatorname{Re}\left(\frac{d \eta}{d r}, \mathcal{P} \eta\right) \geq-c_{2}\|\mathcal{P} \eta\|\|\eta\|-c_{3}\|\eta\|^{2},$$
for positive constants $c_{2}, c_{3}$ and every $r \in\left[r_{0}, R\right)$, then the following holds: If $\eta\left(r_{0}\right)=0$ then $\eta(r)=0$ for all $r \in\left[r_{0}, R\right)$.

Applications of [4, Theorem 2] to the proof of unique continuation results for first-order elliptic and parabolic partial differential equations were considered by Agmon in [3, Chapter II]. In our application $\mathcal{P}(r)$ will be a family of first-order partial differential operators which are self-adjoint over the closed manifold $X$. Theorem 5.25 has also been applied by D. Salamon to prove the unique continuation property for harmonic spinors [77, Appendix E]. One of the difficulties in applying the Agmon-Nirenberg theorem to the PU(2) monopole equations (in Gaussian polar coordinates, $(r, \theta)$ )
is the requirement that the one-parameter family of operators be self-adjoint with respect to a fixed inner product on a fixed vector space. The additional complication, not present in [20, §4.3.4], is that the induced spin ${ }^{c}$ structures on geodesic spheres in $X$ vary with the induced family of $r$-dependent metrics.

Remark 5.26. [4, Remark, p. 209] If $\operatorname{Dom}(\mathcal{P}(r))=D$ is independent of $r$ and $\mathcal{P}(r)$, $r \in\left[r_{0}, R\right)$, is a differentiable family of self-adjoint operators, then the left-hand side of (5.11) simplifies, of course, to give the condition
$$\left(\eta, \frac{d \mathcal{P}}{d r} \eta\right) \geq-c_{2}\|\mathcal{P} \eta\|\|\eta\|-c_{3}\|\eta\|^{2},$$
since, noting that $\mathcal{P}$ is self-adjoint,
$$\begin{aligned}
\frac{d}{d r}(\eta, \mathcal{P} \eta)-2 \operatorname{Re}\left(\frac{d \eta}{d r}, \mathcal{P} \eta\right)= & \left(\frac{d \eta}{d r}, \mathcal{P} \eta\right)+\left(\eta, \frac{d \mathcal{P}}{d r} \eta\right)+\left(\eta, \mathcal{P} \frac{d \eta}{d r}\right) \\
& -\left(\frac{d \eta}{d r}, \mathcal{P} \eta\right)-\left(\mathcal{P} \eta, \frac{d \eta}{d r}\right) \\
= & \left(\eta, \frac{d \mathcal{P}}{d r} \eta\right) .
\end{aligned}$$
If $\mathcal{P}(r), r \in\left[r_{0}, R\right)$, is a differentiable family of self-adjoint operators then it is easy to see that (5.12) follows from the simpler condition
$$\left\|\frac{d \mathcal{P}}{d r} \eta\right\| \leq c_{2}\|\mathcal{P} \eta\|+c_{3}\|\eta\|,$$
provided $\mathcal{P} \eta \in C^{0}\left(\left[r_{0}, R\right), \mathfrak{H}\right)$.
5.3.2. The PU(2) monopole equations in Gaussian polar coordinates. Our first task is to write the pair PU(2) monopole equations (2.27) as an ordinary differential equation with respect to Gaussian polar coordinates $(r, \theta)$ centered at a point $x_{0} \in X$. For the analogous ordinary differential equation in the case of the anti-self-dual equation, see [20, 63, 88] and for the Seiberg-Witten equations see [47, 77].

Recall that $\varrho$ is the injectivity radius of $(X, g)$ at the point $x_{0}$, so $\exp _{x_{0}}: B(0, \varrho) \subset$ $(T X)_{x_{0}} \rightarrow B\left(x_{0}, \varrho\right) \subset X$ is a diffeomorphism. For each $\xi$ in the unit sphere $S^{3} \subset$ $(T X)_{x_{0}}$, let $\left\{e_{i}(\xi)\right\}_{i=1}^{3}$ be an oriented, orthonormal basis for $(\mathbb{R} \xi)^{\perp}=\left(T S^{3}\right)_{\xi} \subset$ $(T X)_{x_{0}}$; that is, let $\left\{e_{i}\right\}$ be an orthonormal frame for $T S^{3}$. Let $\gamma_{\xi}(r)$ be the geodesic $\exp _{x_{0}}(r \xi), r \in[0, \varrho)$, so that $\gamma_{\xi}(0)=x_{0}$ and $\left|\gamma_{\xi}^{\prime}(r)\right|=|\xi|$, and let $\tau_{\xi}(r):(T X)_{x_{0}} \rightarrow$ $(T X)_{\gamma_{\xi}(r)}$ denote parallel translation with respect to the metric's Levi-Civita connection along $\gamma_{\xi}(r)$. Let $e_{i}(r, \xi):=\tau_{\xi}(r) e_{i}(\xi)$ for $r \geq 0$, so that $\left\{\gamma_{\xi}^{\prime}(r), e_{i}(r, \xi)\right\}$ is an orthonormal frame for $(T X)_{\gamma_{\xi}(r)}$ which is parallel along the radial geodesics $\gamma_{\xi}(r)$ and satisfies $\gamma_{\xi}^{\prime}(0)=\xi$ and $e_{i}(0, \xi)=e_{i}(\xi)$. Denote the radial vector $\gamma_{\xi}^{\prime}(r) \in(T X)_{\gamma_{\xi}(r)}$ by $\frac{\partial}{\partial r}:=\left.\frac{\partial}{\partial r}\right|_{\gamma_{\xi}(r)}$ when no confusion can arise. Thus, $\left\{\frac{\partial}{\partial r}, e_{i}\right\}$ is an oriented, orthonormal frame for $T X$ over $B\left(x_{0}, \varrho\right) \backslash\{0\}$, which is parallel along radial geodesics; let $\left\{d r, e^{i}\right\}$ be the corresponding dual frame for $T^{*} X$ over $B\left(x_{0}, \varrho\right) \backslash\{0\}$.

With respect to the parametrization $S^{3} \times(0, \varrho) \simeq B\left(x_{0}, \varrho\right)-\left\{x_{0}\right\}$, given by $(r, \xi) \mapsto$ $\exp _{x_{0}}(r \xi)$, the metric $g$ on $B\left(x_{0}, \varrho\right)-\left\{x_{0}\right\}$ pulls back to
$$g=(d r)^{2}+g_{r}$$
where $g_{r}$ is the metric on $S^{3}$ pulled back from the restriction $\left.g\right|_{S^{3}\left(x_{0}, r\right)}$ to the geodesic sphere $S^{3}\left(x_{0}, r\right):=\left\{x \in X: \operatorname{dist}_{g}\left(x, x_{0}\right)=r\right\}$. Let $*_{g_{r}}$ denote the Hodge star operator for the metric $g_{r}$ on $S^{3}$ and, for emphasis, we write $*_{g}$ for the Hodge star operator for the metric $g$ on $X$.

Suppose that a pair $(A, \Phi)$ on $\left(\mathfrak{s u}(E), W^{+} \otimes E\right)$ is a $C^{r}$ solution to the $\operatorname{PU}(2)$ monopole equations (2.27) over $X$,
$$\begin{aligned}
\rho\left(F_{A}^{+}\right) & =\rho \tau \rho^{-1}\left(\Phi \otimes \Phi^{*}\right)_{00} \\
D_{A, \vartheta_{0}} \Phi & =0
\end{aligned}$$
where $\tau:=\mathrm{id}_{\Lambda^{+}}+\tau_{0}$ is an automorphism of $\Lambda^{+}$and $D_{A, \vartheta_{0}} \Phi:=D_{A} \Phi+\rho\left(\vartheta_{0}\right) \Phi$. We have not included the holonomy perturbations $\vec{\tau} \cdot \overrightarrow{\mathfrak{m}}(A)$ and $\vec{\vartheta} \cdot \overrightarrow{\mathfrak{m}}(A)$ because they vanish near $x_{0}$ by hypothesis.

We obtain an isomorphism $\left.E\right|_{B\left(x_{0}, \varrho\right)} \simeq E_{0} \times B\left(x_{0}, \varrho\right)$ of complex two-plane bundles by choosing a unitary frame for $E_{0}:=\left.E\right|_{x_{0}}$ and using parallel translation via the U(2) connection on $E$ defined by $A$ and $A_{\text {det } E}$ along radial geodesics emanating from $x_{0}$. Let $A=B+C d r$ denote the induced SO(3) connection on the bundle $\mathfrak{s} \mathfrak{u}\left(E_{0}\right) \times S^{3} \times(0, \varrho)$ over $S^{3} \times(0, \varrho)$ and note that $A$ is in radial gauge with respect to the point $x_{0}$, so $C:=A\left(\frac{\partial}{\partial r}\right)=0$. We let $B=B(r), r \in(0, \varrho)$, denote the resulting one-parameter family of SO(3) connections on the bundle $\mathfrak{s u}\left(E_{0}\right) \times S^{3}$ over $S^{3}$. In exactly the same way, we obtain an induced one-parameter family of U(2) connections on the bundle $W_{0}^{+} \times S^{3}$ over $S^{3}, r \in(0, \varrho)$, induced by the isomorphism $\left.W^{+}\right|_{B\left(x_{0}, \varrho\right)-\left\{x_{0}\right\}} \simeq W_{0}^{+} \times S^{3} \times(0, \varrho)$.

A section $\Phi$ of the bundle $W^{+} \otimes E$ over $B\left(x_{0}, \varrho\right)$ pulls back, via the isomorphism $\left.\left(W^{+} \otimes E\right)\right|_{B\left(x_{0}, \varrho\right)-\left\{x_{0}\right\}} \simeq\left(W_{0}^{+} \otimes E_{0}\right) \times S^{3} \times(0, \varrho)$, to a one-parameter family of sections $\Psi(r)$ of the bundle $W_{0}^{+} \otimes E_{0} \times S^{3}$ over $S^{3}$. The automorphism $\tau$ of $\Lambda^{+, g}$ pulls back to a one-parameter family of automorphisms $\sigma(r)$ of $T^{*} S^{3}$, for $r \in(0, \varrho)$, using the isomorphism
$$(0, \varrho) \times T^{*} S^{3} \rightarrow \Lambda^{+, g}\left(T^{*} X\right), \quad(r, \alpha) \mapsto *_{g_{r}} \alpha+d r \wedge \alpha .$$
The $g$-compatible Clifford map $\rho: T^{*} X \rightarrow \operatorname{Hom}\left(W^{+}, W^{-}\right)$and the isomorphism $\left.W^{+}\right|_{B\left(x_{0}, \varrho\right)-\left\{x_{0}\right\}} \simeq W_{0}^{+} \times S^{3} \times(0, \varrho)$ define a family of $g_{r}$-compatible Clifford maps $\gamma(r): T^{*} S^{3} \rightarrow \operatorname{End}\left(W_{0}^{+}\right)$by setting
$$\gamma(r):=\rho(d r) \rho(\cdot) .$$
Indeed, to see this, observe that $g(d r, d r)=1$ and so for a family of one-forms $\alpha(r)$ on $S^{3}$, defined by the isomorphism $B\left(x_{0}, \varrho\right)-\left\{x_{0}\right\} \simeq S^{3} \times(0, \varrho)$ and a one-form $\alpha$ on
$B\left(x_{0}, \varrho\right)$, we have
$$\begin{aligned}
\gamma_{r}(\alpha)^{\dagger} \gamma_{r}(\alpha) & =\rho(\alpha)^{\dagger} \rho(d r)^{\dagger} \rho(d r) \rho(\alpha)=\rho(\alpha)^{\dagger} \rho(\alpha) \\
& =g_{r}(\alpha, \alpha) \operatorname{id}_{W_{0}^{+}},
\end{aligned}$$
as required. The map $\gamma$ extends to a one-parameter family of Clifford maps $\gamma(r)$ : $\Lambda^{\bullet}\left(T^{*} S^{3}\right) \otimes \mathbb{C} \rightarrow \operatorname{End}\left(W_{0}^{+}\right)$in the usual way. For example, $\gamma_{r}(\alpha \wedge \beta):=\gamma_{r}(\alpha) \gamma_{r}(\beta)$, for $\alpha, \beta \in \Omega^{1}\left(S^{3}\right)$, in which case we see that $\gamma_{r}(\alpha \wedge \beta)=\rho(\alpha) \rho(\beta)$.

With the above understood, we can proceed to rewrite the PU(2) monopole equations (2.27) over the ball $B\left(x_{0}, \varrho\right)$ as an ordinary differential equation for a oneparameter family of pairs $(B(r), \Psi(r))$ on $\left(\mathfrak{s u}\left(E_{0}\right), W_{0}^{+} \otimes E_{0}\right)$ over $S^{3}$. The curvature $F_{A}$ of the connection $A$ over $B\left(x_{0}, \varrho\right)$ is given by
$$F_{A}=F_{B}-\frac{d B}{d r} \wedge d r .$$
For any $\omega \in \Omega^{2}(X, \mathbb{R})$, we have $\rho_{+}(\omega)=\rho_{+}\left(*_{g} \omega\right)$, since $\left.\rho_{+}\right|_{\Lambda^{-}}=0$. If the radial component of $\omega$ vanishes and we consider $\left.\omega\right|_{B\left(x_{0}, \varrho\right)}$ as a one-parameter family of twoforms $\omega(r)$ on $S^{3}$, we see that $*_{g} \omega=-\left(*_{g_{r}} \omega\right) \wedge d r$. Combining these observations yields
$$\begin{aligned}
\rho\left(F_{A}^{+}\right) & =\rho_{+}\left(F_{A}\right)=\rho_{+}\left(F_{B}-\frac{d B}{d r} \wedge d r\right) \\
& =\rho_{+}\left(-\left(*_{g_{r}} F_{B}\right) \wedge d r-\frac{d B}{d r} \wedge d r\right) \\
& =\rho_{-}(d r) \rho_{+}\left(*_{g_{r}} F_{B}+\frac{d B}{d r}\right),
\end{aligned}$$
and therefore,
$$\rho\left(F_{A}^{+}\right)=\gamma\left(*_{g_{r}} F_{B}+\frac{d B}{d r}\right) .$$
The section $\rho \tau \rho^{-1}\left(\Phi \otimes \Phi^{*}\right)_{00}$ of $\mathfrak{s} \mathfrak{u}\left(W^{+}\right) \otimes \mathfrak{s} \mathfrak{u}(E)$ over $B\left(x_{0}, \varrho\right)$ pulls back to the oneparameter family of sections $\gamma \sigma \gamma^{-1}\left(\Psi \otimes \Psi^{*}\right)_{00}$ of $\mathfrak{s} \mathfrak{u}\left(W_{0}^{+}\right) \otimes \mathfrak{s} \mathfrak{u}\left(E_{0}\right) \times S^{3}$ over $S^{3}$ via the isomorphism $\left.W^{+}\right|_{B\left(x_{0}, \varrho\right)-\left\{x_{0}\right\}} \simeq W_{0}^{+} \times S^{3} \times(0, \varrho)$ and similarly for $E$.

Let $\theta(r)$ be the induced one-parameter family of complex one-forms on $S^{3}$ defined by $\vartheta_{0}$ on $B\left(x_{0}, \varrho\right)$ and the isomorphism $B\left(x_{0}, \varrho\right)-\left\{x_{0}\right\} \simeq S^{3} \times(0, \varrho)$, so $\vartheta_{0}=-f d r+\theta$ on $S^{3} \times(0, \vartheta)$, where $f(r) \in \Omega^{0}\left(S^{3}, \mathbb{C}\right)$. Given the preceding identifications, the Dirac
operator term in (2.27) can then be written over $S^{3} \times\{r\}$ as
$$\begin{aligned}
D_{A, \vartheta_{0}} \Phi & =\rho(d r) \nabla_{\frac{\partial}{\partial r}}^{A} \Psi+\sum_{i=1}^{3} \rho\left(e^{i}\right) \nabla_{e_{i}}^{A} \Psi+\rho\left(\vartheta_{0}\right) \Psi \\
& =\rho(d r) \frac{d \Psi}{d r}+\sum_{i=1}^{3} \rho\left(e^{i}\right) \nabla_{e_{i}}^{B} \Psi+\rho(\theta) \Psi-f \rho(d r) \Psi \\
& =\rho(d r)\left(\frac{d \Psi}{d r}-\sum_{i=1}^{3} \rho(d r) \rho\left(e^{i}\right) \nabla_{e_{i}}^{B} \Psi-\rho(d r) \rho(\theta) \Psi-f \Psi\right) \\
& =\rho(d r)\left(\frac{d \Psi}{d r}-\sum_{i=1}^{3} \gamma\left(e^{i}\right) \nabla_{e_{i}}^{B} \Psi-\gamma(\theta) \Psi-f \Psi\right),
\end{aligned}$$
and therefore,
$$D_{A, \vartheta_{0}} \Phi=\rho(d r)\left(\frac{d \Psi}{d r}-D_{B, \theta, f} \Psi\right) .$$
Hence, the PU(2) monopole equations (2.27) can be written as
$$\begin{aligned}
\gamma\left(\frac{d B}{d r}+*_{g_{r}} F_{B}\right) & =\gamma \sigma \gamma^{-1}\left(\Psi \otimes \Psi^{*}\right)_{00}, \\
\rho(d r) \frac{d \Psi}{d r} & =\rho(d r) D_{B, \theta, f} \Psi .
\end{aligned}$$
We use $D_{B}: \Omega^{0}\left(S^{3}, W_{0}^{+} \otimes E_{0}\right) \rightarrow \Omega^{0}\left(S^{3}, W_{0}^{+} \otimes E_{0}\right)$ to denote the one-parameter family of Dirac operators defined by the family of $g(r)$-compatible Clifford maps $\gamma(r): T^{*} S^{3} \rightarrow \operatorname{End} W_{0}^{+}$, the family of U(2) connections on $W_{0}^{+} \times S^{3}$, the family of SO(3) connections $B(r)$ on $\mathfrak{s} \mathfrak{u}\left(E_{0}\right) \times S^{3}$ over $S^{3}$, and the family of determinant connections on $\operatorname{det} E_{0} \times S^{3}$ over $S^{3}$. Since the Clifford map gives an isomorphism $\gamma: T^{*} S^{3} \simeq \mathfrak{s u}\left(W_{0}^{+}\right) \times S^{3}$, the PU(2) monopole equations then take the shape
$$\begin{aligned}
\frac{d B}{d r}+*_{g_{r}} F_{B} & =\sigma \gamma^{-1}(\Psi \otimes \Psi)_{00}, \\
\frac{d \Psi}{d r} & =D_{B, \theta, f} \Psi,
\end{aligned}$$
for a one-parameter family $(B(r), \Psi(r)), r \in(0, \varrho)$, on $\left(E_{0}, W_{0}^{+} \otimes E_{0}\right)$ over $S^{3}$.
5.3.3. The ordinary differential equation for the difference pair. Let $(A, \Phi)$ be a $C^{r}$ solution to the PU(2) monopole equations (2.27) over $X$. Suppose, as in the hypothesis of Proposition 5.19, that there is a $C^{r+1}$ gauge transformation $u$ of $\left.E\right|_{B\left(x_{0}, r_{0}\right)}$ such that $u(A, \Phi)=(A, \Phi)$ on $B\left(x_{0}, r_{0}\right)$. Let $(A, \Phi)$ again denote the induced pair defined by the isomorphism $\left.E\right|_{B\left(x_{0}, \varrho\right)} \simeq E_{0} \times S^{3} \times(0, \varrho)$ (given by a choice of unitary frame for $E_{0}=E_{x_{0}}$ and parallel, radial translation via $A$ ) and let $u$ be the induced gauge transformation on $E_{0} \times S^{3} \times\left(0, r_{0}\right)$. Then $u(A)=u A u^{-1}-\left(d_{A} u\right) u^{-1}$ and
$A=B+C d r$, where $C=A\left(\frac{\partial}{\partial r}\right)=0$, and so $d u / d r=0$. We now extend $u$ by parallel translation via $A$ along radial geodesics emanating from $x_{0}$ to a gauge transformation $\hat{u}$ on $E_{0} \times S^{3} \times(0, \varrho)$.

Let $(\hat{A}, \hat{\Phi})=\hat{u}(A, \Phi)$ be the gauge-equivalent pair on $S^{3} \times(0, \varrho)$, so $(\hat{A}, \hat{\Phi})$ is a $C^{r}$ solution to (2.27) over $S^{3} \times(0, \varrho)$ with $\hat{A}=\hat{u}(A)$ in radial gauge. In particular, $(\hat{A}, \hat{\Phi})=(A, \Phi)$ over $S^{3} \times\left(0, r_{0}\right)$ : we need to show that $(\hat{A}, \hat{\Phi})=(A, \Phi)$ over $S^{3} \times\left(0, r_{1}\right)$ in order to prove Proposition 5.19.

The one-parameter family of pairs $(\hat{B}(r), \hat{\Psi}(r))$ on $\left(\mathfrak{s u}\left(E_{0}\right), W_{0}^{+} \otimes E_{0}\right)$ over $S^{3}$ also satisfies the ordinary differential equation in (5.14) so, subtracting these two pairs of ordinary differential equations, we obtain for $r \geq r_{0}$,
$$\begin{aligned}
\frac{d(\hat{B}-B)}{d r}+*_{g_{r}}\left(F_{\hat{B}}-F_{B}\right) & =\sigma \gamma^{-1}\left(\hat{\Psi} \otimes \hat{\Psi}^{*}-\Psi \otimes \Psi^{*}\right)_{00}, \\
\frac{d(\hat{\Psi}-\Psi)}{d r} & =D_{B, \theta, f} \Psi-D_{\hat{B}, \theta, f} \hat{\Psi} .
\end{aligned}$$
Since $F_{B}=d(B-\Gamma)+(B-\Gamma) \wedge(B-\Gamma)$ and $D_{B, \theta, f}=D+\gamma(B-\Gamma)+\gamma(\theta)+f \mathrm{id}_{W_{0}^{+} \otimes E_{0}}$, we obtain an ordinary differential equation for the difference pair
$$(b, \psi):=(\hat{B}-B, \hat{\Psi}-\Psi) \in \Omega^{1}\left(S^{3}, \mathfrak{s} \mathfrak{u}\left(E_{0}\right)\right) \oplus \Omega^{0}\left(S^{3}, W_{0}^{+} \otimes E_{0}\right),$$
so that,
$$\begin{aligned}
& \frac{d b}{d r}=-*_{g_{r}} d b+*_{g_{r}}(\hat{B} \wedge b+b \wedge B)+\sigma \gamma^{-1}\left(\hat{\Psi} \otimes \psi^{*}+\psi \otimes \Psi^{*}\right)_{00}, \\
& \frac{d \psi}{d r}=D \psi+\gamma(\hat{B}-\Gamma) \psi+\gamma(b) \Psi+\gamma(\theta) \psi+f \psi,
\end{aligned}$$
where $r \in\left(r_{0}, \varrho\right)$ and $\Gamma$ is the product connection on $\mathfrak{s} \mathfrak{u}\left(E_{0}\right) \times S^{3}$ over $S^{3}$ defined by our trivialization. The above system has the schematic form
$$\frac{d(b, \psi)}{d r}=\left(\begin{array}{cc}
-*_{g_{r}} d & 0 \\
0 & D
\end{array}\right)(b, \psi)+\mathcal{Z}_{r}(b, \psi),$$
where $\mathcal{Z}_{r}$ is a one-parameter family of zeroth-order operators with coefficients depending on $g_{r}, B, \sigma$, and $\Psi$.
5.3.4. Reduction to the Agmon-Nirenberg theorem. We first observe that the operator - $*_{g_{r}} d$ on $\Omega^{1}\left(S^{3}, \mathfrak{s u}\left(E_{0}\right)\right)$ is self-adjoint with respect to the $L^{2}$ inner product induced by the metric $g_{r}$ on $S^{3}$. Indeed, as $*_{g_{r}}^{2}=1$ on $\Omega^{1}\left(S^{3}\right)$ and $d \operatorname{tr}\left(b \wedge b^{\prime}\right)=\operatorname{tr}\left(d b \wedge b^{\prime}\right)-$
$\operatorname{tr}\left(b \wedge d b^{\prime}\right)$, we have
$$\begin{aligned}
\int_{S^{3}}\left\langle b,-*_{g_{r}} d b^{\prime}\right\rangle_{r} d \operatorname{vol}_{r} & =-\int_{S^{3}} \operatorname{tr}\left(b \wedge *_{g_{r}}\left(-*_{g_{r}} d b^{\prime}\right)\right) \\
& =\int_{S^{3}} \operatorname{tr}\left(b \wedge d b^{\prime}\right)=\int_{S^{3}} \operatorname{tr}\left(d b \wedge b^{\prime}\right) \\
& =\int_{S^{3}} \operatorname{tr}\left(b \wedge d b^{\prime}\right)=\int_{S^{3}} \operatorname{tr}\left(b^{\prime} \wedge *_{g_{r}}^{2} d b\right) \\
& =-\int_{S^{3}}\left\langle b^{\prime}, *_{g_{r}} d b\right\rangle_{r} d \operatorname{vol}_{r},
\end{aligned}$$
and therefore,
$$\int_{S^{3}}\left\langle b,-*_{g_{r}} d b^{\prime}\right\rangle_{r} d \operatorname{vol}_{r}=\int_{S^{3}}\left\langle-*_{g_{r}} d b, b^{\prime}\right\rangle_{r} d \operatorname{vol}_{r}$$
The Dirac operators $D: \Omega^{1}\left(S^{3}, W_{0}^{+} \otimes E_{0}\right) \rightarrow \Omega^{1}\left(S^{3}, W_{0}^{-} \otimes E_{0}\right)$ are defined by the one-parameter family of $g_{r}$-compatible Clifford maps $\gamma_{r}: T^{*} S^{3} \rightarrow \operatorname{End}\left(W_{0}^{+}\right)$, the oneparameter family of U(2) connections on $W_{0}^{+} \times S^{3}$, one-parameter family of determinant connections on $\operatorname{det} E_{0} \times S^{3}$, and the product SO(3) connection on $\mathfrak{s} \mathfrak{u}\left(E_{0}\right) \times S^{3}$. Then, by [57, Proposition II.5.3] we have
$$\left\langle D \psi, \psi^{\prime}\right\rangle=\left\langle\psi, D \psi^{\prime}\right\rangle+\operatorname{div}_{g_{r}} \xi,$$
where $\xi(r)$ is the one-parameter family of vector fields on $S^{3}$ defined by $\alpha(\xi)=$ $-\left\langle\psi, \gamma(\alpha) \psi^{\prime}\right\rangle$, for all $\alpha \in \Omega^{1}\left(S^{3}\right)$. Hence, the Divergence theorem for the metric $g_{r}$ implies that $D$ is self-adjoint with respect the the family of $L^{2}$ inner products on $\Omega^{1}\left(S^{3}, W_{0}^{+} \otimes E_{0}\right)$ defined by $g_{r}$ :
$$\int_{S^{3}}\left\langle D \psi, \psi^{\prime}\right\rangle d \operatorname{vol}_{r}=\int_{S^{3}}\left\langle\psi, D \psi^{\prime}\right\rangle d \operatorname{vol}_{r}$$
The Agmon-Nirenberg theorem is not immediately applicable to the ordinary differential equation in (5.16) since the differential operator $\mathcal{P}_{r}:=-*_{g_{r}} d \oplus D$ is only self-adjoint on the Hilbert space $\mathfrak{H}_{r}:=L^{2}\left(S^{3}, \Lambda^{1} \otimes \mathfrak{s} \mathfrak{u}\left(E_{0}\right)\right) \oplus L^{2}\left(S^{3}, W_{0}^{+} \otimes E_{0}\right)$ with $L^{2}$ inner products $(\cdot, \cdot)_{r}$ defined by the family of metrics $g_{r}$ on $S^{3}$, rather than a fixed inner product.

If $d \mathrm{vol}_{r}$ is the volume form on $S^{3}$ defined by the metric $g_{r}$ then we may write
$$d \mathrm{vol}_{r}=h_{r}^{2} d \mathrm{vol}, \quad r \in(0, \varrho),$$
for some positive function $h_{r}$ on $S^{3}$, where $d$ vol is the volume form on $S^{3}$ defined by the standard metric. However,
$$\mathcal{Q}_{r}:=h_{r} \mathcal{P}_{r} h_{r}^{-1}, \quad r \in(0, \varrho),$$
is a differentiable path of self-adjoint, first-order, elliptic differential operators on the fixed, real Hilbert space underlying $\mathfrak{H}:=L^{2}\left(S^{3}, \Lambda^{1} \otimes \mathfrak{s} \mathfrak{u}\left(E_{0}\right)\right) \oplus L^{2}\left(S^{3}, W_{0}^{+} \otimes E_{0}\right)$ with
$L^{2}$ inner product (• , •) defined by the standard metric on $S^{3}$. Indeed, if we define a Hilbert-space isomorphism $\mathfrak{H}_{r} \rightarrow \mathfrak{H}$ by $(b, \psi) \mapsto(\beta, \varphi):=h_{r}(b, \psi)$, then
$$\begin{aligned}
\int_{S^{3}}\left\langle\mathcal{Q}_{r}(\beta, \varphi),\left(\beta^{\prime}, \varphi^{\prime}\right)\right\rangle d \mathrm{vol} & =\int_{S^{3}}\left\langle h_{r} \mathcal{P}_{r} h_{r}^{-1} h_{r}(b, \psi), h_{r}\left(b^{\prime}, \psi^{\prime}\right)\right\rangle d \mathrm{vol} \\
& =\int_{S^{3}}\left\langle\mathcal{P}_{r}(b, \psi),\left(b^{\prime}, \psi^{\prime}\right)\right\rangle d \operatorname{vol}_{r} \\
& =\int_{S^{3}}\left\langle(b, \psi), \mathcal{P}_{r}\left(b^{\prime}, \psi^{\prime}\right)\right\rangle d \operatorname{vol}_{r} \\
& =\int_{S^{3}}\left\langle h_{r}(b, \psi), h_{r} \mathcal{P}_{r} h_{r}^{-1} h_{r}\left(b^{\prime}, \psi^{\prime}\right)\right\rangle d \mathrm{vol},
\end{aligned}$$
and therefore,
$$\int_{S^{3}}\left\langle\mathcal{Q}_{r}(\beta, \varphi),\left(\beta^{\prime}, \varphi^{\prime}\right)\right\rangle d \mathrm{vol}=\int_{S^{3}}\left\langle(\beta, \varphi), \mathcal{Q}_{r}\left(\beta^{\prime}, \varphi^{\prime}\right)\right\rangle d \mathrm{vol}, \quad r \in(0, \varrho)$$
The operators $\mathcal{Q}_{r}$ have dense domain $L_{1}^{2}$. Since $(b, \psi)=h_{r}^{-1}(\beta, \varphi)$, we see that
$$\frac{d(b, \psi)}{d r}=-h_{r}^{-2} \frac{d h_{r}}{d r}(\beta, \varphi)+h_{r}^{-1} \frac{d(\beta, \varphi)}{d r},$$
and so, subsituting into (5.16) gives
$$\frac{d(\beta, \varphi)}{d r}=\mathcal{Q}_{r}(\beta, \varphi)+h_{r} \mathcal{Z}_{r} h_{r}^{-1}(\beta, \varphi)+h_{r}^{-1} \frac{d h_{r}}{d r}(\beta, \varphi), \quad r \in(0, \varrho),$$
with $(\beta, \varphi)$ a path in $\mathfrak{H}$.
5.3.5. Verification of the Agmon-Nirenberg conditions. We can now conclude the proof of our unique continuation result for reducible PU(2) monopoles:

Completion of proof of Proposition 5.19. The estimates (5.10) and (5.12) are, in principle, straightforward to check since we only need them for $r$ varying in the compact interval $\left[\frac{1}{2} r_{0}, r_{1}\right]$; the second condition, (5.12), requires a little more explanation since we need an estimate for $d \mathcal{Q} / d r$. We first check condition (5.10). Comparing (5.15), (5.16), and (5.18) we find that
$$\left\|\frac{d(\beta, \varphi)}{d r}-\mathcal{Q}_{r}(\beta, \varphi)\right\| \leq c_{1}\|(\beta, \varphi)\|, \quad \frac{1}{2} r_{0} \leq r \leq \frac{1}{2} \varrho,$$
for some positive constant $c_{1}=c_{1}\left(g, r_{0}, A, \Phi\right)$ and so the ordinary differential equation in (5.18) obeys the estimate (5.10) on the interval $\left[\frac{1}{2} r_{0}, r_{1}\right]$. To check condition (5.12), observe that the definition of $\mathcal{Q}_{r}$ in (5.16) and (5.17) yields the pointwise bounds
$$\left|\frac{d \mathcal{Q}_{r}}{d r}(\beta, \varphi)\right| \leq C(|(\nabla \beta, \nabla \varphi)|+|(\beta, \varphi)|),$$
where $\frac{1}{2} r_{0} \leq r \leq \frac{1}{2} \varrho$, for some positive constant $C=C\left(g, \tau, A_{W}, r_{0}\right)$, and ∇ denotes covariant derivatives on $\Lambda^{1} \otimes \mathfrak{s} \mathfrak{u}\left(E_{0}\right)$ and $W_{0}^{+} \otimes E_{0} \times S^{3}$ which are independent of $r$. Thus, using the standard elliptic estimate for $\mathcal{Q}_{r}$ we obtain the $L^{2}$ bound
$$\left\|\frac{d \mathcal{Q}_{r}}{d r}(\beta, \varphi)\right\| \leq C\left(\left\|\mathcal{Q}_{r}(\beta, \varphi)\right\|+\|(\beta, \varphi)\|\right),$$
and so, for $\frac{1}{2} r_{0} \leq r \leq \frac{1}{2} \varrho$,
$$\left|\left((\beta, \varphi), \frac{d \mathcal{Q}_{r}}{d r}(\beta, \varphi)\right)\right| \leq C\left(\left\|\mathcal{Q}_{r}(\beta, \varphi)\right\|(\beta, \varphi)\|+\|(\beta, \varphi) \|^{2}\right) .$$
Therefore, (5.12) is obeyed with $c_{2}=c_{3}=C$ on the interval $\left[\frac{1}{2} r_{0}, r_{1}\right]$. By Theorem 5.25 and Remark 5.26, the solution $(\beta(r), \varphi(r))$ vanishes for $r \in\left(0, r_{1}\right)$ since it vanishes for $r \in\left(0, r_{0}\right)$. Hence, $(a(r), \phi(r))=0$ for $r \in\left(0, r_{1}\right)$ and $\hat{u}(A, \Phi)=(A, \Phi)$ on the ball $B\left(x_{0}, r_{1}\right)$. This completes the proof of Proposition 5.19. \(\square\)

\section*{Appendix A. Holonomy perturbations and regularity}

When defining our holonomy perturbations in §2.5.2 we deferred a detailed discussion of several important regularity issues which arise in their construction. The first concerns the regularity of sections of $E$ and $\mathfrak{s} \mathfrak{u}(E)$ which are constructed by parallel transport via Sobolev connections and is described in §A.1. The second concerns the regularity of the $\mathcal{G}_{E}$ equivariant maps $\mathfrak{h}_{j, l, \alpha}: \mathcal{A}_{E}(X) \rightarrow L_{k+1}^{2}(X, \mathfrak{s} \mathfrak{u}(E))$ and we show in §A. 2 that these maps are $C^{\infty}$. (All of the $\mathcal{G}_{E}$ equivariant maps discussed here are ${ }^{\circ} \mathcal{G}_{E}$ equivariant since $S_{Z}^{1}$ acts trivially on connections in $\mathcal{A}_{E}$; if the connection on $\operatorname{det} E$ is not fixed, then all of the $\mathcal{G}_{E}$ equivariant maps are Aut $E$ equivariant.)

The definition of the maps $\mathfrak{m}_{j, l, \alpha}$ also makes use of the existence of a locally finite, $C^{\infty}$ 'positive partition' on a paracompact manifold modelled on a separable Hilbert space, in the sense of Proposition A.12. The differentials of the cutoff functions in these partitions need not be bounded a priori for the usual reason that in a Hilbert manifold, closed and bounded sets are not compact. Nonetheless, as we shall see in §A.3, it is possible to modify the standard proof [55] of the existence of a $C^{\infty}$ partition of unity on a paracompact $C^{\infty}$ manifold to produce $C^{\infty}$ cutoff functions all of whose differentials are bounded. The sums defining the perturbations $\vec{\tau} \cdot \overrightarrow{\mathfrak{m}}$ and $\vec{\vartheta} \cdot \overrightarrow{\mathfrak{m}}$ of §2.5.2 are finite when restricted to any of the open neighborhoods $\left(\pi \circ r_{Y_{j}}\right)^{-1}\left(U_{j, \alpha}\right) \subset \mathcal{A}_{E}^{*}(X)$, where $r_{Y_{j}}: \mathcal{A}_{E}(X) \rightarrow \mathcal{A}_{E}\left(Y_{j}\right)$ and $\pi: \mathcal{A}_{E}(X) \rightarrow \mathcal{B}_{E}\left(Y_{j}\right)$ is the canonical projection. However, the number of terms in these sums may be infinite in the neighborhood of a reducible connection: It is for this reason that they must converge with respect to a suitable choice of weights, as described in §2.5.2. We specify the choice of weights in § A. 4 and explain why the $\mathcal{G}_{E}$ equivariant maps $\vec{\tau} \cdot \overrightarrow{\mathfrak{m}}$ and $\vec{\vartheta} \cdot \overrightarrow{\mathfrak{m}}$ are $C^{\infty}$ on $\mathcal{A}_{E}(X)$.
A.1. Parallel transport for Sobolev connections. The fact that parallel transport is well-defined for $L_{2}^{2}$ connections has been pointed out in [61]. However, to construct $L_{k+1}^{2}$ sections constructed by parallel transport via $L_{k}^{2}$ connections with
$k \geq 2$, we need to regularize them, taking care to do this gauge equivariantly. (Given an $L_{k}^{2}$ connection $A$ it does not follow that local sections constructed by $A$-parallel transport are in $L_{k+1}^{2}$.) If we ignored the issue of equivariance then it would suffice to use the standard smoothing kernel described in [33, §7.2 \& §7.3], yielding a $C^{\infty}$ section irrespective of whether the connection is $L_{k}^{2}$ or $C^{\infty}$. Instead, we use the kernel $K_{t}(A)(x, y) \in \operatorname{Hom}\left(\left.\mathfrak{s u}(E)\right|_{y},\left.\mathfrak{s u}(E)\right|_{x}\right), t \in(0, \infty)$, of the heat operator
$$K_{t}(A)=\exp \left(-t d_{A}^{*} d_{A}\right): L^{2}(X, \mathfrak{s} \mathfrak{u}(E)) \rightarrow L_{k+1}^{2}(X, \mathfrak{s} \mathfrak{u}(E)),$$
defined by the $C^{\infty}$ metric $g$ on $T X$ and $L_{k}^{2}$ connection $A$ on $E$ [34, §1.6]; related constructions are described in [84, p. 339], [85, p. 177]. The key well-known properties [12], [34, §1.6] of the heat kernel which we need are summarized below:

Lemma A.1. Continue the above notation and suppose $\zeta \in L^{2}(X, \mathfrak{s u}(E))$.
\begin{itemize}
\item[1.] As $t \rightarrow 0$, the heat operator $\exp \left(-t d_{A}^{*} d_{A}\right)$ converges to the $L^{2}$ orthogonal projection onto $\operatorname{Ker}\left(d_{A}^{*} d_{A}\right)^{\perp}$.
\item[2.] If $A$ on $\mathfrak{s u}(E)$ is irreducible then $K_{t}(A)(x, \cdot)$ converges to the Dirac delta distribution $\delta(x, \cdot)$.
\item[3.] If $A$ is $L_{k}^{2}$ then $K_{t}(A) \zeta$ is $L_{k+1}^{2}$; if $A$ is $C^{\infty}$ then $K_{t}(A) \zeta$ is $C^{\infty}$.
\item[4.] If $\zeta \in C^{0}(\widetilde{U}, \mathfrak{s u}(E))$, for an open set $\widetilde{U} \subset X$, and $A$ is irreducible on $\mathfrak{s} \mathfrak{u}(E)$, then $K_{t}(A) \zeta \rightarrow \zeta$ in $C^{0}(U, \mathfrak{s} \mathfrak{u}(E))$ as $t \rightarrow 0$ for any open subset $U \in \widetilde{U}$.
\end{itemize}

Lemma A. 1 continues to hold for unitary connections $A$ on Hermitian bundles $E$ over compact $C^{\infty}$ manifolds with boundary $\bar{Y}=Y \cup \partial Y$; we use the Neumann boundary conditions of [20, p. 192], [87, Proposition 2.1] to obtain an $L^{2}$ self-adjoint Laplacian $d_{A}^{*} d_{A}$. Our main application will be to sections defined by parallel translation:

Lemma A.2. Let $k \geq 2$ be an integer and let $A$ be an $L_{k}^{2}$ unitary connection on a Hermitian two-plane bundle $E$ over $X$. Let $x_{0}$ be a point in $X$, let $\left.\zeta_{0} \in \mathfrak{s u}(E)\right|_{x_{0}}$, and let $B\left(x_{0}, r\right)$ be a geodesic ball with center $x_{0}$ and radius $r>0$.
\begin{itemize}
\item[1.] Parallel transport with respect to $A$ is well-defined along $C^{\infty}$ paths in $X$.
\item[2.] If $\zeta$ is the section of $\left.\mathfrak{s u}(E)\right|_{B\left(x_{0}, r\right)}$ obtained by $A$-parallel transport of $\zeta_{0}$ along radial geodesics originating at $x_{0}$ and $A$ is $C^{\infty}$ then $\zeta$ is $C^{\infty}$ on $B\left(x_{0}, r\right)$. If $A$ is $L_{k}^{2}$ then $\zeta$ is $C^{0}$ on $B\left(x_{0}, r\right)$ and its mollification $K_{t}\left(\left.A\right|_{B\left(x_{0}, r\right)}\right) \zeta$ is $L_{k+1}^{2}$ on $B\left(x_{0}, r\right)$ for any $t>0$.
\end{itemize}

Proof. Let $\gamma:[0,1] \rightarrow X$ be a $C^{\infty}$ path such that $\gamma(0)=x_{0}$ and let $U \subset X$ be an open neighborhood of $\gamma([0,1])$. We may suppose without loss of generality that $A \in L_{k}^{2}\left(U, \Lambda^{1} \otimes \mathfrak{u}(2)\right)$ is a connection matrix and consider the parallel transport of $\eta_{0} \in \mathbb{C}^{2}$. Note that we have a continuous Sobolev embedding $L_{2}^{2}(U) \rightarrow L^{2}([0,1])$ [2, Theorem V.4]. We wish to solve the ordinary differential equation
$$\frac{d \eta}{d t}+a \eta=0, \quad t \in[0,1],$$
where $a=\gamma^{*} A \in L^{2}([0,1], \mathfrak{u}(2))$, with initial condition $\eta(0)=\eta_{0}$, for a solution $\eta \in\left(L_{1}^{2} \cap C^{0}\right)\left([0,1], \mathbb{C}^{2}\right)$.

If $A$ is $C^{\infty}$ then there is a unique solution $\eta \in C^{\infty}\left([0,1], \mathbb{C}^{2}\right)$ to (A.1) (see, for example, [36]) and it obeys the inequality [36, Lemma IV.4.1]
$$\begin{aligned}
|\eta(t)| & \leq\left|\eta_{0}\right| \exp \left(\int_{0}^{t}|a(s)| d s\right) \\
& \leq\left|\eta_{0}\right| \exp \left(\|a\|_{L^{1}([0,1])}\right) \leq\left|\eta_{0}\right| \exp \left(c\|A\|_{L_{2}^{2}(U)}\right),
\end{aligned}$$
for $t \in[0,1]$. If $A$ is only $L_{2}^{2}$, we may choose any sequence $\left\{A_{\alpha}\right\}$ of $C^{\infty}$ connections which converge to $A$ in $L_{2}^{2}$ and let $\left\{\eta_{\alpha}\right\}$ be the corresponding sequence of $C^{\infty}$ solutions to (A.1). From (A.2) it follows that $\left\{\eta_{\alpha}\right\}$ is $C^{0}$-Cauchy and then (A.1) implies that $\left\{\eta_{\alpha}\right\}$ is $L_{1}^{2}$-Cauchy with limit $\eta \in\left(L_{1}^{2} \cap C^{0}\right)\left([0,1], \mathbb{C}^{2}\right)$ solving (A.1). This proves Assertion (1).

From the proof of Assertion (1) we see that $\zeta \in C^{0}(U, \mathfrak{s} \mathfrak{u}(2))$. If the connection $A$ is $C^{\infty}$ on $B\left(x_{0}, r\right)$ then by differentiating (A.1) with respect to local coordinates (regarded as parameters [36, Chapter 5]) on $B\left(x_{0}, r\right)$ and solving the resulting first order ordinary differential equations for the derivatives, it follows that the section $\zeta$ is $C^{\infty}$ on $B\left(x_{0}, r\right)$. The rest of Assertion (2) follows from the properties of the smoothing kernel $K_{t}(A)(x, y)$ given in Lemma A.1. \(\square\)
A.2. Regularity of holonomy maps. We consider the regularity of the holonomy maps from $A \in \mathcal{A}_{E}$ to $\left.h_{\gamma, x_{0}}(A) \in \mathfrak{u}(E)\right|_{x_{0}}$, to $\hat{\mathfrak{h}}_{\gamma}(A) \in C^{0}\left(B\left(x_{0}, r_{0}\right), \mathfrak{s u}(E)\right)$, and to $\mathfrak{h}_{\gamma}(A) \in L_{k+1}^{2}\left(B\left(x_{0}, r_{0}\right), \mathfrak{s} \mathfrak{u}(E)\right)$. See also [8, §3.3], [29, Lemma 1b.1], [86, §8a], and [90, §5A] for related calculations.

Let $\gamma:[0,1] \rightarrow X$ denote a parametrization for an oriented path $\gamma \subset X$ with $\gamma(0)=x_{0}$. The general Sobolev embedding [2, Theorem V.4] implies that we have a continuous restriction map $L_{k}^{2}\left(X, \Lambda^{1} \otimes \mathfrak{s} \mathfrak{u}(E)\right) \rightarrow L_{k-2}^{2}\left(\gamma, \Lambda^{1} \otimes \mathfrak{s} \mathfrak{u}(E)\right)$, for $k \geq 2$. We fix an isomorphism $\left.E\right|_{\gamma} \simeq \gamma \times \mathbb{C}^{2}$ of U(2) bundles and denote the connection matrix corresponding to a unitary connection $A$ on $E$ again by $A \in L_{k-2}^{2}\left(\gamma, \Lambda^{1} \otimes \mathfrak{u}(2)\right)$. Let $A+s a, s \in \mathbb{R}$, be a one-parameter family of nearby connections on $E$, with connection matrices $A(t)+s a(t) \in L_{k-2}^{2}\left(\gamma, \Lambda^{1} \otimes \mathfrak{u}(2)\right)$. Let $\xi_{0} \in \mathbb{C}^{2}$ correspond to a point in the fiber $\left.E\right|_{x_{0}}$ and, with respect to the connection $A+s a$, let $\xi(t ; s)$ be the parallel transport of $\xi_{0}$ along $\gamma(t)$, so $\xi(t ; s)$ solves
$$\left(\frac{d}{d t}+A(t)+s a(t)\right) \xi(t ; s)=0, \quad \xi(0 ; s)=\xi_{0} .$$
Thus, if $P_{\gamma}(t ; A) \in \operatorname{Isom}\left(\left.E\right|_{\gamma(0)}, E_{\gamma(t)}\right) \simeq \mathrm{U}(2)$ denotes parallel transport along $\gamma$ from $\gamma(0)$ to $\gamma(t)$ with respect to the connection $A$, we have
$$\xi(t ; s)=P_{\gamma}(t ; A+s a) \xi_{0}, \quad t \in[0,1] .$$

Therefore, our task is to compute
$$\left(D P_{\gamma}(t ; \cdot)\right)_{A}(a) \xi_{0}=\left.\frac{d}{d s} P_{\gamma}(t ; A+s a) \xi_{0}\right|_{s=0}=\left.\frac{d \xi}{d s}(t ; s)\right|_{s=0}, \quad t \in[0,1] .$$
Differentiating (A.3) with respect to $s$ we see that $d \xi(t ; s) / d s$ solves
$$\left(\frac{d}{d t}+A(t)+s a(t)\right) \frac{d \xi}{d s}=-a(t) \xi(t ; s), \quad \frac{d \xi}{d s}(0 ; s)=0 .$$
Let $Y(t ; s)$ be the fundamental matrix solution for the linear differential operator on the left-hand side, so the solution $d \xi(t ; s) / d s$ can be written as [36, Corollary IV.2.1]
$$\frac{d \xi}{d s}(t ; s)=-Y(t ; s) \int_{0}^{t} Y^{-1}(\tau ; s) a(\tau) \xi(\tau ; s) d \tau$$
Since $\xi(t ; s)=Y(t ; s) \xi_{0}=P_{\gamma}(t ; A+s a) \xi_{0}$ for any $\left.\xi_{0} \in E\right|_{\gamma(0)}$, setting $s=0$ above gives
$$\left(D P_{\gamma}(t ; \cdot)\right)_{A}(a)=-P_{\gamma}(t ; A) \int_{0}^{t} P_{\gamma}^{-1}(\tau ; A) a(\tau) P_{\gamma}(\tau ; A) d \tau$$
and so, by the Sobolev embedding theorem, a derivative bound
$$\left|\left(D P_{\gamma}(t ; \cdot)\right)_{A}(a)\right| \leq\|a\|_{L^{1}(\gamma)} \leq c\|a\|_{L_{2, A}^{2}(X)}, \quad t \in[0,1] .$$
The estimate (A.6) implies that the right-hand side of (A.5) is well-defined whenever $k \geq 2$. In particular, when $t=1$ we have $P_{\gamma}(1 ; A)=h_{\gamma, x_{0}}(A)$, and so (A.5) gives
$$\left(D h_{\gamma, x_{0}}\right)_{A}(a)=-h_{\gamma, x_{0}}(A) \int_{\gamma} P_{\gamma}^{-1}(A) a P_{\gamma}(A) .$$
Thus, we have a well-defined differential
$$\left(D h_{\gamma, x_{0}}\right)_{A}:\left.\left.L_{k}^{2}\left(X, \Lambda^{1} \otimes \mathfrak{u}(E)\right) \rightarrow T_{h_{\gamma, x_{0}}(A)} \mathrm{U}(E)\right|_{x_{0}} \simeq \mathfrak{u}(E)\right|_{x_{0}}$$
of the holonomy map $h_{\gamma, x_{0}}:\left.\mathcal{A}_{E}(X) \rightarrow \mathrm{U}(E)\right|_{x_{0}}$ at the point $A \in \mathcal{A}_{E}(X)$.
A similar argument shows that all higher derivatives exist by repeatedly applying the derivative formulas (A.5) and (A.7) (see, for example, [86, §8a]) and so we may conclude:

Lemma A.3. For $k \geq 2$, the holonomy map $h_{\gamma, x_{0}}:\left.\mathcal{A}_{E}(X) \rightarrow \mathrm{U}(E)\right|_{x_{0}}$ is $C^{\infty}$.
In the same vein, the holonomy map $h_{\gamma, x_{0}}:\left.\mathcal{A}_{E}(X) \rightarrow \operatorname{SO}(\mathfrak{s u}(E))\right|_{x_{0}}$ is $C^{\infty}$ and we have: we have:

Lemma A.4. For $k \geq 2$, the following holonomy maps are $C^{\infty}$ :
$$\begin{aligned}
& \mathcal{A}_{E}(X) \ni A \mapsto \hat{\mathfrak{h}}_{\gamma}(A) \in C^{0}\left(B\left(x_{0}, r_{0}\right), \mathfrak{s u}(E)\right), \\
& \mathcal{A}_{E}(X) \ni A \mapsto \mathfrak{h}_{\gamma}(A) \in L_{k+1}^{2}\left(B\left(x_{0}, r_{0}\right), \mathfrak{s} \mathfrak{u}(E)\right) .
\end{aligned}$$

Proof. The fact that $\hat{\mathfrak{h}}_{\gamma}$ is a $C^{\infty}$ map follows from the proof of Lemma A.3. The map $\mathfrak{h}_{\gamma}$ is defined by $\mathfrak{h}_{\gamma}(A)=K_{t}(A) \hat{\mathfrak{h}}_{\gamma}(A)$ and so the conclusion follows from the fact that the map $\mathcal{A}_{E}(X) \ni A \mapsto K_{t}(A) \in \operatorname{Hom}\left(L^{2}\left(B\left(x_{0}, r_{0}\right), \mathfrak{s u}(E)\right), L_{k+1}^{2}\left(B\left(x_{0}, r_{0}\right), \mathfrak{s u}(E)\right)\right)$ is $C^{\infty}$. \(\square\)
A.3. Positive partitions and cutoff functions with bounded differentials on Hilbert manifolds. We modify Lang's proof of the existence of a $C^{\infty}$ partition of unity on a paracompact $C^{\infty}$ manifold modelled on a separable Hilbert space [55, Corollary II.3.8] to produce a $C^{\infty}$ positive partition whose cutoff functions have bounded differentials of all orders; see Proposition A.12. Recall:

Proposition A.5. [55, Corollary II.3.8] Let $\mathcal{X}$ be a paracompact $C^{\infty}$ manifold modelled on a separable Hilbert space $\mathfrak{H}$. Then $\mathcal{X}$ admits locally finite, $C^{\infty}$ partitions of unity: For any open cover of $\mathcal{X}$ there is a countable, locally finite open subcover $\left\{U_{\alpha}\right\}_{\alpha=1}^{\infty}$ and a family of $C^{\infty}$ functions $\psi_{\alpha}: \mathcal{X} \rightarrow[0,1]$ such that
\begin{itemize}
\item[-] $\operatorname{supp} \psi_{\alpha} \subset U_{\alpha}$,
\item[-] $\sum_{\alpha=1}^{\infty} \psi_{\alpha}(x)=1$ for all $x \in \mathcal{X}$.
\end{itemize}

We shall need the following generalizations to a Banach space setting of the analogous familiar facts from analysis on finite-dimensional spaces.

Lemma A.6. [1, Proposition 1.3.10] Let $M$ be a topological space and let $(N, d)$ be a complete metric space. Then the set $C(M, N)$ of all bounded continuous maps is a complete metric space with respect to the metric $D(f, g):=\sup \{d(f(x), g(x)): x \in$ $M\}$.

Let $\mathbf{E}, \mathbf{F}$ be Banach spaces and let $U \subset \mathbf{E}$ be an open subset. By analogy with the usual definitions in finite dimensions, we let $C^{s}(U, \mathbf{F})$ be the set of $C^{s}$ maps $f: U \rightarrow \mathbf{F}$ with norm
$$\|f\|_{C^{s}(U)}:=\max _{0 \leq p \leq s} \sup _{x \in U}\left\|\left(D^{p} f\right)_{x}\right\|<\infty,$$
where $\left\|\left(D^{p} f\right)_{x}\right\|$ is the norm of $\left(D^{p} f\right)_{x} \in \operatorname{Hom}\left(\otimes^{p} \mathbf{E}, \mathbf{F}\right)$. Lemma A. 6 implies that $C^{0}(U, \mathbf{F})$ is a Banach space. In general we have:

Lemma A.7. For any integer $s \geq 0$, the set $C^{s}(U, \mathbf{F})$ is a Banach space.
Proof. For the case $s=1$ this follows from Lemma A. 6 and [37, Theorem 1.1.5]. The general case [1, pp. 113-114] is proved in the same way using Taylor's Theorem. \(\square\)

By analogy with the finite-dimensional case we set $C^{\infty}(U, \mathbf{F})=\cap_{s \geq 0} C^{s}(U, \mathbf{F})$.
The $C^{\infty}$ cutoff functions produced by Proposition A. 5 may not necessarily have bounded differentials on Hilbert manifolds, as their supports are not compact, so we now describe a modified procedure which does produce bounded cutoff functions.

Lemma A.8. [55, Lemma II.3.5] Let $M$ be a metric space and let $\left\{B_{\alpha}\right\}_{\alpha=1}^{\infty}$ be a covering of a subset $W \subset M$ by open balls. Then there exists a locally finite open covering $\left\{V_{\alpha}\right\}_{\alpha=1}^{\infty}$ of $W$ such that $V_{\alpha} \subset B_{\alpha}$ for all $\alpha$ and
$$V_{\alpha}=B_{\alpha} \cap{ }^{c} \bar{B}\left(x_{\alpha, 1}, r_{\alpha, 1}\right) \cap \cdots \cap{ }^{c} \bar{B}\left(x_{\alpha, \alpha-1}, r_{\alpha, \alpha-1}\right),$$
where ${ }^{c} \bar{B}=M-\bar{B}$.
Lemma A.9. Let $B_{0}, B_{1} \ldots, B_{m}$ be open balls in a Hilbert space $\mathfrak{H}$ and let $V$ be a scalloped open subset:
$$V=B_{0} \cap{ }^{c} \bar{B}_{1} \cap \cdots \cap{ }^{c} \bar{B}_{m} .$$
Then there exists a $C^{\infty}$ function $\omega: \mathfrak{H} \rightarrow[0,1]$ such that $\omega(x)>0$ if $x \in V$ and $\omega(x)=0$ otherwise, while the differentials $D^{p} \omega$ are bounded for all $p \in \mathbb{N}$ with bounds depending only on $p, r_{0}, \ldots, r_{m}$.

Proof. Let $\varphi: \mathbb{R} \rightarrow[0,1]$ be a $C^{\infty}$ function such that $\varphi(t)=1$ for $t \leq 1,0<\varphi(t)<1$ for $1<t<2$, and $\varphi(t)=0$ for $t \geq 2$. Suppose $B_{\alpha}=B\left(x_{\alpha}, r_{\alpha}\right)$ for $\alpha=0, \ldots, m$. Set
$$\varphi_{\alpha}(x):=\varphi\left(r_{\alpha}^{-2}\left\|x-x_{\alpha}\right\|^{2}\right), \quad x \in \mathfrak{H}, \quad \alpha=1, \ldots, m,$$
so $0 \leq \varphi_{\alpha}<1$ on ${ }^{c} \bar{B}_{\alpha}$ and $\varphi_{\alpha}=1$ on $\bar{B}_{\alpha}$. Set $\varphi_{0}(x)=\varphi\left(2 r_{0}^{-2}\left\|x-x_{0}\right\|^{2}\right)$, so $0<\varphi_{0} \leq 1$ on $B_{0}$ and $\varphi_{0}=0$ on ${ }^{c} B_{0}$. Then
$$\omega:=\varphi_{0} \prod_{\alpha=1}^{m}\left(1-\varphi_{\alpha}\right)$$
is positive on $V$ and zero on ${ }^{c} V=\mathfrak{H}-V$, while
$$\left\|D^{p} \omega\right\| \leq C,$$
for some positive constant $C=C\left(\varphi, p, r_{0}, \ldots, r_{m}\right)$ and all $p \in \mathbb{N}$. \(\square\)

Lemma A.10. Let $A_{1}, A_{2}$ be non-empty, closed disjoint subsets of a separable Hilbert space $\mathfrak{H}$. Then there exists a $C^{\infty}$ function $\chi: \mathfrak{H} \rightarrow[0,1]$ such that $\chi(x)=0$ if $x \in A_{1}$ and $\chi(x)>0$ if $x \in A_{2}$, with bounded differentials of all orders.

Proof. By Lindelöf's Theorem there is a countable collection of balls $\left\{B_{\alpha}\right\}_{\alpha=1}^{\infty}$ covering $A_{2}$ and such that $B_{\alpha} \subset{ }^{c} A_{1}=\mathfrak{H}-A_{1}$. Let $W=\cup_{\alpha} B_{\alpha}$ and find a locally finite refinement $\left\{V_{\alpha}\right\}$ of scalloped open subsets $V_{\alpha} \subset B_{\alpha}$ using Lemma A. 8 which covers $W$. Using Lemma A. 9 we find a $C^{\infty}$ function $\omega_{\alpha}: \mathfrak{H} \rightarrow \mathbb{R}$ such that $\omega_{\alpha}$ is positive on $V_{\alpha}$, zero on ${ }^{c} V_{\alpha}$, and has bounded differentials of all orders. The sum
$$\chi:=\sum_{\alpha=1}^{\infty} \frac{2^{-\alpha} \omega_{\alpha}}{1+\left\|\omega_{\alpha}\right\|_{C^{\alpha}(\mathfrak{H})}}$$
is finite on any neighborhood $V_{\alpha}$. The function $\chi: \mathfrak{H} \rightarrow \mathbb{R}$ is positive on $\cup_{\alpha} V_{\alpha}=$ $W \supset A_{2}$ and zero on $A_{1}$. Moreover, $\chi$ has bounded differentials of all orders, as desired. \(\square\)

Remark A.11. It is at this point that the usual proof of existence of a partition of unity encounters difficulties if we wish to ensure that the cutoff function $\chi$ has bounded differentials of all orders. In the proof of Theorem II.3.7 of [55], Lang first constructs a function $\omega$ obeying the conclusions of Lemma A. 10 and then a $C^{\infty}$ function $\sigma: \mathfrak{H} \rightarrow \mathbb{R}$ such that $\sigma>0$ on the closed set ${ }^{c} U$ disjoint from $A_{2}$, where $U$ is the open set where $\omega>0$, and $\sigma=0$ on $A_{2}$. He then defines $\chi=\omega /(\omega+\sigma)$, so $\chi=1$ on $A_{2}$. In finite dimensions, the compactness of closed bounded sets ensures that $\chi$ will have bounded differentials of all orders if $A_{2}$ is bounded, but this obviously fails in infinite dimensions.

Proposition A.12. Let $\mathcal{X}$ be a paracompact $C^{\infty}$ manifold modelled on a separable Hilbert space $\mathfrak{H}$. Then $\mathcal{X}$ admits a locally finite, $C^{\infty}$ positive partition: For any open cover of $\mathcal{X}$ there is a countable, locally finite open subcover by parametrizations $\left\{U_{\alpha}, \pi_{\alpha}\right\}_{\alpha=1}^{\infty}$, where $\pi_{\alpha}: \mathfrak{H} \supset \mathbf{U}_{\alpha} \simeq U_{\alpha} \subset \mathcal{X}$, and a family of $C^{\infty}$ functions $\chi_{\alpha}: \mathcal{X} \rightarrow$ [0, 1] such that
\begin{itemize}
\item[-] $\operatorname{supp} \chi_{\alpha} \subset U_{\alpha}$,
\item[-] $\sum_{\alpha=1}^{\infty} \chi_{\alpha}(x)>0$ for all $x \in \mathcal{X}$,
\item[-] $\chi_{\alpha} \circ \pi_{\alpha}: \mathfrak{H} \rightarrow[0,1]$ has bounded differentials of all orders.
\end{itemize}

Proof. Let $\left\{B_{x}\right\}$ be an open covering of $\mathcal{X}$ by balls and, using paracompactness and Lemma A.8, let $\left\{U_{\alpha}\right\}$ be a countable, locally finite refinement such that each open subset $U_{\alpha}$ is contained in some $B_{x(\alpha)}$, where $\pi_{\alpha}^{-1}: \mathcal{X} \supset B_{x(\alpha)} \rightarrow \mathfrak{H}$ is a coordinate chart and $\pi_{\alpha}^{-1}\left(U_{\alpha}\right)=\mathbf{U}_{\alpha}$. We now find open refinements $\left\{V_{\alpha}\right\}$ and then $\left\{W_{\alpha}\right\}$ such that
$$\bar{W}_{\alpha} \subset V_{\alpha} \subset \bar{V}_{\alpha} \subset U_{\alpha},$$
the bar denoting closure in $\mathcal{X}$. For each $\alpha$, Lemma A. 10 and the identification $\pi_{\alpha}$ : $\mathfrak{H} \supset \mathbf{U}_{\alpha} \simeq U_{\alpha} \subset \mathcal{X}$, provides a $C^{\infty}$ cutoff function $\chi_{\alpha}: \mathcal{X} \rightarrow \mathbb{R}$ such that $\chi_{\alpha}>0$ on $\bar{W}_{\alpha}$ and $\chi_{\alpha}=0$ on $\mathcal{X}-V_{\alpha}$. The $C^{\infty} \operatorname{map} \chi_{\alpha} \circ \pi_{\alpha}: \mathbf{U}_{\alpha} \rightarrow[0,1]$ extends by zero to a $C^{\infty}$ map $\chi_{\alpha} \circ \pi_{\alpha}: \mathfrak{H} \rightarrow[0,1]$ having bounded differentials of all orders. Then $\left\{U_{\alpha}, \chi_{\alpha}\right\}$ is the desired positive partition. \(\square\)

Let $\bar{Y}=Y \cup \partial Y \subset X$ be a smooth submanifold-with-boundary. For any open subset $U \subset \mathcal{A}_{E}(Y)$ and $C^{s}$ function $f: U \rightarrow \mathbb{C}$, we define
$$\|f\|_{C^{s}(U)}:=\sup _{A \in U} \sup _{\left\|a_{i}\right\|_{L_{k}^{2}, A^{(Y)}} \leq 1}\left|\left(D^{s} f\right)_{A}\left(a_{1}, \ldots, a_{s}\right)\right| .$$
Let $\left\{B\left(\left[A_{\alpha}\right], r_{\alpha}\right)\right\}$ be a countable covering of $\mathcal{B}_{E}^{*}(Y)$ by $L_{k}^{2}$ balls with subordinate locally finite subcover $\left\{U_{\alpha}\right\}$ and $C^{\infty}$ positive partition $\left\{\chi_{\alpha}\right\}$, with $\operatorname{supp} \chi_{\alpha} \subset U_{\alpha}$. We may suppose that $B\left(\left[A_{\alpha}\right], r_{\alpha}\right)=\pi\left(\mathbf{B}\left(A_{\alpha}, r_{\alpha}\right)\right)$, where $\mathbf{B}\left(A_{\alpha}, r_{\alpha}\right) \subset \mathcal{A}_{E}^{*}(Y)$ is an open $L_{k}^{2}$ ball in the Coulomb slice $A_{\alpha}+\operatorname{Ker} d_{A_{\alpha}}^{*}$ with center $A_{\alpha}$ and radius $r_{\alpha}$, and $\pi: \mathcal{A}_{E}^{*}(Y) \rightarrow \mathcal{B}_{E}^{*}(Y)$ is the canonical projection. Let $\mathbf{U}_{\alpha}=\pi^{-1}\left(U_{\alpha}\right) \cap \mathbf{B}\left(A_{\alpha}, r_{\alpha}\right)$, so
$\mathbf{U}_{\alpha} \subset A_{\alpha}+\operatorname{Ker} d_{A_{\alpha}}^{*}$ and
$$\operatorname{supp} \chi_{\alpha} \circ \pi \subset \pi^{-1}\left(U_{\alpha}\right)=\mathcal{G}_{E}(Y) \cdot \mathbf{U}_{\alpha} \simeq \mathcal{G}_{E}(Y) \times \mathbf{U}_{\alpha} .$$
Now $\chi_{\alpha} \circ \pi(u(A))=\chi_{\alpha} \circ \pi(A)$ for all $u \in \mathcal{G}_{E}(Y)$ and by the construction of Proposition A. 12 the $C^{\infty}$ map
$$\chi_{\alpha} \circ \pi: A_{\alpha}+\operatorname{Ker} d_{A_{\alpha}}^{*} \subset L_{k+1}^{2}(Y, \mathfrak{s u}(E)) \rightarrow[0,1]$$
has bounded differentials of all orders with respect to the fixed $L_{k+1, A_{\alpha}}^{2}$ norm on $L_{k+1}^{2}(Y, \mathfrak{s} \mathfrak{u}(E))$, that is, it has bounded differentials of all orders in the sense of Proposition A.12. Now for any $A \in \mathbf{U}_{\alpha}$ the $L_{k+1, A_{\alpha}}^{2}$ and $L_{k+1, A}^{2}$ norms on $L_{k+1}^{2}(Y, \mathfrak{s u}(E))$ compare uniformly with constants depending only on $r_{\alpha} \geq\left\|A-A_{\alpha}\right\|_{L_{k ; A_{\alpha}}^{2}}$ (since $k \geq 2$ ), and so the maps (A.9) have bounded differentials of all orders in the sense of Equation (A.8). Moreover, the same holds for the maps
$$\chi_{\alpha} \circ \pi: \mathcal{A}_{E}^{*}(Y) \rightarrow[0,1] .$$
Finally, we have a restriction map $r_{Y}: \mathcal{A}_{E}^{*}(X) \rightarrow \mathcal{A}_{E}^{*}(Y)$ given by $\left.A \mapsto A\right|_{Y}$ and the composition
$$\chi_{\alpha} \circ \pi \circ r_{Y}: \mathcal{A}_{E}^{*}(X) \rightarrow[0,1]$$
again has bounded differentials of all orders in the sense of Equation (A.8).
A.4. Uniform convergence of holonomy perturbations on neighborhoods of reducibles. In §2.5.2 we constrained the sequences perturbations $\vec{\tau}$ and $\vec{\vartheta}$ to vary in certain weighted $\ell_{\delta}^{1}$ spaces. We now show that a sequence of positive weights $\delta \in \ell^{\infty}\left(\mathbb{R}^{+}\right)$may be chosen in such a way that the sums $\vec{\tau} \cdot \overrightarrow{\mathfrak{m}}$ and $\vec{\vartheta} \cdot \overrightarrow{\mathfrak{m}}$ and all their differentials converge uniformly on $\mathcal{A}_{E}(X)$.

For any open subset $U \subset \mathcal{A}_{E}(X)$ and $C^{s}$ map $\mathfrak{f}: U \rightarrow L_{k+1}^{2}(X, \mathfrak{s} \mathfrak{u}(E))$, we define
$$\|\mathfrak{f}\|_{C^{s}(U)}:=\sup _{A \in U} \sup _{\substack{1 \leq i \leq s \\\left\|a_{i}\right\|_{L_{k},( }^{2}(X) \leq 1}}\left\|\left(D^{s} \mathfrak{f}\right)_{A}\left(a_{1}, \ldots, a_{s}\right)\right\|_{L_{k+1, A}^{2}(X)}^{2} .$$
We then have:
Proposition A.13. Continue the notation of §2.5.2 and let $k \geq 2$ be an integer. Then there exists a sequence $\delta=\left(\delta_{\alpha}\right)_{\alpha=1}^{\infty} \in \ell^{\infty}((0,1])$ of positive weights such that the $\mathcal{G}_{E}$ equivariant maps
$$\begin{aligned}
& \vec{\tau} \cdot \overrightarrow{\mathfrak{m}}: \mathcal{A}_{E}(X) \rightarrow L_{k+1}^{2}\left(X, \mathfrak{g} \mathfrak{l}\left(\Lambda^{+}\right) \otimes_{\mathbb{R}} \mathfrak{s} \mathfrak{o}(\mathfrak{s} \mathfrak{u}(E))\right), \\
& \vec{\vartheta} \cdot \overrightarrow{\mathfrak{m}}: \mathcal{A}_{E}(X) \rightarrow L_{k+1}^{2}\left(X, \operatorname{Hom}\left(W^{+}, W^{-}\right) \otimes_{\mathbb{C}} \mathfrak{s l}(E)\right),
\end{aligned}$$
are $C^{\infty}$, with uniformly bounded differentials of all orders in the sense of (A.10). In particular, they satisfy the following $C^{0}$ estimates for $r \geq k+1$,
$$\begin{aligned}
& \sup _{A \in \mathcal{A}_{E}}\|\vec{\vartheta} \cdot \overrightarrow{\mathfrak{m}}(A)\|_{L_{k+1, A}^{2}(X)} \leq C\|\vec{\vartheta}\|_{\ell_{\delta}^{1}\left(C^{r}(X)\right)}, \\
& \sup _{A \in \mathcal{A}_{E}}\|\vec{\tau} \cdot \overrightarrow{\mathfrak{m}}(A)\|_{L_{k+1, A}^{2}(X)} \leq C\|\vec{\tau}\|_{\ell_{\delta}^{1}\left(C^{r}(X)\right)},
\end{aligned}$$
for some positive constant $C=C(g, k)$, and more generally they satisfy the $C^{s}$ estimates of (A.11) and (A.12), for every integer $s \geq 0$.

Remark A.14. As should be clear from their definition, the maps $\vec{\tau} \cdot \overrightarrow{\mathfrak{m}}$ and $\vec{\vartheta} \cdot \overrightarrow{\mathfrak{m}}$ are not analytic, although this will cause no difficulty in practice.

Proof. It suffices to consider $\vec{\vartheta} \cdot \overrightarrow{\mathfrak{m}}$, since the argument for $\vec{\tau} \cdot \overrightarrow{\mathfrak{m}}$ is obviously identical. We first observe that the sum $\vec{\vartheta} \cdot \overrightarrow{\mathfrak{m}}(A)$ is finite for each connection $A \in \mathcal{A}_{E}(X)$, and so defines an element of $L_{k+1}^{2}\left(X, \operatorname{Hom}\left(W^{+}, W^{-}\right) \otimes \mathfrak{g l}(E)\right)$, while it is identically zero if $A$ is reducible on $X$. However, on any open neighborhood of a reducible connection $A \in \mathcal{A}_{E}(X)$, the number of terms in the sum $\vec{\vartheta} \cdot \overrightarrow{\mathfrak{m}}$ may be infinite and so our task is to choose a sequence of weights $\delta$ such that this sum and all its differentials converge uniformly on $\mathcal{A}_{E}(X)$. The sum $\vec{\vartheta} \cdot \overrightarrow{\mathfrak{m}}$ will then define a $C^{\infty}$ map. We begin with a couple of preparatory lemmas.

Lemma A.15. Let $\bar{Y}=Y \cup \partial Y \subset X$ be a smooth submanifold with boundary, let $B\left(A_{0}, r_{0}\right) \subset \mathcal{A}_{E}^{*}(Y)$ be an open $L_{k}^{2}$ ball with $k \geq 2$, and let $\eta \in L^{2}(Y, \mathfrak{s u}(E))$. Then the maps
$$B\left(A_{0}, r_{0}\right) \ni A \mapsto \mathfrak{f}(A):=e^{-t d_{A}^{*} d_{A}} \eta \in L_{k+1}^{2}(Y, \mathfrak{s} \mathfrak{u}(E))$$
have bounded differentials of all orders, in the sense of (A.10), with constants $c=$ $c\left(k, r_{0}, s, t\right)$ :
$$\|\mathfrak{f}\|_{C^{s}\left(B\left(A_{0}, r_{0}\right)\right)} \leq c\|\eta\|_{L^{2}(Y)} .$$
Proof. The Sobolev multiplication theorems and the fact that $k \geq 2$ imply that the norms
$$\|\zeta\|_{L_{k+1, A}^{2}(Y)} \quad \text { and } \quad\|\zeta\|_{L_{k+1, A}^{2}(Y)}^{\prime}:=\left\|\left(1+\Delta_{A}\right)^{(k+1) / 2} \zeta\right\|_{L^{2}(Y)}$$
on $L_{k+1}^{2}(Y, \mathfrak{s u}(E))$ are equivalent for $A \in B\left(A_{0}, r_{0}\right) \subset \mathcal{A}_{E}^{*}(Y)$, with constants depending at most on $k, r_{0}$.