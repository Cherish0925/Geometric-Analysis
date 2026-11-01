---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: On boundary value problems for Einstein metrics]

For example, the Lagrangian for a scalar field with potential $V$ is given by
$$\mathcal{L}_{m}=-\int_{M}\left[\frac{1}{2}|d u|^{2}+V(u)\right] d V_{g}$$
where $V: \mathbb{R} \rightarrow \mathbb{R}$. An important special case is the free massive scalar field, where $V(u)=m^{2} u^{2}$. The field equation (5-5) for $u$ is then
$$\Delta_{g} u=V^{\prime}(u),$$
with stress-energy tensor given by
$$T=\frac{1}{2}\left[d u \cdot d u-\left(\frac{1}{2}|d u|^{2}+V(u)\right) g\right] .$$
For a gauge field or connection 1-form $\phi=d+A$, the usual Lagrangian is the Yang-Mills action
$$\mathcal{L}_{m}=-\frac{1}{2} \int_{M}|F|^{2} d V_{g}$$
where $F=d_{A} A \equiv d A+\frac{1}{2}[A, A]$ is the curvature of $A$. The field equations are the Yang-Mills equations, (or Maxwell equations in the case of a $U(1)$ bundle):
$$d_{A} F=\delta_{A} F=0,$$
with stress-energy tensor
$$T=F \cdot F-\frac{1}{2}|F|^{2} g,$$
where $(F \cdot F)_{\mu \nu}=\left\langle F_{\mu \alpha}, F_{\nu \beta}\right\rangle g^{\alpha \beta}$.
To match with the work in Section 2, we pass from (5-3) to the equivalent equations
$$\operatorname{Ric}_{g}-\lambda g-T_{0}=0$$
where $T_{0}=T-\frac{\operatorname{tr} T}{n+1} g$ is the trace-free part of $T$. The conservation law (5-4) then translates to
$$\beta(\widetilde{T})=0 .$$
We begin with a detailed discussion of the case of the Einstein equations coupled to a scalar field $u: M \rightarrow \mathbb{R}$ with potential $V(u)$, where $V: \mathbb{R} \rightarrow \mathbb{R}$ is an arbitrary smooth function; as will be seen below, the treatment of other fields is very similar.

The full Lagrangian is given by
$$\mathcal{L}(g, u)=\int_{M}\left[(s-2 \Lambda)-\frac{1}{2}|d u|^{2}-V(u)\right] d V_{g}$$
which gives the field equations
$$\operatorname{Ric}_{g}-\lambda g=T_{0}=\frac{1}{2}\left(d u \cdot d u-\frac{1}{n-1} V g\right), \Delta u=V^{\prime}(u),$$
when the variations of $(g, u)$ are of compact support in $M$. As in the proof of Theorem 1.1, where the boundary data for the metric $g$ were not fixed in advance, it is useful here not to fix boundary values for the scalar field $u$. Thus, instead of (5-14), we consider the Lagrangian
$$\mathcal{L}(g, u)=\int_{M}\left[(s-2 \Lambda)+\frac{1}{2} u \Delta u-V(u)\right] d V$$
Of course, the Lagrangians (5-14) and (5-16) differ just by boundary terms.
The Lagrangian is a map $\operatorname{Met}^{m, \alpha}(M) \times C^{k, \beta}(M) \rightarrow \mathbb{R}$, and we assume $k \geq 2$, $\beta \in(0,1)$. The differential (or variation) $d \mathcal{L}$ is then a map
$$d \mathcal{L}=\left(\mathcal{L}^{1}, \mathcal{L}^{2}\right): \operatorname{Met}^{m, \alpha}(M) \times C^{k, \beta}(M) \rightarrow T^{*}\left(\operatorname{Met}^{m-2, \alpha}(M) \times C^{k-2, \beta}(M)\right),$$
where
$$d \mathcal{L}_{(g, u)}^{1}(h, v)=-\left\langle\operatorname{Ric}_{g}-\lambda g-\widetilde{T}(g, u), h\right\rangle d V,$$
represents the variation with respect to $g$ and
$$d \mathcal{L}_{(g, u)}^{2}(h, v)=\left(\frac{1}{2}(v \Delta u+u \Delta v)-V^{\prime}(u) \cdot v\right) d V,$$
represents the variation with respect to $u$. The "new" stress-energy tensor $\widehat{T}$ for (5-16) is given by $\widehat{T}=\frac{1}{2}\left[u \Delta^{\prime} u+\left(\frac{1}{2} u \Delta u-V(u)\right) g\right]$, where $\Delta^{\prime} u$ is the metric variation of the Laplacian, given by
$$\Delta^{\prime} u(h)=-\left\langle D^{2} u, h\right\rangle+\langle d u, \beta(h)\rangle,$$
where $\beta$ is the Bianchi operator $\beta(h)=\delta h+\frac{1}{2} d(\operatorname{tr} h)$. Using (5-20), it is easily seen that $\widehat{T}=T$, for $T$ as in (5-8), modulo boundary terms, and so we continue to use (5-8). In particular, for variations of compact support, one obtains the Euler-Lagrange equations (5-15).

Let $\mathbb{E}=\mathbb{E}(M, g, u)$ denote the space of all solutions of the equation $d \mathcal{L}=0$, for $\mathcal{L}$ as in (5-16), ie the space of solutions to the Einstein equations coupled to the scalar field $u$. This space is invariant under the diffeomorphism group $\mathcal{D}_{1}$, acting on both $(g, u)$ by pullback.

As in Section 2, one needs to choose a gauge to break the diffeomorphism invariance; (the scalar field has no internal symmetry group, so there is no need of an extra gauge for $u$ ). Thus, analogous to the discussion in Section 2, given a background metric $\widetilde{\boldsymbol{g}} \in \mathbb{E}$, define
$$\Phi=\Phi \widetilde{g}: \operatorname{Met}(M) \times C^{k, \beta}(M) \rightarrow T^{*}\left(\operatorname{Met}(M) \times C^{k-2, \beta}(M)\right) ;$$
$$\Phi(g, u)=\left[\left(\operatorname{Ric}_{g}-\lambda g-\widetilde{T}(g, u)+\delta^{*} \beta \widetilde{g}(g)\right) d V,-\left(\frac{1}{2}(\cdot \Delta u+u \Delta \cdot)-V^{\prime}(u) \cdot\right) d V\right] .$$
(For convenience, we have switched the signs in comparison with (5-18)-(5-19)). As before, $\operatorname{Met}_{C}(M)=\operatorname{Met}_{C}^{m, \alpha}(M)$ is defined to be the space of $C^{m, \alpha}$ metrics satisfying the Bianchi constraint (2-9), and we set
$$Z_{C}=\Phi^{-1}(0) \subset \operatorname{Met}_{C}(M) \times C^{m, \alpha}(M) .$$
Corollary 2.3 also holds as before, so that
$$Z_{C}=\mathbb{E}_{C},$$
(for any boundary conditions on $u$ ). Given this, the main task is to verify that the analog of Proposition 2.5 holds.

Proposition 5.1 Proposition 2.5 holds for the map $\Phi$ in (5-21), ie $D \Phi$ is surjective.

Proof Consider the derivative of $\Phi$ at $g=\widetilde{g}$ :
$$D \Phi=\left(D \Phi^{1}, D \Phi^{2}\right): T\left(\operatorname{Met}(M) \times C^{m, \alpha}(M)\right) \rightarrow T\left(T^{*}\left(\operatorname{Met}(M) \times C^{m-2, \alpha}(M)\right)\right) .$$
This is a block matrix of the form
$$\mathcal{H}=\left(\begin{array}{cc}
\frac{\partial \Phi^{1}}{\partial g} & \frac{\partial \Phi^{1}}{\partial u} \\
\frac{\partial \Phi^{2}}{\partial g} & \frac{\partial \Phi^{2}}{\partial u}
\end{array}\right) .$$
The matrix $\mathcal{H}$ is essentially the same as the second variation of the Lagrangian (5-16); they agree modulo the gauge term $\delta^{*} \beta \widetilde{g}(g)$. A straightforward computation, using the fact that $(g, u) \in \mathbb{E}$, gives:
$$\begin{aligned}
& \frac{\partial \Phi^{1}}{\partial g}(h)=\widetilde{L}(h)=L(h)+S(h), \\
& \frac{\partial \Phi^{1}}{\partial u}(v)=-d u \cdot d v+\frac{1}{2} V^{\prime}(u) v g, \\
& \frac{\partial \Phi^{2}}{\partial g}(h)=-\frac{1}{2}\left(\cdot \Delta^{\prime} u+u \Delta^{\prime} \cdot\right)-\left[\frac{1}{4}(\cdot \Delta u+u \Delta \cdot)-\frac{1}{2} V^{\prime}(u) \cdot\right] \operatorname{tr} h \\
& \frac{\partial \Phi^{2}}{\partial u}(v)=-\frac{1}{2}(\cdot \Delta v+v \Delta \cdot)+V^{\prime \prime}(u) v \cdot
\end{aligned}$$
where $L$ is the Bianchi-gauged linearized Einstein operator (2-6) and $S(h)$ is an algebraic operator of the form
$$S(h)=\frac{1}{2} \operatorname{tr} h d u \cdot d u-\frac{1}{2} V(u) h-\frac{1}{2} \operatorname{tr} h V(u) g .$$

Now if there exists $(k, w) \perp \operatorname{Im}(D \Phi)$, then
$$\int_{M}\langle D \Phi(h, v),(k, w)\rangle d V=0$$
for all $(h, v)$ with $h \in T\left(\operatorname{Met}(M) \times C^{k, \beta}(M)\right)$. As in the proof of Proposition 2.5, one integrates the expressions (5-24)-(5-27) by parts. For (5-24), one obtains, as in (2-21),
$$\int_{M}\langle L(h), k\rangle+\langle S(h), k\rangle=\int_{M}\langle L(k), h\rangle+\langle S(k), h\rangle+\int_{\partial M} D(h, k),$$
where $D$ is given by (2-22). For (5-25):
$$\left.\left[-d u \cdot d v+V^{\prime}(u) \cdot v\right) g\right](k)=\int_{M}-\langle d u \cdot d v, k\rangle+\frac{1}{2} V^{\prime}(u) \cdot v \operatorname{tr} k=$$
$$\int_{M} v\left[-\delta(k(d u))+\frac{1}{2} V^{\prime}(u) \operatorname{tr} k\right]-\int_{\partial M} v k(d u, N) .$$
Next for (5-26):
$$\begin{aligned}
& \left.-\left[\frac{1}{2}\left(\cdot \Delta^{\prime} u+u \Delta^{\prime} \cdot\right)+\frac{1}{4}(\cdot \Delta u+u \Delta \cdot)-\frac{1}{2} V^{\prime}(u) \cdot\right) \operatorname{tr} h\right](w) \\
& \left.=-\int_{M} \frac{1}{2}\left(w \Delta^{\prime} u+u \Delta^{\prime} w\right)+\frac{1}{4}(w \Delta u+u \Delta w)-\frac{1}{2} V^{\prime}(u) w\right) \operatorname{tr} h
\end{aligned}$$
and
$$\begin{aligned}
\int_{M} w \Delta^{\prime} u & =\int_{M}-w\left\langle D^{2} u, h\right\rangle+w\langle d u, \beta(h)\rangle \\
& =\int_{M}\left\langle d u \cdot d w+\frac{1}{2} \delta(w d u) g, h\right\rangle-\int_{\partial M} w h(d u, N)-\frac{1}{2} \operatorname{tr} h w N(u)
\end{aligned}$$
Interchanging $u$ and $w$ then gives
$$\begin{aligned}
w \cdot \frac{\partial \Phi^{2}}{\partial g}(h)= & -\int_{M}\left\langle d u \cdot d w+\frac{1}{4} \delta(d u w) g+\frac{1}{4}(w \Delta u+u \Delta w) g\right. \\
& \left.\left.-\frac{1}{2} V^{\prime}(u) w\right) g, h\right\rangle+\frac{1}{2} \int_{\partial M} h(d u w, N)-\frac{1}{2} \operatorname{tr} h N(u w)
\end{aligned}$$
Finally, for (5-27),
$$\begin{aligned}
-\left[\frac{1}{2}(\cdot \Delta v+v \Delta \cdot)-V^{\prime \prime}(u) v \cdot\right](w) & =-\frac{1}{2} \int_{M}\left(w \Delta v+v \Delta w-2 V^{\prime \prime}(u) v w\right) \\
& =-\int_{M} v\left(\Delta w-V^{\prime \prime}(u) w\right)-\frac{1}{2} \int_{\partial M} w N(v)-v N(w)
\end{aligned}$$

Now, supposing (5-28) holds, since $v$ is arbitrary, by adding the bulk terms in (5-30) and (5-32) one obtains
$$\Delta w-V^{\prime \prime}(u) \cdot w+\delta(k(d u))-\frac{1}{2} V^{\prime}(u) \operatorname{tr} k=0,$$
on $(M, g)$; this is the equation for the variation $w$ of the scalar field $u$. Adding the boundary terms in (5-30) and (5-32) gives
$$\int_{\partial M} w N(v)-v[N(w)-2 k(d u, N)]=0 .$$
The boundary values of $v$ are arbitrary, so that both $v$ and $N(v)$ can be prescribed arbitrarily at $\partial M$. Hence (5-34) implies that
$$w=0 \text { and } N(w)-2 k(d u, N)=0,$$
at $\partial M$.
Next, since $h$ is arbitrary in the interior, adding the bulk terms in (5-29) and (5-31) gives
$$L(k)+S(k)-d u \cdot d w-\frac{1}{4} \delta(d u w) g-\frac{1}{4}(w \Delta u-u \Delta w) g+\frac{1}{2} V^{\prime}(u) w g=0 .$$
This is the equation for the variation $k$ of the metric $g$. At $\partial M$, adding the boundary terms in (5-29) and (5-31) gives
$$D(h, k)+\frac{1}{2}\left[h(d u w, N)-\frac{1}{2} \operatorname{tr} h N(u w)\right]=0 .$$
Since $w=0$ at $\partial M$, one thus has
$$D(h, k)+\frac{1}{2} u N(w)\left[h(N, N)-\frac{1}{2} \operatorname{tr} h\right]=0 .$$
Now the same arguments as in (2-21)-(2-37) carry over to this situation essentially unchanged. The proof of (2-24) follows in the same way as before, via the diffeomorphism invariance of $\mathbb{E}$. It follows then from (5-35) and (5-37) that the geometric Cauchy data vanish at $\partial M$, ie
$$k^{T}=\left(A_{k}^{\prime}\right)^{T}=0, \text { and } w=N(w)=0, \text { at } \partial M .$$
By (5-33) and (5-36), the pair $(k, w)$ satisfy the coupled system of equations:
$$\begin{aligned}
L(k)+S(k)-d u \cdot d w-\frac{1}{4} \delta(d u w) g-\frac{1}{4}(w \Delta u-u \Delta w) g+\frac{1}{2} V^{\prime}(u) w g & =0, \\
\Delta w-V^{\prime \prime}(u) \cdot w+\delta(k(d u))-\frac{1}{2} V^{\prime}(u) \operatorname{tr} k & =0 .
\end{aligned}$$

Here, ( $g, u$ ) are fixed, and viewed as (smooth) coefficients, while ( $k, w$ ) are the unknowns. The equations (5-39)-(5-40) express the fact that $(k, w) \in T Z$. Since $k$ is transverse-traceless so that $\beta(k)=0$, the pair $(k, w)$ satisfy the linearized Einstein equations coupled to a scalar field.

The unique continuation property, Proposition 2.4, also holds for these linearized Einstein equations, since the scalar field $u$ modifies the Einstein equations only at first order. Given the vanishing of the geometric Cauchy data in (5-38), the proof that
$$k=w=0 \text { on } M,$$
proceeds just as before. This proves the surjectivity of $D \Phi$, and the proof that the kernel splits is again the same. \(\square\)

Let $\mathcal{E}=\mathcal{E}_{\lambda, V}^{m, \alpha}(g, u)$ be the moduli space of Einstein metrics $g$ coupled to a scalar field $u$ with potential $V$ on $(M, \partial M)$. As before, one has a natural Dirichlet boundary map $\Pi_{D}$, giving Dirichlet boundary values to $u$, or its mixed version $\widetilde{\Pi}_{D}$ as in (1-5). Given Proposition 5.1 and the remarks above, the rest of the work in Section 2 and Section 3 carries over unchanged, and proves the following.

Corollary 5.2 Suppose $\pi_{1}(M, \partial M)=0$. Then the space $\mathcal{E}$ of solutions to the Einstein equations coupled to a scalar field with potential $V$, if non-empty, is an infinite dimensional smooth Banach manifold, (Fréchet when $m=\infty$ ), for which the boundary map $\widetilde{\Pi}_{D}$ is smooth and Fredholm of index 0, ie Theorem 1.1 and Theorem 1.2 hold.

Similarly, Corollary 5.2 holds in the same way, for scalar fields in the space $C_{\delta}^{k, \beta}$ with $\delta$ satisfying (4-12), ie in the asymptotically flat context.

Next consider the situation of the Einstein equations coupled to a nonlinear $\sigma$-model. In this case the field $\phi$ is a smooth function $u:(M, g) \rightarrow(X, \sigma)$, with matter Lagrangian
$$\mathcal{L}_{m}=-\int_{M}\left[\frac{1}{2}|d u|^{2}+V(u)\right] d V_{g}$$
where $|d u|^{2}=\sigma\left(d u\left(e_{i}\right), d u\left(e_{i}\right)\right)$, for a local orthonormal basis $e_{i}$ of $(M, g) ; d u$ is the derivative map of $u$, and $V: X \rightarrow \mathbb{R}$ the potential function.

The analysis in this case is essentially the same as that of a single scalar field discussed above. Probably the simplest way to see this is to isometrically embed ( $X, \sigma$ ), via the Nash embedding theorem, into a large Euclidean space $\mathbb{R}^{N}$. Then $u:(M, g) \rightarrow(X, \sigma)$ is a vector-valued function $u=\left\{u^{i}\right\}:(M, g) \rightarrow \mathbb{R}^{N}, 1 \leq i \leq N$, with the constraint
that $\operatorname{Im} u \subset X \subset \mathbb{R}^{N}$. The metric $\sigma$ on $X$ is then just the restriction of the Euclidean dot-product metric to $T X$.

The $\sigma$-model field equations for the Lagrangian (5-42) are
$$\Delta^{T} u=V^{\prime}(u)=u^{*}(\nabla V),$$
where $\Delta^{T}$ is the projection of the Laplacian $\Delta=\Delta_{(M, g)}$, acting on the components $u^{i}$ of $u$, onto $T X$. If $S$ denotes the second fundamental form of $X$ in $\mathbb{R}^{N}$, then (5-43) is equivalent to the system
$$\Delta u=S(d u, d u)+V^{\prime}(u) .$$
The stress-energy tensor $T$ has exactly the same form as in (5-8), where $d u \cdot d u$ is the symmetric bilinear form on $M$ given by taking the Euclidean dot product of the vector $u=\left\{u^{i}\right\}$.

Given this, it is now straightforward to see that all the computations carried out in the case of a single scalar field $u$ carry over without significant change to the present constrained, vector-valued field $u$ to give the following.

Corollary 5.3 If $\pi_{1}(M, \partial M)=0$, then the space $\mathcal{E}$ of solutions to the Einstein equations coupled to a $\sigma$-model $u: M \rightarrow(X, \sigma)$, if non-empty, is an infinite dimensional smooth Banach manifold, for which the boundary map $\widetilde{\Pi}_{D}$ is smooth and Fredholm, of index 0.

Again, the analog of Theorem 4.2 also holds in this context.
Finally consider the Einstein equations coupled to gauge fields, ie connections $\omega$ on principal bundles $P$ over $M$ with compact semi-simple structure group $G$ with bi-invariant metric. The simplest coupled Lagrangian is
$$\mathcal{L}=\int_{M}(s-2 \Lambda) d V_{g}-\frac{1}{2} \int_{M}|F|^{2} d V_{g}$$
with field equations
$$\text { Ric }-\lambda g-T_{0}=0, \delta_{\omega} F=0$$
where $T$ is given by (5-11) and $T_{0}$ is the trace-free part.
Let $\mathcal{A}(P)=\mathcal{A}^{k, \beta}(P)$ denote the space of connections on $P$ which are $C^{k, \beta}$ smooth up to $\partial M$, with $k \geq 2, \beta \in(0,1)$. Given any fixed connection $\omega_{0} \in \mathcal{A}(P)$, any $\omega \in \mathcal{A}(P)$ has the form $\omega=\omega_{0}+A$, where $A$ is a 1-form on $P$ with values in the Lie algebra $\mathcal{L}(G)$. Let $\mathbb{E}=\mathbb{E}(g, A)$ be the space of all solutions to the field equations
(5-46), ie the space of all solutions of the Einstein equations coupled to the gauge field $A$. The Lagrangian (5-45) and the field equations (5-46) are invariant under the diffeomorphisms $\mathcal{D}_{1}$ of $M$, as well as gauge transformations of $P$, again equal to the identity on $\partial M$. We expect the natural analogs of Theorem 1.1 and Theorem 1.2, (and Theorem 4.2), hold in this context as well, by the same methods. However, this will not be discussed here in detail, cf Marini [14] for some discussion along these lines.

Remark 5.4 Although the focus of this work has been on Einstein metrics, the main results also apply to other field equations, with the background manifold and metric ( $M, g$ ) arbitrary, (not necessarily Einstein), but fixed. Thus for example, the proof of Corollary 5.2 shows that the space of solutions to the scalar field equation (5-7) with fixed ( $M, g$ ) is an infinite dimensional smooth Banach manifold, (if non-empty), with Dirichlet and Neumann boundary maps Fredholm of index 0. This follows just by considering the piece $\partial \Phi^{2} / \partial u$ in $\mathcal{H}$ in (5-23). Thus, one may set $k=0$ following $(5-38)$ and argue as before. Of course in the case the potential $V(u)$ is linear, the space of solutions of (5-7) is a linear space.

Similarly, the space of harmonic maps $u:(M, g) \rightarrow(X, \sigma)$ with fixed data $(M, g)$ and $(X, \sigma)$ also satisfies the conclusions of Theorem 1.1 and Theorem 1.2. This has previously been known, cf Eells-Lemaire [7], only in the case of "non-degenerate" harmonic maps.

\section*{References}
\begin{itemize}
\item[] [1] S Agmon, A Douglis, L Nirenberg, Estimates near the boundary for solutions of elliptic partial differential equations satisfying general boundary conditions. I and II, Comm. Pure Appl. Math. 12 and 17 (1964) 623-727 and 35-92
\item[] [2] M Anderson, Geometric aspects of the AdS/CFT correspondence, from: "AdS/CFT correspondence: Einstein metrics and their conformal boundaries", IRMA Lect. Math. Theor. Phys. 8, Eur. Math. Soc., Zürich (2005) 1-31 MR2160865
\item[] [3] MT Anderson, M Herzlich, Unique continuation results for Ricci curvature and applications, J. Geom. Phys. 58 (2008) 179-207 MR2384310
\item[] [4] M Anderson, A Katsuda, Y Kurylev, M Lassas, M Taylor, Boundary regularity for the Ricci equation, geometric convergence, and Gel'fand's inverse boundary problem, Invent. Math. 158 (2004) 261-321 MR2096795
\item[] [5] A L Besse, Einstein manifolds, Ergebnisse series 10, Springer, Berlin (1987) MR867684
\item[] [6] D G Ebin, The manifold of Riemannian metrics, from: "Global Analysis (Proc. Sympos. Pure Math., Vol. XV, Berkeley, Calif., 1968)", Amer. Math. Soc., Providence, R.I. (1970) 11-40 MR0267604
\end{itemize}
[7] J Eells, L Lemaire, Deformations of metrics and associated harmonic maps, from: "Geometry and analysis", Indian Acad. Sci., Bangalore (1980) 33-45 MR592252
[8] D Gilbarg, NS Trudinger, Elliptic partial differential equations of second order, second edition, Grundlehren series 224, Springer, Berlin (1983) MR737190
[9] RS Hamilton, The inverse function theorem of Nash and Moser, Bull. Amer. Math. Soc. (N.S.) 7 (1982) 65-222 MR656198
[10] S W Hawking, G F R Ellis, The large scale structure of space-time, Cambridge University Press, London (1973) MR0424186 Cambridge Monographs on Mathematical Physics, No. 1
[11] S Kobayashi, K Nomizu, Foundations of Differential Geometry, Volume 1, John Wiley, New York (1963)
[12] N Koiso, Rigidity and infinitesimal deformability of Einstein metrics, Osaka J. Math. 19 (1982) 643-668 MR676241
[13] C LeBrun, M Wang, Surveys in differential geometry: essays on Einstein manifolds, Surveys in Differential Geometry, VI, International Press, Boston (1999) MR1798603
[14] A Marini, Dirichlet and Neumann boundary value problems for Yang-Mills connections, Comm. Pure Appl. Math. 45 (1992) 1015-1050 MR1168118
[15] R Mazzeo, R B Melrose, Pseudodifferential operators on manifolds with fibred boundaries, Asian J. Math. 2 (1998) 833-866 MR1734130
[16] C B Morrey, Jr, Multiple integrals in the calculus of variations, Grundlehren series 130, Springer, New York (1966) MR0202511
[17] J Nash, The imbedding problem for Riemannian manifolds, Ann. of Math. (2) 63 (1956) 20-63 MR0075639
[18] L Nirenberg, The Weyl and Minkowski problems in differential geometry in the large, Comm. Pure Appl. Math. 6 (1953) 337-394 MR0058265
[19] J-M Schlenker, Einstein manifolds with convex boundaries, Comment. Math. Helv. 76 (2001) 1-28 MR1819659

Dept of Mathematics, SUNY at Stony Brook
Stony Brook, NY 11794-3651, USA
anderson@math.sunysb.edu

Proposed: Tobias Colding
Seconded: Simon Donaldson, David Gabai

Received: 11 March 2008
Revised: 6 May 2008