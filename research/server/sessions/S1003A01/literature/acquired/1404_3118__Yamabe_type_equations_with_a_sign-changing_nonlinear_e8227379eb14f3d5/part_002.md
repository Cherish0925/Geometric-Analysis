---
retention_scope: session
part: 2
total_parts: 4
---

[Part 2/4 of: [1404.3118] Yamabe type equations with a sign-changing nonlinearity, and the prescribed curvature problem]

Next, we need a gluing result which we will call the pasting lemma. Although for $V \equiv 0$ this is somehow standard (a simple proof can be given by adapting Lemma 2.4 in [65]), the presence of a nonzero $V$ makes things more delicate. First, we introduce some definitions. We recall that, given an open subset $\Omega \subset M$ possibly with non-compact closure, the space $W_{\text {loc }}^{1, p}(\bar{\Omega})$ is the set of all functions $u$ on $\Omega$ such that, for every relatively compact open set $U \subseteq M$ with $U \cap \Omega \neq \emptyset, u \in W^{1, p}(\Omega \cap U)$. A function $u$ in this space is thus well behaved on relatively compact portions of $\partial \Omega$, while no global control is assumed on the $W^{1, p}$ norm of $u$.

Lemma 3.1 (The pasting lemma). Let $(M,\langle\rangle$,$) be a Riemannian manifold, f \in$ $C^{\infty}(M), p \in(1, \infty), V \in L_{\mathrm{loc}}^{\infty}(M)$. Let $\Omega_{1}, \Omega_{2}$ be open sets such that $\Omega_{1} \subset \Omega_{2}$. For $j=1,2$, let $u_{j} \in C^{0}\left(\bar{\Omega}_{j}\right) \cap W_{\text {loc }}^{1, p}\left(\bar{\Omega}_{j}\right)$ be a positive supersolution of $Q_{V}^{\prime}$ on $\Omega_{j}$, that is, $Q_{V}^{\prime}\left(u_{j}\right) \geq 0$ on $\Omega_{j}$. If
$$u_{2} \leq u_{1} \quad \text { on } \partial \Omega_{1} \cap \Omega_{2},$$
then the positive function
$$u \doteq \begin{cases}\min \left\{u_{1}, u_{2}\right\} & \text { on } \bar{\Omega}_{1} \\ u_{2} & \text { on } \Omega_{2} \backslash \Omega_{1}\end{cases}$$
is in $W_{\text {loc }}^{1, p}\left(\bar{\Omega}_{2}\right)$ and it satisfies $Q_{V}^{\prime}(u) \geq 0$ on $\Omega_{2}$.
When $\Omega_{1} \equiv \Omega_{2}$, a general result of V.K. Le, [46], guarantees that $\min \left\{u_{1}, u_{2}\right\}$ is a supersolution. The pasting lemma can then be deduced by an approximation argument, along the lines described in [2], and we leave the details to the interested reader. In the Appendix below, we give a quite different proof by using the obstacle
problem for $Q_{V}$ and the minimizing properties of its solutions, that might have an independent interest.

\section*{4. Criticality theory for $Q_{V}$, capacity and Hardy weights}

The criticality theory for $Q_{V}$ reveals an interesting scenario, and extends in a nontrivial way the parabolicity theory for the standard Laplacian and for the $p$-Laplacian (developed, among others, in [34, 64, 79]). Although a thorough description goes beyond the scope of this paper, nevertheless the validity of the pasting lemma gives us the opportunity to complement known results (especially those in [67, 68]) by relating them to a capacity theory for $Q_{V}$, see Theorem 4.1 below. We underline that, although the $Q_{V}$-capacity theory is investigated by following the same lines as those for the standard $p$-Laplacian, as in the previous results the presence of a nontrivial $V$ makes things subtler.

Let $Q_{V} \geq 0$ on $M$, and fix a positive supersolution $g \in C^{0}(M) \cap W_{\text {loc }}^{1, p}(M)$ of $Q_{V}^{\prime}$, that is, a solution of
$$Q_{V}^{\prime}(g) \geq 0 .$$
For each $K \Subset \Omega \Subset M, K$ compact, $\Omega$ open, let
$$\mathcal{D}(K, \Omega, g)=\left\{\varphi \in C^{0}(\bar{\Omega}) \cap W_{0}^{1, p}(\Omega): \varphi \geq g \text { in a neighbourhood of } K\right\}$$
and define the $Q_{V}$-capacity
$$\operatorname{cap}_{Q_{V}}(K, \Omega, g) \doteq \inf _{\varphi \in \mathcal{D}(K, \Omega, g)} Q_{V}(\varphi)$$
Clearly, $\operatorname{cap}_{Q_{V}}(K, \Omega, g)$ grows if we decrease $\Omega$, as well as if we increase $K$. If $V \equiv 0$, it is customary to choose $g \equiv 1$ as solution of $\Delta_{p, f} g=0$, and we recover the classical definition of capacity. We however underline that, for the next arguments to work, it is essential that the fixed $g$ solves $Q_{V}^{\prime}(g) \geq 0$ on $M$, for otherwise the basic properties needed in the next results could not hold.

Proposition 4.1. Let $K$ be the closure of an open domain and suppose that $\partial \Omega, \partial K$ are of class $C^{1, \alpha}$ for some $\alpha \in(0,1)$. Then
$$\operatorname{cap}_{Q_{V}}(K, \Omega, g)=Q_{V}(u)$$
where $u$ is the unique positive solution $u \in C^{0}(\bar{\Omega}) \cap W_{0}^{1, p}(\Omega) \cap C^{1, \mu}(\bar{\Omega} \backslash K)$ of
$$\left\{\begin{array}{l}
Q_{V}^{\prime}(u)=0 \quad \text { on } \Omega \backslash K, \\
u=g \quad \text { on } K, \quad u=0 \quad \text { on } \partial \Omega .
\end{array}\right.$$
We call such a solution $u$ the $Q_{V}$-capacitor of $(K, \Omega, g)$.
Remark 4.1. The existence, uniqueness and positivity of $u$ is granted by iv) in Proposition 3.4 As for regularity, the interior estimate $u \in C_{\text {loc }}^{1, \mu}(\bar{\Omega} \backslash K)$ follows by [78, 27], and the boundary continuity at $\partial K \cup \partial \Omega$ by Theorem 5.4, page 235 in [52]. The fact that $u \in W^{1, p}(\Omega)$ follows by standard theory of Sobolev functions ${ }^{3}$.

\footnotetext{
${ }^{3}$ In fact, $u-g \in W^{1, p}(\Omega \backslash K)$ has zero trace on $\partial K$, thus it is the $W^{1, p}$-limit (and also, up to extracting a subsequence, the pointwise limit) of some sequence $\left\{\varphi_{j}\right\} \subset C^{\infty}(\overline{\Omega \backslash K})$ where $\varphi_{j} \equiv 0$ in a neighbourhood of $\partial K$. Extending $\varphi_{j}$ to be zero on $K$ we have that $g+\varphi_{j}$ is Cauchy in $W^{1, p}$ and pointwise convergent to $u$, thus $g+\varphi_{j} \rightarrow u \in W^{1, p}(\Omega)$.
}

Proof. Let $\varphi \in \mathcal{D}(K, \Omega, g)$. First, we claim that $\hat{\varphi}=\min \{\varphi, g\} \in \mathcal{D}(K, \Omega, g)$ solves $Q_{V}(\hat{\varphi}) \leq Q_{V}(\varphi)$, whence we can assume, without loss of generality, that $\varphi \leq g$ on $\Omega$ (and hence $\varphi=g$ on a neighbourhood of $K$ ).

Consider the open set $U=\{\varphi>g\} \Subset \Omega$. We test $Q_{V}^{\prime}(g) \geq 0$ with the non-negative function $\left(\varphi^{p}-g^{p}\right)_{+} / g^{p-1} \in W_{0}^{1, p}(\Omega)$ and use the non-negativity of the Lagrangian in (3.5) to deduce
$$\begin{aligned}
0 \leq & \int_{U}|\nabla g|^{p-2}\left\langle\nabla g, \nabla\left(\frac{\varphi^{p}}{g^{p-1}}\right)\right\rangle \mathrm{d} \mu_{f}-\int_{U} V \varphi^{p} \mathrm{~d} \mu_{f}-p Q_{V}\left(g_{\mid U}\right) \\
= & p \int_{U}\left(\frac{\varphi}{g}\right)^{p-1}|\nabla g|^{p-2}\langle\nabla g, \nabla \varphi\rangle \mathrm{d} \mu_{f}-(p-1) \int_{U}\left(\frac{\varphi}{g}\right)^{p}|\nabla g|^{p} \mathrm{~d} \mu_{f} \\
& -\int_{U} V \varphi^{p} \mathrm{~d} \mu_{f}-p Q_{V}\left(g_{\mid U}\right) \\
= & \int_{U}|\nabla \varphi|^{p} \mathrm{~d} \mu_{f}-\int_{U} \mathcal{L}(\varphi, g) \mathrm{d} \mu_{f}-\int_{U} V \varphi^{p} \mathrm{~d} \mu_{f}-p Q_{V}\left(g_{\mid U}\right) \\
\leq & p Q_{V}\left(\varphi_{\mid U}\right)-p Q_{V}\left(g_{\mid U}\right)
\end{aligned}$$
hence $Q_{V}\left(\hat{\varphi}_{\mid U}\right)=Q_{V}\left(g_{\mid U}\right) \leq Q_{V}\left(\varphi_{\mid U}\right)$. Since $\varphi \equiv \hat{\varphi}$ on $\Omega \backslash U$, the claim follows. Let now $\varphi \in \mathcal{D}(K, \Omega, g)$ be such that $\varphi=g$ on $K$. By density, we can assume that $\varphi \in \operatorname{Lip}_{0}(\Omega)$. We therefore have $u-\varphi \in \operatorname{Lip}_{0}(\Omega \backslash K)$. Again by density, we can further assume that $\varphi=0$ in a neighbourhood of $\partial \Omega$. Thus, testing $Q_{V}^{\prime}(u)=0$ with $\left(\varphi^{p}-u^{p}\right) / u^{p-1} \in \operatorname{Lip}_{0}(\Omega \backslash K)$ and proceeding as above we obtain
$$\begin{aligned}
0= & \int_{\Omega \backslash K}|\nabla u|^{p-2}\left\langle\nabla u, \nabla\left(\frac{\varphi^{p}}{u^{p-1}}\right)\right\rangle \mathrm{d} \mu_{f}-\int_{\Omega \backslash K} V \varphi^{p} \mathrm{~d} \mu_{f}-p Q_{V}\left(u_{\mid \Omega \backslash K}\right) \\
= & p \int_{\Omega \backslash K}\left(\frac{\varphi}{u}\right)^{p-1}|\nabla u|^{p-2}\langle\nabla u, \nabla \varphi\rangle \mathrm{d} \mu_{f}-(p-1) \int_{\Omega \backslash K}\left(\frac{\varphi}{u}\right)^{p}|\nabla u|^{p} \mathrm{~d} \mu_{f} \\
& -\int_{\Omega \backslash K} V \varphi^{p} \mathrm{~d} \mu_{f}-p Q_{V}\left(u_{\mid \Omega \backslash K}\right) \\
= & \int_{\Omega \backslash K}|\nabla \varphi|^{p} \mathrm{~d} \mu_{f}-\int_{\Omega \backslash K} \mathcal{L}(\varphi, u) \mathrm{d} \mu_{f}-\int_{\Omega \backslash K} V \varphi^{p} \mathrm{~d} \mu_{f}-p Q_{V}\left(u_{\mid \Omega \backslash K}\right) \\
\leq & p Q_{V}\left(\varphi_{\mid \Omega \backslash K}\right)-p Q_{V}\left(u_{\mid \Omega \backslash K}\right) .
\end{aligned}$$
As $u=\varphi=g$ on $K$, we conclude $Q_{V}(u) \leq Q_{V}(\varphi)$ and whence $Q_{V}(u) \leq \operatorname{cap}(K, \Omega, g)$. Since $u$ lies in the $W^{1, p}$ closure of $\mathcal{D}(K, \Omega, g)$, equality (4.2) follows. \(\square\)

Remark 4.2. By the pasting Lemma 3.1, note that $u$ solving (4.3) is a supersolution on the whole $\Omega$, that is, $Q_{V}^{\prime}(u) \geq 0$ on $\Omega$.

Proposition 4.2. In the assumptions of the previous theorem, suppose that $Q_{V}^{\prime}(g)=0$ on a neighbourhood of $K$, and that $\partial K$ is smooth. Then,
$$Q_{V}(u)=\frac{1}{p} \int_{\partial K} g\left[|\nabla g|^{p-2} \frac{\partial g}{\partial \nu}-|\nabla u|^{p-2} \frac{\partial u}{\partial \nu}\right] \mathrm{d} \sigma_{f},$$
where $\nu$ is the unit normal to $\partial K$ pointing outward of $K$.
Proof. Let $T \approx \partial K \times\left(-\varepsilon_{0}, \varepsilon_{0}\right) \Subset \Omega$ be a tubular neighbourhood of $\partial K$ where Fermi coordinates are defined, and let $\rho(x)$ be the smooth signed distance from $\partial K$, that is, $\rho(x)=\operatorname{dist}(x, \partial K)$ if $x \notin K$, and $\rho(x)=-\operatorname{dist}(x, \partial K)$ if $x \in K$. Let $h \in \operatorname{Lip}\left(\mathbb{R}_{0}^{+}\right)$
be such that $h(t)=0$ if $t \leq 0, h(t)=t$ for $t \in[0,1]$ and $h(t)=1$ for $t \geq 1$ and, for small $\varepsilon \in\left(0, \varepsilon_{0}\right)$, set $h_{\varepsilon}(t) \doteq h(t / \varepsilon)$. Applying (4.3) on $\Omega \backslash K$ to the test function $h_{\varepsilon}(\rho) u \in \operatorname{Lip}_{0}(\Omega \backslash K)$, using the coarea's formula and letting $\varepsilon \rightarrow 0$, since $g$ is $C^{1}$ we deduce
$$0=\lim _{\varepsilon \rightarrow 0} Q_{V}^{\prime}(u)\left[h_{\varepsilon}(\rho) u\right]=p Q_{V}\left(u_{\Omega \backslash K}\right)+\int_{\partial K} u|\nabla u|^{p-2} \frac{\partial u}{\partial \nu} \mathrm{~d} \sigma_{f} .$$
In a similar way, applying $Q_{V}^{\prime}(g)=0$ on $K$ to the non-negative test function $h_{\varepsilon}(-\rho) g \in$ $\operatorname{Lip}_{0}(K)$ and letting $\varepsilon \rightarrow 0$ we deduce that
$$0=\lim _{\varepsilon \rightarrow 0} Q_{V}^{\prime}(u)\left[h_{\varepsilon}(-\rho) g\right]=p Q_{V}\left(u_{K}\right)-\int_{\partial K} g|\nabla g|^{p-2} \frac{\partial g}{\partial \nu} \mathrm{~d} \sigma_{f} .$$
Subtracting the two identities and using $u=g$ on $\partial K$ yields (4.6). \(\square\)

Next, we consider the $Q_{V}$-capacity of $K$ in the whole $M$ :
$$\begin{gathered}
\mathcal{D}(K, g)=\left\{\varphi \in C_{c}^{0}(M) \cap W_{\text {loc }}^{1, p}(M): \varphi \geq g \text { in a neighbourhood of } K\right\} \\
\operatorname{cap}_{Q_{V}}(K, g) \doteq \inf _{\varphi \in \mathcal{D}(K, g)} Q_{V}(\varphi) .
\end{gathered}$$
Let $\left\{\Omega_{j}\right\}$ be an exhaustion of $M$ with $K \Subset \Omega_{1}$. Then, from the definitions it readily follows that
$$\operatorname{cap}_{Q_{V}}(K, g)=\inf _{j} \operatorname{cap}_{Q_{V}}\left(K, \Omega_{j}, g\right)=\lim _{j \rightarrow+\infty} \operatorname{cap}_{Q_{V}}\left(K, \Omega_{j}, g\right) .$$
If $K$ is the closure of a open set and $\partial K$ is of class $C^{1, \alpha}$ for some $\alpha \in(0,1)$, let $u_{j}$ be the $Q_{V}$-capacitor of $\left(K, \Omega_{j}, g\right)$. By Proposition 4.1,
$$\operatorname{cap}_{Q_{V}}(K, g)=\lim _{j \rightarrow+\infty} Q_{V}\left(u_{j}\right) .$$
Proposition 3.3 implies that $0 \leq u_{j} \leq u_{j+1} \leq g$ for each $j$, whence, by Dini theorem and elliptic estimates, $u_{j}$ converges locally uniformly on $M$, in $W_{\text {loc }}^{1, p}(M)$ and in the $C^{1}$ topology on $M \backslash K$ to a weak solution $u \in C^{0}(M) \cap W_{\text {loc }}^{1, p}(M) \cap C_{\text {loc }}^{1, \mu}(M \backslash K)$ of
$$\left\{\begin{array}{l}
Q_{V}^{\prime}(u)=0 \quad \text { on } M \backslash K, \\
u=g \quad \text { on } K, \quad 0<u \leq g \quad \text { on } M \backslash K .
\end{array}\right.$$
The pasting Lemma 3.1 guarantees that $Q_{V}^{\prime}(u) \geq 0$ on the whole $M$. We call such a $u$ the $Q_{V}$-capacitor of $(K, g)$.

Proposition 4.3. In the assumptions of Proposition 4.2, if $Q_{V}^{\prime}(g)=0$ on a neighbourhood of $K$,
$$\operatorname{cap}_{Q_{V}}(K, g)=\frac{1}{p} \int_{\partial K} g\left[|\nabla g|^{p-2} \frac{\partial g}{\partial \nu}-|\nabla u|^{p-2} \frac{\partial u}{\partial \nu}\right] \mathrm{d} \sigma_{f},$$
where $\nu$ is the unit normal to $\partial K$ pointing outward of $K$.
Proof. By Proposition 4.1, $\operatorname{cap}_{Q_{V}}(K, g)=\lim _{j} Q_{V}\left(u_{j}\right)$, where $u_{j}$ is the $Q_{V}$-capacitor of $\left(K, \Omega_{j}, g\right)$. Now, since $u_{j} \rightarrow u$ in $C^{1}(\partial K)$, it is enough to pass to the limit in 4.6. \(\square\)

Next Theorem, the core of this section, relates the subcriticality of $Q_{V}$ and the $Q_{V}$-capacity with other basic properties, which we will define below. It is due to Y. Pinchover and K. Tintarev (see [67]), and it is known in the literature as the ground state alternative. The authors state it for $f$ constant and $M=\mathbb{R}^{m}$. Our contribution here is to include the $Q_{V}$-capacity properties to the above picture. However, since at
some point of [67] the authors use inequalities for which we found no counterpart in a manifold setting, we prefer to provide a full proof which sometimes uses arguments that differ from those in [67, 68], though keeping the same guidelines.
Definition 4.1. For $V \in L_{\text {loc }}^{\infty}(M)$, define $Q_{V}$ as in (2.7) and let $\Omega \subseteq M$ be an open set.
\begin{itemize}
\item[iii)] $Q_{V}$ has a weighted spectral gap on $\Omega$ if there exists $W \in C^{0}(\Omega), W>0$ on $\Omega$ such that
$$\int_{\Omega} W(x)|\varphi|^{p} \mathrm{~d} \mu_{f} \leq Q_{V}(\varphi) \quad \forall \varphi \in \operatorname{Lip}_{c}(\Omega) .$$
\item[iv)] A sequence $\left\{\eta_{j}\right\} \in L_{c}^{\infty}(\Omega) \cap W^{1, p}(\Omega)$ is said to be a null sequence if $\eta_{j} \geq 0$ a.e. for each $j, Q_{V}\left(\eta_{j}\right) \rightarrow 0$ as $j \rightarrow+\infty$ and there exists a relatively compact open set $B \subseteq M$ and $C>1$ such that $C^{-1} \leq\left\|\eta_{j}\right\|_{L^{p}(B)} \leq C$ for each $j$.
\item[v)] A function $0 \leq \eta \in W_{\text {loc }}^{1, p}(\Omega), \eta \geq 0, \eta \not \equiv 0$ is a ground state for $Q_{V}$ on $\Omega$ if it is the $L_{\text {loc }}^{p}(\Omega)$ limit of a null sequence.
\end{itemize}

Theorem 4.1. Let $(M,\langle\rangle$,$) be connected and non-compact, and for V \in L_{\text {loc }}^{\infty}(M)$ consider an operator $Q_{V} \geq 0$ on $M$. Then, either $Q_{V}$ has a weighted spectral gap or a ground state on $M$, and the two possibilities mutually exclude. Moreover, the following properties are equivalent:
\begin{itemize}
\item[] $(i)_{\mathrm{S}} Q_{V}$ has a weighted spectral gap.
\item[] $(i i)_{\mathrm{S}} Q_{V}$ is subcritical on $M$.
\item[(iii)] ${ }_{\mathrm{S}}$ There exist two positive solutions $u_{1}, u_{2} \in C^{0}(M) \cap W_{\text {loc }}^{1, p}(M)$ of $Q_{V}^{\prime}(u) \geq 0$ which are not proportional.
\item[] $(i v)_{\mathrm{S}}$ For some (any) $K \Subset M$ compact with non-empty interior, and for some (any) $0<g \in C^{0}(M) \cap W_{\text {loc }}^{1, p}(M)$ solving $Q_{V}^{\prime}(g) \geq 0, \operatorname{cap}(K, g)>0$.
\end{itemize}

When $Q_{V}$ has a ground state $\eta, \eta$ solves $Q_{V}^{\prime}(\eta)=0$, and in particular $\eta \in C_{\text {loc }}^{1, \mu}(M)$, $\eta>0$ on $M$. Furthermore, the next properties are equivalent:
\begin{itemize}
\item[] $(i)_{\mathrm{GS}} Q_{V}$ has a ground state.
\item[] $(i i)_{\mathrm{GS}}$ All positive solutions $g \in C^{0}(M) \cap W_{\mathrm{loc}}^{1, p}(M)$ of $Q_{V}^{\prime}(g) \geq 0$ are proportional; in particular, each positive supersolution is indeed a solution (hence, a ground state).
\item[] $(i i i)_{\mathrm{GS}}$ For some (any) $K \Subset M$ compact with non-empty interior, and for some (any) $0<g \in C^{0}(M) \cap W_{\text {loc }}^{1, p}(M)$ solving $Q_{V}^{\prime}(g) \geq 0, \operatorname{cap}(K, g)=0$.
\end{itemize}

Proof. Hereafter, $L^{p}$ and $W^{1, p}$ spaces will be considered with respect to the measure $\mathrm{d} \mu_{f}$. We begin with the following fact.

Claim 1: Fix an open set $U \subset M$. If $\left\{\phi_{j}\right\} \subset L_{c}^{\infty}(M) \cap W^{1, p}(M)$ is such that $\left\|\phi_{j}\right\|_{L^{p}(U)}+Q_{V}\left(\phi_{j}\right) \leq C$ for some $C>0$ independent of $j$, then $\left\{\phi_{j}\right\}$ is locally bounded in $W^{1, p}(M)$.

Proof of Claim 1. Up to replacing $\phi_{j}$ with $\left|\phi_{j}\right|$, we can assume that $\phi_{j} \geq 0$ a.e. on $M$. Using that $Q_{V}$ is non-negative on $M$, choose a positive solution $g \in C_{\text {loc }}^{1, \mu}(M)$ of $Q_{V}^{\prime}(g)=0$ and consider the Lagrangian representation of $Q_{V}\left(\phi_{j}\right)$ :
$$Q_{V}\left(\phi_{j}\right)=\int_{M} \mathcal{L}\left(\phi_{j}, g\right) \mathrm{d} \mu_{f}$$

Fix $\Omega \Subset M$ containing $\bar{U}$. Since $Q_{V}\left(\phi_{j}\right) \leq C$ and $\mathcal{L}\left(\phi_{j}, g\right) \geq 0$ on $M$, it holds
$$0 \leq \limsup _{j \rightarrow+\infty} \int_{\Omega} \mathcal{L}\left(\phi_{j}, g\right) \mathrm{d} \mu_{f} \leq C .$$
By using Cauchy-Schwarz and Young inequalities on the third addendum of the expression of $\mathcal{L}\left(\phi_{j}, g\right)$ we deduce that, for each $\varepsilon>0$,
$$\mathcal{L}\left(\phi_{j}, g\right) \geq\left(1-\varepsilon^{p}\right)\left|\nabla \phi_{j}\right|^{p}+(p-1)\left(1-\varepsilon^{-\frac{p}{p-1}}\right)\left(\frac{\phi_{j}}{g}\right)^{p}|\nabla g|^{p} .$$
In our assumptions, $|\nabla \log g| \in L^{\infty}(\Omega)$. Setting $\varepsilon=1 / 2$ in (4.15), integrating and using (4.14) we get
$$\limsup _{j \rightarrow+\infty}\left[\left(1-2^{-p}\right) \int_{\Omega}\left|\nabla \phi_{j}\right|^{p} \mathrm{~d} \mu_{f}+(p-1)\left(1-2^{\frac{p}{p-1}}\right)\|\nabla \log g\|_{L^{\infty}(\Omega)} \int_{\Omega}\left|\phi_{j}\right|^{p} \mathrm{~d} \mu_{f}\right] \leq C .$$
From this inequality we argue the existence of constants $C_{1}, C_{2}>0$ independent of $j$ such that
$$\left\|\nabla \phi_{j}\right\|_{L^{p}(\Omega)} \leq C_{1}\left\|\phi_{j}\right\|_{L^{p}(\Omega)}+C_{2} .$$
Suppose now, by contradiction, that $\left\{\phi_{j}\right\}$ is not bounded in $W^{1, p}(\Omega)$. By (4.17), $\left\|\phi_{j}\right\|_{L^{p}(\Omega)}$ diverge. Set $\bar{\phi}_{j}=\phi_{j} /\left\|\phi_{j}\right\|_{L^{p}(\Omega)}$. Then, by (4.17) $\left\{\bar{\phi}_{j}\right\}$ is bounded in $W^{1, p}(\Omega)$, thus it has a subsequence (still called $\left\{\bar{\phi}_{j}\right\}$ ) converging weakly in $W^{1, p}$, strongly in $L^{p}$ and pointwise almost everywhere to some non-negative function $\Psi$ satisfying $\|\Psi\|_{L^{p}(\Omega)}=\lim _{j}\left\|\bar{\phi}_{j}\right\|_{L^{p}(\Omega)}=1$. Since $|\nabla \log g| \in L^{\infty}(\Omega)$ we straightforwardly have that
$$\begin{array}{lll}
\text { (i) } & \bar{\phi}_{j}^{p}|\nabla \log g|^{p} \rightarrow \Psi^{p}|\nabla \log g|^{p} & \text { in } L^{1}(\Omega), \\
\text { (ii) } & \bar{\phi}_{j}^{p-1}|\nabla \log g|^{p-1} \rightarrow \Psi^{p-1}|\nabla \log g|^{p-1} & \text { in } L^{\frac{p}{p-1}}(\Omega) .
\end{array}$$
We just prove (ii), the other being a consequence of the proof. By the elementary inequalities
$$(x-y)^{\beta} \leq x^{\beta}-y^{\beta} \leq C x^{\beta-1}(x-y) \quad \text { for } y \in[0, x] \text { and } \beta>1,$$
for some $C$ depending on $\beta$, with a final application of Hölder inequality we deduce that
$$\begin{aligned}
& \left\|\left(\bar{\phi}_{j}^{p-1}-\Psi^{p-1}\right)|\nabla \log g|^{p-1}\right\|_{L^{p /(p-1)}(\Omega)}^{p /(p-1)} \leq\|\nabla \log g\|_{L^{\infty}(\Omega)}^{p} \int_{\Omega}\left|\bar{\phi}_{j}^{p-1}-\Psi^{p-1}\right|^{\frac{p}{p-1}} \mathrm{~d} \mu_{f} \\
& \leq\|\nabla \log g\|_{L^{\infty}(\Omega)}^{p} \int_{\Omega}\left|\bar{\phi}_{j}^{p}-\Psi^{p}\right| \mathrm{d} \mu_{f} \leq C\|\nabla \log g\|_{L^{\infty}(\Omega)}^{p} \int_{\Omega}\left(\max \left\{\bar{\phi}_{j}, \Psi\right\}\right)^{p-1}\left|\bar{\phi}_{j}-\Psi\right| \mathrm{d} \mu_{f}, \\
& \leq C\|\nabla \log g\|_{L^{\infty}(\Omega)}^{p}\left\|\bar{\phi}_{j}+\Psi\right\|_{L^{p}(\Omega)}^{(p-1) / p}\left\|\bar{\phi}_{j}-\Psi\right\|_{L^{p}(\Omega)}
\end{aligned}$$
and this latter goes to zero $\bar{\phi}_{j} \rightarrow \Psi$ in $L^{p}(\Omega)$. Now, coupling $(i i)$ with the weak convergence of $\bar{\phi}_{j}$ to $\Psi$ in $W^{1, p}(\Omega)$, we get
$$\int_{\Omega}\left(\frac{\bar{\phi}_{j}}{g}\right)^{p-1}|\nabla g|^{p-2}\left\langle\nabla g, \nabla \bar{\phi}_{j}\right\rangle \mathrm{d} \mu_{f} \longrightarrow \int_{\Omega}\left(\frac{\Psi}{g}\right)^{p-1}|\nabla g|^{p-2}\langle\nabla g, \nabla \Psi\rangle \mathrm{d} \mu_{f},$$
so that, combining $(i)$, (ii) and the weak lower semicontinuity of $\|\cdot\|_{W^{1, p}(\Omega)}$,
$$0 \leq \int_{\Omega} \mathcal{L}(\Psi, g) \mathrm{d} \mu_{f} \leq \liminf _{j \rightarrow+\infty} \int_{\Omega} \mathcal{L}\left(\bar{\phi}_{j}, g\right) \mathrm{d} \mu_{f}=\left\|\phi_{j}\right\|_{L^{p}(\Omega)}^{-p} \int_{\Omega} \mathcal{L}\left(\phi_{j}, g\right) \mathrm{d} \mu_{f} \rightarrow 0$$
as $j \rightarrow+\infty$. Hence $\mathcal{L}(\Psi, g)=0$ on $\Omega$, so by Proposition $3.1 \Psi=c g$ for some constant $c \geq 0$. However, since $\left\|\phi_{j}\right\|_{L^{p}(U)} \leq C$ for each $j$,
$$0 \leq\|\Psi\|_{L^{p}(U)}=\lim _{j \rightarrow+\infty}\left\|\bar{\phi}_{j}\right\|_{L^{p}(U)}=\lim _{j \rightarrow+\infty} \frac{\left\|\phi_{j}\right\|_{L^{p}(U)}}{\left\|\phi_{j}\right\|_{L^{p}(\Omega)}} \leq \limsup _{j \rightarrow+\infty} \frac{C}{\left\|\phi_{j}\right\|_{L^{p}(\Omega)}}=0,$$
hence $c=0$ and $\Psi \equiv 0$ on $\Omega$, contradicting the fact that $\|\Psi\|_{L^{p}(\Omega)}=1$. This concludes the proof of the claim.

Claim 2: Either $Q_{V}$ has a weighted spectral gap or a ground state, but not both.
Proof of Claim 2. For a relatively compact open set $U$, define the $L^{p}$-capacity $c$ as follows:
$$\mathcal{D}(U)=\left\{\varphi \in L_{c}^{\infty}(M) \cap W^{1, p}(M):\|\varphi\|_{L^{p}(U)}=1\right\}, \quad c(U)=\inf _{\varphi \in \mathcal{D}(U)} Q_{V}(\varphi),$$
where, as usual, the $L^{p}$-norm is computed with respect to $\mathrm{d} \mu_{f}$. Then, two mutually exclusive cases may occur: ether $c(U)>0$ for each $U$, or $c(U)=0$ for some $U$. In the first case, it is easy to see that $Q_{V}$ has a weighted spectral gap. Indeed, let $\left\{U_{j}\right\}$ be a locally finite covering of $M$ via relatively compact, open sets, set $c_{j}=c\left(U_{j}\right)>0$ and let $\left\{t_{j}\right\}$ be a sequence of positive numbers such that $\sum_{j} t_{j}=1$. For each $\varphi \in \operatorname{Lip}_{c}(M)$, by the definition of $c_{j}$ we get $Q_{V}(\varphi) \geq c_{j}\|\varphi\|_{L^{p}\left(U_{j}\right)}^{p}$, and summing up we get
$$Q_{V}(\varphi)=\left[\sum_{j=1}^{+\infty} t_{j}\right] Q_{V}(\varphi) \geq \sum_{j=1}^{+\infty} t_{j} c_{j} \int_{U_{j}}|\varphi|^{p} \mathrm{~d} \mu_{f}=\int_{M} \hat{W}|\varphi|^{p} \mathrm{~d} \mu_{f},$$
where
$$\hat{W}(x)=\sum_{j=1}^{+\infty} t_{j} c_{j} 1_{U_{j}}(x)>0 \quad \text { on } M$$
We can thus choose a weighted spectral gap $W$ by taking a positive, continuous function $W$ not exceeding $\hat{W}$.
Now, suppose that $c(U)=0$ for some $U$. We show that there exists a ground state. Indeed, by the definition of $c(U)$ there exists $\left\{\eta_{j}\right\} \subset L_{c}^{\infty}(M) \cap W^{1, p}(M)$ such that $\left\|\eta_{j}\right\|_{L^{p}(U)}=1$ and $Q_{V}\left(\eta_{j}\right) \rightarrow 0$. Up to replacing $\eta_{j}$ with $\left|\eta_{j}\right|$, we can suppose that $\eta_{j} \geq 0$ a.e. on $M$. By Claim 1, $\eta_{j}$ is locally bounded in $W^{1, p}$, and a Cantor type argument on an increasing exhaustion of $M$ ensures the existence of a subsequence, still called $\left\{\eta_{j}\right\}$, converging weakly in $W_{\text {loc }}^{1, p}(M)$ and strongly in $L_{\text {loc }}^{p}(M)$ to some function $\eta \in W_{\text {loc }}^{1, p}(M)$. By definition, $\eta$ is a ground state.

We now show our desired equivalences. To establish those involving $(i v)_{\mathrm{S}}$ and $(i i i)_{\mathrm{GS}}$, where the "some/all" alternative appears, then we will always assume the weakest alternative and prove the strongest one.
$(\mathbf{i})_{\mathrm{GS}} \Rightarrow(\mathbf{i i})_{\mathrm{GS}}$. Let $\eta \geq 0$ be a ground state, and let $\left\{\eta_{j}\right\} \subset L_{c}^{\infty}(M) \cap W^{1, p}(M)$ be a null sequence converging in $L_{\text {loc }}^{p}$ to $\eta$. Then, by Claim $1\left\{\eta_{j}\right\}$ is locally bounded in $W^{1, p}$, thus up to passing to a subsequence we can assume that also $\eta_{j} \rightarrow \eta$ weakly in $W_{\text {loc }}^{1, p}$. Consider a positive solution $g \in C^{0}(M) \cap W_{\text {loc }}^{1, p}(M)$ of $Q_{V}^{\prime}(g) \geq 0$. Fix $\Omega \subseteq M$. Up to multiply $g$ by a large positive constant, we can suppose that $\{x \in \Omega: \eta(x)<g(x)\}$ has positive measure. Let $\bar{\eta}_{j}=\min \left\{\eta_{j}, g\right\}$, and note that $\left\{\bar{\eta}_{j}\right\}$ is still a null sequence,
converging weakly in $W_{\text {loc }}^{1, p}$ to $\bar{\eta}=\min \{\eta, g\}$. Consider the Lagrangian representation
$$Q_{V}\left(\bar{\eta}_{j}\right) \geq \int_{M} \mathcal{L}\left(\bar{\eta}_{j}, g\right) \mathrm{d} \mu_{f}$$
guaranteed by Proposition 3.1. We claim that
$$\frac{\bar{\eta}_{j}^{p}}{g^{p-1}} \rightarrow \frac{\bar{\eta}^{p}}{g^{p-1}} \quad \text { weakly in } W^{1, p}(\Omega) .$$
To see this, we follows arguments analogous to those yielding (4.18). Choose a constant $c_{\Omega}>0$ large enough to satisfy $g \geq c_{\Omega}^{-1}$ on $\Omega$ and $\bar{\eta}_{j} \leq c_{\Omega}$. By a direct computation, $\left\|\bar{\eta}_{j}^{p} / g^{p-1}\right\|_{W^{1, p}(\Omega)}$ is uniformly bounded so that, by density, it is enough to check the weak convergence with test function $\varphi \in \operatorname{Lip}_{0}(\Omega)$. From
$$\left|\int_{\Omega} \frac{\bar{\eta}_{j}^{p}-\bar{\eta}^{p}}{g^{p-1}} \varphi \mathrm{~d} \mu_{f}\right| \leq c_{\Omega}^{p-1}\|\varphi\|_{L^{\infty}(\Omega)} \int_{\Omega}\left|\bar{\eta}_{j}^{p}-\bar{\eta}^{p}\right| \mathrm{d} \mu_{f},$$
applying the inequalities in (4.20) from the second line to the end we deduce that $\bar{\eta}_{j}^{p} / g^{p-1} \rightarrow \bar{\eta}^{p} / g^{p-1}$ weakly in $L^{p}(\Omega)$. Regarding the gradient part,
$$\left|\int_{\Omega}\left\langle\nabla\left(\frac{\bar{\eta}_{j}^{p}-\bar{\eta}^{p}}{g^{p-1}}\right), \nabla \varphi\right\rangle \mathrm{d} \mu_{f}\right| \leq(\mathrm{I})+(\mathrm{II}),$$
where
$$\begin{aligned}
(\mathrm{I}) & =(p-1) \int_{\Omega}\left|\bar{\eta}_{j}^{p}-\bar{\eta}^{p}\right||\nabla g| \frac{|\nabla \varphi|}{g^{p}} \\
(\mathrm{II}) & =p\left|\int_{\Omega}\left\langle\left(\frac{\bar{\eta}_{j}}{g}\right)^{p-1} \nabla \varphi, \nabla \bar{\eta}_{j}\right\rangle \mathrm{d} \mu_{f}-\int_{\Omega}\left\langle\left(\frac{\bar{\eta}}{g}\right)^{p-1} \nabla \varphi, \nabla \bar{\eta}\right\rangle \mathrm{d} \mu_{f}\right| .
\end{aligned}$$
As for (I), by Hölder and both the inequalities in (4.19) we deduce
$$\begin{aligned}
\frac{1}{p-1}(\mathrm{I}) & \leq c_{\Omega}^{p}\|\nabla \varphi\|_{L^{\infty}(\Omega)}\|\nabla g\|_{L^{p}(\Omega)}\left(\int_{\Omega}\left|\bar{\eta}_{j}^{p}-\bar{\eta}^{p}\right|^{\frac{p}{p-1}} \mathrm{~d} \mu_{f}\right)^{\frac{p-1}{p}} \\
& \leq c_{\Omega}^{p}\|\nabla \varphi\|_{L^{\infty}(\Omega)}\|\nabla g\|_{L^{p}(\Omega)}\left(\int_{\Omega}\left|\bar{\eta}_{j}^{\frac{p^{2}}{p-1}}-\bar{\eta}^{\frac{p^{2}}{p-1}}\right| \mathrm{d} \mu_{f}\right)^{\frac{p-1}{p}} \\
& \leq c_{\Omega}^{p}\|\nabla \varphi\|_{L^{\infty}(\Omega)}\|\nabla g\|_{L^{p}(\Omega)} C^{\frac{p-1}{p}}\left(\int_{\Omega} \max \left\{\bar{\eta}_{j}, \bar{\eta}\right\}^{\frac{p^{2}}{p-1}-1}\left|\bar{\eta}_{j}-\bar{\eta}\right| \mathrm{d} \mu_{f}\right)^{\frac{p-1}{p}} \\
& \leq c_{\Omega}^{p+\frac{p}{p-1}-\frac{p-1}{p}}\|\nabla \varphi\|_{L^{\infty}(\Omega)}\|\nabla g\|_{L^{p}(\Omega)} C^{\frac{p-1}{p}}\left(\int_{\Omega}\left|\bar{\eta}_{j}-\bar{\eta}\right| \mathrm{d} \mu_{f}\right)^{\frac{p-1}{p}}
\end{aligned}$$
Again by Hölder inequality, the last integral goes to zero since $\bar{\eta}_{j} \rightarrow \bar{\eta}$ in $L^{p}(\Omega)$, which shows that (I) → 0 as $j \rightarrow+\infty$. Finally, we consider (II). To show that (II) → 0, using the weak convergence if $\bar{\eta}_{j}$ to $\bar{\eta}$ in $W^{1, p}(\Omega)$ and standard estimates it is enough to prove that
$$\left(\frac{\bar{\eta}_{j}}{g}\right)^{p-1} \nabla \varphi \rightarrow\left(\frac{\bar{\eta}}{g}\right)^{p-1} \nabla \varphi \quad \text { strongly in } L^{\frac{p}{p-1}}(\Omega) .$$
This follows from
$$\int_{\Omega}|\nabla \varphi|^{\frac{p}{p-1}}\left|\left(\frac{\bar{\eta}_{j}}{g}\right)^{p-1}-\left(\frac{\bar{\eta}}{g}\right)^{p-1}\right|^{\frac{p}{p-1}} \mathrm{~d} \mu_{f} \leq c_{\Omega}^{p}\|\nabla \varphi\|_{L^{\infty}(\Omega)}^{\frac{p}{p-1}} \int_{\Omega}\left|\bar{\eta}_{j}^{p-1}-\bar{\eta}^{p-1}\right|^{\frac{p}{p-1}} \mathrm{~d} \mu_{f}$$
and inequalities analogous to those in the second and third lines of (4.20). This concludes the proof of (4.22).
Now, (4.22) implies that
$$\int_{\Omega}|\nabla g|^{p-2}\left\langle\nabla g, \nabla\left(\frac{\bar{\eta}_{j}^{p}}{g^{p-1}}\right)\right\rangle \mathrm{d} \mu_{f} \longrightarrow \int_{\Omega}|\nabla g|^{p-2}\left\langle\nabla g, \nabla\left(\frac{\bar{\eta}^{p}}{g^{p-1}}\right)\right\rangle \mathrm{d} \mu_{f},$$
so that integrating on $\Omega$ the Lagrangian identity
$$\mathcal{L}\left(\bar{\eta}_{j}, g\right)=\left|\nabla \bar{\eta}_{j}\right|^{p}-|\nabla g|^{p-2}\left\langle\nabla g, \nabla\left(\frac{\bar{\eta}_{j}^{p}}{g^{p-1}}\right)\right\rangle$$
and using the weak lower semicontinuity of the $W^{1, p}$ norm we deduce
$$0 \leq \int_{\Omega} \mathcal{L}(\bar{\eta}, g) \mathrm{d} \mu_{f} \leq \liminf _{j \rightarrow+\infty} \int_{\Omega} \mathcal{L}\left(\bar{\eta}_{j}, g\right) \mathrm{d} \mu_{f}$$
Inequalities (4.21) and $\mathcal{L}\left(\bar{\eta}_{j}, g\right) \geq 0$ on $M$ then imply
$$0 \leq \int_{\Omega} \mathcal{L}\left(\bar{\eta}_{j}, g\right) \mathrm{d} \mu_{f} \leq \int_{M} \mathcal{L}\left(\bar{\eta}_{j}, g\right) \mathrm{d} \mu_{f} \leq Q_{V}\left(\bar{\eta}_{j}\right) \longrightarrow 0$$
as $j \rightarrow+\infty$, so we conclude by (4.23) that $\mathcal{L}(\bar{\eta}, g) \equiv 0$ on $\Omega$. By Proposition 3.1, $\bar{\eta}=c g$ on $\Omega$ for some $c \geq 0$. In fact, $c>0$ since $\|\eta\|_{L^{p}(U)}=\lim _{j}\left\|\eta_{j}\right\|_{L^{p}(U)} \neq 0$, and $c<1$ since $\{x \in \Omega: \eta(x)<g(x)\}$ has positive measure. Therefore, $\bar{\eta} \equiv \eta$ on $\Omega$, showing that $g$ is a positive multiple of $\eta$ on $\Omega$, that is, $(i i)_{\mathrm{GS}}$ holds.
Claim 3. When $Q_{V}$ has a ground state $\eta, \eta \in C_{\text {loc }}^{1, \mu}(M)$, is positive and solves $Q_{V}^{\prime}(\eta)=0$.

Proof of Claim 3. By $(i)_{\mathrm{GS}} \Rightarrow(i i)_{\mathrm{GS}}$, all solutions $g \in C^{0}(M) \cap W_{\mathrm{loc}}^{1, p}(M)$ of $Q_{V}^{\prime}(g) \geq 0$ are proportional. Choosing $g$ to be a positive solution of $Q_{V}^{\prime}(g)=0$ (which exists by Proposition 3.4, we get that $\eta>0$ solves $Q_{V}^{\prime}(\eta)=0$ and $\eta \in C_{\text {loc }}^{1, \mu}(M)$, proving the claim.
$(\mathbf{i i i})_{\mathrm{GS}} \Rightarrow(\mathbf{i})_{\mathrm{GS}}$. Since $\operatorname{Int}(K) \neq \emptyset$ we select a closed smooth geodesic ball $B$ contained in $\operatorname{Int}(K)$. By the monotonicity of capacity, $\operatorname{cap}_{Q_{V}}(B, g)=0$. Fix an exhaustion $\{\Omega\}_{j}$ of $M$ with $B \Subset \Omega_{1}$, let $\eta_{j}$ be the $Q_{V}$-capacitor of $\left(B, \Omega_{j}, g\right)$ extended with zero outside $\Omega_{j}$, and let $\eta$ be the capacitor of $(B, g)$. Then, (4.10) ensures that $Q_{V}\left(\eta_{j}\right) \rightarrow$ $\operatorname{cap}_{Q_{V}}(B, g)=0$, and since $\eta_{j} \rightarrow \eta$ in $L_{\text {loc }}^{p}(M)$ we deduce that $\eta$ is the desired ground state.
$(\text { iv })_{\mathrm{S}} \Rightarrow(\text { iii })_{\mathrm{S}}$. Up to enlarging $K$ (capacity increases), we can assume that $K$ is the closure of a relatively compact open set with smooth boundary. Now, consider a solution $\bar{g} \in C_{\text {loc }}^{1, \mu}(M)$ of $Q_{V}^{\prime}(\bar{g})=0$ on $M$. Up to multiplying $\bar{g}$ by a small positive constant, we can suppose that $\bar{g} \leq g$ on $K$. By the very definition of $Q_{V}$-capacity,
$$\operatorname{cap}_{Q_{V}}(K, g) \geq \operatorname{cap}_{Q_{V}}(K, \bar{g}) .$$
We claim that $\operatorname{cap}_{Q_{V}}(K, \bar{g})>0$. Indeed, otherwise, by $(i i i)_{\mathrm{GS}} \Rightarrow(i)_{\mathrm{GS}}$ just proved, $Q_{V}$ has a ground state and so all solutions $u \in C^{0}(M) \cap W_{\text {loc }}^{1, p}(M)$ of $Q_{V}^{\prime}(u) \geq 0$ are proportional. In particular, $\bar{g}=c g$ for some constant $c>0$, which implies $\operatorname{cap}_{Q_{V}}(K, g)=c^{-p} \operatorname{cap}_{Q_{V}}(K, \bar{g})=0$ contradicting our assumptions. Now, since $\bar{g}$ solves $Q_{V}^{\prime}(\bar{g})=0$ and $\operatorname{cap}_{Q_{V}}(K, \bar{g})>0$, applying formula (4.12) in Proposition 4.3 with $\bar{g}$ replacing $g$ we deduce that necessarily the $Q_{V}$-capacitor $u$ of $(K, \bar{g})$ is different from $\bar{g}$. As $u$ solves $Q_{V}^{\prime}(u) \geq 0$ on $M$ and $u=g$ on $K, u$ and $\bar{g}$ are two non-proportional
solutions of $Q_{V}^{\prime}(v) \geq 0$, proving $(i i i)_{\mathrm{S}}$.
$(\mathbf{i i})_{\mathrm{GS}} \Rightarrow(\mathbf{i i i})_{\mathrm{GS}}$. If, by contradiction, $\operatorname{cap}_{Q_{V}}(K, g)>0$ for some $(K, g)$, then by $(i v)_{\mathrm{S}} \Rightarrow(i i i)_{\mathrm{S}}$ above there would exists two non-proportional solutions of $Q_{V}^{\prime}(g) \geq 0$, contradicting $(i i)_{\mathrm{GS}}$.

Now, we have concluded the equivalence $(i)_{\mathrm{GS}} \Leftrightarrow(i i)_{\mathrm{GS}} \Leftrightarrow(i i i)_{\mathrm{GS}}$ in the "ground state" part of the theorem. Combining with Claim 2, we automatically have the validity of
$(\mathbf{i})_{\mathrm{S}} \Leftrightarrow(\mathbf{i i i})_{\mathrm{S}} \Leftrightarrow(\mathbf{i v})_{\mathrm{S}}$.
We are thus left to show $(i)_{\mathrm{S}} \Leftrightarrow(i i)_{\mathrm{S}}$. Having observed that $(i)_{\mathrm{S}} \Rightarrow(i i)_{\mathrm{S}}$ is obvious (set $w=W$ ), to conclude we prove that
$(\mathbf{i i})_{\mathrm{S}} \Rightarrow(\mathbf{i})_{\mathrm{S}}$. Suppose by contradiction that $(i)_{\mathrm{S}}$ is not true. Then, by Claim 2, $Q_{V}$ has a ground state $\eta$, which is positive on $M$ and solves $Q_{V}^{\prime}(\eta)=0$. Fix a smooth open set $U$ such that $w \not \equiv 0$ on $U$, let $\left\{\Omega_{j}\right\} \uparrow M$ be an exhaustion of $M$ with $U \subseteq \Omega_{1}$, and let $\eta_{j}$ be the $Q_{V}$-capacitor of $\left(U, \Omega_{j}, \eta\right)$. Then, by the equivalence $(i)_{\mathrm{GS}} \Leftrightarrow(i i i)_{\mathrm{GS}}$ (in particular, by the proof of $\left.(i i i)_{\mathrm{GS}} \Rightarrow(i)_{\mathrm{GS}}\right),\left\{\eta_{j}\right\}$ is a null sequence. By the subcriticality assumption and since $\eta_{j}=\eta$ on $U$,
$$\int_{U} w|\eta|^{p} \mathrm{~d} \mu_{f} \leq \int_{M} w\left|\eta_{j}\right|^{p} \mathrm{~d} \mu_{f} \leq Q_{V}\left(\eta_{j}\right) \rightarrow 0$$
as $j \rightarrow+\infty$, contradicting the fact that $\eta>0$ on $M$ and $w \not \equiv 0$ on $U$. \(\square\)

Remark 4.3. We can now give a simple proof of the fact that the positivity of the Yamabe invariant $Y(M)$ in Theorem 1.1 implies the subcriticality of the conformal Laplacian $L_{\langle,\rangle}$. Indeed, suppose the contrary. Then, by Theorem 4.1, there exist a ground state $\eta>0$ and a null sequence $\left\{\eta_{j}\right\}$ locally $L^{2}$-converging to $\eta$. From the chain of inequalities
$$Y(M)\left(\int_{M}\left|\eta_{j}\right|^{\frac{2 m}{m-2}}\right)^{\frac{m-2}{m}} \leq \int_{M}\left[\left|\nabla \eta_{j}\right|^{2}+\frac{s(x)}{c_{m}} \eta_{j}^{2}\right] \rightarrow 0 \quad \text { as } j \rightarrow+\infty,$$
we deduce that $\eta_{j} \rightarrow 0$ in $L^{\frac{2 m}{m-2}}(M)$, hence locally in $L^{2}(M)$, a contradiction.
It is now immediate to prove the equivalence partly mentioned in the Introduction (Proposition 2.1). We suggest the interested reader to consult the very recent [23, 24] for an investigation on the optimality of the Hardy weights given in items 5) and 6) below.

Proposition 4.4. Let $M^{m}$ be a Riemannian manifold of dimension $m \geq 2, p \in$ $(1,+\infty)$ and $f \in C^{\infty}(M)$. The following properties are equivalent:
\begin{itemize}
\item[1)] There exists a positive, non-constant solution $g \in C^{0}(M) \cap W_{\text {loc }}^{1, p}(M)$ of $\Delta_{p, f} g \leq$ 0.
\item[2)] For some (any) compact $K \subset M$ with non-empty interior, and for some (any) solution $g$ of $\Delta_{p, f} g \leq 0, \operatorname{cap}(K, g)>0$.
\item[3)] $Q_{0}$ is subcritical on $M$ : there exists $w \in L_{\text {loc }}^{1}(M), w \geq 0, w \not \equiv 0$ on $M$ such that
\end{itemize}
$$\int_{M} w(x)|\varphi|^{p} \mathrm{~d} \mu_{f} \leq \int_{M}|\nabla \varphi|^{p} \mathrm{~d} \mu_{f} \quad \forall \varphi \in \operatorname{Lip}_{c}(M) .$$
\begin{itemize}
\item[4)] $Q_{0}$ has a weighted spectral gap on $M$ : there exists $W \in C^{0}(M), W>0$ on $M$ such that
$$\int_{M} W(x)|\varphi|^{p} \mathrm{~d} \mu_{f} \leq \int_{M}|\nabla \varphi|^{p} \mathrm{~d} \mu_{f} \quad \forall \varphi \in \operatorname{Lip}_{c}(M) .$$
\item[5)] For each non-constant, positive weak solution $u \in W_{\text {loc }}^{1, p}(M)$ of $\Delta_{p, f} u \leq 0$ the following Hardy type inequality holds:
$$\left(\frac{p-1}{p}\right)^{p} \int_{M} \frac{|\nabla u|^{p}}{u^{p}}|\varphi|^{p} \mathrm{~d} \mu_{f} \leq \int_{M}|\nabla \varphi|^{p} \mathrm{~d} \mu_{f} \quad \forall \varphi \in \operatorname{Lip}_{c}(M) .$$
\item[6)] For each $y \in M,-\Delta_{p, f}$ has a positive Green kernel $\mathcal{G}(x, y)$ and the following Hardy inequality holds:
$$\left(\frac{p-1}{p}\right)^{p} \int_{M} \frac{\left|\nabla_{x} \mathcal{G}\right|^{p}}{\mathcal{G}^{p}}|\varphi|^{p} \mathrm{~d} \mu_{f} \leq \int_{M}|\nabla \varphi|^{p} \mathrm{~d} \mu_{f} \quad \forall \varphi \in \operatorname{Lip}_{c}(M) .$$
\end{itemize}

Remark 4.4. Here, a Green kernel $\mathcal{G}(x, y)$ means a distributional solution of
$$\Delta_{p, f} \mathcal{G}(\cdot, y)=-\delta_{y},$$
where $\delta_{y}$ is the Dirac delta function at $y$.
Proof. The equivalence 1) $\Leftrightarrow 2) \Leftrightarrow 3) \Leftrightarrow 4$ ) is the particular case $V \equiv 0$ of Theorem 4.1. Indeed, as any positive constant is a solution of $\Delta_{p, f} u \leq 0,1$ ) can be rephrased as the existence of two non-proportional solutions of $\Delta_{p, f} u \leq 0$. Clearly 5) ⇒ 3), thus 5) yields that $Q_{0}$ is subcritical on $M$; therefore, we just need to show that 1) ⇒ 5). Towards this aim observe that if $g \in C^{0}(M) \cap \in W_{\text {loc }}^{1, p}(M), g>0$ is a positive, non-constant solution of $\Delta_{p, f} g \leq 0$, then by (3.14) $z=g^{\frac{p-1}{p}}$ is a positive weak solution of
$$\Delta_{p, f} z+\left(\frac{p-1}{p}\right)^{p} \frac{|\nabla u|^{p}}{u^{p}} z^{p-1} \leq 0 \quad \text { on } M .$$
Proposition 3.1 and the non-negativity of $\mathcal{L}$ then imply that $Q_{V}$ is non-negative for
$$V=\left(\frac{p-1}{p}\right)^{p} \frac{|\nabla u|^{p}}{u^{p}},$$
which gives (4.26).
To prove 6) ⇒ 1), take a positive Green kernel $\mathcal{G}(x, y)$ for $-\Delta_{p, f}$ at $y$. For large $c>0$, the function $G_{c}(x)=\min \{c, \mathcal{G}(x, y)\}$ is a non-constant, positive weak solution of $\Delta_{p, f} G_{c} \leq 0$ by the pasting Lemma 3.1, showing 1). Vice versa, if 1) holds, then by the equivalence 1) ⇔ 2) we deduce that each compact set has positive capacity with respect to the "standard" supersolution $g \equiv 1$. This implies, by results in [38] and [39], that for each $y \in M$ there exists a positive Green kernel $\mathcal{G}(x, y)$ for $-\Delta_{p, f}$. Defining again $G_{c}$ as above, $\Delta_{p, f} G_{c} \leq 0$ and the equivalence 1) ⇔ 5) ensures that the Hardy inequality
$$\left(\frac{p-1}{p}\right)^{p} \int_{M} \frac{\left|\nabla G_{c}\right|^{p}}{G_{c}^{p}}|\varphi|^{p} \mathrm{~d} \mu_{f} \leq \int_{M}|\nabla \varphi|^{p} \mathrm{~d} \mu_{f} \quad \text { holds for each } \varphi \in \operatorname{Lip}_{c}(M) \text {, }$$
and (4.27) follows by letting $c \rightarrow+\infty$ and using the monotone convergence theorem. \(\square\)

Remark 4.5. As a consequence of [75, 76] and Theorem 1.1 in [44] (see also [45]), if $M=\mathbb{R}^{m}$ each positive Green kernel $\mathcal{G}$ satisfies
$$\frac{\left|\nabla_{x} \mathcal{G}\right|^{p}}{\mathcal{G}^{p}}(x, y) \sim \begin{cases}C \operatorname{dist}(x, y)^{-m} \log ^{-m} \operatorname{dist}(x, y) & \text { if } p=m, \\ C \operatorname{dist}(x, y)^{-p} & \text { if } p<m\end{cases}$$
as $\operatorname{dist}(x, y) \rightarrow 0$, for some explicit $C>0$. In the linear case $p=2$, the first order expansions in [75, 76] guarantee the validity of (4.29) on each Riemannian manifold. On the contrary, when $p \neq 2$, the scaling arguments used in [44] are typical of the Euclidean setting and, although we believe (4.29) to be true in general, to the best of our knowledge there is still no proof of (4.29) in a manifold setting.

The above proposition gives a useful, simple criterion to check the subcriticality of some $Q_{V}$.

Proposition 4.5. Let $(M,\langle\rangle$,$) be a Riemannian manifold, f \in C^{0}(M)$ and $p>1$. Let $V \in L_{\text {loc }}^{\infty}(M)$. Suppose that $Q_{0}$ is subcritical on $M$. If, for some Hardy weight $\hat{w}$, it holds $V \leq \hat{w}$ and $V \not \equiv \hat{w}$, then $Q_{V}$ is subcritical.

Proof. Indeed, using (4.24),
$$Q_{V}(\varphi) \doteq \int_{M}|\nabla \varphi|^{p} \mathrm{~d} \mu_{f}-\int_{M} V|\varphi|^{p} \mathrm{~d} \mu_{f} \geq \int_{M}(\hat{w}-V)|\varphi|^{p} \mathrm{~d} \mu_{f} ;$$
consequently, $w$ in (2.10) can be chosen to be $\hat{w}-V$, proving the subcriticality of $Q_{V}$. \(\square\)

Remark 4.6. The alternative in Theorem 4.1 is also related to the existence of a global positive Green kernel for $Q_{V}^{\prime}$. It has been shown in [67] (Theorems 5.4 and 5.5) that, on $\mathbb{R}^{m}, Q_{V}$ has a weighted spectral gap if and only if $Q_{V}^{\prime}$ admits a global positive Green kernel. The result depends on Lemma 5.1 therein, which has been proved via a rescaling argument typical of the Euclidean space, and calls for a different strategy in a manifold setting. However, in the linear case we can easily obtain the above equivalence on general manifolds by relating $Q_{V}^{\prime}$ to a weighted Laplacian via a standard transformation. In fact, suppose that $p=2$ and that $Q_{V}$ is non-negative. Let $g$ be a positive solution of $Q_{V}^{\prime}(g)=0$. Then, setting $h=f-2 \log g$, by a simple computation the following formula holds weakly for $\varphi \in C^{2}(M)$ :
$$-\Delta_{h}\left(\frac{\varphi}{g}\right)=g^{-1} Q_{V}^{\prime}(\varphi) .$$
Note that, according to our notation, for smooth $\phi$
$$\Delta_{h} \phi=g^{-2} e^{f} \operatorname{div}\left(e^{-f} g^{2} \nabla \phi\right)$$
Integrating by parts, we infer
$$\frac{1}{2} \int_{M}\left|\nabla\left(\frac{\varphi}{g}\right)\right|^{2} g^{2} \mathrm{~d} \mu_{f}=Q_{V}(\varphi) \quad \forall \varphi \in C_{c}^{2}(M) .$$
Therefore, it is readily seen that $Q_{V}^{\prime}$ is subcritical if and only if so is $-\Delta_{h}$ with respect to the measure $g^{2} \mathrm{~d} \mu_{f}$. Now, Proposition 4.4 guarantees that this happens if and only if $-\Delta_{h}$ has a positive Green kernel $\mathcal{G}(x, y)$. Coming back with the aid of (4.30), it is easy to see that $\mathcal{G}(x, y) g(x) g(y)$ is a global positive Green kernel for $Q_{V}^{\prime}$.

\section*{5. Hardy weights and comparison geometry}

On a manifold $M$ for which $Q_{0}$ is subcritical, the criterion in Proposition 4.5 shifts the problem of the subcriticality of $Q_{V}$ to the one of finding explicit Hardy weights. As we will see in a moment, the construction of weights given in 4) and 5) of Proposition 4.4 is compatible with the usual geometric comparison theorems. Therefore, it gives a useful way to produce simple Hardy weights on manifolds satisfying suitable curvature assumptions. In this section, we describe some examples to illustrate the method.

First, we underline the following simple fact. By its very definition, the set of Hardy weights $w \in L_{\text {loc }}^{1}(M), w \geq 0, w \not \equiv 0$ is convex in $L_{\text {loc }}^{1}(M)$. More generally, given a family $\left\{w_{\alpha}\right\}_{\alpha \in A}$ of Hardy weights on $M$ whose index $\alpha$ lies in a measurable space $(A, \mathscr{F})(\mathscr{F}$ a $\sigma$-algebra), and such that the map
$$w:(x, \alpha) \in M \times A \longrightarrow w_{\alpha}(x) \in[0,+\infty]$$
is measurable, for each measure $\lambda$ on $A$ such that $0<\lambda(A) \leq 1$ the function
$$\chi(x)=\int_{A} w(x, \alpha) \mathrm{d} \lambda(\alpha)$$
is still a Hardy weight. Indeed, it is enough to apply Tonelli's theorem: for each $\varphi \in \operatorname{Lip}_{c}(M)$,
$$\begin{aligned}
\int_{M} \chi|\varphi|^{p} \mathrm{~d} \mu_{f} & =\int_{A}\left[\int_{M} w_{\alpha}(x)|\varphi(x)|^{p} \mathrm{~d} \mu_{f}\right] \mathrm{d} \lambda(\alpha) \\
& \leq \int_{A}\left[\int_{M}|\nabla \varphi|^{p} \mathrm{~d} \mu_{f}\right] \mathrm{d} \lambda(\alpha) \leq \int_{M}|\nabla \varphi|^{p} \mathrm{~d} \mu_{f}
\end{aligned}$$
Clearly, this construction makes sense also if for $\lambda$-almost all $\alpha \in A, w_{\alpha}$ is a Hardy weight.

Remark 5.1. By item 5) of Proposition 4.4, each Green kernel $\mathcal{G}$ generates a family $w$ indexed by $A=M$ :
$$w(x, y) \doteq\left(\frac{p-1}{p}\right)^{p} \frac{\left|\nabla_{x} \mathcal{G}(x, y)\right|^{p}}{\mathcal{G}(x, y)^{p}} \quad: \quad M \times M \longrightarrow[0,+\infty],$$
provided that $w$ is measurable. If $p=2$, the standard construction of a Green kernel in [34] produces a symmetric kernel, and measurability is obvious. However, measurability seems to be a subtle issue if $p \neq 2$, since $\mathcal{G}(x, y)$ is constructed in [38] and [39] by fixing $y$ and finding a solution of $\Delta_{p, f} \mathcal{G}(x, y)=-\delta_{y}$. The dependence of $\mathcal{G}(x, y)$ from $y$ could be, a priori, wild.

We now describe two simple measures $\lambda$ that have been considered in the literature when $M=\mathbb{R}^{m}$, and the corresponding Hardy inequalities.

Example 5.1. [Multipole Hardy weights]
Fix a possibly infinite sequence $\left\{y_{j}\right\} \subset M, j \in I \subset \mathbb{N}$, let $\left\{t_{j}\right\}_{j \in I} \subset(0,1]$ be such that $\sum_{j} t_{j} \leq 1$ and define
$$\lambda=\sum_{j} t_{j} \delta_{y_{j}},$$
where $\delta_{y_{j}}$ is the Dirac delta function at $y_{j}$. Being $\lambda$ discrete, measurability of $w$ follows automatically and thus, by (5.2),
$$\left(\frac{p-1}{p}\right)^{p} \int_{M}\left[\sum_{j \in I} \frac{t_{j}\left|\nabla_{x} \mathcal{G}\left(x, y_{j}\right)\right|^{p}}{\mathcal{G}\left(x, y_{j}\right)^{p}}\right]|\varphi(x)|^{p} \mathrm{~d} \mu_{f} \leq \int_{M}|\nabla \varphi(x)|^{p} \mathrm{~d} \mu_{f}$$
holds for $\varphi \in \operatorname{Lip}_{c}(M)$.
Example 5.2. [Hardy weights that blow-up along a submanifold]
If $w(x, y)$ in (5.3) is measurable, for each rectifiable subset $\Sigma \hookrightarrow M^{m}$ of finite non-zero $k$-dimensional Hausdorff measure $\mathcal{H}^{k}$ we can set
$$\lambda=\frac{\mathcal{H}^{k}\llcorner\Sigma}{\mathcal{H}^{k}(\Sigma)},$$
Then, we have the Hardy inequality
$$\left(\frac{p-1}{p}\right)^{p} \int_{M}\left[\frac{1}{\mathcal{H}^{k}(\Sigma)} \int_{\Sigma} \frac{\left|\nabla_{x} \mathcal{G}(x, y)\right|^{p}}{\mathcal{G}(x, y)^{p}} \mathrm{~d} \mathcal{H}^{k}(y)\right]|\varphi(x)|^{p} \mathrm{~d} x \leq \int_{M}|\nabla \varphi(x)|^{p} \mathrm{~d} x$$
for each $\varphi \in \operatorname{Lip}_{c}(M)$.
Hardy weights of this type have been considered, for instance, in [31]: in Theorem 1.1 therein, $M=\mathbb{R}^{m}=\mathbb{R}^{2} \times \mathbb{R}^{m-2}, p=2, f \equiv 0$ and $\Sigma \subset \mathbb{R}^{m}$ is a round circle $S_{\rho} \doteq \mathbb{S}^{1}(\rho) \times\{0\} \subset \mathbb{R}^{2} \times \mathbb{R}^{m-2}$ centered at the origin and of radius $\rho$. We remark that Hardy weights of different type but still depending on the distance from a submanifold have been investigated, among others, in [10]. The reader is also suggested to see the references therein for deepening.

To introduce the results below, we first recall comparison geometry, starting with the definition of a model manifold. Briefly, fix a point $o \in \mathbb{R}^{m}$. Given $g \in C^{2}\left(\mathbb{R}_{0}^{+}\right)$such that $g>0$ on some open interval $(0, R) \subset \mathbb{R}^{+}, g(0)=0, g^{\prime}(0)=1$, a model $\left(M_{g}^{m}, \mathrm{~d} s_{g}^{2}\right)$ is the manifold $B_{R}(o) \subset \mathbb{R}^{m}$ equipped with a radially symmetric $C^{2}$ metric $\mathrm{d} s_{g}^{2}$ whose expression, in polar geodesic coordinates $(\rho, \theta)$ centered at $o$ (where $\theta \in \mathbb{S}^{m-1}$ ), is given by
$$\mathrm{d} s_{g}^{2}=\mathrm{d} \rho^{2}+g(\rho)^{2} \mathrm{~d} \theta^{2},$$
$\mathrm{d} \theta^{2}$ being the standard metric on the unit sphere $\mathbb{S}^{m-1}$. Clearly, $\rho$ is the distance function from $o$, and $M_{g}$ is complete if and only if $R=+\infty$. At a point $x=(\rho, \theta)$, the radial sectional curvature $K_{\text {rad }}$ of $M_{g}$ (that is, the sectional curvature restricted to planes containing $\nabla \rho(x))$, the Hessian and the Laplacian of $\rho$ are given by
$$K_{\mathrm{rad}}(x)=-\frac{g^{\prime \prime}(\rho)}{g(\rho)}, \quad \nabla \mathrm{d} \rho(x)=\frac{g^{\prime}(\rho)}{g(\rho)}\left(\mathrm{d} s_{g}^{2}-\mathrm{d} \rho \otimes \mathrm{~d} \rho\right), \quad \Delta \rho(x)=(m-1) \frac{g^{\prime}(\rho)}{g(\rho)} .$$
By the first formula, in (5.6), a model can also be given by prescribing the radial sectional curvature $-G \in C^{0}\left(\mathbb{R}_{0}^{+}\right)$and recovering $g \in C^{2}\left(\mathbb{R}_{0}^{+}\right)$as the solution of
$$\left\{\begin{array}{l}
g^{\prime \prime}-G g=0 \quad \text { on } \mathbb{R}^{+}, \\
g(0)=0, \quad g^{\prime}(0)=1,
\end{array}\right.$$
on the maximal interval where $g>0$. A sharp condition on $G$ that ensures the positivity of $g$ on the whole $\mathbb{R}^{+}$is given by
$$G_{-} \in L^{1}\left(\mathbb{R}^{+}\right), \quad t \int_{t}^{+\infty} G_{-}(s) \mathrm{d} s \leq \frac{1}{4} \quad \text { on } \mathbb{R}^{+}$$
see Proposition 1.21 in [12]. In particular, if $G \equiv \kappa^{2}$ for some constant $\kappa \geq 0$, we will denote with $g_{\kappa}$ the solution $g$ of (5.7):
$$g_{\kappa}(\rho)= \begin{cases}\rho & \text { if } \kappa=0, \\ \kappa^{-1} \sinh (\kappa \rho) & \text { if } \kappa>0 .\end{cases}$$
When $\kappa=0, M_{g}$ is the Euclidean space $\mathbb{R}^{m}$, while if $\kappa>0$ our model is the hyperbolic space $\mathbb{H}_{\kappa}^{m}$ of sectional curvature $-\kappa^{2}$. Clearly, the two examples are radially symmetric with respect to any chosen origin $o$. Hereafter, we will always consider geodesically complete models.
Given $p \in(1,+\infty),-\Delta_{p}$ is subcritical on $M_{g}$ if and only if
$$g(\rho)^{-\frac{m-1}{p-1}} \in L^{1}(+\infty)$$
(the case $p=2$ can be found, for instance, in [34], and for $p \neq 2$ the argument of the proof goes along the same lines). In fact, under the validity of (5.9), up to an unessential constant, the function
$$G(x, o)=G((\rho, \theta), o)=\int_{\rho}^{+\infty} g(s)^{-\frac{m-1}{p-1}} \mathrm{~d} s$$
is the minimal positive Green kernel for $-\Delta_{p}$ with singularity at $o$.
A simplified version of the Hessian and Laplacian comparison theorems from below (see [58, 62, 12]) can be stated as follows: suppose that $(M,\langle\rangle$,$) has a pole o$ and, denoting with $r(x)=\operatorname{dist}(x, o)$, that the radial sectional curvature $K_{\text {rad }}$ satisfies
$$K_{\mathrm{rad}}(x) \leq-G(r(x))$$
(i.e., for each plane $\pi \leq T_{x} M$ containing $\nabla r(x), K(\pi) \leq-G(r(x))$ ). Denote with $g$ the solution of (5.7), and let $(0, R)$ be the maximal interval where $g>0$. Then, in the sense of quadratic forms,
$$\nabla \mathrm{d} r(x) \geq \frac{g^{\prime}(r(x))}{g(r(x))}(\langle,\rangle-\mathrm{d} r \otimes \mathrm{~d} r)$$
pointwise on $B_{R}(o) \backslash\{o\}$, and tracing
$$\Delta r(x) \geq(m-1) \frac{g^{\prime}(r(x))}{g(r(x))},$$
whose validity holds weakly on the geodesic ball $B_{R}(o) \subset M$. As it is apparent from (5.6), $M$ is compared with a model $M_{g}$ of radial sectional curvature $-G$. Indeed, via Sturm comparison, for (5.12) to hold it is enough that $g \in C^{2}\left(\mathbb{R}_{0}^{+}\right)$solves the inequality
$$\left\{\begin{array}{l}
g^{\prime \prime}-G g \leq 0 \quad \text { on } \mathbb{R}^{+}, \\
g(0)=0, \quad g^{\prime}(0)=1,
\end{array}\right.$$
so that the model to which $M$ is compared has radial sectional curvature greater than or equal to $-G$. In [13], we have collected a number of examples of $G$ for which explicit positive solutions $g$ of (5.13) can be found. These also include manifolds whose sectional curvature can be positive but in a controlled way, loosely speaking manifolds whose compared model is some sort of paraboloid.

With this preparation, we are now ready to discuss the next cases.

\subsection*{5.1. Hardy weights on manifolds with a pole.}

Theorem 5.1. Let $(M,\langle\rangle$,$) be a Riemannian manifold with a pole o$. Denoting with $r(x)=\operatorname{dist}(x, o)$, assume that the radial sectional curvature satisfies
$$K_{\mathrm{rad}} \leq-G(r(x)),$$
for some $G \in C^{2}\left(\mathbb{R}_{0}^{+}\right)$. Suppose that $g$ solving (5.13) is positive on $\mathbb{R}^{+}$, and, for $p \in(1,+\infty)$, assume that
$$g(r)^{-\frac{m-1}{p-1}} \in L^{1}(+\infty) .$$
Then, the Hardy inequality
$$\int_{M}(\chi \circ r)|\varphi|^{p} \mathrm{~d} x \leq \int_{M}|\nabla \varphi|^{p} \mathrm{~d} x$$
holds for each $\varphi \in \operatorname{Lip}_{c}(M)$, where
$$\chi(t)=\left(\frac{p-1}{p}\right)^{p}\left[g(t)^{\frac{m-1}{p-1}} \int_{t}^{+\infty} g(s)^{-\frac{m-1}{p-1}} \mathrm{~d} s\right]^{-p}$$
Proof. Consider the transplanted Green kernel of the model $M_{g}$ with pole at $o$ :
$$G(x)=\int_{r(x)}^{+\infty} g(s)^{-\frac{m-1}{p-1}}$$
Then, a computation using (5.11) shows that $\Delta_{p} G \leq 0$ on $M \backslash\{o\}$.
Furthermore, $G$ satisfies the asymptotic behaviour
$$G(x) \sim\left\{\begin{array}{ll}
C>0 & \text { if } p>m, \\
|\log r| & \text { if } p=m, \\
\frac{p-1}{m-p} r^{-\frac{m-p}{p-1}} & \text { if } p<m,
\end{array} \quad \text { as } r \rightarrow 0^{+},\right.$$
for some constant $C>0$. It thus follows that, for each $c \in(0, C)$ if $p>m$ and $c \in \mathbb{R}^{+}$ if $p \leq m$, by the pasting Lemma 3.1 the function $G_{c}=\min \{G, c\}$ is a solution of $\Delta_{p} G_{c} \leq 0$, hence by (4.4)
$$\left(\frac{p-1}{p}\right)^{p} \int_{M} \frac{\left|\nabla G_{c}\right|^{p}}{G_{c}^{p}}|\varphi|^{p} \mathrm{~d} x \leq \int_{M}|\nabla \varphi|^{p} \mathrm{~d} x \quad \text { holds for each } \varphi \in \operatorname{Lip}_{c}(M) \text {. }$$
Letting $c \rightarrow C^{-}$when $p>m, C \rightarrow+\infty$ when $p \leq m$, and since
$$\left(\frac{p-1}{p}\right)^{p} \frac{|\nabla G|^{p}}{G^{p}}(x)=\chi(r(x)),$$
we conclude the validity of (5.15). \(\square\)

The function $\chi \circ r$ has the following asymptotics as $r=r(x) \rightarrow 0^{+}$:
$$\chi(r) \sim \begin{cases}\left(\frac{p-1}{C p}\right)^{p} r^{-\frac{p(m-1)}{p-1}} & \text { if } p>m, \\ \left(\frac{m-1}{m}\right)^{m} \frac{1}{r^{m} \log ^{m} r} & \text { if } p=m, \\ \left(\frac{m-p}{p}\right)^{p} \frac{1}{r^{p}} & \text { if } p<m,\end{cases}$$
where, for $p>m$, the constant $C$ is the same as in (5.18). Note that, on each case, $\chi \circ r \in L_{\mathrm{loc}}^{1}(M)$, in particular the singularity at $o$ is integrable.

Remark 5.2. Under the same assumptions on $M$, this example can be extended to deal with the weighted operator $\Delta_{p, f}$ provided that $f=f(r(x))$ is a radial function. In this case, it can be seen that (5.14) must be replaced by
$$\frac{e^{f(r)}}{g(r)^{\frac{m-1}{p-1}}} \in L^{1}(+\infty),$$
and that
$$G(x)=\int_{r(x)}^{+\infty} \frac{e^{f(s)} \mathrm{d} s}{g(s)^{\frac{m-1}{p-1}}}$$
is a solution of $\Delta_{p, f} G \leq 0$ on $M \backslash\{o\}$ that gives rise to a Hardy weight analogous to (5.15).

The Hardy weight in (5.15) is explicit once we have an explicit $g$ solving (5.13), for example those related to the families of $G$ described in the Appendix of [13]. We refer the reader to the above mentioned paper also for a detailed study of the corresponding Hardy weight (called the "critical curve" therein) for $p=2$. The modifications needed to deal with general $p$ are straightforward. Here, we just focus on the Euclidean and hyperbolic settings.

Example 5.3. [Hardy weights for Euclidean and hyperbolic spaces]
Consider the Euclidean space, where $g(r)=g_{0}(r)=r$. Condition (5.14) is met if and only if $p<m$, and the Hardy weight (5.15) has the simple expression
$$\chi(r(x))=\left(\frac{m-p}{p}\right)^{p} \frac{1}{r(x)^{p}} .$$
Consequently, the Hardy inequality
$$\left(\frac{m-p}{p}\right)^{p} \int_{M} \frac{|\varphi|^{p}}{r^{p}} \mathrm{~d} x \leq \int_{M}|\nabla \varphi|^{p} \mathrm{~d} x \quad \forall \varphi \in \operatorname{Lip}_{c}(M)$$
holds on each manifold with a pole and radial sectional curvature $K_{\text {rad }} \leq 0$. Inequality (5.22) is classical and well-known in $\mathbb{R}^{m}$, see [10].
On the hyperbolic space $\mathbb{H}_{\kappa}^{m}$ of sectional curvature $-\kappa^{2}$, where $g_{\kappa}(r)=\kappa^{-1} \sinh (\kappa r)$, condition (5.14) is met for each $m \geq 2$ independently of $p$, but the expression of $\chi(r(x))$ is not so neat. However, an iterative argument allows us to explicitly compute the integral in the expression of $\chi$ in some relevant cases. For $\alpha>0$, set
$$I_{\alpha}(r) \doteq \int_{r}^{+\infty} \frac{\mathrm{d} s}{g_{\kappa}(s)^{\alpha}} \quad \text { and } \quad \chi_{\alpha}(r) \doteq\left(\frac{p-1}{p}\right)^{p}\left[g_{\kappa}(r)^{\alpha} I_{\alpha}(r)\right]^{-p} .$$
In view of (5.16), our case of interest is $\alpha=\frac{m-1}{p-1}$. Writing
$$\frac{I_{\alpha+2}}{\kappa^{\alpha+2}}=\int_{r}^{+\infty} \frac{\cosh (\kappa s) \cosh (\kappa s)}{\sinh ^{\alpha+2}(\kappa s)} \mathrm{d} s-\frac{I_{\alpha}}{\kappa^{\alpha}},$$
and integrating by parts, we obtain the recursion formula
$$\alpha I_{\alpha}(r)=\frac{\cosh (\kappa r)}{\kappa^{2} g_{\kappa}(r)^{\alpha+1}}-\frac{\alpha+1}{\kappa^{2}} I_{\alpha+2}(r)$$
that yields
$$\alpha \chi_{\alpha}^{-1 / p}=\frac{p \operatorname{coth}(\kappa r)}{(p-1) \kappa}-\frac{\alpha+1}{\kappa^{2} g_{\kappa}(r)^{2}} \chi_{\alpha+2}^{-1 / p} .$$

Therefore, one may inductively recover $\chi_{\alpha}$. In particular, if $\alpha=1$ (i.e., in our case of interest, $p=m$ ), by explicit integration of $I_{1}(r)$ we get
$$\chi_{1}(r)=\left(\frac{(m-1) \kappa}{m}\right)^{m}\left[\sinh (\kappa r) \log \left(\frac{e^{\kappa r}+1}{e^{\kappa r}-1}\right)\right]^{-m},$$
while if $\alpha=2$ (i.e. $m=2 p-1$ ), again by explicit integration of $I_{2}(r)$ we deduce
$$\chi_{2}(r)=\left(\frac{2(m-1) \kappa}{m+1}\right)^{\frac{m+1}{2}}\left(1-e^{-2 \kappa r}\right)^{-\frac{m+1}{2}},$$
see Example 3.15 in [12]. An important feature of $\chi_{\alpha}(r)$ is the following:
$$\chi_{\alpha}(r) \geq\left(\frac{p-1}{p}\right)^{p} \alpha^{p} \kappa^{p}, \quad \chi_{\alpha}(r) \rightarrow\left(\frac{p-1}{p}\right)^{p} \alpha^{p} \kappa^{p} \quad \text { as } r \rightarrow+\infty .$$
Indeed, the limit is straightforwardly computable. As for the first relation, it follows from the following property. To state it, for fixed $\alpha>0$ and for $g$ satisfying $1 / g^{\alpha} \in$ $L^{1}(+\infty)$, write
$$\chi_{g}(r) \doteq\left(\frac{p-1}{p}\right)^{p}\left(g(r)^{\alpha} \int_{r}^{+\infty} \frac{\mathrm{d} s}{g(s)^{\alpha}}\right)^{-p} .$$
Then, the next comparison result holds:
if $g_{1} / g_{2}$ is non-decreasing on $\mathbb{R}^{+}$(respectively, non-increasing),
then $\chi_{g_{1}} \geq \chi_{g_{2}}$ on $\mathbb{R}^{+}$(resp, $\leq$).
The proof of this fact goes along the same lines as in Proposition 3.12 in [12], and is left to the interested reader. Using this with $g_{1}(r) \doteq g_{\kappa}(r)$ and $g_{2}(r) \doteq \exp \{\kappa r\}$ we get
$$\chi_{g_{1}}(r) \geq \chi_{g_{2}}(r) \equiv\left(\frac{p-1}{p}\right)^{p} \alpha^{p} \kappa^{p},$$
as claimed.
When each point of the manifold $M$ is a pole, we can construct multipole Hardy weights by the standard procedure described at the beginning of Section 5. This is the case if, for example, $M$ is a Cartan-Hadamard manifold, that is, a simply-connected, complete manifold with non-positive sectional curvature.

Theorem 5.2. For $m \geq 2$, let $M^{m}$ be a Cartan-Hadamard manifold satisfying $K \leq$ $-\kappa^{2}$, for some constant $H \geq 0$. Given the solution $g_{\kappa}$ of (5.8), let
$$\begin{cases}p \in(1, m) & \text { if } \kappa=0 \\ p \in(1,+\infty) & \text { if } \kappa>0 .\end{cases}$$
Then, for each unit measure $\lambda$ on $M$, the Hardy inequality
$$\int_{M}\left[\int_{M}(\chi(\operatorname{dist}(x, y))) \mathrm{d} \lambda(y)\right]|\varphi(x)|^{p} \mathrm{~d} x \leq \int_{M}|\nabla \varphi(x)|^{p} \mathrm{~d} x$$
holds for each $\varphi \in \operatorname{Lip}_{c}(M)$, where
$$\chi(t)=\left(\frac{p-1}{p}\right)^{p}\left[g_{\kappa}(t)^{\frac{m-1}{p-1}} \int_{t}^{+\infty} g_{\kappa}(s)^{-\frac{m-1}{p-1}} \mathrm{~d} s\right]^{-p} .$$
In particular, when $\kappa=0$, for each $\varphi \in \operatorname{Lip}_{c}(M)$
$$\left(\frac{m-p}{p}\right)^{p} \int_{M}\left[\int_{M} \frac{\mathrm{~d} \lambda(y)}{\operatorname{dist}(x, y)^{p}}\right]|\varphi(x)|^{p} \mathrm{~d} x \leq \int_{M}|\nabla \varphi(x)|^{p} \mathrm{~d} x .$$

Proof. By (5.26), (5.14) is met for $g=g_{\kappa}$. Since each $y \in M$ is a pole of $M$, setting $r_{y}(\cdot)=\operatorname{dist}(\cdot, y)$ one can apply Theorem 5.1 to deduce that (5.15) holds for each fixed $y$, namely,
$$\int_{M}\left(\chi \circ r_{y}\right)|\varphi|^{p} \mathrm{~d} x \leq \int_{M}|\nabla \varphi|^{p} \mathrm{~d} x \quad \forall \varphi \in \operatorname{Lip}_{c}(M),$$
where $\chi$ is as in (5.28). The generalization in (5.27) follows from the argument at the beginning of Section 5. \(\square\)

\subsection*{5.2. Hardy weights on minimally immersed submanifolds.}

Theorem 5.3. Let $F:\left(M^{m},\langle\rangle,\right) \rightarrow\left(N^{n},(),\right)$ be an immersed, minimal submanifold of a Cartan-Hadamard ambient space $N^{n}$, and suppose that the sectional curvature $\bar{K}$ of $N$ satisfies $\bar{K} \leq-\kappa^{2}$, for some constant $H \geq 0$. If $\kappa=0$, we assume that $m \geq 3$. Then, given the solution $g_{\kappa}$ of (5.8), and denoting with $\bar{r}_{q}$ the extrinsic distance from a point $q \in N$ evaluated along the immersion $F$, the following Hardy inequality holds:
$$\int_{M}\left(\chi \circ \bar{r}_{q}\right) \varphi^{2} \mathrm{~d} x \leq \int_{M}|\nabla \varphi|^{2} \mathrm{~d} x \quad \forall \varphi \in \operatorname{Lip}_{c}(M),$$
where
$$\chi(t)=\frac{1}{4}\left[g_{\kappa}(t)^{m-1} \int_{t}^{+\infty} g_{\kappa}(s)^{1-m} \mathrm{~d} s\right]^{-2} .$$
In particular, if $\kappa=0$,
$$\left(\frac{m-2}{2}\right)^{2} \int_{M} \frac{\varphi^{2}}{\bar{r}_{q}^{2}} \mathrm{~d} x \leq \int_{M}|\nabla \varphi|^{2} \mathrm{~d} x, \quad \forall \varphi \in \operatorname{Lip}_{c}(M),$$
while, if $\kappa>0$,
\begin{itemize}
\item[-] when $m=2$, that is, $M$ is a surface, for each $\varphi \in \operatorname{Lip}_{c}(M)$
\end{itemize}
$$\left(\frac{\kappa}{2}\right)^{2} \int_{M}\left[\sinh \left(\kappa \bar{r}_{q}\right) \log \left(\frac{e^{\kappa \bar{r}_{q}}+1}{e^{\kappa \bar{r}_{q}}-1}\right)\right]^{-2} \varphi^{2} \mathrm{~d} x \leq \int_{M}|\nabla \varphi|^{2} \mathrm{~d} x ;$$
- when $m=3$, for each $\varphi \in \operatorname{Lip}_{c}(M)$
$$\kappa^{2} \int_{M} \frac{\varphi^{2}}{\left(1-e^{-2 \kappa \bar{r}_{q}}\right)^{2}} \mathrm{~d} x \leq \int_{M}|\nabla \varphi|^{2} \mathrm{~d} x .$$

Remark 5.3. The inequality in (5.33) has been proved in [19, 49] by combining the comparison for the Hessian of the extrinsic distance function with an integration by parts argument. The case $\kappa>0$ has been considered in [49, Example 1.8]. However, the Hardy weight found there is skew with (5.34) and (5.35), in particular it is quite smaller if $\bar{r}_{q}$ is close to zero. As before, other Hardy weights can be constructed in the way described in Examples (5.1) and (5.2).

Proof. We mark with a bar each quantity when referred to $N$, so that, for example, $\bar{\nabla}$, $\overline{\text { dist }}$ are the Riemannian connection and the distance function of $N$. For simplicity, we denote with $\bar{r}_{q}$ the distance function from $q$ in the manifold $N$, i.e. $\bar{r}_{q}(\cdot)=\overline{\operatorname{dist}}(\cdot, q)$, so that the function $\bar{r}_{q}$ in the statement of the theorem is, indeed, $\bar{r}_{q} \circ F$. By the Hessian comparison theorem (5.11), for each $q \in N$ it holds
$$\bar{\nabla} \mathrm{d} \bar{r}_{q} \geq \frac{g_{\kappa}^{\prime}\left(\bar{r}_{q}\right)}{g_{\kappa}\left(\bar{r}_{q}\right)}\left((,)-\mathrm{d} \bar{r}_{q} \otimes \mathrm{~d} \bar{r}_{q}\right) \quad \text { on } N \backslash\{q\} .$$

For $x \in M, q \in N$ define
$$G_{q}(x)=h\left(\bar{r}_{q}(F(x))\right), \quad \text { where } h(t)=\int_{t}^{+\infty} \frac{\mathrm{d} s}{g_{\kappa}(s)^{m-1}} .$$
Observe that the integral in $h(t)$ converges for each $m \geq 2$ when $\kappa>0$, and for each $m \geq 3$ if $\kappa=0$, which accounts for our dimensional restrictions. Denote with II the second fundamental form of $F$. By the chain rule and using $h^{\prime}<0$, for each vector field $X$ on $M$ (identified with $F_{*}(X)$ ) we get
$$\begin{aligned}
\nabla \mathrm{d} G_{q}(X, X) & =h^{\prime \prime}\left(\bar{\nabla} \bar{r}_{q}, X\right)^{2}+h^{\prime} \bar{\nabla} \mathrm{d} \bar{r}_{q}(X, X)+h^{\prime}\left(\bar{\nabla} \bar{r}_{q}, \mathrm{II}(X, X)\right) \\
& \leq\left(h^{\prime \prime}-\frac{g_{\kappa}^{\prime}}{g_{\kappa}} h^{\prime}\right)\left(\bar{\nabla} \bar{r}_{q}, X\right)^{2}+h^{\prime} \frac{g_{\kappa}^{\prime}}{g_{\kappa}}|X|^{2}+h^{\prime}\left(\bar{\nabla} \bar{r}_{q}, \mathrm{II}(X, X)\right) \\
& =-m h^{\prime} \frac{g_{\kappa}^{\prime}}{g_{\kappa}}\left(\bar{\nabla} \bar{r}_{q}, X\right)^{2}+h^{\prime} \frac{g_{\kappa}^{\prime}}{g_{\kappa}}|X|^{2}+h^{\prime}\left(\bar{\nabla} \bar{r}_{q}, \mathrm{II}(X, X)\right) \\
& =h^{\prime} \frac{g_{\kappa}^{\prime}}{g_{\kappa}}\left[|X|^{2}-m\left(\bar{\nabla} \bar{r}_{q}, X\right)^{2}\right]+h^{\prime}\left(\bar{\nabla} \bar{r}_{q}, \mathrm{II}(X, X)\right)
\end{aligned}$$
Tracing with respect to an orthonormal frame $\left\{e_{i}\right\}$ of $M$, using minimality and again $h^{\prime}<0$, we obtain
$$\Delta G_{q} \leq m h^{\prime} \frac{g_{\kappa}^{\prime}}{g_{\kappa}}\left(1-\left|\bar{\nabla}^{T} \bar{r}_{q}\right|^{2}\right) \leq 0$$
where $\bar{\nabla}^{T}$ is the component of the gradient in $N$ which is tangent to $M$. By Proposition 4.4
$$\frac{\left|\nabla G_{q}(x)\right|^{2}}{4 G_{q}(x)^{2}}=\left(\frac{h^{\prime}\left(\bar{r}_{q}\right)}{2 h\left(\bar{r}_{q}\right)}\right)^{2}\left|\bar{\nabla}^{T} \bar{r}_{q}\right|^{2}=\chi\left(\bar{r}_{q}(F(x))\right)\left|\bar{\nabla}^{T} \bar{r}_{q}\right|^{2} .$$
is a Hardy weight. Unfortunately, such a weight is not effective, since we cannot control the size of $\bar{\nabla}^{T} \bar{r}_{q}$. However, we can improve (5.38) to the effective Hardy weight $\chi\left(\bar{r}_{q}\right)$ by using the full information coming from (5.37). In fact, since $h^{\prime}<0$, by (5.37) the function $u_{1} \doteq \sqrt{G_{q}}$ solves, on $M \backslash f^{-1}\{q\}$,
$$\begin{aligned}
\Delta u_{1} & =\left[\frac{\Delta G_{q}}{2 G_{q}}-\chi\left(\bar{r}_{q}\right)\left|\bar{\nabla}^{T} \bar{r}_{q}\right|^{2}\right] u_{1} \leq\left[m \frac{h^{\prime}}{2 h} \frac{g_{\kappa}^{\prime}}{g_{\kappa}}\left(1-\left|\bar{\nabla}^{T} \bar{r}_{q}\right|^{2}\right)-\chi\left(\bar{r}_{q}\right)\left|\bar{\nabla}^{T} \bar{r}_{q}\right|^{2}\right] u_{1} \\
& \leq\left[-m \sqrt{\chi\left(\bar{r}_{q}\right)} \frac{g_{\kappa}^{\prime}}{g_{\kappa}}+\sqrt{\chi\left(\bar{r}_{q}\right)}\left|\bar{\nabla}^{T} \bar{r}_{q}\right|^{2}\left(m \frac{g_{\kappa}^{\prime}}{g_{\kappa}}-\sqrt{\chi\left(\bar{r}_{q}\right)}\right)\right] u_{1} .
\end{aligned}$$
Now, we claim that
$$\zeta(t) \doteq m \frac{g_{\kappa}^{\prime}(t)}{g_{\kappa}(t)}-\sqrt{\chi(t)} \geq 0 \quad \text { for } t \in \mathbb{R}^{+} \text {. }$$
Indeed, in the Euclidean case $\kappa=0, g_{\kappa}(t)=t$ and explicit computation gives
$$\zeta(t)=\frac{m+2}{2 t}>0 \quad \text { on } \mathbb{R}^{+} .$$
When $\kappa>0, g_{\kappa}(t)=\kappa^{-1} \sinh (\kappa t)$. A computation gives
$$\zeta(t) \sim \frac{m+2}{2 t} \quad \text { as } t \rightarrow 0, \quad \zeta(t) \sim \frac{(m+1) \kappa}{2} \quad \text { as } t \rightarrow+\infty .$$