---
retention_scope: session
part: 5
total_parts: 6
---

[Part 5/6 of: PU(2) Monopoles. I: Regularity, Uhlenbeck Compactness, and Transversality]

since $(v,\psi) = 0$ on $\bar{B}_I(A)$ and $D\mathfrak{S}^0 \neq D\mathfrak{S}$ only on $B_I(A)$, while $D\mathfrak{S}^0 = D\mathfrak{S}$ on $X - B_{I(A)}$.

Without loss of generality, we may scale the Dirac equation in (2.21) by $1/\sqrt{2}$. We then have

$$D\mathfrak{S}^0(D\mathfrak{S}^0)^* = \begin{pmatrix} d_A^+ d_A^{+,*} & 0 \\ 0 & \frac{1}{2} D_A D_A^* \end{pmatrix} + \text{First-order differential terms},$$

and so by the Bochner formulas of Lemma 4.1 and [30, Eq. (6.26)], the Laplacian $D\mathfrak{S}^0(D\mathfrak{S}^0)^*$ is a second order elliptic differential operator with scalar principal symbol (given by the metric $\frac{1}{2} g$ on $T^* X$). The desired conclusion then follows from Aronszajn’s unique continuation theorem [5]. q.e.d.

## Remark 5.10.

1. Aronszajn’s theorem does not apply without the given restriction on the open set $U$ in the statement of Lemma 5.9, as the Laplacian $(D\mathfrak{S})(D\mathfrak{S})^*$ is not a purely differential operator over all of $X$. One can see from equations (5.3) and (5.4) that the problem terms are those appearing in the last line of each displayed equation: the operator $\delta m_{j,\ell,\alpha}/\delta A$ acting on $a \in \Omega^1(\mathfrak{su}(E))$ is an integral operator, as is clear from the formula (A.7) for the differential of the holonomy with respect to the connection.

2. Lemma 5.9 can also be proved without using Aronszajn’s theorem explicitly and instead applying the Agmon-Nirenberg unique continuation theorem (Theorem 5.25) to the equation $(D\mathfrak{S})^*(v,\psi) = 0$, and mimicking the existing application in the proof of Theorem 5.11. Indeed, this second proof of Lemma 5.9 is virtually identical to the proof of Theorem 5.11. We leave the details to the interested reader, as the preceding use of Aronszajn’s theorem appears easier to us. We note that Aronszajn’s theorem can be derived from that of Agmon-Nirenberg (see [3]).

If $(v, \psi)$ is an $L_{k-1}^2$ element of the cokernel of $D\mathfrak{S}$, then elliptic regularity for the Laplacian $D\mathfrak{S}(D\mathfrak{S})^*$, with $C^{r-1}$ coefficients, implies that $(v, \psi)$ is in $C^{r+1}$. Our proof of Theorem 5.2 also relies on the following ‘unique continuation’ result for reducible monopoles:

**Theorem 5.11.** If $(A, \Phi)$ is a $C^r$ solution to the perturbed PU(2) monopole equations (2.27) with $\Phi \neq 0$ over a connected, oriented, smooth four-manifold $X$ with $C^r$ Riemannian metric, and $(A, \Phi)$ is reducible on a non-empty open subset $U \subset X$ with $\bar{B}(x_j, R_0) \subset U$ for all $j$ such that $\beta_j[A] > 0$, then $(A, \Phi)$ is reducible on $X$.

The proof of Theorem 5.11 is lengthy, so we defer it to §5.3.

**Proof of Theorem 5.2, given Proposition 5.8 and Theorem 5.11.** Let $(\tau_0, \vartheta_0, \vec{\tau}, \vec{\vartheta}, A, \Phi)$ be a $C^r$ representative for a point in $\mathfrak{M}_{W,E}^{*0}$, so that $A$ is irreducible and $\Phi \neq 0$, and suppose $(v, \psi)$ is in the cokernel of $D\mathfrak{S}$. By definition of $N_b$ in §2.5.2, the set

$$J(A) := \{ j : 1 \leq j \leq N_b \text{ and } \beta_j[A] > 0 \}$$

is non-empty. Since $A$ is irreducible on $X$, Theorem 5.11 implies that $A|_{B(x_j', 2R_0)}$ must be irreducible for some $j' \in \{1, \ldots, N_b\}$ such that $\beta_j'A] > 0$; otherwise, $A|_{B(x_j', 2R_0)}$ would be reducible for all $j$ such that $\beta_j[A] > 0$, and Theorem 5.11 would imply that $A$ would be reducible over all of $X$, contradicting our assumption that $A$ is irreducible. By Proposition 5.8 we see that $(v, \psi)|_{B(x_j, R_0)} \equiv 0$ for all $j$ such that $\beta_j[A] > 0$ and $A|_{B(x_j, 2R_0)}$ is irreducible, so $(v, \psi) \equiv 0$ on $X$ by Lemma 5.9.

q.e.d.

The proof of Proposition 5.8 occupies the remainder of this subsection. We first note that since $\Phi$ is in the kernel $D_A + \vec{\vartheta} \cdot \vec{\mathfrak{m}}(A)$, it has the unique continuation property by Aronszajn’s Theorem [5]:

**Lemma 5.12.** If $(D_A + \rho(\vartheta_0) + \vec{\vartheta} \cdot \vec{\mathfrak{m}}(A))\Phi = 0$ and $\Phi|_U \equiv 0$ for some non-empty open subset $U \subset X$, then $\Phi \equiv 0$.

**Proof.** The perturbed Dirac operator $D_A + \rho(\vartheta_0) + \vec{\vartheta} \cdot \vec{\mathfrak{m}}(A)$ differs from $D_A$ by a zeroth order term and so

$$(D_A + \rho(\vartheta_0) + \vec{\vartheta} \cdot \vec{\mathfrak{m}}(A))^*(D_A + \rho(\vartheta_0) + \vec{\vartheta} \cdot \vec{\mathfrak{m}}(A))$$

$$= D_A^*D_A + \text{First order terms.}$$

---

The Bochner formula of Lemma 4.1 then implies that the above Laplacian is a second order elliptic differential operator with scalar principal symbol (given by the metric $g$ on $T^*X$). The conclusion now follows from Aronszajn’s unique continuation theorem [5]. q.e.d.

We shall use the following linear algebra result to show that $v \in C^{r+1}(X, \Lambda^+ \otimes \mathfrak{su}(E))$ vanishes on a ball:

**Lemma 5.13.** Let $M,N$ be elements of $(\Lambda^+ \otimes \mathfrak{su}(E))|_x$. Suppose $\mathfrak{m}_1, \mathfrak{m}_2, \mathfrak{m}_3$ span $\mathfrak{su}(E)|_x$. If

(5.7) $$\langle \tau_0 M, N \rangle + \sum_{l=1}^{3} \langle (\tau_l \otimes \mathrm{ad}(\mathfrak{m}_l)) M, N \rangle = 0$$

for all $\tau_0, \tau_1, \tau_2, \tau_3 \in \mathfrak{gl}(\Lambda^+)|_x$, then either $M = 0$ or $N = 0$.

Proof. If $\langle \tau_0 M, N \rangle = 0$ for all $\tau_0 \in \mathfrak{gl}(\Lambda^+)|_x$, then by the proof of [30, Lemma 3.7], the images in $\mathfrak{su}(E)|_x$ of $M, N \in \mathrm{Hom}(\Lambda^+|_x, \mathfrak{su}(E)|_x)$ are orthogonal. (Although their lemma refers to an element of $\mathrm{Hom}(\Lambda^+|_x, \mathfrak{su}(E)|_x)$ and an element of $\mathrm{Hom}(\Lambda^-|_x, \mathfrak{su}(E)|_x)$, we can choose any isomorphism between $\Lambda^+|_x$ and $\Lambda^-|_x$ to translate the result.) We can therefore assume that $M$ has rank one and $N$ has rank less than or equal to two. (If $M$ is rank two and $N$ is rank one, we can reverse their roles by using adjoints.) If both $M \neq 0$ and $N \neq 0$ let

$$M = u \otimes m \quad \text{and} \quad N = v_1 \otimes n_1 + v_2 \otimes n_2,$$

where $u, v_1, v_2 \in \Lambda^+|_x$ and $m, n_1, n_2 \in \mathfrak{su}(E)|_x$. Since the images of $M$ and $N$ in $\mathfrak{su}(E)|_x$ are orthogonal, we have $\langle m, n_1 \rangle = 0 = \langle m, n_2 \rangle$; without loss of generality, we can assume that $\langle n_1, n_2 \rangle = 0$. (If $N$ is rank one, $n_2$ can be any element of $\mathfrak{su}(E)|_x$ completing $m, n_1$ to an orthogonal basis of $\mathfrak{su}(E)|_x$.) Under the isomorphism $\mathfrak{su}(E)|_x \simeq \mathbb{R}^3$, the adjoint representation is given by the cross-product. We can find $f_l \in \mathbb{R}$ such that $n_2 = \sum_l f_l \mathfrak{m}_l$, so

(5.8) $$\sum_{l=1}^{3} \langle \mathrm{ad}(f_l \mathfrak{m}_l) m, n_1 \rangle = \langle [n_2, m], n_1 \rangle \neq 0,$$

(5.9) $$\sum_{l=1}^{3} \langle \mathrm{ad}(f_l \mathfrak{m}_l) m, n_2 \rangle = \langle [n_2, m], n_2 \rangle = 0.$$

By assumption, $M \neq 0$ and $N \neq 0$, so $u \neq 0$ and either $v_1 \neq 0$ or $v_2 \neq 0$; we may suppose without loss of generality that $v_1 \neq 0$. Thus, we can find $\tau \in \mathfrak{gl}(\Lambda^+)|_x$ such that $\tau u = v_1$, and so choosing $\tau_l = f_l\tau$
for $l = 1,2,3$ and $\delta\tau_0 = 0$, we have

$$\sum_{l=1}^{3} \langle (\tau_l \otimes \mathrm{ad}(\mathfrak{m}_l)) M, N \rangle = \sum_{l=1}^{3} \langle \tau \otimes \mathrm{ad}(f_l \mathfrak{m}_l) M, N \rangle$$
$$= \langle (\tau \otimes \mathrm{ad}(n_2)) M, N \rangle$$
$$= \langle (\tau \otimes \mathrm{ad}(n_2)) (u \otimes m), v_1 \otimes n_1 + v_2 \otimes n_2 \rangle$$
$$= \langle \tau u \otimes [n_2, m], v_1 \otimes n_1 + v_2 \otimes n_2 \rangle$$
$$= \langle \tau u, v_1 \rangle \langle [n_2, m], n_1 \rangle + \langle \tau u, v_2 \rangle \langle [n_2, m], n_2 \rangle$$
$$= |v_1|^2 \langle [n_2, m], n_1 \rangle \neq 0 \text{ by (5.8) and (5.9)},$$

contradicting our hypothesis in (5.7). Hence, either $M = 0$ or $N = 0$, as desired. q.e.d.

Remark 5.14. Lemma 5.13 does not hold if the rank of $E$ is greater than two. If $a,b \in \mathfrak{su}(E)$, the above arguments would only allow one to conclude that

$$0 = \langle [\mathfrak{m}, a], b \rangle = \langle \mathfrak{m}, [a, b] \rangle$$

for all $\mathfrak{m} \in \mathfrak{su}(E)$, so $[a,b] = 0$ and $a,b$ are simultaneously diagonalizable. The subspace of diagonal elements of $\mathfrak{su}(n)$ has dimension $n-1$, so this would not contradict the orthogonality of $a,b$ if $n > 2$.

Lemma 5.15. Continue the hypotheses of Proposition 5.8 and suppose $B(x_j,R_0)$ is a ball supporting holonomy perturbations for $A$. Then $v \equiv 0$ on $B(x_j,R_0)$.

Proof. By hypothesis, there are holonomy sections $\mathfrak{m}_l \equiv \mathfrak{m}_{j,l,\alpha}(A)$, $l = 1,2,3$, which span $\mathfrak{su}(E)|_y$, for any point $y \in B(x_j,R_0)$. Let $\delta\tau_l := \delta\tau_{j,l,\alpha} \in \Omega^0(\mathfrak{gl}(\Lambda^+))$, $l = 1,2,3$, denote the corresponding coefficients, and let $\delta\tau$ be a sequence with all other coefficients equal to zero.

By the hypothesis of Proposition 5.8, we have

$$(D\mathfrak{S}(\delta\tau_0, \delta\vartheta_0, \delta\tau, \delta\vec{\vartheta}, a, \phi), (v, \psi))_{L^2} = 0$$

for all $(\delta\tau_0, \delta\vartheta_0, \delta\tau, \delta\vec{\vartheta}, a, \phi)$, and so

$$0 = (D\mathfrak{S}(\delta\tau_0, 0, \delta\tau, 0, 0, 0), (v, \psi))_{L^2}$$
$$= (D\mathfrak{S}_1(\delta\tau_0, 0, \delta\tau, 0, 0, 0), v)_{L^2}$$
$$= ((\delta\tau_0 \otimes \mathrm{id}_{\mathfrak{su}(E)} + \delta\tau \cdot \vec{\mathfrak{m}}(A))\rho^{-1}(\Phi \otimes \Phi^*)_{00}), v)_{L^2}$$
$$= (\delta\tau_0\rho^{-1}(\Phi \otimes \Phi^*)_{00}, v)_{L^2} + \sum_{l=1}^{3}(\delta\tau_l \otimes \mathrm{ad}(\mathfrak{m}_l)\rho^{-1}(\Phi \otimes \Phi^*)_{00}, v)_{L^2}.$$

---

Taking a sequence of $\delta\tau_l$'s which approximate $\delta\tau_{l,y}\delta(\cdot,y)$, where $\delta(\cdot,y)$ is the Dirac delta distribution supported at $y$ and $\delta\tau_{l,y} \in \mathfrak{gl}(\Lambda^+)|_y$, we obtain the pointwise identity

$$\langle \delta\tau_{0,y}\rho^{-1}(\Phi \otimes \Phi^*)_{00}|_y,v|_y\rangle + \sum_{l=1}^{3}\langle \delta\tau_{l,y} \otimes \mathrm{ad}(\mathfrak{m}_l)\rho^{-1}(\Phi \otimes \Phi^*)_{00}|_y,v|_y\rangle = 0,

for all $\delta\tau_{l,y} \in \mathfrak{gl}(\Lambda^+)|_y$, $l = 0,1,2,3$. Lemma 5.13 then implies that either $\rho^{-1}(\Phi \otimes \Phi^*)_{00}|_y = 0$, and thus $\Phi|_y = 0$ by Lemma 2.19, or else $v|_y = 0$. If $v|_y \neq 0$, we see that $\Phi$ would be zero on the nonempty open subset $\{v \neq 0\} \cap B(x_j,R_0)$. But then Lemma 5.12 would imply that $\Phi \equiv 0$ on $X$, contradicting our assumption that $\Phi \neq 0$. Thus, $v \equiv 0$ on $B(x_j,R_0)$, as desired. q.e.d.

The following similar argument shows that $\psi \equiv 0$ on the ball $B(x_j,R_0)$. Note that having only $v \equiv 0$ or $\psi \equiv 0$ on an open set does not suffice to contradict Lemma 5.9, as the non-vanishing result of Lemma 5.9 applies to the pair $(v,\psi)$. We again begin with a linear algebra lemma:

**Lemma 5.16.** Let $S^{+} \in (W^{+} \otimes E)|_x$ and $S^{-} \in (W^{-} \otimes E)|_x$. If $\mathfrak{m}_0,\ldots,\mathfrak{m}_3$ span $\mathfrak{u}(E)|_x$ and

$$\sum_{l=0}^{3}\langle (\vartheta_l \otimes \mathfrak{m}_l)S^{+},S^{-}\rangle = 0

for all $\vartheta_0,\ldots,\vartheta_3 \in \mathrm{Hom}_{\mathbb{C}}(W^{+},W^{-})|_x$, then $S^{+}=0$ or $S^{-}=0$.

**Proof.** Because $\{\mathfrak{m}_l\}_{l=0}^{3}$ spans $\mathfrak{u}(E)|_x$ and $\mathfrak{gl}(E)|_x = \mathfrak{u}(E)|_x \oplus i\mathfrak{u}(E)|_x$, we have $\mathfrak{gl}(E)|_x = \mathfrak{u}(E)|_x \otimes_{\mathbb{R}}\mathbb{C}$, and the set $\{\mathfrak{m}_l\}_{l=0}^{3}$ is a complex basis for $\mathfrak{gl}(E)|_x$. Thus, any element of

$$\mathrm{Hom}_{\mathbb{C}}(W^{+} \otimes_{\mathbb{C}} E,W^{-} \otimes_{\mathbb{C}} E)|_x \simeq \mathrm{Hom}_{\mathbb{C}}(W^{+},W^{-})|_x \otimes_{\mathbb{C}} \mathfrak{gl}(E)|_x

can be written as $\sum_{l=0}^{3}\vartheta_l \otimes \mathfrak{m}_l$, for some $\vartheta_l \in \mathrm{Hom}_{\mathbb{C}}(W^{+},W^{-})|_x$, $l = 0,\ldots,3$. Thus, if $S^{+} \neq 0$, the hypothesis implies that $S^{-}=0$ and conversely, if $S^{-} \neq 0$, then $S^{+}=0$. q.e.d.

**Lemma 5.17.** Continue the hypotheses of Proposition 5.8 and suppose $B(x_j,R_0)$ is a ball supporting holonomy perturbations for $A$. Then $\psi \equiv 0$ on $B(x_j,R_0)$.

**Proof.** By hypothesis, there are holonomy sections $\mathfrak{m}_l := \mathfrak{m}_{j,l,\alpha}(A)$, $l = 1,2,3$, which span $\mathfrak{su}(E)|_y$, for any point $y \in B(x_j,R_0)$, and so

---

$\{m_l\}_{l=0}^3$ spans $u(E)|_y$, where $m_0 := i \cdot id_E$. Let $\delta \vartheta_l := \delta \vartheta_{j,l,\alpha} \in \Omega^1(X, \mathbb{C})$, $l = 1, 2, 3$, denote the corresponding coefficients, and let $\delta \vec{\vartheta}$ be a perturbation sequence with all other coefficients equal to zero.

By the hypothesis of Proposition 5.8, we have

$$
(D\mathfrak{S}(\delta\tau_0, \delta \vartheta_0, \delta \vec{\tau}, \delta \vec{\vartheta}, a, \phi), (v, \psi))_{L^2} = 0
$$

for all $(\delta\tau_0, \delta \vartheta_0, \delta \vec{\tau}, \delta \vec{\vartheta}, a, \phi)$, and so

$$0 = (D\mathfrak{S}(0, \delta \vartheta_0, 0, \delta \vec{\vartheta}, 0, 0), (v, \psi))_{L^2}$$

$$= (D\mathfrak{S}_2(0, \delta \vartheta_0, 0, \delta \vec{\vartheta}, 0, 0), \psi)_{L^2}$$

$$= (\rho(\delta \vartheta_0)\Phi + \delta \vec{\vartheta} \cdot \mathfrak{m}(A)\Phi, \psi)_{L^2}$$

$$= \sum_{l=0}^{3} (\rho(\delta \vartheta_l) \otimes m_l\Phi, \psi)_{L^2}.$$

Taking a sequence of $\delta \vartheta_l$'s which approximate $\delta \vartheta_{l,y}\delta(\cdot, y)$, where $\delta(\cdot, y)$ is the Dirac delta distribution supported at $y$ and $\delta \vartheta_{l,y} \in T^*X|_y \otimes \mathbb{C}$, we obtain the pointwise identity

$$\sum_{l=0}^{3} \langle \rho(\delta \vartheta_{l,y}) \otimes m_l\Phi|_y, \psi|_y \rangle = 0,$$

for all $\delta \vartheta_{l,y} \in T^*X|_y \otimes \mathbb{C}$, $l = 0, 1, 2, 3$. Lemma 5.16 then implies that either $\Phi|_y = 0$ or $\psi|_y = 0$. If $\psi|_y \neq 0$, then $\Phi$ would be zero on the nonempty open subset $\{\psi \neq 0\} \cap B(x_j,R_0)$. Consequently, Lemma 5.12 would imply that $\Phi \equiv 0$ on $X$, again contradicting our assumption that $\Phi \neq 0$. Thus, $\psi \equiv 0$ on $B(x_j,R_0)$, as desired. q.e.d.

We can now conclude the proof of Proposition 5.8:

Proof of Proposition 5.8. If $(v, \psi)$ is in the cokernel of $D\mathfrak{S}$ and $B(x_j,R_0)$ is a ball supporting holonomy perturbations for $A$, then $(v, \psi) \equiv 0$ on $B(x_j,R_0)$ by Lemmas 5.15 and 5.17. q.e.d.

5.3. Local reducibility implies global reducibility. The goal of this section is to prove Theorem 5.11. The argument has two main ingredients: a local extension result for stabilizers of pairs which are reducible on a ball and a description of how these local stabilizers fit together to give a stabilizer and thus a reducible pair on the whole manifold.

---

Remark 5.18. The fact that an anti-self-dual connection which is reducible on an open subset is necessarily reducible on all of $X$ is an essential part of Donaldson and Kronheimer’s proof of transversality for the moduli space of anti-self-dual connections in [20, §4.3]. The original argument of Freed and Uhlenbeck [30, pp. 57-58] constructs a parallel section $\zeta$ of $\mathfrak{su}(E)$ on the set $\{F_A \neq 0\}$. Because the connection $A$ is anti-self-dual and therefore Yang-Mills, so $d^*_A F_A = 0 = d_A F_A$, the set $\{F_A \neq 0\}$ is open, dense and connected. The section $\zeta$ cannot develop any holonomy on $\{F_A = 0\}$, so it extends across all of $X$, showing that $A$ is globally reducible. This argument does not work in the case of PU(2) monopoles because the connection $A$ is not necessarily Yang-Mills and our argument does not show that the existence of a nonzero element $(v, \psi)$ in Coker $D\mathfrak{S}$ implies that the connection $A$ is reducible on a dense open subset of $X$.

We first state the local extension result for pair stabilizers and defer its lengthy proof until after that of Theorem 5.11. Generalizations due to Taubes of the analogous result for anti-self-dual connections, namely Lemma 4.3.21 in [20], appear as Theorems 4 and 5 in [88]. As Taubes points out in [88, p. 35], unique continuation theorems for solutions to the anti-self-dual equation do not seem to follow from standard results for elliptic partial differential equations (such as those of Aronszajn [5]) since the anti-self-dual equation does not linearize as an elliptic equation for the connection. Because the PU(2) monopole equations do not linearize as an elliptic system for pairs, the same remarks apply here as well. Rather than rely on the Agmon-Nirenberg theorem for the unique continuation property for a general class of ordinary differential equations (Theorem 5.25), Taubes proves the required unique continuation property directly for the ordinary differential equation induced by the anti-self-dual equation on a cylinder. (As Mrowka pointed out to us, it should also be possible to deduce the unique continuation results of [88] by studying the anti-self-dual equation on a ball and applying the Fredholm theory of [6].) Recall that $B(x_0, r_0) \subset X$ denotes an open geodesic ball with center at the point $x_0$ and radius $r_0$. Also, recall that if $[A, \Phi]$ is a point in $M_{W, E}$, then Proposition 3.7 implies that it has a ‘smooth’ (that is, $C^r$) representative $(A, \Phi)$ solving (2.27).

Proposition 5.19. Let $X$ be an oriented, smooth four-manifold with $C^r$ Riemannian metric $g$ and injectivity radius $\varrho = \varrho(x_0)$ at a point $x_0$. Suppose that $0 < r_0 < r_1 \leq \frac{1}{2}\varrho$. Let $(A, \Phi)$ be a $C^r$ pair solving the PU(2) monopole equations (2.27) on $X$. If $u$ is a $C^{r+1}$ gauge transformation of $ E |_{B(x_{0}, r_{0})} $ satisfying u(A, $ \Phi )=(A,\Phi) $ on $ B(x_{0},r_{0}) $ and if either $ B(x_{j},R_{0})\cap B(x_{0},r_{1})=\emptyset $ or $ B(x_{j},R_{0})\subset B(x_{0},r_{0}) $ , for all balls $ B(x_{j},R_{0}) $ for which $ \beta_{j}[A]>0 $ , then there is an extension of u to a $ C^{r+1} $ gauge transformation $ \hat{u} $ of $ E |_{B(x_{0},r_{1})} $ with $ \hat{u}(A,\Phi)=(A,\Phi) $ on $ B(x_{0},r_{1}). $

$$
\left|E\right|_{B\left(x_{0},r_{0}\right)}
$$

$$
u(A,\Phi)=(A,\Phi)
$$

$$
B(x_{0},r_{0})
$$

$$
B(x_{j},R_{0})\cap B(x_{0},r_{1})=\varnothing
$$

$$
B(x_{j},R_{0})\subset B(x_{0},r_{0})
$$

$$
B(x_{j},R_{0})
$$

$$
\beta_{j}[A]>0
$$

$$
a C^{r+1}
$$

$$
\hat{u}(A,\Phi)=(A,\Phi)
$$

$$
E|_{B(x_0,r_1)}
$$

$$
B(x_{0},r_{1})
$$

Remark 5.20. This extension result only holds on domains $ B ( x_{0}, r_{1} ) \backslash\bar{B} ( x_{0}, r_{0} ) $ where the perturbations vanish because the perturbation terms $ \mathfrak{m}_{j,l,\alpha}(A) $ depend not just on the connection A and its derivatives at a point, but rather on the connection A over open neighborhoods in X . Although the unique continuation theorem of [4] does allow certain integral terms, it still does not cover the perturbations we consider here because of their non-local dependence on A.

$$
B(x_{0},r_{1})\backslash\bar{B}(x_{0},r_{0})
$$

$$
\mathfrak{m}_{j,l,\alpha}(A)
$$

We digress briefly to introduce some useful facts about stabilizer subgroups of $ ^{\circ}\mathcal{G}_{E}. $

$$
^{\circ}\mathcal{G}_{E}
$$

Lemma 5.21. If $ u \in \mathrm{Stab}_{\Phi} $ for $ \Phi\in C^{0}(X,W^{+}\otimes E) $ and $ u\neq \mathrm{id}_{E}, $ then $ \Phi $ is rank one. If $ u \in S_{Z}^{1} $ and $ u\neq \mathrm{id}_{E}, $ then $ \Phi\equiv0 $ on X.

$$
\text{"}u\in\mathrm{Stab_{\Phi}}\text{"}
$$

$$
\Phi\in C^{0}(X,W^{+}\otimes E)
$$

$$
u\neq\mathrm{id}_E.
$$

$$
\mathit{If}u\in S_{Z}^{1}
$$

$$
u\neq\mathrm{id}_E
$$

$$
\Phi\equiv0
$$

Proof. Because u and $ \Phi $ are continuous, the equality $ u\Phi=\Phi $ holds at each point x $ \in X $ and so $ u|_{x}\in\mathfrak{gl}(E)|_{x} $ must be the identity on the image of $ \Phi $ in $ E|_{x}. $ If $ \Phi|_{x} $ is rank two, then $ u|_{x} $ must be the identity on $ E|_{x}, $ while if $ u|_{x}\neq\mathrm{id}_{E_{x}} $ , then $ \Phi|_{x} $ can be at most rank one. If $ u\in S_{Z}^{1}, $ then $ u\Phi=e^{i\theta}\Phi=\Phi $ and so $ \Phi=0. $ q.e.d.

$$
u\Phi=\Phi
$$

$$
x\in X
$$

$$
u|_{x}\in\mathfrak{g l}(E)|_{x}
$$

$$
E|_{x}
$$

$$
\Phi|_{x}
$$

$$
u|_{x}
$$

$$
E|_{x},
$$

$$
u|_{x}\neq\mathrm{id}_{E_{x}}
$$

$$
\Phi|_{x}
$$

$$
u\in S_{Z}^{1}
$$

$$
u\Phi=e^{i\theta}\Phi=\Phi
$$

$$
\Phi=0.\quad\textrm{q.e.d}
$$

Next we consider the stabilizers of reducible pairs. Recall from [44, Chapter II], [61, §III.3.3] that the stabilizer $ \mathrm{Stab}_{A}\subset^{\circ} \mathcal{G}_{E} $ may be identified with a subgroup of $ \operatorname{Aut}(E|_{x}) $ , for any point x $ \in X $ , by parallel translation with respect to the connection A and hence identified with a subgroup of U(2) by choosing an orthonormal frame for $ E|_{x} $ ; these subgroups are again denoted by $ \mathrm{Stab}_{A}. $ If $ E=L_{1}\oplus L_{2} $ , let $ S_{L_{1}}^{1} $ denote the group of gauge transformations given by $ e^{i\theta}\mathrm{id}_{L_{1}}\oplus\mathrm{id}_{L_{2}}. $

$$
\mathrm{Stab}_{A}\subset{}^{\circ}\mathcal{G}_{E}
$$

$$
\mathrm{Aut}(E|_x)
$$

$$
x\in X
$$

$$
\mathrm{U}(2)
$$

$$
E|_{x};
$$

$$
A
$$

$$
E=L_{1}\oplus L_{2}
$$

$$
S_{L_{1}}^{1}
$$

$$
e^{i\theta}\mathrm{id}_{L_1}\oplus\mathrm{id}_{L_2}
$$

Lemma 5.22. Let $ ( A, \Phi) $ be a PU(2) monopole in $ C^{r} $ on $ ( E, W^{+}\otimes E). $ Let U $ \subset X $ be a connected open set, with $ U\cap B(x_{j},R_{0}) $ empty or $ B(x_{j},2R_{0})\subset U $ for all balls $ B(x_{j},R_{0}) $ such that $ \beta_{j}[A]>0. $ If $ \Phi\neq0 $ and $ A|_{U} $ is reducible, then $ A|_{U} $ is reducible with respect to a splitting $ E|_{U}=L_{1}\oplus L_{2} $ where $ \Phi $ is rank one on U,with image contained either in $ L_{1} $ or in $ L_{2}. $ In the first case, $ \mathrm{Stab}_{(A,\Phi)|_U}=S_{L_{2}}^{1}, $ while in the second case, $ \mathrm{Stab}_{(A,\Phi)|_U}=S_{L_{1}}^{1}. $

$$
(E,W^{+}\otimes E)
$$

$$
C^{r}
$$

$$
U\subset X
$$

$$
U\cap B(x_{j},R_{0})
$$

$$
B(x_{j},2R_{0})\subset U
$$

$$
B(x_{j},R_{0})
$$

$$
\text{"}\Phi\not\equiv0
$$

$$
\beta_{j}[A]>0
$$

$$
A|_{U}
$$

$$
A|_{U}
$$

$$
E|_{\underline{U}}=L_{1}\oplus L_{2}
$$

$$
U.
$$

$$
L_{1}
$$

$$
\mathrm{Stab}_{(A,\Phi)|_U}=S^1_{L_2}
$$

$$
L_{2}
$$

$$
\mathrm{Stab}_{(A,\Phi)|_U}=S^1_{L_1}
$$

Proof. Because $ A |_{U} $ is reducible, all the holonomy sections $ \mathfrak{m}_{j,l,\alpha}(A) $ vanish on U if $ B(x_{j},2R_{0})\subset U $ . If $ B(x_{j},R_{0})\cap U $ is empty, the holonomy

$$
A|_{U}
$$

$$
\mathfrak{m}_{j,l,\alpha}(A)
$$

$$
B(x_{j},2R_{0})\subset U
$$

$$
B(x_{j},R_{0})\cap U
$$ sections also vanish on $U$, as they are supported on $B(x_j, R_0)$. Since $\Phi \neq 0$, we have $(F_A^+)_0 \neq 0$ on $U$ by Lemma 2.19 and the equation $(F_A^+)_0 = (\mathrm{id} + \tau_0)\rho^{-1}(\Phi \otimes \Phi^*)_{00}$ of (2.27), so $A|_U$ is not projectively flat. Therefore, $\text{Stab}_{A|_U} \simeq T^2$ and $A|_U$ is reducible with respect to a splitting $E|_U = L_1 \oplus L_2$ by Lemma 2.6.

Because the connection $A|_U$ is reducible with respect to the splitting $E|_U = L_1 \oplus L_2$, we can write $A|_U = A_1 \oplus A_2$, where $A_1, A_2$ are unitary connections on $L_1, L_2$, so $F_A|_U = F_{A_1} \oplus F_{A_2}$ and

$(F_A^+)_0 = \begin{pmatrix}
\frac{1}{2}(F_{A_1}^+ - F_{A_2}^+) & 0 \\
0 & -\frac{1}{2}(F_{A_1}^+ - F_{A_2}^+)
\end{pmatrix} = \varpi \otimes \sigma_1,$

where $\varpi = -\frac{i}{2}(F_{A_1}^+ - F_{A_2}^+) \in \Omega^+(U, \mathbb{R})$ and $\sigma_1 \in \mathfrak{su}(2)$ is one of the Pauli matrices (2.14). Hence, $(F_A^+)_0$ is rank one on $U$, and the equation $(F_A^+)_0 = (\mathrm{id} + \tau_0)\rho^{-1}(\Phi \otimes \Phi^*)_{00}$ implies that $(\Phi \otimes \Phi^*)_{00}$ is rank one on $U$. Lemma 2.21 then implies that $\Phi$ is also rank one on $U$ and so $F|_U = \phi \otimes \xi$ for some $\phi \in C^r \Omega^0(U, W^+)$ and $\xi \in C^r \Omega^0(U, E)$, and

$$
(\Phi \otimes \Phi^*)_{00} = -i(\phi \otimes \phi^*)_0 \otimes i(\xi \otimes \xi^*)_0.
$$

Writing $\xi = \xi_1 + \xi_2$ for $\xi_j \in C^r \Omega^0(U, L_j)$, we see that

$(\xi \otimes \xi^*)_0 = \begin{pmatrix}
\frac{1}{2}(|\xi_1|^2 - |\xi_2|^2) & \xi_1 \otimes \xi_2^* \\
\xi_2 \otimes \xi_1^* & -\frac{1}{2}(|\xi_1|^2 - |\xi_2|^2)
\end{pmatrix}.$

Since $(\mathrm{id} + \tau_0)\rho^{-1}(\Phi \otimes \Phi^*)_{00} = -(\mathrm{id} + \tau_0)\rho^{-1}(i(\phi \otimes \phi^*)_0) \otimes i(\xi \otimes \xi^*)_0$, we have

$(\mathrm{id} + \tau_0)\rho^{-1}(\Phi \otimes \Phi^*)_{00} = -(\mathrm{id} + \tau_0)\rho^{-1}(i(\phi \otimes \phi^*)_0) \otimes \begin{pmatrix}
\frac{i}{2}(|\xi_1|^2 - |\xi_2|^2) & i(\xi_1 \otimes \xi_2^*) \\
i(\xi_2 \otimes \xi_1^*) & -\frac{i}{2}(|\xi_1|^2 - |\xi_2|^2)
\end{pmatrix},$

and by comparison with our matrix expression for $(F_A^+)_0$, we see that $\xi_1 \otimes \xi_2^* = 0$ on $U$ and thus at each point of $U$, either $\xi_1 = 0$ or $\xi_2 = 0$. Since $\nabla_A \xi = \nabla_{A_1}\xi_1 \oplus \nabla_{A_2}\xi_2$ and because the perturbations vanish on $U$, the equation $(D_A + \vec{\theta} \cdot \vec{\mathfrak{m}}(A))\Phi = 0$ reduces to $(D_{A_1} + \rho(\vartheta_0))(\phi \otimes \xi_1) = 0$ and $(D_{A_2} + \rho(\vartheta_0))(\phi \otimes \xi_2) = 0$. The unique continuation result for the perturbed Dirac operator, Lemma 5.12, implies that if $\phi \otimes \xi_1$ vanishes on an open subset of $U$, then $\phi \otimes \xi_1 \equiv 0$ on $U$, and similarly for $\phi \otimes \xi_2$. If $\xi_1$ is non-zero at a point and thus non-zero on an open neighborhood, $\xi_2$ vanishes on this open set and by unique continuation, $\xi_2 \equiv 0$ on all of the connected set U. Symmetrically, if $ \xi_{2} $ is non-zero at a point, then $ \xi_{1}\equiv0 $ on U . Thus, $ \Phi=\phi\otimes\xi_{1} $ or $ \Phi=\phi\otimes\xi_{2}. $

$$
\xi_{2}
$$

$$
\xi_{1}\equiv0
$$

$$
\Phi=\phi\otimes\xi_{1}
$$

$$
\Phi=\phi\otimes\xi_{2}
$$

The stabilizer of $ A |_{U} $ is $ S_{L_{1}}^{1}\times S_{L_{2}}^{1}. $ Map($ U,S_{L_{1}}^{1} $ ) while if $ \xi_{2}=0 $ , then $ \mathrm{Stab}_{\Phi|_{l}} $

If $ \xi_{1}=0 $ , then $ \mathrm{Stab}_{\Phi|U}= $ $ = \operatorname {M a p} ( U, S_{L_{2}}^{1}). $ q.e.d.

$$
A|_{U}
$$

$$
S_{L_{1}}^{1}\times S_{L_{2}}^{1}
$$

$$
\xi_{1}\;=\;0.
$$

$$
\mathrm{Stab}_{\Phi|_U}=
\mathrm{Map}(U,S^1_{L_1})
$$

$$
\xi_{2}=0
$$

$$
\mathrm{Stab}_{\Phi|_U}^z=\mathrm{Map}(U,S_{L_2}^1)
$$

We see that elements of the stabilizer of a pair cannot exhibit holonomy, in the sense of the following lemma.

Lemma 5.23. Suppose $ ( A, \Phi) $ is a PU(2) monopole with $ \Phi\neq0 $ and that $ U_{1}, U_{2} $ are connected open subsets of X . If there are gauge transformations $ u_{i}\in\circ^{\circ}\mathcal{G}_{E|U_{i}} $ , $ i=1,2 $ , such that $ u_{i}\in\operatorname{Stab}_{A|U_{i}} $ , $ u_{i}\in$ $ \operatorname{Stab}_{(A,\Phi)|_{U_{1}\cap U_{2}}} $ , $ u_{i}\neq\mathrm{id} $ , and there is a point $ x\in U_{1}\cap U_{2} $ such that $ u_{1}=u_{2} $ on $ E|_{x} $ , then $ u_{1}=u_{2} $ on $ E|_{U_{1}\cap U_{2}}. $

$$
U_{1},\;U_{2}
$$

$$
\Phi\not\equiv0
$$

$$
u_{i}\in{}^{\circ}\mathcal{G}_{E|U_{i}},i=1,2
$$

$$
u_{i}\in\mathrm{Stab}_{A|_{U_{i}}},\;u_{i}\in
$$

$$
\mathrm{Stab}_{(A,\Phi)|_{U_1\cap U_2}},u_i\neq\mathrm{id}
$$

$$
x\in U_{1}\cap U_{2}
$$

$$
u_{1}=u_{2}
$$

$$
u_{1}=u_{2}
$$

$$
E^{\dagger}_{x},
$$

$$
E|_{U_{1}\cap U_{2}}
$$

Proof. Let $ V \subset U_{1} \cap U_{2} $ be the dense open subset of points $ \{\Phi\neq 0\} \cap U_{1}\cap U_{2}. $ Because there is a gauge transformation $ u_{i}\in^{\circ}\mathcal{G}_{E|U_{i}} $ with $ u_{i}\Phi=\Phi $ over $ U_{i}, $ then $ \Phi|_{U_{1}\cap U_{2}} $ must be rank one by Lemma 5.21 and there is an orthogonal decomposition $ E|_{V}=\operatorname{Im}\Phi\oplus(\operatorname{Im}\Phi)^{\perp}. $ Since $ u_{i}\Phi=\Phi $ on V, both $ u_{i} $ respect this decomposition and must be the identity on $ \operatorname{Im}\Phi|_{V}. $ Thus, on V we can write

$$
V\subset U_{1}\cap U_{2}
$$

$$
\left\{\Phi\neq\right.
0\}\cap U_{1}\cap U_{2}
$$

$$
u_{i}\in{}^{\circ}\mathcal{G}_{E|U_{i}}
$$

$$
U_{i},
$$

$$
u_{i}\Phi=\Phi
$$

$$
\Phi|_{U_1\cap U_2}
$$

$$
E|_{V}=\mathrm{Im}\Phi\oplus(\mathrm{Im}\Phi)^{\perp}
$$

$$
u_{i}\Phi=\Phi
$$

$$
u_{i}
$$

$$
u_{i}=\begin{pmatrix}1&0\\ 0&e^{i\theta_{i}}\end{pmatrix}
$$

with respect to this decomposition. Now det $ u_{i}=e^{i\theta_{i}} $ and because $ u_{i}\in^{\circ}\mathcal{G}_{E|U_{i}} $ , the function det $ u_{i} $ is constant on $ U_{i} $ and $ e^{i\theta_{i}}\in S^{1}. $ Hence, if $ u_{1}=u_{2} $ on $ E|_{x}, $ then $ u_{1}=u_{2} $ on all points in V which can be connected to x by a path in $ U_{1} $ and a path in $ U_{2} $ (note that these need not be the same paths). Because $ U_{1} $ and $ U_{2} $ are connected, $ u_{1}=u_{2} $ over all of V . But V is dense in $ U_{1}\cap U_{2} $ and the $ u_{i} $ are continuous, so $ u_{1}=u_{2} $ over all of $ U_{1}\cap U_{2}. $ q.e.d.

$$
u_{i}=e^{i\theta_{i}}
$$

$$
u_{i}\in{}^{\circ}\mathcal{G}_{E|U_{i}}
$$

$$
u_{i}
$$

$$
U_{i}
$$

$$
e^{i\theta_i}\in S^1
$$

$$
u_{1}\;=\;u_{2}
$$

$$
\overline{E}|_{x},
$$

$$
u_{1}\;=\;u_{2}
$$

$$
U_{1}
$$

$$
U_{2}
$$

$$
U_{1}
$$

$$
U_{2}
$$

$$
u_{1}=u_{2}
$$

$$
U_{1}\cap U_{2}
$$

$$
u_{1}=u_{2}
$$

$$
U_{1}\cap U_{2}
$$

$$
u_{i}
$$

## Theorem 5.11 now follows from Proposition 5.19:

Proof of Theorem 5.11, given Proposition 5.19. Let $ ( A,\Phi) $ be a $ C^{r} $ solution to the PU(2) monopole equations (2.27) with $ \Phi\neq0 $ and A reducible on a non-empty open set $ U\subset X $ . Let $ J(A)=\{j:1\leq j\leq N_{G} $ and $ \beta_{j}[A]>0 $ } and let $ \bar{B}_{J}(A)=\cup_{j\in J(A)}\bar{B}(x_{j},R_{0}) $ . Let $ U^{\circ} $ be a connected component of $ U-\bar{B}_{J}(A) $ . Lemma 5.22 then implies that $ \operatorname{Stab}_{(A,\Phi)|_{U^{\circ}}}\simeq S^{1}\neq S_{Z}^{1} $ , and so there is a $ C^{r+1} $ gauge transformation u of $ E|_{U^{\circ}} $ such that $ u(A,\Phi)=(A,\Phi) $ on $ U^{\circ}. $ Proposition 5.19 allows the extension of u to open subsets of $ X\backslash\bar{B}_{J}(A) $ containing $ U^{\circ}. $ To be explicit, let x $ \in U^{\circ} $ and $ r_{0}=\mathrm{dist}_{g}(x,\partial U^{\circ}) $ and choose $ r_{1}>r_{0} $ such

$$
C^{r}
$$

$$
\Phi\not\equiv\bar{0}
$$

$$
U\subset X
$$

$$
J(A)=\{j:1\leq
$$

$$
j\leq N_{G}
$$

$$
\bar{B}_{J}(A)=\cup_{j\in J(A)}\bar{B}(x_{j},R_{0})
$$

$$
U^{\circ}
$$

$$
U-\bar{B}_{J}(A)
$$

$$
\mathrm{Stab}_{(A,\Phi)|_{U^{\circ}}}\simeq S^{1}\neq S^{1}_{Z}
$$

$$
C^{r+1}
$$

$$
\overline{E}|_{U^{\circ}}
$$

$$
u(A,\Phi)=(A,\Phi)
$$

$$
U^{\circ}
$$

$$
X\backslash\bar{B}_J(A)
$$

$$
U^{\circ}
$$

$$
x\in U^{\circ}
$$

$$
r_{0}=\mathrm{dist}_{g}(x,\partial U^{\circ})
$$

$$
r_{1}>r_{0}
$$ that $ r_{1}\leq \frac{1}{2}\varrho $ and $ r_{1}\leq \min_{j\in J(A)} \mathrm{dist}_{g}(x,B(x_{j},R_{0})) $ . By Proposition 5.19 there is an extension of u $ \in \operatorname{Stab}_{(A,\Phi)|_{B(x,r_{0})}} $ to an element $ \hat{u}\in \operatorname{Stab}_{(A,\Phi)|_{B(x,r_{1})}} $ . By Lemma 5.23 we have $ \hat{u}=u $ on $ U^{\circ}\cap B(x_{0},r_{1}) $ and not just $ B(x_{0},r_{0}) $ . This gives an extension of the stabilizer u for (A, $ \Phi $ ) over $ U^{\circ} $ to a stabilizer $ \hat{u} $ over the slightly larger open set $ U^{\circ}\cup B(x,r_{1}) $ Since we do not assume that X is simply connected, we must check that the extension obtained by repeating this process yields a single-valued gauge transformation over $ X-\bar{B}_{J}(A) $

$$
r_{1}\leq\frac{1}{2}\varrho
$$

$$
r_{1}\leq\min_{j\in J(A)}\mathrm{dist}_{g}(x,B(x_{j},R_{0}))
$$

$$
u\in\mathrm{Stab}_{(A,\Phi)|_{B(x,r_0)}}
$$

$$
\hat{u}\in
$$

$$
\hat{u}=u
$$

$$
\mathrm{Stab}_{(A,\Phi)|_{B(x,r_1)}}
$$

$$
U^{\circ}\cap B(x_{0},r_{1})
$$

$$
B(x_{0},r_{0})
$$

$$
U^{\circ}
$$

$$
\hat{u}
$$

$$
(A,\Phi)
$$

$$
U^{\circ}\cup B(x,r_1)
$$

$$
X-\bar{B}_{J}(A)
$$

The consistency of two extensions follows from Lemma 5.23. Let $ u_{i}, i=1,2 $ , be two extensions of u to connected open sets $ U_{i}^{\circ} $ containing $ U^{\circ} $ so we have $ u_{i}\in \mathrm{Stab}_{(A,\Phi)|_{U_{i}^{\circ}}} $ with $ u_{i}=u $ on $ E|_{U^{\circ}} $ . Because $ u_{1}=u=u_{2} $ on $ E|_{U^{\circ}} $ , Lemma 5.23 implies that $ u_{1}=u_{2} $ on $ E|_{U_{1}^{\circ}\cap U_{2}^{\circ}} $ . Therefore, the extensions of $ u\in \mathrm{Stab}_{(A,\Phi)|_{U^{\circ}}} $ fit together to form a global gauge transformation $ \hat{u}\in \mathrm{Stab}_{A,\Phi} $ on $ X-\bar{B}_{J}(A) $ such that $ \hat{u}=u $ on $ E|_{U^{\circ}} $ .

$$
u_{i},
$$

$$
i=1,2
$$

$$
U_{i}^{\circ}
$$

$$
U^{\circ}
$$

$$
u_{i}\in\mathrm{Stab}_{(A,\Phi)|_{U_{i}^{\circ}}}
$$

$$
u_{i}=u
$$

$$
E|_{U^{\circ}}
$$

$$
u_{1}=u=u_{2}
$$

$$
u_{1}\;=\;u_{2}
$$

$$
E|_{U^{\circ}}
$$

$$
E|_{U_{1}^{\circ}\cap U_{2}^{\circ}}
$$

$$
u\in\mathrm{Stab}_{(A,\Phi)|_U\circ}
$$

$$
\hat{u}\in\mathrm{Stab}_{A,\Phi}
$$

$$
\widetilde{X}-\bar{B}_J(A)
$$

$$
E|_{U^{\circ}}
$$

$$
\hat{u}=u
$$

Thus, given that A is reducible on an open set U containing $ \bar{B}_{J}(A) $ the above argument produces an element u $ \in $ Stab $ _{(A,\Phi)|_{X-\bar{B}_{J}(A)}} $ with $ u\notin S_{Z}^{1}. $ Consequently, A is reducible on $ X-\bar{B}_{J}(A) $ by Lemma 2.6. For j=1,...,Nb, let Vj be an open, connected subset of U $ \cap B(x_{j},2R_{0}) $ containing $ \bar{B} ( x_{j}, R_{0} ) $ , such that $ V_{j}\cap( X-B_{J}(A)) $ is connected, and set

$$
\bar{B}_{J}(A)
$$

$$
u\in\mathrm{Stab}_{(A,\Phi)|_{X-\bar{B}_J(A)}}
$$

$$
u\notin S_{Z}^{1}
$$

$$
X-\bar{B}_J(A)
$$

$$
j=1,\ldots,N_b
$$

$$
V_{j}
$$

$$
U\cap B(x_{j},2R_{0})
$$

$$
\bar{B}(x_{j},R_{0})
$$

$$
V_{j}\cap\left(X-B_{J}(A)\right)
$$

$$
\begin{aligned}&X_{1}=X-\bar{B}_{J}(A),\quad\\ &X_{j}=(X-\bar{B}_{J}(A))\cup\bigcup_{1\leq k\leq j-1}V_{k},\quad2\leq j\leq N_{b}+1.\\ \end{aligned}
$$

Each subset $ X_{j} $ and $ V_{j}\cap X_{j} $ is commutative $ X_{N_{b}+1}=X. $ We extend u $ \in $ Stab <sub>(A)</sub> of $ X_{j}. $ Plainly, we have u $ \in $ Stab $ _{A|V_{j}\cap X_{j}} $ a first check that $ \mathrm{Stab}_{A|V_{j}}=\mathrm{Stab}_{A|V_{j}\cap X_{j}} $ and so for each subset $ V_{j}\subset U $ , we have $ \Phi |_{V_{j}\cap X_{j}}\neq0 $ and thus $ F_{A}\neq0 $ on $ V_{j} $ is not flat then Lemma 2.6 implies argument yields $ \mathrm{Stab}_{A|V_{j}}\simeq T^{2}. $ connectedness of $ V_{j} $ and $ V_{j}\cap X_{j} $ here the stabilizers would be $ \oplus T^{2}, $ a direct s Thus, $ \mathrm{Stab}_{A|V_{j}}=\mathrm{Stab}_{A|V_{j}\cap X_{j}}\simeq T^{2}. $

ected, and $ X_{1}\subset X_{2}\subset \cdots \subset |_{X-\bar{B}_{J}(A)}$ inductively over each and $ \mathrm{Stab}_{A|V_{j}}\subset\mathrm{Stab}_{A|V_{j}\cap X_{j}} $ , so we By hypothesis, $ A|_{U} $ is reducible that $ A|_{V_{j}} $ is reducible. Because $ \cap X_{j} $ by (2.27) — so $ A|_{V_{j}\cap X_{j}} $ is that $ \mathrm{Stab}_{A|V_{j}\cap X_{j}}\simeq T^{2}. $ The We use the assumptions on the if the sets were not connected, sum over connected components.)

$$
X_{j}
$$

$$
V_{j}\cap X_{j}
$$

$$
X_{1}\subset X_{2}\subset\cdots\subset
$$

$$
X_{N_b+1}=X
$$

$$
u\;\in\;\mathrm{Stab}_{(A,\Phi)|_{X-\bar{B}_J(A)}}
$$

$$
X_{j}
$$

$$
u\in\mathrm{Stab}_{A|_{V_j\cap X_j}}
$$

$$
\mathrm{Stab}_{A|_{V_j}}\subset\mathrm{Stab}_{A|_{V_j\cap X_j}}
$$

$$
\mathrm{Stab}_{A|_{V_j}}=\mathrm{Stab}_{A|_{V_j\cap X_j}}^*
$$

$$
A|_{U}
$$

$$
\tilde{V}_{j}\subset U
$$

$$
A|_{V_{j}}
$$

$$
\Phi|_{V_{j}\cap X_{j}}\not\equiv0
$$

$$
F_{A}\not\equiv0
$$

$$
V_{j}\cap X_{j}
$$

$$
(2. 2 7) - \mathrm {s o} A | _ {V _ {j} \cap X _ {j}}
$$

$$
\mathrm{Stab}_{A|_{V_j\cap X_j}}\;\simeq\;T^2
$$

$$
\mathrm{Stab}_{A|_{V_i}}\simeq T^2
$$

$$
V_{j}\cap X_{j}
$$

$$
V_{j}
$$

$$
\oplus T^{2}
$$

$$
\mathrm{Stab}_{A|_{V_j}}=\mathrm{Stab}_{A|_{V_j\cap X_j}}\simeq T^2
$$

Hence, there is an element $ u^{\prime\prime}\in \mathrm{Stab}_{A|_{V_j}} $ such that $ u^{\prime\prime}=u^{\prime} $ on $ V_{j}\cap X_{j}, $ where $ u^{\prime}\in \mathrm{Stab}_{(A,\Phi)|_{X_{j}}} $ with $ u^{\prime}\neq $ id. Together, $ u^{\prime} $ and $ u^{\prime\prime} $ give an element $ u\in \mathrm{Stab}_{A|_{X_{j+1}}} $ which is not in $ S_{Z}^{1}. $ The connection A is then

$$
u''\in\mathrm{Stab}_{A|_{V_j}}
$$

$$
u^{\prime\prime}=u^{\prime}
$$

$$
V_{j}\cap X_{j}
$$

$$
u^{\prime}\in\mathrm{Stab}_{(A,\Phi)|_{X_{j}}}
$$

$$
u^{\prime}\neq\mathrm{id}
$$

$$
u^{\prime\prime}
$$

$$
u\in\mathrm{Stab}_{A|_{X_{j+1}}}
$$

$$
S_{Z}^{1}
$$ reducible on $X_{j+1}$, which implies that all the holonomy perturbations vanish on $X_{j+1}$. Lemma 5.22 therefore shows that the pair $(A, \Phi)$ is reducible on $X_{j+1}$ and we obtain a stabilizer $u \in \text{Stab}_{(A, \Phi)|X_{j+1}}$, with $u \neq \text{id}$. The construction of $u \in \text{Stab}_{A, \Phi}$, $u \neq \text{id}$, is thus completed by induction on $j$. q.e.d.

Remark 5.24. The analogue of Theorem 5.11 (namely, that local reducibility implies global reducibility) does not hold for anti-self-dual connections without further restrictions on the topology of $X$. For example, in [30] it is assumed that the four-manifold $X$ is simply connected (see Lemma 4.3.21). As described by Kronheimer and Mrowka in [47] one can have locally reducible anti-self-dual connections (called ‘twisted reducibles’ in [47]); see their Lemma 2.4 for a sharp version of the Freed-Uhlenbeck generic metrics theorem (Corollaries 4.3.15, 4.3.18, and 4.3.19 in [20]) which holds when the requirement that $X$ be simply connected is dropped. In our case, we see from the proof of Theorem 5.11 that globally irreducible, locally reducible solutions $(A, \Phi)$ to (2.27) do not exist (at least when $\Phi \neq 0$) because the stabilizer $u \in \text{Stab}_{A, \Phi}$ must stabilize the section $\Phi$ and not just the connection $A$.

The proof of Proposition 5.19 takes up the remainder of this section.

5.3.1. The Agmon-Nirenberg unique continuation theorem. As in the case of the anti-self-dual equation [20, Lemma 4.3.21], our proof of the unique continuation property for PU(2) monopoles in radial gauge relies on the following special case of a more general result due to Agmon and Nirenberg for an ordinary differential equation on a Hilbert space [4]:

Theorem 5.25 [4, Theorem 2 (ii)]. Let $\mathfrak{H}$ be a Hilbert space and let $\mathcal{P} : \text{Dom}(\mathcal{P}(r)) \subset \mathfrak{H} \rightarrow \mathfrak{H}$ be a family of symmetric linear operators for $r \in [r_0, R)$. Suppose that $\eta \in C^1([r_0, R), \mathfrak{H})$, with $\eta(r) \in \text{Dom}(\mathcal{P}(r))$ and $\mathcal{P}\eta \in C^0([r_0, R), \mathfrak{H})$ such that

$$\left\| \frac{d\eta}{dr} - \mathcal{P}(r)\eta(r) \right\| \leq c_1 \|\eta(r)\|,$$

for some positive constant $c_1$ and all $r \in [r_0, R)$. If the function $r \mapsto (\eta(r), \mathcal{P}(r)\eta(r))$ is differentiable for $r \in [r_0, R)$ and satisfies

$$\frac{d}{dr} (\eta, \mathcal{P}\eta) - 2 \text{Re} \left( \frac{d\eta}{dr}, \mathcal{P}\eta \right) \geq -c_2 \|\mathcal{P}\eta\| \|\eta\| - c_3 \|\eta\|^2,$$

for positive constants $c_2, c_3$ and every $r \in [r_0, R)$, then the following holds: If $\eta(r_0) = 0$, then $\eta(r) = 0$ for all $r \in [r_0, R)$.

---

Applications of [4, Theorem 2] to the proof of unique continuation results for first-order elliptic and parabolic partial differential equations were considered by Agmon in [3, Chapter II]. In our application, $P(r)$ will be a family of first-order partial differential operators which are self-adjoint over the closed manifold $X$. Theorem 5.25 has also been applied by D. Salamon to prove the unique continuation property for harmonic spinors [77, Appendix E]. One of the difficulties in applying the Agmon-Nirenberg theorem to the PU(2) monopole equations (in Gaussian polar coordinates, $(r,\theta)$) is the requirement that the one-parameter family of operators be self-adjoint with respect to a fixed inner product on a fixed vector space. The additional complication, not present in [20, §4.3.4], is that the induced spin$^c$ structures on geodesic spheres in $X$ vary with the induced family of $r$-dependent metrics.

Remark 5.26 [4, Remark, p. 209]. If Dom($P(r)) = D$ is independent of $r$, and $P(r), r \in [r_0,R)$, is a differentiable family of self-adjoint operators, then the left-hand side of (5.11) simplifies, of course, to give the condition

$$\left(\eta, \frac{dP}{dr}\eta\right) \geq -c_2 \|P\eta\|\|\eta\| - c_3\|\eta\|^2,$$

since, noting that $P$ is self-adjoint,

$$\frac{d}{dr} (\eta,P\eta) - 2 \text{Re} \left(\frac{d\eta}{dr}, P\eta\right) = \left(\frac{d\eta}{dr}, P\eta\right) + \left(\eta, \frac{dP}{dr}\eta\right) + \left(\eta, P\frac{d\eta}{dr}\right)$$

$$- \left(\frac{d\eta}{dr}, P\eta\right) - \left(P\eta, \frac{d\eta}{dr}\right)$$

$$= \left(\eta, \frac{dP}{dr}\eta\right).$$

If $P(r), r \in [r_0,R)$, is a differentiable family of self-adjoint operators, then it is easy to see that (5.12) follows from the simpler condition

$$\left\| \frac{dP}{dr}\eta \right\| \leq c_2 \|P\eta\| + c_3\|\eta\|,$$

provided $P\eta \in C^0([r_0,R), \mathfrak{H})$.

5.3.2. The PU(2) monopole equations in Gaussian polar coordinates. Our first task is to write the pair of PU(2) monopole equations (2.27) as an ordinary differential equation with respect to

---

Gaussian polar coordinates $(r, \theta)$ centered at a point $x_0 \in X$. For the analogous ordinary differential equation in the case of the anti-self-dual equation, see [20], [63], [88], and for the Seiberg-Witten equations; see [47], [77].

Recall that $\varrho$ is the injectivity radius of $(X,g)$ at the point $x_0$, so $\exp_{x_0} : B(0,\varrho) \subset (TX)_{x_0} \rightarrow B(x_0,\varrho) \subset X$ is a diffeomorphism. For each $\xi$ in the unit sphere $S^3 \subset (TX)_{x_0}$, let $\{e_i(\xi)\}_{i=1}^3$ be an oriented, orthonormal basis for $(\mathbb{R}\xi)^\perp = (TS^3)_\xi \subset (TX)_{x_0}$; that is, let $\{e_i\}$ be an orthonormal frame for $TS^3$. Let $\gamma_\xi(r)$ be the geodesic $\exp_{x_0}(r\xi)$, $r \in [0,\varrho)$, so that $\gamma_\xi(0) = x_0$ and $|\gamma_\xi'(r)| = |\xi|$, and let $\tau_\xi(r) : (TX)_{x_0} \rightarrow (TX)_{\gamma_\xi(r)}$ denote parallel translation with respect to the metric’s Levi-Civita connection along $\gamma_\xi(r)$. Let $e_i(r,\xi) := \tau_\xi(r)e_i(\xi)$ for $r \geq 0$, so that $\{\gamma_\xi'(r), e_i(r,\xi)\}$ is an orthonormal frame for $(TX)_{\gamma_\xi(r)}$ which is parallel along the radial geodesics $\gamma_\xi(r)$ and satisfies $\gamma_\xi'(0) = \xi$ and $e_i(0,\xi) = e_i(\xi)$. Denote the radial vector $\gamma_\xi'(r) \in (TX)_{\gamma_\xi(r)}$ by $\frac{\partial}{\partial r} := \frac{\partial}{\partial r}|_{\gamma_\xi(r)}$ when no confusion can arise. Thus, $\{\frac{\partial}{\partial r}, e_i\}$ is an oriented, orthonormal frame for $TX$ over $B(x_0,\varrho) \setminus \{0\}$, which is parallel along radial geodesics; let $\{dr,e_i\}$ be the corresponding dual frame for $T^*X$ over $B(x_0,\varrho) \setminus \{0\}$.

With respect to the parametrization $S^3 \times (0,\varrho) \simeq B(x_0,\varrho) - \{x_0\}$, given by $(r,\xi) \mapsto \exp_{x_0}(r\xi)$, the metric $g$ on $B(x_0,\varrho) - \{x_0\}$ pulls back to

$$g = (dr)^2 + g_r,$$

where $g_r$ is the metric on $S^3$ pulled back from the restriction $g|_{S^3(x_0,r)}$ to the geodesic sphere $S^3(x_0,r) := \{x \in X : \text{dist}_g(x,x_0) = r\}$. Let $*g_r$ denote the Hodge star operator for the metric $g_r$ on $S^3$ and, for emphasis, we write $*g$ for the Hodge star operator for the metric $g$ on $X$.

Suppose that a pair $(A,\Phi)$ on $(\mathfrak{su}(E), W^+ \otimes E)$ is a $C^r$ solution to the PU(2) monopole equations (2.27) over $X$,

$$\rho(F_A^+) = \rho\tau\rho^{-1}(\Phi \otimes \Phi^*)_{00},$$

$$D_{A,\vartheta_0}\Phi = 0,$$

where $\tau := \text{id}_{\Lambda^+} + \tau_0$ is an automorphism of $\Lambda^+$ and

$$D_{A,\vartheta_0}\Phi := D_A\Phi + \rho(\vartheta_0)\Phi.$$

We have not included the holonomy perturbations $\vec{\tau} \cdot \vec{\mathfrak{m}}(A)$ and $\vec{\vartheta} \cdot \vec{\mathfrak{m}}(A)$ because they vanish near $x_0$ by hypothesis.

---

We obtain an isomorphism $E|_{B(x_0, \varrho)} \simeq E_0 \times B(x_0, \varrho)$ of complex two-plane bundles by choosing a unitary frame for $E_0 := E|_{x_0}$ and using parallel translation via the U(2) connection on $E$ defined by $A$ and $A_{\det E}$ along radial geodesics emanating from $x_0$. Let $A = B + Cdr$ denote the induced SO(3) connection on the bundle $\mathfrak{su}(E_0) \times S^3 \times (0, \varrho)$ over $S^3 \times (0, \varrho)$ and note that $A$ is in radial gauge with respect to the point $x_0$, so $C := A(\frac{\partial}{\partial r}) = 0$. We let $B = B(r), r \in (0, \varrho)$, denote the resulting one-parameter family of SO(3) connections on the bundle $\mathfrak{su}(E_0) \times S^3$ over $S^3$. In exactly the same way, we obtain an induced one-parameter family of U(2) connections on the bundle $W_0^+ \times S^3$ over $S^3$, $r \in (0, \varrho)$, induced by the isomorphism $W^+|_{B(x_0, \varrho)-\{x_0\}} \simeq W_0^+ \times S^3 \times (0, \varrho)$.

A section $\Phi$ of the bundle $W^+ \otimes E$ over $B(x_0, \varrho)$ pulls back, via the isomorphism $(W^+ \otimes E)|_{B(x_0, \varrho)-\{x_0\}} \simeq (W_0^+ \otimes E_0) \times S^3 \times (0, \varrho)$, to a one-parameter family of sections $\Psi(r)$ of the bundle $W_0^+ \otimes E_0 \times S^3$ over $S^3$. The automorphism $\tau$ of $\Lambda^{+,g}$ pulls back to a one-parameter family of automorphisms $\sigma(r)$ of $T^*S^3$, for $r \in (0, \varrho)$, using the isomorphism

$$
(0, \varrho) \times T^*S^3 \rightarrow \Lambda^{+,g}(T^*X), \quad (r, \alpha) \mapsto *g_r \alpha + dr \wedge \alpha.
$$

The $g$-compatible Clifford map $\rho : T^*X \rightarrow \text{Hom}(W^+, W^{-})$ and the isomorphism $W^+|_{B(x_0, \varrho)-\{x_0\}} \simeq W_0^+ \times S^3 \times (0, \varrho)$ define a family of $g_r$-compatible Clifford maps $\gamma(r) : T^*S^3 \rightarrow \text{End}(W_0^+)$ by setting

$$
\gamma(r) := \rho(dr)\rho(\cdot).
$$

Indeed, to see this, observe that $g(dr, dr) = 1$ and so for a family of one-forms $\alpha(r)$ on $S^3$, defined by the isomorphism

$$B(x_0, \varrho) - \{x_0\} \simeq S^3 \times (0, \varrho)$$

and a one-form $\alpha$ on $B(x_0, \varrho)$, we have

$$\gamma_r(\alpha)^\dagger \gamma_r(\alpha) = \rho(\alpha)^\dagger \rho(dr)^\dagger \rho(dr)\rho(\alpha) = \rho(\alpha)^\dagger \rho(\alpha)$$

as required. The map $\gamma$ extends to a one-parameter family of Clifford maps $\gamma(r) : \Lambda^{\bullet}(T^*S^3) \otimes \mathbb{C} \rightarrow \text{End}(W_0^+)$ in the usual way. For example, $\gamma_r(\alpha \wedge \beta) := \gamma_r(\alpha)\gamma_r(\beta)$, for $\alpha, \beta \in \Omega^1(S^3)$, in which case we see that $\gamma_r(\alpha \wedge \beta) = \rho(\alpha)\rho(\beta).$

With the above understood, we can proceed to rewrite the PU(2) monopole equations (2.27) over the ball $B(x_0, \varrho)$ as an ordinary differential equation for a one-parameter family of pairs $(B(r), \Psi(r))$ on

---

($\mathfrak{su}(E_0), W_0^+ \otimes E_0$) over $S^3$. The curvature $F_A$ of the connection $A$ over $B(x_0, \varrho)$ is given by

$$F_A = F_B - \frac{dB}{dr} \wedge dr.$$

For any $\omega \in \Omega^2(X, \mathbb{R})$, we have $\rho_+(\omega) = \rho_+(*g\omega)$, since $\rho_+|_{\Lambda^-} = 0$. If the radial component of $\omega$ vanishes and we consider $\omega|_{B(x_0, \varrho)}$ as a one-parameter family of two-forms $\omega(r)$ on $S^3$, then we see that $*g\omega = -(*g_r\omega) \wedge dr$. Combining these observations yields

$$\rho(F_A^+) = \rho_+(F_A) = \rho_+ \left(F_B - \frac{dB}{dr} \wedge dr\right)$$

$$= \rho_+ \left(-(*g_rF_B) \wedge dr - \frac{dB}{dr} \wedge dr\right)$$

$$= \rho_-(dr)\rho_+ \left(*g_rF_B + \frac{dB}{dr}\right),$$

and therefore,

$$\rho(F_A^+) = \gamma \left(*g_rF_B + \frac{dB}{dr}\right).$$

The section $\rho_T\rho^{-1}(\Phi \otimes \Phi^*)_{00}$ of $\mathfrak{su}(W^+) \otimes \mathfrak{su}(E)$ over $B(x_0, \varrho)$ pulls back to the one-parameter family of sections $\gamma\sigma\gamma^{-1}(\Psi \otimes \Psi^*)_{00}$ of

$$\mathfrak{su}(W_0^+) \otimes \mathfrak{su}(E_0) \times S^3$$

over $S^3$ via the isomorphism

$$W^+|_{B(x_0, \varrho)-\{x_0\}} \simeq W_0^+ \times S^3 \times (0, \varrho),$$

and similarly for $E$.

Let $\theta(r)$ be the induced one-parameter family of complex one-forms on $S^3$ defined by $\vartheta_0$ on $B(x_0, \varrho)$ and the isomorphism

$$B(x_0, \varrho) - \{x_0\} \simeq S^3 \times (0, \varrho),$$

so $\vartheta_0 = -fdr + \theta$ on $S^3 \times (0, \vartheta)$, where $f(r) \in \Omega^0(S^3, \mathbb{C})$. Given the preceding identifications, the Dirac operator term in (2.27) can then be written over $S^3 \times \{r\}$ as

$$D_{A,\vartheta_0} \Phi = \rho(dr) \nabla_{\frac{\partial}{\partial r}}^A \Psi + \sum_{i=1}^{3} \rho(e^i) \nabla_{e_i}^A \Psi + \rho(\vartheta_0) \Psi$$

$$= \rho(dr) \frac{d\Psi}{dr} + \sum_{i=1}^{3} \rho(e^i) \nabla_{e_i}^B \Psi + \rho(\theta) \Psi - f\rho(dr) \Psi$$

$$= \rho(dr) \left( \frac{d\Psi}{dr} - \sum_{i=1}^{3} \rho(dr) \rho(e^i) \nabla_{e_i}^B \Psi - \rho(dr) \rho(\theta) \Psi - f\Psi \right)$$

$$= \rho(dr) \left( \frac{d\Psi}{dr} - \sum_{i=1}^{3} \gamma(e^i) \nabla_{e_i}^B \Psi - \gamma(\theta) \Psi - f\Psi \right),$$

and therefore,

$$D_{A,\vartheta_0} \Phi = \rho(dr) \left( \frac{d\Psi}{dr} - D_{B,\theta,f} \Psi \right).$$

Hence, the PU(2) monopole equations (2.27) can be written as

$$\gamma \left( \frac{dB}{dr} + *_{g_r} F_B \right) = \gamma \sigma \gamma^{-1}(\Psi \otimes \Psi^*)_{00},$$

$$\rho(dr) \frac{d\Psi}{dr} = \rho(dr) D_{B,\theta,f} \Psi.$$

We use $D_B : \Omega^0(S^3, W_0^+ \otimes E_0) \to \Omega^0(S^3, W_0^+ \otimes E_0)$ to denote the one-parameter family of Dirac operators defined by the family of $g(r)$-compatible Clifford maps $\gamma(r) : T^* S^3 \to \text{End } W_0^+,$ the family of U(2) connections on $W_0^+ \times S^3$, the family of SO(3) connections $B(r)$ on $\mathfrak{su}(E_0) \times S^3$ over $S^3$, and the family of determinant connections on $\det E_0 \times S^3$ over $S^3$. Since the Clifford map gives an isomorphism $\gamma : T^* S^3 \simeq \mathfrak{su}(W_0^+) \times S^3$, the PU(2) monopole equations then take the shape

$$\frac{dB}{dr} + *_{g_r} F_B = \sigma \gamma^{-1}(\Psi \otimes \Psi)_{00},$$

$$\frac{d\Psi}{dr} = D_{B,\theta,f} \Psi,$$

for a one-parameter family $(B(r), \Psi(r))$, $r \in (0, \varrho)$, on $(E_0, W_0^+ \otimes E_0)$ over $S^3$.

---

5.3.3. The ordinary differential equation for the difference pair. Let $(A, \Phi)$ be a $C^r$ solution to the PU(2) monopole equations (2.27) over $X$. Suppose, as in the hypothesis of Proposition 5.19, that there is a $C^{r+1}$ gauge transformation $u$ of $E|_{B(x_0,r_0)}$ such that $u(A, \Phi) = (A, \Phi)$ on $B(x_0,r_0)$. Let $(A, \Phi)$ again denote the induced pair defined by the isomorphism $E|_{B(x_0,\varrho)} \simeq E_0 \times S^3 \times (0,\varrho)$ (given by a choice of unitary frame for $E_0 = E_x_0$ and parallel, radial translation via $A$) and let $u$ be the induced gauge transformation on $E_0 \times S^3 \times (0,r_0)$. Then $u(A) = uAu^{-1} - (d_A u)u^{-1}$ and $A = B + C dr$, where $C = A(\frac{\partial}{\partial r}) = 0$, and so $du/dr = 0$. We now extend $u$ by parallel translation via $A$ along radial geodesics emanating from $x_0$ to a gauge transformation $\hat{u}$ on $E_0 \times S^3 \times (0,\varrho)$.

Let $(\hat{A}, \hat{\Phi}) = \hat{u}(A, \Phi)$ be the gauge-equivalent pair on $S^3 \times (0,\varrho)$, so $(\hat{A}, \hat{\Phi})$ is a $C^r$ solution to (2.27) over $S^3 \times (0,\varrho)$, with $\hat{A} = \hat{u}(A)$ in radial gauge. In particular, $(\hat{A}, \hat{\Phi}) = (A, \Phi)$ over $S^3 \times (0,r_0)$: we need to show that $(\hat{A}, \hat{\Phi}) = (A, \Phi)$ over $S^3 \times (0,r_1)$ in order to prove Proposition 5.19.

The one-parameter family of pairs $(\hat{B}(r), \hat{\Psi}(r))$ on $(\mathfrak{su}(E_0), W_0^+ \otimes E_0)$ over $S^3$ also satisfies the ordinary differential equation in (5.14) so, subtracting these two pairs of ordinary differential equations, we obtain for $r \geq r_0$,

$$\frac{d(\hat{B}-B)}{dr} + *_{gr}(F_{\hat{B}}-F_B) = \sigma\gamma^{-1}(\hat{\Psi} \otimes \hat{\Psi}^* - \Psi \otimes \Psi^*)_{00},$$

$$\frac{d(\hat{\Psi}-\Psi)}{dr} = D_{B,\theta,f}\Psi - D_{\hat{B},\theta,f}\hat{\Psi}.$$

Since

$$F_B = d(B-\Gamma) + (B-\Gamma)\wedge(B-\Gamma)$$

and

$$D_{B,\theta,f} = D + \gamma(B-\Gamma) + \gamma(\theta) + f\mathrm{id}_{W_0^+ \otimes E_0},$$

we obtain an ordinary differential equation for the difference pair

$$
(b,\psi) := (\hat{B}-B, \hat{\Psi}-\Psi) \in \Omega^1(S^3, \mathfrak{su}(E_0)) \oplus \Omega^0(S^3, W_0^+ \otimes E_0),
$$

so that,

$$\frac{db}{dr} = -*_{gr} db + *_{gr}(\hat{B} \wedge b + b \wedge B)$$

$$+\sigma\gamma^{-1}(\hat{\Psi} \otimes \psi^* + \psi \otimes \psi^*)_{00},$$

$$\frac{d\psi}{dr} = D\psi + \gamma(\hat{B}-\Gamma)\psi + \gamma(b)\Psi + \gamma(\theta)\psi + f\psi,$$ where $r \in (r_0, \varrho)$, and $\Gamma$ is the product connection on $\mathfrak{su}(E_0) \times S^3$ over $S^3$ defined by our trivialization. The above system has the schematic form

$$\frac{d(b, \psi)}{dr} = \begin{pmatrix} -*_{g_r} & d & 0 \\ 0 & D \end{pmatrix} (b, \psi) + \mathcal{Z}_r(b, \psi),$$

where $\mathcal{Z}_r$ is a one-parameter family of zeroth-order operators with coefficients depending on $g_r$, $B$, $\sigma$, and $\Psi$.

5.3.4. Reduction to the Agmon-Nirenberg theorem. We first observe that the operator $-*_{g_r} d$ on $\Omega^1(S^3, \mathfrak{su}(E_0))$ is self-adjoint with respect to the $L^2$ inner product induced by the metric $g_r$ on $S^3$. Indeed, as $*_{g_r}^2 = 1$ on $\Omega^1(S^3)$ and $d \operatorname{tr}(b \wedge b') = \operatorname{tr}(db \wedge b') - \operatorname{tr}(b \wedge db')$, we have

$$\int_{S^3} \langle b, -*_{g_r} db' \rangle_r d \operatorname{vol}_r = -\int_{S^3} \operatorname{tr}(b \wedge *_{g_r} (-*_{g_r} db'))$$

$$= \int_{S^3} \operatorname{tr}(b \wedge db') = \int_{S^3} \operatorname{tr}(db \wedge b')$$

$$= \int_{S^3} \operatorname{tr}(b \wedge db') = \int_{S^3} \operatorname{tr}(b' \wedge *_{g_r}^2 db)$$

$$= -\int_{S^3} \langle b', *_{g_r} db \rangle_r d \operatorname{vol}_r,

and therefore,

$$\int_{S^3} \langle b, -*_{g_r} db' \rangle_r d \operatorname{vol}_r = \int_{S^3} \langle -*_{g_r} db, b' \rangle_r d \operatorname{vol}_r.$$

The Dirac operators $D : \Omega^1(S^3, W_0^+ \otimes E_0) \to \Omega^1(S^3, W_0^- \otimes E_0)$ are defined by the one-parameter family of $g_r$-compatible Clifford maps $\gamma_r : T^*S^3 \rightarrow \operatorname{End}(W_0^+)$, the one-parameter family of U(2) connections on $W_0^+ \times S^3$, the one-parameter family of determinant connections on $\det E_0 \times S^3$, and the product SO(3) connection on $\mathfrak{su}(E_0) \times S^3$. Then, by [57, Proposition II.5.3] we have

$$\langle D\psi, \psi' \rangle = \langle \psi, D\psi' \rangle + \operatorname{div}_{g_r} \xi,

where $\xi(r)$ is the one-parameter family of vector fields on $S^3$ defined by $\alpha(\xi) = -\langle \psi, \gamma(\alpha)\psi' \rangle$, for all $\alpha \in \Omega^1(S^3)$. Hence, the divergence theorem for the metric $g_r$ implies that $D$ is self-adjoint with respect the family of $L^2$ inner products on $\Omega^1(S^3, W_0^+ \otimes E_0)$ defined by $g_r$:

$$\int_{S^3} \langle D\psi, \psi' \rangle d \operatorname{vol}_r = \int_{S^3} \langle \psi, D\psi' \rangle d \operatorname{vol}_r.$$

---

The Agmon-Nirenberg theorem is not immediately applicable to the ordinary differential equation (5.16) since the differential operator $P_r := - *g_r d \oplus D$ is only self-adjoint on the Hilbert space

$$\mathfrak{H}_r := L^2(S^3, \Lambda^1 \otimes \mathfrak{su}(E_0)) \oplus L^2(S^3, W_0^+ \otimes E_0),$$

with $L^2$ inner products $(\cdot, \cdot)_r$ defined by the family of metrics $g_r$ on $S^3$, rather than a fixed inner product.

If $d \text{ vol}_r$ is the volume form on $S^3$ defined by the metric $g_r$, then we may write

$$d \text{ vol}_r = h_r^2 d \text{ vol}, \quad r \in (0, \varrho),$$

for some positive function $h_r$ on $S^3$, where $d \text{ vol}$ is the volume form on $S^3$ defined by the standard metric. However,

(5.17)

$$Q_r := h_r P_r h_r^{-1}, \quad r \in (0, \varrho),$$

is a differentiable path of self-adjoint, first-order, elliptic differential operators on the fixed, real Hilbert space underlying

$$\mathfrak{H} := L^2(S^3, \Lambda^1 \otimes \mathfrak{su}(E_0)) \oplus L^2(S^3, W_0^+ \otimes E_0),$$

with $L^2$ inner product $(\cdot, \cdot)$ defined by the standard metric on $S^3$. Indeed, if we define a Hilbert-space isomorphism $\mathfrak{H}_r \rightarrow \mathfrak{H}$ by $(b, \psi) \mapsto (\beta, \varphi) := h_r(b, \psi)$, then

$$\int_{S^3} \langle Q_r(\beta, \varphi), (\beta', \varphi') \rangle d \text{ vol} = \int_{S^3} \langle h_r P_r h_r^{-1} h_r(b, \psi), h_r(b', \psi') \rangle d \text{ vol}$$

$$= \int_{S^3} \langle P_r(b, \psi), (b', \psi') \rangle d \text{ vol}_r$$

$$= \int_{S^3} \langle (b, \psi), P_r(b', \psi') \rangle d \text{ vol}_r$$

$$= \int_{S^3} \langle h_r(b, \psi), h_r P_r h_r^{-1} h_r(b', \psi') \rangle d \text{ vol},$$

and therefore,

$$\int_{S^3} \langle Q_r(\beta, \varphi), (\beta', \varphi') \rangle d \text{ vol} = \int_{S^3} \langle (\beta, \varphi), Q_r(\beta', \varphi') \rangle d \text{ vol}, \quad r \in (0, \varrho).$$

The operators $Q_r$ have dense domain $L_1^2$. Since $(b, \psi) = h_r^{-1}(\beta, \varphi)$, we see that

$$\frac{d(b, \psi)}{dr} = -h_r^{-2} \frac{dh_r}{dr}(\beta, \varphi) + h_r^{-1} \frac{d(\beta, \varphi)}{dr},$$ and so, subsituting into (5.16) gives

$$\frac{d(\beta, \varphi)}{dr} = Q_r(\beta, \varphi) + h_r Z_r h_r^{-1}(\beta, \varphi) + h_r^{-1} \frac{dh_r}{dr}(\beta, \varphi),$$
$$r \in (0, \varrho),$$

with $(\beta, \varphi)$ a path in $\mathfrak{H}$.

5.3.5. Verification of the Agmon-Nirenberg conditions. We can now conclude the proof of our unique continuation result for reducible PU(2) monopoles:

Completion of proof of Proposition 5.19. The estimates (5.10) and (5.12) are, in principle, straightforward to check since we only need them for $r$ varying in the compact interval $[\frac{1}{2} r_0, r_1]$; the second condition, (5.12), requires a little more explanation since we need an estimate for $dQ/dr$. We first check condition (5.10). Comparing (5.15), (5.16), and (5.18), we find that

$$\left\| \frac{d(\beta, \varphi)}{dr} - Q_r(\beta, \varphi) \right\| \leq c_1 \|(\beta, \varphi)\|, \quad \frac{1}{2} r_0 \leq r \leq \frac{1}{2}\varrho,

for some positive constant $c_1 = c_1(g, r_0, A, \Phi)$, and so the ordinary differential equation (5.18) obeys the estimate (5.10) on the interval $[\frac{1}{2} r_0, r_1]$. To check condition (5.12), observe that the definition of $Q_r$ in (5.16) and (5.17) yields the pointwise bound

$$\left| \frac{dQ_r}{dr}(\beta, \varphi) \right| \leq C \left(|(\nabla \beta, \nabla \varphi)| + |(\beta, \varphi)|\right),

where $\frac{1}{2} r_0 \leq r \leq \frac{1}{2}\varrho$, for some positive constant $C = C(g, \tau, A_W, r_0)$, and $\nabla$ denotes covariant derivatives on $\Lambda^1 \otimes \mathfrak{su}(E_0)$ and $W_0^+ \otimes E_0 \times S^3$ which are independent of $r$. Thus, using the standard elliptic estimate for $Q_r$ we obtain the $L^2$ bound

$$\left\| \frac{dQ_r}{dr}(\beta, \varphi) \right\| \leq C \left(\|Q_r(\beta, \varphi)\| + \|(\beta, \varphi)\|\right),

and so, for $\frac{1}{2} r_0 \leq r \leq \frac{1}{2}\varrho,$

$$\left| (\beta, \varphi), \frac{dQ_r}{dr}(\beta, \varphi) \right| \leq C \left(\|Q_r(\beta, \varphi)\| + \|(\beta, \varphi)\|^2\right).

Therefore, (5.12) is obeyed with $c_2 = c_3 = C$ on the interval $[\frac{1}{2} r_0, r_1]$. By Theorem 5.25 and Remark 5.26, the solution $(\beta(r), \varphi(r))$ vanishes for $r \in (0, r_1)$ since it vanishes for $r \in (0, r_0)$. Hence, $(a(r), \phi(r)) = 0$ for $r \in (0, r_1)$ and $\hat{u}(A, \Phi) = (A, \Phi)$ on the ball $B(x_0, r_1)$. This completes the proof of Proposition 5.19. q.e.d.

## Appendix A. Holonomy perturbations and regularity

When defining our holonomy perturbations in §2.5.2 we deferred a detailed discussion of several important regularity issues which arise in their construction. The first concerns the regularity of sections of $E$ and $\mathfrak{su}(E)$ which are constructed by parallel transport via Sobolev connections and is described in §A.1. The second concerns the regularity of the $\mathcal{G}_E$ equivariant maps $\mathfrak{h}_{j,l,\alpha} : \mathcal{A}_E(X) \rightarrow L_{k+1}^2(X, \mathfrak{su}(E))$ and we show in §A.2 that these maps are $C^\infty$. (All of the $\mathcal{G}_E$ equivariant maps discussed here are $^\circ\mathcal{G}_E$ equivariant since $S_Z^1$ acts trivially on connections in $\mathcal{A}_E$; if the connection on det $E$ is not fixed, then all of the $\mathcal{G}_E$ equivariant maps are Aut $E$ equivariant.)

The definition of the maps $\mathfrak{m}_{j,l,\alpha}$ also makes use of the existence of a locally finite, $C^\infty$ ‘positive partition’ on a paracompact manifold modelled on a separable Hilbert space, in the sense of Proposition A.12. The differentials of the cutoff functions in these partitions need not be bounded a priori for the usual reason that in an infinite-dimensional Hilbert manifold, closed and bounded sets are not compact. Nonetheless, as we shall see in §A.3, it is possible to modify the standard proof [55] of the existence of a $C^\infty$ partition of unity on a paracompact $C^\infty$ manifold to produce $C^\infty$ cutoff functions all of whose differentials are bounded. The sums defining the perturbations $\vec{\tau} \cdot \vec{\mathfrak{m}}$ and $\vec{\vartheta} \cdot \vec{\mathfrak{m}}$ of §2.5.2 are finite when restricted to any of the open neighborhoods $(\pi \circ r_{Y_j})^{-1}(U_{j,\alpha}) \subset \mathcal{A}_E^*(X)$, where $r_{Y_j}: \mathcal{A}_E(X) \rightarrow \mathcal{A}_E(Y_j)$ is the restriction map and $\pi: \mathcal{A}_E(X) \rightarrow B_E(Y_j)$ is the canonical projection. However, the number of terms in these sums may be infinite in the neighborhood of a reducible connection: it is for this reason that they are required to converge with respect to a suitable choice of weights, as described in §2.5.2. We specify the choice of weights in §A.4 and explain why the $\mathcal{G}_E$ equivariant maps $\vec{\tau} \cdot \vec{\mathfrak{m}}$ and $\vec{\vartheta} \cdot \vec{\mathfrak{m}}$ are $C^\infty$ on $\mathcal{A}_E(X)$.

A.1. Parallel transport for Sobolev connections. The fact that parallel transport is well-defined for $L_2^2$ connections has been pointed out in [61]. However, to construct $L_{k+1}^2$ sections using parallel transport via $L_k^2$ connections with $k \geq 2$, we need to regularize the sections, taking care to do this gauge equivariantly. (Given an $L_k^2$ connection $A$, it does not follow that local sections constructed by $A$-parallel transport are in $L_{k+1}^2$. If we ignored the issue of equivariance, then it would suffice to use the standard smoothing kernel described in [33, §7.2 & §7.3], yielding a $C^\infty$ section irrespective of whether the connection is $L_k^2$ or $C^\infty$. Instead, we use the kernel

$$K_t(A)(x,y) \in \text{Hom}(\mathfrak{su}(E)|_y, \mathfrak{su}(E)|_x),$$

$t \in (0,\infty)$, of the heat operator

$$K_t(A) = \exp(-td_A^*d_A): L^2(X, \mathfrak{su}(E)) \rightarrow L_{k+1}^2(X, \mathfrak{su}(E)),$$

defined by the $C^\infty$ metric $g$ on TX and $L_k^2$ connection $A$ on E [34, §1.6]; related constructions are described in [84, p. 339], [85, p. 177]. The key well-known properties [12], [34, §1.6] of the heat kernel which we need are summarized below:

**Lemma A.1.** Continue the above notation and suppose that $\zeta \in L^2(X, \mathfrak{su}(E))$.

(1) As $t \to 0$, the heat operator $\exp(-td_A^*d_A)$ converges to the $L^2$ orthogonal projection onto Ker($d_A^*d_A$)$^\perp$.

(2) If $A$ on $\mathfrak{su}(E)$ is irreducible, then $K_t(A)(x,\cdot)$ converges to the Dirac delta distribution $\delta(x,\cdot)$.

(3) If $A$ is $L_k^2$, then $K_t(A)\zeta$ is $L_{k+1}^2$; if $A$ is $C^\infty$, then $K_t(A)\zeta$ is $C^\infty$.

(4) If $\zeta \in C^0(\widetilde{U}, \mathfrak{su}(E))$, for an open set $\widetilde{U} \subset X$, and $A$ is irreducible on $\mathfrak{su}(E)$, then $K_t(A)\zeta \rightarrow \zeta$ in $C^0(U, \mathfrak{su}(E))$ as $t \to 0$, for any open subset $U \subset U$.

Lemma A.1 continues to hold for unitary connections $A$ on Hermitian bundles $E$ over compact $C^\infty$ manifolds with boundary $\overline{Y} = Y \cup \partial Y$; we use the Neumann boundary conditions of [20, p. 192], [87, Proposition 2.1] to obtain an $L^2$ self-adjoint Laplacian $d_A^*d_A$. Our main application will be to sections defined by parallel translation:

**Lemma A.2.** Let $k \geq 2$ be an integer and let $A$ be an $L_k^2$ unitary connection on a Hermitian two-plane bundle $E$ over $X$. Let $x_0$ be a point in $X$, let $\zeta_0 \in \mathfrak{su}(E)|_{x_0}$, and let $B(x_0,r)$ be a geodesic ball with center $x_0$ and radius $r > 0$.

(1) Parallel transport with respect to $A$ is well-defined along $C^\infty$ paths in $X$.

---

(2) If $ \zeta $ is the section of $ \mathfrak{su}(E) |_{B(x_0,r)} $ obtained by A-parallel transport of $ \zeta_0 $ along radial geodesics originating at $ x_0 $ , and A is $ C^\infty $ , then $ \zeta $ is $ C^\infty $ on $ B(x_0,r) $ . If A is $ L_k^2 $ , then $ \zeta $ is $ C^0 $ on $ B(x_0,r) $ and its mollification $ K_t(A|_{B(x_0,r)})\zeta $ is $ L_k^{2+1} $ on $ B(x_0,r) $ , for any $ t > 0 $ .

Proof. Let $ \gamma : [0,1] \rightarrow X $ be a $ C^\infty $ path such that $ \gamma(0)=x_0 $ and let $ U \subset X $ be an open neighborhood of $ \gamma([0,1]) $ . We may suppose without loss of generality that $ A \in L_k^2(U,\Lambda^1 \otimes \mathfrak{u}(2)) $ is a connection matrix and consider the parallel transport of $ \eta_0 \in \mathbb{C}^2 $ . Note that we have a continuous Sobolev embedding $ L_2^2(U) \rightarrow L^2([0,1]) $ [2, Theorem V.4]. We wish to solve the ordinary differential equation

(A.1) $ \frac{d\eta}{dt}+a\eta=0, $ $ t \in[0,1], $

where $ a=\gamma^*A \in L^2([0,1],\mathfrak{u}(2)) $ , with initial condition $ \eta(0)=\eta_0 $ , for a solution $ \eta\in(L_1^2 \cap C^0)([0,1],\mathbb{C}^2) $ .

If A is $ C^\infty $ then there is a unique solution $ \eta\in C^\infty([0,1],\mathbb{C}^2) $ to (A.1) (see, for example, [36]) and it obeys the inequality [36, Lemma IV.4.1]

(A.2) $ |\eta(t)| \leq|\eta_0| \exp\left(\int_0^t|a(s)|ds\right)$ $ \leq|\eta_0| \exp\left(\|a\|_{L^1([0,1])}\right)\leq|\eta_0| \exp(c\|A\|_{L_2^2(U)}), $

for $ t \in[0,1] $ . If A is only $ L_2^2 $ , we may choose any sequence $ \{A_\alpha\} $ of $ C^\infty $ connections which converge to A in $ L_2^2 $ and let $ \{\eta_\alpha\} $ be the corresponding sequence of $ C^\infty $ solutions to (A.1). From (A.2) it follows that $ \{\eta_\alpha\} $ is $ C^0 $ - Cauchy, and then (A.1) implies that $ \{\eta_\alpha\} $ is $ L_1^2 $ - Cauchy with limit $ \eta\in(L_1^2 \cap C^0)([0,1],\mathbb{C}^2) $ solving (A.1). This proves Assertion (1).

From the proof of Assertion (1) we see that $ \zeta\in C^0(U,\mathfrak{su}(2)) $ . If the connection A is $ C^\infty $ on $ B(x_0,r) $ , then by differentiating (A.1) with respect to local coordinates (regarded as parameters [36, Chapter 5]) on $ B(x_0,r) $ and solving the resulting first order ordinary differential equations for the derivatives, it follows that the section $ \zeta $ is $ C^\infty $ on $ B(x_0,r) $ . The rest of Assertion (2) is an easy consequence of the properties of the smoothing kernel $ K_t(A)(x,y) $ given in Lemma A.1. q.e.d.

A.2. Regularity of holonomy maps. We consider the regularity of the holonomy maps from $ A \in \mathcal{A}_E $ to $ h_{\gamma,x_0}(A) \in \mathfrak{u}(E)|_{x_0} $ , to $ \hat{\mathfrak{h}}_\gamma(A) \in C^0(B(x_0,r_0),\mathfrak{su}(E)) $ , and to $ \mathfrak{h}_\gamma(A) \in L_k^{2+1}(B(x_0,r_0),\mathfrak{su}(E)) $ . See also [8, §3.3], [29, Lemma 1b.1], [86, §8a], and [90, §5A] for related calculations.

---

Let $\gamma : [0,1] \rightarrow X$ denote a parametrization for an oriented path $\gamma \subset X$ with $\gamma(0) = x_0$. The general Sobolev embedding [2, Theorem V.4] implies that we have a continuous restriction map $L_k^2(X, \Lambda^1 \otimes \mathfrak{su}(E)) \rightarrow L_{k-2}^2(\gamma, \Lambda^1 \otimes \mathfrak{su}(E))$, for $k \geq 2$. We fix an isomorphism $E|_\gamma \simeq \gamma \times \mathbb{C}^2$ of U(2) bundles and denote the connection matrix corresponding to a unitary connection $A$ on $E$ again by $A \in L_{k-2}^2(\gamma, \Lambda^1 \otimes \mathfrak{u}(2))$. Let $A + sa, s \in \mathbb{R}$, be a one-parameter family of nearby connections on $E$, with connection matrices $A(t) + sa(t) \in L_{k-2}^2(\gamma, \Lambda^1 \otimes \mathfrak{u}(2))$. Let $\xi_0 \in \mathbb{C}^2$ correspond to a point in the fiber $E|_{x_0}$ and, with respect to the connection $A + sa$, let $\xi(t;s)$ be the parallel transport of $\xi_0$ along $\gamma(t)$, so $\xi(t;s)$ solves

(A.3) $$\left(\frac{d}{dt} + A(t) + sa(t)\right) \xi(t;s) = 0,$$ $$\xi(0;s) = \xi_0.$$

Thus, if $P_{\gamma}(t;A) \in \text{Isom}(E|_{\gamma(0)}, E_{\gamma(t)}) \simeq \text{U}(2)$ denotes parallel transport along $\gamma$ from $\gamma(0)$ to $\gamma(t)$ with respect to the connection $A$, we have

$$\xi(t;s) = P_{\gamma}(t;A + sa)\xi_0,$$ $$t \in [0,1].$$

Therefore, our task is to compute

$$(DP_{\gamma}(t;\cdot))_A(a)\xi_0 = \frac{d}{ds}P_{\gamma}(t;A + sa)\xi_0 \bigg|_{s=0} = \frac{d\xi}{ds}(t;s) \bigg|_{s=0},$$ $$t \in [0,1].$$

Differentiating (A.3) with respect to $s$, we see that $d\xi(t;s)/ds$ solves

(A.4) $$\left(\frac{d}{dt} + A(t) + sa(t)\right)\frac{d\xi}{ds} = -a(t)\xi(t;s),$$ $$\frac{d\xi}{ds}(0;s) = 0.$$

Let $Y(t;s)$ be the fundamental matrix solution for the linear differential operator on the left-hand side. Then the solution $d\xi(t;s)/ds$ can be written as [36, Corollary IV.2.1]

$$\frac{d\xi}{ds}(t;s) = -Y(t;s) \int_0^t Y^{-1}(\tau;s)a(\tau)\xi(\tau;s) d\tau.$$

Since $\xi(t;s) = Y(t;s)\xi_0 = P_{\gamma}(t;A + sa)\xi_0$ for any $\xi_0 \in E|_{\gamma(0)}$, setting $s = 0$ above gives

(A.5) $$(DP_{\gamma}(t;\cdot))_A(a) = -P_{\gamma}(t;A) \int_0^t P_{\gamma}^{-1}(\tau;A)a(\tau)P_{\gamma}(\tau;A) d\tau,$$ and so, by the Sobolev embedding theorem, a derivative bound

(A.6) $|(DP_{\gamma}(t; \cdot))_A(a)| \leq \|a\|_{L^1(\gamma)} \leq c \|a\|_{L^2_{2,A}(X)}, t \in [0, 1]$.

The estimate (A.6) implies that the right-hand side of (A.5) is well-defined whenever $k \geq 2$. In particular, when $t = 1$ we have $P_{\gamma}(1; A) = h_{\gamma,x_0}(A)$, and so (A.5) gives

(A.7) $(Dh_{\gamma,x_0})_A(a) = -h_{\gamma,x_0}(A) \int_\gamma P_{\gamma}^{-1}(A)aP_{\gamma}(A)$.

Thus, we have a well-defined differential

$$
(Dh_{\gamma,x_0})_A : L_k^2(X, \Lambda^1 \otimes \mathfrak{u}(E)) \rightarrow T_h_{\gamma,x_0}(A) \mathrm{U}(E)|_{x_0} \simeq \mathfrak{u}(E)|_{x_0}
$$

of the holonomy map $h_{\gamma,x_0} : \mathcal{A}_E(X) \rightarrow \mathrm{U}(E)|_{x_0}$ at the point $A \in \mathcal{A}_E(X)$.

A similar argument shows that all higher derivatives exist by repeatedly applying the derivative formulas (A.5) and (A.7) (see, for example, [86, §8a]) and so we may conclude:

**Lemma A.3.** For $k \geq 2$, the holonomy map

$$h_{\gamma,x_0} : \mathcal{A}_E(X) \rightarrow \mathrm{U}(E)|_{x_0}$$

is $C^\infty$.

In the same vein, the holonomy map $h_{\gamma,x_0} : \mathcal{A}_E(X) \rightarrow \mathrm{SO}(\mathfrak{su}(E))|_{x_0}$ is $C^\infty$ and we have:

**Lemma A.4.** For $k \geq 2$, the following holonomy maps are $C^\infty$:

$$\mathcal{A}_E(X) \ni A \mapsto \hat{\mathfrak{h}}_{\gamma}(A) \in C^0(B(x_0,r_0), \mathfrak{su}(E)),$$

$$\mathcal{A}_E(X) \ni A \mapsto \mathfrak{h}_{\gamma}(A) \in L_{k+1}^2(B(x_0,r_0), \mathfrak{su}(E)).$$

Proof. The fact that $\hat{\mathfrak{h}}_{\gamma}$ is a $C^\infty$ map follows from the proof of Lemma A.3. The map $\mathfrak{h}_{\gamma}$ is defined by $\mathfrak{h}_{\gamma}(A) = K_t(A)\hat{\mathfrak{h}}_{\gamma}(A)$ and so the fact that the map

$$\mathcal{A}_E(X) \ni A \mapsto K_t(A) \in \mathrm{Hom}(L^2(B(x_0,r_0), \mathfrak{su}(E)),$$

$$L_{k+1}^2(B(x_0,r_0), \mathfrak{su}(E))$$

is $C^\infty$ yields the second conclusion. q.e.d.

---

A.3. Positive partitions and cutoff functions with bounded differentials on Hilbert manifolds. We modify Lang’s proof of the existence of a $C^\infty$ partition of unity on a paracompact $C^\infty$ manifold modelled on a separable Hilbert space [55, Corollary II.3.8] to produce a $C^\infty$ positive partition whose cutoff functions have bounded differentials of all orders; see Proposition A.12. Recall:

Proposition A.5 [55, Corollary II.3.8]. Let $\mathcal{X}$ be a paracompact $C^\infty$ manifold modelled on a separable Hilbert space $\mathfrak{H}$. Then $\mathcal{X}$ admits locally finite, $C^\infty$ partitions of unity: For any open cover of $\mathcal{X}$ there is a countable, locally finite open subcover $\{U_\alpha\}_{\alpha=1}^{\infty}$ and a family of $C^\infty$ functions $\psi_\alpha : \mathcal{X} \rightarrow [0,1]$ such that

- $\sup \psi_\alpha \subset U_\alpha$,
- $\sum_{\alpha=1}^{\infty} \psi_\alpha(x) = 1$ for all $x \in \mathcal{X}$.

We shall need the following generalizations to a Banach space setting of the analogous familiar facts from analysis on finite-dimensional spaces.