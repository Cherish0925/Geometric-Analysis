---
retention_scope: session
part: 4
total_parts: 4
---

[Part 4/4 of: Peak sections and Bergman kernels on Kähler manifolds with complex hyperbolic cusps]

Since $S_{x, m, Y, i_{1}, \cdots, i_{p}}$ is the peak section of $\left.T_{x, m, i_{1}, \cdots, i_{p}}\right|_{Y_{m, q_{m, \mathfrak{K}}+1}}$, we can conclude that
$$T_{x, m, i_{1}, \cdots, i_{p}}\left(\eta S_{x, m, Y, i_{1}, \cdots, i_{p}}-u_{x, m, Y, i_{1}, \cdots, i_{p}}\right)=\left\|\left.T_{x, m, i_{1}, \cdots, i_{p}}\right|_{Y m, q_{m, \Re}+1}\right\| .$$
It follows that
$$\left\|\left.T_{x, m, i_{1}, \cdots, i_{p}}\right|_{Y_{m, q_{m, \text { } 2}+1}}\right\|^{2} \leq 200\left\|\left.T_{x, m, i_{1}, \cdots, i_{p}}\right|_{Z_{m, q_{m, \text { } 2}+1}}\right\|^{2} .$$
Similarly, we have
$$\left\|\left.T_{x, m, i_{1}, \cdots, i_{p}}\right|_{Z_{m, q_{m, \Re}+1}}\right\|^{2} \leq 200\left\|\left.T_{x, m, i_{1}, \cdots, i_{p}}\right|_{Y_{m, q_{m, \Re}+1}}\right\|^{2} .$$

Let $\left\{\widetilde{S}_{i}\right\}_{i \in I_{m, \mathfrak{K}}}$ be an $L^{2}$ orthonormal basis of $Z_{m, \mathfrak{K}}$. Then we have
$$\begin{aligned}
\frac{\rho_{M, \omega, m}}{\rho_{V, \omega_{V}, m}}= & \left(\sum_{q=1}^{q_{m, \mathfrak{K}}} \sum_{j=1}^{N_{q}}\left\|\widetilde{S}_{m, q, j}\right\|_{h^{m}}^{2}+\sum_{i \in I_{m, \mathfrak{K}}}\left\|\widetilde{S}_{i}\right\|_{h^{m}}^{2}\right) \cdot\left(\sum_{q=1}^{\infty} \sum_{j=1}^{N_{q}}\left\|a_{m, q} f_{S_{q, j}} e_{\mathcal{L}_{V}}^{m}\right\|_{h^{m}}^{2}\right)^{-1} \\
= & \left(\sum_{q=1}^{q_{m, \mathfrak{K}}} \sum_{j=1}^{N_{q}}\left|e_{\mathcal{L}_{V}}^{-m}\left(\widetilde{S}_{m, q, j}\right) h_{D}^{-\frac{1}{2}}\right|^{2}\right) \cdot\left(\sum_{q=1}^{\infty} \sum_{j=1}^{N_{q}}\left|a_{m, q} f_{S_{q, j}} h_{D}^{-\frac{1}{2}}\right|^{2}\right)^{-1} \\
& +\left(\sum_{i \in I_{m, \mathfrak{K}}}\left|e_{\mathcal{L}_{V}}^{-m}\left(\widetilde{S}_{i}\right) h_{D}^{-\frac{1}{2}}\right|^{2}\right) \cdot\left(\sum_{q=1}^{\infty} \sum_{j=1}^{N_{q}}\left|a_{m, q} f_{S_{q, j}} h_{D}^{-\frac{1}{2}}\right|^{2}\right)^{-1} .
\end{aligned}$$

By Lemma 3.1, there exists a constant $C_{6}$ depending only on $k, r$ and $\left(V, \omega_{V}, \mathcal{L}_{V}, h_{V}\right)$, such that
$$\sum_{p=0}^{k}\left\|\nabla^{p} f(x)\right\|_{\omega_{0}} \leq C_{6} \sum_{p=0}^{k} \sum_{1 \leq i_{1}, \cdots, i_{p} \leq 2 n}\left|\mathcal{Z}_{i_{1}}\left(\cdots\left(\mathcal{Z}_{i_{p}}(f)\right) \cdots\right)(x)\right|,$$
for any smooth function around $x$. As in the proof of Proposition 5.1, we see that the estimates (111), (106) and (107) imply that
$$\begin{aligned}
& \quad\left\|\left(\sum_{q=q_{m, \mathfrak{K}}+1}^{\infty} \sum_{j=1}^{N_{q}}\left|a_{m, q} f_{S_{q, j}} h_{D}^{-\frac{1}{2}}\right|^{2}\right) \cdot\left(\sum_{q=1}^{q_{m, \mathfrak{K}}} \sum_{j=1}^{N_{q}}\left|a_{m, q} f_{S_{q, j}} h_{D}^{-\frac{1}{2}}\right|^{2}\right)^{-1}\right\|_{C^{k ; \omega_{0}}}(x) \\
& \leq C_{6} \sum_{p=0}^{k} \sum_{1 \leq i_{1}, \cdots, i_{p} \leq 2 n} \left\lvert\, \mathcal{Z}_{i_{1}}\left(\cdots \left(\mathcal { Z } _ { i _ { p } } \left(\left(\sum_{q=q_{m, \mathfrak{K}+1}}^{\infty} \sum_{j=1}^{N_{q}}\left|a_{m, q} f_{S_{q, j}} h_{D}^{-\frac{1}{2}}\right|^{2}\right)\right.\right.\right.\right. \\
& \left.\left.\left.\quad \cdot\left(\left.\left|\sum_{q=1}^{q_{m, \mathfrak{K}}} \sum_{j=1}^{N_{q}}\right| a_{m, q} f_{S_{q, j}} h_{D}^{-\frac{1}{2}}\right|^{2}\right)^{-1}\right)\right) \cdots\right)(x) \mid \\
& \leq C_{7} e^{k(k-1) m} q_{m, \mathfrak{K}}^{2 k(k+n)}\left(\sum_{p=0}^{k} \sum_{1 \leq i_{1}, \cdots, i_{p} \leq 2 n}\left\|\left.T_{x, m, i_{1}, \cdots, i_{p}}\right|_{Y_{m, q_{m, \mathfrak{K}}+1}}\right\|^{2}\right. \\
& \leq C_{7}^{2}\left(q_{m, \mathfrak{K}}^{m+k+n} h_{D}(x)^{q_{m, \mathfrak{K}}-k-1}\right)^{k},
\end{aligned}$$
where $C_{7}>0$ is a constant depending only on $k, r$ and $\left(V, \omega_{V}, \mathcal{L}_{V}, h_{V}\right)$. Similarly, we have
$$\begin{aligned}
& \quad\left\|\left(\sum_{i \in I_{m, \mathfrak{K}}}\left|e_{\mathcal{L}_{V}}^{-m}\left(\widetilde{S}_{i}\right) h_{D}^{-\frac{1}{2}}\right|^{2}\right) \cdot\left(\sum_{q=1}^{\infty} \sum_{j=1}^{N_{q}}\left|a_{m, q} f_{S_{q, j}} h_{D}^{-\frac{1}{2}}\right|^{2}\right)^{-1}\right\|_{C^{k} ; \omega_{0}}(x) \\
& \leq e^{200 k} C_{7}^{2}\left(q_{m, \mathfrak{K}}^{m+k+n} h_{D}(x)^{q_{m, \mathfrak{K}}-k-1}\right)^{k} .
\end{aligned}$$

Then we can use (102) to find a constant $C_{8}>0$ depending only on $k, r$ and $\left(V, \omega_{V}, \mathcal{L}_{V}, h_{V}\right)$, such that
$$\begin{aligned}
& \quad\left\|\left(\sum_{q=1}^{q_{m, \mathfrak{K}}} \sum_{j=1}^{N_{q}}\left|e_{\mathcal{L}_{V}}^{-m}\left(\widetilde{S}_{m, q, j}\right) h_{D}^{-\frac{1}{2}}\right|^{2}\right) \cdot\left(\sum_{q=1}^{\infty} \sum_{j=1}^{N_{q}}\left|a_{m, q} f_{S_{q, j}} h_{D}^{-\frac{1}{2}}\right|^{2}\right)^{-1}\right\|_{C^{k} ; \omega_{0}}(x) \\
& \leq \quad C_{8} q^{2 n} e^{k^{2} m-\mathfrak{K} m}+C_{8}\left(q_{m, \mathfrak{K}}^{m+k+n} h_{D}(x)^{q_{m, \mathfrak{K}}-k-1}\right)^{k} .
\end{aligned}$$

Let $\mathfrak{K}>100\left(n+k+C_{5}\right)^{2}$ be a large constant, let $m_{1} \geq e^{4(\mathfrak{K}+|\log | \log r| |+|\log r|+2 n+2 k+6)}$ be an integer, and let $\mathcal{C}>m_{1}^{2}$ be a constant. Then for any $m \geq m_{1}$ and $x \in V_{m^{-c}}$, we have
$$q_{m, \mathfrak{K}}^{m+k+n} h_{D}(x)^{q_{m, \mathfrak{K}}-k-1} \leq e^{-m} .$$
It follows that
$$\sup _{V_{m}-\mathcal{C}}\left\|\frac{\rho_{M, \omega, m}(x)}{\rho_{V, \omega_{V}, m}(x)}-1\right\|_{C^{k} ; \omega_{0}} \leq C_{9} e^{-m}, \forall m \geq m_{1},$$
where $C_{9}>0$ is a constant depending only on $k, r$ and $\left(V, \omega_{V}, \mathcal{L}_{V}, h_{V}\right)$.
When $x \in V \backslash V_{m-\mathcal{C}}$, the estimate (97) is a consequence of Proposition 5.3. This completes the proof. \(\square\)

Now we consider Theorem 1.4. In order to consider the case where $\Gamma$ is not torsion free, we need to recall some basic notations about orbifolds and orbifold line bundles.

An $n$-dimensional complex orbifold is a composite concept formed of a second countable Hausdorff paracompact topological space $X$ and a collection of data $\left\{\widetilde{U}_{x}, G_{x}, U_{x}, p_{x}\right\}_{x \in X}$ with the following property. For each point $x \in X$, there exist an open neighborhood $U_{x}$ of $x$ in $X$, a connected open subset $\widetilde{U}_{x} \subset \mathbb{C}^{n}$ and a continuous map $p_{x}: \widetilde{U}_{x} \rightarrow U_{x}$ together with a finite group $G$ of biholomorphic automorphisms of $\widetilde{U}_{x}$ such that $p_{x}$ induces an homeomorphism between $U_{x}$ and $\widetilde{U}_{x} / G$. If $x \in U_{y}$ for some $y \in X$, then there exist a neighborhood $V_{x}$ of $x$ and a holomorphic map $\phi: p_{x}^{-1}\left(V_{x}\right) \rightarrow \widetilde{U}_{y}$ such that $p_{y}=p_{x} \circ \phi$.

Let $G_{x}=\{g \in G: g(x)=x\}$. Then $G_{x}$ is unique up to isomorphism, and the complex manifold $X_{\text {reg }}=\left\{x \in X:\left|G_{x}\right|=1\right\}$ is an open dense subset of $X$. A Kähler metric $\omega$ (resp. line orbibundle $\mathcal{L}$ ) on $X$ is a Kähler metric $\omega$ (resp. line bundle $\mathcal{L}$ ) on $X_{\text {reg }}$ such that for each $x \in X, p_{x}^{*} \omega$ is a restriction of a Kähler metric $\widetilde{\omega}$ (resp. line bundle $\widetilde{\mathcal{L}}$ ) on $\widetilde{U}_{x}$ on $p_{x}^{-1}\left(U_{x} \cap X_{\text {reg }}\right)$. Similarly, a hermitian metric $h$ on $\mathcal{L}$ is a hermitian metric $h$ on $\left.\mathcal{L}\right|_{X_{\text {reg }}}$ such that for each $x \in X, p_{x}^{*} h$ is a restriction of a hermitian metric $\widetilde{h}_{\widetilde{U}_{x}}$ on $\left.\widetilde{\mathcal{L}}\right|_{\widetilde{U}_{x}}$ on $p_{x}^{-1}\left(U_{x} \cap X_{\text {reg }}\right)$.

A Kähler orbifold is defined in terms of a complex orbifold $X$ and a Kähler metric $\omega$ on $X$. We say that a line orbibundle $\mathcal{L}$ on a complex orbifold $X$ is positive, if there exists a hermitian $h$ on $\mathcal{L}$ such that $\frac{1}{2 \pi} \operatorname{Ric}(h)$ is a Kähler metric on $X$, where $\operatorname{Ric}(h)=-\sqrt{-1} \partial \bar{\partial}(\log (h))$. This $\omega=\frac{1}{2 \pi} \operatorname{Ric}(h)$ is a polarized Kähler metric on $X$. A global section $S$ of $\mathcal{L}$ on $X$ is a section $S \in H^{0}\left(X_{\text {reg }},\left.\mathcal{L}\right|_{X_{\text {reg }}}\right)$ that can be extended on each $\widetilde{U}_{x}$. Let $H^{0}(X, \mathcal{L})$ denote the linear space of all these global sections of $\mathcal{L}$. Then we can define the Bergman kernels on orbifolds just as in the beginning of Section 1.

Then we recall some basic properties of Bergman kernels on orbifolds. Let $(X, \omega)$ be a complete Kähler orbifold, and $(\mathcal{L}, h)$ be a Hermitian line orbibundle on $X$. Fix $x \in X$. Then there exists an open neighborhood $U_{x}$ of $x$ such that $U_{x} \cong \widetilde{U}_{x} / G_{x}$ for some open neighborhood $\widetilde{U}_{x}$ of $0 \in \mathbb{C}^{n}$. Let $p_{x}$ denote the quotient map $\widetilde{U}_{x} \rightarrow \widetilde{U}_{x} / G_{x} \cong U_{x}$. Assume that $p_{x}(0)=x, \widetilde{\omega}$ is an extension of $\left.p_{x}^{*} \omega\right|_{U_{x} \cap X_{\text {reg }}}$ on $\widetilde{U}_{x}$, and $(\widetilde{\mathcal{L}}, \widetilde{h})$ is an extension of $\left(\left.p_{x}^{*} \mathcal{L}\right|_{U_{x} \cap X_{\text {reg }}},\left.p_{x}^{*} h\right|_{U_{x} \cap X_{\text {reg }}}\right)$ on $\widetilde{U}_{x}$. Then we see that the action of $G_{x}$ on $U_{x}$ can be extended to an action on $\widetilde{\mathcal{L}}$ that preserves $\widetilde{h}$, and $\widetilde{\mathcal{L}} / G_{x} \cong \mathcal{L}$. Let $H_{L^{2}}^{0}\left(\widetilde{U}_{x}, \widetilde{\omega}, \widetilde{\mathcal{L}}^{m}, \widetilde{h}^{m}\right)_{G_{x}}$ be the subspace of $H_{L^{2}}^{0}\left(\widetilde{U}_{x}, \widetilde{\omega}, \widetilde{\mathcal{L}}^{m}, \widetilde{h}^{m}\right)$ containing all holomorphic sections that are invariant under the action of $G_{x}$. Then there exist an orthonormal basis $\left\{S_{m, i}\right\}_{i \in I_{m}}$ of $H_{L^{2}}^{0}\left(\widetilde{U}_{x}, \widetilde{\omega}, \widetilde{\mathcal{L}}^{m}, \widetilde{h}^{m}\right)$ and a subset $I_{m, 1} \subset I_{m}$, such that $\left\{S_{m, i}\right\}_{i \in I_{m, 1}}$ is an orthonormal basis of $H_{L^{2}}^{0}\left(\widetilde{U}_{x}, \widetilde{\omega}, \widetilde{\mathcal{L}}^{m}, \widetilde{h}^{m}\right)_{G_{x}}$. Then
$$\rho_{U_{x}, \omega, \mathcal{L}^{m}, h^{m}}\left(p_{x}(z)\right)=\left|G_{x}\right| \sum_{i \in I_{m, 1}}\left\|S_{m, i}(z)\right\|_{h^{m}}^{2}=\sum_{g \in G_{x}} \sum_{i \in I_{m}} h^{m}\left(g\left(S_{m, i}\right)(z), S_{m, i}(z)\right),$$
and similarly,
$$p_{x}^{*} B_{U_{x}, \omega, \mathcal{L}^{m}, h^{m}}\left(p_{x}(z), p_{x}(w)\right)=\sum_{g \in G_{x}} \sum_{i \in I_{m}} g\left(S_{m, i}\right)(z) \otimes S_{m, i}(w)^{*} .$$

Assume that there exists a section $e_{\widetilde{\mathcal{L}}} \in H^{0}\left(\widetilde{U}_{x}, \widetilde{\mathcal{L}}\right)$ such that $e_{\widetilde{\mathcal{L}}} \neq 0$ on $\widetilde{U}_{x}$, and $\left\|e_{\widetilde{\mathcal{L}}}\right\|_{h}$ is invariant under the action of $G_{x}$. Then there exists a homomorphism $\Theta_{G_{x}}^{\text {orb }}: G_{x} \rightarrow U(1) \subset \mathbb{C}^{*}$ such that $g\left(e_{\widetilde{\mathcal{L}}}\right)=\Theta_{G_{x}}^{\text {orb }}(g) e_{\widetilde{\mathcal{L}}}, \forall g \in G_{x}$. Clearly, $\Theta_{G_{x}}^{\text {orb }}$ is independent of the choice of $e_{\widetilde{\mathcal{L}}}$.

Now we can give an estimate of the Bergman kernel function on $\mathbb{B}^{n} / \Gamma$ far away from the cusp. The following lemma has actually been proved by Dai-Liu-Ma [6] using the heat kernel method, but here we give a proof that only relies on the peak section method.

Lemma 5.6. We follow the notations and assumptions above. For any constants $n, \Lambda, k, \epsilon>0$, there are constant $\delta, C, m_{0}>0$ with the following property. Let $(X, \omega)$ be a complete Kähler orbifold with $\operatorname{Ric}(\omega) \geq-\Lambda \omega,(\mathcal{L}, h)$ be a Hermitian line orbibundle on $X$ with $\operatorname{Ric}(h) \geq \epsilon \omega, x \in X$ and $m \geq m_{0}$. Assume that $G_{x} \leqslant U(n)$, and there exists a constant $r \geq \frac{\epsilon \log (m)}{\sqrt{m}}$ such that the open set $U_{x}$ containing $B_{r}(x)$. Suppose that the bisectional curvature $B K=-1$ on $U_{x}$, and $\operatorname{Ric}(h)=(n+1) \omega$ on $U_{x}$. Then
$$\left\|\rho_{\omega, m} \circ p_{x}(z)-\frac{(2 \pi)^{-n}(m n-1)!}{(m n-n-1)!} \sum_{g \in G_{x}} \frac{\Theta_{G_{x}}^{o r b}(g)^{m}\left(1-|z|^{2}\right)^{m n}}{\left(1-\left\langle g^{-1} z, z\right\rangle\right)^{m n}}\right\|_{C^{k} ; B_{\frac{r}{2}}(0)} \leq C e^{-\delta m r^{2}},$$
where $\rho_{\omega, m}$ is the Bergman kernel function on $(X, \omega, \mathcal{L}, h)$, and $\langle z, w\rangle=\sum_{i=1}^{n} z_{i} \bar{w}_{i}, \forall z, w \in \mathbb{C}^{n}$.
Proof. By assumptions, we can consider $\widetilde{U}_{x}=p_{x}^{-1}\left(U_{x}\right)$ as an open neighborhood of $0 \in \mathbb{B}^{n}$ such that $\widetilde{U}_{x}$ is invariant under the action of $G_{x} \leqslant U(n)$. Then $\left(\widetilde{U}_{x}, \widetilde{\omega}, \widetilde{\mathcal{L}}, \widetilde{h}\right) \cong\left(\widetilde{U}_{x}, \omega_{\mathbb{B}^{n}}, \mathcal{K}_{\mathbb{B}^{n}}, h_{\mathbb{B}^{n}}\right)$, where $\left(\mathcal{K}_{\mathbb{B}^{n}}, h_{\mathbb{B}^{n}}\right)$ is the Hermitian line bundle in Theorem 1.4.

Let $e_{\mathcal{K}_{\mathbb{B}^{n}}} \in H^{0}\left(\mathbb{B}^{n}, \mathcal{K}_{\mathbb{B}^{n}}\right)$ such that $\left\|e_{\mathcal{K}_{\mathbb{B}^{n}}}\right\|_{h_{\mathcal{K}^{n}} n}^{2}=\left(1-|z|^{2}\right)^{n}$. Then we can describe the action $g: H^{0}\left(\mathbb{B}^{n}, \mathcal{K}_{\mathbb{B}^{n}}\right) \rightarrow H^{0}\left(\mathbb{B}^{n}, \mathcal{K}_{\mathbb{B}^{n}}\right)$ by $g\left(f e_{\mathcal{K}_{\mathbb{B}^{n}}}\right)=\left(\Theta_{G_{x}}^{\text {orb }}(g) \cdot f \circ g^{-1}\right) e_{\mathcal{K}_{\mathbb{B}^{n}}}$, for any holomorphic section $f e_{\mathcal{K}_{\mathbb{B}^{n}}} \in H^{0}\left(\mathbb{B}^{n}, \mathcal{K}_{\mathbb{B}^{n}}\right)$. Write
$$S_{m, P}=\sqrt{\frac{(m n+|P|-1)!}{2^{n} \pi^{n} p_{1}!\cdots p_{n}!(m n-n-1)!}} z^{P} e_{\mathcal{K}_{\mathbb{B}^{n}}}^{m}=f_{m, P}(z) e_{\mathcal{K}_{\mathbb{B}} n}^{m} \in H^{0}\left(\mathbb{B}^{n}, \mathcal{K}_{\mathbb{B}^{n}}^{m}\right),$$
for each multi-index $P \in \mathbb{Z}_{\geq 0}^{n}$ and integer $m \geq 2$. Since $\left\{S_{m, P}\right\}_{P \in \mathbb{Z}_{\geq 0}^{n}}$ is an orthonormal basis of $H_{L^{2}}^{0}\left(\mathbb{B}^{n}, \omega_{\mathbb{B}^{n}}, \mathcal{K}_{\mathbb{B}^{n}}^{m}, h_{\mathbb{B}^{n}}^{m}\right)$, we can apply (119) and (120) to show that for any integer $m \geq 2$,
$$\begin{aligned}
\rho_{\mathbb{B}^{n} / G_{x}, \omega_{\mathbb{B}^{n}}, \mathcal{K}_{\mathbb{B}^{n}} / G_{x}, h_{\mathbb{B}^{n}, m}^{m}\left(p_{x}(z)\right)} & =\sum_{g \in G_{x}} \sum_{P \in \mathbb{Z}_{\geq 0}^{n}} h^{m}\left(g\left(S_{m, P}\right)(z), S_{m, P}(z)\right) \\
& =\sum_{g \in G_{x}} \Theta_{G_{x}}^{o r b}(g)^{m}\left(\sum_{P \in \mathbb{Z}_{\geq 0}^{n}} f_{m, P}\left(g^{-1}(z)\right) \overline{f_{m, P}(z)}\right)\left(1-|z|^{2}\right)^{m n} \\
& =\frac{(2 \pi)^{-n}(m n-1)!}{(m n-n-1)!} \sum_{g \in G_{x}} \Theta_{G_{x}^{o r b}}^{o r b}(g)^{m} \frac{\left(1-|z|^{2}\right)^{m n}}{\left(1-\left\langle g^{-1} z, z\right\rangle\right)^{m n}},
\end{aligned}$$
and
$$\begin{aligned}
p_{x}^{*} B_{\mathbb{B}^{n} / G_{x}, \omega_{\mathbb{B}} n}, & \mathcal{K}_{\mathbb{B}^{n}} / G_{x}, h_{\mathbb{B}^{n}}^{m}, m\left(p_{x}(z), p_{x}(w)\right) \\
& =\frac{(2 \pi)^{-n}(m n-1)!}{(m n-n-1)!} \sum_{g \in G_{x}} \Theta_{G_{x}}^{o r b}(g)^{m} \frac{\left(1-|w|^{2}\right)^{m n}}{\left(1-\left\langle g^{-1} z, w\right\rangle\right)^{m n}} e_{\mathcal{K}_{\mathbb{B}} n}^{m}(z) \otimes e_{\mathcal{K}_{\mathbb{B}} n}^{-m}(w),
\end{aligned}$$

Now we only need to show that
$$\left\|\rho_{X, \omega, \mathcal{L}, m} \circ p_{x}(z)-\rho_{\mathbb{B}^{n} / G_{x}, \omega_{\mathbb{B}} n,\left(\mathcal{K}_{\mathbb{B}^{n}} / G_{x}\right)^{m}, h_{\mathbb{B}^{n}}^{m}} \circ p_{x}(z)\right\|_{C^{k}, B_{\frac{r}{2}}(0)} \leq C e^{-\delta m r^{2}} .$$
We can see that the proof of Theorem 1.1 actually leads to the estimate (124), noting that (122) and (123) implies that the integral of peak sections defined by a distribution that support is a point in $B_{\frac{r}{2}}(x)$ on $B_{\frac{4 r}{5}}(x) \backslash B_{\frac{3 r}{5}}(x)$ decays exponentially as $m r^{2} \rightarrow \infty$. \(\square\)

Now we are in place to prove Theorem 1.4.
Proof of Theorem 1.4: Since $\Gamma$ is a lattice, the quotient space $X=\mathbb{B}^{n} / \Gamma$ is a complete Kähler orbifold, and there exist a finite collection of disjoint open subsets $U_{i} \subset X, i=1, \cdots, N$, and complex hyperbolic cusps $\left(V_{i} / \Gamma_{V_{i}}, \omega_{V_{i}}, \mathcal{L}_{V_{i}} / \Gamma_{V_{i}}, h_{V_{i}}\right)$ such that $\left(U_{i}, \omega_{\mathbb{B}^{n}}\right) \cong\left(V_{i} / \Gamma_{V_{i}}, \omega_{V_{i}}\right)$, and $X \backslash\left(\cup_{i=1}^{N} U_{i}\right)$ is compact. When $\Gamma$ is cocompact, the orbifold $X$ is compact, and hence $N=0$.

Note that the localization principle, Theorem 1.1, holds for complete Kähler orbifolds with asymptotic complex hyperbolic cusps. Then we can apply Lemma 5.6 to conclude that
$$\sup _{X \backslash\left(\cup_{i=1}^{N} U_{i}\right)} \rho_{X, \omega_{\mathbb{B}} n}, \mathcal{K}_{X}, h_{X}, m=c_{m} m^{n}+O\left(m^{n-1}\right), \text { as } m \rightarrow \infty .$$
where $\left\{c_{i}\right\}_{i=1}^{\infty}$ is a sequence of positive constants depending only on $n$ and $\Gamma$, such that $c_{i}=c_{i+\mathcal{N}_{1}}$ for some integer $\mathcal{N}_{1}=\mathcal{N}_{1}(n, \Gamma)>0, \forall i \in \mathbb{N}$.

Similarly, Corollary 23 now implies that there exist an integer $\mathcal{N}_{2}=\mathcal{N}_{2}(n, \Gamma)>0$ and a sequence of positive constants $\left\{c_{i}^{\prime}\right\}_{i=1}^{\infty}$ depending only on $n$ and $\Gamma$, such that $c_{i}^{\prime}=c_{i+\mathcal{N}_{2}}^{\prime}, \forall i \in \mathbb{N}$, and
$$\sup _{\cup_{i=1}^{N} U_{i}} \rho_{X, \omega_{\mathbb{B}} n}, \mathcal{K}_{X}, h_{X}, m=c_{m}^{\prime} m^{n+\frac{1}{2}}+O\left(m^{n}\right), \text { as } m \rightarrow \infty .$$

Combining (125) with (126), we can obtain (10) and (11). When $\Gamma$ is neat, $X$ becomes a manifold, and the all group $\Gamma_{i}$ are trivial. It follows that $\mathcal{N}=1$ in this case, which proves the theorem. \(\square\)

\section*{6. Conflict of interest statement}

On behalf of all authors, the corresponding author states that there is no conflict of interest.

\section*{7. Data availability statements}

My manuscript has no associated data.

\section*{References}
\begin{itemize}
\item[] [1] A. Abbes, E. Ullmo: Comparaison des mètriques d'Arakelov et de Poincarè sur $X_{0}(N)$, Duke Math. J. 80 (1995), 295-307.
\item[] [2] M. Anderson: Convergence and rigidity of manifolds under Ricci curvature bounds, Invent. Math. 102 (1990), 429-445.
\item[] [3] H. Auvray, X.-N. Ma, G. Marinescu: Bergman kernels on punctured Riemann surfaces, Math. Ann. 379 (2021), 951-1002.
\item[] [4] H. Auvray, X.-N. Ma, G. Marinescu: Quotient of Bergman kernels on punctured riemann surfaces, Math. Z. 301 (2022), 2339-2367.
\item[] [5] D. Catlin: The Bergman kernel and a theorem of Tian, Analysis and geometry in several complex variables (Katata, 1997), 1-23, Trends Math., Birkhäuser Boston, Boston, MA, 1999.
\item[] [6] X.-Z. Dai, K.-F.Liu, X.-N. Ma: On the asymptotic expansion of Bergman kernel, J. Differential Geom. 72 (2006), no. 1, 1-41.
\end{itemize}
\begin{itemize}
\item[] [7] V. Datar, X. Fu, J. Song: Kähler-Einstein metrics on near an isolated log-canonical singularity, preprint. arXiv:2106.05486 (2021).
\item[] [8] J.-P. Demailly: Analytic methods in algebraic geometry, Surveys of Modern Mathematics, 1. International Press, Somerville, MA; Higher Education Press, Beijing, 2012.
\item[] [9] S. Donaldson: Scalar curvature and projective embeddings. I, J. Differential Geom. 59 (2001), 479-522.
\item[] [10] X. Fu, H.-J. Hein, X.-M. Jiang: Asymptotics of Kähler-Einstein metrics on complex hyperbolic cusps, preprint. arXiv:2108.13390 (2021).
\item[] [11] D. Gilbarg, N. S. Trudinger: Elliptic partial differential equations of second order, Second edition. Grundlehren der Mathematischen Wissenschaften, 224. Springer-Verlag, Berlin, 1983.
\item[] [12] P. Griffiths, J. Harris: Principles of algebraic geometry, Pure and Applied Mathematics. Wiley-Interscience, New York, 1978.
\item[] [13] M. Gromov: Metric structures for Riemannian and non-Riemannian spaces, Birkhäuser, Boston, 1999.
\item[] [14] H. Hezari, Z.-Q. Lu, H. Xu: Off-diagonal asymptotic properties of Bergman kernels associated to analytic Kähler potentials, Internat. Math. Res. Notices. (2020), 2241-2286.
\item[] [15] L. Hörmander: An introduction to complex analysis in several variables, Van Nostrand, Princeton, NJ, 1973.
\item[] [16] L. Hörmander: Linear Partial Differential Operators, Grundlehren der Mathematischen Wissenschaften, 116. Springer, Berlin, 1963. Springer-Verlag, Berlin, 1983.
\item[] [17] D. Huybrechts: Complex geometry - An introduction, Universitext. Springer-Verlag, Berlin, 2005.
\item[] [18] J. Jorgenson, J. Kramer: Bounding the sup-norm of automorphic forms, Geom. Funct. Anal. 14 (2004), 1267-1277.
\item[] [19] C.-J. Liu: The asymptotic Tian-Yau-Zelditch expansion on Riemann surfaces with constant curvature, Taiwanese J. Math. 14 (2010), 1665-1675.
\item[] [20] C.-J. Liu, Z.-Q. Lu: Abstract Bergman kernel expansion and its applications, Trans. Amer. Math. Soc. 368 (2016), 1467-1495.
\item[] [21] Z.-Q. Lu: On the lower order terms of the asymptotic expansion of Tian-Yau-Zelditch, Amer. J. Math. 122 (2000), 235-273.
\item[] [22] Z.-Q. Lu, G. Tian: The log term of the Szegö kernel, Duke Math. J. 125 (2004), 351-387.
\item[] [23] B. Lukas: The local fundamental group of a Kawamata log terminal singularity is finite, Invent. Math. 226 (2021), 845-896.
\item[] [24] X.-N. Ma, G. Marinescu: Holomorphic Morse inequalities and Bergman kernels, Progress in Mathematics, 254. Birkhäuser Verlag, Basel, 2007.
\item[] [25] P. Michel, E. Ullmo: Points de petite hauteur sur les courbes modulaires $X_{0}(N)$, Invent. Math. 131 (1998), 645-674.
\item[] [26] N.-M. Mok: Projective algebraicity of minimal compactifications of complex-hyperbolic space forms of finite volume, Progress in Mathematics, 296, Birkhäuser/Springer, New York, 2012.
\item[] [27] P. Petersen: Convergence theorems in Riemannian geometry, Comparison geometry, 167-202. Math. Sci. Res. Inst. Publ., 30. Cambridge Univ. Press, Cambridge, 1997.
\item[] [28] M. S. Raghunathan: Discrete subgroups of Lie groups, Ergebnisse der Mathematik und ihrer Grenzgebiete, Band 68. Springer-Verlag, New York-Heidelberg, 1972.
\item[] [29] W.-D. Ruan: Canonical coordinates and Bergman metrics, Comm. Anal. Geom. 6 (1998), 589-631.
\item[] [30] S.-J. Sun: Projective embedding of pairs and logarithmic K-stability, Math. Ann. 375 (2019), 1307-1336.
\item[] [31] S.-J. Sun, S. Sun: Projective embedding of log Riemann surfaces and K-stability, J. Geom. Anal. 31 (2021), 5526-5554.
\item[] [32] G. Tian: Canonical metrics in Kähler geometry, Notes taken by Meike Akveld. Lectures in Mathematics ETH Zürich, Birkhäuser Verlag, Basel, 2000.
\item[] [33] G. Tian: On a set of polarized Kähler metrics on algebraic manifolds, J. Differ. Geom. 32 (1990), 99-130.
\item[] [34] K.-W. Zhang: A quantization proof of the uniform Yau-Tian-Donaldson conjecture, preprint. arXiv:2102.02438 (2021).
\item[] [35] S. Zelditch: Szegö kernels and a theorem of Tian, Internat. Math. Res. Notices. (1998), 317-331.
\end{itemize}

Beijing International Center for Mathematical Research, Peking University, Beijing, 100871, China Email address: zhoushx19@pku.edu.cn