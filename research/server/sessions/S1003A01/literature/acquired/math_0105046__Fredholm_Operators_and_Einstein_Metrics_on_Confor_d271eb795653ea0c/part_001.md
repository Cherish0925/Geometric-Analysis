---
retention_scope: session
part: 1
total_parts: 4
---

[Part 1/4 of: [math/0105046] Fredholm Operators and Einstein Metrics on Conformally Compact Manifolds]

---
source_file: math_0105046.pdf
converter: mathpix
format: mmd
---

\section*{arXiv:math/0105046v5 [math.DG] 27 Jul 2006}

\title{
Fredholm Operators and Einstein Metrics on Conformally Compact Manifolds
}

\author{
John M. Lee
}

Author address:
University of Washington, Department of Mathematics, Box 354350, Seattle, WA 98195-4350
E-mail address: lee@math.washington.edu
URL: http://www.math.washington.edu/ ${ }^{\sim}$ lee

\section*{Contents}
Chapter 1 Introduction ..... 1
Chapter 2. Möbius Coordinates ..... 9
Chapter 3. Function Spaces ..... 13
Chapter 4. Elliptic Operators ..... 23
Chapter 5. Analysis on Hyperbolic Space ..... 34
Chapter 6. Fredholm Theorems ..... 43
Chapter 7 Laplace Operators, ..... 58
Chapter 8. Einstein Metrics ..... 70
Bibliography ..... 77

\begin{abstract}
The main purpose of this monograph is to give an elementary and self-contained account of the existence of asymptotically hyperbolic Einstein metrics with prescribed conformal infinities sufficiently close to that of a given asymptotically hyperbolic Einstein metric with nonpositive curvature. The proof is based on an elementary derivation of sharp Fredholm theorems for self-adjoint geometric linear elliptic operators on asymptotically hyperbolic manifolds.
\end{abstract}

\footnotetext{
Received by the editor February 16, 2004.
1991 Mathematics Subject Classification. [.
Key words and phrases. asymptotically hyperbolic, Einstein metric, conformally compact, Fredholm operator, nonlinear elliptic partial differential equations.

Research supported in part by National Science Foundation grants DMS-8901493 and DMS-9404107.
}

\section*{CHAPTER 1}

\section*{Introduction}

In 1985, Charles Fefferman and Robin Graham [28] introduced a new and powerful approach to the study of local invariants of conformal structures, based on the observation that the group of conformal automorphisms of the $n$-sphere (the Möbius group) is essentially the same as the group of Lorentz transformations of $(n+2)$-dimensional Minkowski space. Concretely, one sees this by noting that the conformal structure of the $n$-sphere can be obtained by viewing the sphere as a cross-section of the forward light cone in Minkowski space. Fefferman and Graham attempted to embed an arbitrary conformal $n$-manifold into an $(n+2)$ -dimensional Ricci-flat Lorentz manifold. They showed that such a Lorentz metric (which they called the ambient metric) can be constructed by formal power series for any conformal Riemannian metric, to infinite order when $n$ is odd and to order $n / 2$ when $n$ is even; and that this formal metric is a conformal invariant of the original conformal structure.

Once this Lorentz metric (or at least its formal power series) is constructed, its pseudo-Riemannian invariants then automatically give conformal invariants of the original conformal structure. Combined with later work of Bailey, Eastwood, and Graham ${ }^{\mathbf{1}} \mathbf{1}$, this construction produces all local scalar conformal invariants of odd-dimensional conformal Riemannian structures.

In [29], Graham and I adapted this idea to the global setting. We began with the observation that there is a third natural realization of the Möbius group, as the set of isometries of the hyperbolic metric on the interior of the unit ball $\mathbb{B}^{n+1} \subset$ $\mathbb{R}^{n+1}$. As noted by Fefferman and Graham in [28], given a compact Riemannian manifold $(S, \widehat{g})$, the problem of finding a Ricci-flat ambient Lorentz metric for the conformal structure $[\widehat{g}]$ is equivalent to that of finding an asymptotically hyperbolic Einstein metric $g$ on the interior of an $(n+1)$-dimensional manifold-with-boundary $\bar{M}$ that has $S$ as boundary and $[\widehat{g}]$ as conformal infinity in the following sense: For any smooth, positive defining function $\rho$ for $S=\partial M$, the metric $\rho^{2} g$ extends continuously to $\bar{M}$ and restricts to a metric in the conformal class $[\widehat{g}]$ on $S$. This suggests the following natural problem: Given a compact manifold-with-boundary $\bar{M}$ and a conformal structure $[\widehat{g}]$ on $\partial M$, can one find a complete, asymptotically hyperbolic Einstein metric $g$ on the interior manifold $M$ that has $[\widehat{g}]$ as conformal infinity? Such a metric is said to be conformally compact. To the extent that the answer is yes and the resulting Einstein metric is unique up to boundary-fixing diffeomorphisms, one would thereby obtain a correspondence between global conformal invariants of $[\widehat{g}]$ and global Riemannian invariants of $g$. Graham and I showed in [29] that every conformal structure on $\mathbb{S}^{n}$ sufficiently close to that of the round metric is the conformal infinity of an Einstein metric close to the hyperbolic metric.

In recent years, interest in asymptotically hyperbolic Einstein metrics has risen dramatically, in no small part because of the role they play in physics. In fact, the notion of conformal infinity for a (pseudo-) Riemannian metric was originally introduced by Roger Penrose [51] in order to analyze the behavior of gravitational energy in asymptotically flat space-times. More recently, asymptotically hyperbolic Einstein metrics have begun to play a central role in the "AdS/CFT correspondence" of quantum field theory. This is not the place for a complete survey of the relevant literature, but let me just refer the reader to $24,2,6,74,16,15,18,29,30,131,32,137,38,146,50,52,57,59$.

The principal purpose of this monograph is to give an elementary and selfcontained account of the following generalization of the perturbation result of [29]. First, a couple of definitions: The Lichnerowicz Laplacian (cf. [13]) is the operator $\Delta_{\mathrm{L}}$ defined on symmetric 2-tensors by $\Delta_{\mathrm{L}}=\nabla^{*} \nabla+2 \stackrel{\circ}{R} c-2 \stackrel{\circ}{R m}$, where $\stackrel{\circ}{R} c$ and $\stackrel{\circ}{R m}$ are the natural actions of the Ricci and Riemann curvature tensors on symmetric 2-tensors given in coordinates by
$$\begin{aligned}
\stackrel{\circ}{R} c(u)_{i j} & =\frac{1}{2}\left(R_{i k} u_{j}^{k}+R_{j k} u_{i}^{k}\right), \\
\stackrel{\circ}{R m}(u)_{i j} & =R_{i k j l} u^{k l} .
\end{aligned}$$
For any conformal class of Riemannian metrics on $\partial M$, the Yamabe invariant is defined as the infimum of the total scalar curvature $\int_{\partial M} S_{\widehat{g}} d V_{\widehat{g}}$ over unit-volume metrics $\widehat{g}$ in the conformal class.

Theorem A. Let $M$ be the interior of a smooth, compact, $(n+1)$-dimensional manifold-with-boundary $\bar{M}, n \geq 3$, and let $h$ be an Einstein metric on $M$ that is conformally compact of class $C^{l, \beta}$ with $2 \leq l \leq n-1$ and $0<\beta<1$. Let $\rho$ be a smooth defining function for $\partial M$, and let $\widehat{h}=\left.\rho^{2} h\right|_{\partial M}$. Suppose the operator $\Delta_{\mathrm{L}}+2 n$ associated with $h$ has trivial $L^{2}$ kernel on the space of trace-free symmetric 2-tensors. Then there is a constant $\varepsilon>0$ such that for any $C^{l, \beta}$ Riemannian metric $\widehat{g}$ on $\partial M$ with $\|\widehat{g}-\widehat{h}\|_{C^{l, \beta}}<\varepsilon$, there exists an Einstein metric $g$ on $M$ that has $[\widehat{g}]$ as conformal infinity and is conformally compact of class $C^{l, \beta}$. In particular, this is the case if either of the following hypotheses is satisfied:
\begin{itemize}
\item[(a)] $h$ has nonpositive sectional curvature.
\item[(b)] The Yamabe invariant of $[\widehat{h}]$ is nonnegative and $h$ has sectional curvatures bounded above by $\left(n^{2}-8 n\right) /(8 n-8)$.
\end{itemize}

An important feature of this result is that the conformal compactification of the Einstein metric has optimal Hölder regularity up to the boundary (in terms of standard Hölder spaces on $\bar{M}$ ), at least when $n$ is even. The work of Fefferman and Graham showed that generically for $n$ even there will be a $\rho^{n} \log \rho$ term in the asymptotic expansion of $\bar{g}$ if $g=\rho^{-2} \bar{g}$ is Einstein; thus we cannot expect to find Einstein metrics with $C^{n}$ conformal compactifications in general. If $h$ has a sufficiently smooth conformal compactification and $\widehat{g}$ is close to $\widehat{h}$ with sufficiently many derivatives, then Theorem gives an Einstein metric that is conformally compact of class $C^{n-1, \beta}$ for any $0<\beta<1$, which is the best Hölder regularity that can be expected when $n$ is even. The results of [21] show that any Einstein metric with smooth conformal infinity and $C^{2}$ conformal compactification actually has an infinite-order asymptotic expansion in powers of $\rho$ and $\log \rho$, and in fact is smooth when $n$ is odd.

A version of Theorem (but with less boundary regularity of the resulting Einstein metrics) was also proved independently by Olivier Biquard [15] around the same time as this monograph was originally completed. In addition, analogous perturbation results starting with Kähler-Einstein metrics on bounded domains have been proved independently by Biquard [15] and John Roth [54], and for Einstein metrics asymptotic to the quaternionic and octonionic hyperbolic metrics by Biquard [15]. See below for more on this. See also [3], 4] for some recent results by Michael Anderson on existence and uniqueness of asymptotically hyperbolic Einstein metrics on 4-manifolds, and [22, 24] for results by Erwann Delay and Marc Herzlich on the related problem of prescribing the Ricci curvatures of metrics close to the Einstein models.

The basic approach in this monograph is similar to that of $\left[\mathbf{2} \overline{\mathbf{9}}^{\mathbf{1}}\right.$. Because the Einstein equation is invariant under the full diffeomorphism group of $M$, it is not elliptic as it stands. We obtain an elliptic equation by adding a gauge-breaking term: Fixing a conformally compact "reference metric" $g_{0}$, let $\Delta_{g g_{0}}$ (Id) denote the harmonic map Laplacian of the identity map, considered as a map from $(M, g)$ to $\left(M, g_{0}\right)$, and let $\delta_{g}$ be the divergence operator associated with $g$. Then, as is by now familiar, the nonlinear equation
$$Q\left(g, g_{0}\right):=R c_{g}+n g-\delta_{g}^{*}\left(\Delta_{g g_{0}}(\mathrm{Id})\right)=0$$
is elliptic as a function of $g$. Under relatively mild assumptions on $g$ (see [29, Lemma 2.2]), the solutions to (12) are exactly those Einstein metrics $g$ such that $\Delta_{g g_{0}}(\mathrm{Id})=0$, i.e., such that Id: $(M, g) \rightarrow\left(M, g_{0}\right)$ is harmonic.

The linearization of the left-hand side of (1.2) with respect to $g$ at a conformally compact Einstein metric $h$ is
$$D_{1} Q_{(h, h)}=\frac{1}{2}\left(\Delta_{\mathrm{L}}+2 n\right),$$
where $\Delta_{\mathrm{L}}$ is the Lichnerowicz Laplacian defined above. In [29], we proved that when $h$ is the hyperbolic metric on the unit ball $\mathbb{B}^{n+1}, \Delta_{\mathrm{L}}+2 n$ is an isomorphism between certain weighted Hölder spaces. However, our methods in that paper were insufficient to prove a sharp isomorphism theorem, with the consequence that our boundary regularity results were not optimal, so even in the case of hyperbolic space Theorem is an improvement on the results of [29].

Much of this monograph is devoted to an elementary proof of some general sharp Fredholm and isomorphism theorems for self-adjoint geometric linear elliptic operators on asymptotically hyperbolic manifolds. These operators are, in particular, uniformly degenerate, in the terminology introduced in [29] (with perhaps less smoothness of the coefficients than we insisted on there): A partial differential operator $P$ on a manifold with boundary is said to be uniformly degenerate if in local coordinates $\left(\theta^{1}, \ldots, \theta^{n}, \rho\right)$ such that $\rho=0$ defines the boundary, $P$ can be written locally as a a system of partial differential operators that are polynomials in the vector fields $\left(\rho \partial / \partial \theta^{1}, \ldots, \rho \partial / \partial \theta^{n}, \rho \partial / \partial \rho\right)$ with coefficients that are at least continuous up to the boundary.

To get an idea of what can be expected, consider a simple example: the scalar Laplacian $\Delta=d^{*} d$ on functions. When applied to a function of $\rho$ alone, this becomes an ordinary differential operator with a regular singular point at $\rho=$ 0. From classical ODE theory, we know that a second-order ordinary differential operator $L$ with a regular singular point at 0 has two characteristic exponents $s_{1}$ and $s_{2}$, defined by $L\left(\rho^{s_{i}}\right)=O\left(\rho^{s_{i}+1}\right)$; if $s_{1} \neq s_{2}$, the homogeneous equation $L u=0$
has two independent solutions $u_{1}, u_{2}$ with $u_{i}=O\left(\rho^{s_{i}}\right)$, and the inhomogeneous equation $L u=f=O\left(\rho^{s}\right)$ can be solved with $u=O\left(\rho^{s}\right)$ whenever $s$ is not a characteristic exponent.

To see how this generalizes to systems of partial differential operators, let $P: C^{\infty}(M ; E) \rightarrow C^{\infty}(M ; F)$ be a uniformly degenerate operator of order $m$ acting between (real or complex) tensor bundles $E$ and $F$, and let $s$ be any complex number. Define the indicial map $I_{s}(P):\left.\left.E\right|_{\partial M} \rightarrow F\right|_{\partial M}$ by setting
$$I_{s}(P) \bar{u}:=\left.\rho^{-s} P\left(\rho^{s} \bar{u}\right)\right|_{\partial M},$$
where $\bar{u}$ is any $C^{m}$ section of $\left.E\right|_{\partial M}$, extended arbitrarily to a $C^{m}$ section of $E$ near $\partial M$. It follows easily from the definition of uniformly degenerate operators that $I_{s}(P)$ is a (pointwise) bundle endomorphism whose coefficients in any local coordinates are polynomials in $s$ with continuous coefficients depending on $\theta \in$ $\partial M$. (In the special case of a single ODE with a regular singular point, $I_{s}(P)$ is just multiplication by a number depending polynomially on $s$, called the indicial polynomial of the ODE.) We say a number $s$ is a characteristic exponent for $P$ if $I_{s}(P)$ is singular somewhere on $\partial M$. Just as in the ODE case, one can construct formal series solutions to $P u=f$ in which the characteristic exponents correspond to powers of $\rho$ whose coefficients are arbitrary.

Now consider a formally self-adjoint operator acting on sections of a tensor bundle $E$ of type $\binom{r_{1}}{r_{2}}$ (i.e., covariant rank $r_{1}$ and contravariant rank $r_{2}$ ). In this case, the difference $r=r_{1}-r_{2}$, which we call the weight of $E$, is of central importance, and the exponent $n / 2-r$ plays a special role. If $\bar{u}$ is a section of $E$ that is continuous up to the boundary, then $\rho^{n / 2-r} \bar{u}$ is just on the borderline of being in $L^{2}$ (see Lemma 3.2( $\mathbf{q}$ )). If $P$ is formally self-adjoint, the set of characteristic exponents turns out to be symmetric about the line $\operatorname{Re} s=n / 2-r$ (Corollary 4.5!). Therefore, we define the indicial radius of $P$ to be the smallest real number $R \geq 0$ such that $P$ has a characteristic exponent whose real part is equal to $n / 2-r+R$. A little experimentation leads one to expect that $P u=f$ should be well-posed roughly when $u$ and $f$ behave like $\rho^{s} \bar{u}$, where $\bar{u}$ is continuous up to the boundary and $n / 2-r-R<s<n / 2-r+R$, because for lower values of $s$ one expects $P$ to have an infinite-dimensional kernel, and for higher values one expects an infinite-dimensional cokernel. (This will be made precise in Chapter $\overline{\mathbf{6}}_{\mathbf{r}}^{\mathbf{1}}$ ) Therefore, a fundamental necessary condition for all of our Fredholm results will be that $P$ has positive indicial radius.

To control the order of vanishing or singularity of $u$ and $f$ at the boundary, we work in weighted Sobolev and Hölder spaces, with weights given by powers of the defining function $\rho$. Precise definitions are given in Chapter but the spaces we work in can be roughly defined as follows: The weighted Sobolev space $H_{\delta}^{k, p}$ is just the space of tensor fields of the form $\rho^{\delta} u$ for $u$ in the usual intrinsic Sobolev space $H^{k, p}$ (tensor fields with $k$ covariant derivatives in $L^{p}$ with respect to $g$ ); and the weighted Hölder space $C_{\delta}^{k, \alpha}$ consists of tensor fields of the form $\rho^{\delta} u$ for $u$ in the usual Hölder space $C^{k, \alpha}$. In each case, the Sobolev and Hölder norms are defined with respect to a fixed conformally compact metric on $M$.

An elementary criterion for operators to be Fredholm on $L^{2}$ is given in the following proposition. Terms used in the statements of these results will be defined in Chapters and

Proposition B. Let ( $M, g$ ) be a connected asymptotically hyperbolic $(n+1)$ manifold of class $C^{l, \beta}$, with $n \geq 1, l \geq 2$, and $0 \leq \beta<1$, and let $E \rightarrow M$ be a geometric tensor bundle over $M$. Suppose $P: C^{\infty}(M ; E) \rightarrow C^{\infty}(M ; E)$ is an elliptic, formally self-adjoint, geometric partial differential operator of order $m$, $0<m \leq l$. As an unbounded operator, $P: L^{2}(M ; E) \rightarrow L^{2}(M ; E)$ is Fredholm if and only if there exist a compact set $K \subset M$ and a positive constant $C$ such that
$$\|u\|_{L^{2}} \leq C\|P u\|_{L^{2}} \text { for all } u \in C_{c}^{\infty}(M \backslash K ; E) .$$

The main analytic result we need for Theorem is the following sharp Fredholm theorem in weighted Sobolev and Hölder spaces for geometric elliptic operators. (See below for references to other proofs of these and similar results using different approaches.)

Theorem C. Let $(M, g)$ be a connected asymptotically hyperbolic $(n+1)$ manifold of class $C^{l, \beta}$, with $n \geq 1, l \geq 2$, and $0 \leq \beta<1$, and let $E \rightarrow M$ be a geometric tensor bundle over $M$. Suppose $P: C^{\infty}(M ; E) \rightarrow C^{\infty}(M ; E)$ is an elliptic, formally self-adjoint, geometric partial differential operator of order $m$, $0<m \leq l$, and assume $P$ satisfies (1.4).
\begin{itemize}
\item[(a)] The indicial radius $R$ of $P$ is positive.
\item[(b)] If $1<p<\infty$ and $m \leq k \leq l$, the natural extension
$$P: H_{\delta}^{k, p}(M ; E) \rightarrow H_{\delta}^{k-m, p}(M ; E)$$
is Fredholm if and only if $|\delta+n / p-n / 2|<R$. In that case, its index is zero, and its kernel is equal to the $L^{2}$ kernel of $P$.
\item[(c)] If $0<\alpha<1$ and $m<k+\alpha \leq l+\beta$, the natural extension
$$P: C_{\delta}^{k, \alpha}(M ; E) \rightarrow C_{\delta}^{k-m, \alpha}(M ; E)$$
is Fredholm if and only if $|\delta-n / 2|<R$. In that case, its index is zero, and its kernel is equal to the $L^{2}$ kernel of $P$.
\end{itemize}

The statement and proof of this theorem extend easily to operators on spinor bundles when $M$ is a spin manifold. We restrict attention here to the case of tensor bundles mainly for simplicity of exposition.

We define a Laplace operator to be a formally self-adjoint second-order geometric operator of the form $\nabla^{*} \nabla+\mathscr{K}$, where $\mathscr{K}$ is a bundle endomorphism. Of course, the ordinary Laplacian on functions and the covariant Laplacian on tensor fields are obvious examples of Laplace operators, as are the Lichnerowicz Laplacian $\Delta_{\mathrm{L}}$ defined above, and the Laplace-Beltrami operator on differential forms by virtue of Bochner's formula.

The most important example to which we will apply these results is the Lichnerowicz Laplacian on symmetric 2-tensors.

Proposition D. If $c \in \mathbb{R}$, the operator $\Delta_{\mathrm{L}}+c$ acting on symmetric 2-tensors satisfies the hypotheses of Theorem if and only if $c>2 n-n^{2} / 4$, in which case the indicial radius of $\Delta_{\mathrm{L}}+c$ is
$$R=\sqrt{\frac{n^{2}}{4}-2 n+c} .$$
The essential $L^{2}$ spectrum of $\Delta_{\mathrm{L}}$ is $\left[n^{2} / 4-2 n, \infty\right)$.
(This characterization of the essential spectrum of $\Delta_{\mathrm{L}}$ has also been proved by E. Delay in [23], using some of the ideas from an earlier draft of this monograph.)

Another example is the covariant Laplacian on trace-free symmetric tensors of any rank.

Proposition E. If $c \in \mathbb{R}$, the operator $\nabla^{*} \nabla+c$ acting on trace-free covariant symmetric $r$-tensors satisfies the hypotheses of Theorem if and only if $c>-r-$ $n^{2} / 4$, in which case the indicial radius of $\nabla^{*} \nabla+c$ is
$$R=\sqrt{\frac{n^{2}}{4}+r+c} .$$
The essential $L^{2}$ spectrum of $\nabla^{*} \nabla$ is $\left[n^{2} / 4+r, \infty\right)$.
Also, for completeness, we point out the following result, originally proved in the $L^{2}$ case by Rafe Mazzeo (cf. [39, 40.71 ).

Proposition F. The Laplace-Beltrami operator acting on $q$-forms satisfies the hypotheses of Theorem in the following cases:
\begin{itemize}
\item[(a)] When $0 \leq q<n / 2$, with $R=n / 2-q$.
\item[(b)] When $n / 2+1<q \leq n+1$, with $R=q-n / 2-1$.
\end{itemize}
In each case, the essential $L^{2}$ spectrum of $\Delta$ is $\left[R^{2}, \infty\right)$.
Finally, we describe one significant non-Laplace operator to which Theorem C applies. The conformal Killing operator is the operator $L: C^{\infty}(M ; T M) \rightarrow$ $C^{\infty}\left(M ; \Sigma_{0}^{2} M\right)$ (where $\Sigma_{0}^{2} M$ is the bundle of trace-free symmetric 2-tensors) defined by letting $L V$ be the trace-free part of the symmetrized covariant derivative of $V$ (see Chapter $\overline{\mathbf{T}}_{\mathbf{1}}$ for details). A vector field $V$ satisfies $L V=0$ if and only if the flow of $V$ preserves the conformal class of $g$. The operator $L^{*} L$, sometimes called the vector Laplacian, plays an important role in the conformal approach to constructing initial data for the Einstein field equations of general relativity; see ${ }^{\mathbf{8 1}}, \mathbf{3 3}$,

Proposition G. The vector Laplacian $L^{*} L$ satisfies the hypotheses of Theorem , with $R=n / 2+1$.

Most of the analytic results in Theorem and Propositions are not really new. The systematic treatment of elliptic uniformly degenerate operators dates back to the work of Mazzeo, building on earlier work of Richard Melrose and others , and Theorem Can also be derived from Mazzeo's microlocal "edge calculus" (cf. [41, Theorem 6.1]). Also, $L^{2}$-Fredholm criteria for a general class of operators including the ones considered here have been obtained by Robert Lauter, Bertrand Monthubert, and Victor Nistor [36, Thm. 4], using the theory of pseudodifferential operators on groupoids. For many purposes in geometric analysis, however, it is useful to have a more "low-tech" approach that does not use pseudodifferential operators. An elementary approach to uniformly degenerate operators based on a priori estimates has been used by Graham and Lee [29], Lars Andersson and Piotr Chrusciel [7, 8], Johan Råde [53], and Michael Anderson [4, 3, 5].

The exposition I present here is based on this low-tech approach, and consists of three main ingredients: sharp a priori $L^{2}$ estimates, a decay estimate for the hyperbolic Green kernel using the spherical symmetry of the ball model, and a technique due to Råde [53] for piecing together a parametrix out of this model Green kernel. One advantage of this approach is that it deals quite naturally with
operators whose coefficients are not smooth up to the boundary, a feature that is crucial for the application to Einstein metrics, because the metrics around which we linearize generally have only finite boundary regularity. It is worth noting that for many Laplace operators, the Green kernel estimates are needed only for extending the sharp Fredholm results to Hölder and $L^{p}$ spaces; sharp Fredholm results in weighted $L^{2}$ spaces can be obtained by a much more elementary proof based solely on a priori estimates. See Chapter for details.

The main new results in this monograph are the Bochner-type formula (7.7) for Laplacians on tensor-valued differential forms, which yields a completely elementary proof of sharp Fredholm theorems in weighted $L^{2}$ spaces and the identification of the essential spectrum (Chapter $\overline{\boldsymbol{T}}$ ); new sufficient curvature conditions for the invertibility of the Lichnerowicz Laplacian (part struction of Einstein metrics in the optimal $C^{n-1, \beta^{\prime}}$ Hölder class up to the boundary when the conformal infinity is sufficiently smooth.

Theorem 'Can be viewed as complementary to the regularity results of Andersson and Chruściel; in particular, for an operator of the type considered here, Proposition 6.5 below can be used to obtain_sharp "regularity intervals" in the sense defined in [8], and then the results of [8] can be used to derive asymptotic expansions for solutions to equations of the form $P u=f$ when $f$ and the metric are sufficiently smooth. We leave it to the interested reader to work out the details. See $\left.[\mathbf{2}]^{1}\right]$ for example, where these ideas play a central role in the proof of boundary regularity for asymptotically hyperbolic Einstein metrics. Similar results can also be obtained using the edge calculus of [41].

The assumption of a weak a priori $L^{2}$ estimate (1.4) near the boundary is used primarily to rule out $L^{2}$ kernel of the model operator on hyperbolic space. For almost all the examples treated here, this hypothesis is equivalent to positive indicial radius (see Propositions , and , above). However, it is possible for (1.4) to fail even when the indicial radius is positive-an example is given by the Laplace-Beltrami operator on differential forms of degree $k$ on a manifold of dimension $2 k$, which is not Fredholm despite the fact that its indicial radius is $1 / 2$ (see $\left.\left.[3]^{1},\right]^{1}\right]$ and Lemma below). Thanks are due to Robin Graham for pointing out the significance of this example.

A word about the history of this monograph is in order. The result of Theorem was originally announced in preliminary form at an AMS meeting in 1991. Shortly after that meeting, I discovered a gap in the proof, and stopped work on the paper until I found a way to bridge the gap, sometime around 1998. By that time, administrative responsibilities kept me away from writing until early 2001. The first complete version of this monograph was posted on www.arxiv.org in May 2001; the present version is a minor modification of that one.

After this monograph was nearly finished, the beautiful monograph [15] by Olivier Biquard came to my attention. There is substantial overlap between the results of [15] and this monograph-in particular, Biquard proves a perturbation result for Einstein metrics similar to Theorem as well as many of the results of Theorem in the special case of Laplace operators, using methods very similar to those used here. (He also proves much more, extending many of the same results to Einstein metrics that are asymptotic to the complex, quaternionic, and octonionic hyperbolic metrics.) On the other hand, many of the results of this monograph are stronger than those of [15], notably the curvature assumptions of in Theorem and the boundary regularity of the resulting Einstein metrics.

In Chapter of this monograph, we give the main definitions, and describe special "Möbius coordinate charts" on an asymptotically hyperbolic manifold that relate the geometry to that of hyperbolic space. In Chapter we introduce our weighted Sobolev and Hölder spaces and prove some of their basic properties, and in Chapter we prove some basic mapping properties of geometric elliptic operators on these spaces. The core of the analysis begins in Chapter a detailed study of the Green kernels for elliptic geometric operators on hyperbolic space. This is then applied in Chapter to construct a parametrix for an arbitrary operator satisfying the hypotheses of Theorem C. Using this analysis, we prove Theorem and Proposition In Chapter we explore how these results apply in detail to Laplace operators, and prove Propositions D, D, and in Chapter we construct asymptotic solutions to (1.2) using a delicate procedure that does not lose any boundary regularity, and use these together with Theorem to prove Theorem

Among the many people to whom I am indebted for inspiration and good ideas while this work was in progress, I would particularly like to express my thanks to Lars Andersson, Piotr Chruściel, Robin Graham, Jim Isenberg, Rafe Mazzeo, Dan Pollack, and John Roth. I also would like to apologize to them and to all who expressed interest in this work for the long delay between the first announcement of these results and the appearance of this monograph. Finally, I am indebted to the referee for a number of useful suggestions.

\section*{CHAPTER 2}

\section*{Möbius Coordinates}

Let $\bar{M}$ be a smooth, compact, $(n+1)$-dimensional manifold-with-boundary, $n \geq 1$, and $M$ its interior. A defining function will mean a function $\rho: \bar{M} \rightarrow \mathbb{R}$ of class at least $C^{1}$ that is positive in $M$, vanishes on $\partial M$, and has nonvanishing differential everywhere on $\partial M$. We choose a fixed smooth defining function $\rho$ once and for all. For any $\varepsilon>0$, let $A_{\varepsilon} \subset M$ denote the open subset where $0<\rho<\varepsilon$.

A Riemannian metric $g$ on $M$ is said to be conformally compact of class $C^{l, \beta}$ for a nonnegative integer $l$ and $0 \leq \beta<1$ if for any smooth defining function $\rho$, the conformally rescaled metric $\rho^{2} g$ has a $C^{l, \beta}$ extension, denoted by $\bar{g}$, to a positive definite tensor field on $\bar{M}$. For such a metric $g$, the induced boundary metric $\widehat{g}:=\left.\bar{g}\right|_{T \partial M}$ is a $C^{l, \beta}$ Riemannian metric on $\partial M$ whose conformal class $[\widehat{g}]$ is independent of the choice of smooth defining function $\rho$; this conformal class is called the conformal infinity of $g$.

Throughout this monograph, we will use the Einstein summation convention, with Roman indices $i, j, k, \ldots$ running from 1 to $n+1$ and Greek indices $\alpha, \beta, \gamma, \ldots$ running from 1 to $n$. We indicate components of covariant derivatives of a tensor field by indices preceded by a semicolon, as in $u_{i j ; k l}$. In component calculations, we will always assume that a fixed conformally compact metric $g$ has been chosen, and all covariant derivatives and index raising and lowering operations will be understood to be with respect to $g$ unless otherwise specified, except that $\bar{g}^{i j}$ denotes the inverse of the metric $\bar{g}=\rho^{2} g$, not its raised-index version. Our convention for the components of the curvature tensor is chosen so that the Ricci tensor is given by the contraction $R_{i k}=R_{i j k}{ }^{j}$.

An important fact about conformally compact metrics is that their local geometry near the boundary looks asymptotically very much like that of hyperbolic space. Mazzeo $[39,40]$ showed, for example, that if $g$ is conformally compact of class at least $C^{2,0^{-}}$, then $g$ is complete and has sectional curvatures uniformly approaching $-|d \rho|^{2} \frac{2}{g}$ near $\partial M$. Thus, if $g$ is conformally compact of class $C^{l, \beta}$ with $l \geq 2$, and $|d \rho|_{\bar{g}}^{2}=1$ on $\partial M$, we say $g$ is asymptotically hyperbolic of class $C^{l, \beta}$.

In fact, the relationship with hyperbolic space can be made even more explicit by constructing special coordinate charts near the boundary. Throughout the rest of this chapter, we assume given a fixed metric $g$ on $M$ that is asymptotically hyperbolic of class $C^{l, \beta}$, with $l \geq 2$ and $0 \leq \beta<1$. Let $\bar{g}=\rho^{2} g$, a $C^{l, \beta}$ metric on $\bar{M}$, and let $\widehat{g}$ denote the restriction of $\bar{g}$ to $T \partial M$.

We begin by choosing a covering of a neighborhood of $\partial M$ in $\bar{M}$ by finitely many smooth coordinate charts $(\Omega, \Theta)$, where each coordinate map $\Theta$ is of the form $\Theta=(\theta, \rho)=\left(\theta^{1}, \ldots, \theta^{n}, \rho\right)$ and extends to a neighborhood of $\bar{\Omega}$ in $\bar{M}$. In keeping with our index convention, we will sometimes denote $\rho$ by $\theta^{n+1}$, and a symbol with a Roman index such as $\theta^{i}$ can refer to any of the coordinates $\theta^{1}, \ldots, \theta^{n}, \rho$.

We fix once and for all finitely many such charts covering a neighborhood $\mathscr{W}$ of $\partial M$ in $\bar{M}$. We will call any of these charts "background coordinates" for $\bar{M}$. By compactness, there is a positive number $c$ such that $A_{c} \subset \mathscr{W}$, and such that every point $p \in A_{c}$ is contained in a background coordinate chart containing a set of the form
$$\{(\theta, \rho):|\theta-\theta(p)|<c, 0 \leq \rho<c\} .$$

We will use two models of hyperbolic space, depending on context. In the upper half-space model, we regard hyperbolic space as the open upper half-space $\mathbb{H}=$ $\mathbb{H}^{n+1} \subset \mathbb{R}^{n+1}$, with coordinates $(x, y)=\left(x^{1}, \ldots, x^{n}, y\right)$, and with the hyperbolic metric $\breve{g}$ given in coordinates by $\breve{g}=y^{-2} \sum_{i}\left(d x^{i}\right)^{2}$. (As above, $x^{i}$ can denote any of the coordinates $x^{1}, \ldots, x^{n}, x^{n+1}=y$.) The other model is the Poincaré ball model, in which we regard hyperbolic space as the open unit ball $\mathbb{B}=\mathbb{B}^{n+1} \subset \mathbb{R}^{n+1}$, with coordinates $\left(\xi^{1}, \ldots, \xi^{n+1}\right)$, and with the hyperbolic metric (still denoted by $\breve{g}$ ) given by $\breve{g}=4(1-|\xi|)^{-2} \sum_{i}\left(d \xi^{i}\right)^{2}$, where $|\xi|$ denotes the Euclidean norm.

In this chapter, we will work exclusively with the upper half-space model. For any $r>0$, we let $B_{r} \subset \mathbb{H}$ denote the hyperbolic geodesic ball of radius $r$ about the point $(x, y)=(0,1)$ :
$$B_{r}=\left\{(x, y) \in \mathbb{H}: d_{\breve{g}}((x, y),(0,1))<r\right\} .$$
It is easy to check by direct computation that
$$B_{r} \subset\left\{(x, y):|x|<\sinh r, e^{-r}<y<e^{r}\right\},$$
where $|x|$ denotes the Euclidean norm of $x \in \mathbb{R}^{n}$.
If $p_{0}$ is any point in $A_{c / 8}$, choose such a background chart containing $p_{0}$, and define a map $\Phi_{p_{0}}: B_{2} \rightarrow M$, called a Möbius chart centered at $p_{0}$, by
$$(\theta, \rho)=\Phi_{p_{0}}(x, y)=\left(\theta_{0}+\rho_{0} x, \rho_{0} y\right),$$
where $\left(\theta_{0}, \rho_{0}\right)$ are the background coordinates of $p_{0}$. (It is more convenient in this context to consider a "chart" to be a mapping from $\mathbb{H} \subset \mathbb{R}^{n+1}$ into $M$, rather than from $M$ to $\mathbb{R}^{n+1}$ as is more common.) Because $\rho_{0}<c / 8$ and $e^{2}<8, \Phi_{p_{0}}$ maps $B_{2}$ diffeomorphically onto a neighborhood of $p_{0}$ in $A_{c}$. In these coordinates, $p_{0}$ corresponds to the point $(x, y)=(0,1) \in \mathbb{H}$. For each $0<r \leq 2$, let $V_{r}\left(p_{0}\right) \subset A_{c}$ be the neighborhood of $p_{0}$ defined by
$$V_{r}\left(p_{0}\right)=\Phi_{p_{0}}\left(B_{r}\right) .$$
We also choose finitely many smooth coordinate charts $\Phi_{i}: B_{2} \rightarrow M$ such that the sets $\left\{\Phi_{i}\left(B_{1}\right)\right\}$ cover a neighborhood of $M \backslash A_{c / 8}$, and such that each chart $\Phi_{i}$ extends smoothly to a neighborhood of $\bar{B}_{2}$. For consistency, we will also call these "Möbius charts."

The following lemma shows that the geometry of $(M, g)$ is uniformly bounded in Möbius charts.

Lemma 2.1. There exists a constant $C>0$ such that if $\Phi_{p_{0}}: B_{2} \rightarrow M$ is any Möbius chart,
$$\begin{aligned}
\left\|\Phi_{p_{0}}^{*} g-\breve{g}\right\|_{C^{l, \beta}\left(B_{2}\right)} & \leq C \\
\sup _{B_{2}}\left|\left(\Phi_{p_{0}}^{*} g\right)^{-1} \breve{g}\right| & \leq C
\end{aligned}$$
(The Hölder and sup norms in this estimate are the usual norms applied to the components of a tensor in coordinates; since $\bar{B}_{2}$ is compact, these are equivalent to the intrinsic Hölder and sup norms on tensors with respect to the hyperbolic metric.)

Proof. The estimate is immediate for the finitely many charts covering the interior of $M$, so we need only consider Möbius charts near the boundary. In background coordinates, $g$ can be written
$$g=\rho^{-2} \bar{g}_{i j}(\theta, \rho) d \theta^{i} d \theta^{j}$$
Pulling back to $\mathbb{H}$, we obtain
$$\begin{aligned}
\Phi_{p_{0}}^{*} g-\breve{g} & =\left(\rho_{0} y\right)^{-2} \bar{g}_{i j}\left(\theta_{0}+\rho_{0} x, \rho_{0} y\right) d\left(\rho_{0} x^{i}\right) d\left(\rho_{0} x^{j}\right)-y^{-2} \delta_{i j} d x^{i} d x^{j} \\
& =y^{-2}\left(\bar{g}_{i j}\left(\theta_{0}+\rho_{0} x, \rho_{0} y\right)-\delta_{i j}\right) d x^{i} d x^{j}
\end{aligned}$$
Since $y$ and $\delta_{i j}$ are smooth functions bounded above and below together with all derivatives on $\bar{B}_{2}$, it suffices to estimate $\bar{g}_{i j}\left(\theta_{0}+\rho_{0} x, \rho_{0} y\right)$. Our choice of background coordinates ensures that the eigenvalues of $\bar{g}_{i j}$ are uniformly bounded above and below by a global constant. Uniform estimates on the derivatives of $\Phi_{p_{0}}^{*} g$ follow from the fact that
$$\partial_{x^{i_{1}}} \cdots \partial_{x^{i_{m}}}\left(\Phi_{p_{0}}^{*} \bar{g}\right)_{i j}=\rho_{0}^{m} \Phi_{p_{0}}^{*}\left(\partial_{\theta^{i_{1}}} \cdots \partial_{\theta^{i_{m}}} \bar{g}_{i j}\right) .$$
Finally, an easy computation yields uniform Hölder estimates for the $l$ th derivatives of $\Phi_{p_{0}}^{*} g$. (See Lemma 6.1 below for a sharper estimate.) \(\square\)

The next lemma is a version of the well-known Whitney covering lemma adapted to the present situation.

Lemma 2.2. There exists a countable collection of points $\left\{p_{i}\right\} \subset M$ and corresponding Möbius charts $\Phi_{i}=\Phi_{p_{i}}: B_{2} \rightarrow V_{2}\left(p_{i}\right) \subset M$ such that the sets $\left\{V_{1}\left(p_{i}\right)\right\}$ cover $M$ and the sets $\left\{V_{2}\left(p_{i}\right)\right\}$ are uniformly locally finite: There exists an integer $N$ such that for each $i, V_{2}\left(p_{i}\right)$ has nontrivial intersection with $V_{2}\left(p_{j}\right)$ for at most $N$ values of $j$.

Proof. We only need to show that there exist points $\left\{p_{i}\right\} \subset A_{c / 8}$ such that $\left\{V_{1}\left(p_{i}\right)\right\}$ cover $A_{c / 8}$ and $\left\{V_{2}\left(p_{i}\right)\right\}$ are uniformly locally finite, for then we can choose finitely many additional charts for the interior without disturbing the uniform local finiteness.

By the preceding lemma, there are positive numbers $r_{0}<r_{1}$ such that each set $V_{1}(p)$ contains the $g$-geodesic ball of radius $r_{0}$ about $p$, and each set $V_{2}(p)$ is contained in the geodesic ball of radius $r_{1}$. Let $\left\{p_{i}\right\}$ be any maximal collection of points in $A_{c / 8}$ such that the open geodesic balls $\left\{B_{r_{0} / 2}\left(p_{i}\right)\right\}$ are disjoint. (Such a maximal collection exists by an easy application of Zorn's lemma.) If $p$ is any point in $A_{c / 8}$, by the maximality of the set $\left\{p_{i}\right\}, B_{r_{0} / 2}(p)$ must intersect at least one of the balls $B_{r_{0} / 2}\left(p_{i}\right)$ nontrivially, which implies that $p \in B_{r_{0}}\left(p_{i}\right) \subset V_{1}\left(p_{i}\right)$ by the triangle inequality. Therefore the sets $\left\{V_{1}\left(p_{i}\right)\right\}$ cover $A_{c / 8}$. To bound the number of sets $\left\{V_{2}\left(p_{i}\right)\right\}$ that can intersect, it suffices to bound the number of geodesic balls of radius $r_{1}$ around points $p_{i}$ that can intersect. Let $i$ be arbitrary and suppose $B_{r_{1}}\left(p_{j}\right) \cap B_{r_{1}}\left(p_{i}\right) \neq \varnothing$ for some $j$. By the triangle inequality again, $B_{r_{0} / 2}\left(p_{j}\right) \subset B_{2 r_{1}+r_{0} / 2}\left(p_{i}\right)$. Since $M$ has bounded sectional curvature, standard
volume comparison theorems (see, for example, [19, Theorems 3.7 and 3.9] yield uniform volume estimates
$$\operatorname{Vol}\left(B_{r_{0} / 2}\left(p_{j}\right)\right) \geq C_{1}, \quad \operatorname{Vol}\left(B_{2 r_{1}+r_{0} / 2}\left(p_{j}\right)\right) \leq C_{2} .$$
Since the sets $B_{r_{0} / 2}\left(p_{j}\right)$ are disjoint for different values of $j$, there can be at most $C_{2} / C_{1}$ such points $p_{j}$. \(\square\)

\section*{CHAPTER 3}

\section*{Function Spaces}

In this chapter, we will define weighted Sobolev and Hölder spaces of tensor fields that are well adapted to the geometry of asymptotically hyperbolic manifolds. Similar spaces have been defined by other authors; for some examples, see ${ }^{1}$, $22,24,291$.
$\bar{T}$ hroughout this chapter, we assume $\bar{M}$ is a connected smooth $(n+1)$-manifold, $g$ is a metric on $M$ that is asymptotically hyperbolic of class $C^{l, \beta}$, with $l \geq 2$ and $0 \leq \beta<1$, and $\rho$ is a fixed smooth defining function for $\partial M$. (It is easy to verify that choosing another smooth defining function will replace the norms we define below by equivalent ones, and will leave the function spaces unchanged.)

A geometric tensor bundle over $\bar{M}$ is a subbundle $E$ of some tensor bundle $T_{r_{2}}^{r_{1}} \bar{M}$ (tensors of covariant rank $r_{1}$ and contravariant rank $r_{2}$ ) associated to a direct summand (not necessarily irreducible) of the standard representation of $\mathrm{O}(n+1)$ (or $\mathrm{SO}(n+1)$ if $M$ is oriented) on tensors of type $\binom{r_{1}}{r_{2}}$ over $\mathbb{R}^{n+1}$. We will also use the same symbol $E$ to denote the restriction of this bundle to $M$. We define the weight of such a bundle $E \subset T_{r_{2}}^{r_{1}} \bar{M}$ to be $r=r_{1}-r_{2}$. The significance of this definition lies in the way tensor norms scale conformally: With $\bar{g}=\rho^{2} g$, an easy computation shows that
$$|T|_{g}=\rho^{r}|T|_{\bar{g}} \quad \text { for all } T \in T_{r_{2}}^{r_{1}} .$$

We begin by defining Hölder spaces of functions and tensor fields that are continuous up to the boundary. For $0 \leq \alpha<1$ and $k$ a nonnegative integer, we let $C_{(0)}^{k, \alpha}(\bar{M})$ denote the usual Banach space of functions on $\bar{M}$ with $k$ derivatives that are Hölder continuous of degree $\alpha$ up to the boundary in each background coordinate chart, with the obvious norm. (When $\alpha=0$, this is just the usual space of functions that are $k$ times continuously differentiable on $\bar{M}$.) If $s$ is a real number such that $0 \leq s \leq k+\alpha$, we define a subspace $C_{(s)}^{k, \alpha}(\bar{M}) \subset C_{(0)}^{k, \alpha}(\bar{M})$ by
$$C_{(s)}^{k, \alpha}(\bar{M})=\left\{u \in C_{(0)}^{k, \alpha}(\bar{M}): u=O\left(\rho^{s}\right)\right\} .$$
The next lemma gives some elementary properties of these spaces.
Lemma 3.1. Suppose $0 \leq \alpha<1$ and $0 \leq s \leq k+\alpha$.
\begin{itemize}
\item[(a)] $C_{(s)}^{k, \alpha}(\bar{M})=\left\{u \in C_{(0)}^{k, \alpha}(\bar{M}): \partial^{i} u /\left.\partial \rho^{i}\right|_{\partial M}=0\right.$ for $\left.0 \leq i<s\right\}$.
\item[(b)] $C_{(s)}^{k, \alpha}(\bar{M})$ is a closed subspace of $C_{(0)}^{k, \alpha}(\bar{M})$.
\item[(c)] If $j$ is a positive integer and $j-1<s \leq j \leq k$, then $C_{(s)}^{k, \alpha}(\bar{M})=C_{(j)}^{k, \alpha}(\bar{M})$.
\item[(d)] If $k<s \leq k+\alpha$, then $C_{(s)}^{k, \alpha}(\bar{M})=C_{(k+\alpha)}^{k, \alpha}(\bar{M})$.
\item[(e)] If $u \in C_{(s)}^{k, \alpha}(\bar{M})$ for $s \geq 1$, then any background coordinate derivative $\partial_{i} u$ is in $C_{(s-1)}^{k-1, \alpha}(\bar{M})$.
\end{itemize}
\begin{itemize}
\item[(f)] If $\delta$ is a positive real number such that $s+\delta \leq k+\alpha$, then $\rho^{\delta} C_{(s)}^{k, \alpha}(\bar{M}) \subset$ $C_{(s+\delta)}^{k, \alpha}(\bar{M})$.
\item[(g)] If $j$ is an integer such that $0<j \leq s$, then $\rho^{-j} C_{(s)}^{k, \alpha}(\bar{M}) \subset C_{(s-j)}^{k-j, \alpha}(\bar{M})$.
\end{itemize}

Proof. All of these claims are local, so we fix one background coordinate chart $(\theta, \rho)$ and do all of our computations there. Let $m$ be any nonnegative integer less than or equal to $k$. Applying the one-variable version of Taylor's formula to $u \in C_{(0)}^{k, \alpha}(\bar{M})$, we obtain
$$u(\theta, \rho)=\sum_{i=0}^{m-1} \frac{1}{i!} \rho^{i} \frac{\partial^{i} u}{\partial \rho^{i}}(\theta, 0)+\frac{1}{(m-1)!} \rho^{m} \int_{0}^{1}(1-t)^{m-1} \frac{\partial^{m} u}{\partial \rho^{m}}(\theta, t \rho) d t .$$
The integral above is easily shown to define a function of $(\theta, \rho)$ that is in $C_{(0)}^{k-m, \alpha}$ up to the boundary and agrees with $\partial^{m} u / \partial \rho^{m}$ on $\partial M$; therefore the last term in (3.1) is $O\left(\rho^{m}\right)$ in general, and if $\alpha>0$, it is $O\left(\rho^{m+\alpha}\right)$ if and only if $\partial^{m} u / \partial \rho^{m}$ vanishes on $\partial M$. Part $\left(e_{1}\right)$ follows easily from this, and $(\overrightarrow{\mathrm{b}}),(\mathrm{c})$, and $\left(\mathrm{e}_{1}\right)$ follow from $\binom{\mathrm{a}_{1}}{\mathrm{a}}$. Part $\binom{\text { th }}{\text { a }}$ is an immediate consequence of the definition, and $\binom{\text { g }}{\text { v }}$ follows by setting $m=j$ in (3.1) and multiplying through by $\rho^{-j}$. \(\square\)

Because of part $\left(\overline{b^{\prime}}\right)$ of this lemma, we can consider $C_{(s)}^{k, \alpha}(\bar{M})$ as a Banach space with the norm inherited from $C_{(0)}^{k, \alpha}(\bar{M})$.

If $E$ is a geometric tensor bundle over $\bar{M}$, we extend this definition to spaces of tensor fields by letting $C_{(s)}^{k, \alpha}(\bar{M} ; E)$ be the space of tensor fields whose components in each background coordinate chart are in $C_{(s)}^{k, \alpha}(\bar{M})$. All the claims of Lemma $\underline{\mathbf{3}_{-1}^{-1}}$ \(\square\) \(\square\) extend immediately to tensor fields. extend immediately to tensor fields.

Next we define some spaces of tensor fields over the interior manifold $M$ associated with the asymptotically hyperbolic metric $g$. Let us start with the Sobolev spaces, for which the definitions are a bit simpler. First, for $1<p<\infty$ and $k$ a nonnegative integer less than or equal to $l$, we define $H^{k, p}(M ; E)$ to be the usual (intrinsic) $L^{p}$ Sobolev space determined by the metric $g$ : That is, $H^{k, p}(M ; E)$ is the Banach space of all locally integrable sections $u$ of $E$ such that $\nabla^{j} u$ (interpreted in the distribution sense) is in $L^{p}\left(M ; E \otimes T^{j} M\right)$ for $0 \leq j \leq k$, with the norm
$$\|u\|_{k, p}=\left(\sum_{j=0}^{k} \int_{M}\left|\nabla^{j} u\right|^{p} d V_{g}\right)^{1 / p}$$
(Here $d V_{g}$ is the Riemannian density.) In the special case of $H^{0,2}(M ; E)=$ $L^{2}(M ; E)$, we will denote the norm $\|\cdot\|_{0,2}$ and its associated inner product simply by $\|\cdot\|$ and $(\cdot, \cdot)$, respectively. (We reserve the notations $|\cdot|_{g}$ and $\langle\cdot, \cdot\rangle_{g}$ for the pointwise norm and inner product on tensors.)

For each real number $\delta$, we define the weighted Sobolev space $H_{\delta}^{k, p}(M ; E)$ by
$$H_{\delta}^{k, p}(M ; E):=\rho^{\delta} H^{k, p}(M ; E)=\left\{\rho^{\delta} u: u \in H^{k, p}(M ; E)\right\}$$
with norm
$$\|u\|_{k, p, \delta}:=\left\|\rho^{-\delta} u\right\|_{k, p} .$$
These are easily seen to be Banach spaces, and $H_{\delta}^{k, 2}(M ; E)$ is a Hilbert space. Note that Hölder's inequality implies that when $1 / p+1 / p^{*}=1, H_{-\delta}^{0, p^{*}}(M ; E)$ is
naturally isomorphic to the dual space of $H_{\delta}^{0, p}(M ; E)$ under the $L^{2}$ pairing $(u, v)=$ $\int_{M}\langle u, v\rangle_{g} d V_{g}$.

The following lemma is elementary but often useful.
Lemma 3.2. Let $(M, g)$ be a conformally compact $(n+1)$-manifold, let $\rho$ be a defining function for $M$, and let $u$ be a continuous section of a natural tensor bundle $E$ of weight $r$ on $M$.
\begin{itemize}
\item[(a)] If $|u|_{g} \leq C \rho^{s}$ with $s$ real and greater than $\delta+n / p$, then $u \in H_{\delta}^{0, p}(M ; E)$.
\item[(b)] If $|u|_{g} \geq C \rho^{s}>0$ on the complement of a compact set, with $s \in \mathbb{R}$ and $s \leq \delta+n / p$, then $u \notin H_{\delta}^{0, p}(M ; E)$.
\item[(c)] If $u=\rho^{s} \bar{u}$, where $s \in \mathbb{C}$ and $\bar{u}$ is continuous on $\bar{M}$ and does not vanish identically on $\partial M$, then $u \in H_{\delta}^{0, p}(M ; E)$ if and only if $\operatorname{Re} s>\delta+n / p-r$.
\end{itemize}

Proof. Let $\bar{g}=\rho^{2} g$, which is a continuous Riemannian metric on $\bar{M}$. The lemma follows from the easily-verified facts that $\left|\rho^{s} \bar{u}\right|_{g}=\rho^{\operatorname{Re} s+r}|\bar{u}|_{\bar{g}}, d V_{g}=$ $\rho^{-n-1} d V_{\bar{g}}$, and $\int_{M} \rho^{s} d V_{g}<\infty$ if and only if $\operatorname{Re} s>n$. \(\square\)

Next we turn to the weighted Hölder spaces. To define Hölder norms for tensor fields on a manifold, one is always faced with the problem of comparing values of a tensor field at nearby points in order to make sense of quotients of the form $|u(x)-u(y)| / d(x, y)^{\alpha}$. There are various intrinsic ways to do this, such as parallel translating $u(x)$ along a geodesic from $x$ to $y$, or comparing the components of $u(x)$ and $u(y)$ in Riemannian normal coordinates centered at $x$; on a noncompact manifold, these can yield different spaces depending on the behavior of the metric near infinity. We will adopt a definition in terms of the Möbius coordinates constructed above which, though not obviously intrinsic to the geometry of $(M, g)$, has the advantage that estimates for elliptic operators in these norms follow very easily from standard local elliptic estimates in Möbius coordinates.

Let $\alpha$ be a real number such that $0 \leq \alpha<1$, and let $k$ be a nonnegative integer such that $k+\alpha \leq l+\beta$. For any tensor field $u$ with locally $C^{k, \alpha}$ coefficients, define the norm $\|u\|_{k, \alpha}$ by
$$\|u\|_{k, \alpha}:=\sup _{\Phi}\left\|\Phi^{*} u\right\|_{C^{k, \alpha}\left(B_{2}\right)}$$
where $\|v\|_{C^{k, \alpha}\left(B_{2}\right)}$ is just the usual Euclidean Hölder norm of the components of $v$ on $B_{2} \subset \mathbb{H}$, and the supremum is over all Möbius charts defined on $B_{2}$. Let $C^{k, \alpha}(M ; E)$ be the space of sections of $E$ for which this norm is finite. (We distinguish notationally between the Hölder and Sobolev norms as follows: A Greek subscript in the second position takes values in the interval [0, 1), and the notation $\|u\|_{k, \alpha}$ denotes a Hölder norm; a Roman subscript takes values in $(1, \infty)$, and the notation $\|u\|_{k, p}$ denotes a Sobolev norm. We will avoid the ambiguous cases $\alpha=1$ and $p=1$.) The corresponding weighted Hölder spaces are defined for $\delta \in \mathbb{R}$ by
$$C_{\delta}^{k, \alpha}(M ; E):=\rho^{\delta} C^{k, \alpha}(M ; E)=\left\{\rho^{\delta} u: u \in C^{k, \alpha}(M ; E)\right\}$$
with norms
$$\|u\|_{k, \alpha, \delta}:=\left\|\rho^{-\delta} u\right\|_{k, \alpha} .$$

If $U \subset M$ is a subset, the restricted norms are denoted by $\|\cdot\|_{k, p, \delta ; U}$ and $\|\cdot\|_{k, \alpha, \delta ; U}$, and the spaces $H_{\delta}^{k, p}(U ; E)$ and $C_{\delta}^{k, \alpha}(U ; E)$ are the spaces of sections over $U$ for which these norms are finite. When $E$ is the trivial line bundle (i.e. when the tensor fields in question are just scalar functions), we omit the bundle
from the notation: For example, $H^{k, p}(M)$ is the Sobolev space of scalar functions on $M$ with $k$ covariant derivatives in $L^{p}(M)$.

It is obvious from the definitions that $\rho^{\delta} \in C_{\delta}^{k, \alpha}(M)$ for every $k$. More importantly, we have the following lemma.

Lemma 3.3. If $0 \leq j \leq l$, then $\nabla^{j} \rho \in C_{1}^{l-j, \beta}\left(M ; T^{j} M\right)$.
Proof. From the definition of $C_{1}^{k, \beta}\left(M ; T^{j} M\right)$, we need to show for any Möbius chart $\Phi_{p_{0}}$ that the coefficients of $\Phi_{p_{0}}^{*}\left(\rho^{-1} \nabla^{j} \rho\right)$ are in $C^{l-j, \beta}\left(B_{2}\right)$, with norm bounded independently of $p_{0}$. Since $\Phi_{p_{0}}^{*} \rho=\rho\left(p_{0}\right) y$, this follows immediately from the coordinate expression for $\Phi_{p_{0}}^{*}\left(\rho^{-1} \nabla^{j} \rho\right)=y^{-1}\left(\nabla_{\Phi_{p_{0}}^{*} g}\right)^{j} y$ and the fact that the Christoffel symbols of $\Phi_{p_{0}}^{*} g$ in Möbius coordinates are uniformly bounded in $C^{l-1, \beta}\left(B_{2}\right)$. \(\square\)

We have defined the weighted spaces by multiplying the standard Sobolev and Hölder spaces by powers of $\rho$. In many circumstances, it is more convenient to use an alternative characterization in terms of weighted norms of covariant derivatives of $u$, as given in the following lemma.

Lemma 3.4. Let $u$ be a locally integrable section of a tensor bundle $E$ over an open subset $U \subset M$.
\begin{itemize}
\item[(a)] For $1<p<\infty$ and $0 \leq k \leq l, u \in H_{\delta}^{k, p}(U ; E)$ if and only if $\rho^{-\delta} \nabla^{j} u \in$ $L^{p}\left(U ; E \otimes T^{j} M\right)$ for $0 \leq j \leq k$, and the $H_{\delta}^{k, p}$ norm is equivalent to
$$\sum_{0 \leq j \leq k}\left\|\rho^{-\delta} \nabla^{j} u\right\|_{0, p ; U} .$$
\item[(b)] If $0 \leq \alpha<1$ and $0<k+\alpha \leq l+\beta, u \in C_{\delta}^{k, \alpha}(U ; E)$ if and only if $\rho^{-\delta} \nabla^{j} u \in C^{0, \alpha}\left(U ; E \otimes T^{j} M\right)$ for $0 \leq j \leq k$, and the $C_{\delta}^{k, \alpha}$ norm is equivalent to
$$\sum_{0 \leq j \leq k} \sup _{U}\left|\rho^{-\delta} \nabla^{j} u\right|+\left\|\rho^{-\delta} \nabla^{k} u\right\|_{0, \alpha ; U}$$
\end{itemize}

Proof. First consider part (A). By definition, $u \in H_{\delta}^{k, p}(U ; E)$ iff $\nabla^{j}\left(\rho^{-\delta} u\right) \in$ $L^{p}\left(U ; E \otimes T^{j} M\right)$ for $0 \leq j \leq k$. By the product rule and induction, we can write
$$\nabla^{j}\left(\rho^{-\delta} u\right)=\rho^{-\delta} \sum_{\substack{0 \leq i \leq j \\ i+j_{1}+\cdots+j_{p}=j}} C\left(\delta, i, j_{1}, \ldots, j_{p}\right) \nabla^{i} u \otimes \frac{\nabla^{j_{1}} \rho}{\rho} \otimes \ldots \otimes \frac{\nabla^{j_{p}} \rho}{\rho},$$
where $C\left(\delta, i, j_{1}, \ldots, j_{p}\right)$ is a constant, equal to 1 when $i=j$. Since, by the preceding lemma, $\left|\nabla^{j} \rho\right| / \rho$ is bounded as long as $j \leq l$, the result follows easily by induction.

For part (b), the case $\delta=0$ follows by inspecting the coordinate expression for $\nabla^{j} u$ in Möbius coordinates, recalling that the Christoffel symbols of $g$ are uniformly bounded in $C^{l-1, \beta}$ in these coordinates. The general case follows as above from (3.3) and the fact that $\nabla^{j} \rho / \rho \in C^{l-j, \beta}\left(U ; T^{j} M\right)$. \(\square\)

It follows from Lemma 2.1 that the norm $\|\cdot\|_{k, 0}$ is equivalent to the usual intrinsic $C^{k}$ norm $\sum_{0 \leq i \leq k} \sup _{M}\left|\nabla^{i} u\right|$ for $0 \leq k \leq l$. Moreover, if $\Phi$ and $\widetilde{\Phi}$ are any Möbius charts whose images intersect, the overlap map $\Phi^{-1} \circ \widetilde{\Phi}$ induces an isomorphism on the space $C^{l, \beta}(U)$ on its domain of definition $U$, with norm bounded by a uniform constant. Therefore, for $0 \leq k+\alpha \leq l+\beta$, it is immediate that the pullback
by any Möbius chart induces isomorphisms on the unweighted Hölder spaces, with norms bounded above and below by constants independent of $i$. Moreover, if $\Phi_{i}$ is a Möbius chart centered at $p_{i}, \Phi_{i}^{*} \rho=\rho\left(p_{i}\right) y$, which is uniformly bounded above and below on $B_{2}$ by constant multiples of $\rho\left(p_{i}\right)$. Therefore the weighted norms scale as follows: for any $r \leq 2$,
$$C^{-1} \rho\left(p_{i}\right)^{-\delta}\left\|\Phi_{i}^{*} u\right\|_{k, \alpha ; B_{r}} \leq\|u\|_{k, \alpha, \delta ; V_{r}\left(p_{0}\right)} \leq C \rho\left(p_{i}\right)^{-\delta}\left\|\Phi_{i}^{*} u\right\|_{k, \alpha ; B_{r}} .$$
Similarly, it follows directly from Lemma that
$$C^{-1} \rho\left(p_{i}\right)^{-\delta}\left\|\Phi_{i}^{*} u\right\|_{k, p ; B_{r}} \leq\|u\|_{k, p, \delta ; V_{r}\left(p_{0}\right)} \leq C \rho\left(p_{i}\right)^{-\delta}\left\|\Phi_{i}^{*} u\right\|_{k, p ; B_{r}} .$$
The next lemma is a strengthening of this.
Lemma 3.5. Suppose $\left\{\Phi_{i}=\Phi_{p_{i}}\right\}$ is a uniformly locally finite cover of $M$ by Möbius charts as in Lemma 2.2. Then we have the following norm equivalences for any $r$ with $1 \leq r \leq 2$ :
$$\begin{aligned}
& C^{-1} \sum_{i} \rho\left(p_{i}\right)^{-\delta}\left\|\Phi_{i}^{*} u\right\|_{k, p ; B_{r}} \leq\|u\|_{k, p, \delta} \leq C \sum_{i} \rho\left(p_{i}\right)^{-\delta}\left\|\Phi_{i}^{*} u\right\|_{k, p ; B_{r}}, \\
& C^{-1} \sup _{i} \rho\left(p_{i}\right)^{-\delta}\left\|\Phi_{i}^{*} u\right\|_{k, \alpha ; B_{r}} \leq\|u\|_{k, \alpha, \delta} \leq C \sup _{i} \rho\left(p_{i}\right)^{-\delta}\left\|\Phi_{i}^{*} u\right\|_{k, \alpha ; B_{r}},
\end{aligned}$$

Proof. If $\Phi_{i}$ is a Möbius chart centered at $p_{i}, \Phi_{i}^{*} \rho=\rho\left(p_{i}\right) y$, which is uniformly bounded above and below by constant multiples of $\rho\left(p_{i}\right)$. Thus if $u \in H_{\delta}^{k, p}(M ; E)$, (3.5) yields
$$\begin{aligned}
\sum_{i} \rho\left(p_{i}\right)^{-\delta}\left\|\Phi_{i}^{*} u\right\|_{k, p ; B_{r}} & \leq C \sum_{i}\left\|\Phi_{i}^{*}\left(\rho^{-\delta} u\right)\right\|_{k, p ; B_{r}} \\
& \leq C^{\prime} \sum_{i}\left\|\rho^{-\delta} u\right\|_{k, p ; V_{r}\left(p_{i}\right)} \\
& \leq C^{\prime} N\left\|\rho^{-\delta} u\right\|_{k, p} \\
& =C^{\prime} N\|u\|_{k, p, \delta}
\end{aligned}$$
where $N$ is an upper bound on the number of sets $V_{2}\left(p_{i}\right)$ that can intersect nontrivially. Conversely, if $\sum_{i} \rho\left(p_{i}\right)^{-\delta}\left\|\Phi_{i}^{*} u\right\|_{k, p ; B_{r}}$ is finite, then
$$\begin{aligned}
\|u\|_{k, p, \delta} & \leq \sum_{i}\left\|\rho^{-\delta} u\right\|_{k, p ; V_{r}\left(p_{i}\right)} \\
& \leq C \sum_{i}\left\|\Phi_{i}^{*}\left(\rho^{-\delta} u\right)\right\|_{k, p ; B_{r}} \\
& \leq C^{\prime} \sum_{i} \rho\left(p_{i}\right)^{-\delta}\left\|\Phi_{i}^{*} u\right\|_{k, p ; B_{r}} .
\end{aligned}$$
The argument for the Hölder case is similar but simpler, because we do not need the uniform local finiteness in that case. \(\square\)

The following results follow easily from Lemma together with standard facts about Sobolev and Hölder spaces on $B_{r} \subset \mathbb{H}$, so the proofs are left to the reader (cf. [29, 7]).

Lemma 3.6. Let $U$ be any open subset of $M$, and let $E, E_{1}, E_{2}$ be geometric tensor bundles over $M$.
\begin{itemize}
\item[(a)] If $1<p<\infty, 0 \leq \alpha<1, \delta, \delta^{\prime} \in \mathbb{R}, 0 \leq k+\alpha \leq l+\beta$, and $1 \leq k^{\prime}+\alpha \leq l+\beta$, the pointwise tensor product induces continuous maps
$$\begin{aligned}
C_{\delta}^{k, \alpha}\left(U ; E_{1}\right) \times H_{\delta^{\prime}}^{k, p}\left(U ; E_{2}\right) & \rightarrow H_{\delta+\delta^{\prime}}^{k, p}\left(U ; E_{1} \otimes E_{2}\right) \\
C_{\delta}^{k^{\prime}, \alpha}\left(U ; E_{1}\right) \times C_{\delta^{\prime}}^{k^{\prime}, \alpha}\left(U ; E_{2}\right) & \rightarrow C_{\delta+\delta^{\prime}}^{k^{\prime}, \alpha}\left(U ; E_{1} \otimes E_{2}\right)
\end{aligned}$$
\item[(b)] If $1<p, p^{\prime}<\infty, 0 \leq \alpha<1$, and $0 \leq k+\alpha \leq l+\beta$, we have continuous inclusions:
$$\begin{array}{rrr}
H_{\delta}^{k, p}(U ; E) & \hookrightarrow H_{\delta^{\prime}}^{k, p^{\prime}}(U ; E), & p \geq p^{\prime}, \\
C_{\delta}^{k, \alpha}(U ; E) & \hookrightarrow+H_{\delta^{\prime}}^{k, p^{\prime}}(U ; E), & \delta+\frac{n}{p}>\delta^{\prime}+\frac{n}{p^{\prime}} ; \\
& \delta>\delta^{\prime}+\frac{n}{p^{\prime}} .
\end{array}$$
\item[(c)] (Sobolev embedding) If $1<p<\infty, 0<\alpha<1,1 \leq k \leq l, k+\alpha \leq l+\beta$, and $\delta \in \mathbb{R}$, we have continuous inclusions
$$\begin{array}{ll}
H_{\delta}^{k, p}(U ; E) \hookrightarrow C_{\delta}^{j, \alpha}(U ; E), & k-\frac{n+1}{p} \geq j+\alpha, \\
H_{\delta}^{k, p}(U ; E) \hookrightarrow H_{\delta}^{j, p^{\prime}}(U ; E), & k-\frac{n+1}{p} \geq j-\frac{n+1}{p^{\prime}} .
\end{array}$$
\item[(d)] (Rellich lemma) If $1<p<\infty, 0<\alpha<1,0 \leq k \leq l$, and $0<j+\alpha \leq$ $l+\beta$, then the following inclusions are compact operators:
$$\begin{array}{lll}
H_{\delta}^{k, p}(M ; E) & \hookrightarrow H_{\delta^{\prime}}^{k^{\prime}, p}(M ; E), & k>k^{\prime}, \\
C_{\delta}^{j, \alpha}(M ; E) & \quad, \quad C_{\delta^{\prime}}^{j^{\prime}, \alpha}(M ; E), & j>j^{\prime}, \\
\delta>\delta^{\prime} .
\end{array}$$
\end{itemize}

The following relationships between the Hölder spaces on $M$ and those on $\bar{M}$ will play an important role in Chapter

Lemma 3.7. Let $E$ be a geometric tensor bundle of weight $r$ over $\bar{M}$, and suppose $0<\alpha<1,0<k+\alpha \leq l+\beta$, and $0 \leq s \leq k+\alpha$. The following inclusions are continuous.
\begin{itemize}
\item[(a)] $C_{(s)}^{k, \alpha}(\bar{M} ; E) \hookrightarrow C_{s+r}^{k, \alpha}(M ; E)$.
\item[(b)] $C_{k+\alpha+r}^{k, \alpha}(M ; E) \hookrightarrow C_{(0)}^{k, \alpha}(\bar{M} ; E)$.
\end{itemize}

Proof. We will prove $\left(a_{1}\right)$ by induction on $k$. Suppose $k=0$, and consider first the case of scalar functions, so that $E$ is the trivial line bundle. By Lemma $3.1(\mathrm{cl})$ there are only two distinct cases: $s=0$ and $s=\alpha$. For $s=0$, let $\Phi_{p_{0}}$ be a Möbius chart and let ( $\rho_{0}, \theta_{0}$ ) be the background coordinates of $p_{0}$. We estimate
$$\begin{aligned}
\left|\Phi_{p_{0}}^{*} u(x, y)\right| & \leq \sup _{M}|u| \\
& \leq\|u\|_{C_{(0)}^{0, \alpha}(\bar{M})} . \\
\left|\Phi_{p_{0}}^{*} u(x, y)-\Phi_{p_{0}}^{*} u\left(x^{\prime}, y^{\prime}\right)\right| & =\left|u\left(\theta_{0}+\rho_{0} x, \rho_{0} y\right)-u\left(\theta_{0}+\rho_{0} x^{\prime}, \rho_{0} y^{\prime}\right)\right| \\
& \leq\|u\|_{C_{(0)}^{0, \alpha}(\bar{M})}\left|\left(\rho_{0} x, \rho_{0} y\right)-\left(\rho_{0} x^{\prime}, \rho_{0} y^{\prime}\right)\right|^{\alpha} \\
& \leq\|u\|_{C_{(0)}^{0, \alpha}(\bar{M})} \rho_{0}^{\alpha}\left|(x, y)-\left(x^{\prime}, y^{\prime}\right)\right|^{\alpha} .
\end{aligned}$$
Since $\rho_{0}^{\alpha}$ is uniformly bounded on $M$, the result follows.
When $s=\alpha$, we need to show that $\Phi_{p_{0}}^{*}\left(\rho^{-\alpha} u\right)$ is uniformly bounded in $C^{0, \alpha}\left(B_{2}\right)$. The Hölder estimate for $u$ in background coordinates, together with
the fact that $u$ vanishes on $\partial M$, shows that
$$|u(\theta, \rho)| \leq\|u\|_{C_{(0)}^{0, \alpha}(\bar{M})} \rho^{\alpha}$$
near $\partial M$, from which the zero-order estimate
$$\left|\Phi_{p_{0}}^{*}\left(\rho^{-\alpha} u\right)\right| \leq C\|u\|_{C_{(0)}^{0, \alpha}(\bar{M})}$$
follows immediately. The Hölder estimate is proved by noting that $\Phi_{p_{0}}^{*}\left(\rho^{-\alpha} u\right)=$ $y^{-\alpha} \rho_{0}^{-\alpha} \Phi_{p_{0}}^{*} u$; since $y^{-\alpha}$ is uniformly bounded together with all derivatives on $B_{2}$, it suffices to show that $\rho_{0}^{-\alpha} \Phi_{p_{0}}^{*} u$ is uniformly bounded in $C^{0, \alpha}\left(B_{2}\right)$. This is proved as follows:
$$\begin{aligned}
\left|\rho_{0}^{-\alpha} \Phi_{p_{0}}^{*} u(x, y)-\rho_{0}^{-\alpha} \Phi_{p_{0}}^{*} u\left(x^{\prime}, y^{\prime}\right)\right| & =\rho_{0}^{-\alpha}\left|u\left(\theta_{0}+\rho_{0} x, \rho_{0} y\right)-u\left(\theta_{0}+\rho_{0} x, \rho_{0} y\right)\right| \\
& \leq \rho_{0}^{-\alpha}\|u\|_{(0)}^{0, \alpha}(\bar{M})\left|\left(\rho_{0} x, \rho_{0} y\right)-\left(\rho_{0} x, \rho_{0} y\right)\right|^{\alpha} \\
& =\|u\|_{(0)}^{0, \alpha}(\bar{M})\left|(x, y)-\left(x^{\prime}, y^{\prime}\right)\right|^{\alpha} .
\end{aligned}$$

Now let $E$ be a tensor bundle of type $\binom{p}{q}$ (and thus of weight $r=p-q$ ). In any background coordinate domain $\Omega$, basis tensors of the form $d \theta^{i_{1}} \otimes \cdots \otimes d \theta^{i_{p}} \otimes$ $\partial_{\theta^{j_{1}}} \otimes \cdots \otimes \partial_{\theta_{j_{q}}}$ are easily seen to be uniformly bounded in $C_{r}^{l, \beta}(\Omega ; E)$. Since any $u \in C_{(s)}^{0, \alpha}(\bar{M} ; E)$ can be written locally as a linear combination of such tensors multiplied by functions in $C_{(s)}^{0, \alpha}(\Omega)$, the result follows from the scalar case together with Lemma 3.6 (a).

Now suppose $1<k+\alpha \leq l+\beta$ and $0 \leq s \leq k+\alpha$, and assume claim ( true for $C_{\left(s_{0}\right)}^{k_{0}, \alpha}(\bar{M} ; E)$ when $0 \leq k_{0}<k$ and $0 \leq s_{0} \leq k_{0}+\alpha$. If $u \in C_{(s)}^{k, \alpha}(\bar{M} ; E)$, then $|u|_{g}=\rho^{r}|u|_{\bar{g}}=O\left(\rho^{s+r}\right)$ by definition, so it suffices to prove that $\nabla u \in$ $C_{s+r}^{k-1, \alpha}\left(M ; E \otimes T^{*} M\right)$ with norm bounded by $\|u\|_{C_{(s)}^{k, \alpha}(\bar{M} ; E)}$. If $D=\nabla-\bar{\nabla}$ denotes the difference tensor between the Levi-Civita connections of $g$ and $\bar{g}$, a computation shows that $D$ is the 3-tensor whose components are given in any coordinates by
$$D_{i j}^{k}=-\rho^{-1}\left(\delta_{i}^{k} \partial_{j} \rho+\delta_{j}^{k} \partial_{i} \rho-\bar{g}^{k l} \bar{g}_{i j} \partial_{l} \rho\right) .$$
Working in background coordinates, we find that $\rho D u \in C_{(s)}^{k, \alpha}\left(M ; E \otimes T^{*} M\right)$ since the coefficients of $\rho D$ are in $C_{(0)}^{l, \beta}(\bar{M})$. Since $\bar{\nabla} u \in C_{(s-1)}^{k-1, \alpha}\left(M ; E \otimes T^{*} M\right)$ by Lemma 3.1(e), we use Lemma 3.1(w) to conclude that
$$\begin{aligned}
\rho \nabla u & =\rho \bar{\nabla} u+\rho D u \\
& \in \rho C_{(s-1)}^{k-1, \alpha}\left(\bar{M} ; E \otimes T^{*} M\right)+C_{(s)}^{k, \alpha}\left(\bar{M} ; E \otimes T^{*} M\right) \\
& \subset C_{(s)}^{k-1, \alpha}\left(\bar{M} ; E \otimes T^{*} M\right)
\end{aligned}$$
with norm bounded by a multiple of $\|u\|_{C_{(s)}^{k, \alpha}(\bar{M} ; E)}$. Therefore, since $\rho \nabla u$ is a tensor field of weight $r+1$, the inductive hypothesis implies that $\rho \nabla u \in C_{s+r+1}^{k-1, \alpha}(M ; E \otimes$ $T^{*} M$ ), which implies in turn that $\nabla u \in C_{s+r}^{k-1, \alpha}\left(M ; E \otimes T^{*} M\right)$ as desired.

For part ( ), we begin with the scalar case, and proceed by induction on $k$. Let $k=0$, and suppose $u \in C_{\alpha}^{0, \alpha}(M)$. Given any Möbius chart $\Phi_{p_{0}}: B_{2} \rightarrow V_{2}\left(p_{0}\right)$, let $\left(\theta_{0}, \rho_{0}\right)$ be the background coordinates of $p_{0}$, and let $v$ be the function $\Phi^{*}\left(\rho^{-\alpha} u\right)$ on $B_{2}$, so that
$$u(\theta, \rho)=\rho^{\alpha} v\left(\left(\theta-\theta_{0}\right) / \rho_{0}, \rho / \rho_{0}\right) .$$

The hypothesis means that $v \in C^{0, \alpha}\left(B_{2}\right)$, with norm bounded by $\|u\|_{0, \alpha, \alpha}$. For $(\theta, \rho) \in V_{2}\left(p_{0}\right)$, we estimate
$$|u(\theta, \rho)|=\left|\rho^{\alpha} v\left(\left(\theta-\theta_{0}\right) / \rho_{0}, \rho / \rho_{0}\right)\right| \leq \rho^{\alpha}\|u\|_{0, \alpha, \alpha} .$$
Since $\rho$ is bounded above on $M$, this shows in particular that $\sup |u|$ is bounded by a multiple of $\|u\|_{0, \alpha, \alpha}$. Similarly, if $(\theta, \rho)$ and $\left(\theta^{\prime}, \rho^{\prime}\right)$ are in $V_{2}\left(p_{0}\right)$, we have
$$\begin{aligned}
\left|u(\theta, \rho)-u\left(\theta^{\prime}, \rho^{\prime}\right)\right|= & \left|\rho^{\alpha} v\left(\left(\theta-\theta_{0}\right) / \rho_{0}, \rho / \rho_{0}\right)-\rho^{\prime \alpha} v\left(\left(\theta^{\prime}-\theta_{0}\right) / \rho_{0}, \rho^{\prime} / \rho_{0}\right)\right| \\
\leq & \rho^{\alpha}\left|v\left(\left(\theta-\theta_{0}\right) / \rho_{0}, \rho / \rho_{0}\right)-v\left(\left(\theta^{\prime}-\theta_{0}\right) / \rho_{0}, \rho^{\prime} / \rho_{0}\right)\right| \\
& \quad+\left(\rho^{\alpha}-\rho^{\prime \alpha}\right)\left|v\left(\left(\theta^{\prime}-\theta_{0}\right) / \rho_{0}, \rho^{\prime} / \rho_{0}\right)\right| \\
\leq & C\|u\|_{0, \alpha, \alpha}\left|(\theta, \rho)-\left(\theta^{\prime}, \rho^{\prime}\right)\right|^{\alpha} .
\end{aligned}$$

To complete the $k=0$ case, it suffices to extend ( 0.12 ) to any $(\theta, \rho)$ and $\left(\theta^{\prime}, \rho^{\prime}\right)$ that lie in the same background chart, for then $u$ extends continuously to the boundary as an element of $C_{(0)}^{0, \alpha}(\bar{M})$. Note that there is a real number $\gamma \in(1,2)$ such that whenever $\left|(\theta, \rho)-\left(\theta^{\prime}, \rho^{\prime}\right)\right| \leq \gamma \rho$, the points $(\theta, \rho)$ and $\left(\theta^{\prime}, \rho^{\prime}\right)$ lie in the image of the same Möbius chart. We estimate as follows:
$$\left|u(\theta, \rho)-u\left(\theta^{\prime}, \rho^{\prime}\right)\right| \leq\left|u(\theta, \rho)-u\left(\theta^{\prime}, \rho\right)\right|+\left|u\left(\theta^{\prime}, \rho\right)-u\left(\theta^{\prime}, \rho^{\prime}\right)\right| .$$
For the first term, the case in which $\left|\theta-\theta^{\prime}\right| \leq \gamma \rho$ is taken care of by (3.12). On the other hand, if $\left|\theta-\theta^{\prime}\right| \geq \gamma \rho$,
$$\begin{aligned}
\left|u(\theta, \rho)-u\left(\theta^{\prime}, \rho\right)\right| & \leq|u(\theta, \rho)|+\left|u\left(\theta^{\prime}, \rho\right)\right| \\
& \leq 2 \rho^{\alpha}\|u\|_{0, \alpha, \alpha} \\
& \leq 2 \gamma^{-\alpha}\|u\|_{0, \alpha, \alpha}\left|\theta-\theta^{\prime}\right|^{\alpha} \\
& \leq C\|u\|_{0, \alpha, \alpha}\left|(\theta, \rho)-\left(\theta^{\prime}, \rho^{\prime}\right)\right|^{\alpha} .
\end{aligned}$$
To estimate the second term of $(3.1)$, let $N$ be a positive integer such that $\rho^{\prime}$ lies in the interval $\left[\gamma^{N} \rho, \gamma^{N+1} \rho\right]$. Then, since $\left(\theta^{\prime}, \gamma^{i} \rho\right)$ and $\left(\theta^{\prime}, \gamma^{i+1} \rho\right)$ lie in the image of a single Möbius chart, as do $\left(\theta^{\prime}, \gamma^{N} \rho\right)$ and $\left(\theta^{\prime}, \rho^{\prime}\right)$, (3.12') gives
$$\begin{aligned}
\left|u\left(\theta^{\prime}, \rho^{\prime}\right)-u\left(\theta^{\prime}, \rho\right)\right| & \leq\left|u\left(\theta^{\prime}, \rho^{\prime}\right)-u\left(\theta^{\prime}, \gamma^{N} \rho\right)\right|+\sum_{i=0}^{N-1}\left|u\left(\theta^{\prime}, \gamma^{i+1} \rho\right)-u\left(\theta^{\prime}, \gamma^{i} \rho\right)\right| \\
& \leq C\|u\|_{0, \alpha, \alpha}\left(\left|\rho^{\prime}-\gamma^{N} \rho\right|^{\alpha}+\sum_{i=0}^{N-1}\left|\gamma^{i+1} \rho-\gamma^{i} \rho\right|^{\alpha}\right) \\
& =C\|u\|_{0, \alpha, \alpha}\left(\left|\rho^{\prime}-\gamma^{N} \rho\right|^{\alpha}+(\gamma-1)^{\alpha} \rho^{\alpha} \sum_{i=0}^{N-1} \gamma^{\alpha i}\right) \\
& =C\|u\|_{0, \alpha, \alpha}\left(\left|\rho^{\prime}-\gamma^{N} \rho\right|^{\alpha}+(\gamma-1)^{\alpha} \rho^{\alpha} \frac{\gamma^{\alpha N}-1}{\gamma^{\alpha}-1}\right) \\
& \leq C^{\prime}\|u\|_{0, \alpha, \alpha}\left(\left|\rho^{\prime}-\gamma^{N} \rho\right|^{\alpha}+\left|\gamma^{N} \rho-\rho\right|^{\alpha}\right)
\end{aligned}$$
where the last inequality follows from the fact that $\gamma^{\alpha N}-1 \leq C\left(\gamma^{N}-1\right)^{\alpha}$ when $N \geq 1$. Since both terms in parentheses above are bounded by $\left|\rho-\rho^{\prime}\right|^{\alpha}$ and thus by $\left|(\theta, \rho)-\left(\theta^{\prime}, \rho^{\prime}\right)\right|^{\alpha}$, this completes the argument for the $k=0$ case. (I am indebted to Eric Bahuaud for pointing out a gap in an earlier version of this proof, and providing helpful suggestions for fixing it.)