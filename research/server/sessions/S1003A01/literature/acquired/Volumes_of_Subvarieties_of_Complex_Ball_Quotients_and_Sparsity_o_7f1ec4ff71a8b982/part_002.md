---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Volumes of Subvarieties of Complex Ball Quotients and Sparsity of Rational Points]

We represent $\gamma_{1}$ and $\gamma_{2}$ by the matrices $g_{\infty}, g_{0} \in \mathrm{PU}(Q)$ respectively, where
$$g_{\infty}=\left[\begin{array}{ccc}
1 & -\tau^{*} & -(|\tau|+i t) / 2 \\
0 & I_{n-1} & \tau \\
0 & 0 & 1
\end{array}\right], \quad g_{0}=\left[\begin{array}{ccc}
1 & 0 & 0 \\
\sigma & I_{n-1} & 0 \\
-(|\tau|+i s) / 2 & -\sigma^{*} & 1
\end{array}\right] .$$
Note that $\gamma_{1}^{-1}=(-\tau,-t)$ corresponds to $g_{\infty}^{-1}$. We can write:
$$\begin{aligned}
\left|\operatorname{tr}\left(g_{\infty} g_{0}\right)\right|+\left|\operatorname{tr}\left(g_{\infty}^{-1} g_{0}\right)\right| & \geq\left|\operatorname{tr}\left(\left(g_{\infty}+g_{\infty}^{-1}\right) g_{0}\right)\right| \\
& =\left|\operatorname{tr}\left(\left[\begin{array}{ccc}
2 & 0 & -|\tau|^{2} \\
0 & 2 I_{n-1} & 0 \\
0 & 0 & 2
\end{array}\right]\left[\begin{array}{ccc}
1 & 0 & 0 \\
\sigma & I_{n-1} & 0 \\
\left(-|\sigma|^{2}+i s\right) / 2 & -\sigma^{*} & 1
\end{array}\right]\right)\right| \\
& \left.=\left.\left|2(n+1)+\frac{1}{2}\right| \tau\right|^{2}\left(|\sigma|^{2}-i s\right) \right\rvert\, \\
& \geq 2(n+1)+\frac{1}{2}|\tau|^{2}|\sigma|^{2}
\end{aligned}$$
Hence, either $\left|\operatorname{tr}\left(g_{\infty} g_{0}\right)\right| \geq n+1+\frac{1}{4}|\tau|^{2}|\sigma|^{2}$ or $\left|\operatorname{tr}\left(g_{\infty}^{-1} g_{0}\right)\right| \geq n+1+\frac{1}{4}|\tau|^{2}|\sigma|^{2}$ and therefore either $\gamma_{1} \gamma_{2}$ or $\gamma_{1}^{-1} \gamma_{2}$ must be hyperbolic. But this implies that either $d\left(\tilde{x}, \gamma_{1} \gamma_{2} . \tilde{x}\right) \geq \operatorname{sys}(X)$ or $d\left(\tilde{x}, \gamma_{1}^{-1} \gamma_{2} \cdot \tilde{x}\right) \geq \operatorname{sys}(X)$, which is a contradiction because $d\left(\tilde{x}, \gamma_{2} \cdot \tilde{x}\right)<\operatorname{sys}(X) / 2, d\left(\tilde{x}, \gamma_{1} \cdot \tilde{x}\right)<$ $\operatorname{sys}(X) / 2$, and $d\left(\tilde{x}, \gamma_{1}^{-1} \cdot \tilde{x}\right)<\operatorname{sys}(X) / 2$. \(\square\)

We define the thick part of $X$ as the complement of the thin part:
$$X_{\text {thick }}:=X \backslash \cup_{i=1}^{k} U_{i, \rho} .$$
Since every point in a thin part of $X$ has a displacement less than $\operatorname{sys}(X) / 2$, the following Proposition tells us that $X_{\text {thick }} \neq \varnothing$.

Proposition 4.2. There exists $x \in X$ such that
$$\operatorname{inj}_{\mathrm{x}}(\mathrm{X}) \geq \operatorname{sys}(X) / 2 .$$
Proof. Note that if $\gamma \in \Gamma$ is not unipotent, then it is semi-simple and for such $\gamma$ and every $x \in \mathbb{B}^{n}$, we have $d(x, \gamma \cdot x) \geq \operatorname{sys}(X)$.

Now, assume for the sake of contradiction that $\operatorname{inj}_{x}(X)<\operatorname{sys}(X) / 2$ for all $x \in X$. Therefore, for all $x$ there is a unipotent element $\gamma \in \Gamma$ such that $d(x, \gamma \cdot x)<\operatorname{sys}(X) / 2$. This means that the thin part of $X$ covers all $X$. However, this is not possible because the thin part of $X$ is a disjoint union of open sets by Proposition 4.1 but $X$ is connected. \(\square\)

Now we show that the monodromy of the $\rho$-thin part of $X$ around each cusp is in the stabilizer of that cusp:

Lemma 4.3. Suppose that $\epsilon<\operatorname{sys}(X) / 2$. Let $U_{i}^{\prime}$ be a connected component of $U_{i, \epsilon}$ and $\iota: U_{i}^{\prime} \rightarrow X$ be the identity map. Then, $\iota_{*}\left(\pi_{1}\left(U_{i}^{\prime}\right)\right)$ is a subgroup of $\Gamma_{i}$.

Proof. As $\epsilon<\operatorname{sys}(X) / 2$, Proposition 4.1 implies that $U_{i, \epsilon} \mathrm{~s}$ are disjoint. Fix $x \in U_{i}^{\prime}$ and let $\gamma:[0,1] \rightarrow X$ be a loop at $x$ which is a representative of a class in $\iota_{*}\left(\pi_{1}\left(U_{i}^{\prime}, x\right)\right)$. Let $\tilde{x}$ be a lift of $x$ to the universal cover $\mathbb{B}^{n}$. As $\gamma$ is fully contained in $U_{i, \epsilon}^{\prime}$, we can lift it to a path $\tilde{\gamma}:[0,1] \rightarrow \tilde{U}_{i, \epsilon}$ which starts at $\tilde{x}$. Therefore, $\tilde{y}:=\gamma \cdot \tilde{x}=\tilde{\gamma}(1)$ is in $\tilde{U}_{i, \epsilon}$. Let $\gamma^{\prime} \in \Gamma_{i}$ such that $d\left(\tilde{x}, \gamma^{\prime} \cdot \tilde{x}\right)<\epsilon$. By homogeneity, we have
$$d\left(\tilde{y}, \gamma \gamma^{\prime} \gamma^{-1} \cdot \tilde{y}\right)=d\left(\gamma \cdot \tilde{x}, \gamma \gamma^{\prime} \gamma^{-1} \gamma \cdot \tilde{x}\right)=d\left(\tilde{x}, \gamma^{\prime} \cdot \tilde{x}\right)<\epsilon .$$
Since $\gamma \gamma^{\prime} \gamma^{-1}$ fixes $\gamma\left(q_{i}\right)$, the previous inequality tells us that $\tilde{y}$ is in the $\epsilon$-thin neighborhood around $\gamma\left(q_{i}\right)$. On the other hand we know $\tilde{y} \in U_{i, \epsilon}$. Since the thin neighborhoods around cusps are disjoint therefore $\gamma\left(q_{i}\right)=q_{i}$, i.e., $\gamma \in \Gamma_{i}$, as desired. \(\square\)

Finally, we show that every subvariety of $X$ intersects with $X_{\text {thick }}$, that is, every subvariety of $X$ contains a point whose injectivity radius in $X$ is larger than $\operatorname{sys}(X) / 2$ :

Theorem 4.4. Every subvariety of $\bar{X}$ either intersects with $X_{\text {thick }}$ or fully contained in the boundary $D$, where $\bar{X}=X \cup D$.

Proof. For the sake of contradiction, assume that there exists a connected subvariety $V$ fully contained in $X_{\text {thin }}$. By Proposition 4.1, $V$ must be contained within a thin neighborhood of a cusp of $X$, say $c_{i}$. With a change of coordinates if necessary (i.e., by conjugating the lattice $\Gamma$ ), we can assume that $c_{i}$ is identified with the equivalence class of $q_{\infty}$. Note that the systole of $X$ is invariant under this change of coordinates, and therefore so is $X_{\text {thin }}$.

Consider the function $-u$ which is a plurisubharmonic function on the Siegel domain $\mathbb{S}$ and invariant under the action of stabilizer $\Gamma_{\infty}$ (see [BT18, §2]). Therefore, it follows from Lemma 4.3 that $-u$ is a well-defined function on every component of the thin part around $q_{\infty}$. Hence, $-u$ is a well-defined plurisubharmonic function on $V$. Notice that if a plurisubharmonic function achieves its maximum on a closed connected variety, it has to be
constant(see [GR22, page 272]). Since $V$ is compact, $-u$ must be constant on $V$. However, it is not possible because the Kähler form on $X$ is induced by $-2 i \partial \bar{\partial} \log (u)$ (see [BT18, Lemma 2.1]) and if $-\log (u)$ were constant, the induced Kähler volume of $V$ would be zero. \(\square\)

\section*{5. Volume estimate of subvarieties}

In this section, we prove Theorem A, and Theorem B. We first state Hwang and To's theorem in the following way:

Theorem 5.1. ([HT02, Theorem 1.1]) Take $x \in X$ with injectivity radius $r=\operatorname{inj}_{x}(X)$. Let $B(x, r)$ be the Bergman ball of radius $r$ centered at $x$. Suppose $V$ is an $m$-dimensional subvariety of $X$ passing through $x$. Then, the following inequality holds:
$$\operatorname{vol}_{\mathrm{X}}(\mathrm{~V} \cap \mathrm{~B}(\mathrm{x}, \mathrm{r})) \geq \frac{(4 \pi)^{m}}{m!} \sinh ^{2 m}(r) \cdot \operatorname{mult}_{x}(V) .$$

Hwang and To generalized the above-mentioned theorem for a general Hermitian symmetric domain in [HT00, HT02].

In the compact case, Theorem 5.1 gives the lower bound on the induced Kähler volume of subvarieties in terms of the injectivity radius of $X$, however, in the case that $X$ is not compact, the injectivity radius of $X$ goes to zero as we get closer to the cusps. So we use the systole, the length of a shortest closed geodesic in $X$, as a geometric invariant of $X$ to uniformly bound the volumes of all subvarieties of $X$. For a compact ball quotient, the systole is twice the injectivity radius. However, for a non-compact $X$ the systole is still not zero and can be estimated by the trace of the hyperbolic elements in a representation of $\Gamma$.

Theorem 4.4 tells us that every subvariety of $X$ has a point with injectivity radius as large as $\operatorname{sys}(X) / 2$. Hence, we will get the following theorem:

Theorem 5.2. Let $V$ be an $m$-dimensional subvariety of $\bar{X}$ which is not contained in $D$. Then,
$$\operatorname{vol}_{X}(V) \geq \frac{(4 \pi)^{m}}{m!} \sinh ^{2 m}(\operatorname{sys}(X) / 2) .$$

Proof. Theorem 4.4 implies that $V \cap X_{\text {thick }} \neq \varnothing$. This means there always exists a point $x \in V$ such that $\operatorname{inj}_{x}(X) \geq \operatorname{sys}(X) / 2$. Now, Theorem 5.1 gives:
$$\operatorname{vol}_{X}(V) \geq \frac{(4 \pi)^{m}}{m!} \sinh ^{2 m}(\operatorname{sys}(X) / 2) .$$ \(\square\)

Corollary 5.3. With the same notation as Theorem 5.2, we have that
$$\left(K_{\bar{X}}+D\right)^{m} \cdot V \geq(n+1)^{m} \sinh ^{2 m}(\operatorname{sys}(X) / 2) .$$

Proof. Theorem 5.2 together with (2.8) gives:
$$\begin{aligned}
\left(K_{\bar{X}}+D\right)^{m} \cdot V & =\left(\frac{n+1}{4 \pi}\right)^{m} m!\operatorname{vol}_{X}(V)(\text { by }(2.8)) \\
& \geq(n+1)^{m} \sinh ^{2 m}(\operatorname{sys}(X) / 2) \text { (by Theorem 5.2) }
\end{aligned}$$ \(\square\)

We recall Bakker and Tsimerman's theorem which tells us that the uniform depth of cusps of $X$ bounds the intersection numbers of $K_{\bar{X}}$ with subvarieties of $\bar{X}$ which is not contained in $D$.

Theorem 5.4. ([BT18, Corollary 3.8]) Suppose $d$ is the uniform depth of cusps. Then,
$$K_{\bar{X}}+(1-\lambda) D$$
is ample for $\lambda \in(0, d(n+1) / 4 \pi)$.
Remark 5.5. There is a typo in the statement of this corollary in the paper by Bakker-Tsimerman. The correct upper bound should be $d(n+1) / 4 \pi$, as is clear from their proof and has been confirmed by the authors.

Consider the decomposition of the boundary divisor $D$ to the connected components $D=$ $\cup_{m=1}^{k} D_{m}$. Due to [Mok12], we know that each $D_{m}$ is an abelian variety with ample conormal bundle $O_{D_{m}}\left(-D_{m}\right)$.

Lemma 5.6. If $d>4 \pi$, then for $i \neq j$ the line bundle $L_{i, j}:=K_{\bar{X}}-D_{i}-D_{j}$ is big and nef.
Proof. since $d>4 \pi$, by Theorem 5.4 the divisor $K_{\bar{X}}-\sum_{m=1}^{k} D_{m}$ is ample. Writing
$$L_{i, j}=\left(K_{\bar{X}}-\sum_{m=1}^{k} D_{m}\right)+\sum_{m \neq i, j} D_{m},$$
we see that $L_{i, j}$ is the sum of an ample divisor and effective divisors, hence $L_{i, j}$ is big.
For nefness let $C \subset \bar{X}$ be any irreducible curve. We consider two separate cases:
\begin{itemize}
\item[(i)] The curve $C$ is contained in $D_{r}$ for some $r \neq i, j$ :
Since the boundary components are pairwise disjoint, for $r \neq i, j$ the restriction $\left.D_{m}\right|_{D_{r}}$ is trivial for all $m \neq r$. Adjunction gives $\left.\left(K_{\bar{X}}+D_{r}\right)\right|_{D_{r}} \cong K_{D_{r}}$. We know that each $D_{r}$ is an abelian variety, so $K_{D_{r}} \cong \mathcal{O}_{D_{r}}$. This yields that $\left(K_{\bar{X}}\right)_{\mid D_{r}} \cong \mathcal{O}_{D_{r}}\left(-D_{r}\right)$. Therefore, for $r \neq i, j$,
$$\left.L_{i, j}\right|_{D_{r}}=\left(K_{\bar{X}}-D_{i}-D_{j}\right)_{\mid D_{r}} \cong\left(K_{\bar{X}}\right)_{\mid D_{r}} \cong \mathcal{O}_{D_{r}}\left(-D_{r}\right) .$$
Since the conormal bundle $\mathcal{O}_{D_{r}}\left(-D_{r}\right)$ is ample on $D_{r}$, its degree on any curve $C \subset D_{r}$ is positive. Thus $L_{i, j} \cdot C>0$ in this case.
\item[(ii)] The curve $C$ is not contained in any boundary component $D_{m}$ except for $m=i$ or $m=j$ : Then for every $m \neq i, j$, we know that $D_{m} \cdot C \geq 0$ (intersection with an effective divisor is non-negative when the curve is not contained in that divisor), and because $K_{\bar{X}}-D$ is ample we have $\left(K_{\bar{X}}-D\right) \cdot C>0$. Hence
$$L_{i, j} \cdot C=\left(K_{\bar{X}}-D\right) \cdot C+\sum_{m \neq i, j} D_{m} \cdot C>0 .$$
\end{itemize}
In both cases $L_{i, j} \cdot C>0$ for every irreducible curve $C$, so $L_{i, j}$ is nef. \(\square\)

Now, putting together Theorem 5.2, Theorem 5.4 and what we proved for the uniform depth of cusps, Theorem 3.14, yields a lower bound for the degree of $K_{\bar{X}}$ on $V$ in terms of $\operatorname{sys}(X)$ :

Theorem 5.7. Let $V$ be an $m$-dimensional subvariety of $\bar{X}$ which is not fully contained in $D$. If $\operatorname{sys}(X) \geq 4 \ln \left(5 n+(4 \pi)^{4}\right)$, then
$$K_{\bar{X}}^{m} \cdot V>\left(\frac{n}{4 \pi}\right)^{m} \cdot e^{m \operatorname{sys}(X) / 16} .$$

Proof. We deal separately with the following two cases:
\begin{itemize}
\item[(i)] $V \cap D=\varnothing:$ In this case we have $K_{\bar{X}}^{m} \cdot V=\left(K_{\bar{X}}+D\right)^{m} \cdot V$ and from Corollary 5.3 we get that
$$\begin{aligned}
K_{\bar{X}}^{m} \cdot V & \geq(n+1)^{m} \sinh ^{2 m}(\operatorname{sys}(X) / 2) \\
& >\left(\frac{n}{4 \pi}\right)^{m} e^{m \operatorname{sys}(X)} \quad \text { (by the bound on the systole) } .
\end{aligned}$$
\item[(ii)] $V \cap D \neq \varnothing$ : Since sys $(X) \geq 4 \ln \left(5 n+(4 \pi)^{4}\right)$ ), Corollary 3.15 gives that the uniform depth of cusps is at least $4 \pi$ and it follows from Bakker-Tsimerman's theorem (Theorem 5.4) that $K_{\bar{X}}$ is ample. In particular, this implies that $K_{\bar{X} \mid D}$ is ample. On the other hand, we know that the conormal bundle $-D_{\mid D}$ is ample. Therefore, for every $i>1$, we have
$$K_{\bar{X}}^{m-i} \cdot(-D)^{i} \cdot V=-\left(K_{\bar{X} \mid D}\right)^{m-i} \cdot\left(-D_{\mid D}\right)^{i-1} \cdot V_{\mid D}<0 .$$
By Bakker-Tsimerman's theorem, Theorem 5.4, we get that
$$\left(K_{\bar{X}}-((n+1) d / 4 \pi-1) D\right)^{m} \cdot V \geq 0 .$$
Expanding this and combining with (5.5) gives:
$$\begin{aligned}
K_{\bar{X}}^{m} \cdot V & \geq((n+1) d / 4 \pi-1)^{m} \cdot-(-D)^{m} \cdot V \\
& \geq((n+1) d / 4 \pi-1)^{m}\left(\text { by ampleness of }-D_{\mid D}\right) \\
& >(n d / 4 \pi)^{m}(\text { because } d>4 \pi) \\
& \geq(n / 4 \pi)^{m} \cdot e^{m \text { sys }(X) / 16}(\text { by Corollary 3.15 }) .
\end{aligned}$$
Combining (5.4) and (5.6) gives that for all $V$ not contained in $D$ we have:
$$K_{\bar{X}}^{m} \cdot V>\left(\frac{n}{4 \pi}\right)^{m} \cdot e^{m \operatorname{sys}(X) / 16} .$$ \(\square\)
\end{itemize}

The volume of a line bundle $L$ on an $m$-dimensional projective variety $V$ is defined as the non-negative real number
$$\operatorname{vol}_{V}(L):=\limsup _{b \rightarrow \infty} \frac{h^{0}(V, b L)}{b^{m} / m!},$$
which measures the positivity of $L$ from the point of view of birational geometry. If $L$ is a nef line bundle on $V$, then $\operatorname{vol}_{V}(L)=L^{n}$. Let $V^{\prime}$ be a smooth variety birational to $V$ with a canonical bundle $K_{V^{\prime}}$. The canonical volume of the subvariety $V$ is
$$\widetilde{\mathrm{vol}_{V}}:=\underset{b \rightarrow \infty}{\limsup } \frac{h^{0}\left(V^{\prime}, b K_{V^{\prime}}\right)}{b^{m} / m!},$$
which does not depend on the choice of $V^{\prime}$.

To prove the bound on the canonical volume for a subvariety which does not intersect the boundary $D$, we will use the following lemma inspired by [Bru20a, Proposition 3.2].

We refer the reader to [GK67] for basics on different notions of curvatures and here we will use the facts that the holomorphic sectional curvature of the Bergman metric is -1 and the holomorphic bisectional curvature of this metric is bounded above by $-\frac{1}{2}$.

Lemma 5.8. Let $V$ be an $m$-dimensional subvariety of $\bar{X}$ which does not intersect with $D$. Let $\omega$ be the Kähler form induced on $V$ from the Bergman metric. Then on $V$ the following inequality holds
$$\operatorname{Ricci}_{\omega} \leq-\frac{m+1}{2} \omega,$$
where Ricci $_{\omega}$ is the Ricci curvature of $\omega$.
Proof. Since both sides of the inequality are bilinear, it is enough to check the inequality only for unit vectors. Let $x \in V$ and $v \in T_{x} V$ be a unit vector, i.e., $\omega(v, v)=1$. Take an orthonormal basis $\left(e_{1}, e_{2} \ldots, e_{m}\right)$ of $T_{x} V$ such that $e_{1}=v$. We will denote the holomorphic bisectional curvature of the Bergman metric at $u_{1}, u_{2} \in T_{x} V$ by $H\left(u_{1}, u_{2}\right)$. Since the holomorphic bisectional curvature and holomorphic sectional curvature only decrease on subvarieties, we have that $H\left(e_{i}, v\right) \leq-\frac{1}{2}$ for $i \in\{2, \ldots, m\}$ and $H\left(e_{1}, e_{1}\right) \leq-1$. Now we can write:
$$\operatorname{Ricci}_{\omega}(v, v)=\sum_{i=1}^{n} H\left(e_{i}, v\right)=H\left(e_{1}, e_{1}\right)+\sum_{i=2}^{n} H\left(e_{i}, v\right) \leq-\frac{m+1}{2} .$$ \(\square\)

Theorem 5.9. Let $V$ be an $m$-dimensional subvariety of $\bar{X}$ which is not contained in $D$. If $\operatorname{sys}(\mathrm{X}) \geq 4 \ln \left(5 n+(8 \pi)^{4}\right)$, then
$$\widetilde{\operatorname{vol}}_{V}>\left(\frac{m}{4 \pi}\right)^{m} e^{m \operatorname{sys}(X) / 16} .$$

Proof. Let $\mu: V^{\prime} \longrightarrow V$ be a desingularization such that the set-theoretic preimage of the boundary divisor $D^{\prime}$ is a normal crossing divisor. We consider two cases:
\begin{itemize}
\item[(i)] $V \cap D=\varnothing$ : Since on $V$ we have that $\operatorname{Ricci}_{\omega}=-2 \pi i \cdot c_{1}\left(K_{V}\right)$, we can apply Lemma 5.8 together with (2.8) to get that $K_{V^{\prime}}-\frac{m+1}{n+1} \mu^{*}\left(K_{\bar{X}}\right)$ is nef and in particular pseudoeffective on $V^{\prime}$. Because the volume does not decrease in a pseudo-effective direction, we get:
$$\widetilde{\operatorname{vol}_{V}}=\operatorname{vol}_{V^{\prime}}\left(K_{V^{\prime}}\right) \geq\left(\frac{m+1}{n+1}\right)^{m} \operatorname{vol}_{V^{\prime}}\left(\mu^{*}\left(K_{\bar{X}}\right)\right) .$$
Since $\operatorname{sys}(X) \geq 4 \ln \left(5 n+(4 \pi)^{4}\right)$, Corollary 3.15 implies that the uniform depth of cusps is at least $4 \pi$. Therefore, by Theorem 5.4, $K_{\bar{X}}$ is ample, and hence $\mu^{*}\left(K_{\bar{X}}\right)$ is big and nef. Now we can write:
$$\begin{aligned}
\operatorname{vol}_{V^{\prime}}\left(\mu^{*}\left(K_{\bar{X}}\right)\right)=\left(\mu^{*}\left(K_{\bar{X}}\right)\right)^{m} & =K_{\bar{X}}^{m} \cdot V \\
& \geq(n+1)^{m} \sinh ^{2 m}(\operatorname{sys}(X) / 2) \quad(\text { by }(5.4)) .
\end{aligned}$$
\end{itemize}

We can conclude the desired inequality for this case by combining this inequality with (5.8).
\begin{itemize}
\item[(ii)] $V \cap D \neq \varnothing$ : Since sys $(X) \geq 4 \ln \left(5 n+(8 \pi)^{4}\right)$ ), Corollary 3.15 gives that the uniform depth of cusps is at least $8 \pi$. By [Mem22, Theorem A] we get that twisted log-cotangent bundle $\Omega_{V^{\prime}}^{1}(\log (D))\left\langle-r D^{\prime}\right\rangle$ is big and nef for every $r \in(0, d / 4 \pi)$. Taking the determinant gives that $K_{V^{\prime}}+(1-m r) D^{\prime}$ is big and nef for every $r \in(0, d / 4 \pi)$. Since $d>4 \pi$, we can plug in $r=1 / m$ and deduce that $K_{V^{\prime}}$ is big and nef. Hence,
$$\widetilde{\operatorname{vol}}_{V}=\operatorname{vol}_{V^{\prime}}\left(K_{V^{\prime}}\right)=K_{V^{\prime}}^{m} .$$
On the other hand, we know that the bundle $-D_{\mid D^{\prime}}^{\prime}$ is big and nef. Therefore, for every $i>1$, we have
\end{itemize}
$$K_{V^{\prime}}^{m-i} \cdot\left(-D^{\prime}\right)^{i} \cdot V^{\prime}=-\left(K_{V^{\prime} \mid D}\right)^{m-i} \cdot\left(-D_{\mid D^{\prime}}^{\prime}\right)^{i-1} \cdot V_{\mid D^{\prime}} \leq 0 .$$

Let $r^{\prime}$ be a rational number between $d / 8 \pi$ and $d / 4 \pi$. Since $K_{V^{\prime}}+\left(1-m r^{\prime}\right) D^{\prime}$ is big and nef we have $\left(K_{V^{\prime}}+\left(1-m r^{\prime}\right) D^{\prime}\right)^{m} \geq 0$. Expanding this and using (5.9) gives that
$$\begin{aligned}
K_{V^{\prime}}^{m} & \geq\left(m r^{\prime}-1\right)^{m}\left(-D_{\mid D^{\prime}}^{\prime}\right)^{m} \\
& \geq\left(m r^{\prime}-1\right)^{m} \quad\left(\text { because }-D_{\mid D^{\prime}}^{\prime} \text { is big and nef }\right) \\
& >(m d / 8 \pi)^{m} \quad\left(\text { because } r^{\prime}>d / 8 \pi>1\right) \\
& \geq\left(\frac{m}{4 \pi}\right)^{m} e^{m \text { sys }(X) / 16}(\text { by Corollary } 3.15) .
\end{aligned}$$ \(\square\)

\section*{6. Effective global generation and very ampleness}

In this section, we prove Corollary D, Corollary E based on the bound we found for $\operatorname{deg}_{\bar{X}}(V)$ in Theorem 5.7. First, we analyze the problem on the boundary divisor $D$.
6.1. Base-point freeness and very ampleness on $D$. In this subsection, we prove that if the uniform depth of cusps is sufficiently large, then $2 K_{\bar{X}}$ does not have a base point on $D$, and moreover $3 K_{\bar{X}}$ can separate any two points, and any tangent direction on $D$. We first prove that the restricted bundles on the boundary satisfy these properties. Consider the decomposition of the boundary divisor $D$ to the connected components $D=\cup_{i=1}^{k} D_{i}$. Due to [Mok12], we know that each $D_{i}$ is an abelian variety with ample conormal bundle $O_{D_{i}}\left(-D_{i}\right)$.

Lemma 6.1. The line bundle $2 K_{\bar{X} \mid D_{i}}$ is base-point free and $3 K_{\bar{X} \mid D_{i}}$ is very ample for every $i$.

Proof. The adjunction formula gives that $K_{\bar{X} \mid D_{i}} \cong-D_{i \mid D_{i}}$. As the conormal bundle is ample and $D_{i}$ is an abelian variety, $-2 D_{i \mid D_{i}}$ is base-point free and $-3 D_{i \mid D_{i}}$ is very ample (see [Ohb87]). \(\square\)

In the next two lemmas, we see how we can lift the sections from the restricted bundle to $\bar{X}$. The base locus of a line bundle $L$ on $\bar{X}$ will be denoted by $\operatorname{Bs}(L)$.

Lemma 6.2. Suppose that the uniform depth of cusps is larger than $4 \pi$, Then, the following hold:
\begin{itemize}
\item[(i)] $\operatorname{Bs}\left(2 K_{\bar{X}}\right) \cap D=\varnothing$
\end{itemize}
\begin{itemize}
\item[(ii)] For any two points on different components of $D$, there exists a global section of $2 K_{\bar{X}}$ which separates them.
\end{itemize}

Proof. Let $L$ be $2 K_{\bar{X}}$.
\begin{itemize}
\item[(i)] By Lemma 6.1, $L_{\mid D}$ is base-point free and therefore it is enough to show that we can lift the global sections from $D$ to $\bar{X}$, that is, $H^{0}(\bar{X}, L) \longrightarrow H^{0}\left(D, L_{\mid D}\right)$ is surjective. Consider the following exact sequence on $\bar{X}$ :
$$0 \longrightarrow L-D \longrightarrow L \longrightarrow L_{\mid D} \longrightarrow 0 .$$
Writing the long exact sequence we can see that it is sufficient to show $H^{1}(\bar{X}, L-D)=$ 0 . As $L-D=K_{\bar{X}}+\left(K_{\bar{X}}-D\right)$, if the uniform depth is sufficiently large, then by Theorem $5.4 K_{\bar{X}}-D$ is ample. Therefore, the vanishing of $H^{1}(\bar{X}, L-D)$ follows from Kodaira's vanishing theorem.
\item[(ii)] Suppose that we want to separate $x \in D_{i}$ and $y \in D_{j}$ with $i \neq j$. It is sufficient to find a global section of $L_{i}:=L-D_{i}$ which does not vanish at $y$. We can argue similar to the first part. Concretely, since $D_{i}$ and $D_{j}$ are disjoint, the line bundle $L_{i \mid D_{j}}$ is isomorphic to the line bundle $L_{\mid D_{j}}$, which we know is base-point free by Lemma 6.1. Therefore, it is enough to show that we can lift the global sections on $D_{j}$ to $\bar{X}$, that is, $H^{0}\left(\bar{X}, L_{i}\right) \longrightarrow H^{0}\left(D, L_{i \mid D_{j}}\right)$ is surjective. Consider the exact sequence
$$0 \longrightarrow L_{i}-D_{j} \longrightarrow L_{i} \longrightarrow L_{i \mid D_{j}} \longrightarrow 0 .$$
Writing the long exact sequence we can see that it is sufficient to show $H^{1}\left(\bar{X}, L_{i}-\right.$ $\left.D_{j}\right)=0$. By Lemma 5.6, we get that $K_{\bar{X}}-D_{i}-D_{j}$ is big and nef. Since $L_{i}-$ $D_{j}=K_{\bar{X}}+\left(K_{\bar{X}}-D_{i}-D_{j}\right)$, the Kawamata-Viehweg vanishing theorem implies that $H^{1}\left(\bar{X}, L_{i}-D_{j}\right)=0$. \(\square\)
\end{itemize}

Lemma 6.3. If the uniform depth of cusps is larger than $2 \pi$, then $3 K_{\bar{X}}$ can separate any two points on a connected component of $D$, and at each point of $D$ it can separate any two tangent directions.

Proof. By Lemma 6.2 and Lemma 6.1, it is enough to show that we can lift the sections from the boundary, i.e.,
$$H^{0}\left(\bar{X}, 3 K_{\bar{X}}\right) \longrightarrow H^{0}\left(D, 3 K_{\bar{X} \mid D}\right) \longrightarrow 0 .$$
Hence, it is enough to show that $H^{1}\left(\bar{X}, 3 K_{\bar{X}}-D\right)=0$. Since $d>2 \pi$, it follows from Theorem 5.4 that $2 K_{\bar{X}}-D$ is ample. Therefore, by Kodaira's vanishing theorem we get that $H^{1}\left(\bar{X}, 3 K_{\bar{X}}-D\right)=0$. \(\square\)
6.2. Global generation and very ampleness on $\bar{X}$. In this subsection, we see how we can conclude effective global generation and effective very ampleness results by using Theorem 5.7. We first recall the famous theorem of Angehrn and Siu on pointwise base-point freeness:

Theorem 6.4. [AS95, Theorem 0.1] Let $Y$ be a smooth projective variety of dimension $n$, and let $L$ be an ample line bundle on $Y$. Fix a point $y \in Y$, and assume that
$$L^{m} \cdot V>\left(\frac{n(n+1)}{2}\right)^{m}$$
for every subvariety $V$ of dimension $m$ passing through $y$. Then, $K_{Y}+L$ has a section that does not vanish at $y$.

Combining Angehrn and Siu's result with our Theorem 5.7 gives that if $\operatorname{sys}(X)$ is sufficiently large relative to $n$, then $2 K_{\bar{X}}$ is globally generated:

Theorem 6.5. If $\operatorname{sys}(\mathrm{X}) \geq 20 \ln \left(5 n+(4 \pi)^{4}\right)$, then $2 K_{\bar{X}}$ is globally generated.
Proof. Using Corollary 3.15 we get that $d>4 \pi$. Therefore, by Lemma 6.2, $2 K_{\bar{X}}$ does not have any base point on $D$. On the other hand, Theorem 5.7 implies that for every $m$-dimensional subvariety $V \subset \bar{X}$ which is not contained in $D$, we have
$$\begin{aligned}
K_{\bar{X}}^{m} \cdot V & \geq\left(\frac{n}{4 \pi}\right)^{m} \cdot e^{m \operatorname{sys}(X) / 16} \\
& \geq n^{m}\left(5 n+(4 \pi)^{4}\right)^{m}(\text { by the bound on sys }(X)) \\
& >\left(\frac{n(n+1)}{2}\right)^{m} .
\end{aligned}$$
Therefore, Theorem 6.4 implies that for every point $x \in \bar{X} \backslash D$, there is a section of $2 K_{\bar{X}}$ which does not vanish at $x$. Hence, $2 K_{\bar{X}}$ is globally generated. \(\square\)

Now, we prove a proposition which will be used to show that $2 K_{\bar{X}}$ can separate any point in $X$ from any point in $D$ :

Proposition 6.6. If $\operatorname{sys}(\mathrm{X}) \geq 20 \ln \left(5 n+(8 \pi)^{4}\right)$, then for every $x \in X$ there exists $s \in$ $H^{0}\left(\bar{X}, 2 K_{\bar{X}}-D\right)$ such that $s$ does not vanish at $x$.

Proof. Since sys $(\mathrm{X}) \geq 20 \ln \left(5 n+(8 \pi)^{4}\right)$, the uniform depth of cusps is larger than $4 \pi$ (see Corollary 3.15) and therefore by Bakker-Tsimerman's result,Theorem 5.4, it follows that $K_{\bar{X}}+(1-\lambda) D$ is ample for $\lambda \in\left(0, \frac{(n+1) d}{4 \pi}\right)$. On the other hand, as $K_{\bar{X} \mid D} \cong-D_{D}$ and $-D_{\mid D}$ is ample, for every subvariety $V$ of dimension $m$ and every $1 \leq i \leq m$ we have
$$\begin{aligned}
\left(K_{\bar{X}}-2 D\right)^{m-i}(-D)^{i} \cdot V_{\mid D} & =-\left(K_{\bar{X}}-2 D\right)_{\mid D}^{i}\left(-D_{\mid D}\right)^{j-1} \cdot V \\
& =-3^{i}\left(-D_{\mid D}\right)^{n-1} \cdot V_{\mid D} \\
& \leq 0 .
\end{aligned}$$
Expanding $\left(K_{\bar{X}}-\left(1-\frac{(n+1) d}{4 \pi}\right) D\right)^{m} \cdot V \geq 0$ and using (6.2) we get:
$$\begin{aligned}
\left(K_{\bar{X}}-2 D\right)^{m} \cdot V & \geq\left(\frac{(n+1) d}{4 \pi}+1\right)^{m}\left(-D_{\mid D}\right)^{m-1} \cdot V_{\mid D} \\
& \geq\left(\frac{(n+1) d}{4 \pi}\right)^{m}\left(\text { by the ampleness of }-D_{\mid D}\right) \\
& \geq\left(\frac{n+1}{4 \pi}\right)^{m} \cdot e^{m \operatorname{sys}(X) / 16} \quad(\text { by Corollary } 3.15) \\
& >(n+1)^{m} n^{m} \quad(\text { by the bound on sys }(X))
\end{aligned}$$
Hence, Theorem 6.4 gives that $2 K_{\bar{X}}-D$ has a global section which does not vanish at $x$. \(\square\)

We recall the result of Ein-Lazarsfeld-Nakamaye on the pointwise separation of jets:

Theorem 6.7. ([ELN96, Theorem 4.4]) Let $Y$ be a smooth projective variety of dimension $n$ and let $L$ be an ample line bundle on $Y$ satisfying $L^{n}>(n+s)^{n}$. Let $b$ be a non-negative number such that $K_{Y}+b L$ is nef. Suppose that $m_{0}$ is a positive integer such that $m_{0} L$ is free. Then, for any point $y \in Y$ either
\begin{itemize}
\item[(a)] $K_{Y}+L$ separates $s$-jets at $y$, or
\item[(b)] there exists a dimension $m$ subvariety $V$ containing $y$ and satisfying
$$\operatorname{deg}_{L}(V) \leq\left(b+m_{0} \cdot m+\frac{n!}{(n-m)!}\right)^{n-m}(n+s)^{n}$$
\end{itemize}

Definition 6.8. Let $Y$ be a smooth projective variety and let $L$ be a nef line bundle on $Y$. Fix a point $y \in Y$. The Seshadri constant of $L$ at $y$ is the real number
$$\epsilon(L, y)=\inf \frac{L \cdot C}{\operatorname{mult}_{y}(C)},$$
where the infimum is taken over all irreducible curves $C$ passing through $y$.
Plugging in Theorem 5.7 and Theorem 6.5 to the result of Ein-Lazarsfeld-Nakamaye allows us to separates $s$-jets of $2 K_{\bar{X}}$ on $X$ if $\operatorname{sys}(X)$ is sufficiently large with respect to $n$ and $s$ :

Theorem 6.9. Let $s$ be a positive integer. Suppose that
$$\operatorname{sys}(X) \geq 20 \max \left\{n \ln ((1+2 n+n!)(n+s)), \ln \left(5 n+(8 \pi)^{4}\right)\right\} .$$
Then for every $x \in X$, the line bundle $2 K_{\bar{X}}$ separates $s$-jets at $x$. In particular, for every $x$ we have $\epsilon\left(K_{\bar{X}}, x\right) \geq s / 2$.

Proof. Since sys $(X)>20 \ln \left(5 n+(8 \pi)^{4}\right)$, Theorem 6.5 implies that $2 K_{\bar{X}}$ is globally generated. Also, as $\operatorname{sys}(X) \geq 20 \ln (n+s)$, Theorem 5.7 implies that
$$K_{\bar{X}}^{n}>(n+s)^{n} .$$
Note that substituting the lower bounds on $\operatorname{sys}(X)$ from Theorem 5.7 shows that for a subvariety $V$ of dimension $m$ not contained in $D$, the following inequality holds:
$$K_{\bar{X}}^{m} \cdot V \geq n^{m}(1+2 n+n!)^{n}(n+s)^{n} \geq\left(b+2 m+\frac{n!}{(n-m)!}\right)^{n-m}(n+s)^{n} .$$
Now, applying Theorem 6.7 to $L=K_{\bar{X}}, m_{0}=2$ and $b=1$ gives that $2 K_{\bar{X}}$ separates $s$-jets at every $x \in X$.

Combining the separation of jets with $\left[\mathrm{BRH}^{+} 09\right.$, Proposition 2.2.5 ] gives that $\epsilon\left(2 K_{\bar{X}}, x\right) \geq$ $s$. Since $\epsilon\left(2 K_{\bar{X}}, x\right)=2 \epsilon\left(K_{\bar{X}}, x\right)$, we get the desired inequality. \(\square\)

We recall a result of Kollar which tells us that a line bundle can separate two points if the degree of every subvariety passing through either of the points with respect to the line bundle is sufficiently large relative to the dimension of the ambient space:

Theorem 6.10. ([Kol97, Theorem 5.9]) Let $L$ be a nef and big divisor on a smooth projective variety $Y$. Let $x_{1}, x_{2}$ be closed points and assume that there are positive numbers $c(k)$ with the following properties:
\begin{itemize}
\item[(i)] If $V \subset Y$ is an irreducible $m$-dimensional subvariety which contains $x_{1}$ or $x_{2}$ then
$$L^{m} \cdot V>c(m)^{m} .$$
\end{itemize}
\begin{itemize}
\item[(ii)] The numbers $c(k)$ satisfy the inequality
$$\sum_{k=1}^{\operatorname{dim}(x)} \sqrt[k]{2} \frac{k}{c(k)} \leq 1 .$$
\end{itemize}
Then, $K_{Y}+L$ separates $x_{1}$ and $x_{2}$.
Definition 6.11. ([Tak93]) Let $L$ be a line bundle on a smooth projective variety $Y$ and let $D$ be a divisor on $Y$. The line bundle $L$ is said to be very ample modulo $D$ if the rational map $\Phi_{L}: Y \rightarrow \mathbb{P}\left(H^{0}\left(Y, O_{Y}(L)\right)\right.$ is an embedding of $Y \backslash D$.

Note that Theorem 6.5 says that the rational map $\Phi_{2 K_{\bar{X}}}: Y \rightarrow \mathbb{P}\left(H^{0}\left(Y, O_{Y}\left(2 K_{\bar{X}}\right)\right)\right.$ is globally defined map on $Y$. Moreover, the following theorem gives that this map is in particular injective on $X$ and can separate any two tangent directions at whole $\bar{X}$ :

Theorem 6.12. Suppose that
$$\operatorname{sys}(X) \geq 20 \max \left\{n \ln ((1+2 n+n!)(n+1)), \ln \left(5 n+(8 \pi)^{4}\right)\right\} .$$
Then the map $\Phi_{2 K_{\bar{X}}}: \bar{X} \rightarrow \mathbb{P}\left(H^{0}\left(\bar{X}, 2 K_{\bar{X}}\right)\right)$ satisfies the following properties:
\begin{itemize}
\item[(i)] If $\phi_{2 K_{\bar{X}}}\left(x_{1}\right)=\phi_{2 K_{\bar{X}}}\left(x_{2}\right)$ for some $x_{1}, x_{2} \in \bar{X}$, then $x_{1}, x_{2} \in D_{i}$, where $D_{i}$ is some connected component of $D$.
\item[(ii)] $\Phi_{2 K_{\bar{X}}}$ separates tangent directions at every $x \in X$.
\end{itemize}

Proof. Separation of points: Note that by Lemma 6.2 if $\phi_{2 K_{\bar{X}}}\left(x_{1}\right)=\phi_{2 K_{\bar{X}}}\left(x_{2}\right)$ and $x_{1}, x_{2} \in D$, then they both lie on the same component of $D$. Hence, we only need to deal with the following two cases:
\begin{itemize}
\item[(i)] $x_{1}, x_{2} \in X$ : Let $V \subset \bar{X}$ be a subvariety of dimension $m$ which passes through either $x_{1}$ or $x_{2}$. Fix $c=n e^{\operatorname{sys}(X) / 20}$. By Theorem 5.7 we have that
$$K_{\bar{X}}^{m} \cdot V \geq c^{m} .$$
Therefore, by Kollar's Theorem, Theorem 6.10, we can separate any two points $x_{1}, x_{2} \in X$.
\item[(ii)] $x_{1} \in X, x_{2} \in D$ : By Proposition 6.6, there is a section $s \in H^{0}\left(\bar{X}, 2 K_{\bar{X}}-D\right)$ which does not vanish at $x_{1}$. Therefore, as $2 K_{\bar{X}}-D$ is a subbundle of $2 K_{\bar{X}}$, we get a section of $2 K_{\bar{X}}$ which does not vanish at $x_{1}$, but vanishes on $D$ and in particular at $x_{2}$.
\end{itemize}

Separation of tangent directions: For $x \in X$, the separation of tangent direction follows from Theorem 6.9 when $s=1$. \(\square\)

In particular, Theorem 6.12 implies that $2 K_{\bar{X}}$ is very ample modulo $D$.
Theorem 6.13. With the same assumption on $\operatorname{sys}(X)$ as Theorem 6.12, $3 K_{\bar{X}}$ is very ample.
Proof. By Theorem 6.12, it follows that we only need to show that $3 K_{\bar{X}}$ can separate any two points and any tangent direction on any connected component of $D$, which follows from Lemma 6.3. \(\square\)

Putting all of these together, we get the following:

Corollary 6.14. Suppose that
$$\operatorname{sys}(X) \geq 20 \max \left\{n \ln ((1+2 n+n!)(n+1)), \ln \left(5 n+(8 \pi)^{4}\right)\right\} .$$
Then, the following hold
\begin{itemize}
\item[(i)] $2 K_{\bar{X}}$ is globally generated and very ample modulo $D$.
\item[(ii)] $3 K_{\bar{X}}$ is very ample.
\end{itemize}

Proof. The global generation of $2 K_{\bar{X}}$ follows from Theorem 6.5. The very ampleness modulo $D$ follows from Theorem 6.12. The very ampleness of $3 K_{\bar{X}}$ follows from Theorem 6.13. \(\square\)

\section*{7. Seshadri Constant}

The goal of this section is to study the relation between the Seshadri constants and the systole of $X$ and in particular we prove Corollary F in this section.

In addition to the result of Theorem 6.9 on the Seshadri constant $\epsilon\left(2 K_{\bar{X}}, x\right)$ for $x \in X$, we obtain the following result, which holds under a smaller bound on $\operatorname{sys}(X)$ :

Corollary 7.1. Suppose that $\operatorname{sys}(X) \geq 20 \ln \left(5 n+(8 \pi)^{4}\right)$. Let
$$E:=\left\{x \in X \mid \epsilon\left(K_{\bar{X}}, x\right)<e^{\operatorname{sys}(X) / 20}\right\} .$$
Then, $E$ satisfies the following properties:
\begin{itemize}
\item[(i)] $E \cap X_{\text {thick }}=\varnothing$.
\item[(ii)] $E$ does not contain any positive-dimensional subvariety.
\item[(iii)] $E$ is contained in a Zariski closed proper subset of $X$.
\end{itemize}

Proof. (i) Fix $x \in X_{\text {thick }}$. Let $C \subset \bar{X}$ be a curve passing through $x$. Since $x \in X_{\text {thick }}$ we have $\operatorname{inj}_{x}(X) \geq \operatorname{sys}(X) / 2$. On the other hand, since $\operatorname{sys}(X) \geq 20 \ln \left(5 n+(8 \pi)^{4}\right)$, Corollary 3.15 gives that $d>8 \pi$, therefore by Theorem $5.4 K_{\bar{X}}-D$ is ample. We can write:
$$\begin{aligned}
2 K_{\bar{X}} \cdot C & \geq\left(K_{\bar{X}}+D\right) \cdot C\left(\text { by ampleness of } K_{\bar{X}}-D\right) \\
& \geq \frac{n+1}{4 \pi} \operatorname{vol}_{X}(C)(\text { by }(2.8)) \\
& \geq(n+1) \sinh ^{2}(\operatorname{sys}(X) / 2) \cdot \operatorname{mult}_{x}(C) \text { (by Theorem 5.1). }
\end{aligned}$$
Therefore,
$$\epsilon\left(x, K_{\bar{X}}\right) \geq \frac{n+1}{2} \sinh ^{2}(\operatorname{sys}(X) / 2)>e^{\operatorname{sys}(X) / 20},$$
and this gives the first property.
\begin{itemize}
\item[(ii)] Combining (i) with Theorem 4.4 we conclude that $E$ does not have any positive-dimensional subvariety.
\item[(iii)] Note that Theorem 5.7 implies that for every $m$-dimensional subvariety $V \not \subset D$, we have
$$\left(K_{\bar{X}}^{m} \cdot V\right)^{\frac{1}{m}} \geq \frac{n+1}{4 \pi} e^{\operatorname{sys}(X) / 16} .$$
Putting this in [EKL95, Theorem 3.1] gives
\end{itemize}
$$\epsilon\left(K_{\bar{X}}, x\right) \geq \frac{1}{4 \pi} e^{\operatorname{sys}(X) / 16}>e^{\operatorname{sys}(X) / 20} .$$
for all $x \in \bar{X}$ off the union of countably many proper subvarieties of $\bar{X}$. On the other hand as $K_{\bar{X}}$ is ample by using [EKL95, Lemma 1.4] we can conclude that inequality (7.1) holds on Zarisiky open set, i.e, $E$ is contained in a proper subvariety of $\bar{X}$. \(\square\)

Consider the decomposition of the boundary divisor $D$ to the connected components $D=$ $\sqcup_{i=1}^{k} D_{i}$. Due to [Mok12], we know that each $D_{i}$ is an abelian variety with ample conormal bundle $O_{D_{i}}\left(-D_{i}\right)$. The adjunction formula gives that $K_{\bar{X} \mid D_{i}}$ is isomorphic to the conormal bundle $O_{D_{i}}\left(-D_{i}\right)$. Suppose that $D_{i}=\Lambda_{i} \backslash W_{i}$, where $W_{i} \cong \mathbb{C}^{n-1}$ is a complex vector space of dimension $n-1$, and $\Lambda_{i} \cong \mathbb{Z}^{n-1}$ is a lattice in $W_{i}$. It is classical that every ample line bundle on $D_{i}$ determines a positive definite Hermitian form on $W_{i}$. Suppose $H_{i}$ is the positive definite Hermitian form determined by $K_{\bar{X} \mid D_{i}}$ on $W_{i}$. The real part $B_{i}=\operatorname{Re}\left(H_{i}\right)$ defines a Euclidean inner product on $W_{i}$ (see [Laz17, sec 5.3.A] for more details). Let $l_{i}$ be the length of a shortest vector of $\Lambda_{i}$ with respect to $B_{i}$. We define the systole of the boundary as
$$\operatorname{sys}(D):=\min _{i=1}^{k} l_{i} .$$

The following lemma gives a lower bound for the Seshadri constant of $K_{\bar{X} \mid D}$ in terms of the systole of the boundary:

Lemma 7.2. Let $x$ be a point on a connected component of the boundary, $D_{i}$. Then,
$$\epsilon\left(K_{\bar{X} \mid D_{i}}, x\right) \geq \frac{\pi}{4} \cdot \operatorname{sys}(D)^{2} .$$

Proof. This follows from [Laz17, Theorem 5.3.6]. \(\square\)

Combining this lemma with the previous results gives that if the systole of $\bar{X}$ and $\operatorname{sys}(D)$ are sufficiently large, then the Seshadri constant $\epsilon\left(K_{\bar{X}}, x\right)$ is large and in particular $2 K_{\bar{X}}$ is very ample:

Corollary 7.3. Suppose that $\operatorname{sys}(D)>2 \sqrt{2 n / \pi}$ and that
$$\operatorname{sys}(X) \geq 20 \max \left\{n \ln (5 n(1+2 n+n!)), \ln \left(5 n+(8 \pi)^{4}\right)\right\} .$$
Then, for every $x \in \bar{X}$ we have $\epsilon\left(K_{\bar{X}}, x\right) \geq 2 n$, and in particular $2 K_{\bar{X}}$ is very ample.
Proof. Let $C \subset \bar{X}$ be a connected curve passing through a point $x \in \bar{X}$. We consider three cases:
\begin{itemize}
\item[(i)] $x \in D$ and $C$ fully contained in a $D$ : Let $D_{i}$ be the connected component of $D$ which contains $x$. Lemma 7.2 implies that
$$K_{\bar{X}} \cdot C=K_{\bar{X} \mid D_{i}} \cdot C \geq \frac{\pi}{4} \operatorname{sys}(D)^{2} \cdot \operatorname{mult}_{x}(C) \geq 2 n \cdot \operatorname{mult}_{x}(C) .$$
\item[(ii)] $x \in D$ and $C$ is not contained in $D$ : Plugging in the bound on the systole in Theorem 3.14 gives that the uniform depth of cusps $d$ is at least $8 \pi$. By the theorem of Bakker-Tsimerman, Theorem 5.4, the line bundle $K_{\bar{X}}+(1-\lambda) D$ is ample for $\lambda \in(0,(n+1) d / 4 \pi)$. Hence, we can write
$$K_{\bar{X}} \cdot C \geq\left(\frac{(n+1) d}{4 \pi}-1\right) D \cdot C \geq \frac{n d}{4 \pi} \operatorname{mult}_{x}(C) \geq 2 n \operatorname{mult}_{x}(C),$$
because $d \geq 8 \pi$ by Corollary 3.15.
\end{itemize}
\begin{itemize}
\item[(iii)] $x \in X$ : For this case we will use Theorem 6.9. Plugging in $s=2 n$ to this theorem gives $K_{\bar{X}} \cdot C \geq 2 n \cdot \operatorname{mult}_{x}(C)$. Hence, for every $x \in X$ we get that $\epsilon\left(K_{\bar{X}}, x\right) \geq 2 n$. Combining this with Demailly's theorem [Dem92, Proposition 6.8).] implies that $2 K_{\bar{X}}$ is very ample.
\end{itemize} \(\square\)

\section*{8. Sparsity of Rational Points}

The goal of this section is to prove Corollary C. The proof is based on Theorem A, Theorem B, and the fundamental idea of Bombieri-Pila, known as the determinant method. Let $F$ be a number field with ring of integers $\mathcal{O}_{F}$ and set of places $M_{F}$. For each place $v \in M_{F}$ let $|\cdot|_{v}$ denote the standard normalized absolute value on $F_{v}$, so that the product formula
$$\prod_{v \in M_{F}}|a|_{v}=1, \quad \text { for all } a \in F^{\times},$$
holds. Concretely:
\begin{itemize}
\item[-] If $v$ is non-archimedean corresponding to a prime ideal $\mathfrak{p} \subset \mathcal{O}_{F}$, set
$$|a|_{v}:=N(\mathfrak{p})^{-\operatorname{ord}_{\mathfrak{p}}(a)}, \quad a \in F^{\times},$$
where $N(\mathfrak{p})=\left|\mathcal{O}_{F} / \mathfrak{p}\right|$ is the absolute norm of $\mathfrak{p}$.
\item[-] If $v$ is archimedean, arising from an embedding $\sigma: F \hookrightarrow \mathbb{R}$ or $\sigma: F \hookrightarrow \mathbb{C}$, set
$$|a|_{v}:=|\sigma(a)|, \quad a \in F^{\times} .$$
In the complex case, we include both $\sigma$ and its conjugate $\bar{\sigma}$ as distinct places.
\end{itemize}

The multiplicative projective height of a point $x=\left[x_{0}: \cdots: x_{N}\right] \in \mathbb{P}_{F}^{N}$ is defined as
$$\mathrm{H}(x)=\prod_{v \in M_{F}} \max _{0 \leq i \leq N}\left|x_{i}\right|_{v} .$$
The product formula ensures that this definition is independent of the choice of homogeneous coordinates, that is, scaling the representative vector $\left(x_{0}, \ldots, x_{N}\right)$ by any $\lambda \in F^{\times}$leaves the height unchanged.

We will use the following recent result of Maculan-Brunebarbe [BM22], obtained by applying the determinant method inductively:

Theorem 8.1. ([BM22, Theorem 4.4]) Let $Z$ be a closed subvariety of $\mathbb{P}_{F}^{N}$, let $\epsilon>0$ be a real number, let $n \geq 0$ and $e \geq 1$ be integers.

Then, there is a real number $C=c(n, e, N, F, D, \epsilon)$ with the following property: For an integral $n$-dimensional closed subvariety $Y$ of $\mathbb{P}^{N}$ of degree $\leq e$ such that each positive-dimensional integral closed subvariety in $Y$ not contained in $Z$ has degree $\geq d^{\operatorname{dim}(Y)}$ for some integer $d \geq 1$, and a real number $B>[F: \mathbb{Q}] \epsilon$, the following inequality holds:
$$\#\{x \in Y(F) \backslash Z \mid \mathrm{H}(x) \leq B\} \leq C B^{(1+\epsilon)[F: \mathbb{Q}] n(n+3) / d} .$$

Remark 8.2. There is a typo in the statement of Theorem 8.1 in the original paper. However, from its applications and the surrounding statements in that paper, it is clear that the power of $d$ should be the dimension of the subvariety $Y$, not $Z$.

On $\mathbb{P}_{F}^{N}$ we fix the standard adelic metric on $\mathcal{O}_{\mathbb{P}^{N}}(1)$, defined as follows: for a local section $s$ given by a homogeneous linear polynomial and a point $x=\left[x_{0}: \cdots: x_{N}\right] \in \mathbb{P}_{F}^{N}$,
$$\|s(x)\|_{v}=\frac{|s(x)|_{v}}{\max _{0 \leq i \leq N}\left|x_{i}\right|_{v}}, \quad v \in M_{F} .$$

Let $\bar{Y}$ be a smooth projective variety over $F$, and let $L$ be a line bundle on $\bar{Y}$. Suppose there exists $b \geq 1$ such that the complete linear system $|b L|$ is base-point free. Choosing a basis of $H^{0}(\bar{Y}, b L)$ defines the morphism
$$\varphi_{|b L|}: \bar{Y} \longrightarrow \mathbb{P}_{F}^{N} .$$
Pulling back the adelic metric on $\mathcal{O}_{\mathbb{P}^{N}}(1)$ gives a metric on $b L$, and we obtain a metric on $L$ by taking the $b$-th root fiberwise: for a local section $t$ of $L$ and a point $x \in \bar{Y}$,
$$\|t(x)\|_{L, v}:=\left(\left\|t^{\otimes b}(x)\right\|_{\varphi_{|b L|}^{*}(\mathcal{O}(1)), v}\right)^{1 / b} .$$
The multiplicative height on $\bar{Y}(F)$ is
$$\mathrm{H}_{L}(x)=\prod_{v \in M_{F}}\|t(x)\|_{L, v}^{-1} .$$

\section*{Remark 8.3.}
\begin{itemize}
\item[(i)] Independence from the choice of local section. Let $x \in \bar{Y}(F)$ and let $s, t$ be two local sections of $L$ defined in a neighborhood of $x$ with $s(x), t(x) \neq 0$. Since $L$ has rank 1, there exists a rational function $f \in F(\bar{Y})^{\times}$defined near $x$ such that $t=f \cdot s$. For each place $v$ we have that
$$\|t(x)\|_{L, v}=\|f(x) \cdot s(x)\|_{L, v}=|f(x)|_{v}\|s(x)\|_{L, v} .$$
Therefore,
$$\prod_{v \in M_{F}}\|t(x)\|_{L, v}^{-1}=\left(\prod_{v \in M_{F}}|f(x)|_{v}^{-1}\right)\left(\prod_{v \in M_{F}}\|s(x)\|_{L, v}^{-1}\right) .$$
Since $f(x) \in F^{\times}$, the product formula gives $\prod_{v \in M_{F}}|f(x)|_{v}=1$, hence
$$\prod_{v \in M_{F}}\|t(x)\|_{L, v}^{-1}=\prod_{v \in M_{F}}\|s(x)\|_{L, v}^{-1} .$$
Thus $\mathrm{H}_{L}(x)(x)$ is independent of the chosen local section.
\item[(ii)] Recovery of the usual height on $\mathcal{O}_{\mathbb{P}_{F}^{N}}(1)$. Let $\bar{Y}=\mathbb{P}_{F}^{N}$ and $L=\mathcal{O}_{\mathbb{P}^{N}}(1)$. For $x=\left[x_{0}: \cdots: x_{N}\right] \in \mathbb{P}_{F}^{N}$, choose an index $j$ with $x_{j} \neq 0$ and take the section $s=X_{j}$ (the $j$-th coordinate function), which does not vanish at $x$. By definition of the metric at every place $v$,
$$\|s(x)\|_{v}=\frac{\left|X_{j}(x)\right|_{v}}{\max _{i}\left|x_{i}\right|_{v}}=\frac{\left|x_{j}\right|_{v}}{\max _{i}\left|x_{i}\right|_{v}} .$$
Hence
$$\mathrm{H}_{L}(x)=\prod_{v \in M_{F}}\|s(x)\|_{v}^{-1}=\prod_{v \in M_{F}} \frac{\max _{i}\left|x_{i}\right|_{v}}{\left|x_{j}\right|_{v}}=\left(\prod_{v \in M_{F}} \max _{i}\left|x_{i}\right|_{v}\right) \cdot\left(\prod_{v \in M_{F}}\left|x_{j}\right|_{v}^{-1}\right) .$$
\end{itemize}
\begin{itemize}
\item[] By the product formula $\prod_{v}\left|x_{j}\right|_{v}=1$, so
$$\mathrm{H}_{L}(x)=\prod_{v \in M_{F}} \max _{0 \leq i \leq N}\left|x_{i}\right|_{v},$$
which is exactly the classical multiplicative projective height (8.1).
\item[(iii)] Tensor powers. If $a \geq 1$, then the induced metric on $a L$ is obtained by taking the $a$-th power of the norm, so for every $x \in \bar{Y}(F)$,
$$\left\|t^{\otimes a}(x)\right\|_{a L, v}=\|t(x)\|_{L, v}^{a},$$
for every local section $t$ of $L$. Therefore
$$\mathrm{H}_{a L}(x)=\mathrm{H}_{L}(x)^{a} .$$
\end{itemize}

Now, combining our effective estimates (Corollary 5.3 and Theorem 5.7) on the degree of the subvarieties with Theorem 8.1 we can conclude the following:

Corollary 8.4. Suppose $\bar{X}$ is defined on the number field $F$. Let $\epsilon$ be a positive number and $B$ any number such that $B \geq \epsilon[F: \mathbb{Q}]$.
\begin{itemize}
\item[(i)] Let $L_{1}=K_{\bar{X}}+D$. Then, there exists a constant $c_{1}$ depending on $X, F$ and $\epsilon$ such that:
$$\#\left\{x \in X(F) \mid \mathrm{H}_{L_{1}}(x) \leq B\right\} \leq c_{1} B^{\delta},$$
where
$$\delta=\frac{[F: \mathbb{Q}] n(n+3)}{\sinh ^{2}(\operatorname{sys}(X) / 2)(n+1)}(1+\epsilon),$$
and $H_{L_{1}}$ is the multiplicative height.
\item[(ii)] Let $L_{2}=K_{\bar{X}}$ and assume that $\operatorname{sys}(X) \geq 4 \ln \left(5 n+(4 \pi)^{4}\right)$. Then, there exists a constant $c_{2}$ depending on $X, F$ and $\epsilon$ such that
$$\#\left\{x \in X(F) \mid \mathrm{H}_{L_{2}}(x) \leq B\right\} \leq c_{2} B^{\delta},$$
where
$$\delta=\frac{4 \pi[F: \mathbb{Q}](n+3)}{e^{\operatorname{sys}(X) / 16}}(1+\epsilon),$$
and $H_{L_{2}}$ is the multiplicative height.
\end{itemize}

Proof. (i) By the main Theorem of [Mok12], there exists $b$ such that $b L_{1}$ is base-point free on $\bar{X}$ and it embeds $X$ into some projective space $\mathbb{P}^{N}$ such that each connected component of $D$ collapses to an isolated point. Let $Z$ be the union of these isolated points in $\mathbb{P}^{N}$. Applying Corollary 5.3 implies that for every subvariety $V$ of $\bar{X}$ not contained in $D$ one has:
$$\left(\left(b L_{1}\right)^{m} \cdot V\right)^{1 / m} \geq b(n+1) \sinh ^{2}(\operatorname{sys}(X) / 2),$$
where $m$ is the dimension of $V$. Hence, applying Theorem 8.1 gives us that:
$$\#\left\{x \in X(F) \mid \mathrm{H}_{b L_{1}}(x) \leq B\right\} \leq C B^{[F: \mathbb{Q}] n(n+3)(1+\epsilon) /(n+1) s},$$
where $s=\sinh ^{2}(\operatorname{sys}(X) / 2)$ and $C$ is constant depending on $X, F$ and $\epsilon$ (Note that $N, n$ and $e$ are fixed when we fixed $\bar{X}$ and $b L_{1}$. Also, the toroidal compactification is unique for a ball quotient, therefore all of these data only depend on $X$ ). To conclude,
\begin{itemize}
\item[] note that $\mathrm{H}_{L_{1}}(x) \leq B$ if and only if $\mathrm{H}_{b L_{1}}(x) \leq B^{b}$. Therefore replacing $B$ with $B^{b}$ implies the claim.
\item[(ii)] We will proceed similar to the previous part, the only difference is that we use the embedding with multiple of $L_{2}$ instead of $L_{1}$. With the bound on the systole, Theorem 5.7 tells us that $L$ is an ample bundle as it has positive intersection with all subvarieties. Let $b$ be an integer such that $b L_{2}$ is very ample. Now, we can embed $\bar{X}$ into some projective space $\mathbb{P}^{N}$ by $b L_{2}$. Applying Theorem 5.7 gives us that for every subvariety of $\bar{X}$ not contained in $D$ one has:
$$\left(\left(b L_{2}\right)^{m} \cdot V\right)^{1 / m} \geq\left(\frac{n b}{4 \pi}\right) e^{\operatorname{sys}(X) / 16} .$$
Applying Theorem 8.1 gives us that:
$$\#\left\{x \in X(F) \mid \mathrm{H}_{b L_{2}}(x) \leq B\right\} \leq C B^{4 \pi[F: \mathbb{Q}](n+3)(1+\epsilon) / b s},$$
where $s=e^{\operatorname{sys}(X) / 16}$, and $C$ is constant depending on $X, F$ and $\epsilon$. Similar to the previous part we can conclude the desired inequality. \(\square\)
\end{itemize}

\section*{References}
\begin{itemize}
\item[] [AS95] Urban Angehrn and Yum Tong Siu. Effective freeness and point separation for adjoint bundles. Invent. Math., 122(2):291-308, 1995.
\item[] [AVA17] Dan Abramovich and Anthony Várilly-Alvarado. Level structures on abelian varieties and Vojta's conjecture. Compositio Mathematica, 153(2):373-394, 2017.
\item[] [AVA18] Dan Abramovich and Anthony Várilly-Alvarado. Level structures on abelian varieties, Kodaira dimensions, and Lang's conjecture. Advances in Mathematics, 329:523-540, 2018.
\item[] [BM22] Yohan Brunebarbe and Marco Maculan. Counting integral points of bounded height on varieties with large fundamental group. arXiv preprint arXiv:2205.05436, 2022.
\item[] [BP89] Enrico Bombieri and Jonathan Pila. The number of integral points on arcs and ovals. 1989.
\item[] [BRH ${ }^{+} 09$ ] Thomas Bauer, S Di Rocco, Brian Harbourne, Michał Kapustka, Andreas Knutsen, Wioletta Syzdek, and Tomasz Szemberg. A primer on Seshadri constants. Contemporary Mathematics, 496:33, 2009.
\item[] [Bru20a] Yohan Brunebarbe. Increasing hyperbolicity of varieties supporting a variation of Hodge structures with level structures. arXiv preprint arXiv:2007.12965, 2020.
\item[] [Bru20b] Yohan Brunebarbe. A strong hyperbolicity property of locally symmetric varieties. Ann. Sci. Éc. Norm. Supér. (4), 53(6):1545-1560, 2020.
\item[] [BT18] Benjamin Bakker and Jacob Tsimerman. The Kodaira dimension of complex hyperbolic manifolds with cusps. Compositio Mathematica, 154(3):549-564, 2018.
\item[] [CG74] SS Chen and Leon Greenberg. Hyperbolic spaces, Contributions to analysis. Academic Press, New York, pages 49-87, 1974.
\item[] [Chi22] Kenneth Chung Tak Chiu. Arithmetic sparsity in mixed Hodge settings. Bulletin of the London Mathematical Society, 2022.
\item[] [DCDC15] Gabriele Di Cerbo and Luca F Di Cerbo. Effective results for complex hyperbolic manifolds. Journal of the London Mathematical Society, 91(1):89-104, 2015.
\item[] [DCL21] Luca F. Di Cerbo and Luigi Lombardi. Moving Seshadri constants, and coverings of varieties of maximal Albanese dimension. Asian J. Math., 25(2):305-320, 2021.
\item[] [Dem92] Jean-Pierre Demailly. Singular Hermitian metrics on positive line bundles. In Complex Algebraic Varieties: Proceedings of a Conference held in Bayreuth, Germany, April 2-6, 1990, pages 87-104. Springer, 1992.
\item[] [EKL95] Lawrence Ein, Oliver Küchle, and Robert Lazarsfeld. Local positivity of ample line bundles. Journal of Differential Geometry, 42(2):193-219, 1995.
\end{itemize}
\begin{itemize}
\item[] [ELN96] Lawrence Ein, Robert Lazarsfeld, and Michael Nakamaye. Zero estimates, intersection theory, and a theorem of Demailly. Higher Dimensional Complex Varieties (Trento, 1994), de Gruyter, pages 183-207, 1996.
\item[] [ELV23] Jordan S Ellenberg, Brian Lawrence, and Akshay Venkatesh. Sparsity of integral points on moduli spaces of varieties. International Mathematics Research Notices, 2023(17):15073-15101, 2023.
\item[] [Fal84] G. Faltings. Arithmetic varieties and rigidity. In Seminar on number theory, Paris 1982-83 (Paris, 1982/1983), volume 51 of Progr. Math., pages 63-77. Birkhäuser Boston, Boston, MA, 1984.
\item[] [FW09] Elisha Falbel and Richard A Wentworth. On products of isometries of hyperbolic space. Topology and its Applications, 156(13):2257-2263, 2009.
\item[] [GK67] Samuel I Goldberg and Shoshichi Kobayashi. Holomorphic bisectional curvature. Journal of Differential Geometry, 1(3-4):225-233, 1967.
\item[] [Gol99] William Mark Goldman. Complex hyperbolic geometry. Oxford University Press, 1999.
\item[] [GR70] Howard Garland and Madabusi Santanam Raghunathan. Fundamental domains for lattices in $(\mathbb{R}-)$ rank 1 semisimple lie groups. Annals of Mathematics, 92(2):279-326, 1970.
\item[] [GR22] Robert C Gunning and Hugo Rossi. Analytic functions of several complex variables, volume 368. American Mathematical Society, 2022.
\item[] [HB02] D Roger Heath-Brown. The density of rational points on curves and surfaces. Annals of mathematics, 155(2):553-598, 2002.
\item[] [HT99] Jun-Muk Hwang and Wing-Keung To. On Seshadri constants of canonical bundles of compact complex hyperbolic spaces. Compositio Mathematica, 118(2):203-215, 1999.
\item[] [HT00] J-M Hwang and W-K To. On Seshadri constants of canonical bundles of compact quotients of bounded symmetric domains. 2000.
\item[] [HT02] Jun-Muk Hwang and Wing-Keung To. Volumes of complex analytic subvarieties of Hermitian symmetric spaces. American Journal of Mathematics, 124(6):1221-1246, 2002.
\item[] [Hwa05] Jun-Muk Hwang. On the number of complex hyperbolic manifolds of bounded volume. International Journal of Mathematics, 16(08):863-873, 2005.
\item[] [Kap22] Michael Kapovich. A survey of complex hyperbolic Kleinian groups. In In the Tradition of Thurston II: Geometry and Groups, pages 7-51. Springer, 2022.
\item[] [Kol97] János Kollár. Singularities of pairs. In Proceedings of Symposia in Pure Mathematics, volume 62, pages 221-288. American Mathematical Society, 1997.
\item[] [Laz17] Robert K Lazarsfeld. Positivity in algebraic geometry I: Classical setting: line bundles and linear series, volume 48. Springer, 2017.
\item[] $\left[\mathrm{M}^{+} 65\right] \quad$ AI Mal et al. On the faithful representation of infinite groups by matrices. Fifteen Papers on Algebra, 45:1-18, 1965.
\item[] [Mem22] Soheil Memariansorkhabi. Positivity of the cotangent bundle of complex hyperbolic manifolds with cusps. arXiv preprint arXiv:2212.10816, 2022.
\item[] [Mok12] Ngaiming Mok. Projective algebraicity of minimal compactifications of complex-hyperbolic space forms of finite volume. In Perspectives in analysis, geometry, and topology, volume 296 of Progr. Math., pages 331-354. Birkhäuser/Springer, New York, 2012.
\item[] [Mum77] David Bryant Mumford. Hirzebruch's proportionality theorem in the non-compact case. Inventiones mathematicae, 1977.
\item[] [Nad89] Alan Michael Nadel. The nonexistence of certain level structures on abelian varieties over complex function fields. Annals of Mathematics, 129(1):161-178, 1989.
\item[] [Ogg72] Andrew Ogg. Rational points on certain elliptic modular curves. In AMS Conference, St. Louis, 1972, pages 211-231, 1972.
\item[] [Ohb87] Akira Ohbuchi. Some remarks on ample line bundles on abelian varieties. Manuscripta mathematica, 57(2):225-238, 1987.
\item[] [Par97] John R Parker. Uniform discreteness and Heisenberg translations. Mathematische Zeitschrift, 225:485-505, 1997.
\item[] [Par98] John R Parker. On the volumes of cusped, complex hyperbolic manifolds and orbifolds. Duke mathematical journal, 94(3):433-464, 1998.
\item[] [Rat06] John G Ratcliffe. Foundations of hyperbolic manifolds. Springer, 2006.
\end{itemize}
[Rou16] Erwan Rousseau. Hyperbolicity, automorphic forms and Siegel modular varieties. In Annales Scientifiques de l'École Normale Supérieure, volume 49, pages 249-255, 2016.
[Shi71] Gorō Shimura. Introduction to the arithmetic theory of automorphic functions, volume 1. Princeton university press, 1971.
[Tak93] Shigeharu Takayama. Ample vector bundles on open algebraic varieties. Publications of the Research Institute for Mathematical Sciences, 29(6):885-910, 1993.
[Wan15] Xu Wang. Effective very ampleness of the canonical line bundles on ball quotients. The Journal of Geometric Analysis, 25:740-760, 2015.
[Won18] Kwok-Kin Wong. On effective existence of symmetric differentials of complex hyperbolic space forms. Math. Z., 290(3-4):711-733, 2018.
[Yeu00] Sai-Kee Yeung. Very ampleness of line bundles and canonical embedding of coverings of manifolds. Compositio Mathematica, 123(2):209-223, 2000.
[Yeu01] Sai-Kee Yeung. Effective estimates on the very ampleness of the canonical line bundle of locally Hermitian symmetric spaces. Transactions of the American Mathematical Society, 353(4):1387-1401, 2001.
[Yeu12] Sai-Kee Yeung. A tower of coverings of quasi-projective varieties. Advances in Mathematics, 230(3):1196-1208, 2012.
[Yeu17] Sai-Kee Yeung. On the canonical line bundle of a locally Hermitian symmetric space. The Journal of Geometric Analysis, 27:3240-3253, 2017.
[Yeu18] Sai-Kee Yeung. Very ampleness of the bicanonical line bundle on compact complex 2-ball quotients. In Forum Mathematicum, volume 30, pages 419-432. De Gruyter, 2018.

Dept. of Mathematics, Purdue University, West Lafayette, IN 47907, USA.
Email address: smemaria@purdue.edu