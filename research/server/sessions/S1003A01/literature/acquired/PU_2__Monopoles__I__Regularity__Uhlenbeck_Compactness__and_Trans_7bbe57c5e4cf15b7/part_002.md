---
retention_scope: session
part: 2
total_parts: 6
---

[Part 2/6 of: PU(2) Monopoles. I: Regularity, Uhlenbeck Compactness, and Transversality]

Proof. Suppose that $(A_i,\Phi_i) \in \mathbf{B}_{A_0,\Phi_0}(\varepsilon)$ for $i=1,2$ and that $[A_1,\Phi_1] = [A_2,\Phi_2] \in \mathcal{C}_{W,E}$, so that $u(A_1,\Phi_1) = (A_2,\Phi_2)$ for some $u \in \circ^\circ G_E$.

Since $u(A_0) = A_0 - (d_{A_0}u)u^{-1}$, we see that $u \in \text{Stab}_{A_0,\Phi_0}$ if and only if $d_{A_0,\Phi_0}^0 u = (d_{A_0}u,-u\Phi_0) = (0,-\Phi_0)$ or, equivalently, if and only if $d_{A_0,\Phi_0}^0(u-\text{id}_E) = 0$, since $\text{id}_E \in \text{Stab}_{A_0,\Phi_0}$. Here, we view $u \in L_{k+1}^2(\mathfrak{gl}(E))$ via the isometric embedding $\circ^\circ G_E \subset L_{k+1}^2(\mathfrak{gl}(E))$ and write

$$u - \text{id}_E = u_0 - \gamma,$$

where $u_0 \in (\text{Ker } d_{A_0,\Phi_0}^{0})^\perp$ and $\gamma \in \text{Ker } d_{A_0,\Phi_0}^{0}$. Our first task is to estimate $\|u - \text{id}_E\|_{L_{3,A_0}^2}$.

By assumption, $d_{A_0,\Phi_0}^0 \gamma = (d_{A_0}\gamma,\gamma\Phi) = 0$, so $d_{A_0}\gamma = 0$ and $\gamma\Phi_0 = 0$. Since $u(A_1) \equiv A_1 - (d_{A_1}u)u^{-1} = A_2$, we have

$$A_2u = A_1u - d_{A_1}u = A_1u - d_{A_0}u - [A_1-A_0],$$

and therefore, using $d_{A_0}\text{id}_E = 0 = d_{A_0}\gamma$, we have

$$d_{A_0}u_0 = d_{A_0}u = u(A_1-A_0) - (A_2-A_0)u.$$

---

As $d_{A_0}^* (A_i - A_0) = (\cdot \Phi_0)^* (\Phi_i - \Phi_0)$, we obtain

$$d_{A_0}^* d_{A_0} u_0 = - * (d_{A_0} u \wedge * (A_1 - A_0)) + ud_{A_0}^* (A_1 - A_0)
- (d_{A_0}^* (A_2 - A_0)) u + * (*(A_2 - A_0) \wedge d_{A_0} u)
= - * (d_{A_0} u_0 \wedge * (A_1 - A_0)) + u(\cdot \Phi_0)^* (\Phi_1 - \Phi_0)
- ((\cdot \Phi_0)^* (\Phi_2 - \Phi_0)) u + * (*(A_2 - A_0) \wedge d_{A_0} u_0).$$

We define the Laplacian $\Delta_{A_0,\Phi_0}^0$ by setting

$$\Delta_{A_0,\Phi_0}^0 = d_{A_0,\Phi_0}^{0,*} d_{A_0,\Phi_0}^0 = d_{A_0}^* d_{A_0} + (\cdot \Phi_0)^* \Phi_0.$$

Now $u_0 = u - \mathrm{id}_E + \gamma$ and $d_{A_0} \mathrm{id}_E = 0 = d_{A_0} \gamma$ and $\gamma \Phi_0 = 0$ so, using $u \Phi_1 = \Phi_2$, we obtain

$$\Delta_{A_0,\Phi_0}^0 u_0 = \Delta_{A_0,\Phi_0}^0 (u - \mathrm{id}_E + \gamma)
= d_{A_0}^* d_{A_0} (u - \mathrm{id}_E + \gamma) + (\cdot \Phi_0)^* (u - \mathrm{id}_E) \Phi_0
= d_{A_0}^* d_{A_0} u + (\cdot \Phi_0)^* (u \Phi_0 - u \Phi_1 + u \Phi_1 - \Phi_0)
= d_{A_0}^* d_{A_0} u_0 + (\cdot \Phi_0)^* (u (\Phi_0 - \Phi_1) + (\Phi_2 - \Phi_0)).$$

Our assumption that $(A_i, \Phi_i) \in \mathbf{B}_{A_0,\Phi_0}(\varepsilon)$ and the embeddings $L_k^2 \subset L_2^2$ imply that for $i = 1, 2$ we have

$$\|(A_i, \Phi_i) - (A_0, \Phi_0)\|_{L_2^2,A_0} \leq \|(A_i, \Phi_i) - (A_0, \Phi_0)\|_{L_2^k,A_0} < \varepsilon.$$

Since $u_0 \in (\mathrm{Ker} d_{A_0,\Phi_0}^0)^\perp$, the standard elliptic estimate for the Laplacian $\Delta_{A_0,\Phi_0}^0$, the fact that $|u| = 1$ as $u \in {}^\circ G_E$, the Sobolev embedding $L_2^2 \subset L^q$, $2 \leq q < \infty$, and multiplication $L_2^2 \times L_2^2 \rightarrow L_1^2$, and our expression for $d_{A_0}^* d_{A_0} u = d_{A_0}^* d_{A_0} u_0$ combine to give

$$\|u_0\|_{L_3^2,A_0} \leq C \|\Delta_{A_0,\Phi_0}^0 u_0\|_{L_1^2,A_0}
\leq C \|d_{A_0}^* d_{A_0} u_0\|_{L_1^2,A_0} + C \|(\cdot \Phi_0)^* (u(\Phi_0 - \Phi_1) + (\Phi_2 - \Phi_0))\|_{L_1^2,A_0}
\leq C \|d_{A_0}^* d_{A_0} \left(\|A_1 - A_0\|_{L_2^2,A_0} + \|A_2 - A_0\|_{L_2^2,A_0}\right)
+ C \|u\|_{L_2^2,A_0} \|\Phi_0\|_{L_2^2,A_0} \left(\|\Phi_1 - \Phi_0\|_{L_2^2,A_0} + \|\Phi_2 - \Phi_0\|_{L_2^2,A_0}\right)
\leq C \|u_0\|_{L_3^2,A_0} \varepsilon + C \|u\|_{L_2^2,A_0} \|\Phi_0\|_{L_2^2,A_0} \varepsilon
\leq C \|u_0\|_{L_3^2,A_0} \varepsilon + C \|\Phi_0\|_{L_2^2,A_0} \varepsilon,$$ for some constant $C = C(A_0, \Phi_0)$. For small enough $\varepsilon$ we can rearrange the preceding inequality and use the Sobolev embedding $L^2_3 \subset C^0$ to yield

$$\|u_0\|_{L^2_3,A_0} \leq C\|\Phi_0\|_{L^2_2,A_0}\varepsilon \text{ and } \|u_0\|_{C^0} \leq C\|\Phi_0\|_{L^2_2,A_0}\varepsilon.$$

Therefore, as $|u| = 1$, we have the pointwise bounds

$$1 - |u_0| \leq |\mathrm{id}_E - \gamma| \leq 1 + |u_0|,$$

and thus, for $\varepsilon$ small, $|\mathrm{id}_E - \gamma| > 0$; the pointwise norm of $z = |\mathrm{id}_E - \gamma|$ is constant since $d_A_0(\mathrm{id}_E - \gamma) = 0$. Consequently, $\gamma_0 \equiv z^{-1}(\mathrm{id}_E - \gamma)$ lies in $^\circ G_E$: clearly, $d_A_0\gamma_0 = 0$, so $\gamma_0 \in \mathrm{Stab}_A$. If $\Phi_0 \equiv 0$, we trivially have $\gamma_0 \in \mathrm{Stab}_\Phi_0$. If $\Phi_0 \neq 0$, then the equalities $|\gamma_0\Phi_0| = |\Phi_0|$ (as $\gamma_0$ is a unitary gauge transformation) and $\gamma_0\Phi_0 = z^{-1}(\mathrm{id}_E - \gamma)\Phi_0 = z^{-1}\Phi_0$, so $|\gamma_0\Phi_0| = z^{-1}|\Phi_0|$ implying that $z = 1$ (it is enough to have equality of $L^2$ norms here as $z$ is constant). Hence, we also have $\gamma_0 \in \mathrm{Stab}_\Phi_0$ and in particular, $\gamma_0 \in \mathrm{Stab}_{A_0,\Phi_0} = \mathrm{Stab}_{A_0} \cap \mathrm{Stab}_\Phi_0$.

We now write $\gamma_0^{-1}u = \gamma_0^{-1}u_0 + \gamma_0^{-1}(\mathrm{id}_E - \gamma) = \gamma_0^{-1}u_0 + z\mathrm{id}_E$, so that

$$\gamma_0^{-1}u - \mathrm{id}_E = (z - 1)\mathrm{id}_E + \gamma_0^{-1}u_0.$$

Clearly, $(z - 1)\mathrm{id}_E \in \mathrm{Ker} d^0_{A_0,\Phi_0}$ by the remarks of the last paragraph, while $\gamma_0^{-1}u_0 \in (\mathrm{Ker} d^0_{A_0,\Phi_0})^\perp$ since $u_0 \in (\mathrm{Ker} d^0_{A_0,\Phi_0})^\perp$ and $\gamma_0^{-1} \in \mathrm{Stab}_{A_0,\Phi_0}$. Similarly, $\gamma_0^{-1}u(A_1,\Phi_1) = \gamma_0^{-1}(A_2,\Phi_2) \in \mathbf{B}_{A_0,\Phi_0}(\varepsilon)$, as the neighborhood $\mathbf{B}_{A_0,\Phi_0}(\varepsilon)$ is $\mathrm{Stab}_{A_0,\Phi_0}$-invariant. Thus, replacing $u$ by $\gamma_0^{-1}u$ and $(A_2,\Phi_2)$ by $(A_2,\tilde{\Phi}_2) \equiv \gamma_0^{-1}(A_2,\Phi_2)$ in our $L^2_{3,A_0}$ estimate for $u_0$ yields

$$\|\gamma_0^{-1}u_0\|_{L^2_{3,A_0}} \leq C\|\Phi_0\|_{L^2_{2,A_0}}\varepsilon,$$

while $|z - 1| \leq \|u_0\|_{C^0} \leq C\|\Phi_0\|_{L^2_{2,A_0}}\varepsilon$, so we find that

$$\|\gamma_0^{-1}u - \mathrm{id}_E\|_{L^2_{3,A_0}} \leq C\|\Phi_0\|_{L^2_{2,A_0}}\varepsilon.$$

If $\varepsilon$ is small enough that $C\|\Phi_0\|_{L^2_{2,A_0}}\varepsilon < \delta$, where $\delta = \delta(A_0,\Phi_0)$ is the constant of Claim 2.11 with $k = 2$, then $\gamma_0^{-1}u \in \mathrm{Stab}_{A_0,\Phi_0}$ and so $u$ lies in $\mathrm{Stab}_{A_0,\Phi_0}$, as desired. q.e.d.

**Claim 2.13.** The quotient space $\mathcal{C}_{W,E}$ is Hausdorff.

Proof. Let $\Gamma$ be the subspace $\{(A,\Phi), u(A,\Phi)\}: (A,\Phi) \in \tilde{\mathcal{C}}_{W,E}$ and $u \in^\circ G_E$ of $\tilde{\mathcal{C}}_{W,E} \times \tilde{\mathcal{C}}_{W,E}$. If $\{(A_\alpha,\Phi_\alpha), u_\alpha(A_\alpha,\Phi_\alpha)\}$ is a sequence in $\Gamma$ which converges in $L_k^2$ to a point $\{(A_\infty, \Phi_\infty), (B_\infty, \Psi_\infty)\}$, then Lemma 2.7 implies that there is a subsequence $\{\alpha'\} \subset \{\alpha\}$ such that $\{u_\alpha\}$ converges in $L_{k+1}^2$ to $u_\infty \in^\circ G_E$ and $u_\infty(A_\infty) = B_\infty$. But then $u_{\alpha'} \Phi_{\alpha'}$ converges in $L_k^2$ to $u_\infty \Phi_\infty$ and so $\Psi_\infty = u_\infty \Phi_\infty$. Thus, $(B_\infty, \Psi_\infty) = u_\infty(A_\infty, \Phi_\infty)$ for some $u_\infty \in^\circ G_E$, and therefore $\Gamma$ is closed. Hence the quotient $\tilde{C}_{W,E}/^\circ G_E$ is Hausdorff. q.e.d.

Claim 2.13 gives Assertion (1) of the proposition. Thus Assertions (2), (3), and (4) now follow from the preceding arguments and Claim 2.12. This completes the proof of the proposition. q.e.d.

Remark 2.14. (1) Alternatively, one can show that the quotient $L_k^2$ topology on $C_{W,E}$ is metrizable via the $L^2$ metric (exactly as in [20, Lemma 4.2.4]) and thus $C_{W,E}$ is Hausdorff.

(2) As Mrowka pointed out to us, one can sharpen the assertions of Proposition 2.8, at least for the quotient space $B_E$: one finds that charts are provided by $L^4$-balls in Ker $d_A^*$ rather than the much smaller $L_k^2,A_0$-balls usually employed; see [22].

It is convenient to extract the following global, Coulomb gauge-fixing result (analogous to Proposition 2.3.4 in [20]) which we established in the course of proving Proposition 2.8:

Lemma 2.15. Let $X$ be a closed, oriented, Riemannian spin$^c$ fourmanifold and let $E$ be a Hermitian vector bundle over $X$. Suppose that $k \geq 2$ is an integer and that $(A_0,\Phi_0) \in \tilde{C}_{W,E}$. Then there is a positive constant $\varepsilon = \varepsilon(A_0,\Phi_0,k)$ such that for any $(A,\Phi) \in \tilde{C}_{W,E}$ with

$$\|(A,\Phi) - (A_0,\Phi_0)\|_{L_k^2,A_0}(X) < \varepsilon,

$$d_{A_0,\Phi_0}^{0,*} (u(A,\Phi) - (A_0,\Phi_0)) = 0.$$

2.3. Connections on SO(3) bundles and groups of gauge transformations. For some local patching arguments over simply-connected open regions $Y \subset X$ in §3 and §4 it is very useful to be able to lift gauge transformations in $G_{\text{su}(E)}(Y)$ to gauge transformations in $G_E(Y)$. The following result tells us that this is always possible when $Y$ is simply connected; it is an extension of Theorem IV.3.1 in [61] from SU(2) to U(2) bundles.

---

Proposition 2.16. Let E be a Hermitian two-plane bundle over a connected manifold X. Then there is an exact sequence

$$1 \rightarrow \{\pm \mathrm{id}_E\} \rightarrow G_E \rightarrow G_{\mathrm{su}(E)} \rightarrow H^1(X; \mathbb{Z}/2\mathbb{Z})$$.

Proof. Let P be the U(2) principal bundle underlying E so $P^{\mathrm{ad}} = P/S_Z^1$ is the SO(3) principal bundle underlying $\mathfrak{su}(E)$. We can view elements of $G_E$ as maps u : P → SU(2) satisfying $u(pg) = g^{-1}u(p)g$ for p ∈ P and g ∈ U(2), and similarly for elements of $G_{\mathrm{su}(E)}$. The map $G_E \rightarrow G_{\mathrm{su}(E)}$ is then given by u → Adu. Because X is connected, the kernel of this map is {±$\mathrm{id}_E$}, giving the exactness of all but the last terms in the sequence.

Let $\nu_2 \in H^1(\mathrm{SO}(3); \mathbb{Z}/2\mathbb{Z})$ be the non-trivial cohomology class given by the double cover SU(2) → SO(3). Then a map u : V → SO(3) lifts to SU(2) if and only if $u^*\nu_2 = 0$. We would like to define the map $\alpha : G_{\mathrm{su}(E)} \rightarrow H^1(X; \mathbb{Z}/2\mathbb{Z})$ by $\alpha(u) = u^*\nu_2$. It is not immediately clear that $\alpha(u)$ actually lies in $H^1(X; \mathbb{Z}/2\mathbb{Z})$. The homotopy exact sequence

$$\pi_1(\mathrm{SO}(3)) \rightarrow \pi_1(P^{\mathrm{ad}}) \rightarrow \pi_1(X) \rightarrow 1$$

gives an exact sequence in cohomology $H^1(\cdot; \mathbb{Z}/2\mathbb{Z}) = \operatorname{Hom}(\pi_1(\cdot), \mathbb{Z}/2\mathbb{Z})$,

$$1 \rightarrow H^1(X; \mathbb{Z}/2\mathbb{Z}) \rightarrow H^1(P^{\mathrm{ad}}; \mathbb{Z}/2\mathbb{Z}) \rightarrow H^1(\mathrm{SO}(3); \mathbb{Z}/2\mathbb{Z}).$$

Thus $u^*\nu_2$ is pulled back from a unique element of $H^1(X; \mathbb{Z}/2\mathbb{Z})$ if and only if $i_x^*u^*\nu_2 = 0$, where i_x : SO(3) → P^{\mathrm{ad}} is the inclusion of a fiber.

Because $u^*\nu_2$ depends only on the homotopy class of u, the map $\alpha$ is constant on connected components. Let $G_{\mathrm{su}(E)}^x$ be the subgroup of elements of $G_{\mathrm{su}(E)}$ which are the identity over x ∈ X. The exact sequence of groups

$$1 \rightarrow G_{\mathrm{su}(E)}^x \rightarrow G_{\mathrm{su}(E)} \rightarrow \mathrm{SO}(3) \rightarrow 1$$

and the corresponding exact sequence of homotopy groups ($\pi_0$ to be specific) show that the inclusion $G_{\mathrm{su}(E)}^x$ induces a surjection of connected components. Now if u ∈ $G_{\mathrm{su}(E)}^x$ then $i_x^*u^*\nu_2 = 0$, and so $i_xu^*\nu_2 = 0$ for all u ∈ $G_{\mathrm{su}(E)}$. This implies that the map $\alpha$ takes values in $H^1(X; \mathbb{Z}/2\mathbb{Z})$.

By the defining property of $\nu_2$, we have $\alpha(u) = 0$ if and only if there is a lift of u to SU(2). Because {±$\mathrm{id}_E$} is central, any Ad-equivariant map $\tilde{u}: P \rightarrow SU(2)$ descends to $P^{\mathrm{ad}} \rightarrow SU(2)$. Thus u ∈ $G_{\mathrm{su}(E)}$ is induced by some $\tilde{u} \in G_E$ if and only if $\alpha(u) = 0$. q.e.d.

---

Remark 2.17. One can also show that the map

$$G_{\text{su}(E)} \rightarrow H^1(X; \mathbb{Z}/2\mathbb{Z})$$

is surjective.

2.4. Quadratic forms for coupled spinor bundles. Give $\mathfrak{gl}(E)$ (respectively, $\mathfrak{gl}(W^{\pm})$) the Hermitian fiber inner product and norm

$$\langle M, N \rangle := \frac{1}{2} \operatorname{tr}(M^\dagger N) \quad \text{and} \quad |M|^2 = \langle M, M \rangle,$$

for $M, N \in \Omega^0(\mathfrak{gl}(E))$ (respectively, $\mathfrak{gl}(W^{\pm})$), so that $|\mathrm{id}_E| = 1$, etc. If $\Phi \in \Omega^0(W^+ \otimes E)$, then $\Phi^* \in \Omega^0((W^+ \otimes E)^*) = \Omega^0((W^+)^* \otimes E^*)$ is defined by $\Phi^*(\Psi) := \langle \Psi, \Phi \rangle$ for $\Psi \in \Omega^0(W^+ \otimes E)$.

With respect to the induced Hermitian fiber inner products on $\mathfrak{gl}(W^+)$ and $\mathfrak{gl}(E)$, we have fiber-wise orthogonal direct sums, $\mathfrak{gl}(W^+) = \mathbb{C}\mathrm{id}_{W^+} \oplus \mathfrak{sl}(W^+)$, and similarly for $\mathfrak{gl}(E)$ and thus $\mathfrak{gl}(W^+) \otimes_{\mathbb{C}} \mathfrak{gl}(E)$. Let $\pi_{W^+}$ (respectively, $\pi_E$) be the fiber-wise orthogonal projection from $\mathfrak{gl}(W^+)$ (respectively, $\mathfrak{gl}(E))$ onto the subspace $\mathfrak{sl}(W^+)$ (respectively, $\mathfrak{sl}(E)$), so that

$$\pi_{W^+} M := M - \frac{1}{2} \operatorname{tr} M \mathrm{id}_{W^+} \quad \text{and} \quad \pi_E N := N - \frac{1}{2} \operatorname{tr} N \mathrm{id}_E$$

are the projection onto the traceless components of $M \in \mathfrak{gl}(W^+)$ and $N \in \mathfrak{gl}(E)$, and

$$\pi_{\perp W^+} M := \frac{1}{2} \operatorname{tr} M \mathrm{id}_{W^+} \quad \text{and} \quad \pi_{\perp E}^+ N := \frac{1}{2} \operatorname{tr} N \mathrm{id}_E$$

are the projections onto the trace components of $M \in \mathfrak{gl}(W^+)$ and $N \in \mathfrak{gl}(E)$. The orthogonal projection from $\mathfrak{gl}(W^+) \otimes_{\mathbb{C}} \mathfrak{gl}(E)$ onto $\mathfrak{sl}(W^+) \otimes_{\mathbb{C}} \mathfrak{sl}(E)$ is obtained by writing $\pi_{W^+} = \mathrm{id}_{W^+} - \pi_{\perp W^+}$ and $\pi_E = \mathrm{id}_E - \pi_{\perp E}$, so that

$$\pi_{W^+} \otimes \pi_E = \mathrm{id}_{W^+} \otimes \mathrm{id}_E - \left( \pi_{W^+} \otimes \pi_{\perp E} + \pi_{\perp W^+} \otimes \pi_E \right) + \pi_{\perp W^+} \otimes \pi_{\perp E}.$$

Consequently, if $\phi \in \Omega^0(W^+)$ and $\Phi \in \Omega^0(W^+ \otimes E)$, we may define

$$(\phi \otimes \phi^*)_0 := \pi_{W^+}(\phi \otimes \phi^*),$$

$$(\Phi \otimes \Phi^*)_{00} := (\pi_{W^+} \otimes \pi_E)(\Phi \otimes \Phi^*).$$

Note that

$$
\mathfrak{gl}(W^+) \otimes_{\mathbb{C}} \mathfrak{gl}(E) = u(W^+) \otimes_{\mathbb{R}} u(E) + iu(W^+) \otimes_{\mathbb{R}} u(E).
$$

Plainly, $(\phi \otimes \phi^*)_0$ is a section of $\mathfrak{sl}(W^+) \cap iu(W^+) = i\mathfrak{su}(W^+)$. The following identities are now well-known [47], [77, Chapter 8]:

---

Lemma 2.18. For every $\phi \in \Omega^0(W^+)$ or $\Omega^0(E)$, $T \in \Omega^0(\mathfrak{sl}(W^+))$, and $\eta \in \Omega^2(X,\mathbb{C})$, the following hold. The endomorphism $(\phi \otimes \phi^*)_0$ is a section of $\Omega^0(i\mathfrak{su}(W^+))$ and satisfies:

(1) $|(\phi \otimes \phi^*)_0|^2 = \frac{1}{4}|\phi|^4,$

(2) $|\rho(\eta)|^2 = 2|\eta^+|^2$ and $|\rho^{-1}T|^2 = \frac{1}{2}|T|^2.$

Similarly, $\Phi \otimes \Phi^*$ is a section of $i\mathfrak{u}(W^+ \otimes_{\mathbb{C}} E) = \mathfrak{u}(W^+) \otimes_{\mathbb{R}} \mathfrak{u}(E)$ and $(\Phi \otimes \Phi^*)_{00}$ is a section of $\mathfrak{su}(W^+) \otimes_{\mathbb{R}} \mathfrak{su}(E)$. We then have the following analogue of Lemma 2.18:

Lemma 2.19. For every $\Phi \in \Omega^0(W^+ \otimes E)$ and

$$M \in \Omega^0(\mathfrak{gl}(W^+ \otimes E)),$$

the following identities hold:

(1) $\langle \Phi \otimes \Phi^*, M \rangle = \frac{1}{2}\langle M\Phi, \Phi\rangle,$

(2) $\left(\frac{5}{4} - \frac{1}{\sqrt{2}}\right)|\Phi|^4 \leq \langle (\Phi \otimes \Phi^*)_{00}\Phi, \Phi \rangle \leq \frac{1}{\sqrt{2}}|\Phi|^4,$

(3) $\left(\frac{5}{8} - \frac{1}{2\sqrt{2}}\right)|\Phi|^4 \leq |(\Phi \otimes \Phi^*)_{00}|^2 \leq \frac{1}{2\sqrt{2}}|\Phi|^4.$

Proof. Using $\Phi = c^a\Phi^a$ (we employ the summation convention), so $M\Phi = c^aM\Phi^a$ and $\Phi^*\Phi^a = \langle \Phi^a, \Phi \rangle = \bar{c}^a$, we have

$$\langle \Phi \otimes \Phi^*, M \rangle = \frac{1}{2}\operatorname{tr}((\Phi \otimes \Phi^*)^\dagger M) = \frac{1}{2}\langle (\Phi \otimes \Phi^*)M\Phi^a, \Phi^a \rangle$$

$$= \frac{1}{2}\langle M\Phi^a, (\Phi \otimes \Phi^*)\Phi^a \rangle = \frac{1}{2}\langle M\Phi^a, \Phi(\Phi^*\Phi^a) \rangle$$

$$= \frac{1}{2}\langle M\Phi^a, \bar{c}^a\Phi \rangle = \frac{1}{2}\langle c^aM\Phi^a, \Phi \rangle = \frac{1}{2}\langle M\Phi, \Phi \rangle,$$

which gives (1). Next, we see that

$$|\Phi \otimes \Phi^*|^2 = \langle \Phi \otimes \Phi^*, \Phi \otimes \Phi^* \rangle = \frac{1}{2}\langle (\Phi \otimes \Phi^*)\Phi, \Phi \rangle$$

$$= \frac{1}{2}|\Phi|^2\langle \Phi, \Phi \rangle = \frac{1}{2}|\Phi|^4,$$

and so the upper bound in (2) is obtained by

$$|\langle (\Phi \otimes \Phi^*)_{00}\Phi, \Phi \rangle| \leq |(\Phi \otimes \Phi^*)_{00}\|\Phi|^2 \leq |\Phi \otimes \Phi^*\|\Phi|^2$$

$$\leq (1/\sqrt{2})|\Phi|^4 < \frac{3}{4}|\Phi|^4,$$

where we use the fact that $(\cdot)_{00} = \pi_W^+ \otimes \pi_E$ is an orthogonal projection to obtain the second inequality.

---

To obtain the lower bound in (2), suppose that $\Phi = \phi^a \otimes \xi^a$ (implied summation), where $\{\phi^a\} \subset \Omega^0(W^+)$ and $\{\xi^a\} \subset \Omega^0(E)$, then $\Phi \otimes \Phi^* = (\phi^a \otimes \phi^{b,*}) \otimes (\xi^a \otimes \xi^{b,*})$ and

$$
(\pi^\perp_{W^+} \otimes \pi^\perp_E)(\Phi \otimes \Phi^*) = \pi^\perp_{W^+}(\phi^a \otimes \phi^{b,*}) \otimes \pi^\perp_E(\xi^a \otimes \xi^{b,*})
$$
$$
= \frac{1}{4}\operatorname{tr}(\phi^a \otimes \phi^{b,*})\operatorname{tr}(\xi^a \otimes \xi^{b,*})\operatorname{id}_{W^+ \otimes E}
$$
$$
= \frac{1}{4}\langle \phi^a, \phi^b \rangle \langle \xi^a, \xi^b \rangle\operatorname{id}_{W^+ \otimes E}
$$
$$
= \frac{1}{4}\langle \phi^a \otimes \xi^a, \phi^b \otimes \xi^b \rangle\operatorname{id}_{W^+ \otimes E}
$$
$$
= \frac{1}{4}\langle \Phi, \Phi \rangle\operatorname{id}_{W^+ \otimes E}.
$$

Using the last identity together with $(\Phi \otimes \Phi^*) \Phi = \Phi \langle \Phi, \Phi \rangle = \Phi |\Phi|^2$ and (2.11) gives

$$
\langle (\Phi \otimes \Phi^*)_{00} \Phi, \Phi \rangle = \langle (\Phi \otimes \Phi^*) \Phi, \Phi \rangle
$$
$$
- \langle (\pi^\perp_{W^+} \otimes \pi_E + \pi_{W^+} \otimes \pi^\perp_E)(\Phi \otimes \Phi^*) \Phi, \Phi \rangle
$$
$$
+ \langle \frac{1}{4}| \Phi|^2 \Phi, \Phi \rangle
$$
$$
= \frac{5}{4}| \Phi|^4 - \langle (\pi^\perp_{W^+} \otimes \pi_E + \pi_{W^+} \otimes \pi^\perp_E)(\Phi \otimes \Phi^*) \Phi, \Phi \rangle.
$$

But $\pi^\perp_{W^+} \otimes \pi_E + \pi_{W^+} \otimes \pi^\perp_E$ is just the orthogonal projection onto the middle two factors of the orthogonal decomposition of $\mathfrak{gl}(W^+) \otimes_{\mathbb{C}} \mathfrak{gl}(E)$, so

$$\left| \langle (\pi^\perp_{W^+} \otimes \pi_E + \pi_{W^+} \otimes \pi^\perp_E)(\Phi \otimes \Phi^*) \Phi, \Phi \rangle \right|
\leq \left| (\pi^\perp_{W^+} \otimes \pi_E + \pi_{W^+} \otimes \pi^\perp_E)(\Phi \otimes \Phi^*) \right| |\Phi|^2
\leq |\Phi \otimes \Phi^*\|\Phi|^2 \leq (1/\sqrt{2})|\Phi|^4 < \frac{3}{4}| \Phi|^4,

and therefore

$$| \langle (\Phi \otimes \Phi^*)_{00} \Phi, \Phi \rangle | \geq \frac{5}{4}| \Phi|^4 - (1/\sqrt{2})|\Phi|^4 > \frac{1}{2}| \Phi|^4.$$

Consequently, using $(\Phi \otimes \Phi^*)_{00}^{\dagger} = (\Phi \otimes \Phi^*)_{00}$, we have

$\frac{1}{2}\langle (\Phi \otimes \Phi^*)_{00} \Phi, \Phi \rangle = \langle (\Phi \otimes \Phi^*)_{00}, \Phi \otimes \Phi^* \rangle = \langle (\Phi \otimes \Phi^*)_{00}, (\Phi \otimes \Phi^*)_{00} \rangle$
$= |(\Phi \otimes \Phi^*)_{00}|^2,$

which gives (3). q.e.d.

The fact that $|(\Phi \otimes \Phi^*)_0|^2 \geq \frac{1}{4}| \Phi|^4$, for $\Phi \in \Omega^0(W^+ \otimes E)$, is used in §4 to show that the moduli space of PU(2) monopoles has an Uhlenbeck compactification. (The analogous equality, $|(\phi \otimes \phi^*)_0|^2 = \frac{1}{4}|\phi|^4$ for $\phi \in \Omega^0(W^+)$, is used in [47], [98] to show that the moduli space of Seiberg-Witten monopoles is compact.)

We adapt some terminology from the proofs of Proposition 3.4 in [30] and Lemma 4.3.25 in [20] which we will need for our proof of transversality for the PU(2) monopole moduli space in §5:

**Definition 2.20.** The rank of a section $\Phi \in \Omega^0(W^\pm \otimes E)$ at a point $x \in X$ is the rank of $\Phi|_x$ considered as a complex linear map $(W^\pm)^*|_x \rightarrow E|_x$ (that is, its rank as a complex two-by-two matrix). We say that $\Phi$ is rank one on a subset $U \subset X$ if it has rank less than or equal to one at all points in $U$. Similarly, for $v \in \Omega^0(\Lambda^+(T^*X) \otimes \mathfrak{su}(E))$, the rank of $v$ at a point $x \in X$ is the rank of $v$ considered as a real linear map from $\Lambda^+(TX)|_x \rightarrow \mathfrak{su}(E)|_x$ (that is, its rank as a real three-by-three matrix). The rank of $v$ on a set $U \subset X$ is the maximum rank of $v|_x$ over all points $x \in U$. Finally, for $M \in \Omega^0(\mathfrak{su}(W^+) \otimes \mathfrak{su}(E))$, the rank of $M$ at a point $x \in X$ is the rank of $M$ considered as a real linear map from $\mathfrak{su}(W^+)^*|_x \rightarrow \mathfrak{su}(E)|_x$ (again, its rank as a real three-by-three matrix). The rank of $M$ on a set $U \subset X$ is the maximum rank of $M|_x$ over all points $x \in U$.

For the proof of Lemma 2.21 below we shall need a simple linear algebra identity. Suppose that $\Phi = \phi \otimes \xi$, for some $\phi \in \Omega^0(W^+)$ and $\xi \in \Omega^0(E)$, and that $\Psi = \psi \otimes \zeta$, with $\phi \in \Omega^0(W^+)$ and $\xi \in \Omega^0(E)$. Then

$$\Phi \otimes \Psi^* = (\phi \otimes \xi) \otimes (\psi \otimes \zeta)^* = (\phi \otimes \psi^*) \otimes (\xi \otimes \zeta^*) \in \mathfrak{gl}(W^+) \otimes_{\mathbb{C}} \mathfrak{gl}(E).$$

Writing $B \in \mathfrak{gl}(W^+)$ (or $\mathfrak{gl}(E)$) as $B = B_h + B_s$, where $B_h = \frac{1}{2}(B + B^\dagger)$ is Hermitian and $B_s = \frac{1}{2}(B - B^\dagger)$ is skew-Hermitian, we have

$$\Phi \otimes \Psi^* = \frac{1}{4}(\phi \otimes \psi^* + \psi \otimes \phi^*) \otimes (\xi \otimes \zeta^* + \zeta \otimes \xi^*)$$

$$+ \frac{1}{4}(\phi \otimes \psi^* - \psi \otimes \phi^*) \otimes (\xi \otimes \zeta^* - \zeta \otimes \xi^*)$$

$$+ \frac{1}{4}(\phi \otimes \psi^* + \psi \otimes \phi^*) \otimes (\xi \otimes \zeta^* - \zeta \otimes \xi^*)$$

and similarly for $\Psi \otimes \Phi^*$. Therefore,

$$\Phi \otimes \Psi^* + \Psi \otimes \Phi^* = \frac{1}{2}(\phi \otimes \psi^* + \psi \otimes \phi^*) \otimes (\xi \otimes \zeta^* + \zeta \otimes \xi^*)$$

$$+ \frac{1}{2}(\phi \otimes \psi^* - \psi \otimes \phi^*) \otimes (\xi \otimes \zeta^* - \zeta \otimes \xi^*)$$

(2.13)

---

We shall need the following elementary observation in our proof of transversality for the moduli space of PU(2) monopoles in §5. Note that as $\rho : \Lambda^+ \rightarrow \mathfrak{su}(W^+)$ is an isomorphism, the rank of a section $v$ of $\Lambda^+ \otimes \mathfrak{su}(E)$ is equal to the rank of the section $\rho(v)$ of $\mathfrak{su}(W^+) \otimes \mathfrak{su}(E)$.

Lemma 2.21. If $\Phi \in C^0(W^+ \otimes E)$ and $x \in X$, then the following hold:

(1) Rank$_R(\Phi(x) \otimes \Phi^*(x))_{00} = 1$ if and only if Rank$_C\Phi(x) = 1$,

(2) Rank$_R(\Phi(x) \otimes \Phi^*(x))_{00} = 3$ if and only if Rank$_C\Phi(x) = 2$.

Proof. For convenience we write $\Phi$, $W^+$, and $E$ for $\Phi|_x$, $W^+|_x$, and $E|_x$. If $\Phi \in \text{Hom}(W^+, E)$ has complex rank one, we can write $\Phi = \phi \otimes \xi$, for $\phi \in W^+$ and $\xi \in E$. Then $(\Phi \otimes \Phi^*)_{00} = -i(\phi \otimes \phi^*)_0 \otimes i(\xi \otimes \xi^*)_0$ and so $(\Phi \otimes \Phi^*)_{00} \in \text{Hom}(\mathfrak{su}(W^+), \mathfrak{su}(E))$ has real rank one.

Conversely, suppose $(\Phi \otimes \Phi^*)_{00}$ has real rank one. Let $\{\xi_1, \xi_2\}$ be an orthonormal basis for $E$ and write $\Phi = \phi_1 \otimes \xi_1 + \phi_2 \otimes \xi_2$: if $\phi_1, \phi_2 \in E$ are linearly dependent, then $\Phi$ has complex rank one and we are done, so suppose that $\phi_1, \phi_2$ are linearly independent. Using the standard basis $\{\sigma_1, \sigma_2, \sigma_3\}$ of Pauli matrices (2.14) for $\mathfrak{su}(2)$, namely

(2.14) $$\sigma_1 = \begin{pmatrix} i & 0 \\ 0 & -i \end{pmatrix}, \quad \sigma_2 = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}, \quad \sigma_3 = \begin{pmatrix} 0 & i \\ i & 0 \end{pmatrix},$$

we obtain bases for the real vector spaces $\mathfrak{su}(W^+)$ and $\mathfrak{su}(E)$:

$$
\sigma_1^e = i(\xi_1 \otimes \xi_1^* - \xi_2 \otimes \xi_2^*), \quad \sigma_2^e = \xi_1 \otimes \xi_2^* - \xi_2 \otimes \xi_1^*,
$$
$$
\sigma_3^e = i(\xi_1 \otimes \xi_2^* + \xi_2 \otimes \xi_1^*),
$$
$$
\sigma_1^w = i(\phi_1 \otimes \phi_1^* - \phi_2 \otimes \phi_2^*), \quad \sigma_2^w = \phi_1 \otimes \phi_2^* - \phi_2 \otimes \phi_1^*,
$$
$$
\sigma_3^w = i(\phi_1 \otimes \phi_2^* + \phi_2 \otimes \phi_1^*).
$$

Writing $\Phi = \Phi_1 + \Phi_2$, we have

$$
(\Phi_a \otimes \Phi_a^*)_{00} = -i(\phi_a \otimes \phi_a^*)_0 \otimes i(\xi_a \otimes \xi_a^*)_0
$$

for $a = 1, 2$ and

$$
(\Phi \otimes \Phi^*)_{00} = (\Phi_1 \otimes \Phi_1^*)_{00} + (\Phi_1 \otimes \Phi_2^* + \Phi_2 \otimes \Phi_1^*)_{00} + (\Phi_2 \otimes \Phi_2^*)_{00}.
$$

So, by the identity (2.13) and noting that

$$
i(\xi_1 \otimes \xi_1^*)_0 = \frac{1}{2} i(\xi_1 \otimes \xi_1^* - \xi_2 \otimes \xi_2^*) = \frac{1}{2} \sigma_1^e = -i(\xi_2 \otimes \xi_2^*)_0,
$$ and

$$i(\phi_1 \otimes \phi_1^*)_0 = \frac{1}{2} i(\phi_1 \otimes \phi_1^* - \phi_2 \otimes \phi_2^*) = \frac{1}{2} \sigma_1^w = -i(\phi_2 \otimes \phi_2^*)_0$$

we see that

$$(\Phi \otimes \Phi^*)_{00} = -i(\phi_1 \otimes \phi_1^*)_0 \otimes i(\xi_1 \otimes \xi_1^*)_0 - i(\phi_2 \otimes \phi_2^*)_0 \otimes i(\xi_2 \otimes \xi_2^*)_0$$
$$- \frac{1}{2} i(\phi_1 \otimes \phi_2^* + \phi_2 \otimes \phi_1^*) \otimes i(\xi_1 \otimes \xi_2^* + \xi_2 \otimes \xi_1^*)$$
$$+ \frac{1}{2}(\phi_1 \otimes \phi_2^* - \phi_2 \otimes \phi_1^*) \otimes (\xi_1 \otimes \xi_2^* - \xi_2 \otimes \xi_1^*)$$
$$= -\frac{1}{4} \sigma_1^w \otimes \sigma_1^e - \frac{1}{4} \sigma_1^w \otimes \sigma_1^e - \frac{1}{2} \sigma_3^w \otimes \sigma_3^e + \frac{1}{2} \sigma_2^w \otimes \sigma_2^e$$
$$= -\frac{1}{2} \sigma_1^w \otimes \sigma_1^e + \frac{1}{2} \sigma_2^w \otimes \sigma_2^e - \frac{1}{2} \sigma_3^w \otimes \sigma_3^e.$$

Thus, $(\Phi \otimes \Phi^*)_{00}$ would have real rank three, a contradiction, and so $\Phi$ must have complex rank one, which proves Assertion 1.

The preceding argument also shows that if $\Phi$ has complex rank two, then $(\Phi \otimes \Phi^*)_{00}$ has real rank three. Conversely, if $(\Phi \otimes \Phi^*)_{00}$ has real rank three, then $\Phi$ cannot have complex rank one by Assertion 1, so $\Phi$ has complex rank two. q.e.d.

2.5. The PU(2) monopole equations and holonomy perturbations. In §2.5.1 we describe the PU(2) monopole equations in their unperturbed form, following [71], [74]. In §2.5.2 we introduce the holonomy perturbations and the perturbed PU(2) monopole equations, deferring a detailed discussion of most of the technical regularity issues concerning holonomy perturbations to the Appendix. In Donaldson’s application to the extended anti-self-dual equation, some important features ensure that the requisite analysis is relatively tractable:

(i) reducible connections can be excluded from the compactification of the extended moduli spaces [18, p. 283], (ii) the cohomology groups for the elliptic complex of his extended equations have simple weak semi-continuity properties with respect to Uhlenbeck limits [18, Proposition 4.33], and (iii) the zero locus being perturbed is cut out of a finite-dimensional manifold [18, p. 281, Lemma 4.35, & Corollary 4.38]. For the development of Donaldson’s method for PU(2) monopoles described here, none of these simplifying features hold and so the corresponding transversality argument is rather complicated. Indeed, from Proposition 7.1.32 in [20] one can see that because of the Dirac operator, the behavior of the cokernels of the linearization of the PU(2) monopole equations can be quite involved under Uhlenbeck limits. The holonomy perturbations considered by Donaldson in [18] are inhomogeneous, as he uses the perturbations to kill the cokernels Coker $d_A^+$ directly. In contrast, the perturbations which we consider in (1.3) are homogeneous and we shall argue indirectly in §5 that the cokernels of the linearization vanish away from the reducible and zero-section solutions.

2.5.1. The unperturbed PU(2) monopole equations. Recall that we consider Hermitian two-plane bundles $E$ over $X$ whose determinant line bundles det $E$ are isomorphic to a fixed Hermitian line bundle over $X$ endowed with a fixed $C^\infty$, unitary connection $A_e$. Let $(\rho, W^+, W^-)$ be a spin$^c$ structure on $X$, where $\rho : T^*X \rightarrow \text{End}W$ is the Clifford map, and the Hermitian four-plane bundle $W = W^+ \oplus W^-$ is endowed with a $C^\infty$ spin$^c$ connection. Given a connection $A$ on $E$ with curvature $F_A \in L_{k-1}^2(\Lambda^2 \otimes u(E))$, then $(F_A^+)_0 \in L_{k-1}^2(\Lambda^+ \otimes su(E))$ denotes the traceless part of its self-dual component. Equivalently, if $A$ is a connection on $su(E)$ with curvature $F_A \in L_{k-1}^2(\Lambda^2 \otimes so(su(E)))$, then $F_A^+ \in L_{k-1}^2(\Lambda^+ \otimes su(E))$ is its self-dual component, viewed as a section of $\Lambda^+ \otimes su(E)$ via the implicit isomorphism ad: $su(E) \rightarrow so(su(E))$. Let $D_A : L_k^2(W^+ \otimes E) \rightarrow L_{k-1}^2(W^- \otimes E)$ be the corresponding Dirac operator.

For an $L_k^2$ section $\Phi$ of $W^+ \otimes E$, let $\Phi^*$ be its pointwise Hermitian dual and let $(\Phi \otimes \Phi^*)_{00}$ be the component of the Hermitian endomorphism $\Phi \otimes \Phi^*$ of $W^+ \otimes E$ which lies in $su(W^+) \otimes su(E)$. The Clifford map $\rho$ defines an isomorphism $\rho : \Lambda^+ \rightarrow su(W^+)$ and thus an isomorphism $\rho = \rho \otimes id_{su(E)}$ of $\Lambda^+ \otimes su(E)$ with $su(W^+) \otimes su(E)$. Then

$$
\begin{aligned}
F_A^+ - \rho^{-1}(\Phi \otimes \Phi^*)_{00} &= 0, \\
D_A \Phi &= 0,
\end{aligned}
$$

are the unperturbed equations considered in [67], [68], [71], [74] (with slightly differing trace conditions) for a pair $(A, \Phi)$ consisting of a connection $A$ on $su(E)$ and a section $\Phi$ of $W^+ \otimes E$. Equivalently, given a pair $(A, \Phi)$ with $A$ a fixed-determinant connection on $E$, equations (2.15) take the same form except that $F_A^+$ is replaced by $(F_A^+)_0$.

2.5.2. The perturbed PU(2) monopole equations. We next introduce perturbations of the PU(2) monopole equations (2.15) which will enable us to prove the transversality result described in Theorem 1.3. The perturbations in question make use of holonomy and their construction is partly modelled on related perturbations introduced by Donaldson, Floer and Taubes [8], [17], [29], [18], [86]. All of these constructions require that a unitary connection $A$ on a Hermitian two-plane bundle $E$ over $X$ be regular enough that parallel translation along a $C^\infty$ path in $X$ is well-defined. For example, Floer employs a configuration space of $L_1^4$ connections modulo $L_2^4$ gauge-transformations over a three-manifold, so these connections are at least continuous (as $L_1^4 \subset C^0$ in dimension three) and the standard theory of ordinary differential equations applies to define parallel translation without further qualification [29]. In dimension four, parallel translation can be defined without difficulty using $L_k^2$ connections with $k \geq 3$. With a little more care one can see that parallel translation can be defined by $L_2^2$ connections, even though $L_2^2 \not\subset C^0$ [61, §3.2]. These regularity issues become rather more intractable, as one can see from the Sobolev restriction theorem, for connections which are only $L_1^2$ [2, Theorem V.5.4]. As explained in the Appendix — to which we refer the reader for a discussion of the more technical points — we shall ultimately restrict our attention to configuration spaces of $L_k^2$ connections with $k \geq 3$. The perturbations will, by definition, be zero on a neighborhood of a point in $X$ where the curvature is large and so our regularity theory for $L_1^2$ monopoles will apply near points where curvature has bubbled off in order to prove removability of singularities (see §4.5.2).

We follow standard convention by saying that a connection $A$ on a $G$ bundle $E$ over a connected manifold $Y$ is ‘irreducible’ if its stabilizer $\text{Stab}_A$ is trivial, that is, the center of the Lie group $G$ [20, p. 133], rather than saying (more correctly) that its holonomy group $\text{Hol}_A(y_0)$ is not a proper Lie subgroup of $\text{Aut}(E_{y_0}) \simeq G$, where $y_0 \in Y$ is any basepoint. However, the holonomy will be our primary concern in this section, so some care is required as the two notions do not coincide in general. Recall from [20, Lemma 4.2.8] that $\text{Stab}_A$ is isomorphic to the centralizer of $\text{Hol}_A(y_0)$ in $G$. If $Y$ is simply connected, then $\text{Hol}_A(y_0)$ is a connected Lie subgroup of $G$ [44, Theorem II.4.2]. Thus, if $G = \text{SU}(2)$ or $\text{SO}(3)$ and $Y$ is simply connected, then $A$ has trivial stabilizer in $G$ if and only if $\text{Hol}_A(y_0) \simeq G$ [20, p. 133]. Indeed, if $G = \text{SO}(3)$ and $\text{Stab}_A = \{\text{id}\}$, then $H := \text{Hol}_A(y_0) = \text{SO}(3)$; otherwise, we would have:

- $H = \text{SO}(2)$, with centralizer $Z(H) = \text{SO}(2)$ (by [11, Theorem IV.2.3(ii)]), contradicting $\text{Stab}_A = \{\text{id}\}$, or

- $H = \{\text{id}\}$, with centralizer $Z(H) = \text{SO}(3)$, again contradicting $\text{Stab}_A = \{\text{id}\}$.

The same argument holds for $G = \text{SU}(2)$, but not for higher-dimensional Lie groups. For example, if $G = \text{U}(2) = \text{SU}(2) \times_{\{\pm \text{id}\}} S^1$, we cannot exclude the possibility that a U(2) connection $A$ with $\text{Stab}_A = S_Z^1$ reduces to an SU(2) connection, t SU(2).

at is, A has holonomy $ \operatorname{Hol}_{A}(y_{0})= $

$$
\mathrm{S U(2)}
$$

$$
\mathrm{Hol}_{A}(y_{0})=
\mathrm{is},\;A
$$

With the preceding comments in mind, the first ingredient in our construction of the holonomy perturbations is a local section of $ \mathfrak{su}(E) $ given by the holonomy of an SO(3) connection A on $ \mathfrak{su}(E). $ Let $ \gamma\subset X $ be a $ C^{\infty} $ loop based at a point $ x_{0}\in X $ and let

$$
\mathfrak{s u}(E)
$$

$$
SO(3)
$$

$$
\mathfrak{s u}(E)
$$

$$
C^{\infty}
$$

$$
\gamma\subset X
$$

$$
x_{0}\in X
$$

$$
h_{\gamma,x_{0}}(A)\in\mathrm{SO}(\mathfrak{s u}(E))|_{x_{0}}
$$

be the holonomy of the connection A around the loop $ \gamma $ . The exponential map $ \exp :\mathfrak{so}(3)\rightarrow\mathrm{SO}(3) $ gives a diffeomorphism from a ball 2B around the origin in $ \mathfrak{so}(3) $ to a ball around the identity in $ \mathrm{SO}(3). $ Let $ \psi:\mathbb{R}\to[0,1] $ be a $ C^{\infty} $ cutoff function such that $ \psi(|\zeta|)=1 $ for $ \zeta\in\frac{1}{2} B,\psi(|\zeta|)>0 $ for $ \zeta\in B $ , and $ \psi(|\zeta|)=0 $ for $ \zeta\in\mathfrak{so}(3)-B. $ Then

$$
\gamma
$$

$$
:\mathfrak{s}\mathfrak{o}(3)\rightarrow\mathrm{SO}(3)
$$

$$
\mathfrak{s}\mathfrak{o}(3)
$$

$$
SO(3)
$$

$$
\psi:\mathbb{R}\rightarrow
$$

$$
\left[0,1\right]
$$

$$
C^{\infty}
$$

$$
\psi(|\zeta|)=1\;\mathrm{for}\;\zeta\in\frac{1}{2}B,\:\psi(|\zeta|)>0
$$

$$
\psi\big(\big|\zeta\big|\big)=0
$$

$$
\zeta\in B
$$

$$
\zeta\in\mathfrak{s}\mathfrak{o}(3)-B
$$

(2.16)

$$
\mathfrak{h}_{\gamma,x_{0}}(A):=\psi\left(|\exp^{-1}(h_{\gamma,x_{0}}(A))|\right)\cdot\mathrm{ad}^{-1}(\exp^{-1}(h_{\gamma,x_{0}}(A)))
$$

defines a gauge-equivariant map $ \mathcal{A}_{E}(X)\rightarrow\mathfrak{su}(E) $ $ \mathfrak{so}(\mathfrak{su}(E)) $ is the standard isomorphism.

$ \mid_{x_{0}}, $ where ad : $ \mathfrak{su}(E)\rightarrow $

$$
\mathcal{A}_{E}(X)\to\mathfrak{s u}(E)|_{x_{0}}
$$

$$
\mathfrak{s u}(E)\rightarrow
$$

$$
\mathfrak{s}\mathfrak{o}(\mathfrak{s}\mathfrak{u}(E))
$$

Lemma 2.22. Let $ U \subset X $ be a simply connected open subset and let $ x_{0} $ be a point in U . If $ A|_{U} $ is an irreducible SO(3) connection on $ \mathfrak{su}(E)|_{U}, $ then there are loops $ \{\gamma_l\}_{l=1}^{3}\subset U, $ depending on A, such that the set $ \{h_{\gamma_l,x_0}(A)\}_{l=1}^{3}\subset \mathrm{SO}(\mathfrak{su}(E))|_{x_0} $ lies in the open subset of $ \mathrm{SO}(\mathfrak{su}(E))|_{x_0} $ given by the image under $ \exp $ of the ball $ B\subset \mathfrak{so}(\mathfrak{su}(E))|_{x_0} $ around the identity. The set $ \{\mathfrak{h}_{\gamma_l,x_0}(A)\}_{l=1}^{3} $ is then a basis for $ \mathfrak{su}(E)|_{x_0}. $

$$
U\subset X
$$

$$
x_{0}
$$

$$
SO(3)
$$

$$
A|_{U}
$$

$$
\mathfrak{n}(E)|_{U}
$$

$$
\{\gamma_{l}\}_{l=1}^{3}\subset U
$$

$$
A,
$$

$$
\{h_{\gamma_{l},x_{0}}(A)\}_{l=1}^{3}\subset\mathrm{SO}(\mathfrak{s u}(E))|_{x_{0}}
$$

$$
\mathrm{SO}(\mathfrak{u}(E))|_{x_0}
$$

$$
B\subset\mathfrak{s o}(\mathfrak{s u}(E))|_{x_0}
$$

$$
\{\mathfrak{h}_{\gamma_{l},x_{0}}(A)\}_{l=1}^{3}
$$

$$
\mathfrak{s u}(E)|_{x_0}
$$

Proof. Since $ A |_{U} $ is an irreducible SO(3) connection over a simply connected manifold U, the holonomy group $ \operatorname{Hol}_{A|U}(x_{0}) $ is equal to $ \mathrm{SO}(\mathfrak{s u}(E))|_{x_{0}} $ by the remarks preceding the statement of the lemma. Hence, there are three loops $ \gamma_{1},\gamma_{2},\gamma_{3} $ such that the holonomies

$$
\bar{A}|_{U}
$$

$$
SO(3)
$$

$$
\mathrm{Hol}_{A|U}(x_0)
$$

$$
\mathrm{SO}(\mathfrak{s u}(E))|_{x_0}
$$

$$
\gamma_{1},\gamma_{2},\gamma_{3}
$$

$$
h_{\gamma_{l},x_{0}}(A)\in B\subset\mathrm{SO}(\mathfrak{s u}(E))|_{x_{0}}
$$

give a basis $ \{\mathfrak{h}_{\gamma_{l},x_{0}}(A)\}_{l=1}^{3} $ for $ \mathfrak{su}(E)|_{x_0}. $ q.e.d.

$$
\{\mathfrak{h}_{\gamma_{l},x_{0}}(A)\}_{l=1}^{3}
$$

$$
\mathfrak{s u}(E)|_{x_{0}}.\quad\mathrm{q.e.d.}
$$

For a $ C^{\infty} $ connection A we may extend $ \mathfrak{h}_{\gamma,x_{0}}(A) $ to a $ C^{\infty} $ section $ \hat{\mathfrak{h}}_{\gamma}(A) $ of $ \mathfrak{su}(E) $ by radial parallel translation, with respect to A over a small ball $ B(x_{0},2R_{0}) $ and then multiplying by a $ C^{\infty} $ cutoff function $ \varphi $ on X which is positive on $ B(x_{0},R_{0}) $ and identically zero on $ X-B(x_{0},R_{0}). $ Thus if the set $ \left\{\mathfrak{h}_{\gamma_{l},x_{0}}(A)\right\}_{l=1}^{3}\mathrm{spans}\mathfrak{su}(E)|_{x_{0}} $ , then the set $ \left\{\varphi\hat{\mathfrak{h}}_{\gamma_{l}}(A)\right|_{y}\bigg]_{l=1}^{4} $ will span $ \mathfrak{su}(E)|_{y} $ for $ y\in B(x_{0},R_{0}). $ The constant $ R_{0} $ is chosen so that $ 4R_{0} $ is smaller than the injectivity radius of (X,g).

$$
C^{\infty}
$$

$$
\mathfrak{h}_{\gamma,x_{0}}(A)
$$

$$
C^{\infty}
$$

$$
\hat{\mathfrak{h}}_{\gamma}(A)
$$

$$
\mathfrak{s u}(E)
$$

$$
B(x_{0},2R_{0})
$$

$$
C^{\infty}
$$

$$
B(x_{0},R_{0})
$$

$$
\varphi
$$

$$
B(x_{0},R_{0})
$$

$$
X-
$$

$$
\{\mathfrak{h}_{\gamma_{l},x_{0}}(A)\}_{l=1}^{3}
\left.\left(E\right)\right|_{x_{0}}
$$

$$
\{\varphi\hat{\mathfrak{h}}_{\gamma_{l}}(A)|_{y}\}_{l=1}^{4}
$$

$$
\mathfrak{u}(E)|_y
$$

$$
y\in B(x_0,R_0)
$$

$$
R_{0}
$$

$$
4R_{0}
$$

$$
(X,g)
$$

---

In general, for an $L_k^2$ connection $A$ with $k \geq 2$, the section $\hat{\mathfrak{h}}_\gamma(A)$ will not be in $L_{k+1}^2$ and so we use the Neumann heat operator, for fixed small $t > 0$,

$$K_t(A|_{B(x_0,2R_0)}) : L^2(B(x_0,2R_0),\mathfrak{su}(E)) \rightarrow L_{k+1}^2(B(x_0,2R_0),\mathfrak{su}(E)),$$

as discussed in Appendix A.1 to construct an $L_{k+1}^2$ section

(2.17) $$\mathfrak{h}_\gamma(A) := K_t(A|_{B(x_0,2R_0)})\hat{\mathfrak{h}}_\gamma(A)$$

of $\mathfrak{su}(E)$ over $B(x_0,2R_0)$ which converges to $\hat{\mathfrak{h}}_\gamma(A)$ in $C^0(B(x_0,R_0))$ as $t \to 0$. Therefore, for small enough $t = t(A)$, the set $\{\varphi\mathfrak{h}_{\gamma l}(A)|_y\}_{l=1}^3$, will span $\mathfrak{su}(E)|_y$ for all $y \in B(x_0,R_0)$ just as before.

**Lemma 2.23.** Let $k \geq 2$ be an integer and let $A_0$ be an $L_k^2$ unitary connection on $E|_{B(x_0,2R_0)}$. Let $\gamma_1,\gamma_2,\gamma_3$ be loops in $B(x_0,2R_0)$ based at $x_0$ such that $\{\mathfrak{h}_{\gamma l,x_0}(A_0)\}_{l=1}^3$ spans $\mathfrak{su}(E)|_{x_0}$. Then there is a positive constant $\varepsilon(A_0,\{\gamma_l\})$ such that if $A$ is an $L_k^2$ unitary connection on $E|_{B(x_0,2R_0)}$ satisfying

$$\|A-A_0\|_{L_k^2,A_0(B(x_0,2R_0))} < \varepsilon,$$

then the set $\{\mathfrak{h}_{\gamma l,x_0}(A)\}_{l=1}^3$ spans $\mathfrak{su}(E)|_{x_0}$.

**Proof.** According to Lemma A.3 the holonomy maps

$$h_{\gamma,x_0} : \mathcal{A}_E(X) \rightarrow U(E)|_{x_0}$$

are continuous and so the maps $\mathfrak{h}_{\gamma l,x_0} : \mathcal{A}_E(X) \rightarrow \mathfrak{su}(E)|_{x_0}$ are continuous on small open neighborhoods of $A_0 \in \mathcal{A}_E(X)$. Hence, for small enough $\varepsilon$, the set $\{\mathfrak{h}_{\gamma l,x_0}(A)\}_{l=1}^3$ spans $\mathfrak{su}(E)|_{x_0}$. q.e.d.

We now specify the loops to be used in this construction, essentially following the argument used in the proof of Lemma 2.5 in [17]. Let $\{B(x_j,4R_0)\}_{j=1}^{N_b}$, be a disjoint collection of open balls, where $N_b$ is a fixed integer to be specified later (see §4.5.2). According to the slice results of [20, p. 192], [87, Proposition 2.1] for manifolds with boundary, the quotient space $\mathcal{B}_E^*(B(x_j,2R_0))$ of irreducible $L_k^2$ connections on $E|_{B(x_j,2R_0)}$ is a $C^\infty$ manifold modelled on a separable Hilbert space. The quotient $L_k^2$ topology on $\mathcal{B}_E^*(B(x_j,2R_0))$ is clearly metrizable and so Stone’s Theorem implies that $\mathcal{B}_E^*(B(x_j,2R_0))$ is paracompact and thus admits partitions of unity [55, Corollary II.3.8].

For each $j = 1,\ldots,N_b$ and each point $[A_0]$ in $\mathcal{B}_E^*(B(x_j,2R_0))$, we can find loops $\{\gamma_{j,l,A_0}\}_{l=1}^3$, contained in $B(x_j,2R_0)$ and based at $x_j$ such that $\{\mathfrak{h}_{\gamma_{j,l},A_0}(A_0)\}_{l=1}^3$, spans $\mathfrak{su}(E)|_{x_j}$. For each such point $[A_0]$, Lemma 2.23 implies that there is an $L_k^2,A_0$ ball

$$B_{[A_0]}(\varepsilon_A_0) := \{[A] \in \mathcal{B}_E^*(B(x_j,2R_0)) : \text{dist}_{L_k^2,A_0}([A],[A_0]) < \varepsilon_A_0\}$$

such that for all $[A] \in B_{[A_0]}(\varepsilon_A_0)$, the set $\{\mathfrak{h}_{\gamma_{j,l},A_0}(A)\}_{l=1}^3$ spans $\mathfrak{su}(E)|_{x_j}$. These balls give an open cover of $\mathcal{B}_E^*(B(x_j,2R_0))$, and hence there is a locally finite refinement of this open cover, $\{U_{j,\alpha}\}_{\alpha=1}^{\infty}$, and a positive partition $\chi_{j,\alpha}$ (see Proposition A.12) subordinate to $\{U_{j,\alpha}\}_{\alpha=1}^{\infty}$ in the sense that

$$\sum_\alpha \chi_{j,\alpha}[A] > 0, \quad [A] \in \mathcal{B}_E^*(B(x_j,2R_0)).$$

Hence, for each $U_{j,\alpha}$, we obtain loops $\{\gamma_{j,l,\alpha}\}_{l=1}^3 \subset B(x_j,2R_0)$ such that for all $[A] \in U_{j,\alpha}$, the sections $\mathfrak{h}_{\gamma_{j,l,\alpha}}(A)$ span $\mathfrak{su}(E)|_{x_j}$.

Let $\beta$ be a smooth cutoff function on $\mathbb{R}$ such that $\beta(t) = 1$ for $t \leq \frac{1}{2}$ and $\beta(t) = 0$ for $t \geq 1$, with $\beta(t) > 0$ for $t < 1$. Then the $C^\infty$ gauge-invariant maps $\mathcal{A}_E(X) \to \mathbb{R}$, $A \mapsto \beta_j[A]$ given by

(2.18) $$\beta_j[A] := \beta \left( \frac{1}{\varepsilon_0^2} \int_{B(x_j,4R_0)} \beta \left( \frac{\text{dist}_g(\cdot,x_j)}{4R_0} \right) |F_A|^2 dV \right)$$

are zero when the energy of the connection $A$ is greater than or equal to $\frac{1}{2}\varepsilon_0^2$ over a ball $B(x_j,2R_0)$. Here, $\varepsilon_0$ is the constant of Corollary 3.16. Finally, we define $C^\infty$ cutoff functions on $X$ by setting

(2.19) $$\varphi_j(x) := \beta \left( \frac{\text{dist}_g(x,x_j)}{R_0} \right), \quad x \in X,$$

so that $\varphi_j$ is positive on the ball $B(x_j,R_0)$ and zero on its complement in $X$.

We can now define a gauge equivariant $C^\infty$ map

$$\mathcal{A}_E(X) \to L_{k+1}^2(X,\mathfrak{su}(E)), \quad A \mapsto \mathfrak{m}_{j,l,\alpha}(A)$$

by setting

(2.20) $$\mathfrak{m}_{j,l,\alpha}(A) := \beta_j[A]\chi_{j,\alpha}[A|B(x_j,2R_0)]\varphi_j\mathfrak{h}_{\gamma_{j,l,\alpha}}(A).$$

Thus at each point $A \in \mathcal{A}_E(X)$ only a finite number of the $\mathfrak{m}_{j,l,\alpha}(A)$ are non-zero and each map $\mathfrak{m}_{j,l,\alpha}$ is $C^\infty$ with uniformly bounded derivatives of all orders on $\mathcal{A}_E(X)$ (see Appendix A.4).

---

To define the perturbation of the Dirac operator in (2.15), we need elements of $\Omega^0(\text{Hom}_{\mathbb{C}}(W^+, W^-))$ and these are conveniently provided by complex one-forms using the Clifford isomorphism

$$\rho : \Lambda^1_{\mathbb{C}} \rightarrow \text{Hom}_{\mathbb{C}}(W^+, W^-),$$

where $\Lambda^1_{\mathbb{C}} = \Lambda^1 \otimes_{\mathbb{R}} \mathbb{C}$. These one-forms are parametrized by the following Banach space: Let $A$ be the index set

$$\{(j, l, \alpha) : 1 \leq j \leq N_b, 1 \leq l \leq 3, \alpha \in \mathbb{N}\},$$

let $\delta = (\delta_\alpha)^\infty_{\alpha=1} \in \ell^1(\mathbb{R})$ be the sequence of positive weights described in Appendix A.4, let $r \geq k + 1$, and let

(2.21)

$$\mathcal{P}^r_{\vartheta} := \ell^1_{\delta}(\mathbb{A}, C^r(X, \Lambda^1_{\mathbb{C}}))$$

be the set of sequences $\vec{\theta} := (\vartheta_{j,l,\alpha})$ in $C^r(X, \Lambda^1_{\mathbb{C}})$ such that

$$\|\vec{\theta}\|_{\ell^1_{\delta}(C^r(X))} := \sum_{j,l,\alpha} \delta^{-1}_\alpha \|\vartheta_{j,l,\alpha}\|_{C^r(X)} < \infty.$$

Then $\mathcal{P}^r_{\vartheta}$ is a Banach space with respect to the above norm [40, §1.7].

## Remark 2.24.

1. Note that we measure reducibility of connections and allow the loops $\gamma_{j,l,\alpha}$ to be contained in the larger balls $B(x_j, 2R_0)$ while the perturbations are supported on the smaller balls $B(x_j, R_0)$. Thus, if $A \in \mathcal{A}_E(X)$ is a connection such that $A|_{B(x_j, 2R_0)}$ is reducible for all $j \in \{1, \ldots, N_b\}$ such that $\beta_j[A] > 0$ and $\Phi \neq 0$, then $[A, \Phi]$ cannot be a point in $M^{*,0}_{W,E}$: our unique continuation result for PU(2) monopoles (see Theorem 5.11) which are reducible on an open subset of $X$ containing all balls $\bar{B}(x_j, R_0)$ with $\beta_j[A] > 0$ would imply that $A$ is reducible on all of $X$ and so $(A, \Phi)$ would be a reducible PU(2) monopole. Consequently, if $[A, \Phi] \in M^{*,0}_{W,E}$ then $A$ must be irreducible on some ball $B(x_j, 2R_0)$; otherwise, $A$ would be reducible on all balls $B(x_j, 2R_0)$ with $\beta_j[A] > 0$ and so reducible on $X$.

2. Note that the sections $m_{j,l,\alpha}$ are defined on the entire space $\mathcal{A}_E(X)$: They are zero for connections $A \in \mathcal{A}_E(X)$ which are reducible when restricted to $B(x_j, 2R_0)$.

---

3. Our energy bound (4.2) for solutions $(A, \Phi)$ to the perturbed PU(2) monopole equations ensures that there is always at least one ball $B(x_j, R_0)$ where the sections $\{m_{j,l,\alpha}(A)\}_{l=1}^3$ span $\text{su}(E)|_{B(x_j,R_0)}$; see §4.5.2.

Because only a finite number of the sections $m_{j,l,\alpha}(A)$ are non-zero at each $A \in \mathcal{A}_E(X)$, the sum

$$\vec{\vartheta} \cdot \vec{m}(A) := \sum_{j,l,\alpha} \rho(\vartheta_{j,l,\alpha}) \otimes_{\mathbb{C}} m_{j,l,\alpha}(A)$$

gives a well-defined $L_{k+1}^2$ section of

$$\text{Hom}_{\mathbb{C}}(W^+, W^-) \otimes_{\mathbb{C}} \text{sl}(E) \simeq \Lambda_{\mathbb{C}}^1 \otimes_{\mathbb{C}} \text{sl}(E),$$

noting that although each $m_{j,l,\alpha}(A)$ is a section of $\text{su}(E)$, we have $\text{sl}(E) = \text{su}(E) \otimes_{\mathbb{R}} \mathbb{C}$. The map

$$\mathcal{A}_E(X) \rightarrow L_{k+1}^2(X, \text{Hom}_{\mathbb{C}}(W^+, W^-) \otimes_{\mathbb{C}} \text{sl}(E)), \quad A \mapsto \vec{\vartheta} \cdot \vec{m}(A)$$

is $C^\infty$ and gauge equivariant and so defines a $C^\infty$ section of the vector bundle

$$\mathcal{A}_E^*(X) \times_{\mathcal{G}_E} L_{k+1}^2(X, \text{Hom}_{\mathbb{C}}(W^+, W^-) \otimes_{\mathbb{C}} \text{sl}(E)) \rightarrow \mathcal{B}_E^*(X).$$

By construction (see Appendix A.4) the sum $\vec{\vartheta} \cdot \vec{m}(A)$ satisfies a $C^0$ estimate of the form

$$\sup_{A \in \mathcal{A}_E(X)} \| \vec{\vartheta} \cdot \vec{m}(A) \|_{L_{k+1}^2(A(X))} \leq C \| \vec{\vartheta} \|_{\ell_\delta^1(C^r(X))}$$

and $\|\vec{\vartheta}\|_{\ell_\delta^1(C^r(X))} \leq \varepsilon_\vartheta,$

where $C = C(g,k)$, and $\varepsilon_\vartheta$ is a positive constant which we are free to specify.

We shall also need to construct a gauge equivariant $C^\infty$ map from $\mathcal{A}_E^*(X)$ to $L_{k+1}^2(\text{gl}(\Lambda^+) \otimes_{\mathbb{R}} \text{so}(\text{su}(E)))$. This map will define a perturbation of the quadratic form in (2.15) using the representation ad : $\text{su}(E) \rightarrow \text{so}(\text{su}(E))$ and is parametrized by the Banach space

$$\mathcal{P}_\tau^r := \ell_\delta^1(\mathbb{A}, C^r(X, \text{gl}(\Lambda^+)))$$

of sequences $\vec{\tau} := (\tau_{j,l,\alpha})$ in $C^r(X, \text{gl}(\Lambda^+))$ such that

$$\|\vec{\tau}\|_{\ell_\delta^1(C^r(X))} := \sum_{j,l,\alpha} \delta_\alpha^{-1} \|\tau_{j,l,\alpha}\|_{C^r(X)} < \infty.$$

---

Then the sum

(2.25) $\vec{\tau} \cdot \vec{m}(A) := \sum_{j,l,\alpha} \tau_{j,l,\alpha} \otimes_{\mathbb{R}} \text{ad}(\mathfrak{m}_{j,l,\alpha}(A))$

is pointwise finite and gives a well-defined $L^2_{k+1}$ section of

$$
\mathfrak{gl}(\Lambda^+) \otimes_{\mathbb{R}} \text{so}(\text{su}(E)).
$$

The map

$$
\mathcal{A}_E(X) \rightarrow L^2_{k+1}(X, \mathfrak{gl}(\Lambda^+) \otimes_{\mathbb{R}} \text{so}(\text{su}(E))), \quad A \mapsto \vec{\tau} \cdot \vec{m}(A)
$$

is $C^\infty$ and gauge equivariant and so defines a $C^\infty$ section of the vector bundle

$$
\mathcal{A}^*_E(X) \times_{\mathcal{G}_E} L^2_{k+1}(X, \mathfrak{gl}(\Lambda^+) \otimes_{\mathbb{R}} \text{so}(\text{su}(E))) \rightarrow \mathcal{B}^*_E(X).
$$

By construction (see Appendix A.4) the sum $\vec{\tau} \cdot \vec{m}(A)$ satisfies $C^0$ estimates

(2.26) $\sup_{A \in \mathcal{A}_E(X)} \| \vec{\tau} \cdot \vec{m}(A)\|_{L^2_{k+1},A(X)} \leq C \|\vec{\tau}\|_{\ell_\delta^1(C^r(X))}$

and $\| \vec{\tau}\|_{\ell_\delta^1(C^r(X))} \leq \varepsilon_\tau$,

where $C = C(g,k)$, and $\varepsilon_\tau$ is a positive constant which we are free to specify.

Our perturbed PU(2) monopole equations for a pair $(A, \Phi)$ on $(\text{su}(E), W^+ \otimes E)$ then take the form

$$
\mathfrak{S}_1(A, \Phi) := F_A^+ - (\text{id} + \tau_0 \otimes \text{id}_{\text{su}(E)})
$$

(2.27) $+\vec{\tau} \cdot \vec{m}(A)) \rho^{-1}(\Phi \otimes \Phi^*)_{00} = 0,$

$$
\mathfrak{S}_2(A, \Phi) := D_A \Phi + \rho(\vartheta_0)\Phi + \vec{\vartheta} \cdot \vec{m}(A)\Phi = 0,
$$

where $\tau_0 \in C^r(X, \mathfrak{gl}(\Lambda^+))$ and $\vartheta_0 \in C^r(X, \Lambda^1_C)$ are additional perturbation parameters. For brevity, we shall often denote $\vec{\tau}_A := \vec{\tau} \cdot \vec{m}(A)$ and $\vec{\vartheta}_A := \vec{\vartheta} \cdot \vec{m}(A)$.

## Remark 2.25.

1. In [25] we consider the question of transversality of the spaces of reducible solutions or U(1) monopoles, which are identified with moduli spaces of Seiberg-Witten monopoles. In particular, we show that the moduli spaces of U(1) monopoles are cut out transversely for generic $\tau_0 \in \Omega^0(\mathfrak{gl}(\Lambda^+))$.

---

2. If the section $\Phi$ is identically zero, then the PU(2) monopole equations reduce to those for a projectively anti-self-dual unitary connection $A$ on $E$. If the connection $A$ is reducible, then all of the sections $m_{j,l,\alpha}(A)$ are identically zero on $X$; the perturbations $\vec{\tau} \cdot \vec{m}(A)$ and $\vec{\vartheta} \cdot \vec{m}(A)$ in (2.27) are then zero.

3. We emphasize that the holonomy sections in the sequence $\vec{m}(A)$ are always $L^2_{k+1}$ by construction for $L^2_k$ connections $A$ (with $k \geq 2$) and that the sums defining $\vec{\tau} \cdot \vec{m}(A)$ and $\vec{\vartheta} \cdot \vec{m}(A)$ are always finite for each $A$, although the number of terms may tend to infinity as $A$ approaches a reducible connection.

The proof of the existence of an Uhlenbeck compactification for $M_{W,E}$ in §4 requires the perturbations $\vec{\tau} \cdot \vec{m}(A)$ and $\vec{\vartheta} \cdot \vec{m}(A)$ to satisfy the following estimates in order to obtain universal a priori $L^2_{1,A}$ bounds for $\Phi$ and $L^2$ bounds for $F_A$ (see Lemmas 4.2 and 4.3):

$$\sup_{A \in A_E} \|\vec{\tau} \cdot \vec{m}(A)\|_{L^\infty(X)} \leq 1,$$

$$\sup_{A \in A_E} \|\vec{\vartheta} \cdot \vec{m}(A)\|_{L^4(X)} \leq 1.$$

To obtain the more delicate universal a priori $L^\infty$ bounds for $\Phi$ and $F_A^+$ (see Lemmas 2.26 and 4.4) required by our Uhlenbeck compactness argument in §4, the perturbations $\tau_0$, $\vec{\tau} \cdot \vec{m}(A)$, and $\vec{\vartheta} \cdot \vec{m}(A)$ must satisfy the following stronger estimates:

$$\|\tau_0\|_{L^\infty(X)} + \sup_{A \in A_E} \|\vec{\tau} \cdot \vec{m}(A)\|_{L^\infty(X)} \leq \frac{1}{64},$$

$$\|\vartheta_0\|_{L^1_\infty(X)} + \sup_{A \in A_E} \|\vec{\vartheta} \cdot \vec{m}(A)\|_{L^1_\infty(A_X)} \leq 1.$$

We take a constant 1 on the right-hand sides of (2.28) and the second inequality in (2.29) for notational convenience only: these bounds do not need to be ‘small’. There are continuous Sobolev embeddings $L^2_4(X, \mathbb{R}) \subset L^\infty(X, \mathbb{R})$ and $L^2_4(X, \mathbb{R}) \subset L^1_\infty(X, \mathbb{R})$ over a four-manifold $X$. The estimates (2.29) then follow from the estimates (2.23) and (2.26) when $k \geq 3$. Therefore, to obtain the inequalities (2.29), we require that $k \geq 3$ in our configuration spaces of $L^2_k$ connections $B_E$ and pairs $C_{W,E}$; see §A.4. The bounds in (2.29) then follow for small enough choices of $\varepsilon_{\tau}$ and $\varepsilon_{\vartheta}$ in the inequalities (2.23) and (2.26).

We shall need a slight generalization of Lemma 2.19 which applies to the perturbed quadratic form $\tau\rho^{-1}(\Phi \otimes \Phi^*)_{00}$ when $\tau \neq \text{id}_{\Lambda^+}$. Without loss of generality, we may restrict our attention to automorphisms $\tau_{\rho} := \rho\tau\rho^{-1}$ of $\mathfrak{su}(W^{+})$ such that $|\tau_{\rho} - \mathrm{id}_{\mathfrak{su}(W^{+})}| = |\rho\tau\rho^{-1} - \mathrm{id}| < \varepsilon_{\tau}$ and thus

$$\langle \Phi_{1}, \Phi_{2} \rangle - \varepsilon_{\tau}|\Phi_{1}\|\Phi_{2}| \leq \langle \tau(\Phi_{1}), \Phi_{2} \rangle \leq \langle \Phi_{1}, \Phi_{2} \rangle + \varepsilon_{\tau}|\Phi_{1}\|\Phi_{2}|$$

for some universal positive constant $\varepsilon_{\tau} \ll 1$ and all

$$\Phi_{1}, \Phi_{2} \in \Omega^{0}(W^{+} \otimes E).$$

Hence, Lemma 2.19 yields the following bounds for the perturbed quadratic form:

**Lemma 2.26.** There is a universal positive constant $\varepsilon_{\tau} \ll 1$ such that for all $\|\tau - \mathrm{id}_{\Lambda^{+}}\|_{C^{0}(X)} < \varepsilon_{\tau}$ and $\Phi \in \Omega^{0}(W^{+} \otimes E)$ the following inequalities hold:

(1) $$\frac{1}{2}|\Phi|^{4} \leq \langle \tau_{\rho}(\Phi \otimes \Phi^{*})_{00}\Phi, \Phi \rangle \leq \frac{3}{4}|\Phi|^{4},$$

(2) $$\frac{1}{4}|\Phi|^{4} \leq |\tau_{\rho}(\Phi \otimes \Phi^{*})_{00}|^{2} \leq \frac{3}{8}|\Phi|^{4}.$$

**Remark 2.27.** The constant $\varepsilon_{\tau} = 1/64$ will suffice. The constraint $\|\tau - \mathrm{id}\|_{C^{0}(X)} < \varepsilon_{\tau}$ is only used in §4.1 and consequently in §4.6, where we establish the ‘universal’ a priori bounds for PU(2) monopoles and prove the existence of an Uhlenbeck compactification, respectively.

**2.6. The moduli space and the elliptic deformation complex.** We define the moduli space of PU(2) monopoles and compute the index of its elliptic deformation complex.

For any integer $k \geq 2$, the PU(2) monopole equations (2.27) define a $C^{\infty}$ map $\mathfrak{S} := (\mathfrak{S}_{1}, \mathfrak{S}_{2})$ of Hilbert manifolds,

(2.30) $$\mathfrak{S} : \tilde{\mathcal{C}}_{W,E} \rightarrow L_{k-1}^{2}(\Lambda^{+} \otimes \mathfrak{su}(E)) \oplus L_{k-1}^{2}(W^{-} \otimes E),$$

given by

$$(A, \Phi) \mapsto \begin{pmatrix} \mathfrak{S}_{1}(A, \Phi) \\ \mathfrak{S}_{2}(A, \Phi) \end{pmatrix}$$

$$:= \begin{pmatrix} F_{A}^{+} - (\mathrm{id} + \tau_{0} \otimes \mathrm{id}_{\mathfrak{su}(E)} + \vec{\tau} \cdot \vec{\mathfrak{m}}(A)) \rho^{-1}(\Phi \otimes \Phi^{*})_{00} \\ D_{A}\Phi + \rho(\vartheta_{0})\Phi + \vec{\vartheta} \cdot \vec{\mathfrak{m}}(A)\Phi \end{pmatrix}.$$

We can then define the moduli space of PU(2) monopoles by setting

(2.31) $$M_{W,E} := \{(A, \Phi) \in \tilde{\mathcal{C}}_{W,E}: \mathfrak{S}(A, \Phi) = 0\}/^\circ G_{E}$$ and denote the moduli space of PU(2) monopoles which are neither reducible nor zero-section pairs by

$$M_{W,E}^{*,0} := M_{W,E} \cap C_{W,E}^{*,0}.$$

We let $M_{E}^{\text{asd}} := \{[A] : F_A^+ = 0\} \subset B_E$ be the moduli space of anti-self-dual connections on $\mathfrak{su}(E)$.

The SO(3) bundle $\mathfrak{su}(E)$ has first Pontrjagin number and second Stiefel-Whitney class given by

$$\kappa := -\frac{1}{4} p_1(\mathfrak{su}(E)) = c_2(E) - \frac{1}{4} c_1(E)^2$$
$$w_2(\mathfrak{su}(E)) = c_1(E) \pmod{2},$$

and, for a connection $A$ on $\mathfrak{su}(E)$, we have the following Chern-Weil integral identity,

$$-\frac{1}{4} p_1(\mathfrak{su}(E)) = \frac{1}{8\pi^2} \int_X \left(|F_A^-|^2 - |F_A^+|^2\right) dV,$$

where we view $F_A$ as a section of $\Lambda^2 \otimes \mathfrak{su}(E)$ via the isomorphism ad: $\mathfrak{su}(E) \simeq \mathfrak{so}(\mathfrak{su}(E))$ (see [20, §2.1.4]).

Since the map $\mathfrak{S}$ is $\circ^\circ G_E$-equivariant, it defines a section of the Hilbert vector bundle $\mathfrak{V}$ over $C_{W,E}^{*,0}$ with total space

$$\mathfrak{V} := \tilde{C}_{W,E}^{*,0} \times \circ^\circ G_E \left(L_{k-1}^2(\Lambda^+ \otimes \mathfrak{su}(E)) \oplus L_{k-1}^2(W^- \otimes E)\right).$$

While the equation $\mathfrak{S}[A,\Phi] = 0$ is, of course, defined on $C_{W,E}$, $\mathfrak{V}$ does not extend from $C_{W,E}^{*,0}$ to a vector bundle over $C_{W,E}$. The moduli space $M_{W,E}^{*,0} \subset C_{W,E}^{*,0}$ is then the zero locus of the section $\mathfrak{S}$ of Hilbert vector bundle $\mathfrak{V}$ over the Hilbert manifold $C_{W,E}^{*,0}$: it will be a regular submanifold if $\mathfrak{S}$ vanishes transversely, that is, if the differential

$$(D\mathfrak{S})_{A,\Phi}: T_{[A,\Phi]} C_{W,E}^{*,0} \to L_{k-1}^2(\Lambda^+ \otimes \mathfrak{su}(E)) \oplus L_{k-1}^2(W^- \otimes E)$$

is surjective at all points $[A,\Phi]$ in $\mathfrak{S}^{-1}(0) \cap C_{W,E}^{*,0}$; recall from §2 that the tangent space $T_{[A,\Phi]} C_{W,E}^{*,0}$ is canonically identified with Ker $d_{A,\Phi}^{0,*} \subset \tilde{C}_{W,E}^{*,0}$.

Suppose $(A,\Phi)$ is a pair in $A_E \times \Omega^0(W^+ \otimes E)$. Recall from Proposition 2.1 that the differential at the identity id$_E \in \circ^\circ G_E$, of the map $\circ^\circ G_E \to A_E \times \Omega^0(W^+ \otimes E)$ given by $u \mapsto u(A,\Phi)$ is

$$\Omega^0(\mathfrak{su}(E)) \oplus i\mathbb{R}_Z \to \Omega^1(\mathfrak{su}(E)) \oplus \Omega^0(W^+ \otimes E),$$
$$\zeta \mapsto -d_{A,\Phi}^0 \zeta = (-d_{A,\Phi}, \zeta\Phi).$$

---

Similarly, the differential $(a, \phi) \mapsto d_{A,\Phi}^{1}(a, \phi) := (D\mathfrak{S})_{A,\Phi}(a, \phi),

$$\Omega^{1}(\mathfrak{su}(E)) \oplus \Omega^{0}(W^{+} \otimes E) \rightarrow \Omega^{+}(\mathfrak{su}(E)) \oplus \Omega^{0}(W^{-} \otimes E),$$

of the map $\mathfrak{S}$ at the point $(A, \Phi)$ is given by

$$d_{A,\Phi}^{1}(a, \phi)
:= \begin{pmatrix}
d_{A}^{+} a - \vec{\tau} \cdot (\delta \vec{\mathfrak{m}})(a)(\Phi \otimes \Phi^{*})_{00} - (\mathrm{id} + \tau_{0} \otimes \mathrm{id}_{\mathfrak{su}(E)} \\
+\vec{\tau} \cdot \vec{\mathfrak{m}}(A)) \rho^{-1}(\Phi \otimes \phi^{*} + \phi \otimes \Phi^{*})_{00}
\end{pmatrix},$$

where $\delta \vec{\mathfrak{m}} = \delta \vec{\mathfrak{m}} / \delta A$. (In the sequels we also find it convenient to use $L_{A,\Phi}$ to denote the linearization of the map $\mathfrak{S}$ at the point $(A, \Phi)$.) The differential of the composition $^{\circ}\mathcal{G}_{E} \mapsto \Omega^{+}(\mathfrak{su}(E)) \oplus \Omega^{0}(W^{-} \otimes E)$ given by

$$u \mapsto u(A, \Phi) \mapsto \mathfrak{S}(u(A, \Phi)) = u(\mathfrak{S}(A, \Phi)) = (u\mathfrak{S}_{1}(A, \Phi)u^{-1}, u\mathfrak{S}_{2}(A, \Phi))$$

is then

$$\Omega^{0}(\mathfrak{su}(E)) \oplus i\mathbb{R}_{Z} \rightarrow \begin{array}{l}
\Omega^{+}(\mathfrak{su}(E)) \\
\oplus \\
\Omega^{0}(W^{-} \otimes E)
\end{array},
\zeta \mapsto d_{A,\Phi}^{1} \circ d_{A,\Phi}^{0} \zeta = ([\zeta, \mathfrak{S}_{1}(A, \Phi)], \zeta\mathfrak{S}_{2}(A, \Phi)).$$

Therefore, $d_{A,\Phi}^{1} \circ d_{A,\Phi}^{0} = 0$ if and only if $\mathfrak{S}(A, \Phi) = 0$, that is, if and only if $(A, \Phi)$ is a PU(2) monopole. Consequently, the sequence

$$\Omega^{0}(\mathfrak{su}(E)) \oplus i\mathbb{R}_{Z} \xrightarrow{d_{A,\Phi}^{0}} \begin{array}{l}
\Omega^{1}(\mathfrak{su}(E)) \\
\oplus \\
\Omega^{0}(W^{+} \otimes E)
\end{array} \xrightarrow{d_{A,\Phi}^{1}} \begin{array}{l}
\Omega^{+}(\mathfrak{su}(E)) \\
\oplus \\
\Omega^{0}(W^{-} \otimes E)
\end{array}$$

is a complex if and only if $(A, \Phi)$ is a PU(2) monopole. The $L^{2}$ adjoint of $-d_{A,\Phi}^{0}$ is given by

$$-d_{A,\Phi}^{0,*} (a, \phi) = -d_{A}^{*} a + (\cdot\Phi)^{*} \phi.$$

The operator

$$\mathcal{D}_{A,\Phi} := d_{A,\Phi}^{0,*} + d_{A,\Phi}^{1}: \begin{array}{l}
\Omega^{1}(\mathfrak{su}(E)) \\
\oplus \\
\Omega^{0}(W^{+} \otimes E)
\end{array} \rightarrow \begin{array}{l}
\Omega^{0}(\mathfrak{su}(E)) \oplus i\mathbb{R}_{Z} \\
\oplus \\
\Omega^{0}(W^{-} \otimes E)
\end{array}$$ is elliptic (thus Fredholm) and so (2.37) is an elliptic deformation complex for the PU(2) monopole equations (2.27), with cohomology groups

$$H^0_{A,\Phi} := \text{Ker } d^0_{A,\Phi}, \quad H^1_{A,\Phi} := \text{Ker } d^1_{A,\Phi}/\text{Im } d^0_{A,\Phi}, \quad H^2_{A,\Phi} := \text{Coker } d^1_{A,\Phi},$$

analogous to the usual elliptic deformation complex [20, Eq. (4.2.26)] for the anti-self-dual equation, $F_A^+ = 0$. (An elliptic deformation complex for stable pairs for holomorphic bundles is given by Bradlow and Daskalopoulos in [9, §2].)

Recall that $H^0_{A,\Phi} = \text{Ker } d^0_{A,\Phi}$ is just the Lie algebra of the stabilizer Stab$_{A,\Phi}$ of the point $[A,\Phi] \in M_{W,E}$ and $H^1_{A,\Phi}$ is the Zariski or formal tangent space. Thus, for any point $[A,\Phi] \in M^{*,0}_{W,E}$ we have $H^0_{A,\Phi} = 0$. If $H^2_{A,\Phi} = 0$, then $\text{Coker}(D\mathfrak{S})_{A,\Phi} = 0$ and so $[A,\Phi]$ is a regular point of the zero locus of the section $\mathfrak{S}$ of $\mathfrak{V}$ over $C^{*,0}_{W,E}$. Thus, if $H^0_{A,\Phi} = 0$ and $H^2_{A,\Phi} = 0$, then $[A,\Phi]$ is a smooth point of $M_{W,E}$ with tangent space $\text{Ker } D_{A,\Phi} = \text{Ker}(d^0_{A,\Phi} + d^1_{A,\Phi}) = H^1_{A,\Phi}$, as we see from (2.35). Provided the zero set $\mathfrak{S}^{-1}(0)$ is regular, then $M^{*,0}_{W,E}$ will be a smooth manifold of dimension $-\text{Ind } D_{A,\Phi}$.

The perturbation terms in (2.27) define gauge equivariant maps

$$\tilde{\mathcal{C}}^{*,0}_{W,E} \rightarrow L^2_{k-1}(\Lambda^+ \otimes \mathfrak{su}(E)) \oplus L^2_{k-1}(W^- \otimes E),$$

given by

$$(A,\Phi) \mapsto \begin{pmatrix}\vec{\tau} \cdot \vec{\mathfrak{m}}(A)\rho^{-1}(\Phi \otimes \Phi^*)_{00} \\ \vec{\vartheta} \cdot \vec{\mathfrak{m}}(A)\Phi\end{pmatrix}.$$

For $k \geq 2$, the Sobolev multiplication theorem implies that $\vec{\vartheta} \cdot \vec{\mathfrak{m}}(A)\Phi$ is in $L^2_k(W^- \otimes E)$, while $\vec{\tau} \cdot \vec{\mathfrak{m}}(A)\rho^{-1}(\Phi \otimes \Phi^*)_{00}$ is in $L^2_k(\Lambda^+ \otimes \mathfrak{su}(E))$ when $k \geq 3$ and in $L^2_p(\Lambda^+ \otimes \mathfrak{su}(E)), 1 \leq p < 2$ when $k = 2$. By the Rellich embedding theorem, the inclusions $L^2_k \subset L^2_{k-1}$ and $L^2_p \subset L^2_1$, $p > 1$, are compact. In particular, it follows that the linearization of the perturbed PU(2) monopole equations (2.36) differs from the linearization of the unperturbed equations (2.15) by a compact operator [2, Theorem VI.2].

**Proposition 2.28.** If the map $\mathfrak{S}$ of (2.30) vanishes transversely for the parameters $(\tau_0, \vartheta_0, \vec{\tau}, \vec{\vartheta})$, then $M^{*,0}_{W,E}(\tau_0, \vartheta_0, \vec{\tau}, \vec{\vartheta})$ is a smooth manifold of dimension

$$\dim M^{*,0}_{W,E} = -2p_1(\mathfrak{su}(E)) - 3(1-b^1(X) + b^+(X))$$

$$+\frac{1}{2}p_1(\mathfrak{su}(E)) + \frac{1}{2}(c_1(W^+) + c_1(E))^2 - \frac{1}{2}\sigma(X) - 1$$

$$= \dim M_E^{\mathrm{asd}} + 2\operatorname{Ind}_\mathbb{C} D_A - 1,$$ where $\sigma(X)$ is the signature of $X$.

Proof. Since $H_{A,\Phi}^{0} = 0$ and $H_{A,\Phi}^{2} = 0$ (by hypothesis) at any point $[A, \Phi]$ in $M_{W,E}^{*,0}$, we have $\dim M_{W,E}^{*,0} = -\text{Ind}\mathcal{D}_{A,\Phi}$. By our regularity result, Proposition 3.7, any point $[A, \Phi]$ in $M_{W,E}^{*,0}$ has a smooth representative $(A, \Phi)$. Therefore, from the expressions for $d_{A,\Phi}^{0,*}$ in (2.38) and for $d_{A,\Phi}^{1}$ in (2.36) and the Sobolev multiplication and embedding theorems, we find that the operator $\mathcal{D}_{A,\Phi} = d_{A,\Phi}^{0,*} + d_{A,\Phi}^{1}: L_{k}^{2} \rightarrow L_{k-1}^{2}$ differs from

$$\begin{pmatrix}
d_{A}^{*} + d_{A}^{+} & 0 \\
0 & D_{A}
\end{pmatrix} : \begin{array}{c}
L_{k}^{2}(\Lambda^{1} \otimes \mathfrak{su}(E)) \oplus i\mathbb{R}_{Z} \\
\oplus \\
L_{k}^{2}(W^{+} \otimes E)
\end{array} \rightarrow L_{k-1}^{2}(\Lambda^{+} \otimes \mathfrak{su}(E)) \oplus L_{k-1}^{2}(\Lambda^{+} \otimes \mathfrak{su}(E))

by a compact operator and so has the same (real) index:

$\text{Ind}\mathcal{D}_{A,\Phi} = \text{Ind}(d_{A}^{*} + d_{A}^{+}) + \text{Ind}_{\mathbb{R}} D_{A} - 1$.

We recall from [20, Eq. (4.2.22)] that the operator

$d_{A}^{*} + d_{A}^{+}: L_{k}^{2}(\Lambda^{1} \otimes \mathfrak{su}(E)) \rightarrow L_{k-1}^{2}(\mathfrak{su}(E)) \oplus L_{k-1}^{2}(\Lambda^{+} \otimes \mathfrak{su}(E))$

has index

$\text{Ind}(d_{A}^{*} + d_{A}^{+}) = -2p_{1}(\mathfrak{su}(E)) - 3(1 - b^{1}(X) + b^{+}(X))$.

The complex index of the Dirac operator $D_{A}$ is given by

$$\text{Ind}_{\mathbb{C}} D_{A} = \langle (\hat{A}(X)) \text{ch}(E) e^{\frac{1}{2} c_{1}(W^{+})}, [X] \rangle$$

$$= \langle (1 - \frac{1}{24} p_{1}(X))(2 + c_{1}(E) \\
+ \frac{1}{2} c_{1}(E)^{2} - c_{2}(E))(1 + \frac{1}{2} c_{1}(W^{+}) + \frac{1}{8} c_{1}(W^{+})^{2}), [X] \rangle$$

$$= \langle -\frac{1}{12} p_{1}(X) + \frac{1}{4} c_{1}(W^{+})^{2} \\
+ \frac{1}{2} c_{1}(E)^{2} - c_{2}(E) + \frac{1}{2} c_{1}(E)c_{1}(W^{+}), [X] \rangle$$

$$= -\frac{1}{4} \sigma(X) + \frac{1}{4} c_{1}(W^{+})^{2} + \frac{1}{2} c_{1}(E)^{2} - c_{2}(E) + \frac{1}{2} c_{1}(E)c_{1}(W^{+})$$

$$= (\frac{1}{4} c_{1}(E)^{2} - c_{2}(E)) + \frac{1}{4} ((c_{1}(W^{+}) + c_{1}(E))^{2} - \sigma(X))$$

$$= \frac{1}{4} p_{1}(\mathfrak{su}(E)) + \frac{1}{4} ((c_{1}(W^{+}) + c_{1}(E))^{2} - \sigma(X)).$$

We obtain our dimension formula by adding these indices and noting that $\text{Ind}_{\mathbb{R}} D_{A} = 2 \text{Ind}_{\mathbb{C}} D_{A}$. q.e.d.

---

## 3. Regularity

Our goal in this section is to establish the basic regularity results for solutions to the PU(2) monopole equations (2.27). In §3.1 we show that global $L_1^2$ solutions to the first-order elliptic system comprising (2.27) and the Coulomb gauge equation (see §2) are necessarily $C^\infty$, while in §3.2 we show that global $L_k^2$ solutions to (2.27) are equivalent via an $L_{k+1}^2$ determinant-one, unitary automorphism of $E$ — provided $k \geq 2$ — to $C^\infty$ solutions to (2.27) in Coulomb gauge relative to some $C^\infty$ reference pair. In §3.3 and §3.4 we establish local versions of the results of §3.1 and §3.2. The regularity results and estimates of this section will be needed repeatedly throughout our work, so we state them here in sufficient generality to cover all of these applications. In the present article, we require the regularity results for our proof of transversality for the moduli space of PU(2) monopoles (see §5) and they form the cornerstone of our proofs of removable singularities and existence of an Uhlenbeck compactification (see §4). Furthermore, in sequels to this article [26], [27], the regularity results of this section are used to show that $L_1^2$ gluing solutions to (2.27) are necessarily $C^\infty$ and to analyse the Uhlenbeck-boundary behavior of the gluing and obstruction maps parametrizing the moduli space ends.

In order to simultaneously address all of the intended applications, the equations we find it convenient to consider here are a quasi-linear, inhomogeneous elliptic system consisting of a generalization of the equations (2.27) and Coulomb gauge equation for a pair $(A, \Phi) \in \tilde{C}_{W,E}(X)$. Specifically, we allow inhomogeneous, right-hand terms: the need for this generalization arises in our proofs of removable singularities, of regularity for gluing solutions to (2.27), and in analysing the Uhlenbeck-boundary behavior of gluing maps. Suppose that $(A_0, \Phi_0)$ is a fixed $C^\infty$ reference pair in $\tilde{C}_{W,E}(X)$: writing $(A, \Phi) = (A_0, \Phi_0) + (a, \phi)$, combining (2.27) with the Coulomb gauge equation, and allowing inhomogenous terms, we obtain an elliptic system of equations for a pair $(a, \phi)$ in $\Omega^1(X, \mathfrak{su}(E)) \oplus \Omega^0(X, W^+ \otimes E)$,

$$d_A^* a - (\cdot \Phi_0)^* \phi = \zeta,$$
$$\mathfrak{S}(A_0 + a, \Phi_0 + \phi) = (v_0, \psi_0),$$

Considering $A$ to be a connection on $\mathfrak{su}(E)$ and using the isomorphism ad : $\mathfrak{su}(E) \rightarrow \mathfrak{so}(\mathfrak{su}(E))$ to view $F_A$ as a section of $\Lambda^2 \otimes \mathfrak{su}(E)$, we write

---

(3.1) as

$$d_{A_0}^* a - (\cdot \Phi_0)^* \phi = \zeta,$$
$$F_{A_0+a}^+ - \left(\mathrm{id} + \tau_0 \otimes \mathrm{id}_{\mathfrak{su}(E)} + \vec{\tau} \cdot \vec{\mathfrak{m}}(A)\right) \rho^{-1}\left((\Phi_0 + \phi) \otimes (\Phi_0 + \phi)^*\right)_{00} = v_0,$$
$$(D_{A_0+a} + \rho(\vartheta_0) + \vec{\vartheta} \cdot \vec{\mathfrak{m}}(A))(\Phi_0 + \phi) = \psi_0,$$

where $(v_0, \psi_0) \in \Omega^+(X, \mathfrak{su}(E)) \oplus \Omega^0(X, W^- \otimes E)$. Recalling that $d_{A_0,\Phi_0}^0$ and $d_{A_0,\Phi_0}^1$ are the differential operators in the elliptic deformation complex (2.37) for the PU(2) monopole equations (2.27), the above system may be rewritten in the form

$$d_{A_0,\Phi_0}^{0,*} (a, \phi) = \zeta,$$
$$d_{A_0,\Phi_0}^{1} (a, \phi) + \{(a, \phi), (a, \phi)\} = -\mathfrak{S}(A_0, \Phi_0) + (v_0, \psi_0) =: (v, \psi),$$

where $(v, \psi) \in \Omega^+(X, \mathfrak{su}(E)) \oplus \Omega^0(X, W^- \otimes E)$, and the differentials $d_{A_0,\Phi_0}^{0,*}$ and $d_{A_0,\Phi_0}^{1}$ are given by (2.38) and (2.36). It will be convenient to view the quadratic term $\{(a, \phi), (a, \phi)\}$ as being defined via the following bilinear form,

$$\{(a, \phi), (b, \varphi)\}$$

$$\quad := \binom{(a \wedge b)^+ - \left(\mathrm{id} + \tau_0 \otimes \mathrm{id}_{\mathfrak{su}(E)} + \vec{\tau} \cdot \vec{\mathfrak{m}}(A)\right) \rho^{-1}(\phi \otimes \varphi^*)_{00}}{\rho(a) \varphi},$$

where $(b, \varphi) \in \Omega^1(X, \mathfrak{su}(E)) \oplus \Omega^0(X, W^+ \otimes E)$; we will further abbreviate $\{(a, \phi), (a, \phi)\}$ by $q(a, \phi)$ when convenient. Our elliptic system (3.1) then takes the simple shape

(3.2) $$\mathcal{D}_{A_0,\Phi_0}(a, \phi) + \{(a, \phi), (a, \phi)\} = (\zeta, v, \psi),$$

recalling from (2.39) that $\mathcal{D}_{A_0,\Phi_0} = d_{A_0,\Phi_0}^{0,*} + d_{A_0,\Phi_0}^{1}$. This is the form of the (inhomogeneous) Coulomb gauge and PU(2) monopole equations we will use for the majority of the basic regularity arguments.