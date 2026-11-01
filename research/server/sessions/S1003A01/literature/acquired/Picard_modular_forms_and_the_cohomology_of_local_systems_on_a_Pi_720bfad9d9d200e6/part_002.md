---
retention_scope: session
part: 2
total_parts: 4
---

[Part 2/4 of: Picard modular forms and the cohomology of local systems on a Picard modular surface]

In this part of the article we will study our spaces using their interpretation as moduli spaces of abelian threefolds with an action by $\rho$. This will give us a Deligne-Mumford stack defined over $\mathbb{Z}[\rho, 1 / 3]$, which enables us to find cohomological information through its finite fibres. Our goal is the $\ell$-adic Euler characteristics of the local systems on our moduli spaces as motives, or more specifically as representations of the absolute Galois group $\operatorname{Gal}(\bar{F} / F)$.
5.1. Picard modular stacks. For any scheme $S$ defined over $\mathcal{O}_{F}$ [1/3] consider the groupoid whose objects are tuples ( $A, \lambda, \iota$ ), where $A$ is an abelian scheme of relative dimension 3 over $S, \lambda: A \rightarrow A^{\vee}$ is a principle polarization of $A$, and $\iota: \mathcal{O}_{F} \rightarrow \operatorname{End}_{S}(A)$ is a homomorphism such that the Rosati involution associated to $\lambda$ acts by complex conjugation on $\iota\left(\mathcal{O}_{F}\right)$ and that gives $\Omega_{A / S}^{1}$ a structure of $\mathcal{O}_{S} \otimes_{\mathbb{Z}} \mathcal{O}_{F}$-module of signature (2, 1). Isomorphisms between $(A, \lambda, \iota)$ and $\left(A^{\prime}, \lambda^{\prime}, \iota^{\prime}\right)$ are given by isomorphisms $f: A \rightarrow A^{\prime}$ such that $\lambda=f^{\vee} \circ \lambda^{\prime} \circ f$ and $f \circ \iota(a)=\iota^{\prime}(a) \circ f$ for all $a \in \mathcal{O}_{F}$. This moduli problem is represented by a Deligne-Mumford stack $\mathcal{X}_{\Gamma}^{\prime}$ of relative dimension 2 that is separated, smooth, connected and of finite type over $\mathcal{O}_{F}[1 / 3]$, see [33, Cor. 1.4.1.12] and [34]. The Picard modular surface $X_{\Gamma}$ is equal to the complex fibre $\mathcal{X}_{\Gamma}^{\prime}(\mathbb{C})$.

Notation 5.1. Put $\alpha:=\iota(\rho)$.
To our moduli problem we now add the principal level-structure with respect to the endomorphism $1-\alpha$. Consider tuples ( $A, \lambda, \iota, \sigma$ ) where
$$\sigma:\left(\mathcal{O}_{F}^{3} /(1-\alpha) \mathcal{O}_{F}^{3}\right)_{S} \rightarrow A[1-\alpha]$$
is an $\mathcal{O}_{F}$-equivariant isomorphism, see [33, Definition 1.3.6.1]. This is represented by a Deligne-Mumford stack $\mathcal{X}_{\Gamma[\sqrt{-3}]}^{\prime}$ with the same properties as above and with $X_{\Gamma[\sqrt{-3}]}$ as complex fibre. Note that $\mathcal{X}_{\Gamma[\sqrt{-3}]}^{\prime}$ comes with an action of the finite group $\Gamma[\sqrt{-3}] / \Gamma$.

More generally, for any open compact subgroup of $G(\hat{\mathbb{Z}})$ we get a levelstructure that we can add to our moduli problem and get a stack with the same properties as above, see [33]. The open compact subgroup
$$K_{\Gamma}:=\left\{g \in G(\hat{\mathbb{Z}}): g \cdot \mathcal{O}_{F}^{3} \otimes_{\mathbb{Z}} \hat{\mathbb{Z}}=\mathcal{O}_{F}^{3} \otimes_{\mathbb{Z}} \hat{\mathbb{Z}}\right\},$$
corresponds to $\mathcal{X}_{\Gamma}^{\prime}$ and if we replace $G$ by $G^{0}$ in the definition we get $\mathcal{X}_{\Gamma_{1}}^{\prime}$. From the subgroup
$$K_{\Gamma[\sqrt{-3}]}:=\left\{g \in G(\hat{\mathbb{Z}}):(g-1) \cdot \mathcal{O}_{F}^{3} \otimes_{\mathbb{Z}} \hat{\mathbb{Z}} \subset \sqrt{-3} \cdot \mathcal{O}_{F}^{3} \otimes_{\mathbb{Z}} \hat{\mathbb{Z}}\right\},$$
we get $\mathcal{X}_{\Gamma[\sqrt{-3}]}^{\prime}$, and replacing $G$ by $G^{0}$ we get $\mathcal{X}_{\Gamma_{1}[\sqrt{-3}]}^{\prime}$, with the corresponding Picard modular surfaces as complex fibres.
5.2. Shimura varieties and complex tori. We briefly revisit our Picard modular surfaces as Shimura varieties and as moduli space of complex tori. For any compact open subgroup $K$ in $G\left(\mathbb{A}_{f}\right)$ put,
$$S_{K}(G, B):=G(\mathbb{Q}) \backslash B \times G\left(\mathbb{A}_{f}\right) / K .$$
This is a Shimura variety defined over $\mathbb{C}$. Taking $K$ equal to any of the compact open subgroups of the previous section we get a connected Shimura variety isomorphic to the corresponding Picard modular surface, see [21].

An abelian variety $A$ in $\mathcal{X}_{\Gamma}^{\prime}(\mathbb{C})$ is a complex torus $V / \Gamma_{*}$ with $\Gamma_{*}$ an $\mathcal{O}_{F}$ -module of rank 3 . Since the class number is 1 , the lattice $\Gamma_{*}$ is isomorphic to $\mathcal{O}_{F}^{3}$. The polarization of $A$ gives rise to an alternating form $E$ on the
underlying real vector space of $V$ which satisfies $E(J x, J y)=E(x, y)$ with $J$ the complex structure on $V$. This gives that $E(\alpha x, y)=E\left(x, \alpha^{\prime} y\right)$ for all $\alpha \in \mathcal{O}_{F}$ and where $z \mapsto z^{\prime}$ denotes the Galois automorphism of $F / \mathbf{Q}$. The corresponding hermitian form $h$ may be normalized (see [45]) so that
$$h\left(z_{1}, z_{2}, z_{3}\right)=z_{1} z_{2}^{\prime}+z_{1}^{\prime} z_{2}+z_{3} z_{3}^{\prime} .$$
5.3. Moduli spaces of curves. The Torelli map that sends a smooth curve of genus $g$ to its Jacobian, induces an embedding of coarse moduli spaces. For the corresponding stacks this does not hold in general due to the fact that if $G$ is the automorphism group of a non-hyperelliptic curve $C$, then the automorphism group of its Jacobian equals $G \times\{-1\}$.

An abelian threefold is either geometrically indecomposable, or a product of the Jacobian of a smooth genus two curve and an elliptic curve, or an unordered product of three elliptic curves. We cut up our spaces $\mathcal{X}_{\Gamma_{*}}^{\prime}$, for all $\Gamma_{*}$ among the four groups $\Gamma, \Gamma_{1}, \Gamma[\sqrt{-3}]$ and $\Gamma_{1}[\sqrt{-3}]$, into three pieces $\mathcal{X}_{1, \Gamma_{*}}^{\prime}, \mathcal{X}_{2, \Gamma_{*}}^{\prime}$ and $\mathcal{X}_{3, \Gamma_{*}}^{\prime}$ according to this distinction.

We will now shift focus to the corresponding moduli spaces of curves $\mathcal{X}_{\Gamma_{*}}$, defined over $\mathbb{Z}[\rho, 1 / 3]$. The stratification on the moduli of abelian varieties induces via Torelli a stratification on the moduli of curves, denoted by $\mathcal{X}_{1, \Gamma_{*}}$, $\mathcal{X}_{2, \Gamma_{*}}$ and $\mathcal{X}_{3, \Gamma_{*}}$.

The space $\mathcal{X}_{\Gamma}$ will then be the moduli space of curves of compact type together with an automorphism of order three, with action of type (2, 1), that induces an admissible tricyclic cover of the projective line (compare the definitions in [1]). The level structure for $\Gamma[\sqrt{-3}]$ will be described in terms of markings of points on the curves. We will not attempt an analogous description for $\Gamma_{1}[\sqrt{-3}]$.

Define also, in a completely analogous way, the moduli space $\mathcal{X}_{\Gamma_{*}}^{(2)}$ of abelian surfaces with signature $(1,1)$ and the moduli space $\mathcal{X}_{\Gamma_{*}}^{(1)}$ of elliptic curves with signature (1, 0).

The two spaces $\mathcal{X}_{\Gamma_{*}}$ and $\mathcal{X}_{\Gamma_{*}}^{\prime}$ only differ for the open strata of geometrically indecomposable abelian threefolds, due to the difference in automorphism group mentioned above. This is intimately connected to the fact that a geometrically indecomposable abelian threefold is either the Jacobian of a smooth curve of genus three, or the (-1)-twist of the Jacobian of a (non-hyperelliptic) smooth curve of genus three.

Our main interest is the cohomology of local systems of these spaces, and in Remark 7.5 we will relate the cohomology of these two types of spaces. This relation shows that there are no new motives appearing in the cohomology of local systems on $\mathcal{X}_{\Gamma_{*}}$ other than the ones appearing for $\mathcal{X}_{\Gamma_{*}}^{\prime}$. This is in sharp contrast to the situation when comparing the cohomology of local systems on the moduli space of curves $\mathcal{M}_{3}$ and the moduli space of principally polarized abelian varieties $\mathcal{A}_{3}$, see [8].

Notation 5.2. Let $K$ denote a field, which is not of characteristic 3, containing a primitive third root of unity $\tilde{\rho}$ that we fix.
5.4. Smooth curves of genus 3. Let $C / K$ be a smooth curve of genus 3 and let $\alpha$ be an automorphism of $C$ of order 3 of type (2, 1), which means that it will have eigenvalues ( $\tilde{\rho}, \tilde{\rho}, \tilde{\rho}^{2}$ ) when acting on the 3-dimensional vector space $H^{0}\left(C, \Omega_{C}^{1}\right)$.

Since there are no invariant differentials of $\alpha$ we see that $\alpha$ induces a cyclic triple cover of $\mathbb{P}^{1} \cong C / \alpha$. The Riemann-Hurwitz formula tells us that there are five ramification points, which is the same as fixed points of $\alpha$. Let $c_{\tilde{\rho}^{i}}$ be the number of ramification points $x$ such that the action of $\alpha$ on $\Omega_{C, x}^{1}$ is by multiplication by $\tilde{\rho}$. We then have that $c_{\tilde{\rho}^{2}}=5-c_{\tilde{\rho}}$. The Woods-Hole formula, together with the isomorphism between $H^{1}\left(C, \mathcal{O}_{C}\right)$ and the dual of $H^{0}\left(C, \Omega_{C}^{1}\right)$, tells us that
$$\sum_{i=0}^{1}(-1)^{i} \operatorname{Tr}\left(\alpha, H^{i}\left(C, \mathcal{O}_{C}\right)\right)=1-\left(\tilde{\rho}+2 \tilde{\rho}^{2}\right)=\frac{c_{\tilde{\rho}}}{1-\tilde{\rho}}+\frac{c_{\tilde{\rho}^{2}}}{1-\tilde{\rho}^{2}}$$
giving $c_{\tilde{\rho}}=4$.
Elementary Galois theory tells us that a cyclic triple cover of $\mathbb{P}^{1}$, with coordinate $x$, can be given by an equation $y^{3}=f(x)$ with cover given by $(x, y) \mapsto x$, together with the automorphism $\alpha:(x, y) \mapsto(x, \tilde{\rho} y)$, and where $f(x)$ does not contain any irreducible factor to the power larger than two. The space $H^{0}\left(C, \Omega_{C}^{1}\right)$ of regular differentials of $C$ is generated by $\left\{d x / y, d x / y^{2}, x d x / y^{2}\right\}$ and the eigenvalues of $\alpha$ are thus of the right form, $\left(\tilde{\rho}^{2}, \tilde{\rho}, \tilde{\rho}\right)$ on the given basis. The ramification point for which the action of $\alpha$ is by $\tilde{\rho}^{2}$ is necessarily defined over $K$ and using a projective transformation we put it in infinity. The polynomial $f(x)$ should then have four distinct roots over $\bar{K}$ and since the action on the ramification is by $\tilde{\rho}$ the polynomial should be square-free.

Remark 5.3. Doing the above in more generality, we begin with a covering $y^{3}=f_{1} f_{2}^{2}$, with square-free polynomials $f_{1}, f_{2}$. If the field is not too small we use a projective transformation to make sure that the point over infinity is not ramified, i.e that 3 divides $\operatorname{deg}(f)=2(g+2)-\operatorname{deg}\left(f_{1}\right)$. As above, we then find that the action of $\alpha$ on $H^{0}\left(C, \Omega_{C}^{1}\right)$ is of type $((g-1+d) / 3,(2 g+1-d) / 3)$.

Let $P_{d}(K) \subset K[x]$ be the subset consisting of polynomials of degree $d$ with non-zero discriminant. To each $f \in P_{4}(K)$ we associate the cyclic triple cover $\left(C_{f}, \alpha\right)$ given by the equation $y^{3}=f(x)$. The isomorphisms between pairs of the form $\left(C_{f}, \alpha\right)$ are given by $(x, y) \mapsto(a x+b, c y)$ with $a, c \in K^{*}$ and $b \in K$. The groupoid of pairs $\left(C_{f}, \alpha\right)$ with $f \in P_{4}(K)$ is equivalent to the groupoid $\mathcal{X}_{1, \Gamma}(K)$.
5.4.1. Ramification and $(1-\alpha)$-torsion. The 3-torsion group of an abelian threefold $A$ in $\mathcal{X}_{\Gamma[\sqrt{-3}]}^{\prime}(K)$ is isomorphic to $(\mathbb{Z} / 3 \mathbb{Z})^{6}$ over $\bar{K}$. We have that
$3=(1-\alpha)\left(1-\alpha^{2}\right)$ and the $(1-\alpha)$-torsion group (which equals the $\left(1-\alpha^{2}\right)$ -torsion group) is isomorphic to $(\mathbb{Z} / 3 \mathbb{Z})^{3}$ over $\bar{K}$. This is a totally isotropic subspace of the 3-torsion group with respect to the Weil pairing and an isomorphism $A[1-\alpha] \cong(\mathbb{Z} / 3 \mathbb{Z})^{3}$ is acted upon by $\mathrm{O}(h, \mathbb{Z} / 3 \mathbb{Z})$, the group of orthogonal matrices with coefficients in $\mathbb{Z} / 3 \mathbb{Z}$ that respect the hermitian form $h$ from Section 2.1. This group is isomorphic to $\Gamma / \Gamma[\sqrt{-3}] \cong \mathfrak{S}_{4} \times \mu_{2}$, c.f. [18, p. 153].

Take a pair $\left(C_{f}, \alpha\right)$ as in the previous section and let $p_{1}, p_{2}, p_{3}, p_{4}$ be the ramification points (not necessarily defined over $K$ ) where $\alpha$ acts by $\tilde{\rho}$ and let $p_{0}$ be the point where it acts by $\tilde{\rho}^{2}$. The degree 0 divisors $\beta_{1}=p_{1}-p_{0}$, $\beta_{2}=p_{2}-p_{0}$ and $\beta_{3}=p_{3}-p_{0}$ are points on the Jacobian of our curve which are fixed by $\alpha$, that is, they belong to $J\left(C_{f}\right)[1-\alpha]$.

The morphism
$$\phi:(\mathbb{Z} / 3 \mathbb{Z})^{3} \rightarrow J\left(C_{f}\right)[1-\alpha]$$
defined by $\left(c_{1}, c_{2}, c_{3}\right) \mapsto c_{1} \beta_{1}+c_{2} \beta_{2}+c_{3} \beta_{3}$ is an isomorphism. A non-trivial element in the kernel of $\phi$ can easily be rearranged using
$$\operatorname{div}(y)=\sum_{i=1}^{4}\left(p_{i}-p_{0}\right)$$
and the relations $3 p_{i} \sim 3 p_{0}$ for all $i$, to a relation of the form $p_{i}+p_{j} \sim p_{k}+p_{l}$ for some $i, j, k, l$. This relation implies that the curve is hyperelliptic which is not possible, see Remark 5.4 below. If we order the points $p_{1}, p_{2}, p_{3}$, $p_{4}$ then we have an action of $\mathfrak{S}_{4}$ on $J\left(C_{f}\right)[1-\alpha]$. This action corresponds to the group $\operatorname{SO}(h, \mathbb{Z} / 3 \mathbb{Z})$. And if we add the action $\beta_{i} \mapsto-\beta_{i}$ we get the whole $\mathrm{O}(h, \mathbb{Z} / 3 \mathbb{Z})$.

The groupoid $\mathcal{X}_{1, \Gamma[\sqrt{-3}]}(K)$ is equivalent to the groupoid of pairs $\left(C_{f}, \alpha\right)$ together with an ordering of the four ramification points where $\alpha$ acts by $\tilde{\rho}$.

Remark 5.4. A smooth curve $C$ of genus 3 which is a cyclic triple cover of $\mathbb{P}^{1}$ of degree 3 is not hyperelliptic. Indeed, if $\tau$ denotes the hyperelliptic involution, then $\tau$ and $\alpha$ commute, and $\alpha$ permutes the eight fixed points of $\tau$, and vice versa. In particular, since $\alpha$ has an unique fixed point $p_{0}$, where it acts by $\tilde{\rho}^{2}$, we see that $\tau$ also has to fix $p_{0}$. Since $8 \equiv_{3} 2$, the action of $\alpha$ must have at least one more fixed point among the fixed points of $\tau$, say $p_{1}$. Then $p_{0}-p_{1}$ defines a point in the kernel of both the endomorphism 2 and $(1-\alpha)\left(1-\alpha^{2}\right)=3$ of the Jacobian of $C$, hence $p_{0} \sim p_{1}$, a contradiction.
5.5. Smooth curves of genus 2. Arguing as in Section 5.4, a curve $C$ of genus 2 together with an automorphism $\alpha$ of order 3 inducing a cyclic cover of $\mathbb{P}^{1}$ can be given on the form $y^{3}=f_{1}(x) f_{2}(x)^{2}$ with $f_{1}$ and $f_{2}$ being relatively prime square-free polynomials for which $\left(\operatorname{deg} f_{1}, \operatorname{deg} f_{2}\right)=(2,2),(2,1)$ or $(1,2)$ and where $\alpha:(x, y) \mapsto(x, \tilde{\rho} y)$ has eigenvalues $\left(\tilde{\rho}, \tilde{\rho}^{2}\right)$ on $H^{0}\left(C, \Omega_{C}^{1}\right)$. Denote the curve corresponding to $f_{1}$ and $f_{2}$ by $C_{f_{1}, f_{2}}$. The isomorphisms between pairs of the form $\left(C_{f_{1}, f_{2}}, \alpha\right)$ are generated by $\operatorname{PGL}_{2}(K)$ acting on $x$ together with $y \mapsto a y$ for any $a \in K^{*}$.

Let $p_{1}, p_{2}$ be the points above the roots of $f_{1}$ and $q_{1}, q_{2}$ be the points above the roots of $f_{2}$. They are related by $p_{1}+p_{2} \sim q_{1}+q_{2}$. The divisors $\beta_{1}=p_{1}-p_{2}$ and $\beta_{2}=q_{1}-q_{2}$ give a basis of the ( $1-\alpha$ )-torsion of the Jacobian of $C_{f_{1}, f_{2}}$.

The groupoid $\mathcal{X}_{\Gamma[\sqrt{-3}]}^{(2)}(K)$ is equivalent to the groupoid of pairs $\left(C_{f_{1}, f_{2}}, \alpha\right)$ together with an ordering of the pair $p_{1}$ and $p_{2}$ and the pair $q_{1}$ and $q_{2}$ of ramification points of $\alpha$. The group $(\mathbb{Z} / 2 \mathbb{Z})^{2}$ acts on this moduli space by switching $p_{1}$ and $p_{2}$ respectively $q_{1}$ and $q_{2}$.
5.6. Elliptic curves. Let $E$ be an elliptic curve with an automorphism $\alpha$ of order 3 inducing a cyclic cover of $\mathbb{P}^{1}$ and let the origin be a fixed point of $\alpha$. Arguing again as in Section 5.4, such a curve can be given on the form $y^{3}=f(x)^{t}$ with $t=1$ or 2, $f$ a square-free polynomial of degree 2, $\alpha:(x, y) \mapsto(x, \tilde{\rho} y)$, and where the origin is placed over infinity. The action of $\alpha$ on $H^{0}\left(C, \Omega_{C}^{1}\right)$ has eigenvalue $\tilde{\rho}^{t}$. For a fixed $t$, the isomorphisms between pairs of the form $\left(C_{f^{t}}, \alpha\right)$ are generated by $x \mapsto a x+b$ and $y \mapsto c y$ for any $a, c \in K^{*}$ and $b \in K$.

If $K$ is algebraically closed then the (coarse) moduli space $\mathcal{X}_{\Gamma}^{(1)}(K)$, which corresponds to $t=1$, consists of one point. This point can be represented by $f(x)=x^{2}+x$.

Let $r_{1}, r_{2}$ be the points above the roots of $f$. The divisor $r_{1}-r_{2}$ gives a basis for the $(1-\alpha)$-torsion points. The groupoid $\mathcal{X}_{\Gamma[\sqrt{-3}]}^{(1)}(K)$ is equivalent to the groupoid of pairs $\left(C_{f}, \alpha\right)$ together with an ordering of the pair $r_{1}$ and $r_{2}$. The group $\mathbb{Z} / 2 \mathbb{Z}$ acts on this moduli space by switching $r_{1}$ and $r_{2}$. This is also the effect of the involution -1 on $E$, and so if $K$ is a algebraically closed field then the (coarse) moduli space $\mathcal{X}_{\Gamma[\sqrt{-3}]}^{(1)}(K)$ also consists of one point.
5.7. A smooth genus 2 curve joined with an elliptic curve. A curve $C$ in $\mathcal{X}_{2, \Gamma}(K)$ consists of a curve $C_{f_{1}, f_{2}}$ in $\mathcal{X}_{\Gamma}^{(2)}(K)$ and $C_{f}$ in $\mathcal{X}_{\Gamma}^{(1)}(K)$ joined at a ramification point of each curves. The ramification point of $C_{f_{1}, f_{2}}$ should be above a root of $f_{2}$ and the ramification point of $C_{f}$ should be above infinity (isomorphisms are induced by the ones of the individual curves that fixes these points). This leaves us, as we want, with four fixed points of $\alpha$ with eigenvalue $\tilde{\rho}$ acting on the tangent space, and one with $\tilde{\rho}^{2}$. It is then straightforward to see that the groupoid $\mathcal{X}_{2, \Gamma[\sqrt{-3}]}(K)$ is given by adding an ordering of the four fixed points.
5.8. Triples of elliptic curves. A curve in $\mathcal{X}_{3, \Gamma}(K)$ has three components, two curves $C_{f_{1}}, C_{f_{2}}$ in $\mathcal{X}_{\Gamma}^{(1)}(K)$ together with a curve of the form $C_{f_{3}^{2}}$ corresponding to a curve $C_{f_{3}}$ in $\mathcal{X}_{\Gamma}^{(1)}(K)$. The two curves $C_{f_{1}}, C_{f_{2}}$ are joined to the curve $C_{f_{3}^{2}}$ at a ramification point over infinity and at a ramification point over one of the roots of $f_{3}$. This leaves us again with the wanted four fixed points of $\alpha$ with eigenvalue $\tilde{\rho}$ acting on the tangent space, and one
with $\tilde{\rho}^{2}$, and the groupoid $\mathcal{X}_{3, \Gamma[\sqrt{-3}]}(K)$ is given by adding an ordering of the four fixed points.
5.9. Stable admissible covers. Let us briefly discuss a compactification, of the moduli space $\mathcal{X}_{\Gamma[\sqrt{-3}]}$ using degenerations of cyclic covers.

Let $\tilde{\mathcal{X}}_{\Gamma[\sqrt{-3}]}$ be the moduli space defined over $\mathbb{Z}[\rho, 1 / 3]$ of stable marked admissible $\mathbb{Z} / 3$-covers of (stable) curves of genus 0 with action of type (2, 1). For the definition of admissible covers, see [26] (and compare with [1]). An element of $\tilde{\mathcal{X}}_{\Gamma[\sqrt{-3}]}(K)$ is a nodal curve $C$ over $K$ of genus 3 with an action $\alpha$ of an automorphism of order 3 with $C / \alpha$ isomorphic to a curve $P$ of genus 0, stably marked by the ramification points $p_{0}, p_{1}, \ldots, p_{4}$ of the cover $C \rightarrow P$ and such that $\alpha$ acts by $\tilde{\rho}$ on the tangent space of the points above $p_{1}, \ldots, p_{4}$ and by $\tilde{\rho}^{2}$ on the point above $p_{0}$.

There is a morphism
$$\tilde{\mathcal{X}}_{\Gamma[\sqrt{-3}]} \rightarrow \overline{\mathcal{M}}_{0,1+4},$$
with $\overline{\mathcal{M}}_{0,1+4}$ the moduli space of (1 + 4)-pointed genus 0 curves.
Note that $\overline{\mathcal{M}}_{0,1+4}$ has a stratification with five strata according to the topological type of the genus 0 curve: a 2-dimensional open stratum $\mathcal{M}_{0,1+4}$, two 1-dimensional strata corresponding to a join $P_{1}, P_{2}$ of two $\mathbb{P}^{1}$ 's intersecting in a point with marked points $p_{0}, p_{1}, p_{2}$ on $P_{1}$ and $p_{3}, p_{4}$ on $P_{2}$, or $p_{0}, p_{1}$ on $P_{1}$ and $p_{2}, p_{3}, p_{4}$ on $P_{2}$ and finally two strata each consisting of one point corresponding to a linear chain of three $\mathbb{P}^{1}$ 's, $P_{1}, P_{2}, P_{3}$ with marked points $p_{1}, p_{2}$ on $P_{1}, p_{0}$ on $P_{2}$ and $p_{3}, p_{4}$ on $P_{3}$, or $p_{0}, p_{1}$ on $P_{1}, p_{2}$ on $P_{2}$ and $p_{3}, p_{4}$ on $P_{3}$ (all described up to the action of $\mathfrak{S}_{4}$ ).

This will induce a stratification of $\tilde{\mathcal{X}}_{\Gamma[\sqrt{-3}]}$. The first three cases above correspond to $\mathcal{X}_{1, \Gamma[\sqrt{-3}]}, \mathcal{X}_{2, \Gamma[\sqrt{-3}]}$ and $\mathcal{X}_{3, \Gamma[\sqrt{-3}]}$ respectively.

The fourth strata is 1-dimensional and the curves it parametrizes consist of an elliptic curve $C_{1}$ with an order 3 automorphism $\alpha_{1}$ with action of type $(1,0)$ and a rational curve $C_{0}=\mathbb{P}^{1}$ with an automorphism $\alpha_{0}$ that acts by $x \mapsto \rho x$, joined by identifying the three points of an $\alpha_{1}$-orbit of length 3 to the points $1, \tilde{\rho}, \tilde{\rho}^{2}$ on $C_{0}$. There are four components depending upon the choice of marking of the ramification point on the rational curve.

The fifth strata is 0-dimensional and the curves it parametrizes consist of an union of an elliptic curve $C_{1}$ with an order 3 automorphism $\alpha_{1}$ with action of type $(1,0)$ and two $\mathbb{P}^{1}$ 's with automorphism $x \mapsto 1 /(1-x)$, say $C_{0}$ and $C_{0}^{\prime}$, that intersect each other in 0, 1 and $\infty$ such that $C_{1}$ and $C_{0}^{\prime}$ are disjoint, while $C_{1}$ and $C_{0}$ intersect in a fixed point of $\alpha_{1}$. This strata consists of twelve points depending upon the choice of marking of the ramification points on the two rational curves.

Let $\mathcal{X}_{\Gamma[\sqrt{-3}]}^{*}$ denote the Satake-Baily-Borel compactification of $\mathcal{X}_{\Gamma[\sqrt{-3}]}^{\prime}$ defined over $\mathbb{Z}[\rho, 1 / 3]$, and so,
$$\mathcal{X}_{\Gamma[\sqrt{-3}]}^{*}(\mathbb{C}) \cong X_{\Gamma[\sqrt{-3}]}^{*} .$$

Sending a curve to its (generalized) Jacobian gives a morphism,
$$\tilde{\mathcal{X}}_{\Gamma[\sqrt{-3}]} \rightarrow \mathcal{X}_{\Gamma[\sqrt{-3}]}^{*} .$$
The Jacobians over the fourth and fifth strata become extensions of an elliptic curve with the multiplicative group $\mathbb{G}_{m, F}$, and these strata will furthermore constitute a $\mathbb{P}^{1}$-bundle over the four cusps of $\mathcal{X}_{\Gamma[\sqrt{-3}]}^{*}$.

\section*{6. Characteristic polynomials of Frobenius}

In this section we find properties of the characteristic polynomial of Frobenius acting on $\rho$-eigenspaces of the first étale cohomology group of a cyclic triple cover of the projective line.
6.1. Notation for primes, generators and finite fields. Let $k=\mathbb{F}_{q}$ always denote a finite field with $q=p^{r}$ elements with $q \equiv_{3} 1$. For any $n \geq 1$ let $k_{n}=\mathbb{F}_{q^{n}}$, a degree $n$ extension of $k$.

If $p \equiv_{3} 1$, choose a third root of unity $\tilde{\rho}$ in $\mathbb{F}_{p}$. This gives us a third root $\tilde{\rho}$ in any extension field $k=\mathbb{F}_{q}$ for $q=p^{r}$. The choice of $\tilde{\rho}$ determines a generator $a_{\mathfrak{p}_{p}}+b_{\mathfrak{p}_{p}} \rho$ of an ideal $\mathfrak{p}_{p}$ of norm $p$, namely let $a_{\mathfrak{p}_{p}}, b_{\mathfrak{p}_{p}}$ be the unique pair of integers such $a_{\mathfrak{p}_{p}}^{2}-a_{\mathfrak{p}_{p}} b_{\mathfrak{p}_{p}}+b_{\mathfrak{p}_{p}}^{2}=p, a_{\mathfrak{p}_{p}} \equiv_{3} 1, b_{\mathfrak{p}_{p}} \equiv_{3} 0$ and such that an (hence any) isomorphism between $\mathbb{Z}[\rho] / \mathfrak{p}_{p}$ and $k=\mathbb{F}_{p}$, sends $\rho$ to $\tilde{\rho}$. Define the integers $a_{\mathfrak{p}_{q}}, b_{\mathfrak{p}_{q}}$ by the equation $a_{\mathfrak{p}_{q}}+b_{\mathfrak{p}_{q}} \rho=\left(a_{\mathfrak{p}_{p}}+b_{\mathfrak{p}_{p}} \rho\right)^{r}$ and define the ideal $\mathfrak{p}_{q}=\left(a_{\mathfrak{p}_{q}}+b_{\mathfrak{p}_{q}} \rho\right)$.

For any $p \equiv_{3} 2$ choose an arbitrary third root of unity $\tilde{\rho}$ in $\mathbb{F}_{p^{2}}$. For any even $r \geq 1$ choose an embedding of $\mathbb{F}_{p^{2}}$ in $k=\mathbb{F}_{p^{r}}$ and let the chosen third root of unity of $\mathbb{F}_{p^{r}}$ be the one coming from $\mathbb{F}_{p^{2}}$. Note that it is presence of the automorphism $x \mapsto x^{p}$ of $\mathbb{F}_{p^{2}}$ that makes that these choices do not matter for the later results for the moduli spaces, see Proposition 7.3. The ideal $\mathfrak{p}_{p}=(p)$ is prime in $\mathbb{Z}[\rho]$ and also here we also choose a generator $a_{\mathfrak{p}_{p}}+b_{\mathfrak{p}_{p}} \rho$ such that $a_{\mathfrak{p}_{p}} \equiv_{3} 1, b_{\mathfrak{p}_{p}} \equiv_{3} 0$, namely $a_{\mathfrak{p}_{p}}=-p$ and $b_{\mathfrak{p}_{p}}=0$. Define also $a_{\mathfrak{p}_{q}}=(-p)^{r}, b_{\mathfrak{p}_{q}}=0$ and the ideal $\mathfrak{p}_{q}=\left(a_{\mathfrak{p}_{q}}+b_{\mathfrak{p}_{q}} \rho\right)$.
6.2. The characteristic polynomial. Let $\chi$ denote the third power residue symbol, that is, if $a \in k^{*}$ then $\chi(a)=\rho^{i}$ where $\tilde{\rho}^{i}=a^{\frac{q-1}{3}}$, and $\chi(0)=0$. Let $C_{f}^{\prime}$ be a cyclic triple cover of the projective line given by an equation of the form $y^{3}=f(x)$, where $f$ is a cube-free polynomial with coefficients in $k$. With $f(\infty)$ we mean the leading coefficient of $f$ if $\operatorname{deg} f \equiv_{3} 0$, and 0 otherwise. Let $g$ be the genus of $C_{f}$. Put $C_{f}:=C_{f}^{\prime} \otimes_{k} \bar{k}$ and let $F_{q}$ denote the geometric Frobenius morphism acting on $C_{f}$. The number of points over $k$ of $C_{f}$ equals
$$\left|C_{f}(k)\right|=\left|C_{f}^{F_{q}}\right|=\sum_{a \in \mathbb{P}^{1}(k)}(1+\chi(f(a))+\overline{\chi(f(a))}) .$$

Let $H_{c}^{i}$ denote compactly supported $\ell$-adic étale cohomology. The Lefschetz trace formula (see [13, Th. 3.2]) tells us that
$$\left|C_{f}^{F}\right|=\sum_{i=1}^{2}(-1)^{i} \operatorname{Tr}\left(F_{q}, H_{c}^{i}\left(C_{f}, \overline{\mathbb{Q}}_{\ell}\right)\right)$$
and so
$$a_{1}\left(C_{f}\right):=\operatorname{Tr}\left(F_{q}, H_{c}^{1}\left(C_{f}, \overline{\mathbb{Q}}_{\ell}\right)\right)=-\sum_{a \in \mathbb{P}^{1}(k)}(\chi(f(a))+\overline{\chi(f(a))}) .$$

Let $\alpha$ be the automorphism of $C_{f}$ given by $(y, x) \mapsto(\tilde{\rho} y, x)$, which commutes with Frobenius. We find that
$$\left|C_{f}^{F_{q} \circ \alpha^{i}}\right|=\sum_{a \in \mathbb{P}^{1}(k)}\left(1+\rho^{i} \chi(f(a))+\overline{\rho^{i} \chi(f(a))}\right) .$$

The automorphism $\alpha$ splits $H_{c}^{j}\left(C_{f}, \overline{\mathbb{Q}}_{\ell}\right)$ into $\rho^{i}$-eigenspaces $H_{c}^{j}\left(C_{f}, \overline{\mathbb{Q}}_{\ell}\right)^{\rho^{i}}$. The projection formula gives,
$$\sum_{j=0}^{2}(-1)^{j} \operatorname{Tr}\left(F_{q}, H_{c}^{j}\left(C_{f}, \overline{\mathbb{Q}}_{\ell}\right)^{\rho^{i}}\right)=\frac{1}{3} \sum_{k=0}^{2} \rho^{-i k}\left|C_{f}^{F_{q} \circ \alpha^{k}}\right| .$$

The 1-dimensional cohomology groups $H_{c}^{0}$ and $H_{c}^{2}$ are $\alpha$-invariant. Since the quotient by $\alpha$ has genus 0, $H_{c}^{1}$ has no $\alpha$-invariant part. These two things can also be deduced using the Lefschetz trace formula for $\alpha$ together with the fact that $\alpha$ has $g+2$ fixed points (using the Hurwitz formula). It follows that
$$a_{1, \rho^{i}}\left(C_{f}\right):=\operatorname{Tr}\left(F_{q}, H_{c}^{1}\left(C_{f}, \overline{\mathbb{Q}}_{\ell}\right)^{\rho^{i}}\right)=-\sum_{a \in \mathbb{P}^{1}(k)} \chi(f(a))^{i} .$$
for $i=1,2$.
Let $\alpha_{1}\left(C_{f}\right), \ldots, \alpha_{g}\left(C_{f}\right)$ be the eigenvalues of Frobenius acting on the $g$ -dimensional vector space $H_{c}^{1}\left(C_{f}, \overline{\mathbb{Q}}_{\ell}\right)^{\rho}$ and denote the characteristic polynomial of Frobenius by $\mathfrak{c h}_{\rho}\left(C_{f}\right)$. Let $e_{i}$ denote the $i$ th elementary symmetric polynomial in $g$ variables. Note then that
$$e_{1}\left(\alpha_{1}\left(C_{f}\right), \ldots, \alpha_{g}\left(C_{f}\right)\right)=a_{1, \rho}\left(C_{f}\right) .$$
and that
$$\mathfrak{c h}_{\rho}\left(C_{f}\right)=\sum_{i=0}^{g} x^{g-i}(-1)^{i} e_{i}\left(\alpha_{1}\left(C_{f}\right), \ldots, \alpha_{g}\left(C_{f}\right)\right) .$$

Since $\alpha_{i}\left(C_{f}\right) \bar{\alpha}_{i}\left(C_{f}\right)=q$ for $1 \leq i \leq g$, we immediately get that
$$e_{g-i} q^{i}=e_{g} \bar{e}_{i} \quad \text { for } 1 \leq i \leq g .$$
6.2.1. Characteristic polynomials of elliptic curves. We will first consider the elliptic curves in some detail. Assume that $p \neq 2$. If $\gamma$ is a generator of $k^{*}$, then $y^{3}=x^{2}+\gamma^{i}$ for $i=0, \ldots, 5$ are representatives of the six $k$-isomorphism classes of curves in $\mathcal{X}_{\Gamma}^{(1)}(k)$.

Let $\nu$ denote the second power residue symbol. Using Jacobi sums (see for instance [29, Chapter 8]) we have
$$a_{1, \rho}\left(C_{x^{2}+D}\right)=\nu(-4 D) \chi(-4 D)(a+b \rho)$$
for any $D \in k^{*}$. Note that $-4 D$ is the discriminant of the polynomial $x^{2}+D$.
Say that $\sigma$ switches the two marked ramification points of a curve in $\mathcal{X}_{\Gamma[\sqrt{-3}]}^{(1)}(\bar{k})$. The fixed points of Frobenius composed with $\sigma$ acting on $\mathcal{X}_{\Gamma}^{(1)}(\bar{k})$ are the curves $y^{3}=x^{2}+D$ such that $\nu(-4 D)=1$.

Assume now that $p=2$. If $\gamma$ is a generator of $k^{*}$, then the following are representatives of the six $k$-isomorphism classes of curves in $\mathcal{X}_{\Gamma}^{(1)}(k), x^{2}+\gamma^{i} x$ for $i=0,1,2$ and $x^{2}+\gamma^{i} x+\delta_{i}$ for $i=0,1,2$ where $\delta_{i}$ is any element of $k$ such that the polynomial is irreducible.

For any $a \in k^{*}$ and $b \in k$, define $\nu_{a}(b)$ to be 1 if the equation $x^{2}+a x+b=0$ has two solutions in $k$, and -1 otherwise. Note first that $t^{2}+t+1$ has two roots, say $\alpha$ and $\beta$, in $k$ and that $t^{2}+a t+a^{2}$ has roots $a \alpha$ and $a \beta$, so in particular $\nu_{a}\left(a^{2}\right)=1$. Using that the Jacobi sum $J(\chi, \chi)$ equals $-a-b \rho$ we get
$$a_{1, \rho}\left(C_{x^{2}+a x+b}\right)=-\sum_{w} \chi\left(w^{2}+a w+b\right)=\nu_{a}(b) \chi\left(a^{2}\right)(a+b \rho) .$$
Note that $a^{2}$ is the discriminant of the polynomial $x^{2}+a x+b$. The fixed points of Frobenius composed with $\sigma$ acting on $\mathcal{X}_{\Gamma}^{(1)}(\bar{k})$ as above are the curves $y^{3}=x^{2}+a x+b$ such that $\nu_{a}(b)=1$.

Theorem 6.5 below is a generalization of the formulas (6.2) and (6.3), which go back to Gauss.
6.2.2. The characteristic polynomial modulo $1-\rho$. Let $p_{1}, \ldots, p_{g+2}$ be the roots of $f=f_{1} f_{2}^{2}$. The elements $\left(v_{1}, \ldots, v_{g}\right)$ with $v_{i}=p_{i}-p_{i+1}$ form a basis of the $g$-dimensional $\mathbb{Z} / 3 \mathbb{Z}$-vector space $J\left(C_{f}\right)[1-\alpha]$. Using the Tate module of $J\left(C_{f}\right)$ we see that the action of Frobenius on $H_{c}^{1}\left(C_{f}, \overline{\mathbb{Q}}_{\ell}\right)^{\rho}$ modulo $(1-\rho)$ is equal to the action of Frobenius on $J\left(C_{f}\right)[1-\alpha]$. Let $\mathfrak{c h}_{\rho}\left(C_{f}\right)_{\rho=1} \in(\mathbb{Z} / 3 \mathbb{Z})[x]$ denote the polynomial $\mathfrak{c h}_{\rho}\left(C_{f}\right)$ modulo $(1-\rho)$. This polynomial is then equal to the characteristic polynomial of Frobenius acting on $J\left(C_{f}\right)[1-\alpha]$.

Say that the Frobenius $F_{q}$ induces a permutation $\sigma \in S_{g+2}$, that has $c_{i}(\sigma)$ cycles of length $i$, on the set of points $\left\{p_{1}, \ldots, p_{g+2}\right\}$. We will now describe the $g \times g$-matrix $A_{\sigma}$ induced by $F_{q}$ acting on the basis $\left(v_{1}, \ldots, v_{g}\right)$ with $v_{i}=p_{i}-p_{i+1}$. Put $d_{1}=\operatorname{deg} f_{1}, d_{2}=\operatorname{deg} f_{2}$ and $\mathfrak{c h}\left(A_{\sigma}\right)=\operatorname{det}(x I-A)$.

Let us first handle the cases for which $c_{1}(\sigma) \geq 1$. In this case we can look at any $\sigma$ without it having to correspond to an actual curve. By reordering, we can assume that $g+2$ is fixed by $\sigma$. If $\sigma=(1, \ldots, g+1)(g+2)$ then
$F_{q}\left(v_{i}\right)=v_{i+1}$ for $i \leq g-1$ and $F_{q}\left(v_{g}\right)=-v_{1}-v_{2}-\ldots-v_{g}$. We find that $\mathfrak{c h}\left(A_{\sigma}\right)=\left(x^{g+1}-1\right) /(x-1)$. Say now that we have computed $A_{\tau}$ for some $\tau$ with $c_{1}(\tau) \geq 1$. If $\sigma$ consists of a cycle $(1, \ldots, h)$ followed by $\tau$ reordered such that $j$ is replaced by $j+h$, then $F_{q}\left(v_{i}\right)=v_{i+1}$ for $i \leq h-2$, $F_{q}\left(v_{h-1}\right)=-v_{1}-v_{2}-\ldots-v_{h}$ and $F_{q}\left(v_{h}\right)=v_{1}+v_{2}+\ldots+v_{h+1}$. If we define $B$ to be the $h \times h$-matrix given by $w_{i} \mapsto w_{i+1}$ for $i \leq h-2$, $w_{h-1} \mapsto-w_{1}-w_{2}-\ldots-w_{h}$ and $v_{h} \mapsto w_{1}+w_{2}+\ldots+w_{h}$ on a basis $\left(w_{1}, \ldots, w_{h}\right)$, then $\mathfrak{c h}\left(A_{\sigma}\right)=\mathfrak{c h}\left(A_{\tau}\right) \mathfrak{c h}(B)=\mathfrak{c h}\left(A_{\tau}\right)\left(x^{h}-1\right)$. This describes, by induction, the structure of $A_{\sigma}$ for any $\sigma$ with $c_{1}(\sigma) \geq 1$.

Example 6.1. For $\sigma=(1)(23)(4567)(8)$ we have
$$A_{\sigma}=\left(\begin{array}{cccccc}
1 & 1 & 0 & 0 & 0 & 0 \\
0 & -1 & 0 & 0 & 0 & 0 \\
0 & 1 & 1 & 1 & 0 & 0 \\
0 & 0 & 0 & 0 & 1 & 0 \\
0 & 0 & 0 & 0 & 0 & 1 \\
0 & 0 & 0 & -1 & -1 & -1
\end{array}\right)$$

Let us now handle the cases for which $c_{1}(\sigma)=0$. Reorder the points $p_{1}, \ldots, p_{g+2}$ such that the roots of $f_{1}$ come before the roots of $f_{2}$ and put $v_{g+1}=p_{g+1}-p_{g+2}$.

Note first that $3 p_{i} \sim 3 p_{j}$ for any $i, j$, and then that on the one hand
$$\operatorname{div}_{0}(y)=\sum_{i=1}^{d_{1}} p_{i}+\sum_{i=1+d_{1}}^{d_{1}+d_{2}} 2 p_{i}$$
and on the other
$$\operatorname{div}_{\infty}(y) \sim\left(d_{1}+2 d_{2}\right) p_{i},$$
for any $i$. If $d_{1} \equiv_{3} 0$ then this can be used to give the relation
$$\sum_{i=1}^{d_{1}} p_{i}+\sum_{i=1+d_{1}}^{d_{1}+d_{2}} 2 p_{i} \sim \sum_{i=1}^{d_{1} / 3} 3 p_{3 i-1}+\sum_{i=1+d_{1} / 3}^{d_{2} / 3} 6 p_{3 i-1}$$
from which it follows that
$$\sum_{i=1}^{d_{1} / 3}\left(v_{3 i-2}-v_{3 i-1}\right)+\sum_{i=1+d_{1} / 3}^{\left(d_{1}+d_{2}\right) / 3}\left(-v_{3 i-2}+v_{3 i-1}\right)=0 .$$

Similarly, if $d_{1} \equiv_{3} 1$ then
$$\sum_{i=1}^{\left(d_{1}-1\right) / 3}\left(v_{3 i-2}-v_{3 i-1}\right)+v_{d_{1}}+\sum_{i=1+\left(d_{1}-1\right) / 3}^{\left(d_{1}+d_{2}-2\right) / 3}\left(-v_{3 i}+v_{3 i+1}\right)=0,$$
and if $d_{1} \equiv_{3} 2$ then
$$\sum_{i=1}^{\left(d_{1}-2\right) / 3}\left(v_{3 i-2}-v_{3 i-1}\right)+v_{d_{1}-1}-v_{d_{1}}-v_{d_{1}+1}+\sum_{i=2+\left(d_{1}-2\right) / 3}^{\left(d_{1}+d_{2}-1\right) / 3}\left(-v_{3 i-1}+v_{3 i}\right)=0 .$$

We will now use the same reasoning as above. The difference is that if $\sigma$ contains the cycle $(s, \ldots, s+t-1)(s+t, s+t+1, \ldots, g+2)$ then $F_{q}\left(v_{g}\right)=v_{g+1}$ if $s+t \leq g$ and $F_{q}\left(v_{g}\right)=v_{s}+\ldots+v_{g+1}$ if $s+t=g+1$. We can express $v_{g+1}$ in terms of $v_{1}, \ldots, v_{g}$ using the formulas above, but we find that only the coefficients of $v_{t-1}, \ldots, v_{g}$ will affect $\mathfrak{c h}\left(A_{\sigma}\right)$. Using that $\sigma$ necessarily permutes the roots of $f_{1}$ and $f_{2}$ respectively, we find that the contribution of the cycles $(s, \ldots, s+t-1)(t, t+1, \ldots, g+2)$ to $\mathfrak{c h}\left(A_{\sigma}\right)$ equals $\left(x^{t}-1\right)\left(x^{g+2-s-t}-1\right) /(x-1)^{2}$.
Example 6.2. For $\sigma_{1}=(123)(456)$ and $\sigma_{2}=(12)(34)(56)$ we have
$$A_{\sigma_{1}}=\left(\begin{array}{cccc}
0 & 1 & 0 & 0 \\
-1 & -1 & 0 & 0 \\
1 & 1 & 1 & 1 \\
1 & -1 & 0 & 1
\end{array}\right), \quad A_{\sigma_{2}}=\left(\begin{array}{cccc}
-1 & 0 & 0 & 0 \\
1 & 1 & 1 & 0 \\
0 & 0 & -1 & 0 \\
1 & -1 & 1 & -1
\end{array}\right)$$

Summing up, we find the following.
Theorem 6.3. Let $C_{f}$ be a tricyclic cover of genus $g$. If Frobenius induces a permutation $\sigma$ on the set of $g+2$ ramification points with $c_{i}(\sigma)$ cycles of length $i$ then we have
$$\mathfrak{c h}{ }_{\rho}\left(C_{f}\right)_{\rho=1}=\mathfrak{c h}\left(A_{\sigma}\right)=\frac{1}{(x-1)^{2}} \prod_{i=1}^{g+2}\left(x^{i}-1\right)^{c_{i}(\sigma)}$$
as polynomials in $(\mathbb{Z} / 3 \mathbb{Z})[x]$.
Remark 6.4. Computing
$$a_{n, \rho}\left(C_{f}\right):=-\sum_{a \in \mathbb{P}^{1}\left(k_{n}\right)} \chi(f(a))=\sum_{i=1}^{g} \alpha_{i}\left(C_{f}\right)^{n} \in \mathbb{Z}[\rho]$$
modulo $1-\rho$ is more straightforward since
$$-\sum_{a \in \mathbb{P}^{1}\left(k_{n}\right)} \chi(f(a))=-\left(q^{n}+1-r_{i}\right)=1+r_{n} \quad \bmod (1-\rho),$$
where $r_{n}$ is the number of roots of $f$ defined over $k_{n}$.
6.2.3. The determinant of Frobenius. Say that $\alpha$ has $s$ eigenvalues equal to $\tilde{\rho}$ when acting on $H^{0}\left(C, \Omega_{C}^{1}\right)$. It then follows from [20, Thèoreme 1] that $e_{g}$ generates the ideal $\mathfrak{p}_{q}^{s} \cdot\left(\overline{\mathfrak{p}_{q}}\right)^{g-s}$ and hence
$$e_{g}\left(\alpha_{1}\left(C_{f}\right), \ldots, \alpha_{g}\left(C_{f}\right)\right)=(-1)^{j_{1}} \rho^{j_{2}}\left(a_{\mathfrak{p}_{p}}+b_{\mathfrak{p}_{p}} \rho\right)^{r s}\left(a_{\mathfrak{p}_{p}}+b_{\mathfrak{p}_{p}} \rho^{2}\right)^{r(g-s)}$$
for some integers $j_{1}$ and $j_{2}$.
Theorem 6.5. For any polynomial $h$, let $D(h)$ denote the discriminant of $h$, and $\epsilon(h)$ the number of irreducible factors (over $k$ ) of $h$. If we assume that $f=f_{1} f_{2}^{2}$ and $3 \mid \operatorname{deg} f$ then
$$\frac{e_{g}\left(\alpha_{1}\left(C_{f}\right), \ldots, \alpha_{g}\left(C_{f}\right)\right)}{\left(a_{\mathfrak{p}_{p}}+b_{\mathfrak{p}_{p}} \rho\right)^{r s}\left(a_{\mathfrak{p}_{p}}+b_{\mathfrak{p}_{p}} \rho^{2}\right)^{r(g-s)}}=(-1)^{g+\epsilon\left(f_{1}\right)+\epsilon\left(f_{2}\right)} \chi\left(D\left(f_{1}\right)\right) \overline{\chi\left(D\left(f_{2}\right)\right)} .$$

Remark 6.6. Note that if $p \neq 2$, then by Stickelberger's theorem (see [10, Thm 1.3] or [11])
$$(-1)^{g+\epsilon\left(f_{1}\right)+\epsilon\left(f_{2}\right)}=\nu\left(D\left(f_{1}\right) D\left(f_{2}\right)\right)=\nu\left(D\left(f_{1}\right)\right) \overline{\nu\left(D\left(f_{2}\right)\right)},$$
where $\nu$ denotes the second power residue symbol.
Proof. Since, $e_{g}\left(\alpha_{1}\left(C_{f}\right), \ldots, \alpha_{g}\left(C_{f}\right)\right)=(-1)^{j_{1}}$ modulo $(1-\rho)$, Theorem 6.3 tells us immediately that $j_{1}=g+\epsilon\left(f_{1}\right)+\epsilon\left(f_{2}\right)$.

The action of Frobenius on $H_{c}^{1}\left(C_{f}, \overline{\mathbb{Q}}_{\ell}\right)^{\rho}$ modulo $1-\rho$ is equal to the action on $J\left(C_{f}\right)[1-\alpha]$. To determine $j_{2}$ it suffices to calculate the expression (6.4) modulo 3 since it equals $(-1)^{j_{1}}(1-\theta)^{j_{2}}$ in $\mathcal{O}_{F} /(3) \cong \mathbb{F}_{3}[\theta]$ with $\theta=$ $1-\rho(\bmod 3)$. That means that it suffices to calculate the determinant of Frobenius on the $\mathbb{F}_{3}[\theta]$-module $J\left(C_{f}\right)[3]$. In view of the exact sequence
$$0 \rightarrow J\left(C_{f}\right)[1-\alpha] \rightarrow J\left(C_{f}\right)[3] \xrightarrow{1-\alpha} J\left(C_{f}\right)[1-\alpha] \rightarrow 0$$
and the fact that $J\left(C_{f}\right)[1-\alpha]$ is isotropic for the Weil pairing, as kernel of an endomorphism, we see that the action of $\alpha$ on $C_{f}$ induces a cyclic $\mu_{3}$ -action on the three possibilities for this determinant. (If we lift our abelian variety together with $\alpha$ to $\mathbb{C}$ then this action corresponds to the action of $\operatorname{diag}(1,1, \rho) \in \Gamma[\sqrt{-3}]$.) The determinant of Frobenius on $J\left(C_{f}\right)[3]$ is determined up to a third root of 1 by the level structure $J\left(C_{f}\right)[1-\alpha] \sim$ $\left(\mathcal{O}_{F} /(1-\alpha)\right)^{3}$.

The moduli stack of triples ( $J, l, d$ ) with $J$ a Jacobian of a cyclic triple cover $C_{f} \rightarrow \mathbb{P}^{1}$ of signature $(s, g-s)$ with a level $(1-\alpha)$-structure $l$ on $J\left(C_{f}\right)[1-\alpha]$ and the determinant $d$ of the cohomology modulo 3, is a threefold étale cover of the moduli stack of tuples $(J, l)$. It is étale since the ramification points of the cover $C_{f} \rightarrow \mathbb{P}^{1}$ determine the level $(1-\alpha)$-structure and $\alpha$ then induces the $\mu_{3}$-action. This degree three cover extends to the appropriate moduli stacks (Picard modular stacks, see 5.1) of principally polarized abelian varieties with level structure.

In the case of $g=3$ and the covers considered in subsection 5.4 this étale cover is given by the $\mu_{3}$-cover $\mathcal{X}_{\Gamma_{1}[\sqrt{-3}]} \rightarrow \mathcal{X}_{\Gamma[\sqrt{-3}]}$ which is étale outside the locus where the discriminant of $f$ vanishes. Indeed, we know that this cover $\mathcal{X}_{\Gamma_{1}[\sqrt{-3}]} \rightarrow \mathcal{X}_{\Gamma[\sqrt{-3}]}$ is the cover defined over $\mathcal{O}_{F}$ by equation (2.1), see also Prop. 2.2. Therefore the action of Frobenius on the fibres of $\mathcal{X}_{\Gamma_{1}[\sqrt{-3}]} \rightarrow$ $\mathcal{X}_{\Gamma[\sqrt{-3}]}$ is determined by the cubic character of the discriminant of $f$, hence $j_{2}$ is. The normalization of the cubic character then follows by checking that it satisfies the formula of the theorem in examples for the case of genus 3 or by checking it for abelian threefolds that are a product of elliptic curves.

In the general case the threefold cover of stacks is ramified along the codimension 1 locus where the discriminant of $f$ vanishes. Therefore $j_{2}$ is determined by the cubic character of the discriminant of $f$. Then we can specialize to the case where the Jacobian $J\left(C_{f}\right)$ splits as a direct sum of Jacobians of curves of lower genus to check the formula inductively starting from the cases of $g \leq 3$. \(\square\)

\section*{7. Euler characteristics of $\ell$-adic local systems}

In this section we will introduce the motivic Euler characteristic of local system on our moduli spaces, stating basic results, showing how the Lefschetz trace formula can be used to find cohomological information and presenting a formula for the integer valued Euler characteristic of any local system.
7.1. Hecke characters. Recall the notation of Section 6.1. Define the Hecke character $\psi$ of conductor (3) for any $\mathfrak{p}_{p}$ by putting $\psi\left(\mathfrak{p}_{p}\right)=a_{\mathfrak{p}}+b_{\mathfrak{p}} \rho$. This gives a 1-dimensional 'motive' that we will denote $\mathbb{L}^{1,0}$, pure of weight 1 and Hodge type $(1,0)$ and as an $\ell$-adic $\operatorname{Gal}(\bar{F} / F)$-representation, the trace of a Frobenius element $F_{\mathfrak{p}_{p}}$, corresponding to a prime ideal $\mathfrak{p}_{p}$, is given by $\psi\left(\mathfrak{p}_{p}\right)$.

Recall that
$$f_{\psi}(z)=\sum_{\alpha} \psi(\alpha) q^{N(\alpha)} \in \mathbb{Z}[q],$$
where $q=e^{2 \pi i z}$ and the sum is over all integral ideals $\alpha$ prime to (3) and $N(\alpha)$ is the norm of $\alpha$, is a cusp form of weight 2 and level $\Gamma_{0}(27)$. Moreover we have that,
$$f_{\psi}(z)=\eta(3 z)^{2} \eta(9 z)^{2}=q-2 q^{2}-q^{7}+5 q^{13}+4 q^{16}-7 q^{19}-5 q^{25}+\ldots .$$
Similarly we define $\mathbb{L}^{0,1}$ of Hodge type $(0,1)$ by using the Hecke character $\bar{\psi}\left(\mathfrak{p}_{p}\right):=a_{\mathfrak{p}_{p}}+b_{\mathfrak{p}_{p}} \rho^{2}$. Finally, for any pair of integers $n, m$ we define $\mathbb{L}^{n, m}$ by taking tensor products of the 'motives' above. Note that $\mathbb{L}^{1,1}$ becomes the usual Lefschetz motive, also denoted $\mathbb{L}^{1}$.
7.2. Euler characteristics of $\ell$-adic local systems. For any of our moduli spaces $\mathcal{X}$ (which are stacks) introduced in Section 5.1 and Section 5.3 we have a universal family $\pi: \mathcal{C} \rightarrow \mathcal{X}$ and we consider the $\ell$-adic local system $\mathbb{V}:=R^{1} \pi_{*} \overline{\mathbb{Q}}_{\ell}$. This local system has rank 6, where the fiber of a geometric point represented by an abelian variety $A$ equals the $\ell$-adic étale cohomology group $H^{1}\left(A, \overline{\mathbb{Q}}_{\ell}\right)$. It is provided with a non-degenerate alternating pairing $\mathbb{V} \times \mathbb{V} \rightarrow \overline{\mathbb{Q}}_{\ell}(-1)$.

The action of $\alpha$ gives rise to a decomposition of the base change to $F$ of $\mathbb{V}$, as a direct sum of two local systems of rank 3 over $F \otimes \overline{\mathbb{Q}}_{\ell}$ :
$$\mathbb{V} \otimes F=\mathbb{W} \oplus \mathbb{W}^{\prime}$$
with $\mathbb{W}$ (respectively $\mathbb{W}^{\prime}$ ) the $\rho$-eigenspace (respectively the $\rho^{2}$-eigenspace) of $\alpha$.

Note that we can also take $\mathcal{X}(\mathbb{C})$ and define the (Betti) local system $\mathbb{V}:=R^{1} \pi_{*} \mathbb{Q}$, and then the $\rho$-eigenspace $\mathbb{W}$ is the same local system as the one defined in Section 3.1.

We define local systems $\mathbb{W}_{\lambda}$ using the representations of $\operatorname{GL}(3, \mathbb{C}) \times \mathbb{G}_{m}$ as in Section 3.1. The multiplier defines the constant local system $F(-1)$.

Let $\mathbb{W}^{\vee}$ denote the $F$-linear dual. Then note that
$$\left(\mathbb{W}_{n_{1}, n_{2}, n_{3}}\right)^{\vee} \cong \mathbb{W}_{n_{2}, n_{1},-n_{1}-n_{2}-n_{3}} .$$
The non-degenerate pairing implies that the conjugate takes the form
$$\mathbb{W}^{\prime} \cong \mathbb{W}^{\vee} \otimes F(-1),$$
and so
$$\mathbb{W}_{n_{1}, n_{2}, n_{3}}^{\prime} \cong \mathbb{W}_{n_{2}, n_{1},-n_{1}-n_{2}-n_{3}} \otimes F\left(-n_{1}-2 n_{2}-3 n_{3}\right) .$$

Let $H_{c}^{*}$ denote compactly supported $\ell$-adic étale cohomology. The action of the symmetric group $\mathfrak{S}_{4} \cong \Gamma[\sqrt{-3}] / \Gamma$ on $\mathcal{X}_{\Gamma[\sqrt{-3}]}$ induces an action on its cohomology groups. We define the Euler characteristic of the local system $\mathbb{W}_{\lambda}$ on $\mathcal{X}_{\Gamma[\sqrt{-3}]} \otimes \bar{F}$ in $K_{0}\left(\mathrm{Gal}_{F}^{\mathfrak{G}_{4}}\right)$, the Grothendieck group of $\ell$-adic $\operatorname{Gal}(\bar{F} / F)$-representations equipped with an action of $\mathfrak{S}_{4}$ by
$$e_{c}\left(\mathcal{X}_{\Gamma[\sqrt{-3}]}, \mathbb{W}_{\lambda}\right):=\sum_{i=0}^{4}(-1)^{i}\left[H_{c}^{i}\left(\mathcal{X}_{\Gamma[\sqrt{-3}]} \otimes \bar{F}, \mathbb{W}_{\lambda}\right)\right] .$$
Similarly, consider compactly supported Betti cohomology and define by (abuse of) the same notation
$$e_{c}\left(\mathcal{X}_{\Gamma[\sqrt{-3}]}, \mathbb{W}_{\lambda}\right):=\sum_{i=0}^{4}(-1)^{i}\left[H_{c}^{i}\left(\mathcal{X}_{\Gamma[\sqrt{-3}]}(\mathbb{C}), \mathbb{W}_{\lambda}\right)\right]$$
in the Grothendieck group of Hodge modules equipped with an action of $\mathfrak{S}_{4}$. Let $e_{c, \mu}\left(\mathcal{X}_{\Gamma[\sqrt{-3}]}, \mathbb{W}_{\lambda}\right)$ correspond to a $\mu$-isotypic component of the Euler characteristics in the sense that
$$e_{c}\left(\mathcal{X}_{\Gamma[\sqrt{-3}]}, \mathbb{W}_{\lambda}\right)=\sum_{\mu \vdash 4} e_{c, \mu}\left(\mathcal{X}_{\Gamma[\sqrt{-3}]}, \mathbb{W}_{\lambda}\right) \mathbf{s}_{\mu} .$$
The statements in Section 12 will be called motivic, and by this we will mean that these are statements about the Euler characteristic in both these Galois groups.

Proposition 7.1. The Euler characteristics fulfils the following for all $\lambda$ :
\begin{itemize}
\item[(1)] $e_{c}\left(\mathcal{X}_{\Gamma[\sqrt{-3}]}, \mathbb{W}_{\lambda}\right)=0$ if $n_{1} \not \equiv_{3} n_{2}$;
\item[(2)] $e_{c}\left(\mathcal{X}_{\Gamma[\sqrt{-3}]}, \mathbb{W}_{\lambda} \otimes F(-k)\right)=e_{c}\left(\mathcal{X}_{\Gamma[\sqrt{-3}]}, \mathbb{W}_{\lambda}\right) \mathbb{L}^{k}$.
\end{itemize}

Proof. We prove (1), the proof of (2) is standard. The automorphism $\alpha$ acts on the fibre $\left(\mathbb{W}_{\lambda}\right)_{A}$ by $\rho^{n_{1}+2 n_{2}}$ for any closed point $A$ of $\mathcal{X}_{\Gamma[\sqrt{-3}]}$. So if $n_{1} \not \equiv_{3} n_{2}$, then this action has no invariants and hence the cohomology has to vanish. \(\square\)
7.3. Traces of Frobenius. Recall the notation of Section 6.1 and Section 6.2. Compare the following section to the article [5] and the references therein. We define the (geometric) Frobenius $F_{q} \in \operatorname{Gal}(\bar{k} / k)$ to be the inverse of $x \mapsto x^{q}$. We choose a Frobenius element $F_{\mathfrak{p}_{q}} \in \operatorname{Gal}(\bar{F} / F)$, using an element of the Galois group of the $p$-adic completion of $F$ that is mapped to the Frobenius element $F_{q} \in \operatorname{Gal}(\bar{k} / k)$. These Frobenii satisfy
$$\operatorname{Tr}\left(F_{\mathfrak{p}_{q}}, e_{c, \mu}\left(\mathcal{X}_{\Gamma[\sqrt{-3}]} \otimes \bar{F}, \mathbb{W}_{\lambda}\right)\right)=\operatorname{Tr}\left(F_{q}, e_{c, \mu}\left(\mathcal{X}_{\Gamma[\sqrt{-3}]} \otimes \bar{k}, \mathbb{W}_{\lambda}\right)\right)$$
and these traces are element of $\mathbb{Z}[\rho]$. The traces of $F_{\mathfrak{p}_{p}}$ for (almost) all unramified primes $\mathfrak{p}_{p}$ will (using a Chebotarov density argument) determine $e_{c, \mu}\left(\mathcal{X}_{\Gamma[\sqrt{-3]}} \otimes \bar{F}, \mathbb{W}_{\lambda}\right)$ as an element of $K_{0}\left(\mathrm{Gal}_{F}\right)$, c.f. [12, Prop. 2.6]. For any element of $V \in K_{0}\left(\mathrm{Gal}_{F}\right)$ we can define a virtual representation $\bar{V}$ by the property $\operatorname{Tr}\left(F_{\mathfrak{p}_{p}}, \bar{V}\right)=\overline{\operatorname{Tr}\left(F_{\mathfrak{p}_{p}}, V\right)}$.
Proposition 7.2. For any $\mu$ and $\lambda=n_{1} \gamma_{1}+n_{2} \gamma_{2}+n_{3} \gamma_{3}$
$$\overline{e_{c, \mu}\left(\mathcal{X}_{\Gamma[\sqrt{-3}]}, \mathbb{W}_{n_{1}, n_{2}, n_{3}}\right)}=e_{c, \mu}\left(\mathcal{X}_{\Gamma[\sqrt{-3}]}, \mathbb{W}_{n_{2}, n_{1},-n_{1}-n_{2}-n_{3}}\right) \mathbb{L}^{-n_{1}-2 n_{2}-3 n_{3}},$$
as elements of $K_{0}\left(\mathrm{Gal}_{F}\right)$.
Proof. This follows directly from equation (7.1). \(\square\)

Proposition 7.3. For any $p \equiv_{3} 2$, even $r \geq 1, \mu$ and $\lambda$
$$\operatorname{Tr}\left(F_{q}, e_{c, \mu}\left(\mathcal{X}_{\Gamma[\sqrt{-3}]} \otimes \bar{k}, \mathbb{W}_{\lambda}\right)\right) \in \mathbb{Z} .$$
Proof. If $p \equiv_{3} 2$, then the automorphism $x \mapsto x^{p}$ sends $\tilde{\rho}$ to $\tilde{\rho}^{2}$ in $k=\mathbb{F}_{p^{r}}$ for any even $r \geq 1$. This immediately shows that
$$\operatorname{Tr}\left(F_{q}, e_{c, \mu}\left(\mathcal{X}_{\Gamma[\sqrt{-3}]} \otimes \bar{k}, \mathbb{W}_{\lambda}\right)\right)=\overline{\operatorname{Tr}\left(F_{q}, e_{c, \mu}\left(\mathcal{X}_{\Gamma[\sqrt{-3}]} \otimes \bar{k}, \mathbb{W}_{\lambda}\right)\right)} .$$ \(\square\)

Let $e_{i}$ denote the $i$ th elementary symmetric polynomial and $p_{i}$ the $i$ th power sum polynomial. The number of variables should in the future be clear from context. For any partition $\nu \vdash n$, let $s_{\nu}$ denote the Schur polynomial associated to $\nu$ and put
$$e_{\nu}:=\prod_{i=1}^{n} e_{i}^{\nu_{i}} \text { and } p_{\nu}:=\prod_{i=1}^{n} p_{i}^{\nu_{i}} .$$
Recall that $s_{\nu}$ is a polynomial with integer coefficients in the elementary symmetric polynomials $e_{1}, e_{2}, \ldots, e_{n}$, and with rational coefficients in the power sum polynomials and we define $c_{\nu, \xi}$ by,
$$s_{\nu}=\sum_{\xi \vdash n} c_{\nu, \xi} \frac{p_{\xi}}{z_{\xi}}, \text { where } z_{\xi}:=\prod_{i=1}^{n} \xi_{i}!i^{\xi_{i}} .$$
In the representation ring of $\mathfrak{S}_{n}$ (tensored with $\mathbb{Q}$ ) we have the corresponding equality
$$\mathbf{s}_{\nu}=\sum_{\xi \vdash n} c_{\nu, \xi} \frac{\mathbf{p}_{\xi}}{z_{\xi}} .$$

Recall the notation in Section 6.2. For any $C \in \mathcal{X}_{\Gamma[\sqrt{-3}]}(k)$ we have, using Poincaré duality in étale cohomology between $H^{1}\left(C, \overline{\mathbb{Q}}_{\ell}\right)$ and $H_{c}^{1}\left(C, \overline{\mathbb{Q}}_{\ell}\right)$, that
$$\operatorname{Tr}\left(F_{q},(\mathbb{W})_{C \otimes \bar{k}}\right)=\overline{\alpha_{1}(C)}+\overline{\alpha_{2}(C)}+\overline{\alpha_{3}(C)},$$
and so for any partition $\lambda$
$$\operatorname{Tr}\left(F_{q},\left(\mathbb{W}_{\lambda}\right)_{C \otimes \bar{k}}\right)=s_{\lambda}\left(\overline{\alpha_{1}(C)}, \overline{\alpha_{2}(C)}, \overline{\alpha_{3}(C)}\right) .$$

For any partition $\nu$ of 4, let $\mathcal{X}_{\nu}(k)$ inside $\mathcal{X}_{\Gamma[\sqrt{-3}]}(k)$ consist of the curves whose ramification points, where $\alpha$ acts by $\rho$, are defined over $k_{\nu_{i}}$ but not over a subfield of $k_{\nu_{i}}$ for $1 \leq i \leq 4$. From the Lefschetz trace formula (see [13, Th. 3.2]), it follows that if $\sigma_{\nu} \in \mathfrak{S}_{4}$ has cycle type $\nu$ then
$$\operatorname{Tr}\left(F_{q} \circ \sigma_{\nu}, e_{c}\left(\mathcal{X}_{\Gamma[\sqrt{-3}]} \otimes \bar{k}, \mathbb{W}_{\lambda}\right)\right)=\sum_{C \in \mathcal{X}_{\nu}(k) / \cong_{k}} \frac{s_{\lambda}\left(\overline{\alpha_{1}(C)}, \overline{\alpha_{2}(C)}, \overline{\alpha_{3}(C)}\right)}{\left|\operatorname{Aut}_{k}(C)\right|} .$$

By the projection formula we then have
$$\operatorname{Tr}\left(F_{q}, e_{c, \mu}\left(\mathcal{X}_{\Gamma[\sqrt{-3}]} \otimes \bar{k}, \mathbb{W}_{\lambda}\right)\right)=\sum_{\nu \vdash 4} c_{\mu, \nu} \operatorname{Tr}\left(F_{q} \circ \sigma_{\nu}, e_{c}\left(\mathcal{X}_{\Gamma[\sqrt{-3}]} \otimes \bar{k}, \mathbb{W}_{\lambda}\right)\right),$$
giving the equality
$$\operatorname{Tr}\left(F_{q}, e_{c, \mu}\left(\mathcal{X}_{\Gamma[\sqrt{-3}]} \otimes \bar{k}, \mathbb{W}_{\lambda}\right)\right) \mathbf{s}_{\mu}=\sum_{\nu \vdash 4} c_{\mu, \nu} \operatorname{Tr}\left(F_{q} \circ \sigma_{\nu}, e_{c}\left(\mathcal{X}_{\Gamma[\sqrt{-3}]} \otimes \bar{k}, \mathbb{W}_{\lambda}\right)\right) \frac{\mathbf{p}_{\nu}}{z_{\nu}} .$$

Proposition 7.4 For any $\lambda$, we have
$$e_{c}\left(\mathcal{X}_{\Gamma[\sqrt{-3}]}, \mathbb{W}_{\lambda} \otimes \operatorname{det}(\mathbb{W})^{3}\right)=e_{c}\left(\mathcal{X}_{\Gamma[\sqrt{-3}]}, \mathbb{W}_{\lambda}\right) \mathbb{L}^{6,3} \mathbf{s}_{1^{4}},$$
as elements of $K_{0}^{\mathfrak{S}_{4}}\left(\operatorname{Gal}_{F}\right)$.
Proof. Let $C$ be an element of $\mathcal{X}_{\mu}(k)$. We see from Theorem 6.5 that
$$\begin{gathered}
\operatorname{Tr}\left(F_{q},\left(\mathbb{W}_{\lambda} \otimes(\operatorname{det} \mathbb{W})^{3}\right)_{C \otimes \bar{k}}\right)=\operatorname{Tr}\left(F_{q},\left(\mathbb{W}_{\lambda}\right)_{C \otimes \bar{k}}\right) e_{3}\left(\alpha_{1}(C), \alpha_{2}(C), \alpha_{3}(C)\right)^{3} \\
=\operatorname{Tr}\left(F_{q},\left(\mathbb{W}_{\lambda}\right)_{C \otimes \bar{k}}\right)(-1)^{\operatorname{sign}(\nu)}\left(a_{\mathfrak{p}_{q}}+b_{\mathfrak{p}_{q}} \rho\right)^{6}\left(a_{\mathfrak{p}_{q}}+b_{\mathfrak{p}_{q}} \rho^{2}\right)^{3} .
\end{gathered}$$
From this the result follows. \(\square\)

Remark 7.5. If the weight $n_{1}+2 n_{2}+3 n_{3}$ of the local system $\lambda=n_{1} \gamma_{1}+$ $n_{2} \gamma_{2}+n_{3} \gamma_{3}$ is even then
$$e_{c}\left(\mathcal{X}_{\Gamma[\sqrt{-3}]}^{\prime}, \mathbb{W}_{\lambda}\right)=e_{c}\left(\mathcal{X}_{\Gamma[\sqrt{-3}]}, \mathbb{W}_{\lambda}\right),$$
but if the weight is odd then
$$e_{c}\left(\mathcal{X}_{\Gamma[\sqrt{-3}]}^{\prime}, \mathbb{W}_{\lambda}\right)=0$$
due to the presence of the automorphism -1 of the abelian varieties that $\mathcal{X}_{\Gamma[\sqrt{-3}]}^{\prime}$ parametrizes. But we see from Proposition 7.4 that there are no new motives appearing for a local system $\mathbb{W}_{\lambda}$ on $\mathcal{X}_{\Gamma[\sqrt{-3}]}$ of odd weight, since
these motives will, after being tensored with the "trivial factor" $\mathbb{L}^{6,3} \otimes \mathbf{s}_{1^{4}}$, appear in $e_{c}\left(\mathcal{X}_{\Gamma[\sqrt{-3}]}^{\prime}, \mathbb{W}_{\lambda} \otimes \operatorname{det}(\mathbb{W})^{3}\right)$.
7.3.1. Normalization of the Euler characteristic. In the proof of Proposition 7.4 we also see that for any $\mu$ and $\lambda$
$$e_{c, \mu}\left(\mathcal{X}_{\Gamma[\sqrt{-3]}}, \mathbb{W}_{\lambda} \otimes \operatorname{det}(\mathbb{W})^{i}\right)=\mathbb{L}^{2 i, i} V_{\lambda, \mu}$$
for some element $V_{\lambda, \mu}$ of $K_{0}\left(\mathrm{Gal}_{F}^{\mathfrak{S}_{4}}\right)$.
Definition 7.6. If $\lambda=n_{1} \gamma_{1}+n_{2} \gamma_{2}+n_{3} \gamma_{3}$ and $\lambda^{\prime}=n_{1} \gamma_{1}+n_{2} \gamma_{2}$ then $\mathbb{W}_{\lambda}=\mathbb{W}_{\lambda^{\prime} \otimes \operatorname{det}(\mathbb{W})^{n_{3}}}$ and by taking away the factor $\mathbb{L}^{2 n_{3}, n_{3}}$ we define the normalized Euler characteristic to be
$$e_{c, \mu}^{\text {norm }}\left(\mathcal{X}_{\Gamma[\sqrt{-3}]}, \mathbb{W}_{\lambda}\right)=V_{\lambda^{\prime}, \mu} .$$
7.3.2. The appearance of Picard modular cusp forms. Using Proposition 7.1, 7.2 and 7.4 we can restrict ourselves to determining the Euler characteristics of local system $\lambda=n_{1} \gamma_{1}+n_{2} \gamma_{2}+n_{3} \gamma_{3}$ for which $n_{2} \leq n_{1}, n_{1} \equiv_{3} n_{2}, n_{1} \equiv_{2} n_{3}$ and $0 \leq n_{3} \leq 5$.

Proposition 3.3 suggests that one finds a motive in the Euler characteristic $e_{c}^{\text {norm }}\left(\mathcal{X}_{\Gamma[\sqrt{-3}]}, \mathbb{W}_{\lambda}\right)$ that will correspond to the space of Picard modular cusp forms $S_{n_{2}, n_{1}+3, n_{2}+n_{3}-1}$, see further in Section 10.

\section*{8. Counts over finite fields}
8.1. Information needed. In this section we will see what information is needed to compute
$$\operatorname{Tr}\left(F_{q}, e_{c, \mu}\left(\mathcal{X}_{\Gamma[\sqrt{-3}]} \otimes \bar{k}, \mathbb{W}_{\lambda}\right)\right) .$$
The results will be used in Section 10.1 and are the basis of our conjectures in Sections 11 and 12.

First, define the contributions of the strata to the trace
$$\operatorname{Tr}_{i, \nu, \lambda, q}:=\operatorname{Tr}\left(F_{q} \circ \sigma_{\nu}, e_{c}\left(\mathcal{X}_{i, \Gamma[\sqrt{-3}]} \otimes \bar{k}, \mathbb{W}_{\lambda}\right)\right) .$$
8.1.1. Counts of smooth curves of genus 3. Let $P_{1, \mu}(k)$ denote the set of square-free polynomials $f$ with coefficients in $k$ of degree four such that $f$ has $\mu_{i}$ roots defined over $k_{i}$ but not over any proper subfield of $k_{i}$. From Equation (7.3), together with the results of Section 5.4 we find that
$$\operatorname{Tr}_{1, \nu, q}=\frac{1}{q(q-1)^{2}} \sum_{f \in P_{1, \mu}(k)} s_{\lambda}\left(\overline{\alpha_{1}(C)}, \overline{\alpha_{2}(C)}, \overline{\alpha_{3}(C)}\right) .$$

If we have computed
$$e_{1}\left(\alpha_{1}\left(C_{f}\right), \alpha_{2}\left(C_{f}\right), \alpha_{3}\left(C_{f}\right)\right)=a_{1, \rho}\left(C_{f}\right)=-\sum_{a \in \mathbb{P}^{1}(k)} \chi(f(a)),$$
then we can use equation (6.1) together with Theorem 6.5 to easily compute $e_{i}\left(\alpha_{1}\left(C_{f}\right), \alpha_{2}\left(C_{f}\right), \alpha_{3}\left(C_{f}\right)\right)$, for $i=2,3$. With this information we can compute $s_{\lambda}\left(\alpha_{1}\left(C_{f}\right), \alpha_{2}\left(C_{f}\right), \alpha_{3}\left(C_{f}\right)\right)$ for any $\lambda$.

One can then simplify the computation of $\operatorname{Tr}_{1, \nu, q}$ by using the group of isomorphisms to find normal forms. Fix a generator $\gamma$ of $k^{*}$. If $p$ is odd and $p \neq 3$, then a curve of the form
$$y^{3}=a_{4} x^{4}+a_{3} x^{3}+a_{2} x^{2}+a_{1} x+a_{0}$$
with $a_{2}, a_{3}$ and $a_{4}$ non-zero, is isomorphic (over $k$ ) to a curve of the form
$$y^{3}=\gamma^{i}\left(a_{4}^{\prime} x^{4}+x^{2}+x+a_{0}^{\prime}\right),$$
for some $a_{4}^{\prime}, a_{0}^{\prime}$ and $0 \leq i \leq 2$. The curves of the latter form are all non-isomorphic and have an automorphism group of order 3 generated by $y \mapsto \tilde{\rho} y$. If $D_{1} \subset P_{1, \mu}(k)$ is the subset of polynomials of the form (8.1) and $D_{2} \subset P_{1, \mu}(k)$ of the form (8.2) then
$$\begin{aligned}
& \frac{1}{q(q-1)^{2}} \sum_{f \in D_{1}} s_{\lambda}\left(\overline{\alpha_{1}(C)}, \overline{\alpha_{2}(C)}, \overline{\alpha_{3}(C)}\right) \\
& \quad=\frac{1}{3} \sum_{i=1}^{3} \sum_{f=a_{4}^{\prime} x^{4}+x^{2}+x+a_{0}^{\prime} \in D_{2}} s_{\lambda}\left(\tilde{\rho}^{i} \overline{\alpha_{1}\left(C_{f}\right)}, \tilde{\rho}^{i} \overline{\alpha_{2}\left(C_{f}\right)}, \tilde{\rho}^{i} \overline{\alpha_{3}\left(C_{f}\right)}\right) .
\end{aligned}$$
In a similar way, one can construct other normal forms if $a_{2}$ or $a_{3}$ is zero.
If $p=2$ then a curve of the form
$$y^{3}=a_{4} x^{4}+a_{3} x^{3}+a_{2} x^{2}+a_{1} x+a_{0}$$
with $a_{1}, a_{0}$ and $a_{4}$ non-zero, will be isomorphic to a curve of the form
$$y^{3}=\gamma^{i}\left(x^{4}+x^{3}+a_{1}^{\prime} x+a_{0}^{\prime}\right)$$
for some $a_{1}^{\prime}, a_{0}^{\prime}$ and $0 \leq i \leq 2$.
In this manner we can reduce the number of free parameters in the polynomials in the sum $\operatorname{Tr}_{1, \nu, q}$ from 5 to 2 (which is optimal since we are considering a surface).
8.1.2. Counts of smooth genus 2 curves joined with elliptic curves. We will denote by $P_{2, \mu}(k)$ the set of triples of polynomials $\left(f_{1}, f_{2}, f\right)$ with coefficients in $k$, as in Section 5.7, but where we assume that $f_{2}$ is of degree 1 by putting the point $q_{2}$ in infinity using a linear transformation in $x$, and such that $f$ and $f_{1}$ together have $\mu_{i}$ roots defined over $k_{i}$ but not over any subfield of $k_{i}$. We find that
$$\operatorname{Tr}_{2, \nu, q}=\frac{1}{\left(q^{2}(q-1)^{4}\right.} \sum_{\left(f_{1}, f_{2}, f\right) \in P_{2, \mu}(k)} s_{\lambda}\left(\overline{\alpha_{1}\left(C_{f_{1}, f_{2}}\right)}, \overline{\alpha_{2}\left(C_{f_{1}, f_{2}}\right)}, \overline{\left.\alpha_{1}\left(C_{f}\right)\right)} .\right.$$
If we have computed
$$e_{1}\left(\alpha_{1}\left(C_{f_{1}, f_{2}}\right), \alpha_{2}\left(C_{f_{1}, f_{2}}\right)\right)=-\sum_{a \in \mathbb{P}^{1}(k)} \chi\left(f_{1}(a)\right) \chi\left(f_{2}(a)\right)^{2},$$
we can use Theorem 6.5 to compute $e_{2}\left(\alpha_{1}\left(C_{f_{1}, f_{2}}\right), \alpha_{2}\left(C_{f_{1}, f_{2}}\right)\right)$. Using the equations in Section 6.2.1 we can compute $e_{1}\left(\alpha_{1}\left(C_{f}\right)\right)$. From this we can determine $e_{i}\left(\alpha_{1}\left(C_{f_{1}, f_{2}}\right), \alpha_{2}\left(C_{f_{1}, f_{2}}\right), \alpha_{1}\left(C_{f}\right)\right)$ for $i=1,2,3$.

As in Section 8.1.1, we can use the group of isomorphisms to find normal forms which will simplify the computation of $\operatorname{Tr}_{2, \nu, q}$. Fix $\gamma$, a generator of $k^{*}$. If $p$ is odd, and $\left(b_{2} x^{2}+b_{1} x+b_{0}, c_{1} x+c_{0}, d_{2} x^{2}+d_{1} x+d_{0}\right)$ is in $P_{2, \mu}(k)$ with $c_{0} \neq 0$, then we can find an isomorphism to a curve given by $\left(f_{1}^{\prime}, f_{2}^{\prime}, f_{3}^{\prime}\right)$ in $P_{2, \mu}(k)$, where $f_{3}^{\prime}=x^{2}+\gamma^{i}, f_{2}^{\prime}=x+1$ and $f_{1}^{\prime}=\gamma^{j}\left(x^{2}+b_{1}\right)$ for some $b_{1} \in k, 0 \leq i \leq 5$ and $0 \leq j \leq 2$. The curves of the latter form are all non-isomorphic and have an automorphism group of order 3 generated by $y \mapsto \tilde{\rho} y$. Similar normal forms can be found if $c_{0}=0$ and if $p$ is even.

In this manner we can reduce the free parameters in the polynomials in the sum $\operatorname{Tr}_{2, \nu, q}$ from 8 to 1 (which is optimal since we are here considering a curve).
8.1.3. Counts of triples of elliptic curves. Let $P_{3, \mu}(k)$ denote the set of triples of polynomials $\left(f_{1}, f_{2}, f_{3}^{2}\right)$ with coefficients in $k$, as in Section 5.8, such that $f_{1}$ and $f_{2}$ together have $\mu_{i}$ roots defined over $k_{i}$ but not over any subfield of $k_{i}$. Define $P_{3, \mu}^{\prime}(k)$ in the same way, but where $f_{1}, f_{2}$ are defined over $k_{2}$ and where Frobenius sends $f_{1}$ to $f_{2}$. Note that we have more isomorphisms between the curves corresponding to elements of these sets, namely by switching the two "wings" of these curves, that is between $C_{f_{1}, f_{2}, f_{3}^{2}}$ and $C_{f_{2}, f_{1}, f_{3}^{2}}$. We have that
$$\begin{aligned}
& \operatorname{Tr}_{3, \nu, q}=\frac{1}{2 q^{3}(q-1)^{3}} \sum_{\left(f_{1}, f_{2}, f_{3}^{2}\right) \in P_{3, \mu}(k)} s_{\lambda}\left(\overline{\alpha_{1}\left(C_{f_{1}}\right)}, \overline{\alpha_{1}\left(C_{f_{2}}\right)}, \overline{\alpha_{1}\left(C_{f_{3}^{2}}\right)}\right) \\
& \left.\quad+\frac{1}{2 q^{3}(q-1)\left(q^{2}-1\right)} \sum_{\left(f_{1}, f_{2}, f_{3}^{2}\right) \in P_{3, \mu}^{\prime}(k)} s_{\lambda}\left(\overline{\alpha_{1}\left(C_{f_{1}}\right)}\right), \overline{\alpha_{2}\left(C_{f_{2}}\right)}, \overline{\alpha_{1}\left(C_{f_{3}^{2}}\right)}\right) .
\end{aligned}$$
If $\left(f_{1}, f_{2}, f_{3}^{2}\right)$ are in $P_{3, \mu}(k)$ then using the equations in Section 6.2.1 we can compute $e_{1}\left(\alpha_{1}\left(C_{f_{i}}\right)\right)$ for $i=1,2,3$. For $\left(f_{1}, f_{2}, f_{3}^{2}\right)$ in $P_{3, \mu}^{\prime}(k)$ we can determine $e_{1}\left(\alpha_{1}\left(C_{f_{3}^{2}}\right)\right)$ in the same way. Moreover, $e_{1}\left(\alpha_{1}\left(C_{f_{1}}\right), \alpha_{2}\left(C_{f_{2}}\right)\right)=0$ and
$$p_{2}\left(\alpha_{1}\left(C_{f_{1}}\right), \alpha_{2}\left(C_{f_{2}}\right)\right)=-\sum_{a \in \mathbb{P}^{1}\left(k_{2}\right)} \chi\left(f_{1}(a)\right)-\sum_{a \in \mathbb{P}^{1}\left(k_{2}\right)} \chi\left(f_{2}(a)\right),$$
where $\chi$ is the third power residue symbol for $k_{2}$. In both cases, this gives enough information to determine $e_{i}\left(\alpha_{1}\left(C_{f_{1}}\right), \alpha_{1}\left(C_{f_{2}}\right), \alpha_{1}\left(C_{f_{3}^{2}}\right)\right)$ for $i=$ 1,2,3.

In Section 6.2.1 a representative of each $k$-isomorphism class of $\mathcal{X}_{\Gamma}^{(1)}(k)$ is given. With this information $\operatorname{Tr}_{3, \nu, q}$ is easily computed for any $\nu$ and $q$.
8.2. Counts with constant coefficients. Let us consider the Euler characteristic when $\mathbb{W}_{\lambda}=\overline{\mathbb{Q}}_{\ell}$.

We will repeatedly use the trick below that summing over all elements defined over $k$, of one of the groupoids at hand, and then dividing by the number of $k$-isomorphisms between these elements is the same as summing
elements weighted by the reciprocal of their number of $k$-automorphisms, compare for instance [4, Section 5].

The elements of $\mathcal{X}_{1, \Gamma}(k)$ together with their isomorphisms are described in Section 5.4. For $\Gamma[\sqrt{-3}]$ we divide into the different choices of four branch points on $\mathbb{P}^{1}$ giving
$$\begin{aligned}
& \operatorname{Tr}\left(F_{q}, e_{c}\left(\mathcal{X}_{1, \Gamma[\sqrt{-3}]} \otimes \bar{k}, \overline{\mathbb{Q}}_{\ell}\right)\right)=\left(q(q-1)(q-2)(q-3) \frac{\mathbf{p}_{1}^{4}}{24}\right. \\
& \quad+\left(q^{2}-q\right) q(q-1) \frac{\mathbf{p}_{1}^{2} \mathbf{p}_{2}}{4}+\left(q^{3}-q\right) q \frac{\mathbf{p}_{1} \mathbf{p}_{3}}{3}+\left(q^{2}-q\right)\left(q^{2}-q-2\right) \frac{\mathbf{p}_{2}^{2}}{8} \\
& \left.\quad+\left(q^{4}-q^{2}\right) \frac{\mathbf{p}_{4}}{4}\right) /(q(q-1))=q^{2} \mathbf{s}_{4}+(1-q) \mathbf{s}_{3,1}-q \mathbf{s}_{2,2}+\mathbf{s}_{2,1,1}
\end{aligned}$$

Similarly for $\mathcal{X}_{2, \Gamma[\sqrt{-3}]}$ we use Sections 5.5, 5.6 and 5.7 and we find that
$$\begin{aligned}
& \operatorname{Tr}\left(F_{q}, e_{c}\left(\mathcal{X}_{2, \Gamma[\sqrt{-3}]} \otimes \bar{k}, \overline{\mathbb{Q}}_{\ell}\right)\right)=\left(( \frac { \mathbf { p } _ { 1 } ^ { 2 } } { 2 } + \frac { \mathbf { p } _ { 2 } } { 2 } ) \left(q(q-1)(q-2) \frac{\mathbf{p}_{1}^{2}}{2}\right.\right. \\
+ & \left.\left.q\left(q^{2}-q\right) \frac{\mathbf{p}_{2} \mathbf{p}_{2}}{2}\right)\right) /(q(q-1))=(q-1) \mathbf{s}_{4}+(q-2) \mathbf{s}_{3,1}+(q-1) \mathbf{s}_{2,2}-\mathbf{s}_{2,1,1} .
\end{aligned}$$

For $\mathcal{X}_{3, \Gamma[\sqrt{-3}]}$ we use Sections 5.6 and 5.8, and we recall the plethysm ∘ to deal with the symmetry of the two elliptic curves that form the "wings". We find that
$$\begin{aligned}
\operatorname{Tr}\left(F_{q}, e_{c}\left(\mathcal{X}_{3, \Gamma[\sqrt{-3}]} \otimes \bar{k}, \overline{\mathbb{Q}}_{\ell}\right)\right) & =\left(\frac{\mathbf{p}_{1}^{2}}{2}+\frac{\mathbf{p}_{2}}{2}\right) \circ\left(\frac{\mathbf{p}_{1}^{2}}{2}+\frac{\mathbf{p}_{2}}{2}\right) \\
= & \frac{1}{2}\left(\frac{\mathbf{p}_{1}^{2}}{2}+\frac{\mathbf{p}_{2}}{2}\right)^{2}+\frac{1}{2}\left(\frac{\mathbf{p}_{2}^{2}}{2}+\frac{\mathbf{p}_{4}}{2}\right)=\mathbf{s}_{4}+\mathbf{s}_{2,2} .
\end{aligned}$$

The trace of Frobenius on $e_{c}\left(\mathcal{X}_{3, \Gamma[\sqrt{-3}]} \otimes \bar{k}\right)$ for all $q \equiv_{3} 1$ determines $e_{c}\left(\mathcal{X}_{\Gamma[\sqrt{-3}]} \otimes \bar{k}, \overline{\mathbb{Q}}_{\ell}\right)$ as an element in $K_{0}\left(\mathrm{Gal}_{F}^{\mathfrak{S}_{4}}\right)$, see Section 7.3. Summing the three cases above we then get the following.

Proposition 8.1. We have an equality of elements in $K_{0}\left(\mathrm{Gal}_{F}^{\mathfrak{S}_{4}}\right)$ :
$$\left.e_{c}\left(\mathcal{X}_{\Gamma[\sqrt{-3}]} \otimes \bar{k}, \overline{\mathbb{Q}}_{\ell}\right)\right)=\left(\mathbb{L}^{2}+\mathbb{L}\right) \mathbf{s}_{4}-\mathbf{s}_{3,1} .$$

We continue with case iv) of Section 5.9. On the elliptic curve $C_{1}$, there is a choice of a point not equal to any of the ramification points. This gives a contribution $q+1-a_{1}\left(C_{1}\right)-r_{1}\left(C_{1}\right)$, where $r_{1}\left(C_{1}\right)$ is the number of ramification points of $C_{1}$ defined over $k$. A computation similar to the one in Section 6.2.1 shows, due to the symmetry, that the contribution from $a_{1}\left(C_{1}\right)$ vanishes. The genus 0 curve contributes a $p_{1}$, and so the trace of Frobenius on the Euler characteristic of the strata for case iv) equals,
$$\begin{aligned}
p_{1}\left((q+1-3) \frac{\mathbf{p}_{1}^{3}}{6}+(q+1-1) \frac{\mathbf{p}_{1} \mathbf{p}_{2}}{2}+\right. & \left.(q+1) \frac{\mathbf{p}_{3}}{3}\right) \\
= & q \mathbf{s}_{4}+(q-1) \mathbf{s}_{3,1}-\mathbf{s}_{2,2}-\mathbf{s}_{2,1,1} .
\end{aligned}$$

Case v) is straightforward and the trace of Frobenius on its Euler characteristic equals,
$$\mathbf{p}_{1}^{2}\left(\frac{\mathbf{p}_{1}^{2}}{2}+\frac{\mathbf{p}_{2}}{2}\right)=\mathbf{s}_{4}+2 \mathbf{s}_{3,1}+\mathbf{s}_{2,2}+\mathbf{s}_{2,1,1} .$$

Summing cases i) to v) and using the purity of a smooth and proper (Deligne-Mumford) stack we find the following.

Proposition 8.2. We have an equality of elements in $\mathrm{Gal}_{F}^{\mathfrak{S}_{4}}$ :
$$\left.H_{c}^{i}\left(\tilde{\mathcal{X}}_{\Gamma[\sqrt{-3}]} \otimes \bar{k}, \overline{\mathbb{Q}}_{\ell}\right)\right)= \begin{cases}\mathbb{L}^{2} \mathbf{s}_{4} & \text { if } i=4 \\ \mathbb{L}\left(2 \mathbf{s}_{4}+\mathbf{s}_{3,1}\right) & \text { if } i=2 \\ \mathbb{L}^{0} \mathbf{s}_{4} & \text { if } i=0 \\ 0 & \text { if } i \text { odd }\end{cases}$$