---
retention_scope: session
part: 2
total_parts: 4
---

[Part 2/4 of: [math/0105046] Fredholm Operators and Einstein Metrics on Conformally Compact Manifolds]

For $k \geq 1$, to show that $u \in C_{(0)}^{k, \alpha}(\bar{M})$, it suffices to show that $u$ is bounded and $V u \in C_{(0)}^{k-1, \alpha}(\bar{M})$ whenever $V$ is a smooth vector field on $\bar{M}$. It is straightforward to check that any such vector field maps $C_{k+\alpha}^{k, \alpha}(M)$ into $C_{k-1+\alpha}^{k-1, \alpha}(M)$. Thus if $u \in$ $C_{k+\alpha}^{k, \alpha}(M)$, then $V u \in C_{k-1+\alpha}^{k-1, \alpha}(M) \subset C_{(0)}^{k-1, \alpha}(\bar{M})$ by induction, with norm bounded by $\|u\|_{k, \alpha, k+\alpha}$. Since $|u|$ is obvious uniformly bounded by $\|u\|_{k, \alpha, k+\alpha}$, it follows that $u \in C_{(0)}^{k, \alpha}(\bar{M})$.

Finally, let $E$ be a $\binom{p}{q}$ tensor bundle. If $u \in C_{k+\alpha+r}^{k, \alpha}(M ; E)$, to show that $u \in$ $C_{(0)}^{k, \alpha}(\bar{M} ; E)$ we have to show that the components of $u$ in any background coordinate domain $\Omega$ are in $C_{(0)}^{k, \alpha}(\Omega)$. These components are given by complete contractions of tensor products of $u$ with tensors of the form $\partial_{\theta^{i_{1}}} \otimes \cdots \otimes \partial_{\theta^{i_{p}}} \otimes d \theta^{j_{1}} \otimes \cdots \otimes d \theta^{j_{q}}$, each of which is in $C_{-r}^{l, \beta}\left(\Omega ; T_{p}^{q} M\right)$. By Lemma in $C_{k+\alpha}^{k, \alpha}\left(\Omega ; E \otimes T_{p}^{q} M\right)$. Since complete contraction clearly maps this space into $C_{k+\alpha}^{k, \alpha}(\Omega)$, the result for tensor fields follows from the scalar case. \(\square\)

Lemma 3.8. Let $\psi: \mathbb{R}^{+} \rightarrow[0,1]$ be a smooth function that is equal to 1 on $\left[0, \frac{1}{2}\right]$ and supported in [0, 1), and set $\psi_{\varepsilon}(q)=\psi(\rho(q) / \varepsilon)$ for $q \in M$. If $0 \leq \alpha<1$ and $0 \leq k+\alpha \leq l+\beta$, then $\psi_{\varepsilon} \in C^{k, \alpha}(M)$, with norm bounded independently of $\varepsilon$.

Proof. Working directly with the definition of $C^{k, \alpha}(M)$, for any Möbius coordinate chart $\Phi_{p_{0}}$, we have to show that $\Phi_{p_{0}}^{*} \psi_{\varepsilon}(x, y)=\psi\left(\rho\left(p_{0}\right) y / \varepsilon\right)$ is uniformly bounded in $C^{k, \alpha}\left(B_{2}\right)$. Since $e^{-2}<y<e^{2}$ on $B_{2}, \Phi_{p_{0}}^{*} \psi_{\varepsilon}$ will be identically equal to 0 or 1 on $B$ unless $\frac{1}{2} \varepsilon e^{-2}<\rho\left(p_{0}\right)<\varepsilon e^{2}$. Under these restrictions, it is easy to verify that $\psi\left(\rho\left(p_{0}\right) y / \varepsilon\right)$ is uniformly bounded in $C^{k, \alpha}\left(B_{2}\right)$. \(\square\)

Lemma 3.9. If $1<p<\infty, \delta \in \mathbb{R}$, and $0 \leq k \leq l$, the set of compactly supported smooth tensor fields is dense in $H_{\delta}^{k, p}(M ; E)$.

Proof. Suppose $u \in H_{\delta}^{k, p}(M ; E)$. First we show that $u$ can be approximated in the $H_{\delta}^{k, p}$ norm by compactly supported elements of $H_{\delta}^{k, p}(M ; E)$.

Let $\psi_{\varepsilon}$ be as in the preceding lemma. We will show that $\left(1-\psi_{\varepsilon}\right) u \rightarrow u$ in $H_{\delta}^{k, p}$ as $\varepsilon \rightarrow 0$, which by Lemma $\nabla_{-1}^{4}$ is the same as $\nabla^{j}\left(\psi_{\varepsilon} u\right) \rightarrow 0$ in $H_{\delta}^{0, p}$ whenever $0 \leq j \leq k$. By the product rule,
$$\nabla^{j}\left(\psi_{\varepsilon} u\right)=\sum_{i=0}^{j} C_{i} \nabla^{j-i} \psi_{\varepsilon} \otimes \nabla^{i} u .$$
Since $\left|\nabla^{j-i} \psi_{\varepsilon}\right|_{g}$ is bounded and supported where $\rho \leq 2 \varepsilon$, we have
$$\left\|\nabla^{j-i} \psi_{\varepsilon} \otimes \nabla^{i} u\right\|_{0, p, \delta}^{p} \leq C \int_{\{\rho \leq 2 \varepsilon\}}\left|\rho^{-\delta} \nabla^{i} u\right|_{g}^{p} d V_{g}$$
By Lemma $4 .\left.\rho^{-\delta} \nabla^{i} u\right|_{g} ^{p}$ is integrable, so the integral on the right-hand side above goes to zero as $\varepsilon \rightarrow 0$ by the dominated convergence theorem.

Next we must check that if $u \in H_{\delta}^{k, p}(M ; E)$ is compactly supported in $M$, it can be approximated in the $H_{\delta}^{k, p}$ norm by smooth, compactly supported tensor fields. The classical argument involving convolution with an approximate identity shows that $u$ can be approximated in the standard Sobolev $H^{k, p}$ norm on a slightly
larger compact set by tensor fields in $C_{c}^{\infty}(M ; E)$. However, on any fixed compact subset of $M$, it is easy to see that the $H_{\delta}^{k, p}$ norm is equivalent to the $H^{k, p}$ norm, thus completing the proof. \(\square\)

\section*{CHAPTER 4}

\section*{Elliptic Operators}

In this chapter, we collect some basic facts regarding elliptic operators on asymptotically hyperbolic manifolds. Throughout this chapter we assume $(M, g)$ is a connected asymptotically hyperbolic $(n+1)$-manifold of class $C^{l, \beta}$ for some $l \geq 2$ and $0 \leq \beta<1$, and $\rho$ is a fixed smooth defining function.

Let $E$ and $F$ be geometric tensor bundles over $M$. We will say a linear partial differential operator $P: C^{\infty}(M ; E) \rightarrow C^{\infty}(M ; F)$ is a geometric operator of order $m$ if the components of $P u$ in any coordinate frame are given by linear functions of the components of $u$ and their partial derivatives, whose coefficients are universal polynomials in the components of the metric $g$, their partial derivatives, and the function $\left(\operatorname{det} g_{i j}\right)^{-1}$ (or $\left(\operatorname{det} g_{i j}\right)^{-1 / 2}$ if $M$ is oriented), such that the coefficient of any $j$ th derivative of $u$ involves at most the first $m-j$ derivatives of the metric. A geometric operator is, in particular, an example of a regular natural differential operator in the terminology introduced by P. Stredder [55]. We note that such an operator is automatically invariant under (orientation-preserving) isometries. By the results of [55], $P$ is geometric of order $m$ if and only if $P u$ can be written as a sum of contractions of tensors of the form
$$\begin{aligned}
\nabla^{j} u \otimes \nabla^{k_{1}} R m \otimes \cdots \otimes & \nabla^{k_{l}} R m \otimes \\
& \underbrace{g \otimes \cdots \otimes g}_{p \text { factors }} \otimes \underbrace{g^{-1} \otimes \cdots \otimes g^{-1}}_{q \text { factors }} \otimes \underbrace{d V_{g} \otimes \cdots \otimes d V_{g}}_{s \text { factors }},
\end{aligned}$$
(possibly after reordering indices), with $0 \leq j \leq m$ and $0 \leq k_{i} \leq m-j-2$, and with $s=0$ unless $M$ is oriented. Here $R m$ is the (covariant) Riemann curvature tensor of $g$, and $d V_{g}$ is its Riemannian volume form.

If $E$ and $F$ are tensor bundles over $\bar{M}$, a differential operator $P: C^{\infty}(M ; E) \rightarrow$ $C^{\infty}(M ; F)$ is said to be uniformly degenerate if it can be written in background coordinates as a system of operators that are polynomials in $\rho \partial / \partial \theta^{i}$ with coefficients that are at least continuous up to the boundary.

Lemma 4.1. Let $(M, g)$ be an asymptotically hyperbolic $(n+1)$-manifold of class $C^{l, \beta}, 0 \leq \beta<1$. Suppose $E$ is a geometric tensor bundle over $M$, and $P: C^{\infty}(M ; E) \rightarrow C^{\infty}(M ; E)$ is a geometric operator of order $m \leq l$. Then $P$ is uniformly degenerate.

Proof. As noted above, for any section $u$ of $E, P u$ can be written as a sum of contractions of terms like (4.1). If $u$ is covariant of degree $r_{1}$ and contravariant of degree $r_{2}$, then this tensor product has $r_{2}+2 q$ upper indices and $r_{1}+j+2 p+(n+$ $1) s+4 l+\sum_{i} k_{i}$ lower indices. (The $4 l$ lower indices are the undifferentiated indices of the $l$ copies of $R m$.) Because we are assuming that $P u$ is the same type of tensor as $u, 2 q$ of the upper indices must be contracted against $j+2 p+(n+1) s+4 l+\sum_{i} k_{i}$
of the lower indices, so in particular we must have
$$2 q=j+2 p+(n+1) s+4 l+\sum_{i} k_{i} .$$

It is obvious that tensoring with $\bar{g}=\rho^{2} g, \bar{g}^{-1}=\rho^{-2} g^{-1}$, and $d V_{\bar{g}}=\rho^{n+1} d V_{g}$ are all uniformly degenerate operators. Using formula (3.10) for the components of the difference tensor $D=\nabla-\bar{\nabla}$, we see that the components of $\rho D_{i j}^{k}$ in background coordinates are $C^{l, \beta}$ up to the boundary. It follows that $(\rho \nabla)^{j}=(\rho \bar{\nabla}+\rho D)^{j}$ is a uniformly degenerate operator for $0 \leq j \leq l$. Since $[\nabla, \rho] u=u \otimes d \rho$ is also uniformly degenerate, it follows by induction that $\rho^{j} \nabla^{j}$ is uniformly degenerate as well.

A straightforward computation (cf. [40, 29]) shows that the components of $R m$ are given by
$$R_{i j k l}=-|d \rho|_{\bar{g}}^{2}\left(g_{i k} g_{j l}-g_{i l} g_{j k}\right)+\rho^{-3} p_{1}\left(\bar{g}, \bar{g}^{-1}, \partial \bar{g}\right)+\rho^{-2} p_{2}\left(\bar{g}, \bar{g}^{-1}, \partial \bar{g}, \partial^{2} \bar{g}\right),$$
where $p_{1}$ and $p_{2}$ are universal polynomials, so $\rho^{4} R m \in C_{(0)}^{l-2, \beta}\left(\bar{M}, T^{4} \bar{M}\right)$. Moreover, an easy induction shows that for $k \leq l-2, \rho^{4+k} \nabla^{k} R m \in C_{(0)}^{l-2-k, \beta}\left(\bar{M}, T^{4} \bar{M}\right)$. It follows that tensoring with $\rho^{4+k} \nabla^{k} R m$ is a uniformly degenerate operator. By virtue of $(4.2)$, therefore, we can rewrite $(4.1)$ in the following manifestly uniformly degenerate form:
$$\begin{aligned}
\rho^{j} \nabla^{j} u \otimes \rho^{4+k_{1}} \nabla^{k_{1}} R m & \otimes \cdots \otimes \rho^{4+k_{l}} \nabla^{k_{l}} R m \otimes \rho^{2} g \otimes \cdots \otimes \rho^{2} g \otimes \\
& \rho^{-2} g^{-1} \otimes \cdots \otimes \rho^{-2} g^{-1} \otimes \rho^{n+1} d V_{g} \otimes \cdots \otimes \rho^{n+1} d V_{g} .
\end{aligned}$$
Since contraction of a lower index against an upper one is also uniformly degenerate, the result follows. \(\square\)

If $P$ is a uniformly degenerate operator, for each $s \in \mathbb{C}$ we define the indicial map of $P$ to be the bundle map $I_{s}(P):\left.\left.E\right|_{\partial M} \rightarrow E\right|_{\partial M}$ defined by
$$I_{s}(P)(\bar{u})=\left.\left(\rho^{-s} P\left(\rho^{s} \bar{u}\right)\right)\right|_{\partial M},$$
where $\rho$ is any smooth defining function, and $\bar{u}$ is extended arbitrarily to a $C^{m}$ section of $E$ in a neighborhood of $\partial M$. It is easy to check that the indicial map of any uniformly degenerate operator is a continuous bundle map, which is independent of the extension or the choice of defining function. For geometric operators, we can say more.

Lemma 4.2. Suppose $(M, g)$ is an asymptotically hyperbolic $(n+1)$-manifold of class $C^{l, \beta}$, and $P: C^{\infty}(M ; E) \rightarrow C^{\infty}(M ; E)$ is a geometric operator of order $m \leq l$. Then for each $s \in \mathbb{C}, I_{s}(P):\left.\left.E\right|_{\partial M} \rightarrow E\right|_{\partial M}$ is a $C^{l, \beta}$ bundle map.

Proof. It is an immediate consequence of the definition of the indicial map that if $P_{1}$ and $P_{2}$ are uniformly degenerate operators with sufficiently smooth coefficients, then
$$\begin{aligned}
I_{s}\left(P_{1} \circ P_{2}\right) & =I_{s}\left(P_{1}\right) \circ I_{s}\left(P_{2}\right) \\
I_{s}\left(P_{1}+P_{2}\right) & =I_{s}\left(P_{1}\right)+I_{s}\left(P_{2}\right)
\end{aligned}$$
Since a sum or composition of two $C^{l, \beta}$ bundle maps is again of class $C^{l, \beta}$, it suffices to display $P$ as a sum of compositions of uniformly degenerate operators with $C^{l, \beta}$ indicial maps.

Writing $P$ as a sum of contractions of terms of the form (4.4), we see that it suffices to show that each of the following uniformly degenerate operators has $C^{l, \beta}$ indicial map:
\begin{itemize}
\item[(a)] $u \mapsto \rho^{j} \nabla^{j} u$;
\item[(b)] $u \mapsto u \otimes \rho^{4+k} \nabla^{k} R m$.
\item[(c)] $u \mapsto u \otimes \rho g$;
\item[(d)] $u \mapsto u \otimes \rho^{-1} g^{-1}$;
\item[(e)] $u \mapsto u \otimes \rho^{n+1} d V_{g}$.
\end{itemize}

The last three operators above are themselves $C^{l, \beta}$ bundle maps over $\bar{M}$, whose indicial maps are just their restrictions to $\partial M$, so there is nothing to prove in those cases. For (a), observe that $\rho^{j} \nabla^{j} u$ can be written as a sum of compositions of the operators $[\rho, \nabla]$ and $\rho \nabla$. Since the commutator $[\rho, \nabla] u=-u \otimes d \rho$ is a smooth bundle map and therefore has smooth indicial map, we need only consider the operator $\rho \nabla$. Let $D=\nabla-\bar{\nabla}$ be the difference tensor as in the preceding proof, and observe that for any $\bar{u} \in C_{(0)}^{1}(\bar{M} ; E)$,
$$\begin{aligned}
\rho^{-s}\left(\rho \nabla\left(\rho^{s} \bar{u}\right)\right) & =\rho^{-s}\left(\rho \bar{\nabla}\left(\rho^{s} \bar{u}\right)+\rho D\left(\rho^{s} \bar{u}\right)\right) \\
& =s \bar{u} \otimes d \rho+\rho D(\bar{u})+O(\rho) .
\end{aligned}$$
As noted above, $\bar{u} \mapsto \bar{u} \otimes d \rho$ is a smooth bundle map; and it follows from (3.10') that $\rho D$ is a $C^{l, \beta}$ bundle map. Therefore the indicial map of $\rho \nabla$ is $C^{l, \beta}$ as claimed.

To analyze the remaining operator, $u \mapsto u \otimes \rho^{4+k} \nabla^{k} R m$, let $K$ be the 4-tensor field on $M$ whose components are
$$K_{i j k l}=-\left(g_{i k} g_{j l}-g_{i l} g_{j k}\right),$$
and let $\bar{K}$ be
$$\bar{K}_{i j k l}=-\left(\bar{g}_{i k} \bar{g}_{j l}-\bar{g}_{i l} \bar{g}_{j k}\right)=\rho^{4} K_{i j k l} .$$
Because the assumption that $g$ is asymptotically hyperbolic means that $|d \rho|_{\bar{g}}=1$ on $\partial M$, we can write $|d \rho|_{\bar{g}}=1+\rho v$, where $v \in C_{(0)}^{l-1, \beta}(\bar{M})$. Using $(4.3)$, therefore, we can write
$$R m=K+\rho^{-3} \bar{V}=\rho^{-4} \bar{K}+\rho^{-3} \bar{V},$$
where $\bar{V} \in C_{(0)}^{l-2, \beta}\left(\bar{M}, T^{4} \bar{M}\right)$. It follows that $I_{s}\left(u \mapsto u \otimes \rho^{4} R m\right)$ is just tensoring with $\left.\bar{K}\right|_{\partial M}$, which is a $C^{l, \beta}$ bundle map. On the other hand, Lemma that
$$\begin{aligned}
R m-K & =\rho^{-3} \bar{V} \in \rho^{-3} C_{(0)}^{l-2, \beta}\left(\bar{M} ; T^{4} \bar{M}\right) \\
& \subset \rho^{-3} C_{4}^{l-2, \beta}\left(M ; T^{4} M\right)=C_{1}^{l-2, \beta}\left(M ; T^{4} M\right)
\end{aligned}$$
Because $K$ is parallel, $\nabla^{k} R m=\nabla^{k}(R m-K) \in C_{1}^{l-2-k, \beta}\left(M ; T^{4} M\right)$. In particular, this implies that
$$\left|\rho^{4+k} \nabla^{k} R m\right|_{\bar{g}}=\left|\nabla^{k} R m\right|_{g}=O(\rho),$$
so $\rho^{4+k} \nabla^{k} R m$ has vanishing indicial map for $k>0$. \(\square\)

A complex number $s$ is called a characteristic exponent of $P$ at $\widehat{p} \in \partial M$ if $I_{s}(P)$ is singular at $\widehat{p}$. Its multiplicity is the dimension of the kernel of $I_{s}(P): E_{\widehat{p}} \rightarrow$ $E_{\widehat{p}}$. If $s$ is a characteristic exponent of $P$ somewhere on $\partial M$, we just say it is a characteristic exponent of $P$.

Let $(\mathbb{B}, \breve{g})$ be the unit ball model of hyperbolic space as described in Chapter let $\breve{E}$ denote the tensor bundle over $\mathbb{B}$ that corresponds to $E$ (i.e., associated to the same representation of $\mathrm{O}(n+1)$ or $\mathrm{SO}(n+1))$, and let $\breve{P}: C^{\infty}(\mathbb{B} ; \breve{E}) \rightarrow C^{\infty}(\mathbb{B} ; \breve{E})$ be the geometric operator on $\breve{E}$ whose coordinate formula is the same as that of $P$. Because $\breve{P}$ is invariant under (orientation-preserving) isometries of $\mathbb{B}$, and Euclidean rotations in the unit ball model of hyperbolic space are isometries of $\breve{g}$ that act transitively on the sphere $\mathbb{S}^{n}=\partial \mathbb{B}$, it follows that the characteristic exponents of $\breve{P}$ and their multiplicities are constant on $\partial \mathbb{B}$. The next lemma shows that the analogous statement holds for $P$ as well.

Lemma 4.3. Let $(M, g)$ be a connected asymptotically hyperbolic $(n+1)$ manifold of class $C^{l, \beta}$, and let $P: C^{\infty}(M ; E) \rightarrow C^{\infty}(M ; E)$ be a geometric operator of order $m \leq l$. The characteristic exponents of $P$ and their multiplicities are constant on $\partial M$, and are the same as those of $\breve{P}$.

Proof. Let $\widehat{p} \in \partial M$ be arbitrary, and let $(\theta, \rho)$ be any background coordinates defined on a neighborhood of $\widehat{p}$ in $\bar{M}$. By an affine change of background coordinates, we may arrange that $\widehat{p}=(0,0)$ and $\bar{g}_{i j}=\delta_{i j}$ at $\widehat{p}$. Let $\Phi: V \rightarrow M$ be the Möbius chart given by $(\theta, \rho)=\Phi(x, y)=(x, y)$ in terms of these background coordinates, defined on some neighborhood $V$ of $(0,0)$ in $\overline{\mathbb{H}}$. Let $\widetilde{g}$ be the Riemannian metric $\Phi^{*} g$ on $V \cap \mathbb{H}$, let $\widetilde{P}=\Phi^{*} \circ P \circ \Phi^{-1 *}$, and let $I_{s}(\widetilde{P})(\bar{u})=y^{-s} \widetilde{P}\left(y^{s} \bar{u}\right)$ be the indicial map of $\widetilde{P}$. Then $I_{s}(\widetilde{P})=\Phi^{*} \circ I_{s}(P) \circ \Phi^{-1 *}$, so the characteristic exponents and multiplicities of $\widetilde{P}$ at $(0,0) \in \partial \mathbb{H}$ are the same as those of $P$ at $\Phi(x, 0)$. Thus it suffices to show that $I_{s}(\widetilde{P})=I_{s}(\breve{P})$ at (0, 0).

For convenience, here is a summary of the several metrics being considered in this proof:
$$\begin{array}{ll}
g & (\text { the given asymptotically hyperbolic metric on } M), \\
\bar{g}=\rho^{2} g & (\text { on } \bar{M}), \\
\widetilde{g}=\Phi^{*} g & (\text { on an open subset of } \mathbb{H}), \\
\breve{g} & (\text { the hyperbolic metric on } \mathbb{H}) .
\end{array}$$

Arguing as in the proof of the preceding lemma, it suffices to show that each of the following operators has vanishing indicial map at (0, 0):
\begin{itemize}
\item[(a)] $u \mapsto \rho \widetilde{\nabla} u-\rho \breve{\nabla} u$,
\item[(b)] $u \mapsto u \otimes\left(\rho^{2} \widetilde{g}-\rho^{2} \breve{g}\right)$,
\item[(c)] $u \mapsto u \otimes\left(\rho^{-2} \widetilde{g}^{-1}-\rho^{-2} \breve{g}^{-1}\right)$,
\item[(d)] $u \mapsto u \otimes\left(\rho^{n+1} d V_{\widetilde{g}}-\rho^{n+1} d V_{\widetilde{g}}\right)$,
\item[(e)] $u \mapsto u \otimes\left(\rho^{4+k} \widetilde{\nabla^{k}} \widetilde{R m}-\rho^{4+k} \breve{\nabla}^{k} \widetilde{R m}\right)$.
\end{itemize}

If we let $E=\widetilde{\nabla}-\widetilde{\nabla}$ be the difference tensor between the two connections, a computation based on (3.10) yields
$$\rho E_{j k}^{i}=+\partial_{j} \rho\left(\bar{g}^{i l} \bar{g}_{k l}-\delta^{i l} \delta_{k l}\right)+O(\rho) .$$
Because $\bar{g}_{i j}=\delta_{i j}$ at $\widehat{p}$, it follows that $\rho \widetilde{\nabla}-\rho \breve{\nabla}$ is a zero-order operator that vanishes at (0, 0).

The next three operators, tensoring with $(\mathrm{b})-(\mathrm{d})$, are obviously zero-order operators vanishing at (0, 0), so their indicial maps have the same property. To complete the proof, we need to show that the indicial map of vanishes at (0, 0).

This is obvious from the argument in the preceding proof when $k>0$, because both $\rho^{4+k} \widetilde{\nabla^{k}} \widetilde{R m}$ and $\rho^{4+k} \breve{\nabla}^{k} \widetilde{R m}$ individually have vanishing indicial maps. On the other hand, the preceding proof showed that the restriction of $\rho^{4} \widetilde{R m}$ to $\partial M$ is equal to $\bar{K}$, which in turn is equal to $\rho^{4} \widetilde{R m}$ at ( 0,0 ). This completes the proof. \(\square\)

The next observation we need to make is that if $P$ is a formally self-adjoint geometric operator acting on a geometric tensor bundle of weight $r$, its set of characteristic exponents is symmetric about the line $\operatorname{Re} s=n / 2-r$. This will follow easily from the next lemma.

Proposition 4.4. Let $(M, g)$ be an asymptotically hyperbolic $(n+1)$-manifold of class $C^{l, \beta}$. Suppose that $m \leq l$ and $P: C^{\infty}(M ; E) \rightarrow C^{\infty}(M ; E)$ is an $m$ th order geometric operator acting on sections of a geometric tensor bundle $E$ of weight $r$, and let $P^{*}$ denote its formal adjoint. Then
$$I_{s}\left(P^{*}\right)=I_{n-2 r-\bar{s}}(P)^{*} .$$

Proof. Choose any point $\widehat{p} \in \partial M$, and let $(\theta, \rho)$ be background coordinates in a neighborhood $\Omega$ of $\widehat{p}$ in $\bar{M}$. Then we can write $P$ locally as
$$P u(\theta, \rho)=\sum_{\substack{0 \leq k \leq m \\ 1 \leq j_{i}, \ldots, j_{k} \leq n+1}} a^{j_{1} \ldots j_{k}}(\theta, \rho)\left(\rho \partial_{j_{1}}\right) \cdots\left(\rho \partial_{j_{k}}\right) u(\theta, \rho),$$
where each coefficient $a^{j_{1} \ldots j_{k}}(\theta, \rho)$ is a matrix-valued $C^{l-m+k, \beta}$ function (the coordinate representation of a bundle map from $E$ to itself). Suppose now that $\bar{u}$ is a section of $E$ that has a $C^{m}$ extension to $\bar{M}$. Then $\rho \partial_{i}\left(\rho^{s} \bar{u}\right)=O\left(\rho^{s+1}\right)$ if $i \neq n+1$, so $I_{s}(P)$ is given locally by
$$\begin{aligned}
I_{s}(P) \bar{u} & =\lim _{\rho \rightarrow 0} \sum_{\substack{0 \leq k \leq m \\
j_{i}=\cdots=j_{k}=n+1}} \rho^{-s} a^{j_{1} \ldots j_{k}}(\theta, \rho)\left(\rho \partial_{n+1}\right) \cdots\left(\rho \partial_{n+1}\right)\left(\rho^{s} \bar{u}(\theta, \rho)\right) \\
& =\sum_{\substack{0 \leq k \leq m \\
j_{i}=\cdots=j_{k}=n+1}} s^{k} a^{j_{1} \ldots j_{k}}(\theta, 0) \bar{u}(\theta, 0)
\end{aligned}$$

To compute $I_{s}\left(P^{*}\right)$, we first compute the formal adjoint of a monomial of the form $\rho \partial_{i}$ as follows. Let $\bar{g}=\rho^{2} g$, which is a $C^{l, \beta}$ metric on $\bar{M}$. The inner products on $E$ defined by $g$ and $\bar{g}$ are related by $\langle u, v\rangle_{g}=\rho^{2 r}\langle u, v\rangle_{\bar{g}}$, and the volume elements by $d V_{g}=\rho^{-n-1} d V_{\bar{g}}$. If $u, v$ are smooth sections of $E$ compactly supported in $\Omega \cap M$, then
$$\begin{aligned}
\int_{M}\left\langle u, \rho \partial_{i} v\right\rangle_{g} d V_{g} & =\int_{M} \rho^{2 r-n-1}\left\langle u, \rho \partial_{i} v\right\rangle_{\bar{g}}(\operatorname{det} \bar{g})^{1 / 2} d \theta^{1} \ldots d \theta^{n+1} \\
& =-\int_{M}\left\langle\partial_{i}\left(\rho^{2 r-n} u b(\bar{g})\right), v\right\rangle_{\bar{g}}(\operatorname{det} \bar{g})^{1 / 2} d \theta^{1} \ldots d \theta^{n+1} \\
& =-\int_{M}\left\langle\rho^{n+1-2 r} \partial_{i}\left(\rho^{2 r-n} u b(\bar{g})\right), v\right\rangle_{g} d V_{g}
\end{aligned}$$
where $b(\bar{g})$ is a constant-coefficient polynomial in the components of $\bar{g}, \bar{g}^{-1}$, and $(\operatorname{det} \bar{g})^{1 / 2}$. From this, it follows easily that
$$\left(\rho \partial_{i}\right)^{*}=-\rho \partial_{i}+(n-2 r) \delta_{i}^{n+1}-\rho b_{i},$$
where $b_{i}=\partial_{i} b(\bar{g})$ is $C^{l-1, \beta}$ up to $\partial M$. Therefore,
$$\begin{aligned}
P^{*} u(\theta, \rho)= & \sum_{\substack{0 \leq k \leq m \\
1 \leq j_{i}, \ldots, j_{k} \leq n+1}}\left(-\rho \partial_{j_{k}}+(n-2 r) \delta_{j_{k}}^{n+1}-\rho b_{j_{k}}\right) \cdots \\
& \left(-\rho \partial_{j_{1}}+(n-2 r) \delta_{j_{1}}^{n+1}-\rho b_{j_{1}}\right)\left(a^{j_{1} \ldots j_{k}}(\theta, \rho)^{*} u(\theta, \rho)\right),
\end{aligned}$$
and we conclude that
$$\begin{aligned}
I_{s}\left(P^{*}\right) \bar{u} & =\lim _{\rho \rightarrow 0} \sum_{\substack{0 \leq k \leq m \\
j_{i}=\cdots=j_{k}=n+1 \\
\left(-\rho \partial_{n+1}+(n-2 r)-\rho b_{n+1}\right)\left(a^{j_{1} \ldots j_{k}}(\theta, \rho)^{*}\left(\rho^{s} \bar{u}(\theta, \rho)\right)\right)}} \rho^{-s}\left(-\rho \partial_{n+1}+(n-2 r)-\rho b_{n+1}\right) \cdots \\
& =\sum_{\substack{0 \leq k \leq m \\
j_{i}=\cdots=j_{k}=n+1}}(n-2 r-s)^{k} a^{j_{1} \ldots j_{k}}(\theta, 0)^{*} \bar{u}(\theta, 0) \\
& =I_{n-2 r-\bar{s}}(P)^{*} \bar{u},
\end{aligned}$$
which was to be proved. \(\square\)

Corollary 4.5. If $P$ is a formally self-adjoint geometric operator of order $m \leq l$, then the set of characteristic exponents of $P$ is symmetric about the line $\operatorname{Re} s=n / 2-r$.

Proof. The preceding proposition shows that $I_{s}(P)=I_{s}\left(P^{*}\right)=I_{n-2 r-\bar{s}}(P)^{*}$. Thus if $s$ is a characteristic exponent of $P$, then $I_{n-2 r-\bar{s}}(P)^{*}$, and hence also $I_{n-2 r-\bar{s}}(P)$, is singular, which means that $s^{\prime}=n-2 r-\bar{s}$ is also a characteristic exponent. Since $\operatorname{Im} s=\operatorname{Im} s^{\prime}$ and $\frac{1}{2}\left(\operatorname{Re} s+\operatorname{Re} s^{\prime}\right)=n / 2-r$, the result follows. \(\square\)

This corollary shows that a geometric self-adjoint operator $P$ must have at least one characteristic exponent whose real part is greater than or equal to $n / 2-r$. We define the indicial radius of $P$ to be the smallest nonnegative number $R$ such that $P$ has a characteristic exponent whose real part is $n / 2-r+R$. (This is well-defined because the set of characteristic exponents is finite by Lemma 4.3.)

Next we investigate the mapping properties of geometric operators on our weighted spaces.

Lemma 4.6. Let $P: C^{\infty}(M ; E) \rightarrow C^{\infty}(M ; F)$ be a geometric operator of order $m$.
\begin{itemize}
\item[(a)] If $\delta \in \mathbb{R}, 1<p<\infty$, and $m \leq k \leq l$, then $P$ extends naturally to a bounded mapping
$$P: H_{\delta}^{k, p}(M ; E) \rightarrow H_{\delta}^{k-m, p}(M ; F) .$$
\item[(b)] If $\delta \in \mathbb{R}, 0 \leq \alpha<1$, and $m \leq k+\alpha \leq l+\beta$, then $P$ extends naturally to a bounded mapping
$$P: C_{\delta}^{k, \alpha}(M ; E) \rightarrow C_{\delta}^{k-m, \alpha}(M ; F) .$$
\end{itemize}

Proof. Let $\left\{\Phi_{i}\right\}$ be a uniformly locally finite covering of $M$ by Möbius charts as in Lemma 2.2. Let $\breve{E}$ be the bundle over hyperbolic space associated to the same $\mathrm{O}(n+1)$ or $S O(n+1)$ representation as $E$, and for each $i$, let $P_{i}: C^{\infty}\left(B_{2} ; E\right) \rightarrow$ $C^{\infty}\left(B_{2} ; E\right)$ be the operator defined by $P_{i}=\Phi_{i}^{*} \circ P \circ\left(\Phi_{i}^{-1}\right)^{*}$. Since the metric $g_{i}=\Phi_{i}^{*} g$ is uniformly $C^{l, \beta}$ equivalent to $\breve{g}$ in Möbius coordinates by Lemma (2.1), it follows that the coefficients of the $j$ th derivatives of $u$ that appear in $P_{i} u$ are
uniformly bounded in $C^{l-m+j, \beta}\left(B_{2}\right)$. Therefore, using Lemmas have
$$\begin{aligned}
\|P u\|_{k, p, \delta} & \leq C \sum_{i} \rho\left(p_{i}\right)^{-\delta}\left\|\Phi_{i}^{*} P u\right\|_{k, p ; B_{2}} \\
& =C \sum_{i} \rho\left(p_{i}\right)^{-\delta}\left\|P_{i}\left(\Phi_{i}^{*} u\right)\right\|_{k, p ; B_{2}} \\
& \leq C^{\prime} \sum_{i} \rho\left(p_{i}\right)^{-\delta}\left\|\Phi_{i}^{*} u\right\|_{k-m, p ; B_{2}} \\
& \leq C^{\prime \prime}\|u\|_{k-m, p, \delta}
\end{aligned}$$
with an analogous estimate in the Hölder case. \(\square\)

Recall from Chapter $\overline{\mathbf{p}}_{1}^{\prime}$ that when $p^{*}=p /(p-1), H_{-\delta}^{0, p^{*}}(M ; E)$ is naturally dual to $H_{\delta}^{0, p}(M ; E)$ under the standard $L^{2}$ pairing. The next lemma shows that $P$ is symmetric with respect to this pairing.

Lemma 4.7. Suppose $P$ satisfies the hypotheses of Theorem . If $1<p<\infty$, $p^{*}=p /(p-1)$, and $\delta \in \mathbb{R}$, then $(P u, v)=(u, P v)$ for all $u \in \dot{H}_{\delta}^{0, p}(M ; E), v \in$ $H_{-\delta}^{0, p^{*}}(M ; E)$.

Proof. This is true for $u, v \in C_{c}^{\infty}(M ; E)$ by the fact that $P$ is formally selfadjoint. The general result follows by density. \(\square\)

The following lemma is a standard application of rescaling techniques and classical interior elliptic regularity (cf. [29, Prop. 3.4], [1, Lemma 2.4], and 4.1.1]).

Lemma 4.8. Let $P: C^{\infty}(M ; E) \rightarrow C^{\infty}(M ; F)$ be a geometric elliptic operator of order $m$.
\begin{itemize}
\item[(a)] Suppose $\delta \in \mathbb{R}, 1<p<\infty$, and $m \leq k \leq l$. If $u \in H_{\delta}^{0, p}(M ; E)$ is such that $P u \in H_{\delta}^{k-m, p}(M ; F)$, then $u \in H_{\delta}^{k, p}(M ; E)$ and
$$\|u\|_{k, p, \delta} \leq C\left(\|P u\|_{k-m, p, \delta}+\|u\|_{0, p, \delta}\right) .$$
\item[(b)] Suppose $\delta \in \mathbb{R}, 0<\alpha<1$, and $m<k+\alpha \leq l+\beta$. If $u \in C_{\delta}^{0,0}(M ; E)$ is such that $P u \in C_{\delta}^{k-m, \alpha}(M ; F)$, then $u \in C_{\delta}^{k, \alpha}(M ; E)$ and
$$\|u\|_{k, \alpha, \delta} \leq C\left(\|P u\|_{k-m, \alpha, \delta}+\|u\|_{0,0, \delta}\right) .$$
\end{itemize}

Proof. Under the hypotheses of case $\left(a_{1}\right), u$ is locally in $H^{k, p}$ by interior elliptic regularity, so only the estimate (4.7) needs to be proved. Let $\left\{\Phi_{i}\right\}$ be a uniformly locally finite covering of $M$ by Möbius charts as in Lemma 2.2. and let $P_{i}=\Phi_{i}^{*} \circ P \circ\left(\Phi_{i}^{-1}\right)^{*}$ as in the proof of Lemma 4.6. Since the coefficients of the highest-order terms in $P_{i}$ are constant-coefficient polynomials in $g_{i}=\Phi_{i}^{*} g$ and $\left(\operatorname{det} g_{i}\right)^{-1 / 2}$, and $g_{i}$ is uniformly equivalent to the hyperbolic metric by Lemma 2.1, $P_{i}$ is uniformly elliptic on $B_{2}$. Moreover, since the coefficients of $P_{i}$ are uniformly bounded in $C^{k-m, \alpha}\left(B_{2}\right)$ by the same lemma, we have the following standard local elliptic estimate $[48,11]$ :
$$\|u\|_{k, p ; B_{1}} \leq C\left(\left\|P_{i} u\right\|_{k-m, p ; B_{2}}+\|u\|_{0, p ; B_{2}}\right),$$
where the constant $C$ depends on $P, k, p$, and $\delta$, but is independent of $u$ and $i$. Thus, using Lemma 3.5 again, we have
$$\begin{aligned}
\|u\|_{k, p, \delta} & \leq C \sum_{i} \rho\left(p_{i}\right)^{-\delta}\left\|\Phi_{i}^{*} u\right\|_{k, p ; B_{1}} \\
& \leq C^{\prime} \sum_{i} \rho\left(p_{i}\right)^{-\delta}\left(\left\|P_{i}\left(\Phi_{i}^{*} u\right)\right\|_{k-m, p ; B_{2}}+\left\|\Phi_{i}^{*} u\right\|_{0, p ; B_{2}}\right) \\
& =C^{\prime} \sum_{i} \rho\left(p_{i}\right)^{-\delta}\left\|\Phi_{i}^{*}(P u)\right\|_{k-m, p ; B_{2}}+C^{\prime} \sum_{i} \rho\left(p_{i}\right)^{-\delta}\left\|\Phi_{i}^{*} u\right\|_{0, p ; B_{2}} \\
& \leq C^{\prime \prime}\left(\|P u\|_{k-m, p, \delta}+\|u\|_{0, p, \delta}\right)
\end{aligned}$$

The argument for case ( ) is similar, using interior Hölder estimates [26]. \(\square\)

Lemma 4.9. If $P$ satisfies the hypotheses of Theorem , then $P$ is self-adjoint as an unbounded operator on $L^{2}(M ; E)$.

Proof. Because of the density of $C_{c}^{\infty}(M ; E)$ in $H^{m, 2}(M ; E), P$ is densely defined, and Lemma 4.8 shows that its domain is exactly $H^{m, 2}(M ; E)$. Clearly the domain of its Hilbert space adjoint contains $H^{m, 2}(M ; E)$. On the other hand, if $v$ is in the domain of the adjoint, then there exists $w \in L^{2}(M ; E)$ such that $(v, P u)=(w, u)$ for all $u \in L^{2}(M ; E)$. This means in particular that $P v=w$ as distributions, which by Lemma 4.8 implies that $v \in H^{m, 2}(M ; E)$. Thus the domain of the adjoint is equal to the domain of $P$. \(\square\)

Next we present some elementary preliminary results about Fredholm operators on these weighted spaces. Our first lemma reduces the problem of proving $L^{p}$ Fredholm theorems to estimates near the boundary. A partial differential operator $P$ acting on sections of a vector bundle over a connected manifold $M$ is said to have the weak unique continuation property if any solution to $P u=0$ that vanishes on an open set must vanish on all of $M$. It has been shown recently by G. Nakamura, G. Uhlmann, and J.-N. Wang 477 that every strongly elliptic operator has this property. We say an operator is semi-Fredholm if it has finite-dimensional kernel and closed range.

Lemma 4.10. Let $P: C^{\infty}(M ; E) \rightarrow C^{\infty}(M ; E)$ be a formally self-adjoint geometric elliptic operator of order $m \leq l$. Suppose $1<p<\infty$ and $\delta \in \mathbb{R}$. Then $P: H_{\delta}^{k, p}(M ; E) \rightarrow H_{\delta}^{k-m, p}(M ; E)$ is semi-Fredholm for $m \leq k \leq l$ if and only if there exist a compact subset $K \subset M$ and a constant $c>0$ such that the following estimate holds for all $u \in C_{c}^{\infty}(M \backslash K ; E)$ :
$$c\|u\|_{0, p, \delta} \leq\|P u\|_{0, p, \delta} .$$
If $P$ is semi-Fredholm and has the weak unique continuation property, then (4.9) holds for every compact subset $K \subset M$ with nonempty interior. If both ( 4.9 ) and
$$c\|u\|_{0, p^{*},-\delta} \leq\|P u\|_{0, p^{*},-\delta}$$
hold for $u \in C_{c}^{\infty}(M \backslash K ; E)$, where $p^{*}=p /(p-1)$, then $P$ is Fredholm.
Proof. The argument in the forward direction is fairly standard; see, for example, $[\overline{1}$, Thm. 1.10] and $[\overline{7}$, Prop. 2.6]. Let $U$ and $V$ be precompact open subsets of $M$ such that $K \subset U \subset \bar{U} \subset V$, and let $\psi \in C^{\infty}(M)$ be a smooth bump function that is equal to 1 on $K$ and supported in $\bar{U}$. It is easy to check that multiplication by $\psi$ is a bounded map from $H_{\delta}^{k, p}(M ; E)$ to itself for any $k, p, \delta$. On the compact
set $\bar{V}$, the $H_{\delta}^{k, p}$ norm is uniformly equivalent to the standard $H^{k, p}$ norm, and $P$ is uniformly elliptic.

First observe that $(4.9)$ extends to all $u \in H_{\delta}^{k, p}(M ; E)$ by continuity. For any $u \in H_{\delta}^{k, p}(M ; E)$, we can write $u=u_{\infty}+u_{0}$, where $u_{0}:=\psi u$ is supported in $\bar{U}$ and $u_{\infty}:=(1-\psi) u$ is supported in $M \backslash K$. We estimate as follows:
$$\|u\|_{k, p, \delta} \leq\left\|u_{\infty}\right\|_{k, p, \delta}+\left\|u_{0}\right\|_{k, p, \delta} .$$
For the first term, (4.7) gives
$$\begin{aligned}
\left\|u_{\infty}\right\|_{k, p, \delta} & \leq C_{1}\left(\left\|P u_{\infty}\right\|_{k-m, p, \delta}+\left\|u_{\infty}\right\|_{0, p, \delta}\right) \\
& \leq C_{2}\left(\left\|P u_{\infty}\right\|_{k-m, p, \delta}+\left\|P u_{\infty}\right\|_{0, p, \delta}\right) \\
& \leq C_{2}\left(\|(1-\psi) P u\|_{k-m, p, \delta}+\|[P, \psi] u\|_{k-m, p, \delta}\right) \\
& \leq C_{3}\left(\|P u\|_{k-m, p, \delta}+\|u\|_{k-1, p ; \bar{V}}\right)
\end{aligned}$$
where in the last line we have used the fact that $[P, \psi]$ is an operator of order $m-1$ supported on $\bar{V}$.

For the second term, standard interior elliptic estimates yield
$$\begin{aligned}
\left\|u_{0}\right\|_{k, p, \delta} & =\left\|u_{0}\right\|_{k, p, \delta ; \bar{U}} \\
& \leq C_{1}\left(\left\|P u_{0}\right\|_{k-m, p, \delta ; \bar{V}}+\left\|u_{0}\right\|_{0, p, \delta ; \bar{V}}\right) \\
& \leq C_{1}\left(\|\psi P u\|_{k-m, p, \delta}+\|[P, \psi] u\|_{k-m, p, \delta}+\|u\|_{0, p, \delta ; \bar{V}}\right) \\
& \leq C_{2}\left(\|P u\|_{k-m, p, \delta}+\|u\|_{k-1, p ; \bar{V}}\right)
\end{aligned}$$
Finally, standard interpolation inequalities on the compact set $\bar{V}$ (see $\mathbf{1 0} \underline{\mathbf{0}}_{\boldsymbol{p}}^{\mathbf{i}}$ Thm. 3.70]) allow us to replace $\|u\|_{k-1, p ; \bar{V}}$ by $C\|u\|_{0, p ; \bar{V}}+\varepsilon\|u\|_{k, p, \delta}$ with an arbitrarily small constant $\varepsilon$. Absorbing the $\varepsilon$ term on the left-hand side, we conclude
$$\|u\|_{k, p, \delta} \leq C\left(\|P u\|_{k-m, p, \delta}+\|u\|_{0, p ; \bar{V}}\right) .$$

Now suppose $\left\{u_{i}\right\}$ is a sequence in $\operatorname{Ker} P \cap H_{\delta}^{k, p}(M ; E)$. Normalize $u_{i}$ so that $\left\|u_{i}\right\|_{k, p, \delta}=1$. By the Rellich lemma on the compact set $\bar{V}$, some subsequence converges in $H^{0, p}(\bar{V} ; E)$. From ( $\overline{4} . \overline{1} \overline{1}$ ) we conclude that this subsequence is Cauchy and hence convergent in $H_{\delta}^{k, p}(M ; E)$, and therefore $\operatorname{Ker} P \cap H_{\delta}^{k, p}(M ; E)$ is finitedimensional.

Next we need to show that $P$ has closed range. Since $\operatorname{Ker} P$ is finitedimensional, it has a closed complementary subspace $Y \subset H_{\delta}^{k, p}(M ; E)$. I claim there is a constant $C$ such that
$$\|u\|_{k, p, \delta} \leq C\|P u\|_{k-m, p, \delta} \quad \text { for all } u \in Y .$$
If not, there is a sequence $\left\{u_{i}\right\} \subset Y$ with
$$\left\|u_{i}\right\|_{k, p, \delta}=1 \text { and }\left\|P u_{i}\right\|_{k-m, p, \delta} \rightarrow 0 .$$
By the Rellich lemma again, there exists a subsequence (still denoted by $\left\{u_{i}\right\}$ ) that converges in $H^{0, p}(\bar{V} ; E)$. Then ( $\overline{4} \overline{1} \overline{1}$ ) shows that the subsequence also converges in $H_{\delta}^{k, p}(M ; E)$. However, the limit $u$ then satisfies $\|u\|_{k, p, \delta}=1$ and $P u=0$ by continuity, and is therefore a nonzero element of $Y \cap \operatorname{Ker} P$, which is a contradiction.

Now if $u_{i} \in H_{\delta}^{k, p}(M ; E)$ with $P u_{i}=f_{i} \rightarrow f$ in $H_{\delta}^{k-m, p}(M ; F)$, we can assume without loss of generality that each $u_{i} \in Y$, and then ( 4.12 ) shows that $\left\{u_{i}\right\}$ converges in $H_{\delta}^{k, p}(M ; E)$, which shows that $P$ has closed range.

Conversely, suppose $P: H_{\delta}^{k, p}(M ; E) \rightarrow H_{\delta}^{k-m, p}(M ; E)$ is semi-Fredholm. Let $K \subset M$ be a compact subset chosen as follows: If $P$ has the unique continuation property, $K$ can be any compact subset of $M$ with nonempty interior; otherwise, let $K=M \backslash A_{\varepsilon}$, where $\varepsilon>0$ is chosen small enough that no element of the finite-dimensional space $\operatorname{Ker} P \cap H_{\delta}^{m, p}(M ; E)$ vanishes identically on $K$.

The key fact is that there exists $c>0$ such that
$$\|u-v\|_{0, p, \delta} \geq c\|u\|_{0, p, \delta}$$
whenever $u \in H_{\delta}^{0, p}(M ; E)$ is supported in $M \backslash K$ and $v \in \operatorname{Ker} P \cap H_{\delta}^{m, p}(M ; E)$. To see this, note that our choice of $K$ ensures that $\|\cdot\|_{0, p, \delta ; K}$ is a norm on $\operatorname{Ker} P \cap$ $H_{\delta}^{m, p}(M ; E)$. Since all norms on a finite-dimensional vector space are equivalent, there exists a constant $a$ such that
$$\|v\|_{0, p, \delta ; K} \geq a\|v\|_{0, p, \delta}$$
for all $v \in \operatorname{Ker} P \cap H_{\delta}^{m, p}(M ; E)$. Suppose now that $u$ is supported in $M \backslash K$, $\|u\|_{0, p, \delta}=1$, and $v \in \operatorname{Ker} P \cap H_{\delta}^{m, p}(M ; E)$. If $\|v\|_{0, p, \delta} \leq 1 /(1+a)$, then by the reverse triangle inequality
$$\|u-v\|_{0, p, \delta} \geq\|u\|_{0, p, \delta}-\|v\|_{0, p, \delta} \geq 1-\frac{1}{1+a}=\frac{a}{1+a} .$$
If on the other hand $\|v\|_{0, p, \delta} \geq 1 /(1+a)$, then because $u$ vanishes on $K$,
$$\begin{aligned}
\|u-v\|_{0, p, \delta} & \geq\|u-v\|_{0, p, \delta ; K}=\|v\|_{0, p, \delta ; K} \\
& \geq a\|v\|_{0, p, \delta} \geq \frac{a}{1+a}
\end{aligned}$$
Inequality (4.13) (with $c=a /(1+a)$ ) then follows for general $u$ by homogeneity.
As above, $\operatorname{Ker} P \cap H_{\delta}^{k, p}(M ; E)$ has a closed complementary subspace $Y$, and both $Y$ and $P\left(H_{\delta}^{k, p}(M ; E)\right) \subset H_{\delta}^{k-m, p}(M ; E)$ are Banach spaces with the induced norms. Then $\left.P\right|_{Y}: Y \rightarrow P\left(H_{\delta}^{k, p}(M ; E)\right)$ is bijective, and its inverse $\left(\left.P\right|_{Y}\right)^{-1}: P\left(H_{\delta}^{k, p}(M ; E)\right) \rightarrow Y$ is bounded by the open mapping theorem. This means there exists a constant $C>0$ such that

Let $u \in H_{\delta}^{k, p}(M ; E)$ be supported in $M \backslash \bar{K}$, and write $u=u_{0}+u_{Y}$, with $u_{0} \in \operatorname{Ker} P, u_{Y} \in Y$. It follows from ( 4.15 ) that
$$\left\|u_{Y}\right\|_{0, p, \delta}=\left\|u-u_{0}\right\|_{0, p, \delta} \geq c\|u\|_{0, p, \delta},$$
and therefore, by (4.12) with $k=m$,
$$\begin{aligned}
\|u\|_{0, p, \delta} & \leq c^{-1}\left\|u_{Y}\right\|_{0, p, \delta} \leq c^{-1}\left\|u_{Y}\right\|_{m, p, \delta} \\
& \leq c^{-1} C\left\|P u_{Y}\right\|_{0, p, \delta}=c^{-1} C\|P u\|_{0, p, \delta}
\end{aligned}$$
which is (4.9).
Finally, suppose that both (4.9) and (4.10) hold. To show that $P$ is actually Fredholm, all that remains to be shown is that the range of $P$ has finite codimension in $H_{\delta}^{k-m, p}(M ; F)$. Recall that $H_{-\delta}^{0, p^{*}}(M ; E)$ is dual to $H_{\delta}^{0, p}(M ; E)$ under the standard $L^{2}$ pairing. The argument above, using (4.10) instead of (4.9), shows that $P^{*}=P: H_{-\delta}^{k, p^{*}}(M ; E) \rightarrow H_{-\delta}^{k-m, p^{*}}(M ; E)$ has finite-dimensional kernel. Any $v \in H_{-\delta}^{0, p^{*}}(M ; E)$ that annihilates the range of $P$ in $H_{\delta}^{k-m, p}(M ; E)$ satisfies in particular $(v, P u)=0$ for all $u \in C_{c}^{\infty}(M ; E)$, so is a distribution solution to $P v=0$.

By Lemma $4.8, v \in H_{-\delta}^{k, p^{*}}(M ; E)$. Thus there is at most a finite-dimensional subspace of $H_{-\delta}^{0, p^{*}}(M ; E)$ that annihilates the range of $P$. Since $P\left(H_{\delta}^{k, p}(M ; E)\right)$ is closed in $H_{\delta}^{k-m, p}(M ; E)$, it has finite codimension. \(\square\)

\section*{CHAPTER 5}

\section*{Analysis on Hyperbolic Space}

In this chapter, we will analyze the behavior of geometric elliptic operators on hyperbolic space, which serves as a model for the more general case. Our goal is to show that if $P$ is an operator on hyperbolic space satisfying the hypotheses of Theorem , then $P$ is an isomorphism on appropriate weighted Sobolev and Hölder spaces. (In the next chapter, we will use the resulting inverse map to piece together a parametrix for the analogous operator acting on an arbitrary asymptotically hyperbolic manifold.)

For the purposes of this chapter, we will use the Poincaré ball model, identifying hyperbolic space with the unit ball $\mathbb{B} \subset \mathbb{R}^{n+1}$, with coordinates $\left(\xi^{1}, \ldots, \xi^{n+1}\right)$, and with the hyperbolic metric $\breve{g}=4(1-|\xi|)^{-2} \sum_{i}\left(d \xi^{i}\right)^{2}$. The hyperbolic distance function can be written in terms of the Euclidean norm and dot product as
$$d_{\breve{g}}(\xi, \eta)=\cosh ^{-1} \frac{\left(1+|\xi|^{2}\right)\left(1+|\eta|^{2}\right)-4 \xi \cdot \eta}{\left(1-|\xi|^{2}\right)\left(1-|\eta|^{2}\right)} .$$
It will be convenient to use
$$\rho(\xi)=\frac{1}{\cosh d_{\breve{g}}(\xi, 0)}=\frac{1-|\xi|^{2}}{1+|\xi|^{2}}$$
as a defining function for the ball, where $0=(0, \ldots, 0)$ denotes the origin in $\mathbb{B} \subset$ $\mathbb{R}^{n+1}$.

Throughout this chapter, $E$ will be a geometric tensor bundle of weight $r$ over $\mathbb{B}$, and $P: C^{\infty}(\mathbb{B} ; E) \rightarrow C^{\infty}(\mathbb{B} ; E)$ will be a formally self-adjoint geometric elliptic operator of order $m$. The fact that $P$ is geometric implies that it is isometry invariant: If $\varphi$ is any orientation-preserving hyperbolic isometry and $u$ is any section of $E$, then
$$\varphi^{*}(P u)=P\left(\varphi^{*} u\right) .$$
We will assume that $P$ satisfies (1.4). Then by Lemma $P: H^{m, 2}(\mathbb{B} ; E) \rightarrow$ $L^{2}(\mathbb{B} ; E)$ is Fredholm. The next lemma shows that this is equivalent to being an isomorphism.

Lemma 5.1. Suppose $P: C^{\infty}(\mathbb{B} ; E) \rightarrow C^{\infty}(\mathbb{B} ; E)$ is a geometric elliptic operator of order $m$ on $\mathbb{B}$. Then $P: H^{m, 2}(\mathbb{B} ; E) \rightarrow H^{0,2}(\mathbb{B} ; F)$ is Fredholm if and only if it is an isomorphism.

Proof. If $P$ is an isomorphism, then clearly it is Fredholm. Conversely, if $P$ is Fredholm, then by Lemma $P$ satisfies
$$\|u\| \leq C\|P u\|$$
whenever $u$ is supported in the complement of some compact set $K$. Suppose $u$ is any smooth, compactly supported section of $E$. There is a Möbius transformation
$\varphi$ such that $\varphi^{-1}(\operatorname{supp} u) \subset \mathbb{B} \backslash K$, so $\varphi^{*} u$ satisfies ( 2. $L^{2}$ norm are preserved by $\varphi, u$ itself satisfies the same estimate. Therefore, by continuity, (5.2) holds for all $u \in H^{m, 2}$, so $\operatorname{Ker} P$ is trivial. Since $P$ is self-adjoint as an unbounded operator on $L^{2}(M ; E)$, its index is zero, which means that it is also surjective. \(\square\)

Let $K$ be the Green kernel of $P$ : That is, $K$ is the Schwartz kernel of the operator $P^{-1}: L^{2}(\mathbb{B} ; E) \rightarrow H^{m, 2}(\mathbb{B} ; E)$. Invariantly, $K$ is interpreted as a distributional section of the bundle $\operatorname{Hom}\left(\pi_{2}^{*} E, \pi_{1}^{*} E\right)$ over $\mathbb{B} \times \mathbb{B}$, where $\pi_{j}$ is projection on the $j$ th factor. For all $f \in L^{2}(\mathbb{B} ; E)$,
$$P^{-1} f(\xi)=\int_{\mathbb{B}} K(\xi, \eta) f(\eta) d V_{\breve{g}}(\eta)$$
Equivalently, if we write $K_{\eta}(\xi)=K(\xi, \eta), K_{\eta}$ satisfies
$$P K_{\eta}(\xi)=\delta_{\eta}(\xi) \operatorname{Id}_{E_{\eta}}$$
in the distribution sense and $K_{\eta} \in L^{2}$ on the complement of a neighborhood of $\eta$. Somewhat more explicitly, for any $\eta \in \mathbb{B}$ and $u_{0} \in E_{\eta}, K_{\eta} u_{0}$ is a (distributional) section of $E$ satisfying $P\left(K_{\eta} u_{0}\right)=\delta_{\eta} u_{0}$. In particular, $K_{0}(\xi)=K(\xi, 0)$ can be viewed as a fundamental solution for $P$ on $\mathbb{B}$ with pole at 0.

By local elliptic regularity, $K$ is $C^{\infty}$ away from the diagonal $\{\xi=\eta\}$. Since $P$ is formally self-adjoint, it is easy to check that $K$ satisfies the symmetry condition $K(\eta, \xi)=K(\xi, \eta)^{*}$ for $\xi \neq \eta$, where $K(\xi, \eta)^{*}: E_{\xi} \rightarrow E_{\eta}$ is the (pointwise) adjoint of $K(\xi, \eta) \in \operatorname{Hom}\left(E_{\eta}, E_{\xi}\right)$.

We extend our defining function $\rho$ to a function $\rho: \overline{\mathbb{B}} \times \overline{\mathbb{B}} \rightarrow[0,1]$ of two variables (still denoted by the same symbol) by
$$\rho(\xi, \eta)=\frac{1}{\cosh d_{\breve{g}}(\xi, \eta)}=\frac{\left(1-|\xi|^{2}\right)\left(1-|\eta|^{2}\right)}{\left(1+|\xi|^{2}\right)\left(1+|\eta|^{2}\right)-4 \xi \cdot \eta} .$$
Observe that $\rho(\xi, 0)=\rho(\xi)$.
Our main technical tool in this chapter is the following decay estimate for $K$.
Proposition 5.2. Let $P: C^{\infty}(\mathbb{B} ; E) \rightarrow C^{\infty}(\mathbb{B} ; E)$ be a formally self-adjoint geometric elliptic operator of order $m$ satisfying (1.4). Then $P$ has positive indicial radius $R$, and for any $\varepsilon>0$ there is a constant $C$ such that
$$|K(\xi, \eta)| \leq C \rho(\xi, \eta)^{n / 2+R-\varepsilon}$$
whenever $d_{\breve{g}}(\xi, \eta) \geq 1$. (The norm here is the pointwise operator norm on $\operatorname{Hom}\left(E_{\eta}, E_{\xi}\right)$ with respect to the hyperbolic metric.)

Proof. The isometry invariance of $P$ implies that $K$ has the following equivariance property for any orientation-preserving hyperbolic isometry $\varphi$ :
$$K(\varphi(\xi), \varphi(\eta))=\left(\varphi^{*}\right)^{-1} \circ K(\xi, \eta) \circ \varphi^{*} .$$
Also, since $\rho$ is defined purely in terms of the hyperbolic distance function, it is clearly isometry invariant:
$$\rho(\varphi(\xi), \varphi(\eta))=\rho(\xi, \eta) .$$
Therefore, to prove ( 5.4 ), it suffices to show that
$$|K(\xi, 0)| \leq C \rho(\xi, 0)^{n / 2+R-\varepsilon}=C \rho(\xi)^{n / 2+R-\varepsilon} \text {. }$$

Note that $K_{0}(\xi)=K(\xi, 0)$ defines a smooth section of the bundle $\operatorname{Hom}\left(E_{0}, E\right)$ over $\mathbb{B} \backslash\{0\}$, whose fiber at $\xi$ is the vector space $\operatorname{Hom}\left(E_{0}, E_{\xi}\right)$.

The group of orientation-preserving hyperbolic isometries that fix 0 is exactly $\mathrm{SO}(n+1)$, acting linearly on the unit ball as isometries of both the hyperbolic and Euclidean metrics. Let $L \subset \mathbb{B}$ be the ray $L=\{(0, \ldots, 0, t): 0 \leq t<1\}$ along the $\xi^{n+1}$-axis. The subgroup of $\mathrm{SO}(n+1)$ that fixes $L$ pointwise is $\operatorname{SO}(n) \subset \operatorname{SO}(n+1)$, realized as the group of linear isometries acting in the first $n$ variables only. Observe that for each $\xi_{0} \in L, \mathrm{SO}(n)$ acts orthogonally (or unitarily if $E$ is a complex tensor bundle) on the fiber $E_{\xi_{0}}$ by pulling back.

Let $E_{0}=E_{0}^{(1)} \oplus \cdots \oplus E_{0}^{(k)}$ be an orthogonal decomposition of $E_{0}$ into irreducible $\operatorname{SO}(n)$-invariant subspaces. We extend this to a decomposition of the bundle $E$ over $\mathbb{B} \backslash\{0\}$ as follows. First, for each $\xi_{0} \in L$, let $E_{\xi_{0}}^{(i)}$ be the subspace of $E_{\xi_{0}}$ obtained by parallel translating $E_{0}^{(i)}$ along $L$ with respect to the Euclidean metric $\bar{g}$; since $\operatorname{SO}(n)$ acts as Euclidean isometries, it follows that
$$E_{\xi_{0}}=E_{\xi_{0}}^{(1)} \oplus \cdots \oplus E_{\xi_{0}}^{(k)}$$
is an orthogonal irreducible $\operatorname{SO}(n)$-decomposition of $E_{\xi_{0}}$. Then for an arbitrary point $\xi \in \mathbb{B} \backslash\{0\}$, let $E_{\xi}^{(i)}=\left(\varphi^{*}\right)^{-1} E_{\xi_{0}}^{(i)}$, where $\xi_{0}$ is the unique point of $L$ such that $\left|\xi_{0}\right|=|\xi|$, and $\varphi \in \mathrm{SO}(n+1)$ satisfies $\varphi\left(\xi_{0}\right)=\xi$. Since $E_{\xi_{0}}^{(i)}$ is invariant under $\mathrm{SO}(n)$, $E_{\xi}^{(i)}$ does not depend on the choice of $\varphi$. Since $\varphi$ can be chosen locally to depend smoothly on $\xi$ (by means of a smooth local section of the submersion $\mathrm{SO}(n+1) \rightarrow$ $\mathrm{SO}(n+1) / \mathrm{SO}(n)=\mathbb{S}^{n}$ ), this results in $k$ smooth subbundles $E^{(1)}, \ldots, E^{(k)}$ of $E$ over $\mathbb{B} \backslash\{0\}$.

For each pair of indices $i, j=1, \ldots, k$, we choose an $\operatorname{SO}(n)$-equivariant linear map $k_{0}^{(i, j)}: E_{0} \rightarrow E_{0}$ as follows: If $E_{0}^{(i)}$ and $E_{0}^{(j)}$ are isomorphic as representations of $\mathrm{SO}(n)$, let $k_{0}^{(i, j)}$ be an $\mathrm{SO}(n)$-equivariant Euclidean isometry from $E_{0}^{(i)}$ to $E_{0}^{(j)}$, extended to be zero on $E_{0}^{(l)}$ for $l \neq i$; and otherwise let $k_{0}^{(i, j)}$ be the zero map. By Schur's lemma, the nonzero maps $k_{0}^{(i, j)}$ form a basis for the space of $\operatorname{SO}(n)$-equivariant endomorphisms of $E_{0}$. Let us renumber these nonzero maps as $k_{0}^{1}, \ldots, k_{0}^{N}$.

Next we extend each map $k_{0}^{j}$ to a section $k^{j}$ of $\operatorname{Hom}\left(E_{0}, E\right)$ over $\mathbb{B} \backslash\{0\}$ in the same way as we extended the spaces $E_{0}^{(i)}$ : First, for each point $\xi_{0} \in L$, define $k_{\xi_{0}}^{j}: E_{0} \rightarrow E_{\xi_{0}}$ to be $k_{0}^{j}$ followed by $\bar{g}$-parallel translation along $L$ from 0 to $\xi_{0}$; and then for arbitrary $\xi \in \mathbb{B} \backslash\{0\}$, define $k_{\xi}^{j}=\left(\varphi^{*}\right)^{-1} \circ k_{\xi_{0}}^{j} \circ \varphi^{*}$, where $\xi_{0} \in L$ and $\varphi \in \operatorname{SO}(n+1)$ satisfies $\varphi\left(\xi_{0}\right)=\xi$.

I claim that there are smooth functions $f_{1}, \ldots, f_{N}:(0,1) \rightarrow \mathbb{C}$ such that
$$K_{0}(\xi)=\sum_{j} f_{j}(\rho(\xi)) k_{\xi}^{j}$$
for all $\xi \in \mathbb{B} \backslash\{0\}$. To see this, first note that for any point $\xi_{0} \in L$, the equivariance property (5.5) implies that $K_{0}\left(\xi_{0}\right)$ is an $\operatorname{SO}(n)$-equivariant linear map from $E_{0}$ to $E_{\xi_{0}}$, and therefore by Schur's lemma it can be written as a linear combination of the maps $k_{\xi_{0}}^{j}$ :
$$K_{0}\left(\xi_{0}\right)=\sum_{j} c_{j}\left(\xi_{0}\right) k_{\xi_{0}}^{j} .$$

For any other point $\xi \in \mathbb{B} \backslash\{0\}$, let $\xi_{0}$ be the point of $L$ such that $\left|\xi_{0}\right|=|\xi|$, and let $\varphi \in \mathrm{SO}(n+1)$ satisfy $\varphi\left(\xi_{0}\right)=\xi$. Then ( 5.51 ) yields
$$\begin{aligned}
K_{0}(\xi) & =K\left(\varphi\left(\xi_{0}\right), \varphi(0)\right) \\
& =\left(\varphi^{*}\right)^{-1} \circ K\left(\xi_{0}, 0\right) \circ \varphi^{*} \\
& =\sum_{j} c_{j}\left(\xi_{0}\right)\left(\varphi^{*}\right)^{-1} \circ k_{\xi_{0}}^{j} \circ \varphi^{*} \\
& =\sum_{j} c_{j}\left(\xi_{0}\right) k_{\xi}^{j} .
\end{aligned}$$
Since $\rho: L \backslash\{0\} \rightarrow(0,1)$ is a diffeomorphism, there are functions $f_{j}:(0,1) \rightarrow \mathbb{C}$ such that $f_{j}(\rho(\xi))=f_{j}\left(\rho\left(\xi_{0}\right)\right)=c_{j}\left(\xi_{0}\right)$ whenever $|\xi|=\left|\xi_{0}\right|$, and then (5.7) is equivalent to $\left(5^{2} .6_{1}\right)$. The smoothness of $K_{0}$ implies that the functions $f_{j}$ are smooth.

Now the equation $P K_{0}=0$ reduces to an analytic system of ordinary differential equations for the functions $f_{j}$, and the fact that $P$ is uniformly degenerate implies that this system has a regular singular point at $\rho=0$. Because the sections $k^{j}$ of $\operatorname{Hom}\left(E_{0}, E\right)$ extend smoothly to $\overline{\mathbb{B}} \backslash\{0\}$, our definition of the indicial map of $P$ guarantees that the characteristic exponents of this system of ODEs are precisely the characteristic exponents of the operator $P$. Therefore, by the standard theory of ODEs with regular singular points, each coefficient function $f_{j}$ satisfies
$$\left|f_{j}(t)\right| \sim C_{j} t^{s_{j}}|\log t|^{k_{j}} \text { as } t \rightarrow 0$$
for some characteristic exponent $s_{j}$ and some nonnegative integer $k_{j}$.
If $u_{0}$ is any tensor in one of the summands $E_{0}^{(i)}$, then the images $k_{\xi}^{j}\left(u_{0}\right)$ lie in different summands of $E_{\xi}$ and are therefore orthogonal, so
$$\left|K_{0}(\xi) u_{0}\right| \frac{2}{g}=\sum_{j}\left|f_{j}(\rho(\xi))\right|^{2}\left|k_{\xi}^{j} u_{0}\right| \frac{2}{g},$$
where $\bar{g}$ is the Euclidean metric on $\mathbb{B}$. Since $k_{\xi}^{j}$ is a Euclidean isometry onto its image, $\left|k_{\xi}^{j} u_{0}\right|_{\bar{g}}$ is independent of $\xi$. Therefore, if $k_{\xi}^{j} u_{0} \neq 0$, then on $\mathbb{B} \backslash\{0\}$ we have
$$\left|K_{0}(\xi) u_{0}\right| \bar{g} \geq C\left|f_{j}(\rho(\xi))\right| \geq C \rho(\xi)^{\operatorname{Re} s_{j}}|\log \rho(\xi)|^{k_{j}}$$
for some positive constant $C$. Because $K_{0}(\xi) u_{0}$ is in $L^{2}$ away from 0, by Lemma 3.2 we must have $\operatorname{Re} s_{j}>n / 2-r$ for each such $j$. Since for each $j$ there is some $u_{0}$ such that $k_{\xi}^{j} u_{0} \neq 0$, the same inequality holds for every $j$. By definition of the indicial radius $R$, this implies that in fact $R>0$ and $\operatorname{Re} s_{j} \geq n / 2-r+R$. Using (5.8), we conclude that for any $\varepsilon>0$ there is a constant $C$ such that
$$\left|f_{j}(t)\right| \leq C t^{n / 2-r+R-\varepsilon} \text { for } t \text { away from } 1 \text {. }$$
This in turn implies
$$\begin{aligned}
\left|K_{0}(\xi) u_{0}\right|_{\breve{g}} & \leq C \rho(\xi)^{r}\left|K_{0}(\xi) u_{0}\right|_{\bar{g}} \\
& \leq C^{\prime} \rho(\xi)^{r} \rho(\xi)^{n / 2-r+R-\varepsilon}\left|u_{0}\right|_{\bar{g}} \\
& =C^{\prime \prime} \rho(\xi)^{n / 2+R-\varepsilon}\left|u_{0}\right|_{\breve{g}}
\end{aligned}$$
whenever $d(\xi, 0) \geq 1$, which was to be proved. \(\square\)

The next two lemmas give some estimates that will be needed to use our decay estimate for proving mapping properties of $P^{-1}$.

Lemma 5.3. For any real numbers $p, q, r$ such that $p+1>0$ and $r>q+1>0$, there exists a constant $C$ depending only on $p, q, r$ such that the following estimate holds for all $u \in[0,1)$ :
$$\int_{0}^{1} \frac{t^{p}(1-t)^{q}}{(1-u t)^{r}} d t \leq C(1-u)^{q+1-r}$$

Proof. We use the following standard integral representation for hypergeometric functions ${ }^{\mathbf{2}-\mathbf{7}}$, p. 59]:
$$F(\alpha, \beta, \gamma ; z)=\frac{\Gamma(\gamma)}{\Gamma(\beta) \Gamma(\gamma-\beta)} \int_{0}^{1} \frac{t^{\beta-1}(1-t)^{\gamma-\beta-1}}{(1-t z)^{\alpha}} d t$$
which is valid if $\operatorname{Re} \gamma>\operatorname{Re} \beta>0$ and $|z|<1$. The hypergeometric function $F(\alpha, \beta, \gamma ; z)$ is analytic for $|z|<1$ and satisfies a second-order ODE that has a regular singular point at $z=1$ with characteristic exponents 0 and $\gamma-\alpha-\beta\left[\mathbf{1 7}{ }_{\mathbf{p}}^{\mathbf{\prime}}\right.$ p. 246]. As long as $\gamma-\alpha-\beta<0$, therefore, it satisfies
$$|F(\alpha, \beta, \gamma ; u)| \leq C(1-u)^{\gamma-\alpha-\beta} \quad \text { if } 0 \leq u<1 .$$
Applying this with $\alpha=r, \beta=p+1$, and $\gamma=p+q+2$ proves the lemma. \(\square\)

Lemma 5.4. Suppose $a$ and $b$ are real numbers such that $a+b>n$ and $a>b$. There exists a constant $C$ depending only on $n, a, b$ such that the following estimate holds for all $\xi, \zeta \in \mathbb{B}$ :
$$\int_{\mathbb{B}} \rho(\xi, \eta)^{a} \rho(\eta, \zeta)^{b} d V_{\breve{g}}(\eta) \leq C \rho(\xi, \zeta)^{b}$$

Proof. By an isometry, we can arrange that $\zeta=0$ and $\xi=(0, \ldots, 0, r)$ is on the positive $\xi^{n+1}$-axis. Substituting $\zeta=0$ into the integral, we must estimate
$$I:=\int_{\mathbb{B}}\left(\frac{\left(1-|\xi|^{2}\right)\left(1-|\eta|^{2}\right)}{\left(1+|\xi|^{2}\right)\left(1+|\eta|^{2}\right)-4 \xi \cdot \eta}\right)^{a}\left(\frac{1-|\eta|^{2}}{1+|\eta|^{2}}\right)^{b} d V_{\breve{g}}(\eta) .$$

Parametrize the ball by the map $\Phi:(0,1) \times(0, \pi) \times \mathbb{S}^{n-1} \rightarrow \mathbb{B}$ given by
$$\Phi(s, \theta, \omega)=\left(s \omega^{1} \sin \theta, \ldots, s \omega^{n} \sin \theta, s \cos \theta\right),$$
so that $s$ is the Euclidean distance from 0 and $\theta$ is the angle from the positive $\xi^{n+1}$-axis. In these coordinates, the hyperbolic metric is
$$\breve{g}=\frac{4}{\left(1-s^{2}\right)^{2}}\left(d s^{2}+s^{2} d \theta^{2}+s^{2} \sin ^{2} \theta \stackrel{\circ}{g}\right),$$
where $\stackrel{\circ}{g}$ represents the standard metric on $\mathbb{S}^{n-1}$. The hyperbolic volume element is therefore
$$d V_{\breve{g}}=\frac{2^{n+1} s^{n} \sin ^{n-1} \theta}{\left(1-s^{2}\right)^{n+1}} d s d \theta d V_{\mathrm{g}}$$
where $d V_{\mathrm{g}}$ is the volume element on $\mathbb{S}^{n-1}$.
In these coordinates, we have $|\xi|=r,|\eta|=s$ and $\xi \cdot \eta=r s \cos \theta$. The integrand in ( 5.9 ) is constant on each sphere $\mathbb{S}^{n-1}$, so we can immediately integrate over $\mathbb{S}^{n-1}$ and write $I$ as a constant multiple of
$$\int_{0}^{1} \int_{0}^{\pi}\left(\frac{\left(1-r^{2}\right)\left(1-s^{2}\right)}{\left(1+r^{2}\right)\left(1+s^{2}\right)-4 r s \cos \theta}\right)^{a}\left(\frac{1-s^{2}}{1+s^{2}}\right)^{b} \frac{s^{n} \sin ^{n-1} \theta}{\left(1-s^{2}\right)^{n+1}} d \theta d s$$

Since we are only interested in estimates up to a constant multiple, we will write $f \sim g$ to mean that $f / g$ is bounded above and below by positive constants depending only on $a, b$, and $n$. Thus, for example, $1-s^{2}=(1-s)(1+s) \sim 1-s$, $1-r^{2} \sim 1-r, 1+r^{2} \sim 1+s^{2} \sim 1$, and
$$I \sim \int_{0}^{1} \int_{0}^{\pi}\left(\frac{(1-r)(1-s)}{\left(1+r^{2}\right)\left(1+s^{2}\right)-4 r s \cos \theta}\right)^{a}(1-s)^{b} \frac{s^{n} \sin ^{n-1} \theta}{(1-s)^{n+1}} d \theta d s$$

The $\theta$ integral can be simplified by the substitution $\cos \theta=2 t-1$ to obtain
$$\begin{aligned}
& \int_{0}^{\pi} \frac{\sin ^{n-1} \theta}{\left(\left(1+r^{2}\right)\left(1+s^{2}\right)-4 r s \cos \theta\right)^{a}} d \theta \\
& \quad=2^{n-1} B(r, s)^{a} \int_{0}^{1} \frac{t^{n / 2-1}(1-t)^{n / 2-1}}{(1-8 B(r, s) r s t)^{a}} d t
\end{aligned}$$
where
$$B(r, s)=\frac{1}{\left(1+r^{2}\right)\left(1+s^{2}\right)+4 r s} \sim 1 .$$
Because our hypothesis guarantees that $n-a<b \leq a$ and therefore $a>n / 2$, Lemma 5.3 shows that the right-hand integral in $(5.11)$ is bounded by a constant multiple of $(1-8 B(r, s) r s)^{n / 2-a}$. Substituting this into $(\overline{1} . \overline{1})$ yields
$$I \leq C(1-r)^{a} \int_{0}^{1} \frac{s^{n}(1-s)^{a+b-n-1}}{(1-8 B(r, s) r s)^{a-n / 2}} d s$$

A computation shows that
$$1-8 B(r, s) r s=\frac{(1-r s)^{2}+(r-s)^{2}}{(1+r s)^{2}+(r+s)^{2}} \sim(1-r s)^{2}+(r-s)^{2} \geq(1-r s)^{2} .$$
Inserting this into (5.12), we conclude that
$$I \leq C(1-r)^{a} \int_{0}^{1} \frac{s^{n}(1-s)^{a+b-n-1}}{(1-r s)^{2 a-n}} d s$$
Lemma 5 then shows that this is bounded by a multiple of $(1-r)^{b} \sim \rho(\xi, \zeta)^{b}$. \(\square\)

The following estimate is the key to proving sharp mapping properties of $P^{-1}$.
Lemma 5.5. Let $P$ satisfy the hypotheses of Proposition 5.2. Then for any real number $b$ satisfying $n / 2-R<b<n / 2+R$, there exists a constant $C$ such that
$$\begin{aligned}
& \int_{\mathbb{B}}|K(\xi, \eta)| \rho(\eta)^{b} d V_{\breve{g}}(\eta) \leq C \rho(\xi)^{b} \\
& \int_{\mathbb{B}}|K(\xi, \eta)| \rho(\xi)^{b} d V_{\breve{g}}(\xi) \leq C \rho(\eta)^{b}
\end{aligned}$$

Proof. Since $|K(\xi, \eta)|=\left|K(\eta, \xi)^{*}\right|=|K(\eta, \xi)|$ by self-adjointness, the two inequalities are equivalent, so it suffices to prove the second one. We will write
$$\begin{aligned}
& \int_{\mathbb{B}}|K(\xi, \eta)| \rho(\xi)^{b} d V_{\breve{g}}(\xi) \\
& \quad=\int_{d_{\breve{g}}(\xi, \eta) \leq 1}|K(\xi, \eta)| \rho(\xi)^{b} d V_{\breve{g}}(\xi)+\int_{d_{\breve{g}}(\xi, \eta) \geq 1}|K(\xi, \eta)| \rho(\xi)^{b} d V_{\breve{g}}(\xi)
\end{aligned}$$
and estimate each term separately.

For the first term, we observe that $K$ is uniformly locally integrable near $\xi=\eta$ : Since $K_{0}(\xi)=K(\xi, 0)$ satisfies $P K_{0}=\delta_{0} \mathrm{Id}_{E_{0}}$, and the Dirac delta function is in the Sobolev space $H^{-1, q}$ for $1<q<1+1 / n$ (defined as the dual space to $H^{1, q^{*}}$, $\left.q^{*}=q /(q-1)\right)$, local elliptic regularity implies that $K_{0} \in L_{\text {loc }}^{q} \subset L_{\text {loc }}^{1}$. Therefore, if $\eta \in \mathbb{B}$ is arbitrary and $\varphi$ is any Möbius transformation sending $\eta$ to 0 , the change of variables $\xi^{\prime}=\varphi(\xi)$ yields
$$\int_{d_{\breve{g}}(\xi, \eta) \leq 1}|K(\xi, \eta)| d V_{\breve{g}}(\xi)=\int_{d_{\breve{g}}\left(\xi^{\prime}, 0\right) \leq 1}\left|K\left(\xi^{\prime}, 0\right)\right| d V_{\breve{g}}\left(\xi^{\prime}\right) \leq C .$$

Using the triangle inequality together with the elementary fact that $\cosh (A+$ $B) \leq 2 \cosh A \cosh B$ for $A, B \geq 0$, we estimate
$$\cosh d_{\breve{g}}(\xi, 0) \leq \cosh \left(d_{\breve{g}}(\xi, \eta)+d_{\breve{g}}(\eta, 0)\right) \leq 2 \cosh d_{\breve{g}}(\xi, \eta) \cosh d_{\breve{g}}(\eta, 0) .$$
It follows that $\rho(\eta) \leq 2 \rho(\xi)$ on the set where $d_{\breve{g}}(\xi, \eta) \leq 1$. By symmetry, the same inequality holds with $\xi$ and $\eta$ reversed. Thus
$$\begin{aligned}
\int_{d_{\breve{g}}(\xi, \eta) \leq 1} & |K(\xi, \eta)| \rho(\xi)^{b} d V_{\breve{g}}(\xi) \\
& \leq\left(\sup _{d_{\breve{g}}(\xi, \eta) \leq 1} \rho(\xi)^{b}\right) \int_{d_{\breve{g}}(\xi, \eta) \leq 1}|K(\xi, \eta)| d V_{\breve{g}}(\xi) \\
& \leq C \rho(\eta)^{b}
\end{aligned}$$

For the second term, choose $\varepsilon>0$ small enough that
$$\frac{n}{2}-R+\varepsilon<b<\frac{n}{2}+R-\varepsilon .$$
Then with $a=n / 2+R-\varepsilon$, we have $a+b>n$ and $a>b$, so we can use Proposition 5.21 and Lemma 5.4 to conclude
$$\begin{aligned}
\int_{d_{\breve{g}}(\xi, \eta) \geq 1}|K(\xi, \eta)| \rho(\xi)^{b} d V_{\breve{g}}(\xi) & \leq \int_{d_{\breve{g}}(\xi, \eta) \geq 1} \rho(\xi, \eta)^{a} \rho(\xi)^{b} d V_{\breve{g}}(\xi) \\
& \leq C \rho(\xi)^{b}
\end{aligned}$$ \(\square\)

Proposition 5.6. If $1<p<\infty, k \geq m$, and $|\delta+n / p-n / 2|<R$, then there exists a constant $C$ such that
$$\|u\|_{k, p, \delta} \leq C\|P u\|_{k-m, p, \delta}$$
for all $u \in H_{\delta}^{k, p}(\mathbb{B} ; E)$.
Proof. Using Lemma it suffices to prove that
$$\|u\|_{0, p, \delta} \leq C\|P u\|_{0, p, \delta}$$
for all $u \in H_{\delta}^{k, p}(\mathbb{B} ; E)$. Because $C_{c}^{\infty}(\mathbb{B} ; E)$ is dense in $H_{\delta}^{k, p}(\mathbb{B} ; E)$, it suffices to prove this inequality for $u \in C_{c}^{\infty}(\mathbb{B} ; E)$. Since $u=P^{-1}(P u)$ in that case, it suffices to prove the estimate
$$\left\|P^{-1} f\right\|_{0, p, \delta} \leq C\|f\|_{0, p, \delta} \text { for all } f \in C_{c}^{\infty}(\mathbb{B} ; E) .$$

Put
$$\begin{aligned}
p^{*} & =\frac{p}{p-1} \\
a & =\frac{1}{p^{*}}\left(\delta+\frac{n}{p}\right)
\end{aligned}$$
so that
$$\begin{aligned}
& \frac{n}{2}-R<a p^{*}<\frac{n}{2}+R \\
& \frac{n}{2}-R<a p-\delta p<\frac{n}{2}+R
\end{aligned}$$

By Hölder's inequality and Lemma 5.5', we estimate
$$\begin{aligned}
\left|P^{-1} f(\xi)\right|_{\breve{g}} \leq & \int_{\mathbb{B}}|K(\xi, \eta)||f(\eta)|_{\breve{g}} d V_{\breve{g}}(\eta) \\
= & \int_{\mathbb{B}}\left(|K(\xi, \eta)|^{1 / p} \rho(\eta)^{-a}|f(\eta)|_{\breve{g}}\right)\left(|K(\xi, \eta)|^{1 / p^{*}} \rho(\eta)^{a}\right) d V_{\breve{g}}(\eta) \\
\leq & \left(\int_{\mathbb{B}}|K(\xi, \eta)| \rho(\eta)^{-a p}|f(\eta)|_{\breve{g}}^{p} d V_{\breve{g}}(\eta)\right)^{1 / p} \times \\
& \quad\left(\int_{\mathbb{B}}|K(\xi, \eta)| \rho(\eta)^{a p^{*}} d V_{\breve{g}}(\eta)\right)^{1 / p^{*}} \\
\leq & C \rho(\xi)^{a}\left(\int_{\mathbb{B}}|K(\xi, \eta)| \rho(\eta)^{-a p}|f(\eta)|_{\breve{g}}^{p} d V_{\breve{g}}(\eta)\right)^{1 / p}
\end{aligned}$$
Therefore,
$$\begin{aligned}
\left\|P^{-1} f\right\|_{0, p, \delta}^{p} & =\int_{\mathbb{B}} \rho(\xi)^{-\delta p}\left|P^{-1} f(\xi)\right|_{\breve{g}}^{p} d V_{\breve{g}}(\xi) \\
& \leq C^{p} \int_{\mathbb{B}} \int_{\mathbb{B}} \rho(\xi)^{a p-\delta p}|K(\xi, \eta)| \rho(\eta)^{-a p}|f(\eta)|_{\breve{g}}^{p} d V_{\breve{g}}(\eta) d V_{\breve{g}}(\xi)
\end{aligned}$$
By Lemma 5.5 again, we can evaluate the $\xi$ integral first to obtain
$$\begin{aligned}
\left\|P^{-1} f\right\|_{0, p, \delta}^{p} & \leq C^{\prime} \int_{\mathbb{B}} \rho(\eta)^{a p-\delta p} \rho(\eta)^{-a p}|f(\eta)|_{\breve{g}}^{p} d V_{\breve{g}}(\eta) \\
& =C^{\prime}\|f\|_{0, p, \delta}^{p} .
\end{aligned}$$ \(\square\)

Theorem 5.7. Let $P: C^{\infty}(\mathbb{B} ; E) \rightarrow C^{\infty}(\mathbb{B} ; \underline{E})$ be a formally self-adjoint geometric elliptic operator of order $m$ satisfying (1.4). If $k \geq m, 1<p<\infty$, and $|\delta+n / p-n / 2|<R$, then the natural extension $P: H_{\delta}^{k, p}(\mathbb{B} ; E) \rightarrow H_{\delta}^{k-m, p}(\mathbb{B} ; E)$ is an isomorphism.

Proof. Injectivity is an immediate consequence of (5.15). To prove surjectivity, let $f \in H_{\delta}^{k-m, p}(\mathbb{B} ; E)$ be arbitrary, and let $f_{i} \in C_{c}^{\infty}(\mathbb{B} ; E)$ be a sequence such that $f_{i} \rightarrow f$ in $H_{\delta}^{k-m, p}(\mathbb{B} ; E)$. Set $u_{i}=P^{-1} f_{i} \in H^{m, 2}(\mathbb{B} ; E)$, so that $P u_{i}=f_{i}$. Then each $u_{i}$ is in $H_{\delta}^{0, p}(\mathbb{B} ; E)$ by $(15.16)$, and in $H_{\delta}^{k, p}(\mathbb{B} ; E)$ by Lemma 4.8, and $(5.15)$ shows that $\left\{u_{i}\right\}$ is Cauchy in $H_{\delta}^{k, p}(\mathbb{B} ; E)$. It follows that $u=\lim u_{i} \in H_{\delta}^{k, p}(\mathbb{B} ; E)$ satisfies $P u=f$ as desired, so $P$ is surjective. The continuity of the inverse map then follows from (5.15). \(\square\)

Now we turn our attention to the Hölder case. First we prove an estimate analogous to (5.16).

Proposition 5.8. If $|\delta-n / 2|<R$, there exists a constant $C$ such that
$$\left\|P^{-1} f\right\|_{0,0, \delta} \leq C\|f\|_{0,0, \delta}$$
for all $f \in C_{\delta}^{0,0}(\mathbb{B} ; E)$.
Proof. By Lemma 5.5,
$$\begin{aligned}
\left|P^{-1} f(\xi)\right|_{\breve{g}} & \leq \int_{\mathbb{B}}|K(\xi, \eta)||f(\eta)|_{\breve{g}} d V_{\breve{g}}(\eta) \\
& \leq C \int_{\mathbb{B}}|K(\xi, \eta)| \rho(\eta)^{\delta}\|f\|_{0,0, \delta} d V_{\breve{g}}(\eta) \\
& \leq C^{\prime} \rho(\xi)^{\delta}\|f\|_{0,0, \delta}
\end{aligned}$$
which implies
$$\left\|P^{-1} f\right\|_{0,0, \delta}=\sup _{\xi \in \mathbb{B}}\left(\rho(\xi)^{-\delta}\left|P^{-1} f(\xi)\right|_{\breve{g}}\right) \leq C^{\prime}\|f\|_{0,0, \delta} .$$ \(\square\)

Theorem 5.9. Let $P: C^{\infty}(\mathbb{B} ; E) \rightarrow C^{\infty}(\mathbb{B} ; \underline{E})$ be a formally self-adjoint geometric elliptic operator of order $m$ satisfying (1.4). If $0<\alpha<1, k \geq m$, and $|\delta-n / 2|<R$, then the natural extension $P: \bar{C}_{\delta}^{k, \alpha}(\mathbb{B} ; E) \rightarrow C_{\delta}^{k-m, \alpha}(\mathbb{B} ; E)$ is an isomorphism.

Proof. To prove surjectivity, let $f \in C_{\delta}^{k-m, \alpha}(\mathbb{B} ; E)$ be arbitrary and set $u=$ $P^{-1} f$, so that $u \in C_{\delta}^{0,0}(\mathbb{B} ; E)$ by Proposition 5.8. An easy computation shows that $P u=f$ in the distribution sense, so $u \in C_{\delta}^{k, \alpha}(\mathbb{B} ; E)$ by Lemma

To prove injectivity, choose $\delta^{\prime}$ close to $\delta$ and $p$ large such that $\delta>\delta^{\prime}+n / p$ and $\left|\delta^{\prime}+n / p-n / 2\right|<R$. Then $C_{\delta}^{k, \alpha}(\mathbb{B} ; E) \subset H_{\delta^{\prime}}^{k, p}(\mathbb{B} ; E)$ by by Lemma 3.6. Since $P$ is injective on $H_{\delta^{\prime}}^{k, p}(\mathbb{B} ; E)$ by Theorem it is injective on the smaller space $C_{\delta}^{k, \alpha}(\mathbb{B} ; E)$. \(\square\)

\section*{CHAPTER 6}

\section*{Fredholm Theorems}

In this chapter, we return to the general case of a connected $(n+1)$-manifold $(M, g)$, assumed to be asymptotically hyperbolic of class $C^{l, \beta}$, with $l \geq 2$ and $0 \leq \beta<1$. Let $E$ be a geometric tensor bundle over $M$, and let $P: C^{\infty}(M ; E) \rightarrow$ $C^{\infty}(M ; E)$ be a formally self-adjoint geometric elliptic operator of order $m \geq 1$. We will prove Fredholm properties of $P$ by using Möbius coordinates near the boundary to piece together a parametrix modeled on the inverse operator on hyperbolic space.

For this purpose, we will need a slightly modified version of Möbius coordinates. Whereas the original Möbius coordinates defined in Chapter were valid in a neighborhood of an interior point, for our parametrix construction we will need coordinates that are defined all the way up to the boundary and adjusted to make the background metric $\bar{g}$ close to the Euclidean metric on a neighborhood of a boundary point. These coordinates will be used to transfer the operator $\breve{P}^{-1}$ to $M$ with an error that decays to one higher order along the boundary.

For each point $\widehat{p} \in \partial M$, choose some neighborhood $\Omega$ on which background coordinates $(\theta, \rho)$ are defined on a set of the form (2.1). Let $\omega^{1}, \ldots, \omega^{n} \in$ $C_{(0)}^{l, \beta}\left(\Omega, T^{*} \bar{M}\right)$ be 1-forms chosen so that $\left(\omega^{1}, \ldots, \omega^{n}, d \rho\right)$ is an orthonormal coframe for $\bar{g}$ at each point of $\partial M \cap \Omega$ (recall that $|d \rho|_{\bar{g}} \equiv 1$ along $\partial M$ ). Let $A_{\beta}^{\alpha}, B^{\alpha}$ be the coefficients of $\omega^{\alpha}$ at $\widehat{p}$, defined by
$$\omega_{\widehat{p}}^{\alpha}=A_{\beta}^{\alpha} d \theta_{\widehat{p}}^{\beta}+B^{\alpha} d \rho_{\widehat{p}}$$
and let $\left(\widetilde{\theta}^{1}, \ldots, \widetilde{\theta}^{n}\right)$ be the functions defined on $\Omega$ by
$$\widetilde{\theta}^{\alpha}=A_{\beta}^{\alpha} \theta^{\beta}+B^{\alpha} \rho .$$
Then $\left(\widetilde{\theta}^{1}, \ldots, \widetilde{\theta}^{n}, \rho\right)$ form coordinates on $\Omega$, and in these new coordinates $\bar{g}$ has the matrix $\delta_{i j}$ at $\widehat{p}$. For $0<a$ and $0<r<c$, define open subsets $Y_{a} \subset \mathbb{H}$ and $Z_{r}(\widehat{p}) \subset \Omega \subset M$ by
$$\begin{aligned}
Y_{a} & =\{(x, y) \in \mathbb{H}:|x|<a, 0<y<a\}, \\
Z_{r}(\widehat{p}) & =\{(\tilde{\theta}, \rho) \in \Omega:|\widetilde{\theta}|<r, 0<\rho<r\} .
\end{aligned}$$
For $0<r<c$, define a chart $\Psi_{\widehat{p}, r}: Y_{1} \rightarrow Z_{r}(\widehat{p})$ by
$$(\tilde{\theta}, \rho)=\Psi_{\widehat{p}, r}(x, y)=(r x, r y) .$$
We will call $\Psi_{\widehat{p}, r}$ a boundary Möbius chart of radius $r$ centered at $\widehat{p}$. Recall that $\breve{g}$ denotes the hyperboolic metric on the upper half-space.

Lemma 6.1. There is a constant $C>0$ such that for any $\widehat{p} \in \partial M$ and any sufficiently small $r>0$,
$$\left\|\Psi_{\widehat{p}, r}^{*} g-\breve{g}\right\|_{l, \beta ; Y_{1}} \leq r C .$$