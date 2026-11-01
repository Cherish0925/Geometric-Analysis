---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Q-Gorenstein deformations of non-normal surfaces]

---
source_file: math_0504211.pdf
converter: mathpix
format: mmd
---

\title{
$\mathbb{Q}$-GORENSTEIN DEFORMATIONS OF NONNORMAL SURFACES
}

\author{
NIKOLAOS TZIOLAS
}

\begin{abstract}
Let $\Delta \subset H$ be the germ of a non-normal surface along a proper curve with smooth components such that the high index points of $H$ are semilog-terminal and the Gorenstein singular points are semi-log-canonical. We describe the sheaf $T_{q G}^{1}(H)$ of $\mathbb{Q}$-Gorenstein deformations of $H$ and we show that the divisorial part of the support of $T_{q G}^{1}(H)$ is $\Delta$. Moreover, we show that if $C$ is any irreducible component of $\Delta$, then the locally free part of $T_{q G}^{1}(H) \otimes$ $\mathcal{O}_{C}$ is a line bundle on $C$ and we obtain a formula for its degree. Finally we obtain criteria for $\Delta \subset H$ to have $\mathbb{Q}$-Gorenstein terminal smoothings.
\end{abstract}

\section*{1. Introduction}

The purpose of this paper is to describe the $\mathbb{Q}$-Gorenstein smoothings of a germ $\Delta \subset H$ of a nonnormal surface with semi-log-canonical (slc) singularities along a proper curve with smooth irreducible components. $\mathbb{Q}$-Gorenstein smoothings of such surface germs provide important information about the components of the versal deformation space $\operatorname{Def}(X)$ of an isolated rational surface singularity $0 \in$ $X$. They are also closely related to 3-fold terminal extremal neighborhoods, a fundamental class of birational maps that appear in the three dimensional minimal model program, and they help to understand the boundary of the compactification of the moduli space of surfaces of general type.

A stable surface is a proper two-dimensional reduced scheme $H$ such that $H$ has only semi-log-canonical singularities and $\omega_{H}^{[k]}$ is locally free and ample for some $k>0$. The boundary of the compactification of surfaces of general type consists of smoothable stable surfaces. Therefore it is interesting to know which stable surfaces are smoothable.

Let $0 \in X$ be the germ of a rational surface singularity. Kollár Ko91 has made a series of conjectures concerning the components of the versal deformation space $\operatorname{Def}(X)$. A $P$-resolution of of $X$ [KoBa88] is a proper birational map $g: H \longrightarrow X$ such that
\begin{itemize}
\item[(1)] $H$ is Cohen Macaulay and Gorenstein outside finitely many points
\item[(2)] $K_{H}$ is $g$-ample
\item[(3)] $H$ has a $\mathbb{Q}$-Gorenstein smoothing.
\end{itemize}

\footnotetext{
1991 Mathematics Subject Classification. Primary 14E30, 14E35.
Key words and phrases. Algebraic geometry.
The author was partially supported by a JSPS fellowship, \# PE 04054.
}

Kollár conjectures that there is a one-to-one correspondence between the components of the versal deformation space $\operatorname{Def}(X)$ of $X$, and $q G$-components of deformations of $P$-resolutions [Ko91]. This conjecture is known to be true for Gorenstein surface singularities, quotient singularities [KoBa88] and rational quadruple points [Ste91].

If a $P$-resolution $H$ of a rational surface singularity is normal, then its deformation theory can be described by the local deformations around the singular points. However, there are examples [Ko91] that show that a $P$-resolution may not be normal. In such a case it is possible that locally $H$ is smoothable but $H$ itself is not. Therefore it is important to give a more detailed study of the deformation theory of nonnormal surface germs along smooth proper curves.

There is also a close relation between $\mathbb{Q}$-Gorenstein smoothings of surface germs $\Delta \subset H$ as above and 3-fold terminal extremal neighborhoods. A 3-fold terminal extremal neighborhood [Ko-Mo92] is a proper birational map $\Delta \subset Y \xrightarrow{f} X \ni P$ such that $Y$ is the germ of a 3-fold along a proper curve $\Delta, \Delta_{\text {red }}=f^{-1}(P), X$ and $Y$ are terminal, and $-K_{Y}$ is $f$-ample. Then $Y$ is a one-parameter $\mathbb{Q}$-Gorenstein smoothing of the general member $H \in\left|\mathcal{O}_{Y}\right|$. In general $H$ may or may not be normal and its singularities may be hard to describe. Kollàr and Mori [Ko-Mo92] showed that given a terminal extremal neighborhood as above, the general members of $\left|-K_{Y}\right|$ and $\left|-K_{X}\right|$ have DuVal singularities. If the neighborhood is isolated and the general member of $\left|-K_{X}\right|$ is of type $A_{n}$, then the general member $H \in\left|\mathcal{O}_{Y}\right|$ has semi-log-canonical (slc) singularities, and in fact the points of index bigger than 1 are semi-log-terminal (slt) [Tzi05]. The same is true if the neighborhood is divisorial and the general member $S \in\left|-K_{X}\right|$ that contains $\Gamma=f(E)$, where $E$ is the $f$-exceptional divisor, is of type $A_{m}$. Hence a detailed description of the $\mathbb{Q}$ -Gorenstein deformations of non-normal surface germs $\Delta \subset H$ with slc singularities will provide information about the structure of terminal extremal neighborhoods.

Let $\Delta \subset H$ be the germ of a surface with slc singularities along a smooth proper curve such that the points of index bigger than 1 are slt. By the classification of slc singularities [KoBa88], if such a germ has a terminal smoothing then its singularities are either normal crossing points, pinch points, degenerate cusps of embedding dimension at most 4 or slt points analytically isomorphic to $(x y=0) / \mathbb{Z}_{n}(a,-a, 1)$, $(a, n)=1$. Such singularities we call singularities of class $q G$. A surface germ $\Delta \subset H$ with singularities of class $q G$ has local $\mathbb{Q}$-Gorenstein smoothings but there is not necessarily a global one extending the local.

The purpose of this paper is to study when the local $\mathbb{Q}$-Gorenstein smoothings extend to a global. To put the problem in the proper setting, we define deformation functors $\operatorname{Def}^{q G}(H)$ and $\operatorname{Def}_{\text {loc }}^{q G}(H)$ that parametrize global and collections of local $\mathbb{Q}$-Gorenstein deformations, and we study the natural transformation $\phi: D e f^{q G}(H) \longrightarrow D e f_{\text {loc }}^{q G}(H)$ and in particular the induced map on tangent spaces.

Theorem 3.1 describes the tangent space of $\operatorname{Def}_{\text {loc }}^{q G}(H)$. This is $H^{0}\left(T_{q G}^{1}(H)\right)$, where $T_{q G}^{1}(H) \subset T^{1}(H)$ is the sheaf of local $\mathbb{Q}$-Gorenstein deformations of $H$. It is shown that the divisorial part of the support of $T_{q G}^{1}(H)$ is $\Delta$. Let $C$ be an irreducible component of $\Delta$ and $L_{C}$ the locally free part of $T_{q G}^{1}(H) \otimes \mathcal{O}_{C}$. It is shown that this is a line bundle and a formula for its degree is given which involves the self intersection $\tilde{C}^{2}$ and some analytic invariants of the singularities of $H$, where $\tilde{C}=\pi^{-1}(C)$ and $\pi: \tilde{H} \longrightarrow H$ is the normalization of $H$. At this point I must
mention that a special case of Theorem 3.1 appeared without proof in [Ko91], and in fact this was the original motivation for this work.

If $H^{2}\left(T_{H}\right)=0$, then Proposition 3.2 says that the natural transformation of the deformation functors $\operatorname{Def}^{q G}(H) \longrightarrow D e f_{l o c}^{q G}(H)$ is smooth. In particular this is the case when $H$ is a modification of an isolated singularity. Moreover, if every irreducible component of $\Delta$ is a smooth rational curve, then $H$ has global $\mathbb{Q}$-Gorenstein smoothings if and only if $d_{c}=\operatorname{deg} L_{C} \geq 0$.

As applications, Corollary 3.3 gives a necessary and sufficient condition for a germ $\Delta \subset H$ to have a one parameter terminal $\mathbb{Q}$-Gorenstein smoothing in the case that $\Delta$ is a rational cycle of curves, and Corollary 3.4 shows that under some conditions there exists a terminal extremal neighborhood $\Delta \subset Y \xrightarrow{f} X \ni P$, such that $H \in\left|\mathcal{O}_{Y}\right|$.

I would like to thank János Kollár for many fruitfull discussions and exchange of ideas. Also Lemma 3.10 was communicated to me by him.

\section*{2. Preliminaries}

Let $\mathcal{F}$ be a coherent sheaf on a scheme $X$. We denote $\mathcal{F}^{[n]}=\left(\mathcal{F}^{\otimes n}\right)^{* *}$.
Definition 2.1. Let $X$ be either a variety, an analytic space or the germ of a singularity, such that it is Cohen Macaulay and Gorenstein in codimension 1. Let $Y$ be the total space of a one parameter deformation of $X$. Then we say that $Y$ is a $\mathbb{Q}$-Gorenstein deformation if $\omega_{Y}^{[n]}$ is locally free for some $n$. The assumptions on $X$ assure that this makes sense even for nonnormal varieties.

We will now define three deformation functors. Let $\operatorname{Art}(\mathbb{C})$ be the category of finite local Artin $\mathbb{C}$-algebras and $\operatorname{Sh}(X)$ the category of sheaves of sets on $X$.

Definition 2.2 (Definition 3.17 [KoBa88]). The functor of global $\mathbb{Q}$-Gorenstein deformations is the functor $\operatorname{Def}^{q G}(X): \operatorname{Art}(\mathbb{C}) \longrightarrow$ Sets such that for any finite local $\mathbb{C}$-algebra $A, \operatorname{Def}^{q G}(X)(A)$ is the set of isomorphism classes of flat morphisms $f: Y \longrightarrow S=\operatorname{Spec}(A)$, such that $Y \otimes k(A) \cong X$, the sheaf $\omega_{Y / S}^{[n]}$ is invertible for some $n$.

It is not immediately clear that $\operatorname{Def}^{q G}(X)$ as defined above is indeed a functor. For this to be true, the property that the relative dualizing sheaf $\omega_{Y / S}$ is $\mathbb{Q}$ -Gorenstein should be stable under base extension. However, this is true Has-Kov04, Lemma 2.6] and therefore $\operatorname{Def}^{q G}(X)$ is a functor and moreover a subfunctor of the versal deformation functor $D e f(X)$.

There are three cases when it is known that $\operatorname{Def}(X)$ is pro-represented by an analytic space $\operatorname{Def}(X)$.
\begin{itemize}
\item[(1)] If $(P \in X)$ is the germ of an isolated singularity [Gra72] [Ko-Mo92],.
\item[(2)] If $X$ is a compact complex space [Gra74] [Ko-Mo92]
\item[(3)] If there is a proper birational morphism $f: X \longrightarrow Y$, where $Y$ is the germ of an isolated singularity and $R^{1} f_{*} \mathcal{O}_{X}=0$ [Wa76] [Ko-Mo92].
\end{itemize}
In general it is not known whether $D e f^{q G}(X)$ is pro-representable in the above cases. However, if $X$ is normal, $\operatorname{dim} X=2$ and its singularities of index bigger than 1 are all of class $T$ [KoBa88], then $\operatorname{Def}^{q G}(X)$ is pro-represented by a closed subspace $\operatorname{Def}^{q G}(X)$ of $\operatorname{Def}(X)$. In fact, $\operatorname{Def}^{q G}(X)=\pi^{-1}\left(\prod_{P} \operatorname{Def}^{q G}(P \in X)\right)$,
where $\pi$ is the natural map
$$\operatorname{Def}(X) \longrightarrow \prod_{P} \operatorname{Def}(P \in X)$$
$P \in X$ is a singular point of index bigger than 1 and $\operatorname{Def}^{q G}(P \in X)$ is the $q G$ -Gorenstein component of $\operatorname{Def}(P \in X)$ which is known to exist [KoBa88].

The purpose of this paper is to describe the tangent space of the functor $\operatorname{Def}^{q G}(X)$ when $X$ has singularities of class $q G$ [Definition 2.10] and to obtain criteria for the existence of $\mathbb{Q}$-Gorenstein smoothings of $X$. The problem of the pro-representability of $D e f^{q G}(X)$ will not be touched here.

Definition 2.3. The functor of $\underline{\operatorname{Def}}^{q G}(X)$ is the functor
$$\underline{\operatorname{Def}}^{q G}(X): \operatorname{Art}(\mathbb{C}) \longrightarrow \operatorname{Sh}(X)$$
defined as follows. For any finite local $\mathbb{C}$-algebra $A, \underline{\operatorname{De}} f^{q G}(X)(A)$ is the sheaf defined by $\underline{\operatorname{De}}{ }^{q G}(X)(A)(U)=D e f^{q G}(U)(A)$, for any affine open subset $U$ of $X$.

Note that $\operatorname{Def}^{q G}(X)(A)$ is the sheaf associated to the presheaf $F$ defined by $F(V)=\operatorname{Def}^{q G}(V)(A)$ for any open set $V$.

Let $k$ be a field and $F: \operatorname{Art}(k) \longrightarrow \mathcal{C}$ be any functor from the category of finite local $k$-algebras to a category $\mathcal{C}$. Then $F\left(k[t] /\left(t^{2}\right)\right)$ is called the tangent space of $F$ [Sch68].

Definition 2.4. We denote by $\mathbb{T}_{q G}^{1}(X), T_{q G}^{1}(X)$ the tangent spaces of the functors $D e f^{q G}(X)$ and $\underline{\operatorname{De}} f^{q G}(X)$, respectively. $\mathbb{T}_{q G}^{1}(X)$ is a finite dimensional vector space over $\mathbb{C}$ and $T_{q G}^{1}(X)$ is a sheaf of $\mathcal{O}_{X}$-modules defined as follows. For any affine open subset $U \subset X, T_{q G}^{1}(X)(U)$ is the $\mathcal{O}_{X}(U)$-module of isomorphism classes of first order $\mathbb{Q}$-Gorenstein deformations of $U$. If $U$ is Gorenstein, then $T_{q G}^{1}(X)(U)=$ $T^{1}(U)$, the space of first order deformations of $U$.

Standard results from deformation theory show that there is an exact sequence
$$0 \longrightarrow H^{1}\left(T_{X}\right) \longrightarrow \mathbb{T}_{q G}^{1}(X) \longrightarrow H^{0}\left(T_{q G}^{1}(X)\right) \longrightarrow H^{2}\left(T_{X}\right)$$
and therefore in order to describe the first order $\mathbb{Q}$-Gorenstein deformations of $X$, and in particular the existence of smoothings, one needs to study the sheaf $T_{q G}^{1}(X)$ and the obstruction space $H^{2}\left(T_{X}\right)$. The purpose of this paper is to describe $T_{q G}^{1}(X)$.
Definition 2.5. The functor of local $\mathbb{Q}$-Gorenstein deformations is the functor $\operatorname{De} f_{\text {loc }}^{q G}(X): \operatorname{Art}(\mathbb{C}) \longrightarrow$ Sets defined by
$$\operatorname{De} f_{l o c}^{q G}(X)(A)=H^{0}\left(\underline{\operatorname{Def}}^{q G}(X)(A)\right)$$

From the definition of the above functors it is clear that there exists a natural transformation $\operatorname{Def}^{q G}(X) \longrightarrow \operatorname{Def}_{\text {loc }}^{q G}(X)$. If $X$ satisfies any of the conditions (1), (2) or (3), above, then both functors are pro-represented by $\operatorname{Def}^{q G}(X)$ and $\operatorname{Def}_{\text {loc }}^{q G}(X) . \operatorname{Def}_{\text {loc }}^{q G}(X)$ parametrizes collections of local deformations and its tangent space is $H^{0}\left(T_{q G}^{1}(X)\right)$.

In this paper we are interested to know when local deformations exist globally. In order to do this we will study $\operatorname{Def}_{\text {loc }}^{q G}(X)$, and in particular its tangent space $H^{0}\left(T_{q G}^{1}(X)\right)$, and we will find cases when the natural morphism $\phi: \operatorname{Def}^{q G}(X) \longrightarrow$ $D e f_{\text {loc }}^{q G}(X)$ is smooth.

Definition 2.6. A surface singularity $(P \in X)$ is called a normal crossing point (resp. pinch point) if it is analytically isomorphic to $(x y=0) \subset \mathbb{C}^{3}$ (resp. $\left(x^{2}-\right.$ $\left.y^{2} z=0\right) \subset \mathbb{C}^{3}$ ).

Definition 2.7. Let $(P \in X)$ be the germ of a nonnormal surface singularity. A map $f: Y \longrightarrow X$ is called a semi-resolution of $X$ if the following conditions are satisfied:
\begin{itemize}
\item[(1)] $f$ is proper
\item[(2)] $Y$ is semismooth
\item[(3)] If $D_{Y}$ is the double curve of $Y$, then no component of $D_{Y}$ is mapped to a point by $f$
\item[(4)] There is a finite set $S \subset X$ such that $f: f^{-1}(X-S) \longrightarrow X-S$ is an isomorphism.
\end{itemize}

Definition 2.8. Let $P \in X$ be a $\mathbb{Q}$-Gorenstein surface singularity such that $X-P$ is semismooth. Let $f: Y \longrightarrow X$ be a good semi-resolution of $X$. We can write $\omega_{Y}^{n}=f^{*} \omega_{X}^{[n]} \otimes \mathcal{O}_{Y}\left(\sum a_{i} E_{i}\right)$, where $E_{i}$ are $f$-exceptional. Then $(P \in X)$ is called
\begin{itemize}
\item[(1)] semi-log-terminal(slt) if $a_{i}>-1$, for all $i$,
\item[(2)] semi-log-canonical(slc) if $a_{i} \geq-1$, for all $i$,
\end{itemize}

Definition 2.9 ( [Ba83]). Let $X$ be a Gorenstein surface singularity which has a minimal semi-resolution $f: Y \longrightarrow X . X$ is called a degenerate cusp if $X$ is not normal and the exceptional divisor is a cycle of smooth rational curves or a rational nodal curve.

It is known [KoBa88] that a Gorenstein surface singularity $P \in X$ is semi-log-canonical, iff $X$ is either simple elliptic, a cusp, a degenerate cusp or semi-canonical. Moreover, from the classification of slt singularities [KoBa88] it follows that the only slt singularities that admit $\mathbb{Q}$-Gorenstein smoothings are analytically isomorphic to $(x y=0) / \mathbb{Z}_{n}(a,-a, 1)$, with $(a, n)=1$, and their $\mathbb{Q}$-Gorenstein deformations are given by $\left(x y+t f\left(t, z^{n}\right)=0\right) / \mathbb{Z}_{n}(a,-a, 1,0)$. If a semi-log-canonical surface germ $X$ has a terminal $\mathbb{Q}$-Gorenstein smoothing, then the degenerate cusps of $X$ must have embedding dimension at most 4 . This motivates the following.

Definition 2.10. A nonnormal surface singularity $P \in X$ is called a singularity of class $q G$, if it is analytically isomorphic to one of the following
\begin{itemize}
\item[(1)] Normal crossing point: $(x y=0) \subset \mathbb{C}^{3}$
\item[(2)] Pinch point: $\left(x^{2}-y^{2} z=0\right) \subset \mathbb{C}^{3}$
\item[(3)] Degenerate cusp of embedding dimension at most 4
\item[(4)] Semi-log-terminal $(s l t):(x y=0) / \mathbb{Z}_{n}(a,-a, 1),(a, n)=1$.
\end{itemize}

Let $(P \in X)$ be a degenerate cusp and $f: Y \longrightarrow X$ the minimal semi-resolution. Let $\Gamma$ be the reduced exceptional locus. The next lemma is a classification of degenerate cusps of embedding dimension at most 4.

Lemma 2.11 (Karras [Ka77], Shepherd-Barron [Ba83], Stevens [Ste98]). Let $P \in$ $X$ be a degenerate cusp and let $f: Y \longrightarrow X$ be the minimal semi-resolution. Let $\Gamma=f^{-1}(P)_{\text {red }}$. Then
$$\operatorname{mult}_{P}(X)=\max \left\{2,-\Gamma^{2}\right\}$$
\begin{itemize}
\item[(2)]
$$\operatorname{embdim}_{P}(X)=\max \left\{3,-\Gamma^{2}\right\}$$
\item[(3)] If $\Gamma^{2}=-1$, then in local analytic coordinates
$$(P \in X) \cong\left(x^{2}=y^{3}+y^{2} z^{2}\right) \subset \mathbb{C}^{3}$$
\item[(4)] If $\Gamma^{2}=-2$ then in suitable local analytic coordinates
$$(P \in X) \cong\left(x^{2}+z^{2}\left(z^{n+1}-y^{2}\right)=0\right) \subset \mathbb{C}^{3}$$
with $2 \leq n \leq \infty$. In the case that $n=\infty$ we set $z^{n}=0$. If $n<\infty$, then the singular locus of $X$ is a smooth irreducible curve. If $n=\infty$, then the singular locus of $X$ is a reducible curve with exactly two smooth irreducible components. We will call such a singularity a degenerate cusp of type $T_{n}^{2}$.
\item[(5)] If $\Gamma^{2}=-3$ then in local analytic coordinates
$$(P \in X) \cong\left(x^{p+2}+y^{q+2}-x y z=0\right) \subset \mathbb{C}^{3}$$
where $1 \leq p, q \leq \infty$ and if $u$ is any of $x, y, z$, we set $u^{\infty}=0$. Moreover, the singular locus of $X$ has exactly $1+k$ smooth irreducible components, where $k$ is the number of exponents that are $\infty$. We will call such a singularity a degenerate cusp of type $T_{p, q}^{3}$.
\item[(6)] If $\Gamma^{2}=-4$ then in local analytic coordinates
$$(P \in X) \cong\left(x y-z^{p}-t^{q}=0, z t-x^{r}=0\right) \subset \mathbb{C}^{4}$$
where $2 \leq p, q, r \leq \infty$ and if $u$ is any of $x, y, z, t$, we set $u^{\infty}=0$. Moreover, the singular locus of $X$ has exactly $1+k$ smooth irreducible components, where $k$ is the number of exponents that are $\infty$. We will call such a singularity a degenerate cusp of type $T_{p, q, r}^{4}$.
\end{itemize}

In particular we see that any degenerate cusp of embedding dimension at most 4 is a complete intersection and in fact a degenerate cusp is a complete intersection if and only if it has embedding dimension at most 4 [Ste98]. Hence they all have smoothings and in fact $T_{q G}^{1}(P \in X)=T^{1}(P \in X)$.

Let $P \in H$ be a degenerate cusp of embedding dimension 4 with reducible singular locus $\Delta$ ( this is the case when at least one of $p, q, r$ is infinity), and let $C$ be a component of $\Delta$. There are many isomorphic ways that one can choose local coordinates to describe the equations $C \subset H$. For example, let $P \in H$ be of type $T_{p, \infty, \infty}^{4}$ and $C$ the curve $x=y=z=0$. This is isomorphic to the curve $z=t=x=0$ in a degenerate cusp of type $T_{\infty, \infty, p}^{4}$. In order to get a description of $T_{q G}^{1}(H)$ we will have to make a choice of local coordinates. This is mostly due to the reason that we want to describe the invariants that appear in 3.1 and correspond to degenerate cusps with reducible singular locus, as limiting cases of the ones that appear in the case of degenerate cusps with irreducible singular locus. The choices that we make in the following corollary are purely for technical reasons.

From Lemma 2.11 it follows that
Corollary 2.12. Let $P \in H$ be a degenerate cusp of embedding dimension 4 and with reducible singular locus $\Delta$. Let $C$ be a component of $\Delta$. Then in suitable local analytic coordinates
\begin{itemize}
\item[(1)] $C=(x=z=t=0)$ and $H=\left(x y-z^{p}-t^{q}=z t=0\right) \subset \mathbb{C}^{4}$, with $p, q<\infty$. In this case we will call the germ $C \subset H$ of type $T_{p, q, \infty}^{4}$.
\end{itemize}
\begin{itemize}
\item[(2)] $C=(x=z=t=0)$ and $H=\left(x y-z^{p}=z t-x^{r}=0\right) \subset \mathbb{C}^{4}$, with $p, r<\infty$. In this case we will call the germ $C \subset H$ of type $T_{p, \infty, r}^{4}$.
\item[(3)] $C=(x=y=z=0)$ and $H=\left(x y-z^{p}=z t=0\right) \subset \mathbb{C}^{4}$, with $p<\infty$. In this case we will call the germ $C \subset H$ of type $T_{p, \infty, \infty}^{4}$.
\item[(4)] $C=(x=y=z=0)$ and $H=\left(x y=z t-x^{r}=0\right) \subset \mathbb{C}^{4}$, with $r<\infty$. In this case we will call the germ $C \subset H$ of type $T_{\infty, \infty, p}^{4}$.
\item[(5)] $C=(x=y=z=0)$ and $H=(x y=z t=0) \subset \mathbb{C}^{4}$. In this case we will call the germ $C \subset H$ of type $T_{\infty, \infty, \infty}^{4}$.
\end{itemize}

Definition 2.13. Let $(P \in X)$ be a surface cyclic quotient singularity of type $1 / n(1, a)$. Let $U$ be the minimal resolution of $H, E_{1}, \ldots, E_{m}$ the exceptional divisors and
$${ }_{\circ}^{E_{1}}-{ }_{\circ}^{E_{2}}-\cdots-{ }_{\circ}^{E_{m}}$$
be the fundamental cycle. Let $C$ be a smooth curve in $X$ going through the singularity. Then $C$ will be called of type $F C_{k}$ if the birational transform $C^{\prime}$ of $C$ in $U$ intersects $E_{k}$.

\section*{3. Local to Global}

The next Theorem describes the tangent space of $\underline{\operatorname{Def}}^{q G}(H)$ and $D e f_{\text {loc }}^{q G}(H)$.
Theorem 3.1. Let $\Delta \subset H$ be the germ of a surface along a reduced proper curve. Assume that every irreducible component of $\Delta$ is smooth and that locally along $\Delta$ the surface H has singularities of class $q G$. Let $\pi: \tilde{H} \longrightarrow H$ be the normalization of $H$. Let $C$ be an irreducible component of $\Delta$ and $\tilde{C}$ the divisorial part of $\pi^{-1}(C)$. Let $p$ be the number of pinch points and $c_{i}$ the number of degenerate cusps with $\Gamma^{2}=-i, 1 \leq i \leq 4$ of $H$ on $C$. Let $U_{3}, U_{4}$ be the sets of points $P$ of $H$ that lie on $C$ such that $P \in H$ is a degenerate cusp with $\Gamma^{2}=-3$ and -4 respectively. Then
\begin{itemize}
\item[(1)] The support of $T_{q G}^{1}(H)$ is 1-dimensional. Its divisorial part is $\Delta$ and it has an embedded point over any pinch point or degenerate cusp of type other than $T_{\infty, \infty}^{3}$ and $T_{\infty, \infty, \infty}^{4}$. Moreover, let $C$ be any component of $\Delta$. Then,
$$T_{q G}^{1}(H) \otimes \mathcal{O}_{C}=L_{C} \oplus\left(\oplus_{i} \mathbb{C}_{P_{i}}\right)$$
where $L_{C}$ is a line bundle on $C$ and $\mathbb{C}_{P_{i}}$ is a 1-dimensional torsion sheaf supported at a degenerate cusp of embedding dimension 4 that lies on $C$.
\item[(2)]
$$\operatorname{deg} L_{C}=\tilde{C}^{2}+p+2 c_{1}+2 c_{2}+\sum_{P \in U_{3}} \alpha_{3}(P)+\sum_{Q \in U_{4}} \alpha_{4}(Q)$$
where
$$\alpha_{3}(P)=1+\frac{p+q}{p q+p+q}$$
if $P \in U_{3}$ and $P \in C \subset H$ is of type $T_{p, q}^{3}$, and
$$\alpha_{4}(Q)=\frac{r(p+q)-4}{r p q-p-q}$$
if $Q \in U_{4}$ and $P \in C \subset H$ is of type $T_{p, q, r}^{4}$. If any of $p, q, r$ is infinity, then we understand $\alpha_{3}(P)$ and $\alpha_{4}(Q)$ to mean the corresponding limits at infinity.
\end{itemize}

The proof of Theorem 3.1 is given in section 4.
Remark: From the equations defining a degenerate cusp, we see that a singularity $P \in H$ of type $T_{p, q}^{3}$ can be considered as of type $T_{p+2, q+2,1}^{4}$. Then the contribution to the degree of $L_{C}$ in 3.2 above is $\alpha_{3}(P)$. One may expect that this should be the same as $\alpha_{4}(P)$. However, $\alpha_{3}(P)=\alpha_{4}(P)+1$. The reason that there is an extra 1 is that we are assuming that $r \geq 2$ and in this case 3.1 shows that $L_{C}$ has a 1-dimensional torsion at $P$ that accounts for the extra 1.

Proposition 3.2. Let $\Delta \subset H$ be a surface germ as in Theorem 3.1, and $C_{i}$, $i=1, \ldots, k$ the irreducible components of $\Delta$. Let $L_{C_{i}} \in \operatorname{Pic}\left(C_{i}\right)$ the locally free part of $T_{q G}^{1}(H) \otimes \mathcal{O}_{C_{i}}$. Assume that $H^{2}\left(T_{H}\right)=0$. Then
\begin{itemize}
\item[(1)] The natural map of functors
$$\phi: D e f^{q G}(H) \longrightarrow D e f_{l o c}^{q G}(H)$$
is smooth.
\item[(2)] Assume that $C_{i} \cong \mathbb{P}^{1}, \forall i$. Then a one-parameter $\mathbb{Q}$-Gorenstein terminal smoothing $X$ of $H$ exists if and only if $d_{i}=\operatorname{deg}\left(L_{C_{i}}\right) \geq 0 . \forall i$. Moreover, in this case $X$ can be chosen so that it has isolated cyclic quotient singularities of type $1 / n(a,-a, 1)$ and ordinary double points $x y-z t=0$.
\end{itemize}

Remark: In general it is rather difficult to calculate $H^{2}\left(T_{H}\right)$. However if $H$ is a modification of an isolated surface singularity $0 \in S$, i.e., there is a birational morphism $f: \Delta \subset H \longrightarrow S \ni 0$, then by the formal functions theorem it follows that $H^{2}\left(T_{H}\right)=0$. Moreover, if $R^{1} f_{*} \mathcal{O}_{H}=0$ (for example if the singularity $0 \in S$ is rational), then $\Delta$ has rational components and hence the assumptions of Proposition 3.2 are satisfied.

Proof. The map $\phi$ is a smooth map of functors iff
$$\operatorname{De} f^{q G}(H)(B) \longrightarrow D e f^{q G}(H)(A) \times_{D e f_{l o c}^{q G}(H)(A)} D e f_{l o c}^{q G}(H)(B)$$
is surjective for any small extension of finite local $\mathbb{C}$-algebras [Li-Sch67]
$$0 \longrightarrow N \longrightarrow B \longrightarrow A \longrightarrow 0$$
In fact it is sufficient to consider only the case when $N=A / m_{A}=\mathbb{C}$.
In general, let $X$ be a scheme and $\mathcal{F}$ a coherent sheaf on it. Then the space $\operatorname{Ex}(X, \mathcal{F})$ of infinitesimal extensions of $X$ by $\mathcal{F}$ fits in the following exact sequence
$$0 \longrightarrow H^{1}\left(\underline{\operatorname{Hom}}\left(\Omega_{X}, \mathcal{F}\right)\right) \longrightarrow E x(X, \mathcal{F}) \longrightarrow H^{0}\left(T^{1}(X, \mathcal{F})\right) \longrightarrow H^{2}\left(\underline{\operatorname{Hom}}\left(\Omega_{X}, \mathcal{F}\right)\right)$$
In our case, it follows from the above sequence that the obstruction to lift a deformation $H_{B}$ of $H$ over $B$ to a deformation $H_{A}$ over $A$, is in $H^{2}\left(\underline{\operatorname{Hom}}\left(\Omega_{H_{A} / A}, \mathcal{O}_{H}\right)\right)=$ $H^{2}\left(\underline{\operatorname{Hom}}\left(\Omega_{H_{A} / A} \otimes \mathcal{O}_{H}, \mathcal{O}_{H}\right)\right)=H^{2}\left(\underline{\operatorname{Hom}}\left(\Omega_{H}, \mathcal{O}_{H}\right)\right)=0$. Hence $\phi$ is smooth.

Now assume that every irreducible component $C_{i}$ of $\Delta$ is a smooth rational curve and let $d_{i}=\operatorname{deg}\left(L_{C_{i}}\right)$. If there is an $i$ such that $d_{i}<0$, then every section $s \in H^{0}\left(T_{q G}^{1}(H)\right)$ vanishes along $C_{i}$ and hence every deformation of $H$ remains singular, and in fact not normal. Suppose that $d_{i} \geq 0, \forall i$. Since every component of $\Delta$ is rational, it is possible to find a section $s \in H^{0}\left(T_{q G}^{1}(H)\right)$ such that it vanishes at $d_{i}$ points with order 1, and in fact we may choose these points to be normal crossing points. We will now show that locally the deformations of $H$ are unobstructed. This is clear for all index 1 points since they are complete intersections. It remains to consider slt points. So let $P \in H$ be an slt point.

Then in suitable analytic coordinates this is isomorphic to $(x y=0) / \mathbb{Z}_{m}(a,-a, 1)$. Let $B \longrightarrow A$ be a surjection of local Artin $\mathbb{C}$-algebras. Let $X_{A}$ be a $\mathbb{Q}$-Gorenstein deformation of $H$ over $A$. Let $p: \tilde{H} \longrightarrow H$ be the index 1 cover of $H$. Then $X_{A}=\tilde{X_{A}} / \mathbb{Z}_{m}$, where $\tilde{X_{A}}$ is a deformation of $\tilde{H}$ [KoBa88] over $A$. Now since $\tilde{H}$ is complete intersection, $\tilde{X}_{A}$ lifts to a deformation $\tilde{X_{B}}$ of $\tilde{H}$ over $B$ and hence $X_{B}=\tilde{X_{B}} / \mathbb{Z}_{m}$ is a deformation of $H$ over $B$. Therefore locally all $\mathbb{Q}$-Gorenstein deformations of $H$ are unobstructed. The obstruction to lift local deformations to global is in $H^{2}\left(T_{H}\right)$ which is zero by our assumptions. Hence if $d_{i} \geq 0, H$ is smoothable to a 3-fold $X$ with isolated cyclic quotient singularities and ordinary double points. \(\square\)

Putting together Theorem 3.1 and Proposition 3.2 we get the following.
Corollary 3.3. Let $\Delta \subset H$ be the germ of a surface along a proper curve $\Delta$ as in Theorem 3.1. In addition assume that $H^{1}\left(\mathcal{O}_{\Delta}\right)=0, H^{2}\left(T_{H}\right)=0$ and
$$\tilde{C}^{2}+p+2 c_{1}+2 c_{2}+\sum_{P \in U_{3}} \alpha_{3}(P)+\sum_{Q \in U_{4}} \alpha_{4}(Q) \geq 0$$
for every irreducible component $C$ of $\Delta$. Then there exists a one-parameter $\mathbb{Q}$ -Gorenstein smoothing $X$ of $H$ whose singularities are isolated cyclic quotient singularities of type $1 / n(a,-a, 1)$, or ordinary double points $(x y-z t=0) \subset \mathbb{C}^{4}$.

The following corollary shows that under certain conditions, it is possible to construct three dimensional terminal extremal neighborhoods $Y \longrightarrow X$ such that $H \in\left|\mathcal{O}_{Y}\right|$

Corollary 3.4. Let $g: \Delta \subset H \longrightarrow S \ni 0$ be a modification of an isolated surface singularity $0 \in S$. Assume that $H$ has singularities of class $q G$ along $\Delta$ and that $R^{1} f_{*} \mathcal{O}_{H}=0$. Then a one parameter smoothing of $g, f: X \longrightarrow Y$, with $X$ terminal, exists, if and only if
$$\tilde{C}^{2}+p+2 c_{1}+2 c_{2}+\sum_{P \in U_{3}} \alpha_{3}(P)+\sum_{Q \in U_{4}} \alpha_{4}(Q) \geq 0$$
for every irreducible component $C$ of $\Delta$. In particular, a terminal extremal neighborhood $f: \Delta \subset X \xrightarrow{f} Y \ni P$ exists such that $H \in\left|\mathcal{O}_{X}\right|$, if and only if the above inequality holds and $K_{H} \cdot C<0$, for every irreducible component of $\Delta$.

Proof. Since $R^{1} f_{*} \mathcal{O}_{H}=0$ and the fibers of $f$ are at most 1-dimensional, it follows that $\Delta$ is a rational cycle of curves and $H^{2}\left(T_{H}\right)=0$. Hence by Corollary 3.3 there exists a terminal smoothing $X$ of $H$. Then by [Wa76], $g$ extends to $X$, and hence there exists a 3-fold contraction $g: X \longrightarrow Y$, as claimed. If it happens that $K_{H} \cdot C<0$, then $K_{X} \cdot C=K_{H} \cdot C<0$, and hence $Y$ is terminal as well and the contraction is an extremal neighborhood. \(\square\)

Example 3.5. In this example we will construct a stable surface $Z$ such that locally around each singularity it has $\mathbb{Q}$-Gorenstein smoothings but it does not have any global $\mathbb{Q}$-Gorenstein smoothings. Such a surface will be in the boundary of the moduli space of stable surfaces.

Let $\sum_{i=1}^{7} E_{i} \subset U$ be the germ of a smooth surface around a chain of rational curves whose dual graph is
![](https://cdn.mathpix.com/cropped/3a943e92-46c2-468a-b7d5-2fca918ccfb3-10.jpg?height=175&width=251&top_left_y=517&top_left_x=937)
where minus the selfintersection of a curve is denoted over it. Contracting all curves except the -6 and -1, we get a birational morphism $\Delta \subset \tilde{H} \xrightarrow{f} S \ni 0$, where $\Delta=C_{1}+C_{2}, C_{i}$ are the birational transforms of the -6 and -1 curves, and $0 \in S$ is a quotient surface singularity whose dual graph is
$$\mathrm{o}^{-2}-\mathrm{o}^{-2}-\mathrm{o}^{-3}-\mathrm{o}^{-2}$$
and hence it is of type 1/11(1,8). The singular locus of $\tilde{H}$ consists of exactly four points $A_{1}, B_{1} \in C_{1}$ and $A_{2}, B_{2} \in C_{2}$ such that $A_{1} \in \tilde{H} \cong 1 / 3(1,1), A_{2} \in \tilde{H} \cong$ $1 / 3(1,2)$, and both $B_{1}, B_{2}$ are of type 1/2(1, 1). Now $C_{1}+C_{2}$ has an involution fixing the intersection $C_{1} \cap C_{2}$ and interchanging $A_{1}, A_{2}$ and $B_{1}, B_{2}$. Identifying now $C_{1}$ and $C_{2}$ with the involution we get a surface germ $C \subset H, C \cong \mathbb{P}^{1}$, whose normalization is $\tilde{H} . H$ has semi-log-canonical singularities and in fact it has two semi-log-terminal singularities of types $(x y=0) / \mathbb{Z}_{2}(1,1,1),(x y=0) / \mathbb{Z}_{3}(1,-1,1)$, one degenerate cusp of embedding dimension 3 and multiplicity 2, and is normal crossing elsewhere along $C$. Note that all the singularities of $H$ have $\mathbb{Q}$-Gorenstein smoothings. Let : $\tilde{H} \longrightarrow H$ be the identification map. Straightforward calculations show that $K_{H} \cdot C=1 / 6>0$ and that $\tilde{C}^{2}=\left(C_{1}+C_{2}\right)^{2}=-3$. Hence from Theorem 3.1 it follows that $\operatorname{deg} T_{q G}^{1}(H) \otimes \mathcal{O}_{C}=-3+2=-1$, and hence $T_{q G}^{1}(H) \otimes$ $\mathcal{O}_{C}=\mathcal{O}_{\mathbb{P}^{1}}(-1)$. Hence $\mathbb{T}_{q G}^{1}(H)=H^{1}\left(T_{H}\right)$, and therefore every $\mathbb{Q}$-Gorenstein deformation of $H$ is locally trivial. In particular, $H$ is not globally smoothable, even though it is locally smoothable. Notice also that in this case $H^{2}\left(T_{H}\right)=0$ which in the isolated singularities case is the obstruction space to lift local deformations to global ones.

Next I claim that $H$ can be compactified to a stable surface $Z$. To do so we will first construct a terminal stable surface $W$ whith a singularity of type 1/11(1,8) and then we will blow it up to get $Z$. So let $W \subset \mathbb{P}(1,1,11,8)$ be a general weighted hypersurface of degree 56, for example $x_{0} x_{2}^{5}+x_{3}^{7}+x_{0}^{56}+x_{1}^{56}=0$. This has exactly one singular point $P$ at [0, 0, 1, 0] which is of type 1/11(1, 8). Moreover $K_{W}=\mathcal{O}_{W}(56-1-1-11-8)=\mathcal{O}_{W}(35)$ and hence ample.

Now $U \longrightarrow S$ is just a sequence of blow ups and hence $U \longrightarrow S$ can be extended to a morphism $X \longrightarrow W$. Contract all curves again except the -6 and -1 to get a compactification $\tilde{Z}$ of $\tilde{H}$, and identifying $C_{1}, C_{2}$ we get the desired compactification $Z$ of $H$. I now claim that $Z$ is stable. Indeed, this is true if and only if $\omega_{Z}^{[n]}$ is ample, for some $n$. This is true if and only if $\pi^{*} \omega_{Z}^{[n]}$ is ample, and by subadjunction, this is ample if and only $K_{\tilde{Z}}+C_{1}+C_{2}$ is ample. Moreover, let $g: \tilde{Z} \longrightarrow W$ be the contraction map. Then $K_{\tilde{Z}}=g^{*} K_{W}+a_{1} C_{1}+a_{2} C_{2}$, with $a_{1}, a_{2}>-1$, since the singularity of $W$ is log terminal. Hence
$$K_{\tilde{Z}}+C_{1}+C_{2}=g^{*} K_{W}+\left(a_{1}+1\right) C_{1}+\left(a_{2}+1\right) C_{2}$$

Therefore $a_{i}+1>0, i=1,2$, and hence if $\Gamma \subset \tilde{Z}$ is any curve different than $C_{1}$, $C_{2}$, then
$$K_{\tilde{Z}} \cdot \Gamma=K_{W} \cdot f(\Gamma)+\left(a_{1}+1\right) C_{1} \cdot \Gamma+\left(a_{2}+1\right) C_{2} \cdot \Gamma>0$$
Moreover, a straightforward calculation shows that $K_{\tilde{Z}} \cdot C_{i}=1 / 6>0$ and it now follows that $Z$ is stable.

Example 3.6. Let $U$ be the germ of a smooth surface around a chain of smooth rational curves with the following dual graph
$$\stackrel{-2}{\circ}^{-2}-\stackrel{-2}{\circ}^{-} \stackrel{-3}{\circ}^{-\stackrel{-2}{\bullet}_{2}}-\stackrel{-3}{\circ}^{-\stackrel{-1}{\circ}_{C_{1}}}-\stackrel{-2}{\circ}^{-\stackrel{-5}{\circ}^{-2}}$$
Contracting all curves except $C_{1}$ and $C_{2}$ we get a map $\tilde{H} \xrightarrow{f} S$, such that $0 \in S$ is an $A_{5}$ singularity. Moreover, $\tilde{H}$ has exactly three singular points $P_{1} \in C_{1}, P_{2} \in C_{2}$ and $Q \in C_{1} \cap C_{2}$, analytically isomorphic to 1/9(1, 5), 1/9(1, -5) and 1/3(1, 1), respectively. We can now identify $C_{1}$ and $C_{2}$ to a smooth rational curve $C$ and get a nonnormal surface $C \subset H . H$ has an slt singular point analytically isomorphic to $(x y=0) / \mathbb{Z}_{9}(5,-5,1)$, a degenerate cusp of type $T_{1,1}^{3}$, and is normal crossing everywhere else. Moreover, $\tilde{H}$ is the normalization of $H$ and there is a morphism $g: H \longrightarrow S$. An easy calculation now on $\tilde{H}$ shows that $\left(C_{1}+C_{2}\right)^{2}=-2 / 3$. Now from Theorem 3.1 it follows that $d=\operatorname{deg} L=\left(C_{1}+C_{2}\right)^{2}+\alpha_{3}(Q)=-2 / 3+(1+$ $1) /(1+1+1)=0$. Hence $L \cong \mathcal{O}_{C}$, and hence there exists a one parameter terminal smoothing $Y$ of $H$ extending the local ones. More precisely, $Y$ has exactly 1 singular point and it is of type 1/7(5, -5, 1). The morphism $g$ extends to $Y$ [Wa76], and hence we get an extremal neighborhood $f: C \subset Y \longrightarrow X \ni 0$, such that $H \in\left|\mathcal{O}_{Y}\right|$.

The next lemma describes the local deformations of singularities of class $q G$.
Lemma 3.7. Let $(P \in H)$ be the germ of a singularity as in Theorem 3.1. Then $(P \in H)$ has a smoothing $(P \in X)$ such that
\begin{itemize}
\item[(1)] $(P \in X)$ is smooth if $(P \in H)$ is not a degenerate cusp of embedding dimension 4 or an slt point.
\end{itemize}
$$(P \in X) \cong(x y-z t=0) \subset \mathbb{C}^{4}$$
if $(P \in H)$ is a degenerate cusp of embedding dimension 4.
$$(P \in X) \cong \mathbb{C}^{3} / \mathbb{Z}_{n}(a,-a, 1)$$
if $(P \in H)$ is an slt point.
Proof. The first part is obvious. Now suppose that $(P \in H)$ is a degenerate cusp of embedding dimension 4. Then in suitable local analytic coordinates it is given by equations $x y-z^{p}-t^{q}=0, z t-x^{r}=0$. Then take $X$ to be $x y+z t-z^{p}-t^{q}-x^{r}=0$ which is analytically equivalent to $x y-z t=0$.

Let $(P \in H)$ be an slt point. Then $(P \in H) \cong(x y=0) / \mathbb{Z}_{n}(a,-a, 1)$. A $\mathbb{Q}$-Gorenstein smoothing is $(x y+t=0) / \mathbb{Z}_{n}(a,-a, 1,0) \cong \mathbb{C}^{3} / \mathbb{Z}_{n}(a,-a, 1)$. \(\square\)

The next lemma describes the support and the torsion part of $T_{q G}^{1}(H)$.
Lemma 3.8. Let $\Delta \subset H$ be the germ of a surface along a proper curve as in Theorem 3.1. Then the support of $T_{q G}^{1}(H)$ is 1-dimensional. Its divisorial part is
$\Delta$ and it has an embedded point over any pinch point or degenerate cusp of type other than $T_{\infty, \infty}^{3}$ and $T_{\infty, \infty, \infty}^{4}$. Moreover, let $C$ be any component of $\Delta$. Then
$$T_{q G}^{1}(H) \otimes \mathcal{O}_{C}=L_{C} \oplus\left(\oplus_{i} \mathbb{C}_{P_{i}}\right)$$
where $L_{C}$ is a line bundle on $C$ and $\mathbb{C}_{P_{i}}$ is a 1-dimensional torsion sheaf supported at a degenerate cusp $P_{i} \in H$ of embedding dimension 4 that lies on $C$.

Proof. Locally, at an index 1 point, $H=(f=0) \subset \mathbb{C}^{3}$ and
$$T^{1}(H)=T_{q G}^{1}(H)=\frac{\mathbb{C}[x, y, z]}{(f, J(f))},$$
where $J(f)$ is the Jacobian of $f$. Then at any generic point of $\Delta, H$ is normal crossing, i.e., $H=(x y=0)$ and therefore $T_{q G}^{1}(H)=\mathbb{C}[x, y, z] /(x, y)=\mathbb{C}[z]$ and hence free of rank 1.

Let $P \in H$ be a pinch point. Then
$$T_{q G}^{1}(P \in H)=\frac{\mathbb{C}[x, y, z]}{\left(x, y^{2}, y z\right)}$$
and hence its support is defined by the ideal $\left(x, y^{2}, y z\right)=\left(x, y^{2}, z\right) \cap(x, y)$. Therefore its divisorial part is $\Delta$ and it also has an embedded point over $P$. Moreover, $\Delta$ is irreducible at a neighborhood of $P$.

Let $P \in H$ be a degenerate cusp of type $T_{n}^{2}$, with $n \leq \infty$. Then
$$T_{q G}^{1}(P \in H)=\frac{\mathbb{C}[x, y, z]}{\left(x, y z^{2},(n+3) z^{n+2}-2 z y^{2}\right)}$$
and hence its support is defined by the ideal $I=\left(x, y z^{2},(n+3) z^{n+2}-2 z y^{2}\right)$ (if $n=\infty$ we set as usual $z^{n}=0$ ). Therefore its divisorial part is $\Delta$ and since $r\left(I: z^{2}\right)=(x, y, z)$, it also has an embedded point over $P$ ( AM69 ).

Let $P \in H$ be a degenerate cusp of type $T_{p, q}^{3}$, with $p, q, \leq \infty$. Then
$$T_{q G}^{1}(P \in H)=\frac{\mathbb{C}[x, y, z]}{\left(p x^{p-1}-y z, q y^{q-1}-x z, x y\right)}$$
with the usual conventions about the cases that at least one of $p, q$, is infinity. Hence its support is defined by the ideal $I=\left(p x^{p-1}-y z, q y^{q-1}-x z, x y\right)$ and therefore its divisorial part is $\Delta$. If at least one of $p, q$ is not infinity, say $p$, then $r(I: x)=(x, y, z)$ and hence the support of $T_{q G}^{1}(H)$ has an embedded point over $P$. If $p=q=\infty$, then $I=(x y, x z, y z)$ and hence in this case there are no embedded points.

Let $C$ be any component of $\Delta$. Then in all of the above cases it is clear that $T_{q G}^{1}(P \in H) \otimes \mathcal{O}_{\Delta}$ is free of rank 1.

Now let $P \in H$ be an slt point. Let $P \in X$ be a $q G$-smoothing and let $\pi: \hat{X} \longrightarrow$ $X$ be the index 1 cover of $X$. Then $\pi^{-1}(H)=\hat{H} \longrightarrow H$ is the index 1 cover of $H$ [KoBa88] and hence $\hat{H}=(x y=0) \subset \mathbb{C}^{3}$. Therefore $q G$-smoothings of $H$ are quotients of $q G$-smoothings of $\hat{H}$ and therefore, $T_{q G}^{1}(P \in H)=T^{1}(\hat{H})^{\mathbb{Z}_{n}}$ and hence $T_{q G}^{1}(P \in H)$ is torsion free and has support $\Delta$.

Finally, let $P \in H$ be a degenerate cusp of type $T_{p, q, r}^{4}$, with $p, q, r \leq \infty$. By Lemma 2.11, in suitable analytic coordinates, $P \in H$ is given by $(f(x, y, z, t)=$ $g(x, y, z, t)=0) \subset \mathbb{C}^{4}$. We will now describe $T_{q G}^{1}(P \in H)$. It is known that
$T_{q G}^{1}(P \in H)=T^{1}(P \in H)=\operatorname{Ext}_{H}^{1}\left(\Omega_{H}, \mathcal{O}_{H}\right)$ [Li-Sch67]. Moreover, there is an exact sequence
$$0 \longrightarrow T_{H} \longrightarrow T_{\mathbb{C}^{4}} \otimes \mathcal{O}_{H} \longrightarrow N_{H / \mathbb{C}^{4}} \longrightarrow E x t_{H}^{1}\left(\Omega_{H}, \mathcal{O}_{H}\right) \longrightarrow 0$$
Writing down explicitely the isomorphisms ${ }_{\mathbb{C}^{4}} \otimes \mathcal{O}_{H} \cong \mathcal{O}_{H}^{\oplus 4}$ and $N_{H / \mathbb{C}^{4}} \cong \mathcal{O}_{H}^{\oplus 2}$, it follows that $T_{q G}^{1}(P \in H)$ fits in the exact sequence
$$\mathcal{O}_{H}^{\oplus 4} \xrightarrow{\phi} \mathcal{O}_{H}^{\oplus 2} \longrightarrow T_{q G}^{1}(P \in H) \longrightarrow 0$$
where $\phi(1,0,0,0)=(\partial f / \partial x, \partial g / \partial x), \phi(0,1,0,0)=(\partial f / \partial y, \partial g / \partial y), \phi(0,0,1,0)=$ $(\partial f / \partial z, \partial g / \partial z)$ and $\phi(0,0,0,1)=(\partial f / \partial t, \partial g / \partial t)$. Therefore we find that
$$T_{q G}^{1}(P \in H)=\frac{\mathbb{C}[x, y, z, t] \oplus \mathbb{C}[x, y, z, t]}{M}$$
where $M$ is the $\mathbb{C}[x, y, z, t]$-submodule of $\mathbb{C}[x, y, z, t] \oplus \mathbb{C}[x, y, z, t]$ that is generated by $(f, 0),(0, f),(g, 0),(0, g),(\partial f / \partial x, \partial g / \partial x),(\partial f / \partial y, \partial g / \partial y),(\partial f / \partial z, \partial g / \partial z)$ and $(\partial f / \partial t, \partial g / \partial t)$. Now a straightforward calculation shows that the divisorial part of the support of $T_{q G}^{1}(P \in H)$ is $\Delta$ and that if at least one of $p, q, r$ is not infinity, then it has an embedded point over $P$. If $p=q=r=\infty$, then the support of $T_{q G}^{1}(P \in H)$ is defined by the ideal ( $x y, x z, x t, y z, y t, z t$ ) and it has no embedded point. Moreover, a straightforward calculation shows that if $C$ is any irreducible component of $\Delta$, then $T_{q G}^{1}(P \in H) \otimes \mathcal{O}_{C}=\mathbb{C}_{P} \oplus \mathcal{O}_{C}$ where $\mathbb{C}_{P}$ is a one-dimensional torsion sheaf concentrated at $P$ as claimed. \(\square\)

The next lemma shows how to calculate $T_{q G}^{1}(H)$ from a suitable embedding.
Lemma 3.9. Let $\Delta \subset H$ be the germ of a surface along a proper curve as in the statement of Theorem 3.1. Let $H \subset X$ be an embedding such that $X$ is a $\mathbb{Q}$ -Gorenstein 3-fold, $H$ is Cartier in $X$, and for all $P \in \Delta \subset H,(P \in X)$ is a general $\mathbb{Q}$-Gorenstein smoothing of $(P \in H)$. Let $C$ be an irreducible component of $\Delta$ and $L_{C}$ be the free part of $T_{q G}^{1}(H) \otimes \mathcal{O}_{C}$. Let $\phi$ be the natural map
$$\mathcal{N}_{H / X} \longrightarrow \underline{\operatorname{Ext}}_{H}^{1}\left(\Omega_{H}, \mathcal{O}_{H}\right)$$
Then
$$L_{C}=\operatorname{Im}\left[\mathcal{N}_{H / X} \otimes \mathcal{O}_{C} \longrightarrow \underline{\operatorname{Ext}}_{H}^{1}\left(\Omega_{H}, \mathcal{O}_{H}\right) \otimes \mathcal{O}_{C}\right]$$
and therefore
$$\operatorname{deg}\left(L_{C} \otimes \mathcal{O}_{C}\right)=C \cdot H$$
Proof. Dualizing the exact sequence
$$0 \longrightarrow I_{H, X} / I_{H, X}^{2} \longrightarrow \Omega_{X} \otimes \mathcal{O}_{H} \longrightarrow \Omega_{H} \longrightarrow 0$$
we get
$$\cdots \longrightarrow \mathcal{N}_{H / X} \xrightarrow{\phi} \underline{\operatorname{Ext}}_{H}^{1}\left(\Omega_{H}, \mathcal{O}_{H}\right)=T^{1}(H) \longrightarrow \underline{\operatorname{Ext}}_{H}^{1}\left(\Omega_{X} \otimes \mathcal{O}_{H}, \mathcal{O}_{H}\right) \longrightarrow 0$$
The claim of the lemma then can be checked locally. $\underline{\operatorname{Ext}}_{H}^{1}\left(\Omega_{X} \otimes \mathcal{O}_{H}, \mathcal{O}_{H}\right)$ is torsion and it is supported over the slt points of $H$ and the degenerate cusps of embedding dimension 4. $X$ is smooth away from such points and Lemma 3.9, 1 is true around all points except possibly slt points and degenerate cusps of embeding dimension 4. We will now check what happens around such points.

Let $P \in X$ be a singular point such that $P \in H$ is an slt point. Let $P \in U$ be a small neighborhood of $X$ around $P$ and $V=U \cap H$. Then (1) restricts to
$$\mathcal{O}_{V} \xrightarrow{\phi} \operatorname{Ext}_{V}^{1}\left(\Omega_{V}, \mathcal{O}_{V}\right)$$
Let $\pi: \hat{U} \longrightarrow U$ be the index 1 cover of $U$. Then it is well known that $\hat{V}=$ $\pi^{-1}(V) \longrightarrow V$ is the index 1 cover of $V$. Therefore this implies that
$$T_{q G}^{1}(V)=T^{1}(\hat{V})^{\mathbb{Z}_{n}}$$
Then (1) follows from the diagram
![](https://cdn.mathpix.com/cropped/3a943e92-46c2-468a-b7d5-2fca918ccfb3-14.jpg?height=216&width=542&top_left_y=823&top_left_x=791)
and from the fact that $\hat{\phi}$ is surjective. Hence there is a surjection
$$N_{V / U} \longrightarrow T_{q G}^{1}(V)$$
It now remains to check what happens around a singular point $P \in H$ that is a degenerate cusp of embedding dimension 4. According to Lemma 3.8, $T_{q G}^{1}(H) \otimes$ $\mathcal{O}_{C}=L_{C} \oplus \mathbb{C}_{P}$, where $\mathbb{C}_{P}$ is a one-dimensional torsion sheaf concentrated at $P$. The statement of the lemma will follow if we show that in a neighborhood of $P$, $\operatorname{Ext}_{H}^{1}\left(\Omega_{X} \otimes \mathcal{O}_{H}, \mathcal{O}_{H}\right) \cong \mathbb{C}_{P}$.

Locally around $P, X=(x y-z w=0) \subset \mathbb{C}^{4}$. Hence there is an exact sequence
$$0 \longrightarrow I_{X, \mathbb{C}^{5}} / I_{X, \mathbb{C}^{4}}^{2} \longrightarrow \Omega_{\mathbb{C}^{5}} \otimes \mathcal{O}_{X} \longrightarrow \Omega_{X} \longrightarrow 0$$
Considering that $I_{X, \mathbb{C}^{5}} / I_{X, \mathbb{C}^{5}}^{2} \cong \mathcal{O}_{X}$, this gives that
$$\operatorname{Hom}_{H}\left(\Omega_{\mathbb{C}^{5}} \otimes_{\mathcal{O}_{X}} \mathcal{O}_{H}, \mathcal{O}_{H}\right) \longrightarrow \operatorname{Hom}_{H}\left(\mathcal{O}_{H}, \mathcal{O}_{H}\right) \longrightarrow \operatorname{Ext}_{H}^{1}\left(\Omega_{X} \otimes \mathcal{O}_{H}, \mathcal{O}_{H}\right) \longrightarrow 0$$
Now writing explicitely all the maps involved in the above sequence and the isomorphisms $\operatorname{Hom}_{H}\left(\Omega_{\mathbb{C}^{5}} \otimes_{\mathcal{O}_{X}} \mathcal{O}_{H}, \mathcal{O}_{H}\right) \cong \mathcal{O}_{H}^{\oplus 4}, \operatorname{Hom}_{H}\left(\mathcal{O}_{H}, \mathcal{O}_{H}\right) \cong \mathcal{O}_{H}$, it follows that the last exact sequence is equivalent to
$$\mathcal{O}_{H}^{\oplus 4} \xrightarrow{\phi} \mathcal{O}_{H} \longrightarrow \operatorname{Ext}_{H}^{1}\left(\Omega_{X} \otimes \mathcal{O}_{H}, \mathcal{O}_{H}\right) \longrightarrow 0$$
where the map $\phi$ is given by sending the standard basis elements (1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0) and (0, 0, 0, 1) to $x, y, z, t$, respectively. Hence it is now clear that $\operatorname{Ext}_{H}^{1}\left(\Omega_{X} \otimes \mathcal{O}_{H}, \mathcal{O}_{H}\right) \cong \mathbb{C}_{P}$. This concludes the proof of the lemma. \(\square\)

The next lemma was communicated to me by János Kollár and it shows that it is always possible to find a 3-fold $X$ with the properties of Lemma 3.9.

Lemma 3.10. Let $\Delta \subset H$ be the germ of a surface along a proper curve $\Delta$. Assume that $H$ is smooth away from $\Delta$ and that generically along every component of $\Delta$ it has at worst singularities of type $(x y=0) \subset \mathbb{C}^{3}$. Assume that for each $c \in \Delta$ we specify a neighborhood $U_{c} \subset X$ and a closed embedding $U_{c} \subset V_{c}$. Assume that $V_{c}$ is smooth away from $c$ and singular for finitely many only $c$. Then there is a global embedding $\Delta \subset H \subset X$ that patches the local embedings.

Proof. Let $W=H-\{$ a few transverse cuts $\}$. Then $W$ is Stein and it embedds in a $\mathbb{C}^{n}$, for some $n$. We want to get an embedding $W \subset V_{W}$ into something three dimensional that has at most finitely many singularities along $\Delta$. Let $f: Y \longrightarrow \mathbb{C}^{n}$ be the blow up of $\mathbb{C}^{n}$ along $W$. Let $E$ be the $f$-exceptional set. Then by the assumptions on the singularities of $H$, a local calculation shows that away from finitely many singularities of $H$ that correspond to non normal crossing points, $E=$ $E_{1}+E_{2}$, where $E_{1}$ and $E_{2}$ are both smooth intersecting transversally. Moreover, $E_{1}+E_{2}$ is Cartier and the singular locus of $Y$ has codimension 3 in $Y$. More precisely, locally the singularities of $Y$ are of the type $(x y-z t=0) \subset \mathbb{C}^{n+1}$. Moreover, $\operatorname{dim} f^{-1}(c)=n-3$, for all $c \in \Delta$. Then by Bertini's theorem, the general $V^{\prime}=Z_{1} \cap Z_{2} \cap \cdots \cap Z_{n-3}$, with $Z_{i} \in\left|-E_{1}-E_{2}\right|$, has finitely many singularities and $V^{\prime} \longrightarrow V_{W}=f_{*}\left(V^{\prime}\right)$ is birational. $V_{W}$ has the required properties.

Therefore, by removing a few more transverse cuts, $W=H-\{$ a few transverse cuts\} has a smooth embedding into a three dimensional space $V_{W}$. Let $(H-W) \cap \Delta=$ $\left\{c_{1}, \ldots, c_{k}\right\}$. Let $U_{c_{i}}$ be a Stein neighborhood of $c_{i} \in H$ and let $U_{c_{i}} \subset V_{c_{i}}$ be an embedding such that $V_{c_{i}}$ is smooth away from $c_{i}$. We want to glue $V_{W}$ and $V_{c_{i}}$ into a 3-fold $V$. This will follow from the following.
Claim: Let $c \in \Delta \subset U$ be the germ of a surface singularity along a curve $\Delta$. Assume that $U$ is singular along $\Delta$. Let $R \subset U$ be a small ring around $c \in U$. Let $R \subset X_{R}^{1}$, $R \subset X_{R}^{2}$ be two embeddings, where $X_{R}^{1}$ and $X_{R}^{2}$ are smooth, which we may also assume that they are Stein. Then, after shrinking $R$ if necessary, $X_{R}^{1} \cong X_{R}^{2}$.

The map $R \subset X_{R}^{2}$ extends to a map $X_{R}^{1} \longrightarrow X_{R}^{2}$. Since $R$ is singular along $C \Delta$, then for all $c \in \Delta, T_{c}(R)=T_{c}\left(X_{R}^{1}\right)=T_{c}\left(X_{R}^{2}\right)$, and hence by shrinking $R$ if necessary, it follows from the inverse function theorem that $X_{R}^{1} \cong X_{R}^{2}$.

Now gluing $V_{W}$ and $V_{c_{i}}, i=1, \ldots, k$, we obtain the required embedding. \(\square\)

An immediate consequence of Lemmas 3.10 and 3.6 is the following.
Corollary 3.11. Let $\Delta \subset H$ be a surface germ as in Theorem 3.1. Then there exists an embedding $H \subset X$ such that $X$ is a terminal 3-fold and $H$ is Cartier in $X$. Moreover, let $P \in X$ be a singular point of $X$. Then either $P \in H$ is a degenerate cusp of embedding dimension 4 and $(P \in X) \cong(x y-z t=0) \subset \mathbb{C}^{4}$ or $P \in H$ is an slt point, and $(P \in X) \cong 1 / n(a,-a, 1)$.

We now want to calculate the degree of $L$, the free part of $T_{q G}^{1}(H)$ from the normalization of $H$. The next proposition is the key to do so.

Proposition 3.12. Let $\Delta \subset X$ be the germ of a 3-fold along a curve $\Delta$ (proper or not). Suppose that $X$ has isolated singularities along $\Delta$ and that locally in a neighborhood of any $P \in \Delta$, the general member of $\left|-K_{X}\right|$ that contains $\Delta$ has
DuVal singularities. Then there exists a divisorial contraction $E \subset Y \xrightarrow{f} X \supset \Delta$, such that $Y$ has canonical singularities and
\begin{itemize}
\item[(1)] $Y-E \cong X-\Delta$
\item[(2)] $-K_{Y}$ is $f$-ample
\item[(3)] Distinct irreducible components of $E$ are contracted onto distinct irreducible components of $\Delta$
\item[(4)] The singularities of $Y$ lie on finitely many fibers over $X$
\end{itemize}
Moreover, over the smooth locus of $X, f$ is the blow up of $X$ along $\Delta$.

In general it is hard to describe the singularities of $E$ and $Y$, but for the cases of interest in this paper we have the following.
\begin{itemize}
\item[(1)] Let $P$ be a point in $X$ such that $(P \in X) \cong(x y-z t=0) \subset \mathbb{C}^{4}$ and $\Delta$ is smooth at $P$. Then $f^{-1}(P)$ is the union of two smooth rational curves $F_{1}$, $F_{2}$ intersecting transversally at a point $Q . Y$ is smooth along $f^{-1}(P)-Q$ and $(Q \in Y) \cong \mathbb{C}^{3} / \mathbb{Z}_{2}(1,1,1)$. $E$ is smooth away from $Q$ and $(Q \in E) \cong$ $\left(x y-z^{2}=0\right) \subset \mathbb{C}^{3}$. Moreover $K_{Y} \cdot F_{i}=-1 / 2, i=1,2$.
\item[(2)] Let $P$ a point in $X$ such that $\Delta$ is smooth at $P$ and $(P \in \Delta \subset X) \cong$ $(x=y=0) \subset \mathbb{C}^{3} / \mathbb{Z}_{n}(a,-a, 1)$. Then $\left(f^{-1}(P)\right)_{\text {red }}=F=\mathbb{P}^{1}$. $E^{\text {sing }} \cap$ $F=\left\{Q_{1}, Q_{2}\right\}$ such that $\left(Q_{1} \in E\right) \cong \mathbb{C}^{2} / \mathbb{Z}_{n}(1,2 a)$ and $\left(Q_{2} \in E\right) \cong$ $\mathbb{C}^{2} / \mathbb{Z}_{n}(1,-2 a)$. Moreover, $\left(Q_{1} \in Y\right) \cong \mathbb{C}^{3} / \mathbb{Z}_{n}(a,-2 a, 1),\left(Q_{2} \in Y\right) \cong$ $\mathbb{C}^{3} / \mathbb{Z}_{n}(-a, 2 a, 1), K_{Y} \cdot F=-1 / n$, if $n$ is odd, and $K_{Y} \cdot F=-2 / n$, if $n$ is even.
\end{itemize}
Note that in the above two cases, there is always a DuVal $S \in\left|-K_{X}\right|$ that contains $\Delta$.

Proof. If a divisorial contraction $f: E \subset Y \longrightarrow X \supset \Delta$ that satisfies the condititions of the proposition exists, then it is unique and in fact
$$Y \cong \operatorname{Proj} \bigoplus_{d} i_{*}\left(I_{\Delta \cap U, U}^{d}\right)$$
where $U$ is the smooth part of $X$. Therefore its existence is equivalent to the finite generation of the sheaf of algebras $\oplus_{d} i_{*}\left(I_{\Delta \cap U, U}^{d}\right)$ [Tzi03]. This can be checked locally and hence the existence of local contractions imply the existence of a global one. We only need to check locally around the singular points of $X$. Let $P \in X$ be a neighborhood of a singular point and let $S \in\left|-K_{X}\right|$ a DuVal surface that contains $\Delta$. Then by inversion of adjunction, $(X, S)$ is $k l t$ and in fact canonical since $K_{X}+S$ is Cartier. Let $g: Z \longrightarrow X$ be the blow up of $X$ along $\Delta$. Let $E$ be the $g$-exceptional divisor that is over $\Delta$. Then generically along $\Delta, K_{Z}=g^{*} K_{X}+E$ and $g^{*} S=S^{\prime}+E$. Hence $K_{Z}+S^{\prime}=g^{*}\left(K_{X}+S\right)$ and therefore $E$ is crepant for the pair $(X, S)$. Hence there exists an extraction of $E, f: E \subset: Y \longrightarrow X \supset \Delta$, such that $f: Y-E \longrightarrow X-\Delta$ is an isomorphism [Ko93, Theorem 17.10]. Moreover, $K_{Y}+f_{*}^{-1} S=f^{*}\left(K_{X}+S\right)$ and hence $\left(Y, f_{*}^{-1} S\right)$ is canonical and therefore $Y$ has canonical singularities too.

Let $P \in X$ be a singular point such that $(P \in X) \cong(x=y=0) \subset \mathbb{C}^{3} / \mathbb{Z}_{n}(a,-a, 1)$, where $x, y, z$ are the coordinates for $\mathbb{C}^{3}$. Hence $\Delta=\pi(L)$, where $L$ is the line $x=y=0$. Then the divisorial contraction can be constructed from the following diagram.
![](https://cdn.mathpix.com/cropped/3a943e92-46c2-468a-b7d5-2fca918ccfb3-16.jpg?height=197&width=428&top_left_y=2034&top_left_x=848)
where $\hat{Y}$ is the blow up of $\mathbb{C}^{3}$ along the $z$-axis, $x=y=0$. A straightforward calculation now of the lifting of the action of $\mathbb{Z}_{n}$ on $\hat{Y}$ shows that the singular locus of $E$ is two points $Q_{1}$ and $Q_{2}$, and $\left(Q_{1} \in E\right) \cong 1 / n(1,2 a)$, $\left(Q_{2} \in E\right) \cong 1 / n(1,-2 a)$. Moreover, $\left(Q_{1} \in Y\right) \cong 1 / n(a,-2 a, 1)$ and $\left(Q_{2} \in Y\right) \cong 1 / n(-a, 2 a, 1)$. If $n$ is odd
then the singular locus of $Y$ consists of the points $Q_{1}$ and $Q_{2}$. If on the other hand $n$ is even, then $Y$ may be singular along $f^{-1}(P)$.

It remains to find $K_{Y} \cdot F$, where $F=f^{-1}(P)_{\text {red }}$. Let $\hat{F}=\hat{f}^{-1}(0)$. Then $F=\hat{F} / \mathbb{Z}_{n}$. Let $u, u$ be homogeneous coordinates for $\mathbb{P}^{1}=\hat{F}$. Let $\zeta$ be a primitive $n$-th root of unity. Then $\mathbb{Z}_{n}$ acts on $\hat{F}$ by $\zeta \cdot[u, v]=\left[\zeta^{a} u, \zeta^{-a} v\right]$. Hence $\hat{F} \longrightarrow F$ is $n$-to-one if $n$ is odd and $n / 2$-to-one of $n$ is even. Now $\hat{\pi}$ is étale in codimension 1 and hence $K_{\hat{Y}}=\pi^{*} K_{Y}$. Therefore
$$-1=K_{\hat{Y}} \cdot \hat{F}=\pi^{*} K_{Y} \cdot \hat{F}=K_{Y} \cdot \pi_{*}(\hat{F})$$
and therefore $K_{Y} \cdot F=-1 / n$, if $n$ is odd, and $K_{Y} \cdot F=-2 / n$, if $n$ is even, as claimed.

Now let $P$ be a singular point of $X$ such that $(P \in X) \cong(x y-z t=0) \subset \mathbb{C}^{4}$. Then the divisorial contraction can be constructed by the following diagram [Tzi03].
![](https://cdn.mathpix.com/cropped/3a943e92-46c2-468a-b7d5-2fca918ccfb3-17.jpg?height=292&width=314&top_left_y=1002&top_left_x=905)
where $W$ is the blow up of $X$ along $\Delta$. A straightforward calculation of the blow up shows that there are two $g$-exceptional divisors. A surface $E$ ruled over $\Delta$ and a $F \cong \mathbb{P}^{2}$ over $P$. The singular locus of $W$ consists of two points $R_{1}$ and $R_{2}$ on $E \cap F$. Then $Z$ is the blow up of $E, F_{Z}=h_{*}^{-1} F \cong F=\mathbb{P}^{2}$, and there are two disjoint $h$-exceptional curves. Moreover, $\phi$ is the contraction of $F_{Z}$. Calculations as in [Tzi03] show that $N_{F_{Z} / Z}=\mathcal{O}_{\mathbb{P}^{2}}(-2)$ and hence it contracts to a 1/2(1,1,1) singularity. All other statements about the singularities of $E$ can also be checked by local calculations. \(\square\)

\section*{4. Proof of Theorem 3.1}

With assumptions and notation as in Theorem 3.1, let $C$ be an irreducible component of $\Delta$, and $H \subset X$ an embedding as in Corollary 3.10. Let $f: E \subset Y \longrightarrow X \supset$ $C$ be the divisorial contraction as in Proposition 3.12, $H^{\prime}=f_{*}^{-1} H$ and $D^{\prime}=E \cdot H^{\prime}$. Let $\pi: \tilde{H} \longrightarrow H$ be the normalization of $H$ and $\nu: \hat{H} \longrightarrow H^{\prime}$ the normalization of $H^{\prime}$. Then there is a commutative diagram
![](https://cdn.mathpix.com/cropped/3a943e92-46c2-468a-b7d5-2fca918ccfb3-17.jpg?height=310&width=321&top_left_y=2012&top_left_x=901)

The next lemma describes the birational transform $H^{\prime}$ of $H$ in $Y$ and the minimal resolution of the normalization $\tilde{H}$ of $H$.

Lemma 4.1. (1) Let $P \in H$ be a nc or a pinch point. Then in a neighborhood of $P \in H, H^{\prime}$ is smooth and it is the normalization $\tilde{H}$ of $H$. Moreover, $D^{\prime}=\tilde{C}$ is smooth, $P$ is not a ramification point of $\pi$, if $P$ is nc, and it is a ramification point if it is a pinch point.
\begin{itemize}
\item[(2)] Let $P \in H$ be a degenerate cusp with $\Gamma^{2}=-1$. Then $H^{\prime}=\tilde{H}$ is smooth. $D^{\prime}=\tilde{C}$ is the union of two smooth curves intersecting transversally, and hence globally $\tilde{C}$ is either two transversal curves or it is nodal. $P$ is a ramification of $\pi$.
\item[(3)] Let $P \in H$ be a degenerate cusp with $\Gamma^{2}=-2$. Suppose it is of type $T_{n}^{2}$ with $n<\infty$. Then $H^{\prime}=\tilde{H}$. If it is of type $T_{\infty}^{2}$, then $H^{\prime}$ is normal crossing and its normalization is $\tilde{H}$, which is smooth. In both cases $D^{\prime}$ is the union of two smooth curves intersecting transversally at a point $Q$, $\left(Q \in H^{\prime}\right) \cong\left(x y-z^{n}=0\right)$ in the $T_{n}^{2}$ case and nc in the the $T_{\infty}^{2}$. Moreover, in both cases $\tilde{C}$ is either two transversal curves or nodal and $P$ is a ramification of $\pi$.
\item[(4)] Let $P \in H$ be a degenerate cusp with $\Gamma^{2}=-3$. Then $D^{\prime}=E \cdot H^{\prime}=C^{\prime}+F$, where $F \cong \mathbb{P}^{1}$ is $f$-exceptional and $C^{\prime}$ is smooth and 2-1 over $C$. Moreover, $C^{\prime} \cap F=\{P, Q\}$, with $P \neq Q$ and,
\begin{itemize}
\item[(a)] Suppose $P \in H$ is of type $T_{p, q}^{3}$, for $1 \leq p, q<\infty$. Then $H^{\prime}$ is normal and is the blow up of $H$ along $C . P \in H^{\prime}$ is an $A_{p-1}$ DuVal singularity and $Q \in H^{\prime}$ is an $A_{q-1}$ Du Val singularity. Moreover, $F^{2}=$ $-1-1 / p-1 / q, C^{\prime}$ is of type $F C_{1}$ in both $\left(P \in H^{\prime}\right)$ and $\left(Q \in H^{\prime}\right)$.
\item[(b)] Suppose $P \in H$ is of type $T_{p, \infty}^{3}$. Then $P \in H^{\prime}$ is an $A_{p-1}$ singularity and $Q \in H^{\prime}$ is nc. Let $\hat{F}$ be the divisorial part of $\nu^{-1}(F)$. Then $\hat{F}^{2}=-1-1 / p$.
\item[(c)] Suppose $P \in H$ is of type $T_{\infty, \infty}^{3}$. Then $H^{\prime}$ is nc and hence its normalization $\hat{H}$ is smooth. Moreover, $P, Q \in H$ are nc points and $\hat{F}^{2}=-1$.
\end{itemize}
\item[(5)] Let $P \in H$ be a degenerate cusp with $\Gamma^{2}=-4$. Then it is of type $T_{p, q, r}^{4}$, with $2 \leq p, q, r \leq \infty$. Let $U$ be the minimal resolution of $\tilde{H}$.
\begin{itemize}
\item[(a)] Suppose $p, q, r<\infty$. Then $H^{\prime}$ is normal. Then the extended dual graph of $C^{\prime} \subset \tilde{H}$ is
\begin{itemize}
\item[(i)] If $r \geq 3, D$, it is
\end{itemize}
\end{itemize}
\end{itemize}
$$\stackrel{\bullet}{C}^{\prime}-\stackrel{-2}{E_{p-2}^{\circ}}-\cdots-\underset{E_{1}}{\stackrel{-2}{\circ}}-\stackrel{-3}{O_{F_{1}}^{\circ}}-\stackrel{-2}{\circ}-\cdots-\underset{D_{1}}{\stackrel{-2}{\circ}}-\stackrel{-3}{D_{r-3}^{\infty}}-\stackrel{-2}{F_{2}}-\cdots-\underset{B_{1}}{\stackrel{-2}{\circ}}-\stackrel{\bullet}{B}_{B_{q-2}}^{\circ}$$
\begin{itemize}
\begin{itemize}
\item[(ii)] If $r=2$, it is
\end{itemize}
\end{itemize}
$$\stackrel{\bullet}{C}^{\prime}-\stackrel{-2}{\underset{E_{p-2}}{\circ}}-\cdots-\stackrel{-2}{\underset{E_{1}}{\circ}-\stackrel{-4}{\circ}}-\stackrel{-2}{\stackrel{\circ}{O}_{B_{1}}^{-2}-\cdots} \underset{B_{q-2}^{-}}{\stackrel{-2}{\circ}-\stackrel{\bullet}{C}^{\prime}}$$
In both cases $H^{\prime}$ is obtained from $U$ by contracting all curves except $E_{1}$ and $B_{1}$. If $p$ or $q$ is 2 then we set $E_{i}=\emptyset$ or $B_{i}=\emptyset$. In particular, if $p=q=2$ then $H^{\prime}=\tilde{H}$. $P$ is a ramification point of $\hat{H} \longrightarrow H$, and $\tilde{C}$ is either a union of two smooth curves intersecting transversally, or nodal. Moreover, $D^{\prime}=C^{\prime}+E_{1}^{\prime}+B_{1}^{\prime}$, where $E_{1}^{\prime}$ and $B_{1}^{\prime}$ are the
\begin{itemize}
\item[] birational transforms of $E_{1}$ and $B_{1}$ in $H^{\prime}$ and
$$\begin{aligned}
E_{1}^{\prime 2} & =-1-\frac{1}{p-2}+\frac{2 r-3}{4 r-4} \\
{B_{1}^{\prime}}^{2} & =-1-\frac{1}{q-2}+\frac{2 r-3}{4 r-4}
\end{aligned}$$
\item[(b)] Suppose $p, q<\infty$ and $r=\infty$. Then the singular locus $\Delta$ of $H$ is the transversal union of $C$ and another smooth curve $C_{1}$ and,
\begin{itemize}
\item[(i)] The extended dual graph of $\Delta \subset \tilde{H}$ is
$$\stackrel{\bullet}{C}^{\prime}-\stackrel{-2}{E_{p-2}^{\circ}}-\cdots-{ }_{E_{1}}^{-2}-{ }_{F_{1}}^{-2}-\stackrel{\bullet}{C}_{C_{1}^{\prime}}^{-}-{ }_{F_{2}}^{-2}-{ }_{B_{1}}^{-2}-\cdots-{ }_{B_{q-2}}^{o_{0}^{-2}}-{\stackrel{\bullet}{C^{\prime}}}^{\bullet}$$
\item[(ii)] $\hat{H}$ is obtained from $U$ by contracting all curves except $E_{1}$ and $B_{1}$ and $D^{\prime}=C^{\prime}+E_{1}^{\prime}+B_{1}^{\prime}$, where $E_{1}^{\prime}$ and $B_{1}^{\prime}$ are the birational transforms of $E_{1}$ and $B_{1}$ in $H^{\prime}$. Moreover, let $\hat{E}_{1}$ and $\hat{B_{1}}$ be the birational transforms of $E_{1}$ and $B_{1}$ in $\hat{H}$. Then
$$\begin{aligned}
& {\hat{E_{1}}}^{2}=-\frac{p}{2(p-2)} \\
& {\hat{B_{1}}}^{2}=-\frac{q}{2(q-2)}
\end{aligned}$$
\end{itemize}
\item[(c)] Suppose $p, r<\infty$ and $q=\infty$. Then the singular locus of $H, \Delta$, is the transversal union of two smooth curves $C_{1}$, and $C_{2}$. Then up to an analytic change of coordinates we can assume that $H=\left(x y-z^{p}=\right.$ $\left.z t-x^{r}=0\right) \subset \mathbb{C}^{4}$ and $C=(x=z=t=0)$. Then the extended dual graph of $\Delta \subset \tilde{H}$ is
$$\stackrel{\bullet}{C_{1}^{\prime}}-\stackrel{-2}{B_{p-2}^{\circ}}-\cdots-\stackrel{-2}{\circ}-\stackrel{-3}{B_{1}}-\stackrel{-2}{{ }_{F}^{\circ}}-\cdots-\underset{E_{1}}{\stackrel{-2}{\circ}}-\underset{E_{r-2}^{\prime}}{\bullet}-\stackrel{\bullet}{C}_{1}^{\circ}$$
and the extended dual graph of $\hat{H}$ is
$$\underset{C_{1}^{\prime}}{\bullet}-\underset{B_{p-2}}{\stackrel{-2}{\circ}}-\cdots-\underset{B_{1}}{-2}-\stackrel{-3}{\circ}-\underset{E_{1}}{-2}-\cdots-\underset{E_{r-3}^{-2}}{\stackrel{\circ}{\circ}}-\underset{E_{r-2}^{-3}}{\circ}-\underset{F_{1}}{\stackrel{-1}{\circ}}-\underset{C_{2}^{\prime}}{\bullet}-\underset{C_{1}^{\prime}}{\bullet}$$
Moreover, $\hat{H}$ is obtained from $U$ by contracting all curves except $B_{1}$ and $F_{1}$ and $D^{\prime}=C^{\prime}+E_{1}^{\prime}+F_{1}^{\prime}$, where $E_{1}^{\prime}$ and $F_{1}^{\prime}$ are the birational transforms of $F_{1}$ and $B_{1}$ in $H^{\prime}$. Moreover, let $\hat{F}_{1}$ and $\hat{B_{1}}$ be the birational transforms of $F_{1}$ and $B_{1}$ in $\hat{H}$. Then
$$\begin{gathered}
{\hat{B_{1}}}^{2}=-1-\frac{1}{p-2}+\frac{2 r-3}{4 r-4} \\
{\hat{F_{1}}}^{2}=-1+\frac{2 r-3}{4 r-4}
\end{gathered}$$
\item[(d)] Suppose $p<\infty$ and $q=r=\infty$. Then the singular locus of $H$, $\Delta$, is the transversal union of three smooth curves $C_{1}, C_{2}$ and $C_{3}$. Moreover, the extended dual graph of $\Delta \subset \tilde{H}$ is
$$\stackrel{\bullet}{C_{1}^{\prime}}-\stackrel{-2}{E_{p-2}^{\circ}}-\cdots-{ }_{E_{1}}^{-2}-\stackrel{-2}{F}-\underset{C_{2}^{\prime}}{\bullet}-\underset{C_{3}^{\prime}}{\bullet}-{ }_{C_{1}^{\prime}}^{\bullet}$$
and the extended dual graph of $\hat{H}$ is
\end{itemize}
\begin{itemize}
\begin{itemize}
\begin{itemize}
\item[(i)] If $C$ is $C_{1}$ or $C_{2}$, it is
$$\underset{C_{1}^{\prime}}{\bullet}-\stackrel{-2}{E_{p-2}^{\circ}}-\cdots-\underset{E_{1}}{\stackrel{-2}{\circ}}-\stackrel{-2}{\stackrel{\circ}{F}}-\underset{C_{2}^{\prime}}{\bullet}-\stackrel{-2}{F_{1}}-\stackrel{-1}{\stackrel{\circ}{B}}-\underset{C_{3}^{\prime}}{\bullet}-\underset{C_{1}^{\prime}}{\bullet}$$
In which case $\hat{H}$ is obtained by contracting all curves except $E_{1}$ and $B$ and $D^{\prime}=C^{\prime}+E_{1}^{\prime}+B^{\prime}$, where $E_{1}^{\prime}$ and $B^{\prime}$ are the birational transforms of $E_{1}$ and $B$ in $H^{\prime}$. Moreover, let $\hat{E}_{1}$ and $\hat{B}$ be the birational transforms of $E_{1}$ and $B$ in $\hat{H}$. Then
$$\begin{gathered}
\hat{E}_{1}^{2}=-\frac{p}{2(p-2)} \\
{\hat{B_{1}}}^{2}=-\frac{1}{2}
\end{gathered}$$
\item[(ii)] If $C=C_{3}$, then it is
$$\stackrel{\bullet}{C_{1}^{\prime}}-\stackrel{-1}{\circ}-\underset{B_{1}}{\stackrel{-3}{\circ}}-\underset{E_{p-2}}{\stackrel{-2}{\circ}}-\cdots-\underset{E_{p-3}}{\stackrel{-2}{\circ}}-\stackrel{-3}{\stackrel{\circ}{F}}-\stackrel{-1}{\underset{B_{2}}{\circ}-}-\underset{C_{2}^{\prime}}{\bullet}-\underset{C_{3}^{\prime}}{\bullet}-\underset{C_{1}^{\prime}}{\bullet}$$
and in this case $\hat{H}$ is obtained by contracting all curves except $B_{1}$ and $B_{2}$ and $D^{\prime}=C^{\prime}+B_{1}^{\prime}+B_{2}^{\prime}$, where $B_{1}^{\prime}$ and $B_{2}^{\prime}$ are the birational transforms of $B_{1}$ and $B_{2}$ in $H^{\prime}$. Moreover, let $\hat{B_{1}}$ and $\hat{B_{2}}$ be the birational transforms of $B_{1}$ and $B_{2}$ in $\hat{H}$. Then
$${\hat{B_{1}}}^{2}={\hat{B_{2}}}^{2}=-1+\frac{2 p-3}{4 p-4}$$
\end{itemize}
\item[(e)] Suppose that $p=q=r=\infty$. Then $\tilde{H}$ is smooth. Moreover, $D^{\prime}=$ $E_{1}+E_{2}+C^{\prime}$, where the $E_{i}$ are $f$-exceptional, and if $\hat{E}_{i}$ are the divisorial parts of $\nu^{-1}\left(E_{i}\right)$, then $\hat{E}_{i}^{2}=-1 / 2$.
\end{itemize}
\item[(6)] If $P \in H$ is an slt point, then $H^{\prime}=\tilde{H}, D^{\prime}=\tilde{C}$ and $f^{-1}(P)=\left\{R_{1}, R_{2}\right\}$ where $\left(R_{1} \in \tilde{H}\right) \cong 1 / n(1, a)$ and $\left(R_{2} \in \tilde{H}\right) \cong 1 / n(1,-a)$.
\end{itemize}

Remark 4.2. In the case that any of $p, q, r$ is infinity, then the selfintersection numbers of the exceptional curves that appear in the previous lemma are exactly the corresponding limits to infinity of the selfintersection numbers that were found in the finite case.

Proof. Let $P \in X$ be a point such that $P \in H$ is not a degenerate cusp of embedding dimension 4 or an slt point. Then $X$ is smooth at $P$ and therefore, $Y$ is just the blow up of $X$ along $C$ and hence $H^{\prime}$ is also the blow up of $H$ along $C$. Then an explicit calculation of the blow up using the normal forms for the equations of the singularities that are given in Lemma 2.11, show parts (1)-(4).

Let $P \in H$ be an slt point. Then $(P \in H) \cong \hat{H} / \mathbb{Z}_{n}(a,-a, 1)$, where $\hat{H}=(x y=$ $0) \subset \mathbb{C}^{3}$. Let $\hat{U}$ be the blow up of $\hat{H}$ along $\hat{C}=(x=y=0)$. Then from the proof of Proposition 3.12 and in particular diagram (4), it follows that $\hat{H}=\pi^{-1}(H)$, $H^{\prime}=\hat{U} / \mathbb{Z}_{n}$ and hence it is the normalization of $H, \tilde{H}$. The claim about the singularities of $\tilde{H}$ follows from KoBa88, or by a careful calculation in diagram (4) in Proposition 3.12.