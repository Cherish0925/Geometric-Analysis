---
retention_scope: session
part: 2
total_parts: 7
---

[Part 2/7 of: PU(2) Monopoles, I: Regularity, Uhlenbeck Compactness ...]

Proof. We first restrict the map $\boldsymbol{\Psi}$ to a neighborhood $B_{\text {id }}(\delta) \times_{\operatorname{Stab}_{A_{0}, \Phi_{0}}} \mathbf{S}_{A_{0}, \Phi_{0}}$, which is diffeomorphic to the neighborhood $B_{\mathrm{id}}^{\perp}(\delta) \times \mathbf{S}_{A_{0}, \Phi_{0}}$ in $\operatorname{Stab}_{A_{0}, \Phi_{0}}^{\perp} \times \mathbf{S}_{A_{0}, \Phi_{0}}$ by Claim 2.9. The differential of the induced map
$$\boldsymbol{\Psi}: \operatorname{Stab}_{A_{0}, \Phi_{0}}^{\perp} \times \mathbf{S}_{A_{0}, \Phi_{0}} \rightarrow \tilde{\mathcal{C}}_{W, E}, \quad(u, A, \Phi) \mapsto u(A, \Phi),$$
at $\left(\operatorname{id}_{E}, A_{0}, \Phi_{0}\right)$ is given by
$$\begin{gathered}
(D \boldsymbol{\Psi})_{\left(\mathrm{id}, A_{0}, \Phi_{0}\right)}: T_{\mathrm{id}} \operatorname{Stab}_{A_{0}, \Phi_{0}}^{\perp} \oplus T_{A_{0}, \Phi_{0}} \mathbf{S}_{A_{0}, \Phi_{0}} \rightarrow T_{A_{0}, \Phi_{0}} \tilde{\mathcal{C}}_{W, E}, \\
(\zeta, a, \phi) \mapsto-d_{A_{0}, \Phi_{0}}^{0} \zeta+(a, \phi),
\end{gathered}$$
where we recall that $T_{A_{0}, \Phi_{0}} \mathbf{S}_{A_{0}, \Phi_{0}}=\mathbf{K}_{A_{0}, \Phi_{0}}$ and
$$T_{\mathrm{id}} \operatorname{Stab}_{A_{0}, \Phi_{0}}^{\perp}=\left(\operatorname{Ker}\left(\left.d_{A_{0}, \Phi_{0}}^{0}\right|_{L_{k+1}^{2}} ^{2}\right)\right)^{\perp}=\operatorname{Im}\left(\left.d_{A_{0}, \Phi_{0}}^{0, *}\right|_{L_{k+2}^{2}}\right) .$$
Using the $L^{2}$-orthogonal decomposition (2.9) of the range we see that the map
$$-d_{A_{0}, \Phi_{0}}^{0} \oplus \operatorname{id}_{E}:\left(\operatorname{Ker}\left(\left.d_{A_{0}, \Phi_{0}}^{0}\right|_{L_{k+1}^{2}} ^{2}\right)\right)^{\perp} \oplus \mathbf{K}_{A_{0}, \Phi_{0}} \rightarrow \operatorname{Im}\left(\left.d_{A_{0}, \Phi_{0}}^{0}\right|_{L_{k+1}^{2}}\right) \oplus \mathbf{K}_{A_{0}, \Phi_{0}}$$
given by $(\zeta, b, \psi) \mapsto-d_{A_{0}, \Phi_{0}}^{0} \zeta+(b, \psi)$ is a Hilbert space isomorphism. So, by the Hilbert space implicit function theorem, there are positive constants $\varepsilon=\varepsilon\left(A_{0}, \Phi_{0}, k\right)$ and $\delta=\delta\left(A_{0}, \Phi_{0}, k\right)$ and an open neighborhood $\mathcal{U}_{A_{0}, \Phi_{0}} \subset \tilde{\mathcal{C}}_{W, E}$ such that the map
$$\boldsymbol{\Psi}: B_{\mathrm{id}}^{\perp}(\delta) \times \mathbf{B}_{A_{0}, \Phi_{0}}(\varepsilon) \rightarrow \mathcal{U}_{A_{0}, \Phi_{0}}, \quad(u, A, \Phi) \mapsto u(A, \Phi),$$
gives a diffeomorphism from an open neighborhood of $\left(\operatorname{id}_{E}, A_{0}, \Phi_{0}\right)$ onto an open neighborhood of $\left(A_{0}, \Phi_{0}\right)$. In particular, we obtain a map $\mathcal{U}_{A_{0}, \Phi_{0}} \rightarrow \operatorname{Stab}_{A_{0}, \Phi_{0}}^{\perp}$, given by $(A, \Phi) \mapsto u=u_{A, \Phi}$, such that
$$\boldsymbol{\Psi}^{-1}(A, \Phi)=\left(u, u^{-1}(A, \Phi)\right) \in B_{\mathrm{id}}^{\perp}(\delta) \times \mathbf{B}_{A_{0}, \Phi_{0}}(\varepsilon) \subset \operatorname{Stab}_{A_{0}, \Phi_{0}}^{\perp} \times \mathbf{B}_{A_{0}, \Phi_{0}}(\varepsilon) .$$

Hence, for any $(A, \Phi) \in \mathcal{U}_{A_{0}, \Phi_{0}}$ there is a unique $u \in B_{\mathrm{id}}^{\perp}(\delta)$ such that $u^{-1}(A, \Phi)-$ $\left(A_{0}, \Phi_{0}\right) \in \mathbf{K}_{A_{0}, \Phi_{0}}$ :
$$d_{A_{0}, \Phi_{0}}^{0, *}\left(u^{-1}\left(A_{1}, \Phi_{1}\right)-\left(A_{0}, \Phi_{0}\right)\right)=0 .$$
The neighborhood $\mathbf{B}_{A_{0}, \Phi_{0}}(\varepsilon)$ is $\operatorname{Stab}_{A_{0}, \Phi_{0}}$-invariant: if $(A, \Phi) \in \mathbf{B}_{A_{0}, \Phi_{0}}(\varepsilon)$ and $\gamma \in$ $\operatorname{Stab}_{A_{0}, \Phi_{0}}$, then
$$\begin{aligned}
\left\|\gamma\left(A_{1}, \Phi_{1}\right)-(A, \Phi)\right\|_{L_{k, A_{0}}^{2}} & =\left\|\left(A_{1}, \Phi_{1}\right)-\gamma^{-1}(A, \Phi)\right\|_{L_{k, \gamma}^{2}-\left(A_{0}\right)} \\
& =\left\|\left(A_{1}, \Phi_{1}\right)-(A, \Phi)\right\|_{L_{k, A_{0}}^{2}}<\varepsilon,
\end{aligned}$$
and
$$\begin{aligned}
d_{A_{0}, \Phi_{0}}^{0, *}\left(\gamma(A, \Phi)-\left(A_{0}, \Phi_{0}\right)\right) & =\gamma\left(d_{\gamma^{-1}\left(A_{0}, \Phi_{0}\right)}^{0, *}\left((A, \Phi)-\left(A_{0}, \Phi_{0}\right)\right)\right) \\
& =\gamma\left(d_{A_{0}, \Phi_{0}}^{0, *}\left((A, \Phi)-\left(A_{0}, \Phi_{0}\right)\right)\right)=0,
\end{aligned}$$
so $\gamma(A, \Phi) \in \mathbf{B}_{A_{0}, \Phi_{0}}(\varepsilon)$.
The group ${ }^{\circ} \mathcal{G}_{E}$ acts on ${ }^{\circ} \mathcal{G}_{E} \times \mathbf{S}_{A_{0}, \Phi_{0}}$ by $(u, A, \Phi) \mapsto(v u, A, \Phi)$, and so gives a diffeomorphism
$$B_{\mathrm{id}}(\delta) \times \mathbf{B}_{A_{0}, \Phi_{0}}(\varepsilon) \rightarrow B_{v}(\delta) \times \mathbf{B}_{A_{0}, \Phi_{0}}(\varepsilon), \quad(u, A, \Phi) \rightarrow(v u, A, \Phi),$$
and as this action commutes with the given action of $\operatorname{Stab}_{\mathcal{A}_{0}, \Phi_{0}}$, it descends to a diffeomorphism
$$B_{\mathrm{id}}(\delta) \times_{\operatorname{Stab}_{A_{0}, \Phi_{0}}} \mathbf{B}_{A_{0}, \Phi_{0}}(\varepsilon) \rightarrow B_{v}(\delta) \times_{\operatorname{Stab}_{A_{0}, \Phi_{0}}} \mathbf{B}_{A_{0}, \Phi_{0}}(\varepsilon), \quad[u, A, \Phi] \rightarrow[v u, A, \Phi],$$
for each $v \in{ }^{\circ} \mathcal{G}_{E}$. Consequently, the ${ }^{\circ} \mathcal{G}_{E}$-equivariant map
$${ }^{\circ} \mathcal{G}_{E} \times_{\operatorname{Stab}_{A_{0}, \Phi_{0}}} \mathbf{B}_{A_{0}, \Phi_{0}}(\varepsilon) \rightarrow \tilde{\mathcal{C}}_{W, E}$$
is a diffeomorphism onto its image, as desired. \(\square\)

Plainly, $[\gamma(A, \Phi)]=[A, \Phi]$ for each $\gamma \in \operatorname{Stab}_{A_{0}, \Phi_{0}}$ and $(A, \Phi) \in \mathbf{B}_{A_{0}, \Phi_{0}}(\varepsilon)$ and hence, the projection $\pi: \mathbf{B}_{A_{0}, \Phi_{0}}(\varepsilon) \rightarrow \mathcal{C}_{W, E}$ factors through $\mathbf{B}_{A_{0}, \Phi_{0}}(\varepsilon) / \operatorname{Stab}_{A_{0}, \Phi_{0}}$.

Claim 2.11. There is a positive constant $\delta=\delta\left(A_{0}, \Phi_{0}, k\right)$ with the following significance. If $\left(A_{i}, \Phi_{i}\right) \in \mathbf{B}_{A_{0}, \Phi_{0}}(\varepsilon)$ for $i=1,2$ and there is a gauge transformation $u \in B_{\mathrm{id}}(\delta)$ such that $u\left(A_{1}, \Phi_{1}\right)=\left(A_{2}, \Phi_{2}\right)$, then $u \in \operatorname{Stab}_{A_{0}, \Phi_{0}}$.

Proof. For small enough $\delta$, Claim 2.9 implies that $u \in B_{\text {id }}(\delta)$ can be written uniquely as $u=u_{1} \gamma$ with $u_{1} \in B_{\mathrm{id}}^{\perp}(\delta)$ and $\gamma \in \operatorname{Stab}_{A_{0}, \Phi_{0}}$. Thus, $\left(A_{2}, \Phi_{2}\right)=u_{1} \gamma\left(A_{1}, \Phi_{1}\right) \in$ $\mathbf{B}_{A_{0}, \Phi_{0}}(\varepsilon)$. But the neighborhood $\mathbf{B}_{A_{0}, \Phi_{0}}(\varepsilon)$ is $\operatorname{Stab}_{A_{0}, \Phi_{0}}$-invariant, so we also have $\gamma\left(A_{1}, \Phi_{1}\right) \in \mathbf{B}_{A_{0}, \Phi_{0}}(\varepsilon)$. Therefore $u_{1}=\mathrm{id}_{E}$ by the uniqueness assertion of Claim 2.9 and so $u=\gamma \in \operatorname{Stab}_{A_{0}, \Phi_{0}}$. This completes the proof of the claim. \(\square\)

Claim 2.11 shows that $\mathbf{B}_{A_{0}, \Phi_{0}}(\varepsilon) / \operatorname{Stab}_{A_{0}, \Phi_{0}}$ injects into the quotient $\mathcal{C}_{W, E}$ modulo the assumption that the gauge transformations are close to $\mathrm{id}_{E}$. It remains to show that if $\left(A_{i}, \Phi_{i}\right) \in \mathbf{B}_{A_{0}, \Phi_{0}}(\varepsilon)$ for $i=1,2$ and there is a gauge transformation $u \in{ }^{\circ} \mathcal{G}_{E}$
such that $u\left(A_{1}, \Phi_{1}\right)=\left(A_{2}, \Phi_{2}\right)$, then $u$ is necessarily close to $\mathrm{id}_{E}$ and hence that $\mathbf{B}_{A_{0}, \Phi_{0}}(\varepsilon) / \operatorname{Stab}_{A_{0}, \Phi_{0}}$ injects into the quotient $\mathcal{C}_{W, E}$.

Claim 2.12. For small enough $\varepsilon\left(A_{0}, \Phi_{0}\right)$, the projection $\pi: \mathbf{B}_{A_{0}, \Phi_{0}}(\varepsilon) / \operatorname{Stab}_{A_{0}, \Phi_{0}} \rightarrow$ $\mathcal{C}_{W, E}$ is injective.

Proof. Suppose $\left(A_{i}, \Phi_{i}\right) \in \mathbf{B}_{A_{0}, \Phi_{0}}(\varepsilon)$ for $i=1,2$ and that $\left[A_{1}, \Phi_{1}\right]=\left[A_{2}, \Phi_{2}\right] \in \mathcal{C}_{W, E}$, so that $u\left(A_{1}, \Phi_{1}\right)=\left(A_{2}, \Phi_{2}\right)$ for some $u \in{ }^{\circ} \mathcal{G}_{E}$.

Since $u\left(A_{0}\right)=A_{0}-\left(d_{A_{0}} u\right) u^{-1}$, we see that $u \in \operatorname{Stab}_{A_{0}, \Phi_{0}}$ if and only $d_{A_{0}, \Phi_{0}}^{0} u=$ $\left(d_{A_{0}} u,-u \Phi_{0}\right)=\left(0,-\Phi_{0}\right)$ or, equivalently, if and only if $d_{A_{0}, \Phi_{0}}^{0}\left(u-\mathrm{id}_{E}\right)=0$, since $\mathrm{id}_{E} \in \operatorname{Stab}_{A_{0}, \Phi_{0}}$. Here, we view $u \in L_{k+1}^{2}(\mathfrak{g l}(E))$ via the isometric embedding ${ }^{\circ} \mathcal{G}_{E} \subset$ $L_{k+1}^{2}(\mathfrak{g} \mathfrak{l}(E))$ and write
$$u-\mathrm{id}_{E}=u_{0}-\gamma,$$
where $u_{0} \in\left(\operatorname{Ker} d_{A_{0}, \Phi_{0}}^{0}\right)^{\perp}$ and $\gamma \in \operatorname{Ker} d_{A_{0}, \Phi_{0}}^{0}$. Our first task is to estimate $\| u-$ $\operatorname{id}_{E} \|_{L_{3, A_{0}}^{2}}$.

By assumption, $d_{A_{0}, \Phi_{0}}^{0} \gamma=\left(d_{A_{0}} \gamma, \gamma \Phi\right)=0$, so $d_{A_{0}} \gamma=0$ and $\gamma \Phi_{0}=0$. Since $u\left(A_{1}\right) \equiv A_{1}-\left(d_{A_{1}} u\right) u^{-1}=A_{2}$, we have $A_{2} u=A_{1} u-d_{A_{1}} u=A_{1} u-d_{A_{0}} u-\left[A_{1}-A_{0}, u\right]$, and therefore, using $d_{A_{0}} \mathrm{id}_{E}=0=d_{A_{0}} \gamma$, we have
$$d_{A_{0}} u_{0}=d_{A_{0}} u=u\left(A_{1}-A_{0}\right)-\left(A_{2}-A_{0}\right) u .$$
As $d_{A_{0}}^{*}\left(A_{i}-A_{0}\right)=\left(\cdot \Phi_{0}\right)^{*}\left(\Phi_{i}-\Phi_{0}\right)$, we obtain
$$\begin{aligned}
d_{A_{0}}^{*} d_{A_{0}} u_{0}=- & *\left(d_{A_{0}} u \wedge *\left(A_{1}-A_{0}\right)\right)+u d_{A_{0}}^{*}\left(A_{1}-A_{0}\right) \\
& -\left(d_{A_{0}}^{*}\left(A_{2}-A_{0}\right)\right) u+*\left(*\left(A_{2}-A_{0}\right) \wedge d_{A_{0}} u\right) \\
=- & *\left(d_{A_{0}} u_{0} \wedge *\left(A_{1}-A_{0}\right)\right)+u\left(\cdot \Phi_{0}\right)^{*}\left(\Phi_{1}-\Phi_{0}\right) \\
& -\left(\left(\Phi_{0}\right)^{*}\left(\Phi_{2}-\Phi_{0}\right)\right) u+*\left(*\left(A_{2}-A_{0}\right) \wedge d_{A_{0}} u_{0}\right) .
\end{aligned}$$
We define the Laplacian $\Delta_{A_{0}, \Phi_{0}}^{0}$ by setting
$$\Delta_{A_{0}, \Phi_{0}}^{0}=d_{A_{0}, \Phi_{0}}^{0, *} d_{A_{0}, \Phi_{0}}^{0}=d_{A_{0}}^{*} d_{A_{0}}+\left(\cdot \Phi_{0}\right)^{*} \Phi_{0} .$$
Now $u_{0}=u-\mathrm{id}_{E}+\gamma$ and $d_{A_{0}} \operatorname{id}_{E}=0=d_{A_{0}} \gamma$ and $\gamma \Phi_{0}=0$ so, using $u \Phi_{1}=\Phi_{2}$,
$$\begin{aligned}
\Delta_{A_{0}, \Phi_{0}}^{0} u_{0} & =\Delta_{A_{0}, \Phi_{0}}^{0}\left(u-\mathrm{id}_{E}+\gamma\right) \\
& =d_{A_{0}}^{*} d_{A_{0}}\left(u-\operatorname{id}_{E}+\gamma\right)+\left(\cdot \Phi_{0}\right)^{*}\left(u-\operatorname{id}_{E}\right) \Phi_{0} \\
& =d_{A_{0}}^{*} d_{A_{0}} u+\left(\cdot \Phi_{0}\right)^{*}\left(u \Phi_{0}-u \Phi_{1}+u \Phi_{1}-\Phi_{0}\right) \\
& =d_{A_{0}}^{*} d_{A_{0}} u_{0}+\left(\cdot \Phi_{0}\right)^{*}\left(u\left(\Phi_{0}-\Phi_{1}\right)+\left(\Phi_{2}-\Phi_{0}\right)\right) .
\end{aligned}$$
Our assumption that $\left(A_{i}, \Phi_{i}\right) \in \mathbf{B}_{A_{0}, \Phi_{0}}(\varepsilon)$ and the embeddings $L_{k}^{2} \subset L_{2}^{2}$ imply that for $i=1,2$ we have
$$\left\|\left(A_{i}, \Phi_{i}\right)-\left(A_{0}, \Phi_{0}\right)\right\|_{L_{2, A_{0}}^{2}} \leq\left\|\left(A_{i}, \Phi_{i}\right)-\left(A_{0}, \Phi_{0}\right)\right\|_{L_{k, A_{0}}^{2}}<\varepsilon,$$
Since $u_{0} \in\left(\operatorname{Ker} d_{A_{0}, \Phi_{0}}^{0}\right)^{\perp}$, the standard elliptic estimate for the Laplacian $\Delta_{A_{0}, \Phi_{0}}^{0}$, the fact that $|u|=1$ as $u \in{ }^{\circ} \mathcal{G}_{E}$, the Sobolev embedding $L_{2}^{2} \subset L^{q}, 2 \leq q<\infty$, and
multiplication $L_{2}^{2} \times L_{2}^{2} \rightarrow L_{1}^{2}$, and our expression for $d_{A_{0}}^{*} d_{A_{0}} u=d_{A_{0}}^{*} d_{A_{0}} u_{0}$ combine to give
$$\begin{aligned}
\left\|u_{0}\right\|_{L_{3, A_{0}}^{2}} \leq & C\left\|\Delta_{A_{0}, \Phi_{0}}^{0} u_{0}\right\|_{L_{1, A_{0}}^{2}} \\
\leq & C\left\|d_{A_{0}}^{*} d_{A_{0}} u_{0}\right\|_{L_{1, A_{0}}^{2}}+C\left\|\left(\cdot \Phi_{0}\right)^{*}\left(u\left(\Phi_{0}-\Phi_{1}\right)+\left(\Phi_{2}-\Phi_{0}\right)\right)\right\|_{L_{1, A_{0}}^{2}} \\
\leq & C\left\|d_{A_{0}} u_{0}\right\|_{L_{2, A_{0}}^{2}}\left(\left\|A_{1}-A_{0}\right\|_{L_{2, A_{0}}^{2}}+\left\|A_{2}-A_{0}\right\|_{L_{2, A_{0}}^{2}}\right) \\
& +C\|u\|_{L_{2, A_{0}}^{2}}\left\|\Phi_{0}\right\|_{L_{2, A_{0}}^{2}}\left(\left\|\Phi_{1}-\Phi_{0}\right\|_{L_{2, A_{0}}^{2}}+\left\|\Phi_{2}-\Phi_{0}\right\|_{L_{2, A_{0}}^{2}}\right) \\
\leq & C\left\|u_{0}\right\|_{L_{3, A_{0}}^{2}} \varepsilon+C\|u\|_{L_{2, A_{0}}^{2}}\left\|\Phi_{0}\right\|_{L_{2, A_{0}}^{2}} \varepsilon \\
\leq & C\left\|u_{0}\right\|_{L_{3, A_{0}}^{2}} \varepsilon+C\left\|\Phi_{0}\right\|_{L_{2, A_{0}}^{2}} \varepsilon,
\end{aligned}$$
for some constant $C=C\left(A_{0}, \Phi_{0}\right)$. For small enough $\varepsilon$ we can rearrange the preceding inequality and use the Sobolev embedding $L_{3}^{2} \subset C^{0}$ to give
$$\left\|u_{0}\right\|_{L_{3, A_{0}}^{2}} \leq C\left\|\Phi_{0}\right\|_{L_{2, A_{0}}^{2}} \varepsilon \quad \text { and } \quad\left\|u_{0}\right\|_{C^{0}} \leq C\left\|\Phi_{0}\right\|_{L_{2, A_{0}}^{2}} \varepsilon .$$
Therefore, as $|u|=1$, we have the pointwise bounds
$$1-\left|u_{0}\right| \leq\left|\operatorname{id}_{E}-\gamma\right| \leq 1+\left|u_{0}\right|,$$
and thus, for $\varepsilon$ small, $\left|\operatorname{id}_{E}-\gamma\right|>0$; the pointwise norm of $z=\left|\operatorname{id}_{E}-\gamma\right|$ is constant since $d_{A_{0}}\left(\operatorname{id}_{E}-\gamma\right)=0$. Consequently, $\gamma_{0} \equiv z^{-1}\left(\operatorname{id}_{E}-\gamma\right)$ lies in ${ }^{\circ} \mathcal{G}_{E}$ : clearly, $d_{A_{0}} \gamma_{0}=0$, so $\gamma_{0} \in \operatorname{Stab}_{A}$. If $\Phi_{0} \equiv 0$, we trivially have $\gamma_{0} \in \operatorname{Stab}_{\Phi_{0}}$; if $\Phi_{0} \not \equiv 0$, then the equalities $\left|\gamma_{0} \Phi_{0}\right|=\left|\Phi_{0}\right|$ (as $\gamma_{0}$ is a unitary gauge transformation) and $\gamma_{0} \Phi_{0}=z^{-1}\left(\mathrm{id}_{E}-\gamma\right) \Phi_{0}=$ $z^{-1} \Phi_{0}$, so $\left|\gamma_{0} \Phi_{0}\right|=z^{-1}\left|\Phi_{0}\right|$, imply that $z=1$ (it is enough to have equality of $L^{2}$ norms here as $z$ is constant). Hence, we also have $\gamma_{0} \in \operatorname{Stab}_{\Phi_{0}}$ and in particular, $\gamma_{0} \in \operatorname{Stab}_{A_{0}, \Phi_{0}}=\operatorname{Stab}_{A_{0}} \cap \operatorname{Stab}_{\Phi_{0}}$.

We now write $\gamma_{0}^{-1} u=\gamma_{0}^{-1} u_{0}+\gamma_{0}^{-1}\left(\mathrm{id}_{E}-\gamma\right)=\gamma_{0}^{-1} u_{0}+z \mathrm{id}_{E}$, so that
$$\gamma_{0}^{-1} u-\mathrm{id}_{E}=(z-1) \operatorname{id}_{E}+\gamma_{0}^{-1} u_{0} .$$
Clearly, $(z-1) \operatorname{id}_{E} \in \operatorname{Ker} d_{A_{0}, \Phi_{0}}^{0}$ by the remarks of the last paragraph, while $\gamma_{0}^{-1} u_{0} \in$ (Ker $\left.d_{A_{0}, \Phi_{0}}^{0}\right)^{\perp}$ since $u_{0} \in\left(\operatorname{Ker} d_{A_{0}, \Phi_{0}}^{0}\right)^{\perp}$ and $\gamma_{0}^{-1} \in \operatorname{Stab}{ }_{A_{0}, \Phi_{0}}$. Similarly, $\gamma_{0}^{-1} u\left(A_{1}, \Phi_{1}\right)=$ $\gamma_{0}^{-1}\left(A_{2}, \Phi_{2}\right) \in \mathbf{B}_{A_{0}, \Phi_{0}}(\varepsilon)$, as the neighborhood $\mathbf{B}_{A_{0}, \Phi_{0}}(\varepsilon)$ is $\operatorname{Stab}_{A_{0}, \Phi_{0}}$-invariant. Thus, replacing $u$ by $\gamma_{0}^{-1} u$ and $\left(A_{2}, \Phi_{2}\right)$ by $\left(\tilde{A}_{2}, \tilde{\Phi}_{2}\right) \equiv \gamma_{0}^{-1}\left(A_{2}, \Phi_{2}\right)$ in our $L_{3, A_{0}}^{2}$ estimate for $u_{0}$ yields
$$\left\|\gamma_{0}^{-1} u_{0}\right\|_{L_{3, A_{0}}^{2}} \leq C\left\|\Phi_{0}\right\|_{L_{2, A_{0}}^{2}} \varepsilon,$$
while $|z-1| \leq\left\|u_{0}\right\|_{C^{0}} \leq C\left\|\Phi_{0}\right\|_{L_{2, A_{0}}^{2}} \varepsilon$, so we find that
$$\left\|\gamma_{0}^{-1} u-\operatorname{id}_{E}\right\|_{L_{3, A_{0}}^{2}} \leq C\left\|\Phi_{0}\right\|_{L_{2, A_{0}}^{2}} \varepsilon .$$
If $\varepsilon$ is small enough that $C\left\|\Phi_{0}\right\|_{L_{2, A_{0}}^{2}} \varepsilon<\delta$, where $\delta=\delta\left(A_{0}, \Phi_{0}\right)$ is the constant of Claim 2.11 with $k=2$, then $\gamma_{0}^{-1} u \in \operatorname{Stab}_{A_{0}, \Phi_{0}}$ and so $u$ lies in $\operatorname{Stab}_{A_{0}, \Phi_{0}}$, as desired. \(\square\)

Claim 2.13. The quotient space $\mathcal{C}_{W, E}$ is Hausdorff.

Proof. Let $\Gamma$ be the subspace $\left\{\{(A, \Phi), u(A, \Phi)\}:(A, \Phi) \in \tilde{\mathcal{C}}_{W, E}\right.$ and $\left.u \in{ }^{\circ} \mathcal{G}_{E}\right\}$ of $\tilde{\mathcal{C}}_{W, E} \times \tilde{\mathcal{C}}_{W, E}$. If $\left\{\left(A_{\alpha}, \Phi_{\alpha}\right), u_{\alpha}\left(A_{\alpha}, \Phi_{\alpha}\right)\right\}$ is a sequence in $\Gamma$ which converges in $L_{k}^{2}$ to a point $\left\{\left(A_{\infty}, \Phi_{\infty}\right),\left(B_{\infty}, \Psi_{\infty}\right)\right\}$, then Lemma 2.7 implies that there is a subsequence $\left\{\alpha^{\prime}\right\} \subset\{\alpha\}$ such that $\left\{u_{\alpha}\right\}$ converges in $L_{k+1}^{2}$ to $u_{\infty} \in{ }^{\circ} \mathcal{G}_{E}$ and $u_{\infty}\left(A_{\infty}\right)=B_{\infty}$. But then $u_{\alpha^{\prime}} \Phi_{\alpha^{\prime}}$ converges in $L_{k}^{2}$ to $u_{\infty} \Phi_{\infty}$ and so $\Psi_{\infty}=u_{\infty} \Phi_{\infty}$. Thus, $\left(B_{\infty}, \Psi_{\infty}\right)=$ $u_{\infty}\left(A_{\infty}, \Phi_{\infty}\right)$ for some $u_{\infty} \in{ }^{\circ} \mathcal{G}_{E}$, so $\Gamma$ is closed and the quotient $\tilde{\mathcal{C}}_{W, E} /{ }^{\circ} \mathcal{G}_{E}$ is Hausdorff. \(\square\)

Claim 2.13 gives Assertion (1) of the proposition and Assertions (2), (3), and (4) now follow from the preceding arguments and Claim 2.12. This completes the proof of the proposition. \(\square\)

Remark 2.14. (1) Alternatively, one can show that the quotient $L_{k}^{2}$ topology on $\mathcal{C}_{W, E}$ is metrizable via the $L^{2}$ metric (exactly as in [20, Lemma 4.2.4]) and thus $\mathcal{C}_{W, E}$ is Hausdorff.
(2) As Mrowka pointed out to us, one can sharpen the assertions of Proposition 2.8, at least for the quotient space $\mathcal{B}_{E}$ : one finds that charts are provided by $L^{4}$-balls in $\operatorname{Ker} d_{A_{0}}^{*}$ rather than the much smaller $L_{k, A_{0}}^{2}$-balls usually employed; see [22].

It is convenient to extract the following global, Coulomb gauge-fixing result (analogous to Proposition 2.3.4 in [20]) which we established in the course of proving Proposition 2.8:

Lemma 2.15. Let $X$ be a closed, oriented, Riemannian spin ${ }^{c}$ four-manifold and let $E$ be a Hermitian vector bundle over $X$. Suppose that $k \geq 2$ is an integer and that $\left(A_{0}, \Phi_{0}\right) \in \tilde{\mathcal{C}}_{W, E}$. Then there is a positive constant $\varepsilon=\varepsilon\left(A_{0}, \Phi_{0}, k\right)$ such that for any $(A, \Phi) \in \tilde{\mathcal{C}}_{W, E}$ with
$$\left\|(A, \Phi)-\left(A_{0}, \Phi_{0}\right)\right\|_{L_{k, A_{0}}^{2}(X)}<\varepsilon,$$
there is a gauge transformation $u \in{ }^{\circ} \mathcal{G}_{E}$, unique up to an element of $\operatorname{Stab}_{A_{0}, \Phi_{0}}$, such that
$$d_{A_{0}, \Phi_{0}}^{0, *}\left(u(A, \Phi)-\left(A_{0}, \Phi_{0}\right)\right)=0 .$$

\subsection*{2.3. Connections on $\boldsymbol{\operatorname { S O }}(\mathbf{3})$ bundles and groups of gauge transformations.}

For some local patching arguments over simply-connected open regions $Y \subset X$ in §3 and §4 it is very useful to be able to lift gauge transformations in $\mathcal{G}_{\mathfrak{s} \mathfrak{u}(E)}(Y)$ to gauge transformations in $\mathcal{G}_{E}(Y)$. The following result tells us that this is always possible when $Y$ is simply connected; it is an extension of Theorem IV.3.1 in [61] from SU(2) to U(2) bundles.

Proposition 2.16. Let $E$ be a Hermitian two-plane bundle over a connected manifold $X$. Then there is an exact sequence
$$1 \rightarrow\left\{ \pm \operatorname{id}_{E}\right\} \rightarrow \mathcal{G}_{E} \rightarrow \mathcal{G}_{\mathfrak{s u}(E)} \rightarrow H^{1}(X ; \mathbb{Z} / 2 \mathbb{Z}) .$$

Proof. Let $P$ be the U(2) principal bundle underlying $E$ so $P^{\mathrm{ad}}=P / S_{Z}^{1}$ is the SO(3) principal bundle underlying $\mathfrak{s u}(E)$. We can view elements of $\mathcal{G}_{E}$ as maps $u: P \rightarrow$ SU(2) satisfying $u(p g)=g^{-1} u(p) g$ for $p \in P$ and $g \in \mathrm{U}(2)$, and similarly for elements of $\mathcal{G}_{\mathfrak{s u}(E)}$. The map $\mathcal{G}_{E} \rightarrow \mathcal{G}_{\mathfrak{s u}(E)}$ is then given by $u \rightarrow \operatorname{Ad} u$. Because $X$ is connected, the kernel of this map is $\left\{ \pm \mathrm{id}_{E}\right\}$, giving the exactness of all but the last terms in the sequence.

Let $\nu_{2} \in H^{1}(\operatorname{SO}(3) ; \mathbb{Z} / 2 \mathbb{Z})$ be the non-trivial cohomology class given by the double cover $\mathrm{SU}(2) \rightarrow \mathrm{SO}(3)$. Thus a map $u: V \rightarrow \mathrm{SO}(3)$ lifts to SU(2) if and only if $u^{*} \nu_{2}=0$. We would like to define the map $\alpha: \mathcal{G}_{\mathfrak{s u}(E)} \rightarrow H^{1}(X ; \mathbb{Z} / 2 \mathbb{Z})$ by $\alpha(u)=u^{*} \nu_{2}$. It is not immediately clear that $\alpha(u)$ actually lies in $H^{1}(X ; \mathbb{Z} / 2 \mathbb{Z})$. The homotopy exact sequence
$$\pi_{1}(\mathrm{SO}(3)) \rightarrow \pi_{1}\left(P^{\mathrm{ad}}\right) \rightarrow \pi_{1}(X) \rightarrow 1$$
gives an exact sequence in cohomology $H^{1}(\cdot ; \mathbb{Z} / 2 \mathbb{Z})=\operatorname{Hom}\left(\pi_{1}(\cdot), \mathbb{Z} / 2 \mathbb{Z}\right)$,
$$1 \rightarrow H^{1}(X ; \mathbb{Z} / 2 \mathbb{Z}) \rightarrow H^{1}\left(P^{\mathrm{ad}} ; \mathbb{Z} / 2 \mathbb{Z}\right) \rightarrow H^{1}(\operatorname{SO}(3) ; \mathbb{Z} / 2 \mathbb{Z}) .$$
Thus $u^{*} \nu_{2}$ is pulled back from a unique element of $H^{1}(X ; \mathbb{Z} / 2 \mathbb{Z})$ if and only if $i_{x}^{*} u^{*} \nu_{2}=$ 0 , where $i_{x}: \mathrm{SO}(3) \rightarrow P^{\text {ad }}$ is the inclusion of a fiber.

Because $u^{*} \nu_{2}$ depends only on the homotopy class of $u$, the map $\alpha$ is constant on connected components. Let $\mathcal{G}_{\mathfrak{s u}(E)}^{x}$ be the subgroup of elements of $\mathcal{G}_{\mathfrak{s u}(E)}$ which are the identity over $x \in X$. The exact sequence of groups
$$1 \rightarrow \mathcal{G}_{\mathfrak{s} \mathfrak{u}(E)}^{x} \rightarrow \mathcal{G}_{\mathfrak{s} \mathfrak{u}(E)} \rightarrow \operatorname{SO}(3) \rightarrow 1$$
and the corresponding exact sequence of homotopy groups ( $\pi_{0}$ to be specific) shows that the inclusion $\mathcal{G}_{\mathfrak{s} \mathfrak{u}(E)}^{x}$ induces a surjection of connected components. Now if $u \in$ $\mathcal{G}_{\mathfrak{s} \mathfrak{u}(E)}^{x}$ then $i_{x}^{*} u^{*} \nu_{2}=0$, and so $i_{x} u^{*} \nu_{2}=0$ for all $u \in \mathcal{G}_{\mathfrak{s} \mathfrak{u}(E)}$. This implies that the map $\alpha$ takes values in $H^{1}(X ; \mathbb{Z} / 2 \mathbb{Z})$.

By the defining property of $\nu_{2}$, we have $\alpha(u)=0$ if and only if there is a lift of $u$ to $\mathrm{SU}(2)$. Because $\left\{ \pm \mathrm{id}_{E}\right\}$ is central, any Ad-equivariant map $\tilde{u}: P \rightarrow \operatorname{SU}(2)$ descends to $P^{\text {ad }} \rightarrow \operatorname{SU}(2)$. Thus $u \in \mathcal{G}_{\mathfrak{s u}(E)}$ is induced by some $\tilde{u} \in \mathcal{G}_{E}$ if and only if $\alpha(u)=0$. \(\square\)

Remark 2.17. It can also be shown that the map $\mathcal{G}_{\mathfrak{s u}(E)} \rightarrow H^{1}(X ; \mathbb{Z} / 2 \mathbb{Z})$ is surjective. We omit the proof here in the interests of brevity.
2.4. Quadratic forms for coupled spinor bundles. Give $\mathfrak{g l}(E)$ (respectively, $\left.\mathfrak{g} \mathfrak{l}\left(W^{ \pm}\right)\right)$the Hermitian fiber inner product and norm
$$\langle M, N\rangle:=\frac{1}{2} \operatorname{tr}\left(M^{\dagger} N\right) \quad \text { and } \quad|M|^{2}=\langle M, M\rangle,$$
for $M, N \in \Omega^{0}(\mathfrak{g l}(E))$ (respectively, $\mathfrak{g l}\left(W^{ \pm}\right)$), so that $\left|\operatorname{id}_{E}\right|=1$, etc. If $\Phi \in \Omega^{0}\left(W^{+} \otimes\right.$ $E$ ), then $\Phi^{*} \in \Omega^{0}\left(\left(W^{+} \otimes E\right)^{*}\right)=\Omega^{0}\left(\left(W^{+}\right)^{*} \otimes E^{*}\right)$ is defined by $\Phi^{*}(\Psi):=\langle\Psi, \Phi\rangle$ for $\Psi \in \Omega^{0}\left(W^{+} \otimes E\right)$.

With respect to the induced Hermitian fiber inner products on $\mathfrak{g l}\left(W^{+}\right)$and $\mathfrak{g l}(E)$, we have fiber-wise orthogonal direct sums, $\mathfrak{g l}\left(W^{+}\right)=\mathbb{C i d}_{W^{+}} \oplus \mathfrak{s l}\left(W^{+}\right)$, and similarly
for $\mathfrak{g} \mathfrak{l}(E)$ and thus $\mathfrak{g} \mathfrak{l}\left(W^{+}\right) \otimes_{\mathbb{C}} \mathfrak{g} \mathfrak{l}(E)$. Let $\pi_{W^{+}}$(respectively, $\pi_{E}$ ) be the fiber-wise orthogonal projection from $\mathfrak{g} \mathfrak{l}\left(W^{+}\right)$(respectively, $\left.\mathfrak{g} \mathfrak{l}(E)\right)$ onto the subspace $\mathfrak{s} \mathfrak{l}\left(W^{+}\right)$ (respectively, $\mathfrak{s l}(E)$ ), so that
$$\pi_{W^{+}} M:=M-\frac{1}{2} \operatorname{tr} M \mathrm{id}_{W^{+}} \quad \text { and } \quad \pi_{E} N:=N-\frac{1}{2} \operatorname{tr} N \operatorname{id}_{E}$$
are the projection onto the traceless components of $M \in \mathfrak{g l}\left(W^{+}\right)$and $N \in \mathfrak{g l}(E)$, and
$$\pi_{W^{+}}^{\perp} M:=\frac{1}{2} \operatorname{tr} M \mathrm{id}_{W^{+}} \quad \text { and } \quad \pi_{E}^{\perp} N:=\frac{1}{2} \operatorname{tr} N \operatorname{id}_{E}$$
are the projections onto the trace components of $M \in \mathfrak{g l}\left(W^{+}\right)$and $N \in \mathfrak{g l}(E)$. The orthogonal projection from $\mathfrak{g} \mathfrak{l}\left(W^{+}\right) \otimes_{\mathbb{C}} \mathfrak{g} \mathfrak{l}(E)$ onto $\mathfrak{s} \mathfrak{l}\left(W^{+}\right) \otimes_{\mathbb{C}} \mathfrak{s} \mathfrak{l}(E)$ is obtained by writing $\pi_{W^{+}}=\mathrm{id}_{W^{+}}-\pi_{W^{+}}^{\perp}$ and $\pi_{E}=\mathrm{id}_{E}-\pi_{E}^{\perp}$, so that
$$\pi_{W^{+}} \otimes \pi_{E}=\mathrm{id}_{W^{+}} \otimes \mathrm{id}_{E}-\left(\pi_{W^{+}} \otimes \pi_{E}^{\perp}+\pi_{W^{+}}^{\perp} \otimes \pi_{E}\right)+\pi_{W^{+}}^{\perp} \otimes \pi_{E}^{\perp} .$$
Consequently, if $\phi \in \Omega^{0}\left(W^{+}\right)$and $\Phi \in \Omega^{0}\left(W^{+} \otimes E\right)$, we may define
$$\begin{aligned}
\left(\phi \otimes \phi^{*}\right)_{0} & :=\pi_{W^{+}}\left(\phi \otimes \phi^{*}\right) \\
\left(\Phi \otimes \Phi^{*}\right)_{00} & :=\left(\pi_{W^{+}} \otimes \pi_{E}\right)\left(\Phi \otimes \Phi^{*}\right) .
\end{aligned}$$
Note that
$$\mathfrak{g} \mathfrak{l}\left(W^{+}\right) \otimes_{\mathbb{C}} \mathfrak{g} \mathfrak{l}(E)=\mathfrak{u}\left(W^{+}\right) \otimes_{\mathbb{R}} \mathfrak{u}(E)+i \mathfrak{u}\left(W^{+}\right) \otimes_{\mathbb{R}} \mathfrak{u}(E) .$$
Plainly, $\left(\phi \otimes \phi^{*}\right)_{0}$ is a section of $\mathfrak{s l}\left(W^{+}\right) \cap i \mathfrak{u}\left(W^{+}\right)=i \mathfrak{s} \mathfrak{u}\left(W^{+}\right)$. The following identities are now well-known [47], [77, Chapter 8]:

Lemma 2.18. For every $\phi \in \Omega^{0}\left(W^{+}\right)$or $\Omega^{0}(E), T \in \Omega^{0}\left(\mathfrak{s} \mathfrak{l}\left(W^{+}\right)\right)$, and $\eta \in \Omega^{2}(X, \mathbb{C})$, the following hold. The endomorphism $\left(\phi \otimes \phi^{*}\right)_{0}$ is a section of $\Omega^{0}\left(i \mathfrak{s u}\left(W^{+}\right)\right)$and satisfies:
$$\begin{aligned}
\left|\left(\phi \otimes \phi^{*}\right)_{0}\right|^{2} & =\frac{1}{4}|\phi|^{4}, \\
|\rho(\eta)|^{2} & =2\left|\eta^{+}\right|^{2} \quad \text { and } \quad\left|\rho^{-1} T\right|^{2}=\frac{1}{2}|T|^{2} .
\end{aligned}$$

Similarly, $\Phi \otimes \Phi^{*}$ is a section of $i \mathfrak{u}\left(W^{+} \otimes_{\mathbb{C}} E\right)=\mathfrak{u}\left(W^{+}\right) \otimes_{\mathbb{R}} \mathfrak{u}(E)$ and $\left(\Phi \otimes \Phi^{*}\right)_{00}$ is a section of $\mathfrak{s} \mathfrak{u}\left(W^{+}\right) \otimes_{\mathbb{R}} \mathfrak{s} \mathfrak{u}(E)$. We then have the following analogue of Lemma 2.18:

Lemma 2.19. For every $\Phi \in \Omega^{0}\left(W^{+} \otimes E\right)$ and $M \in \Omega^{0}\left(\mathfrak{g l}\left(W^{+} \otimes E\right)\right)$, the following identities hold:
$$\begin{aligned}
\left\langle\Phi \otimes \Phi^{*}, M\right\rangle & =\frac{1}{2}\langle M \Phi, \Phi\rangle, \\
\left(\frac{5}{4}-\frac{1}{\sqrt{2}}\right)|\Phi|^{4} & \leq\left\langle\left(\Phi \otimes \Phi^{*}\right)_{00} \Phi, \Phi\right\rangle \leq \frac{1}{\sqrt{2}}|\Phi|^{4}, \\
\left(\frac{5}{8}-\frac{1}{2 \sqrt{2}}\right)|\Phi|^{4} & \leq\left|\left(\Phi \otimes \Phi^{*}\right)_{00}\right|^{2} \leq \frac{1}{2 \sqrt{2}}|\Phi|^{4} .
\end{aligned}$$

Proof. Using $\Phi=c^{a} \Phi^{a}$, so $M \Phi=c^{a} M \Phi^{a}$ and $\Phi^{*} \Phi^{a}=\left\langle\Phi^{a}, \Phi\right\rangle=\bar{c}^{a}$, we have
$$\begin{aligned}
\left\langle\Phi \otimes \Phi^{*}, M\right\rangle & =\frac{1}{2} \operatorname{tr}\left(\left(\Phi \otimes \Phi^{*}\right)^{\dagger} M\right)=\frac{1}{2}\left\langle\left(\Phi \otimes \Phi^{*}\right) M \Phi^{a}, \Phi^{a}\right\rangle \\
& =\frac{1}{2}\left\langle M \Phi^{a},\left(\Phi \otimes \Phi^{*}\right) \Phi^{a}\right\rangle=\frac{1}{2}\left\langle M \Phi^{a}, \Phi\left(\Phi^{*} \Phi^{a}\right)\right\rangle \\
& =\frac{1}{2}\left\langle M \Phi^{a}, \bar{c}^{a} \Phi\right\rangle=\frac{1}{2}\left\langle c^{a} M \Phi^{a}, \Phi\right\rangle=\frac{1}{2}\langle M \Phi, \Phi\rangle,
\end{aligned}$$
which gives (1). Next, we see that
$$\left|\Phi \otimes \Phi^{*}\right|^{2}=\left\langle\Phi \otimes \Phi^{*}, \Phi \otimes \Phi^{*}\right\rangle=\frac{1}{2}\left\langle\left(\Phi \otimes \Phi^{*}\right) \Phi, \Phi\right\rangle=\frac{1}{2}|\Phi|^{2}\langle\Phi, \Phi\rangle=\frac{1}{2}|\Phi|^{4},$$
and so the upper bound in (2) is obtained by
$$\left|\left\langle\left(\Phi \otimes \Phi^{*}\right)_{00} \Phi, \Phi\right\rangle\right| \leq\left|\left(\Phi \otimes \Phi^{*}\right)_{00}\right||\Phi|^{2} \leq\left|\Phi \otimes \Phi^{*}\right||\Phi|^{2} \leq(1 / \sqrt{2})|\Phi|^{4}<\frac{3}{4}|\Phi|^{4},$$
where we use the fact that $(\cdot)_{00}=\pi_{W^{+}} \otimes \pi_{E}$ is an orthogonal projection to obtain the second inequality.

To obtain the lower bound in (2), suppose that $\Phi=\phi^{a} \otimes \xi^{a}$ (implied summation), where $\left\{\phi^{a}\right\} \subset \Omega^{0}\left(W^{+}\right)$and $\left\{\xi^{a}\right\} \subset \Omega^{0}(E)$, then $\Phi \otimes \Phi^{*}=\left(\phi^{a} \otimes \phi^{b, *}\right) \otimes\left(\xi^{a} \otimes \xi^{b, *}\right)$ and
$$\begin{aligned}
\left(\pi_{W^{+}}^{\perp} \otimes \pi_{E}^{\perp}\right)\left(\Phi \otimes \Phi^{*}\right) & =\pi_{W^{+}}^{\perp}\left(\phi^{a} \otimes \phi^{b, *}\right) \otimes \pi_{E}^{\perp}\left(\xi^{a} \otimes \xi^{b, *}\right) \\
& =\frac{1}{4} \operatorname{tr}\left(\phi^{a} \otimes \phi^{b, *}\right) \operatorname{tr}\left(\xi^{a} \otimes \xi^{b, *}\right) \operatorname{id}_{W^{+} \otimes E} \\
& =\frac{1}{4}\left\langle\phi^{a}, \phi^{b}\right\rangle\left\langle\xi^{a}, \xi^{b}\right\rangle \operatorname{id}_{W^{+} \otimes E} \\
& =\frac{1}{4}\left\langle\phi^{a} \otimes \xi^{a}, \phi^{b} \otimes \xi^{b}\right\rangle \operatorname{id}_{W^{+} \otimes E}=\frac{1}{4}\langle\Phi, \Phi\rangle \operatorname{id}_{W^{+} \otimes E} .
\end{aligned}$$
Using the last identity together with $\left(\Phi \otimes \Phi^{*}\right) \Phi=\Phi\langle\Phi, \Phi\rangle=\Phi|\Phi|^{2}$ and (2.11) gives
$$\begin{aligned}
\left\langle\left(\Phi \otimes \Phi^{*}\right)_{00} \Phi, \Phi\right\rangle= & \left\langle\left(\Phi \otimes \Phi^{*}\right) \Phi, \Phi\right\rangle-\left\langle\left(\pi_{W^{+}}^{\perp} \otimes \pi_{E}+\pi_{W^{+}} \otimes \pi_{E}^{\perp}\right)\left(\Phi \otimes \Phi^{*}\right) \Phi, \Phi\right\rangle \\
& \left.+\left.\left\langle\frac{1}{4}\right| \Phi\right|^{2} \Phi, \Phi\right\rangle \\
= & \frac{5}{4}|\Phi|^{4}-\left\langle\left(\pi_{W^{+}}^{\perp} \otimes \pi_{E}+\pi_{W^{+}} \otimes \pi_{E}^{\perp}\right)\left(\Phi \otimes \Phi^{*}\right) \Phi, \Phi\right\rangle .
\end{aligned}$$
But $\pi_{W^{+}}^{\perp} \otimes \pi_{E}+\pi_{W^{+}} \otimes \pi_{E}^{\perp}$ is just the orthogonal projection onto to the middle two factors of the orthogonal decomposition of $\mathfrak{g l}\left(W^{+}\right) \otimes_{\mathbb{C}} \mathfrak{g} \mathfrak{l}(E)$, so
$$\begin{aligned}
& \left|\left\langle\left(\pi_{W^{+}}^{\perp} \otimes \pi_{E}+\pi_{W^{+}} \otimes \pi_{E}^{\perp}\right)\left(\Phi \otimes \Phi^{*}\right) \Phi, \Phi\right\rangle\right| \\
& \quad \leq\left|\left(\pi_{W^{+}}^{\perp} \otimes \pi_{E}+\pi_{W^{+}} \otimes \pi_{E}^{\perp}\right)\left(\Phi \otimes \Phi^{*}\right)\right||\Phi|^{2} \\
& \quad \leq\left|\Phi \otimes \Phi^{*}\right||\Phi|^{2} \leq(1 / \sqrt{2})|\Phi|^{4}<\frac{3}{4}|\Phi|^{4},
\end{aligned}$$
and therefore
$$\left|\left\langle\left(\Phi \otimes \Phi^{*}\right)_{00} \Phi, \Phi\right\rangle\right| \geq \frac{5}{4}|\Phi|^{4}-(1 / \sqrt{2})|\Phi|^{4}>\frac{1}{2}|\Phi|^{4} .$$
Consequently, using $\left(\Phi \otimes \Phi^{*}\right)_{00}^{\dagger}=\left(\Phi \otimes \Phi^{*}\right)_{00}$, we have
$$\begin{aligned}
\frac{1}{2}\left\langle\left(\Phi \otimes \Phi^{*}\right)_{00} \Phi, \Phi\right\rangle & =\left\langle\left(\Phi \otimes \Phi^{*}\right)_{00}, \Phi \otimes \Phi^{*}\right\rangle=\left\langle\left(\Phi \otimes \Phi^{*}\right)_{00},\left(\Phi \otimes \Phi^{*}\right)_{00}\right\rangle \\
& =\left|\left(\Phi \otimes \Phi^{*}\right)_{00}\right|^{2},
\end{aligned}$$
which gives (3). \(\square\)

The fact that $\left|\left(\Phi \otimes \Phi^{*}\right)_{0}\right|^{2} \geq \frac{1}{4}|\Phi|^{4}$, for $\Phi \in \Omega^{0}\left(W^{+} \otimes E\right)$, is used in §4 to show that the moduli space of PU(2) monopoles has an Uhlenbeck compactification. (The analogous equality, $\left|\left(\phi \otimes \phi^{*}\right)_{0}\right|^{2}=\frac{1}{4}|\phi|^{4}$ for $\phi \in \Omega^{0}\left(W^{+}\right)$, is used in [47, 98] to show that the moduli space of Seiberg-Witten monopoles is compact.)

We adapt some terminology from the proofs of Proposition 3.4 in [30] and Lemma 4.3.25 in [20] which we will need for our proof of transversality for the PU(2) monopole moduli space in §5:
Definition 2.20. The rank of a section $\Phi \in \Omega^{0}\left(W^{ \pm} \otimes E\right)$ at a point $x \in X$ is the rank of $\left.\Phi\right|_{x}$ considered as a complex linear map $\left.\left.\left(W^{ \pm}\right)^{*}\right|_{x} \rightarrow E\right|_{x}$ (that is, its rank as a complex two-by-two matrix). We say that $\Phi$ is rank one on a subset $U \subset X$ if it has rank less than or equal to one at all points in $U$. Similarly, for $v \in \Omega^{0}\left(\Lambda^{+}\left(T^{*} X\right) \otimes \mathfrak{s u}(E)\right)$, the rank of $v$ at a point $x \in X$ is the rank of $v$ considered as a real linear map from $\left.\left.\Lambda^{+}(T X)\right|_{x} \rightarrow \mathfrak{s u}(E)\right|_{x}$ (that is, its rank as a real three-by-three matrix). The rank of $v$ on a set $U \subset X$ is the maximum rank of $\left.v\right|_{x}$ over all points $x \in U$. Finally, for $M \in \Omega^{0}\left(\mathfrak{s u}\left(W^{+}\right) \otimes \mathfrak{s u}(E)\right)$, the rank of $M$ at a point $x \in X$ is the rank of $M$ considered as a real linear map from $\left.\left.\mathfrak{s} \mathfrak{u}\left(W^{+}\right)^{*}\right|_{x} \rightarrow \mathfrak{s} \mathfrak{u}(E)\right|_{x}$ (again, its rank as a real three-by-three matrix). The rank of $M$ on a set $U \subset X$ is the maximum rank of $\left.M\right|_{x}$ over all points $x \in U$.

For the proof of Lemma 2.21 below we shall need a simple linear algebra identity. Suppose that $\Phi=\phi \otimes \xi$, for some $\phi \in \Omega^{0}\left(W^{+}\right)$and $\xi \in \Omega^{0}(E)$, and that that $\Psi=\psi \otimes \zeta$, with $\phi \in \Omega^{0}\left(W^{+}\right)$and $\xi \in \Omega^{0}(E)$. Then
$$\Phi \otimes \Psi^{*}=(\phi \otimes \xi) \otimes(\psi \otimes \zeta)^{*}=\left(\phi \otimes \psi^{*}\right) \otimes\left(\xi \otimes \zeta^{*}\right) \in \mathfrak{g} \mathfrak{l}\left(W^{+}\right) \otimes_{\mathbb{C}} \mathfrak{g} \mathfrak{l}(E) .$$
Writing $B \in \mathfrak{g l}\left(W^{+}\right)$(or $\left.\mathfrak{g} \mathfrak{l}(E)\right)$ as $B=B_{h}+B_{s}$, where $B_{h}=\frac{1}{2}\left(B+B^{\dagger}\right)$ is Hermitian and $B_{s}=\frac{1}{2}\left(B-B^{\dagger}\right)$ is skew-Hermitian, we have
$$\begin{aligned}
\Phi \otimes \Psi^{*}= & \frac{1}{4}\left(\phi \otimes \psi^{*}+\psi \otimes \phi^{*}\right) \otimes\left(\xi \otimes \zeta^{*}+\zeta \otimes \xi^{*}\right) \\
& +\frac{1}{4}\left(\phi \otimes \psi^{*}-\psi \otimes \phi^{*}\right) \otimes\left(\xi \otimes \zeta^{*}-\zeta \otimes \xi^{*}\right) \\
& +\frac{1}{4}\left(\phi \otimes \psi^{*}+\psi \otimes \phi^{*}\right) \otimes\left(\xi \otimes \zeta^{*}-\zeta \otimes \xi^{*}\right) \\
& +\frac{1}{4}\left(\phi \otimes \psi^{*}-\psi \otimes \phi^{*}\right) \otimes\left(\xi \otimes \zeta^{*}+\zeta \otimes \xi^{*}\right),
\end{aligned}$$
and similarly for $\Psi \otimes \Phi^{*}$. Therefore,
$$\begin{aligned}
\Phi \otimes \Psi^{*}+\Psi \otimes \Phi^{*}= & \frac{1}{2}\left(\phi \otimes \psi^{*}+\psi \otimes \phi^{*}\right) \otimes\left(\xi \otimes \zeta^{*}+\zeta \otimes \xi^{*}\right) \\
& +\frac{1}{2}\left(\phi \otimes \psi^{*}-\psi \otimes \phi^{*}\right) \otimes\left(\xi \otimes \zeta^{*}-\zeta \otimes \xi^{*}\right) \\
= & -\frac{1}{2} i\left(\phi \otimes \psi^{*}+\psi \otimes \phi^{*}\right) \otimes i\left(\xi \otimes \zeta^{*}+\zeta \otimes \xi^{*}\right) \\
& +\frac{1}{2}\left(\phi \otimes \psi^{*}-\psi \otimes \phi^{*}\right) \otimes\left(\xi \otimes \zeta^{*}-\zeta \otimes \xi^{*}\right) .
\end{aligned}$$
We shall need the following elementary observation in our proof of transversality for the moduli space of PU(2) monopoles in §5. Note that as $\rho: \Lambda^{+} \rightarrow \mathfrak{s u}\left(W^{+}\right)$is an isomorphism, the rank of a section $v$ of $\Lambda^{+} \otimes \mathfrak{s u}(E)$ is equal to the rank of the section $\rho(v)$ of $\mathfrak{s} \mathfrak{u}\left(W^{+}\right) \otimes \mathfrak{s} \mathfrak{u}(E)$.

Lemma 2.21. If $\Phi \in C^{0}\left(W^{+} \otimes E\right)$ and $x \in X$, then the following hold:
\begin{itemize}
\item[1.] $\operatorname{Rank}_{\mathbb{R}}\left(\Phi(x) \otimes \Phi^{*}(x)\right)_{00}=1$ if and only if $\operatorname{Rank}_{\mathbb{C}} \Phi(x)=1$,
\item[2.] $\operatorname{Rank}_{\mathbb{R}}\left(\Phi(x) \otimes \Phi^{*}(x)\right)_{00}=3$ if and only if $\operatorname{Rank}_{\mathbb{C}} \Phi(x)=2$.
\end{itemize}

Proof. For convenience we write $\Phi, W^{+}$, and $E$ for $\left.\Phi\right|_{x},\left.W^{+}\right|_{x}$, and $\left.E\right|_{x}$. If $\Phi \in$ $\operatorname{Hom}\left(W^{+}, E\right)$ has complex rank one, we can write $\Phi=\phi \otimes \xi$, for $\phi \in W^{+}$and $\xi \in E$. Then $\left(\Phi \otimes \Phi^{*}\right)_{00}=-i\left(\phi \otimes \phi^{*}\right)_{0} \otimes i\left(\xi \otimes \xi^{*}\right)_{0}$ and so $\left(\Phi \otimes \Phi^{*}\right)_{00} \in \operatorname{Hom}\left(\mathfrak{s u}\left(W^{+}\right), \mathfrak{s u}(E)\right)$ has real rank one.

Conversely, suppose $\left(\Phi \otimes \Phi^{*}\right)_{00}$ has real rank one. Let $\left\{\xi_{1}, \xi_{2}\right\}$ be an orthonormal basis for $E$ and write $\Phi=\phi_{1} \otimes \xi_{1}+\phi_{2} \otimes \xi_{2}$ : if $\phi_{1}, \phi_{2} \in E$ are linearly dependent then $\Phi$ has complex rank one and we are done, so suppose that $\phi_{1}, \phi_{2}$ are linearly independent. Using the standard basis $\left\{\sigma_{1}, \sigma_{2}, \sigma_{3}\right\}$ of Pauli matrices (2.14) for $\mathfrak{s} \mathfrak{u}(2)$, namely
$$\sigma_{1}=\left(\begin{array}{cc}
i & 0 \\
0 & -i
\end{array}\right), \quad \sigma_{2}=\left(\begin{array}{cc}
0 & 1 \\
-1 & 0
\end{array}\right), \quad \sigma_{3}=\left(\begin{array}{cc}
0 & i \\
i & 0
\end{array}\right),$$
we obtain bases for the real vector spaces $\mathfrak{s u}\left(W^{+}\right)$and $\mathfrak{s u}(E)$ :
$$\begin{gathered}
\sigma_{1}^{e}=i\left(\xi_{1} \otimes \xi_{1}^{*}-\xi_{2} \otimes \xi_{2}^{*}\right), \quad \sigma_{2}^{e}=\xi_{1} \otimes \xi_{2}^{*}-\xi_{2} \otimes \xi_{1}^{*}, \quad \sigma_{3}^{e}=i\left(\xi_{1} \otimes \xi_{2}^{*}+\xi_{2} \otimes \xi_{1}^{*}\right), \\
\sigma_{1}^{w}=i\left(\phi_{1} \otimes \phi_{1}^{*}-\phi_{2} \otimes \phi_{2}^{*}\right), \quad \sigma_{2}^{w}=\phi_{1} \otimes \phi_{2}^{*}-\phi_{2} \otimes \phi_{1}^{*}, \quad \sigma_{3}^{w}=i\left(\phi_{1} \otimes \phi_{2}^{*}+\phi_{2} \otimes \phi_{1}^{*}\right) .
\end{gathered}$$
Writing $\Phi=\Phi_{1}+\Phi_{2}$, we have $\left(\Phi_{a} \otimes \Phi_{a}^{*}\right)_{00}=-i\left(\phi_{a} \otimes \phi_{a}^{*}\right)_{0} \otimes i\left(\xi_{a} \otimes \xi_{a}^{*}\right)_{0}$ for $a=1,2$ and
$$\left(\Phi \otimes \Phi^{*}\right)_{00}=\left(\Phi_{1} \otimes \Phi_{1}^{*}\right)_{00}+\left(\Phi_{1} \otimes \Phi_{2}^{*}+\Phi_{2} \otimes \Phi_{1}^{*}\right)_{00}+\left(\Phi_{2} \otimes \Phi_{2}^{*}\right)_{00} .$$
So, by the identity (2.13) and noting that $i\left(\xi_{1} \otimes \xi_{1}^{*}\right)_{0}=\frac{1}{2} i\left(\xi_{1} \otimes \xi_{1}^{*}-\xi_{2} \otimes \xi_{2}^{*}\right)=\frac{1}{2} \sigma_{1}^{e}=$ $-i\left(\xi_{2} \otimes \xi_{2}^{*}\right)_{0}$, and $i\left(\phi_{1} \otimes \phi_{1}^{*}\right)_{0}=\frac{1}{2} i\left(\phi_{1} \otimes \phi_{1}^{*}-\phi_{2} \otimes \phi_{2}^{*}\right)=\frac{1}{2} \sigma_{1}^{w}=-i\left(\phi_{2} \otimes \phi_{2}^{*}\right)_{0}$ we see that
$$\begin{aligned}
\left(\Phi \otimes \Phi^{*}\right)_{00}= & -i\left(\phi_{1} \otimes \phi_{1}^{*}\right)_{0} \otimes i\left(\xi_{1} \otimes \xi_{1}^{*}\right)_{0}-i\left(\phi_{2} \otimes \phi_{2}^{*}\right)_{0} \otimes i\left(\xi_{2} \otimes \xi_{2}^{*}\right)_{0} \\
& -\frac{1}{2} i\left(\phi_{1} \otimes \phi_{2}^{*}+\phi_{2} \otimes \phi_{1}^{*}\right) \otimes i\left(\xi_{1} \otimes \xi_{2}^{*}+\xi_{2} \otimes \xi_{1}^{*}\right) \\
& +\frac{1}{2}\left(\phi_{1} \otimes \phi_{2}^{*}-\phi_{2} \otimes \phi_{1}^{*}\right) \otimes\left(\xi_{1} \otimes \xi_{2}^{*}-\xi_{2} \otimes \xi_{1}^{*}\right) \\
= & -\frac{1}{4} \sigma_{1}^{w} \otimes \sigma_{1}^{e}-\frac{1}{4} \sigma_{1}^{w} \otimes \sigma_{1}^{e}-\frac{1}{2} \sigma_{3}^{w} \otimes \sigma_{3}^{e}+\frac{1}{2} \sigma_{2}^{w} \otimes \sigma_{2}^{e} \\
= & -\frac{1}{2} \sigma_{1}^{w} \otimes \sigma_{1}^{e}+\frac{1}{2} \sigma_{2}^{w} \otimes \sigma_{2}^{e}-\frac{1}{2} \sigma_{3}^{w} \otimes \sigma_{3}^{e} .
\end{aligned}$$
Thus, $\left(\Phi \otimes \Phi^{*}\right)_{00}$ would have real rank three, a contradiction, and so $\Phi$ must have complex rank one, which proves Assertion 1.

The preceding argument also shows that if $\Phi$ has complex rank two, then $\left(\Phi \otimes \Phi^{*}\right)_{00}$ has real rank three. Conversely, if $\left(\Phi \otimes \Phi^{*}\right)_{00}$ has real rank three, then $\Phi$ cannot have complex rank one by Assertion 1, so $\Phi$ has complex rank two. \(\square\)
2.5. The PU(2) monopole equations and holonomy perturbations. In §2.5.1 we describe the PU(2) monopole equations in their unperturbed form, following [71, 74]. In §2.5.2 we introduce the holonomy perturbations and the perturbed PU(2) monopole equations, deferring a detailed discussion of most of the technical regularity issues concerning holonomy perturbations to the Appendix. In Donaldson's application to the extended anti-self-dual equation, some important features ensure that the requisite analysis is relatively tractable: (i) reducible connections can be excluded from the compactification of the extended moduli spaces [18, p. 283], (ii) the cohomology groups for the elliptic complex of his extended equations have simple weak semi-continuity properties with respect to Uhlenbeck limits [18, Proposition 4.33], and (iii) the zero locus being perturbed is cut out of a finite-dimensional manifold [18, p. 281, Lemma 4.35, \& Corollary 4.38]. For the development of Donaldson's method for PU(2) monopoles described here, none of these simplifying features hold and so the corresponding transversality argument is rather complicated. Indeed, one can see from Proposition 7.1.32 in [20] that because of the Dirac operator, the behavior of the cokernels of the linearization of the PU(2) monopole equations can be quite involved under Uhlenbeck limits. The holonomy perturbations considered by Donaldson in [18] are inhomogeneous, as he uses the perturbations to kill the cokernels $\operatorname{Coker} d_{A}^{+}$ directly. In contrast, the perturbations we consider in (1.3) are homogeneous and we shall argue indirectly in §5 that the cokernels of the linearization vanish away from the reducible and zero-section solutions.
2.5.1. The unperturbed PU(2) monopole equations. Recall that we consider Hermitian two-plane bundles $E$ over $X$ whose determinant line bundles $\operatorname{det} E$ are isomorphic to a fixed Hermitian line bundle over $X$ endowed with a fixed $C^{\infty}$, unitary connection $A_{e}$. Let $\left(\rho, W^{+}, W^{-}\right)$be a spin ${ }^{c}$ structure on $X$, where $\rho: T^{*} X \rightarrow \operatorname{End} W$ is the Clifford map, and the Hermitian four-plane bundle $W=W^{+} \oplus W^{-}$is endowed with a $C^{\infty}$ spin ${ }^{c}$ connection. Given a connection $A$ on $E$ with curvature $F_{A} \in L_{k-1}^{2}\left(\Lambda^{2} \otimes \mathfrak{u}(E)\right)$, then $\left(F_{A}^{+}\right)_{0} \in L_{k-1}^{2}\left(\Lambda^{+} \otimes \mathfrak{s u}(E)\right)$ denotes the traceless part of its self-dual component. Equivalently, if $A$ is a connection on $\mathfrak{s u}(E)$ with curvature $F_{A} \in L_{k-1}^{2}\left(\Lambda^{2} \otimes \mathfrak{s o}(\mathfrak{s u}(E))\right)$, then $F_{A}^{+} \in L_{k-1}^{2}\left(\Lambda^{+} \otimes \mathfrak{s} \mathfrak{u}(E)\right)$ is its self-dual component, viewed as a section of $\Lambda^{+} \otimes \mathfrak{s u}(E)$ via the implicit isomorphism ad : $\mathfrak{s u}(E) \rightarrow \mathfrak{s o}(\mathfrak{s u}(E))$. Let $D_{A}: L_{k}^{2}\left(W^{+} \otimes\right.$ $E) \rightarrow L_{k-1}^{2}\left(W^{-} \otimes E\right)$ be the corresponding Dirac operator.

For an $L_{k}^{2}$ section $\Phi$ of $W^{+} \otimes E$, let $\Phi^{*}$ be its pointwise Hermitian dual and let $\left(\Phi \otimes \Phi^{*}\right)_{00}$ be the component of the Hermitian endomorphism $\Phi \otimes \Phi^{*}$ of $W^{+} \otimes E$ which lies in $\mathfrak{s u}\left(W^{+}\right) \otimes \mathfrak{s u}(E)$. The Clifford map $\rho$ defines an isomorphism $\rho: \Lambda^{+} \rightarrow \mathfrak{s u}\left(W^{+}\right)$ and thus an isomorphism $\rho=\rho \otimes \operatorname{id}_{\mathfrak{s u}(E)}$ of $\Lambda^{+} \otimes \mathfrak{s u}(E)$ with $\mathfrak{s u}\left(W^{+}\right) \otimes \mathfrak{s u}(E)$. Then
$$\begin{aligned}
F_{A}^{+}-\rho^{-1}\left(\Phi \otimes \Phi^{*}\right)_{00} & =0 \\
D_{A} \Phi & =0
\end{aligned}$$
are the unperturbed equations considered in [67, 68, 71, 74] (with slightly differing trace conditions) for a pair $(A, \Phi)$ consisting of a connection $A$ on $\mathfrak{s u}(E)$ and a section
$\Phi$ of $W^{+} \otimes E$. Equivalently, given a pair ( $A, \Phi$ ) with $A$ a fixed-determinant connection on $E$, the equations (2.15) take the same form except that $F_{A}^{+}$is replaced by $\left(F_{A}^{+}\right)_{0}$.
2.5.2. The perturbed PU(2) monopole equations. We next introduce perturbations of the PU(2) monopole equations (2.15) which will enable us to prove the transversality result described in Theorem 1.3. The perturbations in question make use of holonomy and their construction is partly modelled on related perturbations introduced by Donaldson, Floer and Taubes [8, 17, 29, 18, 86]. All of these constructions require that a unitary connection $A$ on a Hermitian two-plane bundle $E$ over $X$ be regular enough that parallel translation along a $C^{\infty}$ path in $X$ is well-defined. For example, Floer employs a configuration space of $L_{1}^{4}$ connections modulo $L_{2}^{4}$ gauge-transformations over a three-manifold, so these connections are at least continuous (as $L_{1}^{4} \subset C^{0}$ in dimension three) and the standard theory of ordinary differential equations applies to define parallel translation without further qualification [29]. In dimension four, parallel translation can be defined without difficulty using $L_{k}^{2}$ connections with $k \geq 3$. With a little more care one can see that parallel translation can be defined by $L_{2}^{2}$ connections, even though $L_{2}^{2} \not \subset C^{0}$ [61, §3.2]. These regularity issues become rather more intractable, as one can see from the Sobolev restriction theorem, for connections which are only $L_{1}^{2}$ [2, Theorem V.5.4]. As explained in the Appendix - to which we refer the reader for a discussion of the more technical points - we shall ultimately restrict our attention to configuration spaces of $L_{k}^{2}$ connections with $k \geq 3$. The perturbations will, by definition, be zero on a neighborhood of a point in $X$ where the curvature is large and so our regularity theory for $L_{1}^{2}$ monopoles will apply near points where curvature has bubbled off in order to prove removability of singularities (see §4.5.2).

We follow standard convention by saying that a connection $A$ on a $G$ bundle $E$ over a connected manifold $Y$ is 'irreducible' if its stabilizer $\operatorname{Stab}_{A}$ is trivial, that is, the center of the Lie group $G$ [20, p. 133], rather than saying (more correctly) that its holonomy group $\operatorname{Hol}_{A}\left(y_{0}\right)$ is not a proper Lie subgroup of $\operatorname{Aut}\left(E_{y_{0}}\right) \simeq G$ (where $y_{0} \in Y$ is any basepoint). However, the holonomy will be our primary concern in this section, so some care is required as the two notions do not coincide in general. Recall from [20, Lemma 4.2.8] that $\operatorname{Stab}_{A}$ is isomorphic to the centralizer of $\operatorname{Hol}_{A}\left(y_{0}\right)$ in $G$. If $Y$ is simply connected, then $\operatorname{Hol}_{A}\left(y_{0}\right)$ is a connected Lie subgroup of $G$ [44, Theorem II.4.2]. Thus, if $G=\operatorname{SU}(2)$ or SO(3) and $Y$ is simply connected, then $A$ has trivial stabilizer in $G$ if and only if $\operatorname{Hol}_{A}\left(y_{0}\right) \simeq G$ [20, p. 133]. Indeed, if $G=\operatorname{SO}(3)$ and $\operatorname{Stab}_{A}=\{\mathrm{id}\}$, then $H:=\operatorname{Hol}_{A}\left(y_{0}\right)=\operatorname{SO}(3)$; otherwise, we would have
\begin{itemize}
\item[-] $H=\mathrm{SO}(2)$, with centralizer $Z(H)=\mathrm{SO}(2)$ (by [11, Theorem IV.2.3(ii)]), contradicting $\operatorname{Stab}_{A}=\{\mathrm{id}\}$, or
\item[-] $H=\{\mathrm{id}\}$, with centralizer $Z(H)=\operatorname{SO}(3)$, again contradicting $\operatorname{Stab}_{A}=\{\mathrm{id}\}$.
\end{itemize}
The same argument holds for $G=\operatorname{SU}(2)$, but not for higher-dimensional Lie groups. For example, if $G=\mathrm{U}(2)=\mathrm{SU}(2) \times_{\{ \pm \mathrm{id}\}} S^{1}$, we cannot exclude the possibility that a

U(2) connection $A$ with $\operatorname{Stab}_{A}=S_{Z}^{1}$ reduces to an SU(2) connection, that is, $A$ has holonomy $\operatorname{Hol}_{A}\left(y_{0}\right)=\mathrm{SU}(2)$.

With the preceding comments in mind, the first ingredient in our construction of the holonomy perturbations is a local section of $\mathfrak{s u}(E)$ given by the holonomy of an SO(3) connection $A$ on $\mathfrak{s} \mathfrak{u}(E)$. Let $\gamma \subset X$ be a $C^{\infty}$ loop based at a point $x_{0} \in X$ and let
$$\left.h_{\gamma, x_{0}}(A) \in \mathrm{SO}(\mathfrak{s u}(E))\right|_{x_{0}}$$
be the holonomy of the connection $A$ around the loop $\gamma$. The exponential map $\exp : \mathfrak{s o}(3) \rightarrow \operatorname{SO}(3)$ gives a diffeomorphism from a ball $2 B$ around the origin in $\mathfrak{s} \mathfrak{o}(3)$ to a ball around the identity in SO(3). Let $\psi: \mathbb{R} \rightarrow[0,1]$ be a $C^{\infty}$ cutoff function such that $\psi(|\zeta|)=1$ for $\zeta \in \frac{1}{2} B, \psi(|\zeta|)>0$ for $\zeta \in B$, and $\psi(|\zeta|)=0$ for $\zeta \in \mathfrak{s o}(3)-B$. Then
$$\mathfrak{h}_{\gamma, x_{0}}(A):=\psi\left(\left|\exp ^{-1}\left(h_{\gamma, x_{0}}(A)\right)\right|\right) \cdot \operatorname{ad}^{-1}\left(\exp ^{-1}\left(h_{\gamma, x_{0}}(A)\right)\right)$$
defines a gauge-equivariant map $\left.\mathcal{A}_{E}(X) \rightarrow \mathfrak{s u}(E)\right|_{x_{0}}$, where ad : $\mathfrak{s u}(E) \rightarrow \mathfrak{s o}(\mathfrak{s u}(E))$ is the standard isomorphism.

Lemma 2.22. Let $U \subset X$ be a simply connected open subset and let $x_{0}$ be a point in $U$. If $\left.A\right|_{U}$ is an irreducible SO(3) connection on $\left.\mathfrak{s} \mathfrak{u}(E)\right|_{U}$ then there are loops $\left\{\gamma_{l}\right\}_{l=1}^{3} \subset U$, depending on $A$, such that the set $\left.\left\{h_{\gamma_{l}, x_{0}}(A)\right\}_{l=1}^{3} \subset \operatorname{SO}(\mathfrak{s u}(E))\right|_{x_{0}}$ lies in the open subset of $\left.\operatorname{SO}(\mathfrak{s u}(E))\right|_{x_{0}}$ given by the image under exp of the ball $B \subset$ $\left.\mathfrak{s} \mathfrak{o}(\mathfrak{s} \mathfrak{u}(E))\right|_{x_{0}}$ around the identity. The set $\left\{\mathfrak{h}_{\gamma_{l}, x_{0}}(A)\right\}_{l=1}^{3}$ is then a basis for $\left.\mathfrak{s} \mathfrak{u}(E)\right|_{x_{0}}$.

Proof. Since $\left.A\right|_{U}$ is an irreducible SO(3) connection over a simply connected manifold $U$, the holonomy group $\operatorname{Hol}_{A \mid U}\left(x_{0}\right)$ is equal to $\left.\operatorname{SO}(\mathfrak{s u}(E))\right|_{x_{0}}$ by the remarks preceding the statement of the lemma. Hence, there are three loops $\gamma_{1}, \gamma_{2}, \gamma_{3}$ such that the holonomies $\left.h_{\gamma_{l}, x_{0}}(A) \in B \subset \operatorname{SO}(\mathfrak{s u}(E))\right|_{x_{0}}$ give a basis $\left\{\mathfrak{h}_{\gamma_{l}, x_{0}}(A)\right\}_{l=1}^{3}$ for $\left.\mathfrak{s} \mathfrak{u}(E)\right|_{x_{0}}$. \(\square\)

For a $C^{\infty}$ connection $A$ we may extend $\mathfrak{h}_{\gamma, x_{0}}(A)$ to a $C^{\infty}$ section $\hat{\mathfrak{h}}_{\gamma}(A)$ of $\mathfrak{s} \mathfrak{u}(E)$ by radial parallel translation, with respect to $A$ over a small ball $B\left(x_{0}, 2 R_{0}\right)$ and then multiplying by a $C^{\infty}$ cutoff function $\varphi$ on $X$ which is positive on $B\left(x_{0}, R_{0}\right)$ and identically zero on $X-B\left(x_{0}, R_{0}\right)$. Thus if the set $\left\{\mathfrak{h}_{\gamma_{l}, x_{0}}(A)\right\}_{l=1}^{3}$ spans $\left.\mathfrak{s} \mathfrak{u}(E)\right|_{x_{0}}$, then the set $\left\{\left.\varphi \hat{\mathfrak{h}}_{\gamma_{l}}(A)\right|_{y}\right\}_{l=1}^{4}$ will span $\left.\mathfrak{s} \mathfrak{u}(E)\right|_{y}$ for $y \in B\left(x_{0}, R_{0}\right)$. The constant $R_{0}$ is chosen so that $4 R_{0}$ is smaller than the injectivity radius of $(X, g)$.

In general, for an $L_{k}^{2}$ connection $A$ with $k \geq 2$, the section $\hat{\mathfrak{h}}_{\gamma}(A)$ will not be in $L_{k+1}^{2}$ and so we use the Neumann heat operator, for fixed small $t>0$,
$$K_{t}\left(\left.A\right|_{B\left(x_{0}, 2 R_{0}\right)}\right): L^{2}\left(B\left(x_{0}, 2 R_{0}\right), \mathfrak{s} \mathfrak{u}(E)\right) \rightarrow L_{k+1}^{2}\left(B\left(x_{0}, 2 R_{0}\right), \mathfrak{s} \mathfrak{u}(E)\right),$$
as discussed in Appendix A. 1 to construct an $L_{k+1}^{2}$ section
$$\mathfrak{h}_{\gamma}(A):=K_{t}\left(\left.A\right|_{B\left(x_{0}, 2 R_{0}\right)}\right) \hat{\mathfrak{h}}_{\gamma}(A)$$
of $\mathfrak{s} \mathfrak{u}(E)$ over $B\left(x_{0}, 2 R_{0}\right)$ which converges to $\hat{\mathfrak{h}}_{\gamma}(A)$ in $C^{0}\left(B\left(x_{0}, R_{0}\right)\right)$ as $t \rightarrow 0$. Therefore, for small enough $t=t(A)$, the set $\left\{\left.\varphi \mathfrak{h}_{\gamma_{l}}(A)\right|_{y}\right\}_{l=1}^{3}$, will span $\left.\mathfrak{s u}(E)\right|_{y}$ for all $y \in B\left(x_{0}, R_{0}\right)$ just as before.

Lemma 2.23. Let $k \geq 2$ be an integer and let $A_{0}$ be an $L_{k}^{2}$ unitary connection on $\left.E\right|_{B\left(x_{0}, 2 R_{0}\right)}$. Let $\gamma_{1}, \gamma_{2}, \gamma_{3}$ be loops in $B\left(x_{0}, 2 R_{0}\right)$ based at $x_{0}$ such that $\left\{\mathfrak{h}_{\gamma_{l}, x_{0}}\left(A_{0}\right)\right\}_{l=1}^{3}$ spans $\left.\mathfrak{s u}(E)\right|_{x_{0}}$. Then there is a positive constant $\varepsilon\left(A_{0},\left\{\gamma_{l}\right\}\right)$ such that the following holds. If $A$ is an $L_{k}^{2}$ unitary connection on $\left.E\right|_{B\left(x_{0}, 2 R_{0}\right)}$ such that
$$\left\|A-A_{0}\right\|_{L_{k, A_{0}}^{2}\left(B\left(x_{0}, 2 R_{0}\right)\right)}<\varepsilon,$$
then the set $\left\{\mathfrak{h}_{\gamma_{l}, x_{0}}(A)\right\}_{l=1}^{3}$ spans $\left.\mathfrak{s u}(E)\right|_{x_{0}}$.
Proof. According to Lemma A. 3 the holonomy maps $h_{\gamma, x_{0}}:\left.\mathcal{A}_{E}(X) \rightarrow \mathrm{U}(E)\right|_{x_{0}}$ are continuous and so the maps $\mathfrak{h}_{\gamma_{l}, x_{0}}:\left.\mathcal{A}_{E}(X) \rightarrow \mathfrak{s u}(E)\right|_{x_{0}}$ are continuous on small open neighborhoods of $A_{0} \in \mathcal{A}_{E}(X)$. Hence, for small enough $\varepsilon$, the set $\left\{\mathfrak{h}_{\gamma_{l}, x_{0}}(A)\right\}_{l=1}^{3}$ spans $\left.\mathfrak{s u}(E)\right|_{x_{0}}$. \(\square\)

We now specify the loops to be used in this construction, essentially following the argument used in the proof of Lemma 2.5 in [17]. Let $\left\{B\left(x_{j}, 4 R_{0}\right)\right\}_{j=1}^{N_{b}}$, be a disjoint collection of open balls, where $N_{b}$ is a fixed integer to be specified later (see §4.5.2). According to the slice results of [20, p. 192], [87, Proposition 2.1] for manifolds with boundary, the quotient space $\mathcal{B}_{E}^{*}\left(B\left(x_{j}, 2 R_{0}\right)\right)$ of irreducible $L_{k}^{2}$ connections on $\left.E\right|_{B\left(x_{j}, 2 R_{0}\right)}$ is a $C^{\infty}$ manifold modelled on a separable Hilbert space. The quotient $L_{k}^{2}$ topology on $\mathcal{B}_{E}^{*}\left(B\left(x_{j}, 2 R_{0}\right)\right)$ is clearly metrizable and so Stone's Theorem implies that $\mathcal{B}_{E}^{*}\left(B\left(x_{j}, 2 R_{0}\right)\right)$ is paracompact and thus admits partitions of unity [55, Corollary II.3.8].

For each $j=1, \ldots, N_{b}$ and each point $\left[A_{0}\right]$ in $\mathcal{B}_{E}^{*}\left(B\left(x_{j}, 2 R_{0}\right)\right)$, we can find loops $\left\{\gamma_{j, l, A_{0}}\right\}_{l=1}^{3}$, contained in $B\left(x_{j}, 2 R_{0}\right)$ and based at $x_{j}$ such that $\left\{\mathfrak{h}_{\gamma_{j, l, A_{0}}}\left(A_{0}\right)\right\}_{l=1}^{3}$, spans $\left.\mathfrak{s} \mathfrak{u}(E)\right|_{x_{j}}$. For each such point $\left[A_{0}\right]$, Lemma 2.23 implies that there is an $L_{k, A_{0}}^{2}$ ball
$$B_{\left[A_{0}\right]}\left(\varepsilon_{A_{0}}\right):=\left\{[A] \in \mathcal{B}_{E}^{*}\left(B\left(x_{j}, 2 R_{0}\right)\right): \operatorname{dist}_{L_{k, A_{0}}^{2}}\left([A],\left[A_{0}\right]\right)<\varepsilon_{A_{0}}\right\}$$
such that for all $[A] \in B_{\left[A_{0}\right]}\left(\varepsilon_{A_{0}}\right)$, the set $\left\{\mathfrak{h}_{\gamma_{j, l, A_{0}}}(A)\right\}_{l=1}^{3}$ spans $\left.\mathfrak{s u}(E)\right|_{x_{j}}$. These balls give an open cover of $\mathcal{B}_{E}^{*}\left(B\left(x_{j}, 2 R_{0}\right)\right)$ and hence there is a locally finite refinement of this open cover, $\left\{U_{j, \alpha}\right\}_{\alpha=1}^{\infty}$, and a positive partition $\chi_{j, \alpha}$ (see Proposition A.12) subordinate to $\left\{U_{j, \alpha}\right\}_{\alpha=1}^{\infty}$ in the sense that
$$\sum_{\alpha} \chi_{j, \alpha}[A]>0, \quad[A] \in \mathcal{B}_{E}^{*}\left(B\left(x_{j}, 2 R_{0}\right)\right) .$$
Hence, for each $U_{j, \alpha}$, we obtain loops $\left\{\gamma_{j, l, \alpha}\right\}_{l=1}^{3} \subset B\left(x_{j}, 2 R_{0}\right)$ such that for all $[A] \in$ $U_{j, \alpha}$, the sections $\mathfrak{h}_{\gamma_{j, l, \alpha}}(A)$ span $\left.\mathfrak{s} \mathfrak{u}(E)\right|_{x_{j}}$.

Let $\beta$ be a smooth cutoff function on $\mathbb{R}$ such that $\beta(t)=1$ for $t \leq \frac{1}{2}$ and $\beta(t)=0$ for $t \geq 1$, with $\beta(t)>0$ for $t<1$. Then the $C^{\infty}$ gauge-invariant maps $\mathcal{A}_{E}(X) \rightarrow \mathbb{R}$,
$A \mapsto \beta_{j}[A]$ given by
$$\beta_{j}[A]:=\beta\left(\frac{1}{\varepsilon_{0}^{2}} \int_{B\left(x_{j}, 4 R_{0}\right)} \beta\left(\frac{\operatorname{dist}_{g}\left(\cdot, x_{j}\right)}{4 R_{0}}\right)\left|F_{A}\right|^{2} d V\right)$$
are zero when the energy of the connection $A$ is greater than or equal to $\frac{1}{2} \varepsilon_{0}^{2}$ over a ball $B\left(x_{j}, 2 R_{0}\right)$. Here, $\varepsilon_{0}$ is the constant of Corollary 3.16. Finally, we define $C^{\infty}$ cutoff functions on $X$ by setting
$$\varphi_{j}(x):=\beta\left(\frac{\operatorname{dist}_{g}\left(x, x_{j}\right)}{R_{0}}\right), \quad x \in X,$$
so that $\varphi_{j}$ is positive on the ball $B\left(x_{j}, R_{0}\right)$ and zero on its complement in $X$.
We can now define a gauge equivariant $C^{\infty}$ map
$$\mathcal{A}_{E}(X) \rightarrow L_{k+1}^{2}(X, \mathfrak{s u}(E)), \quad A \mapsto \mathfrak{m}_{j, l, \alpha}(A)$$
by setting
$$\mathfrak{m}_{j, l, \alpha}(A):=\beta_{j}[A] \chi_{j, \alpha}\left[\left.A\right|_{B\left(x_{j}, 2 R_{0}\right)}\right] \varphi_{j} \mathfrak{h}_{\gamma_{j, l, \alpha}}(A) .$$
Thus at each point $A \in \mathcal{A}_{E}(X)$ only a finite number of the $\mathfrak{m}_{j, l, \alpha}(A)$ are non-zero and each map $\mathfrak{m}_{j, l, \alpha}$ is $C^{\infty}$ with uniformly bounded derivatives of all orders on $\mathcal{A}_{E}(X)$ (see Appendix A.4).

To define the perturbation of the Dirac operator in (2.15), we need elements of $\Omega^{0}\left(\operatorname{Hom}_{\mathbb{C}}\left(W^{+}, W^{-}\right)\right)$and these are conveniently provided by complex one-forms using the Clifford isomorphism
$$\rho: \Lambda_{\mathbb{C}}^{1} \rightarrow \operatorname{Hom}_{\mathbb{C}}\left(W^{+}, W^{-}\right),$$
where $\Lambda_{\mathbb{C}}^{1}=\Lambda^{1} \otimes_{\mathbb{R}} \mathbb{C}$. These one-forms are parametrized by the following Banach space: Let $\mathbb{A}$ be the index set $\left\{(j, l, \alpha): 1 \leq j \leq N_{b}, 1 \leq l \leq 3, \alpha \in \mathbb{N}\right\}$, let $\delta=\left(\delta_{\alpha}\right)_{\alpha=1}^{\infty} \in \ell^{1}(\mathbb{R})$ be the sequence of positive weights described in Appendix A.4, let $r \geq k+1$, and let
$$\mathcal{P}_{\vartheta}^{r}:=\ell_{\delta}^{1}\left(\mathbb{A}, C^{r}\left(X, \Lambda_{\mathbb{C}}^{1}\right)\right)$$
be the set of sequences $\vec{\vartheta}:=\left(\vartheta_{j, l, \alpha}\right)$ in $C^{r}\left(X, \Lambda_{\mathbb{C}}^{1}\right)$ such that
$$\|\vec{\vartheta}\|_{\ell_{\delta}^{1}\left(C^{r}(X)\right)}:=\sum_{j, l, \alpha} \delta_{\alpha}^{-1}\left\|\vartheta_{j, l, \alpha}\right\|_{C^{r}(X)}<\infty .$$
Then $\mathcal{P}_{\vartheta}^{r}$ is a Banach space with respect to the above norm [40, §1.7].
Remark 2.24. 1. Note that we measure reducibility of connections and allow the loops $\gamma_{j, l, \alpha}$ to be contained in the larger balls $B\left(x_{j}, 2 R_{0}\right)$ while the perturbations are supported on the smaller balls $B\left(x_{j}, R_{0}\right)$. Thus, if $A \in \mathcal{A}_{E}(X)$ is a connection such that $\left.A\right|_{B\left(x_{j}, 2 R_{0}\right)}$ is reducible for all $j \in\left\{1, \ldots, N_{b}\right\}$ such that $\beta_{j}[A]>0$ and $\Phi \not \equiv 0$, then $[A, \Phi]$ cannot be a point in $M_{W, E}^{*, 0}$ : our unique continuation result for PU(2) monopoles (see Theorem 5.11) which are reducible on an open
\begin{itemize}
\item[] subset of $X$ containing all balls $\bar{B}\left(x_{j}, R_{0}\right)$ with $\beta_{j}[A]>0$ would imply that $A$ is reducible on all of $X$ and so $(A, \Phi)$ would be a reducible PU(2) monopole. Consequently, if $[A, \Phi] \in M_{W, E}^{*, 0}$ then $A$ must be irreducible on some ball $B\left(x_{j}, 2 R_{0}\right)$; otherwise, $A$ would be reducible on all balls $B\left(x_{j}, 2 R_{0}\right)$ with $\beta_{j}[A]>0$ and so reducible on $X$.
\item[2.] Note that the sections $\mathfrak{m}_{j, l, \alpha}$ are defined on the entire space $\mathcal{A}_{E}(X)$ : They are zero for connections $A \in \mathcal{A}_{E}(X)$ which are reducible when restricted to $B\left(x_{j}, 2 R_{0}\right)$.
\item[3.] Our energy bound (4.2) for solutions $(A, \Phi)$ to the perturbed PU(2) monopole equations ensures that there is always at least one ball $B\left(x_{j}, R_{0}\right)$ where the sections $\left\{\mathfrak{m}_{j, l, \alpha}(A)\right\}_{l=1}^{3}$ span $\left.\mathfrak{s} \mathfrak{u}(E)\right|_{B\left(x_{j}, R_{0}\right)}$ : see §4.5.2.
\end{itemize}

Because only a finite number of the sections $\mathfrak{m}_{j, l, \alpha}(A)$ are non-zero at each $A \in$ $\mathcal{A}_{E}(X)$ the sum
$$\vec{\vartheta} \cdot \overrightarrow{\mathfrak{m}}(A):=\sum_{j, l, \alpha} \rho\left(\vartheta_{j, l, \alpha}\right) \otimes_{\mathbb{C}} \mathfrak{m}_{j, l, \alpha}(A)$$
gives a well-defined $L_{k+1}^{2}$ section of $\operatorname{Hom}_{\mathbb{C}}\left(W^{+}, W^{-}\right) \otimes_{\mathbb{C}} \mathfrak{s l}(E) \simeq \Lambda_{\mathbb{C}}^{1} \otimes_{\mathbb{C}} \mathfrak{s l}(E)$. Note that although each $\mathfrak{m}_{j, l, \alpha}(A)$ is a section of $\mathfrak{s u}(E)$, the tensor product is over the complex numbers, where $\mathfrak{s u}(E)$ is contained in the complex space $\mathfrak{s l}(E)=\mathfrak{s u}(E) \otimes_{\mathbb{R}} \mathbb{C}$. (Since $\mathfrak{s} \mathfrak{l}(E)=\mathfrak{s} \mathfrak{u}(E) \oplus i \mathfrak{s} \mathfrak{u}(E)$, then $\operatorname{Hom}_{\mathbb{C}}\left(W^{+}, W^{-}\right) \otimes_{\mathbb{C}} \mathfrak{s} \mathfrak{u}(E)=\operatorname{Hom}_{\mathbb{C}}\left(W^{+}, W^{-}\right) \otimes_{\mathbb{C}} \mathfrak{g} \mathfrak{l}(E)$ and similarly for $\mathfrak{g l}(E)$.) The map
$$\mathcal{A}_{E}(X) \rightarrow L_{k+1}^{2}\left(X, \operatorname{Hom}_{\mathbb{C}}\left(W^{+}, W^{-}\right) \otimes_{\mathbb{C}} \mathfrak{s l}(E)\right), \quad A \mapsto \vec{\vartheta} \cdot \overrightarrow{\mathfrak{m}}(A)$$
is $C^{\infty}$ and gauge equivariant and so defines a $C^{\infty}$ section of the vector bundle
$$\mathcal{A}_{E}^{*}(X) \times_{\mathcal{G}_{E}} L_{k+1}^{2}\left(X, \operatorname{Hom}_{\mathbb{C}}\left(W^{+}, W^{-}\right) \otimes_{\mathbb{C}} \mathfrak{s} \mathfrak{l}(E)\right) \rightarrow \mathcal{B}_{E}^{*}(X) .$$
By construction (see Appendix A.4) the sum $\vec{\vartheta} \cdot \overrightarrow{\mathfrak{m}}(A)$ satisfies a $C^{0}$ estimate of the form
$$\sup _{A \in \mathcal{A}_{E}(X)}\|\vec{\vartheta} \cdot \overrightarrow{\mathfrak{m}}(A)\|_{L_{k+1, A}^{2}(X)} \leq C\|\vec{\vartheta}\|_{\ell_{\delta}^{1}\left(C^{r}(X)\right)} \quad \text { and } \quad\|\vec{\vartheta}\|_{\ell_{\delta}^{1}\left(C^{r}(X)\right)} \leq \varepsilon_{\vartheta},$$
where $C=C(g, k)$ and $\varepsilon_{\vartheta}$ is a positive constant which we are free to specify.
We shall also need to construct a gauge equivariant $C^{\infty}$ map from $\mathcal{A}_{E}^{*}(X)$ to $L_{k+1}^{2}\left(\mathfrak{g l}\left(\Lambda^{+}\right) \otimes_{\mathbb{R}} \mathfrak{s o}(\mathfrak{s u}(E))\right)$. This map will define a perturbation of the quadratic form in (2.15) using the representation ad : $\mathfrak{s u}(E) \rightarrow \mathfrak{s o}(\mathfrak{s u}(E))$ and is parametrized by the Banach space
$$\mathcal{P}_{\tau}^{r}:=\ell_{\delta}^{1}\left(\mathbb{A}, C^{r}\left(X, \mathfrak{g} \mathfrak{l}\left(\Lambda^{+}\right)\right)\right)$$
of sequences $\vec{\tau}:=\left(\tau_{j, l, \alpha}\right)$ in $C^{r}\left(X, \mathfrak{g} \mathfrak{l}\left(\Lambda^{+}\right)\right)$such that
$$\|\vec{\tau}\|_{\ell_{\delta}^{1}\left(C^{r}(X)\right)}:=\sum_{j, l, \alpha} \delta_{\alpha}^{-1}\left\|\tau_{j, l, \alpha}\right\|_{C^{r}(X)}<\infty .$$

Then the sum
$$\vec{\tau} \cdot \overrightarrow{\mathfrak{m}}(A):=\sum_{j, l, \alpha} \tau_{j, l, \alpha} \otimes_{\mathbb{R}} \operatorname{ad}\left(\mathfrak{m}_{j, l, \alpha}(A)\right)$$
is pointwise finite and gives a well-defined $L_{k+1}^{2}$ section of $\mathfrak{g} \mathfrak{l}\left(\Lambda^{+}\right) \otimes_{\mathbb{R}} \mathfrak{s} \mathfrak{o}(\mathfrak{s} \mathfrak{u}(E))$. The map
$$\mathcal{A}_{E}(X) \rightarrow L_{k+1}^{2}\left(X, \mathfrak{g} \mathfrak{l}\left(\Lambda^{+}\right) \otimes_{\mathbb{R}} \mathfrak{s} \mathfrak{o}(\mathfrak{s} \mathfrak{u}(E))\right), \quad A \mapsto \vec{\tau} \cdot \overrightarrow{\mathfrak{m}}(A)$$
is $C^{\infty}$ and gauge equivariant and so defines a $C^{\infty}$ section of the vector bundle
$$\mathcal{A}_{E}^{*}(X) \times_{\mathcal{G}_{E}} L_{k+1}^{2}\left(X, \mathfrak{g} \mathfrak{l}\left(\Lambda^{+}\right) \otimes_{\mathbb{R}} \mathfrak{s o}(\mathfrak{s u}(E))\right) \rightarrow \mathcal{B}_{E}^{*}(X) .$$
By construction (see Appendix A.4) the sum $\vec{\tau} \cdot \overrightarrow{\mathfrak{m}}(A)$ satisfies $C^{0}$ estimates
$$\sup _{A \in \mathcal{A}_{E}(X)}\|\vec{\tau} \cdot \overrightarrow{\mathfrak{m}}(A)\|_{L_{k+1, A}^{2}(X)} \leq C\|\vec{\tau}\|_{\ell_{\delta}^{1}\left(C^{r}(X)\right)} \quad \text { and } \quad\|\vec{\tau}\|_{\ell_{\delta}^{1}\left(C^{r}(X)\right)} \leq \varepsilon_{\tau},$$
where $C=C(g, k)$ and $\varepsilon_{\tau}$ is a positive constant which we are free to specify.
Our perturbed $\mathrm{PU}(2)$ monopole equations for a pair $(A, \Phi)$ on $\left(\mathfrak{s u}(E), W^{+} \otimes E\right)$ then take the form
$$\begin{aligned}
& \mathfrak{S}_{1}(A, \Phi):=F_{A}^{+}-\left(\mathrm{id}+\tau_{0} \otimes \mathrm{id}_{\mathfrak{s u}(E)}+\vec{\tau} \cdot \overrightarrow{\mathfrak{m}}(A)\right) \rho^{-1}\left(\Phi \otimes \Phi^{*}\right)_{00}=0, \\
& \mathfrak{S}_{2}(A, \Phi):=D_{A} \Phi+\rho\left(\vartheta_{0}\right) \Phi+\vec{\vartheta} \cdot \overrightarrow{\mathfrak{m}}(A) \Phi=0,
\end{aligned}$$
where $\tau_{0} \in C^{r}\left(X, \mathfrak{g} \mathfrak{l}\left(\Lambda^{+}\right)\right)$and $\vartheta_{0} \in C^{r}\left(X, \Lambda_{\mathbb{C}}^{1}\right)$ are additional perturbation parameters. For brevity, we shall often denote $\vec{\tau}_{A}:=\vec{\tau} \cdot \overrightarrow{\mathfrak{m}}(A)$ and $\vec{\vartheta}_{A}:=\vec{\vartheta} \cdot \overrightarrow{\mathfrak{m}}(A)$.

Remark 2.25. 1. In [25] we consider the question of transversality of the spaces of reducible solutions or U(1) monopoles, which are identified with moduli spaces of Seiberg-Witten monopoles. In particular, we show that the moduli spaces of U(1) monopoles are cut out transversely for generic $\tau_{0} \in \Omega^{0}\left(\mathfrak{g l}\left(\Lambda^{+}\right)\right)$.
\begin{itemize}
\item[2.] If the section $\Phi$ is identically zero then the PU(2) monopole equations reduce to those for a projectively anti-self-dual unitary connection $A$ on $E$. If the connection $A$ is reducible then all of the sections $\mathfrak{m}_{j, l, \alpha}(A)$ are identically zero on $X$; the perturbations $\vec{\tau} \cdot \overrightarrow{\mathfrak{m}}(A)$ and $\vec{\vartheta} \cdot \overrightarrow{\mathfrak{m}}(A)$ in (2.27) are then zero.
\item[3.] We emphasize that the holonomy sections in the sequence $\overrightarrow{\mathfrak{m}}(A)$ are always $L_{k+1}^{2}$ by construction for $L_{k}^{2}$ connections $A$ (with $k \geq 2$ ) and that the sums defining $\vec{\tau} \cdot \overrightarrow{\mathfrak{m}}(A)$ and $\vec{\vartheta} \cdot \overrightarrow{\mathfrak{m}}(A)$ are always finite for each $A$, although the number of terms may tend to infinity as $A$ approaches a reducible connection.
\end{itemize}