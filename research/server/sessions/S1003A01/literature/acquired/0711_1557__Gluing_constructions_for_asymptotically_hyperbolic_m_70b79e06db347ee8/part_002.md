---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: [0711.1557] Gluing constructions for asymptotically hyperbolic manifolds with constant scalar curvature]

First, we have $\widehat{g}(\rho)-\widehat{b}(\rho)=O\left(\rho^{\sigma}\right)$ and $\partial_{\rho}[\widehat{g}-\widehat{b}](\rho)=O\left(\rho^{\sigma-1}\right)$, so that
$$\begin{gathered}
\delta_{\widehat{g}}(z)-{ }^{\delta} \widehat{b}(z)=O\left(\delta^{\sigma}\right) \\
\partial_{z}\left[\delta^{\delta} \widehat{g}-{ }^{\delta} \widehat{b}\right](z)=\delta O\left(\delta^{\sigma-1}\right)=O\left(\delta^{\sigma}\right) .
\end{gathered}$$
The non-trivial Christoffel symbols of $g_{\delta}$ are
$$\begin{gathered}
{ }^{\delta} \Gamma_{z z}^{z}=-z^{-1}={ }^{\delta} \Gamma_{z z}^{z}\left(b_{\delta}\right), \\
\delta^{\delta} \Gamma_{A B}^{z}={ }^{\delta} \Gamma_{A B}^{z}\left(b_{\delta}\right)+O\left(\delta^{\sigma-2}\right)_{A B}, \\
{ }^{\delta} \Gamma_{A z}^{C}={ }^{\delta} \Gamma_{z A}^{C}={ }^{\delta} \Gamma_{A z}^{C}\left(b_{\delta}\right)+O\left(\delta^{\sigma}\right)_{A}^{C}, \\
{ }^{\delta} \Gamma_{A B}^{C}=\Gamma_{A B}^{C}\left({ }^{\delta} \widehat{g}\right)={ }^{\delta} \widehat{\Gamma}_{A B}^{C}\left({ }^{\delta} \widehat{b}\right)+O\left(\delta^{\sigma}\right)_{A B}^{C} .
\end{gathered}$$
Let $\nu$ be a one-form on $A$. To make things clear, let ${ }^{\delta} \widetilde{\nabla}$ denote the covariant derivative operator of the metric $b_{\delta}$ and ${ }^{\delta} \nabla$ the one for $g_{\delta}$, we have
$$\begin{gathered}
{ }^{\delta} \nabla_{z} \nu_{z}=\partial_{z} \nu_{z}+z^{-1} \nu_{z}, \\
{ }^{\delta} \nabla_{z} \nu_{A}={ }^{\delta} \widetilde{\nabla}_{z} \nu_{A}+O\left(\delta^{\sigma}\right)_{A}^{C} \nu_{C}, \\
{ }^{\delta} \nabla_{A} \nu_{z}={ }^{\delta} \widetilde{\nabla}_{A} \nu_{z}+O\left(\delta^{\sigma}\right)_{A}^{C} \nu_{C}, \\
\delta^{\delta} \nabla_{A} \nu_{B}={ }^{\delta} \widetilde{\nabla}_{A} \nu_{B}+O\left(\delta^{\sigma-2}\right)_{A B} \nu_{z}+O\left(\delta^{\sigma}\right)_{A B}^{C} \nu_{C},
\end{gathered}$$
where the error terms are measured with any fixed metric on the compact set $\bar{A}$, e.g. $d z^{2}+\widehat{b}(0)$.

If $\nu=d u$, then
$$\begin{gathered}
{ }^{\delta} \nabla_{z} \partial_{z} u=\partial_{z}^{2} u+z^{-1} \partial_{z} u={ }^{\delta} \widetilde{\nabla}_{z} \partial_{z} u, \\
{ }^{\delta} \nabla_{z} \partial_{A} u={ }^{\delta} \widetilde{\nabla}_{z} \partial_{A} u+O\left(\delta^{\sigma}\right)_{A}^{C} \partial_{C} u, \\
{ }^{\delta} \nabla_{A} \partial_{B} u={ }^{\delta} \widetilde{\nabla}_{A} \partial_{B} u+O\left(\delta^{\sigma-2}\right)_{A B} \partial_{z} u+O\left(\delta^{\sigma}\right)_{A B}^{C} \partial_{C} u,
\end{gathered}$$
thus
$${ }^{\delta} \nabla^{k} \partial_{k} u={ }^{\delta} \widetilde{\nabla}^{k} \partial_{k} u+O\left(\delta^{\sigma}\right) \partial_{z} u+O\left(\delta^{\sigma+2}\right)^{A B \delta} \widehat{\widetilde{\nabla}}_{B} \partial_{A} u+O\left(\delta^{\sigma+2}\right)^{C} \partial_{C} u .$$
We obtain for the components of $P_{g_{\delta}}^{*} u$ :
$$\begin{aligned}
\left(P_{g_{\delta}}^{*} u\right)_{z z}= & \left(P_{b_{\delta}}^{*} u\right)_{z z}+O\left(\delta^{\sigma}\right) \partial_{z} u+O\left(\delta^{\sigma}\right) u+O\left(\delta^{\sigma+2}\right)^{A B} \delta \widehat{\widetilde{\nabla}}_{B} \partial_{A} u+O\left(\delta^{\sigma+2}\right)^{C} \partial_{C} u \\
& \left(P_{g_{\delta}}^{*} u\right)_{z A}=\left(P_{b_{\delta}}^{*} u\right)_{z A}+O\left(\delta^{\sigma}\right)_{A}^{C} \partial_{C} u+O\left(\delta^{\sigma-1}\right)_{A} u \\
\left(P_{g_{\delta}}^{*} u\right)_{A B}= & \left(P_{b_{\delta}}^{*} u\right)_{A B}+O\left(\delta^{\sigma-2}\right)_{A B} \partial_{z} u+O\left(\delta^{\sigma}\right)_{B}^{C} \widehat{\widetilde{\nabla}}_{C} \partial_{A} u+O\left(\delta^{\sigma}\right)_{A B}^{C} \partial_{C} u+O\left(\delta^{\sigma-2}\right)_{A B} u
\end{aligned}$$

Next, we compute the explicit expression of $P_{b_{\delta}}^{*}$ for a metric of the form (2.3). In that case we have
$$\delta \widehat{b}(z)=\left[1-k\left(\frac{\delta z}{2}\right)^{2}\right]^{2} \widehat{b},$$
then
$$\partial_{z}\left({ }^{\delta} \widehat{b}\right)(z)=-k \delta^{2} z\left[1-k\left(\frac{\delta z}{2}\right)^{2}\right] \widehat{b}$$

The non-trivial Christoffel symbols of $b_{\delta}$ are
$$\begin{gathered}
\delta^{z} \Gamma_{z z}^{z}=-z^{-1} \\
{ }^{\delta} \Gamma_{A B}^{z}=\delta^{-2} z^{-1}\left[1-k\left(\frac{\delta z}{2}\right)^{2}\right]\left[1+k\left(\frac{\delta z}{2}\right)^{2}\right] \widehat{b}_{A B} \\
{ }^{\delta} \Gamma_{A z}^{C}=-z^{-1}\left[1-k\left(\frac{\delta z}{2}\right)^{2}\right]^{-1}\left[1+k\left(\frac{\delta z}{2}\right)^{2}\right] \delta_{A}^{C} \\
\delta_{\Gamma_{A B}^{C}}=\Gamma_{A B}^{C}(\widehat{b}) .
\end{gathered}$$
We thus obtain for the components of the Hessian of $u$ :
$$\begin{gathered}
\delta \widetilde{\nabla}_{z} \partial_{z} u=\partial_{z}^{2} u+z^{-1} \partial_{z} u \\
\delta \widetilde{\nabla}_{z} \partial_{A} u=\partial_{z} \partial_{A} u+z^{-1}\left[1-k\left(\frac{\delta z}{2}\right)^{2}\right]^{-1}\left[1+k\left(\frac{\delta z}{2}\right)^{2}\right] \partial_{A} u, \\
\delta \widetilde{\nabla}_{A} \partial_{B} u=\widehat{\nabla}_{A} \partial_{B} u-\delta^{-2} z^{-1}\left[1-k\left(\frac{\delta z}{2}\right)^{2}\right]\left[1+k\left(\frac{\delta z}{2}\right)^{2}\right] \widehat{b}_{A B} \partial_{z} u,
\end{gathered}$$
thus
$$\begin{aligned}
{ }^{\delta} \widetilde{\nabla}^{k} \partial_{k} u=z^{2} \partial_{z}^{2} u+\{1-(n-1) & {\left.\left[1-k\left(\frac{\delta z}{2}\right)^{2}\right]^{-1}\left[1+k\left(\frac{\delta z}{2}\right)^{2}\right]\right\} z \partial_{z} u } \\
& +z^{2} \delta^{2}\left[1-k\left(\frac{\delta z}{2}\right)^{2}\right]^{-2} \widehat{\nabla}^{A} \partial_{A} u
\end{aligned}$$

One checks that $\operatorname{Ric}(b)=-(n-1) b$, which implies
$$\operatorname{Ric}\left(b_{\delta}\right)=-(n-1) b_{\delta} .$$
We obtain for the components of $P_{b_{\delta}}^{*} u$ :
$$\begin{aligned}
\left(P_{b_{\delta}}^{*} u\right)_{z z}= & (n-1)\left\{\left[1-k\left(\frac{\delta z}{2}\right)^{2}\right]^{-1}\left[1+k\left(\frac{\delta z}{2}\right)^{2}\right] z^{-1} \partial_{z} u+z^{-2} u\right. \\
& \left.-\frac{1}{n-1} \delta^{2}\left[1-k\left(\frac{\delta z}{2}\right)^{2}\right]^{-2} \widehat{\nabla}^{A} \partial_{A} u\right\} \\
\left(P_{b_{\delta}}^{*} u\right)_{z A}= & \partial_{z} \partial_{A} u+z^{-1}\left[1-k\left(\frac{\delta z}{2}\right)^{2}\right]^{-1}\left[1+k\left(\frac{\delta z}{2}\right)^{2}\right] \partial_{A} u, \\
\left(P_{b_{\delta}}^{*} u\right)_{A B}= & \widehat{\nabla}_{A} \partial_{B} u-\widehat{\nabla}^{C} \partial_{C} u \widehat{b}_{A B}-\delta^{-2} z^{-2}\left[1-k\left(\frac{\delta z}{2}\right)^{2}\right]^{2}\left\{z^{2} \partial_{z}^{2} u\right. \\
& \left.+z\left(1-(n-2) \frac{1+k\left(\frac{\delta z}{2}\right)^{2}}{1-k\left(\frac{\delta z}{2}\right)^{2}}\right) \partial_{z} u-(n-1) u\right\}_{\widehat{b} A B}
\end{aligned}$$

Now, a function $u$ is in the kernel of $P_{b_{\delta}}^{*}$ if and only if
$${ }^{\delta} \nabla \partial u=u b_{\delta} .$$
One checks that
$$u_{0}=z^{-1}\left[1+k\left(\frac{\delta z}{2}\right)^{2}\right],$$
is indeed in this kernel. Further, if $v$ is a non trivial solution of the Obatatype equation
$$\widehat{\nabla}_{A} \partial_{B} v=-k v \widehat{b}_{A B}$$
on the boundary at infinity, then the function
$$u=v z^{-1}\left[1-k\left(\frac{\delta z}{2}\right)^{2}\right]$$
satisfies $\left(P_{b_{\delta}}^{*} u\right)_{z z}=\left(P_{b_{\delta}}^{*} u\right)_{z A}=0$, with $\left(\left(P_{b_{\delta}}^{*} u\right)_{A B}=0\right.$ if and only if $\left.k=1\right)$. Finally, it is an easy exercise to show that these functions generate the kernel of $P_{b_{\delta}}^{*}$. Here one can use the well known fact that the kernel of $P^{*}$ has dimension at most $n+1$ (see, e.g., [12]).

\section*{Appendix B. Proof of Lemma 3.6}

Throughout this appendix we write $A_{\delta}$ for $A_{\delta, 4 \delta}$ and $A$ for $A_{1,4}$; we hope that the clash of notation with the $A$-spaces occasionally used elsewhere will not confuse the reader. We start by scaling $A_{\delta}$ to $A=(1,4) \times \partial M$. Recall that the weight function $\phi=y^{2}$ on $A$ relevant for the calculation at hand equals $(z-1)^{2}(z-4)^{2} / 9$, where $z$ runs along the $(1,4)$ factor of $A$. The argument that follows actually applies to any non-negative function $\phi=\phi(z)$ which vanishes precisely at the boundary of $A$ and satisfies:
$$\phi(1)=\phi(4)=\phi^{\prime}(1)=\phi^{\prime}(4)=0, \quad \phi^{\prime \prime}(1)>0, \phi^{\prime \prime}(4)>0 .$$

The idea of the proof is to cover $(1,4)$ by intervals $I_{i}$, with sizes chosen so that on each interval the ratio $\sup \phi / \inf \phi$ is bounded independently of $i$. Furthermore, the size of each interval should be of the order of the value of $\phi$ on the interval, to ensure good scaling properties. We then use interior elliptic estimates after a cube decomposition of $I_{i} \times \partial M$; this requires a second family of thickened intervals $\widehat{I}_{i}$, with properties similar to the ones satisfied by the $I_{i}$ 's. Summing over the cubes provides the desired estimate, after having ensured that the $\widehat{I}_{i}$ 's do not overlap too much. We note that the scalings in $z$ and $\theta^{A}$ are different; the former is tailored to account for the degeneracy in the "radial" $z$-direction, measured by $\phi$, and the latter accounting for the $\phi \delta$-dependent degeneracy in the "angular" $\theta^{A}$-direction.

So we divide $(1,4)$ into intervals
$$I_{k} \subset \widehat{I}_{k} \subset(1,4), \quad \cup_{k} I_{k}=(1,4),$$
as follows: There exists $1<z_{1}<5 / 2$ such that $\phi:\left[1, z_{1}\right] \rightarrow \mathbb{R}^{+}$is strictly increasing. Choose $a>0$ small enough so that
$$z-2 a \phi(z)>1 \text { on }\left(1, z_{1}\right] \text { and } z_{1}+a\left(\phi\left(z_{1}\right)\right) \leq 4 .$$
Define $z_{i}$ by induction using
$$z_{i+1}=z_{i}-a \phi\left(z_{i}\right)$$
thus $1<z_{i+1}<z_{i}$, and $\lim _{i \rightarrow \infty} z_{i}=1$. For any function $f \in L^{1}(A)$ we thus have
$$\int_{\left[1, z_{1}\right] \times \partial M} f=\sum_{i} \int_{\left[z_{i+1}, z_{i}\right] \times \partial M} f .$$
We want to show that there exists a constant $C$ such that for all $a$ small enough and for all positive integrable functions $f$ we have
$$\sum_{i} \int_{\left[z_{i}-2 a \phi\left(z_{i}\right), z_{i}+a \phi\left(z_{i}\right)\right] \times \partial M} f \leq C \int_{[1,4] \times \partial M} f$$
In order to do that we need to count how many of the intervals $\left[z_{i}-\right.$ $\left.2 a \phi\left(z_{i}\right), z_{i}+a \phi\left(z_{i}\right)\right]$ overlap. Letting $b:=a \phi^{\prime \prime}(1) / 2$, one easily finds
$$\begin{aligned}
z_{i}-2 a \phi\left(z_{i}\right)-1 & =\left(z_{i}-1\right)\left(1-2 b\left(z_{i}-1\right)\right)+O\left(\left(z_{i}-1\right)^{3}\right) \\
z_{i+k}-1 & =\left(z_{i}-1\right)\left(1-k b\left(z_{i}-1\right)\right)+O\left(\left(z_{i}-1\right)^{3}\right) \\
z_{i+k}+a \phi\left(z_{i+k}\right)-1 & =\left(z_{i}-1\right)\left(1-(k-1) b\left(z_{i}-1\right)\right)+O\left(\left(z_{i}-1\right)^{3}\right)
\end{aligned}$$
where the error terms in the second and third equation depend upon $k$. Choosing $k=4$, it follows that
$$z_{i+k}+a \phi\left(z_{i+k}\right)<z_{i}-2 a \phi\left(z_{i}\right)$$
for all $i$ large enough. So for $i$ large enough $\left[z_{i}-2 a \phi\left(z_{i}\right), z_{i}+a \phi\left(z_{i}\right)\right]$ will intersect at most six such other intervals, and (B.3) with a constant $C \geq 6$ follows.

An obvious modification of the above construction, decreasing $a$ if necessary, will lead to a sequence $z_{k}^{\prime} \rightarrow 4$ satisfying
$$5 / 2<z_{1}^{\prime} \leq z_{i}^{\prime}=z_{i+1}^{\prime}-a \phi\left(z_{i+1}^{\prime}\right)<z_{i+1}^{\prime}<4,$$
with, for $f \in L^{1}(A)$,
$$\int_{\left[z_{1}^{\prime}, 4\right] \times \partial M} f=\sum_{i} \int_{\left[z_{i}^{\prime}, z_{i+1}^{\prime}\right] \times \partial M} f,$$
and if moreover $f$ is positive then
$$\sum_{i} \int_{\left[z_{i}^{\prime}-2 a \phi\left(z_{i}^{\prime}\right), z_{i}^{\prime}+a \phi\left(z_{i}^{\prime}\right)\right] \times \partial M} f \leq C \int_{[1,4] \times \partial M} f$$

Letting $\left\{I_{k}\right\}_{k \in \mathbb{N}}$ be the collection, without repetitions, of the intervals
$$\{\underbrace{\left[z_{1}, z_{1}^{\prime}\right]}_{=: I_{1}},\left[z_{i+1}, z_{i}\right],\left[z_{j}^{\prime}, z_{j+1}^{\prime}\right]\}_{i, j \in \mathbb{N}^{*}},$$
and letting $\left\{\widehat{I}_{k}\right\}_{k \in \mathbb{N}}$ be the collection, without repetitions, of the intervals
$$\{\underbrace{\left[z_{1}-a \phi\left(z_{1}^{\prime}\right), z_{1}^{\prime}+a \phi\left(z_{1}^{\prime}\right)\right]}_{=: \widehat{I}_{1}},\left[z_{i}-2 a \phi\left(z_{i}\right), z_{i}+a \phi\left(z_{i}\right)\right],\left[z_{j}^{\prime}-2 a \phi\left(z_{j}^{\prime}\right), z_{j}^{\prime}+a \phi\left(z_{j}^{\prime}\right)\right]\}_{i, j \in \mathbb{N}^{*}},$$
we obtain (B.1) together with
$$\begin{gathered}
\int_{[1,4] \times \partial M} f=\sum_{k} \int_{I_{k} \times \partial M} f \\
C^{-1} \int_{[1,4] \times \partial M} f \leq \sum_{k} \int_{\widehat{I}_{k} \times \partial M} f \leq C \int_{[1,4] \times \partial M} f,
\end{gathered}$$
for positive $f \in L^{1}(A)$. We set
$$\tilde{z}_{k}=\sup I_{k} .$$

The above construction provides a $\delta$-independent decomposition of $A$ into stripes $I_{k} \times \partial M$, the size of which in the $z$-direction is comparable to $\phi(z)$ for any $(z, v) \in I_{k} \times \partial M$; similarly the sizes of $\widehat{I}_{k} \times \partial M$ are comparable to $\phi(z)$ for any $(z, v) \in \widehat{I}_{k} \times \partial M$. Mapping $A$ to $A_{\delta}$ provides an associated decomposition of $A_{\delta}$ into stripes $I_{k}^{\delta} \times \partial M$ with sizes uniformly comparable to $\phi(\rho / \delta)$ for any $(\rho, v) \in I_{k}^{\delta} \times \partial M$; similarly for $\widehat{I}_{k}^{\delta} \times \partial M$.

We continue with a $\delta$-dependent, and stripe dependent, cube decomposition of $\partial M$, as follows: Let $\left\{\left(\mathscr{O}_{i}, \psi_{i}\right)\right\}_{i=1, \ldots, N}$ be a covering of $M$ by coordinate charts with each coordinate system $\psi_{i}^{-1}$ mapping $\mathscr{O}_{i}$ smoothly and diffeomorphically to a neighbourhood of $[0,1]^{n-1}$; the local coordinates on $[0,1]^{n-1}$ will be denoted by $\theta^{A}$. We further assume that $\cup \psi_{i}\left([0,1]^{n-1}\right)$ covers $\partial M$ as well. Let $\varphi_{i}$ be an associated decomposition of unity, thus $\sum_{i} \varphi_{i}=1$. Setting $f_{i}=\left(\varphi_{i} f\right) \circ \psi_{i}$, for any integrable function $f$ we have
$$\int_{[1,4] \times \partial M} f=\sum_{i=1}^{N} \int_{[1,4] \times[0,1]^{n-1}} f_{i} .$$

Given $\delta$ satisfying $0<\delta<1 / \sup _{[1,4]} \phi$ and given an interval $I_{k}$ define $m=m(k, \delta) \in \mathbb{N}$ by the inequality
$$\frac{1}{m+1} \leq \phi\left(\tilde{z}_{k}\right) \delta<\frac{1}{m} .$$

Let $\left\{K_{j}\right\}$ be the collection of closed $(n-1)$-cubes, with pairwise disjoint interiors, and with edges of size $1 / m$, covering $[0,1]^{n-1}$. For any $K_{j}$ let $\widehat{K}_{j}$ be the union of those cubes $K_{i}$ which have non-empty intersection with $K_{j}$. Note that there exists a number $\widehat{N}(n)$ such that $\widehat{K}_{j}$ is consists of at most $\widehat{N}(n)$ cubes $K_{i}$. It follows that for any integrable function $f_{i}$ we have
$$\int_{[1,4] \times[0,1]^{n-1}} f_{i}=\sum_{k} \int_{[1,4] \times K_{k}} f_{i},$$
and if $f_{i} \geq 0$ then
$$\int_{[1,4] \times[0,1]^{n-1}} f_{i} \leq \sum_{k} \int_{[1,4] \times \widehat{K}_{k}} f_{i} \leq \widehat{N}(n) \int_{[1,4] \times[0,1]^{n-1}} f_{i} .$$

We are ready now to pass to the heart of our argument. Let $\left\{\mathscr{U}_{\ell}\right\}_{\ell \in \mathbb{N}}$ be the collection, without repetitions, of the sets
$$\left\{I_{k} \times \psi_{i}\left(K_{j}\right)\right\}_{k \in \mathbb{N}, i=1, \ldots, N, j=0, \ldots, m^{n-1}} .$$
Similarly let $\left\{\widehat{\mathscr{U}}_{\ell}\right\}_{\ell \in \mathbb{N}}$ be the collection, without repetitions, of the sets
$$\left\{\widehat{I}_{k} \times \psi_{i}\left(\widehat{K}_{j}\right)\right\}_{k \in \mathbb{N}, i=1, \ldots, N, j=0, \ldots, m^{n-1}} .$$
From what has been said we have, for any positive integrable function $f$,
$$\begin{gathered}
\int_{[1,4] \times \partial M} f \leq \sum_{\ell} \int_{\mathscr{U}_{\ell}} f \leq N \int_{[1,4] \times \partial M} f, \\
\int_{[1,4] \times \partial M} f \leq \sum_{\ell} \int_{\widehat{\mathscr{U}}_{\ell}} f \leq N \widehat{N}(n) \int_{[1,4] \times \partial M} f .
\end{gathered}$$
If $\mathscr{U}_{\ell}=I_{k} \times \psi_{i}\left(K_{j}\right)$ set $\phi_{\ell}=\phi\left(\tilde{z}_{k}\right)$. Scale the local coordinates $\left(z, \theta^{A}\right)$ in $\widehat{\mathscr{U}}_{\ell}$ as
$$\left(z, \theta^{A}\right) \mapsto\left(z / \phi_{\ell}, m \theta^{A}\right) .$$
Up to translations, this maps all $\mathscr{U}_{\ell} \subset \widehat{\mathscr{U}}_{\ell}$ 's to fixed cubes
$$\mathscr{U}_{\ell} \longrightarrow[0, a] \times[0,1]^{n} \subset[-a, 2 a] \times[-1,2]^{n} \longleftarrow \widehat{\mathscr{U}}_{\ell},$$
except for those which correspond to $I_{1} \times \psi_{i}\left(K_{j}\right)$, which are mapped to $\mathscr{U}_{\ell} \longrightarrow\left[0, a\left(z_{1}^{\prime}-z_{1}\right) / \phi\left(z_{1}^{\prime}\right)\right] \times[0,1]^{n} \subset\left[-a, a+a\left(z_{1}^{\prime}-z_{1}\right) / \phi\left(z_{1}^{\prime}\right)\right] \times[-1,2]^{n} \longleftarrow \widehat{\mathscr{U}}_{\ell}$, By construction there exists a constant $C>0$, independent of $i$, such that we have
$$\sup _{I_{i} \times \partial M} \phi \leq C \inf _{I_{i} \times \partial M} \phi, \quad \sup _{\widehat{I}_{i} \times \partial M} \phi \leq C \inf _{\widehat{I}_{i} \times \partial M} \phi,$$
hence the same is true on each $\mathscr{U}_{\ell}$ and $\widehat{\mathscr{U}}_{\ell}$. Let $\psi=e^{-s / 2 y}$; it is shown at the end of [8, Appendix B] that one also has
$$\sup _{I_{i} \times \partial M} \psi \leq C \inf _{I_{i} \times \partial M} \psi, \quad \sup _{\widehat{I}_{i} \times \partial M} \psi \leq C \inf _{\widehat{I}_{i} \times \partial M} \psi$$
(with perhaps a different constant $C$ ), and again such $\ell$-independent inequalities hold on the $\mathscr{U}_{\ell}$ 's and $\widehat{\mathscr{U}}_{\ell}$ 's. At this stage in is important to realize that
$$L_{g_{\delta}}=B\left(\phi \partial_{z}, \phi \delta \partial_{\theta^{A}}\right),$$
where $B$ is uniformly elliptic of order 4 (see equation (A.4) in [8]) on the relevant cubes. We can also write
$$g_{\delta}=z^{-2}\left(d z^{2}+\delta^{2} \widehat{g}_{A B}(\delta z) d \theta^{A} d \theta^{B}\right)=z^{-2}\left(d z^{2}+\widehat{g}_{A B}(\delta z) d(\delta \theta)^{A} d(\delta \theta)^{B}\right) .$$
It then follows from the usual elliptic interior estimates [19, p. 246] for the operator $B$ and scaling that (here $g=g_{\delta}$ )
$$\sum_{i \leq k+4} \int_{\mathscr{U}_{\ell}} \psi^{2} \phi^{2 i}\left|\nabla^{(i)} u\right|_{g}^{2} \leq C\left(\sum_{i \leq k} \int_{\widehat{\mathscr{U}}_{\ell}} \psi^{2} \phi^{2 i}\left|\nabla^{(i)} L u\right|_{g}^{2}+\int_{\widehat{\mathscr{U}}_{\ell}} \psi^{2}|u|^{2}\right),$$
where $C$ does not depend upon $\delta$ nor $g$ close to $b$. Summing over $\ell$, Lemma 3.6 follows. \(\square\)

Acknowledgements We are grateful to two anonymous referees for suggesting many improvements to the original version of this paper.

\section*{References}
\begin{itemize}
\item[1.] L. Andersson, M. Cai, and G.J. Galloway, Rigidity and positivity of mass for asymptotically hyperbolic manifolds, Ann. Henri Poincaré 9 (2008), 1-33, arXiv:math.dg/0703259. MR MR2389888 (2009e:53054)
\item[2.] L. Andersson and P.T. Chruściel, On asymptotic behavior of solutions of the constraint equations in general relativity with "hyperboloidal boundary conditions", Dissert. Math. 355 (1996), 1-100. MR MR1405962 (97e:58217)
\item[3.] L. Andersson, P.T. Chruściel, and H. Friedrich, On the regularity of solutions to the Yamabe equation and the existence of smooth hyperboloidal initial data for Einsteins field equations, Commun. Math. Phys. 149 (1992), 587-612. MR MR1186044 (93i:53040)
\item[4.] R. Beig, P.T. Chruściel, and R. Schoen, KIDs are non-generic, Ann. H. Poincaré 6 (2005), 155-194, arXiv:gr-qc/0403042. MR MR2121280 (2005m:83013)
\item[5.] D. Birmingham, Topological black holes in anti-de Sitter space, Class. Quantum Grav. 16 (1999), 1197-1205, arXiv:hep-th/9808032. MR MR1696149 (2000c:83062)
\item[6.] P.T. Chruściel, The Hamiltonian mass and asymptotically anti-de Sitter space-times, Proceedings of the Symposium "100 Years Werner Heisenberg-Works and Impact" (Bamberg, 2001), vol. 50, 2002, pp. 624-629. MR MR1909102 (2003h:83034)
\item[7.] P.T. Chruściel and E. Delay, Existence of non-trivial asymptotically simple vacuum space-times, Class. Quantum Grav. 19 (2002), L71-L79, arXiv:gr-qc/0203053, erratum-ibid, 3389. MR MR1902228 (2003e:83024a)
\item[8.] $\_\_\_\_$, On mapping properties of the general relativistic constraints operator in weighted function spaces, with applications, Mém. Soc. Math. de France. 94 (2003), vi+103, arXiv:gr-qc/0301073v2. MR MR2031583 (2005f:83008)
\item[9.] $\_\_\_\_$, Manifold structures for sets of solutions of the general relativistic constraint equations, Jour. Geom Phys. (2004), 442-472, arXiv:gr-qc/0309001v2. MR MR2085346 (2005i:83008)
\item[10.] P.T. Chruściel and M. Herzlich, The mass of asymptotically hyperbolic Riemannian manifolds, Pacific J. Math. 212 (2003), 231-264, arXiv:dg-ga/0110035. MR MR2038048 (2005d:53052)
\item[11.] P.T. Chruściel and D. Pollack, Singular Yamabe metrics and initial data with exactly Kottler-Schwarzschild-de Sitter ends, Ann. H. Poincaré (2008), 639-654, arXiv:0710.3365 [gr-qc].
\item[12.] J. Corvino, Scalar curvature deformation and a gluing construction for the Einstein constraint equations, Commun. Math. Phys. 214 (2000), 137-189. MR MR1794269 (2002b:53050)
\item[13.] J. Corvino and R.M. Schoen, On the asymptotics for the vacuum Einstein constraint equations, Jour. Diff. Geom. 73 (2006), 185-217, arXiv:gr-qc/0301071. MR MR2225517 (2007e:58044)
\end{itemize}
14. F. Kottler, Über die physikalischen Grundlagen der Einsteinschen Gravitationstheorie, Annalen der Physik 56 (1918), 401-462.
15. W. Kuehnel, Conformal transformations between Einstein spaces, Conformal geometry (Bonn, 1985/1986) (R.S. Kulkarni and U. Pinkall, eds.), Aspects Math., E12, F. Vieweg \& Sohn, Braunschweig, 1988, pp. 105-146. MR MR979791 (90b:53055)
16. J.M. Lee, Fredholm operators and Einstein metrics on conformally compact manifolds, Mem. Amer. Math. Soc. 183 (2006), vi+83, arXiv:math.DG/0105046. MR MR2252687
17. R. Mazzeo, The Hodge cohomology of a conformally compact metric, Jour. Diff. Geom. 28 (1988), 309-339. MR MR961517 (89i:58005)
18. $\_\_\_\_$, Unique continuation at infinity and embedded eigenvalues for asymptotically hyperbolic manifolds, Am. Jour. Math. 113 (1991), 25-45.
19. C.B. Morrey, Multiple integrals in the calculus of variation, Die Grundlehren der mathematischen Wissenschaften, Band 130, Springer Verlag, Berlin, Heidelberg, New York, 1966. MR MR0202511 (34 \#2380)
20. M. Obata, The conjectures of conformal transformations of Riemannian manifolds., Bull. Amer. Math. Soc. 77 (1971), 265-270. MR MR0270397 (42 \#5286)
21. R. Schoen, Variational theory for the total scalar curvature functional for Riemannian metrics and related topics, Topics in calculus of variations (Montecatini Terme, 1987), Lecture Notes in Math., vol. 1365, Springer, Berlin, 1989, pp. 120-154. MR MR994021 (90g:58023)
22. X. Wang, Mass for asymptotically hyperbolic manifolds, Jour. Diff. Geom. 57 (2001), 273-299. MR MR1879228 (2003c:53044)

Piotr T. Chruściel, LMPT, Fédération Denis Poisson, Tours; Mathematical Institute and Hertford College, Oxford.
E-mail address: chrusciel@maths.ox.ac.uk
URL: http://www.phys.univ-tours.fr/ ~piotr
Erwann Delay, Laboratoire d'analyse non linéaire et géométrie, Faculté des Sciences, 33 rue Louis Pasteur, 84000 Avignon, France
E-mail address: Erwann.Delay@univ-avignon.fr
URL: http://www.math.univ-avignon.fr/Delay