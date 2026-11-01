---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 2608_13481.pdf
converter: mathpix
format: mmd
---

\title{
A NEGATIVE KÄHLER-EINSTEIN THREEFOLD WITH NON-INTEGRABLE INFINITESIMAL EINSTEIN DEFORMATIONS
}

\author{
ARI KRISHNA
}

\begin{abstract}
We construct a smooth canonically polarized threefold, not biholomorphic to a product of positive-dimensional varieties, whose normalized Kähler-Einstein metric admits a non-integrable infinitesimal Einstein deformation. The same tangent direction is non-integrable as an infinitesimal complex deformation. In fact, the space of infinitesimal Einstein deformations in our example has real dimension 8, its integrable directions form a real 6-dimensional subspace, and every direction outside that subspace is obstructed. This answers both parts of a suitably generalized version of a question posed by Dai, Wang, and Wei in real dimension 6.
\end{abstract}

\section*{1. Introduction}

Let $(M, g)$ be a compact Einstein manifold. An infinitesimal Einstein deformation (IED) is a transverse-traceless symmetric 2-tensor in the kernel of the linearized Einstein operator. It is integrable if it is tangent, modulo diffeomorphisms and homotheties, to a smooth curve of Einstein metrics. If $(M, g, J)$ is Kähler-Einstein, one may also consider infinitesimal complex deformations (ICDs), namely tangent directions to the space of complex structures. These are parametrized by $H^{1}\left(M, T_{M}\right)$, and their integrability is governed by the Kuranishi space.

Schwahn and Semmelmann [10, §6.3] formulate the following version of a question of Dai, Wang, and Wei [3].

Question 1.1 (Dai-Wang-Wei; Schwahn-Semmelmann). Does there exist a compact Kähler-Einstein manifold $(M, g, J)$ of negative scalar curvature, with $\operatorname{dim}_{\mathbb{R}} M \neq 4$, admitting a non-integrable infinitesimal complex deformation or a non-integrable infinitesimal Einstein deformation?

When the Einstein constant is negative, Koiso gives a real-linear isomorphism between $H^{1}\left(M, T_{M}\right)$ and the space of IEDs [5]. An obstructed ICD, however, could conceivably integrate through Einstein metrics that cease to be Kähler, and holonomy rigidity for nonzero Kähler-Einstein metrics is not known in full generality [10, §6.3]. Moreover, every IED of a negative Kähler-Einstein metric is integrable to second Einstein order [9, Thm. 5.3]. Thus, a quadratic complex obstruction is not a second-order Einstein obstruction.

Nagy's recent computation of the third-order Einstein equation [8] implies that a nonzero primary Kodaira-Spencer obstruction prevents the corresponding IED from extending to third Einstein order, even along a curve of non-Kähler-Einstein metrics. Combining this with an equivariant construction from a rigid but not infinitesimally rigid surface yields the following result whose proof we establish in this paper.

Theorem 1.2. There exist a smooth projective threefold $X$, a class $\alpha_{X} \in H^{1}\left(X, T_{X}\right)$, and a Kähler-Einstein metric $g$ on $X$ with $\operatorname{Ric}_{g}=-g$ such that:
(i) $K_{X}$ is ample, and $X$ is not biholomorphic to a product of positive-dimensional varieties;
(ii) $\left[\alpha_{X}, \alpha_{X}\right] \neq 0$ in $H^{2}\left(X, T_{X}\right)$, so $\alpha_{X}$ is a non-integrable ICD;

\footnotetext{
2020 Mathematics Subject Classification. 53C25, 32G05, 14J30.
Key words and phrases. Kähler-Einstein metrics, infinitesimal Einstein deformations, Kuranishi spaces, obstructed deformations, canonically polarized varieties.
}
\begin{itemize}
\item[(iii)] the IED corresponding to $\alpha_{X}$ under Koiso's isomorphism is non-integrable, and is obstructed at third Einstein order.
\end{itemize}

More precisely, for a smooth curve $B$ of genus 2 there is a decomposition
$$H^{1}\left(X, T_{X}\right)=\mathbb{C} \alpha_{X} \oplus H^{1}\left(B, T_{B}\right),$$
and the ICD and IED associated with $\lambda \alpha_{X}+\beta$ are integrable if and only if $\lambda=0$. Hence, the real 8-dimensional space of IEDs has a real 6-dimensional subspace consisting precisely of its integrable directions.

The threefold has an étale cover that is a product, but is not itself a product. The obstruction is inherited from the surface factor, while the free action on the curve makes the diagonal quotient smooth.

Acknowledgments. We thank Tristan Ozuch, Dhruv Goel, and Laasya Nagumalli for helpful conversations and proofreading.

\section*{2. Constructing the threefold}

We write $q(S)=h^{1}\left(S, \mathcal{O}_{S}\right)$.
Proposition 2.1. There exist a smooth projective surface $S$, a faithful action of $G \cong(\mathbb{Z} / 7)^{4}$ on $S$, and a class $\alpha \in H^{1}\left(S, T_{S}\right)^{G}$ such that
$$K_{S} \text { is ample }, \quad q(S)=0, \quad H^{1}\left(S, T_{S}\right)=\mathbb{C} \alpha,$$
and
$$[\alpha, \alpha] \neq 0 \quad \text { in } H^{2}\left(S, T_{S}\right) .$$
Proof. Böhning, Graf von Bothmer, and Pignatelli construct a smooth surface $S$ with
$$\operatorname{Kur}(S) \cong \operatorname{Spec} \mathbb{C}[x] /\left(x^{2}\right),$$
$K_{S}$ ample, and $q(S)=0$ [2, Thm. 1.1 and Thms. 6.3, 6.5]. Their surface is a totally ramified abelian cover whose deck group is $G \cong(\mathbb{Z} / 7)^{4}$ [2, Cor. 5.4]. The natural transformation of [2, Lem. 2.11] identifies the tangent space of the branch-data deformation functor with $H^{1}\left(S, T_{S}\right)^{G}$. The verification in the proof of [2, Thm. 5.5], using [2, Thm. 3.19], of the hypotheses of [2, Cor. 2.13] shows that this transformation is an isomorphism. Hence,
$$H^{1}\left(S, T_{S}\right)=H^{1}\left(S, T_{S}\right)^{G} .$$

The aforementioned description of $\operatorname{Kur}(S)$ gives $\operatorname{dim}_{\mathbb{C}} H^{1}\left(S, T_{S}\right)=1$; let $\alpha$ be a generator. Since $K_{S}$ is ample, $H^{0}\left(S, T_{S}\right)=0$, so the deformation functor is prorepresentable. The first-order deformation associated with $\alpha$ is induced by
$$\mathbb{C}[x] /\left(x^{2}\right) \longrightarrow \mathbb{C}[t] /\left(t^{2}\right), \quad x \longmapsto a t,$$
for some $a \neq 0$. A lift to $\mathbb{C}[t] /\left(t^{3}\right)$ would have to send $x$ to $a t+b t^{2}$, but
$$\left(a t+b t^{2}\right)^{2}=a^{2} t^{2} \neq 0 \quad\left(\bmod t^{3}\right) .$$
It follows that $\alpha$ has no second-order lift. By the primary obstruction criterion recalled in Lemma 3.1, this is equivalent to $[\alpha, \alpha] \neq 0$. \(\square\)

Let $B$ be a smooth projective curve of genus 2. Its fundamental group surjects onto $G$ : in the standard presentation, send the four generators of $\pi_{1}(G)$ to a basis of the abelian group $G$; the surface-group relation maps to zero. By the Riemann existence theorem, the resulting connected topological cover carries a unique structure of a finite étale Galois cover
$$q: C \longrightarrow B$$
with Galois group $G$. Then, Riemann-Hurwitz gives that the genus of $C$ is
$$g(C)=1+|G|(g(B)-1)=1+7^{4}=2402 .$$
Note that the diagonal action of $G$ on $S \times C$ is free. With this in hand, let
$$X=(S \times C) / G$$
and denote the quotient map by $\pi: S \times C \rightarrow X$.
We turn to examining the deformation theory of this quotient. Let $p_{S}$ and $p_{C}$ be the two projections.

Lemma 2.2 (Descent and splitting). There are natural isomorphisms
$$H^{1}\left(X, T_{X}\right) \cong H^{1}\left(S \times C, T_{S \times C}\right)^{G} \cong H^{1}\left(S, T_{S}\right)^{G} \oplus H^{1}\left(C, T_{C}\right)^{G} .$$
Moreover, étale descent along $q$ identifies
$$H^{1}\left(C, T_{C}\right)^{G} \cong H^{1}\left(B, T_{B}\right) .$$
If $\alpha_{X} \in H^{1}\left(X, T_{X}\right)$ is defined by
$$\pi^{*} \alpha_{X}=p_{S}^{*} \alpha,$$
then, for $\lambda \in \mathbb{C}$ and $\beta \in H^{1}\left(B, T_{B}\right)$,
$$\pi^{*}\left[\lambda \alpha_{X}+\beta, \lambda \alpha_{X}+\beta\right]=\lambda^{2} p_{S}^{*}[\alpha, \alpha] .$$
In particular, the bracket on the left-hand side is nonzero if and only if $\lambda \neq 0$.
Proof. Pullback identifies the Kodaira-Spencer differential graded Lie algebra of $X$ with the invariant sub-DGLA on $S \times C$. Since the group-invariants functor under a finite group is exact in characteristic zero, we get
$$H^{i}\left(X, T_{X}\right) \cong H^{i}\left(S \times C, T_{S \times C}\right)^{G} .$$
Now,
$$T_{S \times C}=p_{S}^{*} T_{S} \oplus p_{C}^{*} T_{C} .$$
The Künneth formula, in conjunction with $H^{0}\left(S, T_{S}\right)=H^{0}\left(C, T_{C}\right)=0$, yields
$$H^{1}\left(S \times C, T_{S \times C}\right)=H^{1}\left(S, T_{S}\right) \oplus H^{1}\left(C, T_{C}\right) .$$
The asserted identification for $C \rightarrow B$ arises from the same étale descent argument.
Let $\widetilde{\beta} \in H^{1}\left(C, T_{C}\right)^{G}$ be the pullback of $\beta$. Classes pulled back from different factors have zero Kodaira-Spencer bracket. Moreover,
$$[\widetilde{\beta}, \widetilde{\beta}]=0,$$
because it is represented by a (0, 2)-form on a curve. This proves (2.1). Finally, the Künneth decomposition
$$\begin{aligned}
H^{2}\left(S \times C, T_{S \times C}\right)= & H^{2}\left(S, T_{S}\right) \oplus\left(H^{1}\left(S, T_{S}\right) \otimes H^{1}\left(C, \mathcal{O}_{C}\right)\right) \\
& \oplus\left(H^{1}\left(C, T_{C}\right) \otimes H^{1}\left(S, \mathcal{O}_{S}\right)\right)
\end{aligned}$$
shows that $p_{S}^{*}: H^{2}\left(S, T_{S}\right) \rightarrow H^{2}\left(S \times C, T_{S \times C}\right)$ is injective. Since $[\alpha, \alpha]$ is $G$-invariant, it remains nonzero after invariant descent. The last assertion follows. \(\square\)

\section*{3. From complex obstructions to Einstein obstructions}

We first recall the primary complex obstruction. For a compact complex manifold $Z$, its Kodaira-Spencer DGLA is
$$L_{Z}=\left(A^{0, \bullet}\left(Z, T_{Z}\right), \bar{\partial},[,]\right) .$$
It governs the Kuranishi deformation functor via the Maurer-Cartan equation
$$\bar{\partial} \phi+\frac{1}{2}[\phi, \phi]=0 ;$$
consult [4, 6, 7, 11]for details.
Lemma 3.1 (Primary obstruction). Let $Z$ be a compact complex manifold and $\xi \in H^{1}\left(Z, T_{Z}\right)$. The class $\xi$ admits a second-order lift if and only if
$$[\xi, \xi]=0 \quad \text { in } H^{2}\left(Z, T_{Z}\right) .$$
In particular, a class with nonzero bracket is not integrable. The construction can be shown to be functorial under morphisms of Kodaira-Spencer DGLAs.

Proof. Choose a $\bar{\partial}$-closed representative, which we will continue to denote by $\xi$. A second-order Maurer-Cartan lift has the form
$$\phi(t)=t \xi+t^{2} \phi_{2} \quad\left(\bmod t^{3}\right) .$$
The coefficient of $t^{2}$ in the Maurer-Cartan equation is
$$\bar{\partial} \phi_{2}+\frac{1}{2}[\xi, \xi]=0 .$$
Such a $\phi_{2}$ exists exactly when the cohomology class of $[\xi, \xi]$ vanishes. Functoriality follows from compatibility with the differential and bracket. \(\square\)

Next, if $(M, g, J)$ is compact Kähler-Einstein with negative Einstein constant, Koiso's results give a real-linear isomorphism
$$\kappa_{g}: H^{1}\left(M, T_{M}\right)_{\mathbb{R}} \xrightarrow{\sim} \varepsilon(g),$$
where $\varepsilon(g)$ denotes the real vector space of IEDs [5, Lem. 6.6, Props. 7.3, 8.2-8.3, and Lem. 9.3]. Here, the subscript means that the complex vector space is regarded as a real one; the correspondence is unchanged by a constant rescaling of the metric.

Proposition 3.2. Let $(M, g, J)$ be a compact Kähler-Einstein manifold with $\operatorname{Ric}_{g}=E g$ and $E<0$. If $\xi \in H^{1}\left(M, T_{M}\right)$ satisfies
$$[\xi, \xi] \neq 0 \quad \text { in } H^{2}\left(M, T_{M}\right),$$
then the IED $\kappa_{g}(\xi)$ is not integrable. More precisely, it cannot be extended to third order as an Einstein deformation.

Proof. Write $h=\kappa_{g}(\xi)$ and suppose, more generally, that $h$ extends to an Einstein deformation through third order. All the normalizations and equations below depend only on the 3-jet [8, Thm. 5.12]; in particular, they apply to the jet of every actual Einstein curve. Rescale the jet to have the same total volume as $g$. Since $h$ is trace-free,
$$\left.\frac{d}{d t}\right|_{t=0} \operatorname{Vol}\left(g_{t}\right)=\frac{1}{2} \int_{M} \operatorname{tr}_{g}(h) d V_{g}=0,$$
so this rescaling does not change the tangent vector. The Einstein constant is then $E$ to the required order. Indeed, on the fixed-volume hypersurface , the Einstein-Hilbert functional is stationary at every Einstein metric, whereas its value at $g_{t}$ is $(\operatorname{dim} M) E_{t} \operatorname{Vol}(g)$.

We use $g$ to identify symmetric 2-tensors with self-adjoint endomorphisms. Since $h$ is already divergence-free, the normalizing diffeomorphism in the proof of [8, Prop. 3.2] may be chosen with trivial first jet. Thus, the normalization in [8, Thm. 1.2(i)] preserves $h$, and we may write
$$g^{-1} g_{t}=\mathrm{id}+t h+\frac{t^{2}}{2} h_{2}+\frac{t^{3}}{6} h_{3}+O\left(t^{4}\right) .$$
Nagy's third-order Einstein equation [8, Thm. 1.2(ii)(b)] implies
$$\mathcal{B}\left(h_{2}-h^{2}\right)+[h, h]^{c}=0 .$$
Here, $\mathcal{B}$ is the real form of the Dolbeault operator and $[,]^{c}$ is the real Kodaira-Spencer bracket. Consequently, the cohomology class of $[h, h]^{c}$ vanishes. Nagy identifies the complexification of this real class with the primary Dolbeault obstruction in $H^{0,2}\left(M, T_{M}\right)$; under Koiso's correspondence, it is a nonzero universal scalar multiple of $[\xi, \xi]$ [8, §2.2 and the discussion following Thm. 1.2]. Hence, $[\xi, \xi]=0$, a contradiction. \(\square\)

\section*{4. Proof of the main theorem}

We now prove all the assertions of Theorem 1.2 in one fell swoop.
4.1. The metric and its infinitesimal deformations. The diagonal action on $S \times C$ is free, so $X$ is smooth and projective and $\pi$ is finite étale. Moreover,
$$\pi^{*} K_{X}=K_{S \times C}=p_{S}^{*} K_{S} \otimes p_{C}^{*} K_{C}$$
is ample. Ampleness descends under a finite surjection, so $K_{X}$ is ample.
Let $g_{S}$ and $g_{C}$ be the unique Kähler-Einstein metrics normalized by
$$\operatorname{Ric}_{g_{S}}=-g_{S}, \quad \operatorname{Ric}_{g_{C}}=-g_{C} ;$$
their existence is guaranteed by the Aubin-Yau theorem [1, 12]. Every element of $G$ is a holomorphic automorphism of $S$ or $C$, so uniqueness makes it an isometry of the corresponding normalized metric. Hence, the product metric $g_{S} \oplus g_{C}$ is $G$-invariant, and therefore descends to a metric $g$ on $X$. Since
$$\operatorname{Ric}_{g_{S} \oplus g_{C}}=-\left(g_{S} \oplus g_{C}\right),$$
the descended metric satisfies $\operatorname{Ric}_{g}=-g$. It is the unique normalized Kähler-Einstein metric on $X$.
Proposition 2.1 and Lemma 2.2 give
$$H^{1}\left(X, T_{X}\right)=\mathbb{C} \alpha_{X} \oplus H^{1}\left(B, T_{B}\right) .$$
Since $g(B)=2$,
$$\operatorname{dim}_{\mathbb{C}} H^{1}\left(B, T_{B}\right)=3, \quad \operatorname{dim}_{\mathbb{C}} H^{1}\left(X, T_{X}\right)=4 .$$
Koiso's isomorphism (3.1) therefore gives
$$\operatorname{dim}_{\mathbb{R}} \varepsilon(g)=8 .$$

Let $\xi=\lambda \alpha_{X}+\beta$. If $\lambda \neq 0$, Lemma 2.2 gives
$$[\xi, \xi] \neq 0 .$$
Lemma 3.1 shows that $\xi$ is a non-integrable ICD, and Proposition 3.2 shows that $\kappa_{g}(\xi)$ is a non-integrable IED, obstructed at third Einstein order.

It remains to show that every direction with $\lambda=0$ is integrable in both senses. Every $\beta \in$ $H^{1}\left(B, T_{B}\right)$ is tangent to a curve of complex structures $B_{t}$, because the deformation space of a smooth curve is unobstructed. Now keep the underlying topological $G$-cover $C \rightarrow B$ fixed, and pull back the complex structures on $B_{t}$; this produces a curve of étale holomorphic $G$-covers $C_{t} \rightarrow B_{t}$. The quotients
$$X_{t}=\left(S \times C_{t}\right) / G$$
form a curve of canonically polarized complex manifolds tangent to $\beta$. Thus, $\beta$ is an integrable ICD. By the parametric Aubin-Yau theorem, or equivalently Koiso's deformation theorem in the negative case, the normalized Kähler-Einstein metrics on $X_{t}$ vary smoothly [5, Prop. 10.1]. Their tangent can be prescribed to represent $\kappa_{g}(\beta)$, so this IED is integrable, as was sought.
4.2. Non-productness. It remains to show that $X$ is not biholomorphic to a product. Though Schwann-Semmelmann's survey does not necessarily mandate this, we remark that the problem is only interesting when this condition is imposed.

To this end, first note that the map $q \circ p_{C}: S \times C \rightarrow B$ descends to a smooth isotrivial fibration
$$f: X \longrightarrow B$$
whose fibers are isomorphic to $S$. Its monodromy is the composite
$$\pi_{1}(B) \rightarrow G \hookrightarrow \operatorname{Aut}(S) .$$
The first map is surjective and the second is faithful, so this monodromy is nontrivial. Since $K_{S}$ is ample, $\operatorname{Aut}(S)$ is finite; thus, the monodromy is well-defined up to conjugacy, and a product fibration would have trivial monodromy.

Since $q(S)=0$, invariant descent and Künneth give
$$H^{0}\left(X, \Omega_{X}^{1}\right)=H^{0}\left(S \times C, \Omega_{S \times C}^{1}\right)^{G}=H^{0}\left(C, \Omega_{C}^{1}\right)^{G}=H^{0}\left(B, \Omega_{B}^{1}\right) .$$
Consequently, the Albanese map $a_{X}: X \rightarrow \operatorname{Alb}(X)$ is constant on the fibers of $f$ and factors as
$$a_{X}=j \circ f$$
for a nonconstant map $j: B \rightarrow \operatorname{Alb}(X)$. The map $j$ is finite onto its image. Since $f$ has connected fibers, it is the Stein factorization of $a_{X}$. In particular, the Albanese image of $X$ is one-dimensional.

Suppose that $X \cong A \times D$ with both factors positive-dimensional. Any decomposition with more factors may of course be grouped in this form. Restricting $K_{X}$ to the fibers of the two projections shows that $K_{A}$ and $K_{D}$ are ample, so both factors are projective. The Albanese image of a product is the product of the Albanese images. Since the Albanese image of $X$ is a curve, after interchanging the factors we may assume that $q(A)=0$ and that the Albanese map depends only on $D$. For fixed $d \in D$, the connected set $f(A \times\{d\})$ lies in the finite fiber of $j$ over the point $a_{X}(A \times\{d\})$, and hence it is a point. Thus, $f$ factors through the projection to $D$ : there is a holomorphic map $h: D \rightarrow B$ such that
$$f=h \circ p_{D} .$$

If $\operatorname{dim} D=1$, then $h$ is finite. Connectedness of the fibers of $f$ forces $h$ to have degree 1, so $h$ is an isomorphism. The fibration $f$ is then a product projection $A \times B \rightarrow B$ and has trivial monodromy, contradicting the monodromy computed above. If $\operatorname{dim} D=2$, then $A$ is a curve with $q(A)=0$, hence, $A \cong \mathbb{P}^{1}$, contradicting ampleness of $K_{A}$. The remaining possibility would make one factor a point. Thus, $X$ has no nontrivial product decomposition.

This completes the proof of Theorem 1.2.

\section*{References}
\begin{itemize}
\item[] [1] T. Aubin, Équations du type Monge-Ampère sur les variétés kählériennes compactes, Bull. Sci. Math. 102 (1978), 63-95.
\item[] [2] C. Böhning, H.-C. Graf von Bothmer, and R. Pignatelli, A rigid, not infinitesimally rigid surface with $K$ ample, Boll. Unione Mat. Ital. 15 (2022), 57-85.
\item[] [3] X. Dai, X. Wang, and G. Wei, On the variational stability of Kähler-Einstein metrics, Comm. Anal. Geom. 15 (2007), 669-693.
\item[] [4] K. Kodaira, Complex Manifolds and Deformation of Complex Structures, Grundlehren der mathematischen Wissenschaften 283, Springer, 1986.
\item[] [5] N. Koiso, Einstein metrics and complex structures, Invent. Math. 73 (1983), 71-106.
\item[] [6] M. Kuranishi, New proof for the existence of locally complete families of complex structures, in: Proc. Conf. Complex Analysis (Minneapolis, 1964), Springer, 1965, pp. 142-154.
\end{itemize}
[7] M. Manetti, Lectures on deformations of complex manifolds, Rend. Mat. Appl. (7) 24 (2004), 1-183.
[8] P.-A. Nagy, Third order Einstein deformations for Kähler-Einstein metrics, preprint, arXiv:2606.04501v1 (2026).
[9] P.-A. Nagy and U. Semmelmann, Second order Einstein deformations, J. Math. Soc. Japan 77 (2025), no. 2, 345-389.
[10] P. Schwahn and U. Semmelmann, Einstein metrics, their moduli spaces and stability, preprint, arXiv:2507.18463v3 (2026).
[11] E. Sernesi, Deformations of Algebraic Schemes, Grundlehren der mathematischen Wissenschaften 334, Springer, 2006.
[12] S.-T. Yau, On the Ricci curvature of a compact Kähler manifold and the complex Monge-Ampère equation, I, Comm. Pure Appl. Math. 31 (1978), 339-411.

Department of Mathematics, Harvard University, Cambridge, Massachusetts 02138, USA