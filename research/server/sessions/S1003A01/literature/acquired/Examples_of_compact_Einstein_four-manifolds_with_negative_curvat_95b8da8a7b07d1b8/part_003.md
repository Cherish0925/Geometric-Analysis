---
retention_scope: session
part: 3
total_parts: 3
---

[Part 3/3 of: Examples of compact Einstein four-manifolds with negative curvature]

Recall that our hypothesis provided a sequence $\tilde{g}_{k}$ of metrics on $X_{k}$ satisfying (5.1) and a sequence $s_{k}$ of symmetric bilinear forms with $L_{\tilde{g}_{k}}\left(s_{k}\right)$ supported in $S_{k}$ and satisfying (5.2). We write $\tilde{s}_{k}=\eta s_{k}$, which is supported in $A_{k}$. For this section only we denote by $L_{h_{k}}$ the linearised Ricci operator in the Bianchi gauge with respect to $h_{k}$ itself, acting on sections compactly supported in $D$. By (4.4) it is a rough laplacian plus zeroth-order terms, and direct computation gives
$$L_{h_{k}}\left(\tilde{s}_{k}\right)=\eta L_{h_{k}}\left(s_{k}\right)-\nabla_{\nabla \eta} s_{k}++\frac{1}{2}\left(\Delta_{h_{k}} \eta\right) s_{k}$$
where here ∇ is taken with respect to $h_{k}$. The last two terms here are supported only where $\nabla \eta$ is non-zero, i.e., in the region $B_{k}$ given by
$$\begin{aligned}
B_{k}= & B_{k}^{\prime} \cap A_{k} \\
B_{k}^{\prime}= & \left\{e^{-M} u\left(x_{k}\right) \leq u \leq e^{-M / 2} u\left(x_{k}\right)\right\} \cup\left\{e^{M / 2} u\left(x_{k}\right) \leq u \leq e^{M} u\left(x_{k}\right)\right\} \\
& \cup\left\{-\frac{3 \pi}{4 l} \leq \theta \leq-\frac{\pi}{2 l}\right\} \cup\left\{\frac{\pi}{2 l} \leq \theta \leq \frac{3 \pi}{4 l}\right\} \cup\{\sigma-2 \leq s \leq \sigma-1\}
\end{aligned}$$

We want to compare (5.32) to $L_{\tilde{g}_{k}}\left(s_{k}\right)$. We begin with the last two terms. By definition of the $\eta_{i}$, we have that for any $y \in B_{k}$,
$$\left|-\nabla_{\nabla \eta} s_{k}+\frac{1}{2}\left(\Delta_{h_{k}} \eta\right) s_{k}\right|_{h_{k}}(y) \leq \frac{C}{M}\left(\left|s_{k}\right|_{h_{k}}(y)+\left|\nabla s_{k}\right|_{h_{k}}(y)\right)$$
for some $C$ independent of $k$ or $M$, and for all $k$ sufficiently large. Since $u\left(x_{k}\right) \rightarrow \infty$, we have that for any $m \in \mathbb{N}$, as $k \rightarrow \infty$,
$$\left\|g_{k}-h_{k}\right\|_{C^{m}\left(A_{k}\right)} \rightarrow 0$$
This means that for $y \in B_{k}$,
$$\left|-\nabla_{\nabla \eta} s_{k}+\frac{1}{2}\left(\Delta_{h_{k}} \eta\right) s_{k}\right|_{h_{k}}(y) \leq \frac{C}{M}\left(\left|s_{k}\right|_{g_{k}}(y)+\left|\nabla s_{k}\right|_{g_{k}}(y)\right)$$
where on the right-hand side ∇ is now defined using $g_{k}$. From here, and by (4.16) we have
$$\left|-\nabla_{\nabla \eta} s_{k}+\frac{1}{2}\left(\Delta_{h_{k}} \eta\right) s_{k}\right|_{h_{k}}(y) \leq \frac{C}{M} u(y)^{-\alpha}\left\|s_{k}\right\|_{C_{\alpha}^{1}}$$
Now, by the weighted elliptic estimate, Lemma 4.13, for the metric $\tilde{g}_{k}$, together with the hypothesis (5.2), we have
$$\left\|s_{k}\right\|_{C_{\alpha}^{m+2, \eta}} \lesssim\left\|s_{k}\right\|_{C_{\alpha}^{0}}$$
Together with (5.35), this gives
$$\left|-\nabla_{\nabla \eta} s_{k}+\frac{1}{2}\left(\Delta_{h_{k}} \eta\right) s_{k}\right|_{h_{k}}(y) \leq \frac{C}{M} u(y)^{-\alpha}\left\|s_{k}\right\|_{C_{\alpha}^{0}}$$

Meanwhile, with an eye on the first term in (5.32), we note that, by (5.1), $\tilde{g}_{k}-g_{k}$ is small in $C_{\alpha}^{m+2, \eta}$. Together with (5.34), and similar reasoning as led to (5.36), we see that for any $y \in A_{k}$,
$$\left|\left(L_{h_{k}}-L_{\tilde{g}_{k}}\right)\left(s_{k}\right)\right|_{g_{k}}(y)=o\left(u(y)^{-\alpha}\left\|s_{k}\right\|_{C_{\alpha}^{0}}\right)$$

We are now in a position to apply the representation formula (5.30) for tensors compactly supported in the region $D \subset \tilde{\mathbb{H}}^{4}$. Since $\tilde{s}_{k}$ is supported in a region on which $h_{k}$ is isometric to $(D, \tilde{h})$ we can apply this formula to $\tilde{s}_{k}$. For clarity, we will only consider from now on norms defined with respect to $\tilde{h}$.

When taken together with (5.36) and (5.37) we obtain the following (recall that $S_{k}$ is the gluing region, in which we assume $L_{\tilde{g}_{k}}\left(s_{k}\right)$ is supported):
$$\begin{aligned}
& \left|\tilde{s}_{k}\left(x_{k}\right)\right|_{g_{k}} \lesssim\left\|L_{\tilde{g}_{k}}\left(s_{k}\right)\right\|_{C_{\alpha}^{0}} \cdot \int_{A_{k} \cap S_{k}} u(y)^{-\alpha}\left|G_{\tilde{h}}\left(x_{k}, y\right)\right|_{\tilde{h}} \mathrm{dvol}_{\tilde{h}}(y) \\
& \quad+o\left(\left\|s_{k}\right\|_{C_{\alpha}^{0}} \cdot \int_{A_{k}} u(y)^{-\alpha}\left|G_{\tilde{h}}\left(x_{k}, y\right)\right|_{\tilde{h}} \mathrm{~d} \operatorname{vol}_{\tilde{h}}(y)\right) \\
& \quad \quad+O\left(\frac{1}{M}\left\|s_{k}\right\|_{C_{\alpha}^{0}} \cdot \int_{B_{k}} u(y)^{-\alpha}\left|G_{\tilde{h}}\left(x_{k}, y\right)\right|_{\tilde{h}} \mathrm{~d} \operatorname{vol}_{\tilde{h}}(y)\right)
\end{aligned}$$
The crux then is to control the integrals appearing in (5.38).
Lemma 5.10. Let $0<\alpha<3$. Then
$$\int_{A_{k}} u(y)^{-\alpha}\left|G_{\tilde{h}}\left(x_{k}, y\right)\right|_{\tilde{h}} \operatorname{dvol}_{\tilde{h}}(y) \lesssim u\left(x_{k}\right)^{-\alpha}$$
Proof. The Green's operator $G_{\tilde{h}}\left(x_{k}, y\right)$ has a pole at $y=x_{k}$ which we take care of first. By definition (5.31) of $A_{k}$, there is a radius $\rho>0$ depending only on the degree $l$ of the cover (and in particular independent of $k$ and $M$ ), such that $B_{\tilde{h}}\left(x_{k}, \rho\right) \subset A_{k}$. Since $u$ is of controlled growth on this ball, for any $y \in B_{\tilde{h}}\left(x_{k}, \rho\right)$, we have $u(y)^{-\alpha} \lesssim u\left(x_{k}\right)^{-\alpha}$. Meanwhile, the Green's operator of hyperbolic space is $L^{1}$ near the pole, so that
$$\int_{B_{\tilde{h}}\left(x_{k}, \rho\right)}\left|G_{\tilde{h}}\left(x_{k}, y\right)\right|_{\tilde{h}} \operatorname{dvol}_{\tilde{h}}(y)=\int_{B_{h}(p, \rho)}\left|G_{h}(p, q)\right|_{h} \operatorname{dvol}_{h}(q)=C$$
is independent of $k$. It follows that
$$\int_{B_{\tilde{h}}\left(x_{k}, \rho\right)} u(y)^{-\alpha}\left|G_{\tilde{h}}\left(x_{k}, y\right)\right|_{\tilde{h}} \mathrm{dvol}_{\tilde{h}} \lesssim u\left(x_{k}\right)^{-\alpha}$$

Away from the pole we will use the pointwise exponential decay of $G_{h}$. For the hyperbolic Green's function of $L_{h}$, for any $\rho>0$ there is a constant $C$ such that for any $p, q \in \mathbb{H}^{4}$ with $d_{h}(p, q) \geq \rho$, we have
$$\left|G_{h}(p, q)\right|_{h} \leq C e^{-3 d_{h}(p, q)}$$
See for instance Biquard [10], Proposition 1.2.2. It follows that for $y \in A_{k} \backslash B_{\tilde{h}}\left(x_{k}, \rho\right)$, we have
$$\left|G_{\tilde{h}}\left(x_{k}, y\right)\right|_{\tilde{h}} \leq C e^{-3 d_{h}\left(p\left(x_{k}\right), p(y)\right)}$$

We express this distance function in the coordinates $(u, \theta, s, \phi)$. We parameterize the onesheeted hyperboloid in coordinates ( $u, \theta, s, \phi$ ) and use the well-known explicit expression of the hyperbolic distance. With $x_{k}=\left(u\left(x_{k}\right), 0,0, *\right)$ and $y=(u, \theta, s, \phi)$ the bound (5.39) then reads
$$\left|G_{\tilde{h}}\left(x_{k}, y\right)\right|_{\tilde{h}} \leq C\left(u\left(x_{k}\right) u \cosh (s)-\sqrt{\left(u\left(x_{k}\right)^{2}-1\right)\left(u^{2}-1\right)} \cos (l \theta)\right)^{-3}$$
Now since the volume form is
$$\mathrm{dvol}_{\tilde{h}}=l u^{2} \sinh (s) \mathrm{d} u \mathrm{~d} \theta \mathrm{~d} s \mathrm{~d} \phi$$
we see that
$$\begin{aligned}
& \int_{A_{k} \backslash B_{\tilde{h}}\left(x_{k}, \rho\right)} u(y)^{-\alpha}\left|G_{\tilde{h}}\left(x_{k}, y\right)\right|_{\tilde{h}} \operatorname{dvol}_{\tilde{h}}(y) \lesssim \\
& \quad \int_{A_{k}}\left(u\left(x_{k}\right) u \cosh (s)-\sqrt{\left(u\left(x_{k}\right)^{2}-1\right)\left(u^{2}-1\right)} \cos (l \theta)\right)^{-3} l u^{2-\alpha} \sinh (s) \mathrm{d} u \mathrm{~d} \theta \mathrm{~d} s \mathrm{~d} \phi
\end{aligned}$$
The right-hand side is easily computed with standard integrals. In particular:
$$\begin{aligned}
\int_{A_{k} \backslash B_{\tilde{h}}\left(x_{k}, \rho\right)} u(y)^{-\alpha}\left|G_{\tilde{h}}\left(x_{k}, y\right)\right|_{\tilde{h}} \operatorname{dvol}_{\tilde{h}}(y) & \lesssim \int_{e^{-M} u\left(x_{k}\right)}^{e^{M} u\left(x_{k}\right)} \frac{u^{2-\alpha} \mathrm{d} u}{\left(u\left(x_{k}\right)^{2}+u^{2}\right)^{3 / 2}} \\
& =u\left(x_{k}\right)^{-\alpha} \int_{e^{-M}}^{e^{M}} \frac{u^{2-\alpha} \mathrm{d} u}{\left(1+u^{2}\right)^{3 / 2}}
\end{aligned}$$
This last integral converges both at 0 and $\infty$ when $M \rightarrow \infty$, provided $0<\alpha<3$, completing the proof of the Lemma. \(\square\)

Next we control the integral over the region $B_{k}$, where $\nabla \eta$ is non-zero. We write $B_{k}=B_{k}^{u} \cup B_{k}^{\theta} \cup B_{k}^{s}$ where
$$\begin{aligned}
B_{k}^{u} & =A_{k} \cap\left\{e^{-M} u\left(x_{k}\right) \leq u \leq e^{-M / 2} u\left(x_{k}\right)\right\} \cup A_{k} \cap\left\{e^{M / 2} u\left(x_{k}\right) \leq u \leq e^{M} u\left(x_{k}\right)\right\} \\
B_{k}^{\theta} & =A_{k} \cap\left\{-\frac{3 \pi}{4 l} \leq \theta \leq-\frac{\pi}{2 l}\right\} \cup A_{k} \cap\left\{\frac{\pi}{2 l} \leq \theta \leq \frac{3 \pi}{4 l}\right\} \\
B_{k}^{s} & =A_{k} \cap\{\sigma-2 \leq s \leq \sigma-1\}
\end{aligned}$$

Lemma 5.11. Let $0<\alpha<3$. There is a function $\epsilon: \mathbb{R} \rightarrow \mathbb{R}_{+}$with $\epsilon(M) \rightarrow 0$ as $M \rightarrow \infty$ such that
$$\int_{B_{k}^{u}} u(y)^{-\alpha}\left|G_{\tilde{h}}\left(x_{k}, y\right)\right|_{\tilde{h}} \operatorname{dvol}_{\tilde{h}}(y) \lesssim \epsilon(M) u\left(x_{k}\right)^{-\alpha}$$
Proof. By the same arguments as led to (5.41), the integral over $B_{k}^{u}$ is bounded by
$$\left(\int_{e^{-M}}^{e^{-M / 2}} \frac{u^{2-\alpha} \mathrm{d} u}{\left(1+u^{2}\right)^{3 / 2}}+\int_{e^{M / 2}}^{e^{M}} \frac{u^{2-\alpha} \mathrm{d} u}{\left(1+u^{2}\right)^{3 / 2}}\right) u\left(x_{k}\right)^{-\alpha}$$
Since the integral of $u^{2-\alpha}\left(1+u^{2}\right)^{-3 / 2}$ over the whole of $\mathbb{R}_{+}$is finite, these two tails must tend to zero as $M \rightarrow \infty$. \(\square\)

Lemma 5.12. Let $\alpha>0$. Then, as $k \rightarrow \infty$,
$$\int_{B_{k}^{\theta}} u(y)^{-\alpha}\left|G_{\tilde{h}}\left(x_{k}, y\right)\right|_{\tilde{h}} \operatorname{dvol}_{\tilde{h}}(y)=o\left(u\left(x_{k}\right)^{-\alpha}\right)$$
Proof. By the pointwise control of $G_{\tilde{h}}$ in (5.40), we have
$$\begin{aligned}
\int_{B_{k}^{\theta}} u(y)^{-\alpha}\left|G_{\tilde{h}}\left(x_{k}, y\right)\right|_{\tilde{h}} \mathrm{~d} \operatorname{vol}_{\tilde{h}}(y) & \lesssim u\left(x_{k}\right)^{-3} \int_{u=e^{-M} u\left(x_{k}\right)}^{e^{M} u\left(x_{k}\right)} \int_{s=0}^{\infty} u^{-1-\alpha} \cosh (s)^{-3} \sinh (s) \mathrm{d} u \mathrm{~d} s \\
& \lesssim e^{\alpha M} u\left(x_{k}\right)^{-3-\alpha} \\
& =o\left(u\left(x_{k}\right)^{-\alpha}\right)
\end{aligned}$$ \(\square\)

Lemma 5.13. Let $\alpha>0$. Then, as $k \rightarrow \infty$
$$\int_{B_{k}^{s}} u(y)^{-\alpha}\left|G_{\tilde{h}}\left(x_{k}, y\right)\right|_{\tilde{h}} \mathrm{dvol}_{\tilde{h}}(y)=o\left(u\left(x_{k}\right)^{-\alpha}\right)$$
Proof. By the pointwise control of $G_{\tilde{h}}$ in (5.40), we have
$$\begin{aligned}
\int_{B_{k}^{s}} u(y)^{-\alpha}\left|G_{\tilde{h}}\left(x_{k}, y\right)\right|_{\tilde{h}} \mathrm{dvol}_{\tilde{h}}(y) & \lesssim u\left(x_{k}\right)^{-3} \int_{e^{-M} u\left(x_{k}\right)}^{e^{M} u\left(x_{k}\right)} u^{-1-\alpha} \mathrm{d} u \\
& \lesssim e^{\alpha M} u\left(x_{k}\right)^{-3-\alpha} \\
& =o\left(u\left(x_{k}\right)^{-\alpha}\right)
\end{aligned}$$ \(\square\)

We are finally ready to prove the estimate which contradicts (5.2).
Proposition 5.14. Let $\alpha>0$. As $k \rightarrow \infty$,
$$\left\|s_{k}\right\|_{C_{\alpha}^{0}} \lesssim\left\|L_{\tilde{g}_{k}}\left(s_{k}\right)\right\|_{C_{\alpha}^{0, \eta}}$$
Proof. By (5.38) and Lemmas 5.10, 5.11, 5.12 and 5.13 we have that at the point $x_{k}$ where $u(x)^{\alpha}\left|s_{k}(x)\right|_{g_{k}}$ is maximal,
$$u\left(x_{k}\right)^{\alpha}\left|s_{k}\left(x_{k}\right)\right|_{g_{k}} \lesssim\left\|L_{\tilde{g}_{k}}\left(s_{k}\right)\right\|_{C_{\alpha}^{0}}+o\left(\left\|s_{k}\right\|_{C_{\alpha}^{0}}\right)+\left(\frac{\epsilon(M)}{M}+o(1)\right)\left\|s_{k}\right\|_{C_{\alpha}^{0}}$$
where $\epsilon(M) \rightarrow 0$ as $M \rightarrow \infty$. We now take $M$ very large (but fixed) so that the $\left\|s_{k}\right\|_{C_{\alpha}^{0}}$ terms on the right-hand side can be absorbed on the left. \(\square\)

This Proposition shows that Case 3 cannot actually have occurred after all. Since we have already ruled out the other possibilities, the proof of Theorem 1.2 is complete.

\section*{A Technical results on Green's operators}

For the purpose of this Appendix, we will denote by $\left(M_{k}, g_{k}\right)$ the sequence of complete non-compact negatively curved Riemannian four-manifolds investigated respectively in 5.1 and \$5.2. More precisely, $\left(M_{k}, g_{k}\right)$ will denote:
\begin{itemize}
\item[-] either $\left(\mathbb{H}^{4}, g_{k}\right)$, where $g_{k}$ is the extension of the metric $g_{k}$ (originally constructed in Proposition 3.1) to $\mathbb{H}^{4}$. The extension process is described after (5.9);
\item[-] or $\left(Y_{k}, g_{k}\right)$, where $Y_{k}$ is defined in 55.2 and $g_{k}$ is again the extension of the approximate Einstein metric to $Y_{k}$, interpolated with the hyperbolic metric at large distances.
\end{itemize}

We will also let $\left(\tilde{g}_{k}\right)$ be another family of Riemannian metrics on $M_{k}$, which coincides with $g_{k}$ outside of a compact set $K_{k}$ of $M_{k}$ (possibly depending on $k$ ) and which satisfies
$$\left\|\tilde{g}_{k}-g_{k}\right\|_{C^{m, \eta}\left(M_{k}\right)}=o(1)$$
for some $m \geq 3$ and $0<\eta<1$. In the first case where $M_{k}=\mathbb{H}^{4}$ we will also assume that $\left\|\tilde{g}_{k}-g_{\text {hyp }}\right\|_{C^{m, \eta}\left(\mathbb{H}^{4}\right)}=o(1)$. These assumptions are met when $\tilde{g}_{k}$ is the metric considered in Section 5.1 and 5.2. In both cases, these assumptions imply that $i_{\tilde{g}_{k}}\left(M_{k}\right)$ is uniformly bounded from below by a positive number.

The proof of Theorem 4.15 relies on suitable representation formulae for $L_{\tilde{g}_{k}}$. In this Appendix we construct a fundamental solution for $L_{\tilde{g}_{k}}^{*}$ on $M_{k}$, describe its behavior around the singularity and prove a global $L^{2}$ estimate for it. In the following we let $S=S_{(2,0)}\left(T^{*} M_{k}\right)$ be the bundle of symmetric bilinear forms on $T^{*} M_{k}$. We prove the following result:

Proposition A.1. Let $x \in M_{k}$. There exists a fundamental solution $G_{k}(\cdot, x)$ for $L_{\tilde{g}_{k}}^{*}$ in the following sense: it is a section of the bundle $y \mapsto \operatorname{Hom}\left(S_{x}, S_{y}\right)$ which is in $C^{1, \eta}\left(M_{k} \backslash\{x\}\right)$ and satisfies the following distributional equation:
$$L_{\tilde{g}_{k}}^{*}\left(G_{k}(\cdot, x)\left(f^{i j}(x)\right)\right)=\delta_{x} \cdot f^{i j}(x),$$
for any $1 \leq i, j \leq n$, where $f^{i j}$ is a local orthonormal basis of $S$ around $x$ and parallel at $x$. Also, $G_{k}$ satisfies that:
$$\int_{M_{k} \backslash\left\{d_{\tilde{g}_{k}}(x, y) \leq r\right\}}\left(\left|G_{k}(y, x)\right|_{\tilde{g}_{k}}^{2}+\left|\nabla_{\tilde{g}_{k}} G_{k}(y, x)\right|_{\tilde{g}_{k}}^{2}\right) \operatorname{dvol}_{\tilde{g}_{k}}(y) \leq C(r),$$
and that:
$$\int_{B_{\tilde{g}_{k}}(x, r)}\left(\left|G_{k}(y, x)\right|_{\tilde{g}_{k}(y)}+\left|\nabla_{\tilde{g}_{k}} G_{k}(y, x)\right|_{\tilde{g}_{k}}\right) \operatorname{dvol} \tilde{g}_{k}(y) \leq C(r)$$
for some positive constant $C(r)$ independent of $x$ and $k$ and depending only on $r$.
As a consequence of Proposition A. 1 we get that, for any compactly supported bilinear form $h$ of class $C^{2}$ in $M_{k}$ :
$$h(x)=\int_{M_{k}} G_{k}(y, x)^{t}\left(L_{\tilde{g}_{k}}(h)(y)\right) \mathrm{d} \operatorname{vol}_{\tilde{g}_{k}}(y),$$
where $G_{k}(y, x)^{t}$ is the adjoint of the linear map $G_{k}(y, x): S_{x} \rightarrow S_{y}$.
Proof. For a fixed Riemannian metric, the arguments used here are standard and are an adaptation of the constructions in [4] (see also [34]). The point is to ensure that the constants in (A.2) and (A.3) are independent of $\tilde{g}_{k}$. We sketch the relevant parts of the proof.

An explicit expression for the operator $L_{\tilde{g}_{k}}^{*}$, that we will not write here, can be obtained from formula 4.5. In particular, in a neighbourhood of $x, L_{\tilde{g}_{k}}^{*}$ looks like, at first order, a constant-coefficients elliptic system $L_{k}$ in $\mathbb{R}^{\frac{n(n+1)}{2}}$ satisfying, by (A.1), the Legendre condition. Fundamental solutions for such systems, whose norm behaves as $d_{\tilde{g}_{k}}(x, \cdot)^{2-n}$ around $x$, are known to exist (see for instance [16]). Let $0<\delta_{0}<i_{\widetilde{g}_{k}}\left(M_{k}\right)$. If $H_{k}$ is a fundamental solution of $L_{k}$ we define, for $1 \leq i, j \leq n$ and for $y \in B_{\tilde{g}_{k}}\left(x, \delta_{0}\right) \backslash\{x\}$ :
$$G_{0, k}^{i j}(y, x):=\chi\left(d_{\tilde{g}_{k}}(x, y)\right) H_{k}(\eta)_{p q}^{i j} f^{p q}(y),$$
where $\eta$ is such that $y=\exp _{x}(\eta), \exp _{x}$ is the exponential map at $x$ for $\tilde{g}_{k}$ and $\chi$ is a cut-off function in $\mathbb{R}_{+}$such that $\chi \equiv 1$ in $\left[0, \frac{1}{2} \delta_{0}\right]$ and $\chi \equiv 0$ in $\left[\delta_{0},+\infty\right)$. Equivalently, we denote by $G_{0, k}(y, x)$ the element of $\operatorname{Hom}\left(S_{x}, S_{y}\right)$ such that $G_{0, k}(y, x)\left(f^{i j}(x)\right)=G_{0, k}^{i j}(y, x)$. This is now a global section of $S$, smooth on $M_{k} \backslash\{x\}$, singular at $x$ and compactly supported in $B_{\tilde{g}_{k}}\left(x, \delta_{0}\right)$. Straightforward computations using (A.1) show that the following holds, in a distributional sense:
$$L_{\tilde{g}_{k}}^{*} G_{0, k}^{i j}(\cdot, x)=\delta_{x} f^{i j}(x)+R_{0, k}^{i j}(\cdot, x),$$
where $R_{0, k}^{i j}(y, x)=R_{0, k}(y, x)\left(f^{i j}(x)\right)$ and $R_{0, k}(\cdot, x)$ is a singular section of $S$, supported in $B_{\tilde{g}_{k}}\left(x, \delta_{0}\right)$, satisfying
$$\left|R_{0, k}(y, x)\right|_{\tilde{g}_{k}} \leq C d_{\tilde{g}_{k}}(x, y)^{1-n}$$
for some positive $C$ independent of $x$ and $k$. As a consequence of (A.6) we get that for any $h \in S$ compactly supported and of class $C^{2}$ one has:
$$h(x)=\int_{M_{k}} G_{0, k}(y, x)^{t}\left(L_{\tilde{g}_{k}}(h)(y)\right) \mathrm{d} \operatorname{vol}_{\tilde{g}_{k}}(y)-\int_{M_{k}} R_{0, k}(y, x)^{t}(h(y)) \operatorname{dvol}_{\tilde{g}_{k}}(y)$$

The iterative construction now goes as follows: for any $p \geq 0$ we let
$$G_{p+1, k}^{i j}(y, x)=G_{0, k}^{i j}(y, x)-\sum_{q=0}^{p} \int_{M_{k}} G_{0, k}(y, z) \circ R_{q, k}(z, x)\left(f^{i j}(x)\right) \operatorname{dvol}_{\tilde{g}_{k}}(z),$$
and
$$R_{p+1, k}^{i j}(y, x)=-\int_{M_{k}} R_{0, k}(y, z) \circ R_{p, k}(z, x)\left(f^{i j}(x)\right) \operatorname{dvol}_{\tilde{g}_{k}}(z)$$
By (A.6):
$$L_{\tilde{g}_{k}}^{*} G_{p+1, k}^{i j}(\cdot, x)=\delta_{x} f^{i j}(x)+R_{p+1, k}^{i j}(\cdot, x) .$$
An iterative use of Giraud's lemma (see [23], Lemma 7.5) with (A.5) and (A.7) shows that
$$\left|R_{n-1, k}^{i j}(y, x)\right|_{\tilde{g}_{k}} \leq C\left|\ln d_{\tilde{g}_{k}}(x, y)\right|$$
and that
$$\left|G_{p+1, k}(y, x)\right|_{\tilde{g}_{k}} \leq C d_{\tilde{g}_{k}}(x, y)^{2-n},$$
for some positive $C$ independent of $k, x$, and $y$, for any $0<d_{\tilde{g}_{k}}(x, y) \leq M \delta_{0}$ for some $M>0$. Note also that by construction $R_{n-1, k}^{i j}(\cdot, x)$ is compactly supported in $M_{k}$. It
remains to solve for the remainder term. We claim that there exists a unique bilinear form $N_{k}^{i j}(\cdot, x)$ in $H^{1}\left(M_{k}\right)$ satisfying:
$$L_{\tilde{g}_{k}^{*}}^{*} N_{k}^{i j}(\cdot, x)=-R_{n-1, k}^{i j}(\cdot, x)$$
and
$$\left\|N_{k}^{i j}(\cdot, x)\right\|_{H^{1}\left(M_{k}\right)} \leq C$$
for some positive $C$ independent of $x$ and $k$. The existence of $N_{k}^{i j}(\cdot, x)$ and the bound (A.12) follow from 4.5 and from (A.1), which show that $L_{\tilde{g}_{k}}^{*}$ is $o(1)$-close, in operator norm, to an injective self-adjoint elliptic operator. By (A.10) and since $R_{n-1, k}^{i j}(\cdot, x)$ is compactly supported, it in $L^{p}\left(M_{k}\right)$ for all $p \geq 1$, so standard elliptic regularity theory with (A.1) shows that $N_{k}^{i j}(\cdot, x)$ is of class $C^{1, \eta}$ in $M_{k}$ for all $0<\eta<1$ and that
$$\left\|N_{k}^{i j}(\cdot, x)\right\|_{C^{1, \eta}\left(B_{\tilde{g}_{k}}\left(x, 2 \delta_{0}\right)\right)} \leq C .$$
It remains to define $G_{k}(y, x)=G_{n-1, k}(y, x)+N_{k}(y, x)$, where $G_{n-1, k}(y, x)$ is given by (A.9). There holds then, for any $1 \leq i, j \leq n$ :
$$L_{\tilde{g}_{k}}^{*} G_{k}^{i j}(\cdot, x)=\delta_{x} f^{i j}(x),$$
and (A. 2 ) and (A.3) follow from (A.11), (A.12) and (A.13). \(\square\)

We also remark that by standard elliptic theory applied to the operator $L_{\tilde{g}_{k}}^{*}$, and as a consequence of (A.1), we also get uniform (in $k$ ) $C^{m, \eta}$ bounds on $G_{k}(\cdot, x)$ in every fixed compact set of $M_{k} \backslash\{x\}$.

\section*{References}
\begin{itemize}
\item[] [1] M. T. Anderson, Dehn filling and Einstein metrics in higher dimensions, J. Differential Geom. 73 (2006), no. 2, 219-261.
\item[] [2] Michael T. Anderson, Geometric aspects of the AdS/CFT correspondence, AdS/CFT correspondence: Einstein metrics and their conformal boundaries, IRMA Lect. Math. Theor. Phys., vol. 8, Eur. Math. Soc., Zürich, 2005, pp. 1-31. MR 2160865
\item[] [3] T. Aubin, Équations du type Monge-Ampère sur les variétés kählériennes compactes, Bull. Sci. Math. (2) 102 (1978), no. 1, 63-95.
\item[] [4] $\_\_\_\_$, Nonlinear Analysis on Manifolds. Monge-Ampère Equations, Grundlehren der mathematischen Wissenshaften, vol. 252, Springer-Verlag New York, 1982.
\item[] [5] R. H. Bamler, Construction of Einstein metrics by generalized Dehn filling, J. Eur. Math. Soc. 14 (2012), no. 3, 887-909.
\item[] [6] M. Berger, Les variétés riemanniennes 1/4 pincées, Ann. Scuola Norm. Pisa 14 (1960), 161-170.
\end{itemize}
\begin{itemize}
\item[] [7] Arthur L. Besse, Einstein manifolds, Classics in Mathematics, Springer-Verlag, Berlin, 2008, Reprint of the 1987 edition. MR 2371700
\item[] [8] G. Besson, G. Courtois, and S. Gallot, Entropies et rigidité des espaces localement symétriques de courbure strictement négative, Geom. Funct. Anal. 5 (1995), no. 5, 731-799.
\item[] [9] O. Biquard, Polycopié on Differential Geometry and Global Analysis, Unpublished lecture notes, available at math.ens.fr/ ${ }^{\sim}$ biquard/dgga2007.pdf, 2007.
\item[] [10] Olivier Biquard, Métriques d'Einstein asymptotiquement symétriques, Astérisque (2000), no. 265, vi+109. MR 1760319
\item[] [11] S. Brendle and R. Schoen, Manifolds with 1/4-pinched curvature are space forms, J. Amer. Math. Soc. 22 (2009), 287-307.
\item[] [12] P. Buser and P. Sarnack, On the period matrix of a Riemann surface of large genus, Invent. Math. 117 (1994), no. 1, 27-56, With appendix by J. Conway and N. Sloane.
\item[] [13] P. Chruściel and W. Simon, Towards the classification of static vacuum spacetimes with negative cosmological constant, J. Math. Phys. 42 (2001), 1779-1817.
\item[] [14] V. Cortés and A. Saha, Quarter-pinched Einstein metrics interpolating between real and complex hyperbolic metrics, Math. Z. 290 (2018), no. 1-2, 155-166. MR 3848428
\item[] [15] E. Delay, Essential spectrum of the Lichnerowicz Laplacian on two-tensors on asymptotically hyperbolic manifolds, J. Geom. Phys. 43 (2002), no. 1, 33-44.
\item[] [16] G. Dolzmann and S. Müller, Estimates for Green's matrices of elliptic systems by $l^{p}$-theory, Manuscripta Math. 88 (1995), no. 1, 261-273.
\item[] [17] J. Fine, Constant scalar curvature Kähler metrics on fibred complex surfaces, J. Differential Geom. 68 (2004), no. 3, 397-432.
\item[] [18] J. Fine, K. Krasnov, and D. Panov, A gauge theoretic approach to Einstein 4manifolds, New York J. Math. 20 (2014), 293-323.
\item[] [19] J. Fine and D. Panov, Symplectic Calabi-Yau manifolds, minimal surfaces and the hyperbolic geometry of the conifold, J. Differential Geom. 82 (2009), no. 1, 155-205.
\item[] [20] R. C. Graham and J. M. Lee, Einstein metrics with prescribed conformal infinity on the ball, Adv. Math. 87 (1991), no. 2, 186-225.
\item[] [21] M. Gromov and W. Thurston, Pinching constants for hyperbolic manifolds, Invent. Math. 89 (1987), no. 1, 1-12.
\item[] [22] L. Guth and A. Lubotzky, Quantum error correcting codes and 4-dimensional arithmetic hyperbolic manifolds, J. Math. Phys. 55 (2014), no. 8, 13pp.
\item[] [23] E. Hebey, Compactness and Stability for Nonlinear Elliptic Equations, Zurich Lectures in Advanced Mathematics, European Mathematical Society, 2014.
\end{itemize}
\begin{itemize}
\item[] [24] F. Hirzebruch, The signature of ramified coverings, Global analysis. Papers in honor of K. Kodaira, University of Tokyo Press and Princeton University Press, 1969, pp. 253-265.
\item[] [25] G. R. Jensen, Homogeneous Einstein spaces of dimension four, J. Differential Geom. 3 (1969), 309-349.
\item[] [26] Michael Kapovich, Convex projective structures on gromov-thurston manifolds, Geom. Topol. 11 (2007), no. 3, 1777-1830.
\item[] [27] M. G. Katz, M. Schaps, and U. Vishne, Logarithmic growth of systole of arithmetic Riemann surfaces along congruence subgroups, J. Differential Geom. 76 (2007), no. 3, 399-422.
\item[] [28] W. Klingenberg, Über Riemannsche Mannigfaltigkeiten mit positiver Krümmung, Comment. Math. Helv. 35 (1961), 47-54.
\item[] [29] N. Koiso, Non-deformability of Einstein metrics, Osaka J. Math. 15 (1978), 419-433.
\item[] [30] C. LeBrun, Einstein metrics and Mostow rigidity, Math. Res. Lett. 2 (1995), 1-8.
\item[] [31] J. Lee, Fredholm Operators and Einstein Metrics on Conformally Compact Manifolds, Memoirs of the American Mathematical Society, American Mathematical Society, 2006.
\item[] [32] P. G. P. Murillo, Systole of congruence coverings of arithmetic hyperbolic manifolds, arXiv e-print (2016), arxiv:1610.03870.
\item[] [33] H Pedersen, Einstein metrics, spinning top motions and monopoles, Math. Ann. 274 (1986), 35-59.
\item[] [34] F. Robert, Existence et asymptotiques optimales des fonctions de Green des opérateurs elliptiques d'ordre deux, Unpublished notes, available at http://www.iecl.univlorraine.fr/ ${ }^{\sim}$ Frederic.Robert/ConstrucGreen.pdf, 2010.
\item[] [35] W. P. Thurston, The Geometry and Topology of Three-Manifolds, Lecture notes distributed by Princeton University, available at http://library.msri.org/books/gt3m/, 1980.
\item[] [36] P. Topping, Lectures on the Ricci Flow, London Mathematical Society Lecture Note Series, Cambridge University Press, 2006.
\item[] [37] S.-T. Yau, On the Ricci curvature of a compact Kähler manifold and the complex Monge-Ampère equation. I, Comm. Pure Appl. Math. 31 (1978), no. 3, 339-411.
\end{itemize}