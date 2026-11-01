---
retention_scope: session
part: 2
total_parts: 4
---

[Part 2/4 of: [2012.13316] Higher order obstructions to the desingularization of Einstein metrics]

The link between the next asymptotic term $H_{2}^{4}$ of the Einstein modulo obstructions deformation $\underline{h}_{2}=H_{2}+H_{2}^{4}+\ldots$ of Lemma 2.3 and the development of $\underline{h}_{0}=H_{0}+H_{0}^{4}+\ldots$ is given by the following integration by parts:
$$\begin{aligned}
0 & =\int_{N}\left\langle P_{\mathbf{e h}} \underline{h}_{2}-\Lambda \mathbf{e h}-\sum_{k} \lambda_{k} \mathbf{o}_{k}, \underline{h}_{0}\right\rangle_{\mathbf{e h}} d v_{\mathbf{e h}} \\
& =\int_{N}\left\langle P_{\mathbf{e h}} \underline{h}_{2}, \underline{h}_{0}\right\rangle_{\mathbf{e h}} d v_{\mathbf{e h}} \\
& =\int_{N}\left\langle\underline{h}_{2}, P_{\mathbf{e h}} \underline{h}_{0}\right\rangle_{\mathbf{e h}} d v_{\mathbf{e h}}+\frac{1}{2} \lim _{r \rightarrow+\infty} \int_{\left\{r_{\mathbf{e}}=r\right\}}\left\langle\nabla_{\partial_{r \mathbf{e}}}\left(\underline{h}_{2}\right), \underline{h}_{0}\right\rangle_{\mathbf{e h}}-\left\langle\underline{h}_{2}, \nabla_{\partial_{r \mathbf{e}}} \underline{h}_{0}\right\rangle_{\mathbf{e h}} d v_{\left\{r_{\mathbf{e}}=r\right\}} \\
0 & =-3 \int_{\mathbb{S}^{3} / \mathbb{Z}_{2}}\left\langle H_{2}, H_{0}^{4}\right\rangle_{\mathbf{e}} d v_{\mathbb{S}^{3} / \mathbb{Z}_{2}}-\int_{\mathbb{S}^{3} / \mathbb{Z}_{2}}\left\langle H_{2}^{4}, H_{0}\right\rangle_{\mathbf{e}} d v_{\mathbb{S}^{3} / \mathbb{Z}_{2}},
\end{aligned}$$
where we used that by homogeneity, we have $\nabla_{\partial_{r_{\mathbf{e}}}} H_{2}=\frac{2}{r_{\mathbf{e}}} H_{2}, \nabla_{\partial_{r_{\mathbf{e}}}} H_{0}=0, \nabla_{\partial_{r_{\mathbf{e}}}} H_{2}^{4}=$ $-\frac{2}{r_{\mathrm{e}}} H_{2}^{4}$ and $\nabla_{\partial_{r_{\mathrm{e}}}} H_{0}^{4}=-\frac{4}{r_{\mathrm{e}}} H_{0}^{4}$.

Finally, if $\lambda_{k}=0$, using the fact that $H_{2}^{4}=0$ from Lemma 2.3, we find:
$$\int_{\mathbb{S}^{3} / \mathbb{Z}_{2}}\left\langle H_{2}, H_{0}^{4}\right\rangle_{\mathbf{e}} d v_{\mathbb{S}^{3} / \mathbb{Z}_{2}}=0$$ \(\square\)
2.1.2. A first obstruction on the orbifold. We have a similar result for the extension of tensors on the orbifold. Consider an infinitesimal Ricci-flat variation of $\mathbf{e h}_{\zeta_{j}^{ \pm}}$in the direction $\mathbf{o}_{m}=\mathbf{o}_{m}\left(\zeta_{j}^{ \pm}\right) \in \mathbf{O}\left(\mathbf{e h}_{\zeta_{j}^{ \pm}}\right)$where $\mathbf{o}_{m}\left(\zeta_{j}^{ \pm}\right)$is the 2-tensor defined in (16) and Remark 1.20. In particular, $\mathbf{o}_{m}$ has a development $\mathbf{o}_{m}=O_{m}^{4}+\mathcal{O}\left(|\zeta|^{3} r_{\mathbf{e}}^{-8}\right)$ with $\left|O_{m}^{4}\right|_{\mathbf{e}} \sim|\zeta| r^{-4}$.

Lemma 2.9. We define $\overline{\mathbf{o}}_{m}^{4}$ for $m \in\{1,2,3\}$ some solutions to the following equation
$$\left\{\begin{array}{l}
P_{o} \overline{\mathbf{o}}_{m}^{4} \in \mathbf{O}\left(\mathbf{g}_{o}\right), \\
\quad \overline{\mathbf{o}}_{m}^{4}=O_{m}^{4}+\mathcal{O}\left(r_{o}^{-2-\epsilon}\right) \text { for any } \epsilon>0 \text { at the singular point } j \\
\quad \overline{\mathbf{o}}_{m}^{4} \perp \mathbf{O}\left(\mathbf{g}_{o}\right) .
\end{array}\right.$$
They are determined up to the kernel of $P_{\mathbf{g}_{o}}$ in $\mathcal{O}\left(r_{\mathbf{e}}^{-2}\right)$ at the singular points and this choice will not alter the result at this level of precision.

Proof. Let us consider a cut-off function $\chi$ on $M_{o}$ supported in a small enough neighborhood of a singular point $p$. We have $P_{\mathbf{g}_{o}}\left(\chi O_{m}^{4}\right)=\mathcal{O}\left(r^{-4}\right)$, hence there exists a 2 tensor $\left|O_{m, 2}^{4}\right|=\mathcal{O}\left(r^{-2-\epsilon}\right)$ so that
$$P_{\mathbf{g}_{o}}\left(\chi\left(O_{m}^{4}+O_{m, 2}^{4}\right)\right)=\mathcal{O}\left(r^{-2-\epsilon}\right) .$$
Finally, using the Fredholm properties of $P_{\mathbf{g}_{o}}$ proven in [Ozu19b], there exists $\left|h^{\prime}\right|=\mathcal{O}\left(r^{-\epsilon}\right)$ for all $\epsilon>0$ so that:
$$P_{\mathbf{g}_{o}}\left(\chi\left(O_{m}^{4}+O_{m, 2}^{4}\right)+h^{\prime}\right) \in \mathbf{O}\left(\mathbf{g}_{o}\right) .$$

Now, we can uniquely choose it by imposing $\left(\chi\left(O_{m}^{4}+O_{m, 2}^{4}\right)+h^{\prime}\right) \perp_{L^{2}\left(\mathbf{g}_{o}\right)} \mathbf{O}\left(\mathbf{g}_{o}\right)$, where the $L^{2}$ product is a priori ill-defined as in the proof of Lemma 2.7, but makes sense via the orthogonality of the different eigenspaces of the Laplacian on $\mathbb{R P}^{3}$. \(\square\)

Proposition 2.10. Let us denote $\left(\mathbf{v}_{l}\right)_{l}$ an orthonormal basis of $\mathbf{O}\left(\mathbf{g}_{o}\right)$. Consider the development of the symmetric 2-tensor $\underline{h}_{2}=H_{2}+H_{2}^{4}+\mathcal{O}\left(r_{\mathbf{e}}^{-6+\epsilon}\right)$ of (22) (again, we will omit the dependence in $\zeta^{ \pm}$).

For $\zeta^{ \pm} \in \Omega^{ \pm}$and the symmetric 2-tensor $H^{4}=H^{4}\left(\zeta^{ \pm}\right)$with $P_{\mathbf{e}} H^{4}=0$ and $B_{\mathbf{e}} H^{4}=0$, there exists $\left(\bar{h}^{4},\left(\nu_{l}\right)_{l}\right)$ with a symmetric 2-tensor $\bar{h}^{4}$ and real numbers $\left(\nu_{l}\right)_{l}$ on $M_{o}$ satisfying the following equations
$$\left\{\begin{aligned}
P_{o} \bar{h}^{4} & =\sum_{l} \nu_{l} \mathbf{v}_{l}+\sum_{k} \lambda_{k} \overline{\mathbf{o}}_{k}^{4} \\
\bar{h}^{4} & =H^{4}+H_{2}^{4}+\mathcal{O}\left(|\zeta|^{2} r_{o}^{-\epsilon}\right) \text { for any } \epsilon>0 \text { at the singular point } j \\
\bar{h}^{4} & \perp \mathbf{O}\left(\mathbf{g}_{o}\right)
\end{aligned}\right.$$

We moreover have the following value for the obstruction when $\lambda_{k}=0$ for $k \in\{1,2,3\}$
$$\nu_{l}=3 \int_{\mathbb{S}^{3} / \mathbb{Z}_{2}}\left\langle H^{4}, V_{l, 2}\right\rangle_{\mathbf{e}} d v_{\mathbb{S}^{3} / \mathbb{Z}_{2}} .$$
where we have $\mathbf{v}_{l}=V_{l, 0}+V_{l, 2}+\mathcal{O}\left(r_{\mathbf{e}}^{4}\right)$ with $\left|V_{l, m}\right|_{\mathbf{e}} \sim r_{\mathbf{e}}^{m}$.
Remark 2.11. The next term in the development of $\bar{h}^{4}$ is $H_{4}^{4}$ with $\left|H_{4}^{4}\right|_{\mathbf{e}}=\mathcal{O}\left(r_{\mathbf{e}}^{\epsilon}+r_{\mathbf{e}}^{-\epsilon}\right)$ for any $\epsilon>0$ (it will typically be logarithmic in $r_{\mathbf{e}}$ ) for which we have
$$\bar{h}^{4}=H^{4}+H_{2}^{4}+H_{4}^{4}+\mathcal{O}\left(|\zeta|^{2} r_{o}^{2-\epsilon}\right) .$$
It satisfies
$$P_{\mathbf{e}} H_{4}^{4}+Q_{\mathbf{e}}^{(2)}\left(H^{4}, H_{4}\right)+Q_{\mathbf{e}}^{(2)}\left(H_{2}^{4}, H_{2}\right)+Q_{\mathbf{e}}^{(3)}\left(H^{4}, H_{2}, H_{2}\right)=0 .$$
for $Q_{\mathbf{e}}^{(m)}$ the $m$-linear terms of the development of $h \mapsto\left(\operatorname{Ric}-\Lambda+\delta_{\mathbf{e}+h}^{*} B_{\mathbf{e}}\right)(\mathbf{e}+h)$ around $h=0$. The equality (37) is exactly the equation satisfied by the next term in the development of $\underline{h}_{4}$ defined in (21) or (23). That was what made $\underline{h}_{4}$ non unique: one could add any element of the kernel of $P_{\mathbf{e h}}$ asymptotic to a constant 2-tensor to it. We can make it unique (and still existing) by imposing that we have for the above $H_{4}^{4}$ :
$$\underline{h}_{4}=H_{4}+H_{4}^{4}+\mathcal{O}\left(r^{-2+\epsilon}\right) .$$

Proof. Consider $\chi$ a cut-off function supported in the neighborhood of the singular point $j \in M_{o}$. From $P_{\mathbf{e}} H^{4}=0, r_{\mathbf{e}}^{k}\left|\nabla_{\mathbf{e}}^{k}\left(\mathbf{g}_{o}-\mathbf{e}\right)\right|_{\mathbf{e}}=\mathcal{O}\left(r_{\mathbf{e}}^{2}\right)$ and using (26), we find
$$P_{o}\left(\chi\left(H^{4}+H_{2}^{4}\right)\right)-\sum_{k} \lambda_{k} \overline{\mathbf{o}}_{k}^{4} \in r_{o}^{-2} C_{\beta}^{\alpha}\left(\mathbf{g}_{o}\right)$$
for $0<\beta<1$ where the norms are defined in the Appendix A.
Moreover, by integration by parts and using $\overline{\mathbf{o}}_{k}^{4} \perp_{L^{2}\left(\mathbf{g}_{o}\right)} \mathbf{O}\left(\mathbf{g}_{o}\right)$, we find
$$\begin{aligned}
\int_{M_{o}}\langle & \left.P_{o}\left(\chi\left(H^{4}+H_{2}^{4}\right)\right), \mathbf{v}_{l}\right\rangle_{\mathbf{g}_{o}} d v_{\mathbf{g}_{o}} \\
= & \int_{M_{o}}\left\langle\chi\left(H^{4}+H_{2}^{4}\right), P_{o}\left(\mathbf{v}_{l}\right)\right\rangle_{\mathbf{g}_{o}} d v_{\mathbf{g}_{o}} \\
& +\frac{1}{2} \lim _{r \rightarrow 0} \int_{\left\{r_{o}=r\right\}}\left\langle\nabla_{\partial_{r_{o}}}\left(\chi H^{4}\right), \mathbf{v}_{l}\right\rangle_{\mathbf{g}_{o}}-\left\langle\chi H^{4}, \nabla_{\partial_{r_{o}}} \mathbf{v}_{l}\right\rangle_{\mathbf{g}_{o}} d v_{\left\{r_{o}=r\right\}} \\
& +\frac{1}{2} \lim _{r \rightarrow 0} \int_{\left\{r_{o}=r\right\}}\left\langle\nabla_{\partial_{r_{o}}}\left(\chi H_{2}^{4}\right), \mathbf{v}_{l}\right\rangle_{\mathbf{g}_{o}}-\left\langle\chi H_{2}^{4}, \nabla_{\partial_{r_{o}}} \mathbf{v}_{l}\right\rangle_{\mathbf{g}_{o}} d v_{\left\{r_{o}=r\right\}} \\
= & 3 \int_{\mathbb{S}^{3} / \mathbb{Z}_{2}}\left\langle H^{4}, V_{l, 2}\right\rangle_{\mathbf{e}} d v_{\mathbb{S}^{3} / \mathbb{Z}_{2}}+\int_{\mathbb{S}^{3} / \mathbb{Z}_{2}}\left\langle H_{2}^{4}, V_{l, 0}\right\rangle_{\mathbf{e}} d v_{\mathbb{S}^{3} / \mathbb{Z}_{2}}
\end{aligned}$$
Indeed, since once restricted to $\mathbb{S}^{3} / \mathbb{Z}_{2}$, the coefficients of $H^{4}$ and $V_{l, 0}$ are eigenfunctions of the Laplace-Beltrami operator and associated to different eigenvalues, the product against the first asymptotic term $V_{l, 0}$ vanishes. Note that this also justifies the orthogonality of (35). For the second term $V_{l, 2}$, we use the homogeneity of $H^{4}$ and $V_{l, 2}$ which yield $\nabla_{\partial_{r_{\mathrm{e}}}} H^{4}=-\frac{4}{r_{\mathrm{e}}} H^{4}$ and $\nabla_{\partial_{r_{\mathrm{e}}}} V_{l, 2}=\frac{2}{r_{\mathrm{e}}} V_{l, 2}$ and the above value. Thanks to the Fredholm properties of $P_{o}$ proved in [Ozu19b], we have the stated result.

When $\lambda_{k}=0$ for $k \in\{1,2,3\}$, then, we can use Lemma 2.3, hence plug $H_{2}^{4}=0$ into (38) and find the expected value. \(\square\)

Similarly, if $\left(M_{o}, \mathbf{g}_{o}\right)$ has several $\mathbb{R}^{4} / \mathbb{Z}_{2}$ singularities, denote $\bar{h}_{j}^{4}$ the symmetric 2-tensors of (35) asymptotic to $H^{4}\left(\zeta_{j}^{ \pm}\right)+H_{2}^{4}\left(\zeta_{j}^{ \pm}\right)$at the singular point $j$. The symmetric 2-tensor
$$\bar{h}^{4}:=\sum_{j \text { singular }} \bar{h}_{j}^{4}$$
satisfies
$$\left\{\begin{aligned}
& P_{o} \bar{h}^{4}=\sum_{k} \nu_{l} \mathbf{v}_{l}+\sum_{j} \sum_{k} \lambda_{k}^{j} \overline{\mathbf{o}}_{j, k}^{4}, \\
& \bar{h}^{4}=H^{4}\left(\zeta_{j}^{ \pm}\right)+H_{2}^{4}\left(\zeta_{j}^{ \pm}\right)+\mathcal{O}\left(r_{o}^{-\epsilon}\right) \text { for any } \epsilon>0 \text { at each singular point } j \\
& \bar{h}^{4} \perp \mathbf{O}\left(\mathbf{g}_{o}\right) .
\end{aligned}\right.$$
2.1.3. First variation of the initial obstruction. By [Ozu19b, Proposition 5.17], around a singular point $j$, in coordinates where $\mathbf{g}_{o}=\mathbf{e}+H_{j, 2}+\mathcal{O}\left(r_{\mathbf{e}}^{4}\right)$, for $v \in \mathbf{O}\left(\mathbf{g}_{o}\right)$ small enough and with $v=V_{j, 0}+V_{j, 2}+\mathcal{O}\left(r_{\mathbf{e}}^{4}\right)$ in the same coordinates, we have
$$\mathbf{g}_{v}=\left(\mathbf{e}+\tilde{V}_{j, 0}\right)+\left(H_{j, 2}+\tilde{V}_{j, 2}\right)+\mathcal{O}\left(r_{\mathbf{e}}^{4}\right),$$
with $\tilde{V}_{j, 0}=V_{j, 0}+\mathcal{O}\left(\|v\|_{L^{2}\left(\mathbf{g}_{o}\right)}^{2}\right)$ and $\tilde{V}_{j, 2}=V_{j, 2}+\mathcal{O}\left(\|v\|_{L^{2}\left(\mathbf{g}_{o}\right)}^{2} r_{\mathbf{e}}^{2}\right)$. We also denote $\psi\left(\tilde{V}_{j, 0}\right)$ : $\mathbb{R}^{4} / \mathbb{Z}_{2} \rightarrow \mathbb{R}^{4} / \mathbb{Z}_{2}$ the linear isomorphism for which $\psi\left(\tilde{V}_{j, 0}\right)^{*} \mathbf{e}=\mathbf{e}+\tilde{V}_{j, 0}$.

For $k \in\{1,2,3\}$ and a singular point $j$, and $\zeta=\left(\zeta_{j}\right)_{j}$ with $\zeta_{j} \in \mathbb{R}^{3} \backslash\{0\}$, we will denote $\lambda_{k}^{j}(\zeta, v)$ the real numbers of (28) obtained for $H_{0}=\tilde{V}_{j, 0}$ and $H_{2}=H_{j, 2}+\tilde{V}_{j, 2}$, that is for $c>0$,
$$\lambda_{k}^{j}(\zeta, v)=c\left\langle\mathbf{R}^{ \pm}\left(\psi\left(\tilde{V}_{j, 0}\right)_{*}\left(H_{j, 2}+\tilde{V}_{j, 2}\right)\right) \zeta_{j}^{ \pm}, \zeta_{j,(k)}^{ \pm}\right\rangle .$$

We find a link between the variations of the first obstruction $\lambda_{1}$ on the Eguchi-Hanson metric and the first obstructions $\nu_{l}$ on the orbifold.

Corollary 2.12. Consider ( $M_{o}, \mathbf{g}_{o}$ ) an integrable Einstein orbifold with only $\mathbb{R}^{4} / \mathbb{Z}_{2}$ singularities. Consider also a small enough $v \in \mathbf{O}\left(\mathbf{g}_{o}\right)$, the orthonormal basis $\left(\mathbf{v}_{l}\right)_{l}$ of Proposition 2.10 and the Einstein deformation $\mathbf{g}_{v}$ of $\mathbf{g}_{o}$ of Definition 1.10. Assume that we have $\lambda_{k}^{j}(\zeta, 0)=0$ for all $k, j$.

Then, for some constant $C \in \mathbb{R}^{*}$, we have the following control:
$$\sum_{j \text { singular }}\left|\zeta_{j}\right| \lambda_{1}^{j}(\zeta, v)=C \sum_{l}\left\langle v, \mathbf{v}_{l}\right\rangle \nu_{l}(\zeta, 0)+\mathcal{O}\left(\|v\|_{L^{2}}^{2}|\zeta|^{2}\right),$$
where the $\nu_{l}$ are real numbers of (39), and where $|\zeta|=\max _{j}\left|\zeta_{j}\right|$.
Proof. Let $\left(M_{o}, \mathbf{g}_{o}\right)$ be like in the statement above and consider a small enough $v \in \mathbf{O}\left(\mathbf{g}_{o}\right)$ and $\mathbf{g}_{v}$ the Einstein deformation of $\mathbf{g}_{o}$ of Definitions 1.9 and 1.10, denote $\lambda_{1}^{j}(\zeta, v)$ the constant in (40) above. Our goal is to show that the first variation of $v \mapsto \sum_{j}\left|\zeta_{j}\right| \lambda_{1}^{j}(\zeta, v)$ around $(\zeta, 0)$ is proportional to $\sum_{k}\left\langle v, \mathbf{v}_{l}\right\rangle \nu_{l}(\zeta, 0)$.

From the expression (40) and the formula [Biq13, Proposition 3.2], we see that for the singular point $j$, the first variation of $v \mapsto \sum_{j}\left|\zeta_{j}\right| \lambda_{1}^{j}(\zeta, v)$ is
$$\sum_{j}\left|\zeta_{j}\right| \int_{\mathbb{S}^{3} / \mathbb{Z}_{2}}\left\langle V_{2}, O_{j, 1}^{4}\right\rangle_{\mathbf{e}} d v_{\mathbb{S}^{3} / \mathbb{Z}_{2}}$$
up to a multiplicative constant. Using the equality $H^{4}\left(\zeta_{j}^{ \pm}\right)=\frac{\left|\zeta_{j}\right|}{2} O_{j, 1}^{4}\left(\zeta_{j}^{ \pm}\right)$together with (39), we see that this equals $\sum_{k}\left\langle v, \mathbf{v}_{l}\right\rangle \nu_{l}$ up to a multiplicative constant and the estimate (41) follows. \(\square\)
2.1.4. Values for the second obstruction. Let $H_{2}$ be a quadratic symmetric 2-tensor with $P_{\mathbf{e}} H_{2}=\Lambda \mathbf{e}$, and $H_{4}$ with $\left|H_{4}\right|_{\mathbf{e}} \sim r_{\mathbf{e}}^{4}$ and $P_{\mathbf{e}} H_{4}=\Lambda H_{2}-Q_{\mathbf{e}}^{(2)}\left(H_{2}, H_{2}\right)$, and recall the notation $\mathbf{R}^{+}\left(H_{2}\right)$ as the common selfdual part of the curvature at $r_{\mathbf{e}}=0$ of Riemannian metrics with a development $\mathbf{e}+H_{2}+\mathcal{O}\left(r_{\mathbf{e}}^{3}\right)$. As seen above, we have $\lambda_{k}:=c\left\langle\mathbf{R}^{+}\left(H_{2}\right)\left(\omega_{1}^{+}\right), \omega_{k}^{+}\right\rangle$ for the $\lambda_{k}$ of (20) and $c>0$. In particular, if for all $k, \lambda_{k}=0$, then we have
$$\mathbf{R}^{+}\left(H_{2}\right)=\left[\begin{array}{ccc}
0 & 0 & 0 \\
0 & R_{22} & R_{23} \\
0 & R_{32} & R_{33}
\end{array}\right],$$
and in this case, for a positive constant $C>0$, by [Biq16, Lemme 9] we have
$$\mu_{1}=C \operatorname{det}\left[\begin{array}{ll}
R_{22} & R_{23} \\
R_{32} & R_{33}
\end{array}\right]$$

Remark 2.13. If $\operatorname{Ric}\left(H_{2}\right)=0$, then we have $\operatorname{tr}^{+}\left(H_{2}\right)=0$ and therefore
$$\operatorname{det}\left[\begin{array}{ll}
R_{22} & R_{23} \\
R_{32} & R_{33}
\end{array}\right] \leqslant 0$$
with equality if and only if $\mathbf{R}^{+}\left(H_{2}\right)=0$.
In general, we might only know that the $\lambda_{k}$ are small rather than exactly vanishing. We still have the following estimate.

Lemma 2.14. Let $H_{2}$ and $H_{4}$ be homogeneous symmetric 2-tensors as above. We have
$$\mu_{1}=C \operatorname{det}\left[\begin{array}{ll}
R_{22} & R_{23} \\
R_{32} & R_{33}
\end{array}\right]+\mathcal{O}\left(\sum_{k}\left|\lambda_{k}\right| \cdot\left|r_{e}^{-2} H_{2}\right|_{g_{e}}\right) .$$

Proof. According to [Biq16, Lemma 7], we have
$$\mathbf{R}^{+}\left(H_{2}\right)=\left[\begin{array}{ccc}
c^{-1} \lambda_{1} & c^{-1} \lambda_{2} & c^{-1} \lambda_{3} \\
c^{-1} \lambda_{2} & R_{22} & R_{23} \\
c^{-1} \lambda_{3} & R_{32} & R_{33}
\end{array}\right] .$$
Exactly like in the proof of [Biq16, Lemma 8], we use the expression of $Q_{e}^{(2)}$ given in Biq16, Lemma 3] in order to express $\mu_{1}$. The value of $\mu_{1}$ is a quadratic form in the coefficients of $\mathbf{R}^{+}\left(H_{2}\right)$. It is composed of products of a $\lambda_{k}$ and a $\lambda_{j}$, products of the $\lambda_{k}$ with the remaining $R_{i j}$, and its last part involving $R_{22}, R_{23}, R_{32}$ and $R_{33}$ is
$$C \operatorname{det}\left[\begin{array}{ll}
R_{22} & R_{23} \\
R_{32} & R_{33}
\end{array}\right],$$
as proven in [Biq16, Lemma 8]. Since all of the $\lambda_{k}$ as well as the $R_{i j}$ are linear in $H_{2}$ and are therefore are controlled by $\left|r_{e}^{-2} H_{2}\right|_{g_{e}}$. We deduce the stated estimate. \(\square\)

For another Eguchi-Hanson metric $\mathbf{e h}_{\zeta^{ \pm}}$, one has similar estimates with the matrix expression of $\mathbf{R}^{+}\left(H_{2}\right)$ in the basis $\left(\zeta^{ \pm},|\zeta| \cdot \zeta_{(2)}^{ \pm},|\zeta| \cdot \zeta_{(3)}^{ \pm}\right)$on $\mathbb{R} \cdot \zeta^{ \pm}$and its orthogonal. Note that in that case, we have $\lambda_{k} \sim|\zeta|$ and $\mu_{1} \sim|\zeta|^{2}$.
2.2. Approximate Einstein metrics and obstructions. Let ( $M_{o}, \mathbf{g}_{o}$ ) be a compact Einstein orbifold with integrable Einstein deformations and only $\mathbb{R}^{4} / \mathbb{Z}_{2}$ singularities. For $v \in \mathbf{O}\left(\mathbf{g}_{o}\right)$ small enough and $\zeta=\left(\zeta_{j}^{ \pm}\right)_{j}$ with $\zeta_{j} \in \mathbb{R}^{3} \backslash\{0\}$, we recall the notations:
\begin{itemize}
\item[(1)] $\mathbf{g}_{v}$ the Einstein deformation of $\mathbf{g}_{o}$ of Definition 1.10,
\item[(2)] for a singular point $j$, symmetric 2-tensors $\underline{h}_{j, 2}(v, \zeta)$ and $\underline{h}_{j, 4}(v, \zeta)$ of (22) and (23) by extending the asymptotic terms of $\mathbf{g}_{v}$ on $\mathbf{e h}_{\zeta_{j}^{ \pm}}$and
\item[(3)] a symmetric 2-tensor $\bar{h}^{4}(v, \zeta)$ of (39) extending the $r^{-4}$ term of $\mathbf{e h}_{\zeta_{j}^{ \pm}}$on $\left(M_{o}, \mathbf{g}_{v}\right)$.
\item[(4)] $g^{D}$ or $g^{D}$ for the naïve desingularization and $r_{D}$ the associated radial parameter, see Definitions 1.23 and 1.22
\end{itemize}

Definition 2.15 (Approximate Einstein modulo obstructions metric $g_{\zeta, v}^{A}$ ). We define an approximate Einstein modulo obstructions metric $g_{\zeta, v}^{A}$ as the naïve gluing of the metrics $\mathbf{e h}_{\zeta_{j}^{ \pm}}+\underline{h}_{j, 2}(v, \zeta)+\underline{h}_{j, 4}(v, \zeta)$ at the singular points $j$ of $\left(M_{o}, \mathbf{g}_{v}+\bar{h}^{4}(v, \zeta)\right)$.

There exists $C=C\left(\mathbf{g}_{o}\right)>0$ such that we have
\begin{itemize}
\item[-] $r_{D}^{k}\left|\nabla_{\mathbf{e h}_{\zeta_{j}^{ \pm}}}^{k} \underline{h}_{2}\right| \leqslant C r_{D}^{2}$,
\item[-] $r_{D}^{k}\left|\nabla_{\mathbf{e h}_{\zeta_{j}^{ \pm}}}^{k} h_{4}\right| \leqslant C r_{D}^{4}$, and
\item[-] $r_{D}^{k}\left|\nabla_{\mathbf{e h}_{\zeta_{j}^{+}}}^{k} \bar{h}^{4}\right| \leqslant C|\zeta|^{2} r_{D}^{-4}$,
\end{itemize}
we have the following controls: on $M_{o}(\epsilon)$ (defined in (5))
$$r_{D}^{k}\left|\nabla^{k}\left(g_{\zeta, v}^{A}-g_{\zeta, v}^{D}\right)\right|_{g_{\zeta, v}^{D}} \leqslant C|\zeta|^{2},$$
and on the connected component of $M \backslash M_{o}(\epsilon)$ containing the singular point $j \in S$ :
$$r_{D}^{k}\left|\nabla^{k}\left(g_{\zeta, v}^{A}-g_{\zeta, v}^{D}\right)\right|_{g_{\zeta, v}^{D}} \leqslant C\left(\mathbb{1}_{\left\{r_{D}>\left|\zeta_{j}\right|^{\frac{1}{4}}\right\}}\left|\zeta_{j}\right|^{2} r_{D}^{-4}+\mathbb{1}_{\left\{r_{D}<2\left|\zeta_{j}\right|^{\frac{1}{4}}\right\}} r_{D}^{2}\right) .$$
where $\mathbb{1}_{A}$ is the indicator function for $A$.
We now approximate the kernel of the linearization of the Einstein operator at $g_{\zeta, v}^{A}$.

Definition 2.16 (Approximate obstructions $\tilde{\mathbf{O}}\left(g_{\zeta, v}^{A}\right)$ ). We define $\tilde{\mathbf{O}}\left(g_{\zeta, v}^{A}\right)$ the linear space spanned by the infinitesimal variations of $(v, \zeta) \mapsto g_{\zeta, v}^{A}$.

More precisely for the element $\mathbf{o}_{k} \in \mathbf{O}\left(\mathbf{e h}_{\zeta_{j}^{ \pm}}\right)$with $\mathbf{o}_{k}=\partial_{\zeta_{j,(k)}} \mathbf{e h}_{\zeta_{j}^{ \pm}}$, we define
$$\tilde{\mathbf{o}}_{k}:=\partial_{\zeta_{j,(k)}} g_{\zeta, v}^{A}$$
and, for $\mathbf{w} \in \mathbf{O}\left(\mathbf{g}_{v}\right)$, we define $\tilde{\mathbf{w}}$ the associated infinitesimal deformation of $v \mapsto g_{\zeta, v}^{A}$.
Remark 2.17. As in Remark 1.25, the space $\tilde{\mathbf{O}}\left(g_{\zeta, v}^{A}\right)$ is very close to the space $\tilde{\mathbf{O}}\left(g_{\zeta, v}^{D}\right)$ of [Ozu19b] and even yields better estimate. The results of [Ozu19b] therefore hold when replacing $\tilde{\mathbf{O}}\left(g_{\zeta, v}^{D}\right)$ by $\tilde{\mathbf{O}}\left(g_{\zeta, v}^{A}\right)$.

We have the following estimates which show that the space $\tilde{\mathbf{O}}\left(g_{\zeta, v}^{A}\right)$ is an approximate $L^{2}$-cokernel of the linearization of the Einstein equation.
Lemma 2.18. For $\tilde{\mathbf{o}}_{k} \in \tilde{\mathbf{O}}\left(g_{\zeta, v}^{A}\right)$ and $\tilde{\mathbf{w}} \in \tilde{\mathbf{O}}\left(g_{\zeta, v}^{A}\right)$ as in Definition 2.16 above, we have for any symmetric 2-tensor $h$ on $M$,
$$\begin{gathered}
\left|\left\langle P_{g_{\zeta, v}^{D}} h, \tilde{\mathbf{o}}_{k}\right\rangle_{L^{2}\left(g_{\zeta, v}^{D}\right)}\right| \leqslant C|\zeta| \cdot\|h\|_{C_{\beta, *}^{2, \alpha}\left(g_{\zeta, v}^{D}\right)}\left\|\mathbf{o}_{k}\right\|_{L^{2}\left(\mathbf{e h}_{\zeta_{j}^{ \pm}}\right)} \text {and } \\
\left|\left\langle P_{g_{\zeta, v}^{D}} h, \tilde{\mathbf{w}}\right\rangle_{L^{2}\left(g_{\zeta, v}^{D}\right)}\right| \leqslant C|\zeta| \cdot\|h\|_{C_{\beta, *}^{2, \alpha}\left(g_{\zeta, v}^{D}\right)}\|\mathbf{w}\|_{L^{2}\left(\mathbf{g}_{o}\right)}
\end{gathered}$$
Proof. By integration by parts and symmetry of $P_{g_{\zeta v}^{D}}$ on the closed manifold $M$, it is equivalent to control
$$\int_{M}\left\langle h, P_{g_{\zeta, v}^{D}} \tilde{\mathbf{o}}_{k}\right\rangle_{g_{\zeta, v}^{D}} d v_{g_{\zeta, v}^{D}} \text { and } \int_{M}\left\langle h, P_{g_{\zeta, v}^{D}} \tilde{\mathbf{w}}\right\rangle_{g_{\zeta, v}^{D}} d v_{g_{\zeta, v}^{D}} .$$

On the region where $g_{\zeta, v}^{D}=\mathbf{e h}_{\zeta_{j}^{ \pm}}$, we have $P_{g_{\zeta, v}^{D}} \tilde{\mathbf{o}}_{k}=0$. There remains the region where $g_{\zeta, v}^{D}=\mathbf{g}_{v}$ on which by differentiating (39) with respect to $\zeta_{j}^{ \pm}$, we find
$$P_{g_{\zeta, v}^{D}} \tilde{\mathbf{o}}_{k}=\sum_{l} \partial_{\zeta_{j,(k)}} \nu_{l} \mathbf{w}_{l}+\sum_{i, m} \partial_{\zeta_{j,(k)}}\left(\lambda_{i}^{m} \overline{\mathbf{o}}_{i, m}^{4}\right),$$
where $\left(\mathbf{w}_{l}\right)_{l}$ denotes an orthonormal basis of $\mathbf{O}\left(\mathbf{g}_{v}\right)$, and where the $\partial_{\zeta_{j,(k)}} \nu_{l}$ are the derivatives of the $\nu_{l}=\nu_{l}(v, \zeta)$ of (39) in the direction $\zeta_{j,(k)}$. Given the expressions (24), (16) and (39), that gives for some $C=C\left(\mathbf{g}_{o}\right)>0$,
$$\left\|P_{g_{\zeta, v}^{D}} \tilde{\mathbf{o}}_{k}\right\|_{L^{2}\left(\mathbf{e h}_{\zeta_{j}^{ \pm}}\right)} \leqslant C|\zeta| \cdot\left\|\mathbf{o}_{k}\left(\zeta_{j}^{ \pm}\right)\right\|_{L^{2}\left(\mathbf{e h}_{\zeta_{j}^{ \pm}}\right)} .$$
We find that
$$\int_{\left\{r_{D}>2\left|\zeta_{j}^{ \pm}\right|^{1 / 4}\right\}}\left\langle h, P_{g_{\zeta, v}^{D}} \tilde{\mathbf{o}}_{k}\right\rangle_{g_{\zeta, v}^{D}} d v_{g_{\zeta, v}^{D}} \leqslant C|\zeta| \cdot\|h\|_{C^{0}\left(g_{\zeta, v}^{D}\right)}\left\|\mathbf{o}_{k}\left(\zeta_{j}^{ \pm}\right)\right\|_{L^{2}\left(\mathbf{e h}_{\zeta_{j}^{ \pm}}\right)} .$$

Finally, on the gluing region where $\left|\zeta_{j}^{ \pm}\right|^{\frac{1}{4}}<r_{D}<2\left|\zeta_{j}^{ \pm}\right|^{\frac{1}{4}}$, we have for all $l \in \mathbb{N}$ and $C_{l}>0$
$$r_{D}^{l}\left|\nabla^{l}\left(g_{\zeta, v}^{D}-\mathbf{e h}_{\zeta_{j}^{ \pm}}\right)\right|_{g_{\zeta, v}^{D}} \leqslant C_{l}\left(\left|\zeta_{j}^{ \pm}\right|^{2} r_{D}^{-4}+r_{D}^{2}\right)$$
and
$$r_{D}^{l}\left|\nabla^{l}\left(\tilde{\mathbf{o}}_{k}-\mathbf{o}_{k}\right)\right|_{g_{\zeta, v}^{D}} \leqslant C\left(\left|\zeta_{j}^{ \pm}\right|^{4} r_{D}^{-8}+\left|\zeta_{j}^{ \pm}\right|^{2} r_{D}^{-2}\right),$$
and we find that on the gluing region where $\left|\zeta_{j}^{ \pm}\right|^{\frac{1}{4}}<r_{D}<2\left|\zeta_{j}^{ \pm}\right|^{\frac{1}{4}}$, we have
$$\begin{aligned}
\left|P_{g_{\zeta, v}^{D}} \tilde{\mathbf{o}}_{k}\right|_{g_{\zeta, v}^{D}} & \leqslant\left|P_{g_{\zeta, v}^{D}}\left(\tilde{\mathbf{o}}_{k}-\mathbf{o}_{k}\right)\right|_{g_{\zeta, v}^{D}}+\left|\left(P_{g_{\zeta, v}^{D}}-P_{\mathbf{e h}_{\zeta_{j}^{ \pm}}}\right)\left(\mathbf{o}_{k}\right)\right|_{g_{\zeta, v}^{D}} \\
& \leqslant C\left|\zeta_{j}^{ \pm}\right| \cdot\left\|\mathbf{o}_{k}\right\|_{L^{2}\left(\mathbf{e h}_{\zeta_{j}^{ \pm}}\right)} .
\end{aligned}$$

We therefore globally find the estimate (46).
For the second estimate, note first that on the region where $g_{\zeta, v}^{D}=\mathbf{g}_{v}$, we have
$$P_{g_{\zeta, v}^{D}} \mathbf{w}=0,$$
and by a similar argument to the above one, by differentiating (22) and (23), on each region where $g_{\zeta, v}^{D}=\mathbf{e h}_{\zeta_{j}^{ \pm}}$, we have
$$P_{g_{\zeta, v}^{D}} \tilde{\mathbf{w}}=\sum_{k} \partial_{\mathbf{w}}\left(\lambda_{k}+\mu_{k}\right) \mathbf{o}_{k}\left(\zeta_{j}^{ \pm}\right),$$
and we find that there exists $C=C\left(\mathbf{g}_{o}\right)>0$ such that $\left|\partial_{\mathbf{w}}\left(\lambda_{k}+\mu_{k}\right)\right| \leqslant C|\zeta|$. Together with a control on the gluing region like the above one, one obtains the estimate (47). \(\square\)

Proposition 2.19. Assume that there exists an Einstein metric $\mathbf{g}_{\zeta, v}$ satisfying:
\begin{itemize}
\item[(1)] $\mathbf{\Phi}_{g_{\zeta, v}^{D}}\left(\mathbf{g}_{\zeta, v}\right)=0$,
\item[(2)] $\mathbf{g}_{\zeta, v}-g_{\zeta, v}^{A} \perp \tilde{\mathbf{O}}\left(g_{\zeta, v}^{A}\right)$
\item[(3)] $\left\|\mathbf{g}_{\zeta, v}-g_{\zeta, v}^{A}\right\|_{C_{\beta, *}^{2, \alpha}\left(g_{\zeta, v}^{D}\right)}<\epsilon$ for $\epsilon>0$ small enough determined in Ozu19b depending only on $\mathbf{g}_{o}$.
\end{itemize}

Then, we actually have for all $l$ for the obstructions of (35):
$$\nu_{l}=\mathcal{O}\left(|\zeta|^{\frac{5}{2}}\right),$$
and for each $j$, and all $k \in\{1,2,3\}$ for the obstructions of (22) and (23):
$$\lambda_{k}^{j}+\mu_{k}^{j}=\mathcal{O}\left(\left|\zeta_{j}\right|^{\frac{5}{2}}\right) .$$
Proof. Let us denote $\left.\pi_{\tilde{\mathbf{O}}\left(g_{\zeta, v}^{A}\right)}\right)^{\perp}$ the $L^{2}\left(g_{\zeta, v}^{A}\right)$-orthogonal projection on $\tilde{\mathbf{O}}\left(g_{\zeta, v}^{A}\right)^{\perp}$. Thanks to the obstruction result of [Ozu20t, Proposition 5.1], we only have to understand the value of $\left\|\pi_{\tilde{\mathbf{O}}\left(g_{\zeta, v}^{A}\right)^{\perp}} \boldsymbol{\Phi}_{g_{\zeta, v}^{D}}\left(g_{\zeta, v}^{A}\right)\right\|_{r_{D}^{-2} C^{\alpha}\left(g_{\zeta, v}^{D}\right)}$, in order to control both $\left\|g_{\zeta, v}^{A}-\mathbf{g}_{\zeta, v}\right\|_{C_{\beta, *}^{2, \alpha}\left(g_{\zeta, v}^{D}\right)}$ and the obstructions, where the norms are defined in Definition A. 3 in the Appendix.

The estimate on the different Eguchi-Hanson regions has been done in Biq13. Section 14]. There remains to understand the orbifold region. Using the definition of $\bar{h}^{4}$, we control the first variation
$$P_{\mathbf{g}_{o}} \bar{h}^{4}=\sum_{l} \nu_{l} \mathbf{v}_{l}+\sum_{j} \sum_{k=1}^{3} \lambda_{k}^{j} \overline{\mathbf{o}}_{j, k}^{4},$$
and on the region where $g_{\zeta, v}^{A}=\mathbf{g}_{o}+\bar{h}^{4}$ with $\bar{h}^{4}=\mathcal{O}\left(|\zeta|^{2} r_{D}^{-4}\right)$, we have:
$$\mathbf{\Phi}_{g_{\zeta, v}^{D}}\left(g_{\zeta, v}^{A}\right)=\sum_{l} \nu_{l} \mathbf{v}_{l}+\sum_{j} \sum_{k=1}^{3} \lambda_{k}^{j} \overline{\mathbf{o}}_{j, k}^{4}+\mathcal{O}\left(|\zeta|^{4} r_{D}^{-10}\right)$$
which is exactly analogous to the estimate [Biq13, (108)]. The gluing region is treated exactly as in [Biq13, Section 14] for instance, see also the above proof of Lemma 2.18. We conclude like in [Biq13, (109)] that
$$\left\|\pi_{\tilde{\mathbf{O}}\left(g_{\zeta, v}^{A}\right)^{\perp}} \boldsymbol{\Phi}_{g_{\zeta, v}^{D}}\left(g_{\zeta, v}^{A}\right)\right\|_{r_{D}^{-2} C^{\alpha}\left(g_{\zeta, v}^{D}\right)} \leqslant C|\zeta|^{\frac{3}{2}-\frac{\beta}{4}} .$$
We conclude exactly like in order to prove [Biq13, (112)] that we have the stated control (see also [Ozu20t, Proposition 5.1]). \(\square\)
2.3. A new obstruction to the desingularization of Einstein orbifolds. By Ozu19a, [Ozu19b], we know that Einstein metrics which are close to an Einstein orbifold $\left(M_{o}, \mathbf{g}_{o}\right)$ result from a gluing-perturbation procedure. To prove that it cannot be desingularized, we just need to prove that an obstruction to this procedure does not vanish.
2.3.1. Approximate obstructions. Let us denote $\zeta=t \cdot \phi$ with $t=\left(t_{j}\right)_{j}=\left(\left|\zeta_{j}\right|\right)_{j}$ and $\phi=\left(\phi_{j}\right)_{j}=\left(\zeta_{j}^{ \pm} /\left|\zeta_{j}\right|\right)_{j}$. By Proposition 2.19, we find the following estimate for any singular point $j$, any $k \in\{1,2,3\}$ :
$$\begin{gathered}
t_{j} \lambda_{k}^{j}\left(\phi_{j}, v\right)+t_{j}^{2} \mu_{k}^{j}\left(\phi_{j}, v\right)=\mathcal{O}\left(t_{\max }^{\frac{5}{2}}\right), \text { and } \\
\nu_{l}(t \cdot \phi, v)=\mathcal{O}\left(t_{\max }^{\frac{5}{2}}\right), \text { for each } l
\end{gathered}$$
where the $\lambda_{k}^{j}\left(\phi_{j}, v\right)$ and $\mu_{k}^{j}\left(\phi_{j}, v\right)$ and $\nu_{l}(t \cdot \phi, v)$ are the constants of Lemma (22), (23) and (39) for each $\mathbf{e h}_{\zeta_{j}^{ \pm}}$associated to the development of $\mathbf{g}_{v}$ at the singular point $j$.

Our goal is to prove that for all $j$, both all of the $\lambda_{k}^{j}$ and $\mu_{1}^{j}$ have to vanish when $t \rightarrow 0$. The main concern is to rule out the compensation of $t_{j}^{2} \mu_{1}^{j}$ by $t_{j} \lambda_{1}^{j}$ just like in the desingularization case of [Biq13, Theorem 14.3].

Proof of Theorem 0.2 and Proposition 0.4. Let us consider $\left(M_{o}, \mathbf{g}_{o}\right) \in \overline{\mathbf{E}}_{(M)}{ }_{G H}$ for $M$ having the topology of $M_{o}$ desingularized by $T^{*} \mathbb{S}^{2}$ in an orientation at each of its singular point and assume that $\mathbf{g}_{o}$ only has integrable Einstein deformations (see Definition 1.10). Let us assume that there exists a sequence of Einstein metrics $\left(M, \mathbf{g}_{n}\right)_{n}$ desingularizing $\left(M_{o}, \mathbf{g}_{o}\right)$. We will discuss at the end of the proof in which situation we shall assume that this sequence is nondegenerate, transverse or stable.

Then, by [Ozu19a, Ozu19b], there exists a sequence of naïve desingularizations $g_{\zeta_{n}, v_{n}}^{D}$ such that the metrics $\left(M, \mathbf{g}_{n}\right)$ are Einstein perturbations of $g_{\zeta_{n}, v_{n}}^{D}$ with $\zeta_{n}=\left(\zeta_{n, j}\right)_{j}$. We will use the notations $t_{n}=\left(t_{n, j}\right)_{j}$, with $t_{n, j}=\left|\zeta_{n, j}\right|>0$ and $\phi_{n}=\left(\phi_{n, j}\right)_{j}, \phi_{n, j}=\frac{\zeta_{n, j}^{ \pm}}{\left|\zeta_{n, j}\right|}$ satisfying $\zeta_{n, j}^{ \pm}=t_{n, j} \cdot \phi_{n, j}$, and we will denote $t_{n} \cdot \phi_{n}=\left(t_{n, j} \phi_{n, j}\right)_{j}$.

By compactness, up to taking a subsequence, we can assume that for any $j, \phi_{n, j} \rightarrow \phi_{\infty, j}$ on the sphere while $t_{n} \rightarrow 0$ and $v_{n} \rightarrow 0$ since by assumption the limit is $\mathbf{g}_{o}$.

Denote $\lambda_{k}^{j}\left(\phi_{n, j}, v_{n}\right)$ and $\mu_{k}^{j}\left(\phi_{n, j}, v_{n}\right)$ the real numbers of (20) and (21) for these configurations. According to (51), we have the following controls: for all $j$ and $k$,
$$t_{n, j} \lambda_{k}^{j}\left(\phi_{n, j}, v_{n}\right)+t_{n, j}^{2} \mu_{k}^{j}\left(\phi_{n, j}, v_{n}\right)=\mathcal{O}\left(t_{n, \max }^{\frac{5}{2}}\right) .$$

The first obstruction of [Biq13, Ozu19b] means that at the limit, for any singular point $j$, we have $\lambda_{k}^{j}\left(\phi_{\infty, j}, 0\right)=0$ for $k \in\{1,2,3\}$, there exists a basis of the selfdual or anti-selfdual (depending on the orientation of the gluing) 2-forms starting with $\phi_{\infty, j}=\lim _{j \rightarrow+\infty} \zeta_{n, j}^{ \pm} /\left|\zeta_{n, j}\right|$ in which we have
$$\mathbf{R}_{g_{o}}^{ \pm}(j)=\left[\begin{array}{ccc}
0 & 0 & 0 \\
0 & a_{2}^{j} & 0 \\
0 & 0 & a_{3}^{j}
\end{array}\right] .$$

Our goal is to prove that for all $j$ we have, $\mu_{1}^{j}\left(\phi_{\infty, j}, 0\right)=0$. By Lemma (2.14), this will then imply that either $a_{2}^{j}=0$ or $a_{3}^{j}=0$ in (54).

Assume towards a contradiction that both $a_{2}^{j} \neq 0$ and $a_{3}^{j} \neq 0$. Let us use the variations of the $\phi \mapsto \lambda_{k}^{j}(\phi, 0)$ computed in [Biq13, Lemma 12.2] at $\phi_{\infty, j}$, we first have the controls:
$$\lambda_{1}^{j}\left(\phi_{n, j}, 0\right)=\mathcal{O}\left(\left|\phi_{n, j}-\phi_{\infty, j}\right|^{2}\right),$$
because the first variation of the smooth map $\phi \mapsto \lambda_{1}^{j}(\phi, 0)$ vanishes at $\phi_{\infty, j}$. Similarly since we assumed towards a contradiction that $a_{2}^{j} \neq 0$ and $a_{3}^{j} \neq 0$, there exists $c>0$ depending on $\left(a_{2}^{j}, a_{3}^{j}\right)$, so that
$$\left|\left(\lambda_{2}^{j}\left(\phi_{n, j}, 0\right), \lambda_{3}^{j}\left(\phi_{n, j}, 0\right)\right)\right| \geqslant c\left|\phi_{n, j}-\phi_{\infty, j}\right|,$$
since the first order variations of $\phi \mapsto\left(\lambda_{2}^{j}(\phi, 0), \lambda_{3}^{j}(\phi, 0)\right)$ is invertible at $\phi_{\infty, j}$. For the variations induced by $v_{n} \in \mathbf{O}\left(\mathbf{g}_{o}\right)$, for any $k \in\{1,2,3\}$, from the expression (40), we have
$$\left|\lambda_{k}^{j}\left(\phi_{n, j}, v_{n}\right)-\lambda_{k}^{j}\left(\phi_{n, j}, 0\right)\right|=\mathcal{O}\left(\left\|v_{n}\right\|_{L^{2}\left(\mathbf{g}_{o}\right)}\right) .$$
For the $\mu_{k}^{j}$, we have the control $\mu_{k}^{j}\left(\phi_{n, j}, v_{n}\right)=\mu_{k}^{j}\left(\phi_{\infty, j}, 0\right)+\mathcal{O}\left(\left|\phi_{n, j}-\phi_{\infty, j}\right|\right)+\mathcal{O}\left(\left\|v_{n}\right\|_{L^{2}\left(\mathbf{g}_{o}\right)}\right)$. Therefore for $k=2$ or $k=3$, (53) gives
$$t_{n, j} \lambda_{k}^{j}\left(\phi_{n, j}, v_{n}\right)=-t_{n, j}^{2}\left(\mu_{k}^{j}\left(\phi_{\infty, j}, v_{n}\right)+\mathcal{O}\left(\left|\phi_{n, j}-\phi_{\infty, j}\right|\right)+\mathcal{O}\left(\left\|v_{n}\right\|_{L^{2}\left(\mathbf{g}_{o}\right)}\right)\right)+\mathcal{O}\left(t_{n, \max }^{\frac{5}{2}}\right) .$$
At any singular point $j$, we must therefore have $\left|\left(\lambda_{2}^{j}\left(\phi_{n, j}, v_{n}\right), \lambda_{3}^{j}\left(\phi_{n, j}, v_{n}\right)\right)\right|=\mathcal{O}\left(t_{n, j}+\right.$ $\frac{t_{n, \text { max }}^{5 / 2}}{t_{n, j}}$ ), and by (56), this implies that $\left|\phi_{n, j}-\phi_{\infty, j}\right|=\mathcal{O}\left(\left\|v_{n}\right\|_{L^{2}\left(\mathbf{g}_{o}\right)}+t_{n, j}+\frac{t_{n, \text { max }}^{5 / 2}}{t_{n, j}}\right)$.
\begin{itemize}
\item[(1)] In the transverse (Definition 1.27) situation, where we have $t_{n, \max }=\mathcal{O}\left(t_{n, j}\right)$ and $\left\|v_{n}\right\|_{L^{2}\left(\mathbf{g}_{o}\right)}=o\left(t_{n, \text { min }}\right)$. By rewriting (53) for $k=1$, including the bound (55) with the new information that $\left|\phi_{n, j}-\phi_{\infty, j}\right|=\mathcal{O}\left(t_{n, j}\right)$ and using $\mid \lambda_{1}\left(\phi_{\infty, j}, v_{n, j}\right)-$ $\lambda_{1}\left(\phi_{\infty, j}, 0\right) \mid=\mathcal{O}\left(\left\|v_{n, j}\right\|_{L^{2}\left(\mathbf{g}_{o}\right)}\right)=o\left(t_{n, \min }\right)$, we consequently find
$$o\left(t_{n, j}^{2}\right)+t_{n, j}^{2}\left(\mu_{1}^{j}\left(\phi_{\infty, j}, 0\right)+\mathcal{O}\left(\left|\phi_{n, j}-\phi_{\infty, j}\right|\right)+\mathcal{O}\left(\left\|v_{n}\right\|_{L^{2}\left(\mathbf{g}_{o}\right)}\right)\right)=\mathcal{O}\left(t_{n, \max }^{\frac{5}{2}}\right),$$
and therefore $\mu_{1}^{j}\left(\phi_{\infty, j}, 0\right)=0$.
\item[(2)] As proven in [Biq17], Proof of Theorem 3], and thanks to the estimate (50), we know that the linearization of Ric in Bianchi gauge at $\mathbf{g}_{n}$ denoted $P_{\mathbf{g}_{n}}$, satisfies for some $o_{n, j, k} \in L^{2}\left(\mathbf{g}_{n}\right)$ (constructed from $\mathbf{o}_{n, j, k} \in \mathbf{O}\left(\mathbf{e h}_{\zeta_{n, j}}\right)$ ) for $k \in\{1,2,3\}$ :
$$\begin{gathered}
\left\langle P_{\mathbf{g}_{n}} o_{n, j, 1}, o_{n, j, 1}\right\rangle_{L^{2}\left(\mathbf{g}_{n}\right)}=o(1) \cdot\left\|o_{n, j, 1}\right\|_{L^{2}\left(\mathbf{g}_{n}\right)} \text {, and } \\
\left\langle P_{\mathbf{g}_{n}} o_{n, j, k}, o_{n, j, k}\right\rangle_{L^{2}\left(\mathbf{g}_{n}\right)}=\left(a_{k}^{j}+o(1)\right) \cdot\left\|o_{n, j, k}\right\|_{L^{2}\left(\mathbf{g}_{n}\right)}
\end{gathered}$$
for $k \in\{2,3\}$. That means that the metric cannot be stable as in Definition 1.11 if $a_{2}^{j}=-a_{3}^{j} \neq 0$. Consequently, we necessarily have $a_{2}^{j}=a_{3}^{j}=0$ for stable Ricci-flat desingularizations.
\item[(3)] If the orbifold satisfies $\mathbf{O}\left(\mathbf{g}_{o}\right)=\{0\}$ and only has one $\mathbb{R}^{4} / \mathbb{Z}_{2}$ singularity, then the transversality assumption is automatically satisfied and the result follows.
\item[(4)] In the Ricci-flat situation, then the nondegeneracy assumption is enough because we can use Remark 2.13. Indeed, first, the nondegeneracy assumption gives $\mid \phi_{n, j}-$ $\phi_{\infty, j} \left\lvert\,=o\left(t_{n, j}^{\frac{1}{2}}\right)\right.$, hence $\left|\lambda_{1}\left(\phi_{n, j}, 0\right)\right|=o\left(t_{n, j}\right)$ by (55); second from (41), we moreover have a better control over the sum of the $t_{j}^{2} \lambda_{1}^{j}(\zeta, v)$, namely:
$$\sum_{j} t_{j}^{2} \lambda_{1}^{j}\left(\phi_{n, j}, v_{n}\right)-t_{j}^{2} \lambda_{1}^{j}\left(\phi_{n, j}, 0\right)=\mathcal{O}\left(t_{\max }^{\frac{5}{2}}\left\|v_{n}\right\|_{L^{2}\left(\mathbf{g}_{o}\right)}\right)+\mathcal{O}\left(t_{\max }^{2}\left\|v_{n}\right\|_{L^{2}\left(\mathbf{g}_{o}\right)}^{2}\right) .$$
which together with (55) and (51) and using $\left\|v_{n}\right\|_{L^{2}\left(\mathbf{g}_{o}\right)}^{2}=o\left(t_{n, j}\right)$ yields the estimate
$$\begin{aligned}
& \sum_{j} o\left(t_{n, j}^{3}+t_{n, \max }^{\frac{5}{2}} t_{n, j}^{\frac{1}{2}}+t_{n, \max }^{2} t_{n, j}\right) \\
& \quad+\sum_{j} t_{n, j}^{3}\left(\mu_{1}^{j}\left(\phi_{\infty, j}, 0\right)+\mathcal{O}\left(\left|\phi_{n, j}-\phi_{\infty, j}\right|\right)+\mathcal{O}\left(\left\|v_{n}\right\|_{L^{2}\left(\mathbf{g}_{o}\right)}\right)\right)=\mathcal{O}\left(t_{n, j} t_{n, \max }^{\frac{5}{2}}\right),
\end{aligned}$$
\end{itemize}
\begin{itemize}
\item[] which with $t_{n, \text { max }}=\mathcal{O}\left(t_{n, j}\right)$ from the nondegeneracy assumption implies that
$$\sum_{j} \mu_{1}^{j}\left(\phi_{\infty, j}, 0\right)=0$$
and since all of the $\mu_{1}^{j}\left(\phi_{\infty, j}, 0\right)$ are nonpositive by Remark 2.13, for any $j$, we have $\mu_{1}^{j}\left(\phi_{\infty, j}, 0\right)=0$.
\item[(5)] Similarly for Einstein but non Ricci-flat orbifolds with only one singularity, we use (41) as in the previous point since there is only one term in the sum.
\end{itemize}

Remark 2.20. The estimate (52) also implies that: for any $l$, one has
$$\lim _{n \rightarrow+\infty} \nu_{l}\left(\frac{t_{n}}{t_{n, \max }} \cdot \phi_{n}, v_{n}\right)=\lim _{n \rightarrow+\infty} \frac{\nu_{l}\left(t_{n} \cdot \phi_{n}, v_{n}\right)}{t_{n, \max }^{2}}=0$$
which has an interpretation in terms of curvature, at least when the infinitesimal Einstein deformations vanish at the singular points by (39) and (41). \(\square\)

Remark 2.21. The same obstruction result also holds if we consider desingularizations by smooth Ricci-flat ALE of $A_{1}, D_{k}$ or $E_{k}$ singularities by [Biq16, Lemme 9]. An obstruction is also satisfied for $A_{k}$ singularities but it also involves derivatives of the curvature [Biq16, Lemme 12]. It also extends to Kähler Ricci-flat ALE manifolds by taking their hyperkähler finite cover.

We also believe that the nondegeneracy assumption is purely technical. Understanding higher order obstructions should yield the following conjectural statement which already holds under a stability assumption.

Conjecture 2.22. Let $\left(M_{n}, \mathbf{g}_{n}\right)_{n}$ be a sequence of compact smooth Ricci-flat metrics converging in the Gromov-Hausdorff sense towards a Ricci-flat orbifold $\left(M_{o}, \mathbf{g}_{o}\right)$ while bubbling Eguchi-Hanson metrics. Then the curvature of $\mathbf{g}_{o}$ at its singular points is either selfdual or anti-selfdual depending on the orientation of the Eguchi-Hanson metrics.

\section*{3. Ricci-flat modulo obstructions desingularizations of $\mathbb{T}^{4} / \mathbb{Z}_{2}$}

Let us now work with the flat orbifold $\mathbb{T}^{4} / \mathbb{Z}_{2}$. We will study the question of whether or not it is possible to desingularize it by Ricci-flat metrics obtained by gluing Eguchi-Hanson metrics in different orientations at its singular points.
3.1. The orbifold $\mathbb{T}^{4} / \mathbb{Z}_{2}$ and its deformations. We define $\mathbb{T}^{4} / \mathbb{Z}_{2}$ as the quotient of $\mathbb{R}^{4} /\left(2 L \mathbb{Z}^{4}\right)$ for some $L \in G L(4, \mathbb{R})$ by the action of $\{\mathrm{Id},-\mathrm{Id}\}$. A metric on $\mathbb{T}^{4} / \mathbb{Z}_{2}$ can be seen as an $2 L \mathbb{Z}^{4}$-invariant and $\mathbb{Z}_{2}$-invariant metric on $\mathbb{R}^{4}$. It is therefore determined by its values on any cube $L\left([a, a+1]^{4}\right)$ for $a \in \mathbb{R}$. We will denote $\left(\mathbb{T}^{4} / \mathbb{Z}_{2}, \mathbf{g}_{L}\right)$ the orbifold obtained with the matrix $L$.

All of the infinitesimal Ricci-flat deformations of a flat $\mathbb{T}^{4} / \mathbb{Z}_{2}$ are integrable. More precisely, all of the Ricci-flat deformations of $\mathbb{T}^{4} / \mathbb{Z}_{2}$ are flat and can be seen as either varying the above invertible matrix $L$, or as modifying the scalar product, that is by adding a constant symmetric 2-tensor of norm smaller than 1 to the metric $\mathbf{g}_{L}$.

This orbifold has 16 singular points with $\mathbb{R}^{4} / \mathbb{Z}_{2}$ singularities. We will denote
$$S:=\left\{L\left(\epsilon_{1}, \epsilon_{2}, \epsilon_{3}, \epsilon_{4}\right), \epsilon_{i} \in\{0,1\}\right\}+2 \mathbb{Z}^{4}$$
its singular set on $\mathbb{R}^{4}$ before the taking the quotients by $2 L \mathbb{Z}^{4}$ and $\{\mathrm{Id},-\mathrm{Id}\}$.
Remark 3.1. Since this orbifold is flat, it clearly satisfies our obstruction (0.2).
3.2. Partial hyperkähler desingularizations and estimates. In the rest of the article, we consider $\left(M, g_{L, \zeta}^{D}\right)$ a naïve desingularization of $\left(\mathbb{T}^{4} / \mathbb{Z}_{2}, \mathbf{g}_{L}\right)$ for $L \in G L(4, \mathbb{R})$ by positively oriented Eguchi-Hanson metrics $\left(\mathbf{e h}_{\zeta_{i}^{+}}\right)_{i \in S_{+}}$for $\zeta_{i} \in \mathbb{R}^{3} \backslash\{0\}$ at a subset $S_{+}$of the 16 singular points of $\mathbb{T}^{4} / \mathbb{Z}_{2}$ and by negatively oriented $\left(\mathbf{e h}_{\zeta_{j}^{-}}\right)_{j \in S_{-}}$for $\zeta_{j} \in \mathbb{R}^{3} \backslash\{0\}$ at a subset $S_{-}$of the singular points. We denote $\zeta=\left(\left(\zeta_{i}^{+}\right)_{i \in S_{+}},\left(\zeta_{j}^{-}\right)_{j \in S_{-}}\right)$. We will first be interested in its partial hyperkähler desingularizations obtained by perturbation of the metric only desingularized by Eguchi-Hanson metrics in the same orientation.
3.2.1. Hyperkähler partial desingularizations of $\mathbb{T}^{4} / \mathbb{Z}_{2}$ and approximations. Let us define $\left(M_{ \pm}, g_{ \pm}^{D}\right):=\left(M_{S_{ \pm}}, g_{L, \zeta^{ \pm}}^{D}\right)$ the partial desingularizations where the only points which are desingularized are $S_{ \pm}$by the above Eguchi-Hanson metrics $\left(\mathbf{e h}_{\zeta_{i}^{ \pm}}\right)_{i \in S_{ \pm}}$. They can be perturbed to hyperkähler orbifolds.

Lemma 3.2. Let $g_{ \pm}^{D}:=g_{L, \zeta^{ \pm}}^{D}$ be a naïve desingularization of $\mathbb{T}^{4} / \mathbb{Z}_{2}$ thanks to Eguchi-Hanson metrics (7) glued in the same orientation at some or all singular points.

Then, the Einstein modulo obstructions perturbation of $g_{ \pm}^{D}$, denoted $\mathbf{g}_{ \pm}:=\mathbf{g}_{L, \zeta^{ \pm}}$and defined in [Ozu19b] is hyperkähler.

Sketch of proof. It is well-known (or can be proven from [Don12]) that the moduli space of the Ricci-flat and even hyperkähler (orbifold) metrics on $M_{ \pm}$is of maximal dimension $3\left|S_{ \pm}\right|+9$ which is the same as the space of Ricci-flat modulo obstructions metrics of Ozu19b. Using a connectedness argument similar to that of [Ozu20t, Proposition 5.70] for the moduli space of Kronheimer's gravitational instantons, we conclude that any Einstein modulo obstruction perturbation of a metric $g_{ \pm}^{D}$ is actually Ricci-flat (and even hyperkähler). \(\square\)

To obtain more information about these hyperkähler metrics $\mathbf{g}_{ \pm}$, it suffices to construct metrics which are approximately Ricci-flat by [Ozu19b].

Remark 3.3. We will in particular need to have a good approximation of the Riemannian curvature tensor of $\mathbf{g}_{ \pm}$at the remaining singular points. We will see that we have $\left|\mathbf{R}_{\mathbf{g}_{ \pm}}\right| \sim$ $\left|\zeta^{ \pm}\right|^{2}$, and the previous control (50) in $\mathcal{O}\left(\left|\zeta^{ \pm}\right|^{\frac{3}{2}-\frac{\beta}{4}}\right)$ is not sufficient for our purpose.
3.2.2. Approximation of the partial hyperkähler desingularizations. We want to find good enough approximations to be able to control the curvature of our hyperkähler partial desingularizations. Consider the following construction.

On the orbifold ( $\mathbb{T}^{4} / \mathbb{Z}_{2}, \mathbf{g}_{L}$ ), for any harmonic homogeneous symmetric 2-tensor on $\mathbb{R}^{4} /$ $\mathbb{Z}_{2}$ with $\left|H^{4}\right|_{\mathbf{e}} \sim r_{\mathbf{e}}^{-4}$ and a singular point $i \in S$, we can solve the equation
$$\left\{\begin{aligned}
P_{L} \bar{h}^{4} & =0, \text { and } B_{L} \bar{h}^{4}=0, \\
\bar{h}^{4} & =H^{4}+0+\mathcal{O}\left(r^{-\epsilon}\right) \text { for any } \epsilon>0 \text { at the singular point } i, \\
\bar{h}^{4} & \perp \mathbf{O}\left(\mathbf{g}_{L}\right) .
\end{aligned}\right.$$
somewhat explicitly (notice that there is no obstruction contrarily to (35)). Indeed, as in [BK17], one would expect the periodization of the sum of the symmetric 2-tensors $H$ to be a solution. At $x \in \mathbb{R}^{4}$, this would look like
$$\sum_{a \in \mathbb{Z}^{4}} H^{4}(L(2 a)+x-i) .$$
However except in the most symmetric cases, like the one treated in [BK17], this periodization diverges (it is a sum of terms in $r^{-4}$ over a $\mathbb{Z}^{4}$ grid). One way around it is simply
to substract to each term of the sum the mean value of it over a period, namely, we define
$$\bar{h}^{4}(x)=\sum_{a \in \mathbb{Z}^{4}}\left(H^{4}(L(2 a)+x-i)-H_{a v}^{4}(L, i, 2 a)\right),$$
where $H_{a v}^{4}(L, i, 2 a)$ is the average of $H^{4}(x)$ on the set $i+L\left(2 a+[-1,1]^{4}\right)$. This sum converges because we have $\nabla^{l} H^{4}=\mathcal{O}\left(r_{\mathbf{e}}^{-4-l}\right)$ which is summable on $\mathbb{Z}^{4} \backslash\{0\}$ for $l>0$. In particular, the curvature is summable. Note moreover that, by construction, $\bar{h}^{4}$ of (62) is indeed orthogonal to the infinitesimal deformations of $\mathbf{g}_{L}$ which are constant symmetric 2-tensor and that $B_{\mathbf{g}_{L}} \bar{h}^{4}=0$ as well as $\operatorname{tr}_{\mathbf{g}_{L}} \bar{h}^{4}=0$.

Remark 3.4. The point is that the symmetric 2-tensors we have substracted are constant and therefore, the curvature induced are the same as those of the sum (61).

Let, $H^{4}\left(\zeta_{i}^{ \pm}\right)$for $i \in S_{ \pm}$be the $r^{-4}$-asymptotic terms of the metric $\mathbf{e h}_{\zeta_{i}^{ \pm}}$, see (11). Consider the unique symmetric 2-tensor $\bar{h}^{4}\left(\zeta_{i}^{ \pm}\right)$as in (62) which is asymptotic to $H^{4}\left(\zeta_{i}^{ \pm}\right)$ at $i$ and bounded everywhere else while satisfying $\bar{h}^{4}\left(\zeta_{i}^{ \pm}\right) \perp_{\mathbf{g}_{L}} \mathbf{O}\left(\mathbf{g}_{L}\right)$.

Consider now a singular point $i \in S_{ \pm}$and denote $\left|\zeta^{ \pm}\right|=\max _{i^{\prime} \in S_{ \pm}}\left|\zeta_{i^{\prime}}^{ \pm}\right|$. We have the following expansion of the sum $\sum_{i^{\prime} \neq i} \bar{h}^{4}\left(\zeta_{i^{\prime}}^{ \pm}\right)=H_{0}(i)+H_{2}(i)+\mathcal{O}\left(d(i, .)^{4}\right)$ at $i$ with $\left|H_{0}(i)\right|=\mathcal{O}\left(\left|\zeta^{ \pm}\right|^{2}\right)$ a constant symmetric 2-tensor, and $\left|H_{2}(i)\right|=\mathcal{O}\left(\left|\zeta^{ \pm}\right|^{2}\right) r_{\mathbf{e}}^{2}$. For some linear isomorphism $\phi_{i}$ with, $\left\|\phi_{i}-\mathrm{Id}\right\|=\mathcal{O}\left(\left|\zeta^{ \pm}\right|^{2}\right)$, we have $\mathbf{e}+H_{0}(i)=\phi_{i}^{*} \mathbf{e}$. In the coordinates of (7), the metric $\phi_{i}^{*} \mathbf{e h}_{\zeta_{i}^{ \pm}}$(see Remark 2.6 for the meaning of this action of the diffeomorphism) is asymptotic to $\mathbf{e}+H_{0}(i)$. Consider now $\underline{h}_{2}(i)$ a solution to $P_{\phi_{i}^{*} \mathbf{e} \mathbf{h}_{\zeta_{i}^{ \pm}}} \underline{h}_{2}(i) \in \mathbf{O}\left(\phi_{i}^{*} \mathbf{e h}_{\zeta_{i}^{ \pm}}\right)$, with $\underline{h}_{2}(i)=H_{2}(i)++\mathcal{O}\left(r^{-2+\epsilon}\right)$ for all $\epsilon>0$ from (20). Since the perturbation $\mathbf{g}_{ \pm}$is Ricci-flat, we actually have
$$P_{\phi_{i}^{*} \mathbf{e h}} \zeta_{i}^{ \pm} \underline{h}_{2}(i)=0$$
Note that $\underline{h}_{2}(i)$ it is determined up to $\mathbf{O}\left(\phi_{i}^{*} \mathbf{e h}_{\zeta_{i}^{ \pm}}\right)$. We choose the solution which is orthogonal to $\mathbf{O}\left(\phi_{i}^{*} \mathbf{e h}_{\zeta_{i}^{ \pm}}\right)$for the $L^{2}$-product induced by $\phi_{i}^{*} \mathbf{e h}_{\zeta_{i}^{ \pm}}$on $\mathbb{S}^{2}$ as in (20).

Definition 3.5 (Approximate hyperkähler metric $g_{ \pm}^{A}$ ). We define the approximate hyperkähler metric $g_{ \pm}^{A}$ in a way similar to Definition 1.21): we glue the different $\phi_{i}^{*} \mathbf{e h}_{\zeta_{i}^{ \pm}}+\underline{h}_{2}(i)$ for $i \in S_{ \pm}$to the metric $\mathbf{g}_{L}+\sum_{i \in S_{ \pm}} \bar{h}^{4}\left(\zeta_{i}^{ \pm}\right)$at the points $i \in S_{ \pm}$with cut-off at distance at $\left|\zeta_{i}^{ \pm}\right|^{\frac{1}{6}}$, that is with the following metric on the gluing region:
$$\chi\left(\left|\zeta_{i}^{ \pm}\right|^{-\frac{1}{6}} r_{e}\right)\left(\phi_{i}^{*} \mathbf{e h}_{\zeta_{i}^{ \pm}}+\underline{h}_{2}(i)\right)+\left(1-\chi\left(\left|\zeta_{i}^{ \pm}\right|^{-\frac{1}{6}} r_{e}\right)\right)\left(\mathbf{g}_{L}+\sum_{i \in S_{ \pm}} \bar{h}^{4}\left(\zeta_{i}^{ \pm}\right)\right) .$$
3.2.3. Control of the partial hyperkähler desingularizations. We now justify the qualifier "approximate" for the metric $g_{ \pm}^{A}$.

Proposition 3.6. We have the following control on the metric: for all $k \in \mathbb{N}$, there exists $C=C(k, L)>0$, such that
$$\left\|g_{ \pm}^{A}-\mathbf{g}_{ \pm}\right\|_{C_{\beta, *}^{k}\left(g_{ \pm}^{D}\right)} \leqslant C\left|\zeta^{ \pm}\right|^{2+\frac{2}{3}-\frac{\beta}{6}}$$
In particular, at each remaining singular point $p$, we have
$$\left|\mathbf{R}_{g_{ \pm}^{A}}-\mathbf{R}_{\mathbf{g}_{ \pm}}\right|_{g_{ \pm}^{D}} \leqslant C\left|\zeta^{ \pm}\right|^{2+\frac{2}{3}-\frac{\beta}{6}} .$$

Remark 3.7. We a priori had $\mathbf{R}_{\mathbf{g}_{ \pm}}=\mathcal{O}\left(\left|\zeta^{ \pm}\right|^{2}\right)$ so this is indeed a good approximation of $\mathbf{R}_{\mathbf{g}_{ \pm}}$as $\zeta^{ \pm} \rightarrow 0$. The controls of (50) in $|\zeta|^{\frac{3}{2}-\frac{\beta}{4}}$ are not precise enough here.

Proof. Thanks to [Ozu20t, Proof of Theorem 4.51], it is enough to control the values of $\boldsymbol{\Phi}_{g_{ \pm}^{D}}\left(g_{ \pm}^{A}\right)$ in $r_{D}^{-2} C_{\beta}^{k, \alpha}\left(g_{ \pm}^{D}\right)$ in order to obtain (64), where for two metrics $g$ and $g^{\prime}$, we define
$$\boldsymbol{\Phi}_{g}\left(g^{\prime}\right):=\operatorname{Ric}\left(g^{\prime}\right)+\delta_{g^{\prime}}^{*} B_{g} g^{\prime}$$
as in the first section. Estimates similar to [Biq13, Lemma 14.2] and [BK17, Proposition 3.4], yield the following controls. For all $k \in \mathbb{N}$, there exists $C_{k}>0$ for which for a given singular point $i_{0}$, in the neighborhood of $i_{0}$
\begin{itemize}
\item[(1)] in the region where $r_{D}>2\left|\zeta_{i_{0}}^{ \pm}\right|^{\frac{1}{6}}$, we have $g_{ \pm}^{A}=\mathbf{g}_{L}+\bar{h}^{4}$ and $g_{ \pm}^{D}=\mathbf{g}_{L}$ and therefore, since the linear terms vanish, that is $d_{\mathbf{g}_{L}} \boldsymbol{\Phi}_{\mathbf{g}_{L}} \bar{h}^{4}=0$, the error is at least quadratic. Since $r_{D}^{k}\left|\nabla^{k} \bar{h}^{4}\right|_{g_{ \pm}^{D}} \leqslant C\left|\zeta^{ \pm}\right|^{2} r_{D}^{-4}$, we have
$$r_{D}^{k}\left|\nabla^{k} \mathbf{\Phi}_{g_{ \pm}^{D}}\left(g_{ \pm}^{A}\right)\right|_{g_{ \pm}^{A}} \leqslant C_{k}\left|\zeta^{ \pm}\right|{ }^{4} r_{D}^{-10}$$
\item[(2)] in the region where $r_{D}<\left|\zeta_{i_{0}}^{ \pm}\right|^{\frac{1}{6}}$, we have $g_{ \pm}^{A}=\mathbf{e h}_{\zeta_{i}^{ \pm}}+\underline{h}_{2}$ and $g_{ \pm}^{D}=\mathbf{e h}_{\zeta_{i}^{ \pm}}$. Like above, by (63) we also only have to control the nonlinear terms, and since $r_{D}^{k}\left|\nabla^{k} \underline{h}_{2}\right|_{g_{ \pm}^{D}} \leqslant C\left|\zeta^{ \pm}\right|^{2} r_{D}^{2}$, we find
$$r_{D}^{k}\left|\nabla^{k} \mathbf{\Phi}_{g_{ \pm}^{D}}\left(g_{ \pm}^{A}\right)\right|_{g_{ \pm}^{A}}=\left|\zeta^{ \pm}\right|^{4} r_{D}^{2}$$
\item[(3)] in the region where $\left|\zeta_{i_{0}}^{ \pm}\right|^{\frac{1}{6}}<r_{D}<2\left|\zeta_{i_{0}}^{ \pm}\right|^{\frac{1}{6}}, g_{ \pm}^{A}$ and $g_{ \pm}^{D}$ are respectively an interpolation between $\mathbf{g}_{L}+\bar{h}^{4}$ and $\mathbf{e h}_{\zeta_{i}^{ \pm}}+\bar{h}_{2}$ and an interpolation between $\mathbf{g}_{L}$ and $\mathbf{e h}_{\zeta_{i}^{ \pm}}$ thanks to a cut-off function. Now we have
$$\begin{gathered}
r_{D}^{k}\left|\nabla^{k}\left(\left(\mathbf{g}_{L}+\bar{h}^{4}\right)-\left(\mathbf{e h}_{\zeta_{i}^{ \pm}}+\underline{h}_{2}\right)\right)\right|_{\mathbf{e}} \leqslant C\left|\zeta^{ \pm}\right|^{2} r_{D}^{4}+\left|\zeta^{ \pm}\right|^{4} r_{D}^{-8}, \text { and } \\
r_{D}^{k}\left|\nabla^{k}\left(\mathbf{g}_{L}-\mathbf{e h}_{\zeta_{i}^{ \pm}}\right)\right|_{\mathbf{e}} \leqslant C\left|\zeta^{ \pm}\right|^{2} r_{D}^{2}+\left|\zeta^{ \pm}\right|^{2} r_{D}^{-4}
\end{gathered}$$
and since $\left|\zeta^{ \pm}\right|^{1 / 6}<r_{D}<2\left|\zeta^{ \pm}\right|^{1 / 6}$, by controlling the cut-off function, we find $r_{D}^{2+k}\left|\nabla^{k} \mathbf{\Phi}_{g_{ \pm}^{D}}\left(g_{ \pm}^{A}\right)\right|_{g_{ \pm}^{A}} \leqslant C\left|\zeta^{ \pm}\right|^{2+\frac{2}{3}}$.
\end{itemize}
Finally, since the control is straightforward away from the singular points, we obtain
$$\left\|\boldsymbol{\Phi}_{g_{ \pm}^{D}}\left(g_{ \pm}^{A}\right)\right\|_{r_{D}^{-2} C_{\beta}^{k, \alpha}\left(g_{ \pm}^{D}\right)} \leqslant C\left|\zeta^{ \pm}\right|^{2+\frac{2}{3}-\frac{\beta}{6}},$$
which gives the estimate (64), see the argument of [Ozu20t, Theorem 4.51]. \(\square\)
3.2.4. Approximation of the infinitesimal deformations. Let us approximate the kernel of $P_{\mathbf{g}_{ \pm}}, \mathbf{O}\left(\mathbf{g}_{ \pm}\right)$thanks to the following symmetric 2-tensors.

Definition 3.8. We define $\tilde{\mathbf{O}}\left(g_{ \pm}^{A}\right)$ the linear space spanned by the infinitesimal variations of $\left(L, \zeta^{ \pm}\right) \mapsto g_{ \pm}^{A}=g_{L, \zeta^{ \pm}}^{A}$.

Let us start by recalling a general lemma for operators between Banach spaces which will be useful to approximate the elements of the kernel of our operator on the hyperkähler partial desingularizations.

Lemma 3.9 ([Ozu19b]). Let $P, P^{\prime}: X \rightarrow Y$ be two operators between two Banach spaces $X$ and $Y$ for which there exists $C>0 \frac{1}{100 C}>\epsilon>0$ and a finite-dimensional linear subspace $K^{\prime}$ and $S^{\prime}$ a supplement of $K^{\prime}$ in $X$ such that we have
\begin{itemize}
\item[(1)] for any $x \in X,\left\|\left(P-P^{\prime}\right) x\right\|_{Y} \leqslant \epsilon\|x\|_{X}$,
\item[(2)] for any $x \in S^{\prime},\|x\|_{X} \leqslant C\left\|P^{\prime} x\right\|_{Y}$,
\item[(3)] for any $x \in K^{\prime},\left\|P^{\prime} x\right\|_{Y} \leqslant \epsilon\|x\|_{X}$,
\item[(4)] $\operatorname{dim}(\operatorname{ker} P)=\operatorname{dim}\left(K^{\prime}\right)$.
\end{itemize}

Then, for any element $k^{\prime}$ of $K^{\prime}$, there exists an element $k$ of $\operatorname{ker} P$ such that
$$\left\|k-k^{\prime}\right\|_{X} \leqslant \frac{2 C \epsilon}{1-C \epsilon}\left\|k^{\prime}\right\|_{X}$$ \(\square\)

Proposition 3.10. Let $\mathbf{O}\left(\mathbf{g}_{ \pm}\right)$be the kernel of $P_{\mathbf{g}_{ \pm}}$. Then, for any $\mathbf{o}_{ \pm} \in \mathbf{O}\left(\mathbf{g}_{ \pm}\right)$, there exist $\mathbf{o}_{ \pm}^{A} \in \tilde{\mathbf{O}}\left(g_{ \pm}^{A}\right)$ such that we have
$$\left\|\mathbf{o}_{ \pm}-\mathbf{o}_{ \pm}^{A}\right\|_{C_{\beta, *}^{2, \alpha}\left(g_{ \pm}^{D}\right)} \leqslant C\left|\zeta^{ \pm}\right|^{2+\frac{2}{3}-\frac{\beta}{6}} .$$
Proof. Let us apply Lemma 3.9 with $P=P_{\mathbf{g}_{ \pm}}, P^{\prime}=P_{g_{ \pm}^{A}}, K^{\prime}=\tilde{\mathbf{O}}\left(g_{ \pm}^{D}\right)$ and $S^{\prime}=\tilde{\mathbf{O}}\left(g_{ \pm}^{A}\right)^{\perp}$. We have the following controls: there exists $C>0$ independent of $\left|\zeta^{ \pm}\right|$small enough
\begin{itemize}
\item[(1)] for any $h \in C_{\beta, *}^{2, \alpha}\left(g_{ \pm}^{D}\right)$, by Proposition 3.6, we have
$$\left\|\left(P_{\mathbf{g}_{ \pm}}-P_{g_{ \pm}^{A}}\right) h\right\|_{r_{D}^{-2} C_{\beta}^{\alpha}\left(g_{ \pm}^{D}\right)} \leqslant C\left|\zeta^{ \pm}\right|^{2+\frac{2}{3}-\frac{\beta}{6}}\|h\|_{C_{\beta, *}^{2, \alpha}\left(g_{ \pm}^{D}\right)},$$
\item[(2)] for any $h \in C_{\beta, *}^{2, \alpha}\left(g_{ \pm}^{D}\right) \cap \tilde{\mathbf{O}}\left(g_{ \pm}^{A}\right)^{\perp}$, by [Ozu19b], we have
$$\|h\|_{C_{\beta, *}^{2, \alpha}\left(g_{ \pm}^{D}\right)} \leqslant C\left\|P_{g_{ \pm}^{A}} h\right\|_{r_{D}^{-2} C_{\beta}^{\alpha}\left(g_{ \pm}^{D}\right)},$$
\item[(3)] by an estimation very similar to that of Proposition 3.6, which we therefore omit, for any $\mathbf{o}^{A} \in \tilde{\mathbf{O}}\left(g_{ \pm}^{A}\right)$,
$$\left\|P_{g_{ \pm}^{A}} \mathbf{o}^{A}\right\|_{r_{D}^{-2} C_{\beta}^{\alpha}\left(g_{ \pm}^{D}\right)} \leqslant C\left|\zeta^{ \pm}\right|^{2+\frac{2}{3}-\frac{\beta}{6}}\left\|\mathbf{o}^{A}\right\|_{C_{\beta, *}^{2, \alpha}\left(g_{ \pm}^{D}\right)},$$
\item[(4)] and, $\operatorname{dim} \mathbf{O}\left(\mathbf{g}_{ \pm}\right)=\operatorname{dim} \tilde{\mathbf{O}}\left(g_{ \pm}^{A}\right)$ since every gluing configuration can be perturbed to a Ricci-flat manifold by Lemma 3.2.
\end{itemize}
We can therefore apply Lemma 3.9 and obtain the stated estimate. \(\square\)

Using the control of $\mathbf{o}_{ \pm}$of Proposition 2.19, we moreover have the following estimate of the infinitesimal variation of $\mathbf{R}_{\mathbf{g}}$ in the direction of $\mathbf{o}_{ \pm}$: for $C>0$, we have
$$\left|\partial_{\mathbf{o}_{ \pm}} \mathbf{R}_{\mathbf{g}_{ \pm}}-\partial_{\mathbf{o}_{ \pm}^{A}} \mathbf{R}_{g_{ \pm}^{A}}\right|_{g_{ \pm}^{A}} \leqslant C\left|\zeta^{ \pm}\right|^{2+\frac{2}{3}-\frac{\beta}{6}\left\|\mathbf{o}_{ \pm}\right\|_{L^{2}\left(\mathbf{g}_{ \pm}\right)}}$$
where we denoted $\partial_{\mathbf{o}_{ \pm}} \mathbf{R}_{\mathbf{g}_{ \pm}}$the differential of $\mathbf{g}_{ \pm} \mapsto \mathbf{R}_{\mathbf{g}_{ \pm}}$at $\mathbf{g}_{ \pm}$in the direction $\mathbf{o}_{ \pm}$.
3.3. Total desingularizations modulo obstructions. Let us start by using a notation which will be convenient for this section.

Definition 3.11. For a section $s$ on $\left(\mathbb{R}^{4} / \mathbb{Z}_{2}\right) \backslash\{0\}$, we will write $s \propto r_{\mathbf{e}}^{k}$ if $s \in r_{\mathbf{e}}^{k} C_{-\epsilon}^{l}\left(\mathbb{R}^{4} /\right.$ $\mathbb{Z}_{2}$ ) for all $l \in \mathbb{N}$ and $\epsilon>0$.

For $k \in \mathbb{Z}$ and $f:\left(\mathbb{R}^{3}\right)^{16} \mapsto \mathbb{R}_{*}^{+}$, we will write $s \propto f(\zeta) r_{\mathbf{e}}^{k}$ if as the parameters $\zeta \rightarrow 0$, we have $s=\left(f(\zeta)+o(f(\zeta)) s^{\prime}\right.$ for $s^{\prime} \propto r_{\mathbf{e}}^{k}$.

Remark 3.12. For any $l \geqslant 0$, we have $r_{\mathbf{e}}^{k} \log ^{l}\left(r_{\mathbf{e}}\right) \propto r_{\mathbf{e}}^{k}$.
Let us now consider the total desingularization of the partial hyperkähler desingularizations $\mathbf{g}_{ \pm}$by gluing the Eguchi-Hanson metrics $\mathbf{e h}_{\zeta_{j}^{\mp}}$ at the remaining singular points $j \in S_{\mp}$. Here, the hyperkähler orbifold ( $M_{ \pm}, \mathbf{g}_{ \pm}$) will play the role of ( $M_{o}, \mathbf{g}_{o}$ ) in Section 2. From the obstruction result of Theorem 0.2, we can already say that in order to desingularize the orbifold $\left(M_{ \pm}, \mathbf{g}_{ \pm}\right)$by a nondegenerate sequence of Einstein manifolds in the Gromov-Hausdorff sense, it is necessary that the condition $\mathbf{R}_{\mathbf{g}_{ \pm}}=0$ is satisfied at every remaining singular point. This was done thanks to an approximate development at order 4, see Definition 2.15.

In this section, we are interested in the more challenging situation of a sequence of desingularization of a sequence of metrics $\mathbf{g}_{ \pm, n}$, and this requires an approximation at an even higher order.
3.3.1. An approximate Einstein modulo obstructions metric. Let $L \in G L(4, \mathbb{R})$ and $\zeta=$ $\left(\left(\zeta_{i}^{ \pm}\right)_{i \in S_{ \pm}},\left(\zeta_{j}^{\mp}\right)_{j \in S_{\mp}}\right) \in\left(\mathbb{R}^{3}\right)^{\left|S_{ \pm}\right|} \times\left(\mathbb{R}^{3}\right)^{\left|S_{\mp}\right|} \sim\left(\mathbb{R}^{3}\right)^{16}$.

Definition 3.13 (Total desingularizations, $g_{L, \zeta}^{D}$ ). We define $g_{L, \zeta}^{D}$ the naïve gluing at all $j \in S_{\mp}$ of the metrics $\mathbf{e h}_{\zeta_{j}^{\mp}}$ to the metric $\mathbf{g}_{ \pm}$. Recall the notation $\left|\zeta^{ \pm}\right|=\max _{i \in S_{ \pm}}\left|\zeta_{i}\right|$.

As in Section 2, the goal of the present section is to construct better approximate Einstein modulo obstructions metric in order to identify the obstructions.

Proposition 3.14. Let $L_{0} \in G L(4, \mathbb{R})$. Then there exists $C>0$ and a neighborhood $\mathcal{U}$ of $\left(L_{0}, 0\right) \in G L(4, \mathbb{R}) \times\left(\mathbb{R}^{3}\right)^{16}$ such that there exists a smooth family of metrics $\left(g_{L, \zeta}^{A}\right)_{(L, \zeta) \in \mathcal{U}}$ for which if we denote $\tilde{\mathbf{O}}\left(g_{L, \zeta}^{A}\right)$ the space of the infinitesimal deformations of $(L, \zeta) \mapsto g_{L, \zeta}^{A}$, we have
\begin{itemize}
\item[(1)] $\left\|g_{L, \zeta}^{A}-g_{L, \zeta}^{D}\right\|_{C_{\beta, *}^{2, \alpha}\left(g_{L, \zeta}^{D}\right)} \rightarrow 0$ as $\zeta \rightarrow 0$,
\item[(2)] $g_{L, \zeta}^{A}-g_{L, \zeta}^{D} \perp_{L^{2}\left(g_{L, \zeta}^{A}\right)} \tilde{\mathbf{O}}\left(g_{L, \zeta}^{A}\right)$, and
\item[(3)] $\left\|\boldsymbol{\Phi}_{g_{L, \zeta}^{A}}\left(g_{L, \zeta}^{A}\right)-\mathbf{o}_{L, \zeta}^{A}\right\|_{r_{D}^{-2} C_{\beta}^{\alpha}\left(g_{L, \zeta}^{D}\right)} \leqslant C\left|\zeta^{ \pm}\right|^{1+\frac{\beta}{12}}\left|\zeta^{\mp}\right|^{3-\frac{\beta}{4}}$ for $\mathbf{o}_{L, \zeta}^{A} \in \tilde{\mathbf{O}}\left(g_{L, \zeta}^{A}\right)$ explicited in the proof.
\end{itemize}

Let us consider the development of the metric $\mathbf{g}_{ \pm}$at the singular point $j \in S_{\mp}$,
$$\mathbf{g}_{ \pm}=\mathbf{e}+\sum_{m \in \mathbb{N}^{*}} H_{j, 2 m}, \text { with } H_{j, 2 m} \propto\left|\zeta^{ \pm}\right|^{2} r_{\mathbf{e}}^{2 m}$$
by Proposition 3.6, and similarly, for each $j$, at infinity we have
$$\mathbf{e h}_{\zeta_{j}^{\mp}}=\mathbf{e}+\sum_{m \in \mathbb{N}^{*}} H^{4 m}\left(\zeta_{j}^{\mp}\right), \text { with } H^{4 m}\left(\zeta_{j}^{\mp}\right) \propto\left|\zeta^{\mp}\right|^{2 m} r_{\mathbf{e}}^{-4 m} .$$
3.3.2. Extension of the first asymptotic terms. As in Section 2, we define 2-tensors satisfying the following equations for $\left(\mathbf{o}_{j, k}\right)_{k}$ a basis of $\mathbf{O}\left(\mathbf{e h}_{\zeta_{j}^{ \pm}}\right)$and $\lambda_{j}^{k} \in \mathbb{R}$ as in (22):
$$\left\{\begin{array}{c}
P_{\mathbf{e h}_{\zeta_{j}^{\mp}}} \underline{h}_{j, 2}=\sum_{k} \lambda_{k}^{j} \mathbf{o}_{j, k} \\
\underline{h}_{j, 2}=H_{j, 2}+\mathbf{O}\left(\left|\zeta^{ \pm}\right|^{2} \cdot\left|\zeta_{j}^{\mp}\right|^{2} r_{\mathbf{e}}^{-2+\epsilon}\right), \\
\int_{\mathbb{S}^{2}}\left\langle\underline{h}_{j, 2}, \mathbf{o}_{j, k}\right\rangle_{\mathbf{e h}_{\zeta_{j}^{\mp}}} d v_{\mathbf{e h}_{\zeta_{j}^{\mp} \mid \mathbb{S}^{2}}}=0 \text { for all } k \in\{1,2,3\}
\end{array}\right.$$
for $H_{j, 2}$ as in (67) and we have a converging development in a neighborhood of infinity.
$$\underline{h}_{j, 2}=H_{j, 2}+H_{j, 2}^{4}+\sum_{m \geqslant 2} H_{j, 2}^{4 m}, \text { with } H_{j, 2}^{4 m} \propto\left|\zeta^{ \pm}\right|^{2}\left|\zeta^{\mp}\right|^{2 m} r_{\mathbf{e}}^{2-4 m} .$$

We then define the extension of the obstructions $\overline{\mathbf{o}}_{j, m}^{4}$ for $m \in\{1,2,3\}$ as the unique solutions to the following equation as in (34):
$$\left\{\begin{aligned}
P_{\mathbf{g}_{ \pm}} & \overline{\mathbf{o}}_{j, m}^{4} \in \mathbf{O}\left(\mathbf{g}_{o}\right), \\
& \overline{\mathbf{o}}_{j, m}^{4}=O_{j, m}^{4}+\mathcal{O}\left(r_{\mathbf{e}}^{-2-\epsilon}\right) \text { for any } \epsilon>0 \text { at the singular point } j \\
& \overline{\mathbf{o}}_{j, m}^{4} \perp \mathbf{O}\left(\mathbf{g}_{o}\right)
\end{aligned}\right.$$
for $O_{j, m}^{4} \propto\left|\zeta_{j}^{\mp}\right| r_{\mathbf{e}}^{-4}$ and $O_{j, m, 2}^{4} \propto\left|\zeta^{ \pm}\right|^{2}\left|\zeta_{j}^{\mp}\right| r_{\mathbf{e}}^{-2}$ the asymptotic term of the infinitesimal variation of $\underline{h}_{2}$ of (70) as $\mathbf{e h}_{\zeta_{j}^{\mp}}$ is perturbed in the direction $\mathbf{o}_{j, m}$ like in Section 2.

For the first approximation term on $M_{ \pm}$,
$$\left\{\begin{aligned}
P_{\mathbf{g}_{ \pm}} \bar{h}^{4} & =\sum_{k} \lambda_{k}^{j} \overline{\mathbf{o}}_{j, k}^{4}+\sum_{l} \nu_{l} \mathbf{v}_{l} \\
\bar{h}^{4} & =H^{4}\left(\zeta_{j}^{\mp}\right)+H_{j, 2}^{4}+\mathcal{O}\left(\left|\zeta^{ \pm}\right|^{2} \cdot\left|\zeta^{\mp}\right|^{2} r_{\mathbf{e}}^{-\epsilon}\right) \text { for any } \epsilon>0 \text { at the singular point } j \\
\bar{h}^{4} & \perp \mathbf{O}\left(\mathbf{g}_{o}\right)
\end{aligned}\right.$$
for $H^{4}\left(\zeta_{j}^{\mp}\right)$ as in (68) with $H_{j, 2}^{4}$ determined in (70) and we have a converging development
$$\bar{h}^{4}=H^{4}\left(\zeta_{j}^{\mp}\right)+H_{j, 2}^{4}+\sum_{m \geqslant 2} H_{j, 2 m}^{4}$$
in a neighborhood of each singular point $j$, with $H_{j, 2 m}^{4} \propto\left|\zeta_{j}^{\mp}\right|^{2}\left|\zeta^{ \pm}\right|^{2} r_{\mathbf{e}}^{2 m-4}$.
Let us come back to the development (67) of $\mathbf{g}_{ \pm}$at a singular point $j \in S_{\mp}$ and the term $H_{j, 4}$. We know that $H_{j, 4} \propto\left|\zeta^{ \pm}\right|^{2} r_{\mathbf{e}}^{4}$ and satisfies
$$P_{\mathbf{e}} H_{j, 4}+Q_{\mathbf{e}}^{(2)}\left(H_{j, 2}, H_{j, 2}\right)=0 .$$
Since $H_{j, 2} \propto\left|\zeta^{ \pm}\right|^{2} r_{\mathbf{e}}^{2}$, one would therefore expect by homogeneity to have $H_{j, 4} \propto\left|\zeta^{ \pm}\right|^{4} r_{\mathbf{e}}^{4}$ instead of the above $H_{j, 4} \propto\left|\zeta^{ \pm}\right|^{2} r_{\mathbf{e}}^{4}$. The reason is that $H_{j, 4}$ might have a harmonic part in $\left|\zeta^{ \pm}\right|^{2} r_{\mathbf{e}}^{4}$ while its part compensating the quadratic terms in $H_{j, 2}$ is $\propto\left|\zeta^{ \pm}\right|^{4} r_{\mathbf{e}}^{4}$. By Lemma A. 5 in the Appendix, there exists $\stackrel{\circ}{H}_{j, 4}$ such that $\stackrel{\circ}{H}_{j, 4} \propto\left|\zeta^{ \pm}\right|^{2} r_{\mathbf{e}}^{4}$ such that $H_{j, 4}-\stackrel{\circ}{H}_{j, 4} \propto\left|\zeta^{ \pm}\right|^{4} r_{\mathbf{e}}^{4}$ and satisfying $P_{\mathbf{e}} \stackrel{\circ}{H}_{j, 4}=0$. The crucial thing to note is that the extension of the harmonic part $\stackrel{\circ}{H}_{j, 4}$ on $\mathbf{e h}_{\zeta_{j}^{\mp}}$ does not induce any obstruction by Biq16, (25), proof of Lemma 9]. This will ensure that we can indeed "see" the second obstruction $\mu_{j, 1}=0$ for all $j$. More precisely, there exists $\stackrel{\circ}{\underline{h}}_{j, 4}$ for which we have:
$$\left\{\begin{array}{c}
P_{\mathbf{e h}_{\zeta_{j}^{\mp}}} \stackrel{\circ}{\underline{h}}_{j, 4}=0 \\
\stackrel{\circ}{\underline{h}}_{j, 4}=\stackrel{\circ}{H}_{j, 4}+\mathbf{O}\left(\left|\zeta^{ \pm}\right|^{2} \cdot\left|\zeta_{j}^{\mp}\right|^{2} r_{\mathbf{e}}^{\epsilon}\right), \text { for any } \epsilon>0 \\
\int_{\mathbb{S}^{2}}\left\langle\stackrel{\circ}{h}_{j, 4}, \mathbf{o}_{j, k}\right\rangle_{\mathbf{e h}_{\zeta_{j}^{\mp}}} d v_{\mathbf{e h}_{\zeta_{j}^{\mp} \mid \mathbb{S}^{2}}}=0 \text { for all } k \in\{1,2,3\} .
\end{array}\right.$$
We can therefore define the following 2-tensors on each $\left(T^{*} \mathbb{S}^{2}, \mathbf{e h}_{\zeta_{j}^{\mp}}\right)$ :
$$\left\{\begin{array}{c}
P_{\mathbf{e h}_{\zeta_{j}^{\mp}}} \underline{h}_{j, 4}+Q_{\mathbf{e h}_{\zeta_{j}^{\mp}}^{(2)}}\left(\underline{h}_{j, 2}, \underline{h}_{j, 2}\right)=\sum_{k} \mu_{k}^{j} \mathbf{o}_{j, k} \\
\underline{h}_{j, 4}=H_{j, 4}+H_{j, 4}^{4}+\mathbf{O}\left(\left|\zeta^{ \pm}\right|^{2} \cdot\left|\zeta_{j}^{\mp}\right|^{2} r_{\mathbf{e}}^{-2+\epsilon}\right) \text { for any } \epsilon>0, \\
\int_{\mathbb{S}^{2}}\left\langle\underline{h}_{j, 4}, \mathbf{o}_{j, k}\right\rangle_{\mathbf{e h}_{\zeta_{j}^{\mp}}} d v_{\mathbf{e h}_{\zeta_{j}^{\mp \mid \mathbb{S}^{2}}}}=0 \text { for all } k \in\{1,2,3\}
\end{array}\right.$$
where $H_{j, 4}^{4}$ is defined in (73) and satisfies
$$P_{\mathbf{e}} H_{j, 4}^{4}+Q_{\mathbf{e}}^{(2)}\left(H_{j, 4}, H^{4}\left(\zeta_{j}^{\mp}\right)\right)+Q_{\mathbf{e}}^{(2)}\left(H_{j, 2}, H_{j, 2}^{4}\right)+Q_{\mathbf{e}}^{(3)}\left(H_{j, 2}, H_{j, 2}, H^{4}\left(\zeta_{j}^{\mp}\right)\right)=0$$
which ensures that (75) has a unique solution as in Section 2. The coefficients $\mu_{k}^{j}$ are the same as in (23), and one has
$$\left\|\sum_{k} \mu_{k}^{j} \mathbf{o}_{j, k}\right\|_{L^{2}\left(\mathbf{e h}_{\zeta_{j}^{\mp}}\right)}=\mathcal{O}\left(\left|\zeta^{ \pm}\right|^{4}\left|\zeta^{\mp}\right|^{2}\right) .$$
Remark that the factor $\left|\zeta^{ \pm}\right|^{4}$ comes from the previous discussion about extending a harmonic tensor $\stackrel{\circ}{H}_{4}$ and the difference between $H^{4}-\stackrel{\circ}{H}_{4} \propto\left|\zeta^{ \pm}\right|^{4} r_{\mathbf{e}}^{4}$.