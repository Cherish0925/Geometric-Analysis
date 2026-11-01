---
retention_scope: session
part: 2
total_parts: 4
---

[Part 2/4 of: [math/0206047] Seiberg-Witten-Floer Homology and Gluing Formulae]

Let $(A(t), \psi(t))$ represent a flowline in $\mathcal{M}(\alpha, \beta)$, then any flowline in the same component as $[A(t), \psi(t)]$ has constant energy, given by
$$\mathcal{C}_{\eta}(A(-\infty), \psi(-\infty))-\mathcal{C}_{\eta}(A(\infty), \psi(\infty)),$$
where $(A(-\infty), \psi(-\infty))$ and $(A(\infty), \psi(\infty))$ are two asymptotic limits of $(A(t), \psi(t))$ as $t \rightarrow \pm \infty$, whose existence follows from Corollary 3.10. There is a constant $\delta>0$ depending on the critical points, a constant $C$ depending only on the local geometry of $Y$ and perturbation $\eta$ such that for sufficiently large $T$
$$\sum_{0 \leq k \leq 2}\left(\left|\nabla^{k}\left(A(t)-A_{ \pm \infty}\right)\right|+\mid\left(\nabla_{A_{ \pm \infty}}\right)^{k}(\psi(t)-\psi( \pm \infty) \mid) \leq C e^{-\delta(|t|-T)}\right.$$
for $t \in(-\infty, T]$ and $t \in[T, \infty)$ respectively.
In this subsection, we will prove that generically each component of the moduli space $\mathcal{M}(\alpha, \beta)$ is a smooth manifold with dimension prescribed by the index theorem. We remind the reader that we always identify a path $(A(t), \psi(t))$ in $\mathcal{A}$ with a pair consisting of a $U(1)$-connection on the determinant bundle of the pull-back Spin ${ }^{c}$ structure and a spinor on $\pi^{*}(W)$ in temporal gauge.

To achieve transversality for the moduli space $\mathcal{M}(\alpha, \beta)$, we need to perturb the gradient flow equations in a non-local fashion:
$$\left\{\begin{array}{l}
\frac{\partial A}{\partial t}=-* F_{A}+\sigma(\psi, \psi)+\eta(A, \psi) \\
\frac{\partial \psi}{\partial t}=-\not \partial_{A}(\psi)-\nu(A, \psi) \cdot \psi+\phi(A, \psi)
\end{array}\right.$$
where $\eta(A, \psi), \nu(A, \psi)$ and $\phi(A, \psi)$ are functions of $(A, \psi)$. This general perturbation is chosen so as to preserve translation invariance of the gradient flow equation under the action of $\mathbb{R}$.

We now describe in detail how to construct such perturbations. For any Riemannian 3-manifold $(Y, g)$ with a $\operatorname{Spin}^{c}$ structure $\mathfrak{s}$, we choose a complete $L^{2}$-basis $\left\{\nu_{j}\right\}_{j=1}^{\infty}$ for the imaginary-valued 1-forms on $Y$, and a complete $L^{2}$-basis $\left\{\mu_{j}\right\}_{j=1}^{\infty}$ for the co-closed imaginary-valued 1-forms on $Y$. Under the Hodge decomposition,
$$\Omega_{L^{2}}^{1}(Y, i \mathbb{R})=H^{1}(Y, i \mathbb{R}) \oplus \operatorname{Im}\left(d^{*}\right) \oplus \operatorname{Im}(d),$$
$\left\{\mu_{j}\right\}_{j=1}^{\infty}$ span the space $H^{1}(Y, i \mathbb{R}) \oplus I m\left(d^{*}\right)$ and $\left\{\nu_{j}\right\}_{j=1}^{\infty}$ span the space $\Omega_{L^{2}}^{1}(Y, i \mathbb{R})$. We also need to choose a complete $L^{2}$-basis $\left\{\psi_{j}\right\}_{j=1}^{\infty}$ for the sections of the spinor bundle $W$. They are eigenvectors of the fixed Dirac operator $\not \partial_{A_{0}}$ for a a fixed $U(1)$-connection $A_{0}$ on the determinant
bundle $\operatorname{det}(\mathfrak{s})$. For each co-closed 1-form $\mu_{j}$, we associate a function on the configuration space $\mathcal{A}$ by
$$\tau_{j}(A, \psi)=\tau_{j}\left(A-A_{0}\right)=\int_{Y}\left(A-A_{0}\right) \wedge * \mu_{j} .$$
For simplicity, we assume that $\left\{\mu_{j}\right\}_{j=1}^{b_{1}}$ consist of a basis of $H^{1}(Y, i \mathbb{R})$, and $\left[* \mu_{j}\right]=0$ for $j>b_{1}$. It is easy to see that:
\begin{itemize}
\item[(1)] $\tau_{j}$ is invariant under gauge transformations for $j>b_{1}$;
\item[(2)] for the map obtained from the first $b_{1}$ functions
$$\left(\tau_{1}, \cdots, \tau_{b_{1}}\right): \mathcal{A} \rightarrow \mathbb{R}^{b_{1}},$$
\end{itemize}
the gauge transformation $g: Y \rightarrow U(1)$ on $\mathcal{A}$ commutes with the $H^{1}(Y, \mathbb{Z}) \cong \mathbb{Z}^{b_{1}}$-action on $\mathbb{R}^{b_{1}}$ by translation by the vector
$$<\left(\left[g^{-1} d g\right] \cup\left[* \mu_{1}\right],\left[g^{-1} d g\right] \cup\left[* \mu_{2}\right], \cdots,\left[g^{-1} d g\right] \cup\left[* \mu_{b_{1}}\right]\right),[Y]>.$$

To each imaginary-valued 1-form $\nu_{j}$ we associate a function $\zeta_{j}$ on $\mathcal{A}$ as follows
$$\zeta_{j}(A, \psi)=\zeta_{j}(\psi, \psi)=\int_{Y}\left\langle\nu_{j} \cdot \psi, \psi\right\rangle d v o l_{Y}$$
where $\langle$,$\rangle is the Hermitian metric on the space of spinors. It is easy to see that \zeta_{j}$ is gauge invariant and real-valued. We also define $\zeta_{j}(\psi, \phi)=2 \int_{Y} \operatorname{Re}\left\langle\nu_{j} . \psi, \phi\right\rangle d v o l_{Y}$.

To each $\psi_{j}$, we associate a function $\xi_{j}$ on $\mathcal{A}$ as follows
$$\xi_{j}(A, \psi)=\int_{Y}\left\langle e^{-\frac{1}{2} G d^{*}\left(A-A_{0}\right)} \psi_{j}, \psi\right\rangle d v o l_{Y}$$
where $G$ is the Green's operator for the ordinary Laplacian on $L^{2}(Y)$. Let $\psi_{j}^{A}=e^{-\frac{1}{2} G d^{*}\left(A-A_{0}\right) \psi_{j}}$. Then $\xi_{j}$ is invariant under the action of the subgroup
$$H=\left\{e^{i f} \mid f: Y \rightarrow \mathbb{R}, \int_{Y} f d v o l_{Y}=0\right\}$$
of the identity component of the gauge group $\mathcal{G}_{Y}$ where $\mathcal{G}_{Y} / H \cong S^{1} \times H^{1}(Y, \mathbb{Z})$. The action of the $S^{1}$-factor has weight -1, that is, for $u \in S^{1}$,
$$\xi_{j}(u(A, \psi))=u^{-1} \xi_{j}(A, \psi) .$$

For any $n \geq b_{1}(Y), k \geq 0$ and $l \geq 0,(\tau, \zeta, \xi)=\left(\tau_{1}, \cdots, \tau_{n}, \zeta_{1}, \cdots, \zeta_{k}, \xi_{1}, \cdots, \xi_{l}\right)$ defines a $\operatorname{map} \mathcal{A} \rightarrow \mathbb{R}^{n} \times \mathbb{R}^{k} \times \mathbb{C}^{l}$ with the following key property.

Lemma 3.11. For any two points $\left(A_{1}, \psi_{1}\right)$ and $\left(A_{2}, \psi_{2}\right)$ in $\mathcal{A}$ representing two different points in $\mathcal{B}$, there exist $n, k$ and $l$ such that
$$(\tau, \zeta, \xi)\left(A_{1}, \psi_{1}\right) \neq(\tau, \zeta, \xi)\left(A_{2}, \psi_{2}\right) .$$

Proof. On the contrary, suppose that for any $n, k$ and $l,\left(\tau_{1}, \cdots, \tau_{n}, \zeta_{1}, \cdots, \zeta_{k}, \xi_{1}, \cdots, \xi_{l}\right)$ takes the same values on $\left(A_{1}, \psi_{1}\right)$ and $\left(A_{2}, \psi_{2}\right)$. Then from the definition of $\tau_{j}$, we know that $A_{1}=A_{2}-i d f$ for some real-valued function $f$ on $Y$, and from the definition of $\xi_{j}$, we know that
$$e^{-\frac{1}{2} G d^{*}\left(A_{1}-A_{0}\right)} \psi_{1}=e^{-\frac{1}{2} G d^{*}\left(A_{2}-A_{0}\right)} \psi_{2},$$
which implies that $\psi_{1}=e^{\frac{i}{2} f} \psi$. Hence $\left(A_{1}, \psi_{1}\right)$ and $\left(A_{2}, \psi_{2}\right)$ are gauge equivalent. This contradicts the assumption of the lemma. \(\square\)

As a corollary we have injectivity of the induced map
$$(\tau, \zeta, \xi): \mathcal{B} \rightarrow \bigcup\left(\mathbb{R}^{n} \times \mathbb{R}^{k} \times \mathbb{C}^{l}\right) /\left(H^{1}(Y, \mathbb{Z}) \times S^{1}\right) s,$$
which implies that there are sufficiently many perturbations to achieve the transversality of the moduli spaces of flowlines. This will be crucial in the proof of Proposition 3.16.

Now we choose any function $\mathfrak{p} \in C^{\infty}\left(\mathbb{R}^{n} \times \mathbb{R}^{k} \times \mathbb{C}^{l}, \mathbb{R}\right)$ (for $n \geq b_{1}, k, l>0$ ) where $\mathfrak{p}$ is invariant under the action of $H^{1}(Y, Z)$ on $\mathbb{R}^{b_{1}}$ (the first $b_{1}$-components of $\mathbb{R}^{N}$ ), and invariant under the action of $S^{1} \times H^{1}(Y, \mathbb{Z})$ on $\mathbb{C}^{l}$. We can define a function on $\mathcal{A} / \mathcal{G}$ by composition:
$$\mathfrak{p}\left(\tau_{1}, \cdots, \tau_{n}, \zeta_{1}, \cdots, \zeta_{k}, \xi_{1}, \cdots, \xi_{l}\right) .$$
Let $\mathcal{C}_{\eta}$ be the Chern-Simons-Dirac function as in (14). We can perturb this functional to form
$$\mathcal{C}_{\eta, \mathfrak{p}}=\mathcal{C}_{\eta}+\mathfrak{p}\left(\tau_{1}, \cdots, \tau_{n}, \zeta_{1}, \cdots, \zeta_{k}, \xi_{1}, \cdots, \xi_{l}\right) .$$

Let $\mathcal{P}$ be the subspace of $\bigcup_{n \geq b_{1}, k, l>0} C^{\infty}\left(\mathbb{R}^{n} \times \mathbb{R}^{k} \times \mathbb{C}^{l}, \mathbb{R}\right)$ which is invariant under the above action of $H^{1}(Y, \mathbb{Z}) \times S^{1} \times H^{1}(Y, \mathbb{Z})$ and has finite Floer $\epsilon$ norm. To be specific, choose $\underline{\epsilon}=\left(\epsilon_{k}\right)_{k \in \mathbb{N}}$ to be a given sequence of positive real numbers, then the Floer $\epsilon$-norm (cf. [9]): is given by
$$\|\mathfrak{p}\|_{\underline{\epsilon}}=\sum_{k \geq 0} \epsilon_{k} \sup \left|\nabla^{k} \mathfrak{p}\right| .$$
By arguments similar to those in Lemma 5.1 of [9], the sequence $\underline{\epsilon}$ can be chosen such that $\mathcal{P}$ is a Banach space and $\mathcal{P}$ is dense in the subspace of $L_{k}^{2}$, whose elements are invariant under the above action of $H^{1}(Y, \mathbb{Z}) \times S^{1} \times H^{1}(Y, \mathbb{Z})$.

For each $\mathfrak{p} \in \mathcal{P}$, the gradient of $\mathcal{C}_{\eta, \mathfrak{p}}$ at $[A, \psi]$ with respect to the natural $L^{2}$ inner product is given by
$$\begin{gathered}
\left(* F_{A}-\sigma(\psi, \psi)-\eta-\sum_{j=1}^{n} \frac{\partial \mathfrak{p}}{\partial \tau_{j}} \mu_{j}+\sum_{j=1}^{l} \frac{\partial \mathfrak{p}}{\partial \xi_{j}} d \circ G\left(i \operatorname{Im}<\psi_{j}^{A}, \psi>\right),\right. \\
\left.\not \partial_{A}(\psi)+\sum_{j=1}^{K} \frac{\partial \mathfrak{p}}{\partial \zeta_{j}} \nu_{j} \cdot \psi+\sum_{j=1}^{l} \frac{\partial \mathfrak{p}}{\partial \xi_{j}} \psi_{j}^{A}\right) .
\end{gathered}$$

Here $\nabla \mathfrak{p}=\left(-\sum_{j=1}^{n} \frac{\partial \mathfrak{p}}{\partial \tau_{j}} \mu_{j}+\sum_{j=1}^{l} \frac{\partial \mathfrak{p}}{\partial \xi_{j}} d \circ G\left(i \operatorname{Im}<\psi_{j}^{A}, \psi>\right), \sum_{j=1}^{K} \frac{\partial \mathfrak{p}}{\partial \zeta_{j}} \nu_{j} . \psi+\sum_{j=1}^{l} \frac{\partial \mathfrak{p}}{\partial \xi_{j}} \psi_{j}^{A}\right)$.
In order not to change the critical points of $\mathcal{C}_{\eta}$ when perturbed by $\mathfrak{p}$, we need to impose some condition on $\mathfrak{p} \in \mathcal{P}$. We remind the reader that, as in Lemma 3.3, given a small $\epsilon>0$, there is a constant $\lambda$, such that
$$\left\|\nabla \mathcal{C}_{\eta}([A, \psi])\right\|_{L^{2}}=\left\|\left(* F_{A}-\sigma(\psi, \psi)-\eta, \not \partial_{A}(\psi)\right)\right\|_{L^{2}}>\lambda$$
for $[A, \psi]$ at $L_{1}^{2}$-distance at least $\epsilon$ away from the set of critical points. For each critical point $\alpha \in \mathcal{M}_{Y}(\mathfrak{s}, \eta)$, let $B(\alpha, \epsilon)$ be ball of radius $\epsilon$ centered at $\alpha$ in the $L_{1}^{2}$ topology.

Condition 3.12. We require that the perturbation function $\mathfrak{p} \in \mathcal{P}$ satisfies the following conditions:
\begin{itemize}
\item[1.] $\mathfrak{p}=0$ on $\bigcup_{\alpha \in \mathcal{M}_{Y}(\mathfrak{s}, \eta)}(\tau, \zeta, \tau)(B(\alpha, \epsilon))$.
\item[2.] The corresponding perturbation term $\nabla \mathfrak{p}$ has $L^{2}$-norm less than $\epsilon_{0} \lambda$ for a sufficiently small $\epsilon_{0} \ll 1$.
\end{itemize}
Let $\mathcal{P}_{c}$ be the set of perturbation functions $\mathfrak{p} \in \mathcal{P}$ satisfying (a) and (b).
The corresponding downward gradient flow equation of $\mathcal{C}_{\mathfrak{p}}$ is given by
$$\left\{\begin{aligned}
\frac{\partial A}{\partial t} & =-* F_{A}+\sigma(\psi, \psi)+\eta+\sum_{j=1}^{N} \frac{\partial \mathfrak{p}}{\partial \tau_{j}} \mu_{j}-\sum_{j=1}^{l} \frac{\partial \mathfrak{p}}{\partial \xi_{j}} d \circ G\left(i \operatorname{Im}<\psi_{j}^{A}, \psi>\right) \\
\frac{\partial \psi}{\partial t} & =-\not \partial_{A} \psi-\sum_{j=1}^{K} \frac{\partial \mathfrak{p}}{\partial \zeta_{j}} \nu_{j} \cdot \psi-\sum_{j=1}^{l} \frac{\partial \mathfrak{p}}{\partial \xi_{j}} \psi_{j}^{A}
\end{aligned}\right.$$
for a pair $(A(t), \Phi(t))$ regarded as a family of connections and spinors. These are the perturbed 4-dimensional Seiberg-Witten equations on $Y \times \mathbb{R}$ in temporal gauge. The corresponding perturbation of the Seiberg-Witten equations on $Y \times \mathbb{R}$ is given by
$$\left\{\begin{array}{l}
F_{A}^{+}=q(\psi, \psi)+\eta^{+}+\sum_{j=1}^{N} \frac{\partial \mathfrak{p}}{\partial \tau_{j}} \mu_{j}^{+}-\sum_{j=1}^{l} \frac{\partial \mathfrak{p}}{\partial \xi_{j}}\left(d \circ G\left(i \operatorname{Im}<\psi_{j}^{A}, \psi>\right)\right)^{+} \\
\not D_{A}(\psi)+\sum_{j=1}^{K} \frac{\partial \mathfrak{p}}{\partial \zeta_{j}} \nu_{j} \cdot \psi+\sum_{j=1}^{l} \frac{\partial \mathfrak{p}}{\partial \xi_{j}} \psi_{j}^{A}=0
\end{array}\right.$$
where $\mu_{j}^{+}=\frac{1}{2}\left(*_{3} \mu_{j}+\mu_{j} \wedge d t\right)$ and $\left(d \circ G\left(i I m<\psi_{j}^{A}, \psi>\right)\right)^{+}$is the self-dual part of $d \circ G\left(i I m<\psi_{j}^{A}, \psi>\right) \wedge d t$, and the function $\mathfrak{p}$ is the corresponding function on the 4-dimensional configuration space of $U(1)$-connections and spinors on $\left(\mathbb{R} \times Y d t^{2}+g\right)$ with the pull back $\operatorname{Spin}^{c}$ structure. Note that $\mathfrak{p}$ is invariant under gauge transformations. It is easy to see that $\mathfrak{p}$ is a well-defined function over the 4-dimensional configuration space. For any solution $(A(t), \psi(t))$ to the perturbed Seiberg-Witten equations (30) on $\left[R_{1}, R_{2}\right] \times Y$ in temporal gauge, we say that
$(A(t), \psi(t))$ has finite energy if and only if
$$\int_{R_{1}}^{R_{2}}\left(\left\|\frac{\partial A(t)}{\partial t}\right\|_{L^{2}(Y)}^{2}+\left\|\frac{\partial \psi(t)}{\partial t}\right\|_{L^{2}(Y)}^{2}\right) d t<\infty .$$

Lemma 3.13. Let $\gamma(t)=(A(t), \psi(t))$ be a solution to the perturbed Seiberg-Witten equations (30) on $\left[R_{1}, R_{2}\right] \times Y$ in temporal gauge, then $(A(t), \psi(t))$ has finite energy if and only if one of the following terms is finite:
\begin{itemize}
\item[1.] $\mathcal{C}_{\eta}\left(A\left(R_{1}\right), \psi\left(R_{1}\right)\right)-\mathcal{C}_{\eta}\left(A\left(R_{2}\right), \psi\left(R_{2}\right)\right)$,
\item[2.] $\mathcal{C}_{\eta, \mathfrak{p}}\left(A\left(R_{1}\right), \psi\left(R_{1}\right)\right)-\mathcal{C}_{\eta, \mathfrak{p}}\left(A\left(R_{2}\right), \psi\left(R_{2}\right)\right)$,
\item[3.] $\mathcal{C}\left(A\left(R_{1}\right), \psi\left(R_{1}\right)\right)-\mathcal{C}\left(A\left(R_{2}\right), \psi\left(R_{2}\right)\right)$,
\item[4.] $E_{\left[R_{1}, R_{2}\right] \times Y}(\mathbb{A}, \Psi)$ (as defined in (21)), where $(\mathbb{A}, \Psi)=(A(t), \psi(t))$ is the corresponding 4-dimensional monopole on $\left[R_{1}, R_{2}\right] \times Y$.
\end{itemize}

Proof. Note that $\gamma(t)=(A(t), \psi(t))$ satisfies the perturbed Seiberg-Witten equations (30) on $\left[R_{1}, R_{2}\right] \times Y$ in temporal gauge, that is, $\frac{\partial \gamma(t)}{\partial t}=-\nabla \mathcal{C}_{\eta, \mathfrak{p}}(\gamma(t))$, hence we have
$$\begin{aligned}
& \mathcal{C}_{\eta}\left(A\left(R_{1}\right), \psi\left(R_{1}\right)\right)-\mathcal{C}_{\eta}\left(A\left(R_{2}\right), \psi\left(R_{2}\right)\right) \\
= & -\int_{R_{1}}^{R_{2}}<\nabla \mathcal{C}_{\eta}(\gamma(t)), \frac{\partial \gamma(t)}{\partial t}>d t \\
= & \int_{R_{1}}^{R_{2}}<\nabla \mathcal{C}_{\eta}(\gamma(t)), \nabla \mathcal{C}_{\eta, \mathfrak{p}}(\gamma(t))>d t \\
= & \int_{R_{1}}^{R_{2}}\left(\left\|\nabla \mathcal{C}_{\eta}(\gamma(t))\right\|_{L^{2}}^{2}+<\nabla \mathcal{C}_{\eta}(\gamma(t)), \nabla \mathfrak{p}(\gamma(t))>\right) d t .
\end{aligned}$$
and
$$\begin{aligned}
& \mathcal{C}_{\eta, \mathfrak{p}}\left(A\left(R_{1}\right), \psi\left(R_{1}\right)\right)-\mathcal{C}_{\eta, \mathfrak{p}}\left(A\left(R_{2}\right), \psi\left(R_{2}\right)\right) \\
= & -\int_{R_{1}}^{R_{2}}<\nabla \mathcal{C}_{\eta, \mathfrak{p}}(\gamma(t)), \frac{\partial \gamma(t)}{\partial t}>d t \\
= & \int_{R_{1}}^{R_{2}}\left\|\frac{\partial \gamma(t)}{\partial t}\right\|_{L^{2}}^{2} d t \\
= & \int_{R_{1}}^{R_{2}}\left\|\nabla \mathcal{C}_{\eta, \mathfrak{p}}(\gamma(t))\right\|_{L^{2}}^{2} d t .
\end{aligned}$$
From Condition 3.12, we get
$$\left\|\nabla \mathcal{C}_{\eta}(\gamma(t))-\nabla \mathcal{C}_{\eta, \mathfrak{p}}(\gamma(t))\right\|_{L^{2}}<\epsilon_{0}\left\|\mathcal{C}_{\eta}(\gamma(t))\right\|_{L^{2}} .$$
Putting all these together and setting $\epsilon=\epsilon_{0} / 5$, we have
$$1-\epsilon<\frac{\mathcal{C}_{\eta}\left(A\left(R_{1}\right), \psi\left(R_{1}\right)\right)-\mathcal{C}_{\eta}\left(A\left(R_{2}\right), \psi\left(R_{2}\right)\right.}{\mathcal{C}_{\eta, \mathfrak{p}}\left(A\left(R_{1}\right), \psi\left(R_{1}\right)\right)-\mathcal{C}_{\eta, \mathfrak{p}}\left(A\left(R_{2}\right), \psi\left(R_{2}\right)\right)}<1+\epsilon .$$

Similarly, under the condition that $\eta$ is sufficiently small as in Remark 3.4, we can prove that
$$1-\epsilon<\frac{\mathcal{C}_{\eta}\left(A\left(R_{1}\right), \psi\left(R_{1}\right)\right)-\mathcal{C}_{\eta}\left(A\left(R_{2}\right), \psi\left(R_{2}\right)\right.}{\mathcal{C}\left(A\left(R_{1}\right), \psi\left(R_{1}\right)\right)-\mathcal{C}\left(A\left(R_{2}\right), \psi\left(R_{2}\right)\right)}<1+\epsilon,$$

These last two inequalities imply that $\gamma(t)$ has finite energy if and only if any one of $\mathcal{C}_{\eta}\left(\gamma\left(R_{1}\right)\right)-\mathcal{C}_{\eta}\left(\gamma\left(R_{2}\right)\right), \mathcal{C}\left(A\left(R_{1}\right), \psi\left(R_{1}\right)\right)-\mathcal{C}\left(A\left(R_{2}\right), \psi\left(R_{2}\right)\right)$ or $\mathcal{C}_{\eta, \mathfrak{p}}\left(\gamma\left(R_{1}\right)\right)-\mathcal{C}_{\eta, \mathfrak{p}}\left(\gamma\left(R_{2}\right)\right)$ is finite.

For the proof of part (4), direct calculation leads to the following identities:
$$\begin{aligned}
& \mathcal{C}_{\eta}\left(A\left(R_{1}\right), \psi\left(R_{1}\right)\right)-\mathcal{C}_{\eta}\left(A\left(R_{2}\right), \psi\left(R_{2}\right)\right) \\
= & \frac{1}{2} \int_{\left[R_{1}, R_{2}\right] \times Y}\left(F_{\mathbb{A}}-* \eta\right) \wedge\left(F_{\mathbb{A}}-* \eta\right) \\
& +\int_{\left\{R_{1}\right\} \times Y}<\psi, \not D_{A} \psi>d v o l_{Y}-\int_{\left\{R_{2}\right\} \times Y}<\psi, \not \partial A_{A} \psi>d v o l_{Y} .
\end{aligned}$$
and
$$\begin{aligned}
& \mathcal{C}\left(A\left(R_{1}\right), \psi\left(R_{1}\right)\right)-\mathcal{C}\left(A\left(R_{2}\right), \psi\left(R_{2}\right)\right) \\
= & \frac{1}{2} \int_{\left[R_{1}, R_{2}\right] \times Y} F_{\mathbb{A}} \wedge F_{\mathbb{A}} \\
& +\int_{\left\{R_{1}\right\} \times Y}<\psi, \not \partial_{A} \psi>d v o l_{Y}-\int_{\left\{R_{2}\right\} \times Y}<\psi, \not \partial_{A} \psi>d v o l_{Y} .
\end{aligned}$$

To prove the last claim, we write the perturbed Seiberg-Witten equations (30) as follows:
$$\left\{\begin{array}{l}
F_{\mathbb{A}}^{+}=q(\Psi, \Psi)+\mu^{+}+\mathfrak{p}_{\mathbb{A}}^{+} \\
\not D_{\mathbb{A}}(\Psi)+\mathfrak{p}_{\Psi}=0 .
\end{array}\right.$$
where $q(\Psi, \Psi)=(d t \wedge \sigma(\psi, \psi))^{+}$and $\left(\mathfrak{p}_{\mathbb{A}}^{+}, \mathfrak{p}_{\Psi}\right)$ is the perturbation term coming from the perturbation $\mathfrak{p}$ (see (30) for exact expression), notice that, by Condition 3.12, the $L^{2}$-norm of $\left(\mathfrak{p}_{A}^{+}, \mathfrak{p}_{\psi}\right)$ is less than $\epsilon_{0}\left\|\nabla \mathcal{C}_{\eta}\right\|_{L^{2}}$ for a sufficiently small $\epsilon_{0} \ll 1$.

Now we calculate
$$\int_{\left[R_{1}, R_{2}\right] \times Y}\left(\left|\not D_{\mathbb{A}}(\Psi)\right|^{2}+\left|F_{\mathbb{A}}^{+}-q(\Psi, \Psi)-\mu^{+}\right|^{2}\right) d t d v o l_{Y}$$
using the 3- and 4-dimensional Weitzenböck formulae
The 4-dimensional Weitzenböck formula is
$$\not D_{\mathbb{A}}^{*} \not D_{\mathbb{A}}(\Psi)=\nabla_{\mathbb{A}}^{*} \nabla_{\mathbb{A}} \Psi+\frac{s}{4} \Psi+\frac{1}{2} F_{\mathbb{A}}^{+} \cdot \Psi,$$
where $s$ denotes the scalar curvature on $\left(\mathbb{R} \times Y, g_{Y}+d t^{2}\right)$. Take the inner product of both sides with $\Psi=\psi(t)$, and then integrate them over $\left[R_{1}, R_{2}\right] \times Y$. Here we need to understand the boundary contribution when we integrate by parts. To see what this contribution is, we proceed
as follows
$$\begin{aligned}
& \int_{\left[R_{1}, R_{2}\right] \times Y}\left|\not D_{\mathbb{A}} \Psi\right|^{2} d t d v o l_{Y} \\
= & \int_{\left[R_{1}, R_{2}\right] \times Y}\left(\left|\frac{\partial \psi(t)}{\partial t}+\not \partial_{A} \psi\right|^{2}\right) d t d v o l_{Y} \\
= & \int_{\left[R_{1}, R_{2}\right] \times Y}\left(\left|\frac{\partial \psi(t)}{\partial t}\right|^{2}+\left|\not \partial_{A} \psi\right|^{2}+<\frac{\partial \psi(t)}{\partial t}, \not \partial_{A} \psi>+<\not \partial_{A} \psi, \frac{\partial \psi(t)}{\partial t}\right) d t d v o l_{Y} \\
= & \int_{\left[R_{1}, R_{2}\right] \times Y}\left(\left|\frac{\partial \psi(t)}{\partial t}\right|^{2}+\left|\not \partial_{A} \psi\right|^{2}+\frac{\partial}{\partial t}\left(<\psi, \not \partial_{A} \psi>\right)-\frac{1}{2}<\frac{\partial A(t)}{\partial t} \cdot \psi, \psi>\right) d t d v o l_{Y} .
\end{aligned}$$
Now apply the 3-dimensional Weitzenböck formula,
$$\not \partial_{A}^{2} \psi=\nabla_{A}^{*} \nabla_{A} \psi+\frac{s}{4} \psi-\frac{1}{2}\left(* F_{A}\right) \cdot \psi,$$
and note that $F_{\mathbb{A}}^{+} \cdot \Psi=\left(\frac{\partial A(t)}{\partial t}+*_{3} F_{A}\right) \cdot \psi$, where $*_{3}$ is the Hodge star operator on $Y$. Using the various expressions above, we obtain that
$$\begin{aligned}
& \int_{\left[R_{1}, R_{2}\right] \times Y}\left|\not D_{\mathbb{A}}(\Psi)\right|^{2} d t d v o l_{Y} \\
= & \int_{\left[R_{1}, R_{2}\right] \times Y}\left(\left|\nabla_{\mathbb{A}} \Psi\right|^{2}+\frac{s}{4}|\Psi|^{2}-\frac{1}{2}<F_{\mathbb{A}}^{+} \cdot \Psi, \Psi>\right) d t d v o l_{Y} \\
& +\int_{\left\{R_{2}\right\} \times Y}<\psi, \partial_{A} \psi>d v o l_{Y}-\int_{\left\{R_{1}\right\} \times Y}<\psi, \partial_{A} \psi>d v o l_{Y} .
\end{aligned}$$
We also have
$$\begin{aligned}
& \int_{\left[R_{1}, R_{2}\right] \times Y} 2\left|F_{\mathbb{A}}^{+}-q(\Psi, \Psi)-\eta^{+}\right|^{2} d t d v_{o} l_{Y} \\
= & \int_{\left[R_{1}, R_{2}\right] \times Y}\left(\left(\left|F_{\mathbb{A}}\right|^{2}+|\sigma(\psi, \psi)+\eta|^{2}+<F_{\mathbb{A}}^{+} . \Psi, \Psi>\right) d t d v o l_{Y}\right. \\
& -\left(F_{\mathbb{A}}-*_{3} \eta\right) \wedge\left(F_{\mathbb{A}}-*_{3} \eta\right)+2 d t \wedge F_{\mathbb{A}} \wedge \eta .
\end{aligned}$$
Using the perturbed Seiberg-Witten equations (35) and the identity (33), we have
$$\begin{aligned}
& \int_{\left[R_{1}, R_{2}\right] \times Y} 2\left(\left|\left(\mathfrak{p}_{\mathbb{A}}^{+}, \mathfrak{p}_{\Psi}\right)\right|^{2}\right) d t d v o l_{Y} \\
= & \int_{\left[R_{1}, R_{2}\right] \times Y}\left(2\left|\not D_{\mathbb{A}}(\Psi)\right|^{2}+2\left|F_{\mathbb{A}}^{+}-q(\Psi, \Psi)-\eta^{+}\right|^{2}\right) d t d v o l_{Y} \\
= & \int_{\left[t_{1}, t_{2}\right] \times Y}\left(\left|F_{\mathbb{A}}\right|^{2}+2\left|q(\Psi, \Psi)+\eta^{+}\right|^{2}+2\left|\nabla_{\mathbb{A}} \Psi\right|^{2}+\frac{s}{2}|\Psi|^{2}\right) d t d v o l_{Y} \\
& +\int_{\left[t_{1}, t_{2}\right] \times Y}\left(2\left(F_{\mathbb{A}} \wedge d t \wedge \eta\right)-\left(F_{\mathbb{A}}-*_{3} \eta\right) \wedge\left(F_{\mathbb{A}}-*_{3} \eta\right)\right) \\
& +2\left(\int_{\left\{R_{2}\right\} \times Y}<\psi, \not \partial_{A} \psi>d v o l_{Y}-\int_{\left\{R_{1}\right\} \times Y}<\psi, \not 力_{A} \psi>d v o l_{Y}\right) \\
= & E_{\left[R_{1}, R_{2}\right] \times Y}(\mathbb{A}, \Psi)+2\left(\mathcal{C}_{\eta}\left(A\left(R_{2}\right), \psi\left(R_{2}\right)\right)-\mathcal{C}_{\eta}\left(A\left(R_{1}\right), \psi\left(R_{1}\right)\right)\right) .
\end{aligned}$$
Thus, we have the following inequalities $\left(\epsilon=\epsilon_{0} / 5\right)$
$$2<\frac{E_{\left[R_{1}, R_{2}\right] \times Y}(\mathbb{A}, \Psi)}{\mathcal{C}_{\eta}\left(A\left(R_{1}\right), \psi\left(R_{1}\right)\right)-\mathcal{C}_{\eta}\left(A\left(R_{2}\right), \psi\left(R_{2}\right)\right)}<2+\epsilon,$$
which implies that $\mathcal{C}_{\eta}\left(A\left(R_{1}\right), \psi\left(R_{1}\right)\right)-\mathcal{C}_{\eta}\left(A\left(R_{2}\right), \psi\left(R_{2}\right)\right)$ is finite if and only if $E_{\left[R_{1}, R_{2}\right] \times Y}(\mathbb{A}, \Psi)$ is finite. The completes the proof of the Lemma. \(\square\)

The following lemma states the basic properties of the perturbed CSD functional $\mathcal{C}_{\eta, \mathfrak{p}}$. The proof follows the same arguments as are used for the corresponding properties of the CSD functional $\mathcal{C}_{\eta}$ and of the perturbation terms satisfying Condition 3.12 for $\mathfrak{p} \in \mathcal{P}_{c}$.

Lemma 3.14. For any $\mathfrak{p} \in \mathcal{P}_{c}$, the perturbed Chern-Simons-Dirac functional $\mathcal{C}_{\eta, \mathfrak{p}}$ on $\mathcal{B}$ has the following properties:
\begin{itemize}
\item[1.] The critical point set of $\mathcal{C}_{\eta, \mathfrak{p}}$ agrees with the critical point set of $\mathcal{C}_{\eta}$, and all points are non-degenerate.
\item[2.] The Hessian operator of $\mathcal{C}_{\eta, \mathfrak{p}}$ on $\mathcal{B}$ is a compact perturbation of the Hessian operator of $\mathcal{C}_{\eta}$, hence has the same properties as the Hessian operator of $\mathcal{C}_{\eta}$ in Lemma 3.1.
\item[3.] Let $(A(t), \psi(t))$ be a solution to the perturbed Seiberg-Witten equations (30) on $\mathbb{R} \times Y$ in temporal gauge with finite energy, then there exists a sufficiently large $T$ such that on $(-\infty,-T] \times Y$ and $[T, \infty) \times Y$ the perturbation term from $\mathfrak{p}$ is zero, in other words, $\mathfrak{p}(\tau, \zeta, \xi)(A(t), \psi(t))$ has compact support in $[-T, T]$. Hence, $(A(t), \psi(t))$ is a solution to the gradient flow equation (18) of $\mathcal{C}_{\eta}$ outside the compact set $[-T, T] \times Y$.
\item[4.] There is a constant $\delta>0$, such that a choice of sufficiently small $\epsilon$ determines $E_{0}>0$ with the following property: suppose that $(A(t), \psi(t))$ is a solution to the perturbed Seiberg-Witten equations (30) on $\left[R_{1}-2, R_{2}+2\right] \times Y$ in temporal gauge with energy
$$E_{\left[R_{1}-2, R_{2}+2\right] \times Y}(A(t), \psi(t))<E_{0},$$
then there exists a critical point $\alpha \in \mathcal{M}_{Y}(\mathfrak{s}, \eta)$ such that the $L_{1}^{2}$-distance from $[A(t), \psi(t)]$ (for any $t \in\left[R_{1}, R_{2}\right]$ ) to $\alpha$ is at most $4 \epsilon\left(e^{-\delta\left(t-R_{1}\right)}+e^{-\delta\left(R_{2}-t\right)}\right)$. Moreover, there exists a sequence of constants $\left\{\lambda_{k}\right\}_{k=0,1,2, \ldots}$ such that there is a 3-dimensional monopole $\left(A_{\alpha}, \psi_{\alpha}\right)$ representing $\alpha$ for which
$$\left|\nabla^{k}\left(A(t)-A_{\alpha}\right)\right|+\left|\left(\nabla_{A_{\alpha}}\right)^{k}\left(\psi(t)-\psi_{\alpha}\right)\right| \leq \lambda_{k}\left(e^{-\delta\left(t-R_{1}\right)}+e^{-\delta\left(R_{2}-t\right)}\right),$$
for any point $(t, y) \in\left[R_{1}, R_{2}\right] \times Y$.
\item[5.] Let $(A(t), \psi(t))$ be a solution to the perturbed Seiberg-Witten equations (30) on $\mathbb{R} \times Y$ in temporal gauge with finite energy, then there exist two 3-dimensional monopoles $\left(A_{\alpha}, \psi_{\alpha}\right)$ and $\left(A_{\beta}, \psi_{\beta}\right)$ representing two critical points $\alpha$ and $\beta$ in $\mathcal{M}_{Y}(\mathfrak{s}, \eta)$, such that $A-A_{\alpha}$ and $\psi-\psi_{\alpha}$ decay exponentially along with their first derivatives as $t \rightarrow-\infty$, and $A-A_{\beta}$ and $\psi-\psi_{\beta}$ decay exponentially along with their first derivatives as $t \rightarrow \infty$.
\end{itemize}

Corollary 3.15. If $(A(t), \psi(t))$ is a solution to the perturbed Seiberg-Witten equations (30) on $[0, \infty) \times Y$ in temporal gauge with finite energy, then there exists a sequence of constants $\left\{\lambda_{k}\right\}_{k=0,1,2, \ldots}$ such that there is a 3-dimensional monopole $\left(A_{\alpha}, \psi_{\alpha}\right)$ representing a critical point $\alpha$ in $\mathcal{M}_{Y}(\mathfrak{s}, \eta)$ for which
$$\left|\nabla^{k}\left(A(t)-A_{\alpha}\right)\right|+\left|\left(\nabla_{A_{\alpha}}\right)^{k}\left(\psi(t)-\psi_{\alpha}\right)\right| \leq \lambda_{k} e^{-\delta t},$$
for any point $(t, y) \in[0, \infty) \times Y$, and
$$\left|\int_{[0, \infty) \times Y} F_{\mathbb{A}} \wedge F_{\mathbb{A}}\right|<\infty .$$

We now study the geometric structure of the moduli space $\mathcal{M}_{\mathfrak{p}}(\alpha, \beta)$ for the gradient flow lines of $\mathcal{C}_{\eta, \mathfrak{p}}$ on $\mathcal{B}$ connecting two different critical points $\alpha, \beta$ of $\mathcal{M}_{Y}(\mathfrak{s}, \eta)$. The space $\mathcal{M}_{\mathfrak{p}}(\alpha, \beta)$ is also the moduli space of solutions to the perturbed Seiberg-Witten equations on $\left(Y \times \mathbb{R}, g+d t^{2}, \pi^{*}(\mathfrak{s})\right)$, whose asymptotic limits at $\pm \infty$ represent $\alpha$ and $\beta$ respectively. Let $\delta$ be the decay rate of the gradient flow line in $\mathcal{M}_{\mathfrak{p}}(\alpha, \beta)$ (see Proposition 3.9 and Lemma 3.14).

We will consider the space of pairs consisting of $U(1)$ connections on the determinant bundle and sections of the spinor bundle on
$$\left(Y \times \mathbb{R}, g+d t^{2}, \pi^{*}(\mathfrak{s})\right),$$
topologized with weighted Sobolev norms of weight $\delta$ as in [18]. Here the weight function is $e_{\delta}(t)=e^{\tilde{\delta} t}$, where $\tilde{\delta}$ is a smooth function with bounded derivatives, $\tilde{\delta}: \mathbb{R} \rightarrow[-\delta, \delta]$ such that $\tilde{\delta}(t) \equiv-\delta$ for $t \leq-1$ and $\tilde{\delta}(t) \equiv \delta$ for $t \geq 1$. The $L_{k, \delta}^{2}$ norm is defined as
$$\|f\|_{L_{k, \delta}^{2}}=\left(\int_{Y \times \mathbb{R}} e_{\delta}(t)\left(|f|^{2}+|\nabla f|^{2}+\left|\nabla^{2} f\right|^{2}+\cdots+\left|\nabla^{k} f\right|^{2}\right) d t d v o l_{Y}\right)^{\frac{1}{2}}$$
The weight $e_{\delta}$ imposes an exponential decay as an asymptotic condition along the cylinder.
An element $\gamma_{0}$ of $\mathcal{M}(\alpha, \beta)$ determines a path in $\mathcal{A} / \mathcal{G}$, also denoted $\gamma_{0}$. We lift $\gamma_{0}$ to a path in $\mathcal{A}$ which we denote by $\tilde{\gamma}_{0}=\left(A_{0}(t), \psi_{0}(t)\right)$. From Lemma 3.14, we know that $\left(A_{\alpha}, \psi_{\alpha}\right)$ and $\left(A_{\beta}, \psi_{\beta}\right)$ represent $\alpha$ and $\beta$ respectively, such that $\left(A_{0}(t), \psi_{0}(t)\right)$ approaches to $\left(A_{\alpha}, \psi_{\alpha}\right)$ and $\left(A_{\beta}, \psi_{\beta}\right)$ exponentially fast in the $L_{1}^{2}$-topology as $t \rightarrow \pm \infty$ respectively.

The operators $T(t)$ have a spectral flow denoted by $\mathfrak{i}\left(\gamma_{0}\right)$ along the path $\tilde{\gamma}_{0}$ (see (16) for the relation with the spectral flow of the Hessian operator $Q$ ). We see that
$$\mathfrak{i}\left(\gamma_{0}\right)=S F_{\gamma_{0}}(Q)=\mathfrak{i}(\alpha, \beta)(\bmod d(\mathfrak{s}))$$
where $\mathfrak{i}(\alpha, \beta)$ is the relative index between $\alpha$ and $\beta$, defined in (3.6). Note that $\mathfrak{i}\left(\gamma_{0}\right)$ is $\mathbb{Z}$-valued.
Choose a $U(1)$-connection $\mathbb{A}_{0}$ on $\operatorname{det}\left(W^{+}\right)$and a spinor section $\Psi_{0}$ of $W^{+}$such that $\left(A_{0}, \Psi_{0}\right)$ is in temporal gauge outside a compact set and satisfies $\left(\mathbb{A}_{0}, \Psi_{0}\right)=\left(A_{\alpha}, \psi_{\alpha}\right)$ for $t \ll 0$ and $\left(\mathbb{A}_{0}, \Psi_{0}\right)=\left(A_{\beta}, \psi_{\beta}\right)$ for $t \gg 0$.

For $k \geq 2$, let $\mathcal{A}_{k, \delta}(\alpha, \beta)$ be the space of pairs of connections and spinor sections $(A, \psi)$ on $Y \times \mathbb{R}$ satisfying
$$(A, \psi) \in\left(\mathbb{A}_{0}, \Psi_{0}\right)+\left(\Omega_{L_{k, \delta}^{2}}^{1}(Y \times \mathbb{R}, i \mathbb{R}) \oplus L_{k, \delta}^{2}\left(W^{+}\right)\right) .$$
The gauge transformation group $\mathcal{G}_{k+1, \delta}(\alpha, \beta)$ is locally modelled on
$$L_{k+1, \delta}^{2}\left(\Omega^{0}(Y \times \mathbb{R}, i \mathbb{R})\right)$$
and approaches elements in the stabilizers $G_{\alpha}$ and $G_{\beta}$ of $\alpha$ and $\beta$ as $t \rightarrow \pm \infty$. This gauge group acts on $\mathcal{A}_{k, \delta}(\alpha, \beta)$ freely, so we can form the quotient $\mathcal{B}_{k, \delta}(\alpha, \beta)$, a smooth Banach manifold, whose tangent space at $[A, \psi]$ (represented by $(A, \psi) \in \mathcal{A}_{k, \delta}(\alpha, \beta)$ ) is given by
$$\left\{(a, \phi) \in \Omega_{L_{k, \delta}^{2}}^{1} \oplus L_{k, \delta}^{2}\left(W^{+}\right) \mid G_{[A, \psi], \delta}^{*}(a, \phi)=\left(e_{-\delta} d^{*} e_{\delta}\right) a+i \operatorname{Im}\langle\psi, \phi\rangle=0\right\} .$$

Using Proposition 3.9, we know that the component of $\mathcal{M}_{\mathfrak{p}}(\alpha, \beta)$ containing the given gradient flow line $\gamma_{0}$, denoted by $\mathcal{M}_{\mathfrak{p}}(\alpha, \beta)_{\gamma_{0}}$, can be identified with
$$\left\{(A, \psi) \in \mathcal{A}_{k, \delta}(\alpha, \beta) \left\lvert\, \begin{array}{l}
(A, \psi) \text { satisfies the } \\
\text { monopole equations (30). }
\end{array}\right.\right\} / \mathcal{G}_{k+1, \delta}(\alpha, \beta) .$$

Proposition 3.16. There is a Baire set $\mathcal{P}_{0}$ of smooth functions $\mathfrak{p} \in \mathcal{P}_{c}$, satisfying Condition 3.12, such that for $\mathfrak{p} \in \mathcal{P}_{0} \mathcal{M}_{\mathfrak{p}}(\alpha, \beta)_{\gamma_{0}}$, the component of $\mathcal{M}(\alpha, \beta)$ containing $\gamma_{0}$, if non-empty, is a smooth oriented manifold of dimension $\mathfrak{i}\left(\gamma_{0}\right)-d_{\alpha}$ where $d_{\alpha}=1$ if $\alpha$ is reducible and $d_{\alpha}=0$ otherwise.

Proof. Suppose $(A(t), \psi(t), \mathfrak{p})$, representing a point in $\mathcal{M}_{\mathfrak{p}}(\alpha, \beta)_{\gamma_{0}}$, is a solution to the perturbed gradient flow equation (27) or the perturbed Seiberg-Witten equations (30) in temporal gauge with the perturbation $\mathfrak{p} \in \mathcal{P}_{c}$. Using the linearization of (30) and gauge transformations at $(A(t), \psi(t), \mathfrak{p})$ we may define the following operator
$$\begin{gathered}
\mathcal{D}_{A, \psi, \mathfrak{p}}: \quad \mathcal{P}_{c} \oplus L_{k, \delta}^{2}\left(i \Omega^{1} \oplus W^{+}\right) \rightarrow L_{k-1, \delta}^{2}\left(i \Omega^{0} \oplus i \Omega^{2,+} \oplus W^{-}\right), \\
\mathcal{D}_{A, \psi, \mathfrak{p}}(\tilde{p}, a, \phi)=\left(G_{(A, \psi), \delta}^{*}, d^{+} a-(d t \wedge \sigma(\phi, \psi))^{+}+\mathfrak{p}^{+}, \not D_{A} \phi+\frac{1}{2} a . \psi+\mathfrak{p}_{\psi}\right),
\end{gathered}$$
where $\left(\mathfrak{p}^{+}, \mathfrak{p}_{\psi}\right)$ is given by the linearization of the perturbation term at $(A(t), \psi(t), \mathfrak{p})$.
Let $\pi: Y \times \mathbb{R} \rightarrow Y$ be the projection map, then as bundles over $Y \times \mathbb{R}$,
$$\begin{gathered}
\Lambda^{1}(Y \times \mathbb{R}, i \mathbb{R}) \cong \pi^{*} \Lambda^{1}(Y, i \mathbb{R}) \oplus \pi^{*}\left(\Lambda^{0}(Y, i \mathbb{R})\right. \\
\Lambda^{2,+}(Y \times \mathbb{R}, i \mathbb{R}) \cong \pi^{*} \Lambda^{1}(Y, i \mathbb{R})
\end{gathered}$$

Also, using Clifford multiplication by $d t$, we identify $W^{+} \cong W^{-} \cong \pi^{*} W$. Under these identifications, fix $\mathfrak{p}$, then the operator $\mathcal{D}_{A, \psi, \mathfrak{p}}$, restricted to $L_{k, \delta}^{2}\left(i \Omega^{1} \oplus W^{+}\right)$, has the form
$$\frac{\partial}{\partial t}+\left(\begin{array}{cc}
L_{(A, \psi)} & G_{(A, \psi)} \\
G_{(A, \psi)}^{*} & 0
\end{array}\right)+\delta+o(1)$$
where $L_{(A, \psi)}, G_{(A, \psi)}$ and $G_{(A, \psi)}^{*}$ are given by (13). By the result of Lockhart-McOwen [18], as $\mathfrak{p}$ varies through $\mathcal{P}_{c}, \mathcal{D}_{A, \psi, \mathfrak{p}}$, restricted to $L_{k, \delta}^{2}\left(i \Omega^{1} \oplus W^{+}\right)$, forms a continuous family of Fredholm operators with index equal to $\mathfrak{i}\left(\gamma_{0}\right)-d_{\alpha}$.

Now we prove that $\mathcal{D}_{A(t), \psi(t), \mathfrak{p}}$ is surjective. Note that any solution $(A(t), \psi(t))$ which represents a point in $\mathcal{M}_{\mathfrak{p}}(\alpha, \beta)_{\gamma_{0}}$, is a solution to the perturbed gradient flow equation (27) with finite energy $\mathcal{C}_{\eta}\left(A_{\alpha}, \psi_{\alpha}\right)-\mathcal{C}_{\eta}\left(A_{\beta}, \psi_{\beta}\right)$. We can use Condition 3.12, to assert that there is a compact subset $[-T, T] \times Y$ in $\mathbb{R} \times Y$, such that outside this compact set, the perturbation function $\mathfrak{p} \in \mathcal{P}_{c}$ is zero.

Suppose that $(f, b, \phi) \in L_{-\delta}^{2}\left(i \Omega^{0} \oplus i \Omega^{2,+} \oplus W^{-}\right)$is $L^{2}$-orthogonal to the image of $\mathcal{D}_{A(t), \psi(t), \mathfrak{p}}$, then using Lemma 3.11 and a direct calculation shows that $(f, b, \phi)$ is zero on $[-T, T] \times Y$. As an element in the cokernel of $\mathcal{D}_{A(t), \psi(t), \mathfrak{p}},(f, b, \phi)$ satisfies the weak unique continuation principle [3] and hence $(f, b, \phi)$ is zero everywhere. This proves that $\mathcal{D}_{A(t), \psi(t), \mathfrak{p}}$ is surjective.

The Sard-Smale theorem implies that there exists a Baire set $\mathcal{P}_{0}$ of functions $\mathfrak{p} \in \mathcal{P}_{c}$, so that the moduli space $\mathcal{M}_{\mathfrak{p}}(\alpha, \beta)_{\gamma_{0}}$, for $\mathfrak{p} \in \mathcal{P}_{0}$, is a smooth manifold of dimension $\mathfrak{i}\left(\gamma_{0}\right)-d_{\alpha}$ if $\mathfrak{i}\left(\gamma_{0}\right)-d_{\alpha}>0$, and is empty otherwise.

The orientation of $\mathcal{M}_{\mathfrak{p}}(\alpha, \beta)_{\gamma_{0}}$ is determined by the determinant line bundle of $\mathcal{D}_{A, \psi, \mathfrak{p}}$ over $\mathcal{A}_{k, \delta}(\alpha, \beta)$ for a fixed perturbation $\mathfrak{p}$. This is established in Proposition 2.15 of [20] where it is shown that $\mathcal{M}_{\mathfrak{p}}(\alpha, \beta)_{\gamma_{0}}$ is orientable, the orientation is determined by choosing an orientation of
$$\wedge^{t o p} H_{\delta}^{1}(Y \times \mathbb{R}, i \mathbb{R}) \otimes \wedge^{t o p} H_{\delta}^{2,+}(Y \times \mathbb{R}, i \mathbb{R}) .$$ \(\square\)

Proposition 3.16 has an immediate corollary.
Corollary 3.17. Let $(Y, g, \mathfrak{s})$ be a closed, oriented 3-manifold with a Riemannian metric $g$ and a $\operatorname{Spin}^{c}$ structure $\mathfrak{s}$. Let $\mathcal{M}(\alpha, \beta)$ be the moduli space of gradient flows of $\mathcal{C}_{\eta, \mathfrak{p}}$ which connect two different critical points $\alpha$ and $\beta$. Then, for a generic perturbation $\mathfrak{p}$, we have the following results.
\begin{itemize}
\item[1.] When $Y$ is a homology 3-sphere, $\mathcal{M}(\alpha, \beta)$ is empty if $\mathfrak{i}(\alpha)-\mathfrak{i}(\beta)-d_{\alpha} \leq 0$, otherwise, $\mathcal{M}(\alpha, \beta)$ is an oriented, smooth manifold of dimension $\mathfrak{i}(\alpha)-\mathfrak{i}(\beta)-d_{\alpha}$.
\end{itemize}
\begin{itemize}
\item[2.] If $c_{1}(\mathfrak{s})$ is non-zero in $H^{2}(Y, \mathbb{R}), \mathcal{M}(\alpha, \beta)$ has infinitely many components. Each of them is an oriented, smooth manifold with dimension given by $\mathfrak{i}(\gamma)-d_{\alpha}>0$, where $\gamma$ is a chosen element in that component. The dimensions of two non-empty components differ by a multiple of $d(\mathfrak{s})$, where $d(\mathfrak{s})$ is the divisibility of $c_{1}(\mathfrak{s})$ in $H^{2}(Y, \mathbb{Z}) /$ Torsion .
\end{itemize}

Now we discuss the compactness of the trajectory moduli space. For the case of a 3-manifold $Y$ with $b_{1}(Y)>0$ and $c_{1}(\mathfrak{s}) \neq 0$ in $H^{2}(Y, \mathbb{R})$, we know that $\hat{\mathcal{M}}(\alpha, \beta)$, the quotient of $\mathcal{M}(\alpha, \beta)$ by $\mathbb{R}$, has infinitely many components. Assume $\mathfrak{i}(\alpha)-\mathfrak{i}(\beta)=k+1(\bmod d(\mathfrak{s}))$ with $k \geq 0$, then
$$\hat{\mathcal{M}}(\alpha, \beta)=\cup_{n \in \mathbb{N}} \hat{\mathcal{M}}^{k+n d(\mathfrak{s})}(\alpha, \beta)$$
where $\hat{\mathcal{M}}^{k+n d(\mathfrak{s})}(\alpha, \beta)$ is the union of components of dimension $k+n d(\mathfrak{s})$ in $\hat{\mathcal{M}}(\alpha, \beta)$. We now summarize the compactness results and refer to page 501-549 in [20] for the proofs.

Proposition 3.18. (Theorem 4.23 [20]) For any 3-manifold $(Y, g, \mathfrak{s})$ with a Riemannian metric $g$ and a $\operatorname{Spin}^{c}$ structure $\mathfrak{s}$, assume $c_{1}(\mathfrak{s}) \neq 0$ if $b_{1}(Y)>0$, then $\hat{\mathcal{M}}^{k+n d(\mathfrak{s})}(\alpha, \beta)(\hat{\mathcal{M}}(\alpha, \beta)$ for $b_{1}(Y)=0$ ) can be compactified by adding lower dimensional boundary strata of broken trajectory moduli spaces. Namely, for $b_{1}(Y)=0$, the boundary strata are of the form
$$\bigcup_{\alpha_{1}, \cdots \alpha_{j}} \hat{\mathcal{M}}\left(\alpha, \alpha_{1}\right) \times \hat{\mathcal{M}}\left(\alpha_{1}, \alpha_{2}\right) \times \cdots \times \hat{\mathcal{M}}\left(\alpha_{j}, \beta\right) .$$
Here the union is over all possible sequences of critical points $\alpha, \alpha_{1}, \cdots \alpha_{j}, \beta$ with decreasing indices. For $b_{1}(Y)>0$ and $c_{1}(Y) \neq 0, \hat{\mathcal{M}}^{k+n d(\mathfrak{s})}(\alpha, \beta)$ can be compactified by adding boundary strata of the form
$$\bigcup_{\alpha_{1}, \cdots \alpha_{j}} \hat{\mathcal{M}}^{k_{0}}\left(\alpha, \alpha_{1}\right) \times \hat{\mathcal{M}}^{k_{1}}\left(\alpha_{1}, \alpha_{2}\right) \times \cdots \times \hat{\mathcal{M}}^{k_{j}}\left(\alpha_{j}, \beta\right) .$$
Here the union is over all possible sequences of critical points $\alpha, \alpha_{1}, \cdots \alpha_{j}, \beta$ with $k_{0}+k_{1}+\cdots+k_{j} \leq k+n d(\mathfrak{s})-j$ and $k_{i}=\mathfrak{i}\left(\alpha_{i}, \alpha_{i+1}\right)(\bmod d(\mathfrak{s}))$.

With these compactness results for the moduli space, we have the following corollary which will be crucial for the construction of Seiberg-Witten-Floer homology.

Corollary 3.19. 1. Let $(Y, \mathfrak{s})$ be a homology 3-sphere or $b_{1}(Y)>0$ with $c_{1}(\mathfrak{s}) \neq 0$, then the zero dimensional components $\hat{\mathcal{M}}^{0}(\alpha, \beta)$ for two critical points $\alpha$ and $\beta$ of relative index 1 are compact, and consist of finitely many oriented points.
\begin{itemize}
\item[2.] Let $(Y, \mathfrak{s})$ be a homology 3-sphere or $b_{1}(Y)>0$ with $c_{1}(\mathfrak{s}) \neq 0$, let $\alpha, \gamma$ be two irreducible critical points in $\mathcal{M}_{Y}(\mathfrak{s}, \eta)$ with relative index $\mathfrak{i}(\alpha, \gamma)=2$, or $2 \bmod d(\mathfrak{s})$ for $b_{1}(Y)>0$. Then the boundary of $\hat{\mathcal{M}}^{1}(\alpha, \gamma)$ (an oriented, compact 1-manifold) consists of the union
$$\bigcup_{\beta \in \mathcal{M}_{\mathfrak{s}, \mathfrak{p}}^{*}} \hat{\mathcal{M}}^{0}(\alpha, \beta) \times \hat{\mathcal{M}}^{0}(\beta, \gamma)$$
\end{itemize}
where $\beta$ runs over those critical points $\beta$ with relative index $\mathfrak{i}(\alpha, \beta)=1$ or $1 \bmod d(\mathfrak{s})$ for $b_{1}(Y)>0$.

Remark 3.20. For a 3-manifold $(Y, \mathfrak{s})$ with $b_{1}(Y)>0$ and $c_{1}(\mathfrak{s})=0$, we need to perturb by a coclosed 2-form $\eta$ such that $[* \eta]$ representing a non-trivial cohomology class. Then $\mathcal{C}_{\eta}$ has finitely many critical points $\mathcal{M}_{Y}(\mathfrak{s}, \eta)$, which are all irreducible and have $\mathbb{Z}$-valued indices. Note that in this case $\mathcal{C}_{\eta}(g .(A, \psi))-\mathcal{C}_{\eta}(A, \psi)=\langle[g] \cup[\eta],[Y]\rangle$, which is a multiple of a positive number $e_{\eta}$ ( $e_{\eta}$ depends on $\eta$ ). For two critical points $\alpha$ and $\beta$ with relative index $k+1>0$, and for generic $\mathfrak{p}, \hat{\mathcal{M}}(\alpha, \beta)$ is an oriented and smooth manifold of dimension $k, \hat{\mathcal{M}}(\alpha, \beta)=\bigcup_{n \in \mathbb{N}} \hat{\mathcal{M}}_{(n)}(\alpha, \beta)$ where $\hat{\mathcal{M}}_{(0)}(\alpha, \beta)$ is the union of components in $\hat{\mathcal{M}}(\alpha, \beta)$ with minimal energy $e_{0}(\alpha, \beta)$, and for $n>0, \hat{\mathcal{M}}_{(n)}(\alpha, \beta)$ is the the union of components in $\hat{\mathcal{M}}(\alpha, \beta)$ with energy $e_{0}(\alpha, \beta)+n e_{\eta}$. Moreover $\hat{\mathcal{M}}_{(n)}(\alpha, \beta)$ can be compactified by adding boundary strata of the form
$$\bigcup_{\alpha_{1}, \cdots, \alpha_{l}} \hat{\mathcal{M}}_{\left(i_{0}\right)}\left(\alpha, \alpha_{1}\right) \times \hat{\mathcal{M}}_{\left(i_{1}\right)}\left(\alpha_{1}, \alpha_{2}\right) \times \cdots \times \hat{\mathcal{M}}_{\left(i_{l}\right)}\left(\alpha_{l}, \beta\right) .$$
Here the union is over all possible sequences of $\alpha_{0}=\alpha, \alpha_{1}, \cdots, \alpha_{l}, \alpha_{l+1}=\beta$ with decreasing indices and $\sum_{j=0}^{l} e_{0}\left(\alpha_{j}, \alpha_{j+1}\right)+\sum_{j=0}^{l} i_{j} e_{\eta} \leq e_{0}(\alpha, \beta)+n e_{\eta}$.

\subsection*{3.4 Seiberg-Witten-Floer homology: definition and properties}

In this section, we will only construct the Seiberg-Witten-Floer homology for $(Y, \mathfrak{s})$ when $(Y, \mathfrak{s})$ has $b_{1}(Y)>0$ and $c_{1}(\mathfrak{s}) \neq 0$. When $Y$ is a homology sphere, there is an equivariant Seiberg-Witten-Floer homology, developed in [20], which is a topological invariant.

Let $(Y, g, \mathfrak{s})$ be an oriented, closed 3-manifold with a Riemannian metric $g$ and a Spin ${ }^{c}$ structure $\mathfrak{s}$. For a generic $\eta$, the critical points of $\mathcal{C}_{\mathfrak{p}}$ consist of finitely many, non-degenerate points, which we denote by $\mathcal{M}_{Y}(\mathfrak{s}, \eta)$, all irreducible.

The Floer complex $C_{*}^{S W}(Y, \mathfrak{s})$ is generated freely by the critical points in $\mathcal{M}_{Y}(\mathfrak{s}, \eta)$ with a relative $d(\mathfrak{s})$-grading
$$C_{*}(Y, \mathfrak{s})=\oplus_{\alpha \in \mathcal{M}_{Y}(\mathfrak{s}, \eta)} \mathbb{Z} .<\alpha>.$$
The boundary operator $\partial$ on $C_{*}(Y, \mathfrak{s})$ is defined by
$$\partial(\langle\alpha\rangle)=\sum_{\beta \in \mathcal{M}_{Y}(\mathfrak{s}, \eta)} n_{\alpha \beta}\langle\beta\rangle,$$
where $n_{\alpha \beta}$ is given by counting the points in $\hat{\mathcal{M}}^{0}(\alpha, \beta)$ (an oriented, smooth, compact 0-manifold from Corollary 3.19) with sign.

Lemma 3.21. $\partial \circ \partial=0$.

Proof. By definition,
$$\begin{aligned}
\partial^{2}(<\alpha>) & =\sum_{\beta \in \mathcal{M}_{Y}(\mathfrak{s}, \eta)} n_{\alpha \beta} \partial(<\beta>) \\
& =\sum_{\beta \in \mathcal{M}_{Y}(\mathfrak{s}, \eta)} \sum_{\gamma \in \mathcal{M}_{Y}(\mathfrak{s}, \eta)} n_{\alpha \beta} n_{\beta \gamma}<\gamma>.
\end{aligned}$$
where $\beta$ runs over the critical points with relative index $\mathfrak{i}(\alpha, \beta)=1 \bmod (\partial(\mathfrak{s})), \gamma$ runs over the critical points with relative index $\mathfrak{i}(\alpha, \gamma)=2 \bmod (\partial(\mathfrak{s}))$. We want to show that
$$\sum_{\{\beta \mid \mathfrak{i}(\alpha, \beta)=1 \bmod (d(\mathfrak{s}))\}} n_{\alpha \beta} n_{\beta \gamma}=0$$
for any $\gamma \in \mathcal{M}_{Y}(\mathfrak{s}, \eta)$ with $\mathfrak{i}(\alpha, \gamma)=2 \bmod (d(\mathfrak{s}))$. We know that the number
$$\sum_{\{\beta \mid \mathfrak{i}(\alpha, \beta)=1 \bmod (d(\mathfrak{s}))\}} n_{\alpha \beta} n_{\beta \gamma}$$
is the number of oriented boundary points of the 1 -manifold $\hat{\mathcal{M}}^{1}(\alpha, \gamma)$ by Corollary 3.19, and hence is zero. \(\square\)

Now we can define the Seiberg-Witten-Floer homology.
Definition 3.22. For any closed oriented 3-manifold $Y$ with a Spin ${ }^{c}$ structure, the Seiberg-Witten-Floer homology is defined to be
$$H F_{*}^{S W}(Y, \mathfrak{s})=H_{*}\left(C_{*}^{S W}(Y, \mathfrak{s}), \partial_{*}\right),$$
which is a $\mathbb{Z}_{d(\mathfrak{s})}$-graded and finitely generated Abelian group.

Remark 3.23. The Seiberg-Witten-Floer homology can be thought as a refinement of the Seiberg-Witten invariant for a 3-manifold $Y$ with a $\operatorname{Spin}^{c}$ structure $\mathfrak{s}$, in the sense that the Seiberg-Witten invariant for $(Y, \mathfrak{s})$ is the Euler characteristic of the Seiberg-Witten-Floer homology $H F_{*}^{S W}(Y, \mathfrak{s})$.

The definition of $H F_{*}^{S W}(Y, \mathfrak{s})$ involves both the metric and perturbations. The following proposition shows that for a 3-manifold $Y$ with $b_{1}(Y)>0$ and $c_{1}(\mathfrak{s}) \neq 0$, the Seiberg-Witten-Floer homology is a topological invariant, independent of the metric and generic perturbations $\eta$ and $\mathfrak{p}$. We then show that there is an the action of $\mathbb{A}(Y)=\operatorname{Sym}^{*}\left(H_{0}(Y, \mathbb{Z})\right) \otimes \Lambda^{*}\left(H_{1}(Y, \mathbb{Z}) /\right.$ torsion $)$ on $H F_{*}^{S W}(Y, \mathfrak{s})$.

Proposition 3.24. For any closed oriented 3-manifold $Y$ with a $\operatorname{Spin}^{c}$ structure $\mathfrak{s}$ such that $c_{1}(\mathfrak{s})$ is non-torsion, then $H F_{*}^{S W}(Y, \mathfrak{s})$ is a topological invariant and there is an action of $\mathbb{Z}[U]$ on $H F_{*}^{S W}(Y, \mathfrak{s})$ where the $U$-action decreases the relative grading by 2 .

Proof. The proof of topological invariance can be found in [20]. The $\mathbb{Z}[U]$-module structure can also be extracted from the isomorphism between $H F_{*}^{S W}(Y, \mathfrak{s})$ and the corresponding equivariant Seiberg-Witten-Floer homology $H F_{*, U(1)}^{S W}(Y, \mathfrak{s})$. Here we sketch a more direct proof of the existence of a $\mathbb{Z}[U]$-module structure on $H F_{*}^{S W}(Y, \mathfrak{s})$. In subsection 5.3 of [20], there is an associated integer $m_{\alpha \gamma}$ for each pair of critical points $\alpha$ and $\gamma$ in $\mathcal{M}_{Y}(\mathfrak{s}, \eta)$ of relative index 2 $\bmod (d(\mathfrak{s}))$, defined as follows.

Let $\mathcal{M}^{2}(\alpha, \beta)$ be the 2-dimensional components of the moduli space of parametrized flowlines between $\alpha$ and $\gamma$. There is a $U(1)$-principal bundle over $\mathcal{M}^{2}(\alpha, \beta)$, denoted by $\tilde{\mathcal{M}}^{2}(\alpha, \beta)$, which is the based moduli space corresponding to $\mathcal{M}^{2}(\alpha, \beta)$. That is, fix a base point $\left(t_{0}, y_{0}\right) \in \mathbb{R} \times Y$ and a complex line $L_{y_{0}}$ in the fiber $W_{y_{0}}$ of the spinor bundle $W$ over $Y$ such that $L_{y_{0}}$ doesn't contain the spinor part of any critical point in $\mathcal{M}_{Y}(\mathfrak{s}, \eta)$. Such $L_{y_{0}}$ exists due to the fact that $\mathcal{M}_{Y}(\mathfrak{s}, \eta)$ consists of finitely many irreducible critical points. Note also that the space of such $L_{y_{0}}$ is path-connected. Then there is a complex line bundle $\mathcal{L}_{\alpha \gamma}$ over $\mathcal{M}^{2}(\alpha, \beta)$
$$\mathcal{L}_{\alpha \gamma}=\tilde{\mathcal{M}}^{2}(\alpha, \beta) \times_{U(1)}\left(W_{y_{0}} / L_{y_{0}}\right)$$
with a canonical section
$$s_{\alpha \gamma}([\mathbb{A}, \Psi])=\left([\mathbb{A}, \Psi], \Psi\left(t_{0}, y_{0}\right)\right) .$$
This canonical section determines a trivialization of $\mathcal{L}_{\alpha \gamma}$ away from a compact set (see Lemma 5.7 in [20]) by the choice of $L_{y_{0}}$. Then the relative Euler number of $\left(\mathcal{L}_{\alpha \gamma}, s_{\alpha \gamma}\right)$ defines an integer $m_{\alpha \gamma}$ for each pair of $\alpha$ and $\gamma$ with relative index $2 \bmod (d(\mathfrak{s}))$. The system of integers $\left\{m_{\alpha \gamma}: \mathfrak{i}(\alpha, \gamma)=2 \bmod (d(\mathfrak{s}))\right\}$ satisfies the following properties (Cf. Lemma 5.7 and Remark 5.8 in [20]): $m_{\alpha \gamma}$ is independent of the choices of base points and $L_{y_{0}}$, and for $\alpha$ and $\delta$ two critical points with relative index $3 \bmod (d(\mathfrak{s}))$, then
$$\sum_{\{\beta \mid \mathfrak{i}(\alpha, \beta)=1 \bmod (d(\mathfrak{s}))\}} n_{\alpha \beta} m_{\beta \delta}-\sum_{\{\gamma \mid \mathfrak{i}(\alpha \gamma)=2 \bmod (d(\mathfrak{s}))\}} m_{\alpha \gamma} n_{\gamma \delta}=0 .$$
Now we can define a map
$$\begin{array}{lllc}
U: & C_{*}^{S W}(Y, \mathfrak{s}) & \longrightarrow & C_{*-2}^{S W}(Y, \mathfrak{s}) \\
& <\alpha> & \mapsto & \sum_{\{\gamma \mid \mathfrak{i}(\alpha, \gamma)=1 \bmod (d(\mathfrak{s}))\}} m_{\alpha \gamma}<\gamma>.
\end{array}$$
Identity (39) implies that $U$ induces a map on the Seiberg-Witten-Floer homology which decreases the relative grading by 2 . This is the $\mathbb{Z}[U]$ module structure on $H F_{*}^{S W}(Y, \mathfrak{s})$. \(\square\)

Now we define the action of $\mathbb{A}(Y)=\operatorname{Sym}^{*}\left(H_{0}(Y, \mathbb{Z})\right) \otimes \Lambda^{*}\left(H_{1}(Y, \mathbb{Z}) /\right.$ Torsion $)$ on $H F_{*}^{S W}(Y, \mathfrak{s})$. Note that $\operatorname{Sym}^{*}\left(H_{0}(Y, \mathbb{Z})\right) \cong \mathbb{Z}[U]$, so we only need to define an action of $\Lambda^{*}\left(H_{1}(Y, \mathbb{Z}) /\right.$ Torsion $)$ on $H F_{*}^{S W}(Y, \mathfrak{s})$.

Let $\pi$ be an embedded loop in $Y$ which represents a non-torsion element in $H_{1}(Y, \mathbb{Z})$. For any $\alpha$ and $\beta$ two critical points in $\mathcal{M}_{Y}(\mathfrak{s}, \eta)$ with relative index $1 \bmod (d(\mathfrak{s}))$, let $\mathcal{M}^{1}(\alpha, \beta)$ denote the 1-dimensional components of the moduli space of parametrized flowlines between $\alpha$ and $\beta$. Then there is a universal line bundle over $\pi \times \mathcal{M}^{1}(\alpha, \beta)$ constructed as follows: for any point $y \in \pi$, the based moduli space with base point $\left(t_{0}, y\right)$ defines a $U(1)$-bundle over $\mathcal{M}^{1}(\alpha, \beta)$. Varying $y$ in $\pi$ gives rise to a universal line $\widetilde{\mathcal{M}_{\pi}^{1}(\alpha, \beta)}$ over $\pi \times \mathcal{M}^{1}(\alpha, \beta)$.

As in the proof of Proposition 3.24, choose a fixed base point $y_{0}$ and a complex line $L_{y_{0}} \subset W_{y_{0}}$, then there is an associated complex line bundle
$$\mathcal{L}_{\alpha \beta}^{\pi}=\widetilde{\mathcal{M}_{\pi}^{1}(\alpha, \beta)} \times_{U(1)}\left(W_{y_{0}} / L_{\left.y_{0}\right)}\right)$$
over $\pi \times \mathcal{M}^{1}(\alpha, \beta)$, endowed with a canonical section $s_{\alpha \beta}^{\pi}$ defined in a fashion similar to that in the proof of Proposition 3.24. This canonical section $s_{\alpha \beta}^{\pi}$ also defines a trivialization away from a compact set in $\pi \times \mathcal{M}^{1}(\alpha, \beta)$. The corresponding relative Euler number is denoted by $\pi_{\alpha \beta}$ : it counts the zeros of a generic section which agrees with the trivialization determined by $s_{\alpha \beta}^{\pi}$. The standard cobordism argument implies that $\pi_{\alpha \beta}$ is independent of the choice of embedded loop $\pi$, hence we can denote this relative Euler number as $[\pi]_{\alpha \beta}$ for any non-torsion element $[\pi] \in H_{1}(Y, \mathbb{Z})$. This defines a map of degree -1 on the Seiberg-Witten-Floer chain complex:
$$\begin{array}{llc}
{[\pi]} & C_{*}^{S W}(Y, \mathfrak{s}) & \longrightarrow \\
<\alpha> & \mapsto & \sum_{\{\beta \mid i(\alpha, \beta)=1 \bmod (d(\mathfrak{s}))\}}[\pi]_{\alpha \beta}<\beta>.
\end{array}$$

Proposition 3.25. $[\pi]$ is a chain map and satisfies $[\pi] \circ[\pi]=0$, hence it defines an action of $\Lambda^{*}\left(H_{1}(Y, \mathbb{Z}) /\right.$ Torsion $)$ on the Seiberg-Witten-Floer homology $H F_{*}^{S W}(Y, \mathfrak{s})$.

Proof. First, we show that $[\pi]$ is a chain map. Let $\alpha$ and $\gamma$ be two critical points of relative index $2 \bmod (d(\mathfrak{s}))$. Let $\mathcal{M}^{2}(\alpha, \gamma)^{*}$ be the induced partial compactification of the 2-dimensional components of $\mathcal{M}(\alpha, \gamma)$ obtained by adding the broken flowlines. Note that, $\mathcal{M}^{2}(\alpha, \gamma)^{*}$ consists of finitely many cylinders (homeomorphic to $S^{1} \times \mathbb{R}$ ), and finitely many bands (homeomorphic to $[0,1] \times \mathbb{R}$ ). The boundary ends in the bands correspond to the unparametrised broken flowlines
$$\bigcup_{\{\beta \mid \mathfrak{i}(\alpha, \beta)=1 \bmod (d(\mathfrak{s}))\}} \hat{\mathcal{M}}^{0}(\alpha, \beta) \times \hat{\mathcal{M}}^{0}(\beta, \gamma),$$
where $\hat{\mathcal{M}}^{0}(\alpha, \beta)$ and $\hat{\mathcal{M}}^{0}(\beta, \gamma)$ are the quotients of $\mathcal{M}^{1}(\alpha, \beta)$ and $\hat{\mathcal{M}}^{1}(\beta, \gamma)$ by the $\mathbb{R}$-action respectively. There is a complex line bundle $\mathcal{L}_{\alpha \gamma}^{\pi}$ over $\pi \times \mathcal{M}^{2}(\alpha, \gamma)^{*}$ with a canonical section $s_{\alpha \gamma}^{\pi}$, constructed in a fashion similar to that of $\left(\mathcal{L}_{\alpha \beta}^{\pi}, s_{\alpha \beta}^{\pi}\right)$ in the proof of Proposition 3.24. Away from a compact set in $\pi \times \mathcal{M}^{2}(\alpha, \gamma)^{*}, s_{\alpha \gamma}^{\pi}$ is nowhere vanishing, hence it determines a
trivialization of $\mathcal{L}_{\alpha \gamma}^{\pi}$ away from a compact set. The zeros of a section which agrees with $s_{\alpha \gamma}^{\pi}$ away from a compact set form an oriented smooth 1-manifold. Such sections we refer to as generic sections of $\left(\mathcal{L}_{\alpha \gamma}^{\pi}, s_{\alpha \gamma}^{\pi}\right)$. Looking at the boundary of this zero set we see that it consists of
$$\bigcup_{\{\beta \mid \mathfrak{i}(\alpha, \beta)=1 \bmod (d(\mathfrak{s}))\}}\left(\hat{s}_{\alpha \beta}^{-1}(0) \times \hat{\mathcal{M}}^{0}(\beta, \gamma) \cup \mathcal{M}^{0}(\alpha, \beta) \times \hat{s}_{\beta \gamma}^{-1}(0)\right) .$$
Here $\hat{s}_{\alpha \beta}$ and $\hat{s}_{\beta \gamma}$ are generic sections of $\left(\mathcal{L}_{\alpha \beta}^{\pi}, s_{\alpha \beta}^{\pi}\right)$ and $\left(\mathcal{L}_{\beta \gamma}^{\pi}, s_{\beta \gamma}^{\pi}\right)$ respectively. The counting of these boundary points implies that
$$\sum_{\{\beta \mid \mathfrak{i}(\alpha, \beta)=1 \bmod (d(\mathfrak{s}))\}}[\pi]_{\alpha \beta} n_{\beta \gamma}-\sum_{\left\{\beta^{\prime} \mid \mathfrak{i}\left(\alpha, \beta^{\prime}\right)=1 \bmod (d(\mathfrak{s}))\right\}} n_{\alpha \beta^{\prime}}[\pi]_{\beta^{\prime} \gamma}=0 .$$
Hence $[\pi]$ is a chain map so we have defined an action of $H_{1}(Y, \mathbb{Z}) /$ Torsion on $H F_{*}^{S W}(Y, \mathfrak{s})$.
To get $[\pi] \circ[\pi]=0$ on the chain level, we need to give another way of calculating the relative Euler number of $\left(\mathcal{L}_{\alpha \beta}^{\pi}, s_{\alpha \beta}^{\pi}\right)$ in terms of the following holonomy map:
$$h_{\alpha \beta}^{\pi}: \quad \mathcal{M}^{1}(\alpha, \beta) \longrightarrow U(1),$$
where $h_{\alpha \beta}^{\pi}([\mathbb{A}, \Psi])$ is given by the holonomy of $\mathbb{A}$ along the loop $\left\{t_{0}\right\} \times \pi$ for any $[\mathbb{A}, \Psi] \in \mathcal{M}^{1}(\alpha, \beta)$. Let $\omega$ be the standard closed 1-form on $U(1)$ with integral one over $U(1)$. Then pulling back:
$$[\pi]_{\alpha \beta}=\int_{\mathcal{M}^{1}(\alpha, \beta)}\left(h_{\alpha \beta}^{\pi}\right)^{*} \omega$$
which is the winding number of the holonomy map $h_{\alpha \beta}^{\pi}$, that is, the counting of a generic fiber of $h_{\alpha \beta}^{\pi}$.

Now for two critical points $\alpha$ and $\gamma$ with relative index $2 \bmod (d(\mathfrak{s}))$, the corresponding holonomy map can be extended over the partial compactification of $\mathcal{M}^{2}(\alpha, \gamma)^{*}$. We denote this holonomy map by $h_{\alpha \gamma}^{\pi}$. Then the fiber of $h_{\alpha \gamma}^{\pi}$ at a generic point $p \in U(1)$ is an oriented smooth 1-manifold whose boundary consists of
$$\bigcup_{\{\beta \mid \mathfrak{i}(\alpha, \beta)=1 \bmod (d(\mathfrak{s}))\}}\left(h_{\alpha \beta}^{\pi}\right)^{-1}(p) \times\left(h_{\beta \gamma}^{\pi}\right)^{-1}(p) .$$
Counting these boundary points with sign, we obtain
$$\sum_{\{\beta \mid \mathfrak{i}(\alpha, \beta)=1 \bmod (d(\mathfrak{s}))\}}[\pi]_{\alpha \beta}[\pi]_{\beta \gamma}=0 .$$
This shows that $[\pi] \circ[\pi]=0$ on the chain level. Hence there is an action of $\Lambda^{*}\left(H_{1}(Y, \mathbb{Z}) /\right.$ Torsion $)$ on the Seiberg-Witten-Floer homology $H F_{*}^{S W}(Y, \mathfrak{s})$. \(\square\)

Let $(-Y,-\mathfrak{s})$ be the 3-manifold $Y$ with the reversed orientation. There is a one-to-one correspondence between the 3-dimensional monopoles on $(Y, \mathfrak{s})$ and $(-Y,-\mathfrak{s})$
$$\mathcal{M}_{Y}(\mathfrak{s}, \eta) \cong \mathcal{M}_{-Y}(-\mathfrak{s},-\eta)$$
which sends $\alpha \mapsto \hat{\alpha}$, such that
$$\mathfrak{i}_{Y}(\alpha, \beta)=\mathfrak{i}_{-Y}(\hat{\beta}, \hat{\alpha}) .$$
There is also an orientation preserving diffeomorphism between the moduli space of gradient flow lines for the Chern-Simons-Dirac functionals on $(Y, \mathfrak{s})$ and $(-Y,-\mathfrak{s})$ :
$$\mathcal{M}_{\mathbb{R} \times Y}(\alpha, \beta) \cong \mathcal{M}_{\mathbb{R} \times-Y}(\hat{\beta}, \hat{\alpha}) .$$
Hence from the construction of the Seiberg-Witten-Floer homology, we see that $C_{-*}(-Y,-\mathfrak{s})$ can be identified to the dual complex of $C_{*}(Y, \mathfrak{s})$. This gives rise to a natural pairing
$$\langle,\rangle: \quad H F_{*}^{S W}(Y, \mathfrak{s}) \times H F_{-*}^{S W}(-Y,-\mathfrak{s}) \longrightarrow \mathbb{Z},$$
which satisfies the following properties whose proofs are immediate from the definition:
\begin{itemize}
\item[1.] For two relative degree 2 cycles $\Xi_{1}$ and $\Xi_{2}$ in $H F_{*}^{S W}(Y, \mathfrak{s})$ and $H F_{-*}^{S W}(-Y,-\mathfrak{s})$ respectively $<U\left(\Xi_{1}\right), \Xi_{2}>=<\Xi_{1}, U\left(\Xi_{2}\right)>$.
\item[2.] For two relative degree 1 cycles $\Xi_{1}$ and $\Xi_{2}$ in $H F_{*}^{S W}(Y, \mathfrak{s})$ and $H F_{-*}^{S W}(-Y,-\mathfrak{s})$ respectively, and any $[\pi] \in H_{1}(Y, \mathbb{Z}) /$ Torsion $\cong H_{1}(-Y, \mathbb{Z}) /$ Torsion $,<[\pi]\left(\Xi_{1}\right), \Xi_{2}>=<\Xi_{1},[\pi]\left(\Xi_{2}\right)>$.
\end{itemize}
Thus, $<z \cdot \Xi_{1}, \Xi_{2}>=<\Xi_{1}, z \cdot \Xi_{2}>$ for any $z \in \mathbb{A}(Y) \cong \mathbb{A}(-Y)$, for any cycles $\Xi_{1} \in H F_{*}^{S W}(Y, \mathfrak{s})$ and $\Xi_{2} \in H F_{-*}^{S W}(-Y,-\mathfrak{s})$ respectively.

\subsection*{3.5 Variants of the Seiberg-Witten-Floer homology}

The Seiberg-Witten-Floer homology $H F_{*}^{S W}(Y, \mathfrak{s})$, as defined in the previous subsection, is a finitely generated $\mathbb{Z}_{d(\mathfrak{s})}$-graded Abelian group. There are various ways of defining $\mathbb{Z}$-graded Seiberg-Witten-Floer homology groups for any closed oriented 3-manifold $Y$ with a non-torsion Spin ${ }^{c}$ structure $\mathfrak{s}$. These were briefly discussed at the end of section 4.1 of [20]. In this subsection, we propose a way of defining $\mathbb{Z}$-graded Seiberg-Witten-Floer homology, which will be convenient for our later description of the relative Seiberg-Witten invariant for a 4-manifold with cylindrical end modelled on $([-2, \infty) \times Y, \mathfrak{s})$.

Notice that the first Chern class of the non-torsion Spin ${ }^{c}$ structure $\mathfrak{s}$ defines a homomorphism: $c_{1}(\mathfrak{s}): \quad H^{1}(Y, \mathbb{Z}) \longrightarrow \mathbb{Z}$ by $c_{1}(\mathfrak{s})([u])=<[u] \cup c_{1}(\mathfrak{s}),[Y]>$ for any element $[u] \in H^{1}(Y, \mathbb{Z})$.

For any subgroup $K \subseteq \operatorname{Ker}\left(c_{1}(\mathfrak{s})\right)$, there is a subgroup $\mathcal{G}_{Y}^{K}$ of the full gauge transformation group $\mathcal{G}_{Y}$, whose elements lie in the connected components determined by $K$ (note that the
group of connected components of $\mathcal{G}_{Y}$ is $H^{1}(Y, \mathbb{Z})$ ). Consider the Seiberg-Witten-Floer homology theory for the Chern-Simons-Dirac functional on the configuration space $\mathcal{A}_{Y}$ modulo the gauge group $\mathcal{G}_{Y}^{K}$. The critical point set, denoted by $\mathcal{M}_{Y, K}(\mathfrak{s}, \eta)$, is a covering space
$$\pi_{K}: \quad \mathcal{M}_{Y, K}(\mathfrak{s}, \eta) \longrightarrow \mathcal{M}_{Y}(\mathfrak{s}, \eta)$$
whose fiber is an $H^{1}(Y, \mathbb{Z}) / K$-homogeneous space, hence, there is a natural action of $H^{1}(Y, \mathbb{Z}) / K$ on $\mathcal{M}_{Y, K}(\mathfrak{s}, \eta)$.

The generators of this variant of the Seiberg-Witten-Floer chain complex are elements in $\mathcal{M}_{Y, K}(\mathfrak{s}, \eta)$, with relative $\mathbb{Z}$-graded indices. Denote this chain complex by
$$C_{*,[K]}^{S W}(Y, \mathfrak{s})=\sum_{\Gamma \in \mathcal{M}_{Y, K}(\mathfrak{s}, \eta)} \mathbb{Z}<\Gamma>.$$
The boundary operator $\partial^{K}$ is given by counting the gradient flowlines of the perturted CSD functional on $\mathcal{A}_{Y} / \mathcal{G}_{Y}^{K}$ connecting two critical points with relative index 1. Fix an element $\Gamma_{\alpha} \in \pi_{K}^{-1}(\alpha)$, for any critical point $\beta \in \mathcal{M}_{Y}(\mathfrak{s}, \eta)$, there is an orientation presevering diffeomorphism
$$\mathcal{M}(\alpha, \beta) \cong \bigcup_{\Gamma_{\beta} \in \pi_{K}^{-1}(\beta)} \mathcal{M}\left(\Gamma_{\alpha}, \Gamma_{\beta}\right),$$
where $\mathcal{M}\left(\Gamma_{\alpha}, \Gamma_{\beta}\right)$ is the moduli space of flowlines on $\mathcal{A}_{Y} / \mathcal{G}_{Y}^{K}$ connecting $\Gamma_{\alpha}$ and $\Gamma_{\beta}$. Hence, it is easy to see that there is a well-defined topological invariant, given by the homology of this new version of the Seiberg-Witten-Floer chain complex, though not finitely generated, still admitting an action of $\mathbb{A}(Y)$.

Definition 3.26. For any subgroup $K \subseteq \operatorname{Ker}\left(c_{1}(\mathfrak{s})\right)$, there is a variant of the Seiberg-Witten-Floer chain complex, whose generators are elements from the covering space $\mathcal{M}_{Y, K}(\mathfrak{s}, \eta)$ of $\mathcal{M}_{Y}(\mathfrak{s}, \eta)$, and the boundary operator is given by counting the gradient flowlines of the perturbed CSD functional on $\mathcal{A}_{Y} / \mathcal{G}_{Y}^{K}$ connecting two critical points with relative index 1. We denote the Seiberg-Witten-Floer homology in this setting by $H F_{*,[K]}^{S W}(Y, \mathfrak{s})$, the actions of elements in $H_{0}(Y, \mathbb{Z})$ and $H_{1}(Y, \mathbb{Z}) /$ Torsion decreasing degree in $H F_{*,[K]}^{S W}(Y, \mathfrak{s})$ by 2 and 1 respectively.

From the definition, it is easy to get the following periodicity property for $H F_{*,\left[K e r\left(c_{1}(\mathfrak{s})\right)\right]}^{S W}(Y, \mathfrak{s})$ :
$$H F_{m,\left[K e r\left(c_{1}(\mathfrak{s})\right)\right]}^{S W}(Y, \mathfrak{s}) \cong H F_{m}^{S W} \bmod (d(\mathfrak{s}))(Y, \mathfrak{s}),$$
for any $m \in \mathbb{Z}$.
Remark 3.27. From the natural action of $H_{1}(Y, \mathbb{Z}) / K$ on the generators of the chain complex $C_{*,[K]}^{S W}(Y, \mathfrak{s}), H F_{*,[K]}^{S W}(Y, \mathfrak{s})$ can be thought as an $H_{1}(Y, \mathbb{Z}) / K$-equivariant Seiberg-Witten-Floer
homology of $(Y, \mathfrak{s})$. For any $[u] \in H_{1}(Y, \mathbb{Z}) / K$, the action of $[u]$ on $H F_{*,[K]}^{S W}(Y, \mathfrak{s})$ is the following $\mathbb{A}(Y)$-equivariant homomorphism:
$$[u]: \quad H F_{*,[K]}^{S W}(Y, \mathfrak{s}) \longrightarrow H F_{*-n,[K]}^{S W}(Y, \mathfrak{s})$$
with $n=<[u] \wedge c_{1}(\mathfrak{s}),[Y]>$.
For $(-Y,-\mathfrak{s})$, where $-Y$ is $Y$ with the reversed orientation and $-\mathfrak{s}$ is the induced Spin ${ }^{c}$ structure, the corresponding Seiberg-Witten-Floer complex $C_{*,[K]}^{S W}(-Y,-\mathfrak{s})$ is the dual complex of $C_{*,[K]}^{S W}(Y, \mathfrak{s})$. This gives a natural pairing
$$\langle,\rangle: \quad H F_{*,[K]}^{S W}(Y, \mathfrak{s}) \times H F_{-*,[K]}^{S W}(-Y,-\mathfrak{s}) \longrightarrow \mathbb{Z}$$
satisfying $<z \cdot \Xi_{1}, \Xi_{2}>=<\Xi_{1}, z \cdot \Xi_{2}>$ for any $z \in \mathbb{A}(Y) \cong \mathbb{A}(-Y)$ and any cycles $\Xi_{1} \in H F_{*,[K]}^{S W}(Y, \mathfrak{s})$ and $\Xi_{2} \in H F_{-*,[K]}^{S W}(-Y,-\mathfrak{s})$ respectively.

For any subgroup $K$ in $\operatorname{Ker}\left(c_{1}(\mathfrak{s})\right)$, there is a chain map $C_{*,[K]}^{S W}(Y, \mathfrak{s}) \rightarrow C_{*}^{S W}(Y, \mathfrak{s})$ induced from the map $\pi_{K}$, which descends to an $\mathbb{A}(Y)$-equivariant homomorphism
$$\pi_{K}: \quad H F_{*,[K]}^{S W}(Y, \mathfrak{s}) \longrightarrow H F_{*}^{S W}(Y, \mathfrak{s}) .$$

Let $K_{1} \subset K_{2}$ be two subgroups in $\operatorname{Ker}\left(c_{1}(\mathfrak{s})\right)$. There is a covering map
$$\pi: \quad \mathcal{M}_{Y, K_{1}}(\mathfrak{s}, \eta) \longrightarrow \mathcal{M}_{Y, K_{2}}(\mathfrak{s}, \eta)$$
which induces a map:
$$\pi_{*}: \quad C_{*,\left[K_{1}\right]}^{S W}(Y, \mathfrak{s}) \longrightarrow C_{*,\left[K_{2}\right]}^{S W}(Y, \mathfrak{s})$$
assigning the generator $\langle\Gamma\rangle$ of $C_{*,\left[K_{1}\right]}(Y, \mathfrak{s})$ to $\langle\pi(\Gamma)\rangle$ in $C_{*,\left[K_{2}\right]}(Y, \mathfrak{s})$. For any $\alpha, \beta$ in $\mathcal{M}_{Y, K_{2}}(\mathfrak{s}, \eta)$ of relative index 1, and for any fixed $\Gamma_{\alpha}$ in $\pi^{-1}(\alpha)$, there is an orientation preserving diffeomorphism:
$$\mathcal{M}_{\mathbb{R} \times Y}(\alpha, \beta) \cong \bigcup_{\Gamma_{\beta} \in \pi^{-1}(\beta)} \mathcal{M}_{\mathbb{R} \times Y}\left(\Gamma_{\alpha}, \Gamma_{\beta}\right) .$$
which implies that $\pi_{*}$ is a chain map and induces an $\mathbb{A}(Y)$-equivariant homomorphism
$$\pi: \quad H F_{*,\left[K_{1}\right]}^{S W}(Y, \mathfrak{s}) \longrightarrow H F_{*,\left[K_{2}\right]}^{S W}(Y, \mathfrak{s}) .$$

For any two subgroups $K_{1}$ and $K_{2}$ in $\operatorname{Ker}\left(c_{1}(\mathfrak{s})\right)$, we have the following commutative diagram which relates various covering spaces of $\mathcal{M}_{Y}(\mathfrak{s}, \eta)$ :
$$\begin{array}{lcccl} 
& & M_{Y, K_{1}}(\mathfrak{s}, \eta) & & \\
M_{Y, K_{1} \cap K_{2}}(\mathfrak{s}, \eta) & & { }^{\pi_{1}} & \\
& & \xrightarrow{\pi_{2}} & & \mathcal{M}_{Y}(\mathfrak{s}, \eta) \\
& \searrow & & { }^{\pi_{2}} & \\
& & \mathcal{M}_{Y, K_{2}}(\mathfrak{s}, \eta) & &
\end{array}$$
where the fibers of $\pi_{0}, \pi^{1}, \pi_{1}, \pi^{2}$ and $\pi_{2}$ are the homogeneous spaces of $H^{1}(Y, \mathbb{Z}) /\left(K_{1} \cap K_{2}\right)$, $K_{1} /\left(K_{1} \cap K_{2}\right), H^{1}(Y, \mathbb{Z}) / K_{1}, K_{2} /\left(K_{1} \cap K_{2}\right)$ and $H^{1}(Y, \mathbb{Z}) / K_{2}$ respectively.

Fix an element in $\mathcal{M}_{Y, K_{1} \cap K_{2}}(\mathfrak{s}, \eta)$, then there is a well-defined $\mathbb{Z}$-graded index on $\mathcal{M}_{Y, K_{1} \cap K_{2}}(\mathfrak{s}, \eta)$, as $K_{1}$ and $K_{2}$ are two subgroups of $\operatorname{Ker}\left(c_{1}(\mathfrak{s})\right)$. Hence there are the induced $\mathbb{Z}$-graded indices on $\mathcal{M}_{Y, K_{1}}(\mathfrak{s}, \eta)$ and $\mathcal{M}_{Y, K_{2}}(\mathfrak{s}, \eta)$. The $\mathcal{A}(Y)$-equivariant homomorphisms as provided in (45) and (44) induce the following commutative diagram of $\mathbb{A}(Y)$-equivariant homomorphisms.
![](https://cdn.mathpix.com/cropped/fe62acfa-5786-4f08-ad7d-3eb6081e3ffb-43.jpg?height=248&width=934&top_left_y=762&top_left_x=658)

\section*{4 Gluing formulae for 4-dimensional Seiberg-Witten invariants}

In this Section, we will study the Seiberg-Witten invariant of a closed smooth 4-manifold $X$ with $b_{2}^{+}(X)>1$ and Spin ${ }^{c}$ structure $\mathfrak{s}$ by stretching its metric along a smooth embedded separating 3-manifold $Y$ with the condition that $\left.\mathfrak{s}\right|_{Y}$ is non-torsion. Consider a 1-parameter family of metrics $\left\{g_{R}\right\}_{R>0}$ on $X$ such that for each $\left(X, g_{R}\right)$, there is an isometrical embedding
$$\left([-R-2, R+2] \times Y, d t^{2}+g_{Y}\right) \longrightarrow\left(X, g_{R}\right) .$$
Write for brevity, $X(R)=\left(X, g_{R}\right)$.
As $Y$ separates $X=X(0)$, we write $X(0)=X_{+} \cup X_{-}$with $Y=\{0\} \times Y=X_{+} \cap X_{-}$. There is a canonical orientation preserving isometry
$$\Theta_{R}: \quad X(R)-\{0\} \times Y \longrightarrow X_{+}(R) \cup X_{-}(R),$$
where $X_{+}(R)=X_{+} \cup[0, R] \times Y, X_{-}(R)=X_{-} \cup[-R, 0] \times Y$. As $R \rightarrow \infty, X_{ \pm}(R)$ become 4 -manifolds with cylindrical ends modelled on $[-2, \infty) \times Y$ and $(-\infty, 2] \times Y$. We denote these 4 -manifolds by $X_{ \pm}(\infty)$.