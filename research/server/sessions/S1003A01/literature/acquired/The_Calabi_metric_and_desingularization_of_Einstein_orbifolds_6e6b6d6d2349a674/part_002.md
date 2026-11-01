---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: The Calabi metric and desingularization of Einstein orbifolds]

Proof. This is easily proved using a special boundary defining function $x$ such that
$$g=\sinh ^{-2}(x)\left(d x^{2}+g_{x}\right),$$
where $g_{x}$ is an $x$-dependent metric on a slice, and $g_{0}=\bar{g}$. This is proved, for example, in [AD98]. The remainder of the proof is a standard calculation, and is omitted. \(\square\)

We also need the following analytic continuation result for analytic Riemannian manifolds.

Lemma 7.3. Let ( $M^{m}, \partial M, g, x$ ) be $A H E$ and let $P(s)=0$ in some open set $V \subset M$ such that $s=\delta^{*} \alpha$ for some one-form $\alpha$ defined in some open ball $U \subset V$ then $\alpha$ can be analytically continued to a vector field $\tilde{\alpha}$ defined on any simply connected domain $U \subset U_{1} \subset V$ such that $s=\delta^{*} \tilde{\alpha}$. Furthermore, if $V$ contains a punctured ball around $p_{0}$, and $s=O\left(|z|^{\gamma}\right)$ for $\gamma \neq-1$ where $|z|$ is distance to the point $p_{0}$, then $\tilde{\alpha}=O\left(|z|^{\gamma+1}\right)$ as $|z| \rightarrow 0$.

Proof. Since Einstein metrics are real analytic in harmonic coordinates one can use the infinitesimal version of analytic continuation technique (see KN96, Corollary 6.4]) to extend $\alpha$ to a larger domain. We refer to [And08, Lemma 2.6] for a complete proof. Finally, an examination of the proof shows that the solution is obtained by integration, and the last statement follows from this (the details are omitted). \(\square\)

Another crucial result we will need is the following unique continuation theorem due to Biquard.

Theorem 7.4 (Biquard [Biq08]). Let ( $M^{m}, \partial M, g, x$ ) be AHE. If $h \in \Gamma\left(S^{2}\left(T^{*} U\right)\right.$ ), where $U$ is a neighborhood of $\partial M$, is a solution of $d_{g} \operatorname{Ric}(h)=\Lambda h$, and $h$ is in radial gauge (i.e $\left.\partial_{x}\right\lrcorner h=0$ ), such that $|h|_{g}=o\left(x^{m-1}\right)$ as $x \rightarrow 0$, then $h \equiv 0$.

We next define a mapping on 0-germs
$$S_{0}^{\infty}: S_{0}^{2}\left(T_{p_{0}}^{*} M_{0}\right) \rightarrow V_{0},$$
where $V_{0}$ was defined in (6.4). Given a traceless symmetric matrix $a_{i j}$, then there is a unique solution $\tilde{h} \in \Gamma\left(S_{0}^{2}\left(T^{*} M_{0}\right)\right)$ of $P(\tilde{h})=0$ satisfying
$$\tilde{h}=\frac{a_{i j}}{|z|^{m-2}} d z^{i} \odot d z^{j}+O\left(|z|^{3-m}\right)$$
as $|z| \rightarrow 0$, and such that $\tilde{h} \in L^{2}\left(M_{0} \backslash B\left(p_{0}, \epsilon\right)\right)$. The solution is unique since $M_{0}$ is assumed to be non-degenerate. From Proposition 6.1, $\tilde{h}$ admits an expansion
$$\tilde{h}=\sigma_{0} x^{m-1}+o\left(x^{m-1}\right),$$
with $x^{2} \sigma_{0} \in \bar{V}_{0}$, as $x \rightarrow 0$. Since $\tilde{h}$ is unique, the mapping
$$\left.S_{0}^{\infty}\left(a_{i j} d z^{i} \odot d z^{j}\right) \equiv x^{2} \sigma_{0}\right|_{\partial M_{0}}$$
is well-defined. Next, let $E_{0}=\operatorname{Im}\left(S_{0}^{\infty}\right)$. In a similar fashion we can define a mapping on 1-germs
$$S_{1}^{\infty}: F_{1} \otimes S_{0}^{2}\left(T_{p_{0}}^{*} M_{0}\right) \rightarrow E_{0}^{\perp} \subset V_{0}$$
with respect to the $L^{2}$ inner product on $\partial M_{0}$, defined by the following. Given
$$a_{i j k} z^{i} d z^{j} \odot d z^{k} \in F_{1} \otimes S_{0}^{2}\left(T_{p_{0}}^{*} M_{0}\right)$$
then there is a solution $\tilde{h} \in \Gamma\left(S_{0}^{2}\left(T^{*} M_{0}\right)\right)$ of $P(\tilde{h})=0$ satisfying
$$\tilde{h}=\frac{a_{i j k} z^{i}}{|z|^{m}} d z^{j} \odot d z^{k}+O\left(|z|^{2-m}\right)$$
as $|z| \rightarrow 0$, and such that $\tilde{h} \in L^{2}\left(M_{0} \backslash B\left(p_{0}, \epsilon\right)\right)$. Again, from Proposition 6.1 there is an expansion
$$\tilde{h}=\sigma_{0} x^{m-1}+o\left(x^{m-1}\right),$$
where $x^{2} \sigma_{0} \in \bar{V}_{0}$, as $x \rightarrow 0$. Since $\tilde{h}$ is only unique up to the solutions from the $S_{0}^{\infty}$ construction above, the mapping
$$S_{1}^{\infty}\left(a_{i j k} z^{i} d z^{j} \odot d z^{k}\right)=\left.x^{2} \sigma_{0}\right|_{\partial M_{0}}$$
is well-defined modulo the image of $S_{0}^{\infty}$ and therefore gives a well-defined mapping to $E_{0}^{\perp}$. Letting $E_{1}=\operatorname{Im}\left(S_{1}^{\infty}\right)$, in a similar fashion, we may define a mapping on 2-germs
$$S_{2}^{\infty}: S_{0}^{2}\left(\mathbb{R}^{m}\right) \otimes S_{0}^{2}\left(T_{p_{0}}^{*} M_{0}\right) \rightarrow\left(E_{0} \oplus E_{1}\right)^{\perp} .$$
by the following. Given
$$a_{i j k l} z^{i} z^{j} d z^{k} \odot d z^{l} \in F_{2} \otimes S_{0}^{2}\left(T_{p_{0}}^{*} M_{0}\right),$$
then there is a solution $\tilde{h} \in \Gamma\left(S_{0}^{2}\left(T^{*} M_{0}\right)\right)$ of $P(\tilde{h})=0$ satisfying
$$\tilde{h}=\frac{a_{i j k l} z^{i} z^{j}}{|z|^{m+2}} d z^{k} \odot d z^{l}+O\left(|z|^{1-m}\right)$$
as $|z| \rightarrow 0$, and such that $\tilde{h} \in L^{2}\left(M_{0} \backslash B\left(p_{0}, \epsilon\right)\right)$. Again, from Proposition 6.1 there is an expansion
$$\tilde{h}=\sigma_{0} x^{m-1}+o\left(x^{m-1}\right),$$
where $x^{2} \sigma_{0} \in \bar{V}_{0}$ as $x \rightarrow 0$. Since $\tilde{h}$ is only unique up to the solutions from the $S_{0}^{\infty}$ and $S_{1}^{\infty}$ constructions above, the mapping
$$S_{2}^{\infty}\left(a_{i j k l}\right)=\left.x^{2} \sigma_{0}\right|_{\partial M_{0}}$$
is well-defined modulo the image of $S_{0}^{\infty}$ and $S_{1}^{\infty}$ and therefore gives a well-defined mapping to $\left(E_{0} \oplus E_{1}\right)^{\perp}$.

Proposition 7.5. Let $\left(M_{0}^{m}, \partial M_{0}, g, x\right)$ be an AHE orbifold with one singular point $p_{0}$ of type $\Gamma_{n}(m=2 n)$ and non-degenerate. Then we have the following:
\begin{itemize}
\item[(1)] $S_{0}^{\infty}$ is injective.
\item[(2)] $S_{1}^{\infty}$ is injective.
\item[(3)] The kernel of $S_{2}^{\infty}$ is the space of 2-germs of the form $|z|^{m+2} \mathcal{K}_{\text {euc }}\left(\frac{\alpha_{1}}{|z|^{m}}\right)$, where $\alpha_{1}$ is a one-form with linear coefficients. ${ }^{2}$
\end{itemize}

Proof. In any of these cases, let $s$ be the solution from the above construction which is blowing up at the point, and $L^{2}$ in a neighborhood of infinity, so that top $L^{2}$ weight vanishes. By Proposition 6.1, $s$ admits an expansion
$$s=\sigma_{1} x^{m}+o\left(x^{m}\right)$$
where $x^{2} \sigma_{1} \in \bar{V}_{1}$, as $x \rightarrow 0$. A straightforward calculation shows that $B s=o\left(x^{m}\right)$ as $x \rightarrow 0$. By Lemma 6.2, $P_{1}(B s)=0$, so by Proposition 6.1, we must have
$$B s=\alpha_{n} x^{\delta_{1, P_{1}}^{+}}+o\left(x^{\delta_{1, P_{1}}^{+}}\right)$$
where $\alpha_{n} \in \Omega_{n}^{1} \overline{M_{0}}$, as $x \rightarrow 0$. Then, again by the Lemma 6.2 and Proposition 6.1 and the fact that $\delta_{1, P_{1}}^{+}>\delta_{1, P_{2}}^{+}$, we have that $d B s \equiv 0$. We need the following lemma.
Lemma 7.6. The function $f=\delta B s$ satisfies
$$\begin{aligned}
B s & =\frac{1}{\Lambda} d f \\
P_{0}(f) & =0
\end{aligned}$$
Proof. Since $t r_{g} s=0$ and $d B s=0$, using Lemma 6.2, we have
$$d f=d \delta \delta s=\left(\Delta_{H}-\delta d\right) \delta s=\Lambda \delta s-\delta d \delta s=\Lambda \delta s,$$
and (7.18) follows. Lemma 6.2 directly implies (7.19) since $P s=0$. \(\square\)

Letting $\tilde{f}=\frac{2 f}{(2-m) \Lambda}$, from Lemma 7.6, we have that
$$\begin{aligned}
& P(s+\tilde{f} g)=0, \\
& B(s+\tilde{f} g)=0 .
\end{aligned}$$
Consequently,
$$\begin{aligned}
d_{g} R i c(s+\tilde{f} g) & =\Lambda(s+\tilde{f} g), \\
s+\tilde{f} g & =o\left(x^{m-1}\right),
\end{aligned}$$
as $x \rightarrow 0$.
Then by Theorem 7.4 and Lemma 7.2 it follows that
$$s+\tilde{f} g=\delta^{*}(\alpha)$$
for some one-form $\alpha$ defined in a neighborhood of the boundary. Since $\left(M_{0}, g\right)$ is a non-compact and complete Riemannian manifold there exists a geodesic ray $\gamma$ starting

\footnotetext{
${ }^{2}$ The reader should compare this statement with Biq13, Lemma 10.1], from which our conclusion differs.
}
from $p_{0}$ to infinity. Now applying Lemma 7.3 inductively on $\gamma$ we can analytically continue $\alpha$ to a one-form $\tilde{\alpha}$ defined in a neighborhood of $\gamma$ such that
$$s+\tilde{f} g=\delta^{*}(\tilde{\alpha}) .$$
Equivalently,
$$s=\mathcal{K}(\tilde{\alpha}),$$
for a 1-form $\tilde{\alpha}$ satisfying
$$P_{1}(\tilde{\alpha})=0 .$$

In the case of $S_{0}^{\infty}$, let $s$ be the solution of $P s=0$ whose leading term is $|z|^{2-m} h_{0}$ at the point, where $h_{0}$ is a 0-germ at $p_{0}$, and $s=o\left(x^{m-1}\right)$ as $x \rightarrow 0$. Since $s=O\left(|z|^{-m+2}\right)$ around $p_{0}$ and (7.27) is satisfied, by Lemma 7.3, $\tilde{\alpha}=O\left(|z|^{-m+3}\right)$. The Bochner formula implies that there is no nontrivial $L^{2}$ kernel for $P_{1}$. Since $P_{1} \tilde{\alpha}=0$, this implies that $\tilde{\alpha}=0$ by a standard removable singularity theorem for solutions of $P_{1}$, and therefore $h_{0}=0$.

In case of $S_{1}^{\infty}$, given any 1-germ $h_{1}$ at $p_{0}$ let $s$ be the solution of $P s=0$ whose leading term is $|z|^{-m} h_{1}$ at $p_{0}$, and $\left.x^{2} s\right|_{\partial M_{0}} \in E_{0}^{\perp}$. If $h_{1} \in \operatorname{Ker}\left(S_{1}^{\infty}\right)$ then $s=o\left(x^{m-1}\right)$ as $x \rightarrow 0$. Since $s=O\left(|z|^{-m+1}\right)$ as $|z| \rightarrow 0$ and (7.27) is satisfied, by Lemma 7.3, $\tilde{\alpha}=O\left(|z|^{-m+2}\right)$. This implies that $\tilde{\alpha}=0$ by the removable singularity theorem, since there is no solution with that leading term which is also invariant under group action, and therefore $h_{1}=0$.

In case of $S_{2}^{\infty}$, given any 2-germ $h_{2}$ at $p_{0}$ let $s$ be the solution of $P s=0$ whose leading term is $|z|^{-m-2} h_{2}$ at $p_{0}$, and $\left.x^{2} s\right|_{\partial M_{0}} \in\left(E_{0} \oplus E_{1}\right)^{\perp}$. If $h_{2} \in \operatorname{Ker}\left(S_{2}^{\infty}\right)$ then $s=o\left(x^{m-1}\right)$ as $x \rightarrow 0$. Since $s=O\left(|z|^{-m+1}\right)$ as $|z| \rightarrow 0$ and (7.27) is satisfied by Lemma 7.3, $\tilde{\alpha}=O\left(|z|^{-m+2}\right)$. This implies that
$$\tilde{\alpha}=\frac{\alpha_{1}}{|z|^{m}}+O\left(|z|^{-m+2}\right),$$
where $\alpha_{1}$ is a one-form with linear coefficients. Then we have
$$s=\mathcal{K}(\tilde{\alpha})=\mathcal{K}_{e u c}\left(\frac{\alpha_{1}}{|z|^{m}}\right)+O\left(|z|^{-m+1}\right)$$
as $|z| \rightarrow 0$. For the converse, since there is no nontrivial $L^{2}$ kernel for $P_{1}$, given a linear form $\alpha_{1}=a_{i j} z^{i} d z^{j}$, there exists a unique solution $\tilde{\alpha}_{1}$ of $P_{1}\left(\tilde{\alpha}_{1}\right)=0$ which is in $L^{2}\left(M_{0} \backslash B\left(p_{0}, \epsilon\right)\right)$ satisfying
$$\tilde{\alpha}_{1}=|z|^{2-m} a_{i j} z^{i} d z^{j}+O\left(|z|^{2-m}\right),$$
as $|z| \rightarrow 0$. By Proposition 6.1, $\tilde{\alpha}_{1}$ admits an expansion
$$\tilde{\alpha}_{1}=\alpha_{t} x^{\delta_{0, P_{1}}^{+}}+o\left(x^{\delta_{0, P_{1}}^{+}}\right),$$
where $x \alpha_{t} \in \Omega_{t}^{1} \overline{M_{0}}$, as $x \rightarrow 0$. From Proposition 6.2, it follows easily that $h=\mathcal{K} \tilde{\alpha}_{1}$ is a solution of $P h=0$, and thus the 2 -germ $|z|^{m+2} \mathcal{K}_{e u c}\left(\frac{\alpha_{1}}{|z|^{m}}\right)$, is in the kernel of $S_{2}^{\infty}$, where $\alpha_{1}$ is any one-form with linear coefficients. \(\square\)

\section*{8. From boundary tensors to germs}

The following lemma describes a "duality" between boundary tensors and germs. We state the following

Lemma 8.1. Let ( $M^{m}, \partial M, g, x$ ) be $A H$ with one orbifold point $p_{0}$ of type $\Gamma_{n}$. Let $\sigma_{k}, \tau_{k}$ be $k$-germs at $p_{0}$ and Let $s$ and $t$ be two solutions for $P$ such that
$$\begin{aligned}
& s=\sigma_{k}|z|^{2-m-2 k}+o\left(z^{2-m-k}\right) \text { as }|z| \rightarrow 0 \\
& s=\sigma_{\infty} x^{\delta_{0, P}^{+}}+o\left(x^{\delta_{0, P}^{+}}\right) \text {as } x \rightarrow 0
\end{aligned}$$
where $x^{2} \sigma_{\infty} \in \bar{V}_{0}$, and
$$\begin{aligned}
& t=\tau_{k}+o\left(|z|^{k}\right) \text { as }|z| \rightarrow 0 \\
& t=\tau_{\infty} x^{\delta_{0, P}^{-}}+o\left(x^{\delta_{0, P}^{-}}\right) \text {as } x \rightarrow 0,
\end{aligned}$$
where $x^{2} \tau_{\infty} \in \bar{V}_{0}$. For $k=0$ we have
$$(m-2) \frac{\omega_{m-1}}{n}\left\langle\left\langle\sigma_{0}, \tau_{0}\right\rangle\right\rangle=(m-1)\left\langle x^{2} \sigma_{\infty}, x^{2} \tau_{\infty}\right\rangle,$$
for $k=1$ we have
$$\frac{\omega_{m-1}}{n}\left\langle\left\langle\sigma_{1}, \tau_{1}\right\rangle\right\rangle=(m-1)\left\langle x^{2} \sigma_{\infty}, x^{2} \tau_{\infty}\right\rangle,$$
and for $k=2$ we have
$$\frac{2 \omega_{m-1}}{m n}\left\langle\left\langle\sigma_{2}, \tau_{2}\right\rangle\right\rangle=(m-1)\left\langle x^{2} \sigma_{\infty}, x^{2} \tau_{\infty}\right\rangle,$$
where the left inner product is the germ inner product at $p_{0}$ (see the proof for the definition), and the right inner product is the $L^{2}$ inner product on the boundary.

Proof. Let $M_{0, \epsilon}=\bar{M}_{0} \backslash\left(B\left(p_{0}, \epsilon\right) \cup \partial M_{0} \times[0, \epsilon)\right)$. Integrating by parts on $M_{0, \epsilon}$ implies that
$$\int_{M_{0, \epsilon}}(\langle P s, t\rangle-\langle s, P t\rangle) d V_{g}=\int_{\partial M_{0, \epsilon}}\left(\left\langle-\nabla_{\vec{n}} s, t\right\rangle+\left\langle s, \nabla_{\vec{n}} t\right\rangle\right) d S_{g}$$
The interior boundary integral is given by
$$\lim _{\epsilon \rightarrow 0} \int_{\partial B\left(p_{0}, \epsilon\right)}\left(\left\langle-\nabla_{\vec{n}} s, t\right\rangle+\left\langle s, \nabla_{\vec{n}} t\right\rangle\right) d S_{g}=(2-m-2 k) \int_{S^{m-1} / \Gamma_{n}}\left\langle\sigma_{k}, \tau_{k}\right\rangle d S_{e u c}$$
where the inner product denotes contraction on only the indices of the germs corresponding to $S_{0}^{2}\left(T_{p_{0}}^{*}\left(M_{0}\right)\right)$.

Recall from Proposition 6.1 that $\delta_{0, P}^{+}=m-1$ and $\delta_{0, P}^{-}=0$. Since $\sqrt{\operatorname{det} \bar{g}}=$ $x^{1-m} \sqrt{\operatorname{det} g}$ when we restrict both metrics to $\partial M_{0} \times\{\epsilon\}$, it follows that the outer boundary integral is given by
$$\lim _{\epsilon \rightarrow 0} \int_{\partial M_{0} \times\{\epsilon\}}\left(\left\langle-\nabla_{\vec{n}} s, t\right\rangle+\left\langle s, \nabla_{\vec{n}} t\right\rangle\right) d S_{g}=(m-1) \int_{\partial M_{0}}\left\langle x^{2} \sigma_{\infty}, x^{2} \tau_{\infty}\right\rangle d S_{g_{\infty}}$$

If $k=0$ then then working in a coordinate chart around $p_{0}$ with $g_{i j}\left(p_{0}\right)=\delta_{i j}$ we have
$$\begin{aligned}
\sigma_{0} & =H_{k l} d z^{k} \otimes d z^{l}, \\
\tau_{0} & =K_{k l} d z^{k} \otimes d z^{l},
\end{aligned}$$
and (8.3) follows immediately, with $\left\langle\left\langle\sigma_{0}, \tau_{0}\right\rangle\right\rangle=\sum_{k, l} H_{k l} K_{k l}$.
If $k=1$, then
$$\begin{aligned}
\sigma_{1} & =H_{j k l} z^{j} d z^{k} \otimes d z^{l}, \\
\tau_{1} & =K_{j k l} z^{j} d z^{k} \otimes d z^{l},
\end{aligned}$$
and (8.4) follows from (3.21) with $\left\langle\left\langle\sigma_{1}, \tau_{1}\right\rangle\right\rangle=\sum_{j, k, l} H_{j k l} K_{j k l}$.
Finally, if $k=2$, then
$$\begin{aligned}
\sigma_{2} & =H_{i j k l} z^{i} z^{j} d z^{k} \otimes d z^{l}, \\
\tau_{2} & =K_{i j k l} z^{i} z^{j} d z^{k} \otimes d z^{l},
\end{aligned}$$
and (8.5) follows from (3.22) with $\left\langle\left\langle\sigma_{2}, \tau_{2}\right\rangle\right\rangle=\sum_{i, j, k, l} H_{i j k l} K_{i j k l}$. \(\square\)

Next, we explain how to construct a map which sends boundary tensors to germs at $p_{0}$. Identify a neighborhood of the boundary with $\partial M_{0} \times[0, \epsilon)$. Let $\varphi$ be a cutoff function which is 1 on $\partial M_{0} \times\left[0, \frac{\epsilon}{2}\right)$ and is zero on $M_{0} \backslash\left(\partial M_{0} \times[0, \epsilon)\right)$. Given $\sigma_{0} \in V_{0}$, consider the tensor $\varphi x^{-2} \sigma_{0}$. By solving a finite number of terms of a power series, we can then find $s$ of the form $s=\varphi x^{-2} \sigma_{0}+\tilde{s}$, where $\tilde{s}$ are lower order terms supported in a neighborhood of the boundary, such that $P s$ is in $L^{2}$ in a neighborhood of the boundary. (For this power series method, see for example [AG11] for the Hodge Laplacian acting on forms; the same technique applies to solutions of $P$.) Then, using the non-degeneracy assumption, we can find a solution of $P s=0$ defined on all of $M_{0}$, which is in $L^{2}$ on any compact subset of $M_{0}$, so that
$$s=x^{-2} \sigma_{0}+o(1)$$
as $x \rightarrow 0$. Note that by non-degeneracy, the solution $s$ is unique. The solution $s$ admits the following expansion around $p_{0}$
$$s=h_{0}+o(1) \text { as }|z| \rightarrow 0,$$
where $h_{0}$ is a 0 -germ at $p_{0}$. Define a mapping
$$\begin{aligned}
& S_{\infty}^{0}: V_{0} \rightarrow S^{2}\left(T_{p_{0}}^{*} M_{0}\right), \text { by } \\
& S_{\infty}^{0}\left(\sigma_{0}\right) \equiv h_{0} .
\end{aligned}$$
This mapping enjoys the following property.
Lemma 8.2. The mapping $S_{\infty}^{0}: V_{0} \rightarrow S^{2}\left(T_{p_{0}}^{*} M_{0}\right)$ is surjective.
Proof. Assume $S_{\infty}^{0}$ is not surjective. Then there exist a 0 -germ $h_{0}$ such that $h_{0}$ is orthogonal to the image of $S_{\infty}^{0}$. Let $\tilde{h}$ be the solution of $P \tilde{h}=0$ with following
leading terms
$$\begin{aligned}
\tilde{h} & =h_{0}|z|^{2-m}+o\left(|z|^{2-m}\right) \text { as }|z| \rightarrow 0, \\
\tilde{h} & =S_{0}^{\infty}(h) x^{\delta_{0, P}^{+}}+o\left(x^{\delta_{0, P}^{+}}\right) \text {as } x \rightarrow 0 .
\end{aligned}$$
Also for a boundary tensor $\tau \in V_{0}$, let $\tilde{\tau}$ be the solution of $P \tilde{\tau}=0$ with following leading terms
$$\begin{aligned}
& \tilde{\tau}=S_{\infty}^{0}(\tau)+o(1) \text { as }|z| \rightarrow 0, \\
& \tilde{\tau}=x^{-2} \tau+o(1) \text { as } x \rightarrow 0 .
\end{aligned}$$

By applying Lemma 8.1 to $\tilde{\tau}$ and $\tilde{h}$ we see that
$$\left\langle\left\langle h_{0}, S_{\infty}^{0} \tau\right\rangle\right\rangle=c\left\langle S_{0}^{\infty} h_{0}, \tau\right\rangle,$$
for every $\tau \in V_{0}$, where $c \neq 0$, so $S_{0}^{\infty}(h)=0$. This implies that $h_{0}=0$ by Proposition 7.5 (1), which is a contradiction. \(\square\)

We next define a mapping from $E_{0}^{\perp} \subset V_{0}$ (the orthogonal complement in $L^{2}$ ) to 1-germs by the following. Given $\sigma_{0} \in E_{0}^{\perp}$, as above let $s$ be the solution of $P s=0$ defined on all of $M_{0}$, which is in $L^{2}$ on any compact subset of $M_{0}$, and satisfies
$$s=x^{-2} \sigma_{0}+o(1),$$
as $x \rightarrow 0$. By Lemma 8.1, $s$ admits an expansion
$$s=h_{1}+o(|z|),$$
as $|z| \rightarrow 0$, where $h_{1}$ is a 1 -germ at $p_{0}$. We then define the mapping
$$\begin{aligned}
& S_{\infty}^{1}: E_{0}^{\perp} \rightarrow F_{1} \otimes S^{2}\left(T_{p_{0}}^{*} M_{0}\right), \text { by } \\
& S_{\infty}^{1}\left(\sigma_{0}\right) \equiv h_{1}
\end{aligned}$$
This mapping is also onto.
Lemma 8.3. The mapping $S_{\infty}^{1}: E_{0}^{\perp} \rightarrow F_{1} \otimes S^{2}\left(T_{p_{0}}^{*} M_{0}\right)$ is surjective.
Proof. By Proposition 7.5 (2), $S_{1}^{\infty}$ is injective, so by the same argument in the proof of Lemma 8.2, it follows that $S_{\infty}^{1}$ is surjective. \(\square\)

We next define a mapping from $\left(E_{0} \oplus E_{1}\right)^{\perp} \subset V_{0}$ (the orthogonal complement in $L^{2}$ ) to 2-germs by the following. Given $\sigma_{0} \in\left(E_{0} \oplus E_{1}\right)^{\perp}$, as above let $s$ be the solution of $P s=0$ defined on all of $M_{0}$, which is in $L^{2}$ on any compact subset of $M_{0}$, and satisfies
$$s=x^{-2} \sigma_{0}+o(1),$$
as $x \rightarrow 0$. By Lemma 8.1, $s$ admits an expansion
$$s=h_{2}+o\left(|z|^{2}\right),$$
as $|z| \rightarrow 0$, where $h_{2}$ is a 2-germ at $p_{0}$.

We then define the mapping
$$\begin{aligned}
& S_{\infty}^{2}:\left(E_{0} \oplus E_{1}\right)^{\perp} \rightarrow F_{2} \otimes S^{2}\left(T_{p_{0}}^{*} M_{0}\right), \text { by } \\
& S_{\infty}^{2}\left(\sigma_{0}\right) \equiv h_{2}
\end{aligned}$$
The following Lemma says that $S_{\infty}^{2}$ is not surjective, and also gives a complete characterization of its image ${ }^{3}$

Lemma 8.4. Let $T=\operatorname{Im}\left(S_{\infty}^{2}\right)$ then
$$T=S^{\perp},$$
where the orthogonal complement is with respect to the 2 -germ inner product, and
$$S=\left\{\left.|z|^{m+2} \mathcal{K}_{e u c}\left(\frac{\alpha}{|z|^{m}}\right) \right\rvert\, \alpha \text { is a one-form with linear coefficients }\right\} .$$
Proof. Let $h_{2} \in T$ so $h_{2}=S_{\infty}^{2}(\tau)$ and let $\tilde{h}$ be the solution of $P \tilde{h}=0$ with following leading terms
$$\begin{aligned}
& \tilde{h}=h_{2}+o\left(|z|^{2}\right) \text { as }|z| \rightarrow 0, \\
& \tilde{h}=x^{-2} \tau+o(1) \text { as } x \rightarrow 0 .
\end{aligned}$$
For any $t_{2} \in S$, Let $\tilde{t}$ be the solution of $P \tilde{t}=0$ with the following leading terms
$$\begin{aligned}
& \tilde{t}=t_{2}|z|^{-2-m}+o\left(|z|^{-m}\right) \text { as }|z| \rightarrow 0, \\
& \tilde{t}=S_{2}^{\infty}\left(t_{2}\right) x^{-2} x^{m-1}+o\left(x^{m-1}\right) \text { as } x \rightarrow 0 .
\end{aligned}$$
Applying Lemma 8.1 to $\tilde{t}$ and $\tilde{h}$ we obtain
$$\left\langle\left\langle h_{2}, t_{2}\right\rangle\right\rangle=\left\langle\left\langle S_{\infty}^{2}(\tau), t_{2}\right\rangle\right\rangle=c\left\langle\tau, S_{2}^{\infty}\left(t_{2}\right)\right\rangle=0,$$
for some constant $c \neq 0$, so by Proposition 7.5 it follows that $T \subset S^{\perp}$.
Next, assume that $S_{\infty}^{2}$ is not surjective onto $S^{\perp}$. Then there exists a nontrivial $s_{2} \in S^{\perp} \cap T^{\perp}$. Let $\tilde{s}$ be the solution of $P(\tilde{s})=0$ with the following leading terms
$$\begin{aligned}
& \tilde{s}=s_{2}|z|^{-2-m}+o\left(|z|^{-m}\right) \text { as }|z| \rightarrow 0, \\
& \tilde{s}=S_{2}^{\infty}\left(s_{2}\right) x^{-2} x^{m-1}+o\left(x^{m-1}\right) \text { as } x \rightarrow 0 .
\end{aligned}$$
Also, for any boundary tensor $\tau \in\left(E_{0} \oplus E_{1}\right)^{\perp}$, let $\tilde{t}$ be the solution of $P$ with following leading terms
$$\begin{aligned}
& \tilde{t}=S_{\infty}^{2}(\tau)+o\left(|z|^{2}\right) \text { as }|z| \rightarrow 0, \\
& \tilde{t}=x^{-2} \tau+o(1) \text { as } x \rightarrow 0 .
\end{aligned}$$
Applying Lemma 8.1 to $\tilde{t}$ and $\tilde{s}$ we obtain
$$\left\langle S_{2}^{\infty}\left(s_{2}\right), \tau\right\rangle=c\left\langle\left\langle s_{2}, S_{\infty}^{2}(\tau)\right\rangle\right\rangle=0,$$

\footnotetext{
${ }^{3}$ The reader should compare to [Biq13, Lemma 11.1], where it is claimed that this mapping is surjective. However, this does not affect any of the main results in [Biq13], since one can simply gauge the elements $k_{2}$ and $k_{3}$ so that the germs of their leading terms are orthogonal to $S$. See also Biq17.
}
which implies that $S_{2}^{\infty}\left(s_{2}\right)=0$ so $s_{2} \in S$ by Proposition 7.5 (3), which gives a contradiction. \(\square\)

Next, we give an explicit description of the elements of $S$.
Lemma 8.5. Let $\alpha=\frac{\alpha_{1}}{|z|^{m}}$ where $\alpha_{1}=a_{i j} z_{i} d z^{j}$ is a one-form with linear coefficients. Then
$$\mathcal{K}_{e u c}(\alpha)_{i j}=\frac{1}{2}\left(\frac{a_{i j}+a_{j i}}{|z|^{m}}+\frac{-m z_{i} z_{p} a_{p j}-m z_{j} z_{t} a_{t i}}{|z|^{m+2}}\right)+\frac{1}{m}\left(\frac{-\operatorname{tr}(a)}{|z|^{m}}+\frac{m z_{t} z_{p} a_{p t}}{|z|^{m+2}}\right) \delta_{i j}$$
Furthermore, we may write
$$\mathcal{K}_{e u c}(\alpha)=|z|^{-m-2} K_{k l i j} z^{k} z^{l} d z^{i} d z^{j},$$
where
$$\begin{aligned}
K_{i j k l} & =\frac{1}{2}\left(\left(a_{i j}+a_{j i}\right) \delta_{k l}-\frac{m}{2}\left(\delta_{i k} a_{l j}+\delta_{i l} a_{k j}\right)-\frac{m}{2}\left(\delta_{k j} a_{l i}+\delta_{l j} a_{k i}\right)\right) \\
& +\frac{-\operatorname{tr}(a) \delta_{k l} \delta_{i j}}{m}+\frac{\delta_{i j}}{2}\left(a_{l k}+a_{k l}\right)
\end{aligned}$$
Proof. Let $\alpha_{1}=a_{i j} x_{i} d x^{j}$ be a one-form with linear coefficients. Then we have
$$\begin{aligned}
\left(\delta_{e u c}^{*} \alpha\right)_{i j} & =\frac{1}{2}\left(\partial_{i} \alpha_{j}+\partial_{j} \alpha_{i}\right) \\
& =\frac{1}{2}\left(\partial_{i}\left(\frac{a_{p j} z_{p}}{|z|^{m}}\right)+\partial_{j}\left(\frac{a_{k i} z_{k}}{|z|^{m}}\right)\right)
\end{aligned}$$
Using $\partial_{i}\left(|z|^{-m}\right)=\frac{-m z_{i}}{|z|^{m+2}}$ we obtain
$$\left(\delta_{e u c}^{*} \alpha\right)_{i j}=\frac{1}{2}\left(\frac{a_{i j}+a_{j i}}{|z|^{m}}+\frac{-m z_{i} z_{p} a_{p j}-m z_{j} z_{k} a_{k i}}{|z|^{m+2}}\right) .$$
Also,
$$\delta_{e u c}(\alpha)=-\partial_{k} X_{k}=-\partial_{k}\left(\frac{a_{p k} z_{p}}{|z|^{m}}\right)=\frac{-\operatorname{tr}(a)}{|z|^{m}}+\frac{m z_{k} z_{p} a_{p k}}{|z|^{m+2}} .$$
The formula (8.41) follows directly from these computations, and (8.42) follows easily from this. \(\square\)

Lemma 8.6. The tensor $r^{2} g_{\text {euc }}=P_{i j k l} z^{i} z^{j} d z^{k} d z^{l}$, where
$$P_{i j k l}=\delta_{i j} \delta_{k l}$$
satisfies $B_{\text {euc }}\left(r^{2} g_{\text {euc }}\right)=2(n-1) r d r$. The tensor $r^{2} d r \otimes d r=Q_{\text {ijkl }} z^{i} z^{j} d z^{k} d z^{l}$, where
$$Q_{i j k l}=\frac{1}{2}\left(\delta_{i k} \delta_{j l}+\delta_{i l} \delta_{j k}\right),$$
satisfies $B_{\text {euc }}\left(r^{2} d r \otimes d r\right)=(-2 n) r d r$. The tensor $r^{4} \theta \otimes \theta=A_{i j k l} z^{i} z^{j} d z^{k} d z^{l}$, where
$$A_{i j k l}=\frac{1}{2}\left(J_{i}^{k} J_{j}^{l}+J_{i}^{l} J_{j}^{k}\right),$$
satisfies $B_{\text {euc }}\left(r^{4} \theta \otimes \theta\right)=2 r d r$.

Proof. The proof is a simple calculation, and is omitted. \(\square\)

Lemma 8.7. We have the following identities:
$$\begin{aligned}
& \langle\langle Q, K\rangle\rangle=\frac{2-m^{2}-m}{2} \operatorname{tr}(a), \\
& \langle\langle A, K\rangle\rangle=\frac{m+2}{2} \operatorname{tr}(a), \\
& \langle\langle K, P\rangle\rangle=0 .
\end{aligned}$$
Proof. We compute
$$\begin{aligned}
\langle\langle Q, K\rangle\rangle & =\frac{1}{2}\left(\left(a_{i j}+a_{j i}\right) \delta_{i j}-\frac{m}{2}\left(\delta_{i i} a_{j j}+\delta_{i j} a_{i j}\right)-\frac{m}{2}\left(\delta_{i j} a_{j i}+\delta_{j j} a_{i i}\right)\right) \\
& +\frac{-\operatorname{tr}(a) \delta_{i j} \delta_{i j}}{m}+\frac{\delta_{i j}}{2}\left(a_{j i}+a_{i j}\right) \\
& \left.=\frac{1}{2}\left(2 \operatorname{tr}(a)-m^{2} \operatorname{tr}(a)-m \operatorname{tr}(a)\right)\right)=\frac{2-m^{2}-m}{2} \operatorname{tr}(a) .
\end{aligned}$$
This proves the first identity. For the second identity, we have
$$\begin{aligned}
\langle\langle A, K\rangle\rangle= & \frac{1}{2}\left(\left(a_{i j}+a_{j i}\right) \delta_{k l} J_{i}^{k} J_{j}^{l}-\frac{m}{2}\left(J_{i}^{k} J_{j}^{l} \delta_{i k} a_{l j}+J_{i}^{k} J_{j}^{l} \delta_{i l} a_{k j}\right)\right. \\
& \left.-\frac{m}{2}\left(J_{i}^{k} J_{j}^{l} \delta_{k j} a_{l i}+J_{i}^{k} J_{j}^{l} \delta_{l j} a_{k i}\right)\right)+\frac{-\operatorname{tr}(a) \delta_{k l} \delta_{i j} J_{i}^{k} J_{j}^{l}}{m}+J_{i}^{k} J_{j}^{l} \delta_{i j} \frac{\left(a_{l k}+a_{k l}\right)}{2} \\
& =\frac{1}{2}(2 \operatorname{tr}(a)+m \operatorname{tr}(a))-\operatorname{tr}(a)+\operatorname{tr}(a)=\frac{m+2}{2} \operatorname{tr}(a) .
\end{aligned}$$
Finally, the last identity follows from the fact that $K$ is traceless on the first and last two pairs of indices. \(\square\)

We next construct a special symmetric 2-tensor $k_{1}$ on the Calabi manifold.
Proposition 8.8. Let $\sigma_{2}$ denote the quadratic 2-tensor
$$\sigma_{2}=r^{2}\left(-d r \otimes d r-(2 n-1) r^{2} \theta \otimes \theta+g_{e u c}\right)=S_{i j k l} x^{i} x^{j} d x^{k} d x^{l} .$$
Then
$$\operatorname{tr}_{e u c}\left(\sigma_{2}\right)=0, \quad B_{e u c}\left(\sigma_{2}\right)=0 \Delta_{e u c}\left(\sigma_{2}\right)=0,$$
and
$$\langle\langle S, K\rangle\rangle=0,$$
for all $K_{i j k l}$ of the form in (8.43). Furthermore, there exist a constant $c \neq 0$ and a tensor $k_{1}$ defined on the Calabi manifold with the following properties
$$\begin{aligned}
& k_{1}=c \cdot \sigma_{2}+O\left(r^{-2 n+2+\epsilon}\right) \\
& P_{g_{c a l}}\left(k_{1}\right)=o \\
& B_{g_{c a l}}\left(k_{1}\right)=0
\end{aligned}$$
as $r \rightarrow \infty$.

Proof. First, we have
$$\operatorname{tr}_{e u c}\left(\sigma_{2}\right)=r^{2}(-1-(2 n-1)+2 n)=0 .$$
Next, using Lemma 8.6, we have
$$B_{e u c}\left(\sigma_{2}\right)=(2 n-2(2 n-1)+2(n-1)) r d r=0 .$$
Next, it follows from Lemma 8.6 that $S_{i j k l}=S_{k l i j}$, so the first equation in (8.56) implies the last.

To see (8.57), Lemma 8.7 implies that
$$\langle\langle S, K\rangle\rangle=\left((n+1)(1-2 n)-\left(1-2 n^{2}-n\right)\right) \operatorname{tr}(a)=0 .$$
Next, let $(H, \Lambda)=\left(\sigma_{2}, 0\right)$ in Proposition 3.2 to find a solution of
$$\begin{aligned}
P_{g_{c a l}}\left(k_{1}\right) & =\tilde{\lambda} o \\
k_{1} & =c \cdot \sigma_{2}+O\left(r^{-2 n+2+\epsilon}\right) \\
B_{g_{c a l}}(h) & =0
\end{aligned}$$
where $\tilde{\lambda}$ is given by
$$\tilde{\lambda}=-\frac{c}{\|o\|_{L^{2}}^{2}} \lim _{r \rightarrow \infty} \int_{S_{r} / \Gamma_{n}} \frac{n+1}{r}\left\langle\sigma_{2}, o\right\rangle d S_{S_{r} / \Gamma_{n}} .$$
The leading term in the integrand is given by
$$\frac{n+1}{r}\left\langle\sigma_{2}, o_{e u c}\right\rangle=c \cdot 2 n\left(1-n^{2}\right) r^{1-m},$$
so choosing the scaling constant $c$ to make $\tilde{\lambda}=1$ finishes the proof. \(\square\)

The following result is the key ingredient to our existence theorem in the AHE case, which will be proved in Section 9.

Proposition 8.9. Let $\sigma=c \cdot \sigma_{2}=c \cdot S_{i j k l} z^{i} z^{j} d z^{k} d z^{l}$ be as Proposition 8.8. Then there exist a solution $\tilde{k}$ of $P_{g_{0}}(\tilde{k})=0$ defined on $M_{0}$ such that
$$\begin{aligned}
& \tilde{k}=\sigma+O(|z|) \text { as }|z| \rightarrow 0 \\
& \tilde{k}=k_{\infty}+o(1) \text { as } x \rightarrow 0,
\end{aligned}$$
where $x^{2} k_{\infty} \in \overline{V_{0}}$.
Proof. The proof is immediate from Lemma 8.4 if we let $\sigma$ be the leading term of the tensor $k_{1}$ found in Proposition 8.8. \(\square\)

\section*{9. Completion of proofs}

In this section, we complete the proofs of Theorems 1.2 and 1.3. First, for $u \in \mathbb{R}$, we define
$$h_{t, u}=g_{c a l}+t h+u t k_{1},$$
where $h$ was defined in (4.4), and $k_{1}$ was defined in Proposition 8.8.

Lemma 9.1. For $t$ and $u$ sufficiently small, $h_{t, u}$ is a Riemannian metric on $X^{t}$. Moreover, for each integer $\ell \geq 0$, there exists a constant $c_{\ell}$ so that $h_{t, u}$ satisfies the following estimate on $X^{t}$
$$\left|\nabla^{\ell}\left(\operatorname{Ric}_{h_{t, u}}-t \Lambda h_{t, u}-t(\lambda+u) \chi_{t}(\rho) o\right)\right|_{g_{c a l}} \leq c_{\ell} t^{2}\left(1+u^{2}+t^{2}\right) \rho^{2-\ell} .$$
Proof. Since $h$ and $k_{1}$ both have quadratic leading terms, and $g_{\text {cal }}$ is ALE, there exist constants $c$ and $c_{1}$ so that
$$\begin{array}{r}
|h|_{g_{c a l}}(p) \leq c \rho^{2}(p) \\
\left|k_{1}\right|_{g_{c a l}}(p) \leq c_{1} \rho^{2}(p)
\end{array}$$
for any $p \in X^{t}$. Similarly, there exists a constant $c_{2}$ so that
$$|o|_{g_{c a l}}(p) \leq c_{2} \rho^{-2 n}(p),$$
for any $p \in X^{t}$. It follows that
$$\begin{array}{r}
|t h|_{g_{c a l}}(p) \leq c \rho^{2}(p) \leq \frac{1}{2} c t^{\frac{1}{2}} \\
\left|t u k_{1}\right|_{g_{c a l}}(p) \leq c_{1} u \rho^{2}(p) \leq \frac{1}{2} c_{1} u t^{\frac{1}{2}} \\
|t u o|_{g_{c a l}}(p) \leq c_{2} u \rho^{2}(p) \leq \frac{1}{2} c_{2} u t^{\frac{1}{2}}
\end{array}$$
The right hand side is independent of $p$ so $h_{t, u}$ is a Riemannian metric for sufficiently small $t$ and $u$. Recall that
$$\begin{aligned}
& d_{g_{c a l}} \operatorname{Ric}(h)=\Lambda g_{c a l}+\lambda o \\
& d_{g_{c a l}} \operatorname{Ric}(o)=0 \\
& d_{g_{c a l}} \operatorname{Ric}\left(k_{1}\right)=o,
\end{aligned}$$
so we have
$$\operatorname{Ric}\left(g_{c a l}+t h+t u k_{1}\right)=\operatorname{Ric}\left(g_{c a l}\right)+d_{g_{c a l}} \operatorname{Ric}\left(t h+t u k_{1}\right)+Q\left(t h+t u k_{1}\right),$$
where, using (4.14), $Q$ is a nonlinear term satisfying
$$\begin{aligned}
\left|Q\left(t h+t u k_{1}\right)\right| \leq b\left(\left|R m_{g_{\text {cal }}}\right|\left|t h+t u k_{1}\right|^{2}\right. & +\left|t h+t u k_{1}\right|\left|\nabla^{2}\left(t h+t u k_{1}\right)\right| \\
& \left.+\left|\nabla\left(t h+t u k_{1}\right)\right|^{2}\right),
\end{aligned}$$
for some constant $b$ and for $t$ and $u$ sufficiently small, and where the norms and covariant derivatives are measured with respect to the Calabi metric. Note that
$$\begin{array}{r}
\left|\nabla^{\ell} h\right| \leq c_{\ell} \rho^{2-\ell} \\
\left|\nabla^{\ell} o\right| \leq c_{\ell} \rho^{-2 n-\ell} \\
\left|\nabla^{\ell} k_{1}\right| \leq c_{\ell} \rho^{2-\ell},
\end{array}$$
so it follows that
$$\left|Q\left(t h+t u k_{1}\right)\right| \leq b_{1} t^{2}\left(1+t^{2}+u^{2}\right) \rho^{2}$$
and consequently
$$\mid \text { Ric }_{h_{t, u}}-t \Lambda h_{t, u}-t \lambda o-t u o \mid \leq c_{0} t^{2}\left(1+t^{2}+u^{2}\right) \rho^{2},$$
for some constant $c_{0}$, so the lemma for $\ell=0$ follows. The proof for $\ell>0$ is similar and is omitted. \(\square\)

We next define
$$k=\left\{\begin{array}{ll}
\tilde{k} & M_{0} \backslash B\left(p_{0}, 2 t^{1 / 4}\right) \\
\left(1-\chi_{t}(r)\right) \phi_{t}^{*} \tilde{k}+\chi_{t}(r) t^{2} k_{1} & (1 / 2) t^{-1 / 4}<r<2 t^{-1 / 4} \\
t^{2} k_{1} & r<(1 / 2) t^{-1 / 4}
\end{array},\right.$$
where $\chi_{t}$ is the cutoff function we defined in (1.11), and $\tilde{k}$ was defined in Proposition 8.9. For $u \in \mathbb{R}$, consider the metric on $M^{t}$ defined by $g_{t, u}=g_{t}+u k$, where $g_{t}$ is the refined metric defined in (4.20). Note that $g_{t, u}$ has the following expression
$$g_{t, u}=\left\{\begin{array}{ll}
g_{0}+u \tilde{k} & M_{0} \backslash B\left(p_{0}, 2 t^{1 / 4}\right) \\
\left(1-\chi_{t}(r)\right) \phi_{t}^{*}\left(g_{0}+u \tilde{k}\right)+\chi_{t}(r) t h_{t, u} & (1 / 2) t^{-1 / 4}<r<2 t^{-1 / 4} \\
t h_{t, u} & r<(1 / 2) t^{-1 / 4}
\end{array} .\right.$$
This metric satisfies the following modification of Lemma 4.2.
Lemma 9.2. For $t$ and $u$ sufficiently small, $g_{t, u}$ is a Riemannian metric on $M^{t}$. Moreover, for each integer $\ell \geq 0$, there exist a constant $c_{\ell}$ so that $g_{t, u}$ satisfies the following estimate on $X^{t}$
$$\left|\nabla^{\ell}\left(\operatorname{Ric}_{g_{t, u}}-\Lambda g_{t, u}-t(\lambda+u) \chi_{t}(\rho) o\right)\right|_{g_{c a l}} \leq c_{\ell} t^{2}\left(1+t^{2}+u^{2}\right) \rho^{2-\ell} .$$
Proof. If $r<(1 / 2) t^{-1 / 4}$, then the proof follows from the Lemma 9.1 by scaling. If
$$(1 / 2) t^{-1 / 4}<r<2 t^{-1 / 4},$$
then
$$g_{t, u}=\left(1-\chi_{t}(r)\right)\left(\phi_{t}^{*}\left(u \tilde{k}+g_{0}\right)\right)+\chi_{t}(r)\left(t h_{t}+t^{2} u k_{1}\right) .$$
We have that
$$\begin{aligned}
& \phi_{t}^{*} g_{0}=t g_{e u c}+t^{2} H+O\left(t^{\frac{3}{2}} \rho^{3}\right) \\
& t h_{t}=t g_{e u c}+t^{2} H+t O\left(r^{-2 n}\right)+t O\left(r^{2-2 n+\epsilon}\right),
\end{aligned}$$
and
$$\begin{aligned}
& \phi_{t}^{*}(u \tilde{k})=t^{2}(u \sigma)+u t^{2} O\left(r^{-2 n+2+\epsilon}\right) \\
& t^{2} u k_{1}=t^{2} u(\sigma)+t^{2} O\left(r^{-2 n+2+\epsilon}\right),
\end{aligned}$$
as $t \rightarrow 0$. Since the quadratic terms agree in each of these, we have the estimate
$$g_{t, u}=t g_{e u c}+t^{2} H+t^{2} u \sigma+t O\left(t^{\frac{3}{2}} \rho^{3}\right),$$
as $t \rightarrow 0$. Writing
$$\theta=g_{t}-t g_{e u c},$$
expanding the Ricci tensor near $t \cdot g_{\text {euc }}$ we have
$$\operatorname{Ric}_{g_{t, u}}=d_{t \cdot e u c} \operatorname{Ric}(\theta)+Q(\theta),$$
where $Q(\theta)$ satisfies the estimate
$$t^{2}|Q(\theta)| \leq c\left(|\theta|\left|\nabla^{2} \theta\right|+|\nabla \theta|^{2}\right),$$
for some constant $c$, where the norms are with respect to $g_{\text {euc }}$. More precisely,
$$\theta=t^{2} H+t^{2} u \sigma+t O\left(t^{\frac{3}{2}} \rho^{3}\right)$$
implies that
$$\begin{aligned}
& \left|\nabla^{2} \theta\right||\theta|=O\left(t^{4}\left(1+u^{2}+t^{2}\right) \rho^{2}\right), \\
& |\nabla \theta|^{2}=O\left(t^{4}\left(1+u^{2}+t^{2}\right) \rho^{2}\right) .
\end{aligned}$$
From (4.4) it follows that
$$d_{t \cdot e u c} \operatorname{Ric}(\theta)=t \Lambda g_{e u c}+O\left(t^{2}\left(1+u^{2}+t^{2}\right) \rho^{2}\right),$$
where $O$ is with respect to the Euclidean metric. Note that (9.22) implies that
$$t \lambda \chi_{t}(\rho) o=O\left(t^{2} \rho^{2}\right) .$$
Finally we obtain
$$\operatorname{Ric}_{g_{t, u}}-\Lambda g_{t, u}-t(\lambda+u) \chi_{t}(\rho) o=O\left(t^{2}\left(1+t^{2}+u^{2}\right) \rho^{2}\right),$$
so the lemma for $\ell=0$ follows. For $\ell>0$, the proof is similar and is omitted. \(\square\)

Proof of Theorem 1.2. We apply Proposition 5.2, keeping track of the dependence on the variable $u$. From Proposition 5.2, we obtain a solution of
$$\Phi\left(\hat{g}_{t, u, v}\right)=\lambda(t, u)\left(\chi_{t} o\right) .$$
Lemma 9.2 implies that $\lambda(t, u)$ is differentiable in the $u$ variable, and if $\lambda=0$ then
$$\lambda(t, u)=t u+O\left(t^{\frac{3}{2}-\delta}\right) .$$
By the classical implicit function theorem, for each $t$ sufficiently small, there exists $u(t)$ such that $\lambda(t, u(t))=0$. For $t$ sufficiently small, Ric $_{g_{t, u, v}}$ is strictly negative, and a standard argument (see [Biq06]) then implies that $\hat{g}_{t, u, v}$ is Einstein. \(\square\)

Proof of Theorem 1.3. First assume that $g_{0}$ is non-degenerate. Observe that the refined approximate metric is close to the naïve approximate metric in the $C_{\delta_{0}, \delta_{\infty} ; t}^{2, \alpha}$ weighted norm, for $t$ sufficiently small. As above, from the results in [Biq13, Section 8], for any metric $g_{E}$ satisfying (1.16), then there exists a diffeomorphism $\varphi: M^{t} \rightarrow M^{t}$ so that $B_{g_{t}}\left(g_{t}-\varphi^{*} g_{E}\right)=0$, and $\varphi^{*} g_{E}$ remains close to $g_{t}$ in the $C_{\delta_{0}, \delta_{\infty} ; t}^{2, \alpha}$ weighted norm. The metric $\varphi^{*} g_{E}$ would then give a zero of the mapping $\Phi_{t}$, but then (5.20) would then imply that $\lambda=0$, a contradiction.

If $g_{0}$ is not non-degenerate, then if $\delta_{\infty}$ is chosen sufficiently small, the linearized operator is Fredholm (see [Lee06]), so there is a finite-dimensional space of $L^{2}$ infinitesimal Einstein deformations on $\left(M_{0}, g_{0}\right)$. The remainder of the proof is almost identical to the proof of Theorem 1.1 given above. \(\square\)

\section*{References}
[AD98] Lars Andersson and Mattias Dahl, Scalar curvature rigidity for asymptotically locally hyperbolic manifolds, Ann. Global Anal. Geom. 16 (1998), no. 1, 1-27.
[AG11] Erwann Aubry and Colin Guillarmou, Conformal harmonic forms, Branson-Gover operators and Dirichlet problem at infinity, J. Eur. Math. Soc. (JEMS) 13 (2011), no. 4, 911-957.
[And08] Michael T. Anderson, On boundary value problems for Einstein metrics, Geom. Topol. 12 (2008), no. 4, 2009-2045.
[AV12] Antonio G. Ache and Jeff A. Viaclovsky, Obstruction-flat asymptotically locally Euclidean metrics, Geom. Funct. Anal. 22 (2012), no. 4, 832-877.
[Bar86] Robert Bartnik, The mass of an asymptotically flat manifold, Comm. Pure Appl. Math. 39 (1986), no. 5, 661-693.
[BB82] Lionel Bérard-Bergery, Sur de nouvelles variétés riemanniennes d'Einstein, Institut Élie Cartan, 6, Inst. Élie Cartan, vol. 6, Univ. Nancy, Nancy, 1982, pp. 1-60.
[Bes08] Arthur L. Besse, Einstein manifolds, Classics in Mathematics, Springer-Verlag, Berlin, 2008, Reprint of the 1987 edition.
[Biq06] Olivier Biquard, Asymptotically symmetric Einstein metrics, SMF/AMS Texts and Monographs, vol. 13, American Mathematical Society, Providence, RI; Société Mathématique de France, Paris, 2006, Translated from the 2000 French original by Stephen S. Wilson.
[Biq08] $\_\_\_\_$, Continuation unique à partir de l'infini conforme pour les métriques d'Einstein, Math. Res. Lett. 15 (2008), no. 6, 1091-1099.
[Biq13] $\_\_\_\_$, Désingularisation de métriques d'Einstein. I, Invent. Math. 192 (2013), no. 1, 197-252.
[Biq16] $\_\_\_\_$, Désingularisation de métriques d'Einstein. II, Invent. Math. 204 (2016), no. 2, 473-504.
[Biq17] $\_\_\_\_$, Non dégénérescence et singularités des métriques d'Einstein asymptotiquement hyperboliques en dimension 4, arXiv.org:1704.05389, 2017.
[Bre08] Simon Brendle, Blow-up phenomena for the Yamabe equation, J. Amer. Math. Soc. 21 (2008), no. 4, 951-979.
[Cal79] E. Calabi, Métriques kählériennes et fibrés holomorphes, Ann. Sci. École Norm. Sup. (4) 12 (1979), no. 2, 269-294.
[CDLS05] Piotr T. Chruściel, Erwann Delay, John M. Lee, and Dale N. Skinner, Boundary regularity of conformally compact Einstein metrics, J. Differential Geom. 69 (2005), no. 1, 111-136.
[GL91] C. Robin Graham and John M. Lee, Einstein metrics with prescribed conformal infinity on the ball, Adv. Math. 87 (1991), no. 2, 186-225.
[GV16] Matthew J. Gursky and Jeff A. Viaclovsky, Critical metrics on connected sums of Einstein four-manifolds, Adv. Math. 292 (2016), 210-315.
[HV16] Jiyuan Han and Jeff A. Viaclovsky, Deformation theory of scalar-flat Kähler ALE surfaces, arXiv.org:1605.05267, 2016.
[Joy00] Dominic D. Joyce, Compact manifolds with special holonomy, Oxford Mathematical Monographs, Oxford University Press, Oxford, 2000.
[KN96] Shoshichi Kobayashi and Katsumi Nomizu, Foundations of differential geometry. Vol. II, Wiley Classics Library, John Wiley \& Sons, Inc., New York, 1996, Reprint of the 1969 original, A Wiley-Interscience Publication.
[KR97] W. Kühnel and H.-B. Rademacher, Conformal completion of $\mathrm{U}(n)$-invariant Ricci-flat Kähler metrics at infinity, Z. Anal. Anwendungen 16 (1997), no. 1, 113-117, Dedicated to the memory of Paul Günther.
[Lee06] John M. Lee, Fredholm operators and Einstein metrics on conformally compact manifolds, Mem. Amer. Math. Soc. 183 (2006), no. 864, vi+83.
[Lu99] Peng Lu, Kähler-Einstein metrics on Kummer threefold and special Lagrangian tori, Comm. Anal. Geom. 7 (1999), no. 4, 787-806.
[Maz88] Rafe Mazzeo, The Hodge cohomology of a conformally compact metric, J. Differential Geom. 28 (1988), no. 2, 309-339.
[Maz91a] $\_\_\_\_$, Elliptic theory of differential edge operators. I, Comm. Partial Differential Equations 16 (1991), no. 10, 1615-1664.
[Maz91b] $\_\_\_\_$, Unique continuation at infinity and embedded eigenvalues for asymptotically hyperbolic manifolds, Amer. J. Math. 113 (1991), no. 1, 25-45.
[MK06] James Morrow and Kunihiko Kodaira, Complex manifolds, AMS Chelsea Publishing, Providence, RI, 2006, Reprint of the 1971 edition with errata.
[MS07] Rafe Mazzeo and Michael Singer, Some remarks on conic degeneration and bending of Poincaré-Einstein metrics, arXiv.org:0709.1498, 2007.
[OSS16] Yuji Odaka, Cristiano Spotti, and Song Sun, Compact moduli spaces of del Pezzo surfaces and Kähler-Einstein metrics, J. Differential Geom. 102 (2016), no. 1, 127-172.
[PP87] Don N. Page and C. N. Pope, Inhomogeneous Einstein metrics on complex line bundles, Classical Quantum Gravity 4 (1987), no. 2, 213-225.
[Sal89] Simon Salamon, Riemannian geometry and holonomy groups, Pitman Research Notes in Mathematics Series, vol. 201, Longman Scientific \& Technical, Harlow, 1989.
[Tia90] G. Tian, On Calabi's conjecture for complex surfaces with positive first Chern class, Invent. Math. 101 (1990), no. 1, 101-172.

Department of Mathematics, University of Wisconsin, Madison, WI, 53706
E-mail address: morteza@math.wisc.edu
Department of Mathematics, University of California, Irvine, CA, 92697
E-mail address: jviaclov@uci.edu