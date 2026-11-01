---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Refined gluing for Vacuum Einstein constraint equations]

---
source_file: 1003_4178.pdf
converter: mathpix
format: mmd
---

\title{
REFINED GLUING FOR VACUUM EINSTEIN CONSTRAINT EQUATIONS
}

\author{
ERWANN DELAY AND LORENZO MAZZIERI
}

\begin{abstract}
We first show that the connected sum along submanifolds introduced by the second author for compact initial data sets of the vacuum Einstein system can be adapted to the asymptotically Euclidean and to the asymptotically hyperbolic context. Then, we prove that in any case, and generically, the gluing procedure can be localized, in order to obtain new solutions which coincide with the original ones outside of a neighborhood of the gluing locus.
\end{abstract}

\section*{Contents}
1. Introduction ..... 1
1.1. Conformal gluing ..... 2
1.2. Localized gluing ..... 5
2. The geometric construction ..... 5
3. The momentum constraint: existence of solutions ..... 8
3.1. Asymptotically Euclidean manifold ..... 9
3.2. Asymptotically Hyperbolic manifold ..... 10
4. The momentum constraint: uniform a priori bound ..... 11
5. The energy constraint ..... 16
5.1. Analysis of the linearized Lichnerowicz operator ..... 17
5.2. Fixed point argument ..... 20
6. Localized gluing ..... 22
7. Constraint with cosmological constant and constant scalar curvature metrics ..... 23
8. Concluding remarks ..... 23
References ..... 24

\section*{1. Introduction}

It is well known [8] that a vacuum solution $(Z, \gamma)$ for the Einstein system Ric $_{\gamma}=0$, where $Z$ is an $(m+1)$-dimensional manifold and $\gamma$ is a Lorentzian metric, may be obtained from solutions to the vacuum Einstein constraint equations on an $m$-dimensional space-like Riemannian submanifold $(M, \tilde{g})$ of $Z$ (for further details see eg. [4]). To fix the notations, we say that the triple $(M, \tilde{g}, \tilde{\Pi})$, where $M$ is a smooth manifold, $\tilde{g}$ is a Riemannian metric and $\tilde{\Pi}$ is a symmetric $(2,0)$ tensors is a solution to the vacuum Einstein

\footnotetext{
Date: March 22, 2010.
}
constraints equations if the following relationships are satisfied
$$\begin{gathered}
J(\tilde{g}, \tilde{\Pi}):=\operatorname{div}_{\tilde{g}} \tilde{\Pi}-d\left(\operatorname{tr}_{\tilde{g}} \tilde{\Pi}\right)=0 \\
\rho(\tilde{g}, \tilde{\Pi}):=R_{\tilde{g}}-|\tilde{\Pi}|_{\tilde{g}}^{2}+\left(\operatorname{tr}_{\tilde{g}} \tilde{\Pi}\right)^{2}=0 .
\end{gathered}$$
Here $\operatorname{div}_{\tilde{g}}$ and $\operatorname{tr}_{\tilde{g}}$ are respectively the divergence operator and the trace operator computed with respect to the metric $\tilde{g}$ and $R_{\tilde{g}}$ is the scalar curvature of the metric $\tilde{g}$. In the following we will also refer to the triple $(M, \tilde{g}, \tilde{\Pi})$ as (vacuum) initial data set or Cauchy data set. We also point out that when the evolution $(Z, \gamma)$ of the initial data set is considered according to the hyperbolic formulation of the vacuum Einstein system, then $\tilde{g}$ and $\tilde{\Pi}$ turn out to be respectively the Riemannian metric and the second fundamental form induced by the Lorentzian metric $\gamma$ on the space-like slice $M$.

Of interest in this paper are constant mean curvature (briefly CMC) initial data sets, this means that $\tau:=\operatorname{tr}_{\tilde{g}} \tilde{\Pi}$ is a constant. In the case the system above becomes equivalent to a semi-decoupled system. In fact, following [8], [20] and [21], one can split the second fundamental form $\tilde{\Pi}$ into trace free and pure trace parts
$$\tilde{\Pi}=\tilde{\mu}+\frac{\tau}{m} \tilde{g},$$
where $\tilde{\mu}$ is a symmetric 2-tensor such that $\operatorname{tr}_{\tilde{g}} \tilde{\mu}=0$. Applying the so called conformal method, we set
$$\tilde{g}=: u^{4 / m-2} g \quad \text { and } \quad \tilde{\mu}=: u^{-2} \mu,$$
where the conformal factor $u$ is a positive smooth function on $M$. It is now straightforward to check that $\tilde{g}$ and $\tilde{\Pi}$ verify the Einstein constraint equations (1) and (2) if and only if $g, \mu$ and $u$ satisfy
$$\left\{\begin{array}{l}
\operatorname{tr}_{g} \mu=0 \\
\operatorname{div}_{g} \mu=0
\end{array}\right.$$
$$\Delta_{g} u-c_{m} R_{g} u+c_{m}|\mu|_{g}^{2} u^{-\frac{3 m-2}{m-2}}-c_{m} \frac{m-1}{m} \tau^{2} u^{\frac{m+2}{m-2}}=0,$$
with $c_{m}=\frac{m-2}{4(m-1)}$. Notice that our Laplacian is negative definite.
Therefore, starting with a metric $g$ and a real number $\tau$, one can obtain a $\tau$-CMC solution to the Einstein constraints by producing a symmetric $(2,0)$ -tensor $\mu$ which verifies (5) (for short a TT-tensor) together with a smooth positive solution $u$ to (6), which will play the role of the conformal factor. Using then (4) it is easy to recover the triple $(M, \tilde{g}, \tilde{\Pi})$.

In this context and due to the physical meaning, the equation (1) (or equivalently the second equation in (5)) is known as the momentum constraint, whereas the equation (2) is the so called Hamiltonian constraint and modulo the conformal transformations it corresponds to the Lichnerowicz equation (6).
1.1. Conformal gluing. In the spirit of [31], we suppose now to start with two Cauchy data sets in the semi-decoupled formulation of the constraints, namely two solutions $\left(M_{i}, g_{i}, \mu_{i}, u_{i}, \tau\right), i=1,2$ to equations (5) and (6) with the same constant mean curvature $\tau$ and we construct the generalized connected sum of the $m$-dimensional manifolds $M_{1}$ and $M_{2}$ along
a common isometrically embedded $k$-dimensional Riemannian submanifold $\left(K, g_{K}\right)$ with codimension $n:=m-k \geq 3$. This construction consists in excising a small $\varepsilon$-tubular neighborhood (i.e. a tubular neighborhood of size $\varepsilon \in(0,1))$ of $K$ in both the starting manifolds and in identifying the differentiable structures along the leftover boundaries as explained in [29] and summarized in Section 2. The reasons for requiring $n \geq 3$ is discussed in [29] and [30] as well as in [31]. Our goal is then to endow the new manifold $M_{\varepsilon}=M_{1} \sharp_{K, \varepsilon} M_{2}$ with a Riemannian structure $g_{\varepsilon}$ and a symmetric TT-tensor $\mu_{\varepsilon}$ such that it is possible to find a solution $u_{\varepsilon}$ to the Lichnerowicz equation (6).

In [31] the second author treated the case where $M_{1}, M_{2}$ and $K$ are compact. Here we extend the conformal gluing construction to the case where $M_{1}$ and $M_{2}$ are asymptotically Euclidean (AE) and asymptotically hyperbolic (AH) and the submanifold $K$ is still compact. The generalized connected sum along a non compact submanifold embedded in asymptotically Euclidean or asymptotically hyperbolic initial data sets seems to require some extra assumption on the behavior of $K$ at infinity and will be the object of further investigations.

As in [31], we will obtain a control of the new solutions in terms of the original ones. In fact, setting
$$\begin{aligned}
& \tilde{g}_{\varepsilon}:=u_{\varepsilon}^{\frac{4}{m-2}} g_{\varepsilon} \quad \text { and } \quad \tilde{\Pi}_{\varepsilon}:=u_{\varepsilon}^{-2} \mu_{\varepsilon}+\frac{\tau}{m} u_{\varepsilon}^{\frac{4}{m-2}} g_{\varepsilon}, \\
& \tilde{g}_{i}:=u_{i}^{\frac{4}{m-2}} g_{i} \quad \text { and } \quad \tilde{\Pi}_{i}:=u_{i}^{-2} \mu_{i}+\frac{\tau}{m} u_{i}^{\frac{4}{m-2}} g_{i},
\end{aligned}$$
we will have that $\tilde{g_{\varepsilon}} \rightarrow \tilde{g}_{i}$ and $\tilde{\Pi}_{\varepsilon} \rightarrow \tilde{\Pi}_{i}$ on the compact sets of $M_{i} \backslash K$, with respect to the $\mathcal{C}^{r}$ topology, for every $r \in \mathbb{N}, i=1,2$. This fact turns out to be very important when we will discuss the localization procedure.

The strategy of the proof is the same as in the compact case [31] and here we just outline it briefly. The first step is the construction of a family of approximate solution metrics $g_{\varepsilon}, \varepsilon \in(0,1)$, which coincide with $g_{i}, i=1,2$ away from $K$. In correspondence to each $\varepsilon$ we will then produce a $g_{\varepsilon}$-trace free symmetric 2-tensor $\mu$ by means of cut-off functions. We notice that $\mu$ coincide with $\mu_{i}, i=1,2$, in the region where $g_{\varepsilon}$ coincide with the original metrics.

The next step is the resolution of the momentum constraint equation, which is the linear part of the semi-decoupled system. This will be done by adding to $\mu$ a correction term of the form $D_{g_{\varepsilon}} X$, where $D_{g_{\varepsilon}}$ denotes the conformal Killing operator acting on vector fields
$$D_{g_{\varepsilon}} X:=\frac{1}{2} \mathcal{L}_{X} g_{\varepsilon}-\frac{1}{m}\left(\operatorname{div}_{g_{\varepsilon}} X\right) \cdot g_{\varepsilon} .$$
As a consequence, the momentum equation becomes
$$L_{g_{\varepsilon}} X=\sharp \operatorname{div}_{g_{\varepsilon}} \mu,$$
where $L_{g_{\varepsilon}}:=\sharp \operatorname{div}_{g_{\varepsilon}} \circ D_{g_{\varepsilon}}$ is a second order elliptic partial differential operator known as vector Laplacian. The fact that $L_{g_{\varepsilon}}$ is self-adjoint follows from the algebraic identity $D_{g_{\varepsilon}}=-\left(\sharp \operatorname{div}_{g_{\varepsilon}}\right)^{*}$.

A crucial step in the study of equation (8) is to provide the solution with an a priori estimate independent of $\varepsilon$. This will allows us to control
the squared pointwise norm $\left|\mu_{\varepsilon}\right|^{2}$ of the TT-tensor $\mu_{\varepsilon}:=\mu+D_{g_{\varepsilon}} X$ which appears in the Lichnerowicz equation. To obtain this $\varepsilon$-uniform a priori bound we need to introduce the following notion of nondegeneracy

Definition 1 (Nondegeneracy). A compact Riemannian manifold $(M, g)$ is said to be nondegenerate if there are no nontrivial conformal Killing vector fields on it or equivalently if the conformal Killing operator $D_{g}$ is injective.

We will see that the injectivity of the conformal Killing operator is automatically achieved in the asymptotically Euclidean (AE) and in the asymptotically hyperbolic (AH) situation, up to a careful choice of the functional setting. Notice that due the different geometric construction this assumption turns out to be slightly different from the nondegeneracy condition required in [21]. In fact the IMP gluing works under the assumption that there are no nontrivial conformal Killing vector fields on $\left(M_{1}, g_{1}\right)$ and $\left(M_{2}, g_{2}\right)$ which vanish at the excised points.

The last step of the overall strategy is the perturbative resolution of the Lichnerowicz equation. In analogy with [21] and [31] this will be done by studying the linearized operator about $g_{\varepsilon}$. Here as well the key point is the obtention of $\varepsilon$-uniform a priori bounds. With these at hand, one can then carry out a fixed point argument which yields a solution to the Lichnerowicz equation. Again, the proof of the uniform a priori bounds requires a sort of non-degeneracy assumption, more precisely we need to suppose that both $\tilde{\Pi}_{1}$ and $\tilde{\Pi}_{2}$ are non identically zero. This is sufficient to guarantee that the linearized Lichnerowicz operators about the original metrics
$$\Delta_{g_{i}}-\left|\mu_{i}\right|_{g_{i}}^{2}-\tau^{2} / m, \quad i=1,2$$
are injective. We remark that, also in this case, for asymptotically Euclidean and asymptotically hyperbolic summands the injectivity of the linearized Lichnerowicz operator will follows directly from a judicious choice of the functional setting, without any further assumption.

Following the strategy summarized above, we can prove the following generalized conformal gluing result

Theorem 1 (Conformal gluing). Let $\left(M_{1}, \tilde{g}_{1}, \tilde{\Pi}_{1}\right)$ and $\left(M_{2}, \tilde{g}_{2}, \tilde{\Pi}_{2}\right)$ be two $m$-dimensional CMC solutions to the Einstein constraint equations (1)-(2) having the same constant mean curvature $\tau$ and such that $M_{i}$ is either compact or $A E$ or $A H$. If for some $i=1,2 M_{i}$ is compact, we further assume that it is nondegenerate and that $\tilde{\Pi}_{i}$ is non identically zero. Let $\left(K, \tilde{g}_{K}\right)$ be a common isometrically embedded $k$-dimensional compact sub-manifold of codimension $n:=m-k \geq 3$ such that the normal bundles of $K$ in $M_{1}$ and in $M_{2}$ are diffeomorphic. Then
\begin{itemize}
\item[(1)] There exists a real number $\varepsilon_{0} \in(0,1)$ such that for every $\varepsilon \in$ $\left(0, \varepsilon_{0}\right)$ it is possible to endow the $\varepsilon$-generalized connected sum $M_{\varepsilon}=$ $M_{1} \sharp_{K, \varepsilon} M_{2}$ of $M_{1}$ and $M_{2}$ along $K$ with a metric $\tilde{g}_{\varepsilon}$ and a second fundamental form $\tilde{\Pi}_{\varepsilon}$ such that the triple $\left(M_{\varepsilon}, \tilde{g}_{\varepsilon}, \tilde{\Pi}_{\varepsilon}\right)$ is still a $\tau$ -CMC solution to the Einstein constraint equations.
\item[(2)] The new metric $\tilde{g}_{\varepsilon}$ and the new symmetric $T T$-tensor $\tilde{\mu}_{\varepsilon}$ tend to the original metric $\tilde{g}_{i}$ and to the original symmetric $T T$-tensor $\tilde{\mu}_{i}$ with
\end{itemize}
respect to the $\mathcal{C}^{r}$-topology on the compact subsets of $M_{i} \backslash K$, for every $r \in \mathbb{N}$ and $i=1,2$, when the geometric parameter $\varepsilon$ tends to zero.
1.2. Localized gluing. Once the conformal gluing is performed, we refine the result of Theorem 1 by showing that one can actually produce new solutions to the Einstein constraints on $M_{\varepsilon}$ which coincide exactly with the starting ones outside a suitable neighborhood of the gluing locus. This will be done by re-gluing the old solutions to the conformally glued ones far enough from the so called poly-neck region.

To present our second issue, we recall that, in analogy with [31], the conformal gluing occurs, for $\varepsilon \leq \varepsilon_{0}<1$, in the regions $K_{1}^{i} \backslash \bar{K}_{\varepsilon}^{i}$, where for an arbitrary $r>0$ we have set
$$K_{r}^{i}:=\left\{m \in M_{i}: m=\exp _{z}^{g_{i}}(x), z \in K, x \in\left(T_{z} K\right)^{\perp},|x|_{g_{i}}<r\right\} .$$
Furthermore, we recall that $\left(\tilde{g}_{\varepsilon}, \tilde{\Pi}_{\varepsilon}\right)$ are conformal deformations of $\left(\tilde{g}_{i}, \tilde{\Pi}_{i}\right)$ on $M_{i} \backslash K_{1}^{i}, i=1,2$. Having these observations in mind, we will show that in generic situations the conformal gluing can be localized. Our second result reads

Theorem 2 (Localized gluing). Let $\varepsilon_{0}<1 / 2$ be small enough so that the boundary's $\partial K_{\varepsilon}^{i}$ are smooth manifolds for $\varepsilon \leq 2 \varepsilon_{0}$. Suppose that there exists $0<\varepsilon_{1} \leq \varepsilon_{0}$ such that the set of KIDs on $\Gamma^{i}\left(\varepsilon_{1}, 2 \varepsilon_{1}\right):=K_{2 \epsilon_{1}}^{i} \backslash \overline{K_{\epsilon_{1}}^{i}}$ is trivial. Then, there exists $\varepsilon_{2} \leq \varepsilon_{1}$ and a family of smooth vacuum initial data sets $\left(M_{\varepsilon}, \hat{g}_{\varepsilon}, \hat{\Pi}_{\varepsilon}\right), \varepsilon \leq \varepsilon_{2}$ such that
$$\left(\hat{g}_{\varepsilon}, \hat{\Pi}_{\varepsilon}\right)=\left(\tilde{g}_{i}, \tilde{\Pi}_{i}\right) \quad \text { on } \quad M_{i} \backslash K_{2 \varepsilon_{1}}^{i} \quad i=1,2$$
and $\left(\hat{g}_{\varepsilon}, \hat{\Pi}_{\varepsilon}\right)$ coincide with $\left(\tilde{g}_{\varepsilon}, \tilde{\Pi}_{\varepsilon}\right)$ in the poly-neck region.
Note that a priori these solutions fail to be CMC in the region $\Gamma^{i}\left(\varepsilon_{1}, 2 \varepsilon_{1}\right)$, $i=1,2$.

To explain better the meaning of our hypothesis we also recall that the KIDs are by definition the elements in the kernel of the $L^{2}$ formal adjoint $D \Phi^{*}(g, \Pi)$ of the linearization at $(g, \Pi)$ of the constraint operator $\Phi(g, \Pi):=$ $(\rho(g, \Pi), J(g, \Pi))$. According to [5], one has that for a generic metric the set of KID's on $\Gamma\left(\varepsilon_{1}, 2 \varepsilon_{1}\right)$ is trivial for all $\varepsilon_{1}$.

Finally, we observe that in the case where the set of KIDs is trivial only on say $\Gamma^{1}\left(\varepsilon_{1}, 2 \varepsilon_{1}\right)$, then the same construction gives initial data sets which coincide with $\left(\tilde{g}_{1}, \tilde{\Pi}_{1}\right)$ on $M_{1} \backslash K_{2 \varepsilon_{1}}^{1}$ and with $\left(\tilde{g}_{\varepsilon}, \tilde{\Pi}_{\varepsilon}\right)$ on $M_{\varepsilon} \backslash\left(M_{1} \backslash K_{\varepsilon_{1}}^{1}\right)$.

\section*{2. The geometric construction}

In this section we briefly present the construction of the approximate solution metrics $g_{\varepsilon}, \varepsilon \in(0,1)$ and the consequent construction of the $g_{\varepsilon}$-trace free 2-tensors $\mu=\mu(\varepsilon)$ via cut-off functions. Even though the construction is local and then it is identical to the one used in [31], we prefer to recall it quickly, in order to fix the notations that will be used throughout the paper.

Let $\left(K, g_{K}\right)$ be a $k$-dimensional compact Riemannian manifold isometrically embedded in both the $m$-dimensional Riemannian manifolds $\left(M_{1}, g_{1}\right)$ and $\left(M_{2}, g_{2}\right)$, we label the embedding maps as follows
$$\iota_{i}: K \hookrightarrow M_{i}, \quad i=1,2 .$$

We assume that the map $\iota_{1}^{-1} \circ \iota_{2}: \iota_{1}(K) \rightarrow \iota_{2}(K)$ is an isometry which extends to a diffeomorphism between the normal bundles of $\iota_{i}(K)$ in $\left(M_{i}, g_{i}\right)$, $i=1,2$. To simplify the notations and the computations, we suppose, without loss of generality, that the injectivity radius of $K$ in both the manifolds is greater than one, so that we are allowed to manipulate the differential and the metric structure of the original solutions in a fixed size one tubular neighborhood of $K$ in both $M_{1}$ and $M_{2}$. This fixed tubular neighborhood will be referred in the following as gluing locus.

For a fixed $\varepsilon \in(0,1)$, we describe the construction of the generalized connected sum of $M_{1}$ and $M_{2}$ along $K$ and the definition of the metric $g_{\varepsilon}$ in local coordinates. The fact that this construction yields a globally defined metric will follow at once.

Let $U^{k}$ be an open set in $\mathbb{R}_{z}^{k}$ an let $B^{n}$ be the $n$-dimensional open ball of radius one in $\mathbb{R}_{x}^{n}$. We recall that $n$ is the codimension of $K$ in $M_{i}$ an verifies $n:=m-k \geq 3$. For $i=1,2$, the map given by
$$F_{i}: U^{k} \times B^{n} \rightarrow W_{i} \subset M_{i}, \quad F_{i}(z, x):=\exp _{(z, 0)}^{g_{i}}(x)$$
defines local Fermi coordinates near the coordinate patches $F_{i}(\cdot, 0)\left(U^{k}\right) \subset$ $\iota_{i}(K) \subset M_{i}$. In these coordinates, the metric $g_{i}$ can be decomposed as
$$g_{(i)}(z, x)=g_{j l}^{(i)} d z^{j} \otimes d z^{l}+g_{\alpha \beta}^{(i)} d x^{\alpha} \otimes d x^{\beta}+g_{j \alpha}^{(i)} d z^{j} \otimes d x^{\alpha},$$
where the coefficients are such that
$$g_{\alpha \beta}^{(i)}=\delta_{\alpha \beta}+\mathcal{O}\left(|x|^{2}\right) \quad \text { and } \quad g_{j \alpha}^{(i)}=\mathcal{O}(|x|) .$$
Also notice that, since $K$ is isometrically embedded in $M_{1}$ and in $M_{2}$, we have that
$$g_{i j}^{(1)}(z, 0)=g_{i j}^{K}(z)=g_{i j}^{(2)}(z, 0) .$$
To define the differential and the metric structure of the generalized connected sum, we consider now, in correspondence to each $\varepsilon \in(0,1)$, the hollow domain $U^{k} \times A^{n}\left(\varepsilon^{2}, 1\right)$, where, for $r, s \in \mathbb{R}^{+}, A^{n}(r, s)$ denotes the $n$-dimensional annulus $\{r<|x|<s\}$. With the notations of the previous chapter we have that
$$F_{i}\left(U^{k} \times A^{n}\left(\varepsilon^{2}, 1\right)\right)=W_{i} \cap \Gamma^{i}\left(\varepsilon^{2}, 1\right), \quad i=1,2 .$$
To identify $W_{1} \cap \Gamma^{1}\left(\varepsilon^{2}, 1\right)$ and $W_{2} \cap \Gamma^{2}\left(\varepsilon^{2}, 1\right)$ it is convenient to set
$$\begin{aligned}
& x=\varepsilon \mathrm{e}^{-t} \theta \quad \text { in } F_{1}^{-1}\left[W_{1} \cap \Gamma^{1}\left(\varepsilon^{2}, 1\right)\right] \\
& x=\varepsilon \mathrm{e}^{t} \theta \quad \text { in } F_{2}^{-1}\left[W_{2} \cap \Gamma^{2}\left(\varepsilon^{2}, 1\right)\right],
\end{aligned}$$
with $\varepsilon \in(0,1), \log \varepsilon<t<-\log \varepsilon, \theta \in S^{n-1}$. Now, it is immediate to check that both $W_{1} \cap \Gamma^{1}\left(\varepsilon^{2}, 1\right)$ and $W_{2} \cap \Gamma^{2}\left(\varepsilon^{2}, 1\right)$ are diffeomorphic to $U^{k} \times$ $(\log \varepsilon,-\log \varepsilon) \times S^{n-1}$ and that $(z, t, \theta)$ yield a local coordinates for $M_{\varepsilon}$, this automatically provides the local definition of the differential structure of $M_{\varepsilon}$. Using these coordinates, the expressions of the two metrics $g_{1}$ and $g_{2}$ become respectively
$$\begin{aligned}
g_{1}(z, t, \theta) & =g_{i j}^{(1)} d z^{i} \otimes d z^{j} \\
& +u_{\varepsilon}^{(1)} \frac{4}{n-2}\left[\left(d t \otimes d t+g_{\lambda \mu}^{(1)} d \theta^{\lambda} \otimes d \theta^{\mu}\right)+g_{t \theta}^{(1)} d t \ltimes d \theta\right] \\
& +g_{i t}^{(1)} d z^{i} \otimes d t+g_{i \lambda}^{(1)} d z^{i} \otimes d \theta^{\lambda}
\end{aligned}$$
and
$$\begin{aligned}
g_{2}(z, t, \theta) & =g_{i j}^{(2)} d z^{i} \otimes d z^{j} \\
& +u_{\varepsilon}^{(2)} \frac{4}{n-2}\left[\left(d t \otimes d t+g_{\lambda \mu}^{(2)} d \theta^{\lambda} \otimes d \theta^{\mu}\right)+g_{t \theta}^{(2)} d t \ltimes d \theta\right] \\
& +g_{i t}^{(2)} d z^{i} \otimes d t+g_{i \lambda}^{(2)} d z^{i} \otimes d \theta^{\lambda},
\end{aligned}$$
where the compact notation $g_{t \theta} d t \ltimes d \theta$ indicates the general component of the normal metric tensor, i.e., a linear combination with smooth coefficients of $d t \otimes d t, d \theta^{\lambda} \otimes d \theta^{\mu}$ and $d t \otimes d \theta^{\lambda}$. The normal conformal factors are given by
$$u_{\varepsilon}^{(1)}(t)=\varepsilon^{\frac{n-2}{2}} \mathrm{e}^{-\frac{n-2}{2} t} \quad \text { and } \quad u_{\varepsilon}^{(2)}(t)=\varepsilon^{\frac{n-2}{2}} \mathrm{e}^{\frac{n-2}{2} t},$$
whereas $g_{\lambda \mu}^{(1)}$ and $g_{\lambda \mu}^{(2)}$ are the coefficients of the round metrics on $S^{n-1}$. Remark that for $j=1,2$ we have
$$\begin{array}{ll}
g_{\lambda \mu}^{(j)}=\mathcal{O}(1) & g_{t \theta}^{(j)}=\mathcal{O}\left(|x|^{2}\right) \\
g_{i t}^{(j)}=\mathcal{O}\left(|x|^{2}\right) & g_{i \lambda}^{(j)}=\mathcal{O}\left(|x|^{2}\right) .
\end{array}$$

We choose now a cut-off function $\chi:(\log \varepsilon,-\log \varepsilon) \rightarrow[0,1]$ which is a non increasing smooth function identically equal to 1 in ( $\log \varepsilon$, -1] and identically equal to 0 in $[1,-\log \varepsilon$ ). We choose then another cut-off function $\eta:(\log \varepsilon,-\log \varepsilon) \rightarrow[0,1]$ which is a non increasing smooth function identically equal to 1 in $(\log \varepsilon,-\log \varepsilon-1]$ and such that $\lim _{t \rightarrow-\log \varepsilon} \eta=0$. Using these two cut-off functions, we can define a new normal conformal factor $u_{\varepsilon}$ by setting
$$u_{\varepsilon}(t):=\eta(t) u_{\varepsilon}^{(1)}(t)+\eta(-t) u_{\varepsilon}^{(2)}(t) .$$
The metric $g_{\varepsilon}$ is then locally defined by
$$\begin{aligned}
g_{\varepsilon}(z, t, \theta) & :=\left(\chi g_{i j}^{(1)}+(1-\chi) g_{i j}^{(2)}\right) d z^{i} \otimes d z^{j} \\
& +u_{\varepsilon}^{\frac{4}{n-2}}\left[d t \otimes d t+\left(\chi g_{\lambda \mu}^{(1)}+(1-\chi) g_{\lambda \mu}^{(2)}\right) d \theta^{\lambda} \otimes d \theta^{\mu}\right. \\
& \left.\quad+\left(\chi g_{t \theta}^{(1)}+(1-\chi) g_{t \theta}^{(2)}\right) d t \ltimes d \theta\right] \\
& +\left(\chi g_{i t}^{(1)}+(1-\chi) g_{i t}^{(2)}\right) d z^{i} \otimes d t \\
& +\left(\chi g_{i \lambda}^{(1)}+(1-\chi) g_{i \lambda}^{(2)}\right) d z^{i} \otimes d \theta^{\lambda} .
\end{aligned}$$

Closer inspection of this expression shows that the only objects that are not a priori globally defined on the identification of the hollow tubular neigh-borhoods (poly-neck) of $\iota_{1}(K)$ in $M_{1}$ and $\iota_{2}(K)$ in $M_{2}$ are the functions $\chi$ and $u_{\varepsilon}$ (since the cut-off $\eta$ is involved in its definition). However, observe that both cut-off functions can easily be expressed as functions of the Riemannian distance to $K$ in the respective manifolds. Hence, they are globally defined and the metric $g_{\varepsilon}$ - whose definition can be obviously completed by setting $g_{\varepsilon} \equiv g_{1}$ and $g_{\varepsilon} \equiv g_{2}$ out of the poly-neck - is a Riemannian metric which is globally defined on the manifold $M_{\varepsilon}$.

We conclude this section with the definition of the 'proto-TT-tensor' $\mu=$ $\mu(\varepsilon)$. This is a $g_{\varepsilon}$-trace free symmetric 2-tensor which in the next section will
be corrected to a $g_{\varepsilon}$-TT-tensor by adding an $\varepsilon$-uniformly bounded term of the form $D_{g_{\varepsilon}} X$, as anticipated in the introduction. To define $\mu$ we describe a warped cut off procedure on the side of the polyneck coming from $M_{1}$. The same manipulation on the other side provides us with the complete definition of $\mu$. Let then $\mu_{1}$ be the given $g_{1}$-trace-free symmetric tensor on $M_{1}$. In local coordinates this reads
$$g_{i j}^{(1)} \mu_{1}^{i j}+2 g_{i \alpha}^{(1)} \mu_{1}^{i \alpha}+g_{\alpha \beta}^{(1)} \mu_{1}^{\alpha \beta}=0 .$$
We are looking for a symmetric tensor $\mu$ which is trace free with respect to the metric $g_{\varepsilon}$. To do that we set
$$\begin{aligned}
\mu^{i j} & =a(t) \cdot \mu_{1}^{i j} \\
\mu^{i \alpha} & =a(t) \cdot \mu_{1}^{i \alpha} \\
\mu^{\alpha \beta} & =b(t) \cdot \mu_{1}^{\alpha \beta},
\end{aligned}$$
where $a$ and $b$ are smooth radial cut-off functions which are equal to one on $M_{1}$ and which vanish for $t>c \log \varepsilon+1$, where $0<c<1$ is a constant that will be determined in Section 4. The definitions of $a$ and $b$ are made more precise below. However, we remark that the warped cut-off still guarantees the symmetry of $\mu$. Taking into account (16) and the definition of the metric $g_{\varepsilon}$ on the region where $\mu$ is not identically zero, the condition $\operatorname{tr}_{g_{\varepsilon}} \mu=0$ is equivalent to
$$0=a g_{i j}^{(1)} \mu_{1}^{i j}+2 a g_{i \alpha}^{(1)} \mu_{1}^{i \alpha}+b \phi^{2} g_{\alpha \beta}^{(1)} \mu_{1}^{\alpha \beta}=\left[b \phi^{2}-a\right] \cdot g_{\alpha \beta}^{(1)} \mu_{1}^{\alpha \beta},$$
where the normal conformal factor $\phi^{2}$ defined by
$$\phi^{2}:=\left[1+\eta(-t) \cdot\left(u_{\varepsilon}^{(2)} / u_{\varepsilon}^{(1)}\right)\right]^{\frac{4}{n-2}} .$$

It is now straightforward to verify that one can always choose two smooth cut-off functions satisfying the conditions above and such that $a=\phi^{2} b$. In particular we will choose $b \equiv 1$, for $\log \varepsilon<t<c \log \varepsilon$. As a consequence, $a=b+\mathcal{O}\left(\mathrm{e}^{(n-2) t}\right)$ on this interval and $\mu$ converges to $\mu_{1}$ on the compact sets of $M_{1} \backslash K$ with respect to the $\mathcal{C}^{2}$-topology.

Notice that since $\phi$ depends on $\varepsilon$, also $a$ and $b$ depend on $\varepsilon$. Nevertheless, they and their derivatives do admit an $\varepsilon$-uniform bound. Finally, let us observe that $\left|\operatorname{div}_{g_{\varepsilon}} \mu\right|_{g_{\varepsilon}}$ and $\left|\nabla \operatorname{div}_{g_{\varepsilon}} \mu\right|_{g_{\varepsilon}}$ are $\mathcal{O}\left(\varepsilon^{n-2}\right)$ near the boundary of the poly-neck and $\varepsilon$-uniformly bounded in the interior.

\section*{3. The momentum constraint: existence of solutions}

The aim of this section is to provide existence and uniform a priori estimates for solutions to the equation
$$L_{g_{\varepsilon}} X=\sharp \operatorname{div}_{g_{\varepsilon}} \mu \quad \text { in } M_{\varepsilon},$$
where $g_{\varepsilon}$ and $\mu$ are respectively the approximate solution metric and the approximate symmetric TT-tensor defined in the previous section. According to the strategy explained in the introduction, we will then obtain a family of TT-tensor by setting $\mu_{\varepsilon}:=\mu+D_{g_{\varepsilon}} X$. We recall that the vector Laplacian - is defined as $L_{g_{\varepsilon}}:=\left(D_{g_{\varepsilon}}\right)^{*} \cdot D_{g_{\varepsilon}}=-\sharp \operatorname{div}_{g_{\varepsilon}} \cdot D_{g_{\varepsilon}}$. As it is easy to verify, $L_{g_{\varepsilon}}$ is a linear elliptic second order partial differential operator with smooth
coefficients and it is formally self-adjoint. We can think of the vector Laplacian as acting between the spaces of sections of the tangent bundle with Hölder regularity
$$L_{g_{\varepsilon}}: \mathcal{C}^{k+2, \alpha}\left(M_{\varepsilon}, T M_{\varepsilon}\right) \longrightarrow \mathcal{C}^{k, \alpha}\left(M_{\varepsilon}, T M_{\varepsilon}\right) .$$
We recall that for a general tensor field $T$ the $\mathcal{C}^{k}$ norm of $T$ is defined by
$$\|T\|_{\mathcal{C}^{k}}:=\sum_{j=0}^{k} \sup _{M_{\varepsilon}}\left|\nabla^{j} T\right|_{g_{\varepsilon}},$$
where ∇ is the Levi-Civita connection of $g_{\varepsilon}$, whereas the Hölder seminorm of the $k$-th derivative with Hölder exponent $\alpha \in(0,1)$ is defined by
$$\left[\nabla^{k} T\right]_{\alpha}:=\sup _{p \neq q} \frac{\left|\nabla^{k} T(p)-\nabla^{k} T(q)\right|_{g_{\varepsilon}}}{d_{g_{\varepsilon}}(p, q)^{\alpha}},$$
where the distance $d_{g_{\varepsilon}}(p, q)$ is supposed to be smaller than the injectivity radius and, with abuse of notation, the term $\nabla^{k} T(q)$ is interpreted as its parallel transport from $q$ to $p$ along the unique geodesic joining $p$ and $q$ (in order to give sense to the subtraction which appears in the numerator above). The definition of the $\mathcal{C}^{k, \alpha}$-Hölder norm is then given by
$$\|T\|_{\mathcal{C}^{k, \alpha}}:=\|T\|_{\mathcal{C}^{k}}+\left[\nabla^{k} T\right]_{\alpha} .$$

As explained in [31], the existence of solutions to (17) in the compact case (i.e., when both the summands $M_{1}$ and $M_{2}$ are compact and hence $M_{\varepsilon}$ itself is compact) is an easy consequence of the Fredholm alternative. In fact, using integration by parts, it is immediate to check that the right hand side $\sharp \operatorname{div}_{g_{\varepsilon}} \mu$ is $L^{2}$-orthogonal to $\operatorname{Ker} L_{g_{\varepsilon}}^{*}$. The Hölder regularity of the solution follows then from standard elliptic regularity theory.

In the non compact case we need to use a more sophisticated functional setting in order to provide existence. More precisely, we are going to recall the definitions of asymptotically Euclidean (AE) and asymptotically hyperbolic (AH) Riemannian manifold, together with the notion of weighted Hölder spaces (at infinity). In this context it will be possible to quote some well known result about the mapping properties of the vector Laplacian, insuring the existence of solutions to equation (17) also in the non compact case.
3.1. Asymptotically Euclidean manifold. An asymptotically Euclidian (AE) Riemannian manifold $(M, g)$ is a manifold $M$ with a finite number of ends, each of them being diffeomorphic to the exterior of a ball in $\mathbb{R}^{n}$, and such that, up to this diffeomorphism, the components of the metric on each end verifies
$$\left|g_{i j}-\delta_{i j}\right| \leq C r^{-\nu},$$
along with appropriate decay of the derivatives. Here $\nu>0$ and $r$ is a function which is equal to the standard radius of $\mathbb{R}^{n}$ on each end and which is equal to the constant 1 on the remaining compact region of $M$.

The weighted Hölder spaces $r^{-\nu} C_{A E}^{k, \alpha}$ are given by the tensor fields such that the norm
$$\|\cdot\|_{C_{-\nu}^{k, \alpha}}:=\left\|r^{\nu} \cdot\right\|_{C^{k, \alpha}}$$
is well definite and finite. Roughly speaking a function (or a tensor field) $u$ is in $r^{-\nu} C_{A E}^{k}$ if $u \in C_{\text {loc }}^{k}$ and on each end $\nabla^{l} u=O\left(r^{-\nu-l}\right)$, for all $l \leq k$. For further references on this topic, we point out that the spaces defined here coincide with the spaces denoted by $\Lambda_{A E}^{k, \alpha}$ in [21].

Since the model we want to reproduce is the 'horizontal' Euclidean slice in Minkowski space, we will assume that $\tau=0$, when at least one of the two summands in $M_{\varepsilon}$ is AE. Because of the nature of the Hamiltonian constraint it is also natural to assume that
$$\mu \in r^{-\nu / 2-1} C_{A E}^{k, \alpha}(M, T M \otimes T M)$$
in this case.
Before going to the isomorphism results, we recall that on an AE manifold $(M, g)$ the relevant part of the operator $L_{g}$ at infinity is given by
$$L_{\mathbb{R}^{m}}:=-\frac{1}{2} \Delta_{\mathbb{R}^{m}}+\frac{m-2}{2 m} \operatorname{grad}_{\mathbb{R}^{m}} \circ \operatorname{div}_{\mathbb{R}^{m}} .$$
where the differential operators on the right hand side are computed with respect to the Euclidean metric, with the agreement that the Laplace operator here acts on each component of the vector field.

Now, exactly as in [21, Proposition 13], we have
Proposition 3. Suppose that $(M, g)$ is an $m$-dimensional $A E$ Riemannian manifold with $2-m<-\nu<0$, then the vector Laplacian
$$L_{g}: r^{-\nu} C_{A E}^{k+2, \alpha}(M, T M) \longrightarrow r^{-\nu-2} C_{A E}^{k, \alpha}(M, T M)$$
is an isomorphism for every $k \in \mathbb{N}$.
Proof. See [21], we just mention a misprint in the proof of Proposition 13, the paper cited as the number [9] seems to be in fact the number [8] so [7] for us, especially Lemma 3.1 and Theorem 3.5 there, see also [3]. \(\square\)

In the following, when at least one of the two components of $M_{\varepsilon}$ is AE (and then $M_{\varepsilon}$ itself is AE), we will systematically make use of the weighted functional setting introduced above in order to recover existence of solution to the equation (17).
3.2. Asymptotically Hyperbolic manifold. An asymptotically hyperbolic (AH) manifold $(M, g)$ is the interior $M$ of a compact manifold $\bar{M}$ with boundary $\partial M$, endowed with a metric $g=y^{-2} \bar{g}$, where $\bar{g}$ is a metric on $\bar{M}$ and $y$ is a defining function of the boundary $\partial M=y^{-1}(\{0\})$ such that $|d y|_{\bar{g}}=1$ on $\partial M$. The terminology comes from the fact that, under this assumption, the sectional curvatures of $(M, g)$ goes to -1 when approaching $\partial M$.

For a precise definition of the weighted Hölder spaces in the asymptotically hyperbolic context, we refer the reader to [21], with the only observation that the Hölder spaces denoted here by $y^{\nu} C_{A H}^{k, \alpha}$ coincide with $y^{\nu} \Lambda_{A H}^{k, \alpha}$ in [21]. Hence, formally, a function (or tensor field) $u$ is in $y^{\nu} C_{A H}^{k, \alpha}$ if $u \in C_{l o c}^{k, \alpha}$ and, for all $l \leq k, \bar{\nabla}^{(l)} u=O\left(y^{\nu+l}\right)$ near $\partial M$.

Since the model we want to reproduce, is the 'horizontal' hyperbolic slice $\mathbb{H}^{n}$ in Minkowski space, we will assume $\tau=m$, when at least one of the
summands in the generalized connected sum is an AH manifold. Again, the Hamiltonian constraint suggests the assumption
$$\mu \in y^{-1} C_{A H}^{k, \alpha}(M, T M \otimes T M) .$$
The isomorphism result in the AH context (see [21] Proposition 16) reads
Proposition 4. Suppose that $(M, g)$ is an $m$-dimensional $A H$ Riemannian manifold and suppose $0<\nu<m+1$, then the vector Laplacian
$$L_{g}: y^{\nu} C_{A H}^{k+2, \alpha}(M, T M) \longrightarrow y^{\nu} C_{A H}^{k, \alpha}(M, T M)$$
is an isomorphism for every $k \in \mathbb{N}$.
Proof. See [1], [22], and also [16]. \(\square\)

In the following, when at least one of the two components of $M_{\varepsilon}$ is AH (and then $M_{\varepsilon}$ itself is AH), we will systematically make use of the weighted functional setting introduced above in order to recover existence of solution to the equation (17).

\section*{4. The momentum constraint: uniform a priori bound}

In this section we will provide solutions to equation (17) with a priori bounds which do not depend on the parameter $\varepsilon$. In analogy with [31], this fact turns out to be crucial in the analysis of the Lichnerowicz equation, since it will allow us to control the squared pointwise norm of $\mu_{g_{\varepsilon}}=\mu+D_{g_{\varepsilon}} X$ in terms of the norm of $\mu$, which can be explicitly estimated.

It is clear that when $\varepsilon$ tends to zero the geometry of the underlying manifold $M_{\varepsilon}$ becomes closer and closer to a degenerate configuration, since the poly-neck size is shrinking down. On the other hand, it is clear that this phenomenon only takes place on the poly-neck region. Thus, to obtain the desired uniform bound, it is convenient to pass to a more sophisticated functional framework, by modifying the usual norms on the poly-neck region. We introduce then a weighting function $\rho_{\varepsilon}$ by setting $\rho_{\varepsilon} \equiv 1$ on $M_{i} \backslash K_{1}^{i}$, $i=1,2$, and $\rho_{\varepsilon}:=\varepsilon \cosh t$ for $(\log \varepsilon)+1<t<-(\log \varepsilon)-1$, where $t$ is the poly-neck variable introduced in Section 2. To complete the definition, we further assume $\rho_{\varepsilon}$ to be a monotone radial smooth interpolation between these regions.

Now, for $k \in \mathbb{N}, \alpha \in(0,1)$ and a weight parameter $\gamma \in \mathbb{R}$, we define the weighted $\mathcal{C}^{k}$-norms and the weighted Hölder $(k, \alpha)$-seminorms of a tensor field $T$ on ( $M_{\varepsilon}, g_{\varepsilon}$ ). Let us set
$$\begin{aligned}
\|T\|_{\mathcal{C}_{\gamma}^{k}} & :=\sum_{j=0}^{k} \sup _{M_{\varepsilon}} \rho_{\varepsilon}^{-\gamma+j} \cdot\left|\nabla^{j} T\right|_{g_{\varepsilon}} \\
{\left[\nabla^{k} T\right]_{\alpha, \gamma} } & :=\sup _{p \neq q}\left|\rho_{\varepsilon}(p) \wedge \rho_{\varepsilon}(q)\right|^{-\gamma+k} \cdot \frac{\left|\nabla^{k} T(p)-\nabla^{k} T(q)\right|_{g_{\varepsilon}}}{d_{g_{\varepsilon}}(p, q)^{\alpha}},
\end{aligned}$$
where ∇ indicates the Levi-Civita connection of $g_{\varepsilon},\left|\rho_{\varepsilon}(p) \wedge \rho_{\varepsilon}(q)\right|$ is the minimum between $\rho_{\varepsilon}(p)$ and $\rho_{\varepsilon}(q)$, and the conventions used in (20) to define the Hölder ratio are still valid here. The weighted Hölder norm is then defined as
$$\|T\|_{\mathcal{C}_{\gamma}^{k, \alpha}}:=\|T\|_{\mathcal{C}_{\gamma}^{k}}+\left[\nabla^{k} T\right]_{\alpha, \gamma} .$$

The $C_{\gamma}^{k, \alpha}$-Hölder space is given by the tensor fields on $M_{\varepsilon}$ with $(k, \alpha)$ -regularity such that the above norm is well defined and finite.

We point out that for any fixed $\varepsilon$ such a norm is equivalent to the standard $C^{k, \alpha}$-Hölder norm and thus the weighted spaces introduced here coincide with the usual $C^{k, \alpha}$-Hölder spaces, since the standard definition has been modified only on a compact region. Nevertheless, these new spaces will reveal to be the suitable ones in the analysis of the singular limit for $\varepsilon \rightarrow 0$.

To treat all the possible situations at once, we denote by $E_{\delta}^{k, \alpha}\left(M_{\varepsilon}, T M_{\varepsilon}\right)$ the space of vector fields on $M_{\varepsilon}$ with $(k, \alpha)$-regularity endowed with $\delta$ -weighted norm in the poly-neck region, $\delta \in \mathbb{R}$, and eventually with the suitable $\nu$-weighted norm on the AE or AH ends. Of course, the weight parameter $\nu$ at infinity is fixed according to the conventions of the previous section. Moreover, the fact that for any fixed $\varepsilon$ the $C_{\delta}^{k, \alpha}$-norm is equivalent to the $C^{k, \alpha}$-norm insures that the isomorphism results still hold true in both the compact and the non compact case. In this context it is convenient to think of $L_{g_{\varepsilon}}$ as acting between the spaces
$$L_{g_{\varepsilon}}: E_{\delta}^{k+2, \alpha}\left(M_{\varepsilon}, T M_{\varepsilon}\right) \longrightarrow E_{\delta-2}^{k, \alpha}\left(M_{\varepsilon}, T M_{\varepsilon}\right),$$
for a suitable weight $\delta \in \mathbb{R}$. We can now state the following:
Proposition 5. Let $X \in E_{\delta}^{k+2, \alpha}\left(M_{\varepsilon}, T M_{\varepsilon}\right)$ and $W \in E_{\delta-2}^{k, \alpha}\left(M_{\varepsilon}, T M_{\varepsilon}\right)$ be vector fields satisfying the equation $L_{g_{\varepsilon}} X=W$. Moreover, suppose that $W$ is of the form $W=\sharp \operatorname{div}_{g_{\varepsilon}} \mu$, for some symmetric 2-tensor $\mu$. Then for any $2-n<\delta<(2-n) / 2$, there exist a real number $\varepsilon_{0} \in(0,1)$ and a positive constant $C>0$ such that for every $\varepsilon \in\left(0, \varepsilon_{0}\right)$
$$\|X\|_{E_{\delta}^{k+2, \alpha}} \leq C \cdot\|W\|_{E_{\delta-2}^{k, \alpha}} .$$
(Remember that $n$ is the codimension of $K$ in $M_{i}, i=1,2$ and it is supposed to be at least 3).

Proof. The proof is analogous to the prove of [31, Proposition 2]. Nevertheless, we recall it here in oder to discuss the changes which are needed in the non compact cases, and possibly to simplify the argument. Here we only prove the uniform weighted $C^{0}$-bound, namely
$$\|X\|_{E_{\delta}^{0}} \leq C \cdot\|W\|_{E_{\delta-2}^{0}} .$$
The estimate (23) will follow from local Schauder estimates for elliptic systems in divergence form (see [15], here we take advantage of the fact that $\left.W=\sharp \operatorname{div}_{g_{\varepsilon}} \mu\right)$ combined with standard scaling arguments.

We proceed by contradiction. If (24) does not hold, then it is possible to find a sequence $\left(\varepsilon_{j}, X_{j}, W_{j}\right), j \in \mathbb{N}$, such that
\begin{itemize}
\item[(1)] $\varepsilon_{j} \rightarrow 0, \quad j \rightarrow+\infty$
\item[(2)] $L_{\varepsilon_{j}} X_{j}=W_{j}, \quad j \in \mathbb{N}$
\item[(3)] $\left\|X_{j}\right\|_{E_{\delta}^{0}}=1, \quad j \in \mathbb{N} \quad$ and $\quad\left\|W_{j}\right\|_{E_{\delta-2}^{0}} \rightarrow 0, \quad j \rightarrow+\infty$.
\end{itemize}
For every $j \in \mathbb{N}$ we consider now a point $p_{j} \in M_{\varepsilon_{j}}$ such that the pointwise norm $\left|X_{j}\right|\left(p_{j}\right)$ eventually multiplied by weighting function raised to the power indicated by the weight is greater or equal than $1-\varepsilon_{j}$. For example, if the point $p_{j}$ lies in the region where $\rho_{j}$ is different from 1, we are assuming that $\rho_{j}^{-\delta}\left|X_{j}\right|\left(p_{j}\right) \geq 1-\varepsilon_{j}$. If $M_{\varepsilon_{j}}$ has an AE end and the point $p_{j}$ is near
infinity, we are assuming that $r^{\nu}\left|X_{j}\right|\left(p_{j}\right) \geq 1-\varepsilon_{j}$ and so on. The fact that one can find such a point for each $j \in \mathbb{N}$ follows from the third hypothesis in the argument by contradiction. Depending on the behavior of the sequence $\left\{p_{j}\right\}$, we are going to distinguish several cases.

Case 1a. Suppose that up to a subsequence the points $p_{j}$ 's lie in a compact region of $M_{i} \backslash K$ for some $i=1,2$. Without loss of generality we only consider the case $i=1$, since the other one is identical.

In analogy with [31], we have that as $j \rightarrow+\infty$, the sequence of vector fields $X_{j}$ converges to a nontrivial weak solution $X$ of the homogeneous problem
$$\left\{\begin{array}{l}
L_{g_{1}} X=0 \quad \text { on } M_{1} \backslash K \\
|X|_{g_{1}}(\cdot) \leq A\left|d_{g_{1}}(\cdot, K)\right|^{\delta}
\end{array}\right.$$
where $d_{g_{1}}(\cdot, K)$ represents the Riemannian distance to the submanifold $K$, and $A>0$ is a positive constant. Without discussing all the details, we just recall that this follows from the fact that in our geometric construction the metrics $g_{\varepsilon}$ 's converge to the original metric $g_{1}$ on the compact subset of $M_{1} \backslash K$. The growth prescription near $K$ is a direct consequence of the weighted setting introduced on the poly-neck region.

As it is easy to verify, the condition $2-n<\delta$ guarantees that $X$ verifies the equation $L_{g_{1}} X=0$ on the whole $M_{1}$ in the sense of distributions, and thanks to the elliptic regularity we deduce that $X$ can be extended through the singular set $K$ to a nontrivial smooth solution of $L_{g_{1}} X=0$. If $M_{1}$ is either AE or AH this contradicts the isomorphism results discussed in the previous section. If $M_{1}$ is compact, we integrate by parts obtaining
$$0=\left(L_{g_{1}} X, X\right)_{L^{2}}={ }^{g_{1}}\left\|D_{g_{1}} X\right\|_{L^{2}}^{2} .$$
Hence $X$ is a nontrivial conformal Killing vector field on $M_{1}$, which is excluded by the nondegeneracy condition.

Case 1b. Suppose that $M_{\varepsilon}$ is non compact and that, up to a subsequence, the points $p_{j}$ leave every compact subset of $M_{\varepsilon}$. Again, without loss of generality, we assume that the points $p_{j}$ 's of the subsequence lie on the piece of $M_{\varepsilon}$ coming from $M_{1}$.

For every fixed compact subset $Q$ of $M_{1}$ we can suppose that $\rho_{j}^{-\delta}\left|X_{j}\right| \rightarrow 0$ on $Q$ when $j \rightarrow+\infty$, otherwise we are either in Case 1a discussed above or in Case 2 or 3 discussed below. We consider now a cut-off function $\varphi$ which is identically equal to 1 on $M_{1} \backslash K_{2}^{1}$ and which vanishes on $K_{1}^{1}$, with the notations introduced in the introduction. Setting $Y_{j}:=\varphi X_{j}$ and $Z_{j}:=\varphi W_{j}+\left[L_{j}, \varphi\right] X_{j}$, where $[\cdot, \cdot \cdot]$ is the formal commutator, we obtain $L_{g_{1}} Y_{j}=Z_{j}$. Moreover, for every $j \in \mathbb{N}$, both the vector fields $Y_{j}$ and $Z_{j}$ can be regarded as vector fields defined on $M_{1}$. Furthermore, using the second part of hypothesis 3 together with local Schauder estimates on $K_{2}^{1}$, it is easy to deduce that $Z_{j} \rightarrow 0$ in $E_{0}^{0}\left(M_{1}, T M_{1}\right)$, as $j \rightarrow 0$. On the other hand $\left\|X_{j}\right\|_{E_{0}^{0}\left(M_{1}, T M_{1}\right)} \geq 1 / 2$ for large enough $j$. This contradicts the isomorphism results of the previous section.

Case 2. Suppose that up to a subsequence and without loss of generality the points $p_{j}$ 's verify $d_{g_{1}}\left(p_{j}, K\right)=\mathcal{O}\left(\varepsilon_{j}\right)$, as $j \rightarrow+\infty$. This means that they are converging to $K$ with the largest velocity allowed.

Performing the same blow-up as in [31, Proposition 2], we have that the vector fields $X_{j}$ converge to a nontrivial weak solution $X$ of the homogeneous problem
$$\left\{\begin{array}{l}
L_{\mathbb{R}^{k} \times \mathbb{S}^{n}} X \quad \text { on } \mathbb{R}_{z}^{k} \times \mathbb{S}_{t, \theta}^{n} \\
|X|_{\mathbb{R}^{k} \times \mathbb{S}^{n}} \leq B \quad(\cosh t)^{\delta}
\end{array}\right.$$
where $B>0$ is a positive constant and $\mathbb{S}^{n}$ denotes the $n$-dimensional (Riemannian) Schwarzschild space, $n \geq 3$. For sake of completeness we recall that the space $\mathbb{S}^{n}$ is diffeomorphic to the standard cylinder $\mathbb{R}_{t} \times S_{\theta}^{n-1}$ and it is endowed with the metric
$$g_{\mathbb{S}^{n}}=\left[\cosh \left(\frac{n-2}{2} t\right)\right]^{\frac{4}{n-2}} \cdot d t^{2}+g_{S^{n-1}} .$$
We also point out that the expressions $L_{\mathbb{R}^{k} \times \mathbb{S}^{n}}$ and $|\cdot|_{\mathbb{R}^{k} \times \mathbb{S}^{n}}$ indicate respectively the vector Laplacian and the pointwise norm of the product metric $g_{\mathbb{R}^{k}}+g_{\mathbb{S}^{n}}$.

In order to simplify the argument presented in [31] and getting the desired contradiction, we split the vector field $X$ into the $T \mathbb{R}^{k}$ component and the $T \mathbb{S}^{n}$ component. Thus, we write $X=U+V$, where
$$U=U^{j}(z, t, \theta) \cdot e_{j} \quad \text { and } \quad V=V^{t}(z, t, \theta) \frac{\partial}{\partial t}+V^{\mu}(z, t, \theta) \frac{\partial}{\partial \theta^{\mu}} .$$
Here $\left\{e_{1}, \ldots, e_{k}\right\}$ is the standard basis on $T \mathbb{R}^{k} \simeq \mathbb{R}^{k}$. The action of $L_{\mathbb{R}^{k} \times \mathbb{S}^{n}}$ is then given by
$$\begin{aligned}
& L_{\mathbb{R}^{k} \times \mathbb{S}^{n}} X= \\
& \left(\begin{array}{cc}
L_{\mathbb{R}^{k}}-\frac{1}{2} \Delta_{\mathbb{S}^{n}} & -\left(\frac{m-2}{2 m}\right) \operatorname{grad}_{\mathbb{R}^{k}} \circ \operatorname{div}_{\mathbb{S}^{n}} \\
-\left(\frac{m-k}{k m}\right) \operatorname{grad}_{\mathbb{R}^{k}} \circ \operatorname{div}_{\mathbb{R}^{k}} & \\
-\left(\frac{m-2}{2 m}\right) \operatorname{grad}_{\mathbb{S}^{n}} \circ \operatorname{div}_{\mathbb{R}^{k}} & L_{\mathbb{S}^{n}}-\frac{1}{2} \Delta_{\mathbb{R}^{k}} \\
& -\left(\frac{m-n}{n m}\right) \operatorname{grad}_{\mathbb{S}^{n} \circ \operatorname{div}_{\mathbb{S}^{n}}(\cdot)}
\end{array}\right)\binom{U}{V}
\end{aligned}$$
where $\Delta_{g} W$ indicates the (negative definite) Laplace-Beltrami operator of a Riemannian metric $g$ applied to the components of the vector field $W$.

We observe that, by the elliptic regularity, the components $U^{j}, V^{t}$ and $V^{\mu}$ are smooth functions which verify the decay prescription when $|t| \rightarrow+\infty$ and which are uniformly bounded in the $z$-direction. To proceed with the analysis, it is then convenient to consider these components as $C_{\delta}^{2, \alpha}$-valued tempered distributions, namely as elements in
$$\mathcal{S}^{\prime}\left(\mathbb{R}^{k}, C_{\delta}^{2, \alpha}\left(\mathbb{S}^{n}\right)\right) .$$
Now, we are going to take the Fourier transform along the $z$ variable
$$\hat{U}=\hat{U}^{j}(\zeta, t, \theta) \cdot e_{j} \quad \text { and } \quad \hat{V}=\hat{V}^{t}(\zeta, t, \theta) \frac{\partial}{\partial t}+\hat{V}^{\mu}(\zeta, t, \theta) \frac{\partial}{\partial \theta^{\mu}} .$$
Notice that $\hat{U}$ and $\hat{V}$ verify the decay prescriptions
$$|\hat{U}|_{\mathbb{R}^{k}}(\zeta, t, \theta) \leq B(\cosh t)^{\delta} \quad \text { and } \quad|\hat{V}|_{\mathbb{S}^{n}}(\zeta, t, \theta) \leq B(\cosh t)^{\delta}$$
along with their derivatives.
We have now at hand the family of operators $\hat{L}(\zeta)$ acting on $\hat{X}(\zeta, t, \theta)=$ $\hat{U}(\zeta, t, \theta)+\hat{V}(\zeta, t, \theta)$ in the following way
$$\hat{L}(\zeta) \hat{X}=\left(\begin{array}{cc}
-\frac{1}{2} \Delta_{\mathbb{S}^{n}}+\frac{1}{2}|\zeta|^{2} & -i\left(\frac{m-2}{2 m}\right) \operatorname{div}_{\mathbb{S}^{n}}(\cdot) \zeta \\
+\left(\frac{m-2}{2 m}\right)\langle\zeta, \cdot\rangle \zeta & \\
-i\left(\frac{m-2}{2 m}\right) \operatorname{grad}_{\mathbb{S}^{n}}\langle\zeta, \cdot\rangle & L_{\mathbb{S}^{n}}+\frac{1}{2}|\zeta|^{2} \\
-\left(\frac{m-n}{n m}\right) \operatorname{grad}_{\mathbb{S}^{n}} \circ \operatorname{div}_{\mathbb{S}^{n}}(\cdot)
\end{array}\right)\binom{\hat{U}}{\hat{V}}$$
Clearly $\hat{L}(\zeta) \hat{X}=0$. If we show that, for every $\zeta \in \mathbb{R}^{k}, \hat{L}(\zeta) \hat{X}=0$ implies $\hat{X}=0$, we will also have that $X$ must be identically 0 , reaching a contradiction. To show that this is actually the case, we are going to integrate by parts the expression
$$0=(\hat{L}(\zeta) \hat{X}, \hat{X})_{L^{2}} .$$
A direct computation shows that
$$\begin{aligned}
0= & \int_{\mathbb{S}^{n}} \sum_{j=1}^{k}\left|\operatorname{grad}_{\mathbb{S}^{n}} \hat{U}^{j}\right|_{\mathbb{S}^{n}}^{2}+\left(\frac{m-2}{m}\right)|\langle\zeta, \hat{U}\rangle|^{2}+|\zeta|^{2}|\hat{U}|_{\mathbb{R}^{k}}^{2} d v o l_{\mathbb{S}^{n}} \\
& +\int_{\mathbb{S}^{n}} 2\left|D_{\mathbb{S}^{n}} \hat{V}\right|_{\mathbb{S}^{n}}^{2}+2\left(\frac{m-n}{n m}\right)\left|\operatorname{div}_{\mathbb{S}^{n}} \hat{V}\right|_{\mathbb{S}^{n}}^{2}+|\zeta|^{2}|\hat{V}|_{\mathbb{S}^{n}}^{2} d v o l_{\mathbb{S}^{n}} \\
& -\left.\lim _{T \rightarrow+\infty} \int_{S^{n-1}} \sum_{j=1}^{k} \hat{U}^{j} \partial_{t} \hat{U}^{j}\left[\cosh \frac{n-2}{2} t\right]^{2}\right|_{-T} ^{+T} d v o l_{S^{n-1}} \\
& -\left.\lim _{T \rightarrow+\infty} 2\left(\frac{m-n}{n m}\right) \int_{S^{n-1}} \hat{V}^{t} \operatorname{div}_{\mathbb{S}^{n}} \hat{V}\left[\cosh \frac{n-2}{2} t\right]{ }^{\frac{2 n}{n-2}}\right|_{-T} ^{+T} d v o l_{S^{n-1}} \\
& -\left.\lim _{T \rightarrow+\infty} 2 \int_{S^{n-1}} D_{\mathbb{S}^{n}} \hat{V}\left(\hat{V}, \partial_{t}\right)\left[\cosh \frac{n-2}{2} t\right]^{2}\right|_{-T} ^{+T} d v o l_{S^{n-1}} \\
& -\left.\lim _{T \rightarrow+\infty} i\left(\frac{m-2}{m}\right) \int_{S^{n-1}} \hat{V}^{t}\langle\zeta, \hat{U}\rangle\left[\cosh \frac{n-2}{2} t\right]^{\frac{2 n}{n-2}}\right|_{-T} ^{+T} d v o l_{S^{n-1}} .
\end{aligned}$$
Using the decay prescription and remembering that $\delta<(2-n) / 2$ it is immediate to check that first three boundary terms tend to zero as $T \rightarrow+\infty$. Moreover, when $\zeta=0$, also the last boundary term gives no contribution and we deduce immediately that $\hat{U}$ is constant and $\hat{V}$ is a conformal Killing vector field on $\mathbb{S}^{n}$. Since they decay at infinity, they must vanish everywhere, leading us to a contradiction.

Hence we suppose now $\zeta \neq 0$ and we show that also in this case the contribution of the last boundary term is zero. First we observe that the component $\hat{V}^{t}$ is controlled by $(\cosh t)^{\delta-1}$, whereas a priori the bound on $|\hat{U}|_{\mathbb{R}^{k}}$ is just given by $(\cosh t)^{\delta}$. Since the third factor in the last integral goes like $(\cosh t)^{n}$, this is in general not sufficient to guarantee the vanishing of the entire boundary term in the limit for $T \rightarrow+\infty$. To overcome this difficulty, we are going to show that the decay of $\hat{U}$ is better than expected. In fact, from $\hat{L}(\zeta) \hat{X}=0$ we have that
$$\Delta_{\mathbb{S}^{n}} \hat{U}-|\zeta|^{2} \hat{U}-\left(\frac{m-2}{m}\right)\langle\zeta, \hat{U}\rangle \zeta=-i\left(\frac{m-2}{m}\right)\left(\operatorname{div}_{\mathbb{S}^{n}} \hat{V}\right) \zeta .$$
Multiplying this equation by a vector $\eta \in \mathbb{R}^{k}$ with $\langle\eta, \zeta\rangle=0$, we obtain
$$\Delta_{\mathbb{S}^{n}}\langle\hat{U}, \eta\rangle-|\zeta|^{2}\langle\hat{U}, \eta\rangle=0 .$$

Since $\hat{U}$ decays at infinity, we can use the maximum principle to deduce that $\langle\hat{U}, \eta\rangle=0$ everywhere on $\mathbb{S}^{n}$. As a consequence we write the vector field $\hat{U}(\zeta, t, \theta)$ as $u(\zeta, t, \theta) \zeta$, where $u$ is a suitable function verifying the decay prescriptions induced by $\hat{U}$. The equation above becomes then
$$\Delta_{\mathbb{S}^{n}} u-\left(\frac{2 m-2}{m}\right)|\zeta|^{2} u=-i\left(\frac{m-2}{m}\right)\left(\operatorname{div}_{\mathbb{S}^{n}} \hat{V}\right) .$$
In order to split this equation into its real part and its pure imaginary part, we set $u=\phi+i \psi$ and $\operatorname{div}_{\mathbb{S}^{n}} \hat{V}=a+i b$, where, according to the decay prescription on $\hat{V}$, both the functions $a$ and $b$ are bounded by $(\cosh t)^{\delta-1}$. We obtain then
$$\begin{aligned}
\Delta_{\mathbb{S}^{n}} \phi-\left(\frac{2 m-2}{m}\right)|\zeta|^{2} \phi & =\left(\frac{m-2}{m}\right) b \\
\Delta_{\mathbb{S}^{n}} \psi-\left(\frac{2 m-2}{m}\right)|\zeta|^{2} \psi & =\left(\frac{2-m}{m}\right) a .
\end{aligned}$$
Now, using separation of variables and translating the problem into an infinite dimensional system of ODE's, it is easy to obtain explicit solutions for this Bessel type equations. Moreover, both the solutions $\phi$ and $\psi$ are now of the same order of the right hand side, as $t \rightarrow+\infty$. Coming back to $\hat{U}$, we have that $|\hat{U}|_{\mathbb{R}^{k}}$ is bounded by $(\cosh t)^{\delta-1}$. Hence also the last boundary term is vanishing in the limit for $T \rightarrow+\infty$. The integration by parts is then completely justified and it is now straightforward to deduce that also when $\zeta \neq 0$ the vector fields $\hat{U}$ and $\hat{V}$ are forced to be trivial, which is a contradiction.

Case 3. Suppose that up to a subsequence and without loss of generality the points $p_{j}$ 's still converge to a point $p_{\infty}$ which lies in $K$, but with a lower velocity than in the previous case. This can be phrased by saying that $d_{g_{1}}\left(p_{j}, K\right) / \varepsilon_{j} \rightarrow+\infty$, as $j \rightarrow+\infty$ (notice that, up to pass to a new subsequence, we can suppose that all the $p_{j}$ 's lie in the side of $M_{\varepsilon}$ which comes from $M_{1}$ ). Following [31, Proposition 2], we rescale our sequence of problems with the rate of convergence of the $p_{j}$ 's, so that the blow-up limit is now given by
$$\begin{cases}L_{\mathbb{R}^{k} \times \mathbb{R}^{n}} X=0 & \text { on } \mathbb{R}_{z}^{k} \times\left(\mathbb{R}_{x}^{n} \backslash\{0\}\right) \\ |X|_{\mathbb{R}^{k} \times \mathbb{R}^{n}} \leq C|x|^{\delta} & \end{cases}$$
where $C>0$ is a positive constant and $X$ is nontrivial.
This last case can be treated easily first by showing that the condition $2-n<\delta$ allows one to extend smoothly the solution through the singular set $\mathbb{R}^{k} \times\{0\}$ in analogy with the Case 1.a, and then using the decay condition at infinity, with $\delta<(2-n) / 2$, as in Case 2 to justify the integration by parts which implies the vanishing of $X$ and thus the contradiction. \(\square\)

\section*{5. The energy constraint}

In this section we conclude the proof of Theorem 1 by showing that the Lichnerowicz equation can be solved
$$\Delta_{g_{\varepsilon}} u-c_{m} R_{g_{\varepsilon}} u+c_{m}\left|\mu_{\varepsilon}\right|_{g_{\varepsilon}}^{2} u^{-\frac{3 m-2}{m-2}}-c_{m} \frac{m-1}{m} \tau^{2} u^{\frac{m+2}{m-2}}=0,$$
provided the parameter $\varepsilon$ is sufficiently small. Before starting, we recall that the terms $\mu_{\varepsilon}$ is the sum of the 'proto TT-tensor' $\mu$ defined in of Section 2
and the correction term $D_{g_{\varepsilon}} X$, where the vector field $X$ solves the equation (17) and hence by Proposition 5 is $\varepsilon$-uniformly bounded in terms of $\mu$.

In analogy with [31], the solution to (28) will be obtained by perturbation. Since in Theorem 1 we claimed the convergence of the new solutions to the original ones, it is natural to linearize our equation about the constant 1. Hence we set $v:=u-1$ and we consider the linear operator
$$\mathcal{L}_{g_{\varepsilon}}=\Delta_{g_{\varepsilon}}-\chi_{1}\left(\left|\mu_{1}\right|_{g_{1}}^{2}+\tau^{2} / m\right)-\chi_{2}\left(\left|\mu_{2}\right|_{g_{2}}^{2}+\tau^{2} / m\right),$$
where $\chi_{1}:=\chi, \chi_{2}:=1-\chi$ and the smooth cut-off $\chi$ has been defined in Section 2. In the following $\mathcal{L}_{g_{\varepsilon}}$ will be referred as the linearized Lichnerowicz operator. For sake of completeness we recall that $\Delta_{g_{\varepsilon}}$ can be written on the poly-neck as
$$\Delta_{g_{\varepsilon}}=u_{\varepsilon}^{-\frac{4}{n-2}}\left[\partial_{t}^{2}+(n-2) \tanh \left(\frac{n-2}{2} t\right) \partial_{t}+\Delta_{S^{n-1}}+u_{\varepsilon}^{\frac{4}{n-2}} \Delta_{g_{K}}+P_{\varepsilon}\right],$$
where $P_{\varepsilon}$ is a second order partial differential operator whose coefficients are bounded by $\rho_{\varepsilon}$. Finally, collecting all the remainders, we define the error term $F_{\varepsilon}(v)$ by
$$\begin{aligned}
F_{\varepsilon}(v):= & -c_{m}\left(R_{g_{1}}-R_{g_{\varepsilon}}\right) \chi_{1}+c_{m}\left(\left|\mu_{1}\right|_{g_{1}}^{2}-\left|\mu_{\varepsilon}\right|_{g_{\varepsilon}}^{2}\right) \chi_{1} \\
& -c_{m}\left(R_{g_{2}}-R_{g_{\varepsilon}}\right) \chi_{2}+c_{m}\left(\left|\mu_{2}\right|_{g_{2}}^{2}-\left|\mu_{\varepsilon}\right|_{g_{\varepsilon}}^{2}\right) \chi_{2} \\
& -c_{m}\left(R_{g_{1}}-R_{g_{\varepsilon}}\right) \chi_{1} v-b_{m}\left(\left|\mu_{1}\right|_{g_{1}}^{2}-\left|\mu_{\varepsilon}\right|_{g_{\varepsilon}}^{2}\right) \chi_{1} v \\
& -c_{m}\left(R_{g_{2}}-R_{g_{\varepsilon}}\right) \chi_{2} v-b_{m}\left(\left|\mu_{2}\right|_{g_{2}}^{2}-\left|\mu_{\varepsilon}\right|_{g_{\varepsilon}}^{2}\right) \chi_{2} v \\
& -c_{m}\left|\mu_{\varepsilon}\right|_{g_{\varepsilon}}^{2} h(v)+c_{m} \frac{m-1}{m} \tau^{2} f(v),
\end{aligned}$$
where $c_{m}=(m-2) /[4(m-1)], b_{m}=c_{m}(3 m-2) /(m-2)$ and
$$\begin{aligned}
& h(v):=\left[(1+v)^{-\frac{3 m-2}{m-2}}-1+\left(\frac{3 m-2}{m-2}\right) v\right] \\
& f(v):=\left[(1+v)^{\frac{m+2}{m-2}}-1-\left(\frac{m+2}{m-2}\right) v\right] .
\end{aligned}$$
Hence both $h$ and $f$ are $\mathcal{O}\left(|v|^{2}\right)$.
In order to solve (28), we first prove invertibility and a priori estimates for $\mathcal{L}_{g_{\varepsilon}}$ and then we show that the fixed point problem
$$v=\mathcal{L}_{g_{\varepsilon}}^{-1} \circ F_{\varepsilon}(v)$$
admits a solution.
5.1. Analysis of the linearized Lichnerowicz operator. We consider the following linear problem
$$\mathcal{L}_{g_{\varepsilon}} v=w \quad \text { on } M_{\varepsilon} .$$
Concerning the existence of solutions, we observe that in the compact case this is a consequence of the non vanishing of $\tilde{\Pi}_{1}$ and $\tilde{\Pi}_{2}$. In fact this implies that the operator $\mathcal{L}_{g_{\varepsilon}}$ is negative definite, thus injective on $L^{2}\left(M_{\varepsilon}\right)$. Since it is also self adjoint, we deduce by the Fredholm alternative that it is also surjective. Moreover, by elliptic regularity, we have that if the right hand side is in $C^{0, \alpha}\left(M_{\varepsilon}\right)$, then the solution belongs to $C^{2, \alpha}\left(M_{\varepsilon}\right)$. If one of the summands is either AE or AH, the existence of solutions is guaranteed by the following issues without any further assumption on $\tilde{\Pi}_{i}, i=1,2$ (the references for these results are the same as for Proposition 3 and 4).

Proposition 6. Suppose that $(M, g)$ is an $m$-dimensional $A E$ Riemannian manifold with $2-m<-\nu<0$, then the linearized Lichnerowicz operator
$$\mathcal{L}_{g}: r^{-\nu} C_{A E}^{k+2, \alpha}(M) \longrightarrow r^{-\nu-2} C_{A E}^{k, \alpha}(M)$$
is an isomorphism for every $k \in \mathbb{N}$.
Proposition 7. Suppose that $(M, g)$ is an $m$-dimensional $A H$ Riemannian manifold with $0<\nu<m+1$, then, if $\nu^{\prime} \in(-1, m)$, the linearized Lichnerowicz operator
$$\mathcal{L}: y^{\nu^{\prime}} C_{A H}^{k+2, \alpha}(M) \longrightarrow y^{\nu^{\prime}} C_{A H}^{k, \alpha}(M),$$
is an isomorphism for every $k \in \mathbb{N}$.
We pass now to establish the a priori bound for solutions to (32). To treat all the possible situations at once, we denote by $F_{\gamma}^{k, \alpha}\left(M_{\varepsilon}\right)$ the space of functions $M_{\varepsilon}$ with $(k, \alpha)$-regularity endowed with $\gamma$-weighted norm in the poly-neck region, $\gamma \in \mathbb{R}$, and eventually with the suitable $\nu$ or $\nu^{\prime}$-weighted norm on the AE or AH ends. The linearized Lichnerowicz operator is naturally defined between the spaces
$$\mathcal{L}_{g_{\varepsilon}}: F_{\gamma}^{k+2, \alpha}\left(M_{\varepsilon}\right) \longrightarrow F_{\gamma-2}^{k, \alpha}\left(M_{\varepsilon}\right),$$
for $\gamma \in \mathbb{R}$. We can now state the following:
Proposition 8. Let $v \in F_{\gamma}^{k+2, \alpha}\left(M_{\varepsilon}\right)$ and $w \in F_{\gamma-2}^{k, \alpha}\left(M_{\varepsilon}\right)$ be functions satisfying the equation $\mathcal{L}_{g_{\varepsilon}} v=w$. Then, for any $2-n<\gamma<0$, there exist a real number $\varepsilon_{0} \in(0,1)$ and a positive constant $C>0$ such that for every $\varepsilon \in\left(0, \varepsilon_{0}\right)$
$$\|v\|_{F_{\gamma}^{k+2, \alpha}} \leq C \cdot\|w\|_{F_{\gamma-2}^{k, \alpha}} .$$
(Remember that $n$ is the codimension of $K$ in $M_{i}, i=1,2$ and it is supposed to be at least 3).

Proof. As in Proposition 5 the difficult part is to provide the uniform $C_{\gamma}^{0}$ bound. Hence we will focus here on the estimate
$$\|v\|_{F_{\gamma}^{0}} \leq C \cdot\|w\|_{F_{\gamma-2}^{0}} .$$
As a first step we produce a local version of the a priori estimate. Assuming the hypothesis of the theorem, we claim that there exist a real number $\beta=\beta(n, \gamma)>0$ and a positive constant $B=B(n, \gamma)>0$ such that for every $\varepsilon \in\left(0, e^{-\beta}\right)$
$$\|v\|_{\mathcal{C}_{\gamma}^{0}\left(T_{\beta}^{\varepsilon}\right)} \leq B\left[\|w\|_{\mathcal{C}_{\gamma-2}^{0}\left(T_{\beta}^{\varepsilon}\right)}+\|v\|_{\mathcal{C}_{\gamma}^{0}\left(\partial T_{\beta}^{\varepsilon}\right)}\right],$$
where $T_{\beta}^{\varepsilon}$ is the portion of the poly-neck where $\beta+\log \varepsilon \leq t \leq-\beta-\log \varepsilon$.
To prove this claim, we observe that the approximate solution metrics are the same as the ones used in [29] in order to produce the generalized connected sum of constant scalar curvature metrics. Hence, we recover from [29, Lemma 3] the existence of barrier function for $\Delta_{g_{\varepsilon}}$. Combining this with the maximum principle one can easily deduce that if $\Delta_{g_{\varepsilon}} v=\underline{f}$, with $f \in C^{0}$, then for every $2-n<\gamma<0$ there exist a real number $\bar{\beta}=\bar{\beta}(n, \gamma)>0$ and
a positive constant $A=A(n, \gamma)>0$ such that for every $\beta>\bar{\beta}$ and every $\varepsilon \in\left(0, e^{-\beta}\right)$
$$\|v\|_{\mathcal{C}_{\gamma}^{0}\left(T_{\beta}^{\varepsilon}\right)} \leq A\left[\|f\|_{\mathcal{C}_{\gamma-2}^{0}\left(T_{\beta}^{\varepsilon}\right)}+\|v\|_{\mathcal{C}_{\gamma}^{0}\left(\partial T_{\beta}^{\varepsilon}\right)}\right] .$$
To obtain the claim, we let now
$$f=w+\left[\chi_{1}\left(\left|\mu_{1}\right|_{g_{1}}^{2}+\tau^{2} / m\right)+\chi_{2}\left(\left|\mu_{2}\right|_{g_{2}}^{2}+\tau^{2} / m\right)\right] v$$
and we observe that for large enough $\beta$, we have
$$\begin{aligned}
\left.\sup _{T_{\beta}^{\varepsilon}}\left|\rho_{\varepsilon}^{-\gamma+2}\right| \mu_{1}\right|_{g_{1}} ^{2} v \mid & \leq \frac{1}{4} \sup _{T_{\beta}^{\varepsilon}}\left|\rho_{\varepsilon}^{-\gamma} v\right| \\
\sup _{T_{\beta}^{\varepsilon}}\left|\rho_{\varepsilon}^{-\gamma+2}\left(\tau^{2} / m\right) v\right| & \leq \frac{1}{4} \sup _{T_{\beta}^{\varepsilon}}\left|\rho_{\varepsilon}^{-\gamma} v\right|,
\end{aligned}$$
for every $\varepsilon \in\left(0, e^{-\beta}\right)$. The estimate (35) follows at once.
To obtain (34) we argue by contradiction as in the proof of Proposition 5. If (34) does not hold, we can consider a sequence of counterexamples $\left(\varepsilon_{j}, v_{j}, w_{j}\right), j \in \mathbb{N}$, such that
\begin{itemize}
\item[(1)] $\varepsilon_{j} \rightarrow 0, \quad j \rightarrow+\infty$
\item[(2)] $\mathcal{L}_{\varepsilon_{j}} v_{j}=w_{j}, \quad j \in \mathbb{N}$
\item[(3)] $\left\|v_{j}\right\|_{F_{\gamma}^{0}}=1, \quad j \in \mathbb{N} \quad$ and $\quad\left\|w_{j}\right\|_{F_{\gamma-2}^{0}} \rightarrow 0, \quad j \rightarrow+\infty$.
\end{itemize}
As in Proposition 5 we consider the sequence of points $p_{j} \in M_{\varepsilon_{j}}, j \in \mathbb{N}$ such that the pointwise norm $\left|v_{j}\right|\left(p_{j}\right)$ eventually multiplied by weighting function raised to the power indicated by the weight is greater or equal than $1-\varepsilon_{j}$. Depending on the behavior of the sequence $\left\{p_{j}\right\}$, we are going to distinguish several cases.

Case 1. The first case is when up to a subsequence the points $p_{j}$ lie in a compact region of say $M_{1} \backslash K$ (the case of $M_{2} \backslash K$ is analogous). Hence, it is not hard to dee that the functions $v_{j}$ tend to a nontrivial distributional solution $v_{\infty}$ of the homogeneous problem $\mathcal{L}_{g_{1}} v_{\infty}=0$ on $M_{1} \backslash K$, which in addition satisfies the growth prescription $\left|v_{\infty}\right| \leq C\left|d_{g_{1}}(\cdot, K)\right|^{\gamma}$. Since $2-n<\gamma, v_{\infty}$ extends smoothly through $K$. On the other hand, we have already seen that the linearized Lichnerowicz operator about the metric $g_{1}$ is injective in both the compact and the non compact case. Hence, $v_{\infty}$ must be trivial, which is a contradiction.

Case 2. The second case is when $M_{\varepsilon}$ is non compact and, up to a subsequence, the points $p_{j}$ 's leave every compact subset of $M_{\varepsilon}$. Again, without loss of generality, we assume that the points $p_{j}$ 's of the subsequence lie on the piece of $M_{\varepsilon}$ coming from $M_{1}$. In this case the contradiction is reached by the same argument used in Case 1b of Proposition 5, mutatis mutandis.

Case 3. The remaining case is when up to a subsequence the points $p_{j}$ 's lie in the region $T_{\beta}^{\varepsilon_{j}}$. Again, in this case the functions $v_{j}$ tend to a distributional solution of $\mathcal{L}_{g_{i}} v_{\infty}=0$ on $M_{i} \backslash K$ verifying the prescription $\left|v_{\infty}\right| \leq C\left|d_{g_{i}}(\cdot, K)\right|^{\gamma}$, for $i=1,2$. The fact that $v_{\infty}$ is nontrivial is now a consequence of the local a priori bound (35). In fact in correspondence to the $p_{j}$ 's, we can find another sequence of points $q_{j}$ 's lying in $\partial T_{\beta}^{\varepsilon_{j}}$, where the quantities $\left|v_{j}\right|$ 's are uniformly bounded from below. Notice that in the limit,
the loci $\partial T_{\beta}^{\varepsilon_{j}}$ correspond to the locus $\left\{d_{g_{1}}(\cdot, K)=e^{-\beta}\right\} \cup\left\{d_{g_{2}}(\cdot, K)=e^{-\beta}\right\}$. To reach the contradiction it is now sufficient to repeat the same argument as in the Case 1 above. \(\square\)
5.2. Fixed point argument. In this subsection, taking advantage of Proposition 8 we will produce a solution to equation (28) by solving the fixed point problem (31).

As a first step we show that $\mathcal{L}_{g_{\varepsilon}} \circ F_{\varepsilon}$ viewed as a mapping from the space of continuous functions on $M_{\varepsilon}$ in itself sends a small ball centered at the origin in itself. Having this result, it is not difficult to show that $\mathcal{L}_{g_{\varepsilon}}^{-1} \circ F_{\varepsilon}$ is a contraction on this ball. This will provide automatically the fixed point and the control on the size of the correction.