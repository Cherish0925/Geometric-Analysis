---
retention_scope: session
part: 3
total_parts: 7
---

[Part 3/7 of: PU(2) Monopoles, I: Regularity, Uhlenbeck Compactness ...]

The proof of the existence of an Uhlenbeck compactification for $M_{W, E}$ in §4 requires the perturbations $\vec{\tau} \cdot \overrightarrow{\mathfrak{m}}(A)$ and $\vec{\vartheta} \cdot \overrightarrow{\mathfrak{m}}(A)$ to satisfy the following estimates in order to obtain universal a priori $L_{1, A}^{2}$ bounds for $\Phi$ and $L^{2}$ bounds for $F_{A}$ (see Lemmas 4.2
and 4.3):
$$\begin{aligned}
& \sup _{A \in \mathcal{A}_{E}}\|\vec{\tau} \cdot \overrightarrow{\mathfrak{m}}(A)\|_{L^{\infty}(X)} \leq 1, \\
& \sup _{A \in \mathcal{A}_{E}}\|\vec{\vartheta} \cdot \overrightarrow{\mathfrak{m}}(A)\|_{L^{4}(X)} \leq 1 .
\end{aligned}$$
To obtain the more delicate universal a priori $L^{\infty}$ bounds for $\Phi$ and $F_{A}^{+}$(see Lemmas 2.26 and 4.4) required by our Uhlenbeck compactness argument in §4, the perturbations $\tau_{0}, \vec{\tau} \cdot \overrightarrow{\mathfrak{m}}(A)$, and $\vec{\vartheta} \cdot \overrightarrow{\mathfrak{m}}(A)$ must satisfy the following stronger estimates:
$$\begin{array}{r}
\left\|\tau_{0}\right\|_{L^{\infty}(X)}+\sup _{A \in \mathcal{A}_{E}}\|\vec{\tau} \cdot \overrightarrow{\mathfrak{m}}(A)\|_{L^{\infty}(X)} \leq \frac{1}{64}, \\
\left\|\vartheta_{0}\right\|_{L_{1}^{\infty}(X)}+\sup _{A \in \mathcal{A}_{E}}\|\vec{\vartheta} \cdot \overrightarrow{\mathfrak{m}}(A)\|_{L_{1, A}^{\infty}(X)} \leq 1 .
\end{array}$$
We take a constant 1 on the right-hand sides of (2.28) and the second inequality in (2.29) for notational convenience only: these bounds do not need to be 'small'. There are continuous Sobolev embeddings $L^{\infty}(X, \mathbb{R}) \subset L_{4}^{2}(X, \mathbb{R})$ and $L_{1}^{\infty}(X, \mathbb{R}) \subset L_{4}^{2}(X, \mathbb{R})$ over a four-manifold $X$. The estimates (2.29) then follow from the estimates (2.23) and (2.26) when $k \geq 3$. Therefore, to obtain the inequalities (2.29), we require that $k \geq 3$ in our configuration spaces of $L_{k}^{2}$ connections $\mathcal{B}_{E}$ and pairs $\mathcal{C}_{W, E}$ : see § A.4. The bounds in (2.29) then follow for small enough choices of $\varepsilon_{\tau}$ and $\varepsilon_{\vartheta}$ in the inequalities (2.23) and (2.26).

We shall need a slight generalization of Lemma 2.19 which applies to the perturbed quadratic form $\tau \rho^{-1}\left(\Phi \otimes \Phi^{*}\right)_{00}$ when $\tau \neq \mathrm{id}_{\Lambda^{+}}$. Without loss of generality, we may restrict our attention to automorphisms $\tau_{\rho}:=\rho \tau \rho^{-1}$ of $\mathfrak{s} \mathfrak{u}\left(W^{+}\right)$such that $\mid \tau_{\rho}-$ $\operatorname{id}_{\mathfrak{s u}\left(W^{+}\right)}\left|=\left|\rho \tau \rho^{-1}-\mathrm{id}\right|<\varepsilon_{\tau}\right.$ and thus
$$\left\langle\Phi_{1}, \Phi_{2}\right\rangle-\varepsilon_{\tau}\left|\Phi_{1}\right|\left|\Phi_{2}\right| \leq\left\langle\tau\left(\Phi_{1}\right), \Phi_{2}\right\rangle \leq\left\langle\Phi_{1}, \Phi_{2}\right\rangle+\varepsilon_{\tau}\left|\Phi_{1}\right|\left|\Phi_{2}\right|$$
for some universal positive constant $\varepsilon_{\tau} \ll 1$ and all $\Phi_{1}, \Phi_{2} \in \Omega^{0}\left(W^{+} \otimes E\right)$. Then Lemma 2.19 yields the following bounds for the perturbed quadratic form:

Lemma 2.26. There is universal positive constant $\varepsilon_{\tau} \ll 1$ such that for all $\| \tau-$ $\operatorname{id}_{\Lambda^{+}} \|_{C^{0}(X)}<\varepsilon_{\tau}$ and $\Phi \in \Omega^{0}\left(W^{+} \otimes E\right)$ the following inequalities hold:
$$\begin{aligned}
& \frac{1}{2}|\Phi|^{4} \leq\left\langle\tau_{\rho}\left(\Phi \otimes \Phi^{*}\right)_{00} \Phi, \Phi\right\rangle \leq \frac{3}{4}|\Phi|^{4}, \\
& \frac{1}{4}|\Phi|^{4} \leq\left|\tau_{\rho}\left(\Phi \otimes \Phi^{*}\right)_{00}\right|^{2} \leq \frac{3}{8}|\Phi|^{4} .
\end{aligned}$$

Remark 2.27. The constant $\varepsilon_{\tau}=1 / 64$ will suffice. The constraint $\|\tau-\mathrm{id}\|_{C^{0}(X)}<\varepsilon_{\tau}$ is only used in §4.1 and consequently in §4.6, where we establish the 'universal' a priori bounds for PU(2) monopoles and prove the existence of an Uhlenbeck compactification, respectively.
2.6. The moduli space and the elliptic deformation complex. We define the moduli space of PU(2) monopoles and compute the index of its elliptic deformation complex.

For any integer $k \geq 2$, the PU(2) monopole equations (2.27) define a $C^{\infty}$ map $\mathfrak{S}:=\left(\mathfrak{S}_{1}, \mathfrak{S}_{2}\right)$ of Hilbert manifolds,
$$\mathfrak{S}: \tilde{\mathcal{C}}_{W, E} \rightarrow L_{k-1}^{2}\left(\Lambda^{+} \otimes \mathfrak{s} \mathfrak{u}(E)\right) \oplus L_{k-1}^{2}\left(W^{-} \otimes E\right),$$
given by
$$(A, \Phi) \mapsto\binom{\mathfrak{S}_{1}(A, \Phi)}{\mathfrak{S}_{2}(A, \Phi)}:=\binom{F_{A}^{+}-\left(\mathrm{id}+\tau_{0} \otimes \mathrm{id}_{\mathfrak{s u}(E)}+\vec{\tau} \cdot \overrightarrow{\mathfrak{m}}(A)\right) \rho^{-1}\left(\Phi \otimes \Phi^{*}\right)_{00}}{D_{A} \Phi++\rho\left(\vartheta_{0}\right) \Phi+\vec{\vartheta} \cdot \overrightarrow{\mathfrak{m}}(A) \Phi} .$$
We can then define the moduli space of $\operatorname{PU}(2)$ monopoles by setting
$$M_{W, E}:=\left\{(A, \Phi) \in \tilde{\mathcal{C}}_{W, E}: \mathfrak{S}(A, \Phi)=0\right\} /{ }^{\circ} \mathcal{G}_{E}$$
and denote the moduli space of $\operatorname{PU}(2)$ monopoles which are neither reducible nor zero-section pairs by
$$M_{W, E}^{*, 0}:=M_{W, E} \cap \mathcal{C}_{W, E}^{*, 0} .$$
We let $M_{E}^{\text {asd }}:=\left\{[A]: F_{A}^{+}=0\right\} \subset \mathcal{B}_{E}$ be the moduli space of anti-self-dual connections on $\mathfrak{s u}(E)$.

The SO(3) bundle $\mathfrak{s u}(E)$ has first Pontrjagin number and second Stiefel-Whitney class given by
$$\kappa:=-\frac{1}{4} p_{1}(\mathfrak{s u}(E))=c_{2}(E)-\frac{1}{4} c_{1}(E)^{2} \quad \text { and } \quad w_{2}(\mathfrak{s u}(E))=c_{1}(E) \quad(\bmod 2),$$
and, for a connection $A$ on $\mathfrak{s} \mathfrak{u}(E)$, we have the following Chern-Weil integral identity,
$$-\frac{1}{4} p_{1}(\mathfrak{s u}(E))=\frac{1}{8 \pi^{2}} \int_{X}\left(\left|F_{A}^{-}\right|^{2}-\left|F_{A}^{+}\right|^{2}\right) d V$$
where we view $F_{A}$ as a section of $\Lambda^{2} \otimes \mathfrak{s} \mathfrak{u}(E)$ via the isomorphism ad : $\mathfrak{s} \mathfrak{u}(E) \simeq$ $\mathfrak{s} \mathfrak{o}(\mathfrak{s} \mathfrak{u}(E))$ (see [20, §2.1.4]).

Since the map $\mathfrak{S}$ is ${ }^{\circ} \mathcal{G}_{E}$-equivariant it defines a section of the Hilbert vector bundle $\mathfrak{V}$ over $\mathcal{C}_{W, E}^{*, 0}$ with total space
$$\mathfrak{V}:=\tilde{\mathcal{C}}_{W, E}^{*, 0} \times{ }_{\circ} \mathcal{G}_{E}\left(L_{k-1}^{2}\left(\Lambda^{+} \otimes \mathfrak{s} \mathfrak{u}(E)\right) \oplus L_{k-1}^{2}\left(W^{-} \otimes E\right)\right) .$$
While the equation $\mathfrak{S}[A, \Phi]=0$ is, of course, defined on $\mathcal{C}_{W, E}, \mathfrak{V}$ does not extend from $\mathcal{C}_{W, E}^{*, 0}$ to a vector bundle over $\mathcal{C}_{W, E}$. The moduli space $M_{W, E}^{*, 0} \subset \mathcal{C}_{W, E}^{*, 0}$ is then the zero locus of the section $\mathfrak{S}$ of Hilbert vector bundle $\mathfrak{V}$ over the Hilbert manifold $\mathcal{C}_{W, E}^{*, 0}$ : it will be a regular submanifold if $\mathfrak{S}$ vanishes transversely, that is, if the differential
$$(D \mathfrak{S})_{A, \Phi}: T_{[A, \Phi]} \mathcal{C}_{W, E}^{*, 0} \rightarrow L_{k-1}^{2}\left(\Lambda^{+} \otimes \mathfrak{s} \mathfrak{u}(E)\right) \oplus L_{k-1}^{2}\left(W^{-} \otimes E\right)$$
is surjective at all points $[A, \Phi]$ in $\mathfrak{S}^{-1}(0) \cap \mathcal{C}_{W, E}^{*, 0}$; recall from §2.2 that the tangent space $T_{[A, \Phi]} \mathcal{C}_{W, E}^{*, 0}$ is canonically identified with $\operatorname{Ker} d_{A, \Phi}^{0, *} \subset \tilde{\mathcal{C}}_{W, E}^{*, 0}$.

Suppose ( $A, \Phi$ ) is a pair in $\mathcal{A}_{E} \times \Omega^{0}\left(W^{+} \otimes E\right)$. Recall from Proposition 2.1 that the differential at the identity $\mathrm{id}_{E} \in{ }^{\circ} \mathcal{G}_{E}$, of the map ${ }^{\circ} \mathcal{G}_{E} \rightarrow \mathcal{A}_{E} \times \Omega^{0}\left(W^{+} \otimes E\right)$ given by $u \mapsto u(A, \Phi)$ is
$$\Omega^{0}(\mathfrak{s u}(E)) \oplus i \mathbb{R}_{Z} \rightarrow \Omega^{1}(\mathfrak{s u}(E)) \oplus \Omega^{0}\left(W^{+} \otimes E\right), \quad \zeta \mapsto-d_{A, \Phi}^{0} \zeta=\left(-d_{A} \zeta, \zeta \Phi\right) .$$
Similarly, the differential $(a, \phi) \mapsto d_{A, \Phi}^{1}(a, \phi):=(D \mathfrak{S})_{A, \Phi}(a, \phi)$,
$$\Omega^{1}(\mathfrak{s u}(E)) \oplus \Omega^{0}\left(W^{+} \otimes E\right) \rightarrow \Omega^{+}(\mathfrak{s u}(E)) \oplus \Omega^{0}\left(W^{-} \otimes E\right),$$
of the map $\mathfrak{S}$ at the point $(A, \Phi)$ is given by
$$d_{A, \Phi}^{1}(a, \phi):=\left(\begin{array}{c}
d_{A}^{+} a-\vec{\tau} \cdot(\delta \overrightarrow{\mathfrak{m}})(a)\left(\Phi \otimes \Phi^{*}\right)_{00}-\left(\mathrm{id}+\tau_{0} \otimes \mathrm{id}_{\mathfrak{s} \mathfrak{u}(E)}\right. \\
+\vec{\tau} \cdot \overrightarrow{\mathfrak{m}}(A)) \rho^{-1}\left(\Phi \otimes \phi^{*}+\phi \otimes \Phi^{*}\right)_{00} \\
D_{A} \phi+\rho\left(\vartheta_{0}\right) \phi+\vec{\vartheta} \cdot \overrightarrow{\mathfrak{m}}(A) \phi+\rho(a) \Phi+\vec{\vartheta} \cdot(\delta \overrightarrow{\mathfrak{m}})(a) \Phi
\end{array}\right),$$
where $\delta \overrightarrow{\mathfrak{m}}=\delta \overrightarrow{\mathfrak{m}} / \delta A$. (In the sequels we also find it convenient to use $L_{A, \Phi}$ to denote the linearization of the map $\mathfrak{S}$ at the point $(A, \Phi)$.) The differential of the composition ${ }^{\circ} \mathcal{G}_{E} \mapsto \Omega^{+}(\mathfrak{s u}(E)) \oplus \Omega^{0}\left(W^{-} \otimes E\right)$ given by
$$u \mapsto u(A, \Phi) \mapsto \mathfrak{S}(u(A, \Phi))=u(\mathfrak{S}(A, \Phi))=\left(u \mathfrak{S}_{1}(A, \Phi) u^{-1}, u \mathfrak{S}_{2}(A, \Phi)\right)$$
is then
$$\Omega^{0}(\mathfrak{s u}(E)) \otimes i \mathbb{R}_{Z} \rightarrow \underset{\Omega^{0}\left(W^{-} \otimes E\right)}{\Omega^{+}(\mathfrak{s u}(E))}, \quad \zeta \mapsto d_{A, \Phi}^{1} \circ d_{A, \Phi}^{0} \zeta=\left(\left[\zeta, \mathfrak{S}_{1}(A, \Phi)\right], \zeta \mathfrak{S}_{2}(A, \Phi)\right) .$$
Therefore, $d_{A, \Phi}^{1} \circ d_{A, \Phi}^{0}=0$ if and only if $\mathfrak{S}(A, \Phi)=0$, that is, if and only if ( $A, \Phi$ ) is a PU(2) monopole. Consequently, the sequence
$$\Omega^{0}(\mathfrak{s u}(E)) \oplus i \mathbb{R}_{Z} \xrightarrow{d_{A, \Phi}^{0}} \begin{gathered}
\Omega^{1}(\mathfrak{s u}(E)) \\
\oplus \\
\Omega^{0}\left(W^{+} \otimes E\right)
\end{gathered} \xrightarrow{\substack{d_{A, \Phi}^{1}\\
}} \begin{gathered}
\Omega^{+}(\mathfrak{s u}(E)) \\
\oplus \\
\Omega^{0}\left(W^{-} \otimes E\right)
\end{gathered}$$
is a complex if and only if ( $A, \Phi$ ) is a $\mathrm{PU}(2)$ monopole. The $L^{2}$ adjoint of $-d_{A, \Phi}^{0}$ is given by
$$-d_{A, \Phi}^{0, *}(a, \phi)=-d_{A}^{*} a+(\cdot \Phi)^{*} \phi .$$
The operator
$$\mathcal{D}_{A, \Phi}:=d_{A, \Phi}^{0, *}+d_{A, \Phi}^{1}: \begin{gathered}
\Omega^{1}(\mathfrak{s u}(E)) \\
\oplus \\
\Omega^{0}\left(W^{+} \otimes E\right)
\end{gathered} \longrightarrow \begin{gathered}
\Omega^{0}(\mathfrak{s u}(E)) \oplus i \mathbb{R}_{Z} \\
\oplus \\
\Omega^{+}(\mathfrak{s u}(E)) \\
\oplus \\
\Omega^{0}\left(W^{-} \otimes E\right)
\end{gathered}$$
is elliptic (thus Fredholm) and so (2.37) is an elliptic deformation complex for the PU(2) monopole equations (2.27), with cohomology groups
$$H_{A, \Phi}^{0}:=\operatorname{Ker} d_{A, \Phi}^{0}, \quad H_{A, \Phi}^{1}:=\operatorname{Ker} d_{A, \Phi}^{1} / \operatorname{Im} d_{A, \Phi}^{0}, \quad \text { and } \quad H_{A, \Phi}^{2}:=\operatorname{Coker} d_{A, \Phi}^{1},$$
analogous to the usual elliptic deformation complex [20, Eq. (4.2.26)] for the anti-self-dual equation, $F_{A}^{+}=0$. (An elliptic deformation complex for stable pairs for holomorphic bundles is given by Bradlow and Daskalopoulos in [9, §2].)

Recall that $H_{A, \Phi}^{0}=\operatorname{Ker} d_{A, \Phi}^{0}$ is just the Lie algebra of the stabilizer $\operatorname{Stab}_{A, \Phi}$ of the point $[A, \Phi] \in M_{W, E}$ and $H_{A, \Phi}^{1}$ is the Zariski or formal tangent space. Thus, for any point $[A, \Phi] \in M_{W, E}^{*, 0}$ we have $H_{A, \Phi}^{0}=0$. If $H_{A, \Phi}^{2}=0$, then $\operatorname{Coker}(D \mathfrak{S})_{A, \Phi}=0$ and so $[A, \Phi]$ is a regular point of the zero locus of the section $\mathfrak{S}$ of $\mathfrak{V}$ over $\mathcal{C}_{W, E}^{*, 0}$. So, if $H_{A, \Phi}^{0}=0$ and $H_{A, \Phi}^{2}=0$, then $[A, \Phi]$ is a smooth point of $M_{W, E}$ with tangent space $\operatorname{Ker} \mathcal{D}_{A, \Phi}=\operatorname{Ker}\left(d_{A, \Phi}^{0, *}+d_{A, \Phi}^{1}\right)=H_{A, \Phi}^{1}$, as we see from (2.35). Provided the zero set $\mathfrak{S}^{-1}(0)$ is regular, then $M_{W, E}^{*, 0}$ will be a smooth manifold of dimension - Ind $\mathcal{D}_{A, \Phi}$.

The perturbation terms in (2.27) define gauge equivariant maps
$$\tilde{\mathcal{C}}_{W, E}^{*, 0} \rightarrow L_{k-1}^{2}\left(\Lambda^{+} \otimes \mathfrak{s u}(E)\right) \oplus L_{k-1}^{2}\left(W^{-} \otimes E\right),$$
given by
$$(A, \Phi) \mapsto\binom{\vec{\tau} \cdot \overrightarrow{\mathfrak{m}}(A) \rho^{-1}\left(\Phi \otimes \Phi^{*}\right)_{00}}{\vec{\vartheta} \cdot \overrightarrow{\mathfrak{m}}(A) \Phi} .$$
For $k \geq 2$, the Sobolev multiplication theorem implies that $\vec{\vartheta} \cdot \overrightarrow{\mathfrak{m}}(A) \Phi$ is in $L_{k}^{2}\left(W^{-} \otimes E\right)$, while $\vec{\tau} \cdot \overrightarrow{\mathfrak{m}}(A) \rho^{-1}\left(\Phi \otimes \Phi^{*}\right)_{00}$ is in $L_{k}^{2}\left(\Lambda^{+} \otimes \mathfrak{s} \mathfrak{u}(E)\right)$ when $k \geq 3$ and in $L_{2}^{p}\left(\Lambda^{+} \otimes \mathfrak{s} \mathfrak{u}(E)\right)$, $1 \leq p<2$ when $k=2$. By the Rellich embedding theorem, the inclusions $L_{k}^{2} \subset L_{k-1}^{2}$ and $L_{2}^{p} \subset L_{1}^{2}, p>1$, are compact. In particular, it follows that the linearization of the perturbed PU(2) monopole equations (2.36) differs from the linearization of the unperturbed equations (2.15) by a compact operator [2, Theorem VI.2].

Proposition 2.28. If the map $\mathfrak{S}$ of (2.30) vanishes transversely for the parameters $\left(\tau_{0}, \vartheta_{0}, \vec{\tau}, \vec{\vartheta}\right)$ then $M_{W, E}^{*, 0}\left(\tau_{0}, \vartheta_{0}, \vec{\tau}, \vec{\vartheta}\right)$ is a smooth manifold of dimension
$$\begin{aligned}
\operatorname{dim} M_{W, E}^{*, 0}= & -2 p_{1}(\mathfrak{s u}(E))-3\left(1-b^{1}(X)+b^{+}(X)\right) \\
& +\frac{1}{2} p_{1}(\mathfrak{s u}(E))+\frac{1}{2}\left(c_{1}\left(W^{+}\right)+c_{1}(E)\right)^{2}-\frac{1}{2} \sigma(X)-1 \\
= & \operatorname{dim} M_{E}^{\operatorname{asd}}+2 \operatorname{Ind}_{\mathbb{C}} D_{A}-1,
\end{aligned}$$
where $\sigma(X)$ is the signature of $X$.
Proof. Since $H_{A, \Phi}^{0}=0$ and $H_{A, \Phi}^{2}=0$ (by hypothesis) at any point $[A, \Phi]$ in $M_{W, E}^{*, 0}$, we have $\operatorname{dim} M_{W, E}^{*, 0}=-\operatorname{Ind} \mathcal{D}_{A, \Phi}$. By our regularity result, Proposition 3.7, any point $[A, \Phi]$ in $M_{W, E}^{*, 0}$ has a smooth representative $(A, \Phi)$. Therefore, from the expressions for $d_{A, \Phi}^{0, *}$ in (2.38) and for $d_{A, \Phi}^{1}$ in (2.36) and the Sobolev multiplication and embedding
theorems, we find that the operator $\mathcal{D}_{A, \Phi}=d_{A, \Phi}^{0, *}+d_{A, \Phi}^{1}: L_{k}^{2} \rightarrow L_{k-1}^{2}$ differs from
$$\left(\begin{array}{cc}
d_{A}^{*}+d_{A}^{+} & 0 \\
0 & D_{A}
\end{array}\right): \begin{gathered}
L_{k}^{2}\left(\Lambda^{1} \otimes \mathfrak{s u}(E)\right) \\
\oplus \\
L_{k}^{2}\left(W^{+} \otimes E\right)
\end{gathered} \begin{gathered}
L_{k-1}^{2}(\mathfrak{s u}(E)) \oplus i \mathbb{R}_{Z} \\
\oplus \\
L_{k-1}^{2}\left(\Lambda^{+} \otimes \mathfrak{s u}(E)\right) \\
L_{k-1}^{2}\left(W^{-} \otimes E\right)
\end{gathered}$$
by a compact operator and so has the same (real) index:
$$\operatorname{Ind} \mathcal{D}_{A, \Phi}=\operatorname{Ind}\left(d_{A}^{*}+d_{A}^{+}\right)+\operatorname{Ind}_{\mathbb{R}} D_{A}-1 .$$
We recall from [20, Eq. (4.2.22)] that the operator
$$d_{A}^{*}+d_{A}^{+}: L_{k}^{2}\left(\Lambda^{1} \otimes \mathfrak{s u}(E)\right) \rightarrow L_{k-1}^{2}(\mathfrak{s u}(E)) \oplus L_{k-1}^{2}\left(\Lambda^{+} \otimes \mathfrak{s u}(E)\right)$$
has index
$$\operatorname{Ind}\left(d_{A}^{*}+d_{A}^{+}\right)=-2 p_{1}(\mathfrak{s u}(E))-3\left(1-b^{1}(X)+b^{+}(X)\right) .$$
The complex index of the Dirac operator $D_{A}$ is given by
$$\begin{aligned}
\operatorname{Ind}_{\mathbb{C}} D_{A}= & \left\langle(\hat{A}(X)) \operatorname{ch}(E) e^{\frac{1}{2} c_{1}\left(W^{+}\right)},[X]\right\rangle \\
= & \left\langle( 1 - \frac { 1 } { 2 4 } p _ { 1 } ( X ) ) \left( 2+c_{1}(E)\right.\right. \\
& \left.\left.\quad+\frac{1}{2} c_{1}(E)^{2}-c_{2}(E)\right)\left(1+\frac{1}{2} c_{1}\left(W^{+}\right)+\frac{1}{8} c_{1}\left(W^{+}\right)^{2}\right),[X]\right\rangle \\
= & \left\langle-\frac{1}{12} p_{1}(X)+\frac{1}{4} c_{1}\left(W^{+}\right)^{2}+\frac{1}{2} c_{1}(E)^{2}-c_{2}(E)+\frac{1}{2} c_{1}(E) c_{1}\left(W^{+}\right),[X]\right\rangle \\
= & -\frac{1}{4} \sigma(X)+\frac{1}{4} c_{1}\left(W^{+}\right)^{2}+\frac{1}{2} c_{1}(E)^{2}-c_{2}(E)+\frac{1}{2} c_{1}(E) c_{1}\left(W^{+}\right) \\
= & \left(\frac{1}{4} c_{1}(E)^{2}-c_{2}(E)\right)+\frac{1}{4}\left(\left(c_{1}\left(W^{+}\right)+c_{1}(E)\right)^{2}-\sigma(X)\right) \\
= & \frac{1}{4} p_{1}(\mathfrak{s u}(E))+\frac{1}{4}\left(\left(c_{1}\left(W^{+}\right)+c_{1}(E)\right)^{2}-\sigma(X)\right) .
\end{aligned}$$
Adding these indices and noting that $\operatorname{Ind}_{\mathbb{R}} D_{A}=2 \operatorname{Ind}_{\mathbb{C}} D_{A}$ gives our dimension formula. \(\square\)

\section*{3. Regularity}

Our goal in this section is to establish the basic regularity results for solutions to the PU(2) monopole equations (2.27). In §3.1 we show that global $L_{1}^{2}$ solutions to the firstorder elliptic system comprising (2.27) and the Coulomb gauge equation (see §2.2) are necessarily $C^{\infty}$, while in §3.2 we show that global $L_{k}^{2}$ solutions to (2.27) are equivalent via an $L_{k+1}^{2}$ determinant-one, unitary automorphism of $E$ - provided $k \geq 2$ - to $C^{\infty}$ solutions to (2.27) in Coulomb gauge relative to some $C^{\infty}$ reference pair. In §3.3 and §3.4 we establish local versions of the results of §3.1 and §3.2. The regularity results and estimates of this section will be needed repeatedly throughout our work, so we state them here in sufficient generality to cover all of these applications. In the present article, we require the regularity results for our proof of transversality for the moduli space of PU(2) monopoles (see §5) and they form the cornerstone of our proofs of removable singularities and existence of an Uhlenbeck compactification (see §4).

Furthermore, in sequels to this article [26, 27], the regularity results of this section are used to show that $L_{1}^{2}$ gluing solutions to (2.27) are necessarily $C^{\infty}$ and to analyse the Uhlenbeck-boundary behavior of the gluing and obstruction maps parametrizing the moduli space ends.

In order to simultaneously address all of the intended applications, the equations we find it convenient to consider here are a quasi-linear, inhomogeneous elliptic system consisting of a generalization of the equations (2.27) and Coulomb gauge equation for a pair $(A, \Phi) \in \mathcal{A}_{E}(X) \times \Omega^{0}\left(W^{+} \otimes E\right)$. Specifically, we allow inhomogeneous, righthand terms: the need for this generalization arises in our proofs of removable singularities and of regularity for gluing solutions to (2.27) and in analysing the Uhlenbeck-boundary behavior of gluing maps. Suppose that $\left(A_{0}, \Phi_{0}\right)$ is a fixed $C^{\infty}$ reference pair in $\mathcal{A}_{E}(X) \times \Omega^{0}\left(X, W^{+} \otimes E\right)$ : writing $(A, \Phi)=\left(A_{0}, \Phi_{0}\right)+(a, \phi)$, combining (2.27) with the Coulomb gauge equation, and allowing inhomogenous terms, we obtain an elliptic system of equations for a pair $(a, \phi)$ in $\Omega^{1}(X, \mathfrak{s u}(E)) \oplus \Omega^{0}\left(X, W^{+} \otimes E\right)$,
$$\begin{aligned}
d_{A_{0}}^{*} a-\left(\cdot \Phi_{0}\right)^{*} \phi & =\zeta \\
\mathfrak{S}\left(A_{0}+a, \Phi_{0}+\phi\right) & =\left(v_{0}, \psi_{0}\right),
\end{aligned}$$
Considering $A$ to be a connection on $\mathfrak{s u}(E)$ and using the isomorphism ad : $\mathfrak{s u}(E) \rightarrow$ $\mathfrak{s} \mathfrak{o}(\mathfrak{s} \mathfrak{u}(E))$ to view $F_{A}$ as a section of $\Lambda^{2} \otimes \mathfrak{s} \mathfrak{u}(E)$, we write (3.1) as
$$\begin{aligned}
d_{A_{0}}^{*} a-\left(\cdot \Phi_{0}\right)^{*} \phi & =\zeta, \\
F_{A_{0}+a}^{+}-\left(\mathrm{id}+\tau_{0} \otimes \mathrm{id}_{\mathfrak{s u}(E)}+\vec{\tau} \cdot \overrightarrow{\mathfrak{m}}(A)\right) \rho^{-1}\left(\left(\Phi_{0}+\phi\right) \otimes\left(\Phi_{0}+\phi\right)^{*}\right)_{00} & =v_{0}, \\
\left(D_{A_{0}+a}+\rho\left(\vartheta_{0}\right)+\vec{\vartheta} \cdot \overrightarrow{\mathfrak{m}}(A)\right)\left(\Phi_{0}+\phi\right) & =\psi_{0},
\end{aligned}$$
where $\left(v_{0}, \psi_{0}\right) \in \Omega^{+}(X, \mathfrak{s u}(E)) \oplus \Omega^{0}\left(X, W^{-} \otimes E\right)$. Recalling that $d_{A_{0}, \Phi_{0}}^{0}$ and $d_{A_{0}, \Phi_{0}}^{1}$ are the differential operators in the elliptic deformation complex (2.37) for the PU(2) monopole equations (2.27), the above system may be rewritten in the form
$$\begin{aligned}
d_{A_{0}, \Phi_{0}}^{0, *}(a, \phi) & =\zeta, \\
d_{A_{0}, \Phi_{0}}^{1}(a, \phi)+\{(a, \phi),(a, \phi)\} & =-\mathfrak{S}\left(A_{0}, \Phi_{0}\right)+\left(v_{0}, \psi_{0}\right)=:(v, \psi),
\end{aligned}$$
where $(v, \psi) \in \Omega^{+}(X, \mathfrak{s u}(E)) \oplus \Omega^{0}\left(X, W^{-} \otimes E\right)$ and the differentials $d_{A_{0}, \Phi_{0}}^{0, *}$ and $d_{A_{0}, \Phi_{0}}^{1}$ are given by (2.38) and (2.36). It will be convenient to view the quadratic term $\{(a, \phi),(a, \phi)\}$ as being defined via the following bilinear form,
$$\{(a, \phi),(b, \varphi)\}:=\binom{(a \wedge b)^{+}-\left(\mathrm{id}+\tau_{0} \otimes \mathrm{id}_{\mathfrak{s u}(E)}+\vec{\tau} \cdot \overrightarrow{\mathfrak{m}}(A)\right) \rho^{-1}\left(\phi \otimes \varphi^{*}\right)_{00}}{\rho(a) \varphi},$$
where $(b, \varphi) \in \Omega^{1}(X, \mathfrak{s u}(E)) \oplus \Omega^{0}\left(X, W^{+} \otimes E\right)$; we will further abbreviate $\{(a, \phi),(a, \phi)\}$ by $q(a, \phi)$ when convenient. Our elliptic system (3.1) then takes the simple shape
$$\mathcal{D}_{A_{0}, \Phi_{0}}(a, \phi)+\{(a, \phi),(a, \phi)\}=(\zeta, v, \psi),$$
recalling from (2.39) that $\mathcal{D}_{A_{0}, \Phi_{0}}=d_{A_{0}, \Phi_{0}}^{0, *}+d_{A_{0}, \Phi_{0}}^{1}$. This is the form of the (inhomogeneous) Coulomb gauge and PU(2) monopole equations we will use for the majority of the basic regularity arguments.

Some of the regularity results and estimates of this section generalize corresponding results for the first-order anti-self-dual equation [20, 30] and, to a certain extent, those of Uhlenbeck [94] and Parker [70] for the second-order (coupled) Yang-Mills equations. As usual for a quasi-linear, first-order elliptic system with a quadratic non-linearity, over an $n$-dimensional manifold, the main difficulty is to prove regularity for $L_{1}^{n / 2}$ solutions (that is, at the critical Sobolev exponent). Once the solutions are known to be in $L^{\infty}$, then standard linear elliptic regularity theory can applied [37, 64]. It is worth noting at the outset, though, that despite an extensive literature on quasi-linear elliptic systems due to Ladyzhenskaya-Ural'tseva, Morrey and others [54, 64] these classical results do not meet the usual demands of gauge theory and this explains why we develop the precise results we require here. The constants appearing in our estimates generally depend on the underlying Riemannian metric on $X$, the fixed spin ${ }^{c}$ connection on $W$, the fixed unitary connection on $\operatorname{det} E$, and the perturbations $\left(\tau_{0}, \vec{\tau}, \vec{\vartheta}\right)$ : this dependence is not explicitly noted, as these ingredients in the PU(2) monopole equations (2.27) are fixed once and for all.
3.1. Regularity for $L_{1}^{2}$ solutions to the inhomogeneous Coulomb gauge and PU(2) monopole equations. We show in this subsection that an $L_{1}^{2}$ solution $(a, \phi)$ to the PU(2) monopole and Coulomb-gauge equations (3.2), with an $L_{k}^{2}$ inhomogeneous term (with $k \geq 1$ ) is in $L_{k+1}^{2}$. Thus, if the inhomogeneous term is in $C^{\infty}$ then $(a, \phi)$ is in $C^{\infty}$. In passing from an $L_{1}^{2}$ to an $L_{2}^{2}$ solution we need only consider the case where $(\vec{\tau}, \vec{\vartheta})=0$, while no restriction is placed on the perturbation $(\vec{\tau}, \vec{\vartheta}) \in \mathcal{P}$ given an $L_{2}^{2}$ solution $(a, \phi)$.

Our regularity result contains, as special cases, Proposition 4.4.13 in [20] and Theorem 8.8 in [30], for anti-self-dual connections, and Theorem 8.11 in [77] for Seiberg-Witten monopoles. The proof we give below for PU(2) monopoles is rather different. We provide a fairly detailed argument here since regularity of $L_{2}^{2}$ solutions to an elliptic equation with a quadratic non-linear term does not quite follow directly from standard theory for non-linear elliptic systems (for example, [64, Theorem 6.8.1]).

The two principal steps are, first, to get $L_{1}^{p}$ regularity of an $L_{1}^{2}$ solution $(a, \phi)$ when $2<p<4$ and $(a, \phi)$ is sufficiently $L^{4}$-small and, second, to apply elliptic boostrapping and the Sobolev multiplication and embedding theorems to get $C^{\infty}$ regularity of an $L_{1}^{p}$ solution $(a, \phi)$ when $2<p<\infty$. We will use these sharp regularity results and estimates repeatedly throughout our work, so we give the argument in some detail here. The main ingredient in the first step is supplied by Proposition 3.2 and uses a Fredholm alternative argument to pass from $L_{1}^{2}$ to the slightly stronger $L_{1}^{p}$ regularity [33, Theorem 5.3]. Although we will often be able to simply assume that the inhomogenous term is in $C^{\infty}$, rather than just in $L^{p}$, we will later need these intermediate regularity results in our development of the gluing theory for PU(2)
monopoles [26, 27] to show that $L_{1}^{2}$ solutions $(a, \phi)$ to the system (3.2) with a certain inhomogeneous term $(\zeta, v, \psi)$, where the latter is initially only known to be in $L_{1}^{2}$ or $L_{2}^{2}$, are actually in $C^{\infty}$ (together, of course, with $(\zeta, v, \psi)$ ).

Lemma 3.1. Let $\mathfrak{B}_{1}, \mathfrak{B}_{2}$ be Banach spaces and let $T \in \operatorname{Hom}\left(\mathfrak{B}_{1}, \mathfrak{B}_{2}\right)$ have a right (left) inverse $P$. If $T^{\prime} \in \operatorname{Hom}\left(\mathfrak{B}_{1}, \mathfrak{B}_{2}\right)$ satisfies $\left\|T^{\prime}-T\right\|<\|P\|^{-1}$, then $T^{\prime}$ also has a right (left) inverse.

Proof. If $P \in \operatorname{Hom}\left(\mathfrak{B}_{2}, \mathfrak{B}_{1}\right)$ is a right inverse for $T$, so $T P=\mathrm{id}_{1}$, then $\left\|\left(T^{\prime}-T\right) P\right\| \leq$ $\left\|T^{\prime}-T\right\|\|P\|<1$ and $\mathrm{id}_{1}+\left(T^{\prime}-T\right) P$ is an invertible element of the Banach algebra $\operatorname{End}\left(\mathfrak{B}_{1}\right)$. Define $P^{\prime}=P\left(1+\left(T^{\prime}-T\right) P\right)^{-1}$, so $T^{\prime} P^{\prime}=\mathrm{id}_{1}$ and $P^{\prime}$ is a right inverse for $T^{\prime}$. Similarly for left inverses. \(\square\)

The preceding elementary consequence of the usual characterization of invertible elements of a Banach algebra will be frequently invoked in this section and in particular, in the proof of the proposition below.

Proposition 3.2. Let $X$ be a closed, oriented, Riemannian four-manifold with metric $g$, spin ${ }^{c}$ structure ( $\rho, W$ ), and let $E$ be a Hermitian two-plane bundle over $X$. Let $\left(A_{0}, \Phi_{0}\right)$ be a $C^{\infty}$ pair on the $C^{\infty}$ bundles $\left(\mathfrak{s u}(E), W^{+} \otimes E\right)$ over $X$ and let $2 \leq p<4$. Then there are positive constants $\varepsilon=\varepsilon\left(A_{0}, \Phi_{0}, p\right)$ and $C=C\left(A_{0}, \Phi_{0}, p\right)$ with the following significance. Suppose that $(a, \phi) \in L_{1}^{2}\left(X, \Lambda^{1} \otimes \mathfrak{s u}(E)\right) \oplus L_{1}^{2}\left(X, W^{+} \otimes E\right)$ is an $L_{1}^{2}$ solution on $\left(\mathfrak{s u}(E), W^{+} \otimes E\right)$ to the elliptic system (3.2) over $X$ with $(\vec{\tau}, \vec{\vartheta})=0$, where ( $\zeta, v, \psi$ ) is in $L^{p}$. If $\|(a, \phi)\|_{L^{4}(X)}<\varepsilon$ then ( $a, \phi$ ) is in $L_{1}^{p}$ and
$$\|(a, \phi)\|_{L_{1, A_{0}}^{p}(X)} \leq C\left(\|(\zeta, v, \psi)\|_{L^{p}(X)}+\|(a, \phi)\|_{L^{2}(X)}\right) .$$
Proof. The operator $\mathcal{D}_{A_{0}, \Phi_{0}}$ is Fredholm (since it is elliptic with $C^{\infty}$ coefficients and $X$ is closed), and so has a finite-dimensional kernel and cokernel. In particular, $\left.\operatorname{Ker} \mathcal{D}_{A_{0}, \Phi_{0}}\right|_{L_{1}^{2}} \subset C^{\infty}$. Let $\Pi_{1}$ be the $L^{2}$-orthogonal projection onto $\left.\operatorname{Ker} \mathcal{D}_{A_{0}, \Phi_{0}}\right|_{L_{1}^{2}}$ and let $\Pi_{2}$ be the $L^{2}$-orthogonal projection onto $\left.\operatorname{Ker} \mathcal{D}_{A_{0}, \Phi_{0}}^{*}\right|_{L^{2}}=\left(\left.\operatorname{Im} \mathcal{D}_{A_{0}, \Phi_{0}}\right|_{L_{1}^{2}}\right)^{\perp}$, the $L^{2}$ -orthogonal complement of the image of $\left.\operatorname{Im} \mathcal{D}_{A_{0}, \Phi_{0}}\right|_{L_{1}^{2}}$. The $L^{2}$-adjoint $\mathcal{D}_{A_{0}, \Phi_{0}}^{*}$ is again a first-order linear elliptic operator with $C^{\infty}$ coefficients and so $\left.\operatorname{Ker} \mathcal{D}_{A_{0}, \Phi_{0}}^{*}\right|_{L^{2}} \subset C^{\infty}$. We may then rewrite our quasi-linear elliptic equation (3.2) in the form
$$\begin{array}{r}
\Pi_{2}^{\perp} \mathcal{D}_{A_{0}, \Phi_{0}} \Pi_{1}^{\perp}(a, \phi)+\Pi_{2}^{\perp}\left\{(a, \phi), \Pi_{1}^{\perp}(a, \phi)\right\} \\
=-\Pi_{2}\left(\mathcal{D}_{A_{0}, \Phi_{0}}(a, \phi)+\left\{(a, \phi), \Pi_{1}^{\perp}(a, \phi)\right\}\right) \\
-\left\{(a, \phi), \Pi_{1}(a, \phi)\right\}+(\zeta, v, \psi)=: \Upsilon .
\end{array}$$
where $\Pi_{i}^{\perp}=\mathrm{id}-\Pi_{i}$ for $i=1,2$. Thus, we need to consider the existence and uniqueness problem for solutions $(b, \varphi)$ to
$$\Pi_{2}^{\perp} \mathcal{D}_{A_{0}, \Phi_{0}}(b, \varphi)+\Pi_{2}^{\perp}\{(a, \phi),(b, \varphi)\}=\Upsilon$$
where $(b, \varphi) \in L_{1}^{p} \cap\left(\operatorname{Ker} \mathcal{D}_{A_{0}, \Phi_{0}}\right)^{\perp}$. Plainly, the operator
$$\Pi_{2}^{\perp} \mathcal{D}_{A_{0}, \Phi_{0}}: L_{1}^{p} \cap\left(\operatorname{Ker} \mathcal{D}_{A_{0}, \Phi_{0}}\right)^{\perp} \rightarrow L_{1}^{p} \cap\left(\operatorname{Ker} \mathcal{D}_{A_{0}, \Phi_{0}}^{*}\right)^{\perp}$$
is (left and right) invertible and hence this will also be true for any operator from $L_{1}^{p} \cap\left(\operatorname{Ker} \mathcal{D}_{A_{0}, \Phi_{0}}\right)^{\perp}$ to $L^{p} \cap\left(\operatorname{Ker} \mathcal{D}_{A_{0}, \Phi_{0}}^{*}\right)^{\perp}$, such as $\Pi_{2}^{\perp} \mathcal{D}_{A_{0}, \Phi_{0}}+\Pi_{2}^{\perp}\{(a, \phi)$, • \}, which is sufficiently close in the $\operatorname{Hom}\left(L_{1, A_{0}}^{p}, L^{p}\right)$ operator norm by Lemma 3.1. Since $\mathcal{D}_{A_{0}, \Phi_{0}}$ and $\mathcal{D}_{A_{0}, \Phi_{0}}^{*}$ are first-order linear elliptic operators with $C^{\infty}$ coefficients and $\mathcal{D}_{A_{0}, \Phi_{0}} \Pi_{1}=0$ and $\mathcal{D}_{A_{0}, \Phi_{0}}^{*} \Pi_{2}=0$, standard elliptic theory implies that
$$\begin{aligned}
\left\|\Pi_{2}(\xi, w, \varrho)\right\|_{L_{k, A_{0}}^{r}} & \leq C\|(\xi, w, \varrho)\|_{2}, \quad(\xi, w, \varrho) \in L_{k}^{r}, \\
\left\|\Pi_{1}(b, \varphi)\right\|_{L_{k, A_{0}}^{r}} & \leq C\|(b, \varphi)\|_{2}, \quad(b, \varphi) \in L_{k}^{r},
\end{aligned}$$
for some constant $C=C\left(A_{0}, \Phi_{0}, k, r\right)$, whenever $k \geq 1$ and $r k \geq 4 / 3$ or $k=0$ and $r \geq 2$.

Since $(a, \phi)$ is in $L_{1}^{2}$, the terms $\mathcal{D}_{A_{0}, \Phi_{0}}(a, \phi)$ and $\{(a, \phi),(a, \phi)\}$ and $\left\{(a, \phi), \Pi_{1}^{\perp}(a, \phi)\right\}$ are in $L^{2}$, while the term $\left\{(a, \phi), \Pi_{1}(a, \phi)\right\}$ is in $L_{1}^{2}$. The terms $\Pi_{2} \mathcal{D}_{A_{0}, \Phi_{0}}(a, \phi)$ and $\Pi_{2}\left\{(a, \phi), \Pi_{1}^{\perp}(a, \phi)\right\}$ are each in $C^{\infty}$, while $(\zeta, v, \psi)$ is in $L^{p}$, and so the right-hand side $\Upsilon$ of (3.3) is in $L^{p} \cap\left(\operatorname{Ker} \mathcal{D}_{A_{0}, \Phi_{0}}^{*}\right)^{\perp}$.

Let $q=4 p /(4-p)$, so $4<q<\infty$; there is a continuous multiplication map $L^{4} \times L^{q} \rightarrow L^{p}$ and an embedding $L_{1}^{p} \subset L^{q}$. So, as $\Pi_{2}^{\perp}=\mathrm{id}-\Pi_{2}$,
$$\begin{aligned}
\left\|\Pi_{2}^{\perp}\{(a, \phi),(b, \varphi)\}\right\|_{L^{p}} & \leq\|\{(a, \phi),(b, \varphi)\}\|_{L^{p}}+C\|\{(a, \phi),(b, \varphi)\}\|_{L^{2}} \\
& \leq C\|(a, \phi)\|_{L^{4}}\|(b, \varphi)\|_{L_{1, A_{0}}^{p}},
\end{aligned}$$
for some positive constant $C=C\left(A_{0}, \Phi_{0}, p\right)$. By Lemma 3.1 there is a positive constant $\varepsilon=\varepsilon\left(A_{0}, \Phi_{0}, p\right)$ such that if $\|(a, \phi)\|_{L^{4}}<\varepsilon$, the linear operator $\Pi_{2}^{\perp} \mathcal{D}_{A_{0}, \Phi_{0}}+$ $\Pi_{2}^{\perp}\{(a, \phi), \cdot\}$ is (left and right) invertible as a map $L_{1}^{p} \cap\left(\operatorname{Ker} \mathcal{D}_{A_{0}, \Phi_{0}}\right)^{\perp} \rightarrow L^{p} \cap$ ( $\left.\operatorname{Ker} \mathcal{D}_{A_{0}, \Phi_{0}}^{*}\right)^{\perp}$. Since $\Pi_{1}^{\perp}(a, \phi)$ is a solution to (3.3) when $p=2$, then it is the unique solution for $p=2$.

Let $\left(a_{p}, \phi_{p}\right) \in L_{1}^{p} \cap\left(\operatorname{Ker} \mathcal{D}_{A_{0}, \Phi_{0}}\right)^{\perp}$ be the $L_{1}^{p}$ solution to (3.3). Then $\left(a_{p}, \phi_{p}\right)$ is also an $L_{1}^{2}$ solution and by the uniqueness assertion we must have that $\left(a_{p}, \phi_{p}\right)=\Pi_{1}^{\perp}(a, \phi)$. Thus, $\Pi_{1}^{\perp}(a, \phi)$ is in $L_{1}^{p}$ and so $(a, \phi)$ is in $L_{1}^{p}$, since $\Pi_{1}(a, \phi)$ is in $C^{\infty}$. Finally, the standard estimate for $\mathcal{D}_{A_{0}, \Phi_{0}}$, the estimate (3.4), and equation (3.2) yield
$$\begin{aligned}
\|(a, \phi)\|_{L_{1, A_{0}}^{p}} & \leq C\left(\left\|\mathcal{D}_{A_{0}, \Phi_{0}}(a, \phi)\right\|_{L^{p}}+\left\|\Pi_{1}(a, \phi)\right\|_{L^{2}}\right) \\
& \leq C\left(\|\{(a, \phi),(a, \phi)\}\|_{L^{p}}+\|(\zeta, v, \psi)\|_{L^{p}}+\left\|\Pi_{1}(a, \phi)\right\|_{L^{2}}\right),
\end{aligned}$$
and so the desired bound for $(a, \phi)$ follows by the Sobolev multiplication $L^{4} \times L^{q} \rightarrow L^{p}$, the embedding $L_{1}^{p} \subset L^{q}$, and rearrangement. \(\square\)

Proposition 3.2 will have two main applications: the first is in our proof of removable singularities for PU(2) monopoles and the second is in our proof of $C^{\infty}$ regularity for $L_{1}^{2}$ solutions to the PU(2) monopole equation obtained by gluing [26, 27].

As is well-known from standard gauge theory, it is not possible to construct a well-defined quotient space using $L_{1}^{2}$ pairs modulo $L_{2}^{2}$ gauge transformations. We construct a quotient using $L_{k}^{2}$ pairs modulo $L_{k+1}^{2}$ gauge transformations, with $k \geq 2$. We first establish a regularity result for the inhomogeneous PU(2) monopole and Coulomb
gauge equations, while in §3.2 we show that any PU(2) monopole in $L_{k}^{2}$ is $L_{k+1}^{2}$-gauge equivalent to a PU(2) monopole in $C^{\infty}$.

Proposition 3.3. Continue the notation of Proposition 3.2. Let $k \geq 1$ be an integer and let $2<p<\infty$. Let $\left(A_{0}, \Phi_{0}\right)$ be a $C^{\infty}$ pair on the $C^{\infty}$ bundles $\left(\mathfrak{s} \mathfrak{u}(E), W^{+} \otimes E\right)$ over $X$. Suppose that either
\begin{itemize}
\item[-] $(a, \phi) \in L_{1}^{p}\left(X, \Lambda^{1} \otimes \mathfrak{s u}(E)\right) \oplus L_{1}^{p}\left(X, W^{+} \otimes E\right)$, with $(\vec{\tau}, \vec{\vartheta})=0$, or
\item[-] $(a, \phi) \in L_{2}^{2}\left(X, \Lambda^{1} \otimes \mathfrak{s} \mathfrak{u}(E)\right) \oplus L_{2}^{2}\left(X, W^{+} \otimes E\right)$
\end{itemize}
is a solution on $\left(\mathfrak{s u}(E), W^{+} \otimes E\right)$ to the elliptic system (3.2) over $X$, where ( $\zeta, v, \psi$ ) is in $L_{k}^{2}$. Then $(a, \phi)$ is in $L_{k+1}^{2}$ and there is a universal polynomial $Q_{k}(x, y)$, with positive real coefficients, depending at most on $\left(A_{0}, \Phi_{0}\right), k$, such that $Q_{k}(0,0)=0$ and
$$\|(a, \phi)\|_{L_{k+1, A_{0}}^{2}(X)} \leq Q_{k}\left(\|(\zeta, v, \psi)\|_{L_{k, A_{0}}^{2}(X)},\|(a, \phi)\|_{L_{1, A_{0}}^{p}(X)}\right) .$$
In particular, if $(\zeta, v, \psi)$ is in $C^{\infty}$ then $(a, \phi)$ is in $C^{\infty}$ and if $(\zeta, v, \psi)=0$, then
$$\|(a, \phi)\|_{L_{k+1, A_{0}}^{2}(X)} \leq C\|(a, \phi)\|_{L_{1, A_{0}}^{p}(X)} .$$
Proof. We consider the cases $k=1, k=2$, and $k \geq 3$ separately. We may further assume without loss of generality that $2<p<4$.

Case $1(\boldsymbol{k}=\mathbf{1})$. Let $p_{0}=p$ and $q_{0}=q=4 p /(4-p)$, so that $1 / p=1 / 4+1 / q$ and $4<q<\infty$. We have a continuous Sobolev multiplication map $L^{4} \times L^{q} \rightarrow L^{p}$ and an embedding $L_{1}^{p} \subset L^{q}$. Since
$$\mathcal{D}_{A_{0}, \Phi_{0}}(a, \phi)=-\{(a, \phi),(a, \phi)\}+(\zeta, v, \psi),$$
then elliptic regularity for $\mathcal{D}_{A_{0}, \Phi_{0}}$ implies that $(a, \phi) \in L_{1}^{p_{1}}$, where $p_{1}=2 p /(4-p)$ and $q_{1}=4 p_{1} /\left(4-p_{1}\right)$, so $2<p_{1}<4$ and $4<q_{1}<\infty$. Here, we used the Sobolev multiplication $L^{4} \times L^{q_{1}} \rightarrow L^{p_{1}}$ to get $\{(a, \phi),(a, \phi)\}$ in $L^{p_{1}}$ and and the embedding $L_{1}^{2} \subset L^{p_{1}}$ to get $(\zeta, v, \psi)$ in $L^{p_{1}}$. Let $p=2+\varepsilon$ and $\delta=\varepsilon /(2-\varepsilon)$, and note that
$$p_{1}=\frac{2 p}{4-p}=\frac{2 p}{2-\varepsilon}=(1+\delta) p>2+\varepsilon .$$
If $p_{j}<4$, we inductively define $p_{j+1}=2 p_{j} /\left(4-p_{j}\right)$ and $q_{j+1}=4 p_{j} /\left(4-p_{j}\right)$ for $j \geq 0$. Therefore, we have $p_{j}>2+\varepsilon$ and thus
$$p_{j+1}=\frac{2 p_{j}}{4-p_{j}}>\frac{2 p_{j}}{2-\varepsilon}=(1+\delta) p_{j}>p_{j}>2+\varepsilon,$$
and so $p_{j+1}>(1+\delta)^{j+1} p$ for $j \geq 0$.
By repeating the above regularity argument when $2<p_{j+1}<4$, using (3.5) at each stage, we see that $(a, \phi) \in L_{1}^{p_{j}}$ for $j \geq 0$. We continue the induction until for large enough $j \geq 0$, we find that $p^{\prime}:=p_{j+1} \geq 8 / 3$ and $q^{\prime}:=q_{j+1} \geq 8$, so $(a, \phi) \in$ $L_{1}^{8 / 3} \subset L^{8}$. Therefore, with $(\zeta, v, \psi) \in L_{1}^{2} \subset L^{4}$ and using the Sobolev multiplication $L^{8} \times L^{8} \rightarrow L^{4}$ to get $\{(a, \phi),(a, \phi)\}$ in $L^{4}$, equation (3.5) gives $(a, \phi) \in L_{1}^{4}$. The

Sobolev multiplication $L_{1}^{4} \times L_{1}^{4} \rightarrow L_{1}^{2}$ implies that the quadratic term $\{(a, \phi),(a, \phi)\}$ is in $L_{1}^{2}$ and so (3.5) gives $(a, \phi) \in L_{2}^{2}$, as required.

Case $2(\boldsymbol{k}=\mathbf{2})$. From the case $k=1$ we continue the induction until $p^{\prime}>8 / 3$ and $q^{\prime}>4$. So, with $(\zeta, v, \psi)$ now in $L_{2}^{2} \subset L_{1}^{p^{\prime}}$, equation (3.5) gives $(a, \phi) \in L_{2}^{p^{\prime}} \subset C^{0}$. The Sobolev multiplication $L_{2}^{p^{\prime}} \times L_{2}^{2} \rightarrow L_{2}^{2}$ implies that the quadratic term $\{(a, \phi),(a, \phi)\}$ is then in $L_{2}^{2}$ and so (3.5) gives $(a, \phi) \in L_{4}^{2}$, as required.

Case $3(\boldsymbol{k} \geq \mathbf{3})$. There is continuous Sobolev multiplication map $L_{k}^{2} \times L_{k}^{2} \rightarrow L_{k}^{2}$ and so the quadratic term $\{(a, \phi),(a, \phi)\}$ is in $L_{k}^{2}$, since $(a, \phi)$ is in $L_{k}^{2}$. Therefore, (3.5) gives $(a, \phi) \in L_{k+1}^{2}$.

This completes the proof of the proposition. \(\square\)

By combining Propositions 3.2 and 3.3 we obtain the desired regularity result for $L_{1}^{2}$ solutions to the inhomogeneous Coulomb gauge and PU(2) monopole equations:

Corollary 3.4. Continue the notation of Proposition 3.2. Let $\left(A_{0}, \Phi_{0}\right)$ be a $C^{\infty}$ pair on the $C^{\infty}$ bundles $\left(\mathfrak{s u}(E), W^{+} \otimes E\right)$ over $X$. Then there is a positive constant $\varepsilon=\varepsilon\left(A_{0}, \Phi_{0}\right)$ such that the following hold. Suppose that either
\begin{itemize}
\item[-] $(a, \phi) \in L_{1}^{2}\left(X, \Lambda^{1} \otimes \mathfrak{s} \mathfrak{u}(E)\right) \oplus L_{1}^{2}\left(X, W^{+} \otimes E\right)$, with $(\vec{\tau}, \vec{\vartheta})=0$, or
\item[-] $(a, \phi) \in L_{2}^{2}\left(X, \Lambda^{1} \otimes \mathfrak{s} \mathfrak{u}(E)\right) \oplus L_{2}^{2}\left(X, W^{+} \otimes E\right)$
\end{itemize}
is a solution on $\left(\mathfrak{s u}(E), W^{+} \otimes E\right)$ to the elliptic system (3.2) over $X$, where $(\zeta, v, \psi)$ is in $L_{k}^{2}$ and $\|(a, \phi)\|_{L^{4}(X)}<\varepsilon$ and $k \geq 0$ is an integer. Then $(a, \phi)$ is in $L_{k+1}^{2}$ and there is a universal polynomial $Q_{k}(x, y)$, with positive real coefficients, depending at most on $\left(A_{0}, \Phi_{0}\right), k$, such that $Q_{k}(0,0)=0$ and
$$\|(a, \phi)\|_{L_{k+1, A_{0}}^{2}(X)} \leq Q_{k}\left(\|(\zeta, v, \psi)\|_{L_{k, A_{0}}^{2}(X)},\|(a, \phi)\|_{L^{2}(X)}\right) .$$
In particular, if $(\zeta, v, \psi)$ is in $C^{\infty}$ then $(a, \phi)$ is in $C^{\infty}$ and if $(\zeta, v, \psi)=0$, then
$$\|(a, \phi)\|_{L_{k+1, A_{0}}^{2}(X)} \leq C\|(a, \phi)\|_{L^{2}(X)} .$$

Remark 3.5. A similar sharp regularity result for solutions to the Coulomb and anti-self-dual equations (that is, $\left.\left(d_{\Gamma}^{*}+d_{\Gamma}^{+}\right) a+(a \wedge a)^{+}=v\right)$ on the product bundle over $S^{4}$ is given by Proposition 4.4.13 in [20]. The reader is forwarned that Corollary 3.4 does not apply directly to show that $L_{1}^{2}$ solutions to the PU(2) monopole equation in [26] are $C^{\infty}$ due to the unfavorable dependence of the constant $\varepsilon\left(A^{\prime}, \Phi^{\prime}, p\right)$ on the approximate PU(2) monopole $\left(A^{\prime}, \Phi^{\prime}\right)$ when $p>2$. However, a local version of this result, namely Corollary 3.11 below, is applicable in this situation. The point is explained further in [26].
3.2. Regularity of $L_{k}^{2}$ solutions to the PU(2) monopole equations. We explain in this subsection why an $L_{k}^{2}$ monopole $(A, \Phi)$ on the $C^{\infty}$ bundles $\left(\mathfrak{s u}(E), W^{+} \otimes E\right)$ over $X$ is gauge equivalent, via an $L_{k+1}^{2}$ determinant-one, unitary automorphism $u$ of the bundle $E$, to a $C^{\infty}$ solution $u(A, \Phi)$ on $\left(\mathfrak{s u}(E), W^{+} \otimes E\right)$ over $X$ when $k \geq 2$. This regularity result contains, as special cases, Theorem 8.8 in [30], for anti-self-dual connections, and Theorem 8.11 in [77] for Seiberg-Witten monopoles.

We will need the following observation concerning the symmetry of the Coulomb gauge equation for pairs; the corresponding fact for connections is explained in [20, p. 56].

Lemma 3.6. Let $(A, \Phi),\left(A_{0}, \Phi_{0}\right)$ be $L_{k}^{2}$ pairs on the bundles $\left(\mathfrak{s u}(E), W^{+} \otimes E\right)$ over $X$. If $\left(A_{0}, \Phi_{0}\right)$ is in Coulomb gauge relative to $(A, \Phi)$, so $d_{A, \Phi}^{0, *}\left(\left(A_{0}, \Phi_{0}\right)-(A, \Phi)\right)=0$ then $(A, \Phi)$ is in Coulomb gauge relative to $\left(A_{0}, \Phi_{0}\right)$, so $d_{A_{0}, \Phi_{0}}^{0, *}\left((A, \Phi)-\left(A_{0}, \Phi_{0}\right)\right)=0$.

Proof. The equation $d_{A, \Phi}^{0, *}\left(\left(A_{0}, \Phi_{0}\right)-(A, \Phi)\right)=0$ is the Euler-Lagrange equation for the functional $\mathcal{G}_{E}^{2, k+1} \ni u \mapsto\left\|u\left(A_{0}, \Phi_{0}\right)-(A, \Phi)\right\|_{L^{2}}^{2}$, while the equation $d_{A_{0}, \Phi_{0}}^{0, *}((A, \Phi)-$ $\left.\left(A_{0}, \Phi_{0}\right)\right)=0$ is the Euler-Lagrange equation for the functional $\mathcal{G}_{E}^{2, k+1} \ni v \mapsto$ $\left\|v(A, \Phi)-\left(A_{0}, \Phi_{0}\right)\right\|_{L^{2}}^{2}$.

But for any $u \in \mathcal{G}_{E}^{2, k+1}$ we have $\left\|u\left(A_{0}, \Phi_{0}\right)-(A, \Phi)\right\|_{L^{2}}=\left\|u^{-1}(A, \Phi)-\left(A_{0}, \Phi_{0}\right)\right\|_{L^{2}}$ and so if the functional $u \mapsto\left\|u\left(A_{0}, \Phi_{0}\right)-(A, \Phi)\right\|_{L^{2}}^{2}$ has a critical point at $u=\mathrm{id}_{E}$, then functional $u^{-1} \mapsto\left\|u^{-1}(A, \Phi)-\left(A_{0}, \Phi_{0}\right)\right\|_{L^{2}}^{2}$ will also have a critical point at $u=\operatorname{id}_{E}$. \(\square\)

Proposition 3.7. Let $X$ be a closed, oriented, Riemannian four-manifold with spin ${ }^{c}$ bundle $W$ and let $E$ be a Hermitian two-plane bundle over $X$. Let $k \geq 2$ be an integer and suppose that $(A, \Phi)$ is an $L_{k}^{2}$ solution to (2.27) on the $C^{\infty}$ bundles $\left(\mathfrak{s u}(E), W^{+} \otimes E\right)$ over $X$. Then there is a $L_{k+1}^{2}$ determinant-one, unitary automorphism $u$ of the bundle $E$ over $X$ such that $u(A, \Phi)$ is $C^{\infty}$ over $X$.

Proof. It suffices, of course, to show that there is an $L_{k+1}^{2}$ gauge transformation $u$ of $E$ over such that $u(A, \Phi)$ is in $L_{k+1}^{2}$. The $C^{\infty}$ pairs $\left(A_{0}, \Phi_{0}\right)$ on $\left(\mathfrak{s} \mathfrak{u}(E), W^{+} \otimes E\right)$ form a dense subspace of the space of $L_{k}^{2}$ pairs and so, given $\varepsilon=\varepsilon(A, \Phi)>0$, there is a $C^{\infty}$ pair $\left(A_{0}, \Phi_{0}\right)$ such that
$$\left\|(A, \Phi)-\left(A_{0}, \Phi_{0}\right)\right\|_{L_{k, A_{0}}^{2}}<\varepsilon .$$
For small enough $\varepsilon$, Proposition 2.8 gives an $L_{k+1}^{2}$ determinant-one, unitary automorphism $u$ of the bundle $E$ such that $u^{-1}\left(A_{0}, \Phi_{0}\right)$ is in Coulomb gauge relative to $(A, \Phi)$ :
$$d_{A, \Phi}^{0, *}\left(u^{-1}\left(A_{0}, \Phi_{0}\right)-(A, \Phi)\right)=0 .$$
Now $u\left(d_{A, \Phi}^{0, *}\left(u^{-1}\left(A_{0}, \Phi_{0}\right)-(A, \Phi)\right)\right)=d_{u(A, \Phi)}^{0, *}\left(\left(A_{0}, \Phi_{0}\right)-u(A, \Phi)\right)$ and so
$$d_{u(A, \Phi)}^{0, *}\left(\left(A_{0}, \Phi_{0}\right)-u(A, \Phi)\right)=0 .$$

Therefore, $\left(A_{0}, \Phi_{0}\right)$ is in Coulomb gauge relative to $u(A, \Phi)$ and Lemma 3.6 implies that $u(A, \Phi)$ is in Coulomb gauge relative to $\left(A_{0}, \Phi_{0}\right)$,
$$d_{A_{0}, \Phi_{0}^{0}}^{0, *}\left(u(A, \Phi)-\left(A_{0}, \Phi_{0}\right)\right)=0 .$$
Let $(a, \phi)=u(A, \Phi)-\left(A_{0}, \Phi_{0}\right)$, so that $(a, \phi) \in L_{k}^{2}\left(X, \Lambda^{1} \otimes \mathfrak{s} \mathfrak{u}(E)\right) \oplus L_{k}^{2}\left(X, W^{+} \otimes E\right)$; the Coulomb gauge condition then takes the simpler form $d_{A_{0}, \Phi_{0}}^{0, *}(a, \phi)=0$. Since $u(A, \Phi)=\left(A_{0}, \Phi_{0}\right)+(a, \phi)$ is an $L_{k}^{2}$ monopole, then $\mathfrak{S}\left(\left(A_{0}, \Phi_{0}\right)+(a, \phi)\right)=0$ and so $(a, \phi)$ is an $L_{k}^{2}$ solution to the quasi-linear elliptic equation
$$\mathcal{D}_{A_{0}, \Phi_{0}}(a, \phi)+\{(a, \phi),(a, \phi)\}=-\mathfrak{S}\left(A_{0}, \Phi_{0}\right),$$
with $C^{\infty}$ data $-\mathfrak{S}\left(A_{0}, \Phi_{0}\right)$. The conclusion now follows from Proposition 3.3 with $\zeta=0$ and $(v, \psi)=-\mathfrak{S}\left(A_{0}, \Phi_{0}\right)$. \(\square\)

One of the convenient practical consequences of Proposition 3.7 is that we can always work, modulo global $L_{k+1}^{2}$ gauge transformations, with $C^{\infty}$ rather than $L_{k}^{2}$ monopoles. For the remainder of this article, therefore, the term 'PU(2) monopole' is generally reserved for $C^{\infty}$ solutions to the perturbed PU(2) monopole equations (2.27). In a similar vein, we generally reserve the terms 'gauge transformation' or 'bundle map' for gauge transformations or bundle maps which are in $C^{\infty}$.

Given Proposition 3.7, we then have the following analogue of Proposition 4.2.16 in [20], the corresponding result for the moduli space of anti-self-dual connections. The proof is standard and so is left to the reader.

Corollary 3.8. Continue the hypotheses of Proposition 3.7. Then for any $k \geq 2$ the natural inclusion of topological spaces $M_{W, E}^{k} \hookrightarrow M_{W, E}^{k+1}$ is a homeomorphism.

Thus, the topology of the moduli space $M_{W, E}^{k}$ of $L_{k}^{2}$ monopoles is independent of the Sobolev spaces used in its construction for $k \geq 2$ and so we simply denote the moduli space by $M_{W, E}$.
3.3. Local regularity and interior estimates for $L_{1}^{2}$ solutions to the inhomogeneous Coulomb gauge and PU(2) monopole equations. In this section we specialize the results of §3.1 to the case where the reference pair is a trivial PU(2) monopole, so $\left(A_{0}, \Phi_{0}\right)=(\Gamma, 0)$ on the bundles $\left(\mathfrak{s u}(E), W^{+} \otimes E\right)$, over an open subset $\Omega \subset X$, where $\Gamma$ is a flat connection.

We continue to assume that $X$ is a closed, oriented four-manifold with metric $g$, spin ${ }^{c}$ bundle $W$, and Hermitian two-plane bundle $E$ extending those on $\Omega \subset X$. We use the inhomogenous estimates and regularity results in our proof of removable singularities for PU(2) monopoles in §4.3 and in our development of the gluing theory for PU(2) monopoles in sequels [26, 27] to the present article - especially to show that a global $L_{1}^{2}$ gluing solution $(a, \phi)$ is actually $C^{\infty}$. We use the homogeneous estimates and regularity results in §4, in our proof of the existence of an Uhlenbeck compactification for the moduli space of PU(2) monopoles.

We have the following local versions of Propositions 3.2 and 3.3 and Corollary 3.4:

Proposition 3.9. Continue the notation of the preceding paragraph. Let $\Omega^{\prime} \Subset \Omega$ be a precompact open subset and let $2 \leq p<4$. Then there are positive constants $\varepsilon=$ $\varepsilon(\Omega, p)$ and $C=C\left(\Omega^{\prime}, \Omega, p\right)$ with the following significance. Suppose that $(a, \phi)$ is an $L_{1}^{2}(\Omega)$ solution to the elliptic system (3.2) over $\Omega$ for $(\vec{\tau}, \vec{\vartheta})=0$, with $\left(A_{0}, \Phi_{0}\right)=(\Gamma, 0)$ and where ( $\zeta, v, \psi$ ) is in $L^{p}(\Omega)$. If $\|(a, \phi)\|_{L^{4}(\Omega)}<\varepsilon$ then ( $a, \phi$ ) is in $L_{1}^{p}\left(\Omega^{\prime}\right)$ and
$$\|(a, \phi)\|_{L_{1, \Gamma}^{p}\left(\Omega^{\prime}\right)} \leq C\left(\|(\zeta, v, \psi)\|_{L^{p}(\Omega)}+\|(a, \phi)\|_{L^{2}(\Omega)}\right) .$$
Proof. Choose an open subset $\Omega^{\prime \prime}$ such that $\Omega^{\prime} \Subset \Omega^{\prime \prime} \Subset \Omega$. Let $\chi$ be $C^{\infty}$ cutoff function such that $\operatorname{supp} \chi \subset \Omega^{\prime \prime}$ and $\chi=1$ on $\Omega^{\prime}$. Let $\beta$ be a cutoff function such that $\beta=1$ on $\operatorname{supp} \chi$ and $\operatorname{supp} \beta \subset \Omega^{\prime \prime}$. Since $(a, \phi)$ is a solution to (3.2) with right-hand side $(\zeta, v, \psi)$ over $\Omega$, then $\chi(a, \phi)$ solves
$$\begin{aligned}
\mathcal{D}_{\Gamma, 0} \chi & (a, \phi)+\{(a, \phi), \chi(a, \phi)\} \\
& =\chi \mathcal{D}_{\Gamma, 0}(a, \phi)+d \chi \otimes(a, \phi)+\chi\{(a, \phi),(a, \phi)\} \\
& =\chi(\zeta, v, \psi)+d \chi \otimes(a, \phi)=:\left(\zeta^{\prime}, v^{\prime}, \psi^{\prime}\right) .
\end{aligned}$$
Thus, $\chi(a, \phi)$ is an $L_{1}^{2}$ solution over $X$ to the linear elliptic system over $X$,
$$\mathcal{D}_{\Gamma, 0}(b, \varphi)+\{\beta(a, \phi),(b, \varphi)\}=\left(\zeta^{\prime}, v^{\prime}, \psi^{\prime}\right),$$
with $L_{1}^{2}$ coefficient $\beta(a, \phi)$ and $L_{1}^{2}$ right-hand side $\left(\zeta^{\prime}, v^{\prime}, \psi^{\prime}\right)$. Since $\|\beta(a, \phi)\|_{L^{4}(X)} \leq$ $\|(a, \phi)\|_{L^{4}(\Omega)}$, the proof of Proposition 3.2 implies that $\chi(a, \phi)$ is in $L_{1}^{p}$ over $X$ if $\varepsilon=\varepsilon(g, \Omega, p)$ is sufficiently small. Thus, $(a, \phi)$ is in $L_{1}^{p}$ over $\Omega^{\prime}$ with
$$\|\chi(a, \phi)\|_{L_{1, \Gamma}^{p}(X)} \leq C\left(\left\|\left(\zeta^{\prime}, v^{\prime}, \psi^{\prime}\right)\right\|_{L^{p}(X)}+\|\chi(a, \phi)\|_{L^{2}(X)}\right),$$
and therefore, for $2 \leq p<4$, we have
$$\|(a, \phi)\|_{L_{1, \Gamma}^{p}\left(\Omega^{\prime}\right)} \leq C\left(\|(\zeta, v, \psi)\|_{L^{p}\left(\Omega^{\prime \prime}\right)}+\|(a, \phi)\|_{L^{p}\left(\Omega^{\prime \prime}\right)}\right) .$$
The preceding bound and the Sobolev embedding $L_{1}^{2} \subset L^{p}$ give the estimate
$$\|(a, \phi)\|_{L^{p}\left(\Omega^{\prime \prime}\right)} \leq c\|(a, \phi)\|_{L_{1, \Gamma}^{2}\left(\Omega^{\prime \prime}\right)} \leq C\left(\|(\zeta, v, \psi)\|_{L^{2}(\Omega)}+\|(a, \phi)\|_{L^{2}(\Omega)}\right) .$$
Combining these inequalities then gives the required $L_{1}^{p}$ estimate for $(a, \phi)$ over $\Omega^{\prime}$. \(\square\)

Proposition 3.10. Continue the notation of Proposition 3.9. Let $k \geq 1$ be an integer, and let $2<p<\infty$. Suppose that either
\begin{itemize}
\item[-] $(a, \phi)$ is an $L_{1}^{p}(\Omega)$, when $(\vec{\tau}, \vec{\vartheta})=0$, or
\item[-] $(a, \phi)$ is an $L_{2}^{2}(\Omega)$
\end{itemize}
solution to the elliptic system (3.2) over $\Omega$ with $\left(A_{0}, \Phi_{0}\right)=(\Gamma, 0)$, where $(\zeta, v, \psi)$ is in $L_{k}^{2}(\Omega)$. Then $(a, \phi)$ is in $L_{k+1}^{2}\left(\Omega^{\prime}\right)$ and there is a universal polynomial $Q_{k}(x, y)$, with positive real coefficients, depending at most on $k, \Omega^{\prime}, \Omega$, such that $Q_{k}(0,0)=0$ and
$$\|(a, \phi)\|_{L_{k+1, \Gamma}^{2}\left(\Omega^{\prime}\right)} \leq Q_{k}\left(\|(\zeta, v, \psi)\|_{L_{k, \Gamma}^{2}(\Omega)},\|(a, \phi)\|_{L_{1, \Gamma}^{p}(\Omega)}\right) .$$

If $(\zeta, v, \psi)$ is in $C^{\infty}(\Omega)$ then $(a, \phi)$ is in $C^{\infty}\left(\Omega^{\prime}\right)$ and if $(\zeta, v, \psi)=0$, then
$$\|(a, \phi)\|_{L_{k+1, \Gamma}^{2}\left(\Omega^{\prime}\right)} \leq C\|(a, \phi)\|_{L_{1, \Gamma}^{p}(\Omega)} .$$
Proof. Again, choose an open subset $\Omega^{\prime \prime}$ such that $\Omega^{\prime} \Subset \Omega^{\prime \prime} \Subset \Omega$, let $\chi$ be $C^{\infty}$ cutoff function such that $\operatorname{supp} \chi \subset \Omega$ and $\chi=1$ on $\Omega^{\prime \prime}$ and let $\beta$ be a cutoff function such that $\beta=1$ on $\operatorname{supp} \chi$ and $\operatorname{supp} \beta \subset \Omega$. Since $(a, \phi)$ is a solution to (3.2) with right-hand side ( $\zeta, v, \psi$ ) over $\Omega$, then $\chi(a, \phi)$ solves
$$\begin{aligned}
\mathcal{D}_{\Gamma, 0} & \chi(a, \phi)+\{\chi(a, \phi), \chi(a, \phi)\} \\
& =\chi \mathcal{D}_{\Gamma, 0}(a, \phi)+d \chi \otimes(a, \phi)+\chi\{(a, \phi),(a, \phi)\}+\chi(\chi-1)\{(a, \phi),(a, \phi)\} \\
& =\chi(\zeta, v, \psi)+d \chi \otimes(a, \phi)+\chi(\chi-1)\{(a, \phi),(a, \phi)\} \\
& =:\left(\zeta^{\prime}, v^{\prime}, \psi^{\prime}\right) .
\end{aligned}$$
Note that $\chi(\zeta, v, \psi)$ is in $L_{k}^{2}(X)$, while $d \chi \otimes(a, \phi)$ is in $L_{1}^{p}(X)$ and the Sobolev multiplication $L^{q} \times L^{q} \rightarrow L^{p_{1}}$ implies that $\chi(\chi-1)\{(a, \phi),(a, \phi)\}$ is in $L^{p_{1}}(X)$, where $p_{1}=q / 2=2 p /(4-p)>p$. Thus, ( $\left.\zeta^{\prime}, v^{\prime}, \psi^{\prime}\right)$ is in $L^{p_{1}}(X)$.

The proof of the case $k=1$ in Proposition 3.3 then implies that $\chi(a, \phi)$ is an $L_{1}^{p_{1}}(X)$ so $(a, \phi)$ is in $L_{1}^{p_{1}}\left(\Omega^{\prime \prime}\right)$. We now repeat this process for each of the remaining steps in the proof of Proposition 3.3, at each stage on successively smaller open subsets $\Omega^{\prime \prime \prime}$ such that $\Omega^{\prime} \Subset \Omega^{\prime \prime \prime} \Subset \Omega^{\prime \prime}$, until we obtain $(a, \phi)$ in $L_{k+1}^{2}\left(\Omega^{\prime}\right)$ and the desired $L_{k+1}^{2}\left(\Omega^{\prime}\right)$ estimate. \(\square\)

Corollary 3.11. Continue the notation of Proposition 3.10. Then there is a positive constant $\varepsilon=\varepsilon(\Omega)$ with the following significance. Suppose that either
\begin{itemize}
\item[-] $(a, \phi)$ is an $L_{1}^{2}(\Omega)$, when $(\vec{\tau}, \vec{\vartheta})=0$, or
\item[-] $(a, \phi)$ is an $L_{2}^{2}(\Omega)$
\end{itemize}
solution to the elliptic system (3.2) over $\Omega$ with $\left(A_{0}, \Phi_{0}\right)=(\Gamma, 0)$, where $(\zeta, v, \psi)$ is in $L_{k}^{2}(\Omega)$ and $\|(a, \phi)\|_{L^{4}(\Omega)}<\varepsilon$. Then $(a, \phi)$ is in $L_{k+1}^{2}\left(\Omega^{\prime}\right)$ and there is a universal polynomial $Q_{k}(x, y)$, with positive real coefficients, depending at most on $k, \Omega^{\prime}, \Omega$, such that $Q_{k}(0,0)=0$ and
$$\|(a, \phi)\|_{L_{k+1, \Gamma}^{2}\left(\Omega^{\prime}\right)} \leq Q_{k}\left(\|(\zeta, v, \psi)\|_{L_{k, \Gamma}^{2}(\Omega)},\|(a, \phi)\|_{L^{2}(\Omega)}\right) .$$
If $(\zeta, v, \psi)$ is in $C^{\infty}(\Omega)$ then $(a, \phi)$ is in $C^{\infty}\left(\Omega^{\prime}\right)$ and if $(\zeta, v, \psi)=0$, then
$$\|(a, \phi)\|_{L_{k+1, \Gamma}^{2}\left(\Omega^{\prime}\right)} \leq C\|(a, \phi)\|_{L^{2}(\Omega)} .$$

Corollary 3.11 thus yields a sharp local elliptic regularity result for PU(2) monopoles $(A, \Phi)$ in $L_{1}^{2}$ which are given to us in Coulomb gauge relative to $(\Gamma, 0)$ : this regularity result is the key ingredient in our proof (given in §4.3) of removable point singularities for PU(2) monopoles.

Proposition 3.12. Continue the notation of Corollary 3.11. Then there is a positive constant $\varepsilon=\varepsilon(\Omega)$ and, if $k \geq 1$ is an integer, there is a positive constant $C=$ $C\left(\Omega^{\prime}, \Omega, k\right)$ with the following significance. Suppose that either
\begin{itemize}
\item[-] $(A, \Phi)$ is an $L_{1}^{2}$, when $(\vec{\tau}, \vec{\vartheta})=0$, or
\item[-] $(A, \Phi)$ is an $L_{2}^{2}$
\end{itemize}
solution to the PU(2) monopole equations (2.27) over $\Omega$, which is in Coulomb gauge over $\Omega$ relative to $(\Gamma, 0)$, so $d_{\Gamma}^{*}(A-\Gamma)=0$, and obeys $\|(A-\Gamma, \Phi)\|_{L^{4}(\Omega)}<\varepsilon$. Then $(A-\Gamma, \Phi)$ is in $C^{\infty}\left(\Omega^{\prime}\right)$ and for any $k \geq 1$,
$$\|(A-\Gamma, \Phi)\|_{L_{k, \Gamma}^{2}\left(\Omega^{\prime}\right)} \leq C\|(A-\Gamma, \Phi)\|_{L^{2}(\Omega)} .$$
Proof. Corollary 3.11 applies to the $L_{1}^{2}(\Omega)$ pair $(a, \phi)=(A-\Gamma, \Phi)$ and yields the required regularity and estimates for $(A-\Gamma, \Phi)$ with $(\zeta, v, \psi)=0$ in (3.2). \(\square\)
3.4. Estimates for PU(2) monopoles in a good local gauge. It remains to combine the local regularity results and estimates of §3.3, for $\mathrm{PU}(2)$ monopoles $(A, \Phi)$ where the connection $A$ is assumed to be in Coulomb gauge relative to the product SO(3) connection $\Gamma$, with Uhlenbeck's local, Coulomb gauge-fixing theorem. We then obtain regularity results and estimates for $\mathrm{PU}(2)$ monopoles $(A, \Phi)$ with small curvature $F_{A}$, parallel to those of Theorem 2.3.8 and Proposition 4.4.10 in [20] for anti-self-dual connections.

In order to apply Corollary 3.11 we need Uhlenbeck's Coulomb gauge-fixing result [95, Theorem 2.1 \& Corollary 2.2]). Let $B$ (respectively, $\bar{B}$ ) be the open (respectively, closed) unit ball centered at the origin in $\mathbb{R}^{4}$ and let $G$ be a compact Lie group. In order to provide universal constants we assume $\mathbb{R}^{4}$ has its standard metric, though the results of this subsection naturally hold for any $C^{\infty}$ Riemannian metric, with comparable constants for metrics which are suitably close.

Theorem 3.13. There are positive constants $c$ and $\varepsilon$ with the following significance. If $2 \leq p<4$ is a constant and $A \in L_{1}^{p}\left(B, \Lambda^{1} \otimes \mathfrak{g}\right) \cap L_{1}^{p}\left(\partial B, \Lambda^{1} \otimes \mathfrak{g}\right)$ is a connection matrix whose curvature satisfies $\left\|F_{A}\right\|_{L^{p}(B)}<\varepsilon$, then there is an gauge transformation $u \in L_{2}^{p}(B, G) \cap L_{2}^{p}(\partial B, G)$ such that $u(A):=u A u^{-1}-(d u) u^{-1}$ satisfies
$$\begin{aligned}
d^{*} u(A) & =0 \text { on } B, \\
\left.\frac{\partial}{\partial r}\right\lrcorner u(A) & =0 \text { on } \partial B, \\
\|u(A)\|_{L_{1}^{p}(B)} & \leq c\left\|F_{A}\right\|_{L^{p}(B)} .
\end{aligned}$$
If $A$ is in $L_{k}^{p}(B)$, for $k \geq 2$, then $u$ is in $L_{k+1}^{p}(B)$. The gauge transformation $u$ is unique up to multiplication by a constant element of $G$.

Remark 3.14. If $G$ is abelian then the requirement that $\left\|F_{A}\right\|_{L^{p}(B)}<\varepsilon$ can be omitted.

It is often useful to rephrase Theorem 3.13 in two other slightly different ways. Suppose $A$ is an $L_{k}^{2}$ connection on a $C^{\infty}$ principal $G$ bundle $P$ over $B$ with $k \geq 2$ and $\left\|F_{A}\right\|_{L^{2}(B)}<\varepsilon$. Then the assertions of Theorem 3.13 are equivalent to each of the following:
\begin{itemize}
\item[-] There is an $L_{k+1}^{2}$ trivialization $\tau: P \rightarrow B \times G$ such that (i) $d_{\Gamma}^{*}(\tau(A)-\Gamma)=0$, where $\Gamma$ is the product connection on $B \times G$, (ii) $\left.\frac{\partial}{\partial r}\right\lrcorner(\tau(A)-\Gamma)=0$, and (iii) $\|(\tau(A)-\Gamma)\|_{L_{1}^{2}(B)} \leq c\left\|F_{A}\right\|_{L^{2}(B)}$.
\item[-] There is an $L_{k+1}^{2}$ flat connection $\Gamma$ on $P$ such that (i) $d_{\Gamma}^{*}(A-\Gamma)=0$, (ii) $\left.\frac{\partial}{\partial r}\right\lrcorner(A-\Gamma)=0$, and (iii) $\|(A-\Gamma)\|_{L_{1}^{2}(B)} \leq c\left\|F_{A}\right\|_{L^{2}(B)}$, and an $L_{k+1}^{2}$ trivialization $\left.P\right|_{B} \simeq B \times G$ taking $\Gamma$ to the product connection.
\end{itemize}

We can now combine Theorem 3.13 with Proposition 3.12 to give the following analogue of Theorem 2.3.8 in [20] — the interior estimate for anti-self-dual connections with $L^{2}$-small curvature.

Corollary 3.15. Let $B \subset \mathbb{R}^{4}$ be the open unit ball with center at the origin with spinc structure $(\rho, W)$, let $U \in B$ be an open subset, and let $\Gamma$ be the product connection on $B \times \operatorname{SO}(3)$. Then there is a positive constant $\varepsilon$ and if $\ell \geq 1$ is an integer, there is a positive constant $C(\ell, U)$ with the following significance. Suppose that either
\begin{itemize}
\item[-] $(A, \Phi)$ is an $L_{1}^{2}$, when $(\vec{\tau}, \vec{\vartheta})=0$, or
\item[-] $(A, \Phi)$ is an $L_{k}^{2}, k \geq \max \{2, \ell\}$,
\end{itemize}
solution to the $\mathrm{PU}(2)$ monopole equations (2.27) over $B$ and that the curvature of the SO(3) connection matrix $A$ obeys $\left\|F_{A}\right\|_{L^{2}(B)}<\varepsilon$. Then there is an $L_{k+1}^{2}$ gauge transformation $u: B \rightarrow \operatorname{SU}(2)$ such that $(u(A)-\Gamma, u \Phi)$ is in $C^{\infty}(B)$ with $d^{*}(u(A)-$ $\Gamma)=0$ over $B$ and
$$\|(u(A)-\Gamma, u \Phi)\|_{L_{\ell, \Gamma}^{2}(U)} \leq C\left\|F_{A}\right\|_{L^{2}(B)}^{1 / 2} .$$
Proof. Let $\varepsilon_{1}$ be the constant in Theorem 3.13 and note that for $\varepsilon \leq \varepsilon_{1}$, Theorem 3.13 (taking $G=\operatorname{SO}(3)$ ) and the Sobolev embedding $L_{1}^{2}(B) \subset L^{4}(B)$ imply that there is an $L_{k+1}^{2}$ gauge transformation $u: B \rightarrow \operatorname{SU}(2)$ (by lifting the SO(3) gauge transformation) such that
$$\begin{aligned}
d_{\Gamma}^{*}(u(A)-\Gamma) & =0 \\
\|u(A)-\Gamma\|_{L^{4}(B)} & \leq c_{1}\left\|F_{A}\right\|_{L^{2}(B)}<c_{1} \varepsilon .
\end{aligned}$$
On the other hand, the quadratic equation for $\Phi$ in (2.27) and Lemma 2.26 give the $L^{4}$ and $L^{2}$ estimates,
$$\begin{aligned}
& \|u \Phi\|_{L^{4}(B)}=\|\Phi\|_{L^{4}(B)} \leq 2\left\|F_{A}^{+}\right\|_{L^{2}(B)}^{1 / 2}, \\
& \|u \Phi\|_{L^{2}(B)} \leq 2\left\|F_{A}\right\|_{L^{1}(B)}^{1 / 2} .
\end{aligned}$$

Let $\varepsilon_{2}$ be the constant in Proposition 3.12. Hence, if $c_{1} \varepsilon \leq \varepsilon_{2}$ and $4 \sqrt{\varepsilon} \leq \varepsilon_{2}$, then Proposition 3.12 implies that $(u(A)-\Gamma, u \Phi)$ obeys
$$\|(u(A)-\Gamma, u \Phi)\|_{L_{\ell, \Gamma}^{2}(U)} \leq C\|(u(A)-\Gamma, u \Phi)\|_{L^{2}(B)},$$
since $d_{\Gamma}^{*}(u(A)-\Gamma)=0$ and $\|(u(A)-\Gamma, u \Phi)\|_{L^{4}(B)}<\varepsilon_{2}$. The desired estimate follows by combining these inequalities for small enough $\varepsilon \leq 1$. \(\square\)

Again, it is often useful to rephrase Corollary 3.15 in the two other slightly different ways. Suppose $\ell \geq 1$ and that $(A, \Phi)$ is a $\operatorname{PU}(2)$ monopole in $L_{k}^{2}$ on $\left(\mathfrak{s u}(E), W^{+} \otimes E\right)$ over the unit ball $B \subset \mathbb{R}^{4}$ with $k \geq \max \{2, \ell\},\left\|F_{A}\right\|_{L^{2}(B)}<\varepsilon$ and $U \subset B$. Then the assertions of Corollary 3.15 are equivalent to each of the following:
\begin{itemize}
\item[-] There is a $C^{\infty}$ trivialization $\tau:\left.E\right|_{B} \rightarrow B \times \mathbb{C}^{2}$ and a $L_{k+1}^{2}$ determinant-one, unitary bundle automorphism $u$ of $\left.E\right|_{B}$ such that, with respect to the product connection $\Gamma$ on $B \times \mathfrak{s u}(2)$, we have (i) $d_{\Gamma}^{*}(\tau u(A)-\Gamma)=0$, and (ii) $\|(\tau u(A)-$ $\Gamma, \tau u \Phi)\left\|_{L_{\ell, \Gamma}^{2}(U)} \leq C\right\| F_{A} \|_{L^{2}(B)}^{1 / 2}$.
\item[-] There is an $L_{k+1}^{2}$ flat connection $\Gamma$ on $\left.\mathfrak{s u}(E)\right|_{B}$ such that (i) $d_{\Gamma}^{*}(A-\Gamma)=0$, and (ii) $\|(A-\Gamma, \Phi)\|_{L_{\ell, \Gamma}^{2}(U)} \leq c\left\|F_{A}\right\|_{L^{2}(B)}^{1 / 2}$, and an $L_{k+1}^{2}$ trivialization $\left.\mathfrak{s} \mathfrak{u}(E)\right|_{B} \simeq B \times \mathfrak{s} \mathfrak{u}(2)$ taking $\Gamma$ to the product connection.
\end{itemize}

Corollary 3.15 immediately yields the following local compactness result for PU(2) monopoles analogous to the local compactness result for anti-self-dual connections in [20, Corollary 2.3.9].

Corollary 3.16. Let $B \subset \mathbb{R}^{4}$ be the open unit ball and spin ${ }^{c}$ structure $(\rho, W)$. Then there is a positive constant $\varepsilon_{0}\left(g, A_{\operatorname{det} W^{+}}, A_{\operatorname{det} E}\right)$ with the following significance. Let $U \Subset B$ be an open subset and let $k \geq 2$ be an integer. If $\left(A_{\alpha}, \Phi_{\alpha}\right)$ is a sequence of PU(2) monopoles in $L_{k}^{2}$ on $\left(\mathfrak{s u}(E), W^{+} \otimes E\right)$ over $B$ such that
$$\left\|F_{A_{\alpha}}\right\|_{L^{2}(B)}<\varepsilon_{0},$$
then the following holds. There are a subsequence $\left\{\alpha^{\prime}\right\} \subset\{\alpha\}$, a sequence of determinantone, unitary $L_{k+1}^{2}$ automorphisms $\left\{u_{\alpha^{\prime}}\right\}$ of $\left.E\right|_{B}$ and a sequence of gauge equivalent pairs $\left(\tilde{A}_{\alpha^{\prime}}, \tilde{\Phi}_{\alpha^{\prime}}\right):=u_{\alpha^{\prime}}\left(A_{\alpha^{\prime}}, \Phi_{\alpha^{\prime}}\right)$ which converge in $L_{k, \text { loc }}^{2}$ on $U$ to a $\mathrm{PU}(2)$ monopole ( $\tilde{A}, \tilde{\Phi}$ ) over $U$.

We will also need interior estimates for PU(2) monopoles in a good local gauge over more general simply-connected regions than the open balls considered in Corollary 3.15. Specifically, recall that a domain $\Omega \subset X$ is strongly simply-connected if it has an open covering by balls $D_{1}, \ldots, D_{m}$ (not necessarily geodesic) such that for $1 \leq r \leq m$ the intersection $D_{r} \cap\left(D_{1} \cup \cdots \cup D_{r-1}\right)$ is connected. We recall (see [20, Proposition 2.2.3] or [43, Proposition I.2.6]):

Proposition 3.17. If $\Gamma$ is a $C^{\infty}$ flat connection on a principal $G$ bundle $P$ over a simply-connected manifold $\Omega$, then there is a $C^{\infty}$ isomorphism $P \simeq \Omega \times G$ taking $\Gamma$ to the product connection on $\Omega \times G$.

More generally, if $A$ is $C^{\infty}$ connection on a $G$ bundle $P$ over a simply-connected manifold-with-boundary $\bar{\Omega}=\Omega \cup \partial \Omega$ with $L^{p}$-small curvature (with $p>2$ ), then Uhlenbeck's theorem implies that $A$ is $L_{2}^{p}$-gauge equivalent to a connection which is $L_{1}^{p}$-close to an $L_{1}^{p}$ flat connection on $P$ (see [96, Corollary 4.3] or [20, p. 163]). The following a priori interior estimate is a straightforward generalization of [20, Proposition 4.4.10]: the method of proof is identical to that described in [20, pp. 161-162] and uses a patching argument for gauge transformations employed by Uhlenbeck in the proof of Theorem 3.6 in [95]. The required bound for the connection in terms of its curvature is obtained by covering the given open region with balls and applying the estimate of Corollary 3.15 in place of Theorem 2.3.8 in [20].

We recall from Proposition 2.16 that any automorphism of the SO(3) bundle $\left.\mathfrak{s} \mathfrak{u}(E)\right|_{\Omega}$ over a simply-connected open subset $\Omega \subset X$ lifts to a determinant-one, unitary bundle automorphism of $\left.E\right|_{\Omega}$. The method of [20, pp. 161-162] then yields:

Proposition 3.18. Let $X$ be a closed, oriented, Riemannian four-manifold with spin ${ }^{c}$ structure $(\rho, W)$ and let $\Omega \subset X$ be a strongly simply-connected open subset. Then there is a positive constant $\varepsilon(\Omega)$ with the following significance. For $\Omega^{\prime} \Subset \Omega$ a precompact open subset and an integer $\ell \geq 1$, there is a constant $C\left(\ell, \Omega^{\prime}, \Omega\right)$ such that the following holds. Suppose ( $A, \Phi$ ) is a $\operatorname{PU}(2)$ monopole in $L_{k}^{2}$ on ( $\left.\mathfrak{s u}(E), W^{+} \otimes E\right)$ over $\Omega$ with $k \geq \max \{2, \ell\}$ such that
$$\left\|F_{A}\right\|_{L^{2}(\Omega)}<\varepsilon .$$
Then there is an $L_{k+1}^{2}$ flat connection $\Gamma$ on $\left.\mathfrak{s u}(E)\right|_{\Omega^{\prime}}$ such that
$$\|(A-\Gamma, \Phi)\|_{L_{\ell, \Gamma}^{2}\left(\Omega^{\prime}\right)} \leq C\left\|F_{A}\right\|_{L^{2}(\Omega)}^{1 / 2},$$
and an $L_{k+1}^{2}$ trivialization $\left.\mathfrak{s u}(E)\right|_{\Omega^{\prime}} \simeq \Omega^{\prime} \times \mathfrak{s u}(2)$ taking $\Gamma$ to the product connection.

\section*{4. Uhlenbeck compactification for the moduli space of PU(2) MONOPOLES}

Our goal in this section is to prove the existence of an Uhlenbeck-type compactification of the moduli space of PU(2) monopoles analogous to the Uhlenbeck compactification of the moduli space of anti-self-dual connections [20]. A compactification of this type, for the unperturbed moduli space of PU(2) monopoles, was first outlined by Pidstrigach and Tyurin [71, 74]. By construction our holonomy perturbations are continuous with respect Uhlenbeck limits, as outlined in §4.5.2.

In §4.1 we establish the Bochner-Weitzenböck formulas for the coupled Dirac operators $D_{A}$ and $D_{A}^{*}$ and the a priori bounds satisfied by the section $\Phi$ and the curvature $F_{A}$, if $(A, \Phi)$ is a PU(2) monopole on $\left(\mathfrak{s u}(E), W^{+} \otimes E\right)$; these generalize the well-known a priori bounds for Seiberg-Witten monopoles [47, 62, 77]. In our proof of removable singularities we need to take into account the variation of spin ${ }^{c}$ structures with the Riemannian metric and the rescaling behavior of the PU(2) equations: this variation is discussed in §4.2.