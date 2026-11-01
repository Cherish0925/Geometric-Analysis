---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 2407_10217.pdf
converter: mathpix
format: mmd
---

\title{
COMPARING KÄHLER CONE AND SYMPLECTIC CONE OF ONE-POINT BLOWUP OF ENRIQUES SURFACE
}

\author{
SHENGZHEN NING
}

\begin{abstract}
We follow the study by Cascini-Panov ([CP12]) on symplectic generic complex structures on Kähler surfaces with $p_{g}=0$, a question proposed by Tian-Jun Li in Li08, by demonstrating that the one-point blowup of an Enriques surface admits non-Kähler symplectic forms. This phenomenon relies on the abundance of elliptic fibrations on Enriques surfaces, characterized by various invariants from algebraic geometry. We also provide a quantitative comparison of these invariants to further give a detailed examination of the distinction between Kähler cone and symplectic cone.
\end{abstract}

\section*{Contents}
1. Introduction ..... 1
2. Enriques surface as smooth manifold ..... 5
2.1. Some standard facts and notations ..... 5
2.2. Diffeomorphism group action and normalized fundamental chamber ..... 7
3. Enriques surface as complex manifold ..... 9
3.1. Some standard facts and notations ..... 10
3.2. Period domain and Torelli theorem ..... 11
3.3. $\Phi$-invariant, Seshadri constant and algebraic capacity ..... 12
4. Enriques surface as symplectic manifold ..... 14
4.1. Gromov-Taubes and Seiberg-Witten invariants ..... 15
4.2. Symplectic cone of $S$ ..... 17
5. Proof of the main theorems ..... 18
References ..... 19

\section*{1. Introduction}

Let $(X, \omega)$ be a closed symplectic manifold. It is called non-Kähler if $\omega$ is not compatible with any complex structure $J$ on $X$. In other words, $\omega(\cdot, J \cdot)$ doesn't define a Riemannian metric on $X$. Let's emphasize that the notion 'non-Kähler' here should be understood to describe the symplectic manifold $(X, \omega)$ or the symplectic form $\omega$ rather than only the manifold ${ }^{1} X$.

A well-known fact in symplectic geometry is that the space of compatible almost complex structures is always non-empty and contractible. Sometimes it's also worthwhile to investigate its subspace consisting of the integrable ones. For example, when $X$ is a rational ruled surface, [AGK09] shows that the inclusion of

\footnotetext{
${ }^{1}$ By manifold, we always mean a smooth oriented closed manifold. The symplectic, complex or Kähler structure has to be compatible with the orientation.
}
this subspace is a weak homotopy equivalence (in particular, non-empty) which plays an essential role in their study of the topology of the symplectomorphism groups. Nevertheless, it is possible for this subspace consisting of compatible complex structures to be empty for many other symplectic manifolds. The first such example is due to Thurston. In [Thu76], he revisited Kodaira's example of a complex surface with odd first Betti number, which is topologically a torus bundle over torus. Since then more and more examples have been discovered with different techniques showing the non-Kählerness in both dimension 4 and higher dimensions. The first simply connected example was given by [McD84] in higher dimension using symplectic blowup operation. Now, setting aside the variety of examples found in higher dimensions, we will concentrate on dimension 4 and the known examples ${ }^{2}$ can actually be classified (very roughly) into three categories.
\begin{itemize}
\item[(1)] The manifold $X$ admits no complex structure. In this category, one can apply results from the theory of complex surface such as Kodaira's classification and Noether's inequality. For example, the solvmanifolds in [FG90] and the manifolds constructed from fiber sum operations in [Gom95]. When gauge theory came into play, there were more examples such as the homotopy K3 surfaces in [GM93] using Donaldson's invariants or the knot surgery manifolds $E(1)_{K}$ for some fibered knot $K$ in [Par04] using Seiberg-Witten invariants, which share the feature that the smooth structures are exotic.
\item[(2)] The manifold $X$ can either admit complex structure or not, but it admits no Kähler structure. The first example [Thu76] belongs to this category, where the topological constraint of even first Betti number was used. Other than the parity of Betti numbers, other topological constraints on Kähler manifolds such as formality, fundamental group and hard Lefschetz property can also be used to construct examples in this category. For instance, all nilmanifolds other than $T^{4}$ (see [TO97]), Gompf's symplectic manifolds with $\pi_{1}$ not satisfying the condition like [JR87] and some $S^{1}$-bundles over mapping torus with degenerate cup product on $H^{1}$ constructed in [Bal05, BL05].
\item[(3)] The manifold $X$ admits Kähler structure. In this case, one has to construct a symplectic form on the manifold underlying a Kähler surface and then argue it can not be the Kähler form of any complex structure. [Dra99] showed for all $b_{2}^{+}>1$ minimal Kähler surface of general type, one can deform the Kähler form in the direction along the real part of holomorphic 2-form to obtain a symplectic form which will be non-Kähler due to Hodge index theorem. More examples in this category include $T^{4} \# \overline{\mathbb{C P}^{2}}$ in LMS13, and $\left(S^{2} \times T^{2}\right) \# \overline{\mathbb{C P}^{2}}$ and Burniat surface (of general type and $b_{2}^{+}=1$ ) in [CP12].
\end{itemize}

Note that subtlety exists in the above classification. For instance, there are examples that deviate from the topological constraints of Kähler manifolds but with even first Betti number $b_{1}$. This would eventually imply $X$ admits no complex structure due to [Buc99, Lam99]. However we are more willing to put it into category (2) rather than (1) since the constraints really come from the property of being Kähler. Moreover, the hard Lefschetz property, though we stated it in category (2), can be employed to build examples in category (3) in higher dimension. See [Cho16] for his example of an $S^{2}$-bundle over the K3 surface which admits Kähler

\footnotetext{
${ }^{2}$ Obviously, it is unrealistic to give a complete list all the known examples here. I feel sorry for the authors whose examples are not mentioned here due to my limited knowledge.
}
structure and also symplectic forms of non-hard Lefschetz type. It's interesting to see whether one can still find such an example in dimension 4.

It seems that examples in the category (3) are the most limited among the three. The purpose of this paper is to add another example into this category, which is the one point blowup of Enriques surface as suggested by the title. The motivation for studying such an example is that the authors of [CP12] forgot to add the minimal assumption in their statement of Proposition 4.2 (although they added the assumption in their Question 4.1). Moreover, in the end of [CP12] the authors were asking for an example with finite fundamental group. And Enriques surface has fundamental group $\mathbb{Z}_{2}$.

Our approach of showing non-Kählerness is in the same spirit of [LMS13] and [CP12]. By combining results from both algebraic geometry and symplectic geometry, we can compare the Kähler cone with the symplectic cone which we now define. For a manifold $X$, we define its symplectic cone to be
$$\mathcal{C}(X):=\left\{x \in H^{2}(X ; \mathbb{R}) \mid x \text { is represented by a symplectic form }\right\} .$$
If $J$ is a complex structure on $X$, then the $J$-Kähler cone and Kähler cone are defined to be
$\mathcal{K}_{J}(X):=\left\{x \in H^{2}(X ; \mathbb{R}) \mid x\right.$ is represented by a symplectic form compatible with $\left.J\right\}$,
$$\mathcal{K}(X):=\bigcup_{\text {all complex structures } J} \mathcal{K}_{J}(X) .$$
We use $S$ to denote the Enriques surface and $\tilde{S}$ its blowup. Then our main result can be formulated by the following.

Theorem 1.1. $\mathcal{C}(\tilde{S}) \neq \mathcal{K}(\tilde{S})$.
Remark 1.2. Obviously, the distinction between Kähler cone and symplectic cone implies the existence of non-Kähler symplectic form. However it remains unclear whether the equality of two cones would imply all symplectic forms are Kähler. For Kodaira dimension $-\infty$ manifolds, this implication holds true since all cohomologous symplectic forms are diffeomorphic (see Li08]). For Kodaira dimension $\geq 0$ manifolds, less is known but there is a speculation by Donaldson that one can attack this problem via almost Kähler Calabi-Yau equation (see [Don06]).

Our example has $b_{2}^{+}=1$. Under such circumstances, the symplectic cone and each $J$-Kähler cone are both open in $H^{2}(X ; \mathbb{R})$. Moreover, LL01] shows that $\mathcal{C}(X)$ is a disjoint union of $\mathcal{C}_{K}(X)$ for all $K \in H^{2}(X ; \mathbb{Z})$, where
$\mathcal{C}_{K}(X):=\left\{x \in \mathcal{C}(X) \mid x\right.$ is represented by a symplectic form $\omega$ with $\left.c_{1}(X, \omega)=-K\right\}$.
[Li08] introduced the concept of the so-called symplectic generic complex structure, which just means the complex structure $J$ with its canonical class $K_{J}$ satisfies $\mathcal{C}_{K_{J}}(X)=\mathcal{K}_{J}(X)$. Li08, Question 4.6] further asked about the existence of a symplectic generic complex structure on a $b_{2}^{+}=1$ manifold admitting Kähler structure. Since we prove that even the union of all $\mathcal{K}_{J}(\tilde{S})$ 's can not be the entire $\mathcal{C}(\tilde{S})$, the manifold $\tilde{S}$ doesn't admit symplectic generic complex structure by uniqueness of symplectic canonical class on $S$ (see the beginning of Section 4). Due to the examples given by [CP12] and our Theorem 1.1, we would like to update the question here.

Question 1.3 (Refinement of Li08 Question 4.6). Which manifolds X, underlying a minimal Kähler surface with $b_{2}^{+}(X)=1$, allow for demonstrating the absence of a symplectic generic complex structure on the blowup manifold $X \# n \overline{\mathbb{C P}^{2}}$ for some $n \geq 0$ ?

Remark 1.4. Question 1.3 is open for $X=\mathbb{C P}^{2}$, which is related to some famous conjectures on rational surfaces such as Nagata conjecture and SHGH conjecture. We refer to [Bir99] for the exploration in this direction, including the relation to symplectic packing problems.

Now we briefly explain the reason why the blowup of Enriques surface could serve as an example of non-Kähler symplectic manifold. The proof of Theorem 1.1 will rely on the abundance of elliptic fibrations on Enriques surface. Roughly speaking, this means when the manifold $S$ is equipped with any complex structure $J$, one can always think of $S$ covered by an $S^{2}$-family of $J$-holomorphic tori. The proper transforms of these tori in the blowup manifold $(\tilde{S}, \tilde{J})$ will provide the obstructions for a cohomology class of $\tilde{S}$ being Kähler. On the other hand, when the complex structure $\tilde{J}$ is deformed into a generic almost complex structure, these proper transforms will not persist by Gromov's theory in symplectic geometry. Hence, the classes of these proper transforms don't provide obstructions for a class being symplectic, which cause the distinction between Kähler cone and symplectic cone.

To make the previous illustration more precise, we need a quantitative characterization of the non-Kählerness which is encoded by the relations among several important invariants coming from algebraic geometry. Assume $L$ is a nef line bundle on an Enriques surface $S$. These invariants, introduced by various individuals at different times and for distinct purposes, are (see Section 3.3 for more precise definitions)
\begin{itemize}
\item[-] $\Phi$-invariant introduced in [Cos85]
$$\Phi(L):=\inf \left\{L \cdot C \mid C^{2}=0, C \in \operatorname{Pic}(S) \text { is effective }\right\} .$$
\item[-] Seshadri constant introduced in Dem92
$$\varepsilon_{s}(S, L):=\inf \left\{\left.\frac{L \cdot C}{\nu(C, s)} \right\rvert\, C \text { is an irreducible curve passing through } s\right\},$$
where $s$ is a point on $S$.
\item[-] Algebraic capacities introduced in [Wor21, Wor22]
$$c_{k}^{\text {alg }}(S, L):=\inf \left\{L \cdot C \mid C^{2}-K_{S} \cdot C \geq 2 k, C \in \operatorname{Pic}(S) \text { is nef }\right\},$$
where $k$ is an integer and $K_{S}$ denotes the canonical class.
\end{itemize}

Although they are defined for line bundles, in Section 2 we will have a polytope $\Delta$ (polyhedra cone $\tilde{\Delta}$ ) of dimension nine (ten) which is a fundamental domain under the diffeomorphism group and $\mathbb{R}^{+}$-rescaling (without $\mathbb{R}^{+}$-rescaling) actions on $H^{2}(S ; \mathbb{R})$, where all these invariants can be viewed as functions and compared. This will be convenient for the computational purposes. Our Theorem 1.1 actually follows from the following comparison results.

Theorem 1.5. Suppose the ample cone of the Enriques surface contains the interior of the $\tilde{\Delta}$, then the $\Phi$-invariant, Seshadri constant and algebraic capacities can be
naturally viewed as functions over $\Delta$ (or $\tilde{\Delta}$ ) such that
$$\sup _{s \in S} \varepsilon_{s} \leq 2 c_{0}^{a l g}=2 \Phi$$

We end this introduction section by a digression on the $b_{2}^{+}>1$ case.
Remark 1.6. When $b_{2}^{+}(X)>1$ each $\mathcal{K}_{J}(X)$ is contained in a proper linear subspace $H_{J}^{1,1}(X ; \mathbb{R}) \subseteq H^{2}(X ; \mathbb{R})$. Although it doesn't make sense to talk about symplectic generic complex structure, one can still ask whether $\mathcal{C}(X)=\mathcal{K}(X)$ or not. Note that by [Dra99] and the fact that Kodaira dimension $-\infty$ manifolds have $b_{2}^{+}=1$, we only need to consider Kodaira dimension 0 or 1. For torus bundle over torus, [Gei92] fully determined the symplectic cone. [LMS13] studied the unobstructedness of ball packing for $T^{4}$ and obtained the information about $\mathcal{C}(X)$ for one-point blowup of $T^{4}$. This was further generalized by [EV16] to manifolds admitting IHS hyperkähler structures. For elliptic surfaces $E(m)$ with $m>2$, Ham14 obtained some partial information about $\mathcal{C}(X)$. See also [LU06] for their effort in understanding $\mathcal{C}(X)$ by doing negative inflations. On the other hand, much less is known for $\mathcal{K}(X)$. [LMS13] verified $\mathcal{K}(X)$ is strictly smaller than $\mathcal{C}(X)$ for onepoint blowup of $T^{4}$ by utilizing results regarding the Seshadri constant on principally polarized abelian surfaces .

\section*{2. Enriques surface as smooth manifold}
2.1. Some standard facts and notations. Of course, we have to firstly give the most indispensable definition in this paper.

Definition 2.1. An Enriques surface is a compact complex surface satisfying
\begin{itemize}
\item[-] (regularity) $q:=\operatorname{dim} H^{1}(\mathcal{O})=0$;
\item[-] (non-trivial canonical bundle) $K \neq \mathcal{O}$;
\item[-] (2-torsion canonical bundle) $K^{\otimes 2}=\mathcal{O}$.
\end{itemize}

We recall some standard facts and refer to [BHPVdV04, FM94, Dol16] for more details. Firstly, due to the fundamental result by Horikawa ([Hor78]), all Enriques surfaces are deformation equivalent as complex surfaces, hence oriented diffeomorphic. We thus denote by $S$ the underlying closed oriented smooth 4-manifold. There are numerous methods available for constructing such a manifold. Here we only list few of them from the topological perspective.
\begin{itemize}
\item[-] ([GS99]) Quotient of the complete intersection $S(2,2,2) \subseteq \mathbb{C P}^{5}$, namely the K3 surface defined by quadratic polynomial equations $p_{i}\left(z_{0}, z_{1}, z_{2}\right)+$ $q_{i}\left(z_{3}, z_{4}, z_{5}\right)=0$ for $i=1,2,3$, by the $\mathbb{Z}_{2}$-action of the free involution $\left[z_{0}: z_{1}: z_{2}: z_{3}: z_{4}: z_{5}\right] \mapsto\left[z_{0}: z_{1}: z_{2}:-z_{3}:-z_{4}:-z_{5}\right]$.
\item[-] ([GS99]) Logarithmic transform $E(1)_{2,2}$ of the rational elliptic surface $E(1)=$ $\mathbb{C P}^{2} \# 9 \overline{\mathbb{C P}^{2}}$.
\item[-] ( Ush09 ) Fiber sum $E(1) \#_{T^{\prime}=T} S^{2} \times T^{2}$ along the embedded tori $T^{\prime} \subseteq E(1)$ and $T \subseteq S^{2} \times T^{2}$ representing the anti-canonical class.
\item[-] ([Dor15]) Rational blowdown of a (-4)-sphere within the homology class $6 H-\sum_{i=1}^{10} E_{i}$ in $\mathbb{C P}^{2} \# 10 \overline{\mathbb{C P}^{2}}$, where $H$ is the line class and $E_{i}$ 's are exceptional classes.
\item[-] ([LS10]) Torus fibration over the base $\mathbb{R P}^{2}$ with 12 nodal singular fibers.
\end{itemize}

Remark 2.2. Note that [CP12, Lemma 3.2] shows any complex surface homeomorphic to $\left(T^{2} \times S^{2}\right) \# \overline{\mathbb{C P}^{2}}$ must be biholomorphic to the blowup of a minimal elliptic ruled surface. However, the same statement doesn't hold for Enriques surface since [Oko88] shows that for relatively prime, odd, positive integers $(p, q) \neq(1,1)$, the logarithmic transforms $E(1)_{2 p, 2 q}$ of the rational elliptic surface are complex surfaces homeomorphic but not diffeomorphic to $S$ (which are called the fake Enriques surfaces).

Remark 2.3. If we reverse the orientation of $S$ to get $\hat{S}$, then it is neither complex nor symplectic. On the one hand, from $c_{1}^{2}(\hat{S})=3 \sigma(\hat{S})+2 e(\hat{S})=3 \cdot 8+2 \cdot 12=$ $48>36=3 c_{2}(\hat{S})$ one sees that $\hat{S}$ can not be complex by Bogomolov-Miyaoka-Yau inequality. On the other hand, as we will see later, $S$ contains embedded (-2)-spheres so that $\hat{S}$ will contain embedded (+2)-spheres. Then by FS95, Proposition 5.1] or [Kot97, Proposition 1] all Seiberg-Witten invariants of $\hat{S}$ vanish, which is impossible for a symplectic manifold by [Tau95].

By the previous two remarks, we emphasize that throughout our discussions, by $S$ we mean the smooth oriented manifold not priorly equipped with any geometric structure. The basic topological invariants of $S$ are summarized by the following chart.

\begin{tabular}[t]{|l|l|l|l|l|l|}
\hline $\pi_{1}(S)$ & $H^{2}(S ; \mathbb{Z})$ & $Q_{S}$ & $b_{2}^{+}(S)$ & $e(S)$ & $\sigma(S)$ \\
\hline $\mathbb{Z}_{2}$ & $\mathbb{Z}^{10} \oplus \mathbb{Z}_{2}$ & $-E_{8} \oplus U$ & 1 & 12 & -8 \\
\hline
\end{tabular}

The rank 10 even unimodular lattice $-E_{8} \oplus U$, which is the intersection form of $S$, is called the Enriques lattice. Following the notation of [Cos85], we always choose a basis $\left\{r_{0}, r_{1}, \cdots, r_{7}, s_{1}, s_{2}\right\}$ for this lattice, where $r_{0}, r_{1}, \cdots, r_{7}$ all have square -2 and form a basis of $-E_{8}$ with Dynkin diagram
![](https://cdn.mathpix.com/cropped/4c88ca62-a5be-4ea0-bcbd-9a1e0f9476c8-06.jpg?height=126&width=472&top_left_y=1492&top_left_x=825)
and $s_{1}, s_{2}$ are the basis for the hyperbolic plane $U$ with $s_{1}^{2}=s_{2}^{2}=0, s_{1} \cdot s_{2}=1$. Let $I_{1,10}$ be the unimodular lattice of rank 11 coming from the intersection form of $\mathbb{C P}^{2} \# 10 \overline{\mathbb{C P}^{2}}$. Take the basis $\left\{l_{0}, l_{1}, \cdots, l_{10}\right\} \subseteq I_{1,10}$ such that $l_{0}^{2}=1, l_{1}^{2}=$ $\cdots=l_{10}^{2}=-1$ and $l_{i} \cdot l_{j}=0$ for all $i \neq j$. We use $k$ to denote the element $-3 l_{0}+l_{1}+\cdots+l_{10} \in I_{1,10}$. Let $-\mathbb{1}_{e}$ be the rank 1 lattice with $e^{2}=-1$. Then there is an isomorphism
$$\Psi:-\mathbb{1}_{e} \oplus-E_{8} \oplus U \rightarrow I_{1,10}$$
by sending
$$\begin{gathered}
e \mapsto-k, \\
r_{0} \mapsto l_{0}-l_{1}-l_{2}-l_{3}, \\
r_{i} \mapsto l_{i}-l_{i+1}, 1 \leq i \leq 7, \\
s_{1} \mapsto 3 l_{0}-l_{1}-\cdots-l_{8}-l_{9}, \\
s_{2} \mapsto 3 l_{0}-l_{1}-\cdots-l_{8}-l_{10} .
\end{gathered}$$
We also let $r_{8}:=l_{8}-l_{9}$ and $r_{9}:=l_{9}-l_{10}$ be two elements in the Enriques lattice under the above identification. After tensoring with $\mathbb{R}$, this isomorphism $\Psi$ can be upgraded into an isomorphism
$$\Psi_{\mathbb{R}}: H^{2}(\tilde{S} ; \mathbb{R}) \rightarrow I_{1,10} \otimes_{\mathbb{Z}} \mathbb{R}$$
where the subspace $H^{2}(S ; \mathbb{R}) \subseteq H^{2}(S ; \mathbb{R}) \oplus \mathbb{R} e=H^{2}(\tilde{S} ; \mathbb{R})$ is sent to the orthogonal complement of $k$. Define the positive cone
$$\mathcal{P}_{\tilde{S}}:=\left\{x^{2}>0 \mid x \in H^{2}(\tilde{S} ; \mathbb{R})\right\} .$$
It has two connected components and one of them contains the class $l_{0}$ under the identification $\Psi_{\mathbb{R}}$ which we will denote by $\mathcal{P}_{\tilde{S}}^{\prime}$ and call it the forward cone. Similarly, for $H^{2}(S ; \mathbb{R})$ we use $\mathcal{P}_{S}$ to denote its positive cone and $\mathcal{P}_{S}^{\prime}$ its component that is contained in $\mathcal{P}_{\tilde{S}}^{\prime}$.

The manifold $S$ has a universal covering space $\pi: T \rightarrow S$. When the manifold $T$ is equipped with a complex structure, it's called a K3 surface. The basic topological invariants for $T$ are the following.

\begin{tabular}[t]{|l|l|l|l|l|l|}
\hline $\pi_{1}(T)$ & $H^{2}(T ; \mathbb{Z})$ & $Q_{T}$ & $b_{2}^{+}(T)$ & $e(T)$ & $\sigma(T)$ \\
\hline 0 & $\mathbb{Z}^{22}$ & $2\left(-E_{8}\right) \oplus 3 U$ & 3 & 24 & -16 \\
\hline
\end{tabular}

We denote by $\iota$ the covering involution on $T$ so that $S=T / \iota$. Then the action $\iota^{*}$ on $H^{2}(T ; \mathbb{Z})$ is given by
$$\iota^{*}\left(x \oplus y \oplus z_{1} \oplus z_{2} \oplus z_{3}\right)=y \oplus x \oplus-z_{1} \oplus z_{3} \oplus z_{2},$$
where $x, y$ belong to the two $-E_{8}$ components and $z_{1}, z_{2}, z_{3}$ belong to the three $U$ components. Let $Q_{T}^{+}\left(Q_{T}^{-}\right)$be the $\iota^{*}$-invariant (anti-invariant) sublattice of $Q_{T}$. Then we see that
$$\begin{gathered}
Q_{T}^{+}=\left\{x \oplus x \oplus 0 \oplus z \oplus z \mid x \in-E_{8}, z \in U\right\} \\
Q_{T}^{-}=\left\{x \oplus-x \oplus z_{1} \oplus z_{2} \oplus-z_{2} \mid x \in-E_{8}, z_{1}, z_{2} \in U\right\},
\end{gathered}$$
which are of rank 10 and 12 respectively. The pullback map $\pi^{*}: Q_{S} \rightarrow Q_{T}$ will send $x \oplus z \in-E_{8} \oplus U$ to $x \oplus x \oplus 0 \oplus z \oplus z \in Q_{T}^{+} \subseteq Q_{T}$, which defines a lattice isomorphism between $Q_{S}$ and $Q_{T}^{+}$but does not preserve the bilinear form. Indeed, $\left(\pi^{*}(\alpha), \pi^{*}(\beta)\right)=2(\alpha, \beta)$.
2.2. Diffeomorphism group action and normalized fundamental chamber.

By diffeomorphisms we always mean the orientation-preserving ones. Since we are interested in the Kähler cone and symplectic cone which are the domains invariant under the action by diffeomorphisms, it's important to figure out how the diffeomorphism group $\operatorname{Diff}^{+}(S)$ or $\operatorname{Diff}^{+}(\tilde{S})$ acts on $H^{2}(S ; \mathbb{R})$ or $H^{2}(\tilde{S} ; \mathbb{R})$. [L98] investigates the image of the natural map
$$\psi_{X}: \operatorname{Diff}^{+}(X) \rightarrow O\left(Q_{X}\right)$$
from the diffeomorphism group to the isometry group of the intersection form for all relatively minimal elliptic surfaces $X$ with positive Euler number. We will need the special case for Enriques surface summarized by the following theorem. Recall that (for example, see [FM88, Proposition 2.4]) an embedded sphere representing class $\alpha$ with self-intersection (-2) or (-1) will give a diffeomorphism whose cohomological action is the reflection $R_{\alpha}$ which maps any class $\beta$ to $\beta-2 \frac{(\alpha, \beta)}{(\alpha, \alpha)} \alpha$. An isometry in $O\left(Q_{S}\right)$ is said to have real spinor norm one if it preserves the forward cone $\mathcal{P}_{S}^{\prime}$.

Theorem 2.4 ([L9̈8] Theorem 7, Lemma 7). For the manifold $S$, we have the following:
\begin{itemize}
\item[-] Every class in $Q_{S}$ of square (-2) can be represented by a smoothly embedded 2-sphere. Diff ${ }^{+}(S)$ acts transitively on all (-2)-classes.
\end{itemize}
\begin{itemize}
\item[-] The reflections along all (-2)-classes generate an index 2 subgroup $O^{\prime}\left(Q_{S}\right)$ of $O\left(Q_{S}\right)$ consisting of elements with real spinor norm one. Moreover, this subgroup can be generated by finitely many reflections along $r_{0}, r_{1}, \cdots, r_{8}, r_{9}$.
\item[-] There exists a diffeomorphism on $S$ inducing - id on $Q_{S}$ and therefore, $\psi_{S}$ is surjective.
\end{itemize}

It's known that for Kähler surfaces ([Bru96], [FM97]) or more generally symplectic 4-manifolds ([Li99]) of non-negative Kodaira dimension, up to sign the classes represented by smoothly embedded (-1)-spheres are exactly the same as the ones represented by holomorphic or symplectic embedded (-1)-spheres. Consequently $\pm e$ are the only classes that can be represented smoothly embedded (-1)-sphere in $\tilde{S}$. As a result we have the immediate corollary:

Corollary 2.5. The image of $\psi_{\tilde{S}}$ splits as $O\left(Q_{S}\right) \times \mathbb{Z}_{2}$, where $\mathbb{Z}_{2}$ denotes the reflection along the (-1)-class e.

Observe that the positive cone $\mathcal{P}_{S}$ is invariant under the entire diffeomorphism group $\operatorname{Diff}^{+}(S)$ and the component $\mathcal{P}_{S}^{\prime}$ is invariant under the ones inducing isometries of $Q_{S}$ with real spinor norm one. Also there is the obvious $\mathbb{R}^{+}$-action on $\mathcal{P}_{S}^{\prime}$ by rescaling. There is an explicit domain $\Delta$, which we call it the normalized fundamental chamber, parametrizing the quotient of these actions. Let
$$\Delta:=\left\{\left(b_{1}, b_{2}, \cdots, b_{10}\right) \in \mathbb{R}^{10} \mid \sum_{i=1}^{10} b_{i}=3, b_{1}+b_{2}+b_{3} \leq 1, b_{1} \geq b_{2} \geq \cdots \geq b_{10}>0\right\}$$
be the region in $\mathbb{R}^{10}$ and $\bar{\Delta}$ be its closure. Note that $\bar{\Delta}$ is a convex polytope of dimension 9 sitting inside $\mathbb{R}^{10}$. It has 9 vertices
$$\begin{aligned}
V_{1} & =\frac{1}{7}(3,2,2,2,2,2,2,2,2,2) \\
V_{2} & =\frac{1}{14}(5,5,4,4,4,4,4,4,4,4) \\
V_{3} & =\frac{1}{21}(7,7,7,6,6,6,6,6,6,6) \\
V_{4} & =\frac{1}{18}(6,6,6,6,5,5,5,5,5,5) \\
V_{5} & =\frac{1}{15}(5,5,5,5,5,4,4,4,4,4) \\
V_{6} & =\frac{1}{12}(4,4,4,4,4,4,3,3,3,3) \\
V_{7} & =\frac{1}{9}(3,3,3,3,3,3,3,2,2,2) \\
V_{8} & =\frac{1}{6}(2,2,2,2,2,2,2,2,1,1) \\
V_{9} & =\frac{1}{3}(1,1,1,1,1,1,1,1,1,0)
\end{aligned}$$
and $\bar{\Delta} \backslash \Delta$ is exactly the single point $V_{9}$. Any point $\left(b_{1}, \cdots, b_{10}\right) \in \bar{\Delta}$ corresponds to the class $\mathbf{b}:=l_{0}-\sum_{i=1}^{10} b_{i} l_{i} \in H^{2}(S ; \mathbb{R})$. Since $\bar{\Delta}$ is the convex hull of its vertices, by checking the values at all vertices one can see that $\mathbf{b} \in \mathcal{P}_{S}^{\prime}$ for all points in $\Delta$. The next lemma follows from some general results in Coxeter theory (Hum90). We include a proof in our specific case for completeness, which is a minor modification of the MathSciNet reivew of [KK17] by Weiyi Zhang.

Lemma 2.6. The action of $\operatorname{Diff}^{+}(S) \times \mathbb{R}^{+}$on $\mathcal{P}_{S}$ has a fundamental domain naturally parametrized by $\Delta$.

Proof. By Theorem 2.4, the quotient of $\mathcal{P}_{S}$ by the entire diffeomorphism group is the same as the quotient of $\mathcal{P}_{S}^{\prime}$ by the reflections along (-2)-classes $r_{0}, r_{1}, \cdots, r_{8}, r_{9}$. Note that the group $O^{\prime}\left(Q_{S}\right)$ with the generating set $\left\{r_{0}, r_{1}, \cdots, r_{8}, r_{9}\right\}$ forms a Coxeter system. By [Hum90, Section 5.13], the following domain
$$\tilde{\Delta}:=\left\{\left(a, b_{1}, b_{2}, \cdots, b_{10}\right) \in \mathbb{R}^{11} \mid \sum_{i=1}^{10} b_{i}=3 a, b_{1}+b_{2}+b_{3} \leq a, b_{1} \geq b_{2} \geq \cdots \geq b_{10}\right\}$$
is the fundamental domain of the Tits cone $U:=\bigcup_{g \in O^{\prime}\left(Q_{S}\right)} g \tilde{\Delta}$ acted by $O^{\prime}\left(Q_{S}\right)$. To prove our statement, it suffices to show every element in $\mathcal{P}_{S}^{\prime}$ can be transformed into $\tilde{\Delta}$ by reflections. Now a key input from [Hum90, Section 5.13] is that the Tits cone is convex, which allows us to only consider integral classes by rescaling and convex combination. The elements $a l_{0}-\sum_{i=1}^{10} b_{i} l_{i} \in \mathcal{P}_{S}^{\prime}$ are characterized by
$$a>0,3 a=\sum_{i=1}^{10} b_{i}, a^{2}>\sum_{i=1}^{10} b_{i}^{2} .$$
Note that the reflections along $l_{i}-l_{j}$ or $l_{0}-l_{i}-l_{j}-l_{k}$ have the effect switching the coefficients
$$\left(b_{i}, b_{j}\right) \mapsto\left(b_{j}, b_{i}\right)$$
or
$$\left(a, b_{i}, b_{j}, b_{k}\right) \mapsto\left(2 a-b_{i}-b_{j}-b_{k}, a-b_{j}-b_{k}, a-b_{i}-b_{k}, a-b_{i}-b_{j}\right) .$$
For elements in $\mathcal{P}_{S}^{\prime}$ with integer coefficients, one can repeat the procedure of choosing three biggest $b_{i}, b_{j}, b_{k}$ and whenever $a>b_{i}+b_{j}+b_{k}$ applying reflection along $l_{0}-l_{i}-l_{j}-l_{k}$. Since each reflection decreases $a$ by at least 1 and the reflection preserves the connected component $\mathcal{P}_{S}^{\prime}$, after finitely many steps and applying reflections along $l_{i}-l_{j}$, we will get a non-increasing sequence $\left(b_{1}, \cdots, b_{10}\right)$ with $3 a=\sum_{i=1}^{10} b_{i}$ and $a \geq b_{1}+b_{2}+b_{3}$. It's easy to see from Cauchy-Schwarz inequality that these conditions force $b_{10}>0$ since $a^{2}>\sum_{i=1}^{10} b_{i}^{2}$. Therefore after normalizing the coefficient $a$ to 1 by the $\mathbb{R}^{+}$-action, we get an element in $\Delta$. \(\square\)

Remark 2.7. The polytope $\Delta$ actually coincides with the ' $c_{1}=0$ '-part of the normalized symplectic reduced cone of $\mathbb{C P}^{2} \# 10 \overline{\mathbb{C P}^{2}}$ (for example, see [LLW22]). Since cohomologous symplectic forms on Kodaira dimension $-\infty$ manifolds are diffeomorphic (Li08]), this implies there is a bijection between $\Delta$ and the space of symplectic forms $\omega$ on $\mathbb{C P}^{2} \# 10 \overline{\mathbb{C P}^{2}}$ satisfying $\omega \cdot c_{1}(\omega)=0$ modulo the action by Diff ${ }^{+}\left(\mathbb{C P}^{2} \# 10 \overline{\mathbb{C P}^{2}}\right) \times \mathbb{R}^{+}$. However, for Enriques surface, $\Delta$ only parametrizes the cohomology classes of symplectic forms modulo the action since it's not known whether two cohomologous symplectic forms on Enriques surface are diffeomorphic or not.

\section*{3. Enriques surface as complex manifold}

In this section we will treat $S$ as a complex surface by equipping it with some complex structure $J$. A basic observation is that by the smooth invariance of Kodaira dimension (FQ94) we see that $S$ becomes a complex surface of Kodaira dimension 0 . Since it's also easy to see $S$ is not diffeomorphic to any other complex
surface with Kodaira dimension 0 in the list of Enriques-Kodaira classification, any complex structure will satisfy the conditions in Definition 2.1. Similar argument shows that any complex structure on the smooth manifold $\tilde{S}:=S \# \overline{\mathbb{C P}^{2}}$ comes from the complex blowup of some Enriques surface $(S, J)$. Since $p_{g}(S)=0$ implies the complex surface must be algebraic and $q(S)=0$ implies the Picard variety $\operatorname{Pic}_{0}(S)$ is trivial, we can naturally identify the Picard group $\operatorname{Pic}(S)$ with $H^{2}(S ; \mathbb{Z})$ by taking the first Chern class. The group of numerically equivalent divisor classes $\operatorname{Num}(S)$ is thus naturally identified with $H^{2}(S ; \mathbb{Z}) / \operatorname{Tor}=Q_{S}$.
3.1. Some standard facts and notations. We briefly review some standard facts about Enriques surface from [BHPVdV04, CDL24] and fix some notations.

Let $K$ be the canonical class which is the torsion element in $\operatorname{Pic}(S)=H^{2}(S ; \mathbb{Z})$. For any class $D \in H^{2}(S ; \mathbb{Z})$ we denote by $|D|$ its linear system when viewing $D$ as a divisor and by $h^{i}(D)$ the dimension of the cohomology groups $H^{i}\left(S, \mathcal{O}_{S}(D)\right)$ where $\mathcal{O}_{S}(D)$ is the associated line bundle on $S . D$ is called effective (or sometimes $J$ -effective if we want to address the complex structure $J$ ) if $h^{0}(D)=\operatorname{dim}|D|+1 \geq 1$ and nef (or $J$-nef) if it pairs non-negatively with any effective class. We say $D$ gives an elliptic pencil if $\operatorname{dim}|D|=1$ with no fixed component. This implies the existence of an $S^{2}$-family of genus zero $J$-holomorphic curves in class $D$ which covers $S$ and all but finitely many of them are smooth and connected tori. The basic tools from complex geometry are the Riemman-Roch formula and Serre duality
$$\begin{gathered}
h^{0}(D)-h^{1}(D)+h^{2}(D)=\frac{D(D-K)}{2}+\chi_{h}\left(\mathcal{O}_{S}\right)=\frac{D^{2}}{2}+1, \\
h^{i}(D)=h^{2-i}(K-D) \text { for } i=0,1,2,
\end{gathered}$$
from which we obtain the inequality
$$h^{0}(D)+h^{0}(K-D) \geq \frac{D^{2}}{2}+1$$
The following lemma can be found in [BHPVdV04, Section VIII.17] or [CDL24, Section 2.2]. We give a sketch of the proof.

Lemma 3.1. Let $D$ be a primitive class in $H^{2}(S ; \mathbb{Z})$ with $D^{2}=0$ and $J$ is an arbitrary complex structure on $S$. Then either $D$ or $-D$ is $J$-effective. If $D$ is both $J$-effective and $J$-nef, then either $D$ or $2 D$ gives an elliptic pencil. ${ }^{3}$

Proof. By (1), if $D$ is not effective then $K-D$ must be effective. Since $(S, J)$ is always algebraic, we have $-(K-D)=K+D$ can not be effective. Now apply (1) again to $-D$, we obtain that $-D$ is effective. Now suppose $D$ is both effective and nef. Since we also imposed the condition that $D$ is a primitive class, $D$ will be represented by a reduced by possibly reducible $J$-holomorphic curve which is an elliptic configuration (in the language of [BHPVdV04]) or indecomposable of canonical type (in the language of [CDL24]). This means the configuration is from the list of Kodaira's table in his classification of singular elliptic fibres. If $D$ doesn't give an elliptic pencil, then $h^{0}(D)=1$ and by Riemann-Roch formula, we have $h^{1}(D)=0$. The short exact sequence of sheaves
$$0 \rightarrow \mathcal{O}_{S}(D) \rightarrow \mathcal{O}_{S}(2 D) \rightarrow \mathcal{O}_{D}(2 D) \rightarrow 0$$

\footnotetext{
${ }^{3}$ Actually [CDL24] Proposition 2.2.8] shows that the primitive assumption can guarantee $|D|$ has dimension 0 and $|2 D|$ has dimension 1. But we don't need this result.
}
and its induced long exact sequence of cohomology shows that
$$h^{0}(2 D)=1+\operatorname{dim} H^{0}\left(D, \mathcal{O}_{D}(2 D)\right) .$$
Note that when $D$ is represented by a smooth elliptic curve, it's easy to see from adjunction formula that
$$\mathcal{O}_{D}(2 D) \cong \mathcal{O}_{D}(2 K+2 D) \cong \mathcal{O}_{D}(D+K)^{\otimes 2} \cong \omega_{D}^{\otimes 2} \cong \mathcal{O}_{D}^{\otimes 2} \cong \mathcal{O}_{D} .$$
Here $\omega_{D}$ denotes the dualizing sheaf on the curve $D$ which is trivial for a smooth elliptic curve. [BHPVdV04] or [CDL24] also shows that this is still the case when $D$ is only assumed to be an elliptic configuration of indecomposable of canonical type. And as a result, $\operatorname{dim} H^{0}\left(D, \mathcal{O}_{D}(2 D)\right)=1$ always holds true under our assumptions. So the linear system $|2 D|$ has dimension 1 and it doesn't contain fixed component since all the components must have self-intersection (-2). \(\square\)
3.2. Period domain and Torelli theorem. Now we review some knowledge about period domain of Enriques surface from [Hor78] and [Nam85]. Firstly note that when $S$ is given a complex structure $J$, the universal covering $\pi: T \rightarrow S$ and the involution $\iota: T \rightarrow T$ will become holomorphic once we equip $T$ with the complex structure $\pi^{*} J$. The complex surface $\left(T, \pi^{*} J\right)$ is then a K3 surface in the sense that it has trivial canonical line bundle and the irregularity $q=0$. The trivialization of the canonical line bundle offers a holomorphic 2-form $\Omega$ on $T$ which is unique up to a constant rescaling. Note that $\iota^{*} \Omega$ is still a holomorphic 2-form which must be either $\Omega$ or $-\Omega$ since $\iota^{*}$ has only $\pm 1$ as its eigenvalues. But the former case can never happen since that will imply the existence of a non-trivial holomorphic 2-form on the quotient surface $(S, J)$ contradicting the condition $p_{g}(S)=0$. As a result, if we view $Q_{T, \mathbb{C}}^{-}:=Q_{T}^{-} \otimes_{\mathbb{Z}} \mathbb{C}$ as a complex linear subspace of $H^{2}(T ; \mathbb{C})$, then the class $[\Omega]$ must belong to $Q_{T, \mathbb{C}}^{-}$. Moreover, since $\Omega$ is a $(2,0)$-form, it would satisfy $[\Omega] \cdot[\Omega]=0$ and $[\Omega] \cdot[\bar{\Omega}]>0$. Therefore, any complex structure $J$ on $S$ defines a point in the period domain
$$\mathcal{D}:=\left\{(v) \in \mathbb{P}\left(Q_{T, \mathbb{C}}^{-}\right) \mid(v, v)=0,(v, \bar{v})>0\right\} .$$
$\mathcal{D}$ is an open subset of a smooth complex projective variety of dimension 10, on which the isometry group $\Gamma:=O\left(Q_{T}^{-}\right)$naturally acts. However, not all the points in $\mathcal{D}$ can be realized as the period. Applying Riemman-Roch to the K3 surface, if $l \in H^{1,1}(T ; \mathbb{Z})$ is a (-2)-class, then either $l$ or $-l$ is effective. The condition $l \in H^{1,1}(T ; \mathbb{Z})$ is equivalent to $l \cdot[\Omega]=l \cdot[\bar{\Omega}]=0$. Also note that an effective class can never be $\iota$-anti-invariant. We then see that all the periods which can be realized must be contained in the following smaller subset of $\mathcal{D}$ removing countably many hyperplanes:
$$\mathcal{D}_{0}:=\left\{(v) \in \mathcal{D} \mid(l, v) \neq 0 \text { for all } l \in Q_{T}^{-} \text {with } l^{2}=-2\right\} .$$
The isometry group $\Gamma$ also acts this smaller subset. The significant achievement in algebraic geometry is the following Torelli theorem for Enriques surface, which is proved using Torelli theorem for K3 surface.

Theorem 3.2 (Hor78, Nam85). There is a bijection between the space of all complex structures on $S$ modulo the action by Diff $^{+}(S)$ with $\mathcal{D}_{0} / \Gamma$.

Remark 3.3. We just rephrase the statement in most literature of algebraic geometry using the terminology 'marked Enriques surface' by fixing the manifold $S$ and
modulo the diffeomorphism group action. The moduli space $\mathcal{D}_{0} / \Gamma$ can be given the structure of a connected quasiprojective variety of dimension 10.

By adjunction formula, an irreducible curve $D$ on Enriques surface must be a smooth rational (-2)-curve. If such a curve appears, then $p^{-1}(D)$ must be a disjoint union of two smooth rational (-2)-curves in $T$ since $\pi$ is unramified. Denote by $\alpha, \beta$ the classes of these two curves. They will satisfy $\iota^{*}(\alpha)=\beta,(\alpha, \beta)=0$. So $l:=\alpha-\beta$ will be a (-4)-class in $Q_{T}^{-}$and we call such a (-4)-class of even type (following [Nam85]). Note that for effective classes $\alpha$ and $\beta,[\Omega] \cdot \alpha=[\Omega] \cdot \beta=0$ and thus $[\Omega] \cdot l=0$. As a consequence, if we further zoom into a smaller subset of $\mathcal{D}_{0}$ removing countably hyperplanes determined by (-4)-classes:
$$\mathcal{D}_{g e n}:=\left\{(v) \in \mathcal{D}_{0} \mid(v, l) \neq 0, l \in Q_{T}^{-}, l^{2}=-4, \text { is of even type }\right\} .$$
We say a complex structure $J$ on $S$ is general if its period point belong to this $\mathcal{D}_{\text {gen }}$. So a general Enriques surface doesn't contain any smooth (-2)-curve.
$3.3 . \Phi$-invariant, Seshadri constant and algebraic capacity. The goal of this section is to show the relations among $\Phi$-invariant introduced by Cossec ([Cos85]), Seshadri constant introduced by Demailly ([Dem92]) and algebraic capacities introduced by Wormleighton ([Wor21, Wor22]), all of which can be naturally viewed as functions over the normalized fundamental chamber $\Delta$ introduced in Section 2. From these relations we will obtain the information about the Kähler cone of $\tilde{S}$.

Recall that any $\left(b_{1}, \cdots, b_{10}\right) \in \Delta$ satisfies
$$3=b_{1}+b_{2}+\cdots+b_{10}, 1 \geq b_{1}+b_{2}+b_{3}, b_{1} \geq b_{2} \geq \cdots \geq b_{10}>0$$
which gives rise to the class $\mathbf{b}:=l_{0}-\sum_{i=1}^{10} b_{i} l_{i} \in H^{2}(S ; \mathbb{R})$. The $\Phi$-invariant is defined for an Enriques surface $(S, J)$ and a big line bundle $L \in \operatorname{Pic}(S)$ :
$$\Phi_{J}(L):=\inf \left\{L \cdot F \mid F^{2}=0, F \text { is } J \text {-effective, } F \in \operatorname{Pic}(S)\right\} .$$
Since either $F$ or $-F$ is effective when $F^{2}=0$ (Lemma 3.1), one can immediately see the independence of the complex structure $J$. It can be defined over $\Delta$ by
$$\Phi\left(b_{1}, \cdots, b_{10}\right):=\inf \left\{|\mathbf{b} \cdot F| \mid F^{2}=0, F \in \operatorname{Num}(S)\right\} .$$

Proposition 3.4. $\Phi\left(b_{1}, \cdots, b_{10}\right)=b_{10}$.
Proof. We only need to show the class $s_{1}=3 l_{0}-l_{1}-\cdots-l_{9}$ of square 0 is the best minimizer for $\Phi$ over the polytope $\bar{\Delta}$. If $F=c l_{0}-\sum_{i=1}^{10} d_{i} l_{i} \in Q_{S}$ of square 0 is another class such that $|\mathbf{b} \cdot F|<\left|\mathbf{b} \cdot s_{1}\right|$, then since $\bar{\Delta}$ is the convex hull of its vertices $V_{1}, \cdots, V_{9}$, there must be some $V_{i}$ where the pairing with $F$ is smaller than $s_{1}$. We will show this can not happen case by case. Let $\mathbf{v}_{i}$ be the class in $H^{2}(S ; \mathbb{R})$ corresponding to $V_{i}$. Note that we have the conditions $c^{2}=\sum_{i=1}^{10} d_{i}^{2}$ and $3 c=\sum_{i=1}^{10} d_{i}$ and may further assume $c>0$ without loss of generality.
\begin{itemize}
\item[-] At $V_{1}$ : if $\mathbf{v}_{\mathbf{1}} \cdot F<\mathbf{v}_{1} \cdot s_{1}$, then
$$\frac{1}{7}\left(c-d_{1}\right)=c-\frac{1}{7}\left(3 d_{1}-2 \sum_{i=2}^{10} d_{i}\right)<\frac{2}{7}$$
and we must have $d_{1}=c-1$. By Cauchy-Schwarz inequality,
$$c^{2}-(c-1)^{2}=\sum_{i=2}^{10} d_{i}^{2} \geq \frac{1}{9}\left(\sum_{i=2}^{10} d_{i}\right)^{2}=\frac{1}{9}(3 c-(c-1))^{2} .$$
\end{itemize}

This will imply $c=1,2$ which are impossible by simple observation.
\begin{itemize}
\item[-] At $V_{2}$ : if $\mathbf{v}_{\mathbf{2}} \cdot F<\mathbf{v}_{2} \cdot s_{1}$, then
$$\frac{1}{14}\left(2 c-d_{1}-d_{2}\right)=c-\frac{1}{14}\left(5 d_{1}-5 d_{2}-4 \sum_{i=3}^{10} d_{i}\right)<\frac{4}{14}$$
and we must have $d_{1}+d_{2} \geq 2 c-3$ so that $d_{1}$ or $d_{2}$ is $\geq c-1$. Now by the previous case we know this can not happen.
\item[-] At $V_{k}$ for $3 \leq k \leq 9$ : from the pattern of $V_{k}$ we see that if $\mathbf{v}_{\mathbf{k}} \cdot F<\mathbf{v}_{k} \cdot s_{1}$, then
$$\frac{\sum_{i=k+1}^{10} d_{i}}{3(10-k)}=c-\frac{(10-k) \sum_{i=1}^{k} d_{i}+(9-k) \sum_{i=k+1}^{10} d_{i}}{3(10-k)}<\frac{9-k}{3(10-k)},$$
which would imply at least one of $d_{i}$ is negative. However, by Cauchy-Schwarz inequality it's impossible to have nine numbers whose sum is $\geq$ $3 c+1$ but the sum of square is $\leq c^{2}-1$. So these cases would not happen. \(\square\)
\end{itemize}

Now we introduce the algebraic capacities. The $k$-th algebraic capacity is defined for $(S, J)$ and a nef line bundle $L$
$$c_{k, J}^{\text {alg }}(L):=\inf \left\{L \cdot F \mid F^{2} \geq 2 k, F \text { is } J \text {-nef, } F \in \operatorname{Pic}(S)\right\} .$$
The actual definition for algebraic capacities has to replace $F^{2}$ term by $F^{2}-K \cdot F$, which is the (real) Gromov-Taubes dimension introduced in Section 4. Since we are dealing with Enriques surface, they are certainly equal. This notion has been generalized in [LN23] to the triple $(X, \omega, J)$ of a symplectic 4-manifold with a tamed almost complex structure. It's shown in [LN23] that when $X$ is a rational manifold, the capacities only depend on the cohomology class $[\omega]$ but not on the tamed almost complex structures. Now we proceed to prove a similar result for Enriques surface, but only for $k=0$ and complex structures.

Lemma 3.5. For any complex structure $J$ on $S$, there exists a self-diffeomorphism $f$ on $S$ such that the ample cone of $\left(S, f^{*} J\right)$ contains the interior of $\tilde{\Delta}$ (defined in the proof of Lemma 2.6).

Proof. By possibly composing the diffeomorphism inducing -Id on cohomology, we may assume the ample cone is contained in the forward cone $\mathcal{P}_{S}^{\prime}$. By Hum90, Section 5.13], an interior point of $\tilde{\Delta}$ has trivial stabilizer group under the action of $O^{\prime}\left(Q_{S}\right)$. So its pairing with any (-2)-class is non-zero otherwise the stabilizer group will contain the reflection along that (-2)-class. Since the ample cone is open and $\tilde{\Delta}$ is the fundamental domain, we could always compose some diffeomorphism such that the ample cone contains some point in the interior of $\tilde{\Delta}$, which pairs positively with all effective (-2)-classes. By connectedness of $\tilde{\Delta}$ we see that the entire interior of $\tilde{\Delta}$ must pair positively with all effective (-2)-classes. The result then follows from Nakai-Moishezon criterion. \(\square\)

By the above lemma, for any complex structure $J$ on $S$, there is another $J^{\prime}$ with the same period as $J$ such that the nef cone of $\left(S, J^{\prime}\right)$ contains the closure of $\tilde{\Delta}$. It thus makes sense to extend $c_{k, J^{\prime}}^{\text {alg }}$ as a function over $\Delta$ by substituting the integral class $L$ in the original definition with the real class b.

Proposition 3.6. If the ample cone of $(S, J)$ contains the interior of $\tilde{\Delta}$, then $\Phi=c_{0, J}^{\mathrm{alg}}$ as functions on $\Delta$.

Proof. We need to show the class $s_{1}=3 l_{0}-l_{1}-\cdots-l_{9}$ is also the best minimizer for $c_{0, J}^{\text {alg }}$ over the entire $\Delta$. By Proposition 3.4. this amounts to show that $s_{1}$ is $J$-nef and there is no better minimizer with positive square. For the first thing, just note that the class $s_{1}$ is actually in the closure of $\tilde{\Delta}$ ( $\frac{1}{3} s_{1}$ is the vertex $V_{9}$ ). Since the ample cone contains the interior of $\tilde{\Delta}$, the class $s_{1}$ must be $J$-nef. For the second thing, just go through the same argument as the proof of Proposition 3.4 with the only modification by replacing the equality $c^{2}=\sum_{i=1}^{10} d_{i}^{2}$ with the inequality $c^{2}>\sum_{i=1}^{10} d_{i}^{2}$. \(\square\)

Since a general complex structure doesn't allow any (-2)-curves, the following corollary is immediate.

Corollary 3.7. $\Phi=c_{0, J}^{\text {alg }}$ as functions on $\Delta$ for all general complex structures $J$.
Finally we introduce the Seshadri constant. For a nef line bundle $L$ over $(S, J)$ and a point $s \in S$, the Seshadri constant is defined to be
$$\varepsilon_{J, s}(L):=\inf \left\{\left.\frac{L \cdot C}{\nu(C, s)} \right\rvert\, C \text { is an irreducible curve passing through } s\right\}$$
where $\nu(C, s)$ is the multiplicity of $C$ at $s$. Again, if the ample cone of $(S, J)$ contains the interior of $\tilde{\Delta}$, then $\varepsilon_{J, s}$ can be viewed as a function on $\Delta$ by pairing with any real class $\mathbf{b}$ in the definition. Observe that since $p_{g}(S)=0$, by Nakai-Moishezon criterion, Corollary 2.5 and Lemma 3.5, if we define $\mathcal{K}: \Delta \rightarrow \mathbb{R}^{+}$by
$$\mathcal{K}\left(b_{1}, \cdots, b_{10}\right):=\sup \{t \mid \mathbf{b}-t e \text { can be represented by a Kähler form on } \tilde{S}\},$$
then the relation between $\varepsilon_{J, s}$ and $\mathcal{K}$ is given by
$$\mathcal{K}\left(b_{1}, \cdots, b_{10}\right)=\sup \left\{\varepsilon_{J, s}(\mathbf{b}) \mid J \text { 's ample cone contains } \operatorname{Int}(\tilde{\Delta}), s \in S\right\} .$$

Proposition 3.8. $\mathcal{K} \leq 2 \Phi$ as functions over $\Delta$.
Proof. Lemma 3.1 tells us if $F^{2}=0$ and $F$ is both $J$-effective and $J$-nef, then there is a $J$-holomorphic curve in class $2 F$ passing through any point on $S$. Consequently, from the definition we have
$$\sup \left\{\varepsilon_{J, s}(\mathbf{b}) \mid s \in S\right\} \leq 2 c_{0, J}^{\mathrm{alg}}(\mathbf{b})$$
for all complex structures $J$ whose ample cone contains the interior of $\tilde{\Delta}$. Now applying Proposition 3.6 and taking the supremum over all such complex structures $J$ for the above inequality, we obtain that $\mathcal{K} \leq 2 \Phi$. \(\square\)

\section*{4. Enriques surface as symplectic manifold}

In this section will treat $S$ and $\tilde{S}$ as symplectic 4-manifolds by equipping then with any symplectic form $\omega$ and $\tilde{\omega}$ compatible with the orientation. A basic fact from [LL01, Theorem 1] we should keep in mind is the uniqueness of the first Chern class. That is, $c_{1}(S, \omega)$ must be the torsion element in $H^{2}(S ; \mathbb{Z})$ and $c_{1}(\tilde{S}, \tilde{\omega})$ must be $c_{1}(S, \omega) \pm e$ where the sign in front of $e$ depends on the sign of $\tilde{\omega}(e)$. We always assume the cohomology class $[\omega]$ or $[\tilde{\omega}]$ lies in the connected component $\mathcal{P}_{S}^{\prime}$ or $\mathcal{P}_{\tilde{S}}^{\prime}$. Such a choice will make the invariants introduced in the sequel unambiguous.
4.1. Gromov-Taubes and Seiberg-Witten invariants. For a closed symplectic 4-manifold $(X, \omega)$ with $b_{2}^{+}=1$, we can consider its Gromov-Taubes invariant introduced in [Tau96]. It is a function
$$G r_{\omega}: H^{2}(X ; \mathbb{Z}) \rightarrow \mathbb{Z}$$
which is defined to be 0 whenever $B \in H^{2}(X ; \mathbb{Z})$ has negative complex Gromov-Taubes dimension
$$d(B):=\frac{1}{2}\left(B^{2}+c_{1}(X, \omega) \cdot B\right) ;$$
is defined to be a sophisticated count of embedded, but may be non-connected and with multiplicities, pseudoholomorphic submanifolds passing through $d(B)$ points whose homology class is Poincaré dual to $B$ for a generic choice of $\omega$-tame almost complex structure $J$ and $d(B)$ points on $S$ when $d(B) \geq 0$ and $B \neq 0$; and is defined to be 1 if $B=0$. Note that [McD97, Theorem 1.2] shows that when the almost complex structure is generic, all the components with negative self-intersection must be exceptional spheres. Therefore the non-vanishing of the invariant for a non-zero class $B$ will then imply the existence of an embedded symplectic surface representing the class $B$ with no components having self-intersection $\leq-2$. When $(X, \omega)$ is not minimal, let $\mathcal{E}_{\omega}$ be the set of classes represented by embedded symplectic exceptional spheres. To circumvent the subtlety of multiply-covered exceptional spheres, [McD97] proposed a modified version of this invariant
$$G r_{\omega}^{\prime}: H^{2}(X ; \mathbb{Z}) \rightarrow \mathbb{Z}$$
by assigning $G r_{\omega}^{\prime}(B)$ to $G r_{\omega}\left(B^{\prime}\right)$ where
$$B^{\prime}:=B+\sum_{E \in \mathcal{E}_{\omega}, E \cdot B<-1}(E \cdot B) E .$$

On the other hand, Seiberg-Witten theory (see [Sal] or [Nic00]) gives two functions
$$S W_{\omega, \pm}: H^{2}(X ; \mathbb{Z}) \rightarrow \mathbb{Z}$$
which are defined as follows. We first need a Riemannian metric $g$ and a spin ${ }^{c}$ structure which gives the spinor bundles $W^{ \pm}$with $\operatorname{det}\left(W^{+}\right)=\operatorname{det}\left(W^{-}\right)=\mathcal{L}$. By our choice of $\omega$, there is a bijection between spin ${ }^{c}$ structures and $H^{2}(X ; \mathbb{Z})$ by associating $\mathcal{L}$ to $B:=\frac{1}{2}\left(c_{1}(\mathcal{L})-c_{1}(X, \omega)\right)$. Then for a self-dual 2-form $\eta$, the Seiberg-Witten equations are for a pair $(A, \phi)$ consisting of a connection $A$ of $\mathcal{L}$ and a section $\phi$ of $W^{+}$which are given by
$$\left\{\begin{array}{l}
D_{A} \phi=0 \\
F_{A}^{+}=i q(\phi)+i \eta
\end{array}\right.$$
where $D_{A}$ is the Dirac operator, $F_{A}^{+}$is the self-dual component of the curvature $F_{A}$ and $q: \Gamma\left(W^{+}\right) \rightarrow \Omega_{+}^{2}(X)$ is a canonical map. When the choice of $(g, \eta)$ is generic, the quotient of the space of solutions by $C^{\infty}\left(X ; S^{1}\right)$ is a compact manifold $\mathcal{M}_{X}(\mathcal{L}, g, \eta)$ of real dimension $2 d(B)$. There is a principal $S^{1}$-bundle $\mathcal{M}_{X}^{0}(\mathcal{L}, g, \eta)$ over $\mathcal{M}_{X}(\mathcal{L}, g, \eta)$ if we take the quotient by only elements in $C^{\infty}\left(X ; S^{1}\right)$ mapping a base point of $X$ to $1 \in S^{1}$. Now we can get a number by pairing the maximal cup product of the fundamental class of $\mathcal{M}_{X}(\mathcal{L}, g, \eta)$ with the Euler class of the principal $S^{1}$-bundle. If $b_{2}^{+}(X)=1$, the number defined above depends on the chamber where the pair $(g, \eta)$ lives. More precisely, let $\omega_{g}$ denote the $g$-harmonic self-dual 2-form whose cohomology class lies in the same component as $[\omega]$ in the
positive cone. Then whether this number is the value for $S W_{\omega,+}(B)$ or $S W_{\omega,-}(B)$ is determined by the sign of the discriminant
$$\Delta_{\mathcal{L}}(g, \eta):=\int_{X}\left(2 \pi c_{1}(\mathcal{L})+\eta\right) \wedge \omega_{g} .$$

The following results are the key properties of these invariants we will apply.
Theorem 4.1 (see [LL95, LL99]). Let $(X, \omega)$ be a closed symplectic 4-manifold with $b_{2}^{+}(X)=1$ and $B \in H^{2}(X ; \mathbb{Z})$, then
\begin{itemize}
\item[-] (Symmetry lemma) $\left|S W_{\omega,+}(B)\right|=\left|S W_{\omega,-}\left(-c_{1}(X, \omega)-B\right)\right|$.
\item[-] (Wall crossing formula) $\left|S W_{\omega,+}(B)-S W_{\omega,-}(B)\right|=1$.
\item[-] $\left(S W=G r\right.$ for $\left.b_{2}^{+}=1\right) G r_{\omega}^{\prime}(B)=S W_{\omega,-}(B)$ when the set $\left\{E \in \mathcal{E}_{\omega} \mid E \cdot B<\right.$ -1\} is finite.
\item[-] (Blowup formula) Let $(\tilde{X}, \tilde{\omega})$ be the symplectic blowup of $(X, \omega)$ with exceptional class $e$, then $S W_{\tilde{\omega},-}(B+l e)=S W_{\omega,-}(B)$ when $d(B+l e) \geq 0$.
\end{itemize}

Note that for manifolds with non-negative Kodaira dimension, by [Li99, Corollary 3] the set $\left\{E \in \mathcal{E}_{\omega} \mid E \cdot B<-1\right\}$ is always finite. For rational manifolds $\mathbb{C P}^{2} \# n \overline{\mathbb{C P}^{2}}$, the subtlety around the infinity of this set was further investigated in [LN23]. Now we determine all the classes with non-trivial invariants for Enriques surface $S$ and its one-point blowup $\tilde{S}$.
Proposition 4.2. Let $S$ and $\tilde{S}$ be equipped with the symplectic forms $\omega$ and $\tilde{\omega}$ whose cohomology classes live in $\mathcal{P}_{S}^{\prime}$ and $\mathcal{P}_{\tilde{S}}^{\prime}$ respectively. Let $B \in H^{2}(S ; \mathbb{Z})$ and $\tilde{B}=B+l e \in H^{2}(S ; \mathbb{Z}) \oplus \mathbb{Z} e=H^{2}(\tilde{S} ; \mathbb{Z})$. Denote by $B_{f}$ the torsion-free part of $B$. Assume further that $\tilde{\omega} \cdot e>0$. Then
\begin{itemize}
\item[-] $G r_{\omega}(B) \neq 0 \Longleftrightarrow G r_{\omega}^{\prime}(B) \neq 0 \Longleftrightarrow S W_{\omega,-}(B) \neq 0 \Longleftrightarrow B_{f} \in \overline{\mathcal{P}_{S}^{\prime}}$,
\item[-] $G r_{\tilde{\omega}}(\tilde{B}) \neq 0 \Longleftrightarrow B^{2} \geq l^{2}-l, l \leq 1$ and $B_{f} \in \overline{\mathcal{P}_{S}^{\prime}}$,
\item[-] $G r_{\tilde{\omega}}^{\prime}(\tilde{B}) \neq 0 \Longleftrightarrow S W_{\tilde{\omega},-}(\tilde{B}) \neq 0 \Longleftrightarrow B_{f} \in \overline{\mathcal{P}_{S}^{\prime}}$ and either $B^{2} \geq$ $l^{2}-l$ or $l \geq 2$.
\end{itemize}
Proof. For the first item, the minimality of $S$ and $\mathrm{SW}=\mathrm{Gr}$ in Theorem 4.1 give the first two equivalence. Also note that a class $B$ with non-trivial invariants must have non-negative $d(B)=\frac{1}{2}\left(B^{2}+c_{1}(S, \omega) \cdot B\right)=\frac{1}{2} B^{2}$ and $\omega \cdot B>0$ since $B$ can be represented by embedded symplectic surfaces, which implies $B_{f} \in \overline{\mathcal{P}_{S}^{\prime}}$ by the assumption that $[\omega] \in \mathcal{P}_{S}^{\prime}$. On the other hand, if $B_{f} \in \overline{\mathcal{P}_{S}^{\prime}}$, then $\omega \cdot\left(-c_{1}(S, \omega)-B\right)<$ 0 which implies $G r_{\omega}\left(-c_{1}(S, \omega)-B\right)=0$. Now by symmetry lemma and wall crossing formula in Theorem 4.1, $S W_{\omega,-}(B) \neq 0$. This shows the third equivalence.
For the second item, note that the condition $\tilde{\omega} \cdot e>0$ guarantees $c_{1}(\tilde{S}, \tilde{\omega})=$ $c_{1}(S, \omega)-e$. Assuming $G r_{\tilde{\omega}}(\tilde{B}) \neq 0$, then we firstly have $0 \leq d(\tilde{B})=B^{2}-l^{2}+l$. If $l \geq 2$, then by positivity of intersection and $\operatorname{Gr}_{\omega^{\prime}}(e) \neq 0$ (can be seen from the blowup formula), any embedded pseudoholomorphic representative of the class $B$ must have a component of the exceptional class $e$ with multiplicity $\geq 2$, which doesn't appear for generic almost complex structures. This shows $l \leq 1$ and further implies $\left\{E \in \mathcal{E}_{\tilde{\omega}} \mid E \cdot \tilde{B}<-1\right\}$ is empty. So $0 \neq G r_{\tilde{\omega}}(\tilde{B})=G r_{\tilde{\omega}}^{\prime}(\tilde{B})=S W_{\tilde{\omega},-}(\tilde{B})=$ $S W_{\omega,-}(B)$ by Theorem 4.1. The first item then implies $B_{f} \in \overline{\mathcal{P}_{S}^{\prime}}$. The another direction also easily follows from the similar argument.
For the third item, just note that $\operatorname{Gr}_{\tilde{\omega}}^{\prime}(\tilde{B})=\operatorname{Gr}_{\tilde{\omega}}(\tilde{B}-l e)$ when $l \geq 2$ by the definition of $G r^{\prime}$ and apply the first and the second item. \(\square\)

The following corollary immediately follows from the definition of Gromov-Taubes invariant.

Corollary 4.3. Under the same assumption of Proposition 4.2, any class $\tilde{B}=$ $B+l e \in H^{2}(S ; \mathbb{Z}) \oplus \mathbb{Z} e=H^{2}(\tilde{S} ; \mathbb{Z})$ satisfying $B^{2} \geq l^{2}-l, l \leq 0$ and $B_{f} \in \overline{\mathcal{P}_{S}^{\prime}}$ can be represented by a connected embedded $\tilde{\omega}$-symplectic surface in $(\tilde{S}, \tilde{\omega})$.

Proof. From Proposition 4.2 we know $G r_{\tilde{\omega}}(\tilde{B}) \neq 0$ so that $\tilde{B}$ can be represented by embedded symplectic surface whose components with negative self-intersection are exceptional spheres. But the condition $l \leq 0$ doesn't allow the appearance of exceptional spheres by positivity of intersection. So all the components must have non-negative self-intersection, which implies the number of components must be one since $b_{2}^{+}(\tilde{S})=1$. \(\square\)
4.2. Symplectic cone of $\tilde{S}$. In [LL01], the symplectic cone has been determined for all smooth 4-manifolds which admit symplectic structures and have $b_{2}^{+}=1$. Here we recall its proof, specializing on the manifold $\tilde{S}$. The main ingredient for constructing symplectic forms is the inflation procedure of adding suitable Thom forms near a symplectic submanifold with positive self-intersection.

Lemma 4.4 (McD98 ). Let $(X, \omega)$ be a symplectic 4-manifold and $B \in H^{2}(X ; \mathbb{Z})$. Assume $B^{2}>0$ and $B$ can be represented by a connected embedded $\omega$-symplectic surface. Denote by $B_{f}$ the torsion free part of $B$. Then for all $t>0$, the cohomology class $[\omega]+t B_{f}$ can be realized by a symplectic form.

Combined with the calculation of the classes with non-trivial invariants from the previous section, we then have the following.

Proposition 4.5. Any cohomology class $a \in \mathcal{P}_{\tilde{S}}^{\prime}$ with $a \cdot e \neq 0$ can be realized by a symplectic form on $\tilde{S}$.

Proof. By rescaling and density of rational classes, without loss of generality we may assume $a$ is an integral class since the symplectic cone is open. Also, since there is the diffeomorphism coming from the reflection along the exceptional sphere in class $e$, we may further assume $a \cdot e>0$. Now pick an arbitrary integral symplectic form $\tilde{\omega}$ whose cohomology class belongs to $\mathcal{P}_{\tilde{S}}^{\prime}$. Then for sufficiently large positive integer $P$, the class $P a-[\tilde{\omega}]$ will have positive square and satisfy the conditions in Corollary 4.3. Thus it will be represented by a connected embedded $\tilde{\omega}$-symplectic surface and Lemma 4.4 can be applied to produce the symplectic form realizing the class $[\tilde{\omega}]+P a-[\tilde{\omega}]=P a$. By rescaling $a$ can be realized as well. \(\square\)

For the convenience of stating our comparison theorem later, we introduce the function $\mathcal{S}: \Delta \rightarrow \mathbb{R}^{+}$defined on the fundamental chamber by
$$\left(b_{1}, \cdots, b_{10}\right) \mapsto \sup \left\{t \mid l_{0}-\sum_{i=1}^{10} b_{i} l_{i}-t e \text { can be realized by a symplectic form }\right\} .$$

Corollary 4.6. $\mathcal{S}\left(b_{1}, \cdots, b_{10}\right)=\left(1-\sum_{i=1}^{10} b_{i}^{2}\right)^{\frac{1}{2}}$.
Remark 4.7. Corollary 4.6 has been essentially known in [LL01]. It's interesting to see if there is another proof without the heavy machinery of Taubes-Seiberg-Witten theory by directly showing the unobstructedness of ball packings, possibly using the techniques of almost toric fibrations of [LS10].

\section*{5. Proof of the main theorems}

Proof of Theorem 1.5. By Proposition 3.6 and Proposition 3.8. \(\square\)

Proof of Theorem 1.1. By Theorem 1.5, Corollary 2.5, Proposition 3.4 and Corollary 4.6, we only need to check there exists $\left(b_{1}, \cdots, b_{10}\right) \in \Delta$ such that $\mathcal{S}\left(b_{1}, \cdots, b_{10}\right)>$ $\mathcal{K}\left(b_{1}, \cdots, b_{10}\right)$. This is equivalent to
$$\left(1-\sum_{i=1}^{10} b_{i}^{2}\right)^{\frac{1}{2}}>2 b_{10} .$$
For example we can take
$$\left(b_{1}, \cdots, b_{10}\right)=\left(\frac{1}{3}, \frac{1}{3}, \frac{1}{3}, \frac{1}{3}, \frac{1}{3}, \frac{1}{3}, \frac{1}{3}, \frac{1}{3}, \frac{1}{4}, \frac{1}{12}\right) .$$
See also Figure 1. \(\square\)

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/4c88ca62-a5be-4ea0-bcbd-9a1e0f9476c8-18.jpg?height=845&width=1098&top_left_y=1169&top_left_x=526}
\captionsetup{labelformat=empty}
\caption{Figure 1. This is a picture for the normalized fundamental chamber $\Delta$ with 9 vertices $V_{1}, \cdots . V_{9}$. The region enclosed by the dashed ellipse satisfies $\mathcal{K}<\mathcal{S}$, from which one can see the difference between Kähler cone and symplectic cone.}
\end{figure}

Remark 5.1. The recent result by [GK22, Theorem 1.3] verifies that for a very general Enriques surface ( $S, J$ ), one has $\Phi=\inf _{s \in S} \varepsilon_{J, s}$. In our terminology, this means $\mathcal{K} \geq \Phi$ holds true. Therefore $\mathcal{K}$ is a function between $\Phi$ and $2 \Phi$.

\section*{References}
\begin{itemize}
\item[] [AGK09] Miguel Abreu, Gustavo Granja, and Nitu Kitchloo, Compatible complex structures on symplectic rational ruled surfaces, Duke Math. J. 148 (2009), no. 3, 539-600. MR 2527325
\item[] [Bal05] Scott Baldridge, New symplectic 4-manifolds with $b_{+}=1$, Math. Ann. 333 (2005), no. 3, 633-643. MR 2198801
\item[] [BHPVdV04] Wolf P. Barth, Klaus Hulek, Chris A. M. Peters, and Antonius Van de Ven, Compact complex surfaces, second ed., Ergebnisse der Mathematik und ihrer Grenzgebiete. 3. Folge. A Series of Modern Surveys in Mathematics, vol. 4, Springer-Verlag, Berlin, 2004. MR 2030225
\item[] [Bir99] Paul Biran, Constructing new ample divisors out of old ones, Duke Math. J. 98 (1999), no. 1, 113-135. MR 1687571
\item[] [BL05] Scott Baldridge and Tian-Jun Li, Geography of symplectic 4-manifolds with Kodaira dimension one, Algebr. Geom. Topol. 5 (2005), 355-368. MR 2135557
\item[] [Bru96] Rogier Brussee, The canonical class and the $C^{\infty}$ properties of Kähler surfaces, New York J. Math. 2 (1996), 103-146. MR 1423304
\item[] [Buc99] Nicholas Buchdahl, On compact Kähler surfaces, Ann. Inst. Fourier (Grenoble) 49 (1999), no. 1, vii, xi, 287-302. MR 1688136
\item[] [CDL24] François Cossec, Igor Dolgachev, and Christian Liedtke, Enriques surfaces. I, https://dept.math.lsa.umich.edu/ idolga/EnriquesOne.pdf, 2024.
\item[] [Cho16] Yunhyung Cho, Hard Lefschetz property of symplectic structures on compact Kähler manifolds, Trans. Amer. Math. Soc. 368 (2016), no. 11, 8223-8248. MR 3546798
\item[] [Cos85] François R. Cossec, On the Picard group of Enriques surfaces, Math. Ann. 271 (1985), no. 4, 577-600. MR 790116
\item[] [CP12] Paolo Cascini and Dmitri Panov, Symplectic generic complex structures on fourmanifolds with $b_{+}=1$, J. Symplectic Geom. 10 (2012), no. 4, 493-502. MR 2982020
\item[] [Dem92] Jean-Pierre Demailly, Singular Hermitian metrics on positive line bundles, Complex algebraic varieties (Bayreuth, 1990), Lecture Notes in Math., vol. 1507, Springer, Berlin, 1992, pp. 87-104. MR 1178721
\item[] [Dol16] Igor V. Dolgachev, A brief introduction to Enriques surfaces, Development of moduli theory-Kyoto 2013, Adv. Stud. Pure Math., vol. 69, Math. Soc. Japan, [Tokyo], 2016, pp. 1-32. MR 3586505
\item[] [Don06] S. K. Donaldson, Two-forms on four-manifolds and elliptic equations, Inspired by S. S. Chern, Nankai Tracts Math., vol. 11, World Sci. Publ., Hackensack, NJ, 2006, pp. 153-172. MR 2313334
\item[] [Dor15] Josef G. Dorfmeister, Kodaira dimension of fiber sums along spheres, Geom. Dedicata 177 (2015), 1-25. MR 3370019
\item[] [Dra99] Tedi Draghici, The Kähler cone versus the symplectic cone, Bull. Math. Soc. Sci. Math. Roumanie (N.S.) 42(90) (1999), no. 1, 41-49. MR 1880654
\item[] [EV16] Michael Entov and Misha Verbitsky, Unobstructed symplectic packing for tori and hyper-Kähler manifolds, J. Topol. Anal. 8 (2016), no. 4, 589-626. MR 3545014
\item[] [FG90] Marisa Fernández and Alfred Gray, Compact symplectic solvmanifolds not admitting complex structures, Geom. Dedicata 34 (1990), no. 3, 295-299. MR 1066580
\item[] [FM88] Robert Friedman and John W. Morgan, On the diffeomorphism types of certain algebraic surfaces. I, J. Differential Geom. 27 (1988), no. 2, 297-369. MR 925124
\item[] [FM94] , Smooth four-manifolds and complex surfaces, Ergebnisse der Mathematik und ihrer Grenzgebiete (3) [Results in Mathematics and Related Areas (3)], vol. 27, Springer-Verlag, Berlin, 1994. MR 1288304
\item[] [FM97] -, Algebraic surfaces and Seiberg-Witten invariants, J. Algebraic Geom. 6 (1997), no. 3, 445-479. MR 1487223
\item[] [FQ94] Robert Friedman and Zhenbo Qin, The smooth invariance of the Kodaira dimension of a complex surface, Math. Res. Lett. 1 (1994), no. 3, 369-376. MR 1302651
\item[] [FS95] Ronald Fintushel and Ronald J. Stern, Immersed spheres in 4-manifolds and the immersed Thom conjecture, Turkish J. Math. 19 (1995), no. 2, 145-157. MR 1349567
\item[] [Gei92] Hansjörg Geiges, Symplectic structures on $T^{2}$-bundles over $T^{2}$, Duke Math. J. 67 (1992), no. 3, 539-555. MR 1181312
\end{itemize}
\begin{itemize}
\item[] [GK22] Concettina Galati and Andreas Leopold Knutsen, Rational curves and seshadri constants on enriques surfaces, Preprint arXiv:2212.08191 (2022).
\item[] [GM93] Robert E. Gompf and Tomasz S. Mrowka, Irreducible 4-manifolds need not be complex, Ann. of Math. (2) 138 (1993), no. 1, 61-111. MR 1230927
\item[] [Gom95] Robert E. Gompf, A new construction of symplectic manifolds, Ann. of Math. (2) 142 (1995), no. 3, 527-595. MR 1356781
\item[] [GS99] Robert E. Gompf and András I. Stipsicz, 4-manifolds and Kirby calculus, Graduate Studies in Mathematics, vol. 20, American Mathematical Society, Providence, RI, 1999. MR 1707327
\item[] [Ham14] M. J. D. Hamilton, The closure of the symplectic cone of elliptic surfaces, J. Symplectic Geom. 12 (2014), no. 2, 365-377. MR 3210580
\item[] [Hor78] Eiji Horikawa, On the periods of Enriques surfaces. I, Math. Ann. 234 (1978), no. 1, 73-88. MR 491725
\item[] [Hum90] James E. Humphreys, Reflection groups and Coxeter groups, Cambridge Studies in Advanced Mathematics, vol. 29, Cambridge University Press, Cambridge, 1990. MR 1066460
\item[] [JR87] F. E. A. Johnson and E. G. Rees, On the fundamental group of a complex algebraic manifold, Bull. London Math. Soc. 19 (1987), no. 5, 463-466. MR 898726
\item[] [KK17] Yael Karshon and Liat Kessler, Distinguishing symplectic blowups of the complex projective plane, J. Symplectic Geom. 15 (2017), no. 4, 1089-1128. MR 3734610
\item[] [Kot97] D. Kotschick, Orientations and geometrisations of compact complex surfaces, Bull. London Math. Soc. 29 (1997), no. 2, 145-149. MR 1425990
\item[] [L9̈8] Michael Lönne, On the diffeomorphism groups of elliptic surfaces, Math. Ann. 310 (1998), no. 1, 103-117. MR 1600035
\item[] [Lam99] A. Lamari, Le cône kählérien d'une surface, J. Math. Pures Appl. (9) 78 (1999), no. 3, 249-263. MR 1687094
\item[] [Li99] Tian-Jun Li, Smoothly embedded spheres in symplectic 4-manifolds, Proc. Amer. Math. Soc. 127 (1999), no. 2, 609-613. MR 1459135
\item[] [Li08] \_\_\_\_, The space of symplectic structures on closed 4-manifolds, Third International Congress of Chinese Mathematicians. Part 1, 2, AMS/IP Stud. Adv. Math., vol. 42, pt. 1, 2, Amer. Math. Soc., Providence, RI, 2008, pp. 259-277. MR 2409637
\item[] [LL95] T. J. Li and A. Liu, General wall crossing formula, Math. Res. Lett. 2 (1995), no. 6, 797-810.
\item[] [LL99] Tian-Jun Li and Ai-Ko Liu, The equivalence between SW and Gr in the case where $b^{+}=1$, Internat. Math. Res. Notices (1999), no. 7, 335-345. MR 1683312
\item[] [LL01] \_\_\_\_, Uniqueness of symplectic canonical class, surface cone and symplectic cone of 4-manifolds with $B^{+}=1$, J. Differential Geom. 58 (2001), no. 2, 331-370. MR 1913946
\item[] [LLW22] Jun Li, Tian-Jun Li, and Weiwei Wu, Symplectic torelli groups of rational surfaces, arXiv preprint arXiv:2212.01873 (2022).
\item[] [LMS13] Janko Latschev, Dusa McDuff, and Felix Schlenk, The Gromov width of 4-dimensional tori, Geom. Topol. 17 (2013), no. 5, 2813-2853. MR 3190299
\item[] [LN23] Tian-Jun Li and Shengzhen Ning, Algebraic capacity as tropical polynomial over $c_{1}$-nef symplectic cone, Preprint arXiv:2303.12607 (2023).
\item[] [LS10] Naichung Conan Leung and Margaret Symington, Almost toric symplectic fourmanifolds, J. Symplectic Geom. 8 (2010), no. 2, 143-187. MR 2670163
\item[] [LU06] Tian-Jun Li and Michael Usher, Symplectic forms and surfaces of negative square, J. Symplectic Geom. 4 (2006), no. 1, 71-91. MR 2240213
\item[] [McD84] Dusa McDuff, Examples of simply-connected symplectic non-Kählerian manifolds, J. Differential Geom. 20 (1984), no. 1, 267-277. MR 772133
\item[] [McD97] \_\_\_\_, Lectures on Gromov invariants for symplectic 4-manifolds, Gauge theory and symplectic geometry (Montreal, PQ, 1995), NATO Adv. Sci. Inst. Ser. C: Math. Phys. Sci., vol. 488, Kluwer Acad. Publ., Dordrecht, 1997, With notes by Wladyslav Lorek, pp. 175-210. MR 1461573
\item[] [McD98] \_\_\_\_, From symplectic deformation to isotopy, Topics in symplectic 4-manifolds (Irvine, CA, 1996), First Int. Press Lect. Ser., vol. I, Int. Press, Cambridge, MA, 1998, pp. 85-99. MR 1635697
\end{itemize}
[Nam85] Yukihiko Namikawa, Periods of Enriques surfaces, Math. Ann. 270 (1985), no. 2, 201-222. MR 771979
[Nic00] Liviu I. Nicolaescu, Notes on Seiberg-Witten theory, Graduate Studies in Mathematics, vol. 28, American Mathematical Society, Providence, RI, 2000. MR 1787219
[Oko88] Christian Okonek, Fake Enriques surfaces, Topology 27 (1988), no. 4, 415-427. MR 976584
[Par04] Jongil Park, Non-complex symplectic 4-manifolds with $b_{2}^{+}=1$, Bull. London Math. Soc. 36 (2004), no. 2, 231-240. MR 2026418
[Sal] Dietmar Salamon, Spin geometry and Seiberg-Witten invariants.
[Tau95] Clifford Henry Taubes, More constraints on symplectic forms from Seiberg-Witten invariants, Math. Res. Lett. 2 (1995), no. 1, 9-13. MR 1312973
[Tau96] , Counting pseudo-holomorphic submanifolds in dimension 4, J. Differential Geom. 44 (1996), no. 4, 818-893. MR 1438194
[Thu76] W. P. Thurston, Some simple examples of symplectic manifolds, Proc. Amer. Math. Soc. 55 (1976), no. 2, 467-468. MR 402764
[TO97] Aleksy Tralle and John Oprea, Symplectic manifolds with no Kähler structure, Lecture Notes in Mathematics, vol. 1661, Springer-Verlag, Berlin, 1997. MR 1465676
[Ush09] Michael Usher, Kodaira dimension and symplectic sums, Comment. Math. Helv. 84 (2009), no. 1, 57-85. MR 2466075
[Wor21] Ben Wormleighton, ECH capacities, Ehrhart theory, and toric varieties, J. Symplectic Geom. 19 (2021), no. 2, 475-506. MR 4325410
[Wor22] B. Wormleighton, Algebraic capacities, Selecta Math. (N.S.) 28 (2022), no. 1, Paper No. 9, 45. MR 4344145

School of Mathematics, University of Minnesota, Minneapolis, MN, US
E-mail address: ning0040@umn.edu