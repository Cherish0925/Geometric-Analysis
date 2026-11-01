---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 1511_04831v1.pdf
converter: mathpix
format: mmd
---

\title{
KODAIRA DIMENSION IN LOW DIMENSIONAL TOPOLOGY
}

\author{
TIAN-JUN LI
}

\begin{abstract}
This is a survey on the various notions of Kodaira dimension in low dimensional topology. The focus is on progress after the 2006 survey [78].
\end{abstract}

\section*{Contents}
1. Introduction ..... 1
2. $\kappa^{t}$ and $\kappa^{s}$ ..... 2
2.1. The topological Kod dim $\kappa^{t}$ for manifolds up to dimension 3 ..... 2
2.2. The symplectic Kod $\operatorname{dim} \kappa^{s}$ for 4 -manifolds ..... 4
2.3. Symplectic manifolds of dimension 6 and higher ..... 6
3. Calculating $\kappa^{s}$ ..... 6
3.1. Additivity and subadditivity ..... 6
3.2. Behavior under Surgeries ..... 7
4. Main problems and progress in each class ..... 8
4.1. Surfaces and symmetry of $\kappa=-\infty$ manifolds ..... 8
4.2. Towards the classification of $\kappa=0$ manifolds ..... 11
4.3. Euler number and decomposition of $\kappa^{s}=1$ manifolds ..... 15
4.4. Geography and exotic geography of $\kappa^{s}=2$ manifolds ..... 16
5. Extensions ..... 17
5.1. Relative Kodaira dim for a symplectic pair ..... 17
5.2. Symplectic manifolds with concave boundary ..... 19
References ..... 19

\section*{1. Introduction}

Roughly speaking, a Kodaira dimension type invariant on a class of $n$-dimensional manifolds is a numerical invariant taking values in the finite set
$$\left\{-\infty, 0,1, \cdots,\left\lfloor\frac{n}{2}\right\rfloor\right\},$$
where $\lfloor x\rfloor$ is the largest integer bounded by $x$.

\footnotetext{
Date: November 17, 2015.
}

The first invariant of this type is due to Kodaira ([64]) for smooth algebraic varieties (naturally extended to complex manifolds): Suppose $(M, J)$ is a complex manifold of real dimension $2 m$. The holomorphic Kodaira dimension $\kappa^{h}(M, J)$ is defined as follows:
$$\kappa^{h}(M, J)= \begin{cases}-\infty & \text { if } P_{l}(M, J)=0 \text { for all } l \geq 1, \\ 0 & \text { if } P_{l}(M, J) \in\{0,1\}, \text { but } \not \equiv 0 \text { for all } l \geq 1, \\ k & \text { if } P_{l}(M, J) \sim c l^{k} ; c>0 .\end{cases}$$
Here $P_{l}(M, J)$ is the $l$-th plurigenus of the complex manifold $(M, J)$ defined by $P_{l}(M, J)=h^{0}\left(\mathcal{K}_{J}^{\otimes l}\right)$, with $\mathcal{K}_{J}$ the canonical bundle of $(M, J)$.

This classical Kodaira dimension $\kappa^{h}$, along with its various extensions, has played an essential role in algebraic geometry, Kähler geometry and complex geometry (cf. [60], [28], [124]).

In the past 20 years, it has been gradually realized that such notions also exist in low dimensional topology. The paper [78] is a survey on the Kodaira dimension $\kappa^{s}$ for symplectic 4-manifolds up to 2005. The current article updates the progress on $\kappa^{s}$ and its extensions, as well as its cousin $\kappa^{t}$ for 3-manifolds.

The construction of the symplectic Kodaira dimension $\kappa^{s}$ is impossible without Taubes' fundamental works. We would like to take this opportunity to express our deep gratitude towards him. We also benefit from discussions with I. Baykur, J. Dorfmeister, J. Fine, S. Friedl, Y. Koichi, G. LaNave, C. Mak, D. Salamon, W. Wu, W. Zhang. We are also grateful to the referee for useful suggestions. This work is supported by NSF.
$$\text { 2. } \kappa^{t} \text { AND } \kappa^{s}$$

Let $M$ be a closed, smooth, oriented manifold. To begin with, we make the following definition for logical compatibility.

Definition 2.1. If $M=\emptyset$, then its Kodaira dimension is defined to be $-\infty$.
2.1. The topological Kod $\boldsymbol{\operatorname { d i m }} \kappa^{t}$ for manifolds up to dimension 3.
2.1.1. $\kappa^{t}$ in dimensions 0, 1 and 2. The only closed connected 0-dimensional manifold is a point, and the only closed connected 1-dimensional manifold is a circle.

Definition 2.2. If $M$ has dimension 0 or 1, then its Kodaira dimension $\kappa^{t}(M)$ is defined to be 0.

The 2 -dimensional Kodaira dimension is defined by the positivity of the Euler class. Suppose $M^{2}$ is a 2 -dimensional closed, connected, oriented manifold with Euler class $e\left(M^{2}\right)$. Write $K=-e\left(M^{2}\right)$ and define
$$\kappa^{t}\left(M^{2}\right)=\left\{\begin{array}{cl}
-\infty & \text { if } K<0, \\
0 & \text { if } K=0, \\
1 & \text { if } K>0 .
\end{array}\right.$$

It is easy to see that for any complex structure $J$ on $M^{2}, K$ is its canonical class, and $\kappa^{h}\left(M^{2}, J\right)=\kappa^{t}\left(M^{2}\right) . \kappa^{t}\left(M^{2}\right)$ can be further interpreted from other viewpoints: symplectic structure ( $K$ is also the symplectic canonical class), the Yamabe invariant, geometric structures etc.
2.1.2. $\kappa^{t}$ in dimension 3. We move on to dimension 3. In this dimension the definition of the Kodaira dimension in [129] by Weiyi Zhang is based on geometric structures in the sense of Thurston.

Divide the 8 Thurston geometries into 3 categories:
$$\begin{array}{ll}
-\infty: & S^{3} \text { and } S^{2} \times \mathbb{R} ; \\
0: & \mathbb{E}^{3}, \text { Nil and Sol; } \\
1: & \mathbb{H}^{2} \times \mathbb{R}, \underline{S L_{2}(\mathbb{R})} \text { and } \mathbb{H}^{3} .
\end{array}$$
Given a closed, connected 3-manifold $M^{3}$, we decompose it first by a prime decomposition and then further consider a toroidal decomposition for each prime summand, such that at the end each piece has a geometric structure either in group (1), (2) or (3) with finite volume.

Definition 2.3. For a closed, connected 3-dimensional manifold $M^{3}$, its Kodaira dimension $\kappa^{t}(M)$ is defined as follows:
\begin{itemize}
\item[(1)] $\kappa^{t}\left(M^{3}\right)=-\infty$ if for any decomposition, each piece has geometry type in category $-\infty$,
\item[(2)] $\kappa^{t}\left(M^{3}\right)=0$ if for any decomposition, we have at least one piece with geometry type in category 0, but no piece has type in category 1,
\item[(3)] $\kappa^{t}\left(M^{3}\right)=1$ if for any decomposition, we have at least one piece in category 1.
\end{itemize}

The following are basic properties and facts established in [129]:
\begin{itemize}
\item[-] $\kappa^{t}$ is additive for any fiber bundle.
\item[-] If there is a nonzero degree map from $M$ to $N$, then $\kappa^{t}(M) \geq \kappa^{t}(N)$.
\item[-] If $\kappa^{t}(M)=-\infty$, then each prime summand of $M$ is either (a) spherical, i.e. it has a Riemannian metric of constant positive sectional curvature; or (b) an $S^{2}$ bundle over $S^{1}$.
\item[-] If $\kappa^{t}(M)=0$, then each prime summand of $M$ is either in (a) or (b), or it is (c) a Seifert fibration with zero orbifold Euler characteristic; or (d) a mapping torus of an Anosov map of the 2-torus or quotient of these by groups of order at most 8.
\end{itemize}

Let $v b_{1}(M)$ be the supremum of $b_{1}(\tilde{M})$ among all finite covers $\tilde{M}$. Due to Agol's remarkable resolution of the virtual Betti number conjecture, $\kappa^{t}$ has the following interpretation in terms of the virtual 1st Betti number $v b_{1}$, at least for irreducible 3-manifolds (private communication with W. Zhang): $\kappa^{t}=-\infty$ when $v b_{1}=0, \kappa^{t}=0$ when $v b_{1}$ is finite and positive, $\kappa^{t}=1$ when $v b_{1}$ is infinite.

Notice that we use $\kappa^{t}$ to denote the Kodaira dimension for smooth manifolds in dimensions 0,1,2,3. Here $t$ stands for topological/smooth, because in these dimensions homeomorphic manifolds are actually diffeomorphic.

For a non-orientable, connected manifold, we define its Kodaira dimension to be that of its (unique) orientable, connected covering. For a possibly disconnected manifold, we define its Kodaira dimension to be the maximum of that of its components.

In summary, the Kodaira dimension is defined for all closed smooth manifolds with dimension less than 4, and is a topological/smooth invariant.

\subsection*{2.2. The symplectic Kod dim $\kappa^{s}$ for 4 -manifolds.}
2.2.1. Definition based on Taubes SW. Let $M$ be a closed, oriented smooth 4-manifold. Let $\mathcal{E}_{M}$ be the set of cohomology classes whose Poincaré dual are represented by smoothly embedded spheres of self-intersection $-1 . M$ is said to be (smoothly) minimal if $\mathcal{E}_{M}$ is the empty set. Equivalently, $M$ is minimal if it is not the connected sum of another manifold with $\overline{\mathbb{C P}^{2}}$.

Suppose $\omega$ is a symplectic form compatible with the orientation. $(M, \omega)$ is said to be (symplectically) minimal if $\mathcal{E}_{\omega}$ is empty, where
$$\mathcal{E}_{\omega}=\left\{E \in \mathcal{E}_{M} \mid E \text { is represented by an embedded } \omega \text {-symplectic sphere }\right\} .$$
We say that $(N, \tau)$ is a minimal model of $(M, \omega)$ if $(N, \tau)$ is minimal and $(M, \omega)$ is a symplectic blow up of $(N, \tau)$. A basic fact proved using Taubes SW theory is: $\mathcal{E}_{\omega}$ is empty if and only if $\mathcal{E}_{M}$ is empty. In other words, $(M, \omega)$ is symplectically minimal if and only if $M$ is smoothly minimal.

For a minimal symplectic 4 -manifold $\left(M^{4}, \omega\right)$ with symplectic canonical class $K_{\omega}$, the Kodaira dimension of $\left(M^{4}, \omega\right)$ is defined in the following way:
$$\kappa^{s}\left(M^{4}, \omega\right)=\left\{\begin{array}{lll}
-\infty & \text { if } K_{\omega} \cdot[\omega]<0 \text { or } & K_{\omega} \cdot K_{\omega}<0, \\
0 & \text { if } K_{\omega} \cdot[\omega]=0 \text { and } & K_{\omega} \cdot K_{\omega}=0, \\
1 & \text { if } K_{\omega} \cdot[\omega]>0 \text { and } & K_{\omega} \cdot K_{\omega}=0, \\
2 & \text { if } K_{\omega} \cdot[\omega]>0 \text { and } & K_{\omega} \cdot K_{\omega}>0 .
\end{array}\right.$$
Here $K_{\omega}$ is defined as the first Chern class of the cotangent bundle for any almost complex structure compatible with $\omega$.
$\kappa^{s}$ is well defined since there does not exist a minimal $(M, \omega)$ with
$$K_{\omega} \cdot[\omega]=0, \quad \text { and } \quad K_{\omega} \cdot K_{\omega}>0 .$$
This again follows from Taubes SW theory. Moreover, $\kappa^{s}$ is independent of $\omega$, so it is an oriented diffeomorphism invariant of $M$. And it follows from [94] (cf. also [107]) that $\kappa^{s}(M)=-\infty$ if and only if $M$ is $\mathbb{C P}^{2}, S^{2} \times S^{2}$ or an $S^{2}$-bundle over a Riemann surface of positive genus.

The Kodaira dimension of a non-minimal manifold is defined to be that of any of its minimal models. $\kappa^{s}(M, \omega)$ is well-defined for any $(M, \omega)$ since minimal models always exist. Moreover, minimal models are almost unique up to diffeomorphisms: If $(M, \omega)$ has non-diffeomorphic minimal models, then these minimal models have $\kappa^{s}=-\infty$. Diffeomorphic minimal models have the same $\kappa^{s}$.

Here are basic properties of $\kappa^{s}$ :
\begin{itemize}
\item[-] $\kappa^{s}$ is an oriented diffeomorphism invariant of $M$ ([77]).
\item[-] $\kappa^{s}=\kappa^{h}$ whenever both are defined ([35]).
\end{itemize}

We remark that it was shown by Friedman and Qin ([52]) that $\kappa^{h}\left(M^{4}, J\right)$ only depends on the oriented diffeomorphism type of $M^{4}$. In light of these properties of $\kappa^{s}$ and $\kappa^{h}$, we ask

Question 2.4. To what extent can $\kappa^{s}$ and $\kappa^{h}$ be extended to $\kappa^{d}$ for smooth 4-manifolds (here $d$ stands for 'differentiable').
2.2.2. Yamabe invariant. Recall that the Yamabe invariant is defined in the following way:
$$Y(M)=\sup _{[g] \in \mathcal{C}} \inf _{g \in[g]} \int_{M} s_{g} d V_{g},$$
where $g$ is a Riemannian metric on $M, s_{g}$ the scalar curvature, [ $g$ ] the conformal class of $g$, and $\mathcal{C}$ the set of conformal classes on $M$.

A basic fact is that $Y(M)>0$ if and only if $M$ admits a metric of positive scalar curvature. Thus $Y(M)$ is non-positive if $M$ does not admit metrics of positive scalar curvature. Furthermore, in this case, another basic fact is that $Y(M)$ is the supremum of the scalar curvatures of all unit volume constant-scalar-curvature metrics on $M$ (such metrics exist due to the resolution of the Yamabe conjecture). It immediately follows that, in dimension two, the sign of $Y\left(M^{2}\right)$ completely determines $\kappa^{t}\left(M^{2}\right)$.

In dimension three, $Y\left(M^{3}\right)$ is also closely related to the geometric structure of $M^{3}$, at least when $M^{3}$ is irreducible. However, the number $Y\left(M^{3}\right)$ does not completely determine $\kappa^{t}\left(M^{3}\right)$ (See [129] and [93]).

When $M^{4}$ admits a Kähler structure, LeBrun ([75]) calculated $Y\left(M^{4}\right)$ and concluded that (1) completely determines $\kappa^{h}$. As $\kappa^{s}=\kappa^{h}$ for a Kähler surface, if $M^{4}$ admits a Kähler structure, then
$$\kappa^{s}\left(M^{4}\right)= \begin{cases}-\infty & \text { if } Y\left(M^{4}\right)>0, \\ 0 & \text { if } Y\left(M^{4}\right)=0 \text { and } 0 \text { is attainable by a metric, } \\ 1 & \text { if } Y\left(M^{4}\right)=0 \text { and } 0 \text { is not attainable, } \\ 2 & \text { if } Y\left(M^{4}\right)<0 .\end{cases}$$
It is worth mentioning that there is connection between Ricci flow and the Yamabe invariant, which is related to the beautiful criterion (2) in the Kähler context. (See eg. [62]). However, in the general symplectic context, (2) does not determine $\kappa^{s}\left(M^{4}\right)$ : All $T^{2}$-bundles over $T^{2}$ have $\kappa^{s}=0$, while most of them do not have any zero scalar curvature metrics. And, while $\kappa^{s}$ is invariant under finite coverings, the sign of the Yamabe invariant is not a covering invariant of 4-manifolds ([74]). But the question of LeBrun still makes sense: if $M^{4}$ admits a symplectic structure and $Y\left(M^{4}\right)<0$, is $\kappa^{s}\left(M^{4}\right)$ equal to 2? (cf. [73], [118], [123]).
2.3. Symplectic manifolds of dimension 6 and higher. In higher dimension, Kodaira dimension is only defined for complex manifolds. Further, it is known that $\kappa^{h}$ is not a diffeomorphism invariant [110]. Thus we can only expect to have a notion of Kodaira dimension for smooth manifolds with some additional structures. For higher dimensional symplectic manifolds, there is a proposal to extend $\kappa^{s}$ in [91]. Another approach via Donaldson' peak sections is investigated in [67].

In the rest of the paper we will focus on symplectic 4-manifolds.

\section*{3. Calculating $\kappa^{s}$}

\subsection*{3.1. Additivity and subadditivity.}
3.1.1. Subadditivity for Lefschetz fibrations. A central problem in birational geometry is the following Iitaka conjecture $C_{n, m}$ for holomorphic fibrations of algebraic varieties: Let $f: X \rightarrow Z$ be an algebraic fibre space where $X$ and $Z$ are smooth projective varieties of dimension $n$ and $m$, respectively, and let $F$ be a general fibre of $f$. Then, $\kappa^{h}(X) \geq \kappa^{h}(F)+\kappa^{h}(Z)$.

It has been verified when $n \leq 6$ (cf. [20] for the status of this conjecture). For symplectic 4-manifolds, Lefschetz fibrations are the analogues of holomorphic fibrations, and it is established in [35] that
$$\kappa^{s}(X) \geq \kappa^{t}(\text { Base })+\kappa^{t}(\text { Fiber }) .$$

This is certainly true when the base is $S^{2}$. When the base genus is at least 1, given a relative minimal $(g, h, n)$ Lefschetz fibration with $h \geq 1$, the Kodaira dimension $\kappa^{l}(g, h, n)$ is introduced in [35]:
$$\kappa^{l}(g, h, n)= \begin{cases}-\infty & \text { if } g=0, \\ 0 & \text { if }(g, h, n)=(1,1,0), \\ 1 & \text { if }(g, h)=(1, \geq 2) \text { or }(g, h, n)=(1,1,>0) \text { or }(\geq 2,1,0), \\ 2 & \text { if }(g, h) \geq(2,2) \text { or }(g, h, n)=(\geq 2,1, \geq 1) .\end{cases}$$
The Kodaira dimension of a non-minimal Lefschetz fibration with $h \geq 1$ is defined to be that of its minimal models. Further it is verified in [35] and [32] that $\kappa^{l}(g, h, n)=\kappa^{s}$. Clearly the subadditivity (3) follows.
3.1.2. Additivity for fibred manifolds. For a holomorphic fiber bundle in the projective category, a classical theorem [61] says that the holomorphic Kodaira dimension $\kappa^{h}$ is additive. The additivity for $\kappa^{t}$ has been established in [129], and there is strong evidence that it is also valid for $\kappa^{s}$.

\section*{0-dimensional fibers}
$\kappa^{s}$ and $\kappa^{h}$ are invariant under finite coverings. Thus $\kappa^{s}$ can be extended to virtually symplectic/complex manifolds, manifolds which are finitely covered by symplectic/complex manifolds: If $X$ is finitely covered by a symplectic/complex manifold $M$, then $v \kappa(X):=\kappa^{s / h}(M)$.

\section*{1-dimensional fibers}

When $M=S^{1} \times Y$ it was conjectured by Taubes and confirmed by Friedl and Vidussi [47] that $M$ is symplectic if and only if $Y$ is fibred. In this case the additivity is verified in [129].

For general circle bundles it is essentially understood in [48] which ones admit symplectic structures, and the virtual Betti number calculations in [11] provide ample evidence for the additivity of $\kappa^{s}$ for $S^{1}$-bundles, ie. $\kappa^{s}(M)=\kappa^{t}(Y)$.

\section*{2-dimensional fibers}

Thurston observed that surface bundles admit symplectic structures if the fibers are homologically essential, and the converse is also true ([127]). A consequence of the equality $\kappa^{l}(g, h, n)=\kappa^{s}$ in [35] is that $\kappa^{s}$ is additive for surface bundles over surfaces, ie. $\kappa^{s}=\kappa^{t}(f i b e r)+\kappa^{t}$ (base).

\section*{3-dimensional fibers}

It is not completely understood yet which mapping tori admit symplectic structures. However, a 'virtual' progress has been made. To put it in context recall that, by Agol's solution of virtual fibration conjecture, all irreducible 3-manifolds are virtually fibred except some graph manifolds.

Suppose $X$ fibers over the circle with fiber $Y$ and $Y$ is finitely covered by a mapping torus with fiber $F$. Applying Luttinger surgery to $F \times T^{2}$, it is shown in [90] (cf. also [14]) that
\begin{itemize}
\item[(1)] If $g(F)=0$, then $X$ is virtually symplectic and $v \kappa(X)=-\infty$.
\item[(2)] If $g(F)=1$, then $X$ is virtually symplectic if and only if $v b_{1}(X) \geq 2$. Moreover, if $v b_{1}(X) \geq 2$, then $v \kappa(X)=0$.
\item[(3)] If $g(F)>1$, then $X$ is virtually symplectic with $v \kappa=1$.
\end{itemize}
In particular, if $v \kappa^{s}(X)$ is defined then it satisfies the additivity $v \kappa(X)=$ $\kappa^{t}(F)+\kappa^{t}(Y)$.

\subsection*{3.2. Behavior under Surgeries.}
3.2.1. Luttinger surgery. It is shown in [59] that $\kappa^{s}$ is unchanged under Luttinger surgery along Lagrangian tori ([96], [9]). Combined with the diffeomorphism invariance of $\kappa^{s}$, this fact can be used to distinguish non-diffeomorphic manifolds.

In [6], [7], [15], [46], several symplectic manifolds homeomorphic to small rational manifolds are constructed via Luttinger surgery. With $\kappa^{s}=2$ manifolds such as $\Sigma_{g} \times \Sigma_{h}$ with $g, h \geq 2$ as the building blocks, the invariance of $\kappa^{s}$ gives a quick alternative proof that these manifolds are small exotic manifolds. The invariance of $\kappa^{s}$ under Luttinger surgery is also used effectively in [5] to construct non-holomorphic Lefschetz fibrations with arbitrary $\pi_{1}$, starting from Kähler surfaces with $\kappa^{s}=\kappa^{s}=1$.
3.2.2. Genus 0 sum and rational blow-down. For a genus zero sum, the computation $\kappa^{s}$ is largely carried out in [33] by Dorfmeister and finished in [34]. The general behavior of $\kappa^{s}$ under a genus zero sum is non-decreasing. The rational blow-down of -4 spheres in $\mathbb{C} P^{2} \# 10 \overline{\mathbb{C} P^{2}}$ is the most interesting
case. The resulting manifolds include some Dolgachev surfaces, which have $\kappa^{s}=1$, and the Enriques surface which has $\kappa^{s}=0$.

General rational blow-down operations of Fintushel-Stern [43] and Symington [119] have been used effectively for the symplectic geography problem, and especially striking in [108] and subsequent works by Fintushel, J. Park, Stern, Stipsicz and Szabo for the exotic geography problem. We postulate that $\kappa^{s}$ also non-decreases under an arbitrary rational blow-down. It will be nice to have a simple way to determine the change of $\kappa^{s}$ (as well as for the related star surgery in [66]).
3.2.3. Positive genus sum. Usher systematically investigated $\kappa^{s}$ for positive genus sum in [126]. His calculation is interpreted in [95] in terms of properties of the adjoint class of the gluing surfaces. It is further rephrased in terms of relative Kodaira dimension of the summands in [93] (cf. Section 5.1): If $(M, \omega)$ is the positive genus fiber sum of $\left(M_{i}, \omega_{i}\right)$ along $F_{i} \subset M_{i}$, then
$$\kappa^{s}(M, \omega)=\max \left\{\kappa^{s}\left(M_{1}, \omega_{1}, F_{1}\right), \kappa^{s}\left(M_{2}, \omega_{2}, F_{2}\right)\right\} .$$
Such a formula is especially effective in distinguishing exotic smooth structures on symplectic manifolds homeomorphic to small rational manifolds (eg. [2]). Notice that this formula applies to Fintushel-Stern's powerful knot surgery ([44]), which is a genus 1 fiber sum.

\section*{4. Main problems and progress in each class}

In this section we will discuss properties of symplectic 4-manifolds in each $\kappa^{s}$ class. The slogan is: the smaller $\kappa^{s}$ the more we understand.
4.1. Surfaces and symmetry of $\kappa=-\infty$ manifolds. The symplectic 4-manifolds with Kodaira dimension $\kappa=-\infty$ have been classified. As smooth 4-manifolds, they are rational or ruled (ie. diffeomorphic to projective surfaces which are rational or ruled). And the moduli space of symplectic structures is identified with the quotient of the symplectic cone by the geometric automorphism group. Moreover, both the symplectic cone and the geometric automorphism group have been explicitly determined.

A central ingredient of all the progress is the existence and abundance of non-negative self-intersection symplectic surfaces. The major source of such surfaces is Taubes symplectic Seiberg-Witten theory. Recall that the GT (which means Gromov-Taubes) invariant of a class $e$ in $H_{2}(M ; \mathbb{Z})$ is a Gromov type invariant defined by Taubes (cf. [61]) counting embedded (but not necessarily connected) symplectic surfaces representing the Poincaré dual to $e$, and $e$ is called a GT basic class if its GT invariant is nonzero.

There are still many open problems. Among them are: Symplectic versus Kähler, classifying symplectic surfaces and Lagrangian surfaces, determining the symplectomorphism group.
4.1.1. Smooth and symplectic classification. The smooth classification in [94] is achieved by finding a symplectic sphere with non-negative self-intersection. Such manifolds are uniruled, and a uniruled manifold is a rational manifold or an irrational ruled manifold according to McDuff [98].

There are other characterizations in terms of smooth surfaces:
\begin{itemize}
\item[-] The existence of a smoothly embedded sphere with non-negative self-intersection ([80]).
\item[-] The existence of a smoothly embedded surface with positive genus $g$ and self-intersection $2 g-1$ ([88]).
\end{itemize}
Notice that all $\kappa^{s}=-\infty$ manifolds have $b^{+}=1$. Due to the fundamental fact that any $b^{+}=1$ manifold has infinitely many GT classes, the inflation process of LaLonde-McDuff ([69]) can be applied effectively, which is essential for the symplectic classification (up to diffeomorphisms) of $\kappa^{s}=-\infty$ manifolds.

The moduli space of symplectic structures, which is the space of diffeomorphic symplectic forms, is completely understood (See [112] for a beautiful account).
\begin{itemize}
\item[(1)] Symplectic structures are unique up to diffeomorphisms in each cohomology class ([68], [87]).
\item[(2)] There is a unique symplectic canonical class up to orientation-preserving diffeomorphisms.
\item[(3)] Therefore the moduli space $\mathcal{M}_{X}$ is identified with the quotient of the symplectic cone by the geometric automorphism group. Here, the symplectic cone is the open set of cohomology classes represented by symplectic forms, and the geometric automorphism group records the action of the orientation-preserving diffeomorphism group on homology.
\item[(4)] The symplectic cone is completely determined in terms of the set $\mathcal{E}$ ([85]). And the subcone with a fixed canonical class is a convex set, in particular, path connected.
\item[(5)] The geometric automorphism group is generated by the reflections on $\mathcal{E}, \mathcal{L}$ and $\mathcal{H}$, where $\mathcal{L}$ and $\mathcal{H}$ are the sets of the classes represented by smoothly embedded spheres, and having square -2 and 1 respectively ([51], [83]).
\item[(6)] The sets $\mathcal{E}, \mathcal{L}$ and $\mathcal{H}$ are explicitly determined ([82]).
\end{itemize}

All $\kappa^{s}=-\infty$ manifolds admit Kähler structures. However, the following symplectic versus Kähler question is still open.

Question 4.1. For which $\kappa^{s}=-\infty$ manifold does there exist non-Kähler symplectic form?

Surprisingly, it is shown in [25] that there are non-Kähler symplectic forms on one point blow up of elliptic ruled surfaces. Due to properties (1) and (2), to show that any symplectic form is Kähler on a given $\kappa^{s}=-\infty$ manifold, it suffices to show that the generic Kähler cone coincides with the
sub-symplectic cone with the fixed Kähler canonical class. Such a equality of cones is known to be true for $S^{2}$-bundles ([99]) and up to 9 blow-ups of the projective plane (cf. [19] for the connection to the longstanding Nagata conjecture and [79] for results on other Kähler surfaces).
4.1.2. Symplectic and Lagrangian surfaces. The following is a conjecture in [34] regarding the existence of symplectic surfaces.

Conjecture 4.2. Let $(M, \omega)$ be a symplectic 4-manifold with $\kappa^{s}=-\infty$. Let $A \in H_{2}(M, \mathbb{Z})$ be a homology class. Then $A$ is represented by a connected $\omega$-symplectic surface if and only if
\begin{itemize}
\item[(1)] $[\omega] \cdot A>0$,
\item[(2)] $g_{\omega}(A) \geq 0$, where $g_{\omega}(A)$ is defined by $2 g_{\omega}(A)-2=K_{\omega} \cdot A+A \cdot A$,
\item[(3)] $A$ is represented by a smooth connected surface of genus $g_{\omega}(A)$.
\end{itemize}

A rather general answer comes from Taubes' symplectic SW theory and the SW wall crossing formula ([65], [86]): any sufficiently large $\omega$-positive class is represented by an $\omega$-symplectic surface. In light of properties (1), (2), and (4) of the moduli space of symplectic structures, the following birational stability result in [34] reduces the verification of the conjecture for an arbitrary symplectic form to some fixed symplectic form $\omega_{0}$.

Theorem 4.3. Let $(M, \omega)$ be a symplectic manifold with $b^{+}=1$ and $V$ an $\omega$-symplectic surface. Then for any symplectic form $\tilde{\omega}$ homotopic to $\omega$ and positive on the class $[V]$, there exists an $\tilde{\omega}$-symplectic surface $\tilde{V}$, which is smoothly isotopic to $V$.

This stability is applied in [34] to classify symplectic spheres of negative self-intersection.

For orientable Lagrangian surfaces, the existence problem is completely solved. Since $\kappa^{s}=-\infty$ manifolds have $b^{+}=1$, there are no essential orientable Lagrangian surfaces of positive genus. For Lagrangian spheres there is the following simple criterion in [92] (compare with Conjecture 4.2): $A \in H_{2}(M ; \mathbb{Z})$ contains a Lagrangian sphere if and only if
\begin{itemize}
\item[-] $\omega(A)=0$,
\item[-] $A \cdot A=-2$,
\item[-] $A$ is represented by a smooth sphere.
\end{itemize}

In summary, a nonzero class in $H_{2}(M ; \mathbb{Z})$ is represented by a Lagrangian surface if and only if it is in the set $\mathcal{L}$ and has zero pairing with $\omega$. Furthermore, the solution has been extended to Lagrangian ADE configurations in [34]. For uniqueness, it is shown in [92] and [18] that homologous Lagrangian spheres are unique up to smooth isotopy. The much stronger uniqueness up to Hamiltonian isotopy was first established by Hind for the monotone $S^{2} \times S^{2}$ ([57]) and then by Evans for monotone manifolds with Euler number at most 7([36]). For further extensions see [92]. On the other hand, Seidel ([113]) discovered that Hamiltonian uniqueness fails for the monotone manifold with Euler number 8.

There has been progress towards classifying Lagrangian $\mathbb{R} P^{2}$ in small rational manifolds (cf. [18] for the status). With the recent classification of symplectic spheres with self-intersection -4 in [34], it seems possible to classify Lagrangian $\mathbb{R} P^{2}$ since they correspond to symplectic -4 spheres via rational blow down.
4.1.3. Symplectic mapping class group and symplectic Cremona map. A consequence of the simple criterion for the existence of Lagrangian spheres is the calculation of the homological action of the symplectomorphism group $\operatorname{Symp}(M, \omega)$ in [92]: the action is generated by Dehn twists along Lagrangian spheres.

The Torelli part is much harder to determine. It is known to be connected for rational manifolds with Euler number up to 7, due to many people's work (cf. [84] for references). Hence the symplectic mapping class group is a finite reflection group for these manifolds. On the other hand, Seidel showed that the symplectic mapping class group for the monotone rational manifold with Euler number 8 is infinite ([113] and [37]). The natural question is: Is the symplectic mapping class group infinite for any symplectic rational manifold with Euler number at least 8?

Finite symplectic symmetry is being investigated in [24]. This is the symplectic analogue of the classical Cremona problem in algebraic geometry. A classification of $\mathbb{Z}_{n}$-Hirzebruch surfaces up to orientation-preserving equivariant diffeomorphisms has been achieved in [21].
4.2. Towards the classification of $\kappa=0$ manifolds. The basic problem is the speculation on smooth classification.

Conjecture 4.4. (31, 77]) If $\kappa^{s}(M, \omega)=0$ and $(M, \omega)$ minimal, then $M$ is diffeomorphic to one of the following:
\begin{itemize}
\item[-] K3,
\item[-] Enriques surface,
\item[-] a $T^{2}$ - bundle over $T^{2}$
\end{itemize}

Minimal $\kappa=0$ manifolds are exactly the ones with torsion $K_{\omega}$. If $(M, \omega)$ has $K_{\omega}=0,(M, \omega)$ is called a symplectic Calabi-Yau surface. In the case of SCY, the speculation is that $M$ is diffeomorphic to K3 or a $T^{2}$-bundle over $T^{2}$. Notice all the manifolds in the list above allow some kind of torus fibrations.
4.2.1. Homological classification. Conjecture 4.4 has been verified at the level of homology. The crucial step is to derive the following bound on $b^{+}$.

Theorem 4.5. [76], [10]) Suppose $\kappa(M, \omega)=0$. Then $b^{+}(M) \leq 3$.
This bound on $b^{+}$was established in [106] assuming $b_{1}=0$, and in [77] assuming $b_{1} \leq 4$. The main idea is to apply Furuta's $\operatorname{Pin}(2)$-equivariant finite dimensional approximation ([53]) to the SW equation of the symplectic

Spin ${ }^{c}$ structure to show that $S W\left(K_{\omega}\right)$ is even if $b^{+}>3$. Then invoke Taubes' fundamental calculation $S W\left(K_{\omega}\right)= \pm 1$ ([120]).

Theorem 4.5 has the following consequences: If $M$ is minimal with $\kappa^{s}(M)=$ 0, then
\begin{itemize}
\item[(1)] $b^{-}(M) \leq 19$.
\item[(2)] $b_{1}(M) \leq 4$.
\item[(3)] The signature is equal to 0, -8, -16.
\item[(4)] Euler number is equal to 0, 12, 24.
\item[(5)] $M$ either has the same $\mathbb{Z}$-cohomology group and intersection form as the K3 or the Enriques surface, or the same $\mathbb{Q}$-homology group and intersection form as a $T^{2}$-bundle over $T^{2}$.
\item[(6)] If $b_{1}(M)=4$, then $H^{*}(M ; \mathbb{Q})$ is generated by $H^{1}(M ; \mathbb{Q})$ and hence isomorphic to $H^{*}\left(T^{4} ; \mathbb{Q}\right)$ as a ring.
\end{itemize}

Notice that when $M$ is minimal, we have
$$0=K_{\omega} \cdot K_{\omega}=2 \chi(M)+3 \sigma(M)=4-4 b_{1}(M)+5 b^{+}(M)+b^{-}(M),$$
from which both bounds (1) and (2) follow. (3) then follows from the divisibility of $\sigma$ by 8, and (4) is a consequence of $2 \chi(M)+3 \sigma(M)=0$. The claim (5) is based on the Euler number bound (4) and the observation that a finite covering of a minimal $\kappa^{s}=0$ manifold is still such a manifold. Finally, (6) relies on (5) and the main result in [111].

Remark 4.6. A famous consequence of Yau's solution to the Calabi conjecture is that any Kähler manifold with torsion canonical class admits Ricci flat metrics, and hence its $b_{1}$ is bounded by the real dimension ([128]). Notice that this is still valid for symplectic 4-manifolds with torsion canonical class due to consequence (2) above. Thus it was tempting to speculate the $b_{1}$ bound continues to hold for any symplectic manifold with torsion canonical class. However, Fine and Panov showed in [41] that this is far from true in dimension 6 and higher (see also [39], [40]). Fine-Panov's manifolds, which are obtained by Crepant resolutions of orbifold twister spaces coming from hyperbolic geometry, certainly cannot carry Ricci flat metrics. Nevertheless, these singular twistor spaces carry Chern-Ricci flat Almost Kähler metrics (cf. [109]).

The following table lists possible homological invariants of minimal $\kappa=0$ manifolds:

\begin{tabular}[t]{|l|l|l|l|l|l|}
\hline $b_{1}$ & $b_{2}$ & $b^{+}$ & $\chi$ & $\sigma$ & known manifolds \\
\hline 0 & 22 & 3 & 24 & -16 & K3 \\
\hline 0 & 10 & 1 & 12 & -8 & Enriques surface \\
\hline 4 & 6 & 3 & 0 & 0 & 4-torus \\
\hline 3 & 4 & 2 & 0 & 0 & $T^{2}$-bundles over $T^{2}$ \\
\hline 2 & 2 & 1 & 0 & 0 & $T^{2}$-bundles over $T^{2}$ \\
\hline
\end{tabular}

Accordingly, there are three homology types: K3 type, Enriques type, and torus bundle type, distinguished by the Euler number.

All the known $\kappa=0$ manifolds allow $T^{2}$-fibrations. One approach towards the smooth classification is to detect the existence of tori. Suppose a homology K3 has a winding family, then via parametrized SW theory there is an embedded symplectic torus for some symplectic form in the winding family. Existence of symplectic torus can be proved in homology $T^{2}$-bundles with $T^{2}$.
4.2.2. Virtual $b_{1}, S C Y$ group, and partial homeomorphism classification. Recall that $v b_{1}(M)$ is the supremum of $b_{1}(\tilde{M})$ among all finite covers $\tilde{M}$. If $(M, \omega)$ has $\kappa^{s}=0$, then any finite cover also has $\kappa^{s}=0$. This implies that $v b_{1}(M) \leq 4$. The following question is raised in [49]: Is the $\mathbb{F}_{p}$-virtual Betti number of a $\kappa^{s}=0$ manifold bounded by 4?

Any minimal $\kappa^{s}=0$ symplectic 4-manifold has torsion symplectic canonical class so it admits a finite cover with trivial symplectic canonical class. Thus such a manifold could be called a virtual SCY surface. Following [50], a finitely presented group $G$ is called a (v)SCY group if $G=\pi_{1}\left(M_{G}\right)$ for some (virtual) SCY surface $M_{G}$. If $b_{1}(G)=0$ and $G$ is residually finite, then $G=1$ or $\mathbb{Z}_{2}$ and the corresponding vSCY surfaces are unique up to homeomorphism.
\begin{itemize}
\item[-] If $G=1$, then $M_{G}$ has the same intersection form as the K3 surface and hence is homeomorphic to the K3 surface by Freedman's fundamental classification of simply connected topological 4-manifolds ([106]).
\item[-] If $G=\mathbb{Z}_{2}$, then $M_{G}$ has the same intersection form and $w_{2}$-type as the Enriques surface and hence is homeomorphic to the Enriques surface by the extension in [56] of Freedman's classification to the case $\pi_{1}=\mathbb{Z}_{2}$ ([77]).
\end{itemize}
If $b_{1}(G)>0$ then it follows from the consequence (5) of Theorem 4.5 that
$$2 \leq v b_{1}(G) \leq 4, \quad \chi\left(M_{G}\right)=\sigma\left(M_{G}\right)=0 .$$
In this case, Friedl and Vidussi showed in [50]: If $G=\pi_{1}$ of a (Infra)solvable manifold, then the corresponding SCY surfaces are unique up to homeomorphism.

Since all $T^{2}$-bundles over $T^{2}$ are solvable manifolds, the beautiful conclusion is that, any known vSCY group $G$ determines the homeomorphism type of the corresponding vSCY surfaces.
4.2.3. Constructions. It has been verified that various constructions only produce minimal $\kappa^{s}=0$ manifolds in Conjecture 4.4. There are also a couple of constructions potentially producing new $\kappa=0$ manifolds.

\section*{Fiber bundles}

Suppose $(M, \omega) \rightarrow B$ is a fibre bundle and $\kappa^{s}(M)=0$.
If $B$ is a surface then $M$ is a $T^{2}$ bundle over $T^{2}$ ([35], [11], [50]).
For mapping tori with prime fiber, the fiber has to be a $T^{2}$-bundle over $S^{1}$, and $M$ is a $T^{2}$-bundle over $T^{2}([90])$.

For circle bundles, the base $B$ must be a $T^{2}$-bundle ([49]). In particular, $M$ is a mapping torus with fiber $T^{3}$, and hence a $T^{2}$-bundle over $T^{2}$ by the claim above on mapping tori.

\section*{Lefschetz fibrations/pencils}

Smith observed that if a SCY surface $M$ admits a genus $g$ Lefschetz fibration with singular fibers, then $g=1$ by the adjunction formula and it follows from the classification of genus 1 Lefschetz fibrations of Moishezon+Matsumoto that $M$ is the K3 surface or a $T^{2}$-bundle over $T^{2}$ ([114]). More generally, if multiple fibers are allowed, then $M$ is the Enriques surface.

On the other hand, according to Donaldson ([30]), any symplectic manifold admits Lefschetz pencils. Baykur and collaborators are able to read off the Kodaira dimension from monodromy factorizations of Lefschetz pencils with multisections in framed mapping class groups ([13]). This could potentially lead to discovering new $\kappa^{s}=0$ manifolds distinguished by the fundamental group.

\section*{Fiber sums}

If ( $M, \omega$ ) with $\kappa^{s}=0$ is a non-trivial genus 0 fibred sum, then $M$ is diffeomorphic to the blow up of the Enriques surface, as the rational blow down of $\mathbb{C} P^{2} \# l \overline{\mathbb{C P}}^{2}$ for some $l \geq 10$ ([33]).

If $(M, \omega)$ with $\kappa^{s}=0$ is a non-trivial positive genus fibred sum, then the summands have $\kappa^{s}=-\infty$ (rational or ruled), and the sum is along tori representing $-K_{\omega}$ ([126]). Moreover, if the sum is relatively minimal then $(M, \omega)$ is a vSCY surface by [125]. In this case, $M$ is diffeomorphic to the K3 surface, the Enriques surface, or a $T^{2}$-bundle over $T^{2}$ with $b_{1}=2$, and the only decompositions are as follows: $K 3=E(1) \#_{f} E(1)$ along fibers, Enriques $=E(1) \#_{f}\left(S^{2} \times T^{2}\right)$ along a fiber and a bi-section, and the sum of two $S^{2}$-bundles over $T^{2}$ along bi-sections give rise to $T^{2}$-bundles over $T^{2}$. We remark that Akhmedov constructed in [1] a family of simply connected symplectic CY 3-folds via fiber sums along $T^{4}$.

\section*{Hypersurfaces in $\mathbb{C} P^{3}$}

Smooth complex hypersurfaces in $\mathbb{C} P^{3}$ of the same degree are diffeomorphic to each other, and the degree 4 ones are just the K3 surface.

Question 4.7. Is a degree 4 symplectic hypersurface in $\mathbb{C} P^{3}$ diffeomorphic to K3?

Such a symplectic hypersurface is a symplectic CY surface with $c_{2}=24$. By the homological classification, $b_{1}$ vanishes and it is a homology K3.

Remark 4.8. By the Lefschetz hyperplane theorem, any complex hypersurface is simply connected. This is known to be true for symplectic hypersurfaces up to degree 3. In fact, via pseudo holomorphic curve theory, Hind [58] showed that degree 1 and 2 symplectic hypersurfaces are diffeomorphic to the complex hypersurfaces of the same degree. Further, for degree up to 3, a symplectic hypersurface has Kodaira dimension $-\infty$, thus the same conclusion
for degree 3 can be shown to follow from the classification of $\kappa=-\infty$ manifolds. On the other hand, McLean ([103]) recently constructed Donaldson type symplectic hypersurfaces ([29]) with large degree and positive $b_{1}$.

\section*{Luttinger surgery}

Luttinger surgery is a vSCY surgery and even preserves the K3, Enriques, $T^{2}$-bundle types ([59]). It is easy to check that some (possibly all) $T^{2}$-bundles over $T^{2}$ can be obtained from $T^{4}$ via Luttinger surgeries. More interestingly, if there is a Lagrangian torus in the K3 such that the resulting manifold after Luttinger surgery is not simply connected, then it would be a new symplectic CY surface. We remark that the coisotropic surgery, which is a higher dimensional analogue of Luttinger surgery, has been explored in [1], [16] to construct 6-dimensional symplectic CY manifolds.

\subsection*{4.3. Euler number and decomposition of $\kappa^{s}=1$ manifolds.}
4.3.1. On the non-negativity of Euler number. Gompf's family of manifolds in [54] which any finitely presented group as the fundamental group have $\kappa^{s}=1$, so classification in this case is unattainable. A fundamental conjecture is

Conjecture 4.9. If $\kappa^{s}(M)=1$ then its Euler number $\chi(M)$ is non-negative.
We have mentioned that the Euler number is indeed non-negative when $\kappa^{s}=0$. In fact, the only known symplectic 4-manifolds with negative Euler number are $g \geq 2 S^{2}$-bundles and their blow ups up to $4 g-5$ points. Assuming the conjecture, the geography of $\kappa=1$ manifolds was investigated in [17].

When $b^{+}=1$ this conjecture holds. This implication is essentially contained in [94], which says that $b_{1} \leq 2$ if $b^{+}=1$ and $\kappa^{s} \geq 0$. If a manifold with $b_{1}=2$ and $b^{+}=1$ has negative Euler number, then it must have $b_{2}=0$. But such a manifold has $\chi=-1$ and $\sigma=1$ and hence $K_{\omega} \cdot K_{\omega}=2 \chi+3 \sigma=1$. Since it has $b^{-}=0$ and hence minimal, such a manifold has $\kappa^{s}=2$.

One approach to this conjecture for manifolds with $b^{+}=2$ is to note that (i) Gompf's manifolds are constructed via genus 1 fiber sum along square zero tori and (ii) the non-negativity of $\chi$ is preserved under a genus 1 fiber sum. Thus it is natural to postulate whether manifolds with $\kappa=1$ and $b^{+}=2$ can be split along symplectic tori into manifolds with $b^{+}=1$. To find the splitting tori, a useful observation is that a genus 1 fiber sum often leads to non-trivial Gromov-Taubes counting for the resulting torus class (see [101]). When $b^{+} \geq 2$, there are only finitely many GT classes, and when $\kappa^{s}=1$ and minimal, any GT class is a square zero class represented by a disjoint union of symplectic tori. Thus we are led to the simple (but hard) question: can we always find a splitting torus from these finitely many GT classes?
4.3.2. The $G T$ length of $K_{\omega}$ and conjectured upper bound on $b^{+}$. When $b^{+} \geq$ 2, the symplectic canonical class $K_{\omega}$ is a GT class. It is also conjectured in [78] that for a symplectic manifold with $\kappa^{s}=1$,
$$b^{+} \leq 3+2 l\left(K_{\omega}\right),$$
where $l\left(K_{\omega}\right)$ is the GT length of $K_{\omega}$.
Definition 4.10. A (fine) GT decomposition of a nonzero class e is an unordered set of pairwise orthogonal nonzero GT classes $\left\{A_{1}, \ldots, A_{m}\right\}$ such that $e=A_{1}+\cdots+A_{m}$. $m$ is called the length of the decomposition. The $G T$ length $l(e)$ of the class $e$ is the maximal length among all such decompositions, and it is defined to be zero if $e=0$ or $e$ is not a GT class.

The inequality (5) is a variation of the Noether type inequalities proposed in [97], [45]. Notice that it holds for elliptic surfaces $E(n)$, where $b^{+}=2 n-1$ and $l\left(K_{\omega}\right)=n-2$. It also seems not hard to verify that (5) is preserved under a genus 1 sum. In addition, Theorem 4.5 can be interpreted as asserting that the inequality (5) holds when $\kappa=0$ since $l\left(K_{\omega}\right)=0$ in this case.

\subsection*{4.4. Geography and exotic geography of $\kappa^{s}=2$ manifolds.}
4.4.1. Geography. The symplectic geography problem was originally posed by Gompf in [54]. In the case $\kappa^{s}=2$, it refers to the problem of determining which ordered pairs of positive integers are realized as $\left(\chi(M), K_{\omega} \cdot K_{\omega}\right)$ for some minimal symplectic 4-manifold $M$. There has been considerable progress: all the lattice points with $K_{\omega} \cdot K_{\omega}-2 \chi(M)=3 \sigma(M) \leq 0$ have been filled (see [3] and references therein). The region of positive $\sigma$ is not well understood yet (see [4] for the current status). The basic conjecture is

Conjecture 4.11. $\kappa^{s}=2$ manifolds satisfy the Bogomolov-Miyaoka-Yau inequality $K_{\omega} \cdot K_{\omega} \leq 3 \chi(M)$.

The BMY inequality is valid for Kähler surfaces of general type, which is a classical theorem of Miyaoka ([105]) and Yau ([128]). LeBrun ([71], [72]) verified this for 4-manifolds with Einstein metrics, and recently Hamenstaedt ([55]) verified it for surface bundles over surfaces. Symplectic manifolds near the BMY line have been constructed in [116], [117] and [8]. An open problem is to construct symplectic non-Kähler manifolds on the BMY line. We remark that Conjecture 4.9 for minimal $\kappa^{s}=1$ manifolds fits with Conjecture 4.11.

On the other hand, there are also the Noether type inequalities proposed in [97], [45], which are conjectured lower bounds for $K_{\omega} \cdot K_{\omega}$ (cf. a sightly stronger version in [78], and see [38] for progress).

As in the $\kappa^{s}=1$ case, one approach to the geography conjectures is to decompose along tori: If $M$ has $b^{+} \geq 2$ and contains a square zero class of symplectic torus with non-trivial Gromov-Taubes invariant, can $M$ be split into a genus 1 fiber sum? This would be the analogue of the toroidal decomposition in dimension 3 along $\pi_{1}$-injective tori. When $b^{+} \geq 2$, we call
a manifold atoroidal if there are no genus 1 GT invariants. The geography of such manifolds was investigated in [42].
4.4.2. Exotic geography. It is understood now that most positive pairs have more than one, or infinitely many representatives as well. The current interest is on small pairs. Remarkable progress on exotic small manifolds (necessarily having $\kappa^{s}=2$ ) has been made by Akhmedov-D. Park, J. Park, Fintushel-Stern, Stipsicz-Oszváth-Szabo, Baldridge-Kirk etc. (cf. discussions in section 3.2).

There are at most countably many distinct smooth structures on a closed topological manifold, and it has been suggested to use
\begin{itemize}
\item[-] the minimal genus function ([70], [27]),
\item[-] size of the geometric automorphism groups ([26]),
\item[-] size of finite symmetry ([23])
\end{itemize}
to order smooth/symplectic structures on a topological 4-manifold. The moral is that a smooth structure on a topological 4-manifold is considered the 'standard one' if it has the smallest minimal genus function, largest geometric automorphism group, or largest finite symmetry among all smooth structures. In [27] it is verified that $S^{2} \times T^{2}, S^{2}$-bundles over $S^{2}$, the Enriques surface, and $\mathbb{C} P^{2} \# n \overline{\mathbb{C} P^{2}}$ with $n \leq 9$ are standard in the sense of having the smallest minimal genus function. It will be nice to show that $\mathbb{C} P^{2} \# n \overline{\mathbb{C} P^{2}}$ is 'standard' for any $n$.

\section*{5. Extensions}
5.1. Relative Kodaira dim for a symplectic pair. Let $(M, \omega)$ be a connected, closed symplectic 4-manifold and $F \subset(M, \omega)$ a symplectic surface, not necessarily connected but having no sphere components. For such a pair the notion of relative Kodaira dimension is introduced in [93].

The definition involves the adjoint class of $F$, which is $K_{\omega}+[F]$. Assume that $F$ is maximal in the sense that its adjoint class satisfies
$$\left(K_{\omega}+[F]\right) \cdot E \geq 0$$
for any $E \in \mathcal{E}_{\omega}$. Clearly, this is the same as $[F] \cdot E>0$ for any class $E$, or equivalently, the complement of $F$ is minimal. Thus we call a pair minimal if $F$ is maximal. As in the absolute case, any pair can be blown down to a minimal pair. What is a bit surprising is that the minimal models are unique in the relative setting.

The adjoint class of a maximal $F$ without sphere components satisfies the following positivity.

Lemma 5.1. Suppose $F$ is maximal and has no sphere components.
If $\kappa^{s}(M, \omega) \geq 0$, then
$$\begin{gathered}
\left(K_{\omega}+[F]\right) \cdot[\omega]>0, \quad\left(K_{\omega}+[F]\right)^{2} \geq 0 . \\
\text { If } \kappa^{s}(M, \omega)=-\infty \text { and }\left(K_{\omega}+[F]\right)^{2}>0, \text { then }\left(K_{\omega}+[F]\right) \cdot[\omega]>0 .
\end{gathered}$$

In particular, it is impossible to have a maximal surface without sphere components such that
$$\left(K_{\omega}+[F]\right) \cdot \omega=0 \quad \text { and } \quad\left(K_{\omega}+[F]\right)^{2}>0 .$$

Definition 5.2. Let $F \subset(M, \omega)$ be a symplectic surface without sphere components.
\begin{itemize}
\item[-] If $F$ is empty, then $\kappa^{s}(M, \omega, F)$ is defined to be $\kappa^{s}(M, \omega)$.
\item[-] Suppose $F$ is non-empty and maximal. Then
$$\kappa^{s}(M, \omega, F)=\left\{\begin{array}{cl}
-\infty & \text { if }\left(K_{\omega}+[F]\right) \cdot \omega<0 \text { or }\left(K_{\omega}+[F]\right)^{2}<0, \\
0 & \text { if }\left(K_{\omega}+[F]\right) \cdot \omega=0 \text { and }\left(K_{\omega}+[F]\right)^{2}=0, \\
1 & \text { if }\left(K_{\omega}+[F]\right) \cdot \omega>0 \text { and }\left(K_{\omega}+[F]\right)^{2}=0, \\
2 & \text { if }\left(K_{\omega}+[F]\right) \cdot \omega>0 \text { and }\left(K_{\omega}+[F]\right)^{2}>0 .
\end{array}\right.$$
\item[-] For a general pair, the Kodaira dimension is defined to be that of its unique minimal model.
\end{itemize}
$\kappa^{s}(M, \omega, F)$ is well defined in light of Lemma 5.1. Here are basic properties of $\kappa^{s}(M, \omega, F)$ :
\begin{itemize}
\item[(1)] Suppose $F_{1}, F_{2} \subset(M, \omega)$ are maximal symplectic surfaces without sphere components. If $\left[F_{1}\right]=\left[F_{2}\right]$, then $\kappa^{s}\left(M, \omega, F_{1}\right)=\kappa^{s}\left(M, \omega, F_{2}\right)$.
\end{itemize}
$$\kappa^{s}(M, \omega, F) \geq \kappa^{s}(M, \omega) .$$
\begin{itemize}
\item[(3)] The formula (4) for a positive genus fiber sum holds.
\item[(4)] Suppose a nonempty surface $F \subset(M, \omega)$ is maximal with each component of positive genus. Then
\begin{itemize}
\item[-] $\kappa^{s}(M, \omega, F)=-\infty$ if and only if $M$ is a genus $h \geq 1 S^{2}$-bundle, and $F$ is a section.
\item[-] $\kappa^{s}(M, \omega, F)=0$ if and only if $\kappa^{s}(M)=-\infty$ and $[F]=-K_{\omega}$.
\end{itemize}
\end{itemize}

Although Lemma 5.1 is not valid for spheres, $\kappa^{s}(M, \omega, F)$ can be extended to an arbitrary embedded symplectic surface $F \subset(M, \omega)$ as follows: Let $F^{+}$ be the surface obtained from $F$ by removing the sphere components, and define $\kappa^{s}(M, \omega, F)$ as $\kappa^{s}\left(M, \omega, F^{+}\right)$. All the results still hold in this more general setting with obvious modifications. We notice that the above definition is similar in one aspect to that of the Thurston norm of 3-manifolds: the 2-spheres have to be discarded. One explanation is that a 2-sphere has $\kappa^{t}=-\infty$, so it behaves like the empty set.

Due to Property (1), it is possible to further extend $\kappa^{s}(M, \omega, F)$ to the case of $F$ being a symplectic surface with pseudo-holomorphic singularities, or a weighted symplectic surface. In algebraic geometry there is the notion of the log Kodaira dimension of a noncomplete variety introduced by Iitaka (see [61]).

Question 5.3. For a projective pair, is the relative Kodaira dimension equal to Iitaka' s log Kodaira dimension?

The log Kodaira dimension of cyclic affine surfaces has been extensively studied, so we could use them as testing ground. In fact, results in ([104]) strongly suggest the symplectic nature of log Kodaira dimension for affine surfaces.
5.2. Symplectic manifolds with concave boundary. More generally, we ask for what open symplectic manifolds we can define the Kodaira dimension. An appropriate category consists of symplectic 4-manifolds with concave boundary. Such manifolds are also called symplectic caps. In [88], uniruled caps and Calabi-Yau caps are introduced.

Definition 5.4. Let $(P, \omega)$ be a compact symplectic 4-manifold with concave boundary $(Y, \xi)$.
$(P, \omega)$ is called a uniruled cap if $\left[c_{1}(P)\right] \cdot[(\omega, \alpha)]>0$ for a choice of Liouville contact one form $\alpha$ (induced by a choice of Liouville vector field $V$ defined near $Y$ pointing inward along $Y$ ).
$(P, \omega)$ is called a Calabi-Yau cap if $c_{1}(P)$ is a torsion class.
These caps are useful to establish the finiteness of topological complexity of strong symplectic fillings and Stein fillings. In fact, all known contact 3-manifolds with some sort of bounded topological complexity of fillings admit such caps.

We remark that since $[(\omega, \alpha)]$ is a relative class, $\left[c_{1}(P)\right] \cdot[(\omega, \alpha)]$ is well-defined. The Kodaira dimension of a general cap will be investigated in [89]. The uniruled caps are those with Kodaira dimension $-\infty$, and the Calabi-Yau caps are the minimal ones with Kodaira dimension 0.

Suppose a cap $(P, \omega)$ is embedded in a closed manifold $(M, \Omega)$. It is shown in [88] that if $(P, \omega)$ is uniruled then $\kappa^{s}(M, \Omega)=-\infty$, and if $(P, \omega)$ is Calabi-Yau then $\kappa^{s}(M, \Omega) \leq 0$. We speculate that $\kappa^{s}(P, \omega) \geq \kappa^{s}(M, \Omega)$ holds in general, which will be the analogue of Property (2) for the relative Kodaira dimension.

\section*{References}
\begin{itemize}
\item[] [1] A. Akhmedov, Symplectic Calabi-Yau 6-manifolds, Adv. Math. 262 (2014), 115-125.
\item[] [2] A. Akhmedov, Small exotic 4-manifolds, Algebr. Geom. Topol. 8 (2008), 1781-1794
\item[] [3] A. Akhmedov, S. Baldridge, I. Baykur, P. Kirk, and D. Park, Simply connected min-imal symplectic 4-manifolds with signature less than -1, J. Eur. Math. Soc. (JEMS), 12(1):133-161, 2010.
\item[] [4] A. Akhmedov, M. Hughes, D. Park, Geography of simply connected nonspin symplectic 4-manifolds with positive signature, Pacific J. Math., 261(2):257-282, 2013.
\item[] [5] A. Akhmedov, B. Ozbagci, Exotic Stein llings with arbitrary fundamental group, preprint, arXiv:1212.1743.
\item[] [6] A. Akhmedov, D. Park, Exotic smooth structures on small 4-manifolds, Invent. Math. 173 (2008), no. 1, 209-223.
\item[] [7] A. Akhmedov, D. Park, Exotic smooth structures on small 4-manifolds with odd signatures, Invent. Math., 181(3):577-603, 2010.
\item[] [8] A. Akhmedov, D. Park, G.Urzúa, Spin symplectic 4-manifolds near the Bogomolov-Miyaoka-Yau line, JGGT, 4, (2010), 55-66.
\end{itemize}
\begin{itemize}
\item[] [9] D. Auroux, S. Donaldson, L. Katzarkov, Luttinger surgery along Lagrangian tori and non-isotopy for singular symplectic plane curves, Math. Ann. 326 (2003), no. 1, 185-203.
\item[] [10] S. Bauer, Almost complex 4-manifolds with vanishing first Chern class, J. Differential Geom., 79(1):25-32, 2008.
\item[] [11] I. Baykur, Virtual Betti numbers and the symplectic Kodaira dimension of fibred 4-manifolds, arXiv:1210.6584
\item[] [12] I. Baykur, Virtual betti numbers and the symplectic Kodaira dimension of fibered 4-manifolds, Proceedings of the American Mathematical Society, 142 (2014), 4377-4384.
\item[] [13] I. Baykur, K. Hayano, Multisections of Lefschetz fibrations and topology of symplectic4-manifolds, arXiv:1309.2667
\item[] [14] I. Baykur, S. Friedl, Virtually symplectic fibered 4-manifolds, arXiv:1210.4983, to appear in Indiana University Mathematics Journal.
\item[] [15] S. Baldridge, P. Kirk, Constructions of small symplectic 4-manifolds using Luttinger surgery, J. Differential Geom. 82 (2009), no. 2, 317-361.
\item[] [16] S. Baldridge, P. Kirk, Coisotropic Luttinger surgery and some new examples of symplectic Calabi-Yau 6-manifolds, Indiana Univ. Math. J. 62 (2013), no. 5, 1457-1471.
\item[] [17] S. Baldridge, T. J. Li, Geography of symplectic 4-manifolds with Kodaira dimension one, Algebr. Geom. Topol. 5 (2005), 355-368.
\item[] [18] M. S. Borman, T. J. Li, W. Wu, Spherical Lagrangians via ball packings and symplectic cutting, Selecta Math. (N.S.), 20(1):261-283, 2014.
\item[] [19] P. Biran, From symplectic packings to algebraic geometry and back, European Congress of Mathematics, Vol. II (Barcelona, 2000), 507-524, Progr. Math., 202, Birkhuser, Basel, 2001.
\item[] [20] C. Birkar, Iitaka conjecture $C_{n, m}$ in dimension six, arXiv:0806.4413
\item[] [21] W. Chen, $G$-minimality and invariant negative spheres in $G$-Hirzebruch surfaces, arXiv:1312.0848
\item[] [22] W. Chen, On the orders of periodic diffeomorphisms of 4-manifolds, Duke Math. J. 156 (2011), no. 2, 273-310.
\item[] [23] W. Chen, S. Kwasik, Symmetric symplectic homotopy K3 surfaces, J. Topol. 4 (2011), no. 2, 406-430.
\item[] [24] W. Chen, T.J. Li, W. Wu, Symplectic Cremona map, in preparation.
\item[] [25] P. Cascini, Panov, Symplectic Generic Complex Structures on Four-Manifolds with $b^{+}=1, \mathrm{~J}$. Symplectic Geom. Volume 10, Number 4 (2012), 493-502.
\item[] [26] B. Dai, C. Ho, T. J. Li, Geometric automorphism groups of symplectic 4-manifolds, Topology Appl. 162 (2014), 1-11.
\item[] [27] B. Dai, C. Ho, T. J. Li, Minimal genus for 4-manifolds with $b^{+}=1$, preprint.
\item[] [28] J.-P. Demailly, Khler manifolds and transcendental techniques in algebraic geometry, International Congress of Mathematicians, Madrid 2006, Volume I, Plenary lectures and ceremonies, European Math. Soc. (2007) 153-186.
\item[] [29] S. Donaldson, Symplectic submanifolds and almost-complex geometry, J. Differential Geom. 44 (1996), 666-705.
\item[] [30] S. Donaldson, Lefschetz pencils on symplectic manifolds, J. Differential Geom. 53 (1999), 205-236.
\item[] [31] S. Donaldson, Some problems in differential geometry and topology, Nonlinearity 21 (2008) 157-164.
\item[] [32] J. Dorfmeister, Kodaira dimension of Lefschetz fibrations over tori, to appear in Proc. AMS.
\item[] [33] J. Dorfmeister, Kodaira dimension of symplectic fiber sums along spheres, arXiv:1008.4447, Geom. Dedic. March 2014.
\item[] [34] J. Dorfmeister, T. J. Li, W. Wu, Stability and Existence of Surfaces in Symplectic 4-Manifolds with $b^{+}=1$, arXiv preprint arXiv:1407.1089
\end{itemize}
\begin{itemize}
\item[] [35] J. G. Dorfmeister, W. Zhang, The Kodaira Dimension of Lefschetz Fibrations, Asian J. Math. 13 (2009), no. 3, 341-357.
\item[] [36] J. Evans, Lagrangian spheres in del Pezzo surfaces, J. Topol. 3 (2010) 181-227
\item[] [37] J. Evans, Symplectic mapping class groups of some Stein and rational surfaces, J. Symplectic Geom. 9 (2011) 45-82.
\item[] [38] P. Feehan, T. Leness, The SO(3) monopole cobordism and superconformal simple type, arXiv:1408.5307.
\item[] [39] J. Fine, D. Panov, Symplectic Calabi-Yau manifolds, minimal surfaces and the hyperbolic geometry of the conifold, J. Differential Geom., 82 (1), 155-205, (2009).
\item[] [40] J. Fine, D. Panov, Hyperbolic geometry and non-Kähler manifolds with trivial canonical bundle, Geometry and Topology 14, 1723-1763, (2010).
\item[] [41] J. Fine, D. Panov, The diversity of symplectic Calabi-Yau 6-manifolds, Journal of Topology, 2013.
\item[] [42] R. Fintushel, J. Park, R. Stern, Rational surfaces and symplectic 4-manifolds with one basic class, Algebr. Geom. Topol. 2 (2002), 391-402.
\item[] [43] R. Fintushel, R. Stern, Rational blowdowns of smooth 4-manifolds, J. Diff. Geom. 46, (1997), 181-235.
\item[] [44] R. Fintushel, R. Stern, Knots, links, and 4-manifolds, Inv. Math. 134 (1998), 363-400.
\item[] [45] R. Fintushel, R. Stern, The canonical class of a symplectic 4-manifold, Turkish J. Math. 25 (2001), 137-145.
\item[] [46] R. Fintushel, B. Park, R. Stern, Reverse engineering small 4-manifolds, Algebr. Geom. Topol. 7 (2007), 2103-2116.
\item[] [47] S. Friedl, S. Vidussi, Twisted Alexander polynomials detect fibered 3-manifolds, Ann. of Math. 173 (2011).
\item[] [48] S. Friedl, S. Vidussi, A vanishing theorem for twisted Alexander polynomials with applications to symplectic 4-manifolds, J. Eur. Math. Soc. (JEMS) 15 (2013), no. 6, 2127-2041.
\item[] [49] S. Friedl, S. Vidussi, Symplectic 4-manifolds with $K=0$ and the Lubotzky alternative, Math. Res. Lett. 18 (2011) 513-519.
\item[] [50] S. Friedl, S. Vidussi, On the topology of symplectic Calabi-Yau 4-manifolds, J. Topol. 6 (2013).
\item[] [51] R. Friedman, J. Morgan, Algebraic surfaces and Seiberg-Witten invariants, J. Alg. Geom., 6 (1997), 445-479.
\item[] [52] R. Friedman, Z. Qin, The smooth invariance of the Kodaira dimension of a complex surface, Math. Res. Lett. 1 (1994), no. 3, 369-376.
\item[] [53] M. Furuta, Monopole equation and the 11/8 conjecture, Math. Res. Letters 8 (2001), 279-291.
\item[] [54] R. Gompf, A new construction of symplectic manifolds, Ann. Math., 142 (1995), 527-595.
\item[] [55] U. Hamenstädt, Signatures of surface bundles and Milnor Wood inequalities, arXiv:1206.0236
\item[] [56] I. Hambleton, M. Kreck, Cancellation, elliptic surfaces and the topology of certain four-manifolds, J. Reine Angew. Math. 444 (1993) 79100.
\item[] [57] R. Hind, Lagrangian spheres in $S^{2} \times S^{2}$, Geom. Funct. Anal, 14 (2004) 303-318.
\item[] [58] R. Hind, Symplectic hypersurfaces in $\mathbb{C} P^{3}$, Proc. Amer. Math. Soc. 134 (2006), no. 4, 1205-1211.
\item[] [59] C. Ho, T. J. Li, Luttinger surgery and Kodaira dimension, Asian J. Math. 16 (2012), no. 2, 299-318.
\item[] [60] S. Iitaka, On $D$-dimensions of algebraic varieties, J. Math. Soc. Jap. 23(1971), 356-373
\item[] [61] S. Iitaka, Algebraic geometry. An introduction to birational geometry of algebraic varieties, Graduate Texts in Mathematics, 76. North-Holland Mathematical Library, 24. Springer-Verlag, New York-Berlin, 1982. x+357 pp.
\end{itemize}
\begin{itemize}
\item[] [62] M. Ishida, R. Răsdeaconu, I. Suvaina, On normalized Ricci flow and smooth structures on four-manifolds with $b^{+}=1$, Archiv der Mathematik 92 (2009), no. 4, 355-365.
\item[] [63] O. Kobayashi, Scalar curvature of a metric of unit volume, Math. Ann., 279 (1987), 253-265.
\item[] [64] Kunihiko Kodaira: collected works. Vol. III. Edited by Walter L. Baily, Jr. Iwanami Shoten, Publishers, Tokyo; Princeton University Press, Princeton, N.J., 1975. pp. i-x and 1142-1621.
\item[] [65] P. Kronheimer, T. Mrowka, The genus of embedded surfaces in the projective plane, Math. Res. Letters 1 (1994), 797-808.
\item[] [66] C. Karakurt, L. Starkston, Surgery along star shaped plumbings and exotic smooth structures on 4-manifolds, arXiv:1402.0801
\item[] [67] G. LaNave, T. J. Li, Symplectic Kodaira dimension via Donaldson's peak sections in preparation.
\item[] [68] F. LaLonde, D. McDuff, $J$-curves and the classification of rational and ruled symplectic 4-manifolds, Contact and symplectic geometry Publ. Newton Inst. 8, (Cambridge, 1994), 3-42, Cambridge Univ. Press, Cambridge, 1996
\item[] [69] F. LaLonde, Isotopy of symplectic balls, Gromovs radius and the structure of ruled symplectic 4-manifolds, Math. Ann. 300, no. 2, 273-296, (1994).
\item[] [70] T. Lawson, The minimal Genus problem, Expo. Math. 15(1997), 385-431.
\item[] [71] C. LeBrun, Einstein metrics and Mostow rigidity, MRL 2(1995), 1-8.
\item[] [72] C. LeBrun, Einstein metrics, complex surfaces, and symplectic 4-manifolds, MPCPS 147 (2009), 1-8.
\item[] [73] C. LeBrun, On the Notion of general type, Rend. Mat. Appl. (7) 17 (1997), no. 3, 513-522
\item[] [74] C. LeBrun, Scalar curvature, covering spaces, and Seiberg-Witten theory, New York J. Math. 9 (2003), 93-97
\item[] [75] C. LeBrun, Kodaira dimension and the Yamabe problem, Comm. Anal. Geom. 7 (1999), no. 1, 133-156.
\item[] [76] T. J. Li, Quaternionic bundles and Betti numbers of symplectic 4-manifolds with Kodaira dimension zero, Int. Math. Res. Not., 2006, Art. ID 37385, 28
\item[] [77] T. J. Li, Symplectic 4-manifolds with Kodaira dimension zero, J. Differential Geometry 74 (2006) 321-352.
\item[] [78] T. J. Li, The Kodaira dimension of symplectic 4-manifolds, Floer homology, gauge theory, and low-dimensional topology, 249261, Clay Math. Proc., 5, Amer. Math. Soc., Providence, RI, 2006.
\item[] [79] T. J. Li, The space of symplectic structures on closed 4-manifolds, Third International Congress of Chinese Mathematicians. Part 1, 2, AMS/IP Stud. Adv. Math., 42, pt. 1, vol. 2, Amer. Math. Soc., Providence, RI, 2008, pp. 259277.
\item[] [80] T. J. Li, Smoothly embedded spheres in symplectic 4-manifolds, Proc. AMS. Vol. 127 No. 2 (1999) 609-613.
\item[] [81] T. J. Li, Existence of symplectic surfaces, Geometry and Topology of manifolds, 203-217, Fields Inst. Commun., 47, AMS, 2005.
\item[] [82] B. H. Li, T. J. Li, Symplectic genus, minimal genus and diffeomorphisms, Asian J. Math. 6, (2002), 123-144.
\item[] [83] B. H. Li, T. J. Li, On the diffeomorphism groups of rational and ruled 4-manifolds, J. Math. Kyoto Univ. 46 (2006), no. 3, 583-593.
\item[] [84] J. Li, T. J. Li, W. Wu, The symplectic mapping class group of $\mathbb{C} P^{2} \# n \overline{\mathbb{C} P^{2}}$ with $n \leq 4$, arXiv:1310.7329, to appear in Michigan Math. J.
\item[] [85] T. J. Li, A. Liu, Uniqueness of symplectic canonical class, surface cone and symplectic cone of 4-manifolds with $B^{+}=1, \mathrm{~J}$. Differential Geom. 58 (2001), no. 2, 331-370.
\item[] [86] T. J. Li, A. Liu, Symplectic structures on ruled surfaces and a generalized adjunction inequality, Math. Res. Letters 2 (1995), 453-471.
\end{itemize}
\begin{itemize}
\item[] [87] T. J. Li, A. Liu, General wall crossing formula, Mathematical Research Letters 2, 797-810.
\item[] [88] T. J. Li, C. Y. Mak, Uniruled caps and Calabi-Yau caps, arXiv: 1412.3208.
\item[] [89] T. J. Li, C. Y. Mak, Kodaira dimension of symplectic 4-manifolds with contact boundary, in preparation.
\item[] [90] T. J. Li, Y. Ni, Virtual Betti numbers and virtual symplecticity of 4-dimensional mapping tori, Math. Z. 277 (2014), no. 1-2, 195-208.
\item[] [91] T. J. Li, Y. Ruan, Symplectic Birational Geometry, 307-326, New Perspectives and Challenges in Symplectic Field Theory, AMS. 2009.
\item[] [92] T. J. Li, W. Wu, Lagrangian spheres, symplectic surfaces and the symplectic mapping class group, Geom. Topol. 16 (2012), no. 2, 1121-1169.
\item[] [93] T. J. Li, W. Zhang, Additivity and relative Kodaira dimensions, Geometry and analysis. No. 2, 103135, Adv. Lect. Math. (ALM), 18, Int. Press, Somerville, MA, 2011.
\item[] [94] A. Liu, Some new applications of the general wall crossing formula, Math. Res. Lett. 3 (1996) 569-585.
\item[] [95] T. J. Li, S.T. Yau, Embedded surfaces and Kodaira dimension, preprint.
\item[] [96] K. M. Luttinger, Lagrangian tori in $\mathbb{R}^{4}$, J. Diff. Geom. 42, 220-228 (1995).
\item[] [97] M. Marino, G. Moore, G. Peradze, Four-manifold geography and superconformal symmetry, Math. Res. Lett. 6 (1999), 429-437.
\item[] [98] D. McDuff, The structure of rational and ruled symplectic 4-manifolds, J. Amer. Math. Soc. 3 (1990), 679-712.
\item[] [99] D. McDuff, Notes on ruled symplectic 4-manifolds, Trans. Amer. Math. Soc. 345 (1994), no. 2, 623-639.
\item[] [100] D. McDuff, From symplectic deformation to isotopy, (Irvine, CA, 1996), 85-99, First Int. Press Lect Ser. I, Internat. Press, Cambridge, MA, 1998.
\item[] [101] D. McDuff, Lectures on Gromov invariants for symplectic 4-manifolds, Gauge theory and symplectic geometry, 1997, 175-210.
\item[] [102] D. McDuff, D. Salamon, A survey of symplectic 4-manifolds with $b_{+}=1$, Turkish J. Math. 20 (1996), no. 1, 47-60.
\item[] [103] M. McLean, Private communication, 2014.
\item[] [104] M. McLean, Symplectic invariance of uniruled affine varieties and log Kodaira dimension, Duke Math. J. 163 (2014), no. 10, 1929-1964.
\item[] [105] Y. Miyaoka, On the Chern numbers of surfaces of general type, Inv. Math. 42 (1977), 225-237.
\item[] [106] J. Morgan, Z. Szabo, Homotopy K3 surfaces and Mod 2 Seiberg-Witten invariants, Math. Res. Lett. 4 (1997) 17-21.
\item[] [107] H. Ohta, K. Ono, Notes on symplectic 4-manifolds with $b_{2}^{+}=1$, II, IJM 7 (1996), 755-770.
\item[] [108] J. Park, Simply connected symplectic 4-manifolds with $b_{2}^{+}=1$ and $c_{1}^{2}=2$, Invent. Math. 159 (2005), no. 3, 657-667.
\item[] [109] J. Pook, Homogeneous and locally homogeneous solutions to curvature flow, arXiv: 1202.1427.
\item[] [110] R. Răsdeaconu, The Kodaira dimension of diffeomorphic Kähler threefolds, Proc. Amer. Math. Soc. 134 (2006), no.12, 3543-3553.
\item[] [111] D. Ruberman, S. Strule,Mod 2 Seiberg-Witten invariants of homology tori, Math. Res. Lett. 7 (2000), 789-799.
\item[] [112] D. Salamon, Uniqueness of symplectic structures, Acta Math. Viet. 38, (2013), 123-144.
\item[] [113] P. Seidel, Lectures on four-dimensional Dehn twists, from: "Symplectic 4-manifolds and algebraic surfaces", (F Catanese, G Tian, editors), Lecture Notes in Math. 1938, Springer, Berlin (2008) 231-267
\item[] [114] I. Smith, Torus fibrations on symplectic four-manifolds, Turkish J. Math. 25 (2001), no. 1, 69-95.
\end{itemize}
[115] I. Smith, Lefschetz pencils and divisors in moduli space, Geom. Topol. 5 (2001), 579-608
[116] A. Stipsicz, Simply connected symplectic 4-manifolds with positive signature, In Proceedings of 6th Gökova Geometry-Topology Conference, volume 23, pages 145-150, 1999.
[117] A. Stipsicz, Simply connected 4-manifolds near the Bogomolov-Miyaoka-Yau line, Math. Res. Lett., 5(6):723-730, 1998.
[118] I. Suvaina, Yamabe invariant of a class of symplectic manifolds, arXiv:1410.1236.
[119] M. Symington, Symplectic rational blowdowns, J. Differ. Geom. 50, 505-518 (1998).
[120] C. H. Taubes, The Seiberg-Witten invariants and symplectic forms, Math. Research Letters, 1 (1994) 809-822.
[121] C. H. Taubes, $S W \Rightarrow G r$ : From the Seiberg-Witten equations to pseudoholomorphic curves, J. Amer. Math. Soc. 9(1996), 845-918
[122] C. H. Taubes, Counting pseudoholomorphic submanifolds in dimension 4, Jour. Diff. Geom. 44 (1996), 818-893.
[123] P. Surez-Serrato, R. Torres, A note on collapse, entropy, and vanishing of the Yamabe invariant of symplectic 4-manifolds, arXiv:1408.1586, to appear in JGP.
[124] K. Ueno, Classification theory of algebraic varieties and compact complex spaces, Notes written in collaboration with P. Cherenack. Lecture Notes in Mathematics, Vol. 439. Springer-Verlag, Berlin-New York, 1975. xix+278 pp.
[125] M. Usher, Minimality and symplectic sums, Int. Math. Res. Not. 2006, Art. ID 49857, 17 pp.
[126] M. Usher, Kodaira dimension and symplectic sums, To appear in Comment. Math. Helv.
[127] R. Walczak, Existence of symplectic structures on torus bundles over surfaces, Ann. Global Anal. Geom. 28 (2005), no. 3, 211-231.
[128] S. T. Yau, Calabi conjecture and some new results in algebraic geometry, PNAU, 74, 1977, 1789-1799
[129] W. Zhang, Geometric structures, Gromov norm and Kodaira dimensions, arXiv:1404.4231.

School of Mathematics, University of Minnesota, Minneapolis, MN 55455
E-mail address: tjli@math.umn.edu