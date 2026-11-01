---
retention_scope: session
part: 6
total_parts: 6
---

[Part 6/6 of: PU(2) Monopoles. I: Regularity, Uhlenbeck Compactness, and Transversality]

Lemma A.6 [1, Proposition 1.3.10]. Let $M$ be a topological space and let $(N,d)$ be a complete metric space. Then the set $C(M,N)$ of all bounded continuous maps is a complete metric space with respect to the metric $D(f,g) := \sup \{d(f(x),g(x)) : x \in M\}$.

Let $\mathbf{E}, \mathbf{F}$ be Banach spaces and let $U \subset \mathbf{E}$ be an open subset. By analogy with the usual definitions in finite dimensions, we let $C^s(U, \mathbf{F})$ be the set of $C^s$ maps $f : U \rightarrow \mathbf{F}$ with norm

$$\|f\|_{C^s(U)} := \max_{0 \leq p \leq s} \sup_{x \in U} \|(D^p f)_x\| < \infty,

where $\|(D^p f)_x\|$ is the norm of $(D^p f)_x \in \text{Hom}(\otimes^p \mathbf{E}, \mathbf{F})$. Lemma A.6 implies that $C^0(U, \mathbf{F})$ is a Banach space. In general we have:

Lemma A.7. For any integer $s \geq 0$, the set $C^s(U, \mathbf{F})$ is a Banach space.

Proof. For the case $s = 1$ this follows from Lemma A.6 and [37, Theorem 1.1.5]. The general case [1, pp. 113–114] is proved in the same way using Taylor’s Theorem. q.e.d.

By analogy with the finite-dimensional case we set $C^\infty(U, \mathbf{F}) = \cap_{s \geq 0} C^s(U, \mathbf{F}).$

---

The $C^\infty$ cutoff functions produced by Proposition A.5 may not necessarily have bounded differentials on Hilbert manifolds, as their supports are not compact, so we now describe a modified procedure which does produce bounded cutoff functions.

Lemma A.8 [55, Lemma II.3.5]. Let $M$ be a metric space and let $\{B_\alpha\}_{\alpha=1}^{\infty}$ be a covering of a subset $W \subset M$ by open balls. Then there exists a locally finite open covering $\{V_\alpha\}_{\alpha=1}^{\infty}$ of $W$ such that $V_\alpha \subset B_\alpha$ for all $\alpha$ and

$$V_\alpha = B_\alpha \cap {}^c\bar{B}(x_{\alpha,1}, r_{\alpha,1}) \cap \cdots \cap {}^c\bar{B}(x_{\alpha,\alpha-1}, r_{\alpha,\alpha-1})$$,

where ${}^c\bar{B} = M - \bar{B}$.

Lemma A.9. Let $B_0, B_1, \ldots, B_m$ be open balls in a Hilbert space $\mathfrak{H}$ and let $V$ be a scalloped open subset:

$$V = B_0 \cap {}^c\bar{B}_1 \cap \cdots \cap {}^c\bar{B}_m.$$

Then there exists a $C^\infty$ function $\omega : \mathfrak{H} \rightarrow [0,1]$ such that $\omega(x) > 0$ if $x \in V$ and $\omega(x) = 0$ otherwise, while the differentials $D^p\omega$ are bounded for all $p \in \mathbb{N}$, with bounds depending only on $p, r_0, \ldots, r_m$.

Proof. Let $\varphi : \mathbb{R} \rightarrow [0,1]$ be a $C^\infty$ function such that $\varphi(t) = 1$ for $t \leq 1$, $0 < \varphi(t) < 1$ for $1 < t < 2$, and $\varphi(t) = 0$ for $t \geq 2$. Suppose $B_\alpha = B(x_\alpha, r_\alpha)$ for $\alpha = 0, \ldots, m$. Set

$$\varphi_\alpha(x) := \varphi(r_\alpha^{-2}\|x-x_\alpha\|^2), \quad x \in \mathfrak{H}, \quad \alpha = 1, \ldots, m,$$

so $0 \leq \varphi_\alpha < 1$ on ${}^c\bar{B}_\alpha$ and $\varphi_\alpha = 1$ on $\bar{B}_\alpha$. Set $\varphi_0(x) = \varphi(2r_0^{-2}\|x-x_0\|^2)$, so $0 < \varphi_0 \leq 1$ on $B_0$ and $\varphi_0 = 0$ on ${}^cB_0$. Then

$$\omega := \varphi_0 \prod_{\alpha=1}^{m}(1-\varphi_\alpha)$$

is positive on $V$ and zero on ${}^cV = \mathfrak{H}-V$, while

$$\|D^p\omega\| \leq C,$$

for some positive constant $C = C(\varphi,p,r_0, \ldots, r_m)$ and all $p \in \mathbb{N}$.

Lemma A.10. Let $A_1, A_2$ be non-empty, closed disjoint subsets of a separable Hilbert space $\mathfrak{H}$. Then there exists a $C^\infty$ function $\chi : \mathfrak{H} \rightarrow [0,1]$ such that $\chi(x) = 0$ if $x \in A_1$ and $\chi(x) > 0$ if $x \in A_2$, with bounded differentials of all orders.

---

Proof. By Lindelöf’s Theorem there is a countable collection of balls $\{B_{\alpha}\}_{\alpha=1}^{\infty}$ covering $A_2$ such that $B_{\alpha} \subset {}^c A_1 = \mathfrak{H}-A_1$. Let $W = \cup_{\alpha} B_{\alpha}$ and find a locally finite refinement $\{V_{\alpha}\}$ of scalloped open subsets $V_{\alpha} \subset B_{\alpha}$, using Lemma A.8, which covers $W$. Using Lemma A.9 we find a $C^{\infty}$ function $\omega_{\alpha}: \mathfrak{H} \rightarrow \mathbb{R}$ such that $\omega_{\alpha}$ is positive on $V_{\alpha}$, zero on ${}^c V_{\alpha}$, and has bounded differentials of all orders. The sum

$$\chi := \sum_{\alpha=1}^{\infty} \frac{2^{-\alpha} \omega_{\alpha}}{1 + \|\omega_{\alpha}\|_{C^{\alpha}(\mathfrak{H})}}$$

is finite on any neighborhood $V_{\alpha}$. The function $\chi : \mathfrak{H} \rightarrow \mathbb{R}$ is positive on $\cup_{\alpha} V_{\alpha} = W \supset A_2$ and zero on $A_1$. Moreover, $\chi$ has bounded differentials of all orders, as desired. q.e.d.

Remark A.11. It is at this point that the usual proof of existence of a partition of unity encounters difficulties if we wish to ensure that the cutoff function $\chi$ has bounded differentials of all orders. In the proof of Theorem II.3.7 of [55], Lang first constructs a function $\omega$ obeying the conclusions of Lemma A.10 and then a $C^{\infty}$ function $\sigma : \mathfrak{H} \rightarrow \mathbb{R}$ such that $\sigma > 0$ on the closed set ${}^c U$ disjoint from $A_2$, where $U$ is the open set where $\omega > 0$, and $\sigma = 0$ on $A_2$. He then defines $\chi = \omega / (\omega + \sigma)$, so $\chi = 1$ on $A_2$. In finite dimensions, the compactness of closed bounded sets ensures that $\chi$ will have bounded differentials of all orders if $A_2$ is bounded, but this obviously fails in infinite dimensions.

Proposition A.12. Let $\mathcal{X}$ be a paracompact $C^{\infty}$ manifold modelled on a separable Hilbert space $\mathfrak{H}$. Then $\mathcal{X}$ admits a locally finite, $C^{\infty}$ positive partition: For any open cover of $\mathcal{X}$ there is a countable, locally finite open subcover by parametrizations $\{U_{\alpha}, \pi_{\alpha}\}_{α=1}^{\infty}$, where

$$\pi_{\alpha}: \mathfrak{H} \supset \mathbf{U}_{\alpha} \simeq U_{\alpha} \subset \mathcal{X},$$

and a family of $C^{\infty}$ functions $\chi_{\alpha}: \mathcal{X} \rightarrow [0,1]$ such that

- supp $\chi_{\alpha} \subset U_{\alpha}$,
- $\sum_{\alpha=1}^{\infty} \chi_{\alpha}(x) > 0$ for all $x \in \mathcal{X}$,
- $\chi_{\alpha} \circ \pi_{\alpha}: \mathfrak{H} \rightarrow [0,1]$ has bounded differentials of all orders.

Proof. Let $\{B_x\}$ be an open covering of $\mathcal{X}$ by balls and, using para-compactness and Lemma A.8, let $\{U_{\alpha}\}$ be a countable, locally finite refinement such that each open subset $U_{\alpha}$ is contained in some $B_{x(\alpha)}$, where $\pi_{\alpha}^{-1} : \mathcal{X} \supset B_{x(\alpha)} \rightarrow \mathfrak{H}$ is a coordinate chart and $\pi_{\alpha}^{-1}(U_{\alpha}) = \mathbf{U}_{\alpha}$. We now find open refinements $\{V_{\alpha}\}$ and then $\{W_{\alpha}\}$ such that

$$\overline{W}_{\alpha} \subset V_{\alpha} \subset \overline{V}_{\alpha} \subset U_{\alpha},$$

the bar denoting closure in $\mathcal{X}$. For each $\alpha$, Lemma A.10 and the identification $\pi_{\alpha} : \mathfrak{H} \supset \mathbf{U}_{\alpha} \simeq U_{\alpha} \subset \mathcal{X}$ provide a $C^\infty$ cutoff function $\chi_{\alpha} : \mathcal{X} \rightarrow \mathbb{R}$ such that $\chi_{\alpha} > 0$ on $\overline{W}_{\alpha}$ and $\chi_{\alpha} = 0$ on $\mathcal{X} - V_{\alpha}$. The $C^\infty$ map $\chi_{\alpha} \circ \pi_{\alpha} : \mathbf{U}_{\alpha} \rightarrow [0,1]$ extends by zero to a $C^\infty$ map $\chi_{\alpha} \circ \pi_{\alpha} : \mathfrak{H} \rightarrow [0,1]$ having bounded differentials of all orders. Hence, $\{U_{\alpha}, \chi_{\alpha}\}$ is the desired positive partition. q.e.d.

Let $\overline{Y} = Y \cup \partial Y \subset X$ be a smooth submanifold-with-boundary. For any open subset $U \subset \mathcal{A}_E(Y)$ and $C^s$ function $f : U \rightarrow \mathbb{C}$, we define

(A.8) $$\|f\|_{C^s(U)} := \sup_{A \in U} \sup_{1 \leq i \leq s} |(D^s f)_A(a_1, \dots, a_s)|.$$

Let $\{B([A_{\alpha}], r_{\alpha})\}$ be a countable covering of $\mathcal{B}^*_E(Y)$ by $L_k^2$ balls with subordinate locally finite subcover $\{U_{\alpha}\}$ and $C^\infty$ positive partition $\{\chi_{\alpha}\}$, with supp $\chi_{\alpha} \subset U_{\alpha}$. We may suppose that $B([A_{\alpha}], r_{\alpha}) = \pi(B(A_{\alpha}, r_{\alpha}))$, where $B(A_{\alpha}, r_{\alpha}) \subset \mathcal{A}^*_E(Y)$ is an open $L_k^2$ ball in the Coulomb slice $A_{\alpha} + \text{Ker } d^*_{A_{\alpha}}$ with center $A_{\alpha}$ and radius $r_{\alpha}$, and $\pi : \mathcal{A}^*_E(Y) \rightarrow \mathcal{B}^*_E(Y)$ is the canonical projection. Let $\mathbf{U}_{\alpha} = \pi^{-1}(U_{\alpha}) \cap \mathbf{B}(A_{\alpha}, r_{\alpha})$. Then $\mathbf{U}_{\alpha} \subset A_{\alpha} + \text{Ker } d^*_{A_{\alpha}}$ and

$$\text{supp} \chi_{\alpha} \circ \pi \subset \pi^{-1}(U_{\alpha}) = \mathcal{G}_E(Y) \cdot \mathbf{U}_{\alpha} \simeq \mathcal{G}_E(Y) \times \mathbf{U}_{\alpha}.$$

Now $\chi_{\alpha} \circ \pi(u(A)) = \chi_{\alpha} \circ \pi(A)$ for all $u \in \mathcal{G}_E(Y)$, and by the construction of Proposition A.12 the $C^\infty$ map

(A.9) $$\chi_{\alpha} \circ \pi : A_{\alpha} + \text{Ker } d^*_{A_{\alpha}} \subset L_k^{2+1}(Y, \mathfrak{su}(E)) \rightarrow [0,1]$$

has bounded differentials of all orders with respect to the fixed $L_k^{2+1,A_{\alpha}}$ norm on $L_k^{2+1}(Y, \mathfrak{su}(E))$, that is, it has bounded differentials of all orders in the sense of Proposition A.12. Now for any $A \in \mathbf{U}_{\alpha}$, the $L_k^{2+1,A_{\alpha}}$ and $L_k^{2+1,A}$ norms on $L_k^{2+1}(Y, \mathfrak{su}(E))$ compare uniformly with constants depending only on $r_{\alpha} \geq \|A-A_{\alpha}\|_{L_k^{2+1,A_{\alpha}}}$ (since $k \geq 2$), and so the maps (A.9) have bounded differentials of all orders in the sense of equation (A.8). Moreover, the same holds for the maps

$$\chi_{\alpha} \circ \pi : \mathcal{A}^*_E(Y) \rightarrow [0,1].$$

---

Finally, we have a restriction map $r_Y : \mathcal{A}_E^*(X) \rightarrow \mathcal{A}_E^*(Y)$ given by $A \mapsto A|_Y$ and the composition

$$\chi_\alpha \circ \pi \circ r_Y : \mathcal{A}_E^*(X) \rightarrow [0,1]$$

again has bounded differentials of all orders in the sense of equation (A.8).

A.4. Uniform convergence of holonomy perturbations on neighborhoods of reducibles. In §2.5.2 we constrained the sequences perturbations $\vec{\tau}$ and $\vec{\vartheta}$ to vary in certain weighted $\ell_{\delta}^1$ spaces. We now show that a sequence of positive weights $\delta \in \ell^\infty(\mathbb{R}^+)$ may be chosen in such a way that the sums $\vec{\tau} \cdot \vec{\mathfrak{m}}$ and $\vec{\vartheta} \cdot \vec{\mathfrak{m}}$ and all their differentials converge uniformly on $\mathcal{A}_E(X)$.

For any open subset $U \subset \mathcal{A}_E(X)$ and $C^s$ map

$$f : U \rightarrow L_{k+1}^2(X, \mathfrak{su}(E)),$$

we define

(A.10) $$\|\mathfrak{f}\|_{C^s(U)} := \sup_{A \in U} \sup_{1 \leq i \leq s} \|(D^s f)_A(a_1, \ldots, a_s)\|_{L_{k+1}^2(A(X))}.$$

We then have:

Proposition A.13. Continue the notation of §2.5.2 and let $k \geq 2$ be an integer. Then there exists a sequence $\delta = (\delta_\alpha)_{\alpha=1}^{\infty} \in \ell^\infty((0,1])$ of positive weights such that the $\mathcal{G}_E$ equivariant maps

$$\vec{\tau} \cdot \vec{\mathfrak{m}} : \mathcal{A}_E(X) \rightarrow L_{k+1}^2(X, \mathfrak{gl}(\Lambda^+) \otimes_{\mathbb{R}} \mathfrak{so}(\mathfrak{su}(E))),$$

$$\vec{\vartheta} \cdot \vec{\mathfrak{m}} : \mathcal{A}_E(X) \rightarrow L_{k+1}^2(X, \mathrm{Hom}(W^+, W^-) \otimes_{\mathbb{C}} \mathfrak{sl}(E)),$$

are $C^\infty$, with uniformly bounded differentials of all orders in the sense of (A.10). In particular, they satisfy the following $C^0$ estimates for $r \geq k + 1,

$$\sup_{A \in \mathcal{A}_E} \|\vec{\vartheta} \cdot \vec{\mathfrak{m}}(A)\|_{L_{k+1}^2(A(X))} \leq C \|\vec{\vartheta}\|_{\ell_{\delta}^1(C^r(X))},$$

$$\sup_{A \in \mathcal{A}_E} \|\vec{\vartheta} \cdot \vec{\mathfrak{m}}(A)\|_{L_{k+1}^2(A(X))} \leq C \|\vec{\vartheta}\|_{\ell_{\delta}^1(C^r(X))},$$

for some positive constant $C = C(g,k)$, and more generally they satisfy the $C^s$ estimates of (A.11) and (A.12), for every integer $s \geq 0$.

---

Remark A.14. As should be clear from their definition, the maps $\vec{\tau} \cdot \vec{m}$ and $\vec{\vartheta} \cdot \vec{m}$ are not analytic, although this will cause no difficulty in practice.

Proof. It suffices to consider $\vec{\vartheta} \cdot \vec{m}$, since the argument for $\vec{\tau} \cdot \vec{m}$ is obviously identical. We first observe that the sum $\vec{\vartheta} \cdot \vec{m}(A)$ is finite for each connection $A \in \mathcal{A}_E(X)$, and so defines an element of $L_{k+1}^2(X, \text{Hom}(W^+, W^-) \otimes \mathfrak{gl}(E))$, while it is identically zero if $A$ is reducible on $X$. However, on any open neighborhood of a reducible connection $A \in \mathcal{A}_E(X)$, the number of terms in the sum $\vec{\vartheta} \cdot \vec{m}$ may be infinite, and so our task is to choose a sequence of weights $\delta$ such that this sum and all its differentials converge uniformly on $\mathcal{A}_E(X)$. The sum $\vec{\vartheta} \cdot \vec{m}$ will then define a $C^\infty$ map. We begin with a couple of preparatory lemmas.

Lemma A.15. Let $\overline{Y} = Y \cup \partial Y \subset X$ be a smooth submanifold with boundary, let $B(A_0, r_0) \subset \mathcal{A}_E^*(Y)$ be an open $L_k^2$ ball with $k \geq 2$, and let $\eta \in L^2(Y, \mathfrak{su}(E))$. Then the maps

$$B(A_0, r_0) \ni A \mapsto f(A) := e^{-td_A^*d_A} \eta \in L_{k+1}^2(Y, \mathfrak{su}(E))$$

have bounded differentials of all orders, in the sense of (A.10), with constants $c = c(k, r_0, s, t)$:

$$\|\mathfrak{f}\|_{C^s(B(A_0, r_0))} \leq c\|\eta\|_{L^2(Y)}.$$

Proof. The Sobolev multiplication theorems and the fact that $k \geq 2$ imply that the norms

$$\|\zeta\|_{L_{k+1}^2(A(Y))} \quad \text{and} \quad \|\zeta\|'_{L_{k+1}^2(A(Y))} := \|(1 + \Delta_A)^{(k+1)/2}\zeta\|_{L^2(Y)}$$

on $L_{k+1}^2(Y, \mathfrak{su}(E))$ are equivalent for $A \in B(A_0, r_0) \subset \mathcal{A}_E^*(Y)$, with constants depending at most on $k, r_0$.

Since $\Delta_A = d_A^*d_A$, its derivative with respect to $A$ in the direction $\delta A = a$ is given by $\delta \Delta_A = [a, \cdot]^*d_A + d_A^*[a, \cdot]$; we use the abbreviation $\delta \Delta_A = (D \Delta_{\cdot})_A(a)$. The connection $A_0$ is irreducible by hypothesis and so for a small enough open $L_k^2$ ball $B(A_0, r_0)$, there is a positive constant $\lambda_0 > 0$ such that $\lambda[A] \geq \lambda_0 > 0$ for all $A \in B(A_0, r_0)$, where $\lambda[A]$ is the least eigenvalue of $\Delta_A$. Thus,

$$\text{Spec}(\Delta_A) \subset [\lambda_0, \infty), \quad A \in B(A_0, r_0),$$ and, for any holomorphic function $f$ on an open neighborhood $\Omega \subset \mathbb{C}$ with $\text{Spec}(\Delta_A) \subset \Omega$ and $\Gamma$ any contour that surrounds $\text{Spec}(\Delta_A)$ in $\Omega$, we have [76]

$$f(\Delta_A) = \frac{1}{2\pi i} \oint_{\Gamma} f(\lambda)(\lambda - \Delta_A)^{-1} d\lambda,$$

$$(Df)_{\Delta_A}(\delta \Delta_A) = \frac{1}{2\pi i} \oint_{\Gamma} f(\lambda)(\lambda - \Delta_A)^{-1}(\delta \Delta_A)(\lambda - \Delta_A)^{-1} d\lambda,$$

and similarly for all higher-order derivatives. Note that

$$(1 + \Delta_A)^{(k+1)/2} f(\Delta_A)$$

$$= \frac{1}{2\pi i} \oint_{\Gamma}(1 + \lambda)^{(k+1)/2} f(\lambda)(\lambda - \Delta_A)^{-1} d\lambda,$$

$$(1 + \Delta_A)^{(k+1)/2}(Df)_{\Delta_A}(\delta \Delta_A)$$

$$= \frac{1}{2\pi i} \oint_{\Gamma}(1 + \lambda)^{(k+1)/2} f(\lambda)(\lambda - \Delta_A)^{-1}(\delta \Delta_A)(\lambda - \Delta_A)^{-1} d\lambda.$$

We can fix $\Omega$ and $\Gamma \subset \Omega$ such that $\text{dist}(\Gamma, \text{Spec}(\Delta_A)) \geq d_0 > 0$, for some positive constant $d_0$ and all $A \in B(A_0,r_0)$ (see [34, §1.6]). Now choose $f(z) = e^{-tz}$ and $f_{k+1}(z) = (1 + z)^{(k+1)/2} f(z)$, and estimate as in [34, p. 53]:

$$\|e^{-t\Delta_A}\eta\|_{L^2_{k+1,A}(Y)} \leq c\|(1 + \Delta_A)^{(k+1)/2}e^{-t\Delta_A}\eta\|_{L^2(Y)}$$

$$\leq c \oint_{\Gamma} \left|(1 + \lambda)^{(k+1)/2}e^{-t\lambda} d\lambda\right| \sup_{\lambda \in \Gamma} \|(\lambda - \Delta_A)^{-1}\eta\|_{L^2(Y)}$$

$$\leq c \|\eta\|_{L^2(Y)},$$

which gives the desired $C^0$ bound

$$\sup_{A \in B(A_0,r_0)} \|e^{-t\Delta_A}\eta\|_{L^2_{k+1,A}(Y)} \leq c \|\eta\|_{L^2(Y)},$$

where $c = c(d_0,k,r_0,t)$.

To obtain the $C^1$ bound, observe that

$$\|(Df)_{\Delta_A}(\delta \Delta_A)\eta\|_{L^2_{k+1,A}(Y)}$$

$$\leq c\|(1 + \Delta_A)^{(k+1)/2}(Df)_{\Delta_A}(\delta \Delta_A)\eta\|_{L^2(Y)}$$

$$\leq c \oint_{\Gamma} \left|(1 + \lambda)^{(k+1)/2}f(\lambda) d\lambda\right| \sup_{\lambda \in \Gamma} \|(\lambda - \Delta_A)^{-1}(\delta \Delta_A)(\lambda - \Delta_A)^{-1}\eta\|_{L^2(Y)}$$

$$\leq \sup_{\lambda \in \Gamma} c\|(\lambda - \Delta_A)^{-1}(\delta \Delta_A)(\lambda - \Delta_A)^{-1}\eta\|_{L^2(Y)}.$$

---

Our expression for $\delta \Delta_A$ gives

$$\|(\lambda - \Delta_A)^{-1}(\delta \Delta_A)(\lambda - \Delta_A)^{-1}\eta\|_{L^2(Y)}
\leq \|(\lambda - \Delta_A)^{-1}([a, \cdot]^*d_A + d_A^*[a, \cdot])(\lambda - \Delta_A)^{-1}\eta\|_{L^2(Y)}
\leq c\left(\|[a, \cdot]^*d_A(\lambda - \Delta_A)^{-1}\eta\|_{L^2(Y)} + \|d_A^*[a, \cdot](\lambda - \Delta_A)^{-1}\eta\|_{L^2(Y)}\right)
\leq c\|a\|_{L^2_{2;A}(Y)}\|(\lambda - \Delta_A)^{-1}\eta\|_{L^2_{2;A}(Y)}
\leq c\|a\|_{L^2_{k,A}(Y)}\|\eta\|_{L^2(Y)},

where $c = c(r_0,d_0)$. Combining these estimates yields

$$\|\delta(e^{-t \Delta_A})\eta\|_{L^2_{k+1,A}(Y)} \leq c\|a\|_{L^2_{k,A}(Y)}\|\eta\|_{L^2(Y)},

and so we have the desired $C^1$ bound

$$\sup_{A \in B(A_0,r_0)} \sup_{a \|_{L^2_{k,A}(X)}} \|(De^{-t \Delta(\cdot)})_A(a)\eta\|_{L^2_{k+1,A}(Y)} \leq c\|\eta\|_{L^2(Y)},

for some $c = c(d_0,k,r_0,t)$. The analysis can be repeated, essentially unchanged, for all higher differentials and is left to the reader. q.e.d.

**Lemma A.16.** The $G_E$ equivariant holonomy maps

$$\mathfrak{m}_{j,l,\alpha}: \mathcal{A}_E(X) \to L^2_{k+1}(X, \mathfrak{su}(E))$$

of (2.20) are $C^\infty$ with bounded differentials of all orders in the sense of (A.10).

Proof. Recall from (2.17) and (2.20) that

$$\mathfrak{m}_{j,l,\alpha}(A) = \beta_j[A]\chi_{j,\alpha}[A|_{B(x_j,2R_0)}]\varphi_j\mathfrak{h}_{\gamma_{j,l,\alpha}}(A),$$

$$\varphi_j\mathfrak{h}_{\gamma_{j,l,\alpha}}(A) = \varphi_jK_t(A|_{B(x_0,2R_0)})\hat{\mathfrak{h}}_{\gamma_{j,l,\alpha}}(A).$$

The cutoff functions $\chi_{j,\alpha} \circ \pi \circ r_B(x_j,2R_0): \mathcal{A}_E(X) \to [0,1]$ have bounded differentials of all orders, in the sense of (A.8), by the remarks following Proposition A.12; moreover, they are supported in $\mathcal{A}^*_E(X)$. The functions $\beta_j: \mathcal{A}_E(X) \to [0,1]$ have bounded differentials of all orders, as is clear from their definition in (2.18). Finally, from the proofs of Lemmas A.3 and A.4, together with Lemma A.15, one can see that the maps

$$\varphi_j K_t(\cdot|_{B(x_0,2R_0)})\hat{\mathfrak{h}}_{\gamma_{j,l,\alpha}}: \mathcal{A}^*_E(X) \to L^2_{k+1}(X, \mathfrak{su}(E))$$ have bounded differentials of all orders in the sense of (A.10) on open
subsets $G_E \cdot B(A_0, r_0) \subset A^*_E(X)$, where $B(A_0, r_0)$ is an open $L_k^2$ ball in
$K_{A_0} \subset A^*_E(X)$. q.e.d.

Given Lemma A.16, we have

$$M_{\alpha,s} := \max_{j,l} \|m_{j,\alpha,l}\|_{C^s(A_E)} < \infty,$$

where we recall that $1 \leq l \leq 3$ and $1 \leq j \leq N_b$. Now choose a sequence
of positive weights $\delta = (\delta_\alpha)_{\alpha=1}^{\infty} \in \ell^\infty(\mathbb{R}^+)$ by setting

$$\delta_\alpha := \left(1 + \max_{0 \leq s \leq \alpha} M_{\alpha,s}\right)^{-1}, \quad \alpha \in \mathbb{N},$$

and suppose $\vec{\vartheta} \in \ell^1_{\delta}(\mathbb{A}, C^r(X))$. Then

$$\|\vec{\vartheta}\|_{\ell^1_{\delta}(C^r(X))} = \sum_{j,l,\alpha} \delta_\alpha^{-1} \|\vartheta_{j,l,\alpha}\|_{C^r(X)} < \infty,$$

and therefore,

$$\|\vec{\vartheta} \cdot \vec{m}\|_{C^s(A_E)} \leq \sum_{j,l,\alpha} \|\vartheta_{j,l,\alpha} m_{j,l,\alpha}\|_{C^s(A_E)}$$

$$\leq c \sum_{j,l,\alpha} \|\vartheta_{j,l,\alpha}\|_{L^2_{k+1}(X)} \|m_{j,l,\alpha}\|_{C^s(A_E)} \text{ by (A.10)}$$
$$\leq c \sum_{j,l,\alpha} \|\vartheta_{j,l,\alpha}\|_{C^r(X)} M_{\alpha,s},$$

since $r \geq k+1$. Here, $c = c(g,k)$ is a universal positive constant coming
from the continuous Sobolev multiplication $L_{k+1}^2 \times L_{k+1,A}^2 \to L_{k+1,A}^2$. Hence, using the facts that $M_{\alpha,s} \leq 1 + \max_{0 \leq t \leq \alpha} M_{\alpha,t} = \delta_\alpha^{-1}$ for $\alpha \geq s$ and $1 \leq \delta_{\alpha}^{-1}$ for $1 \leq \alpha \leq s - 1$, we get

$$\|\vec{\vartheta} \cdot \vec{m}\|_{C^s(\mathcal{A}_E)} \leq c \sum_{j,l} \left( \sum_{\alpha=1}^{s-1} M_{\alpha,s} \|\vartheta_{j,l,\alpha}\|_{C^r(X)} + \sum_{\alpha \geq s} \delta_{\alpha}^{-1} \|\vartheta_{j,l,\alpha}\|_{C^r(X)} \right)$$

$$\leq c \left( 1 + \max_{1 \leq \alpha \leq s-1} M_{\alpha,s} \right) \sum_{j,l} \left( \sum_{\alpha=1}^{s-1} \|\vartheta_{j,l,\alpha}\|_{C^r(X)} \right)$$

(A.11)

$$+ \sum_{\alpha \geq s} \delta_{\alpha}^{-1} \|\vartheta_{j,l,\alpha}\|_{C^r(X)}$$

$$\leq c \left( 1 + \max_{1 \leq \alpha \leq s-1} M_{\alpha,s} \right) \sum_{j,l,\alpha} \delta_{\alpha}^{-1} \|\vartheta_{j,l,\alpha}\|_{C^r(X)}$$

$$= C \|\vec{\vartheta}\|_{\ell_8^{1}(C^r(X))} < \infty,

where $C = C(g, s, k)$ is defined by the last equality above. In particular, we see that $\vec{\vartheta} \cdot \vec{m}$ is a $C^s$ map on $\mathcal{A}_E(X)$, for every integer $s \geq 0$. The same argument gives

(A.12) $$\|\vec{\tau} \cdot \vec{m}\|_{C^s(\mathcal{A}_E)} \leq C \|\vec{\tau}\|_{\ell_8^{1}(C^r(X))} < \infty,

and $\vec{\tau} \cdot \vec{m}$ is a $C^s$ map on $\mathcal{A}_E(X)$, for every integer $s \geq 0$. q.e.d.

## References

[1] R. Abraham, J. E. Marsden & T. Ratiu, Manifolds, tensor analysis, and applications, 2nd ed., Springer, New York, 1988.

[2] R. A. Adams, Sobolev spaces, Academic Press, Orlando, FL, 1975.

[3] S. Agmon, Unicité et convexité dans les problèmes differentiels, Sém. Math. Sup., 1965, Univ. of Montreal Press, 1966.

[4] S. Agmon & L. Nirenberg, Lower bounds and uniqueness theorems for solutions of differential equations in Hilbert spaces, Comm. Pure Appl. Math. 20 (1967) 207–229.

[5] N. Aronszajn, A unique continuation theorem for solutions of elliptic partial differential equations or inequalities of the second order, J. Math. Pures Appl. 36 (1957) 235–249.

---

[6] M. F. Atiyah, V. K. Patodi & I. M. Singer, *Spectral asymmetry in Riemannian geometry. I*, Math. Proc. Cambridge Philos. Soc. **77** (1975) 43–69.

[7] T. Aubin, *Nonlinear analysis on complex manifolds. Monge-Ampère Equations*, Springer, New York, 1982.

[8] P. J. Braam & S. K. Donaldson, *Floer’s work on instanton homology, knots, and surgery*, The Floer Memorial Volume, (eds. H. Hofer et al.), Birkhäuser, Boston, 1995, 196–256.

[9] S. B. Bradlow & G. D. Daskalopoulos, *Moduli of stable pairs for holomorphic bundles over Riemann surfaces*, Internat. J. Math. **2** (1991) 477–513.

[10] S. B. Bradlow & O. Garcia-Prada, *Non-abelian monopoles and vortices*, Proc. Conference on Geom. and Phys. (Aarhus, 1995), Lecture Notes in Pure and Appl. Math. **184**, Dekker, New York, 1997, 567–589; alg-geom/9602010.

[11] T. Bröcker & T. tom Dieck, *Representations of compact Lie groups*, Springer, New York, 1985.

[12] I. Chavel, *Eigenvalues in Riemannian geometry*, Academic Press, Orlando, FL, 1984.

[13] R. Constantinescu, MIT Thesis (Mathematics), 1996.

[14] S. K. Donaldson, *An application of gauge theory to four-dimensional topology*, J. Differential Geom. **18** (1983) 279–315.

[15] _____, *Connections, cohomology and the intersection forms of four-manifolds*, J. Differential Geom. **24** (1986) 275–341.

[16] _____, *Irrationality and the h-cobordism conjecture*, J. Differential Geom. **26** (1987), 141–168.

[17] _____, *The orientation of Yang-Mills moduli spaces and 4-manifold topology*, J. Differential Geom. **26** (1987) 397–428.

[18] _____, *Polynomial invariants for smooth four-manifolds*, Topology **29** (1990) 257–315.

[19] _____, *The Seiberg-Witten equations and four-manifold topology*, Bull. Amer. Math. Soc. **33** (1996) 45–70.

[20] S. K. Donaldson & P. B. Kronheimer, *The geometry of four-manifolds*, Oxford University Press, Oxford, 1990.

[21] G. Ellingsrud & L. Göttsche, *Wall-crossing formulas, Bott residue formula and the Donaldson invariants of rational surfaces*, alg-geom/9506019.

[22] P. M. N. Feehan, *Critical-exponent Sobolev norms and the slice theorem for the quotient space of connections*, submitted to a print journal, October, 1996; dg-ga/9711004.

---

[23] ____, Generic metrics, irreducible rank-one PU(2) monopoles, and transversality, submitted to a print journal, August 27, 1997.

[24] P. M. N. Feehan & T. G. Leness, PU(2) monopoles and relations between four-manifold invariants, Topology Appl. 88 (1988) 111–145; dg-ga/9709022.

[25] ____, PU(2) monopoles, II: Highest-level singularities and relations between four-manifold invariants, submitted to a print journal, December 8, 1997; dg-ga/9712005.

[26] ____, PU(2) monopoles, III: Existence of gluing and obstruction maps, in preparation.

[27] ____, PU(2) monopoles, IV: Surjectivity of gluing maps, in preparation.

[28] R. Fintushel & R. Stern, Donaldson invariants of 4-manifolds with simple type, J. Differential Geom. 42 (1995) 577–633.

[29] A. Floer, An instanton-invariant for 3-manifolds, Comm. Math. Phys. 118 (1988) 215–240.

[30] D. Freed & K. K. Uhlenbeck, Instantons and four-manifolds, 2nd ed., Springer, New York, 1991.

[31] R. Friedman & J. W. Morgan, Smooth four-manifolds and complex surfaces, Springer, Berlin, 1994.

[32] R. Friedman & Z. Qin, Flips of moduli spaces and transition formulas for Donaldson polynomial invariants of rational surfaces, Comm. Anal. Geom. (1995) 11–83.

[33] D. Gilbarg & N. Trudinger, Elliptic partial differential equations of second order, 2nd ed., Springer, New York, 1983.

[34] P. B. Gilkey, Invariance theory, the heat equation, and the Atiyah-Singer index theorem, Publish or Perish, Wilmington, DE, 1984.

[35] L. Göttsche, Modular forms and Donaldson invariants for 4-manifolds with $b_+ = 1$, J. Amer. Math. Soc. 9 (1996), 827–843.

[36] P. Hartman, Ordinary differential equations, 2nd ed., Birkhäuser, Boston, 1982.

[37] L. Hörmander, The analysis of linear partial differential operators, Vol. III, Springer, New York, 1983.

[38] S. Hyun, J. Park & J-S. Park, Topological QCD, Nuclear Phys. B 453 (1995) 199–224; hep-th/9503201.

[39] ____, $N = 2$ Supersymmetric QCD and four-manifolds, I: the Donaldson and the Seiberg-Witten invariants, hep-th/9508162.

[40] R. V. Kadison & J. R. Ringrose, Fundamentals of the theory of operator algebras, Vol. I, Academic Press, New York, 1983.

---

[41] T. Kato, Perturbation theory for linear operators, 2nd ed., Springer, New York, 1984.

[42] J. Kazdan, Unique continuation in geometry, Comm. Pure Appl. Math. 41 (1988) 667–681.

[43] S. Kobayashi Differential geometry of complex vector bundles, Princeton University Press, Princeton, NJ, 1987.

[44] S. Kobayashi & K. Nomizu, Foundations of differential geometry, Vols. I & II, Wiley, New York, 1963 & 1968.

[45] D. Kotschick & J. W. Morgan, SO(3) invariants for four-manifolds with $b^+ = 1$. II, J. Differential Geom. 39 (1994) 433–456.

[46] P. B. Kronheimer, Seiberg-Witten invariants for four-manifolds, Lectures at Oxford University, Spring 1995.

[47] P. B. Kronheimer & T. S. Mrowka, The genus of embedded surfaces in the projective plane, Math. Res. Lett. 1 (1994) 797–808.

[48] _____, Embedded surfaces and the structure of Donaldson’s polynomial invariants, J. Differential Geom. 43 (1995) 573–734.

[49] _____, Monopoles and contact structures, Invent. Math. 130 (1997) 209–255.

[50] J. M. F. Labastida & C. Lozano, Mathai-Quillen formulation of twisted $N=4$ supersymmetric Gauge theories in four dimensions, Nuclear Phys. B 502 (1997) 741–790; hep-th/9702106.

[51] J. M. F. Labastida & M. Mariño, Non-abelian monopoles on four-manifolds, Nuclear Phys. B 448 (1995) 373–395; hep-th/9504010.

[52] _____, Polynomial invariants for SU(2) monopoles, Nuclear Phys. B 456 (1995) 633–668; hep-th/9507140.

[53] _____, Twisted $N=2$ supersymmetry with central charge and equivariant cohomology, Comm. Math. Phys. 185 (1997) 37–71; hep-th/9603169.

[54] O. A. Ladyzhenskaya & N. N. Ural’tseva, Linear and quasilinear elliptic equations, Academic Press, New York, 1968.

[55] S. Lang, Differential and Riemannian manifolds, 3rd ed., Springer, New York, 1995.

[56] H. B. Lawson, The theory of gauge fields in four dimensions, Conf. Board Math. Sci. 58, Amer. Math. Soc., Providence, RI, 1985.

[57] H. B. Lawson & M-L. Michelsohn, Spin geometry, Princeton Univ. Press, Princeton, NJ, 1988.

[58] T. G. Leness, Donaldson wall-crossing formulas via topology, Forum Math., to appear; dg-ga/9603016.

---

[59] J. Li & G. Tian, Virtual moduli cycles and Gromov-Witten invariants of general symplectic manifolds, alg-geom/9602007.

[60] G. Moore & E. Witten, Integration over the u-plane in Donaldson theory, Adv. Theor. Math. Phys. 1 (1997) 298–387; hep-th/9709193.

[61] J. W. Morgan, Gauge theory and the topology of smooth four-manifolds, Lecture Notes, Harvard University, 1988.

[62] _____, The Seiberg-Witten equations and applications to the topology of smooth four-manifolds, Princeton University Press, Princeton, NJ, 1996.

[63] J. W. Morgan, T. S. Mrowka & D. Ruberman, $L^2$ moduli spaces and a vanishing theorem for Donaldson polynomial invariants, Internat. Press, Cambridge, MA, 1994.

[64] C. B. Morrey, Multiple integrals in the calculus of variations, Springer, New York, 1966.

[65] T. S. Mrowka, Seiberg-Witten invariants for four-manifolds, Lectures at Harvard University, Spring 1995.

[66] T. S. Mrowka, P. S. Ozsváth & B. Yu, Seiberg-Witten monopoles on Seifert-fibered spaces, Comm. Anal. Geom. 5 (1997) 685–791.

[67] C. Okonek & A. Teleman, The coupled Seiberg-Witten equations, vortices, and moduli spaces of stable pairs, Internat. J. Math. 6 (1995) 893–910; alg-geom/9505012.

[68] _____, Quaternionic monopoles, Comm. Math. Phys. 180 (1996) 363–388; alg-geom/9505029.

[69] _____, Recent developments in Seiberg-Witten theory and complex geometry, alg-geom/9612015.

[70] T. H. Parker, Gauge theories on four dimensional Riemannian manifolds, Comm. Math. Phys. 85 (1982) 563–602.

[71] V. Y. Pidstrigach, From Seiberg-Witten to Donaldson: SO(3) monopole equations, Lecture at Newton Institute, Cambridge, December 1994.

[72] _____, Seiberg-Witten and Donaldson invariants, Lecture at Oberwolfach, May 1996.

[73] V. Y. Pidstrigach & A. N. Tyurin, Invariants of the smooth structure of an algebraic surface arising from the Dirac operator, Russian Acad. Sci. Izv. Math. 40 (1993) 267–351.

[74] _____, Localization of Donaldson invariants along the Seiberg-Witten classes, dg-ga/9507004.

[75] Y. Ruan, Virtual neighborhoods and pseudoholomorphic curves, alg-geom/9611021.

[76] W. Rudin, Functional analysis, McGraw-Hill, New York, 1973.

---

[77] D. Salamon, Spin geometry and Seiberg-Witten invariants, Birkhäuser, Boston, to appear.

[78] S. Sedlacek, A direct method for mimizing the Yang-Mills functional, Comm. Math. Phys. 86 (1982) 515–527.

[79] B. Siebert, Gromov-Witten invariants for general symplectic manifolds, alg-geom/9608005.

[80] S. Smale, An infinite-dimensional version of Sard’s theorem, Amer. J. Math. 87 (1973) 213–221.

[81] C. H. Taubes, Self-dual Yang-Mills connections on non-self-dual 4-manifolds, J. Differential Geom. 17 (1982) 139–170.

[82] _____, Self-dual connections on 4-manifolds with indefinite intersection matrix, J. Differential Geom. 19 (1984) 517–560.

[83] _____, Path-connected Yang-Mills moduli spaces, J. Differential Geom. 19 (1984) 337–392.

[84] _____, A framework for Morse theory for the Yang-Mills functional, Invent. Math. 94 (1988) 327–402.

[85] _____, The stable topology of self-dual moduli spaces, J. Differential Geom. 29 (1989) 162–230.

[86] _____, Casson’s invariant and gauge theory, J. Differential Geom. 31 (1990) 547–599.

[87] _____, $L^2$ moduli spaces on 4-manifolds with cylindrical ends, Internat. Press, Cambridge, MA, 1993.

[88] _____, Unique continuation theorems in gauge theories, Comm. Anal. Geom. 2 (1994) 35–52.

[89] _____, The Seiberg-Witten invariants and symplectic forms, Math. Res. Lett. 1 (1994) 809–822.

[90] _____, Floer theory for twisted circle bundles, Internat. Press, Cambridge, MA, to appear.

[91] A. Teleman, Non-abelian Seiberg-Witten theory and stable oriented pairs, Internat. J. Math. 8 (1997) 507–535; alg-geom/9609020.

[92] _____, Moduli spaces of PU(2) monopoles, dg-ga/9702006.

[93] _____, Untitled preprint.

[94] K. K. Uhlenbeck, Removable singularities in Yang-Mills fields, Comm. Math. Phys. 83 (1982) 11–29.

---

[95] _____, Connections with $L^p$ bounds on curvature, Comm. Math. Phys. 83 (1982) 31–42.

[96] _____, The Chern classes of Sobolev connections, Comm. Math. Phys. 101 (1985) 449–457.

[97] V. S. Varadarajan, Lie groups, Lie algebras, and their representations, Springer, New York, 1984.

[98] E. Witten, Monopoles and four-manifolds, Math. Res. Lett. 1 (1994) 769–796.

[99] H-J. Yang, Transition functions and a blow-up formula for Donaldson polynomials, Columbia University Thesis, 1992.

HARVARD UNIVERSITY
MICHIGAN STATE UNIVERSITY