---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: On boundary value problems for Einstein metrics]

---
source_file: On_boundary_value_problems_for_Einstein_metrics_10572b2b78cb.pdf
converter: mathpix
format: mmd
---

\title{
On boundary value problems for Einstein metrics
}

\author{
Michael T Anderson
}

On any given compact manifold $M^{n+1}$ with boundary $\partial M$, it is proved that the moduli space $\mathcal{E}$ of Einstein metrics on $M$, if non-empty, is a smooth, infinite dimensional Banach manifold, at least when $\pi_{1}(M, \partial M)=0$. Thus, the Einstein moduli space is unobstructed. The usual Dirichlet and Neumann boundary maps to data on $\partial M$ are smooth, but not Fredholm. Instead, one has natural mixed boundaryvalue problems which give Fredholm boundary maps.

These results also hold for manifolds with compact boundary which have a finite number of locally asymptotically flat ends, as well as for the Einstein equations coupled to many other fields.

58J05, 58J32; 53C25

\section*{1 Introduction}

Let $M=M^{n+1}$ be a compact $(n+1)$-dimensional manifold with boundary $\partial M$, $n \geq 2$. In this paper, we consider the structure of the space of Einstein metrics on $(M, \partial M)$, ie metrics $g$ on $\bar{M}=M \cup \partial M$ satisfying the Einstein equations
$$\operatorname{Ric}_{g}=\lambda g .$$
Here $\lambda$ is a fixed constant, equal to $\frac{s}{n+1}$, where $s$ is the scalar curvature. It is natural to consider boundary value problems for the equations (1-1). For example, the Dirichlet problem asks: given a (smooth) Riemannian metric $\gamma$ on $\partial M$, determine whether there exists a Riemannian metric $g$ on $\bar{M}$, which satisfies the Einstein equations (1-1) with the boundary condition
$$\left.g\right|_{T(\partial M)}=\gamma .$$
Although there has been a great deal of interest in such existence (and uniqueness) questions on compact manifolds without boundary, very little in the way of general results or a general theory are known, cf Besse [5] and LeBrun-Wang [13] for surveys. Similarly, this question has been extensively studied for complete metrics on noncompact manifolds, particularly in the asymptotically Euclidean, flat and asymptotically
hyperbolic settings. However, Einstein metrics on manifolds with boundary, which are in a sense intermediate between the compact and complete, non-compact cases, have not been studied in much detail in the literature.

To describe the results, for a given $\lambda \in \mathbb{R}$, let $\mathcal{E}=\mathcal{E}_{\lambda}^{m, \alpha}(M)$ be the moduli space of Einstein metrics on $M$, satisfying (1-1), which are $C^{m, \alpha}$ smooth up to $\partial M$; here $m \geq 3$ and $\alpha \in(0,1)$. By definition, $\mathcal{E}$ is the space of all such metrics satisfying (1-1), modulo the action of the group $\mathcal{D}_{1}=\mathcal{D}_{1}^{m+1, \alpha}$ of $C^{m+1, \alpha}$ diffeomorphisms of $M$ equal to the identity on $\partial M$.

The first main result of the paper is the following theorem.
Theorem 1.1 Suppose $\pi_{1}(M, \partial M)=0$. Then for any $\lambda \in \mathbb{R}$, the moduli space $\mathcal{E}$, if non-empty, is an infinite dimensional $C^{\infty}$ smooth Banach manifold.

Theorem 1.1 also holds in the $C^{\infty}$ context: the space $\mathcal{E}^{\infty}$ of $C^{\infty}$ Einstein metrics on $M$ is a smooth Fréchet manifold.

The topological condition $\pi_{1}(M, \partial M)=0$ means that $\partial M$ is connected, and the inclusion map $\iota: \partial M \rightarrow M$ induces a surjection
$$\pi_{1}(\partial M) \rightarrow \pi_{1}(M) \rightarrow 0 .$$
It is an open question whether Theorem 1.1 holds without this topological condition. The method of proof, via the implicit function theorem, fails without it, cf Remark 2.7. On the other hand, Theorem 1.1 holds at least for generic Einstein metrics, without the $\pi_{1}$ condition, if $\partial M$ is connected.

A consequence of the proof of Theorem 1.1 is that the moduli space $\mathcal{E}$ is "unobstructed", in that any infinitesimal Einstein deformation $h$ of $(M, g)$ is tangent to curve in $\mathcal{E}$, ie all infinitesimal deformations may be integrated to curves. This is in strong contrast to the situation on compact manifolds without boundary, where a well-known result of Koiso [12] gives examples where the Einstein moduli space is obstructed, cf also [5].

Theorem 1.1 does not involve the specification of any boundary values of the metric $g$. Boundary values are given by natural boundary maps to the space of symmetric bilinear forms $S_{2}(\partial M)$ on $\partial M$. For the Dirichlet problem, one has the $C^{\infty}$ smooth Dirichlet boundary map
$$\Pi_{D}: \mathcal{E}^{m, \alpha} \rightarrow \operatorname{Met}^{m, \alpha}(\partial M), \Pi_{D}[g]=\gamma=\left.g\right|_{T(\partial M)},$$
where $\operatorname{Met}^{m, \alpha}(\partial M)$ is the Banach space of $C^{m, \alpha}$ metrics on $\partial M$. However, $\Pi_{D}$ does not have good local properties, in that $\Pi_{D}$ is never Fredholm. For instance, when $m<\infty, D \Pi$ always has an infinite dimensional cokernel, so that the variety
$\mathcal{B}=\Pi\left(\mathcal{E}^{m, \alpha}\right)$ has infinite codimension in $\operatorname{Met}^{m, \alpha}(\partial M)$. This is a consequence of the scalar or Hamiltonian constraint on the boundary metric $\gamma$ induced by the Einstein metric $(M, g)$ :
$$|A|^{2}-H^{2}+s_{\gamma}-(n-1) \lambda=0 .$$
Here $A$ is the second fundamental form of $\partial M$ in $(M, g), H=\operatorname{tr} A$ is the mean curvature and $s_{\gamma}$ is the scalar curvature of $(\partial M, \gamma)$. For $g \in \mathbb{E}^{m, \alpha}$, one has $A, H \in$ $S_{2}^{m-1, \alpha}(\partial M)$, so that (1-4) gives $s_{\gamma} \in C^{m-1, \alpha}(\partial M)$. However, a generic $C^{m, \alpha}$ metric $\gamma$ on $\partial M$ has scalar curvature $s_{\gamma}$ in $C^{m-2, \alpha}$; in fact the space of $C^{m, \alpha}$ metrics $\gamma$ on $\partial M$ for which $s_{\gamma} \in C^{m-1, \alpha}(\partial M)$ is of infinite codimension. Of course the simplest instance of this relation is Gauss' Theorema Egregium, $K=\frac{1}{2} s_{\gamma}=\operatorname{det} A$, for surfaces in $\mathbb{R}^{3}$.

Similarly, there are situations where the linearization $D \Pi$ has infinite dimensional kernel; for example this is the case whenever the second fundamental form $A$ of $\partial M$ in $M$ vanishes on an open set in $\partial M$. These remarks show that the Dirichlet problem for the Einstein equations is not a well-posed elliptic boundary value problem. The discussion above also holds for the natural Neumann boundary map, taking $g \in \mathcal{E}$ to its second fundamental form $A$ on $\partial M$.

These failures of the Fredholm property above are closely related to the fact that Einstein metrics are invariant under the full diffeomorphism group $\mathcal{D}$ of $\bar{M}$, which is much larger than the restricted group $\mathcal{D}_{1}$. It is also closely related to loss-of-derivative issues in the isometric embedding of manifolds in $\mathbb{R}^{N}$, cf Nash [17] and Nirenberg [18].

On the other hand, there are Fredholm boundary maps of mixed (Dirichlet-Neumann) type. There are several classes of these, but perhaps the most natural is given by the following result. Let $\mathcal{C}^{m, \alpha}(\partial M)$ be the space of pointwise conformal classes of $C^{m, \alpha}$ metrics on $\partial M$, with $[\gamma]$ denoting the conformal class of $\gamma$.

Theorem 1.2 The boundary map
$$\begin{aligned}
\widetilde{\Pi}_{D}: \mathcal{E}^{m, \alpha} & \rightarrow \mathcal{C}^{m, \alpha}(\partial M) \times C^{m-1, \alpha}(\partial M) \\
& \widetilde{\Pi}_{D}(g)=([\gamma], H)
\end{aligned}$$
is $C^{\infty}$ smooth and Fredholm, of Fredholm index 0.
In particular, the image $\widetilde{\mathcal{B}}=\widetilde{\Pi}_{D}\left(\mathcal{E}^{m, \alpha}\right)$ is a variety of finite codimension in $\mathcal{C}^{m, \alpha}(\partial M) \times C^{m-1, \alpha}(\partial M)$. It is an interesting open problem to relate this image with the image of the usual (non-Fredholm) Dirichlet boundary map (1-3). Thus, one may fix the conformal class $[\gamma]$ and vary the mean curvature $H$. It would be interesting
to understand the resulting space of metrics $\widetilde{\mathcal{B}} \cap[\gamma]$ within $[\gamma]$ that are obtained in this way.

The results above generalize easily to "exterior" boundary value problems. In this context, $(M, g)$ is then a complete, non-compact manifold, with a compact (interior) boundary. Such Einstein metrics necessarily have non-positive scalar curvature, and the simplest asymptotic behaviors are asymptotically (locally) hyperbolic, when $s<0$, and asymptotically (locally) Euclidean or flat. The former case has been extensively studied elsewhere, (cf the author's [2] for example), in the case $\partial M=\varnothing$, so we concentrate here on the asymptotically flat case.

Suppose then $M$ is a manifold with a compact non-empty boundary $\partial M$ and a finite collection of asymptotically locally flat ends; such ends are metrically asymptotic to a flat metric on the space $\left(\mathbb{R}^{m} \times T^{n+1-m}\right) / \Gamma$, where $T^{k}$ is the $k$-torus, $3 \leq m \leq n+1$ and $\Gamma$ is a finite group of Euclidean isometries.

Theorem 1.3 The results above, ie Theorem 1.1 and Theorem 1.2, hold for the moduli space $\mathcal{E}$ of Ricci-flat, locally asymptotically flat metrics on $M$.

A more precise statement of Theorem 1.3, in particular regarding the assumptions on the asymptotic behavior of the metrics, is given in Section 4, cf Theorem 4.2.

The results above also hold for the Einstein equations coupled to other fields, for example scalar fields, sigma models (harmonic maps), etc. These are discussed in detail in Section 5. In fact the method of proof is quite general and should apply to many geometric variational problems.

Theorem 1.1 and Theorem 1.2 show that one has reasonably good local behavior associated with the moduli space $\mathcal{E}$ of Einstein metrics on $M$. It is then of basic interest to understand more global issues associated with $\mathcal{E}$; for example, under what conditions is the boundary map $\widetilde{\Pi}_{D}$ in (1-5) proper? We hope to address some of these questions in the future.

I would like to thank the referee for several constructive comments leading to improvements in the paper. This work was partially supported by NSF Grant DMS 0604735.

\section*{2 The moduli space $\mathcal{E}$}

Theorem 1.1 is proved via application of the implicit function theorem, (ie the regular value theorem). To do this, one needs to choose suitable function spaces and make
a choice of gauge in order to break the diffeomorphism invariance of the Einstein equations. As function space, we consider the Banach space
$$\operatorname{Met}(M)=\operatorname{Met}^{m, \alpha}(M)$$
of metrics on $M$ which are $C^{m, \alpha}$ smooth up to $\partial M$. Here $m$ is any fixed integer with $m \geq 2$ and $\alpha \in(0,1)$. In the following, the smoothness index $(m, \alpha)$ will often be suppressed from the notation unless it is important to indicate it. Let
$$\mathbb{E}=\mathbb{E}(M)$$
be the space of Einstein metrics on $M$,
$$\operatorname{Ric}_{g}=\lambda g,$$
viewed as a subset of $\operatorname{Met}(M)$, for any fixed $\lambda \in \mathbb{R}$. The Einstein operator $E$ is a $\left(C^{\infty}\right)$ smooth map
$$\begin{gathered}
E: \operatorname{Met}(M) \rightarrow S_{2}(M), \\
E(g)=\operatorname{Ric}_{g}-\lambda g,
\end{gathered}$$
or more precisely $E: \operatorname{Met}^{m, \alpha}(M) \rightarrow S_{2}^{m-2, \alpha}(M)$, where $S_{2}^{m-2, \alpha}(M)$ is the space of $C^{m-2, \alpha}$ symmetric bilinear forms on $M$. Thus
$$\mathbb{E}=E^{-1}(0) .$$
Let $\widetilde{g} \in \mathbb{E}$ be a fixed but arbitrary background Einstein metric. A number of different gauge choices have been used to study the Einstein equations (2-3) near $\widetilde{g}$. For the purposes of this work, the simplest and most natural choice is the Bianchi-gauged Einstein operator, given by
$$\begin{gathered}
\Phi \widetilde{g}: \operatorname{Met}(M) \rightarrow S_{2}(M), \\
\Phi \widetilde{g}(g)=\operatorname{Ric}_{g}-\lambda g+\delta_{g}^{*} \beta \widetilde{g}(g),
\end{gathered}$$
where $\left(\delta^{*} X\right)(A, B)=\frac{1}{2}\left(\left\langle\nabla_{A} X, B\right\rangle+\left\langle\nabla_{B} X, A\right\rangle\right)$ and $\delta X=-\operatorname{tr} \delta^{*} X$ is the divergence and $\beta_{\widetilde{g}}(g)=\delta_{\widetilde{g}} g+\frac{1}{2} d \operatorname{tr}_{\widetilde{g}} g$ is the Bianchi operator with respect to $\widetilde{g}$. Although $\Phi_{\widetilde{g}}$ is defined for all $g \in \operatorname{Met}(M)$, we will only consider it acting on $g$ near $\widetilde{g}$.

Clearly $g$ is Einstein if $\Phi \widetilde{g}(g)=0$ and $\beta \widetilde{g}(g)=0$, so that $g$ is in the Bianchi-free gauge with respect to $\widetilde{g}$. Using standard formulas for the linearization of the Ricci and scalar curvatures, cf [5] for instance, one finds that the linearization of $\Phi$ at $\widetilde{g}=g$ is given by
$$L(h)=2(D \Phi \widetilde{g})_{g}(h)=D^{*} D h-2 R h$$
where the covariant derivatives and curvature are taken with respect to $g$. Similarly, the linearization $E^{\prime}=L_{E}$ of the Einstein operator $E$ is given by
$$2 L_{E}(h)=L(h)-2 \delta^{*} \beta(h) .$$
Note that the operator $L$ is formally self-adjoint. While $L$ is elliptic, $L_{E}$ is not; this is the reason for choosing a gauge. The zero-set of $\Phi \widetilde{g}$ near $\widetilde{g}$,
$$Z=\left\{g: \Phi_{\widetilde{g}}=0\right\}$$
consists of metrics $g \in \operatorname{Met}(M)$ satisfying the Ricci soliton equation
$$\operatorname{Ric}_{g}-\lambda g+\delta_{g}^{*} \beta \widetilde{g}(g)=0$$
One needs to choose boundary conditions on $\partial M$ to obtain a well-defined elliptic boundary value problem for the operator $\Phi$ on $M$. This will be done in detail in Section 3. For now, given $\widetilde{g}$, consider simply the Banach space
$$\operatorname{Met}_{C}(M)=\operatorname{Met}_{C}^{m, \alpha}(M)=\left\{g \in \operatorname{Met}^{m, \alpha}(M): \beta \widetilde{g}(g)=0 \text { on } \partial M\right\} .$$
Clearly the map
$$\Phi: \operatorname{Met}_{C}(M) \rightarrow S^{2}(M),$$
is $C^{\infty}$ smooth.
Let $Z_{C}$ be the space of metrics $g \in \operatorname{Met}_{C}(M)$ satisfying $\Phi \widetilde{g}(g)=0$, and let
$$\mathbb{E}_{C} \subset Z_{C}$$
be the subset of Einstein metrics $g, \operatorname{Ric}_{g}=\lambda g$ in $Z_{C}$. To justify the use of $\Phi$, one needs to show that the opposite inclusion to (2-10) holds, so that $\mathbb{E}_{C}=Z_{C}$. Let $\chi_{1}^{k, \alpha}$ be the space of $C^{k, \alpha}$ vector fields on $M$ which vanish on $\partial M$. One then has
$$V=\beta \widetilde{g}(g) \in \chi_{1}^{m-1, \alpha}$$
and wants to show that $\delta^{*} V=0$. (Here and below we identify vector fields and 1 -forms via the metric $g$ ). This will require several Lemmas, which will also be of importance later.

Lemma 2.1 For $g$ in $\operatorname{Met}^{m, \alpha}(M)$, one has
$$T_{g} \operatorname{Met}^{m-2, \alpha}(M) \simeq S_{2}^{m-2, \alpha}(M)=\operatorname{Ker} \delta \oplus \operatorname{Im} \delta^{*},$$
where $\delta^{*}$ acts on $\chi_{1}^{m-1, \alpha}$.

Proof Given $h \in S_{2}^{m-2, \alpha}(M)$, consider the equation $\delta \delta^{*} X=\delta h \in C^{m-3, \alpha}$. If $X=0$ at $\partial M$, this has a unique solution $X$ with $X \in \chi_{1}^{m-1, \alpha}$, by elliptic regularity (Gilbarg-Trudinger [8] and Morrey [16]). Setting $\pi=h-\delta^{*} X$ gives the splitting (2-11). \(\square\)

Lemma 2.2 For $\widetilde{g} \in \mathbb{E}^{m, \alpha}$ and $g$ in $\operatorname{Met}^{m, \alpha}$ close to $\widetilde{g}$, one has
$$T_{g} \operatorname{Met}^{m-2, \alpha}(M) \simeq S_{2}^{m-2, \alpha}(M)=\operatorname{Ker} \beta \oplus \operatorname{Im} \delta^{*}$$

Proof By the same argument as in Lemma 2.1, it suffices to prove that the operator $\beta \delta^{*}: \chi_{1}^{m-1, \alpha} \rightarrow \Omega^{1}$ is an isomorphism, where $\Omega^{1}$ is the space of $C^{m-3, \alpha} 1$-forms on $M$. Since this is an open condition, it suffices to prove this when $g=\widetilde{g}$ is Einstein. A standard Weitzenbock formula gives
$$2 \beta \delta^{*} X=D^{*} D X-\operatorname{Ric}(X)=D^{*} D X-\lambda X .$$
Hence, if $\lambda \leq 0, \beta \delta^{*}$ is a positive operator and it follows easily that $\beta \delta^{*}$ is an isomorphism, (as in the proof of Lemma 2.1).
When $\lambda>0$, this requires some further work. First, note that $\beta$ itself is surjective. To see this, suppose $Y$ is a 1 -form (or vector field) orthogonal to $\operatorname{Im} \beta$. Then
$$0=\int_{M}\langle\beta(h), Y\rangle=\int_{M}\left\langle h, \beta^{*} Y\right\rangle-\int_{\partial M}\left[h(N, Y)-\frac{1}{2} \operatorname{tr} h\langle Y, N\rangle\right] .$$
Since $h$ is arbitrary, this implies $\beta^{*} Y=\delta^{*} Y+\frac{1}{2} \delta Y g=0$, and hence, by taking the trace of this equation, $\delta^{*} Y=0$. The boundary term also vanishes, which implies $Y=0$ at $\partial M$. Thus, $Y$ is a Killing field vanishing on $\partial M$, and hence $Y=0$, which proves the claim.
To prove that $\beta \delta^{*}$ is surjective, it then suffices to show that for any $h \in S_{2}^{m-2, \alpha}(M)$, there exists $X$ such that $\beta \delta^{*}(X)=\beta(h)$. Via (2-11), write $h=k+\delta^{*} Y$ with $\delta k=0$. Then $\beta(h)=\frac{1}{2} d \operatorname{tr} k+\beta \delta^{*}(Y)$. This shows that it suffices to prove $\beta \delta^{*}$ is surjective onto exact 1 -forms $d f$.

Thus, suppose there exists $f$ such that $d f \perp \operatorname{Im} \beta \delta^{*}=\operatorname{Im}\left(D^{*} D-\lambda I\right)$. Arguing just as in (2-13), it follows that $d \Delta f-\lambda(d f)=0$ on $M$, with boundary condition $d f=0$ at $\partial M$. Hence, $\Delta f+\lambda f=$ const , with $f=$ const and $N(f)=0$ at $\partial M$. It then follows from unique continuation for Laplace-type operators that $f=$ const on $M$, and hence $\beta \delta^{*}$ is surjective.

To see that $\beta \delta^{*}=D^{*} D-\lambda I$ is injective, the family $D^{*} D-t \lambda I$ for $t \in[0,1]$, with boundary condition $X=0$ on $\partial M$, is a curve of elliptic boundary value problems. Since the index is 0 when $t=0$, it follows that the index is also 0 when $t=1$, ie $\beta \delta^{*}$ has index 0 on $\chi_{1}$, which proves the injectivity. This completes the proof. \(\square\)

Corollary 2.3 Any metric $g \in Z_{C}$ near $\widetilde{g}$ is necessarily Einstein, with $\operatorname{Ric}_{g}=\lambda g$, and in Bianchi gauge with respect to $\widetilde{g}$, ie
$$\beta \widetilde{g}(g)=0$$
Proof Since $g \in Z_{C}$, one has $\Phi(g)=0$, ie
$$\operatorname{Ric}_{g}-\lambda g+\delta_{g}^{*} \beta \widetilde{g}(g)=0$$
The Bianchi identity $\beta_{g}\left(\operatorname{Ric}_{g}\right)=0$ implies
$$\beta_{g}\left(\delta_{g}^{*}(V)\right)=0,$$
where $V=\beta \widetilde{g}(g)$. By the constraint (2-9), the vector field $V$ vanishes on $\partial M$, so that $V \in \chi_{1}^{m-1, \alpha}$. It then follows from Lemma 2.2 that
$$\delta^{*} V=0,$$
so that $g$ is Einstein. To prove the second statement, (2-15) implies that $V$ is a Killing field on $(M, g)$ with $V=0$ at $\partial M$ by (2-9). It is then standard that $V=0$ on $M$ so that (2-14) holds. \(\square\)

By linearizing, the same proof shows that the infinitesimal version of Corollary 2.3 holds. Thus, if $k$ is an infinitesimal deformation of $g \in Z_{C}$, ie $k \in \operatorname{Ker} D \Phi$ and if $\beta \widetilde{g}(g)=0$, (for example $\widetilde{g}=g$ ), then $k$ is an infinitesimal Einstein deformation, ie the variation of $g$ in the direction $k$ preserves (2-3) to first order and $\beta(k)=0$. The proof is left to the reader.

As mentioned above, Theorem 1.1 is proved via the implicit function theorem in Banach spaces. To set the stage for this, the natural or geometric Cauchy data for the Einstein equations (2-3) on $M$ at $\partial M$ consist of the pair $(\gamma, A)$. If $k$ is an infinitesimal Einstein deformation of $(M, g)$, so that $L_{E}(k)=0$, then the induced variation of the Cauchy data on $\partial M$ is given by
$$k^{T} \text { and }\left(A_{k}^{\prime}\right)^{T},$$
where $A_{k}^{\prime}=\frac{1}{2}\left(\mathcal{L}_{N} g\right)^{\prime}$ is the variation of $A$ in the direction $k$, given by
$$2 A_{k}^{\prime}=\nabla_{N} k+2 A \circ k-2 \delta^{*}\left(k(N)^{T}\right)-\delta^{*}\left(k_{00} N\right),$$
where we have used the formula $\mathcal{L}_{N} k=\nabla_{N} k+2 A \circ k$.
It is proved in Anderson-Herzlich [3] that an Einstein metric $g$ is uniquely determined in a neighborhood of $\partial M$, up to isometry, by the Cauchy data $(\gamma, A)$. This also holds, with the same proof, for the linearized Einstein equations and this linearized unique continuation result will be needed in the proof of Theorem 1.1.

Proposition 2.4 (Anderson-Herzlich [3]) Given any $(M, g) \in \mathbb{E}=\mathbb{E}^{m, \alpha}, m \geq 3$, let $k$ be any infinitesimal Einstein deformation of $g$ such that
$$k^{T}=0 \text { and }\left(A_{k}^{\prime}\right)^{T}=0,$$
at $\partial M$. Then there exists a $C^{m+1, \alpha}$ vector field $Z$, defined in a neighborhood of $V$ of $\partial M$, with $Z=0$ on $\partial M$, such that on $V$,
$$k=\delta^{*} Z .$$
We note that the boundary conditions (2-17) are invariant under infinitesimal gauge transformations $k \rightarrow k+\delta^{*} Z$, with $Z=0$ on $\partial M$. The following result is the main part of the proof of Theorem 1.1.

Proposition 2.5 Suppose $\pi_{1}(M, \partial M)=0$. Then at any $\widetilde{g} \in \mathbb{E}^{m, \alpha}, m \geq 3$, the map $\Phi=\Phi \widetilde{g}$ is a submersion on $\operatorname{Met}_{C}^{m, \alpha}(M)$. Thus, the linearized operator $L=2 D \Phi$ :
$$L: T_{\widetilde{g}} \operatorname{Met}_{C}(M) \rightarrow S_{2}(M)$$
is surjective, and the kernel of $L$ splits in $T_{\widetilde{g}} \operatorname{Met}_{C}(M)$.

Proof The operator $L$ is elliptic on $T_{\widetilde{g}} \operatorname{Met}_{C}(M)$, and so Fredholm. (More precisely, one can augment the constraint (2-9) with further boundary conditions to obtain an elliptic boundary value problem; this is discussed in detail in Section 3.)

In particular, $\operatorname{Im}(L)$ is closed and has a closed complement in $S_{2}(M)$. If $L$ is not surjective, then there exists a non-zero $k \in T_{\widetilde{g}} \operatorname{Met}(M)=S_{2}(M)$ such that, for all $h \in T_{\widetilde{g}} \operatorname{Met}_{C}(M)$,
$$\int_{M}\langle L(h), k\rangle d V_{\widetilde{g}}=0 .$$
The idea of the proof is to show that ( $2-20$ ) implies $k$ is an infinitesimal Einstein deformation, so $L_{E}(k)=0$, (in transverse-traceless gauge), and satisfying the boundary conditions (2-17), so that the unique continuation property in Proposition 2.4 applies. Once this is established, the proof follows by a simple global argument, using the condition on $\pi_{1}$. In the following, we set $\widetilde{g}=g$ and drop the volume forms from the notation; $N$ denotes the unit outward normal at $\partial M$.

To begin, integrating (2-20) by parts, one obtains
$$0=\int_{M}\langle L(h), k\rangle=\int_{M}\langle h, L(k)\rangle+\int_{\partial M} D(h, k),$$
where the boundary pairing $D(h, k)$ has the form
$$D(h, k)=\left\langle h, \nabla_{N} k\right\rangle-\left\langle k, \nabla_{N} h\right\rangle .$$
Since $h$ is arbitrary in the interior, the bulk integral and the boundary integral on the right in (2-21) vanish separately, and hence
$$L(k)=0 .$$
Next, observe that (2-20) implies that
$$\delta k=0 \text { on } M,$$
so that $k$ is in divergence-free gauge on $M$. To see this, (2-7) implies that $L\left(\delta^{*} X\right)=$ $\delta^{*} Y$, where $Y=2 \beta \delta^{*} X$. Then
$$0=\int_{M}\left\langle L\left(\delta^{*} X\right), k\right\rangle=\int_{M}\langle Y, \delta k\rangle+\int_{\partial M} k(Y, N) .$$
For $h=\delta^{*} X$, the Bianchi constraint (2-9) gives exactly $Y=0$ at $\partial M$. By Lemma 2.2, $Y$ is arbitrary in the interior of $M$, which thus gives (2-24).

The boundary integral in (2-21) vanishes for all $h \in T_{g} \operatorname{Met}_{C}(M)$, ie all $h$ satisfying the linearized constraint (2-9). Written out in tangential and normal components, this requires
$$\begin{aligned}
\left(\nabla_{N} h\right)(N)^{T} & =\delta^{T} h^{T}-\alpha(h(N))+\frac{1}{2} d^{T} \operatorname{tr} h \\
N\left(h_{00}\right) & =\delta^{T}\left(h(N)^{T}\right)-h_{00} H+\langle A, h\rangle+\frac{1}{2} N(\operatorname{tr} h)
\end{aligned}$$
where $\alpha(h(N))=A(h(N))+H h(N)^{T}, h_{00}=h(N, N)$ and $N\left(h_{00}\right)=\left(\nabla_{N} h\right)(N, N)$.
We first use various test-forms $h$ to obtain restrictions on $k$ at $\partial M$. Thus, suppose first $h=0$ at $\partial M$. The constraints (2-25)-(2-26) then require that
$$\left(\nabla_{N} h\right)(N)^{T}=0 \text { and } N\left(h_{00}\right)=\left\langle\nabla_{N} h, \gamma\right\rangle,$$
where we have used the fact that $\operatorname{tr} h=h_{00}+\operatorname{tr}_{\gamma} h$. For all such $h$, (2-21)-(2-22) gives
$$\int_{\partial M}\left\langle\nabla_{N} h, k\right\rangle=0,$$
and hence
$$\int_{\partial M} N\left(h_{00}\right) k_{00}+\frac{1}{n}\left\langle\nabla_{N} h, \gamma\right\rangle\langle\gamma, k\rangle+\left\langle\left(\nabla_{N} h\right)_{0}^{T}, k_{0}^{T}\right\rangle=0,$$
where $k_{0}^{T}$ is the trace-free part of $k^{T}$. This implies that
$$k^{T}=\phi \gamma, \text { and } k_{00}=-\frac{1}{n} t r_{\gamma} k=-\phi,$$
for some function $\phi$.
Next, set $h^{T}=h_{00}=0$ with $h(N)^{T}$ chosen arbitrarily, and similarly $\nabla_{N} h=0$ except for the two relations $\left(\nabla_{N} h\right)(N)^{T}=-\alpha\left(h(N)^{T}\right)$ and $N(\operatorname{tr} h)=-2 \delta^{T}\left(h(N)^{T}\right)$. The constraints are then satisfied and via (2-27), one has
$$\int_{\partial M}\left\langle\nabla_{N} h, k\right\rangle=-2 \int_{\partial M}\left\langle\alpha(h(N)), k(N)^{T}\right\rangle-2 \frac{n-1}{n+1} \phi \delta^{T}\left(h(N)^{T}\right),$$
while
$$\int_{\partial M}\left\langle\nabla_{N} k, h\right\rangle=2 \int_{\partial M}\left\langle h(N)^{T},\left(\nabla_{N} k\right)(N)^{T}\right\rangle .$$
Now by (2-24) one has, (as in (2-25)),
$$\begin{aligned}
\left(\nabla_{N} k\right)(N, T) & =-\left(\nabla_{e_{i}} k\right)\left(e_{i}, T\right) \\
& =-e_{i}\left(k\left(e_{i}, T\right)\right)+k\left(\nabla_{e_{i}} e_{i}, T\right)+k\left(e_{i}, \nabla_{e_{i}} T\right) \\
& =-\langle d \phi, T\rangle-\langle\alpha(k(N)), T\rangle,
\end{aligned}$$
so that
$$\left(\nabla_{N} k\right)(N)^{T}=-d^{T} \phi-\alpha(k(N)) .$$
Note that $\alpha$ is symmetric: $\langle\alpha(h(N)), k(N)\rangle=\langle\alpha(k(N)), h(N)\rangle$. It then follows from the two equations above and the divergence theorem that
$$\phi=\text { const. }$$
We note that, analogous to (2-26), (2-24) together with (2-27) gives
$$N\left(k_{00}\right)=\delta^{T}\left(k(N)^{T}\right)-k_{00} H+\langle k, A\rangle=\delta^{T}\left(k(N)^{T}\right)+2 H \phi .$$
Next, suppose $h=0$ except for $h_{00}$, which is chosen arbitrarily, and similarly $\nabla_{N} h=0$ except for the component $\nabla_{N} h(N)^{T}$. Then (2-25) and (2-26) require
$$\begin{aligned}
N\left(h_{00}\right) & =-H h_{00}, \\
\left(\nabla_{N} h\right)(N)^{T} & =\frac{1}{2} d^{T} h_{00} .
\end{aligned}$$

This gives
$$\begin{aligned}
\int_{\partial M}\left\langle\nabla_{N} h, k\right\rangle & =2 \int_{\partial M}\left\langle\left(\nabla_{N} h\right)^{T}, k(N)^{T}\right\rangle-h_{00} k_{00} H \\
& =\int_{\partial M}\left\langle d^{T} h_{00}, k(N)^{T}\right\rangle-h_{00} k_{00} H \\
& =\int_{\partial M} h_{00} \delta^{T}\left(k(N)^{T}\right)-h_{00} k_{00} H,
\end{aligned}$$
while
$$\int_{\partial M}\left\langle h, \nabla_{N} k\right\rangle=\int_{\partial M} h_{00} N\left(k_{00}\right) .$$
Hence
$$N\left(k_{00}\right)=\delta^{T}\left(k(N)^{T}\right)-k_{00} H .$$
Via (2-30) and (2-27), this implies that
$$H \phi=0,$$
so that $\phi \equiv 0$ unless $H \equiv 0$.
Finally, set $h^{T}=f \gamma, h_{00}=-\frac{n-2}{2} f$ with the rest of $h$ set to 0. Then setting $N\left(h_{00}\right)=n f H$ with the rest of $\nabla_{N} h$ set to 0 solves the constraints (2-25)-(2-26), and (2-21)-(2-22) together with (2-27) and (2-32) then gives, since $f$ is arbitrary,
$$\left\langle\nabla_{N} k, \gamma\right\rangle=\frac{n-2}{2} N\left(k_{00}\right),$$
or equivalently
$$N(\operatorname{tr} k)=\frac{n}{2} N\left(k_{00}\right) .$$
We now analyse the boundary term in (2-21) in general, using the information obtained above. Thus, expand the inner products in (2-33) into tangential, mixed and normal components. Using (2-27), one has $\left\langle\nabla_{N} h, k\right\rangle=2\left\langle\left(\nabla_{N} h\right)(N)^{T}, k(N)^{T}\right\rangle$, since the 00 and trace components cancel by (2-26) and (2-29). Using the constraint (2-25), together with the fact that, modulo divergence terms, $\left\langle\delta^{T} h^{T}, k(N)^{T}\right\rangle=\left\langle h^{T},\left(\delta^{T}\right)^{*} k(N)^{T}\right\rangle=$ $\left\langle h^{T}, \delta^{*}\left(k(N)^{T}\right)\right\rangle$, one has
$$\begin{aligned}
\int_{\partial M}\left\langle\nabla_{N} h, k\right\rangle= & \int_{\partial M} 2\left\langle h^{T}, \delta^{*}\left(k(N)^{T}\right)\right\rangle+\delta^{T}\left(k(N)^{T}\right) \operatorname{tr} h-2\langle\alpha(h(N)), k(N)\rangle \\
= & \int_{\partial M} 2\left\langle h^{T}, \delta^{*}\left(k(N)^{T}\right)\right\rangle+\delta^{T}\left(k(N)^{T}\right)\left\langle h^{T}, \gamma\right\rangle+\delta^{T}\left(k(N)^{T}\right) h_{00} \\
& -2\langle\alpha(h(N)), k(N)\rangle
\end{aligned}$$

On the other hand, $\left\langle\nabla_{N} k, h\right\rangle=\left\langle\left(\nabla_{N} k\right)^{T}, h^{T}\right\rangle+2\left\langle\nabla_{N} k(N)^{T}, h(N)^{T}\right\rangle+N\left(k_{00}\right) h_{00}$. The middle term is computed in (2-28) and using (2-29), one has
$$\int\left\langle\nabla_{N} k, h\right\rangle=\left\langle\left(\nabla_{N} k\right)^{T}, h^{T}\right\rangle+N\left(k_{00}\right) h_{00}-2\langle\alpha(k(N)), h(N)\rangle .$$
Now take the difference of these terms. Recall that $\alpha$ is symmetric and from (2-16), $\left(\nabla_{N} k\right)^{T}-2 \delta^{*} k(N)^{T}=2\left(A_{k}^{\prime}\right)^{T}-2 A \circ k+k_{00} A$. Using also (2-31) and (2-32) then gives
$$\int_{\partial M}\left\langle 2\left(A_{k}^{\prime}\right)^{T}-\delta^{T}\left(k(N)^{T}\right) \gamma-3 \phi A, h^{T}\right\rangle=0 .$$
Since $h^{T}$ may be chosen arbitrarily consistent with the constraints, it follows that the integrand is 0. Taking the $\gamma$-trace, using (2-32), this gives
$$N(\operatorname{tr} k)-N\left(k_{00}\right)-(n-2) \delta^{T}\left(k(N)^{T}\right)=0,$$
which via (2-31) and (2-33) implies that
$$N(\operatorname{tr} k)=N\left(k_{00}\right)=0 .$$
Finally, we claim that
$$\operatorname{tr} k=(n-1) \phi=0 .$$
To see this, the trace of (2-23) gives
$$\Delta \operatorname{tr} k+\frac{s}{n+1} \operatorname{tr} k=0 .$$
Since $\operatorname{tr} k=(n-1) \phi=$ const and $N(\operatorname{tr} k)=0$ on $\partial M$, a standard unique continuation principle for the Laplacian implies that $\operatorname{tr} k=c$ on $M$. However, integrating the equation above over $M$ and using (2-35) implies $\operatorname{tr} k$ has mean value 0 on $M$, which gives (2-36).

The results above thus imply that
$$k^{T}=0,\left(A_{k}^{\prime}\right)^{T}=0, \text { on } \partial M \text {. }$$
In addition, $k$ is an infinitesimal Einstein deformation, since $\beta(k)=0$ and (2-23) holds. By the unique continuation property, (Proposition 2.4), one thus has
$$k=\delta^{*} Z,$$
in a neighborhood $U$ of $\partial M$, with $Z=0$ at $\partial M$. In the Lemma below, it will be shown, via the topological condition $\pi_{1}(M, \partial M)=0$, that $Z$ extends to a (global)
vector field on $M$ and (2-38) holds on all of $M$. Since $k$ is divergence-free by (2-24), one then has
$$\delta \delta^{*} Z=0,$$
globally on $M$, with $Z=0$ on $\partial M$. Pairing this with $Z$ and integrating over $M$, it follows from the divergence theorem that $\delta^{*} Z=0$ on $M$, and hence $k=0$. Thus the Lemma below will complete the proof of surjectivity.

Lemma 2.6 If $\pi_{1}(M, \partial M)=0$ and (2-38) holds in a neighborhood $U$ of $\partial M$, then there is a unique extension of the vector field $Z$ to $M$, also denoted $Z$, such that (2-38) holds on $M$.

Proof This result is an infinitesimal version of a well-known result on extension of isometries: namely, if $M$ and $M^{\prime}$ are complete, connected and simply connected analytic Riemannian manifolds, then every isometry between connected open sets of $M$ and $M^{\prime}$ extends uniquely to an isometry between $M$ and $M^{\prime}$, cf Kobayashi-Nomizu [11, Corollary 6.4].

In the current context, given the Einstein metric $g$ on $M$, let $g_{t}^{\prime}=g+t k$, so that for $t$ small, $g_{t}^{\prime}$ is a curve of global metrics on $M$. Since $g$ is analytic in harmonic or geodesic normal coordinates in the interior of $M$, so is the variation $k$, (by elliptic regularity), and hence $g_{t}^{\prime}$ is an analytic metric on $M$, for each $t$ small; $g_{t}^{\prime}$ is also analytic in $t$. The vector field $Z$ is defined and analytic in the region $U \subset M$, and the main issue is to extend $Z$ to a larger region. We do this via an analytic continuation argument following [11].

Thus, let $\phi_{t}$ be the flow of $Z$ defined in $U$, (or more precisely in $U^{\prime} \subset U$ for $t$ small), and let $g_{t}=\phi_{t}^{*} g$, so that $g_{t}$ is an analytic curve of metrics in $U$. By construction and (2-38), in $U$ one has
$$g_{t}^{\prime}=g_{t}+O\left(t^{2}\right) .$$
This estimate also holds for derivatives of $g_{t}$ and $g_{t}^{\prime}$ in local coordinates.
Now choose any $p \in U$ near the inner boundary of $U$ and consider the family of $g$-geodesics through $p$ and strictly within $U$. Working within $U$, the map $\phi_{t}$ sends this family to the family of $g_{t}$-geodesics through $p_{t}=\phi_{t}(p)$. Thus $\phi_{t}$ commutes with the exponential maps of the respective metrics, and so is determined by the derivative mapping $\left(\phi_{t}\right)_{*}$ taking $X \in T_{p} M$ to $X^{\prime}=\left(\phi_{t}\right)_{*} X \in T_{p_{t}} M$. On the other hand, by (2-39), the (global) $g_{t}^{\prime}$-geodesics based at $p_{t}$ agree to second order in $t$ with the family of $g_{t}$-geodesics through $p_{t}$.

In a full geodesically convex neighborhood $W$ of $p$ which extends past $U$, one then has a local analytic map $\phi_{t}^{\prime}$ defined, as above, by sending the $g$-geodesic with tangent
vector $X$ to the $g_{t}^{\prime}$-geodesic with tangent vector $\left(\phi_{t}\right)_{*} X$. Now take the derivative of this curve $\phi_{t}^{\prime}$ of mappings with respect to $t$ at $t=0$. This uniquely defines a vector field $Z$ in $U \cup W$, which, by construction, agrees with the original vector field $Z$ in $U \cap W$. This extension is analytic and hence (2-38) remains valid on $U \cup W$, ie one has a local analytic continuation of $Z$ preserving (2-38). This process may be repeated a finite number of times until all of $M$ is covered. The topological condition $\pi_{1}(M, \partial M)=0$ guarantees the path independence of these local analytic continuations; we refer to [11] for further details if needed. This completes the proof. \(\square\)

Having proved surjectivity, it is now essentially standard or formal that the kernel of $D \Phi_{g}$ splits, ie it admits a closed complement in $T_{g}$ Met $_{C}$. In more detail, it suffices to find a bounded linear projection $P$ mapping $T_{g} \operatorname{Met}_{C}(M)$ onto $\operatorname{Ker}\left(D \Phi_{g}\right)$. To do this, let $\operatorname{Met}_{C}^{0}(M) \subset \operatorname{Met}_{C}(M)$ be the subspace of metrics $g$ such that $\left.g\right|_{T(\partial M)}=$ $\left.\widetilde{g}\right|_{T(\partial M)}=\widetilde{\gamma}$. Choose a fixed smooth extension operator taking metrics $\gamma$ on $T(\partial M)$ into $\operatorname{Met}_{C}(M)$, and let $\operatorname{Met}_{C}^{1}(M)$ be the resulting space of metrics, so that
$$\operatorname{Met}_{C}(M)=\operatorname{Met}_{C}^{0}(M) \oplus \operatorname{Met}_{C}^{1}(M) .$$
Let $T$ and $T^{0}, T^{1}$ denote the corresponding tangent spaces at $\widetilde{g}$ and $L^{i}=\left.D \Phi\right|_{T^{i}}: T^{i} \rightarrow$ $S_{2}(M)$, for $i=1,2$. Then
$$\operatorname{Ker} D \Phi_{g}=\left\{\left(h, g_{\dot{\gamma}}\right) \in T^{0} \oplus T^{1}: L^{0}(h)+L^{1}\left(g_{\dot{\gamma}}\right)=0\right\} .$$
The operator $L$ is elliptic, so that $L^{0}$ is Fredholm on $T^{0}$. The image $\operatorname{Im}\left(L^{0}\right)$ thus has a finite dimensional complement $S, S_{2}(M)=\operatorname{Im}\left(L^{0}\right) \oplus S$. By (2-40), $\operatorname{Im}\left(L^{1}\right) \subset$ $\operatorname{Im}\left(L^{0}\right)$ and so $\operatorname{Im} L^{1} \subset \operatorname{Ker}\left(\pi_{S} L^{1}\right)$, where $\pi_{S}$ is orthogonal projection onto $S$. By the nondegeneracy property (2-20), $L^{1}$ maps onto $S$ and hence $\operatorname{Im} \pi_{S} L^{1}=S$. Viewing $S$ as a subspace of $T$, under the natural isomorphism $T \simeq S_{2}(M)$, this gives $T=\operatorname{Im}\left(\pi_{S} L^{1}\right) \oplus \operatorname{Ker}\left(\pi_{S} L^{1}\right)$, ie $\operatorname{Ker}\left(\pi_{S} L^{1}\right)$ splits, and so there is a bounded linear projection $P_{1}$ onto $\operatorname{Ker}\left(\pi_{S} L^{1}\right)$. The mapping $L+\pi_{S}$ is invertible and
$$P\left(h, g_{\dot{\gamma}}\right)=\left(\left(L^{0}+\pi_{S}\right)^{-1}\left(-L^{1} P_{1}\left(g_{\dot{\gamma}}\right)+\pi_{S} h\right), P_{1} g_{\dot{\gamma}}\right)$$
gives required bounded linear projection onto $\operatorname{Ker} D \Phi_{g}$. This completes the proof. □
Remark 2.7 There exist at least some examples of Einstein metrics ( $M, g$ ) having non-zero solutions of (2-20), so that $L$ on $T_{g} \operatorname{Met}_{C}(M)$ is not surjective in general; (of course such metrics must violate the condition $\pi_{1}(M, \partial M)=0$ ). As a simple example, let $M=I \times T^{n}, I=[0,1]$, and let $g$ be a flat product metric on $M$. Let $x^{\alpha}$ denote standard coordinates on $M$, with $x^{0}=t$ parameterizing $I$. Then the symmetric form
$$k=d t \cdot d x^{\alpha}=\delta^{*}\left(t \nabla x^{\alpha}\right)$$
is a divergence-free deformation of the flat metric satisfying (2-20), at least when $\alpha>0$. Note that this solution is pure gauge, $k=\delta^{*} Y$, with $Y=t \nabla x^{\alpha}$ vanishing at one boundary component but not at the other.

On the other hand, the condition on $\pi_{1}$ in Proposition 2.5 and Theorem 1.1 is used only to extend the locally defined solution $Z$ in (2-38) to a globally defined vector field on $M$ with $Z=0$ on $\partial M$. For example, $Z$ in (2-38) is unique modulo local Killing fields. Hence if $(M, g)$ has no local Killing fields, (which is the case for generic metrics), then Proposition 2.5, and Theorem 1.1, hold near $g$, provided $\partial M$ is connected.

Corollary 2.8 Under the assumptions of Proposition 2.5, if $\mathbb{E}$ is non-empty, then the local spaces $\mathbb{E}_{C}$ are infinite dimensional $C^{\infty}$ Banach manifolds, with
$$T_{\widetilde{g}} \mathbb{E}_{C}=\operatorname{Ker}(D \Phi \widetilde{g}) \widetilde{g}$$

Proof This is an immediate consequence Corollary 2.3, Proposition 2.5 and the implicit function theorem, (regular value theorem), in Banach spaces. \(\square\)

By Corollary 2.3, Einstein metrics in $\mathbb{E}_{C}$ satisfy the Bianchi gauge condition
$$\beta \widetilde{g}(g)=0$$
We need to show that (2-43) is actually a well-defined gauge condition. Let $\mathcal{D}_{1}=$ $\mathcal{D}_{1}^{m+1, \alpha}(M)$ be the group of $C^{m+1, \alpha}$ diffeomorphisms of $M$ which equal the identity on $\partial M$. The action of $\mathcal{D}_{1}$ on $\mathbb{E}$ is continuous and also free, since any isometry $\phi$ of a metric inducing the identity on $\partial M$ must itself be the identity. However, the action of $\mathcal{D}_{1}$ is not a priori smooth. Namely, as before let $\chi_{1}=\chi_{1}^{m+1, \alpha}$ denote the space of $C^{m+1, \alpha}$ vector fields $X$ on $\bar{M}$ with $X=0$ on $\partial M$, so that $\chi_{1}$ represents the tangent space of $\mathcal{D}_{1}$ at the identity. For $X \in \chi_{1}$ and $g \in \operatorname{Met}^{m, \alpha}(M)$, one has $\delta^{*} X=\frac{1}{2} \mathcal{L}_{X} g \in S_{2}^{m-1, \alpha}(M)$, but $\delta^{*} X \notin S_{2}^{m, \alpha}(M)$, so that there is a loss of one derivative.

For the same reasons, at a general metric $g \in \operatorname{Met}^{m, \alpha}$, the splitting (2-12) does not hold when $(m-2)$ is replaced by $m$. However, for Einstein metrics, this loss of regularity can be restored.

Lemma 2.9 For $g \in \mathbb{E}^{m, \alpha}$, the splittings (2-11) and (2-12) hold, and for any $X \in$ $\chi_{1}^{m+1, \alpha}, \delta^{*} X \in S_{2}^{m, \alpha}(M)$.

Proof By the proofs of (2-11) and (2-12), it suffices to prove the second statement. Since Einstein metrics are $C^{\infty}$ smooth, (in fact real-analytic), in harmonic coordinates in the interior, $\mathcal{L}_{X} g$ is $C^{m, \alpha}$ smooth in the interior of $M$. To see that $\mathcal{L}_{X} g$ is $C^{m, \alpha}$ smooth up to $\partial M$, recall that in suitable boundary harmonic coordinates, one has
$$\Delta_{g} g_{\alpha \beta}+Q_{\alpha \beta}(g, \partial g)=-2 \operatorname{Ric}_{\alpha \beta}=-2 \lambda g_{\alpha \beta},$$
cf Anderson et al [4] for the analysis of boundary regularity of Einstein metrics. Applying $X$ to this equation and commuting derivatives gives an equation for $\Delta_{g} X\left(g_{\alpha \beta}\right)$ with 0 boundary values, (since $X(g)=0$ on $\partial M$ ), and with right-hand side in $C^{m-2, \alpha}$. Elliptic boundary regularity results then imply that $X\left(g_{\alpha \beta}\right) \in C^{m, \alpha}$. From this, it is easy to see that $\mathcal{L}_{X} g$ is $C^{m, \alpha}$ smooth up to $\partial M$. \(\square\)

Next we pass from the infinitesimal splitting to its local version.

Lemma 2.10 Given any $\widetilde{g} \in \mathbb{E}^{m, \alpha}$ and $g \in \operatorname{Met}^{m, \alpha}(M)$ nearby $\widetilde{g}$, there exists a unique diffeomorphism $\phi \in \mathcal{D}_{1}^{m+1, \alpha}$, close to the identity, such that
$$\beta \widetilde{g}\left(\phi^{*} g\right)=0$$
In particular, $\phi^{*} g \in \operatorname{Met}_{C}^{m, \alpha}(M)$.

Proof Given Lemma 2.9, this can be derived from the slice theorem of Ebin [6], but we give a direct and simpler argument here. (Note that the Lemma does not assert the existence of a smooth slice). Let $\widetilde{g} \in \mathbb{E}$ and consider the map $F: \mathcal{D}_{1} \times \operatorname{Met}_{C}(M) \rightarrow$ $\operatorname{Met}(M)$ given by $F(\phi, g)=\phi^{*} g$. The proof of Lemma 2.9 above shows that $F$ is $C^{\infty}$ smooth at $\widetilde{g} ; F$ is linear in $g$ and smooth in the direction of $\mathcal{D}_{1}$ at $\widetilde{g}$ and hence smooth at $\widetilde{g}$.

Now suppose $g \in \operatorname{Met}(M)$ is close to $\widetilde{g}$. The linearization of $F$ at $(\mathrm{Id}, \widetilde{g})$ is the map $(X, h) \rightarrow \delta^{*} X+h$. By Lemma 2.9, given any $h$, there exists a unique vector field $X \in \chi_{1}^{m+1, \alpha}$ such that on $(M, \widetilde{g}), \beta\left(\delta^{*} X+h\right)=0$, or
$$\beta \delta^{*} X=-\beta(h),$$
with respect to $\widetilde{g}$. Hence, for $g$ sufficiently close to $\widetilde{g}$, there is a vector field $X$ such that
$$\left|\beta \widetilde{g}\left(g+\delta \stackrel{*}{g}^{*} X\right)\right| \ll \beta \widetilde{g}(g) .$$
It then follows from the inverse function theorem that there exists a unique diffeomorphism $\phi \in \mathcal{D}_{1}$ close to the identity such that (2-44) holds. \(\square\)

Lemma 2.10 implies that if $g \in \mathbb{E}$ is an Einstein metric near $\widetilde{g}$, then $g$ is isometric, by a unique diffeomorphism in $\mathcal{D}_{1}$, to an Einstein metric in $\mathbb{E}_{C}$. Hence (2-43) is a well-defined gauge condition and the spaces $\mathbb{E}_{C}$ are local slices for the action of $\mathcal{D}_{1}$ on $\mathbb{E}$.

We are now in position to complete the proof of Theorem 1.1.
Proof of Theorem 1.1 The space $\mathbb{E}=\mathbb{E}^{m, \alpha}(M) \subset \operatorname{Met}^{m, \alpha}(M)$ of all Einstein metrics on $M$ is invariant under the action of the group $\mathcal{D}_{1}=\mathcal{D}_{1}^{m+1, \alpha}$. The moduli space $\mathcal{E}=\mathcal{E}^{m, \alpha}(M)$ of $C^{m, \alpha}$ Einstein metrics on $M$ is the quotient
$$\mathcal{E}=\mathbb{E} / \mathcal{D}_{1} .$$
Two metrics $g_{1}$ and $g_{2}$ in $\mathcal{E}$ are equivalent if there exists $\phi \in \mathcal{D}_{1}$, such that $\phi^{*} g_{1}=g_{2}$.
The local spaces $\mathbb{E}_{C}$ are smooth Banach manifolds and depend smoothly on the background metric $\widetilde{g}$, since the gauge condition (2-43) varies smoothly with $\widetilde{g}$. As noted above, the action of $\mathcal{D}_{1}$ on $\mathbb{E}$ is free and by Lemma 2.9, the action is smooth. Hence the global space $\mathbb{E}$ is a smooth Banach manifold, as is the quotient $\mathcal{E}$. The local slices $\mathbb{E}_{C}$ represent local coordinate patches for $\mathcal{E}$.

It also follows immediately from the proof above that the spaces $\mathbb{E}^{\infty}$ and $\mathcal{E}^{\infty}=$ $\mathbb{E}^{\infty} / \mathcal{D}^{\infty}$ of $C^{\infty}$ Einstein metrics on $M$ are smooth Fréchet manifolds. \(\square\)

\section*{3 Elliptic boundary problems for the Einstein equations}

In this section, we consider elliptic boundary value problems for the Einstein equations. We begin with the Dirichlet boundary value problem. A metric $g$ on $M$ induces naturally a boundary metric
$$\gamma=g^{T}=\left.g\right|_{T(\partial M)}$$
on $\partial M$. One also has a normal part $\left.g^{N} \equiv g\right|_{N(\partial M)}$ of the metric $g$ at $\partial M$. In local coordinates $\left(x^{0}, x^{1}, \ldots, x^{n}\right)$ for $\partial M$ in $M$ with $x^{0}=0$ on $\partial M$, these are the $g_{0 \alpha}$ components of $g_{\alpha \beta}$, with $0 \leq \alpha \leq n$. Observe that the normal part of $g$ is a gauge term, in the sense that it transforms as a 1 -form under the action of diffeomorphisms of $M$ equal to the identity on $\partial M$.

Given the work in Section 2 and the relation (2-7) between $L_{E}$ with $L$, the most obvious boundary conditions to impose for the Dirichlet problem are:
$$\begin{aligned}
\left.g\right|_{T(\partial M)} & =\gamma \text { on } \partial M, \text { and } \\
\beta_{\widetilde{g}}(g) & =0 \text { on } \partial M .
\end{aligned}$$

Here $\gamma$ is an arbitrary Riemannian metric on $\partial M$, close to $\widetilde{\gamma}$ in $\operatorname{Met}^{m, \alpha}(\partial M)$. Note this is a formally determined set of boundary conditions; the Dirichlet condition (3-2) gives $\frac{1}{2} n(n+1)$ equations, while the Neumann-type boundary condition $(3-3)$ gives $n+1$ equations. In sum, this gives $\frac{1}{2}(n+1)(n+2)$ equations, which equals the number of components of the variable $g$ on $M$.

However, the operator $\Phi$ with the boundary conditions (3-2)-(3-3) does not form a well-defined elliptic boundary value problem. Geometrically, the reason for this is as follows. Metrics $g$ satisfying $\Phi(g)=0$ with the boundary condition (3-3) are Einstein, (cf Corollary 2.3), and so satisfy the Einstein constraint equations on $\partial M$. These are given by
$$\begin{aligned}
|A|^{2}-H^{2}+s_{\gamma}-(n-1) \lambda & =\left(\operatorname{Ric}_{g}-\lambda g\right)(N, N)=0, \\
\delta(A-H \gamma) & =\operatorname{Ric}(N, \cdot)=0 .
\end{aligned}$$
The scalar or Hamiltonian constraint (3-5) imposes a constraint on the regularity of the boundary metric $\gamma$ not captured by (3-2)-(3-3). Thus, if the boundary conditions (3-2)-(3-3) gave an elliptic system, (3-4) would hold for a space of boundary metrics $\gamma$ of finite codimension in $\operatorname{Met}^{m, \alpha}(\partial M)$, which, as discussed in the introduction, is impossible.

The discussion above implies there is no natural elliptic boundary value problem for the Einstein equations, associated with Dirichlet boundary values. To obtain an elliptic problem, one needs to add either gauge-dependent terms or terms depending on the extrinsic geometry of $\partial M$ in $(M, g)$. To maintain a determined boundary value problem, one then has to subtract part of the intrinsic Dirichlet boundary data on $\partial M$.

There are several ways to carry this out in practice, but we will concentrate on the following situations. Let $B$ be a $C^{m, \alpha}$ positive definite symmetric bilinear form on $\partial M$. In place of prescribing the boundary metric $g^{T}$ on $\partial M$, only $g^{T}$ modulo $B$ will be prescribed. Thus, let $\pi$ be the projection
$$\pi: \operatorname{Met}^{m, \alpha}(\partial M) \rightarrow \operatorname{Met}^{m, \alpha}(\partial M) / B, \pi(\gamma)=[\gamma]_{B}=[\gamma+f B]_{B} .$$
We allow here $B$ to depend on $\gamma$. For instance, if $B=\gamma$, then $[\gamma]_{B}=[\gamma]$ is the conformal class of $\gamma$.

The simplest gauge-dependent term one can add to (3-3) is the equation $g(\widetilde{N}, \widetilde{N})=$ $\gamma_{00}$, where $\widetilde{N}$ is the unit normal with respect to $\widetilde{g}$, while the simplest extrinsic geometric scalar is $H$, the mean curvature of $\partial M$ in $(M, g)$.

Proposition 3.1 The Bianchi-gauged Einstein operator $\Phi$ with boundary conditions either
$$\beta \widetilde{g}(g)=0,\left[g^{T}\right]_{B}=[\gamma]_{B}, \quad g(\widetilde{N}, \widetilde{N})=\gamma_{00} \text { at } \partial M,$$
or
$$\beta \widetilde{g}(g)=0,\left[g^{T}\right]_{B}=[\gamma]_{B}, \quad H_{g}=h \text { at } \partial M,$$
is an elliptic boundary value problem of Fredholm index 0.

Proof The proof is essentially a standard computation, following ideas initially introduced by Nash [17] in the isometric embedding problem, cf also Hamilton [9]. We will follow the method used by Schlenker in [19].

It suffices to show that the leading order part of the linearized operators forms an elliptic system. The leading order symbol of $L=D \Phi$ is given by
$$\sigma(L)=-|\xi|^{2} I,$$
where $I$ is the $N \times N$ identity matrix, with $N=(n+2)(n+1) / 2$ the dimension of the space of symmetric bilinear forms on $\mathbb{R}^{n+1}$. In the following, the subscript 0 represents the direction normal to $\partial M$ in $M$, and Latin indices run from 1 to $n$. The positive roots of (3-8) are $i|\xi|$, with multiplicity $N$.

Writing $\xi=\left(z, \xi_{i}\right)$, the symbols of the leading order terms in the boundary operators are given by:
$$\begin{aligned}
-2 i z h_{0 k}-2 i \sum \xi_{j} h_{j k}+i \xi_{k} \operatorname{tr} h & =0 \\
-2 i z h_{00}-2 i \sum \xi_{k} h_{0 k}+i z \operatorname{tr} h & =0 \\
h^{T} & =\left(\gamma^{\prime}\right)^{T} \bmod B, \\
h_{00} & =\omega \text { or }, H_{h}^{\prime}=\omega,
\end{aligned}$$
where $h$ is an $N \times N$ matrix. Then ellipticity requires that the operator defined by the boundary symbols above has trivial kernel when $z$ is set to the root $i|\xi|$. Carrying this out then gives the system
$$\begin{aligned}
2|\xi| h_{0 k}-2 i \sum \xi_{j} h_{j k}+i \xi_{k} \operatorname{tr} h & =0 \\
2|\xi| h_{00}-2 i \sum \xi_{k} h_{0 k}-|\xi| \operatorname{tr} h & =0 \\
h_{k l} & =\phi b_{k k} \delta_{k l} \\
h_{00} & =0 \text { or }, H_{h}^{\prime}=0
\end{aligned}$$
where without loss of generality we assume $B$ is diagonal, with entries $b_{k k}$, and $\phi$ is an undetermined function.

Multiplying (3-9) by $i \xi_{k}$ and summing gives
$$2|\xi| i \sum \xi_{k} h_{0 k}=2 i^{2} \xi_{k}^{2} h_{k k}-i^{2} \xi_{k}^{2} \operatorname{tr} h .$$
Substituting (3-10) on the term on the left above then gives
$$2|\xi|^{2} h_{00}-|\xi|^{2} \operatorname{tr} h=-2 \sum \xi_{k}^{2} h_{k k}+|\xi|^{2} \operatorname{tr} h,$$
so that
$$|\xi|^{2} h_{00}-|\xi|^{2} \operatorname{tr} h=-\sum \xi_{k}^{2} h_{k k}=-\phi\langle B(\xi), \xi\rangle .$$
Using the fact that $\sum h_{k k}=\operatorname{tr} h-h_{00}$, this is equivalent to
$$\phi\langle B(\xi), \xi\rangle=\phi|\xi|^{2} \operatorname{tr} B .$$
Since $B$ is assumed to be positive definite, it follows that $\phi=0$ and hence $h^{T}=0$.
If the first boundary condition $h_{00}=0$ in (3-12) is used, then $\operatorname{tr} h=0$, and hence via $(3-9), h_{0 k}=0$. This gives $h=0$, as required. If instead one uses the second condition $H^{\prime}=0$ in (3-12), a simple computation shows that to leading order, $H_{h}^{\prime}=$ $\operatorname{tr}^{T}\left(\nabla_{N} h-2 \delta^{*}\left(h(N)^{T}\right)\right)$, which has symbol $i z \sum h_{k k}-2 i \xi_{k} h_{0 k}$. Setting this to 0 at the root $z=i|\xi|$ gives
$$\sum\left(|\xi| h_{k k}+2 i \xi_{k} h_{0 k}\right)=0 .$$
Since $h^{T}=0$, this gives $\sum \xi_{k} h_{0 k}=0$, which, via (3-10) gives $h_{00}=0$ and hence $h=0$ as before.

To prove the operator $\Phi$ with boundary values (3-6) or (3-7) is Fredholm of index 0 , we deform the boundary data through elliptic boundary values to self-adjoint boundary data, which clearly has index 0 . The result then follows from the homotopy invariance of the index.

The boundary conditions (3-6) for the linearized operator $L$ may be continuously deformed to the data
$$h^{T}=0, \nabla_{N} h(N, \cdot)=0,$$
preserving ellipticity. This is proved in [19], (with only very minor differences in the details), and so we refer to [19] for further detail as needed. It is also easy to see via (2-21)-(2-22) that the boundary data (3-13) are self-adjoint for the operator $L$.

Instead, we provide more detail for the boundary values (3-7). We claim that the boundary data (3-7) can be deformed, preserving ellipticity, to the boundary data
$$h_{0}^{T}=0, N\left(\operatorname{tr} h^{T}\right)=0, \text { and } \nabla_{N} h(N, \cdot)=0,$$
where $h_{0}^{T}$ is the trace-free part of $h^{T}$. To see this, first the deformation $B_{t}=(1-$ $t) B+t \gamma$ from the positive form $B$ to $\gamma,(t \in[0,1])$, clearly preserves ellipticity, and so we may assume $B=\gamma$. Next deform $\beta$ to $\beta_{t}$ as
$$\beta_{t}(h)=-\nabla_{N} h(N, \cdot)-(1-t) \nabla_{e_{i}} h\left(e_{i}, \cdot\right)+\frac{1}{2}(1-t) d \operatorname{tr} h,$$
with $t \in[0,1]$, and similarly
$$H_{t}^{\prime}(h)=\operatorname{tr}^{T}\left(\nabla_{N} h-2(1-t) \delta^{*}\left(h(N)^{T}\right)\right),$$
where we have ignored the lower order terms in $H^{\prime}$. The boundary data (3-9)-(3-12) are then replaced by
$$\begin{aligned}
2|\xi| h_{0 k}-2 i(1-t) \sum \xi_{j} h_{j k}+i(1-t) \xi_{k} \operatorname{tr} h & =0 \\
2|\xi| h_{00}-2 i(1-t) \sum \xi_{k} h_{0 k}-(1-t)|\xi| \operatorname{tr} h & =0 \\
h_{k l} & =\phi \delta_{k l} \\
-|\xi| \sum h_{k k}-2 i(1-t) \xi_{k} h_{0 k} & =0
\end{aligned}$$
Now multiply $(3-15)$ by $(1-t) i \xi_{k}$ and use $(3-17)$ to obtain
$$\left.2 i(1-t)|\xi| \sum\left|\xi_{k} h_{0 k}=-2(1-t)^{2} \phi\right| \xi\right|^{2}+n(1-t)^{2} \phi|\xi|^{2}+(1-t)^{2}|\xi|^{2} h_{00} .$$
By (3-17)-(3-18), the left side above equals $-n|\xi|^{2} \phi$, so that
$$-n|\xi|^{2} \phi=(n-2)(1-t)^{2} \phi|\xi|^{2}+(1-t)^{2}|\xi|^{2} h_{00} .$$
Next substituting $2 i(1-t) \sum \xi_{k} h_{0 k}=-n|\xi| \phi$ in (3-16) gives
$$-n \phi=(1+t) h_{00}-n(1-t) \phi,$$
so that $h_{00}=-n t \phi /(1+t)$. Substituting this into (3-20) gives
$$(n-2)(1-t)^{2} \phi=-n \phi+\frac{t(1-t)^{2}}{1+t} n \phi$$
which is easily seen to give $\phi=0$, so that $h^{T}=0$. Via (3-18), this implies (1- t) $\xi_{k} h_{0 k}=0$, which, when substituted in (3-16) implies that $h_{00}=0$. From (3-15) one then also obtains $h_{0 k}=0$, and hence $h=0$, as required. This proves the claim above, and hence the index of $\Phi$ with boundary data (3-7) is the same as that with
boundary data (3-14). Again via (2-21)-(2-22), it is easily seen by inspection that $L$ is self-adjoint with the boundary data (3-14), which completes the proof. \(\square\)

Next we consider some applications of Proposition 3.1. Probably the most natural choice for the form $B$ is just $B=g^{T}$, so that for $\gamma=g^{T},[\gamma]_{B}=[\gamma]$ is the conformal class of $\gamma$. This leads to Theorem 1.2.

Proof of Theorem 1.2 Let $\mathcal{C}^{m, \alpha}(\partial M)$ be the space of pointwise conformally equivalent $C^{m, \alpha}$ metrics on $\partial M$. Proposition 3.1 and elliptic boundary regularity, cf Agmon-Douglis-Nirenberg [1] and Morrey [16], implies that the map
$$\begin{gathered}
\Psi: \operatorname{Met}_{C}^{m, \alpha}(M) \rightarrow S_{2}^{m-2, \alpha}(M) \times \mathcal{C}^{m, \alpha}(\partial M) \times C^{m-1, \alpha}(\partial M) \\
\Psi(g)=\left(\Phi_{\widetilde{g}}(g),\left[g^{T}\right], H\right)
\end{gathered}$$
is a smooth Fredholm map of index 0 for $g$ near $\widetilde{g}$. Hence, the associated boundary map
$$\begin{gathered}
\widetilde{\Pi}_{D}: \mathbb{E}_{C}^{m, \alpha}(M) \rightarrow \mathcal{C}^{m, \alpha}(\partial M) \times C^{m-1, \alpha}(\partial M), \\
\widetilde{\Pi}_{D}(g)=\left(\left[g^{T}\right], H\right),
\end{gathered}$$
is also smooth and Fredholm, of Fredholm index 0 for $g$ near $\widetilde{g}$. The proof of Theorem 1.2 then follows from Lemma 2.10, just as in the proof of Theorem 1.1. \(\square\)

Note that for $g \in \mathcal{E}^{m, \alpha}$, the scalar constraint (3-4) implies that the scalar curvature of the boundary metric $\gamma=g^{T} \in \operatorname{Met}^{m, \alpha}(\partial M)$ is in $C^{m-1, \alpha}$. This is consistent with the fact that only the conformal class of the boundary metric $g^{T}$ is prescribed in (3-22).

Next, consider the example where $B$ equals the second fundamental form $A$ of the metric $g \in \mathbb{E}_{C}^{m, \alpha}$ and assume $\partial M$ is strictly convex for ( $M, g$ ). One has $A \in S_{2}^{m-1, \alpha}(\partial M)$, so that the quotient $\operatorname{Met}^{m, \alpha}(\partial M) / A$ is not well-defined. To remedy this, let $\widetilde{A}=$ $\widetilde{A}(g, \varepsilon) \in S_{2}^{\infty}(\partial M)$ be a $C^{\infty}$ smooth approximation to $A=A(g), \varepsilon$-close to $A$ in $C^{m-1, \alpha}$. As above, the boundary map
$$\begin{gathered}
\widetilde{\Pi} \widetilde{A}^{:} \mathbb{E}_{C}^{m, \alpha}(M) \rightarrow \operatorname{Met}^{m, \alpha}(\partial M) / \widetilde{A} \times C^{m-1, \alpha}(\partial M), \\
\widetilde{\Pi}_{D}(g)=\left(\left[g^{T}\right] \widetilde{A}, H\right),
\end{gathered}$$
is $C^{\infty}$ smooth and Fredholm, of Fredholm index 0 for $g$ near $\widetilde{g}$. In particular, the linearized map has finite dimensional kernel and cokernel. This leads to the following result, closely related to a result of Schlenker [19].

Proposition 3.2 Suppose $\partial M$ is strictly convex in $(M, g)$. Then near $g$, the space of boundary values $\mathcal{B}=\Pi_{D}\left(\mathcal{E}^{\infty}\right)$ of $C^{\infty}$ Einstein metrics on $M$, if non-empty, is a variety of finite codimension in $\operatorname{Met}^{\infty}(\partial M)$.

Proof It suffices to prove the result at the linearized level. First, note that the Fredholm property of the boundary map (3-23) also holds when $m=\infty$. Observe also that the full diffeomorphism group $\mathcal{D}^{\infty}$ acts on $\mathbb{E}^{\infty}$, (but not on the slice $\mathbb{E}_{C}^{\infty}$ ).
Suppose then $h \in \operatorname{Im} D \Pi \subset S_{2}^{\infty}(\partial M)$. The projection $S_{2}^{\infty}(\partial M) \rightarrow S_{2}^{\infty}(\partial M) / \widetilde{A}$ sends $\operatorname{Im} D \Pi$ onto a subspace of finite codimension. On the other hand, regarding the fiber of this projection, for $f \in C^{\infty}$, one has $f A=\delta^{*}(f N) \in S_{2}^{\infty}(\partial M)$, so that $h+f A \in \operatorname{Im} D \Pi$, for any such $f$ and any $h \in \operatorname{Im} D \Pi$. It follows that $\operatorname{Im} D \Pi$ is $\varepsilon$-dense in a subspace of finite codimension in $S_{2}^{\infty}(\partial M)$. One may then let $\widetilde{A}=$ $\widetilde{A}(\varepsilon) \rightarrow A$ in $C^{\infty}$, and the result follows. \(\square\)

We point out that natural analogs of Proposition 3.1, Proposition 3.2 and the discussion above also for Neumann boundary value problems, (replacing $\gamma$ by $A$ ). The details of this are left to the interested reader.

\section*{4 Extension to complete, noncompact metrics}

In this section, we consider extensions of Theorem 1.1 and Theorem 1.2 to complete open manifolds with compact boundary. Of course this is only relevant in the case $\lambda \leq 0$, since Einstein metrics of positive Ricci curvature have a bound on their diameter.

Let $M$ be an open manifold with compact boundary, in the sense that $M$ has a compact (interior) boundary $\partial M$, together with a collection of non-compact ends. A priori, at this stage $M$ could have an infinite number of ends, and/or ends of infinite topological type. As in Section 2, we assume $\pi_{1}(M, \partial M)=0$, so that in particular $\partial M$ is connected.

Let $g_{0}$ be an Einstein metric on $M$ which is $C^{m, \alpha}$ up to $\partial M, m \geq 2$, and which is complete away from $\partial M$. Choose also a fixed, locally finite atlas in which the metric $g_{0}$ is locally in $C^{m, \alpha}$ up to $\partial M$.

The metric $g_{0}$ determines the asymptotic behavior of the space of metrics to be considered. To describe this, on $\left(M, g_{0}\right)$, let
$$v(r)=\operatorname{vol} S(r),$$
where $S(r)$ is the geodesic $r$-sphere about $\partial M$, ie
$$S(r)=\left\{x \in\left(M, g_{0}\right): \operatorname{dist}(x, \partial M)=r\right\} .$$

Choose positive constants, $a, b>0$ and let $\operatorname{Met}_{0}(M)=\operatorname{Met}_{g_{0}, a, b}^{m, \alpha}(M)$ be the space of $C^{m, \alpha}$ metrics on $M$, (in the given atlas), such that, for $r$ large,
$$\begin{aligned}
\left|g-g_{0}\right|(r) & =\sup _{x \in S(r)}\left|g-g_{0}\right|(x) \leq r^{-a} \\
\left|\nabla^{k} g\right|(r) & =\sup _{x \in S(r)}\left|\nabla^{k} g\right|(x) \leq r^{-(a+b)}
\end{aligned}$$
for $k=1,2$ and for any $g_{1}, g_{2} \in \operatorname{Met}_{0}(M)$,
$$\left|g_{1}-g_{0}\right| \cdot\left|\nabla g_{2}\right|(r)+\left|\nabla g_{1}\right| \cdot\left|\nabla^{2} g_{2}\right|(r) \leq \varepsilon(r) v(r)^{-1},$$
where $\varepsilon(r) \rightarrow 0$ as $r \rightarrow \infty$; the norms and covariant derivatives are taken with respect to $g_{0}$.

These decay conditions at infinity are quite weak. Consider for example the situation where $g_{0}$ is Euclidean, or more generally flat in the sense that $g_{0}$ is the flat metric on $\mathbb{R}^{m} \times T^{n-m+1}$, where $T^{n-m+1}$ is a flat $(n-m+1)$ torus and $m \geq 3$. Then $v(r)=c r^{m-1}$ and the conditions (4-2)-(4-4) are satisfied if
$$2 a+b>m-1 .$$
The usual notion of an asymptotically flat metric $g$ requires $g$ to decay at the rate of the Green's function, $\left|g-g_{0}\right|=O\left(r^{-(m-2)}\right)$ in this case, while $\left|\nabla^{k} g\right|=O\left(r^{-(m-2+k)}\right)$. The condition (4-5) is clearly much weaker than this requirement.

Now given $g_{0}$, define the spaces $\operatorname{Met}_{C}, Z_{C}$ and $\mathbb{E}_{C} \subset Z_{C}$ as subspaces of $\operatorname{Met}_{0}(M)$ exactly as in (2-9)-(2-10). Further, let
$$\mathbb{E} \subset \operatorname{Met}_{0}(M),$$
be the space of all Einstein metrics in $\operatorname{Met}_{0}(M)$.
Next, regarding the gauge groups for these spaces, let $\mathcal{D}$ be the group of $C^{m+1, \alpha}$ diffeomorphisms $\phi$ of $M$ which satisfy decay conditions analogous to (4-2)-(4-4), ie taking the supremum over $x \in S(r)$,
$$\begin{aligned}
|\phi-\mathrm{Id}|(r) & \leq r^{-a} \\
\left|\nabla^{k}(\phi-\mathrm{Id})\right|(r) & \leq r^{-(a+b)}
\end{aligned}$$
for $k=1,2$ and for any $\phi_{1}, \phi_{2} \in \mathcal{D}$,
$$\left|\phi_{1}-\mathrm{Id}\right| \cdot\left|\nabla\left(\phi_{2}-\mathrm{Id}\right)\right|(r)+\left|\nabla\left(\phi_{1}-\mathrm{Id}\right)\right| \cdot\left|\nabla^{2}\left(\phi_{2}-\mathrm{Id}\right)\right|(r) \leq \varepsilon(r) v(r)^{-1} .$$
Then $\mathcal{D}$ acts on $\operatorname{Met}_{0}(M)$. Let $\mathcal{D}_{1} \subset \mathcal{D}$ be the subgroup of diffeomorphisms equal to the identity on $\partial M$. Let $\chi_{1}$ denote the corresponding space of vector fields on $M$.

The proofs of Theorems 1.1-1.2 in this context are identical to the proofs when $M$ is compact, provided two issues are addressed. First, in the integration by parts arguments used in several places in the proof of Proposition 2.5 and the lemmas preceding it, one needs all boundary terms taken over $S(r)$ to decay to 0 as $r \rightarrow \infty$. Second, one needs to choose function spaces and boundary conditions at infinity for which the operators $L$ and $\beta \delta^{*}$ are Fredholm.

Thus, consider closed subspaces $\operatorname{Met}_{F}(M) \subset \operatorname{Met}_{C}(M), \mathcal{D}_{F} \subset \mathcal{D}_{1}$, and the associated $S_{F}(M) \subset S_{2}(M)$ and $\chi_{F}(M) \subset \chi_{1}$, which are compatible in the sense that $\mathcal{D}_{F}$ acts on $\operatorname{Met}_{F}(M)$. One may then consider the quotient spaces $\operatorname{Met}_{F}(M) / \mathcal{D}_{F}$ and in particular
$$\mathcal{E}_{F}=\mathbb{E}_{F} / \mathcal{D}_{F},$$
where $\mathbb{E}_{F} \subset \mathbb{E}$ is the subspace of Einstein metrics in $\operatorname{Met}_{F}(M)$.

Proposition 4.1 Let $\operatorname{Met}_{F}(M) \subset \operatorname{Met}{ }_{C}(M)$ and $\mathcal{D}_{F} \subset \mathcal{D}_{1}$ be compatible closed subspaces on which the operators $\left.L\right|_{T_{g} \operatorname{Met}_{F}(M)}$ and $\left.\beta \delta^{*}\right|_{\chi_{F}}$ are Fredholm.

Then Theorems 1.1-1.2 hold on $\operatorname{Met}_{F}(M)$, ie the space $\mathcal{E}=\mathcal{E}_{F}(M)$ is either empty or an infinite dimensional smooth Banach manifold, (or Fréchet manifold when $m=\infty$ ), on which the boundary map (1-5) satisfies the conclusions of Theorem 1.2.

Proof By straightforward inspection, the decay conditions (4-2)-(4-4) and (4-7)-(4-9) insure that the first condition above regarding the decay of the boundary terms at $S(r)$ holds. These boundary terms arise in $(2-11),(2-13)$ and in $(2-21)$, via the divergence theorem.

Given that $L$ and $\beta \delta^{*}$ is Fredholm, the proofs of Theorems 1.1-1.2 then carry over without change to the current situation. \(\square\)

For an arbitrary complete Einstein metric ( $M, g_{0}$ ), there is no general theory to determine whether natural elliptic operators are Fredholm on suitable function spaces. A detailed analysis in the case of "fibered boundary" metrics has been carried out by Mazzeo and Melrose, cf [15]. For simplicity, we restrict here to the situation of asymptotically flat metrics.

Thus, let $g_{f l}$ be a complete flat metric on the manifold $N=\mathbb{R}^{m} \times T^{n+1-m} / \Gamma$, where $\Gamma$ is a finite group of isometries. Let $(x, y)$ be standard coordinates for $\mathbb{R}^{m}$ and $T^{n+1-m}$ and let $r=|x|$. Define
$$C_{\delta}^{m, \alpha}(N)=\left\{u=r^{-\delta} f: f \in C_{0}^{m, \alpha}(N)\right\},$$
where $C_{0}^{m, \alpha}$ is the space of functions $f$ such that $\left(1+r^{2}\right)^{|\beta| / 2} \partial_{x}^{\beta} f \in C^{0, \alpha}, \partial_{y}^{\beta} f \in C^{0, \alpha}$, where $|\beta| \leq m$, and $C^{0, \alpha}$ is the usual space of $C^{\alpha}$ Holder continuous functions on $N$.

Let $M$ be a manifold with compact boundary $\partial M$, having a finite number of ends, each diffeomorphic to some $N$ above, (not necessarily fixed). Given a choice of flat metric $g_{f l}$ on each end, let $\operatorname{Met}_{\delta}(M)$ be the space of locally $C^{m, \alpha}$ metrics $g$ on $M$ such that the components of $\left(g-g_{f l}\right)$ in the $(x, y)$ coordinates are in $C_{\delta}^{m, \alpha}(N)$. One defines the group of $C^{m+1, \alpha}$ diffeomorphisms $\mathcal{D}_{1, \delta}$ and associated vector fields $\chi_{1, \delta}$ in the same way.

By [15], the Laplace-type operators $L$ and $\delta \delta^{*}$ are $\operatorname{Fredholm}$ as maps $\operatorname{Met}_{\delta}^{m, \alpha}(M) \rightarrow$ $S_{2, \delta}^{m-2, \alpha}(M)$ and $\chi_{1, \delta}^{m+1, \alpha} \rightarrow \chi_{1, \delta}^{m-1, \alpha}$ provided $m \geq 3$ and
$$0<\delta<m-2 \text {. }$$
Choosing then $a=\delta$ and $b=\delta+1$ in (4-2)-(4-3) and (4-7)-(4-8) shows that (4-4) and (4-9) hold provided
$$\frac{m-2}{2}<\delta<m-2 .$$
We now set $\operatorname{Met}_{F}(M)=\operatorname{Met}_{\delta}^{m, \alpha}(M)$, for $\delta$ satisfying (4-12) and let $\mathcal{D}_{F}$ be the corresponding space of $C^{m+1, \alpha}$ diffeomorphisms. Let $\mathcal{E}=\mathcal{E}_{F}$. Then combining the results above with the rest of the proof of Theorem 1.1 proves the following more precise version of Theorem 1.3.

Theorem 4.2 For $\pi_{1}(M, \partial M)=0$, the space $\mathcal{E}$ of Ricci-flat, locally asymptotically flat metrics on $M$, satisfying the decay conditions (4-12), if non-empty, is an infinite dimensional smooth Banach manifold, (Fréchet if $m=\infty$ ). Further, the boundary map (1-5) satisfies the conclusions of Theorem 1.2.

Note that Einstein metrics $g \in \mathcal{E}$ will often satisfy stronger decay conditions than (4-12). The Einstein equations imply that the metrics decay to the flat metric on the order of $O\left(r^{-(m-2)}\right)$; this will not be discussed further here however.

\section*{5 Matter fields}

In this section, we consider Theorems 1.1-1.3 for the Einstein equations coupled to other (matter) fields $\phi$. Typical examples of such fields, which arise naturally in physics are:
\begin{itemize}
\item[-] Scalar fields, $u: M \rightarrow \mathbb{R}$.
\end{itemize}
\begin{itemize}
\item[-] $\sigma$-models, $\varphi:(M, g) \rightarrow(X, \sigma)$, where $(X, \sigma)$ is a Riemannian manifold.
\item[-] Gauge fields $A$, ie connection 1-forms on principal bundles over $M$.
\item[-] $p$-form fields $\omega$.
\end{itemize}
We assume that there is an action or Lagrangian $\mathcal{L}=\mathcal{L}(g, \phi)$, of the form
$$\mathcal{L}=\mathcal{L}_{E H}+\mathcal{L}_{m},$$
where $\mathcal{L}_{E H}$ is the Einstein-Hilbert Lagrangian with integrand $(s-2 \Lambda) d V$ and where the matter Lagrangian $\mathcal{L}_{m}$ involves the fields $\phi$ up to first order, with coupling to the metric $g$ also involving at most the first derivatives of $g$. We also assume that $\mathcal{L}$ is analytic in $(g, \phi)$ and is diffeomorphism invariant, in that for any $f \in \mathcal{D}_{1}$,
$$\mathcal{L}\left(f^{*} g, f^{*} \phi\right)=\mathcal{L}(g, \phi) .$$
The variation of $\mathcal{L}$ with respect to $g, \frac{\partial \mathcal{L}}{\partial g}$ gives the Euler-Lagrange equations for $g$ :
$$-E^{1}(g, \phi)=\operatorname{Ric}_{g}-\frac{s}{2} g+\Lambda g-T=0$$
where $T$ is the stress-energy tensor of the fields $\phi$, ie the variation of $\mathcal{L}_{m}$ with respect to $g$, cf Hawking-Ellis [10] for instance. The stress-energy $T$ is first order in $g$ and $\phi$ and the Bianchi identity implies the conservation property
$$\delta T=0 .$$
Similarly, the variation of $\mathcal{L}_{m}$ with respect to the fields $\phi$ gives the Euler-Lagrange equations for $\phi$, written schematically as
$$E^{2}(g, \phi)=E_{g}^{2}(\phi)=0 .$$
We assume $E_{g}^{2}(\phi)$ can be written in the form of a second order elliptic system for $\phi$, with coefficients depending on $g$ up to first order. Typically, the operator $E_{g}^{2}$ will be a diagonal or uncoupled system of Laplace-type operators at leading order. For simplicity, we do not discuss Dirac-type operators, although it can be expected that similar results hold in this case. Note that by (5-2), the coupled field equations (5-3) and (5-5) are invariant under the action of $\mathcal{D}_{1}$.