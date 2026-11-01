---
retention_scope: session
part: 2
total_parts: 5
---

[Part 2/5 of: THE FAMILY SEIBERG-WITTEN INVARIANT AND NON-SYMPLECTIC LOOPS OF DIFFEOMORPHISMS]

Given any pairs of critical points $[\mathfrak{a}],[\mathfrak{b}] \in \mathfrak{C}$, we consider the moduli space $\breve{\mathcal{M}}([\mathfrak{a}],[\mathfrak{b}])$ of unparametrized, nonconstant flow lines of $v_{\mathfrak{q}}^{\sigma}$ going from $[\mathfrak{a}]$ to $[\mathfrak{b}]$. This moduli space is an oriented manifold. Note that different components of $\breve{\mathcal{M}}([\mathfrak{a}],[\mathfrak{b}])$ may have different dimensions. We use $\# \breve{\mathcal{M}}([\mathfrak{a}],[\mathfrak{b}])$ to denote the signed count of points in the 0-dimensional components. Similarly, for each pair of reducible critical points $[\mathfrak{a}],[\mathfrak{b}]$, we use $\breve{\mathcal{M}}^{\text {red }}([\mathfrak{a}],[\mathfrak{b}])$ to denote the moduli space of unparametrized, nonconstant reducible flow lines going from $[\mathfrak{a}]$ to $[\mathfrak{b}]$ and use $\# \breve{\mathcal{M}}^{\text {red }}([\mathfrak{a}],[\mathfrak{b}])$ to denote the signed count of points in the 0-dimensional components. The compactness theorem for the Seiberg-Witten trajectories ([19, Proposition 16.1.4]) ensures that $\# \breve{\mathcal{M}}([\mathfrak{a}],[\mathfrak{b}])$ and $\# \breve{\mathcal{M}}^{\text {red }}([\mathfrak{a}],[\mathfrak{b}])$ are always finite numbers.

Let $C^{o}$ (respectively $C^{s}$ and $C^{u}$ ) be the vector space over $\mathbb{Q}$ whose basis vectors $e_{[\mathfrak{a}]}$ are indexed by elements $[\mathfrak{a}] \in \mathfrak{C}^{o}$ (respectively $\mathfrak{C}^{o}$ and $\mathfrak{C}^{u}$ ). We define a linear map $\partial_{s}^{o}: C^{o} \rightarrow C^{s}$ by the formula
$$\partial_{s}^{o} e_{[\mathfrak{a}]}:=\sum_{[\mathfrak{b}] \in \mathfrak{C}^{s}} \# \breve{\mathcal{M}}([\mathfrak{a}],[\mathfrak{b}]) \cdot e_{[\mathfrak{b}]} .$$
The linear maps $\partial_{o}^{o}: C^{o} \rightarrow C^{o}, \partial_{s}^{u}: C^{u} \rightarrow C^{s}$ and $\partial_{o}^{u}: C^{u} \rightarrow C^{o}$ are defined similarly. Moreover, by counting only reducible flow lines, one can define another four linear maps
$$\bar{\partial}_{s}^{s}: C^{s} \rightarrow C^{s}, \bar{\partial}_{u}^{s}: C^{s} \rightarrow C^{u}, \bar{\partial}_{s}^{u}: C^{s} \rightarrow C^{s}, \quad \bar{\partial}_{u}^{u}: C^{u} \rightarrow C^{u}$$
by the formula
$$\bar{\partial}_{*}^{*}[\mathfrak{a}]:=\sum_{[\mathfrak{b}] \in \mathfrak{C}^{*}} \# \breve{\mathcal{M}}^{\mathrm{red}}([\mathfrak{a}],[\mathfrak{b}]) \cdot e_{[\mathfrak{b}]} .$$
Consider the vector spaces
$$\bar{C}=C^{s} \oplus C^{u}, \quad \check{C}=C^{o} \oplus C^{s}, \quad \widehat{C}=C^{o} \oplus C^{u} .$$
The three flavors of monopole Floer homology $\overline{H M}_{*}(Y, \mathfrak{s}), \widetilde{H M}_{*}(Y, \mathfrak{s}), \widehat{H M}_{*}(Y, \mathfrak{s})$ are defined as homology of the chain complexes $(\bar{C}, \bar{\partial}),(\widehat{C}, \widehat{\partial}),(\check{C}, \check{\partial})$ with differentials
$$\bar{\partial}=\left(\begin{array}{cc}
\bar{\partial}_{s}^{s} & \bar{\partial}_{s}^{u} \\
\bar{\partial}_{u}^{s} & \bar{\partial}_{u}^{u}
\end{array}\right), \quad \hat{\partial}=\left(\begin{array}{cc}
\partial_{o}^{o} & \partial_{o}^{u} \\
-\hat{\partial}_{u}^{s} \partial_{s}^{o} & -\hat{\partial}_{u}^{u}-\hat{\partial}_{u}^{s} \partial_{s}^{u}
\end{array}\right), \quad \check{\partial}=\left(\begin{array}{cc}
\partial_{o}^{o} & -\partial_{o}^{u} \hat{\partial}_{u}^{s} \\
\partial_{s}^{o} & \hat{\partial}_{s}^{s}-\partial_{s}^{u} \hat{\partial}_{u}^{s}
\end{array}\right) .$$

The corresponding monopole Floer cohomology $\overline{H M}^{*}(Y, \mathfrak{s}), \widehat{H M}^{*}(Y, \mathfrak{s}), \widehat{H M}^{*}(Y, \mathfrak{s})$ are defined as homology of the dual complexes $\operatorname{Hom}(\bar{C}, \mathbb{Q}), \operatorname{Hom}(\check{C}, \mathbb{Q})$ and $\operatorname{Hom}(\widehat{C}, \mathbb{Q})$. It's shown in [19, Corollary 23.1.6] that all these flavors of monopole Floer (co)homology are independent with the choice of auxiliary data (e.g. perturbation and Riemannian matric) and hence are invariants of the pair $(Y, \mathfrak{s})$. Many results in [19] holds for all three flavors. In this situation, we will simply use the notation $H M_{*}^{\circ}(Y, \mathfrak{s})$ for homology and $H M_{\circ}^{*}(Y, \mathfrak{s})$ for cohomology. We define
$$H M_{*}^{\circ}(Y):=\bigoplus_{\mathfrak{s} \in \operatorname{spin}^{c}(Y)} H M_{*}^{\circ}(Y, \mathfrak{s}), \quad H M_{\circ}^{*}(Y):=\bigoplus_{\mathfrak{s} \in \operatorname{spin}^{c}(Y)} H M_{\circ}^{*}(Y, \mathfrak{s}) .$$

We use
$$\langle-,-\rangle: H M_{*}^{\circ}(Y, \mathfrak{s}) \otimes H M_{\circ}^{*}(Y, \mathfrak{s}) \rightarrow \mathbb{Q}$$
to denote the canonical pairing induced by the obvious pairing on the chain level.
3.2. Basic properties of the monopole Floer homology. In this section, we recall some basic properties of monopole Floer homology which will be useful in later sections.

First, there are $U$-actions on $H M_{*}^{\circ}(Y, \mathfrak{s})$ and $H M_{\circ}^{*}(Y, \mathfrak{s})$, making them into modules over the polynomial ring $\mathbb{Q}[U]$. The actions are defined as follows: Consider the canonical $S^{1}$-bundle $P$ over $\mathcal{B}^{\sigma}(Y)$, obtained as the quotient of $\mathcal{C}^{\sigma}(Y)$ by the based gauge group (the group of gauge transformations that equal 1 at the base point). Let $\mathcal{M}([\mathfrak{a}],[\mathfrak{b}])$ (resp. $\mathcal{M}^{\text {red }}([\mathfrak{a}],[\mathfrak{b}])$ ) be the moduli spaces of parametrized nonconstant flow lines (resp. reducible flow lines). Evaluating these flow lines at $t=0$ defines the maps
$$r: \mathcal{M}([\mathfrak{a}],[\mathfrak{b}]) \rightarrow \mathcal{B}^{\sigma}(Y) \text { and } r^{\prime}: \mathcal{M}^{\mathrm{red}}([\mathfrak{a}],[\mathfrak{b}]) \rightarrow \mathcal{B}^{\sigma}(Y) .$$
We take a generic section of the line bundle associated to $r^{*}(P)$ (respectively $r^{\prime *}(P)$ ) and use it to cut the 2-dimensional components of the moduli space $\mathcal{M}([\mathfrak{a}],[\mathfrak{b}])$ (respectively $\left.\mathcal{M}^{\text {red }}([\mathfrak{a}],[\mathfrak{b}])\right)$ into a 0-dimensional manifold. By counting points in these cut moduli spaces, one can define linear maps $l_{*}^{*}, \bar{l}_{*}^{*}$ similar to $\partial_{*}^{*}$ and $\bar{\partial}_{*}^{*}$ (see (17) and (18)). Then we define the chain maps
$$\bar{l}: \bar{C} \rightarrow \bar{C}, \quad \check{l}: \check{C} \rightarrow \check{C}, \quad \hat{l}: \widehat{C} \rightarrow \widehat{C}$$
by replacing $\partial_{*}^{*}$ and $\widehat{\partial}_{*}^{*}$ in (19) with $l_{*}^{*}$ and $\widehat{l}_{*}^{*}$ respectively. The induced map on (co)homology defines the $U$-action.

Second, the monopole (co)homology has two gradings: the rational grading and the mod-2 grading. Here we focus on the rational grading, which is only defined when $c_{1}(\mathfrak{s})$ is torsion. There is a grading function
$$\operatorname{gr}^{\mathbb{Q}}: \mathfrak{C} \rightarrow \mathbb{Q} .$$
(see [19, Definition 28.3.1] for definition) which induce a rational grading on $\widetilde{H M}_{*}(Y, \mathfrak{s})$ and $\widehat{H M}_{*}(Y, \mathfrak{s})$. The rational grading on $\overline{H M}_{*}(Y, \mathfrak{s})$ is induced by a lightly modified grading function $\overline{\operatorname{gr}}^{\mathbb{Q}}: \mathfrak{C}^{u} \cup \mathfrak{C}^{\mathfrak{s}} \rightarrow \mathbb{Q}$ defined as
$$\overline{\operatorname{gr}}^{\mathbb{Q}}(\mathfrak{a})=\left\{\begin{array}{ll}
\operatorname{gr}^{\mathbb{Q}}(\mathfrak{a}) & \text { if } \mathfrak{a} \in \mathfrak{C}^{s} \\
\operatorname{gr}^{\mathbb{Q}}(\mathfrak{a})-1 & \text { if } \mathfrak{a} \in \mathfrak{C}^{u}
\end{array} .\right.$$
When $c_{1}(\mathfrak{s})$ is torsion, we will use the notation $H M_{k}^{\circ}(Y, \mathfrak{s})$ to denote the component of $H M_{*}^{\circ}(Y, \mathfrak{s})$ with respect to this rational grading $k$. The $U$-action decrease the rational on $H M_{*}^{\circ}(Y, \mathfrak{s})$ by 2.

Next, there is an exact triangle relating the three flavours of monopole Floer homology:
$$\cdots \xrightarrow{i_{*, Y}} \widetilde{H M}_{*}(Y, \mathfrak{s}) \xrightarrow{j_{*, Y}} \widehat{H M}_{*}(Y, \mathfrak{s}) \xrightarrow{p_{*, Y}} \overline{H M}_{*}(Y, \mathfrak{s}) \xrightarrow{i_{*, Y}} \widehat{H M}_{*}(Y, \mathfrak{s}) \xrightarrow{j_{*, Y}} \cdots .$$
(See [19, Proposition 22.2.1] for a construction.) All the maps in this exact triangle preserve the $U$-action. When $c_{1}(\mathfrak{s})$ is torsion, the maps $i_{*, Y}, j_{*, Y}$ preserve the rational grading and the map $p_{*, Y}$ decrease the rational grading by 1.

Lastly, we discuss how the theory can be simplified when $Y$ is a rational homology 3-sphere. In this case, the curvature equation $F_{B^{t}}=0$ has a unique solution $B_{0}$ up to gauge transformations. One can achieve transversality by introducing a small perturbation $\mathfrak{q}$ with the property that the perturbed curvature equation (15) still have $B_{0}$ as its unique solution. (See [25, Section 2.2] for an explicit construction of such perturbations.) Therefore, the reducible critical points upstairs are exactly $\left\{\left[\left(B_{0}, 0, \psi_{i}\right)\right]\right\}_{i \in \mathbb{Z}}$, where $\psi_{i}$ is a unit-length eigenvalue vector of the perturbed Dirac operator (16).

Moreover, the moduli space of reducible trajectories can be explicitly described. In particular, $\breve{\mathcal{M}}^{\text {red }}\left(\left[\left(B_{0}, 0, \psi_{i}\right)\right],\left[\left(B_{0}, 0, \psi_{j}\right)\right]\right)$ never has a zero-dimensional component so the maps $\bar{\partial}_{*}^{*}$ are vanishing. The only case that $\mathcal{M}^{\text {red }}\left(\left[\left(B_{0}, 0, \psi_{i}\right)\right],\left[\left(B_{0}, 0, \psi_{j}\right)\right]\right)$ has a 2-dimensional component is when $j=i+1$. We have
$$\mathcal{M}^{\mathrm{red}}\left(\left[\left(B_{0}, 0, \psi_{i}\right)\right],\left[\left(B_{0}, 0, \psi_{i+1}\right)\right]\right)=\mathbb{C P}^{1}$$
and $r^{\prime *}(P)$ is the tautological bundle over it. Therefore, the $U$-action on $\overline{H M}_{*}(Y, \mathfrak{s})$ sends $e_{\left[\left(B_{0}, 0, \psi_{i}\right)\right]}$ to $e_{\left[\left(B_{0}, 0, \psi_{i-1}\right)\right]}$. Hence we have an isomorphism:
$$\overline{H M}_{*}(Y, \mathfrak{s}) \cong \mathbb{Q}\left[U, U^{-1}\right] .$$
The image of $p_{*, Y}$ is isomorphic to $\mathbb{Q}[U]$. The Frøyshov invariant $h(Y, \mathfrak{s}) \in \mathbb{Q}$ is defined by the formula
$$-2 h(Y, \mathfrak{s})-2=\min \left\{\overline{\operatorname{gr}}^{\mathbb{Q}}(\mathfrak{a}) \mid \mathfrak{a} \in \operatorname{Im}\left(p_{*}\right)\right\}$$
Namely, $-2 h(Y, \mathfrak{s})-2$ equals the rational grading of the generator of the submodule $\operatorname{Im}\left(p_{*}\right) \subset \overline{H M}_{*}(Y, \mathfrak{s})$.

Recall that a rational homology 3-sphere $Y$ is called an $L$-space (over $\mathbb{Q}$ ) if $p_{*, Y}$ is injective for any spin ${ }^{c}$-structure $\mathfrak{s}$. In this case, $\widehat{H M}_{*}(Y, \mathfrak{s})$ is a free $\mathbb{Q}[U]$-module of rank 1 and the generator has the rational grading $-2 h(Y, \mathfrak{s})-1$.

We end this section by introducing some notations.
Notation 3.1. For any $k \in-2 h(Y, \mathfrak{s})+2 \mathbb{Z}$, we use $\bar{e}_{k}(Y)$ to denote the unique element in $\overline{H M}_{k}(Y, \mathfrak{s})$ represented by a reducible critical point $\left(B_{0}, 0, \psi_{*}\right)$. When $k \geqslant-2 h(Y, \mathfrak{s})$, the element $i_{*, Y}\left(\bar{e}_{k}\right)$ is nonzero in $\widetilde{H M}_{k}(Y, \mathfrak{s})$ and we denote it as $\left[\check{e}_{k}(Y)\right]$. Furthermore, suppose $Y$ is an $L$-space. Then for any $k \in-2 h(Y, \mathfrak{s})-1+2 \mathbb{Z}^{\geqslant 0}$, there is a unique element in $\widehat{H M}_{k}(Y, \mathfrak{s})$ that is sent to $\bar{e}_{k-1}(Y)$ under $p_{*, Y}$. We use $\widehat{e}_{k}(Y)$ to denote this element. Note that unlike $\check{e}_{k}(Y)$ and $\bar{e}_{k}(Y)$, the class $\widehat{e}_{k}(Y)$ is not well-defined for a general rational homology 3-sphere because $p_{*, Y}$ is not necessarily injective.

\section*{4. Maps on induced by family cobordisms}

In this section, we discuss maps between monopole Floer homology induced by families of cobordisms. These maps were defined by Kronheimer-Mrowka [19] for a single cobordism. Although most of our constructions are adapted from there, we still provide some details for the sake of concreteness and completeness.
4.1. Definition of maps induced by family cobordisms. We start by clarifying the meaning of family cobordisms in our setting.

Definition 4.1. Let $Y_{0}, Y_{1}$ be two nonempty, connected oriented 3-manifolds and let $\mathcal{Q}$ be a closed, connected, oriented smooth manifold. A family of cobordisms $\widetilde{W} / \mathcal{Q}$ from $Y_{0}$ to $Y_{1}$ consists of the following data:
\begin{itemize}
\item[-] A smooth fiber bundle $p: \widetilde{W} \rightarrow \mathcal{Q}$ whose total space $\widetilde{W}$ is an oriented manifold and whose fiber $W$ is a smooth, connected 4-manifold with boundary.
\item[-] An orientation preserving diffeomorphism
$$f: \partial \widetilde{W} \stackrel{\cong}{\Rightarrow}\left(-Y_{0} \bigsqcup Y_{1}\right) \times \mathcal{Q}$$
compatible with $p$, called the boundary parameterization of the family. Here $-Y_{0}$ denotes the orientation reversal of $Y_{0}$. (In particular, we only consider bundles that are trivial when restricted to the boundary.)
\end{itemize}

For family cobordisms, we will use the same set of notations as what we used for families of closed manifolds (see Section 2). In particular, we use $W_{b}$ to denote the fiber over $b \in \mathcal{Q}$. And we say the family cobordism is a homology product if the monodromy action of $\pi_{1}(\mathcal{Q})$ on $H_{*}(W ; \mathbb{Z})$ is trivial. We equip the family with a smooth family of metrics $\left\{g_{W_{b}}\right\}$. We require that when restricted to a collar neighborhood $N_{i}$ of the boundary component $Y_{i}$, the metric $g_{W_{b}}$ is isomorphic to the product $[0,1) \times Y_{i}$ for a fixed metric $g_{Y_{i}}$ (independent with $b$ ).

Definition 4.2. Let $T(\widetilde{W} / \mathcal{Q})$ be the vertial tangent bundle and let Fr be its frame bundle. A family spin ${ }^{c}$ structure $\mathfrak{s}_{\widetilde{W}}$ on $\widetilde{W} / \mathcal{Q}$ is a lift of Fr to a principal $\operatorname{Spin}^{c}(4)$-bundle $P_{\mathfrak{s}_{\widetilde{W}}}$. We say $\mathfrak{s}_{\widetilde{W}}$ and $\mathfrak{s}_{\widetilde{W}}^{\prime}$ are isomorphic if there is a bundle isomorphism $P_{\mathfrak{s}_{\widetilde{W}}} \cong P_{\mathfrak{s}_{\widetilde{W}}^{\prime}}$ that covers the identity map on Fr.

Definition 4.3. We say $\mathfrak{s}_{\widetilde{W}}$ is a product on the boundary if under the boundary parameterization (22), the restriction of $\mathfrak{s}_{\widetilde{W}}$ to $\partial \widetilde{W}$ is isomorphic to the pull-back of a spin ${ }^{c}$ -structure $\mathfrak{s}_{Y_{i}}$ on $Y_{i}$ for $i=0,1$. In this case, we call $\left(\widetilde{W} / \mathcal{Q}, \mathfrak{s}_{\widetilde{W}}\right)$ a family $\operatorname{spin}^{c}$-cobordism from $\left(Y_{0}, \mathfrak{s}_{Y_{0}}\right)$ to $\left(Y_{1}, \mathfrak{s}_{Y_{1}}\right)$.

Remark 6. In Definition 4.3, we do not specify an identification between the spinor bundles $\left.S_{\widetilde{W}}^{ \pm}\right|_{\partial \widetilde{W}}$ and $\mathcal{Q} \times S_{Y_{i}}^{ \pm}$. We will choose any such identification when we later define the induced map on monopole Floer homology. This choice does not affect the induced map.

By attaching cylindrical ends $(-\infty, 0] \times Y_{0}$ and $[0, \infty) \times Y_{1}$ fiberwisely (via the boundary parameterization $f$ ), we obtain a family of noncompact cylindrical end manifolds, denoted by $\widetilde{W}^{*} / \mathcal{Q}$. The induced map
$$H M_{*}^{\circ}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right): H M_{*}^{\circ}\left(Y_{0}, \mathfrak{s}_{Y_{0}}\right) \rightarrow H M_{*}^{\circ}\left(Y_{1},, \mathfrak{s}_{Y_{1}}\right)$$
is defined by studying the family Seiberg-Witten equations on $\widetilde{W}^{*} / \mathcal{Q}$.
Since solutions of the Seiberg-Witten equations on $W_{b}^{*}$ usually have infinite $L^{2}$-norms, the blown-up configuration space is defined in a different way from the 3-dimensional case
(14). We define $\mathcal{C}^{\sigma}\left(\widetilde{W}^{*}, \mathfrak{s}_{\widetilde{W}}\right)$ be the space of quadruples $(b, A, \Phi, \phi)$, where $b$ is a point in $\mathcal{Q} ; A$ is a $L_{k, \text { loc }}^{2}$-connection on the spinor bundle $S_{W_{b}^{*}}^{+} ; \phi$ is an element in the topological quotient
$$\left\{\text { nonzero } L_{k, \text { loc }}^{2} \text {-sections of } S_{W_{b}^{*}}^{+}\right\} / \mathbb{R}_{>0}$$
and $\Phi \in \mathbb{R}_{\geqslant 0} \cdot \phi$. We treat $\mathcal{C}^{\sigma}\left(\widetilde{W}^{*}, \mathfrak{s}_{\widetilde{W}}\right)$ as a bundle over $\mathcal{Q}$. The fiber over $b$ is the blown-up configuration space for $W_{b}$ and it is acted upon by the gauge group
$$\mathcal{G}\left(W_{b}\right):=L_{k+3 / 2, \mathrm{loc}}^{2}\left(\operatorname{Map}\left(W_{b}, S^{1}\right)\right) .$$
We use $\mathcal{B}^{\sigma}\left(\widetilde{W}^{*}, \mathfrak{s}_{\widetilde{W}}\right)$ to denote the quotient space of $\mathcal{C}^{\sigma}\left(\widetilde{W}^{*}, \mathfrak{s}_{\widetilde{W}}\right)$ by this fiberwise action.
The blown-up Seiberg-Witten equations on the fiber $W_{b}^{*}$ are written as
$$\begin{array}{r}
\rho\left(F_{A^{t}}^{+}\right)+\left(\Phi \Phi^{*}\right)_{0}=0 \\
\not D_{A}^{+} \phi=0 .
\end{array}$$

Again, one has to introduce suitable perturbations to achieve transversality.
Construction 4.4. We perturb (23) in three steps:
\begin{itemize}
\item[(i)] We choose a smooth family $\tilde{\omega}=\left\{\omega_{b}\right\}_{b \in \mathcal{Q}}$ of self-dual two forms on the fibers $W_{b}$. We require that $\omega_{b}$ is supported in $W_{b} \backslash\left(N_{0} \cup N_{1}\right)$. We use these two forms to perturb the curvature equation into
$$\rho\left(F_{A^{t}}^{+}\right)+\left(\Phi \Phi^{*}\right)_{0}=\rho\left(i \omega_{b}\right) .$$
\item[(ii)] To define the perturbation on the the cylindrical ends $(-\infty, 0] \times Y_{0}$ and $[0,+\infty) \times Y_{1}$, we choose 3-dimensional perturbations $\mathfrak{q}_{i}$ on $Y_{i}(i=0,1)$ so that moduli spaces of Seiberg-Witten flow lines on $Y_{i}$ are regular. We apply the corresponding 4-dimensional perturbations $\hat{\mathfrak{q}}_{0}$ and $\hat{\mathfrak{q}}_{1}$ on the cylindrical ends. (Recall that on cylindrical ends, the 4-dimensional Seiberg-Witten equations can be rewritten as the equations for the Seiberg-Witten flow on $Y_{i}$. Therefore, $\mathfrak{q}_{i}$ induces a perturbation $\hat{\mathfrak{q}}_{i}$ for the 4-dimensional Seiberg-Witten equations.)
\item[(iii)] To define the perturbation on the collar neighborhood $N_{i}$ of $\partial W_{b}$, we choose a smooth family of 3-dimensional perturbations $\left\{\mathfrak{p}_{i, b}^{\prime}\right\}_{b \in \mathcal{Q}}$ on $Y_{i}$. Then we take the following perturbation on $N_{i}=[0,1] \times Y_{i}$ :
$$\hat{\mathfrak{p}}_{i, b}:=\beta(t) \hat{\mathfrak{q}}_{i}+\beta_{0}(t) \hat{\mathfrak{p}}_{i, b}^{\prime} .$$
Here $\beta(t)$ is a cutoff function that equals 1 near $t=0$ and equals 0 near $t=1$. And $\beta_{0}$ is a bump function supported in ( 0,1 ). This is the third part of the perturbation.
\end{itemize}

Remark 7. We briefly explain the purpose of these perturbations. The perturbations $\left\{\omega_{b}\right\}$ in step (i) are introduced to avoid reducible solutions when the fiber $W_{b}$ has positive $b_{2}^{+}$(see Lemma 4.7). Absence of reducible solutions is essential in the definition of $\overrightarrow{H M}_{*}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right)$ but not required in the definition of $\widehat{H M}_{*}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right), \widetilde{H M}_{*}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right)$ and $\overline{H M}_{*}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right)$. So when defining the later three maps, one can simply set $\omega_{b}=0$. The perturbation $\hat{\mathfrak{q}}_{i}$ in step (ii) is introduced to achieve the transversality on $\mathbb{R} \times Y_{i}$, which is necessary to define the monopole Floer homology groups. The perturbations $\left\{\hat{\mathfrak{p}}_{i, b}\right\}$ in step (iii) are introduced
to ensure the transversality of the family Seiberg-Witten equations on $\widetilde{W}^{*}$. Note that the only perturbations we impose on the cylindrical ends are $\hat{\mathfrak{q}}_{i}$, which is fiber-independent.

To simplify our notations, we will use $\hat{\mathfrak{p}}_{b}$ denote the sum of the perturbations in (ii) and (iii). We use $\hat{\mathfrak{p}}_{b}^{0}$ and $\hat{\mathfrak{p}}_{b}^{1}$ to denote its connection component and the spinor component respectively. The triply perturbed blown-up Seiberg-Witten equations on $W_{b}^{+}$can be written as
$$\mathfrak{F}_{\mathfrak{p}_{b}, \omega_{b}}^{\sigma}(A, \phi, \Phi)=0 .$$
We refer to [19, Page 156] for an explicit expression of $\mathfrak{F}_{\tilde{q}_{b}, \omega_{b}}^{\sigma}$. We mention that when $\Phi=0$ (i.e. on the reducibles), the equation (26) can be written as
$$\begin{aligned}
& \rho\left(F_{A^{t}}^{+}\right)=-2 \hat{\mathfrak{p}}_{b}^{0}(A, 0) \\
& \not D_{A, \hat{\mathfrak{p}}_{b}}^{+}(\phi)=0 .
\end{aligned}$$
Here $\not D_{A, \mathfrak{p}_{b}}^{+}$is the perturbed 4-dimensional Dirac operator, defined as
$$\not D_{A, \hat{\mathfrak{p}}_{b}}^{+}(\phi):=\not D_{A}^{+} \phi+\mathcal{D}_{\left(A_{b}, 0\right)} \hat{\mathfrak{p}}_{b}^{1}(0, \phi) .$$

Given critical points $[\mathfrak{a}] \in \mathfrak{C}\left(Y_{0}\right)$ and $[\mathfrak{b}] \in \mathfrak{C}\left(Y_{1}\right)$, we use $\mathcal{B}^{\sigma}\left([\mathfrak{a}], \widetilde{W}^{*}, \mathfrak{s}_{\widetilde{W}},[\mathfrak{b}]\right)$ to denote the subspace of $\mathcal{B}^{\sigma}\left(W^{*}, \mathfrak{s}_{\widetilde{W}}\right)$ consisting of points that satisfy the asymptotic condition
$$\begin{aligned}
& \lim _{t \rightarrow-\infty}\left[\left(\left.A\right|_{\{t\} \times Y_{0}}, \frac{\left.\phi\right|_{\{t\} \times Y_{0}}}{|\phi|_{\{t\} \times Y_{0} \mid L^{2}}},\left.|\Phi|_{\{t\} \times Y_{0}}\right|_{L^{2}}\right)\right]=[\mathfrak{a}] \\
& \lim _{t \rightarrow+\infty}\left[\left(\left.A\right|_{\{t\} \times Y_{1}}, \frac{\left.\phi\right|_{\{t\} \times Y_{1}}}{|\phi|_{\{t\} \times\left. Y_{1}\right|_{L^{2}}}},\left.|\Phi|_{\{t\} \times Y_{1}}\right|_{L^{2}}\right)\right]=[\mathfrak{b}]
\end{aligned}$$
(In particular, this condition requires that $\left.\phi\right|_{\{t\} \times Y_{i}} \neq 0$ when $|t| \gg 0$.)
We consider the moduli space
$$\mathcal{M}\left([\mathfrak{a}], \widetilde{W}^{*}, \mathfrak{s}_{\widetilde{W}},[\mathfrak{b}]\right):=\left\{[(b, A, \phi, \Phi)] \in \mathcal{B}^{\sigma}\left([\mathfrak{a}], \widetilde{W}^{*}, \mathfrak{s}_{\widetilde{W}},[\mathfrak{b}]\right) \text { that satisfies (26) }\right\} .$$
We let $\mathcal{M}^{\text {red }}\left([\mathfrak{a}], \widetilde{W}^{*}, \mathfrak{s}_{\widetilde{W}},[\mathfrak{b}]\right)$ be the subspace of $\mathcal{M}\left([\mathfrak{a}], \widetilde{W}^{*}, \mathfrak{s}_{\widetilde{W}},[\mathfrak{b}]\right)$ that consists of all reducible solutions.

According to the path component of $\mathcal{B}^{\sigma}\left([\mathfrak{a}], \widetilde{W}^{*}, \mathfrak{s}_{\widetilde{W}},[\mathfrak{b}]\right)$, we have the canonical decompositions
$$\begin{gathered}
\mathcal{M}\left([\mathfrak{a}], \widetilde{W}^{*}, \mathfrak{s}_{\widetilde{W}},[\mathfrak{b}]\right)=\bigsqcup_{\left.z \in \pi_{0}\left(\mathcal{B}^{\sigma}\left([\mathfrak{a}], \widetilde{W}^{*}, \mathfrak{s}_{\widetilde{W}},[\mathfrak{b}]\right]\right)\right)} \mathcal{M}_{z}\left([\mathfrak{a}], \widetilde{W}^{*},[\mathfrak{b}]\right), \\
\mathcal{M}^{\mathrm{red}}\left([\mathfrak{a}], \widetilde{W}^{*}, \mathfrak{s}_{\widetilde{W}},[\mathfrak{b}]\right)=\bigsqcup_{z \in \pi_{0}\left(\mathcal{B}^{\sigma}\left([\mathfrak{a}], \widetilde{W}^{*}, \mathfrak{s}_{\widetilde{W}},[\mathfrak{b}]\right)\right)} \mathcal{M}_{z}\left([\mathfrak{a}], \widetilde{W}^{*},[\mathfrak{b}]\right) .
\end{gathered}$$

Remark 8. For each $b \in \mathcal{Q}$, the inclusion map $i_{b}: W_{b} \hookrightarrow \widetilde{W}$ induces a map
$$i_{b}^{*}: \pi_{0}\left(\mathcal{B}^{\sigma}\left([\mathfrak{a}], \widetilde{W}^{*}, \mathfrak{s}_{\widetilde{W}},[\mathfrak{b}]\right)\right) \rightarrow \pi_{0}\left(\mathcal{B}^{\sigma}\left([\mathfrak{a}], W_{b}^{*}, \mathfrak{s}_{W},[\mathfrak{b}]\right)\right) .$$
This map is always a bijection. To see this, we take $[\gamma],\left[\gamma^{\prime}\right] \in \mathcal{B}^{\sigma}\left([\mathfrak{a}], W_{b}^{*}, \mathfrak{s}_{W},[\mathfrak{b}]\right)$. On the cylindrical end $(-\infty, 0] \times Y_{0}, \gamma$ (resp. $\gamma^{\prime}$ ) converges to a critical point $\mathfrak{a}_{1}$ (resp. $\left.\mathfrak{a}_{2}\right)$ in $\mathcal{C}^{\sigma}\left(Y_{0}, \mathfrak{s}_{Y_{0}}\right)$. Let $\gamma_{\mathfrak{a}}$ be a path from $\mathfrak{a}_{1}$ to $\mathfrak{a}_{2}$ and let $\gamma_{\mathfrak{b}}$ be a path in $\mathcal{C}^{\sigma}\left(Y_{1}, \mathfrak{s}_{Y_{1}}\right)$
defined similarly. Then $\gamma_{\mathfrak{a}} \cdot \gamma^{\prime} \cdot \bar{\gamma}_{\mathfrak{b}}$ have the same end points as $\gamma$. The linear homotopy between $\gamma_{\mathfrak{a}} \cdot \gamma^{\prime} \cdot \bar{\gamma}_{\mathfrak{b}}$ and $\gamma$ implies that $\left[\gamma_{\mathfrak{a}} \cdot \gamma^{\prime} \cdot \bar{\gamma}_{\mathfrak{b}}\right]$ and $\left[\gamma^{\prime}\right]$ are in the same component of $\mathcal{B}^{\sigma}\left([\mathfrak{a}], W_{b}^{*}, \mathfrak{s}_{W},[\mathfrak{b}]\right)$. Note that $\gamma_{\mathfrak{a}}$ and $\gamma_{\mathfrak{b}}$ represent elements in $\pi_{1}\left(\mathcal{B}^{\sigma}\left(Y_{0}, \mathfrak{s}_{Y_{0}}\right),[\mathfrak{a}]\right)$ and $\pi_{1}\left(\mathcal{B}^{\sigma}\left(Y_{1}, \mathfrak{s}_{Y_{1}}\right),[\mathfrak{b}]\right)$ respectively. From this construction, we get a transitive action of
$$\pi_{1}\left(\mathcal{B}^{\sigma}\left(Y_{0}, \mathfrak{s}_{Y_{0}}\right),[\mathfrak{a}]\right) \times \pi_{1}\left(\mathcal{B}^{\sigma}\left(Y_{1}, \mathfrak{s}_{Y_{1}}\right),[\mathfrak{b}]\right)$$
on $\pi_{0}\left(\mathcal{B}^{\sigma}\left([\mathfrak{a}], W_{b}^{*}, \mathfrak{s}_{W},[\mathfrak{b}]\right)\right)$. Now we treat $\mathcal{B}^{\sigma}\left([\mathfrak{a}], \widetilde{W}^{*}, \mathfrak{s}_{\widetilde{W}},[\mathfrak{b}]\right)$ as a fiber bundle over $\mathcal{Q}$ with fibers $\left\{\mathcal{B}^{\sigma}\left([\mathfrak{a}], W_{b}^{*}, \mathfrak{s}_{W},[\mathfrak{b}]\right)\right\}$. Since $\widetilde{W}$ is a product near the boundary, $\pi_{1}(\mathcal{Q})$ acts trivially on $\pi_{1}\left(\mathcal{B}^{\sigma}\left(Y_{0}, \mathfrak{s}_{Y_{0}}\right),[\mathfrak{a}]\right) \times \pi_{1}\left(\mathcal{B}^{\sigma}\left(Y_{1}, \mathfrak{s}_{Y_{1}}\right),[\mathfrak{b}]\right)$ and hence also trivially on the set $\pi_{0}\left(\mathcal{B}^{\sigma}\left([\mathfrak{a}], W_{b}^{*}, \mathfrak{s}_{W},[\mathfrak{b}]\right)\right)$. Therefore, the map $i_{b}^{*}$ is an bijection. In Section 4.2, this observation will allow us to compose homotopy classes $z_{1}, z_{2}$ of configurations for two family cobordisms $\widetilde{W}_{01}$ and $\widetilde{W}_{12}$ and obtain a homotopy class $z_{1} \circ z_{2}$ for the composed cobordism $\widetilde{W}_{01} \cup \widetilde{W}_{12}$, without worrying the choice of a fiber.

With a choice of generic perturbations, these moduli spaces are smooth manifolds (possibly with boundaries). Moreover, they are canonically oriented after we choose an orientation of the space
$$H^{1}\left(Y_{0} ; \mathbb{R}\right) \oplus H^{1}\left(W_{b} ; \mathbb{R}\right) \oplus H_{+}^{2}\left(W_{b} ; \mathbb{R}\right)$$
for some $b$ (and hence all $b$ ). By counting points in the zero-dimensional components of $\mathcal{M}\left([\mathfrak{a}], \widetilde{W}^{*}, \mathfrak{s}_{\widetilde{W}},[\mathfrak{b}]\right)$ and $\mathcal{M}^{\text {red }}\left([\mathfrak{a}], \widetilde{W}^{*}, \mathfrak{s}_{\widetilde{W}},[\mathfrak{b}]\right)$, one can define operators
$$m_{o}^{o}: C^{o}\left(Y_{0}\right) \rightarrow C^{o}\left(Y_{1}\right), \quad m_{s}^{o}: C^{o}\left(Y_{0}\right) \rightarrow C^{s}\left(Y_{1}\right), \quad m_{o}^{u}: C^{u}\left(Y_{0}\right) \rightarrow C^{o}\left(Y_{1}\right)$$
and
$$\begin{array}{ll}
\bar{m}_{s}^{s}: C^{s}\left(Y_{0}\right) \rightarrow C^{s}\left(Y_{1}\right), & \bar{m}_{u}^{u}: C^{u}\left(Y_{0}\right) \rightarrow C^{u}\left(Y_{1}\right) \\
\bar{m}_{s}^{u}: C^{u}\left(Y_{0}\right) \rightarrow C^{s}\left(Y_{1}\right), & \bar{m}_{u}^{s}: C^{s}\left(Y_{0}\right) \rightarrow C^{u}\left(Y_{1}\right)
\end{array}$$
respectively. As in [19], we pack these maps as follows:
$$\bar{m}=\left[\begin{array}{cc}
\bar{m}_{s}^{s} & \bar{m}_{s}^{u} \\
\bar{m}_{u}^{s} & \bar{m}_{u}^{u}
\end{array}\right]: \quad \bar{C}\left(Y_{0}\right) \rightarrow \bar{C}\left(Y_{1}\right),$$
$$\widehat{m}=\left[\begin{array}{cc}
m_{o}^{o} & m_{o}^{u} \\
\bar{m}_{u}^{s} \partial_{s}^{o}\left(Y_{0}\right)-\bar{\partial}_{u}^{s}\left(Y_{1}\right) m_{s}^{o} & \bar{m}_{u}^{u}+\bar{m}_{u}^{s} \partial_{s}^{u}\left(Y_{0}\right)-\bar{\partial}_{u}^{s}\left(Y_{1}\right) m_{s}^{u}
\end{array}\right]: \quad \widehat{C}\left(Y_{0}\right) \rightarrow \widehat{C}\left(Y_{1}\right),$$
$$\check{m}=\left[\begin{array}{cc}
m_{o}^{o} & -m_{o}^{u} \bar{\partial}_{u}^{s}\left(Y_{0}\right)-\partial_{o}^{u}\left(Y_{1}\right) \bar{m}_{u}^{s} \\
m_{s}^{o} & \bar{m}_{s}^{s}-m_{s}^{u} \bar{\partial}_{u}^{s}\left(Y_{0}\right)-\partial_{s}^{u}\left(Y_{1}\right) \bar{m}_{u}^{s}
\end{array}\right]: \quad \check{C}\left(Y_{0}\right) \rightarrow \check{C}\left(Y_{1}\right) .$$

Proposition 4.5. The maps $\bar{m}, \breve{m}, \widehat{m}$ are chain maps. The induced maps on homology
$$\begin{aligned}
& \widehat{H M}_{*}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right): \widehat{H M}_{*}\left(Y_{0}, \mathfrak{s}_{Y_{0}}\right) \rightarrow \widehat{H M}_{*}\left(Y_{1}, \mathfrak{s}_{Y_{1}}\right) \\
& \widehat{H M}_{*}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right): \widehat{H M}_{*}\left(Y_{0}, \mathfrak{s}_{Y_{0}}\right) \rightarrow \widehat{H M}_{*}\left(Y_{1}, \mathfrak{s}_{Y_{1}}\right) \\
& \overline{H M}_{*}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right): \overline{H M}_{*}\left(Y_{0}, \mathfrak{s}_{Y_{0}}\right) \rightarrow \overline{H M}_{*}\left(Y_{1}, \mathfrak{s}_{Y_{1}}\right)
\end{aligned}$$
are smooth invariants of $\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right)$. (Namely, they do not depend on auxiliary choices made in the construction such as metrics and perturbations.) They preserve the $U$-actions and commutes with the maps $i_{*}, j_{*}, p_{*}$ in the long exact sequence (21).

Proof. When $\mathcal{Q}$ is a single point, all these claims are proved [19]. In particular, it is proved in [19, Proposition 25.3.4] that $\bar{m}, \breve{m}, \widehat{m}$ are chain maps. By [19, Corollary 25.3.9], the induced maps are independent with the metric $g_{\widetilde{W} / \mathcal{Q}}$ and the perturbations in Step (i) and (iii) of Construction 4.4. Therefore, these maps could only possibly depend on the metric/perturbation $\left(g_{Y_{i}}, \mathfrak{q}_{i}\right)$ on the cylindrical ends. This potential dependence is ruled out as a consequence of the composition law of the cobordism-induced maps ([19, Proposition 26.1.2]). Furthermore, by [19, Proposition 25.5.1 and Corollary 25.5.2], these maps preserve the $U$-action and they commute with $i_{*}, j_{*}, p_{*}$ up to sign.

For a general $\mathcal{Q}$, all the arguments can adapted without essential change. In particular, we will give a proof of the composition law for the induced map by family of cobordisms (see Theorem 4.12). \(\square\)

Next, we discuss a fourth map
$$\overrightarrow{H M}_{*}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right)_{\xi}: \widehat{H M}_{*}\left(Y_{0}, \mathfrak{s}_{Y_{0}}\right) \rightarrow \widetilde{H M}_{*}\left(Y_{1}, \mathfrak{s}_{Y_{1}}\right) .$$
Unlike its cousins in (35), this map is only defined when $b_{2}^{+}(W)>0$. Furthermore, when $\mathfrak{s}_{Y_{0}}$ and $\mathfrak{s}_{Y_{1}}$ are both torsion and $b_{2}^{+}(W)<\operatorname{dim} \mathcal{Q}+1$, this map depends on the choice of a chamber $\xi$ for $\widetilde{W} / \mathcal{Q}$.

We start by assuming that that both $\mathfrak{s}_{Y_{0}}$ and $\mathfrak{s}_{Y_{1}}$ are torsion. For any $b \in \mathcal{Q}$, we consider the space
$$I\left(W_{b}\right):=\operatorname{Image}\left(H^{2}\left(W_{b}, \partial W_{b} ; \mathbb{R}\right) \xrightarrow{l} H^{2}\left(W_{b} ; \mathbb{R}\right)\right),$$
where $l$ is induced by the inclusion map. Then there is a non-degenerate pairing on $I\left(W_{b}\right)$ defined as
$$\langle l(\alpha), l(\beta)\rangle:=(\alpha \cup \beta)\left[W_{b}\right] .$$
(Recall that $b_{2}^{+}\left(W_{b}\right)$ is defined as the maximal dimension of a subspace of $I(W)$ on which this pairing is positive definite.) We can also identify $I\left(W_{b}\right)$ with the space of square-integrable harmonic 2-forms $\kappa$ on $W_{b}^{*}$. For such $\kappa$, we use $[\kappa] \in I\left(W_{b}\right)$ to denote the corresponding cohomology class. For any square-integrable 2-form $\omega$ on $W_{b}^{*}$ (not necessarily harmonic), we use $P_{I}(\omega)$ to denote the unique element in $I\left(W_{b}\right)$ such that
$$\left\langle P_{I}(\omega),[\kappa]\right\rangle=\int_{W_{b}} \omega \wedge \kappa$$
for any square-integrable harmonic 2-form $\kappa$.
The identification between $I\left(W_{b}\right)$ and the space of harmonic forms gives us an involution
$$*_{g_{b}}: I\left(W_{b}\right) \rightarrow I\left(W_{b}\right)$$
As a result, we have an eigenspace decomposition
$$I\left(W_{b}\right)=I^{+}\left(W_{b}, g_{b}\right) \oplus I^{-}\left(W_{b}, g_{b}\right),$$
where $I^{+}\left(W_{b}, g_{b}\right)$ and $I^{-}\left(W_{b}, g_{b}\right)$ denotes the subspace respesnted by self-dual and anti-self dual harmonic 2-forms respectively. We use
$$P_{I^{+}}: I\left(W_{b}\right) \rightarrow I^{+}\left(W_{b}, g_{b}\right)$$
to denote the corresponding projection.

Recall that we chose a family $\widetilde{\omega}=\left\{\omega_{b}\right\}$ of compactly supported 2-forms on $W$ as a first perturbation of the family Seiberg-Witten equations (see Construction 4.4). We make the following definition, which is analogous to Definition 2.2 in the case of family cobordisms.
Definition 4.6. Suppose $c_{1}\left(\mathfrak{s}_{Y_{i}}\right)$ is torsion for $i=0,1$. Then the pair $\left(g_{\widetilde{W} / \mathcal{Q}}, \widetilde{\omega}\right)$ is called admissible (with respect to $\mathfrak{s}_{\widetilde{W}}$ ) if the following inequality holds for any for any $b \in Q$ :
$$P_{I}\left(\omega_{b}\right)+2 \pi P_{I^{+}} c_{1}\left(\mathfrak{s}_{W}\right) \neq 0 .$$

Note that the family metrics $g_{\widetilde{W} / \mathcal{Q}}$ has been chosen so that its restriction to the tubular neighborhood $N_{i}$ is isometric to $[0,1] \times Y_{i}$. We can modify the cobordism by inserting another cylinder $[1, T] \times Y_{i}$ between $N_{i}$ and $W_{b} \backslash N_{i}$. On this new cylinder, we apply no perturbation on the Seiberg-Witten equations. So this modification will not change the admissibility condition.

Lemma 4.7. Consider any collections of perturbations
$$\left\{\omega_{b}\right\}_{b \in Q}, \mathfrak{q}_{0}, \mathfrak{q}_{1},\left\{\mathfrak{q}_{0, b}^{\prime}\right\}_{b \in Q},\left\{\mathfrak{q}_{1, b}^{\prime}\right\}_{b \in Q} .$$
as in Construction 4.4. Suppose $\left(g_{\widetilde{W} / \mathcal{Q}}, \widetilde{\omega}\right)$ is admissible. Then after inserting the cylinder $[1, T] \times Y_{i}$ for $T \gg 0$, we may assume that the perturbed Seiberg-Witten equation (26) has no finite energy reducible solutions for any $b \in \mathcal{Q}$.

Proof. The case $\mathcal{Q}$ equals a point is proved in [19, Proposition 27.2.4]. The key observation is that by inserting $[1, T] \times Y_{i}$, the perturbations introduced in step (ii) and (iii) of Construction 4.4 are pushed far away from the non-cylindrical part of $\widetilde{W}$. And in the limit case, the $\widetilde{\omega}$-perturbed curvature equation (24) has no reducible solution because $\left(g_{\widetilde{W} / \mathcal{Q}^{\prime}}, \widetilde{\omega}\right)$ is admissible. With this observation in mind, proof of the general case is the same. \(\square\)

Under the the perturbations and modified metric in Lemma 4.7, the maps $\bar{m}_{*}^{*}$ are all zero since there are no reducible solutions. We consider the linear map
$$\vec{m}=\left[\begin{array}{cc}
m_{o}^{o} & m_{o}^{u} \\
m_{s}^{o} & m_{s}^{u}
\end{array}\right]: \quad \widehat{C}\left(Y_{0}\right) \rightarrow \check{C}\left(Y_{1}\right),$$

Lemma 4.8. $\vec{m}$ is a chain map. The induced map
$$\vec{m}_{*}: \widehat{H M}_{*}\left(Y_{0}, \mathfrak{s}_{Y_{0}}\right) \rightarrow \widehat{H M}_{*}\left(Y_{1}, \mathfrak{s}_{Y_{1}}\right)$$
preserves the $U$-action. The composition
$$j_{*, Y_{1}} \circ \vec{m}_{*}: \widehat{H M}_{*}\left(Y_{0}, \mathfrak{s}_{Y_{0}}\right) \rightarrow \widehat{H M}_{*}\left(Y_{1}, \mathfrak{s}_{Y_{1}}\right)$$
with the map $j_{1, Y_{1}}$ in (21) equals the cobordism-induced map $\widehat{H M}_{*}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right)$.
Proof. When $\mathcal{Q}$ equals a point, this is proved as [19, Theorem 3.5.3]. The general case is essentially the same. \(\square\)

Like the family Seiberg-Witten invariant, there is a chamber structure on the space of all admissible pairs and the induced map $\vec{m}_{*}$ depends on the choice of chamber. To explain this, we consider the positive cone
$$V^{+}(W):=\{\mathfrak{a} \in \underset{28}{I}(W) \mid\langle\mathfrak{a}, \mathfrak{a}\rangle>0\} .$$
where $\langle\cdot, \cdot\rangle$ is the intersection pairing defined in (37). Because $\widetilde{W}$ is a homology product, we can canonically identify $V^{+}(W)$ with the corresponding space for each fiber $W_{b}$. Therefore, for any admissible pair $\left(g_{\widetilde{W} / \mathcal{Q}}, \widetilde{\omega}\right)$, we have a map
$$b \mapsto P_{I}\left(\omega_{b}\right)+2 \pi P_{I^{+}} c_{1}\left(\mathfrak{s}_{W}\right) \in V^{+}(W) .$$
This gives an element $\xi\left(g_{\widetilde{W} / \mathcal{Q}}, \widetilde{\omega}\right) \in\left[\mathcal{Q}, V^{+}(W)\right]$. We call this homotopy class the chamber of $\left(g_{\widetilde{W} / \mathcal{Q}}, \widetilde{\omega}\right)$.

Lemma 4.9. Any element $\xi \in\left[\mathcal{Q}, V^{+}(W)\right]$ can be realized as the chamber of an admissible pair $\left(g_{\widetilde{W} / \mathcal{Q}}, \widetilde{\omega}\right)$. Furthermore, the induced map (39) only depends on the chamber. We use the notation
$$\overrightarrow{H M}_{*}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right)_{\xi}: \widehat{H M}\left(Y_{0}, \mathfrak{s}_{Y_{0}}\right) \rightarrow \widetilde{H M}\left(Y_{1}, \mathfrak{s}_{Y_{1}}\right)$$
to denote this map.
Proof. When $\mathcal{Q}$ is a single point and $b_{2}^{+}(W) \geqslant 2$, this is proved as Proposition 27.3.4 in [19]. To adapt the proof in our case, we note that any two admissible pairs $\left(g_{\widetilde{W} / \mathcal{Q}, 0}, \widetilde{\omega}_{0}\right)$ and $\left(g_{\widetilde{W} / \mathcal{Q}, 1}, \widetilde{\omega}_{1}\right)$ in the same chamber can be connected by a path $\left\{\left(g_{\widetilde{W} / \mathcal{Q}, t}, \widetilde{\omega}_{t}\right)\right\}_{t \in[0,1]}$ of admissible pairs. After a further small perturbation on this path, one can assume that the parmatrized moduli space over [0, 1] is regular and has no reducible solutions. The rest of the proof follows exactly the same argument as [19]. Note that just as Proposition 4.5, proof of the independence with $\left(g_{Y_{i}}, \mathfrak{q}_{i}\right)$ relies on the composition law of the cobordism-induced maps (Theorem 4.12). \(\square\)

Similar to the case of closed 4-manifolds, a chamber represented by a constant map is called a canonical chamber. Recall that $V^{+}(W)$ is homeomorphic to $\left(\mathbb{R}^{b_{2}^{+}(W)}-\{\overrightarrow{0}\}\right) \times$ $\mathbb{R}^{b^{-}(W)}$. So when $b_{2}^{+}(W) \geqslant 2$, there is a unique canonical chamber $\xi_{c}$. When $b_{2}^{+}(W)=1$, there are two canonical chambers. By picking an orientation on $H_{+}^{2}(W ; \mathbb{R})$, we can talk about the positive canonical chamber $\xi_{c}^{+}$and the negative canonical chamber $\xi_{c}^{-}$. To simply our notation, we also use
$$\overrightarrow{H M}_{*}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right), \quad \overrightarrow{H M}_{*}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right)_{+}, \quad \overrightarrow{H M_{*}}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right)_{-}$$
to denote the maps for $\xi_{c}, \xi_{c}^{+}$and $\xi_{c}^{-}$.
Now we turn to the case that $c_{1}\left(\mathfrak{s}_{Y_{k}}\right)$ is nontorsion from $k=0$ or 1. This case is actually easier: the unperturbed curvature equation on $Y_{k}$ has no solution. As a result, as along as one choose the 3-dimensional perturbation $\mathfrak{q}_{k}$ to be small enough, there will be no reducible critical point on $Y_{k}$, and hence no finite energy reducible solution on $W_{b}$. As a consequence, the map $\vec{m}$ defined in (38) is always a chain map. With $\mathfrak{q}_{0}, \mathfrak{q}_{1}$ fixed, any two choices of possible combinations of perturbations $\left\{\omega_{b}\right\}_{b \in Q},\left\{\mathfrak{q}_{0, b}^{\prime}\right\}_{b \in Q},\left\{\mathfrak{q}_{1, b}^{\prime}\right\}_{b \in Q}$ can be connected by a generic path. Along this path, a reducible solution never appears and a standard cobordism argument shows that the induced map is independent with $\left\{\omega_{b}\right\}_{b \in Q},\left\{\mathfrak{q}_{0, b}^{\prime}\right\}_{b \in Q},\left\{\mathfrak{q}_{1, b}^{\prime}\right\}_{b \in Q}$. The proof of the independence with $\mathfrak{q}_{0}, \mathfrak{q}_{1}$ can be proceed in the same way as Lemma 4.9. We denote the induced map $\vec{m}_{*}$ by
$$\overrightarrow{H M}_{*}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right): \widehat{H M}_{*}\left(Y_{0}, \mathfrak{s}_{Y_{0}}\right) \rightarrow \widetilde{H M}_{*}\left(Y_{1}, \mathfrak{s}_{Y_{1}}\right) .$$

By our discussion above, this is an invariant of $\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right)$. But it is actually not a new one: when $c_{1}\left(\mathfrak{s}_{Y_{k}}\right)$ is nontorsion, the map $j_{*, Y_{k}}$ in (21) is an isomorphism. And one has
$$\overrightarrow{H M}_{*}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right)=j_{*, Y_{1}}^{-1} \circ \widehat{H M}_{*}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right)$$
when $c_{1}\left(\mathfrak{s}_{Y_{1}}\right)$ is nontorsion and
$$\overrightarrow{H M}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right)=\widetilde{H M}_{*}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right) \circ j_{*, Y_{0}}^{-1}$$
when $c_{1}\left(\mathfrak{s}_{Y_{0}}\right)$ is nontorsion. To unify our notation with the torsion case, when $c_{1}\left(\mathfrak{s}_{Y_{k}}\right)$ is nontorsion for some $k$, we simply define
$$\overrightarrow{H M}_{*}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right)_{\xi}:=\overrightarrow{H M}_{*}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right)$$
for any $\xi \in\left[\mathcal{Q}, V^{+}(W)\right]$.
By taking the map induced by $\vec{m}$ on the dual complexes, one can define the induced map on the monopole Floer cohomology
$$\overrightarrow{H M}^{*}\left(\widetilde{W}, \mathfrak{s}_{\widetilde{W}}\right)_{\xi}: \widehat{H M}^{*}\left(Y_{1}, \mathfrak{s}_{Y_{1}}\right) \rightarrow \widehat{H M}^{*}\left(Y_{0}, \mathfrak{s}_{Y_{0}}\right) .$$
4.2. Composition laws for cobordism-induced maps. In this section, we prove the composition laws for various maps induced by family of cobordisms (Theorem 4.12 and Theorem 4.22). These results are proved in [19] when $\mathcal{Q}$ is a single point. So we only sketch the proofs, indicating what adaptions are needed in the family setting. This section will assume readers' familiarity with [19].
4.2.1. The gluing theorem for $\overline{H M}, \widehat{H M}$ and $\widetilde{H M}$. We start by setting up some notations. Given spin ${ }^{c}$ 3-manifolds $\left(Y_{i}, \mathfrak{s}_{Y_{i}}\right)$ for $i=0,1,2$, we consider a family spin ${ }^{c}$ cobordism $\left(\widetilde{W}_{01} / \mathcal{Q}, \mathfrak{s}_{\widetilde{W}_{01}}\right)$ from $\left(Y_{0}, \mathfrak{s}_{Y_{0}}\right)$ to $\left(Y_{1}, \mathfrak{s}_{Y_{1}}\right)$, and a family $\operatorname{spin}^{c} \operatorname{cobordism}\left(\widetilde{W}_{12} / \mathcal{Q}, \mathfrak{s}_{\widetilde{W}_{12}}\right)$ from $\left(Y_{1}, \mathfrak{s}_{Y_{1}}\right)$ to $\left(Y_{2}, \mathfrak{s}_{Y_{2}}\right)$. We assume both families are homology products. By composing the cobordisms fiberwisely, we form a family cobordism $\widetilde{W}_{02} / \mathcal{Q}$ from $Y_{0}$ to $Y_{2}$. For $b \in \mathcal{Q}$, we use $W_{01, b}, W_{12, b}$ and $W_{02, b}$ to denote the corresponding fibers over $b$. As before, we denote the fibers over the base point $b_{0} \in \mathcal{Q}$ by $W_{01}, W_{12}$ and $W_{02}$.

Note that we did not specify a way to the spinor bundles over $\mathcal{Q} \times Y_{1}$ so we do not have a single family spin ${ }^{c}$-structure on $\widetilde{W}_{02} / \mathcal{Q}$. Instead, we consider the set $\mathbb{S}$ of isomorphism classes of family spin ${ }^{c}$ structures $\mathfrak{s}$ on $\widetilde{W}_{02}$ that satisfies
$$\left.\mathfrak{s}\right|_{\widetilde{W}_{01}} \cong \mathfrak{s}_{\widetilde{W}_{01}} \quad \text { and }\left.\quad \mathfrak{s}\right|_{\widetilde{W}_{12}} \cong \mathfrak{s}_{\widetilde{W}_{12}} .$$

Lemma 4.10. $\mathbb{S}$ is an affine set over image of the boundary map
$$\partial: H^{1}\left(Y_{1} ; \mathbb{Z}\right) \rightarrow H^{2}\left(W_{02} ; \mathbb{Z}\right)$$
in the Mayer-Vietoris sequence arising from the decomposition $W_{02}=W_{01} \cup W_{12}$. In particular, $\mathbb{S}$ contains a single element if $Y_{1}$ is a rational homology 3-sphere.

Proof. We let $P_{01}$ and $P_{12}$ be the principal $\operatorname{Spin}^{c}(4)$-bundle for the family spin ${ }^{c}$ structure $\mathfrak{s}_{\widetilde{W}_{01}}$ and $\mathfrak{s}_{\widetilde{W}_{12}}$. We let $P_{1}$ be the principal bundle for the product family $\mathcal{Q} \times\left(Y_{1}, \mathfrak{s}_{Y_{1}}\right)$. We pick specific identifications
$$\tau_{01}:\left.P_{01}\right|_{\mathcal{Q} \times Y_{1}} \cong P_{1} \text { and } \tau_{12}:\left.P_{12}\right|_{\mathcal{Q} \times Y_{1}} \stackrel{\cong}{\Rightarrow} P_{1} .$$

Given any continuous map $f: \mathcal{Q} \times Y_{1} \rightarrow S^{1}$, multiplying $f$ fiberwisely defines a bundle automorphism $\tau_{f}: P_{1} \rightarrow P_{1}$. We can construct a family spin ${ }^{c}$ structure $\mathfrak{s}_{f} \in \mathbb{S}$ by gluing $P_{01}$ and $P_{12}$ together along $\mathcal{Q} \times Y_{1}$ using $\tau_{12}^{-1} \circ \tau_{f} \circ \tau_{01}$. Furthermore, it's straightforward to check that any element in $\mathbb{S}$ arises as some $\mathfrak{s}_{f}$.

Given $f, f^{\prime}$, an isomorphism $\mathfrak{s}_{f} \xrightarrow{\cong} \mathfrak{s}_{f^{\prime}}$ is given by gluing together bundle automorphisms
$$\tau_{g_{01}}: P_{01} \rightarrow P_{01} \quad \text { and } \quad \tau_{g_{12}}: P_{12} \rightarrow P_{12}$$
which are defined as fiberwise multiplication with continuous functions $g_{01}: \widetilde{W}_{01} \rightarrow S^{1}$ and $g_{12}: \widetilde{W}_{12} \rightarrow S^{1}$ respectively. They need to satisfy the compatibility condition
$$\left(\left.g_{12}\right|_{\mathcal{Q} \times Y_{2}}\right) \cdot f=\left(\left.g_{01}\right|_{\mathcal{Q} \times Y_{2}}\right) \cdot f^{\prime} .$$
Here "." means pointwise multiplication. In other words, $\mathfrak{s}_{f} \cong \mathfrak{s}_{f^{\prime}}$ if and only if there exists $g_{01}, g_{12}$ that satisfies (41). Note that $\left[A, S^{1}\right] \cong H^{1}(A ; \mathbb{Z})$ for a general space $A$. We obtain a bijection between $\mathbb{S}$ and cokernel of the map
$$\tilde{i}_{12}: H^{1}\left(\widetilde{W}_{01} ; \mathbb{Z}\right) \oplus H^{1}\left(\widetilde{W}_{12} ; \mathbb{Z}\right) \rightarrow H^{1}\left(\mathcal{Q} \times Y_{1} ; \mathbb{Z}\right)$$
in the Mayer-Vietoris sequence for the decomposition $\widetilde{W}_{02}=\widetilde{W}_{01} \cup \widetilde{W}_{12}$.
Note that the inclusion maps from $\mathcal{Q} \times Y_{1}$ to $\widetilde{W}_{01}$ and $\widetilde{W}_{12}$ preserve the fiber bundle structure. By the naturality of the Serre spectral sequence, we get isomorphisms
$$\begin{aligned}
& H^{1}\left(\widetilde{W}_{01} ; \mathbb{Z}\right) \cong H^{1}\left(W_{01} ; \mathbb{Z}\right) \oplus H^{1}(\mathcal{Q} ; \mathbb{Z}), \\
& H^{1}\left(\widetilde{W}_{12} ; \mathbb{Z}\right) \cong H^{1}\left(W_{12} ; \mathbb{Z}\right) \oplus H^{1}(\mathcal{Q} ; \mathbb{Z}), \\
& H^{1}(\mathcal{Q} \times Y ; \mathbb{Z}) \cong H^{1}(Y ; \mathbb{Z}) \oplus H^{1}(\mathcal{Q} ; \mathbb{Z}) .
\end{aligned}$$
Therefore, the cokernel of $\tilde{i}_{12}$ is isomorphic to the cokernel of the map
$$i_{12}: H^{1}\left(W_{01} ; \mathbb{Z}\right) \oplus H^{1}\left(W_{12} ; \mathbb{Z}\right) \rightarrow H^{1}\left(Y_{1} ; \mathbb{Z}\right)$$
in the Mayer-Vietoris sequence of $W_{02}=W_{01} \cup W_{12}$. This is exactly the image of $\partial$. \(\square\)

Lemma 4.11. The map $H M_{*}^{\circ}\left(\widetilde{W}_{02}, \mathfrak{s}\right)$ is nontrivial for only finitely many $\mathfrak{s} \in \mathbb{S}$.
Proof. There is nothing to prove if $\mathbb{S}$ is a finite set. Suppose $\mathbb{S}$ is an infinite set. Then by Lemma 4.10, the map
$$\partial \otimes \mathbb{R}: H^{1}\left(Y_{2} ; \mathbb{R}\right) \rightarrow H^{2}\left(W_{12} ; \mathbb{R}\right)$$
is nontrivial. By [19, Lemma 3.9.2], this implies that $b_{2}^{+}\left(W_{02}\right)>0$. As a result, we may choose the perturbation forms $\left\{\omega_{b}\right\}$ in (4.4) such that the perturbed family Seiberg-Witten equations has no reducible solutions. In particular, the maps $\bar{m}_{s}^{s}, \bar{m}_{s}^{u}, \bar{m}_{u}^{s}, \bar{m}_{u}^{u}$ are all vanishing. Furthermore, if if $[\mathfrak{a}]$ is boundary stable or $[\mathfrak{b}]$ is boundary unstable then we have
$$\mathcal{M}\left([\mathfrak{a}], \widetilde{W}_{02}^{*}, \mathfrak{s},[\mathfrak{b}]\right)=\varnothing$$
because it can't contain an irreducible solution.
We first assume that $\mathcal{Q}$ is a single point. We fix a critical point $[\mathfrak{a}]$. Then [19, Lemma 25.3.1] implies the following statement: There are only finitely many pairs $(\mathfrak{s},[\mathfrak{b}])$ such that both conditions are satisfied:
\begin{itemize}
\item[(i)] The moduli space $\mathcal{M}\left([\mathfrak{a}], \widetilde{W}_{02}^{*}, \mathfrak{s},[\mathfrak{b}]\right)$ has a (nonempty) 0-dimensional component.
\item[(ii)] [b] is either irreducible or boundary stable.
\end{itemize}

In our case, (ii) is implied by (i) because of (42). So we can conclude that for any $[\mathfrak{a}]$, there are only finitely many $\mathfrak{s}$ such that the corresponding maps $m_{*}^{*}$ do not all vanish on $[\mathfrak{a}]$. From this, we can further deduce that for any fixed element $a \in H M_{*}^{\circ}\left(Y_{0}, \mathfrak{s}_{Y_{0}}\right)$, there are only finitely many $\mathfrak{s} \in \mathbb{S}$ such that $H M_{*}^{\circ}\left(\widetilde{W}_{02}, \mathfrak{s}\right)(a) \neq 0$. This finishes the proof for $\widehat{H M}$ and $\overline{H M}$ because they are finitely generated as $\mathbb{Q}[U]$-modules. The same is true for $\widetilde{H M}$ if $c_{1}\left(\mathfrak{s}_{Y_{0}}\right)$ is nontorsion. When $c_{1}\left(\mathfrak{s}_{Y_{0}}\right)$ is torsion, we may decompose $\widetilde{H M}_{*}\left(Y_{0}, \mathfrak{s}_{Y_{0}}\right)$ as $\widetilde{H M}_{\leqslant N}\left(Y_{0}, \mathfrak{s}_{Y_{0}}\right) \oplus \widetilde{H M}_{>N}\left(Y_{0}, \mathfrak{s}_{Y_{0}}\right)$ according to the rational grading. The first summand is a finite dimensional vector space so our old argument works. Elements in the second summand can be represented by linear combinations of boundary stable critical points with grading greater than $N$. When $N$ is large enough, these critical points are all annihilated by the map $\bar{\partial}_{u}^{s}$. By (34), we see that $\widetilde{H M}_{>N}\left(Y_{0}, \mathfrak{s}_{Y_{0}}\right)$ is in the kernel of $\widetilde{H M}\left(\widetilde{W}_{02}, \mathfrak{s}\right)$ for any $\mathfrak{s} \in \mathbb{S}$. This finishes the proof when $\mathcal{Q}$ is a single point.

The above argument relies on the finiteness result [19, Lemma 25.3.1], which is a consequence of the compactness theorem [19, Proposition 24.6.4]. For a general compact base $\mathcal{Q}$, this compactness theorem (and hence the finiteness result) can be adapted without essential difficulty. The rest of the proof can be proceeded in the same way. \(\square\)

Now we state the first composition law.
Theorem 4.12. (1) Suppose $\left(\widetilde{W}_{01}, \mathfrak{s}_{\widetilde{W}_{01}}\right)$ is the product family associated to a single spin ${ }^{c}$ cobordism $\left(W_{01}, \mathfrak{s}_{W_{01}}\right)$. Then we have
$$\sum_{\mathfrak{s} \in \mathbb{S}} \widehat{H M}_{*}\left(\widetilde{W}_{02}, \mathfrak{s}\right)=\widehat{H M}_{*}\left(W_{01}, \mathfrak{s}_{W_{01}}\right) \circ \widehat{H M}_{*}\left(\widetilde{W}_{12}, \mathfrak{s}_{\widetilde{W}_{12}}\right)$$
(2) Suppose $\left(\widetilde{W}_{12}, \mathfrak{s}_{\widetilde{W}_{12}}\right)$ is the product family associated to a $\operatorname{spin}^{c}$ cobordism $\left(W_{12}, \mathfrak{s}_{W_{12}}\right)$. Then we have
$$\sum_{\mathfrak{s} \in \mathbb{S}} \widehat{H M}_{*}\left(\widetilde{W}_{02}, \mathfrak{s}\right)=\widehat{H M}_{*}\left(\widetilde{W}_{01}, \mathfrak{s}_{\widetilde{W}_{01}}\right) \circ \widehat{H M}_{*}\left(W_{12}, \mathfrak{s}_{W_{12}}\right) .$$
(3) Parallel results hold for $\overline{H M}$ and $\widetilde{H M}$.

Theorem 4.12 is a family version of [19, Proposition 26.1.2] and the proof here is adapted from there. All these adaptions are inessential (although some are not completely obvious). For the sake of completeness, we will sketch the major steps of the proof in the family setting, emphasizing all the adaptions we need.

We will be dealing with two similar but different situations (either $\widetilde{W}_{01}$ or $\widetilde{W}_{12}$ is a product family). So we first set up a general framework without assuming that any of them is a product. Then we specify to one of the two cases and discuss extra constrains coming from the product structure.
4.2.2. The general setup. We use $N_{0}, N_{1}$ to denote collar neighborhoods of the boundary component $Y_{0}, Y_{1}$ in the fibers of $\widetilde{W}_{01}$ and we use $N_{1}^{\prime}, N_{2}$ to denote collar neighborhoods of the boundary component $Y_{1}, Y_{2}$ in the fibers of $\widetilde{W}_{12}$. We equip $\widetilde{W}_{01}$ and $\widetilde{W}_{12}$ with
family metrics $g_{\widetilde{W}_{01}}$ and $g_{\widetilde{W}_{12}}$ which are isomorphic to $[0,1] \times Y_{*}$ when restricts to these collar neighborhoods. For any $S>0$, we consider the family cobordism $\widetilde{W}(S)$ obtained by inserting a neck of length $2 S$ in the middle. So the fiber of $\widetilde{W}(S)$ over $b$ is given by
$$W(S)_{b}:=W_{01, b} \cup\left([-S, S] \times Y_{1}\right) \cup W_{12, b} .$$
By further attaching cylindrical ends $(-\infty, 0] \times Y_{0}$ and $[0, \infty) \times Y_{1}$ on each fiber, we obtain the family $\widetilde{W}(S)^{*}$.

Construction 4.13. We specify a set of perturbations on $\widetilde{W}(S)^{*}$ in three steps. (c.f. Construction 4.4.)
\begin{itemize}
\item[(i)] We pick smooth families $\left\{\omega_{b}^{01}\right\},\left\{\omega_{b}^{12}\right\}$ of self-dual 2-forms $\widetilde{W}_{01}$ and $\widetilde{W}_{12}$, with the requirement that $\omega_{b}^{01}$ and $\omega_{b}^{12}$ vanishes on $N_{0} \cup N_{1}$ and $N_{1}^{\prime} \cup N_{2}$ respectively.
\item[(ii)] Then we pick tame, admissible perturbations $\mathfrak{q}_{0}, \mathfrak{q}_{1}, \mathfrak{q}_{2}$ on $Y_{0}, Y_{1}, Y_{2}$. We add the corresponding 4-dimensional perturbations $\hat{\mathfrak{q}}_{0}, \hat{\mathfrak{q}}_{1}, \hat{\mathfrak{q}}_{2}$ on the cylindrical parts $(-\infty, 0] \times Y_{0},[-S, S] \times Y_{1},[0, \infty) \times Y_{2}$ of each fiber.
\item[(iii)] We pick families of 3-dimensional perturbations $\left\{\mathfrak{p}_{0, S, b}^{\prime}\right\},\left\{\mathfrak{p}_{1, S, b}^{\prime}\right\},\left\{\mathfrak{p}_{1, S, b}^{\prime \prime}\right\},\left\{\mathfrak{p}_{2, S, b}^{\prime}\right\}$ on $Y_{0}, Y_{1}, Y_{1}, Y_{2}$. Similar to (25), we then add the following 4-dimensional perturbations
$$\begin{array}{ll}
\beta(t) \hat{\mathfrak{q}}_{0}+\beta_{0}(t) \hat{\mathfrak{p}}_{0, S, b}^{\prime}, & \beta(t) \hat{\mathfrak{q}}_{1}+\beta_{0}(t) \hat{\mathfrak{p}}_{1, S, b}^{\prime} \\
\beta(t) \hat{\mathfrak{q}}_{1}+\beta_{0}(t) \hat{\mathfrak{p}}_{1, S, b}^{\prime \prime}, & \beta(t) \hat{\mathfrak{q}}_{2}+\beta_{0}(t) \hat{\mathfrak{p}}_{2, S, b}^{\prime}
\end{array}$$
on $N_{0}, N_{1}, N_{1}^{\prime}$ and $N_{2}$ respectively.
\end{itemize}

Let $[\mathfrak{a}]$ and $[\mathfrak{b}]$ be a pair of critical points for $\left(Y_{0}, \mathfrak{s}_{Y_{0}}\right)$ and $\left(Y_{2}, \mathfrak{s}_{Y_{2}}\right)$. For any homotopy class
$$z \in \bigcup_{\mathfrak{s} \in \mathbb{S}} \pi_{0}\left(\mathcal{B}^{\sigma}\left([\mathfrak{a}], \widetilde{W}_{02}^{*}, \mathfrak{s},[\mathfrak{b}]\right),\right.$$
we consider the moduli space
$$\mathcal{M}_{z}([\mathfrak{a}],[\mathfrak{b}])=\bigcup_{S \in[0,+\infty)}\{S\} \times \mathcal{M}_{z}\left([\mathfrak{a}], \widetilde{W}(S)^{*},[\mathfrak{b}]\right),$$
which admits an obvious projection map to $[0,+\infty)$. By the same argument as $[19$, Proposition 26.1.3], one can prove that under suitable perturbations, the moduli space $\mathcal{M}_{z}([\mathfrak{a}],[\mathfrak{b}])$ is a smooth manifold with boundary for any $z,[\mathfrak{a}],[\mathfrak{b}]$ and the boundary is the fiber over $S=0$.

To compactify $\mathcal{M}_{z}([\mathfrak{a}],[\mathfrak{b}])$, we first compactify each fiber
$$\{S\} \times \mathcal{M}_{z}\left([\mathfrak{a}], \widetilde{W}(S)^{*},[\mathfrak{b}]\right)$$
into
$$\{S\} \times \mathcal{M}_{z}^{+}\left([\mathfrak{a}], \widetilde{W}(S)^{*},[\mathfrak{b}]\right),$$
by adding in broken trajectories on the fibers $\left\{W(S)_{b}\right\}$ in the homotopy class $z$. The result is still not compact due the non-compactness of the base $[0,+\infty)$. So we further add the
fiber over $S=\infty$, which we denote by $\mathcal{M}_{z}^{+}\left([\mathfrak{a}], \widetilde{W}(\infty)^{*},[\mathfrak{b}]\right)$. An element in this space is a quintuple $\left(\left[\breve{\gamma}_{0}\right],\left[\gamma_{01}\right],\left[\breve{\gamma}_{1}\right],\left[\gamma_{12}\right],\left[\breve{\gamma}_{2}\right]\right)$, where
$$\begin{aligned}
& {\left[\breve{\gamma}_{0}\right] \in \breve{\mathcal{M}}^{+}\left([\mathfrak{a}],\left[\mathfrak{a}_{0}\right]\right),} \\
& {\left[\gamma_{01}\right] \in \mathcal{M}\left(\left[\mathfrak{a}_{0}\right], W_{01, b}^{*},\left[\mathfrak{a}_{1}\right]\right),} \\
& {\left[\breve{\gamma}_{1}\right] \in \breve{\mathcal{M}}^{+}\left(\left[\mathfrak{a}_{1}\right],\left[\mathfrak{b}_{1}\right]\right),} \\
& {\left[\gamma_{12}\right] \in \mathcal{M}\left(\left[\mathfrak{b}_{1}\right], W_{12, b}^{*},\left[\mathfrak{b}_{2}\right]\right),} \\
& {\left[\breve{\gamma}_{2}\right] \in \breve{\mathcal{M}}^{+}\left(\left[\mathfrak{b}_{2}\right],[\mathfrak{b}]\right) .}
\end{aligned}$$
Here $\left[\mathfrak{a}_{i}\right]$ and $\left[\mathfrak{b}_{i}\right]$ are critical points on $Y_{i}$ and $\breve{\mathcal{M}}^{+}(-)$denotes the moduli space of broken trajectories on $Y_{i}$. (We allow an unbroken constant trajectory in this moduli space.) We require that the homotopy classes compose to give $z$ and that $\left[\gamma_{01}\right]$ and $\left[\gamma_{12}\right]$ are over the same point $b \in \mathcal{Q}$. Note that on the fiber over $S=\infty$, we are using the same perturbations $\left\{\omega_{b}^{01}\right\},\left\{\omega_{b}^{12}\right\}, \mathfrak{q}_{0}, \mathfrak{q}_{1}, \mathfrak{q}_{2}$ as finite $S$. And we set $\left\{\mathfrak{p}_{0, \infty, b}^{\prime}\right\},\left\{\mathfrak{p}_{1, \infty, b}^{\prime}\right\},\left\{\mathfrak{p}_{1, \infty, b}^{\prime \prime}\right\},\left\{\mathfrak{p}_{2, \infty, b}^{\prime}\right\}$ to be limits of $\left\{\mathfrak{p}_{0, S, b}^{\prime}\right\},\left\{\mathfrak{p}_{1, S, b}^{\prime}\right\},\left\{\mathfrak{p}_{1, S, b}^{\prime \prime}\right\},\left\{\mathfrak{p}_{2, S, b}^{\prime}\right\}$ as $S \rightarrow \infty$. (Perturbations for finite $S$ are chosen such that these limits exist.)

We use $\mathcal{M}_{z}^{+}([\mathfrak{a}],[\mathfrak{b}])$ to denote the space
$$\mathcal{M}_{z}^{+}([\mathfrak{a}],[\mathfrak{b}])=\bigcup_{S \in[0,+\infty]}\{S\} \times \mathcal{M}_{z}^{+}\left([\mathfrak{a}], \widetilde{W}(S)^{*},[\mathfrak{b}]\right) .$$
When $\mathcal{Q}$ is a point, the topology on $\mathcal{M}_{z}^{+}([\mathfrak{a}],[\mathfrak{b}])$ is defined in [19, Page 539]. The topology for a general $\mathcal{Q}$ can be defined similarly. The following theorem is a family version of [19]. The proof is essential identical so we omit it.

Theorem 4.14. For any $[\mathfrak{a}],[\mathfrak{b}], z$, the moduli space $\mathcal{M}_{z}^{+}([\mathfrak{a}],[\mathfrak{b}])$ is compact.
There is the following finiteness result, which is a family version of [19, Lemma 26.1.5]. Again, the proof is essentially the same and omitted.

Lemma 4.15. For any $[\mathfrak{a}], d_{0}$ and $i_{0}$, there are only finitely many pairs $(z,[\mathfrak{b}])$ such that
\begin{itemize}
\item[(i)] the moduli space $\mathcal{M}_{z}^{+}([\mathfrak{a}],[\mathfrak{b}])$ is non-empty;
\item[(ii)] the dimension of the moduli space is at most $d_{0}$;
\item[(iii)] if $\mathfrak{s}_{Y_{2}}$ is torsion, then $\operatorname{gr}^{\mathbb{Q}}([\mathfrak{b}]) \geqslant i_{0}$.
\end{itemize}

The moduli space $\mathcal{M}_{z}^{+}([\mathfrak{a}],[\mathfrak{b}])$ is a stratified space and there are two types of strata:
\begin{itemize}
\item[(I)] The first type of strata do not intersect the fiber over $S=\infty$. These strata are products of moduli spaces of unbroken solutions. A typical example is
$$\breve{\mathcal{M}}_{z_{0}}\left([\mathfrak{a}],\left[\mathfrak{a}_{0}\right]\right) \times \mathcal{M}_{z_{1}}\left(\left[\mathfrak{a}_{0}\right],\left[\mathfrak{b}_{2}\right]\right) \times \breve{\mathcal{M}}_{z_{2}}\left(\left[\mathfrak{b}_{2}\right],[\mathfrak{b}]\right)$$
for some critical points $\left[\mathfrak{a}_{0}\right]$ and $\left[\mathfrak{b}_{2}\right]$ on $Y_{0}$ and $Y_{2}$ respectively.
\item[(II)] The second type of strata are contained in the fiber over $S=\infty$. These strata involve fiber products over $\mathcal{Q}$. A typical exam of such strata is
$$\mathcal{M}_{z_{0}}\left([\mathfrak{a}], \widetilde{W}_{01}^{*},\left[\mathfrak{a}_{1}\right]\right) \times_{\mathcal{Q}}\left(\breve{\mathcal{M}}_{z_{1}}\left(\left[\mathfrak{a}_{1}\right],\left[\mathfrak{b}_{1}\right]\right) \times \mathcal{Q}\right) \times_{\mathcal{Q}} \mathcal{M}_{z_{2}}\left(\left[\mathfrak{b}_{1}\right], \widetilde{W}_{12}^{*},[\mathfrak{b}]\right) .$$
for some critical points $\left[\mathfrak{a}_{1}\right]$ and $\left[\mathfrak{b}_{1}\right]$ on $Y_{1}$.
\end{itemize}

Definition 4.16. We say the moduli space $\mathcal{M}_{z}^{+}([\mathfrak{a}],[\mathfrak{b}])$ is regular if the following conditions are both satisfied:
\begin{itemize}
\item[(1)] All factors of all these strata are regular (see [19, Definition 24.4.9]).
\item[(2)] The projection map
$$\mathcal{M}_{z_{0}}\left(\left[\mathfrak{a}_{0}\right], \widetilde{W}_{01}^{*},\left[\mathfrak{a}_{1}\right]\right) \times \mathcal{M}_{z_{1}}\left(\left[\mathfrak{b}_{1}\right], \widetilde{W}_{12}^{*},\left[\mathfrak{b}_{2}\right]\right) \rightarrow \mathcal{Q} \times \mathcal{Q}$$
is transverse to the diagonal whenever $\mathcal{M}_{z_{0}}\left(\left[\mathfrak{a}_{0}\right], \widetilde{W}_{01}^{*},\left[\mathfrak{a}_{1}\right]\right)$ and $\mathcal{M}_{z_{1}}\left(\left[\mathfrak{b}_{1}\right], \widetilde{W}_{12}^{*},\left[\mathfrak{b}_{2}\right]\right)$ appear as two factors of a same strata of type (II).
\end{itemize}

The following result is a family version of [19, Proposition 26.1.6]. The proof is essential identical.

Proposition 4.17. Assume $\mathcal{M}_{z}^{+}([\mathfrak{a}],[\mathfrak{b}])$ is regular. And suppose that the moduli space $\mathcal{M}_{z}([\mathfrak{a}],[\mathfrak{b}])$ contains irreducible solutions and has dimension $d+1$. Then $\mathcal{M}_{z}^{+}([\mathfrak{a}],[\mathfrak{b}])$ is a space stratified by manifolds and has $\mathcal{M}_{z}([\mathfrak{a}],[\mathfrak{b}])$ as its top stratum. In the fiber over $S=\infty$, the strata of dimension $d$ are the top strata of the following pieces of $\mathcal{M}_{z}^{+}\left([\mathfrak{a}], \widetilde{W}(\infty)^{*},[\mathfrak{b}]\right)$ :
\begin{itemize}
\item[(i)] $\widetilde{\mathcal{M}}_{01} \times_{\mathcal{Q}} \widetilde{\mathcal{M}}_{12}$,
\item[(ii)] $\breve{\mathcal{M}}_{0} \times\left(\widetilde{\mathcal{M}}_{01} \times_{\mathcal{Q}} \widetilde{\mathcal{M}}_{12}\right)$,
\item[(iii)] $\widetilde{\mathcal{M}}_{01} \times_{\mathcal{Q}}\left(\breve{\mathcal{M}}_{1} \times \mathcal{Q}\right) \times_{\mathcal{Q}} \widetilde{\mathcal{M}}_{12}$,
\item[(iv)] $\left(\widetilde{\mathcal{M}}_{01} \times_{\mathcal{Q}} \widetilde{\mathcal{M}}_{12}\right) \times \breve{\mathcal{M}}_{2}$,
\end{itemize}
where $\widetilde{\mathcal{M}}_{i j}$ denotes a typical moduli space on $\widetilde{W}_{i j}$ and $\breve{\mathcal{M}}_{i}$ denotes a typical moduli space (of unparametrized, possibly broken trajectories) on $\mathbb{R} \times Y_{i}$. In the last three cases, the middle one in the three moduli spaces is boundary-obstructed. In The moduli space has a codimension-1 $\delta$-structure along the strata in the last three cases, and is a manifold with boundary along the stratum in the first case.
4.2.3. Proof of Theorem 4.12. Our argument will be an adaption of the argument in [19, Section 26.2] to the family setting. We focus on Part (1) as the other parts are essential the same. For rest of the proof, we assume $\left(\widetilde{W}_{01}, \mathfrak{s}_{\widetilde{W}_{01}}\right)$ is a product family associated to a single cobordism $\left(W_{01}, \mathfrak{s}_{W_{01}}\right)$.
Construction 4.18. We start by choosing appropriate perturbations in this setting:
\begin{itemize}
\item[(1)] Since we are dealing with induced maps on $\widetilde{H M}$, by Remark 17, we may set the perturbation 2-forms $\left\{\omega_{01, b}\right\}$ and $\left\{\omega_{12, b}\right\}$ to be identically zero.
\item[(2)] We choose perturbations $p_{1, \infty}^{\prime \prime}$ (resp. $p_{2, \infty}^{\prime \prime}$ ) and on $Y_{1}$ (resp. $Y_{2}$ ) such that the moduli space $\mathcal{M}_{z}\left([\mathfrak{a}], W_{12}^{*},[\mathfrak{b}]\right)$ is regular for any $[\mathfrak{a}],[\mathfrak{b}]$ and $z$.
\item[(3)] We define the family perturbations $\left\{p_{1, \infty, b}^{\prime \prime}\right\}$ and $\left\{p_{2, \infty, b}^{\prime}\right\}$ by setting $p_{1, \infty, b}^{\prime \prime}=p_{1, \infty}^{\prime \prime}$ and $p_{2, \infty, b}^{\prime}=p_{2, \infty}^{\prime}$ for any $b \in \mathcal{Q}$. Then the family moduli space $\mathcal{M}_{z}\left([\mathfrak{a}], \widetilde{W}_{12}^{*},[\mathfrak{b}]\right)$ is automatically regular and we have the diffeomorphism
$$\mathcal{M}_{z}\left([\mathfrak{a}], \widetilde{W}_{12}^{*},[\mathfrak{b}]\right) \cong \mathcal{Q} \times \mathcal{M}_{z}\left([\mathfrak{a}], W_{12}^{*},[\mathfrak{b}]\right] .$$
\item[(4)] We also choose family perturbations $\left\{p_{0, \infty, b}^{\prime}\right\}$ and $\left\{p_{1, \infty, b}^{\prime}\right\}$ on $Y_{0}$ and $Y_{1}$ such that the moduli space $\mathcal{M}_{z}\left([\mathfrak{a}], \widetilde{W}_{12}^{*},[\mathfrak{b}]\right)$ is always regular.
\end{itemize}
\begin{itemize}
\item[(5)] On the fiber over $S=0$, we pick family perturbations $\left\{p_{0,0, b}^{\prime}\right\},\left\{p_{1,0, b}^{\prime}\right\},\left\{p_{1,0, b}^{\prime \prime}\right\}$ and $\left\{p_{2,0, b}^{\prime}\right\}$ such that the moduli space $\mathcal{M}_{z}\left([\mathfrak{a}], \widetilde{W}_{02}^{*},[\mathfrak{b}]\right)$ is regular for any $[\mathfrak{a}],[\mathfrak{b}]$ and $z$. (Recall that $\widetilde{W}(0)^{*}=\widetilde{W}_{02}^{*}$.)
\item[(6)] By the same argument as [19, Proposition 24.4.10], we can find family perturbations $\left\{p_{0, S, b}^{\prime}\right\},\left\{p_{1, S, b}^{\prime}\right\},\left\{p_{1, S, b}^{\prime \prime}\right\}$ and $\left\{p_{2, S, b}^{\prime}\right\}$ that extend the corresponding perturbations at $S=0$ and $S=\infty$ and make the compactified parametrized moduli space $\mathcal{M}_{z}^{+}([[\mathfrak{a}]],[\mathfrak{b}])$ regular for any $[\mathfrak{a}]$, [b] and $z$. Note that the second condition in Definition 4.16 is automatically satisfied because of equation (44).
\end{itemize}

Again because of (44), the four types of strata in Proposition 4.17 become the following strata
$$\begin{aligned}
\text { (i) } \mathcal{M}_{01} \times \widetilde{\mathcal{M}}_{12}, & \text { (ii) } \breve{\mathcal{M}}_{0} \times \mathcal{M}_{01} \times \widetilde{\mathcal{M}}_{12} \\
\text { (iii) } \mathcal{M}_{01} \times \breve{\mathcal{M}}_{1} \times \widetilde{\mathcal{M}}_{12}, & \text { (iv) } \mathcal{M}_{01} \times \widetilde{\mathcal{M}}_{12} \times \breve{\mathcal{M}}_{2} .
\end{aligned}$$
Here $\mathcal{M}_{01}$ denotes a typical moduli space on the single cobordism $W_{01}$.
We have the following Proposition regarding the boundary orientations of these strata.
Proposition 4.19. Suppose the moduli space $\mathcal{M}_{z}([\mathfrak{a}],[\mathfrak{b}])$ in Proposition 4.17 contains irreducible solutions and has dimension $d+1$. Then the four types of strata (45) differ from their boundary orientations by the signs
\begin{itemize}
\item[(i)] $1 \cdot(-1)^{d_{01} \cdot \operatorname{dim}(\mathcal{Q})}$
\item[(ii)] $(-1)^{d_{0}+d_{01}+1} \cdot(-1)^{\left(d_{0}+d_{01}-1\right) \cdot \operatorname{dim}(\mathcal{Q})}$
\item[(iii)] $(-1)^{d_{1}} \cdot(-1)^{\left(d_{01}+d_{1}-1\right) \cdot \operatorname{dim}(\mathcal{Q})}$
\item[(iv)] $(-1) \cdot(-1)^{d_{01} \cdot \operatorname{dim}(\mathcal{Q})}$
\end{itemize}
accordingly, where $d_{0}$ and $d_{1}$ are the dimensions of the parametrized moduli spaces $\mathcal{M}_{0}$ and $\mathcal{M}_{1}$, (so the dimension of $\breve{\mathcal{M}}_{i}$ equals $d_{i}-1$ ) and $d_{01}$ is the dimension of $\mathcal{M}_{01}$.

Proof. This is a family version of [19, Proposition 26.1.7]. One can give a prove by unwinding the gluing construction and adapting the corresponding arguments in [19]. But the argument is long and tedious. Instead, we give an indirect proof here.