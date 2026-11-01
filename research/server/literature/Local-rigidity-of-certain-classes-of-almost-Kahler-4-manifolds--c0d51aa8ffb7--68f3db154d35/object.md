# Local rigidity of certain classes of almost Kahler 4-manifolds

- Category: papers
- Identity: arxiv:math/9911197
- Content status: fulltext_ok

---

---
source_file: math_9911197v2.pdf
converter: mathpix
format: mmd
---

\title{
LOCAL RIGIDITY OF CERTAIN CLASSES OF ALMOST KÄHLER 4-MANIFOLDS
}

\author{
VESTISLAV APOSTOLOV, JOHN ARMSTRONG AND TEDI DRĂGHICI
}

\begin{abstract}
We show that any non-Kähler, almost Kähler 4-manifold for which both the Ricci and the Weyl curvatures have the same algebraic symmetries as they have for a Kähler metric is locally isometric to the (only) proper 3-symmetric 4-dimensional space [17, 20].
\end{abstract}

2000 Mathematics Subject Classification. Primary 53B20, 53C25

\section*{1. Introduction}

An almost Kähler structure on a manifold $M^{2 n}$ is an almost Hermitian structure $(g, J, \Omega)$ with a closed, and therefore symplectic fundamental 2form $\Omega$. If additionally the almost complex structure $J$ is integrable, then $(g, J, \Omega)$ is a Kähler structure. Almost Kähler metrics for which the almost complex structure is not integrable will be called strictly almost Kähler metrics.

Many efforts have been done in the direction of finding curvature conditions on the metric which insure the integrability of the almost complex structure. For example, an old, still open conjecture of Goldberg [16] says that a compact almost Kähler, Einstein manifold is necessarily Kähler. Important progress was made by K. Sekigawa who proved that the conjecture is true if the scalar curvature is non-negative [27]. The case of negative scalar curvature is still wide open, despite of recent progress in dimension 4. Nurowski and Przanowski [24] and K.P.Tod [6, 26] constructed 4-dimensional local examples of Einstein (in fact, Ricci flat), strictly almost Kähler manifolds. Thus, it is now known that compactness must play an essential role, should the Goldberg conjecture be true. In all these examples the structure of the Weyl tensor is unexpectedly special - the anti-self-dual part of the Weyl tensor vanishes and the fundamental form is an eigenform of the self-dual Weyl tensor (equivalently, $W^{-}=0$ and $W_{2}^{+}=0$, see below). Conversely, a recent result of [6] states that any 4-dimensional strictly almost Kähler, Einstein manifold is obtained by Nurowski-Przanowski-Tod construction, provided that the fundamental form is an eigenform of the Weyl tensor. It follows that such a manifold can never be compact. Some

\footnotetext{
The first author was supported in part by an FCAR, a PAFARC-UQAM, and by an NSERC grant. He is also member of EDGE, Research Training Network HPRN-CT-2000-00101, supported by the European Human Potential Programme. The first and the third authors were supported in part by an NSF grant INT-9903302.
}
other positive partial results on the Goldberg conjecture in dimension 4 have been obtained by imposing additional assumptions on the structure of Weyl tensor, cf. [4, 5, 6, 7, 25].

For an oriented four dimensional Riemannian manifold, it is well known the $\mathrm{SO}(4)$-decomposition of the Weyl tensor $W$ into its self-dual and antiself-dual parts, $W^{+}$and $W^{-}$. Moreover, for every almost-Hermitian 4manifold $(M, g, J, \Omega)$ the self-dual part of the Weyl tensor decomposes further under the action of the unitary group U(2). To see this, consider $W^{+}$ as a trace-free, self-adjoint endomorphism of the bundle of self-dual 2-forms $\Lambda^{+} M$. Since $\Lambda^{+} M$ decomposes under U(2) as $\mathbb{R} \Omega \oplus \llbracket \Lambda^{0,2} M \rrbracket$, we can write $W^{+}$as a matrix with respect to this block decomposition as follows:
$$\left(\begin{array}{c|c}
\frac{\kappa}{6} & W_{2}^{+} \\
\hline\left(W_{2}^{+}\right)^{*} & W_{3}^{+}-\frac{\kappa}{12} \operatorname{Id}_{\mid \Lambda^{0,2} M}
\end{array}\right),$$
where the smooth function $\kappa$ is the so-called conformal scalar curvature, $W_{2}^{+}$ corresponds to the part of $W^{+}$that interchanges the two factors of the U(2)splitting of $\Lambda^{+} M$, and $W_{3}^{+}$is a trace-free, self-adjoint endomorphism of the real vector bundle $\llbracket \Lambda^{0,2} M \rrbracket$ underlying the anti-canonical bundle $\Lambda^{0,2} M$. Also, the traceless part of the Ricci tensor Ric ${ }_{0}$ decomposes under U(2) into two irreducible components - the invariant part and the anti-invariant part with respect to $J, \operatorname{Ric}_{0}^{\text {inv }}$ and $\operatorname{Ric}_{0}^{\text {anti }}$. Correspondingly, there are several interesting types of almost Hermitian 4-manifolds, each imposing the vanishing of certain U(2)-components of Ric ${ }_{0}$ and $W$, cf. [28].

The curvature of a Kähler metric $(g, J)$, for instance, satisfies any of the following three conditions:
$$\text { (i) } \operatorname{Ric}_{0}^{\text {anti }}=0 \text {; (ii) } W_{2}^{+}=0 \text {, and (iii) } W_{3}^{+}=0 \text {. }$$
These three conditions are equivalent to the fact that the curvature (considered as a $\mathbb{C}$-linear symmetric endomorphism of the bundle of complex 2-forms) preserves the type decomposition of 2-forms with respect to $J$, a property commonly referred to as the second Gray condition of the curvature, cf. [18].

Of course, the curvature of an arbitrary almost Kähler metric may have none of these algebraic symmetries. It is natural, therefore, to wonder if the integrability of the almost complex structure is implied by the conditions (i)-(iii) above. In [3] and [2] an affirmative answer to this question is given for compact almost Kähler 4-manifolds, by using some powerful global arguments coming from the Seiberg-Witten theory and Kodaira classification of compact complex surfaces. One is then motivated to ask what local rigidity, if any, do the conditions (i)-(iii) impose on almost Kähler 4-manifolds. The goal of our paper is to answer this question.

We first provide a family of strictly almost Kähler 4-manifolds satisfying, more generally, the conditions (i) and (ii), see Proposition 1 below. Note that the strictly almost Kähler, Ricci-flat flat examples of Nurowski,

Przanowski [24] and Tod [6, 26] satisfy (i) and (ii) (but not (iii)), and our examples appear as a generalization of Tod's construction [26, 6]; instead of the Gibbons-Hawking ansatz, we consider its generalized version introduced by LeBrun in [21], and observe that appropriate variable reductions lead to strictly almost Kähler metrics with $J$-invariant Ricci tensor and with special structure of the Weyl tensor. While the Nurowski-Przanowski-Tod examples are just particular metrics in this family, it turns out that for other distinguished metrics the conditions (i)-(iii) are fulfilled. Looking more carefully at the metrics satisfying conditions (i)-(iii) from our family, one can further see that all of them are, in fact, (locally) isometric to the unique 4-dimensional proper (i.e. non-symmetric) 3-symmetric space described by Kowalski [20] (see Section 4 below); as a homogeneous space it is isomorphic to $\left(\operatorname{Isom}\left(\mathbb{E}^{2}\right) \cdot \operatorname{Sol}_{2}\right) / S O(2)$ equipped with a left-invariant metric, or, by introducing an invariant complex structure compatible with the opposite orientation, it becomes isomorphic to the irreducible homogeneous Kähler surface corresponding to the $\mathbf{F}_{\mathbf{4}}$-geometry of [29]. It might be also interesting to note that this same example was discovered in yet a different context by R. Bryant [11] (see also Remark 1).

Although one consequence of the existence of this example is that the conditions (i)-(iii) are not enough to insure the local integrability of an almost Kähler structure, we prove that, in fact, this is the only such example in dimension four.

Theorem 1. Any strictly almost Kähler 4-manifold whose curvature satisfies $\operatorname{Ric}_{0}^{\text {anti }}=0, W_{2}^{+}=0, W_{3}^{+}=0$ is locally isometric to the (unique) 4-dimensional proper 3-symmetric space.

Remarks. 1.- It follows by Theorem 1 and the general theory of 3-symmetric spaces [17] that any complete, simply connected strictly almost Kähler 4manifold satisfying the conditions (i)-(iii) is globally isometric to the proper 3-symmetric 4-space.
2.- Since any 3-symmetric 4-space is almost Kähler and satisfies (i)-(iii) [17], Theorem 1 in turn provides a differential geometric proof of the existence and the uniqueness of the proper 3-symmetric 4-space (see, however, [20] for more general results obtained by using Lie algebra techniques).
3.- Combining Theorem 1 with Wall's classification of compact locally homogeneous complex surfaces [29], one sees that there are no compact strictly almost Kähler 4-manifolds whose curvature satisfies the conditions (i)-(iii). This provides an alternative proof of the integrability result in [3] (see also Corollary 3 below).

Although our main goal of this paper is the study of almost Kähler 4manifolds which satisfy the three conditions (i)-(iii), Theorem 1 is derived from the local classification of a larger class of strictly almost Kähler 4manifolds (Theorem 2), including as particular cases both the Einstein metrics of [24, 6] and the almost Kähler 4-manifold satisfying the conditions (i)-(iii) (see Remark 2). Our results therefore generalize those in [6].

The proof of our results relies on the strategy already developed in [6] for finding out whether a given Riemannian metric locally admits a compatible almost Kähler structure, which allows us, as in [6], to reduce the problem to an integrable Frobenius system. However, the more general class of almost Kähler 4-manifolds that we consider in the current paper leads to more involved proofs and makes the spinorial approach invented in [6] somehow less adequate. We thus prefer to use classical tensorial notations, which we hope will ease the task of the reader in following the technical parts.

The paper is organized as follows: In Sections 2 and 3, we prepare the necessary background of almost Kähler geometry, with a detailed analysis of the Riemannian curvature and its covariant derivative, based on some representation theory. In Section 4, we introduce our main examples of strictly almost Kähler 4-manifolds satisfying conditions (i) and (ii), and describe those which satisfy conditions (i)-(iii); we show that the latter are isometric to the unique proper 3-symmetric 4-space. The last section is devoted to the proof of our main result which is stated in Theorem 2; Theorem 1 is then just a particular case.

\section*{2. The curvature tensor of almost Kähler 4-manifolds}

Let $(M, g)$ be an oriented, 4-dimensional Riemannian manifold. The involutive action of the Hodge operator * on the bundle of 2-forms $\Lambda^{2} M$ induces the decomposition $\Lambda^{2} M=\Lambda^{+} M \oplus \Lambda^{-} M$ into the sub-bundles of self-dual, resp. anti-self-dual 2-forms, corresponding to the +1, resp. -1 eigenspaces of $*$. We will implicitly identify vectors and covectors via the metric $g$ and, accordingly, a 2-form $\phi$ with the corresponding skew-symmetric endomorphism of the tangent bundle $T M$, by putting: $g(\phi(X), Y)=\phi(X, Y)$ for any vector fields $X, Y$. Also, if $\phi, \psi \in T M^{\otimes 2}$, by $\phi \circ \psi$ we understand the endomorphism of $T M$ obtained by the composition of the endomorphisms corresponding to the two tensors. The inner product on $\Lambda^{2} M$ induced by $g$ will be denoted by $\langle\cdot, \cdot\rangle$, so as the induced norm differs by a factor $\frac{1}{2}$ from the usual tensor norm of $T M^{\otimes 2}$.

Considering the Riemannian curvature tensor $R$ as a symmetric endomorphism of $\Lambda^{2} M$ we have the following well known SO(4)-splitting
$$R=\frac{s}{12} \operatorname{Id}_{\mid \Lambda^{2} M}+\widetilde{\operatorname{Ric}_{0}}+W^{+}+W^{-},$$
where $s$ is the scalar curvature, $\widetilde{\operatorname{Ric}_{0}}$ is the the Kulkarni-Nomizu extension of the traceless Ricci tensor Ric ${ }_{0}$ to an endomorphism of $\Lambda^{2} M$ (anti-commuting with *), and $W^{ \pm}$are respectively the self-dual and anti-self-dual parts of the Weyl tensor $W$. The self-dual Weyl tensor $W^{+}$is viewed as a section of the bundle $S_{0}^{2}\left(\Lambda^{+} M\right)$ of symmetric, traceless endomorphisms of $\Lambda^{+} M$ (also considered as a sub-bundle of the tensor product $\Lambda^{+} M \otimes \Lambda^{+} M$ ).

Let $(M, g, J)$ be an almost Hermitian 4-manifold, i.e., an oriented Riemannian 4-manifold $(M, g)$ endowed with a $g$-orthogonal almost complex
structure $J$ which induces the chosen orientation of $M$. We denote by $\Omega$ the corresponding fundamental 2-form, defined by $\Omega(X, Y)=g(J X, Y)$. The action of $J$ extends to the cotangent bundle $\Lambda^{1} M$ by putting $(J \alpha)(X)=$ $-\alpha(J X)$, so as to be compatible with the Riemannian duality between $T M$ and $\Lambda^{1} M$. This action defines an involution, $\imath_{J}$, on $\Lambda^{2} M$ by putting $\imath_{J}(\phi)(X, Y)=\phi(J X, J Y)$, which in turn gives rise to the following orthogonal splitting of $\Lambda^{+} M$ :
$$\Lambda^{+} M=\mathbb{R} \Omega \oplus \llbracket \Lambda^{0,2} M \rrbracket,$$
where $\llbracket \Lambda^{0,2} M \rrbracket$ denotes the bundle of $J$-anti-invariant real 2-forms, i.e., the 2-forms $\phi$ such that $\imath_{J}(\phi)=-\phi$. Note that $\llbracket \Lambda^{0,2} M \rrbracket$ is the real underlying bundle of the anti-canonical bundle $\left(K_{J}\right)^{-1}=\Lambda^{0,2} M$ of $(M, J)$; the induced complex structure $J$ on $\llbracket \Lambda^{0,2} M \rrbracket$ acts by $(J \phi)(X, Y)=-\phi(J X, Y)$.

Consequently, the vector bundle $\mathcal{W}^{+}=S_{0}^{2}\left(\Lambda^{+} M\right)$ of the symmetric traceless endomorphisms of $\Lambda^{+} M$ decomposes into the sum of three sub-bundles, $\mathcal{W}_{1}^{+}, \mathcal{W}_{2}^{+}, \mathcal{W}_{3}^{+}$, defined as follows, see [28]:
\begin{itemize}
\item[-] $\mathcal{W}_{1}^{+}=\mathbb{R} \times M$ is the sub-bundle of elements preserving the decomposition (2) and acting by homothety on the two factors; hence it is the trivial line bundle generated by the element $\frac{1}{8} \Omega \otimes \Omega-\frac{1}{12} \mathrm{Id}_{\mid \Lambda^{+} M}$.
\item[-] $\mathcal{W}_{2}^{+}=\llbracket \Lambda^{0,2} M \rrbracket$ is the sub-bundle of elements which exchange the two factors in (2); the real isomorphism with $\llbracket \Lambda^{0,2} M \rrbracket$ is seen by identifying each element $\phi$ of $\llbracket \Lambda^{0,2} M \rrbracket$ with the element $\frac{1}{2}(\Omega \otimes \phi+\phi \otimes \Omega)$ of $\mathcal{W}_{2}^{+}$.
\item[-] $\mathcal{W}_{3}^{+}=S_{0}^{2}\left(\llbracket \Lambda^{0,2} M \rrbracket\right)$ is the sub-bundle of elements preserving the splitting (2) and acting trivially on the first factor $\mathbb{R} \Omega$.
\end{itemize}

We then obtain the following U(2)-splitting of the Riemannian curvature operator, cf. [28]:
$$R=\frac{s}{12} \operatorname{Id}_{\mid \Lambda^{2} M}+\left(\widetilde{\operatorname{Ric}_{0}}\right)^{\mathrm{inv}}+\left(\widetilde{\operatorname{Ric}_{0}}\right)^{\text {anti }}+W_{1}^{+}+W_{2}^{+}+W_{3}^{+}+W^{-},$$
where $\left(\widetilde{\mathrm{Ric}_{0}}\right)^{\text {inv }}$ and $\left(\widetilde{\mathrm{Ric}_{0}}\right)^{\text {anti }}$ are the Kulkarni-Nomizu extensions of the $J$-invariant and the $J$-anti-invariants parts of the traceless Ricci tensor, respectively, and $W_{i}^{+}$are the projections of $W^{+}$on the spaces $\mathcal{W}_{i}^{+}, i=1,2,3$. The component $W_{1}^{+}$is given by
$$W_{1}^{+}=\frac{\kappa}{8} \Omega \otimes \Omega-\frac{\kappa}{12} \operatorname{Id}_{\mid \Lambda^{+} M},$$
where the smooth function $\kappa$ is the so called conformal scalar curvature of $(g, J)$;
$$W_{2}^{+}=-\frac{1}{4}(\Psi \otimes \Omega+\Omega \otimes \Psi),$$
for a section $\Psi$ of $\llbracket \Lambda^{0,2} M \rrbracket$.
For any (local) section $\phi$ of $\llbracket \Lambda^{0,2} M \rrbracket$ of square-norm 2, the component in
$\mathcal{W}_{3}^{+}$is given by
$$W_{3}^{+}=\frac{\lambda}{2}[\phi \otimes \phi-J \phi \otimes J \phi]+\frac{\mu}{2}[\phi \otimes J \phi+J \phi \otimes \phi],$$
where $\lambda$ and $\mu$ are (locally defined) smooth functions.
For any almost Kähler structure $(g, J, \Omega)$, the covariant derivative $\nabla \Omega$ of the fundamental form is identified with the Nijenhuis tensor of $(M, J)$, the obstruction for the integrability of the almost complex structure $J$. Moreover, $\nabla \Omega$ can be viewed as a section of the real vector bundle underlying $\Lambda^{0,1} M \otimes \Lambda^{0,2} M$, which allows us to write with respect to any section $\phi$ of $\llbracket \Lambda^{0,2} M \rrbracket$ :
$$\nabla \Omega=a \otimes \phi-J a \otimes J \phi .$$
The 1-form $a$ satisfies $|\nabla \Omega|^{2}=4|a|^{2}$, provided that $\phi$ is of square-norm 2. Consequently, the covariant derivatives of $\phi$ and $J \phi$ are given by
$$\nabla \phi=-a \otimes \Omega+b \otimes J \phi ; \quad \nabla J \phi=J a \otimes \Omega-b \otimes \phi,$$
for some 1-form $b$.
Observe that we have an $S^{1}$-freedom for the choice of $\phi$ into the formulas (6) and (7). We shall refer to this as a gauge dependence and any local section $\phi$ of $\llbracket \Lambda^{0,2} M \rrbracket$ of square-norm 2 will be called a gauge.

Convention. From now on, $\phi$ will be assumed to be an eigenform of $W_{3}^{+}$, i.e., the function $\mu$ in (6) identically vanishes.

Note that the above assumption can be locally arranged (for a smooth gauge $\phi$ !) on the open dense subset of points, $x$, where either $W_{3}^{+}(x) \neq 0$, or $W_{3}^{+} \equiv 0$ in the neighbourhood of $x$; however, by continuity, all gauge independent properties will hold everywhere on $M$.

Once the gauge $\phi$ is fixed as above, one can determine the smooth functions $\kappa$ and $\lambda$ and the 2 -form $\Psi$ in terms of the 1 -forms $a$ and $b$ and the 2-form $\phi$, or, equivalently in terms of 2-jets of $J$. For that, we first make use of the Weitzenböck formula for self-dual 2-forms, cf. e.g. [12]:
$$\Delta \psi=\nabla^{*} \nabla \psi+\frac{s}{3} \psi-2 W^{+}(\psi) .$$
Since the fundamental form $\Omega$ is a self-dual, closed 2-form, it is therefore harmonic and (9) implies
$$|\nabla \Omega|^{2}+\frac{2}{3} s-2\left\langle W^{+}(\Omega), \Omega\right\rangle=0,$$
which, by (4)-(6), is equivalent to
$$\kappa-s=6|a|^{2}=\frac{3}{2}|\nabla \Omega|^{2} .$$

Formula (10) shows that the smooth function $\kappa-s$ is everywhere nonnegative on $M$; it vanishes exactly at the points where the Nijenhuis tensor is zero. Observe also that applying (9) to $\Omega$ we involve the 2-jets of $J$. Thus
(10) can be considered as an "obstruction" to lifting the 1-jets of $J$ to 2-jets (see [6]), although eventually it takes form of a condition on the 1-jets.
In order to express $W_{2}^{+}$and $W_{3}^{+}$we make use of the Ricci identity
$$\left(\nabla_{X, Y}^{2}-\nabla_{Y, X}^{2}\right)(\Omega)(\cdot, \cdot)=-R_{X, Y}(J \cdot, \cdot)-R_{X, Y}(\cdot, J \cdot) .$$
From (7) we get
$$\left.\nabla^{2}\right|_{\Lambda^{2} M} \Omega=(d a-J a \wedge b) \otimes \phi-(d(J a)+a \wedge b) \otimes J \phi,$$
so, (11) can be rewritten as
$$d a-J a \wedge b=-R(J \phi) ; d(J a)+a \wedge b=-R(\phi) .$$
Projecting on $\Lambda^{+} M$ and using (3)-(6) and (10), the equalities in (12) give
$$\begin{gathered}
\lambda=-\frac{1}{2}\left(|a|^{2}-\langle d a, J \phi\rangle+\phi(a, b)\right) ; \\
\mu=-\frac{1}{2}(\langle d a, \phi\rangle+J \phi(a, b))=0 ; \\
\Psi=(\langle d(J a), \Omega\rangle+\Omega(a, b)) \phi+(\langle d a, \Omega\rangle+g(a, b)) J \phi .
\end{gathered}$$
We observe again that the relations (13)-(15) are conditions on the 2-jets of the compatible almost Kähler structure $J$, and can be viewed as a further "obstruction" to lifting the 1-jets to 2-jets, see [6].

Similarly, projecting formulae (12) on $\Lambda^{-} M$ we completely determine the $J$-anti-invariant part of the Ricci tensor. In order to determine its $J$ invariant part one needs the 3-jets of $J$, involved in the Ricci identity for the Nijenhuis tensor (viewed as a section of $\Lambda^{1} M \otimes \Lambda^{2} M$ ). Writing the Ricci identity with respect to $\nabla \Omega$ is nothing but adding to (12) one more relation coming from
$$\left(\nabla_{X, Y}^{2}-\nabla_{Y, X}^{2}\right)(\phi)(., .)=-R_{X, Y}(\phi ., .)-R_{X, Y}(., \phi .) .$$
Using (7),(8) and (3)-(6) we eventually obtain
$$d b=a \wedge J a-R(\Omega)=a \wedge J a-\frac{(s+2 \kappa)}{12} \Omega-J \circ\left(\operatorname{Ric}_{0}^{\operatorname{inv}}\right)+\frac{1}{2} \Psi .$$
The closed 2-form $d b$ is gauge independent and is thus defined on whole $M$; in fact, up to a factor $-\frac{1}{2 \pi}, d b$ is a De Rham representative of the first Chern class of $(M, J)$, see e.g. [19].

Note that the relations (12) and (16) completely determine the Ricci tensor and the self-dual Weyl tensor of $(M, g, J)$ in terms of the 3-jets of $J$. One can further see that the remaining part of the curvature, the antiself-dual Weyl tensor, is determined by the 4-jets of $J$. But we shall show in Section 5 that when the metric satisfies some additional properties, the relations (12) and (16) are sufficient to write down the whole Riemannian curvature of $g$. A careful analysis of the above mentioned "obstructions" to lifting the 1, 2 and 3-jets of $J$ will eventually permit us to apply the Frobenius theorem in order to obtain the desired classification.

\section*{3. Almost Kähler 4-manifolds and Gray conditions. Preliminary results}

For a 4-dimensional almost Hermitian manifold, the relations (i)-(iii) mentioned in the introduction are closely related to the following conditions on the curvature defined by A. Gray [18] (not necessarily in the 4-dimensional context).
$\left(G_{1}\right) \quad R_{X Y Z W}=R_{X Y J Z J W}$;
$\left(G_{2}\right) \quad R_{X Y Z W}-R_{J X J Y Z W}=R_{J X Y J Z W}+R_{J X Y Z J W}$;
$\left(G_{3}\right) \quad R_{X Y Z W}=R_{\text {JXJYJZJW }}$.
Identity $\left(G_{i}\right)$ will be called the $i$-th Gray condition. Each imposes on the curvature of the almost Hermitian structure a certain degree of resemblance to that of a Kähler one. A simple application of the first Bianchi identity yields the implications $\left(G_{1}\right) \Rightarrow\left(G_{2}\right) \Rightarrow\left(G_{3}\right)$. Also elementary is the fact that a Kähler structure satisfies relation $\left(G_{1}\right)$ (hence, all of the relations $\left(G_{i}\right)$ ). Following [18], if $\mathcal{A} \mathcal{K}$ is the class of almost Kähler manifolds, let $\mathcal{A} \mathcal{K}_{i}$ be the subclass of manifolds whose curvature satisfies identity $\left(G_{i}\right)$. We have the obvious inclusions
$$\mathcal{A K} \supseteq \mathcal{A} \mathcal{K}_{3} \supseteq \mathcal{A} \mathcal{K}_{2} \supseteq \mathcal{A} \mathcal{K}_{1} \supseteq \mathcal{K},$$
where $\mathcal{K}$ denotes the class of Kähler manifolds. In [16] it was observed that the equality $\mathcal{A} \mathcal{K}_{1}=\mathcal{K}$ holds locally (this fact is an immediate consequence of (10)).

From the examples of Davidov and Muškarov [13], multiplied by compact Kähler manifolds, it follows that the inclusion $\mathcal{A} \mathcal{K}_{2} \supset \mathcal{K}$ is strict in dimension $2 n \geq 6$, even in the compact case. This is no longer true in dimension 4; it was proved in [3] that the equality $\mathcal{A} \mathcal{K}_{2}=\mathcal{K}$ holds for compact 4-manifolds (see also Corollary 3 in Section 5 for a partially different proof of this result).

Let us first observe that the conditions $\left(G_{i}\right)$ fit in with the U(2)-decomposition (3) of the curvature in the following manner:

Lemma 1. An almost Hermitian 4-manifold $(M, g, J)$ satisfies the property $\left(G_{3}\right)$ if and only if the Ricci tensor is $J$-invariant and $W_{2}^{+}=0$. It satisfies $\left(G_{2}\right)$ if moreover $W_{3}^{+}=0$.

Proof: A consequence of (3), see [28]. Q.E.D.
Denote by $\mathcal{D}=\left\{X \in T: \nabla_{X} \Omega=0\right\}$ the Kähler nullity of $(g, J)$ and by $\mathcal{D}^{\perp}$ its $g$-orthogonal complement. According to (7), $\mathcal{D}$ is $J$-invariant at every point and has rank 4 or 2, depending on whether or not the Nijenhuis tensor $N$ vanishes at that point. As an easy consequence of (12), we have the following useful observation:

Lemma 2. A non-Kähler, almost Kähler 4-manifold with J-invariant Ricci tensor belongs to the class $\mathcal{A K}_{3}$ if and only if the Kähler nullity $\mathcal{D}$ is a rank 2 involutive distribution on the open set of points where the Nijenhuis tensor does not vanish.

Proof: Let $\{B, J B\}$ be any (local) orthonormal frame of $\mathcal{D}$ and let $\{A, J A\}$ be an orthonormal frame of $\mathcal{D}^{\perp}$, so that $A$ and $J A$ are the dual orthonormal frame of $\{a, J a\}$, see (7). Then the fundamental form can be written as
$$\Omega=A \wedge J A+B \wedge J B .$$
By (12) we see that $\mathcal{D}$ is involutive if and only if
$$R(\phi)(B, J B)=0, \quad R(J \phi)(B, J B)=0 .$$
On the other hand, as the Ricci tensor is $J$-invariant, it follows by (3)-(6) and (17):
$$R(\phi)(B, J B)=-\frac{1}{4}\langle\Psi, \phi\rangle ; R(J \phi)(B, J B)=-\frac{1}{4}\langle\Psi, J \phi\rangle,$$
i.e., according to (18), we obtain that $\mathcal{D}$ is involutive if and only if $W_{2}^{+}=0$ (see (5)). The claim now follows by Lemma 1. Q.E.D.

We shall further use the following refined version of the differential Bianchi identity [4]:

Lemma 3. (Differential Bianchi identity) Let $(M, g, J)$ be an almost Kähler 4-manifold in the class $\mathcal{A} \mathcal{K}_{3}$. Then the following relations hold:
$$\begin{gathered}
d(\kappa-s)=-12 \lambda J \phi(a) ; \\
\operatorname{Ric}_{0}(a)=\frac{\kappa}{4} a+2 \lambda \phi(b)-J \phi(d \lambda) ; \\
\Delta(\kappa-s)=-\frac{\kappa}{2}(\kappa-s)-24 \lambda^{2}+12 \operatorname{Ric}_{0}(a, a) .
\end{gathered}$$
Proof: The co-differential $\delta W^{+}$of the self-dual Weyl tensor of $(M, g)$ is a section of the rank 8 vector bundle $\mathcal{V}=\operatorname{Ker}\left(\right.$ trace $\left.: \Lambda^{1} M \otimes \Lambda^{+} M \rightarrow \Lambda^{1} M\right)$, where the trace is defined by $\operatorname{trace}(\alpha \otimes \phi)=\phi(\alpha)$ on decomposed elements. For every almost-Hermitian 4-manifold the vector bundle $\mathcal{V}$ splits as $\mathcal{V}=$ $\mathcal{V}^{+} \oplus \mathcal{V}^{-}$, see [1], where $\mathcal{V}^{+}$is identified with the cotangent bundle $\Lambda^{1} M$ by
$$\Lambda^{1} M \ni \alpha \mapsto A=J \alpha \otimes \Omega-\frac{1}{2} \sum_{i=1}^{4} e_{i} \otimes\left(\alpha \wedge e_{i}-J \alpha \wedge J e_{i}\right),$$
while $\mathcal{V}^{-}$is identified (as a real vector bundle) with $\Lambda^{0,1} M \otimes \Lambda^{0,2} M$. For any gauge $\phi$ the vector bundle $\mathcal{V}^{-}$can be again identified with $\Lambda^{1} M$ by
$$\Lambda^{1} M \ni \beta \mapsto B=J \beta \otimes \phi+\beta \otimes J \phi .$$
We denote by $\left(\delta W^{+}\right)^{+}$, resp. $\left(\delta W^{+}\right)^{-}$, the component of $\delta W^{+}$on $\mathcal{V}^{+}$, resp. on $\mathcal{V}^{-}$, and, for any gauge $\phi$ satisfying the Convention of Section 2 we consider the corresponding 1-forms $\alpha$ and $\beta$. By (22), (23) and (4)-(6) one directly calculates:
$$\alpha=-\frac{1}{2} J\left\langle\delta W^{+}, \Omega\right\rangle=-\frac{d \kappa}{12}-\lambda J \phi(a) ;$$
$$\begin{aligned}
\beta & =\frac{1}{2}\left(-J\left\langle\delta W^{+}, \phi\right\rangle+\frac{1}{2} \phi\left\langle\delta W^{+}, \Omega\right\rangle\right) \\
& =-\frac{\kappa}{8} a+\lambda \phi(b)-\frac{1}{2} J \phi(d \lambda)
\end{aligned}$$
Recall that the Cotton-York tensor $C$ of $(M, g)$ is defined by:
$$C_{X, Y, Z}=\frac{1}{2}\left[\nabla_{Z}\left(\frac{s}{12} g+\operatorname{Ric}_{0}\right)(Y, X)-\nabla_{Y}\left(\frac{s}{12} g+\operatorname{Ric}_{0}\right)(Z, X)\right],$$
for any vector fields $X, Y, Z$. Considering $C$ as a 2 -form with values in $\Lambda^{1} M$, the second Bianchi identity reads as $\delta W=C$. In dimension 4 we have also the "half" Bianchi identity
$$\delta W^{+}=C^{+},$$
where $C^{+}$denotes the self-dual part of $C_{X}, X \in T M$. When the Ricci tensor is $J$-invariant, we make use of (26) to give an equivalent expression for the 1 -forms $\alpha$ and $\beta$ in terms of the Ricci tensor and the 1 -form $a$. According to (22) we get
$$\begin{aligned}
& \alpha(X)=-\frac{1}{2} J\left\langle C^{+}, \Omega\right\rangle=-\frac{1}{4} \sum_{i=1}^{4} \nabla_{e_{i}}\left(\frac{s}{12} g+\operatorname{Ric}_{0}\right)\left(J e_{i}, J X\right)= \\
& =-\frac{1}{4}\left[\frac{d s}{12}(X)-\left(\delta \operatorname{Ric}_{0}\right)(X)+\sum_{i=1}^{4} \operatorname{Ric}_{0}\left(e_{i}, J\left(\nabla_{e_{i}} J\right)(X)\right)\right]= \\
& =-\frac{1}{4}\left[\frac{d s}{3}(X)+\sum_{i=1}^{4} \operatorname{Ric}_{0}\left(e_{i}, J\left(\nabla_{e_{i}} J\right)(X)\right)\right] .
\end{aligned}$$
Using (7) and the fact that the Ricci tensor is $J$-invariant, we obtain
$$\sum_{i=1}^{4} \operatorname{Ric}_{0}\left(e_{i}, J\left(\nabla_{e_{i}} J\right)(X)\right)=0,$$
and then
$$\alpha=-\frac{d s}{12} .$$
Regarding the component of $C^{+}$in $\mathcal{V}^{-}$, we have by (23):
$$\beta=\frac{1}{2}\left(-J\left\langle C^{+}, \phi\right\rangle+\frac{1}{2} \phi\left\langle C^{+}, \Omega\right\rangle\right) .$$
To compute $J\left\langle C^{+}, \phi\right\rangle$ we proceed in the same way as computing $J\left\langle C^{+}, \Omega\right\rangle$; instead of $J$ we consider the almost complex structure $I_{\phi}$ whose Kähler form is $\phi$. Observe that Ric ${ }_{0}$ is now $I_{\phi}$-anti-invariant. By (7), (8) and (27) we eventually get
$$\beta=-\frac{1}{2} \operatorname{Ric}_{0}(a) .$$

Comparing (27) and (28) with (24) and (25) we obtain the equalities (19) and (20). Finally, taking co-differential of both sides of (19) and using (20) and (10) we derive
$$\begin{aligned}
\Delta(\kappa-s)= & -12 J \phi(d \lambda, a)-12 \lambda \delta(J \phi(a)) \\
= & 12 \operatorname{Ric}_{0}(a, a)-\frac{\kappa}{2}(\kappa-s)+ \\
& 12 \lambda(2 \phi(a, b)-\langle d a, J \phi\rangle+\delta(J \phi)(a)) .
\end{aligned}$$
By (13) and (8) we calculate
$$12 \lambda(2 \phi(a, b)-\langle d a, J \phi\rangle+\delta(J \phi)(a))=-24 \lambda^{2},$$
and we reach the equality (21). Q.E.D.
We have the following consequence of Lemma 3 (see also [2, Prop.2] and [23, Prop.4]):

Corollary 1. A 4-dimensional almost Kähler structure ( $g, J, \Omega$ ) in the class $\mathcal{A} \mathcal{K}_{3}$ belongs to $\mathcal{A} \mathcal{K}_{2}$ if and only if the norm of $\nabla \Omega$ is constant. Moreover, if $(g, J, \Omega)$ is an $\mathcal{A} \mathcal{K}_{2}$, non-Kähler structure, then the traceless Ricci tensor $\mathrm{Ric}_{0}$ is given by
$$\operatorname{Ric}_{0}=\frac{\kappa}{4}\left[-g^{\mathcal{D}}+g^{\mathcal{D}^{\perp}}\right],$$
where $g^{\mathcal{D}}$ (resp. $g^{\mathcal{D}^{\perp}}$ ) denotes the restriction of $g$ on $\mathcal{D}$ (resp. on $\mathcal{D}^{\perp}$ ).
Proof: According to (10), we have $|\nabla \Omega|^{2}=\frac{\kappa-s}{6}$. We then get by Lemma 3 the equality $d\left(|\nabla \Omega|^{2}\right)=-2 \lambda J \phi(a)$, and the first part of the claim follows by Lemma 1 and (6). Since $W_{3}^{+} \equiv 0$ (i.e. $\lambda \equiv 0$ according to (6)), the second relation stated in Lemma 3 reads as $\operatorname{Ric}_{0}(a)=\frac{\kappa}{4} a$. As $\operatorname{Ric}_{0}$ is symmetric traceless and $J$-invariant tensor, in the case when $(g, J)$ is not Kähler the expression above implies the second part of the corollary. Q.E.D.

\section*{4. Examples of almost Kähler 4-manifolds satisfying Gray conditions}
4.1. 3-symmetric spaces. In this subsection we briefly describe an already known example of strictly almost Kähler 4-manifold satisfying the condition $\left(G_{2}\right)$. This example comes from works of Gray [17] and Kowalski [20] on 3-symmetric spaces and we refer to their papers for more details on the subject.

A Riemannian 3-symmetric space is a manifold $(M, g)$ such that for each point $p \in M$ there exists an isometry $\theta_{p}: M \rightarrow M$ of order 3 (i.e. $\theta_{p}^{3}=1$ ), with $p$ as an isolated fixed point. Any such manifold has a naturally defined (canonical) $g$-orthogonal almost complex structure $J$, and we further require that each $\theta_{p}$ is a holomorphic map with respect to $J$. Moreover, the canonical almost Hermitian structure $(g, J)$ of a 3-symmetric space always satisfies the second Gray condition and, in dimension 4, is automatically almost Kähler (it is Kähler if and only if the manifold is Hermitian symmetric, see [17]). It only remains the question of whether there exists a 4-dimensional example
of a 3-symmetric space with a non-integrable almost complex structure (we shall call this a proper 3-symmetric space). This is solved by Kowalski, who constructs such an example and, moreover, shows that this is the only proper 3-symmetric space in dimension 4 (in fact, this is the only proper generalized symmetric space in dimension 4, [20, Theorem VI.3]). Explicitly, up to a homothety, Kowalski's example is defined on $\mathbb{R}^{4}=\left\{\left(u_{1}, v_{2}, u_{2}, v_{2}\right)\right\}$ with the metric
$$\begin{aligned}
g= & \left(-u_{1}+\sqrt{u_{1}^{2}+v_{1}^{2}+1}\right) d u_{2}^{2}+\left(u_{1}+\sqrt{u_{1}^{2}+v_{1}^{2}+1}\right) d v_{2}^{2} \\
& -2 v_{1} d u_{2} \odot d v_{2} \\
& +\frac{1}{\left(u_{1}^{2}+v_{1}^{2}+1\right)}\left[\left(1+v_{1}^{2}\right) d u_{1}^{2}+\left(1+u_{1}^{2}\right) d v_{1}^{2}-2 u_{1} v_{1} d u_{1} \odot d v_{1}\right]
\end{aligned}$$
where as usually ⊙ stands for symmetric tensor products.
4.2. Generalized Gibbons-Hawking Ansatz. We now present a different and more general approach of obtaining examples of almost Kähler 4manifolds satisfying Gray conditions $\left(G_{3}\right)$ and $\left(G_{2}\right)$, which is based on the idea of generalizing Tod's construction of Ricci-flat strictly almost Kähler 4-manifolds [6, 26]. For this purpose, we consider instead of the Gibbons-Hawking ansatz, its generalized version, introduced by LeBrun [21] to construct scalar-flat Kähler surfaces. Following [21], let $w>0$ and $u$ be smooth real-valued functions on an open, simply-connected set $V \subset \mathbb{R}^{3}=\{(x, y, z)\}$, which satisfy
$$w_{x x}+w_{y y}+\left(w e^{u}\right)_{z z}=0 .$$
Let $M=\mathbb{R} \times V$ and $\omega$ be a 1-form on $M$ non-vanishing when restricted to the $\mathbb{R}$-factor and determined (up to gauge equivalence) by
$$d \omega=w_{x} d y \wedge d z+w_{y} d z \wedge d x+\left(w e^{u}\right)_{z} d x \wedge d y .$$
It is shown in [21] that the metric
$$g=e^{u} w\left(d x^{2}+d y^{2}\right)+w d z^{2}+w^{-1} \omega^{2}$$
admits a Kähler structure $I$, defined by its fundamental form
$$\Omega_{I}=d z \wedge \omega+e^{u} w d x \wedge d y .$$
Moreover, if we denote by $\frac{\partial}{\partial t}$ the dual vector field of $w^{-1} \omega$ with respect to $g$, then $\frac{\partial}{\partial t}$ is Killing and preserves $I$. Conversely, every Kähler metric admitting a hamiltonian Killing field locally arises by this construction [21].

Besides the Kähler structure $I$, we shall consider the almost Hermitian structure $J$ whose fundamental form is
$$\Omega_{J}=-d z \wedge \omega+e^{u} w d x \wedge d y .$$
Clearly, the almost complex structures $I$ and $J$ commute and yield different orientations on $M$. Our objective is the following generalization of [26]:

Proposition 1. Let $w>0$ and $u$ be smooth functions satisfying (30). Then the almost Hermitian structure $(g, J)$ defined via (32) and (34) is almost Kähler if and only if $u$ and $w$ satisfy
$$\left(e^{u} w\right)_{z}=0 .$$
It is Kähler if moreover $w$ does not depend on $x$ and $y$.
Furthermore, the following are true:
\begin{itemize}
\item[(i)] The almost Hermitian manifold $(M, g, J)$ is non-Kähler and belongs to $\mathcal{A} \mathcal{K}_{3}$ if and only if $w$ is a non-constant, positive harmonic function of $x$ and $y$, and $u(x, y)$ is any function defined on $U=V \cap \mathbb{R}^{2}$.
\item[(ii)] The manifold $(M, g, J)$ belongs to $\mathcal{A} \mathcal{K}_{2}$ if and only if, in addition, $w$ has no critical values on $U$ and $u$ is given by
$$u=\ln \left(w_{x}^{2}+w_{y}^{2}\right)-3 \ln w+\text { const } .$$
\end{itemize}

Remark 1. (a) If $w$ is a non-constant harmonic function of $(x, y)$, then the holomorphic function $h$ of $x+i y$ such that $\operatorname{Re}(h)=w$ can be used as a holomorphic coordinate in place of $x+i y$. Up to a change of the smooth function $u$ and the transversal coordinate $t$, the metrics described in Proposition 1(i) are then all isometric to
$$g=e^{u} x\left(d x^{2}+d y^{2}\right)+x d z^{2}+\frac{1}{x}(d t+y d z)^{2},$$
and therefore is defined on $M=\left\{(x, y, z, t) \in \mathbb{R}^{4}, x>0\right\}$ for any smooth function $u$ of $(x, y)$. It is easily checked [21] that the Ricci tensor of the metrics (37) has two vanishing eigenvalues while the scalar curvature $s$ is given by $s=\frac{u_{x x}+u_{y y}}{4 x e^{u}}$. It thus follows that the Ricci-flat Tod's examples are obtained precisely when $u$ is a harmonic function.
(b) Concerning the metrics given in Proposition 1(ii), by (36) we obtain $e^{u}=$ const. $\frac{1}{x^{3}}$, so that (up to homothety of $(z, t)$ ) all these metrics are homothetic to
$$g=\frac{d x^{2}}{x^{2}}+\frac{1}{x^{2}} \sigma_{1}^{2}+x \sigma_{2}^{2}+\frac{1}{x} \sigma_{3}^{2},$$
where $\sigma_{1}=d y ; \sigma_{2}=d z ; \sigma_{3}=d t+y d z$ are the standard generators of the Lie algebra of the three dimensional Heisenberg group Nil ${ }^{3}$. It turns out that (38) defines a complete metric, in fact, a homogeneous one which is nothing else than the (unique) proper 3-symmetric metric (29) mentioned in Sec. 4.1. To see this directly, one should do the change of variables
$$u_{1}=\frac{x^{2}+y^{2}-1}{2 x}, \quad v_{1}=-\frac{y}{x}, \quad u_{2}=t, \quad v_{2}=z,$$
and after a straightforward calculation it can be seen that the metric of Kowalski defined by (29) reduces exactly to (38). In fact, we were motivated to look for and were able to find this change of variables only after we realized that one must have the uniqueness stated in Theorem 1 (see also Remark 4).
\begin{itemize}
\item[(c)] One can easily write down the whole Riemannian curvature of the metric (38): it turns out that it is completely determined by the (constant) scalar curvature $s=\frac{u_{x x}+u_{y y}}{4 x e^{u}}=-\frac{3}{4}$. Indeed, it is easily checked that the conformal scalar curvature (which determines $W^{+}$) is equal to $\frac{3}{4}$, the Ricci tensor has constant eigenvalues (0, 0, - $\frac{3}{8}$, - $\frac{3}{8}$ ), and as $g$ is Kähler with respect to $I$ (see (33)), the anti-self-dual Weyl tensor is also determined by $s$, see e.g. [14]. The metric (38) with its negative Kähler structure $I$ provide therefore a non-symmetric, homogeneous Kähler surface which corresponds to the $\mathbf{F}_{\mathbf{4}}$-geometry of [29]; it is thus a complete irreducible Kähler metric with two distinct constant eigenvalues of the Ricci tensor. From this point of view, the metric (38) has been independently discovered by R. Bryant in [11]. Remark that many others (non-homogeneous in general) Kähler metrics of constant eigenvalues of the Ricci tensor arise from (37), provided that $u$ is a smooth solution to the elliptic equation
$$u_{x x}+u_{y y}=4 s x e^{u},$$
where $s$ is a non-zero constant, the scalar curvature of the metric.
Proof of Proposition 1: By (34) and (31) one readily sees that $\Omega_{J}$ is closed if and only if (35) holds. In order to determine the Kähler nullity $\mathcal{D}$ we consider the $J$-anti-invariant 2 -forms
$$\begin{gathered}
\phi=e^{\frac{u}{2}}(w d z \wedge d x+\omega \wedge d y) \\
J \phi=e^{\frac{u}{2}}(w d z \wedge d y-\omega \wedge d x) .
\end{gathered}$$
They are both of square-norm 2 and we then have
$$d \phi=\tau_{\phi} \wedge \phi ; \quad d(J \phi)=\tau_{J \phi} \wedge J \phi,$$
where, according to (8), the 1 -forms $\tau_{\phi}, \tau_{J \phi}$ are given by
$$\tau_{\phi}=-J b-J \phi(a) ; \quad \tau_{J \phi}=-J b+J \phi(a) .$$
On the other hand, computing $d \phi$ and $d(J \phi)$ directly by making use of (31) we get
$$\tau_{\phi}=\frac{d u}{2}+2(\ln w)_{y} d y ; \quad \tau_{J \phi}=\frac{d u}{2}+2(\ln w)_{x} d x .$$
We conclude by (40) that $J \phi(a)=(\ln w)_{x} d x-(\ln w)_{y} d y$. But we know from (7) that $J \phi(a)$ belongs to $\mathcal{D}$; the latter implies the following relations:
\item[(a)] $(g, J)$ is Kähler if and only if $w$ does not depend on $x$ and $y$;
\item[(b)] if $(g, J)$ is not Kähler, then $\mathcal{D}=\operatorname{span}\left\{\frac{\partial}{\partial x}, \frac{\partial}{\partial y}\right\}$;
\item[(c)] $\left|\nabla\left(\Omega_{J}\right)\right|_{g}^{2}=\frac{w_{x}^{2}+w_{y}^{2}}{4 e^{u} w^{3}}$.
The Ricci form of the Kähler structure ( $g, I$ ) is given by $\frac{1}{2} d d_{I}^{c} u$ (see [21]). Here, and in the rest of the paper, the operator $d_{I}^{c}$ denotes the composition $I \circ d$, where $d$ is the usual differential. Clearly, the Ricci tensor of $g$ is $J$ invariant if and only if $d d_{I}^{c} u$ is a (1,1)-form with respect to $J$. One easily checks that the latter is equivalent to
$$\left(\frac{u_{z}}{w}\right)_{x}=\left(\frac{u_{z}}{w}\right)_{y}=0$$
\end{itemize}

Thus $u_{z}=f w$ for some function $f$ of $z$. By (35) we get moreover $w=\frac{1}{F+h}$, where $F$ is a primitive of $f$, i.e., $\frac{d}{d z} F=f$, and $h$ is a function of $x$ and $y$. According to the relation (a), we know that $h$ is constant if and only if $(g, J)$ is Kähler. Substituting into (30) we obtain that if $h$ is not constant, then $F$ is constant, or equivalently, $w_{z}=0, u_{z}=0$. Thus, if $(g, J)$ is not Kähler, then $u$ and $w$ are functions of $x$ and $y$ and the equation (30) simply means that $w$ is a harmonic function of $x$ and $y$. The Ricci tensor is then given by
$$\operatorname{Ric}=\left(u_{x x}+u_{y y}\right)\left[d x^{2}+d y^{2}\right] .$$
Therefore, according to Corollary 1, the implication in (b) gives $(g, J) \in$ $\mathcal{A} \mathcal{K}_{3}$, while according to Lemma 3, the equality stated in (c) shows that $(g, J) \in \mathcal{A} \mathcal{K}_{2}$ if and only if $e^{u}=$ const. $\frac{w_{x}^{2}+w_{y}^{2}}{w^{3}}$. Q.E.D.
Corollary 2. The inclusions $\mathcal{K} \subset \mathcal{A} \mathcal{K}_{2} \subset \mathcal{A} \mathcal{K}_{3}$ are strict in any dimension $2 n, n \geq 2$.

Proof: Multiplying the examples obtained via Proposition 1 by Riemann surfaces one provides appropriate examples in any dimension. Q.E.D.

\section*{5. Classification results}

The proof of Theorem 1 stated in the introduction will be a consequence of a slightly more general classification that we shall prove in Theorem 2 (see below). The key idea of the proof is to investigate the properties of the negative almost complex structure that we define as follows:
Definition. Let $(M, g, J)$ be a strictly almost-Kähler 4-manifold. On the open set of points where the Nijenhuis tensor of $(g, J)$ does not vanish, let $I$ be the almost complex structure defined to be equal to $J$ on $\mathcal{D}$ and to $-J$ on $\mathcal{D}^{\perp}$.
Clearly, the almost complex structure $I$ is $g$-orthogonal and yields on the manifold the opposite orientation than the one given by $J$. We show that curvature symmetry properties of the almost Kähler structure $(g, J, \Omega)$ have a strong effect on the negative almost Hermitian structure ( $g, I, \bar{\Omega}$ ), where $\bar{\Omega}$ denotes the fundamental form of $(g, I)$.

Let us assume that $(M, g, J, \Omega)$ is a 4-dimensional, strictly almost Kähler manifold of the class $\mathcal{A} \mathcal{K}_{3}$. We use the same notations as in the previous sections, in particular for the 1-forms $a$ and $b$ defined by (7) and (8) under the same convention for the choice of the gauge $\phi$. Our first goal is to show that the negative almost Hermitian structure ( $g, I, \bar{\Omega}$ ) is almost Kähler, and then to determine the 1-forms $\bar{a}, \bar{b}$ corresponding to the negative gauge
$$\bar{\phi}=\phi+\frac{12}{(\kappa-s)} J a \wedge J \phi(a),$$
see (10). This is summarized in the following
Lemma 4. Let ( $M, g, J, \Omega$ ) be a strictly almost Kähler 4-manifold in the class $\mathcal{A K}_{3}$ and let $I$ be the negative, orthogonal, almost complex structure
defined as above. Then $(g, I, \bar{\Omega})$ is an almost Kähler structure compatible with the reversed orientation of $M$. Moreover, $\mathcal{D}^{\perp}$ belongs to the Kähler nullity of $(g, I)$ and, with the choice of the negative gauge as above,
$$\bar{b}=3 b+\frac{12 \lambda}{(\kappa-s)} \phi(a) .$$

Proof: Defining the 1 -forms $m_{i}, n_{i}, i=1,2$, by
$$\nabla a=m_{1} \otimes a+n_{1} \otimes J a+m_{2} \otimes \phi(a)+n_{2} \otimes J \phi(a),$$
we use (7) and (8) to derive the next three equalities:
$$\begin{aligned}
\nabla(J a)= & -n_{1} \otimes a+m_{1} \otimes J a+\left(a-n_{2}\right) \otimes \phi(a) \\
& +\left(m_{2}-J a\right) \otimes J \phi(a) ; \\
\nabla(\phi(a))= & -m_{2} \otimes a+\left(n_{2}-a\right) \otimes J a+m_{1} \otimes \phi(a) \\
& +\left(b-n_{1}\right) \otimes J \phi(a) ; \\
\nabla(J \phi(a))= & -n_{2} \otimes a+\left(J a-m_{2}\right) \otimes J a+\left(n_{1}-b\right) \otimes \phi(a) \\
& +m_{1} \otimes J \phi(a) .
\end{aligned}$$
From (43), (10) and Lemma 3-(19) we obtain
$$\begin{aligned}
m_{1} & =\frac{1}{|a|^{2}} g(\nabla a, a)=\frac{1}{2} d(\ln (\kappa-s)) \\
& =-\frac{6 \lambda}{(\kappa-s)} J \phi(a) .
\end{aligned}$$
We further use the Ricci relations (12) in order to determine the 1-forms $n_{1}, m_{2}$, and $n_{2}$. For that we replace the left-hand sides of the two equalities (12) respectively by
$$\begin{gathered}
d a=m_{1} \wedge a+n_{1} \wedge J a+m_{2} \wedge \phi(a)+n_{2} \wedge J \phi(a), \\
d(J a)=-n_{1} \wedge a+m_{1} \wedge J a+\left(a-n_{2}\right) \wedge \phi(a)+\left(m_{2}-J a\right) \wedge J \phi(a),
\end{gathered}$$
(see (44)), and also take into account that under the $\mathcal{A} \mathcal{K}_{3}$ assumption we have
$$R(\phi)=\left(\frac{s-\kappa}{12}+\lambda\right) \phi ; \quad R(J \phi)=\left(\frac{s-\kappa}{12}-\lambda\right) J \phi,$$
see Lemma 1 and (3)-(6). After comparing the components of both sides, we obtain
$$n_{1}=-b-\frac{6 \lambda}{(\kappa-s)} \phi(a) ; m_{2}=\frac{1}{2} J a+J m_{0} ; n_{2}=\frac{1}{2} a+m_{0},$$
where $m_{0}$ is a 1-form which belongs to $\mathcal{D}$.
With relations (43)-(46) in hand, we can now compute $\nabla \bar{\Omega}$, starting from $\bar{\Omega}=\Omega-\frac{12}{(\kappa-s)} a \wedge J a$ (see (10)), and also using (7). We get:
$$\nabla \bar{\Omega}=2 m_{0} \otimes \bar{\phi}-2 I m_{0} \otimes I \bar{\phi} .$$
This proves that ( $g, I, \bar{\Omega}$ ) is an almost Kähler structure, since $d \bar{\Omega}=0$ is immediate from (47). The claim about the Kähler nullity of $(g, I)$ follows
from $\bar{a}=2 m_{0} \in \mathcal{D}$. Similarly, starting from (41) and using (8), (43)-(46) we obtain
$$\nabla \bar{\phi}=\left(3 b+\frac{12 \lambda}{(\kappa-s)} \phi(a)\right) \otimes I \bar{\phi}-2 m_{0} \otimes \bar{\Omega},$$
and the relation (42) follows. Q.E.D.
As our statements are purely local, for brevity purposes, we now introduce the following
Definition. Let $(M, g, J)$ be a strictly almost Kähler 4-manifold in the class $\mathcal{A} \mathcal{K}_{3}$, and suppose that the Nijenhuis tensor of $(g, J)$ does not vanish anywhere. We say that $(M, g, J)$ is a doubly $\mathcal{A} \mathcal{K}_{3}$ manifold, if the almost Kähler structure $(g, I)$ defined above belongs to the class $\mathcal{A} \mathcal{K}_{3}$ as well.
Remark 2. Every non-Kähler 4-manifold in the class $\mathcal{A} \mathcal{K}_{3}$, which is Einstein, or belongs to class $\mathcal{A} \mathcal{K}_{2}$ is a doubly $\mathcal{A} \mathcal{K}_{3}$ manifold. Indeed, this is an immediate consequence of Lemma 2 and Corollary 1. Note also that all the examples arising from Proposition 1 are doubly $\mathcal{A} \mathcal{K}_{3}$ manifolds - the negative almost Kähler structure $(g, I)$ is in fact Kähler for all these examples.

To anticipate, the end result of this section, slightly more general than Theorem 1, will be that every non-Kähler, doubly $\mathcal{A} \mathcal{K}_{3}$ 4-manifold is necessarily given by Proposition 1. Getting closer to this goal, we now prove

Proposition 2. Let $(M, g, J)$ be a non-Kähler, doubly $\mathcal{A} \mathcal{K}_{3}$ 4-manifold. Then the negative almost Kähler structure $(g, I)$ is Kähler. Moreover, the Ricci tensor is given by
$$\operatorname{Ric}=\frac{s}{2} g^{\mathcal{D}}$$
where $g^{\mathcal{D}}$ denotes the restriction of the metric to the Kähler nullity $\mathcal{D}$ of $(g, J)$.

Proof of Proposition 2: For the beginning, we assume only that $(M, g, J)$ is a strictly almost Kähler manifold of the class $\mathcal{A} \mathcal{K}_{3}$. We use the Bianchi identity (19), together with (20) rewritten as
$$d \lambda=2 \lambda J b-\frac{\kappa}{4} J \phi(a)+J \phi\left(\operatorname{Ric}_{0}(a)\right),$$
and the relation (see (44)-(46))
$$d(J \phi(a))=-2 b \wedge \phi(a)-m_{0} \wedge a-J m_{0} \wedge J a .$$
Differentiating (19), we get by (49) and (50):
$$\begin{aligned}
0=2 \lambda(b \wedge \phi(a) & -J b \wedge J \phi(a))+\lambda\left(m_{0} \wedge a+J m_{0} \wedge J a\right) \\
& -J \phi\left(\operatorname{Ric}_{0}(a)\right) \wedge J \phi(a) .
\end{aligned}$$
Taking various components, the relation (51) can be seen to be equivalent to:
$$\lambda m_{0}=2 \lambda \phi\left(b^{\mathcal{D}^{\perp}}\right)=\frac{1}{2}\left(\operatorname{Ric}_{0}(a)\right)^{\mathcal{D}},$$
where the super-scripts $\mathcal{D}$ and $\mathcal{D}^{\perp}$ denote the projections on those spaces. Now we shall consider separately the following two cases:

Case 1. $(M, g, J)$ is a doubly $\mathcal{A} \mathcal{K}_{3}$ manifold which does not belong to $\mathcal{A} \mathcal{K}_{2}$. Then by Corollary 1 we have $\lambda \neq 0$. Since, by assumption, the Ricci tensor is both $J$ and $I$ invariant, it follows that $\mathcal{D}$ and $\mathcal{D}^{\perp}$ are eigenspaces for the traceless Ricci tensor Ric ${ }_{0}$. In other words, we have
$$\operatorname{Ric}_{0}=\frac{f}{4}\left[-g^{\mathcal{D}}+g^{\mathcal{D}^{\perp}}\right],$$
where $f$ is a smooth function. This implies that $\left(\operatorname{Ric}_{0}(a)\right)^{\mathcal{D}}=0$. Since $\lambda \neq 0$, from (52) it follows that $m_{0}=0$, i.e., $(g, I)$ is Kähler, see (47). Also, from (52) it follows that $b \in \mathcal{D}$. Under the doubly $\mathcal{A} \mathcal{K}_{3}$ assumption, the Ricci relation (16) takes the form
$$d b=a \wedge J a-\frac{(s+2 \kappa)}{12} \Omega+\frac{f}{4} \bar{\Omega},$$
or further (see (10))
$$d b=-\frac{(s+f)}{4} A \wedge J A+\frac{(3 f-s-2 \kappa)}{12} B \wedge J B,$$
where $\{B, J B\}$ is an orthonormal basis for $\mathcal{D}$ and $\{A, J A\}$ is an orthonormal basis for $\mathcal{D}^{\perp}$. Similarly, the Ricci relation (16), written with respect to the Kähler structure $(g, I)$, reads as
$$d \bar{b}=\frac{(f+s)}{4} A \wedge J A+\frac{(f-s)}{4} B \wedge J B .$$
On the other hand, using Lemma 3-(19), the equality (42) can be rewritten as
$$\bar{b}=3 b+d_{J}^{c} \ln (\kappa-s),$$
where, we recall, $d_{J}^{c}=J \circ d$. After differentiating we obtain the gauge independent equality
$$d \bar{b}=3 d b+d d_{J}^{c}(\ln (\kappa-s)) .$$
For computing $d d_{J}^{c}(\ln (\kappa-s))$, we remark first that by Lemma 3-(19) the vector field dual to $d_{J}^{c}(\ln (\kappa-s))$ belongs to the kernel $\mathcal{D}$ of the Nijenhuis tensor of $J$, so that $d d_{J}^{c}(\ln (\kappa-s))$ is a (1,1)-form with respect to $J$. Furthermore, from Lemma 3-(19) it also follows that $d_{J}^{c} \ln (\kappa-s)=d_{I}^{c}(\ln (\kappa-s))$, and then
$$d d_{J}^{c}(\ln (\kappa-s))=d d_{I}^{c}(\ln (\kappa-s)),$$
where $d_{I}^{c}=I \circ d$ stands for the $d^{c}$ operator with respect to $I$. Since $I$ is integrable, the latter equality shows that the 2-form $d d_{J}^{c}(\ln (\kappa-s))$ it is of type $(1,1)$ with respect to $I$ as well. Finally, keeping in mind that $I$ is Kähler
and $J$ is almost Kähler , from (57), (21) and (19) we compute
$$\begin{aligned}
\left\langle d d_{J}^{c}(\ln (\kappa-s)), \bar{\Omega}\right\rangle & =\left\langle d d_{J}^{c}(\ln (\kappa-s)), \Omega\right\rangle \\
& =-\Delta \ln (\kappa-s) \\
& =-\frac{\Delta(\kappa-s)}{(\kappa-s)}+\frac{|d(\kappa-s)|^{2}}{(\kappa-s)^{2}} \\
& =\frac{\kappa-f}{2} .
\end{aligned}$$
Since $d d_{J}^{c}(\ln (\kappa-s))$ is a (1,1)-form with respect to both $J$ and $I$, the latter equality shows that
$$d d_{J}^{c}(\ln (\kappa-s))=\frac{(\kappa-f)}{2} B \wedge J B .$$
By (54), (55) and (58), the equality (56) finally reduces to $f+s=0$ which, together with (53), imply the claimed expression of the Ricci tensor.

Case 2. ( $M, g, J$ ) is non-Kähler manifold in the class $\mathcal{A} \mathcal{K}_{2}$. Now $\lambda=0$ by Lemma 1, so the equality (52) is not useful anymore, as all terms vanish trivially. However, applying Case 1 to the structure $(g, I)$, we conclude that it must be itself in the class $\mathcal{A} \mathcal{K}_{2}$, since otherwise it would follow that $(g, J)$ is Kähler, a contradiction. With the same choices of the gauge as in Lemma 4, we have in this case $\bar{b}=3 b$. This leads to the gauge independent relation $d b=3 d b$. Assuming that $(g, I)$ is not Kähler, we interchange the roles of $J$ and $I$ to also get $d b=3 d \bar{b}$, i.e., $d b=0$ holds. But this leads to a contradiction. Indeed, according to Corollary 1 we have $f=\kappa$, so from the Ricci relation (54) we get $\kappa-s=0$, i.e., $(g, J)$ is Kähler which contradicts the assumption. Thus $(g, I)$ must be Kähler and (55) holds. It is easily checked that $d \bar{b}=3 d b$ is, in this case, equivalent to $\kappa+s=0$. This and Corollary 1 imply the desired form of the Ricci tensor. Q.E.D.

Proposition 3. Let $(M, g, J)$ be a non-Kähler, doubly $\mathcal{A} \mathcal{K}_{3}$ 4-manifold. Then $\mathcal{D}^{\perp}$ is spanned by commuting Killing vector fields.

Proof of Proposition 3: For any smooth functions $p$ and $q$ we consider the vector field $X_{p, q}$ in $\mathcal{D}^{\perp}$, the dual to the 1-form $p a+q J a$. The condition that $X_{p, q}$ is Killing is equivalent to $\nabla(p a+q J a)$ being a section of $\Lambda^{2} M$. To write explicitly the equation on $p$ and $q$ that arise from the latter condition we need the covariant derivative of $a$ and $J a$. But we know already by Proposition 2 that $(g, I)$ is Kähler, i.e., the 1-form $m_{0}$ defined in (46) vanishes (see (47)).

We thus have by (43)-(46)
$$\begin{aligned}
\nabla a= & -\frac{6 \lambda}{(\kappa-s)} J \phi(a) \otimes a-\frac{6 \lambda}{(\kappa-s)} \phi(a) \otimes J a \\
& -b \otimes J a+\frac{1}{2} J a \otimes \phi(a)+\frac{1}{2} a \otimes J \phi(a) ; \\
\nabla(J a)= & \frac{6 \lambda}{(\kappa-s)} \phi(a) \otimes a-\frac{6 \lambda}{(\kappa-s)} J \phi(a) \otimes J a \\
& +b \otimes a+\frac{1}{2} a \otimes \phi(a)+\frac{1}{2} J a \otimes J \phi(a) .
\end{aligned}$$
Using (59) and (60) the condition that $\nabla(p a+q J a)$ belongs to $\Lambda^{2} M$ can be rewritten as
$$\left.\begin{array}{l}
d p=-q b-\frac{p}{2}\left(1-\frac{12 \lambda}{(\kappa-s)}\right) J \phi(a)-\frac{q}{2}\left(1+\frac{12 \lambda}{(\kappa-s)}\right) \phi(a)+r J a ; \\
d q=p b-\frac{p}{2}\left(1-\frac{12 \lambda}{(\kappa-s)}\right) \phi(a)+\frac{q}{2}\left(1+\frac{12 \lambda}{(\kappa-s)}\right) J \phi(a)-r a,
\end{array}\right\}$$
where $r$ is a smooth function. Since we are looking for commuting Killing fields, we have $r \equiv 0$, and we thus obtain a Frobenius type system. To show that (61) has solution in a neighborhood of a point $x \in M$ for any given values $(p(x), q(x))$, we apply the Frobenius theorem. Accordingly, we have to check
$$\begin{gathered}
d\left(2 q b+p\left(1-\frac{12 \lambda}{(\kappa-s)}\right) J \phi(a)+q\left(1+\frac{12 \lambda}{(\kappa-s)}\right) \phi(a)\right)=0 \\
d\left(-2 p b+p\left(1-\frac{12 \lambda}{(\kappa-s)}\right) \phi(a)-q\left(1+\frac{12 \lambda}{(\kappa-s)}\right) J \phi(a)\right)=0
\end{gathered}$$
For that we further specify the relations (44) and (54), taking into account that $m_{0}=0$ and $f=-s$ (see Proposition 2). We thus get:
$$\begin{gathered}
d(J \phi(a))=-2 J b \wedge J \phi(a), \\
d(\phi(a))=2 b \wedge J \phi(a)+2 \lambda B \wedge J B, \\
d b=-\frac{(2 s+\kappa)}{6} B \wedge J B,
\end{gathered}$$
where $B=\frac{1}{|a|} \phi(a)$ and $J B=\frac{1}{|a|} J \phi(a)$ is an orthonormal frame of $\mathcal{D}$. By Lemma 3 and (58) we also have
$$\begin{gathered}
d \ln (\kappa-s)=-\frac{12 \lambda}{(\kappa-s)} J \phi(a) ; \quad d_{J}^{c} \ln (\kappa-s)=\frac{12 \lambda}{(\kappa-s)} \phi(a), \\
d d_{J}^{c}(\ln (\kappa-s))=\frac{(\kappa+s)}{2} B \wedge J B .
\end{gathered}$$
Using the above equalities, together with (61) and (10), it is now straightforward to check (62) and (63). Q.E.D.

Remark 3. The miraculous cancellation that appears by checking the equalities (62) and (63) can be explained by simply observing that if the
cancellation hadn't occurred we would then derive an integrability condition depending on $\lambda$ and $\kappa-s$. But these take arbitrary values for the examples provided by Proposition 1. We thus conclude that the integrability conditions (62) and (63) must be satisfied.

Theorem 2. Any 4-dimensional non-Kähler, doubly $\mathcal{A} \mathcal{K}_{3}$ metric is locally isometric to one of the metrics described by Proposition 1(i) (or equivalently, by (37)).

Proof of Theorem 2: Let $(M, g, J)$ be a non-Kähler, doubly $\mathcal{A} \mathcal{K}_{3} 4$-manifold. By Proposition 2, there exists a Kähler structure $I$, which yields the opposite orientation of $M$. Moreover, we know by Proposition 3 that in a neighborhood of any point there exists a Killing vector field $X \in \mathcal{D}^{\perp}$, determined by a solution of the system (61). It is not difficult to check that $X$ preserves $I$. Indeed, we have to verify
$$\mathcal{L}_{X} \bar{\Omega}=d(I(p a+q J a))=d(q a-p J a)=0 .$$
The latter equality is a consequence of (61) and the Ricci identities (12) (If the manifold is not Ricci flat, the invariance of $I$ also follows from the fact that $I$ is determined up to sign by the two eigenspaces of Ric). According to [21], the metric $g$ has the form (32), where the functions $w$ and $u$ satisfy (30) and $X=\frac{\partial}{\partial t}$. From Proposition 2 we also know that $\operatorname{Ric}(X)=0$. But the Ricci form of the Kähler structure ( $g, I$ ) is given by $\frac{1}{2} d d_{I}^{c} u$ (see [21]); we thus obtain $w=$ const. $u_{z}$ and then
$$\operatorname{Ric}=\left(u_{x x}+u_{y y}+\left(e^{u}\right)_{z z}\right)\left[d x^{2}+d y^{2}\right] .$$
The above equality shows that either $g$ is Ricci flat (then $g$ is given by Tod's ansatz, see [6]), or else, according to Proposition 2, the Kähler nullity $\mathcal{D}$ of $(g, J)$ is spanned by the (Riemannian) dual fields $d x$ and $d y$. The latter means that the Kähler form $\Omega$ of $(g, J)$ is given by (34), and the result follows by Proposition 1 and Remark 1. Q.E.D.

Theorem 1 is now just a particular case.
Proof of Theorem 1. By Remark 2 we know that every strictly almost-Kähler 4-manifold ( $M, g, J, \Omega$ ) satisfying ( $G_{2}$ ) is doubly $\mathcal{A} \mathcal{K}_{3}$; it follows by Theorem 2 and Proposition 1 that $(M, g, J, \Omega)$ arises from Proposition 1(ii). According to Remark 1(b) the metric $g$ is locally isometric to (38) which, in turn, is isometric to Kowalski's metric, doing the change of variables (39). Q.E.D.
Remark 4. Avoiding the use of the change of variables (39), one could have completed the proof of Theorem 1 as follows: as above one shows that any strictly almost-Kähler 4-manifold $(M, g, J, \Omega)$ satisfying $\left(G_{2}\right)$ is locally isometric to (38). On the other hand, A.Gray [17] showed that any Riemannian 3-symmetric space has a canonical almost-Hermitian structure, which in 4-dimensions, is necessarily almost-Kähler (Kähler iff the manifold is symmetric) and satisfies the condition $\left(G_{2}\right)$. It thus follows that the
proper 3-symmetric metric of Kowalski [20] is isometric to (38) as well. In particular, this provides a differential geometric proof of existence and uniqueness of proper 3-symmetric 4-dimensional manifolds, result proved by Kowalski using Lie algebra techniques [20].

Corollary 3. ([3]) Every compact almost Kähler 4-manifold satisfying the second curvature condition of Gray is Kähler.

Proof of Corollary 3: Suppose for contradiction that $(M, g, J)$ is a compact, non-Kähler, almost Kähler 4-manifold in the class $\mathcal{A} \mathcal{K}_{2}$.

According to Corollary 1, the distributions $\mathcal{D}$ and $\mathcal{D}^{\perp}$ are globally defined on $M$, and by Proposition 2 they give rise to a negative Kähler structure $(g, I)$. We know by Theorem 1 that $(g, J, I)$ locally arise from Proposition 1. Then the whole curvature of $g$ is completely determined by the (negative constant) scalar curvature $s$, cf. Remark 1. More precisely, the conformal curvature $\kappa$ is given by $\kappa=-s$ (Corollary 1 and Proposition 2). Since $(g, I)$ is Kähler, we also have $\left|W^{-}\right|^{2}=\frac{s^{2}}{24}$, see e.g. [14]. As $(g, J)$ is in the class $\mathcal{A} \mathcal{K}_{2}$, the self-dual Weyl tensor satisfies $W_{2}^{+}=0, W_{3}^{+}=0$ and then $\left|W^{+}\right|^{2}=\frac{\kappa^{2}}{24}$ (see (4)); by $\kappa=-s$ we conclude $\left|W^{+}\right|^{2}=\left|W^{-}\right|^{2}=\frac{s^{2}}{24}$. We then get by the Chern-Weil formula
$$\sigma(M)=\frac{1}{12 \pi^{2}} \int_{M}\left|W^{+}\right|^{2}-\left|W^{-}\right|^{2} d V_{g}$$
that the signature $\sigma(M)$ vanishes. Similarly, the Euler characteristic $e(M)$ is given by
$$e(M)=\frac{1}{8 \pi^{2}} \int_{M}\left|W^{+}\right|^{2}+\left|W^{-}\right|^{2}+\frac{s^{2}}{24}-\frac{1}{2}\left|\operatorname{Ric}_{0}\right|^{2} d V_{g} .$$
But we know that the Ricci tensor of $g$ has eigenvalues $\left(0,0, \frac{s}{2}, \frac{s}{2}\right)$ (Proposition 2) and then $\left|\operatorname{Ric}_{0}\right|^{2}=\frac{s^{2}}{4}$; we thus readily see that $e(M)=0$. Furthermore, since $(\bar{M}, g, I)$ is a Kähler surface of (constant) negative scalar curvature, we have $H^{0}\left(\bar{M}, K^{\otimes-m}\right)=0$, where $K$ denotes the canonical bundle of $(\bar{M}, I)$. The conditions $\sigma(\bar{M})=-\sigma(M)=0, e(\bar{M})=e(M)=0$ then imply that the Kodaira dimension of $(\bar{M}, I)$ is necessarily equal to 1 , cf. e.g. [8]. Thus $(\bar{M}, I)$ is a minimal properly elliptic surface with vanishing Euler characteristic. Using an argument from [3], we conclude that, up to a finite cover, $(\bar{M}, I)$ admits a non-vanishing holomorphic vector field $X$. Now the well known Bochner formula for holomorphic fields and the fact that the Ricci tensor of $(\bar{M}, g, I)$ is semi-negative whose kernel is the distribution $\mathcal{D}^{\perp}$ (Proposition 2) imply that $X$ is parallel and belongs to $\mathcal{D}^{\perp}$. Then $\mathcal{D}^{\perp}$ (hence also $\mathcal{D}$ ) is parallel. Since $(g, I)$ is a Kähler structure, $I$ is parallel, and consequently, the almost complex structure $J$ must be parallel as well, i.e., $(g, J)$ is Kähler, which contradicts our assumption. Q.E.D.
Remark 5. For obtaining a contradiction in the proof of Corollary 3 one can alternatively argue as follows: We know by Theorem 1 that $(g, J, I)$
locally arise from Proposition 1. The metric $g$ is therefore locally homogeneous and the complex structure $I$ is invariant as being determined by the eigenspaces of the Ricci tensor. It thus follows that $(M, g, I)$ is a compact locally homogeneous Kähler surface; it is well known that any such surface is locally (Hermitian) symmetric (cf. e.g. [29]), while the metric $g$ given by Proposition 1(ii) is not.
Remark 6. Using the method of "nuts and bolts" [15], C.LeBrun [22] successfully "compactified" certain Kähler metrics arising from (32) and obtained explicit examples of compact scalar-flat Kähler surfaces admitting a circle action. The idea is the following: Starting from an open (incomplete) manifold $M_{0}$ where the metric $g$ has the form (32), one adds points and (real) surfaces in order to obtain a larger, complete manifold $M$, such that $M_{0}$ is a dense open subset of $M$, and the circle action on $M_{0}$ generated by the Killing vector field $X=\frac{\partial}{\partial t}$ extends to $M$; the added points and surfaces become the fixed point of this action.

It is thus natural to wonder if similar "compactification" exists for the metrics given by Proposition 1, providing compact examples of non-Kähler, almost Kähler 4-manifolds in the class $\mathcal{A} \mathcal{K}_{3}$. (The interest in such compact examples is motivated by some variational problems on compact symplectic manifolds [9, 10]). Corollary 3 shows that this is impossible if we insist that (36) is satisfied. Unfortunately, even in the case when (36) does not hold, the variable reduction we have for the functions $u$ and $w$ does not permit us to obtain compact examples directly following LeBrun's approach. Indeed, if $(M, g, J)$ was a compactification of $\left(M_{0}, J, g\right)$ with extended circle action generated by a Killing vector field $X=\frac{\partial}{\partial t}$, then by Propositions 2 and 3, we would have $\operatorname{Ric}(X, X)=0$ on $M_{0}$, hence also, on $M$ as $M_{0}$ is a dense subset; by the Bochner formula $X$ would then be parallel. In particular, the $g$-norm of $X$ would be constant, hence also, the smooth function $w=\frac{1}{g(X, X)}$. Therefore, $(g, J)$ would be Kähler by Proposition 1, a contradiction.

As a final note, it is tempting to conjecture that the local classification obtained in Theorem 2 could be further extended to the general case of strictly $\mathcal{A} \mathcal{K}_{3}$ 4-manifolds (in other words, we believe that the doubly $\mathcal{A} \mathcal{K}_{3}$ assumption in the Theorem 2 could be removed). For this goal a further analysis of the higher jets of $J$ would be needed, with computations becoming more involved, but it is possible that some nice cancellations might still take place.

Acknowledgements: The first author thanks the Mathematical Institute of Oxford for hospitality during the preparation of an important part of this paper. The authors are grateful to R. Bryant, G. Gibbons, C. LeBrun, S. Salamon and P. Tod for their interest and some stimulating discussions. We would also like to express our thanks to O. Muškarov whose comments essentially improved the presentation of the results in Section 4, to D. Blair for his friendly assistance in reading the manuscript and suggesting several improvements, and to A. Moroianu for bringing to our attention the unpublished work [11].

\section*{References}
\begin{itemize}
\item[] [1] V.Apostolov and P.Gauduchon, The Riemannian Goldberg-Sachs Theorem, Int. J. Math. 8 (1997), 421-439.
\item[] [2] V. Apostolov and T. Draghici, Almost Kähler 4-manifolds with J-invariant Ricci tensor and special Weyl tensor, Q. J. Math. 51 (2000), 275-294.
\item[] [3] V. Apostolov, T. Draghici, and D. Kotschick, An integrability theorem for almost Kähler 4-manifolds, C. R. Acad. Sci. Paris t.329, sér. I (1999), 413-418.
\item[] [4] V. Apostolov, J. Armstrong, Symplectic 4-manifolds with Hermitian Weyl tensor, Trans. Amer. Math. Soc. 352 (2000), 4501-4513.
\item[] [5] J. Armstrong, On four-dimensional almost Kähler manifolds, Quart. J. Math. Oxford Ser.(2) 48 (1997), no.192, 405-415.
\item[] [6] J. Armstrong, An ansatz for Almost-Kähler, Einstein 4-manifolds, preprint 1997, to appear in J. reine angew. Math.
\item[] [7] J. Armstrong, Almost Kähler Geometry, Ph.D. Thesis, Oxford (1998).
\item[] [8] W.Barth, C.Peters and A.Van de Ven, Compact complex surfaces, Springer-Verlagh, Berlin Heidelberg New York Tokyo, 1984.
\item[] [9] D. E. Blair, The "total scalar curvature" as a symplectic invariant and related results, Proc. 3rd Congress of Geometry, Thessaloniki (1991), 79-83.
\item[] [10] D. E. Blair and S. Ianus, Critical associated metrics on symplectic manifolds, Contemp. Math. 51 (1986), 23-29.
\item[] [11] R. Bryant, unpublished.
\item[] [12] J.-P. Bourguignon, Les variétés de dimension 4 à signature non nule dont la courbure est harmonique sont d'Einstein, Invent. Math. 63 (1981), 263-286.
\item[] [13] J. Davidov and O. Muškarov, Twistor spaces with Hermitian Ricci tensor, Proc. Amer. Math. Soc. 109 (1990), no. 4, 1115-1120.
\item[] [14] P. Gauduchon, Surfaces kählériennes dont la courbure vérifie certaines conditions de positivité, in Géométrie riemannienne en dimension 4, Séminaire Arthur Besse, 1978/79, eds. Bérard-Bergery, M. Berger, C. Houzel, Cedic/Fernand Nathan, Paris 1981.
\item[] [15] G. Gibbons and S. Hawking, Classification of Gravitational Instanton Symmetries, Comm. Math. Phys. 66 (1979), 291-310.
\item[] [16] S. I. Goldberg, Integrability of almost Kähler manifolds, Proc. Amer. Math. Soc. 21 (1969), 96-100.
\item[] [17] A. Gray, Riemannian manifolds with geodesic symmetries of order 3. J. Differential Geom. 7 (1972), 343-369.
\item[] [18] A. Gray, Curvature identities for Hermitian and almost Hermitian manifolds, Tôhoku Math. J. 28 (1976), 601-612.
\item[] [19] L. Hervella and M. Fernandez, Curvature and charactersitic classes of an almost-Hermtian manifold, Tensor N.S. 31 (1997), 138-140.
\item[] [20] O. Kowalski, Generalized Symmetric Spaces, LNM 805, 1980.
\item[] [21] C.LeBrun, Explicit self-dual metrics on $\mathbb{C P}^{2} \sharp \ldots \sharp \mathbb{C P}^{2}$, J.Differential Geom. 34 (1991), 223-253.
\item[] [22] C.LeBrun, Scalar-flat Kähler metrics on blown-up ruled surfaces, J. reine angew. Math. 420 (1991), 161-177.
\item[] [23] W. Jelonek, On certain four dimensional almost Kähler manifolds, preprint 1999.
\item[] [24] P. Nurowski and M. Przanowski, A four-dimensional example of Ricci flat metric admitting almost Kähler non-Kähler structure, Classical Quantum Gravity 16 (1999), no 3, L9-L13.
\item[] [25] T. Oguro and K. Sekigawa, Four-dimensional almost Kähler Einstein and *-Einstein manifolds, Geom. Dedicata 69 (1998), 91-112.
\item[] [26] K. P. Tod, private communication to the second author.
\end{itemize}
[27] K. Sekigawa, On some compact Einstein almost Kähler manifolds, J. Math. Soc. Japan 36 (1987), 677-684.
[28] F. Tricerri and L. Vanhecke, Curvature tensors on almost Hermitian manifolds, Trans. Amer. Math. Soc. 267 (1981), 365-398.
[29] C.T.C. Wall, Geometric structures on compact complex analytic surfaces, Topology 25 (1986), 119-153.

Vestislav Apostolov, Département de mathématiques, UQAM, succursale Centre-ville c.p. 8888, Montréal, H3C 3P8, Canada
E-mail address: apostolo@math.uqam.ca
John Armstrong, 10, Alan Bullock Close, Oxford 0X4 1AU, UK
E-mail address: John.Armstrong@madge.com
Tedi Drăghici, Department of Mathematics, Florida International University, Miami FL 33199, USA
E-mail address: draghici@fiu.edu
