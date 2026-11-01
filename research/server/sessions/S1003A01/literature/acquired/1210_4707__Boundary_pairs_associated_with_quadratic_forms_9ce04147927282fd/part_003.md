---
retention_scope: session
part: 3
total_parts: 4
---

[Part 3/4 of: [1210.4707] Boundary pairs associated with quadratic forms]

If we assume elliptic regularity for the boundary pair then we can conclude the following stronger spectral relations:
Theorem 4.14. Assume that $(\Gamma, \mathscr{G})$ is an elliptically regular boundary pair associated with the quadratic form $\mathfrak{h}$ and let $\lambda \in \mathbb{C} \backslash \sigma\left(H^{\mathrm{D}}\right)$. Then the following assertions are true:
\begin{itemize}
\item[i.] The spectral relation
$$\lambda \in \sigma(H) \quad \Leftrightarrow \quad 0 \in \sigma(\Lambda(\lambda)) .$$
holds for the entire spectrum.
\item[ii.] Assume that $\Gamma: \mathscr{H}^{1} \longrightarrow \mathscr{G}$ is a compact operator (see Theorem 2.36 for equivalent characterisations) then $\sigma_{\mathrm{ess}}(H)=\sigma_{\mathrm{ess}}\left(H^{\mathrm{D}}\right)$, and $\sigma(H) \backslash \sigma\left(H^{\mathrm{D}}\right)$ consists of discrete eigenvalues of $H$, only. In particular, if $\lambda \notin \sigma\left(H^{\mathrm{D}}\right)$, then the relation (4.15) is true for the discrete spectrum, i.e., with $\sigma(\cdot)$ replaced by $\sigma_{\text {disc }}(\cdot)$.
\item[iii.] An eigenvalue $\lambda$ is isolated in the spectrum of $H$ iff $\lambda$ is isolated in the spectrum of the operator pencil $\Lambda(\cdot)$, i.e.,
$$\lambda \text { is isolated in } \sigma(H) \quad \Leftrightarrow \quad \lambda \text { is isolated in the operator pencil spectrum } \sigma(\Lambda(\cdot)) \text {. }$$
If one of the conditions is fulfilled, then the estimate (4.12c) holds.
\item[iv.] Assume additionally, that the boundary pair is positive, then
$$\lambda \text { is isolated in } \sigma(H) \quad \Leftrightarrow \quad 0 \text { is isolated in the individual spectrum } \sigma(\Lambda(\lambda))$$
(i.e., isolated in the spectrum of the individual operator $\Lambda(\lambda)$ ). In particular, the spectral relation (4.15) is also true for the discrete and essential spectrum, i.e., with $\sigma(\cdot)$ replaced by $\sigma_{\text {disc }}(\cdot)$ resp. $\sigma_{\text {ess }}(\cdot)$.
\end{itemize}

Proof. (i) Note first that by elliptic regularity, $\Lambda(\lambda)$ is closed for all $\lambda \in \mathbb{C} \backslash \sigma\left(H^{\mathrm{D}}\right)$ (i.e., also for $\lambda \in \sigma(H)$ ) by Theorem 3.10 (iv), and it makes sense to speak of $\sigma(\Lambda(\lambda))$.
"⇒": We argue by contraposition: If $0 \notin \sigma(\Lambda(\lambda))$, then $\Lambda(\lambda)^{-1}$ exists and is bounded. Moreover, the limit of $\left(\Lambda(z)^{-1}-\Lambda(\lambda)^{-1}\right) /(z-\lambda)$ as $z \rightarrow \lambda$ exists in $\mathscr{B}(\mathscr{G})$ by Proposition 3.13 (vi) (the boundary pair is elliptic!). Note that we only know $\lambda \notin \sigma\left(H^{\mathrm{D}}\right)$ here, but we do not know yet that $\lambda \notin \sigma(H)$, therefore we cannot apply the formula of Proposition 2.34 (i) here.

In particular, the map $\Lambda(z)^{-1}: \mathscr{G} \longrightarrow \mathscr{G}$ is holomorphic in $z \in \mathbb{C} \backslash \sigma\left(H^{\mathrm{D}}\right)$ and also in $z=\lambda$. Since also $\lambda \notin \sigma\left(H^{\mathrm{D}}\right)$ and since again the boundary pair is elliptically regular, $\bar{S}(z): \mathscr{G} \longrightarrow \mathscr{H}$ is bounded and also depends holomorphically on $z$ near $\lambda$. Therefore, the operator
$$R^{\mathrm{D}}(z)+\bar{S}(z) \Lambda(z)^{-1} S(\bar{z})^{*}: \mathscr{H} \longrightarrow \mathscr{H}$$
depends holomorphically on $z$ and is still a bounded operator as $z \rightarrow \lambda$. By Theorem 4.3 (ii), this operator equals $R(z)$ for $z \in \mathbb{C} \backslash \sigma(H)$. As $R(z)$ is then still a bounded operator on $\mathscr{H}$ for $z \rightarrow \lambda$, we have $\lambda \notin \sigma(H)$ (the resolvent set $\mathbb{C} \backslash \sigma(H)$ is the maximal set of holomorphy, see [Ka66, Thm. III.6.7]).
"⇐" was already shown in Theorem 4.11 (iii).
(ii) By Theorem 2.36, $\Lambda^{-1}$ is compact, and by (4.4c) and the elliptic regularity, it follows that the resolvent difference $R-R^{\mathrm{D}}$ is compact, too. In particular, the essential spectra agree. The spectral relation follows from Theorem 4.11(i), since the spectrum now consists of eigenvalues of finite multiplicity only.
(iii) That $\lambda$ is an eigenvalue of $\sigma(H)$ iff $\operatorname{ker} \Lambda(\lambda)$ is nontrivial follows already from Theorem 4.11 (i).
"⇒" follows from Theorem 4.11 (iv), but a shorter proof is as follows: If $\lambda$ is isolated in $\sigma(H)$, then $\Lambda(z)^{-1}$ exists and is bounded by Proposition 2.31 (iii) for $z \in \mathbb{C} \backslash \sigma\left(H^{\mathrm{D}}\right)$ with $0<|z-\lambda|$ small enough, i.e., $\lambda$ is isolated in $\sigma(\Lambda(\cdot))$. "⇐" Using (4.16), Krein's resolvent formula (4.4c) (and the elliptic regularity), we conclude that $R(z)$ is defined for $z$ with $0<|z-\lambda|$ small enough, and also has a pole at $z=\lambda$, hence $\lambda \in \sigma(H)$ is isolated.
(iv) is a consequence of (iii) and Proposition 4.6. For the representation (4.7) we refer to (4.13). \(\square\)

Remark 4.17. Let us comment on the elliptic regularity condition and some other aspects:
\begin{itemize}
\item[i.] The elliptic regularity condition for the spectral equivalence in Theorem 4.14 (i) is needed for the implication "⇒": We give a counterexample of a non-elliptically regular boundary pair in Example 6.17, where $0 \in \sigma(H)$ but $0 \notin \sigma(\Lambda(0))$.
For the opposite implication it is enough to assume that $\Lambda(\lambda)$ is closed.
\item[ii.] Without the elliptic regularity assumption, the conclusion of Theorem 4.14 (ii) is also generally false: From Krein's resolvent formula (4.4b) the compactness of $\Lambda^{-1}$ does not in general imply that $R-R^{\mathrm{D}}$ is compact: In Example 6.16 we have a non-elliptically regular boundary pair for which $R^{\mathrm{D}}$ is compact, but $R$ is not, even though $\Lambda^{-1}$ may be be compact.
\item[iii.] The implication " $0 \in \sigma(\Lambda(\lambda))$ isolated $\Rightarrow \lambda \in \sigma(H)$ isolated" in Theorem 4.14 (iv) is generally false for non-elliptically regular boundary pairs: In Example 6.18 we give an example of a boundary pair which is positive, but not elliptically regular. For this example, $0 \in \sigma(\Lambda(0))$ is isolated, while $0 \in \sigma(H)=[0, \infty)$ is not.
\item[iv.] Note that the spectral characterisations of Theorems 4.11 and 4.14 are void if $\sigma(H)=\sigma\left(H^{\mathrm{D}}\right)=[0, \infty)$ as in the example of a non-compact cylindrical manifold in Section 6.4. In this case, the Dirichlet-to-Neumann operator is not defined for $\lambda \in[0, \infty)$.
\item[v.] For bounded and positive boundary pairs (hence for ordinary boundary triples, see Theorem 1.20), there is also a characterisation for the absolutely and singular continuous spectrum (see [BGPa08]) if the Dirichlet-to-Neumann operator has the special form
$$\Lambda(z)=\frac{\dddot{\Delta}-m(z)}{n(z)},$$
where $\ddot{\Delta}$ is a bounded, self-adjoint operator on $\mathscr{G}$ and where $m, n$ are functions holomorphic on $\mathbb{C} \backslash \sigma\left(H^{\mathrm{D}}\right)$. We believe that this assertion remains true for elliptically regular and positive boundary pairs (and maybe even in more general settings), but where $\ddot{\Delta}$ may be unbounded. We hope to come back to the analysis of the absolutely continuous spectrum in a forthcoming publication.
\end{itemize}

\section*{5 Boundary pairs constructed from other boundary pairs}

In this section, we give classes of of boundary pairs constructed from others, such as Robin-type perturbations (where we change the quadratic form with which the boundary pair is associated), coupled boundary pairs or the bounded modification of an unbounded boundary pair (where we change the boundary space).

\subsection*{5.1 Robin boundary conditions}

We start explaining how to use our concept of boundary pairs also for more general "boundary conditions" than Neumann. The basic idea is to change the underlying quadratic form $\mathfrak{h}$, but leave the boundary pair $(\Gamma, \mathscr{G})$ as it is. For simplicity, we consider only constants $a$ and no operators on $\mathscr{G}$, here.

Let $(\Gamma, \mathscr{G})$ be a boundary pair associated with a quadratic form $\mathfrak{h}$. For $a \geq 0$, we define
$$\mathfrak{h}_{a}(f):=\mathfrak{h}(f)+a\|\Gamma f\|_{\mathscr{G}}^{2}$$
for $h \in \operatorname{dom} \mathfrak{h}_{a}:=\mathscr{H}^{1}$. Since
$$(\mathfrak{h}+\mathfrak{1})(f) \leq\left(h_{a}+\mathfrak{1}\right)(f) \leq\left(1+a\|\Gamma\|^{2}\right)(\mathfrak{h}+\mathfrak{1})(f),$$
the norms associated with $\mathfrak{h}$ and $\mathfrak{h}_{a}$ (see (2.1)) are equivalent, hence $\mathfrak{h}_{a}$ is also a closed quadratic form on $\mathscr{H}^{1}$. We will now derive the objects arising from the boundary pair $(\Gamma, \mathscr{G})$ associated with $\mathfrak{h}_{a}$, denoted with a subscript $(\cdot)_{a}$ :

Proposition 5.2.
\begin{itemize}
\item[i.] The Dirichlet operator is unchanged, i.e., $\mathscr{H}_{a}^{1, \mathrm{D}}=\mathscr{H}^{1, \mathrm{D}}=\operatorname{ker} \Gamma$ and $H_{a}^{\mathrm{D}}=H^{\mathrm{D}}$.
\end{itemize}
\begin{itemize}
\item[ii.] The Neumann operator $H_{a}$ has domain
$$\operatorname{dom} H_{a}=\left\{f \in \mathscr{W} \mid \Gamma^{\prime} f+a \Gamma f=0\right\},$$
where $\mathscr{W}$ is the domain of $\Gamma^{\prime}$ for the maximal boundary triple associated with $(\Gamma, \mathscr{G})$ (see Definition 1.13 and Section 1.4 for the notation).
\item[iii.] The range of the boundary map is unchanged, as well as the Dirichlet solution operator; i.e., $\mathscr{G}_{a}^{1 / 2}=\mathscr{G}^{1 / 2}=$ $\operatorname{ran} \Gamma$ and $S_{a}(z)=S(z)$.
\item[iv.] The Dirichlet-to-Neumann form $\mathfrak{l}_{z, a}$ for the boundary pair associated with $\mathfrak{h}_{a}$ is given by
$$\mathfrak{l}_{z, a}(\varphi)=\mathfrak{l}_{z}(\varphi)+a\|\varphi\|_{\mathscr{G}}^{2} \quad \text { or, in operator form, } \quad \breve{\Lambda}_{a}(z)=\breve{\Lambda}(z)+a .$$
\item[] $v$. The boundary pair associated with $\mathfrak{h}_{a}$ is elliptically regular resp. positive iff the boundary pair associated with $\mathfrak{h}$ is.
\item[vi.] We have $R \geq R_{a} \geq R^{\mathrm{D}}$. In particular, if $R: \mathscr{H} \longrightarrow \mathscr{H}$ is compact, then $R_{a}: \mathscr{H} \longrightarrow \mathscr{H}$ and $R^{\mathrm{D}}: \mathscr{H} \longrightarrow \mathscr{H}$ are also compact, and the eigenvalues fulfil
$$\lambda_{k}(H) \leq \lambda_{k}\left(H_{a}\right) \leq \lambda_{k}\left(H^{\mathrm{D}}\right)$$
(labelled in increasing order respecting their multiplicity).
\end{itemize}

Proof. We only indicate some of the arguments here: For the domain inclusion " $\subset$ " of (ii) note that $f \in \operatorname{dom} H_{a}$ implies that there is $h \in \mathscr{H}$ such that
$$\mathfrak{h}(f, g)+a\langle\Gamma f, \Gamma g\rangle=\langle h, g\rangle$$
for all $g \in \mathscr{H}^{1}$. If we assume $g \in \operatorname{dom} H^{\min }=\operatorname{dom} H^{\mathrm{D}} \cap \operatorname{dom} H$ in the last equation, then the boundary term vanishes and $\mathfrak{h}(f, g)=\langle f, H g\rangle$, hence $f \in \operatorname{dom} H^{\text {max }}$ and $H^{\text {max }} f=h$. Moreover, the defining equation for $\mathscr{W}$ of the associated maximal boundary triple (see the forthcoming publication [P] for details) is fulfilled. Finally, comparing the above formula with Green's first identity (1.14), we see that $\Gamma^{\prime} f=-a \Gamma f$. Therefore, we have shown that $f \in \mathscr{W}$. (vi) For the last assertion note that $(0 \leq) \mathfrak{h} \leq \mathfrak{h}_{a} \leq \mathfrak{h}^{\mathrm{D}}$ in the sense of quadratic forms (cf. e.g. [Da95, Sec. 4.4]). Therefore, $R \geq R_{a} \geq R^{\mathrm{D}}(\geq 0)$, i.e., $R_{a}$ and $R^{\mathrm{D}}$ are also compact. \(\square\)

The following proposition is useful when proving statements for $\lambda$ inside the Neumann spectrum $H$ stating that one can always find an $a>0$ such that $\lambda$ is not in the spectrum of $H_{a}$, even if $\lambda \in \sigma(H)$, provided the Dirichlet and Neumann spectra are purely discrete.

Proposition 5.3. Let $(\Gamma, \mathscr{G})$ be a boundary pair and $\lambda \in[0, \infty)$. Assume in addition that $R$ is compact. If $\lambda \notin \sigma\left(H^{\mathrm{D}}\right)$ then there exists $a_{0}>0$ such that $\lambda \notin \sigma\left(H_{a}\right)$ for all $a \geq a_{0}$.

Proof. The operator
$$\Lambda^{1 / 2} \Gamma R^{1 / 2}: \mathscr{H} \xrightarrow{R^{1 / 2}} \mathscr{H} \xrightarrow{\Gamma} \mathscr{G}^{1 / 2} \xrightarrow{\Lambda^{1 / 2}} \mathscr{G}$$
is bounded and $R^{1 / 2}$ is compact as operator in $\mathscr{H}$, since $R$ is compact. In particular, the operator $\Lambda^{1 / 2} \Gamma R=$ $\Lambda^{1 / 2} \Gamma R^{1 / 2} R^{1 / 2}: \mathscr{H} \longrightarrow \mathscr{G}$ is compact. By [BBABr11, Thm. 2.6], we have $\left\|R_{a}-R^{\mathrm{D}}\right\| \rightarrow 0$ as $a \rightarrow \infty$, i.e., $H_{a}$ converges in norm resolvent sense to $H^{\mathrm{D}}$. This implies in particular, that if $\lambda \notin \sigma\left(H^{\mathrm{D}}\right)$, then there exists $a_{0}>0$ such that $\lambda \notin \sigma\left(H_{a}\right)$ for all $a \geq a_{0}$ (see e.g. [RS80, Thm VIII.23]). \(\square\)

\subsection*{5.2 Coupled boundary pairs}

We present in this subsection two procedures of coupling boundary pairs. Such couplings have already been treated e.g. in [DHMdS00].

Assume that $\left(\Gamma_{i}, \mathscr{G}\right)$ is a boundary pair associated with $\mathfrak{h}_{i}\left(\operatorname{dom} \mathfrak{h}_{i}=\mathscr{H}_{i}^{1}\right)$ in the Hilbert space $\mathscr{H}_{i}$ for $i=1,2$. Note that the boundary space is the same for both boundary pairs. We assume additionally that
$$\mathscr{G}^{1 / 2}:=\operatorname{ran} \Gamma_{1} \cap \operatorname{ran} \Gamma_{2} \quad \text { is dense in } \mathscr{G} .$$
We set $\mathscr{H}:=\mathscr{H}_{1} \oplus \mathscr{H}_{2}$ and $\mathscr{H}^{1, \text { dec }}:=\mathscr{H}_{1}^{1} \oplus \mathscr{H}_{2}^{1}$. It follows easily from the boundedness of $\Gamma_{i}: \mathscr{H}_{i}^{1} \longrightarrow \mathscr{G}$ that
$$\mathscr{H}^{1}:=\left\{f \in \mathscr{H}^{1, \mathrm{dec}} \mid \Gamma_{1} f_{1}=\Gamma_{2} f_{2}\right\}$$
is a closed subspace of $\mathscr{H}^{1, \text { dec }}$, and $\mathfrak{h}:=\left(\mathfrak{h}_{1} \oplus \mathfrak{h}_{2}\right) \upharpoonright_{\mathscr{H}^{1}}$ is a non-negative, closed form in $\mathscr{H}$ with associated operator $H$. We call $\mathfrak{h}$ the coupled form obtained from $\mathfrak{h}_{1}$ and $\mathfrak{h}_{2}$.

Set
$$\Gamma: \mathscr{H}^{1} \longrightarrow \mathscr{G}, \quad \Gamma f:=\Gamma_{1} f_{1}=\Gamma_{2} f_{2} .$$

Proposition 5.6. Assume that $\left(\Gamma_{i}, \mathscr{G}\right)$ are boundary pairs for $i=1,2$ such that the density condition (5.4) holds. Then the following assertions are true:
\begin{itemize}
\item[i.] The pair $(\Gamma, \mathscr{G})$ is a boundary pair associated with the coupled quadratic form $\mathfrak{h}$, called here the (Neumann-)coupled boundary pair.
\item[ii.] The Dirichlet operator associated with the coupled boundary pair is decoupled, i.e., $H^{\mathrm{D}}=H_{1}^{\mathrm{D}} \oplus H_{2}^{\mathrm{D}}$, while the Neumann operator (the operator associated with $\mathfrak{h}$ ) is (in general) coupled. Moreover, the Dirichlet solution operator and the Dirichlet-to-Neumann operator of the coupled boundary pair are given by
$$S(z) \varphi=S_{1}(z) \varphi \oplus S_{2}(z) \varphi \quad \text { and } \quad \breve{\Lambda}(z) \varphi=\breve{\Lambda}_{1}(z) \varphi+\breve{\Lambda}_{2}(z) \varphi$$
for $\varphi \in \mathscr{G}^{1 / 2}=\operatorname{ran} \Gamma$, where $z \in \mathbb{C} \backslash \sigma\left(H^{\mathrm{D}}\right)=\mathbb{C} \backslash\left(\sigma\left(H_{1}^{\mathrm{D}}\right) \cup \sigma\left(H_{2}^{\mathrm{D}}\right)\right)$.
\item[iii.] We have
$$\|\varphi\|_{\mathscr{G}^{1 / 2}}^{2}:=\|S \varphi\|_{\mathscr{H}^{1}}^{2}=\left\|S_{1} \varphi\right\|_{\mathscr{H}_{1}^{1}}^{2}+\left\|S_{2} \varphi\right\|_{\mathscr{H}_{2}^{1}}^{2} \geq\|\varphi\|_{\mathscr{G}_{i}^{1 / 2}}^{2},$$
i.e., the embedding $\mathscr{G}_{i}^{1 / 2} \hookrightarrow \mathscr{G}^{1 / 2}=\operatorname{ran} \Gamma$ is bounded for $i=1,2$. If in addition $\operatorname{ran} \Gamma_{1}=\operatorname{ran} \Gamma_{2}$, then the embedding is surjective, and the norms on $\mathscr{G}^{1 / 2}, \mathscr{G}_{1}^{1 / 2}$ and $\mathscr{G}_{2}^{1 / 2}$ are mutually equivalent.
\item[iv.] If the boundary pairs $\left(\Gamma_{i}, \mathscr{G}\right)$ are elliptically regular resp. positive, then the coupled boundary pair $(\Gamma, \mathscr{G})$ is elliptically regular resp. positive.
\item[v.] Krein's resolvent formula in this context reads as
$$\left.\breve{R}(z)=\iota_{1} \breve{R}_{1}^{\mathrm{D}}(z) \iota_{1}^{*} \oplus \iota_{2} \breve{R}_{2}^{\mathrm{D}}(z)\right) \iota_{2}^{*}+S(z) \breve{\Lambda}(z)^{-1} S(\bar{z})^{*}: \mathscr{H}^{-1} \longrightarrow \mathscr{H}^{1}$$
$\left(\right.$ with $\breve{R}_{i}^{\mathrm{D}}(z)=\left(\breve{H}_{i}^{\mathrm{D}}-z\right)^{-1}: \mathscr{H}_{i}^{-1, \mathrm{D}} \longrightarrow \mathscr{H}_{i}^{1, \mathrm{D}}$ and $\left.\iota_{i}: \mathscr{H}_{i}^{1, \mathrm{D}} \hookrightarrow \mathscr{H}_{i}^{1}\right)$, i.e., the resolvent of the coupled operator can be expressed by operators of the individual boundary pairs only, namely, the direct sum of the Dirichlet resolvents and a coupling term.
\end{itemize}

Proof. (i) The boundedness of $\Gamma$ is obvious, as well as the density of
$$\mathscr{H}^{1, \mathrm{D}}:=\operatorname{ker} \Gamma=\operatorname{ker} \Gamma_{1} \oplus \operatorname{ker} \Gamma_{2}=\mathscr{H}_{1}^{1, \mathrm{D}} \oplus \mathscr{H}_{2}^{1, \mathrm{D}} .$$
Moreover, $\operatorname{ran} \Gamma=\mathscr{G}^{1 / 2}$ is dense in $\mathscr{G}$ by assumption (5.4).
(ii) That $H^{\mathrm{D}}$ is decoupled is obvious, as well as the formula for the coupled Dirichlet solution operator. The formula for the coupled solution operator is obvious. The corresponding Neumann operator is (in general) coupled (i.e., not a direct sum of the individual Neumann operators) For the coupled Dirichlet-to-Neumann operator, note that
$$\begin{aligned}
\langle\breve{\Lambda}(z) \varphi, \psi\rangle & =(\mathfrak{h}-z \mathbf{l})(S(z), g) \\
& =\left(\mathfrak{h}_{1}-z \mathbf{l}\right)\left(S_{1}(z), g_{1}\right)+\left(\mathfrak{h}_{1}-z \mathbf{l}\right)\left(S_{1}(z), g_{2}\right)=\left\langle\breve{\Lambda}_{1}(z) \varphi, \psi\right\rangle+\left\langle\breve{\Lambda}_{2}(z) \varphi, \psi\right\rangle
\end{aligned}$$
for $\varphi \in \mathscr{G}^{1 / 2}$ and any $g=g_{1} \oplus g_{2} \in \mathscr{H}^{1}$ with $\Gamma g=\psi$ (see (2.24a) and Definition 2.25).
(iii) The equivalence of the norms follows from the open mapping theorem (a bounded bijective operator has also a bounded inverse).
(iv) The last assertion is also obvious, using Definitions 3.1 and 3.15. We have e.g.
$$\mathfrak{q}(\varphi)=\|S \varphi\|_{\mathscr{H}}^{2}=\left\|S_{1} \varphi\right\|_{\mathscr{H}_{1}}^{2}+\left\|S_{1} \varphi\right\|_{\mathscr{H}_{1}}^{2}=\mathfrak{q}_{1}(\varphi)+\mathfrak{q}_{2}(\varphi) \leq\left(C_{1}+C_{2}\right)\|\varphi\|_{\mathscr{G}}^{2}$$
if $\mathfrak{q}_{1}, \mathfrak{q}_{2}$ resp. $C_{1}, C_{2}$ are the solution forms resp. constants in the estimate of Definition 3.1 for the individual boundary pairs. \(\square\)

In many applications, the RHS of Krein's resolvent formula (5.7) in the coupled case can be calculated explicitly, hence we have a formula for the resolvent of the coupled operator (see Remark 6.28 for an example).

There is another way of coupling two boundary pairs: Let $\mathfrak{h}^{\text {dec }}=\mathfrak{h}_{1} \oplus \mathfrak{h}_{2}$ with domain $\operatorname{dom} \mathfrak{h}^{\text {dec }}=\mathscr{H}^{1 \text {,dec }}=$ $\mathscr{H}_{1}^{1} \oplus \mathscr{H}_{2}^{2}$. As boundary operator, we define here
$$\widetilde{\Gamma} f:=\Gamma_{1} f_{1}-\Gamma_{2} f_{2} .$$
It is again easily seen that $(\widetilde{\Gamma}, \mathscr{G})$ is a boundary pair associated with $\mathfrak{h}^{\text {dec }}$. Then the associated Neumann operator is $\widetilde{H}=H_{1} \oplus H_{2}$, hence decoupled. Moreover, ker $\widetilde{\Gamma}$ equals $\mathscr{H}^{1}$ defined in (5.5), and the Dirichlet operator $\widetilde{H}^{\mathrm{D}}$ associated with this boundary pair is the coupled operator. We call this boundary pair the Dirichlet-coupled boundary pair, since the Dirichlet operator is coupled here.

It is now straightforward to calculate the associated Dirichlet solution operators and the Neumann-to-Dirichlet operator of the coupled boundary pair as
$$\widetilde{S} \varphi=S_{1}\left(\breve{\Lambda}_{1}+\breve{\Lambda}_{2}\right)^{-1} \breve{\Lambda}_{2} \varphi \oplus S_{2}\left(\breve{\Lambda}_{1}+\breve{\Lambda}_{2}\right)^{-1} \breve{\Lambda}_{1} \varphi \quad \text { and } \quad \breve{\widetilde{\Lambda}}(z)^{-1} \varphi=\breve{\Lambda}_{1}(z)^{-1} \varphi+\breve{\Lambda}_{2}(z)^{-1} \varphi$$
for $\varphi \in \widetilde{\mathscr{G}}^{1 / 2}=\mathscr{G}_{1}^{1 / 2}+\mathscr{G}_{2}^{1 / 2}$.

\subsection*{5.3 Direct sum of boundary pairs}

Another way of obtaining a new boundary pair from two boundary pairs ( $\Gamma_{i}, \mathscr{G}_{i}$ ) associated with $\mathfrak{h}_{i}$ on $\mathscr{H}_{i}(i=1,2)$ is by taking the direct sum of all objects, i.e., $\mathscr{H}:=\mathscr{H}_{1} \oplus \mathscr{H}_{2}, \mathscr{G}:=\mathscr{G}_{1} \oplus \mathscr{G}_{2}, \Gamma:=\Gamma_{1} \oplus \Gamma_{2}$ etc. We call this boundary pair the direct sum of the boundary pairs $\left(\Gamma_{1}, \mathscr{G}_{1}\right)$ and $\left(\Gamma_{2}, \mathscr{G}_{2}\right)$. The corresponding derived objects and the properties of the direct sum can easily be derived; e.g. $\Lambda(z)=\Lambda_{1}(z) \oplus \Lambda_{2}(z)$ and its spectrum is the union of the spectra of $\Lambda_{i}(z)$. Note that the direct sum is different from the coupled pairs defined in Section 5.2.

\subsection*{5.4 Regularisation: Making a boundary pair bounded}

Let us finally define a bounded boundary pair $(\widetilde{\Gamma}, \widetilde{\mathscr{G}})$ constructed from an unbounded boundary pair $(\Gamma, \mathscr{G})$ associated with $\mathfrak{h}$ as follows: We set
$$\widetilde{\mathscr{G}}:=\mathscr{G}^{1 / 2} \quad \text { and } \quad \widetilde{\Gamma}: \mathscr{H}^{1} \longrightarrow \widetilde{\mathscr{G}},$$
where $\widetilde{\mathscr{G}}$ is endowed with the norm $\|\varphi\|_{\widetilde{\mathscr{G}}}=\|\varphi\|_{\mathscr{G}^{1 / 2}}=\|S \varphi\|_{\mathscr{H}^{1}}$, i.e., we just change the range space of $\Gamma$, and obviously, $\operatorname{ran} \widetilde{\Gamma}=\widetilde{\mathscr{G}}$, i.e., $(\widetilde{\Gamma}, \widetilde{\mathscr{G}})$ is a bounded boundary pair. For the new boundary pair, called the bounded modification or regularisation of $(\Gamma, \mathscr{G})$, we have $\|\widetilde{\Gamma}\|_{1 \rightarrow 0}=1$. Moreover its weak Dirichlet solution operator and Dirichlet-to-Neumann operator are given as follows:

Proposition 5.9. Assume that $(\Gamma, \mathscr{G})$ is an unbounded boundary pair associated with a quadratic form $\mathfrak{h}$. Denote by $(\widetilde{\Gamma}, \widetilde{\mathscr{G}})$ its bounded modification, given by $\widetilde{\mathscr{G}}=\mathscr{G}^{1 / 2}, \widetilde{\Gamma}: \mathscr{H}^{1} \longrightarrow \widetilde{\mathscr{G}}, \widetilde{\Gamma} f=\Gamma f$, where the objects without tilde refer to $(\Gamma, \mathscr{G})$ and the objects with tilde refer to $(\widetilde{\Gamma}, \widetilde{\mathscr{G}})$. Then the following assertions are true:
\begin{itemize}
\item[i.] The Neumann and Dirichlet operators remain unchanged, i.e., $\widetilde{H}^{\mathrm{D}}=H^{\mathrm{D}}$ and $\widetilde{H}=H$.
\item[ii.] We have
$$\widetilde{S}(z): \widetilde{\mathscr{G}} \longrightarrow \mathscr{H}^{1}, \quad \widetilde{S}(z) \varphi=S(z) \varphi, \quad \widetilde{\Lambda}=\mathrm{id}_{\widetilde{\mathscr{G}}} \quad \text { and } \quad \widetilde{\Lambda}(z)=\breve{\Lambda}^{-1} \breve{\Lambda}(z): \widetilde{\mathscr{G}} \longrightarrow \widetilde{\mathscr{G}} .$$
\item[iii.] The boundary pair $(\widetilde{\Gamma}, \widetilde{\mathscr{G}})$ is bounded and in particular elliptically regular. Moreover $\widetilde{S}(z): \widetilde{\mathscr{G}} \longrightarrow \mathscr{H}$ and $\widetilde{\Lambda}(z): \widetilde{\mathscr{G}} \longrightarrow \widetilde{\mathscr{G}}$ are bounded operators, the norm of the latter is bounded by $L(z)$ (cf. (2.24c)).
\item[iv.] If $(\Gamma, \mathscr{G})$ is not positive, then $(\widetilde{\Gamma}, \widetilde{\mathscr{G}})$ is not either.
\end{itemize}

Remark 5.10. Note that although we could only work with bounded boundary pairs, there is not always an associated ordinary boundary triple (for this we need that the new (and hence the old) boundary pair is positive, see Theorem 1.20). The bounded modification of an unbounded boundary pair is obviously elliptically regular (because it is bounded), but not necessarily positive (in particular the bounded modification is not positive if the original boundary pair is not). In Example 6.29 we present a bounded modification of a boundary pair which is not positive.

Moreover, the unbounded boundary pair is in many examples more "natural" like in the manifold example in Section 6.3 since the regularised boundary pair involves the Dirichlet-to-Neumann operator in the norm of the new boundary space (see also the second last paragraph of Section 1.5: "Applications of . . .").

\section*{6 Examples}

All our examples are of the form $\mathscr{H}=\mathrm{L}_{2}(X, \mu)$ and $\mathscr{G}:=\mathrm{L}_{2}(Y, \nu)$ where $(X, \mu)$ and $(Y, \nu)$ are measure spaces and $Y \subset X$, as explained in Example 2.4

\subsection*{6.1 Examples with finite-dimensional boundary space}

We treat here a simple example where $X=I$ is a compact interval and $Y=\partial I$ consists of two points only. The corresponding boundary space is two-dimensional and the boundary pair is bounded and positive, hence associated with an ordinary boundary triple (see Theorem 1.20).

More precisely, let $I=[0, \ell]$ for some $\ell \in(0, \infty)$ and set $\mathscr{H}:=\mathrm{L}_{2}(I), \mathscr{H}^{1}:=\mathrm{H}^{1}(X), \mathfrak{h}(f):=\left\|f^{\prime}\right\|_{\mathrm{L}_{2}(I)}^{2}$. As boundary operator, we choose $\Gamma f=(f(0), f(\ell))$. It follows now from standard assertions on Sobolev spaces that $(\Gamma, \mathscr{G})$ is a boundary pair. Moreover, the Neumann and Dirichlet operators are the usual Neumann and Dirichlet Laplacians on $[0, \ell]$, and the Dirichlet solution operator is given by
$$S(z) \varphi=\varphi_{0} \frac{\sin (\sqrt{z}(\ell-s))}{\sin (\sqrt{z} \ell)}+\varphi_{1} \frac{\sin (\sqrt{z} s)}{\sin (\sqrt{z} \ell)}$$
for $z \notin \sigma\left(H^{\mathrm{D}}\right)=\left\{k^{2} \pi^{2} / \ell^{2} \mid k=1,2, \ldots\right\}$, where $\varphi=\left(\varphi_{0}, \varphi_{1}\right) \in \mathbb{C}^{2}$ and where the complex square root is suitably chosen. If $z=0$, we use the continuous extension of the above expressions. The Dirichlet-to-Neumann operator is represented by the matrix
$$\Lambda(z)=\frac{\sqrt{z}}{\sin (\sqrt{z} \ell)}\left(\begin{array}{cc}
\cos (\sqrt{z} \ell) & -1 \\
-1 & \cos (\sqrt{z} \ell)
\end{array}\right)$$
with eigenvalues $-\sqrt{z} \tan (\sqrt{z} \ell / 2)$ and $\sqrt{z} \cot (\sqrt{z} \ell / 2)$. For $z=-\kappa^{2}<0(\kappa>0)$, the former eigenvalue, i.e., $\kappa \tanh (\kappa \ell / 2)$, is smaller than the latter one, i.e., $\kappa \operatorname{coth}(\kappa \ell / 2)$. The corresponding eigenvectors are (1, 1) and (-1, 1). The eigenvalues of $\Lambda(0)$ are 0 and $2 / \ell$. It follows that $\|\Gamma\|_{1 \rightarrow 0}^{2}=(\inf \sigma(\Lambda))^{-1}=(\tanh (\ell / 2))^{-1}=\operatorname{coth}(\ell / 2)(\kappa=1$; see Theorem 2.11 (ii).

The matrix $Q(z)=S(z)^{*} S(z)$ has the same eigenvectors and the eigenvalues for $z=-\kappa^{2}(\kappa>0)$ are
$$\xi_{+}^{\ell}\left(-\kappa^{2}\right)=\frac{\tanh (\kappa \ell / 2)}{2 \kappa}+\frac{\ell}{4 \cosh ^{2}(\ell \kappa / 2)} \geq \xi_{-}^{\ell}\left(-\kappa^{2}\right)=\frac{\operatorname{coth}(\kappa \ell / 2)}{2 \kappa}-\frac{\ell}{4 \sinh ^{2}(\ell \kappa / 2)}$$
with asymptotics $\xi_{+}^{\ell}(-1) \approx \ell / 2$ and $\xi_{-}^{\ell}(-1) \approx \ell / 6$ as $\ell \rightarrow 0$ and $\xi_{+}^{\ell}(-1) \rightarrow 1 / 2$ and $\xi_{-}^{\ell}(-1) \rightarrow 1 / 2$ as $\ell \rightarrow \infty$. If $z=0$, then $\xi_{+}^{\ell}(0)=\ell / 2$ and $\xi_{-}^{\ell}(0)=\ell / 6$.

We call $(\Gamma, \mathscr{G})$ the boundary pair associated with $I=[0, \ell]$ and $\partial I=\{0, \ell\}$.

\subsection*{6.2 Examples with Jacobi operators}

We present here a boundary pair which mainly serves as a "zoo" of examples in which $X=[0, \ell)$ and $Y$ is a countable subset of $X$ accumulating only at $\ell \in(0, \infty]$. It will turn out that the associated Dirichlet-to-Neumann operator (for certain real values of $z$ ) is actually a Jacobi operator in $\ell_{2}(\mathbb{N})$ acting as
$$(J \varphi)_{n}=a_{n-1} \varphi_{n-1}+b_{n} \varphi_{n}+a_{n} \varphi_{n+1}, \quad n=1,2, \ldots,$$
and $\varphi_{0}=0$. Here, $a_{n}, b_{n}$ are suitable real-valued sequences. We call $J$ the Jacobi operator associated with $\left(a_{n}\right)_{n}$ and $\left(b_{n}\right)_{n}$.

Note that if $a_{n}<0$ and $b_{n}=-\left(a_{n}+a_{n-1}\right)$, then we can interpret $J$ as a discrete weighted Laplacian with corresponding form $\langle J \varphi, \varphi\rangle=\sum_{n=1}^{\infty}\left(-a_{n}\right)\left|\varphi_{n+1}-\varphi_{n}\right|^{2}$, i.e., we can consider $-a_{n}$ as a weight of the edge from vertex $n$ to $n+1$ of the half-line graph $\mathbb{N}$. If $q_{n}:=b_{n}+a_{n}+a_{n-1} \neq 0$ then we can interpret $\left(q_{n}\right)_{n}$ as a discrete potential, and $J$ is a discrete Schrödinger operator with this potential with associated form
$$\langle J \varphi, \varphi\rangle=\sum_{n=1}^{\infty}\left(-a_{n}\right)\left|\varphi_{n+1}-\varphi_{n}\right|^{2}+\sum_{n=1}^{\infty} q_{n}\left|\varphi_{n}\right|^{2} .$$

Remark 6.6. Recently, boundary triple methods have also been used in KoM10 for the spectral analysis of Laplacians with infinitely many delta-interactions in dimension 1 which become arbitrarily close. Kostenko and Malamud couple infinitely many boundary triples to a new boundary relation (a generalisation of boundary triples, see the text after Theorem 1.20). Kostenko and Malamud provide a theory allowing them to describe self-adjoint extensions of a minimal operator of the coupled boundary relation, and these can be parametrised by Jacobi operators. Moreover, they provide conditions under which the extension is bounded from below and under which resolvent differences are in Schatten-von Neumann classes. In our context, we can understand these Laplacian with delta-interactions as Robin-type perturbations of the Neumann operator, and the Dirichlet-to-Neumann operator is then a Jacobi operator. We will not analyse such perturbations in this work, but Kostenko and Malamud's result could also be recovered by our boundary pair method. There are similar results for Dirac-type operators with infinitely many delta-interactions in dimension 1 ([CMPc13]) and also for infinitely many delta-interactions in dimension 3 ([MSch12]).

Let $I:=[0, \ell)$ for some $\ell \in(0, \infty]$ and set $\mathscr{H}:=\mathrm{L}_{2}(I)$. As quadratic form, we choose $\mathfrak{h}(f)=\left\|f^{\prime}\right\|_{\mathrm{L}_{2}(I)}^{2}$ with domain
$$\mathscr{H}^{1}:=\left\{f \in \mathrm{H}^{1}(X) \mid f(0)=0\right\} .$$
As boundary $Y$, we choose a sequence of points $\left(x_{n}\right)_{n}$ such that $x_{0}=0, \ell_{n}:=x_{n+1}-x_{n}>0$ and $\lim _{n \rightarrow \infty} x_{n}=\ell$. We set $I_{n}:=\left[x_{n}, x_{n+1}\right]$. As boundary space and operator we set $\mathscr{G}:=\ell_{2}(\mathbb{N})$ and $(\Gamma f)_{n}:=\varrho_{n}^{1 / 2} f\left(x_{n}\right)$, respectively, where $\left(\varrho_{n}\right)_{n}$ is a sequence of positive numbers. To simplify some estimates, and to assure that $(\Gamma, \mathscr{G})$ will be a boundary pair associated with $\mathfrak{h}$, we assume that there are constants $\tau_{+}, \varrho_{ \pm} \in(0, \infty)$ such that
$$\tau_{+}:=\sup _{n} \frac{\varrho_{n}}{2} \operatorname{coth}\left(\frac{\ell_{n}}{2}\right)<\infty \quad \text { and } \quad \varrho_{-} \leq \frac{\varrho_{n}}{\varrho_{n+1}} \leq \varrho_{+}$$
for all $n \in \mathbb{N}$. From the first condition we can conclude the following: since tanh $y \leq y$ for $y>0$, we have $1 / y \leq \operatorname{coth}(y / 2) / 2$ or
$$\frac{\varrho_{n}}{\ell_{n}} \leq \frac{\varrho_{n}}{2} \operatorname{coth}\left(\ell_{n} / 2\right) \leq \tau_{+} .$$
The second condition of (6.7) allows us to replace $\varrho_{n \pm 1}$ by $\varrho_{n}$ in estimates. We also set
$$\ell_{n}^{-}:=\min \left\{\ell_{n}, 1\right\}, \quad \text { hence } \tau_{+}<\infty \text { is equivalent with } \quad \sup _{n} \frac{\varrho_{n}}{\ell_{n}^{-}}<\infty .$$

Proposition 6.10. Assume that (6.7) holds then the following assertions are true:
\begin{itemize}
\item[i.] The operator $\Gamma: \mathscr{H}^{1} \longrightarrow \mathscr{G}$ is bounded and $\|\Gamma\|_{1 \rightarrow 0}^{2}=2 \tau_{+}$; moreover, $(\Gamma, \mathscr{G})$ is a boundary pair associated with $\mathfrak{h}$.
\item[ii.] The associated Neumann operator H is the Laplacian with Dirichlet condition at 0 and Neumann condition at $\ell$ (if $\ell<\infty$ ). Its spectrum is purely discrete and given by $\left\{(k+1 / 2)^{2} \pi^{2} / \ell^{2} \mid k=0,1, \ldots\right\}$ if $\ell<\infty$, and purely absolutely continuous and given by $\sigma(H)=[0, \infty)$ if $\ell=\infty$.
\item[iii.] The associated Dirichlet operator is given by $H^{\mathrm{D}}=\bigoplus_{n} \Delta_{I_{n}}^{\mathrm{D}}$, where $\Delta_{I_{n}}^{\mathrm{D}}$ denotes the Dirichlet operator on the interval $I_{n}$ acting as $\Delta_{I_{n}}^{\mathrm{D}} f=-f^{\prime \prime}$. In particular, $H^{\mathrm{D}}$ is decoupled and has spectrum
$$\left.\sigma\left(H^{\mathrm{D}}\right)=\overline{\left\{\left(k \pi / \ell_{n}\right)^{2} \mid k=1,2, \ldots,\right.} \quad n=0,1, \ldots\right\} .$$
\end{itemize}

We can omit the closure if $\ell_{n} \rightarrow 0$. If $\ell_{n} \rightarrow \infty$, then $\sigma\left(H^{\mathrm{D}}\right)=[0, \infty)$.
\begin{itemize}
\item[iv.] Assume that $0 \notin \sigma\left(H^{\mathrm{D}}\right)$, then the Dirichlet-to-Neumann operator $\Lambda(0)$ is a Jacobi operator associated with
$$a_{n}=a_{n}(0)=-\frac{1}{\ell_{n}} \cdot \frac{1}{\left(\varrho_{n} \varrho_{n+1}\right)^{1 / 2}} \quad \text { and } \quad b_{n}=b_{n}(0)=\left(\frac{1}{\ell_{n-1}}+\frac{1}{\ell_{n}}\right) \cdot \frac{1}{\varrho_{n}} .$$
\item[v.] The boundary pair is bounded iff $\inf _{n} \ell_{n}^{-} \varrho_{n}>0$. If $\lim _{n} \ell_{n}=0$, then the boundary pair is unbounded.
\item[vi.] The operator $Q$ associated with the solution form $\mathfrak{q}$ is bounded from below and above by a constant times multiplication with $\left(\ell_{n}^{-} / \varrho_{n}\right)_{n}$. In particular, the boundary pair is positive.
\item[vii.] The boundary pair is elliptically regular iff $\tau_{-}:=\inf _{n} \varrho_{n} / \ell_{n}^{-}>0$.
\end{itemize}

Proof. Let us denote the objects of the boundary pair associated with $I_{n}$ and $\left\{x_{n}, x_{n+1}\right\}$ using the subscript $(\cdot)_{I_{n}}$ (see Section 6.1).
(i) We have
$$\|\Gamma f\|^{2}=\sum_{n=1}^{\infty} \varrho_{n}\left|f\left(x_{n}\right)\right|^{2} \leq \sum_{n=1}^{\infty} \varrho_{n} \operatorname{coth}\left(\ell_{n} / 2\right)\|f\|_{\mathrm{H}^{1}\left(I_{n}\right)}^{2} \leq 2 \tau_{+}\|f\|_{\mathrm{H}^{1}(I)}^{2}$$
using the optimal bound $\left|f\left(x_{n}\right)\right|^{2} \leq \operatorname{coth}\left(\ell_{n} / 2\right)\|f\|_{\mathrm{H}^{1}\left(I_{n}\right)}^{2}$ from the two-dimensional boundary pair ( $\Gamma_{I_{n}}, \mathbb{C}^{2}$ ) in Section 6.1. That $2 \tau_{+}$is the optimal constant follows by a standard argument. Moreover, it is easily seen that $\operatorname{ker} \Gamma=\bigoplus_{n} \stackrel{\circ}{\mathrm{H}}^{1}\left(I_{n}\right)$ is dense in $\mathrm{L}_{2}(I)$ as well as ran $\Gamma$ is dense in $\ell_{2}(\mathbb{N})$ (the sequences with finite support are obviously in $\operatorname{ran} \Gamma$ ).
(ii) is obvious. (iii) The form of the associated Dirichlet operator is clear. Note that the set
$$\left\{\left(k \pi / \ell_{n}\right)^{2} \mid k=1,2, \ldots, n=0,1, \ldots\right\} \cap[0, \lambda]$$
is finite for any $\lambda>0$ if $\ell_{n} \rightarrow 0$, hence we can omit the closure in this case. If $\ell_{n} \rightarrow \infty$, then for given $\mu \geq 0$ and $\varepsilon>0$ choose $n \in \mathbb{N}$ such that $\pi / \ell_{n}<\varepsilon$. Now choose $k \in \mathbb{N}$ such that $k \pi / \ell_{n} \leq \mu<(k+1) \pi / \ell_{n}$. Clearly, $\left|\mu-k \pi / \ell_{n}\right|<\varepsilon$, hence $\bigcup_{n} \sqrt{\sigma(\Delta)_{I_{n}}^{\mathrm{D}}}$ is dense in $[0, \infty)$. As $\mu \mapsto \mu^{2}$ is a homeomorphism of $[0, \infty)$ the result follows.
(iv) The Dirichlet solution operator is given as follows: Let $h=S(z) \varphi$ for $\varphi \in \mathscr{G}^{1 / 2}$. Then $h_{n}:=h \upharpoonright_{I_{n}}=S_{I_{n}}(z) \Phi_{n}$, where $\Phi_{n}=\left(\widetilde{\varphi}_{n}, \widetilde{\varphi}_{n+1}\right)$ and $\widetilde{\varphi}_{n}=\varrho_{n}^{-1 / 2} \varphi_{n}$. Moreover, the Dirichlet-to-Neumann operator is given by
$$\begin{aligned}
\langle\Lambda(z) \varphi, \varphi\rangle_{\ell_{2}(\mathbb{N})} & =(\mathfrak{h}-z \mathbf{1})(S(z) \varphi, S \varphi)=\sum_{n=0}^{\infty}\left(\mathfrak{h}_{I_{n}}-z \mathbf{1}\right)\left(S_{I_{n}}(z) \Phi_{n}, S_{I_{n}} \Phi_{n}\right) \\
& =\sum_{n=0}^{\infty}\left\langle\Lambda_{I_{n}}(z) \Phi_{n}, \Phi_{n}\right\rangle_{\mathbb{C}^{2}}=\sum_{n=1}^{\infty}\left(a_{n-1}(z) \varphi_{n-1}+b_{n}(z) \varphi_{n}+a_{n}(z) \varphi_{n+1}\right) \overline{\varphi_{n}}
\end{aligned}$$
for suitable $\varphi \in \mathscr{G}^{1 / 2}$, where
$$a_{n}(z)=-\frac{\sqrt{z}}{\sin \left(\sqrt{z} \ell_{n}\right)} \cdot \frac{1}{\left(\varrho_{n} \varrho_{n+1}\right)^{1 / 2}} \quad \text { and } \quad b_{n}(z)=\sqrt{z}\left(\cot \left(\sqrt{z} \ell_{n-1}\right)+\cot \left(\sqrt{z} \ell_{n}\right)\right) \cdot \frac{1}{\varrho_{n}}$$
(see (6.2)). The formula for $z=0$ follows by taking $z \rightarrow 0$.
(v) The boundary pair is bounded iff $\Lambda$ is bounded (see Theorem 2.11 (iii)); and the Jacobi operator $\Lambda$ is bounded iff the Jacobi sequences $\left(a_{n}(-1)\right)_{n}$ and $\left(b_{n}(-1)\right)_{n}$ are both bounded. Since $1 / \sinh \ell_{n} \leq \operatorname{coth}\left(\ell_{n}\right)$ and using the second condition of (6.7), we see that both Jacobi sequences are bounded iff $\left(b_{n}(-1)\right)_{n}$ is bounded, i.e., iff $\sup p_{n}\left(\operatorname{coth} \ell_{n}\right) / \varrho_{n}<$ $\infty$, hence $\operatorname{iff}_{i} \inf _{n} \ell_{n}^{-} \varrho_{n}>0$.

Since $\ell_{n} \varrho_{n} \leq \tau_{+} \ell_{n}^{2}$ by (6.8), we have that $\lim _{n} \ell_{n}=0$ implies $\ell_{n}^{-}=\ell_{n}$ eventually and $\inf _{n} \ell_{n}^{-} \varrho_{n}=0$, i.e., the boundary pair is not bounded.
(vi) and (vii): The solution form is given by
$$\mathfrak{q}(\varphi)=\|S \varphi\|_{\mathrm{L}_{2}(I)}^{2}=\sum_{n=0}^{\infty}\left\|S_{I_{n}} \Phi_{n}\right\|_{\mathrm{L}_{2}\left(I_{n}\right)}^{2}=\sum_{n=0}^{\infty}\left\langle Q_{I_{n}}(-1) \Phi_{n}, \Phi_{n}\right\rangle_{\mathbb{C}^{2}}$$
and this is bounded from above and below by $\left(1+\varrho_{ \pm}\right) \sum_{n=0}^{\infty}\left|\varphi_{n}\right|_{\mathbb{C}^{2}}^{2} \xi_{ \pm}^{\ell_{n}}(-1) / \varrho_{n}$ using (6.3) of Section 6.1 and (6.7). Since $\xi_{ \pm}^{\ell}(-1)$ is of order $\ell$ as $\ell \rightarrow 0$ and $\xi_{ \pm}^{\ell}(-1) \rightarrow 1 / 2$ as $\ell \rightarrow \infty$, we can bound $\mathfrak{q}(\varphi)$ from below and above by multiplying with $\left(\ell_{n}^{-} / \varrho_{n}\right)_{n}$.
(vi) In particular, we can bound $\mathfrak{q}(\varphi)$ from below by a positive constant times $\left(\inf _{n} \ell_{n}^{-} / \varrho_{n}\right)\|\varphi\|_{\ell_{2}(\mathbb{N})}^{2}$. But $\inf _{n} \ell_{n}^{-} / \varrho_{n}>$ 0 by (6.9), hence the boundary pairs positive.
(vii) Similarly, $\mathfrak{q}(\varphi)=\|S \varphi\|^{2}$ is bounded from above by a constant times $\left(\sup _{n} \xi_{+}^{\ell_{n}}(-1) / \varrho_{n}\right)\|\varphi\|_{\ell_{2}(\mathbb{N})}^{2}$. Since $\xi_{+}^{\ell}(-1)$ has the same behaviour as $\xi_{-}^{\ell}(-1)$ for $\ell \rightarrow 0$ and $\ell \rightarrow \infty$, the solution form $\mathfrak{q}$ is bounded iff $\sup _{n} \ell_{n}^{-} / \varrho_{n}<\infty$. \(\square\)

Let us now provide a list of examples:
Example 6.12 (Unbounded, positive and elliptically regular boundary pair). Let $\ell_{n}$ and $\varrho_{n}$ be of the same order $\left(0<\tau_{-} \leq \varrho_{n} / \ell_{n} \leq \tau_{+}<\infty\right)$ and $\lim _{n} \ell_{n}=0$, then $\ell_{n}^{-}=\ell_{n}$ eventually and the boundary pair is unbounded and elliptically regular (and of course positive), see Proposition 6.10 (v)-(vii). The Neumann operator in this case has purely discrete spectrum iff $\sum_{n} \ell_{n}<\infty$.

This example shows that the spectral characterisation in Theorem 4.14 (iv) can be actually used in a slightly wider class than ordinary boundary triples (see Theorem 1.20).

Example 6.13 (Not elliptically regular, positive boundary pair). If $\left(\ell_{n}\right)_{n}$ and $\left(\varrho_{n}\right)_{n}$ are chosen such that we have $\sup _{n} \varrho_{n} / \ell_{n}<\infty$, but $\inf _{n} \varrho_{n} / \ell_{n}=0$, then the boundary pair is not elliptic (in particular not bounded). For example, if $\varrho_{n}=q^{n}(0<q<1)$ or $\varrho_{n}=n^{-\gamma}$ and $\ell_{n}=n^{-\beta}, \gamma>\beta>0$, then the boundary pair is not elliptic.

For further examples, let us specify $\ell_{n}=n^{-\beta}$ and $\varrho_{n}=n^{-\gamma}$ with $\beta \leq \gamma$ and $\gamma \geq 0$. In particular, (6.7) is then fulfilled and $(\Gamma, \mathscr{G})$ is a boundary pair by Proposition 6.10 (i). It is now a straightforward calculation using (6.11) to see that
$$-a_{n}(z)=\frac{n^{\gamma} \sqrt{z}}{\sin \left(n^{-\beta} \sqrt{z}\right)}(1+\mathrm{o}(1)) \sim\left\{\begin{array}{ll}
n^{\alpha}, & \beta \geq 0, \quad z \in \mathbb{C} \backslash \sigma\left(H^{\mathrm{D}}\right), \\
n^{\gamma} \mathrm{e}^{-n^{-\beta}}, & \beta<0, \quad z=-1,
\end{array} \quad \alpha:=\beta+\gamma,\right.$$
(where $a_{n} \sim b_{n}$ means that $a_{n} / b_{n}$ is bounded from above and below by positive constants) and
$$q_{n}(z)=b_{n}(z)+a_{n}(z)+a_{n-1}(z) \sim\left\{\begin{array}{lll}
n^{\alpha-1}, & \beta \geq 1 / 2, & z \in \mathbb{C} \backslash[0, \infty), \\
& \text { or } \beta>0, & z=0, \\
(-2 z) n^{\alpha-2 \beta}+\beta n^{\alpha-2 \beta-1}, & 0<\beta<1 / 2, & z \in \mathbb{C} \backslash \sigma\left(H^{\mathrm{D}}\right), \\
n^{\alpha-\beta}=n^{\gamma}, & \beta \leq 0, & z<0 .
\end{array}\right.$$
Moreover, the squared norm of $\mathscr{G}^{1 / 2}$ is equivalent with
$$\|\varphi\|_{\mathrm{h}^{1}(\mathbb{N}, r, w)}^{2}:=\sum_{n \in \mathbb{N}}\left(\left|(\mathrm{~d} \varphi)_{n}\right|^{2} r_{n}+\left|\varphi_{n}\right|^{2} w_{n}\right) \quad \text { with } \quad r_{n}=-a_{n}(-1), \quad w_{n}=q_{n}(-1),$$
where $(\mathrm{d} \varphi)_{n}=\varphi_{n+1}-\varphi_{n}$ is the discrete derivative.
Example 6.15 (Dirichlet-to-Neumann form unbounded from both sides). For a non-elliptically regular boundary pair, the Dirichlet-to-Neumann form can be unbounded from both sides: let $\ell_{n}=n^{-\beta}$ and $\varrho_{n}=n^{-\gamma}$ with $\gamma>\beta>0$ and $0<\beta<1 / 2$, and let $z \in(0, \infty) \backslash \sigma\left(H^{\mathrm{D}}\right)$ : Since the boundary pair is not bounded, $\mathfrak{l}_{\lambda}$ is not bounded from above. To see that $\mathfrak{l}_{z}$ is not bounded from below, take $\varphi^{k}=\left(\varphi_{n}^{k}\right)_{n}$ with $\varphi_{n}^{k}=1$ if $1 \leq n \leq k$ and 0 otherwise. Then, using the asymptotics stated above, we obtain
$$\mathfrak{l}_{z}\left(\varphi^{k}\right)=\sum_{n \in \mathbb{N}}\left(-a_{n}(z)\left|\varphi_{n+1}^{k}-\varphi_{n}^{k}\right|^{2}+q_{n}(z)\left|\varphi_{n}^{k}\right|^{2}\right) \sim k^{\alpha}-2 z \sum_{n=1}^{k} n^{\alpha-2 \beta} .$$

Since $0<\beta<1 / 2$, the second sum, of order $k^{\alpha-2 \beta+1}$, is dominant, and negative. Moreover, $\left\|\varphi^{k}\right\|_{\mathscr{G}}^{2}=k$, and therefore $\left.\mathfrak{l}_{\lambda}\left(\varphi^{k}\right) /\left\|\varphi^{k}\right\|_{\mathscr{G}}^{2} \sim-z k^{\alpha-2 \beta}\right) \rightarrow-\infty$ as $k \rightarrow \infty$. In particular, we have shown that $\mathfrak{l}_{\lambda}$ is neither bounded from above nor from below (see also Remark 2.28 (ii)).

Let us now have another choice for $\left(\ell_{n}\right)_{n}$ and $\left(\varrho_{n}\right)_{n}$. In particular, we want the corresponding Jacobi coefficients to have the form $a_{n}=a_{n}(0)=-n^{\alpha}$ and $b_{n}=b_{n}(0)=-\left(a_{n}+a_{n-1}\right)$. Then the corresponding Jacobi operator $J=\Lambda(0)$ is a pure (discrete) Laplacian, while for other values $\lambda \in \mathbb{R} \backslash \sigma\left(H^{\mathrm{D}}\right), \Lambda(\lambda)$ is a discrete Schrödinger operator with an additional potential of order $-\lambda \ell_{n} / \varrho_{n}$ (and this is of order $-\lambda n^{\alpha-2 \beta}$, see below), hence unbounded if $\alpha-2 \beta=\gamma-\beta>0$. Therefore, we have another example where the form $\mathfrak{l}_{0}$ is not closed on $\mathscr{G}^{1 / 2}$ but only on a larger space $\mathscr{G}_{0}^{1 / 2} \supsetneq \mathscr{G}^{1 / 2}$.

We use the ansatz $\ell_{n}=n^{-\beta} L_{n}^{-1}$ and $\varrho_{n}=n^{-\gamma} R_{n}^{-1}$ with $\alpha=\beta+\gamma>0$ and $\gamma>\beta$. It can then be shown that for $a_{n}=n^{\alpha}$ and $b_{n}=-\left(a_{n}+a_{n-1}\right)$ the sequences $\left(L_{n}\right)_{n}$ and $\left(R_{n}\right)_{n}$ defined above actually converge to 1 as $n \rightarrow \infty$.

This ansatz allows us to use known results on the spectrum of this special Jacobi operator (see e.g. [Sa08, Thm 1.1] and references therein; as well as [JN01] for the case $\alpha=1$ and the general ideas of the spectral analysis). The spectrum of $J$ is purely discrete if $\alpha>2$, and absolutely continuous if $0<\alpha \leq 2$. If $\alpha<2$ then $\sigma(J)=[0, \infty)$ and if $\alpha=2$ then $\sigma(J)=[1 / 4, \infty)$. In the latter case $(\alpha=2)$, the spectrum is purely absolutely continuous.

Example 6.16 (Counterexamples to the compactness). Here, we show that $R$ can be non-compact, while $R^{\mathrm{D}}$ is compact and $\Lambda(0)^{-1}$ can be either compact or non-compact.

If we choose $\gamma \geq \beta=1$ then the Neumann operator $H$ has purely absolutely continuous spectrum $[0, \infty)$ since $\sum_{n} \ell_{n}=\infty$, while the Dirichlet operator $H^{\mathrm{D}}$ has purely discrete spectrum.

If $\gamma>\beta=1$, i.e., if $\alpha=\beta+\gamma>2$ then the Dirichlet-to-Neumann operator $\Lambda(0)=J$ has purely discrete spectrum. By the monotonicity (Theorem 2.23 (v)), $0 \leq \mathfrak{l}_{0} \leq \mathfrak{l}=\mathfrak{l}_{-1}$, and this inequality remains true for the closure of the form $\mathfrak{l}_{0}$ (see [Da95, Sec. 4.4] for an order of quadratic forms). In particular, the associated non-negative operators fulfil $0 \leq \Lambda(0) \leq \Lambda=\Lambda(-1)$, hence $\Lambda(0)^{-1} \geq \Lambda^{-1} \geq 0$, and $\Lambda^{-1}$ is also compact. In this case, the boundary pair is not elliptically regular, and Theorem 4.14 (ii) is no longer true, as $\Gamma: \mathscr{H}^{1} \longrightarrow \mathscr{G}$ is compact by Theorem 2.36, but $\sigma_{\text {ess }}(H)=[0, \infty) \neq \emptyset=\sigma_{\text {ess }}\left(H^{\mathrm{D}}\right)$.

If $\gamma=\beta=1$, then $\alpha=2$ and the Dirichlet-to-Neumann operator $\Lambda(0)$ has purely absolutely continuous spectrum $[1 / 4, \infty)$. The boundary pair then is elliptically regular.

Example 6.17 (Example violating the spectral relation Theorem 4.14 (i)). Choose $0<\beta<1 / 2$ and $\gamma=2-\beta>0$. Then $\alpha=2$, and $\sigma(\Lambda(0))=[1 / 4, \infty)$, but the spectrum of the Neumann operator is $[0, \infty)$ (and purely absolutely continuous, see Proposition 6.10 (ii)); the Dirichlet spectrum is again discrete. In particular, the implication " $0 \in$ $\sigma(H) \Rightarrow 0 \in \sigma(\Lambda(0))$ " is not true (note that $0 \notin \sigma\left(H^{\mathrm{D}}\right)$ ). Since $\beta<\gamma$, the boundary pair is not elliptic. It can be seen as in Example 6.15 that $\mathfrak{l}_{\lambda}$ is even unbounded from below for all $\lambda>0$ (not in the Dirichlet spectrum).

Let us illustrate what goes wrong in the proof of Theorem 4.14 (i): We argued by contraposition, so our assumption is $0 \notin \sigma(\Lambda(0))$ (which is true here). In order to show that $0 \notin \sigma(H)$, we would have to show that $D(z):=$ $S(z) \Lambda(z)^{-1} S(\bar{z})^{*}$ is holomorphic in $z=0$ as function with values in $\mathscr{B}(\mathscr{G})$. But $D(0)$ is not bounded, as we need to use the weak version of $\Lambda(z)^{-1}$.

Example 6.18 (Example violating the spectral relation Theorem 4.14 (iv)). We can actually modify Example 6.17 such that the implication " $0 \in \sigma_{\text {disc }}(\Lambda(0)) \Rightarrow 0 \in \sigma_{\text {disc }}(H)$ " is false, although the boundary pair is positive (but not elliptically regular): Take the direct sum $(\Gamma, \mathscr{G})$ (see Section 5.3) of the boundary pair of the previous example (denoted now $\left(\Gamma_{1}, \mathscr{G}_{1}\right)$ ) and any boundary pair $\left(\Gamma_{2}, \mathscr{G}_{2}\right)$ such that 0 is a simple and isolated eigenvalue in $\sigma\left(\Lambda_{2}(0)\right)$ and $\sigma\left(H_{2}\right)$ (e.g., the boundary pair on $[0,1]$ as in Section 6.1). Then 0 is a discrete eigenvalue of $\sigma(\Lambda(0))=\sigma\left(\Lambda_{1}(0)\right) \cup \sigma\left(\Lambda_{2}(0)\right)$, but 0 is not isolated in $\sigma(H)=\sigma\left(H_{1}\right) \cup \sigma\left(H_{2}\right)=[0, \infty)$.

\subsection*{6.3 Laplacian on Lipschitz domains}

We consider now a compact $d$-dimensional Riemannian manifold $X$ with its natural $d$-dimensional volume measure $\mu$. Moreover, we assume that $X$ has a Lipschitz boundary $Y=\partial X$ in the following sense: let $\widetilde{X}$ be a complete smooth Riemannian manifold. A (smooth) manifold with Lipschitz boundary or a Lipschitz domain $X$ in $\widetilde{X}$ is the closure $X$ of an open subset of $\widetilde{X}$ such that $\partial X$ can locally be written as graph of a Lipschitz function (for details see MiT99, App. A]). It can be shown that $\partial X$ has a natural measure $\nu$, the $(d-1)$-dimensional Hausdorff measure.

Remark 6.19. A manifold with Lipschitz boundary $X$ is locally $\mathrm{C}^{\infty}$-diffeomorphic with the set below the graph of a Lipschitz function, hence all results on Lipschitz domains in $\mathbb{R}^{d}$, which are invariant under such diffeomorphisms, remain true on a smooth manifold with Lipschitz boundary. If we choose the half-space $\mathbb{R}^{d-1} \times \mathbb{R}$ as local model space (i.e., if $X$ has a local parametrisation into the half-space), the transition functions are only bi-Lipschitz. Therefore, we can only carry over results for smooth boundaries onto smooth manifolds with Lipschitz boundary which are invariant under bi-Lipschitz transformations.

The boundary $\partial X$ is only a Lipschitz manifold, i.e., the transition maps are only bi-Lipschitz functions, and no longer smooth. A very nice introduction to Lipschitz manifolds (and even differential forms in this context) is given in [MiMiT01, App. A] (we refer also to the discussion in [Gv85, Sec. 1.2.1]).

Denote by $\mathrm{C}^{\infty}(X)$ the space of functions, which are smooth on the interior $\stackrel{\circ}{X}:=X \backslash \partial X$ such that all derivatives extend continuously onto $X$. We set $\mathscr{H}:=\mathrm{L}_{2}(X)$ (with respect to the volume measure $\mu$ ). Moreover, $\mathscr{H}^{1}:=\mathrm{H}^{1}(X)$ denotes the completion of $\mathrm{C}^{\infty}(X)$ with respect to the norm given by $\|u\|_{\mathrm{H}^{1}(X)}^{2}:=\|u\|_{\mathrm{L}_{2}(X)}^{2}+\|\mathrm{d} u\|_{\mathrm{L}_{2}(X)}^{2}$, where $\mathrm{d} u$ denotes the exterior derivative of $u$. We consider the form $\mathfrak{h}$ given by $\mathfrak{h}(u):=\|\mathrm{d} u\|^{2}, u \in \mathscr{H}^{1}$.

We set $\mathscr{G}:=\mathrm{L}_{2}(Y)$ (with respect to the $(d-1)$-dimensional Hausdorff measure $\nu$ on $Y=\partial X$ ). Moreover, for smooth functions $u$ we set $\Gamma u:=u \upharpoonright_{\partial X}$. For the definition of fractional Sobolev spaces $\mathrm{H}^{s}(\partial X)(0 \leq s \leq 1)$, see e.g. [Gv85, Sec. 1.3.3] or [GeMi09, App. A]).

Our main result here is the following:
Theorem 6.20. The boundary pair $(\Gamma, \mathscr{G})$ associated with the quadratic form $\mathfrak{d}$ is unbounded with $\mathscr{G}^{1 / 2}=\mathrm{H}^{1 / 2}(\partial X)$, elliptically regular and not positive. The Dirichlet and Neumann operators $H^{\mathrm{D}}$ and $H$ are the usual Dirichlet and Neumann Laplacians $\Delta_{X}^{\mathrm{D}}$ and $\Delta_{X}^{\mathrm{N}}$ on $X$, respectively (with the sign convention $\Delta_{X}^{\mathrm{D}}, \Delta_{X}^{\mathrm{N}} \geq 0$ ). Moreover, the Dirichlet-to-Neumann operator $\Lambda(z)\left(z \notin \sigma\left(\Delta^{\mathrm{D}}\right)\right)$ has the usual interpretation, i.e., $\psi=\Lambda(z) \varphi$ iff $\psi$ is the normal derivative of the solution of the Dirichlet problem $(\Delta-z) h=0$ and $h \upharpoonright_{\partial X}=\varphi$ (provided $\varphi$ is smooth enough). Finally, $H, H^{\mathrm{D}}$ and $\Lambda(z)$ all have compact resolvents.

Proof. For the boundedness of $\Gamma: \mathrm{H}^{1}(X) \longrightarrow \mathrm{L}_{2}(\partial X)$, note that $\mathrm{H}^{1}(X)$ and $\mathrm{L}_{2}(\partial X)$ are both invariant under bi-Lipschitz transformations, hence the boundedness follows from the corresponding result for smooth boundaries. Moreover, smooth functions with support away from $\partial X$ are in $\operatorname{ker} \Gamma=: \stackrel{\circ}{\mathrm{H}}^{1}(X)$, and also dense in $\mathscr{H}=\mathrm{L}_{2}(X)$, hence $\operatorname{ker} \Gamma$ is dense in $\mathscr{H}$. In addition, $\Gamma\left(\mathrm{C}^{\infty}(X)\right)$ is dense in $\mathrm{L}_{2}(\partial X)$. In particular, $(\Gamma, \mathscr{G})$ is a boundary pair. It is also well-known, that the range of the Sobolev trace map $\Gamma$ is $\mathrm{H}^{1 / 2}(\partial X) \subsetneq \mathrm{L}_{2}(\partial X)$ (see e.g. [Gv85, Thm. 1.5.1.3]), hence the boundary pair is unbounded.

In order to show the elliptic regularity, we have to check that the solution operator $S: \mathrm{H}^{1 / 2}(\partial X) \longrightarrow \mathrm{H}^{1}(X)$ extends to the corresponding $\mathrm{L}_{2}$-spaces, i.e., to
$$\bar{S}: \mathrm{L}_{2}(\partial X) \longrightarrow \mathrm{L}_{2}(X) ;$$
for Lipschitz domains in Riemannian manifolds, this has been shown in [MiT03, Thm. 4.1] (see also [MiT05, Prop. 3.7 and its proof]).

If the boundary pair was positive, then $S: \mathscr{G}^{1 / 2} \longrightarrow \mathscr{N}^{1}$ would extend to a topological isomorphism $\bar{S}: \mathscr{G} \longrightarrow \mathscr{N}^{0}$ by Remark 3.6 (ii) and Theorem 3.17 (iii), where $\mathscr{N}^{0}$ is the closure of $\mathscr{N}^{1}$ in $\mathscr{H}$. It can be seen that $\mathscr{N}^{0}=$ $\operatorname{ker}\left(H^{\max }+1\right)$, where $H^{\max }=\Delta^{\max }$ is the Laplacian in the distributional sense ( $u \in \operatorname{dom} \Delta^{\max }$ iff $u$ and $\Delta^{\max } u$ are in $\mathrm{L}_{2}(X)$ ). In particular, any $h=\bar{S} \varphi \in \operatorname{ker}\left(H^{\text {max }}+1\right)$ would have a boundary value $\varphi \in \mathrm{L}_{2}(Y)$ which is known not to be true.

The compactness of the resolvents is a standard fact for (pseudo-)differential operators on compact manifolds. \(\square\)

We call $(\Gamma, \mathscr{G})$ the boundary pair associated with the manifold $X$ and boundary $\partial X$.
Remark 6.22. Note that in the context of non-smooth domains, questions of regularity for the operator are rather delicate. For more details on Sobolev spaces and elliptic boundary value problems on Lipschitz domains we refer e.g. to [JeKe95, MiT99, MiMiT01, MiT03, MiT05, GeMi09, GeMi11, BeM14] and references therein. Our approach only needs the first order spaces, as we only have to check that the solution operator extends to an operator on the corresponding $\mathrm{L}_{2}$-spaces, and we believe that this is generally simpler to check. In this context, the solution operator (at $z=0$ ) is also called Poisson operator.

Remark 6.23. The notion "elliptically regular" for a boundary pair has its motivation from this manifold example: The boundary triple $\left(\Gamma, \Gamma^{\prime}, \mathscr{G}\right)$ associated with the boundary pair $(\Gamma, \mathscr{G})$ (see Section 1.4) is called elliptically regular if $\operatorname{dom} H^{\mathrm{D}} \subset \mathscr{W}$ and $\operatorname{dom} H \subset \mathscr{W}$ (in [P12, Def. 3.4.21] we actually used additional assumptions about the range of the boundary maps $\Gamma$ and $\Gamma^{\prime}$ ); and a (maximal) boundary triple is elliptically regular iff the corresponding boundary pair is. Here, $\mathscr{W}$ is a space on which $\Gamma^{\prime}$ is defined and bounded $\left(\Gamma^{\prime}: \mathscr{W} \longrightarrow \mathscr{G}\right)$ and on which Green's identity (1.14) holds. If we assume (for simplicity) that $\partial X$ is smooth then we can choose $\mathscr{W}=\mathrm{H}^{2}(X)$. The condition $\operatorname{dom} H^{\mathrm{D}} \subset \mathscr{W}$ is then equivalent to an "elliptic regularity estimate"
$$\|u\|_{\mathrm{H}^{2}(X)} \leq C\left(\|u\|_{\mathrm{L}_{2}(X)}+\left\|\Delta_{X}^{\mathrm{D}} u\right\|_{\mathrm{L}_{2}(X)}\right)$$
for all $u \in \operatorname{dom} \Delta_{X}^{\mathrm{D}} \cap \mathrm{H}^{2}(X)$ and similarly for the Neumann operator $H=\Delta_{X}^{\mathrm{N}}$.
Moreover, we have indicated in Remark 1.11 that a boundary pair is elliptically regular iff a "normal derivative" $\Gamma^{\prime}$ can be defined such that Green's identity (1.14) holds and such that $\Gamma^{\prime} u \in \mathscr{G}$ for all $u \in \operatorname{dom} H^{\mathrm{D}}$. We will treat such questions, namely boundary triples associated with quadratic forms and the relation with boundary pairs in a forthcoming publication [P] (see also [P12, Sec. 3.4]).

Krein's resolvent formula now is valid for the Neumann and Dirichlet Laplacian, i.e.,
$$\left(\Delta_{X}^{\mathrm{N}}-z\right)^{-1}-\left(\Delta_{X}^{\mathrm{D}}-z\right)^{-1}=\bar{S}(z) \Lambda(z)^{-1} \bar{S}(\bar{z})^{*},$$
Moreover, the (extension of the) solution operator $\bar{S}(z): \mathrm{L}_{2}(\partial X) \longrightarrow \mathrm{L}_{2}(X)$ is usually called Poisson operator in this context. In addition, we have the characterisation of the spectrum
$$\lambda \in \sigma\left(\Delta^{\mathrm{N}}\right) \quad \Leftrightarrow \quad 0 \in \sigma(\Lambda(\lambda))$$
provided $\lambda \notin \sigma\left(\Delta^{\mathrm{D}}\right)$. Since the spectrum of $\Delta^{\mathrm{N}}$ is purely discrete, and since $\Gamma: \mathrm{H}^{1}(X) \longrightarrow \mathrm{L}_{2}(\partial X)$ is a compact operator, the spectra of $\Delta^{\mathrm{D}}$ and $\Lambda(\lambda)$ are purely discrete, too (see Proposition 5.2 (vi) and Theorem 2.36). Moreover, the multiplicities of the eigenvalues are preserved (Theorem 4.11).

Remark 6.27. Most of our results extend to the case when $X$ is non-compact but $\partial X$ is compact, e.g. products (see Section 6.4 and also Remark 6.28) or warped products $X=[0, \infty) \times Y$ with metric $g=\mathrm{d} s^{2}+r(s)^{2} h$, where $(Y, h)$ is a compact Riemannian manifold. The only problem here is that the essential spectra of the Dirichlet and Neumann operator are the same (Theorem 4.14 (ii)), and in many cases just the entire half-axis $[0, \infty)$. Nevertheless, the Dirichlet-to-Neumann operator might be extended analytically into $[0, \infty)$; we come back to this situation in a forthcoming publication.

Let us illustrate how coupling of boundary pairs can be used in the manifold case
Remark 6.28. A prominent example of a coupled boundary pair (see Section 5.2) we have in mind is a smooth manifold $X=X_{1} \cup X_{2}$ without boundary such that $Y=X_{1} \cap X_{2}$ is a smooth submanifold of co-dimension 1, $X_{1}$ is a compact manifold with boundary $Y$ and $X_{2}=I \times_{r} Y$ is a warped product over an interval $I$, i.e., a manifold with metric $g=\mathrm{d} s^{2}+r(s)^{2} h(r: I \longrightarrow(0, \infty), h$ a metric on $Y$ ). For a warped product, we have explicit formulae for the solution and the Dirichlet-to-Neumann operators (in terms of solutions of some ODEs related with $r$ ). As boundary pairs we now choose $\left(\Gamma_{i}, \mathscr{G}\right)$ associated with the quadratic forms $\mathfrak{h}_{i}(u)=\|\mathrm{d} u\|_{X_{i}}^{2}, u \in \mathscr{H}_{i}{ }^{1}=\mathrm{H}^{1}\left(X_{i}\right)$, where $\mathscr{G}=\mathrm{L}_{2}(Y)$ and $\Gamma_{i} u=u \upharpoonright_{Y}$. The coupled form and operator (i.e., the Neumann operator) is now the form and Laplacian on the entire manifold $X$. Moreover, for the boundary pairs $\left(\Gamma_{1}, \mathscr{G}\right)$ on the compact part of the manifold one can derive explicit formulae for the Dirichlet solution operators and Dirichlet-to-Neumann maps, as well as for the (possibly non-compact) warped product. Hence we have rather explicit formulae for the resolvent of the entire Laplacian on $X$ in terms of simpler building blocks. We will come back to these ideas, treating also more complicated coupled structures, in a forthcoming publication.

\section*{Regularisation of the manifold boundary pair}

Example 6.29 (A bounded, but not positive boundary pair). Let $(\widetilde{\Gamma}, \widetilde{\mathscr{G}})$ be the bounded modification or regularisation of the above boundary pair $(\Gamma, \mathscr{G})$ associated with $X$ (see Section 5.4): it follows from Proposition 5.9 that $(\widetilde{\Gamma}, \widetilde{\mathscr{G}})$ is not positive, although bounded.

Example 6.30 (Non-compact Dirichlet-to-Neumann, but compact Dirichlet and Neumann operator). If we assume (with the notation of the previous example) that the manifold $X$ is compact, then $\widetilde{R}^{\mathrm{D}}=R$ and $\widetilde{R}^{\mathrm{D}}=R^{\mathrm{D}}$ are compact. But since $\widetilde{\Lambda}=\operatorname{id}_{\widetilde{\mathscr{G}}}$ and since $\widetilde{\mathscr{G}}=\mathrm{H}^{1 / 2}(\partial X)$ is infinite-dimensional, $\widetilde{\Lambda}^{-1}$ is not compact.

\subsection*{6.4 Laplacian on a non-compact cylindrical manifold}

Let us consider here a simple example in which the space $X$ is a product manifold $X=[0, \infty) \times Y$ with corresponding product metric $g=\mathrm{d} s^{2}+h$, where ( $Y, h$ ) is a compact Riemannian manifold without boundary. Similar cases were considered e.g. in [GG91, Sec. 2.5] or [DHMdS06, Ex. 6.8].

In this case, we have again $\mathscr{H}=\mathrm{L}_{2}(X), \mathscr{H}^{1}=\mathrm{H}^{1}(X), \mathfrak{h}(u)=\|\mathrm{d} u\|^{2}$ and $\mathscr{G}=\mathrm{L}_{2}(Y, h)$. Identifying a function $u: X \longrightarrow \mathbb{C}$ with the corresponding vector-valued function $s \mapsto u(s)$ on $[0, \infty)$, we set $\Gamma u=u(0), u \in \mathscr{H}^{1}$. It can be seen similarly as before that $\Gamma$ is bounded and that $(\Gamma, \mathscr{G})$ is an unbounded, elliptically regular, but not positive boundary pair.

This example can be seen as a vector-valued version of the interval case in Section 6.1 (except that $I=[0, \infty)$ is non-compact here and has only one boundary point). Namely, we can write
$$\mathfrak{h}(u)=\int_{I}\left(\left\|u^{\prime}(s)\right\|_{\mathrm{L}_{2}(Y, h)}^{2}+\left\|\mathrm{d}_{Y} u(s)\right\|_{\mathrm{L}_{2}(Y, h)}^{2}\right) \mathrm{d} s,$$
where $\mathrm{d}_{Y} \varphi$ denotes the exterior derivative on $Y$. Moreover, all objects can be calculated rather explicitly using separation of variables (denoting the eigenvalues and eigenfunctions of the Laplacian on $Y$ by $\kappa_{k} \geq 0$ and $\Phi_{k}$, respectively). For example, we have
$$S(z) \varphi=\sum_{k} f_{z, k} \otimes \Phi_{k}$$
where $f_{k, z}(s)=\exp \left(\mathrm{i} s \sqrt{z-\kappa_{k}}\right)$ (the square root is cut along the positive real line). Moreover,
$$\Lambda(z) \varphi=\sum_{k}\left\langle\varphi, \Phi_{k}\right\rangle_{\mathrm{L}_{2}(Y, h)} f_{z, k} \otimes \Phi_{k}=-\mathrm{i}\left(\sqrt{z-\Delta_{Y}}\right) \varphi$$
(see [P12, Sec. 3.5] for details, e.g., the type of convergence of the sums). In particular, for $z=-1$ we have $\Lambda=\sqrt{\Delta_{Y}+1}$.

Similarly, we can treat more general cases like warped products (i.e., $X=I \times Y$ with metric $g=\mathrm{d} s^{2}+r(s)^{2} h$ for some function $r: I \longrightarrow(0, \infty))$. We will come back to this point in a forthcoming publication.

Example 6.31 ( $R, R^{\mathrm{D}}$ non-compact, $\Lambda^{-1}$ compact). The compactness of $\Lambda^{-1}$ does not imply the compactness of $R$ : In the example above, the Neumann and Dirichlet operators are the Laplacians on the non-compact cylinder $X=\mathbb{R}_{+} \times Y$ with Neumann resp. Dirichlet conditions at $\partial X=\{0\} \times Y$, hence their resolvents are not compact. On the other hand, $\Lambda^{-1}=\left(\Delta_{Y}+1\right)^{-1 / 2}$ is compact.

Example 6.32 ( $R, R^{\mathrm{D}}$ non-compact, $\Lambda^{-1}$ non-compact). If we take the bounded modification of the above example, we obtain the case where none of the operators $R, R^{\mathrm{D}}$ and $\Lambda^{-1}\left(=\mathrm{id}_{\widetilde{\mathscr{G}}}\right)$ is compact.

\subsection*{6.5 Dirichlet-to-Neumann operator supported on a metric graph: leaky graphs and photonic crystals}

Let us consider here a case of a Dirichlet-to-Neumann operator defined on a singular space $Y$, where $Y$ is a metric graph embedded in a 2-dimensional Riemannian manifold $X$, i.e., $Y=\bigcup_{e \in E} Y_{e}$, and each $Y_{e}$ is a closed one-dimensional (smooth) submanifold in $X$, called edge segment. We assume for simplicity that $X$ is compact, but under suitable uniformity assumptions the results below remain true; e.g. if $X$ is a covering manifold with compact quotient.

We call the closure of each connected component of $X \backslash Y$ a face of $Y$ in $X$, and label the faces by $\left(X_{f}\right)_{f \in F}$. We assume that each face is compact in $X$, and that the boundary of each face, consisting of the adjacent edges $E_{f}$, is Lipschitz (if $X$ is non-compact, one needs e.g. that the Lipschitz constants are globally bounded). Let $\left(\Gamma_{f}, \mathscr{G}_{f}\right)$ be the boundary pair associated with the manifold $X_{f}$ and boundary $\partial X_{f}$. Note that each function $\varphi_{f} \in \mathscr{G}_{f}:=\mathrm{L}_{2}\left(\partial X_{f}\right)$ decomposes into its components $\varphi_{f}=\left(\varphi_{e, f}\right)_{e \in E_{f}}$ of the adjacent edge segments $Y_{e}$, i.e., $\varphi_{e, f} \in \mathrm{~L}_{2}\left(Y_{e}\right)$.

A global boundary map is now defined on
$$\mathscr{H}^{1}:=\left\{u \in \bigoplus_{f \in F} \mathrm{H}^{1}\left(X_{f}\right) \mid(\Gamma u)_{e, f_{1}}=(\Gamma u)_{e, f_{2}} \text { whenever } X_{f_{1}} \cap X_{f_{2}}=Y_{e}\right\}$$
by $\Gamma u:=u \upharpoonright_{Y}\left(u \in \mathscr{H}^{1}\right)$. This map is well-defined since the boundary values of $u$ from different sides on an edge agree by definition. It is not difficult to see that $\mathscr{H}^{1}=\mathrm{H}^{1}(X)$, and that $\Gamma: \mathscr{H}^{1} \longrightarrow \mathscr{G}:=\mathrm{L}_{2}(Y)$ is bounded, since $\Gamma$ is the restriction of the direct sum of the boundary maps $\Gamma_{f}: \mathrm{H}^{1}\left(X_{f}\right) \longrightarrow \mathrm{L}_{2}\left(\partial X_{f}\right)$ to $\mathscr{H}^{1}$ after suitable identifications.

As quadratic form, we consider $\mathfrak{h}(u):=\|\mathrm{d} u\|^{2}, u \in \mathscr{H}^{1}=\mathrm{H}^{1}(X)$.
Proposition 6.34. The boundary pair $(\Gamma, \mathscr{G})$ is unbounded, elliptically regular and not positive. The Neumann operator $H$ is the Laplacian on $X$, and the Dirichlet Laplacian is given by the direct sum of the Dirichlet Laplacians on $X_{f}$, i.e.,
$$H^{\mathrm{D}}=\bigoplus_{f \in F} \Delta_{X_{f}}^{\mathrm{D}}$$
and $H^{\mathrm{D}}$ is in particular decoupled. The Dirichlet-to-Neumann operator $\Lambda(z)$ acts as follows: if $\varphi$ is a (suitably smooth) function on $Y$, then $\psi=\Lambda(z) \varphi$ is given on $Y_{e}$ as the sum of the normal derivatives of the solutions of the Dirichlet problem on the two adjacent faces of e (i.e., $\psi_{e}$ is the jump in the derivative when crossing $Y_{e}$ form one face to the other).

Proof. We omit the details here, since we will consider these questions in a forthcoming publication. We only indicate how to prove the elliptic regularity of the boundary pair: this can be seen by noting first that the solution form is given by
$$\mathfrak{q}(\varphi)=\sum_{f \in F} \mathfrak{q}_{f}\left(\varphi_{f}\right),$$
where $\mathfrak{q}_{f}$ is the solution form of the boundary pair $\left(\Gamma_{f}, \mathscr{G}_{f}\right)$ associated with the face $X_{f}$. As these boundary pairs are all elliptically regular (the face $f$ is assumed to have a Lipschitz boundary), each of the solution forms is bounded by $C_{f}^{2}$ in $\mathscr{G}_{f}=\mathrm{L}_{2}\left(\partial X_{f}\right)$, the entire solution form is then bounded by $\max _{f \in F} C_{f}^{2}$, and hence $(\Gamma, \mathscr{G})$ is elliptically regular. \(\square\)

Remark 6.35 (Leaky graphs and photonic crystals). Let $\mathfrak{h}_{a}$ be the Robin-type perturbation of the form $\mathfrak{h}$ (i.e., $\mathfrak{h}_{a}(u):=\mathfrak{h}(u)+a\|\Gamma u\|^{2}$ for $a \geq 0$, see Section 5.1). Then $\mathfrak{h}_{a}$ is non-negative and closed, and we can consider $(\Gamma, \mathscr{G})$ associated with the form $\mathfrak{h}_{a}$. The associated (Neumann) operator $H_{a}$ then has a Robin-type boundary condition of the type $\Gamma^{\prime} u+a \Gamma u=0$, where $\Gamma^{\prime} u$ on $Y_{e}$ is the sum of the normal (outwards) derivative of $u$ on the two adjacent faces.

The resolvent difference of $H_{a}$ and $H^{\mathrm{D}}$ (the latter is still decoupled) can be expressed by a Krein-type formula, and $H_{a}$ converges to $H^{\mathrm{D}}$ in norm resolvent sense as $a \rightarrow \infty$. Moreover, the associated Dirichlet-to-Neumann operator of $(\Gamma, \mathscr{G})$ associated with $\mathfrak{h}_{a}$ is $\Lambda_{a}(z)=\Lambda(z)+a$.

This situation is closely related to a model called leaky graph (see the overview article [Ex08]). Note that in the situation of a leaky graph, one has $X=\mathbb{R}^{2}$ and $a<0$ (this needs some modifications of our arguments). Moreover, some faces may be non-compact with finitely many adjacent edges, some of them having infinite length. One is interested e.g. in the asymptotic behaviour of the negative eigenvalues as $a \rightarrow-\infty$. If the graph is just a curve embedded in $\mathbb{R}^{2}$, then the asymptotics are typically of the form $\lambda_{k}(a)=-a^{2} / 4+\mu_{k}+\mathrm{O}\left(|a|^{-1} \ln |a|\right)$ where $\mu_{k}$ is the $k$-th eigenvalue of a Schrödinger operator on the curve with (negative) potential given by the curvature of the curve in the plane. Only very few results are known if the curve is replaced by a graph. In particular, it would be very interesting to relate $\mu_{k}$ with the above defined Dirichlet-to-Neumann operator (or any other related one) on the graph (see [Ex08, Sec. 7.13]).