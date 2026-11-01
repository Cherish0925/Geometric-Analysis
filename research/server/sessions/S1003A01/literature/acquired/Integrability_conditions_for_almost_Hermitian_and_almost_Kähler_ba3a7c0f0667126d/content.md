---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: math_0605611v1.pdf
converter: mathpix
format: mmd
---

\title{
INTEGRABILITY CONDITIONS FOR ALMOST HERMITIAN AND ALMOST KÄHLER 4-MANIFOLDS
}

\author{
K.-D. KIRCHBERG
}
(Version of August 3, 2018)

\begin{abstract}
If $W_{+}$denotes the self dual part of the Weyl tensor of any Kähler 4-manifold and $S$ its scalar curvature, then the relation $\left|W_{+}\right|^{2}=S^{2} / 6$ is well-known. For any almost Kähler 4-manifold with $S \geq 0$, this condition forces the Kähler property. A compact almost Kähler 4-manifold is already Kähler if it satisfies the conditions $\left|W_{+}\right|^{2}=S^{2} / 6$ and $\delta W_{+}=0$ and also if it is Einstein and $\left|W_{+}\right|$is constant. Some further results of this type are proved. An almost Hermitian 4-manifold $(M, g, J)$ with $\operatorname{supp}\left(W_{+}\right)=M$ is already Kähler if it satisfies the condition $\left|W_{+}\right|^{2}=3\left(S_{\star}-S / 3\right)^{2} / 8$ together with $\left|\nabla W_{+}\right|=|\nabla| W_{+}| |$or with $\left.\delta W_{+}+\nabla \log \left|W_{+}\right|\right\lrcorner W_{+}=0$, respectively. The almost complex structure $J$ enters here explicitely via the star scalar curvature $S_{\star}$ only.
\end{abstract}

2002 Mathematics Subject Classification: 53B20, 53C25

\section*{0. Introduction}

This paper is related to the following general question: Which curvature properties of an almost Hermitian (almost Kähler) manifold $(M, g, J)$ imply that $(M, g, J)$ is in fact a Hermitian manifold or a Kähler manifold, respectively? On can also consider the stronger problem which curvature properties of the corresponding oriented Riemannian manifold $(M, g)$ force that $(M, g, J)$ is already Hermitian or Kähler, respectively. By definition, curvature properties of this kind imply the integrability of the almost complex structure $J$ and, hence, are called integrability conditions for almost Hermitian (almost Kähler) manifolds. Here we investigate these problems in dimension 4 and we formulate integrability conditions where the Weyl tensor enters essentially. This was motivated by the fact that the very special form of the self-dual part of the Weyl tensor of a Kähler 4-manifold yields several necessary integrability conditions. Hence, it is very natural to ask which of these conditions are also sufficient. In more detail, for any Kähler 4-manifold $(M, g, J)$ with scalar curvature $S$ and self-dual part $W_{+}: \Lambda_{+}^{2} \rightarrow \Lambda_{+}^{2}$ of the Weyl tensor $W$, the relations
$$\begin{aligned}
\left|W_{+}\right|^{2} & =\frac{S^{2}}{6}, \\
\left(\operatorname{det}\left(W_{+}\right)\right)^{2} & =\frac{1}{54}\left|W_{+}\right|^{6}, \\
\left|\nabla W_{+}\right|^{2} & =\frac{1}{6}|\nabla S|^{2}
\end{aligned}$$
are well-known. From (1) and (3) we obtain the equation
$$\left|\nabla W_{+}\right|=|\nabla| W_{+} \|$$
which is valid on the open subset $M_{+} \subset M$ where $W_{+}$does not vanish. Moreover, one has the equation
$$\left.\delta W_{+}+\nabla \log \left|W_{+}\right|\right\lrcorner W_{+}=0$$
on $M_{+}$. Thus, the Kähler property imposes strong conditions on $W_{+}$. This paper deals with the converse question which curvature conditions already imply the Kähler property of an almost Hermitian 4-manifold $(M, g, J)$ or, more specially, of an almost Kähler 4-manifold.

In the almost Hermitian case, we replace (1) by the basic condition
$$\left|W_{+}\right|^{2}=\frac{3}{8}\left(S_{\star}-\frac{S}{3}\right)^{2}$$
containing the star scalar curvature $S_{\star}$ and being equivalent to (1) if $S_{\star}=S$. If $M_{+}$is dense in $M$ ( $\operatorname{supp}\left(W_{+}\right)=M$ ), we show that (4), (6) and also (5), (6) are sufficient conditions for an almost Hermitian 4-manifold to be Kähler (Theorem 3.1 and Theorem 3.3). Combining the condition
$$\delta W_{+}=0$$
with (6) we obtain that $J$ is integrable on $M_{+}$. Thus, every almost Hermitian 4-manifold $(M, g, J)$ with (6), (7) and $\operatorname{supp}\left(W_{+}\right)=M$ is already Hermitian (Theorem 3.2). In this case, the restriction of $g$ to $M_{+}$is conformally equivalent to a metric $\bar{g}$ on $M_{+}$such that $\left(M_{+}, \bar{g}, J\right)$ is a Kähler manifold. This result is related to a theorem which was published by A. Derdzinski already in 1983 [8]. He considered oriented Riemannian 4-manifolds for which $W_{+}$has at most two eigenvalues at every point and satisfies (7). Then he proved that on $M_{+}$the metric $g$ is conformally equivalent to a metric $\bar{g}$ which is locally Kähler ([6], 16.67). The relation to this result follows from the fact that (6) implies that $W_{+}$has exactly two eigenvalues on $M_{+}$or, equivalently, satisfies the conformally invariant equation (2). A result similar to the mentioned result of Derdzinski is Theorem 3.4 which states that an oriented Riemannian 4-manifold $(M, g)$ with $W_{+} \neq 0$ everywhere is locally Kähler with respect to local complex structures that are compatible with the given orientation if and only if $W_{+}$satisfies the conditions (2) and (4) or (2) and (5), respectively. In Section 4, we finally consider integrability conditions for almost Kähler 4-manifolds. In connection with the conjecture of S.I. Goldberg [11], interesting results in this direction were proved already ([2]-[4], [9], [10], [12], [14-18]). The Goldberg conjecture states that any compact almost Kähler Einstein manifold is in fact Kähler. For non-negative scalar curvature $S$, it was shown by K. Sekigawa [18] that this conjecture is true. For $S<0$, no proof is known so far. There are attempts to construct counterexamples of this part of the Goldberg conjecture ([1], [13]). A result which also uses the assumption $S \geq 0$ is our Theorem 4.1 It states that an almost Kähler 4-manifold with $S \geq 0$ is Kähler if the curvature condition (1) is fulfilled. In the compact case, our basic result is Theorem 4.2 By this theorem, a compact almost Kähler 4-manifold $(M, g, J)$ is Kähler if and only if it satisfies condition (1) together with $Q(J)=0$, where the number $Q(J)$ is an obstruction to the Kähler property for any compact almost Hermitian manifold. $Q(J)$ vanishes, for example, if the Weyl tensor $W$ is harmonic $(\delta W=0)$. An application of Theorem 4.2 is Theorem 4.3 which involves two assertions. The first one states that a compact almost Kähler 4-manifold is Kähler if and only if it satisfies (1) together with
$$\delta W_{+}+\Theta=0,$$
where $\Theta$ is a certain tensor field of type $(2,1)$ depending on $J$ purely algebraically. By the second assertion of Theorem 4.3 a compact almost Kähler 4-manifold is a Kähler manifold of constant scalar curvature if and only if it has the properties (1) and (7). We remark that condition (7) and also condition (8) generalize the Einstein condition. Thus, our Theorem 4.3 is related to the Goldberg conjecture. For example, it yields an improvement of Corollary F in [17] which asserts that any compact almost Kähler Einstein 4-manifold of negative scalar curvature is Kähler if it satisfies (1). The final theorems are also related to the Goldberg conjecture. We show that a compact almost Kähler Einstein 4-manifold is already Kähler if $\left|W_{+}\right|$is constant (Theorem 4.4). Moreover, by Theorem 4.5 a compact almost Kähler 4-manifold with constant negative scalar curvature $S$ is Kähler if it satisfies equation (7) together with the necessary condition
$$\operatorname{det}\left(W_{+}\right)=\frac{S^{3}}{108} .$$

In particular, this implies that a compact almost Kähler Einstein 4-manifold with $S<0$ and (9) is in fact Kähler (Corollary 4.4).

\section*{1. Preliminaries}

Let $(M, g)$ be any Riemannian $n$-manifold. Then, for any endomorphism of the tangent bundle $A: T M \rightarrow T M$, we denote by $A^{*}: T M \rightarrow T M$ the corresponding adjoint endomorphism defined by the characteristic property $g(A X, Y)=g\left(X, A^{*} Y\right)$. The almost Hermitian structure of an almost Hermitian $n$-manifold $(M, g, J)$ is characterized by the basic properties
$$J^{2}=-1 \quad, \quad J^{*}=-J$$
of the almost complex structure $J$ which imply that
$$g(J X, J Y)=g(X, Y)$$
for all vector fields $X, Y$. The fundamental 2-form $\Omega$ is defined by $\Omega(X, Y):=g(J X, Y)$ and the canonical orientation is given by the volume $n$-form $\omega:=\frac{1}{m!} \Omega^{m}(n=2 m)$. As usual, by $\nabla$ we denote the Levi-Civita covariant derivative corresponding to $g$. We use the notation
$$\nabla_{X, Y}^{2}:=\nabla_{X} \circ \nabla_{Y}-\nabla_{\nabla_{X} Y}$$
for the tensorial covariant derivatives of second order such that the Riemannian curvature tensor $R$ is given by $R(X, Y) Z=\nabla_{X, Y}^{2} Z-\nabla_{Y, X}^{2} Z$. In our paper, the Ricci tensor is the endomorphism Ric : $T M \rightarrow T M$ locally defined by $\operatorname{Ric}(X):=R\left(X, X_{k}\right) X^{k}$. Here $\left(X_{1}, \ldots, X_{n}\right)$ denotes a local frame of vector fields and $\left(X^{1}, \ldots, X^{n}\right)$ the associated frame defined by $X^{k}:=g^{k l} \cdot X_{l}(k=1, \ldots, n)$, where $\left(g^{k l}\right)$ is the inverse of the matrix $\left(g_{k l}\right)$ with $g_{k l}:=g\left(X_{k}, X_{l}\right)$. In case of an orthonormal frame, we have $X^{k}=X_{k}(k=1, \ldots, n)$ then. For any almost Hermitian manifold $(M, g, J)$, the star Ricci tensor Ric ${ }_{\star}: T M \rightarrow T M$ is defined by $\operatorname{Ric}_{\star}(X):=R\left(J X, J X_{k}\right) X^{k}$. The first Bianchi identity yields the equation
$$\operatorname{Ric}_{\star}=-\frac{1}{2} R\left(J X_{k}, X^{k}\right) \circ J$$
which implies
$$\left(\operatorname{Ric}_{\star}\right)^{*}=-J \circ \operatorname{Ric}_{\star} \circ J .$$
We also use the notations
$$\begin{aligned}
\operatorname{Ric}^{ \pm} & :=\frac{1}{2}(\operatorname{Ric} \mp J \circ \operatorname{Ric} \circ J), \\
\operatorname{Ric}_{\star}^{ \pm} & :=\frac{1}{2}\left(\operatorname{Ric}_{\star} \pm\left(\operatorname{Ric}_{\star}\right)^{*}\right) .
\end{aligned}$$
By definition, then we have
$$\begin{gathered}
\operatorname{Ric}^{=} \operatorname{Ric}^{+}+\operatorname{Ric}^{-} \quad, \quad \operatorname{Ric}_{\star}=\operatorname{Ric}_{\star}^{+}+\operatorname{Ric}_{\star}^{-}, \\
\left(\operatorname{Ric}^{ \pm}\right)^{*}=\operatorname{Ric}^{ \pm} \quad, \quad\left(\operatorname{Ric}_{\star}^{ \pm}\right)^{*}= \pm \operatorname{Ric}_{\star}^{ \pm} .
\end{gathered}$$
Moreover, the endomorphisms $\operatorname{Ric}^{+}$and $\operatorname{Ric}_{\star}^{+}$(Ric ${ }^{-}$and $\operatorname{Ric}_{\star}^{-}$) commute (anticommute) with $J$, i.e., it holds that
$$\left[\operatorname{Ric}^{+}, J\right]=\left[\operatorname{Ric}_{\star}^{+}, J\right]=\left\{\operatorname{Ric}^{-}, J\right\}=\left\{\operatorname{Ric}_{\star}^{-}, J\right\}=0,$$
where $[A, B]:=A \circ B-B \circ A$ denotes the commutator and $\{A, B\}:=A \circ B+B \circ A$ the anticommutator of endomorphisms $A, B$. The Ricci form $\rho$ and the star Ricci forms $\rho_{\star}, \rho_{\star}^{+}, \rho_{\star}^{-}$are defined by
$$\begin{gathered}
\rho(X, Y):=g\left(\left(\operatorname{Ric}^{+} \circ J\right) X, Y\right) \quad, \quad \rho_{\star}(X, Y):=g\left(\left(\operatorname{Ric}_{\star} \circ J\right) X, Y\right), \\
\rho_{\star}^{ \pm}(X, Y):=g\left(\left(\operatorname{Ric}_{\star}^{ \pm} \circ J\right) X, Y\right) .
\end{gathered}$$

By definition, we have the decomposition
$$\rho_{\star}=\rho_{\star}^{+}+\rho_{\star}^{-} .$$
Moreover, (14) yields
$$\rho(J X, J Y)=\rho(X, Y) \quad, \quad \rho_{\star}^{ \pm}(J X, J Y)= \pm \rho_{\star}^{ \pm}(X, Y) .$$
Besides the scalar curvature $S:=\operatorname{tr}(\operatorname{Ric})=\operatorname{tr}\left(\operatorname{Ric}^{+}\right)$we also consider the star scalar curvature $S_{\star}:=\operatorname{tr}\left(\operatorname{Ric}_{\star}\right)=\operatorname{tr}\left(\operatorname{Ric}_{\star}^{+}\right)$. The tensor field $\tilde{R}$ defined by
$$\tilde{R}(X, Y):=\frac{1}{4}[R(X, Y)-R(J X, J Y), J] \circ J$$
has the properties
$$\begin{gathered}
\tilde{R}(X, Y)^{*}=-\tilde{R}(X, Y)=\tilde{R}(Y, X), \\
\tilde{R}(J X, J Y)=-\tilde{R}(X, Y), \\
\{\tilde{R}(X, Y), J\}=0 .
\end{gathered}$$
Furthermore, we use the decomposition
$$\tilde{R}(X, Y)=\tilde{R}^{+}(X, Y)+\tilde{R}^{-}(X, Y)$$
with $\tilde{R}^{ \pm}(X, Y):=\frac{1}{2}(\tilde{R}(X, Y) \pm \tilde{R}(J X, Y) \circ J)$. Then $\tilde{R}^{+}$and $\tilde{R}^{-}$have the additional properties
$$\tilde{R}^{ \pm}(J X, Y) \circ J= \pm \tilde{R}^{ \pm}(X, Y) .$$
It is well-known that $\tilde{R}^{-}$is already determined by the Weyl tensor $W$, i.e., we have
$$\tilde{R}^{-}(X, Y)=\tilde{W}^{-}(X, Y) .$$
We introduce the curvature endomorphism $\widetilde{\operatorname{Ric}}$ defined by $\widetilde{\operatorname{Ric}}(X):=\tilde{R}\left(X, X_{k}\right) X^{k}$ and the function $\tilde{S}:=\operatorname{tr}(\widetilde{\text { Ric }})$. A direct calculation yields the identity
$$\widetilde{\operatorname{Ric}}=\frac{1}{2}\left(\mathrm{Ric}_{\star}^{+}-\mathrm{Ric}^{+}\right)$$
implying
$$\begin{gathered}
\tilde{S}=\frac{1}{2}\left(S_{\star}-S\right), \\
(\widetilde{\mathrm{Ric}})^{*}=\widetilde{\mathrm{Ric}} \quad, \quad[\widetilde{\mathrm{Ric}}, J]=0 .
\end{gathered}$$
For any skew symmetric endomorphism $A: T M \rightarrow T M\left(A^{*}=-A\right)$ we define skew symmetric endomorphisms $R(A), \tilde{R}(A), W(A)$ by $R(A):=R\left(A X_{k}, X^{k}\right), \tilde{R}(A):=\tilde{R}\left(A X_{k}, X^{k}\right)$ and $W(A):=$ $W\left(A X_{k}, X^{k}\right)$. Then, the equations
$$R(A)=W(A)+\frac{2}{n-2}\left(\{\text { Ric }, A\}-\frac{S}{n-1} A\right),$$
$$\begin{gathered}
\tilde{R}(A)=\frac{1}{4}[R(A)+R(J \circ A \circ J), J] \circ J, \\
\{\tilde{R}(A), J\}=0, \\
\tilde{R}(J \circ A \circ J)=\tilde{R}(A)
\end{gathered}$$
are valid for all skew symmetric endomorphisms $A$. We remark, that usually $R, \tilde{R}$ and $W$ are considered as endomorphisms of the bundle $\Lambda^{2}:=\Lambda^{2} T^{*} M$. But here we use the canonical isomorphism between skew symmetric endomorphisms and 2-forms given by
$$\Omega_{A}(X, Y)=g(A X, Y),$$
where $\Omega_{A}$ denotes the 2-form corresponding to the skew symmetric endomorphism $A$. For example, we have $\Omega=\Omega_{J}$ then and $W\left(\Omega_{A}\right)$ and $W(A)$ are related by
$$W\left(\Omega_{A}\right)(X, Y)=g(W(A) X, Y) .$$

Using (10) and (17) we obtain
$$W(J)=\frac{2 S}{(n-1)(n-2)} J+2\left(\text { Ric }_{\star}-\text { Ric }^{+}\right) \circ J+\frac{n-4}{n-2}\{\text { Ric }, J\} .$$
In the following, for any endomorphisms $A, B: T M \rightarrow T M$, we use the scalar product $\langle A, B\rangle$ defined by
$$\langle A, B\rangle=\frac{1}{n} \operatorname{tr}\left(A^{*} \circ B\right)=\frac{1}{n} g\left(A X_{k}, B X^{k}\right)$$
which differs from the usual one by the dimension factor $1 / n$. According to (19) we define the scalar product of 2-forms such that
$$\left\langle\Omega_{A}, \Omega_{B}\right\rangle=\langle A, B\rangle .$$
Now, let us consider the almost Kähler case. An almost Kähler manifold is an almost Hermitian manifold ( $M, g, J$ ) with closed fundamental 2-form $\Omega=\Omega_{J}$, i.e., with
$$d \Omega=0 .$$
It is well-known, that
$$\delta \Omega=0$$
follows, i.e., $\Omega$ is also co-closed then. Furthermore, the almost complex structure $J$ of any almost Kähler manifold satisfies the so-called quasi Kähler condition
$$\nabla_{J X} J=\nabla_{X} J \circ J .$$
In the almost Kähler case, the tensor $\widetilde{\text { Ric }}$ has the special form ([12], eq. (41))
$$\widetilde{\mathrm{Ric}}=-\frac{1}{4} \nabla_{X_{k}} J \circ \nabla_{X^{k}} J .$$
This implies $\widetilde{\text { Ric }} \geq 0$ and, moreover,
$$\tilde{S}=\frac{n}{4}|\nabla J|^{2},$$
where, according to the definition of the scalar product above, the function $|\nabla J|^{2}$ is locally given by
$$|\nabla J|^{2}=\left\langle\nabla_{X_{k}} J, \nabla_{X^{k}} J\right\rangle=-\frac{1}{n} \operatorname{tr}\left(\nabla_{X_{k}} J \circ \nabla_{X^{k}} J\right) .$$
By (16) and (21), we have
$$S_{\star}-S=\frac{n}{2}|\nabla J|^{2}$$
in the almost Kähler case.

\section*{2. The Weyl tensor of an almost Hermitian 4-manifold.}

For any oriented Riemannian 4-manifold $(M, g)$, the Hodge operator $*$ acts as an involution on the bundle $\Lambda^{2}:=\Lambda^{2} T^{*} M$. This yields the orthogonal splitting
$$\Lambda^{2}=\Lambda_{+}^{2} \oplus \Lambda_{-}^{2}$$
with rank $\left(\Lambda_{ \pm}^{2}\right)=3$, where $\Lambda_{+}^{2}\left(\Lambda_{-}^{2}\right)$ denotes the eigen-subbundle of this involution to the eigenvalue 1 (-1). We use the notations $P_{+}$and $P_{-}$for the corresponding bundle projections $\left(P_{ \pm}\left(\Lambda^{2}\right)=\Lambda_{ \pm}^{2}\right)$. Since the Weyl tensor $W$ considered as an endomorphism of $\Lambda^{2}$ commutes with $P_{ \pm}, W$ decomposes in the form $W=W_{+} \oplus W_{-}$, where $W_{+}: \Lambda_{+}^{2} \rightarrow \Lambda_{+}^{2}\left(W_{-}: \Lambda_{-}^{2} \rightarrow \Lambda_{-}^{2}\right)$ is called the self-dual (anti-self-dual) part of $W . W_{+}$and $W_{-}$are self-adjoint and traceless endomorphisms. We summarize some well-known basic facts concerning this splitting in the following lemma (see [5]).

Lemma 2.1.
(i) For any section $\Omega_{A}$ of $\Lambda_{+}^{2}$ and any section $\Omega_{B}$ of $\Lambda_{-}^{2}, A$ and $B$ commute ( $[A, B]=0$ ).
(ii) If $\Omega_{J} \in \Gamma\left(\Lambda_{+}^{2}\right)\left(\Omega_{J} \in \Gamma\left(\Lambda_{-}^{2}\right)\right)$ is any unit section $\left(\left|\Omega_{J}\right|=1\right)$, then $(M, g, J)$ is an almost Hermitian manifold and we have $\frac{1}{2} \Omega_{J} \wedge \Omega_{J}=\omega\left(\frac{1}{2} \Omega_{J} \wedge \Omega_{J}=-\omega\right)$, where $\omega$ is the volume 4-form defined by the metric $g$ and the given orientation.
(iii) $\Lambda_{+}^{2}$ and $\Lambda_{-}^{2}$ are endowed with a canonical orientation, where a local orthonormal frame $\left(\Omega_{I}, \Omega_{J}, \Omega_{K}\right)$ of $\Lambda_{+}^{2}$ or $\Lambda_{-}^{2}$, respectively, is positively oriented if and only if the corresponding frame $(I, J, K)$ satisfies the quaternionic relations $I^{2}=J^{2}=K^{2}=-1, I \circ J \circ K=-1$.

We now consider an almost Hermitian 4-manifold $(M, g, J)$ endowed with the orientation given by $J$. Then the corresponding fundamental 2-form $\Omega=\Omega_{J}$ satisfies the equation $* \Omega=\Omega$ implying $\Omega \in \Gamma\left(\Lambda_{+}^{2}\right)$. Thus, we obtain the orthogonal splitting
$$\Lambda_{+}^{2}=\mathbb{R} \cdot \Omega \oplus P_{+}\left(\Omega^{\perp}\right) .$$
Let $x \in M$ be any point and let $\left(X_{1}, \ldots, X_{4}\right)$ be any orthonormal frame of vector fields in a neighborhood $U$ of $x$ with the property
$$J X_{1}=X_{2} \quad, \quad J X_{2}=-X_{1} \quad, \quad J X_{3}=X_{4} \quad, \quad J X_{4}=-X_{3} .$$
Such a frame is called a $J$-frame. We consider the endomorphisms $I, K$ on $U$ defined by
$$\begin{aligned}
& I X_{1}=X_{3} \quad, \quad I X_{2}=-X_{4} \quad, \quad I X_{3}=-X_{1} \quad, \quad I X_{4}=X_{2} \quad, \\
& K X_{1}=-X_{4} \quad, \quad K X_{2}=-X_{3} \quad, \quad K X_{3}=X_{2} \quad, \quad K X_{4}=X_{1} .
\end{aligned}$$
Then, by definition, we have
$$I^{*}=-I \quad, \quad K^{*}=-K$$
and the quaternionic relations
$$I^{2}=J^{2}=K^{2}=-1 \quad, \quad I \circ J \circ K=-1$$
are satisfied. In the following, such a pair of endomorphisms $(I, K)$ is called a local quaternionic supplement of $J$. Moreover, it holds that
$$\begin{gathered}
|I|^{2}=|J|^{2}=|K|^{2}=1 \quad, \quad\langle I, J\rangle=\langle I, K\rangle=\langle J, K\rangle=0, \\
* \Omega_{I}=\Omega_{I} \quad, \quad * \Omega_{K}=\Omega_{K} .
\end{gathered}$$
Thus, every triple $\left(\Omega, \Omega_{I}, \Omega_{K}\right)$ is a (negatively oriented) local orthonormal frame of $\Lambda_{+}^{2}$, where $\left(\Omega_{I}, \Omega_{K}\right)$ is a frame of $P_{+}\left(\Omega^{\perp}\right)$. Furthermore, two quaternionic supplements $(I, K)$ and $\left(I^{\prime}, K^{\prime}\right)$ of $J$ on a sufficiently small open neighborhood $U$ are related by
$$I^{\prime}=\cos \alpha \cdot I-\sin \alpha \cdot K \quad, \quad K^{\prime}=\sin \alpha \cdot I+\cos \alpha \cdot K$$
with a function $\alpha$ on $U$.

For any local quaternionic supplement $(I, K)$ of $J$, we introduce the local endomorphisms $\operatorname{Ric}_{\triangle}$ and Ric ${ }_{\square}$ defined by
$$\operatorname{Ric}_{\triangle}(X):=\operatorname{Ric}\left(I X, I X_{k}\right) X^{k} \quad, \quad \operatorname{Ric}_{\square}(X):=\operatorname{Ric}\left(K X, K X_{k}\right) X^{k} .$$
By definition, Ric $\triangle$ and Ric □ are the star Ricci tensors corresponding to the local almost Hermitian structures ( $g, I$ ) and ( $g, K$ ), respectively.

Lemma 2.2. For every local quaternionic supplement $(I, K)$ of $J$, we have the relation
$$\operatorname{Ric}_{\triangle}+\operatorname{Ric}_{\square}+\operatorname{Ric}_{\star}=\operatorname{Ric}_{.}$$

Proof. Let $\left(X_{1}, \ldots, X_{4}\right)$ be the $J$-frame according to which $(I, K)$ is defined. Using the first Bianchi identity we calculate
$$\begin{aligned}
\operatorname{Ric}_{\triangle}\left(X_{1}\right) & =R\left(I X_{1}, I X_{2}\right) X_{2}+R\left(I X_{1}, I X_{3}\right) X_{3}+R\left(I X_{1}, I X_{4}\right) X_{4}= \\
& =R\left(X_{3},-X_{4}\right) X_{2}+R\left(X_{3},-X_{1}\right) X_{3}+R\left(X_{3}, X_{2}\right) X_{4}= \\
& =R\left(X_{1}, X_{3}\right) X_{3}+R\left(X_{4}, X_{2}\right) X_{3} .
\end{aligned}$$
In this way, we obtain the images $\operatorname{Ric}_{\triangle}\left(X_{k}\right), \operatorname{Ric}_{\square}\left(X_{k}\right)$ and $\operatorname{Ric}_{\star}\left(X_{k}\right)$ for $k=1, \ldots, 4$. Then, we find
$$\operatorname{Ric}_{\triangle}\left(X_{k}\right)+\operatorname{Ric}_{\square}\left(X_{k}\right)+\operatorname{Ric}_{\star}\left(X_{k}\right)=\operatorname{Ric}\left(X_{k}\right) \quad(k=1, \ldots, 4) .$$ \(\square\)

According to (12) we have the decompositions
$$\operatorname{Ric}_{\triangle}=\operatorname{Ric}_{\triangle}^{+}+\operatorname{Ric}_{\triangle}^{-} \quad, \quad \operatorname{Ric}_{\square}=\operatorname{Ric}_{\square}^{+}+\operatorname{Ric}_{\square}^{-}$$
with the properties corresponding to (13) and (14), respectively. Hence, Taking the symmetric and the skew symmetric part of (24) we see that (24) is equivalent to the two equations
$$\operatorname{Ric}_{\triangle}^{+}+\operatorname{Ric}_{\square}^{+}+\operatorname{Ric}_{\star}^{+}=\operatorname{Ric},$$
$$\operatorname{Ric}_{\triangle}^{-}+\operatorname{Ric}_{\square}^{-}+\operatorname{Ric}_{\star}^{-}=0 .$$
Moreover, with $S_{\triangle}:=\operatorname{tr}\left(\operatorname{Ric}_{\triangle}\right)$ and $S_{\square}:=\operatorname{tr}\left(\operatorname{Ric}_{\square}\right)$ from (24) we obtain
$$S_{\triangle}+S_{\square}+S_{\star}=S .$$
Since, the endomorphism $\widetilde{\text { Ric }}$ is a multiple of the identity for any almost Hermitian 4-manifold ([17], (2.3.1)), from (15), (16) we obtain here
$$\widetilde{\operatorname{Ric}}=\frac{\tilde{S}}{4}=\frac{1}{8}\left(S_{\star}-S\right)=\frac{1}{2}\left(\mathrm{Ric}_{\star}^{+}-\mathrm{Ric}^{+}\right) .$$
For $n=4$, (20) can thus be written in the form
$$W(J)=\frac{1}{2}\left(S_{\star}-\frac{S}{3}\right) J+2 \mathrm{Ric}_{\star}^{-} \circ J .$$
Hence, for any local quaternionic supplement $(I, K)$ of $J$, we have quite analogously
$$\begin{aligned}
W(I) & =\frac{1}{2}\left(S_{\triangle}-\frac{S}{3}\right) I+2 \operatorname{Ric}_{\triangle}^{-} \circ I, \\
W(K) & =\frac{1}{2}\left(S_{\square}-\frac{S}{3}\right) K+2 \operatorname{Ric}_{\square}^{-} \circ K,
\end{aligned}$$
We remark that, using the correspondence (19) between skew symmetric endomorphisms and 2-forms, the equations (28)-(30) can equivalently be stated
$$\begin{aligned}
W_{+}(\Omega) & =\frac{1}{2}\left(S_{\star}-\frac{S}{3}\right) \Omega+2 \rho_{\star}^{-}, \\
W_{+}\left(\Omega_{I}\right) & =\frac{1}{2}\left(S_{\triangle}-\frac{S}{3}\right) \Omega_{I}+2 \rho_{\triangle}^{-}, \\
W_{+}\left(\Omega_{K}\right) & =\frac{1}{2}\left(S_{\square}-\frac{S}{3}\right) \Omega_{K}+2 \rho_{\square}^{-} .
\end{aligned}$$
Using (27) the equations (31)-(33) yield
$$\left|W_{+}\right|^{2}=\frac{1}{4}\left(S_{\star}^{2}+S_{\triangle}^{2}+S_{\square}^{2}-\frac{S^{2}}{3}\right)+4\left(\left|\operatorname{Ric}_{\star}^{-}\right|^{2}+\left|\operatorname{Ric}_{\triangle}^{-}\right|^{2}+\left|\operatorname{Ric}_{\square}^{-}\right|^{2}\right) .$$

Applying (10) in the case where $J$ is replaced by $I$ or $K$, respectively, (18) yields the equations
$$\begin{aligned}
\tilde{R}(I) & =-\operatorname{Ric}_{\triangle} \circ I-J \circ \operatorname{Ric}_{\triangle} \circ K, \\
\tilde{R}(K) & =-\operatorname{Ric}_{\square} \circ K-J \circ \operatorname{Ric}_{\square} \circ I .
\end{aligned}$$
This shows that $\{\tilde{R}(I), J\}=\{\tilde{R}(K), J\}=0$. Hence, $\tilde{R}(I)$ and $\tilde{R}(K)$ correspond to local sections of $P_{+}\left(\Omega^{\perp}\right)$ implying that these endomorphisms are linear combinations of $I$ and $K$. Thus, using (26) from (35), (36) we obtain
$$\begin{aligned}
\tilde{R}(I) & =-\frac{1}{2} S_{\triangle} \cdot I+2\left\langle J, \operatorname{Ric}_{\triangle}^{-}\right\rangle K, \\
\tilde{R}(K) & =-\frac{1}{2} S_{\square} \cdot K+2\left\langle J, \operatorname{Ric}_{\triangle}^{-}\right\rangle I .
\end{aligned}$$
Since $\mathrm{Ric}_{\star}^{-}, \mathrm{Ric}_{\triangle}^{-}$and $\mathrm{Ric}_{\square}^{-}$are skew symmetric and, moreover, it holds that (compare (14))
$$\left\{\operatorname{Ric}_{\star}^{-}, J\right\}=\left\{\operatorname{Ric}_{\triangle}^{-}, I\right\}=\left\{\operatorname{Ric}_{\square}^{-}, K\right\}=0,$$
analogous considerations using (26) yield the equations
$$\begin{aligned}
\operatorname{Ric}_{\star}^{-} & =\left\langle I, \operatorname{Ric}_{\star}^{-}\right\rangle I+\left\langle K, \operatorname{Ric}_{\star}^{-}\right\rangle K, \\
\operatorname{Ric}_{\triangle}^{-} & =\left\langle J, \operatorname{Ric}_{\triangle}^{-}\right\rangle J-\left\langle K, \operatorname{Ric}_{\star}^{-}\right\rangle K, \\
\operatorname{Ric}_{\square}^{-} & =-\left\langle I, \operatorname{Ric}_{\star}^{-}\right\rangle I-\left\langle J, \operatorname{Ric}_{\triangle}^{-}\right\rangle J,
\end{aligned}$$
and, hence, the local relation
$$\left|\operatorname{Ric}_{\triangle}^{-}\right|^{2}+\left|\operatorname{Ric}_{\square}^{-}\right|^{2}-\left|\operatorname{Ric}_{\star}^{-}\right|^{2}=2\left\langle J, \operatorname{Ric}_{\triangle}^{-}\right\rangle^{2} .$$
Equation (18) shows that $\tilde{R}(A)=0$ for all $A$ with $[A, J]=0$. Thus, locally we have
$$|\tilde{R}|^{2}=|\tilde{R}(I)|^{2}+|\tilde{R}(K)|^{2} .$$
By (37), (38), (40), we find
$$|\tilde{R}|^{2}=\frac{1}{4}\left(S_{\triangle}^{2}+S_{\square}^{2}\right)+4\left(\left|\operatorname{Ric}_{\triangle}^{-}\right|^{2}+\left|\operatorname{Ric}_{\square}^{-}\right|^{2}-\left|\operatorname{Ric}_{\star}^{-}\right|^{2}\right) .$$
By definition of $\tilde{R}^{-}$, we have generally
$$\tilde{R}^{-}(A)=\frac{1}{2}(\tilde{R}(A)-\tilde{R}(J A) \circ J) .$$
Using (37), (38), we particularly obtain
$$\begin{aligned}
\tilde{R}^{-}(I) & =\frac{1}{4}\left(S_{\square}-S_{\triangle}\right) I+2\left\langle J, \operatorname{Ric}_{\triangle}^{-}\right\rangle K, \\
\tilde{R}^{-}(K) & =-\frac{1}{4}\left(S_{\square}-S_{\triangle}\right) K+2\left\langle J, \operatorname{Ric}_{\triangle}^{-}\right\rangle I,
\end{aligned}$$
With (39) this yields analogously
$$\left|\tilde{R}^{-}\right|^{2}=\frac{1}{8}\left(S_{\triangle}-S_{\square}\right)^{2}+4\left(\left|\operatorname{Ric}_{\triangle}^{-}\right|^{2}+\left|\operatorname{Ric}_{\square}^{-}\right|^{2}-\left|\operatorname{Ric}_{\star}^{-}\right|^{2}\right) .$$
Since the decomposition $\tilde{R}=\tilde{R}^{+}+\tilde{R}^{-}$is orthogonal, we have
$$|\tilde{R}|^{2}=\left|\tilde{R}^{+}\right|^{2}+\left|\tilde{R}^{-}\right|^{2}$$
implying the equation
$$\left|\tilde{R}^{+}\right|^{2}=\frac{1}{8}\left(S_{\star}-S\right)^{2}$$
by (27), (41) and (42). Using (27), (34) and (42) we immediately obtain the following assertion.

Lemma 2.3. For any almost Hermitian 4-manifold, the equation
$$\left.\left|W_{+}\right|^{2}=\frac{3}{8}\left(S_{\star}-\frac{S}{3}\right)^{2}+8 \right\rvert\, \text { Ric }\left._{\star}^{-}\right|^{2}+\left|\tilde{R}^{-}\right|^{2}$$
is valid.
We denote by $P_{1}, P_{2}: \Lambda_{+}^{2} \rightarrow \Lambda_{+}^{2}$ the projection corresponding to the splitting (23) with $P_{1}\left(\Lambda_{+}^{2}\right)=$ $\mathbb{R} \cdot \Omega$ and $P_{2}\left(\Lambda_{+}^{2}\right)=P_{+}\left(\Omega^{\perp}\right)$. Moreover, we shall use the notations
$$\lambda:=\frac{1}{4}\left(S_{\star}-\frac{S}{3}\right) \quad, \quad F:=\lambda\left(2 P_{1}-P_{2}\right) \quad, \quad G:=W_{+}-F .$$

Lemma 2.4. The equation
$$\left|W_{+}\right|^{2}=6 \lambda^{2}+|G|^{2}$$
holds for any almost Hermitian 4-manifold $(M, g, J)$.
Proof. Let $(I, K)$ be any local quaternionic supplement of $J$ and let $\left(\Omega^{J}, \Omega^{I}, \Omega^{K}\right)$ be the coframe of the negatively oriented frame $\left(\Omega_{J}, \Omega_{I}, \Omega_{K}\right)$ of $\Lambda_{+}^{2}$. Using the local representations
$$P_{1}=\Omega^{J} \otimes \Omega_{J} \quad, \quad P_{2}=\Omega^{I} \otimes \Omega_{I}+\Omega^{K} \otimes \Omega_{K}$$
we calculate
$$\begin{gathered}
\left\langle W_{+}, P_{1}\right\rangle=\operatorname{tr}\left(W_{+} \circ P_{1}\right)=\operatorname{tr}\left(W_{+} \circ\left(\Omega^{J} \otimes \Omega_{J}\right)\right)= \\
\operatorname{tr}\left(\Omega^{J} \otimes W_{+}\left(\Omega_{J}\right)\right)=\Omega^{J}\left(W_{+}\left(\Omega_{J}\right)\right) \stackrel{(31)}{=} \frac{1}{2}\left(S_{\star}-\frac{S}{3}\right)=2 \lambda
\end{gathered}$$
and, furthermore,
$$\begin{aligned}
& \left\langle W_{+}, P_{2}\right\rangle=\Omega^{I}\left(W_{+}\left(\Omega_{I}\right)\right)+\Omega^{K}\left(W_{+}\left(\Omega_{K}\right)\right) \stackrel{(32),(33)}{=} \\
& \frac{1}{2}\left(S_{\triangle}-\frac{S}{3}\right)+\frac{1}{2}\left(S_{\square}-\frac{S}{3}\right) \stackrel{(27)}{=}-\frac{1}{2}\left(S_{\star}-\frac{S}{3}\right)=-2 \lambda .
\end{aligned}$$
Thus, we obtain
$$\left\langle W_{+}, P_{1}\right\rangle=2 \lambda=-\left\langle W_{+}, P_{2}\right\rangle .$$
Finally, we have
$$\begin{aligned}
& |G|^{2}=\left\langle W_{+}-F, W_{+}-F\right\rangle=\left|W_{+}\right|^{2}-2\left\langle W_{+}, F\right\rangle+|F|^{2}= \\
& \left|W_{+}\right|^{2}-2 \lambda\left(2\left\langle W_{+}, P_{1}\right\rangle-\left\langle W_{+}, P_{2}\right\rangle\right)+|F|^{2} \stackrel{\text { (47) }}{=} \\
& \left|W_{+}\right|^{2}-12 \lambda^{2}+|F|^{2}=\left|W_{+}\right|^{2}-12 \lambda^{2}+6 \lambda^{2}=\left|W_{+}\right|^{2}-6 \lambda^{2} .
\end{aligned}$$ \(\square\)

Proposition 2.1. For any almost Hermitian 4-manifold, the following assertions are equivalent:
\begin{itemize}
\item[(i)] The characteristic polynomial of the self-dual part $W_{+}$of the Weyl tensor has the form
$$\chi(t)=(t-2 \lambda)(t+\lambda)^{2} .$$
\item[(ii)] The equation
$$\left|W_{+}\right|^{2}=6 \lambda^{2}$$
\end{itemize}
is satisfied.
\begin{itemize}
\item[(iii)] $W_{+}$is given by
\end{itemize}
$$W_{+}=\lambda \cdot\left(2 P_{1}-P_{2}\right) .$$
\begin{itemize}
\item[(iv)] The vanishing conditions
$$\operatorname{Ric}_{\star}^{-}=0 \quad, \quad \tilde{R}^{-}=0$$
\end{itemize}
are fulfilled.

Proof. By Lemma 2.3 and Lemma 2.4 the equivalence of the assertions (ii) - (iv) are obvious. Furthermore, (iii) implies (i) and (i) implies (ii). \(\square\)

An immediate consequence of this proposition is the following assertion.
Corollary 2.1. For any almost Hermitian 4-manifold, condition (48) implies the conformally invariant property
$$\left(\operatorname{det}\left(W_{+}\right)\right)^{2}=\frac{1}{54}\left|W_{+}\right|^{6}$$
of the self-dual part $W_{+}$of the Weyl tensor.
It is well-known that, for any oriented Riemannian 4-manifold $(M, g)$, the characteristic polynomial of $W_{+}$is given by
$$\chi(t)=t^{3}-\frac{1}{2}\left|W_{+}\right|^{2} \cdot t-\operatorname{det}\left(W_{+}\right) .$$
Thus, (50) is equivalent to the fact that $W_{+}: \Lambda_{+}^{2} \rightarrow \Lambda_{+}^{2}$ has exactly two eigenvalues on the subset $M_{+} \subseteq M$ on which $W_{+}$does not vanish, i.e., at most two eigenvalues at every point of $M$.

We finish this section by a proposition summarizing some well-known facts concerning Kähler 4-manifolds ([7], XII).

Proposition 2.2. Let $(M, g, J)$ be any Kähler 4-manifold with scalar curvature $S$ and self-dual part $W_{+}$of its Weyl tensor and let $M_{+} \subseteq M$ denote the subset on which $W_{+}$does not vanish. Then the following assertions are valid:
(i) The equations
$$\left|W_{+}\right|^{2}=\frac{S^{2}}{6},$$
$$\operatorname{det}\left(W_{+}\right)=\frac{S^{3}}{108}$$
are satisfied and, hence, also equation (50). Moreover, the characteristic polynomial of $W_{+}$has the form
$$\chi(t)=\left(t-\frac{S}{3}\right)\left(t+\frac{S}{6}\right)^{2} .$$
(ii) $W_{+}$is given by
$$W_{+}=\frac{S}{6}\left(2 P_{1}-P_{2}\right)$$
and it holds that
$$\nabla W_{+}=\frac{1}{6} d S \otimes\left(2 P_{1}-P_{2}\right),$$
$$\left|\nabla W_{+}\right|^{2}=\frac{1}{6}|\nabla S|^{2} .$$
(iii) On $M_{+}$we have the equation
$$\left|\nabla W_{+}\right|^{2}=|\nabla| W_{+}| |^{2} .$$

Proof. On any Kähler manifold, Ric ${ }_{\star}=$ Ric and hence $S_{\star}=S$, Ric $_{\star}^{-}=0$. Moreover, in the Kähler case, we have $\tilde{R}=0$. Hence, (45) becomes (51). (46), (51) and $S_{\star}=S$ imply $G=0$ and hence equation (54). This equation immediately yields (52) and (53). Moreover, by $P_{1}+P_{2}=P_{+}, \nabla P_{+}=$ 0 and $\nabla J=0$, we have
$$\nabla P_{1}=0 \quad, \quad \nabla P_{2}=0 .$$

Using (58) we obtain (55) from (54). (55) implies (56). Finally, we find (57) using (51) and (56). \(\square\)

\section*{3. Integrability conditions for almost Hermitian 4-manifolds.}

In the following $M_{+}$always denotes the open subset of $M$ on which $W_{+}$does not vanish. Further on we use the notation $\lambda:=\frac{1}{4}\left(S_{\star}-\frac{S}{3}\right)$.

Lemma 3.1. For any almost Hermitian 4-manifold $(M, g, J)$, equation (48) implies the equation
$$\left|\nabla W_{+}\right|^{2}=|\nabla| W_{+}| |^{2}+\frac{3}{2}\left|W_{+}\right|^{2} \cdot\left|\nabla P_{1}\right|^{2}$$
on the subset $M_{+} \subseteq M$.
Proof. By Proposition 2.1 (48) is equivalent to (49). Using $P_{1}+P_{2}=P_{+}$equation (49) becomes
$$W_{+}=\lambda\left(3 P_{1}-P_{+}\right) .$$
Since $P_{+}$is parallel, applying $\nabla_{X}$ to this equation we obtain
$$\nabla_{X} W_{+}=X(\lambda) \cdot\left(3 P_{1}-P_{+}\right)+3 \lambda \nabla_{X} P_{1}$$
for any vector field $X$. Moreover, on $M_{+}$, (48) yields
$$|\nabla| W_{+}| |^{2}=6|\nabla \lambda|^{2} .$$
The equations $\left\langle P_{1}, P_{1}\right\rangle=\left\langle P_{+}, P_{1}\right\rangle=1, \nabla P_{+}=0$ imply
$$\left\langle P_{1}, \nabla_{X} P_{1}\right\rangle=\left\langle P_{+}, \nabla_{X} P_{1}\right\rangle=0 .$$
Finally, we calculate
$$\begin{gathered}
\left|\nabla W_{+}\right|^{2}=\left\langle\nabla_{X} W_{+}, \nabla_{X^{k}} W_{+}\right\rangle=\operatorname{tr}\left(\nabla_{X_{k}} W_{+} \circ \nabla_{X^{k}} W_{+}\right) \stackrel{(59)}{=} \\
6|\nabla \lambda|^{2}+6 \lambda\left\langle 3 P_{1}-P_{+}, \nabla_{\nabla \lambda} P_{1}\right\rangle+9 \lambda^{2}\left|\nabla P_{1}\right|^{2} \text { (48), (60), (61) } \\
|\nabla| W_{+}| |^{2}+\frac{3}{2}\left|W_{+}\right|^{2} \cdot\left|\nabla P_{1}\right|^{2} .
\end{gathered}$$ \(\square\)

Theorem 3.1. Let $(M, g, J)$ be any almost Hermitian 4-manifold such that $M_{+}$is dense in $M$. Then, $(M, g, J)$ is Kähler if and only if the equation (48) is satisfied on $M$ and, moreover, equation (57) on $M_{+}$.

Proof. By Lemma 3.1 (57) implies $\nabla P_{1}=0$ on $M_{+}$and, hence, on $M$ since $M_{+}$is dense in $M$. On any section $\Omega_{A}$ of $\Lambda_{+}^{2}, P_{1}$ acts by $P_{1}\left(\Omega_{A}\right)=\langle J, A\rangle \Omega_{J}$. Hence, $\nabla P_{1}=0$ is equivalent to $\nabla J=0$. Conversely, in the Kähler case, Proposition 2.2 shows that we have (48) and (57) then. \(\square\)

An immediate consequence of this theorem is the following assertion.
Corollary 3.1. An almost Hermitian 4-manifold $(M, g, J)$ with $\operatorname{supp}\left(W_{+}\right)=M$ is Kähler if and only if the equations $S_{\star}=S,\left|W_{+}\right|^{2}=S^{2} / 6$ are valid and on $M_{+}$the equation $\left|\nabla W_{+}\right|=|\nabla| W_{+}| |$.

We remark that the almost complex structure $J$ enters the integrability conditions of Theorem 3.1 or Corollary 3.1 respectively, only via $S_{\star}$. In particular, these conditions do not contain any derivatives of $J$.

In the following we combine the basic condition (48) of this section with the divergence condition
$$\delta W_{+}=0$$
and also with the condition
$$\left.\delta W_{+}+\nabla \log \left|W_{+}\right|\right\lrcorner W_{+}=0$$
on $M_{+}$. The proof of Theorem 3.3 shows that the last equation is satisfied on every Kähler 4-manifold.

We recall that $\delta W$ is an endomorphism valued 1-form (tensor field of type $(2,1)$ ) locally defined by $\delta W(X):=\left(\nabla_{X_{k}} W\right)\left(X, X^{k}\right)$. Moreover, for any vector field $X \in \Gamma(T M)$, by $\left.X\right\lrcorner W$ we denote the endomorphism valued 1-form given by $(X\lrcorner W)(Y):=W(X, Y)$. Using the identification introduced in section 1 we have the relation $W(X, Y)=\frac{1}{2} W(g(Y) \otimes X-g(X) \otimes Y)$, where the skew symmetric endomorphism $g(Y) \otimes X-g(X) \otimes Y$ acts by $(g(Y) \otimes X-g(X) \otimes Y)(Z):=g(Y, Z) X-g(X, Z) Y$. Locally we obtain
$$\delta W(X)=\frac{1}{2}\left(\nabla_{X_{k}} W\right)\left(\xi^{k} \otimes X-g(X) \otimes X^{k}\right),$$
where $\left(\xi^{1}, \ldots, \xi^{n}\right)$ is the coframe corresponding to the local frame $\left(X_{1}, \ldots, X_{n}\right)$. For any oriented Riemannian 4-manifold $(M, g)$, the decomposition $W=W_{+} \oplus W_{-}$implies the decomposition
$$\delta W=\delta W_{+} \oplus \delta W_{-},$$
where $\delta W_{+}$and $\delta W_{-}$are locally given by
$$\delta W_{ \pm}(X)=\frac{1}{2}\left(\nabla_{X_{k}} W_{ \pm}\right)\left(\xi^{k} \otimes X-g(X) \otimes X^{k}\right) .$$

Lemma 3.2. Let $(M, g, J)$ be an almost Hermitian 4-manifold satisfying condition (48). Then, for any vector field $X$ and any local quaternionic supplement $(I, K)$ of $J$, we have the equation
$$\delta W_{+}(X)=-\frac{1}{4}\left((3 \lambda \delta \Omega(X)+2 d \lambda(J X)) J+3 \lambda \cdot \nabla_{J X} J-d \lambda(I X) I-d \lambda(K X) K\right) .$$

Proof. We already know that (48) implies equation (59) being equivalent to
$$\nabla_{X} W_{+}=X(\lambda)\left(2 P_{1}-P_{2}\right)+3 \lambda \nabla_{X} P_{1} .$$
Moreover, for any skew symmetric endomorphisms $A$ and any local quaternionic supplement $(I, K)$ of $J$, it holds that
$$\begin{gathered}
P_{1}(A)=\langle J, A\rangle J \quad, \quad P_{2}(A)=\langle I, A\rangle I+\langle K, A\rangle K, \\
\left(\nabla_{X} P_{1}\right)(A)=\left\langle\nabla_{X} J, A\right\rangle J+\langle J, A\rangle \nabla_{X} J .
\end{gathered}$$
Hence, by the former expression for $\nabla_{X} W_{+}$, we obtain
$$\begin{aligned}
& \left(\nabla_{X} W_{+}\right)(A)=\left(2 X(\lambda)\langle J, A\rangle+3 \lambda\left\langle\nabla_{X} J, A\right\rangle\right) J+ \\
& 3 \lambda\langle J, A\rangle \nabla_{X} J-X(\lambda)(\langle I, A\rangle I+\langle K, A\rangle K) .
\end{aligned}$$
Now, by a direct calculation using (63), we obtain (64). \(\square\)

Theorem 3.2. Let $(M, g, J)$ be an almost Hermitian 4-manifold with the properties (48) and $\operatorname{supp}\left(W_{+}\right)=M$. Furthermore, we suppose that at least one of the following conditions is satisfied:
\begin{itemize}
\item[(i)] $(M, g)$ is Einstein.
\item[(ii)] The Ricci tensor is parallel ( $\nabla$ Ric $=0$ ).
\item[(iii)] The curvature tensor is harmonic $(\delta R=0)$.
\item[(iv)] The Weyl tensor is harmonic $(\delta W=0)$.
\item[(v)] $W_{+}$is divergence free $\left(\delta W_{+}=0\right)$.
\end{itemize}

Then the following assertions are valid:
\begin{itemize}
\item[(a)] $J$ is integrable, i.e., $(M, g, J)$ is a Hermitian manifold.
\item[(b)] On $M_{+} \subseteq M, g$ is conformally equivalent to a Kähler metric $\bar{g}$ such that $\left(M_{+}, \bar{g}, J\right)$ is a Kähler manifold.
\item[(c)] $(M, g, J)$ itself is a Kähler manifold if and only if the function $\left|W_{+}\right|$is constant.
\end{itemize}

Proof. First of all, we note the implications (i) → (ii) → (iii) → (iv) → (v). Thus, it suffices to consider the case of condition (v). By Lemma 3.2 on $M_{+} \subseteq M$, the equation $\delta W_{+}=0$ implies the equations
$$\begin{gathered}
\delta \Omega(X)=-\frac{2}{3 \lambda} d \lambda(J X) \\
\nabla_{J X} J=\frac{1}{3 \lambda}(d \lambda(I X) I+d \lambda(K X) K) .
\end{gathered}$$
We see that (66) implies (65) and, moreover, the relation
$$\nabla_{J X} J=J \circ \nabla_{X} J .$$
It is known that (67) forces the vanishing of the Nijenhuis tensor $N_{J}$. Thus, we have $N_{J}=0$ on $M_{+}$and, hence, on $M$ since $M_{+}$is dense in $M$. This proves (a). By (48), assertion (c) is an immediate consequence of (66). Finally, we prove assertion (b). Let us consider a conformal transformation $\bar{g}=e^{f} \cdot g$. Then, the covariant derivatives $\bar{\nabla}$ of $\bar{g}$ and ∇ of $g$ are related by
$$\bar{\nabla}_{X}=\nabla_{X}+\frac{1}{2}(X(f)+d f \otimes X-g(X) \otimes \nabla f) .$$
This yields
$$\bar{\nabla}_{X} J=\nabla_{X} J+\frac{1}{2}[d f \otimes X-g(X) \otimes \nabla f, J] .$$
On the other hand, choosing any local quaternionic supplement $(I, K)$ of $J$ we find the relation
$$[d f \otimes X-g(X) \otimes \nabla f, J]=d f(K X) I-d f(I X) K .$$
Inserting (69) into (68) we obtain
$$\bar{\nabla}_{X} J=\nabla_{X} J+\frac{1}{2} d f(K X) I-\frac{1}{2} d f(I X) K .$$
Hence, the special choice
$$e^{f}=\sqrt[3]{\lambda^{2}} \stackrel{(48)}{=} \sqrt[3]{\frac{1}{6}\left|W_{+}\right|^{2}}$$
yields
$$\bar{\nabla}_{X} J \stackrel{(70)}{=} \nabla_{X} J+\frac{1}{3 \lambda}(d \lambda(K X) I-d \lambda(I X) K) \stackrel{(66)}{=} 0 .$$ \(\square\)

Proposition 3.1. For any almost Hermitian 4-manifold ( $M, g, J$ ) which satisfies condition (48), the equation
$$\left.\delta W_{+}(X)=-\frac{3}{4} \lambda\left(\delta \Omega(X) J+\nabla_{J X} J\right)-\left(\nabla \log \left|W_{+}\right|\right\lrcorner W_{+}\right)(X)$$
is valid for any vector field $X$ on $M_{+}$.
Proof. Using any local quaternionic supplement $(I, K)$ of $J$ we calculate
$$\begin{gathered}
\left.\left(\nabla \log \left|W_{+}\right|\right\lrcorner W_{+}\right)(X)=W_{+}\left(\nabla \log \left|W_{+}\right|, X\right) \stackrel{(48)}{=} W_{+}(\nabla \log |\lambda|, X)= \\
W_{+}\left(\frac{\nabla \lambda}{\lambda}, X\right)=\frac{1}{2} W_{+}\left(g(X) \otimes \frac{\nabla \lambda}{\lambda}-\frac{d \lambda}{\lambda} \otimes X\right) \stackrel{\text { (49) }}{=} \\
\frac{1}{2}\left(2 P_{1}-P_{2}\right)(g(X) \otimes \nabla \lambda-d \lambda \otimes X)= \\
-2\langle d \lambda \otimes X, J\rangle J+\langle d \lambda \otimes X, I\rangle I+\langle d \lambda \otimes X, K\rangle K= \\
\frac{1}{4}(2 d \lambda(J X) J-d \lambda(I X)-d \lambda(K X) K)
\end{gathered}$$

Thus, we have
$$\left.\left(\nabla \log \left|W_{+}\right|\right\lrcorner W_{+}\right)(X)=\frac{1}{4}(2 d \lambda(J X) J-d \lambda(I X)-d \lambda(K X) K) .$$
Inserting this into (64) we obtain (71). \(\square\)

We remark that the tensor field $\left.\nabla \log \left|W_{+}\right|\right\lrcorner W_{+}$is defined not only on $M_{+}$. It can be extended to M by equation (72).

Theorem 3.3. An almost Hermitian 4-manifold $(M, g, J)$ with $\operatorname{supp}\left(W_{+}\right)=M$ is Kähler if and only if it satisfies the conditions (48) and (62).

Proof. By Proposition 3.1 the conditions (48), (62) immediately imply $\nabla J=0$. Conversely, by Proposition 2.2 we have equation (55) in the Kähler case. Using (55) we obtain the equation
$$\left.\delta W_{+}+\nabla \log |S|\right\lrcorner W_{+}=0$$
and, hence, equation (62) by (51). \(\square\)

Since (51) and $S_{\star}=S$ imply (48), the following corollary is an immediate consequence of Theorem 3.3

Corollary 3.2. An almost Hermitian 4-manifold $(M, g, J)$ with $\operatorname{supp}(S)=M$ is Kähler if and only if the equations $S_{\star}=S,\left|W_{+}\right|^{2}=S^{2} / 6$ are valid and equation (73) on $M_{+}$.
We remark that condition (73) is satisfied automatically if the curvature tensor is harmonic $(\delta R=0)$ and, hence, if the Ricci tensor is parallel or if the manifold is Einstein.

We finish this section by a theorem which is closely related to a result of Derdzinski ([6], 16.67) and which shows that the local Kähler property of an oriented Riemannian 4-manifold $(M, g)$ with $W_{+} \neq 0$ everywhere can be formulated without using any almost complex structure.

Theorem 3.4. Let $(M, g)$ be an oriented Riemannian 4-manifold such that $W_{+}$vanishes nowhere. Then the following conditions are equivalent:
(i) $g$ is locally a Kähler metric with respect to local complex structures that are compatible with the given orientation.
(ii) The condition (50) and (57) are satisfied.
(iii) The equations (50) and (62) are valid.

Proof. The assumptions $M_{+}=M$ and (50) imply that $W_{+}$has exactly two eigenvalues at every point of $M$. This yields the orthogonal splitting
$$\Lambda_{+}^{2}=E_{1} \oplus E_{2}$$
of $\Lambda_{+}^{2}$ into the corresponding eigenbundles $E_{1}, E_{2}$ of $W_{+}$with $\operatorname{rank}\left(E_{\alpha}\right)=\alpha(\alpha=1,2)$. By assertion (ii) of Lemma 2.1 the local unit sections of $E_{1}$ define local almost complex structures compatible with the metric $g$ and the given orientation. Thus, any oriented Riemannian 4-manifold $(M, g)$ with $M_{+}=M$ and (50) is locally almost Hermitian. Moreover, by $\operatorname{tr}\left(W_{+}\right)=0$, (74) implies that $W_{+}=\mu\left(2 Q_{1}-Q_{2}\right)$, where $Q_{1}, Q_{2}: \Lambda_{+}^{2} \rightarrow \Lambda_{+}^{2}$ denote the corresponding projections $\left(Q_{\alpha}\left(\Lambda_{+}^{2}\right)=E_{\alpha}, \alpha=1,2\right)$. Now, the proofs of Theorem 3.1 and Theorem 3.3 show that, in this case, condition (57) and also condition (62) forces the Kähler property of all these local almost Hermitian structures. The converse is true by Proposition 2.2 and Theorem 3.3 \(\square\)

\section*{4. Integrability conditions for almost Kähler 4-manifolds.}

By (22) and (43)-(45), we immediately obtain the following assertion.
Proposition 4.1. On every almost Kähler 4-manifold $(M, g, J)$, the equation
$$\left|W_{+}\right|^{2}-\frac{S^{2}}{6}=S|\nabla J|^{2}+|\nabla J|^{4}+8\left|\mathrm{Ric}_{\star}^{-}\right|^{2}+|\tilde{R}|^{2}$$
is valid.

Together with assertion (i) of Proposition 2.2 this proves the following result.
Theorem 4.1. Let $(M, g, J)$ be any almost Kähler 4-manifold with scalar curvature $S \geq 0$. Then $(M, g, J)$ is Kähler if and only if the equation $\left|W_{+}\right|^{2}=S^{2} / 6$ is satisfied.

Corollary 4.1. Every almost Kähler 4-manifold with the property $S=\left|W_{+}\right| \sqrt{6}$ is already a Kähler manifold.

For any compact almost Hermitian manifold $(M, g, J)$ we consider the number
$$Q(J):=\int_{M} q(J) \omega,$$
where $\omega$ denotes the volume form and $q(J)$ the function locally defined by
$$q(J):=g\left(\left(\nabla_{X_{k}, X_{l}}^{2} \operatorname{Ric}\right) J X^{k}, J X^{l}\right) .$$
$Q(J)$ is an obstruction to the Kähler property for any compact almost Hermitian manifold ([12], Section 2). The following proposition is a corollary of Proposition 2.5 in [12].

Proposition 4.2. For any compact almost Kähler 4-manifold $(M, g, J)$, we have the equation
$$Q(J)+\int_{M}\left(|\tilde{R}|^{2}+4\left|\operatorname{Ric}_{\star}^{-}\right|^{2}+\frac{S}{2}|\nabla J|^{2}+|\nabla J|^{4}\right) \omega=0 .$$
We remark that, in contrast to this paper, in [12] the length of an endomorphism $A$ is defined by $|A|^{2}:=\operatorname{tr}\left(A^{*} \circ A\right)$. This explains the factor 4 in equation (76). We also have to take into account the different definitions of the function $|\nabla J|^{2}$ in [12] and in this paper.
Combining (75) and (76) we obtain the next proposition.
Proposition 4.3. On any compact almost Kähler 4-manifold $(M, g, J)$, the equation
$$Q(J)+\frac{1}{2} \int_{M}\left(|\tilde{R}|^{2}+|\nabla J|^{4}+\left|W_{+}\right|^{2}-\frac{S^{2}}{6}\right) \omega=0$$
holds.
The Weitzenböck formula (77) immediately yields the following result.
Theorem 4.2. A compact almost Kähler 4-manifold $(M, g, J)$ is Kähler if and only if the equations $Q(J)=0$ and $\left|W_{+}\right|^{2}=S^{2} / 6$ are satisfied.

By Remark 3.9 in [12], we know several conditions that imply the vanishing of $Q(J)$. For example, the assumption $[\nabla$ Ric,$J]=0$, i.e., $\left[\nabla_{X} \operatorname{Ric}, J\right]=0$ for all vector fields $X$, implies $Q(J)=0$ and also the supposition $\left[\nabla^{2}\right.$ Ric, $\left.J\right]=0$, i.e., $\left[\nabla_{X, Y}^{2}\right.$ Ric, $\left.J\right]=0$ for all vector fields $X, Y$. In particular, we have $Q(J)=0$ if the Ricci tensor is parallel ( $\nabla$ Ric $=0$ ). Another condition that forces $Q(J)=0$ is $\delta W=0$ (harmonic Weyl tensor). Thus, the next corollary is an immediate consequence of Theorem 4.2

Corollary 4.2. Let $(M, g, J)$ be a compact almost Kähler 4-manifold satisfying at least one of the following conditions:
\begin{itemize}
\item[(i)] The relation $\left[\nabla^{2} \operatorname{Ric}, J\right]=0$ is valid.
\item[(ii)] It holds that $[\nabla \mathrm{Ric}, J]=0$.
\item[(iii)] The Weyl tensor is harmonic.
\item[(iv)] The Ricci tensor is parallel.
\item[(v)] $(M, g)$ is Einstein.
\end{itemize}
Then $(M, g, J)$ is a Kähler manifold if and only if $\left|W_{+}\right|^{2}=S^{2} / 6$.
It is known that the Ricci tensor of a Kähler manifold with harmonic Weyl tensor is parallel ([6], 16.30). This shows that, in the context of Corollary 4.2 the conditions (iii) and (iv) are equivalent.

In the following we prove a result which is an essential generalization of this part of Corollary 4.2. For any Riemannian $n$-manifold $(M, g)$ with $n \geq 3$, the relation
$$g(\delta W(X) Y, Z)=\frac{n-3}{n} g\left(X,\left(\nabla_{Y} \operatorname{Ric}\right) Z-\left(\nabla_{Z} \operatorname{Ric}\right) Y-\frac{1}{2(n-1)}(Y(S) Z-Z(S) Y)\right)$$
is well-known. Using this we obtain the equation
$$\begin{aligned}
\langle\delta W(X), A\rangle & =\frac{n-3}{n(n-2)} g\left(X,\left(\nabla_{X_{k}} \operatorname{Ric}\right) A X^{k}-\left(\nabla_{A X_{k}} \operatorname{Ric}\right) X^{k}\right. \\
& \left.-\frac{1}{2(n-1)}\left(A(\nabla S)-d S\left(A X_{k}\right) X^{k}\right)\right)
\end{aligned}$$
for any vector field $X$ and any skew symmetric endomorphism $A: T M \rightarrow T M$.
Lemma 4.1. Let $(M, g)$ be any oriented Riemannian 4-manifold. Then, for any vector field $X$ and any positively oriented local orthonormal frame $\left(\Omega_{I}, \Omega_{J}, \Omega_{K}\right)$ of $\Lambda_{+}^{2}$, we have the equation
$$\begin{gathered}
\delta W_{+}(X)=\frac{1}{4}\left(g\left(X,\left(\nabla_{X_{k}} \operatorname{Ric}\right) I X^{k}\right) I+g\left(X,\left(\nabla_{X_{k}} \operatorname{Ric}\right) J X^{k}\right) J+g\left(X,\left(\nabla_{X_{k}} \operatorname{Ric}\right) K X^{k}\right) K\right) \\
+\frac{1}{24}(d S(I X) I+d S(J X) J+d S(K X) K) .
\end{gathered}$$
Proof. By definition, it holds that
$$\delta W_{+}(X)=P_{+}(\delta W(X)) .$$
Thus, we obtain the local representation
$$\delta W_{+}(X)=\langle\delta W(X), I\rangle I+\langle\delta W(X), J\rangle J+\langle\delta W(X), K\rangle K,$$
where $\left(\Omega_{I}, \Omega_{J}, \Omega_{K}\right)$ is any positively oriented local orthonormal frame of $\Lambda_{+}^{2}$. By (78), this yields
$$\begin{aligned}
\delta W_{+}(X)= & \frac{1}{4} g\left(X,\left(\nabla_{X_{k}} \operatorname{Ric}\right) I X^{k}-\frac{1}{6} I(\nabla S)\right) I \\
& \left.+\frac{1}{4} g\left(X, \nabla_{X_{k}} \operatorname{Ric}\right) J X^{k}-\frac{1}{6} J(\nabla S)\right) J \\
& +\frac{1}{4} g\left(X,\left(\nabla_{X_{k}} \operatorname{Ric}\right) K X^{k}-\frac{1}{6} K(\nabla S)\right) K
\end{aligned}$$
and, hence, (79). \(\square\)

Now, for any almost Hermitian 4-manifold $(M, g, J)$, we consider the endomorphism valued 1-form $\Theta$ defined by
$$\left.\Theta:=\frac{1}{6} \nabla S\right\lrcorner\left(2 P_{1}-P_{2}\right),$$
where $P_{1}, P_{2}$ as before denote the projections of splitting (23). Then, for any vector field $X$, we have locally
$$\Theta(X)=\frac{1}{24}(2 d S(J X) J-d S(I X) I-d S(K X) K)$$
where $(I, K)$ is any local quaternionic supplement of $J$.
Lemma 4.2. Let $(M, g, J)$ be any almost Hermitian 4-manifold. Then, the following assertions are valid: The condition
$$\delta W_{+}+\Theta=0 \quad\left(\delta W_{+}=0\right)$$
is satisfied if and only if we have the equation
$$\left(\nabla_{X_{k}} \operatorname{Ric}\right) J X^{k}=\frac{1}{2} J(\nabla S) \quad\left(\left(\nabla_{X_{k}} \operatorname{Ric}\right) J X^{k}=\frac{1}{6} J(\nabla S)\right)$$
and, moreover, for any local quaternionic supplement $(I, K)$ of $J$, the equations
$$\begin{gathered}
\left(\nabla_{X_{k}} \operatorname{Ric}\right) I X^{k}=0 \quad, \quad\left(\nabla_{X_{k}} \operatorname{Ric}\right) K X^{k}=0 \\
\left(\left(\nabla_{X_{k}} \operatorname{Ric}\right) I X^{k}=\frac{1}{6} I(\nabla S) \quad, \quad\left(\nabla_{X_{k}} \operatorname{Ric}\right) K X^{k}=\frac{1}{6} K(\nabla S)\right) .
\end{gathered}$$

Proof. We apply Lemma 4.1 to such local orthonormal frames $\left(\Omega_{I}, \Omega_{J}, \Omega_{K}\right)$ of $\Lambda_{+}^{2}$ for which $(I, K)$ is any local quaternionic supplement of $J$. Then, by (79) and (80), we immediately obtain the assertion of our lemma. \(\square\)

Now, for any almost Hermitian manifold $(M, g, J)$, we introduce the vector valued 2-forms $\varphi$ and $\psi$ defined by
$$\begin{gathered}
\varphi(X, Y):=\left(\nabla_{X} J\right) Y-\left(\nabla_{Y} J\right) X, \\
\psi(X, Y):=\frac{1}{8}\left(\left[\nabla_{X} \operatorname{Ric}, J\right] Y-\left[\nabla_{Y} \operatorname{Ric}, J\right] X-\left[\nabla_{J X} \operatorname{Ric}, J\right] J Y+\left[\nabla_{J Y} \operatorname{Ric}, J\right] J X\right) .
\end{gathered}$$
Using the notation $\langle\varphi, \psi\rangle:=\frac{1}{2} g\left(\varphi\left(X^{k}, X^{l}\right), \psi\left(X_{k}, X_{l}\right)\right)$, by (63) and (72) in [12], we have the following lemma.

Lemma 4.3. Let $(M, g, J)$ be any almost Kähler manifold. Then the equation
$$\langle\varphi, \psi\rangle=\frac{1}{4} g\left(J\left(\varphi\left(X^{k}, X^{l}\right)\right),\left(\nabla_{X_{k}} \operatorname{Ric}\right) X_{l}-\left(\nabla_{X_{l}} \operatorname{Ric}\right) X_{k}\right)$$
is valid. Moreover, if $M$ is compact, then
$$Q(J)=2 \int_{M}\langle\varphi, \psi\rangle \omega .$$
If $(M, g, J)$ is any almost Hermitian 4-manifold and $(I, K)$ any quaternionic supplement of $J$ on a sufficiently small open subset $U \subseteq M$, then there are uniquely determined vector fields $\xi, \eta$ on $U$ such that
$$\nabla_{X} J=g(\xi, X) I+g(\eta, X) K$$
for any vector field $X$ on $U$. It is well-known that we have $d \Omega_{J}=0$ then if and only if
$$\eta=J \xi .$$

Lemma 4.4. Let $(M, g, J)$ be any almost Kähler 4-manifold. Then the function $\langle\varphi, \psi\rangle$ is locally given by
$$\langle\varphi, \psi\rangle=\frac{1}{2} g\left(\left(\nabla_{X_{k}} \operatorname{Ric}\right) K X^{k}, \xi\right)-\frac{1}{2} g\left(\left(\nabla_{X_{k}} \operatorname{Ric}\right) I X^{k}, \eta\right),$$
where $(I, K)$ is any local quaternionic supplement of $J$ and $\xi, \eta$ the corresponding vector fields defined by (83).

Proof. Using (82) and (83), we compute
$$\begin{aligned}
\langle\varphi, \psi\rangle= & \frac{1}{2} g\left(J\left(\left(\nabla_{X^{k}} J\right) X^{l}\right),\left(\nabla_{X_{k}} \operatorname{Ric}\right) X_{l}-\left(\nabla_{X_{l}} \operatorname{Ric}\right) X_{k}\right)= \\
& \frac{1}{2} g\left(-g\left(\xi, X^{k}\right) K X^{l}+g\left(\eta, X^{k}\right) I X^{l},\left(\nabla_{X_{k}} \operatorname{Ric}\right) X_{l}-\left(\nabla_{X_{l}} \operatorname{Ric}\right) X_{k}\right)= \\
& -2\left\langle K, \nabla_{\xi} \operatorname{Ric}\right\rangle+\frac{1}{2} g\left(\left(\nabla_{X_{l}} \operatorname{Ric}\right) K X^{l}, \xi\right)+2\left\langle I, \nabla_{\eta} \operatorname{Ric}\right\rangle-\frac{1}{2} g\left(\left(\nabla_{X_{l}} \operatorname{Ric}\right) I X^{l}, \eta\right) .
\end{aligned}$$
This yields (85) since $\left\langle K, \nabla_{\xi}\right.$ Ric $\rangle=\left\langle I, \nabla_{\eta}\right.$ Ric $\rangle=0$. \(\square\)

Now, we are able to prove the main results of this section.
Theorem 4.3. Let $(M, g, J)$ be a compact almost Kähler 4-manifold. Then we have the following:
(i) $(M, g, J)$ is Kähler if and only if $\left|W_{+}\right|^{2}=S^{2} / 6$ and $\delta W_{+}+\Theta=0$.
(ii) $(M, g, J)$ is a Kähler manifold of constant scalar curvature if and only if $\left|W_{+}\right|^{2}=S^{2} / 6$ and $\delta W_{+}=0$.

Proof. By Lemma 4.2 and Lemma 4.4 we see that $\delta W_{+}+\Theta=0$ implies $\langle\varphi, \psi\rangle=0$ and, hence, $Q(J)=0$ by Lemma 4.3 Thus, by Theorem $4.2(M, g, J)$ is Kähler. Conversely, by Proposition 2.2 (equations (51) and (55)), we see that the equations $|W|^{2}=S^{2} / 6$ and $\delta W_{+}+\Theta=0$ are valid for any Kähler manifold. This proves assertion (i). By Lemma 4.2 the assumption $\delta W_{+}=0$ implies locally
$$\left(\nabla_{X_{k}} \operatorname{Ric}\right) I X^{k}=\frac{1}{6} I(\nabla S) \quad, \quad\left(\nabla_{X_{k}} \operatorname{Ric}\right) K X^{k}=\frac{1}{6} K(\nabla S) .$$
Inserting this into (85) we obtain
$$\langle\varphi, \psi\rangle=\frac{1}{12} g(K(\nabla S), \xi)-\frac{1}{12} g(I(\nabla S), \eta) \stackrel{(84)}{=} 0$$
and, hence, $Q(J)=0$ as before. Thus, the conditions $\delta W_{+}=0$ and $\left|W_{+}\right|^{2}=S^{2} / 6$ also imply the Kähler property. But, in the Kähler case, equation (81) in parentheses immediately yields $\nabla S=0$. \(\square\)

Since the condition $\delta W_{+}+\Theta=0$ and also $\delta W_{+}=0$ generalizes the Einstein condition, Theorem 4.3 is related to the Goldberg conjecture (see introduction). The following theorems are also results in this direction.

Theorem 4.4. A compact almost Kähler Einstein 4-manifold is Kähler if and only if the length of the self-dual part of its Weyl tensor is constant.

Proof. By (45), we have the inequality
$$\left|W_{+}\right|^{2} \geq \frac{3}{8}\left(S_{\star}-\frac{S}{3}\right)^{2}$$
for any almost Hermitian 4-manifold. Now, for any compact almost Kähler Einstein 4-manifold, it was proved by J. Armstrong 3 that there is at least one point at which $S_{\star}=S$. By (86), at such a point we have
$$\left|W_{+}\right|^{2} \geq \frac{S^{2}}{6} .$$
Thus, if $\left|W_{+}\right|$is constant, this inequality is satisfied everywhere since $S$ is constant owing to the Einstein condition. By Proposition 4.3 this forces $\nabla J=0$ since we have $Q(J)=0$ in the Einstein case. The converse is true by assertion (i) of Proposition 2.2 \(\square\)

A theorem of Oguro and Sekigawa [16] asserts that an almost Kähler Einstein 4-manifold is Kähler if and only if its star scalar curvature is constant. Theorem 4.4 is a similar result in the compact case.

Corollary 4.3. A compact almost Kähler Einstein 4-manifold is Kähler if and only if it has the property
$$\operatorname{det}\left(W_{+}\right)=\frac{S}{18}\left|W_{+}\right|^{2} .$$
Proof. By assertion (i) of Proposition 2.2 we see that equation (87) is satisfied in the Kähler case. Conversely, the Einstein condition implies $\delta W_{+}=0$ and, hence, by 16.73 in [6], the equation
$$2\left|\nabla W_{+}\right|^{2}+\triangle\left|W_{+}\right|^{2}=18 \operatorname{det}\left(W_{+}\right)-S\left|W_{+}\right|^{2} .$$
Integrating this equation the supposition (87) immediately forces $\nabla W_{+}=0$. In particular, $\left|W_{+}\right|$ is constant. By Theorem 4.4 this implies the Kähler property. \(\square\)

Theorem 4.5. A compact almost Kähler 4-manifold with constant negative scalar curvature $S$ is Kähler if and only if it satisfies the curvature conditions $\operatorname{det}\left(W_{+}\right)=S^{3} / 108$ and $\delta W_{+}=0$.

Proof. By Proposition 2.2 the conditions of our theorem are satisfied for any Kähler 4-manifold of constant scalar curvature. Conversely, since $\delta W_{+}=0$ and $S$ is constant by supposition, we have
$$\begin{gathered}
0 \leq 2 \int_{M}\left|\nabla W_{+}\right|^{2} \omega=\int_{M}\left(2\left|\nabla W_{+}\right|^{2}+\triangle\left|W_{+}\right|^{2}\right) \omega \stackrel{(88)}{=} \\
\int_{M}\left(18 \operatorname{det}\left(W_{+}\right)-S\left|W_{+}\right|^{2}\right) \omega=(-S) \cdot \int_{M}\left(\left|W_{+}\right|^{2}-\frac{S^{2}}{6}\right) \omega .
\end{gathered}$$
Thus, it follows $\int_{M}\left(\left|W_{+}\right|^{2}-\frac{S^{2}}{6}\right) \omega \geq 0$ since $S<0$. By Proposition 4.3 this yields $\nabla J=0$ since we already know that $\delta W_{+}=0$ implies $Q(J)=0$ in the almost Kähler case. \(\square\)

Corollary 4.4. Let $(M, g, J)$ be a compact almost Kähler 4-manifold with $S<0$ such that at least one of the following conditions is satisfied:
(i) The curvature tensor is harmonic $(\delta R=0)$.
(ii) The Ricci tensor is parallel.
(iii) $(M, g)$ is Einstein.
Then $(M, g, J)$ is Kähler if and only if $\operatorname{det}\left(W_{+}\right)=S^{3} / 108$.
Proof. We have the implications (iii) → (ii) → (i). But $\delta R=0$ implies that $S$ is constant and $\delta W_{+}=0$. \(\square\)

\section*{References}
\begin{itemize}
\item[] [1] V. Apostolov, T. Draghici and A. Moroianu, A splitting theorem for Kähler manifolds whose Ricci tensors have constant eigenvalues, Int. J. Math. 12 (7) (2001), 769-789.
\item[] [2] V. Apostolov, J Armstrong, T. Draghici, Local models and integrability of certain almost Kähler 4-manifolds, Math. Ann., 323 (2002), 633-666.
\item[] [3] J. Armstrong, On four-dimensional almost Kähler manifolds, Quart. J. Math. Oxford Ser. (2), 48 (1997), 405-415.
\item[] [4] J. Armstrong, An ansatz for almost-Kähler, Einstein 4-manifolds, J. Reine Angew. Math., 542 (2002), 53-84.
\item[] [5] M.F. Atiyah, N.J. Hitchin and I.M. Singer, Self-duality in four-dimensional Riemannian geometry, Proc. Roy. Soc. London A362 (1978), 425-461.
\item[] [6] A.L. Besse, Einstein manifolds II, Springer, Berlin 1987.
\item[] [7] Seminaire Arthur Besse 1978/79, Géométrie riemannienne en dimension 4, Cedic / Fernand Nathan, Paris 1981.
\item[] [8] A. Derdzinski, Self-dual Kähler manifolds and Einstein manifolds of dimension four, Comp. Math. 49 (1983), 405-433.
\item[] [9] T. Draghici, On some 4-dimensional almost Kähler manifolds, Kodai Math. J. 18 (1995), 156-163.
\item[] [10] T. Draghici, Almost Kähler 4-manifolds with J-invariant Ricci tensor, Houston J. Math. 25 (1999), 133-145.
\item[] [11] S.I. Goldberg, Integrability of almost Kähler manifolds, Proc. Amer. Math. Soc. 21 (1969), 96-100.
\item[] [12] K.-D. Kirchberg, Some integrability conditions for almost Kähler manifolds, J. Geom. Phys. 49 (2004), 101-115.
\item[] [13] P. Nurowski and M. Przanowski, A four-dimensional example of Ricci flat metric admitting almost Kähler non-Kähler structure, Classical Quantum Gravity 16 (1999), No. 3, L9-L13.
\item[] [14] T. Oguro, K. Sekigawa, Four-dimensional almost Kähler Einstein and $*$-Einstein manifolds, Geom. Dedicata 69 (1998), 91-112.
\item[] [15] T. Oguro, K. Sekigawa, A. Yamada, Four-dimensional almost Kähler Einstein and weakly *-Einstein manifolds, Yokohama Math. J. 47 (1999), 75-92.
\item[] [16] T. Oguro, K. Sekigawa, On some four-dimensional almost Kähler Einstein manifolds, Kodai Math. J. 24 (2001), 226-258.
\item[] [17] T. Oguro, K. Sekigawa, A. Yamada, Goldberg conjecture and related topics, Proceedings of the Eighth International Workshop on Diff. Geom. 8 (2004), 1-21.
\item[] [18] K. Sekigawa, On some compact Einstein almost Kähler manifolds, J. Math. Soc. Japan 39 (1987), 677-684.
\end{itemize}

Institute of Mathematics
Humboldt-Universität zu Berlin
Office: Rudower Chaussee 25
D-10099 Berlin, Germany
kirchber@mathematik.hu-berlin.de