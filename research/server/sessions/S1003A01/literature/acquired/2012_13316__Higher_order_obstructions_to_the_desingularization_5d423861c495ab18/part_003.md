---
retention_scope: session
part: 3
total_parts: 4
---

[Part 3/4 of: [2012.13316] Higher order obstructions to the desingularization of Einstein metrics]

We will need to extend higher order terms of the orbifold and ALE in order to produce a better approximation of the Einstein modulo obstructions perturbation of $g_{\zeta, v}^{D}$. We have to obtain good enough controls to "see" an obstruction of the same order as in (76).
3.3.3. Extension of the higher order terms. We then also extend the obstructions of the orbifold $\mathbf{g}_{ \pm}$to the Eguchi-Hanson metrics to ensure a good approximation. Consider the development of $\mathbf{v}_{l} \in \mathbf{O}\left(\mathbf{g}_{ \pm}\right)$at the singular point $j: \mathbf{v}_{l}=V_{j, l, 0}+V_{j, l, 2}+V_{j, l, 4}+$ $V_{j, l, 6}+\mathcal{O}\left(\left\|\mathbf{v}_{l}\right\|_{L^{2}} \cdot\left|\zeta^{ \pm}\right|^{2} r_{\mathbf{e}}^{8}\right)$, we define the extensions $\underline{\mathbf{v}_{j, l, 0}}=V_{j, l, 0}+\mathcal{O}\left(\left|\zeta^{\mp}\right|^{2} r_{\mathbf{e}}^{-4+\epsilon}\right), \underline{\mathbf{v}_{j, l, 2}}=$ $V_{j, l, 2}+\mathcal{O}\left(\left|\zeta^{ \pm}\right|^{2}\left|\zeta^{\mp}\right|^{2} r_{\mathbf{e}}^{-2+\epsilon}\right)$ and $\underline{\mathbf{v}_{j, l, 4}}=V_{j, l, 4}+\mathcal{O}\left(\left|\zeta^{\overline{ \pm}}\right|^{2}\left|\zeta^{\mp}\right|^{2} r_{\mathbf{e}}^{\epsilon}\right)$ for all $\epsilon>0$ satisfying:
$$P_{\mathbf{e h}_{\zeta_{j}}} \mathbf{v}_{j, l, l_{0}}=0,$$
where there are no obstructions by Lemma 2.7,
$$\begin{gathered}
P_{\mathbf{e h}_{\zeta_{j}}} \underline{\mathbf{v}}_{j, l, l_{2}}+Q_{\mathbf{e h}_{\zeta_{j}}}^{(2)}\left(\underline{h}_{2}, \underline{\mathbf{v}}_{j, l, l_{0}}\right) \in \mathbf{O}\left(\mathbf{e h}_{\zeta_{j}^{\mp}}\right) \text { and } \\
P_{\mathbf{e h}_{\zeta_{j}}} \underline{\mathbf{v}}_{j, l, 4}+Q_{\mathbf{e h}_{\zeta_{j}}}^{(2)}\left(\underline{h}_{j, 2}, \underline{\mathbf{v}}_{j, l, 2}\right)+Q_{\mathbf{e h}_{\zeta_{j}}}^{(2)}\left(\underline{h}_{j, 4}, \underline{\mathbf{v}}_{j, l, 0}\right)+Q_{\mathbf{e h}_{\zeta_{j}}}^{(3)}\left(\underline{h}_{j, 2}, \underline{h}_{j, 2}, \underline{\mathbf{v}}_{j, l, 0}\right) \in \mathbf{O}\left(\mathbf{e h}_{\zeta_{j}^{\mp}}\right),
\end{gathered}$$
and we will take the solutions which are orthogonal to $\mathbf{O}\left(\mathbf{e h}_{\zeta_{j}^{\mp}}\right)$ for the $L^{2}$-product on $\mathbb{S}^{2}$ induced by $\mathbf{e h}_{\zeta_{j}^{\mp}}$.

Like in the decomposition for $H_{j, 4}$, from the 2-tensor $H_{j, 6}$ of (67) there exists $\stackrel{\circ}{H}_{j, 6} \propto$ $\left|\zeta^{ \pm}\right|^{2} r_{\mathbf{e}}^{6}$ for which we have $H_{j, 6}-\stackrel{\circ}{H}_{j, 6} \propto\left|\zeta^{ \pm}\right|^{4} r_{\mathbf{e}}^{6}$, and
$$P_{\mathbf{e}} \AA_{j, 6}=0,$$
Indeed, considering the quadratic 2-tensor $H_{j, 6}$ satisfying
$$P_{\mathbf{e}} H_{j, 6}+Q_{\mathbf{e}}^{(2)}\left(H_{j, 2}, H_{j, 4}\right)+Q_{\mathbf{e}}^{(3)}\left(H_{j, 2}, H_{j, 2}, H_{j, 2}\right)=0,$$
as $\left|\zeta^{ \pm}\right| \rightarrow 0$, one finds a 2-tensor $\stackrel{\circ}{H}_{j, 6}$ satisfying (77) and $H_{j, 6}-\stackrel{\circ}{H}_{j, 6} \propto\left|\zeta^{ \pm}\right|^{4} r_{\mathbf{e}}^{6}$, since $H_{j, 2} \propto\left|\zeta^{+}\right|^{2} r_{\mathbf{e}}^{2}$ and $H_{j, 4} \propto\left|\zeta^{+}\right|^{2} r_{\mathbf{e}}^{4}$ by Lemma A. 5 in the Appendix.

Lemma 3.15. There exists a unique 2 -tensor $\underline{\underline{h}}_{j, 6}$ satisfying the following identity:
$$\left\{\begin{array}{c}
P_{\mathbf{e h}_{\zeta_{j}^{\mp}}} \stackrel{\circ}{\underline{h}}_{j, 6}-\sum_{l} \nu_{l} \underline{\mathbf{v}}_{j, l, 0}=0 \\
\stackrel{\circ}{\underline{h}}_{j, 6}=\stackrel{\circ}{H}_{j, 6}+\stackrel{\circ}{H}_{j, 6}^{4}+\mathbf{O}\left(\left|\zeta^{ \pm}\right|^{2} \cdot\left|\zeta_{j}^{\mp}\right|^{2} r_{\mathbf{e}}^{-4+\epsilon}\right) \text { for any } \epsilon>0 \\
\int_{\mathbb{S}^{2}}\left\langle\stackrel{\circ}{\underline{h}}_{j, 6}, \mathbf{o}_{j, k}\right\rangle_{\mathbf{e h}_{\zeta_{j}^{\mp}}} d v_{\mathbf{e h}_{\zeta_{j}^{\mp} \mid \mathbb{S}^{2}}}=0 \text { for all } k \in\{1,2,3\},
\end{array}\right.$$
where $\stackrel{\circ}{H}_{j, 6}^{4} \propto\left|\zeta^{ \pm}\right|^{2}\left|\zeta^{\mp}\right|^{2} r_{\mathbf{e}}^{2}$ satisfies $P_{\mathbf{e}} \stackrel{\circ}{H}_{j, 6}^{4}=-Q_{\mathbf{e}}^{(2)}\left(\stackrel{\circ}{H}_{j, 6}, H^{4}\left(\zeta_{j}^{\mp}\right)\right)+\sum_{l} \nu_{l} V_{j, l, 0}$ while the restriction of the coefficients of $\stackrel{\circ}{H}_{j, 6}^{4}$ in a basis of the covering $\mathbb{R}^{4}$, once restricted to $\mathbb{S}^{3}$ are $L^{2}\left(\mathbb{S}^{3}\right)$-orthogonal to the eigenfunctions associated to the second eigenvalue of the Laplacian on $\mathbb{S}^{3}$.

Remark 3.16. Note that $\stackrel{\circ}{H}_{j, 6}^{4}$ is different from $H_{j, 6}^{4}$ defined in (73). They are both $\propto\left|\zeta^{ \pm}\right|^{2}\left|\zeta^{\mp}\right|^{2} r_{\mathbf{e}}^{2}$, and so is their difference.

Proof. Let $\stackrel{\circ}{H}_{j, 6}$ be as in (77). The term $H_{j, 6}^{4}$ in the development (73) satisfies for all $\epsilon>0$ :
$$P_{\mathbf{e}} H_{j, 6}^{4}+Q_{\mathbf{e}}^{(2)}\left(\stackrel{\circ}{H}_{j, 6}, H^{4}\left(\zeta^{\mp}\right)\right)-\sum_{l} \nu_{l} V_{j, l, 0}=\mathcal{O}\left(\left|\zeta^{ \pm}\right|^{4}\left|\zeta^{\mp}\right|^{2} r_{\mathbf{e}}^{\epsilon}\right)$$
since we have $H_{j, 6}-\stackrel{\circ}{H}_{j, 6} \propto\left|\zeta^{ \pm}\right|^{4} r_{\mathbf{e}}^{6}, H_{j, 2} \propto\left|\zeta^{ \pm}\right|^{2} r_{\mathbf{e}}^{2}$ and $H_{j, 4} \propto\left|\zeta^{ \pm}\right|^{2} r_{\mathbf{e}}^{4}$. Thanks to Lemma A.5, we therefore find $\stackrel{\circ}{H}_{j, 6}^{4}$ with $\stackrel{\circ}{H}_{j, 6}^{4} \propto\left|\zeta^{ \pm}\right|^{2}\left|\zeta^{\mp}\right|^{2} r_{\mathbf{e}}^{2}$ satisfying
$$P_{\mathbf{e}} \stackrel{\circ}{H}_{j, 6}^{4}+Q_{\mathbf{e}}^{(2)}\left(\stackrel{\circ}{H}_{j, 6}, H^{4}\left(\zeta^{\mp}\right)\right)-\sum_{l} \nu_{l} V_{j, l, 0}=0 .$$
The 2-tensor $\stackrel{\circ}{H}_{j, 6}^{4}$ is defined by (80) up to the harmonic quadratic 2-tensors on $\mathbb{R}^{4} / \mathbb{Z}_{2}$, and we choose the unique solution such that the restriction of the coefficients of $\stackrel{\circ}{H}_{j, 6}^{4}$ in a basis of the covering $\mathbb{R}^{4}$, once restricted to $\mathbb{S}^{3}$ are $L^{2}\left(\mathbb{S}^{3}\right)$-orthogonal to the eigenfunctions associated to the second eigenvalue of the Laplacian on $\mathbb{S}^{3}$.

Without loss of generality by rescaling and by acting on $H_{j, 6}, \stackrel{\circ}{H}_{j, 6}$ and $V_{j, 0}$ by an element of $O(4) \backslash S O(4)$, we will study the existence of $\underline{\underline{h}}_{j, 6}$ and the vanishing of the associated obstructions on eh, that is, as if we had $\zeta_{j}^{ \pm}=(1,0,0)^{+}$.

Remark 3.17. This may change the orientation and in particular makes the curvature of $\stackrel{\circ}{H}_{j, 6}$ become selfdual. This will let us use the more convenient usual Eguchi-Hanson metric in our computations.

For a smooth cut-off function $\chi$ supported at the infinity of eh we have $P_{\mathbf{e h}}\left(\chi\left(\stackrel{\circ}{H}_{j, 6}+\right.\right.$ $\left.\left.\stackrel{\circ}{H}_{j, 6}^{4}\right)\right)-\sum_{l} \nu_{l} \mathbf{v}_{j, l,{ }_{0}}=\mathcal{O}\left(\left|\zeta^{ \pm}\right|^{2} r_{\mathbf{e}}^{-4}\right)$. By [Biq13, Proposition 2.1], one can find a smooth 2 -tensor $h^{\prime}$ decaying at infinity such that
$$\begin{gathered}
P_{\mathbf{e h}}\left(\chi\left(\stackrel{\circ}{H}_{j, 6}+\stackrel{\circ}{H}_{j, 6}^{4}\right)+h^{\prime}\right)-\sum_{l} \nu_{l} \mathbf{v}_{j, l, 0} \in \mathbf{O}(\mathbf{e h}), \text { with } \\
\left\|P_{\mathbf{e h}}\left(\chi\left(\stackrel{\circ}{H}_{j, 6}+\stackrel{\circ}{H}_{j, 6}^{4}\right)+h^{\prime}\right)-\sum_{l} \nu_{l} \underline{\mathbf{v}}_{j, l, 0}\right\|_{r_{\mathbf{e h}}^{-2} C_{\beta}^{\alpha}(\mathbf{e h})} \leqslant C\left|\zeta^{ \pm}\right|^{2}
\end{gathered}$$
for some $C>0$ depending on the metric eh only.
There now remains to prove that the obstruction actually vanishes. For this, again by [Biq13, Proposition 2.1], we need to prove that for all $k \in\{1,2,3\}$
$$\int_{T^{*} \mathbb{S}^{2}}\left\langle P_{\mathbf{e h}}\left(\chi\left(\stackrel{\circ}{H}_{j, 6}+\stackrel{\circ}{H}_{j, 6}^{4}\right)\right)-\sum_{l} \nu_{l} \underline{\mathbf{v}_{j, l, 0}}, \mathbf{o}_{k}\right\rangle_{\mathbf{e h}} d v_{\mathbf{e h}}=0 .$$
Let us use the formalism of [Biq16] in order to show this. Let us denote $\Omega$ the closed anti-selfdual 2-form generating of the $L^{2}$-cohomology of eh as in [Biq13, (5)]. We will need its asymptotics at infinity:
$$\begin{aligned}
\Omega & =\frac{\theta_{1}^{-}}{r^{4}}-\frac{\theta_{1}^{-}+\frac{1}{2} \omega_{1}^{+}}{r^{8}}+\mathcal{O}\left(r_{\mathbf{e}}^{-12}\right) \\
& =d\left(d^{C}\left(\frac{1}{r^{2}}\right)+\frac{\alpha_{1}}{4 r^{6}}+\mathcal{O}\left(r_{\mathbf{e}}^{-11}\right)\right)
\end{aligned}$$
where $d^{C}$ is the operator defined as $d^{C}=\frac{1}{2 i \pi}(\partial-\bar{\partial})$ in complex geometry.
As in the first Section, we use the identification of traceless 2-tensors and (commuting) compositions of a selfdual and an anti-selfdual 2-form, see Remark 1.13. We will use this on both the flat metric e for which a basis of $\Omega^{+}(\mathbf{e})$ is $\left(\omega_{k}^{+}\right)_{k \in\{1,2,3\}}$ and for the Eguchi-Hanson metric, we will use the basis $\left(\tilde{\omega}_{k}^{+}\right)_{k \in\{1,2,3\}}$ of $\Omega^{+}(\mathbf{e h})$ satisfying $\tilde{\omega}_{k}^{+}=\omega_{k}^{+}+\mathcal{O}\left(r_{\mathbf{e}}^{-4}\right)$ at infinity. We can therefore rewrite
\begin{itemize}
\item[-] $\stackrel{\circ}{H}_{j, 6}=\sum_{k} \tilde{\phi}_{j, 6}^{k} \circ \tilde{\omega}_{k}^{+}$for $\tilde{\phi}_{j, 6}^{k} \in \Omega^{-}(\mathbf{e h})$, as well as $\stackrel{\circ}{H}_{j, 6}=\sum_{k} \phi_{j, 6}^{k} \circ \omega_{k}^{+}$for $\phi_{j, 6}^{k} \in$ $\Omega^{-}(\mathbf{e})$,
\item[-] $\stackrel{\circ}{H}_{j, 6}^{4}=\sum_{k} \tilde{\phi}_{j, 6}^{4, k} \circ \tilde{\omega}_{k}^{+}$for $\tilde{\phi}_{j, 6}^{4, k} \in \Omega^{-}(\mathbf{e h})$, as well as $\stackrel{\circ}{H}_{j, 6}^{4}=\sum_{k} \phi_{j, 6}^{4, k} \circ \omega_{k}^{+}$for $\phi_{j, 6}^{4, k} \in$ $\Omega^{-}(\mathbf{e})$,
\end{itemize}
\begin{itemize}
\item[-] $\sum_{l} \nu_{l} \mathbf{v}_{j, l, 0}=\sum_{k} \tilde{V}_{j, 0}^{k} \circ \tilde{\omega}_{k}^{+}$, for $\tilde{V}_{j, 0}^{k} \in \Omega^{-}(\mathbf{e h})$ as well as $\sum_{l} \nu_{l} V_{j, l, 0}=\sum_{k} V_{j, 0}^{k} \circ \omega_{k}^{+}$, for $V_{j, 0}^{k} \in \Omega^{-}(\mathbf{e})$,
\item[-] $\mathbf{o}_{k}=\Omega \circ \tilde{\omega}_{k}^{+}$see Biq16,
\item[-] recall also that $H^{4}=-\frac{\theta_{1}^{-} \circ \omega_{1}^{+}}{2 r_{\mathrm{e}}^{4}}$.
\end{itemize}

This lets us rewrite several of the above identities:
\begin{itemize}
\item[-] the equality (77) becomes
$$\left(d_{-} d^{*}\right)_{\mathbf{e}} \phi_{j, 6}^{k}=0, \text { or equivalently }\left(d d^{*}\right)_{\mathbf{e}} \phi_{j, 6}^{k} \in \Omega^{+}(\mathbf{e})$$
\item[-] the equality (80) becomes:
$$\left(d_{-} d^{*}\right)_{\mathbf{e h}}\left(\phi_{j, 6}^{k}+\phi_{j, 6}^{4, k}\right)-\tilde{V}_{0}^{k}=\mathcal{O}\left(r_{\mathbf{e}}^{-4}\right)$$
\item[-] a direct extension of [Biq16, Lemme 3] to the computation of the bilinear terms of the selfdual part of the Riemannian curvature. Let $\phi:=\sum_{k} \phi_{k} \circ \omega_{k}^{+}$and $\psi:=$ $\sum_{k} \psi_{k} \circ \omega_{k}^{+}$be infinitesimal Ricci-flat deformations of $\mathbf{e}$ which satisfy $B_{\mathbf{e}}(\phi)=$ $B_{\mathbf{e}}(\psi)=0$. Assume additionally that $\operatorname{tr}_{\mathbf{e}} \phi=0$ and $d * d \phi_{k}=0$, then the second variation of the selfdual part of the curvature at $\mathbf{e}$ in the directions $\phi$ and $\psi$, is:
$$\mathbf{R}_{\mathbf{e}}^{+,(2)}(\phi, \psi)=-\frac{1}{2}\left[a_{\mathbf{e}}(\phi), a_{\mathbf{e}}(\psi)\right]_{+},$$
where $a_{\mathbf{e}}(\phi)$ and $a_{\mathbf{e}}(\psi)$ are respectively the first variations of the connection on the bundle of selfdual 2-forms at e in the directions $\phi$ and $\psi$. In the particular case of $\phi=H^{4}$ and $\psi=\stackrel{\circ}{H}_{j, 6}$, since $a_{\mathbf{e}}\left(H^{4}\right)=-* d\left(\frac{\theta_{1}^{-}}{2 r_{\mathbf{e}}^{4}}\right)=0$, we find
$$\mathbf{R}_{\mathbf{e}}^{+,(2)}\left(\stackrel{\circ}{H}_{j, 6}, H^{4}\right)=0 .$$
\item[-] the equalities (80) and (84) imply that in a neighborhood of infinity we have
$$\begin{aligned}
d d_{\mathbf{e h}}^{*}\left(\tilde{\phi}_{j, 6}^{k}+\tilde{\phi}_{j, 6}^{4, k}\right)-\tilde{V}_{0}^{k} & =\left(d_{+} d^{*}\right)_{\mathbf{e}} \phi_{j, 6}^{k}+\left(d_{+} d^{*}\right)_{\mathbf{e}} \phi_{j, 6}^{4, k}+\mathcal{O}\left(r_{\mathbf{e}}^{-4}\right) \\
& =-d_{\mathbf{e}} \mathbf{R}^{+}\left(\stackrel{\circ}{H}_{j, 6}\right)-d_{\mathbf{e}} \mathbf{R}^{+}\left(\stackrel{\circ}{H}_{j, 6}^{4}\right)+\mathcal{O}\left(r_{\mathbf{e}}^{-4}\right) .
\end{aligned}$$
\end{itemize}

Following the integration by parts of the proof of [Biq16. Lemma 7], since $\Omega \in \Omega^{-}(\mathbf{e h})$, by (81) and by (85), we have
$$\begin{aligned}
\frac{1}{\left\|\mathbf{o}_{k}\right\|_{L^{2}}} & \int_{T^{*} \mathbb{S}^{2}}\left\langle P_{\mathbf{e h}}\left(\chi\left(\stackrel{\circ}{H}_{j, 6}+\stackrel{\circ}{H}_{j, 6}^{4}\right)\right)-\sum_{l} \nu_{l} \mathbf{v}_{j, l, 0}, \mathbf{o}_{k}\right\rangle_{\mathbf{e h}} d v_{\mathbf{e h}} \\
= & -\frac{1}{\|\Omega\|_{L^{2}}} \int_{T^{*} \mathbb{S}^{2}} \Omega \wedge\left(d d_{\mathbf{e h}}^{*}\left(\tilde{\phi}_{j, 6}^{k}+\tilde{\phi}_{j, 6}^{4, k}\right)-\tilde{V}_{0}^{k}\right) \\
= & -\frac{1}{\|\Omega\|_{L^{2}}} \int_{T^{*} \mathbb{S}^{2}} d\left(d^{C}\left(\frac{1}{r_{\mathbf{e}}^{2}}\right)+\frac{\alpha_{1}}{4 r_{\mathbf{e}}^{6}}+\mathcal{O}\left(r_{\mathbf{e}}^{-11}\right)\right) \wedge\left(d d_{\mathbf{e h}}^{*}\left(\tilde{\phi}_{j, 6}^{k}+\tilde{\phi}_{j, 6}^{4, k}\right)-\tilde{V}_{0}^{k}\right) \\
= & -\frac{1}{\|\Omega\|_{L^{2}}} \lim _{r \rightarrow+\infty} \int_{\left\{r_{\mathbf{e}}=r\right\}}\left(d^{C}\left(\frac{1}{r_{\mathbf{e}}^{2}}\right)+\frac{\alpha_{1}}{4 r_{\mathbf{e}}^{6}}\right) \wedge\left(\left(d_{+} d^{*}\right)_{\mathbf{e}} \phi_{j, 6}^{k}+\left(d_{+} d^{*}\right)_{\mathbf{e}} \phi_{j, 6}^{4, k}\right) \\
= & +\frac{1}{\|\Omega\|_{L^{2}}} \lim _{r \rightarrow+\infty} r^{4} \int_{\left\{r_{\mathbf{e}}=1\right\}} d^{C}\left(\frac{1}{r_{\mathbf{e}}^{2}}\right) \wedge d_{\mathbf{e}} \mathbf{R}^{+}\left(\dot{H}_{j, 6}\right)\left(\omega_{k}^{+}\right) \\
& +\frac{1}{\|\Omega\|_{L^{2}}} \lim _{r \rightarrow+\infty} \int_{\left\{r_{\mathbf{e}}=1\right\}} \frac{\alpha_{1}}{4 r_{\mathbf{e}}^{6}} \wedge d_{\mathbf{e}} \mathbf{R}^{+}\left(\stackrel{\circ}{H}_{j, 6}\right)\left(\omega_{k}^{+}\right) \\
& +\frac{1}{\|\Omega\|_{L^{2}}} \lim _{r \rightarrow+\infty} \int_{\left\{r_{\mathbf{e}}=1\right\}} d^{C}\left(\frac{1}{r_{\mathbf{e}}^{2}}\right) \wedge d_{\mathbf{e}} \mathbf{R}^{+}\left(\dot{H}_{j, 6}^{4}\right)\left(\omega_{k}^{+}\right)
\end{aligned}$$

Now, the coefficients of $d_{\mathbf{e}} \mathbf{R}^{+}\left(\stackrel{\circ}{H}_{j, 6}\right)\left(\omega_{k}^{+}\right)$are harmonic functions in $r_{\mathbf{e}}^{4}$ and their restrictions to a sphere $\left\{r_{\mathbf{e}}=r\right\}=r \cdot \mathbb{S}^{3} / \mathbb{Z}_{2}$ are eigenfunctions of the Laplacian associated
to the second eigenvalue on $\mathbb{S}^{3} / \mathbb{Z}_{2}$ (fourth eigenvalue on $\mathbb{S}^{3}$ ). They are therefore $L^{2}\left(\mathbb{S}^{3} /\right.$ $\mathbb{Z}_{2}$ )-orthogonal to the coefficients of the restriction of $d^{C}\left(\frac{1}{r_{\mathbf{e}}^{2}}\right)$ or $\frac{\alpha_{1}}{4 r_{\mathbf{e}}^{6}}$ to $\mathbb{S}^{3} / \mathbb{Z}_{2}$.

Similarly, by the two formulas of [Biq13, Proposition 2.1] and [Biq16, Lemme 7], we know that $\int_{\left\{r_{\mathbf{e}}=r\right\}} d^{C}\left(\frac{1}{r_{\mathbf{e}}^{2}}\right) \wedge d_{\mathbf{e}} \mathbf{R}^{+}\left(\stackrel{\circ}{H}_{j, 6}^{4}\right)\left(\omega_{k}^{+}\right)$is proportional to $\int_{\mathbb{S}^{3} / \mathbb{Z}_{2}}\left\langle\stackrel{\circ}{H}_{j, 6}^{4}, O_{k}^{4}\right\rangle d v_{\mathbb{S}^{3} / \mathbb{Z}_{2}}$, where $O_{k}^{4}$ is explicited in (14) and once restricted to a sphere $\left\{r_{\mathbf{e}}=r\right\}, O_{k}^{4}$ has eigenfunctions of the Laplacian on $\mathbb{S}^{3} / \mathbb{Z}_{2}$ associated to the first eigenvalue as coefficients. By construction, $\stackrel{\circ}{H}_{j, 6}^{4}$ is orthogonal to this eigenspace. The obstructions therefore vanish. \(\square\)

We then extend the next term of the development of $\mathbf{o}_{m}$, for $m \in\{1,2,3\}$ to the orbifold. Recall that $\mathbf{o}_{j, m}=O_{j, m}^{4}+O_{j, m}^{8}+\mathcal{O}\left(|\zeta|^{5} r_{\mathbf{e}}^{-12}\right)$, with $O_{j, m}^{4} \propto\left|\zeta^{\mp}\right| r_{\mathbf{e}}^{-4}$ and $O_{j, m}^{8} \propto\left|\zeta^{\mp}\right|^{3} r_{\mathbf{e}}^{-8}$. We can therefore find by the general method of [Biq13, Section 10] $\overline{\mathbf{o}}_{j, m}^{8}$ satisfying
$$\left\{\begin{array}{l}
P_{\mathbf{g}_{ \pm}} \overline{\mathbf{o}}_{j, m}^{8}+Q_{\mathbf{g}_{ \pm}}^{(2)}\left(\overline{\mathbf{o}}_{j, m}^{4}, \overline{\mathbf{o}}_{j, m}^{4}\right)+Q_{\mathbf{g}_{ \pm}}^{(2)}\left(\overline{\mathbf{o}}_{j, m}^{4}, \bar{h}^{4}\right) \in \mathbf{O}\left(\mathbf{g}_{ \pm}\right) \\
\quad \overline{\mathbf{o}}_{j, m}^{8}=O_{m}^{8}\left(\zeta_{j}^{\mp}\right)+\mathcal{O}\left(\left|\zeta^{ \pm}\right|^{2}\left|\zeta^{\mp}\right|^{4} r_{\mathbf{e}}^{-6-\epsilon}\right) \text { for any } \epsilon>0 \text { at the point } j \\
\quad \overline{\mathbf{o}}_{j, k}^{8} \perp \mathbf{O}\left(\mathbf{g}_{o}\right) .
\end{array}\right.$$
We then need to come back to the orbifold in order to find:
$$\left\{\begin{array}{l}
P_{\mathbf{g}_{ \pm}} \bar{h}^{8}+Q_{\mathbf{g}_{ \pm}}^{(2)}\left(\bar{h}^{4}, \bar{h}^{4}\right)-\sum_{k} \lambda_{k}^{j} \overline{\mathbf{o}}_{j, m}^{8} \in \mathbf{O}\left(\mathbf{g}_{ \pm}\right) \\
\quad \bar{h}^{8}=H^{8}\left(\zeta_{j}^{\mp}\right)+H_{j, 2}^{8}+H_{j, 4}^{8}+\stackrel{\circ}{H}_{j, 6}^{8}+\stackrel{\circ}{H}_{j, 8}^{8}+\mathcal{O}\left(\left|\zeta^{ \pm}\right|^{2}\left|\zeta^{\mp}\right|^{4} r_{\mathbf{e}}^{-2-\epsilon}\right), \forall \epsilon>0 \text { at } j \\
\quad \bar{h}^{8} \perp \mathbf{O}\left(\mathbf{g}_{o}\right)
\end{array}\right.$$
with $H^{8}\left(\zeta_{j}^{\mp}\right), H_{2}^{8}, H_{4}^{8}$ and $\stackrel{\circ}{H}_{6}^{8}$ from (67), (70), and the asymptotic terms of (75) and (78) and $\stackrel{\circ}{H}_{j, 8}^{8} \propto\left|\zeta^{ \pm}\right|^{2}\left|\zeta^{\mp}\right|^{4}$. We moreover have a converging development
$$\bar{h}^{8}=H^{8}\left(\zeta_{j}^{\mp}\right)+H_{j, 2}^{8}+H_{j, 4}^{8}+\stackrel{\circ}{H}_{j, 6}^{8}+\stackrel{\circ}{H}_{j, 8}^{8}+\sum_{m \geqslant 5} H_{j, 2 m}^{8}$$
with $H_{j, 2 m}^{8} \propto\left|\zeta^{ \pm}\right|^{2}\left|\zeta^{\mp}\right|^{4} r_{\mathbf{e}}^{2 m-8}$ in a neighborhood of $j$. We moreover have the control
$$\left\|P_{\mathbf{g}_{ \pm}} \bar{h}^{8}+Q_{\mathbf{g}_{ \pm}}^{(2)}\left(\bar{h}^{4}, \bar{h}^{4}\right)-\sum_{k} \lambda_{k}^{j} \overline{\mathbf{o}}_{j, m}^{8}\right\|_{L^{2}\left(\mathbf{g}_{ \pm}\right)}=\mathcal{O}\left(\left|\zeta^{ \pm}\right|^{2} \cdot\left|\zeta_{j}^{\mp}\right|^{4}\right)$$
which will be sufficient on the orbifold.
As for $\stackrel{\circ}{H}_{j, 6}$ defined in (77) from $H_{j, 6}$, one finds $\stackrel{\circ}{H}_{j, 8}$ from $H_{j, 8}$ of (67). More precisely, we have $H_{j, 8}-\stackrel{\circ}{H}_{j, 8} \propto\left|\zeta^{ \pm}\right|^{4} r_{\mathbf{e}}^{8}$ where $\stackrel{\circ}{H}_{j, 8} \propto\left|\zeta^{ \pm}\right|^{2} r_{\mathbf{e}}^{8}$ satisfies $P_{\mathbf{e}} \stackrel{\circ}{H}_{j, 8}=\sum_{l} \nu_{l} V_{j, l, 2}$.

As in Lemma 3.15, we prove that one can extend $\stackrel{\circ}{H}_{j, 8}$ on $\mathbf{e h}_{\zeta_{j}^{\mp}}$ without obstruction.
Lemma 3.18. There exists a unique 2-tensor $\stackrel{\circ}{\underline{h}}_{j, 8}$ satisfying the following identity:
$$\left\{\begin{array}{c}
P_{\mathbf{e h}_{\zeta_{j}^{\mp}}} \stackrel{\circ}{\underline{h}}_{j, 8}-\sum_{l} \nu_{l} \underline{\mathbf{v}}_{j, l, 2}=0 \\
\stackrel{\circ}{\underline{h}}_{j, 8}=\stackrel{\circ}{H}_{j, 8}+\stackrel{\circ}{H}_{j, 8}^{4}+\stackrel{\circ}{H}_{j, 8}^{8}+\mathcal{O}\left(\left|\zeta^{ \pm}\right|^{2} \cdot\left|\zeta_{j}^{\mp}\right|^{2} r_{\mathbf{e}}^{-6+\epsilon}\right) \text { for any } \epsilon>0 \\
\int_{\mathbb{S}^{2}}\left\langle\stackrel{\circ}{\underline{h}}_{j, 8}, \mathbf{o}_{j, k}\right\rangle_{\mathbf{e h}_{\zeta_{j}^{\mp}}} d v_{\mathbf{e h}_{\zeta_{j}^{\mp} \mid \mathbb{S}^{2}}}=0 \text { for all } k \in\{1,2,3\},
\end{array}\right.$$
where $\stackrel{\circ}{H}_{j, 8}^{4} \propto\left|\zeta^{ \pm}\right|^{2}\left|\zeta^{\mp}\right|^{2} r_{\mathbf{e}}^{4}$ satisfies $P_{\mathbf{e}} \stackrel{\circ}{H}_{j, 8}^{4}=-Q_{\mathbf{e}}^{(2)}\left(\stackrel{\circ}{H}_{j, 8}, H^{4}\left(\zeta_{j}^{\mp}\right)\right)+\sum_{l} \nu_{l} V_{j, l, 2}$, and where $\stackrel{\circ}{H}_{j, 8}^{8} \propto\left|\zeta^{ \pm}\right|^{2}\left|\zeta^{\mp}\right|^{4}$ satisfies
$$P_{\mathbf{e}} \stackrel{\circ}{H}_{j, 8}^{8}=-Q_{\mathbf{e}}^{(2)}\left(\stackrel{\circ}{H}_{j, 8}, H^{8}\left(\zeta_{j}^{\mp}\right)\right)-Q_{\mathbf{e}}^{(2)}\left(\stackrel{\circ}{H}_{j, 8}, H^{4}\left(\zeta_{j}^{\mp}\right), H^{4}\left(\zeta_{j}^{\mp}\right)\right)+\sum_{l} \nu_{l} V_{j, l, 2}^{4}$$
for $V_{j, l, 2}^{4}$ defined by $\underline{\mathbf{v}_{j, l, 2}}=V_{j, l, 2}+V_{j, l, 2}^{4}+o\left(\left|\zeta^{ \pm}\right|^{2}\left|\zeta^{\mp}\right|^{4} r_{\mathbf{e}}^{-6}\right)$

Proof．The proof of the existence of $\underline{⿱ ⺊ 口}_{j, 8}$ satisfying
$$\left\{\begin{array}{c}
P_{\mathbf{e h}_{\zeta_{j}^{\mp}}}^{\stackrel{\circ}{h}_{j, 8}}-\sum_{l} \nu_{l} \mathbf{v}_{j, l, l_{2}} \in \mathbf{O}(\mathbf{e h}) \\
\stackrel{\circ}{h}_{j, 8}=\stackrel{\circ}{H}_{j, 8}+\stackrel{\circ}{H}_{j, 8}^{4}+\stackrel{\circ}{H}_{j, 8}^{8}+\mathcal{O}\left(\left|\zeta^{ \pm}\right|^{2} \cdot\left|\zeta_{j}^{\mp}\right|^{6} r_{\mathbf{e}}^{-6+\epsilon}\right) \text { for any } \epsilon>0 \\
\int_{\mathbb{S}^{2}}\left\langle\stackrel{\circ}{h}_{j, 8}, \mathbf{o}_{j, k}\right\rangle_{\mathbf{e h}_{\zeta_{j}^{\mp}}} d v_{\mathbf{e h}_{\zeta_{j}^{\mp} \mid \mathbf{S}^{2}}}=0 \text { for all } k \in\{1,2,3\},
\end{array}\right.$$
is very similar to that of $\stackrel{\circ}{h}_{j, 6}$ of Lemma 3.15 once $\stackrel{\circ}{H}_{j, 8}^{4}$ and $\stackrel{\circ}{H}_{j, 8}^{8}$ are identified like $\stackrel{\circ}{H}_{j, 6}^{4}$ is in Lemma 3．15．We will therefore omit the proof．

Let us focus on showing that the obstructions vanish．Again，after rescaling and act－ ing by a rotation in $O(4) \backslash S O(4)$ ，we will work on the usual metric eh．Mimicking the computation of（86），and dropping the terms not contributing to the boundary term，we find
$$\begin{aligned}
\left\langle P_{\mathbf{e h}}\left(\chi\left(\stackrel{\circ}{H}_{j, 8}+\stackrel{\circ}{H}_{j, 8}^{4}+\stackrel{\circ}{H}_{j, 8}^{8}\right)\right)\right. & \left.-\sum_{l} \nu_{l} \underline{\mathbf{v}_{j, l, 2}}, \mathbf{o}_{k}\right\rangle \\
= & \lim _{r \rightarrow+\infty}\left(\int_{\left\{r_{\mathbf{e}}=r\right\}}\left(d^{C}\left(\frac{1}{r_{\mathbf{e}}^{2}}\right)+\frac{\alpha_{1}}{4 r_{\mathbf{e}}^{6}}\right) \wedge d_{\mathbf{e}} \mathbf{R}^{+}\left(\stackrel{\circ}{H}_{j, 8}\right)\left(\omega_{k}^{+}\right)\right. \\
& \left.\quad+\int_{\left\{r_{\mathbf{e}}=r\right\}} d^{C}\left(\frac{1}{r_{\mathbf{e}}^{2}}\right) \wedge d_{\mathbf{e}} \mathbf{R}^{+}\left(\stackrel{\circ}{H}_{j, 8}^{4}\right)\left(\omega_{k}^{+}\right)\right) \\
= & \lim _{r \rightarrow+\infty}\left(r^{6} \int_{\left\{r_{\mathbf{e}}=1\right\}} d^{C}\left(\frac{1}{r_{\mathbf{e}}^{2}}\right) \wedge d_{\mathbf{e}} \mathbf{R}^{+}\left(\stackrel{\circ}{H}_{j, 8}\right)\left(\omega_{k}^{+}\right)\right. \\
& \quad+r^{2} \int_{\left\{r_{\mathbf{e}}=1\right\}} \frac{\alpha_{1}}{4 r_{\mathbf{e}}^{6}} \wedge d_{\mathbf{e}} \mathbf{R}^{+}\left(\stackrel{\circ}{H}_{j, 8}\right)\left(\omega_{k}^{+}\right) \\
& \left.\quad+r^{2} \int_{\left\{r_{\mathbf{e}}=1\right\}} d^{C}\left(\frac{1}{r_{\mathbf{e}}^{2}}\right) \wedge d_{\mathbf{e}} \mathbf{R}^{+}\left(\stackrel{\circ}{H}_{j, 8}^{4}\right)\left(\omega_{k}^{+}\right)\right)
\end{aligned}$$
because of the homogeneity of each term：
\begin{itemize}
\item[] －$d^{C}\left(\frac{1}{r_{\mathrm{e}}^{2}}\right) \propto r_{\mathrm{e}}^{-3}$ ，
\item[] －$\frac{\alpha_{1}}{4 r_{\mathrm{e}}^{6}} \propto r_{\mathrm{e}}^{-7}$
\item[] －$d_{\mathbf{e}} \mathbf{R}^{+}\left(\stackrel{\circ}{H}_{j, 8}\right)\left(\omega_{k}^{+}\right) \propto\left|\zeta^{ \pm}\right|^{2} r_{\mathbf{e}}^{6}$
\item[] －$d_{\mathbf{e}} \mathbf{R}^{+}\left(\stackrel{\circ}{H}_{j, 8}^{4}\right)\left(\omega_{k}^{+}\right) \propto\left|\zeta^{ \pm}\right|^{2}\left|\zeta^{\mp}\right|^{2} r_{\mathbf{e}}^{2}$ ．
\end{itemize}
We see that the obstruction either vanishes or is infinite．However $\left\langle P_{\mathbf{e h}}\left(\chi\left(\stackrel{\circ}{H}_{j, 8}+\stackrel{\circ}{H}_{j, 8}^{4}+\right.\right.\right.$ $\left.\left.\left.\stackrel{\circ}{H}_{j, 8}^{8}\right)\right)-\sum_{l} \nu_{l} \underline{\mathbf{v}_{j, l, 2}}, \mathbf{\mathbf { o } _ { k }}\right\rangle$ is finite because both $P_{\mathbf{e h}}\left(\chi\left(\stackrel{\circ}{H}_{j, 8}+\stackrel{\circ}{H}_{j, 8}^{4}+\stackrel{\circ}{H}_{j, 8}^{8}\right)\right)-\sum_{l} \nu_{l} \mathbf{\mathbf { v }}_{j, l, 2}$ and $\mathbf{o}_{k}$ are in $L^{2}(\mathbf{e h})$ ．The obstruction therefore necessarily vanishes． \(\square\)

Similarly，there exists $\stackrel{\circ}{h}_{j, 10}$ satisfying：for $\stackrel{\circ}{H}_{j, 10}$ the harmonic part of $H_{j, 10}$ from（67） and $\stackrel{\circ}{H}_{j, 10}^{4}$ and $\stackrel{\circ}{H}_{j, 10}^{8}$ associated from the development of $\bar{h}^{4}$ of（72）and $\bar{h}^{8}$ of（88）：
$$\left\{\begin{array}{c}
P_{\mathbf{e h}_{\zeta_{j}^{\mp}} \stackrel{\circ}{h}_{j, 10}}-\sum_{l} \nu_{l} \underline{\mathbf{v}}_{j, l_{4}} \in \mathbf{O}\left(\mathbf{e h}_{\zeta_{j}^{\mp}}\right) \\
\stackrel{\circ}{\underline{h}}_{j, 10}=\stackrel{\circ}{H}_{j, 10}+\stackrel{\circ}{H}_{j, 10}^{4}+\stackrel{\circ}{H}_{j, 10}^{8}+\mathbf{O}\left(\left|\zeta^{ \pm}\right|^{2} \cdot\left|\zeta_{j}^{\mp}\right|^{6} r_{\mathbf{e}}^{-2+\epsilon}\right) \text { for any } \epsilon>0 \\
\int_{\mathbb{S}^{2}}\left\langle\stackrel{\circ}{h}_{j, 10}, \mathbf{o}_{j, k}\right\rangle_{\mathbf{e h}_{\zeta_{j}^{\mp}}} d v_{\mathbf{e h}_{\zeta_{j}^{\mp} \mid \mathbf{s}^{2}}}=0 \text { for all } k \in\{1,2,3\},
\end{array}\right.$$
$$\text { with }\left\|P_{\mathbf{e h}}{ }_{\zeta_{j}^{\mp}} \stackrel{\circ}{\underline{h}}_{j, 10}-\sum_{l} \nu_{l} \underline{\mathbf{v}}_{j, l}\right\|_{L^{2}\left(\mathbf{e h}_{\zeta_{j}^{\mp}}\right)}=\mathcal{O}\left(\left|\zeta^{ \pm}\right|^{2}\left|\zeta^{\mp}\right|^{5}\right) .$$

Remark 3.19. The obstruction may not vanish here, but it is small enough for our present purpose: it is better than $\mu_{1} \sim\left|\zeta^{ \pm}\right|^{4}\left|\zeta^{\mp}\right|^{2}$ when $\zeta^{ \pm} \sim \zeta^{\mp}$ as for transverse or nondegenerate desingularizations.

Let us define
$$\mathbf{e h}_{\zeta_{j}^{\mp}}^{[10]}:=\mathbf{e h}_{\zeta_{j}^{\mp}}+\underline{h}_{j, 2}+\underline{h}_{j, 4}+\sum_{m=3}^{5} \stackrel{\circ}{\underline{h}}_{j, 2 m}$$
which is a metric for $r_{\mathbf{e}} \ll 1$, and
$$\mathbf{g}_{ \pm}^{[8]}:=\mathbf{g}_{ \pm}+\bar{h}^{4}+\bar{h}^{8}$$
which is a metric for $\left|\zeta_{j}\right|^{\frac{1}{2}} \ll r_{\mathbf{e}}$. On the region where $\left|\zeta_{j}\right|^{\frac{1}{2}} \ll r_{\mathbf{e}} \ll 1$, we have
$$r_{\mathbf{e}}^{k}\left|\nabla^{k}\left(\mathbf{e h}_{\zeta_{j}^{\mp}}^{[10]}-\mathbf{g}_{ \pm}^{[8]}\right)\right| \leqslant C\left(\left|\zeta^{ \pm}\right|^{2} r_{\mathbf{e}}^{12}+\left|\zeta_{j}^{\mp}\right|^{6} r_{\mathbf{e}}^{-12}+\left|\zeta^{ \pm}\right|^{2}\left|\zeta_{j}^{\mp}\right|^{2} r^{2}\right),$$
which is minimized at $r_{\mathbf{e}}=\left|\zeta^{ \pm}\right|^{-\frac{1}{12}} \cdot\left|\zeta_{j}^{\mp}\right|^{\frac{1}{4}}$, in a neighborhood of the singular point $j$.
Proof of Proposition 3.14. We define an approximate desingularization $g_{L, \zeta}^{A}$ as the gluing of $\mathbf{e h}_{\zeta_{j}^{\mp}}^{[10]}$ to $\mathbf{g}_{ \pm}^{[8]}$ at the singular point $j$ and with a gluing scale at $\left|\zeta^{ \pm}\right|^{-\frac{1}{12}} \cdot\left|\zeta_{j}^{\mp}\right|^{\frac{1}{4}}<r_{\mathbf{e}}<$ $2\left|\zeta^{ \pm}\right|^{-\frac{1}{12}} \cdot\left|\zeta_{j}^{\mp}\right|^{\frac{1}{4}}$. As in Definition 2.16, we will denote $\tilde{\mathbf{O}}\left(g_{L, \zeta}^{A}\right)$ the space of the infinitesimal deformations of $\left(L, \zeta_{i}^{ \pm}, \zeta_{j}^{\mp}\right) \mapsto g_{L, \zeta}^{A}$.

Remark 3.20. The space $\tilde{\mathbf{O}}\left(g_{L, \zeta}^{A}\right)$ is different from the space $\tilde{\mathbf{O}}\left(g^{D}\right)$ of Ozu19b but yields better estimates. The results of [Ozu19b] with $\tilde{\mathbf{O}}\left(g^{D}\right)$ therefore hold with $\tilde{\mathbf{O}}\left(g_{L, \zeta}^{A}\right)$.

Denote $\mathbf{o}_{L, \zeta}^{A}$ as the element of $\tilde{\mathbf{O}}\left(g_{L, \zeta}^{A}\right)$ associated to the same variations of $L$ and the $\zeta_{i}^{ \pm}$as $\sum_{l} \nu_{l} \mathbf{v}_{l}(L, \zeta) \in \mathbf{O}\left(\mathbf{g}_{ \pm}\right)$defined in (72), and to the variations of each $\zeta_{j}^{\mp}$ associated to $\sum_{k}\left(\lambda_{k}^{j}(L, \zeta)+\mu_{k}^{j}(L, \zeta)\right) \mathbf{o}_{j, k}$. From the construction of the $\mathbf{e h}_{\zeta_{j}^{\mp}}^{[10]}$ and $\mathbf{g}_{ \pm}^{[8]}$ we find:
\begin{itemize}
\item[(1)] on the region where $g_{L, \zeta}^{A}=\mathbf{e h}_{\zeta_{j}^{\mp}}+\underline{h}_{j, 2}+\underline{h}_{j, 4}+\sum_{m=3}^{5} \stackrel{\circ}{\underline{h}}_{j, 2 m}$, we have:
$$\begin{aligned}
(\operatorname{Ric}-\Lambda)\left(g_{L, \zeta}^{A}\right)= & \sum_{k}\left(\lambda_{k}^{j}+\mu_{k}^{j}+\mathcal{O}\left(\left|\zeta^{ \pm}\right|^{2}\left|\zeta^{\mp}\right|^{5}\right)\right) \mathbf{o}_{j, k} \\
& +\sum_{l}\left(\nu_{l}+\mathcal{O}\left(\left|\zeta^{ \pm}\right|^{2}\left|\zeta^{\mp}\right|^{4}\right)\right)\left(\underline{\mathbf{v}_{j, l, 0}}+\underline{\mathbf{v}_{j, l, 2}}+\underline{\mathbf{v}_{j, l, 4}}\right) \\
& +\mathcal{O}\left(\left|\zeta^{ \pm}\right|^{4} r_{\mathbf{e}}^{4}+\left|\zeta^{ \pm}\right|^{2} r_{\mathbf{e}}^{10}\right),
\end{aligned}$$
\item[(2)] on the region where $g_{L, \zeta}^{A}=\mathbf{g}_{ \pm}+\bar{h}^{4}+\bar{h}^{8}$, we have:
$$\begin{aligned}
(\operatorname{Ric}-\Lambda)\left(g_{L, \zeta}^{A}\right)= & \sum_{k}\left(\lambda_{k}^{j}+\mu_{k}^{j}+\mathcal{O}\left(\left|\zeta^{ \pm}\right|^{2}\left|\zeta^{\mp}\right|^{5}\right)\right)\left(\overline{\mathbf{o}}_{j, k}^{4}+\overline{\mathbf{o}}_{j, k}^{8}\right) \\
& +\sum_{l}\left(\nu_{l}+\mathcal{O}\left(\left|\zeta^{ \pm}\right|^{2}\left|\zeta^{\mp}\right|^{4}\right)\right) \mathbf{v}_{l} \\
& +\mathcal{O}\left(\left|\zeta^{\mp}\right|^{6} r_{\mathbf{e}}^{-14}\right)
\end{aligned}$$
\end{itemize}
\begin{itemize}
\item[(3)] on the gluing region at $j$, we find:
$$\begin{aligned}
(\operatorname{Ric}-\Lambda)\left(g_{L, \zeta}^{A}\right)= & \sum_{k}\left(\lambda_{k}^{j}+\mu_{k}^{j}+\mathcal{O}\left(\left|\zeta^{ \pm}\right|^{2}\left|\zeta^{\mp}\right|^{5}\right)\right) \mathbf{o}_{j, k} \\
& +\sum_{l}\left(\nu_{l}+\mathcal{O}\left(\left|\zeta^{ \pm}\right|^{2}\left|\zeta^{\mp}\right|^{4}\right)\right) \mathbf{v}_{l} \\
& +\mathcal{O}\left(\left|\zeta^{ \pm}\right|^{4} r_{\mathbf{e}}^{4}+\left|\zeta^{ \pm}\right|^{2} r_{\mathbf{e}}^{10}+\left|\zeta^{\mp}\right|^{6} r_{\mathbf{e}}^{-14}\right) .
\end{aligned}$$
\end{itemize}

Let us finally mention the controls on the elements of $\tilde{\mathbf{O}}\left(g_{L, \zeta}^{A}\right)$ which let us conclude. Recall that for $\zeta_{j,(k)} \in \Omega^{\mp}$, we have $\mathbf{o}_{j, k}=\partial_{\zeta_{j,(k)}} \mathbf{e h}_{\zeta_{j}^{\mp}}$, and consider $\mathbf{v}_{l}$ one of the elements of the orthonormal basis of $\mathbf{O}\left(\mathbf{g}_{o}\right)$. On the region where $g_{L, \zeta}^{A}=\mathbf{e h}_{\zeta_{j}^{\mp}}^{[10]}$, where $r_{D}<$ $\left|\zeta^{ \pm}\right|^{-\frac{1}{12}} \cdot\left|\zeta_{j}^{\mp}\right|^{\frac{1}{4}}: r_{D}^{2}\left|\partial_{\zeta_{j,(k)}} g_{L, \zeta}^{A}-\mathbf{o}_{j, k}\right|_{\mathbf{e h}_{\zeta_{\mathbf{j}}^{\mp}}} \leqslant C\left|\zeta^{ \pm}\right|^{2}\left|\zeta^{\mp}\right|^{2} r_{D}^{-2}$, on the region where $g_{L, \zeta}^{A}=\mathbf{g}_{ \pm}^{[8]}$, where $r_{D}>2\left|\zeta^{ \pm}\right|^{-\frac{1}{12}} \cdot\left|\zeta_{j}^{\mp}\right|^{\frac{1}{4}}$
$$r_{D}^{2}\left|\partial_{\zeta_{j,(k)}} g_{L, \zeta}^{A}-\left(\overline{\mathbf{o}}_{j, k}^{4}+\overline{\mathbf{o}}_{j, k}^{8}\right)\right|_{\mathbf{g}_{ \pm}}<C\left(\left|\zeta^{ \pm}\right|^{6} r_{D}^{-12}+\left|\zeta^{ \pm}\right|^{2}\left|\zeta^{\mp}\right|^{2} r_{D}^{-2}\right) .$$
We have similar controls between $\partial_{\mathbf{v}_{l}} g_{L, \zeta}^{A}$ and $\mathbf{v}_{l}$ where $g_{L, \zeta}^{A}=\mathbf{g}_{ \pm}^{[8]}$ and between $\partial_{\mathbf{v}_{l}} g_{L, \zeta}^{A}$ and $\underline{\mathbf{v}_{j, l, 0}}+\underline{\mathbf{v}_{j, l, 2}}+\underline{\mathbf{v}_{j, l, 4}}$ where $g_{L, \zeta}^{A}=\mathbf{e h}_{\zeta_{j}^{\mp}}^{[10]}$.

As a consequence, using the fact that on the gluing region where $\left|\zeta^{ \pm}\right|^{-\frac{1}{12}}\left|\zeta_{j}^{\mp}\right|^{\frac{1}{4}} \leqslant r_{D} \leqslant$ $\left|\zeta^{ \pm}\right|^{-\frac{1}{12}} \cdot\left|\zeta_{j}^{\mp}\right|^{\frac{1}{4}}$, the difference between the metrics is controlled by (95) we globally find
$$\left\|\mathbf{\Phi}_{g_{L, \zeta}^{A}}\left(g_{L, \zeta}^{A}\right)-\mathbf{o}_{L, \zeta}^{A}\right\|_{r_{D}^{-2} C_{\beta}^{\alpha}} \leqslant C\left|\zeta^{ \pm}\right|^{1+\frac{\beta}{12}}\left|\zeta^{\mp}\right|^{3-\frac{\beta}{4}} .$$
which proves the statement of Proposition 3.14. \(\square\)
3.3.4. Controls on the approximate Einstein modulo obstructions metric. By [Ozu19b], we can always solve the Einstein equation modulo obstructions.

Definition 3.21 (Total Einstein modulo obstructions desingularization $\hat{g}_{L, \zeta}$ ). For $L \in$ $G L(4, \mathbb{R})$, and $\zeta$ small enough depending on $L$ (as determined in [Ozu19b]), we define $\hat{g}_{L, \zeta}$ as the unique metric satisfying for some $\epsilon=\epsilon(L)>0$ independent on $\zeta$ determined in [Ozu19b]:
\begin{itemize}
\item[-] $\left\|\hat{g}_{L, \zeta}-g_{L, \zeta}^{A}\right\|_{C_{\beta, *}^{2, \alpha}\left(g_{L, \zeta}^{A}\right)}<\epsilon$,
\item[-] $\boldsymbol{\Phi}_{g_{L, \zeta}^{A}}\left(\hat{g}_{L, \zeta}\right) \in \tilde{\mathbf{O}}\left(g_{L, \zeta}^{A}\right)$, and
\item[-] $\hat{g}_{L, \zeta}-g_{L, \zeta}^{A}$ is $L^{2}\left(g_{L, \zeta}^{A}\right)$-orthogonal to $\tilde{\mathbf{O}}\left(g_{L, \zeta}^{A}\right)$.
\end{itemize}

First, we have a good control on the projection on $\tilde{\mathbf{O}}\left(g_{L, \zeta}^{A}\right)$. The proof is analogous to the proof of Lemma 2.18 above so we omit it, compare also with Biq13, Lemma 13.2].

Lemma 3.22. Let $h$ be a symmetric 2-tensor on $M$, and let $\mathbf{o}^{A} \in \tilde{\mathbf{O}}\left(g_{L, \zeta}^{A}\right)$, then we have the following estimate, there exists $C>0$ such that
$$\left|\left\langle P_{g_{L, \zeta}^{D}} h, \mathbf{o}^{A}\right\rangle_{L^{2}\left(g_{L, \zeta}^{D}\right)}\right| \leqslant C\left|\zeta^{ \pm}\right|^{2}\left|\zeta^{\mp}\right|^{1-\frac{\beta}{2}}\|h\|_{C_{\beta, *}^{0}}\left\|\mathbf{o}^{A}\right\|_{L^{2}} .$$ \(\square\)

Replacing the control [Ozu20t, (4.46), Lemma 4.46] by the above Lemma 3.22 in the proof of [Ozu20t, Proposition 5.1], we get the following statement as a direct consequence.

Lemma 3.23. There exists $\epsilon>0$ and $C>0$ such that we have
$$\left\|\hat{g}_{L, \zeta}-g_{L, \zeta}^{A}\right\|_{C_{\beta, *}^{2, \alpha}\left(g_{L, \zeta}^{A}\right)} \leqslant C\left\|\mathbf{\Phi}_{g_{L, \zeta}^{A}}\left(g_{L, \zeta}^{A}\right)-\mathbf{o}_{L, \zeta}^{A}\right\|_{r_{D}^{-2} C_{\beta}^{\alpha}\left(g_{L, \zeta}^{A}\right)},$$
and moreover if the metric $\left(M, \hat{g}_{L, \zeta}\right)$ is an Einstein metric, then, we have
$$\begin{aligned}
\left\|\mathbf{o}_{L, \zeta}^{A}\right\|_{L^{2}\left(g_{L, \zeta}^{A}\right)} \leqslant & C\left(\left\|\mathbf{\Phi}_{g_{L, \zeta}^{A}}\left(g_{L, \zeta}^{A}\right)-\mathbf{o}_{L, \zeta}^{A}\right\|_{r_{D}^{-2} C_{\beta}^{\alpha}\left(g_{L, \zeta}^{A}\right)}+\left|\zeta^{\mp}\right|^{1-\frac{\beta}{2}}\left|\zeta^{ \pm}\right|^{2}\right) \\
& \times\left\|\mathbf{\Phi}_{g_{L, \zeta}^{A}}\left(g_{L, \zeta}^{A}\right)-\mathbf{o}_{L, \zeta}^{A}\right\|_{r_{D}^{-2} C_{\beta}^{\alpha}\left(g_{L, \zeta}^{A}\right)}
\end{aligned}$$ \(\square\)

Together with the control of Proposition 3.14, Lemma 3.23 implies both a control of the metric and the obstructions.

Remark 3.24. For small $\zeta$, we can essentially treat the obstructions coming from variations of different $\zeta_{i}^{ \pm}, \zeta_{j}^{\mp}$ or $L$ as orthogonal to each other. Indeed, for the different infinitesimal variations, we have the following controls showing where each of the infinitesimal deformation has most of its mass:
\begin{itemize}
\item[-] $\left|\partial_{z_{j}^{\mp}} g_{L_{k}, \zeta_{k}}^{A}\right|_{g_{L_{k}, \zeta_{k}}^{A}} \leqslant C\left|\zeta_{j}^{\mp}\right|\left\|\partial_{z_{j}^{\mp}} g_{L_{k}, \zeta_{k}}^{A}\right\|_{L^{2}}\left(\left|\zeta_{j}^{\mp}\right|^{\frac{1}{2}}+d_{g_{L_{k}, \zeta_{k}}^{A}}(j, .)\right)^{-4}$
\item[-] $\left|\partial_{z_{i}^{ \pm}} g_{L_{k}, \zeta_{k}}^{A}\right|_{g_{L_{k}, \zeta_{k}}^{A}} \leqslant C\left|\zeta_{i}^{ \pm}\right|\left\|\partial_{z_{i}^{ \pm}} g_{L_{k}, \zeta_{k}}^{A}\right\|_{L^{2}}\left(\left|\zeta_{i}^{ \pm}\right|^{\frac{1}{2}}+d_{g_{L_{k}, \zeta_{k}}^{A}}(i, .)\right)^{-4}$
\item[-] $\left|\partial_{K} g_{L_{k}, \zeta_{k}}^{A}\right|_{g_{L_{k}, \zeta_{k}}^{A}} \leqslant C\left\|\partial_{K} g_{L_{k}, \zeta_{k}}^{A}\right\|_{L^{2}}$.
\end{itemize}
Estimating the $L^{2}$-product of two of the above infinitesimal, we see that as $|\zeta| \rightarrow 0$, they become arbitrarily close to being orthogonal.

Corollary 3.25. We have the following controls:
\begin{itemize}
\item[-] $\left\|\hat{g}_{L, \zeta}-g_{L, \zeta}^{A}\right\|_{C_{\beta, *}^{2, \alpha}\left(g_{L, \zeta}^{A}\right)} \leqslant C\left|\zeta^{ \pm}\right|^{1+\frac{\beta}{12}}\left|\zeta^{\mp}\right|^{3-\frac{\beta}{4}}$,
\item[-] and $\left\|\mathbf{o}_{L, \zeta}^{A}\right\|_{L^{2}\left(g_{L, \zeta}^{A}\right)} \leqslant C\left|\zeta^{ \pm}\right|^{3+\frac{\beta}{12}}\left|\zeta^{\mp}\right|^{4-\frac{3 \beta}{4}}$ which rewrites as, for all $j \in S_{\mp}$ and $k \in\{1,2,3\}$, for any $0<\beta<1$ (chosen small enough)
$$\lambda_{k}^{j}(L, \zeta)+\mu_{k}^{j}(L, \zeta)=\mathcal{O}\left(\left|\zeta^{ \pm}\right|^{2}\left|\zeta^{\mp}\right|^{5}+\left|\zeta^{ \pm}\right|^{3+\frac{\beta}{12}}\left|\zeta^{\mp}\right|^{4-\frac{3 \beta}{4}}\right),$$
with $\left|\zeta^{ \pm}\right|^{2}\left|\zeta^{\mp}\right|^{5}$ from (94), and for all $l$,
$$\nu_{l}(L, \zeta)=\mathcal{O}\left(\left|\zeta^{ \pm}\right|^{2}\left|\zeta^{\mp}\right|^{4}+\left|\zeta^{ \pm}\right|^{3+\frac{\beta}{12}}\left|\zeta^{\mp}\right|^{4-\frac{3 \beta}{4}}\right)$$
where the additional error in $\left|\zeta^{ \pm}\right|^{2}\left|\zeta^{\mp}\right|^{4}$ comes from (89).
\end{itemize}

Remark 3.26. Recall that a priori, we only had $\lambda_{k}^{j}(L, \zeta)=\mathcal{O}\left(\left|\zeta^{ \pm}\right|^{2}\left|\zeta^{\mp}\right|\right), \mu_{k}^{j}(L, \zeta)=$ $\mathcal{O}\left(\left|\zeta^{ \pm}\right|^{4}\left|\zeta^{\mp}\right|^{2}\right)$ and $\nu_{l}=\mathcal{O}\left(\left|\zeta^{ \pm}\right|^{2}\left|\zeta^{\mp}\right|^{2}\right)$.
3.4. Obstruction to the total desingularization. We will now prove that there are obstructions to the Gromov-Hausdorff desingularization of $\mathbb{T}^{4} / \mathbb{Z}_{2}$ by Einstein metrics.

Proposition 3.27. Assume that there exists a sequence of Einstein modulo obstructions metrics $\left(\hat{g}_{L_{n}, \zeta_{n}}=\mathbf{g}_{L_{n}, \zeta_{n}}\right)_{n \in \mathbb{N}}$ which are actually Einstein with $\zeta_{n} \rightarrow 0$ and $L_{n} \rightarrow L_{\infty}$ where $\operatorname{det}\left(L_{\infty}\right)>0$. Up to taking a subsequence, we consider the following limits: $\frac{\zeta_{n, j}^{\mp}}{\left|\zeta_{n}^{\mp}\right|} \rightarrow \zeta_{\infty, j}^{\mp}$, $\frac{\zeta_{n, i}^{ \pm}}{\left|\zeta_{n}^{ \pm}\right|} \rightarrow \zeta_{\infty, i}^{ \pm}$and $\frac{\zeta_{n, j}^{\mp}}{\left|\zeta_{n, j}^{\mp}\right|} \rightarrow \phi_{\infty, j}^{\mp}$, as well as the limit
$$\mathbf{R}_{L_{\infty}, \zeta_{\infty}^{ \pm}}:=\lim _{n \rightarrow \infty} \frac{1}{\left|\zeta_{n}^{ \pm}\right|^{2}} \mathbf{R}_{\mathbf{g}_{ \pm, n}}=\lim _{n \rightarrow \infty} \frac{1}{\left|\zeta_{n}^{ \pm}\right|^{2}} \mathbf{R}_{g_{ \pm, n}^{A}} .$$

Then,
\begin{itemize}
\item[(1)] one always has
$$\mathbf{R}_{L_{\infty}, \zeta_{\infty}^{ \pm}}(j)\left(\phi_{\infty, j}^{\mp}\right)=0$$
for all the deformations $\left(0, z^{ \pm}\right)$of $\left(L_{\infty}, \zeta_{\infty}^{ \pm}\right)$, we have
$$\sum_{j \in S_{ \pm}}\left\langle\partial_{\left(0, z^{ \pm}\right)} \mathbf{R}_{L_{\infty}, \zeta_{\infty}^{ \pm}}(j)\left(\zeta_{\infty, j}^{\mp}\right), \zeta_{\infty, j}^{\mp}\right\rangle=0$$
and for all the deformations $(K, 0)$ of $\left(L_{\infty}, \zeta_{\infty}^{ \pm}\right)$, and $\left(\mathbf{v}_{l}\right)_{l}$ an orthonormal basis of $\mathbf{O}\left(\mathbf{g}_{ \pm}\right)$and $\nu_{l}\left(L_{\infty}, \zeta_{\infty}\right)$ the obstructions of (72), we have
$$\sum_{l}\left\langle\partial_{(K, 0)} \mathbf{g}_{ \pm}, \mathbf{v}_{l}\right\rangle_{L^{2}\left(\mathbf{g}_{ \pm}\right)} \nu_{l}\left(L_{\infty}, \zeta_{\infty}\right)=0 .$$
\item[(2)] If we assume that the sequence $\left(\mathbf{g}_{L_{n}, \zeta_{n}}\right)_{n \in \mathbb{N}}$ is a nondegenerate sequence of Einstein desingularizations (see Definition 1.29), then, one moreover has:
$$\mathbf{R}_{L_{\infty}, \zeta_{\infty}^{ \pm}}(j)=0 \text { at every } j \in S_{\mp} .$$
\end{itemize}

Remark 3.28. The assumption $\operatorname{det}\left(L_{\infty}\right)>0$ for $L_{\infty} \in G L(4, \mathbb{R})$ ensures that there is no collapsing and a bounded diameter in our degeneration and therefore that we stay in the context of [And89, BKN89, Ozu19a, Ozu19b].

Remark 3.29. When (101) is satisfied, from (41), we have the following rewriting of the obstruction (103):
$$\sum_{j \in S_{ \pm}}\left\langle\partial_{(K, 0)} \mathbf{R}_{L_{\infty,} \zeta_{\infty}^{ \pm}}(j)\left(\zeta_{\infty, j}^{\mp}\right), \zeta_{\infty, j}^{\mp}\right\rangle=0 .$$
Proof of Proposition 3.27. Let us assume that there exists a sequence of Einstein modulo obstructions $\left(\hat{g}_{L_{n}, \zeta_{n}}=\mathbf{g}_{L_{n}, \zeta_{n}}\right)_{n \in \mathbb{N}}$ which are Einstein with $\zeta_{n} \rightarrow 0$ and $L_{n} \rightarrow L_{\infty}=$ Id . By compactness, up to taking a subsequence, for all $j \in S_{\mp}$ and all $i \in S_{ \pm}$, we have $\frac{\zeta_{n, j}^{\mp}}{\left|\zeta_{n, j}^{\mp}\right|} \rightarrow \zeta_{\infty, j}^{\mp}, \frac{\zeta_{n, i}^{ \pm}}{\left|\zeta_{n}^{ \pm}\right|} \rightarrow \zeta_{\infty, i}^{ \pm}$and $\frac{\zeta_{n, j}^{\mp}}{\left|\zeta_{n, j}^{\mp}\right|} \rightarrow \phi_{\infty, j}^{\mp}$ as $n \rightarrow+\infty$. By (98) and (99), for any $0<\beta<1$ (chosen small enough), we have
$$\lambda_{k}^{j}\left(L_{n}, \zeta_{n}\right)+\mu_{k}^{j}\left(L_{n}, \zeta_{n}\right)=\mathcal{O}\left(\left|\zeta_{n}^{ \pm}\right|^{2}\left|\zeta_{n}^{\mp}\right|^{5}+\left|\zeta_{n}^{ \pm}\right|^{3+\frac{\beta}{12}}\left|\zeta_{n}^{\mp}\right|^{4-\frac{3 \beta}{4}}\right),$$
and for all $l$,
$$\nu_{l}\left(L_{n}, \zeta_{n}\right)=\mathcal{O}\left(\left|\zeta_{n}^{ \pm}\right|^{2}\left|\zeta_{n}^{\mp}\right|^{4}+\left|\zeta_{n}^{ \pm}\right|^{3+\frac{\beta}{12}}\left|\zeta_{n}^{\mp}\right|^{4-\frac{3 \beta}{4}}\right),$$
We directly see from (106) that
$$\lim _{n \rightarrow \infty} \frac{\lambda_{k}^{j}\left(L_{n}, \zeta_{n}\right)}{\left|\zeta_{n}^{ \pm}\right|^{2}\left|\zeta_{n}^{\mp}\right|}=0$$
because $\mu_{k}^{j}\left(L_{n}, \zeta_{n}\right)=\mathcal{O}\left(\left|\zeta_{n}^{ \pm}\right|^{4}\left|\zeta_{n}^{\mp}\right|^{2}\right)$ which proves (101) by the value the obstruction (24) and the control of the curvature of Proposition 3.6.

Similarly, from (107) we find
$$\lim _{n \rightarrow \infty} \frac{\nu_{l}\left(L_{n}, \zeta_{n}\right)}{\left|\zeta_{n}^{ \pm}\right|^{2}\left|\zeta_{n}^{\mp}\right|^{2}}=0$$
which proves (103). In order to prove (102), we note that the constant part (the limit at the singular point) of $\partial_{\left(0, z^{ \pm}\right)} \mathbf{g}_{ \pm}$scales like $\left|\zeta_{n}^{ \pm}\right|^{2}$. Thanks to the expression (36) of the obstruction, this tells us that the obstruction induced by the constant part (the limit at the singular point) scales like $\left|\zeta_{n}^{ \pm}\right|^{4}\left|\zeta_{n}^{\mp}\right|^{2}$ because we have $H_{2}^{4} \propto\left|\zeta_{n}^{ \pm}\right|^{2}\left|\zeta_{n}^{\mp}\right|^{2} r_{\mathbf{e}}^{-2}$ in the development (70). In the limit, we are left with the obstruction coming from the nonconstant part of $\partial_{\left(0, z^{ \pm}\right)} \mathbf{g}_{ \pm}$whose interpretation in (41) yields the obstruction (102) using the control of the variations of the curvature (66).
We conclude exactly as in the proof of Theorem 0.2 by using (106) as a replacement for
(51). More precisely, if we assume towards a contradiction that the obstruction (104) is not satisfied, that is $\lim _{n \rightarrow \infty} \frac{\mu_{j, 1}\left(L_{n}, \zeta_{n}\right)}{\left|\zeta_{n}^{ \pm}\right|^{4}\left|\zeta_{n}^{\mp}\right|^{2}}=0$ is not satisfied, then since we have $\left|\mathbf{R}_{\mathbf{g}_{ \pm}}\right| \sim\left|\zeta_{n}^{ \pm}\right|^{2}$, the estimates (55) and (56) become
$$\begin{gathered}
\lambda_{1}^{j}\left(L_{\infty}, \phi_{n, j}\right)=\mathcal{O}\left(\left|\zeta_{n}^{ \pm}\right|^{2}\left|\phi_{n, j}-\phi_{\infty, j}\right|^{2}\right), \text { and } \\
\left|\left(\lambda_{2}^{j}\left(L_{\infty}, \phi_{n, j}\right), \lambda_{3}^{j}\left(L_{\infty}, \phi_{n, j}\right)\right)\right| \geqslant c\left|\zeta_{n}^{ \pm}\right|^{2}\left|\phi_{n, j}-\phi_{\infty, j}\right|, \text { for some } c>0 .
\end{gathered}$$
As in the proof of Theorem 0.2, we find a contradiction using (106) for $k=2,3$ and then $k=1$. Similarly, as in the proof of Theorem 0.2 one can use the eigenvalue estimate of [Biq17] to deal with the stable situation thanks to the estimate of Corollary 3.25. \(\square\)

Remark 3.30. Allowing some Eguchi-Hanson metrics to be glued at negligible scale might not preserve the obstruction $\mathbf{R}_{ \pm}=0$ at the associated point and might reduce the number of obstructions by 2 per such point. Indeed, $\mathbf{R}^{ \pm}$is in the 5-dimensional space of traceless symmetric 2-tensors and the first obstructions $\lambda_{k}=0$, give 3 independent equations. But we will see that the scale being negligible means that we lose the 3 degrees of freedom. These situations should therefore be more obstructed even without the obstruction $\mathbf{R}^{ \pm}=0$.

\section*{4. Explicit obstructions to the desingularization of $\mathbb{T}^{4} / \mathbb{Z}_{2}$}

Let us now make the obstructions of Proposition 3.27 more explicit as the vanishing of polynomial functions of the $\zeta^{ \pm}$, whose coefficients depend on the flat metric $\mathbf{g}_{L}$ alone.

Recall from (13) that the curvature of the Eguchi-Hanson metric $\mathbf{e h}_{\zeta^{+}}$and by their first asymptotic term $\frac{\zeta^{+} \circ \rho(\zeta)^{-}}{r^{4}}$ has the form $12 \pi_{\operatorname{tr}} \frac{\rho(\zeta)^{-} \otimes \rho(\zeta)^{-}}{r^{6}}$ where $\rho(\zeta)^{-}$is defined in Definition 1.14.

Note 4.1. During all of this section, we will often identify $\mathbb{R}^{3}$ and $\Omega^{+}$or $\Omega^{-}$thanks to the bases $\left(\omega_{i}^{ \pm}\right)_{i \in\{1,2,3\}}$. This will make it more convenient to find identities relating different obstructions in Lemma 4.6 for instance. That is why we are defining the selfdual or antiselfdual curvature-like quantities $b_{x}$ and $B_{x}^{L}$ on $\mathbb{R}^{3}$. We will also use the identification $\mathbb{R}^{3} \otimes \mathbb{R}^{3} \approx \Omega^{ \pm} \otimes \Omega^{ \pm} \approx\left(\Omega^{ \pm}\right)^{*} \otimes \Omega^{ \pm} \approx \operatorname{End}\left(\Omega^{ \pm}\right)$.

For $x \in \mathbb{R}^{4}$ and $\zeta, \zeta^{\prime} \in \mathbb{R}^{3} \backslash\{0\}$, we define $b_{x}\left(\zeta, \zeta^{\prime}\right):=12 \frac{\rho_{x}(\zeta)^{-} \otimes \rho_{x}\left(\zeta^{\prime}\right)^{-}}{|x|^{6}}$, where $\rho_{x}$ for $x \in \mathbb{R}^{4}$ is the rotation explicited in (8). Note that $\rho_{-x}=\left(\rho_{x}\right)^{t}=\left(\rho_{x}\right)^{-1}=\rho_{x}$. For any $z, z^{\prime} \in \mathbb{R}^{3}$, we have
$$\left\langle b_{x}\left(\zeta, \zeta^{\prime}\right) z, z^{\prime}\right\rangle:=12 \frac{\left\langle\rho_{x}(\zeta), z\right\rangle\left\langle\rho_{x}\left(\zeta^{\prime}\right), z^{\prime}\right\rangle}{|x|^{6}} .$$
We also define the following bilinear form with values in $\mathbb{R}^{3} \otimes \mathbb{R}^{3}$ :
$$B_{x}^{L}\left(\zeta, \zeta^{\prime}\right):=\pi_{t r} \sum_{a \in \mathbb{Z}^{4}} b_{L(x-2 a)}\left(\zeta, \zeta^{\prime}\right)$$
for $x \in \mathbb{R}^{4}$ and $L$ a $4 \times 4$ matrix, where $\pi_{t r}$ is the projection on the traceless part.
Lemma 4.2. Let ( $M_{ \pm}, g_{ \pm}^{A}$ ) be one of the partial desingularizations of $\mathbb{T}^{4} / \mathbb{Z}_{2}$ of Definition (3.5). Then, for any $j_{0} \in S_{-}$and any $\zeta \in \mathbb{R}^{3}$ and the associated $\zeta^{-} \in \Omega^{-}$(thanks to the basis $\left(\omega_{i}^{-}\right)_{i \in\{1,2,3\}}$ ), we have
$$\mathbf{R}_{g_{+}^{A}}^{-}\left(j_{0}\right) \zeta^{-}=\sum_{i \in S_{+}}\left(B_{j_{0}-i}^{L}\left(\zeta_{i}, \zeta_{i}\right) \zeta\right)^{-}$$
where again $B_{j_{0}-i}^{L}\left(\zeta_{i}, \zeta_{i}\right) \zeta \in \mathbb{R}^{3}$ and $\left(B_{j_{0}-i}^{L}\left(\zeta_{i}, \zeta_{i}\right) \zeta\right)^{-} \in \Omega^{-}$.

Proof. Away from the glued Eguchi-Hanson metrics, $g_{+}^{A}$ equals $\mathbf{g}_{L}+\sum_{i \in S_{+}} \bar{h}_{\zeta_{i}^{+}}^{4}$ where the $\bar{h}_{\zeta_{i}^{+}}^{4}$ are explicited in (62). By Remark 3.4 and the formula (13), the induced curvature is therefore given by (110). \(\square\)

We have the following properties for $B_{x}^{L}\left(\zeta, \zeta^{\prime}\right)$ for any $x \in \mathbb{R}^{4}$ and $\zeta, \zeta^{\prime} \in \mathbb{R}^{3}$
\begin{itemize}
\item[(1)] $B_{x}^{L}\left(\zeta, \zeta^{\prime}\right)=B_{x}^{L}\left(\zeta^{\prime}, \zeta\right)$,
\item[(2)] $B_{x}^{L}\left(\zeta, \zeta^{\prime}\right)=B_{-x}^{L}\left(\zeta, \zeta^{\prime}\right)$,
\item[(3)] $B_{x+a}^{L}\left(\zeta, \zeta^{\prime}\right)=B_{x}^{L}\left(\zeta, \zeta^{\prime}\right)$ for $a \in \mathbb{Z}^{4}$,
\end{itemize}

Corollary 4.3. The obstruction (101) rewrites for all $j_{0} \in S_{-}$,
$$\sum_{i \in S_{+}}\left\langle B_{j_{0}-i}^{L}\left(\zeta_{i}, \zeta_{i}\right) \zeta_{j_{0}}, \zeta_{j_{0}}\right\rangle=0$$
and from (102) for $j_{0} \in S_{-}$and an infinitesimal deformation of $\zeta_{j_{0}}$ in the direction $z_{j_{0}}$ :
$$\sum_{i \in S_{+}}\left\langle B_{j_{0}-i}^{L}\left(z_{j_{0}}, \zeta_{j_{0}}\right) \zeta_{i}, \zeta_{i}\right\rangle=0 .$$
For the conjectural value of the obstructions (105), against a deformation $K$ of the matrix $L$, denoting $\partial_{K} B_{j-i}^{L}$ the linearization of $L \mapsto B_{j-i}^{L}$ for $i \in S_{+}$and $j \in S_{-}$at $L$ and in the direction $K$, we have
$$\sum_{i \in S_{+}} \sum_{j \in S_{-}}\left\langle\partial_{K} B_{j-i}^{L}\left(\zeta_{i}, \zeta_{i}\right) \zeta_{j}, \zeta_{j}\right\rangle=0 .$$
Finally, the obstruction (104) rewrites for any $j_{0} \in S_{-}$:
$$\sum_{i \in S_{+}} B_{j_{0}-i}^{L}\left(\zeta_{i}, \zeta_{i}\right)=0$$

The analogous obstructions hold for the other orientation.
Remark 4.4. The obstruction identified in [BK17] corresponds to the nonvanishing of the one obstruction
$$\sum_{i \in S_{+}} \sum_{j \in S_{-}}\left\langle B_{j-i}^{L}\left(\zeta_{i}, \zeta_{i}\right) \zeta_{j}, \zeta_{j}\right\rangle=0$$
(which is clearly implied by (111)), in the particular situation where
\begin{itemize}
\item[-] $L=\mathrm{Id}$,
\item[-] the sets $S_{ \pm}$follow a chessboard pattern (see [BK17] or Section 4.3),
\item[-] for all $i \in S_{+}, j \in S_{-}, \zeta_{i}=(1,0,0)$ and $\zeta_{j}=(1,0,0)$.
\end{itemize}

Remark 4.5. If the Eguchi-Hanson metrics are glued at comparable scales, then:
\begin{itemize}
\item[-] the obstructions (111) correspond to $3\left|S_{+}\right|$equations for $3\left|S_{-}\right|+9$ parameters given by the $\left|S_{-}\right|$vectors $\zeta_{j}^{-}$and the matrix $L$,
\item[-] the obstructions (114) correspond to $5\left|S_{+}\right|$equations since $\mathbf{R}$ is symmetric tracefree for $3\left|S_{-}\right|+9$ parameters given by the $\left|S_{-}\right|$vectors $\zeta_{j}^{-}$and the matrix $L$,
\item[-] the obstructions (113) are 9 equations, for the different deformations of the torus, for $3\left|S_{+}\right|+3\left|S_{-}\right|+9=57$ parameters,
\item[-] the obstructions (112) are $3\left|S_{-}\right|$equations for $3\left|S_{+}\right|+9$ parameters.
\end{itemize}
Since we have analogous obstructions in the other orientation, we see that we a priori have many more obstructions to satisfy than parameters. We will reduce the number of these equations in the next section.
4.1. Equivalent obstructions. Let us show that many of the above equations are actually equivalent. Let us therefore just assume that we have the obstructions (114) at every singular point in both orientations and prove that some of the other obstructions are already satisfied.
4.1.1. Against the deformation of the Eguchi-Hanson metrics.

Lemma 4.6. We have the following equality for all $i \in S_{+}, j \in S_{-}, \zeta \in\left(\mathbb{R}^{3}\right)^{\left|S_{+}\right|} \times\left(\mathbb{R}^{3}\right)^{\left|S_{-}\right|}$ and $z \in \mathbb{R}^{3}$,
$$\left\langle B_{j-i}^{L}\left(\zeta_{i}, z\right) \zeta_{j}, \zeta_{j}\right\rangle=\left\langle B_{j-i}^{L}\left(\zeta_{j}, \zeta_{j}\right) \zeta_{i}, z\right\rangle,$$
and therefore the above obstruction (114) at all singular points in the opposite orientation implies that the obstructions (112) vanish.
Remark 4.7. This shows that the first obstructions coming from the deformations of the Eguchi-Hanson metrics are seen whether we first desingularize the positive ones or the negative ones.
Proof. Given the expression of $B_{j-i}^{L}$ of (109), we will study for $a \in \mathbb{Z}^{4}$ a term of the above expressions. Because of the symmetries of $B$, we can simply study $\left\langle\pi_{t r} b_{x}\left(\zeta_{i}, z\right) \zeta_{j}, \zeta_{j}\right\rangle$. We will first consider $z$ proportional to $\zeta_{i}$ to obtain
$$\begin{aligned}
\left\langle\pi_{t r} b_{x}\left(\zeta_{i}, \zeta_{i}\right) \zeta_{j}, \zeta_{j}\right\rangle & =\left\langle\left(12 \rho_{x}\left(\zeta_{i}\right) \otimes \rho_{x}\left(\zeta_{i}\right)-4\left|\zeta_{i}\right|^{2} \mathrm{I}_{3}\right) \zeta_{j}, \zeta_{j}\right\rangle \\
& =12\left\langle\rho_{x}\left(\zeta_{i}\right), \zeta_{j}\right\rangle^{2}-4\left|\zeta_{i}\right|^{2}\left|\zeta_{j}\right|^{2} \\
& =12\left\langle\left(\rho_{x}\left(\zeta_{j}\right) \otimes \rho_{x}\left(\zeta_{j}\right)-4\left|\zeta_{j}\right|^{2} \mathrm{I}_{3}\right) \zeta_{i}, \zeta_{i}\right\rangle \\
& =\left\langle\pi_{t r} b_{x}\left(\zeta_{j}, \zeta_{j}\right) \zeta_{i}, \zeta_{i}\right\rangle
\end{aligned}$$
where we used the fact that $\rho_{-x}=\left(\rho_{x}\right)^{T}=\left(\rho_{x}\right)^{-1}=\rho_{x}$. For $z \perp \zeta_{i}$,
$$\begin{aligned}
\left\langle\pi_{t r} b_{x}\left(\zeta_{i}, z\right) \zeta_{j}, \zeta_{j}\right\rangle & =\left\langle\left(12 \rho_{x}\left(\zeta_{i}\right) \otimes \rho_{x}(z)\right) \zeta_{j}, \zeta_{j}\right\rangle \\
& =12\left\langle\rho_{x}\left(\zeta_{i}\right), \zeta_{j}\right\rangle\left\langle\rho_{x}(z), \zeta_{j}\right\rangle \\
& =12\left\langle\left(\rho_{x}\left(\zeta_{j}\right) \otimes \rho_{x}\left(\zeta_{j}\right)-4\left|\zeta_{j}\right|^{2} I_{3}\right) \zeta_{i}, z\right\rangle \\
& =\left\langle\pi_{t r} b_{x}\left(\zeta_{j}, \zeta_{j}\right) \zeta_{i}, z\right\rangle
\end{aligned}$$
This proves the statement. \(\square\)
4.1.2. Against the flat deformations of the torus. The last deformations to consider are the flat deformations of the torus which are equivalent to variations of the matrix $L$ used in the definition of $B_{x}^{L}$. For the conjectural form of the obstruction (105), we compute the following expression. We omit the proof as the obstruction itself is only conjectural.
Lemma 4.8. Let us consider an infinitesimal variation of the flat torus seen as an infinitesimal variation of the matrix $L$ in the direction $K L^{-1}$, and assume that the obstruction (114) is satisfied in both orientations.

Then, the conjectural obstruction (105) for a variation $K L^{-1}$ of $L$ is equivalent to
$$\sum_{i \in S_{+}} \sum_{j \in S_{-}} \sum_{a \in \mathbb{Z}^{4}} \frac{\langle L(i-j-2 a), K(i-j-2 a)\rangle}{|L(i-j-2 a)|^{2}}\left\langle\pi_{t r} b_{L(i-j-2 a)}\left(\zeta_{i}, \zeta_{i}\right) \zeta_{j}, \zeta_{j}\right\rangle=0$$ \(\square\)

Remark 4.9. The deformations of the matrix Id other than those in the space spanned by the $\pi_{t r}\left(e_{k} \otimes e_{k}\right)$ for $\left(e_{k}\right)_{k \in\{1,2,3,4\}}$ the usual basis of $\mathbb{R}^{4}$, are equivalent to rotations of the torus and therefore to the rotation of the Eguchi-Hanson metrics and have already been considered above.

Corollary 4.10. The obstructions of Corollary 4.3 reduce to 84 polynomial equations in the $\zeta_{i}$ and $\zeta_{j}$ with coefficients depending on $L$ only.
4.2. Some obstructed situations. We therefore see from Remark 4.5 that even though some obstructions are equivalent, there are many remaining ones that outnumber the degrees of freedom we have. Indeed, we have only ruled out the last type of obstructions corresponding to (112).

Let us now give an example of configuration of desingularization which cannot yield Ricci-flat (or even Einstein) metrics thanks to the obstructions identified in Corollary 4.3.

Theorem 4.11. There does not exist a sequence Einstein metrics $\left(M, \mathbf{g}_{n}\right)_{n \in \mathbb{N}}$ converging in the Gromov-Hausdorff sense to $\left(\mathbb{T}^{4} / \mathbb{Z}_{2}, \mathbf{g}_{L_{\infty}}\right)$ with $L_{\infty}=\mathrm{Id}$ by bubbling out exactly 1 positively oriented Eguchi-Hanson metric and 15 negatively oriented one.

Remark 4.12. This is an obstruction to any Gromov-Hausdorff desingularization under a topological assumption.

Proof. Let $\left(M, \mathbf{g}_{n}\right)_{n \in \mathbb{N}}$ be a sequence of Einstein metrics converging to ( $\mathbb{T}^{4} / \mathbb{Z}_{2}, \mathbf{g}_{L_{\infty}}$ ) with $L_{\infty}=$ Id in the Gromov-Hausdorff sense while bubbling out Eguchi-Hanson metrics and let us assume without loss of generality that $S_{+}=\{0\}$ and $S_{-}$is the complement of $\{0\}$ among the singular points of $\mathbb{T}^{4} / \mathbb{Z}_{2}$. Then, according to [Ozu19b], up to taking a subsequence, for all $n$, there exist $L_{n}, \zeta_{n, 0}^{+}$and $\zeta_{n, j}^{-}$for $j \in S_{-}$, such that the metrics $\mathbf{g}_{n}$ are isometric to Einstein modulo obstructions perturbations of $g_{L_{n}, \zeta_{n}}^{D}$.

Let us show that the limit rescaled curvature $\mathbf{R}_{L_{\infty}, \zeta_{\infty}^{+}}(j)$ defined in Proposition 3.27 is invertible at a singular point $j \in S_{-}$. This will lead to a contradiction by the obstruction (101).

By Lemma 4.2, we have an expression of $\mathbf{R}_{L_{\infty}, \zeta_{\infty}^{+}}^{-}(j)$ : it is a nonvanishing multiple of
$$\sum_{a \in \mathbb{Z}^{4}} \pi_{t r} \frac{\theta_{1}^{-}((1,0,0,0)+2 a) \otimes \theta_{1}^{-}((1,0,0,0)+2 a)}{|(1,0,0,0)+2 a|^{6}} .$$
The value of the summand at $a=0$ and $a=(-1,0,0,0)$ is
$$\pi_{t r}\left(\omega_{1}^{-} \otimes \omega_{1}^{-}\right)=\frac{1}{3}\left(2 \omega_{1}^{-} \otimes \omega_{1}^{-}-\omega_{2}^{-} \otimes \omega_{2}^{-}-\omega_{3}^{-} \otimes \omega_{3}^{-}\right),$$
which is invertible on $\Omega^{-}$. For the sum of the norms of the remaining terms, that is,
$$\sum_{a \in \mathbb{Z}^{4} \backslash\{0,(-1,0,0,0)\}}\left|\pi_{t r} \frac{\theta_{1}^{-}((1,0,0,0)+2 a) \otimes \theta_{1}^{-}((1,0,0,0)+2 a)}{|(1,0,0,0)+2 a|^{6}}\right|,$$
we numerically have the control
$$\sum_{a \in \mathbb{Z}^{4} \backslash\{0,(-1,0,0,0)\}} \frac{1}{|(1,0,0,0)+2 a|^{6}} \approx 0.19<\frac{2}{3} .$$
This is not enough to make the sum (124) non invertible given the expression (125). The result follows by (111). \(\square\)

Remark 4.13. The above proof works for many other limits than $L_{\infty}=\mathrm{Id}$ and it is likely that it is true for any $L_{\infty}$, but it requires some control of the compactness of the lattice generated by $L_{\infty}$. Theorem 4.11 particular holds even with the most compact lattices like the $D_{4}$ lattice. By compactness, we loosely mean how close the points of the lattice are to each other.

Conjecture 4.14. The statement of Theorem 4.11 holds even without the assumption $L_{\infty}=\mathrm{Id}$, but only assuming that $\operatorname{det}\left(L_{\infty}\right)>0$.

For stable or nondegenerate Ricci-flat deformations, one does not simply have $\mathrm{R}_{L_{\infty}, \zeta_{\infty}^{+}}^{-}(j)$ invertible, but $\mathrm{R}_{L_{\infty}, \zeta_{\infty}^{+}}^{-}(j)=0$. Since it is a sum of terms of the form (124) based at each singular point, it is direct to see that $\mathrm{R}_{L_{\infty, \zeta_{\infty}^{+}}^{-}}(j)=0$ requires at least 3 Eguchi-Hanson metrics in this orientation.

Corollary 4.15. There does not exist a sequence of stable Ricci-flat metrics $\left(M, \mathbf{g}_{n}\right)_{n \in \mathbb{N}}$ converging in the Gromov-Hausdorff sense to $\left(\mathbb{T}^{4} / \mathbb{Z}_{2}, \mathbf{g}_{L_{\infty}}\right)$ with $L_{\infty}=\mathrm{Id}$ by bubbling out at most 3 positively oriented Eguchi-Hanson metric and the rest of negatively oriented ones.
4.3. A family of desingularizations satisfying the obstructions. Let us now specialize our discussion to the regular torus with $L=$ Id and with the so-called chessboard pattern considered in [BK17]. We study the 48-dimensional space of gluings to the (fixed) regular torus and test it against the $16 \times 5+4=84$ (the last 4 only having a conjectural expression in terms of curvature) obstruction equations identified in Section 4.

Perhaps surprisingly, in this most symmetric situation, we will find a family of solutions to all of our 84 equations. This family of solutions is 14-dimensional.

Remark 4.16. It will be clear from our proof and computations in this section that in the configuration considered in [BK17], many of these 84 equations are not satisfied.

The chessboard configuration already considered in [BK17] is defined as:
$$\begin{aligned}
& S_{-}=\left(\left\{\left(a_{1}, a_{2}, a_{3}, a_{4}\right) \in \mathbb{Z}^{4}, a_{1}+a_{2}+a_{3}+a_{4} \in 2 \mathbb{Z}\right\} / \mathbb{Z}^{4}\right) / \mathbb{Z}_{2} \text { and } \\
& S_{+}=\left(\left\{\left(a_{1}, a_{2}, a_{3}, a_{4}\right) \in \mathbb{Z}^{4}, a_{1}+a_{2}+a_{3}+a_{4} \in 1+2 \mathbb{Z}\right\} / \mathbb{Z}^{4}\right) / \mathbb{Z}_{2} .
\end{aligned}$$

Remark 4.17. In this chessboard configuration, let $i \in S_{ \pm}$. Then, we have the following configuration of other singular points:
\begin{itemize}
\item[-] at distance 0 is $i \in S_{ \pm}$
\item[-] at distance 1, there are 4 points in $S_{\mp}$
\item[-] at distance $\sqrt{2}$, there are 6 points in $S_{ \pm}$,
\item[-] at distance $\sqrt{3}$, there are 4 points in $S_{\mp}$, and
\item[-] at distance 2, there is a point in $S_{ \pm}$.
\end{itemize}

We will denote $i^{c}$ the opposite of $i$ which is the point at maximal distance 2 from $i$.
Here we will work under the assumption that for all $i$,
$$\zeta_{i}=\zeta_{i^{c}} .$$
We will denote $e_{1}=(1,0,0,0) \in S_{+}$and similarly $e_{i} \in S_{+}$for $i \in\{1,2,3,4\}$ the other vectors of the canonical basis of $\mathbb{R}^{4}$. Let us introduce the following notations for the coordinates of our gluing parameters $\zeta_{e_{i}}$ :
$$\zeta_{e_{i}}=:\left(x_{i}, y_{i}, z_{i}\right),$$
for $i \in\{1,2,3,4\}$. Let us denote $x=\left(x_{1}, x_{2}, x_{3}, x_{4}\right), y=\left(y_{1}, y_{2}, y_{3}, y_{4}\right)$ and $z=$ $\left(z_{1}, z_{2}, z_{3}, z_{4}\right)$ the three vectors in $\mathbb{R}^{4}$ we obtain.

Proposition 4.18. Using the above notations, let us assume that the family $(x, y, z)$ of vectors of $\mathbb{R}^{4}$ forms an orthogonal family of $\mathbb{R}^{4}$ with constant length. Then, the obstructions (105) and the obstructions (104) at every $j \in S_{-}$are satisfied.

Sketch of proof (some computer-based arguments involved). Let us consider a desingularization configuration as above.

Let us study the curvature at the singular point $0 \in S_{-}$induced by the other EguchiHanson metrics glued at the points of $S_{+}$. From (110), we know that this exactly equals
$$\sum_{i=1}^{4} B_{e_{i}}^{\mathrm{Id}}\left(\left(x_{i}, y_{i}, z_{i}\right),\left(x_{i}, y_{i}, z_{i}\right)\right)+B_{e_{i}^{c}}^{\mathrm{Id}}\left(\left(x_{i}, y_{i}, z_{i}\right),\left(x_{i}, y_{i}, z_{i}\right)\right) .$$

Numerically, we obtain the following form for $B_{e_{i}}^{\mathrm{Id}}\left(\left(x_{i}, y_{i}, z_{i}\right),\left(x_{i}, y_{i}, z_{i}\right)\right)+B_{e_{i}^{c}}^{\mathrm{Id}}\left(\left(x_{i}, y_{i}, z_{i}\right),\left(x_{i}, y_{i}, z_{i}\right)\right)$ :
$$\left[\begin{array}{ccc}
a \cdot\left(2 x_{i}^{2}-y_{i}^{2}-z_{i}^{2}\right) & b \cdot x_{i} y_{i} & b \cdot x_{i} z_{i} \\
b \cdot x_{i} y_{i} & a \cdot\left(-x_{i}^{2}+2 y_{i}^{2}-z_{i}^{2}\right) & b \cdot y_{i} z_{i} \\
b \cdot x_{i} z_{i} & b \cdot y_{i} z_{i} & a \cdot\left(-x_{i}^{2}-y_{i}^{2}+2 z_{i}^{2}\right)
\end{array}\right],$$
for some real numbers $a \approx 0.69$ and $b \approx 2.0$, and similar formulas for the other $i$ by symmetries. Therefore, the equation
$$\sum_{i=1}^{4} B_{e_{i}}^{\mathrm{Id}}\left(\left(x_{i}, y_{i}, z_{i}\right),\left(x_{i}, y_{i}, z_{i}\right)\right)+B_{e_{i}^{c}}^{\mathrm{Id}}\left(\left(x_{i}, y_{i}, z_{i}\right),\left(x_{i}, y_{i}, z_{i}\right)\right)=0 .$$
coming from the obstruction (114) reduces to having both
$$\begin{gathered}
\sum_{i=1}^{4} x_{i}^{2}=\sum_{i=1}^{4} y_{i}^{2}=\sum_{i=1}^{4} z_{i}^{2}, \text { and } \\
\sum_{i=1}^{4} x_{i} y_{i}=\sum_{i=1}^{4} x_{i} z_{i}=\sum_{i=1}^{4} y_{i} z_{i}=0
\end{gathered}$$
This means that we are looking for an orthogonal family of 3 vectors $x=\left(x_{i}\right)_{i}, y=\left(y_{i}\right)_{i}$ and $z=\left(z_{i}\right)_{i}$ with same length in $\mathbb{R}^{4}$. This is given by an element of $\mathbb{R}^{+} \times \mathbb{R} P^{3} \times O(3)$. More precisely, the element of $\mathbb{R}$ is equal to $\sum_{i=1}^{4} x_{i}^{2}=\sum_{i=1}^{4} y_{i}^{2}=\sum_{i=1}^{4} z_{i}^{2}$, the element of $\mathbb{R} P^{3}$ is a line orthogonal to $(x, y, z)$ in $\mathbb{R}^{4}$ and $O(3)$ is the orthonormal basis $(x /|x|, y /|y|, z /|z|)$ in the orthogonal of the element of $\mathbb{R} P^{3}$. This set is 7 -dimensional.

Similarly, we can study the variations of the curvature when $L=\mathrm{Id}$ in the directions $e_{i} \otimes e_{i}$ for $i \in\{1,2,3,4\}$. We again find numerically that the conjectural obstructions (105) are of the form:
$$\left[\begin{array}{ccc}
c \cdot\left(2 x_{i}^{2}-y_{i}^{2}-z_{i}^{2}\right) & d \cdot x_{i} y_{i} & e \cdot x_{i} z_{i} \\
d \cdot x_{i} y_{i} & c \cdot\left(-x_{i}^{2}+2 y_{i}^{2}-z_{i}^{2}\right) & f \cdot y_{i} z_{i} \\
e \cdot x_{i} z_{i} & f \cdot y_{i} z_{i} & c \cdot\left(-x_{i}^{2}-y_{i}^{2}+2 z_{i}^{2}\right)
\end{array}\right],$$
for some nonvanishing real numbers $c, d, e, f$ which depend on the direction in which the deformation is done. Therefore, they also vanish under the conditions $\sum_{i=1}^{4} x_{i}^{2}=$ $\sum_{i=1}^{4} y_{i}^{2}=\sum_{i=1}^{4} z_{i}^{2}$ and $\sum_{i=1}^{4} x_{i} y_{i}=\sum_{i=1}^{4} x_{i} z_{i}=\sum_{i=1}^{4} y_{i} z_{i}=0$.

Moreover, because we have similar equations and degrees of freedom in the other orientation, we obtain a 14-dimensional family of candidates satisfying all of the obstructions of Corollary 4.3. \(\square\)

Example 4.19. Some examples of solutions to the above equations are
$$\begin{gathered}
\zeta_{1}=(1,1,1), \quad \zeta_{2}=(1,-1,-1), \zeta_{3}=(-1,1,-1) \text { and } \zeta_{4}=(-1,-1,1) \text { and } \\
\zeta_{1}=(1,0,0), \quad \zeta_{2}=(0,1 / \sqrt{2}, 0), \zeta_{3}=(0,0,1 / \sqrt{2}) \text { and } \quad \zeta_{4}=(1,0,0)
\end{gathered}$$

\section*{Appendix A. Function spaces}

For a tensor $s$, a point $x, \alpha>0$ and a Riemannian manifold $(M, g)$. The Hölder seminorm is defined as
$$[s]_{C^{\alpha}(g)}(x):=\sup _{\left\{y \in T_{x} M,|y|<\operatorname{inj}_{g}(x)\right\}}\left|\frac{s(x)-s\left(\exp _{x}^{g}(y)\right)}{|y|^{\alpha}}\right|_{g} .$$

For orbifolds, we consider a norm bounded for tensors decaying at the singular points.
Definition A. 1 (Weighted Hölder norms on an orbifold). Let $\beta \in \mathbb{R}, k \in \mathbb{N}, 0<\alpha<1$ and $\left(M_{o}, g_{o}\right)$ an orbifold. Then, for any tensor $s$ on $M_{o}$, we define
$$\|s\|_{C_{\beta}^{k, \alpha}\left(g_{o}\right)}:=\sup _{M_{o}} r_{o}^{-\beta}\left(\sum_{i=0}^{k} r_{o}^{i}\left|\nabla_{g_{o}}^{i} s\right|_{g_{o}}+r_{o}^{k+\alpha}\left[\nabla_{g_{o}}^{k} s\right]_{C^{\alpha}\left(g_{o}\right)}\right) .$$

For ALE manifolds, we will consider a norm bounded for tensors decaying at infinity.
Definition A. 2 (Weighted Hölder norms on an ALE orbifold). Let $\beta \in \mathbb{R}, k \in \mathbb{N}, 0<$ $\alpha<1$ and $\left(N, g_{b}\right)$ be an ALE manifold. Then, for all tensor $s$ on $N$, we define
$$\|s\|_{C_{\beta}^{k, \alpha}\left(g_{b}\right)}:=\sup _{N} r_{b}^{\beta}\left(\sum_{i=0}^{k} r_{b}^{i}\left|\nabla_{g_{b}}^{i} s\right|_{g_{b}}+r_{b}^{k+\alpha}\left[\nabla_{g_{b}}^{k} s\right]_{C^{\alpha}\left(g_{b}\right)}\right) .$$

On $M$, using a partition of unity $1=\chi_{M_{o}^{t}}+\sum_{j} \chi_{N_{j}^{t}}$ with $\chi_{M_{o}^{t}}$ equals to 1 where $g_{t}^{D}=\mathbf{g}_{o}$ and $\chi_{N_{j}^{t}}$ equals to 1 where $g_{t}^{D}=t_{j} \mathbf{g}_{b_{j}}$ (see [Ozu19a]), we can define a global norm.
Definition A. 3 (Weighted Hölder norm on a naïve desingularization). Let $\beta \in \mathbb{R}, k \in \mathbb{N}$ and $0<\alpha<1$. We define for $s \in T M^{\otimes l_{+}} \otimes T^{*} M^{\otimes l_{-}}$a tensor $\left(l_{+}, l_{-}\right) \in \mathbb{N}^{2}$, with $l:=l_{+}-l_{-}$the associated conformal weight,
$$\|s\|_{C_{\beta}^{k, \alpha}\left(g^{D}\right)}:=\left\|\chi_{M_{o}^{t}} s\right\|_{C_{\beta}^{k, \alpha}\left(g_{o}\right)}+\sum_{j} T_{j}^{\frac{l}{2}}\left\|\chi_{N_{j}^{t}} s\right\|_{C_{\beta}^{k, \alpha}\left(g_{b_{j}}\right)} .$$
A.1. Decoupling norms. We actually need a last family of norms to get good analytic properties for our operators, see [Ozu19b]. With the notations of Definition 1.2, denote for each singular point $k, A_{k}\left(t, \epsilon_{0}\right):=\left(\Phi_{k}\right)_{*} A_{\mathbf{e}}\left(\epsilon_{0}^{-1} \sqrt{t_{k}}, \epsilon_{0}\right)$ and $B_{k}\left(\epsilon_{0}\right):=\left(\Phi_{k}\right)_{*} B_{\mathbf{e}}\left(0, \epsilon_{0}\right)$, as well as cut-off functions $\chi_{A_{k}\left(t, \epsilon_{0}\right)}$ and $\chi_{B_{k}\left(\epsilon_{0}\right)}$ respectively supported in $A_{k}(t, \epsilon)$ and $B_{k}\left(\epsilon_{0}\right)$, and equal to 1 on $A_{k}\left(t, 2 \epsilon_{0}\right)$ and $B_{k}\left(\epsilon_{0} / 2\right)$.