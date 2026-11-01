---
retention_scope: session
part: 1
total_parts: 5
---

[Part 1/5 of: [PDF] On tamed almost complex four manifolds]

---
source_file: 1712_02948.pdf
converter: mathpix
format: mmd
---

\title{
On Tamed Almost Complex Four-Manifolds*
}

\author{
Qiang Tan, Hongyu Wang ${ }^{\dagger}$, Jiuru Zhou and Peng Zhu \\ Dedicated to professor Kung-Ching Chang on the occasion of his 85th birthday
}

\begin{abstract}
This paper proves that on any tamed closed almost complex four-manifold $(M, J)$ whose dimension of $J$-anti-invariant cohomology is equal to the self-dual second Betti number minus one, there exists a new symplectic form compatible with the given almost complex structure $J$. In particular, if the self-dual second Betti number is one, we give an affirmative answer to a question of Donaldson for tamed closed almost complex four-manifolds. Our approach is along the lines used by Buchdahl to give a unified proof of the Kodaira conjecture.
\end{abstract}

Keywords: $\omega$-tame(compatible) almost complex structure; $J$-anti-invariant cohomology; positive $(1,1)$ current; local symplectic property; $J$-holomorphic curve.

2010 Mathematics Subject Classification: 53D35, 53C56, 53C65

\section*{1 Introduction}

Suppose that $M$ is a closed, oriented, smooth 4-manifold and suppose that $\omega$ is a symplectic form on $M$ that is compatible with the orientation. An endomorphism, $J$, of $T M$ is said to be an almost complex structure when $J^{2}=-i d_{T M}$. Such an almost complex structure is said to be tamed by $\omega$ when the bilinear form $\omega(\cdot, J \cdot)$ is positive definite. The almost complex structure $J$ is said to be compatible (or calibrate) with $\omega$ when this same bilinear form is also symmetric, that is, $\omega(\cdot, J \cdot)>0$ and $\omega(J \cdot, J \cdot)=\omega(\cdot, \cdot)$. M. Gromov [32] observed that tamed almost complex structures and also compatible almost complex structures always exist. Let $\mathcal{J}(M)$ be the space of all almost complex structures on $M$, $\mathcal{J}_{c}(M, \omega)$ the space of all $\omega$-compatible almost complex structures on $M$ and $\mathcal{J}_{\tau}(M, \omega)$ the space of all $\omega$-tame almost complex structures on $M$. Note that $\mathcal{J}_{c}(M, \omega)$ and $\mathcal{J}_{\tau}(M, \omega)$ are even contractible, and $\mathcal{J}_{\tau}(M, \omega)$ is open in the space $\mathcal{J}(M)$ (This is defined using the $C^{\infty}$-Fréchet space topology (cf. [2])). S. K. Donaldson [16] posed the following question: If an almost complex structure is tamed by a given symplectic form $\omega$, must it be compatible with a new symplectic form? That is, which tamed almost complex 4-manifolds can be calibrated? This is a natural question to arise in the context of calibrated geometries

\footnotetext{
*The work is supported by PRC grant NSFC 11701226 (Tan), 11371309, 11771377 (Wang), 11426195 (Zhou), 11471145 (Zhu); Natural Science Foundation of Jiangsu Province BK20170519 (Tan); University Scinence Research Project of Jiangsu Province 15KJB110024 (Zhou); Foundation of Yangzhou University 2015CXJ003 (Zhou).
${ }^{\dagger}$ E-mail:hywang@yzu.edu.cn
}

33,35,36]. Since any almost complex 4-manifold $(M, J)$ has the local symplectic property [54, 68], that is, for any $p \in M$, there exists a $J$-compatible symplectic 2-form $\omega_{p}$ on a neighborhood $U_{p}$ of $p$ which can be viewed as a calibration on $U_{p}$ [33, 35, 36].

Note that there are topological obstructions to the existence of almost complex structures on an even dimensional manifold. For a closed 4-manifold, a necessary condition is that $1-b^{1}+b^{+}$be even [3], where $b^{1}$ is the first Betti number and $b^{+}$is the number of positive eigenvalues of the quadratic form on $H^{2}(M ; \mathbb{R})$ defined by the cup product, hence the condition is either $b^{1}$ be even and $b^{+}$odd, or $b^{1}$ be odd and $b^{+}$even. It is a well-known fact (that is the Kodaira conjecture [50]) that any closed complex surface with $b^{1}$ even is Kähler. The direct proofs have been given by N. Buchdahl [7] and A. Lamari [53]. R. Harvey and H. B. Lawson, Jr. (Theorems 26 and 38 in [34]) proved that for any closed complex surface $(M, J)$ with $b^{1}$ even, there exists a symplectic form $\omega$ on $M$ by which $J$ is tamed. Thus, Donaldson's question for tamed almost complex 4-manifolds (in particular, $b^{+}=1$ ) is related to the Kodaira conjecture for complex surfaces (cf. [18]).

When $M=\mathbb{C} P^{2}$ for every tamed almost complex structure $J$, there exists a symplectic form $\Omega$ on $\mathbb{C} P^{2}$ with which $J$ is compatible. It follows from M. Gromov's result [32] on pseudoholomorphic curves and C. H. Taubes' result [75] on symplectic forms on $\mathbb{C} P^{2}$.

Donaldson suggests in [16] an approach to his question, one along the lines used by S.-T. Yau in [82] to prove the Calabi conjecture. This approach is considered by V. Tosatti, B. Weinkove, and S.-T. Yau in [77, 80].

Taubes considered in [76] Donaldson's question as follows: Fix a closed almost complex 4-manifold $M$ with $b^{+}=1$ and with a given symplectic form $\omega$. He proves in [76] the following: The Fréchet space, $\mathcal{J}_{\tau}(M, \omega)$, of tamed almost complex structures as defined by $\omega$ has an open and dense subset whose almost complex structures are compatible with a new symplectic form that is cohomologous to $\omega$.

Very recently, T.-J. Li and W. Zhang [59] studied Nakai-Moishezon type question and Donaldson's "tamed to compatible" question for almost complex structures on rational 4-manifolds. By extending Taubes' subvarieties-current-form technique to J-nef genus 0 classes, they gave affirmative answers of these two questions for all tamed almost complex structures on $S^{2}$ bundles over $S^{2}$ as well as for many geometrically interesting tamed almost complex structures on other rational four manifolds.

For a closed almost complex 4-manifold $(M, J)$, T.-J. Li and W. Zhang [58] introduced subgroups $H_{J}^{+}$and $H_{J}^{-}$, of the real degree 2 de Rham cohomology group $H^{2}(M ; \mathbb{R})$, as the sets of cohomology classes which can be represented by $J$-invariant and $J$-anti-invariant real 2-forms. Let us denote by $h_{J}^{+}$and $h_{J}^{-}$the dimensions of $H_{J}^{+}$and $H_{J}^{-}$, respectively. T. Draghici, T.-J. Li and W. Zhang [18] proved that for a closed almost complex 4-manifold $(M, J)$,
$$H^{2}(M ; \mathbb{R})=H_{J}^{+} \oplus H_{J}^{-} .$$
If $J$ is integrable, the induced decomposition is nothing but the classical real Hodge-Dolbeault decomposition of $H^{2}(M ; \mathbb{R})$ (cf. [3, 18]), that is,
$$H_{J}^{+}=H_{\bar{\partial}}^{1,1} \cap H^{2}(M ; \mathbb{R}) \text { and } H_{J}^{-}=\left(H_{\bar{\partial}}^{2,0} \oplus H_{\bar{\partial}}^{0,2}\right) \cap H^{2}(M ; \mathbb{R}) \text {. }$$

In this paper, we give an affirmative answer to Donaldson's question when $h_{J}^{-}=b^{+}-1$ by using very different approach. In particular, if the self-dual second Betti number is one, we give an affirmative answer to the conjecture of Tosatti, Weinkove and Yau [77]. Our approach is along the lines used by Buchdahl in [7] to give a unified proof of the Kodaira conjecture.

Theorem 1.1. Let $M$ be a closed symplectic 4-manifold with symplectic form $\omega$. Suppose that $J$ is an $\omega$-tame almost complex structure on $M$ and $h_{J}^{-}=b^{+}-1$. Then there exists a new symplectic form $\Omega$ that is compatible with $J$.

Remark 1.2. If $(M, J)$ is a closed complex surface with $b^{1}$ even, then there exists a symplectic form $\omega$ by which $J$ is tamed (see Theorem 26 and 38 in [34]) and $h_{J}^{-}=b^{+}-1$. Thus, the above theorem gives an affirmative answer to the Kodaira conjecture in symplectic version.

Note that if $(M, J)$ is a tamed, closed almost complex 4-manifold, then it is easy to see that $0 \leq h_{J}^{-} \leq b^{+}-1$ (cf. [73, 78]), thus $h_{J}^{-}=b^{+}-1$ is a technical condition. Hence if $b^{+}=1$, then $h_{J}^{-}=b^{+}-1=0$. As a direct consequence of Theorem 1.1, we have the following corollary which gives an affirmative answer to Conjecture 1.2 in [77] (see also the description in [80]).

Corollary 1.3. Let $(M, J)$ be a tamed, closed, almost complex 4-manifold with a taming form $\omega$. When $b^{+}=1$, then exists a new symplectic form $\Omega$ that is compatible with almost complex structure $J$ and cohomologous to $\omega$.

We have shown that generically $h_{J}^{-}=0$ (cf. [73,74]). So when $b^{+}>1$ the hypothesis of Theorem 1.1 can at best be satisfied by very special almost complex structures (for example, $J$ is integrable). Hence, it is natural to ask the following question,

Question 1.4. (1) Which is the sufficient and necessary condition for Donaldson's "tamed to compatible" question?
(2) Is it possible to construct a closed symplectic 4-manifold $(M, \omega)$ with $b^{+}>1$ such that for any $\omega$-compatible almost complex structure $J, h_{J}^{-}$is strictly less than $b^{+}-1$ ?

The remainder of the paper is organized as follows:
Section 2: Preliminaries. In this section, it is similar to $\partial \bar{\partial}$ operator in classical complex analysis, we introduce the operators $\widetilde{\mathcal{D}}_{J}^{+}$and $\mathcal{D}_{J}^{+}$on tamed almost complex 4-manifolds.

Section 3: The intersection pairing on weakly $\widetilde{\mathcal{D}}_{J}^{+}$-closed (1,1)-forms. In this section, as done in complex surfaces, we give the notion of weakly $\widetilde{\mathcal{D}}_{J}^{+}$-closed (1,1)-form which is similar to the weakly $\partial \bar{\partial}$-closed (1,1)-form in classical complex analysis. We investigate the intersection pairing on weakly $\widetilde{\mathcal{D}}_{J}^{+}$-closed (1,1)-forms, and obtain a key lemma (Lemma 3.12) as done in compact complex surfaces.

Section 4: The tamed almost complex 4-manifolds with $h_{J}^{-}=b^{+}-1$. In this section, based on the key lemma proved in Section 3, we give a proof of our main theorem
which follows mainly Buchdahl's proof of the fact that compact complex surfaces with $b_{1}$ even is Kähler.

To prove the main result, we extend several notions and important theorems from complex analysis to the almost complex setting which are necessary for the proof of the main theorem. Many of them are interesting by themselves. The rest of this paper contains three appendices:

Appendix A: Elementary pluripotential theory
A.1: $J$-plurisubharmonic functions on almost complex manifolds.
A.2: Kiselman's minimal principle for $J$-plurisubharmonic functions.
A.3: Hörmander's $L^{2}$-estimates on tamed almost complex 4-manifolds.
A.4: The singularities of $J$-plurisubharmonic functions on tamed almost complex 4-manifolds.

Appendix B: Siu's decomposition theorem on tamed almost complex 4-manifolds
B.1: Lelong numbers of closed positive (1, 1)-currents on tamed complex 4-manifolds.
B.2: Siu's decomposition formula of closed positive $(1,1)$-currents on tamed almost complex 4-manifolds.

Appendix C: Demailly's approximation theorem on tamed almost complex 4-manifolds
C.1: Exponential map associated to the second canonical connection.
C.2: Regularization of quasi- $J$-plurisubharmonic functions on tamed almost Hermitian 4-manifolds.
C.3: Regularization of closed positive (1, 1)-currents on tamed almost complex 4-manifolds.
C.4: Demailly's approximation theorem on tamed almost complex 4-manifolds.

\section*{2 Preliminaries}

Suppose that $M$ is an almost complex manifold with almost complex structure $J$, then for any $x \in M, T_{x}(M) \otimes_{\mathbb{R}} \mathbb{C}$ which is the complexification of $T_{x}(M)$, has the following decomposition (cf. [2, 48, 58]):
$$T_{x}(M) \otimes_{\mathbb{R}} \mathbb{C}=T_{x}^{1,0}+T_{x}^{0,1},$$
where $T_{x}^{1,0}$ and $T_{x}^{0,1}$ are the eigenspaces of $J$ corresponding to the eigenvalues $\sqrt{-1}$ and $-\sqrt{-1}$, respectively. A complex tangent vector is of type $(1,0)$ (resp. $(0,1)$ ) if it belongs to $T_{x}^{1,0}$ (resp. $T_{x}^{0,1}$ ). Let $T(M) \otimes_{\mathbb{R}} \mathbb{C}$ be the complexification of the tangent bundle. Similarly, let $T^{*} M \otimes_{\mathbb{R}} \mathbb{C}$ denote the complexification of the cotangent bundle $T^{*} M . J$ can act on $T^{*} M \otimes_{\mathbb{R}} \mathbb{C}$ as follows:
$$\forall \alpha \in T^{*} M \otimes_{\mathbb{R}} \mathbb{C}, \quad J \alpha(\cdot)=-\alpha(J \cdot) .$$
Hence $T^{*} M \otimes_{\mathbb{R}} \mathbb{C}$ has the following decomposition according to the eigenvalues $\mp \sqrt{-1}$ :
$$T^{*} M \otimes_{\mathbb{R}} \mathbb{C}=\Lambda_{J}^{1,0} \oplus \Lambda_{J}^{0,1} .$$

We can form exterior bundle $\Lambda_{J}^{p, q}=\Lambda^{p} \Lambda_{J}^{1,0} \otimes \Lambda^{q} \Lambda_{J}^{0,1}$. Let $\Omega_{J}^{p, q}(M)$ denote the space of $C^{\infty}$ sections of the bundle $\Lambda_{J}^{p, q}$. The exterior differential operator acts on $\Omega_{J}^{p, q}$ as follows:
$$d \Omega_{J}^{p, q} \subset \Omega_{J}^{p-1, q+2}+\Omega_{J}^{p+1, q}+\Omega_{J}^{p, q+1}+\Omega_{J}^{p+2, q-1} .$$
Hence, $d$ has the following decomposition:
$$d=A_{J} \oplus \partial_{J} \oplus \bar{\partial}_{J} \oplus \bar{A}_{J} .$$
Recall that on an almost complex manifold $(M, J)$, there exists the Nijenhuis tensor $\mathcal{N}_{J}$ as follows:
$$4 \mathcal{N}_{J}=[J X, J Y]-[X, Y]-J[X, J Y]-J[J X, Y],$$
where $X, Y \in T M$. By the Newlander-Nirenberg Theorem [2], $\mathcal{N}_{J}=0$ if and only if $J$ is integrable, that is, $J$ is a complex structure. If $J$ is integrable, then $d=\partial_{J} \oplus \bar{\partial}_{J}$ (For details, see [2,48,58]). By a direct calculation, we have: For any $\alpha \in\left(\Omega_{J}^{p, q}+\Omega_{J}^{q, p}\right)_{\mathbb{R}} \subset \Omega_{\mathbb{R}}^{p+q}$,
$$\left(A_{J}+\bar{A}_{J}\right)(\alpha)\left(X_{1}, \ldots, X_{p+q+1}\right)=\sum_{i<j}(-1)^{i+j+1} \alpha\left(\mathcal{N}_{J}\left(X_{i}, X_{j}\right), X_{1}, \ldots, \hat{X}_{i}, \ldots, \hat{X}_{j}, \ldots, X_{p+q+1}\right),$$
where $X_{1}, \ldots, X_{p+q+1} \in T(M)$ (cf. [48, 77, 79]).
Let $(M, J)$ be an almost complex 4-manifold. After a simple calculation, we can get the following properties:
$$\begin{gathered}
d: \Omega_{\mathbb{R}}^{0} \longrightarrow \Omega_{\mathbb{R}}^{1}, \quad d=\partial_{J}+\bar{\partial}_{J} . \\
A_{J} \circ \partial_{J}+\bar{\partial}_{J}^{2}+\bar{A}_{J} \circ \bar{\partial}_{J}+\partial_{J}^{2}=0: \Omega_{\mathbb{R}}^{0} \longrightarrow\left(\Omega_{J}^{2,0}+\Omega_{J}^{0,2}\right)_{\mathbb{R}} . \\
\partial_{J} \circ \bar{\partial}_{J}+\bar{\partial}_{J} \circ \partial_{J}=0: \Omega_{\mathbb{R}}^{0} \longrightarrow \Omega_{\mathbb{R}}^{1,1} . \\
d: \Omega_{\mathbb{R}}^{1} \longrightarrow \Omega_{\mathbb{R}}^{2}, \quad d=A_{J}+\partial_{J}+\bar{\partial}_{J}+\bar{A}_{J} . \\
d:\left(\Omega^{2,0}+\Omega^{0,2}\right)_{\mathbb{R}} \longrightarrow\left(\Omega^{1,2}+\Omega^{2,1}\right)_{\mathbb{R}}, \quad d=A_{J}+\partial_{J}+\bar{\partial}_{J}+\bar{A}_{J} . \\
d: \Omega_{\mathbb{R}}^{1,1} \longrightarrow\left(\Omega^{1,2}+\Omega^{2,1}\right)_{\mathbb{R}}, \quad d=\partial_{J}+\bar{\partial}_{J} . \\
\partial_{J} \circ \bar{\partial}_{J}+\bar{\partial}_{J} \circ \partial_{J}=0: \Omega_{\mathbb{R}}^{1,1} \longrightarrow \Omega_{\mathbb{R}}^{4} .
\end{gathered}$$

Suppose that $(M, J)$ is an almost complex 4-manifold. One can construct a $J$-invariant Riemannian metric $g$ on $M$, namely, $g(J X, J Y)=g(X, Y)$ for all tangent vector fields $X$ and $Y$ on $M$. Such a metric $g$ is called an almost Hermitian metric (real) on $(M, J)$. This then in turn gives a $J$-compatible nondegenerate 2-form $F$ on $M$ by $F(X, Y)=$ $g(J X, Y)$, called the fundamental 2-form. Such a quadruple $(M, g, J, F)$ is called an almost Hermitian 4-manifold. Thus an almost Hermitian structure on $M$ is a triple $(g, J, F)$. If $J$ is integrable, the triple $(g, J, F)$ is called an Hermitian structure (In complex coordinate system, the almost Hermitian metric is written as $h=g-\sqrt{-1} F$.). By using almost Hermitian structure $(g, J, F)$, we can define a volume form $d \mu_{g}=F^{2} / 2$ with
$$\int_{M} d \mu_{g}=1$$
by rescaling in the conformal equivalent class $[g]$. If the 2-form $F$ is closed, then the triple $(g, J, F)$ is called an almost Kähler structure. When the two conditions hold simultaneously, the $(g, J, F)$ defines a Kähler structure on $M$ (cf. [2, 48]). Note that although $M$ need not admit a symplectic condition (i.e. $d F=0$ ), P. Gauduchon [27] has shown that for a closed almost Hermitian 4-manifold $(M, g, J, F)$ there is a conformal rescaling of the metric $g$, unique up to positive constant, such that the associated form satisfies $\bar{\partial}_{J} \partial_{J} F=0$. This metric is called Gauduchon metric.

Let $\Omega_{\mathbb{R}}^{2}(M)$ denote the space of real smooth 2-forms on $M$, that is, the real $C^{\infty}$ sections of the bundle $\Lambda_{\mathbb{R}}^{2}(M)$. The almost complex structure $J$ acts on $\Omega_{\mathbb{R}}^{2}(M)$ as an involution by $\alpha(\cdot, \cdot) \mapsto \alpha(J \cdot, J \cdot)$, thus we have the splitting into $J$-invariant and $J$-anti-invariant 2-forms respectively
$$\Lambda_{\mathbb{R}}^{2}=\Lambda_{J}^{+} \oplus \Lambda_{J}^{-},$$
where the bundles $\Lambda_{J}^{ \pm}$are defined by
$$\Lambda_{J}^{ \pm}=\left\{\alpha \in \Lambda_{\mathbb{R}}^{2} \mid \alpha(J \cdot, J \cdot)= \pm \alpha(\cdot, \cdot)\right\} .$$
We will denote by $\Omega_{J}^{+}$and $\Omega_{J}^{-}$, respectively, the $C^{\infty}$ sections of the bundles $\Lambda_{J}^{+}$and $\Lambda_{J}^{-}$. For $\alpha \in \Omega_{\mathbb{R}}^{2}(M)$, denote by $\alpha_{J}^{+}$and $\alpha_{J}^{-}$, respectively, the $J$-invariant and $J$-anti-invariant components of $\alpha$ with respect to the decomposition (2.14). We will also use the notation $\mathcal{Z}_{\mathbb{R}}^{2}$ for the space of real closed 2-forms on $M$ and $\mathcal{Z}_{J}^{ \pm}=\mathcal{Z}_{\mathbb{R}}^{2} \cap \Omega_{J}^{ \pm}$for the corresponding projections.

Li and Zhang have defined in [58] the $J$-invariant and $J$-anti-invariant cohomology subgroups $H_{J}^{ \pm}$of $H^{2}(M ; \mathbb{R})$ as follows:
$$H_{J}^{ \pm}=\left\{\mathfrak{a} \in H^{2}(M ; \mathbb{R}) \mid \exists \alpha \in \mathcal{Z}_{J}^{ \pm} \text {such that }[\alpha]=\mathfrak{a}\right\} ;$$
$J$ is said to be $C^{\infty}$-pure if $H_{J}^{+} \cap H_{J}^{-}=\{0\}, C^{\infty}$-full if $H_{J}^{+}+H_{J}^{-}=H^{2}(M ; \mathbb{R}) . \quad J$ is $C^{\infty}$-pure and full if and only if $H^{2}(M ; \mathbb{R})=H_{J}^{+} \oplus H_{J}^{-}$.

Proposition 2.1. (Theorem 2.2 in [18]) If $M$ is a closed almost complex 4-manifold $(M, J)$, then the almost complex structure $J$ on $M$ is $C^{\infty}$-pure and full. Thus, there is a direct sum cohomology decomposition
$$H^{2}(M ; \mathbb{R})=H_{J}^{+} \oplus H_{J}^{-} .$$
Let us denote by $h_{J}^{+}$and $h_{J}^{-}$the dimensions of $H_{J}^{+}$and $H_{J}^{-}$, respectively. Then we have $b^{2}=h_{J}^{+}+h_{J}^{-}$, where $b^{2}$ is the second Betti number.

When $J$ is integrable, there is the Dolbeault decomposition which has long been discovered.

Remark 2.2. (cf. [3, 18]) If $J$ is integrable on a closed 4-manifold, then
$$H_{J}^{+}=H_{\bar{\partial}_{J}}^{1,1} \cap H^{2}(M ; \mathbb{R}) ; \quad H_{J}^{-}=\left(H_{\bar{\partial}_{J}}^{2,0} \oplus H_{\bar{\partial}_{J}}^{0,2}\right) \cap H^{2}(M ; \mathbb{R}) .$$

Let us denote the dimension of $H_{\bar{\partial}_{J}}^{p, q}$ by $h_{\bar{\partial}_{J}}^{p, q}$. So if $J$ is integrable, it follows from the above proposition that $h_{J}^{+}=h_{\bar{\partial}_{J}}^{1,1}, \quad h_{J}^{-}=2 h_{\bar{\partial}_{J}}^{2,0}$. So in this case, using the signature theorem we get
$$h_{J}^{+}=\left\{\begin{array}{ll}
b^{-}+1 & \text { if } b_{1} \text { even } \\
b^{-} & \text {if } b_{1} \text { odd, }
\end{array} \quad h_{J}^{-}= \begin{cases}b^{+}-1 & \text { if } b_{1} \text { even } \\
b^{+} & \text {if } b_{1} \text { odd. }\end{cases}\right.$$

Since $(M, g, J, F)$ is a closed almost Hermitian 4-manifold, the Hodge star operator $*_{g}$ gives the self-dual, anti-self-dual decomposition of the bundle of 2-forms (see [16,17]):
$$\Lambda_{\mathbb{R}}^{2}=\Lambda_{g}^{+} \oplus \Lambda_{g}^{-} .$$
We denote by $\Omega_{g}^{ \pm}$the spaces of smooth sections of $\Lambda_{g}^{ \pm}$, and by $\alpha_{g}^{+}$and $\alpha_{g}^{-}$respectively the self-dual and anti-self-dual components of a 2-form $\alpha$. Since the Hodge-de Rham Laplacian $\Delta_{g}=d d^{*}+d^{*} d$, where $d^{*}=-*_{g} d *_{g}$ is the codifferential operator with respect to the metric $g$, commutes with $*$, the decomposition (2.15) holds for the space $\mathcal{H}_{g}$ of harmonic 2-forms as well. By Hodge theory, this induces cohomology decomposition by the metric $g$ :
$$\mathcal{H}_{g}=\mathcal{H}_{g}^{+} \oplus \mathcal{H}_{g}^{-} .$$
Suppose $\alpha \in \Omega_{g}^{+}$and its Hodge decomposition [16,17] is:
$$\alpha=\alpha_{h}+d \theta+d^{*} \psi=\alpha_{h}+d \theta+*_{g} d \varphi,$$
where $\alpha_{h}$ is a harmonic 2-form and $\varphi=-*_{g} \psi$. Then, since $*_{g} \alpha=\alpha$, the uniqueness of the Hodge decomposition gives that $\theta=\varphi$, and $\alpha_{h}=*_{g} \alpha_{h}$, so $\alpha=\alpha_{h}+d_{g}^{+}(2 \theta)$, where
$$d_{g}^{ \pm}: \Omega_{\mathbb{R}}^{1} \rightarrow \Omega_{g}^{ \pm}$$
is the first-order differential operator formed from the composite of the exterior derivative $d: \Omega_{\mathbb{R}}^{1} \rightarrow \Omega_{\mathbb{R}}^{2}$ with the algebraic projections $P_{g}^{ \pm}=\frac{1}{2}\left(1 \pm *_{g}\right)$ from $\Omega_{\mathbb{R}}^{2}$ to $\Omega_{g}^{ \pm}$, where $d_{g}^{ \pm}=P_{g}^{ \pm} d$. So we can get the following Hodge decompositions (see [17]):
$$\Omega_{g}^{+}=\mathcal{H}_{g}^{+} \oplus d_{g}^{+}\left(\Omega^{1}\right), \quad \Omega_{g}^{-}=\mathcal{H}_{g}^{-} \oplus d_{g}^{-}\left(\Omega^{1}\right) .$$
Note that
$$d_{g}^{ \pm} d^{*}: \Omega_{g}^{ \pm} \rightarrow \Omega_{g}^{ \pm}$$
are self-adjoint strongly elliptic operators and $\operatorname{ker} d_{g}^{ \pm} d^{*}=\mathcal{H}_{g}^{ \pm}$. If $d_{g}^{+} u$ is $d$-closed, that is, $d d_{g}^{+} u=0$, then
$$0=\int_{M} d d_{g}^{+} u \wedge u=-\int_{M} d_{g}^{+} u \wedge d u=-\int_{M}\left|d_{g}^{+} u\right|^{2},$$
so $d_{g}^{+} u=0$. Similarly, for any $u \in \Omega_{\mathbb{R}}^{1}$, if $d_{g}^{+} u=0$,
$$0=\int_{M} d u \wedge d u=\int_{M}\left|d_{g}^{+} u\right|^{2}-\int_{M}\left|d_{g}^{-} u\right|^{2}=-\int_{M}\left|d_{g}^{-} u\right|^{2},$$
so $d_{g}^{-} u=0$ too, therefore we can get $d u=0$ (cf. [16,17]).

We define,
$$H_{g}^{ \pm}=\left\{\mathfrak{a} \in H^{2}(M ; \mathbb{R}) \mid \exists \alpha \in \mathcal{Z}_{g}^{ \pm}:=\mathcal{Z}_{\mathbb{R}}^{2} \cap \Omega_{g}^{ \pm} \text {such that } \mathfrak{a}=[\alpha]\right\} .$$
There are the following relations between the decompositions (2.14) and (2.15) on an almost Hermitian 4-manifold:
$$\begin{gathered}
\Lambda_{J}^{+}=\mathbb{R} \cdot F \oplus \Lambda_{g}^{-}, \quad \Lambda_{g}^{+}=\mathbb{R} \cdot F \oplus \Lambda_{J}^{-}, \\
\Lambda_{J}^{+} \cap \Lambda_{g}^{+}=\mathbb{R} \cdot F, \quad \Lambda_{J}^{-} \cap \Lambda_{g}^{-}=\{0\} .
\end{gathered}$$
It is easy to see that $H_{J}^{-} \subset H_{g}^{+}$and $H_{g}^{-} \subset H_{J}^{+}$(cf. [19, 73]).
Let $b^{+}$the self-dual Betti number, and $b^{-}$the anti-self-dual Betti number of $M$, hence $b^{2}=b^{+}+b^{-}$. Thus, for a closed almost Hermitian 4-manifold $(M, g, J, F)$, we have (cf. [73]):
$$\mathcal{Z}_{J}^{-} \subset \mathcal{Z}_{g}^{+}, \quad \mathcal{Z}_{g}^{-} \subset \mathcal{Z}_{J}^{+}, b^{+}+b^{-}=h_{J}^{+}+h_{J}^{-}, h_{J}^{+} \geq b^{-}, 0 \leq h_{J}^{-} \leq b^{+} .$$
M. Lejmi [56] recognizes $\mathcal{Z}_{J}^{-}$as the kernel of an elliptic operator on $\Omega_{J}^{-}$.

Lemma 2.3. (Lemma 4.1 in [56]) Let $(M, g, J, F)$ be a closed almost Hermitian 4-manifold. Let operator $P: \Omega_{J}^{-} \rightarrow \Omega_{J}^{-}$be defined by
$$P(\psi)=P_{J}^{-}\left(d d^{*} \psi\right),$$
where $P_{J}^{-}: \Omega_{\mathbb{R}}^{2} \rightarrow \Omega_{J}^{-}$is the projection. Then $P$ is a self-adjoint strongly elliptic linear operator with kernel the $g$-self-dual-harmonic, $J$-anti-invariant 2-forms. Hence,
$$\Omega_{J}^{-}=k e r P \oplus P_{J}^{-}\left(d \Omega_{\mathbb{R}}^{1}\right)=H_{J}^{-} \oplus P_{J}^{-}\left(d \Omega_{\mathbb{R}}^{1}\right) .$$

Suppose that $(M, J)$ is a closed complex surface, that is, $J$ is integrable. Theorem 2.13 of [3] shows that the cup product form on $H^{2}(M, \mathbb{R})$, restricted to $H_{\mathbb{R}}^{1,1}(M)$, is nondegenerate of type ( $1, h^{1,1}-1$ ) if $b^{1}$ is even and of type ( $0, h^{1,1}$ ) if $b^{1}$ is odd. For closed almost complex 4-manifolds, by using Proposition 2.1 and Lemma 2.3, we have the following analogous theorem:

Theorem 2.4. (Signature Theorem) Let $(M, J)$ be a closed almost complex 4-manifold. Then the cup-product form on $H^{2}(M ; \mathbb{R})$ restricted to $H_{J}^{+}$is nondegenerate of type ( $b^{+}-$ $h_{J}^{-}, b^{-}$).

Proof. We define an almost Hermitian structure $(g, J, F)$ on $M$. By Proposition 2.1, we have
$$H^{2}(M ; \mathbb{R})=H_{g}^{+} \oplus H_{g}^{-}=H_{J}^{+} \oplus H_{J}^{-} .$$
So we can get
$$H_{J}^{+}=H_{g}^{-} \oplus\left(H_{J}^{+} \cap H_{g}^{+}\right), \quad \operatorname{dim}\left(H_{J}^{+} \cap H_{g}^{+}\right)=b^{+}-h_{J}^{-} .$$

For any $[\gamma] \in H_{g}^{+}, \gamma \in \mathcal{H}_{g}^{+}$,
$$\gamma_{J}^{-}=\frac{1}{2}(\gamma(\cdot, \cdot)-\gamma(J \cdot, J \cdot)) \in \Omega_{J}^{-},$$
by Lemma 2.3 ,
$$\gamma_{J}^{-}=\gamma_{h}+d_{J}^{-}\left(v_{\gamma}+\bar{v}_{\gamma}\right),$$
where
$$\gamma_{h} \in \mathcal{Z}_{J}^{-} \subseteq \mathcal{H}_{g}^{+}, \quad v_{\gamma} \in \Omega_{J}^{0,1} .$$
$\gamma-\gamma_{h}$ is still a self-dual harmonic 2-form.
$$\gamma-\gamma_{h}-d\left(v_{\gamma}+\bar{v}_{\gamma}\right) \in H_{J}^{+} .$$

By the discussion above, we can choose $\left[\omega_{1}\right], \ldots,\left[\omega_{b^{+}-h_{J}^{-}}\right]$, where $\left(\omega_{i}, \omega_{j}\right)_{g}=\delta_{i j}$ for a standard orthonormal basis of $H_{J}^{+} \cap H_{g}^{+}$with respect to the cup product. Let $\widetilde{\omega}_{i} \in \mathcal{Z}_{J}^{+}$ cohomologous to $\omega_{i}$. So
$$\int_{M} \widetilde{\omega}_{i} \wedge \widetilde{\omega}_{j}=\int_{M} \omega_{i} \wedge \omega_{j}=\int_{M} \omega_{i} \wedge *_{g} \omega_{j}=\left(\omega_{i}, \omega_{j}\right)_{g}=\delta_{i j} .$$

Let $\beta_{1}, \ldots, \beta_{b^{-}} \in \mathcal{H}_{g}^{-}$be a standard orthonormal basis of $\mathcal{H}_{g}^{-}$with respect to the integration by $g$, i.e. ,
$$\left(\beta_{i}, \beta_{j}\right)_{g}=\int_{M} \beta_{i} \wedge *_{g} \beta_{j}=\delta_{i j} .$$
So $\left[\beta_{1}\right], \ldots,\left[\beta_{b^{-}}\right]$is standard orthonormal basis of $H_{g}^{-}$with respect to the cup product.
It is easy to see that $\left(\widetilde{\omega}_{i}, \beta_{j}\right)_{g}=0$ pointwise. So $\left\{\widetilde{\omega}_{1}, \ldots, \widetilde{\omega}_{b^{+}-h_{J}^{-}}, \beta_{1}, \ldots, \beta_{b^{-}}\right\}$is a standard orthonormal basis of $\mathcal{Z}_{J}^{+}$with respect to the cup product. The matrix of the cupproduct form on $H^{2}(M ; \mathbb{R})$ restricted to $H_{J}^{+}$under the above basis is
$$\left(\begin{array}{cc}
I_{b^{+}-h_{J}^{-}} & 0 \\
0 & -I_{b^{-}}
\end{array}\right) .$$
This completes the proof of Theorem 2.4. \(\square\)

We define the following operators:
$$\begin{aligned}
& d_{J}^{+}=P_{J}^{+} d: \Omega_{\mathbb{R}}^{1} \longrightarrow \Omega_{\mathbb{R}}^{1,1} \\
& d_{J}^{-}=P_{J}^{-} d: \Omega_{\mathbb{R}}^{1} \longrightarrow\left(\Omega_{J}^{2,0}+\Omega_{J}^{0,2}\right)_{\mathbb{R}},
\end{aligned}$$
where $P_{J}^{ \pm}: \Omega_{\mathbb{R}}^{2} \longrightarrow \Omega_{J}^{ \pm}$.
Suppose that $(M, g, J, F)$ is a closed almost Hermitian 4-manifold, and that the given almost complex structure $J$ is also tamed by a symplectic form $\omega$. By Lemma 2.3, $\omega$ can be decomposed as follows:
$$\omega=F+d_{J}^{-}(v+\bar{v})+\alpha_{\omega},$$
where $\alpha_{\omega} \in \mathcal{Z}_{J}^{-} \subset \mathcal{H}_{g}^{+}, v \in \Omega_{J}^{0,1}, F^{2}>0$. Set $\omega_{1}=\omega-\alpha_{\omega}$. It is clear that $J$ is also an $\omega_{1}$-tame almost complex structure. Set
$$\widetilde{\omega}_{1}=\omega_{1}-d(v+\bar{v})=F-d_{J}^{+}(v+\bar{v}) \in \mathcal{Z}_{J}^{+} .$$

Thus $\left[\widetilde{\omega}_{1}\right] \in H_{g}^{+} \cap H_{J}^{+}$. It is easy to see that $0 \leq h_{J}^{-} \leq b^{+}-1$ (cf. [73]). We may assume without loss of generality that
$$\int_{M} F^{2}=2$$
and
$$\int_{M}\left|d_{J}^{-}(v+\bar{v})\right|^{2} d \mu_{g}=2 a>0$$
for if $a=0$, then $F$ is a symplectic form compatible with $J$.
Let $(g, J, F)$ be an almost Hermitian structure on a closed 4-manifold $M, \omega_{1}=F+$ $d_{J}^{-}(v+\bar{v})$ a symplectic form on $M$ by which $J$ is tamed, where $v \in \Omega_{J}^{0,1}$. Suppose $\psi \in \Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)$ is $d$-exact with
$$\psi=d(u+\bar{u})=d_{J}^{+}(u+\bar{u}), \quad \text { i.e., } \quad d_{J}^{-}(u+\bar{u})=0,$$
for some $u \in \Lambda_{J}^{0,1} \otimes L_{1}^{2}(M)$. Let
$$f_{\psi}=\frac{1}{2} \psi \wedge F / d \mu_{g}-\frac{1}{2} \int_{M} \psi \wedge F,$$
then
$$\int_{M} f_{\psi} d \mu_{g}=0$$
Define
$$L_{2}^{2}(M)_{0}:=\left\{f \in L_{2}^{2}(M) \mid \int_{M} f d \mu_{g}=0\right\}$$
It is easy to see that $f_{\psi} \in L_{2}^{2}(M)_{0}$. Recall that if $J$ is integrable, in classical complex analysis, it follows that $d J d f_{\psi}=2 \sqrt{-1} \partial_{J} \bar{\partial}_{J} f_{\psi}$. For general case (i.e., $J$ is not integrable), by Lemma 2.3, there exists $\eta_{\psi}^{1} \in \Lambda_{J}^{0,2} \otimes L_{2}^{2}(M)$ such that
$$d_{J}^{-} J d f_{\psi}+d_{J}^{-} d^{*}\left(\eta_{\psi}^{1}+\bar{\eta}_{\psi}^{1}\right)=0 .$$
Then, by Lemma 2.3 and the Hodge decomposition $\Omega_{g}^{+}=\mathcal{H}_{g}^{+} \oplus d_{g}^{+}\left(\Omega^{1}\right)$ (cf. [16,17]), since
$$d_{g}^{+} d^{*}: \Omega_{g}^{+} \longrightarrow \Omega_{g}^{+}$$
is a strongly self-adjoint elliptic operator, there are $\eta_{\psi}^{2} \in \Lambda_{J}^{0,2} \otimes L_{2}^{2}(M) 4$ satisfying
$$d_{g}^{+}(u+\bar{u})=d_{g}^{+} d^{*}\left[f_{\psi} \omega_{1}+\left(\eta_{\psi}^{1}+\eta_{\psi}^{2}+\bar{\eta}_{\psi}^{1}+\bar{\eta}_{\psi}^{2}\right)\right],$$
where
$$f_{\psi} \omega_{1}+\left(\eta_{\psi}^{1}+\eta_{\psi}^{2}\right)+\left(\bar{\eta}_{\psi}^{1}+\bar{\eta}_{\psi}^{2}\right) \in \Omega_{g}^{+} .$$
Note that
$$\begin{aligned}
d^{*}\left(f_{\psi} \omega_{1}\right) & =-*_{g} d\left(f_{\psi} \omega_{1}\right) \\
& =-*_{g}\left(d f_{\psi} \wedge \omega_{1}\right) \\
& =-*_{g}\left(d f_{\psi} \wedge F\right) \\
& =J d f_{\psi}-*_{g}\left(d f_{\psi} \wedge d_{J}^{-}(v+\bar{v})\right) .
\end{aligned}$$

By (2.18) and (2.26), we have
$$\begin{aligned}
\psi & =d(u+\bar{u}) \\
& =d d^{*}\left[f_{\psi} \omega_{1}+\left(\eta_{\psi}^{1}+\eta_{\psi}^{2}+\bar{\eta}_{\psi}^{1}+\bar{\eta}_{\psi}^{2}\right)\right] \\
& =d J d f_{\psi}+d d^{*}\left(\eta_{\psi}^{1}+\bar{\eta}_{\psi}^{1}\right)-d *_{g}\left(d f_{\psi} \wedge d_{J}^{-}(v+\bar{v})\right)+d d^{*}\left(\eta_{\psi}^{2}+\bar{\eta}_{\psi}^{2}\right),
\end{aligned}$$
where, by Lemma 2.3,
$$-d_{J}^{-} *_{g} d f_{\psi} \wedge d_{J}^{-}(v+\bar{v})+d_{J}^{-} d^{*}\left(\eta_{\psi}^{2}+\bar{\eta}_{\psi}^{2}\right)=0 .$$
Thus, by the above discussion, we can define two operators
$$\mathcal{D}_{J}^{+} \text {and } \widetilde{\mathcal{D}}_{J}^{+}: L_{2}^{2}(M)_{0} \longrightarrow \Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M) .$$

Definition 2.5. Set $\mathcal{W}: L_{2}^{2}(M)_{0} \longrightarrow \Lambda_{\mathbb{R}}^{1} \otimes L_{1}^{2}(M)$,
$$\mathcal{W}(f)=J d f+d^{*}\left(\eta_{f}^{1}+\bar{\eta}_{f}^{1}\right), \quad \eta_{f}^{1} \in \Lambda_{J}^{0,2} \otimes L_{2}^{2}(M),$$
satisfying
$$d_{J}^{-} \mathcal{W}(f)=0 .$$

Define $\mathcal{D}_{J}^{+}: L_{2}^{2}(M)_{0} \longrightarrow \Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M), \quad \mathcal{D}_{J}^{+}(f)=d \mathcal{W}(f)$.
Set $\widetilde{\mathcal{W}}: L_{2}^{2}(M)_{0} \longrightarrow \Lambda_{\mathbb{R}}^{1} \otimes L_{1}^{2}(M)$,
$$\widetilde{\mathcal{W}}(f)=\mathcal{W}(f)-*_{g}\left(d f \wedge d_{J}^{-}(v+\bar{v})\right)+d^{*}\left(\eta_{f}^{2}+\bar{\eta}_{f}^{2}\right), \quad \eta_{f}^{2} \in \Lambda_{J}^{0,2} \otimes L_{2}^{2}(M),$$
satisfying
$$d^{*} \widetilde{\mathcal{W}}(f)=0, \quad d_{J}^{-} \widetilde{\mathcal{W}}(f)=0 .$$

Define $\widetilde{\mathcal{D}}_{J}^{+}: L_{2}^{2}(M)_{0} \longrightarrow \Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M), \quad \widetilde{\mathcal{D}}_{J}^{+}(f)=d \widetilde{\mathcal{W}}(f)$.
Remark 2.6. Notice that $d_{J}^{-} \widetilde{\mathcal{W}}=0=d_{J}^{-} \mathcal{W}$, by the above formula, it implies that
$$d_{J}^{-}\left(*_{g}\left(d f \wedge d_{J}^{-}(v+\bar{v})\right)+d^{*}\left(\eta_{f}^{2}+\bar{\eta}_{f}^{2}\right)\right)=0$$
If $d F=0$, then $\mathcal{D}_{J}^{+}=\widetilde{\mathcal{D}}_{J}^{+}$since $d_{J}^{-}(v+\bar{v})=0$. If $J$ is integrable, $\bar{\partial}_{J}^{2}=\partial_{J}^{2}=0$ and $\partial_{J} \bar{\partial}_{J}+\bar{\partial}_{J} \partial_{J}=0$, then $d J d f=2 \sqrt{-1} \partial_{J} \bar{\partial}_{J} f=\mathcal{D}_{J}^{+}(f)$, that is, $\eta_{f}^{1}=0$. (cf. [77,79]). For the higher dimensional closed almost Kähler manifold $(M, g, J, \omega)$, could one define the similar operator $\mathcal{D}_{J}^{+}$with the strongly self-adjoint elliptic operator?

Denote by $\mathbb{G}$ the Green operator associated to $\Delta_{g}$ (cf. [49]). The Hodge operator $*_{g}$ commutes with $\Delta_{g}$. It follows that $*_{g}$ commutes with $\mathbb{G}$. It is clear that $d$ and $d^{*}$ commute with $\mathbb{G}$. Lejmi [56] proved a generalized $\partial \bar{\partial}$-lemma for almost Kähler 4-manifolds under the condition $h_{J}^{-}=b^{+}-1$, and in the following, we generalize this result to almost Hermitian manifolds $(M, g, J, F)$ with $J$ tamed by $\omega_{1}$, where $\omega_{1}$ is the form defined earlier.

Proposition 2.7. (cf. Proposition 2.5 in [57]) If $h_{J}^{-}=b^{+}-1$, then $\widetilde{\mathcal{D}}_{J}^{+}(f)$ can be rewritten as
$$\widetilde{\mathcal{D}}_{J}^{+}(f)=2 d \mathbb{G} d^{*}\left(f^{\prime} F\right)=2 \mathbb{G} d d^{*}\left(f^{\prime} F\right)=2 d d^{*} \mathbb{G}\left(f^{\prime} F\right),$$
and $\widetilde{\mathcal{W}}(f)$ can be rewritten as
$$\widetilde{\mathcal{W}}(f)=2 \mathbb{G} d^{*}\left(f^{\prime} F\right)=2 d^{*} \mathbb{G}\left(f^{\prime} F\right),$$
where $f^{\prime} \in L^{2}(M)_{0}, f \in L_{2}^{2}(M)_{0}$.
Proof. First of all, we prove that for any $f^{\prime} \in L^{2}(M)_{0}, d \mathbb{G} d^{*}\left(f^{\prime} F\right)$ is $J$-invariant if $h_{J}^{-}=$ $b^{+}-1$. Without loss of generality, we choose $f^{\prime} \in C^{\infty}(M)_{0}$.
$$\begin{aligned}
\left(d G d^{*}\left(f^{\prime} F\right)\right)_{J}^{-} & =P_{g}^{+}\left(d \mathbb{G} d^{*}\left(f^{\prime} F\right)\right)-\frac{1}{2}\left(P_{g}^{+}\left(d \mathbb{G} d^{*}\left(f^{\prime} F\right)\right), F\right)_{g} F \\
& =\frac{1}{2}\left(1+*_{g}\right)\left(-\mathbb{G} d *_{g} d *_{g}\left(f^{\prime} F\right)\right)-\frac{1}{4}\left(1+*_{g}\right)\left(-\mathbb{G} d *_{g} d *_{g}\left(f^{\prime} F\right), F\right)_{g} F \\
& =\frac{1}{2} \mathbb{G} \Delta_{g}\left(f^{\prime} F\right)-\frac{1}{4}\left(\mathbb{G} \Delta_{g}\left(f^{\prime} F\right), F\right)_{g} F \\
& =\frac{1}{2}\left(f^{\prime} F\right)-\frac{1}{2}\left(f^{\prime} F\right)_{H}-\frac{1}{4}\left(f^{\prime} F-\left(f^{\prime} F\right)_{H}, F\right)_{g} F \\
& =\frac{1}{2}\left(f^{\prime} F\right)-\frac{1}{2}\left(f^{\prime} F\right)_{H}-\frac{1}{2}\left(f^{\prime} F\right)+\frac{1}{4}\left(\left(f^{\prime} F\right)_{H}, F\right)_{g} F \\
& =-\frac{1}{2}\left(f^{\prime} F\right)_{H}+\frac{1}{4}\left(\left(f^{\prime} F\right)_{H}, F\right)_{g} F,
\end{aligned}$$
where $\left(f^{\prime} F\right)_{H}$ denotes the harmonic part with respect to $\Delta_{g}$. Under the assumption $h_{J}^{-}=b^{+}-1$, it follows that $\left(f^{\prime} F\right)_{H}=0$ for any smooth function $f^{\prime}$ with zero integral for the following reason. In this case,
$$\mathcal{H}_{g}^{2}=\mathbb{R} \cdot \omega_{1} \oplus \mathcal{H}_{J}^{-} \oplus \mathcal{H}_{g}^{-} .$$
Since
$$\int_{M} f^{\prime} F \wedge \omega_{1}=\int_{M} f^{\prime} F \wedge F=2 \int_{M} f^{\prime} d \mu_{g}=0$$
$f^{\prime} F \wedge \alpha \equiv 0$ for any $\alpha \in \mathcal{H}_{J}^{-}$and $f^{\prime} F \wedge \beta \equiv 0$ for any $\beta \in \mathcal{H}_{g}^{-}$, by Hodge decomposition (cf. [17]), we can get $\left(f^{\prime} F\right)_{H}=0$. By the above calculation, it is easy to see that
$$P_{g}^{+}\left(2 d \mathbb{G} d^{*}\left(f^{\prime} F\right)\right)=P_{g}^{+}\left(2 d d^{*} \mathbb{G}\left(f^{\prime} F\right)\right)=\mathbb{G} \Delta_{g}\left(f^{\prime} F\right)=f^{\prime} F .$$

Second, let $\psi$ be a smooth $J$-invariant 2-form which is $d$-exact, i.e., $\psi=d(u+\bar{u})$ and $d_{J}^{-}(u+\bar{u})=0$, where $u \in \Omega_{J}^{0,1}$. Then $P_{g}^{+}(\psi)=f_{\psi}^{\prime} F, f_{\psi}^{\prime} \in C^{\infty}(M)_{0}$, since $\omega_{1}=$ $F+d_{J}^{-}(v+\bar{v}), v \in \Omega_{J}^{0,1}$ and
$$2 \int_{M} f_{\psi}^{\prime} d \mu_{g}=\int_{M} \psi \wedge F=\int_{M} \psi \wedge \omega_{1}=\int_{M} d(u+\bar{u}) \wedge \omega_{1}=0$$
Therefore, by (2.28),
$$P_{g}^{+}(\psi)=f_{\psi}^{\prime} F=P_{g}^{+}\left(d 2 \mathbb{G} d^{*}\left(f_{\psi}^{\prime} F\right)\right) .$$

Hence
$$\psi=d(u+\bar{u})=d 2 \mathbb{G} d^{*}\left(f_{\psi}^{\prime} F\right),$$
since $P_{g}^{+}\left(\psi-d 2 \mathbb{G} d^{*}\left(f_{\psi}^{\prime} F\right)\right)=0$ and $\psi-d 2 \mathbb{G} d^{*}\left(f_{\psi}^{\prime} F\right)$ is $d$-exact (cf. (2.18) or [17]). According to the construction of $\widetilde{\mathcal{D}}_{J}^{+}$, there exists a function $f_{\psi} \in L_{2}^{2}(M)_{0}$ such that $\psi=\widetilde{\mathcal{D}}_{J}^{+}\left(f_{\psi}\right)=2 d d^{*} \mathbb{G}\left(f_{\psi}^{\prime} F\right)$. \(\square\)

Remark 2.8. (1) If $(M, g, J, \omega)$ is a Kähler surface, then $h_{J}^{-}=b^{+}-1$ and
$$\mathcal{D}_{J}^{+}(f)=\widetilde{\mathcal{D}}_{J}^{+}(f)=2 d \mathbb{G} d^{*}\left(f^{\prime} \omega\right)=2 d \mathbb{G} J\left(d f^{\prime}\right)=2 d \mathbb{G} d^{c} f^{\prime}=2 d d^{c} \mathbb{G} f^{\prime}=2 \sqrt{-1} \partial_{J} \bar{\partial}_{J} f,$$
where $f=\mathbb{G} f^{\prime}$. Hence, the above proposition can be viewed as a generalized $\partial \bar{\partial}$-lemma and
$$\begin{aligned}
& \qquad P_{g}^{+}\left(2 d \mathbb{G} d^{*}\left(f_{\psi}^{\prime} F\right)\right)=P_{g}^{+}\left(2 d d^{*} \mathbb{G}\left(f_{\psi}^{\prime} F\right)\right)=P_{g}^{+}\left(2 \mathbb{G} d d^{*}\left(f_{\psi}^{\prime} F\right)\right)=f_{\psi}^{\prime} F . \\
& \text { (2) } \mathbb{G}\left(f_{\psi}^{\prime} F\right) \in \Lambda_{\mathbb{R}}^{2} \otimes L_{2}^{2}(M), \text { where } f_{\psi}^{\prime} \in L^{2}(M)_{0} .
\end{aligned}$$

Suppose that $(M, g, J, F)$ is tamed by $\omega_{1}=F+d_{J}^{-}(v+\bar{v})$, where $v \in \Omega_{J}^{0,1}$, suppose that $\left[\alpha_{1}\right], \cdots,\left[\alpha_{h_{J}^{-}}\right]$is a basis of $H_{J}^{-}$, and $\left[\omega_{1}\right], \cdots,\left[\omega_{b^{+}-h_{J}^{-}}\right]$is a basis of $H_{g}^{+} \cap H_{J}^{+}$, where $0 \leq h_{J}^{-} \leq b^{+}-1$. Let $\psi \in \Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)$ be a real d-exact (1,1)-form, that is, there exists $u_{\psi} \in \Omega_{J}^{0,1}$ such that $\psi=d\left(u_{\psi}+\bar{u}_{\psi}\right)$, hence $d_{J}^{-}\left(u_{\psi}+\bar{u}_{\psi}\right)=0$. It is clear that
$$\psi \wedge \alpha_{j}=0, \quad 1 \leq j \leq h_{J}^{-} .$$
Hence,
$$\begin{gathered}
\int_{M} \psi \wedge \alpha_{j}=0, \quad 1 \leq j \leq h_{J}^{-} \\
\int_{M} \psi \wedge \omega_{i}=0, \quad 1 \leq i \leq b^{+}-h_{J}^{-} .
\end{gathered}$$
Thus $\psi$ is orthogonal to the self-dual harmonic 2-forms, $\mathcal{H}_{g}^{+}$, with respect to the cup product. By Hodge decomposition (cf. [17]), there exist
$$f_{\psi} \in L_{2}^{2}(M)_{0}, \quad \eta_{\psi}^{1}, \quad \eta_{\psi}^{2} \in \Lambda_{J}^{-} \otimes L_{2}^{2}(M)$$
such that
$$P_{g}^{+} \psi=d_{g}^{+}\left(u_{\psi}+\bar{u}_{\psi}\right)=d_{g}^{+} d^{*}\left(f_{\psi} \omega_{1}+\left(\eta_{\psi}^{1}+\bar{\eta}_{\psi}^{1}\right)+\left(\eta_{\psi}^{2}+\bar{\eta}_{\psi}^{2}\right)\right)$$
satisfying
$$d_{J}^{-} d^{*}\left(f_{\psi} \omega_{1}+\left(\eta_{\psi}^{1}+\bar{\eta}_{\psi}^{1}\right)+\left(\eta_{\psi}^{2}+\bar{\eta}_{\psi}^{2}\right)\right)=0,$$
and it follows that
$$\psi=d d^{*}\left(f_{\psi} \omega_{1}+\left(\eta_{\psi}^{1}+\bar{\eta}_{\psi}^{1}\right)+\left(\eta_{\psi}^{2}+\bar{\eta}_{\psi}^{2}\right)\right) .$$

By Definition 2.5 and Proposition 2.7, we have the following lemma,
Lemma 2.9. Let $(M, J)$ be a tamed closed almost complex 4-manifold with $h_{J}^{-}=b^{+}-1$. Suppose that $\psi \in \Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)$ is $d$-exact. Then there exists $f_{\psi} \in L_{2}^{2}(M)_{0}$ and $f_{\psi}^{\prime} \in$ $L^{2}(M)_{0}$ such that
$$\psi=\widetilde{\mathcal{D}}_{J}^{+}\left(f_{\psi}\right)=d \widetilde{\mathcal{W}}\left(f_{\psi}\right)=2 d d^{*} \mathbb{G}\left(f_{\psi}^{\prime} F\right) .$$

\section*{3 The intersection pairing on weakly $\widetilde{\mathcal{D}}_{J}^{+}$-closed (1,1)-forms}

In this section, we shall investigate the intersection paring on weakly $\widetilde{\mathcal{D}}_{J}^{+}$-closed (1,1)-forms defined below as done in Buchdahl's paper [7]. First, we consider the following technical lemma (compare Lemma 1 in [7] or § 3.2 in [31]):

Lemma 3.1. Suppose that $(M, g, J, F)$ is a closed almost Hermitian 4-manifold. Then
$$d_{J}^{+}: \Lambda_{\mathbb{R}}^{1} \otimes L_{1}^{2}(M) \longrightarrow \Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)$$
has closed range.
Proof. Let $\left\{w_{i}\right\}$ be a sequence of real 1-forms on $M$ with coefficients in $L_{1}^{2}$ such that $\psi_{i}=d_{J}^{+} w_{i}$ is converging in $L^{2}$ to some $\psi \in \Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)$. Write $w_{i}=u_{i}+\bar{u}_{i}$ for some $(0,1)$-form $u_{i}$, so $\psi_{i}=d_{J}^{+}\left(u_{i}+\bar{u}_{i}\right)=\partial_{J} u_{i}+\bar{\partial}_{J} \bar{u}_{i}$.

By smoothing and diagonalising, it can be assumed without loss of generality that $u_{i}$ is smooth for each $i$. Note that
$$\begin{aligned}
F \wedge \psi_{i} & =\left(\wedge \psi_{i}\right) F^{2} / 2, \\
*_{g} \psi_{i} & =\left(\wedge \psi_{i}\right) F-\psi_{i}, \\
\left|\psi_{i}\right|^{2} d \mu_{g} & =\left(\wedge \psi_{i}\right)^{2} F^{2} / 2-\psi_{i}^{2},
\end{aligned}$$
where $\wedge: \Omega_{\mathbb{R}}^{1,1} \longrightarrow \Omega_{\mathbb{R}}^{0}$ is an algebraic operator in Lefschetz decomposition (cf. [31]). Using Stokes' Theorem,
$$\begin{gathered}
\int_{M}\left|\psi_{i}\right|^{2} d \mu_{g}=\int_{M}\left(\wedge \psi_{i}\right)^{2} d \mu_{g}+2 \int_{M}\left(\bar{\partial}_{J} u_{i}+A_{J} \bar{u}_{i}\right)^{2} \\
\int_{M} d w_{i} \wedge *_{g} d w_{i}=\int_{M} \psi_{i} \wedge *_{g} \psi_{i}+2 \int_{M}\left(\bar{\partial}_{J} u_{i}+A_{J} \bar{u}_{i}\right)^{2}
\end{gathered}$$
So it follows that $d w_{i}=d_{J}^{+} w_{i}+d_{J}^{-} w_{i}$ is bounded in $L^{2}$. Let $\widetilde{w}_{i}$ be the $L^{2}$-projection of $w_{i}$ perpendicular to the kernel of $d$, so $d^{*} \widetilde{w}_{i}=0$ and $\widetilde{w}_{i}$ is perpendicular to the harmonic 1-forms. Hence $d \widetilde{w}_{i}=d w_{i}$ and there exists a constant $C$ such that
$$\left\|\widetilde{w}_{i}\right\|_{L_{1}^{2}(M)}^{2} \leq C\left(\left\|d \widetilde{w}_{i}\right\|_{L^{2}(M)}^{2}+\left\|d^{*} \widetilde{w}_{i}\right\|_{L^{2}(M)}^{2}\right)=C\left\|d w_{i}\right\|_{L^{2}(M)}^{2}<\text { Const., }$$
so a subsequence of the sequence $\left\{\widetilde{w}_{i}\right\}$ converges weakly in $L_{1}^{2}$ to some $\widetilde{w} \in \Lambda_{\mathbb{R}}^{1} \otimes L_{1}^{2}(M)$. Since $d_{J}^{+} \widetilde{w}_{i}=d_{J}^{+} w_{i}=\psi_{i}$, it follows $d_{J}^{+} \widetilde{w}=\psi$, proving the claim. \(\square\)

We now consider the closed tamed almost Hermitian 4-manifold $(M, g, J, F)$. We may assume without loss of generality that $\omega_{1}=F+d_{J}^{-}(v+\bar{v}), v \in \Omega_{J}^{0,1}, F$ is the fundamental form with
$$\int_{M} F^{2}=2, g(\cdot, \cdot)=F(\cdot, J \cdot), \quad \int_{M} \omega_{1}^{2}=2(1+a), \quad 2 a=\int_{M}\left|d_{J}^{-}(v+\bar{v})\right|^{2} d \mu_{g}>0,$$
where $d \mu_{g}$ is the volume form defined by $g$; if $a=0$, then $F$ is a $J$-compatible symplectic form. It is clear that $0 \leq h_{J}^{-} \leq b^{+}-1$ (cf. [73]). Denote by
$$\widetilde{\omega}_{1}:=\omega_{1}-d(v+\bar{v})=F-d_{J}^{+}(v+\bar{v}),$$
then $\widetilde{\omega}_{1} \in \mathcal{Z}_{J}^{+}$being cohomologous to $\omega_{1}$,
$$\begin{aligned}
\int_{M} \widetilde{\omega}_{1}^{2} & =\int_{M} \omega_{1}^{2}=2(1+a) \\
-\int_{M}\left(d_{J}^{+}(v+\bar{v})\right)^{2} & =\int_{M}\left|d_{J}^{-}(v+\bar{v})\right|^{2} d \mu_{g}=2 a>0
\end{aligned}$$
and
$$\int_{M} d_{J}^{+}(v+\bar{v}) \wedge F=-2 a$$
Choose $\alpha_{j} \in \mathcal{Z}_{J}^{-} \subset \mathcal{Z}_{g}^{+}=\mathcal{H}_{g}^{+}$such that
$$\int_{M} \alpha_{i} \wedge \alpha_{j}=\delta_{i j}, \quad 1 \leq j \leq h_{J}^{-} .$$
We can find $\omega_{2}, \cdots, \omega_{b^{+}-h_{J}^{-}} \in \mathcal{Z}_{g}^{+} \backslash \mathcal{Z}_{J}^{-}$, such that
$$\begin{gathered}
\int_{M} \omega_{j} \wedge \omega_{k}=\delta_{j k}, \quad 2 \leq j, k \leq b^{+}-h_{J}^{-} \\
\int_{M} \omega_{1} \wedge \omega_{j}=0, \quad 2 \leq j \leq b^{+}-h_{J}^{-}
\end{gathered}$$
Hence $\mathcal{H}_{g}^{+}=\operatorname{Span}\left\{\omega_{1}, \cdots, \omega_{b^{+}-h_{J}^{-}}, \alpha_{1}, \cdots, \alpha_{h_{J}^{-}}\right\}$. Let $\widetilde{\omega}_{i} \in \mathcal{Z}_{J}^{+}$be cohomologous to $\omega_{i}$, $1 \leq i \leq b^{+}-h_{J}^{-}$, so
$$\int_{M} \widetilde{\omega}_{1} \wedge F=2(1+a)$$
and
$$\int_{M} \widetilde{\omega}_{j} \wedge F=0, \quad 2 \leq j \leq b^{+}-h_{J}^{-} .$$

In Section 2, we define $\mathcal{D}_{J}^{+}$and $\widetilde{\mathcal{D}}_{J}^{+}: L_{2}^{2}(M)_{0} \longrightarrow \Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)$. Analogous to Lemma 3.1, we have:

Lemma 3.2. $\widetilde{\mathcal{D}}_{J}^{+}: L_{2}^{2}(M)_{0} \longrightarrow \Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)$ has closed range. If $J$ is integrable, then
$$\mathcal{D}_{J}^{+}=d J d f=2 \sqrt{-1} \partial_{J} \bar{\partial}_{J} f,$$
hence $\mathcal{D}_{J}^{+}$has closed range too.
Proof. Let $\left\{f_{i}\right\}$ be a sequence of real functions on $M$ in $L_{2}^{2}(M)_{0}$. By Definition 2.5, $\left\{\widetilde{\mathcal{W}}\left(f_{i}\right)\right\}$ is a sequence of real 1-forms on $M$ with coefficients in $L_{1}^{2}$ such that
$$\psi_{i}=d \widetilde{\mathcal{W}}\left(f_{i}\right)=\widetilde{\mathcal{D}}_{J}^{+}\left(f_{i}\right) \in \Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)$$
is converging in $L^{2}$ to some $\psi \in \Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)$. It is clear that $d^{*} \widetilde{\mathcal{W}}\left(f_{i}\right)=0$. By the proof of Lemma 3.1, $\left\{\widetilde{\mathcal{W}}\left(f_{i}\right)\right\}$ is bounded in $L_{1}^{2}$, so a subsequence of $\left\{\widetilde{\mathcal{W}}\left(f_{i}\right)\right\}$ converges weakly in $L_{1}^{2}$ to some $\widetilde{\mathcal{W}} \in \Lambda_{\mathbb{R}}^{1} \otimes L_{1}^{2}(M)$. Since $d \widetilde{\mathcal{W}}\left(f_{i}\right) \in \Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)$, it follows that
$$d \widetilde{\mathcal{W}}=\psi \in \Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M) .$$

To complete the proof of Lemma 3.2, we need the following claim:
Claim (cf. Lemma 2.9): Suppose that $\psi \in \Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)$ is $d$-exact, that is, there is $u_{\psi} \in \Lambda_{J}^{0,1} \otimes L_{1}^{2}(M)$ such that $\psi=d\left(u_{\psi}+\bar{u}_{\psi}\right)$. Then $\psi$ is $\widetilde{\mathcal{D}}_{J}^{+}$-exact, that is, there exists $f_{\psi} \in L_{2}^{2}(M)_{0}$ such that $\psi=\widetilde{\mathcal{D}}_{J}^{+}\left(f_{\psi}\right)$.

Indeed, let $A \in \Omega_{\mathbb{R}}^{1}(M), d A=d_{J}^{+} A+d_{J}^{-} A$. By (3.1)-(3.3), we have
$$\begin{aligned}
\int_{M}\left|d_{J}^{+} A\right|^{2} d \mu_{g} & =\int_{M}\left(\wedge d_{J}^{+} A\right)^{2} d \mu_{g}+\int_{M}\left|d_{J}^{-} A\right|^{2} d \mu_{g} \\
\int_{M}|d A|^{2} d \mu_{g} & =\int_{M}\left|d_{J}^{+} A\right|^{2} d \mu_{g}+\int_{M}\left|d_{J}^{-} A\right|^{2} d \mu_{g}
\end{aligned}$$
Let $\tilde{A}$ be the $L^{2}$-projection of $A$ perpendicular to the kernel of $d$, by Hodge decomposition, $d^{*} \tilde{A}=0$ and $\tilde{A}$ are perpendicular to the harmonic 1-forms. Hence $d \tilde{A}=d A$ and there exists a constant $C$ such that
$$\|\tilde{A}\|_{L^{2}}^{2} \leq\|\tilde{A}\|_{L_{1}^{2}}^{2} \leq C\left(\|d \tilde{A}\|_{L^{2}}^{2}+\left\|d^{*} \tilde{A}\right\|_{L^{2}}^{2}\right) \leq \text { Const. }(d A) .$$
Recall the definition of $\widetilde{\mathcal{W}}$ (cf. Definition 2.5): $f \in L_{2}^{2}(M)_{0}, \eta_{f}^{1}, \eta_{f}^{2} \in \Lambda_{J}^{0,2} \otimes L_{2}^{2}(M)$ such that
$$\widetilde{\mathcal{W}}(f)=d^{*}\left(f \omega_{1}+\left(\eta_{f}^{1}+\bar{\eta}_{f}^{1}\right)+\left(\eta_{f}^{2}+\bar{\eta}_{f}^{2}\right)\right)$$
satisfying $d_{J}^{-} \widetilde{\mathcal{W}}(f)=0, d^{*} \widetilde{\mathcal{W}}(f)=0$ and $d \widetilde{\mathcal{W}}(f)=d_{J}^{+} \widetilde{\mathcal{W}}(f) \in \Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)$. As done in Appendix A.3, without loss of generality, we may assume that if $A \in \Omega_{\mathbb{R}}^{1}(M), d^{*} A=0$ and $d_{J}^{-} A=0$, then
$$\begin{aligned}
\widetilde{\mathcal{W}}(f), A) & =-\int_{M} A \wedge d\left[f \omega_{1}+\left(\eta_{f}^{1}+\bar{\eta}_{f}^{1}\right)+\left(\eta_{f}^{2}+\bar{\eta}_{f}^{2}\right)\right] \\
& =-\int_{M} d(A) \wedge\left[f \omega_{1}+\left(\eta_{f}^{1}+\bar{\eta}_{f}^{1}\right)+\left(\eta_{f}^{2}+\bar{\eta}_{f}^{2}\right)\right] \\
& =-\int_{M} d_{J}^{+}(A) \wedge f F \\
& =\left(f, \widetilde{\mathcal{W}}^{*} A\right) .
\end{aligned}$$
Thus, the formal $L^{2}$-adjoint operator of $\widetilde{\mathcal{W}}$ is
$$\widetilde{\mathcal{W}^{*}} A=\frac{-2 F \wedge d_{J}^{+} A}{F^{2}}=-\left(\wedge d_{J}^{+} A\right) .$$
By (3.11), (3.12), we have: If $A \in \Lambda_{\mathbb{R}}^{1} \otimes L_{1}^{2}(M), d^{*} A=0$, then
$$\|A\|_{L^{2}}^{2} \leq C\left(\left\|\widetilde{\mathcal{W}}^{*} A\right\|_{L^{2}}^{2}+2\left\|d_{J}^{-} A\right\|_{L^{2}}^{2}\right) \leq \operatorname{Const} .\left(\wedge d_{J}^{+} A, d_{J}^{-} A\right) .$$
Now suppose that $\psi \in \Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)$ is $d$-exact, then there exists $u_{\psi} \in \Lambda_{J}^{0,1} \otimes L_{1}^{2}(M)$ such that $\psi=d\left(u_{\psi}+\bar{u}_{\psi}\right), d_{J}^{-}\left(u_{\psi}+\bar{u}_{\psi}\right)=0$. By Hodge decomposition, there exists $\tilde{u}_{\psi} \in \Lambda_{J}^{0,1} \otimes L_{1}^{2}(M)$ satisfying that
$$\psi=d\left(\tilde{u}_{\psi}+\overline{\tilde{u}}_{\psi}\right), \quad d_{J}^{-}\left(\tilde{u}_{\psi}+\overline{\tilde{u}}_{\psi}\right)=0, \quad d^{*}\left(\tilde{u}_{\psi}+\overline{\tilde{u}}_{\psi}\right)=0 .$$

By (3.13),
$$\left\|\tilde{u}_{\psi}+\overline{\tilde{u}}_{\psi}\right\|_{L^{2}} \leq C\|\wedge \psi\|_{L^{2}}=C\left\|P_{g}^{+} \psi\right\|_{L^{2}} .$$
Since $d_{g}^{+} \oplus d^{*}: \Lambda_{\mathbb{R}}^{1} \rightarrow \Lambda_{\mathbb{R}}^{1,1} \oplus \Lambda_{\mathbb{R}}^{0}$ is an elliptic system, we can solve $\widetilde{\mathcal{W}}, d_{J}^{-}$-problem (that is similar to $\bar{\partial}$-problem in classical complex analysis [40]) for closed almost Hermitian 4-manifold $(M, g, J, F)$ tamed by the symplectic form $\omega_{1}$ (more details see Appendix A.3), that is, there exists $f_{\psi} \in L_{2}^{2}(M)_{0}$ such that $\widetilde{\mathcal{W}}\left(f_{\psi}\right)=\tilde{u}_{\psi}+\overline{\tilde{u}}_{\psi}, P_{g}^{+} d \widetilde{\mathcal{W}}\left(f_{\psi}\right)=P_{g}^{+} \psi$. Since $\psi \in \Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)$ is $d$-exact, it follows that $d \widetilde{\mathcal{W}}\left(f_{\psi}\right)=\psi$. This completes the proof of the above Claim.

We now return to the proof of Lemma 3.2. By the above claim which is similar to Lemma 2.9, there exists $f \in L_{2}^{2}(M)_{0}$ such that $\widetilde{\mathcal{D}}_{J}^{+}(f)=d \widetilde{\mathcal{W}}(f)=\psi$.

If $J$ is integrable, after a simple calculation, we can get
$$\mathcal{D}_{J}^{+}(f)=d J d f=2 \sqrt{-1} \partial_{J} \bar{\partial}_{J} f$$
and
$$2 \sqrt{-1} \partial_{J} \bar{\partial}_{J} f \wedge F=\Delta_{g} f \cdot \frac{F^{2}}{2} .$$
So by Poincaré's Inequality and Interpolation Inequality, we can immediately get that $\mathcal{D}_{J}^{+}$ has closed range. \(\square\)

Definition 3.3. $\psi \in \Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)$ is said to be weakly $\widetilde{\mathcal{D}}_{J}^{+}$-closed if and only if for any $f \in L_{2}^{2}(M)_{0}$,
$$\int_{M} \psi \wedge \widetilde{\mathcal{D}}_{J}^{+}(f)=0 .$$

Let $\left(\Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)\right)_{w}$ denote the space of weakly $\widetilde{\mathcal{D}}_{J}^{+}$-closed (1,1)-forms. It is easy to get the following lemma since
$$\widetilde{\mathcal{D}}_{J}^{+}(f)=d \widetilde{\mathcal{W}}(f) \in \Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M) .$$

Lemma 3.4. $F, d_{J}^{+}(u+\bar{u})$ where $u \in \Lambda_{J}^{0,1} \otimes L_{1}^{2}(M)$ are weakly $\widetilde{\mathcal{D}}_{J}^{+}$-closed.
Proof. Notice that
$$\int_{M} F \wedge \widetilde{\mathcal{D}}_{J}^{+}(f)=\int_{M} \omega_{1} \wedge \widetilde{\mathcal{D}}_{J}^{+}(f)=0$$
and
$$\int_{M} d_{J}^{+}(u+\bar{u}) \wedge \widetilde{\mathcal{D}}_{J}^{+}(f)=\int_{M} d(u+\bar{u}) \wedge \widetilde{\mathcal{D}}_{J}^{+}(f)=0$$ \(\square\)

Remark 3.5. If $J$ is integrable, then $\partial_{J}^{2}=0=\bar{\partial}_{J}^{2}, \partial_{J} \bar{\partial}_{J}+\bar{\partial}_{J} \partial_{J}=0$. Hence $d_{J}^{+}(u+\bar{u})$ is also weakly $\partial_{J} \bar{\partial}_{J}$-closed. Since $\widetilde{\omega}_{1}=F-d_{J}^{+}(v+\bar{v})$ is a smooth $d$-closed (1,1)-form, $\widetilde{\omega}_{1}$ is also $\partial_{J} \bar{\partial}_{J}$-closed, hence, $F$ is weakly $\partial_{J} \bar{\partial}_{J}$-closed. Thus, the notation of weakly $\widetilde{\mathcal{D}}_{J}^{+}$-closed is a generalization of the notation of weakly $\partial_{J} \bar{\partial}_{J}$-closed defined in [7] (also see [34]).

Definition 3.6. $\left(\Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)\right)_{w}^{0}:=\left\{c F+\psi \mid \quad c \in \mathbb{R}, \quad \psi \in\left(\Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)\right)_{w}\right.$
$$\text { satisfies } \left.P_{g}^{+}(\psi) \perp \mathcal{H}_{g}^{+} \text {with respect to the integration }\right\}$$

It is clear that $\left(\Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)\right)_{w}^{0} \subset\left(\Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)\right)_{w}$, since $F \in\left(\Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)\right)_{w}$. Let $\psi \in\left(\Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)\right)_{w}^{0}$ and set
$$c_{\psi}=\frac{1}{2} \int_{M} \psi \wedge F .$$
Since $\psi \in\left(\Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)\right)_{w}^{0}$ and
$$\Lambda_{g}^{+}=\mathbb{R} \cdot F \oplus \Lambda_{J}^{-}, \quad \Lambda_{J}^{+}=\mathbb{R} \cdot F \oplus \Lambda_{g}^{-}$$
we can get that $P_{g}^{+}\left(\psi-c_{\psi} F\right)$ is orthogonal to $\mathcal{H}_{g}^{+}(M)$ with respect to the integration. By Hodge decomposition, there exists $f_{\psi} \in L_{2}^{2}(M)_{0}$ such that
$$P_{g}^{+}\left(\psi-c_{\psi} F\right)=P_{g}^{+}\left(\widetilde{\mathcal{D}}_{J}^{+}\left(f_{\psi}\right)\right)$$
holds in $\Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)$. If $\psi$ is smooth, then $f_{\psi}$ is also smooth. By (3.14), we will find that
$$\psi-c_{\psi} F-\widetilde{\mathcal{D}}_{J}^{+}\left(f_{\psi}\right)=P_{g}^{-}\left(\psi-c_{\psi} F-\widetilde{\mathcal{D}}_{J}^{+}\left(f_{\psi}\right)\right) \in \Lambda_{g}^{-} \otimes L^{2}(M)$$
since $P_{g}^{+}\left(\psi-c_{\psi} F-\widetilde{\mathcal{D}}_{J}^{+}\left(f_{\psi}\right)\right)=0$. By Hodge decomposition again, we have the following decomposition
$$\psi-c_{\psi} F-\widetilde{\mathcal{D}}_{J}^{+}\left(f_{\psi}\right)=\beta_{\psi}+d_{g}^{-}\left(\gamma_{\psi}\right)$$
where $\beta_{\psi} \in \mathcal{H}_{g}^{-}(M), \gamma_{\psi} \in \Lambda_{\mathbb{R}}^{1} \otimes L_{1}^{2}(M)$. Hence,
$$\psi=c_{\psi} F+\beta_{\psi}+d_{g}^{-}\left(\gamma_{\psi}\right)+\widetilde{\mathcal{D}}_{J}^{+}\left(f_{\psi}\right) .$$
It is easy to see that $d_{g}^{-}\left(\gamma_{\psi}\right) \in\left(\Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)\right)_{w}^{0}$, since $\psi, F, \beta_{\psi}, \widetilde{\mathcal{D}}_{J}^{+}\left(f_{\psi}\right) \in\left(\Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)\right)_{w}^{0}$. Let
$$\psi^{\prime}=\psi-d_{g}^{-}\left(\gamma_{\psi}\right)=c_{\psi} F+\beta_{\psi}+\widetilde{\mathcal{D}}_{J}^{+}\left(f_{\psi}\right) .$$
$\psi^{\prime}$ is also in $\left(\Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)\right)_{w}^{0}$. If $\psi$ is smooth, both $\psi^{\prime}$ and $f_{\psi}$ are smooth. Then, we have the following equation
$$F \wedge\left(\psi^{\prime}-c_{\psi} F-\widetilde{\mathcal{D}}_{J}^{+}\left(f_{\psi}\right)\right)=0 .$$
If $\psi$ is not smooth, in $\Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)$, we still have
$$\psi=c_{\psi} F+\beta_{\psi}+d_{g}^{-}\left(\gamma_{\psi}\right)+\widetilde{\mathcal{D}}_{J}^{+}\left(f_{\psi}\right),$$
where $\beta_{\psi} \in \mathcal{H}_{g}^{-}(M), c_{\psi}$ is a constant, $f_{\psi} \in L_{2}^{2}(M)_{0}, \gamma_{\psi} \in \Lambda_{\mathbb{R}}^{1} \otimes L_{1}^{2}(M)$, and $d_{g}^{-}\left(\gamma_{\psi}\right) \in$ $\left(\Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)\right)_{w}^{0}$. Let $\psi^{\prime}=c_{\psi} F+\beta_{\psi}+\widetilde{\mathcal{D}}_{J}^{+}\left(f_{\psi}\right)$, then $\psi=\psi^{\prime}+d_{g}^{-}\left(\gamma_{\psi}\right)$. Since $d_{g}^{-}\left(\gamma_{\psi}\right) \in$ $\left(\Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)\right)_{w}^{0}$, it is easy to see that
$$\int_{M} \psi^{\prime} \wedge d_{g}^{-}\left(\gamma_{\psi}\right)=0$$
and
$$\begin{aligned}
\int_{M} \psi^{2} & =\int_{M}\left(\psi^{\prime}+d_{g}^{-}\left(\gamma_{\psi}\right)\right)^{2} \\
& =\int_{M} \psi^{\prime 2}-\left\|d_{g}^{-}\left(\gamma_{\psi}\right)\right\|_{L^{2}(M)}^{2} .
\end{aligned}$$
Also, we can find a smooth sequence of $\left\{f_{\psi, j}\right\} \subset C^{\infty}(M)_{0}$ such that
$$\psi_{j}^{\prime}=c_{\psi} F+\beta_{\psi}+\widetilde{\mathcal{D}}_{J}^{+}\left(f_{\psi, j}\right)$$
is converging to $\psi^{\prime}$ in $L^{2}(M)$. By the above statement, we get the following lemma,

Lemma 3.7. If $\psi \in\left(\Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)\right)_{w}^{0}$, then $\psi$ could be written as
$$\psi=c F+\beta_{\psi}+\widetilde{\mathcal{D}}_{J}^{+}\left(f_{\psi}\right)+d_{g}^{-}\left(\gamma_{\psi}\right),$$
where $f_{\psi} \in L_{2}^{2}(M)_{0}, \beta_{\psi} \in \mathcal{H}_{g}^{-}(M), d_{g}^{-}\left(\gamma_{\psi}\right) \in\left(\Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)\right)_{w}^{0}, \gamma_{\psi} \in \Lambda_{\mathbb{R}}^{1} \otimes L_{1}^{2}(M)$ and $c$ is a constant. Denote $\psi-d_{g}^{-}\left(\gamma_{\psi}\right)$ by $\psi^{\prime}$. Then
$$\int_{M} \psi^{2}=\int_{M} \psi^{\prime 2}-\left\|d_{g}^{-}\left(\gamma_{\psi}\right)\right\|_{L^{2}(M)}^{2},$$
and there is a smooth sequence of $\left\{f_{\psi, j}\right\} \subset C^{\infty}(M)_{0}$ such that
$$\psi_{j}^{\prime}=c F+\beta_{\psi}+\widetilde{\mathcal{D}}_{J}^{+}\left(f_{\psi, j}\right)$$
is converging to $\psi^{\prime}$ in $L^{2}$.
It is similar to the argument of Buchdahl in [7], we need the following lemmas and propositions,

Lemma 3.8. (cf. Lemma 4 in [7]) If $\psi \in\left(\Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)\right)_{w}^{0}$, then
$$\left(\int_{M} F \wedge \psi\right)^{2} \geq\left(\int_{M} F^{2}\right)\left(\int_{M} \psi^{2}\right)$$
with equality if and only if $\psi=c F+\widetilde{\mathcal{D}}_{J}^{+}(f)$ for some constant $c$ and some $f \in L_{2}^{2}(M)_{0}$.
Proof. Let
$$c=\frac{1}{2} \int_{M} F \wedge \psi .$$
By Lemma 3.7, we can get
$$\begin{aligned}
\psi & =\psi^{\prime}+d_{g}^{-}\left(\gamma_{\psi}\right) \\
& =c F+\beta_{\psi}+\widetilde{\mathcal{D}}_{J}^{+}\left(f_{\psi}\right)+d_{g}^{-}\left(\gamma_{\psi}\right),
\end{aligned}$$
where $f_{\psi} \in L_{2}^{2}(M)_{0}, \beta_{\psi} \in \mathcal{H}_{g}^{-}(M), d_{g}^{-}\left(\gamma_{\psi}\right) \in\left(\Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)\right)_{w}^{0}$ and $\gamma_{\psi} \in \Lambda_{\mathbb{R}}^{1} \otimes L_{1}^{2}(M)$. Then
$$P_{g}^{+}\left(\psi^{\prime}-c F-\widetilde{\mathcal{D}}_{J}^{+}\left(f_{\psi}\right)\right)=0 .$$
If $\psi^{\prime}$ is smooth, there is a smooth solution $f_{\psi}$ to the equation
$$F \wedge\left(\psi^{\prime}-c F-\widetilde{\mathcal{D}}_{J}^{+}\left(f_{\psi}\right)\right)=0 .$$
Hence,
$$\begin{aligned}
\left\|\psi^{\prime}-c F-\widetilde{\mathcal{D}}_{J}^{+}\left(f_{\psi}\right)\right\|_{L^{2}(M)}^{2} & =-\int_{M}\left(\psi^{\prime}-c F-\widetilde{\mathcal{D}}_{J}^{+}\left(f_{\psi}\right)\right)^{2} \\
& =-\int_{M}\left(\psi^{\prime}\right)^{2}+2 c \int_{M} F \wedge \psi^{\prime}-2 c^{2} \\
& =-\int_{M}\left(\psi^{\prime}\right)^{2}+2 c^{2} \\
& =-\int_{M}\left(\psi^{\prime}\right)^{2}+\left(\int_{M} F \wedge \psi^{\prime}\right)^{2} /\left(\int_{M} F^{2}\right) .
\end{aligned}$$

Since
$$\left\|\psi^{\prime}-c F-\widetilde{\mathcal{D}}_{J}^{+}\left(f_{\psi}\right)\right\|_{L^{2}(M)}^{2} \geq 0,$$
we can easily get
$$\left(\int_{M} F \wedge \psi^{\prime}\right)^{2} \geq\left(\int_{M} F^{2}\right) \int_{M}\left(\psi^{\prime}\right)^{2} .$$
If $\psi^{\prime}$ is not smooth, the inequality follows from smooth case after approximating $\psi^{\prime}$ by using Lemma 3.7. Hence
$$\left(\int_{M} F \wedge \psi\right)^{2}=\left(\int_{M} F \wedge \psi^{\prime}\right)^{2} \geq\left(\int_{M} F^{2}\right) \int_{M}\left(\psi^{\prime}\right)^{2} \geq\left(\int_{M} F^{2}\right)\left(\int_{M} \psi^{2}\right) .$$

Suppose
$$\left(\int_{M} F \wedge \psi\right)^{2}=\left(\int_{M} F^{2}\right)\left(\int_{M} \psi^{2}\right) .$$
By Lemma 3.7,
$$\int_{M} \psi^{2}=\int_{M}\left(\psi^{\prime}\right)^{2}-\left\|d_{g}^{-}\left(\gamma_{\psi}\right)\right\|^{2}$$
and
$$\begin{aligned}
\left(\int_{M} F \wedge \psi\right)^{2} & =\left(\int_{M} F \wedge \psi^{\prime}\right)^{2} \\
& \geq\left(\int_{M} F^{2}\right) \int_{M}\left(\psi^{\prime}\right)^{2} \\
& \geq\left(\int_{M} F^{2}\right)\left(\int_{M} \psi^{2}\right),
\end{aligned}$$
which implies that
$$d_{g}^{-}\left(\gamma_{\psi}\right)=0, \quad\left(\int_{M} F \wedge \psi^{\prime}\right)^{2}=\left(\int_{M} F^{2}\right) \int_{M}\left(\psi^{\prime}\right)^{2} \quad \text { and } \quad \psi=\psi^{\prime} .$$
By
$$\left(\int_{M} F \wedge \psi^{\prime}\right)^{2}=\left(\int_{M} F^{2}\right) \int_{M}\left(\psi^{\prime}\right)^{2},$$
we have $4 c^{2}=4 c^{2}-2\left\|\beta_{\psi}\right\|_{L^{2}(M)}^{2}$, which implies that $\beta_{\psi}=0$. Hence, $\psi=c F+\widetilde{\mathcal{D}}_{J}^{+}\left(f_{\psi}\right)$. \(\square\)

By Lemma 3.7, we have the following proposition.
Proposition 3.9. Let $\psi_{1}, \psi_{2} \in\left(\Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)\right)_{w}^{0}$ and satisfy
$$\int_{M} \psi_{j}^{2} \geq 0 \text { and } \int_{M} F \wedge \psi_{j} \geq 0$$
for $j=1,2$. Then
$$\int_{M} \psi_{1} \wedge \psi_{2} \geq\left(\int_{M} \psi_{1}^{2}\right)^{\frac{1}{2}}\left(\int_{M} \psi_{2}^{2}\right)^{\frac{1}{2}},$$
with equality if and only if $\psi_{1}$ and $\psi_{2}$ are linearly dependent modulo the image of $\widetilde{\mathcal{D}}_{J}^{+}$.

Proof. It can be assumed that
$$a_{j}=\frac{1}{2} \int_{M} F \wedge \psi_{j}$$
are strictly positive for $j=1,2$ else $\psi_{j}$ are $\widetilde{\mathcal{D}}_{J}^{+}$-exact for $j=1,2$. Indeed, if $a_{j}=0$ for $j=1,2$, then by Lemma 3.7, we have
$$\begin{aligned}
\psi_{j} & =\psi_{j}^{\prime}+d_{g}^{-}\left(\gamma_{\psi_{j}}\right) \\
& =\beta_{\psi_{j}}+\widetilde{\mathcal{D}}_{J}^{+}\left(f_{\psi_{j}}\right)+d_{g}^{-}\left(\gamma_{\psi_{j}}\right),
\end{aligned}$$
where $f_{\psi_{j}} \in L_{2}^{2}(M)_{0}, \beta_{\psi_{j}} \in \mathcal{H}_{g}^{-}(M), d_{g}^{-}\left(\gamma_{\psi_{j}}\right) \in\left(\Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)\right)_{w}^{0}$ and $\gamma_{\psi_{j}} \in \Lambda_{\mathbb{R}}^{1} \otimes L_{1}^{2}(M)$ for $j=1,2$. Hence $\psi_{j}^{\prime}-\widetilde{\mathcal{D}}_{J}^{+}\left(f_{\psi_{j}}\right)=\beta_{\psi_{j}}$ are anti-self-dual smooth harmonic 2-forms, $j=1,2$. Then, by Lemma 3.7,
$$\begin{aligned}
0 & \geq-\left\|\psi_{j}^{\prime}-\widetilde{\mathcal{D}}_{J}^{+}\left(f_{\psi_{j}}\right)\right\|_{L^{2}(M)}^{2} \\
& =\int_{M}\left(\psi_{j}^{\prime}-\widetilde{\mathcal{D}}_{J}^{+}\left(f_{\psi_{j}}\right)\right)^{2} \\
& =\int_{M}\left(\psi_{j}^{\prime}\right)^{2} \\
& =\int_{M} \psi_{j}^{2}+\left\|d_{g}^{-}\left(\gamma_{\psi_{j}}\right)\right\|_{L^{2}(M)}^{2} \geq 0,
\end{aligned}$$
and it follows that $d_{g}^{-}\left(\gamma_{\psi_{j}}\right)=0, \beta_{\psi_{j}}=0$ and $\psi_{j}=\psi_{j}^{\prime}=\widetilde{\mathcal{D}}_{J}^{+}\left(f_{\psi_{j}}\right)$ for $j=1,2$.
To prove the inequality, after replacing $\psi_{j}$ by $\psi_{j}+\varepsilon F$ and taking the limit as $\varepsilon \rightarrow 0$, it can be assumed that
$$\int_{M} \psi_{j}^{2}>0$$
and
$$a_{j}=\frac{1}{2} \int_{M} F \wedge \psi_{j}>0$$
for $j=1,2$. By Lemma 3.7, we have the following decompositions
$$\psi_{j}=a_{j} F+\beta_{\psi_{j}}+\widetilde{\mathcal{D}}_{J}^{+}\left(f_{\psi_{j}}\right)+d_{g}^{-}\left(\gamma_{\psi_{j}}\right),$$
where
$$f_{\psi_{j}} \in L_{2}^{2}(M)_{0}, \beta_{\psi_{j}} \in \mathcal{H}_{g}^{-}(M), d_{g}^{-}\left(\gamma_{\psi_{j}}\right) \in\left(\Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)\right)_{w}^{0},$$
and $\gamma_{\psi_{j}} \in \Lambda_{\mathbb{R}}^{1} \otimes L_{1}^{2}(M)$ for $j=1,2$.
By (3.17), we have
$$a_{2} \psi_{1}-a_{1} \psi_{2}=a_{2} \beta_{\psi_{1}}-a_{1} \beta_{\psi_{2}}+\widetilde{\mathcal{D}}_{J}^{+}\left(a_{2} f_{\psi_{1}}-a_{1} f_{\psi_{2}}\right)+d_{g}^{-}\left(a_{2} \gamma_{\psi_{1}}-a_{1} \gamma_{\psi_{2}}\right) .$$
It follows that
$$a_{2} \psi_{1}-a_{1} \psi_{2}-\widetilde{\mathcal{D}}_{J}^{+}\left(a_{2} f_{\psi_{1}}-a_{1} f_{\psi_{2}}\right)=\left(a_{2} \beta_{\psi_{1}}-a_{1} \beta_{\psi_{2}}\right)+d_{g}^{-}\left(a_{2} \gamma_{\psi_{1}}-a_{1} \gamma_{\psi_{2}}\right)$$
is an anti-self-dual 2-form. So
$$\begin{aligned}
0 & \geq-\left\|a_{2} \beta_{\psi_{1}}-a_{1} \beta_{\psi_{2}}\right\|_{L^{2}(M)}^{2}-\left\|d_{g}^{-}\left(a_{2} \gamma_{\psi_{1}}-a_{1} \gamma_{\psi_{2}}\right)\right\|_{L^{2}(M)}^{2} \\
& =\int_{M}\left(a_{2} \psi_{1}-a_{1} \psi_{2}-\widetilde{\mathcal{D}}_{J}^{+}\left(a_{2} f_{\psi_{1}}-a_{1} f_{\psi_{2}}\right)\right)^{2} \\
& =\int_{M}\left(a_{2} \psi_{1}-a_{1} \psi_{2}\right)^{2} \\
& =a_{2}^{2} \int_{M} \psi_{1}^{2}+a_{1}^{2} \int_{M} \psi_{2}^{2}-2 a_{1} a_{2} \int_{M} \psi_{1} \wedge \psi_{2} \\
& \geq 2 a_{1} a_{2}\left(\int_{M} \psi_{1}^{2}\right)^{\frac{1}{2}}\left(\int_{M} \psi_{2}^{2}\right)^{\frac{1}{2}}-2 a_{1} a_{2} \int_{M} \psi_{1} \wedge \psi_{2},
\end{aligned}$$
giving the desired inequality
$$\int_{M} \psi_{1} \wedge \psi_{2} \geq\left(\int_{M} \psi_{1}^{2}\right)^{\frac{1}{2}}\left(\int_{M} \psi_{2}^{2}\right)^{\frac{1}{2}} .$$
If
$$\int_{M} \psi_{1} \wedge \psi_{2}=\left(\int_{M} \psi_{1}^{2}\right)^{\frac{1}{2}}\left(\int_{M} \psi_{2}^{2}\right)^{\frac{1}{2}},$$
we obtain that $a_{2} \beta_{\psi_{1}}-a_{1} \beta_{\psi_{2}}=0$ and $d_{g}^{-}\left(a_{2} \gamma_{\psi_{1}}-a_{1} \gamma_{\psi_{2}}\right)=0$. Hence, by (3.18), we get
$$a_{2} \psi_{1}-a_{1} \psi_{2}=\widetilde{\mathcal{D}}_{J}^{+}\left(a_{2} f_{\psi_{1}}-a_{1} f_{\psi_{2}}\right) .$$
This completes the proof of Proposition 3.9. \(\square\)

It is easy to see the following corollary,
Corollary 3.10. If $\psi \in\left(\Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)\right)_{w}^{0}$ and satisfies
$$\int_{M} \psi^{2}>0 \text { and } \int_{M} \psi \wedge F>0,$$
then
$$\int_{M} \psi \wedge \varphi>0$$
for any other such form $\varphi \in\left(\Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)\right)_{w}^{0}$ satisfying
$$\int_{M} \varphi^{2} \geq 0 \text { and } \int_{M} \varphi \wedge F>0 .$$

In order to get the desired key lemma (Lemma 3.12), we need the following technical lemma,

Lemma 3.11. If $h_{J}^{-}=b^{+}-1$, then
$$\left(\Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)\right)_{w}^{0}=\left(\Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)\right)_{w} .$$

Proof. It is clear that $\left(\Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)\right)_{w}^{0} \subset\left(\Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)\right)_{w}$. For any $\varphi \in\left(\Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)\right)_{w}$, set
$$c=\frac{1}{2} \int_{M} F \wedge \varphi$$
and let $\widetilde{\varphi}=\varphi-c F$. Then we will find that
$$\int_{M} \widetilde{\varphi} \wedge \omega_{1}=\int_{M} \widetilde{\varphi} \wedge F=0 .$$
Thus, $P_{g}^{+}(\widetilde{\varphi}) \perp \mathcal{H}_{g}^{+}$since $h_{J}^{-}=b^{+}-1$, that is,
$$\mathcal{H}_{g}^{+}=\operatorname{Span}\left\{\omega_{1}, \alpha_{1}, \cdots, \alpha_{h_{J}^{-}}\right\} .$$
$\varphi=c F+\widetilde{\varphi} \in\left(\Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)\right)_{w}^{0}$. Hence $\left(\Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)\right)_{w}^{0}=\left(\Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)\right)_{w}$. \(\square\)

With Corollary 3.10 and Lemma 3.11, as done in the proof of Lemma 7 in [7], we can get the following key lemma,

Lemma 3.12. (Compare Lemma 7 in [7]) Let $(M, J)$ be a closed tamed almost complex 4-manifold with $h_{J}^{-}=b^{+}-1$. Suppose $\varphi \in\left(\Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)\right)_{w}$ and satisfies
$$\int_{M} \varphi \wedge F \geq 0 \text { and } \int_{M} \varphi^{2} \geq 0 .$$
For each $\varepsilon>0$ there is a positive (1,1)-form $p_{\varepsilon}$ and a function $f_{\varepsilon}$ such that
$$\left\|\varphi+\widetilde{\mathcal{D}}_{J}^{+}\left(f_{\varepsilon}\right)-p_{\varepsilon}\right\|_{L^{2}(M)}<\varepsilon .$$
Moreover, $p_{\varepsilon}$ and $f_{\varepsilon}$ can be assumed to be smooth.
Proof. Since $h_{J}^{-}=b^{+}-1$, by Lemma 3.11, we can get $\varphi \in\left(\Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)\right)_{w}^{0}$. If
$$\int_{M} \varphi \wedge F=0$$
by Lemma 3.7, it follows that
$$\varphi=\beta_{\varphi}+\widetilde{\mathcal{D}}_{J}^{+}\left(f_{\varphi}\right)+d_{g}^{-}\left(\gamma_{\varphi}\right) .$$
Then
$$0 \geq-\left\|\beta_{\varphi}\right\|_{L^{2}(M)}^{2}-\left\|d_{g}^{-}\left(\gamma_{\varphi}\right)\right\|_{L^{2}(M)}^{2}=\int_{M}\left(\varphi-\widetilde{\mathcal{D}}_{J}^{+}\left(f_{\varphi}\right)\right)^{2}=\int_{M} \varphi^{2} \geq 0,$$
and we can get $\varphi=\widetilde{\mathcal{D}}_{J}^{+}\left(f_{\varphi}\right)$, that is, $\varphi$ is $\widetilde{\mathcal{D}}_{J}^{+}$exact. In this case the result follows from the denseness of the smooth functions in $L_{2}^{2}(M)_{0}$.

We may assume without loss of generality that
$$\int_{M} \varphi \wedge F>0 .$$
After rescaling $\varphi$ if necessary, it can be supposed that
$$\int_{M} \varphi \wedge F=1 .$$

Let
$$\begin{gathered}
\mathcal{P}:=\left\{p \in \Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M) \mid p \geq 0, \text { a.e. }, \quad \int_{M} p \wedge F=1\right\} ; \\
\mathcal{P}_{\varepsilon}:=\left\{\rho \in \Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M) \mid\|\rho-p\|_{L^{2}(M)}<\varepsilon \text { for some } p \in \mathcal{P}\right\} ; \\
\mathcal{H}_{\varphi}:=\left\{\varphi+\widetilde{\mathcal{D}}_{J}^{+}(f) \mid f \in L^{2}(M)_{0}\right\} .
\end{gathered}$$
Then $\mathcal{P}_{\varepsilon}$ is an open convex subset of the Hilbert space $H:=\Lambda_{\mathbb{R}}^{1,1} \otimes L^{2}(M)$, and $\mathcal{H}_{\varphi}$ is a closed convex subset since $\widetilde{\mathcal{D}}_{J}^{+}$has closed range by Lemma 3.2. If $\mathcal{P}_{\varepsilon} \cap \mathcal{H}_{\varphi}=\emptyset$, the Hahn-Banach Theorem implies that there exists $\phi \in H$ and a constant $c \in \mathbb{R}$ such that
$$\int_{M} \phi \wedge h \leq c, \quad \int_{M} \phi \wedge p>c,$$
for every $h \in \mathcal{H}_{\varphi}$, and every $p \in \mathcal{P}_{\varepsilon}$ (Compare Proof of Theorem I. 7 in D. Sullivan [71] and Proof of Lemma 7 in N. Buchdahl [7]).