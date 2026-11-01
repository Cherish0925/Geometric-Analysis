---
retention_scope: session
part: 4
total_parts: 6
---

[Part 4/6 of: PU(2) Monopoles. I: Regularity, Uhlenbeck Compactness, and Transversality]

Thus, $\|F_{A_r}\|_{L^2(B_{r_0})}$ tends to zero as $r_0 \to 0$, uniformly with respect to $r \in (0,r_0)$. Fix $r_0$ small enough so that $\|F_{A_r}\|_{L^2(B_{r_0})} < \varepsilon_1$ for all $r \in (0,r_0)$, where $\varepsilon_1$ is the constant of Theorem 3.13. Hence, there is a family of $C^\infty$ flat connections $\Gamma_r$, $r \in (0,r_0)$, on the SO(3) bundles $\mathfrak{su}(E_r)$ over $B_{r_0}$ such that

$$d_{\Gamma_r}^* (A_r - \Gamma_r) = 0 \quad \text{and} \quad \|A_r - \Gamma_r\|_{L^2_{1,\Gamma_r}(B_{r_0})} \leq c\|F_{A_r}\|_{L^2(B_{r_0})},$$

for a positive constant $c$ independent of $r \in (0,r_0)$, and a family of $C^\infty$ bundle isomorphisms $\tau_r : \mathfrak{su}(E_r)|_{B_{r_0}} \simeq B_{r_0} \times \mathfrak{su}(2)$ inducing $C^\infty$ bundle isomorphisms $\tau_r : E_r \simeq B_{r_0} \times \mathbb{C}^2$, via a choice of fixed $C^\infty$ trivialization $\det E_r|_{B_{r_0}} = \det E|_{B_{r_0}} \simeq B_{r_0} \times \mathbb{C}$.

Since $\|\Phi\|_{L^2_{1,A}(B)} < \infty$, then $\|\Phi\|_{L^2_{1,A}(B_{r_0})}$ and $\|\Phi\|_{L^4(B_{r_0})}$ tend to zero as $r_0$ as tends to zero. As $\Phi_r = \chi_r\Phi$ over $B(\frac{1}{2}r)$ and using (4.3), we have

$$\|\Phi_r\|_{L^2_{1,\Gamma_r}(B_{r_0})} \leq \|\Phi_r\|_{L^2(B_{r_0})} + \|\nabla_{\Gamma_r}\Phi_r\|_{L^2(B_{r_0})}$$

$$\leq \|\Phi_r\|_{L^2(B_{r_0})} + \left(\|A_r - \Gamma_r|\cdot \Phi_r\|_{L^2(B_{r_0})}\right)$$

$$+ \|\nabla_{A_r}\Phi_r\|_{L^2(B_{r_0})}$$

$$\leq c\left(1 + \left(\|A_r - \Gamma_r|\right)_{L^4(B_{r_0})}\right)\|\Phi_r\|_{L^4(B_{r_0})}$$

$$\leq c\|\Phi_r\|_{L^4(B_{r_0})} + \|\nabla_{A_r}(\chi_r\Phi)\|_{L^2(\Omega(\frac{1}{4}r,\frac{1}{2}r))}$$

$$+ \|\nabla_A\Phi\|_{L^2(\Omega(\frac{1}{2}r,r_0))}$$

$$\leq c\|\Phi_r\|_{L^2_{1,A}(B_{r_0})} + \|d\chi_r\cdot \Phi\|_{L^2(\Omega'(r))}$$

$$+ \|\chi_r\nabla_{A_r}\Phi\|_{L^2(\Omega'(r))}$$

---

$$\leq c \|\Phi\|_{L^2_{1,A}(B_{r_0})} + \|d\chi_r\|_{L^4(B_{r_0})}\|\Phi\|_{L^4(B_{r_0})}$$
$$
+ \|\nabla_A\Phi\|_{L^2(\Omega'(r))}
$$
$$
+ \|(\chi_r - 1)(A - \Gamma'_r)\cdot\Phi\|_{L^2(\Omega'(r))}
$$
$$
\leq c \|\Phi\|_{L^2_{1,A}(B_{r_0})} + \|A - \Gamma'_r\|_{L^4(\Omega'(r))}\|\Phi\|_{L^4(\Omega'(r))},
$$

using $A_r = \Gamma'_r + \chi_r(A - \Gamma'_r) = A + (\chi_r - 1)(A - \Gamma'_r)$ over $\Omega'(r)$, and so

(4.6) $$\|\Phi_r\|_{L^2_{1,\Gamma_r}(B_{r_0})} \leq c \|\Phi\|_{L^2_{1,A}(B_{r_0})},$$

for some constant $c$ independent of $r \in (0,r_0)$. Therefore, $$\|\Phi_r\|_{L^2_{1,\Gamma_r}(B_{r_0})}$$ tends to zero as $r_0 \to 0$, uniformly with respect to $r \in (0,r_0)$.

Hence, the estimates (4.4), (4.5), and (4.6) combine to give a uniform bound,

(4.7) $$\|(A_r - \Gamma_r, \Phi_r)\|_{L^2_{1,\Gamma_r}(B_{r_0})} \leq c\left(\|F_A\|_{L^2(B_{r_0})} + \|\Phi\|_{L^2_{1,A}(B_{r_0})}\right),$$

for some constant $c$ independent of $r \in (0,r_0)$. Note that

$$L^2_{1,\Gamma_r}(B_{r_0}, \Lambda^1 \otimes \mathfrak{su}(E_r)) \oplus L^2_{1,\Gamma_r}(B_{r_0}, W^+ \otimes E_r)$$
$$= L^2_{1,\Gamma}(B_{r_0}, \Lambda^1 \otimes \mathfrak{su}(2)) \oplus L^2_{1,\Gamma}(B_{r_0}, W^+ \otimes \mathbb{C}^2),$$

via the $C^\infty$ isomorphisms $\tau_r : E_r|_{B_{r_0}} \to B_{r_0} \times \mathbb{C}^2$, with

$$\|(A_r - \Gamma_r, \Phi_r)\|_{L^2_{1,\Gamma_r}(B_{r_0})} = \|(\tau_r(A_r) - \Gamma, \tau_r(\Phi_r))\|_{L^2_{1,\Gamma_r}(B_{r_0})},$$
$$d_\Gamma^*(\tau_r(A_r) - \Gamma) = 0.$$

By the weak compactness of the unit ball in the Hilbert space $L^2_{1}(B_{r_0})$, there is a sequence $r_\alpha \to 0$ such that the pairs $(A_{r_\alpha} - \Gamma_{r_\alpha}, \Phi_{r_\alpha})$ converge weakly in $L^2_{1}(B_{r_0})$ to a limit $(\tilde{A}, \tilde{\Phi})$ in $L^2_{1}(B_{r_0})$. For brevity, we denote $(A_r^\tau, \Phi_r^\tau) := (\tau_r(A_r), \tau_r(\Phi_r))$.

Claim 4.12. Continue the above notation. Then the following hold:

(1) After passing to a subsequence, the pairs $(A_{r_\alpha}^{\tau}, \Phi_{r_\alpha}^{\tau})$ converge in $C^\infty$ over compact subsets of $B_{r_0} \setminus \{0\}$ to $(\tilde{A}^{\tau}, \tilde{\Phi}^{\tau})$ and so $(\tilde{A}^{\tau}, \tilde{\Phi}^{\tau})$ is in $C^\infty$ over $B_{r_0} \setminus \{0\}$;

(2) The pair $(\tilde{A}^{\tau}, \tilde{\Phi}^{\tau})$ is an $L^2_{1}$ solution over $B_{r_0}$ to the elliptic system

$$\mathfrak{S}(\tilde{A}^{\tau}, \tilde{\Phi}^{\tau}) = 0 \quad \text{and} \quad d_\Gamma^*(\tilde{A}^{\tau} - \Gamma) = 0.$$

---

Proof. For any open subset $U \in B_{r_0} \setminus \{0\}$, the ball $B(\frac{1}{2} r)$ containing the support of the cutoff function $\chi_r$ does not meet $U$ when $r$ is sufficiently small and so $(A_r^\tau, \Phi_r^\tau)$ is a PU(2) monopole in $C^\infty$ over $U$ in Coulomb gauge with respect to $(\Gamma, 0)$ with uniformly $L^2$-small curvature. Hence, choosing $U' \in B_{r_0} \setminus \{0\}$ so that $U' \supseteq U$, Proposition 3.12 implies that for any integer $k \geq 1$ and $r$ small enough that $B(\frac{1}{2} r) \cap U' = \emptyset$, we have uniform bounds

$$\|(A_r^\tau - \Gamma, \Phi_r^\tau)\|_{L^2_k,\Gamma}(U) \leq C\left(\|(A_r^\tau - \Gamma, \Phi_r^\tau)\|_{L^2(U')} + \|F(A_r^\tau)\|_{L^2(U')}\right)
\leq C\left(\|\Phi\|_{L^4(B)} + \|F_A\|_{L^2(B)}\right) < \infty,

for some constant $C(g,k,U)$ independent of $r \in (0,r_0)$. Therefore, by passing to a subsequence, the pairs $(A_r_\alpha^\tau, \Phi_r_\alpha^\tau)$ converge in $C^\infty$ over compact subsets of $B_{r_0} \setminus \{0\}$ to a $C^\infty$ pair $(A^\tau, \tilde{\Phi}^{\tau})$ over $B_{r_0} \setminus \{0\}$ as $r_\alpha \to 0$. But for any $U \in B_{r_0} \setminus \{0\}$ and small enough $r \in (0,r_0)$, we have $\mathfrak{S}(A_r^\tau, \Phi_r^\tau) = \mathfrak{S}(A_r, \Phi_r) = 0$ over $U$, and so

$$\mathfrak{S}(\tilde{\Lambda}^{\tau}, \tilde{\Phi}^{\tau}) = \lim_{\alpha \to \infty} \mathfrak{S}(A_r_\alpha^\tau, \Phi_r_\alpha^\tau) = 0 \text{ over } U.

Hence, $\mathfrak{S}(\tilde{\Lambda}^{\tau}, \tilde{\Phi}^{\tau}) = 0$ over $B_{r_0} \setminus \{0\}$ and so $(\tilde{\Lambda}^{\tau}, \tilde{\Phi}^{\tau})$ is a PU(2) monopole in $C^\infty$ over $B_{r_0} \setminus \{0\}$. This proves Assertion (1) of the claim.

Since $(\tilde{\Lambda}^{\tau}, \tilde{\Phi}^{\tau})$ is a $C^\infty$ monopole over $B_{r_0} \setminus \{0\}$, then $\mathfrak{S}(\tilde{\Lambda}^{\tau}, \tilde{\Phi}^{\tau}) = 0$ a.e. over $B_{r_0}$ and so $(\tilde{\Lambda}^{\tau}, \tilde{\Phi}^{\tau})$ is an $L^2_1$ monopole over $B_{r_0}$. Let $W_0^{2,1}(B_{r_0}) \subset L^2_1(B_{r_0})$ be the closure in $L^2_1(B_{r_0})$ of the pairs

$$C_0^\infty(B_{r_0}, \Lambda^1 \otimes \mathfrak{su}(E)) \oplus C_0^\infty(B_{r_0}, W^+ \otimes E)

with compact support in the open ball $B_{r_0}$. Then, for any $(b, \varphi) \in W_0^{2,1}(B_{r_0})$ we have

$$(b, d_\Gamma^*(\tilde{\Lambda}^{\tau} - \Gamma))_{L^2(B_{r_0})} = (d_\Gamma b, \tilde{\Lambda}^{\tau} - \Gamma)_{L^2(B_{r_0})}
= \lim_{\alpha \to \infty}(d_\Gamma b, (A_r_\alpha^\tau - \Gamma))_{L^2(B_{r_0})}
= \lim_{\alpha \to \infty}(b, d_\Gamma^*(A_r_\alpha^\tau - \Gamma))_{L^2(B_{r_0})} = 0,

and so $d_\Gamma^*(\tilde{\Lambda}^{\tau} - \Gamma) = 0$, as required. This completes the proof of the claim. q.e.d.

By Claim 4.12, the pair $(\tilde{\Lambda}^{\tau}, \tilde{\Phi}^{\tau})$ is an $L^2_1$ monopole over $B_{r_0}$ in Coulomb gauge relative to $(\Gamma, 0)$. From the estimate (4.7) and the

---

Sobolev embedding $L_1^2(B_{r_0}) \subset L^4(B_{r_0})$, we can ensure that for sufficiently small $r_0$,

$$\|(A_r^\tau - \Gamma, \Phi_r^\tau)\|_{L^4(B_{r_0})} < \varepsilon_2,$$

for all $r \in (0,r_0)$ and so $\|(\tilde{A}_r^\tau, \tilde{\Phi}_r^\tau)\|_{L^4(B_{r_0})} < \varepsilon_2$, where $\varepsilon_2$ is the constant of Proposition 3.12 and therefore, $(\tilde{A}_r^\tau, \tilde{\Phi}_r^\tau)$ is a $C^\infty$ monopole over $B_{r_0}$. (As usual this means, more precisely, that there is a $C^\infty$ monopole over $B_{r_0}$ which coincides with $(\tilde{A}_r^\tau, \tilde{\Phi}_r^\tau)$ over $B_{r_0}$ except over a subset of measure zero; since $(\tilde{A}_r^\tau, \tilde{\Phi}_r^\tau)$ is already $C^\infty$ on the punctured ball $B_{r_0} \setminus \{0\}$, this $C^\infty$ monopole is equal to $(\tilde{A}_r^\tau, \tilde{\Phi}_r^\tau)$ except possibly at the origin.)

Finally, the $C^\infty$ bundle isomorphisms $\tau_r : \mathfrak{su}(E_r)|_{B_{r_0}} \simeq B_{r_0} \times \mathfrak{su}(2)$ may be viewed as SU(2) automorphisms acting on the SO(3) bundle $B_{r_0} \times \mathfrak{su}(2)$ by initially choosing a fixed $C^\infty$ trivialization

$$E|_{B \setminus \{0\}} \simeq B \setminus \{0\} \times \mathbb{C}^2,$$ with $\mathfrak{su}(E)|_{B \setminus \{0\}} \simeq B \setminus \{0\} \times \mathfrak{su}(2).$$

Then Lemma 2.7 implies, after passing to a subsequence, that the sequence of SU(2) automorphisms $\tau_{r_\alpha}$ converges in $C^\infty$ over compact subsets of $B_{r_0} \setminus \{0\}$ to a $C^\infty$ limit $\sigma$ over $B_{r_0} \setminus \{0\}$. Then $(\tilde{A}_r^\tau, \tilde{\Phi}_r^\tau) = (A^\sigma, \Phi^\sigma)$ over the punctured ball $B_{r_0} \setminus \{0\}$, while $(\tilde{A}_r^\tau, \tilde{\Phi}_r^\tau)$ is smooth over $B_{r_0}$. Thus, the finite-energy $C^\infty$ monopole $(A, \Phi)$ over the punctured ball $B_{r_0} \setminus \{0\}$ is equivalent via a $C^\infty$, determinant-one, unitary bundle isomorphism to $(\tilde{A}_r^\tau, \tilde{\Phi}_r^\tau)$ over $B_{r_0} \setminus \{0\}$, where $(\tilde{A}_r^\tau, \tilde{\Phi}_r^\tau)$ is a $C^\infty$ monopole over $B_{r_0}$. This completes the proof of the theorem. q.e.d.

Remark 4.13. The proof of Theorem 4.10 does not imply, of course, that the section $\tilde{\Phi}_r^\tau$ is zero at the center of the ball $B$. Even though the $C^\infty$ sections $\Phi_{r_\alpha}^{\tau}$ are zero at the center, the subsequence only converges in $L_1^2(B_{r_0})$ over $B_{r_0}$ to a limit $\tilde{\Phi}_r^\tau$. Similarly, while Lemma 4.4 provides a uniform $C^0$ bound for the sections $\Phi_{r_\alpha}^{\tau}$ over $B_{r_0}$, we would need a uniform, $C^{0,\nu}$ Hölder bound, for some $\nu \in (0,1)$, in order to extract a convergent subsequence.

4.4. Patching arguments. The standard proof of the compactness theorem for the moduli space of anti-self-dual connections employs a patching argument for gauge transformations to obtain $C^\infty$ convergence (modulo gauge transformations) on compact subsets of $X \setminus \{x_1, \ldots, x_m\}$ for a sequence of anti-self-dual connections $A_\alpha$ on a Hermitian bundle $E$ over $X$. The gauge transformations that require patching are obtained by repeated application of Corollary 2.3.9 in [20]

---

to geodesic balls where the $L^2$ norm of the curvature $F_{A_\alpha}$ is less than $\varepsilon$: since the $L^2$ norm of the curvature is scale invariant, these possibly small balls may be rescaled to standard size with metrics which are approximately Euclidean as in [20, Corollary 2.3.9].

Throughout this subsection, $(A_\alpha, \Phi_\alpha)$ will denote a sequence of $C^\infty$ pairs (not necessarily PU(2) monopoles) on $(\mathfrak{su}(E), W^+ \otimes E)$ over $\Omega$ and $u_\alpha$ will denote a sequence of $C^\infty$ determinant-one, unitary automorphisms of a Hermitian bundle $E$ (that is, gauge transformations in $\mathcal{G}_E$ and not $^\circ\mathcal{G}_E$), where $\Omega$ is an oriented, Riemannian four-manifold with spin$^c$ structure $(\rho, W)$. Convergence will mean convergence in $C^\infty$ on compact subsets which, as usual, can be replaced by $L_{k+1,\text{loc}}^2$ convergence of $L_k^2$ pairs $(A_\alpha, \Phi_\alpha)$ provided $k \geq 2$.

The following four patching results follow almost immediately from the proofs of Lemmas 4.4.5–4.4.7 and Corollary 4.4.8 in [20] (where the sequence of connections $A_\alpha$ is not assumed to be anti-self-dual). Their proofs are omitted and instead we refer the reader to [20] or [95] for a detailed account; patching arguments of this type are used by Uhlenbeck in her proof of Theorem 3.6 [95], where the connections (not necessarily anti-self-dual or Yang-Mills) are just assumed to be in $L_1^p$ and the gauge transformations are in $L_2^p$ with $p > 2$.

**Lemma 4.14.** Suppose that $(A_\alpha, \Phi_\alpha)$ is a sequence of pairs on $(\mathfrak{su}(E), W^+ \otimes E)$ over a base manifold $\Omega$ (possibly non-compact), and let $\tilde{\Omega} \in \Omega$ be an interior domain. Suppose that there are gauge transformations $u_\alpha \in \mathcal{G}_E$ and $\tilde{u}_\alpha \in \mathcal{G}_{E|\tilde{\Omega}}$ such that $u_\alpha(A_\alpha, \Phi_\alpha)$ converges over $\Omega$ and $\tilde{u}_\alpha(A_\alpha, \Phi_\alpha)$ converges over $\tilde{\Omega}$. Then for any compact set $K \in \tilde{\Omega}$ there are a subsequence $\{\alpha'\} \subset \{\alpha\}$ and gauge transformations $w_{\alpha'} \in \mathcal{G}_E$ such that $w_{\alpha'} = \tilde{u}_{\alpha'}$ on a neighborhood of $K$ and the pairs $w_{\alpha'}(A_{\alpha'}, \Phi_{\alpha'})$ converge over $\Omega$.

We have the following two extensions of this result.

**Lemma 4.15.** Let $\Omega$ be exhausted by an increasing sequence of precompact open subsets $U_1 \in U_2 \in \cdots \in \Omega$ with $\cup_n U_n = \Omega$. Suppose $(A_\alpha, \Phi_\alpha)$ is a sequence of pairs on $(\mathfrak{su}(E), W^+ \otimes E)$ over $\Omega$ and that for each $n$ there are a subsequence $\{\alpha'\} \subset \{\alpha\}$ and gauge transformations $u_{\alpha'} \in \mathcal{G}_{E|U_n}$ such that $u_{\alpha'}(A_{\alpha'}, \Phi_{\alpha'})$ converges over $U_n$. Then there are a subsequence $\{\alpha''\} \subset \{\alpha\}$ and gauge transformations $u_{\alpha''} \in \mathcal{G}_E$ such that $u_{\alpha''}(A_{\alpha''}, \Phi_{\alpha''})$ converges over $\Omega$.

**Lemma 4.16.** Suppose that $\Omega = \Omega_1 \cup \Omega_2$ and that $(A_\alpha, \Phi_\alpha)$ is a sequence of pairs on $(\mathfrak{su}(E), W^+ \otimes E)$ over $\Omega$. If there are sequences of gauge transformations $v_{\alpha} \in \mathcal{G}_{E|\Omega_1}$ and $w_{\alpha} \in \mathcal{G}_{E|\Omega_2}$ such that $v_{\alpha}(A_{\alpha}, \Phi_{\alpha})$ converges over $\Omega_1$ and $w_{\alpha}(A_{\alpha}, \Phi_{\alpha})$ converges over $\Omega_2$, then there are a subsequence $\{\alpha'\} \subset \{\alpha\}$ and gauge transformations $u_{\alpha'} \in \mathcal{G}_E$ such that the pairs $u_{\alpha'}(A_{\alpha'}, \Phi_{\alpha'})$ converge over $\Omega$.

Lemmas 4.14, 4.15, and 4.16 combine to yield the following analogue of Corollary 4.4.8 in [20].

Corollary 4.17. Suppose that $(A_{\alpha}, \Phi_{\alpha})$ is a sequence of pairs on $(\mathfrak{su}(E), W^+ \otimes E)$ over $\Omega$ such that the following holds. For each point $x \in \Omega$ there are a neighborhood $D$ of $x$, a subsequence $\{\alpha'\} \subset \{\alpha\}$, and gauge transformations $v_{\alpha'} \in \mathcal{G}_{E|D}$ such that the pairs $v_{\alpha'}(A_{\alpha'}, \Phi_{\alpha'})$ converge over $D$. Then there are a single subsequence $\{\alpha''\} \subset \{\alpha\}$, and gauge transformations $u_{\alpha''} \in \mathcal{G}_E$ such that the pairs $u_{\alpha''}(A_{\alpha''}, \Phi_{\alpha''})$ converge over $\Omega$.

We now assume that $(A_{\alpha}, \Phi_{\alpha})$ is a sequence of PU(2) monopoles on $(\mathfrak{su}(E), W^+ \otimes E)$ over $\Omega$ and obtain the required convergence from our local elliptic estimates for PU(2) monopoles and Uhlenbeck’s gauge-fixing theorem. The following result is the analogue of Proposition 4.4.9 in [20], which applies to a sequence of anti-self-dual connections.

Proposition 4.18. Let $Y$ be an oriented four-manifold with Riemannian metric $g$ and spinc structure $(\rho, W)$. Suppose that $(A_{\alpha}, \Phi_{\alpha})$ is a sequence of PU(2) monopoles, on the bundles $(\mathfrak{su}(E), W^+ \otimes E)$ over $Y$, with the following property. For each point $y \in Y$ there is a geodesic ball $B_g(y, r_y)$ with center $y$, radius $r_y$, and index $\alpha_y$ such that

$$\|F_{A_\alpha}\|_{L^2(B_g(y, r_y))} < \varepsilon_0, \quad \alpha \geq \alpha_y,

where $\varepsilon_0(g, A_{\det W^+}, A_{\det E})$ is the constant of Corollary 3.16. Then there are a subsequence $\{\alpha''\} \subset \{\alpha\}$ and a sequence of $C^\infty$ gauge transformations $u_{\alpha''} \in \mathcal{G}_E$ such that $u_{\alpha''}(A_{\alpha''}, \Phi_{\alpha''})$ converges in $C^\infty$ on compact subsets over $Y$.

Proof. Fix a point $y \in Y$. If $B_g(y, r_y)$ is a geodesic ball with center $y$ and $g$-radius $r_y$, then $B_{gr}(y, 1)$ is a geodesic ball with center $y$ and $g_r$-radius one, where $g_r = r_y^{-2} g$. Thus, $(A_{\alpha}, r_y^{-1}\Phi_{\alpha})$ is sequence of PU(2) monopoles over $B_{gr}(y, 1)$ such that

$$\|F_{A_\alpha}\|_{L^2(B_{gr}(y, 1))} < \varepsilon_0, \quad \alpha \geq \alpha_y.

Corollary 3.16 implies that there are a subsequence $\{\alpha'\} \subset \{\alpha\}$ and a sequence of gauge transformations $\{u_{\alpha'\}}\$ over $B_{gr}(y, 1)$ such that the sequence $u_{\alpha'} (A_{\alpha',} r_y^{-1}\Phi_{\alpha'})$ converges over $B_{gr}(y, \frac{1}{2})$.

---

Therefore, for each point $y \in Y$, we have a sequence of gauge transformations $\{u_{\alpha'}\}$ over $B_g(y,r_y)$ such that the sequence $u_{\alpha'} (A_{\alpha'},\Phi_{\alpha'})$ converges over $B_g(y,\frac{1}{2}r_y)$. The conclusion now follows from Corollary 4.17. q.e.d.

4.5. Definition of the Uhlenbeck closure. The definition of the Uhlenbeck closure of the moduli space of solutions to the perturbed PU(2) monopole equations (2.27) is slightly more involved than that of the unperturbed PU(2) monopole equations (2.15). For this reason it is convenient to define the Uhlenbeck closure in the unperturbed case before considering the general case.

4.5.1. Definition of the Uhlenbeck closure for the moduli space of unperturbed PU(2) monopoles. Let $M_{W,E}$ (temporarily) denote the moduli space of gauge-equivalence classes of solutions $(A,\Phi)$ on $(\mathfrak{su}(E),W^+ \otimes E)$ to the unperturbed PU(2) monopole equations (2.15). We define the Uhlenbeck closure $\bar{M}_{W,E}$ of the moduli space $M_{W,E}$ by analogy with the definition of the Uhlenbeck closure of the moduli space of anti-self-dual connections [20, §4.4]. The moduli set IM_{W,E}$ of unperturbed ideal PU(2) monopoles on $(\mathfrak{su}(E),W^+ \otimes E)$ is given by

$$IM_{W,E} := \bigcup_{\ell=0}^{N} M_{W,E-\ell} \times \text{Sym}^{\ell}(X),$$

where $N \geq N_p$, $N_p$ is the constant defined in equation (4.15), $E_{-\ell}$ denotes a Hermitian two-plane bundle with det $E_{-\ell} = \det E$, and $c_2(E_{-\ell}) = c_2(E) - \ell$, for $\ell \geq 0$.

Definition 4.19. Suppose that $[A_\alpha, \Phi_\alpha, y_\alpha]$ is a sequence of points in IM_{W,E}$ and that $[A_0, \Phi_0, x]$ is a point in IM_{W,E}$, where $(A_\alpha, \Phi_\alpha)$ and $(A_0, \Phi_0)$ are monopoles on $(\mathfrak{su}(E_\alpha), W^+ \otimes E_\alpha)$ and $(\mathfrak{su}(E_0), W^+ \otimes E_0)$ over $X$, respectively, with det $E_\alpha = \det E_0 = \det E$ and $c_2(E_\alpha), c_2(E_0) \leq c_2(E)$. Then the sequence of points $[A_\alpha, \Phi_\alpha, y_\alpha]$ converges to $[A_0, \Phi_0, x]$ (or, the sequence of triples $(A_\alpha, \Phi_\alpha, y_\alpha)$ converges weakly to $(A_0, \Phi_0, x)$ if the following hold:

• There is a sequence of $L_{k+1,\text{loc}}^2$ determinant-one, unitary bundle isomorphisms $u_\alpha : E_\alpha|_{X \backslash x} \rightarrow E_0|_{X \backslash x}$ such that the sequence of PU(2) monopoles $u_\alpha(A_\alpha, \Phi_\alpha)$ converges to $(A_0, \Phi_0)$ in $L_{k,\text{loc}}^2$ over $X \backslash x$.

• The sequence $|F_{A_\alpha}|^2 + 8\pi^2 \sum_{y \in y_\alpha} \delta(y)$ converges in the weak-$*$ topology on measures to $|F_{A_0}|^2 + 8\pi^2 \sum_{x \in x} \delta(x).$

---

• We have $c_2(E) = c_2(E_0) + |\mathbf{x}|$.

Give IM$_{W,E}$ the Uhlenbeck topology specified by Definition 4.19 and let $\bar{M}_{W,E} \subset IM_{W,E}$ be the closure of $M_{W,E}$ in IM$_{W,E}$. The topological space IM$_{W,E}$ is second-countable and Hausdorff.

4.5.2. Definition of the Uhlenbeck closure for the moduli space of perturbed PU(2) monopoles. The basic idea underlying the choice of holonomy perturbations described in §2.5.2 is a generalization of an earlier construction due to S. K. Donaldson for the moduli spaces of solutions to the ‘extended anti-self-dual equations’, to which the Freed-Uhlenbeck generic metrics theorem does not apply [18, §IV(v), pp. 282–286]. As in the case of the moduli space of anti-self-dual connections, we shall see in §4.6 that there is an upper bound M (which is determined by g, $A_{\det W+}$, $A_{\det E}$, and $p_1(\mathfrak{su}(E))$) on the total energy $\|F_A\|^2_{L^2(X)}$ for any solution $(A, \Phi)$ to the perturbed PU(2) monopole equations (2.27) and so an upper bound $2M/\varepsilon_0^2$ on the number of disjoint balls $B(x_j, 4R_0)$ with energy greater than or equal to $\frac{1}{2}\varepsilon_0^2$. Hence, if $N_b \geq 2M/\varepsilon_0^2 + 1$, at least one ball $B(x_j, 4R_0)$ in the collection $\{B(x_j, 4R_0)\}_{j=1}^N_b$ has energy less than $\frac{1}{2}\varepsilon_0^2$.

Suppose $(A_\alpha, \Phi_\alpha)$ is a sequence of PU(2) monopoles which converges to an ideal PU(2) monopole $(A_0, \Phi_0, \mathbf{x})$ in $\tilde{C}_{W,E-\ell} \times \text{Sym}^{\ell}(X)$. If a point $x \in \mathbf{x}$ lies in a ball $B(x_j, 2R_0)$, the corresponding sections $\mathfrak{m}_{j,l,\beta}(A_\alpha)$ supported on $\bar{B}(x_j, R_0)$ converge to zero (by construction) for all $l, \beta$. Thus, the solution $(A_0, \Phi_0)$ will satisfy a version of the PU(2) monopole equations (2.27) with the perturbations supported on $\bar{B}(x_j, R_0)$ omitted. (In the situation considered by Donaldson, ideal extended anti-self-dual connections also satisfy a family of equations [18, Eq. (4.37)] which depend on the bubble points in $X$.) Therefore, the ideal limit $[A_0, \Phi_0, \mathbf{x}]$ is a point in the fiber $M_{W,E-\ell}|_{\mathbf{x}}$ over a point $\mathbf{x}$ in the base Sym$\ell$(X). Here, $M_{W,E-\ell}|_{\mathbf{x}}$ is simply the moduli space of solutions to the perturbed monopole equations (2.27) with the connection energy cutoff functions $\beta_j[A]$ of (2.18) (used in the definition of the perturbing sections $\mathfrak{m}_{j,l,\beta}(A)$ of (2.20)) replaced by cutoff functions

(4.8)
$$\beta_j[A_0, \mathbf{x}]$$
$$\therefore \beta\left(\frac{1}{\varepsilon_0^2} \int_{B(x_j, 4R_0)} \beta\left(\frac{\text{dist}_g(\cdot, x_j)}{4R_0}\right)\left(|F_A_0|^2 + 8\pi^2 \sum_{x \in \mathbf{x}}\delta(x)\right) dV\right),$$ where $ \varepsilon_{0} $ is the constant of Corollary 3.16. Then $ M_{W,E-\ell} $ is the moduli space of triples ($ A_{0}, \Phi_{0}, \mathbf{x} $) solving the ‘lower-level’ PU(2) monopole equations

$$F_{A}^{+} - \left( \mathrm{id} + \tau_{0} \otimes \mathrm{id}_{5u(E)} + \vec{\tau} \cdot \vec{\mathfrak{m}} (A, \mathbf{x}) \right) \rho^{-1} (\Phi \otimes \Phi^{*})_{00} = 0,$$
$$D_{A} \Phi + \rho(\vartheta_{0}) \Phi + \vec{\vartheta} \cdot \vec{\mathfrak{m}} (A, \mathbf{x}) \Phi = 0.$$

In the more familiar case of the Uhlenbeck compactification of the moduli space of solutions to the unperturbed PU(2) monopole equations (2.15), the spaces $ M_{W,E-\ell} $ above would be replaced by the products $ M_{W,E-\ell} \times \operatorname{Sym}^{\ell}(X). $

The definition of the Uhlenbeck topology for the moduli space of solutions to the perturbed PU(2) monopole equations (2.27) is almost identical to that of the unperturbed case. The only difference is in the definition of the set of ideal solutions to (2.27). In the presence of holonomy perturbations, the Uhlenbeck closure $ \bar{M}_{W,E} $ is therefore defined to be the closure of $ M_{W,E} $ in

$$I M_{W,E} := \bigcup_{\ell=0}^{N} M_{W,E-\ell} \subset \bigcup_{\ell=0}^{N} C_{W,E-\ell} \times \operatorname{Sym}^{\ell}(X),$$

where $ M_{W,E-0} := M_{W,E} $ , while $ N \geq N_{p} $ and $ N_{p} $ is the constant defined in equation (4.15).

4.6. Sequential compactness. In this section we apply our elliptic regularity and removable singularity results to prove our main compactness result, namely Theorem 1.1, which asserts the existence of an Uhlenbeck compactification for the moduli space of PU(2) monopoles, analogous to that given by Theorem 4.4.3 [20] in the case of the moduli space of anti-self-dual connections.

As in [20], the proof of Theorem 1.1 follows by an entirely routine argument (which we leave to the reader) from the special case below which is an analogue of similar compactness results for anti-self-dual connections; see, for example, [20, Theorem 4.4.4], [31, Theorem 3.2], [30, Chapter 8], [78, Theorem 3.1], [83, Proposition 4.4], and [84, Proposition 5.1].

Theorem 4.20. Let $ X $ be a closed, oriented, smooth four-manifold with $ C^{\infty} $ Riemannian metric, spin$^{c}$ structure ($ \rho, W $ ) with spin$^{c}$ connection, and a Hermitian two-plane bundle $ E $ with unitary connection on det $ E $ . Then there is a positive integer $ N_{p} $ , depending at most on the curvatures of the fixed connections on $W$ and det $E$ together with $c_2(E)$, such that for all $N \geq N_p$, any infinite sequence in $M_{W,E}$ has a weakly convergent subsequence, with limit point in $\cup_{\ell=0}^{N} M_{W,E-\ell}$.

Proof. The basic argument follows that of [20, pp. 163–165] and [83, Proposition 4.4] for the moduli space of anti-self-dual connections. Let $[A_\alpha, \Phi_\alpha]$ be a sequence of points in $M_{W,E}$ and let $(A_\alpha, \Phi_\alpha)$ be a corresponding sequence of PU(2) monopoles in $C^\infty$ on $(E, W^+ \otimes E)$. By passing to a subsequence we can assume that the sequence of positive measures $\mu_\alpha := |F_{A_\alpha}|^2$ on $X$ converges to a measure $\mu_\infty$ on $X$ in the weak-<sup>*</sup> topology on measures, so

$$\lim_{\alpha \to \infty} \int_X |F_{A_\alpha}|^2 dV = \int_X \mu_\infty =: M_\infty \leq K,$$

where $K < \infty$ is the constant in our universal energy bound (4.2) for a PU(2) monopole over $X$. Hence there are at most $M_\infty/\varepsilon_0^2$ distinct points in $X$, labelled $\{x_1, \ldots, x_m\}$, which do not lie in a geodesic ball $B(x,r)$ of $\mu_\infty$-measure less than $\varepsilon_0^2$, where $\varepsilon_0$ is the constant of Proposition 4.18 and which appears in (2.18) and (4.8). Thus, for any $r > 0$, we have

$$\lim_{\alpha \to \infty} \int_B(x_i,r) |F_{A_\alpha}|^2 dV = \int_B(x_i,r) \mu_\infty \geq \varepsilon_0^2, \quad i = 1, \ldots, m,$$

and so we may define real numbers $\kappa_i \geq \varepsilon_0^2/8\pi^2$ by setting

$$\kappa_i := \lim_{r \to 0} \lim_{\alpha \to \infty} \frac{1}{8\pi^2} \int_B(x_i,r) |F_{A_\alpha}|^2 dV = \lim_{r \to 0} \frac{1}{8\pi^2} \int_B(x_i,r) \mu_\infty.$$

We may suppose, without loss of generality, that $m \geq 1$. If a point $x_i$ lies in a ball $\bar{B}(x_j, 2R_0)$ then the holonomy perturbation sections are zero over $B(x_j, R_0)$ since $8\pi^2\kappa_i \geq \frac{1}{2}\varepsilon_0^2$. Hence, the points $\{x_1, \ldots, x_m\}$ are contained in a large open subset of $X$ where $(\vec{\tau}, \vec{\vartheta}) = 0$.

By passing to a subsequence, Proposition 4.18 supplies determinant-one, unitary gauge transformations $u_\alpha$ over $X \setminus \{x_1, \ldots, x_m\}$ such that the sequence $u_\alpha(A_\alpha, \Phi_\alpha)$ converges over $X \setminus \{x_1, \ldots, x_m\}$ to a pair $(A_0, \Phi_0)$ on $(\mathfrak{su}(E), W^+ \otimes E)|_X \setminus \{x_1, \ldots, x_m\}$, such that the triple $(A_0, \Phi_0, \mathbf{x})$ solves the lower-level PU(2) monopole equations (4.9). Plainly,

$$\int_X \{x_1, \ldots, x_m\} \left(|F_{A_0}|^2 + |\Phi_0|^4 + |\nabla_A_0\Phi_0|^2\right) dV \leq K < \infty.$$

---

By the removability of point singularities for finite-energy PU(2) monopoles (Theorem 4.10), there are a Hermitian two-plane bundle $E_0$ with $\det E_0 = \det E$ over $X$, a PU(2) monopole $(\tilde{A}_0, \tilde{\Phi}_0)$ on $(\mathfrak{su}(E_0), W^+ \otimes E_0)$, and a determinant-one, unitary bundle isomorphism $u_0$ from $E|_{X \setminus \{x_1, \ldots, x_m\}}$ to $E_0|_{X \setminus \{x_1, \ldots, x_m\}}$ such that $u_0(A_0, \Phi_0) = (\tilde{A}_0, \tilde{\Phi}_0)$ over $X \setminus \{x_1, \ldots, x_m\}$.

The limiting measure $\mu_\infty$ has the form

$$\mu_\infty = |F_A_0|^2 + 8\pi^2 \sum_{i=1}^{m} \kappa_i \delta_x_i,$$

where the $\delta_x_i$ have unit mass concentrated at the points $x_i$. It remains to show that the $\kappa_i$ are positive integers. For this purpose we use an argument similar to that used to prove Lemma 3.8 in [31] (due to Taubes) which fits better with our later development of the gluing theory for PU(2) monopoles, though one could also use the Chern-Simons functional for this purpose as in [20, p. 164]. The proof of Theorem 3.2 in [31] is a modification of an earlier compactness result, Proposition 4.4 in [83], for connections with $L^2$ bounded curvature but which are only approximately anti-self-dual in a suitable sense. Theorem 4.20 follows easily from the next lemma:

**Lemma 4.21.** The bundle $E_0$ has Chern classes $c_1(E_0) = c_1(E)$ and $c_2(E_0) = c_2(E) - \ell$, where $\ell = \sum_{i=1}^{m} \kappa_i$ and the constants $\kappa_i$ are positive integers for $i = 1, \ldots, m$.

**Proof.** The equality of the first Chern classes follows from the remarks in the preceding paragraph. The proof that each $\kappa_i$ is an integer requires a brief digression in order to discuss the limiting behavior of the connections $A_\alpha$ near the points $x_i \in X$.

Fix an index $i \in \{1, \ldots, m\}$, let $\varrho$ be the injectivity radius of $(X, g)$, and fix a constant $\delta \in (0, \frac{1}{4}\varrho)$. Choose an orthogonal frame for $\mathfrak{su}(E_0)|_{x_i}$, use parallel translation via the connection $A_0$ along radial geodesics from $x_i \in X$ to trivialize $\mathfrak{su}(E_0)$ over the ball $B(x_i, \varrho)$, and let $w_{0,i} : \mathfrak{su}(E_0)|_{B(x_i, \varrho)} \rightarrow B(x_i, \varrho) \times \mathfrak{su}(2)$ be the resulting smooth bundle map. We have $\|F_A_0\|_{L^\infty(X)} \leq C$, for some positive constant $C$, and so

$$\|F_A_0\|_{L^2(B(x_i, \delta))} \leq C\delta^2.$$

Thus, we may suppose that $\delta$ is fixed small enough so that Theorem 3.13 provides an SU(2) gauge transformation $v_{0,i}$ of $B(x_i, \delta) \times \mathfrak{su}(2)$ such that

$$\|a_{0,i}\|_{L^4(B(x_i, \delta))} + \|\nabla_\Gamma a_{0,i}\|_{L^2(B(x_i, \delta))} \leq c\|F_A_0\|_{L^2(B(x_i, 2\delta))},$$ where $a_{0,i} := u_{0,i}(A_0) - \Gamma \in \Omega^1(B(x_i, \delta), \mathfrak{su}(2))$ and $u_{0,i} := v_{0,i} \circ w_{0,i}$, and $\Gamma$ is the product connection on $B(x_i, \delta) \times \mathfrak{su}(2)$. The sequence of connections $u_\alpha(A_\alpha)$ converges in $C^\infty$ on compact subsets of the punctured balls $B(x_i, \delta)\{x_i\}$ to the $C^\infty$ connection $A_0$ on $\mathfrak{su}(E_0)|_{B(x_i, \delta)\{x_i\}}$; therefore, the sequence of connections $u_{0,i}u_\alpha(A_\alpha)$ converges in $C^\infty$ on compact subsets of the punctured balls $B(x_i, \delta)\{x_i\}$ to the $C^\infty$ connection $u_{0,i}(A_0)$ on $B(x_i, \delta)\{x_i\} \times \mathfrak{su}(2)$.

Write $u_{0,i}u_\alpha(A_\alpha) = \Gamma + a_{i,\alpha}$ over $B(x_i, \delta)\{x_i\}$, where $a_{i,\alpha} \in \Omega^1(B(x_i, \delta)\{x_i\}, \mathfrak{su}(2))$. Let $\Omega(x_i; \frac{1}{2}r, 2r)$ denote the open annulus $\{x \in X : \frac{1}{2}r < \text{dist}_g(x,x_i) < 2r\}$ in $X$. Then, for any $r \in (0, \frac{1}{2}\delta)$, there is an index $\alpha_0(r)$ such that

$$\int_{\Omega(x_i, \frac{1}{2}r, 2r)} \left(|a_{i,\alpha}-a_{0,i}|^4 + |\nabla_\Gamma(a_{i,\alpha}-a_{0,i})|^2\right) dV < r^4, \quad \alpha \geq \alpha_0.$$

Since $\|F_A_0\|_{L^\infty(X)} \leq C$, we have

(4.10) $$\int_{B(x_i, 2r)} \left(|a_{0,i}|^4 + |\nabla_\Gamma a_{0,i}|^2\right) dV \leq c \int_{B(x_i, 2r)} |F_A_0|^2 dV \leq Cr^4,$$

and therefore

(4.11) $$\int_{\Omega(x_i, \frac{1}{2}r, 2r)} \left(|a_{i,\alpha}|^4 + |\nabla_\Gamma a_{i,\alpha}|^2\right) dV \leq Cr^4, \quad \alpha \geq \alpha_0.$$

Let $\chi : \mathbb{R} \rightarrow [0,1]$ be a bump function such that $\chi(t) = 0$ for $t \leq \frac{1}{2}$ and $\chi(t) = 1$ for $t \geq 2$. Define a cutoff function $\chi_{i,r}: X \rightarrow [0,1]$ by setting $\chi_{i,r}(x) = 1 - \chi(\text{dist}_g(x,x_i)/r)$ so that $\chi_{i,r} = 1$ on $B(x_i, \frac{1}{2}r)$ and $\chi_{i,r} = 0$ on $X-B(x_i, 2r)$. Fix a Riemannian metric $g_i$ on $S^4$ which coincides with $g$ on $B(x_i, \delta) = B(n, \delta)$ (after identifying the point $x_i \in X$ with the north pole $n \in S^4$) and extends $g$ outside $B(x_i, 2\delta) = B(n, 2\delta)$ to a smooth metric on $S^4$. Define a sequence of SO(3) bundles $V_{i,r,\alpha}$ over $S^4$ by setting

$$V_{i,r,\alpha} := \begin{cases} \mathfrak{su}(E) & \text{over } B(n, 2r), \\ S^4 \setminus \{n\} \times \mathfrak{su}(2) & \text{over } S^4 \setminus \{n\}, \end{cases}$$

where the identification of the SO(3) bundles $\mathfrak{su}(E)$ and $S^4 \setminus \{n\} \times \mathfrak{su}(2)$ over the annulus $B(n, 2r) \setminus \{n\} = B(x_i, 2r) \setminus \{x_i\}$ is induced from the the SO(3) bundle isomorphism

$$u_{0,i} \circ u_\alpha : \mathfrak{su}(E)|_{B(n, 2r)\setminus \{n\}} \rightarrow B(n, 2r) \setminus \{n\} \times \mathfrak{su}(2).$$

---

We cut off the sequence of connections $A_{\alpha}$ on $\mathfrak{su}(E)$ over the annulus $\Omega(x_i; \frac{1}{2}r, 2r)$ and thus obtain a sequence of $C^\infty$ connections $A_{i,r,\alpha}$ on the sequence of SO(3) bundles $V_{i,r,\alpha}$ over $S^4$ by setting

$$A_{i,r,\alpha} := \begin{cases}
A_{\alpha} & \text{on } \mathfrak{su}(E)|_{B(n, \frac{1}{2}r)}, \\
\Gamma + \chi_{i,r}a_{i,\alpha} & \text{on } S^4 \setminus \{n\} \times \mathfrak{su}(2).
\end{cases}$$

Recall from Lemma 4.4 that there is a constant $C$ independent of $\alpha$ such that $\|F^{+}_{A_{\alpha}}\|_{L^\infty(X)} \leq C$ and so

(4.12) $$\|F^{+}_{A_{\alpha}}\|_{L^2(B(x_i,2r))} \leq Cr^2 \quad \text{for all } \alpha.$$

Since

$$F^{+}_{A_{i,r,\alpha}} = \chi_{i,r}F^{+}_{A_{\alpha}} + (d\chi_{i,r} \wedge a_{i,\alpha})^+ + \chi_{i,r}(\chi_{i,r}-1)(a_{i,\alpha} \wedge a_{i,\alpha})^+,$$

the estimates (4.10), (4.11), and (4.12) imply that

$$\|F^{+}_{A_{i,r,\alpha}}\|_{L^2(S^4)} \leq \|F^{+}_{A_{\alpha}}\|_{L^2(B(x_i,2r))} \\
+ \sqrt{2}\|d\chi_{i,r}\|_{L^4(X)} \|a_{i,\alpha}\|_{L^4(\Omega(x_i; \frac{1}{2}r,2r))} \\
+ \sqrt{2}\|a_{i,\alpha}\|_ {L^4(\Omega(x_i; \frac{1}{2}r,2r))} \\
\leq C(r+r^2), \quad \alpha \geq \alpha_0.$$

Therefore,

(4.13) $$\lim_{r \to 0} \lim_{\alpha \to \infty} \|F^{+}_{A_{i,r,\alpha}}\|_{L^2(S^4)} = 0.$$

Similarly, as

$$F_{A_{i,r,\alpha}} = \chi_{i,r}F_{A_{\alpha}} + d\chi_{i,r} \wedge a_{i,\alpha} + \chi_{i,r}(\chi_{i,r}-1)a_{i,\alpha} \wedge a_{i,\alpha},$$

the estimates (4.10) and (4.11) yield

$$\|F_{A_{i,r,\alpha}} - F_{A_{\alpha}}\|_{L^2(\Omega(x_i; \frac{1}{2}r,2r))} \\
\leq \|\nabla_{\Gamma}a_{i,\alpha}\|_{L^2(\Omega(x_i; \frac{1}{2}r,2r))} + c\|a_{i,\alpha}\|_{L^4(\Omega(x_i; \frac{1}{2}r,2r))} \\
+ \|a_{i,\alpha}\|_ {L^4(\Omega(x_i; \frac{1}{2}r,2r))} \\
< C(r+r^2), \quad \alpha \geq \alpha_0.$$

---

Therefore,

(4.14) $\lim_{r \to 0} \lim_{\alpha \to \infty} \| F_{A_i,r,\alpha} - F_{A_\alpha} \|_{L^2(\Omega(x_i; \frac{1}{2} r, 2r))} = 0$.

We can now complete the argument that the $\kappa_i$ are integers:

Claim 4.22. There is an SU(2) bundle $E_i$ over $S^4$ such $c_2(E_i) = \kappa_i$ for each $i = 1, \ldots, m$.

Proof. Fix an index $i \in \{1, \ldots, m\}$. Over $S^4$, the SO(3) bundles $V_{i,r,\alpha}$ lift to SU(2) bundles $E_{i,r,\alpha}$ with $V_{i,r,\alpha} = \mathfrak{su}(E_{i,r,\alpha})$ and $p_1(V_{i,r,\alpha}) = -4c_2(E_{i,r,\alpha})$. The second Chern classes of the SU(2) bundles $E_{i,r,\alpha}$ are given by

$$c_2(E_{i,r,\alpha}) = \frac{1}{8\pi^2} \int_S^4 \left(|F_{A_i,r,\alpha}^-|^2 - |F_{A_i,r,\alpha}^+|^2\right) dV,$$

recalling that the isomorphisms ad : $\mathfrak{su}(E_{i,r,\alpha}) \rightarrow \mathfrak{so}(\mathfrak{su}(E_{i,r,\alpha}))$ are implicit and that we view $F_{A_i,r,\alpha}$ as sections of $\Lambda^2 \otimes \mathfrak{su}(E_{i,r,\alpha})$. Therefore, by (4.14) and (4.13) and the fact that $F_{A_i,r,\alpha} = F_{A_\alpha}$ on $B(x_i, \frac{1}{2} r)$, we have

$$\lim_{r \to 0} \lim_{\alpha \to \infty} c_2(E_{i,r,\alpha}) = \lim_{r \to 0} \lim_{\alpha \to \infty} \frac{1}{8\pi^2} \int_S^4 |F_{A_i,r,\alpha}^-|^2 dV$$

$$= \lim_{r \to 0} \lim_{\alpha \to \infty} \frac{1}{8\pi^2} \int_S^4 \left(|F_{A_i,r,\alpha}^-|^2 + |F_{A_i,r,\alpha}^+|^2\right) dV$$

$$= \lim_{r \to 0} \lim_{\alpha \to \infty} \frac{1}{8\pi^2} \int_B(x_i, 2r) |F_{A_i,r,\alpha}|^2 dV$$

$$= \lim_{r \to 0} \lim_{\alpha \to \infty} \frac{1}{8\pi^2} \int_B(x_i, 2r) |F_{A_\alpha}|^2 dV = \kappa_i,$$

where the final equality follows by definition of $\kappa_i$. Thus, for small enough $r$ and large enough $\alpha$, we have $c_2(E_{i,r,\alpha}) = c_2(E_i)$ for some fixed SU(2) bundle $E_i$ over $S^4$ and so $\kappa_i = c_2(E_i)$, completing the proof of the claim. q.e.d.

By Claim 4.22 the $\kappa_i$ are positive integers for $i = 1, \ldots, m$. We can now compute the second Chern class of the limit bundle $E_0$. The Chern-Weil identity (2.33) implies that, for all $\alpha$,

$$-\frac{1}{4} p_1(\mathfrak{su}(E)) = c_2(E) - \frac{1}{4} c_1(E)^2 = \frac{1}{8\pi^2} \int_X \left(|F_{A_\alpha}^-|^2 - |F_{A_\alpha}^+|^2\right) dV.$$

---

Therefore, by (4.12) we have

$$c_2(E) - \frac{1}{4} c_1(E)^2 = \lim_{r \to 0} \lim_{\alpha \to \infty} \frac{1}{8\pi^2} \int_X \left( |F_A_\alpha|^2 - |F_A^+_\alpha|^2 \right) dV$$
$$= \lim_{r \to 0} \lim_{\alpha \to \infty} \frac{1}{8\pi^2} \int_X \cup_{i=1}^{m} B(x_i, 2r) \left( |F_A_\alpha|^2 - |F_A^+_\alpha|^2 \right) dV$$
$$+ \sum_{i=1}^{m} \lim_{r \to 0} \lim_{\alpha \to \infty} \frac{1}{8\pi^2} \int_B(x_i, 2r) \left( |F_A_\alpha|^2 - |F_A^+_\alpha|^2 \right) dV$$
$$= \frac{1}{8\pi^2} \int_X \left( |F_A_0|^2 - |F_A^+_0|^2 \right) dV + \sum_{i=1}^{m} \kappa_i$$
$$= c_2(E_0) - \frac{1}{4} c_1(E_0)^2 + \sum_{i=1}^{m} \kappa_i.$$

Now $c_1(E) = c_1(E_0)$ and thus $c_2(E_0) = c_2(E) - \sum_{i=1}^{m} \kappa_i$. This completes the proof of Lemma 4.21. q.e.d.

Therefore, after passing to a subsequence, the sequence of points $[A_\alpha, \Phi_\alpha]$ in $M_{W,E}$ converges to an ideal monopole $[A_0, \Phi_0, \mathbf{x}]$ in $M_{L,E_0} \times \text{Sym}^{\ell}(X)$, for some integer $\ell \geq 0$, and Lemma 4.21 implies the Chern classes of the limit bundle $E_0$ are given by $c_1(E_0) = c_1(E)$ and $c_2(E_0) = c_2(E) - \ell$.

It remains to give an upper bound for the integer $\ell = c_2(E) - c_2(E_0)$. The Chern-Weil identity (2.33) implies that

$$\ell = c_2(E) - c_2(E_0) = \frac{1}{8\pi^2} \int_X \left( |F_A|^2 - |F_A^+|^2 \right) dV$$
$$- \frac{1}{8\pi^2} \int_X \left( |F_A_0|^2 - |F_A^+_0|^2 \right) dV,

and thus, by Lemma 4.3, we have

$$\ell \leq \frac{1}{8\pi^2} \int_X |F_A|^2 dV + \frac{1}{8\pi^2} \int_X |F_A^+_0|^2 dV \leq N_p,$$

for some positive integer $N_p = N_p(c_1(E), c_2(E), g, F(A_{\det W}), F(A_{\det E}))$. This completes the proof of Theorem 4.20. q.e.d.

Remark 4.23. The compactness result in this section for the moduli space of PU(2) monopoles has an antecedent in [31, Theorem 3.2] (due to Taubes) in the following sense. Taubes' theorem provides a weak compactness result for connections $A$ satisfying the ‘infinite-dimensional’ part' of the anti-self-dual equation, namely $\Pi_{A;\mu} F_A^+ = 0$, where $\mu \notin$ Spec $d_A^+ d_A^*$, and $\Pi_{A;\mu}$ is the $L^2$-orthogonal projection onto the eigenvectors of $d_A^+ d_A^*$ with eigenvalue less than $\mu$, together with the curvature bounds $\|F_A\|_{L^2(X)} + \|d_A F_A^+\|_{L^2(X)} \leq C$ for some constant $C$ independent of $A$. The analogous point here is that although $\int_X |F_A|^2 dV$ is not a topological invariant unless $F_A^+ = 0$ or $F_A^- = 0$, just as in the case of the PU(2) monopoles, it is enough for the purposes of obtaining a weak compactness result to have uniform bounds on the $L^2$ norm of $F_A$ together with an $L^p$ bound on $F_A^+$ for some $p > 2$.

There is one further compactness result we will need, analogous to Uhlenbeck’s original compactness theorem for connections (not necessarily satisfying any elliptic equation) with $L^p$ bounds on curvature with $p > 2$ [95, Theorem 1.5].

**Proposition 4.24.** Let $p > 2$ and $K > 0$ be constants. If $[A_\alpha, \Phi_\alpha]$ is an infinite sequence in $M_{W,E}$ satisfying

$$\|F_A_\alpha\|_{L^p(X)} \leq K,$$

then there is a subsequence $\{\alpha'\} \subset \{\alpha\}$ such that the sequence $[A_{\alpha'}, \Phi_{\alpha'}]$ converges to a point $[A_\infty, \Phi_\infty] \in M_{W,E}$.

**Proof.** Let $(A_\alpha, \Phi_\alpha)$ be a corresponding sequence of $C^\infty$ pairs. Since $p > 2$, Hölder’s inequality implies that for any geodesic ball $B(x,r) \subset X$ we have

$$\|F_A_\alpha\|_{L^2(B(x,r)} \leq cr^{2-(4/p)} \|F_A_\alpha\|_{L^p(B(x,r))} \leq cKr^{2-(4/p)}.$$

Hence, for small enough $r$, Proposition 4.18 applies and there are a subsequence $\{\alpha'\} \subset \{\alpha\}$ and a sequence of $C^\infty$ gauge transformations $u_{\alpha'}$ such that the sequence $u_{\alpha'} (A_{\alpha'}, \Phi_{\alpha'})$ converges in $C^\infty$ to a limit $(A_\infty, \Phi_\infty)$ over all of $X$, with no exceptional points. q.e.d.

As we shall see in §5.1.2, Proposition 4.24 allows us to work with perturbation parameters $(\tau_0, \vec{\tau}, \vec{\vartheta})$ and a metric $g$ which are $C^\infty$ rather than just $C^r$, as required by the application of the Sard-Smale theorem in our proof of transversality in §5.

## 5. Transversality

In this section we show that for generic perturbation parameters $(\vartheta_0, \tau_0, \vec{\tau}, \vec{\vartheta})$ the moduli space of solutions to the perturbed PU(2) monopole equations (2.27) is a smooth manifold away from the zero-section and reducible pairs.

The outline of the proof is of the now standard form introduced in [14] and [30]. In §5.1 we define a parametrized moduli space and explain why transversality for the moduli space (Corollary 5.3) follows from transversality for the parametrized moduli space (Theorem 5.2) via the Sard-Smale theorem. In §5.2 we show that the parametrized moduli space is a smooth Banach manifold (Theorem 5.2). The proof of Theorem 5.2 relies on the fact that a PU(2) monopole, which is reducible on an admissible open subset of the manifold $X$, is reducible on the entire manifold (Theorem 5.11) and this is proved in §5.3.

The proof of Theorem 1.3 does not apply to PU(2) monopoles which are zero-sections or which are reducible. We describe the cokernels of $D\mathfrak{S}$ evaluated at these pairs in the sequel [25] to the present article.

5.1. The parametrized moduli space. It is convenient to first consider the question of transversality for the top stratum $M_{W,E}^{*,0}$ of the Uhlenbeck compactification $\bar{M}_{W,E}$ and then consider the very slight modification required to obtain simultaneous transversality for all the lower-level moduli spaces $M_{W,E-\ell}^{*,0}|_{\Sigma} \subset C_{W,E-\ell}^{*,0} \times \Sigma$, for smooth strata $\Sigma \subset \text{Sym}^{\ell}(X)$.

5.1.1. Transversality for the top-level moduli space. The condition in Proposition 2.28 that the section $\mathfrak{S}$, vanish transversely is, of course, not necessarily true for all the parameters $(\tau_0, \vartheta_0, \vec{\tau}, \vec{\vartheta})$, on which $\mathfrak{S}$ depends. As in the cases of the moduli spaces of anti-self-dual connections [14], [20], [30] and Seiberg-Witten monopoles [47], [98], we first show that the family of moduli spaces parametrized by the perturbations $(\tau_0, \vartheta_0, \vec{\tau}, \vec{\vartheta})$ is smooth and then apply the Sard-Smale theorem [80] to conclude that for generic perturbations $(\tau_0, \vartheta_0, \vec{\tau}, \vec{\vartheta})$ (that is, a subset of perturbations which is the complement of some first-category subset), the moduli space $\mathfrak{S}^{-1}(0) = M_{W,E}^{*,0}(\tau_0, \vartheta_0, \vec{\tau}, \vec{\vartheta})$ is smooth.

Set $\mathcal{P}_0^r := C^r(X, \mathfrak{gl}(\Lambda^+)) \oplus C^r(X, \Lambda^1 \otimes \mathbb{C})$, let $\mathcal{P}^r := \mathcal{P}_0^r \oplus \mathcal{P}_{\tau}^r \oplus \mathcal{P}_{\vartheta}^r$ denote our Banach space of $C^r$ perturbation parameters, and define a $^\circ G_E$-equivariant map

$$
\mathfrak{S} := (\mathfrak{S}_1, \mathfrak{S}_2): \mathcal{P}^r \times \tilde{\mathcal{C}}_{W,E} \rightarrow L_{k-1}^2(\Lambda^+ \otimes \mathfrak{su}(E)) \oplus L_{k-1}^2(W^{-} \otimes E)
$$ by setting

$$\underline{\mathfrak{S}}(\tau_0, \vartheta_0, \vec{\tau}, \vec{\vartheta}, A, \Phi)$$

(5.1) $$:= \begin{pmatrix} \underline{\mathfrak{S}}_1(\tau_0, \vartheta_0, \vec{\tau}, \vec{\vartheta}, A, \Phi) \\ \underline{\mathfrak{S}}_2(\tau_0, \vartheta_0, \vec{\tau}, \vec{\vartheta}, A, \Phi) \end{pmatrix}$$

$$= \begin{pmatrix} F_A^+ - (\mathrm{id} + \tau_0 \otimes \mathrm{id}_{\mathrm{su}(E)} + \vec{\tau} \cdot \vec{\mathfrak{m}}(A)) \rho^{-1}(\Phi \otimes \Phi^*)_{00} \\ D_A \Phi + \rho(\vartheta_0)\Phi + \vec{\vartheta} \cdot \vec{\mathfrak{m}}(A)\Phi \end{pmatrix},$$

where $(A, \Phi)$ is a pair on $(\mathfrak{su}(E), W^+ \otimes E)$ and the isomorphism ad : $\mathfrak{su}(E) \simeq \mathfrak{so}(\mathfrak{su}(E))$ is implicit, $^\circ G_E$ acts trivially on the space of perturbations $\mathcal{P}^r$, and so $\underline{\mathfrak{S}}^{-1}(0)/^\circ G_E$ is a subset of $\mathcal{P}^r \times C_{W,E}$. We let $M_{W,E}$ denote the parametrized moduli space $\underline{\mathfrak{S}}^{-1}(0)/^\circ G_E$ and let $M_{W,E}^{*,0} = M_{W,E} \cap (\mathcal{P}^r \times C_{W,E}^{*,0})$.

Remark 5.1. While we assumed for convenience in §3 and §4 that the parameters $g, \tau_0, \vartheta_0, \vec{\tau}, \vec{\vartheta}$ were $C^\infty$, the only difference, if the parameters are only assumed to be $C^r$ for some finite $r$, is the slight increase in bookkeeping required to keep track of the regularity of solutions to (2.27) and other associated elliptic systems.

Just as in §2.6, the $^\circ G_E$-equivariant map $\underline{\mathfrak{S}}$ defines a section of a Banach vector bundle $\underline{\mathfrak{V}}$ over $\mathcal{P}^r \times C_{W,E}^{*,0}$ with total space

$$\underline{\mathfrak{V}} := \mathcal{P}^r \times \tilde{C}_{W,E}^{*,0} \times^\circ G_E \left(L_{k-1}^2(\Lambda^+ \otimes \mathfrak{su}(E)) \oplus L_{k-1}^2(W^- \otimes E)\right),$$

so $\mathfrak{S} := \underline{\mathfrak{S}}(\tau_0, \vartheta_0, \vec{\tau}, \vec{\vartheta}, \cdot)$ is a section over $\tilde{C}_{W,E}^{*,0}$ of the Banach vector bundle $\mathfrak{V} := \underline{\mathfrak{V}}|_{(\tau_0, \vartheta_0, \vec{\tau}, \vec{\vartheta})}$ in (2.34). In particular, the parametrized moduli space $M_{W,E}^{*,0}$ is the zero set of the section $\underline{\mathfrak{S}}$ of the vector bundle $\mathfrak{V}$ over $\mathcal{P}^r \times C_{W,E}^{*,0}$.

Theorem 5.2. The zero set in $\mathcal{P}^r \times C_{W,E}^{*,0}$ of the section $\underline{\mathfrak{S}}$ is regular and, in particular, the moduli space $M_{W,E}^{*,0}$ is a smooth Banach submanifold of $\mathcal{P}^r \times C_{W,E}^{*,0}$.

To preserve continuity, we defer the proof of Theorem 5.2 to §5.2. The differential $D\underline{\mathfrak{S}} := (D\underline{\mathfrak{S}})_{[\tau_0, \vartheta_0, \vec{\tau}, \vec{\vartheta}, A, \Phi]}$ in $\mathcal{P}^r \times C_{W,E}^{*,0}$ is given by

(5.2) $$D\underline{\mathfrak{S}}(\delta\tau_0, \delta\vartheta_0, \delta\vec{\tau}, \delta\vec{\vartheta}, a, \phi) = \begin{pmatrix} D\underline{\mathfrak{S}}_1(\delta\tau_0, \delta\vartheta_0, \delta\vec{\tau}, \delta\vec{\vartheta}, a, \phi) \\ D\underline{\mathfrak{S}}_2(\delta\tau_0, \delta\vartheta_0, \delta\vec{\tau}, \delta\vec{\vartheta}, a, \phi) \end{pmatrix},$$ where $(a, \phi) \in \mathbf{K}_{A,\Phi} \subset L_{k}^{2}(\Lambda^{1} \otimes \mathfrak{su}(E)) \oplus L_{k}^{2}(W^{+} \otimes E)$ represents a vector in the tangent space $(T\mathcal{C}_{W,E}^{*,0})_{[A,\Phi]}$ and $(\delta\tau_{0}, \delta\vartheta_{0}, \delta\tau, \delta\vec{\vartheta}) \in \mathcal{P}^{r}$. The differential of the first component in (5.2) is given explicitly by

$$D\mathfrak{S}_{1}\left(\delta\tau_{0}, \delta\vartheta_{0}, \delta\tau, \delta\vec{\vartheta}, a, \phi\right)$$
$$= d_{A}^{+}a - \delta\tau_{0}\rho^{-1}(\Phi \otimes \Phi^{*})_{00}$$
$$- (\mathrm{id} + \tau_{0} \otimes \mathrm{id}_{\mathfrak{su}(E)} + \vec{\tau} \cdot \vec{\mathfrak{m}}(A))\rho^{-1}(\phi \otimes \Phi^{*} + \Phi \otimes \phi^{*})_{00}$$

(5.3)
$$-\sum_{j,l,\alpha}(\delta\tau_{j,l,\alpha} \otimes \mathrm{ad}(\mathfrak{m}_{j,l,\alpha}(A))\rho^{-1}(\Phi \otimes \Phi^{*})_{00}$$
$$-\sum_{j,l,\alpha}\tau_{j,l,\alpha} \otimes \mathrm{ad}\left(\frac{\delta\mathfrak{m}_{j,l,\alpha}}{\delta A}a\right)\rho^{-1}(\Phi \otimes \Phi^{*})_{00},

and the second component by

$$D\mathfrak{S}_{2}\left(\delta\tau_{0}, \delta\vartheta_{0}, \delta\tau, \delta\vec{\vartheta}, a, \phi\right)$$
$$= D_{A}\phi + \vec{\vartheta} \cdot \vec{\mathfrak{m}}(A)\phi + \rho(a)\Phi$$
$$+ \rho(\delta\vartheta_{0})\Phi + \sum_{j,l,\alpha}\rho(\delta\vartheta_{j,l,\alpha}) \otimes \mathfrak{m}_{j,l,\alpha}(A)\Phi$$
$$+ \sum_{j,l,\alpha}\rho(\vartheta_{j,l,\alpha}) \otimes\left(\frac{\delta\mathfrak{m}_{j,l,\alpha}}{\delta A}a\right)\Phi.

We note that from their definitions in §2.5.2 the perturbations (and their variations) are zeroth order, unlike the first order perturbations considered in [92].

Recall from the arguments of §2.2 that $D\mathfrak{S}(\cdot,d_{A,\Phi}^{0}\zeta) = 0$ for all $\zeta \in L_{k+1}^{2}(\mathfrak{su}(E)) \oplus i\mathbb{R}_{Z}$ since $\mathfrak{S}$ is $^\circ G_{E}$-equivariant. By Proposition 3.7 we may assume, without loss of generality, that the pair $(A, \Phi)$ in $\tilde{\mathcal{C}}_{W,E}^{*,0}$ is a $C^{r}$ representative for the point $[A, \Phi]$ in the zero set $\mathfrak{S}^{-1}(0) \subset \mathcal{C}_{W,E}^{*,0}$. Since the tangent space $(T\mathcal{C}_{W,E}^{*,0})_{[A,\Phi]}$ may be identified with $\mathbf{K}_{A,\Phi} := \text{Ker } d_{A,\Phi}^{0,*}$ (see §2.2), we have

$$D\mathfrak{S}(0,0,0,0,a, \phi) = d_{A,\Phi}^{1}(a, \phi) = (d_{A,\Phi}^{0,*} + d_{A,\Phi}^{1})(a, \phi),

for $(a, \phi) \in \mathbf{K}_{A,\Phi}$, so the differential $D\mathfrak{S}|_{\{0\} \times T\mathcal{C}_{W,E}^{*,0}}$ is Fredholm, where $\{0\} \times T\mathcal{C}_{W,E}^{*,0} = T(\{\tau_{0}, \vartheta_{0}, \vec{\tau}, \vec{\vartheta}\} \times \mathcal{C}_{W,E}^{*,0})$. Thus, $\mathfrak{S}$ is a Fredholm section when restricted to the fixed parameter fibers

$\{\tau_{0}, \vartheta_{0}, \vec{\tau}, \vec{\vartheta}\} \times \mathcal{C}_{W,E}^{*,0} \subset \mathcal{P}^{r} \times \mathcal{C}_{W,E}^{*,0}.$

---

The Sard-Smale theorem (in the form of Proposition 4.3.11 in [20]) then implies that there is a first-category subset of the space $P^r$ such that the zero sets in $C_{W,E}^{*,0}$ of the sections $\mathfrak{S} = \mathfrak{S}(\tau_0, \vartheta_0, \vec{\tau}, \vec{\vartheta}, \cdot)$ are regular for all $C^r$ perturbations $(\tau_0, \vartheta_0, \vec{\tau}, \vec{\vartheta})$ in the complement of this subset. Now

$$M_{W,E}^{*,0}(\tau_0, \vartheta_0, \vec{\tau}, \vec{\vartheta}) = \mathfrak{S}^{-1}(0) \cap C_{W,E}^{*,0},$$

and so for generic parameters $(\tau_0, \vartheta_0, \vec{\tau}, \vec{\vartheta})$, the moduli space $M_{W,E}^{*,0}(\tau_0, \vartheta_0, \vec{\tau}, \vec{\vartheta})$ is a smooth manifold of the expected dimension. In summary, we have:

**Corollary 5.3.** There is a first-category subset of the space $P^r$, such that for all $C^r$ perturbations $(\tau_0, \vartheta_0, \vec{\tau}, \vec{\vartheta})$ in the complement of this subset, the zero locus of the section $\mathfrak{S}$ is regular and so the moduli space $M_{W,E}^{*,0}(\tau_0, \vartheta_0, \vec{\tau}, \vec{\vartheta}) = \mathfrak{S}^{-1}(0) \cap C_{W,E}^{*,0}$ is a smooth submanifold of $C_{W,E}^{*,0}$ with the expected dimension.

We recall that a subset $S$ of a topological space $P$ is a set of the first category if its complement $P - S$ is a countable intersection of dense open sets or, equivalently, if $S$ is a countable union of closed subsets of $P$ with empty interior; if $P$ is a complete metric space, then Baire’s theorem implies that $P - S$ is dense in $P$ [76]. In our applications, $P$ will either be a Banach or Fréchet space (with a complete metric), so $P - S$ will always be dense if $S$ is a first-category subset.

**5.1.2. Reduction to the case of $C^\infty$ parameters.** The restriction to $C^r$ parameters $(\tau_0, \vartheta_0, \vec{\tau}, \vec{\vartheta})$, necessary to apply the Sard-Smale theorem in §5.1.1, proves inconvenient in practice. We shall see that these restrictions can now be removed, so we need only use $C^\infty$ parameters $(\tau_0, \vartheta_0, \vec{\tau}, \vec{\vartheta})$. Although we did not need the metric $g$ to be generic in order for our transversality proof to work, we will nonetheless require the metric $g$ to be generic in the sequels to the present article and so, a priori, $g$ would also be restricted to a certain Banach manifold of metrics on $X$. An argument almost identical to the one which we describe here can be used to show that one need only consider generic $C^\infty$ metrics in those applications.

There is an argument due to Taubes — for the moduli space of Seiberg-Witten monopoles — which reduces the case of transversality for $C^\infty$ parameters to the case of Hölder or Sobolev parameters [77, §9.4]. (A related result for generic metrics due to Freed and Uhlenbeck appears as Proposition 3.20 in [30], although it is only stated for the moduli space of anti-self-dual SU(2) connections with second Chern class one over a simply-connected, negative definite four-manifold.)

We adapt Taubes argument here to the case of the moduli spaces of PU(2) monopoles. We define

$$\mathcal{P} := \mathcal{P}_0 \oplus \mathcal{P}_\tau \oplus \mathcal{P}_\vartheta,
$$
$$\mathcal{P}_0 := \Omega^0(X, \mathfrak{gl}(\Lambda^+)) \oplus \Omega^1(X, \mathbb{C}),
$$
$$\mathcal{P}_\tau = \ell_\delta^1(\mathbb{A}, \Omega^0(X, \mathfrak{gl}(\Lambda^+))) := \bigcap_{r=0}^{\infty} \ell_\delta^1(\mathbb{A}, C^r(X, \mathfrak{gl}(\Lambda^+))),
$$
$$\mathcal{P}_\vartheta = \ell_\delta^1(\mathbb{A}, \Omega^1(X, \mathbb{C})) := \bigcap_{r=0}^{\infty} \ell_\delta^1(\mathbb{A}, C^r(X, \Lambda^1 \otimes \mathbb{C})),

and let $\mathcal{P}^r$ be the Banach space

$$\mathcal{P}^r := \mathcal{P}_0^r \oplus \mathcal{P}_\tau^r \oplus \mathcal{P}_\vartheta^r
$$
$$= C^r(X, \mathfrak{gl}(\Lambda^+)) \oplus C^r(X, \Lambda^1 \otimes \mathbb{C})
$$
$$\oplus \ell_\delta^1(\mathbb{A}, C^r(X, \mathfrak{gl}(\Lambda^+))) \oplus \ell_\delta^1(\mathbb{A}, C^r(X, \Lambda^1 \otimes \mathbb{C})).

Define metrics $d_0$, $d_\tau$ and $d_\vartheta$ on Met(X), $\mathcal{P}_0$, $\mathcal{P}_\tau$ and $\mathcal{P}_\vartheta$ by setting

$$d_0(\tau_{01}, \vartheta_{01}; \tau_{02}, \vartheta_{02}) := \sum_{r=0}^{\infty} \frac{2^{-r}\left(\| \tau_{01} - \tau_{02} \|_{C^r} + \| \vartheta_{01} - \vartheta_{02} \|_{C^r}\right)}{1 + \| \tau_{01} - \tau_{02} \|_{C^r} + \| \vartheta_{01} - \vartheta_{02} \|_{C^r}},
$$
$$d_\tau(\vec{\tau}_1, \vec{\tau}_2) := \sum_{r=0}^{\infty} \frac{2^{-r}\|\vec{\tau}_1 - \vec{\tau}_2\|_{\ell_\delta^1(C^r)}}{1 + \|\vec{\tau}_1 - \vec{\tau}_2\|_{\ell_\delta^1(C^r)}},
$$
$$d_\vartheta(\vec{\vartheta}_1, \vec{\vartheta}_2) := \sum_{r=0}^{\infty} \frac{2^{-r}\|\vec{\vartheta}_1 - \vec{\vartheta}_2\|_{\ell_\delta^1(C^r)}}{1 + \|\vec{\vartheta}_1 - \vec{\vartheta}_2\|_{\ell_\delta^1(C^r)}},

and observe that $\mathcal{P}_0$, $\mathcal{P}_\tau$ and $\mathcal{P}_\vartheta$ are complete metric spaces, with the above metrics inducing the $C^\infty$ topologies. Thus, $\mathcal{P}$ is a complete metric space with respect to the product metric $d = d_0 \times d_\tau \times d_\vartheta$, which induces the $C^\infty$ topology on $\mathcal{P}$. The $C^r$ topology of $\mathcal{P}^r$ is induced by the product metric $d^r := d_0^r \times d_\tau^r \times d_\vartheta^r$.

Let $\mathcal{P}_{\text{reg}} \subset \mathcal{P}$ be the subspace of parameters for which the zero set of $\mathfrak{S}_p$ is regular, and note that

$$\mathcal{P}_{\text{reg}} = \bigcap_{n \geq 1} \mathcal{P}_{n,\text{reg}},$$ where $ \mathcal{P}_{n,\mathrm{reg}}\subset\mathcal{P}_{\mathrm{reg}} $ is the subsp the differential $ D\mathfrak{S}_{\mathbf{p}} $ is surjective f satisfying

of $ C^{\infty} $ parameters p such that for all pairs (A, $ \Phi $ ) in $ \mathfrak{S}_{p}^{-1}(0)\cap\tilde{\mathcal{C}}_{W,E}^{*,0}, $

$$
\mathcal{P}_{n,\mathrm{reg}}\subset\mathcal{P}_{\mathrm{reg}}
$$

$$
C^{\infty}
$$

$$
D\mathfrak{S}_{\mathrm{p}}
$$

$$
(A,\Phi)
$$

$$
\mathfrak{S}_{\mathbf{p}}^{-1}(0)\cap\tilde{\mathcal{C}}_{W,E}^{*,0},
$$

(5.5)

$$
\|F_{A}\|_{L^{p}}\leq n\quad\mathrm{and}\quad\nu_{0}(A,\Phi;\mathbf{p})\geq1/n,
$$

for some $ p > 2 $ , where $ \nu_{0}(A,\Phi;{\bf p}) $ is the least eigenvalue of the Laplacian $ \Delta_{A,\Phi;{\bf p}}^{0}:=d_{A,\Phi}^{0,*}d_{A,\Phi}^{0} $ computed with respect to the metric g. Define, in the analogous way, the subspaces $ \mathcal{P}_{\mathrm{reg}}^{r} $ and $ \mathcal{P}_{n,\mathrm{reg}}^{r} $ of $ \mathcal{P}^{r}. $

$$
p>2
$$

$$
\nu_{0}(A,\Phi;\mathbf{p})
$$

$$
\Delta_{A,\Phi;\mathbf{p}}^{0}:=d_{A,\Phi}^{0,*}d_{A,\Phi}^{0}
$$

$$
g.
$$

$$
\mathcal{P}_{reg}^{r}
$$

$$
\mathcal{P}_{n,\mathrm{reg}}^{r}
$$

$$
\mathcal{P}^{r}
$$

The uniform upper $ L^{p} $ bound uniform lower bound on $ \nu_{0}(A,\Phi $ reducible or zero-section pairs of the Laplacian $ \Delta_{A,\Phi ;\mathbf{p}}^{2}:=d_{A,\Phi}^{1} $ rameters $ \mathbf{p}=(\tau_{0},\vartheta_{0},\vec{\tau},\vec{\vartheta}). $ The $ \nu_{2}(A,\Phi ;\mathbf{p})>0. $

on $ F_{A} $ precludes bubbling, while the keeps $ ( A,\Phi) $ bounded away from the let $ \nu_{2}(A,\Phi;{\bf p}) $ be the least eigenvalue $ _{A,\Phi}^{1,*} $ computed with respect to the pa $ ( D\mathfrak{S}_{{\bf p}} )_{A,\Phi} $ is surjective if and only if

$$
F_{A}
$$

$$
\nu_{0}(A,\Phi)
$$

$$
\nu_{2}(A,\Phi;\mathbf{p})
$$

$$
\Delta_{A,\Phi;\mathbf{p}}^{2}:=d_{A,\Phi}^{1}d_{A,\Phi}^{1,*}
$$

$$
\mathbf{p}=(\tau_0,\vartheta_0,\vec{\tau},\vec{\vartheta})
$$

$$
(D\mathfrak{S}_{\mathbf{p}})_{A,\Phi}
$$

$$
\nu_{2}(A,\Phi;\mathbf{p})>0
$$

Claim 5.4. The subspace $ \mathcal{P}_{n,\mathrm{reg}}\subset\mathcal{P} $ is open in the $ C^{\infty} $ topology and $ \mathcal{P}_{n,\mathrm{reg}}^{r}\subset\mathcal{P}^{r} $ is open in the $ C^{r} $ topology.

$$
\mathcal{P}_{n,\mathrm{reg}}\subset\mathcal{P}
$$

$$
C^{\infty}
$$

$$
\mathcal{P}_{n,\mathrm{reg}}^{r}\subset\mathcal{P}^{r}
$$

$$
C^{r}
$$

Proof. Let $ \left\{\mathbf{p}_{\alpha}\right\}_{\alpha=1}^{\infty}\subset\mathcal{P}\backslash\mathcal{P}_{n,\mathrm{reg}} $ be a sequence of parameters and suppose that $ \mathbf{p}_{\alpha} $ converges to $ \mathbf{p}\in\mathcal{P} $ in the $ C^{\infty} $ topology. Then there is a sequence of solutions $ (A_{\alpha},\Phi_{\alpha}) $ to (2.27) in $ \tilde{\mathcal{C}}_{W,E}^{*,0} $ , with parameters $ \mathbf{p}_{\alpha} $ which satisfy the bounds in (5.5) and for which $ \nu_{2}(A_{\alpha},\Phi_{\alpha};\mathbf{p}_{\alpha})=0 $ Proposition 4.24 and the $ L^{p} $ bounds in (5.5) imply that, after passing to a subsequence, there is a sequence of gauge transformations $ \{u_{\alpha}\}\subset\mathcal{G}_{E} $ such that $ u_{\alpha}(A_{\alpha},\Phi_{\alpha}) $ converges (strongly) in $ L_{k}^{2} $ to a solution $ (A,\Phi) $ in $ \tilde{\mathcal{C}}_{W,E}^{*,0} $ to (2.27) which satisfies the curvature bound in (5.5). Standard perturbation theory implies that the eigenvalues $ \nu_{i}(u_{\alpha}(A_{\alpha},\Phi_{\alpha});\mathbf{p}_{\alpha}) $ converge to $ \nu_{i}(A,\Phi;\mathbf{p}) $ for $ i=0,2 $ [41], so that the triple $ (A,\Phi;\mathbf{p}) $ satisfies the eigenvalue bound in (5.5). The eigenvalue $ \nu_{2}(A,\Phi;\mathbf{p}) $ must be zero otherwise the eigenvalues $ \nu_{2}(u_{\alpha}(A_{\alpha},\Phi_{\alpha});\mathbf{p}_{\alpha}) $ would be positive for large enough $ \alpha $ . Hence, $ \mathbf{p}\notin\mathcal{P}_{n,\mathrm{reg}} $ and so $ \mathcal{P}_{n,\mathrm{reg}} $ is open. The proof that $ \mathcal{P}_{n,\mathrm{reg}}^{r} $ is an open subset of $ \mathcal{P}^{r} $ is identical. q.e.d.

$$
\{\mathbf{p}_{\alpha}\}_{\alpha=1}^{\infty}\subset\mathcal{P}\setminus\mathcal{P}_{n,\mathrm{reg}}
$$

$$
\mathbf{p}_{\alpha}
$$

$$
C^{\infty}
$$

$$
\mathbf{p}\in\mathcal{P}
$$

$$
\left(A_{\alpha},\Phi_{\alpha}\right)
$$

$$
\tilde{\mathcal{C}}_{W,E}^{*,0},
$$

$$
\mathbf{p}_{\alpha}
$$

$$
\left[\nu_{2}(A_{\alpha},\Phi_{\alpha};\mathbf{p}_{\alpha})=0\right.
L^{p}
$$

$$
\{u_{\alpha}\}\subset\mathcal{G}_{E}
$$

$$
u_{\alpha}(A_{\alpha},\Phi_{\alpha})
$$

$$
L_{k}^{2}
$$

$$
\tilde{\mathcal{C}}_{W,E}^{*,0}
$$

$$
\nu_{i}(u_{\alpha}(A_{\alpha},\Phi_{\alpha});\mathbf{p}_{\alpha})
$$

$$
\nu_{i}(A,\Phi;\mathbf{p})
$$

$$
i=0,2
$$

$$
\left(A,\Phi;\mathbf{p}\right)
$$

$$
\nu_{2}(A,\Phi;\mathbf{p})
$$

$$
\nu_{2}(u_{\alpha}(A_{\alpha},\Phi_{\alpha});\mathbf{p}_{\alpha})
$$

$$
\alpha
$$

$$
\mathbf{p}\notin\mathcal{P}_{n,reg}
$$

$$
\mathcal{P}_{n,\mathrm{reg}}^{r}
$$

$$
\mathcal{P}_{n,\mathrm{reg}}
$$

$$
\mathcal{P}^{r}
$$

Claim 5.5. The subspace $ \mathcal{P}_{n,\mathrm{reg}}\subset\mathcal{P} $ is dense in the $ C^{\infty} $ topology.

$$
\mathcal{P}_{n,\mathrm{reg}}\subset\mathcal{P}
$$

$$
C^{\infty}
$$

Proof. By Corollary 5.3, the space $ \mathcal{P}_{\mathrm{reg}}^{r} $ is the complement in $ \mathcal{P}^{r} $ of a first-category subset and so is dense by Baire's theorem; clearly, $ \mathcal{P}_{n,\mathrm{reg}}^{r} $ is also dense in $ \mathcal{P}^{r} $ , since $ \mathcal{P}_{\mathrm{reg}}^{r}\subset\mathcal{P}_{n,\mathrm{reg}}^{r}. $ Let $ \mathbf{p}\in\mathcal{P} $ be a $ C^{\infty} $ parameter, and let $ \left\{\mathbf{p}_{\alpha}\right\}\subset\mathcal{P}_{n,\mathrm{reg}}^{r} $ be a sequence of $ C^{r} $ parameters such that $ d^{r}(\mathbf{p},\mathbf{p}_{\alpha})<2^{-\alpha-1} $ , so $ \mathbf{p}_{\alpha} $ converges in $ C^{r} $ to $ \mathbf{p}. $ Since $ \mathcal{P}_{n,\mathrm{reg}}^{r}\subset\mathcal{P}^{r} $ is open by Claim 5.4 and the $ C^{\infty} $ parameters $ \mathcal{P} $ are dense in $ \mathcal{P}_{n,\mathrm{reg}}^{r}, $ we may choose, for each $ \alpha $ , a $ C^{\infty} $ parameter $ \mathbf{p}_{\alpha}^{\prime}\in\mathcal{P}_{n,\mathrm{reg}}^{r} $ such that $ d^{r}(\mathbf{p}_{\alpha},\mathbf{p}_{\alpha}^{\prime})< $

$$
\mathcal{P}_{reg}^{r}
$$

$$
\mathcal{P}^{r}
$$

$$
\mathcal{P}_{n,\mathrm{reg}}^{r}
$$

$$
\mathcal{P}_{\mathrm{reg}}^{r}\subset\mathcal{P}_{n,\mathrm{reg}}^{r}.
$$

$$
\mathcal{P}^{r}
$$

$$
\mathbf{p}\in\mathcal{P}
$$

$$
\{\mathbf{p}_{\alpha}\}\subset\mathcal{P}_{n,\mathrm{reg}}^{r}
$$

$$
C^{\infty}
$$

$$
C^{r}
$$

$$
d^{r}(\mathbf{p},\mathbf{p}_{\alpha})<2^{-\alpha-1}
$$

$$
\mathcal{P}_{n,\mathrm{reg}}^{r}\subset\mathcal{P}^{r}
$$

$$
C^{r}
$$

$$
\mathbf{p}_{\alpha}
$$

$$
C^{\infty}
$$

$$
\mathcal{P}
$$

$$
\mathcal{P}_{n,\mathrm{reg}}^{r}
$$

$$
\alpha,
$$

$$
C^{\infty}
$$

$$
\mathbf{p}_{\alpha}^{\prime}\in\mathcal{P}_{n,\mathrm{reg}}^{r}
$$

$$
d^{r}(\tilde{\mathbf{p}}_{\alpha},\mathbf{p}'_{\alpha})<
$$

---

2$^{-\alpha-1}$. Since $\mathbf{p}'_{\alpha}$ is $C^{\infty}$, then $\{\mathbf{p}'_{\alpha}\} \subset \mathcal{P}_{n,\text{reg}}$ and by construction we have $d^{r}(\mathbf{p}, \mathbf{p}'_{\alpha}) < 2^{-\alpha}$ and so the sequence $\{\mathbf{p}'_{\alpha}\}$ converges in $C^{r}$ to $\mathbf{p} \in \mathcal{P}$.

Therefore, for each $r$, we obtain a sequence $\{\mathbf{p}'_{\alpha}(r)\} \subset \mathcal{P}_{n,\text{reg}}$ which converges in $C^{r}$ to $\mathbf{p} \in \mathcal{P}_{\text{reg}}$. But then the diagonal sequence $\{\mathbf{p}'_{\alpha}(\alpha)\} \subset \mathcal{P}_{n,\text{reg}}$ converges to $\mathbf{p}$ in $C^{r}$ for each $r$ (it satisfies $d^{r}(\mathbf{p}, \mathbf{p}'_{\alpha}(\alpha)) < 2^{-\alpha}$ for all $\alpha \geq r$) and so the sequence converges in $C^{\infty}$ to $\mathbf{p} \in \mathcal{P}$, as required. q.e.d.

From Claims 5.4 and 5.5 we conclude that $\mathcal{P}_{\text{reg}}$ is a countable intersection of dense, open subsets of $\mathcal{P}$ and hence is the complement of a first-category subset (in particular, the subset $\mathcal{P}_{\text{reg}} \subset \mathcal{P}$ is dense by Baire’s theorem). Hence, the space $\mathcal{P}_{\text{reg}}$ of $C^{\infty}$ parameters $(\tau_{0}, \vartheta_{0}, \vec{\tau}, \vec{\vartheta})$ such that the moduli spaces $M_{W,E}^{*,0}(\tau_{0}, \vartheta_{0}, \vec{\tau}, \vec{\vartheta})$ are regular is the complement of a first-category subset of $\mathcal{P}$. From this and Corollary 5.3 we conclude:

Corollary 5.6. Let $X$ be a closed, oriented, smooth four-manifold with $C^{\infty}$ metric $g$. There is a first-category subset of the space $\mathcal{P}$, such that for all $C^{\infty}$ perturbations $(\tau_{0}, \vartheta_{0}, \vec{\tau}, \vec{\vartheta})$ in the complement of this subset, the zero locus of the section $\mathfrak{S}$ is regular and so the moduli space $M_{W,E}^{*,0}(\tau_{0}, \vartheta_{0}, \vec{\tau}, \vec{\vartheta}) = \mathfrak{S}^{-1}(0)$ is a smooth submanifold of $C_{W,E}^{*,0}$ with the expected dimension.

Remark 5.7. The same argument shows that the standard Freed-Uhlenbeck generic metrics theorems (specifically, Corollaries 4.3.15, 4.3.18, and 4.3.19 in [20] and the refinement Lemma 2.4 in [48] for the non-simply connected case) for the moduli spaces of anti-self-dual connections on an SU(2) or SO(3) bundle over $X$ continue to hold for the complement of a first-category subset of $C^{\infty}$ metrics, rather than just $C^{r}$ metrics.

5.1.3. Simultaneous transversality for the top and lower-level moduli spaces. Let $\Sigma$ be a smooth stratum of Sym$\ell(X)$. Recall from §4.5.2 that a universal choice of a sufficiently large constant $N_{b}$ guarantees that if $[A, \Phi, \mathbf{x}]$ is any point in $\bar{M}_{W,E}$ and $A$ is irreducible, then $A$ has at least one ball $B(x_j, R_0)$ which supports holonomy perturbations.

The PU(2) monopole equations cutting out the locus

$$M_{W,E-_\ell}^{*,0}|_{\Sigma} \subset C_{W,E-_\ell}^{*,0} \times \Sigma$$

from the Uhlenbeck compactification $\bar{M}_{W,E}$ are equations for triples

---

$(A, \Phi, \mathbf{x}) \in \tilde{\mathcal{C}}^{*,0}_{W,E_{-\ell}} \times \Sigma$. We can again define a $^\circ\mathcal{G}_E$-equivariant $C^\infty$ map

$$\underline{\mathfrak{S}} : \mathcal{P}^r \times \tilde{\mathcal{C}}^{*,0}_{W,E_{-\ell}} \times \Sigma \rightarrow L^2_{k-1}(\Lambda^+ \otimes \mathfrak{su}(E)) \oplus L^2_{k-1}(W^- \otimes E)$$

by setting

$$\underline{\mathfrak{S}}(\tau_0, \vartheta_0, \vec{\tau}, \vec{\vartheta}, A, \Phi, \mathbf{x})$$

$$\quad := \begin{pmatrix} F_A^+ - (\mathrm{id} + \tau_0 \otimes \mathrm{id}_{\mathfrak{su}(E)} + \vec{\tau} \cdot \vec{\mathfrak{m}}(A, \mathbf{x})) & \rho^{-1}(\Phi \otimes \Phi^*)_{00} \\ D_A \Phi + \rho(\vartheta_0)\Phi + \vec{\vartheta} \cdot \vec{\mathfrak{m}}(A, \mathbf{x}) & \Phi \end{pmatrix}.$$

The proof of Corollary 5.6 now shows that $\mathbf{M}^{*,0}_{W,E_{-\ell}} |_\Sigma \subset \mathcal{C}^{*,0}_{W,E_{-\ell}} \times \Sigma$ is a smooth submanifold of the expected dimension for generic parameters $(\tau_0, \vartheta_0, \vec{\tau}, \vec{\vartheta})$,

(5.6)

$$\dim \mathbf{M}^{*,0}_{W,E_{-\ell}} |_\Sigma = \dim M^{*,0}_{W,E_{-\ell}} + \dim \Sigma.$$

Furthermore, by considering regular values of the projection maps onto the second factors $\Sigma$, Sard’s Theorem also shows that the fibers $M^{*,0}_{W,E_{-\ell}} |_{\mathbf{x}}$ are smooth manifolds of the expected dimension for generic points $\mathbf{x} \in \operatorname{Sym}^{\ell}(X)$. Indeed, the only tangent vectors in each stratum $\Sigma$, which might not appear in the image of the projection, are those arising from the radial vector on the annuli $B(x_j, 4R_0) \backslash \bar{B}(x_j, 2R_0)$. This observation shows that the projection from $\mathbf{M}^{*,0}_{W,E_{-\ell}}$ to $\Sigma$ is transverse to certain submanifolds of $\Sigma$ which would allow dimension-counting arguments similar to those in [25]. Issues related to dimension-counting in the presence of holonomy perturbations are also discussed by Donaldson in [18, pp. 282–287]. We can now conclude the proof of our main transversality result:

Proof of Theorem 1.3, given Corollary 5.6. For the case $\ell = 0$, the transversality assertion is given by Corollary 5.6 and the dimension formula is provided by Proposition 2.28. The case $\ell > 0$ then follows from the discussion in the preceding paragraphs. q.e.d.

5.2. Smoothness of the parametrized moduli space. We prove Theorem 5.2 by showing that the $^\circ\mathcal{G}_E$-equivariant map

$$\underline{\mathfrak{S}} : \mathcal{P}^r \times \tilde{\mathcal{C}}^{*,0}_{W,E} \rightarrow L^2_{k-1}(\Lambda^+ \otimes \mathfrak{su}(E)) \oplus L^2_{k-1}(W^+ \otimes E)$$

vanishes transversely, and so the parametrized moduli space $\mathfrak{M}^{*,0}_{W,E} = \underline{\mathfrak{S}}^{-1}(0)/^\circ\mathcal{G}_E$ is a smooth Banach manifold. The broad strategy is reminiscent of that of [30, Chapter 3] and [20, §4.3.5], where the analogous result is established for the moduli space of anti-self-dual connections parametrized by the Banach space of $C^r$ (conformal classes of) metrics: our proof of surjectivity of the differential $D\underline{\mathfrak{S}}$ at a point $(\tau_0, \vartheta_0, \vec{\tau}, \vec{\vartheta}, A, \Phi)$ in the zero set $\underline{\mathfrak{S}}^{-1}(0)$ ultimately relies on the fact that, for $\Phi \neq 0$, a monopole $(A, \Phi)$ which is reducible on an admissible open subset of $X$ is necessarily reducible over all of $X$ (Theorem 5.11). If there are sections $\mathfrak{m}_{j,l,\alpha}(A)$ which are non-zero on $B(x_j,R_0)$, we say that the connection $A$ has holonomy perturbations supported on $B(x_j,R_0)$; the set $\{\mathfrak{m}_{j,l,\alpha}(A)\}_{l=1}^3$ then spans $\text{su}(E)|_{B(x_j,R_0)}$ for at least one index $\alpha$. Then an admissible open set for the pair $(A, \Phi)$ is one containing the $\bar{B}(x_j,R_0)$ for all $j$ such that $\beta_j[A] > 0$. (The supports of all the sections $\mathfrak{m}_{j,l,\alpha}(A)$ are contained in $\cup_{j=1}^{N_b}\bar{B}(x_j,R_0)$, and so any open subset of $X$ containing $\cup_{j=1}^{N_b}\bar{B}(x_j,R_0)$ is admissible.) Recall from §4.5.2 that because of our choice of constant $N_b$, if $[A, \Phi]$ is any point in $M^*_{W,E}$, then at least one ball $B(x_j,R_0)$ supports holonomy perturbations for $A$.

Theorem 5.2 is an almost immediate consequence of

**Proposition 5.8.** Suppose $(\tau_0, \vartheta_0, \vec{\tau}, \vec{\vartheta}, A, \Phi)$ is a point in $\underline{\mathfrak{S}}^{-1}(0)$ with $A$ irreducible and $\Phi \neq 0$. If $(v, \psi)$ is in the cokernel of the differential $D\underline{\mathfrak{S}}$ at the point $(\tau_0, \vartheta_0, \vec{\tau}, \vec{\vartheta}, A, \Phi)$, then $(v, \psi)|_{B(x_j,R_0)} \equiv 0$ for each ball $B(x_j,R_0)$ supporting holonomy perturbations for $A$.

We first observe that the elements of the cokernel of

$$D\underline{\mathfrak{S}} := D\underline{\mathfrak{S}}_{(\tau_0, \vartheta_0, \vec{\tau}, \vec{\vartheta}, A, \Phi)}$$

have a restricted form of the unique continuation property (sufficient for our purposes) by Aronszajn’s theorem [5]:

**Lemma 5.9.** If $(v, \psi) \in \text{Ker } D\underline{\mathfrak{S}}(D\underline{\mathfrak{S}})^*$ and $(v, \psi)|_U \equiv 0$ on some non-empty open subset $U \subset X$ containing all balls $B(x_j,R_0)$ supporting holonomy perturbations for $A$, then $(v, \psi) \equiv 0$ on $X$.

**Proof.** By hypothesis, the pair $(v, \psi)$ solves the second-order elliptic equation

$$(D\underline{\mathfrak{S}})(D\underline{\mathfrak{S}})^*(v, \psi) = 0 \quad \text{on } X,$$

where the Laplacian $D\underline{\mathfrak{S}} = (D\underline{\mathfrak{S}}_1,D\underline{\mathfrak{S}}_2)$, given by equations (4.3) and (4.4), has $C^{r-1}$ coefficients and $(v, \psi)$ is at least $C^{r+1}$. Also, $(v, \psi) \equiv 0$ on the set of closed balls supporting holonomy perturbations,

$$\bar{B}_I(A) := \bigcup_{j \in I(A)} \bar{B}(x_j,R_0),$$

where $I(A) := \{j : 1 \leq j \leq N_b, \beta_j[A] > 0\}$, and $A|_{B(x_j,2R_0)}$ is irreducible. Now, on the subset $X - B_{I(A)}$ where all of the holonomy perturbations and especially their derivatives with respect to $A$ vanish (see their definition in §2.5.2), the Laplacian $(D\mathfrak{S})(D\mathfrak{S})^*$ is a purely differential operator. In particular, it extends to a differential operator with $C^{r-1}$ coefficients over $X$, say $(D\mathfrak{S}^0)(D\mathfrak{S}^0)^*$, given by the linearized PU(2) monopole equations (5.3) and (5.4) with all terms involving holonomy perturbations and their derivatives set equal to zero. On the other hand, the pair $(v,\psi)$ also solves the resulting second-order elliptic differential equation

$(D\mathfrak{S}^0)(D\mathfrak{S}^0)^*(v,\psi) = 0$ on $X$,