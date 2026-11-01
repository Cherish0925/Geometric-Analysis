---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: math_0304092.pdf
converter: mathpix
format: mmd
---

\title{
SOME INTEGRABILITY CONDITIONS FOR ALMOST KÄHLER MANIFOLDS
}

\author{
K.-D. KIRCHBERG
}

\begin{abstract}
Among other results, a compact almost Kähler manifold is proved to be Kähler if the Ricci tensor is semi-negative and its length coincides with that of the star Ricci tensor or if the Ricci tensor is semi-positive and its first order covariant derivatives are Hermitian. Moreover, it is shown that there are no compact almost Kähler manifolds with harmonic Weyl tensor and non-parallel semi-positive Ricci tensor. Stronger results are obtained in dimension 4.
\end{abstract}

2002 Mathematics Subject Classification: 53B20, 53C25

\section*{0. Introduction}

To find suitable curvature conditions that imply the integrability of the almost complex structure is one of the most important problems concerning almost Kähler manifolds. In this context, the starting point for many investigations was Goldberg's conjecture of 1969, which states that every compact Einstein almost Kähler manifold is necessarily Kähler [14]. Important progress was made by K. Sekigawa in 1987. He proved the Goldberg conjecture for non-negative scalar curvature [27]. In case of negative scalar curvature, no proof is known so far. There are attempts to construct counterexamples against this part of the Goldberg conjecture. Our paper deals with several kinds of curvature conditions that force an almost Kähler manifold to be Kähler, i.e., that the almost complex structure of an almost Kähler manifold is integrable. One of our main results is a generalization of Sekigawa's theorem mentioned above. We prove that a compact almost Kähler manifold is Kähler if the Ricci tensor is semi-positive (Ric $\geq 0$ ) and its first order covariant derivatives commute with the almost complex structure (Corollary 3.10). In dimension 4, the supposition that Ric $\geq 0$ can be replaced by the weaker condition that the star scalar curvature $S_{\star}$ is non-negative (Corollary 3.11). This result is more general than the theorem that H. Satoh [25] proved recently. Satoh's theorem states that every compact almost Kähler manifold with semi-positive Ricci tensor and harmonic Weyl tensor $(\delta W=0)$ is already Kähler. We show that there are no compact almost Kähler manifolds with harmonic Weyl tensor and semi-positive, non-parallel Ricci tensor (Corollaries 3.12 3.13). Thus, the suppositions of Satoh's theorem imply that the Ricci tensor is parallel.
It is well known that an almost Kähler manifold is Kähler if its star scalar curvature coincides with the scalar curvature $S$. A similar result is our Proposition 3.1 which states that an almost Kähler manifold with semi-positive Ricci tensor is already Kähler if the Hermitian parts of the Ricci tensor and the star Ricci tensor have the same length. In dimension 4, the supposition that Ric $\geq 0$ can replaced by the essential weaker condition that $S \geq 0$ or that the set of zeros of $S+S_{\star}$ is nowhere dense (Proposition 3.2). For a compact almost Kähler manifold with semi-negative Ricci tensor (Ric $\leq 0$ ), the Kähler property is forced by the supposition that the length of the star Ricci tensor Ric ${ }_{\star}$ coincides with that of the Ricci tensor (Theorem 3.3).

In the case of a compact Einstein almost Kähler $n$-manifold, the curvature inequality
$$\left|\tilde{R}^{-}\right|^{2}+\mid \text { Ric }\left._{\star}\right|^{2} \geq \frac{1}{n} S \cdot S_{\star}$$
forces the Kähler property (Theorem 3.4). Here $\tilde{R}^{-}$is a part of the curvature tensor depending on the almost complex structure $J$ and the Weyl tensor $W$ only. This inequality is satisfied trivially if $S_{\star} \geq 0$. Since $S \geq 0$ implies $S_{\star} \geq 0$, we obtain Sekigawa's result. With regard to the Goldberg conjecture it may be interesting to investigate for which compact Einstein almost Kähler manifolds $(*)$ is valid if $S<0$.
In order to obtain the results for the compact case, we modify a well known basic Weitzenböck formula. So we find two integral formulas of different kind (Proposition 2.5). The second one is applicable if a certain number $Q(J)$ vanishes. $Q(J)$ is a globally defined obstruction against the integrability of the almost complex structure $J$ of every compact almost Kähler manifold. We prove that a compact almost Kähler manifold with semi-positive Ricci tensor is Kähler if and only if $Q(J)=0$ (Theorem 3.6). This theorem and the corresponding 4-dimensional version (Theorem 3.7) are essential results of this paper. In these theorems the suppositions that Ric $\geq 0$ and $S_{\star} \geq 0$, respectively, can be replaced by weaker curvature inequalities (Remark 3.8). Moreover, we list some geometrical conditions, each of which implies $Q(J)=0$ (Remark 3.9).

\section*{1. Preliminaries}

Let $(M, g, J)$ be an almost Hermitian manifold of dimension $n=2 m$ with Riemannian metric $g$ and almost complex structure $J$. Then, by definition
$$J^{2}=-1$$
and $g$ is $J$-invariant, i.e., we have
$$g(J X, J Y)=g(X, Y)$$
for all vector fields $X, Y$. The corresponding fundamental 2-form $\Omega$ is defined by $\Omega(X, Y):=$ $g(J X, Y)$. An almost Hermitian manifold is called almost Kähler if its fundamental form is closed
$$d \Omega=0 .$$
It is well known that the basic equations (1)-(3) of an almost Kähler manifold imply that $\Omega$ is also co-closed
$$\delta \Omega=0$$
and that $J$ satisfies the so-called quasi Kähler condition
$$\nabla_{J X} J=\nabla_{X} J \circ J,$$
where ∇, as usually, denotes the Levi-Civita covariant derivative corresponding to $g$. (3) is equivalent to
$$g\left(\left(\nabla_{X} J\right) Y, Z\right)+g\left(\left(\nabla_{Y} J\right) Z, X\right)+g\left(\left(\nabla_{Z} J\right) X, Y\right)=0 .$$
By (1) and (2), it holds that
$$g(J X, Y)=-g(X, J Y),$$
i.e., $J$ is anti-selfadjoint (skew symmetric)
$$J^{*}=-J .$$
Applying $\nabla_{X}$ to equation (1) we obtain
$$\nabla_{X} J \circ J+J \circ \nabla_{X} J=0 .$$

In the following we use the notation
$$\nabla_{X, Y}^{2}:=\nabla_{X} \circ \nabla_{Y}-\nabla_{\nabla_{X} Y}$$
for the tensorial covariant derivatives of second order. Then the Riemannian curvature tensor $R$ of the metric $g$ is given by
$$R(X, Y) Z=\nabla_{X, Y}^{2} Z-\nabla_{Y, X}^{2} Z .$$
Moreover, using (5) we obtain the equations
$$\begin{aligned}
\nabla_{X, J Y}^{2} J & =\nabla_{X, Y}^{2} J \circ J+\nabla_{Y} J \circ \nabla_{X} J-\nabla_{\left(\nabla_{X} J\right) Y} J, \\
\nabla_{X, J Y}^{2} J & =-J \circ \nabla_{X, Y}^{2} J-\nabla_{X} J \circ \nabla_{Y} J-\nabla_{\left(\nabla_{X} J\right) Y} J .
\end{aligned}$$
For endomorphisms $A, B$ of the tangent bundle $T M$, we use the notations
$$[A, B]:=A \circ B-B \circ A \quad, \quad\{A, B\}:=A \circ B+B \circ A$$
for their commutator and anti-commutator, respectively. Then, for any endomorphism $A$ and the almost complex structure $J$, we have the relations
$$[\{A, J\}, J]=0 \quad, \quad\{[A, J], J\}=0 .$$
By (11) and (12), we immediately obtain
$$\left\{\nabla_{X, Y}^{2} J, J\right\}=-\left\{\nabla_{X} J, \nabla_{Y} J\right\} .$$
Let $\left(X_{1}, \ldots, X_{n}\right)$ be any local frame of vector fields on $M$. Then, by $\left(X^{1}, \ldots, X^{n}\right)$ we denote the associated coframe, which, using the convention of summation, is defined by $X^{k}:=g^{k l} X_{l}$, where $\left(g^{k l}\right)$ is the inverse of the matrix $\left(g_{k l}\right)$ with $g_{k l}:=g\left(X_{k}, X_{l}\right)$. Thus, in the case of an orthonormal frame, we have $X^{k}=X_{k}(k=1, \ldots, n)$. In the following we sometimes use orthonormal frames. We remark that (4) is then locally equivalent to
$$\left(\nabla_{X_{k}} J\right) X^{k}=0,$$
implying the equation
$$\left(\nabla_{X, X_{k}}^{2} J\right) X^{k}=0$$
for any vector field $X$. The Ricci tensor is given by
$$\operatorname{Ric}(X):=R\left(X, X_{k}\right) X^{k}$$
and the star Ricci tensor of the almost Kähler manifold $(M, g, J)$ is defined by
$$\operatorname{Ric}_{\star}(X):=R\left(J X, J X_{k}\right) X^{k} .$$
Moreover, we use the notations
$$\begin{aligned}
\operatorname{Ric}^{+} & :=\frac{1}{2}(\operatorname{Ric}-J \circ \operatorname{Ric} \circ J)=-\frac{1}{2} J \circ\{\operatorname{Ric}, J\}, \\
\operatorname{Ric}^{-} & :=\frac{1}{2}(\operatorname{Ric}+J \circ \operatorname{Ric} \circ J)=\frac{1}{2} J \circ[\operatorname{Ric}, J], \\
\operatorname{Ric}_{\star}^{+} & :=\frac{1}{2}\left(\operatorname{Ric}_{\star}-J \circ \operatorname{Ric}_{\star} \circ J\right)=-\frac{1}{2} J \circ\left\{\operatorname{Ric}_{\star}, J\right\}, \\
\operatorname{Ric}_{\star}^{-} & :=\frac{1}{2}\left(\operatorname{Ric}_{\star}+J \circ \operatorname{Ric}_{\star} \circ J\right)=\frac{1}{2} J \circ\left[\operatorname{Ric}_{\star}, J\right] .
\end{aligned}$$
By definition, we have
$$\operatorname{Ric}=\operatorname{Ric}^{+}+\operatorname{Ric}^{-} \quad, \quad \operatorname{Ric}_{\star}=\operatorname{Ric}_{\star}^{+}+\operatorname{Ric}_{\star}^{-}$$
and from (13) and (19) - (22) we see that
$$\left[\operatorname{Ric}^{+}, J\right]=\left\{\operatorname{Ric}^{-}, J\right\}=\left[\operatorname{Ric}_{\star}^{+}, J\right]=\left\{\operatorname{Ric}_{\star}^{-}, J\right\}=0 .$$
Obviously, the endomorphisms Ric ${ }^{+}$and Ric ${ }^{-}$are symmetric
$$\left(\operatorname{Ric}^{ \pm}\right)^{*}=\operatorname{Ric}^{ \pm} .$$

Using the first Bianchi identity we find
$$\operatorname{Ric}_{\star}=\frac{1}{2} R\left(X_{k}, J X^{k}\right) \circ J,$$
which implies
$$\left(\operatorname{Ric}_{\star}\right)^{*}=-J \circ \operatorname{Ric}_{\star} \circ J .$$
From (21), (22) and (27) we see that $\mathrm{Ric}_{\star}^{+}$is symmetric and $\mathrm{Ric}_{\star}^{-}$is skew symmetric
$$\left(\operatorname{Ric}^{ \pm}\right)^{*}= \pm \operatorname{Ric}_{\star}^{ \pm} .$$
We remark that in the Kähler case $(\nabla J=0)$ we have Ric $_{\star}=$ Ric and Ric $_{\star}^{-}=$Ric $^{-}=0$. The Ricci form $\rho$ and the star Ricci form $\rho_{\star}$ are defined by
$$\rho(X, Y):=g\left(\left(J \circ \operatorname{Ric}^{+}\right) X, Y\right) \quad \text { and } \quad \rho_{\star}(X, Y):=g\left(\left(J \circ \operatorname{Ric}_{\star}^{+}\right) X, Y\right),$$
respectively. Both Ricci forms are Hermitian ( $J$-invariant)
$$\rho(J X, J Y)=\rho(X, Y) \quad, \quad \rho_{\star}(J X, J Y)=\rho_{\star}(X, Y) .$$
Besides the scalar curvature $S:=\operatorname{tr}(\operatorname{Ric})=\operatorname{tr}\left(\operatorname{Ric}^{+}\right)$also the star scalar curvature $S_{\star}:=$ $\operatorname{tr}\left(\operatorname{Ric}_{\star}\right)=\operatorname{tr}\left(\operatorname{Ric}_{\star}^{+}\right)$is considered. Further, for all $X, Y \in \Gamma(T M)$, we have the curvature endomorphism $\tilde{R}(X, Y)$ defined by
$$\tilde{R}(X, Y):=\frac{1}{4}[R(X, Y)-R(J X, J Y), J] \circ J .$$
We see that $\tilde{R}$ has the properties
$$\tilde{R}(X, Y,)^{*}=-\tilde{R}(X, Y)=\tilde{R}(Y, X),$$
$$\{\tilde{R}(X, Y), J\}=0$$
$$\tilde{R}(J X, J Y)=-\tilde{R}(X, Y) .$$
$\tilde{R}(X, Y)$ decomposes as follows
$$\tilde{R}(X, Y)=\tilde{R}^{+}(X, Y)+\tilde{R}^{-}(X, Y),$$
where $\tilde{R}^{+}$and $\tilde{R}^{-}$are given by
$$\tilde{R}^{ \pm}(X, Y):=\frac{1}{2}(\tilde{R}(X, Y) \pm \tilde{R}(J X, Y) \circ J) .$$
Obviously, $\tilde{R}^{+}$and $\tilde{R}^{-}$also have the properties (30) - (32) and it holds that
$$\tilde{R}^{ \pm}(J X, Y) \circ J= \pm \tilde{R}^{ \pm}(X, Y) .$$
Using (11), (12) a straightforward calculation yields the relation
$$\tilde{R}^{+}(X, Y)=\frac{1}{4} \nabla_{\varphi(X, Y)} J,$$
where $\varphi$ is the vector-valued 2-form defined by $\varphi(X, Y):=\left(\nabla_{X} J\right) Y-\left(\nabla_{Y} J\right) X$. Using (5) and (9) it is easy to see that $\varphi$ has the properties
$$\varphi(J X, J Y)=-\varphi(X, Y),$$
$$\varphi(J X, Y)=\varphi(X, J Y)=-J(\varphi(X, Y)) .$$
Furthermore, from (6) we derive
$$\nabla_{\varphi(X, Y)} J=-g\left(\left(\nabla_{X_{k}} J\right) X, Y\right) \cdot \nabla_{X^{k}} J .$$

Inserting (38) into (35) we obtain Gray's identity [15]
$$\tilde{R}^{+}=-\frac{1}{4} \nabla_{X_{k}} \Omega \otimes \nabla_{X^{k}} J .$$
It is well known that $\tilde{R}^{-}$is already determined by the Weyl tensor. Let $\widetilde{\text { Ric }}$ be the endomorphism of $T M$ locally defined by $\widehat{\operatorname{Ric}}(X):=\tilde{R}\left(X, X_{k}\right) X^{k}$. Using (33) and (34) we obtain
$$\widetilde{\operatorname{Ric}}(X)=\tilde{R}^{+}\left(X, X_{k}\right) X^{k} .$$
By (39) and (40), we find
$$\widetilde{\text { Ric }}=-\frac{1}{4} \nabla_{X_{k}} J \circ \nabla_{X^{k}} J .$$
Thus, $\widetilde{\text { Ric }}$ is symmetric and semi-positive
$$(\widetilde{\mathrm{Ric}})^{*}=\widehat{\mathrm{Ric}},$$
$$\widetilde{\operatorname{Ric}} \geq 0 .$$
Moreover, $\widetilde{\text { Ric }}$ commutes with the almost complex structure
$$[\widetilde{\mathrm{Ric}}, J]=0 .$$
In the following we use the Bochner Laplacian $\nabla^{*} \nabla$ locally given by $\nabla^{*} \nabla:=-\nabla_{X_{k}, X^{k}}^{2}$. From (14) and (42) we immediately obtain
$$\left\{\nabla^{*} \nabla J, J\right\}=-8 \widetilde{\operatorname{Ric}}$$
and using (16) we find
$$\left(\nabla_{X_{k}, X}^{2} J\right) X^{k}=\left(J \circ \operatorname{Ric}-\operatorname{Ric}_{\star} \circ J\right) X .$$
Further, (6) implies the equation
$$g\left(\left(\nabla_{V, X}^{2} J\right) Y, Z\right)+g\left(\left(\nabla_{V, Z}^{2} J\right) X, Y\right)+g\left(\left(\nabla_{V, Y}^{2} J\right) Z, X\right)=0,$$
which is valid for all vector fields $V, X, Y, Z$. Contracting this equation and using (19), (27), (46) we obtain
$$\nabla^{*} \nabla J=2\left(\text { Ric }_{\star}-\text { Ric }^{+}\right) \circ J .$$
By (45), (48) and (21), we find the identity
$$\widetilde{\operatorname{Ric}}=\frac{1}{2}\left(\operatorname{Ric}_{\star}^{+}-\operatorname{Ric}^{+}\right) .$$
Multiplying (46) by $J$ and using (23), (27) and ( 28) we obtain
$$\left(J \circ \nabla_{X_{k}, X}^{2} J\right) X^{k}=\left(\operatorname{Ric}_{\star}^{+}-\operatorname{Ric}^{+}\right) X-\left(\operatorname{Ric}_{\star}^{-}+\operatorname{Ric}^{-}\right) X .$$
For endomorphisms $A, B$ of the tangent bundle $T M$, we use the scalar product $\langle A, B\rangle:=$ $\operatorname{tr}\left(A \circ B^{*}\right)$. On the other hand, the scalar product of 2-forms $\xi, \eta$ is defined by $\langle\xi, \eta\rangle:=$ $\frac{1}{2} \xi\left(X_{k}, X_{l}\right) \cdot \eta\left(X^{k}, X^{l}\right)$. By (42), the trace of (49) yields the well known equation
$$S_{\star}-S=|\nabla \Omega|^{2} .$$
Let $\phi$ be the (0, 2)-tensor field on $M$ defined by
$$\phi(X, Y):=\frac{1}{2} \operatorname{tr}\left(\nabla_{X} J \cdot \nabla_{J Y} J\right)=-\frac{1}{2}\left\langle\nabla_{X} J, \nabla_{J Y} J\right\rangle .$$
Using (5) and (9) we see that $\phi$ has the properties
$$\phi(X, Y)=\phi(J X, J Y)=-\phi(Y, X) .$$

Thus, $\phi$ is a $J$-invariant 2-form. Moreover, by definition, it holds that
$$\phi(X, J Y)=\left\langle\nabla_{X} \Omega, \nabla_{Y} \Omega\right\rangle .$$
Gray's identity (39) provides
$$\left|\tilde{R}^{+}\right|^{2}=\frac{1}{2}|\phi|^{2} .$$
By (33) and (34), this implies
$$|\tilde{R}|^{2}=\frac{1}{2}|\phi|^{2}+\left|\tilde{R}^{-}\right|^{2} .$$
An $\Omega$-contraction of equation (47) yields
$$g\left(\left(\nabla_{X, X_{k}}^{2} J\right) J X^{k}, Y\right)=\frac{1}{2} \operatorname{tr}\left(J \circ \nabla_{X, Y} J\right) .$$
Furthermore, by (14) we find
$$\frac{1}{2} \operatorname{tr}\left(J \circ \nabla_{X, Y}^{2} J\right)=\phi(X, J Y) .$$
On the other hand, using (14), (15), (16) we have
$$\left(\nabla_{X, X_{k}}^{2} J\right) J X^{k}=-\left(\nabla_{X_{k}} J \circ \nabla_{X} J\right) X^{k} .$$
By (56) and (57), this provides the identity
$$g\left(\left(\nabla_{X_{k}} J \circ \nabla_{X} J\right) X^{k}, Y\right)=-\phi(X, J Y) .$$

\section*{2. Weitzenböck formulas}

Let $(M, g, J)$ be any almost Kähler manifold. By Proposition 1 in [5] and (55), there is a vector field $V_{1}$ on $M$ such that
$$\frac{1}{2}\left|\nabla^{*} \nabla \Omega\right|^{2}+|\tilde{R}|^{2}-\mid \text { Ric }\left.^{-}\right|^{2}+2\left\langle\rho, \nabla^{*} \nabla \Omega\right\rangle-2\langle\rho, \phi\rangle+\operatorname{div}\left(V_{1}\right)=0 .$$
In contrast to the paper [5] the definition $|\tilde{R}|^{2}:=\sum_{k, l}\left|\tilde{R}\left(X_{k}, X_{l}\right)\right|^{2}$ is used here. The authors show that Sekigawa's theorem is an immediate consequence of the basic Weitzenböck formula (60). In the following we modify this formula in order to obtain some more general results.

Lemma 2.1. For any almost Kähler manifold, we have the equations
$$\begin{gathered}
2\langle\rho, \phi\rangle=\left\langle\nabla_{\operatorname{Ric}\left(X_{k}\right)} \Omega, \nabla_{X^{k}} \Omega\right\rangle, \\
\left\langle\rho, \nabla^{*} \nabla \Omega\right\rangle=2\langle\text { Ric }, \widetilde{\text { Ric }}\rangle
\end{gathered}$$

Proof. We calculate
$$\begin{aligned}
& 2\langle\rho, \phi\rangle=\rho\left(X^{k}, X^{l}\right) \cdot \phi\left(X_{k}, X_{l}\right)=\frac{1}{2} g\left(\left(J \circ \operatorname{Ric}^{+}\right) X^{k}, X^{l}\right) \cdot \operatorname{tr}\left(\nabla_{X_{k}} J \circ \nabla_{J X_{l}} J\right)= \\
& =\frac{1}{2} \operatorname{tr}\left(\nabla_{X_{k}} J \circ \nabla_{J\left(\left(J \circ \operatorname{Ric}^{+}\right) X^{k}\right)} J\right)=\phi\left(X_{k},\left(J \circ \operatorname{Ric}^{+}\right) X^{k}\right) \stackrel{[52]}{=} \\
& =\phi\left(X_{k},(J \circ \operatorname{Ric}) X^{k}\right) \stackrel{[53]}{=}\left\langle\nabla_{X_{k}} \Omega, \nabla_{\operatorname{Ric}\left(X^{k}\right)} \Omega\right\rangle .
\end{aligned}$$
This proves (61). Further, we have
$$\left\langle\rho, \nabla^{*} \nabla \Omega\right\rangle=\frac{1}{2}\left\langle J \circ \mathrm{Ric}^{+}, \nabla^{*} \nabla J\right\rangle=-\frac{1}{4}\left\langle\mathrm{Ric}^{+},\left\{\nabla^{*} \nabla J, J\right\}\right\rangle \stackrel{\text { 45 }}{=} 2\left\langle\mathrm{Ric}^{+}, \widetilde{\operatorname{Ric}}\right\rangle .$$

This yields (62) since $\left\langle\right.$ Ric $\left.^{-}, \widetilde{\text { Ric }}\right\rangle=0$ by (24) , (44). \(\square\)

We introduce the vector-valued 2-form $\psi$ defined by
$$\psi(X, Y):=\frac{1}{8}\left(\left[\nabla_{X} \operatorname{Ric}, J\right] Y-\left[\nabla_{Y} \operatorname{Ric}, J\right] X-\left[\nabla_{J X} \operatorname{Ric}, J\right] J Y+\left[\nabla_{J Y} \operatorname{Ric}, J\right] J X\right) .$$
A simple calculation using (36) , (37) provides the equation
$$\frac{1}{4} g\left(J\left(\varphi\left(X^{k}, X^{l}\right)\right),\left(\nabla_{X_{k}} \operatorname{Ric}\right) X_{l}-\left(\nabla_{X_{l}} \operatorname{Ric}\right) X_{k}\right)=\langle\varphi, \psi\rangle$$
with $\langle\varphi, \psi\rangle:=\frac{1}{2} g\left(\varphi\left(X^{k}, X^{l}\right), \psi\left(X_{k}, X_{l}\right)\right)$.

Lemma 2.2. For any almost Kähler manifold, it holds that
$$2\langle\operatorname{Ric}, \widetilde{\operatorname{Ric}}\rangle=2\langle\rho, \phi\rangle+2\langle\varphi, \psi\rangle+\left|\operatorname{Ric}^{-}\right|^{2}+\operatorname{div}\left(V_{2}\right),$$
where $V_{2}$ is the vector field locally defined by
$$V_{2}:=g\left(\operatorname{Ric}\left(X^{l}\right),\left(J \circ \nabla_{X_{l}} J\right) X^{k}\right) \cdot X_{k} .$$

Proof. We calculate
$2\langle$ Ric,$\widetilde{\text { Ric }}\rangle \stackrel{\text { 49 }}{=}\left\langle\right.$ Ric, Ric $_{\star}^{+}-$Ric $\left.^{+}\right\rangle \stackrel{[50]}{\equiv}$
$$=\left\langle\operatorname{Ric}^{-} \operatorname{Ric}_{\star}^{-}+\operatorname{Ric}^{-}\right\rangle+g\left(\operatorname{Ric}\left(X^{l}\right),\left(J \circ \nabla_{X_{k}, X_{l}} J\right) X^{k}\right) .$$
By $\left\langle\right.$ Ric $^{\prime}$ Ric $\left._{\star}^{-}\right\rangle=\left\langle\right.$Ric $^{+}$, Ric $\left.^{-}\right\rangle=0$, this yields
$$2\langle\operatorname{Ric}, \widetilde{\operatorname{Ric}}\rangle=\left|\operatorname{Ric}^{-}\right|^{2}+g\left(\operatorname{Ric}\left(X^{l}\right),\left(J \circ \nabla_{X_{k}, X_{l}} J\right) X^{k}\right)$$
Let $x \in M$ be any point and $\left(X_{1}, \ldots, X_{n}\right)$ an orthonormal frame in neighbourhood of $x$ with $\left(\nabla X_{k}\right)_{x}=0$ for $k=1, \ldots, n$. Then, at $x \in M$, we have
$$\begin{aligned}
& g\left(\operatorname{Ric}\left(X^{l}\right),\left(J \circ \nabla_{X_{k}, X_{l}}^{2} J\right) X^{k}\right)=X_{k}\left(g\left(\operatorname{Ric}\left(X^{l}\right),\left(J \circ \nabla_{X_{l}} J\right) X^{k}\right)\right)- \\
& -g\left(\operatorname{Ric}\left(X^{l}\right),\left(\nabla_{X_{k}} J \circ \nabla_{X_{l}} J\right) X^{k}\right)-g\left(\left(\nabla_{X_{k}} \operatorname{Ric}\right) X^{l},\left(J \circ \nabla_{X_{l}} J\right) X^{k}\right) \stackrel{[59],(5),(9)}{=} \\
= & \operatorname{div}\left(V_{2}\right)+\phi\left(X_{l},(J \circ \operatorname{Ric}) X^{l}\right)-g\left(J\left(\left(\nabla_{X^{l}} J\right) X^{k}-\left(\nabla_{X^{k}} J\right) X^{l}\right),\left(\nabla_{X_{k}} \operatorname{Ric}\right) X_{l}\right) \stackrel{[53}{=} \\
= & \operatorname{div}\left(V_{2}\right)+\left\langle\nabla_{X_{l}} \Omega, \nabla_{\operatorname{Ric}\left(X^{l}\right)} \Omega\right\rangle+g\left(J\left(\varphi\left(X^{k}, X^{l}\right)\right),\left(\nabla_{X_{k}} \operatorname{Ric}\right) X_{l}\right) \stackrel{[61]}{=} \\
= & \operatorname{div}\left(V_{2}\right)+2\langle\rho, \phi\rangle+\frac{1}{2} g\left(J\left(\varphi\left(X^{k}, X^{l}\right)\right),\left(\nabla_{X_{k}} \operatorname{Ric}\right) X_{l}-\left(\nabla_{X_{l}} \operatorname{Ric}\right) X_{k}\right) \stackrel{63}{=} \\
= & \operatorname{div}\left(V_{2}\right)+2\langle\rho, \phi\rangle+2\langle\varphi, \psi\rangle
\end{aligned}$$
and, hence,
$$g\left(\operatorname{Ric}\left(X^{l}\right),\left(J \circ \nabla_{X_{k}, X_{l}}^{2} J\right) X^{k}\right)=2\langle\rho, \phi\rangle+2\langle\varphi, \psi\rangle+\operatorname{div}\left(V_{2}\right) .$$
Inserting (2*) into (*) we obtain (64). \(\square\)

Using (48), (49) and $\langle$ Ric, $\widetilde{\text { Ric }}\rangle=\left\langle\right.$ Ric $\left.^{+}, \widetilde{\text { Ric }}\right\rangle$ we obtain by straightforward calculations

Lemma 2.3. The identities
$$\frac{1}{2}\left|\nabla^{*} \nabla \Omega\right|^{2}=\left|\operatorname{Ric}_{\star}^{-}\right|^{2}+4\left|\widetilde{\operatorname{Ric}^{2}}\right|^{2},$$
$$|\widetilde{\operatorname{Ric}}|^{2}+\langle\operatorname{Ric}, \widetilde{\operatorname{Ric}}\rangle=\frac{1}{4}\left(\left|\operatorname{Ric}_{\star}^{+}\right|^{2}-\left|\operatorname{Ric}^{+}\right|^{2}\right),$$
$$2|\widetilde{\operatorname{Ric}}|^{2}+\langle\operatorname{Ric}, \widetilde{\operatorname{Ric}}\rangle=\left\langle\operatorname{Ric}_{\star}^{+}, \widetilde{\operatorname{Ric}}\right\rangle$$
are valid for any almost Kähler manifold.

Lemma 2.4. Let $(M, g, J)$ be any almost Kähler manifold. Then we have the equations
$$|\tilde{R}|^{2}+\left|\operatorname{Ric}_{\star}\right|^{2}-|\operatorname{Ric}|^{2}-2\langle\rho, \phi\rangle+\operatorname{div}\left(V_{1}\right)=0,$$
$$|\tilde{R}|^{2}+\left|\operatorname{Ric}_{\star}^{-}\right|^{2}+2\left\langle\operatorname{Ric}_{\star}^{+}, \widehat{\operatorname{Ric}}\right\rangle+2\langle\varphi, \psi\rangle+\operatorname{div}\left(V_{1}+V_{2}\right)=0 .$$

Proof. Inserting (62) and (65) into (60) we find (68) using (66). We eliminate the term $2\langle\rho, \phi\rangle$ in (68) by (64) and then we obtain (69) using (66) , (67). \(\square\)

Let $(M, g, J)$ be any almost Hermitian $n$-manifold. Then we consider the function $q(J)$ locally defined by
$$q(J):=g\left(\left(\nabla_{X_{k}, X_{l}}^{2} \operatorname{Ric}\right) J X^{k}, J X^{l}\right) .$$
Obviously, it holds that
$$q(J)=\frac{1}{2} g\left(\left(\nabla_{X_{k}, X_{l}}^{2} \operatorname{Ric}+\nabla_{X_{l}, X_{k}}^{2} \operatorname{Ric}\right) J X^{k}, J X^{l}\right)=\frac{1}{2} g\left(\left(\nabla_{J X_{k}, J X_{l}}^{2} \operatorname{Ric}+\nabla_{J X_{l}, J X_{k}}^{2} \operatorname{Ric}\right) X^{k}, X^{l}\right) .$$
If $M$ is compact, then we consider the number
$$Q(J):=\int_{M} q(J) \omega,$$
where $\omega:=\frac{1}{m!} \Omega^{m}(n=2 m)$ is the volume form. Since in the Kähler case $\left[\nabla^{2} \operatorname{Ric}, J\right]=0$, i.e., $\left[\nabla_{X, Y}^{2} R i c, J\right]=0$ for all vector fields $X$ and $Y$, we have
$$q(J)=g\left(\left(\nabla_{X_{k}, X_{l}}^{2} \operatorname{Ric}\right) X^{k}, X^{l}\right)=-\frac{1}{2} \Delta S$$
then and, hence, $Q(J)=0$. Thus, $Q(J)$ is an obstruction against the Kähler property of any compact almost Hermitian manifold. Furthermore, if $(M, g, J)$ is almost Kähler, then a simple calculation yields
$$q(J)=2\langle\varphi, \psi\rangle+\operatorname{div}\left(V_{3}\right),$$
where $V_{3}$ is the vector field on $M$ locally given by $V_{3}:=g\left(\left(\nabla_{X_{l}} \operatorname{Ric}\right) J X^{l}, J X^{k}\right) \cdot X_{k}$. This implies
$$Q(J)=2 \int_{M}\langle\varphi, \psi\rangle \omega .$$
By (72), Lemma 2.4 provides immediately

Proposition 2.5. For any compact almost Kähler manifold, the equations
$$\begin{gathered}
\int_{M}\left(|\tilde{R}|^{2}+\mid \text { Ric }\left._{\star}\right|^{2}-\mid \text { Ric }^{2}-2\langle\rho, \phi\rangle\right) \omega=0, \\
Q(J)+\int_{M}\left(|\tilde{R}|^{2}+\mid \text { Ric }\left._{\star}^{-}\right|^{2}+2\left\langle\text { Ric }_{\star}^{+}, \widetilde{\text { Ric }^{\prime}}\right\rangle\right) \omega=0
\end{gathered}$$
are valid.

\section*{3. Applications}

For any almost Kähler manifold, it is very natural to compare the tensors $\mathrm{Ric}_{\star}^{+}$and $\mathrm{Ric}^{+}$since both tensors are symmetric, Hermitian and coincide with the Ricci tensor in the Kähler case. In particular, a necessary condition for an almost Kähler manifold to be Kähler is that $\mathrm{Ric}_{\star}^{+}$ and $\mathrm{Ric}^{+}$have the same length $\left(\left|\mathrm{Ric}_{\star}^{+}\right|=\left|\mathrm{Ric}^{+}\right|\right)$.

Proposition 3.1. Let $(M, g, J)$ be an almost Kähler manifold with $\mid$ Ric $_{\star}^{+}|=|$Ric $^{+} \mid$. Then $(M, g, J)$ is Kähler if Ric or $\operatorname{Ric}^{+}$is semi-positive or if $\mathrm{Ric}_{\star}^{+}$is semi-negative.

Proof. Since $\langle$ Ric,$\widetilde{\text { Ric }}\rangle=\left\langle\right.$ Ric $\left.^{+}, \widetilde{\text { Ric }}\right\rangle$ and $\widetilde{\text { Ric }} \geq 0$, our supposition Ric $\geq 0$ or Ric ${ }^{+} \geq 0$, respectively, implies $\langle$ Ric, $\widetilde{\text { Ric }}\rangle \geq 0$. Thus, the assumption $\mid$ Ric $_{\star}^{+}|=|$Ric $^{+} \mid$forces $\widetilde{\text { Ric }}=0$ by (66). Using (66) and (67) we immediately obtain the equation
$$\left\langle\text { Ric }_{\star}^{+}, \widetilde{\operatorname{Ric}}\right\rangle-\left|\widetilde{\text { Ric }^{2}}\right|^{2}=\frac{1}{4}\left(\mid \text { Ric }\left._{\star}^{+}\right|^{2}-\mid \text { Ric }\left.^{+}\right|^{2}\right) .$$
This shows that the suppositions $\mid$ Ric $_{\star}^{+}|=|$Ric $^{+} \mid$and Ric $_{\star}^{+} \leq 0$ also force $\widetilde{\text { Ric }}=0$. By (41), we have $\operatorname{tr}(\widetilde{\text { Ric }})=\frac{1}{4}|\nabla J|^{2}$. Thus, $\widetilde{\text { Ric }}=0$ implies $\nabla J=0$. \(\square\)

In dimension 4, we have the following stronger result.

Proposition 3.2. Let $(M, g, J)$ be an almost Kähler 4-manifold such that $\mathrm{Ric}_{\star}^{+}$and $\mathrm{Ric}^{+}$have the same length. Then $(M, g, J)$ is Kähler if $S \geq 0$ or $S_{\star} \leq 0$ or if $\operatorname{supp}\left(S+S_{\star}\right)=M$.

Proof. It is known that, for any almost Kähler 4-manifold, the endomorphism $\nabla_{X_{k}} J \circ \nabla_{X^{k}} J$ is a multiple of the identity map [28]. By (41), this yields
$$\widetilde{\text { Ric }}=\frac{1}{8}|\nabla \Omega|^{2} .$$
Inserting (76) into (66) and (75) we obtain the equations
$$4\left(\left|\operatorname{Ric}_{\star}^{+}\right|^{2}-\left|\operatorname{Ric}^{+}\right|^{2}\right)=|\nabla \Omega|^{4}+2 S \cdot|\nabla \Omega|^{2}=2 S_{\star} \cdot|\nabla \Omega|^{2}-|\nabla \Omega|^{4},$$
which provide
$$4\left(\left|\operatorname{Ric}_{\star}^{+}\right|^{2}-\left|\operatorname{Ric}^{+}\right|^{2}\right)=\left(S+S_{\star}\right) \cdot|\nabla \Omega|^{2} .$$
Obviously, our suppositions imply $\nabla \Omega=0$ by (77), (78). \(\square\)

Another necessary condition for an almost Kähler manifold to be Kähler is $\mid$ Ric $_{\star}|=|$ Ric $\mid$. The following theorem shows that this condition is also sufficient in the compact case with seminegative Ricci tensor (Ric $\leq 0$ ).

Theorem 3.3. Let $(M, g, J)$ be any compact almost Kähler manifold such that at least one of the tensors Ric, Ric ${ }^{+}$or Ric ${ }_{\star}^{+}$is semi-negative. Then $(M, g, J)$ is Kähler if Ric ${ }_{\star}$ and Ric have the same length.

Proof. It holds that
$$\left\langle\nabla_{\operatorname{Ric}\left(X_{k}\right)} \Omega, \nabla_{X^{k}} \Omega\right\rangle \stackrel{(5),(9)}{=}\left\langle\nabla_{\operatorname{Ric}^{+}\left(X_{k}\right)} \Omega, \nabla_{X^{k}} \Omega\right\rangle \stackrel{\text { 49 }}{=}\left\langle\nabla_{\operatorname{Ric}_{\star}^{+}\left(X_{k}\right)} \Omega, \nabla_{X^{k}} \Omega\right\rangle-2\left\langle\nabla_{\widetilde{\operatorname{Ric}}\left(X_{k}\right)} \Omega, \nabla_{X^{k}} \Omega\right\rangle .$$
By (61), this yields
$$2\langle\rho, \phi\rangle=\left\langle\nabla_{\operatorname{Ric}^{+}\left(X_{k}\right)} \Omega, \nabla_{X^{k}} \Omega\right\rangle=\left\langle\nabla_{\operatorname{Ric}_{\star}^{+}\left(X_{k}\right)} \Omega, \nabla_{X_{k}} \Omega\right\rangle-2\left\langle\nabla_{\widetilde{\operatorname{Ric}}\left(X_{k}\right)} \Omega, \nabla_{X^{k}} \Omega\right\rangle .$$
Using (61) and (79) we see that each of the suppositions Ric $\leq 0, \mathrm{Ric}^{+} \leq 0$ or $\mathrm{Ric}_{\star}^{+} \leq 0$ implies $\langle\rho, \phi\rangle \leq 0$. Thus, by (55) and (73), we obtain the inequality
$$\int_{M}\left(\frac{1}{2}|\phi|^{2}+\left|\tilde{R}^{-}\right|^{2}+\left|\operatorname{Ric}_{\star}\right|^{2}-|\operatorname{Ric}|^{2}\right) \omega \leq 0$$
which provides $\phi=0$ if $\mid$ Ric $_{\star}|=|$ Ric $\mid$. By (53), $\phi=0$ implies $\nabla \Omega=0$. \(\square\)

The application of the integral formula (73) to the Einstein case yields

Theorem 3.4. A compact Einstein almost Kähler $n$-manifold is necessarily Kähler if the inequality
$$\left|\tilde{R}^{-}\right|^{2}+\mid \text { Ric }\left._{\star}\right|^{2} \geq \frac{1}{n} S \cdot S_{\star}$$
is satisfied.

Proof. In the Einstein case of $\mathrm{Ric}=\frac{S}{n}$, we have
$$|\operatorname{Ric}|^{2}+2\langle\rho, \phi\rangle \stackrel{61}{=} \frac{S^{2}}{n}+\frac{S}{n}|\nabla \Omega|^{2} \stackrel{\text { 51 }}{=} \frac{1}{n} S \cdot S_{\star} .$$
Inserting this into (73) we see that (81) forces $\nabla \Omega=0$. \(\square\)

Since inequality (81) is equivalent to
$$\left|\tilde{R}^{-}\right|^{2}+\mid \text { Ric }_{\star}-\left.\frac{S_{\star}}{n}\right|^{2}+\frac{S_{\star}}{n}|\nabla \Omega|^{2} \geq 0,$$
we immediately obtain

Corollary 3.5. Every compact Einstein almost Kähler manifold with non-negative star scalar curvature is Kähler.

This corollary is a slight generalization of Sekigawa's theorem since $S \geq 0$ implies $S_{\star} \geq 0$ by (51).
Concerning the Goldberg conjecture it may be interesting to investigate inequality (81) in suitable geometrical situations with $S<0$.
Now we consider the integral formula (74). The main results of this paper are the following two theorems.

Theorem 3.6. Let $(M, g, J)$ be any compact almost Kähler manifold such that at least one of the tensors Ric, Ric ${ }^{+}$or $\mathrm{Ric}_{\star}^{+}$is semi-positive. Then $J$ is integrable if $Q(J)=0$.

Proof. By (43) and (67), each of the suppositions $\mathrm{Ric} \geq 0, \mathrm{Ric}^{+} \geq 0$ or $\operatorname{Ric}_{\star}^{+} \geq 0$, respectively, implies $\left\langle\right.$ Ric $\left._{\star}^{+}, \widehat{\text { Ric }}\right\rangle \geq 0$. Thus, (74) and $Q(J)=0$ force $\tilde{R}=0$, and, hence, $\nabla \Omega=0$ by (55) and (53). \(\square\)

By (76), equation (74) yields immediately

Theorem 3.7. If $(M, g, J)$ is a compact almost Kähler 4-manifold with $S_{\star} \geq 0$, then $Q(J)=0$ implies $\nabla J=0$.

Remark 3.8. The supposition in Theorem 3.6 that at least one of the tensors Ric, Ric ${ }^{+}$or $\mathrm{Ric}_{\star}^{+}$is semi-positive can be replaced by the weaker condition
$$\left|\tilde{R}^{-}\right|^{2}+\left|\operatorname{Ric}_{\star}^{-}\right|^{2}+2\left\langle\operatorname{Ric}_{\star}^{+}, \widetilde{\operatorname{Ric}}\right\rangle \geq 0 .$$
This condition does not involve any derivatives of the almost complex structure $J$. By (49) , (83) becomes
$$\left|\tilde{R}^{-}\right|^{2}+\left|\operatorname{Ric}_{\star}\right|^{2} \geq\left\langle\operatorname{Ric}_{\star}^{+}, \operatorname{Ric}^{+}\right\rangle .$$
Moreover, in dimension 4, (83) is equivalent to
$$\left|\tilde{R}^{-}\right|^{2}+\left|\operatorname{Ric}_{\star}^{-}\right|^{2}+\frac{S_{\star}}{4}|\nabla \Omega|^{2} \geq 0 .$$
In the Kähler case, these inequalities are satisfied trivially.

Remark 3.9. (i) The condition
$$[\nabla \operatorname{Ric}, J]=0,$$
i.e., $\left[\nabla_{X} \operatorname{Ric}, J\right]=0$ for all vector fields $X$, implies $\psi=0$ and, hence, $Q(J)=0$ by (72). Obviously, any Kähler manifold satisfies this condition.
(ii) By (70), the condition
$$\left[\nabla_{X, Y}^{2} \operatorname{Ric}+\nabla_{Y, X}^{2} \operatorname{Ric}, J\right]=0$$
yields $q(J)=-\frac{1}{2} \Delta S$ and, hence, $Q(J)=0$. In particular, the stronger supposition that $\left[\nabla^{2} \operatorname{Ric}, J\right]=0$ forces $Q(J)=0$. Again, any Kähler manifold fulfils this condition.
(iii) The second one of the equations (70) shows that
$$\nabla_{J X, J Y}^{2} \operatorname{Ric}+\nabla_{J Y, J X}^{2} \operatorname{Ric}=\nabla_{X, Y}^{2} \operatorname{Ric}+\nabla_{Y, X}^{2} \operatorname{Ric}$$
implies $Q(J)=0$.
(iv) Using (63) a simple calculation yields that the supposition
$$\left(\nabla_{X} \operatorname{Ric}\right) Y-\left(\nabla_{Y} \operatorname{Ric}\right) X=\frac{1}{2(n-1)}(X(S) Y-Y(S) X)$$
provides $\langle\varphi, \psi\rangle=0$ and, hence, $Q(J)=0$ by (72).
It is well known that, for dimension $n \geq 4$, (89) is equivalent to the condition that the Weyl tensor $W$ is divergence-free or co-closed $(\delta W=0)$. Since $\delta W=0$ implies $d W=0$ (second Bianchi identity for $W$ ), $W$ is also called harmonic in this case. Examples of Riemannian manifolds with harmonic Weyl tensor are given in [7], Chapter 16.D. Such manifolds are also called nearly conformally symmetric.
(v) A straightforward calculation shows that (89) implies
(90)
$$\nabla_{X, Y}^{2} \operatorname{Ric}+\nabla_{Y, X}^{2} \operatorname{Ric}=\left(\nabla_{X, \cdot}^{2} \operatorname{Ric}\right) Y+\left(\nabla_{Y, \cdot}^{2} \text { Ric }\right) X+\frac{1}{2(n-1)}\left(2 \nabla_{X, Y}^{2} S-\nabla_{X} d S \otimes Y-\nabla_{Y} d S \otimes X\right)$$
Inserting this into (70) we find $q(J)=-\frac{1}{2(n-1)} \Delta S$. Thus, (90) forces $Q(J)=0$.

Remark 3.9 yields some possibilities for concrete applications of our main theorems. The simplest case of application is the situation with parallel Ricci tensor in which each of the conditions (86) - (90) is satisfied trivially. By Remark 3.9 (i), the following corollaries are immediate consequences of Theorem 3.6 and Theorem 3.7 respectively.

Corollary 3.10. Let $(M, g, J)$ be any compact almost Kähler manifold such that at least one of the tensors Ric, Ric ${ }^{+}$or Ric ${ }_{\star}^{+}$is semi-positive. Then $[\nabla \mathrm{Ric}, J]=0$ implies $\nabla J=0$.

Corollary 3.11. Every compact almost Kähler 4-manifold $(M, g, J)$ with $S_{\star} \geq 0$ and $[\nabla \operatorname{Ric}, J]=$ 0 is Kähler.

Our Corollary 3.10 is a generalization of Sekigawa's theorem. It shows that the assertion of this theorem is true not only for compact Einstein manifolds of non-negative scalar curvature but also for Riemannian products of such manifolds. It seems that condition (89) is a suitable generalization of the supposition that $\nabla$ Ric $=0$ for our purposes. But this is not the case by the fact that the Ricci tensor of a Kähler manifold with harmonic Weyl tensor is parallel ([7], 16.30 Prop.). Thus, every almost Kähler manifold with harmonic Weyl tensor and non-parallel Ricci tensor cannot be Kähler and, hence, is strictly almost Kähler by definition. Taking into account this fact, by Remark 3.9 (iv) and Theorem 3.6 we immediately obtain

Corollary 3.12. A compact almost Hermitian manifold of dimension $n \geq 4$ with harmonic Weyl tensor and non-parallel, semi-positive Ricci tensor cannot be almost Kähler.

Finally, Theorem 3.7 implies

Corollary 3.13. Every compact almost Hermitian 4-manifold with harmonic Weyl tensor, non-parallel Ricci tensor and non-negative scalar curvature is not almost Kähler.

In particular, Corollary 3.13 shows that there are no compact almost Kähler 4-manifolds with harmonic Weyl tensor and non-constant, non-negative scalar curvature.

\section*{References}
\begin{itemize}
\item[] [1] B. Alexandrov, G. Grancharov and S. Ivanov, Curvature properties of twistor spaces of quaternionic Kähler manifolds, J. Geom. 62 (1998), 1-12.
\item[] [2] V. Apostolov and J. Armstrong, Symplectic 4-manifolds with Hermitian Weyl tensor, Trans. Amer. Math. Soc. 352 (2000), 4501-4513.
\item[] [3] V. Apostolov, J. Armstrong and T. Drăghici, Local ridigity of certain classes of almost Kähler 4-manifolds, Ann. Glob. Anal. Geom. 21 (2002), 151-176.
\item[] [4] V. Apostolov and T. Drăghici, Almost Kähler 4-manifolds with $J$-invariant Ricci tensor and special Weyl tensor, Quart. J. Math. 51 (2000), 275-294.
\item[] [5] V. Apostolov, T. Drăghici and A. Moroianu, A splitting theorem for Kähler manifolds with constant eigenvalues of the Ricci tensor, Int. Math. 12 (2001), 769-789.
\end{itemize}
[6] J. Armstrong, An ansatz for almost-Kähler, Einstein 4-manifolds, J. reine angew. Math. 542 (2002), 53-84.
[7] A. L. Besse, Einstein manifolds, Springer Verlag, Berlin, 1987.
[8] A. L. Cordero, M. Fernandez and M. de Leon, Examples of compact non-Kähler almost Kähler manifolds, Proc. Amer. Math. Soc. 95 (1985), 282-286.
[9] D. E. Blair and S. Ianus, Critical associated metrics on symplectic manifolds, Contemp. Math. 51 (1986), 23-29.
[10] J. Davidov and O. Muskarov, Twistor spaces with Hermitian Ricci tensor, Proc. Amer. Math. Soc. 109 (1990), 1115-1120.
[11] T. Drăghici, On the almost Kähler manifolds with Hermitian Ricci tensor, Houston J. of Math. 20 (1994), 293-298.
[12] T. Drăghici, On some 4-dimensional almost Kähler manifolds, Kodai Math. J. 18 (1995), 156-163.
[13] T. Drăghici, Almost Kähler 4-manifolds with $J$-invariant Ricci tensor, Houston J. Math. 25 (1999), 133-145.
[14] S. I. Goldberg, Integrability of almost Kähler manifolds, Proc. Amer. Math. Soc. 21 (1969), 96-100.
[15] A. Gray, Curvature identities for Hermitian and almost Hermitian manifolds, Tohôku Math. J., 28 (1976), 601-612.
[16] W. Jelonek, Some simple examples of almost Kähler non-Kähler structures, Math. Ann. 305 (1996), 639-649.
[17] J. F. T. Lopera, A family of constant non-Kähler manifolds which admit semi-Kähler or almost-Kähler structures, Boll. Un. Mat. Ital. 5A (1986), 353-360.
[18] N. Murakoshi, T. Oguro and K. Sekigawa, Four-dimensional almost Kähller locally symmetric spaces, Diff. Geom. Appl. 6 (1996), 237-244.
[19] T. Oguro, Examples of non-Kähler almost Kähler symmetric spaces, C.R. Math. Rep. Acad. Sci. Canada 18 (1996), 243-246.
[20] T. Oguro, On some compact almost Kähler locally symmetric spaces, Internat. J. Math. Sci. 21 (1998), 69-72.
[21] T. Oguro and K. Sekigawa, Four-dimensional almost Kähler Einstein and *-Einstein manifolds, Geom. Dedicata 69 (1998), 91-112.
[22] T. Oguro and K. Sekigawa, On some four-dimensional almost Kähler Einstein manifolds, Kodai Math. J. 24 (2001), 226-258.
[23] T. Oguro, K. Sekigawa and A. Yamada, Four-dimensional almost Kähler Einstein and weakly *-Einstein manifolds, Yokohama Math. J. 47 (1999), 75-92.
[24] T. Sato, An example of an almost Kähler manifold with pointwise constant holomorphic sectional curvature, Tokyo J. Math. 23 (2000), 387-401.
[25] H. Satoh, Compact almost Kähler manifolds with divergence-free Weyl conformal tensor, Preprint (2003).
[26] K. Sekigawa, On some 4-dimensional compact Einstein almost Kähler manifolds, Math. Ann. 271 (1985), 333-337.
[27] K. Sekigawa, On some compact Einstein almost Kähler manifolds, J. Math. Soc. Japan 39 (1987), 677-684.
[28] K. Sekigawa, On some 4-dimensional compact almost Hermitian manifolds, J. Ramanujan Math. Soc. 2 (2) (1987), 101-116.
[29] F. Tricerri, L. Vanhecke, Curvature tensors on almost Hermitian manifolds, Trans. Amer. Math. Soc., 267 (1981), 365-398.
[30] W. P. Thurston, Some simple examples of symplectic manifolds, Proc. Amer. Math. Soc. 55 (1976), 467-468.
[31] B. Watson, New examples of stricly almost Kähler manifolds, Proc. Amer. Math. Soc. 88 (1983), 541-544.