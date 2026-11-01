---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: Kodaira_dimension_of_almost_Kähler_manifolds_and_curvature_of_the_canonical_conn_de6c7952cd4e.pdf
converter: mathpix
format: mmd
---

\title{
KODAIRA DIMENSION OF ALMOST KÄHLER MANIFOLDS AND CURVATURE OF THE CANONICAL CONNECTION
}

\author{
ANDREA CATTANEO, ANTONELLA NANNICINI, AND ADRIANO TOMASSINI
}

\begin{abstract}
The notion of Kodaira dimension has recently been extended to general almost complex manifolds. In this paper we focus on the Kodaira dimension of almost Kähler manifolds, providing an explicit computation for a family of almost Kähler threefolds on the differentiable manifold underlying a Nakamura manifold. We concentrate also on the link between Kodaira dimension and the curvature of the canonical connection of an almost Kähler manifold, and show that in the previous example (and in another one obtained from a Kodaira surface) the Ricci curvature of the almost Kähler metric vanishes for all the members of the family.
\end{abstract}

\section*{Contents}
1. Introduction ..... 1
2. Kodaira dimension of almost complex manifolds ..... 3
3. Recaps on the canonical connection on almost complex manifolds ..... 4
3.1. Generalities on connections ..... 4
3.2. The type of a form with values in a bundle ..... 5
3.3. Connections on the tangent bundle ..... 6
3.4. The case of almost Hermitian manifolds ..... 6
3.5. The complex formalism ..... 9
4. The Kodaira-Thurston manifold ..... 10
4.1. An alternative derivation of the connection forms ..... 12
4.2. Complex curvature of the canonical connection ..... 13
5. Kodaira dimension of completely solvable Nakamura manifolds ..... 14
5.1. Kodaira dimension of a deformation of Nakamura manifolds ..... 17
5.2. Ricci and scalar curvature of the deformed Nakamura manifold ..... 19
References ..... 22

\section*{1. Introduction}

When studying complex manifolds, one of the first invariants one can attach to any given complex manifold is its Kodaira dimension. This invariant captures the geometry of the manifold $X$ under consideration expressing the rate of growth of the plurigenera $P_{m}(X)=\operatorname{dim}_{\mathbb{C}} H^{0}\left(X, \mathscr{K}_{X}^{\otimes m}\right)$ with respect to $m$. The definition of the Kodaira dimension has recently been extended by Chen-Zhang in the setting of almost complex manifolds (see [CZ18]). Among the main points addressed in this paper, there are two which, according to us, deserve particular attention: first of

\footnotetext{
2010 Mathematics Subject Classification. 53C55, 53C25.
Key words and phrases. Kodaira dimension, almost complex manifolds, almost Kähler manifolds, canonical connection.
This work was partially supported by the Project PRIN "Varietà reali e complesse: geometria, topologia e analisi armonica" and by GNSAGA of INdAM. Andrea Cattaneo is also supported by the 'Grant de Bartolomeis', a fellowship in memory of Prof. Paolo de Bartolomeis.
}
all the proof that the the spaces of sections of the pluricanonical bundles $\mathscr{K}_{X}^{\otimes m}$ are finite dimensional, and then the attention one must pay to properly define what a pseudoholomorphic pluricanonical section is. Regarding these points, up to now the state of the art does not provide tools for the actual computations of the spaces of pluricanonical sections other than the definitions, which makes the determination of the Kodaira dimension of an almost complex manifold extremely challenging.

The aim of the present note is to show some of the features of this extended version of the Kodaira dimension, focussing in particular in the case of (non-integrable) almost Kähler manifolds. We present some results in complex dimension 2 and 3: we endow the differentiable manifolds underlying a Kodaira-Thurston surface and a completely solvable Nakamura threefold with families of almost complex structures and Riemannian metrics turning them into families of almost Kähler manifolds. In particular, we prove the following

Theorem (Theorem 5.5) - There exist a family of almost complex structures $J_{t}$ with $t=\left(t_{1}, t_{2}, t_{3}, t_{4}\right) \in \mathbb{R}^{4}$ on the differentiable manifold $N$ underlying the Nakamura threefold such that
$$\kappa^{J_{t}}(N)= \begin{cases}0 & \text { if } t_{4}=0, \\ -\infty & \text { if } t_{4} \neq 0 .\end{cases}$$

It is known that almost Hermitian manifolds carry a canonical connection on their tangent bundle (in the integrable case, it is the Chern connection). Our second aim is to study the relationship between the curvature of the canonical connection and the Kodaira dimension. In the integrable case, a theorem of Yau (see [Yau74, Corollary 2]) states that on a compact Kähler manifold the positivity of the total scalar curvature of the Chern connection forces the Kodaira dimension of the manifold to be $-\infty$; a generalization of this result for almost Hermitian manifolds is provided in [Yan17, Theorem 1.1], [Yan19, Theorem 1.3] and [CZ18, Proposition 9.5]. Our results show that the opposite implication does not hold in general: by computing explicitly the scalar curvature of the canonical connection of our examples, we find that it is possible for an almost Kählelr manifold to have vanishing scalar curvature and Kodaira dimension 0. More precisely, we prove the following

Theorem (Theorem 4.6 and 5.9) - There exist families $X_{a}$ and $Y_{t}$ of almost Kähler manifolds (with $a \in \mathbb{R} \backslash\{0\}$ and $t \in \mathbb{R}^{4}$ ) whose members have Kodaira dimension $-\infty$ on a dense subset of the parameter space, and whose canonical connection $\nabla^{c}$ has $\operatorname{Ric}\left(\nabla^{c}\right) \equiv 0$ (hence also scal $\left(\nabla^{c}\right) \equiv 0$ ).

A final outcome of our work can be obtained by combining the previous two results. As we mentioned, the different members of the families we consider have different Kodaira dimension and vanishing scalar curvature. More in detail, all the members have Kodaira dimension $-\infty$ except those on a subvariety of the parameter space where the Kodaira dimension jumps to 0; on the other hand, for all the members of these families the reason why the scalar curvature vanishes is that the canonical connection has trivial Ricci tensor. Hence we show also that in the almost Kähler case it is possible for a manifold to have vanishing Ricci curvature (hence trivial first Chern class) but Kodaira dimension $-\infty$.

The structure of the paper is as follows. In Section 2 we recall the definition of Kodaira dimension for almost complex manifolds from [CZ18]. In Section 3 we collect some known results concerning the canonical connection on an almost complex manifold and its Ricci and scalar curvature, focussing in particular on the case of almost Kähler manifolds. In Section 4 we compute the curvature of the canonical connection on a family of almost Kahler structures on the family of
almost complex manifolds introduced in [CZ18, §6.1] on the differentiable manifold underlying a Kodaira surface, showing our first main result (Theorem 4.6). In Section 5 we consider the differentiable manifold underlying a Nakamura threefold, and endow it with a family of almost Kähler structures: in Section 5.1 we compute the Kodaira dimension of these almost complex manifolds, and prove that it can assume the values 0 or $-\infty$ (Theorem 5.5); finally in Section 5.2 we show that the Ricci and scalar curvature of the almost Kähler metrics on the member of this family always vanish (Theorem 5.9).

Acknowledgement - The authors express their gratitude to Weiyi Zhang for having introduced them to the subject of Kodaira dimension for almost complex manifolds. We also thank Tian-Jun Li for having brought to our attention the reference [Li10] and Valentino Tosatti for his comments on a previous version of this paper.

\section*{2. Kodaira dimension of almost complex manifolds}

Let $(M, J)$ be a compact $2 n$-dimensional smooth manifold endowed with an almost complex structure $J$. Following [CZ18], we recall briefly the definition of Kodaira dimension of $(M, J)$.

Let $\Lambda_{J}^{p, q} M$ be the bundle of $(p, q)$-forms on $(M, J)$ and denote by $\Omega_{J}^{p, q}(M)=$ $\Gamma\left(M, \Lambda_{J}^{p, q} M\right)$ the space of $(p, q)$-forms on $(M, J)$. Denote by $d$ the exterior differential, then
$$d\left(\Omega_{J}^{p, q}(M)\right) \subset \Omega_{J}^{p+2, q-1}(M)+\Omega_{J}^{p+1, q}(M)+\Omega_{J}^{p, q+1}(M)+\Omega_{J}^{p-1, q+2}(M) .$$
Consequently $d$ splits as
$$d=A_{J}+\partial_{J}+\bar{\partial}_{J}+\bar{A}_{J},$$
where $A_{J}=\pi^{p+2, q-1} \circ d, \bar{\partial}_{J}=\pi^{p, q+1} \circ d$. Let $\mathscr{K}_{X}=\Lambda_{J}^{n, 0} M$ be the canonical bundle of the almost complex manifold $X=(M, J)$. Then $\mathscr{K}_{X}$ is a complex line bundle over $X$ and the $\bar{\partial}_{J}$-operator on $(M, J)$ gives rise to a pseudoholomorphic structure on $\mathscr{K}_{X}$, i.e., a differential operator still denoted by $\bar{\partial}_{J}$,
$$\bar{\partial}_{J}: \Gamma\left(M, \mathscr{K}_{X}\right) \rightarrow \Gamma\left(M, T^{*} M^{0,1} \otimes \mathscr{K}_{X}\right)$$
satisfying the Leibniz rule
$$\bar{\partial}_{J}(f \sigma)=\bar{\partial}_{J} f \otimes \sigma+f \bar{\partial}_{J} \sigma,$$
for every smooth function $f$ and section $\sigma$.
By Hodge Theory (see [CZ18, Theorem 1.1]), $H^{0}\left(M, \mathscr{K}_{X}^{\otimes m}\right)$ is a finite dimensional complex vector space for every $m \geq 1$.

Definition 2.1 ([CZ18, Definition 1.2]) - The $m^{\text {th }}$-plurigenus of $(M, J)$ is defined as
$$P_{m}(M, J):=\operatorname{dim}_{\mathbb{C}} H^{0}\left(M, \mathscr{K}_{X}^{\otimes m}\right) .$$
The Kodaira dimension of $(M, J)$ is defined as
$$\kappa^{J}(M):= \begin{cases}-\infty & \text { if } P_{m}(J)=0 \text { for every } m \geq 1, \\ \limsup _{m \rightarrow+\infty} \frac{\log P_{m}(J)}{\log m} & \text { otherwise. }\end{cases}$$

In their paper, Chen and Zhang provide also another definition of Kodaira dimension for an almost complex manifold (see [CZ18, Definition 1.5]): one uses a basis for the space of pseudoholomorphic sections of the pluricanonical bundle to produce a map
$$\Phi_{\mathscr{K}_{X}^{\otimes m}}^{\otimes}: X \backslash B \longrightarrow \mathbb{P}^{n},$$
where $B$ is the base locus of $\left|\mathscr{K}_{X}\right|$, and then define
$$\kappa_{J}(M):= \begin{cases}-\infty & \text { if } P_{m}(J)=0 \text { for every } m \geq 1, \\ \max _{m} \operatorname{dim}_{\mathbb{C}} \Phi_{\mathscr{K}_{X}^{\otimes m}}(X \backslash B) & \text { otherwise. }\end{cases}$$
Remark 2.2 — It is an open problem whether these two definitions actually coincide, but there are few cases where this is known. By definition, for an almost complex manifold $(M, J)$ we have $\kappa^{J}(M)=-\infty$ if and only if $\kappa_{J}(M)=-\infty$. It requires some moments more of thinking the fact that also $\kappa^{J}(M)=0$ if and only if $\kappa_{J}(M)=$ 0. Anyway, it is a well-known fact that $\kappa^{J}(M)=\kappa_{J}(M)$ if $J$ is integrable.

\section*{3. Recaps on the canonical connection on almost complex manifolds}

In this section we recall some basic facts and definitions concerning canonical connections on almost complex manifolds. The theory is well known, but we decided to include this section for the sake of completeness and to set up the notation we will use throughout the paper.

The interested reader may refer to [Gau97] or [TWY08] for a more detailed exposition.
3.1. Generalities on connections. We begin recalling the definition of complex connection.

Definition 3.1 (Complex connection) - Let $M$ be a smooth manifold, and let $E$ be a complex vector bundle on $M$. A (complex) connection on $E$ is a map
$$\nabla: \Gamma\left(M, T_{\mathbb{C}} M\right) \times \Gamma(M, E) \longrightarrow \Gamma(M, E)$$
such that:
\begin{itemize}
\item[(1)] ∇ is C-linear in each entry;
\item[(2)] $\nabla_{f X} s=f \nabla_{X} s$ for every (complex smooth) function $f$ on $M$;
\item[(3)] $\nabla_{X}(f s)=X(f) \cdot s+\nabla_{X} s$ for every (complex smooth) function $f$ on $M$.
\end{itemize}

If we have a real vector bundle $E$ on the manifold $M$, endowed with a (real) connection $D$, then there is a canonical way to extend this connection to a complex connection $D^{\mathbb{C}}$ on the complexification $E_{\mathbb{C}}$ of $E$ :
$$D_{X+\sqrt{-1} Y}^{\mathbb{C}}(s+\sqrt{-1} t)=D_{X} s-D_{Y} t+\sqrt{-1}\left(D_{X} t+D_{Y} s\right) .$$

Let now consider a complex vector bundle on $M$. We can see our complex vector bundle as a pair $(E, I)$, where $E$ is a real vector bundle on $M$ and $I$ is an endomorphism of $E$ such that $I^{2}=-\operatorname{id}_{E}$ (cf. [dBT96, Definition 1.1]). For this reason, we will refer to $(E, I)$ as the complex vector bundle, while $E$ will denote the underlying real bundle. Of course, there is a canonical isomorphism of complex vector bundles $(E, I) \simeq E^{1,0} \subseteq E_{\mathbb{C}}$.

Let $D$ be a (real) connection on $E$. We define
$$\begin{array}{ccc}
\nabla^{D}: \Gamma\left(M, T_{\mathbb{C}} M\right) \times \Gamma(M,(E, I)) & \longrightarrow & \Gamma(M,(E, I)) \\
(X+\sqrt{-1} Y, s) & \longmapsto D_{X} s+I D_{Y} s .
\end{array}$$
The following Lemma is well known.
Lemma 3.2 - In the above situation, $\nabla^{D}$ is a (complex) connection on $(E, I)$ if and only if $D I=0$. In this case, $\nabla^{D}$ coincides with the restriction of $D^{\mathbb{C}}$ to $E^{1,0}$ under the canonical isomorphism
$$\begin{array}{rcrc}
\xi:(E, I) & \longrightarrow & E^{1,0} \\
s & \longmapsto & \frac{1}{2}(s-\sqrt{-1} I s) .
\end{array}$$

Lemma 3.2 essentially states that if $(E, I)$ is a complex vector bundle and $D$ is a connection of $E$ such that $D I=0$, then we have a commutative diagram
![](https://cdn.mathpix.com/cropped/0646c5c5-1fe8-4ff4-b751-bfb8d5c5662c-05.jpg?height=202&width=705&top_left_y=517&top_left_x=679)
where the vertical maps are isomorphisms. As a consequence, we have canonical bijections between the following sets:
\begin{itemize}
\item[(1)] $\{$ Real connections $D$ on $E$ such that $D I=0\}$;
\item[(2)] \{Complex connections on $(E, I)$ \};
\item[(3)] \{Complex connections on $E^{1,0}$ \}.
\end{itemize}
3.2. The type of a form with values in a bundle. In this section we want to discuss some classical stuff on the type decomposition on almost complex manifolds. We restrict ourselves to the case of 2-forms as this is the only case we will consider in the sequel.

Let $(E, I)$ be a complex vector bundle on the almost complex manifold $(M, J)$. From the real point of view, a 2-form on $M$ with values in $E$ is a section
$$\omega \in \Gamma\left(M, \bigwedge^{2} T^{*} M \otimes_{\mathbb{R}} E\right) .$$
When we extend this form by $\mathbb{C}$-linearity, we get then a section
$$\hat{\omega} \in \Gamma\left(M, \bigwedge^{2} T_{\mathbb{C}}^{*} M \otimes_{\mathbb{C}}(E, I)\right) .$$
It makes then sense to decompose
$$\hat{\omega}=\omega^{2,0}+\omega^{1,1}+\omega^{0,2}$$
according to the type decomposition of the form part of $\hat{\omega}$. The relation between $\omega^{p, q}$ and $\omega$ is outlined in the following Lemma.

Lemma 3.3 - Keep the notations as above. Then:
\begin{itemize}
\item[(1)] the form $\hat{\omega}$ is of pure type $(2,0)$ if and only if $\omega(J X, Y)=I \omega(X, Y)$;
\item[(2)] the form $\hat{\omega}$ is of pure type $(1,1)$ if and only if $\omega(J X, J Y)=\omega(X, Y)$;
\item[(3)] the form $\hat{\omega}$ is of pure type $(0,2)$ if and only if $\omega(J X, Y)=-I \omega(X, Y)$.
\end{itemize}

Proof. As the proof of each point is very similar (and these points should also be familiar), we give a proof only of (1).

Let $X, Y \in \Gamma\left(M, T_{\mathbb{C}} M\right)$, and denote $X^{1,0}$ (resp., $X^{0,1}$ ) the (1,0)-part (resp., the $(0,1)$-part) of $X$, and similarly for $Y$. Then $\hat{\omega}$ is of pure type $(2,0)$ if and only if
$$\hat{\omega}(X, Y)=\hat{\omega}\left(X^{1,0}, Y^{1,0}\right) .$$
Assume this holds, and let $X, Y \in \Gamma(M, T M)$. Then $\omega(X, Y)=\hat{\omega}(X, Y)$, and so
$$\begin{aligned}
\omega(X, Y) & =\hat{\omega}\left(X^{1,0}, Y^{1,0}\right)= \\
& =\frac{1}{4}(\hat{\omega}(X-\sqrt{-1} J X, Y-\sqrt{-1} J Y))= \\
& =\frac{1}{4}(\omega(X, Y)-\omega(J X, J Y)-I(\omega(X, J Y)+\omega(X, J Y))) .
\end{aligned}$$
A similar computation shows that
$$\omega(J X, Y)=\frac{1}{4}(\omega(X, J Y)+\omega(X, J Y)+I(\omega(X, Y)-\omega(J X, J Y))),$$
hence that $\omega(J X, Y)=I \omega(X, Y)$.

Vice versa, observe that $\omega(J X, Y)=I \omega(X, Y)$ implies that also $\omega(X, J Y)=$ $I \omega(X, Y)$. It then follows that
$$\begin{aligned}
\hat{\omega}\left(X^{1,0}, Y^{1,0}\right)= & \frac{1}{4}(\hat{\omega}(X-\sqrt{-1} J X, Y-\sqrt{-1} J Y))= \\
= & \frac{1}{4}(\hat{\omega}(X, Y)-\hat{\omega}(J X, J Y)+ \\
& -I(\hat{\omega}(X, J Y)+\hat{\omega}(X, J Y)))= \\
= & \left.\frac{1}{4}(\hat{\omega}(X, Y)+\hat{\omega}(X, Y)+\hat{\omega}(X, Y)+\hat{\omega}(X, Y))\right)= \\
= & \hat{\omega}(X, Y) .
\end{aligned}$$ \(\square\)

This Lemma justifies the definition of type of a form with values in a complex bundle given in [Gau97, Definition 1]. Here we provide the complex interpretation, comparing $\hat{\omega}$ with the 'usual' complex extension
$$\omega_{\mathbb{C}} \in \Gamma\left(M, \bigwedge^{2} T^{*} \mathbb{C} M \otimes_{\mathbb{C}} E_{\mathbb{C}}\right)$$
of $\omega$. It is in fact easy to see that there is a commutative diagram
![](https://cdn.mathpix.com/cropped/0646c5c5-1fe8-4ff4-b751-bfb8d5c5662c-06.jpg?height=195&width=319&top_left_y=1154&top_left_x=872)
where $\xi$ denote the standard complex isomorphism $(E, I) \simeq E^{1,0}$ as before.
3.3. Connections on the tangent bundle. We now want to restrict to the case where $(M, J)$ is an almost complex manifold. Let ∇ be a complex connection on $T^{1,0} M$ : our aim is to give a 'good' definition for the torsion of ∇ .

Let $D$ be the real connection on $T M$ associated to ∇ , which is explicitly given by $D_{X} Y=\xi^{-1}\left(\nabla_{X} \xi(Y)\right)$ and satisfies $D I=0$. The holomorphic torsion of ∇ is then defined as $T^{\nabla}=\hat{T^{D}}$, i.e.
$$\begin{aligned}
T^{\nabla}: \Gamma\left(M, \bigwedge^{2} T_{\mathbb{C}} M\right) & \longrightarrow \Gamma\left(M, T^{1,0} M\right) \\
(X, Y) & \longmapsto \pi^{1,0}\left(D_{X}^{\mathbb{C}} Y-D_{Y}^{\mathbb{C}} X-[X, Y]\right) .
\end{aligned}$$
3.4. The case of almost Hermitian manifolds. Let $(M, g, J)$ be an almost Hermitian manifold, i.e., $(M, J)$ is an almost complex manifold and $g$ is a Riemannian metric on $M$ such that $g(J \cdot, J \cdot)=g(\cdot, \cdot)$. Let $\omega(\cdot, \cdot)=g(J \cdot, \cdot)$ be the associated fundamental 2-form. Then
$$h=g-\sqrt{-1} \omega$$
defines a Hermitian scalar product on $(T M, J)$. Moreover, if we denote by $g_{\mathbb{C}}$ the complex bilinear extension of $g$ to $T_{\mathbb{C}} M$, then for all $X, Y \in \Gamma(M, T M)$
$$h(X, Y)=2 g_{\mathbb{C}}(\xi(X), \overline{\xi(Y)}),$$
i.e., $\frac{1}{2} h$ coincides with the complex Hermitian extension of $g$ via the canonical identification $(T M, J) \simeq T^{1,0} M$ provided by $\xi$.

Let now $D$ be a real connection on $T M$, and assume that
$$D g=0, \quad D J=0 .$$
An easy computation then shows that $D \omega=0$, from which we deduce that $\nabla^{D} h=$ 0.

Remark 3.4 - We show now that there exists at least one such connection. Let $D$ be a connection such that $D g=0$, e.g., the Levi-Civita connection of $g$. Let $D^{\prime}$ be another connection such that $D^{\prime} g=0$ : we have $D_{X}^{\prime} Y=D_{X} Y+F_{X} Y$, and the condition on the metric is equivalent to
$$g\left(F_{X} Y, Z\right)+g\left(Y, F_{X} Z\right)=0 .$$
We want to find a suitable $F$ such that $D^{\prime} J=0$. For this purpose, we see that $D^{\prime} J=0$ is equivalent to
$$(D J)_{X} Y=J F_{X} Y-F_{X} J Y .$$
So, if we choose
$$F_{X} Y=-\frac{1}{2} D_{X} Y-\frac{1}{2} J D_{X} J Y$$
the resulting connection
$$D_{X}^{\prime} Y=\frac{1}{2}\left(D_{X} Y-J D_{X} J Y\right)$$
is such that $D^{\prime} g=0$ and $D^{\prime} J=0$.
Let $\nabla^{L C}$ denote the Levi-Civita connection of $g$, and consider the connection
$$D_{X} Y=\frac{1}{2}\left(\nabla_{X}^{L C} Y-J \nabla_{X}^{L C} J Y\right), \quad X, Y \in \Gamma(M, T M)$$
on $T M$. It follows from the discussion in Remark 3.4 that $D g=0$ and $D J=0$, and as a consequence we have the induced (isomorphic) complex connections $\nabla^{D}$ and $D^{\mathbb{C}}$ on ( $T M, I$ ) and $T^{1,0} M$ respectively.

We want to compute the holomorphic torsion of these connections, so we begin with some remarks on the torsion of $D$.

Definition 3.5 - Let $J$ be an almost complex structure on the differentiable manifold $M$. The Nijenhuis tensor of $J$ is
$$N_{J}(X, Y)=[J X, J Y]-J[J X, Y]-J[X, J Y]-[X, Y], \quad X, Y \in \Gamma(M, T M) .$$
So $N_{J} \in \Gamma\left(M, \bigwedge^{2} T^{*} M \otimes T M\right)$.
Lemma 3.6 - Let $(M, g, J)$ be an almost Hermitian manifold. Denote by $\nabla^{L C}$ the Levi-Civita connection of $g$ and by $D$ the induced connection as in (3.1). Then
$$2 T^{D}(X, Y)=N_{J}(X, Y)-\left(\nabla^{L C} J\right)_{J X} Y+\left(\nabla^{L C} J\right)_{J Y} X,$$
where $N_{J}$ is the Nijenhuis tensor of $J$.
Proof. This is just a computation. On one hand we have
$$\begin{aligned}
2 T^{D}(X, Y) & =\nabla_{X}^{L C} Y-J \nabla_{X}^{L C} J Y-\nabla_{Y}^{L C} X+J \nabla_{Y}^{L C} J X-2[X, Y]= \\
& =-J \nabla_{X}^{L C} J Y+J \nabla_{Y}^{L C} J X-\nabla_{X}^{L C} Y+\nabla_{Y}^{L C} X= \\
& =J\left(-\nabla_{X}^{L C} J Y+J \nabla_{X}^{L C} Y+\nabla_{Y}^{L C} J X-J \nabla_{Y}^{L C} X\right)= \\
& =-J\left(\left(\nabla^{L C} J\right)_{X} Y-\left(\nabla^{L C} J\right)_{Y} X\right) ;
\end{aligned}$$
on the other
$$\begin{aligned}
N_{J}(X, Y)= & \nabla_{J X}^{L C} J Y-\nabla_{J Y}^{L C} J X-J\left(\nabla_{J X}^{L C} Y-\nabla_{Y}^{L C} J X\right)+ \\
& -J\left(\nabla_{X}^{L C} J Y-\nabla_{J Y}^{L C} X\right)-\nabla_{X}^{L C} Y+\nabla_{Y}^{L C} X= \\
= & \left(\nabla^{L C} J\right)_{J X} Y-\left(\nabla^{L C} J\right)_{J Y} X+J\left(-\left(\nabla^{L C} J\right)_{X} Y+\left(\nabla^{L C} J\right)_{Y} X\right),
\end{aligned}$$
and the Lemma follows. \(\square\)

Definition 3.7 - Let $(M, g, J)$ be an almost Hermitian manifold, with associated fundamental form $\omega$. Then $(M, g, J)$ is said
\begin{itemize}
\item[(1)] almost Kähler if $d \omega=0$;
\end{itemize}
\begin{itemize}
\item[(2)] quasi Kähler if $\bar{\partial} \omega=0$.
\end{itemize}

In particular, any almost Kähler manifold is quasi Kähler.
Corollary 3.8 - Let $(M, g, J)$ be a quasi Kähler manifold, and let $\nabla^{L C}$ denote the Levi-Civita connection of $g$. Then $N_{J}(X, Y)=-2 J\left(\left(\nabla^{L C} J\right)_{X} Y-\left(\nabla^{L C} J\right)_{Y} X\right)$, and so
$$T^{D}=\frac{1}{4} N_{J}(X, Y),$$
where $D$ is the connection defined by (3.1).
Proof. It follows from [Gau97, Proposition 1(iv)] that $(M, g, J)$ is quasi Kähler if and only if $\left(\nabla^{L C} J\right)_{J X} Y=-J\left(\nabla^{L C} J\right)_{X} Y$. But then the equation (3.3) semplifies to $N_{J}(X, Y)=-2 J\left(\left(\nabla^{L C} J\right)_{X} Y-\left(\nabla^{L C} J\right)_{Y} X\right)$. The result then follows from equation (3.2). \(\square\)

Under the assumptions of Corollary 3.8, we can see that $T^{D}$ is of pure type $(0,2)$ : this follows from the fact that the Nijenhuis tensor satisfies $N_{J}(J X, Y)=$ $-J N_{J}(X, Y)$. We give now the complex version of the previous result.

Proposition 3.9 - Let $(M, g, J)$ be a quasi Kähler manifold. Denote by $\nabla^{L C}$ the Levi-Civita connection of $g$ and by $D$ the connection on $T M$ induced by (3.1). Let ∇ be the complex connection on $T^{1,0} M$ induced by $D$. Then the holomorphic torsion of ∇ is
$$T^{\nabla}(X, Y)=\frac{1}{4} \pi^{1,0} N_{I}^{\mathbb{C}}(X, Y), \quad X, Y \in \Gamma\left(M, T_{\mathbb{C}} M\right) .$$
Remark 3.10 - We can simplify the expression for $T^{\nabla}$ further. It is in fact easy to see that for $X, Y \in \Gamma\left(M, T_{\mathbb{C}} M\right)$ one has
$$N_{J}^{\mathbb{C}}(X, Y)=-4 \pi^{1,0}\left[\pi^{0,1} X, \pi^{0,1} Y\right]-4 \pi^{0,1}\left[\pi^{1,0} X, \pi^{1,0} Y\right],$$
and as a consequence
$$T^{\nabla}(X, Y)=\frac{1}{4} \pi^{1,0} N_{J}^{\mathbb{C}}(X, Y)=-\pi^{1,0}\left[\pi^{0,1} X, \pi^{0,1} Y\right] .$$
We can also observe that now it is evident that $T^{\nabla}$ is a (0, 2)-form with values in $T^{1,0} M$.

The connection ∇ we defined is the connection appearing in [Gau97, §2.6] corresponding to the parameter $t=0$. It is uniquely determined by the following conditions:
\begin{itemize}
\item[(1)] $\nabla h=0$;
\item[(2)] $T^{\nabla}$ has vanishing (2, 0)-part and its (1, 1)-part is anti-symmetric.
\end{itemize}
On the contrary, the canonical connection (which is the Chern connection if $I$ is integrable) corresponds to the choice $t=1$ of the parameter in Gauduchon's paper, and it is characterized by the vanishing of the (1, 1)-part of its holomorphic torsion. What Proposition 3.9 and Remark 3.10 show is that, in the case of almost Kähler manifolds, these two connections actually coincide.

Notation - Let $(M, g, J)$ be a quasi Kähler manifold, and let $\nabla^{L C}$ be the Levi-Civita connection of $g$. We will denote by $\nabla^{c}$ the induced canonical connection on $T^{1,0} M$, i.e., the complex connection
$$\nabla_{X}^{c} Y=\frac{1}{2}\left(\nabla_{X}^{L C} Y-J \nabla_{X}^{L C} J Y\right), \quad X \in \Gamma\left(M, T_{\mathbb{C}} M\right), Y \in \Gamma\left(M, T^{1,0} M\right) .$$
3.5. The complex formalism. As we are dealing with almost complex manifolds, it is more convenient to work within the complex framework, rather than stay with the real formalism.

Let $X=(M, g, J)$ be an almost Hermitian manifold, and let $h$ be the Hermitian scalar product induced by $g$ on $T^{1,0} M$, namely $h(Z, W)=g_{\mathbb{C}}(Z, \bar{W})$ where $Z, W \in$ $\Gamma\left(M, T^{1,0} M\right)$ and $g_{\mathbb{C}}$ is the complex bilinear extension of $g$. Fix a (local) $h$-unitary frame $\left\{e_{1}, \ldots, e_{n}\right\}$ for $T^{1,0} M$ with dual frame $\left\{e^{1}, \ldots, e^{n}\right\}$.

Let ∇ be a connection on $T M$ such that $\nabla g=\nabla J=0$, and denote also by $\nabla$ its extension to $T_{\mathbb{C}} M$. The connection 1-forms of ∇ are then the 1-forms defined by
$$\nabla e_{j}=\sum_{i=1}^{n} \theta_{j}^{i} e_{i},$$
and they satisfy $\theta_{i}^{j}+\bar{\theta}_{j}^{i}=0$. Let $\tau$ be the holomorphic torsion of $\nabla$, then we have $\tau \in \Gamma\left(M, \bigwedge^{2} T_{\mathbb{C}}^{*} M \otimes_{\mathbb{C}} T^{1,0} M\right)$ and so we can write
$$\tau=\sum_{i=1}^{n} \Theta^{i} \otimes e_{i} .$$
The 2-forms $\Theta^{i}$ appearing in this expression are called the torsion forms of ∇ , and they are related to the connection form by the first structure equation
$$\Theta^{i}=d e^{i}+\sum_{j=1}^{n} \theta_{j}^{i} \wedge e^{j}, \quad i=1, \ldots, n .$$
Concerning the curvature, we can also decompose the holomorphic curvature of ∇ as follows:
$$R(X, Y) e_{j}=\sum_{i=1}^{n} \Psi_{j}^{i}(X, Y) e_{i}$$
for suitable 2-forms $\Psi_{j}^{i}$, known the as curvature forms of ∇ . The second structure equations
$$\Psi_{j}^{i}=d \theta_{j}^{i}+\sum_{k=1}^{n} \theta_{k}^{i} \wedge \theta_{j}^{k}, \quad i, j=1, \ldots, n$$
provide a direct link between the connection forms and the curvature forms.
We focus now on the case where ∇ is the canonical connection $\nabla^{c}$ of $X$. Each curvature form $\Psi_{j}^{i}$ can be decomposed according to types into its ( 2,0 ), ( 1,1 ) and $(0,2)$ parts, and we can then define functions $R_{j k \bar{l}}^{i}$ by the relation
$$\left(\Psi_{j}^{i}\right)^{1,1}=\sum_{k, l=1}^{n} R_{j k l}^{i} \bar{e}^{k} \wedge \bar{e}^{l} .$$

Definition 3.11 (Ricci and scalar curvature) - The Ricci curvature of the canonical connection $\nabla^{c}$ of an almost Hermitian manifold $(M, g, J)$ is the tensor
$$\operatorname{Ric}\left(\nabla^{c}\right)=\sum_{k, l=1}^{n} R_{k \bar{l}} e^{k} \wedge \bar{e}^{l}, \quad \text { with } R_{k \bar{l}}=\sum_{i=1}^{n} R_{i k \bar{l}}^{i} .$$
The scalar curvature of $\nabla^{c}$ is the function
$$\operatorname{scal}\left(\nabla^{c}\right)=\sum_{k=1}^{n} R_{k \bar{k}}=\sum_{i, k=1}^{n} R_{i k \bar{k}}^{i} .$$

\section*{4. The Kodaira-Thurston manifold}

Let us consider the differentiable manifold $M=S^{1} \times G$, where $S^{1}$ is a circle and $G$ is the (left) quotient of the Heisenberg group
$$\left\{\left.\left(\begin{array}{ccc}
1 & x & z \\
0 & 1 & y \\
0 & 0 & 1
\end{array}\right) \right\rvert\, x, y, z \in \mathbb{R}\right\}$$
by its subgroup consisting of matrices with integral entries. Call $t$ a coordinate on $S^{1}$, then $M$ admits the following global fields of tangent vectors
$$e_{1}=\frac{\partial}{\partial t}, \quad e_{2}=\frac{\partial}{\partial x}, \quad e_{3}=\frac{\partial}{\partial y}+x \frac{\partial}{\partial z}, \quad e_{4}=\frac{\partial}{\partial z},$$
whose duals are
$$e^{1}=d t, \quad e^{2}=d x, \quad e^{3}=d y, \quad e^{4}=d z-x d y .$$
We recall that the only non-trivial differential of the $e^{i}$ 's is $d e^{4}=-e^{2} \wedge e^{3}$, as the only non-trivial commutator among the global vector fields given above is easily seen to be $\left[e_{2}, e_{3}\right]=e_{4}$.

Once we equip $M$ with the complex structure $J$ defined by
$$J e_{1}=e_{4}, \quad J e_{2}=e_{3}, \quad J e_{3}=-e_{2}, \quad J e_{4}=-e_{1}$$
we obtain a complex manifold, which is known as a Kodaira surface. It is well known that $\kappa^{J}(M)=0$.

In these notes we want to focus on a different (non-integrable) almost complex structure on the same manifold, which was introduced in [CZ18, §6.1]. For any $a \in \mathbb{R} \backslash\{0\}$, the almost complex structure $J_{a}$ is defined by
$$J_{a} e_{1}=e_{2}, \quad J_{a} e_{2}=-e_{1}, \quad J_{a} e_{3}=\frac{1}{a} e_{4}, \quad J_{a} e_{4}=-a e_{3},$$
and it induces the almost complex structure
$$J_{a}^{*} e^{1}=-e^{2}, \quad J_{a}^{*} e^{2}=e^{1}, \quad J_{a}^{*} e^{3}=-a e^{4}, \quad J_{a}^{*} e^{4}=\frac{1}{a} e_{3}$$
on the cotangent bundle $T^{*} M$. The Kodaira dimension $\kappa^{J_{a}}(M)$ is known.
Proposition 4.1 (cf. [CZ18, Proposition 6.1]) - Consider the almost complex structure $J_{a}$ on $M$. Then
$$\kappa^{J_{a}}(M)= \begin{cases}-\infty & \text { for } a \notin \pi \mathbb{Q}, \\ 0 & \text { for } a \in \pi \mathbb{Q} .\end{cases}$$

The 2-form
$$\omega=e^{1} \wedge e^{2}+e^{3} \wedge e^{4}$$
is a symplectic form on $M$, which is always compatible with $J_{a}$, meaning that $\omega\left(J_{a} \cdot, J_{a} \cdot\right)=\omega(\cdot, \cdot)$. In the basis of tangent fields $\left\{e_{1}, \ldots, e_{4}\right\}$, the symmetric bilinear form $g_{a}(\cdot, \cdot)=\omega\left(\cdot, J_{a} \cdot\right)$ is represented by the matrix
$$\left(\begin{array}{cccc}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & \frac{1}{a} & 0 \\
0 & 0 & 0 & a
\end{array}\right),$$
hence $g_{a}$ is a Riemannian metric on $M$ if and only if $a>0$. So from now on we will restrict to the case $a>0$ : we have then an almost Kähler manifold $X_{a}=$ $\left(M, g_{a}, J_{a}\right)$. We also see that if we let
$$E_{1}=e_{1}, \quad E_{2}=e_{2}, \quad E_{3}=\sqrt{a} e_{3}, \quad E_{4}=\frac{1}{\sqrt{a}} e_{4},$$
then $\left\{E_{1}, E_{2}, E_{3}, E_{4}\right\}$ is an orthonormal global frame on $X$. Its dual frame is
$$E^{1}=e^{1}, \quad E^{2}=e^{2}, \quad E^{3}=\frac{1}{\sqrt{a}} e^{3}, \quad E^{4}=\sqrt{a} e^{4},$$
and we easily see that
$$d E^{4}=-a E^{2} \wedge E^{3}, \quad\left[E_{2}, E_{3}\right]=a E_{4} .$$

Lemma 4.2 - The Nijenhuis tensor $N_{J_{a}}$ of $X_{a}$ is given by
$$\begin{array}{lll}
N_{J_{a}}\left(E_{1}, E_{2}\right)=0, & N_{J_{a}}\left(E_{1}, E_{3}\right)=a E_{3}, & N_{J_{a}}\left(E_{1}, E_{4}\right)=-a E_{4}, \\
N_{J_{a}}\left(E_{2}, E_{3}\right)=-a E_{4}, & N_{J_{a}}\left(E_{2}, E_{4}\right)=-a E_{3}, & N_{J_{a}}\left(E_{3}, E_{4}\right)=0 .
\end{array}$$

Proof. This is a standard computation. Using the definition, it's easy to see that
$$J_{a} E_{1}=E_{2}, \quad J_{a} E_{2}=-E_{1}, \quad J_{a} E_{3}=E_{4}, \quad J_{a} E_{4}=-E_{3},$$
and so $N_{J_{a}}\left(E_{1}, E_{3}\right)=a E_{3}$. The other expressions can be easily deduced from the fact that
$$N_{J_{a}}\left(J_{a} X, Y\right)=N_{J_{a}}\left(X, J_{a} Y\right)=-J_{a} N_{J_{a}}(X, Y) .$$ \(\square\)

Let now $\nabla^{c}$ be the canonical connection on $X_{a}=\left(M, g_{a}, J_{a}\right)$ introduced in (3.1), and denote by $T=T^{\nabla^{c}}$ its torsion. We denote by $\Theta^{i}$ the real torsion forms of $\nabla^{c}$, namely the 2-forms such that
$$T^{\nabla^{c}}(X, Y)=\sum_{i} \Theta^{i}(X, Y) E_{i} .$$

Lemma 4.3 — The real torsion forms of the canonical connection $\nabla^{c}$ on the almost complex manifold $X_{a}$ are given by
$$\begin{array}{ll}
\Theta^{1}=0, & \Theta^{2}=0, \\
\Theta^{3}=\frac{1}{4} a\left(E^{1} \wedge E^{3}-E^{2} \wedge E^{4}\right), & \Theta^{4}=-\frac{1}{4} a\left(E^{2} \wedge E^{3}+E^{1} \wedge E^{4}\right) .
\end{array}$$

Proof. By Corollary 3.8 we know that $T(X, Y)=\frac{1}{4} N_{J_{a}}(X, Y)$, hence the result follows from Lemma 4.2. \(\square\)

We now want to deduce the connection forms of $\nabla^{c}$. To set up the notation, we recall that the real connection forms of $\nabla^{c}$ are the 1-forms $\omega_{j}^{i}$ such that $\nabla^{c} e_{j}=$ $\sum_{i} \omega_{j}^{i} \otimes e_{j}$, and we can collect them in the connection matrix $\omega=\left(\omega_{j}^{i}\right)(i$ is the row index, $j$ is the column index).

Proposition 4.4 — The real connection matrix for the canonical connection $\nabla^{c}$ on the almost complex manifold $X_{a}$ is
$$\omega=\frac{1}{4} a\left(\begin{array}{llll}
0 & 0 & E^{3} & -E^{4} \\
0 & 0 & E^{4} & E^{3} \\
-E^{3} & -E^{4} & 0 & -2 E^{2} \\
E^{4} & -E^{3} & 2 E^{2} & 0
\end{array}\right) .$$
Proof. We can compute the connection forms $\omega_{j}^{i}$ using the Cartan structure equations
$$\left\{\begin{array}{l}
d E^{i}+\sum_{j=1}^{4} \omega_{j}^{i} \wedge E^{j}=\Theta^{i} \\
\omega_{j}^{i}+\omega_{i}^{j}=0 .
\end{array}\right.$$
In fact, the second set of equations allows us to restrict to $\omega_{j}^{i}$ with $j>i$. Hence the first set of equations reduces to
$$\left\{\begin{array}{l}
\omega_{2}^{1} \wedge E^{2}+\omega_{3}^{1} \wedge E^{3}+\omega_{4}^{1} \wedge E^{4}=0 \\
-\omega_{2}^{1} \wedge E^{1}+\omega_{3}^{2} \wedge E^{3}+\omega_{4}^{2} \wedge E^{4}=0 \\
-\omega_{3}^{1} \wedge E^{1}-\omega_{3}^{2} \wedge E^{2}+\omega_{4}^{3} \wedge E^{4}=\frac{1}{4} a\left(E^{1} \wedge E^{3}-E^{2} \wedge E^{4}\right) \\
-a E^{2} \wedge E^{3}-\omega_{4}^{1} \wedge E^{1}-\omega_{3}^{2} \wedge E^{2}-\omega_{4}^{3} \wedge E^{3}=-\frac{1}{4} a\left(E^{2} \wedge E^{3}+E^{1} \wedge E^{4}\right),
\end{array}\right.$$
and it is then easy to verify that (4.1) is the solution of this system. \(\square\)

From the knowledge of the real connection matrix $\omega$, we can deduce the real curvature matrix $\Omega$ of $\nabla^{c}$ :
$$\Omega=d \omega+\omega \wedge \omega=\frac{1}{8} a^{2}\left(\begin{array}{cccc}
0 & -E^{3} \wedge E^{4} & E^{2} \wedge E^{4} & 3 E^{2} \wedge E^{3} \\
E^{3} \wedge E^{4} & 0 & -3 E^{2} \wedge E^{3} & E^{2} \wedge E^{4} \\
-E^{2} \wedge E^{4} & 3 E^{2} \wedge E^{3} & 0 & E^{3} \wedge E^{4} \\
-3 E^{2} \wedge E^{3} & -E^{2} \wedge E^{4} & -E^{3} \wedge E^{4} & 0
\end{array}\right) .$$

Theorem 4.5 - The real scalar curvature of the canonical connection $\nabla^{c}$ on the almost complex manifold $X_{a}$ is given by
$$\operatorname{scal}(D)=-\frac{1}{8} a^{2} .$$
Proof. From the expression of the curvature matrix $\Omega=\left(\Omega_{j}^{i}\right)$ given in (4.2) we can compute the components $R_{j k l}^{i}$ of the curvature of $\nabla^{c}$, in fact by definition
$$\Omega_{j}^{i}=\sum_{k, l} R_{j k l}^{i} \otimes\left(E^{k} \wedge E^{l}\right) .$$
As $\left\{E_{1}, \ldots E_{4}\right\}$ is an orthonormal frame, we have that $R_{i j k l}=R_{j k l}^{i}$ : the non-vanishing components are then
$$\begin{array}{llll}
R_{1234}=-\frac{1}{8} a^{2} & R_{1324}=\frac{1}{8} a^{2} & R_{1423}=\frac{3}{8} a^{2} & R_{2323}=-\frac{3}{8} a^{2} \\
R_{2424}=\frac{1}{8} a^{2} & R_{3434}=\frac{1}{8} a^{2} & R_{2134}=\frac{1}{8} a^{2} & R_{3124}=-\frac{1}{8} a^{2} \\
R_{3223}=\frac{3}{8} a^{2} & R_{4123}=-\frac{3}{8} a^{2} & R_{4224}=-\frac{1}{8} a^{2} & R_{4334}=-\frac{1}{8} a^{2} .
\end{array}$$
As a consequence, the Ricci tensor $R_{i j}=\sum_{k} R_{i k j}^{k}$ is expressed by the matrix
$$\left(\begin{array}{cccc}
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & -\frac{3}{8} a^{2} & 0 \\
0 & 0 & 0 & \frac{1}{4} a^{2}
\end{array}\right),$$
and so the scalar curvature is
$$\operatorname{scal}(D)=-\frac{1}{8} a^{2} .$$
Observe that once again in this last computation we used the fact that $\left\{E_{1}, \ldots, E_{4}\right\}$ is an orthonormal frame. \(\square\)
4.1. An alternative derivation of the connection forms. Recall from (3.1) that the canonical connection is explicitly given by
$$\nabla^{c}=\frac{1}{2}\left(\nabla^{L C}-J_{a} \nabla^{L C} J_{a}\right),$$
where $\nabla^{L C}$ is the Levi-Civita connection of $g_{a}$. From the Koszul formula expressing the Levi-Civita connection we deduce that in the $g_{a}$-orthonormal frame of global fields $\left\{E_{1}, E_{2}, E_{3}, E_{4}\right\}$ we have
$$g_{a}\left(\nabla_{E_{i}}^{L C} E_{j}, E_{k}\right)=\frac{1}{2}\left(g_{a}\left(\left[E_{i}, E_{j}\right], E_{k}\right)-g_{a}\left(\left[E_{j}, E_{k}\right], E_{i}\right)-g_{a}\left(\left[E_{i}, E_{k}\right], E_{j}\right)\right) .$$
In our case, on the almost complex manifold $X_{a}=\left(M, g_{a}, J_{a}\right)$ we see that then $g_{a}\left(\nabla_{E_{i}}^{L C} E_{j}, E_{k}\right)=0$ if both 2 and 3 do not appear among $i, j, k$, as the only non-trivial bracket is $\left[E_{2}, E_{3}\right]=a E_{4}$. Moreover, for the same reason we see that if 2
and 3 appear among $i, j, k$, then $g_{a}\left(\nabla_{E_{i}}^{L C} E_{j}, E_{k}\right)$ is a priori non-trivial only if the remaining index is 4. Hence the only non-vanishing among the $g_{a}\left(\nabla_{E_{i}}^{L C} E_{j}, E_{k}\right)$ are
$$\begin{array}{lll}
g_{a}\left(\nabla_{E 2}^{L C} E_{3}, E_{4}\right)=\frac{1}{2} a & g_{a}\left(\nabla_{E_{2}}^{L C} E_{4}, E_{3}\right)=-\frac{1}{2} a & g_{a}\left(\nabla_{E E_{2}}^{L C} E_{2}, E_{3}\right)=-\frac{1}{2} a \\
g_{a}\left(\nabla_{E_{4}}^{L C} E_{3}, E_{2}\right)=\frac{1}{2} a & g_{a}\left(\nabla_{E_{3}}^{L C} E_{4}, E_{2}\right)=\frac{1}{2} a & g_{a}\left(\nabla_{E_{3}}^{L C} E_{2}, E_{4}\right)=-\frac{1}{2} a
\end{array}$$

We can then use this to compute explicitly how the Levi-Civita connection acts on the basis vector:
$$\begin{array}{llll}
\nabla_{E_{1}}^{L C} E_{1}=0, & \nabla_{E_{1}}^{L C} E_{2}=0, & \nabla_{E 1}^{L C} E_{3}=0, & \nabla_{E_{1}}^{L C} E_{4}=0, \\
\nabla_{E_{2}}^{L C} E_{1}=0, & \nabla_{E 2}^{L C} E_{2}=0, & \nabla_{E 2}^{L C} E_{3}=\frac{1}{2} a E_{4}, & \nabla_{E 2}^{L C} E_{4}=-\frac{1}{2} a E_{3}, \\
\nabla_{E E_{2}}^{L C} E_{1}=0, & \nabla_{E E_{2}}^{L C} E_{2}=-\frac{1}{2} a E_{4}, & \nabla_{E 3}^{L C} E_{3}=0, & \nabla_{E 3}^{L C} E_{4}=\frac{1}{2} a E_{2}, \\
\nabla_{E_{4}}^{L C} E_{1}=0, & \nabla_{E_{4}}^{L C} E_{2}=-\frac{1}{2} a E_{2}, & \nabla_{E_{4}}^{L C} E_{3}=\frac{1}{2} a E_{2}, & \nabla_{E_{4}}^{L C} E_{4}=0 .
\end{array}$$
This result readily implies that
$$\begin{array}{llll}
\nabla_{E_{1}}^{c} E_{1}=0, & \nabla_{E_{1}}^{c} E_{2}=0, & \nabla_{E_{1}}^{c} E_{3}=0, & \nabla_{E_{1}}^{c} E_{4}=0, \\
\nabla_{E_{2}}^{c} E_{1}=0, & \nabla_{E_{2}}^{c} E_{2}=0, & \nabla_{E_{2}}^{c} E_{3}=\frac{1}{2} a E_{4}, & \nabla_{E_{2}}^{c} E_{4}=-\frac{1}{2} a E_{3}, \\
\nabla_{E_{3}}^{c} E_{1}=-\frac{1}{4} a E_{3}, & \nabla_{E_{3}}^{c} E_{2}=-\frac{1}{4} a E_{4}, & \nabla_{E_{3}}^{c} E_{3}=\frac{1}{4} a E_{1}, & \nabla_{E_{3}}^{c} E_{4}=\frac{1}{4} a E_{2}, \\
\nabla_{E_{4}}^{c} E_{1}=\frac{1}{4} a E_{4}, & \nabla_{E_{4}}^{c} E_{2}=-\frac{1}{4} a E_{3}, & \nabla_{E_{4}}^{c} E_{3}=\frac{1}{4} a E_{2}, & \nabla_{E_{4}}^{c} E_{4}=-\frac{1}{4} a E_{1},
\end{array}$$
from which we can compute the connection matrix (4.1).
4.2. Complex curvature of the canonical connection. It is easy to verify that
$$z_{1}=\frac{\sqrt{2}}{2}\left(E_{1}-\sqrt{-1} E_{2}\right), \quad z_{2}=\frac{\sqrt{2}}{2}\left(E_{3}-\sqrt{-1} E_{4}\right)$$
is a unitary global frame for $T^{1,0} M$ with respect to the Hermitian scalar product induced by the complex extension of the metric $g_{a}$. Its dual frame is given by
$$z^{1}=\frac{\sqrt{2}}{2}\left(E^{1}+\sqrt{-1} E^{2}\right), \quad z^{2}=\frac{\sqrt{2}}{2}\left(E^{3}+\sqrt{-1} E^{4}\right) .$$

Thanks to the work done in the previous subsections, we can write down the complex connection forms $\theta_{j}^{i}$ for the canonical connection $\nabla^{c}$ :
$$\begin{aligned}
\nabla^{c} z_{1}= & \frac{\sqrt{2}}{2}\left(\nabla^{c} E_{1}-\sqrt{-1} \nabla^{c} E_{2}\right)= \\
= & \frac{\sqrt{2}}{8} a\left(-E^{3} \otimes E_{3}+\sqrt{-1} E^{4} \otimes E_{3}+E^{4} \otimes E_{4}+\sqrt{-1} E^{3} \otimes E_{4}\right)= \\
= & \frac{\sqrt{2}}{8} a\left(\left(-E^{3}+\sqrt{-1} E^{4}\right) \otimes\left(E_{3}-\sqrt{-1} E_{4}\right)\right)= \\
= & -\frac{\sqrt{2}}{4} a \bar{z}^{2} \otimes z_{2} ; \\
\nabla^{c} z_{2}= & \frac{\sqrt{2}}{2}\left(\nabla^{c} E_{3}-\sqrt{-1} \nabla^{c} E_{4}\right)= \\
= & \frac{\sqrt{2}}{8} a\left(2 E^{2} \otimes E_{4}+E^{3} \otimes E_{1}+E^{4} \otimes E_{2}+2 \sqrt{-1} E^{2} \otimes E_{3}+\right. \\
& \left.-\sqrt{-1} E^{3} \otimes E_{2}+\sqrt{-1} E^{4} \otimes E_{1}\right)= \\
= & \frac{\sqrt{2}}{8} a\left(2 \sqrt{-1} E^{2} \otimes\left(E_{3}-\sqrt{-1} E_{4}\right)+\right. \\
& \left.+\left(E^{3}+\sqrt{-1} E^{4}\right) \otimes\left(E_{1}-\sqrt{-1} E_{2}\right)\right)= \\
= & \frac{\sqrt{2}}{4} a z^{2} \otimes z_{1} \otimes z_{2}+\sqrt{2} \\
& a\left(z^{1}-\bar{z}^{1}\right) .
\end{aligned}$$
From this computations we deduce that the connection matrix for $\nabla^{c}$ is
$$\theta=\frac{\sqrt{2}}{4} a\left(\begin{array}{cc}
0 & z^{2} \\
-\bar{z}^{2} & z^{1}-\bar{z}^{1}
\end{array}\right),$$
hence the curvature matrix is
$$\Psi=d \theta+\theta \wedge \theta=\frac{1}{8} a^{2}\left(\begin{array}{cc}
-z^{2 \overline{2}} & -2 z^{12}-z^{1 \overline{2}}-2 z^{2 \overline{1}}+z^{\overline{1} \overline{2}} \\
-z^{12}-2 z^{\overline{2}}-z^{2 \overline{1}}+2 z^{\overline{1} \overline{2}} & z^{2 \overline{2}}
\end{array}\right) .$$
From this we infer that the only non-trivial coefficient $R_{j k \bar{l}}^{i}$ are
$$\begin{array}{lll}
R_{12 \overline{2}}^{1}=-\frac{1}{8} a^{2} & R_{11 \overline{2}}^{1}=-\frac{1}{8} a^{2} & R_{22 \overline{1}}^{1}=-\frac{1}{4} a^{2} \\
R_{11 \overline{2}}^{2}=-\frac{1}{4} a^{2} & R_{12 \overline{1}}^{2}=-\frac{1}{8} a^{2} & R_{22 \overline{2}}^{2}=\frac{1}{8} a^{2}
\end{array}$$

Theorem 4.6 - The Ricci curvature $\operatorname{Ric}\left(\nabla^{c}\right)$ on the almost Hermitian manifold $X_{a}=\left(M, g_{a}, J_{a}\right)$ vanishes. In particular, the scalar curvature $\operatorname{scal}\left(\nabla^{c}\right)$ also vanishes.

Proof. The Theorem follows directly from (4.3) and the definitions. \(\square\)

Remark 4.7 - The results in Theorem 4.6 can be compared with [Li10, Proposition 7.18]. Our techniques are however different, and can be used to study the behaviour of Kodaira dimension for the other (non-toral) 4-dimensional almost complex nilmanifolds. We will come back on this topic in a future paper.

Remark 4.8 — For $a=-1$ it is possible to find a different computation of the Ricci tensor of the canonical connection on $X_{a}$ in [TW11, §4].

\section*{5. Kodaira dimension of completely solvable Nakamura manifolds}

The Nakamura threefold was introduced in [Nak75, Case III-(3b), p. 90]. In the same paper, Nakamura also describes the Kuranishi family of this manifold, and computes the Kodaira dimension of its members. This example showed that the Hodge numbers $h^{p, q}$, the plurigenera and the Kodaira dimension of a complex manifold are not deformation invariants (see [Nak75, Theorem 2]). In this section we endow the differentiable manifold underlying the Nakamura threefold with a family of non-integrable almost complex structures, and compute the Kodaira dimension of its members in Theorem 5.5.

We briefly recall the construction of completely solvable Nakamura manifolds. Let $A \in \operatorname{SL}(2, \mathbb{Z})$ have two real positive distinct eigenvalues
$$\mu_{1}=e^{-\zeta}, \quad \mu_{2}=e^{\zeta}, \quad \zeta \neq 0 .$$
Set
$$\Lambda=\left(\begin{array}{cc}
e^{-\zeta} & 0 \\
0 & e^{\zeta}
\end{array}\right)$$
and let $P \in M_{2,2}(\mathbb{R})$ be such that
$$\Lambda=P A P^{-1}$$
Consider $\Gamma:=P \mathbb{Z}^{2} \oplus \sqrt{-1} P \mathbb{Z}^{2}$; then $\Gamma$ is a lattice in $\mathbb{C}^{2}$. Let $\mathbb{T}_{\mathbb{C}}^{2}=\mathbb{C}^{2} / \Gamma$ be a 2-dimensional complex torus.

Then the map
$$\begin{aligned}
& \Phi: \mathbb{C}^{2} \longrightarrow \mathbb{C}^{2} \\
& \Phi(z)=\Lambda z, \quad \text { where } \quad z=\left(z^{1}, z^{2}\right)^{t},
\end{aligned}$$
induces a biholomorphism of $\mathbb{T}_{\mathbb{C}}^{2}$ by setting $\tilde{\Phi}([z])=[\Phi(z)]$.
First of all, $\tilde{\Phi}$ is well-defined, since if $z^{\prime}$ and $z$ are equivalent, i.e., if $z^{\prime}=z+$ $P\left(\gamma_{1}+\sqrt{-1} \gamma_{2}\right)$, with $\gamma_{1}, \gamma_{2} \in \mathbb{Z}^{2}$, then
$$\begin{aligned}
\Phi\left(z^{\prime}\right) & =\Lambda z^{\prime}=\Lambda z+\Lambda P\left(\gamma_{1}+\sqrt{-1} \gamma_{2}\right) \\
& =\Lambda z+P A P^{-1} P\left(\gamma_{1}+\sqrt{-1} \gamma_{2}\right) \\
& =\Lambda z+P A\left(\gamma_{1}+\sqrt{-1} \gamma_{2}\right) \\
& =\Lambda z+P\left(\lambda_{1}+\sqrt{-1} \lambda_{2}\right) \\
& =\Phi(z)+P\left(\lambda_{1}+\sqrt{-1} \lambda_{2}\right) \quad \text { with } \lambda_{1}, \lambda_{2} \in \mathbb{Z}^{2},
\end{aligned}$$
so that $\Phi\left(z^{\prime}\right) \sim \Phi(z)$. Furthermore $\tilde{\Phi}^{-1}([z])=\left[\Phi^{-1}(z)\right]$.

We identify $\mathbb{R} \times \mathbb{C}^{2}$ with $\mathbb{R}^{5}$ by $\left(s, z^{1}, z^{2}\right) \longmapsto\left(s, y^{1}, y^{2}, y^{3}, y^{4}\right)$, where $z^{1}=$ $y^{1}+\sqrt{-1} y^{3}, z^{2}=y^{2}+\sqrt{-1} y^{4}$, and consider
$$\begin{aligned}
& T_{1}: \mathbb{R}^{5} \longrightarrow \mathbb{R}^{5} \\
& T_{1}\left(s, y^{1}, y^{2}, y^{3}, y^{4}\right)=\left(s+\zeta, e^{-\zeta} y^{1}, e^{\zeta} y^{2}, e^{-\zeta} y^{3}, e^{\zeta} y^{4}\right),
\end{aligned}$$
then
$$T_{1}\left(s, y^{1}, y^{2}, y^{3}, y^{4}\right)=T_{1}\left(s, z^{1}, z^{2}\right)=\left(s+\zeta, \Phi\left(z^{1}, z^{2}\right)\right) .$$
Hence $T_{1}$ induces a transformation of $\mathbb{R} \times \mathbb{T}_{\mathbb{C}}^{2}$, by setting
$$T_{1}\left(s,\left[\left(z^{1}, z^{2}\right)\right]\right)=\left(s+\zeta,\left[\Phi\left(z^{1}, z^{2}\right)\right]\right) .$$

Define
$$N:=\mathbb{S}^{1} \times \frac{\mathbb{R} \times \mathbb{T}_{\mathbb{C}}^{2}}{<T_{1}>} .$$
Then, we obtain a family of compact 6-dimensional solvmanifold of completely solvable type $N$, called Nakamura manifolds.

We give a numerical example. Let
$$A=\left(\begin{array}{cc}
3 & -1 \\
1 & 0
\end{array}\right),$$
so $A \in \operatorname{SL}(2, \mathbb{Z})$. Then $\mu_{1,2}=\frac{3 \pm \sqrt{5}}{2}$. We set
$$\mu_{1}=\frac{3-\sqrt{5}}{2}=e^{-\zeta} \quad \text { and } \quad \mu_{2}=\frac{3+\sqrt{5}}{2}=e^{\zeta},$$
i.e., $\zeta=\log \left(\frac{3+\sqrt{5}}{2}\right)$. Then
$$P^{-1}=\left(\begin{array}{cc}
\frac{3-\sqrt{5}}{2} & \frac{3+\sqrt{5}}{2} \\
1 & 1
\end{array}\right),$$
and
$$P=-\frac{1}{\sqrt{5}}\left(\begin{array}{cc}
1 & -\frac{3+\sqrt{5}}{2} \\
-1 & \frac{3-\sqrt{5}}{2}
\end{array}\right)$$
and the lattice $\Gamma$ is given by
$$\Gamma=\operatorname{Span}_{\mathbb{Z}}<\left[\begin{array}{c}
-\frac{\sqrt{5}}{5} \\
\frac{\sqrt{5}}{5} \\
0 \\
0
\end{array}\right],\left[\begin{array}{c}
\frac{5+3 \sqrt{5}}{10} \\
\frac{5-3 \sqrt{5}}{10} \\
0 \\
0
\end{array}\right],\left[\begin{array}{c}
0 \\
0 \\
\frac{-\sqrt{5}}{5} \\
\frac{\sqrt{5}}{5}
\end{array}\right],\left[\begin{array}{c}
0 \\
0 \\
\frac{5+3 \sqrt{5}}{10} \\
\frac{5-3 \sqrt{5}}{10}
\end{array}\right]>.$$

Going back to the general setting and by using previous notations, it is straightforward to check that
$$\left\{\begin{array}{lll}
E^{1}:=d s, & E^{2}:=d x, & E^{3}:=e^{s} d y^{1}, \\
E^{4}:=e^{-s} d y^{2}, & E^{5}:=e^{s} d y^{3}, & E^{6}:=e^{-s} d y^{4} .
\end{array}\right.$$
gives rise to a global co-frame on $N$, where $d x$ is the global 1-form on $\mathbb{S}^{1}$. Therefore, with respect to $\left\{E^{i}\right\}_{i \in\{1, \ldots, 6\}}$ the structure equations are the following:
$$\left\{\begin{array}{lll}
d E^{1}=0, & d E^{2}=0, & d E^{3}=E^{13} \\
d E^{4}=-E^{14}, & d E^{5}=E^{15}, & d E^{6}=-E^{16}
\end{array}\right.$$
where as usual $E^{i j}:=E^{i} \wedge E^{j}$. Set
$$\left\{\begin{aligned}
J^{*} E^{1} & :=-E^{2}, \\
J^{*} E^{3} & :=-E^{4}, \\
J^{*} E^{5} & :=-E^{6},
\end{aligned}\right.$$
then $J^{*}$ is an almost complex on $T^{*} N$, inducing an almost complex structure $J$ on $N$. Furthermore,
$$\left\{\begin{array}{l}
\Phi^{1}:=E^{1}+\sqrt{-1} E^{2}, \\
\Phi^{2}:=E^{3}+\sqrt{-1} E^{4}, \\
\Phi^{3}:=E^{5}+\sqrt{-1} E^{6} .
\end{array}\right.$$
is a complex co-frame of (1, 0)-forms on $Y=(N, J)$; one can compute
$$\left\{\begin{array}{l}
d \Phi^{1}=0 \\
d \Phi^{2}=\frac{1}{2}\left(\Phi^{1 \overline{2}}+\Phi^{\overline{1} \overline{2}}\right) \\
d \Phi^{3}=\frac{1}{2}\left(\Phi^{1 \overline{3}}+\Phi^{\overline{1} \overline{3}}\right)
\end{array}\right.$$
where $\Phi^{i \bar{j}}=\Phi^{i} \wedge \overline{\Phi^{j}}$ and so on.
Since $b_{1}(N)=2, b_{2}(N)=5$ (see [dBT06]), we obtain
$$\begin{aligned}
H_{d R}^{1}(N ; \mathbb{R}) & \simeq \operatorname{Span}_{\mathbb{R}}<E^{1}, E^{2}>=\operatorname{Span}_{\mathbb{R}}<\frac{1}{2}\left(\Phi^{1}+\Phi^{\overline{1}}\right), \frac{1}{2 \sqrt{-1}}\left(\Phi^{\overline{1}}-\Phi^{1}\right)>, \\
H_{d R}^{2}(N ; \mathbb{R}) \simeq & \operatorname{Span}_{\mathbb{R}}<E^{12}, E^{34}, E^{56}, E^{36}, E^{45}> \\
\simeq & \operatorname{Span}_{\mathbb{R}}<\sqrt{-1} \Phi^{1 \overline{1}}, \sqrt{-1} \Phi^{2 \overline{2}}, \sqrt{-1} \Phi^{3 \overline{3}}, \\
& \sqrt{-1}\left(\Phi^{\overline{23}}-\Phi^{2 \overline{3}}\right), \sqrt{-1}\left(\Phi^{23}-\Phi^{\overline{23}}\right)>.
\end{aligned}$$
The dual vector fields are given by
$$\left\{\begin{array}{lll}
E_{1}:=\frac{\partial}{\partial s}, & E_{2}:=\frac{\partial}{\partial x}, & E_{3}:=e^{-s} \frac{\partial}{\partial y^{1}}, \\
E_{4}:=e^{s} \frac{\partial}{\partial y^{2}}, & E_{5}:=e^{-s} \frac{\partial}{\partial y^{3}}, & E_{6}:=e^{s} \frac{\partial}{\partial y^{4}} .
\end{array}\right.$$
Let $\sigma$ be a section of $\mathscr{K}_{Y}$. Then $\sigma=f \Phi^{1} \wedge \Phi^{2} \wedge \Phi^{3}$, where $f$ is a smooth complex valued function on $N$.

Lemma $5.1-\bar{\partial} \sigma=0$ if and only if $f=$ const.
Proof. Let $f=u+i v$, where $u: \mathbb{R}^{6} \rightarrow \mathbb{R}$ and $v: \mathbb{R}^{6} \rightarrow \mathbb{R}$ are smooth and $\Gamma$ -periodic. Then, since $\bar{\partial}\left(\Phi^{1} \wedge \Phi^{2} \wedge \Phi^{3}\right)=0$, we have that $\bar{\partial} \sigma=0$ if and only if $\bar{\partial} f=0$. This turns to be equivalent to the following PDEs system
$$\left\{\begin{array}{l}
u_{s}-v_{x}=0, \\
u_{x}+v_{s}=0, \\
e^{-s} u_{y^{1}}-e^{s} v_{y^{2}}=0, \\
e^{s} u_{y^{2}}+e^{-s} v_{y^{1}}=0, \\
e^{-s} u_{y^{3}}-e^{s} v_{y^{4}}=0, \\
e^{s} u_{y^{4}}+e^{-s} v_{y^{3}}=0 .
\end{array}\right.$$
The first two equations imply that $f=f\left(y^{1}, y^{2}, y^{3}, y^{4}\right)$, since $N$ is compact. The other equations imply that $f=$ const since they form an elliptic PDE system. \(\square\)

Therefore,
$$P_{1}(N, J)=1 .$$
Similar computations give
$$P_{m}(N, J)=1 .$$
Indeed, it is easy to see by induction that $\bar{\partial}\left(\left(\Phi^{1} \wedge \Phi^{2} \wedge \Phi^{3}\right)^{\otimes k}\right)=0$ for every $k \geq 1$, so the condition $\bar{\partial}\left(f \cdot\left(\Phi^{1} \wedge \Phi^{2} \wedge \Phi^{3}\right)^{\otimes k}\right)$ is again equivalent to $\bar{\partial} f=0$.

Corollary 5.2 — Let $N$ be a Nakamura manifold of completely solvable type endowed with the (non-integrable) almost complex structure $J$. Then
$$\kappa^{J}(N)=0 .$$
5.1. Kodaira dimension of a deformation of Nakamura manifolds. In this section we will show that the Kodaira dimension is unstable under almost Kähler deformations (cf. [Nak75, Theorem 2]). First of all, the following defines a symplectic structure on $N$
$$\omega:=E^{12}+E^{34}+E^{56},$$
and $g(\cdot, \cdot)=\omega(\cdot, J \cdot)$ gives rise to an almost Kähler structure on $N$.
Let $t=\left(t_{1}, t_{2}, t_{3}, t_{4}\right) \in \mathbb{R}^{4},|t|^{2}<\varepsilon$ and $L_{t} \in(\operatorname{End}(T N))$ be the endomorphism given by
$$\left\{\begin{array}{lll}
L_{t}\left(E_{1}\right)=-t_{1} E_{1}-t_{2} E_{2}, & L_{t}\left(E_{2}\right)=-t_{2} E_{1}+t_{1} E_{2}, & L_{t}\left(E_{3}\right)=E_{3}, \\
L_{t}\left(E_{4}\right)=E_{4}, & L_{t}\left(E_{5}\right)=-t_{3} E_{5}-t_{4} E_{6}, & L_{t}\left(E_{6}\right)=-t_{4} E_{5}+t_{3} E_{6} .
\end{array}\right.$$
Set
$$J_{t}=\left(I+L_{t}\right) J\left(I+L_{t}\right)^{-1} .$$
Then, by a direct computation, we can show the following
Lemma 5.3 - The set $\left\{J_{t}\right\}_{t}$ is a family of $\omega$-compatible almost complex structures on $N$ such that $J_{0}=J$. Furthermore, setting
$$\left\{\begin{array}{l}
\alpha(t):=\frac{2 t_{2}}{t_{1}^{2}+t_{2}^{2}-1}, \\
\beta(t):=\frac{\left(1-t_{1}\right)^{2}+t_{2}^{2}}{t_{1}^{2}+t_{2}^{2}-1}, \\
\gamma(t):=-\frac{\left(1+t_{1}\right)^{2}+t_{2}^{2}}{t_{1}^{2}+t_{2}^{2}-1}, \\
\delta(t):=\frac{2 t_{4}^{2}}{t_{3}^{2}+t_{4}^{2}-1}, \\
\lambda(t):=\frac{\left(1-t_{3}\right)^{2}+t_{4}^{2}}{t_{3}^{2}+t_{4}^{2}-1}, \\
\mu(t):=-\frac{\left(1+t_{3}\right)^{2}+t_{4}^{2}}{t_{3}^{2}+t_{4}^{2}-1},
\end{array}\right.$$
a (1, 0)-coframe for $\left(N, J_{t}\right)$ is given by
$$\left\{\begin{array}{l}
\Phi_{t}^{1}=E^{1}-\sqrt{-1}\left(\alpha(t) E^{1}+\beta(t) E^{2}\right), \\
\Phi_{t}^{2}=E^{3}+\sqrt{-1} E^{4}, \\
\Phi_{t}^{3}=E^{5}-\sqrt{-1}\left(\delta(t) E^{5}+\lambda(t) E^{6}\right) .
\end{array}\right.$$

With these notations, we have in fact
$$J_{t}=\left(\begin{array}{cccccc}
\alpha(t) & \beta(t) & 0 & 0 & 0 & 0 \\
\gamma(t) & -\alpha(t) & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & -1 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & \delta(t) & \lambda(t) \\
0 & 0 & 0 & 0 & \mu(t) & -\delta(t)
\end{array}\right),$$
and we get also the relation $-\alpha^{2}-\beta \gamma=-\delta^{2}-\lambda \mu=1$.
Lemma 5.4 - We have the following equalities:
$$\bar{\partial} \Phi_{t}^{1}=0, \quad \bar{\partial} \Phi_{t}^{2}=\frac{1}{2} \Phi_{t}^{1 \overline{2}}, \quad \bar{\partial} \Phi_{t}^{3}=\frac{1}{2}\left[(1-\sqrt{-1} \delta(t)) \Phi_{t}^{1 \overline{3}}-\sqrt{-1} \delta(t) \Phi_{t}^{\overline{1} 3}\right] .$$

By Lemma 5.3, we easily obtain the dual frame $\left\{V_{1}^{t}, V_{2}^{t}, V_{3}^{t}\right\}$ of global (1,0)-vector fields on $\left(N, J_{t}\right)$ :
$$\left\{\begin{array}{l}
V_{1}^{t}=\frac{1}{2}\left[\left(E_{1}-\frac{\alpha}{\beta}(t) E_{2}\right)+\frac{\sqrt{-1}}{\beta(t)} E_{2}\right], \\
V_{2}^{t}=\frac{1}{2}\left(E^{3}-\sqrt{-1} E_{4}\right), \\
V_{3}^{t}=\frac{1}{2}\left[\left(E_{5}-\frac{\delta}{\lambda}(t) E_{6}\right)+\frac{\sqrt{-1}}{\lambda(t)} E_{6}\right] .
\end{array}\right.$$

More explicitly,
$$\left\{\begin{array}{l}
V_{1}^{t}=\frac{1}{2}\left[\left(\frac{\partial}{\partial s}-\frac{\alpha}{\beta}(t) \frac{\partial}{\partial x}\right)+\frac{\sqrt{-1}}{\beta(t)} \frac{\partial}{\partial x}\right] \\
V_{2}^{t}=\frac{1}{2}\left(e^{-s} \frac{\partial}{\partial y_{1}}-\sqrt{-1} e^{s} \frac{\partial}{\partial y_{2}}\right) \\
V_{3}^{t}=\frac{1}{2}\left[\left(e^{-s} \frac{\partial}{\partial y_{3}}-\frac{\delta}{\lambda}(t) e^{s} \frac{\partial}{\partial y_{4}}\right)+\frac{\sqrt{-1}}{\lambda(t)} e^{s} \frac{\partial}{\partial y_{4}}\right] .
\end{array}\right.$$
Let now $\sigma=f \Phi_{t}^{123}$. Then $\bar{\partial} \sigma=0$ if and only if
$$\bar{\partial} f \wedge \Phi_{t}^{123}-\sqrt{-1} \delta(t) f \Phi_{t}^{\overline{1} 123}=0,$$
which turns to be equivalent to the system
$$\left\{\begin{array}{l}
\bar{V}_{1}^{t} f-\sqrt{-1} \delta(t) f=0, \\
\bar{V}_{2}^{t} f=0, \\
\bar{V}_{3}^{t} f=0 .
\end{array}\right.$$
By the second and third equation in (5.8), we obtain
$$\left(V_{2}^{t} \bar{V}_{2}^{t}+V_{3}^{t} \bar{V}_{3}^{t}\right) f=0 .$$
As $V_{2}^{t} \bar{V}_{2}^{t}+V_{3}^{t} \bar{V}_{3}^{t}$ is a real operator, setting $f=u+\sqrt{-1} v$, the last complex equation is equivalent to the following two real equations,
$$\left\{\begin{aligned}
\left(V_{2}^{t} \bar{V}_{2}^{t}+V_{3}^{t} \bar{V}_{3}^{t}\right) u & =0 \\
\left(V_{2}^{t} \bar{V}_{2}^{t}+V_{3}^{t} \bar{V}_{3}^{t}\right) v & =0 .
\end{aligned}\right.$$
By using (5.7), a direct computation shows that the second order differential operator $4\left(V_{2}^{t} \bar{V}_{2}^{t}+V_{3}^{t} \bar{V}_{3}^{t}\right)$ is given by
$$4\left(V_{2}^{t} \bar{V}_{2}^{t}+V_{3}^{t} \bar{V}_{3}^{t}\right)=e^{-2 s} \frac{\partial^{2}}{\partial y_{1}^{2}}+e^{2 s} \frac{\partial^{2}}{\partial y_{2}^{2}}+e^{-2 s} \frac{\partial^{2}}{\partial y_{3}^{2}}+\frac{\left(1+\delta^{2}(t)\right)}{\lambda^{2}(t)} e^{2 s} \frac{\partial^{2}}{\partial y_{4}^{2}}-2 \frac{\delta(t)}{\lambda(t)} \frac{\partial^{2}}{\partial y_{3} \partial y_{4}}$$
and one can check that it is elliptic. Consequently, $u=u(s, x), v=v(s, x)$, that is $f=f(s, x)$.

The first equation in (5.8) is then equivalent to the system
$$\left\{\begin{array}{l}
2 \delta u=\frac{\partial v}{\partial s}-\frac{\alpha}{\beta} \frac{\partial v}{\partial x}-\frac{1}{\beta} \frac{\partial u}{\partial x} \\
2 \delta v=\frac{\partial u}{\partial s}-\frac{\alpha}{\beta} \frac{\partial u}{\partial x}+\frac{1}{\beta} \frac{\partial v}{\partial x} .
\end{array}\right.$$

To resolve system (5.10), we begin by observing that it is equivalent to
$$\left\{\begin{array}{l}
\frac{1}{\beta} \frac{\partial u}{\partial x}=\frac{\partial v}{\partial s}-\frac{\alpha}{\beta} \frac{\partial v}{\partial x}-2 \delta u \\
\frac{\partial u}{\partial s}=\alpha\left(\frac{\partial v}{\partial s}-\frac{\alpha}{\beta} \frac{\partial v}{\partial x}-2 \delta u\right)-\frac{1}{\beta} \frac{\partial v}{\partial x}+2 \delta v,
\end{array}\right.$$
hence to
$$\left\{\begin{aligned}
\frac{\partial u}{\partial s} & =\alpha \frac{\partial v}{\partial s}+\gamma \frac{\partial v}{\partial x}-2 \alpha \delta u+2 \delta v \\
\frac{\partial u}{\partial x} & =\beta \frac{\partial v}{\partial s}-\alpha \frac{\partial v}{\partial x}-2 \beta \delta u .
\end{aligned}\right.$$
Taking the derivative with respect to $x$ of the first equation, and with respect to $s$ of the second one, we can then see that the following relation holds:
$$\left(\beta \frac{\partial^{2}}{\partial s^{2}}-2 \alpha \frac{\partial^{2}}{\partial s \partial x}-\gamma \frac{\partial^{2}}{\partial x^{2}}\right) v=2 \beta \delta \frac{\partial u}{\partial s}-2 \alpha \delta \frac{\partial u}{\partial x}+2 \delta \frac{\partial v}{\partial x}=4 \beta \delta^{2} v .$$
Observe that the operator in the left term is elliptic.
So, if $\delta(t)=0$ (i.e., for $t=\left(t_{1}, t_{2}, t_{3}, 0\right)$ ), we obtain that $v$ must be constant, which forces $u$ to be also constant. This shows that $P_{1}\left(M, J_{t}\right)=1$ for $t=\left(t_{1}, t_{2}, t_{3}, 0\right)$. We observe that a similar computation shows that $u$ also satisfies
$$\left(\beta \frac{\partial^{2}}{\partial s^{2}}-2 \alpha \frac{\partial^{2}}{\partial s \partial x}-\gamma \frac{\partial^{2}}{\partial x^{2}}\right) u=4 \beta \delta^{2} u .$$

Since we are looking for periodic solutions of (5.11), we can work with Fourier series and assume that the solution $u$ is of the form
$$u(s, x)=\sum_{n, m \in \mathbb{Z}} A_{n m} e^{2 \pi \sqrt{-1}\left(n x+\frac{m}{\zeta} s\right)}$$
Assume that $u$ is such a solution, with $A_{n m} \neq 0$ for some pair $(n, m)$ : we deduce that the relation
$$\frac{\beta^{2}}{\zeta^{2}} m^{2}-2 \frac{\alpha}{\zeta} n m-\gamma n^{2}=-\frac{\beta \delta^{2}}{\pi^{2}}$$
holds, and since $\beta(0)=-1$ we can see this as an equation of degree 2 in the unknown $m$. The 'key observation' is that the discriminant of (5.12), which is $-\frac{4}{\zeta^{2}}\left(n^{2}+\frac{\beta^{2} \delta^{2}}{\pi^{2}}\right)$, must be non-negative as we are assuming $u$ to be a solution, which forces $n=\beta \delta=0$. As $\beta(0)=-1$ (and so $\beta(t) \neq 0$ for $|t|<\varepsilon$ ), the last relation reduces to $\delta=0$. In particular, this shows that if $\delta(t) \neq 0$, then the only solution to (5.11) and to (5.10) is the trivial one. Assuming instead that $n=\delta=0$, relation (5.12) implies that $m=0$ : this means that a non-trivial solution for (5.11) must be constant.

We have then shown that
$$P_{1}(N, J)= \begin{cases}1 & \text { if } \delta(t)=0 \\ 0 & \text { if } \delta(t) \neq 0 .\end{cases}$$

Finally, one can prove by induction that $\bar{\partial}\left(\left(\Phi_{t}^{123}\right)^{\otimes m}\right)=-m \frac{\sqrt{-1} \delta}{2} \Phi_{t}^{\overline{1}} \wedge\left(\Phi_{t}^{123}\right)^{\otimes m}$, hence it follows that $\bar{\partial}\left(f\left(\Phi_{t}^{123}\right)^{\otimes m}\right)=0$ if and only if
$$\bar{V}_{1}^{t} f-m \frac{\sqrt{-1} \delta}{2} f=0, \quad \bar{V}_{2}^{t} f=\bar{V}_{3}^{t} f=0,$$
so the same methods apply also for pluricanonical differentials (just replace $\delta$ with $m \delta)$.

Theorem 5.5 - Let $Y_{t}=\left(N, g_{t}, J_{t}\right)$ be the almost Kähler family of deformations the Nakamura manifold defined above, where $g_{t}(\cdot, \cdot)=\omega\left(\cdot, J_{t} \cdot\right)$. Take any $t=$ $\left(t_{1}, t_{2}, t_{3}, t_{4}\right) \in \mathbb{R}^{4},|t|^{2}<\varepsilon$. Then
$$\kappa^{J_{t}}(N)= \begin{cases}0 & \text { if } t_{4}=0, \\ -\infty & \text { if } t_{4} \neq 0 .\end{cases}$$
5.2. Ricci and scalar curvature of the deformed Nakamura manifold. In this section we consider the almost complex manifolds $\left(N, J_{t}\right)$ where $J_{t}$ is given by (5.6). With the notations introduced in (5.1), let us consider the real (1, 1)-form
$$\omega=E^{1} \wedge E^{2}+E^{3} \wedge E^{4}+E^{5} \wedge E^{6}:$$
it is then easy to observe that
$$d \omega=0, \quad \omega\left(J_{t} \cdot, J_{t} \cdot\right)=\omega(\cdot, \cdot) .$$
As a consequence, we can endow $\left(N, J_{t}\right)$ with the structure of an almost Kähler manifold once we consider the Riemannian metric $g_{t}$ given as $g_{t}(\cdot, \cdot)=\omega\left(\cdot, J_{t} \cdot\right)$.

A $g_{t}$-orthonormal frame for $Y_{t}=\left(N, g_{t}, J_{t}\right)$ is then provided by
$$\begin{array}{ll}
E_{1}^{\prime}=\frac{1}{\sqrt{\gamma}} E_{1}, & E_{3}^{\prime}=E_{3}, \\
E_{2}^{\prime}=\frac{\alpha}{\sqrt{\gamma}} E_{1}+\sqrt{\gamma} E_{2}, & E_{4}^{\prime}=E_{4}, \quad E_{6}^{\prime}=\frac{1}{\sqrt{\mu}} E_{5}, \\
\frac{\delta}{\sqrt{\mu}} E_{5}+\sqrt{\mu} E_{6},
\end{array}$$
and with respect to this frame the almost complex structure $J_{t}$ takes the standard form:
$$\begin{array}{lll}
J E_{1}^{\prime}=E_{2}^{\prime} & J E_{3}^{\prime}=E_{4}^{\prime}, & J E_{5}^{\prime}=E_{6}^{\prime}, \\
J E_{2}^{\prime}=-E_{1}^{\prime}, & J E_{4}^{\prime}=-E_{3}^{\prime}, & J E_{6}^{\prime}=-E_{5}^{\prime} .
\end{array}$$

We can then introduce the following complex frame, which is $h_{t}$-unitary on $T^{1,0} N$, where $h_{t}$ denotes the Hermitian extension of $g_{t}$ to $T_{\mathbb{C}} N$ :
$$\begin{array}{ll}
z_{1}=\frac{\sqrt{2}}{2}\left(E_{1}^{\prime}-\sqrt{-1} E_{2}^{\prime}\right), & \bar{z}_{1}=\frac{\sqrt{2}}{2}\left(E_{1}^{\prime}+\sqrt{-1} E_{2}^{\prime}\right), \\
z_{2}=\frac{\sqrt{2}}{2}\left(E_{3}^{\prime}-\sqrt{-1} E_{4}^{\prime}\right), & \bar{z}_{2}=\frac{\sqrt{2}}{2}\left(E_{3}^{\prime}+\sqrt{-1} E_{4}^{\prime}\right), \\
z_{3}=\frac{\sqrt{2}}{2}\left(E_{5}^{\prime}-\sqrt{-1} E_{6}^{\prime}\right), & \bar{z}_{3}=\frac{\sqrt{2}}{2}\left(E_{5}^{\prime}+\sqrt{-1} E_{6}^{\prime}\right) .
\end{array}$$

Dually, we can define the coframe
$$\begin{array}{ll}
E^{1^{\prime}}=\sqrt{\gamma} E^{1}-\frac{\alpha}{\sqrt{\gamma}} E^{2}, & E^{3^{\prime}}=E^{3}, \quad E^{5^{\prime}}=\sqrt{\mu} E^{5}-\frac{\delta}{\sqrt{\mu}} E^{6}, \\
E^{2^{\prime}}=\frac{1}{\sqrt{\gamma}} E^{2}, & E^{4^{\prime}}=E^{4}, \quad E^{6^{\prime}}=\frac{1}{\sqrt{\mu}} E^{6},
\end{array}$$
to which corresponds the complex coframe
$$\begin{array}{lll}
\Phi^{1}=\frac{\sqrt{2}}{2}\left(E^{1^{\prime}}+\sqrt{-1} E^{2^{\prime}}\right), & \bar{\Phi}^{1}=\frac{\sqrt{2}}{2}\left(E^{1^{\prime}}-\sqrt{-1} E^{2^{\prime}}\right), \\
\Phi^{2}=\frac{\sqrt{2}}{2}\left(E^{3^{\prime}}+\sqrt{-1} E^{4^{\prime}}\right), & \bar{\Phi}^{2}=\frac{\sqrt{2}}{2}\left(E^{3^{\prime}}-\sqrt{-1} E^{4^{\prime}}\right), \\
\Phi^{3}=\frac{\sqrt{2}}{2}\left(E^{5^{\prime}}+\sqrt{-1} E^{6^{\prime}}\right), & \bar{\Phi}^{3}=\frac{\sqrt{2}}{2}\left(E^{5^{\prime}}-\sqrt{-1} E^{6^{\prime}}\right) .
\end{array}$$

Lemma 5.6 - The (real) torsion forms for the canonical connection $\nabla^{c}$ on $Y_{t}$ are
$$\begin{aligned}
& \Theta^{1}=0 \\
& \Theta^{2}=0, \\
& \Theta^{3}=\frac{1}{2 \sqrt{\gamma}} E^{\prime 13}+\frac{\alpha}{2 \sqrt{\gamma}} E^{\prime 14}+\frac{\alpha}{2 \sqrt{\gamma}} E^{\prime 23}-\frac{1}{2 \sqrt{\gamma}} E^{\prime 24}, \\
& \Theta^{4}=\frac{\alpha}{2 \sqrt{\gamma}} E^{\prime 13}-\frac{1}{2 \sqrt{\gamma}} E^{\prime 14}-\frac{1}{2 \sqrt{\gamma}} E^{\prime 23}-\frac{\alpha}{2 \sqrt{\gamma}} E^{\prime 24}, \\
& \Theta^{5}=\frac{1}{2 \sqrt{\gamma}}(1-\alpha \delta) E^{\prime 15}+\frac{1}{2 \sqrt{\gamma}}(\alpha+\delta) E^{\prime 16}+\frac{1}{2 \sqrt{\gamma}}(\alpha+\delta) E^{\prime 25}-\frac{1}{2 \sqrt{\gamma}}(1-\alpha \delta) E^{\prime 26}, \\
& \Theta^{6}=\frac{1}{2 \sqrt{\gamma}}(\alpha+\delta) E^{\prime 15}-\frac{1}{2 \sqrt{\gamma}}(1-\alpha \delta) E^{\prime 16}-\frac{1}{2 \sqrt{\gamma}}(1-\alpha \delta) E^{\prime 25}-\frac{1}{2 \sqrt{\gamma}}(\alpha+\delta) E^{\prime 26},
\end{aligned}$$
where $E^{\prime i j}$ stands for $E^{i^{\prime}} \wedge E^{j^{\prime}}$ and so on.
Proof. Thanks to Corollary 3.8, we only need to compute the Nijenhuis tensor of $J_{t}$, which can be done by a direct computation. \(\square\)

Corollary 5.7 — The (complex) torsion forms for the holomorphic torsion of the canonical connection $\nabla^{c}$ on $Y_{t}$ are
$$\begin{aligned}
& \Theta^{1^{\prime}}=0 \\
& \Theta^{2^{\prime}}=\frac{\sqrt{2}}{2 \sqrt{\gamma}}(1+\sqrt{-1} \alpha) \bar{\Phi}^{1} \wedge \bar{\Phi}^{2}, \\
& \Theta^{3^{\prime}}=\frac{\sqrt{2}}{2 \sqrt{\gamma}}(1+\sqrt{-1} \alpha)(1+\sqrt{-1} \delta) \bar{\Phi}^{1} \wedge \bar{\Phi}^{3} .
\end{aligned}$$
Proof. From the relation
$$\begin{array}{ll}
E_{1}^{\prime}=\frac{\sqrt{2}}{2}\left(z_{1}+\bar{z}_{1}\right), & E_{2}^{\prime}=\sqrt{-1} \frac{\sqrt{2}}{2}\left(z_{1}-\bar{z}_{1}\right), \\
E_{3}^{\prime}=\frac{\sqrt{2}}{2}\left(z_{2}+\bar{z}_{2}\right), & E_{4}^{\prime}=\sqrt{-1} \frac{\sqrt{2}}{2}\left(z_{2}-\bar{z}_{2}\right), \\
E_{5}^{\prime}=\frac{\sqrt{2}}{2}\left(z_{3}+\bar{z}_{3}\right), & E_{6}^{\prime}=\sqrt{-1} \frac{\sqrt{2}}{2}\left(z_{3}-\bar{z}_{3}\right),
\end{array}$$
we can see that the complexified torsion of the canonical connection satisfies
$$T=\Theta^{1} \otimes E_{1}^{\prime}+\Theta^{2} \otimes E_{2}^{\prime}+\ldots=\frac{\sqrt{2}}{2}\left(\Theta^{1}+\sqrt{-1} \Theta^{2}\right) \otimes z_{1}+\frac{\sqrt{2}}{2}\left(\Theta^{1}-\sqrt{-1} \Theta^{2}\right) \otimes \bar{z}_{1}+\ldots .$$
So the torsion forms for the holomorphic curvature of the canonical connection are
$$\begin{aligned}
& \Theta^{1^{\prime}}=\frac{\sqrt{2}}{2}\left(\Theta^{1}+\sqrt{-1} \Theta^{2}\right), \\
& \Theta^{2^{\prime}}=\frac{\sqrt{2}}{2}\left(\Theta^{3}+\sqrt{-1} \Theta^{4}\right), \\
& \Theta^{3^{\prime}}=\frac{\sqrt{2}}{2}\left(\Theta^{5}+\sqrt{-1} \Theta^{6}\right)
\end{aligned}$$
and we can compute them from the knowledge of the real curvature forms. \(\square\)

Our next step is to compute the connection forms $\theta_{j}^{i}$ for the canonical connection $\nabla^{c}$, which can be done by solving explicitly the structure equations
$$\left\{\begin{array}{l}
d \Phi^{1}+\theta_{1}^{1} \wedge \Phi^{1}+\theta_{2}^{1} \wedge \Phi^{2}+\theta_{3}^{1} \wedge \Phi^{3}=\Theta^{1^{\prime}} \\
d \Phi^{2}+\theta_{1}^{2} \wedge \Phi^{1}+\theta_{2}^{2} \wedge \Phi^{2}+\theta_{3}^{2} \wedge \Phi^{3}=\Theta^{2^{\prime}} \\
d \Phi^{3}+\theta_{1}^{3} \wedge \Phi^{1}+\theta_{2}^{3} \wedge \Phi^{2}+\theta_{3}^{3} \wedge \Phi^{3}=\Theta^{3^{\prime}} \\
\theta_{j}^{i}+\bar{\theta}_{i}^{j}=0 \quad(i, j=1,2,3) .
\end{array}\right.$$
This is a standard computation, so we prefer to skip all the details and present only the solution in the following Lemma.

Lemma 5.8 - Let $Y_{t}$ be the family of almost Kähler deformations of the Nakamura threefold under consideration. The complex connection forms for the canonical connection $\nabla^{c}$ of $Y_{t}$ are then
$$\begin{array}{ll}
\theta_{1}^{1}=0, & \theta_{2}^{1}=-\frac{\sqrt{2}}{2 \sqrt{\gamma}}(1+\sqrt{-1} \alpha) \Phi^{2}, \\
\theta_{2}^{2}=0, & \theta_{3}^{1}=-\frac{\sqrt{2}}{2 \sqrt{\gamma}}(1+\sqrt{-1} \alpha)(1-\sqrt{-1} \delta) \Phi^{3}, \\
\theta_{3}^{2}=0, & \theta_{3}^{3}=\frac{\sqrt{2}}{2 \sqrt{\gamma}}(\alpha+\sqrt{-1}) \delta \Phi^{1}-\frac{\sqrt{2}}{2 \sqrt{\gamma}}(\alpha-\sqrt{-1}) \delta \bar{\Phi}^{1} .
\end{array}$$

From the knowledge of the connection forms, we can deduce the curvature forms via the second structure equations
$$\Psi=\left(\Psi_{j}^{i}\right)=d \theta+\theta \wedge \theta, \quad \text { where } \theta=\left(\theta_{j}^{i}\right) .$$
The result is
$$\begin{aligned}
& \Psi_{1}^{1}=-\frac{1}{2 \gamma}\left(1+\alpha^{2}\right) \Phi^{2} \wedge \bar{\Phi}^{2}-\frac{1}{2 \gamma}\left(1+\alpha^{2}\right)\left(1+\delta^{2}\right) \Phi^{3} \wedge \bar{\Phi}^{3}, \\
& \Psi_{2}^{1}=-\frac{1}{2 \gamma}\left(1+\alpha^{2}\right) \Phi^{1} \wedge \bar{\Phi}^{2}-\frac{1}{2 \gamma}(1+\sqrt{-1} \alpha)^{2} \bar{\Phi}^{1} \wedge \bar{\Phi}^{2}, \\
& \Psi_{3}^{1}=\frac{1}{2 \gamma}\left(1+\alpha^{2}\right)\left(1+\delta^{2}\right) \Phi^{1} \wedge \bar{\Phi}^{2}+\frac{1}{2 \gamma}(1+\sqrt{-1} \alpha)^{2}\left(1+\delta^{2}\right) \bar{\Phi}^{1} \wedge \bar{\Phi}^{3}, \\
& \Psi_{2}^{2}=\frac{1}{2 \gamma}\left(1+\alpha^{2}\right) \Phi^{2} \wedge \bar{\Phi}^{2}, \\
& \Psi_{3}^{2}=\frac{1}{2 \gamma}\left(1+\alpha^{2}\right)(1-\sqrt{-1} \delta) \Phi^{3} \wedge \bar{\Phi}^{2}, \\
& \Psi_{3}^{3}=\frac{1}{2 \gamma}\left(1+\alpha^{2}\right)\left(1+\delta^{2}\right) \Phi^{3} \wedge \bar{\Phi}^{3},
\end{aligned}$$
and the other curvature forms are deduced from these thanks to the relation $\Psi_{j}^{i}+$ $\bar{\Psi}_{i}^{j}=0$.

Recall that the $k \bar{l}$-component of the Ricci curvature of the canonical connection is expressed by
$$R_{k \bar{l}}=\sum_{i=1}^{3} R_{i k \bar{l}}^{i}, \quad \text { with }\left(\Psi_{j}^{i}\right)^{1,1}=\sum_{k, l} R_{j k \bar{l}}^{i} \Phi^{i} \wedge \overline{P h} i^{j} .$$
We have then no problems with proving the following result.
Theorem 5.9 - Let $Y_{t}$ be the family of almost Kähler deformations of the Nakamura threefold under consideration. For every value of the parameter $t$, the canonical connection $\nabla^{c}$ on $Y_{t}$ is Ricci-flat, and in particular its scalar curvature vanishes.

Remark 5.10 — As it was mentioned in the Introduction, we can see that the family of almost Kähler structures on the differentiable manifold underlying the Nakamura threefold we are considering has the following properties:
\begin{itemize}
\item[(1)] there are members of this family having Kodaira dimension 0 and $-\infty$;
\item[(2)] the canonical connection of all the members has vanishing Ricci curvature.
\end{itemize}
Such a behaviour in the integrable case was pointed out in by Tosatti in [Tos15, Example 3.2], based on the original work of Nakamura (see [Nak75]).

\section*{References}
\begin{itemize}
\item[] [CZ18] Haojie Chen and Weiyi Zhang. Kodaira dimensions of almost complex manifolds. arXiv preprint arXiv:1808.00885 [math.DG], 2018. (Cited on pages 1, 2, 3, and 10.)
\item[] [dBT96] Paolo de Bartolomeis and Gang Tian. Stability of complex vector bundles. J. Differential Geom., 43(2):231-275, 1996. (Cited on page 4.)
\item[] [dBT06] Paolo de Bartolomeis and Adriano Tomassini. On solvable generalized Calabi-Yau manifolds. Ann. Inst. Fourier (Grenoble), 56(5):1281-1296, 2006. (Cited on page 16.)
\item[] [Gau97] Paul Gauduchon. Hermitian connections and Dirac operators. Boll. Un. Mat. Ital. B (7), 11(2, suppl.):257-288, 1997. (Cited on pages 4, 6, and 8.)
\item[] [Li10] Tian-Jun Li. Symplectic Calabi-Yau surfaces. In Handbook of geometric analysis, No. 3, volume 14 of Adv. Lect. Math. (ALM), pages 231-356. Int. Press, Somerville, MA, 2010. (Cited on pages 3 and 14.)
\item[] [Nak75] Iku Nakamura. Complex parallelisable manifolds and their small deformations. J. Differential Geometry, 10:85-112, 1975. (Cited on pages 14, 17, and 21.)
\item[] [Tos15] Valentino Tosatti. Non-Kähler Calabi-Yau manifolds. In Analysis, complex geometry, and mathematical physics: in honor of Duong H. Phong, volume 644 of Contemp. Math., pages 261-277. Amer. Math. Soc., Providence, RI, 2015. (Cited on page 21.)
\item[] [TW11] Valentino Tosatti and Ben Weinkove. The Calabi-Yau equation on the Kodaira-Thurston manifold. J. Inst. Math. Jussieu, 10(2):437-447, 2011. (Cited on page 14.)
\item[] [TWY08] Valentino Tosatti, Ben Weinkove, and Shing-Tung Yau. Taming symplectic forms and the Calabi-Yau equation. Proc. Lond. Math. Soc. (3), 97(2):401-424, 2008. (Cited on page 4.)
\item[] [Yan17] Xiaokui Yang. Scalar curvature, kodaira dimension and $\hat{A}$-genus. arXiv preprint arXiv:1706.01122 [math.DG], 2017. (Cited on page 2.)
\item[] [Yan19] Xiaokui Yang. Scalar curvature on compact complex manifolds. Trans. Amer. Math. Soc., 371(3):2073-2087, 2019. (Cited on page 2.)
\item[] [Yau74] Shing-Tung Yau. On the curvature of compact Hermitian manifolds. Invent. Math., 25:213-239, 1974. (Cited on page 2.)
\end{itemize}

Dipartimento di Matematica ed Informatica "U. Dini", Università degli Studi di Firenze, Viale Morgagni 67/A, 50134 Firenze, Italy

E-mail address: andrea.cattaneo@unifi.it
E-mail address: antonella.nannicini@unifi.it
Dipartimento di Scienze Matematiche, Fisiche ed Informatiche Unità di Matematica e Informatica, Università di Parma, Parco Area delle Scienze 53/A, 43124, Parma, Italy

E-mail address: adriano.tomassini@unipr.it