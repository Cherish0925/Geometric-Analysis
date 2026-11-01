---
retention_scope: session
part: 3
total_parts: 5
---

[Part 3/5 of: [PDF] On tamed almost complex four manifolds]

Suppose that $J$ is an almost complex structure on $\mathbb{R}^{4}$ which is tamed by a symplectic 2-form $\omega_{1}=F+d_{J}^{-}(v+\bar{v})$, where $F$ is a fundamental form on $\mathbb{R}^{4}$ and $v \in \Lambda_{J}^{0,1} \otimes L_{1}^{2}\left(\mathbb{R}^{4}\right)$. Let $g_{J}(\cdot, \cdot)=F(\cdot, J \cdot)$ be an almost Hermitian metric and $d \mu_{g_{J}}$ the volume form. Let $(\Omega, J)$ be a bounded open set in $\left(\mathbb{R}^{4}, J\right), A=u+\bar{u} \in \Lambda_{\mathbb{R}}^{1} \otimes L_{1}^{2}(\Omega)$ and satisfy $d_{J}^{-}(A)=0$, where $u \in \Lambda_{J}^{0,1} \otimes L_{1}^{2}(\Omega)$. Let $L_{2}^{2}(\Omega)_{0}$ be the completion of the space of smooth functions with compact support in $\Omega$ under the $L_{2}^{2}$ norm. Since $d_{J}^{-} d^{*}: \Omega_{J}^{-}(\Omega) \rightarrow \Omega_{J}^{-}(\Omega)$ is a strongly elliptic linear operator (see Section 2 or [56]), where $d^{*}=-*_{g_{J}} d *_{g_{J}}$, we define a linear operator $\widetilde{\mathcal{W}}$ as in Section 2, $\widetilde{\mathcal{W}}: L_{2}^{2}(\Omega)_{0} \longrightarrow \Lambda_{\mathbb{R}}^{1} \otimes L_{1}^{2}(\Omega)$, where $L_{2}^{2}(\Omega)_{0}$ is the completion of the space of smooth functions with compact support in $\Omega$ under the $L_{2}^{2}$ norm,
$$\widetilde{\mathcal{W}}(f)=J d f+d^{*}\left(\eta_{f}^{1}+\bar{\eta}_{f}^{1}\right)-*_{g_{J}}\left(d f \wedge d_{J}^{-}(v+\bar{v})\right)+d^{*}\left(\eta_{f}^{2}+\bar{\eta}_{f}^{2}\right), \quad \eta_{f}^{1}, \eta_{f}^{2} \in \Lambda_{J}^{0,2} \otimes L_{2}^{2}(\Omega),$$
satisfying
$$\begin{gathered}
d^{*} \widetilde{\mathcal{W}}(f)=0 \\
d_{J}^{-} J d f+d_{J}^{-} d^{*}\left(\eta_{f}^{1}+\bar{\eta}_{f}^{1}\right)=0
\end{gathered}$$
and
$$-d_{J}^{-} *_{g_{J}}\left(d f \wedge d_{J}^{-}(v+\bar{v})\right)+d_{J}^{-} d^{*}\left(\eta_{f}^{2}+\bar{\eta}_{f}^{2}\right)=0$$
where
$$\left.\eta_{f}^{1}\right|_{\partial \Omega}=0,\left.\quad \eta_{f}^{2}\right|_{\partial \Omega}=0 .$$
Notice that $C_{0}^{\infty}(\Omega)$ (which is the space of smooth functions with compact support in $\Omega$ ) is dense in $L_{2}^{2}(\Omega)_{0}$. The question with our relationship is whether $\widetilde{\mathcal{W}}(f)=A$ has a solution. Note that $d_{J}^{-} \circ \widetilde{\mathcal{W}}=0$. If we use the theory of Hilbert space, considing
$$L_{2}^{2}(\Omega)_{0} \xrightarrow{\widetilde{\mathcal{W}}} \Lambda_{\mathbb{R}}^{1} \otimes L_{1}^{2}(\Omega) \xrightarrow{d_{J}^{-}} \Lambda_{J}^{-} \otimes L^{2}(\Omega),$$
then the above problem is equivalent to: Whether the kernel of $d_{J}^{-}$is equal to the image of $\widetilde{\mathcal{W}}$. As the $\bar{\partial}$-problem in classical complex analysis, we call this problem the $\widetilde{\mathcal{W}}, d_{J^{-}}^{-}$problem.

Our approach is along the lines used by L. Hörmander to present the method of $L^{2}$ estimates for the $\bar{\partial}$-problem in [39]. We summarize the above discussion in terms of the model of Hilbert spaces below:
$$H_{1} \xrightarrow{T} H_{2} \xrightarrow{S} H_{3},$$
where $H_{1}, H_{2}, H_{3}$ are all Hilbert spaces, and $T, S$ are linear, closed and densely defined operators. Assume $S T=0$, the problem is whether, $\forall g \in \operatorname{ker} S$, a solution to
$$T f=g$$
exists. First, note a simple fact that $T f=g$ is equivalent to
$$(T f, h)_{H_{2}}=(g, h)_{H_{2}}, \quad \forall h \in \text { some dense subset }$$
because $(T f-g, h)_{H_{2}}=0, \forall h \in$ some dense subset $\Longleftrightarrow\left(T f-g, H_{2}\right)_{H_{2}}=0 \Longleftrightarrow T f=g$.
Let $T^{*}$ be an adjoint operator of $T$ in the sense of distributions. By the theory of functional analysis, $T^{*}$ is a closed operator, and $\left(T^{*}\right)^{*}=T$ if and only if $T$ is closed.

From (A.11), $(T f, h)_{H_{2}}=(g, h)_{H_{2}}, \forall h \in$ some dense subset. If this dense subset is contained in $D_{T^{*}}$, then, noticing $(T f, h)_{H_{2}}=\left(f, T^{*} h\right)_{H_{1}}$,
$$\begin{aligned}
T f=g & \Longleftrightarrow(T f, h)_{H_{2}}=(g, h)_{H_{2}} \\
& \Longleftrightarrow\left(f, T^{*} h\right)_{H_{1}}=(g, h)_{H_{2}}, \quad \forall h \in \text { some dense subset in } \mathrm{D}_{\mathrm{T}^{*}} .
\end{aligned}$$
Let $T^{*} h \longrightarrow(g, h)_{H_{2}}$ be a linear functional defined on a subset of $H_{1}$ (that is, $\left\{T^{*} g \mid g \in\right.$ some dense subset in $\left.D_{T^{*}}\right\}$ ). If we can extend the above functional to a bounded linear functional on the entire $H_{1}$, then an application of Riesz Representation theorem to (A.12) will thus show that the problem $T f=g$ is solved. Recall that the Riesz Representation theorem states that if $\lambda: H \rightarrow \mathbb{C}$ is a bounded linear functional on a Hilbert space $H$, then there exists $g \in H$ such that $\lambda(x)=(x, g)_{H} \forall x \in H$. Hence the main step is whether we can extend $T^{*} h \longrightarrow(g, h)_{H_{2}}$ to a bounded linear functional on the entire $H_{1}$ (for details, see [39, 40]).

As in classical complex analysis, we have the following lemmas:
Lemma A.24. (cf. [39, Theorem 1.1.1]) If there exists a constant $c_{g}$ depending only on $g$ such that
$$\left|(g, h)_{H_{2}}\right| \leq c_{g}\left\|T^{*} h\right\|_{H_{1}},$$
then $T^{*} h \longrightarrow(g, h)_{H_{2}}$ can be extended to a bounded linear functional on $H_{1}$.
In the above discussion, we used only the front half of
$$H_{1} \xrightarrow{T} H_{2} \xrightarrow{S} H_{3} .$$

However, since we only need to solve the equation $T f=g$ or $\left(T^{*} h, f\right)=(h, g)$ for $g \in \operatorname{ker} S$, it is unnecessary to prove (A.13) for $g \in H_{2}$, rather we just need to prove (A.13) for $g \in \operatorname{ker} S$. In this case, we hope that $h$ in (A.13) belongs to some dense subset in $D_{T^{*}}$.

The method of proving
$$\left|(g, h)_{H_{2}}\right| \leq c_{g}\left\|T^{*} h\right\|_{H_{1}}$$
is through proving a more general inequality:
$$\|h\|_{H_{2}}^{2} \leq c\left(\left\|T^{*} h\right\|_{H_{1}}^{2}+\|S h\|_{H_{3}}^{2}\right), \quad h \in D_{T^{*}} \cap D_{S} .$$
First we note, in our problem, $D_{T^{*}}$ and $D_{S}$ contain $C^{\infty}(\Omega)_{0}$ which is the space of smooth functions on $\Omega$ with compact support, hence $D_{T^{*}} \cap D_{S}$ is dense on both $D_{T^{*}}$ and $H_{2}$. Notice that $T, S$ are linear, closed densely defined operators, and $S T=0$. Now we need

Lemma A.25. (cf. 39, Theorem 1.1.2]) If
$$\|h\|_{H_{2}}^{2} \leq c\left(\left\|T^{*} h\right\|_{H_{1}}^{2}+\|S h\|_{H_{3}}^{2}\right) h \in D_{T^{*}} \cap D_{S},$$
then
$$\left|(g, h)_{H_{2}}\right| \leq c^{\frac{1}{2}}\|g\|_{H_{2}}\left\|T^{*} h\right\|_{H_{1}} \quad \forall g \in \operatorname{ker} S, \quad h \in D_{T^{*}} \cap D_{S} .$$

Applying Lemma A.25, we have that if
$$\|h\|_{H_{2}}^{2} \leq c\left(\left\|T^{*} h\right\|_{H_{1}}^{2}+\|S h\|_{H_{3}}^{2}\right)$$
for all $h \in D_{T^{*}} \cap D_{S}$, then
$$\left|(g, h)_{H_{2}}\right| \leq c^{\frac{1}{2}}\|g\|_{H_{2}}\left\|T^{*} h\right\|_{H_{1}} \quad \forall g \in \operatorname{ker} S, h \in D_{T^{*}} \cap D_{S} .$$
Hence, by Lemma A.24, $T^{*} h \longrightarrow(g, h)_{H_{2}}$ can be extended to a bounded linear functional on $H_{1}$, whose bound is $c^{\frac{1}{2}}\|g\|_{H_{2}}$. By Riesz Representation theorem, there exists $f \in H_{1}$ such that
$$\left(T^{*} h, f\right)_{H_{1}}=(h, g)_{H_{2}}, \forall h \in D_{T^{*}} \cap D_{S} .$$
Since $D_{T^{*}} \cap D_{S}$ is dense in $H_{2}$, we have
$$(h, T f)_{H_{2}}=(h, g)_{H_{2}}, \quad \forall h \in H_{2} .$$
By (A.12), the equation $T f=g$ has a solution. In addition, from the Riesz Representation theorem, we have
$$\|f\|_{H_{1}} \leq c^{\frac{1}{2}}\|g\|_{H_{2}}, \quad f \in(\operatorname{ker} T)^{\perp} .$$
In fact,
$$\|f\|_{H_{1}} \leq c^{\frac{1}{2}}\|g\|_{H_{2}}$$
is the direct consequence of Riesz Representation theorem. To show $f \in(\operatorname{ker} T)^{\perp}$, note that, according to the way that $T^{*} h \rightarrow(h, g)_{H_{2}}$ is extended to a bounded linear functional on the entire $H_{1}$, this functional vanishes on the orthogonal complement of
$\overline{\left\{T^{*} h \mid h \in D_{T^{*}}\right\}}$, thus $f \in \overline{\left\{T^{*} h \mid h \in D_{T^{*}}\right\}}$. If $f \in \lim _{k \rightarrow \infty} T^{*} h_{k}$, then for every $X \in \operatorname{ker} T$, we have
$$(X, f)_{H_{1}}=\lim _{k \rightarrow \infty}\left(X, T^{*} h_{k}\right)_{H_{1}}=\lim _{k \rightarrow \infty}\left(T X, h_{k}\right)_{H_{2}}=0,$$
hence, $f \in(\operatorname{ker} T)^{\perp}$.
In general, the solution of $T f=g$ is not unique, since $f_{1} \in \operatorname{ker} T$, then
$$\begin{aligned}
\left(T^{*} h, f+f_{1}\right)_{H_{1}} & =\left(T^{*} h, f\right)_{H_{1}}+\left(T^{*} h, f_{1}\right)_{H_{1}} \\
& =\left(T^{*} h, f\right)_{H_{1}}+\left(T h, T f_{1}\right)_{H_{2}} \\
& =\left(T^{*} h, f\right)_{H_{1}},
\end{aligned}$$
and $f, f+f_{1}$ are both the solutions of $T f=g$. However, $f \in(\operatorname{ker} T)^{\perp}$ is the condition to assure that the above solution to $T f=g$ is unique.

From the above discussion, we have
Lemma A.26. (cf. 39, Theorem 1.1.4]) If
$$\|h\|_{H_{2}}^{2} \leq c\left(\left\|T^{*} h\right\|_{H_{1}}^{2}+\|S h\|_{H_{3}}^{2}\right),$$
then $T f=g$ has a solution to $g \in \operatorname{ker} S$. This solution $f$ satisfies the estimate
$$\|f\|_{H_{1}} \leq c^{\frac{1}{2}}\|g\|_{H_{2}}, \quad f \in(\operatorname{ker} T)^{\perp} .$$

We now return to the $\widetilde{\mathcal{W}}, d_{J}^{-}$-problem discussed above. If $\varphi$ is a continuous function in $\Omega$, we denote by $L^{2}(\Omega, \varphi)$ the space of functions in $\Omega$ which are square integrable with respect to the measure $e^{-\varphi} d \mu_{g_{J}}$. This is a subspace of the space $L^{2}(\Omega, l o c)$ of functions in $\Omega$ which are locally square integrable with respect to the Lebesgue measure, and it is clear that every function in $L^{2}(\Omega, l o c)$ belongs to $L^{2}(\Omega, \varphi)$ for some $\varphi$. By $\Lambda^{k} \otimes L^{2}(\Omega, \varphi)$ we denote the space of $k$-forms with coefficients in $L^{2}(\Omega, \varphi)$. We set
$$\|f\|^{2}=\int_{\Omega}|f|^{2} e^{-\varphi} d \mu_{g_{J}}$$
It is clear that $L^{2}(\Omega, \varphi)$ is a Hilbert space with this norm.
In our application of the above lemmas, the spaces $H_{1}, H_{2}$ and $H_{3}$ will be $L_{2}^{2}(\Omega, \varphi)_{0}$, $\Lambda_{\mathbb{R}}^{1} \otimes L_{1}^{2}(\Omega, \varphi)$ and $\Lambda_{J}^{-} \otimes L^{2}(\Omega, \varphi)$, respectively, $T$ the operator between these space defined as explained above by the $\widetilde{\mathcal{W}}$ operator, and let $G$ be the set of all $A \in \Lambda_{\mathbb{R}}^{1} \otimes L_{1}^{2}(\Omega, \varphi)$ with $d_{J}^{-}(A)=0$. Let $S$ be the operator from $\Lambda_{\mathbb{R}}^{1} \otimes L_{1}^{2}(\Omega, \varphi)$ to $\Lambda_{J}^{-} \otimes L^{2}(\Omega, \varphi)$ defined by $d_{J}^{-}$. Then $G$ is the null space of $S$, and to prove (A.14) it will be sufficient to show that
$$\|A\|_{H_{2}}^{2} \leq C^{2}\left(\left\|T^{*} A\right\|_{H_{1}}^{2}+\|S A\|_{H_{3}}^{2}\right), \quad A \in D_{T^{*}} \cap D_{S} .$$
To prove this basic inequality, we require the following set steps:
Step 1. The formally adjoint operator, $\widetilde{\mathcal{W}^{*}}$, of $T=\widetilde{\mathcal{W}}$ (for $\bar{\partial}$-operator cf. L. Hörmander [39]).

First, we calculate it in the non weighted space. For all $f \in C^{\infty}(\bar{\Omega}) \subset D_{\widetilde{\mathcal{W}}}$ (where $C^{\infty}(\bar{\Omega})$ is the set of infinitely differentiable functions on some neighborhood of $\bar{\Omega}$ ), we have
$$(\widetilde{\mathcal{W}}(f), A)=\left(f, \widetilde{\mathcal{W}}^{*} A\right) .$$
If $\operatorname{supp} f \subset \Omega, A=u+\bar{u} \in \Omega_{\mathbb{R}}^{1}(\bar{\Omega})$ (where $\Omega_{\mathbb{R}}^{1}(\bar{\Omega})$ is the set of infinitely differentiable real 1-forms on some neighborhood of $\bar{\Omega}$ ), $u \in \Omega_{J}^{0,1}(\bar{\Omega})$ (where $\Omega_{J}^{0,1}(\bar{\Omega})$ is the set of infinitely differentiable real (0, 1)-forms with respect to the almost complex structure $J$ on some neighborhood of $\bar{\Omega}$ ) and $d_{J}^{-}(A)=0$, the above equality becomes
$$\begin{aligned}
\widetilde{\mathcal{W}}(f), A)= & -\int_{\Omega} A \wedge d\left[f \omega_{1}+\left(\eta_{f}^{1}+\eta_{f}^{2}+\bar{\eta}_{f}^{1}+\bar{\eta}_{f}^{2}\right)\right] \\
= & -\int_{\Omega} d(A) \wedge\left[f \omega_{1}+\left(\eta_{f}^{1}+\eta_{f}^{2}+\bar{\eta}_{f}^{1}+\bar{\eta}_{f}^{2}\right)\right] \\
= & -\int_{\Omega} d_{J}^{+}(A) \wedge\left[f \omega_{1}+\left(\eta_{f}^{1}+\eta_{f}^{2}+\bar{\eta}_{f}^{1}+\bar{\eta}_{f}^{2}\right)\right] \\
& -\int_{\Omega} d_{J}^{-}(A) \wedge\left[f \omega_{1}+\left(\eta_{f}^{1}+\eta_{f}^{2}+\bar{\eta}_{f}^{1}+\bar{\eta}_{f}^{2}\right)\right] \\
= & -\int_{\Omega} d_{J}^{+}(A) \wedge f F \\
= & \left(f, \widetilde{\mathcal{W}}^{*} A\right)
\end{aligned}$$
is valid to all $f \in C^{\infty}(\bar{\Omega})_{0}$. Thus, the formally adjoint operator of $\widetilde{\mathcal{W}}$ is
$$\widetilde{\mathcal{W}^{*}} A=\frac{-2 F \wedge d_{J}^{+}(A)}{F^{2}} .$$
Then we define $\widetilde{\mathcal{W}^{*}}$ in weighted space by
$$\widetilde{\mathcal{W}^{*}} A=\frac{-2 F \wedge d_{J}^{+}\left(e^{-\varphi} A\right)}{F^{2}} \cdot e^{\varphi} .$$

Step 2. Computing $\left\|\widetilde{\mathcal{W}}^{*} A\right\|_{H_{1}}^{2}+\left\|d_{J}^{-} A\right\|_{H_{3}}^{2}$, as $A \in D_{\widetilde{\mathcal{W}}^{*}} \cap D_{d_{J}^{-}} \cap \Omega_{\mathbb{R}}^{1}(\bar{\Omega})$ (for $\bar{\partial}$-operator cf. L. Hörmander [39]).

Using the second canonical connection $\nabla^{1}$ with respect to metric $g_{J}$ (cf. Appendix A. 1 or [28]), for $p \in \Omega$, choose a local moving unitary frame $\left\{e^{1}, e^{2}\right\}$ for $T^{1,0}(\Omega)$ and local complex coordinate $\left\{z^{1}, z^{2}\right\}$ in a neighborhood of $p$ satisfying $e^{i}(p)=\left.\frac{\partial}{\partial z^{i}}\right|_{p}$ with respect to the Hermitian inner product $h=g_{J}-\sqrt{-1} F$ (cf. [9]). Denote $\left\{\theta_{1}, \theta_{2}\right\}$ by the dual frame of $\left\{e^{1}, e^{2}\right\}$. Hence
$$h=g_{J}-\sqrt{-1} F=\theta_{1} \otimes \bar{\theta}_{1}+\theta_{2} \otimes \bar{\theta}_{2}$$
and
$$F=\theta_{1} \wedge \bar{\theta}_{1}+\theta_{2} \wedge \bar{\theta}_{2} .$$
By a direct calculation,
$$\begin{aligned}
d_{J}^{+}\left(e^{-\varphi} A\right) \wedge F & =\left[\partial_{J}\left(e^{-\varphi} u\right)+\bar{\partial}_{J}\left(e^{-\varphi} \bar{u}\right)\right] \wedge F \\
& =-e^{-\varphi}\left(\frac{\partial \varphi}{\partial z^{1}} \theta_{1}+\frac{\partial \varphi}{\partial z^{2}} \theta_{2}\right) \wedge\left(u^{1} \bar{\theta}_{1}+u^{2} \bar{\theta}_{2}\right) \wedge F+e^{-\varphi} \partial_{J}\left(u^{1} \bar{\theta}_{1}+u^{2} \bar{\theta}_{2}\right) \wedge F
\end{aligned}$$
$$\begin{aligned}
& +\bar{\partial}_{J}\left(e^{-\varphi} \bar{u}\right) \wedge F \\
= & -e^{-\varphi}\left(\frac{\partial \varphi}{\partial z^{1}} u^{1} \theta_{1} \wedge \bar{\theta}_{1}+\frac{\partial \varphi}{\partial z^{2}} u^{2} \theta_{2} \wedge \bar{\theta}_{2}\right) \wedge F \\
& +e^{-\varphi}\left(\frac{\partial u^{1}}{\partial z^{1}} \theta_{1} \wedge \bar{\theta}_{1}+\frac{\partial u^{2}}{\partial z^{2}} \theta_{2} \wedge \bar{\theta}_{2}\right) \wedge F+\bar{\partial}_{J}\left(e^{-\varphi} \bar{u}\right) \wedge F \\
= & -\frac{1}{2} e^{-\varphi}\left(\frac{\partial \varphi}{\partial z^{1}} u^{1}+\frac{\partial \varphi}{\partial z^{2}} u^{2}\right) F^{2}+\frac{1}{2} e^{-\varphi}\left(\frac{\partial u^{1}}{\partial z^{1}}+\frac{\partial u^{2}}{\partial z^{2}}\right) F^{2}+\bar{\partial}_{J}\left(e^{-\varphi} \bar{u}\right) \wedge F,
\end{aligned}$$
where $u=u^{1} \bar{\theta}_{1}+u^{2} \bar{\theta}_{2}, A=u+\bar{u}$. Thus, by (A.18) and (A.19),
$$\widetilde{\mathcal{W}}^{*} A=\frac{\partial \varphi}{\partial z^{1}} u^{1}+\frac{\partial \varphi}{\partial z^{2}} u^{2}-\frac{\partial u^{1}}{\partial z^{1}}-\frac{\partial u^{2}}{\partial z^{2}}+\frac{\partial \varphi}{\partial \bar{z}^{1}} \bar{u}^{1}+\frac{\partial \varphi}{\partial \bar{z}^{2}} \bar{u}^{2}-\frac{\partial \bar{u}^{1}}{\partial \bar{z}^{1}}-\frac{\partial \bar{u}^{2}}{\partial \bar{z}^{2}} .$$

Now computing
$$\left\|\widetilde{\mathcal{W}}^{*} A\right\|_{H_{1}}^{2}=\int_{\Omega}\left|\sum_{i} \delta_{i} u^{i}\right|^{2} e^{-\varphi}=\sum_{i, j} \int_{\Omega}\left(\delta_{i} u^{i}\right) \overline{\left(\delta_{j} u^{j}\right)} e^{-\varphi},$$
where $\delta_{i} u^{i}=\frac{\partial u^{i}}{\partial z^{i}}-\frac{\partial \varphi}{\partial z^{i}} u^{i}$.
$$\begin{aligned}
d_{J}^{-}(A)= & d_{J}^{-}(u+\bar{u}) \\
= & \bar{\partial}_{J} u+\bar{A}_{J} u+\partial_{J} \bar{u}+A_{J} \bar{u} \\
= & \left(\frac{\partial \bar{u}^{2}}{\partial z^{1}}-\frac{\partial \bar{u}^{1}}{\partial z^{2}}\right) \theta_{1} \wedge \theta_{2}+\left(\frac{\partial u^{2}}{\partial \bar{z}^{1}}-\frac{\partial u^{1}}{\partial \bar{z}^{2}}\right) \bar{\theta}_{1} \wedge \bar{\theta}_{2} \\
& +\left(A_{J 2} \bar{u}^{2}-A_{J 1} \bar{u}^{1}\right) \theta_{1} \wedge \theta_{2}+\left(\bar{A}_{J 2} u^{2}-\bar{A}_{J 1} u^{1}\right) \bar{\theta}_{1} \wedge \bar{\theta}_{2},
\end{aligned}$$
where $A_{J i}$ are the coefficients of $A_{J}$ which is the linear operator defined in Section 2. So
$$\begin{aligned}
\left\|d_{J}^{-} A\right\|_{H_{3}}^{2} & =\int_{\Omega} \sum_{i<j}\left(\left|\frac{\partial u^{j}}{\partial \bar{z}^{i}}-\frac{\partial u^{i}}{\partial \bar{z}^{j}}\right|^{2}+\left|A_{J j} \bar{u}^{j}-A_{J i} \bar{u}^{i}\right|^{2}\right) e^{-\varphi} \\
& =\sum_{i, j} \int_{\Omega}\left(\left|\frac{\partial u^{j}}{\partial \bar{z}^{i}}\right|^{2}-\frac{\partial u^{j}}{\partial \bar{z}^{i}} \frac{\partial \bar{u}^{i}}{\partial z^{j}}\right) e^{-\varphi}+\int_{\Omega} \sum_{i<j}\left|A_{J j} \bar{u}^{j}-A_{J i} \bar{u}^{i}\right|^{2} e^{-\varphi} .
\end{aligned}$$
Hence,
$$\begin{aligned}
\left\|\widetilde{\mathcal{W}}^{*} A\right\|_{H_{1}}^{2}+\left\|d_{J}^{-} A\right\|_{H_{3}}^{2}= & \sum_{i, j} \int_{\Omega}\left|\frac{\partial u^{j}}{\partial \bar{z}^{i}}\right|^{2} e^{-\varphi}+\int_{\Omega} \sum_{i<j}\left|A_{J j} \bar{u}^{j}-A_{J i} \bar{u}^{i}\right|^{2} e^{-\varphi} \\
& +\sum_{i, j} \int_{\Omega}\left(\left(\delta_{i} u^{i}\right) \overline{\left(\delta_{j} u^{j}\right)}-\frac{\partial u^{j}}{\partial \bar{z}^{i}} \frac{\partial \bar{u}^{i}}{\partial z^{j}}\right) e^{-\varphi} .
\end{aligned}$$

Before continuing discussing, we need a formula which is basically the divergence theorem.

Proposition A.27. (for $\bar{\partial}$ operator, see [39, ChapterII] [40, ChapterIV]) If the boundary $\partial \Omega=\{r=0\}$ of a bounded domain $\Omega=\{r<0\} \subset\left(\mathbb{R}^{4}, J\right)$ is differentiable, $|d r|=1$ on $\partial \Omega$ with respect to the metric $g_{J}$, and $L=\sum_{i} a_{i} \frac{\partial}{\partial x^{i}}$ is a differentiable operator of 1 -order with constant coefficients, then
$$\int_{\Omega} L f=\int_{\partial \Omega}(L r) f .$$

By the above proposition, we can get
$$\begin{aligned}
\sum \int_{\Omega} f \frac{\overline{\partial\left(u^{i} e^{-\varphi}\right)}}{\partial z^{i}} & =-\sum \int_{\Omega} \frac{\partial f}{\partial \bar{z}^{i}} \bar{u}^{i} e^{-\varphi}+\sum \int_{\Omega} \frac{\partial\left(f \bar{u}^{i} e^{-\varphi}\right)}{\partial \bar{z}^{i}} \\
& =-\sum \int_{\Omega} \frac{\partial f}{\partial \bar{z}^{i}} \bar{u}^{i} e^{-\varphi}+\sum \int_{\partial \Omega} \frac{\partial r}{\partial \bar{z}^{i}}\left(f \bar{u}^{i} e^{-\varphi}\right) .
\end{aligned}$$
We can reduce the deduced formula above to
$$\left(f, \delta_{i} g\right)=-\left(\bar{\partial}_{i} f, g\right)+\left(\left(\bar{\partial}_{i} r\right) f, g\right)_{\partial \Omega},$$
where $f, g \in C^{\infty}(\bar{\Omega})$, and $(\cdot, \cdot)_{\partial \Omega}$ indicates the integral on $\partial \Omega$ relative to the weight factor $e^{-\varphi}$. By (A.23),
$$\begin{aligned}
& \int_{\Omega}\left(\delta_{i} u^{i}\right) \overline{\left(\delta_{j} u^{j}\right)} e^{-\varphi}=-\left(\bar{\partial}_{j} \delta_{i} u^{i}, u^{j}\right)+\left(\left(\bar{\partial}_{j} r\right) \delta_{i} u^{i}, u^{j}\right)_{\partial \Omega}, \\
& \int_{\Omega}\left(\bar{\partial}_{i} u^{j}\right) \overline{\left(\bar{\partial}_{j} u^{i}\right)} e^{-\varphi}=-\left(u^{j}, \delta_{i} \bar{\partial}_{j} u^{i}\right)+\left(\left(\bar{\partial}_{i} r\right) u^{j}, \bar{\partial}_{j} u^{i}\right)_{\partial \Omega} .
\end{aligned}$$
Then,
$$\begin{aligned}
\left\|\widetilde{\mathcal{W}^{*}} A\right\|_{H_{1}}^{2}+\left\|d_{J}^{-} A\right\|_{H_{3}}^{2}= & \sum_{i, j} \int_{\Omega}\left|\frac{\partial u^{j}}{\partial \bar{z}^{i}}\right|^{2} e^{-\varphi}+\int_{\Omega} \sum_{i<j}\left|A_{J j} \bar{u}^{j}-A_{J i} \bar{u}^{i}\right|^{2} e^{-\varphi} \\
& +\sum_{i, j}\left(\left(\delta_{i} \bar{\partial}_{j}-\bar{\partial}_{j} \delta_{i}\right) u^{i}, u^{j}\right)+\sum_{i, j} \int_{\partial \Omega}\left(\bar{\partial}_{i} r\right)\left(\delta_{i} u^{j}\right) \bar{u}^{i} e^{-\varphi} \\
& -\sum_{i, j} \int_{\partial \Omega}\left(\partial_{i} r\right) \bar{u}^{j}\left(\overline{\partial_{j} \bar{u}^{i}}\right) e^{-\varphi} \\
= & \sum_{i, j} \int_{\Omega}\left|\frac{\partial u^{j}}{\partial \bar{z}^{i}}\right|^{2} e^{-\varphi}+\int_{\Omega} \sum_{i<j}\left|A_{J j} \bar{u}^{j}-A_{J i} \bar{u}^{i}\right|^{2} e^{-\varphi} \\
& +\sum_{i, j} \int_{\Omega}\left(\bar{\partial}_{j} \partial_{i} \varphi\right) u^{i} \bar{u}^{j} e^{-\varphi}+\sum_{j} \int_{\partial \Omega}\left(\delta_{i} u^{j}\right) \sum_{i}\left(\bar{\partial}_{i} r\right) \bar{u}^{i} e^{-\varphi} \\
& -\sum_{i, j} \int_{\partial \Omega}\left(\partial_{i} r\right) \bar{u}^{j}\left(\overline{\partial_{j} \bar{u}^{i}}\right) e^{-\varphi} .
\end{aligned}$$
If we add conditions
$$\left.\sum_{i}\left(\partial_{i} r\right) u^{i}\right|_{\partial \Omega}=0$$
to $A=u+\bar{u}$, then
$$\begin{aligned}
\left\|\widetilde{\mathcal{W}^{*}} A\right\|_{H_{1}}^{2}+\left\|d_{J}^{-} A\right\|_{H_{3}}^{2}= & \sum_{i, j} \int_{\Omega}\left|\frac{\partial u^{j}}{\partial \bar{z}^{i}}\right|^{2} e^{-\varphi}+\int_{\Omega} \sum_{i<j}\left|A_{J j} \bar{u}^{j}-A_{J i} \bar{u}^{i}\right|^{2} e^{-\varphi} \\
& +\sum_{i, j} \int_{\Omega}\left(\bar{\partial}_{j} \partial_{i} \varphi\right) u^{i} \bar{u}^{j} e^{-\varphi}-\sum_{i, j} \int_{\partial \Omega}\left(\partial_{i} r\right) \bar{u}^{j}\left(\overline{\partial_{j} \bar{u}^{i}}\right) e^{-\varphi} .
\end{aligned}$$

Step 3. The domination of the boundary term-Morrey's trick (cf. Morrey [61] or Hörmander [39, Chapter II]).

The method is: Let $A \in D_{\widetilde{\mathcal{W}}^{*}} \cap \Omega_{\mathbb{R}}^{1}(\bar{\Omega}), r=0$ define the boundary of $\Omega$, and the defining function $r$ be differentiable. Thus $\sum_{i}\left(\partial_{i} r\right) u^{i}$ are local functions, differentiable at every point. By (A.25), these functions vanish at $r=0$, i.e. on $\partial \Omega$. By Taylor expansion, it can be written as
$$\sum_{i}\left(\partial_{i} r\right) u^{i}=\lambda r$$
where $\lambda$ is some differentiable function. Taking $\bar{\partial}_{j}$ to both sides to yield
$$\sum_{i}\left(\bar{\partial}_{j} \partial_{i} r\right) u^{i}+\sum_{i}\left(\partial_{i} r\right)\left(\bar{\partial}_{j} u^{i}\right)=\left(\bar{\partial}_{j} \lambda\right) r+\lambda \bar{\partial}_{j} r .$$
Multiplying $\bar{u}^{j}$ and summing up for $j$,
$$\sum_{i, j}\left(\bar{\partial}_{j} \partial_{i} r\right) u^{i} \bar{u}^{j}+\sum_{i, j}\left(\partial_{i} r\right)\left(\bar{\partial}_{j} u^{i}\right) \bar{u}^{j}=\sum_{j} r\left(\bar{\partial}_{j} \lambda\right) \bar{u}^{j}+\sum_{j} \lambda\left(\bar{\partial}_{j} r\right) \bar{u}^{j} .$$
Integrating on $\partial \Omega$, noting $r=0$ on $\partial \Omega,\left.\sum_{i}\left(\partial_{i} r\right) u^{i}\right|_{\partial \Omega}=0$, to get
$$-\sum_{i, j} \int_{\partial \Omega}\left(\partial_{i} r\right)\left(\bar{\partial}_{j} u^{i}\right) \bar{u}^{j} e^{-\varphi}=\sum_{i, j} \int_{\partial \Omega}\left(\bar{\partial}_{j} \partial_{i} r\right) u^{i} \bar{u}^{j} e^{-\varphi} .$$
Then we get
$$\begin{aligned}
\left\|\widetilde{\mathcal{W}^{*}} A\right\|_{H_{1}}^{2}+\left\|d_{J}^{-} A\right\|_{H_{3}}^{2}= & \sum_{i, j} \int_{\Omega}\left|\frac{\partial u^{j}}{\partial \bar{z}^{i}}\right|^{2} e^{-\varphi}+\int_{\Omega} \sum_{i<j}\left|A_{J j} \bar{u}^{j}-A_{J i} \bar{u}^{i}\right|^{2} e^{-\varphi} \\
& +\sum_{i, j} \int_{\Omega}\left(\bar{\partial}_{j} \partial_{i} \varphi\right) u^{i} \bar{u}^{j} e^{-\varphi} \\
& +\sum_{i, j} \int_{\partial \Omega}\left(\bar{\partial}_{j} \partial_{i} r\right) u^{i} \bar{u}^{j} e^{-\varphi} .
\end{aligned}$$
Note that we have not made any special restrictions to the choice of $\varphi$ so far. Now we assume
(1) $\Omega$ is a compact $J$-pseudoconvex domain, i.e.
$$\sum_{i, j}\left(\bar{\partial}_{j} \partial_{i} r\right) \xi^{i} \bar{\xi}^{j} \geq 0, \quad \forall \sum_{i}\left(\partial_{i} r\right) \xi^{i}=0 ;$$
(2) $\varphi$ satisfies that complex Hessian is strictly positive-definite (i.e. $\varphi$ is a strictly $J$-plurisubharmonic function (cf. Harvey-Lawson [37] or Appendix A.1)), that is, there exists $c>0$ such that
$$\sum_{i, j}\left(\partial_{i} \bar{\partial}_{j} \varphi\right) \xi^{i} \bar{\xi}^{j} \geq c \sum_{i}\left|\xi^{i}\right|^{2} .$$
Under the two assumptions above, we have proved the following theorem:
Proposition A.28. (for $\bar{\partial}$-problem see [39, 40]) Let $\Omega$ be a compact $J$-pseudoconvex domain. Given a real valued function $\varphi \in C^{\infty}(\bar{\Omega})$ satisfying $\sum_{i, j}\left(\partial_{i} \bar{\partial}_{j} \varphi\right) \xi^{i} \bar{\xi}^{j} \geq c \sum_{i}\left|\xi^{i}\right|^{2}$, $c>0$, then for $A \in D_{\widetilde{\mathcal{W}}^{*}} \cap D_{d_{J}^{-}} \cap \Omega_{\mathbb{R}}^{1}(\bar{\Omega})$, we have
$$c\|A\|_{H_{2}}^{2} \leq\left\|\widetilde{\mathcal{W}}^{*} A\right\|_{H_{1}}^{2}+\left\|d_{J}^{-} A\right\|_{H_{3}}^{2} .$$

Recall that in the previous discussion, if for all $A \in D_{\widetilde{\mathcal{W}}^{*}} \cap D_{d_{J}^{-}}$, we have
$$c\|A\|_{H_{2}}^{2} \leq\left\|\widetilde{\mathcal{W}}^{*} A\right\|_{H_{1}}^{2}+\left\|d_{J}^{-} A\right\|_{H_{3}}^{2},$$
then the $\widetilde{\mathcal{W}}, d_{J}^{-}$-problem of a $J$-pseudoconvex domain has a solution (which is similar to the $\bar{\partial}$-problem in [39,40]). However, Proposition A. 28 implies that
$$c\|A\|_{H_{2}}^{2} \leq\left\|\widetilde{\mathcal{W}}^{*} A\right\|_{H_{1}}^{2}+\left\|d_{J}^{-} A\right\|_{H_{3}}^{2}$$
holds for all infinitely differentiable functions in $D_{\widetilde{\mathcal{W}}^{*}} \cap D_{d_{J}^{-}}$. To prove that this estimate holds for all $A$ in $D_{\widetilde{\mathcal{W}}^{*}} \cap D_{d_{J}^{-}}$, it suffices to show that, $\forall A \in D_{\widetilde{\mathcal{W}}^{*}} \cap D_{d_{J}^{-}}$there exists a sequence $A_{\nu} \in D_{\widetilde{\mathcal{W}}^{*}} \cap D_{d_{J}^{-}} \cap \Omega_{\mathbb{R}}^{1}(\bar{\Omega})$ such that
$$A_{\nu} \rightarrow A, \widetilde{\mathcal{W}}^{*} A_{\nu} \rightarrow \widetilde{\mathcal{W}}^{*} A, d_{J}^{-} A_{\nu} \rightarrow d_{J}^{-} A .$$
Note that it is important to prove that this convergence holds at the same time. It is easy to prove that the first and the third hold. The question becomes to show that the second holds at the same time. The method presented below is called the regularization method of K. Friedrichs, first due to K. Friedrichs [26] in 1944, and later further developed by L. Hörmander [39] in 1965.

Let a domain $\Omega \subset \mathbb{R}^{n}, L$ be a linear differential operator
$$L: C^{\infty}(\bar{\Omega}) \longrightarrow C^{\infty}(\bar{\Omega}) .$$
We want to extend $L$ to $L_{1}$,
$$L_{1}: L^{2}(\Omega) \longrightarrow L^{2}(\Omega) .$$
There are two ways to do the extension (cf. L. Hörmander [39, 40]):
1. The strict extension. $L_{1}$ is the closed extension of $L$, that is, $L_{1}=\bar{L}$. The definition is : $L_{1} f=g$ is equivalent to that there exists $f_{\nu} \in C^{\infty}(\bar{\Omega})$ such that $f_{\nu} \rightarrow f, L f_{\nu} \rightarrow g$ (the convergence in the sense of $L^{2}$ ).
2. The weak extension. The extension is in the sense of distributions, i.e. as $f, g \in L^{2}$. The definition of $L f=g$ is:
$$(g, \varphi)=\left(f, L^{*} \varphi\right)$$
to every $\varphi \in C^{\infty}(\Omega)_{0}$.
Theorem A.29. (Friedrichs ) If $L$ is a differential operator of first-order, the weak extension is equivalent to the strict extension (that is, the weak extension implies the strict extension).

Remark A.30. It is enough to require that $\varphi$ is a strictly $J$-plurisubharmonic function. If $J$ is integrable, then $\widetilde{\mathcal{W}}, d_{J}^{-}$-problem becomes $\bar{\partial}$-problem, hence Proposition 4.28 is a generalization of Theorem 4.2.2 in [40].

Now we return to prove the iequality
$$c\|A\|_{H_{2}}^{2} \leq\left\|\widetilde{\mathcal{W}}^{*} A\right\|_{H_{1}}^{2}+\left\|d_{J}^{-} A\right\|_{H_{3}}^{2}, A \in D_{\widetilde{W}^{*}} \cap D_{d_{J}^{-}} .$$

We have proved the case for $A \in \Omega_{\mathbb{R}}^{1}(\bar{\Omega})$. For $A \in D_{\widetilde{W}^{*}} \cap D_{d_{J}^{-}}$, we need to find $A_{\nu} \in \Omega_{\mathbb{R}}^{1}(\bar{\Omega})$ so that
$$A_{\nu} \rightarrow A, \widetilde{\mathcal{W}}^{*} A_{\nu} \rightarrow \widetilde{\mathcal{W}}^{*} A, d_{J}^{-} A_{\nu} \rightarrow d_{J}^{-} A .$$
We can do that by using the smoothing method of K. Friedrichs. Since $A \in D_{\widetilde{W}^{*}} \cap D_{d_{J}^{-}}$, $\widetilde{\mathcal{W}^{*}} A$ and $d_{J}^{-} A$ exists. Note by the definition of $\widetilde{\mathcal{W}^{*}}, \widetilde{\mathcal{W}^{*}} A=f$ is in the sense of weak extension, and $d_{J}^{-}$is a closed operator, $d_{J}^{-} A$ is in the sense of strict extension. Obviously, sttict extension implies weak one, so, in the sense of distributions ( recall (A.20)-(A.21)), we have
$$\widetilde{\mathcal{W}}^{*} A=\frac{\partial \varphi}{\partial z^{1}} u^{1}+\frac{\partial \varphi}{\partial z^{2}} u^{2}+\frac{\partial \varphi}{\partial \bar{z}^{1}} \bar{u}^{1}+\frac{\partial \varphi}{\partial \bar{z}^{2}} \bar{u}^{2}-\frac{\partial u^{1}}{\partial z^{1}}-\frac{\partial u^{2}}{\partial z^{2}}-\frac{\partial \bar{u}^{1}}{\partial \bar{z}^{1}}-\frac{\partial \bar{u}^{2}}{\partial \bar{z}^{2}},$$
where $A=u+\bar{u}, u=u^{1} \bar{\theta}_{1}+u^{2} \bar{\theta}_{2} \in \Omega_{J}^{0,1}(\bar{\Omega}),\left\{\theta_{1}, \theta_{2}\right\}$ is the dual frame of the local moving unitary frame $\left\{e^{1}, e^{2}\right\}$ for $T^{1,0}(\bar{\Omega})$;
$$\begin{aligned}
d_{J}^{-} A & =\left(\frac{\partial \bar{u}^{2}}{\partial z^{1}}-\frac{\partial \bar{u}^{1}}{\partial z^{2}}\right) \theta_{1} \wedge \theta_{2}+\left(\frac{\partial u^{2}}{\partial \bar{z}^{1}}-\frac{\partial u^{1}}{\partial \bar{z}^{2}}\right) \bar{\theta}_{1} \wedge \bar{\theta}_{2} \\
& +\left(A_{J_{2}} \bar{u}^{2}-A_{J_{1}} \bar{u}^{1}\right) \theta_{1} \wedge \theta_{2}+\left(\bar{A}_{J_{2}} u^{2}-\bar{A}_{J_{1}} u^{1}\right) \bar{\theta}_{1} \wedge \bar{\theta}_{2},
\end{aligned}$$
where
$$A_{J}: \Omega_{J}^{1,0}(\bar{\Omega})-\Omega_{J}^{0,2}(\bar{\Omega}), \bar{A}_{J}: \Omega_{J}^{0,1}(\bar{\Omega})-\Omega_{J}^{2,0}(\bar{\Omega}),$$
are linear operators depending on $J$ (if $J$ is integrable, $A_{J}=0=\bar{A}_{J}$ ), $A_{J_{i}}, i=1,2$, are the coefficients of $A_{J}$ (more details, see Section 2). There are linear differential equations of first order. By the smoothing method of Friedrichs (Friedrichs theorem holds for first-order differential operator), setting $A_{\varepsilon}=A * \chi_{\varepsilon}$ (where $A * \chi_{\varepsilon}$ is the convolution of $A$ with respect to mean value function $\chi_{\varepsilon}$, cf. [39, 40]), then
$$\widetilde{\mathcal{W}}^{*} A_{\varepsilon} \rightarrow \widetilde{\mathcal{W}}^{*} A, d_{J}^{-} A_{\varepsilon} \rightarrow d_{J}^{-} A, A_{\varepsilon} \rightarrow A .$$
Note that $A_{\varepsilon}$ which is obtained by quoting Friedrichs regularization method directly, is contained in $\Omega_{\mathbb{R}}^{1}(\bar{\Omega})$. However, it is not clear whether it is in $D_{\widetilde{\mathcal{W}}^{*}}$, since that $A_{\varepsilon} \in$ $D_{\widetilde{\mathcal{W}}^{*}} \cap \Omega_{\mathbb{R}}^{1}(\bar{\Omega})$ has to satisfy the boundary condition (cf. (A.25)):
$$\left.\sum_{i=1}^{2}\left(\partial_{i} r\right) u_{\varepsilon}^{i}\right|_{\partial \Omega}=0, \quad A_{\varepsilon}=u_{\varepsilon}+\bar{u}_{\varepsilon} .$$

How do all $A_{\varepsilon}$ satisfy (A.29) at the same time? In 1965, L. Hörmander [40] further extended Friedrichs regularization method to satisfy the given boundary conditions.

Assume $\Omega=\{r<0\} \subset \mathbb{R}^{N}$, we consider differential equations system (in the sense of distribution) on $\Omega$ :
$$\sum_{i=1}^{N} \sum_{j=1}^{I} b_{i j}^{k} D_{i} u_{j}+\sum_{j=1}^{I} c_{j}^{k} u_{j}=f_{k}, \quad 1 \leq k \leq I,$$
where $D_{i}=\frac{\partial}{\partial x_{i}}, i=1, \cdots, N, b_{i j}^{k}, c_{j}^{k} \in C^{\infty}(\bar{\Omega})$. We write them in a matrix form:
$$B u+C u=f$$
where $u=\left(u_{1}, \cdots, u_{I}\right)^{T}, f=\left(f_{1}, \cdots, f_{I}\right)^{T}$. The actual situation over here is
$$f=\binom{T^{*} u}{S^{*} u}$$
We set the former $K^{0}$ equations of (A.30) by
$$B^{0} u+C^{0} u=f^{0} .$$

Next we see how to describe the boundary conditions. For $u \in L^{2}(\Omega)$, we denote its null extension by $\tilde{u}$
$$\begin{aligned}
u & \rightarrow \tilde{u} \in L^{2}\left(\mathbb{R}^{N}\right), \\
\tilde{u}(x)= & \begin{cases}u(x), & x \in \Omega, \\
0, & x \in \mathbb{R}^{N} \backslash \Omega .\end{cases}
\end{aligned}$$
We know that $u \in D_{T^{*}} \Leftrightarrow(T \varphi, u)=\left(\varphi, T^{*} u\right), \forall \varphi \in D_{T}$. That is
$$\int_{\Omega}(T \varphi) u=\int_{\Omega} \varphi\left(T^{*} u\right) .$$
In particular, it is true for a $C^{\infty}$ function $\varphi$ with a compact support in $\mathbb{R}^{N}$, but
$$\int_{\Omega}(T \varphi) u=\int_{\Omega} \varphi\left(T^{*} u\right)=\int_{\mathbb{R}^{N}} \varphi \widetilde{\varphi\left(T^{*} u\right)},$$
while
$$\int_{\Omega}(T \varphi) u=\int_{\mathbb{R}^{N}}(T \varphi) \tilde{u},$$
so
$$\int_{\mathbb{R}^{N}}(T \varphi) \tilde{u}=\int_{\mathbb{R}^{N}} \varphi \widetilde{\varphi\left(T^{*} u\right)} .$$
It is true for each $C^{\infty}$ function $\varphi$ with its support in $\mathbb{R}^{N}$, thus
$$T^{*} \tilde{u}=\widetilde{\left(T^{*} u\right)} .$$
So we consider that the equations and their boundary conditions are
$$\left\{\begin{array}{l}
(B+C) u=f, \\
\left(B^{0}+C^{0}\right) \tilde{u}=\tilde{f}^{0} .
\end{array}\right.$$
We have the following Friedrichs-Hörmander Theorem (cf. L. Hörmander 40, Proposition $1.2 .4]$ ): Let $u, f \in L^{2}(\Omega)$ satisfy (in the sense of distributions) equations
$$\tilde{u}(x)= \begin{cases}(B+C) u=f, & B=\binom{B^{0}}{*}_{K \times I}, C=\binom{C^{0}}{*}_{K \times I}, \\ \left(B^{0}+C^{0}\right) \tilde{u}=\tilde{f}^{0}, & f=\binom{f^{0}}{*}_{I \times 1},\end{cases}$$
where $\Omega=\{r<0\} \subset \subset \mathbb{R}^{N}$. If the ranks of $B^{0}(r)$ at each point in $\partial \Omega$ are constants, there is a sequence of $u_{\nu} \in C^{\infty}(\Omega)$ such that
$$\left\{\begin{array}{l}
u_{\nu} \rightarrow u ; \\
B u_{\nu}+C u_{\nu} \rightarrow f ; \\
B^{0} \tilde{u}_{\nu}+C^{0} \tilde{u}_{\nu} \rightarrow B^{0} \widetilde{u_{\nu}+C^{0}} u_{\nu} .
\end{array}\right.$$

Now we return to $\widetilde{\mathcal{W}}, d_{J}^{-}$-problem. In our discussed situations, $\Omega=\{r<1\} \subset \subset \mathbb{R}^{4}$, $T^{*}=\widetilde{\mathcal{W}^{*}}, S=d_{J}^{-}$. For $A \in D_{\widetilde{\mathcal{W}}^{*}} \cap D_{d_{J}^{-}}$,
$$f=\binom{\widetilde{\mathcal{W}}^{*} A}{d_{J}^{-} A} .$$
In terms of local moving unitary dual frame $\left\{\theta_{1}, \theta_{2}\right\}$,
$$A=u+\bar{u}=u^{1} \bar{\theta}_{1}+u^{2} \bar{\theta}_{2}+\bar{u}^{1} \theta_{1}+\bar{u}^{2} \theta_{2} .$$
By (A.27) and (A.28)
$$\begin{aligned}
\widetilde{\mathcal{W}^{*} A}=\frac{\partial \varphi}{\partial z^{1}} u^{1} & +\frac{\partial \varphi}{\partial z^{2}} u^{2}+\frac{\partial \varphi}{\partial \bar{z}^{1}} \bar{u}^{1}+\frac{\partial \varphi}{\partial \bar{z}^{2}} \bar{u}^{2}-\frac{\partial u^{1}}{\partial z^{1}}-\frac{\partial u^{2}}{\partial z^{2}}-\frac{\partial \bar{u}^{1}}{\partial \bar{z}^{1}}-\frac{\partial \bar{u}^{2}}{\partial \bar{z}^{2}}, \\
d_{J}^{-} A & =\left(\frac{\partial \bar{u}^{2}}{\partial z^{1}}-\frac{\partial \bar{u}^{1}}{\partial z^{2}}\right) \theta_{1} \wedge \theta_{2}+\left(\frac{\partial u^{2}}{\partial \bar{z}^{1}}-\frac{\partial u^{1}}{\partial \bar{z}^{2}}\right) \bar{\theta}_{1} \wedge \bar{\theta}_{2} \\
& +\left(A_{J_{2}} \bar{u}^{2}-A_{J_{1}} \bar{u}^{1}\right) \theta_{1} \wedge \theta_{2}+\left(\bar{A}_{J_{2}} u^{2}-\bar{A}_{J_{1}} u^{1}\right) \bar{\theta}_{1} \wedge \bar{\theta}_{2}
\end{aligned}$$
The 1 -form $A$ can be written as a vector: $A_{1}=\left(u^{1}, u^{2}, \bar{u}^{1}, \bar{u}^{2}\right)^{T}$. Hence we have a matrix equation
$$f_{1}=\binom{B^{0} A_{1}+C^{0} A_{1}}{D A_{1}+E A_{1}},$$
which is equivalent to
$$f=\binom{\widetilde{\mathcal{W}}^{*} A}{d_{J}^{-} A} .$$
It is easy to see that
$$\begin{gathered}
B^{0}=\left(-\frac{\partial}{\partial z^{1}}-\frac{\partial}{\partial z^{2}}-\frac{\partial}{\partial \bar{z}^{1}}-\frac{\partial}{\partial \bar{z}^{2}}\right) \\
C^{0}=\left(\frac{\partial \varphi}{\partial z^{1}} \frac{\partial \varphi}{\partial z^{2}} \frac{\partial \varphi}{\partial \bar{z}^{1}} \frac{\partial \varphi}{\partial \bar{z}^{2}}\right), K^{0}=1, \\
D=\left(\begin{array}{cccc}
0 & 0 & -\frac{\partial}{\partial z_{2}} & \frac{\partial}{\partial z_{1}} \\
-\frac{\partial}{\partial \bar{z}_{2}} & \frac{\partial}{\partial \bar{z}_{1}} & 0 & 0
\end{array}\right), E=\left(\begin{array}{cccc}
0 & 0 & -A_{J_{1}} & A_{J_{2}} \\
-\bar{A}_{J_{1}} & \bar{A}_{J_{2}} & 0 & 0
\end{array}\right) .
\end{gathered}$$

By Friedrichs-Hörmander Theorem, having proved that for a $J$-pseudoconvex domain $\Omega$ in a tamed almost complex 4-manifold $(M, J)$, if $\varphi \in C^{\infty}(\bar{\Omega})$ satisfies
$$\sum_{i, j}\left(\partial_{i} \bar{\partial}_{j} \varphi\right) \xi^{i} \bar{\xi}^{j} \geq c \sum_{i}\left|\xi^{i}\right|^{2}, c>0$$
then for $A \in D_{\widetilde{\mathcal{W}}^{*}} \cap D_{d_{J}^{-}}$, we have
$$c\|A\|_{H_{2}}^{2} \leq\left\|\widetilde{\mathcal{W}}^{*} A\right\|_{H_{1}}^{2}+\left\|d_{J}^{-} A\right\|_{H_{3}}^{2} .$$
Combining the former part of this subsection, we solved the $\widetilde{\mathcal{W}}, d_{J}^{-}$-problem (as the $\bar{\partial}$ -problem in classical complex analysis) of $J$-pseudoconvex domain in the sense of distribution (for $\bar{\partial}$-problem see [39,40]).

Theorem A.31. Let $\Omega$ be a compact $J$-pseudoconvex domain in a tamed almost complex 4-manifold. Given a real valued function $\varphi \in C^{\infty}(\bar{\Omega})$ satisfies
$$\sum_{i, j}\left(\partial_{i} \bar{\partial}_{j} \varphi\right) \xi^{i} \bar{\xi}^{j} \geq c \sum_{i}\left|\xi^{i}\right|^{2}, c>0$$
then for all $A \in \Lambda_{\mathbb{R}}^{1} \otimes L_{1}^{2}(\Omega, \varphi)$ and satisfy $d_{J}^{-}(A)=0$, then there exists $f \in L_{2}^{2}(\Omega, \varphi)_{0}$ such that
$$\widetilde{\mathcal{W}}(f)=A, \quad\|f\|_{H_{1}} \leq \frac{1}{\sqrt{c}}\|A\|_{H_{2}} .$$

Remark A.32. 1. As in classical complex analysis, there is the regularity properties of the solution, i.e., when $A$ has enough differentiability, the solution $f$ to $\widetilde{\mathcal{W}}(f)=A$ must have appropriate differentiability (for $\bar{\partial}$-problem, see J. J. Kohn [51, 52]). A stronger result is: For a strictly pseudoconvex domain $\Omega, \widetilde{\mathcal{W}}(f)=A$. If $A \in \Omega_{\mathbb{R}}^{1}(\bar{\Omega})$, then $f \in C^{\infty}(\bar{\Omega})$.
2. It is well known that $\bar{\partial}$-problem in classical complex analysis is for any dimension. It is natural to ask that could we consider $\widetilde{\mathcal{W}}, d_{J}^{-}$-problem for higher dimensional almost Kähler manifolds.

\section*{A. 4 The singularities of $J$-plurisubharmonic functions on tamed almost complex 4-manifolds}

The goal of this subsection is to study singularities of $J$-plurisubharmonic functions on tamed almost complex 4-manifolds as in classical complex analysis. F. Elkhadhra had the following result (cf. [23, Proposition 1]):

Let $\Omega$ be an open set of $\mathbb{R}^{2 n}$ equipped with an almost complex structure $J$ of class $C^{1}$. Let $N$ be a $C^{2}$ submanifold of codimension $2 k$ such that $J(T N)=T N$. Then for every $x_{0} \in N$ there exists an open neighborhood $U$ of $x_{0}$ and functions $f_{1}, \cdots, f_{k}$ of class $C^{2}$ on $U$ such that
$$\begin{gathered}
N \cap U=\left\{x \in U \mid f_{1}(x)=\cdots=f_{k}(x)=0, \quad \bar{\partial}_{J} f_{j}=0\right. \\
\text { on } \left.N \cap U, \text { and } \partial_{J} f_{1} \wedge \cdots \wedge \partial_{J} f_{k} \neq 0 \text { on } U\right\} .
\end{gathered}$$
Moreover there exists a $J$-plurisubharmonic function $u$ on $U$ of class $C^{2}$ on $U \backslash N$ such that $N \cap U=\{u=-\infty\}$.

In fact, if $(M, J)$ is an almost complex manifold, and $f$ a $J$-holomorphic function at some point $p \in M$. Then, for all vector fields $X, Y, d f\left(\mathcal{N}_{J}(X, Y)\right)=0$ at $p$, where $\mathcal{N}_{J}$ is the Nijenhuis tensor (cf. Lemma 3.2 in Wang-Zhu [79]). Note that if there exist $n J$ -holomorphic functions on a real $2 n$-dimensional almost Hermitian manifold $(M, g, J)$ which are independent at some point $p \in M$, then the Nijenhuis tensor $\mathcal{N}_{J}$ identically vanishes
at $p$. This means that an integrable complex structure is one with many holomorphic functions. It is a hard theorem (Newlander-Nirenberg integrability theorem for almost complex structures) that the converse is also true. In general, an almost complex manifold has no holomorphic functions at all. On the other hand, it has a lot of $J$-holomorphic curves (i.e., maps $u: \mathbb{C} \rightarrow(M, g, J)$ such that $d f \circ i=J \circ d f$ ) (cf. M. Gromov [32]).

As done in Theorems 4.4.2-4.4.5 of L. Hörmander [40], we study a $J$-plurisubharmonic function $\varphi$ which is not identically $-\infty$ on a connected $J$-pseudoconvex open set $\Omega$, then $e^{-\varphi}$ is locally integrable in a dense open subset of $\Omega$. Therefore we have the following theorem:

Theorem A.33. Suppose that $(M, J)$ is an almost complex 4-manifold which is tamed by symplectic form $\omega_{1}=F+d_{J}^{-}(v+\bar{v})$, where $F$ is the fundamental 2-form on $M . g_{J}(\cdot, \cdot):=$ $F(\cdot, J \cdot)$ is an almost Hermitian metric on $M$. Let $\varphi$ be a strictly $J$-plurisubharmonic function on a $J$-pseudoconvex open set $\Omega \subset M$. If $p \in \Omega$, there exists a neighborhood of $p$ such that the set of points of which $e^{-\varphi}$ is not integrable in this neighborhood is a $J$-analytic subset of $\Omega$ of dimension (complex) $\leq 1$.

Remark A.34. According to Gromov's fundamental theory of J-holomorphic curves [32], almost complex submanifolds of complex dimension one always exist locally in a given almost complex manifold (there are no local obstructions). These curves can be realized globally as images of Riemann surfaces under J-holomorphic maps. In higher dimension, even through the existence of almost submanifolds can be obstructed. Donaldson [15] has shown that every compact symplectic manifold admits symplectic submanifolds which is done by approximating a compatible almost complex structure. It is natural to ask the following question: Could one generalize Theorem A. 33 to higher dimensional symplectic manifolds for closed positive $(1,1)$-currents or $(n-1, n-1)$-currents $(n>2)$.

Proof of Theorem A.33: Since any almost complex 4-manifold has the local symplectic property (cf. [54]), there exists an open set $U_{p} \subset \Omega$ and a symplectic form $\omega_{p}$ on $U_{p}$ such that $\left.F\right|_{p}=\left.\omega_{p}\right|_{p}$. Hence we choose a Darboux coordinate chart
$$\left\{\left(z_{1}, z_{2}\right) \mid z_{1}(p)=z_{2}(p)=0\right\}$$
for the symplectic form $\omega_{p}$. Without loss of generality, we may assume that $U_{p}$ is the Darboux coordinate chart (see [2]). Let
$$g_{J}^{\prime}(\cdot, \cdot):=\omega_{p}(\cdot, J \cdot), g_{0}(\cdot, \cdot):=\omega_{p}\left(\cdot, J_{s t} \cdot\right),$$
then $g_{J}^{\prime}(p)=g_{0}(p)=g_{J}(p)$. Since
$$d d_{J_{s t}}^{c}\left(\left|z_{1}\right|^{2}+\left|z_{2}\right|^{2}\right)=2 \sqrt{-1}\left(d z_{1} \wedge d \bar{z}_{1}+d z_{2} \wedge d \bar{z}_{2}\right),$$
$\left|z_{1}\right|^{2}+\left|z_{2}\right|^{2}$ is a strictly plurisubharmonic function in classical sense on the Darboux coordinate chart. Let
$$B_{r}(p):=\left\{\left|z_{1}\right|^{2}+\left|z_{2}\right|^{2}<r\right\} \subset U_{p}$$
and $B_{r}(p)$ is a strictly pseudoconvex domain. $\left\|J-J_{s t}\right\|$ is small on $B_{r}(p)$ when $r$ is small enough (cf. [14,15,37,74]). Indeed, we can get
$$\left.g_{J}^{\prime}\right|_{B_{r}(p)}=\left.g_{0}\right|_{B_{r}(p)} \cdot e^{h}$$
where $h$ is a symmetric $J$-anti-invariant $(2,0)$ tensor (cf. Kim [44], also see Tan-Wang-Zhou [74]) and $g_{0} e^{h}$ is defined by $g_{0} e^{h}(X, Y)=g_{0}\left(X, e^{g_{J}^{\prime-1}} h Y\right)$. Here $g_{J}^{\prime-1} h$ is the lifted $(1,1)$ tensor of $h$ with respect to $g_{J}^{\prime}$ and $e^{g_{J}^{\prime-1} h}$ is identity at point $p$. Hence, when $r$ is small enough, $\varphi+\log \left(1+|z|^{2}\right)^{2}$ is a strictly plurisubharmonic function in classical sense on $B_{r}(p)$. Without loss of generality, we may assume that $r=1$.

To complete the proof of Theorem A.33, we need the following propositions:
Proposition A.35. (cf. Hörmander [40, Theorem 4.4.3]) Let $\psi$ be a plurisubharmonic function in classical sense on $B_{1}(p)$ such that
$$\left|\psi(z)-\psi\left(z^{\prime}\right)\right|<c, \quad z, z^{\prime} \in B_{1}(p)$$
for some constant $c$. Let $V$ be a complex linear subspace of $\mathbb{C}^{2}$ of codimension $k, k=0,1,2$. For every holomorphic function $g$ on $V \cap B_{1}(p)$ such that
$$\int_{V \cap B_{1}(p)}|g|^{2} e^{-\psi} d \lambda<\infty,$$
where $d \lambda$ denotes the volume form of $V$, there exists a holomorphic function $f$ on $B_{1}(p)$ such that $\left.f\right|_{V \cap B_{1}(p)}=g$ and
$$\int_{B_{1}(p)}|f|^{2} e^{-\psi}\left(1+|z|^{2}\right)^{-3 k} d \mu_{g_{J}^{\prime}} \leq 9^{k} \pi^{k} e^{k c} \int_{V \cap B_{1}(p)}|g|^{2} e^{-\psi} d \lambda .$$
Note that $d \mu_{g_{J}^{\prime}}=d \mu_{g_{0}}=\omega_{p}^{2} / 2$ is the volume form on $B_{1}(p)$ since $J$ and $J_{\text {st }}$ are $\omega_{p}$ -compatible; and on $B_{1}(p)$, for any $q \in B_{1}(p), F(q)=L_{p}(q) \omega_{p}(q)$, where $L_{p}(q)$ is a positive function on $B_{1}(p), L_{p}(p)=1$.

By Proposition A.35, we have the following proposition:
Proposition A.36. (cf. Hörmander [40, Theorem 4.4.4]) Let $\psi$ be a plurisubharmonic function in classical sense on $B_{1}(p)$. If $z^{0} \in B_{1}(p)$ and $e^{-\psi}$ is integrable in a neighborhood of $z^{0}$ one can find a holomorphic function $f$ in $B_{1}(p)$ such that $f\left(z^{0}\right)=1$ and
$$\int_{B_{1}(p)}|f(z)|^{2} e^{-\psi}\left(1+|z|^{2}\right)^{-6} d \mu_{g_{J}^{\prime}}<\infty .$$

Let $\left(\Sigma, j_{\Sigma}\right)$ be a compact Riemann surface. A smooth map $u:\left(\Sigma, j_{\Sigma}\right) \rightarrow(M, J)$ is called a $J$-holomorphic curve if the differential $d u$ is a complex linear map with respect to $j_{\Sigma}$ and $J$ :
$$J \circ d u=d u \circ j_{\Sigma} .$$
Hence
$$\bar{\partial}_{J} u(X)=\frac{1}{2}\left[d u(X)+J(u) d u\left(j_{\Sigma} X\right)\right]=0$$
if $u$ is a $J$-holomorphic curve. Recall that the energy of a smooth map $u: \Sigma \longrightarrow$ $\left(B_{1}(p), g_{J}^{\prime}, J\right)$ is defined as the $L^{2}$-norm of the 1-form $d u \in \Omega^{1}\left(\Sigma, u^{*} T M\right)$ :
$$E_{J}(u):=\frac{1}{2} \int_{\Sigma}|d u|_{J}^{2} d v o l_{\Sigma} .$$
Here the norm of the (real) linear map
$$L:=d u(z): T_{z} \Sigma \rightarrow T_{u(z)} B_{1}(p)$$
is defined by
$$|L|_{J}:=\left.\xi\right|^{-1} \sqrt{|L(\xi)|_{J}^{2}+\left|L\left(j_{\Sigma} \xi\right)\right|_{J}^{2}}$$
for $0 \neq \xi \in T_{z} \Sigma$, where $|L(\xi)|_{J}^{2}=g_{J}^{\prime}(\xi, \xi)$. By Lemma 2.2.1 in McDuff-Salamon [60],
$$E_{J}(u)=\int_{\Sigma}\left|\bar{\partial}_{J} u\right|_{J}^{2} d v o l_{\Sigma}+\int_{\Sigma} u^{*} \omega_{p} .$$
Hence a $J$-holomorphic curve $u: \Sigma \longrightarrow\left(B_{1}(p), g_{J}^{\prime}, J\right)$ is a minimal surface with respect to the metric $g_{J}^{\prime}$. Note that a smooth map $u: \Sigma \longrightarrow(M, g, J)$ (an almost Hermitian manifold) is a $J$-holomorphic curve if and only if it is conformal with respect to $g$, i.e. its differential preserves angles or, equivalently, it preserves inner products up to a common positive factor. In our case, $g_{J}$ and $g_{J}^{\prime}$ are in the same conformal class since $\left.F\right|_{B_{1}(p)}$ and $\omega_{p}$ are in the same conformal class since for any $q \in B_{1}(p), F(q)=L_{p}(q) \omega_{p}(q)$, where $L_{p}(q)$ is a positive function on $B_{1}(p), L_{p}(p)=1$. Therefore, a $J$-holomorphic curve $u: \Sigma \longrightarrow\left(B_{1}(p), g_{J}^{\prime}, J\right)$ is also a minimal surface with respect to the almost Hermitian metric $g_{J}$.

We now return to the proof of Theorem A.33. The set of non integrability points of $e^{-\varphi}$ is the intersection of all hypersurfaces $f^{-1}(0)$ defined by holomorphic functions such that
$$\int_{B_{1}(p)}|f|^{2}\left(1+|z|^{2}\right)^{-6} e^{-\varphi} d \mu_{g_{J}^{\prime}}<\infty$$
Indeed $f$ must vanish at any non integrability point, and on the other hand Proposition A. 36 shows that one can choose $f\left(z^{0}\right)=1$ at any integrability point $z^{0}$. Suppose that $z^{0} \in f^{-1}(0)$, where $f$ is a holomorphic function on $B_{1}(p)$. Then there exists a holomorphic curve $u_{f}: \Sigma \longrightarrow\left(B_{1}(p), g_{0}, J_{s t}\right)$ passing through point $z^{0}$. Nijenhuis and Woolf (cf. [62, Theorem III]) proved the following result: Let $J$ be an almost-complex structure on a manifold $X$ of real dimension $2 n$, of class $C^{k, \lambda}$ ( $k \geq 0$ is integer, $0<\lambda<1$ ). Then for every point $x$ of $X$ and every complex tangent vector $v$, there is a $J$-holomorphic curve of class $C^{1, \lambda}$ passing through $x$ with tangent vector $v$ at $x$. Every such curve is actually of class $C^{k+1, \lambda}$.

Hence, there exists a $J$-holomorphic curve $u_{f}^{\prime}: \Sigma^{\prime} \rightarrow B_{1}(p)$ passing through $z^{0} \in B_{1}(p)$ which is contact $u_{f}: \Sigma \rightarrow B_{1}(p)$ at $z^{0}$, that is, $T_{z^{0}} u_{f}^{\prime}\left(\Sigma^{\prime}\right)=T_{z^{0}} u_{f}(\Sigma)$. In fact, one can obtain a bijective corresponding between small enough $J$-holomorphic discs and usual holomorphic discs (see Diederich-Sukhov [14, p.334] for details).

Therefore, the set of non integrability points of $e^{-\varphi}$ is the intersection of all $J$ -holomorphic curves $u_{f}^{\prime}: \Sigma^{\prime} \rightarrow\left(B_{1}(p), J\right)$ which are minimal surfaces with respect to
the almost Hermitian metric $g_{J}$. Thus, the set of points in the neighborhood of which $e^{-\varphi}$ is not integrable is a $J$-analytic subset of $\Omega$ of dimension (complex) $\leq 1$. This completes the proof of Theorem A.33. \(\square\)

\section*{Appendix B Siu's decomposition theorem on tamed almost complex 4-manifolds}

As done in classical complex analysis, we define Lelong number for closed, positive almost complex (1, 1)-currents (almost Kähler currents). We will discuss basic properties of almost Kähler currents and prove Siu's decomposition theorem on tamed almost complex 4-manifolds. Our argument follows J.-P. Deamilly [13].

\section*{B. 1 Lelong numbers of closed positive (1, 1)-currents on tamed almost complex 4-manifolds}

In this subsection, we will study closed, positive almost complex (1, 1)-currents on almost complex 4-manifolds. Note that any almost complex 4-manifold $(M, J)$ has the local symplectic property [54], that is, $\forall p \in M$, there are a neighborhood $U_{p}$ of $p$ and a closed $J$-compatible 2-form $\omega_{p}$ on $U_{p}$ such that $d \omega_{p}=0$ and $\omega_{p} \wedge \omega_{p}>0$ on $U_{p}$. We may assume without loss of generality that $U_{p}$ is a star shaped strictly $J$-pseudoconvex open set, by Poincaré Lemma, there is a vector field $\xi_{p}$ on $U_{p}$ such that $i_{\xi_{p}} \omega_{p}=\alpha_{p}$ and $\omega_{p}=d \alpha_{p}$. The fundamental theorem of Darboux [2, 22] shows that there are a neighborhood $U_{p}^{\prime} \subset \subset U_{p}$ of $p$ and diffeomorphism $\Phi_{p}$ from $U_{p}^{\prime}$ onto $\Phi_{p}\left(U_{p}^{\prime}\right) \subset \mathbb{C}^{2} \cong \mathbb{R}^{4}$ such that $\left.\omega_{p}\right|_{U_{p}^{\prime}}=\Phi_{p}^{*} \omega_{0}$, where $\Phi_{p}(p)=0 \in \mathbb{C}^{2}$. Since the concepts we are going to study mostly concern the behaviour of currents or $J$-plurisubharmonic functions in a neighbordhood of a point on an almost complex 4-manifold $(M, J)$, we may assume that $\left(M, g_{J}, J, \omega\right)$ is an almost Kähler 4-manifold, where $g_{J}(\cdot, \cdot)=\omega(\cdot, J \cdot)$. Moreover, without loss of generality, we may assume that $M$ is an open subset of $\mathbb{C}^{2}$. Then the $J$-plurisubharmonic, standard plurisubharmonic and Hermitian plurisubharmonic on $M$ are equivalent. Let $\phi: M \rightarrow$ $[-\infty, \infty)$ be a continuous $J$-plurisubharmonic function (our continuity assumption means that $e^{\phi}$ is continuous). We say that a $J$-plurisubharmonic function $\phi$ is semi-exhaustive if there exists a real number $c$ such that $B_{c, \phi} \subset \subset M$, where
$$B_{c, \phi}:=\{x \in M \mid \phi(x)<c\} .$$
Similarly, $\phi$ is said to be semi-exhaustive on a closed subset $A \subset M$ if there exists $c$ such that $A \cap B_{c, \phi} \subset \subset M$. We are interested especially in the set of poles $\{\phi=-\infty\}$. Let $T$ be a closed positive current of bidimension $(1,1)$ on $M$. Assume that $\phi$ is semi-exhaustive on SuppT and that $B_{c, \phi} \cap$ SuppT $\subset \subset M$.

Definition B.1. (cf. Demailly [13, Definition (5.4) in Chapter 3]) Let $\left(M, g_{J}, J, \omega\right)$ be an almost Kähler 4-manifold. If $\phi$ is semi-exhaustive on SuppT and $B_{c, \phi} \cap$ Supp $T \subset \subset M$, we set for $r \in(-\infty, c)$
$$\nu(\phi, r, T)=\int_{B_{r, \phi}} T \wedge\left(d d_{J}^{c} \phi\right)$$
and
$$\nu(\phi, T)=\lim _{r \rightarrow-\infty} \nu(\phi, r, T) .$$
The number $\nu(\phi, T)$ will be called the generalized Lelong number of $T$ with respect to the weight $\phi$.

As in cassical complex analysis (cf. [13, 31]), the above limit exists because $\nu(\phi, r, T)$ is a monotone increasing function of $r$.

Proposition B.2. (cf. Demailly [13, Formula (5.5) in Chapter 3]) For any convex increasing function $\chi: \mathbb{R} \rightarrow \mathbb{R}$ we have
$$\int_{B_{r, \phi}} T \wedge\left(d d_{J}^{c} \chi \circ \phi\right)=\chi^{\prime}(r-0) \nu(\phi, r, T)$$
where $\chi^{\prime}(r-0)$ denotes the left derivative of $\chi$ at $r$.
Proof. For a detailed proof of the above Proposition, we refer to Formula (5.5) in Chapter 3 of [13]. \(\square\)

We get in particular
$$\int_{B_{r, \phi}} T \wedge\left(d d_{J}^{c} e^{2 \phi}\right)=2 e^{2 r} \nu(\phi, r, T),$$
whence the formula
$$\nu(\phi, r, T)=e^{-2 r} \int_{B_{r, \phi}} T \wedge\left(\frac{1}{2} d d_{J}^{c} e^{2 \phi}\right)$$
Suppose $p \in S u p p T$, then we define the Lelong number of $T$ with respect to the weight function $\varphi=\log \rho_{g}(p, q)$,
$$\nu(\varphi, r, T)=\int_{B_{r, \varphi}} T \wedge\left(d d_{J}^{c} \varphi\right)$$
and
$$\nu(p, T)=\lim _{r \rightarrow-\infty} \nu(\varphi, r, T) .$$
The number $\nu(p, T)$ will be called the Lelong number of $T$ at point $p$. Then Formula (B.1) gives
$$\begin{aligned}
\nu(\varphi, \log r, T) & =r^{-2} \int_{\rho_{g}(p, q)<r} T \wedge \frac{1}{2} d d_{J}^{c} \rho_{g}^{2}(p, q) \\
& =r^{-2} \int_{\rho_{g}(p, q)<r} T \wedge \sqrt{-1} \partial_{J} \bar{\partial}_{J} \rho_{g}^{2}(p, q)
\end{aligned}$$
The positive measure $\sigma_{T}=T \wedge \sqrt{-1} \partial_{J} \bar{\partial}_{J} \rho_{g}^{2}(p, q)$ is called the trace measure of $T$ (cf. Demailly [13]). We get
$$\nu(\varphi, \log r, T)=\frac{\sigma_{T}(B(p, r))}{r^{2}}$$
and $\nu(p, T)$ is the limit of this ratio as $r \rightarrow 0$. The ratio $\frac{\sigma_{T}(B(p, r))}{r^{2}}$ is an increasing function of $r$. If $T$ is smooth at $p$, then $\sigma_{T}(B(p, r))$ is bounded near the point $p$ and $\sigma_{T}(B(p, r))=O\left(r^{4}\right)$. Hence,
$$\nu(p, T)=\lim _{r \rightarrow 0} \frac{\sigma_{T}(B(p, r))}{r^{2}}=\lim _{r \rightarrow 0} O\left(r^{2}\right)=0 .$$
It is similar to the case of $J$ being integrable (cf. [13, 31, 45, 70]) that $\nu(p, T) \geq 0$ and is identically equal to zero in case $T$ is a smooth current. Also, as in classical complex analysis (cf. [13, 31]), we have the following proposition

Proposition B.3. According to the above definition, we have
$$\nu(p, T)=\lim _{r \rightarrow 0} \frac{2}{r^{2}} \int_{\rho_{g}(p, q)<r} T \wedge \omega .$$
Proof. We have the result of K. Diederich and A. Sukhov (cf. Lemma 2.1 in [14]): Let $(M, J)$ be an almost complex manifold. Then for every point $p \in M$, every $\alpha \geq 0$ and $\lambda_{0}>0$ there exists a neighborhood $U$ of $p$ and a coordinate diffeomorphism $z: U \rightarrow \mathbb{B}$ such that $z(p)=0, d z(p) \circ J(p) \circ d z^{-1}(0)=J_{s t}$ and the direct image $z_{*}(J)=d z \circ J \circ d z^{-1}$ satisfies $\left\|z_{*}(J)-J_{s t}\right\|_{C^{\alpha}(\overline{\mathbb{B}})} \leq \lambda_{0}$.

Now, let $\left(M, g_{J}, J, \omega\right)$ be an almost Kähler 4-manifold. For any $p \in M$, there exists a Darboux coordinate $\left\{z_{1}, z_{2}\right\}$ on a small neighborhood $U_{p}$ of $p$ such that
$$\omega=\frac{\sqrt{-1}}{2}\left(d z_{1} \wedge d \bar{z}_{1}+d z_{2} \wedge d \bar{z}_{2}\right)=\frac{\sqrt{-1}}{2} \partial_{J_{s t}} \bar{\partial}_{J_{s t}}|z|^{2}=\frac{\sqrt{-1}}{2} \partial_{J_{s t}} \bar{\partial}_{J_{s t}}\left(z_{1} \bar{z}_{1}+z_{2} \bar{z}_{2}\right) .$$
Choose $\alpha=1, \lambda_{0}=1$. When $r$ is small, for
$$\forall z \in B(0, r):=\left\{z \in U_{p} \mid \rho_{g_{J}}(0, z)<r\right\},$$
we have $\left\|z_{*}(J)-J_{s t}\right\|_{C^{1}} \leq 1$ and
$$\begin{aligned}
\left(d d_{J}^{c}-d d^{c}\right)|z|^{2} & =d\left(J_{s t}-J\right) d|z|^{2} \\
& =d\left(J_{s t}-J\right)\left(z_{1} \cdot d \bar{z}_{1}+d z_{1} \cdot \bar{z}_{1}+z_{2} \cdot d \bar{z}_{2}+d z_{2} \cdot \bar{z}_{2}\right) .
\end{aligned}$$
Hence
$$\left.\left|\left(d d_{J}^{c}-d d^{c}\right)\right| z\right|^{2}|\leq c| z \mid,$$
where $c$ is a positive constant. Then
$$\begin{aligned}
\frac{1}{r^{2}} \int_{\rho_{g_{J}}(0, z)<r} T \wedge \sqrt{-1} \partial_{J_{s t}} \bar{\partial}_{J_{s t}}|z|^{2}= & \frac{1}{r^{2}} \int_{\rho_{g_{J}}(0, z)<r} T \wedge \sqrt{-1} \partial_{J} \bar{\partial}_{J}|z|^{2} \\
& +O(r) \cdot \frac{1}{r^{2}} \int_{\rho_{g_{J}}(0, z)<r} T \wedge \sqrt{-1} \partial_{J} \bar{\partial}_{J}|z|^{2} .
\end{aligned}$$
Therefore
$$\lim _{r \rightarrow 0} \frac{1}{r^{2}} \int_{\rho_{g_{J}}(0, z)<r} T \wedge \sqrt{-1} \partial_{J_{s t}} \bar{\partial}_{J_{s t}}|z|^{2}=\lim _{r \rightarrow 0} \frac{1}{r^{2}} \int_{\rho_{g_{J}}(0, z)<r} T \wedge \sqrt{-1} \partial_{J} \bar{\partial}_{J}|z|^{2} .$$

On the other hand, let $\left(x^{1}, \cdots, x^{4}\right)$ be the normal coordinates of $g_{J}$ in a neighborhood $U$ of the point $p$. Then $g_{J, k l}$ have the following Taylor expansion (cf. Schone-Yau [67]):
$$g_{J, k l}(x)=\delta_{k l}+\frac{1}{3} R_{k i j l} x^{i} x^{j}+\frac{1}{6} R_{k i j l, s} x^{i} x^{j} x^{s}+O\left(r^{4}\right),$$
where all the curvatures and their covariant derivatives are evaluated at $p$. If $q \in U$,
$$\rho_{g_{J}}(p, q)=\int_{0}^{1}\left|\gamma^{\prime}(t)\right|_{g_{J}(\gamma(t))} d t$$
where $\gamma$ is the geodesic connecting points $p$ and $q$. Hence,
$$\begin{aligned}
\rho_{g_{J}}(p, q) & =\int_{0}^{1} \sqrt{g_{J}(\gamma(t))\left(\gamma^{\prime}(t), \gamma^{\prime}(t)\right)} d t \\
& =\int_{0}^{1} \sqrt{g_{J, k l}(t x) x^{k} x^{l}} d t \\
& =\int_{0}^{1} \sqrt{\left[\delta_{k l}+\frac{1}{3} R_{k i j l} t x^{i} t x^{j}+O\left(r^{3}\right)\right] x^{k} x^{l}} d t \\
& =\int_{0}^{1} \sqrt{|x|^{2}+\frac{t^{2}}{3} R_{k i j l} x^{i} x^{j} x^{k} x^{l}+O\left(r^{5}\right)} d t \\
& =\int_{0}^{1}|x| \sqrt{1+\frac{\frac{t^{2}}{3} R_{k i j l} x^{i} x^{j} x^{k} x^{l}+O\left(r^{5}\right)}{|x|^{2}}} d t \\
& =\int_{0}^{1}\left[|x|+\frac{t^{2} R_{k i j l} x^{i} x^{j} x^{k} x^{l}}{6|x|}+O\left(r^{4}\right)\right] d t \\
& =|x|+\frac{R_{k i j l} x^{i} x^{j} x^{k} x^{l}}{18|x|}+O\left(r^{4}\right)
\end{aligned}$$
Therefore,
$$\rho_{g_{J}}^{2}(p, q)=|x|^{2}+\frac{1}{9} R_{k i j l} x^{i} x^{j} x^{k} x^{l}+O\left(r^{5}\right),$$
and
$$\rho_{g_{J}}^{2}(p, q)-|x|^{2}=\frac{1}{9} R_{k i j l} x^{i} x^{j} x^{k} x^{l}+O\left(r^{5}\right)=O\left(r^{4}\right) .$$
In fact, $\rho_{g_{J}}^{2}(p, q)$ is strictly $J$-plurisubharmonic near $p$ (cf. Ivashkovich-Rosay [41, Lemma 1.3]). Then we can get
$$\begin{aligned}
\frac{1}{r^{2}} \int_{\rho_{g_{J}}(0, z)<r} T \wedge \sqrt{-1} \partial_{J} \bar{\partial}_{J} \rho_{g_{J}}^{2}(p, q)= & \frac{1}{r^{2}} \int_{\rho_{g_{J}}(0, z)<r} T \wedge \sqrt{-1} \partial_{J} \bar{\partial}_{J}|z|^{2} \\
& +O\left(r^{2}\right) \cdot \frac{1}{r^{2}} \int_{\rho_{g_{J}}(0, z)<r} T \wedge \sqrt{-1} \partial_{J} \bar{\partial}_{J}|z|^{2},
\end{aligned}$$
and
$$\lim _{r \rightarrow 0} \frac{1}{r^{2}} \int_{\rho_{g_{J}}(0, z)<r} T \wedge \sqrt{-1} \partial_{J} \bar{\partial}_{J} \rho_{g_{J}}^{2}(p, q)=\lim _{r \rightarrow 0} \frac{1}{r^{2}} \int_{\rho_{g_{J}}(0, z)<r} T \wedge \sqrt{-1} \partial_{J} \bar{\partial}_{J}|z|^{2} .$$
At last, by (B.4) and (B.5),
$$\lim _{r \rightarrow 0} \frac{1}{r^{2}} \int_{\rho_{g_{J}}(0, z)<r} T \wedge \sqrt{-1} \partial_{J} \bar{\partial}_{J} \rho_{g_{J}}^{2}(p, q)=\lim _{r \rightarrow 0} \frac{1}{r^{2}} \int_{\rho_{g_{J}}(0, z)<r} T \wedge \sqrt{-1} \partial_{J_{s t}} \bar{\partial}_{J_{s t}}|z|^{2} .$$
This completes the proof of the proposition. \(\square\)

All these results are particularly interesting when $T_{\Sigma}$ is the current of integration over a $J$-holomorphic curve. Then $\sigma_{T}(B(p, r))$ is the Euclidean area of $\Sigma \cap B(p, r)$, while $\pi r^{2}$ is the area of a disc of radius $r$. Then it is immediate to check that
$$\nu\left(p, T_{\Sigma}\right)= \begin{cases}0 & \text { if } p \notin \Sigma, \\ 1 & \text { if } p \in \Sigma .\end{cases}$$

In [24], Elkhadhra has studied the Lelong number of a positive current $T$ of bidimension $(p, p)$ defined on an almost complex manifold. In particular, he has proven that the Lelong numbers of a positive current are independent on the coordinate systems (cf. Elkhadhra [24, Theorem 3]). Thus, we have the following proposition:

Proposition B.4. (cf. [13, 24, 70]) The Lelong number, $\nu(\phi, T)$, is independent of the choice of local coordinates.

We are going to introduce the notions of $J$-pluripolar subset and $J$-analytic subset in an almost complex $2 n$-manifold $(X, J)$. Such subsets should be considered as almost complex analogues of "classical" complex case. In general, $J$-pluripolar subsets are the sets of $-\infty$ poles of $J$-plurisubharmonic functions.

Definition B.5. (cf. [13,23]) A subset $A$ of an almost complex $2 n$-manifold $(X, J)$ is said to be $J$-pluripolar if for every point $x \in X$ there exist a connected neighborhood $U$ of $x$ and $u \in P S H(X, J), u \not \equiv-\infty$, such that $A \cap U \subset\{y \in U \mid u(y)=-\infty\}$.
$A$ subset $A \subset X$ is said to be complete $J$-pluripolar in $X$ if for every point $x \in X$ there exist a neighborhood $U$ of $x$ and $u \in P S H(X, J) \cap L_{\text {loc }}^{1}(U)$ such that $A \cap U \subset$ $\{y \in U \mid u(y)=-\infty\}$. A is said to be regular complete $J$-pluripolar if there exists a $J$ -plurisubharmonic function $u$ on $X$, of class $C^{2}$ on $X \backslash u^{-1}(-\infty)$ such that $A=u^{-1}(-\infty)$.

Remark B.6. In the case when the structure $J$ is integrable, El Mir [20] proved that every complete $(J-)_{\text {pluripolar }}$ subset is regular.

Let $(X, J)$ be an almost complex manifold, $A$ a closed subset of $X$ and $T$ a current of order zero on $X \backslash A$. One says that $T$ admits a trivial extension $\tilde{T}$ on $X$ if $T$ has a locally finite mass in the neighborhood of every point of $A$, in which case $\tilde{T}$ can be defined by putting $\tilde{T}=0$ on $A$; the existence of some extension $T^{\prime}$ is in any case equivalent to the local finiteness of the mass of $T$ near $A$. In [23], F. Elkhadhra presented a generalization of El Mir's theorem [20] on the extension of positive currents across a complete $J$-pluripolar subset, in the almost complex setting. For a detailed description of the almost complex version of El Mir's theorem, we refer to Theorem 1 in [23]. Here, we mainly want to apply its corollary, hence, we have the following proposition:

Proposition B.7. (cf. Elkhadhra [23, Corollary 1]) Let $T$ is a closed positive current of bidimension (1, 1). If $A \subset X$ is a closed regular complete $J$-pluripolar set and $i d_{A}$ is its characteristic function, then $i d_{A} T$ is a closed positive current.

It is well known that if $J$ is integrable, every ( $J$-)analytic subset is a regular complete ( $J$-)pluripolar set. But this is not yet established in the non-integrable case. As a generalization of classical complex analysis, we have the following definition:

Definition B.8. (cf. Elkhadhra [24]) We say that $A$ is a $J$-analytic subset of an almost complex $2 n$-manifold $(X, J)$ of dimension $p$ if there exists a finite sequence of closed subsets
$$\emptyset=A_{-1} \subset A_{0} \subset \cdots \subset A_{p}=A,$$
where $A_{j} \backslash A_{j-1}$ is a smooth almost complex submanifold of $X \backslash A_{j-1}$, of complex dimension $j$ and has a locally finite $2 j$-Hausdorff measure in the neighborhood of every point of $X$. We say that $A$ is of pure complex dimension $p$ if moreover we have $A_{j-1} \subset \overline{A_{j} \backslash A_{j-1}}$, for $j=0,1,2, \cdots, p$. If the $p$-dimensional strata $A_{p} \backslash A_{p-1}$ are connected we say that $A$ is irreducible.

Notice that the definition for the almost complex setting does coincide with the usual analytic subsets in the integrable case. In order to justify the above definition let us recall that every closed $J$-holomorphic curve $A$ of $(X, J)$ is $J$-analytic. Indeed, we write $\emptyset=A_{-1} \subset A_{0} \subset A_{1}=A$, where $A_{0}$ is the singular part of $A$ which is discrete. More generally, every almost complex submanifold is a $J$-analytic subset. As in classical complex analysis, we have the following lemma:

Lemma B.9. (cf. Demailly [13, Lemma 8.15 in Chapter 3]) If $T$ is a closed positive current of bidimension $(1,1)$ on a almost Kähler 4-manifold $\left(X, g_{J}, J, \omega\right)$ and let $A$ be an irreducible $J$-analytic set, we set
$$m_{A}:=\inf \{\nu(x, T) \mid x \in A\} .$$
Then $\nu(x, T)=m_{A}$ for $x \in A \backslash \cup A_{j}$, where $\left(A_{j}\right)$ is a countable family of proper $J$-analytic subsets of $A$. We say that $m_{A}$ is the generic Leong number of $T$ along $A$.

Proof. The upperlevel sets of the Lelong number is defined by
$$E_{c}(T):=\{x \in X \mid \nu(x, T) \geq c\} .$$
By definition of $m_{A}$ and $E_{c}(T)$, we have $\nu(x, T) \geq m_{A}$ for every $x \in A$ and
$$\nu(x, T)=m_{A}$$
on $A \backslash \bigcup_{c \in \mathbb{Q}, c>m_{A}} A \cap E_{c}(T)$. However, for $c>m_{A}$, the intersection $A \cap E_{c}(T)$ is a proper $J$-analytic subset of $A$. \(\square\)

According to Definition B.8, this enables us to deduce without difficulty that every $J$ -analytic subset $A$ is a locally regular complete $J$-pluripolar subset away from the singular part of $A$. Obviously, a natural question arises here: Is every $J$-analytic subset a (locally) regular complete $J$-pluripolar set? What would happen if closed positive currents are restricted to $J$-analytic subsets? Although this is a well-known result when $J$ is integrable. Our next result concerns the restriction of closed positive currents on $J$-analytic subsets. First, recall that in terms of currents, if $A$ is a $J$-analytic subset of complex dimension $p$ then $T_{A}$ defines a closed positive $(p, p)$-current by integrating $(p, p)$ test forms on the components of $A$ of dimension $2 p$. More precisely, assume that
$$\emptyset=A_{-1} \subset A_{0} \subset \cdots \subset A_{p}=A$$
is a sequence as in Definition B. 8 and let $Y=A_{p} \backslash A_{p-1}$. Since $Y$ is a smooth almost complex submanifold of $X \backslash A_{p-1}$, then the integration on $Y$ defines a positive closed current on $X \backslash A_{p-1}$. When $A$ is a $J$-analytic subset of complex dimension $p$, we obtain the following proposition.

Proposition B.10. (cf. Elkhadhra [24, Lemma 1]) Assume that $T$ is a positive closed current of bidimension $(p, p)$ on almost complex manifold $(X, J)$, and $A$ is a $J$-analytic subset of complex dimension $p$, then the cut-off $i d_{A} T$ is also a positive and closed current supported by $A$.

Notice also that by the same idea of Proposition B.10, we can easily see that the current of integration $T_{A}$ on a $J$-analytic subset is positive and closed.

Proposition B.11. (cf. Elkhadhra [24, Theorem 2]) Let $T$ be a closed positive current of bidimension $(p, p)$ on an almost Kähler manifold $(X, J)$. Let $A$ be a $J$-analytic subset of $(X, J)$ of dimension $p$. Then, we have
$$i d_{A} T=m_{A} T_{A},$$
in particular $T-m_{A} T_{A}$ is positive.
Remark B.12. Elkhadhra proved the above proposition on the almost complex manifold in [24]. Since our Lelong number is defined on the almost Kähler manifold in this paper, we describe Elkhadhra's result on the almost Kähler manifold.

The purpose of the remainder of this subsection is to give two other definitions of Lelong number on tamed closed almost complex 4-manifolds. Suppose that $(M, J)$ is an almost complex 4-manifold tamed by a symplectic 2-form $\omega_{1}=F+d_{J}^{-}(v+\bar{v})$, where $v \in \Omega_{J}^{0,1}$ and $F$ is a fundamental 2-form. Let $g_{J}(\cdot, \cdot)=F(\cdot, J \cdot)$ be an almost Hermitian metric and $d \mu_{g_{J}}$ the volume form. Suppose that $\rho_{g_{J}}(p, q)$ is the geodesic distance of points $p, q$ with respect to $g_{J}$ (cf. Chavel [9]). Denote by
$$B(p, r):=\left\{q \in M \mid \rho_{g_{J}}(p, q) \leq r\right\} .$$

Definition B.13. If $p \in \operatorname{Supp} T, T$ is a closed positive $(1,1)$-current on a closed almost complex 4-manifold tamed by a symplectic form $\omega_{1}=F+d_{J}^{-}(v+\bar{v}), v \in \Omega_{J}^{0, l}$, we define the Lelong number as follows
$$\nu_{1}\left(p, \omega_{1}, r, T\right)=\frac{2}{r^{2}} \int_{B(p, r)} T \wedge \omega_{1}$$
and
$$\nu_{1}(p, T)=\lim _{r \rightarrow 0} \nu_{1}\left(p, \omega_{1}, r, T\right) .$$

Notice that as in the almost Kähler case, $\nu_{1}\left(p, \omega_{1}, r, T\right)$ is an increasing function of $r$. On the other hand, any almost complex 4-manifold $(M, J)$ has the local symplectic property [54], that is, $\forall p \in M$, there is a neighborhood $U_{p}$ of $p$ and a $J$-compatible
symplectic form $\omega_{p}$ on $U_{p}$ such that $\left.\omega_{p}\right|_{p}=\left.F\right|_{p}$ and $F=f_{p} \omega_{p}, f_{p} \in C^{\infty}\left(U_{p}\right)$. Fix a point $q \in U_{p}$. Moreover, we assume that $r$ is small enough such that $B(q, r) \subset U_{p}$. It is similar to Definition B.1, in particular (B.3), on symplectic 4-manifold $\left(U_{p}, \omega_{p}\right)$, we can define Lelong number as follows,