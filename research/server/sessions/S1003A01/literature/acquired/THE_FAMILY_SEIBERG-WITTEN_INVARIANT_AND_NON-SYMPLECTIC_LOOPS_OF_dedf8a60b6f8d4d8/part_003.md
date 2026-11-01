---
retention_scope: session
part: 3
total_parts: 5
---

[Part 3/5 of: THE FAMILY SEIBERG-WITTEN INVARIANT AND NON-SYMPLECTIC LOOPS OF DIFFEOMORPHISMS]

The discrepancy between the orientation of the boundary strata and the boundary orientation is caused by switching various factors in the gluing construction. Therefore, there are universal formulas that express the sign differences in terms of $\operatorname{dim} \mathcal{Q}$ and dimension of the various moduli spaces. To find out these formulas, we consider the special case $\widetilde{W}_{12}=\mathcal{Q} \times W_{12}$, which also implies that $\widetilde{W}_{02}=\mathcal{Q} \times W_{02}$. Therefore, we have orientation preserving homeomorphisms
$$\widetilde{M}_{12} \cong \mathcal{Q} \times M_{12}, \quad \widetilde{M}_{02} \cong \mathcal{Q} \times M_{02} .$$
(Recall that we orient the moduli spaces by putting the $\mathcal{Q}$-coordinates first.) By [19, Proposition 26.1.7] , the orientation of the boundary strata $\mathcal{M}_{01} \times \mathcal{M}_{12} \times \breve{\mathcal{M}}_{2}$ differs from the boundary orientation of $\bigcup_{S \in[0,+\infty]}\{S\} \times \mathcal{M}_{z}^{+}\left([\mathfrak{a}], W(S)^{*},[\mathfrak{b}]\right)$ by the sign (-1). As a result, the orientation of the boundary strata
$$\mathcal{M}_{01} \times \widetilde{\mathcal{M}}_{12} \times \breve{\mathcal{M}}_{2} \cong \mathcal{M}_{01} \times \mathcal{Q} \times \mathcal{M}_{12} \times \breve{\mathcal{M}}_{2}$$
differs from the boundary orientation of the parametrized moduli space
$$\mathcal{M}_{z}^{+}([\mathfrak{a}],[\mathfrak{b}]) \cong \mathcal{Q} \times\left(\bigcup_{S \in[0,+\infty]}\{S\} \times \mathcal{M}_{z}^{+}\left([\mathfrak{a}], W(S)^{*},[\mathfrak{b}]\right)\right)$$
by the sign $(-1) \cdot(-1)^{d_{01} \cdot \operatorname{dim}(\mathcal{Q})}$. This finishes the proof of (iv). And the other cases are similar. \(\square\)

Now we define maps
$$\begin{aligned}
& K_{o}^{o}: C_{\bullet}^{o}\left(Y_{0}, \mathfrak{s}_{Y_{0}}\right) \rightarrow C_{\bullet}^{o}\left(Y_{2}, \mathfrak{s}_{Y_{2}}\right) \\
& K_{s}^{o}: C_{\bullet}^{o}\left(Y_{0}, \mathfrak{s}_{Y_{0}}\right) \rightarrow C_{\bullet}^{s}\left(Y_{2}, \mathfrak{s}_{Y_{2}}\right) \\
& K_{o}^{s}: C_{\bullet}^{o}\left(Y_{0}, \mathfrak{s}_{Y_{0}}\right) \rightarrow C_{\bullet}^{o}\left(Y_{2}, \mathfrak{s}_{Y_{2}}\right) \\
& K_{s}^{s}: C_{\bullet}^{o}\left(Y_{0}, \mathfrak{s}_{Y_{0}}\right) \rightarrow C_{\bullet}^{o}\left(Y_{2}, \mathfrak{s}_{Y_{Y}}\right)
\end{aligned}$$
by counting points in the zero-dimensional moduli spaces $\mathcal{M}_{z}([\mathfrak{a}],[\mathfrak{b}])$. More precisely, we define
$$\begin{aligned}
K_{o}^{o}\left(e_{[\mathfrak{a}]}\right) & =\sum_{[\mathfrak{b}] \in \mathfrak{C}^{o}\left(Y_{2}, \mathfrak{s}_{Y_{2}}\right)} \sum_{z} \# \mathcal{M}_{z}([\mathfrak{a}],[\mathfrak{b}]) \cdot e_{[\mathfrak{b}]} \\
K_{s}^{o}\left(e_{[\mathfrak{a}]}\right) & =\sum_{[\mathfrak{b}] \in \mathfrak{C}^{s}\left(Y_{2}, \mathfrak{s}_{Y_{2}}\right)} \sum_{z} \# \mathcal{M}_{z}([\mathfrak{a}],[\mathfrak{b}]) \cdot e_{[\mathfrak{b}]} \\
K_{o}^{s}\left(e_{[\mathfrak{a}]}\right) & =\sum_{[\mathfrak{b}] \in \mathfrak{C}^{o}\left(Y_{2}, \mathfrak{s}_{Y_{2}}\right)} \sum_{z} \# \mathcal{M}_{z}([\mathfrak{a}],[\mathfrak{b}]) \cdot e_{[\mathfrak{b}]} \\
K_{s}^{s}\left(e_{[\mathfrak{a}]}\right) & =\sum_{\left[\hat{C}^{s}\left(Y_{2}, \mathfrak{s}_{Y_{2}}\right)\right.} \sum_{z} \# \mathcal{M}_{z}([\mathfrak{a}],[\mathfrak{b}]) \cdot e_{[\mathfrak{b}]}
\end{aligned}$$
Here we are summing over all homotopy classes
$$z \in \bigcup_{\mathfrak{s} \in \mathbb{S}} \pi_{0}\left(\mathcal{B}^{\sigma}\left([\mathfrak{a}], \widetilde{W}_{02}^{*}, \mathfrak{s},[\mathfrak{b}]\right),\right.$$
such that $\mathcal{M}_{z}([\mathfrak{a}],[\mathfrak{b}])$ is 0 -dimensional. The sum may not be finite but the finiteness result Lemma 4.15 ensures that these maps are still well-defined because we have passed to the completion. Similarly, we can define operators $\bar{K}_{s}^{u}, \bar{K}_{u}^{u}, \bar{K}_{u}^{s}, \bar{K}_{s}^{s}$ by counting reducible solutions only.

As in [19], we package these operators and obtain an operator
$$\check{K}: \check{C}_{\bullet}\left(Y_{0}, \mathfrak{s}_{Y_{0}}\right) \rightarrow \check{C}_{\bullet}\left(Y_{2}, \mathfrak{s}_{Y_{2}}\right)$$
defined by
$$\check{K}=\left[\begin{array}{cc}
K_{o}^{o} & -K_{o}^{u} \bar{\partial}_{u}^{s}-m_{o}^{u} \bar{m}_{s}^{u}-\partial_{o}^{u} \bar{K}_{s}^{u} \\
K_{s}^{o} & \bar{K}_{s}^{s}-K_{s}^{u} \bar{\partial}_{u}^{s}-m_{s}^{u} \bar{m}_{u}^{s}-\partial_{s}^{u} \bar{K}_{u}^{s}
\end{array}\right] .$$
Here $m_{o}^{u}$ and $m_{s}^{u}$ are defined in (30) using the single cobordism $\left(W_{01}, \mathfrak{s}_{W_{01}}\right)$ with perturbations $\mathfrak{p}_{1, \infty}^{\prime \prime}$ and $\mathfrak{p}_{2, \infty}^{\prime}$ introduced in Construction 4.18 (3). And $\bar{m}_{s}^{u}$ and $\bar{m}_{u}^{s}$ are defined in (31) using the family cobordism $\left(\widetilde{W}_{12}, \mathfrak{s}_{\widetilde{W}_{12}}\right)$, with perturbations $\left\{\mathfrak{p}_{0, \infty, b}^{\prime}\right\}$ and $\left\{\mathfrak{p}_{1, \infty, b}^{\prime}\right\}$ introduced in Construction 4.18 (4).

Using the perturbations specified in Construction 4.18, we can define the operator
$$\check{m}_{01}: \check{C}_{\bullet}\left(Y_{0}, \mathfrak{s}_{Y_{0}}\right) \rightarrow \check{C}_{\bullet}\left(Y_{1}, \mathfrak{s}_{Y_{1}}\right)$$
for the cobordism $\left(W_{01}, \mathfrak{s}_{W_{01}}\right)$, as well as the operator
$$\check{m}_{12}: \check{C}_{\bullet}\left(Y_{1}, \mathfrak{s}_{Y_{1}}\right) \rightarrow \check{C}_{\bullet}\left(Y_{2}, \mathfrak{s}_{Y_{2}}\right)$$
for the (family) cobordism $\left(\widetilde{W}_{12}, \mathfrak{s}_{\widetilde{W}_{12}}\right)$. Furthermore, for any $\mathfrak{s} \in \mathbb{S}$, we define the operator
$$\check{m}_{02}: \check{C}_{\bullet}\left(Y_{0}, \mathfrak{s}_{Y_{0}}\right) \rightarrow \check{C}_{\bullet}\left(Y_{2}, \mathfrak{s}_{Y_{2}}\right)$$
for the family spin ${ }^{c}$-cobordism $\left(\widetilde{W}_{02}, \mathfrak{s}\right)$. By summing these operators for all $\mathfrak{s} \in \mathbb{S}$, we get the operator
$$\breve{m}_{02, \mathbb{S}}: \breve{C}_{\bullet}\left(Y_{0}, \mathfrak{s}_{Y_{0}}\right) \rightarrow \breve{C}_{\bullet}\left(Y_{2}, \mathfrak{s}_{Y_{2}}\right)$$

Proposition 4.20. The following equality holds:
$$\check{K} \check{\partial}+\check{\partial} \check{K}=\check{m}_{02, \mathbb{S}}-\check{m}_{01} \check{m}_{12} .$$
Proof. The proof is essentially identical to [19, Lemma 26.2.2]. We consider parametrized moduli space $\mathcal{M}_{z}^{+}([\mathfrak{a}],[\mathfrak{b}])$ of dimension 1. By counting points in various boundary strata of this moduli space, we obtain relations between the operators $\bar{\partial}_{*}^{*}, \partial_{*}^{*}, m_{*}^{*}, m_{*}^{*}, K_{*}^{*}$ (see [19, Lemma 26.2.3]), which implies (48). Note that we are using the family cobordism $\widetilde{W}_{12}$ instead of a single cobordism $W_{12}$. This could potentially change the sign in these relations. However, since we are only considering 1-dimensional moduli space $\mathcal{M}_{z}^{+}([\mathfrak{a}],[\mathfrak{b}])$ here. The boundary strata are all 0-dimensional. As a result, the second factors in Proposition 4.19 is always 1. This allows us to use the same sign as [19] and repeat their calculation without worrying about sign-issue. \(\square\)

Proposition 4.20 directly implies that
$$\sum_{\mathfrak{s} \in \mathbb{S}} \widetilde{H M} \bullet\left(\widetilde{W}_{02}, \mathfrak{s}\right)=\widetilde{H M}_{\bullet}\left(W_{01}, \mathfrak{s}_{W_{01}}\right) \circ \widetilde{H M} \bullet\left(\widetilde{W}_{12}, \mathfrak{s}_{\widetilde{W}_{12}}\right) .$$
Since there is a natural inclusion $\widetilde{H M}_{*}\left(Y_{i}, \mathfrak{s}_{Y_{i}}\right) \hookrightarrow \widetilde{H M}_{\bullet}\left(Y_{i}, \mathfrak{s}_{Y_{i}}\right)$, the proof of Theorem 4.12 (1) is finished. The other parts of Theorem 4.12 are proved by modifying the corresponding proofs of [19] in exactly the same way.
4.2.4. Composition law for the mixed map. Next, we discuss the composition law for $\overrightarrow{H M}$. We start with our assumption in the current subsection:

Assumption 4.21. $\left(\widetilde{W}_{12}, \mathfrak{s}_{\widetilde{W}_{12}}\right)$ is a product family associated to a $\operatorname{spin}^{c}-\operatorname{cobordism}\left(W_{12}, \mathfrak{s}_{W_{12}}\right)$ with $b_{2}^{+}\left(W_{12}\right)>0$.

We fix an orientation on $H_{2}^{+}\left(W_{12} ; \mathbb{R}\right)$ so that when $b_{2}^{+}\left(W_{12}\right)=1$, we can talk about the maps
$$\overrightarrow{H M}_{*}\left(W_{12}, \mathfrak{s}_{W_{12}}\right)_{+}, \overrightarrow{H M}_{*}\left(W_{12}, \mathfrak{s}_{W_{12}}\right)_{-}: \widehat{H M}\left(Y_{1}, \mathfrak{s}_{Y_{1}}\right) \rightarrow \widetilde{H M}\left(Y_{2}, \mathfrak{s}_{Y_{2}}\right)$$
associated to the positive/negative chamber. If we further have $b_{2}^{+}\left(W_{02}\right)=b_{2}^{+}\left(W_{12}\right)=1$, then this orientation on $H_{2}^{+}\left(W_{12} ; \mathbb{R}\right)$ also induces an orientation on $H_{2}^{+}\left(W_{02} ; \mathbb{R}\right)$. So we have maps
$$\overrightarrow{H M}_{*}\left(\widetilde{W}_{02}, \mathfrak{s}\right)_{+}, \overrightarrow{H M}_{*}\left(\widetilde{W}_{02}, \mathfrak{s}\right)_{-}: \widehat{H M}\left(Y_{0}, \mathfrak{s}_{Y_{0}}\right) \rightarrow \widetilde{H M}\left(Y_{2}, \mathfrak{s}_{Y_{2}}\right) .$$

When $b_{2}^{+}\left(W_{12}\right)>1$ (resp. $b_{2}^{+}\left(W_{02}\right)>1$ ), we have the map $\overrightarrow{H M}_{*}\left(W_{12}, \mathfrak{s}\right)$ (resp. $\overrightarrow{H M}_{*}\left(\widetilde{W}_{02}, \mathfrak{s}\right)$ ) defined using the unique canonical chamber.

Theorem 4.22. Under Assumption 4.21, we have the following results:
\begin{itemize}
\item[(1)] Suppose $b_{2}^{+}\left(W_{12}\right)>1$. Then
$$\sum_{\mathfrak{s} \in \mathbb{S}} \overrightarrow{H M}_{*}\left(\widetilde{W}_{02}, \mathfrak{s}\right)=\widehat{H M}_{*}\left(\widetilde{W}_{01}, \mathfrak{s}_{\widetilde{W}_{01}}\right) \circ \overrightarrow{H M}_{*}\left(W_{12}, \mathfrak{s}_{W_{12}}\right) .$$
\item[(2)] Suppose $b_{2}^{+}\left(W_{02}\right)>b_{2}^{+}\left(W_{12}\right)=1$. Then
$$\sum_{\mathfrak{s} \in \mathbb{S}} \overrightarrow{H M}_{*}\left(\widetilde{W}_{02}, \mathfrak{s}\right)=\widehat{H M}_{*}\left(\widetilde{W}_{01}, \mathfrak{s} \widetilde{W}_{01}\right) \circ \overrightarrow{H M}_{*}\left(W_{12}, \mathfrak{s}_{W_{12}}\right)_{ \pm} .$$
\item[(3)] Suppose $b_{2}^{+}\left(W_{02}\right)=b_{2}^{+}\left(W_{12}\right)=1$. Then
$$\sum_{\mathfrak{s} \in \mathbb{S}} \overrightarrow{H M}_{*}\left(\widetilde{W}_{02}, \mathfrak{s}\right)_{ \pm}=\widehat{H M}_{*}\left(\widetilde{W}_{01}, \mathfrak{s}_{\widetilde{W}_{01}}\right) \circ \overrightarrow{H M}_{*}\left(W_{12}, \mathfrak{s}_{W_{12}}\right)_{ \pm} .$$
\end{itemize}

We will prove Theorem 4.22 through the rest of this subsection. We will focus on (1) because the proof of the other two cases are essential the same by working with the positive or the negative canonical chamber.

We first show that the sums in above formulas are always finite.
Lemma 4.23. For any chamber $\xi \in\left[\mathcal{Q}, V^{+}\left(W_{02}\right)\right]$, there are only finitely many $\mathfrak{s} \in \mathbb{S}$ such that the map $\overrightarrow{H M}\left(\widetilde{W}_{02}, \mathfrak{s}\right)_{\xi}$ is nontrivial.

Proof. The proof is similar to Lemma 4.11. The current case is actually simpler because there is no reducible solutions on $\widetilde{W}_{02}$ by our choice of perturbation 2-forms $\left\{\omega_{02, b}\right\}$. Hence no solutions on $\widetilde{W}_{02}$ can limit to a boundary stable solution on $Y_{0}$ or a boundary unstable solution on $Y_{2}$. \(\square\)

For the rest of this section, we assume $b_{2}^{+}\left(W_{12}\right)>1$. We fix a single metric $g_{W_{12}}$ on $W_{12}$ and a family metric $\left\{g_{W_{01, b}}\right\}$ on $\widetilde{W}_{01}$. Note that we have chosen $g_{W_{12}}$ such that the collar neighborhood $N_{i}$ of the boundary component $Y_{i}$ is isometric to $[0,1] \times Y_{i}$. For $T>0$, we let $W_{12}^{T}$ be obtained from $W_{12}$ by inserting two cylinders $[1, T] \times Y_{1}$ and $[1, T] \times Y_{2}$ between $W_{12} \backslash\left(N_{1} \cup N_{2}\right)$ and $N_{1} \cup N_{2}$.

For $S>0$, we consider a new family of cobordism $\widetilde{W}(S, T)$ from $Y_{0}$ to $Y_{2}$, whose fiber over $b$ is given by
$$W(S, T)_{b}:=W_{01, b} \cup\left([-S, S] \times Y_{1}\right) \cup W_{12}^{T} .$$
As before, we use $\widetilde{W}(S, T)^{*}$ to denote the family obtained by attaching cylindrical ends to each fiber. We denote the family metric on $\widetilde{W}(S, T)$ by $g_{\widetilde{W}(S, T)}=\left\{g_{W(S, T)_{b}}\right\}$.

To construct suitable perturbations on $\widetilde{W}(S, T)^{*}$, we slightly modify Construction 4.18 as follows:
\begin{itemize}
\item[-] In step (1), we pick a self-dual 2-form $w_{12}$ supported on $W_{12} \backslash\left(N_{1} \cup N_{2}\right)$. We require that $\left(\omega_{12}, g_{W_{12}}\right)$ is admissible with respect to $\mathfrak{s}_{W_{12}}$ if $c_{1}\left(\mathfrak{s}_{Y_{1}}\right)$ and $c_{1}\left(\mathfrak{s}_{Y_{2}}\right)$ are torsion. Then we use $\omega_{12}$ as a perturbation 2-form on the fiber $W(S, T)_{b}$ for any $S, T, b$.
\item[-] We repeat the rest steps without change. We emphasise that we don't apply any perturbations on the newly-added cylinders $[1, T] \times Y_{1}$ and $[1, T] \times Y_{2}$.
\end{itemize}

Lemma 4.24. Suppose $c_{1}\left(\mathfrak{s}_{Y_{0}}\right)$ and $c_{1}\left(\mathfrak{s}_{Y_{2}}\right)$ are both torsion. Then for any $\mathfrak{s} \in \mathbb{S}$, there exists $T_{\mathfrak{s}, 0} \gg 0$ such that for any $S \geqslant 0$ and $T \geqslant T_{\mathfrak{s}, 0}$, the pair $\left(g_{\widetilde{W}(S, T)}, \omega_{12}\right)$ is admissible with respect to $\mathfrak{s}$ and the corresponding chamber is the canonical chamber $\xi_{c}$.

Proof. Because $\left(\widetilde{W}(S, T), g_{\widetilde{W}(S, T)}\right)$ is isometric to $\left(\widetilde{W}(S+T), g_{\widetilde{W}(S+T)}\right)$, we may assume $S=0$. We pick a family spin ${ }^{c}$ connection $\left\{A_{b, T}\right\}$ on the fibers of $\widetilde{W}(T)^{*}$ that satisfies the following conditions:
\begin{itemize}
\item[-] When restricted to $W_{01, b}, A_{b, T}$ is independent with $T$;
\item[-] When restricted to $W_{12, b}, A_{b, T}$ is independent with $T$ and $b$;
\item[-] When restricted to the cylinders $(-\infty, 0] \times Y_{0},[-T, T] \times Y_{1}$ and $[0,+\infty) \times Y_{1}$, $A_{b, T}$ is pulled back from a connection $A_{Y_{i}}$ on $Y_{i}$ that is independent with $b, T$. We assume that $A_{Y_{i}}^{t}$ is flat for $i=0,2$. This is possible because our assumption that $c_{1}\left(\mathfrak{s}_{Y_{1}}\right)$ and $c_{1}\left(\mathfrak{s}_{Y_{2}}\right)$ are torsion.
\end{itemize}
We first suppose $c_{1}\left(\mathfrak{s}_{Y_{1}}\right)$ is torsion. Then we can pick $A_{Y_{1}}$ such that $A_{Y_{1}}^{t}$ is also flat. Hence $F_{A_{b, T}^{t}}$ is supported in $W_{01, b} \cup W_{12, b}$.

Because ( $\omega_{12}, g_{W_{12}}$ ) is admissible, there exists an embedded surface $\Sigma$ in $W_{12}$ such that $\Sigma \cdot \Sigma \geqslant 0$ and that
$$\int_{W_{12, b}}\left(\mathrm{i} F_{A_{b, T}^{t}}^{+}+\omega_{12}\right) \wedge \kappa_{\Sigma}>0 .$$
Here $\kappa_{\Sigma}$ is the square integrable, harmonic 2-form on $W_{12}^{*}$ that corresponds to the image of $[\Sigma]$ under the map
$$H_{2}\left(W_{12} ; \mathbb{R}\right) \xrightarrow{\mathrm{PD}} H^{2}\left(W_{12}, \partial W_{12} ; \mathbb{R}\right) \rightarrow H^{2}\left(W_{12} ; \mathbb{R}\right) .$$
Similarly, we can treat $\Sigma$ as a surface in $W(T)_{b}$ and consider the corresponding harmonic two form $\kappa_{\Sigma, b, T}$ on $W(T)_{b}^{*}$. As $T$ goes to infinity, both norms
$$\left\|\left.\kappa_{\Sigma, b, T}\right|_{W_{01, b}}\right\|_{L^{2}} \text { and }\left\|\left.\kappa_{\Sigma, b, T}\right|_{W_{12, b}}-\left.\kappa_{\Sigma}\right|_{W_{12, b}}\right\|_{L^{2}}$$
converge to zero uniformly in $b$. Therefore, when $T$ is large enough, we have
$$\int_{W(T)_{b}^{*}}\left(\mathrm{i} F_{A_{b, T}^{t}}^{+}+\omega_{12}\right) \wedge \kappa_{\Sigma, b, T}=\int_{W_{01, b}} \mathrm{i} F_{A_{b, T}^{t}}^{+} \wedge \kappa_{\Sigma, b, T}+\int_{W_{12, b}}\left(\mathrm{i} F_{A_{b, T}^{t}}^{+}+\omega_{12}\right) \wedge \kappa_{\Sigma, b, T}>0$$
for any $b \in \mathcal{Q}$. This implies that $\left(g_{\widetilde{W}(0, T)}, \omega_{12}\right)$ is admissible. By Lemma 2.4, the corresponding chamber is the canonical chamber.

Next we assume $c_{1}\left(\mathfrak{s}_{Y_{1}}\right)$ is nontorsion. Then there exists an embedded surface $\Sigma^{\prime}$ in $Y_{1}$ such that $\left\langle c_{1}\left(\mathfrak{s}_{Y_{1}}\right),\left[\Sigma^{\prime}\right]\right\rangle>0$. We let $\kappa_{\Sigma^{\prime}, b, T}$ be the square integrable harmonic 2-form on $W(T)_{b}^{*}$ that corresponds to $\operatorname{PD}\left(\left[\Sigma^{\prime}\right]\right)$. Then as $T \rightarrow \infty$, we have
$$\left\|\left.\kappa_{\Sigma^{\prime}, b, T}\right|_{W_{01, b} \cup W_{12, b}}\right\|_{L^{2}} \rightarrow 0, \quad\left\|\left.\kappa_{\Sigma^{\prime}, b, T}\right|_{[-T, T] \times Y_{1}}-\frac{d t \wedge \alpha}{2 T}\right\|_{L^{2}} \rightarrow 0 .$$
Here $\alpha$ is the harmonic 1-form on $Y_{1}$ that represents the Poincare dual of $\Sigma^{\prime}$. Therefore, we have
$$\int_{W(T)_{b}^{*}}\left(\mathrm{i} F_{A_{b, T}^{t}}^{+}+\omega_{12}\right) \wedge \kappa_{\Sigma^{\prime}, b, T} \rightarrow \frac{1}{4 T} \int_{[-T, T] \times Y_{1}} \mathrm{i}\left(F_{A_{Y_{1}}^{t}}+* F_{A_{Y_{1}}^{t}}\right) \cup(d t \wedge \alpha)=\frac{c_{1}\left(\mathfrak{s} Y_{1}\right)\left[\Sigma^{\prime}\right]}{2}>0 .$$
Rest of proof proceeds similarly. \(\square\)

We take a pair of critical points
$$\begin{aligned}
& \mathfrak{a} \in \mathfrak{C}^{o}\left(Y_{0}, \mathfrak{s}_{Y_{0}}\right) \cup \mathfrak{C}^{u}\left(Y_{0}, \mathfrak{s}_{Y_{0}}\right), \\
& \mathfrak{b} \in \mathfrak{C}^{o}\left(Y_{2}, \mathfrak{s}_{Y_{2}}\right) \cup \mathfrak{C}^{s}\left(Y_{2}, \mathfrak{s}_{Y_{2}}\right) .
\end{aligned}$$
and a homotopy class
$$z \in \pi_{0}\left(\mathcal{B}^{\sigma}\left([\mathfrak{a}], \widetilde{W}_{02}^{*}, \mathfrak{s},[\mathfrak{b}]\right) .\right.$$
Then we consider the parametrized moduli space
$$\mathcal{M}_{T, z}([\mathfrak{a}],[\mathfrak{b}])=\bigcup_{S \in[0,+\infty)}\{S\} \times \mathcal{M}_{z}\left([\mathfrak{a}], \widetilde{W}(S, T)^{*},[\mathfrak{b}]\right)$$

Lemma 4.25. For any $\mathfrak{s} \in \mathbb{S}$, there exists $T_{\mathfrak{s}, 1} \gg 0$ such that for all $T \geqslant T_{\mathfrak{s}, 1}$, the moduli space $\mathcal{M}_{T, z}([\mathfrak{a}],[\mathfrak{b}])$ has no reducible for any $\mathfrak{a}, \mathfrak{b}$ and $z \in \pi_{0}\left(\mathcal{B}^{\sigma}\left([\mathfrak{a}], \widetilde{W}_{02}^{*}, \mathfrak{s},[\mathfrak{b}]\right)\right.$.

Proof. This lemma is a family version of [19, Lemma 27.3.5] and it follows directly from Lemma 4.24. \(\square\)

We fix a choice of $T_{\mathfrak{s}} \geqslant \max \left(T_{0, \mathfrak{s}}, T_{1, \mathfrak{s}}\right)$. Using these new moduli spaces $\mathcal{M}_{T, z}([\mathfrak{a}],[\mathfrak{b}])$, we define operators $K_{o}^{o}, K_{s}^{o}, K_{s}^{u}, K_{o}^{u}$ exactly as in in (46). We then define the operator
$$\vec{K}_{\mathfrak{s}}=\left[\begin{array}{ll}
K_{o}^{o} & K_{s}^{o} \\
K_{o}^{u} & K_{s}^{u}
\end{array}\right]: \quad \widehat{C}_{*}\left(Y_{0}, \mathfrak{s}_{Y_{0}}\right) \rightarrow \check{C}_{*}\left(Y_{2}, \mathfrak{s}_{Y_{2}}\right) .$$
There is no need for completion in this case because the rational gradings of the generators of $\breve{C}_{*}\left(Y_{2}, \mathfrak{s}_{Y_{2}}\right)$ are bounded below.

Using the perturbations over $S=\infty$, we define the map
$$\widehat{m}_{01}: \widehat{C}_{*}\left(Y_{0}, \mathfrak{s}_{Y_{0}}\right) \rightarrow \widehat{C}_{*}\left(Y_{1}, \mathfrak{s}_{Y_{1}}\right)$$
for the family cobordisms $\left(\widetilde{W}_{01}, \mathfrak{s}_{\widetilde{W}_{01}}\right)$, and the map
$$\vec{m}_{12}: \widehat{C}_{*}\left(Y_{1}, \mathfrak{s}_{Y_{1}}\right) \rightarrow \check{C}_{*}\left(Y_{2}, \mathfrak{s}_{Y_{2}}\right)$$
for the single cobordism $\left(W_{12}, \mathfrak{s}_{W_{02}}\right)$. Using the perturbations over $S=0$, we define the map
$$\vec{m}_{02, \mathfrak{s}}: \widehat{C}_{*}\left(Y_{0}, \mathfrak{s}_{Y_{0}}\right) \rightarrow \check{C}_{*}\left(Y_{2}, \mathfrak{s}_{Y_{2}}\right)$$
for the family cobordism $\left(\widetilde{W}_{02}, \mathfrak{s}\right)$ with any $\mathfrak{s} \in \mathbb{S}$. We set
$$\vec{m}_{02, \mathbb{S}}=\sum_{\mathfrak{s} \in \mathbb{S}} \vec{m}_{02, \mathfrak{s}} \quad \text { and } \quad \vec{K}_{\mathbb{S}}=\sum_{\mathfrak{s} \in \mathbb{S}} \vec{K}_{\mathfrak{s}} .$$

The following proposition can be proved by modifying the proof of [19, formula (27.7)] in a similar way as last subsection.

Proposition 4.26. We have $-\vec{K}_{\mathbb{S}} \circ \hat{\partial}-\check{\partial}_{\circ} \vec{K}_{\mathbb{S}}+\vec{m}_{02, \mathbb{S}}+\vec{m}_{12} \circ \hat{m}_{01}=0$.
Suppose either $\mathfrak{s}_{Y_{0}}$ or $\mathfrak{s}_{Y_{2}}$ is non-torsion. Then there is no chamber structure in defining $\overrightarrow{H M}_{*}\left(\widetilde{W}_{02}, \mathfrak{s}\right)$. So Proposition 4.26 directly implies Theorem 4.22 (1).

Suppose $\mathfrak{s}_{Y_{0}}$ and $\mathfrak{s}_{Y_{2}}$ are both torsion. By Lemma 4.24, the operator $\vec{m}_{02, \mathfrak{s}}$ corresponds to the canonical chamber $\xi_{c}$ and thus induces the map $\overrightarrow{H M}_{*}\left(\widetilde{W}_{02}, \mathfrak{s}\right)$. So Proposition 4.26 again implies Theorem 4.22 (1).
4.3. A computation of some cobordism-induced maps. Computing the cobordism induced maps $\widehat{H M}_{*}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right)$ and $\widetilde{H M}_{*}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right)$ are difficult in general. But $\overline{H M}_{*}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right)$ is much easier to handle because it only involves counting reducible solutions. For the same reason, $\overline{H M}_{*}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right)$ contains significant less amount of information about the cobordism $\widetilde{W}$. However, when $Y_{0}, Y_{1}$ are $L$-spaces, $\overline{H M}_{*}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right)$ actually determines $\widehat{H M}_{*}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right)$ and $\widetilde{H M}_{*}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right)$ through the exact sequence (21). The main result of this section (Theorem 4.32) computes the map $\widehat{H M}_{*}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right)$ in this situation.

We start by stating the assumptions imposed in the current section:
Assumption 4.27. Let $Y_{0}$ and $Y_{1}$ be two rational homology 3-spheres and let $\widetilde{W} / \mathcal{Q}$ be a family cobordism from $Y_{0}$ to $Y_{1}$. We assume that $\widetilde{W} / \mathcal{Q}$ is a homology product and the fiber $W$ satisfies $b_{1}(W)=0$. Let $\mathfrak{s}_{\widetilde{W}}$ be a family spin ${ }^{c}$ structure on $\widetilde{W}$ which is a product near the boundary.

We consider the cobordism induced map
$$\overline{H M}_{*}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right): \overline{H M}_{*}\left(Y_{0}, \mathfrak{s}_{Y_{0}}\right) \rightarrow \overline{H M}_{*}\left(Y_{1}, \mathfrak{s}_{Y_{1}}\right) .$$
We use $\bar{e}_{k}^{i}$ to denote the canonical generator of $\overline{H M}_{*}\left(Y_{i}, \mathfrak{s}_{Y_{i}}\right)$ with rational grading $k$. It is given by a reducible critical point $\left[\left(B_{i}, 0, \psi_{*}^{i}\right)\right]$. (See Notation 3.1.)

In what follows, we will use $\operatorname{Ind}\left\{P_{*}\right\} \in K^{0}(\mathcal{Q})$ to denote the virtual index bundle of a family of complex Fredholm operator $\left\{P_{b}\right\}_{b \in \mathcal{Q}}$ and use ind $\in \mathbb{Z}$ to denote the complex numerical index of a single operator $P$.

Proposition 4.28. Under Assumption 4.27, we have the following results.
\begin{itemize}
\item[(1)] Suppose $b_{2}^{+}(W)>0$. Then $\overline{H M}_{*}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right)$ is trivial.
\item[(2)] Suppose $\operatorname{dim} \mathcal{Q}$ is odd. Then $\overline{H M}_{*}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right)$ is trivial.
\item[(3)] Suppose $b_{2}^{+}(W)=0$ and $\operatorname{dim} \mathcal{Q}$ is even. Then we have
$$\overline{H M}_{*}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right)\left(\bar{e}_{n}^{0}\right)=c_{\frac{\operatorname{dim} \mathcal{Q}}{2}}\left(-\operatorname{Ind}\left\{\not D_{A_{b}^{0}, \hat{q}_{b}}^{+}\left(W_{b}\right)\right\}\right)[\mathcal{Q}] \cdot \bar{e}_{n+d}^{1},$$
\end{itemize}
where
$$d=\frac{c_{1}\left(\mathfrak{s}_{W}\right)^{2}-\sigma(W)}{4}+\operatorname{dim} \mathcal{Q},$$
and $\left\{\not D_{A_{b}, \hat{q}_{b}}^{+}\left(W_{b}\right)\right\}$ denotes the family perturbed Dirac operator
$$\not D_{A_{b}^{0}, \hat{\mathfrak{q}}_{b}}^{+}: L_{k}^{2}\left(W_{b}^{*}, S^{+}\right) \rightarrow L_{k-1}^{2}\left(W_{b}^{*}, S^{-}\right) \quad \text { for } \quad b \in \mathcal{Q},$$
as defined in (28). Here we choose any smooth family $\left\{A_{b}^{0}\right\}_{b \in \mathcal{Q}}$ of $\operatorname{spin}^{c}$ connections on $\widetilde{W}^{*}$ that equals the pull back of $B_{0}$ and $B_{1}$ on the cylindrical ends.

To prove Proposition 4.28, we start with some general discussions in index theory. Consider a smooth family of Fredholm operator $\left\{P_{b}: H_{1} \rightarrow H_{2}\right\}_{b \in \mathcal{Q}}$ between Hilbert spaces. They together give a map
$$\widetilde{P}: \mathcal{Q} \times H_{1} \rightarrow H_{2} .$$
Suppose we have
$$\operatorname{2ind}\left(P_{b}\right)=2-\operatorname{dim} \mathcal{Q}$$
and suppose $\overrightarrow{0}$ is a regular value of $\widetilde{P}$. Then for any $b \in \mathcal{Q}$, the composition
$$L_{b}: T_{b} \mathcal{Q} \xrightarrow{\mathcal{D}_{(b, 0)}} H_{2} \xrightarrow{\text { projection }} \text { coker } P_{b}$$
is surjective. This implies the inequality
$$\operatorname{dim} \mathcal{Q} \geqslant \operatorname{dim} \operatorname{coker} P_{b}=\operatorname{dim} \operatorname{ker} P_{b}-2 \operatorname{ind}\left(P_{b}\right) .$$
Therefore, the complex dimension of $\operatorname{ker} P_{b}$ is either 0 or 1 . When $\operatorname{ker} P_{b}$ is 1 -dimensional, the map $L_{b}$ is an isomorphism. For such $b$, we assign it with a positive sign if $L_{b}$ sends the orientation on $T_{b} \mathcal{Q}$ to the complex orientation of coker $P_{b}$ and a negative sign otherwise.

Lemma 4.29. The number of $b \in Q$ such that $\operatorname{ker} P_{b} \neq 0$, when counted with sign specified above, equals $c_{\frac{\operatorname{dim} \mathcal{Q}}{2}}\left(-\operatorname{Ind}\left\{P_{*}\right\}\right)[\mathcal{Q}]$.
Proof. By compactness of $\mathcal{Q}$, we can find a finite dimensional subbundle $F$ of $H_{2}$ such that $P_{b}$ is transverse to $F$ for every $b$. Then $E:=\widetilde{P}^{-1}(F)$ is a finite dimensional sub-bundle of $\mathcal{Q} \times H_{1}$. By enlarging $F$ if necessary, we may assume that $E$ is a trivial bundle $\mathbb{C}^{N}$. The restriction $\left.\widetilde{P}\right|_{E}$ defines sections $s_{1}, s_{2}, \cdots, s_{N}$ of $F$. Note that $\operatorname{ker} P_{b} \neq 0$ if and only if $\operatorname{ker}\left(\left.\widetilde{P}\right|_{E}\right)_{b} \neq 0$ and this happens exactly when $s_{1}, \cdots, s_{N}$ are linearly dependent at $b$. By the classical obstruction theoretic definition of Chern class, the number of such $b$ equals $c_{\operatorname{dim}(F)+1-N}(F)[\mathcal{Q}]$. The proof is finished by observing that
$$\left[-\operatorname{Ind}\left\{P_{*}\right\}\right]=\left[F-\underline{\mathbb{C}}^{N}\right] \in K^{0}(\mathcal{Q}) .$$ \(\square\)

Proof of Proposition 4.28. (1) Suppose $b_{2}^{+}(W)>0$. Then there exists a family of self-dual 2-forms $\left\{\omega_{b}\right\}_{b \in \mathcal{Q}}$ supported in the interior of $W_{b}$ such that $\left\{g_{\widetilde{W} / \mathcal{Q}},\left\{\omega_{b}\right\}\right\}$ is admissible with respect to $\mathfrak{s}_{\widetilde{W}}$. By Lemma 4.7, the perturbed Seiberg-Witten equations has no reducible solutions. Therefore, the map $\overline{H M}_{*}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right)$ is trivial.
(2) Suppose $\mathcal{Q}$ is odd dimensional. By (1), we may also assume $b_{2}^{+}(W)=0$. Then for any pair of reducible critical points $[\mathfrak{a}]$ and $[\mathfrak{b}]$ on $Y_{0}$ and $Y_{1}$. Dimension of the moduli space $\mathcal{M}^{\text {red }}\left([\mathfrak{a}], \widetilde{W}^{*},[\mathfrak{b}]\right)$ equals the sum of $\operatorname{dim} \mathcal{Q}$ and the index of the linearized Seiberg-Witten operators. Since $b_{1}(W)=b_{2}^{+}(W)=0$, the curvature equation doesn't contribute to the index and the index is an even number because the Dirac operator is complex linear. Therefore, when $\mathcal{Q}$ is odd-dimensional, this moduli space can never be 0-dimensional. Hence the the map $\overline{H M}_{*}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right)$ is trivial.
(3) Now suppose $\mathcal{Q}$ is even-dimensional and $b_{2}^{+}(W)=0$. Let $\left[\left(B_{0}, 0, \psi_{j_{0}}^{0}\right)\right]$ and $\left[\left(B_{1}, 0, \psi_{j_{1}}^{1}\right)\right]$ be the critical points that give $\bar{e}_{n}^{0}$ and $\bar{e}_{n+d}^{1}$ respectively. Since the map $\overline{H M}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right)$ increase the rational grading by $d$ (see [19, (28.3)]), the moduli space
$$\mathcal{M}^{\mathrm{red}}:=\mathcal{M}^{\mathrm{red}}\left(\left[\left(B_{0}, 0, \psi_{j_{0}}^{0}\right)\right], \widetilde{W}^{*}, \mathfrak{s}_{\widetilde{W}},\left[\left(B_{1}, 0, \psi_{j_{1}}^{1}\right)\right]\right)$$
is an oriented 0-dimensional manifold and we have
$$\overline{H M}_{*}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right)\left(\bar{e}_{n}^{0}\right)=\# \mathcal{M}^{\text {red }} \cdot \bar{e}_{n+d}^{1} .$$
Because $b_{1}(W)=b_{2}^{+}(W)=0$, on each fiber $W_{b}^{*}$, the curvature equation $F_{A^{t}}^{+}=i \omega_{b}$ has a unique solution that converges to $B_{0}$ and $B_{1}$ on the two ends. Therefore, by choosing the perturbations $\mathfrak{q}_{i}$ and $\mathfrak{q}_{i}^{\prime}$ small enough, we may assume that for any $b \in \mathcal{Q}$, the the perturbed Seiberg-Witten equations on $W_{b}^{*}$ has a unique finite energy downstairs reducible solution $\left[\left(A_{b}, 0\right)\right]$ up to gauge transformation. Upstairs, a reducible solution of the blown-up Seiberg-Witten equations is given by $\left[\left(A_{b}, \phi, 0\right)\right]$, where $\phi$ is a nonzero local- $L_{k}^{2}$ spinor that satisfies the perturbed Dirac equation $\not D_{A_{b}, \hat{q}_{b}}^{+}(\phi)=0$. (See formula (28).)

To discuss the when $\left[\left(A_{b}, \phi, 0\right)\right]$ limits to $\left[\left(B_{i}, 0, \psi_{j_{i}}^{i}\right)\right]$ on the two ends, we consider the weighted Sobolev norm for a spinor $\psi$ on $W_{b}^{*}$ :
$$\|\psi\|_{L_{p, \lambda, \lambda^{\prime}}^{2}}:=\sqrt{\sum_{i=0}^{p}\left\|\nabla_{A_{b}}^{(p)} \tau \cdot \psi\right\|_{L^{2}}^{2}} .$$
Here $\lambda, \lambda^{\prime} \in \mathbb{R}$ are two real numbers. And $\tau_{\lambda, \lambda^{\prime}}: W_{b}^{*} \rightarrow \mathbb{R}^{>0}$ is a smooth function that satisfies
$$\tau_{\lambda, \lambda^{\prime}}(x, t)= \begin{cases}e^{-\lambda t} & \text { if }(x, t) \in(-\infty, 0] \times Y_{0} \\ e^{\lambda^{\prime} t} & \text { if }(x, t) \in[0, \infty) \times Y_{1} .\end{cases}$$

On cylindrical ends, the equation $\not D_{A_{b}, \hat{q}_{b}}^{+}(\phi)=0$ can be written as
$$\frac{d}{d t} \varphi(t)+\not D_{B_{i}(t), \mathfrak{q}_{i}} \varphi(t)=0,$$
where $B_{i}(t)=\left.A_{b}\right|_{\{t\} \times Y_{i}}$ and $\varphi(t)=\left.\phi\right|_{\{t\} \times Y_{i}}$. Using the spectral decomposition for $\not D_{B_{i}(t), \mathfrak{q}_{i}}$, one can prove that upstairs, $\left[\left(A_{b}, \phi, 0\right)\right]$ converges to $\left[\left(B_{0}, 0, \psi_{j}^{0}\right)\right]$ and $\left[\left(B_{1}, 0, \psi_{j^{\prime}}^{1}\right)\right]$ for some $j \leqslant j_{0}$ and $j^{\prime} \geqslant j_{1}$ if and only if
$$\phi \in L_{k,-\lambda_{j_{0}}-\epsilon, \lambda_{j_{1}}-\epsilon}^{2}\left(W_{b}^{*}\right) .$$

Here $\epsilon$ can be any positive number small enough. (See [19, Proposition 14.6.1] for a similar argument on the cylinder $\mathbb{R} \times Y$.) However, for any $j \leqslant j_{0}$ and any $j^{\prime} \geqslant j_{1}$, the moduli space
$$\mathcal{M}^{\text {red }}\left(\left[\left(B_{0}, 0, \psi_{j}^{0}\right)\right], \widetilde{W}^{*},\left[\left(B_{1}, 0, \psi_{j^{\prime}}^{1}\right)\right]\right)$$
has a negative expected dimension unless both equality are achieved. By our transversality assumption, these moduli spaces are all empty. So $\left[\left(A_{b}, 0, \phi\right)\right]$ belongs to $\mathcal{M}^{\text {red }}$ if and only if $\phi$ is a nonzero vector in the kernel of the operator
$$\not D_{A_{b}, \hat{\mathfrak{q}}_{b}}^{+}: L_{k,-\lambda_{j_{0}}-\epsilon, \lambda_{j_{1}}-\epsilon}\left(W_{b}^{*} ; S^{+}\right) \rightarrow L_{k-1,-\lambda_{j_{0}}-\epsilon, \lambda_{j_{1}}-\epsilon}^{2}\left(W_{b}^{*} ; S^{-}\right) \quad \text { for } \quad b \in \mathcal{Q} .$$
This leads to our explicit description of the moduli space
$$\mathcal{M}^{\mathrm{red}} \cong \bigcup_{b \in \mathcal{Q}} \mathbb{P}\left(\operatorname{ker} \not D_{A_{b}, \hat{\mathrm{q}}_{b}}^{+}\right)$$
where $\mathbb{P}(\cdot)$ denotes the associated complex project space. (Note that $\left(A_{b}, 0, \phi\right)$ and $\left(A_{b}, 0, \phi^{\prime}\right)$ are gauge equivalent if $\phi=z \phi^{\prime}$ for some $z \neq 0$.)

At a point $\left[\left(A_{b}, 0, \phi\right)\right] \in \mathcal{M}^{\text {red }}$, deformation of the moduli space is controlled by the Fredholm operator
$$\begin{array}{r}
R: T_{b} \mathcal{Q} \oplus L_{k,-\lambda_{j_{0}}-\epsilon, \lambda_{j_{1}}-\epsilon}^{2}\left(W_{b}^{*} ; S^{+}\right) \rightarrow L_{k-1,-\lambda_{j_{0}}-\epsilon, \lambda_{j_{1}}-\epsilon}^{2}\left(W_{b}^{*} ; S^{+}\right) \oplus \mathbb{C} \\
(\vec{v}, \psi) \mapsto\left(\mathcal{D}_{(b, \phi)} \not D_{A_{b}, \hat{q}_{b}}^{+}(\vec{v}, \psi), \int_{W_{b}^{*}} \tau^{2}\langle\psi, \phi\rangle d \mathrm{vol}\right)
\end{array}$$
Since $\mathcal{M}^{\text {red }}$ is regular and 0-dimensional, we see that $R$ is surjective and has index 0. This implies that the family of Dirac operators $\left\{\not D_{A_{b}, \hat{\mathfrak{q}}_{b}}^{+}\right\}_{b \in \mathcal{Q}}$ in (52) satisfies the condition of Lemma 4.29. As a result, we get
$$\# \mathcal{M}^{\text {red }}=c_{\frac{\operatorname{dim} \mathcal{Q}}{2}}\left(-\operatorname{Ind}\left\{\not D_{A_{b}, \hat{\mathrm{q}}_{b}}^{+}\right\}\right)[\mathcal{Q}] .$$
The proof is completed by the following lemma. \(\square\)

Lemma 4.30. The index bundles of the families (51) and (52) differ from each other by a trivial bundle over $\mathcal{Q}$. Hence they have the same Chern class.

Proof. We first deform the connection $A_{b}$ to the connection $A_{b}^{0}$ via the linear homotopy
$$A_{b}^{s}:=s \cdot A_{b}+(1-s) \cdot A_{b}^{0}, \quad s \in[0,1] .$$
Note that for any $s$, the restrictions $\left.A_{b}^{s}\right|_{t \times Y_{1}}$ and $\left.A_{b}^{s}\right|_{-t \times Y_{0}}$ limits to $B_{1}$ and $B_{0}$ respectively. Since $\lambda_{j_{i}} \pm \epsilon$ is not an eigenvalue of the Dirac operator $\not D_{B_{i}, \mathfrak{q}_{i}}$. For any $s \in[0,1]$ and $b \in \mathcal{Q}$, the operator
$$\not D_{A_{b}^{s}, \hat{q}_{b}}^{+}: L_{k,-\lambda_{j_{0}}-\epsilon, \lambda_{j_{1}}-\epsilon}^{2}\left(W_{b}^{*} ; S^{+}\right) \rightarrow L_{k-1,-\lambda_{j_{0}}-\epsilon, \lambda_{j_{1}}-\epsilon}^{2}\left(W_{b}^{*} ; S^{-}\right)$$
is Fredholm. By invariance of the index bundle under continuous deformation, we see that (52) has the same index bundle as the family
$$\not D_{A_{b}^{0}, \hat{q}_{b}}^{+}: L_{k,-\lambda_{j_{0}}-\epsilon, \lambda_{j_{1}}-\epsilon}^{2}\left(W_{b}^{*} ; S^{+}\right) \rightarrow L_{k-1,-\lambda_{j_{0}}-\epsilon, \lambda_{j_{1}}-\epsilon}^{2}\left(W_{b}^{*} ; S^{-}\right) \quad \text { for } \quad b \in \mathcal{Q} .$$

The only difference (51) and (53) is that we are using different weights on the Sobolev spaces. To compare their index bundles, we consider the following four Dirac operators, treated as trivial family over $\mathcal{Q}$ :
$$\begin{aligned}
\not D_{\hat{B}_{0}, \hat{\mathfrak{q}}_{0}}^{+}: L_{k,-\lambda_{j_{0}}-\epsilon, 0}^{2}\left(\mathbb{R} \times Y_{0} ; S^{+}\right) & \rightarrow L_{k-1,-\lambda_{j_{0}}-\epsilon, 0}^{2}\left(\mathbb{R} \times Y_{0} ; S^{-}\right) \\
\not D_{\hat{B}_{0}, \hat{\mathfrak{q}}_{0}}^{+}: L_{k, 0,0}^{2}\left(\mathbb{R} \times Y_{0} ; S^{+}\right) & \rightarrow L_{k-1,0,0}^{2}\left(\mathbb{R} \times Y_{0} ; S^{-}\right) \\
\not D_{\hat{B}_{1}, \hat{\mathfrak{q}}_{1}}^{+}: L_{k, 0, \lambda_{j_{1}}-\epsilon}^{2}\left(\mathbb{R} \times Y_{1} ; S^{+}\right) & \rightarrow L_{k-1,0, \lambda_{j_{1}}-\epsilon}^{2}\left(\mathbb{R} \times Y_{1} ; S^{-}\right) \\
\not D_{\hat{B}_{1}, \hat{\mathfrak{q}}_{1}}^{+}: L_{k, 0,0}^{2}\left(\mathbb{R} \times Y_{1} ; S^{+}\right) & \rightarrow L_{k-1,0,0}^{2}\left(\mathbb{R} \times Y_{1} ; S^{-}\right)
\end{aligned}$$
Here $\hat{B}_{i}$ and $\hat{\mathfrak{q}}_{i}$ are 4-dimensional connection and perturbation pulled back from $B_{i}$ and $\mathfrak{q}_{i}$ respectively. By the excision theorem of index, we see that the direct sum of the index bundles for the families (53), (55) and (57) equals the corresponding bundle for the families (51), (54) and (56). This shows that the index bundles of the families (51) and (53) differ from each other by a linear combination of index bundles of (54) and (55), (56) and (57), which are all trivial bundles over $\mathcal{Q}$. This finishes the proof. \(\square\)

In practical, it's convenient to convert the index bundle of the family (51) into a family of Dirac operators on closed 4-manifolds, so that one can apply the Atiyah-Singer index theorem. The following lemma can be proved similarly as Lemma 4.30 using the excision principle of indices.
Lemma 4.31. For $i=0,1$, let $\left(M_{i}, \mathfrak{s}_{M_{i}}\right)$ a be spin ${ }^{c}$ 4-manifold bounded by $\left(Y_{i}, \mathfrak{s}_{Y_{i}}\right)$. Consider the new family of closed spin ${ }^{c}$ 4-manifolds $\left(\widetilde{W}^{\prime}, \mathfrak{s}_{\widetilde{W}^{\prime}}\right)$ obtained by gluing together $\widetilde{W}, M_{0} \times \mathcal{Q}$ and $-M_{1} \times \mathcal{Q}$. Then the index bundle of the family Dirac operators
$$\not D_{A_{b}^{\prime}}^{+}\left(W_{b}^{\prime}, \mathfrak{s}_{W_{b}^{\prime}}\right): L_{k}^{2}\left(W_{b}^{\prime} ; S^{+}\right) \rightarrow L_{k-1}^{2}\left(W_{b}^{\prime} ; S^{-}\right) \quad \text { for } b \in \mathcal{Q}$$
differ from the index bundle of the family (51) by a trivial bundle and hence have the same Chern classes. Here we can choose any smooth family of base connection $\left\{A_{b}^{\prime}\right\}$ on $W_{b}^{\prime}$.

Now we state and proof the main result of this section.
Theorem 4.32. Let $\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right)$ be a $\operatorname{spin}^{c}$-family cobordism from $S^{3}$ to an $L$-space $Y$ which satisfies Assumption (4.27). Let $\widehat{1}$ be the standard generator of $\widehat{H M}_{*}\left(S^{3}\right)$ as a $\mathbb{Q}[U]$ -module. Then one has
$$\widehat{H M}_{*}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right)(\hat{1})=\left\langle c_{\frac{\operatorname{dim} \mathcal{Q}}{2}}\left(-\operatorname{Ind}\left\{\not D_{A_{b}^{0}, \hat{\mathfrak{q}}_{b}}^{+}\left(W_{b}\right)\right\}\right),[\mathcal{Q}]\right\rangle \cdot \hat{e}_{d-1}$$
if $\operatorname{dim} \mathcal{Q}$ is even and $b_{2}^{+}(\widetilde{W})=0$. Otherwise, $\widehat{H M}_{*}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right)(\widehat{1})=0$.
Proof. We set $Y_{0}=S^{3}$ and $Y_{1}=Y$. Cobordism induced maps are compatible with the exact sequence (21). In particular, we have
$$p_{*, Y} \circ \widehat{H M}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right)=\overline{H M}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right) \circ p_{*, S^{3}} .$$
First, we assume that $\operatorname{dim} \mathcal{Q}$ is odd or $b_{2}^{+}(\widetilde{W})>0$. By Proposition 4.28, the map $\overline{H M}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right)$ is trivial. Since $Y$ is an $L$-space, the map $p_{*, Y}$ is injective. So $\widehat{H M}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right)$ is trivial as well.

Next, we assume that $\operatorname{dim} \mathcal{Q}$ is even, $b_{2}^{+}(\widetilde{W})=0$, and $-2 h\left(Y, \mathfrak{s}_{Y}\right)<d-1$. Since $\operatorname{gr}^{\mathbb{Q}}(\widehat{1})=-1$ and $\widehat{H M}_{*}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right)$ increases the rational grading by $d$, we have
$$\operatorname{gr}^{\mathbb{Q}}\left(\widehat{H M}_{*}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right)(\widehat{1})\right)=d-1 .$$
Since $Y$ is an $L$-space, $\widehat{H M}_{*}\left(Y, \mathfrak{s}_{Y}\right)$ is supported in $\operatorname{gr}^{\mathbb{Q}}$-grading $\leqslant-2 h\left(Y, \mathfrak{s}_{Y}\right)$. Therefore, $\widehat{H M}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right)_{*}(\widehat{1})=0$. On the other hand, by (59) and the fact that $p_{*, S^{3}}$ is injective. We conclude that the map $\overline{H M}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right)$ is trivial as well. By Proposition 4.28, this implies $c_{\frac{\operatorname{dim} \mathcal{Q}}{2}}\left(-\operatorname{Ind}\left\{\not D_{A_{b}^{0}, \hat{q}_{b}}^{+}\left(W_{b}\right)\right\}\right)[\mathcal{Q}]=0$. So in this case, both sides of (58) are zero.

Lastly, we assume $\operatorname{dim} \mathcal{Q}$ is even, $b_{2}^{+}(\widetilde{W})=0$, and $-2 h\left(Y, \mathfrak{s}_{Y}\right) \geqslant d-1$. Then we have $\widehat{H M}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right)_{*}(\widehat{1})=x \cdot \hat{e}_{d-1}(Y)$ for some constant $x$. Note that $p_{*, S^{3}}(\widehat{1})=\bar{e}_{-2}^{0}$ and $p_{*, Y}\left(\widehat{e}_{d-1}(Y)\right)=\bar{e}_{d-2}^{1}$. By (59), we have
$$\overline{H M}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right)\left(\bar{e}_{-2}^{0}\right)=x \cdot \bar{e}_{d-2}^{1}$$
By Proposition 4.28, we see that $x=c_{\frac{\operatorname{dim} \mathcal{Q}}{2}}\left(-\operatorname{Ind}\left\{\not D_{A_{b}^{0}, \hat{q}_{b}}^{+}\left(W_{b}\right)\right\}\right)[\mathcal{Q}]$. This proves the last case. \(\square\)

\section*{5. A Gluing theorem for the family Seiberg-Witten invariant}

In this section, we prove Theorem L. This is a gluing formula which expresses the family Seiberg-Witten invariants in terms of Floer theoretic data. Then we prove Theorem M, which relates the Seiberg-Witten invariants for certain families with the corresponding invariant for their fibers. This formula will be the main tool in our applications.
5.1. Expressing family Seiberg invariants using cobordism induced maps. Let $\widetilde{M} / \mathcal{Q}$ be a smooth family of closed 4-manifolds which is a homology product. Let $\tau_{i}$ : $\mathcal{Q} \rightarrow \widetilde{M}(i=0,1)$ be two disjoint smooth sections. We assume the vertical tangent bundle $T \widetilde{M} / \mathcal{Q}$ is trivial when restricted to the image of $\tau_{i}$ and we fix a trivilization. Let $\widetilde{W} / \mathcal{Q}$ be the family of 4-manifolds with boundary, obtained by removing tubular neighborhoods of $\tau_{i}(\mathcal{Q})$. Then we can identity components $\partial \widetilde{W}$ with the unit sphere bundles of $\left.(T \widetilde{M} / \mathcal{Q})\right|_{\tau_{i}(Q)}$. Using the trivializations we chose, we get a natural boundary parametrization of $\widetilde{W}$, making it into a family of cobordism from $S^{3}$ to $S^{3}$. Let $\widetilde{\mathfrak{s}}$ be a family spin ${ }^{c}$ structure on $\widetilde{M}$. We assume that $\widetilde{\mathfrak{s}}$ is the trivial spin ${ }^{c}$ structure when restricted to $\tau_{i}(\mathcal{Q})$, then $\mathfrak{s}_{\widetilde{W}}$ (the restriction of $\widetilde{\mathfrak{s}}$ to $\widetilde{W}$ ) will satisfy Assumption 4.27. Hence we can talk about cobordism induced maps.

Theorem 5.1. Suppose $d(\widetilde{\mathfrak{s}}, \widetilde{M})=0$. Then for any chamber $\xi \in\left[\mathcal{Q}, V^{+}(W)\right]$, we have the formula
$$\operatorname{FSW}_{\xi}(\widetilde{M}, \widetilde{\mathfrak{s}})=\left\langle\overrightarrow{H M}_{*}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right)_{\xi}(\widehat{1}), \check{1}\right\rangle .$$
Here $\widehat{1}$ and $\check{1}$ denotes the standard generator of $\widehat{H M}_{*}\left(S^{3}\right) \cong \mathbb{Q}[U]$ and $\widetilde{H M}^{*}\left(S^{3}\right) \cong \mathbb{Q}[U]$ respectively, and $\langle-,-\rangle$ denotes the natural pairing (20).

Proof. This is a family version of [19, Proposition 27.4.1]. It is essentially a neck-stretching argument. For any $T>0$, we consider a decomposition of $\widetilde{M}$ into five pieces
$$\widetilde{M}_{T}:=\left(B^{4} \times \mathcal{Q}\right) \cup\left(S^{3} \times[-T, 0] \times \mathcal{Q}\right) \cup \widetilde{W} \cup\left(S^{3} \times[0, T] \times \mathcal{Q}\right) \cup\left(-B^{4} \times \mathcal{Q}\right),$$
where $-B^{4}$ denotes the orientation reversal of $B^{4}$. We specify the family metrics and perturbations on each piece as follows:
\begin{itemize}
\item[-] On the cylindrical pieces $S^{3} \times[-T, 0] \times b$ and $S^{3} \times[0, T] \times b$, the metrics are the cylindrical metrics for the standard round metric on $S^{3}$.
\item[-] On $B^{4} \times\{b\}$ and $-B^{4} \times\{b\}$, we put positive scalar curvature metrics which are cylindrical near the boundary.
\item[-] We put a smooth family of metrics $g_{\widetilde{W} / \mathcal{Q}}=\left\{g_{b}\right\}$ on the fibers of $\widetilde{W}$. They also need to be cylindrical near the boundaries.
\item[-] We pick a family of compactly supported 2-forms $\widetilde{w}=\left\{\omega_{b}\right\}$ on $W_{b}$ to perturb the curvature equation. We require that $\left(g_{\widetilde{W} / \mathcal{Q}}, \widetilde{w}\right)$ is admissible with respect to $\mathfrak{s}_{\widetilde{W}}$ and gives the chamber $\xi$. Note that $\omega_{b}$ depends on $b$ but doesn't depend on $T$.
\item[-] We pick a small 3-dimensional perturbation $\mathfrak{q}$ on $S^{3}$ as in Section 3 and denote the corresponding 4-dimensional perturbation by $\hat{\mathfrak{q}}$.
\item[-] On $B^{4} \times\{b\}$ and $-B^{4} \times\{b\}$, we put 4-dimensional perturbations $\hat{\mathfrak{q}}^{ \pm}$which equals $\hat{\mathfrak{q}}$ near the boundary. $\hat{\mathfrak{q}}^{ \pm}$are independent with $b$ and $T$.
\item[-] Denote the perturbations on $S^{3} \times[-T, 0] \times\{b\}$ and $S^{3} \times[0, T] \times\{b\}$ by $\hat{\mathfrak{q}}_{T, b}^{-}$and $\hat{\mathfrak{q}}_{T, b}^{+}$respectively. Then we require that
$$\left.\hat{\mathfrak{q}}_{T, b}^{-}\right|_{\left[-T,-\frac{2 T}{3}\right] \times S^{3}}=\hat{\mathfrak{q}},\left.\quad \hat{\mathfrak{q}}_{T, b}^{+}\right|_{\left[\frac{2 T}{3}, T\right] \times S^{3}}=\hat{\mathfrak{q}} .$$
and
$$\left.\hat{\mathfrak{q}}_{T, b}^{-}\right|_{\left[-\frac{T}{3}, 0\right] \times S^{3}}=0,\left.\quad \hat{\mathfrak{q}}_{T, b}^{+}\right|_{\left[0, \frac{T}{3}\right] \times S^{3}}=0 .$$
Note that $\hat{\mathfrak{q}}_{T, b}^{ \pm}$will depend on both $T$ and $b$.
\end{itemize}
Let $\mathcal{M}_{T}$ denote the moduli space of perturbed Seiberg-Witten equation on the family $\widetilde{M}_{T}$. Then by choosing generic perturbations as above, one can ensure that the parametrized moduli space
$$\mathcal{M}:=\bigcup_{T \in\left[T_{0},+\infty\right)} \mathcal{M}_{T}$$
is regular, where $T_{0}$ is a large enough number. As a result, $\mathcal{M}$ is a 1-dimensional manifold because $d(\widetilde{\mathfrak{s}}, \widetilde{M})=0$. To compactify $\mathcal{M}$, we need add in the corresponding moduli space when $T=\infty$. Namely, the broken trajectories on
$$\left(\left(B^{4}\right)^{*} \times Q\right) \cup \widetilde{W}^{*} \cup\left(\left(-B^{4}\right)^{*} \times Q\right)$$
Here $\left(B^{4}\right)^{*}$ is obtained by attaching a cylindrical end to $B^{4}$. This trajectory belongs to the moduli space
$$\mathcal{M}_{\infty}^{i, j}=\mathcal{M}\left(\left(B^{4}\right)^{*} \times Q,\left[\mathfrak{a}_{i}\right]\right) \times_{Q} \mathcal{M}\left(\left[\mathfrak{a}_{i}\right], \widetilde{W}^{*},\left[\mathfrak{a}_{j}\right]\right) \times_{Q} \mathcal{M}\left(\left[\mathfrak{a}_{j}\right],\left(-B^{4}\right)^{*} \times Q\right) .$$

Note that (61) implies that the limiting perturbation on $\left(B^{4}\right)^{*}$ and $\left(-B^{4}\right)^{*}$ are independent with $b$, therefore, we have
$$\mathcal{M}\left(\left(B^{4}\right)^{*} \times Q,\left[\mathfrak{a}_{i}\right]\right)=\mathcal{M}\left(\left(B^{4}\right)^{*},\left[\mathfrak{a}_{i}\right]\right) \times Q$$
and
$$\mathcal{M}\left(\left[\mathfrak{a}_{j}\right],\left(-B^{4}\right)^{*} \times Q\right)=\mathcal{M}\left(\left[\mathfrak{a}_{j}\right],\left(-B^{4}\right)^{*}\right) \times Q .$$
That implies
$$\mathcal{M}_{\infty}^{i, j}=\mathcal{M}\left(\left(B^{4}\right)^{*},\left[\mathfrak{a}_{i}\right]\right) \times \mathcal{M}\left(\left[\mathfrak{a}_{i}\right], \widetilde{W}^{*},\left[\mathfrak{a}_{j}\right]\right) \times \mathcal{M}\left(\left[\mathfrak{a}_{j}\right],\left(-B^{4}\right)^{*}\right) .$$
By computing the expected dimension, we see that $\mathcal{M}_{\infty}^{i, j}$ is empty unless $i=-1$ and $j=0$. Furthermore, as proved in [19], when the perturbations are small enough, $\mathcal{M}\left(\left(B^{4}\right)^{*},\left[\mathfrak{a}_{-1}\right]\right)$ and $\mathcal{M}\left(\left[\mathfrak{a}_{0}\right],\left(-B^{4}\right)^{*}\right)$ both contain a single point (with positive sign). Hence we further have
$$\mathcal{M}_{\infty}^{-1,0}=\mathcal{M}\left(\left[\mathfrak{a}_{-1}\right], \widetilde{W}^{*},\left[\mathfrak{a}_{0}\right]\right) .$$
To this end, we see that we can compactify $\mathcal{M}$ into a 1-dimensional manifold $\mathcal{M}^{+}$with boundary by adding in points in $\mathcal{M}\left(\left[\mathfrak{a}_{-1}\right], \widetilde{W}^{*},\left[\mathfrak{a}_{0}\right]\right)$. The signed count of boundary points of $\mathcal{M}^{+}$must be zero. That implies
$$\# \mathcal{M}_{T_{0}}=\# \mathcal{M}\left(\left[\mathfrak{a}_{-1}\right], \widetilde{W}^{*},\left[\mathfrak{a}_{0}\right]\right) .$$
This is exactly (60) because $\breve{1}$ and $\widehat{1}$ correspond to the critical points $\left[\mathfrak{a}_{0}\right]$ and $\left[\mathfrak{a}_{-1}\right]$ respectively. \(\square\)
5.2. A gluing formula for the family Seiberg-Witten invariants. Now we are ready to prove Theorem L. For readers' convenience, we restate our setting as follows:

Let $\widetilde{M}_{1}$ be a family of 4-manifolds with boundary $Y$. We assume $\widetilde{M}_{1}$ is a homology product and a product near the boundary. We take a family spin ${ }^{c}$ structure $\mathfrak{s}_{\widetilde{M_{1}}}$ on $\widetilde{M}_{1}$ which is a product near the boundary and we use $\mathfrak{s}_{Y}$ to denote its resection to the boundary of each fiber. As in previous section, we use the product structure near the boundary to specify a section $s: \mathcal{Q} \rightarrow \widetilde{M}_{1}$. By fiberwisely removing small balls surrounding the image of $s$, we obtain a family spin ${ }^{c}$ cobordism $\left(\widetilde{W}_{01}, \mathfrak{s}_{\widetilde{W}_{01}}\right)$ from $S^{3}$ to $Y$.

On the other side, we take a single 4 -manifold $M_{2}$ with boundary $-Y$. Let $\mathfrak{s}_{M_{2}}$ be a spin ${ }^{c}$ that is isomorphic to $\mathfrak{s}_{Y}$ ) on the boundary. We remove a small ball from $M_{2}$ to obtain a spin ${ }^{c}$ cobordism $\left(W_{12}, \mathfrak{s}_{W_{12}}\right)$ from $Y$ to $S^{3}$.

We then form a family of closed 4-manifold
$$\widetilde{M}:=\widetilde{M}_{1} \cup_{\mathcal{Q} \times Y}\left(\mathcal{Q} \times M_{2}\right)$$
with fiber $M=M_{1} \cup_{Y} M_{2}$
Theorem 5.2 (Theorem L restated). Let $\widetilde{M}$ be defined as above. Then we have the following results regarding the family Seiberg-Witten invariants of $\widetilde{M}$.
\begin{itemize}
\item[(1)] Suppose $b_{2}^{+}\left(M_{2}\right)>1$. Then we have
$$\sum_{\widetilde{\mathfrak{s}}} \operatorname{FSW}(\widetilde{M}, \widetilde{\mathfrak{s}})=\left\langle\widehat{H M}_{*}\left(\widetilde{W}_{01}, \mathfrak{s}_{\widetilde{W}_{01}}\right)(\widehat{1}), \overline{H M}^{*}\left(W_{12}, \mathfrak{s}_{W_{12}}\right)(\check{1})\right\rangle$$
\end{itemize}
\begin{itemize}
\item[(2)] Suppose $b_{2}^{+}(M)>b_{2}^{+}\left(M_{2}\right)=1$. Then we have
$$\sum_{\widetilde{\mathfrak{s}}} \operatorname{FSW}(\widetilde{M}, \widetilde{\mathfrak{s}})=\left\langle\widehat{H M}_{*}\left(\widetilde{W}_{01}, \mathfrak{s}_{\widetilde{W}_{01}}\right)(\widehat{1}), \overrightarrow{H M}^{*}\left(W_{12}, \mathfrak{s}_{W_{12}}\right)_{ \pm}(\check{1})\right\rangle .$$
\item[(3)] Suppose $b_{2}^{+}(M)=b_{2}^{+}\left(M_{2}\right)=1$. Then we have
$$\sum_{\widetilde{\mathfrak{s}}} \operatorname{FSW}(\widetilde{M}, \widetilde{\mathfrak{s}})_{ \pm}=\left\langle\widehat{H M}_{*}\left(\widetilde{W}_{01}, \mathfrak{s}_{\widetilde{W}_{01}}\right)(\widehat{1}), \overline{H M}^{*}\left(W_{12}, \mathfrak{s}_{W_{12}}\right)_{ \pm}(\check{1})\right\rangle .$$
\end{itemize}
In these formulas, we are summing over all family $\operatorname{spin}^{c}$ structures $\widetilde{\mathfrak{s}}$ that satisfy
$$\left.\widetilde{\mathfrak{s}}\right|_{\widetilde{M}_{1}}=\mathfrak{s} \widetilde{M}_{1},\left.\widetilde{\mathfrak{s}}\right|_{M_{2}}=\mathfrak{s}_{M_{2}} \text { and } d(\widetilde{\mathfrak{s}}, \widetilde{M})=0 .$$
Proof. This is a direct corollary of Theorem 5.1 and Theorem 4.22. Note that when $b_{1}(Y)>0$, there can be a family spin ${ }^{c}$ structure $\widetilde{\mathfrak{s}}$ such that $\left.\widetilde{\mathfrak{s}}\right|_{\widetilde{M}_{1}}=\mathfrak{s}_{\widetilde{M}_{1}},\left.\widetilde{\mathfrak{s}}\right|_{M_{2}}=\mathfrak{s}_{M_{2}}$ but $d(\widetilde{\mathfrak{s}}, \widetilde{M}) \neq 0$. Such a $\operatorname{spin}^{c}$ structure has no contribution on either side of the above equalities. \(\square\)

Theorem 5.3 (Theorem M restated). Let $\widetilde{M}$ be a family of closed 4-manifolds with an even dimensional, connected base $\mathcal{Q}$. Suppose $\pi_{1}(\mathcal{Q})$ acts trivially on $H_{*}(M ; \mathbb{Z})$ and suppose $\widetilde{M}$ has a decomposition of the form (62) with $Y$ being an $L$-space. Let $\widetilde{\mathfrak{s}}$ be a family spin ${ }^{c}$ structure on $\widetilde{M}$ and let $\mathfrak{s}$ be a spin ${ }^{c}$ structure on the fiber $M$ which satisfy $\left.\widetilde{\mathfrak{s}}\right|_{M_{2}}=\left.\mathfrak{s}\right|_{M_{2}}$ and $d(\mathfrak{s}, M) \geqslant d(\widetilde{\mathfrak{s}}, \widetilde{M})=0$. Then the following results hold.
\begin{itemize}
\item[(1)] Suppose $b_{2}^{+}\left(M_{1}\right)=0$ and $b_{2}^{+}\left(M_{2}\right)>1$. Then
$$\operatorname{FSW}(\widetilde{M}, \widetilde{\mathfrak{s}})=\left\langle c_{\frac{\operatorname{dim}(\mathcal{Q})}{2}}\left(-\operatorname{Ind}\left(\not D^{+}(\widetilde{M}, \widetilde{\mathfrak{s}})\right) \otimes L^{-1}\right),[\mathcal{Q}]\right\rangle \cdot \operatorname{SW}(M, \mathfrak{s})$$
\item[(2)] Suppose $b_{2}^{+}\left(M_{1}\right)=0$ and $b_{2}^{+}\left(M_{2}\right)=1$. Then
$$\operatorname{FSW}_{ \pm}(\widetilde{M}, \widetilde{\mathfrak{s}})=\left\langle c_{\frac{\operatorname{dim}(\mathcal{Q})}{2}}\left(-\operatorname{Ind}\left(\not D^{+}(\widetilde{M}, \widetilde{\mathfrak{s}})\right) \otimes L^{-1}\right),[\mathcal{Q}]\right\rangle \cdot \mathrm{SW}_{ \pm}(M, \mathfrak{s})$$
\item[(3)] Suppose $b_{2}^{+}\left(M_{1}\right)>0$ and $b_{2}^{+}(M)>1$. Then $\operatorname{FSW}(\widetilde{M}, \widetilde{\mathfrak{s}})=0$.
\item[(4)] Suppose $b_{2}^{+}\left(M_{1}\right)>0$ and $b_{2}^{+}(M)=1$. Then $\operatorname{FSW}_{ \pm}(\widetilde{M}, \widetilde{\mathfrak{s}})=0$.
\end{itemize}
Here $L$ is the unique complex line bundle over $\mathcal{Q}$ such that $\left(\left.\widetilde{\mathfrak{s}}\right|_{\mathcal{Q} \times M_{2}}\right) \otimes p^{*}\left(L^{-1}\right)$ is a pull back of $\left(M_{2},\left.\widetilde{\mathfrak{s}}\right|_{M_{2}}\right)$. And $\operatorname{Ind}\left(\not D^{+}(\widetilde{M}, \widetilde{\mathfrak{s}})\right.$ denotes the index bundle of the family Dirac operator.
Proof. Suppose $b_{2}^{+}\left(M_{1}\right)>0$. By Theorem 4.32, we have $\widehat{H M}_{*}\left(\widetilde{W}_{01}, \mathfrak{s}_{\widetilde{W}_{01}}\right)(\widehat{1})=0$. By Theorem L, we have $\operatorname{FSW}(\widetilde{M}, \widetilde{\mathfrak{s}})=0$ when $b_{2}^{+}(M)>1$ and we have $\operatorname{FSW}_{ \pm}(\widetilde{M}, \widetilde{\mathfrak{s}})=0$ when $b_{2}^{+}(M)=1$. This proves the case (3) and (4).

Next, we assume $b_{2}^{+}\left(M_{2}\right)>1$. By Lemma 12, replacing $\widetilde{\mathfrak{s}}$ with $(\widetilde{\mathfrak{s}}) \otimes p^{*}\left(L^{-1}\right)$ does not change the family Seiberg-Witten invariant. Therefore, it suffice to show that
$$\operatorname{FSW}_{\xi_{c}}(\widetilde{M}, \widetilde{\mathfrak{s}})=\left\langle c_{\frac{\operatorname{dim}(\mathcal{Q})}{2}}\left(-\operatorname{Ind}\left(\not D^{+}(\widetilde{M}, \widetilde{\mathfrak{s}})\right),[\mathcal{Q}]\right\rangle \cdot \operatorname{SW}(M, \mathfrak{s})\right.$$
under the additional assumption that $\left.\widetilde{\mathfrak{s}}\right|_{\mathcal{Q} \times M_{2}}$ is pulled back from $\left.\widetilde{\mathfrak{s}}\right|_{M_{2}}$. Note that since $Y$ is a rational homology 3-sphere, the family spin ${ }^{c}$-structure $\widetilde{\mathfrak{s}}$ is uniquely determined by its
restrictions to $\widetilde{M}_{1}$ and $\mathcal{Q} \times M_{2}$. Therefore, by applying Theorem L to the family $(\widetilde{M}, \widetilde{\mathfrak{s}})$, we get
$$\operatorname{FSW}(\widetilde{M}, \widetilde{\mathfrak{s}})=\left\langle\widehat{H M}_{*}\left(\widetilde{W}_{01},\left.\widetilde{\mathfrak{s}}\right|_{\widetilde{W}_{01}}\right)(\widehat{1}), \overline{H M}^{*}\left(W_{12},\left.\widetilde{\mathfrak{s}}\right|_{W_{12}}\right)(\widetilde{1})\right\rangle .$$

For a single 4-manifold $(M, \mathfrak{s})$, there is the following gluing formula
$$\operatorname{SW}(M, \mathfrak{s})=\left\langle U^{\frac{d(\mathfrak{s}, M)}{2}} \cdot \widehat{H M}_{*}\left(W_{01},\left.\mathfrak{s}\right|_{W_{01}}\right)(\widehat{1}), \overrightarrow{H M}^{*}\left(W_{12},\left.\widetilde{\mathfrak{s}}\right|_{W_{12}}\right)(\check{1})\right\rangle .$$
which generalizes Theorem L (see [19, Proposition 27.4.1]). Applying Theorem 4.32 to the single cobordism $\left(W_{01},\left.\mathfrak{s}\right|_{W_{01}}\right)$, we get
$$\widehat{H M}_{*}\left(W_{01},\left.\mathfrak{s}\right|_{W_{01}}\right)(\widehat{1})=\hat{e}_{d^{\prime}-1},$$
where $d^{\prime}=\frac{c_{1}^{2}\left(\mathfrak{s} \mid{ }_{M_{1}}\right)-\sigma\left(M_{1}\right)}{4}$. Applying Theorem 4.32 again to the family cobordism $\left(\widetilde{W}_{01},\left.\widetilde{\mathfrak{s}}\right|_{\widetilde{W}_{01}}\right)$, we get that
$$\widehat{H M}_{*}\left(\widetilde{W}_{01}, \widetilde{\mathfrak{s}}_{\mid \widetilde{W}_{01}}\right)(\widehat{1})=\left\langle c_{\frac{\operatorname{dim} \mathcal{Q}}{2}}\left(-\operatorname{Ind}\left\{D_{A_{b}^{0}, \hat{q}_{b}}^{+}\left(W_{01, b}\right)\right\}\right),[\mathcal{Q}]\right\rangle \cdot \widehat{e}_{d^{\prime}-d(\mathfrak{s}, M)-1} .$$
We combine (66), (67), (68), (69) and we note that
$$U^{\frac{d(\mathfrak{s}, M)}{2}} \cdot \widehat{e}_{d^{\prime}-1}=\widehat{e}_{d^{\prime}-d(\mathfrak{s}, M)-1} .$$
This proves (63). The proof of (64) is completely analogous. \(\square\)

\section*{6. Families of 4-manifolds constructed from ADE-type singularities}

In this section, we construct families of 4-manifolds over $S^{2}$ which arise when one resolves an ADE-type singularity using a hyperhähler family of complex structures near the singularity. See [12, 13, 16] for some previous studies on these natural families.

Recall that an ADE singularity is a singularity that locally models on the quotient $\mathbb{C}^{2} / \Gamma$, where $\Gamma$ is a finite subgroup of SU(2). Such a group correspond to a single laced Dykin diagram $G$ of type A, type D and type E. An ADE singularity carries a minimal resolution
$$p: \widetilde{\mathbb{C}^{2} / \Gamma} \rightarrow \mathbb{C}^{2} / \Gamma .$$
The preimage $p^{-1}(0)$ is the union of a collection of -2-spheres $\left\{S_{1}, \cdots S_{n}\right\}$, which one-to-one correspond to the vertices $\left\{v_{1}, \cdots, v_{n}\right\}$ of $G . S_{i}$ and $S_{j}$ intersects transversely at a single point when there is an edge connecting $v_{i}$ and $v_{j}$ and they don't intersect otherwise. (See, for example, [38] for more detailed discussions.)

We use $D(V)$ (resp. $S(V)$ ) to denote the unit disk (resp. unit sphere) in a normed vector space $V$. Let $M_{1}=p^{-1}\left(D\left(\mathbb{C}^{2}\right) / \Gamma\right)$. Then $M_{1}$ is a 4-manifold whose boundary $Y=S\left(\mathbb{C}^{2}\right) / \Gamma$ is a rational homology sphere that carries a positive scalar curvature. Note that $M_{1}$ can be obtained by plumbing disk bundles over $S_{i}$. Therefore, $M_{1}$ deformation retracts to $p^{-1}(0)$. In particular, it is simply connected and $H_{2}\left(M_{1}\right)$ is freely generated by $\left\{S_{i}\right\}$. The intersection form of $M_{1}$ is the matrix associated to the Dynkin diagram $G$. Hence it is not hard to check that $M_{1}$ is negative definite.

Now we construct a smooth family over $\mathcal{Q}=S^{2}$ with fiber $M_{1}$. We identify $\mathbb{C}^{2}$ with $\mathbb{H}$ by sending $\left(z_{1}, z_{2}\right)$ to $z_{1}+\mathrm{j} \cdot z_{2}$ and identify $S(\mathbb{H})$ with SU(2) by sending $w_{1}+\mathrm{j} w_{2}$ to
$\binom{w_{1}-\bar{w}_{2}}{w_{2}}$. Then the standard action $S U(2)$ on $\mathbb{C}^{2}$ can be equivalently described as the left multiplication of $S(\mathbb{H})$ on $\mathbb{H}$. Consider the space
$$\mathcal{Q}=\left\{a \mathrm{i}+b \mathrm{j}+c \mathrm{k} \mid a, b, c \in \mathbb{R}, a^{2}+b^{2}+c^{2}=1\right\}=S^{2} .$$
with base point $b_{0}=\mathrm{i}$. We use the ordered basis \{i, j, k\} to orent the space they span and to orient $\mathcal{Q}$. For each $b \in \mathcal{Q}$, the right multiplication by $b$ provides a complex structure $J_{b}$ on $\mathbb{H}$. Since right multiplications commute with left multiplications, the action of $\Gamma$ preserve all these complex structures. Therefore, we can take the product space $\mathcal{Q} \times(D(\mathbb{H}) / \Gamma)$ and simultaneously resolve the singularities in the fibers $\{\{b\} \times(D(\mathbb{H}) / \Gamma)\}_{b \in \mathcal{Q}}$ using the complex structures $\left\{J_{b}\right\}_{b \in \mathcal{Q}}$. This gives us a smooth family $\widetilde{M}_{1} / \mathcal{Q}$ of 4-manifolds whose boundary carries a natural trivialization. We use $M_{1, b}$ to denote the fiber over $b$.

Given any smooth 4-manifold $M_{2}$ with fiber $-Y$, we can complete the family $\widetilde{M}_{1} / \mathcal{Q}$ into a family
$$\widetilde{M}=\widetilde{M}_{1} \cup_{\mathcal{Q} \times Y} \widetilde{M}_{2}$$
of closed 4-manifolds. Here $\widetilde{M}_{2}$ is the product family $\mathcal{Q} \times M_{2}$. We call $\widetilde{M} / \mathcal{Q}$ the ADE family with fiber $M=M_{1} \cup M_{2}$.

The clutching function of $\widetilde{M}_{1} / \mathcal{Q}$ is an element in $\pi_{1}\left(\operatorname{Diff}\left(M_{1}, \partial M_{1}\right)\right)$. We give an alternative description of this element. Let $S^{1}=\left\{e^{\mathrm{i} \theta}\right\} \subset S(\mathbb{H})$. Consider the $S^{1}$-action on $\mathbb{H}$ by the right multiplication. Since this action preserves both the action of $\Gamma$ and the complex structure $J_{\mathrm{i}}$, it lifts to an $S^{1}$-action
$$\phi: S^{1} \times M_{1} \rightarrow M_{1} .$$
We want to modify $\phi_{1}$ so that it fix the boundary pointwisely. We take a null-homotopy of the inclusion $S^{1} \hookrightarrow S(\mathbb{H})$
$$h: S^{1} \times\left[\frac{1}{2}, 1\right] \rightarrow S(\mathbb{H})$$
that satisfies $h\left(e^{\mathrm{i} \theta}, t\right)=e^{\mathrm{i} \theta}$ for any $t \in\left[\frac{1}{2}, \frac{2}{3}\right]$ and $h\left(e^{\mathrm{i} \theta}, t\right)=1$ for any $t \in\left[\frac{5}{6}, 1\right]$. Then we consider the map $\phi_{1}^{\prime}: S^{1} \times M_{1} \rightarrow M_{1}$ defined by
$$\phi^{\prime}\left(e^{\mathrm{i} \theta}, x\right)=\left\{\begin{array}{ll}
\phi_{1}\left(e^{\mathrm{i} \theta}, x\right) & \text { if }|p(x)|<\frac{1}{2} \\
p^{-1}\left(p(x) \cdot h\left(e^{\mathrm{i} \theta}, t\right)\right) & \text { if }|p(x)| \in\left[\frac{1}{2}, 1\right]
\end{array} .\right.$$
Because $\phi^{\prime}\left(e^{\mathrm{i} \theta},-\right)$ fixes the boundary pointwisely, we obtain a loop $\gamma$ in $\operatorname{Diff}\left(M_{1}, \partial M_{1}\right)$. Because $\pi_{2}(S(\mathbb{H}))=0$, the homotopy class of $\gamma$ doesn't depend on $h$. We mentioned that for an $A_{1}$-sigularity, $p^{-1}(0)$ consists of a single -2 -sphere $S$ and $\gamma$ is exactly the generalized Dehn twist along $S$ introduced in Section 1.

Remark 9. We specify our convention of clutching function as follows: Given a topological space $F$ and a loop $\eta=\left\{\eta_{\theta}: F \rightarrow F\right\}_{\theta \in[0,2 \pi]}$ of homeomorphisms based at the identity. We can form a fiber bundle $\widetilde{F}$ over $S^{2}=D(\mathbb{C}) / S(\mathbb{C})$, whose total space is defined as
$$(D(\mathbb{C}) \times F) /\left(e^{\mathrm{i} \theta}, x\right) \sim\left(1, \eta_{\theta}(x)\right) .$$

We say the clutching function of this bundle $\widetilde{F}$ is represented by $\eta$. Under this convention, suppose we set $F=\mathbb{C}$ and let $\eta$ be the circle action of weight $k$. Then $\widetilde{F}$ has Euler number $-k$.

Lemma 6.1. $\gamma$ represents the clutching function of the family $\widetilde{M}_{1} / \mathcal{Q}$.
Proof. For any $\theta \in[0,2 \pi]$ and $\xi \in[0, \pi]$, we let
$$b_{\theta, \xi}=\cos \xi \cdot \mathrm{i}+\sin \xi \cos \theta \cdot \mathrm{j}+\sin \xi \sin \theta \cdot \mathrm{k} .$$
Consider a map $f_{\theta, \xi}: D(\mathbb{H}) \rightarrow D(\mathbb{H})$ defined by
$$f_{\theta, \xi}(x)=\left\{\begin{array}{ll}
x \cdot b_{\theta, \frac{\xi}{2}} & \text { if }|x|<\frac{1}{2} \\
x \cdot\left(\tau(|x|)+\sqrt{1-\tau(|x|)^{2}} b_{\theta, \frac{\xi}{2}}\right) & \text { if }|x| \in\left[\frac{1}{2}, 1\right]
\end{array},\right.$$
where $\tau:\left[\frac{1}{2}, 1\right] \rightarrow[0,1]$ is a non-decreasing function that equals 0 near $\frac{1}{2}$ and equals 1 near 1. Note that we have
$$b_{\theta, \frac{\xi}{2}}^{-1} \cdot \mathrm{i} \cdot b_{\theta, \frac{\xi}{2}}=b_{\theta, \xi} .$$
Therefore, near 0, the map $f_{\theta, \xi}$ sends $J_{i}$ to $J_{b_{\theta, \xi}}$. As a result, it induces a diffeomorphism
$$\widetilde{f}_{\theta, \xi}: M_{1, \mathrm{i}} \rightarrow M_{1, b_{\theta, \xi}} .$$
By definition, the clutching function is given by the family of diffeomorphisms
$$\left\{\widetilde{f}_{0, \pi}^{-1} \circ \widetilde{f}_{\theta, \pi}: M_{1, \mathrm{i}} \rightarrow M_{1, \mathrm{i}}\right\}_{\theta \in[0,2 \pi]} .$$
Note that for $|x|<\frac{1}{2}$, we have
$$f_{0, \pi}^{-1} \circ f_{\theta, \pi}(x)=x \cdot b_{\theta, \frac{\pi}{2}} \cdot b_{0, \frac{\pi}{2}}^{-1}=x(\cos \theta+\sin \theta \cdot \mathrm{i}) .$$
Therefore, the loop in $\operatorname{Diff}\left(M_{1}, \partial M_{1}\right)$ given by the family $\left\{\widetilde{f}_{0, \pi}^{-1} \circ \widetilde{f}_{\theta, \pi}\right\}$ is exactly $\gamma$ for a suitable choice of $h$. \(\square\)

The following lemma proves the existence of fiberwise almost complex structures on $\widetilde{M}$.
Lemma 6.2. Let $J$ be an almost complex structure on $M=M_{b_{0}}$. Suppose $c_{1}\left(T M_{1}, J\right)=0$. Then there exists a fiberwise almost complex structure $\left\{J_{b}\right\}_{b \in \mathcal{Q}}$ on fibers of $\widetilde{M}$ that extends $J$.
Proof. Since $M_{1}=\widetilde{D(\mathbb{H}) / \Gamma}$ deformation retracts to $\cup_{1 \leqslant i \leqslant n} S_{i}$, an almost complex structure on $M_{1}$ is determined by its first Chern class. Therefore, after a suitable homotopy, we may assume that $\left.J\right|_{M_{1}}$ is inherited from the complex structure $J_{\mathrm{i}}$ on $\mathbb{H}$.

Let $Y=\partial M_{1}=S(\mathbb{H}) / \Gamma$. Then for each $b \in \mathcal{Q}$, the complex structure $J_{b}$ on $\mathbb{H}$ induces an almost complex structure on $\left.T M_{1}\right|_{Y}$, denoted by $J_{Y, b}$. Then $\left.J\right|_{Y}=J_{Y, i}$.

Next, we consider the fiberwise almost complex structure on the following two families.
\begin{itemize}
\item[-] Since the ADE family $\widetilde{M}_{1} / \mathcal{Q}$ is obtained fiberwisely resolving $\mathcal{Q} \times(D(\mathbb{H}) / \Gamma)$ using $\left\{J_{b}\right\}_{b \in \mathcal{Q}}$, there is an induced fiberwise almost complex structure $\left\{J_{b}^{1}\right\}_{b \in \mathcal{Q}}$ on $\widetilde{M}_{1} / \mathcal{Q}$ such that $\left.J_{b}^{1}\right|_{Y}=J_{Y, b}$.
\end{itemize}
\begin{itemize}
\item[-] Take the product family with fiber $M_{1}$, denoted by $\widetilde{M}_{1}^{\prime} / \mathcal{Q}$. As proved in [16], the space $M_{1}^{*}:=\widetilde{\mathbb{H} / \Gamma}$ is an ALE space. In particular, it admits a family of complex structuers $\left\{J_{M_{1}^{*}, b}\right\}_{b \in \mathcal{Q}}$ such that $J_{M_{1}^{*}, b}$ limits to $J_{b}$ near infinity. By restricting these complex structures to $M_{1}$ and applying a suitable homotopy near the boundary, we obtain a fiberwise almost complex structure $\left\{J_{b}^{2}\right\}_{b \in \mathcal{Q}}$ on $\widetilde{M}_{1}^{\prime} / \mathcal{Q}$ such that $\left.J_{b}^{2}\right|_{Y}=$ $J_{Y, b}$.
\end{itemize}
We glue together the families $\widetilde{M}_{1} / \mathcal{Q}$ and $\widetilde{M}_{1}^{\prime} / \mathcal{Q}$ along their common fiber at $b_{0}$ and form a family $\widetilde{M}_{1} \cup_{M_{1}} \widetilde{M_{1}^{\prime}}$ over $\mathcal{Q} \vee \mathcal{Q}$. Then we pull back this bundle via a map $\rho: \mathcal{Q} \rightarrow \mathcal{Q} \vee \mathcal{Q}$ that is of degree 1 on the first component and degree -1 on the second component. We denote the resulting family by $\widetilde{M}_{1}^{\prime \prime} / \mathcal{Q}$ and denote the pulled-back fiberwise almost complex structure by $\left\{J_{b}^{3}\right\}_{b \in \mathcal{Q}}$. Note that $\left.J_{b}^{3}\right|_{Y}=J_{Y, \rho^{\prime}(b)}$, where $\rho^{\prime}: \mathcal{Q} \rightarrow \mathcal{Q}$ is the composition
$$\mathcal{Q} \xrightarrow{\rho} \mathcal{Q} \vee \mathcal{Q} \xrightarrow{\mathrm{Id}_{\mathcal{Q}} \vee \mathrm{Id}_{\mathcal{Q}}} \mathcal{Q} .$$
Since $\rho^{\prime}$ is null-homotopic, we may homotope $\left\{J_{b}^{3}\right\}_{b \in \mathcal{Q}}$ near the boundary to obtain a fiberwise almost complex structure $\left\{J_{b}^{4}\right\}_{b \in \mathcal{Q}}$ on $\widetilde{M}_{1}^{\prime \prime} / \mathcal{Q}$ such that $\left.J_{b}^{4}\right|_{Y}=J_{Y, \mathrm{i}}$ for any $b \in \mathcal{Q}$. Note that $\widetilde{M}_{1}^{\prime \prime} / \mathcal{Q}$ and $\widetilde{M}_{1} / \mathcal{Q}$ are isomorphic. So we can also treat $\left\{J_{b}^{4}\right\}_{b \in \mathcal{Q}}$ as a fiberwise almost complex structure on $\widetilde{M}_{1} / \mathcal{Q}$. Let $J_{M, b}$ be obtained by gluing together $J_{b}^{4}$ and $\left.J\right|_{M_{2}}$ along $Y$. Then $\left\{J_{M, b}\right\}_{b \in \mathcal{Q}}$ is a fiberwise almost complex structure on $\widetilde{M} / \mathcal{Q}$ that extends $J$. \(\square\)

Next, we give an explicit description of the circle action (72). To do this, we need an alternative construction of $M_{1}$ by plumbing disk bundles.