---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Einstein deformations of Kähler Einstein metrics]

---
source_file: 2603_09028.pdf
converter: mathpix
format: mmd
---

\title{
EINSTEIN DEFORMATIONS OF KÄHLER EINSTEIN METRICS
}

\author{
PAUL-ANDI NAGY
}

\begin{abstract}
We study Einstein deformations of negative Kähler Einstein metrics. We relate the second order Einstein deformation theory of negative Kähler-Einstein metrics to the complex geometry of the underlying Kähler manifold. After suitable gauge normalisation we show that the Taylor expansion to order two of an Einstein deformation tangent to $h_{1}$ in the infinitesimal deformation space is fully determined by $h_{1}^{2}$ and the divergence of the Kodaira-Spencer bracket $\left[h_{1}, h_{1}\right]^{c}$. This substantially refines and extends recent results of Nagy-Semmelmann which state that Einstein deformations for negative Kähler-Einstein metrics are unobstructed to second order.
\end{abstract}

2020 Mathematics Subject Classification: Primary 32Q20; Secondary 53C26, 53C35, 53C15. Keywords: Einstein deformation, gauge normalisation to second order, negative Kähler-Einstein metrics.

\section*{Contents}
1. Introduction ..... 2
1.1. Background and motivation ..... 2
1.2. Main results ..... 3
1.3. Key arguments and outline of proofs for Kähler metrics ..... 5
Acknowledgments ..... 5
2. Preliminaries ..... 5
2.1. The Frölicher-Nijenhuis bracket ..... 7
3. Bianchi map normalisation to second order ..... 8
3.1. Role of the trace ..... 8
3.2. Proof of normalisation to second order ..... 11
4. Negative Kähler-Einstein metrics ..... 13
4.1. Elements of Kähler geometry ..... 13
4.2 Type decomposition of $[\cdot, \cdot]^{\text {FN }}$ and the Kodaira-Spencer bracket ..... 16
4.3. Structure of the operator v ..... 20

\footnotetext{
Date: March 11, 2026.
}

\section*{1. Introduction}
1.1. Background and motivation. Let $(M, g)$ be a compact Riemanian manifold where the metric $g$ is assumed to be Einstein i.e. ric ${ }^{g}=E g$ for some $E$ in $\mathbb{R}$. We study the existence problem for Einstein deformations of $g$, that is curves $g_{t}$ of Riemannian metrics defined for short time $t$ such that $g_{0}=g$ and ric ${ }^{g_{t}}=E g_{t}$. In addition we normalise such deformations to have fixed volume i.e. $g_{t} \in \mathscr{M}_{1}$ where the latter space indicates the space of Riemannian metrics on $M$ having the same volume as $g$. A detailed exposition of the current state of the art of the Einstein deformations problem can be found in [13]; here we only recall a few facts relevant to this work.

The approach consists in considering the Taylor series expansion $g^{-1} g_{t}=\mathrm{id}+\sum_{n \geqslant 1} \frac{t^{n}}{n!} h_{n}$ at $t=0$ and differentiating the Einstein equation ric ${ }^{g_{t}}=E g_{t}$ with respect to $t$. At first order this yields
$$h_{1} \in \mathscr{E}(M, g)$$
where the infinitesimal deformation space $\mathscr{E}(M, g):=\left\{h \in \operatorname{ker} \Delta_{E}: \delta^{g} h=0\right.$ and $\left.\operatorname{tr}(h)=0\right\}$ and where $\Delta_{E}$ denotes the Einstein operator acting on symmetric 2-tensors. In case the space $\mathscr{E}(M, g)$ vanishes identically, the metric $g$ is rigid, in the sense of being isolated in the moduli space of Einstein metrics [3].

Currently there is a good understanding and descriptions of $\mathscr{E}(M, g)$ for large classes of metrics; the list includes symmetric spaces (see [13] for an overview), Kähler [7], nearly-Kähler [10] and squashed 3-sasaki structures [11]. See also [9] for the case of homogeneous spaces and [14] for a discussion of the basic (with respect to the Reeb foliation) piece in $\mathscr{E}(M, g)$ for Sasaki-Einstein metrics.

There are further obstructions on tensor $h_{1}$ as showed by Koiso [6]; indeed one must have $\int_{M} P\left(h_{1}\right) \mathrm{vol}=0$ where
$$2 P\left(h_{1}\right):=3 g\left(\nabla_{e_{i}, h e_{i}}^{2} h_{1}, h_{1}\right)-6 g\left(\left(\nabla_{e_{i}, e_{j}}^{2} h_{1}\right) h_{1} e_{i}, h_{1} e_{j}\right)+2 E \operatorname{tr}\left(h_{1}^{3}\right) .$$
This obstruction was used for the first time in [1] in order to show that the bi-invariant Einstein metric on $\operatorname{SU}(2 n+1)$ is rigid. A systematic approach to deriving the second order Einstein equation was undertaken in [12]; we have observed that the theory is governed by a second order differential operator build from the Frölicher-Nijenhuis bracket $[\cdot, \cdot]^{\text {FN }}$ on symmetric two tensors. Consider the operator $\mathbf{v}: \Gamma\left(\operatorname{Sym}^{2} T M\right) \oplus \Gamma\left(\operatorname{Sym}^{2} T M\right) \rightarrow \Gamma\left(\operatorname{Sym}^{2} T M\right)$ determined from
$$\left\langle\mathbf{v}\left(h_{1}, h_{2}\right), h_{3}\right\rangle_{L^{2}}=\mathfrak{S}_{a b c}\left\langle\delta^{g}\left[h_{a}, h_{b}\right]^{\mathrm{FN}}, h_{c}\right\rangle_{L^{2}}$$
where $\mathfrak{S}$ indicates the cyclic sum.
Theorem 1.1. [12][Theorems 3.13 and 4.3] The Einstein equation to second order is given by
$$\widetilde{\Delta}_{E}\left(h_{2}-\frac{3}{2} h_{1}^{2}\right)=-\mathbf{v}\left(h_{1}, h_{1}\right)+E h_{1}^{2}+\frac{1}{2} \delta^{\star g} \operatorname{tr}\left(h_{1}^{2}\right) .$$
In particular the obstruction to second order deformation reads
$$-\mathbf{v}\left(h_{1}, h_{1}\right)+E h_{1}^{2} \perp_{L^{2}} \mathscr{E}(M, g) .$$

See section 2 for the definition of the perturbed Einstein operator $\widetilde{\Delta}_{E}$ and that of the operator $\delta^{\star g}$. Note that the obstruction to deformation above contains Koiso's obstruction and also extends it in an intrinsic way. The obstruction in (2) has been used [12, 2] to prove that the symmetric Kähler-Einstein metric on $\operatorname{Gr}_{k}\left(\mathbb{C}^{n}\right)$ is rigid, when $n$ is odd.

At the best of our knowledge there is currently no explicit description, amenable to direct computation, of the Einstein equation to order 3.
1.2. Main results. Our first main result is that Einstein deformations $g_{t} \in \mathscr{M}_{1}$ can be normalised up to second order as follows, after taking into account the action of the gauge group
$$\mathbf{G}:=\left\{f \in \operatorname{Diff}(M): f^{\star} \operatorname{vol}=\operatorname{vol}\right\} .$$

Theorem 1.2. Let $(M, g)$ be compact and Einstein and let $g_{t} \in \mathscr{M}_{1}$ be a family of Einstein metrics with Taylor expansion
$$g^{-1} g_{t}=\mathrm{id}+t h_{1}+\frac{t^{2}}{2} h_{2}+\cdots$$
at $t=0$. Up to a time dependent gauge transformation $g_{t} \mapsto f_{t}^{\star} g_{t}$ where $f_{t} \in \mathbf{G}$ we may assume that
\begin{itemize}
\item[(i)] the first order variation $h_{1}$ belongs to $\mathscr{E}(M, g)$
\item[(ii)] the second order variation $h_{2}$ satisfies
$$\Delta_{E}\left(h_{2}-h_{1}^{2}\right)=\frac{1}{2} \widetilde{\Delta}_{E} h_{1}^{2}+E h_{1}^{2}-\mathbf{v}\left(h_{1}, h_{1}\right)$$
as well as
$$\delta^{g}\left(h_{2}-h_{1}^{2}\right)=-\frac{1}{4} \operatorname{dtr}\left(h_{1}^{2}\right) \text { and } \operatorname{tr}\left(h_{2}-h_{1}^{2}\right)=0 .$$
\end{itemize}

Remark 1.3. The construction the gauge transformation $f_{t}$ involves two main ingredients. Firstly, having the volume of $g_{t}$ constant forces $h_{1}$ and $h_{2}-h_{1}^{2}$ be trace free. Next, differentiating the gauge action $f_{t} \mapsto f_{t}^{\star} g_{t}$ to second order we observe that one can always find an $f_{t}$ such that the divergences of $h_{1}$ and $h_{2}-h_{1}^{2}$ are exact. In this case the Einstein equation in (1) combined with trace properties of v entails that $\delta^{g} h_{1}=0$ and also (4).

The rest of this paper focuses on Einstein deformations $g_{t}$ in $\mathscr{M}_{1}$ of Kähler Einstein metrics of negative scalar curvature; that is we assume $\left(M^{2 m}, g, J\right)$ is Kähler-Einstein with Einstein constant $E<0$. Following [13] we briefly record that the Einstein deformation problem for $g$ is a priori unrelated to the complex deformation theory of $J$.

Remark 1.4. If one knows that $J$ can be deformed to a family of complex structures $J_{t}$ then the metric $g$ can also be deformed to a family of Einstein metrics compatible with $J_{t}$, see [7]. On the other hand there are, see [4], many explicit examples of negative Kähler-Einstein manifolds where the deformation theory of the complex structure is obstructed.

In light of the above remark we make no assumption on the complex structure $J$ in the subsequent. Recently we have observed that

Theorem 1.5. [12][Theorem 5.3] Assume that $\left(M^{2 m}, g, J\right)$ is compact and Kähler-Einstein with $E<0$. Then the obstruction in (2) is always satisfied, in other words the Einstein deformation theory of $g$ is unobstructed to second order.

The main result of this paper consists in considerably refining this result by showing how the normalised Einstein equation to second order (3) can be solved explicitly. We consider the splitting of the bundle of symmetric 2-tensors
$$\operatorname{Sym}^{2} T M=\operatorname{Sym}^{2,+} T M \oplus \operatorname{Sym}^{2,-} T M$$
into $J$-invariant, respectively $J$-anti-invariant components. Whenever $h \in \Gamma\left(\operatorname{Sym}^{2} T M\right)$ we indicate with $h_{ \pm}$the corresponding components with respect to this splitting. Following [7] we also recall that due to $E<0$ the space $\mathscr{E}(M, g)$ coincides with the space of (nor-malised)infinitesimal complex deformations, that is
$$\mathscr{E}(M, g)=\left\{h \in \Gamma\left(\operatorname{Sym}^{2,-} T M\right): \bar{\partial} h=0 \text { and } \delta^{g} h=0\right\} .$$

Theorem 1.6. Let $\left(M^{2 m}, g, J\right)$ be Kähler-Einstein with $E<0$ and let $g_{t} \in \mathscr{M}_{1}$ be an Einstein deformation of $g$ with Taylor expansion $g^{-1} g_{t}=\mathrm{id}+t h_{1}+\frac{t^{2}}{2} h_{2}+o\left(t^{3}\right)$ at $t=0$. Up to a gauge transformation $g_{t} \mapsto f_{t}^{\star} g_{t}$ with $f_{t} \in \mathbf{G}$ as given in Theorem 3.9 we have
\begin{itemize}
\item[(i)] $h_{2}^{+}=h_{1}^{2}$
\item[(ii)] $h_{2}^{-}=\mathbf{h}_{2}-\frac{1}{2} \mathscr{L}_{\text {Jgradf }} J$ where the pair $\left(\mathbf{h}_{2}, \mathbf{f}\right)$ belongs to $\operatorname{TT}^{-}(M, g) \oplus C^{\infty} M$ and satisfies the equations
$$\Delta_{E}^{g} \mathbf{h}_{2}=-2 \delta^{g}\left[h_{1}, h_{1}\right]^{c} \text { and }\left(\Delta^{g}-2 E\right) \mathbf{f}=-\frac{1}{2} \operatorname{tr}\left(h_{1}^{2}\right) .$$
\end{itemize}

In particular $h_{2}-h_{1}^{2}$ belongs to $\Gamma\left(\operatorname{Sym}^{2,-} T M\right)$ and satisfies $\bar{\partial}\left(h_{2}-h_{1}^{2}\right)=\bar{\partial} \mathbf{h}_{2}$.
Above we have indicated with $\mathrm{TT}^{-}(M, g)=\mathrm{TT}(M, g) \cap \Gamma\left(\operatorname{Sym}^{2,-} T M\right)$ the space of $J$ -anti-invariant TT tensors and with $[\cdot, \cdot]^{c}$ the Kodaira-Spencer bracket, see section 4.2 for definitions and properties. A few remarks are now in order as far the construction of the pair $\left(\mathbf{h}_{2}, \mathbf{f}\right)$ is concerned.

Remark 1.7. Since $h_{1}$ is divergence free $\delta^{g}\left[h_{1}, h_{1}\right]^{c}$ belongs to $\mathrm{TT}^{-}(M, g)$ (see Proposition 4.12 in the paper); in addition the description of $\mathscr{E}(M, g)$ in (5) leads easily to having $\delta^{g}\left[h_{1}, h_{1}\right]^{c} \perp_{L^{2}} \mathscr{E}(M, g)=\operatorname{ker} \Delta_{E}$. These facts grant existence for $\mathbf{h}_{2} \in \operatorname{TT}^{-}(M, g)$ solving the equation in (ii) above. Since $E<0$ the operator $\Delta-2 E$ is invertible on functions; this guarantees existence for the function f.

We found it striking that the solution $h_{2}^{+}$assumes a particularly simple algebraic form, and also that the final form of the Einstein equation reduces to the divergence of the Kodaira-Spencer bracket alone, instead of the symmetrised operator v. We believe that Theorem 1.6 paves the way to understanding the third order Einstein deformation theory for negative Kähler-Einstein metrics.
1.3. Key arguments and outline of proofs for Kähler metrics. In section 4.2 we use representation theoretical arguments in order to obtain a comparison formula relating the Frölicher-Nijenhuis and Kodaira-Spencer brackets on Kähler manifolds. This formula is described in full generality in Proposition 4.8; it also leads to the important observation that the divergence of the Kodaira-Spencer bracket acting on divergence free tensors is a TT-tensor (see Proposition 4.12). Yet another direct consequence of Proposition 4.8 is to show that the restriction of $\mathbf{v}$ to $\Gamma\left(\operatorname{Sym}^{2,-} T M\right)$ is determined, up to divergence terms, by the Kodaira-Spencer bracket; this is Proposition 4.14 in the paper. The latter actually allows computing the component on $\Gamma\left(\operatorname{Sym}^{2,-} T M\right)$ of elements of the form $\mathbf{v}(h, h)$ with $h$ in $\mathscr{E}(M, g)$, as given by (5). Furthermore we observe that the computation of the component on $\Gamma\left(\operatorname{Sym}^{2,+} T M\right)$ of $\mathbf{v}(h, h)$ reduces to that of $\left\langle H \sharp \mathrm{~d}_{\nabla^{g}} h, \mathrm{~d}_{\nabla^{g}} h\right\rangle_{L^{2}}$ with $H \in \Gamma\left(\operatorname{Sym}^{2,+} T M\right)$; this is the main technical challenge in the second part of this paper which is completed in Proposition 4.19 after a series of preliminary lemmas and representation theoretical arguments. The final expression for $\mathbf{v}(h, h)$ is then given in Proposition 4.20 which allows bringing equation (3) to final form. Theorem 1.6 is then proved by Hodge theoretical arguments for the Einstein operator $\Delta_{E}$ and by also using the normalisation to second order developed in Theorem 3.9.

Acknowledgments. Paul-Andi Nagy was supported by the Institute for Basic Science (IBS-R032-D1).

\section*{2. Preliminaries}

Let $\left(M^{n}, g\right)$ be a Riemannian manifold and denote with $\nabla^{g}$ the Levi-Civita connection of $g$ acting on $T M$ and all tensor bundles. For the Riemannian curvature tensor $R^{g}$ we use the convention $R^{g}(X, Y)=\left(\nabla^{g}\right)_{Y, X}^{2}-\left(\nabla^{g}\right)_{X, Y}^{2}$ for tangent vectors $X, Y \in T M$. In the following we will make a notational difference between the Ricci form ric ${ }^{g}$ considered as a symmetric bilinear form and the Ricci tensor $\mathrm{Ric}^{g}$ considered as a symmetric endomorphism. We will denote by $g^{-1}$ the isomorphism, induced by the metric, between symmetric bilinear forms and symmetric endomorphisms, e.g. we have $g^{-1} \mathrm{ric}^{g}=\mathrm{Ric}^{g}$. The subbundle of $g$-symmetric
endomorphisms is denoted by $\operatorname{Sym}^{2} T M \subseteq \operatorname{End}(T M)$. It is preserved by $\nabla^{g}$ and the curvature action $h \mapsto \stackrel{\circ}{R} h:=\sum_{i} R^{g}\left(e_{i}, \cdot\right) h e_{i}$, where $\left\{e_{i}\right\}$ is some $g$-orthonormal frame.

We will use the coupled exterior differential $\mathrm{d}_{\nabla^{g}}: \Omega^{k}(M, T M) \rightarrow \Omega^{k+1}(M, T M)$. For $k=0$, i.e. on vector fields, it coincides with the covariant derivative $\nabla^{g}$. For $k=1$, that is on endomorphisms $h$ considered as elements in $\Omega^{1}(M, T M)$, it can be written as $\mathrm{d}_{\nabla^{g}} h(X, Y)=\left(\nabla_{X}^{g} h\right) Y-\left(\nabla_{Y}^{g} h\right) X$. The operator formally adjoint to $\mathrm{d}_{\nabla^{g}}$ is the divergence operator $\delta^{g}: \Omega^{k}(M, T M) \rightarrow \Omega^{k-1}(M, T M)$ which is defined according to the convention $\left.\delta^{g}=-\sum_{i} e_{i}\right\lrcorner \nabla_{e_{i}}^{g}$.

Restricting the divergence to symmetric 2-tensors we have $\delta^{g}: \Gamma\left(\operatorname{Sym}^{2} T M\right) \rightarrow \Omega^{1} M$. Its formal adjoint $\delta^{\star_{g}}: \Omega^{1} M \rightarrow \Gamma\left(\operatorname{Sym}^{2} T M\right)$ is the symmetric part of $\nabla^{g}$, i.e. $\nabla^{g}=\delta^{\star_{g}}+\frac{1}{2} \mathrm{~d}$ on $\Omega^{1} M$. As a consequence we note for later application that $\operatorname{tr}\left(\delta^{\star}{ }^{g} \alpha\right)=-\mathrm{d}^{\star} \alpha$ holds for any 1-form $\alpha$. We also have the well-known formula $\delta^{\star g} \alpha=\frac{1}{2} g^{-1} \mathscr{L}_{\alpha^{\sharp}} g$, characterising the kernel of $\delta^{\star g}$ as 1-forms dual to Killing vector fields.

In dealing with the trace and divergence of symmetric tensors we will use the Bianchi operator $\mathbf{b}^{g}: \Gamma\left(\operatorname{Sym}^{2} T M\right) \rightarrow \Omega^{1} M$ given by $\mathbf{b}^{g}=2 \delta^{g}+$ dotr. Certainly $\mathbf{b}^{g}$ vanishes on the space of the so-called TT-tensors defined by
$$\mathrm{TT}(g):=\left\{h \in \Gamma\left(\operatorname{Sym}^{2} T M\right): \delta^{g} h=0 \text { and } \operatorname{tr}(h)=0\right\} .$$
However terms involving divergence and trace must be kept track of in order to obtain gauge invariant equations. For latter use recall that $\mathbf{b}^{g} \operatorname{Ric}^{g}=0$, which is a consequence of the differential Bianchi identity (see [3], 12.33).

On symmetric 2-tensors and for Einstein metrics $g$ with Einstein constant $E$ we will consider the Einstein operator $\Delta_{E}:=\left(\nabla^{g}\right)^{\star} \nabla^{g}-2 \stackrel{\circ}{R}$. Note that $\Delta_{E}=\Delta_{L}-2 E$, where $\Delta_{L}$ is the Lichnerowicz Laplacian on symmetric 2-tensors (see [3], 1.143). We will also use a perturbation of the Einstein operator, the differential operator $\widetilde{\Delta}_{E}: \Gamma\left(\operatorname{Sym}^{2} T M\right) \rightarrow \Gamma\left(\operatorname{Sym}^{2} T M\right)$ given by
$$\widetilde{\Delta}_{E}:=\Delta_{E}-2 \delta^{\star g} \circ\left(\delta^{g}+\frac{1}{2} \mathrm{~d} \circ \operatorname{tr}\right)=\Delta_{E}-\delta^{\star g} \circ \mathbf{b}^{g} .$$

The following Weitzenböck formula on 2-tensors (see [12]) will be used at several places in this paper.
$$\delta^{g} \circ \mathrm{~d}_{\nabla^{g}}=-\nabla^{g} \circ \delta^{g}+\Delta_{E}+E+\stackrel{\circ}{R}=-\left(\delta^{\star_{g}}+\frac{1}{2} \mathrm{~d}\right) \circ \delta^{g}+\Delta_{E}+E+\stackrel{\circ}{R} .$$
Further properties of the Einstein operator needed in this paper are summarised below.
Lemma 2.1. The following hold
\begin{itemize}
\item[(i)] we have $\Delta_{E} \circ \delta^{\star_{g}}=\delta^{\star_{g}} \circ\left(\Delta^{g}-2 E\right)$
\item[(ii)] $\delta^{g} \circ \Delta_{E}=\left(\Delta^{g}-2 E\right) \circ \delta^{g}$.
\end{itemize}

Proof. (i) We have $\widetilde{\Delta}_{E} \circ \delta^{\star g}=0$ by [12, eqn. (28)] as well as $\mathbf{b}^{g} \circ \delta^{\star g}=\Delta^{g}-2 E$ by [12, eqn. (26)]. The claim follows from $\widetilde{\Delta}_{E}=\Delta_{E}-\delta^{\star g} \circ \mathbf{b}^{g}$.
(ii) follows from (i) by $L^{2}$-duality. \(\square\)

We still need another Weitzenböck form, this time on 1 -forms, which reads
$$2 \delta^{g} \delta^{\star g}-\mathrm{dd}^{\star}=\Delta^{g}-2 E,$$
where $\Delta^{g}=\mathrm{d}^{\star}+\mathrm{d}^{\star} \mathrm{d}$ is the Hodge Laplacian and $g$ is again an Einstein metric; see [12] for further details. In subsequent trace computations we will also need the following
Lemma 2.2. Let $H$ belong to $\Gamma\left(\operatorname{Sym}^{2} T M\right)$. Then
\begin{itemize}
\item[(i)] $\operatorname{tr} \delta^{g} \mathrm{~d}_{\nabla^{g}} H=\mathrm{d}^{\star}\left(\delta^{g} H+\operatorname{dtr}(H)\right)$
\item[(ii)] $\frac{1}{2} \operatorname{tr} \widetilde{\Delta}_{E} H=\mathrm{d}^{\star}\left(\delta^{g} H+\operatorname{dtr}(H)\right)-E \operatorname{tr}(H)$.
\end{itemize}

Proof. Record the identity $\operatorname{tr} \circ \delta^{\star g}=-\mathrm{d}^{\star}$ and also that $\operatorname{tr} \stackrel{\circ}{R} H=E \operatorname{tr}(H)$. Both claims follow now from (7). \(\square\)
2.1. The Frölicher-Nijenhuis bracket. On a given manifold $M$ we first recall that the Frölicher-Nijenhuis bracket for sections $h$ of $\operatorname{End}(T M)=\Lambda^{1}(M, T M)$ reads
$$[h, h]^{\mathrm{FN}}(X, Y)=-h^{2}[X, Y]+h([h X, Y]+[X, h Y])-[h X, h Y] .$$
See also [8][section 8] for a detailed discussion of the Frölicher-Nijenhuis bracket of arbitrary degree forms in $\Omega^{\star}(M, T M)$. From now on assume that $g$ is a Riemannian metric on $M$. Recast in terms of the Levi-Civita connection $\nabla^{g}$ of $g$ the bracket $[h, h]^{\mathrm{FN}}$ reads
$$[h, h]^{\mathrm{FN}}(X, Y)=-\left(\nabla_{h X}^{g} h\right) Y+\left(\nabla_{h Y}^{g} h\right) X+\left(h \circ \mathrm{~d}_{\nabla^{g}} h\right)(X, Y) .$$
Here $\mathrm{d}_{\nabla^{g}}$ acts on $h$ considered as an element of $\Omega^{1}(M, T M)$. In the following, whenever the pair $(h, \alpha)$ belongs to $\operatorname{Sym}^{2} T M \oplus \Lambda^{2}(M, T M)$ we indicate with $h \circ \alpha \in \Lambda^{2}(M, T M)$ the tensor given by $(X, Y) \mapsto h \alpha(X, Y)$. A more concise version of (9) is
$$[h, h]^{\mathrm{FN}}=-h \sharp \mathrm{~d}_{\nabla^{g}} h+\mathrm{d}_{\nabla^{g}} h^{2}$$
where the algebraic action $\alpha \in \Lambda^{2}(M, T M) \mapsto h \sharp \alpha \in \Lambda^{2}(M, T M)$ is defined according to $h \sharp \alpha(X, Y)=\alpha(h X, Y)+\alpha(X, h Y)$. The Frölicher-Nijenhuis bracket is extended to a symmetric bracket on the space $\Gamma\left(\operatorname{Sym}^{2} T M\right)$ via
$$2\left[h_{1}, h_{2}\right]^{\mathrm{FN}}=-\left(h_{1} \sharp \mathrm{~d}_{\nabla^{g}} h_{2}+h_{2} \sharp \mathrm{~d}_{\nabla^{g}} h_{1}\right)+\mathrm{d}_{\nabla^{g}}\left\{h_{1}, h_{2}\right\}$$
where the anti-commutator $\left\{h_{1}, h_{2}\right\}:=h_{1} \circ h_{2}+h_{2} \circ h_{1}$. In particular we have $[\mathrm{id}, h]^{\mathrm{FN}}=0$ for all $h \in \operatorname{End}(T M)$. Finally we record that the Frölicher-Nijenhuis bracket is invariant under the action of the diffeomorphism group, $\varphi_{\star}\left[h_{1}, h_{2}\right]^{\mathrm{FN}}=\left[\varphi_{\star} h_{1}, \varphi_{\star} h_{2}\right]^{\mathrm{FN}}$ whenever $\varphi \in \operatorname{Diff}(M)$; with respect to the Lie derivative we thus must have
$$\mathscr{L}_{X}\left[h_{1}, h_{2}\right]^{\mathrm{FN}}=\left[\mathscr{L}_{X} h_{1}, h_{2}\right]^{\mathrm{FN}}+\left[h_{1}, \mathscr{L}_{X} h_{2}\right]^{\mathrm{FN}}$$
whenever $X \in \Gamma(T M)$.

\section*{3. Bianchi map normalisation to second order}

Let $(M, g)$ be a compact Riemannian manifold and $g_{t}$ be a time dependent family of Riemannian metrics. It is well known that, up to a suitable gauge transformation, the tensor $h_{1}:=g^{-1} \dot{g}_{\mid t=0}$ can be normalised to belong to TT $(M, g)$. This process involves first reduction to metrics of fixed volume $\operatorname{vol}\left(g_{t}\right)=\operatorname{vol}(g)$; this can always be achieved by Moser's theorem which asserts that any two volume forms are equivalent. The next step is to take into account the action of the gauge group
$$\mathbf{G}:=\left\{f \in \operatorname{Diff}(M): f^{\star} \operatorname{vol}=\operatorname{vol}\right\} .$$
When coupled with the Einstein equation to first order, that is $\widetilde{\Delta}_{E} h_{1}=0$ this ensures reduction to $\delta^{g} h_{1}=0$ and further $h_{1} \in \mathrm{E}(g)$.

In this section we considerably extend extend these ideas to normalise the action of trace and divergence operators on the second order variation of $g_{t}$. During this process we obtain an easier to deal with form of the second order Einstein equation found in [12]. The technical difficulties that arise are related to the computation of
$$\operatorname{tr} \mathbf{v}(h, h)$$
where $h \in \mathscr{E}(M, g)$. This computation is performed in detail in the section as follows.
Throughout this paper we deal solely with Einstein deformations $g_{t}$ with constant volume, that is $\operatorname{vol}\left(g_{t}\right)=\operatorname{vol}(g)$ for small $t$.
3.1. Role of the trace. We start by examining further properties of the Frölicher-Nijenhuis bracket, in particular up to which extent $\delta^{g}[h, h]^{\mathrm{FN}}$, where $h \in \operatorname{Sym}^{2} T M$, fails to be symmetric. We define the symmetric operator according to
$$\mathrm{L}(h):=\nabla_{e_{i}}^{g} h \circ \nabla_{e_{i}}^{g} h$$
and observe that
Lemma 3.1. Letting $h$ be in $\Gamma\left(\operatorname{Sym}^{2} T M\right)$ the following hold
\begin{itemize}
\item[(i)] the tensor $\delta^{g}\left([h, h]^{\mathrm{FN}}-h \circ \mathrm{~d}_{\nabla^{g}} h\right)-(\stackrel{\circ}{R} h) \circ h-\nabla^{g}\left(\delta^{g} h\right) \circ h$ is symmetric
\item[(ii)] we have
$$\begin{aligned}
\left\langle\delta^{g}[h, h]^{\mathrm{FN}}, H\right\rangle_{L^{2}}= & \left\langle h \circ \mathrm{~d}_{\nabla^{g}} h, \mathrm{~d}_{\nabla^{g}} H\right\rangle_{L^{2}}+\left\langle\mathrm{d}_{\nabla^{g}} h, H \circ \mathrm{~d}_{\nabla^{g}} h\right\rangle_{L^{2}} \\
& -\left\langle\nabla_{h e_{i}}^{g} h, \nabla_{e_{i}}^{g} H\right\rangle_{L^{2}} \\
& +\left\langle(\stackrel{\circ}{R} h) \circ h-E h^{2}-\mathrm{L}(h), H\right\rangle_{L^{2}}+\left\langle-\nabla_{\delta^{g} h}^{g} h+\nabla^{g}\left(\delta^{g} h\right) \circ h, H\right\rangle_{L^{2}}
\end{aligned}$$
for all $H \in \Gamma\left(\operatorname{Sym}^{2} T M\right)$.
\end{itemize}

Proof. Differentiating in (9) shows that
$$\delta^{g}\left([h, h]^{\mathrm{FN}}-h \circ \mathrm{~d}_{\nabla^{g} h} h\right)_{X}=\left(\left(\nabla^{g}\right)_{e_{i}, h e_{i}}^{2} h\right) X-\left(\nabla_{\delta^{g} h}^{g} h\right) X-\left(\left(\nabla^{g}\right)_{e_{i}, h X}^{2} h\right) e_{i}-\left(\nabla_{\left(\nabla_{e_{i}}^{g} h\right) X}^{g} h\right) e_{i}$$
for all $X$ in $T M$. Using the Ricci identity leads to
$$\left(\left(\nabla^{g}\right)_{e_{i}, h X}^{2} h\right) e_{i}=-\nabla_{h X}^{g} \delta^{g} h-\left[R^{g}\left(e_{i}, h X\right), h\right] e_{i}=-\nabla_{h X}^{g} \delta^{g} h+\left(E h^{2}-(\AA h) \circ h\right) X .$$
Taking $Y$ in $T M$ we furthermore compute
$$\begin{aligned}
g\left(\left(\nabla_{\left(\nabla_{e_{i}}^{g} h\right) X}^{g} h\right) e_{i}, Y\right) & =g\left(\left(\nabla_{e_{i}}^{g} h\right) X, e_{k}\right) g\left(\left(\nabla_{e_{k}}^{g} h\right) e_{i}, Y\right) \\
& =g\left(\mathrm{~d}_{\nabla^{g}} h\left(e_{i}, e_{k}\right), X\right) g\left(\left(\nabla_{e_{k}}^{g} h\right) e_{i}, Y\right)+g(\mathrm{~L}(h) X, Y) \\
& =-\frac{1}{2} g\left(\mathrm{~d}_{\nabla^{g}} h\left(e_{i}, e_{k}\right), X\right) g\left(\mathrm{~d}_{\nabla^{g}} h\left(e_{i}, e_{k}\right), Y\right)+g(\mathrm{~L}(h) X, Y) .
\end{aligned}$$
Gathering terms thus leads to
$$\begin{aligned}
g\left(\delta^{g}\left([h, h]^{\mathrm{FN}}-h \circ \mathrm{~d}_{\nabla^{g}} h\right)_{X}, Y\right) & =g\left(\left(\left(\nabla^{g}\right)_{e_{i}, h e_{i}}^{2} h\right) X-\left(\nabla_{\delta^{g} h}^{g} h\right) X+\nabla_{h X}^{g} \delta^{g} h, Y\right) \\
& +g\left(\left((\dot{R} h) \circ h-E h^{2}-\mathrm{L}(h)\right) X, Y\right) \\
& +\frac{1}{2} g\left(\mathrm{~d}_{\nabla^{g}} h\left(e_{i}, e_{k}\right), X\right) g\left(\mathrm{~d}_{\nabla^{g}} h\left(e_{i}, e_{k}\right), Y\right)
\end{aligned}$$
Since the last summand above is symmetric in $X$ and $Y$ the claim in (i) follows from the symmetry of the operator $\mathrm{L}(h)$. The claim in (ii) follows by taking $X=e_{k}, Y=H e_{k}$ and integrating by parts; that is $\left\langle\left(\nabla^{g}\right)_{e_{i}, h e_{i}}^{2} h, H\right\rangle_{L^{2}}=-\left\langle\nabla_{h e_{i}}^{g} h, \nabla_{e_{i}}^{g} H\right\rangle_{L^{2}}$. \(\square\)

In the second part of the paper we will also use Lemma 3.1 for Kähler manifolds in order to determine the symmetry properties of the complex Frölicher-Nijenhuis bracket. To that extent we observe that Lemma 3.1 can be brought to the following more concise form. Whenever $(X, h)$ belongs to $T M \oplus \operatorname{Sym}^{2} T M$ the wedge product $X \wedge h \in \Lambda^{2}(M, T M)$ is defined according to $(X \wedge h)(Y, Z)=g(X, Y) h Z-g(X, Z) h Y$.
Proposition 3.2. Let $h$ belong to $\operatorname{Sym}^{2} T M$. The tensor
$$\delta^{g}\left([h, h]^{\mathrm{FN}}+\delta^{g} h \wedge h-h \circ \mathrm{~d}_{\nabla^{g}} h\right)-(\stackrel{\circ}{R} h) \circ h \text { is symmetric. }$$
Proof. Whenever the tensor $Q$ belongs to $\operatorname{End} T M$ we indicate with $Q_{\text {skew }}$ its skew-symmetric component which is determined from $g\left(Q_{\text {skew }} X, Y\right)=\frac{1}{2}(g(Q X, Y)-g(X, Q Y))$. A straightforward computation leads to
$$\delta^{g}\left(\delta^{g} h \wedge h\right)=\left(\mathrm{d}^{\star} \delta^{g} h\right) h-\nabla_{\delta^{g} h}^{g} h+h \circ\left(\nabla^{g}\left(\delta^{g} h\right)\right)^{T}-\delta^{g} h \otimes \delta^{g} h$$
where the superscript indicates the transpose with respect to the metric $g$. In particular
$$\left.\left(\delta^{g}\left(\delta^{g} h \wedge h\right)\right)_{\text {skew }}=\left(h \circ\left(\delta^{\star g} \delta^{g} h-\frac{1}{2} \mathrm{~d} \delta^{g} h\right)\right)_{\text {skew }}=\frac{1}{2}\left(\left[h, \delta^{\star g} \delta^{g} h\right]-\frac{1}{2}\left\{h, \mathrm{~d} \delta^{g} h\right)\right\}\right) .$$
At the same time $\left.\left(\nabla^{g}\left(\delta^{g} h\right) \circ h\right)_{\text {skew }}=\left(\left(\delta^{\star g} \delta^{g} h+\frac{1}{2} \mathrm{~d} \delta^{g} h\right) \circ h\right)_{\text {skew }}=\frac{1}{2}\left(\left[\delta^{\star g} \delta^{g} h, h\right]+\frac{1}{2}\left\{h, \mathrm{~d} \delta^{g} h\right)\right\}\right)$. Comparison of the skew-symmetric components entails that the tensor $\delta^{g}\left(\delta^{g} h \wedge h\right)+\nabla^{g}\left(\delta^{g} h\right) \circ h$ is symmetric and the claim follows from Lemma 3.1, (i). \(\square\)

Next we observe that one can also compute explicitly the trace of $\delta^{g}[h, h]^{\mathrm{FN}}$, a fact that will be needed later on.

Lemma 3.3. Assume that $h$ in $\Gamma\left(\operatorname{Sym}^{2} T M\right)$ satisfies $\operatorname{tr}(h)=0$. Then
$$\operatorname{tr} \delta^{g}[h, h]^{\mathrm{FN}}=\frac{1}{2} \Delta^{g} \operatorname{tr}\left(h^{2}\right) .$$
Proof. Using (9) shows that
$$\begin{aligned}
g\left([h, h]^{\mathrm{FN}}\left(X, e_{i}\right), e_{i}\right) & =-g\left(\left(\nabla_{h X}^{g} h\right) e_{i}, e_{i}\right)+g\left(\left(\nabla_{h e_{i}}^{g} h\right) X, e_{i}\right)+g\left(\left(\nabla_{X}^{g} h\right) e_{i}-\left(\nabla_{e_{i}}^{g} h\right) X, h e_{i}\right) \\
& =-g\left(\left(\nabla_{h X}^{g} h\right) e_{i}, e_{i}\right)+g\left(\left(\nabla_{X}^{g} h\right) e_{i}, h e_{i}\right)
\end{aligned}$$
since $h$ is symmetric. Because $h$ is trace free it follows that $g\left([h, h]^{\mathrm{FN}}\left(X, e_{i}\right), e_{i}\right)=\frac{1}{2} \mathscr{L}_{X} \operatorname{tr}\left(h^{2}\right)$. The claim follows by taking $X=e_{k}$ and differentiating in direction $e_{k}$. \(\square\)

We finish this section by computing the trace of the operator $\mathbf{v}(h, h)$ with $h \in \mathscr{E}(M, g)$. To perform this computation we first recall that
$$\begin{aligned}
\left\langle\mathbf{v}\left(h_{1}, h_{2}\right), H\right\rangle_{L^{2}} & =2\left\langle\left[h_{1}, h_{2}\right]^{\mathrm{FN}}, \mathrm{~d}_{\nabla^{g}} H\right\rangle_{L^{2}}-\left\langle H \sharp \mathrm{~d}_{\nabla^{g}} h_{1}, \mathrm{~d}_{\nabla^{g}} h_{2}\right\rangle_{L^{2}} \\
& +\frac{1}{2}\left\langle\left\{h_{1}, \delta^{g} \mathrm{~d}_{\nabla^{g}} h_{2}\right\}+\left\{h_{2}, \delta^{g} \mathrm{~d}_{\nabla^{g}} h_{1}\right\}-\delta^{g} \mathrm{~d}_{\nabla^{g}}\left\{h_{1}, h_{2}\right\}, H\right\rangle_{L^{2}}
\end{aligned}$$
for symmetric tensors $h_{1}, h_{2}$ and $H$ in $\Gamma\left(\operatorname{Sym}^{2} T M\right)$; see the proof of Theorem 4.4 in [12]. Record now the following preliminary

Lemma 3.4. Assume that the pair $(h, f) \in \mathscr{E}(g) \oplus C^{\infty} M$. Then
$$\left\langle\mathrm{d}_{\nabla^{g}} h, f \mathrm{~d}_{\nabla^{g}} h\right\rangle_{L^{2}}=\langle f h, E h+\stackrel{\circ}{R} h\rangle_{L^{2}}-\frac{1}{2}\left\langle\mathrm{~d} f, \mathbf{b}\left(h^{2}\right)\right\rangle_{L^{2}} .$$

Proof. Start from $\mathrm{d}_{\nabla^{g}}(f h)=f \mathrm{~d}_{\nabla^{g}} h+\mathrm{d} f \wedge h$ so that
$$\left\langle\mathrm{d}_{\nabla^{g}} h, f \mathrm{~d}_{\nabla^{g}} h\right\rangle_{L^{2}}=\left\langle f h, \delta^{g} \mathrm{~d}_{\nabla^{g}} h\right\rangle_{L^{2}}-\left\langle\delta^{g}(\mathrm{~d} f \wedge h), h\right\rangle_{L^{2}} .$$
Also observe that $\delta^{g}(\mathrm{~d} f \wedge h)=(\Delta f) h-\nabla_{\text {grad } f}^{g} h+h \circ \nabla^{g} \operatorname{grad} f$ since $\delta^{g} h=0$. It follows that
$$\left\langle\delta^{g}(\mathrm{~d} f \wedge h), h\right\rangle_{L^{2}}=\left\langle\Delta^{g} f, \operatorname{tr}\left(h^{2}\right)\right\rangle_{L^{2}}-\frac{1}{2}\left\langle\mathrm{~d} f, \mathrm{~d} \operatorname{tr}\left(h^{2}\right)\right\rangle_{L^{2}}+\left\langle\mathrm{d} f, \delta^{g} h^{2}\right\rangle_{L^{2}}=\frac{1}{2}\left\langle\mathrm{~d} f, \mathbf{b}\left(h^{2}\right)\right\rangle_{L^{2}} .$$
The claim follows by gathering terms and also using (7). \(\square\)

Finally, we are able to prove the following
Proposition 3.5. Assume that $h$ belongs to $\mathscr{E}(M, g)$. We have
$$\operatorname{tr}\left(E h^{2}-\mathbf{v}(h, h)+\frac{1}{2} \widetilde{\Delta}_{E} h^{2}\right)=0 .$$

Proof. We use (12) whilst taking into account the comparison formula (7); we find
$$\begin{aligned}
\langle\mathbf{v}(h, h), f \mathrm{id}\rangle_{L^{2}}= & 2\left\langle\delta^{g}[h, h]^{\mathrm{FN}}, f \mathrm{id}\right\rangle_{L^{2}}-2\left\langle f \mathrm{~d}_{\nabla^{g}} h, \mathrm{~d}_{\nabla^{g}} h\right\rangle_{L^{2}} \\
& +\left\langle\{h, E h+\stackrel{\circ}{R} h\}-\delta^{g} \mathrm{~d}_{\nabla^{g}} h^{2}, f \mathrm{id}\right\rangle_{L^{2}} .
\end{aligned}$$
After taking into account Corollary 3.3 as well as Lemma 3.4 an $L^{2}$-orthogonality argument shows that $\operatorname{tr} \mathbf{v}(h, h)=\Delta^{g} \operatorname{tr}\left(h^{2}\right)+\mathrm{d}^{*} \mathbf{b}\left(h^{2}\right)-\operatorname{tr}\left(\delta^{g} \mathrm{~d}_{\nabla^{g}} h^{2}\right)$. The claim follows now from the first identity in Lemma 2.2. \(\square\)
nos
3.2. Proof of normalisation to second order. We start from the following elementary observation.
red-1 Lemma 3.6. Assume that $H \in \Gamma\left(\operatorname{Sym}^{2} T M\right)$. There exists $X \in \Gamma(T M)$ such that $\mathrm{d}^{* g} X=0$ and $\delta^{g}\left(H+\delta^{\star_{g}} X\right) \in \operatorname{Im} \mathrm{d}$.

Proof. Split $H=Q+\delta^{\star g} X+f$ id where $Q \in \mathrm{TT}(M, g)$ and $(X, f) \in \Gamma(T M) \oplus C^{\infty} M$; see e.g. [3] for more details. Furthermore split, by Hodge decomposition, $X=X_{0}+\mathrm{d} q$ where $X_{0}$ is divergence free and $q$ is a function on $M$. Using (8) shows that
$$\delta^{g}\left(H-\delta^{\star g} X_{0}\right)=\mathrm{d}\left(\left(\Delta^{g}-E\right) q-f\right)$$
is exact and the claim is proved by letting $X:=-X_{0}$. \(\square\)

Yet another preliminary observation we need is the following
red-2 Lemma 3.7. Assume that the family of metrics $g_{t} \in \mathscr{M}_{1}$ with $g_{0}=g$ has Taylor expansion
$$g^{-1} g_{t}=\mathrm{id}+t h_{1}+\frac{t^{2}}{2} h_{2}+\cdots$$
at $t=0$. Then the tensors $h_{1}$ and $h_{2}-h_{1}^{2}$ are both trace-free.
Proof. Write $g^{-1} g_{t}:=h_{t}$ so that having constant volume amounts to $\operatorname{det} h_{t}=1$. Differentiating with respect to $t$ yields $\operatorname{tr}\left(h_{t}^{\prime} h_{t}^{-1}\right)=0$ hence taking $t=0$ shows that $\operatorname{tr}\left(h_{1}\right)=0$. Differentiating a second time whilst taking into account that $\left(h_{t}^{-1}\right)^{\prime}=-h_{t}^{-1} h_{t}^{\prime} h_{t}^{-1}$ yields $\operatorname{tr}\left(h_{2}-h_{1}^{2}\right)=0$. \(\square\)

In particular having $h_{1}$ and $h_{2}-h_{1}^{2}$ trace-free is a property which is invariant under the gauge group $\mathbf{G}$, since the latter preserves the volume form.

The main result in this section is that the coefficients in the Taylor expansion of the Einstein metric $g_{t}$ can be normalised-up to gauge action-to second order as well. The idea is to differentiate to second order the action of the gauge group G on a given one parameter family of metrics $g_{t}$, then use Lemma 3.6 to reduce to the case when the divergences of $h_{1}$ and $h_{2}-h_{1}^{2}$ are exact.

Proposition 3.8. Let $g_{t} \in \mathscr{M}_{1}$ be a family of Riemannian metrics with Taylor expansion
$$g^{-1} g_{t}=\mathrm{id}+t h_{1}+\frac{t^{2}}{2} h_{2}+\cdots$$
at $t=0$. Up to a gauge transformation i.e. $g_{t} \mapsto f_{t}^{\star} g_{t}$ where $f_{t} \in \mathbf{G}$ we may assume that the divergences
$$\delta^{g} h_{1} \text { and } \delta^{g}\left(h_{2}-h_{1}^{2}\right) \text { are both exact. }$$
Proof. We look for a time dependent family $f_{t} \in \mathbf{G}$ with $f_{0}=\mathrm{id}$ such that the coefficients of the Taylor expansion of the family of metrics $\tilde{g}_{t}:=f_{t}^{\star} g_{t}$ have the required properties. Consider the time-dependent family of vector fields $X_{t}$ determined from $f_{t}^{\prime}=X_{t} \circ f_{t}$; since
norm-2nd
$f_{t} \in \mathbf{G}$ we must have $\mathrm{d}^{\star g} X_{t}=0$. Indeed, differentiating in $f_{t}^{\star} \mathrm{vol}=\mathrm{vol}$ we get $\mathscr{L}_{X_{t}} \mathrm{vol}=0$, that is $X_{t}$ is divergence free. Moreover, we consider the Taylor expansion to order 2 of $\tilde{g}_{t}$, that is $g^{-1} \tilde{g}_{t}=\mathrm{id}+t \tilde{h}_{1}+\frac{t^{2}}{2} \tilde{h}_{2}+o\left(t^{3}\right)$. Differentiating shows that
$$\tilde{g}_{t}^{\prime}=f_{t}^{\star}\left(g_{t}^{\prime}+\mathscr{L}_{X_{t}} g_{t}\right) .$$
In particular we have
$$\tilde{h}_{1}=h_{1}+2 \delta^{\star g} X_{0} .$$
Differentiating a second time shows that, at $t=0$,
$$\tilde{g}_{t}^{\prime \prime}=g_{t}^{\prime \prime}+2 \mathscr{L}_{X_{0}} g_{t}^{\prime}+\mathscr{L}_{X_{0}}^{2} g+\mathscr{L}_{X_{1}} g$$
where $X_{1}:=X_{t}^{\prime}(0)$. Thus the Taylor coefficient
$$\tilde{h}_{2}=h_{2}+q+2 \delta^{\star_{g}} X_{1}$$
where the symmetric tensor $q:=g^{-1}\left(2 \mathscr{L}_{X_{0}} g_{t}^{\prime}+\mathscr{L}_{X_{0}}^{2} g\right)$ only depends on $X_{0}$ and $g^{\prime}(0)$; note there is no need of making this tensor more explicit. Therefore
$$\tilde{h}_{2}-\tilde{h}_{1}^{2}=h_{2}+q-\tilde{h}_{1}^{2}+2 \delta^{\star_{g}} X_{1} .$$
Using Lemma 3.6 for the symmetric tensor $h_{1}$ yields a divergence free vector field $X_{0}$ such that $\tilde{h}_{1}$ has exact divergence. Similarly, using Lemma 3.6 for the symmetric tensor $h_{2}+q-\tilde{h}_{1}^{2}$ thus produces a divergence free vector field $X_{1}$ such that $h_{2}+q-\tilde{h}_{1}^{2}+2 \delta^{\star g} X_{1}$, and hence $\tilde{h}_{2}-\tilde{h}_{1}^{2}$, has exact divergence.

To conclude, we consider the divergence free family $X_{t}:=X_{0}+t X_{1}$ where the vector fields $X_{0}$ and $X_{1}$ are constructed as above. The desired gauge transformation $f_{t} \in \mathbf{G}$ is obtained by solving $\dot{f}_{t}=X_{t} \circ f_{t}$. \(\square\)

When coupled with the Einstein equations to first and second order the normalisation in the previous proposition yields the following.

Theorem 3.9. Let $g_{t}$ be a family of Einstein metrics with $\operatorname{vol}\left(g_{t}\right)=\operatorname{vol}$, with Taylor expansion
$$g^{-1} g_{t}=\mathrm{id}+t h_{1}+\frac{t^{2}}{2} h_{2}+\cdots$$
at $t=0$. Up to a time dependent gauge transformation $g_{t} \mapsto f_{t}^{\star} g_{t}$ where $f_{t} \in \mathbf{G}$ we can assume that
\begin{itemize}
\item[(i)] the first order variation $h_{1}$ belongs to $\mathscr{E}(M, g)$
\item[(ii)] the second order variation $h_{2}$ satisfies
\end{itemize}
$$\Delta_{E}\left(h_{2}-h_{1}^{2}\right)=\frac{1}{2} \widetilde{\Delta}_{E} h_{1}^{2}+E h_{1}^{2}-\mathbf{v}\left(h_{1}, h_{1}\right) .$$
as well as
$$\delta^{g}\left(h_{2}-h_{1}^{2}\right)=-\frac{1}{4} \operatorname{dtr}\left(h_{1}^{2}\right) \text { and } \operatorname{tr}\left(h_{2}-h_{1}^{2}\right)=0 .$$

Proof. The argument uses the normalisation from Proposition 3.8; therefore we assume that the trace-free symmetric tensors $h_{1}, h_{2}-h_{1}^{2}$ have exact divergences.
(i) This is well known but we include the proof since the argument fits the higher order set-up we are dealing with. Since $g_{t}$ is an Einstein metric, differentiating the Einstein equation to first order yields $\widetilde{\Delta}_{E} h_{1}=0$, see e.g. [12][Proposition 3.2]. We apply the trace and take into account Lemma 2.2,(ii); since $h_{1}$ is trace free it follows that $\mathrm{d}^{\star} \delta^{g} h_{1}=0$. Since $\delta^{g} h_{1}$ is exact this leads to having $\delta^{g} h_{1}=0$, as claimed.
(ii)Since $h_{1} \in \mathrm{TT}(M, g)$ by (i) we have
$$\widetilde{\Delta}_{E}\left(h_{2}-\frac{3}{2} h_{1}^{2}\right)=E h_{1}^{2}-\mathbf{v}\left(h_{1}, h_{1}\right)+\frac{1}{2} \delta^{\star g} \operatorname{dtr}\left(h_{1}^{2}\right)$$
by [12][Theorem 3.13]. Equivalently
$$\widetilde{\Delta}_{E}\left(h_{2}-h_{1}^{2}\right)=\frac{1}{2} \widetilde{\Delta}_{E} h_{1}^{2}+E h_{1}^{2}-\mathbf{v}\left(h_{1}, h_{1}\right)+\frac{1}{2} \delta^{\star^{\prime} g} \operatorname{dtr}\left(h_{1}^{2}\right) .$$
The assumption of having constant volume guarantees that $h_{2}-h_{1}^{2}$ is trace free by Lemma 3.7; thus taking the trace in the last displayed equation yields
$$\operatorname{tr} \widetilde{\Delta}_{E}\left(h_{2}-h_{1}^{2}\right)=2 \mathrm{~d}^{\star} \delta^{g}\left(h_{2}-h_{1}^{2}\right)$$
by also using Lemma 2.2, (ii). The operator $\frac{1}{2} \widetilde{\Delta}_{E} h_{1}^{2}+E h_{1}^{2}-\mathbf{v}\left(h_{1}, h_{1}\right)$ is trace free according to Proposition 3.5. Thus by applying the trace we find
$$\mathrm{d}^{\star}\left(\delta^{g}\left(h_{2}-h_{1}^{2}\right)+\frac{1}{4} \mathrm{dtr}\left(h_{1}^{2}\right)\right)=0 .$$
Since we know that $\delta^{g}\left(h_{2}-h_{1}^{2}\right)$ is exact the previously displayed equation forces the vanishing of $\delta^{g}\left(h_{2}-h_{1}^{2}\right)+\frac{1}{4} \mathrm{~d} \operatorname{tr}\left(h_{1}^{2}\right)$ and the claim is proved. \(\square\)

This proves Theorem 3.9 in the introduction.

\section*{4. Negative Kähler-Einstein metrics}
4.1. Elements of Kähler geometry. Let $\left(M^{2 m}, g, J\right)$ be Kähler-Einstein, with Einstein constant $E<0$. We briefly review in this section some notation and main facts needed in what follows. The action of $J$ extends to $\Omega^{\star} M$ according to $J \alpha:=\alpha(J \cdot, \ldots, J \cdot)$. The bundle of symmetric 2-tensors splits as $\operatorname{Sym}^{2} T M=\operatorname{Sym}^{2,+} T M \oplus \operatorname{Sym}^{2,-} T M$ where the summands
$$\operatorname{Sym}^{2, \pm} T M=\left\{h \in \operatorname{Sym}^{2} T M: h J= \pm J h\right\} .$$
This allows defining spaces of TT-tensors according to
$$\mathrm{TT}^{ \pm}(M, g):=\mathrm{TT}(M, g) \cap \Gamma\left(\operatorname{Sym}^{2, \pm} T M\right) .$$
Furthermore, the operator $\delta^{\star g}$ splits as
$$\delta^{\star_{g}} X=\delta^{\star_{g},+} X+\delta^{\star_{g},-} X$$
according to $\operatorname{Sym}^{2} T M=\operatorname{Sym}^{2,+} T M \oplus \operatorname{Sym}^{2,-} T M$. The components are explicitly given by
$$4\left(\delta^{\star_{g},+} X\right) \circ J=(1+J) \mathrm{d}(J X)^{b} \text { and }-2 \delta^{\star_{g},-} X=\mathscr{L}_{J X} J+\frac{1}{2}(1-J) \mathrm{d} X^{b}$$
whenever $X \in T M$. Indeed, differentiating in $g(J \cdot, \cdot)=\omega$ and using Cartan's formula leads to the identity $2 g\left(\left(\delta^{\star g} X\right) \circ J, \cdot\right)+g\left(\mathscr{L}_{X} J \cdot, \cdot\right)=\mathrm{d}(J X)^{b}$; the relations in (15) follow now by projection onto $\operatorname{Sym}^{2, \pm} T M$.

In order to obtain the comparison formulas needed in what follows we first observe that
Lemma 4.1. Assume that $H \in \operatorname{Sym}^{2} T M$. Then
$$\delta^{g} \mathrm{~d}_{\nabla^{g}} H(J \cdot, J \cdot)=E[J, H] \circ J+(\stackrel{\circ}{R}-E) H-\left(\nabla^{g} \delta^{g}(H \circ J)\right) \circ J .$$
Proof. With respect to some local orthonormal frame $\left\{e_{i}\right\}$ in $T M$ we have
$$-\left(\delta^{g} \mathrm{~d} H(J \cdot, J \cdot)\right)_{X}=\left(\left(\nabla^{g}\right)_{e_{i}, J e_{i}}^{2} H\right) J X-\left(\left(\nabla^{g}\right)_{e_{i}, J X}^{2} H\right) J e_{i}$$
since $\mathrm{d}_{\nabla^{g}} H\left(J e_{i}, J X\right)=\left(\nabla_{J e_{i}}^{g} H\right) J X-\left(\nabla_{J X}^{g} H\right) J e_{i}$ whenever $X \in T M$. Using the Ricci identity shows that
$$\left(\left(\nabla^{g}\right)_{e_{i}, J e_{i}}^{2} H\right) J X=\frac{1}{2}\left(\left(\nabla^{g}\right)_{e_{i}, J e_{i}}^{2} H-\left(\nabla^{g}\right)_{J e_{i}, e_{i}}^{2} H\right) J X=-\frac{1}{2}\left[R^{g}\left(e_{i}, J e_{i}\right), H\right] J X=-E[J, H] J X .$$
Using again the Ricci identity leads to
$$\begin{aligned}
-\left(\left(\nabla^{g}\right)_{e_{i}, J X}^{2} H\right) J e_{i} & =-\left(\left(\nabla^{g}\right)_{J X, e_{i}}^{2} H\right) J e_{i}+\left[R^{g}\left(e_{i}, J X\right), H\right] J e_{i} \\
& =\nabla_{J X}^{g} \delta^{g}(H J)-\left[R^{g}\left(e_{i}, X\right), H\right] e_{i}=\nabla_{J X}^{g} \delta^{g}(H J)+(E-\stackrel{\circ}{R} H) X
\end{aligned}$$
where in the second equality we have replaced the frame $\left\{e_{i}\right\}$ by $\left\{J e_{i}\right\}$. The claim follows now by collecting terms. \(\square\)

Indicate with $\lambda^{2} M=\left\{\alpha \in \Lambda^{2} M: \alpha(J \cdot, J \cdot)=-\alpha\right\}$, so that $\Lambda^{2} M=\Lambda^{1,1} M \oplus \lambda^{2} M$. Accordingly, the exterior derivative $\mathrm{d}: \Omega^{1} M \rightarrow \Omega^{2} M$ splits into complex types according to $\mathrm{d}=\mathrm{d}^{+}+\mathrm{d}^{-}$where the summands are given by
$$2 \mathrm{~d}^{+} \alpha=\mathrm{d} \alpha+\mathrm{d} \alpha(J \cdot, J \cdot) \in \Omega^{1,1} M \text { and } 2 \mathrm{~d}^{-} \alpha=\mathrm{d} \alpha-\mathrm{d} \alpha(J \cdot, J \cdot) \in \lambda^{2} M$$
whenever $\alpha$ belongs to $\Omega^{1} M$. Similarly, we consider the splitting of real bundles given by $\Lambda^{2}(M, T M)=\Lambda^{1,1}(M, T M) \oplus \lambda^{2}(M, T M)$ where in analogy with the case of 2-forms we define $\lambda^{2}(M, T M):=\left\{\alpha \in \Lambda^{2}(M, T M): \alpha(J \cdot, J \cdot)=-\alpha\right\}$. Accordingly, whenever $H$ belongs to $\Gamma\left(\operatorname{Sym}^{2,+} T M\right)$ we may split $\mathrm{d}_{\nabla^{g}} H=\mathrm{d}_{\nabla^{g}}^{+} H+\mathrm{d}_{\nabla^{g}}^{-} H$ where
$$\mathrm{d}_{\nabla^{g}}^{ \pm} H:=\frac{1}{2}\left(\mathrm{~d}_{\nabla^{g}} H \pm \mathrm{d}_{\nabla^{g}} H(J \cdot, J \cdot)\right) .$$
Then $\mathrm{d}_{\nabla^{g}}^{+} H \in \Omega^{1,1}(M, T M)$ respectively $\mathrm{d}_{\nabla^{g}}^{-} H \in \lambda^{2}(M, T M)$.
As a first consequence of Lemma 4.1 we record that
Corollary 4.2. Letting $H$ be in $\Gamma\left(\operatorname{Sym}^{2,+} T M\right)$ we have
$$\delta^{g} \mathrm{~d}_{\nabla^{g}}^{+} H=\left(\frac{1}{2} \Delta_{E}+\stackrel{\circ}{R}\right) H-\delta^{\star_{g},-} \delta^{g} H-\frac{1}{2} \mathrm{~d}^{-} \delta^{g} H .$$

Proof. By Lemma 4.1 we get
$$\delta^{g} \mathrm{~d}_{\nabla^{g}} H(J \cdot, J \cdot)=(\stackrel{\circ}{R}-E) H-\nabla^{g}\left(\delta^{g}(H J)\right) \circ J$$
since $H J=J H$. To deal with the divergence term we start from observing that the equality $\delta^{g}(H J)=J \delta^{g} H$ entails $\nabla^{g}\left(\delta^{g}(H J)\right) \circ J=J\left(\nabla^{g}\left(\delta^{g} H\right)\right) \circ J$. After expanding
$$\nabla^{g}=\delta^{\star_{g},+}+\delta^{\star_{g},{ }^{-}}+\frac{1}{2}\left(\mathrm{~d}^{+}+\mathrm{d}^{-}\right)$$
we find $J\left(\nabla^{g}\left(\delta^{g} H\right)\right) \circ J=\left(-\delta^{\star_{g},+}+\delta^{\star_{g},-}+\frac{1}{2}\left(-\mathrm{d}^{+}+\mathrm{d}^{-}\right)\right) \delta^{g} H$. Taking this fact into account shows that $\delta^{g} \mathrm{~d}_{\nabla^{g}} H(J \cdot, J \cdot)=(\stackrel{\circ}{R}-E) H+\left(\delta^{\star_{g},+}-\delta^{\star_{g},-}+\frac{1}{2}\left(\mathrm{~d}^{+}-\mathrm{d}^{-}\right)\right) \delta^{g} H$. The claim follows now after re-writing the Weitzenböck formula in (7) as
$$\delta^{g} \mathrm{~d}_{\nabla^{g}} H=-\left(\delta^{\star_{g},+}+\delta^{\star_{g},-}+\frac{1}{2}\left(\mathrm{~d}^{+}+\mathrm{d}^{-}\right)\right) \delta^{g} H+\left(\Delta_{E}+\stackrel{\circ}{R}+E\right) H .$$ \(\square\)

We also recall below the comparison formula between the Einstein operator acting on $\Gamma\left(\operatorname{Sym}^{2,+} T M\right)$ and the Hodge Laplacian $\Delta^{g}$ acting on $\Omega^{1,1} M$. This formula reads
$$g^{-1}\left(\Delta^{g}-2 E\right) A=\left(\Delta_{E} H\right) \circ J$$
whenever $H \in \Gamma\left(\operatorname{Sym}^{2,+} T M\right)$, where $A:=g(H J \cdot, \cdot)$ belongs to $\Omega^{1,1} M$. In particular this entails
$$\operatorname{ker} \Delta_{E} \cap \Gamma\left(\operatorname{Sym}^{2,+} T M\right)=\{0\}$$
when $E<0$.
Whenever $h$ belongs to $\Gamma\left(\operatorname{Sym}^{2,-} T M\right)$ we define the operator
$$\bar{\partial} h:=\frac{1}{2}\left(\mathrm{~d}_{\nabla^{g}} h-\mathrm{d}_{\nabla^{g}} h(J \cdot, J \cdot)\right)$$
and also record that $[h, J]^{\mathrm{FN}}(J \cdot, \cdot)=\bar{\partial} h$; equivalently, $[h, J]^{\mathrm{FN}}=\bar{\partial}(J h)$. We also let $\widetilde{\Delta}_{E}^{-}$ be the component on $\operatorname{Sym}^{2,-} T M$ of the restriction of the perturbation $\widetilde{\Delta}_{E}$ of the Einstein operator to $\operatorname{Sym}^{2,-} T M$; since elements of the latter space are trace-free we obtain
$$\widetilde{\Delta}_{E}^{-} h=\Delta_{E} h-2 \delta^{\star^{g},-} \delta^{g} h$$
for all $h$ in $\Gamma\left(\operatorname{Sym}^{2,-} T M\right)$.
bde Corollary 4.3. Assume that $h \in \Gamma\left(\operatorname{Sym}^{2,-} T M\right)$. Then
$$\delta^{g} \bar{\partial} h=\frac{1}{2} \widetilde{\Delta}_{E}^{-} h-\frac{1}{2} \mathrm{~d}^{-} \delta^{g} h .$$

Proof. Follows from Lemma 4.1 in complete analogy with the proof of Corollary 4.2. \(\square\)

In particular, as showed in [7] we have
$$\operatorname{ker} \Delta_{E} \cap \Gamma\left(\operatorname{Sym}^{2,-} T M\right)=\left\{h \in \Gamma\left(\operatorname{Sym}^{2,-} T M\right): \bar{\partial} h=0 \text { and } \delta^{g} h=0\right\} .$$

Summarising, we thus recall that for Kähler-Einstein metrics with $E<0$ the space of infinitesimal Einstein deformations is given by
$$\mathscr{E}(M, g)=\left\{h \in \Gamma\left(\operatorname{Sym}^{2,-} T M\right): \bar{\partial} h=0 \text { and } \delta^{g} h=0\right\} .$$
4.2. Type decomposition of $[\cdot, \cdot]^{\text {FN }}$ and the Kodaira-Spencer bracket. Letting $h$ belong to $\operatorname{Sym}^{2,-} T M$ the bracket $[h, h]^{\mathrm{FN}}$ lives in $\Lambda^{2}(M, T M)$; by considering the type decomposition of the latter bundle we will explain how this bracket compares to the Kodaira-Spencer bracket by using pure representation theoretical considerations. We recall (see section 4.1) that the bundle $\Lambda^{2}(M, T M)$ splits into complex types as
$$\Lambda^{2}(M, T M)=\Lambda^{1,1}(M, T M) \oplus \lambda^{2}(M, T M)$$
where $\lambda^{2}(M, T M)=\left\{\alpha \in \Lambda^{2}(M, T M): \alpha(J \cdot, J \cdot)=-\alpha\right\}$. The latter bundle splits further as
$$\lambda^{2}(M, T M)=\lambda_{+}^{2}(M, T M) \oplus \lambda_{-}^{2}(M, T M)$$
where
$$\begin{aligned}
& \lambda_{-}^{2}(M, T M):=\left\{\gamma \in \lambda^{2}(M, T M): \gamma(X, J Y)=-J \gamma(X, Y)\right\} \text { and } \\
& \lambda_{+}^{2}(M, T M):=\left\{\gamma \in \lambda^{2}(M, T M): \gamma(X, J Y)=J \gamma(X, Y)\right\} .
\end{aligned}$$

Remark 4.4. The space $\lambda_{+}^{2}(M, T M)$ is canonically isomorphic to $\Lambda^{(1,2)+(2,1)} M$. The inverse of this isomorphism is given by $T \in \Lambda^{(1,2)+(2,1)} M \mapsto \frac{1}{2}(T-T(J \cdot, J \cdot))$.

For subsequent use we record that if $\gamma$ belongs to $\lambda^{2}(M, T M)$ the projectors are given by
$$2 \gamma_{-}(X, Y)=\gamma(X, Y)+J \gamma(X, J Y) \text { and } 2 \gamma_{+}(X, Y)=\gamma(X, Y)-J \gamma(X, J Y) .$$
Notice that $\bar{\partial} h$ belongs to $\lambda_{-}^{2}(M, T M)$ whenever $h \in \operatorname{Sym}^{2,-} T M$. In addition, indicating with a : $\Lambda^{2}(M, T M) \rightarrow \Lambda^{3} M$ the total antisymmetrisation map, that is
$$\mathrm{a}(\alpha)(X, Y, Z)=\mathfrak{S}_{X, Y, Z} g(\alpha(X, Y), Z)$$
we must have $\mathrm{a}(\bar{\partial} h)=0$.
Splitting the Frölicher-Nijenhuis bracket according to (18) yields
$$[h, h]^{\mathrm{FN}}=[h, h]^{\mathrm{FN},+}+[h, h]^{\mathrm{FN},-}$$
where the components
$$\begin{aligned}
& 2[h, h]^{\mathrm{FN},+}(X, Y)=[h, h](X, Y)+[h, h](J X, J Y) \text { and } \\
& 2[h, h]^{\mathrm{FN},-}(X, Y)=[h, h](X, Y)-[h, h](J X, J Y) .
\end{aligned}$$
Define now $\partial^{g} h:=\frac{1}{2}\left(\mathrm{~d}_{\nabla^{g}} h+\mathrm{d}_{\nabla^{g}} h(J \cdot, J \cdot)\right)$ so that $\mathrm{d}_{\nabla^{g}} h=\partial^{g} h+\bar{\partial} h$. Then $h \sharp \partial^{g} h$ belongs to $\lambda^{2}(M, T M)$ hence
$$[h, h]^{\mathrm{FN},+}=-h \sharp \bar{\partial} h+\mathrm{d}_{\nabla^{g}}^{+} h^{2} \text { and }[h, h]^{\mathrm{FN},-}=-h \sharp \partial^{g} h+\mathrm{d}_{\nabla^{g}}^{-} h^{2}$$
by using the comparison formula (10).

Lemma 4.5. Assume that $h \in \Gamma\left(\operatorname{Sym}^{2,-} T M\right)$. Then
$$\left(\nabla_{X}^{g} h\right) Y+\left(\nabla_{J X}^{g} h\right) J Y=\partial^{g} h(X, Y)+\partial^{g}(J h)(X, J Y)$$
for all $X, Y$ in $T M$.
Proof. Start from the identity $\left(\nabla_{X}^{g} h\right) Y+\left(\nabla_{J X}^{g} h\right) J Y=\left(\mathrm{d}_{\nabla^{g}} h\right)(X, Y)+\left(\mathrm{d}_{\nabla^{g}} h J\right)(J X, Y)$ whenever $X, Y \in T M$. Having $\bar{\partial} h$ in $\lambda_{-}^{2}(M, T M)$ entails
$$\bar{\partial}(h J)(J X, Y)=\bar{\partial}(h J)(X, J Y)=-J \bar{\partial}(h J)(X, Y)=-\bar{\partial} h(X, Y) .$$
At the same time, $\partial^{g}(h J)(J X, Y)=-\partial^{g}(h J)(X, J Y)=\partial^{g}(J h)(X, J Y)$ since $\partial^{g}(h J)$ belongs to $\Omega^{1,1}(M, T M)$ and the claim follows. \(\square\)

Based on this we establish the following
Lemma 4.6. Assume that $h \in \Gamma\left(\operatorname{Sym}^{2,-} T M\right)$. The components of $h \sharp \partial^{g} h$ with respect to (19) read
$$\begin{aligned}
& 2\left(h \sharp \partial^{g} h\right)_{-}=h \sharp \partial^{g} h-J h \sharp \partial^{g} J h \\
& 2\left(h \sharp \partial^{g} h\right)_{+}=\mathrm{d}_{\nabla^{g}} h^{2}-\mathrm{d}_{\nabla^{g}} h^{2}(J \cdot, J \cdot)-2 h \circ \bar{\partial} h .
\end{aligned}$$
Proof. We have $2\left(h \sharp \partial^{g} h\right)_{-}(X, Y)=\left(h \sharp \partial^{g} h\right)(X, Y)+J\left(h \sharp \partial^{g} h\right)(X, J Y)$. Since $\partial^{g} h$ belongs to $\Omega^{1,1}(M, T M)$ we have $J \partial^{g} h(h X, J Y)=-J \partial^{g} h(J h X, Y)=-\partial^{g}(J h)(J h X, Y)$; a straightfor-ward computation based on expanding the term $J\left(h \sharp \partial^{g} h\right)(X, J Y)$ then yields the equality $2\left(h \sharp \partial^{g} h\right)_{-}=h \sharp \partial^{g} h-J h \sharp \partial^{g} J h$.

To determine the component $\left(h \sharp \partial^{g} h\right)_{+}$we start from
$$\begin{aligned}
2\left(h \sharp \partial^{g} h\right)_{+}(X, Y) & =\left(h \sharp \partial^{g} h\right)(X, Y)-J\left(h \sharp \partial^{g} h\right)(X, J Y) \\
& =\partial^{g} h(h X, Y)+\partial^{g} h(X, h Y)-J\left(\partial^{g} h(h X, J Y)+\partial^{g} h(X, h J Y)\right) .
\end{aligned}$$
Because $\partial^{g} h$ belongs to $\Omega^{1,1}(M, T M)$ we have $\partial^{g} h(h X, J Y)=-\partial^{g} h(J h X, Y)=\partial^{g} h(h J X, Y)$; thus
$$2\left(h \sharp \partial^{g} h\right)_{+}=h \sharp \partial^{g} h+J h \sharp \partial^{g} J h .$$
Operating the variable change $Y \mapsto h Y$ in Lemma 4.5 yields
$$\left(\nabla_{X}^{g} h\right) h Y-\left(\nabla_{J X}^{g} h\right) h J Y=\partial^{g} h(X, h Y)+\partial^{g}(J h)(X, J h Y) .$$
Re-writing $\left(\nabla_{X}^{g} h\right) h Y=\left(\nabla_{X}^{g} h^{2}\right) Y-h\left(\nabla_{X}^{g} h\right) Y$ and anti-symmetrising in the variables $(X, Y)$ thus leads to
$$\mathrm{d}_{\nabla^{g}} h^{2}-\mathrm{d}_{\nabla^{g}} h^{2}(J \cdot, J \cdot)-2 h \circ \bar{\partial} h=h \sharp \partial^{g} h+J h \sharp \partial^{g} J h$$
and the claim is proved. \(\square\)

K-S Definition 4.7. We define the Kodaira-Spencer bracket according to
$$[h, h]^{c}:=[h, h]_{-}^{\mathrm{FN},-} \text { in } \lambda_{-}^{2}(M, T M)$$
whenever $h \in \operatorname{Sym}^{2,-} T M$.

The first main fact we establish in this section is that the Kodaira-Spencer bracket compares to the Frölicher-Nijenhuis bracket as indicated below.

Proposition 4.8. Assume that $h$ belongs to $\Gamma\left(\operatorname{Sym}^{2,-} T M\right)$. The following hold
\begin{itemize}
\item[(i)] the full type decomposition of $[h, h]^{\mathrm{FN}}$ reads
$$[h, h]^{\mathrm{FN}}=[h, h]^{c}+h \circ \bar{\partial} h+\left(\mathrm{d}_{\nabla^{g}}^{+} h^{2}-h \sharp \bar{\partial} h\right)$$
according to $\Lambda^{2}(M, T M)=\lambda_{-}^{2}(M, T M) \oplus \lambda_{+}^{2}(M, T M) \oplus \Lambda^{1,1}(M, T M)$
\item[(ii)] we have
$$[h, h]^{c}=-\frac{1}{2}\left(h \sharp \partial^{g} h-J h \sharp \partial^{g}(J h)\right)=\frac{1}{2}\left([h, h]^{\mathrm{FN}}-[J h, J h]^{\mathrm{FN}}\right) .$$
\end{itemize}

Proof. (i) We have
$$[h, h]^{\mathrm{FN}}=[h, h]^{\mathrm{FN},+}+[h, h]^{\mathrm{FN},-}=-h \sharp \bar{\partial} h+\mathrm{d}_{\nabla^{g}}^{+} h^{2}-h \sharp \partial^{g} h+\mathrm{d}_{\nabla^{g}}^{-} h^{2}$$
where, to shorten notation, we have set $\mathrm{d}_{\nabla^{g}}^{-} h^{2}:=\frac{1}{2}\left(\mathrm{~d}_{\nabla^{g}} h^{2}-\mathrm{d}_{\nabla^{g}} h^{2}(J \cdot, J \cdot)\right)$. Furthermore, using Lemma 4.6 reveals that
$$h \sharp \partial^{g} h=\left(h \sharp \partial^{g} h\right)_{+}+\left(h \sharp \partial^{g} h\right)_{-}=\mathrm{d}_{\nabla^{g}}^{-} h^{2}-h \circ \bar{\partial} h+\left(h \sharp \partial^{g} h\right)_{-} .$$
After gathering terms we end up with
$$[h, h]^{\mathrm{FN}}=-\left(h \sharp \partial^{g} h\right)_{-}+h \circ \bar{\partial} h+\mathrm{d}_{\nabla^{g}}^{+} h^{2}-h \sharp \bar{\partial} h .$$
The type of the summands above is given by $\left(h \sharp \partial^{g} h\right)_{-}$in $\lambda_{-}^{2}(M, T M)$ as well as $h \circ \bar{\partial} h$ in $\lambda_{+}^{2}(M, T M)$ and $\mathrm{d}_{\nabla^{g}}^{+} h^{2}-h \not{ }^{-} \bar{\partial} h \in \Omega^{1,1}(M, T M)$. This proves (20) and also that
$$[h, h]^{c}=-\left(h \sharp \partial^{g} h\right)_{-} .$$
(ii) Using the equation right above and Lemma 4.6 shows that
$$[h, h]^{c}=-\frac{1}{2}\left(h \sharp \partial^{g} h-J h \sharp \partial^{g}(J h)\right) .$$
To prove the second half of the claim we first record that having $\bar{\partial} h \in \lambda_{-}^{2}(M, T M)$ entails
$$\bar{\partial}(J h)(J h X, Y)=\bar{\partial}(J h)(h X, J Y)=-J \bar{\partial}(J h)(h X, Y)=\bar{\partial} h(h X, Y) .$$
Similarly, $\bar{\partial}(J h)(X, J h Y)=-J \bar{\partial}(J h)(X, h Y)=\bar{\partial} h(X, h Y)$. These facts entail that
$$h \sharp \bar{\partial} h=J h \sharp \bar{\partial}(J h) .$$
Using (10) thus leads to $[h, h]^{\mathrm{FN}}-[J h, J h]^{\mathrm{FN}}=-\left(h \sharp \partial^{g} h-J h \sharp \partial^{g} J h\right)$. The claim is now fully proved. \(\square\)

The type decomposition in (20) will be used in section 4.3 in order to express the restriction of $\mathbf{v}$ to $\Gamma\left(\operatorname{Sym}^{2,-} T M\right)$ in terms of the Kodaira-Spencer bracket.

Remark 4.9. (i) Classically, the Kodaira-Spencer bracket arises in relation to the integrability of almost complex structures of the form $J_{h}:=(1-h)^{-1} J(1-h)$ where $h \in \Gamma\left(\operatorname{End}^{-} T M\right)$. Indeed, $J_{h}$ is complex integrable if and only if $h$ satisfies the Maurer-Cartan equation $\bar{\partial} h+[h, h]^{c}=0$; see [5][Lemma 6.1.2].
\begin{itemize}
\item[(ii)] The Kodaira-Spencer bracket is preserved by the operator $\bar{\partial}$. In particular, if $h$ in $\Gamma\left(\operatorname{Sym}^{2,-} T M\right)$ satisfies $\bar{\partial} h=0$ then $\bar{\partial}[h, h]^{c}=0$.(see e.g. [5][Remark 6.1.1])
\end{itemize}

Below we describe explicitly how to perturb the Kodaira-Spencer bracket in order to obtain, after taking the divergence, a symmetric and divergence-free tensor.

Definition 4.10. We define the perturbed Kodaira-Spencer bracket according to
$$[h, h]_{\mathrm{TT}}^{c}:=[h, h]^{c}+\frac{1}{2}\left(\delta^{g} h \wedge h-\delta^{g}(J h) \wedge J h\right) \text { in } \lambda_{-}^{2}(M, T M)$$
whenever $h$ belongs to $\operatorname{Sym}^{2,-} T M$.
Note that a quick algebraic computation shows that $\delta^{g} h \wedge h-\delta^{g}(J h) \wedge J h$ belongs to $\lambda_{-}^{2}(M, T M)$ hence so does the perturbed complex bracket $[h, h]_{\mathrm{TT}}^{c}$. This bracket extends by polarisation to a symmetric bracket on the space $\Gamma\left(\operatorname{Sym}^{2,-} T M\right)$ via the usual formula $2\left[h_{1}, h_{2}\right]_{\mathrm{TT}}^{c}=\left[h_{1}+h_{2}, h_{1}+h_{2}\right]_{\mathrm{TT}}^{c}-\left[h_{1}, h_{1}\right]_{\mathrm{TT}}^{c}-\left[h_{2}, h_{2}\right]_{\mathrm{TT}}^{c}$. The main properties of this new bracket are summarised below.

Proposition 4.11. Assuming that $h$ is in $\Gamma\left(\mathrm{Sym}^{2,-} T M\right)$ the following hold
\begin{itemize}
\item[(i)] the divergence
$$\delta^{g}[h, h]_{\mathrm{TT}}^{c} \text { belongs to } \mathrm{TT}^{-}(M, g)$$
\item[(ii)] we have $\mathrm{a}[h, h]^{c}=0$ and $\mathrm{a}[h, h]_{\mathrm{TT}}^{c}=0$.
\end{itemize}

Proof. (i) Recall that $[h, h]^{c}=\frac{1}{2}\left([h, h]^{\mathrm{FN}}-[J h, J h]^{\mathrm{FN}}\right)$ by (21). Due to the algebraic identities $J h \circ \mathrm{~d}_{\nabla^{g}}(J h)=h \circ \mathrm{~d}_{\nabla^{g}} h$ and $(\stackrel{\circ}{R}(J h)) \circ J h=\stackrel{\circ}{R}(h) \circ h$ applying successively Proposition 3.2 for $h$ respectively $J h$ ensures that the tensor $\delta^{g}[h, h]_{\mathrm{TT}}^{c}$ is symmetric. Because $[h, h]_{\mathrm{TT}}^{c}$ lies in $\lambda_{-}^{2}(M, T M)$ its divergence is $J$-anti-invariant thus $\delta^{g}[h, h]_{\mathrm{TT}}^{c} \in \operatorname{Sym}^{2,-} T M$. To show it is divergence-free we compute
$$\begin{aligned}
\left\langle\delta^{g}[h, h]_{\mathrm{TT}}^{c}, \delta^{\star_{g}} X\right\rangle_{L^{2}} & =\left\langle\delta^{g}[h, h]_{\mathrm{TT}}^{c}, \delta^{\star_{g},-} X\right\rangle_{L^{2}}=-\frac{1}{2}\left\langle\delta^{g}[h, h]_{\mathrm{TT}}^{c}, \mathscr{L}_{J X} J+\mathrm{d}^{-} X^{b}\right\rangle_{L^{2}} \\
& =-\frac{1}{2}\left\langle\delta^{g}[h, h]_{\mathrm{TT}}^{c}, \mathscr{L}_{J X} J\right\rangle_{L^{2}}
\end{aligned}$$
since $\delta^{g}[h, h]_{\mathrm{TT}}^{c}$ is symmetric and $J$-anti-invariant. However, by $L^{2}$-duality and after taking again into account that $[h, h]_{\mathrm{TT}}^{c}$ is $J$-anti-invariant we obtain
$$\left\langle\delta^{g}[h, h]_{\mathrm{TT}}^{c}, \mathscr{L}_{J X} J\right\rangle_{L^{2}}=\left\langle[h, h]_{\mathrm{TT}}^{c}, \mathrm{~d}_{\nabla^{g}}\left(\mathscr{L}_{J X} J\right)\right\rangle_{L^{2}}=\left\langle[h, h]_{\mathrm{TT}}^{c}, \bar{\partial}\left(\mathscr{L}_{J X} J\right)\right\rangle_{L^{2}}=0$$
and the proof is finished, since $\bar{\partial}\left(\mathscr{L}_{J X} J\right)=0$.
(ii) Since $h$ is symmetric, a direct computation based on (9) shows that the total alternation $\mathrm{a}[h, h]^{\mathrm{FN}}=\mathrm{a}\left(h \circ \mathrm{~d}_{\nabla^{g}} h\right)$. That $\mathrm{a}[h, h]^{c}$ thus follows from the identity $h \circ \mathrm{~d}_{\nabla^{g}} h=J h \circ \mathrm{~d}_{\nabla^{g}} J h$ combined with the expression for $[h, h]^{c}$ given in (21). A direct algebraic computation based
on having $h$ and $h J$ symmetric shows that $\mathrm{a}\left(\delta^{g} h \wedge h-\delta^{g}(J h) \wedge J h\right)=0$ hence $\mathrm{a}[h, h]_{\mathrm{TT}}^{c}=0$ as well. \(\square\)

For divergence-free tensors we have the following immediate consequence of Proposition 4.11 above.

Proposition 4.12. Assuming that $h$ in $\Gamma\left(\operatorname{Sym}^{2,-} T M\right)$ satisfies $\delta^{g} h=0$ we have that
$$\delta^{g}[h, h]^{c} \text { belongs to } \operatorname{TT}^{-}(M, g) .$$

To conclude this section we also compare the divergences of the Frölicher-Nijenhuis respectively Kodaira-Spencer brackets with respect to the type decomposition of the bundle of endomorphisms of $T M$.
Proposition 4.13. Assume that $h \in \Gamma\left(\operatorname{Sym}^{2,-} T M\right)$ satisfies $\bar{\partial} h=0$ and $\delta^{g} h=0$. With respect to the type decomposition
$$\operatorname{End}(T M)=\operatorname{Sym}^{2} T M \oplus \Lambda^{2} M=\operatorname{Sym}^{2,+} T M \oplus \operatorname{Sym}^{2,-} T M \oplus \Lambda^{2} M$$
the tensor $\delta^{g}[h, h]^{\mathrm{FN}}$ splits as
$$\delta^{g}[h, h]^{\mathrm{FN}}=\left(\frac{1}{2} \Delta_{E}+\stackrel{\circ}{R}\right) h^{2}+\left(\delta^{g}[h, h]^{c}-\delta^{\star_{g},-} \delta^{g} h^{2}\right)-\frac{1}{2} \mathrm{~d}^{-} \delta^{g} h^{2} .$$
Proof. Because $[h, h]^{c} \in \lambda_{-}^{2}(M, T M)$ we have $\delta^{g}[h, h]^{c} \in \Gamma\left(\operatorname{Sym}^{2,-} T M\right)$. At the same time we have $[h, h]^{\mathrm{FN}}=[h, h]^{c}+\mathrm{d}_{\nabla^{g}}^{+} h^{2}$ by (20). The claim follows now from Corollary 4.2. \(\square\)
4.3. Structure of the operator v. The aim in this section is to use the previous considerations in order to show that second order infinitesimal Einstein deformations can be explicitely determined. To this aim we need to render explicit the structure of the operator v with respect to the type splitting of symmetric tensors. The first observation in this direction is that the restriction of the operator v to $\mathrm{Sym}^{2,-} T M$ is entirely determined by the Kodaira-Spencer bracket.

3- Proposition 4.14. Assume that $h_{i}$ belong to $\Gamma\left(\operatorname{Sym}^{2,-} T M\right)$ for $1 \leqslant i \leqslant 3$. Then
$$\mathbf{v}\left(h_{1}, h_{2}, h_{3}\right)=2 \mathfrak{S}_{a b c}\left\langle\left[h_{a}, h_{b}\right]^{c}, \bar{\partial} h_{c}\right\rangle_{L^{2}}-\frac{1}{2} \mathfrak{S}_{a b c}\left\langle\delta^{g}\left\{h_{a}, h_{b}\right\}, \delta^{g} h_{c}\right\rangle_{L^{2}}$$
with cyclic permutations on the indices abc.
Proof. According to (20) we have $[h, h]^{\mathrm{FN}}=[h, h]^{c}+h \circ \bar{\partial} h+\left(\mathrm{d}_{\nabla^{g}}^{+} h^{2}-h \sharp \bar{\partial} h\right)$ whenever $h \in \operatorname{Sym}^{2,-} T M$. Since $h \circ \bar{\partial} h$ belongs to $\lambda_{+}^{2}(M, T M)$ its divergence belongs to $\operatorname{End}^{+} T M$; thus
$$\left\langle\delta^{g}[h, h]^{\mathrm{FN}}, h\right\rangle_{L^{2}}=\left\langle[h, h]^{c}, \mathrm{~d}_{\nabla^{g}} h\right\rangle_{L^{2}}+\left\langle\delta^{g} \mathrm{~d}_{\nabla^{g}}^{+} h^{2}, h\right\rangle_{L^{2}}-\left\langle h \sharp \bar{\partial} h, \mathrm{~d}_{\nabla^{g}} h\right\rangle_{L^{2}} .$$
Furthermore,
$$\begin{aligned}
\left\langle h \sharp \bar{\partial} h, \mathrm{~d}_{\left.\nabla^{g} h\right\rangle_{L^{2}}}\right. & =\left\langle\bar{\partial} h, h \sharp \mathrm{~d}_{\nabla^{g} h}\right\rangle_{L^{2}}=\left\langle\bar{\partial} h, \mathrm{~d}_{\nabla^{g}} h^{2}-[h, h]^{\mathrm{FN}}\right\rangle_{L^{2}} \\
& =\left\langle\delta^{g} \bar{\partial} h, h^{2}\right\rangle_{L^{2}}-\left\langle\bar{\partial} h,[h, h]^{c}+h \circ \bar{\partial} h\right\rangle_{L^{2}}=\left\langle\delta^{g} \bar{\partial} h, h^{2}\right\rangle_{L^{2}}-\left\langle\bar{\partial} h,[h, h]^{c}\right\rangle_{L^{2}}
\end{aligned}$$
since $h \circ \bar{\partial} h$ belongs to $\lambda_{+}^{2}(M, T M)$. It follows that
$$\left\langle\delta^{g}[h, h]^{\mathrm{FN}}, h\right\rangle_{L^{2}}=2\left\langle[h, h]^{c}, \bar{\partial} h\right\rangle_{L^{2}}+\left\langle\delta^{g} \mathrm{~d}_{\nabla^{g}}^{+} h^{2}, h\right\rangle_{L^{2}}-\left\langle\delta^{g} \bar{\partial} h, h^{2}\right\rangle_{L^{2}} .$$
Now we use the comparison formula in Corollary 4.2 which yields
$$\delta^{g} \mathrm{~d}_{\nabla g}^{+} h^{2}=\left(\frac{1}{2} \Delta_{E}+\stackrel{\circ}{R}\right) h^{2}-\delta^{\star_{g},-} \delta^{g} h^{2}-\frac{1}{2} \mathrm{~d}^{-} \delta^{g} h^{2} .$$
Because $h$ is symmetric and $J$-anti-invariant, after taking into account that $\Delta_{E}$ and $\stackrel{\circ}{R}$ preserve complex type we find that $\left\langle\delta^{g} \mathrm{~d}_{\nabla^{g}}^{+} h^{2}, h\right\rangle_{L^{2}}=-\left\langle\delta^{g} h^{2}, \delta^{g} h\right\rangle_{L^{2}}$. Similar type arguments based this time on Corollary 4.3 show that $\left\langle\delta^{g} \bar{\partial} h, h^{2}\right\rangle_{L^{2}}=0$. We thus get
$$\frac{1}{3} \mathbf{v}(h, h, h)=\left\langle\delta^{g}[h, h]^{\mathrm{FN}}, h\right\rangle_{L^{2}}=2\left\langle[h, h]^{c}, \bar{\partial} h\right\rangle_{L^{2}}-\left\langle\delta^{g} h^{2}, \delta^{g} h\right\rangle_{L^{2}}$$
and the claim follows now by polarisation. \(\square\)

Our next objective is to explicitly compute quantities of the type
$$\langle\mathbf{v}(h, h), H\rangle_{L^{2}}$$
where $h \in \Gamma\left(\operatorname{Sym}^{2,-} T M\right)$ satisfies $\bar{\partial} h=0$ as well as $\delta^{g} h=0$ and the tensor $H \in \Gamma\left(\operatorname{Sym}^{2,+} T M\right)$. This is considerably more technically involved than Proposition 4.14 and requires a series of preliminary lemmas.
L-1 Lemma 4.15. Assume that $h \in \operatorname{Sym}^{2,-} T M$ and consider the symmetric operator given by $\mathrm{L}(h):=\nabla_{e_{i}}^{g} h \circ \nabla_{e_{i}}^{g} h$. Then
$$\mathrm{L}(h)=\frac{1}{2}\left\{\left(\Delta_{E}+2 \AA\right) h, h\right\}-\frac{1}{2}\left(\Delta_{E}+2 \AA\right) h^{2} .$$
Proof. A straightforward computation shows that $2 \mathrm{~L}(h)=\left\{\nabla^{\star_{g}} \nabla^{g} h, h\right\}-\nabla^{\star_{g}} \nabla^{g} h^{2}$. To conclude, we use that $\Delta_{E}+2 \stackrel{\circ}{R}=\nabla^{\star_{g}} \nabla^{g}$. \(\square\)

The next observation deals with the divergence type expression in the Lemma 4.16 below. In the computations in the rest of this section we will repeatedly use the following fact which is entailed by the definition of $\bar{\partial}$. Namely, if $h \in \Gamma\left(\operatorname{Sym}^{2,-} T M\right)$ then the tensor
$$(X, Y) \mapsto\left(\nabla_{J X}^{g} h\right) J Y-\left(\nabla_{X}^{g} h\right) Y+\bar{\partial} h(X, Y) \text { is symmetric. }$$