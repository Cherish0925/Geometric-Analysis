---
retention_scope: session
part: 4
total_parts: 4
---

[Part 4/4 of: Monopoles over 4-manifolds containing long necks, I]

Proof We may assume $X$ is connected. Let $\widetilde{\Theta}$ be as in Subsection 3.4. Then
$$(S, \nu) \mapsto \widetilde{\Theta}(S, \mu+\nu, 0)$$
defines a smooth map
$$f: \mathcal{C}^{*} \times W \rightarrow L^{p, w}\left(X ; i \Lambda^{+} \oplus \mathbb{S}^{-}\right),$$
where $\mathcal{C}^{*}=\mathcal{C}^{*}(X ; \vec{\alpha})$. We will show that 0 is a regular value of $f$. Suppose $f(S, \nu)=0$ and write $S=(A, \Phi)$. We must show that the derivative $P=$ $D f(S, \nu)$ is surjective. Because of the gauge equivariance of $f$ we may assume that $S$ is smooth. Let $P_{1}$ denote the derivative of $f(\cdot, \nu)$ at $S$. Since the image of $P_{1}$ in $L^{p, w}$ is closed and has finite codimension, the same holds for the image of $P$. Let $p^{\prime}$ be the exponent conjugate to $p$ and suppose $(z, \psi) \in$ $L^{p^{\prime},-w}\left(X ; i \Lambda^{+} \oplus \mathbb{S}^{-}\right)$is $L^{2}$ orthogonal to the image of $P$, ie
$$\int_{X}\left\langle P\left(a, \phi, \nu^{\prime}\right),(z, \psi)\right\rangle=0$$
for all $(a, \phi) \in L_{1}^{p, w}$ and $\nu^{\prime} \in W$. Taking $\nu^{\prime}=0$ we see that $P_{1}^{*}(z, \psi)=0$. Since $P_{1}^{*}$ has injective symbol, $z, \psi$ must be smooth. On the other hand, taking $a, \phi=0$ and varying $\nu^{\prime}$ we find that $\left.z\right|_{K}=0$ by choice of $W$. By assumption, $\Phi$ is not identically zero. Since $D_{A} \Phi=0$, the unique continuation theorem in [19] applied to $D_{A}^{2}$ says that $\Phi$ cannot vanish in any non-empty open set. Hence $\Phi$ must be non-zero at some point $x$ in the interior of $K$. Varying $a$ alone near $x$ one sees that $\psi$ vanishes in some neighbourhood of $x$. But $P_{1} P_{1}^{*}$ has the same symbol as $D_{A}^{2} \oplus d^{+}\left(d^{+}\right)^{*}$, so another application of the same unique continuation theorem shows that $(z, \psi)=0$. Hence $P$ is surjective.

Consider now the vector bundle
$$E=\mathcal{C}^{*} \times_{\mathcal{G}} L^{p, w}\left(X ; i \Lambda^{+} \oplus \mathbb{S}^{-}\right)$$
over $\mathcal{B}^{*}$. The map $f$ defines a smooth section $\sigma$ of the bundle
$$E \times W \rightarrow \mathcal{B}^{*} \times W .$$
Because of the local slice theorem and the gauge equivariance of $f$, the fact that 0 is a regular value of $f$ means precisely that $\sigma$ is transverse to the zero-section. Since $\sigma(\cdot, \nu)$ is a Fredholm section of $E$ for any $\nu$, the proposition follows by another application of the Sard-Smale theorem. \(\square\)

We will now establish transversality results for moduli spaces of the form $M(X, \vec{\alpha})$ or $M(\alpha, \beta)$ involving perturbations of the kind discussed in Subsection 3.3. For the time being we limit ourselves to the case where the 3-manifolds $Y, Y_{j}$ are all rational homology spheres. We will use functions $h_{S}$ that are a small modification of those in [15]. To define these, let $Y$ be a closed Riemannian spin ${ }^{c} 3$-manifold satisfying $b_{1}(Y)=0$, and $\vartheta$ the Chern-Simons-Dirac functional on $Y$ defined by some closed 2-form $\eta$. Choose a smooth, nonnegative function $\chi: \mathbb{R} \rightarrow \mathbb{R}$ which is supported in the interval $\left(-\frac{1}{4}, \frac{1}{4}\right)$ and satisfies $\int \chi=1$. If $S$ is any $L_{1}^{2}$ configuration over a band $\left(a-\frac{1}{4}, b+\frac{1}{4}\right)$ where $a \leq b$ define the smooth function $\widetilde{\vartheta}_{S}:[a, b] \rightarrow \mathbb{R}$ by
$$\widetilde{\vartheta}_{S}(T)=\int_{\mathbb{R}} \chi(T-t) \vartheta\left(S_{t}\right) d t$$
where we interpret the right hand side as an integral over $\mathbb{R} \times Y$. A simple exercise, using the Sobolev embedding theorem, shows that if $S_{n} \rightarrow S$ weakly in $L_{1}^{2}$ over $\left(a-\frac{1}{4}, b+\frac{1}{4}\right) \times Y$ then $\widetilde{\vartheta}_{S_{n}} \rightarrow \widetilde{\vartheta}_{S}$ in $C^{\infty}$ over $[a, b]$.

Choose a smooth function $c: \mathbb{R} \rightarrow \mathbb{R}$ with the following properties:
\begin{itemize}
\item[-] $c^{\prime}>0$,
\item[-] $c$ and all its derivatives are bounded,
\item[-] $c(t)=t$ for all critical values $t$ of $\vartheta$,
\end{itemize}
where $c^{\prime}$ is the derivative of $c$. The last condition is added only for convenience.
For any $L_{1}^{2}$ configuration $S$ over $\left(a-\frac{1}{2}, b+\frac{1}{2}\right) \times Y$ with $a \leq b$ define
$$h_{S}(t)=\int_{\mathbb{R}} \chi\left(t_{1}\right) c\left(\widetilde{\vartheta}_{S}\left(t-t_{1}\right)\right) d t_{1} .$$
It is easy to verify that $h_{S}$ satisfies the properties (P1)-(P3).
It remains to choose $\Xi$ and $\mathfrak{P}$. Choose one compact subinterval (with non-empty interior) of each bounded connected component of $\mathbb{R} \backslash \operatorname{crit}(\vartheta)$, where $\operatorname{crit}(\vartheta)$ is the set of critical values of $\vartheta$. Let $\Xi$ be the union of these compact subintervals. Let $\mathfrak{P}=\mathfrak{P}_{Y}$ be a Banach space of 2-forms on $\mathbb{R} \times Y$ supported in $\Xi \times Y$ as provided by Lemma 8.2.

We now return to the situation described in the paragraph preceding Proposition 8.2 Let $W^{\prime} \subset W$ be the open subset consisting of those elements $\nu$ that satisfy $\|\nu\|_{C^{1}}<1$. Let $\Pi_{\delta}$ denote the set of all $\overrightarrow{\mathfrak{p}}=\left(\mathfrak{p}_{1}, \ldots, \mathfrak{p}_{r}\right)$ where $\mathfrak{p}_{j} \in \mathfrak{P}_{Y_{j}}$ and $\left\|\mathfrak{p}_{j}\right\|_{C^{1}}<\delta$ for each $j$.

Proposition 8.3 Suppose each $Y_{j}$ is a rational homology sphere and $K \subset X_{: 0}$. Then there exists a $\delta>0$ such that the following holds. Let $G$ be the set of all $(\nu, \overrightarrow{\mathfrak{p}}) \in W^{\prime} \times \Pi_{\delta}$ such that every irreducible point of the moduli space $M(X ; \vec{\alpha} ; \mu+\nu ; \overrightarrow{\mathfrak{p}})$ is regular. Then $G \subset W^{\prime} \times \Pi_{\delta}$ is residual, hence dense.

It seems necessary here to let $\overrightarrow{\mathfrak{p}}$ vary as well, because if any of the $\mathfrak{p}_{j}$ is non-zero then the linearization of the monopole map is no longer a differential operator, and it is not clear whether one can appeal to unique continuation as in the proof of Proposition 8.2.

Proof To simplify notation assume $r=1$ and set $Y=Y_{1}, \alpha=\alpha_{1}$ etc. (The proof in the general case is similar.) Note that (A) is trivially satisfied, since each $Y_{j}$ is a rational homology sphere. Therefore, by Propositions 4.3 and 5.6, if $\delta>0$ is sufficiently small then for any $(\nu, \mathfrak{p}) \in W^{\prime} \times \Pi_{\delta}$ and $[S] \in M(X ; \alpha ; \mu+\nu ; \mathfrak{p})$ one has that either
\begin{itemize}
\item[(i)] $\left[S_{t}\right]=\alpha$ for $t \geq 0$, or
\item[(ii)] $\partial_{t} \vartheta\left(S_{t}\right)<0$ for $t \geq 0$.
\end{itemize}
As in the proof of Proposition 8.2 it suffices to prove that 0 is a regular value of the smooth map
$$\begin{aligned}
\widetilde{f}: \mathcal{C}^{*} \times W^{\prime} \times \Pi_{\delta} & \rightarrow L^{p, w}, \\
(S, \nu, \mathfrak{p}) & \mapsto \widetilde{\Theta}(S, \mu+\nu, \mathfrak{p}) .
\end{aligned}$$
The smoothness of the perturbation term $g(S, \mathfrak{p})=\mathfrak{q} h_{S, \mathfrak{p}}$ follows from the smoothness of the map (19), for by (P1) there exist a $t_{0}$ and a neighbourhood $U \subset \mathcal{C}$ of $S$ such that $h_{S^{\prime}}(t) \notin \Xi$ for all $t>t_{0}$ and $S^{\prime} \in U$.
Now suppose $\widetilde{f}(S, \nu, \mathfrak{p})=0$ and $(z, \psi) \in L^{p^{\prime},-w}$ is orthogonal to the image of $D \widetilde{f}(S, \nu, \mathfrak{p})$. We will show that $z$ is orthogonal to the image of $T=D g(S, \mathfrak{p})$, or equivalently, that $(z, \psi)$ is orthogonal to the image of $D f(S, \nu)$, where $f=f-g$ as before. The latter implies $(z, \psi)=0$ by the proof of Proposition 8.2.

Let $h_{S}:\left[\frac{1}{2}, \infty\right) \rightarrow \mathbb{R}$ be defined in terms of the restriction of $S$ to $\mathbb{R}_{+} \times Y$. If $h_{S}(J) \subset \mathbb{R} \backslash \Xi$ for some compact interval $J$ then by (P1) one has that $h_{S^{\prime}}(J) \subset \mathbb{R} \backslash \Xi$ for all $S^{\prime}$ in some neighbourhood of $S$ in $\mathcal{C}$. Therefore, all elements of $\operatorname{im}(T)$ vanish on $h_{S}^{-1}(\mathbb{R} \backslash \Xi) \times Y$.

We now digress to recall that if $u$ is any locally integrable function on $\mathbb{R}^{n}$ then the complement of the Lebesgue set of $u$ has measure zero, and if $v$ is any continuous function on $\mathbb{R}^{n}$ then any Lebesgue point of $u$ is also a Lebesgue point of $u v$. The notion of Lebesgue set also makes sense for sections $\tau$ of a
vector bundle of finite rank over a finite dimensional smooth manifold $M$. In that case a point $x \in M$ is called a Lebesgue point of $\tau$ if it is a Lebesgue point in the usual sense for some (hence any) choice of local coordinates and local trivialization of the bundle around $x$.

Returning to our main discussion, there are now two cases: If (i) above holds then $h_{S}(t)=\vartheta(\alpha) \notin \Xi$ for $t \geq \frac{1}{2}$, whence $T=0$ and we are done (recall the overall assumption $\mathfrak{q}^{-1}(0)=X_{: \frac{3}{2}}$ made in Subsection 3.4). Otherwise (ii) must hold. In that case we have $\partial_{t} c(\widetilde{\vartheta}(t))<0$ for $t \geq \frac{1}{4}$ and $\partial_{t} h_{S}(t)<0$ for $t \geq \frac{1}{2}$. Since $z$ is orthogonal to $\mathfrak{q} h_{S, \mathfrak{p}^{\prime}}$ for all $\mathfrak{p}^{\prime} \in \mathfrak{P}_{Y}$ we conclude that $z(t, y)=0$ for every Lebesgue point $(t, y)$ of $z$ with $t>\frac{3}{2}$ and $h_{S}(t) \in \operatorname{int}(\Xi)$. Since $h_{S}^{-1}(\partial \Xi) \cap\left(\frac{3}{2}, \infty\right)$ is a finite set, $z$ must vanish almost everywhere in $\left[h_{S}^{-1}(\Xi) \cap\left(\frac{3}{2}, \infty\right)\right] \times Y$. Combining this with our earlier result we deduce that $z$ is orthogonal to $\operatorname{im}(T)$. \(\square\)

In the next proposition (which is similar to [15, Proposition 5]) let $\Pi_{\delta}$ be as above with $r=1$, and set $Y=Y_{1}$.

Proposition 8.4 In the situation of Subsection 1.2, suppose $Y$ is a rational homology sphere and $\alpha, \beta \in \mathcal{R}_{Y}=\widetilde{\mathcal{R}}_{Y}$. Then there exists a $\delta>0$ such that the following holds. Let $G$ be the set of all $\mathfrak{p} \in \Pi_{\delta}$ such that every point in $M(\alpha, \beta ; \mathfrak{p})$ is regular. Then $G \subset \Pi_{\delta}$ is residual, hence dense.

Proof If $\alpha=\beta$ then an application of Proposition 4.3 shows that if $\|\mathfrak{p}\|_{C^{1}}$ is sufficiently small then $M(\alpha, \beta ; \mathfrak{p})$ consists of a single point represented by $\underline{\alpha}$, which is regular because $\alpha$ is non-degenerate.

If $\alpha \neq \beta$ and $\|\mathfrak{p}\|_{C^{1}}$ is sufficiently small then for any $[S] \in M(\alpha, \beta ; \mathfrak{p})$ one has $\partial_{t} \vartheta\left(S_{t}\right)<0$ for all $t$. Moreover, the moduli space contains no reducibles, since $\alpha, \beta$ cannot both be reducible. The proof now runs along the same lines as that of Proposition 8.3 Note that the choice of $\Xi$ is now essential: it ensures that $\operatorname{im}\left(h_{S}\right)=(\vartheta(\alpha), \vartheta(\beta))$ contains interior points of $\Xi$. \(\square\)

\section*{9 Proof of Theorems 1.1 and 1.2}

In these proofs we will only use genuine monopoles.
Proof of Theorem 1.1 We may assume $Y$ is connected. Let $\eta$ be a closed non-exact 2-form on $Y$ which is the restriction of a closed form on $Z$. Let $Y$ have a metric of positive scalar curvature. If $s \neq 0$ is a small real number
then $\vartheta_{s \eta}$ will have no irreducible critical points, by the a priori estimate on the spinor fields and the positive scalar curvature assumption. If in addition $s[\eta]-\pi c_{1}\left(\mathcal{L}_{Y}\right) \neq 0$ then $\vartheta_{s \eta}$ will have no reducible critical points either.

Choose a spin ${ }^{c}$ Riemannian 4-manifold $X$ as in Subsection 1.4, with $r=1$, $r^{\prime}=0$, such that there exists a diffeomorphism $X^{\#} \rightarrow Z$ which maps $\{0\} \times Y_{1}$ isometrically onto $Y$. Let $\eta_{1}$ be the pull-back of $s \eta$. Then (B1) is satisfied (but perhaps not (B2)), so it follows from Theorem 1.4 that $M\left(X^{(T)}\right)$ is empty for $T \gg 0$. \(\square\)

We will now define an invariant $h$ for closed spin ${ }^{c} 3$-manifolds $Y$ that satisfy $b_{1}(Y)=0$ and admit metrics with positive scalar curvature. Let $g$ be such a metric on $Y$. Recall that for the unperturbed Chern-Simons-Dirac functional $\vartheta$ the space $\mathcal{R}_{Y}$ of critical points modulo gauge equivalence consists of a single point $\theta$, which is reducible. Let ( $B, 0$ ) be a representative for $\theta$. Let $Y_{1}, \ldots, Y_{r}$ be the connected components of $Y$ and choose a spin ${ }^{c}$ Riemannian 4-manifold $X$ with tubular ends $\mathbb{R}_{+} \times Y_{j}, j=1, \ldots, r$ (in the sense of Subsection 1.3) and a smooth spin connection $A$ over $X$ such that the restriction of $\check{A}$ to $\mathbb{R}_{+} \times Y$ is equal to the pull-back of $\check{B}$. (The notation here is explained in Subsection 3.1) Define
$$\begin{aligned}
h(Y, g) & =\operatorname{ind}_{\mathbb{C}}\left(D_{A}\right)-\frac{1}{8}\left(c_{1}\left(\mathcal{L}_{X}\right)^{2}-\sigma(X)\right) \\
& =\frac{1}{2}\left(\operatorname{dim} M(X ; \theta)-d(X)+b_{0}(X)\right),
\end{aligned}$$
where $D_{A}: L_{1}^{2} \rightarrow L^{2}$, 'dim' is the expected dimension, and $d(X)$ is the quantity defined in Subsection 1.1. Since $\operatorname{ind}_{\mathbb{C}}\left(D_{A}\right)=\frac{1}{8}\left(c_{1}\left(\mathcal{L}_{X}\right)^{2}-\sigma(X)\right)$ when $X$ is closed, it follows easily from the addition formula for the index (see [10, Proposition 3.9]) that $h(Y, g)$ is independent of $X$ and that
$$h(-Y, g)=-h(Y, g) .$$
Clearly,
$$h(Y, g)=\sum_{j} h\left(Y_{j}, g_{j}\right),$$
where $g_{j}$ is the restriction of $g$ to $Y_{j}$. To show that $h(Y, g)$ is independent of $g$ we may therefore assume $Y$ is connected. Suppose $g^{\prime}$ is another positive scalar curvature metric on $Y$ and consider the spin ${ }^{c}$ Riemannian manifold $X=\mathbb{R} \times Y$ where the metric agrees with $1 \times g$ on $(-\infty,-1] \times Y$ and with $1 \times g^{\prime}$ on $[1, \infty) \times Y$. Theorem 1.3 and Proposition 7.2 (ii) say that $M(X ; \theta, \theta)$ is compact. This moduli space contains one reducible point, and arguing as in the
proof of [15, Theorem 6] one sees that the moduli space must have non-positive (odd) dimension. Thus,
$$h\left(Y, g^{\prime}\right)+h(-Y, g)=\frac{1}{2}(\operatorname{dim} M(X ; \theta, \theta)+1) \leq 0 .$$
This shows $h(Y)=h(Y, g)$ is independent of $g$.
Proof of Theorem 1.2 Let each $Y_{j}$ have a positive scalar curvature metric. Choose a spin ${ }^{c}$ Riemannian 4-manifold $X$ as in Subsection 1.4 with $r^{\prime}=0$ and with the same $r$, such that there exists a diffeomorphism $f: X^{\#} \rightarrow Z$ which maps $\{0\} \times Y_{j}$ isometrically onto $Y_{j}$. Then (B1) is satisfied (but perhaps not (B2)). Let $X_{0}$ be the component of $X$ such that $W=f\left(\left(X_{0}\right)_{: 1}\right)$. For each $j$ set $\eta_{j}=0$ and let $\alpha_{j} \in \mathcal{R}_{Y_{j}}$ be the unique (reducible) critical point. Choose a reference connection $A_{o}$ as in Subsection 3.4 and set $A_{0}=\left.A_{o}\right|_{X_{0}}$. Since each $\alpha_{j}$ has representatives of the form $(B, 0)$ where $\check{B}$ is flat it follows that $\hat{F}\left(A_{o}\right)$ is compactly supported. In the following, $\mu$ will denote the (compactly supported) perturbation 2-form on $X$ and $\mu_{0}$ its restriction to $X_{0}$.

Let $\mathcal{H}^{+}$be the space of self-dual closed $L^{2}$ 2-forms on $X_{0}$. Then $\operatorname{dim} \mathcal{H}^{+}=$ $b_{2}^{+}\left(X_{0}\right)>0$, so $\mathcal{H}^{+}$contains a non-zero element $z$. By unique continuation for harmonic forms we can find a smooth 2 -form $\mu_{0}$ on $X_{0}$, supported in any given small ball, such that $\hat{F}^{+}\left(A_{0}\right)+i \mu_{0}^{+}$is not $L^{2}$ orthogonal to $z$. (Here $\hat{F}^{+}$ is the self-dual part of $\hat{F}$.) Then
$$\hat{F}^{+}\left(A_{0}\right)+i \mu_{0}^{+} \notin \operatorname{im}\left(d^{+}: L_{1}^{p, w} \rightarrow L^{p, w}\right),$$
where $w$ is the weight function used in the definition of the configuration space. Hence $M\left(X_{0} ; \vec{\alpha}\right)$ contains no reducible monopoles. After perturbing $\mu_{0}$ in a small ball we can arrange that $M\left(X_{0} ; \vec{\alpha}\right)$ is transversally cut out as well, by Proposition 8.2

To prove (i), recall that
$$\operatorname{dim} M\left(X_{0} ; \vec{\alpha}\right)=d(W)-1+2 \sum_{j} h\left(Y_{j}\right),$$
so the inequality in (i) simply says that
$$\operatorname{dim} M\left(X_{0} ; \vec{\alpha}\right)<0,$$
hence $M\left(X_{0} ; \vec{\alpha}\right)$ is empty. Since there are no other moduli spaces over $X_{0}$, it follows from Theorem 1.4 that $M\left(X^{(T)}\right)$ is empty when $\min _{j} T_{j} \gg 0$.
We will now prove (ii). If $M\left(X^{(T)}\right)$ has odd or negative dimension then there is nothing to prove, so suppose this dimension is $2 m \geq 0$. Since $M\left(X_{0} ; \vec{\alpha}\right)$ contains no reducibles we deduce from Theorem 1.4 that $M\left(X^{(T)}\right)$ is also free
of reducibles when $\min _{j} T_{j}$ is sufficiently large. Let $\mathbf{B} \subset X_{0}$ be a compact 4-ball and $\mathcal{B}^{*}(\mathbf{B})$ the Banach manifold of irreducible $L_{1}^{p}$ configurations over $\mathbf{B}$ modulo $L_{2}^{p}$ gauge transformations. Here $p>4$ should be an even integer to ensure the existence of smooth partitions of unity. Let $\mathbb{L} \rightarrow \mathcal{B}^{*}(\mathbf{B})$ be the natural complex line bundle associated to some base-point in B, and $s$ a generic section of the $m$-fold direct sum $m \mathbb{L}$. For $\min _{j} T_{j} \gg 0$ let
$$S^{(T)} \subset M\left(X^{(T)}\right), \quad S_{0} \subset M\left(X_{0} ; \vec{\alpha}\right)$$
be the subsets consisting of those elements $\omega$ that satisfy $s\left(\left.\omega\right|_{\mathbf{B}}\right)=0$. By assumption, $S_{0}$ is a submanifold of codimension $2 m$. For any $T$ for which $S^{(T)}$ is transversely cut out the Seiberg-Witten invariant of $Z$ is equal to the number of points in $S^{(T)}$ counted with sign. Now, the inequality in (ii) is equivalent to
$$d(W)+2 \sum_{j} h\left(Y_{j}\right)<d(Z)=2 m+1,$$
which by (43) gives
$$\operatorname{dim} S_{0}=\operatorname{dim} M\left(X_{0} ; \vec{\alpha}\right)-2 m<0 .$$
Therefore, $S_{0}$ is empty. By Theorem $1.4 S^{(T)}$ is empty too when $\min _{j} T_{j} \gg 0$, hence $\operatorname{SW}(Z)=0$. \(\square\)

\section*{A Patching together local gauge transformations}

In the proof of Lemma 4.1 we encounter sequences $S_{n}$ of configurations such that for any point $x$ in the base-manifold there is a sequence $v_{n}$ of gauge transformations defined in a neighbourhood of $x$ such that $v_{n}\left(S_{n}\right)$ converges (in some Sobolev norm) in a (perhaps smaller) neighbourhood of $x$. The problem then is to find a sequence $u_{n}$ of global gauge transformations such that $u_{n}\left(S_{n}\right)$ converges globally. If $v_{n}, w_{n}$ are two such sequences of local gauge transformations then $v_{n} w_{n}^{-1}$ will be bounded in the appropriate Sobolev norm, so the problem reduces to the lemma below.

This issue was discussed by Uhlenbeck in [32, Section 3]. Our approach has the advantage that it does not involve any "limiting bundles".

Lemma A. 1 Let $X$ be a Riemannian manifold and $P \rightarrow X$ a principal $G$ -bundle, where $G$ is a compact subgroup of some matrix algebra $M_{r}(\mathbb{R})$. Let $M_{r}(\mathbb{R})$ be equipped with an $A d_{G}$-invariant inner product, and fix a connection in the Euclidean vector bundle $E=P \times_{A d_{G}} M_{r}(\mathbb{R})$ (which we use to define

Sobolev norms of automorphisms of E). Let $\left\{U_{i}\right\}_{i=1}^{\infty},\left\{V_{i}\right\}_{i=1}^{\infty}$ be open covers of $X$ such that $U_{i} \Subset V_{i}$ for each $i$. We also assume that each $V_{i}$ is the interior of a compact codimension 0 submanifold of $X$, and that $\partial V_{i}$ and $\partial V_{j}$ intersect transversally for all $i \neq j$. For each $i$ and $n=1,2, \ldots$ let $v_{i, n}$ be a continuous automorphism of $\left.P\right|_{V_{i}}$. Suppose $v_{i, n} v_{j, n}^{-1}$ converges uniformly over $V_{i} \cap V_{j}$ for each $i, j$ (as maps into $E$ ). Then there exist
\begin{itemize}
\item[-] a sequence of positive integers $n_{1} \leq n_{2} \leq \cdots$,
\item[-] for each positive integer $k$ an open subset $W_{k} \subset X$ with
$$\bigcup_{i=1}^{k} U_{i} \Subset W_{k} \subset \bigcup_{i=1}^{k} V_{i},$$
\item[-] for each $k$ and $n \geq n_{k}$ a continuous automorphism $w_{k, n}$ of $\left.P\right|_{W_{k}}$,
\end{itemize}
such that
\begin{itemize}
\item[(i)] If $1 \leq j \leq k$ and $n \geq n_{k}$ then $w_{j, n}=w_{k, n}$ on $\bigcup_{i=1}^{j} U_{i}$,
\item[(ii)] For each $i, k$ the sequence $w_{k, n} v_{i, n}^{-1}$ converges uniformly over $W_{k} \cap V_{i}$,
\item[(iii)] If $1 \leq p<\infty$, and $m>\frac{n}{p}$ is an integer such that $v_{i, n} \in L_{m, l o c}^{p}$ for all $i, n$ then $w_{k, n} \in L_{m, \text { loc }}^{p}$ for all $k$ and $n \geq n_{k}$. If in addition
$$\sup _{n}\left\|v_{i, n} v_{j, n}^{-1}\right\|_{L_{m}^{p}\left(V_{i} \cap V_{j}\right)}<\infty \quad \text { for all } i, j$$
then
$$\sup _{n \geq n_{k}}\left\|w_{k, n} v_{i, n}^{-1}\right\|_{L_{m}^{p}\left(W_{k} \cap V_{i}\right)}<\infty \quad \text { for all } k, i .$$
\end{itemize}
The transversality condition ensures that the Sobolev embedding theorem holds for $V_{i} \cap V_{j}$ (see [1]). Note that this condition can always be achieved by shrinking the $V_{i}$ 's a little.

Proof Let $N^{\prime} \subset L G$ be a small $\operatorname{Ad}_{G}$ invariant open neighbourhood of 0. Then $\exp : L G \rightarrow G$ maps $N^{\prime}$ diffeomorphically onto an open neighbourhood $N$ of 1. Let $f: N \rightarrow N^{\prime}$ denote the inverse map. Let $\operatorname{Aut}(P)$ the bundle of fibre automorphisms of $P$ and $\mathfrak{g}_{P}$ the corresponding bundle of Lie algebras. Set $\mathbf{N}=P \times \times_{\operatorname{Ad}_{G}} N \subset \mathfrak{g}_{P}$ and let $\exp ^{-1}: \mathbf{N} \rightarrow \operatorname{Aut}(P)$ be the map defined by $f$.

Set $w_{1, n}=v_{1, n}$ and $W_{1}=V_{1}$. Now suppose $w_{k, n}, W_{k}$ have been chosen for $1 \leq k<\ell$, where $\ell \geq 2$, such that (i)-(iii) hold for these values of $k$. Set $z_{n}=w_{\ell-1, n}\left(v_{\ell, n}\right)^{-1}$ on $W_{\ell-1} \cap V_{\ell}$. According to the induction hypothesis the
sequence $z_{n}$ converges uniformly over $W_{\ell-1} \cap V_{\ell}$, hence there exists an integer $n_{\ell} \geq n_{\ell-1}$ such that $y_{n}=\left(z_{n_{\ell}}\right)^{-1} z_{n}$ takes values in $\mathbf{N}$ for $n \geq n_{\ell}$.

Choose an open subset $\mathcal{W} \subset X$ which is the interior of a compact codimension 0 submanifold of $X$, and which satisfies
$$\bigcup_{i=1}^{\ell-1} U_{i} \Subset \mathcal{W} \Subset W_{\ell-1} .$$
We also require that $\partial \mathcal{W}$ intersect $\partial V_{i} \cap \partial V_{j}$ transversally for all $i, j$. (For instance, one can take $\mathcal{W}=\alpha^{-1}([0, \epsilon])$ for suitable $\epsilon$, where $\alpha: X \rightarrow[0,1]$ is any smooth function with $\alpha=0$ on $\cup_{i=1}^{\ell-1} U_{i}$ and $\alpha=1$ on $W_{\ell-1}$.) Choose also a smooth, compactly supported function $\phi: W_{\ell-1} \rightarrow \mathbb{R}$ with $\left.\phi\right|_{\mathcal{W}}=1$. Set $W_{\ell}=\mathcal{W} \cup V_{\ell}$ and for $n \geq n_{\ell}$ define an automorphism $w_{\ell, n}$ of $\left.P\right|_{W_{\ell}}$ by
$$w_{\ell, n}= \begin{cases}w_{\ell-1, n} & \text { on } \mathcal{W}, \\ z_{n_{\ell}} \exp \left(\phi \exp ^{-1} y_{n}\right) v_{\ell, n} & \text { on } W_{\ell-1} \cap V_{\ell}, \\ z_{n_{\ell}} v_{\ell, n} & \text { on } V_{\ell} \backslash \operatorname{supp}(\phi) .\end{cases}$$
Then (i)-(iii) hold for $k=\ell$ as well. To see that (iii) holds, note that our transversality assumptions guarantee that the Sobolev embedding theorem holds for $W_{\ell-1} \cap V_{\ell}$ and for all $V_{i} \cap V_{j}$. Since $m p>n, L_{m}^{p}$ is therefore a Banach algebra for these spaces (see [1]). Recalling the proof of this fact, and the behaviour of $L_{m}^{p}$ under composition with smooth maps on the left (see [27], p 184]), one obtains (iii). \(\square\)

\section*{B A quantitative inverse function theorem}

In this section $E, E^{\prime}$ will be Banach spaces. We denote by $\mathcal{B}\left(E, E^{\prime}\right)$ the Banach space of bounded operators from $E$ to $E^{\prime}$. If $T \in \mathcal{B}\left(E, E^{\prime}\right)$ then $\|T\|=\sup _{\|x\| \leq 1}\|T x\|$. If $U \subset E$ is open and $f: U \rightarrow E^{\prime}$ smooth then $D f(x) \in \mathcal{B}\left(E, E^{\prime}\right)$ is the derivative of $f$ at $x \in U$. The second derivative $D(D f)(x) \in \mathcal{B}\left(E, \mathcal{B}\left(E, E^{\prime}\right)\right)$ is usually written $D^{2} f(x)$ and can be identified with the symmetric bilinear map $E \times E \rightarrow E^{\prime}$ given by
$$D^{2} f(x)(y, z)=\left.\frac{\partial^{2}}{\partial s \partial t}\right|_{(0,0)} f(x+s y+t z) .$$
The norm of the second derivative is
$$\left\|D^{2} f(x)\right\|=\sup _{\|y\|,\|z\| \leq 1}\left\|D^{2} f(x)(y, z)\right\| .$$

For $r>0$ let
$$B_{r}=\{x \in E:\|x\|<r\} .$$

Lemma B. 1 Let $\epsilon, M>0$ be positive real numbers such that $\epsilon M<1$, and suppose $f: B_{\epsilon} \rightarrow E$ is a smooth map satisfying
$$f(0)=0 ; \quad D f(0)=I ; \quad\left\|D^{2} f(x)\right\| \leq M \quad \text { for } x \in B_{\epsilon} .$$
Then $f$ restricts to a diffeomorphism $f^{-1} B_{\frac{\epsilon}{2}} \xrightarrow{ } B_{\frac{\epsilon}{2}}$.
The conclusion of the lemma holds even when $\epsilon M=1$, see Proposition B. 1 below.

Proof The estimate on $D^{2} f$ gives
$$\|D f(x)-I\|=\|D f(x)-D f(0)\| \leq M\|x\| .$$
Therefore the map
$$h(x)=f(x)-x=\int_{0}^{1}(D f(t x)-I) x d t$$
satisfies
$$\begin{gathered}
\|h(x)\| \leq \frac{M}{2}\|x\|^{2} \\
\left\|h\left(x_{2}\right)-h\left(x_{1}\right)\right\| \leq \epsilon M\left\|x_{2}-x_{1}\right\|
\end{gathered}$$
for all $x, x_{1}, x_{2} \in B_{\epsilon}$. Hence for every $y \in B_{\frac{\epsilon}{2}}$ the assignment $x \mapsto y-h(x)$ defines a map $B_{\epsilon} \rightarrow B_{\epsilon}$ which has a unique fix-point. In other words, $f$ maps $f^{-1} B_{\frac{\epsilon}{2}}$ bijectively onto $B_{\frac{\epsilon}{2}}$. Moreover, $D f(x)$ is an isomorphism for every $x \in \stackrel{2}{B}_{\epsilon}$, by (44). Applying the contraction mapping argument above to $f$ around an arbitrary point in $B_{\epsilon}$ then shows that $f$ is an open map. It is then a simple exercise to prove that the inverse $g: B_{\frac{\epsilon}{2}} \rightarrow f^{-1} B_{\frac{\epsilon}{2}}$ is differentiable and $D g(y)=(D f(g(y)))^{-1}$ (see [8, 8.2.3]). Repeated application of the chain rule then shows that $g$ is smooth. \(\square\)

For $r>0$ let $B_{r} \subset E$ be as above, and define $B_{r}^{\prime} \subset E^{\prime}$ similarly.
Proposition B. 1 Let $\epsilon, M$ be positive real numbers and $f: B_{\epsilon} \rightarrow E^{\prime}$ a smooth map such that $f(0)=0, L=D f(0)$ is invertible, and
$$\left\|D^{2} f(x)\right\| \leq M \quad \text { for all } x \in B_{\epsilon} .$$
Set $\kappa=\left\|L^{-1}\right\|^{-1}-\epsilon M$ and $\epsilon^{\prime}=\epsilon\left\|L^{-1}\right\|^{-1}$. Then the following hold:
\begin{itemize}
\item[(i)] If $\kappa \geq 0$ then $f$ is a diffeomorphism onto an open subset of $E^{\prime}$ containing $B_{\epsilon^{\prime} / 2}^{\prime}$.
\item[(ii)] If $\kappa>0$ and $g: B_{\epsilon^{\prime} / 2}^{\prime} \rightarrow B_{\epsilon}$ is the smooth map satisfying $f \circ g=I$ then for all $x \in B_{\epsilon}$ and $y \in B_{\epsilon^{\prime} / 2}^{\prime}$ one has
$$\left\|D f(x)^{-1}\right\|,\|D g(y)\|<\kappa^{-1}, \quad\left\|D^{2} g(y)\right\|<M \kappa^{-3} .$$
\end{itemize}
The reader may wish to look at some simple example (such as a quadratic polynomial) to understand the various ways in which these results are optimal.

Proof (i) For every $x \in B_{\epsilon}$ we have
$$\left\|D f(x) L^{-1}-I\right\| \leq\|D f(x)-L\| \cdot\left\|L^{-1}\right\|<\epsilon M\left\|L^{-1}\right\| \leq 1,$$
hence $D f(x)$ is invertible. Thus $f$ is a local diffeomorphism by Lemma B. 1 Set $h(x)=f(x)-L x$. If $x_{1}, x_{2} \in B_{\epsilon}$ and $x_{1} \neq x_{2}$ then
$$\left\|f\left(x_{2}\right)-f\left(x_{1}\right)\right\| \geq\left\|L\left(x_{2}-x_{1}\right)\right\|-\left\|h\left(x_{2}\right)-h\left(x_{1}\right)\right\|>\kappa\left\|x_{2}-x_{1}\right\|,$$
hence $f$ is injective. By choice of $\epsilon^{\prime}$ the map
$$\widetilde{f}=f \circ L^{-1}: B_{\epsilon^{\prime} / 2}^{\prime} \rightarrow E^{\prime}$$
is well defined, and for every $y \in B_{\epsilon^{\prime} / 2}^{\prime}$ one has
$$\left\|D^{2} \widetilde{f}(y)\right\| \leq M\left\|L^{-1}\right\|^{2} .$$
Because
$$\epsilon^{\prime} M\left\|L^{-1}\right\|^{2}=\epsilon M\left\|L^{-1}\right\| \leq 1,$$
Lemma B. 1 says that the image of $\widetilde{f}$ contains every ball $B_{\delta / 2}^{\prime}$ with $0<\delta<\epsilon^{\prime}$, hence also $B_{\epsilon^{\prime} / 2}^{\prime}$.
(ii) Set $c=I-D f(x) L^{-1}$. Then
$$D f(x)^{-1}=L^{-1} \sum_{n=0}^{\infty} c^{n},$$
hence
$$\left\|D f(x)^{-1}\right\| \leq \frac{\left\|L^{-1}\right\|}{1-\|c\|}<\frac{\left\|L^{-1}\right\|}{1-\epsilon M\left\|L^{-1}\right\|}=\kappa^{-1} .$$
This also gives the desired bound on $D g(y)=D f(g(y))^{-1}$.
To estimate $D^{2} g$, let $\operatorname{Iso}\left(E, E^{\prime}\right) \subset \mathcal{B}\left(E, E^{\prime}\right)$ be the open subset of invertible operators, and let $\iota: \operatorname{Iso}\left(E, E^{\prime}\right) \rightarrow \mathcal{B}\left(E^{\prime}, E\right)$ be the inversion map: $\iota(a)=a^{-1}$. Then $\iota$ is smooth, and its derivative is given by
$$D \iota(a) b=-a^{-1} b a^{-1},$$
see [8]. The chain rule says that
$$\begin{aligned}
D g & =\iota \circ D f \circ g, \\
D(D g)(y) & =D \iota(D f(g(y))) \circ D(D f)(g(y)) \circ D g(y) .
\end{aligned}$$
This gives
$$\|D(D g)(y)\| \leq\left\|D f(g(y))^{-1}\right\|^{2} \cdot\|D(D f)(g(y))\| \cdot\|D g(y)\|<\kappa^{-2} \cdot M \cdot \kappa^{-1} .$$ \(\square\)

\section*{References}
\begin{itemize}
\item[] [1] R A Adams, Sobolev Spaces, Pure and Applied Mathematics 65, Academic Press (1975) MathReview
\item[] [2] MF Atiyah, The index theorem for manifolds with boundary, from: "Seminar on the Atiyah-Singer index theorem", Ann. of Math. Studies 57, Princeton University Press (1965) MathReview
\item[] [3] M F Atiyah, V K Patodi, I M Singer, Spectral asymmetry and Riemannian geometry. I, Math. Proc. Camb. Phil. Soc. 77 (1975) 43-69 MathReview
\item[] [4] Ch Bär, Zero Sets of Solutions to Semilinear Elliptic Systems of First Order, Invent. Math. 138 (1999) 183-202 MathReview
\item[] [5] S Bauer, A stable cohomotopy refinement of Seiberg-Witten invariants: II, Inv. Math. 155 (2004) 21-40 MathReview
\item[] [6] S Bauer, Refined Seiberg-Witten invariants, from: "Different Faces of Geometry", (S K Donaldson, Y Eliashberg, M Gromov, editors), Plenum Publishing Corporation (2004)
\item[] [7] S Bauer, M Furuta, A stable cohomotopy refinement of Seiberg-Witten invariants: I, Inv. Math. 155 (2004) 1-19 MathReview
\item[] [8] J Dieudonné, Foundations of Modern Analysis, Pure and Applied Mathematics 10, Academic Press (1960) MathReview
\item[] [9] S K Donaldson, The Seiberg-Witten equations and 4-manifold topology, Bull. AMS 33 (1996) 45-70 MathReview
\item[] [10] S K Donaldson, Floer Homology Groups in Yang-Mills Theory, Cambridge Tracts in Mathematics 147, Cambridge University Press (2002) MathReview
\item[] [11] S K Donaldson, P B Kronheimer, The Geometry of Four-Manifolds, Oxford University Press (1990) MathReview
\item[] [12] R Fintushel, R J Stern, Immersed spheres in 4-manifolds and the immersed Thom conjecture, Turkish J. Math. 19 (1995) 145-157 MathReview
\item[] [13] A Floer, An instanton invariant for 3-manifolds, Comm. Math. Phys. 118 (1988) 215-240 MathReview
\end{itemize}
\begin{itemize}
\item[] [14] K A Frøyshov, Monopole Floer homology for rational homology 3-spheres, in preparation
\item[] [15] K A Frøyshov, The Seiberg-Witten equations and four-manifolds with boundary, Math. Res. Letters 3 (1996) 373-390 MathReview
\item[] [16] RS Hamilton, Harmonic maps of manifolds with boundary, Lecture notes in mathematics 471, Springer-Verlag (1975) MathReview
\item[] [17] L Hörmander, The Analysis of Linear Partial Differential Operators III, Grundlehren der Mathematischen Wissenschaften 274, Springer-Verlag (1985) MathReview
\item[] [18] M Ishida, C LeBrun, Curvature, connected sums, and Seiberg-Witten theory, Comm. Anal. Geom. 11 (2003) 809-836 MathReview
\item[] [19] J Kazdan, Unique continuation in geometry, Comm. Pure and Applied Math. 41 (1988) 667-681 MathReview
\item[] [20] P B Kronheimer, T S Mrowka, Floer homology for Seiberg-Witten monopoles, book in preparation
\item[] [21] P B Kronheimer, T S Mrowka, The genus of embedded surfaces in the projective plane, Math. Res. Letters 1 (1994) 797-808 MathReview
\item[] [22] P B Kronheimer, T S Mrowka, P S Ozsváth, Z Szabó, Monopoles and lens space surgeries, arXiv:math.GT/0310164
\item[] [23] HB Lawson, M-L Michelsohn, Spin Geometry, Princeton Mathematical Series 38, Princeton University Press (1989) MathReview
\item[] [24] R B Lockhart, R C McOwen, Elliptic differential operators on non-compact manifolds, Ann. Scuola Norm. Sup. Pisa (4) 12 (1985) 409-447 MathReview
\item[] [25] M Marcolli, Seiberg-Witten-Floer homology and Heegaard splittings, Intern. J. Math. 7 (1996) 671-696 MathReview
\item[] [26] M Marcolli, B-L Wang, Equivariant Seiberg-Witten Floer homology, Comm. Anal. and Geom. 9 (2001) 451-639 MathReview
\item[] [27] D McDuff, D Salamon, $J$-holomorphic Curves and Quantum Cohomology, University Lecture Series 6, American Math. Soc. (1994) MathReview
\item[] [28] J Morgan, Z Szabó, C H Taubes, A product formula for the Seiberg-Witten invariants and the generalized Thom conjecture, J. Differential Geometry 44 (1996) 706-788 MathReview
\item[] [29] LI Nicolaescu, Notes on Seiberg-Witten theory, Graduate Studies in Mathematics 28, American Mathematical Society (2000) MathReview
\item[] [30] D A Salamon, Removable singularities and a vanishing theorem for Seiberg-Witten invariants, Turkish J. Math. 20 (1996) 61-73 MathReview
\item[] [31] ME Taylor, Partial Differential Equations I. Basic Theory, Texts in Applied Mathematics 23, Springer-Verlag (1996) MathReview
\item[] [32] K K Uhlenbeck, Connections with $L^{p}$ bounds on curvature, Comm. Math. Phys. 83 (1982) 31-42 MathReview
\end{itemize}