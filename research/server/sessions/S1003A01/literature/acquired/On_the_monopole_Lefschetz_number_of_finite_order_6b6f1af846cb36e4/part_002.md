---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: On the monopole Lefschetz number of finite order ...]

The generator of $\pi_{1}\left(S^{1}\right)$ acts on the cohomology groups $H^{*}(\Sigma, \operatorname{ad} \alpha)$ as
$$\operatorname{Ad} u \circ \tau^{*}: H^{*}(\Sigma, \operatorname{ad} \alpha) \rightarrow H^{*}(\Sigma, \operatorname{ad} \alpha),$$
where $u$ is such that $\tau^{*} \alpha=u \alpha u^{-1}$. If $\alpha$ is irreducible, $H^{0}(\Sigma, \operatorname{ad} \alpha)=0$ and the first summand in (19) vanishes. If $\alpha$ is non-trivial abelian, we may assume without loss of generality that it takes values in the group $U(1)$ of unit complex numbers. Then $\tau^{*} \alpha=u \alpha u^{-1}$ for some $u \in j \cdot U(1)$ and $H^{0}(\Sigma, \operatorname{ad} \alpha)=i \cdot \mathbb{R}$ as a subspace of $\mathfrak{s} \mathfrak{u}(2)$, with $\tau^{*}=\mathrm{id}$. One can easily check that $\operatorname{Ad} u$ acts as minus identity on $i \cdot \mathbb{R}$ hence the first summand in (19) again vanishes. The second summand in (19) is the fixed point set of $\tau^{*}$ acting on $H^{1}(\Sigma, \operatorname{ad} \alpha)$, which is the equivariant cohomology $H_{\tau}^{1}(\Sigma, \operatorname{ad} \alpha)$. Thus we conclude that $H^{1}(X, \operatorname{ad} A)=H_{\tau}^{1}(\Sigma, \operatorname{ad} \alpha)$, which completes the proof. \(\square\)

Let us assume that $\mathcal{R}^{\tau}(\Sigma)$ is non-degenerate. For any $[\alpha] \in \mathcal{R}^{\tau}(\Sigma)$, its orientation will be given by
$$(-1)^{\operatorname{sf}^{\tau}(\theta, \alpha)}$$
where $\mathrm{sf}^{\tau}(\theta, \alpha)$ is the mod 2 equivariant spectral flow defined in [45, Section 3.4] for irreducible $\alpha$. That definition extends word for word to abelian $\alpha$ after one resolves the technical issue of the existence of a constant lift, which we will do next.

Let $P$ be an $S U(2)$ bundle over $\Sigma$ with a fixed trivialization and $\alpha$ an abelian flat connection in $P$ with holonomy in $\mathcal{R}_{\mathrm{ab}}^{\tau}(\Sigma)$; we are abusing notations by using the same symbol for the connection and its holonomy. Since $\mathcal{R}_{\mathrm{ab}}^{\tau}(\Sigma)$ is empty for odd $n$ (see Proposition 6.6) we will assume without loss of generality that $n$ is even. Then $\tau$ admits a lift $\tilde{\tau}: P \rightarrow P$ such that $\tilde{\tau}^{*} \alpha=\alpha$. Since $\alpha$ is abelian and non-central, this lift is defined uniquely up to the stabilizer of $\alpha$, which is a copy of $U(1)$ in $S U(2)$. The lift $\tilde{\tau}$ can be written in the base-fiber coordinates as $\tilde{\tau}(x, y)=(\tau(x), \rho(x) \cdot y)$ for some function $\rho: \Sigma \rightarrow S U(2)$. We call it constant if there exists $u \in S U(2)$ such that $\rho(x)=u$ for all $x \in S U(2)$.

Lemma 6.10. By changing $\alpha$ within its gauge equivalence class, one may assume that $\tilde{\tau}$ is a constant lift with $u^{2}=-1$.

Proof. The equation $\tilde{\tau}^{*} \alpha=\alpha$ implies that $\left(\tilde{\tau}^{n}\right)^{*} \alpha=\alpha$, so the gauge transformation $\tilde{\tau}^{n}$ belongs to the stabilizer of the connection $\alpha$. If $x \in \operatorname{Fix}(\tau)$ then $\tilde{\tau}^{n}(x, y)=$ $\left(x, \rho(x)^{n} \cdot y\right)$ hence $\rho(x)^{n}$ is a unit complex number independent of $x$. This implies
that $\rho(x)$ itself is a unit complex number unless $\rho(x)^{n}= \pm 1$. The latter equation actually implies that $\rho(x)^{2}=-1$ because, at the level of holonomy representations, $\tau^{*} \alpha=\alpha^{-1}$ is conjugate to $\alpha$ by an element $u \in S U(2)$ with $u^{2}=-1$; see the proof of Proposition 6.7. Since $\rho(x)^{2}=-1$ describes a single conjugacy class $\operatorname{tr} \rho(x)=0$ in $S U(2)$, we may assume that $\rho(x)=u$ for all $x \in \operatorname{Fix}(\tau)$.

To finish the proof, we will follow the argument of [45, Section 2.2]. Let $u:$ $P \rightarrow P$ be the constant lift $u(x, y)=(\tau(x), u \cdot y)$ and consider the $S O(3)$ orbifold bundles $P / \tilde{\tau}$ and $P / u$ over the integral homology sphere $Y$. All such bundles are classified by the holonomy around the singular set in $Y$. Since this holonomy equals $\operatorname{Ad}(u)$ in both cases, the bundles $P / \tilde{\tau}$ and $P / u$ must be isomorphic, with any isomorphism pulling back to a gauge transformation $g: P \rightarrow P$ relating the lifts $\tilde{\tau}$ and $u$. \(\square\)

Proposition 6.11. Assuming that the moduli space $\mathcal{R}^{\tau}(\Sigma)$ is non-degenerate, the map (18) is orientation preserving.

Proof. The proof from [45, Section 3] extends to the current situation with no change. \(\square\)
6.2. Orbifold theory. Under the continued non-degeneracy assumption, we will now describe $\mathcal{R}^{\tau}(\Sigma)$ in terms of orbifold representations. Let us consider the orbifold fundamental group $\pi_{1}^{V}(Y, K)=\pi_{1}(N) /\left\langle\mu^{n}\right\rangle$, where $N=Y-\operatorname{Int}(D(K))$ is the knot exterior and $\mu$ is a meridian of $K$. This group can be included into the split orbifold exact sequence
$$1 \longrightarrow \pi_{1} \Sigma \xrightarrow{\pi_{*}} \pi_{1}^{V}(Y, K) \xrightarrow{j} \mathbb{Z} / n \longrightarrow 1,$$
where $j$ is the abelianization homomorphism. Denote by $\mathcal{R}^{V}(Y, K ; S O(3))$ the character variety of irreducible $S O(3)$ representations of the group $\pi_{1}^{V}(Y, K)$, and also introduce the character variety $\mathcal{R}^{\tau}(\Sigma ; S O(3))$ of non-trivial representations $\pi_{1} \Sigma \rightarrow S O(3)$ fixed by $\tau^{*}$.

Proposition 6.12. The pull back of representations via the map $\pi_{*}$ in the orbifold exact sequence gives rise to a one-to-one correspondence
$$\pi^{*}: \mathcal{R}^{V}(Y, K ; S O(3)) \longrightarrow \mathcal{R}^{\tau}(\Sigma ; S O(3)) .$$

Proof. One can easily see that a representation $\alpha^{\prime}: \pi_{1}^{V}(Y, K) \rightarrow S O(3)$ pulls back to a trivial representation $\theta: \pi_{1} \Sigma \rightarrow S O(3)$ if and only if $\alpha^{\prime}$ is reducible. The same argument as in [14, Proposition 3.3] shows that all pull-back representations belong to $\mathcal{R}^{\tau}(\Sigma, S O(3))$. The inverse map for $\pi^{*}$ is constructed as follows: given $[\alpha] \in \mathcal{R}^{\tau}(\Sigma, S O(3))$ choose $v \in S O(3)$ such that $\tau^{*} \alpha=v \alpha v^{-1}$, and define a representation $\alpha^{\prime}$ of $\pi_{1}^{V}(Y, K)=\pi_{1} \Sigma \rtimes \mathbb{Z} / n$ by the formula
$$\alpha^{\prime}\left(g \cdot \mu^{k}\right)=\alpha(g) \cdot v^{k} .$$
If $\alpha$ is irreducible, the element $v$ is unique hence formula (20) gives an inverse map. If $\alpha$ is non-trivial abelian, an argument similar to that in the proof of Proposition 6.6 shows that $v=\operatorname{Ad} u$ for some $u \in j \cdot U(1)$. Since any two elements of $j \cdot U(1)$ are conjugate to each other by a unit complex number, formula (20) again gives an inverse map. \(\square\)

Representations $\pi_{1}^{V}(Y, K) \rightarrow S O(3)$ need not lift to $S U(2)$ representations; however, they lift to projective representations $\pi_{1}^{V}(Y, K) \rightarrow S U(2)$ sending $\mu^{n}$ to ±1; see [44, Section 3.1]. The character variety of such projective representations will be denoted by $\mathcal{R}^{V}(Y, K)$, and it will be oriented using the orbifold spectral flow.

Proposition 6.13. The correspondence of Proposition 6.12 gives rise to an orientation preserving correspondence $\mathcal{R}^{V}(Y, K) \rightarrow \mathcal{R}^{\tau}(\Sigma)$ which is one-to-one over $\mathcal{R}_{\mathrm{ab}}^{\tau}(\Sigma)$ and two-to-one over $\mathcal{R}_{\text {irr }}^{\tau}(\Sigma)$.

Proof. We first need to check that the map $\mathcal{R}^{V}(Y, K) \rightarrow \mathcal{R}^{\tau}(\Sigma)$ is well-defined because the pull back of a projective representation $\pi_{1}^{V}(Y, K) \rightarrow S U(2)$ is a priori a projective representation $\alpha: \Sigma \rightarrow S U(2)$. The only obstruction to it being an actual representation is the second Stiefel-Witney class $w_{2}(\operatorname{Ad} \alpha) \in H^{2}(\Sigma ; \mathbb{Z} / 2)$. That this class vanishes can be seen as follows. The conjugacy class of $\alpha$ is fixed by $\tau$, therefore, $w_{2}(\operatorname{Ad} \alpha)$ must belong to the fixed point set of $\tau^{*}: H^{2}(\Sigma ; \mathbb{Z} / 2) \rightarrow$ $H^{2}(\Sigma ; \mathbb{Z} / 2)$. Using Poincaré duality, this fixed point set can be identified with the kernel of the map $\tau_{*}-1: H_{1}(\Sigma ; \mathbb{Z} / 2) \rightarrow H_{1}(\Sigma ; \mathbb{Z} / 2)$. This kernel vanishes because the map $\tau_{*}-1: H_{1}(\Sigma) \rightarrow H_{1}(\Sigma)$ is injective by Corollary 6.2 and is therefore an automorphism of the finite abelian group $H_{1}(\Sigma)$; cf. the proof of Lemma 6.5.

Let us now consider the adjoint representation Ad : $S U(2) \rightarrow S O(3)$ and the induced maps on character varieties,
$$\mathcal{R}^{\tau}(\Sigma) \rightarrow \mathcal{R}^{\tau}(\Sigma ; S O(3)) \quad \text { and } \quad \mathcal{R}^{V}(Y, K) \rightarrow \mathcal{R}^{V}(Y, K ; S O(3)) .$$

The first map is a one-to-one correspondence, which can be seen as follows. We showed in the previous paragraph that every equivariant representation $\pi_{1} \Sigma \rightarrow$ $S O(3)$ admits a lift to a representation $\pi_{1} \Sigma \rightarrow S U(2)$. The number of all such lifts is known to equal the cardinality of $H^{1}(\Sigma ; \mathbb{Z} / 2)$. However, we are only interested in equivariant lifts, and their number equals the cardinality of the fixed point set of $\tau^{*}: H^{1}(\Sigma ; \mathbb{Z} / 2) \rightarrow H^{1}(\Sigma ; \mathbb{Z} / 2)$. The latter cardinality is easily seen to be one using Corollary 6.2.

The second map in (21) is the quotient map by the action of $\mathbb{Z} / 2$ sending the image of the meridian $\mu$ to its negative. The fixed points of this action are precisely the binary dihedral projective representations $\alpha^{\prime}: \pi_{1}^{V}(Y, K) \rightarrow S U(2)$. Now, the proof will be finished as soon as we show that an irreducible projective representation $\alpha^{\prime}: \pi_{1}^{V}(Y, K) \rightarrow S U(2)$ is binary dihedral if and only if its pull back representation $\pi^{*} \alpha^{\prime}: \pi_{1} \Sigma \rightarrow S U(2)$ is abelian.

If $\pi^{*} \alpha^{\prime}$ is abelian, its image belongs to $U(1) \subset S U(2)$ and the image of $\alpha^{\prime}$ to its $\mathbb{Z} / n$ extension. Since the only finite extension of $U(1)$ inside $S U(2)$ is the binary dihedral group $U(1) \cup j \cdot U(1)$, we conclude that $\alpha^{\prime}$ must be binary dihedral. In particular, if $n$ is odd, the representation $\pi^{*} \alpha^{\prime}$ cannot be abelian, which matches the fact that $\mathcal{R}_{\mathrm{ab}}^{\tau}(\Sigma)$ is empty by Proposition 6.6. Conversely, it follows from the orbifold exact sequence that $\pi_{1} \Sigma$ is the commutator subgroup of $\pi_{1}^{V}(Y, K)$. Therefore, if $\alpha^{\prime}$ is binary dihedral, the image of $\pi^{*} \alpha^{\prime}$ must belong to the commutator subgroup of $U(1) \cup j \cdot U(1)$, which is of course the group $U(1)$.

Since the orbifold spectral flow matches the equivariant spectral flow used to orient $\mathcal{R}^{\tau}(\Sigma)$, the above correspondence is orientation preserving. \(\square\)
6.3. Perturbations. In this section, we will remove the assumption that $\mathcal{R}^{\tau}(\Sigma)$ is non-degenerate which we used until now. To accomplish that, we will switch from the language of representations to the language of connections. Let $P$ a trivialized $S U(2)$ bundle over $\Sigma$. Any endomorphism $\tilde{\tau}: P \rightarrow P$ which lifts the involution $\tau$ induces an action on the space of connections $\mathcal{A}(\Sigma)$ by pull back. Since any two such lifts are related by a gauge transformation, this action gives a well defined
action on the configuration space $\mathcal{B}(\Sigma)=\mathcal{A}(\Sigma) / \mathcal{G}(\Sigma)$. The fixed point set of this action will be denoted by $\mathcal{B}^{\tau}(\Sigma)$.

The irreducible part of $\mathcal{B}^{\tau}(\Sigma)$ was studied in [45] hence we will only deal with reducible connections. In fact, we will further restrict ourselves to constant lifts $u$ because any flat abelian connection $\alpha$ admits such a lift; see Lemma 6.10.

Let $\mathcal{A}^{u}(\Sigma) \subset \mathcal{A}(\Sigma)$ consist of all non-trivial connections $A$ such that $u^{*} A=A$, and $\mathcal{G}^{u}(\Sigma) \subset \mathcal{G}(\Sigma)$ of all gauge transformations $g$ such that $g u=u g$. The quotient space $\mathcal{A}^{u}(\Sigma) / \mathcal{G}^{u}(\Sigma)$ will be denoted by $\mathcal{B}^{u}(\Sigma)$. The following lemma is a key to making the arguments of [45] work in the case of abelian connections.

Lemma 6.14. The group $\mathcal{G}^{u}(\Sigma)$ acts on $\mathcal{A}^{u}(\Sigma)$ with the stabilizer $\{ \pm 1\}$. Moreover, the natural map $\mathcal{B}^{u}(\Sigma) \rightarrow \mathcal{B}^{\tau}(\Sigma)$ is a two-to-one correspondence to its image on the irreducible part of $\mathcal{B}^{u}(\Sigma)$, and a one-to-one correspondence on the reducible part.

Proof. For the sake of simplicity, we will assume that reducible connections have their holonomy in the subgroup $U(1)$ of unit complex numbers in $S U(2)$, and that $u \in j \cdot U(1)$. Let us suppose that $g^{*} A=A$ for a connection $A \in \mathcal{A}^{u}(\Sigma)$ and a gauge transformation $g \in \mathcal{G}^{u}(\Sigma)$. If $A$ is irreducible, we automatically have $g= \pm 1$. If $A$ is non-trivial abelian, then $g$ is a complex number, and the condition $u g=g u$ implies that $g= \pm 1$.

To prove the second statement, consider a connection $A$ such that $u^{*} A=A$ and consider its gauge equivalence class in $\mathcal{B}^{\tau}(\Sigma)$. It consists of all connections $g^{*} A$ such that $u^{*} g^{*} A=g^{*} A$. Since $A=u^{*} A$, we immediately conclude that $u^{*} g^{*} A=g^{*} u^{*} A$ so that $u g$ and $g u$ differ by an element in the stabilizer of $A$. If $A$ is irreducible, its stabilizer consists of $\pm 1$ hence $u g= \pm g u$. The group of gauge transformations satisfying this condition contains $\mathcal{G}^{u}(\Sigma)$ as a subgroup of index two, which leads to the desired two-to-one correspondence. If $A$ is non-trivial abelian, its stabilizer consists of unit complex numbers. Therefore, we can write $u g=c^{2} g u$ with $c \in U(1)$ or, equivalently, $u c g=c g u$. This provides us with a gauge transformation $c g \in \mathcal{G}^{u}(\Sigma)$ such that $(c g)^{*} A=g^{*} A$, yielding the one-to-one correspondence on the reducible part. \(\square\)

With this lemma in place, the proof of Proposition 6.7 can be re-stated in gauge-theoretic terms as in [45, Proposition 3.1]. The treatment of perturbations in our case is then essentially identical to that in [14] and [45], one important observation
being that the orbifold representations $\alpha^{\prime}$ that pull back to abelian representations of $\pi_{1}(\Sigma)$ are in fact irreducible. This fact is used in the proof of [14, Lemma 3.8], which supplies us with sufficiently many admissible perturbations.
6.4. Proof of Theorem 6.4. The outcome of Section 6.1 and Section 6.2 is that, perhaps after perturbing as in Section 6.3, we have two orientation preserving correspondences,
$$\mathcal{M}^{*}(X) \longrightarrow \mathcal{R}^{\tau}(\Sigma) \longleftarrow \mathcal{R}^{V}(Y, K),$$
both of which are one-to-one over $\mathcal{R}_{\mathrm{ab}}(\Sigma)$ and two-to-one over $\mathcal{R}_{\text {irr }}^{\tau}(\Sigma)$ (we omit perturbations in our notations). These correspondences imply the existence of an orientation preserving one-to-one correspondence between $\mathcal{M}^{*}(X)$ and $\mathcal{R}^{V}(Y, K)$. The proof of Theorem 6.4 will be complete after we express the signed count of points in $\mathcal{R}^{V}(Y, K)$ in terms of the Casson invariant of $Y$ and the equivariant knot signatures of $K$.

The character variety $\mathcal{R}^{V}(Y, K)$ of projective representations $\alpha^{\prime}$ splits into two components corresponding to whether $\left(\alpha^{\prime}(\mu)\right)^{n}$ equals +1 or -1. Let $N$ be the exterior of the knot $K$ then this splitting corresponds to the splitting
$$\mathcal{R}^{V}(Y, K)=\bigcup_{k=0}^{n} \mathcal{S}_{k / n}(N, S U(2)),$$
where $\mathcal{S}_{a}(N, S U(2))$ comprises the conjugacy classes of representations $\gamma: \pi_{1} N \rightarrow$ $S U(2)$ such that $\operatorname{tr} \gamma(\mu)=2 \cos (\pi a)$. According to Herald [20], see also Collin-Saveliev [14], the combined signed count of points in (22) equals
$$4 n \cdot \lambda(Y)+\frac{1}{2} \cdot \sum_{m=1}^{n-1} \operatorname{sign}_{m / n}(K) .$$
Dividing this formula by four, we obtain the formula for the Furuta-Ohta invariant $\lambda_{\mathrm{FO}}(X)$ claimed in Theorem 6.4.

\section*{7. Applications}

In this section we supply proofs for the applications of our main theorem discussed in Section 1.2 of the introduction; for the convenience of the reader we will restate each result before giving the proof.

Theorem 7.1 (Theorem H from the introduction). Let $n=p^{m}$ for $p$ a prime number. There is a knot $K_{n}$ such that, for any knot $K$ that is smoothly concordant to $K_{n}$, its $n$-fold cyclic branched cover $\Sigma_{n}(K)$ is not an $L$-space.

Proof. Since $n$ is a prime power, it is standard that all of the Tristram-Levine signatures are knot concordance invariants. Similarly, the $h$-invariant of the $n$-fold cyclic branched cover, with the specified spin ${ }^{c}$ structure, is a knot concordance invariant [21]. It now follows from Theorem A that Lef $\left(\tau_{*}\right)$ is a knot concordance invariant. Therefore, if $K_{n}$ is a knot for which Lef $\left(\tau_{*}\right) \neq 0$, then the same is true for any knot $K$ in the concordance class of $K_{n}$. In particular, the $n$-fold cyclic branched cover of $K$ is not an $L$-space.

All that remains to prove the theorem is to find a knot $K_{n}$ with Lef $\left(\tau_{*}\right) \neq 0$. Pick relatively prime integers $q$ and $r$ both of which are greater than or equal to 2 and are relatively prime with $p$; we will exclude the triple (2, 3, 5) to avoid dealing with the exceptional case of the Poincaré homology sphere. The $n$-fold cyclic branched cover of the right-handed torus knot $T(q, r)$ is the Brieskorn homology sphere
$$\Sigma(n, q, r)=\left\{x^{n}+y^{q}+z^{r}=0\right\} \cap S^{5}$$
with its canonical link orientation and with the covering translation $\tau(x, y, z)=$ $\left(e^{2 \pi i / n} x, y, z\right)$. The homology sphere $\Sigma(n, q, r)$ admits a fixed point free circle action $t(x, y, z)=\left(t^{q r} x, t^{n r} y, t^{n q} z\right)$ making it into a Seifert fibered manifold; see Neumann-Raymond [41]. The covering translation $\tau$ is actually contained in this circle action: it corresponds to the choice of $t=e^{2 \pi i p / n}$ for any integer $p$ such that $p q r \equiv 1(\bmod n)$. This implies that $\tau$ is isotopic to the identity and that Lef $\left(\tau_{*}\right)=\chi\left(H M^{\text {red }}(\Sigma(n, q, r))\right)$.

To show that $\chi\left(H M^{\text {red }}(\Sigma(n, q, r))\right) \neq 0$, we will use the identification of the monopole and Heegaard Floer homology due to Kutluhan, Lee, and Taubes [24, 25, 26, 27, 28], or alternatively, Colin, Ghiggini, and Honda [11, 12, 13] and Taubes [47]. The non-vanishing of the Euler characteristic of $H M^{\text {red }}(\Sigma(n, q, r))$ follows from this identification and the corresponding result in Heegaard Floer homology [9] as well as [15, 46]. \(\square\)

For any prime power $n$, we can define a subgroup $\mathcal{B} L_{n}$ in the smooth concordance group $\mathcal{C}$ generated by knots that are concordant to a knot whose $n$-fold branched cover is an $L$-space. One would expect that, for a given $n$, the group $\mathcal{B} L_{n}$ is rather small; our Theorem 7.1 provides some evidence for that.

Corollary 7.2. Let $n$ be a prime power. Then $\mathcal{C} / \mathcal{B} L_{n}$ has a $\mathbb{Z}$ summand.

Proof. It follows from the proof of Theorem 7.1 that $\operatorname{Lef}\left(\tau_{*}\right): \mathcal{C} \rightarrow \mathbb{Z}$ is a well-defined non-zero map. Since both $h(\Sigma, \mathfrak{s})$ and the Tristram-Levine signatures are homomorphisms, Theorem A implies that $\operatorname{Lef}\left(\tau_{*}\right)$ is a homomorphism as well. Thus there is a surjection from $\mathcal{C} / \mathcal{B} L_{n}$ to the image of this homomorphism, which is isomorphic to $\mathbb{Z}$. \(\square\)

Remark 7.3. One could alternately deduce that the Lefschetz number is a homomorphism from the splitting formula of [32] and the additivity of $\lambda_{\text {SW }}$ proved in [35].

Theorem 7.4 (Theorem I from the introduction). Let $K \subset S^{3}$ be a knot with $\operatorname{det}(K)=1$ and $J^{\prime}(-1) \neq 0$, where $J_{K}(t)$ is the Jones polynomial of $K$. Then, for any $m \geqslant 1$, the 2m-fold cyclic branched cover $\Sigma_{2 m}(K)$ is not an $L$-space.

Proof. We may assume without loss of generality that $\Sigma_{2 m}(K)$ is a rational homology sphere. Since $\operatorname{det}(K)=1, \Sigma_{2}(K)$ is a homology sphere, so this is automatic when $m$ is a prime power. Suppose $\Sigma_{2 m}(K)$ is an $L$-space and apply the formula of Theorem A to the covering translation $\tau$ and its square $\tau^{2}$. We obtain the formulas
$$\begin{aligned}
& h\left(\Sigma_{2 m}(K), \mathfrak{s}\right)=\frac{1}{8} \sum_{j=1}^{2 m-1} \operatorname{sign}_{j / 2 m}\left(K, S^{3}\right) \text { and } \\
& h\left(\Sigma_{2 m}(K), \mathfrak{s}\right)=m \cdot \lambda\left(\Sigma_{2}(K)\right)+\frac{1}{8} \sum_{j=1}^{m-1} \operatorname{sign}_{j / m}\left(K, \Sigma_{2}(K)\right) .
\end{aligned}$$
Comparing them, we obtain
$$m \cdot \lambda\left(\Sigma_{2}(K)\right)=\frac{1}{8} \sum_{j=1}^{2 m-1} \operatorname{sign}_{j / 2 m}\left(K, S^{3}\right)-\frac{1}{8} \sum_{j=1}^{m-1} \operatorname{sign}_{j / m}\left(K, \Sigma_{2}(K)\right) .$$
On the other hand, we have the equality
$$\frac{1}{8} \sum_{j=1}^{2 m-1} \operatorname{sign}_{j / 2 m}\left(K, S^{3}\right)-\frac{1}{8} \sum_{j=1}^{m-1} \operatorname{sign}_{j / m}\left(K, \Sigma_{2}(K)\right)=\frac{m}{8} \cdot \operatorname{sign}_{1 / 2}\left(K, S^{3}\right),$$
which can be proved as follows. By pushing a Seifert surface of $K$ into the interior of the 4-ball and taking the 2-fold and $2 m$-fold branched covers, we obtain 4-manifolds $W_{2}$ and $W_{2 m}$ with
$$\begin{gathered}
\sum_{j=1}^{2 m-1} \operatorname{sign}_{j / 2 m}\left(K, S^{3}\right)=\operatorname{sign}\left(W_{2 m}\right), \\
\sum_{j=1}^{m-1} \operatorname{sign}_{j / m}\left(K, \Sigma_{2}(K)\right)=\operatorname{sign}\left(W_{2 m}\right)-m \cdot \operatorname{sign}\left(W_{2}\right), \quad \text { and } \\
\operatorname{sign}_{1 / 2}\left(K, S^{3}\right)=\operatorname{sign}\left(W_{2}\right) .
\end{gathered}$$
This gives the desired formula. We therefore conclude that
$$\lambda\left(\Sigma_{2}(K)\right)=\frac{1}{8} \operatorname{sign}_{1 / 2}\left(K, S^{3}\right) .$$
Comparing this with Mullins's theorem [40]
$$\lambda\left(\Sigma_{2}(K)\right)=-\frac{1}{12} J^{\prime}(-1)+\frac{1}{8} \operatorname{sign}_{1 / 2}\left(K, S^{3}\right),$$
we obtain $J^{\prime}(-1)=0$, a contradiction. \(\square\)

Theorem 7.5 (Theorem K from the introduction). Let $X$ be the mapping torus of an orientation preserving diffeomorphism (not necessary of finite order) of a rational homology sphere. Then, for any choice of spin structure on $X$, we have
$$-\lambda_{\mathrm{SW}}(X)=\lambda_{\mathrm{SW}}(-X) .$$
Proof. Let $X$ be the mapping torus of a finite order diffeomorphism $\tau: \Sigma \rightarrow \Sigma$ of a rational homology sphere $\Sigma$. Given a spin structure on $X$ denote by $\mathfrak{s}$ its restriction to $\Sigma$ and observe that $\tau^{*}(\mathfrak{s})=\mathfrak{s}$. Let $-\Sigma$ be the manifold $\Sigma$ with reversed orientation and denote by $-\mathfrak{s}$ and $-\tau$ the corresponding spin structure and diffeomorphism, respectively. By the splitting theorem of $\lambda_{\text {SW }}$ [32, Theorem A], we have
$$\begin{gathered}
\lambda_{\mathrm{SW}}(X)=-\operatorname{Lef}\left(\tau_{*}: H M^{\mathrm{red}}(\Sigma, \mathfrak{s}) \rightarrow H M^{\mathrm{red}}(\Sigma, \mathfrak{s})\right)-h(\Sigma, \mathfrak{s}) \quad \text { and } \\
\lambda_{\mathrm{SW}}(-X)=-\operatorname{Lef}\left((-\tau)_{*}: H M^{\mathrm{red}}(-\Sigma,-\mathfrak{s}) \rightarrow H M^{\mathrm{red}}(-\Sigma,-\mathfrak{s})\right)-h(-\Sigma,-\mathfrak{s}) .
\end{gathered}$$
Since $h$ is a homology cobordism invariant, it vanishes on the manifold $\Sigma \#(-\Sigma)$. It now follows from the additivity of $h$ (see [17, Theorem 3]) that $h(-\Sigma,-\mathfrak{s})=$ $-h(\Sigma, \mathfrak{s})$. Therefore, all we need is to check is that
$$\operatorname{Lef}\left((-\tau)_{*}\right)=-\operatorname{Lef}\left(\tau_{*}\right) .$$

Lemma 7.6. There is a duality isomorphism $\widetilde{H M}_{a}(-\Sigma,-\mathfrak{s}) \cong \widehat{H M}_{1+a}(\Sigma, \mathfrak{s})^{*}$ with respect to the canonical mod 2 grading in monopole homology.

Proof. The monopole homology has two canonical gradings, the rational grading $\operatorname{gr}^{\mathbb{Q}}$ and the mod 2 grading $\operatorname{gr}^{(2)}$. Kronheimer and Mrowka [22, Proposition 28.3.4] construct a duality isomorphism $\widetilde{H M}(-\Sigma,-\mathfrak{s}) \rightarrow \widehat{H M}(\Sigma, \mathfrak{s})^{*}$ which maps elements of rational grading $j$ to elements of rational grading $-1-j$. Since the relative rational grading matches modulo 2 the relative mod 2 grading, there is a universal constant $c(\Sigma, \mathfrak{s}) \in \mathbb{Q} / 2 \mathbb{Z}$ such that $\operatorname{gr}^{\mathbb{Q}}=\operatorname{gr}^{(2)}+c(\Sigma, \mathfrak{s})(\bmod 2)$. Therefore, the above duality isomorphism maps elements of mod 2 grading $a$ to elements of $\bmod 2$ grading $1+a+c(\Sigma, \mathfrak{s})+c(-\Sigma,-\mathfrak{s})(\bmod 2)$. The calculation of [32, Lemma 2.6] implies that $c(\Sigma, \mathfrak{s})+c(-\Sigma,-\mathfrak{s})=0(\bmod 2)$, thereby completing the argument. \(\square\)

Recall from [22, (3.4)] that $H M_{a}^{\text {red }}(\Sigma, \mathfrak{s})=\operatorname{im} j_{\Sigma, a}$ for the connecting homomorphism $j_{\Sigma, a}: \widetilde{H M}_{a}(\Sigma, \mathfrak{s}) \rightarrow \widehat{H M}_{a}(\Sigma, \mathfrak{s})$. Moreover, it follows from the definition of $j_{\Sigma, a}$ that, under the duality isomorphisms
$$\widehat{H M}_{a}(-\Sigma,-\mathfrak{s}) \cong \widehat{H M}_{1+a}(\Sigma, \mathfrak{s})^{*} \quad \text { and } \quad \widehat{H M}_{a}(-\Sigma,-\mathfrak{s}) \cong \widetilde{H M}_{1+a}(\Sigma, \mathfrak{s})^{*}$$
of Lemma 7.6, the map $j_{-\Sigma, a}$ is the dual of the map $j_{\Sigma, 1+a}$. As a consequence, we obtain an isomorphism
$$H M_{a}^{\mathrm{red}}(-\Sigma,-\mathfrak{s}) \cong H M_{1+a}^{\mathrm{red}}(\Sigma, \mathfrak{s})^{*} .$$
With respect to this isomorphism, $(-\tau)_{*}$ is the dual of $\tau_{*}$, which implies that $\operatorname{Lef}\left((-\tau)_{*}\right)=-\operatorname{Lef}\left(\tau_{*}\right)$. \(\square\)

\section*{References}
\begin{itemize}
\item[] [1] N. Anvari, A splitting formula in instanton Floer homology. Preprint, https://arxiv.org/ abs/1901.02570 (2019).
\item[] [2] M. Atiyah, V. Patodi, I. Singer, Spectral asymmetry and Riemannian geometry. I, Math. Proc. Cambridge Phil. Soc. 77 (1975), 43-69
\item[] [3] -, Spectral asymmetry and Riemannian geometry. III, Math. Proc. Cambridge Phil. Soc. 79 (1976), 71-99
\item[] [4] S. Baldridge, Seiberg-Witten invariants, orbifolds, and circle actions, Trans. Amer. Math. Soc. 355 (2002), 1669-169
\item[] [5] M. Boileau, S. Boyer, and C. M. Gordon, Branched covers of quasi-positive links and $l$-spaces, Journal of Topology 12 (2019), 536-576.
\end{itemize}
\begin{itemize}
\item[] [6] \_\_\_\_, On definite strongly quasipositive links and L-space branched covers, Adv. Math. 357 (2019), 106828.
\item[] [7] S. Boyer, C. M. Gordon, and L. Watson, On $L$-spaces and left-orderable fundamental groups, Math. Ann. 356 (2013), 1213-1245.
\item[] [8] G. Burde, H. Zieschang, "Knots", vol. 5 of De Gruyter Studies in Mathematics, Walter de Gruyter \& Co., Berlin, 1985.
\item[] [9] M. B. Can and Ç. Karakurt, Calculating Heegaard-Floer homology by counting lattice points in tetrahedra, Acta Math. Hungar. 144 (2014), 43-75.
\item[] [10] S. Cappel, R. Lee, E. Miller, Self-adjoint elliptic operators and manifold decompositions. II, Comm. Pure Appl. Math. 49 (1996), 869-909
\item[] [11] V. Colin, P. Ghiggini, and K. Honda, The equivalence of Heegaard Floer homology and embedded contact homology via open book decompositions I. Preprint http://arxiv.org/abs/1208.1074, 2012.
\item[] [12] \_\_\_\_, The equivalence of Heegaard Floer homology and embedded contact homology via open book decompositions II. Preprint http://arxiv.org/abs/1208.1077, 2012.
\item[] [13] \_\_\_\_, The equivalence of Heegaard Floer homology and embedded contact homology via open book decompositions III: from hat to plus. Preprint http://arxiv.org/abs/1208.1526, 2012.
\item[] [14] O. Collin, N. Saveliev, Equivariant Casson invariants via gauge theory, J. Reine Angew. Math. 541 (2001), 143-169
\item[] [15] E. Eftekhary, Seifert fibered homology spheres with trivial Heegaard Floer homology. Preprint https://arxiv.org/abs/0909.3975 (2009).
\item[] [16] K. A. Frøyshov, Equivariant aspects of Yang-Mills Floer theory, Topology 41 (2002), 525-552
\item[] [17] \_\_\_\_, Floer homology for rational homology 3-spheres, Duke Math. J. 155 (2010), no. 3, 519-576
\item[] [18] M. Furuta, H. Ohta, Differentiable structures on punctured 4-manifolds, Topology Appl. 51 (1993), 291-301
\item[] [19] P. Gilmer, Configurations of surfaces in 4-manifolds, Trans. Amer. Math. Soc. 264 (1981), 353-380
\item[] [20] C. Herald, Flat connections, the Alexander invariant, and Casson's invariant, Comm. Anal. Geom. 5 (1997), 93-120
\item[] [21] S. Jabuka, Concordance invariants from higher order covers, Topology Appl. 159 (2012), 2694-2710
\item[] [22] P. B. Kronheimer and T. S. Mrowka, "Monopoles and Three-Manifolds", Cambridge University Press, Cambridge, UK, 2008.
\item[] [23] \_\_\_\_, Knots, sutures, and excision, J. Differential Geom. 84 (2010), 301-364
\item[] [24] C. Kutluhan, Y.-J. Lee, and C. Taubes, $H F=H M I$ : Heegaard Floer homology and Seiberg-Witten Floer homology. Preprint http://arxiv.org/abs/1007.1979 2010.
\item[] [25] \_\_\_\_, HF=HM II: Reeb orbits and holomorphic curves for the ech/Heegaard-Floer correspondence. Preprint http://arxiv.org/abs/1008.1595, 2010.
\end{itemize}
\begin{itemize}
\item[] [26] \_\_\_\_, HF=HM III: Holomorphic curves and the differential for the ech/Heegaard Floer correspondence. Preprint http://arxiv.org/abs/1010.3456, 2010.
\item[] [27] \_\_\_\_, HF=HM IV: The Seiberg-Witten Floer homology and ech correspondence. Preprint http://arxiv.org/abs/1107.2297 2011.
\item[] [28] \_\_\_\_, HF=HM V: Seiberg-Witten-Floer homology and handle addition. Preprint http:// arxiv.org/abs/1204.0115, 2012.
\item[] [29] J. Levine, Knot modules, I, Trans. Amer. Math. Soc. 229 (1977), 1-50
\item[] [30] Y. Lim, Seiberg-Witten moduli spaces for 3-manifolds with cylindrical-end $T^{2} \times \mathbb{R}^{+}$, Comm. Contemp. Sci. 2 (2000), 461-509
\item[] [31] \_\_\_\_, The equivalence of Seiberg-Witten and Casson invariants for homology 3-spheres, Math. Res. Lett. 6 (1999), 631-643
\item[] [32] J. Lin, D. Ruberman, N. Saveliev, A splitting theorem for the Seiberg-Witten invariant of a homology $S^{1} \times S^{3}$, Geom. Topol. 22 (2018), 2865-2942
\item[] [33] \_\_\_\_, On the Frøyshov invariant and monopole Lefschetz number. Preprint https://arxiv. org/abs/1802.07704 (2018).
\item[] [34] L. Ma, A surgery formula for the Casson-Seiberg-Witten invariant of integral homology $S^{1} \times$ $S^{3}$. Preprint https://arxiv.org/abs/1909.01533 (2019).
\item[] [35] \_\_\_\_, Fiber sum formulae for the Casson-Seiberg-Witten invariant of integral homology $S^{1} \times$ $S^{3}$, 2019. Preprint https://arxiv.org/abs/1910. 07683 (2019).
\item[] [36] C. Manolescu, Pin(2)-equivariant Seiberg-Witten Floer homology and the triangulation conjecture, J. Amer. Math. Soc. 29 (2016), 147-176
\item[] [37] R. Mazzeo, R. Melrose, Analytic surgery and the eta invariant, Geom. Funct. Anal. 5 (1995), 14-75
\item[] [38] R. Meyerhoff and D. Ruberman, Cutting and pasting and the $\eta$-invariant, Duke J. Math. 61 (1990), 747-761
\item[] [39] T. Mrowka, D. Ruberman, N. Saveliev, Seiberg-Witten equations, end-periodic Dirac operators, and a lift of Rohlin's invariant, J. Differential Geom. 88 (2011), 333-377
\item[] [40] D. Mullins, The generalized Casson invariant for 2-fold branched covers of $s^{3}$ and the Jones polynomial, Topology 32 (1993), 419-438
\item[] [41] W. D. Neumann and F. Raymond, Seifert manifolds, plumbing, $\mu$-invariant and orientation reversing maps, in "Algebraic and geometric topology (Proc. Sympos., Univ. California, Santa Barbara, Calif., 1977)", vol. 664 of Lecture Notes in Math., Springer, Berlin, 1978, 163-196
\item[] [42] L. I. Nicolaescu, "Notes on Seiberg-Witten theory", American Mathematical Society, Providence, RI, 2000.
\item[] [43] D. Ruberman and N. Saveliev, Casson-type invariants from the Seiberg-Witten equations. In 'New Ideas in Low-Dimensional Topology', L. Kauffman and V. Manturov, eds., vol. 56 of Series on Knots and Everything, World Scientific, Hackensack, NJ, 2015, 507-524
\item[] [44] \_\_\_\_, Rohlin's invariant and gauge theory I. Homology 3-tori, Comment. Math. Helv. 79 (2004), 618-646
\end{itemize}
\begin{itemize}
\item[] [45] \_\_\_\_, Rohlin's invariant and gauge theory II. Mapping tori, Geom. Topol. 8 (2004), 35-76
\item[] [46] R. Rustamov, On plumbed L-spaces. Preprint https://arxiv.org/abs/math/0505349 (2005).
\item[] [47] C. H. Taubes, Embedded contact homology and Seiberg-Witten Floer cohomology I, Geom. Topol. 14 (2010), 2297-2581
\item[] [48] \_\_\_\_, The Seiberg-Witten invariants and 4-manifolds with essential tori, Geom. Topol. 5 (2001), 441-519
\item[] [49] E. Witten, Monopoles and four-manifolds, Math. Res. Lett. 1 (1994), 769-796
Department of Mathematics
University of California, San Diego
La Jolla, CA 92093
Email address: jil063@ucsd.edu
Department of Mathematics, MS 050
Brandeis University
Waltham, MA 02454
Email address: ruberman@brandeis.edu
Department of Mathematics
University of Miami
PO Box 249085
Coral Gables, FL 33124
Email address: saveliev@math.miami.edu
\end{itemize}