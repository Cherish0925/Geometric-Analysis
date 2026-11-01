---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 2505_09550.pdf
converter: mathpix
format: mmd
---

\title{
Cohomologous symplectic forms with different Gromov widths
}

\author{
Shengzhen Ning
}

\begin{abstract}
We study McDuff-Salamon's Problem 46 in [MS17] by showing that there exist closed manifolds of dimension $\geq 6$ admitting cohomologous symplectic forms with different Gromov widths. The examples are motivated by Ruan's early example ([Rua94]) of deformation inequivalent symplectic forms in dimension 6 distinguished by Gromov-Witten invariants. To find cohomologous symplectic forms and compare their Gromov width, we make use of Li-Liu's theorem of symplectic cone for manifolds with $b_{2}^{+}=1$ and Biran's ball packing theorem in dimension 4. Along the way, we also show that these cohomologous symplectic forms can have distinct first Chern classes, which answers another question by Salamon in [Sal13].
\end{abstract}

\section*{1 Introduction}

The Gromov width of a $2 n$-dimensional symplectic manifold $(M, \omega)$ is defined by
$$w_{G}(M, \omega)=\sup \left\{\pi r^{2} \mid B^{2 n}(r) \text { can be symplectically embedded into }(M, \omega)\right\},$$
where $B^{2 n}(r)$ denotes the open ball in $\mathbb{R}^{2 n}$ of radius $r$ equipped with the standard symplectic form $\sum_{i=1}^{n} d x_{i} \wedge d y_{i}$. Problem 46 in the open problem chapter of [MS17] asks the following.

Problem 1.1. Is there a closed manifold $M$ with cohomologous symplectic forms $\omega_{0}, \omega_{1}$ such that $\left(M, \omega_{0}\right)$ and $\left(M, \omega_{1}\right)$ have different Gromov widths?

Another problem related to cohomologous symplectic forms on a fixed closed manifold, raised in [Sal13], concerns their first Chern classes. In dimension 4, it is a consequence of Seiberg-Witten theory that cohomologous symplectic forms must have the same first Chern class ([Sal13, Corollary A]). In higher dimensions, one can ask the following question.

Problem 1.2 ([Sal13] Discussion 4.6). Do cohomologous symplectic forms on a closed manifold of dimension $\geq 6$ always have the same first Chern class?

The aim of this note is to provide examples to both of the above problems in dimension $\geq 6$.

Theorem 1.3. Let $X$ be any symplectic 4-manifold homeomorphic but not diffeomorphic to the rational manifold $\mathbb{C P}^{2} \# k \overline{\mathbb{C P}^{2}}$ with $k \geq 1$. Then there exists some symplectic form $\omega_{X}$ on $X$ and $\omega_{S^{2}}$ on $S^{2}$ such that the 6-manifold $M:=X \times S^{2}$ admits symplectic form cohomologous to the product symplectic form $\omega_{X} \oplus \omega_{S^{2}}$ but with smaller Gromov width. Moreover, the first Chern classes of these cohomologous symplectic forms are different.

Symplectic 4-manifolds $X$ satisfying the conditions in Theorem 1.3 are quite abundant in the realm of exotic 4-manifolds, even under the minimality assumption. For example, see [Kot89] for $k=8$, [Par05] for $k=7$, [SS05] for $k=6$, [PSS05] for $k=5$, [RU25] for $k=4$, [AP08, BK08] for $k=3$ and [AP10] for $k=2$. Note that $k=2$ is the current world record for smallest $k$. We thus have the following immediate corollary.

Corollary 1.4. For any $k \geq 2$, the smooth 6-manifold $M:=\left(\mathbb{C P}^{2} \# k \overline{\mathbb{C P}^{2}}\right) \times S^{2}$ admits cohomologous symplectic forms with different Gromov widths and different first Chern classes.

As we will see in the proof, based on the examples in Theorem 1.3, it is easy to construct cohomologous symplectic forms with different Gromov widths and Chern classes in any dimension $\geq 6$.

For Problem 1.2, the examples in Theorem 1.3 are not the only candidates. Indeed, $K 3 \times S^{2}$ also works. One can use various symplectic homotopy K3 surfaces such as the ones constructed in [Gom95, FS98, Vid01], which have non-vanishing first Chern classes. The knot surgery manifolds $E(n)_{K}$ of the elliptic surface $E(n)$ have been investigated in [IP99]. They showed that, for two fibered knots $K, K^{\prime}$ with the same genus, the diffeomorphic 6-manifolds $E(n)_{K} \times S^{2}$ and $E(n)_{K^{\prime}} \times S^{2}$ can have deformation inequivalent cohomologous symplectic forms with the same first Chern class. This was later generalized in [Her02] into the $S^{2}$-bundle settings. Rather than comparing symplectic forms coming from different knots $K, K^{\prime}$ as [IP99], one can actually directly compare the symplectic form constructed from $E(2)_{K} \times S^{2}$ directly with the product symplectic form on $K 3 \times S^{2}$. See the discussion after the proof of Theorem 1.3 in the last section.

\section*{Acknowledgement}

The author would like to thank his advisor Tian-Jun Li for helpful discussions and comments during the preparation of this manuscript.

\section*{2 Dimension 4}

\subsection*{2.1 Exceptional classes and minimal models}

For a symplectic 4-manifold $(X, \omega)$, let $\mathcal{E}_{X}$ (resp. $\mathcal{E}_{\omega}$ ) be the set of classes in $H_{2}(X ; \mathbb{Z})$ which can be represented by smoothly (resp. symplectically) embedded sphere of self-intersection -1. A deep result coming from Taubes-Seiberg-Witten theory is that $\mathcal{E}_{X}$ is empty if and only if $\mathcal{E}_{\omega}$ is empty ([Tau96], [LL95], [Li99]). In this case, $(X, \omega)$ is said to be minimal.

Assume $(X, \omega)$ is minimal and not diffeomorphic to a rational or ruled manifold. By the symplectic blowup construction, the smooth manifold $\tilde{X}:=X \# l \overline{\mathbb{C P}^{2}}$ also admits symplectic forms. Let $\tilde{\omega}$ be any symplectic form on $\tilde{X}$. In general, it is unknown whether $\tilde{\omega}$ is symplectomorphic to a symplectic form coming from the symplectic blowup construction. However, by [Li99, Corollary 3], we always have
$$\mathcal{E}_{\tilde{\omega}}=\left\{E_{1}, \cdots, E_{l}\right\}, \mathcal{E}_{\tilde{X}}=\left\{ \pm E_{1}, \cdots, \pm E_{l}\right\}$$
where $E_{i}$ 's are the line classes in those $l \mathbb{C P}^{2}$. In particular, $E_{i} \cdot E_{j}=0$ for any $i \neq j$. By standard pseudoholomorphic curve technique, the classes in $\mathcal{E}_{\tilde{\omega}}$ can be represented by disjoint embedded $J$-holomorphic exceptional spheres for generic $\tilde{\omega}$-tame almost complex structure $J$. Moreover, the space of the symplectic representatives of any class in $\mathcal{E}_{\tilde{\omega}}$ is connected. By performing symplectic blowdown operations on those exceptional spheres, one can obtain the minimal model for $(\tilde{X}, \tilde{\omega})$. Indeed, (1) is closely related to the uniqueness of minimal models for symplectic 4-manifolds not diffeomorphic to rational or ruled manifolds.

Theorem 2.1 ([McD90, McD92]). Any symplectic 4-manifold has a minimal model. When $X$ is not diffeomorphic to rational or ruled manifolds, the symplectomorphism type of the minimal model is unique.

Note that the minimal model depends on the choice of the symplectic form on the non-minimal manifold. As pointed out in [MS17, Example 13.4.5], unless the manifold is rational or ruled, different choice of symplectic forms might even potentially result in non-diffeomorphic manifolds after blowdown. This is because in general, it is unknown whether the diffeomorphism group acts transitively on the space of smoothly embedded exceptional spheres.

\subsection*{2.2 Li-Liu's result of symplectic cones of 4-manifolds with $b_{2}^{+}=1$}

Now, we review the result from [LL01]. For an oriented closed smooth 4-manifold $X$ admitting symplectic structures, introduce the set consisting all the possible symplectic canonical classes
$$\mathcal{K}_{X}:=\left\{K_{\omega} \mid \omega \text { is a symplectic form on } X\right\} \subseteq H^{2}(X ; \mathbb{Z}) .$$
For any $K \in \mathcal{K}_{X}$, consider the $K$-symplectic cone
$$\mathcal{C}_{K}:=\left\{[\omega] \mid \omega \text { is a symplectic form on } X \text { and } K_{\omega}=K\right\} \subseteq H^{2}(X ; \mathbb{R}),$$
and the set of $K$-exceptional classes
$$\mathcal{E}_{K}:=\left\{E \in \mathcal{E}_{X} \mid E \cdot K=-1\right\} .$$
When $b_{2}^{+}(X)=1$, the positive cone
$$\mathcal{P}:=\left\{a \in H^{2}(X ; \mathbb{R}) \mid a^{2}>0\right\} \subseteq H^{2}(X ; \mathbb{R})$$
will contain two connected components. When some $K \in \mathcal{K}_{X}$ is chosen, the connected component of $\mathcal{P}$ containing $\mathcal{C}_{K}$ will be called the forward cone associated to $K$. We denote it by $\mathcal{F} \mathcal{P}(K)$.
Theorem 2.2 ([LL01]). If $b_{2}^{+}(X)=1$ and $\mathcal{K}_{X} \neq \emptyset$, then
$$\mathcal{C}_{K}=\left\{a \in \mathcal{F} \mathcal{P}(K) \mid a \cdot E>0 \text { for any } E \in \mathcal{E}_{K}\right\} .$$

In particular, when $X$ is minimal and $a \in H^{2}(X ; \mathbb{R})$ satisfies $a^{2}>0$, we have $a \in \mathcal{C}_{K} \cup \mathcal{C}_{-K}$ for some ${ }^{1} K \in \mathcal{K}_{X}$. When $X$ is not minimal with $\mathcal{E}_{X}=\left\{ \pm E_{1}, \cdots, \pm E_{l}\right\}$ and not diffeomorphic to rational or ruled manifolds, by Theorem 2.1, we can obtain its unique minimal model $\hat{X}$ by blowing down the exceptional spheres of the classes in $\mathcal{E}_{X}$. Choose any $K_{\hat{X}} \in \mathcal{K}_{\hat{X}}$ so that both $K_{+}:=K_{\hat{X}}+\sum \operatorname{PD}\left(E_{i}\right)$ and $K_{-}:=$ $-K_{\hat{X}}+\sum \operatorname{PD}\left(E_{i}\right)$ are in $\mathcal{K}_{X}$. Assume $a \in H^{2}(X ; \mathbb{R})$ satisfies $a^{2}>0$ and $a \cdot E_{i}>0$ for all $1 \leq i \leq l$. Then it follows from the light cone lemma that $a \in \mathcal{C}_{K_{+}} \cup \mathcal{C}_{K_{-}}$.

\subsection*{2.3 Biran's result of symplectic ball packings in dimension 4}

Now, we review the result from [Bir97], based on the pioneer work [MP94]. Recall that a symplectic 4-manifold $(X, \omega)$ is said to have SW-simple type if its only nonzero Gromov invariants occur in classes $A \in H_{2}(X ; \mathbb{Z})$ for which $A^{2}-K_{\omega} \cdot A=0$. It is known (see [McD98]) that the operation of blowup will preserve the property of being not of SW-simple type. Moreover, in the following situations, $X$ is not of SW-simple type:

\footnotetext{
${ }^{1}$ Actually, [LL01] also showed that $K$ is unique up to sign for minimal manifolds.
}
\begin{itemize}
\item[-] $X$ is diffeomorphic to rational or ruled manifolds;
\item[-] $b_{1}(X)=0$ and $b_{2}^{+}(X)=1$;
\item[-] $b_{1}(X)=2$ and $\left(H^{1}(X)\right)^{2} \neq 0$.
\end{itemize}

Let $(\tilde{X}, \tilde{\omega})$ be some one-point symplectic blowup of $(X, \omega)$ and
$$p r: H_{2}(\tilde{X} ; \mathbb{Z}) \rightarrow H_{2}(X ; \mathbb{Z})$$
be the natural projection map. Consider the set
$$\mathcal{E}_{\omega}^{\prime}:=\operatorname{pr}\left(\mathcal{E}_{\tilde{\omega}}\right) \backslash\{0\} \subseteq H_{2}(X ; \mathbb{Z})$$
and the value
$$d_{\omega}^{\prime}:=\inf _{B \in \mathcal{E}_{\omega}^{\prime}} \frac{\omega(B)}{c_{1}(B)-1} \in[0, \infty],$$
where the convention $\inf \emptyset=\infty$ is used. Biran's packing result in the special case of one ball can then be stated as the following.

Theorem 2.3 ([Bir97]). ${ }^{2}$ If $(X, \omega)$ is a symplectic 4-manifold which is not of SW-simple type. Then $w_{G}(X, \omega)=\min \left\{\sqrt{[\omega]^{2}}, d_{\omega}^{\prime}\right\}$.

When $X$ is further assumed to be not diffeomorphic to rational or ruled manifolds, (1) tells us the set $\mathcal{E}_{\omega}^{\prime}$ must be either empty (when $X$ is minimal) or only contain exceptional classes $E$ in $\mathcal{E}_{\omega}$ which all have $c_{1}(E)=1$. Therefore, $d_{\omega}^{\prime}=\infty$ in this case and we actually have the following corollary.

Corollary 2.4. Let $(X, \omega)$ be a symplectic 4-manifold which is not of $S W$-simple type and not diffeomorphic to rational or ruled manifolds. Then $w_{G}(X, \omega)=\sqrt{[\omega]^{2}}$.

Remark 2.5. [Bir97, Theorem 2.F] already points out that if $X$ is minimal, not of $S W$-simple type and not diffeomorphic to rational or ruled manifolds, then $(X, \omega)$ admits a full packing by one ball. As shown above, the minimality assumption can actually be removed in the non-rational or ruled cases by the observation (1). This observation is also used in [LL01] to establish Theorem 2.2.

Remark 2.6. Note that cohomologous symplectic forms on rational or ruled manifolds are symplectomorphic (LLi08, Theorem 3.18]) and thus have the same Gromov width. Therefore, Corollary 2.4 also implies that the candidates of closed 4-manifolds admitting cohomologous symplectic forms with different Gromov widths must have SW-simple type (such as K3, $T^{4}$ ).

\footnotetext{
${ }^{2}$ This is Theorem 6.A in the published version of [Bir97]. The arXiv version does not have section 6.
}

\subsection*{2.4 Uniruled symplectic manifolds}

Definition 2.7. For semipositive symplectic manifold $(X, \omega)$, a non-zero class $A \in$ $H_{2}(X ; \mathbb{Z})$ is called a uniruled class if there is a non-trivial genus zero Gromov-Witten invariant with a point insertion
$$G W_{A, k}^{X}\left(P D(p t), a_{2}, \cdots, a_{k}\right) \neq 0 .$$
$(M, \omega)$ is said to be symplectically uniruled if there exists a uniruled class.
The following celebrated result goes back to [Gro85].
Theorem 2.8 (Gromov). For any uniruled class $A, w_{G}(X, \omega) \leq \omega(A)$.
In dimension 4, by the fundamental work [McD90], it is well known ([Wen18, Theorem 7.3]) that the characterization of symplectic uniruledness is equivalent to the underlying smooth 4-manifold $X$ being rational or ruled manifolds. Namely, $X$ must be diffeomorphic to the blowup of $\mathbb{C P}^{2}$ or $S^{2}$-bundle over Riemann surface. Moreover, when $X \neq \mathbb{C P}^{2}$, the uniruled class $A$ can be chosen to be the 'fiber class' in the sense that $A$ can be represented by a symplectically embedded sphere of self-intersection zero. The following statement will be used for the upper bound of Gromov width.

Proposition 2.9. Let $(X, \omega)$ be a symplectic rational manifold where $X=\mathbb{C P}^{2} \# k \overline{\mathbb{C P}^{2}}$. Then there always exists a uniruled class $A \in H_{2}(X ; \mathbb{Z})$ satisfying $A^{2}=0$ such that
\begin{itemize}
\item[-] when $1 \leq k \leq 4, \omega(A)<\sqrt{[\omega]^{2}}$;
\item[-] when $k \geq 5$, there exists another symplectic form $\omega^{\prime}$ deformation equivalent to $\omega$ satisfying $\omega^{\prime}(A)<\sqrt{\left[\omega^{\prime}\right]^{2}}$ and $\left[\omega^{\prime}\right] \cdot K_{\omega^{\prime}}<0^{3}$.
\end{itemize}

Proof. Choose the standard basis $\left\{H, E_{1}, \cdots, E_{k}\right\} \subseteq H_{2}(X ; \mathbb{Z})$, where $H^{2}=1$ and all $E_{i}^{2}=-1$. Let $a=\omega(H)$ and $b_{i}=\omega\left(E_{i}\right)$. By the main result in KK17, we may assume the period of $\omega$ satisfies the reduced condition ${ }^{4}$ :
$$a \geq b_{1}+b_{2}+b_{3}, \quad b_{1} \geq b_{2} \geq \cdots \geq b_{k}>0 .$$
In this case, the canonical class $K_{\omega}=\mathrm{PD}\left(-3 H+\sum E_{i}\right)$. Then we can take the fiber class $H-E_{1}$ to be the uniruled class $A$ and compute
$$[\omega]^{2}-(\omega(A))^{2}=a^{2}-\sum_{i=1}^{k} b_{i}^{2}-\left(a-b_{1}\right)^{2}=2 b_{1}\left(1-b_{1}\right)-\sum_{i=2}^{k} b_{i}^{2} \geq 2 b_{1}\left(b_{2}+b_{3}\right)-\sum_{i=2}^{k} b_{i}^{2} .$$

\footnotetext{
${ }^{3}$ This automatically holds when $k \leq 9$ by light cone lemma.
${ }^{4}$ When $k=1,2$, the first equality is $a \geq b_{1}$ or $a \geq b_{1}+b_{2}$.
}

It is clear that if $k \leq 4,2 b_{1}\left(b_{2}+b_{3}\right)-\sum_{i=2}^{k} b_{i}^{2}$ will be positive by the reduced condition. If $k \geq 5$, in order to guarantee the positivity, we just need to deform the values of $b_{5}, \cdots, b_{k}$ so that they are as small as possible. This can always be realized by a symplectic deformation equivalence by [Sal13, Example 3.9+3.10]. Moreover, when $b_{5}, \cdots, b_{k}$ are very small, it also follows from the reduced condition that
$$\left[\omega^{\prime}\right] \cdot K_{\omega^{\prime}}=-3 a+b_{1}+b_{2}+b_{3}+b_{4}+\sum_{i \geq 5} b_{i}<0 .$$ \(\square\)

Finally, we need the fact that the uniruled class can be lifted after taking the product with some symplectic $\left(S^{2}, \omega_{S^{2}}\right)$. Indeed, [LR13] investigates when the existence of uniruled symplectic submanifolds with codimension 2 implies the uniruledness of the ambient manifold. The following proposition is a very simple case. For example, see [LR13, Proposition 2.10].

Proposition 2.10. Let $A \in H_{2}(X ; \mathbb{Z})$ be a uniruled class of $(X, \omega)$. Then, under the natural inclusion $H_{2}(X ; \mathbb{Z}) \subseteq H_{2}\left(X \times S^{2} ; \mathbb{Z}\right)$, $A$ is also a uniruled class for $(X \times$ $\left.S^{2}, \omega \oplus \omega_{S^{2}}\right)$.

Remark 2.11. The obstruction coming from 'stabilized' J-holomoprhic curves for symplectic embeddings was also used in the recent work [SY23]. For any Riemann surface $\Sigma$, the problem of embedding $\sqcup B^{4}\left(R_{i}\right) \times \Sigma \hookrightarrow B^{4}(R) \times \Sigma$ was considered there.

\section*{3 Dimension 6}

From now on, $(X, \omega)$ and $\left(X^{\prime}, \omega^{\prime}\right)$ will be two simply-connected closed symplectic 4-manifolds which are homeomorphic to each other. By Wall's result [Wal64], $X$ and $X^{\prime}$ are $h$-cobordant and so are $X \times S^{2}$ and $X^{\prime} \times S^{2}$. Then Smale's $h$-cobordism theorem [Sma62] implies that there will be an orientation-preserving diffeomorphism between $X \times S^{2}$ and $X^{\prime} \times S^{2}$. For our purpose of choosing cohomologous symplectic forms, we still need to keep track of the cohomological action of the diffeomorphism. The following classification result tells us that the category of torsion-free simply-connected smooth 6-manifolds are equivalent to the category of cohomology rings with certain compatible characteristic classes. See also [Rua94].

Theorem 3.1 (Jup73)). Two closed simply-connected oriented smooth 6-manifolds $M, N$ with torsion-free homology are oriented diffeomorphic if and only if there is an algebraic isomorphism $\Phi: H^{*}(M ; \mathbb{Z}) \rightarrow H^{*}(N ; \mathbb{Z})$ which preserves the cup product
$\mu: H^{2} \otimes H^{2} \otimes H^{2} \rightarrow \mathbb{Z}$, second Stiefel-Whitney class $w_{2}$ and first Pontryagin class $p_{1}$. Furthermore, the diffeomorphism can be chosen to realize this algebraic isomorphism $\Phi$.

We will apply the above theorem for $M=X \times S^{2}, N=X^{\prime} \times S^{2}$. Note that (similarly for $X^{\prime} \times S^{2}$ )
$$\begin{gathered}
H^{2}\left(X \times S^{2} ; \mathbb{Z}\right)=H^{2}(X ; \mathbb{Z}) \oplus \mathbb{Z}[\operatorname{PD}(X)], \\
H^{4}\left(X \times S^{2} ; \mathbb{Z}\right)=\mathbb{Z}\left[\operatorname{PD}\left(S^{2}\right)\right] \oplus\left(H^{2}(X ; \mathbb{Z}) \otimes \mathbb{Z}[\operatorname{PD}(X)]\right), \\
w_{2}\left(X \times S^{2}\right)=\mathbb{Z}_{2} \text {-reduction of } c_{1}(\omega), \\
p_{1}\left(X \times S^{2}\right)=3 \sigma(X) \operatorname{PD}\left(S^{2}\right) .
\end{gathered}$$
If
$$\phi: H^{2}\left(X^{\prime} ; \mathbb{Z}\right) \rightarrow H^{2}(X ; \mathbb{Z})$$
is any isomorphism preserving the intersection pairings, then we can naturally extend $\phi$ to an isomorphism
$$\Phi: H^{*}\left(X^{\prime} \times S^{2} ; \mathbb{Z}\right) \rightarrow H^{*}\left(X \times S^{2} ; \mathbb{Z}\right)$$
which maps
$$\alpha, \operatorname{PD}\left(X^{\prime}\right), \operatorname{PD}\left(S^{2}\right), \alpha \otimes \operatorname{PD}\left(X^{\prime}\right)$$
to
$$\phi(\alpha), \operatorname{PD}(X), \operatorname{PD}\left(S^{2}\right), \phi(\alpha) \otimes \operatorname{PD}(X)$$
respectively, for any $\alpha \in H^{2}\left(X^{\prime} ; \mathbb{Z}\right)$. Since $\phi$ maps characteristic elements to characteristic elements in the intersection form, the $\mathbb{Z}_{2}$-reduction of $\Phi$ will preserve $w_{2}$. $\Phi$ also preserves $p_{1}$ since it maps $\operatorname{PD}\left(S^{2}\right)$ to $\operatorname{PD}\left(S^{2}\right)$. Consequently, the following corollary is immediate.

Corollary 3.2. Any isomorphism
$$\phi \oplus I d: H^{2}\left(X^{\prime} ; \mathbb{Z}\right) \oplus \mathbb{Z}\left[P D\left(X^{\prime}\right)\right] \rightarrow H^{2}(X ; \mathbb{Z}) \oplus \mathbb{Z}[P D(X)],$$
where $\phi$ preserves intersection pairings and Id maps $P D\left(X^{\prime}\right)$ to $P D(X)$, can be realized as the induced map of an orientation-preserving diffeomorphism between $X \times S^{2}$ and $X^{\prime} \times S^{2}$.

Remark 3.3. Corollary 3.2 is about the existence of such a diffeomorphism inducing the desired cohomology map. Conversely, it has been observed in [HW23] that under the condition $\sigma(X) \neq 0$, the induced cohomology map of any diffeomorphism must also split as $\phi \oplus \pm I d$, where $\phi$ may reverse the sign of intersection pairings. This is also alluded in [MS12, Example 9.7.1].

\section*{4 Proof of Theorem 1.3}

Proof of Theorem 1.3. Let $(X, \omega)$ be a symplectic 4-manifold homeomorphic but not diffeomorphic to the rational manifold $\mathbb{C P}^{2} \# k \overline{\mathbb{C P}^{2}}$. By Theorem 2.1, we can take its unique minimal model $(\hat{X}, \hat{\omega})$ by blowing down $l$ disjoint symplectic exceptional spheres in classes $E_{1}, \cdots, E_{l} \in H_{2}(X ; \mathbb{Z})$. Let $\hat{X}^{\prime}$ be the rational manifold homeomorphic to $\hat{X}$ and let $X^{\prime}:=\hat{X} \# l \overline{\mathbb{C P}^{2}}$. Denote the line classes of $l \overline{\mathbb{C P}^{2}}$ in $X^{\prime}$ by $E_{1}^{\prime} \cdots, E_{l}^{\prime} \in H_{2}\left(X^{\prime} ; \mathbb{Z}\right)$. By Proposition 2.9, we can choose some symplectic form $\omega^{\prime}$ on $X^{\prime}$ such that there is a uniruled class $A$ with $\omega^{\prime}(A)<\sqrt{\left[\omega^{\prime}\right]^{2}}$. We further may assume $K_{\omega^{\prime}}=K_{\hat{X}^{\prime}}+\sum \operatorname{PD}\left(E_{i}^{\prime}\right)$ for some $K_{\hat{X}^{\prime}} \in \mathcal{K}_{\hat{X^{\prime}}}$ by first choosing symplectic form on $\hat{X}^{\prime}$ and then performing blowup with small size to obtain $\omega^{\prime}$. By Corollary 3.2, there are orientation-preserving diffeomorphisms
$$f: \hat{X} \times S^{2} \rightarrow \hat{X}^{\prime} \times S^{2}, \quad \tilde{f}: X \times S^{2} \rightarrow X^{\prime} \times S^{2}$$
such that $f^{*}=\phi \oplus \operatorname{Id}, \tilde{f}^{*}=\tilde{\phi} \oplus \operatorname{Id}$, where $\phi: H^{2}\left(\hat{X}^{\prime} ; \mathbb{Z}\right) \rightarrow H^{2}(\hat{X} ; \mathbb{Z})$ is an isomorphism preserving the intersection pairings and $\tilde{\phi}$ is the extension of $\phi$ which maps each $\operatorname{PD}\left(E_{i}^{\prime}\right)$ to $\operatorname{PD}\left(E_{i}\right)$. Let us choose two classes in $\mathcal{K}_{X}$
$$K_{+}:=K_{\hat{\omega}}+\sum \operatorname{PD}\left(E_{i}\right), \quad K_{-}:=-K_{\hat{\omega}}+\sum \operatorname{PD}\left(E_{i}\right)$$
and consider the class ${ }^{5} \tilde{\phi}\left(\left[\omega^{\prime}\right]\right)$. Since $\left[\omega^{\prime}\right] \in \mathcal{C}_{K_{\omega^{\prime}}}$ and $\mathcal{E}_{K_{\omega^{\prime}}} \supseteq\left\{E_{1}^{\prime}, \cdots, E_{l}^{\prime}\right\}$, by Theorem 2.2, $\omega^{\prime}\left(E_{i}^{\prime}\right)>0$ for all $i$. Also, note that $\mathcal{E}_{K_{+}}=\left\{E_{1}, \cdots, E_{l}\right\}$ by (1) and for all $i$,
$$\tilde{\phi}\left(\left[\omega^{\prime}\right]\right)\left(E_{i}\right)=\tilde{\phi}\left(\left[\omega^{\prime}\right]\right) \cdot \tilde{\phi}\left(\operatorname{PD}\left(E_{i}^{\prime}\right)\right)=\left[\omega^{\prime}\right] \cdot \operatorname{PD}\left(E_{i}^{\prime}\right)=\omega^{\prime}\left(E_{i}^{\prime}\right)>0 .$$
Hence, the discussion after Theorem 2.2 implies $\tilde{\phi}\left(\left[\omega^{\prime}\right]\right) \in \mathcal{C}_{K_{+}} \cup \mathcal{C}_{K_{-}}$so that there will be some symplectic form $\omega_{X}$ (different from the initial $\omega$ ) on $X$ in this class.

Now, let us choose a symplectic form $\omega_{S^{2}}$ on $S^{2}$ with sufficiently large area and compare the Gromov widths of the cohomologous symplectic forms $\omega_{X} \oplus \omega_{S^{2}}$ with $\tilde{f}^{*}\left(\omega^{\prime} \oplus \omega_{S^{2}}\right)$. By Corollary 2.4,
$$w_{G}\left(X, \omega_{X}\right)=\sqrt{\left[\omega_{X}\right]^{2}}=\sqrt{\left[\tilde{\phi}\left(\left[\omega^{\prime}\right]\right)\right]^{2}}=\sqrt{\left[\omega^{\prime}\right]^{2}} .$$
Since $\omega_{S^{2}}$ has large enough area, we see that
$$w_{G}\left(X \times S^{2}, \omega_{X} \oplus \omega_{S^{2}}\right) \geq \sqrt{\left[\omega^{\prime}\right]^{2}} .$$
On the other hand, by Theorem 2.8 and Proposition 2.10, we also have
$$w_{G}\left(X \times S^{2}, \tilde{f}^{*}\left(\omega^{\prime} \oplus \omega_{S^{2}}\right)\right)=w_{G}\left(X^{\prime} \times S^{2}, \omega^{\prime} \oplus \omega_{S^{2}}\right) \leq\left(\omega^{\prime} \oplus \omega_{S^{2}}\right)(A)=\omega^{\prime}(A)<\sqrt{\left[\omega^{\prime}\right]}{ }^{2} .$$

\footnotetext{
${ }^{5}$ Here, we also use $\tilde{\phi}$ to denote the map between real cohomology groups.
}

Therefore, they have different Gromov widths.
Fianlly, if these two cohomologous symplectic forms $\omega_{X} \oplus \omega_{S^{2}}$ with $\tilde{f}^{*}\left(\omega^{\prime} \oplus \omega_{S^{2}}\right)$ have the same first Chern classes, then $\tilde{\phi}\left(K_{\omega^{\prime}}\right)=K_{\omega_{X}}$. Recall that by Proposition 2.9, we may also assume $\left[\omega^{\prime}\right] \cdot K_{\omega^{\prime}}<0$. Thus,
$$\left[\omega_{X}\right] \cdot K_{\omega_{X}}=\tilde{\phi}\left(\left[\omega^{\prime}\right]\right) \cdot \tilde{\phi}\left(K_{\omega^{\prime}}\right)=\left[\omega^{\prime}\right] \cdot K_{\omega^{\prime}}<0 .$$
This will contradict with Liu-Ohta-Ono's Theorem [Liu96, OO96] which states that the existence of such symplectic form $\omega_{X}$ implies the manifold $X$ is diffeomorphic to rational or ruled manifold. So their first Chern classes are also different. \(\square\)

Note that it has been observed in [Li08, Proposition 4.10] that $\mathcal{C}_{X}=\mathcal{P}$ when $X=$ K3. Indeed, every positive class even has a hyperKähler representative. Therefore, in the above proof, if we take $\left(X^{\prime}, \omega^{\prime}\right)$ to be any homotopy $K 3$ with $K_{\omega^{\prime}} \neq 0$ and consider the diffeomorphism $f: X \times S^{2} \rightarrow X^{\prime} \times S^{2}$, there will be some symplectic form $\omega_{X} \oplus \omega_{S^{2}}$ on $X \times S^{2}$ cohomologous to $f^{*}\left(\omega^{\prime} \oplus \omega_{S^{2}}\right)$. However, the Chern class for any symplectic form on K3 must vanishi. As a result, $c_{1}\left(\omega_{X} \oplus \omega_{S^{2}}\right)$ belongs to the subspace $\mathbb{Z}[\mathrm{PD}(X)] \subseteq H^{2}\left(X \times S^{2} ; \mathbb{Z}\right)$ while $c_{1}\left(f^{*}\left(\omega^{\prime} \oplus \omega_{S^{2}}\right)\right)$ not. They must be different.

Finally, we remark that one can easily obtain examples of cohomologous symplectic forms with different Gromov widths and first Chern classes in higher dimensions by taking more products. For instance, consider $\left(X \times S^{2}\right) \times\left(S^{2}\right)^{k}$ with cohomologous symplectic forms $\omega_{X} \oplus \omega_{S^{2}} \oplus\left(\omega_{S^{2}}\right)^{k}$ and $\tilde{f}^{*}\left(\omega^{\prime} \oplus \omega_{S^{2}}\right) \oplus\left(\omega_{S^{2}}\right)^{k}$.

\section*{References}
\begin{itemize}
\item[] [AP08] Anar Akhmedov and B. Doug Park, Exotic smooth structures on small 4-manifolds, Invent. Math. 173 (2008), no. 1, 209-223. MR 2403396
\item[] [AP10] \_\_\_\_, Exotic smooth structures on small 4-manifolds with odd signatures, Invent. Math. 181 (2010), no. 3, 577-603. MR 2660453
\item[] [Bir97] P. Biran, Symplectic packing in dimension 4, Geom. Funct. Anal. 7 (1997), no. 3, 420-437. MR 1466333
\item[] [BK08] Scott Baldridge and Paul Kirk, A symplectic manifold homeomorphic but not diffeomorphic to $\mathbb{C P}^{2} \# 3 \overline{\mathbb{C P}}^{2}$, Geom. Topol. 12 (2008), no. 2, 919-940. MR 2403801
\item[] [FS98] Ronald Fintushel and Ronald J. Stern, Knots, links, and 4-manifolds, Invent. Math. 134 (1998), no. 2, 363-400. MR 1650308
\end{itemize}
[Gom95] Robert E. Gompf, A new construction of symplectic manifolds, Ann. of Math. (2) 142 (1995), no. 3, 527-595. MR 1356781
[Gro85] M. Gromov, Pseudo holomorphic curves in symplectic manifolds, Invent. Math. 82 (1985), no. 2, 307-347. MR 809718
[Her02] Haydee Herrera, Gromov invariants of $S^{2}$-bundles over 4-manifolds, Proceedings of the 1999 Georgia Topology Conference (Athens, GA), vol. 124, 2002, pp. 327-345. MR 1936210
[HW23] Amanda Hirschi and Luya Wang, On Donaldson's 4-6 question, arXiv:2309.07041 (2023).
[IP99] Eleny-Nicoleta Ionel and Thomas H. Parker, Gromov invariants and symplectic maps, Math. Ann. 314 (1999), no. 1, 127-158. MR 1689266
[Jup73] P. E. Jupp, Classification of certain 6-manifolds, Proc. Cambridge Philos. Soc. 73 (1973), 293-300. MR 314074
[KK17] Yael Karshon and Liat Kessler, Distinguishing symplectic blowups of the complex projective plane, J. Symplectic Geom. 15 (2017), no. 4, 1089-1128. MR 3734610
[Kot89] Dieter Kotschick, On manifolds homeomorphic to $\mathbf{C P}^{2} \# 8 \overline{\mathbf{C P}}^{2}$, Invent. Math. 95 (1989), no. 3, 591-600. MR 979367
[Li99] Tian-Jun Li, Smoothly embedded spheres in symplectic 4-manifolds, Proc. Amer. Math. Soc. 127 (1999), no. 2, 609-613. MR 1459135
[Li08] \_\_\_\_, The space of symplectic structures on closed 4-manifolds, Third International Congress of Chinese Mathematicians. Part 1, 2, AMS/IP Stud. Adv. Math., vol. 42, pt. 1, 2, Amer. Math. Soc., Providence, RI, 2008, pp. 259-277. MR 2409637
[Liu96] Ai-Ko Liu, Some new applications of general wall crossing formula, Gompf's conjecture and its applications, Math. Res. Lett. 3 (1996), no. 5, 569-585. MR 1418572
[LL95] T. J. Li and A. Liu, Symplectic structure on ruled surfaces and a generalized adjunction formula, Math. Res. Lett. 2 (1995), no. 4, 453-471. MR 1355707
[LL01] Tian-Jun Li and Ai-Ko Liu, Uniqueness of symplectic canonical class, surface cone and symplectic cone of 4-manifolds with $B^{+}=1, \mathrm{~J}$. Differential Geom. 58 (2001), no. 2, 331-370. MR 1913946
\begin{itemize}
\item[] [LR13] Tian-Jun Li and Yongbin Ruan, Uniruled symplectic divisors, Commun. Math. Stat. 1 (2013), no. 2, 163-212. MR 3197859
\item[] [McD90] Dusa McDuff, The structure of rational and ruled symplectic 4-manifolds, J. Amer. Math. Soc. 3 (1990), no. 3, 679-712. MR 1049697
\item[] [McD92] \_\_\_\_, Immersed spheres in symplectic 4-manifolds, Ann. Inst. Fourier (Grenoble) 42 (1992), no. 1-2, 369-392. MR 1162567
\item[] [McD98] \_\_\_\_, From symplectic deformation to isotopy, Topics in symplectic 4-manifolds (Irvine, CA, 1996), First Int. Press Lect. Ser., vol. I, Int. Press, Cambridge, MA, 1998, pp. 85-99. MR 1635697
\item[] [MP94] Dusa McDuff and Leonid Polterovich, Symplectic packings and algebraic geometry, Invent. Math. 115 (1994), no. 3, 405-434, With an appendix by Yael Karshon. MR 1262938
\item[] [MS12] Dusa McDuff and Dietmar Salamon, $J$-holomorphic curves and symplectic topology, second ed., American Mathematical Society Colloquium Publications, vol. 52, American Mathematical Society, Providence, RI, 2012. MR 2954391
\item[] [MS17] \_\_\_\_, Introduction to symplectic topology, third ed., Oxford Graduate Texts in Mathematics, Oxford University Press, Oxford, 2017. MR 3674984
\item[] [OO96] Hiroshi Ohta and Kaoru Ono, Notes on symplectic 4-manifolds with $b_{2}^{+}=1$. II, Internat. J. Math. 7 (1996), no. 6, 755-770. MR 1417784
\item[] [Par05] Jongil Park, Simply connected symplectic 4-manifolds with $b_{2}^{+}=1$ and $c_{1}^{2}=$ 2, Invent. Math. 159 (2005), no. 3, 657-667. MR 2125736
\item[] [PSS05] Jongil Park, András I. Stipsicz, and Zoltán Szabó, Exotic smooth structures on $\mathbb{C P}^{2} \# 5 \overline{\mathbb{C P}^{2}}$, Math. Res. Lett. 12 (2005), no. 5-6, 701-712. MR 2189231
\item[] [RU25] Javier Reyes and Giancarlo Urzúa, Exotic surfaces, Math. Ann. 391 (2025), no. 1, 227-254. MR 4846782
\item[] [Rua94] Yongbin Ruan, Symplectic topology on algebraic 3-folds, J. Differential Geom. 39 (1994), no. 1, 215-227. MR 1258920
\item[] [Sal13] Dietmar Salamon, Uniqueness of symplectic structures, Acta Math. Vietnam. 38 (2013), no. 1, 123-144. MR 3098204
\end{itemize}
[Sma62] S. Smale, On the structure of manifolds, Amer. J. Math. 84 (1962), 387-399. MR 153022
[SS05] András I. Stipsicz and Zoltán Szabó, An exotic smooth structure on $\mathbb{C P}^{2} \# 6 \overline{\mathbb{C P}^{2}}$, Geom. Topol. 9 (2005), 813-832. MR 2140993
[SY23] Kyler Siegel and Yuan Yao, On symplectic packing problems in higher dimensions, arXiv:2312.13224 (2023).
[Tau96] Clifford H. Taubes, SW ⇒ Gr: from the Seiberg-Witten equations to pseudoholomorphic curves, J. Amer. Math. Soc. 9 (1996), no. 3, 845-918. MR 1362874
[Vid01] Stefano Vidussi, Homotopy K3's with several symplectic structures, Geom. Topol. 5 (2001), 267-285. MR 1825663
[Wal64] C. T. C. Wall, On simply-connected 4-manifolds, J. London Math. Soc. 39 (1964), 141-149. MR 163324
[Wen18] Chris Wendl, Holomorphic curves in low dimensions, Lecture Notes in Mathematics, vol. 2216, Springer, Cham, 2018, From symplectic ruled surfaces to planar contact manifolds. MR 3821526