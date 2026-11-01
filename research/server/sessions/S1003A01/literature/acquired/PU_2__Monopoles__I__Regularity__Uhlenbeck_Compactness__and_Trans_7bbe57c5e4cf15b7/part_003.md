---
retention_scope: session
part: 3
total_parts: 6
---

[Part 3/6 of: PU(2) Monopoles. I: Regularity, Uhlenbeck Compactness, and Transversality]

Some of the regularity results and estimates of this section generalize corresponding results for the first-order anti-self-dual equation [20], [30] and, to a certain extent, those of Uhlenbeck [94] and Parker [70] for the second-order (coupled) Yang-Mills equations. As usual for a quasi-linear, first-order elliptic system with a quadratic non-linearity, over an $n$-dimensional manifold, the main difficulty is to prove regularity for $L_1^{n/2}$ solutions (that is, at the critical Sobolev exponent). Once the solutions are known to be in $L^\infty$, then standard linear elliptic regularity theory can be applied [37], [64]. It is worth noting at the outset, though,
that despite an extensive literature on quasi-linear elliptic systems due
to Ladyzhenskaya-Ural’tseva, Morrey and others [54], [64], these classical results do not meet the usual demands of gauge theory and this
explains why we develop the precise results we require here. The constants appearing in our estimates generally depend on the underlying Riemannian metric on $X$, the fixed spin$^c$ connection on $W$, the fixed unitary connection on det $E$, and the perturbations $(\tau_0, \vartheta_0, \vec{\tau}, \vec{\vartheta})$: this dependence is not explicitly noted, as these ingredients in the PU(2) monopole equations (2.27) are fixed once and for all.

3.1. Regularity for $L_1^2$ solutions to the inhomogeneous Coulomb gauge and PU(2) monopole equations. We show
in this subsection that an $L_1^2$ solution $(a, \phi)$ to the PU(2) monopole and Coulomb-gauge equations (3.2), with an $L_k^2$ inhomogeneous term (with $k \geq 1$) is in $L_{k+1}^2$. Thus, if the inhomogeneous term is in $C^\infty$, then $(a, \phi)$ is in $C^\infty$. In passing from an $L_1^2$ to an $L_2^2$ solution we need only consider the case where $(\vec{\tau}, \vec{\vartheta}) = 0$, while no restriction is placed on the perturbation $(\vec{\tau}, \vec{\vartheta}) \in \mathcal{P}$ given an $L_2^2$ solution $(a, \phi)$.

Our regularity result contains, as special cases, Proposition 4.4.13 in [20] and Theorem 8.8 in [30], for anti-self-dual connections, and Theorem 8.11 in [77] for Seiberg-Witten monopoles. The proof we give below for PU(2) monopoles is rather different. We provide a fairly detailed argument here since regularity of $L_2^2$ solutions to an elliptic equation with a quadratic non-linear term does not quite follow directly from the standard theory for non-linear elliptic systems (for example, [64, Theorem 6.8.1]).

The two principal steps are, first, to get $L_1^p$ regularity of an $L_1^2$ solution $(a, \phi)$ when $2 < p < 4$ and $(a, \phi)$ is sufficiently $L^4$-small and, second, to apply elliptic boostrapping and the Sobolev multiplication and embedding theorems to get $C^\infty$ regularity of an $L_1^p$ solution $(a, \phi)$ when $2 < p < \infty$. We will use these sharp regularity results and estimates repeatedly throughout our work, so we give the argument in some detail here. The main ingredient in the first step is supplied by Proposition 3.2 and uses a Fredholm alternative argument to pass from $L_1^2$ to the slightly stronger $L_1^p$ regularity [33, Theorem 5.3]. Although we will often be able to simply assume that the inhomogenous term is in $C^\infty$, rather than just in $L^p$, we will later need these intermediate regularity results in our development of the gluing theory for PU(2) monopoles [26], [27] to show that $L_1^2$ solutions $(a, \phi)$ to the system (3.2) with a certain inhomogeneous term ($\zeta, v, \psi$), where the latter is initially only known to be in $L_1^2$ or $L_2^2$, are actually in $C^\infty$ (together, of course, with $(\zeta, v, \psi)$).

**Lemma 3.1.** Let $\mathfrak{B}_1, \mathfrak{B}_2$ be Banach spaces and let

$$T \in \text{Hom}(\mathfrak{B}_1, \mathfrak{B}_2)$$

have a right (left) inverse $P$. If $T' \in \text{Hom}(\mathfrak{B}_1, \mathfrak{B}_2)$ satisfies

$$\| T' - T \| < \| P \|^{-1},$$

then $T'$ also has a right (left) inverse.

Proof. If $P \in \text{Hom}(\mathfrak{B}_2, \mathfrak{B}_1)$ is a right inverse for $T$, so $TP = \mathrm{id}_1$, then

$$\| (T' - T)P \| \leq \| T' - T \| \| P \| < 1,$$

and $\mathrm{id}_1 + (T' - T)P$ is an invertible element of the Banach algebra End($\mathfrak{B}_1$). Define $P' = P(1 + (T' - T)P)^{-1}$, so $T'P' = \mathrm{id}_1$ and $P'$ is a right inverse for $T'$. Similarly for left inverses. q.e.d.

The preceding elementary consequence of the usual characterization of invertible elements of a Banach algebra will be frequently invoked in this section and in particular, in the proof of the proposition below.

**Proposition 3.2.** Let $X$ be a closed, oriented, Riemannian four-manifold with metric $g$ and spin$^c$ structure ($\rho, W$), and let $E$ be a Hermitian two-plane bundle over $X$. Let $(A_0, \Phi_0)$ be a $C^\infty$ pair on the $C^\infty$ bundles ($\mathfrak{su}(E), W^+ \otimes E$) over $X$ and let $2 \leq p < 4$. Then there are positive constants $\varepsilon = \varepsilon(A_0, \Phi_0, p)$ and $C = C(A_0, \Phi_0, p)$ with the following significance. Suppose that $(a, \phi) \in L_1^2(X, \Lambda^1 \otimes \mathfrak{su}(E)) \oplus L_1^2(X, W^+ \otimes E)$ is an $L_1^2$ solution on $(\mathfrak{su}(E), W^+ \otimes E)$ to the elliptic system (3.2) over $X$ with $(\vec{\tau}, \vec{\vartheta}) = 0$, where $(\zeta, v, \psi)$ is in $L^p$. If $\|(a, \phi)\|_{L^4(X)} < \varepsilon$, then $(a, \phi)$ is in $L_1^p$ and

$$\|(a, \phi)\|_{L_1^p,A_0(X)} \leq C \left(\|(\zeta, v, \psi)\|_{L^p(X)} + \|(a, \phi)\|_{L^2(X)}\right).$$

Proof. The operator $\mathcal{D}_{A_0, \Phi_0}$ is Fredholm (since it is elliptic with $C^\infty$ coefficients and $X$ is closed), and so has a finite-dimensional kernel and cokernel. In particular, Ker $\mathcal{D}_{A_0, \Phi_0}|_{L_1^2} \subset C^\infty$. Let $\Pi_1$ be the $L^2$-orthogonal projection onto Ker $\mathcal{D}_{A_0, \Phi_0}|_{L_1^2}$ and let $\Pi_2$ be the $L^2$-orthogonal projection onto Ker $\mathcal{D}^*_{A_0, \Phi_0}|_{L^2} = (\text{Im } \mathcal{D}_{A_0, \Phi_0}|_{L_1^2})^\perp$, the $L^2$-orthogonal complement of the image of Im $\mathcal{D}_{A_0, \Phi_0}|_{L_1^2}$. The $L^2$-adjoint

---

$D^*_{A_0, \Phi_0}$ is again a first-order linear elliptic operator with $C^\infty$ coefficients and so Ker $D^*_{A_0, \Phi_0}|_{L^2} \subset C^\infty$. We may then rewrite our quasi-linear elliptic equation (3.2) in the form

$$\Pi_2^{\perp} D_{A_0, \Phi_0} \Pi_1^{\perp}(a, \phi) + \Pi_2^{\perp}\{(a, \phi), \Pi_1^{\perp}(a, \phi)\}$$

$$= -\Pi_2\left(D_{A_0, \Phi_0}(a, \phi)+\{(a, \phi), \Pi_1^{\perp}(a, \phi)\}\right)$$

$$- \{(a, \phi), \Pi_1(a, \phi)\}+(\zeta, v, \psi)=:\Upsilon,$$

where $\Pi_i^{\perp} = \text{id}-\Pi_i$ for $i=1,2$. Thus, we need to consider the existence and uniqueness problem for solutions $(b, \varphi)$ to

(3.3) $$\Pi_2^{\perp} D_{A_0, \Phi_0}(b, \varphi) + \Pi_2^{\perp}\{(a, \phi), (b, \varphi)\}=\Upsilon,$$

where $(b, \varphi) \in L_1^p \cap (\text{Ker } D_{A_0, \Phi_0})^{\perp}$. Plainly, the operator

$$\Pi_2^{\perp} D_{A_0, \Phi_0}: L_1^p \cap (\text{Ker } D_{A_0, \Phi_0})^{\perp} \to L_1^p \cap (\text{Ker } D^*_{A_0, \Phi_0})^{\perp}$$

is (left and right) invertible and hence this will also be true for any operator from $L_1^p \cap (\text{Ker } D_{A_0, \Phi_0})^{\perp}$ to $L^p \cap (\text{Ker } D^*_{A_0, \Phi_0})^{\perp}$, such as $\Pi_2^{\perp} D_{A_0, \Phi_0}+\Pi_2^{\perp}\{(a, \phi), \cdot\}$, which is sufficiently close in the Hom($L_1^p, L^p$) operator norm by Lemma 3.1. Since $D_{A_0, \Phi_0}$ and $D^*_{A_0, \Phi_0}$ are first-order linear elliptic operators with $C^\infty$ coefficients and $D_{A_0, \Phi_0}\Pi_1=0$ and $D^*_{A_0, \Phi_0}\Pi_2=0$, standard elliptic theory implies that

(3.4) $$\|\Pi_2(\xi, w, \varrho)\|_{L_k^{r}, A_0} \leq C\|(\xi, w, \varrho)\|_2, \quad (\xi, w, \varrho) \in L_k^{r},$$

$$\|\Pi_1(b, \varphi)\|_{L_k^{r}, A_0} \leq C\|(b, \varphi)\|_2, \quad (b, \varphi) \in L_k^{r},$$

for some constant $C=C(A_0, \Phi_0,k,r)$, whenever $k \geq 1$ and $rk \geq 4/3$ or $k=0$ and $r \geq 2$.

Since $(a, \phi)$ is in $L_1^2$, the terms $D_{A_0, \Phi_0}(a, \phi)$ and $\{(a, \phi), (a, \phi)\}$ are in $L^2$, while the term $\{(a, \phi), \Pi_1(a, \phi)\}$ is in $L_1^2$. The terms $\Pi_2 D_{A_0, \Phi_0}(a, \phi)$ and $\Pi_2\{(a, \phi), \Pi_1^{\perp}(a, \phi)\}$ are each in $C^\infty$, while $(\zeta, v, \psi)$ is in $L^p$, and so the right-hand side $\Upsilon$ of (3.3) is in $L^p \cap (\text{Ker } D^*_{A_0, \Phi_0})^{\perp}$.

Let $q=4p/(4-p)$. Then $4<q <\infty$; there is a continuous multiplication map $L^4 \times L^q \to L^p$ and an embedding $L_1^p \subset L^q$. So, as $\Pi_2^{\perp} = \text{id}-\Pi_2,$

$$\|\Pi_2^{\perp}\{(a, \phi), (b, \varphi)\}\|_{L^p} \leq \|\{(a, \phi), (b, \varphi)\}\|_{L^p} + C\|\{(a, \phi), (b, \varphi)\}\|_{L^2}$$

$$\leq C\|\{(a, \phi)\}\|_{L^4}\|(b, \varphi)\|_{L_1^p,A_0},$$ for some positive constant $C = C(A_0, \Phi_0, p)$. By Lemma 3.1 there is a positive constant $\varepsilon = \varepsilon(A_0, \Phi_0, p)$ such that if $\|(a, \phi)\|_{L^4} < \varepsilon$, the linear operator $\Pi_2^\perp \mathcal{D}_{A_0, \Phi_0} + \Pi_2^\perp\{(a, \phi), \cdot\}$ is (left and right) invertible as a map $L_1^p \cap (\text{Ker } \mathcal{D}_{A_0, \Phi_0})^\perp \rightarrow L^p \cap (\text{Ker } \mathcal{D}^*_{A_0, \Phi_0})^\perp$. Since $\Pi_1^\perp(a, \phi)$ is a solution to (3.3) when $p = 2$, it is the unique solution for $p = 2$.

Let $(a_p, \phi_p) \in L_1^p \cap (\text{Ker } \mathcal{D}_{A_0, \Phi_0})^\perp$ be the $L_1^p$ solution to (3.3). Then $(a_p, \phi_p)$ is also an $L_1^2$ solution and by the uniqueness assertion we must have that $(a_p, \phi_p) = \Pi_1^\perp(a, \phi)$. Thus, $\Pi_1^\perp(a, \phi)$ is in $L_1^p$ and so $(a, \phi)$ is in $L_1^p$, since $\Pi_1(a, \phi)$ is in $C^\infty$. Finally, the standard estimate for $\mathcal{D}_{A_0, \Phi_0}$, the estimate (3.4), and equation (3.2) yield

$$\|(a, \phi)\|_{L_1^p,A_0} \leq C\left(\|\mathcal{D}_{A_0, \Phi_0}(a, \phi)\|_{L^p} + \|\Pi_1(a, \phi)\|_{L^2}\right)
\leq C\left(\{\{(a, \phi), (a, \phi)\}\|_{L^p} + \|\zeta, v, \psi)\|_{L^p} + \|\Pi_1(a, \phi)\|_{L^2}\right),$$

and so the desired bound for $(a, \phi)$ follows by the Sobolev multiplication $L^4 \times L^q \rightarrow L^p$, the embedding $L_1^p \subset L^q$, and rearrangement. q.e.d.

Proposition 3.2 will have two main applications: the first is in our proof of removable singularities for PU(2) monopoles, and the second is in our proof of $C^\infty$ regularity for $L_1^2$ solutions to the PU(2) monopole equation obtained by gluing [26], [27].

As is well-known from standard gauge theory, it is not possible to construct a well-defined quotient space using $L_1^2$ pairs modulo $L_2^2$ gauge transformations. We construct a quotient using $L_k^2$ pairs modulo $L_{k+1}^2$ gauge transformations, with $k \geq 2$. We first establish a regularity result for the inhomogeneous PU(2) monopole and Coulomb gauge equations, while in §3.2 we show that any PU(2) monopole in $L_k^2$ is $L_{k+1}^2$-gauge equivalent to a PU(2) monopole in $C^\infty$.

**Proposition 3.3.** Continue the notation of Proposition 3.2. Let $k \geq 1$ be an integer and let $2 < p < \infty$. Let $(A_0, \Phi_0)$ be a $C^\infty$ pair on the $C^\infty$ bundles $(\mathfrak{su}(E), W^+ \otimes E)$ over $X$. Suppose that either

- $(a, \phi) \in L_1^p(X, \Lambda^1 \otimes \mathfrak{su}(E)) \oplus L_1^p(X, W^+ \otimes E)$, with $(\vec{\tau}, \vec{\psi}) = 0$, or
- $(a, \phi) \in L_2^2(X, \Lambda^1 \otimes \mathfrak{su}(E)) \oplus L_2^2(X, W^+ \otimes E)$

is a solution on $(\mathfrak{su}(E), W^+ \otimes E)$ to the elliptic system (3.2) over $X$, where $(\zeta, v, \psi)$ is in $L_k^2$. Then $(a, \phi)$ is in $L_{k+1}^2$ and there is a universal polynomial $Q_k(x,y)$, with positive real coefficients depending at most on $(A_0, \Phi_0), k$, such that $Q_k(0,0) = 0$ and

$$\|(a, \phi)\|_{L_{k+1}^2,A_0}(X) \leq Q_k\left(\|\zeta, v, \psi\|_{L_{k+1}^2(A_0)(X)}, \|(a, \phi)\|_{L_{k+1}^2(A_0)(X)}\right).$$

---

In particular, if $ (\zeta,v,\psi) $ is in $ C^{\infty},t $ 0,then

en (a, $ \phi $ ) is in $ C^{\infty} $ , and if $ (\zeta,v,\psi)=$

$$
\textit{if}(\zeta,v,\psi)
$$

$$
C^{\infty}
$$

$$
(a,\phi)
$$

$$
C^{\infty}
$$

$$
\it{if}\left(\zeta,v,\psi\right)=
\|(a,\phi)\|_{L^2_{k+1,A_0}(X)}\leq C\|(a,\phi)\|_{L^p_{1,A_0}(X)}.
$$

Proof. We consider the cases k=1, k=2, and k $ \geq 3 $ separately. We may further assume without loss of generality that 2<p<4.

$$
k=1,k=2
$$

$$
k\geq3
$$

$$
2<p<4.
$$

Case (k=1). Let $ p_{0}=p $ and $ q_{0}=q=4 p /(4-p) $ . Then 1/p = 1/4+1/q and 4<q < $ \infty $ . We have a continuous Sobolev multiplication map $ L^{4}\times L^{q}\rightarrow L^{p} $ and an embedding $ L_{1}^{p}\subset L^{q}. $ Since

$$
\left(k=1\right)
$$

$$
p_{0}=p
$$

$$
q_{0}=q=4p/(4-p)
$$

$$
1/p=
1/4+1/q
$$

$$
4<q<\infty
$$

$$
L^{4}\times L^{q}\rightarrow L^{p}
$$

$$
L_{1}^{p}\subset L^{q}
$$

$$
\mathcal{D}_{A_{0},\Phi_{0}}(a,\phi)=-\{(a,\phi),(a,\phi)\}+(\zeta,v,\psi),
$$

(3.5)

elliptic regularity for $ \mathcal{D}_{A_{0},\Phi_{0}} $ implies that $ (a,\phi)\in L_{1}^{p_{1}} $ , where $ p_{1}=2 p /(4-p) $ and $ q_{1}=4 p_{1} /(4-p_{1}) $ , so $ 2<p_{1}<4 $ and $ 4<q_{1}<\infty. $ Here, we have used the Sobolev multiplication $ L^{4}\times L^{q_{1}}\rightarrow L^{p_{1}} $ to get $ \left\{(a,\phi),(a,\phi)\right\} $ in $ L^{p_{1}} $ and the embedding $ L_{1}^{2}\subset L^{p_{1}} $ to get $ (\zeta,v,\psi) $ in $ L^{p_{1}}. $ Let $ p=2+\varepsilon $ and $ \delta=\varepsilon/(2-\varepsilon) $ , and note that

$$
\mathcal{D}_{A_{0},\Phi_{0}}
$$

$$
(a,\phi)\in L_1^{p_1}
$$

$$
p_{1}=
2p/(4-p)
$$

$$
q_{1}=4p_{1}/(4-p_{1})
$$

$$
2<p_{1}<4
$$

$$
4<q_{1}<\infty.
$$

$$
L^{4}\times L^{q_{1}}\rightarrow L^{p_{1}}
$$

$$
\{(a,\phi),(a,\phi)\}
$$

$$
L^{p_{1}}
$$

$$
L_{1}^{2}\subset L^{p_{1}}
$$

$$
L^{p_{1}}
$$

$$
\left(\zeta,v,\psi\right)
$$

$$
p=2+\varepsilon
$$

$$
\delta=\varepsilon/(2-\varepsilon)
$$

$$
p_{1}=\frac{2p}{4-p}=\frac{2p}{2-\varepsilon}=(1+\delta)p>2+\varepsilon.
$$

If $ p_{j}<4 $ , we inductively define $ p_{j+1}=2 p_{j}/(4-p_{j}) $ and $ q_{j+1}= 4 p_{j}/(4-p_{j}) $ for $ j\geq0 $ . Therefore, we have $ p_{j}>2+\varepsilon $ . Thus

$$
p_{j}<4
$$

$$
p_{j+1}=2p_j/(4-p_j)
$$

$$
q_{j+1}=
4p_{j}/(4-p_{j})
$$

$$
j\geq0
$$

$$
p_{j}>2+\varepsilon
$$

$$
p_{j+1}=\frac{2p_{j}}{4-p_{j}}>\frac{2p_{j}}{2-\varepsilon}=(1+\delta)p_{j}>p_{j}>2+\varepsilon,
$$

and so $ p_{j+1} > ( 1+\delta)^{j+1}p $ for $ j\geq0. $

$$
p_{j+1}>(1+\delta)^{j+1}p
$$

$$
j\geq0.
$$

By repeating the above regularity argument when $ 2<p_{j+1}<4 $ using (3.5) at each stage, we see that $ (a,\phi)\in L_{1}^{p_{j}} $ for $ j\geq0 $ . We continue the induction until for large enough $ j\geq0 $ , we find that $ p^{\prime}:=p_{j+1}\geq 8/3 $ and $ q^{\prime}:=q_{j+1}\geq 8 $ , so $ (a,\phi)\in L_{1}^{8/3}\subset L^{8}. $ Therefore, with $ (\zeta,v,\psi)\in L_{1}^{2}\subset L^{4} $ and using the Sobolev multiplication $ L^{8}\times L^{8}\rightarrow L^{4} $ to get $ \{(a,\phi),(a,\phi)\} $ in $ L^{4}, $ equation (3.5) gives $ (a,\phi)\in L_{1}^{4}. $ The Sobolev multiplication $ L_{1}^{4}\times L_{1}^{4}\rightarrow L_{1}^{2} $ implies that the quadratic term $ \{(a,\phi),(a,\phi)\} $ is in $ L_{1}^{2} $ and so (3.5) yields $ (a,\phi)\in L_{2}^{2}, $ as required.

$$
2<p_{j+1}<4,
$$

$$
(a,\phi)\;\in\;L_1^{p_j}
$$

$$
j\geq0
$$

$$
j\geq0
$$

$$
p^{\prime}:=
p_{j+1}\geq8/3
$$

$$
q^{\prime}:=q_{j+1}\geq8
$$

$$
(a,\phi)\in L_{1}^{8/3}\subset L^{8}
$$

$$
(\zeta,v,\psi)\in L_1^2\subset L^4
$$

$$
L^{8}\times L^{8}\rightarrow
$$

$$
\{(a,\phi),(a,\phi)\}
$$

$$
(a,\phi)\in L_1^4
$$

$$
L^{4}
$$

$$
L^{4}
$$

$$
L_{1}^{4}\times L_{1}^{4}\rightarrow L_{1}^{2}
$$

$$
\{(a,\phi),(a,\phi)\}
$$

$$
(a,\phi)\in L_2^2.
$$

$$
L_{1}^{2}
$$

Case (k=2). From the case k until $ p^{\prime} > 8 / 3 $ and $ q^{\prime} > 4. $ Hence, with equation (3.5) gives $ (a,\phi)\in L_{2}^{p^{\prime}}\subset C^{0}. $ $ L_{2}^{p^{\prime}}\times L_{2}^{2}\rightarrow L_{2}^{2} $ implies that the quadratic $ L_{2}^{2} $ and so (3.5) gives $ (a,\phi)\in L_{4}^{2}, $ as requl

1 we continue the induction when $ (\zeta,v,\psi) $ now in $ L_{2}^{2}\subset L_{1}^{p^{\prime}} $ The Sobolev multiplication term $ \{(a,\phi),(a,\phi)\} $ is then in red.

$$
p^{\prime}>8/3
$$

$$
q^{\prime}\;>\;4
$$

$$
\left(\zeta,v,\psi\right)
$$

$$
L_{2}^{2}\subset L_{1}^{p'}
$$

$$
(a,\phi)\;\in\;L_2^{p'}\;\subset\;C^0
$$

$$
L_{2}^{p^{\prime}}\times L_{2}^{2}\rightarrow L_{2}^{2}
$$

$$
\{(a,\phi),(a,\phi)\}
$$

$$
L_{2}^{2}
$$

$$
(a,\phi)\in L_{4}^{2}
$$

---

Case ($k \geq 3$). There is continuous Sobolev multiplication map $L_k^2 \times L_k^2 \rightarrow L_k^2$ and so the quadratic term $\{(a, \phi), (a, \phi)\}$ is in $L_k^2$, since $(a, \phi)$ is in $L_k^2$. Therefore, (3.5) gives $(a, \phi) \in L_{k+1}^2$.

This completes the proof of the proposition. q.e.d.

By combining Propositions 3.2 and 3.3 we obtain the desired regularity result for $L_1^2$ solutions to the inhomogeneous Coulomb gauge and PU(2) monopole equations:

Corollary 3.4. Continue the notation of Proposition 3.2. Let $(A_0, \Phi_0)$ be a $C^\infty$ pair on the $C^\infty$ bundles $(\mathfrak{su}(E), W^+ \otimes E)$ over $X$. Then there is a positive constant $\varepsilon = \varepsilon(A_0, \Phi_0)$ such that the following hold. Suppose that either

- $(a, \phi) \in L_1^2(X, \Lambda^1 \otimes \mathfrak{su}(E)) \oplus L_1^2(X, W^+ \otimes E)$, with $(\vec{\tau}, \vec{\psi}) = 0$, or
- $(a, \phi) \in L_2^2(X, \Lambda^1 \otimes \mathfrak{su}(E)) \oplus L_2^2(X, W^+ \otimes E)$

is a solution on $(\mathfrak{su}(E), W^+ \otimes E)$ to the elliptic system (3.2) over $X$, where $(\zeta, v, \psi)$ is in $L_k^2$ and $\|(a, \phi)\|_{L^4(X)} < \varepsilon$ and $k \geq 0$ is an integer. Then $(a, \phi)$ is in $L_{k+1}^2$ and there is a universal polynomial $Q_k(x, y)$, with positive real coefficients depending at most on $(A_0, \Phi_0), k$, such that $Q_k(0, 0) = 0$ and

$$\|(a, \phi)\|_{L_{k+1}^2,A_0(X)} \leq Q_k\left(\|(\zeta, v, \psi)\|_{L_{k+1}^2,A_0(X)}, \|(a, \phi)\|_{L^2(X)}\right).

In particular, if $(\zeta, v, \psi)$ is in $C^\infty$ then $(a, \phi)$ is in $C^\infty$, and if $(\zeta, v, \psi) = 0$, then

$$\|(a, \phi)\|_{L_{k+1}^2,A_0(X)} \leq C\|(a, \phi)\|_{L^2(X)}.$$

Remark 3.5. A similar sharp regularity result for solutions to the Coulomb and anti-self-dual equations (that is, $(d_\Gamma^* + d_\Gamma^+)a + (a \wedge a)^+ = v)$ on the product bundle over $S^4$ is given by Proposition 4.4.13 in [20]. The reader is forwarned that Corollary 3.4 does not apply directly to show that $L_k^2$ gluing solutions to the PU(2) monopole equation in [26] are $C^\infty$ due to the unfavorable dependence of the constant $\varepsilon(A', \Phi', p)$ on the approximate PU(2) monopole $(A', \Phi')$ when $p > 2$. However, a local version of this result, namely Corollary 3.11 below, is applicable in this situation. The point is explained further in [26].

3.2. Regularity of $L_k^2$ solutions to the PU(2) monopole equations. We explain in this subsection why an $L_k^2$ monopole $(A, \Phi)$ on the $C^\infty$ bundles ($\mathfrak{su}(E), W^+ \otimes E$) over $X$ is gauge equivalent, via an $L_{k+1}^2$ determinant-one, unitary automorphism $u$ of the bundle $E$, to a $C^\infty$ solution $u(A, \Phi)$ on ($\mathfrak{su}(E), W^+ \otimes E$) over $X$ when $k \geq 2$. This regularity result contains, as special cases, Theorem 8.8 in [30], for anti-self-dual connections, and Theorem 8.11 in [77] for Seiberg-Witten monopoles.

We will need the following observation concerning the symmetry of the Coulomb gauge equation for pairs; the corresponding fact for connections is explained in [20, p. 56].

**Lemma 3.6.** Let $(A, \Phi)$, $(A_0, \Phi_0)$ be $L_k^2$ pairs on the bundles $\mathfrak{su}(E), W^+ \otimes E$ over $X$. If $(A_0, \Phi_0)$ is in Coulomb gauge relative to $(A, \Phi)$, so $d_{A, \Phi}^{0,*}((A_0, \Phi_0)-(A, \Phi))=0$, then $(A, \Phi)$ is in Coulomb gauge relative to $(A_0, \Phi_0)$, so $d_{A_0, \Phi_0}^{0,*}((A, \Phi)-(A_0, \Phi_0))=0$.

**Proof.** The equation $d_{A, \Phi}^{0,*}((A_0, \Phi_0)-(A, \Phi))=0$ is the Euler-Lagrange equation for the functional

$$G_E^{2,k+1} \ni u \mapsto \|u(A_0, \Phi_0)-(A, \Phi)\|_L^2,$$

while the equation $d_{A_0, \Phi_0}^{0,*}((A, \Phi)-(A_0, \Phi_0))=0$ is the Euler-Lagrange equation for the functional $G_E^{2,k+1} \ni v \mapsto \|v(A, \Phi)-(A_0, \Phi_0)\|_L^2$.

But for any $u \in G_E^{2,k+1}$ we have

$$\|u(A_0, \Phi_0)-(A, \Phi)\|_L^2 = \|u^{-1}(A, \Phi)-(A_0, \Phi_0)\|_L^2,$$

and so if the functional $u \mapsto \|u(A_0, \Phi_0)-(A, \Phi)\|_L^2$ has a critical point at $u = \text{id}_E$, then the functional $u^{-1} \mapsto \|u^{-1}(A, \Phi)-(A_0, \Phi_0)\|_L^2$ will also have a critical point at $u = \text{id}_E$. q.e.d.

**Proposition 3.7.** Let $X$ be a closed, oriented, Riemannian four-manifold with spin$^c$ bundle $W$ and let $E$ be a Hermitian two-plane bundle over $X$. Let $k \geq 2$ be an integer and suppose that $(A, \Phi)$ is an $L_k^2$ solution to (2.27) on the $C^\infty$ bundles $\mathfrak{su}(E), W^+ \otimes E$ over $X$. Then there is a $L_{k+1}^2$ determinant-one, unitary automorphism $u$ of the bundle $E$ over $X$ such that $u(A, \Phi)$ is $C^\infty$ over $X$.

**Proof.** It suffices, of course, to show that there is an $L_{k+1}^2$ gauge transformation $u$ of $E$ over such that $u(A, \Phi)$ is in $L_{k+1}^2$. The $C^\infty$ pairs $(A_0, \Phi_0)$ on $\mathfrak{su}(E), W^+ \otimes E$ form a dense subspace of the space of $L_k^2$ pairs and so, given $\varepsilon=\varepsilon(A, \Phi)>0$, there is a $C^\infty$ pair $(A_0, \Phi_0)$ such that

$$\|(A, \Phi)-(A_0, \Phi_0)\|_{L_{k+1}^2} < \varepsilon.$$

---

For small enough $\varepsilon$, Proposition 2.8 gives an $L_{k+1}^2$ determinant-one, unitary automorphism $u$ of the bundle $E$ such that $u^{-1}(A_0, \Phi_0)$ is in Coulomb gauge relative to $(A, \Phi)$:

$$d_{A,\Phi}^{0,*} (u^{-1}(A_0, \Phi_0) - (A, \Phi)) = 0.$$

Now $u(d_{A,\Phi}^{0,*} (u^{-1}(A_0, \Phi_0) - (A, \Phi))) = d_{u(A,\Phi)}^{0,*} ((A_0, \Phi_0) - u(A, \Phi))$ and so

$$d_{u(A,\Phi)}^{0,*} ((A_0, \Phi_0) - u(A, \Phi)) = 0.$$

Therefore, $(A_0, \Phi_0)$ is in Coulomb gauge relative to $u(A, \Phi)$ and Lemma 3.6 implies that $u(A, \Phi)$ is in Coulomb gauge relative to $(A_0, \Phi_0)$,

$$d_{A_0,\Phi_0}^{0,*} (u(A, \Phi) - (A_0, \Phi_0)) = 0.$$

Let $(a, \phi) = u(A, \Phi) - (A_0, \Phi_0)$, so that

$$(a, \phi) \in L_k^2(X, \Lambda^1 \otimes \mathfrak{su}(E)) \oplus L_k^2(X, W^+ \otimes E);$$

the Coulomb gauge condition then takes the simpler form $d_{A_0,\Phi_0}^{0,*} (a, \phi) = 0$. Since $u(A, \Phi) = (A_0, \Phi_0) + (a, \phi)$ is an $L_k^2$ monopole, $\mathfrak{S}((A_0, \Phi_0) + (a, \phi)) = 0$ and so $(a, \phi)$ is an $L_k^2$ solution to the quasi-linear elliptic equation

$$\mathcal{D}_{A_0,\Phi_0}(a, \phi) + \{(a, \phi), (a, \phi)\} = -\mathfrak{S}(A_0, \Phi_0),$$

with $C^\infty$ data $-\mathfrak{S}(A_0, \Phi_0)$. The conclusion now follows from Proposition 3.3 with $\zeta = 0$ and $(v, \psi) = -\mathfrak{S}(A_0, \Phi_0)$. q.e.d.

One of the convenient practical consequences of Proposition 3.7 is that we can always work, modulo global $L_{k+1}^2$ gauge transformations, with $C^\infty$ rather than $L_k^2$ monopoles. For the remainder of this article, therefore, the term ‘PU(2) monopole’ is generally reserved for $C^\infty$ solutions to the perturbed PU(2) monopole equations (2.27). In a similar vein, we generally reserve the terms ‘gauge transformation’ or ‘bundle map’ for gauge transformations or bundle maps which are in $C^\infty$.

Given Proposition 3.7, we then have the following analogue of Proposition 4.2.16 in [20], the corresponding result for the moduli space of anti-self-dual connections. The proof is standard and so is left to the reader.

Corollary 3.8. Continue the hypotheses of Proposition 3.7. Then for any $k \geq 2$ the natural inclusion of topological spaces $M_{W,E}^k \hookrightarrow M_{W,E}^{k+1}$ is a homeomorphism.

---

Thus, the topology of the moduli space $M_{W,E}^{k}$ of $L_{k}^{2}$ monopoles is independent of the Sobolev spaces used in its construction for $k \geq 2$ and so we simply denote the moduli space by $M_{W,E}$.

3.3. Local regularity and interior estimates for $L_{1}^{2}$ solutions to the inhomogeneous Coulomb gauge and PU(2) monopole equations. In this section we specialize the results of §3.1 to the case where the reference pair is a trivial PU(2) monopole, so $(A_{0},\Phi_{0}) = (\Gamma,0)$ on the bundles $(\mathfrak{su}(E), W^{+} \otimes E)$, over an open subset $\Omega \subset X$, where $\Gamma$ is a flat connection.

We continue to assume that $X$ is a closed, oriented four-manifold with metric $g$, spin$^{c}$ bundle $W$, and Hermitian two-plane bundle $E$ extending those on $\Omega \subset X$. We use the inhomogenous estimates and regularity results in our proof of removable singularities for PU(2) monopoles in §4.3 and in our development of the gluing theory for PU(2) monopoles in sequels [26], [27] to the present article — especially to show that a global $L_{1}^{2}$ gluing solution $(a,\phi)$ is actually $C^{\infty}$. We use the homogeneous estimates and regularity results in §4 for our proof of the existence of an Uhlenbeck compactification for the moduli space of PU(2) monopoles.

We have the following local versions of Propositions 3.2 and 3.3 and Corollary 3.4:

Proposition 3.9. Continue the notation of the preceding paragraph. Let $\Omega' \in \Omega$ be a precompact open subset and let $2 \leq p < 4$. Then there are positive constants $\varepsilon = \varepsilon(\Omega,p)$ and $C = C(\Omega',\Omega,p)$ with the following significance. Suppose that $(a,\phi)$ is an $L_{1}^{2}(\Omega)$ solution to the elliptic system (3.2) over $\Omega$ for $(\vec{\tau},\vec{\theta}) = 0$, with $(A_{0},\Phi_{0}) = (\Gamma,0)$ and where $(\zeta,v,\psi)$ is in $L^{p}(\Omega)$. If $\|(a,\phi)\|_{L^{4}(\Omega)} < \varepsilon$, then $(a,\phi)$ is in $L_{1}^{p}(\Omega')$ and

$$\|(a,\phi)\|_{L_{1,\Gamma}(\Omega')} \leq C \left( \|(\zeta,v,\psi)\|_{L^{p}(\Omega)} + \|(a,\phi)\|_{L^{2}(\Omega)} \right).

Proof. Choose an open subset $\Omega''$ such that $\Omega' \in \Omega'' \in \Omega$. Let $\chi$ be $C^{\infty}$ cutoff function such that supp $\chi \subset \Omega''$ and $\chi = 1$ on $\Omega'$. Let $\beta$ be a cutoff function such that $\beta = 1$ on supp $\chi$ and supp $\beta \subset \Omega''$. Since $(a,\phi)$ is a solution to (3.2) with right-hand side $(\zeta,v,\psi)$ over $\Omega$, then $\chi(a,\phi)$ solves

$$\mathcal{D}_{\Gamma,0}\chi(a,\phi) + \{(a,\phi),\chi(a,\phi)\}$$

$$= \chi \mathcal{D}_{\Gamma,0}(a,\phi) + d\chi \otimes (a,\phi) + \chi\{(a,\phi),(a,\phi)\}$$

$$= \chi(\zeta,v,\psi) + d\chi \otimes (a,\phi) =: (\zeta',v',\psi').$$

---

Thus, $\chi(a, \phi)$ is an $L_1^2$ solution over $X$ to the linear elliptic system over $X$,

$$\mathcal{D}_{\Gamma,0}(b, \varphi) + \{\beta(a, \phi), (b, \varphi)\} = (\zeta', v', \psi')$$

with $L_1^2$ coefficient $\beta(a, \phi)$ and $L_1^2$ right-hand side $(\zeta', v', \psi')$. Since $\|\beta(a, \phi)\|_{L^4(X)} \leq \|(a, \phi)\|_{L^4(\Omega)}$, the proof of Proposition 3.2 implies that $\chi(a, \phi)$ is in $L_1^p$ over $X$ if $\varepsilon = \varepsilon(g, \Omega, p)$ is sufficiently small. Thus, $(a, \phi)$ is in $L_1^p$ over $\Omega'$ with

$$\|\chi(a, \phi)\|_{L^{p}_{1,\Gamma}(X)} \leq C\left(\|\zeta', v', \psi'\|_{L^{p}(X)} + \|\chi(a, \phi)\|_{L^{2}(X)}\right),$$

and therefore, for $2 \leq p < 4$, we have

$$\|(a, \phi)\|_{L^{p}_{1,\Gamma}(\Omega')} \leq C\left(\|\zeta, v, \psi\|_{L^{p}(\Omega'')} + \|(a, \phi)\|_{L^{p}(\Omega'')}\right).$$

The preceding bound and the Sobolev embedding $L_1^2 \subset L^p$ give the estimate

$$\|(a, \phi)\|_{L^{p}(\Omega'')} \leq c\|(a, \phi)\|_{L^{2}_{1,\Gamma}(\Omega'')} \leq C\left(\|\zeta, v, \psi\|_{L^{2}(\Omega)} + \|(a, \phi)\|_{L^{2}(\Omega)}\right).$$

Combining these inequalities then yields the required $L_1^p$ estimate for $(a, \phi)$ over $\Omega'$. q.e.d.

**Proposition 3.10.** Continue the notation of Proposition 3.9. Let $k \geq 1$ be an integer, and let $2 < p < \infty$. Suppose that either

- $(a, \phi)$ is an $L_1^p(\Omega)$, when $(\vec{\tau}, \vec{\psi}) = 0$, or
- $(a, \phi)$ is an $L_2^2(\Omega)$

solution to the elliptic system (3.2) over $\Omega$ with $(A_0, \Phi_0) = (\Gamma, 0)$, where $(\zeta, v, \psi)$ is in $L_k^2(\Omega)$. Then $(a, \phi)$ is in $L_{k+1}^2(\Omega')$ and there is a universal polynomial $Q_k(x,y)$, with positive real coefficients depending at most on $k$, $\Omega'$, $\Omega$, such that $Q_k(0,0) = 0$ and

$$\|(a, \phi)\|_{L^{2}_{k+1,\Gamma}(\Omega')} \leq Q_k\left(\|\zeta, v, \psi\|_{L^{2}_{k,\Gamma}(\Omega)}, \|(a, \phi)\|_{L_{1,\Gamma}(\Omega)}\right).$$

If $(\zeta, v, \psi)$ is in $C^\infty(\Omega)$, then $(a, \phi)$ is in $C^\infty(\Omega')$ and if $(\zeta, v, \psi) = 0$, then

$$\|(a, \phi)\|_{L^{2}_{k+1,\Gamma}(\Omega')} \leq C\|(a, \phi)\|_{L_{1,\Gamma}(\Omega)}.$$

---

Proof. Again, choose an open subset $ \Omega^{\prime\prime} $ such that $ \Omega^{\prime}\subset\Omega^{\prime\prime}\subset\Omega $ , let $ \chi $ be $ C^{\infty} $ cutoff function such that $ \operatorname{supp} \chi\subset\Omega $ , and $ \chi=1 $ on $ \Omega^{\prime\prime} $ and let $ \beta $ be a cutoff function such that $ \beta=1 $ on $ \operatorname{supp} \chi $ and $ \operatorname{supp} \beta\subset\Omega $ Since $ (a,\phi) $ is a solution to (3.2) with right-hand side $ (\zeta,v,\psi) $ over $ \Omega $ $ \chi(a,\phi) $ solves

$$
\Omega^{\prime\prime}
$$

$$
\Omega'\Subset\Omega''\Subset\Omega
$$

$$
\chi
$$

$$
C^{\infty}
$$

$$
\chi\subset\Omega
$$

$$
\chi=1
$$

$$
\Omega^{\prime\prime}
$$

$$
\beta
$$

$$
\beta=1
$$

$$
(a,\phi)
$$

$$
\beta\subset\Omega
$$

$$
\left(\zeta,v,\psi\right)
$$

$$
\Omega,
$$

$$
\chi(a,\phi)
$$

$$
\begin{align*}\mathcal{D}_{\Gamma,0}&\chi(a,\phi)+\{\chi(a,\phi),\chi(a,\phi)\}\\&=\chi\mathcal{D}_{\Gamma,0}(a,\phi)+d\chi\otimes(a,\phi)+\chi\{(a,\phi),(a,\phi)\}\\&\quad+\chi(\chi-1)\{(a,\phi),(a,\phi)\}\\&=\chi(\zeta,v,\psi)+d\chi\otimes(a,\phi)+\chi(\chi-1)\{(a,\phi),(a,\phi)\}\\&=:(\zeta',v',\psi').\end{align*}
$$

Note that $ \chi(\zeta,v,\psi) $ is in $ L_{k}^{2}(X), $ while $ d\chi\otimes(a,\phi) $ is in $ L_{1}^{p}(X), $ and the Sobolev multiplication $ L^{q}\times L^{q}\rightarrow L^{p_{1}} $ implies that $ \chi(\chi-1)\{(a,\phi),(a,\phi)\} $ is in $ L^{p_{1}}(X), $ where $ p_{1}=q/2=2 p/(4-p)>p. $ Thus, $ (\zeta^{\prime},v^{\prime},\psi^{\prime}) $ is in $ L^{p_{1}}(X). $

$$
\chi(\zeta,v,\psi)
$$

$$
L_{k}^{2}(X)
$$

$$
d\chi\otimes\left(a,\phi\right)
$$

$$
L_{1}^{p}(X)
$$

$$
L^{q}×L^{q}\rightarrow L^{p_{1}}
$$

$$
\chi(\chi-1)\{(a,\phi),(a,\phi)\}
$$

$$
L^{p_{1}}(X)
$$

$$
p_{1}=q/2=2p/(4-p)>p
$$

$$
\left(\zeta^{\prime},v^{\prime},\psi^{\prime}\right)
$$

$$
L^{p_{1}}(X)
$$

The proof of the case k=1 in Proposition 3.3 then implies that $ \chi(a,\phi) $ is an $ L_{1}^{p_{1}}(X), $ so $ (a,\phi) $ is in $ L_{1}^{p_{1}}(\Omega^{\prime\prime}). $ We now repeat this process for each of the remaining steps in the proof of Proposition 3.3, at each stage on successively smaller open subsets $ \Omega^{\prime\prime\prime} $ such that $ \Omega^{\prime}\subseteq\Omega^{\prime\prime}\subseteq\Omega^{\prime\prime}, $ until we obtain $ (a,\phi) $ in $ L_{k+1}^{2}(\Omega^{\prime}) $ and the desired $ L_{k+1}^{2}(\Omega^{\prime}) $ estimate. q.e.d.

$$
k=1
$$

$$
L_{1}^{p_{1}}(X),\mathrm{so}(a,\phi)
$$

$$
\chi(a,\phi)
$$

$$
L_{1}^{p_{1}}(\Omega^{\prime\prime})
$$

$$
\Omega^{\prime\prime\prime}
$$

$$
\Omega^{\prime}\Subset\Omega^{\prime\prime\prime}\Subset\Omega^{\prime\prime}
$$

$$
(a,\phi)
$$

$$
L_{k+1}^{2}(\Omega')
$$

$$
L_{k+1}^{2}(\Omega')
$$

$$
q.e.d
$$

Corollary 3.11. Continue the there is a positive constant $ \varepsilon=\varepsilon $ Suppose that either

notation of Proposition 3.10. Then (2) with the following significance.

$$
\varepsilon=\varepsilon(\Omega)
$$

- (a, $ \phi $ ) is an $ L_{1}^{2}(\Omega) $ , when $ (\vec{\tau},\vec{\vartheta})=0 $ or

$$
(a,\phi)
$$

$$
L_{1}^{2}(\Omega)
$$

$$
(\vec{\tau},\vec{\vartheta})=0,\;or
$$

- (a, $ \phi $ ) is an $ L_{2}^{2}(\Omega) $

$$
(a,\phi)
$$

$$
L_{2}^{2}(\Omega)
$$

solution to the elliptic system (3.2) over $ \Omega $ with $ (A_{0},\Phi_{0})=(\Gamma,0), $ where $ (\zeta,v,\psi) $ is in $ L_{k}^{2}(\Omega) $ and $ \|(a,\phi)\|_{L^{4}(\Omega)}<\varepsilon. $ Then $ (a,\phi) $ is in $ L_{k+1}^{2}(\Omega^{\prime}) $ and there is a universal polynomial $ Q_{k}(x,y), $ with positive real coefficients, depending at most on k, $ \Omega^{\prime},\Omega, $ such that $ Q_{k}(0,0)=0 $ and

$$
\left(A_{0},\Phi_{0}\right)=\left(\Gamma,0\right)
$$

$$
L_{k}^{2}(\Omega)
$$

$$
\|(a,\phi)\|_{L^4(\Omega)}<\varepsilon
$$

$$
\left(\zeta,v,\psi\right)
$$

$$
(a,\phi)
$$

$$
L_{k+1}^{2}(\Omega')
$$

$$
Q_{k}(x,y)
$$

$$
coef_{i}
$$

$$
k,\Omega',\Omega,
$$

$$
Q_{k}(0,0)=0
$$

$$
\|(a,\phi)\|_{L_{k+1,\Gamma}^{2}(\Omega^{\prime})}\leq Q_{k}\left(\|(\zeta,v,\psi)\|_{L_{k,\Gamma}^{2}(\Omega)},\|(a,\phi)\|_{L^{2}(\Omega)}\right).
$$

If $ (\zeta,v,\psi) $ is in $ C^{\infty}(\Omega) $ then $ (a,\phi) $ then

is in $ C^{\infty}(\Omega^{\prime}) $ , and if $ (\zeta,v,\psi)=0, $

$$
C^{\infty}(\Omega)
$$

$$
\bar{I}f\left(\zeta,v,\psi\right)
$$

$$
(a,\phi)
$$

$$
C^{\infty}(\Omega^{\prime})
$$

$$
\textit{if}\left(\zeta,v,\psi\right)=0
$$

$$
\|(a,\phi)\|_{L_{k+1,\Gamma}^{2}(\Omega^{\prime})}\leq C\|(a,\phi)\|_{L^{2}(\Omega)}.
$$

---

Corollary 3.11 thus yields a sharp local elliptic regularity result for PU(2) monopoles $(A, \Phi)$ in $L_1^2$ which are given to us in Coulomb gauge relative to $(\Gamma, 0)$: this regularity result is the key ingredient in our proof (given in §4.3) of removable point singularities for PU(2) monopoles.

Proposition 3.12. Continue the notation of Corollary 3.11. Then there is a positive constant $\varepsilon = \varepsilon(\Omega)$ and, if $k \geq 1$ is an integer, there is a positive constant $C = C(\Omega', \Omega, k)$ with the following significance. Suppose that either

- $(A, \Phi)$ is an $L_1^2$, when $(\vec{\tau}, \vec{\vartheta}) = 0$, or
- $(A, \Phi)$ is an $L_2^2$

solution to the PU(2) monopole equations (2.27) over $\Omega$, which is in Coulomb gauge over $\Omega$ relative to $(\Gamma, 0)$, so $d_\Gamma^*(A - \Gamma) = 0$, and obeys $\|(A - \Gamma, \Phi)\|_{L^4(\Omega)} < \varepsilon$. Then $(A - \Gamma, \Phi)$ is in $C^\infty(\Omega')$ and for any $k \geq 1$,

$$\|(A - \Gamma, \Phi)\|_{L^2_k,\Gamma}(\Omega') \leq C\|(A - \Gamma, \Phi)\|_{L^2(\Omega)}.$$

Proof. Corollary 3.11 applies to the $L_1^2(\Omega)$ pair $(a, \phi) = (A - \Gamma, \Phi)$ and yields the required regularity and estimates for $(A - \Gamma, \Phi)$ with $(\zeta, v, \psi) = 0$ in (3.2). q.e.d.

3.4. Estimates for PU(2) monopoles in a good local gauge. It remains to combine the local regularity results and estimates of §3.3, for PU(2) monopoles $(A, \Phi)$ where the connection $A$ is assumed to be in Coulomb gauge relative to the product SO(3) connection $\Gamma$, with Uhlenbeck’s local, Coulomb gauge-fixing theorem. We then obtain regularity results and estimates for PU(2) monopoles $(A, \Phi)$ with small curvature $F_A$, parallel to those of Theorem 2.3.8 and Proposition 4.4.10 in [20] for anti-self-dual connections.

In order to apply Corollary 3.11 we need Uhlenbeck’s Coulomb gauge-fixing result [95, Theorem 2.1 & Corollary 2.2]). Let $B$ (respectively, $\bar{B}$) be the open (respectively, closed) unit ball centered at the origin in $\mathbb{R}^4$ and let $G$ be a compact Lie group. In order to provide universal constants we assume $\mathbb{R}^4$ has its standard metric, though the results of this subsection naturally hold for any $C^\infty$ Riemannian metric, with comparable constants for metrics which are suitably close.

Theorem 3.13. There are positive constants $c$ and $\varepsilon$ with the following significance. If $2 \leq p < 4$ is a constant and

$$A \in L_1^p(B, \Lambda^1 \otimes \mathfrak{g}) \cap L_1^p(\partial B, \Lambda^1 \otimes \mathfrak{g})$$ is a connection matrix whose curvature satisfies $\|F_A\|_{L^p(B)} < \varepsilon$, then there is an gauge transformation $u \in L_2^p(B,G) \cap L_2^p(\partial B,G)$ such that $u(A) := uAu^{-1} - (du)u^{-1}$ satisfies

(1) $d^*u(A) = 0$ on $B,$
(2) $\frac{\partial}{\partial r}u(A) = 0$ on $\partial B,$
(3) $\|u(A)\|_{L_1^p(B)} \leq c\|F_A\|_{L^p(B)}$.

If $A$ is in $L_k^p(B)$, for $k \geq 2$, then $u$ is in $L_{k+1}^p(B)$, and the gauge transformation $u$ is unique up to multiplication by a constant element of $G$.

Remark 3.14. If $G$ is abelian, then the requirement that

$$\|F_A\|_{L^p(B)} < \varepsilon$$

can be omitted.

It is often useful to rephrase Theorem 3.13 in two other slightly different ways. Suppose $A$ is an $L_k^2$ connection on a $C^\infty$ principal $G$ bundle $P$ over $B$ with $k \geq 2$ and $\|F_A\|_{L^2(B)} < \varepsilon$. Then the assertions of Theorem 3.13 are equivalent to each of the following:

• There is an $L_{k+1}^2$ trivialization $\tau : P \rightarrow B \times G$ such that

(i) $d^*_\Gamma(\tau(A) - \Gamma) = 0$, where $\Gamma$ is the product connection on $B \times G,$
(ii) $\frac{\partial}{\partial r}\lrcorner(\tau(A) - \Gamma) = 0$, and
(iii) $\|(\tau(A) - \Gamma)\|_{L_1^2(B)} \leq c\|F_A\|_{L^2(B)}$.

• There is an $L_{k+1}^2$ flat connection $\Gamma$ on $P$ such that

(i) $d^*_\Gamma(A - \Gamma) = 0,$
(ii) $\frac{\partial}{\partial r}\lrcorner(A - \Gamma) = 0$, and
(iii) $\|(A - \Gamma)\|_{L_1^2(B)} \leq c\|F_A\|_{L^2(B)}$, and an $L_{k+1}^2$ trivialization $P|_B \simeq B \times G$ taking $\Gamma$ to the product connection.

We can now combine Theorem 3.13 with Proposition 3.12 to give the following analogue of Theorem 2.3.8 in [20] — the interior estimate for anti-self-dual connections with $L^2$-small curvature.

---

Corollary 3.15. Let $B \subset \mathbb{R}^4$ be the open unit ball with center at the origin with spin$^c$ structure $(\rho, W)$, let $U \in B$ be an open subset, and let $\Gamma$ be the product connection on $B \times \text{SO}(3)$. Then there is a positive constant $\varepsilon$ and if $\ell \geq 1$ is an integer, there is a positive constant $C(\ell, U)$ with the following significance. Suppose that either

- $(A, \Phi)$ is an $L_1^2$, when $(\vec{\tau}, \vec{\vartheta}) = 0$, or
- $(A, \Phi)$ is an $L_k^2$, $k \geq \max\{2, \ell\}$,

solution to the PU(2) monopole equations (2.27) over $B$ and that the curvature of the SO(3) connection matrix $A$ obeys $\|F_A\|_{L^2(B)} < \varepsilon$. Then there is an $L_{k+1}^2$ gauge transformation $u : B \to \text{SU}(2)$ such that $(u(A) - \Gamma, u\Phi)$ is in $C^\infty(B)$ with $d^*(u(A) - \Gamma) = 0$ over $B$ and

$$\|(u(A) - \Gamma, u\Phi)\|_{L_{\ell,\Gamma}^2(U)} \leq C \|F_A\|_{L^2(B)}^{1/2}.$$

Proof. Let $\varepsilon_1$ be the constant in Theorem 3.13 and note that for $\varepsilon \leq \varepsilon_1$, Theorem 3.13 (taking $G = \text{SO}(3)$) and the Sobolev embedding $L_1^2(B) \subset L^4(B)$ imply that there is an $L_{k+1}^2$ gauge transformation $u : B \to \text{SU}(2)$ (by lifting the SO(3) gauge transformation) such that

$$d^*_\Gamma(u(A) - \Gamma) = 0,$$

$$\|u(A) - \Gamma\|_{L^4(B)} \leq c_1 \|F_A\|_{L^2(B)} < c_1\varepsilon.$$

On the other hand, the quadratic equation for $\Phi$ in (2.27) and Lemma 2.26 give the $L^4$ and $L^2$ estimates,

$$\|u\Phi\|_{L^4(B)} = \|\Phi\|_{L^4(B)} \leq 2 \|F_A^+\|_{L^2(B)}^{1/2},$$

$$\|u\Phi\|_{L^2(B)} \leq 2 \|F_A\|_{L^1(B)}^{1/2}.$$

Let $\varepsilon_2$ be the constant in Proposition 3.12. Hence, if $c_1\varepsilon \leq \varepsilon_2$ and $4\sqrt{\varepsilon} \leq \varepsilon_2$, then Proposition 3.12 implies that $(u(A) - \Gamma, u\Phi)$ obeys

$$\|(u(A) - \Gamma, u\Phi)\|_{L_{\ell,\Gamma}^2(U)} \leq C \|(u(A) - \Gamma, u\Phi)\|_{L^4(B)} < \varepsilon_2.$$

since $d^*_\Gamma(u(A) - \Gamma) = 0$ and $\|(u(A) - \Gamma, u\Phi)\|_{L^4(B)} < \varepsilon_2$. The desired estimate follows by combining these inequalities for small enough $\varepsilon \leq 1$.

q.e.d.

Again, it is often useful to rephrase Corollary 3.15 in the two other slightly different ways. Suppose that $\ell \geq 1$ and that $(A, \Phi)$ is a PU(2) monopole in $L_k^2$ on $(\mathfrak{su}(E), W^+ \otimes E)$ over the unit ball $B \subset \mathbb{R}^4$ with $k \geq \max\{2, \ell\}$, $\|F_A\|_{L^2(B)} < \varepsilon$ and $U \in B$. Then the assertions of Corollary 3.15 are equivalent to each of the following:

---

• There is a $C^\infty$ trivialization $\tau : E|_B \rightarrow B \times \mathbb{C}^2$ and an $L_{k+1}^2$ determinant-one, unitary bundle automorphism $u$ of $E|_B$ such that, with respect to the product connection $\Gamma$ on $B \times \mathfrak{su}(2)$, we have

(i) $d^*_\Gamma(\tau u(A) - \Gamma) = 0$, and

(ii) $\|(\tau u(A) - \Gamma, \tau u\Phi)\|_{L_{\ell,\Gamma}^2(U)} \leq C \|F_A\|_{L^2(B)}^1/2$.

• There is an $L_{k+1}^2$ flat connection $\Gamma$ on $\mathfrak{su}(E)|_B$ such that

(i) $d^*_\Gamma(A - \Gamma) = 0$, and

(ii) $\|(A - \Gamma, \Phi)\|_{L_{\ell,\Gamma}^2(U)} \leq c \|F_A\|_{L^2(B)}^{1/2}$, and an $L_{k+1}^2$ trivialization $\mathfrak{su}(E)|_B \simeq B \times \mathfrak{su}(2)$ taking $\Gamma$ to the product connection.

Corollary 3.15 immediately yields the following local compactness result for PU(2) monopoles analogous to the local compactness result for anti-self-dual connections in [20, Corollary 2.3.9].

**Corollary 3.16.** Let $B \subset \mathbb{R}^4$ be the open unit ball and spin$^c$ structure $(\rho, W)$. Then there is a positive constant $\varepsilon_0(g, A_{\det W^+}, A_{\det E})$ with the following significance. Let $U \in B$ be an open subset and let $k \geq 2$ be an integer. If $(A_\alpha, \Phi_\alpha)$ is a sequence of PU(2) monopoles in $L_k^2$ on $(\mathfrak{su}(E), W^+ \otimes E)$ over $B$ such that

$$\|F_{A_\alpha}\|_{L^2(B)} < \varepsilon_0,

then there is a subsequence $\{\alpha'\} \subset \{\alpha\}$, a sequence of determinant-one, unitary $L_{k+1}^2$ automorphisms $\{u_{\alpha'}\}$ of $E|_B$ and a sequence of gauge equivalent pairs $(\tilde{A}_{\alpha'}, \tilde{\Phi}_{\alpha'}) := u_{\alpha'} (A_{\alpha'}, \Phi_{\alpha'})$ which converge in $L_{k,\text{loc}}^2$ on $U$ to a PU(2) monopole $(\tilde{A}, \tilde{\Phi})$ over $U$.

We will also need interior estimates for PU(2) monopoles in a good local gauge over more general simply-connected regions than the open balls considered in Corollary 3.15. Specifically, recall that a domain $\Omega \subset X$ is strongly simply-connected if it has an open covering by balls $D_1, \ldots, D_m$ (not necessarily geodesic) such that for $1 \leq r \leq m$ the intersection $D_r \cap (D_1 \cup \cdots \cup D_{r-1})$ is connected. We recall (see [20, Proposition 2.2.3] or [43, Proposition I.2.6]):

**Proposition 3.17.** If $\Gamma$ is a $C^\infty$ flat connection on a principal $G$ bundle $P$ over a simply-connected manifold $\Omega$, then there is a $C^\infty$ isomorphism $P \simeq \Omega \times G$ taking $\Gamma$ to the product connection on $\Omega \times G$.

---

More generally, if $A$ is a $C^\infty$ connection on a $G$ bundle $P$ over a simply-connected manifold-with-boundary $\bar{\Omega} = \Omega \cup \partial\Omega$ with $L^p$-small curvature (with $p > 2$), then Uhlenbeck’s theorem implies that $A$ is $L_2^p$-gauge equivalent to a connection which is $L_1^p$-close to an $L_1^p$ flat connection on $P$ (see [96, Corollary 4.3] or [20, p. 163]). The following a priori interior estimate is a straightforward generalization of [20, Proposition 4.4.10]: the method of proof is identical to that described in [20, pp. 161–162] and uses a patching argument for gauge transformations employed by Uhlenbeck in the proof of Theorem 3.6 in [95]. The required bound for the connection in terms of its curvature is obtained by covering the given open region with balls and applying the estimate of Corollary 3.15 in place of Theorem 2.3.8 in [20].

We recall from Proposition 2.16 that any automorphism of the SO(3) bundle $\mathfrak{su}(E)|_\Omega$ over a simply-connected open subset $\Omega \subset X$ lifts to a determinant-one, unitary bundle automorphism of $E|_\Omega$. The method of [20, pp. 161–162] then yields:

**Proposition 3.18.** Let $X$ be a closed, oriented, Riemannian four-manifold with spin$^c$ structure $(\rho, W)$ and let $\Omega \subset X$ be a strongly simply-connected open subset. Then there is a positive constant $\varepsilon(\Omega)$ with the following significance. For $\Omega' \in \Omega$ a precompact open subset and an integer $\ell \geq 1$, there is a constant $C(\ell, \Omega', \Omega)$ such that the following holds. Suppose $(A, \Phi)$ is a PU(2) monopole in $L_k^2$ on $(\mathfrak{su}(E), W^+ \otimes E)$ over $\Omega$ with $k \geq \max\{2, \ell\}$ such that

$$\|F_A\|_{L^2(\Omega)} < \varepsilon.$$

Then there is an $L_k^2$ flat connection $\Gamma$ on $\mathfrak{su}(E)|_\Omega'$ such that

$$\|(A - \Gamma, \Phi)\|_{L_{\ell,\Gamma}^2(\Omega')} \leq C \|F_A\|_{L^2(\Omega)}^{1/2},$$

and an $L_{k+1}^2$ trivialization $\mathfrak{su}(E)|_\Omega' \simeq \Omega' \times \mathfrak{su}(2)$ taking $\Gamma$ to the product connection.

## 4. Uhlenbeck compactification for the moduli space of PU(2) monopoles

Our goal in this section is to prove the existence of an Uhlenbeck-type compactification of the moduli space of PU(2) monopoles analogous to the Uhlenbeck compactification of the moduli space of anti-self-dual connections [20]. In §4.1 we establish the Bochner-Weitzenböck formulas for the coupled Dirac operators $D_A$ and $D^*_A$ and the a priori bounds satisfied by the section $\Phi$ and the curvature $F_A$, if $(A, \Phi)$ is a PU(2) monopole on $(\text{su}(E), W^+ \otimes E)$; these generalize the well-known a priori bounds for Seiberg-Witten monopoles [47], [62], [77]. In our proof of removable singularities we need to take into account the variation of spin$^c$ structures with the Riemannian metric and the rescaling behavior of the PU(2) equations; this variation is discussed in §4.2.

In §4.3 we prove the removability of point singularities for PU(2) monopoles. T. Parker established the removability of point singularities for solutions to the second-order coupled Yang-Mills equations, namely, $d^*_A F_A = q(\Phi)$ and $D_A \Phi = 0$, for a unitary connection $A$ on $E$ and a section $\Phi$ of $W \otimes E$, where $q$ is a certain quadratic form [70]. This generalizes the corresponding results of Uhlenbeck in the case $\Phi = 0$, where the above system then reduces to the second-order Yang-Mills equation [30], [94]; proofs of removable singularities for anti-self-dual connections are given in [20] (see also [96]). D. Salamon has given a proof of removable singularities for Seiberg-Witten monopoles [77, Chapter 9]. The arguments of Uhlenbeck and Parker rely on pointwise curvature and energy decay estimates; Salamon’s method relies on energy decay estimates and elliptic regularity results for Seiberg-Witten monopoles. The proof we give for PU(2) monopoles is rather different and instead relies heavily on our $C^\infty$ regularity result for Coulomb-gauge PU(2) monopoles in $L^2_1$ (Proposition 3.12); this is similar to the strategy used by Donaldson and Kronheimer in [20].

The technical ingredients we need for patching sequences of local gauge transformations are described in §4.4, and the Uhlenbeck closure $\bar{M}_{W,E}$ is defined in §4.5, by analogy with the corresponding definition for the moduli space of anti-self-dual connections in [20, §4.4]. In §4.5.2 we describe how the holonomy perturbations extend continuously with respect to Uhlenbeck limits and induce holonomy perturbations on all lower-level moduli spaces of PU(2) monopoles. We then define the Uhlenbeck closure for the moduli space of perturbed PU(2) monopoles.

In §4.6 we prove Theorem 1.1, which asserts that the Uhlenbeck closure $\bar{M}_{W,E}$ is compact. The main analytical ingredients in the proof comprise the regularity results and estimates of §3; the a priori bounds of §4.1 provide a ‘universal energy bound’ for a PU(2) monopole $(A, \Phi)$ and this bound plays the same role here in establishing the existence of an Uhlenbeck compactification as the usual topological bound for the energy of an anti-self-dual connection in [20]. The scale invariance of the PU(2) monopole equation described in §4.2 is used here in much the same way that the conformal invariance of the anti-self-dual equation is exploited in [20].

The parameters $\tau_0, \vartheta_0, \vec{\tau}, \vec{\vartheta}$ are chosen so that the perturbation estimates (2.29) are satisfied. These bounds follow from Proposition A.13, with $k \geq 2$ for the first inequality in (2.29) and $k \geq 3$ for the second, if

(4.1) $$\|\vec{\vartheta}\|_{\ell^1_\delta(C^r(X))} < \varepsilon_\vartheta$$ and $$\|\vec{\tau}\|_{\ell^1_\delta(C^r(X))} < \varepsilon_\tau$$,

with suitable positive constants $\varepsilon_\tau$ and $\varepsilon_\vartheta$. These constraints are needed in the proofs of the a priori estimates in Lemmas 4.2, 4.3, and 4.4 of §4.1 and hence in the proof of Theorem 4.20 in §4.6. For the remainder of the article we therefore require that $k \geq 3$.

4.1. Bochner formulas and a priori estimates for PU(2) monopoles.

In this section we apply the Bochner-Weitzenböck formula for $D_A^* D_A$ together with Kato’s inequality and the maximum principle to derive a priori estimates for solutions $(A, \Phi)$ to the PU(2) monopole equations (2.27). These estimates then lead to a vanishing result generalizing that of [98, pp. 781–782].

We first have a generalization of the usual Bochner-Weitzenböck identity for Seiberg-Witten monopoles [47], [62], [77], [89], [98].

Lemma 4.1. Let $X$ be an oriented, Riemannian, four-manifold with spin$^c$ structure $(\rho, W)$, and let $E$ be a Hermitian bundle over $X$. If $A$ denotes a U(2) connection on $E$,

$$\nabla_A : \Omega^0(W^\pm \otimes E) \rightarrow \Omega^1(W^\pm \otimes E)$$

are the covariant derivatives defined by $A$, and

$$D_A : \Omega^0(W^+ \otimes E) \rightarrow \Omega^0(W^- \otimes E)$$

the Dirac operator, then

(1a) $$D_A^* D_A = \nabla^*_A \nabla_A + \frac{1}{4} R + \rho_+(F_A^+) + \frac{1}{2} \rho_+(F_{A_L}^+),$$

(2a) $$D_A D_A^* = \nabla^*_A \nabla_A + \frac{1}{4} R + \rho_-(F_A^-) + \frac{1}{2} \rho_-(F_{A_L}^+),$$

where $R$ is the scalar curvature of the Riemannian metric and $A_L = A_{\det W^+}$ is the induced connection on $L = \det W^+ \simeq \det W^{-}$. If $A$ denotes an SO(3) connection on $\mathfrak{su}(E)$, then

(1b) $$D_A^* D_A = \nabla^*_A \nabla_A + \frac{1}{4} R + \rho_+(F_A^+) + \frac{1}{2} \rho_+(F_{A_L}^+ + F_{A_e}^+),$$

(2b) $$D_A D_A^* = \nabla^*_A \nabla_A + \frac{1}{4} R + \rho_-(F_A^-) + \frac{1}{2} \rho_-(F_{A_L}^+ + F_{A_e}^+),$$

where $A_e = A_{\det E}$ is the fixed connection on $\det E$, and the identification ad : $\mathfrak{su}(E) \simeq \mathfrak{so}(\mathfrak{su}(E))$ is implicit.

---

Proof. We just consider the first pair of identities, as the second follow immediately from the fact that

$$F(A_E) = F(A_{\text{su}(E)}) + \frac{1}{2}F(A_{\det E}) \otimes \text{id}_E.$$

Over any sufficiently small local coordinate neighborhood $U$ in $X$ we have a local spin structure and a Hermitian spin bundle $S$ such that $W|_U = S \otimes L^{1/2}$, where $L^{1/2}$ is a Hermitian line bundle over $U$ such that $(L^{1/2})^{\otimes 2} = L|_U$ and having an induced unitary connection $\frac{1}{2}A_L$. Applying the Bochner-Weitzenböck identity of [57, Theorem II.8.17] to the Hermitian bundle $S \otimes L^{1/2} \otimes E$ over $U$ with unitary connection $\nabla_A$, given by the tensor product of $\nabla^S$, $\nabla_{2^{-1}}^{L^{1/2}}A_L$, and $\nabla_A^E$, yields

$$D_A^2 = \nabla_A^*\nabla_A + \frac{1}{4}R + \rho(F_{L^{1/2}\otimes E}),$$

where $F_{L^{1/2}\otimes E}$ is the curvature of the tensor product connection $\nabla_{2^{-1}}^{L^{1/2}}A_L \otimes \text{id}_E + \text{id}_{L^{1/2}} \otimes \nabla_A^E$ on $L^{1/2} \otimes E$. Since

$$F_{L^{1/2}\otimes E} = F_{2^{-1}}A_L \otimes \text{id}_E + \text{id}_{L^{1/2}} \otimes F_A = \frac{1}{2}F_{A_L} \otimes \text{id}_E + \text{id}_{L^{1/2}} \otimes F_A,$$

we have

$$\rho(F_{L^{1/2}\otimes E}) = \frac{1}{2}\rho(F_{A_L}) \otimes \text{id}_E + \text{id}_{L^{1/2}} \otimes \rho(F_A),$$

and hence on $\Omega^0(U, W \otimes E)$,

$$D_A^2 = \nabla_A^*\nabla_A + \frac{1}{4}R + \frac{1}{2}\rho(F_{A_L}) + \rho(F_A),$$

which is plainly independent of the local splitting $W = S \otimes L^{1/2}$ and so gives an identity on $\Omega^0(X, W \otimes E)$. From the decomposition $\rho = \rho_+ \oplus \rho_-$ we see that

$$\rho^\pm(F_A)\Phi^\pm = \rho^\pm(F_A^\pm)\Phi^\pm \quad \text{and} \quad \rho^\pm(F_{A_L})\Phi^\pm = \rho^\pm(F_{A_L}^{\pm})\Phi^\pm,$$

for any $\Phi^\pm \in \Omega^0(X, W^\pm \otimes E)$, and so the result follows. q.e.d.

As in the case of the abelian monopole equations, the equations (2.27) and Lemma 4.1 combine to give a priori estimates for solutions $(A, \Phi)$ which play essential role in the proof of existence of the Uhlenbeck compactification.

---

Lemma 4.2. Let $X$ be a closed, oriented, Riemannian four-manifold with spin$^c$ structure ($\rho, W$), and Hermitian line bundle det $E$ with fixed unitary connection. Then there is a positive constant $K_1$, depending only on the $L^2$ norms of the scalar curvature $R$ and the curvatures $F(A_{\det E})$ and $F(A_{\det W^+})$, such that the following holds. If $(A, \Phi)$ is an $L_1^2$ solution on $(\mathfrak{su}(E), W^+ \otimes E)$ to the PU(2) monopole equations (2.27) over $X$, then

$$\|\Phi\|_{L^4(X)} \leq K_1 \quad \text{and} \quad \|\nabla_A \Phi\|_{L^2(X)} \leq K_1.$$

Proof. We may assume that $(A, \Phi)$ is a $C^\infty$ pair. Then Lemma 4.1 gives

$$(D_A^* D_A \Phi, \Phi) = (\nabla_A^* \nabla_A \Phi, \Phi) + \frac{1}{4}(R \Phi, \Phi) + (\rho(F_A^+) \Phi, \Phi)$$
$$+ \frac{1}{2}(\rho(F_A^+ + F_A_e^+) \Phi, \Phi),$$

while the first equation in (2.27) implies that

$$\rho(F_A^+) = \rho \vec{\tau}_A \rho^{-1}(\Phi \otimes \Phi^*)_{00}.$$

So, using the second equation in (2.27) and integration by parts, we obtain

$$\|\vec{\theta}_A \Phi\|_{L^2}^2 = \|D_A \Phi\|_{L^2}^2$$
$$= \|\nabla_A \Phi\|_{L^2}^2 + \frac{1}{4}(R \Phi, \Phi) + (\rho \vec{\tau}_A \rho^{-1}(\Phi \otimes \Phi^*)_{00} \Phi, \Phi)$$
$$+ \frac{1}{2}(\rho(F_A^+ + F_A_e^+) \Phi, \Phi).$$

Consequently, Lemmas 2.18 and 2.26, Hölder’s inequality, and the estimate for $\vec{\tau}_A$ in (2.29) leads to the bound

$$\frac{1}{2}\|\Phi\|_{L^4}^4 + \|\nabla_A \Phi\|_{L^2}^2$$
$$\leq \left(\frac{1}{4}\|R\|_{L^2} + \frac{1}{2}\|F_A^+\|_{L^2} + \frac{1}{2}\|F_A_e^+\|_{L^2} + \|\vec{\theta}_A\|_{L^4}^2\right)\|\Phi\|_{L^4}^2.$$

Thus, if $\Phi \neq 0$, the above inequality and the estimate for $\vec{\theta}_A$ in (2.29) give the required $L^4$ estimate for $\Phi$. Then the above inequality and the $L^4$ estimate for $\Phi$ yield the $L^2$ bound for $\nabla_A \Phi$. The bounds hold trivially if $\Phi \equiv 0$. q.e.d.

The preceding a priori $L^4$ estimate on the section $\Phi$ yields a priori $L^2$ bounds on the components of the curvature, $F_A^+$ and $F_A^-$, if $(A, \Phi)$ is a PU(2) monopole:

---

Lemma 4.3. Continue the notation and hypotheses of Lemma 4.2. Then there is a positive constant $K_2^+$, depending only on the $L^2$ norms of the scalar curvature $R$, the curvatures $F(A_{\det E})$ and $F(A_{\det W^+})$, and a positive constant $K_2^-$, depending only on $K_2^+$ and $p_1(\mathfrak{su}(E))$, such that if $(A, \Phi)$ is an $L_1^2$ solution on $(\mathfrak{su}(E), W^+ \otimes E)$ to the PU(2) monopole equations (2.27), then

$$\| F_A^+\|_{L^2} \leq K_2^+ \quad \text{and} \quad \| F_A^-\|_{L^2} \leq K_2^-.$$

Proof. Lemma 2.26 and the first PU(2) monopole equation in (2.27) imply that

$$\| F_A^+\|_{L^2} \leq \frac{3}{4}\|\Phi\|_{L^4}^2,$$

and so the $L^4$ bound for $\Phi$ in Lemma 4.2 gives the first estimate. The Chern-Weil integral identity (2.33) yields

$$\int_X |F_A^-|^2 dV \leq \int_X |F_A^+|^2 dV + 8\pi^2 \left(c_2(E) - \frac{1}{4}c_1(E)^2\right),$$

and so the second estimate follows from the first. q.e.d.

Lemmas 4.2 and 4.3 imply an a priori bound $K$ on the ‘energy’ of a PU(2) monopole $(A, \Phi)$ in terms of the scalar curvature $R$, the connections on det $W^+$ and det $E$ and $p_1(\mathfrak{su}(E))$:

$$\int_X \left(|F_A|^2 + |\Phi|^4 + |\nabla_A\Phi|^2\right) dV \leq K.$$

We use Lemmas 4.2 and 4.3 to provide the ‘energy bound’ assumed in our proof of removable singularities (Theorem 4.10) and we use Lemma 4.3 to give a lower bound on the second Chern class of an ideal monopole appearing in the Uhlenbeck compactification of the moduli space of PU(2) monopoles (see §4.5 and the conclusion of the proof of Theorem 4.20 in §4.6).

As in the case of the U(1) monopole equations [47], [98], the Bochner-Weitzenböck identity and the maximum principle yield a priori $C^0$ estimates for $\Phi$ and $F_A^+$ when $(A, \Phi)$ is a PU(2) monopole.

Lemma 4.4. Continue the notation and hypotheses of Lemma 4.2. Then there is a non-negative constant $K_3$, depending only on the $C^0$ norms of the scalar curvature $R$ and the curvatures $F(A_{\det E})$ and $F(A_{\det W^+})$, such that the following holds. If $(A, \Phi)$ is a $C^1$ solution on $(\mathfrak{su}(E), W^+ \otimes E)$ to the PU(2) monopole equations (2.27), then

$$\|\Phi\|_{C^0(X)}^2 \leq K_3 \quad \text{and} \quad \| F_A^+\|_{C^0(X)} \leq K_3.$$

---

Proof. We may assume that the pair $(A, \Phi)$ is $C^\infty$. The analogue of equation (6.18) of [30] for Hermitian bundles (see [77, §8.3]) reads

$$\frac{1}{2} \Delta |\Phi|^2 + |\nabla_A \Phi|^2 = \text{Re} \langle \nabla_A^* \nabla_A \Phi, \Phi \rangle,$$

where $\Delta = d^* d$ on $\Omega^0(X, \mathbb{R})$. Since $\Phi$ is continuous, $|\Phi|$ achieves its maximum at some point $x_0 \in X$, so $|\Delta |\Phi|^2(x_0) = -\nabla_{e_\mu} \nabla_{e_\mu} |\Phi|^2(x_0) \geq 0$ and thus at $x_0$:

$$\text{Re} \langle \nabla_A^* \nabla_A \Phi, \Phi \rangle \geq |\nabla_A \Phi|^2.$$

Let $\{e_\mu\}$ be a local oriented, orthonormal frame for the tangent bundle $TX$ such that $(\nabla_{e_\mu} e^\nu)_{x_0} = 0$, where $\{e^\mu\}$ is the dual coframe for the cotangent bundle $T^*X$. Since $D_A \Phi = -\vec{\vartheta}_A \Phi$ by the second equation in (2.27), at $x_0$ we have

$$\langle D_A^* D_A \Phi, \Phi \rangle = -\langle D_A^* (\vec{\vartheta}_A \Phi), \Phi \rangle$$

$$= -\langle \rho(e^\mu)(\nabla_{e_\mu} \vec{\vartheta}_A) \Phi, \Phi \rangle - \langle \rho(e^\mu) \vec{\vartheta}_A \nabla_{e_\mu}^A \Phi, \Phi \rangle,$$

and so (using the inequality $ab \leq \frac{1}{4}a^2 + b^2$) we get the following bound at $x_0$:

$$|\langle D_A^* D_A \Phi, \Phi \rangle| \leq 4 |\nabla_A \vec{\vartheta}_A\|\Phi|^2 + 4 |\vec{\vartheta}_A\|\nabla_A \Phi\|\Phi|$$

$$\leq 4 |\nabla_A \vec{\vartheta}_A\|\Phi|^2 + 4 \left(|\vec{\vartheta}_A|^2 |\Phi|^2 + \frac{1}{4}|\nabla_A \Phi|^2\right)$$

$$= 4 \left(|\nabla_A \vec{\vartheta}_A| + |\vec{\vartheta}_A|^2\right) |\Phi|^2 + |\nabla_A \Phi|^2.$$

Recall that the first PU(2) monopole equation in (2.27) gives

$$\rho(F_A^+) = \rho \vec{\tau}_A \rho^{-1}(\Phi \otimes \Phi^*)_{00}$$.

The endomorphism $\rho \vec{\tau}_A \rho^{-1}(\Phi \otimes \Phi^*)_{00}$ of $W^+ \otimes E$ lies in $\mathfrak{su}(W^+) \otimes \mathfrak{su}(E)$ and in particular is Hermitian, so

$$\text{Re} \langle \rho \vec{\tau}_A \rho^{-1}(\Phi \otimes \Phi^*)_{00} \Phi, \Phi \rangle = \langle \rho \vec{\tau}_A \rho^{-1}(\Phi \otimes \Phi^*)_{00} \Phi, \Phi \rangle,$$

and similarly for the endomorphism $\rho(F_A^+)$. We now combine Lemmas 2.26 and 4.1 and the first equation in (2.27) to get an estimate for $\Phi$ at the point $x_0$:

$$\frac{1}{2} |\Phi|^4 \leq \langle \rho \vec{\tau}_A \rho^{-1}(\Phi \otimes \Phi^*)_{00} \Phi, \Phi \rangle$$

$$= \langle \rho(F_A^+) \Phi, \Phi \rangle$$

$$= \text{Re} \langle D_A^* D_A \Phi, \Phi \rangle - \text{Re} \langle \nabla_A^* \nabla_A \Phi, \Phi \rangle - \frac{1}{4}\langle R \Phi, \Phi \rangle$$

$$- \frac{1}{2}\langle \rho(F_{A_L}^+ + F_{A_e}^+) \Phi, \Phi \rangle.$$

---

We now combine the last inequality with our estimates for $\langle D_A^*D_A\Phi, \Phi \rangle$ and $\langle \nabla_A^*\nabla_A\Phi, \Phi \rangle$ to obtain the following bound for $\Phi$ at $x_0$:

$$\frac{1}{2}|\Phi|^4 \leq 4\left(|\nabla_A\vec{\theta}_A| + |\vec{\theta}_A|^2\right)|\Phi|^2 + |\nabla_A\Phi|^2$$

$$-|\nabla_A\Phi|^2 - \frac{1}{4}R|\Phi|^2 + \frac{1}{2}\left(|F_{A_L}^+| + |F_{A_e}^+|\right)|\Phi|^2$$

$$\leq 4\left(|\nabla_A\vec{\theta}_A| + |\vec{\theta}_A|^2\right)|\Phi|^2 - \frac{1}{4}R|\Phi|^2 + \frac{1}{2}\left(|F_{A_L}^+| + |F_{A_e}^+|\right)|\Phi|^2.$$

Either $\Phi(x_0) = 0$, and so $\Phi$ is identically zero, or at the point $x_0$ the preceding inequality implies that

$$|\Phi|^2 \leq 8\left(|\nabla_A\vec{\theta}_A| + |\vec{\theta}_A|^2\right) - \frac{1}{2}\inf_X R + |F_{A_L}^+| + |F_{A_e}^+|,$$

which gives the first desired estimate. Then the second desired estimate follows from Lemma 2.26, the first equation in (2.27), and the estimate for $\vec{\theta}_A$ in (2.29). q.e.d.

We use Lemma 4.4 in §4.6 to show that the curvature of a PU(2) monopole connection $A$ concentrates at points with integer multiplicities given by the second Chern classes of limiting (ideal) anti-self-dual connections over $S^4$ (see Lemma 4.21). These $C^0$ estimates yield the following analogue of Witten’s vanishing theorem [98, §3] for U(1) monopoles over four-manifolds with non-negative scalar curvature.

Corollary 4.5. Continue the notation and hypotheses of Lemma 4.4 and suppose $K_3 \leq 0$. If $(A, \Phi)$ is a $C^1$ solution on $(\mathfrak{su}(E), W^+ \otimes E)$ to the PU(2) monopole equations (2.27), then $\Phi \equiv 0$ and $F_{A_L}^+ \equiv 0$.

Remark 4.6. The proof of Lemma 4.4 shows that

$$K_3 = \max \left\{0, -\frac{1}{2}\inf_X R + 8\|\vec{\theta}_A\|_{L^\infty_{1,A}(X)} + \|F_{A_L}^+\|_{C^0(X)} + \|F_{A_e}^+\|_{C^0(X)}\right\}.$$

In particular, we see that if $X = S^4$ has its round metric of scalar curvature $R = 1$, standard spin$^c$ structure with $c_1(W^+) = 0$ and $F_{A_L} = 0$, the Hermitian bundle $E$ has $c_1(E) = 0$ and $F_{A_e} = 0$, and we have $\vec{\theta} = 0$, then $\Phi \equiv 0$ and $A$ is an anti-self-dual SO(3) connection.

4.2. Scale invariance of the PU(2) monopole equations. In this section we describe the behavior of the PU(2) monopole under rescaling of the Riemannian metric. As is well-known, the anti-self-dual equation is conformally invariant. Although the PU(2) monopole equations are not conformally invariant they are, like the Seiberg-Witten equations, invariant under constant rescalings of the metric in a sense we describe below. The proof of the existence of an Uhlenbeck compactification (Theorem 1.1) in §4 relies on local regularity and removable singularity results for solutions to (2.27) over the unit ball $B$ in $\mathbb{R}^4$. The requirements that the $L^2$ norm of the curvature $F_A$ and the $L_1^2$ norm of section $\Phi$ be sufficiently small are met via a rescaling argument.

Suppose that $\lambda > 0$ is a constant and that the Riemannian metric $g$ on $T^*X$ is replaced by $\lambda^2g$. Since the Clifford map $\rho$ is compatible with $g$, the Clifford map

$$\rho_{\lambda^2g} \equiv \lambda\rho_g : T^*X \rightarrow \text{End}(W)$$

is compatible with $\lambda^2g$, as for any $\alpha \in \Omega^1(X, \mathbb{R})$ it satisfies

$$\rho_{\lambda^2g}(\alpha)^\dagger \rho_{\lambda^2g}(\alpha) = \lambda^2\rho_g(\alpha)^\dagger \rho_g(\alpha) = \lambda^2g(\alpha,\alpha)\text{id}_W.$$

It extends in the usual way to a linear map

$$\rho_{\lambda^2g}: \Lambda^\bullet(T^*X) \otimes \mathbb{C} \rightarrow \text{End}(W).$$

The Levi-Civita connection on $T^*X$ for the metric $g$ coincides with the Levi-Civita connection on $T^*X$ for the rescaled metric $\lambda^2g$, so the SO(4) connection on $T^*X$ induced by the unitary connection on $W$ and the Clifford map $\rho_{\lambda^2g}: T^*X \rightarrow \text{End}(W)$ is still torsion free.

**Lemma 4.7.** If $(A, \Phi)$ is a solution to the PU(2) monopole equations (2.27) for the metric $g$ on $T^*X$, then $(A, \lambda\Phi)$ is a solution to the PU(2) monopole equations for the rescaled metric $\lambda^2g$ on $T^*X$, where $\lambda$ is a positive constant.

**Proof.** The projection $P^+(\lambda^2g) = \frac{1}{2}(1 + *_{\lambda^2g})$ from $\Lambda^2(T^*X)$ to $\Lambda^+(T^*X)$ is given by $P^+(\lambda^2g) = P^+(g)$, while the induced map $\rho_{\lambda^2g}: \Lambda^2(T^*X) \rightarrow \text{End}(W)$ is given by $\rho_{\lambda^2g} = \lambda^2\rho_g$. Therefore,

$$\rho_{\lambda^2g}(\vartheta) = \lambda\rho_g(\vartheta), \quad \vartheta \in \Omega^1(X, \mathbb{C}),$$

$$D_A^{\lambda^2g} = \lambda D_A^g,$$

$$\rho_{\lambda^2g}(P^+(\lambda^2g)F_A) = \lambda^2\rho_g(P^+(g)F_A).$$

Consequently, we see from (2.27) that if $(A, \Phi)$ is a solution for the metric $g$, then $(A, \lambda\Phi)$ is a solution for the metric $\lambda^2g$. q.e.d.

---

Remark 4.8. By adapting the proof of Theorem II.5.24 in [57] we see that if $g$ is replaced by the conformally equivalent metric $h^{-2}g$, then $D_A^{h^{-2}g} = h^{5/2} D_A^g h^{-3/2}$. Thus, while the proof of Lemma 4.7 adopts without change to show that the first equation in (2.27) is invariant under the transformation $(A, \Phi) \mapsto (A, h\Phi)$ when $g \mapsto h^{-2}g$, the second equation (when $\vartheta = 0$) is invariant under the transformation $(A, \Phi) \mapsto (A, h^{3/2}\Phi)$. It is this incompatibility which prevents the PU(2) monopole equations from being conformally invariant, although they are scale invariant in the sense described above.

4.3. Removable singularities. Given the sharp local elliptic regularity result of Proposition 3.12 for PU(2) monopoles in Coulomb gauge in $L_1^2$, we can now establish a removable singularities theorem for PU(2) monopoles analogous to Theorem 4.1 in [94] in the case of the Yang-Mills equations, and Theorem 8.1 in [70] in the case of the coupled Yang-Mills equations. Our method is modelled on the proof of Theorem 4.4.12 in [20] — the removable singularities result for the anti-self-dual equation — which uses a local elliptic regularity result for $L_1^2$ solutions to the Coulomb gauge and inhomogeneous anti-self-dual equation (namely, Proposition 4.4.13 in [20]) and which in turn has its antecedent in the proof of Theorem 4.5 in [96]. This, of course, is not the only possible approach: Uhlenbeck’s original argument [94] employed a differential inequality to obtain a pointwise decay estimate for solutions near the singular point, and this was the method generalized by Parker to the case of certain coupled Yang-Mills equations; see [77, §9.2] for a proof of removable singularities for Seiberg-Witten monopoles which also uses differential inequalities.

It will be convenient to define the following annuli in $X$, given a point $x_0 \in X$ and a positive constant $r$:

$$\Omega(x_0; r) := \{ x \in X : \frac{1}{8} r < \text{dist}_g(x, x_0) < r \},$$

$$\Omega'(x_0; r) := \{ x \in X : \frac{1}{4} r < \text{dist}_g(x, x_0) < \frac{1}{2} r \} \in \Omega(x_0, r).$$

If $X = \mathbb{R}^4$ and $x_0 = 0$ and $r = 1$, we denote $\Omega = \Omega(1)$ and $\Omega' = \Omega'(1)$. We will need the following special case of Proposition 3.18.

Lemma 4.9. Let $\mathbb{R}^4$ have a $C^\infty$ Riemannian metric $g$, let $\Omega \subset \mathbb{R}^4$ be an open subset with spin-$c$ structure ($\rho, W$), let $E$ be a Hermitian two-plane product bundle over $\Omega$, and let $\Omega' \in \Omega$ be an open subset. Then there are positive constants $C, \varepsilon$ such that if $(A, \Phi)$ is a PU(2) monopole in $C^\infty$ on $(\mathfrak{su}(E), W^+ \otimes E)$ over $\Omega$ with

$$\|F_A\|_{L^2(\Omega)} < \varepsilon,$$

then there is a $C^\infty$ flat connection $\Gamma$ on $\mathfrak{su}(E)|_{\Omega'}$ such that

$$\|A - \Gamma\|_{L^4(\Omega')} + \|\nabla_\Gamma(A - \Gamma)\|_{L^2(\Omega')} \leq c\|F_A\|_{L^2(\Omega)},$$

and a $C^\infty$ trivialization $\mathfrak{su}(E)|_{\Omega'} \simeq \Omega' \times \mathfrak{su}(2)$ taking $\Gamma$ to the product connection.

The proof of Theorem 4.10 relies on a cutting off procedure to ‘smooth out’ the PU(2) monopole near the singular point, using a family of cutoff functions which we now define. Let $\chi : \mathbb{R} \rightarrow [0,1]$ be a bump function such that $\chi(t) = 1$ if $t \geq \frac{1}{2}$ and $\chi(t) = 0$ if $t \leq \frac{1}{4}$. For any $r \in (0, \varrho)$, where $\varrho$ is the injectivity radius of $(X,g)$, define a $C^\infty$ cutoff function on $X$ by setting $\chi_r(\cdot) = \chi(\text{dist}_g(\cdot,x_0)/r)$. Thus, we have $\chi_r = 0$ on the ball $B(x_0,\frac{1}{4}r)$, while $\chi_r = 1$ on $X-B(x_0,\frac{1}{2}r)$ and so $d\chi_r$ is supported in $\Omega'(x_0,r)$.

**Theorem 4.10.** Let $B \subset \mathbb{R}^4$ be a geodesic ball with $C^\infty$ metric $g$ and center at the origin, spin$^c$ structure $(\rho,W)$ over $B$, and Hermitian two-plane bundle $E$ over $B\{0\}$. Suppose $(A,\Phi)$ is a $C^\infty$ solution to the PU(2) monopole equations (2.27) on $(\mathfrak{su}(E), W^+ \otimes E)$ with $(\vec{\tau},\vec{\vartheta}) = 0$ over the punctured ball $B\{0\}$ and finite energy,

$$\int_{B\{0\}} \left(|F_A|^2 + |\Phi|^4 + |\nabla_A\Phi|^2\right) dV < \infty.$$

Then there are a Hermitian two-plane bundle $\widetilde{E}$ over $B$ with $\det \widetilde{E} = \det E$, a $C^\infty$ PU(2) monopole $(\tilde{A},\tilde{\Phi})$ on $(\mathfrak{su}(\widetilde{E}), W^+ \otimes \widetilde{E})$ over the ball $B$, and a $C^\infty$, determinant-one unitary bundle isomorphism $u : E|_{B\{0\}} \rightarrow \widetilde{E}|_{B\{0\}}$ such that

$$u(A,\Phi) = (\tilde{A},\tilde{\Phi}) \quad \text{over} \quad B\{0\}.$$

**Remark 4.11.** We restrict our attention to the case of $(\vec{\tau},\vec{\vartheta}) = 0$ in the PU(2) monopole equations (2.27) since the holonomy perturbations are undefined for the $L_1^2$ connections which arise in the proof of Theorem 4.10. However, there is no loss of generality in making this restriction as the holonomy perturbations vanish near points where curvature has bubbled off.

---

Proof. We may suppose without loss of generality that the ball $B$ has radius less than or equal to one. Since $\|F_A\|_{L^2(B)} < \infty$, then $\|F_A\|_{L^2(B_r_0)}$ tends to zero as $r_0$ tends to zero. Hence, for small enough $r_0 \in (0,1]$, we may suppose that $\|F_A\|_{L^2(B_r_0)} < \varepsilon$, where $\varepsilon$ is the constant of Lemma 4.9. Thus, for any $r \in (0,r_0)$, Lemma 4.9 provides a $C^\infty$ flat connection $\Gamma'_r$ on $\mathfrak{su}(E)|_{\Omega'(r)}$ such that

$$\|A - \Gamma'_r\|_{L^4(\Omega'(r))} \leq c \|F_A\|_{L^2(\Omega(r))},$$

where the constant $c$ is independent of $r \in (0,r_0)$. To see that the constant $c$ is indeed scale invariant, note that by Lemma 4.7 the pair $(A,r^{-1}\Phi)$ is a PU(2) monopole over $B$ with respect to the rescaled metric $g_r := r^{-2}g$, so $\Omega'_g(r) = \Omega'_{gr}(1)$ and $\Omega_g(r) = \Omega_{gr}(1)$. We then apply Lemma 4.9 to the annuli $\Omega'_{gr}(1) \in \Omega_{gr}(1)$ and observe that the $L^4$ norm on one-forms and the $L^2$ norm on two-forms are scale invariant.

Lemma 4.9 also provides a $C^\infty$ trivialization $\mathfrak{su}(E)|_{\Omega'(r)} \simeq \Omega'(r) \times \mathfrak{su}(2)$ taking $\Gamma'_r$ to the product connection on $\Omega'(r) \times \mathfrak{su}(2)$. We can then define a smooth SO(3) bundle $V_r$ over $B$ by setting

$$V_r := \begin{cases}
B\left(\frac{1}{2}r\right) \times \mathfrak{su}(2) & \text{over } B\left(\frac{1}{2}r\right), \\
\mathfrak{su}(E) & \text{over } B-B\left(\frac{1}{4}r\right),
\end{cases}$$

recalling that $\Omega'(r) = B\left(\frac{1}{2}r\right) - \bar{B}\left(\frac{1}{4}r\right)$. Let $\Gamma'_r$ denote the $C^\infty$ flat connection on $V_r$ over the ball $B\left(\frac{1}{2}r\right)$, extending $\Gamma'_r$ on $\mathfrak{su}(E)|_{\Omega'(r)}$ via the product connection on $B\left(\frac{1}{2}r\right) \times \mathfrak{su}(2)$, and let $E_r$ be the smooth U(2) bundle over $B$ with det $E_r = \det E$ and $\mathfrak{su}(E_r) = V_r$ over $B$.

Now let $(A_r,\Phi_r)$ be the $C^\infty$ pair on $B$ defined by

$$(A_r,\Phi_r) := \begin{cases}
(\Gamma'_r + \chi_r(A - \Gamma'_r), \chi_r\Phi) & \text{over } B\left(\frac{1}{2}r\right), \\
(A,\Phi) & \text{over } B \setminus B\left(\frac{1}{4}r\right),
\end{cases}$$

where we note that $\chi_r = 0$ on $B\left(\frac{1}{4}r\right)$ and $\chi_r = 1$ on $B-B\left(\frac{1}{2}r\right)$. To estimate the $L^2$ norm of $F_{Ar}$, note that over $B-B\left(\frac{1}{2}r\right)$ we have $A_r = A$ and $F_{Ar} = F_A$, while over $B\left(\frac{1}{2}r\right)$,

$$F_{Ar} = \chi_r F_A + d\chi_r \wedge (A - \Gamma'_r) + (\chi_r^2 - \chi_r)(A - \Gamma'_r) \wedge (A - \Gamma'_r).$$

Hence, by (4.3), we have

$$\|F_{Ar}\|_{L^2(\Omega'(r))} \leq \|F_A\|_{L^2(\Omega'(r))} + \|d\chi_r\|_{L^4(\Omega'(r))} \|A - \Gamma'_r\|_{L^4(\Omega'(r))} + \|A - \Gamma'_r\|_{L^4(\Omega'(r))}^2.$$

---

Therefore, since $\|d\chi_r\|_{L^4(\Omega'(r))} \leq c_0$, for a constant $c_0$ independent of $r \in (0,\infty)$, there is a positive constant $c$, independent of $r \in (0,r_0)$, such that

$$\|F_{A_r}\|_{L^2(B_{r_0})} \leq c\left(\|F_A\|_{L^2(B_{r_0})} + \|F_A\|_{L^2(B_{r_0})}^2\right) \leq c\|F_A\|_{L^2(B_{r_0})}.$$