---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Irregular cusps of ball quotients]

---
source_file: 2108_10253.pdf
converter: mathpix
format: mmd
---

\title{
IRREGULAR CUSPS OF BALL QUOTIENTS
}

\author{
YOTA MAEDA
}

\begin{abstract}
We study the branch divisors on the boundary of the canonical toroidal compactification of ball quotients. We show a criterion, the low slope cusp form trick, for proving that ball quotients are of general type. Moreover, we classify when irregular cusps exist in the case of the discriminant kernel and construct concrete examples for some arithmetic subgroups. As another direction of study, when a complex ball is embedded into a Hermitian symmetric domain of type IV, we determine when regular or irregular cusps map to regular or irregular cusps studied by Ma.
\end{abstract}

\section*{1. Introduction}

When calculating the order of modular forms on modular curves at cusps, we need to consider whether the cusp is regular or not. If it is irregular, then the order of the modular forms is defined as half the order determined by its Fourier expansion at the cusp. More precisely, irregular cusps of modular curves are cusps whose width are strictly smaller than the period for Fourier expansion; this is explained in detail in [4]. In the case of orthogonal modular varieties, Ma [16] defined and studied irregular cusps. He classified the structures of discriminant groups for the case of discriminant kernel when irregular cusps may exist on the orthogonal modular varieties and constructed examples. Finally, he proved the low slope cusp form trick, which is a modification of the low weight cusp form trick [8, Theorem 1.1] when the irregular cusps arise, and used it to show that some orthogonal modular varieties are of general type.

In this paper, we work on ball quotients. First, we define irregular cusps on them. Unlike the case of orthogonal modular varieties, in our situation, there may exist branch divisors with branch index 2,3,4 or 6 as explained in section 3. Considering the effects of these cusps, as a main result, we give a sufficient condition for a ball quotient to be of general type in terms of modular forms, called the low slope cusp form trick. On the other hand, we shall give an example of a ball quotient of non-negative Kodaira dimension in section [7] This is done by constructing a cusp form, satisfying a weaker condition appearing in this trick. Second, we consider the relationship between regular/irregular cusps on ball quotients and regular/irregular cusps on orthogonal modular varieties when a Hermitian symmetric domain of type I is embedded into one of type IV. In this situation, we prove that regular cusps map to regular cusps and determine whether irregular cusps map to regular or irregular cusps. Third, we classify the structures of the discriminant group when the discriminant kernel may have irregular cusps in section 4 and Appendix A. Finally, we construct concrete examples of irregular cusps of any index for any imaginary quadratic field with class number 1 in section 8.

Before stating our results, we should summarize our settings. Let $F$ be an imaginary quadratic field and $\mathscr{O}_{F}$ be its ring of integers. Let ( $L,\langle$,$\rangle ) be a Hermitian lattice of signature (1, n)$ over $\mathscr{O}_{F}$ with $n>1$ and $\mathrm{U}(L)$ be the associated unitary group scheme over $\mathbb{Z}$. Then, the Hermitian symmetric domain associated with the unitary group $\mathrm{U}(L)(\mathbb{R}) \cong \mathrm{U}(1, n)$ is defined as
$$D_{L}:=\left\{v \in \mathbb{P}\left(L \otimes_{\mathscr{O}_{F}} \mathbb{C}\right) \mid\langle v, v\rangle>0\right\}$$
which is an $n$-dimensional complex ball. For a finite index subgroup $\Gamma \subset \mathrm{U}(L)(\mathbb{Z})$, we define the ball quotient:
$$\mathscr{F}_{L}(\Gamma):=D_{L} / \Gamma .$$

On the other hand, we define the associated quadratic lattice $\left(L_{Q},(),\right)$ over $\mathbb{Z}$ of signature $(2,2 n)$, where $L_{Q}:=L$ as a $\mathbb{Z}$-module and $():,=\operatorname{Tr}_{F / \mathbb{Q}}\langle$,$\rangle . Let \mathscr{D}_{L_{Q}}$ be the Hermitian symmetric domain associated with $\mathrm{O}^{+}\left(L_{Q}\right)(\mathbb{R}) \cong \mathrm{O}^{+}(2,2 n)$ :
$$\mathscr{D}_{L_{Q}}:=\left\{v \in \mathbb{P}\left(L_{Q} \otimes_{\mathbb{Z}} \mathbb{C}\right) \mid(v, v)=0,(v, \bar{v})>0\right\}^{+} .$$

\footnotetext{
Date: August 16, 2022.
Key words and phrases. ball quotient, toroidal compactification, Kodaira dimension, modular form, Hermitian form.
}

Then, we obtain embeddings $\mathrm{U}(L) \hookrightarrow \mathrm{SO}^{+}\left(L_{Q}\right)$ and $D_{L} \hookrightarrow \mathscr{D}_{L_{Q}}$, as was studied in [11].
Now, let us introduce the notion of irregular cusps. Let $I$ be a rank 1 primitive isotropic sublattice of $L$ and $\Gamma(I)_{\mathbb{Q}}$ be the stabilizer of $I \otimes_{\mathscr{O}_{F}} F$. We denote by $W(I)_{\mathbb{Q}}$ its unipotent part and $Z(I)_{\mathbb{Q}}$ the center of $W(I)_{\mathbb{Q}}$. We say $I$ is irregular with (at least) index 2 if $Z(I)_{\mathbb{Q}} \cap \Gamma \neq Z(I)_{\mathbb{Q}} \cap\langle\Gamma,-\mathrm{id}\rangle$ holds. We have to consider whether the cusp corresponding to $I$ branches with higher index or not for $F=\mathbb{Q}(\sqrt{-1})$ or $\mathbb{Q}(\sqrt{-3})$, but for simplicity, we only concern ourselves with this case here. At irregular cusps, we have to pay attention to the vanishing order of modular forms and related pluricanonical forms.

Here, we shall state our main result, which is a unitary analog of [8, Theorem 1.1] or [16, Theorem 8.9].

Theorem 1.1 (Low slope cusp form trick, Theorem 6.3). Let $F$ be an imaginary quadratic field and $L$ be a Hermitian lattice of signature $(1, n)$ over $\mathscr{O}_{F}$. For a finite index subgroup $\Gamma \subset \mathrm{U}(L)(\mathbb{Z})$, we assume that there is a non-zero cusp form $\Psi$ of weight $k$ with respect to $\Gamma$ on $D_{L}$. In addition, we make the following assumptions.
\begin{itemize}
\item[(1)] $v_{R}(\Psi) / k>\left(r_{i}-1\right) /(n+1)$ for every irreducible component $R_{i}$ of the ramification divisors $D_{L} \rightarrow \mathscr{F}_{L}(\Gamma)$ with ramification index $r_{i}$.
\item[(2)] $v_{I}(\Psi) / k>1 /(n+1)$ for every regular isotropic sublattice $I \subset L$.
\item[(3)] $v_{I}(\Psi) / k>m_{I} /(n+1)$ for every (semi-)irregular isotropic sublattice $I \subset L$ with index $m_{I}$.
\item[(4)] $n \geqslant \max _{i, I}\left\{r_{i}-2, m_{I}-1\right\}$
\item[(5)] $\overline{\mathscr{F}}_{L}(\Gamma)$ has at worst canonical singularities.
\end{itemize}
Then the ball quotient $\mathscr{F}_{L}(\Gamma)$ is of general type.
Remark 1.2. Assumptions (4) and (5) are satisfied if $n \geqslant 13$ and $d<-3$ by [2 Theorem 4].
Here, $\overline{\mathscr{F}_{L}(\Gamma)}$ is the canonical toroidal compactification of $\mathscr{F}_{L}(\Gamma)$. For the notion of "semi-irregular", see section 3.

We also consider the relationship between regular/irregular cusps on $D_{L}$ and regular/irregular cusps on $\mathscr{D}_{L_{Q}}$. Note that irregular cusps on $\mathscr{D}_{L_{Q}}$ have been studied by Ma [16]. Let $\Gamma_{O} \subset \mathrm{O}^{+}\left(L_{Q}\right)(\mathbb{Z})$ be a finite index subgroup and $\Gamma_{U} \subset \mathrm{U}(L)(\mathbb{Z})$ be its restriction to the unitary group. In the following proposition, regular/irregular cusps on $D_{L}$ (resp. $\mathscr{D}_{L_{Q}}$ ) mean regular/irregular cusps with respect to $\Gamma_{U}\left(\right.$ resp. $\left.\Gamma_{O}\right)$.

Proposition 1.3. (1) For any imaginary quadratic field $F$, regular cusps on $D_{L}$ map to regular cusps on $\mathscr{D}_{L_{Q}}$.
\begin{itemize}
\item[(2)] For $F \neq \mathbb{Q}(\sqrt{-1}), \mathbb{Q}(\sqrt{-3})$, irregular cusps on $D_{L}$ map to irregular cusps on $\mathscr{D}_{L_{Q}}$.
\item[(3)] For $F=\mathbb{Q}(\sqrt{-1})$, irregular cusps with index 2 or 4 on $D_{L}$ map to irregular cusps with index 2 on $\mathscr{D}_{L_{Q}}$ and semi-irregular cusps with index 2 on $D_{L}$ map to regular cusps on $\mathscr{D}_{L_{Q}}$.
\item[(4)] For $F=\mathbb{Q}(\sqrt{-3})$, irregular cusps with index 2 or 6 and semi-irregular cusps with index 2 on $D_{L}$ map to irregular cusps with index 2 on $\mathscr{D}_{L_{Q}}$ and irregular cusps with index 3 and semi-irregular cusps with index 3 on $D_{L}$ map to regular cusps on $\mathscr{D}_{L_{Q}}$.
\end{itemize}

For the case of discriminant kernel, we completely classify discriminant groups when the lattice may have irregular cusps.

Proposition 1.4. If $F$ is an imaginary quadratic field of class number 1 , and the discriminant kernel of a unitary group has an irregular cusp, then the discriminant group of an even Hermitian lattice is one of those listed in Appendix A.

\section*{2. 0-DIMENSIONAL CUSPS}

Let $F:=\mathbb{Q}(\sqrt{d})$ be an imaginary quadratic field, where $d$ is a square-free negative integer. Let $(L,\langle\rangle$,$) be a Hermitian lattice over \mathscr{O}_{F}$ of signature $(1, n)$, where $n>1$ and $V:=L \otimes_{\mathscr{O}_{F}} F$. We will consider integral Hermitian lattices in the sense described in [11], that is,
$$\langle,\rangle: L \times L \rightarrow \kappa \mathscr{O}_{F}$$
where
$$\kappa:= \begin{cases}\frac{1}{\sqrt{d}} & (d \equiv 1 \bmod 4) \\ \frac{1}{2 \sqrt{d}} & (d \equiv 2,3 \bmod 4) .\end{cases}$$

In this paper, Hermitian forms are complex linear in the first argument and complex conjugate linear in the second argument. We also define the dual lattice $L^{\vee}$ of $L$ :
$$L^{\vee}:=\left\{v \in L \otimes_{\mathscr{O}_{F}} F \mid\langle v, w\rangle \in \kappa \mathscr{O}_{F} \text { for any } w \in L\right\} .$$
This lattice contains $L$ as a finite index lattice, so the discriminant group $A_{L}:=L^{\vee} / L$ is a finite $\mathscr{O}_{F}$ - module. As an important example of an arithmetic group, the discriminant kernel $\widetilde{\mathrm{U}}(L)$ is defined by
$$\widetilde{\mathrm{U}}(L):=\left\{g \in \mathrm{U}(L)(\mathbb{Z})|g|_{A_{L}}=\mathrm{id}\right\} .$$

Now, let us recall the toroidal compactification of $\mathscr{F}_{L}(\Gamma)$ and its cusps. For a rank 1 primitive isotropic sublattice $I \subset L$, let $\Gamma(I)_{\mathbb{Q}}:=\operatorname{Stab}_{\mathrm{U}(L)(\mathbb{Q})}\left(I_{F}\right)$ be the stabilizer of $I_{F}:=I \otimes_{\mathscr{O}_{F}} F$. Here, we review the structure of $\Gamma(I)_{\mathbb{Q}}$; see [2] and [14] for details. Let
$$W(I)_{\mathbb{Q}}:=\operatorname{Ker}\left(\Gamma(I)_{\mathbb{Q}} \rightarrow \mathrm{U}\left(I^{\perp} / I_{F}\right) \times \operatorname{GL}\left(I_{F}\right)\right)$$
be the unipotent radical of $\Gamma(I)_{\mathbb{Q}}$ and
$$Z(I)_{\mathbb{Q}}:=\operatorname{Ker}\left(\Gamma(I)_{\mathbb{Q}} \rightarrow \operatorname{GL}\left(I^{\perp}\right)\right)$$
be its center. We fix a generator $e$ of $I$. By [14], we define
$$T_{e \otimes v}(z):=z+\langle z, e\rangle v-\langle z, v\rangle e-\frac{1}{2}\langle v, v\rangle\langle z, e\rangle e$$
for $v \in I^{\perp}$ and $z \in V$. Then, the following properties hold:
$$\begin{cases}T_{e \otimes \mu v} & =T_{\bar{\mu} e \otimes v}(\mu \in F) \\ T_{e \otimes \lambda e} & =\mathrm{id}_{V}(\lambda \in \mathbb{Q}) \\ T_{e \otimes v} T_{e \otimes u} & =T_{e \otimes\left(v+u+\frac{1}{2}\langle v, u\rangle e\right)} .\end{cases}$$
Thus, it follows that $T_{e \otimes v}$ depends only on $\bar{I}_{F} \otimes I^{\perp} /(\bar{I} \otimes I)(\mathbb{Q})$. Here,
$$(\bar{I} \otimes I)(\mathbb{Q}):=\{\lambda(e \otimes e) \mid \lambda \in \mathbb{Q}\} .$$
From the definition of $T_{e \otimes v}$, it follows $T_{e \otimes v}=\mathrm{id}_{I^{\perp}}$ for $e \otimes v \in \bar{I}_{F} \otimes I_{F}$ so that
$$\begin{array}{ccc}
\bar{I}_{F} \otimes I_{F} /(\bar{I} \otimes I)(\mathbb{Q})=\sqrt{d}(\bar{I} \otimes I)(\mathbb{Q}) & \cong & Z(I)_{\mathbb{Q}} \\
\sqrt{d} \lambda(e \otimes e) & \mapsto & T_{\sqrt{d} \lambda(e \otimes e)} .
\end{array}$$
More directly, by choosing a basis $\left\{e, b_{1}, \ldots, b_{n-1}, e^{\prime}\right\}$ of $V$ such that $\left\{e, b_{1}, \ldots, b_{n-1}\right\}$ is a basis of $I^{\perp}$ and $\left\langle e, e^{\prime}\right\rangle=1$, the Hermitian form is given by
$$\left(\begin{array}{c|c|c}
0 & 0 & 1 \\
\hline 0 & B & 0 \\
\hline 1 & 0 & 0
\end{array}\right)$$
for some Hermitian matrix $B$, and the center of $W(I)_{\mathbb{Q}}$ is given by
$$Z(I)_{\mathbb{Q}}=\left\{\left.\left(\begin{array}{c|c|c}
1 & 0 & \lambda \sqrt{d} \\
\hline 0 & I_{n-1} & 0 \\
\hline 0 & 0 & 1
\end{array}\right) \right\rvert\, \lambda \in \mathbb{Q}\right\} .$$
This gives the isomorphism (2.1) more explicitly,
$$\begin{array}{cc|c}
\bar{I}_{F} \otimes I_{F} /(\bar{I} \otimes I)(\mathbb{Q})=\sqrt{d}(\bar{I} \otimes I)(\mathbb{Q}) & \cong & \quad Z(I)_{\mathbb{Q}} \\
\sqrt{d} \lambda(e \otimes e) & \mapsto & \left(\begin{array}{c|c|c}
1 & 0 & 2 \lambda \sqrt{d} \\
\hline 0 & I_{n-1} & 0 \\
\hline 0 & 0 & 1
\end{array}\right) .
\end{array}$$
(See [2, Lemma 12] for a description.) Now, $\Gamma(I)_{\mathbb{Q}}$ acts on both sides of the equation. The natural action on the left-hand side coincides with the adjoint action on the right-hand side.
$$T_{\sqrt{d} \lambda \gamma(e \otimes e)}=\gamma^{-1} T_{\sqrt{d} \lambda(e \otimes e)} \gamma \quad\left(\gamma \in \Gamma(I)_{\mathbb{Q}}\right) .$$
We also have the following isomorphism,
$$V(I)_{\mathbb{Q}} \cong \bar{I}_{F} \otimes I^{\perp} / I_{F}$$
by [14]. Here, $V(I)_{\mathbb{Q}}$ is defined in (2.4). For a finite index subgroup $\Gamma \subset \mathrm{U}(L)(\mathbb{Z})$, we introduce the following notation from [1] and [16]:
$$\begin{gathered}
\Gamma(I)_{\mathbb{Z}}:=\Gamma(I)_{\mathbb{Q}} \cap \Gamma, W(I)_{\mathbb{Z}}:=W(I)_{\mathbb{Q}} \cap \Gamma, Z(I)_{\mathbb{Z}}:=Z(I)_{\mathbb{Q}} \cap \Gamma \\
\overline{\Gamma(I)_{\mathbb{Z}}}:=\Gamma(I)_{\mathbb{Z}} / Z(I)_{\mathbb{Z}}, V(I)_{\mathbb{Z}}:=W(I)_{\mathbb{Z}} / Z(I)_{\mathbb{Z}}, \Gamma_{I}:=\Gamma(I)_{\mathbb{Z}} / W(I)_{\mathbb{Z}} \\
\overline{\Gamma(I)_{\mathbb{Q}}}:=\Gamma(I)_{\mathbb{Q}} / Z(I)_{\mathbb{Z}}, W(I)_{\mathbb{Q} / \mathbb{Z}}:=W(I)_{\mathbb{Q}} / Z(I)_{\mathbb{Z}}, Z(I)_{\mathbb{Q} / \mathbb{Z}}:=Z(I)_{\mathbb{Q}} / Z(I)_{\mathbb{Z}} .
\end{gathered}$$
Now we have the following exact sequences:
$$\begin{aligned}
0 \rightarrow V(I)_{\mathbb{Z}} & \rightarrow \overline{\Gamma(I)}_{\mathbb{Z}} \rightarrow \Gamma_{I} \rightarrow 1 \\
0 \rightarrow W(I)_{\mathbb{Q} / \mathbb{Z}} & \rightarrow \overline{\Gamma(I)_{\mathbb{Q}}} \rightarrow \mathrm{U}\left(I^{\perp} / I_{F}\right) \times \operatorname{GL}\left(I_{F}\right) \\
0 \rightarrow Z(I)_{\mathbb{Q} / \mathbb{Z}} & \rightarrow W(I)_{\mathbb{Q} / \mathbb{Z}} \rightarrow V(I)_{\mathbb{Q}} \rightarrow 0 .
\end{aligned}$$
Note that $Z(I)_{\mathbb{Q} / \mathbb{Z}}$ is a torsion subgroup of $T(I):=Z(I)_{\mathbb{C}} / Z(I)_{\mathbb{Z}}$. Let $c_{I}:=\mathbb{P}\left(I \otimes_{\mathscr{O}_{F}} \mathbb{C}\right)$ be the cusp corresponding to $I$. We need a representation of $D_{L}$ as a Siegel domain of the third kind. We define $D(I):=Z(I)_{\mathbb{C}} D_{L}$. Then, we obtain the following fibration by [1]:
$$D(I) \cong Z(I)_{\mathbb{C}} \times V(I)_{\mathbb{C}} \times c_{I} \xrightarrow{\pi_{1}} D(I)^{\prime}:=D(I) / Z(I)_{\mathbb{C}} \xrightarrow{\pi_{2}} c_{I} .$$
Moreover, from this fibration, we have
$$D_{L}=\{(z, u) \in D(I) \mid \Im(z)-h\langle u, u\rangle \in C(I)\}$$
for a cone $C(I)$ in $Z(I)_{\mathbb{R}}$ and some real-bilinear quadratic form $h: \mathbb{C}^{n-1} \times \mathbb{C}^{n-1} \rightarrow Z(I)_{\mathbb{R}}$. Accordingly, we have
$$\mathcal{X}(I):=D / Z(I)_{\mathbb{Z}} \subset D(I) / Z(I)_{\mathbb{Z}} \xrightarrow{\bar{\pi}_{1}} D(I)^{\prime} .$$
Here, the quotient fiber bundle $\bar{\pi}_{1}$ is a principal fiber bundle under the algebraic torus $T(I):=$ $Z(I)_{\mathbb{C}} / Z(I)_{\mathbb{Z}}$. Since $\operatorname{dim}_{\mathbb{R}}\left(Z(I)_{\mathbb{R}}\right)=1$, there exists a natural toric embedding $T(I) \hookrightarrow \overline{T(I)}$. In accordance with [1], we define $\overline{\mathcal{X}(I)}$ as the interior of closure of $\mathcal{X}(I)$ in $\mathcal{X}(I) \times_{T(I)} \overline{T(I)}$.

Finally, the toroidal compactification of $\mathscr{F}_{L}(\Gamma)$ is defined by taking the canonical cone decomposition:
$$\overline{\mathscr{F}_{L}(\Gamma)}:=\left(D_{L} \cup \bigcup_{I \subset L} \overline{\mathcal{X}(I)}\right) / \sim$$
where $I$ is a rank 1 primitive isotropic sublattice of $L$ and the equivalence relation is defined in [1].
Remark 2.1. We can also construct the Satake-Baily-Borel compactification $\overline{\mathscr{F}}_{L}(\Gamma)$ SBB of a ball quotient $\mathscr{F}_{L}(\Gamma)$ as follows. We define the rational completion $D_{L}^{\text {SBB }}$ as the union of $D_{L}$ and 0-dimensional cusps:
$$D_{L}^{\mathrm{SBB}}:=D_{L} \cup \bigcup_{I \subset L} c_{I} .$$
Here, $I \subset L$ runs over the rank 1 primitive isotropic sublattices. Now we define $\overline{\mathscr{F}}_{L}(\Gamma){ }^{\text {SBB }}:=D_{L}^{\text {SBB }} / \Gamma$.

\section*{3. Irregular cusps}
3.1. Case of $\mathbb{Q}(\sqrt{-1})$. Throughout this subsection, we assume $F=\mathbb{Q}(\sqrt{-1})$. Let us define irregular cusps.

Proposition 3.1. The following are equivalent.
\begin{itemize}
\item[(1)] $Z(I)_{\mathbb{Z}}=Z(I)_{\mathbb{Q}} \cap\langle\Gamma,-\mathrm{id}\rangle \neq Z(I)_{\mathbb{Q}} \cap\langle\Gamma, \sqrt{-1} \mathrm{id}\rangle$.
\item[(2)] - $\operatorname{id} \in \Gamma, \sqrt{-1} \operatorname{id} \notin \Gamma$, and $\sqrt{-1} T_{\sqrt{-1} \lambda(e \otimes e)} \in \Gamma(I)_{\mathbb{Z}}$ for some $\sqrt{-1} \lambda(e \otimes e) \in \sqrt{-1}(\bar{I} \otimes I)(\mathbb{Q})$.
\item[(3)] $-\mathrm{id} \in \Gamma, \sqrt{-1} \mathrm{id} \notin \Gamma$, and there exists an element $\gamma \in \overline{\Gamma(I)}_{\mathbb{Z}}$ of order 4, acting on $Z(I)_{\mathbb{Z}}$ and $V(I)_{\mathbb{C}}$ trivially and $\mathcal{X}(I)$ non-trivially, and whose image in $\mathrm{U}\left(I^{\perp}\right) \times \mathrm{GL}\left(I_{F}\right)$ is $\left(\sqrt{-1} \mathrm{id}_{I^{\perp} / I_{F}}, \sqrt{-1} \mathrm{id}_{I_{F}}\right)$. Moreover, the order of this non-trivial action on $\mathcal{X}(I)$ is 2.
\end{itemize}

Proof. (1) ⇒ (2) Since $\sqrt{-1} \mathrm{id} \notin \Gamma$, there exists an element $T_{\sqrt{-1} \lambda(e \otimes e)} \in Z(I)_{\mathbb{Q}} \cap\langle\Gamma, \sqrt{-1} \mathrm{id}\rangle\left\langle Z(I)_{\mathbb{Z}}\right.$ for some $\sqrt{-1} \lambda(e \otimes e) \in \sqrt{-1}(\bar{I} \otimes I)(\mathbb{Q})$. Now $\langle\Gamma, \sqrt{-1} \mathrm{id}\rangle=\Gamma \sqcup \sqrt{-1} \Gamma$ so that $T_{\sqrt{-1} \lambda(e \otimes e)} \in \sqrt{-1} \Gamma$. Combining this with the condition - id $\in \Gamma$, it follows $\sqrt{-1} T_{\sqrt{-1} \lambda(e \otimes e)} \in \Gamma(I)_{\mathbb{Z}}$.
(2) ⇒ (1) Since $-\mathrm{id} \in \Gamma$, we have $Z(I)_{\mathbb{Z}}=Z(I)_{\mathbb{Q}} \cap\langle\Gamma,-\mathrm{id}\rangle$. On the other hand, $\sqrt{-1} T_{\sqrt{-1} \lambda(e \otimes e)} \in$ $\Gamma(I)_{\mathbb{Z}}$ and $\sqrt{-1} \operatorname{id} \notin \Gamma$ together shows that $T_{\sqrt{-1} \lambda(e \otimes e)} \in Z(I)_{\mathbb{Q}} \cap\langle\Gamma, \sqrt{-1} \operatorname{id}\rangle \backslash Z(I)_{\mathbb{Z}}$.
(2) ⇒ (3) Let $\gamma:=\sqrt{-1} T_{\sqrt{-1} \lambda e \otimes \lambda e}$ be an order 4 element in $\overline{\Gamma(I)}_{\mathbb{Z}}$. The element $\gamma$ acts on $\bar{I}$ as $-\sqrt{-1}$-times and $I^{\perp} / I$ as $\sqrt{-1}$-times. Hence, $\gamma$ acts on $V(I)_{\mathbb{C}}$ trivially. By definition, $\sqrt{-1} \mathrm{id}$ and $T_{\sqrt{-1} \lambda(e \otimes e)}$ act on $Z(I)_{\mathbb{Z}}$ trivially, so the same holds for $\gamma$. We also have the image of $\gamma \in \overline{\Gamma(I)_{\mathbb{Z}}}$ in $\mathrm{U}\left(I^{\perp}\right) \times \operatorname{GL}\left(I_{F}\right)$ is $\left(\sqrt{-1} \mathrm{id}_{I^{\perp} / I_{F}}, \sqrt{-1} \mathrm{id}_{I_{F}}\right)$.

On the other hand, under the assumption $\sqrt{-1} \notin \Gamma$, it follows $T_{\sqrt{-1} \lambda(e \otimes e)} \notin Z(I)_{\mathbb{Z}}$. This means that $\gamma$ acts on $\mathcal{X}(I)$ non-trivially. Note that $Z(I)_{\mathbb{Q}}$ acts on $\mathcal{X}(I) \subset T(I):=Z(I)_{\mathbb{C}} / Z(I)_{\mathbb{Z}}$ as a translation, so the above action is a non-trivial translation.
(3) ⇒ (2) From (2.3), we have $\gamma=\left(\sqrt{-1} \mathrm{id}_{I^{\perp} / I_{F}}, \sqrt{-1} \mathrm{id}_{I_{F}}, \alpha\right)$ for some $\alpha \in W(I)_{\mathbb{Q} / \mathbb{Z}}$. Since $\gamma$ acts on $V(I)_{\mathbb{C}}$ trivially, it follows that the image of $\alpha$ in $V(I)_{\mathbb{Q}}$ is 0 in (2.4), so $\alpha \in Z(I)_{\mathbb{Q} / \mathbb{Z}}$. Hence, $\gamma=\left(\sqrt{-1} \mathrm{id}_{I^{\perp} / I_{F}}, \sqrt{-1} \mathrm{id}_{I_{F}}, T_{\sqrt{-1} \lambda(e \otimes e)}\right)$ for some $\sqrt{-1} \lambda(e \otimes e) \in \sqrt{-1(I \otimes I)(\mathbb{Q})}$. Now, we have $\sqrt{-1} \mathrm{id}_{L}=\left(\sqrt{-1} \mathrm{id}_{I^{\perp} / I_{F}}, \sqrt{-1} \mathrm{id}_{I_{F}}, 0\right)$, so combining this with $\gamma=\left(\sqrt{-1} \mathrm{id}_{I^{\perp} / I_{F}}, \sqrt{-1} \mathrm{id}_{I_{F}}, T_{\sqrt{-1} \lambda(e \otimes e)}\right)$, it follows $\sqrt{-1} \gamma=-T_{\sqrt{-1} \lambda(e \otimes e)} \in \Gamma$. Since we have assumed - $\mathrm{id} \in \Gamma$ so that $\sqrt{-1} T_{\sqrt{-1} \lambda(e \otimes e)} \in \Gamma$. \(\square\)

Geometrically, the existence of such a cusp corresponds to the existence of a branch divisor on the boundary of a ball quotient with branch index 2 . We can show the following propositions in the same way as Proposition 3.1

Definition 3.2. We say that $I$ is semi-irregular with index 2 if the conditions in Proposition 3.1 are satisfied. Here, we define $Z(I)_{\mathbb{Z}}^{\prime}:=Z(I)_{\mathbb{Q}} \cap\langle\Gamma, \sqrt{-1} \mathrm{id}\rangle$ and $\Gamma(I)_{\mathbb{Z}}^{\prime}:=\left\langle\Gamma(I)_{\mathbb{Z}}, \sqrt{-1} \mathrm{id}\right\rangle /\langle\sqrt{-1} \mathrm{id}\rangle$.

Now, let us treat the index 4 case.
Proposition 3.3. The following statements are equivalent.
\begin{itemize}
\item[(1)] $Z(I)_{\mathbb{Z}} \neq Z(I)_{\mathbb{Q}} \cap\langle\Gamma,-\mathrm{id}\rangle \neq Z(I)_{\mathbb{Q}} \cap\langle\Gamma, \sqrt{-1} \mathrm{id}\rangle$, that is, all three are different.
\item[(2)] - id, $\sqrt{-1} \mathrm{id} \notin \Gamma$, and $-\sqrt{-1} T_{\sqrt{-1} \lambda(e \otimes e)} \in \Gamma(I)_{\mathbb{Z}}$ for some $\sqrt{-1} \lambda(e \otimes e) \in \sqrt{-1}(\bar{I} \otimes I)(\mathbb{Q})$.
\item[(3)] $\sqrt{-1} \mathrm{id} \notin \Gamma$, and there exists an element $\gamma \in \overline{\Gamma(I)}_{\mathbb{Z}}$ of order 4 acting on $Z(I)_{\mathbb{Z}}$ and $V(I)_{\mathbb{C}}$ trivially and $\mathcal{X}(I)$ non-trivially, and whose image in $\mathrm{U}\left(I^{\perp}\right) \times \mathrm{GL}\left(I_{F}\right)$ is $\left(\sqrt{-1} \mathrm{id}_{I^{\perp} / I_{F}}, \sqrt{-1} \mathrm{id}_{I_{F}}\right)$. Moreover, the order of this non-trivial action on $\mathcal{X}(I)$ is 4.
\end{itemize}

Proof. This can be proven in the same way as Proposition 3.1 \(\square\)

Definition 3.4. We say that $I$ is irregular with index 4 if the conditions in Proposition 3.3 are satisfied. Here, we define $Z(I)_{\mathbb{Z}}^{\prime}:=Z(I)_{\mathbb{Q}} \cap\langle\Gamma, \sqrt{-1} \mathrm{id}\rangle$ and $\Gamma(I)_{\mathbb{Z}}^{\prime}:=\left\langle\Gamma(I)_{\mathbb{Z}}, \sqrt{-1} \mathrm{id}\right\rangle /\langle\sqrt{-1} \mathrm{id}\rangle$.
3.2. Case of $\mathbb{Q}(\sqrt{-3})$. Throughout this subsection, we assume $F=\mathbb{Q}(\sqrt{-3})$. Let $\omega$ be a primitive root of unity.

Proposition 3.5. The following statements are equivalent.
\begin{itemize}
\item[(1)] $Z(I)_{\mathbb{Z}}=Z(I)_{\mathbb{Q}} \cap\langle\Gamma, \omega \mathrm{id}\rangle \neq Z(I)_{\mathbb{Q}} \cap\langle\Gamma,-\mathrm{id}\rangle$.
\item[(2)] $\omega \mathrm{id} \in \Gamma,-\mathrm{id} \notin \Gamma$, and $-T_{\sqrt{-3} \lambda(e \otimes e)} \in \Gamma(I)_{\mathbb{Z}}$ for some $\sqrt{-3} \lambda(e \otimes e) \in \sqrt{-3}(\bar{I} \otimes I)(\mathbb{Q})$.
\item[(3)] $\omega \mathrm{id} \in \Gamma,-\mathrm{id} \notin \Gamma$, and there exists an element $\gamma \in \overline{\Gamma(I)}_{\mathbb{Z}}$ of order 6, acting on $Z(I)_{\mathbb{Z}}$ and $V(I)_{\mathbb{C}}$ trivially and $\mathcal{X}(I)$ non-trivially, and whose image in $\mathrm{U}\left(I^{\perp}\right) \times \mathrm{GL}\left(I_{F}\right)$ is $\left(-\mathrm{id}_{I^{\perp} / I_{F}},-\mathrm{id}_{I_{F}}\right)$. Moreover, the order of this non-trivial action on $\mathcal{X}(I)$ is 2.
\end{itemize}

Proof. This can be proven in the same way as Proposition 3.1 . \(\square\)

Definition 3.6. We say that $I$ is semi-irregular with index 2 if the conditions in Proposition 3.5 are satisfied. Here, we define $Z(I)_{\mathbb{Z}}^{\prime}:=Z(I)_{\mathbb{Q}} \cap\langle\Gamma, \omega \mathrm{id}\rangle$ and $\Gamma(I)_{\mathbb{Z}}^{\prime}:=\left\langle\Gamma(I)_{\mathbb{Z}}, \omega \mathrm{id}\right\rangle\langle\langle\omega \mathrm{id}\rangle$.

Proposition 3.7. The following statements are equivalent.
\begin{itemize}
\item[(1)] $Z(I)_{\mathbb{Z}}=Z(I)_{\mathbb{Q}} \cap\langle\Gamma,-\mathrm{id}\rangle \neq Z(I)_{\mathbb{Q}} \cap\langle\Gamma,-\omega \mathrm{id}\rangle$.
\item[(2)] - $\operatorname{id} \in \Gamma, \omega \mathrm{id} \notin \Gamma$, and $-T_{\sqrt{-3} \lambda(e \otimes e)} \in \Gamma(I)_{\mathbb{Z}}$ for some $\sqrt{-3} \lambda(e \otimes e) \in \sqrt{-3}(\bar{I} \otimes I)(\mathbb{Q})$.
\end{itemize}
\begin{itemize}
\item[(3)] - $\operatorname{id} \in \Gamma, \omega \operatorname{id} \notin \Gamma$, and there exists an element $\gamma \in \overline{\Gamma(I)}_{\mathbb{Z}}$ of order 6, acting on $Z(I)_{\mathbb{Z}}$ and $V(I)_{\mathbb{C}}$ trivially and $\mathcal{X}(I)$ non-trivially, and whose image in $\mathrm{U}\left(I^{\perp}\right) \times \mathrm{GL}\left(I_{F}\right)$ is $\left(\omega \mathrm{id}_{I^{\perp} / I_{F}}, \omega \mathrm{id}_{I_{F}}\right)$. Moreover, the order of this non-trivial action on $\mathcal{X}(I)$ is 3.
\end{itemize}

Proof. This can be proven in the same way as Proposition 3.1 \(\square\)

Definition 3.8. We say that $I$ is semi-irregular with index 3 if the conditions in Proposition 3.5 are satisfied. Here, we define $Z(I)_{\mathbb{Z}}^{\prime}:=Z(I)_{\mathbb{Q}} \cap\langle\Gamma, \omega \mathrm{id}\rangle$ and $\Gamma(I)_{\mathbb{Z}}^{\prime}:=\left\langle\Gamma(I)_{\mathbb{Z}}, \omega \mathrm{id}\right\rangle\langle\omega \mathrm{id}\rangle$.

Proposition 3.9. The following statements are equivalent.
\begin{itemize}
\item[(1)] $Z(I)_{\mathbb{Z}}=Z(I)_{\mathbb{Q}} \cap\langle\Gamma,-\mathrm{id}\rangle \neq Z(I)_{\mathbb{Q}} \cap\langle\Gamma, \omega \mathrm{id}\rangle$.
\item[(2)] - $\operatorname{id} \in \Gamma, \omega \operatorname{id} \notin \Gamma$, and $\omega T_{\sqrt{-3} \lambda(e \otimes e)} \in \Gamma(I)_{\mathbb{Z}}$ for some $\sqrt{-3} \lambda(e \otimes e) \in \sqrt{-3}(\bar{I} \otimes I)(\mathbb{Q})$.
\item[(3)] - $\mathrm{id} \in \Gamma, \omega \mathrm{id} \notin \Gamma$, and there exists an element $\gamma \in \overline{\Gamma(I)}_{\mathbb{Z}}$ of order 3, acting on $Z(I)_{\mathbb{Z}}$ and $V(I)_{\mathbb{C}}$ trivially and $\mathcal{X}(I)$ non-trivially, and whose image in $\mathrm{U}\left(I^{\perp}\right) \times \mathrm{GL}\left(I_{F}\right)$ is $\left(\omega \mathrm{id}_{I^{\perp} / I_{F}}, \omega \mathrm{id}_{I_{F}}\right)$. Moreover, the order of this non-trivial action on $\mathcal{X}(I)$ is 3.
\end{itemize}

Proof. This can be proven in the same way as Proposition 3.1 \(\square\)

Definition 3.10. We say that $I$ is irregular with index 3 if the conditions in Proposition 3.9 are satisfied. Here, we define $Z(I)_{\mathbb{Z}}^{\prime}:=Z(I)_{\mathbb{Q}} \cap\langle\Gamma, \omega \mathrm{id}\rangle$ and $\Gamma(I)_{\mathbb{Z}}^{\prime}:=\left\langle\Gamma(I)_{\mathbb{Z}}, \omega \mathrm{id}\right\rangle\langle\langle\omega \mathrm{id}\rangle$.

Proposition 3.11. The following statements are equivalent.
\begin{itemize}
\item[(1)] $Z(I)_{\mathbb{Z}} \neq Z(I)_{\mathbb{Q}} \cap\langle\Gamma,-\mathrm{id}\rangle \neq Z(I)_{\mathbb{Q}} \cap\langle\Gamma, \omega\rangle$, that is, all three are different.
\item[(2)] - id, $\omega \mathrm{id} \notin \Gamma$, and $-\omega T_{\sqrt{-3} \lambda(e \otimes e)} \in \Gamma(I)_{\mathbb{Z}}$ for some $\sqrt{-3} \lambda(e \otimes e) \in \sqrt{-3}(\bar{I} \otimes I)(\mathbb{Q})$.
\item[(3)] - $\mathrm{id}, \omega \mathrm{id} \notin \Gamma$, and there exists an element $\gamma \in \overline{\Gamma(I)}_{\mathbb{Z}}$ of order 6, acting on $Z(I)_{\mathbb{Z}}$ and $V(I)_{\mathbb{C}}$ trivially and $\mathcal{X}(I)$ non-trivially, and whose image in $\mathrm{U}\left(I^{\perp}\right) \times \mathrm{GL}\left(I_{F}\right)$ is $\left(-\omega \mathrm{id}_{I^{\perp} / I_{F}},-\omega \mathrm{id}_{I_{F}}\right)$. Moreover, the order of this non-trivial action on $\mathcal{X}(I)$ is 6.
\end{itemize}

Proof. This can be proven in the same way as Proposition 3.1 \(\square\)

Definition 3.12. We say that $I$ is irregular with index 6 if the conditions in Proposition 3.11 are satisfied. Here, we define $Z(I)_{\mathbb{Z}}^{\prime}:=Z(I)_{\mathbb{Q}} \cap\langle\Gamma,-\mathrm{id}, \omega \mathrm{id}\rangle$ and $\Gamma(I)_{\mathbb{Z}}^{\prime}:=\left\langle\Gamma(I)_{\mathbb{Z}},-\mathrm{id}, \omega \mathrm{id}\right\rangle\langle\langle-\mathrm{id}, \omega \mathrm{id}\rangle$.
3.3. Other cases. Let $F$ be any imaginary quadratic field.

Proposition 3.13. The following statements are equivalent.
\begin{itemize}
\item[(1)] $Z(I)_{\mathbb{Z}} \neq Z(I)_{\mathbb{Q}} \cap\langle\Gamma,-\mathrm{id}\rangle$.
\item[(2)] $-\mathrm{id} \notin \Gamma$, and $-T_{\sqrt{d} \lambda(e \otimes e)} \in \Gamma(I)_{\mathbb{Z}}$ for some $\sqrt{d} \lambda(e \otimes e) \in \sqrt{d}(\bar{I} \otimes I)(\mathbb{Q})$.
\item[(3)] -id $\notin \Gamma$, and there exists an element $\gamma \in \overline{\Gamma(I)}_{\mathbb{Z}}$ of order 2, acting on $Z(I)_{\mathbb{Z}}$ and $V(I)_{\mathbb{C}}$ trivially and $\mathcal{X}(I)$ non-trivially, and whose image in $\mathrm{U}\left(I^{\perp}\right) \times \mathrm{GL}\left(I_{F}\right)$ is $\left(-\mathrm{id}_{I^{\perp} / I_{F}},-\mathrm{id}_{I_{F}}\right)$. Moreover, the order of this non-trivial action on $\mathcal{X}(I)$ is 2.
\end{itemize}

Proof. This can be proven in the same way as Proposition 3.1 \(\square\)

Definition 3.14. We say that $I$ is irregular with index 2 if the following holds. If $F \neq \mathbb{Q}(\sqrt{-1}), \mathbb{Q}(\sqrt{-3})$, then the conditions in Proposition 3.13 are satisfied. If $F=\mathbb{Q}(\sqrt{-1})$, then the conditions in Proposition 3.13 are satisfied and the conditions in Proposition 3.3 are not satisfied. If $F=\mathbb{Q}(\sqrt{-3})$, then the conditions in Proposition 3.13 are satisfied and the conditions in Proposition 3.5 and Proposition 3.11 are not satisfied. In these cases, we define $Z(I)_{\mathbb{Z}}^{\prime}:=Z(I)_{\mathbb{Q}} \cap\langle\Gamma,-\mathrm{id}\rangle$ and $\Gamma(I)_{\mathbb{Z}}^{\prime}:=$ $\left\langle\Gamma(I)_{\mathbb{Z}},-\mathrm{id}\right\rangle /\langle-\mathrm{id}\rangle$.

Definition 3.15. We say that $I$ is regular if $I$ is not irregular or semi-irregular in the sense of the above definitions.
3.4. Relation with irregular cusps on orthogonal modular varieties. Now, let us give another description of regular or irregular cusps. We define
$$Z(I)_{\mathbb{Z}}^{\star}:= \begin{cases}\left(\{ \pm 1, \pm \sqrt{-1}\} Z(I)_{\mathbb{Q}}\right) \cap \Gamma & (F=\mathbb{Q}(\sqrt{-1})) \\ \left(\left\{ \pm 1, \pm \omega, \pm \omega^{2}\right\} Z(I)_{\mathbb{Q}}\right) \cap \Gamma & (F=\mathbb{Q}(\sqrt{-3})) \\ \left(\{ \pm 1\} Z(I)_{\mathbb{Q}}\right) \cap \Gamma & (F \neq \mathbb{Q}(\sqrt{-1}, \mathbb{Q}(\sqrt{-3}))) .\end{cases}$$
We can classify irregular cusps according to the structure of $Z(I)_{\mathbb{Z}}^{\star} / Z(I)_{\mathbb{Z}}$.

For $F=\mathbb{Q}(\sqrt{-1})$,
$$Z(I)_{\mathbb{Z}}^{\star} / Z(I)_{\mathbb{Z}} \cong \begin{cases}1 & \left(\text { type } R_{1}\right) \\ \langle-\mathrm{id}\rangle \cong \mathbb{Z} / 2 \mathbb{Z} & \left(\text { type } R_{2}\right) \\ \langle\sqrt{-1} \mathrm{id}\rangle \cong \mathbb{Z} / 4 \mathbb{Z} & \left(\text { type } R_{4}\right) \\ \left\langle-T_{\sqrt{-1} \lambda(e \otimes e)}\right\rangle \cong \mathbb{Z} / 2 \mathbb{Z} & \left(\text { type } I_{2}\right) \\ \left\langle-\mathrm{id},-\sqrt{-1} T_{\sqrt{-1} \lambda(e \otimes e)}\right\rangle \cong \mathbb{Z} / 2 \mathbb{Z} \times \mathbb{Z} / 2 \mathbb{Z} & \left(\text { type } S I_{2}\right) \\ \left\langle-\sqrt{-1} T_{\sqrt{-1} \lambda(e \otimes e)}\right\rangle \cong \mathbb{Z} / 4 \mathbb{Z} & \left(\text { type } I_{4}\right)\end{cases}$$
For $F=\mathbb{Q}(\sqrt{-3})$,
$$Z(I)_{\mathbb{Z}}^{\star} / Z(I)_{\mathbb{Z}} \cong \begin{cases}1 & \left(\text { type } R_{1}\right) \\ \langle-\mathrm{id}\rangle \cong \mathbb{Z} / 2 \mathbb{Z} & \text { (type } \left.R_{2}\right) \\ \langle\omega \mathrm{id}\rangle \cong \mathbb{Z} / 3 \mathbb{Z} & \left(\text { type } R_{3}\right) \\ \langle-\omega \mathrm{id}\rangle \cong \mathbb{Z} / 6 \mathbb{Z} & \left(\text { type } R_{6}\right) \\ \left\langle-T_{\sqrt{-3} \lambda(e \otimes e)}\right\rangle \cong \mathbb{Z} / 2 \mathbb{Z} & \left(\text { type } I_{2}\right) \\ \left\langle-\omega,-T_{\sqrt{-3} \lambda(e \otimes e)}\right\rangle \cong \mathbb{Z} / 3 \mathbb{Z} \times \mathbb{Z} / 2 \mathbb{Z} \cong \mathbb{Z} / 6 \mathbb{Z} & \left(\text { type } S I_{2}\right) \\ \left\langle\omega T_{\sqrt{-3} \lambda(e \otimes e)}\right\rangle \cong \mathbb{Z} / 3 \mathbb{Z} & \left(\text { type } I_{3}\right) \\ \left\langle-\mathrm{id}, \omega T_{\sqrt{-3} \lambda(e \otimes e)}\right\rangle \cong \mathbb{Z} / 2 \mathbb{Z} \times \mathbb{Z} / 3 \mathbb{Z} \cong \mathbb{Z} / 6 \mathbb{Z} & \left(\text { type } S I_{3}\right) \\ \left\langle-\omega T_{\sqrt{-3} \lambda(e \otimes e)}\right\rangle \cong \mathbb{Z} / 6 \mathbb{Z} & \text { (type } \left.I_{6}\right) .\end{cases}$$
For $F \neq \mathbb{Q}(\sqrt{-1}), \mathbb{Q}(\sqrt{-3})$,
$$Z(I)_{\mathbb{Z}}^{\star} / Z(I)_{\mathbb{Z}} \cong \begin{cases}1 & \left(\text { type } R_{1}\right) \\ \langle-\mathrm{id}\rangle \cong \mathbb{Z} / 2 \mathbb{Z} & \left(\text { type } R_{2}\right) \\ \left\langle-T_{\sqrt{d} \lambda(e \otimes e)}\right\rangle \cong \mathbb{Z} / 2 \mathbb{Z} & \left(\text { type } I_{2}\right)\end{cases}$$
Here, type $R_{\star}$ corresponds to regular cusps, and type $I_{\star}$ (resp. $S I_{\star}$ ) corresponds to irregular (resp. semi-irregular) cusps with index ★.

Now we will explicitly show how the type of cusps varies when arithmetic subgroups change, and consider the relationship between unitary cusps and orthogonal cusps. Figures 1, 2, 3 show whether the cusps with respect to finite index subgroups of $\mathrm{U}(L)(\mathbb{Z})$ are regular or irregular according to inclusions. We fix an irregular cusp $I$. For a finite index subgroup $\Gamma \subset \operatorname{U}(L)(\mathbb{Z})$, these figures represent the type candidates of another finite index subgroup $\Gamma^{\prime} \subset \mathrm{U}(L)(\mathbb{Z})$ having the inclusion relationship with $\Gamma$. If $\Gamma \subset \Gamma^{\prime}$ and $\Gamma$ is type $X$, then $\Gamma^{\prime}$ is type located above $X$ in the figures, and if $\Gamma^{\prime} \subset \Gamma$, then $\Gamma^{\prime}$ is type located below $X$ in the figures. For example, in Figure 1, for $F=\mathbb{Q}(\sqrt{-1})$, let $\Gamma$ be type $R_{2}$. Then $\Gamma^{\prime} \supset \Gamma$ is type $R_{2}, S I_{2}$ or $R_{4}$. On the other hand if $\Gamma^{\prime} \subset \Gamma$, then $\Gamma^{\prime}$ is type $R_{2}, I_{2}$ or $R_{1}$. Circle nodes mean regular cusps and diamond nodes mean irregular cusps.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/1d82dc1d-9b89-423c-9f41-d1e4693f0a1c-07.jpg?height=434&width=88&top_left_y=2056&top_left_x=991}
\captionsetup{labelformat=empty}
\caption{Figure 1. $F \neq \mathbb{Q}(\sqrt{-1}), \mathbb{Q}(\sqrt{-3})$}
\end{figure}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/1d82dc1d-9b89-423c-9f41-d1e4693f0a1c-08.jpg?height=624&width=349&top_left_y=275&top_left_x=859}
\captionsetup{labelformat=empty}
\caption{Figure 2. $F=\mathbb{Q}(\sqrt{-1})$}
\end{figure}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/1d82dc1d-9b89-423c-9f41-d1e4693f0a1c-08.jpg?height=658&width=868&top_left_y=1089&top_left_x=600}
\captionsetup{labelformat=empty}
\caption{Figure 3. $F=\mathbb{Q}(\sqrt{-3})$}
\end{figure}

Next, let us discuss the relationship between regular/irregular cusps on ball quotients and regular/irregular cusps on orthogonal modular varieties, as studied in [16]. We will borrow a notion of Hermitian forms; i.e., $(L,\langle\rangle$,$) denotes a Hermitian lattice of signature (1, n)$ over $\mathscr{O}_{F}$. We can embed unitary Hermitian symmetric domains (type I) into orthogonal Hermitian symmetric domains (type IV). In regard to the following discussion on orthogonal modular varieties, the reader may find it informative to consult [11, 18, 19].

Let $\left(L_{Q},(),\right)$ be the associated quadratic lattice over $\mathbb{Z}$ of signature $(2,2 n)$, i.e., $L_{Q}:=L$ as a $\mathbb{Z}$-module and ( , ) $:=\operatorname{Tr}_{F / \mathbb{Q}}\langle$, $\rangle$. The associated orthogonal Hermitian symmetric domain is defined by
$$\mathscr{D}_{L_{Q}}:=\left\{v \in \mathbb{P}\left(L_{Q} \otimes \mathbb{C}\right) \mid(v, v)=0,(v, \bar{v})>0\right\}^{+} .$$
Then, we obtain the following embedding:
$$\iota: D_{L} \hookrightarrow \mathscr{D}_{L_{Q}} .$$
By abuse of notation, we also denote by $\iota: \mathrm{U}(L) \hookrightarrow \mathrm{O}^{+}\left(L_{Q}\right)$. In this embedding, we identify the unitary group $\mathrm{U}(L)$ with a subgroup of $\mathrm{O}^{+}\left(L_{Q}\right)$. Specifically, we get
$$\mathrm{U}(V)=\left\{\gamma \in \mathrm{O}^{+}\left(\left(L_{Q}\right)_{\mathbb{Q}}\right) \mid j_{d} \gamma j_{d}=d \gamma\right\}$$
where $j_{d} \in \mathrm{O}^{+}\left(\left(L_{Q}\right)_{\mathbb{Q}}\right)$ satisfies $j_{d}^{2}=d \operatorname{id}_{L_{Q}}$. Explicitly,
$$j_{d}:=\left(\begin{array}{ccc}
\left(\begin{array}{cc}
0 & d \\
1 & 0
\end{array}\right) & 0 & 0 \\
0 & \ddots & 0 \\
0 & 0 & \left(\begin{array}{cc}
0 & d \\
1 & 0
\end{array}\right)
\end{array}\right) .$$

We are concerned whether the image of regular/irregular cusps on ball quotients by (3.1) are regular or irregular on orthogonal modular varieties. By [11, Proposition 2], a 0-dimensional cusp on $D_{L}$, corresponding to a rank 1 primitive isotropic sublattice $I \subset L$ maps to a 1-dimensional cusp on $\mathscr{D}_{L_{Q}}$, corresponding to the rank 2 primitive isotropic sublattice $I_{Q} \subset L_{Q}$ spanned by $I$ and $\sqrt{d} I$ (or $(1+\sqrt{d}) / 2 I$ for $d \equiv 1 \bmod 4)$. Ma studied irregular cusps on orthogonal modular varieties; here, we will review some of his results. In orthogonal cases, only 2-ramifications may occur; they are classified as follows:
$$Z\left(I_{Q}\right)_{\mathbb{Z}}^{\star} / Z\left(I_{Q}\right)_{\mathbb{Z}} \cong \begin{cases}1 & \left(\text { type }\left(R_{1}\right)_{O}\right) \\ \langle-\mathrm{id}\rangle \cong \mathbb{Z} / 2 \mathbb{Z} & \left(\text { type }\left(R_{2}\right)_{O}\right) \\ \left\langle-T_{\sqrt{d} \lambda(e \otimes e)}\right\rangle \cong \mathbb{Z} / 2 \mathbb{Z} & \left(\text { type }\left(I_{2}\right)_{O}\right)\end{cases}$$
where $Z\left(I_{Q}\right)_{\mathbb{Z}}$ is the intersection of the center of the unipotent part of the stabilizer of $I_{Q}$ in $\mathrm{O}^{+}\left(\left(L_{Q}\right)_{\mathbb{Q}}\right)$ and a finite index subgroup $\Gamma_{O} \subset \mathrm{O}^{+}\left(L_{Q}\right)(\mathbb{Z})$ as in our unitary case. Type $\left(R_{1}\right)_{O}$ and $\left(R_{2}\right)_{O}$ (resp. $\left(I_{2}\right)_{O}$ ) means that $I_{Q}$ is regular (resp. irregular with index 2) in $\mathscr{D}_{L_{Q}} / \Gamma_{O}$. Note that the image of $Z(I)_{\mathbb{Q}}$ is precisely $Z\left(I_{Q}\right)_{\mathbb{Q}}$ and the image of the discriminant kernel in the unitary group is a subgroup of the discriminant kernel in the orthogonal group. By [16, Corollary 3,6], we obtain Figure 4 in the orthogonal case.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/1d82dc1d-9b89-423c-9f41-d1e4693f0a1c-09.jpg?height=331&width=90&top_left_y=1379&top_left_x=990}
\captionsetup{labelformat=empty}
\caption{Figure 4. Orthogonal case}
\end{figure}

Now, let us study the image of regular/irregular cusps on orthogonal modular varieties. Refer to Figures 5, 6, 7. By [8, Lemma 2.5], for a 1-dimensional cusp $J \subset L_{Q}$, the center of the unipotent part of its stabilizer in $\mathrm{O}^{+}\left(\left(L_{Q}\right)_{\mathbb{Q}}\right)$ is described as
$$Z(J)_{\mathbb{Q}}=\left\{\left.\left(\begin{array}{ccc}
I_{2} & 0 & \left(\begin{array}{cc}
0 & e \lambda \\
\lambda & 0
\end{array}\right) \\
0 & I_{2 n-2} & 0 \\
0 & 0 & I_{2}
\end{array}\right) \right\rvert\, \lambda \in \mathbb{Q}\right\}$$
for some $e \in \mathbb{Q}$. For a 2-dimensional $\mathbb{Q}$-isotropic subspace $J_{\mathbb{Q}} \subset\left(L_{Q}\right)_{\mathbb{Q}}$, if we consider it to be a subset of $V$, it defines an $F$-subspace of $V$ if and only if $e=d$. In that case, the corresponding subspace $I_{F}$ is a 1-dimensional $F$-isotropic subspace of $V$ and hence corresponds to a 0-dimensional cusp. This shows that when $e=d, \iota\left(Z(I)_{\mathbb{Q}}\right)=Z(J)_{\mathbb{Q}}$. We also have $\iota(-\mathrm{id})=-\mathrm{id}, \iota(\sqrt{-1} \mathrm{id})=j_{-1}$ and
$$\iota(\omega \mathrm{id})=\left(\begin{array}{ccc}
\left(\begin{array}{cc}
0 & 1 \\
-1 & -1
\end{array}\right) & 0 & 0 \\
0 & \ddots & 0 \\
0 & 0 & \left(\begin{array}{cc}
0 & 1 \\
-1 & -1
\end{array}\right)
\end{array}\right) .$$

In this situation, consider the following problem. Let $J \subset L_{Q}$ be a 1-dimensional cusp and $e=d$ as above. Let $I \subset L$ be the corresponding 0-dimensional cusp. Note that $\iota\left(Z(I)_{\mathbb{Q}}\right)=Z(J)_{\mathbb{Q}}$ holds. We assume $J$ is a regular or an irregular cusp in the sense of [16, Definition 6.2] with respect to a finite index subgroup $\Gamma_{O} \subset \mathrm{O}^{+}\left(L_{Q}\right)(\mathbb{Z})$. We shall determine whether the corresponding cusp $I$ is regular or irregular in the sense of the above definitions with respect to $\Gamma_{U}:=\iota^{-1}\left(\Gamma_{O}\right)$.

If $J$ is irregular, then $\Gamma_{O}$ is type $\left(I_{2}\right)_{O}$. In this case, since $-\mathrm{id} \notin \Gamma_{O}$, we have $-\mathrm{id} \notin \Gamma_{U}$; moreover, from the fact $\iota\left(Z(I)_{\mathbb{Q}}\right)=Z(J)_{\mathbb{Q}}$, it follows that $I$ is irregular and $\Gamma_{U}$ is type $I_{2}, I_{4}, S I_{2}$ or $I_{6}$. On the other hand, if $J$ is irregular, then $\Gamma_{O}$ is type $\left(R_{1}\right)_{O}$ or $\left(R_{2}\right)_{O}$. In the first case, since $-\mathrm{id} \in \Gamma_{O}$, it follows that $-\mathrm{id} \in \Gamma_{U}$, so we have that $\Gamma_{U}$ is type $R_{1}, R_{3}$, or $I_{3}$. In the second case, since $-\mathrm{id} \notin \Gamma_{U}$, it follows that $\Gamma_{U}$ is type $R_{2}, R_{4}, S I_{2}$ or $S I_{3}$.

In the following figures, star nodes mean that regular cusps in unitary groups become irregular cusps in orthogonal groups. These figures show what the type of $\Gamma_{O} \subset \mathrm{O}^{+}\left(L_{Q}\right)(\mathbb{Z})$ is when $\Gamma_{U} \subset$ $\mathrm{U}(L)(\mathbb{Z})$ is a certain type. For example, for $F=\mathbb{Q}(\sqrt{-1})$, if $\Gamma_{U} \subset \mathrm{U}(L)(\mathbb{Z})$ is type $R_{4}$, then the corresponding 1-dimensional cusp is type $\left(R_{2}\right)_{O}$. Indeed, regular cusps on $D_{L}$ map to regular cusps on $\mathscr{D}_{L_{Q}}$. On the other hand, for $F=\mathbb{Q}(\sqrt{-3})$, if $\Gamma \subset \mathrm{U}(L)(\mathbb{Z})$ is type $S I_{3}$, i.e, semi-irregular with index 3, then the corresponding 1-dimensional cusp is regular $\left(\operatorname{type}\left(R_{2}\right)_{O}\right)$.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/1d82dc1d-9b89-423c-9f41-d1e4693f0a1c-10.jpg?height=468&width=756&top_left_y=1063&top_left_x=657}
\captionsetup{labelformat=empty}
\caption{Figure 5. Relationship between unitary and orthogonal for $F \neq \mathbb{Q}(\sqrt{-1}), \mathbb{Q}(\sqrt{-3})$}
\end{figure}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/1d82dc1d-9b89-423c-9f41-d1e4693f0a1c-10.jpg?height=637&width=785&top_left_y=1861&top_left_x=645}
\captionsetup{labelformat=empty}
\caption{Figure 6. Relationship between unitary and orthogonal for $F=\mathbb{Q}(\sqrt{-1})$}
\end{figure}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/1d82dc1d-9b89-423c-9f41-d1e4693f0a1c-11.jpg?height=1188&width=782&top_left_y=272&top_left_x=642}
\captionsetup{labelformat=empty}
\caption{Figure 7. Relationship between unitary and orthogonal for $F=\mathbb{Q}(\sqrt{-3})$}
\end{figure}

From the figures 5, 6, 7, we obtain the following proposition. Let $\Gamma_{O} \subset \mathrm{O}^{+}\left(L_{Q}\right)(\mathbb{Z})$ be a finite index subgroup and $\Gamma_{U} \subset \mathrm{U}(L)(\mathbb{Z})$ be its restriction. Here, regular/irregular cusps on $D_{L}$ (resp. $\mathscr{D}_{L_{Q}}$ ) mean regular/irregular cusps with respect to $\Gamma_{U}$ (resp. $\Gamma_{O}$ ).

Proposition 3.16. (1) For any imaginary quadratic field $F$, regular cusps on $D_{L}$ map to regular cusps on $\mathscr{D}_{L_{Q}}$.
\begin{itemize}
\item[(2)] For $F \neq \mathbb{Q}(\sqrt{-1}), \mathbb{Q}(\sqrt{-3})$, irregular cusps on $D_{L}$ map to irregular cusps on $\mathscr{D}_{L_{Q}}$.
\item[(3)] For $F=\mathbb{Q}(\sqrt{-1})$, irregular cusps with index 2 or 4 on $D_{L}$ map to irregular cusps with index 2 on $\mathscr{D}_{L_{Q}}$, and semi-irregular cusps with index 2 on $D_{L}$ map to regular cusps on $\mathscr{D}_{L_{Q}}$.
\item[(4)] For $F=\mathbb{Q}(\sqrt{-3})$, irregular cusps with index 2 or 6 and semi-irregular cusps with index 2 on $D_{L}$ map to irregular cusps with index 2 on $\mathscr{D}_{L_{Q}}$, and irregular cusps with index 3 and semi-irregular cusps with index 3 on $D_{L}$ map to regular cusps on $\mathscr{D}_{L_{Q}}$.
\end{itemize}

\section*{4. Discriminant kernel case}

Here, we shall show a structure theorem of the discriminant group when the discriminant kernel may have irregular cusps. In this section, we assume that the class number of $F$ is 1 . For a rank 1 primitive isotropic sublattice $I$ of $L$ and a generator $e$ of $I$, the quantity $\operatorname{div}(I)$ denotes a generator of the principal ideal $\{\langle\ell, e\rangle \mid \ell \in L\}$. Note that, unlike the orthogonal case, there is no canonical choice of this quantity. Let $\Gamma \subset \mathrm{U}(L)(\mathbb{Z})$ be a finite index subgroup.

In this section and Appendix A, we assume that $L$ is even, that is, $\langle\ell, \ell\rangle \in \mathbb{Z}$ for any $\ell \in L$ in the sense of [11]. Note that this implies that the associated quadratic lattice is even. This corresponds to the assumption in [16, subsection 4.1]. Let $a, b \in \mathbb{Z}$ be integers with $a \neq 0$ or $b \neq 0$. This section
uses the following notation:
$$\operatorname{div}(I)= \begin{cases}\frac{2 a+(1+\sqrt{d}) b}{2 \sqrt{d}} & (d \equiv 1 \bmod 4) \\ \frac{a+b \sqrt{d}}{2 \sqrt{d}} & (d \equiv 2,3 \bmod 4) .\end{cases}$$

\subsection*{4.1. Preparation.}

Lemma 4.1 (c.f. [16, Lemma 4.1]). Assuming $\widetilde{\mathrm{U}}(L) \subset \Gamma$, we have $\sqrt{d}(\bar{I} \otimes I)(\mathbb{Z}) \subset Z(I)_{\mathbb{Z}}$. Here,
$$\sqrt{d}(\bar{I} \otimes I)(\mathbb{Z}):=\{\sqrt{d} \lambda(e \otimes e) \mid \lambda \in \mathbb{Z}\} .$$

Proof. For $\sqrt{d} \lambda(e \otimes e) \in \sqrt{d}(\bar{I} \otimes I)(\mathbb{Z})$, we can show that $T_{\sqrt{d} \lambda(e \otimes e)}$ preserves the discriminant group and this gives the inclusion $\sqrt{d}(\bar{I} \otimes I)(\mathbb{Z}) \subset Z(I)_{\mathbb{Z}}$. \(\square\)

Lemma 4.2 (c.f. [16, Lemma 4.3]). Let $\Gamma=\widetilde{\mathrm{U}}(L)$.
\begin{itemize}
\item[(1)] For any imaginary quadratic field $F$ with class number 1, if $I$ is irregular with index 2, then $2 / \operatorname{div}(I)$ is an element of $\mathscr{O}_{F}$.
\item[(2)] For $F=\mathbb{Q}(\sqrt{-1})$, if $I$ is semi-irregular with index 2 (resp. irregular index 4), then ( 1 - $\sqrt{-1}) / \operatorname{div}(I)($ resp. $(1+\sqrt{-1}) / \operatorname{div}(I))$ is an element of $\mathscr{O}_{F}$.
\item[(3)] For $F=\mathbb{Q}(\sqrt{-3})$, if $I$ is semi-irregular with index 2 (resp. (semi-)irregular with index 3, irregular with index 6), then $2 / \operatorname{div}(I)$ (resp. $(1-\omega) / \operatorname{div}(I),(1+\omega) / \operatorname{div}(I))$ is an element of $\mathscr{O}_{F}$.
\end{itemize}

Proof. (1) Assume $-T_{\sqrt{d} \lambda(e \otimes e)} \in \Gamma=\widetilde{\mathrm{U}}(L)$ for some $\sqrt{d} \lambda(e \otimes e) \in \sqrt{d}(\bar{I} \otimes I)(\mathbb{Q})$. Then, for any $v \in I^{\perp} \cap I^{\vee}$, we have
$$-T_{\sqrt{d} \lambda(e \otimes e)}(v)=-v \in v+L$$
because $-T_{\sqrt{d} \lambda(e \otimes e)}$ acts on the discriminant group of $L$ trivially. This implies that $2 v \in L$. By substituting $v=e^{\prime} / \operatorname{div}(I)$, we find that $2 / \operatorname{div}(I) \in \mathscr{O}_{F}$. We can prove (2) and (3) similarly by calculating $\pm \sqrt{-1} T_{\sqrt{-1} \lambda(e \otimes e)}$ and $\pm \omega T_{\sqrt{-3} \lambda(e \otimes e)}$. \(\square\)

Lemma 4.3 (c.f. [16, Lemma 4.2]). Let $\widetilde{\mathrm{U}}(L) \subset \Gamma$. Assume that the following holds for any $\lambda \in F$; if $2 \sqrt{d} \cdot \overline{\operatorname{div}(I)} \lambda$ is an element of $\mathscr{O}_{F}$, then $\lambda$ is an element of $\mathbb{Z}$. Then, $I$ is regular.

Proof. For a fixed $\operatorname{div}(I)$, we take an $e^{\prime} \in L$ such that $\left\langle e, e^{\prime}\right\rangle=\operatorname{div}(I)$. Now, we shall prove that we can take $e^{\prime}$ to be an isotropic vector.

For simplicity, we only consider the case of $d \equiv 2,3 \bmod 4$. We assume $\left\langle e^{\prime}, e^{\prime}\right\rangle \neq 0$. Let $f:=$ $(p+q \sqrt{d}) e+e^{\prime}$ for some integers $p, q \in \mathbb{Z}$. Note that $\langle e, f\rangle=\operatorname{div}(I)$. Then, since we have
$$\left\langle e, e^{\prime}\right\rangle=\operatorname{div}(I)=\frac{a+b \sqrt{d}}{2 \sqrt{d}},$$
it follows that $\langle f, f\rangle=0$ holds if and only if
$$a q+b p=-\left\langle e^{\prime}, e^{\prime}\right\rangle .$$
Here, $-\left\langle e^{\prime}, e^{\prime}\right\rangle$ is in $\mathbb{Z}$ from the condition that $L$ is even. On the other hand, by our assumption in lemma, the greatest common divisor of $a$ and $b$ is 1 so that there exist some integers $p^{\prime}$ and $q^{\prime}$ that make the equation (4.1) hold. Hence, it suffices to replace $e^{\prime}$ with $\left(p^{\prime}+q^{\prime} \sqrt{d}\right) e+e^{\prime}$. The same discussion holds for the case of $d \equiv 1 \bmod 4$. Below, we take $e^{\prime}$ to be an isotropic vector.

First, suppose $I$ is irregular with index 2 . Equivalently, we can assume $-\mathrm{id} \notin \Gamma$ and $-T_{\sqrt{d} \lambda(e \otimes e)} \in \Gamma$. Since $T_{\sqrt{d} \lambda(e \otimes e)}$ preserves $L$, we have
$$T_{\sqrt{d} \lambda(e \otimes e)}\left(e^{\prime}\right)=e^{\prime}+2 \sqrt{d}\left\langle e^{\prime}, e\right\rangle \lambda e \in L .$$
By assumption, $\lambda \in \mathscr{O}_{F}$ so that $\sqrt{d} \lambda(e \otimes e) \in \sqrt{d}(\bar{I} \otimes I)(\mathbb{Z})$. By Lemma 4.1. $T_{\sqrt{d} \lambda(e \otimes e)} \in U(I)_{\mathbb{Z}}$, so we obtain $T_{\sqrt{d} \lambda(e \otimes e)} \in \Gamma$. This implies - $\mathrm{id} \in \Gamma$, which is a contradiction.

We can give similar proofs for other irregular lattices $I$. \(\square\)

For analysis of the structures of discriminant groups, we need some invariant decomposition theorem of finitely generated modules over a principal ideal domain.

Proposition 4.4. Let $\mathscr{O}$ be a principal ideal domain, $N$ be a finite module over $\mathscr{O}$ and $p \neq 0$ be a prime element in $\mathscr{O}$. We assume that an exact sequence
$$0 \rightarrow \mathscr{O} / p^{m} \rightarrow N \rightarrow \bigoplus_{i=1}^{s}\left(\mathscr{O} / p^{i}\right)^{\oplus a_{i}} \rightarrow 0$$
exists for some non-negative integers $m, s, a_{1}, \ldots, a_{s} \in \mathbb{Z}$. Then, the isomorphism class of $N$ satisfying the above exact sequence corresponds to the pair $\left(i_{0}, \ldots, i_{k}, m_{0}, \ldots, m_{k}\right)$ such that
$$\begin{cases}i_{0}<\cdots<i_{k} & \\ a_{i_{\ell}}>0 & (0<\ell \leqslant k) \\ a_{i_{0}}>0 & \left(\text { if } i_{0}>0\right) \\ m_{0}+\cdots+m_{k}=m & \left(m_{i}>0 \text { for any } i\right) \\ 0<m_{\ell}<i_{\ell+1}-i_{\ell} & (0 \leqslant \ell<k) .\end{cases}$$
Moreover,
$$N \cong \begin{cases}\mathscr{O} / p^{m_{0}} \oplus \bigoplus_{\ell=1}^{k}\left\{\left(\mathscr{O} / p^{i_{\ell}}\right)^{\oplus\left(a_{i_{\ell}}-1\right)} \oplus \mathscr{O} / p^{m_{\ell}+i_{\ell}}\right\} \oplus \bigoplus_{\substack{j \neq i_{t} \\ \text { for any } t}}\left(\mathscr{O} / p^{j}\right)^{\oplus a_{j}} & \left(i_{0}=0\right) \\ \bigoplus_{\ell=0}^{k}\left\{\left(\mathscr{O} / p^{i_{\ell}}\right)^{\oplus\left(a_{i_{\ell}}-1\right)} \oplus \mathscr{O} / p^{m_{\ell}+i_{\ell}}\right\} \oplus \bigoplus_{\substack{j \neq i_{t} \\ \text { for any } t}}\left(\mathscr{O} / p^{j}\right)^{\oplus a_{j}} & \left(i_{0}>0\right)\end{cases}$$

Below, we especially compute the case of class number 1 and discriminant kernels. In the rest of this section, let $\Gamma=\widetilde{\mathrm{U}}(L)$. Combining these calculation, it will be possible to narrow down the list of candidates of discriminant groups; see Appendix A for the classification of $A_{L}$.
4.2 . Case of $\mathbb{Q}(\sqrt{-1})$. Let $F=\mathbb{Q}(\sqrt{-1})$.

Proposition 4.5. (1) If $I$ is irregular with index 2 , then $\operatorname{div}(I)= \pm 1, \pm \sqrt{-1}, \pm 1 \pm \sqrt{-1}, \pm 2, \pm 2 \sqrt{-1}$.
\begin{itemize}
\item[(2)] If $I$ is semi-irregular with index 2 , then $\operatorname{div}(I)= \pm 1 \pm \sqrt{-1}$.
\item[(3)] If $I$ is irregular with index 4 , then $\operatorname{div}(I)= \pm 1 \pm \sqrt{-1}$.
\end{itemize}

Proof. (1) We have
$$\frac{2}{\operatorname{div}(I)}=\frac{4(b+a \sqrt{-1})}{a^{2}+b^{2}} .$$
Hence, $2 / \operatorname{div}(I) \in \mathscr{O}_{F}$ implies $(a, b)=( \pm 1,0),(0, \pm 1),( \pm 1, \pm 1),( \pm 2,0),(0, \pm 2),( \pm 2, \pm 2),( \pm 4,0),(0, \pm 4)$ and these pairs are the candidates for irregular $I$ with index 2 by Lemma 4.2. On the other hand,
$$2 \sqrt{-1}\left\langle e^{\prime}, e\right\rangle \lambda=(a+b \sqrt{-1}) \lambda .$$
If $(a+b \sqrt{-1}) \lambda \in \mathscr{O}_{F}$ implies $\lambda \in \mathbb{Z}$, then $I$ is regular by Lemma 4.3. In this case, the pairs $( \pm 1,0),(0, \pm 1),( \pm 1, \pm 1)$ satisfy the condition in Lemma 4.3 that is, if $(a, b)$ is one of these pairs, then $I$ is regular. Hence, from the above discussion, if $I$ is irregular, then $(a, b)=( \pm 2,0),(0, \pm 2)$, $( \pm 2, \pm 2),( \pm 4,0),(0, \pm 4)$ so that $\operatorname{div}(I)= \pm 1, \pm \sqrt{-1}, \pm 1 \pm \sqrt{-1}, \pm 2, \pm 2 \sqrt{-1}$.
(2) We have
$$\frac{1-\sqrt{-1}}{\operatorname{div}(I)}=\frac{2(a+b)+2(a-b) \sqrt{-1}}{a^{2}+b^{2}} .$$
Hence, $(1-\sqrt{-1}) / \operatorname{div}(I) \in \mathscr{O}_{F}$ implies $(a, b)=( \pm 1,0),(0, \pm 1),( \pm 1, \pm 1),( \pm 2, \pm 2)$ and these pairs are the candidates for semi-irregular $I$ with index 2 by Lemma 4.2. By performing the same calculation, if $I$ is irregular, then $(a, b)=( \pm 2, \pm 2)$ so that $\operatorname{div}(I)=( \pm 2 \pm 2 \sqrt{-1}) / 2= \pm 1 \pm \sqrt{-1}$.

We can prove (3) in the same way. \(\square\)
4.3. Case of $\mathbb{Q}(\sqrt{-3})$. Let $F=\mathbb{Q}(\sqrt{-3})$. See subsection 4.4 for the (semi-)index 2 case.

Proposition 4.6. (1) If $I$ is (semi-)irregular with index 3, then
$$\operatorname{div}(I)=\frac{2 a+(1+\sqrt{-3}) b}{2 \sqrt{-3}}$$
has the candidates listed in Table 1.
\begin{itemize}
\item[(2)] If $I$ is irregular with index 6, then
$$\operatorname{div}(I)=\frac{2 a+(1+\sqrt{-3}) b}{2 \sqrt{-3}}$$
has the candidates listed in Table 2.
\end{itemize}

Proof. These also follow from a direct calculation. \(\square\)

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|l|l|l|l|l|l|l|l|l|l|l|}
\hline $a$ & -3 & -3 & -2 & -1 & -1 & -1 & -1 & 0 & 0 & 0 & 0 & 1 & 1 & 1 & 1 & 2 & 3 & 3 \\
\hline $b$ & 0 & 3 & 1 & -1 & 0 & 1 & 2 & -3 & -1 & 1 & 3 & -2 & -1 & 0 & 1 & -1 & -3 & 0 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 1. Candidates for $\operatorname{div}(I)$ for (semi-)irregular $I$ with index 3}
\end{table}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|l|l|l|l|l|}
\hline $a$ & -2 & -1 & -1 & -1 & -1 & 0 & 0 & 1 & 1 & 1 & 1 & 2 \\
\hline $b$ & 1 & -1 & 0 & 1 & 2 & -1 & 1 & -2 & -1 & 0 & 1 & -1 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 2. Candidates for $\operatorname{div}(I)$ for irregular $I$ with index 6}
\end{table}
4.4. Other cases. Let $F \neq \mathbb{Q}(\sqrt{-1})$ be an imaginary quadratic field with class number 1, that is, $F=\mathbb{Q}(\sqrt{-2}), \mathbb{Q}(\sqrt{-3}), \mathbb{Q}(\sqrt{-7}), \mathbb{Q}(\sqrt{-11}), \mathbb{Q}(\sqrt{-19}), \mathbb{Q}(\sqrt{-43}), \mathbb{Q}(\sqrt{-67}), \mathbb{Q}(\sqrt{-163})$. Then, by performing a similar calculation to the one above, we can prove the following proposition by using a computer.

Proposition 4.7. (1) Let $d \equiv 1 \bmod 4$. If $I$ is irregular with index 2 , then
$$\operatorname{div}(I)=\frac{2 a+(1+\sqrt{d}) b}{2 \sqrt{d}}$$
has the candidates listed in Table 3.
\begin{itemize}
\item[(2)] Let $d=-2$. If $I$ is irregular with index 2, then
$$\operatorname{div}(I)=\frac{a+b \sqrt{-2}}{2 \sqrt{-2}}$$
has the candidates listed in Table 4.
\end{itemize}

Proof. These also follow from a direct calculation. \(\square\)

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|l|l|l|l|l|l|l|l|}
\hline $d$ & \multicolumn{15}{|c|}{} \\
\hline \multirow[t]{4}{*}{-3} & $a$ & -4 & -2 & -2 & -2 & -2 & -2 & -1 & -1 & -1 & -1 & 0 & 0 & 0 & 0 \\
\hline & $b$ & 2 & -2 & 0 & 1 & 2 & 4 & -1 & 0 & 1 & 2 & -2 & -1 & 1 & 2 \\
\hline & $a$ & 1 & 1 & 1 & 1 & 2 & 2 & 2 & 2 & 2 & 4 & \multicolumn{4}{|c|}{\multirow{2}{*}{}} \\
\hline & $b$ & -2 & -1 & 0 & 1 & -4 & -2 & -1 & 0 & 2 & -2 & & & & \\
\hline \multirow[t]{4}{*}{-7} & $a$ & -4 & -3 & -2 & -2 & -1 & -1 & -1 & 0 & 0 & 1 & 1 & 1 & 2 & 2 \\
\hline & $b$ & 1 & -1 & 0 & 4 & 0 & 1 & 2 & -1 & 1 & -2 & -1 & 0 & -4 & 0 \\
\hline & $a$ & 3 & 4 & \multicolumn{12}{|c|}{\multirow{2}{*}{}} \\
\hline & $b$ & 1 & -1 & & & & & & & & & & & & \\
\hline \multirow{2}{*}{-11, -19, -43, -67, -163} & $a$ & -2 & -2 & -1 & -1 & 1 & 1 & 2 & \multicolumn{7}{|l|}{2} \\
\hline & $b$ & 0 & 4 & 0 & 2 & -2 & 0 & -4 & \multicolumn{7}{|l|}{0} \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 3. Candidates for $\operatorname{div}(I)$ for irregular $I$ with index 2 and $d \equiv 1 \bmod 4$}
\end{table}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|l|}
\hline $a$ & 2 & -2 & 4 & -4 & 0 & 0 & 0 & 0 \\
\hline $b$ & 0 & 0 & 0 & 0 & 2 & -2 & 4 & -4 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 4. Candidates for $\operatorname{div}(I)$ for irregular $I$ with index 2 and $d=-2$}
\end{table}

\section*{5. Ramification divisors and canonical singularities}

Now, we consider how irregular cusps affect the geometry of $\overline{\mathscr{F}_{L}(\Gamma)}$. The essence of this section is due to [16, section 7].

Corollary 5.1. Let $I$ be a rank 1 primitive isotropic sublattice of $L$. Then, $I$ is an irregular with index $m$ if and only if the map $\overline{\mathcal{X}(I)} \rightarrow \overline{\mathcal{X}(I)} / \overline{\Gamma(I)_{\mathbb{Z}}}$ ramifies along the unique boundary divisor with ramification index $m$. Moreover, if we take the quotient $Z(I)_{\mathbb{Z}}^{\star} / Z(I)_{\mathbb{Z}}$, then $\overline{D_{L} / Z(I)_{\mathbb{Z}}^{\star}} \rightarrow \overline{\mathscr{F}_{L}(\Gamma)}$ does not ramify along the unique boundary divisor.

Proof. The first claim follows from Propositions 3.1, 3.3, 3.5, 3.7, 3.93.11 and 3.13, and the fact that the unique boundary divisor is $V(I)_{\mathbb{C}}$. The second claim follows in the same way as [16, Proposition 7,2 (2)]. \(\square\)

Remark 5.2. Note that, in the adjoint case, Ma [17] proved there is no branch divisor on the boundary of any toroidal compactification of modular varieties.

Now, let us treat the canonical singularities on the boundary divisors on ball quotients.
Proposition 5.3. If $n \geqslant 13$ and $d<-3$, then the canonical toroidal compactification $\overline{\mathscr{F}_{L}(\Gamma)}$ has canonical singularities at the boundary points.

Proof. If there is no irregular primitive isotropic sublattice $I \subset L$, then the claim follows from [2]. Otherwise, in the same way as [16, Proposition 7.4], we have
$$\overline{\left(D_{L} / Z(I)_{\mathbb{Z}}\right)} / \overline{\Gamma(I)_{\mathbb{Z}}} \cong \overline{\left(D_{L} / Z(I)_{\mathbb{Z}}^{\prime}\right)} /\left(\Gamma(I)_{\mathbb{Z}}^{\prime} / Z(I)_{\mathbb{Z}}^{\prime}\right) .$$
The claim is proved combining this with [2]. \(\square\)

\section*{6. Low slope cusp form trick}

Let $\mathscr{L}:=\left.\mathscr{O}(-1)\right|_{D_{L}}$ and $\chi$ be a character of $\Gamma$. A $\Gamma$-invariant section $\Psi$ of $\mathscr{L}^{\otimes k} \otimes \chi$ is called a modular form of weight $k$ with character $\chi$. We consider $D_{L}$ as a Siegel domain of the third kind. In our setting, for any rank 1 primitive isotropic sublattice $I \subset L$, the corresponding cusp $c_{I}$ is a point, so we will omit this in the Siegel domain of the third kind and consider $D_{L} \subset D(I)=Z(I)_{\mathbb{C}} \times V(I)_{\mathbb{C}}$. Here, $z$ and $u=\left(u_{1}, \ldots, u_{n-1}\right)$ denote the local coordinates of $Z(I)_{\mathbb{C}}$ and $V(I)_{\mathbb{C}}$, respectively. We take a nowhere vanishing section $s_{I}$ of $\mathscr{L}$ with respect to $I$ in the same way as in [16]. Then when we write $\Psi=f s_{I}^{\otimes k} \otimes 1$, the holomorphic function $f$ on $D_{L}$ satisfies the following modularity condition:
$$f(\gamma[v])=\chi(\gamma) j(\gamma,[v])^{\otimes k} f([v]) \quad\left(\gamma \in \Gamma,[v] \in D_{L}\right)$$
where $j(\gamma,[v])$ is the automorphy factor. We assume $\left.\chi\right|_{Z(I)_{\mathbb{Z}}}=1$ so that $f$ descends to a function on $D_{L} / Z(I)_{\mathbb{Z}}$. Then the Fourier expansion of $f$ is
$$f(z, u)=\sum_{\rho \in Z(I)_{\mathbb{Z}}^{\vee}} \varphi_{\rho}(u) \exp (2 \pi \sqrt{-1}\langle\rho, z\rangle) .$$

For a generator $w_{I}$ of $C(I)$, we define the vanishing order $v_{I}(\Psi)$ as
$$v_{I}(\Psi):=\min \left\{\left\langle\ell, w_{I}\right\rangle \mid \ell \in Z(I)_{\mathbb{Z}}^{\vee}, \varphi_{\rho}(\ell) \neq 0\right\} .$$
Moreover, we define the geometric vanishing order $v_{I, \text { geom }}(\Psi)$ as
$$v_{I, \text { geom }}(\Psi):= \begin{cases}v_{I}(\Psi) & (I: \text { regular }) \\ \frac{1}{m} v_{I}(\Psi) & (I:(\text { semi- }) \text { irregular with index } m) .\end{cases}$$

Then, we can give these vanishing orders a geometrical interpretation.
Proposition 6.1 ([16, Proposition 8.4, 8.5, 8.6]). (1) $v_{I}(\Psi)$ is the vanishing order of $\Psi$ over $\overline{\mathcal{X}(I)}$ along the unique boundary divisor $V(I)_{\mathbb{C}}$.
\begin{itemize}
\item[(2)] If $\left.s_{I}^{\otimes k}\right|_{Z(I)_{\mathbb{Z}}^{\star}}=1$, then $v_{I, \text { geom }}(\Psi)$ is the vanishing order of $\Psi$ over $\overline{\mathcal{X}(I)^{\prime}}$ along the unique boundary divisor $V(I)_{\mathbb{C}}^{\prime}$.
\item[(3)] $\mathscr{L}^{\otimes n+1} \otimes \operatorname{det} \cong K_{\overline{\mathcal{X}(I)^{\prime}}}+V(I)_{\mathbb{C}}^{\prime}$ over $\overline{\mathcal{X}(I)^{\prime}}$.
\end{itemize}

The vanishing orders of canonical forms are measured in $\overline{\mathscr{F}_{L}(\Gamma)}$. Now, the projection $\overline{\mathcal{X}(I)^{\prime}} \rightarrow$ $\overline{\mathscr{F}_{L}(\Gamma)}$ does not ramify, so we can measure the order of canonical forms by pulling back to $\overline{\mathcal{X}(I)^{\prime}}$, i.e., for a modular form $\Psi$ of weight $(n+1) k$ and a corresponding $k$-canonical form $\omega_{\Psi}$,
$$v_{V(I)_{\mathbb{C}}}\left(\omega_{\Psi}\right)=v_{V(I)_{\mathbb{C}}^{\prime}}\left(\pi^{\star}\left(\omega_{\Psi}\right)\right)=v_{I, \text { geom }}(\Psi)-k .$$
On the other hand, the projection $\overline{\mathcal{X}(I)} \rightarrow \overline{\mathcal{X}(I)^{\prime}}$ ramifies with index $m$ if $I$ is (semi-)irregular with index $m$ so that
$$v_{V(I)_{\mathbb{C}}}\left(\omega_{\Psi}\right)=\frac{1}{m} v_{I}(\Psi)-k .$$

Proposition 6.2. The $k$-canonical form corresponding to a modular form $\Psi$ of weight $(n+1) k$ extends holomorphically over the regular locus of $\overline{\mathscr{F}_{L}(\Gamma)}$ if and only if the following conditions hold:
\begin{itemize}
\item[(1)] $v_{R}(\Psi) \geqslant\left(r_{i}-1\right) k$ for every irreducible component $R_{i}$ of the ramification divisors $D_{L} \rightarrow \mathscr{F}_{L}(\Gamma)$ with ramification index $r_{i}$.
\item[(2)] $v_{I}(\Psi) \geqslant k$ for every regular isotropic sublattice $I \subset L$.
\item[(3)] $v_{I}(\Psi) \geqslant m_{I} k$ for every (semi-)irregular isotropic sublattice $I \subset L$ with index $m_{I}$.
\end{itemize}

Proof. To conclude the proof, combine the above discussion and [16, Corollary 8.8]. \(\square\)

Theorem 6.3 (Low slope cusp form trick). Let $F$ be an imaginary quadratic field and $L$ be a Hermitian lattice of signature $(1, n)$ over $\mathscr{O}_{F}$. For a finite index subgroup $\Gamma \subset \mathrm{U}(L)(\mathbb{Z})$, we assume that there is a non-zero cusp form $\Psi$ of weight $k$ with respect to $\Gamma$ on $D_{L}$. In addition, we make the following assumptions.
\begin{itemize}
\item[(1)] $v_{R}(\Psi) / k>\left(r_{i}-1\right) /(n+1)$ for every irreducible component $R_{i}$ of the ramification divisors $D_{L} \rightarrow \mathscr{F}_{L}(\Gamma)$ with ramification index $r_{i}$.
\item[(2)] $v_{I}(\Psi) / k>1 /(n+1)$ for every regular isotropic sublattice $I \subset L$.
\item[(3)] $v_{I}(\Psi) / k>m_{I} /(n+1)$ for every (semi-)irregular isotropic sublattice $I \subset L$ with index $m_{I}$.
\item[(4)] $n \geqslant \max _{i, I}\left\{r_{i}-2, m_{I}-1\right\}$
\item[(5)] $\overline{\mathscr{F}_{L}(\Gamma)}$ has at worst canonical singularities.
\end{itemize}
Then the ball quotient $\mathscr{F}_{L}(\Gamma)$ is of general type.
Remark 6.4. By [2, Theorem 4], assumptions (4) and (5) are satisfied if $n \geqslant 13$ and $d<-3$.
Proof. By taking some power of $\Psi$, we may assume that $\Psi$ has trivial character. Note that $r_{i}$ is at most 6 by [2, Corollary 3]. First, let us assume that $k$ is not divisible by $n+1$. Let $m:=\max _{I}\left\{m_{I}\right\} \leqslant 6$ and $r:=\max _{i}\left\{r_{i}\right\} \leqslant 6$. By taking some power of $F$, since $n \geqslant \max \{r-2, m-1\}$, we may assume that
$$\frac{k}{n+1} \geqslant\left[\frac{k}{n+1}\right]+\frac{m-1}{m}, \quad \frac{k}{n+1} \geqslant\left[\frac{k}{n+1}\right]+\frac{r-2}{r-1} .$$
Then, for every ramification divisor with ramification index $r_{i}$ and every (semi-)irregular isotropic sublattice $I$ with index $m_{I}$, we have
$$\left[\frac{m_{I} k}{n+1}\right]=m_{I}\left[\frac{k}{n+1}\right]+1, \quad\left[\frac{\left(r_{i}-1\right) k}{n+1}\right]=\left(r_{i}-1\right)\left[\frac{k}{n+1}\right]+1 .$$
Hence, for $N_{0}:=\left[\frac{k}{n+1}\right]+1$, we have
\begin{itemize}
\item[(1)] $v_{R}(\Psi) \geqslant\left(r_{i}-1\right) N_{0}$ for every irreducible component $R_{i}$ of the ramification divisors $D \rightarrow$ $\mathscr{F}_{L}(\Gamma)$ with ramification index $r_{i}$.
\item[(2)] $v_{I}(\Psi) \geqslant N_{0}$ for every regular isotropic sublattice $I \subset L$.
\item[(3)] $v_{I}(\Psi) \geqslant m_{I} N_{0}$ for every (semi-)irregular isotropic sublattice $I \subset L$ with index $m_{I}$.
\end{itemize}

Now we have
$$V_{\ell}:=\Psi^{\ell} M_{\left((n+1) N_{0}-k\right) \ell}(\Gamma) \hookrightarrow M_{(n+1) N_{0} \ell}(\Gamma) .$$
From the above discussion, any element in $V_{\ell}$ holomorphically extends the $\ell N_{0}$-canonical form over the regular locus of $\overline{\mathscr{F}_{L}(\Gamma)}$. On the other hand, Behrens [2, Theorem 4] showed the canonical singularities of $\overline{\mathscr{F}_{L}(\Gamma)}$. Combining this result and Proposition 5.3, we find that $\ell N_{0}$-canonical forms
holomorphically extend over the desingularization of $\overline{\mathscr{F}_{L}(\Gamma)}$; that is, we can calculate the Kodaira dimension of $\mathscr{F}_{L}(\Gamma)$ using some desingularization of $\mathscr{F}_{L}(\Gamma)$. By Hirzebruch's proportionality principle, the dimension of $V_{\ell}$ grows like $\ell^{n+1}$ and hence $\mathscr{F}_{L}(\Gamma)$ is of general type.

Second, we assume that $k$ is divisible by $n+1$. In this case, we can take $N_{0}$ in the above discussion to be $k /(n+1)$. \(\square\)

Remark 6.5. (1) One can construct a non-zero cusp form for $n<13$, which satisfies (1)-(4) in Theorem 6.3, by using a restriction of quasi-pull back of the Borcherds form for $F=$ $\mathbb{Q}(\sqrt{-1}), \mathbb{Q}(\sqrt{-3})$.
\begin{itemize}
\item[(2)] It is known that unitary groups of unimodular Hermitian lattices have no reflections for $F \neq \mathbb{Q}(\sqrt{-1}), \mathbb{Q}(\sqrt{-3})$ [19, 22]. Hence, if there exists a cusp form of weight less than $n+1$ which vanishes on irregular cusps with higher order, then $\mathscr{F}_{L}(\Gamma)$ is of general type in this situation.
\end{itemize}

\section*{7. A ball quotient of non-negative Kodaira dimension}

To prove that ball quotients are of general type, we need to construct a cusp form of low weight which vanishes on branch divisors with appropriate order by Theorem 6.3. For the orthogonal modular varieties case, this was done by using Borcherds lift [8, 13, 16]. For the unitary case, it seems to be difficult to construct a low slope cusp form satisfying Theorem 6.3 (5), by using unitary Borcherds lift [11] because the Borcherds form exists on a 13-dimensional ball. However, the existence of a cusp form with weaker conditions imposed implies that the Kodaira dimension is non-negative by Freitag's criterion [5]. In this section, we shall construct a cusp form of canonical weight on a ball quotient and conclude that it has non-negative Kodaira dimension. Note that in the notation of this paper, the canonical weight is $n+1$.