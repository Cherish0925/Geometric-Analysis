---
retention_scope: session
part: 1
total_parts: 3
---

[Part 1/3 of: Examples of compact Einstein four-manifolds with negative curvature]

---
source_file: Examples_of_compact_Einstein_four-manifolds_with_negative_curvature_cbdfba5f6a45.pdf
converter: mathpix
format: mmd
---

\title{
Examples of compact Einstein four-manifolds with negative curvature
}

\author{
Joel Fine and Bruno Premoselli \\ Université libre de Bruxelles
}

\begin{abstract}
We give new examples of compact, negatively curved Einstein manifolds of dimension 4. These are seemingly the first such examples which are not locally homogeneous. Our metrics are carried by a sequence of 4 -manifolds $\left(X_{k}\right)$ previously considered by Gromov and Thurston [21]. The construction begins with a certain sequence $\left(M_{k}\right)$ of hyperbolic 4-manifolds, each containing a totally geodesic surface $\Sigma_{k}$ which is nullhomologous and whose normal injectivity radius tends to infinity with $k$. For a fixed choice of natural number $l$, we consider the $l$-fold cover $X_{k} \rightarrow M_{k}$ branched along $\Sigma_{k}$. We prove that for any choice of $l$ and all large enough $k$ (depending on $l$ ), $X_{k}$ carries an Einstein metric of negative sectional curvature. The first step in the proof is to find an approximate Einstein metric on $X_{k}$, which is done by interpolating between a model Einstein metric near the branch locus and the pull-back of the hyperbolic metric from $M_{k}$. The second step in the proof is to perturb this to a genuine solution to Einstein's equations, by a parameter dependent version of the inverse function theorem. The analysis relies on a delicate bootstrap procedure based on $L^{2}$ coercivity estimates.
\end{abstract}

\section*{Contents}
1 Introduction ..... 3
1.1 Compact Einstein manifolds with negative scalar curvature ..... 3
1.2 Statement of the results ..... 4
1.3 Brief outline of the proof ..... 6
1.4 Acknowledgements ..... 7
2 A spin version of Gromov-Thurston manifolds ..... 7
2.1 Gromov and Thurston's construction ..... 7
2.2 Murillo's volume estimate ..... 10
2.3 Proof of Proposition 1.1 ..... 12
3 The approximate solution ..... 13
3.1 The model Einstein metric ..... 14
3.2 The sequence of interpolated metrics ..... 17
4 The inverse function theorem ..... 19
4.1 The Bianchi gauge condition ..... 19
4.2 The linearisation is invertible ..... 21
4.3 Weighted Hölder spaces ..... 24
4.4 The proof assuming a key estimate ..... 26
5 Proving the key estimate ..... 29
5.1 Case 1 ..... 32
5.2 Case 2 ..... 38
5.3 Case 3 ..... 42
A Technical results on Green's operators ..... 48

\section*{1 Introduction}

\subsection*{1.1 Compact Einstein manifolds with negative scalar curvature}

A Riemannian manifold ( $M, g$ ) is called Einstein if $\operatorname{Ric}(g)=\lambda g$, for some $\lambda \in \mathbb{R}$. This article gives a new construction of compact Einstein 4-manifolds with $\lambda<0$. To put our result in context, we recall the other currently known methods for constructing compact Einstein manifolds with $\lambda<0$.
\begin{itemize}
\item[1.] Locally homogeneous Einstein manifolds. These are Einstein manifolds whose universal cover is homogeneous, i.e, acted on transitively by isometries. Negatively curved examples include hyperbolic and complex-hyperbolic manifolds.
\item[2.] Kähler-Einstein metrics. A compact Kähler manifold with $c_{1}<0$ carries a Kähler-Einstein metric with $\lambda<0$. This is due to Aubin 3 and Yau [37].
\item[3.] Dehn fillings of hyperbolic cusps. Given a finite volume hyperbolic $n$-manifold with cusps, one can produce a compact manifold by Dehn filling: each cusp is cut off at finite distance to produce a boundary component diffeomorphic to a torus $T^{n-1}$; this is then filled in by gluing $D^{2} \times T^{n-2}$ along their common $T^{n-1}$ boundary. The resulting manifold depends on the choice of identification of these two copies of $T^{n-1}$. For appropriate choices, the Dehn filling carries an Einstein metric with $\lambda<0$. When $n=3$ this is due to Thurston [35]. In this dimension the Einstein metric is in fact hyperbolic, putting us back in the locally homogeneous case described above. For $n \geq 4$, the Einstein metrics are no longer locally homogeneous. In these dimensions the original idea is due to Anderson [1] and was later refined by Bamler [5] (see also the excellent exposition of Biquard [9]).
\end{itemize}

Of these three constructions, only the first is known to produce Einstein metrics which are negatively curved, i.e., with all sectional curvatures negative.

Any manifold $X$ produced by Dehn filling admits no metrics of negative curvature, at least in dimension $n \geq 4$. This follows from Preissman's theorem: if $X$ is a compact, negatively curved Riemannian manifold then any non-trivial abelian subgroup of $\pi_{1}(X)$ is isomorphic to $\mathbb{Z}$. For a Dehn filling, the core $T^{n-2}$ of the filling is incompressible, giving an abelian subgroup of $\pi_{1}(X)$ isomorphic to $\mathbb{Z}^{n-2}$. We also remark that the Einstein metrics on Dehn fillings found in [1, 5] explicitly have some positive sectional curvatures.

The situation for Kähler-Einstein metrics is less clear. These metrics are found via an abstract existence theorem for solutions to a complex Monge-Ampère equation. Unfortunately, this result gives no direct way to describe the Einstein metrics and, in particular, to estimate the sectional curvatures. The only exception to this is when additional topological information implies that any Kähler-Einstein metric must actually be complex-hyperbolic and so locally homogeneous. This happens, for example, when a Kähler surface $X$ satisfies $c_{1}(X)^{2}=3 c_{2}(X)$ (as was noted by Yau [37]). Besides complex-hyperbolic manifolds, there are no other known examples of negatively curved Kähler-Einstein metrics.

Given this paucity of examples, it is of great interest to find new constructions of Einstein metrics and, in particular, examples with negative curvature which are not just locally homogeneous. It is this question we address in this article. We find infinitely many
compact 4-manifolds that carry negatively curved Einstein metrics, but that admit no locally homogeneous Einstein metrics.

The manifolds on which we find our new Einstein metrics were constructed by Gromov and Thurston [21] in 1987; we briefly describe these manifolds next.

\subsection*{1.2 Statement of the results}

In [21] Gromov and Thurston investigated pinching for negatively curved manifolds of dimension $n \geq 4$. They showed that for any $\epsilon>0$, there exists a compact Riemannian $n$-manifold ( $X, g$ ) with sectional curvatures pinched by $-1-\epsilon<\sec (h) \leq-1$ and yet $X$ does not admit a hyperbolic metric. Note that the positively curved analogue of this statement is false: any compact Riemannian manifold with sectional curvatures pinched by $1<\sec \leq 4$ is necessarily a quotient of the sphere [6, 28, 11].

A natural question, which motivated this work, is do Gromov and Thurston's manifolds carry Einstein metrics? We answer this question positively, at least in dimension 4. In order to state our main result we first construct a particular family of hyperbolic manifolds which belong to the class investigated in [21]. The output of our construction is summarised in the following proposition.

Proposition 1.1. For each $n \in \mathbb{N}$, there exists a sequence $\left(M_{k}\right)$ of compact hyperbolic $n$-manifolds with the following properties.
\begin{itemize}
\item[1.] The injectivity radius $i\left(M_{k}\right)$ satisfies $i\left(M_{k}\right) \rightarrow \infty$ as $k \rightarrow \infty$.
\item[2.] For each $k$, there is a nullhomologous totally-geodesic codimension-2 submanifold $\Sigma_{k} \subset M_{k}$. Moreover, the normal injectivity radius of $\Sigma_{k}$ satisfies $i\left(\Sigma_{k}, M_{k}\right) \geq$ $\frac{1}{2} i\left(M_{k}\right)$.
\item[3.] There is a constant $C$, independent of $k$ such that for all sufficiently large $k$, the volume of $\Sigma_{k}$ with respect to the hyperbolic metric satisfies
$$\operatorname{vol}\left(\Sigma_{k}\right) \leq C \exp \left(\frac{n^{2}-3 n+6}{4} i\left(M_{k}\right)\right)$$
\end{itemize}

We will see that there are infinitely many such sequences $\left(M_{k}\right)$. Gromov and Thurston's original construction was based on sequences $\left(M_{k}\right)$ satisfying the first two properties here. The details are explained in §2.

Since $\left[\Sigma_{k}\right]=0$, given any fixed integer $l \geq 2$, there is a cyclic $l$-fold cover $X_{k} \rightarrow M_{k}$ branched along $\Sigma_{k}$. One way to see this is to take a hypersurface $H_{k}$ bounding $\Sigma_{k}$, cut $M_{k}$ along $H_{k}$ to produce a manifold-with-boundary $M_{k}^{\prime}$; now take $l$ copies of $M_{k}^{\prime}$ and glue their boundaries appropriately. It is important to note that for a ramified cover constructed this way, the local ramification degree is $l$ at every ramification point. We also point out that $\Sigma_{k}$ may have many connected components.

The pull-back of the hyperbolic metric from $M_{k}$ to $X_{k}$ is singular along the branch locus, with cone angle $2 \pi l$. The main result of this article is that, in dimension 4 at least, the manifolds produced do indeed carry smooth Einstein metrics:

Theorem 1.2. Fix $l \geq 2$ and let $\left(M_{k}\right)$ denote a sequence of compact hyperbolic 4-manifolds satisfying the conclusions of Proposition 1.1. Let $X_{k}$ be the cyclic l-fold cover of $M_{k}$ branched along $\Sigma_{k}$. For all sufficiently large $k$ (depending on $l$ ), $X_{k}$ carries an Einstein metric of negative sectional curvature which is not locally homogeneous.

We remark that actually the manifolds $X_{k}$ carry no locally homogenous Einstein metrics whatsoever. In dimension 4, the only possible locally homogenous Einstein metrics on a compact manifold with infinite fundamental group are flat, hyperbolic and complexhyperbolic [25]. In our particular situation it is relatively straightforward to rule out these possibilities. First, the Remark 3.6 of Gromov-Thurston's article [21] explains that the branched covers $X_{k}$ never admit hyperbolic metrics. To rule out complex-hyperbolic metrics note first that the signature of $X_{k}$ is zero. (This follows from the fact that $\left[\Sigma_{k}\right]=0$; see, e.g., equation (15) in the article [24] of Hirzebruch.) From this, Hirzebruch's signature theorem and Chern-Weil it follows that any anti-self-dual metric on $X_{k}$ is automatically conformally flat. Since complex-hyperbolic metrics are anti-self-dual but not conformally flat, they are excluded. Finally, the manifolds $X_{k}$ admit a negatively curved metric (constructed in §3) and so, by Bieberbach's and Preissman's theorems, they cannot admit flat metrics.

Theorem 1.2, together with deep 4-dimensional rigidity results for Einstein metrics on compact manifolds, gives another way to see the manifolds $X_{k}$ do not admit negatively curved locally homogeneous Einstein metrics at all. Indeed, if a compact 4-manifold is either hyperbolic or complex-hyperbolic then the locally homogeneous metric is the only possible Einstein metric (up to overall scale). This was proved in the hyperbolic case by Besson, Courtois and Gallot [8], whilst the complex-hyperbolic case is due to LeBrun 30.

An important feature of our construction is that it is the first occurrence, in the compact case, of a negatively curved Einstein metric which is not locally homogeneous. Noncompact examples are relatively easy to find. There is an infinite dimensional family of Einstein deformations of the hyperbolic metric, found by Graham and Lee [20]; when the deformation is small enough, the curvature remains negative. In 4 dimensions, a 1parameter family of such deformations with an explicit formula was given by Pedersen [33]. It was recently observed by Cortés and Saha [14] that Pedersen's metrics are also negatively curved, even when far from the hyperbolic metric. Other explicit examples can also be found in [14].

As an aside, we mention that our examples also satisfy another curvature inequality, namely that $W^{+}+\frac{R}{12}<0$ (i.e., it is a negative definite endomorphism of the bundle $\Lambda^{+}$of self-dual 2-forms). Again, the only other known compact Einstein examples are hyperbolic and complex-hyperbolic. This inequality means that the twistor space carries a natural symplectic structure [19]. It is also central to an alternative gauge-theoretic description of Einstein 4-manifolds [18]. There is an action functional defined on the space of all definite connections over a 4-manifold, whose critical points are precisely Levi-Civita connections for Einstein metrics (this is described in detail in [18]). The Einstein metrics which arise this way are those for which $W^{+}+\frac{R}{12}$ is a definite endomorphism of $\Lambda^{+}$. The examples provided here show that this alternative formulation of Einstein metrics covers more than just locally homogeneous metrics.

\subsection*{1.3 Brief outline of the proof}

The proof of Theorem 1.2 has two steps. The first, carried out in §3, is similar in spirit to that of the tightly pinched Gromov-Thurston metrics. We smooth out the pull-back of the hyperbolic metric from $M_{k}$ to $X_{k}$ to find a metric which is approximately Einstein. The larger the injectivity radius, the better we can make the approximation. It is important to note, however, that our approximate Einstein metrics are not the same as the tightly pinched metrics that Gromov and Thurston consider. Inside the normal injectivity radius we use a fixed model Einstein metric whose sectional curvatures satisfy sec $\leq-c$ for some constant $0<c<1$ which depends only on $l$ (and not on $k$ ). The least negative sectional curvatures, $\mathrm{sec}=-c$, are attained at points on the branch locus. At large distances from the branch locus, the model is asymptotic to the pull-back of the hyperbolic metric. We interpolate between these two metrics at a distance which tends to infinity with $k$. This gives a metric $g_{k}$ on $X_{k}$ which is Einstein everywhere except for an annular region of large radius and fixed width in the tubular neighbourhood around each connected component of the branch locus. In these annular regions $g_{k}$ is close to Einstein, with error that tends to zero as $k$ tends to infinity.

The second step of the proof is to use the inverse function theorem to prove that for all large $k$, the approximately Einstein metric $g_{k}$ can be perturbed to give a nearby genuine Einstein metric. This new Einstein metric has sectional curvatures which are very close to those of $g_{k}$ and so, in particular, are also negative. The analysis involved turns out to be quite delicate. The fact that $g_{k}$ has negative sectional curvatures leads to the fact that the linearised Einstein equations (in Bianchi gauge) are invertible, with $L^{2}$-control. However, the volume and diameter of $X_{k}$ are rapidly increasing with $k$ and so weighted Hölder spaces, rather than Sobolev spaces, are seemingly the appropriate choice of Banach spaces in which to apply the inverse function theorem. Even with these spaces, however, we are unable to obtain control over the derivative in every direction. We circumvent this as follows. Since the metric $g_{k}$ is made by interpolating two Einstein metrics, the error is supported in a subset $S_{k} \subset X_{k}$. We can control the inverse of the derivative when it acts on sections supported in $S_{k}$. This, together with a careful application of the inverse function theorem, is enough to conclude

We set the problem up in §4 and reduce it to the key estimate, giving control on the inverse of the linearised Einstein equations on sections supported in $S_{k}$. We prove this estimate in §5. Starting from the uniform $L^{2}$ control given by the linearised Einstein equations we perform an involved bootstrap procedure and transform it into a weighted Hölder control. This relies on Carleman-type estimates for the Green's operator of the linearised equations and on a precise control of the volume of the branch locus $\Sigma_{k}$ provided by (1.1).

We close this brief outline with a comment on dimension. The model Einstein metric exists in all dimensions $n \geq 4$ and gives approximately Einstein metrics on Gromov-Thurston manifolds for all $n \geq 4$. Unfortunately, the control of the volume of the branch locus provided by Proposition 1.1 is only sufficient for our analytic arguments to work in dimension four. It would be very interesting to know if our approach could be improved so as to work in all dimensions.

\subsection*{1.4 Acknowledgements}

JF would like to thank Dmitri Panov for introducing him to Gromov and Thurston's work and for many discussions on it and related topics. BP would like to thank Richard Griffon for sharing important insights concerning §2. JF was supported by ERC consolidator grant 646649 "SymplecticEinstein". JF and BP were both supported by the FNRS grant MIS F.4522.15. BP was also the recipient of an FNRS chargé de recherche fellowship whilst this article was being written. Part of this research was carried out whilst JF was a visitor at MSRI and he thanks both them and the NSF (grant number DMS-1440140).

Finally, the authors would like to thank the anonymous referees for their careful reading of the paper and for their comments which greatly helped improve the exposition.

\section*{2 A spin version of Gromov-Thurston manifolds}

In this section we prove Proposition 1.1. In fact we will find infinitely many sequences $\left(M_{k}\right)$ of compact hyperbolic $n$-manifolds satisfying the conclusions of Proposition 1.1. As is mentioned in the introduction, the sequence $\left(X_{k}\right)$ is then found by taking the $l$-fold cover $X_{k} \rightarrow M_{k}$ branched along $\Sigma_{k}$ (for some fixed choice of $l$ ).

The original construction of Gromov and Thurston uses arithmetic hyperbolic geometry to produce $\left(M_{k}\right)$ satisfying the first two properties of Proposition 1.1. We review this in the next subsection. To bound the volume of $\Sigma_{k}$ we will make use of recent work of Murillo [32], which does not apply to all the sequences arising from Gromov-Thurston's original construction, but instead to a special subclass of them. Put loosely, we need the manifolds $M_{k}$ to be spin. We describe how to arrange this in section 2.2. Section 2.3 then gives the proof of Proposition 1.1.

\subsection*{2.1 Gromov and Thurston's construction}

Following Gromov-Thurston [21], consider the following quadratic form on $\mathbb{R}^{n+1}$ :
$$f\left(x_{0}, \ldots, x_{n}\right)=-\sqrt{2} x_{0}^{2}+x_{1}^{2}+\cdots+x_{n}^{2}$$
The corresponding pseudo-Riemannian metric on $\mathbb{R}^{n+1}$ restricts to a genuine Riemannian metric on the hyperboloid $H=\left\{x: f(x)=-1, x_{0}>0\right\}$. This makes $H$ isometric to hyperbolic space $\mathbb{H}^{n}$ and gives an identification between the group $\operatorname{SO}\left(\mathbb{R}^{n+1}, f\right)$ of orientation-preserving isometries of $\left(\mathbb{R}^{n+1}, f\right)$ which are isotopic to the identity, and the group of orientation preserving isometries of $\mathbb{H}^{n}$.

We write $\Gamma$ for those automorphisms of $f$ which are defined over the ring of integers $\mathbb{Z}[\sqrt{2}]$. Explicitly,
$$\Gamma=\mathrm{SO}\left(\mathbb{R}^{n+1}, f\right) \cap \mathrm{GL}(\mathbb{Z}[\sqrt{2}], n+1)$$
It is important that the action of $\Gamma$ on $\mathbb{H}^{n}$ is discrete and cocompact. (This is a classical result in the study of arithmetic hyperbolic manifolds; the use of $\sqrt{2}$ is precisely to ensure the action is cocompact.) The quotient $\mathbb{H}^{n} / \Gamma$ is a compact hyperbolic orbifold with singularities corresponding to the fixed points of $\Gamma$.

We now explain how to pass to finite covers to remove the orbifold singularities and increase the injectivity radius. This is a standard technique in hyperbolic geometry, but
since the proof is short and simple, and the conclusion so important to the rest of the article, we give the details for the benefit of non-experts.

Let $\Gamma^{\prime} \leq \Gamma$ be a finite-index subgroup. Write $i\left(\Gamma^{\prime}\right)$ for one-half of the minimal displacement of elements of $\Gamma^{\prime}$ :
$$i\left(\Gamma^{\prime}\right)=\frac{1}{2} \min \left\{d(\gamma x, x): x \in \mathbb{H}^{n}, \gamma \in \Gamma^{\prime}, \gamma \neq 1\right\}$$
The point is that when $i\left(\Gamma^{\prime}\right)>0$, the action of $\Gamma^{\prime}$ on $\mathbb{H}^{n}$ is fixed-point free and so the quotient $\mathbb{H}^{n} / \Gamma^{\prime}$ is smooth (and still compact, because $\Gamma^{\prime}$ has finite index in $\Gamma$ ). In this case, the injectivity radius of $\mathbb{H}^{n} / \Gamma^{\prime}$ is one-half the length of the shortest closed geodesic, which is exactly this quantity $i\left(\Gamma^{\prime}\right)$.

We will find a sequence $\left(\Gamma_{k}\right)$ of finite-index subgroups for which $i\left(\Gamma_{k}\right) \rightarrow \infty$. The key is the following simple lemma. Let $d \geq 0$ and set
$$\hat{F}_{d}=\left\{\gamma \in \Gamma, \gamma \neq 1: \exists x \in \mathbb{H}^{n} \text { with } d(\gamma x, x) \leq d\right\}$$
$\Gamma$ acts on $\hat{F}_{d}$ by conjugation and we write $F_{d}$ for the quotient.
Lemma 2.1. For any $d \geq 0$, the set $F_{d}$ is finite
Proof. Suppose for a contradiction that $F_{d}$ is not finite. Let $\left[\gamma_{i}\right] \in F_{d}$ be an infinite sequence and $x_{i} \in \mathbb{H}^{n}$ such that $d\left(\gamma_{i} x_{i}, x_{i}\right) \leq d$. Since $\Gamma$ is cocompact, by acting by conjugation we can assume that the $x_{i}$ all lie in a compact set. So a subsequence, which we continue to denote by $x_{i}$, converges to a point $x$. Then by the triangle inequality and for sufficiently large $i$,
$$d\left(\gamma_{i} x, x\right) \leq d\left(\gamma_{i} x, \gamma_{i} x_{i}\right)+d\left(\gamma_{i} x_{i}, x_{i}\right)+d\left(x_{i}, x\right)=d\left(\gamma_{i} x_{i}, x_{i}\right)+2 d\left(x_{i}, x\right) \leq d+1$$
This means that the points $\gamma_{i} x$ lie in a compact set and so either the stabiliser of $x$ is infinite or the orbit of $x$ has an accumulation point, contradicting that the action of $\Gamma$ is discrete. \(\square\)

Given $k \in \mathbb{N}$, write $\Gamma_{k} \leq \Gamma$ for the kernel of the homomorphism given by reducing the entries $\bmod k$, i.e., the homomorphism
$$\Gamma \hookrightarrow \mathrm{GL}(\mathbb{Z}[\sqrt{2}], n+1) \rightarrow \mathrm{GL}((\mathbb{Z} / k \mathbb{Z})[\sqrt{2}], n+1)$$
induced by $\mathbb{Z} \rightarrow \mathbb{Z} / k \mathbb{Z}$. The kernel $\Gamma_{k}$ is a finite-index normal subgroup. Fix $d>0$. Since $F_{d}$ is finite, for any $k$ sufficiently large, $\Gamma_{k}$ contains none of the corresponding conjugacy classes. It follows that $N_{k}=\mathbb{H}^{n} / \Gamma_{k}$ is a compact hyperbolic manifold with injectivity radius at least $d$. This gives a sequence of compact hyperbolic manifolds $\left(N_{k}\right)$ with $i\left(N_{k}\right) \rightarrow$ $\infty$.

The next step is to find the totally geodesic codimension 2 submanifolds. To do this, we may need to pass to a finite cover $M_{k} \rightarrow N_{k}$. The argument goes as follows. Denote by $s$ the reflection of $\mathbb{H}^{n}$ in the $x_{1}$ coordinate and by $r$ the rotation of $\mathbb{H}^{n}$ by $\pi / 2$ in the $\left(x_{1}, x_{2}\right)$-plane. Explicitly,
$$\begin{aligned}
& s\left(x_{0}, \ldots, x_{n}\right)=\left(x_{0},-x_{1},, x_{2}, x_{3}, \ldots, x_{n}\right) \\
& r\left(x_{0}, \ldots, x_{n}\right)=\left(x_{0},-x_{2}, x_{1}, x_{3}, \ldots, x_{n}\right)
\end{aligned}$$

It is simple to check that for any $k \in \mathbb{N}$, we have $s \Gamma_{k} s^{-1}=\Gamma_{k}$ and $r \Gamma_{k} r^{-1}=\Gamma_{k}$. It follows that $s$ and $r$ descend to the compact manifolds $N_{k}$ where they generate an isometric action of the dihedral group $D_{4}$. (For generalisations of the construction to include higher order dihedral groups, as well as further properties of Gromov-Thurston manifolds, we refer to [26].)

Write $H_{k} \subset N_{k}$ for the fixed locus of $s: N_{k} \rightarrow N_{k}$. It is a totally geodesic hypersurface. Note that $H_{k}$ may be disconnected and may have non-orientable components. We will first pass to a cover in which the preimage of $H_{k}$ is separating.

Definition 2.2. We say that a hypersurface $H \subset N$ separates a manifold $N$ if its complement can be written as the disjoint union of two non-empty open sets $N \backslash H=U \cup V$ with $H=\bar{U} \cap \bar{V}$. Notice that a separating hypersurface is necessarily co-orientable and so, when $N$ is also orientable, $H$ is necessarily orientable too.

Lemma 2.3. If a hypersurface $H \subset N$ does not separate $N$ then there is a non-trival double cover $M \rightarrow N$ in which the preimage of $H$ separates.

Proof. $H$ determines a class $[H] \in H_{n-1}\left(N, \mathbb{Z}_{2}\right)$ and hence a homomorphism
$$\rho: \pi_{1}(M) \rightarrow \mathbb{Z}_{2}$$
factoring through $H_{1}\left(N, \mathbb{Z}_{2}\right)$, which counts the parity of the number of intersections of a generic loop with $H$.

We first claim that $H$ separates if and only if $\rho$ is trivial. In one direction, if $H$ separates and $N \backslash H=U \cup V$ then by counting the number of times a loop enters $U$ say, one sees that every loop must cross $H$ an even number of times and so $\rho$ is trivial. Conversely, if $\rho$ is trivial, we can define a decomposition of $N \backslash H$ as follows. Pick a base-point $p \in N \backslash H$. Given $x \in N \backslash H$, join it to $p$ by a path $l$ which meets $H$ transversely. Define $f(p) \in \mathbb{Z}_{2}$ to be the parity of intersection of $l$ and $H$. Since $\rho$ is assumed to be trivial, the definition of $f$ doesn't depend on the choice of $l$; the result is a locally constant function and putting $U=f^{-1}(0)$, and $V=f^{-1}(1)$ gives the required decomposition.

So if $H$ doesn't separate, ker $\rho$ is an index 2 normal subgroup. Let $\pi: M \rightarrow N$ denote the corresponding double cover and $H^{\prime}$ the preimage of $H$. We now repeat the above discussion for $H^{\prime} \subset M$. The resulting homomorphism $\rho^{\prime}: \pi_{1}(M) \rightarrow \mathbb{Z}_{2}$ is given by $\rho \circ \pi_{*}$. Since $\operatorname{Im} \pi_{*}=\operatorname{ker} \rho$ it follows that $\rho^{\prime}$ is trivial and so $H^{\prime}$ separates as claimed. \(\square\)

We remark in passing that when $H$ does not separate, the new separating hypersurface $H^{\prime}$ definitely has different topology. Each oriented connected component of $H$ is replaced by two identical components in $H^{\prime}$, whilst each non-oriented connected component of $H$ is replaced by its oriented double cover in $H^{\prime}$. (One can see this by considering what happens to each component in a tubular neighbourhood.)

Returning to our discussion of Gromov and Thurston's construction, we will pass to a finte cover of $M_{k} \rightarrow N_{k}$ in which the preimage of $H_{k}$ separates and, moreover, to which the rotation $r$ lifts.

Lemma 2.4. For all $k$, there is a finite cover $\pi: M_{k} \rightarrow N_{k}$ for which the preimage $H_{k}^{\prime}=$ $\pi^{-1}\left(H_{k}\right)$ separates and to which the rotation $r$ lifts to a map $r: M_{k} \rightarrow M_{k}$.

Proof. Let $\rho_{k}: \pi_{1}\left(N_{k}\right) \rightarrow \mathbb{Z}_{2}$ denote the homomorphism in the proof of Lemma 2.3, which detects whether or not $H_{k}$ separates $N_{k}$. We must find a finite index subgroup of $\pi_{1}\left(N_{k}\right)$ which is both contained in $\mathrm{ker} \rho_{k}$ and is invariant under $r_{*}$ (the map induced on $\pi_{1}\left(N_{k}\right)$ by the map $r$ ). One checks that this holds for the following subgroup:
$$\Gamma_{k}^{\prime}=\operatorname{ker} \rho_{k} \cap r_{*}\left(\operatorname{ker} \rho_{k}\right) \cap r_{*}^{2}\left(\operatorname{ker} \rho_{k}\right) \cap r_{*}^{3}\left(\operatorname{ker} \rho_{k}\right)$$ \(\square\)

We can now describe the null-homologous totally geodesic codimension 2 submanifold $\Sigma_{k} \subset M_{k}$. Consider the hypersurface $H_{k}^{\prime}$ and its image $H_{k}^{\prime \prime}:=r\left(H_{k}^{\prime}\right)$ under the rotation. Put $S_{k}=H_{k}^{\prime} \cap H_{k}^{\prime \prime}$. To check that $H_{k}^{\prime}$ and $H_{k}^{\prime \prime}$ meet transversely it suffices to check the same is true for the preimages in $\mathbb{H}^{n}$ of each pair of intersecting components; this leads to a pair of distinct hyperplanes, meeting in a totally geodesic copy of $\mathbb{H}^{n-2}$, which projects down to the corresponding component of $S_{k}$. We know that $H_{k}^{\prime}$ separates $M_{k}$, it follows that $H_{k}^{\prime \prime}$ is also separating. In particular, both are orientable and hence $\Sigma_{k}$ is too. To see that $\Sigma_{k}$ is null-homologous, fix a decomposition $M_{k} \backslash H_{k}^{\prime}=U \cup V$ of $M_{k}$ and let $Z_{k}=H_{k}^{\prime \prime} \cap U$. Then $Z_{k}$ is an $(n-1)$-chain with boundary $\partial Z_{k}=\Sigma_{k}$.

Finally, we check the condition on the normal injectivity radius of $\Sigma_{k}$. Since $M_{k}$ is hyperbolic there are no conjugate points on geodesics. This means there is a path $\gamma$ in $M_{k}$ starting and ending on $S_{k}$, which it meets at right-angles and with $L(\gamma)=2 i\left(S_{k}, M_{k}\right)$. Acting on $\gamma$ by $r^{2}$ we find another such path which when joined to $\gamma$ gives a smooth geodesic loop of length $2 L(\gamma)$. But the length of any geodesic loop is at least $2 i\left(M_{k}\right)$ and so $i\left(S_{k}, M_{k}\right)=\frac{1}{2} L(\gamma) \geq \frac{1}{2} i\left(M_{k}\right)$ as claimed.

\subsection*{2.2 Murillo's volume estimate}

So far, we have followed Gromov and Thurston's construction precisely. We now turn to the volume bound, for which we need to modify the construction slightly.

The important new ingredient is a bound of the form
$$\operatorname{vol}\left(M_{k}\right) \leq A e^{C i\left(M_{k}\right)}$$
for constants $A$ and $C$ which are independent of $k$. It is not difficult to show that for the sequence $M_{k}$ constructed by Gromov and Thurston, such constants $A(n), C(n)$ exist, depending only on the dimension $n$. There is a short self-contained proof of this fact in §4.1 of [22]. However, for our purposes it is important to know the precise value of $C(n)$.

For the congruence coverings discussed here, Katz-Schaps-Vishne [27] proved that $C(2)=3 / 2$ and $C(3)=3$. (See also the related work [12] of Buser-Sarnack.) For us, of course, the interest is in $n \geq 4$. This was treated in a recent article by Murillo [32], which shows that, with a couple of caveats, the optimal inequality has
$$C(n)=\frac{n(n+1)}{4}$$
The first caveat is that Murillo's argument works for sequences of congruence subgroups starting with $\operatorname{Spin}\left(\mathbb{R}^{n+1}, f\right)$ rather than $\operatorname{SO}\left(\mathbb{R}^{n+1}, f\right)$. The second is that the congruences must be determined by prime ideals $I \leq \mathbb{Z}[\sqrt{2}]$ and not just reduction modulo an arbitrary integer.

We give a brief description of Murillo's theorem, following the original article closely (where the reader can also find detailed justifications for everything in this section). In order to keep the arithmetic to a minimum, we continue to work with the quadratic form $f$ which is defined over $\mathbb{Q}(\sqrt{2})$ but in fact everything holds much more generally, for admissible quadratic forms defined over totally real number fields. The interested reader can find the details neatly summarised in Murillo's article.

We first give the analogue of $\Gamma \subset \operatorname{SO}\left(\mathbb{R}^{n+1}, f\right)$, namely the subgroup $\bar{\Gamma} \leq \operatorname{Spin}\left(\mathbb{R}^{n+1}, f\right)$ of elements defined over the ring of integers $\mathbb{Z}[\sqrt{2}]$. To do so, we use the Clifford representation of $\operatorname{Spin}\left(\mathbb{R}^{n+1}, f\right)$. The group $\operatorname{Spin}\left(\mathbb{R}^{n+1}, f\right)$ is a subgroup of the Clifford algebra $\operatorname{Cliff}\left(\mathbb{R}^{n+1}, f\right)$ and so acts on it by left multiplication. To use this to get a matrix representation of $\operatorname{Spin}\left(\mathbb{R}^{n+1}, f\right)$ we fix a basis of $\operatorname{Cliff}\left(\mathbb{R}^{n+1}, f\right)$. Choose first a basis $e_{0}, \ldots, e_{n}$ of $\mathbb{R}^{n+1}$ with respect to which the innerproduct $g_{f}$ defined by $f$ is standard:
$$g_{f}\left(e_{i}, e_{j}\right)=\left\{\begin{aligned}
-1 & \text { if } i=j=0 \\
1 & \text { if } i=j>0 \\
0 & \text { if } i \neq j
\end{aligned}\right.$$
Then Cliff $\left(\mathbb{R}^{n+1}, f\right)$ has as basis the $2^{n+1}$ elements of the form $e_{i_{1}} \cdots e_{i_{r}}$ where $i_{1}<\cdots<i_{r}$ and $r=0, \ldots, n+1$. With respect to this basis, left multiplication by Spin on Cliff gives a faithful representation
$$\rho_{L}: \operatorname{Spin}\left(\mathbb{R}^{n+1}, f\right) \hookrightarrow \operatorname{GL}\left(\mathbb{R}, 2^{n+1}\right)$$
We now set $\bar{\Gamma} \subset \operatorname{Spin}\left(\mathbb{R}^{n+1}, f\right)$ to be
$$\bar{\Gamma}=\operatorname{Im} \rho_{L} \cap \operatorname{GL}\left(\mathbb{Z}[\sqrt{2}], 2^{n+1}\right)$$
$\bar{\Gamma}$ has an explicit description in terms of the above basis for $\operatorname{Cliff}\left(\mathbb{R}^{n+1}, f\right)$. Given $J=$ $\left(i_{1}, \ldots, i_{r}\right)$ we write $e_{J}=e_{i_{1}} \cdots e_{i_{r}}$ for the corresponding basis element of the Clifford algebra. Then
$$\bar{\Gamma}=\left\{\gamma=\sum_{|J| \text { even }} c_{J} e_{J} \in \operatorname{Spin}\left(\mathbb{R}^{n+1}, f\right): c_{J} \in \mathbb{Z}[\sqrt{2}] \text { for } J \neq \emptyset, c_{\emptyset}-1 \in \mathbb{Z}[\sqrt{2}]\right\}$$
$\bar{\Gamma}$ acts on $\mathbb{H}^{n}$ via
$$\bar{\Gamma} \hookrightarrow \operatorname{Spin}\left(\mathbb{R}^{n+1}, f\right) \rightarrow \operatorname{SO}\left(\mathbb{R}^{n+1}, f\right)$$
(where the second arrow is the standard double cover). The crucial fact is that the resulting action of $\bar{\Gamma}$ is discrete and cocompact and so $\mathbb{H}^{n} / \bar{\Gamma}$ is a compact hyperbolic orbifold. (Again this is a foundational fact in the study of arithmetic hyperbolic manifolds.)

We now pass to finite covers. Let $I \subset \mathbb{Z}[\sqrt{2}]$ denote an ideal. We obtain a normal subgroup $\Gamma_{I} \leq \bar{\Gamma}$ as the kernel of the homomorphism
$$\bar{\Gamma} \rightarrow \operatorname{GL}\left(\mathbb{Z}[\sqrt{2}] / I, 2^{n+1}\right)$$

Explicitly,
$$\Gamma_{I}=\left\{\gamma=\sum_{|J| \text { even }} c_{J} e_{J} \in \bar{\Gamma}: c_{J} \in I \text { for } J \neq \emptyset, c_{\emptyset}-1 \in I\right\}$$
We are now in a position to state Murillo's Theorem.
Theorem 2.5 (Murillo's volume bound [32]). Let $I_{k} \subset \mathbb{Z}[\sqrt{2}]$ be a sequence of prime ideals with $\left|\mathbb{Z}[\sqrt{2}] / I_{k}\right| \rightarrow \infty$ and write $\Gamma_{I_{k}} \leq \bar{\Gamma}$ for the corresponding normal subgroups of $\bar{\Gamma}$. Then for sufficiently large $k$, the quotient $M_{k}=\mathbb{H}^{n} / \Gamma_{I_{k}}$ is smooth and there is a constant $A$ such that for all $k$,
$$\operatorname{vol}\left(M_{k}\right) \leq A \exp \left(\frac{n(n+1)}{4} i\left(M_{k}\right)\right)$$

The key observation in Murillo's proof is to control the hyperbolic displacement of an element $\sigma \in \operatorname{Spin}\left(\mathbb{R}^{n+1}, f\right)$ by the size of the coefficient of $e_{\emptyset}$ in the expression $\sigma=\sum c_{J} e_{J}$ of $\sigma$ in terms of the chosen basis of $\operatorname{Cliff}\left(\mathbb{R}^{n+1}, f\right)$. From here he is able to control the minimal displacement $i\left(\Gamma_{I}\right)$ from below in terms of the cardinality of the quotient $\mathbb{Z}[\sqrt{2}] / I$. At the same time, the index $\left[\bar{\Gamma}: \Gamma_{I}\right]$ can be controlled from above in terms of this same quantity and, since volume is proportional to index, this leads to Theorem 2.5.

\subsection*{2.3 Proof of Proposition 1.1}

We now give the proof of Proposition 1.1. Let $I_{k} \subset \mathbb{Z}[\sqrt{2}]$ be a sequence of prime ideals as in Murillo's Theorem, let $\Gamma_{I_{k}} \subset \bar{\Gamma}$ and write $M_{k}=\mathbb{H}^{n} / \Gamma_{I_{k}}$ for the corresponding hyperbolic manifolds. We can for instance take $I_{k}=p_{k} \mathbb{Z}[\sqrt{2}]$ for a suitable increasing sequence of prime numbers $\left(p_{k}\right)$. Just as before, $i\left(M_{k}\right) \rightarrow \infty$ as $k \rightarrow \infty$.

To find the nullhomologous totally geodesic codimension 2 submanifold $\Sigma_{k} \subset M_{k}$ we copy the same argument. Recall that the natural action $\rho: \operatorname{Spin}\left(\mathbb{R}^{n+1}, f\right) \rightarrow \operatorname{SO}\left(\mathbb{R}^{n+1}, f\right)$ is given by $\rho(\sigma)(v)=\sigma v \sigma^{-1}$ where we treat $v \in \mathbb{R}^{n+1}$ as an element of the Clifford algebra, and the product on the righthand side of this formula is the Clifford product. We can also represent reflections in a similar way. Let $e_{0}, \ldots, e_{n}$ be a basis of $\mathbb{R}^{n+1}$ for which $f$ is standard and consider the linear transformation $\hat{s}$ of $\operatorname{Cliff}\left(\mathbb{R}^{n+1}, f\right)$ given by $\hat{s}(c)=e_{1} c e_{1}$. Note that for any multi-index $J$,
$$\hat{s}\left(e_{J}\right)= \begin{cases}-1^{|J|+1} e_{J} & \text { if } 1 \notin J \\ -1^{|J|} e_{J} & \text { if } 1 \in J\end{cases}$$
In particular, $\hat{s}$ preserves $\mathbb{R}^{n+1} \subset \operatorname{Cliff}\left(\mathbb{R}^{n+1}, f\right)$ where it acts as reflection in the hyperplane orthogonal to $e_{1}$. Moreover, from the description (2.1) of $\Gamma_{I_{k}}$, it follows that $\hat{s}\left(\Gamma_{I_{k}}\right)=\Gamma_{I_{k}}$. So $\hat{s}$ descends to an isometry $s$ of $M_{k}$. Similarly, there is a second reflection, this time in the hyperplane orthogonal to $e_{1}+e_{2}$, coming from the linear map of $\operatorname{Cliff}\left(\mathbb{R}^{n+1}, f\right)$ given by
$$\hat{s}^{\prime}: c \mapsto \frac{1}{2}\left(e_{1}+e_{2}\right) c\left(e_{1}+e_{2}\right)$$
Again, $\hat{s}^{\prime}\left(\Gamma_{I_{k}}\right)=\Gamma_{I_{k}}$ and so this descends to an isometry $s^{\prime}$ of $M_{k}$. The reflections $s, s^{\prime}$ generate an action of the dihedral group $D_{4}$; in particular we have a reflection $s$ and a
rotation $r=s s^{\prime}$ and we are in precisely the same situation discussed in Section 2.1. Write $H_{k}$ for the fixed locus of $s$; as before we can pass to a finite cover to which the rotation $r$ lifts and in which the preimage of $H_{k}$ separates. We abuse notation by also denoting this cover $M_{k}$. Just as in the original Gromov-Thurston construction, the intersection $H_{k} \cap r\left(H_{k}\right)=\Sigma_{k}$ is the totally geodesic null-homologous submanifold we are looking for and an identical argument as before shows that the normal injectivity radius satisfies $i\left(\Sigma_{k}, M_{k}\right) \geq \frac{1}{2} i\left(M_{k}\right)$.

It remains to prove the volume bound (1.1) on $\Sigma_{k}$. We control the volume of $\Sigma_{k}$ in two steps. Write $i\left(H_{k}, M_{k}\right)$ for the normal injectivity radius of $H_{k} \subset M_{k}$. By considering the volume of an embedded tubular neighbourhood of $H_{k}$ of maximal radius we have
$$\operatorname{vol}\left(H_{k}\right) e^{(n-1) i\left(H_{k}, M_{k}\right)} \leq A_{1} \operatorname{vol}\left(M_{k}\right)$$
where $A_{1}$ is independent of $k$. Similarly, by considering an embedded tubular neighbourhood of $\Sigma_{k}$ in $H_{k}$ of maximal radius, we find a constant $A_{2}$ such that
$$\operatorname{vol}\left(\Sigma_{k}\right) e^{(n-2) i\left(\Sigma_{k}, H_{k}\right)} \leq A_{2} \operatorname{vol}\left(H_{k}\right)$$
Now $i\left(\Sigma_{k}, H_{k}\right) \geq i\left(\Sigma_{k}, M_{k}\right) \geq \frac{1}{2} i\left(M_{k}\right)$ and, similarly, $i\left(H_{k}, M_{k}\right) \geq \frac{1}{2} i\left(M_{k}\right)$. Using this and putting (2.2) and (2.3) together we see that
$$\operatorname{vol}\left(\Sigma_{k}\right) \leq A_{1} A_{2} \operatorname{vol}\left(M_{k}\right) e^{\frac{3-2 n}{2} i\left(M_{k}\right)}$$
The bound 1.1 now follows from (2.4) and Theorem 2.5.

\section*{3 The approximate solution}

In this section we give the construction of the approximate solutions to Einstein's equations. Recall that in the previous section we constructed a sequence of hyperbolic $n$-manifolds $\left(M_{k}, h_{k}\right)$, each containing a totally geodesic hypersurface $H_{k} \subset M_{k}$ whose boundary $\Sigma_{k}$ is also totally geodesic. The injectivity radius $i\left(M_{k}\right)$ of $M_{k}$ tends to infinity with $k$ and $\frac{1}{2} i\left(M_{k}\right)$ is a lower bound for the normal injectivity radius of $\Sigma_{k} \subset M_{k}$. We denote by $p: X_{k} \rightarrow M_{k}$ the cyclic $l$-fold cover branched along $\Sigma_{k}$. We abuse notation by using $\Sigma_{k}$ to also denote the branch locus in $X_{k}$.

Define a function $r: X_{k} \rightarrow \mathbb{R}$ by setting $r(x)$ to be the distance of $p(x) \in M_{k}$ from the branch locus $\Sigma_{k}$. As a notational convenience, we set $u=\cosh (r)$. Write $U_{k, \text { max }}=$ $\cosh \left(\frac{1}{2} i\left(M_{k}\right)\right)$ and pick a sequence $\left(U_{k}\right)$ which tends to infinity, with $U_{k}<\frac{1}{2} U_{k, \text { max }}$. The main result of this section is the following.

Proposition 3.1. For each $k$, there is a smooth Riemannian metric $g_{k}$ on $X_{k}$ with the following properties:
\begin{itemize}
\item[1.] For any $m \in \mathbb{N}$ and $0 \leq \eta<1$, there is a constant $A$ such that for all $k$,
$$\left\|\operatorname{Ric}\left(g_{k}\right)+(n-1) g_{k}\right\|_{C^{m, n}} \leq A U_{k}^{1-n}$$
\item[2.] There is a constant $c>0$ such that for all $k, \sec \left(g_{k}\right) \leq-c$.
\end{itemize}
\begin{itemize}
\item[3.] $\operatorname{Ric}\left(g_{k}\right)+(n-1) g_{k}$ is supported in the region $\frac{1}{2} U_{k}<u<U_{k}$.
\item[4.] For any $m \in \mathbb{N}$, there exists a constant $C$ such that for all $k,\left\|\operatorname{Rm}\left(g_{k}\right)\right\|_{C^{m}} \leq C$.
\end{itemize}

The metric $g_{k}$ will be given by interpolating in the region $\frac{1}{2} U_{k}<u<U_{k}$ between a model Einstein metric defined on a tubular neighbourhood of $\Sigma_{k} \subset X_{k}$ and the hyperbolic metric $p^{*} h_{k}$ pulled back via the branched cover $p: X_{k} \rightarrow\left(M_{k}, h_{k}\right)$ on the complement of this tubular neighbourhood. In Proposition 3.1 the Hölder norms are defined with respect to the metric $g_{k}$ (see definition 4.5 for the explicit definition used in this paper for the Hölder norms). We begin by describing the model.

\subsection*{3.1 The model Einstein metric}

Write $\left(\mathbb{H}^{n}, h\right)$ for hyperbolic space of dimension $n$. Denote by $S \subset \mathbb{H}^{n}$ a totally geodesic copy of $\mathbb{H}^{n-2}$. We can write $h$ as
$$h=\mathrm{d} r^{2}+\sinh ^{2}(r) \mathrm{d} \theta^{2}+\cosh ^{2}(r) h_{S}$$
where $h_{S}$ is the hyperbolic metric on $S$. Here, $(r, \theta) \in(0, \infty) \times S^{1}$ are polar coordinates on the totally geodesic copies of $\mathbb{H}^{2}$ which are orthogonal to $S$. The hypersurfaces given by setting $\theta$ constant are the totally geodesic copies of $\mathbb{H}^{n-1}$ containing $S$. In fact, it will be more convenient to use the coordinate $u=\cosh (r)$; the hyperbolic metric then becomes
$$h=\frac{\mathrm{d} u^{2}}{u^{2}-1}+\left(u^{2}-1\right) \mathrm{d} \theta^{2}+u^{2} h_{S}$$
This expression is valid for $(u, \theta) \in(1, \infty) \times S^{1}$.
We will consider a family $g_{a}$ of Einstein metrics depending on a parameter $a \in \mathbb{R}$. When $a=0$, we recover $h$, whilst for $a \neq 0$ the metric has a cone singularity along $S$, with cone angle varying with $a$. By an appropriate choice of $a$, the metric will have the correct cone angle to become smooth when pulled back by an $l$-fold cover ramified along $S$.

The metrics we will consider all have the form
$$g=\frac{\mathrm{d} u^{2}}{V(u)}+V(u) \mathrm{d} \theta^{2}+u^{2} h_{S}$$
where $V$ is a smooth positive function.
Proposition 3.2. The metric (3.2) solves $\operatorname{Ric}(g)=-(n-1) g$ precisely when
$$V(u)=u^{2}-1+\frac{a}{u^{n-3}}$$
for some $a \in \mathbb{R}$.
Proof. The proof of this is a direct and standard calculation, but we give the details since certain parts (notably the description of the Levi-Civita connection and curvatures) will be useful later. We use the convention that our indices $i, j$ run between $1, \ldots, n-2$. Let $f^{i}$ be an orthonormal coframe for $\left(S, h_{S}\right)$, and write $\omega_{j}^{i}$ for the connection matrix of the Levi-Civita connection of $h_{S}$, i.e, $\nabla^{h_{S}} f^{i}=\omega_{j}^{i} \otimes f^{j}$. Let $W^{2}=V$, then
$$e^{i}=u f^{i}, \quad e^{n-1}=W^{-1} \mathrm{~d} u, \quad e^{n}=W \mathrm{~d} \theta$$
is an orthonormal coframe for $g$. We have the following formulae for the exterior derivatives:
$$\begin{aligned}
\mathrm{d} e^{i} & =\omega_{j}^{i} \wedge e_{j}-\frac{W}{u} e^{i} \wedge e^{n-1} \\
\mathrm{~d} e^{n-1} & =0 \\
\mathrm{~d} e^{n} & =W^{\prime} e^{n-1} \wedge e^{n}
\end{aligned}$$
From here we can write down the connection matrix, $A$, for the Levi-Civita connection of $g$. To ease notation, we write e for the column vector with entries $e_{1}, \ldots, e_{n-2}$.
$$\left(\begin{array}{l}
\nabla \mathbf{e} \\
\nabla e^{n-1} \\
\nabla e^{n}
\end{array}\right)=\left(\begin{array}{ccc}
\omega & -\frac{W}{u} \mathbf{e} & 0 \\
\frac{W}{u} \mathbf{e}^{t} & 0 & W^{\prime} e^{n} \\
0 & -W^{\prime} e^{n} & 0
\end{array}\right) \otimes\left(\begin{array}{l}
\mathbf{e} \\
e^{n-1} \\
e^{n}
\end{array}\right)$$
Next we compute the curvature matrix, $\Omega=\mathrm{d} A-A \wedge A$ :
$$\begin{aligned}
\Omega_{i j} & =(\mathrm{d} \omega-\omega \wedge \omega)_{i j}+\frac{W^{2}}{u^{2}} e^{i} \wedge e^{j} \\
\Omega_{i, n-1} & =\frac{W^{\prime} W}{u} e^{i} \wedge e^{n-1} \\
\Omega_{i, n} & =\frac{W^{\prime} W}{u} e^{i} \wedge e^{n} \\
\Omega_{n-1, n} & =\left(W^{\prime \prime} W+\left(W^{\prime}\right)^{2}\right) e^{n-1} \wedge e^{n}
\end{aligned}$$
From here we can read off the components of the curvature tensor, $R_{a b c d}=-\left\langle\Omega_{a b}, e^{c} \wedge e^{d}\right\rangle$. We use the convention that a Roman index takes the values $1, \ldots, n-2$, whilst a Greek index takes the values $n-1, n$. Since $\left(S, h_{S}\right)$ is hyperbolic, the non-zero components are:
$$\begin{aligned}
R_{i j k l} & =-\frac{1+W^{2}}{u^{2}}\left(\delta_{i k} \delta_{j l}-\delta_{i l} \delta_{j k}\right) \\
R_{i \mu i \mu} & =-\frac{W^{\prime} W}{u} \\
R_{\mu \nu \mu \nu} & =-\left(W^{\prime \prime} W+\left(W^{\prime}\right)^{2}\right)
\end{aligned}$$
whilst the remaining components are zero:
$$\begin{aligned}
R_{i \mu \nu \rho} & =0 \\
R_{i j \mu \nu} & =0 \\
R_{i \mu j \nu} & =0 \text { unless } i=j \text { and } \mu=\nu \\
R_{i j k \mu} & =0 \\
R_{\mu \nu \rho \sigma} & =0 \text { unless } \mu=\rho \text { and } \nu=\sigma
\end{aligned}$$
(One can also use symmetry arguments to show these components vanish. For example, for any point $p$ there is an isometry given by an inversion in $S$ which fixes $p$, reverses the $e^{i}$ and leaves the $e^{\mu}$ unchanged. It follows that any component with an odd number of Roman indices must vanish.)

From here we can compute the Ricci curvature, which is diagonal:
$$\begin{aligned}
R_{i j} & =\left[(3-n) \frac{1+W^{2}}{u^{2}}-\frac{2 W^{\prime} W}{u}\right] \delta_{i j} \\
R_{\mu \nu} & =\left[(2-n) \frac{W^{\prime} W}{u}-\left(W^{\prime \prime} W+\left(W^{\prime}\right)^{2}\right)\right] \delta_{\mu \nu} \\
R_{i \mu} & =0
\end{aligned}$$
To find an Einstein metric with Ric $=-(n-1) g$, it suffices to solve
$$(3-n)\left(1+W^{2}\right)-2 W^{\prime} W u=-(n-1) u^{2}$$
because this sets $R_{i i}=-(n-1)$ and then differentiating (3.8) with respect to $u$ we also get that $R_{\mu \mu}=-(n-1)$. Equation (3.8) rearranges to give
$$V^{\prime}+\frac{n-3}{u} V=(n-1) u-(n-3) u^{-1}$$
and a simple integrating factor shows that the solutions of this equation are
$$V(u)=u^{2}-1+\frac{a}{u^{n-3}}$$
(where $a \in \mathbb{R}$ ) as claimed. \(\square\)

When $V$ is given by (3.3), we denote the metric (3.2) by $g_{a}$. We next consider the singularity of the metric $g_{a}$. The metric is smooth for those values of $u$ for which $0<$ $V(u)<\infty$. Write $u_{a}$ for the largest root of $V$. At least when $u_{a}>0$, the metric $g_{a}$ is defined for $u \in\left(u_{a}, \infty\right)$. The metric $g_{a}$ has a cone singularity at $u=u_{a}$. The next lemma describes how the cone angle depends on $a$.

Lemma 3.3. Let
$$v=\sqrt{\frac{n-3}{n-1}}, \quad a_{\max }=\frac{2}{n-1} v^{n-3}$$
\begin{itemize}
\item[1.] We have $u_{a}>0$ if and only if $a \in\left(-\infty, a_{\max }\right]$. The map $a \mapsto u_{a}$ is a decreasing homeomorphism $\left(-\infty, a_{\max }\right] \rightarrow[v, \infty)$.
\item[2.] When $a \in\left(-\infty, a_{\text {max }}\right)$, the metric $g_{a}$ has a cone singularity along $S$ at $u=u_{a}$, with cone angle $2 \pi c_{a} \in(0, \infty)$.
\item[3.] The map $a \mapsto c_{a}$ is a decreasing homeomorphism $\left(-\infty, a_{\max }\right] \rightarrow[0, \infty)$. In particular, as a runs from 0 to $a_{\text {max }}$, the cone angle takes every value from $2 \pi$ to 0 precisely once.
\end{itemize}
Proof. The number $u_{a}$ is the largest solution of $f(u)=a$ where $f(u)=\left(1-u^{2}\right) u^{n-3}$, so the first assertion follows from a sketch of the graph of $f$. We now turn to the second assertion. For $u$ near to $u_{a}$ we have
$$V(u)=2 c_{a}\left(u-u_{a}\right)+O\left(\left(u-u_{a}\right)^{2}\right)$$
where $c_{a}=\frac{1}{2} V^{\prime}\left(u_{a}\right)$. The substitution $s=\sqrt{\frac{2}{c_{a}}\left(u-u_{a}\right)}$ shows that for $s \sim 0$, the metric becomes
$$g_{a} \sim \mathrm{~d} s^{2}+c_{a}^{2} s^{2} \mathrm{~d} \theta^{2}+\left(w+u_{a}\right)^{2} h_{V}$$
Therefore the metric has a conical singularity at $s=0$, i.e., at $u=u_{a}$, with a cone angle of $2 \pi c_{a}$. Finally, $V^{\prime}(u)=2 u+(3-n) a u^{2-n}$ so
$$\begin{aligned}
2 c_{a} & =2 u_{a}+(3-n) a u_{a}^{2-n} \\
& =(n-1) u_{a}+(3-n) u_{a}^{-1}
\end{aligned}$$
where in the second line we have used that $f\left(u_{a}\right)=0$. By the first assertion we deduce that $a \mapsto c_{a}$ is a homeomorphism $\left(-\infty, a_{\text {max }}\right] \rightarrow[0, \infty)$. Finally, $c_{0}=1$ and so as $a$ runs from 0 to $a_{\text {max }}$ the cone angle varies from $2 \pi$ to 0 exactly as claimed. \(\square\)

We now prove that the sectional curvatures of $g_{k}$ are all negative:
Lemma 3.4. For $a \in\left(0, a_{\text {max }}\right)$, the metric $g_{a}$ is negatively curved, with all sectional curvatures satisfying
$$\sec \leq-1+\frac{n-3}{2} a u_{a}^{1-n}<0$$
Proof. In the proof of Proposition 3.2, we computed the curvature tensor of $g_{a}$. The only non-zero components are:
$$\begin{aligned}
R_{i j k l} & =-\left(1+a u^{1-n}\right)\left(\delta_{i k} \delta_{j l}-\delta_{i l} \delta_{j k}\right) \\
R_{\mu \nu \rho \sigma} & =-\left(1+\frac{(n-3)(n-2)}{2} a u^{1-n}\right)\left(\delta_{\mu \rho} \delta_{\nu \sigma}-\delta_{\mu \sigma} \delta_{\nu \rho}\right) \\
R_{i \mu i \mu} & =-1+\frac{n-3}{2} a u^{1-n}
\end{aligned}$$
From this, the vanishing of the other components of the curvature, and the fact that $a>0$ it follows that the largest sectional curvatures are
$$R_{i \mu i \mu} \leq-1+\frac{n-3}{2} a u_{a}^{1-n}<-1+\frac{n-3}{2} a_{\max } v^{1-n}=0$$ \(\square\)

Remark 3.5. Notice that as $u \rightarrow \infty$, the metric $g_{a}$ approaches the hyperbolic metric. The metrics $g_{a}$ are Riemannian analogues of static generalized Kottler metrics, which are solutions of the Lorentzian Einstein's equations with a negative cosmological constant. We refer to Anderson [2] for a description of the conformal infinities of these metrics, and to Chruściel-Simon [13] for a study of Kottler spacetimes.

\subsection*{3.2 The sequence of interpolated metrics}

We now transfer the model metric to our sequence $\left(M_{k}\right)$ of compact hyperbolic $n$-manifolds. We keep the notation introduced at the beginning of Section 3. We let $\left(U_{k}\right)$ be a sequence tending to infinity with $k$ with $U_{k}<\frac{1}{2} U_{k, \text { max }}$.

Let $\Sigma_{k}^{0}$ denote a connected component of $\Sigma_{k}$. Using geodesics orthogonal to $\Sigma_{k}^{0}$, we can set up a tubular neighbourhood of $\Sigma_{k}^{0}$ in which the hyperbolic metric on $M_{k}$ is given by
$$\frac{\mathrm{d} u^{2}}{u^{2}-1}+\left(u^{2}-1\right) \mathrm{d} \theta^{2}+u^{2} h_{\Sigma}$$
Here $h_{\Sigma}$ is the hyperbolic metric on $\Sigma_{k}^{0}$ and $u=\cosh (r)$ where $r$ is the distance to $\Sigma_{k}^{0}$. The hypersurface $\theta=0$ corresponds to the totally geodesic hypersurface $H_{k}$; in general $\theta(p)$ is the angle that the shortest geodesic from $p$ to $\Sigma_{k}^{0}$ makes with $H_{k}$. This expression is valid for $(u, \theta) \in\left[1, U_{k, \text { max }}\right) \times S^{1}$.

Let $a \in\left(0, a_{\text {max }}\right)$. We define a new metric near $\Sigma_{k}^{0}$ interpolating between $g_{a}$ and the hyperbolic metric as follows. Let $\chi: \mathbb{R} \rightarrow[0, \infty)$ be a smooth function with $\chi(u)=1$ for $u \leq 1 / 2$ and $\chi(u)=0$ for $u \geq 1$. Write
$$V(u)=u^{2}-1+\frac{a}{u^{n-3}} \chi\left(\frac{u}{U_{k}}\right)$$
and consider the corresponding metric
$$\frac{\mathrm{d} u^{2}}{V}+V \mathrm{~d} \theta^{2}+u^{2} h_{\Sigma}$$
The factor $\chi(u / U)$ has the effect of interpolating between the Einstein model of the previous section for $u \leq \frac{1}{2} U_{k}$ and the hyperbolic metric for $u \geq U_{k}$. Since the model is close to hyperbolic at large distances from $\Sigma_{k}^{0}$, when $U_{k}$ is large this interpolation does not change the metric very much. As we will see, this means that the result is close to Einstein.

We also note that in terms of the intrinsic distance $r$ from $\Sigma_{k}^{0}$, we are using the Einstein model for $r<\log U_{k}$ and the hyperbolic metric for $r>\log U_{k}+\log 2$, so the band on which the interpolation takes place has fixed geodesic width, independent of $k$.

The expression for the interpolated metric is valid for $(u, \theta) \in\left(u_{a}, U_{k, \text { max }}\right) \times S^{1}$, where $u_{a}<1$ (since $a>0$ ). We remove the tubular neighbourhood of $\Sigma_{k}^{0}$ at a distance $U_{k}$ and glue this new metric in. The result is a metric on the same manifold, which is smooth across $u=U_{k}$ and which has a cone singularity along $\Sigma_{k}^{0}$ of angle $2 \pi c_{a}$. Carrying out this procedure at every connected component of $\Sigma_{k}$ we obtain a metric $\tilde{g}_{k}$ on $M_{k}$ which is Einstein near $\Sigma_{k}$, hyperbolic at long distances from $\Sigma_{k}$, and has cone singularities along each component of $\Sigma_{k}$, of angle $2 \pi c_{a}$.

We now pass to the $l$-fold branched cover $p: X_{k} \rightarrow M_{k}$. By Proposition 3.3, there is a unique value of $a \in\left(0, a_{\text {max }}\right)$ for which the cone angles of $\tilde{g}_{k}$ are $2 \pi / l$. It follows that the pull-back metric $g_{k}=p^{*} \tilde{g}_{k}$ is smooth on the whole of $X_{k}$, even across the branch locus. We are now in position to prove Proposition 3.1.

Proof of Proposition 3.1. First, part 3 is immediate from the construction, since the only place in which $\operatorname{Ric}\left(g_{k}\right)+(n-1) g_{k}$ is non-zero is the interpolation region. Let $m \in \mathbb{N}$ and $0 \leq \eta<1$. Using equations (3.5), (3.6) and (3.7) we immediately obtain that there is a constant $A$, depending on $m, \eta$ and $l$, but not on $k$, such that
$$\left\|\operatorname{Ric}\left(g_{k}\right)+(n-1) g_{k}\right\|_{C^{m, n}} \leq A U_{k}^{1-n}$$
which proves part 1.

We now move to part 2, showing that there is a constant $c>0$ such that for all large $k$, $\sec \left(g_{k}\right) \leq-c$. For $u \leq \frac{1}{2} U_{k}$ the metric $g_{k}$ agrees with the model whose sectional curvatures are uniformly bounded away from 0 , thanks to Lemma 3.4. For $u \geq U_{k}$, the metric $g_{k}$ is hyperbolic, and in the interpolation region $\frac{1}{2} U_{k}<u<U_{k}$ we have $\sec \left(g_{k}\right)=-1+O\left(U_{k}^{1-n}\right)$ as shown by Proposition 3.2. Similarly, part 4 follows from the previous calculations. \(\square\)

\section*{4 The inverse function theorem}

Our aim in this and the next section is to show that for all sufficiently large $k$ there is an Einstein metric on $X_{k}$ near to $g_{k}$. In this section we will set this up as a question about the inverse function theorem and reduce it to a key analytic estimate. We will then prove this estimate in the case $n=4$ in the following section.

\subsection*{4.1 The Bianchi gauge condition}

We will apply the implicit function theorem to a non-linear elliptic map between appropriate Banach spaces. Einstein's equations are diffeomorphism invariant and so not directly elliptic. We deal with this in the standard way (appropriate for Einstein metrics with negative scalar curvature) by adding an additional term, a technique called Bianchi gauge fixing. We describe this briefly here and refer to [1, 9] for proofs of the results we use.

The following applies to arbitrary closed Riemannian manifolds $(X, g)$, and so we momentarily drop the $k$ subscript to ease the notation. We write $\operatorname{div}_{g}: C^{\infty}\left(S^{2} T^{*} X\right) \rightarrow$ $C^{\infty}\left(T^{*} X\right)$ for the divergence of a symmetric 2-tensor. In abstract index notation, we have $\left(\operatorname{div}_{g} h\right)_{p}=-\nabla^{q} h_{p q}$, where ∇ is the Levi-Civita connection. We write $\operatorname{div}_{g}^{*}$ for the $L^{2}$-adjoint. Again, in index notation, $\left(\operatorname{div}_{g}^{*} \alpha\right)_{a b}=\nabla_{(a} \alpha_{b)}:=\frac{1}{2}\left(\nabla_{a} \alpha_{b}+\nabla_{b} \alpha_{a}\right)$.

A computation gives that the linearisation of the Ricci curvature is
$$\left(\mathrm{d}_{g} \operatorname{Ric}\right)(s)=\frac{1}{2} \Delta_{L}(s)-\operatorname{div}_{g}^{*} \operatorname{div}_{g}(s)-\frac{1}{2} \nabla \mathrm{~d} \operatorname{Tr}_{g}(s)$$
where $\Delta_{L}$ is the Lichnerowicz Laplacian:
$$\Delta_{L}(s)=\nabla^{*} \nabla+\operatorname{Ric}_{g} \circ s+s \circ \operatorname{Ric}_{g}-2 \operatorname{Rm}_{g}(s)$$
In index notation this is
$$\left(\Delta_{L} s\right)_{a b}=\nabla^{p} \nabla_{p} s_{a b}+R_{a}{ }^{p} s_{p b}+R_{b}{ }^{p} s_{p a}-2 s^{p q} R_{a p b q}$$

Define the Bianchi operator $B_{g}: C^{\infty}\left(S^{2} T^{*} X\right) \rightarrow C^{\infty}\left(T^{*} X\right)$ by
$$B_{g}(h)=\operatorname{div}_{g} h+\frac{1}{2} \mathrm{~d}\left(\operatorname{Tr}_{g} h\right)$$
Note that the contracted Bianchi identity gives $B_{g}(\operatorname{Ric}(g))=0$. Now given a pair of metrics $g, h$, we write
$$\Phi_{g}(h)=\operatorname{Ric}(h)+(n-1) h+\operatorname{div}_{h}^{*}\left(B_{g}(h)\right)$$

Here $\operatorname{div}_{h}^{*}$ is the formal adjoint of $\operatorname{div}_{h}$, taken with respect to the $L^{2}$ inner product defined by $h$. We call $\Phi_{g}$ the Einstein operator in Bianchi gauge relative to $g$.

One can check that the addition of this second term produces an elliptic map. We write $L_{h}$ for the derivative of $\Phi_{g}$ at $h$. The case $h=g$ is the simplest:
$$L_{g}(s)=\frac{1}{2} \Delta_{L} s+(n-1) s$$
The derivative at a general point is slightly more awkward. To describe it, we introduce the following notation. Given a metric $h$, a section $s \in C^{\infty}\left(S^{2} T^{*} X\right)$ and a 1-form $\alpha \in$ $C^{\infty}\left(T^{*} X\right)$ we consider the quantity
$$\lim _{t \rightarrow 0} \frac{\left(\operatorname{div}_{h+t s}^{*}-\operatorname{div}_{h}^{*}\right) \alpha}{t}$$
i.e., the infinitesimal change of $\operatorname{div}_{h}^{*}(\alpha)$ when $h$ moves in the direction $s$. This has an expression of the form $\alpha * \nabla s$ where ∇ is the Levi-Civita connection of $h$ and * denotes some universal algebraic contraction. (See for example, the discussion in §2.3.1 of [36].) We can now give the formula for $L_{h}$ :
$$\begin{aligned}
L_{h}(s)=\frac{1}{2} \Delta_{L, h}(s)+(n-1) s+\operatorname{div}_{h}^{*} & \left(\operatorname{div}_{g}-\operatorname{div}_{h}\right)(s) \\
& +\frac{1}{2} \nabla_{h} \mathrm{~d}\left(\operatorname{Tr}_{g}(s)-\operatorname{Tr}_{h}(s)\right)+B_{g}(h) * \nabla_{h}(s)
\end{aligned}$$
(where $\nabla_{h}$ denotes the Levi-Civita connection of $h$ ). This follows by direct differentiation of (4.3) together with the linearisation of Ricci curvature (4.1). Since $B_{g}(g)=0$, (4.4) follows from (4.5).

The precise expression for $L_{h}$ is not important in what follows. What is essential is that it is locally Lipschitz continuous in $h$. More precisely:

Lemma 4.1. Fix an integer $m \geq 2$ and $0 \leq \eta<1$. Given $K>0$ there exist constants $\delta, C>0$ such that if $g, h, \tilde{h}$ are Riemannian metrics on the same $n$-dimensional manifold with
$$\begin{array}{r}
\|g-h\|_{C^{m, \eta}},\|g-\tilde{h}\|_{C^{m, \eta}}<\delta \\
\left\|\operatorname{Rm}_{g}\right\|_{C^{m-2, \eta}}<K
\end{array}$$
where the norms are defined by $g$, then
$$\left\|\left(L_{h}-L_{\tilde{h}}\right)(s)\right\|_{C^{m-2, \eta}} \leq C\|h-\tilde{h}\|_{C^{m, \eta}}\|s\|_{C^{m, \eta}}$$
for all symmetric 2-tensors $s \in C^{m, \eta}$. (Here $L_{h}$ and $L_{\tilde{h}}$ are both defined using $g$ as the reference metric for the Bianchi gauge.)

This is again a standard result and we omit the proof. When there is no ambiguity we write $C^{m, \eta}$ for the space of symmetric bilinear forms of regularity $C^{m, \eta}$, and the Hölder norms in Lemma 4.1 are measured with respect to $g$ (see Definition 4.5 for the explicit definition of the Hölder norms used in this article). Lemma 4.1 implies that $\Phi_{g}: C^{m, \eta} \rightarrow$
$C^{m-2, \eta}$ is a continuously differentiable map of Banach spaces. (Strictly speaking, the domain of $\Phi_{g}$ is the open subset of $C^{m, \eta}$ consisting of positive definite sections.)

We next recall another important fact about Bianchi gauge: at least in the case of negative Ricci curvature, zeros of $\Phi_{g}$ are precisely Einstein metrics. To see this, one computes that
$$2 B_{h} \circ \operatorname{div}_{h}^{*}=\nabla_{h}^{*} \nabla_{h}-\operatorname{Ric}(h)$$
In particular, when $\operatorname{Ric}(h)$ is negative, $B_{h} \circ \operatorname{div}_{h}^{*}$ is an isomorphism. From this, the next result follows easily.

Lemma 4.2. Let $(X, g)$ be a closed Riemannian manifold and $h$ a second metric on $X$ with $\operatorname{Ric}(h)<0$. If $\Phi_{g}(h)=0$ then in fact $\operatorname{Ric}(h)=-(n-1) h$ and $B_{g}(h)=0$.

Proof. Since $B_{h}\left(\operatorname{Ric}_{h}\right)=0=B_{h}(h)$ the fact that $B_{h}\left(\Phi_{g}(h)\right)=0$ implies $B_{h}\left(\operatorname{div}_{h}^{*} B_{g}(h)\right)=$ 0 . Equation (4.6) and integration by parts then implies that $B_{g}(h)=0$ and so $\operatorname{Ric}_{h}=$ $-(n-1) h$. \(\square\)

\subsection*{4.2 The linearisation is invertible}

We return to our sequence $\left(X_{k}, g_{k}\right)$ of approximately Einstein metrics, constructed in §3. Write $\Phi_{k}=\Phi_{g_{k}}$ for the Einstein operator in Bianchi gauge relative to $g_{k}$. By Proposition 3.1, we have that $\Phi_{k}\left(g_{k}\right)=O\left(U_{k}^{1-n}\right)$. We would like to apply the inverse function theorem to $\Phi_{k}$ to show that for sufficiently large $k$ there is a metric $h$ near to $g_{k}$ with $\Phi_{k}(h)=0$. Since $g_{k}$ has negative curvature, the same will be true of $h$ and so, by Lemma 4.2, $h$ will be the Einstein metric we seek. We first show that the linearisation $L_{g}$ of $\Phi_{k}$ at $g$ is invertible for $g$ on a definite neighbourhood of $g_{k}$ whose diameter is bounded below independently of $k$.

Proposition 4.3. There exist constants $\delta>0$ and $C>0$ such that for all sufficiently large $k$, if $g$ is a Riemannian metric on $X_{k}$ with
$$\left\|g-g_{k}\right\|_{C^{2}} \leq \delta$$
then, for any $C^{2}$ symmetric bilinear form $s$,
$$\int_{X_{k}}\left\langle L_{g}(s), s\right\rangle_{g} \mathrm{dvol}_{g} \geq C \int_{X_{k}}|s|_{g}^{2} \mathrm{dvol}_{g}$$
It follows that for any $m \geq 2$ and $0<\eta<1$, the linearisation $L_{g}: C^{m, \eta} \rightarrow C^{m-2, \eta}$ is an isomorphism.

In the statement of Proposition 4.3 it is implicit that the Hölder norm is taken with respect to the metric $g_{k}$. Throughout the proof we use the fact that, provided $\delta$ is small enough, the $C^{0}$ norms defined by $g$ and $g_{k}$ are equivalent uniformly in $k$. We will switch between them without further comment. Our proof is an adaptation of an argument due to Koiso [29] to our setting. Koiso's Theorem showed that if $h$ is an Einstein metric of negative sectional curvature on a compact manifold $M$, then
$$\int_{M}\left\langle L_{h}(s), s\right\rangle \geq \frac{n-2}{2} K \int_{M}|s|^{2} \mathrm{dvol}$$
where $-K$ is the supremum of the sectional curvatures of $h$. Here, $L_{h}$ is the linearised Einstein operator in Bianchi gauge relative to $h$ itself. In our situation, there are two small additional complications. Firstly, $g_{k}$ is merely close to Einstein; secondly we linearise at an arbitrary metric close to $g_{k}$. In particular, when $g \neq g_{k}$, the linearised operator at $g$ is not self-adjoint anymore. A first lemma is as follows:

Lemma 4.4. There exist constants $\delta_{0}>0$ and $C>0$ such that for all $0<\delta \leq \delta_{0}$ and all sufficiently large $k$, if $g$ is a Riemannian metric on $X_{k}$ with
$$\left\|g-g_{k}\right\|_{C^{2}} \leq \delta$$
then, for any $C^{2}$ symmetric bilinear form $s$,
$$\begin{aligned}
\int_{X_{k}}\left\langle L_{g}(s), s\right\rangle_{g} \mathrm{dvol}_{g} \geq\left(\frac{1}{2}-C \delta\right) \int_{X_{k}}|\nabla s|_{g}^{2} \mathrm{dvol}_{g}-C \delta & \int_{X_{k}}|s|_{g}^{2} \mathrm{dvol}_{g} \\
& -\int_{X_{k}}\left\langle\operatorname{Rm}_{g}(s), s\right\rangle_{g} \mathrm{dvol}_{g}
\end{aligned}$$
(where ∇ is the Levi-Civita connection of $g$ ).
Proof. From the expression (4.5) for $L_{g}$, we can write
$$\int_{X_{k}}\left\langle L_{g}(s), s\right\rangle_{g} \mathrm{dvol}_{g}=\frac{1}{2} \int_{X_{k}}|\nabla s|_{g}^{2} \mathrm{dvol}_{g}+I_{1}+I_{2}+I_{3}+I_{4}+I_{5}$$
where
$$\begin{aligned}
I_{1} & =\int_{X_{k}}\left\langle\frac{1}{2}\left(\operatorname{Ric}_{g} \circ s+s \circ \operatorname{Ric}_{g}\right)+(n-1) s, s\right\rangle \operatorname{dvol}_{g} \\
I_{2} & =\int_{X_{k}}\left\langle\operatorname{div}_{g}^{*}\left(\operatorname{div}_{g_{k}}-\operatorname{div}_{g}\right)(s), s\right\rangle \operatorname{dvol}_{g} \\
I_{3} & =\int_{X_{k}} \frac{1}{2}\left\langle\nabla \mathrm{~d}\left(\operatorname{Tr}_{g} s-\operatorname{Tr}_{g_{k}} s\right), s\right\rangle \operatorname{dvol}_{g} \\
I_{4} & =\int\left\langle B_{g_{k}}(g) * \nabla s, s\right\rangle \operatorname{dvol}_{g} \\
I_{5} & =-\int_{X_{k}}\left\langle\operatorname{Rm}_{g}(s), s\right\rangle \operatorname{dvol}_{g}
\end{aligned}$$
(where ∇ denotes the Levi-Civita connection of $g$.)
Since the metrics $g_{k}$ have uniformly bounded curvature tensors we get that for all large $k$,
$$\left\|\operatorname{Ric}_{g}-\operatorname{Ric}_{g_{k}}\right\|_{C^{0}} \leq C \delta$$
(see, for example, Lemma 2.8 of [17] for a proof). Combining the latter with Proposition 3.1, for all $k$ sufficiently large, we get that there is a constant $c_{1}>0$ such that
$$\left\|\operatorname{Ric}_{g}+(n-1) g\right\|_{C^{0}} \leq c_{1} \delta$$

As a consequence:
$$\left|I_{1}\right| \leq c_{1} \delta \int_{X_{k}}|s|_{g}^{2} \mathrm{dvol}_{g}$$
Next, there is a constant $c>0$ such that at all points
$$\left|\left(\operatorname{div}_{g_{k}}-\operatorname{div}_{g}\right)(s)\right|_{g} \leq c \delta\left(|s|_{g}+|\nabla s|_{g}\right)$$
Integrating by parts and using Young's inequality then yields:
$$\left|I_{2}\right| \leq c_{2} \delta\left(\int_{X_{k}}|s|_{g}^{2}+|\nabla s|_{g}^{2}\right) \mathrm{dvol}_{g}$$
for some constant $c_{2}$, provided $\delta>0$ is small enough. In exactly the same way, we see that there are constants $c_{3}, c_{4}$ such that
$$\begin{aligned}
& \left|I_{3}\right| \leq c_{3} \delta\left(\int_{X_{k}}|s|_{g}^{2}+|\nabla s|_{g}^{2}\right) \mathrm{dvol}_{g} \\
& \left|I_{4}\right| \leq c_{4} \delta\left(\int_{X_{k}}|s|_{g}^{2}+|\nabla s|_{g}^{2}\right) \mathrm{dvol}_{g}
\end{aligned}$$
For (4.13) we used that $B_{g_{k}}\left(g_{k}\right)=0$ and thus
$$\left|B_{g_{k}}(g) * \nabla s\right|_{g} \leq c \delta|\nabla s|_{g}$$
Finally, putting (4.10), (4.11), (4.12), (4.13) together proves the result. \(\square\)

Proof of Proposition 4.3. First, a Weitzenböck formula (see e.g. equation (1.5.6) in [9]) shows that for any $C^{2}$ symmetric bilinear form $s$,
$$\int_{X_{k}}|\nabla s|_{g}^{2} \mathrm{dvol}_{g} \geq(n-1-c \delta) \int_{X_{k}}|s|_{g}^{2} \mathrm{dvol}_{g}+\int_{X_{k}}\left\langle\operatorname{Rm}_{g}(s), s\right\rangle_{g} \mathrm{dvol}_{g}$$
(where ∇ is the Levi-Civita connection of $g$ ). Putting Lemma 4.4 and (4.14) together we then see that
$$\begin{aligned}
\int_{X_{k}}\left\langle L_{g}(s), s\right\rangle_{g} \mathrm{dvol}_{g} \geq\left(-\frac{1}{2}-C \delta\right) \int_{X_{k}}\left\langle\mathrm{Rm}_{g}(s)\right. & , s\rangle_{g} \mathrm{dvol}_{g} \\
& +\left(\frac{n-1}{2}-C \delta\right) \int_{X_{k}}|s|_{g}^{2} \mathrm{dvol}_{g}
\end{aligned}$$
We work at a point $p$ and write $\lambda_{i}$ for the eigenvalues of $s$ at that point. Then, in an orthonormal eigenbasis for $s$,
$$\left\langle\operatorname{Rm}_{g}(s), s\right\rangle=s^{a b} s^{p q} R_{a p b q}=\sum_{i \neq j} \lambda_{i} \lambda_{j} K_{i j}$$
where $K_{i j}$ is the sectional curvature of $g$ in the plane spanned by the $\lambda_{i}$ and $\lambda_{j}$ eigendirections of $s$. By Proposition 3.1, the sectional curvatures of $g_{k}$ are negative, uniformly in $k$. Since $g$ is close to $g_{k}$ in $C^{2}$, it also has uniformly negative sectional curvatures. I.e., there
is a constant $K>0$ such that $K_{i j}<-K$ for all $k$ (and all points). Moreover, by (4.9), we have control over the following sum of the sectional curvatures:
$$\sum_{j} K_{i j}=\operatorname{Ric}_{g}\left(e_{i}, e_{i}\right) \geq 1-n-c \delta$$
where $e_{i}$ is a unit eigenvector for the $\lambda_{i}$-eigenvalue of $s$. A straightforward adaptation of Koiso's argument ([29], see also Lemma 12.71 in [7]) then gives:
$$\int_{X_{k}}\left\langle\operatorname{Rm}_{g}(s), s\right\rangle_{g} \operatorname{dvol}_{g} \leq(n-1-(n-2) K+c \delta) \int_{X_{k}}|s|_{g}^{2} \operatorname{dvol}_{g}$$
With (4.15) this yields the desired result provided $\delta$ is taken small enough. \(\square\)

\subsection*{4.3 Weighted Hölder spaces}

The crux to applying the inverse function theorem to find a zero of $\Phi_{k}$ is to obtain uniform control over the inverse $L_{g}^{-1}$. Proposition 4.3 shows that the lowest eigenvalue of $L_{g}$ is uniformly bounded away from zero and this immediately gives good control of the inverse in $L^{2}$. This is not sufficient for our purposes, however. The volume of $\left(X_{k}, g_{k}\right)$ grows rapidly with $k$, so much so that even though we have strong pointwise control of $\Phi_{g_{k}}\left(g_{k}\right)$ it does not even imply that $\Phi_{g_{k}}\left(g_{k}\right)$ tends to zero in $L^{2}$. Instead we work in Hölder spaces. Moreover, since the diameter of $\left(X_{k}, g_{k}\right)$ tends to infinity, weighted Hölder spaces are required.