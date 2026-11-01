---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 2104_01933.pdf
converter: mathpix
format: mmd
---

\title{
BOUNDARY BRANCH DIVISOR OF TOROIDAL COMPACTIFICATIONS
}

\author{
SHOUHEI MA
}

\begin{abstract}
We prove that any toroidal compactification of arithmetic quotient of Hermitian symmetric domain has no boundary branch divisor, in the setting where the algebraic group is of adjoint type.
\end{abstract}

\section*{1. Introduction}

Toroidal compactification introduced by Ash-Mumford-Rapoport-Tai [1] is one of fundamental compactifications of arithmetic quotients of Hermitian symmetric domains that has various nice properties and has found many applications. The aim of this note is to prove absence of the phenomenon of "irregular cusp" in any toroidal compactification when the action of the Lie group is effective, a property that has been known for some examples but seems to have never been noticed in this generality.

We work in the setting of [1] Chapter III.5. Thus let $D$ be a Hermitian symmetric domain and $\mathbb{G}$ be a connected semi-simple linear algebraic group over $\mathbb{Q}$ such that $\mathbb{G}(\mathbb{R})^{\circ}=\operatorname{Aut}(D)^{\circ}=: G$ and $D=G / K$. Here $\mathbb{G}(\mathbb{R})$ is the group of real points of $\mathbb{G}, \circ$ in the superscript means identity component as Lie group, and $K$ is a maximal compact subgroup of $G$. In particular, $G$ acts on $D$ effectively in this setting. Thus, for example, we are considering as $G$ Lie groups like $G=\operatorname{PSL}(2, \mathbb{R}), \operatorname{PSp}(2 g, \mathbb{R}), \operatorname{PSO}(2, n)^{\circ}, \operatorname{PU}(p, q)$ etc. Let $\Gamma$ be an arithmetic subgroup of $G$. (We do not assume that $\Gamma$ is neat.)

A toroidal compactification of $D / \Gamma$, say $(D / \Gamma)^{\Sigma}$, is defined by choosing a $\Gamma$-admissible collection of fans $\Sigma=\left(\Sigma_{F}\right)$, one for each rational boundary component $F$ of $D$. If $U(F)_{\mathbb{Z}}=\Gamma \cap U(F)$ is the integral part of the center of the unipotent part of the stabilizer of $F$, the fan $\Sigma_{F}$ defines a partial compactification $D / U(F)_{\mathbb{Z}} \hookrightarrow\left(D / U(F)_{\mathbb{Z}}\right)^{\Sigma_{F}}$ in the direction of $F$ by means of relative torus embedding. (See §2.1 for more detail.) The partial compactification $\left(D / U(F)_{\mathbb{Z}}\right)^{\Sigma_{F}}$ is accessible and suitable for various kinds of analysis, not just the geometry of $\left(D / U(F)_{\mathbb{Z}}\right)^{\Sigma_{F}}$ itself, but also Fourier-Jacobi expansion of modular forms, extension of period mapping, and so on. We have the fundamental open holomorphic map $\left(D / U(F)_{\mathbb{Z}}\right)^{\Sigma_{F}} \rightarrow(D / \Gamma)^{\Sigma}$, which

\footnotetext{
2020 Mathematics Subject Classification. 14G35, 22E40, 11F99.
Supported by KAKENHI 21H00971 and 20H00112.
}
can be thought of as providing a natural local chart around the boundary points of $(D / \Gamma)^{\Sigma}$ lying over $F$, in the same sense as $D \rightarrow D / \Gamma$ providing a natural local chart for the interior points $D / \Gamma \subset(D / \Gamma)^{\Sigma}$.

We prove the following.
Theorem 1. The holomorphic map $\left(D / U(F)_{\mathbb{Z}}\right)^{\Sigma_{F}} \rightarrow(D / \Gamma)^{\Sigma}$ has no boundary divisor as a ramification divisor.

In some examples, this property has been observed individually by explicit calculation: for $\operatorname{PSp}(2 g, \mathbb{R})$ in [6] p.439, for* $\mathrm{PO}^{+}(2, n)$ in [4] Proposition 8.1 and [3] Corollaries 2.22 and 2.29, and for PU $(1, q)$ in [2] Corollary 4. We prove that this property always holds in full generality. The proof is intrinsic and uniform.

To know (absence of) boundary branch divisor is a fundamental information in the study of the geometry of $(D / \Gamma)^{\Sigma}$. For example, as the above list of papers implies, this is a necessary step in the construction of pluricanonical forms and more generally holomorphic tensors on $(D / \Gamma)^{\Sigma}$. It is also necessary when calculating the vanishing order of $\Gamma$-cusp forms along the boundary divisors of $(D / \Gamma)^{\Sigma}$ : by Theorem 1, this is equal to the vanishing order at the level of $\left(D / U(F)_{\mathbb{Z}}\right)^{\Sigma_{F}}$, which in turn is measured by the Fourier-Jacobi expansion. In particular, it is integral (as opposed to fractional).

When $\Gamma$ is neat, Theorem 1 holds evidently because $\left(D / U(F)_{\mathbb{Z}}\right)^{\Sigma_{F}} \rightarrow$ $(D / \Gamma)^{\Sigma}$ is unramified. For some applications there is no loss if one assumes $\Gamma$ neat, but this is not always the case, especially when one wants to work in the direction of nonvanishing of some invariant of $D / \Gamma$ itself, rather than of its cover.

What is essential for Theorem 1 to hold is the effectiveness of the $G$ action on $D$. In some situations, we have a natural cover $\pi: \tilde{G} \rightarrow G$, such as $\tilde{G}=\operatorname{SL}(2, \mathbb{R}), \operatorname{Sp}(2 g, \mathbb{R}), \operatorname{SO}^{+}(2, n), \operatorname{SU}(p, q)$ etc, and the arithmetic group $\Gamma$ in hand is defined as a subgroup of $\tilde{G}$. The kernel $G_{0}$ of $\tilde{G} \rightarrow G$ acts on $D$ trivially. There is one benefit in working with $\tilde{G}$, rather than with $G$ : we have more weights of modular forms available. For example, odd weights for $\tilde{G}=\operatorname{SL}(2, \mathbb{R})$. In this situation of $\Gamma \subset \tilde{G}$, if we work with $U(F) \subset \tilde{G}$, boundary branch divisor may arise. Classically this is known as irregular cusps of modular curves, and such a phenomenon also happens in higher dimension ([5]). Theorem 1 does not mean absence of boundary branch divisor in this more general situation of $\Gamma \subset \tilde{G}$. Instead, Theorem 1 leads to a classification of the boundary branch divisors for $\Gamma$ (Proposition 3). It turns out that it is the finite abelian group $G_{0} /\left(G_{0} \cap \Gamma\right)$ that is essentially responsible for the presence of such divisors. This is apparent in the case of modular curves, and we find that this is still so in the general higher

\footnotetext{
*Strictly speaking, $\mathrm{O}(2, n)$ is not connected as an algebraic group, but the construction of toroidal compactification still works.
}
dimensional case. To understand what causes boundary ramification divisor for $\Gamma \subset \tilde{G}$ is our motivation of this work. We explain this in §3.

\section*{2. Proof}

In §2.1 we recall the construction of toroidal compactification following [1]. We will basically follow the notation in [1] Chapter III. In §2.2 we prove Theorem 1.
2.1. Toroidal compactification. As in §1, let $D=G / K$ be a Hermitian symmetric domain where $G=\operatorname{Aut}(D)^{\circ}$, and $\mathbb{G}$ a connected semi-simple linear algebraic group over $\mathbb{Q}$ such that $\mathbb{G}(\mathbb{R})^{\circ}=G$. Let $F$ be a rational boundary component of $D$. We denote by $N(F)$ the stabilizer of $F$ in $G$. Let $U(F)$ be the center of the unipotent radical of the identity component $N(F)^{\circ}$ of $N(F)$. Then $U(F)$ is an $\mathbb{R}$-linear space acted on by $N(F)$ by conjugation ([1] p.158). There is an open homogeneous cone $C(F) \subset U(F)$ acted on transitively by $N(F)$, which is self-adjoint with respect to certain natural metric on $U(F)$. If $F^{\prime} \succ F$ is a rational boundary component containing $F$ in its closure, we have $U\left(F^{\prime}\right) \subset U(F)$. We write $C(F)^{*} \subset U(F)$ for the union of $C(F)$ and all $C\left(F^{\prime}\right)$ for such $F^{\prime}$. For simplicity of exposition we also count $D$ as such a boundary component $F^{\prime}$ for which $U\left(F^{\prime}\right)=\{0\}$.

We embed $D=G / K$ in its compact dual $\check{D}=G_{\mathbb{C}} / K_{\mathbb{C}} P_{-}$and let $D(F)=$ $U(F)_{\mathbb{C}} \cdot D \subset \check{D}$. We write $D(F)^{\prime}=D(F) / U(F)_{\mathbb{C}}$. Then there exists an $N(F) \cdot U(F)_{\mathbb{C}}$-equivariant two-step holomorphic fibration
$$D(F) \rightarrow D(F)^{\prime} \rightarrow F$$
and an $N(F) \cdot U(F)_{\mathbb{C}}$-equivariant map $\Phi: D(F) \rightarrow U(F)$ such that $D(F) \rightarrow$ $D(F)^{\prime}$ is a principal $U(F)_{\mathbb{C}}$-bundle and $D=\Phi^{-1}(C(F))$ ([1] Chapter III.4.3 and p.158). Here, on the target $U(F)$ of $\Phi, N(F)$ acts by conjugation and $i U(F) \subset U(F)_{\mathbb{C}}$ acts as translation by the imaginary part. This is the realization of $D$ as a Siegel domain of the third kind with respect to $F$.

Let $\Gamma$ be an arithmetic subgroup of $G$. We put $\Gamma(F)_{\mathbb{Z}}=\Gamma \cap N(F)$ and $U(F)_{\mathbb{Z}}=\Gamma \cap U(F)$. We denote by $T(F)=U(F)_{\mathbb{C}} / U(F)_{\mathbb{Z}}$ the algebraic torus associated to $U(F)_{\mathbb{Z}}$. Then $D(F) / U(F)_{\mathbb{Z}}$ is a principal $T(F)$-bundle over $D(F)^{\prime}$. The map $\Phi$ descends to $D(F) / U(F)_{\mathbb{Z}} \rightarrow U(F)$, still denoted by $\Phi$, and we have $D / U(F)_{\mathbb{Z}}=\Phi^{-1}(C(F))$ in $D(F) / U(F)_{\mathbb{Z}}$.

Let $\Sigma=\left(\Sigma_{F}\right)$ be a $\Gamma$-admissible collection of fans in the sense of [1] Definition III.5.1. Each fan $\Sigma_{F}=\left(\sigma_{\alpha}\right)$ is a rational polyhedral cone decomposition of $C(F)^{*} \subset U(F)$ preserved under the adjoint action of $\Gamma(F)_{\mathbb{Z}}$. This defines a torus embedding $T(F) \hookrightarrow T(F)^{\Sigma_{F}}$. We take the relative torus embedding
$$\left(D(F) / U(F)_{\mathbb{Z}}\right)^{\Sigma_{F}}=\left(D(F) / U(F)_{\mathbb{Z}}\right) \times_{T(F)} T(F)^{\Sigma_{F}}$$
over $D(F)^{\prime}$. Recall ([1] Chapter I.1) that the fan $\Sigma_{F}$ also defines a partial compactification $U(F)^{\Sigma_{F}}$ of $U(F)$ whose boundary is stratified into $U(F)$ -orbits $U(F) / L(\sigma), \sigma \in \Sigma_{F}$, where $L(\sigma) \subset U(F)$ is the linear span of $\sigma$. Then $\Phi$ extends continuously to
$$\Phi:\left(D(F) / U(F)_{\mathbb{Z}}\right)^{\Sigma_{F}} \rightarrow U(F)^{\Sigma_{F}} .$$

Let $\left(D / U(F)_{\mathbb{Z}}\right)^{\Sigma_{F}}$ be the interior of the closure of $D / U(F)_{\mathbb{Z}}$ in $\left(D(F) / U(F)_{\mathbb{Z}}\right)^{\Sigma_{F}}$. If $C(F)^{\prime \prime} \subset U(F)^{\Sigma_{F}}$ is the interior of the closure of $C(F)$ in $U(F)^{\Sigma_{F}}$, then ([1] p.161)
$$\left(D / U(F)_{\mathbb{Z}}\right)^{\Sigma_{F}}=\Phi^{-1}\left(C(F)^{\prime \prime}\right) \quad \subset \quad\left(D(F) / U(F)_{\mathbb{Z}}\right)^{\Sigma_{F}} .$$
The boundary of $\left(D / U(F)_{\mathbb{Z}}\right)^{\Sigma_{F}}$ is stratified into loci indexed by the cones $\sigma$ in $\Sigma_{F}$. When the relative interior of $\sigma$ is contained in $C(F)$, the boundary stratum $U(F) / L(\sigma)$ of $U(F)^{\Sigma_{F}}$ is contained in $C(F)^{\prime \prime}$, and the corresponding boundary stratum of $\left(D / U(F)_{\mathbb{Z}}\right)^{\Sigma_{F}}$ is $\Phi^{-1}(U(F) / L(\sigma))$. This is a principal bundle over $D(F)^{\prime}$ for the quotient torus of $T(F)$ associated to the quotient lattice $U(F)_{\mathbb{Z}} /\left(U(F)_{\mathbb{Z}} \cap L(\sigma)\right)$. The union of all such boundary strata of $\left(D / U(F)_{\mathbb{Z}}\right)^{\Sigma_{F}}$ is called the $F$-stratum ([1] p.164).

The toroidal compactification of $D / \Gamma$ associated to $\Sigma$ is defined by the gluing
$$(D / \Gamma)^{\Sigma}=\left(\sqcup_{F}\left(D / U(F)_{\mathbb{Z}}\right)^{\Sigma_{F}}\right) / \sim$$
where $F$ ranges over all rational boundary components of $D$ (including $D$ itself for which $U(F)$ is trivial), and ~ is the equivalence relation generated by the following maps:
\begin{itemize}
\item[-] Action of $\gamma \in \Gamma$ giving $\left(D / U(F)_{\mathbb{Z}}\right)^{\Sigma_{F}} \rightarrow\left(D / U(\gamma F)_{\mathbb{Z}}\right)^{\Sigma_{\gamma F}}$.
\item[-] Gluing map $\left(D / U\left(F^{\prime}\right)_{\mathbb{Z}}\right)^{\Sigma_{F^{\prime}}} \rightarrow\left(D / U(F)_{\mathbb{Z}}\right)^{\Sigma_{F}}$ for $F \prec F^{\prime}$.
\end{itemize}
Then $(D / \Gamma)^{\Sigma}$ is a compact Moishezon space containing $D / \Gamma$ as a Zariski open set and having a morphism to the Baily-Borel compactification of $D / \Gamma$. We have a natural open holomorphic map $\left(D / U(F)_{\mathbb{Z}}\right)^{\Sigma_{F}} \rightarrow(D / \Gamma)^{\Sigma}$. Points in the $F$-stratum of $\left(D / U(F)_{\mathbb{Z}}\right)^{\Sigma_{F}}$ are mapped to points in the image of $F$ in the Baily-Borel compactification.
2.2. Proof of Theorem 1. Now we prove Theorem 1 in four steps. We take the quotient group $\overline{\Gamma(F)_{\mathbb{Z}}}=\Gamma(F)_{\mathbb{Z}} / U(F)_{\mathbb{Z}}$, which makes sense because $U(F)_{\mathbb{Z}}$ is normal in $\Gamma(F)_{\mathbb{Z}}$. This group acts on $\left(D / U(F)_{\mathbb{Z}}\right)^{\Sigma_{F}}$ naturally. We begin with the following reduction.

Step 1. For the proof of Theorem 1 it suffices to prove the following:
If an element $\gamma \in{\overline{\Gamma(F)_{\mathbb{Z}}}}$ fixes a divisor in the boundary of $\left(D / U(F)_{\mathbb{Z}}\right)^{\Sigma_{F}}$ whose general point belongs to the $F$-stratum, then $\gamma=\mathrm{id}$.

Proof. First, for the proof of Theorem 1, it is sufficient to consider only boundary divisors whose general point belongs to the $F$-stratum. Indeed, a point in the boundary of $\left(D / U(F)_{\mathbb{Z}}\right)^{\Sigma_{F}}$ which does not belong to the $F$ -stratum is contained in the image of the gluing map
$$p_{F^{\prime}}:\left(D / U\left(F^{\prime}\right)_{\mathbb{Z}}\right)^{\Sigma_{F^{\prime}}} \rightarrow\left(D / U(F)_{\mathbb{Z}}\right)^{\Sigma_{F}}$$
for some $F^{\prime} \succ F$. The composition of $\left(D / U(F)_{\mathbb{Z}}\right)^{\Sigma_{F}} \rightarrow(D / \Gamma)^{\Sigma}$ with $p_{F^{\prime}}$ coincides with the natural map $\left(D / U\left(F^{\prime}\right)_{\mathbb{Z}}\right)^{\Sigma_{F^{\prime}}} \rightarrow(D / \Gamma)^{\Sigma}$ for $F^{\prime}$. Therefore the assertion for boundary divisors whose general point is not in the $F$ -stratum follows from the corresponding assertion for some $F^{\prime} \succ F$.

The holomorphic map $\left(D / U(F)_{\mathbb{Z}}\right)^{\Sigma_{F}} \rightarrow(D / \Gamma)^{\Sigma}$ factorizes as
$$\left(D / U(F)_{\mathbb{Z}}\right)^{\Sigma_{F}} \rightarrow\left(D / U(F)_{\mathbb{Z}}\right)^{\Sigma_{F}} / \overline{\Gamma(F)_{\mathbb{Z}}} \rightarrow(D / \Gamma)^{\Sigma} .$$
By [1] p.175, the second map $\left(D / U(F)_{\mathbb{Z}}\right)^{\Sigma_{F}} / \overline{\Gamma(F)_{\mathbb{Z}}} \rightarrow(D / \Gamma)^{\Sigma}$ is isomorphic in an open neighborhood of the $F$-stratum. This implies that Theorem 1 follows if we could show that the first map $\left(D / U(F)_{\mathbb{Z}}\right)^{\Sigma_{F}} \rightarrow$ $\left(D / U(F)_{\mathbb{Z}}\right)^{\Sigma_{F}} / \overline{\Gamma(F)_{\mathbb{Z}}}$ has no boundary divisor over $F$ as a ramification divisor. \(\square\)

Let $\gamma \in \overline{\Gamma(F)}_{\mathbb{Z}}$ and $\Delta$ be an irreducible component of the boundary divisor of $\left(D / U(F)_{\mathbb{Z}}\right)^{\Sigma_{F}}$ which is fixed by $\gamma$ and whose general point belongs to the $F$-stratum. We want to show that $\gamma=\mathrm{id}$. Note first that $\gamma$ must be of finite order because the action of $\overline{\Gamma(F)_{\mathbb{Z}}}$ on $\left(D / U(F)_{\mathbb{Z}}\right)^{\Sigma_{F}}$ is properly discontinuous ([1] Proposition III.6.10).

Step 2. The adjoint action of $\gamma$ on $U(F)$ is trivial.
Proof. The boundary divisor $\Delta$ corresponds to a ray $\sigma=\mathbb{R}_{\geq 0} v$ in $\Sigma_{F}$ whose relative interior $\mathbb{R}_{>0} v$ is contained in $C(F)$. We choose as the generator $v$ a primitive vector of $U(F)_{\mathbb{Z}}$. We shrink $\Delta$ to its Zariski open stratum so that $\Delta \rightarrow D(F)^{\prime}$ is a principal bundle for the quotient torus of $T(F)$ associated to $U(F)_{\mathbb{Z}} / \mathbb{Z} v$. Since we have a $\overline{\Gamma(F)_{\mathbb{Z}}}$-equivariant map
$$\Phi: \Delta \rightarrow U(F) / \mathbb{R} v \quad \subset U(F)^{\Sigma_{F}},$$
we see that the adjoint action of $\gamma$ on $U(F)$ preserves $\mathbb{R} v$ and acts on $U(F) / \mathbb{R} v$ trivially. Moreover, since $\gamma$ preserves the lattice $U(F)_{\mathbb{Z}}$ and the cone $C(F)$, it must fix the unique primitive integral generator $v$ of $\sigma$. Thus $\gamma$ also acts on $\mathbb{R} v$ trivially. Since $\gamma$ is of finite order, we conclude that $\gamma$ acts on $U(F)$ trivially. \(\square\)

We can also prove Step 2 by looking at the $T(F)$-action on $\Delta$, instead of looking at $\Phi$. The next step is the key step.

Step 3. There exists an element $\alpha$ of $T(F)$ of finite order such that the $\gamma$ action on $D(F) / U(F)_{\mathbb{Z}}$ coincides with the relative translation by $\alpha$ on every fiber of $\pi: D(F) / U(F)_{\mathbb{Z}} \rightarrow D(F)^{\prime}$.

Proof. Since we have a $\overline{\Gamma(F)}_{\mathbb{Z}}$-equivariant surjective map $\Delta \rightarrow D(F)^{\prime}$, we find that $\gamma$ acts on $D(F)^{\prime}$ trivially. Hence $\gamma$ preserves each fiber $\pi^{-1}(x) \simeq$ $T(F)$ of $\pi$. Let $\gamma_{x}: \pi^{-1}(x) \rightarrow \pi^{-1}(x)$ be the action of $\gamma$ on $\pi^{-1}(x)$. By Step 2, $\gamma$ commutes with every element of $U(F)_{\mathbb{C}}$. Therefore the map $\gamma_{x}$ commutes with the translation by $T(F)$ on $\pi^{-1}(x) \simeq T(F)$. This shows that $\gamma_{x}$ itself is a translation, say by $\alpha(x) \in T(F)$. Since $\alpha(x) \in T(F)$ depends continuously on $x \in D(F)^{\prime}$ and at the same time is of finite order at every $x$, we find that $\alpha(x)$ is constant for $x$. This proves our assertion. \(\square\)

Step 4. $\gamma=\mathrm{id}$.
Proof. We consider, as an auxiliary group, the normalizer of the lattice $U(F)_{\mathbb{Z}}$ in $N(F)$ and denote it by $\Gamma(F)^{*} \subset N(F)$. By definition we have $U(F)_{\mathbb{Z}} \triangleleft \Gamma(F)^{*}$. Note that $U(F)$ and $\Gamma(F)_{\mathbb{Z}}$ are contained in $\Gamma(F)^{*}$. We put $\overline{\Gamma(F)_{\mathbb{R}}}=\Gamma(F)^{*} / U(F)_{\mathbb{Z}}$. Then $U(F) / U(F)_{\mathbb{Z}}$ and $\overline{\Gamma(F)_{\mathbb{Z}}}$ are subgroups of $\overline{\Gamma(F)_{\mathbb{R}}}$, and we have
$$\left(U(F) / U(F)_{\mathbb{Z}}\right) \cap \overline{\Gamma(F)}_{\mathbb{Z}}=\{\operatorname{id}\}$$
in $\overline{\Gamma(F)_{\mathbb{R}}}$ by the definition $U(F)_{\mathbb{Z}}=U(F) \cap \Gamma(F)_{\mathbb{Z}}$ of $U(F)_{\mathbb{Z}}$.
The group $\overline{\Gamma(F)_{\mathbb{R}}}$ acts on $D(F) / U(F)_{\mathbb{Z}}$. Since $N(F)$ acts on $D(F)$ effectively by our initial setting, and since $U(F)_{\mathbb{Z}}$ is discrete and acts on $D(F)$ freely, we see that the action of $\overline{\Gamma(F)_{\mathbb{R}}}$ on $D(F) / U(F)_{\mathbb{Z}}$ is also effective. By Step 3, we know that the elements $\gamma \in \overline{\Gamma(F)_{\mathbb{Z}}}$ and $\alpha \in U(F) / U(F)_{\mathbb{Z}}$ have the same action on $D(F) / U(F)_{\mathbb{Z}}$. Therefore we find that $\gamma=\alpha$ as elements of $\overline{\Gamma(F)_{\mathbb{R}}}$ by the effectivity of the action. By (2.2), we conclude that $\gamma=\mathrm{id}$. This completes the proof of Theorem 1. \(\square\)

\section*{3. Covering group}

In this section we consider the more general case where $\Gamma$ is defined as a subgroup of a covering group of $\operatorname{Aut}(D)^{\circ}$. Theorem 1 leads to a classification of the boundary branch divisors of $(D / \Gamma)^{\Sigma}$ in this situation (Proposition (3).
3.1. Toroidal compactification with sublattices. In this subsection, which is the preliminary for the next §3.2, we work in the setting of §2.1. Thus $\Gamma$ is an arithmetic subgroup of $G=\operatorname{Aut}(D)^{\circ}$. Suppose that a finiteindex sublattice $U(F)_{\mathbb{Z}}^{+} \subset U(F)_{\mathbb{Z}}$ is given for each rational boundary component $F$, satisfying the following conditions:
\begin{itemize}
\item[-] $U\left(F^{\prime}\right)_{\mathbb{Z}}^{+}=U\left(F^{\prime}\right) \cap U(F)_{\mathbb{Z}}^{+}$when $F^{\prime} \succ F$.
\end{itemize}
\begin{itemize}
\item[-] $U(\gamma F)_{\mathbb{Z}}^{+}=\gamma U(F)_{\mathbb{Z}}^{+} \gamma^{-1}$ for $\gamma \in \Gamma$. In particular, $U(F)_{\mathbb{Z}}^{+}$is preserved under the adjoint action of $\Gamma(F)_{\mathbb{Z}}$ on $U(F)_{\mathbb{Z}}$.
\end{itemize}

Let $A_{F}=U(F)_{\mathbb{Z}} / U(F)_{\mathbb{Z}}^{+}$and $T(F)_{+}=U(F)_{\mathbb{C}} / U(F)_{\mathbb{Z}}^{+}$. Since the fan $\Sigma_{F}$ is also rational with respect to $U(F)_{\mathbb{Z}}^{+}$, it defines a torus embedding $T(F)_{+}^{\Sigma_{F}}$ of $T(F)_{+}$, and we have $T(F)^{\Sigma_{F}}=T(F)_{+}^{\Sigma_{F}} / A_{F}$. This defines the partial compactification $\left(D / U(F)_{\mathbb{Z}}^{+}\right)^{\Sigma_{F}}$ of $D / U(F)_{\mathbb{Z}}^{+}$. Working with $U(F)_{\mathbb{Z}}^{+}$in place of $U(F)_{\mathbb{Z}}$, we can define the toroidal compactification of $D / \Gamma$ with $\left(U(F)_{\mathbb{Z}}^{+}\right)_{F}$ by the same gluing procedure as (2.1), covered by the partial compactifications $\left(D / U(F)_{\mathbb{Z}}^{+}\right)^{\Sigma_{F}}$. The result is still naturally isomorphic to the usual $(D / \Gamma)^{\Sigma}$ with $\left(U(F)_{\mathbb{Z}}\right)_{F}$, as can be seen from the fact that the natural map between their local models around the $F$-stratum
$$\left(D / U(F)_{\mathbb{Z}}^{+}\right)^{\Sigma_{F}} /\left(\Gamma(F)_{\mathbb{Z}} / U(F)_{\mathbb{Z}}^{+}\right) \rightarrow\left(D / U(F)_{\mathbb{Z}}\right)^{\Sigma_{F}} / \overline{\Gamma(F)_{\mathbb{Z}}}$$
is isomorphic. Here note that $\left(D / U(F)_{\mathbb{Z}}^{+}\right)^{\Sigma_{F}} / A_{F}=\left(D / U(F)_{\mathbb{Z}}\right)^{\Sigma_{F}}$.
Lemma 2. Let $\Delta$ be a boundary divisor of $\left(D / U(F)_{\mathbb{Z}}^{+}\right)^{\Sigma_{F}}$ corresponding to a ray $\sigma$ of $\Sigma_{F}$. The map $\left(D / U(F)_{\mathbb{Z}}^{+}\right)^{\Sigma_{F}} \rightarrow(D / \Gamma)^{\Sigma}$ is ramified along $\Delta$ if and only if $\sigma \cap U(F)_{\mathbb{Z}} \neq \sigma \cap U(F)_{\mathbb{Z}}^{+}$, with the ramification caused by the cyclic subgroup $\left(\mathbb{R} \sigma \cap U(F)_{\mathbb{Z}}\right) /\left(\mathbb{R} \sigma \cap U(F)_{\mathbb{Z}}^{+}\right)$of $A_{F}$.

Proof. Since $\left(D / U(F)_{\mathbb{Z}}^{+}\right)^{\Sigma_{F}} \rightarrow(D / \Gamma)^{\Sigma}$ factorizes as
$$\left(D / U(F)_{\mathbb{Z}}^{+}\right)^{\Sigma_{F}} \rightarrow\left(D / U(F)_{\mathbb{Z}}\right)^{\Sigma_{F}} \rightarrow(D / \Gamma)^{\Sigma},$$
Theorem 1 shows that the boundary ramification divisors of the map $\left(D / U(F)_{\mathbb{Z}}^{+}\right)^{\Sigma_{F}} \rightarrow(D / \Gamma)^{\Sigma}$ are the same as those of $\left(D / U(F)_{\mathbb{Z}}^{+}\right)^{\Sigma_{F}} \rightarrow$ $\left(D / U(F)_{\mathbb{Z}}\right)^{\Sigma_{F}}$, which in turn correspond to those of $T(F)_{+}^{\Sigma_{F}} \rightarrow T(F)^{\Sigma_{F}}$. \(\square\)
3.2. Effect of ineffective kernel. Let $G=\mathbb{G}(\mathbb{R})^{\circ}=\operatorname{Aut}(D)^{\circ}$ be as in §2.1. Let $\pi: \tilde{G} \rightarrow G$ be a finite covering of Lie groups. $\tilde{G}$ is a connected Lie group, not assumed to be associated to an algebraic group over $\mathbb{Q}$. The kernel $G_{0}=\operatorname{Ker}(\pi)$ of $\pi$ is the center of $\tilde{G}$, and $\tilde{G}$ acts on $D$ with ineffective kernel $G_{0}$. For $U(F) \subset G$ we denote by $U(F)^{+} \subset \tilde{G}$ the identity component of $\pi^{-1}(U(F))$. Then $U(F)^{+} \rightarrow U(F)$ is isomorphic and $\pi^{-1}(U(F))=U(F)^{+} \times G_{0} . U(F)^{+}$is what we should write " $U(F)$ " for $\tilde{G}$.

Let now $\Gamma$ be an arithmetic subgroup of $\tilde{G}$, namely $\pi(\Gamma) \subset G$ arithmetic. We write $U(F)_{\mathbb{Z}}=\Gamma \cap U(F)^{+}$and $U(F)_{\mathbb{Z}}^{\prime}=\Gamma \cap \pi^{-1}(U(F))$. We have
$$U(F)_{\mathbb{Z}} \subset U(F)_{\mathbb{Z}} \times\left(G_{0} \cap \Gamma\right) \subset U(F)_{\mathbb{Z}}^{\prime} .$$
Note that $\pi\left(U(F)_{\mathbb{Z}}^{\prime}\right) \subset G$ is what we previously wrote " $U(F)_{\mathbb{Z}}$ " for $\pi(\Gamma) \subset$ $G$. (We want to stick to the notation $U(F)_{\mathbb{Z}}$ for the lattice of unipotent elements in the given arithmetic group $\Gamma$.) It is necessary to work with $\Gamma \subset \tilde{G}$, rather than with $\pi(\Gamma) \subset G$, when considering modular forms of
(say) odd weight. We must work with $U(F)_{\mathbb{Z}} \subset U(F)^{+}$, rather than with $U(F)_{\mathbb{Z}}^{\prime}$, when considering Fourier-Jacobi expansion of such modular forms.

Let $\Sigma=\left(\Sigma_{F}\right)$ be a $\Gamma$-admissible collection of fans, where each $\Sigma_{F}$ is a fan in $U(F)^{+} \simeq U(F)$. It is possible to construct the toroidal compactification $(D / \Gamma)^{\Sigma}$ of $D / \Gamma$ with the lattices $U(F)_{\mathbb{Z}} \subset U(F)^{+}$. This is the same as the toroidal compactification of $D / \pi(\Gamma)$ with the sublattices $\left(\pi\left(U(F)_{\mathbb{Z}}\right)\right)_{F}$ of $\left(\pi\left(U(F)_{\mathbb{Z}}^{\prime}\right)\right)_{F}$, hence with $\left(\pi\left(U(F)_{\mathbb{Z}}^{\prime}\right)\right)_{F}$, which satisfies the conditions in §3.1.

Proposition 3. For $\Gamma \subset \tilde{G}$ the natural map $\left(D / U(F)_{\mathbb{Z}}\right)^{\Sigma_{F}} \rightarrow(D / \Gamma)^{\Sigma}$ is ramified along a boundary divisor corresponding to a ray $\sigma \in \Sigma_{F}$ if and only if $\sigma \cap \pi\left(U(F)_{\mathbb{Z}}\right) \neq \sigma \cap \pi\left(U(F)_{\mathbb{Z}}^{\prime}\right)$, with the ramification caused by the cyclic subgroup $\left(\mathbb{R} \sigma \cap \pi\left(U(F)_{\mathbb{Z}}^{\prime}\right)\right) /\left(\mathbb{R} \sigma \cap \pi\left(U(F)_{\mathbb{Z}}\right)\right)$ of $G_{0} /\left(G_{0} \cap \Gamma\right)$.

Proof. This follows from Lemma 2. Note that
$$\pi\left(U(F)_{\mathbb{Z}}^{\prime}\right) / \pi\left(U(F)_{\mathbb{Z}}\right) \simeq U(F)_{\mathbb{Z}}^{\prime} /\left(U(F)_{\mathbb{Z}} \times\left(G_{0} \cap \Gamma\right)\right)$$
is naturally a subgroup of $G_{0} /\left(G_{0} \cap \Gamma\right)$. \(\square\)

The analogy with the case of modular curves would justify the following terminology.

Definition 4. We call a cusp $F$ irregular when $\pi\left(U(F)_{\mathbb{Z}}^{\prime}\right) \neq \pi\left(U(F)_{\mathbb{Z}}\right)$, or equivalently, $U(F)_{\mathbb{Z}}^{\prime} \neq U(F)_{\mathbb{Z}} \times\left(G_{0} \cap \Gamma\right)$.

By Proposition 3, boundary branch divisor may arise over $F$ only when $F$ is irregular. It is evident that, if $F$ is regular, any $F^{\prime} \succ F$ is also regular. It is also clear that, if $\Gamma$ is neat (with $\tilde{G}$ associated to an algebraic group over $\mathbb{Q}$ ), every cusp $F$ is regular because $U(F)_{\mathbb{Z}}^{\prime}=U(F)_{\mathbb{Z}}$.

\section*{References}
\begin{itemize}
\item[] [1] Ash, A.; Mumford, D.; Rapoport, M.; Tai, Y. Smooth compactifications of locally symmetric varieties. 2nd edition. Cambridge Univ. Press, 2010.
\item[] [2] Behrens, N. Singularities of ball quotients. Geom. Dedicata 159 (2012), 389-407.
\item[] [3] Gritsenko, V.; Hulek, K.; Sankaran, G. The Kodaira dimension of the moduli of K3 surfaces. Invent. Math. 169 (2007), 519-567.
\item[] [4] Kondō, S. On the Kodaira dimension of the moduli space of K3 surfaces. Compositio Math. 89 (1993), 251-299.
\item[] [5] Ma, S. Irregular cusps of orthogonal modular varieties. arXiv:2101.02950
\item[] [6] Tai, Y. On the Kodaira dimension of the moduli space of Abelian varieties. Invent. Math. 68 (1982), 425-439.
\end{itemize}