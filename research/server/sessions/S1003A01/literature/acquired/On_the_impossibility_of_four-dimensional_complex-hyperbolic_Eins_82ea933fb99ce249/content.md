---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 2111_12667.pdf
converter: mathpix
format: mmd
---

\title{
ON THE IMPOSSIBILITY OF FOUR-DIMENSIONAL COMPLEX-HYPERBOLIC EINSTEIN DEHN FILLING
}

\author{
LUCA F. DI CERBO AND MARCO GOLLA
}

\begin{abstract}
We show that the complex-hyperbolic Einstein Dehn filling compactification cannot possibly be performed in dimension four.
\end{abstract}

\section*{Contents}
1. Introduction and statement of the main result ..... 1
Organization ..... 3
Acknowledgments ..... 3
2. Background and motivation ..... 3
3. Einstein metrics on 4-manifolds, Hitchin-Thorpe-type inequalities, and $L^{2}$-characteristic numbers ..... 7
4. Non-Einstein Dehn filling compactifications ..... 8
4.1. Hirzebruch's example(s) ..... 9
4.2. Playing with Hirzebruch's example ..... 9
4.3. The proof of Theorem 1.1 ..... 11
5. Non-Einstein non-compact Dehn fillings ..... 11
6. Final remarks and questions ..... 13
References ..... 14

\section*{1. Introduction and statement of the main result}

Hyperbolic Dehn filling is a remarkable construction, due to Thurston [Thu78], that allows to build hyperbolic metrics on closed 3-manifolds starting from non-compact complete hyperbolic 3-manifolds of finite volume. Anderson [And06] adapted this construction to higher dimension, allowing to build Einstein metrics on $n$-manifolds starting from non-compact hyperbolic $n$-manifolds of finite volume, whose ends (or cusps) are all diffeomorphic to $T^{n-1} \times \mathbb{R}^{+}$, where $T^{n-1}$ is a $(n-1)$-dimensional torus. This construction is called hyperbolic Einstein Dehn filling. Given the nature of the arguments in [And06], there was hope that a similar construction could work starting from a complex-hyperbolic $n$-manifold (note that $n$ is the complex dimension). This problem is for example mentioned in the survey [And10, Page 28]. We show that such a construction is not allowed, i.e., that complex-hyperbolic Einstein Dehn filling on ball quotients in dimension four is impossible.

It is well-known that complex-hyperbolic surfaces have infra-nilmanifold cusp cross-sections. Torus-like cusps, i.e., cusps whose ideal boundary fibers over a torus, are
parametrized by their Euler number, which is a positive integer $e>0$. Moreover, the result of Dehn filling a torus-like cusp is uniquely determined up to diffeomorphism (see Proposition 2.1). If a complex-hyperbolic surface has only torus-like cusps, we will call the result of filling all cusps the Dehn filling compactification of the surface.

Theorem 1.1. For each positive integer e there exists a complex-hyperbolic surface $X_{e}$ with cusps, all torus-like and with Euler number $e$, whose Dehn filling compactification does not admit any Einstein metric.

The nature of the proof of the theorem is topological. We will show that the closed 4-manifolds obtained by filling the cusps of $X_{e}$ violates the Hitchin-Thorpe inequality, and therefore cannot support an Einstein metric. In fact, since the Hitchin-Thorpe inequality only depends on the homotopy type of the 4-manifold, this is true for any 4-manifold homeomorphic to the Dehn filling compactification.

Based on similar ideas, we prove the following non-compact version of Theorem 1.1. In this case, though, we bring in more geometry: Dai and Wei's logarithmic version of the Hitchin-Thorpe inequality and Cheeger and Gromoll's splitting theorem.

Theorem 1.2. For each integer $e>1$ there exists a complex-hyperbolic surface $Y_{e}$ with $e+3$ cusps, all torus-like, three of which have Euler number $e$ and the rest with Euler number 1, such the 4-manifold obtained from $Y_{e}$ by Dehn filling the first three cusps does not admit an Einstein metric with fibered cusp structure at infinity.

The remarkable property of the surfaces $X_{e}$ and $Y_{e}$, that ultimately makes them useful to prove the non-existence of Einstein Dehn filling compactifications, is that they admit smooth toroidal compactifications with non-nef canonical divisors. Recall that a toroidal compactification is a Dehn filling compactification that minimally and uniquely compactifies the complex structure of the complex-hyperbolic surface with nilmanifold cusps, see [DCDC15, Section 1.1] and [DCDC17, Proposition 2.3] for more details. We note that such examples cannot exist if the complex dimension is bigger than or equal to three, as shown by G. Di Cerbo and the first author [DCDC17]. Thus, somewhat interestingly, this paper highlights a new corollary of the fact that complex-hyperbolic geometry is special in complex dimension two. This peculiarity, when combined with the Hitchin-Thorpe inequality, is ultimately responsible for the non-existence of the complex-hyperbolic Einstein Dehn filling in real dimension four.

We point out that most complex-hyperbolic surfaces with cusps do not satisfy Theorem 1.1. Indeed, as proved in [DC12, Theorem A], most complex-hyperbolic surfaces with cusps have smooth toroidal compactifications with ample canonical divisors, and they then support Kähler-Einstein metrics thanks to the celebrated work of Yau [Yau78]. The same is true in higher dimensions as well, in fact up to a finite étale cover any complex hyperbolic $n$-manifold admits a smooth toroidal compactification with ample canonical divisor [DCDC17, Theorem 1.3]. Again by Yau [Yau78], the smooth toroidal compactification of the cover supports a Kähler-Einstein metric. Remarkably, Bakker and Tsimerman [BT18] have recently shown that any smooth toroidal compactification of a complex hyperbolic $n$-manifold has ample canonical divisor if $n \geq 6$. Thus, in this range of dimensions there is no need to pass to a cover to equip a smooth toroidal compactification with a Kähler-Einstein metric.

Organization. In Section 2 we give some further background and motivation, and establish terminology and notation. In Section 3 we recall some background on the Hitchin-Thorpe inequality and its logarithmic analogue. In Section 4 we give the proof of Theorem 1.1, based on the Hitchin-Thorpe inequality, and in Section 5 we give the proof of Theorem 1.2, based on the Dai-Wei inequality.

Acknowledgments. The authors would like to thank the Mathematics Department of Stony Brook University for the ideal research environment they enjoyed during the 2010/2011 and 2017/2018 academic years, as well as the Simons Center for Geometry and Physics for the outstanding coffee breaks where this collaboration began, unbeknownst to the authors. They also thank Stefano Riolo for suggesting Proposition 2.1, and the referee for pertinent and constructive comments that helped us improve the presentation. LFDC would like to thank Michael Anderson for useful email exchanges on this topic, and Claude LeBrun for suggesting to study Anderson's Dehn filling in dimension four. MG would like to thank Vestislav Apostolov, Yann Rollin, and François Laudenbach. LFDC is partially supported by the NSF grant DMS-2104662.

\section*{2. Background and motivation}

Suppose that $X$ is an $n$-manifold of finite type; a codimension-0 submanifold $E \subset X$ is a an end (or cusp) if:
\begin{itemize}
\item[-] $E$ is a cylinder, i.e., it is diffeomorphic to $Y \times[0, \infty)$ for some closed $(n-1)$ -manifold $Y$, and
\item[-] there is a compact submanifold $K \subset X$ such that $E$ is the closure of one of the components of $X \backslash \operatorname{Int}(K)$.
\end{itemize}
We call $Y$ the ideal boundary of $E$, and the disjoint union of the ideal boundaries of all ends of $X$ the ideal boundary of $X$.

We can truncate a cusp by removing $Y \backslash(1, \infty)$ from $E \cong Y \times[0, \infty)$. This produces a manifold $X_{\text {tr }}$ with one less end than $X$ and with a boundary component diffeomorphic to $Y$. A cusp is toral if its ideal boundary $Y$ is an $(n-1)$-torus. We say that it is torus-like if $Y$ is a circle bundle over an $(n-2)$-torus. If $E$ is torus-like, then $Y$ is the boundary of a 2-disc bundle $D_{E}$ over $T^{n-2}$.

By Dehn filling along a torus-like end $E$ of $X$ we mean the following: first we truncate $E$ to obtain a boundary component of $X_{\text {tr }}$ diffeomorphic to $Y$, and we glue in the 2-disk bundle $D_{E}$ to obtain a manifold $\bar{X}$ which has one less end than $X$. (Here $\partial D_{E}$ is $Y$ with its orientation reversed.) Such a gluing is determined by the choice of an orientation-reversing diffeomorphism $\partial D_{E} \rightarrow \partial E$. Another way of looking at Dehn filling is to view $X$ as the complement of an embedded ( $n-2$ )-torus $T \subset \bar{X}$ (i.e., the 0 -section of $D_{E}$ ).

Broadly speaking, the question we are interested in is whether, given a geometric (e.g., hyperbolic or complex-hyperbolic) structure on $X$, one can find another geometric (e.g., hyperbolic or Einstein) structure on $\bar{X}$.

Let us first look at hyperbolic manifolds. First, recall that the ideal boundary of a hyperbolic $n$-manifold is flat. If an orientable non-compact 3-manifold $M$ admits a complete real-hyperbolic metric of finite volume, then its ideal boundary is a collection
of tori (since tori are the only orientable flat surfaces). It is a well-known fact that for each cusp there are at most finitely many slopes $s$ such that Dehn filling along $s$ produces a manifold that has no complete hyperbolic metric of finite volume. The proof of this theorem was outlined by Thurston in his celebrated Princeton University notes [Thu78], and then more details were provided by Neumann and Zagier (in the presence of an ideal triangulation) [NZ85] and by Petronio and Porti (in the general case) [PP00].

By contrast, for $n>3$, one cannot, as in the 3-dimensional case, construct hyperbolic metrics on all but finitely many Dehn fillings of a complete, finite-volume hyperbolic $n$-manifold with an $(n-1)$-torus end. This is a consequence of Gromov and Thurston's so-called $2 \pi$ Theorem ([And06, Section 2]). To see this, suppose that $X$ is a hyperbolic $n$-manifold with a complete hyperbolic metric of finite volume, where $n>3$. The $2 \pi$ Theorem ensures that any sufficiently large Dehn filling $\bar{X}$ of $X$ admits a metric of non-positive sectional curvature in which the core $T$ of the filling (which is an ( $n-2$ )-torus) is a totally geodesic submanifold. (Here by sufficiently large we mean that the surgery geodesic $\sigma$ is sufficiently long.) In particular, $\pi_{1}(T) \cong \mathbb{Z}^{n-2}$ injects into $\pi_{1}(\bar{X})$, which therefore contains a free Abelian subgroup of rank 2. By Preissman's theorem [Pre42] (see also [dC92, Chapter 12]), such Dehn-filled manifolds cannot support a real-hyperbolic metric.

With that said, it is remarkable that Anderson [And06] was able to extend many features of Thurston's Dehn surgery for hyperbolic 3-manifolds to higher dimensions by softening the hyperbolicity requirement on the Dehn-filled manifold. (Biquard [Biq07] and Bamler [Bam12] have since strengthened this construction.) More precisely, Anderson requires the Dehn-filled manifold not to be hyperbolic, but rather to have an Einstein metric with negative cosmological constant. Recall that Einstein metrics are Riemannian metrics $g$ for which the Ricci tensor is proportional to the metric
$$\operatorname{Ric}_{g}=\lambda g$$
for some constant $\lambda \in \mathbb{R}$, where $\lambda$ is referred to as the cosmological or Einstein constant. We say that an Einstein manifold is negative, positive, or flat, according to whether $\lambda$ is negative, positive, or 0. In dimensions at most three, being Einstein is equivalent to having constant sectional curvature. In higher dimensions, Einstein metrics are usually hard to construct. However, they are a very desirable class of metrics of interests, especially in dimension 4: for instance, they are the fixed points of the volume-preserving Hamilton-Ricci flow, and, as pointed out in [LeB99, Section 11], it is tantalizing to imagine that Einstein four-dimensional pieces play the same role as hyperbolic pieces do in the case of Thurston's geometrization conjecture. We refer to the survey paper of Lott and Kleiner [KL08] on the monumental work of Perelman resolving the Geometrization conjecture [Per02, Per03].

We now describe Anderson's construction in some detail. One starts with any orientable $n$-manifold $N$ with cusps, equipped with a complete real-hyperbolic metric $g_{-1}$ of finite volume. Note that $g_{-1}$ is automatically Einstein with cosmological constant $-(n-1): \operatorname{Ric}_{g_{-1}}=-(n-1) g_{-1}$. The manifold $N$ has finitely many cusps $\operatorname{Ends}(N)$, and we suppose that each of them is toral. Given any subset $\mathcal{E} \subset \operatorname{Ends}(N)$, we can
perform Dehn filling along each end in $\mathcal{E}$ by filling a simple closed geodesics $\sigma_{E}$ in the ideal boundary of each $E \in \mathcal{E}$. For simplicity, let
$$\bar{\sigma}=\left(\sigma_{1}, \ldots, \sigma_{p}\right)$$
be the collection of filled simple geodesics, and we denote by $N_{\bar{\sigma}}$ the corresponding filled manifolds. Note that $N_{\bar{\sigma}}$ is closed if and only if $\mathcal{E}=\operatorname{Ends}(N)$, in other words if we fill all the cusps of $N$. In this case, $N_{\bar{\sigma}}$ is a Dehn filling compactification. As above, we say that the Dehn filling is sufficiently large, if each geodesic $\sigma_{i} \in \bar{\sigma}$ is sufficiently long. Anderson's Dehn filling theorem then tells us that, if a Dehn filling is sufficiently large, then it admits a negative Einstein metric that is asymptotic to the real-hyperbolic metric on the ends which are not filled. The proof of this remarkable theorem is analytical in nature. First, one needs to construct a clever Riemannian metric on the Dehn-filled manifold $N_{\bar{\sigma}}$ which is approximately Einstein. Then, a lengthy and technical argument using the implicit function theorem produces an exact Einstein metric on $N_{\bar{\sigma}}$ which is close to the original approximate Einstein metric in some Hölder topology. We refer to [And06, Biq07, Bam12] for further details.

Anderson's theory produces large classes of both compact and complete Einstein manifolds in dimensions $n \geq 4$. It is tantalizing to ask to what extent this theory could be extended by varying the geometry on the manifold that we want to fill, but still obtaining an Anderson-type result. One of the categories that was considered for such a construction is that of complex-hyperbolic manifolds.

Recall that a complex-hyperbolic manifold is a complex manifold, and in particular it is an $n$-dimensional manifold with $n$ even. When $n=4$, we speak about complex-hyperbolic surfaces, rather than about complex-hyperbolic 4-manifolds. A finite-volume complex-hyperbolic surface is a quotient of
$$\mathbb{B}^{2}:=\left\{\left|z_{1}\right|^{2}+\left|z_{2}\right|^{2}<1, \quad\left(z_{1}, z_{2}\right) \in \mathbb{C}^{2}\right\}$$
equipped with the symmetric Bergman Kähler metric
$$\omega_{\mathrm{B}}:=2 i \bar{\partial} \partial \log \left(1-\|z\|^{2}\right)$$
by a torsion free non-uniform lattice $\Gamma$ in $\operatorname{PU}(2,1)$, which is the group of holomorphic isometries of $\left(\mathbb{B}^{2}, \omega_{\mathrm{B}}\right)$. It follows that any complete finite-volume quotient $\Gamma \backslash \mathbb{B}^{2}$ is Kähler-Einstein with
$$\operatorname{Ric}_{\omega_{\mathrm{B}}}=-\frac{3}{2} \omega_{\mathrm{B}},$$
where by slightly abusing notation we denote by $\omega_{B}$ the induced Kähler metric on the quotient $\Gamma \backslash \mathbb{B}^{2}$. If now $\Gamma$ is non-uniform, we then have that $\Gamma \backslash \mathbb{B}^{2}$ is a non-compact, finite-volume, complete complex-hyperbolic surface with finitely many cuspidal ends. Each cuspidal end has an ideal boundary $N$, where $N$ is a compact infra-nilmanifolds, i.e., a compact orientable quotient of the 3-dimensional Heisenberg Lie group. If all parabolic isometries in $\Gamma$ have no rotational part, then all of the N's are nilmanifolds. (We point out that this condition on the parabolic isometries, and therefore on the cross-sections of the cusps, can always be attained by passing to a finite index normal subgroup in $\Gamma$. We point the reader to [DCDC15, Section 1.1] for more details.)

The folklore idea concerning complex-hyperbolic Einstein Dehn filling proceeds now in parallel with the real-hyperbolic case. Start with a complex-hyperbolic surface whose cusps have nilmanifold cross sections (recall in the real-hyperbolic case we required tori cross sections), truncate a sub-collection of these cusps, and glue back in the associated non-trivial disk bundles over tori. Note that a 3 -nilmanifold $N^{3}$ is diffeomorphic to a non-trivial $S^{1}$-bundle over a torus, which in turn is determined by the Euler number of the associated $D^{2}$-bundle. The complex orientation on a complex-hyperbolic surface induces an orientation on the boundaries of the corresponding truncated 4-manifold. With this orientation, the $S^{1}$-bundles ideal boundaries of the cusps have positive Euler number-note that these manifolds have no orientation-reversing self-diffeomorphisms. Viewed from the perspective of the Dehn-filled manifold $\bar{X}$, each of the 2-tori $T$ in the complement $\bar{X} \backslash X$ has negative self-intersection.

Contrarily to the real-hyperbolic case, there is no choice involved for the filling.
Proposition 2.1. There is a unique way to fill a torus-like cusp of a complex-hyperbolic surface (as defined in (1) and (2)), up to diffeomorphism.

Proof. Recall that Dehn filling a torus-like cusp requires two steps: first we truncate the cusp, creating a boundary component $Y$, and then we glue onto the resulting boundary component a disc bundle $D$ over $T^{2}$ whose boundary is $-Y$. At each step we are making a choice, and we need to show that the diffeomorphism type of the Dehn filling is independent of these choices.

When we truncate the cusp, we are choosing the level at which we are truncating the end $Y \times[0, \infty)$. This choice is restricted by the complex-hyperbolic metric, so that every two choices differ by a translation in the $[0, \infty)$-direction. In particular, any two choices are smoothly isotopic, and it follows that the truncated manifold is unique up to diffeomorphism.

We now need to show that the gluing diffeomorphism does not affect the result of the filling, either. In order to see that, we view the disc bundle $D$ as the union of a (fibered) neighborhood $F$ of a fiber and its complement $H$. Therefore, gluing $D$ amounts to first gluing $F$ and then gluing $H$. We view $F$ as a 4-dimensional 2-handle: its gluing data is specified by the attaching curve (a simple closed curve in $Y$ ) and a framing. However, every self-diffeomorphism of a 3-dimensional nilmanifold preserves the $S^{1}$-fibration up to isotopy [Wal67, Wal68], so we can choose the attaching curve to be a fiber. The framing, too, is determined by the fibration. Now, $H$ is a disk bundle over a torus minus a disk, so it is a 4-dimensional 1-handlebody. Laudenbach and Poenaru have shown that each self-diffeomorphism of the boundary of $H$ extends to $H$ [LP72], so the gluing diffeomorphism of $Y$ extends to $D$, as claimed. \(\square\)

Given this general set-up, the hope was then to be able to at least replicate some of Anderson's arguments in order to produce new classes of Einstein manifolds in dimension four. Theorems 1.1 and 1.2 above show that such a plan is in general doomed for topological reasons. With that said, such a construction is not obstructed up to a finite cover, and it is tantalizing to ask whether a Dehn filling compactification can be performed up to a finite cover, and if the hypothetical Einstein metric coincides with the Kähler-Einstein metric constructed by Yau. Recall that up to a finite cover
any finite-volume complex-hyperbolic surface with cusps admits a smooth toroidal compactification with ample canonical class, see [DC12, Theorem A].

\section*{3. Einstein metrics on 4-manifolds, Hitchin-Thorpe-type inequalities, and $L^{2}$-CHARACTERISTIC NUMBERS}

In this section, we recall some results concerning Einstein metrics in dimension 4 and $L^{2}$-characteristic numbers. We follow the notation and curvature normalization adopted in LeBrun's survey paper [LeB99]. We also refer to [LeB99] as a general reference for the geometry and topology of 4-manifolds and Einstein metrics.

The Gauss-Bonnet formula for the Euler characteristic of a closed (oriented) 4-manifold $(M, g)$ is given by
$$\chi(M)=\frac{1}{8 \pi^{2}} \int_{M}\left(\left|W^{+}\right|_{g}^{2}+\left|W^{-}\right|_{g}^{2}+\frac{s_{g}^{2}}{24}-\frac{|\operatorname{Ric}|_{g}^{2}}{2}\right) d \mu_{g}$$
where $W^{ \pm}$are the self-dual and anti-self-dual Weyl curvatures, $s_{g}$ is the scalar curvature, and Ric is the trace-free part of the Ricci tensor. Observe that $g$ is Einstein if and only if $\mathrm{Ric}^{\circ}=0$. Also, by the Hirzebruch signature theorem we can express the signature of $(M, g)$ as a curvature integral:
$$\tau(M)=\frac{1}{12 \pi^{2}} \int_{M}\left(\left|W^{+}\right|_{g}^{2}-\left|W^{-}\right|_{g}^{2}\right) d \mu_{g}$$

Next, we recall the Hitchin-Thorpe inequality.
Theorem 3.1 ([Hit74]). Let ( $X, g$ ) be a compact orientable Einstein 4-manifold with signature $\tau$ and Euler characteristic $\chi$. Then
$$\chi \geq \frac{3}{2}|\tau| .$$
Furthermore, if equality occurs then either $X$ is flat or the universal cover of $X$ is a K3 surface (up to orientation reversal).

The proof of the inequality in Theorem 3.1 follows easily by combining Equations (3) and (4), and this was originally observed in [Tho69]. The characterization of the equality case in such an inequality is more delicate, and we refer to [Hit74] for a beautiful proof of this fact.

The formulas given in Equations (3) and (4) admit some interesting generalizations to the complete finite-volume setting. These equations will be used in Section 5, where we prove Theorem 1.2. First, Equation (3) generalizes to the finite-volume setting with bounded curvature: this follows from the Gauss-Bonnet-type formula due to Cheeger and Gromov [CG85] (see also Harder [Har71]):
$$\chi_{L^{2}}(M):=\frac{1}{8 \pi^{2}} \int_{M}\left(\left|W^{+}\right|_{g}^{2}+\left|W^{-}\right|_{g}^{2}+\frac{s_{g}^{2}}{24}-\frac{|\mathrm{Ric}|_{g}^{2}}{2}\right) d \mu_{g}=\chi(M) .$$

In this setting, one may also consider the $L^{2}$-curvature integral analogous to Equation (4):
$$\tau_{L^{2}}(M)=\frac{1}{12 \pi^{2}} \int_{M}\left(\left|W^{+}\right|_{g}^{2}-\left|W^{-}\right|_{g}^{2}\right) d \mu_{g}$$
Despite the apparent similarity with Equation (4), this finite curvature integral has no immediate topological interpretation in general. However, if the ideal boundary of $(M, g)$ is a finite collection of fibered cusps, with each fibration being a circle bundle over a surface, we do have a topological interpretation of Equation (6) by keeping into account the limit $\eta$-invariant of each cusp. More precisely, we have the following formula, due to Dai and Wei (see [DW07, Page 568]):
$$\tau_{L^{2}}(M)=\tau(M)+\sum_{E \in \operatorname{Ends}(M)} \frac{e(E)-3 \operatorname{sign}(e(E))}{3},$$
where $\tau(M)$ is again the signature of $M$, and where $e(E)$ is the Euler number of the circle bundle associated to $E \in \operatorname{Ends}(X)$. Recall that in order for the signature to be defined one just needs that $M$ is oriented and that $H_{2}(M ; \mathbb{Z})$ is finitely generated. (Note that $H_{2}(M ; \mathbb{Z})$ is automatically finitely generated for a complex-hyperbolic manifold of finite volume.) Under these assumptions, $H_{2}(M ; \mathbb{Z}) /$ Tor is a free Abelian group of finite rank, and the intersection product induces on it a (possibly degenerate) bilinear form: given two classes $A, B \in H_{2}(M ; \mathbb{Z}) /$ Tor, we can represent them by two transversely embedded compact surfaces, $F_{A}$ and $F_{B}$; the intersection $Q_{M}(A, B)$ is the count of their intersections with the sign determined by the orientation. Then we define $\tau(M)$ to be the signature of $Q_{M}$, i.e., the number of positive eigenvalues minus the number of negative eigenvalues of $Q_{M}$. (When $M$ is non-compact or has non-empty boundary, $Q_{M}$ could have non-degenerate kernel.)

By combining these formulas, we have the following generalization of the Hitchin-Thorpe inequality.

Theorem 3.2 ([DW07]). Let ( $X, g$ ) be a non-compact, complete Einstein 4-manifold whose ideal boundary is a finite collection of fibered cusps, with each fibration being a circle bundle over a surface. We then have
$$\chi(X) \geq \frac{3}{2}\left|\tau(X)+\sum_{E \in \operatorname{Ends}(X)} \frac{e(E)-3 \operatorname{sign}(e(E))}{3}\right|$$
where, as above, $e(E)$ is the Euler number of the circle bundle associated to $E$. Moreover, equality holds if and only if $(X, g)$ is a complete Calabi-Yau manifold.

\section*{4. Non-Einstein Dehn filling compactifications}

We start by describing Hirzebruch's example [Hir84] of a complex-hyperbolic surface of finite volume with a smooth toroidal compactification of Kodaira dimension zero, whose cusps all have Euler number 1. We will then tinker around with Hirzebruch's example to produce, for each $n>0$, a complex-hyperbolic surface that has the same property, except that the cusps have all Euler number $e$.
4.1. Hirzebruch's example(s). Let $\zeta=e^{\frac{\pi i}{3}}$ and $E_{\zeta}=\mathbb{C} / \Lambda_{\zeta}$ be the elliptic curve associated to the lattice $\Lambda_{\zeta}=\mathbb{Z}[1, \zeta]$. Consider the Abelian surface $A=E_{\zeta} \times E_{\zeta}$, with coordinates $(z, w)$. Since $E_{\zeta}$ is an elliptic curve with complex multiplication, the following four elliptic curves in $A$ are defined:
$$C_{0}=\{w=0\}, \quad C_{\infty}=\{z=0\}, \quad C_{1}=\{w=z\}, \quad C_{\zeta}=\{w=\zeta z\} .$$
The four elliptic curves in Equation (8) intersect transversely only in the point $(0,0) \in$ $A$. Moreover, by adjunction we know that each of them has self-intersection 0. Blow $\operatorname{up} A$ at $(0,0)$ to obtain $X$, and let $D$ be the proper transform of $C_{0} \cup C_{\infty} \cup C_{1} \cup C_{\zeta}$. we obtain a pair $(X, D)$ where $X$ is a blown-up Abelian surface and $D$ is a divisor consisting of four smooth disjoint elliptic curves, that we call $D_{1}, D_{2}, D_{3}, D_{4}$.

The surface $X$ is a smooth toroidal compactification of $X \backslash D$, which in turn can be shown to be complex-hyperbolic by Tian and Yau's uniformization theorem [TY87]. It suffices to compare $\sum_{i} D_{i}^{2}$ with $3 c_{2}(X)-c_{1}^{2}(X)$, if one has equality in the (logarithmic) Bogomolov-Miyaoka-Yau (log-BMY, for short) inequality
$$-\sum_{i} D_{i}^{2} \leq 3 c_{2}(X)-c_{1}^{2}(X),$$
then $X \backslash \cup_{i} D_{i}$ is complex-hyperbolic. In our case, the left-hand side is $-4 \cdot(-1)$, while the right-hand side is $3 \cdot 1-(-1)$, so we have equality, and $X \backslash \cup_{i} D_{i}$ is complex-hyperbolic, as claimed. By construction, $X \backslash D$ has four torus-like cusps, all with Euler number 1.

In [Hir84], Hirzebruch also consider $n^{2}$-fold covers of the surface $X$ we constructed above, in which he finds $4 n^{2}$ elliptic curves, each of self-intersection $-n^{2}$, and one easily check that their complement again satisfies equality in Equation (9), and thus the complement of all these curves is a complex-hyperbolic surface with all cusps of Euler number $n^{2}$.

Remark 4.1. Hirzebruch then uses these surfaces and these divisors to produce compact complex surfaces approaching the equality in the (non-logarithmic) BMY inequality. We will not need this part of his paper, but just the most basic example.
4.2. Playing with Hirzebruch's example. We want to tweak Hirzebruch's example from the previous subsection to obtain, for each $e>0$, a complex-hyperbolic surface whose cusps all have Euler number $e$. (As mentioned above, Hirzebruch himself had already found such examples, when $e$ is a square.) In fact, we will construct such examples with four cusps.

We will present a covering argument in slightly broader generality. Consider a pair $(A, C)$ where $A$ is a product of two tori $E \times E^{\prime}$ and $C$ is the union of four tori $C_{1}, C_{2}, C_{3}, C_{4}$, such that $C_{j} \cdot C_{k} \neq 0$ whenever $j \neq k$.

Lemma 4.2. For each prime $p$ there exists a $p$-fold étale cover $\pi: A^{\prime} \rightarrow A$ such that $C_{j}^{\prime}:=\pi^{-1}\left(C_{j}\right)$ is connected for $j=1, \ldots, 4$. For such a cover $\pi, C_{j}^{\prime} \cdot C_{k}^{\prime}=p \cdot\left(C_{j} \cdot C_{k}\right)$.
Proof. Let $\mathbb{F}_{p}$ the field with $p$ elements. Since each $C_{j}$ is a torus and every two of them intersect non-trivially, $P_{j}:=H_{1}\left(C_{j} ; \mathbb{F}_{p}\right) \subset H_{1}\left(A ; \mathbb{F}_{p}\right)$ is a 2 -plane in $\mathbb{F}_{p}$, and $P_{j} \cap P_{k}=\{0\}$ whenever $j \neq k$.

In order to prove the lemma, we need to find a surjective homomorphism $\phi \in$ $\operatorname{Hom}\left(H_{1}(A ; \mathbb{Z}), \mathbb{F}_{p}\right) \cong H^{1}\left(A ; \mathbb{F}_{p}\right) \cong \mathbb{F}_{p}^{4}$ such that $\operatorname{ker} \phi \cap P_{j}$ is 1-dimensional for each $j$. To see that this is sufficient, fix one of the divisors, $C_{j}$. Since $\operatorname{ker} \phi$ does not contain all of $P_{j}$, there is a curve $\gamma \subset C_{1}$ such that $\phi([\gamma]) \neq 0 \in \mathbb{F}_{p}$. Since $p$ is a prime, $\phi([\gamma])$ generates $\mathbb{F}_{p}$, so $\gamma$ lifts to a single simple closed curve in $\pi^{-1}(X)$, and in particular $\pi^{-1}\left(C_{j}\right)$ is connected.

Up to scalars, a homomorphism $\phi: H_{1}(A ; \mathbb{Z}) \rightarrow \mathbb{F}_{p}$ is determined by its kernel, $\operatorname{ker} \phi$. Conversely, if we find a hyperplane $K \subset H_{1}\left(A ; \mathbb{F}_{p}\right)$ such that $K \cap P_{j}$ is 1-dimensional for each $j$, then there exists $\phi_{K} \in H^{1}\left(A ; \mathbb{F}_{p}\right)$ such that $\operatorname{ker} \phi=K$, which is the homomorphism we required.

Instead of exhibiting such a hyperplane $K$, we will non-constructively show that there exists one by counting: we will prove that the number of hyperplanes in $H_{1}\left(A ; \mathbb{F}_{p}\right)$ such that $K \cap P_{j}$ is not 1-dimensional for at least an index $j \in\{1,2,3,4\}$ is strictly smaller than the number of hyperplanes in $H_{1}\left(A ; \mathbb{F}_{p}\right)$. (The total number of hyperplanes in $H_{1}\left(A ; \mathbb{F}_{p}\right)$ is the cardinality of the projective space $\mathbb{P}\left(H^{1}\left(A ; \mathbb{F}_{p}\right)\right) \cong \mathbb{P}_{\mathbb{F}_{p}}^{3}$, which is $p^{3}+p^{2}+p+1$.)

Let us now consider a hyperplane $K \subset H_{1}\left(A ; \mathbb{F}_{p}\right)$. Since $K$ is a hyperplane and $P_{j}$ is a 2 -plane, $1 \leq \operatorname{dim}\left(K \cap P_{j}\right) \leq 2$. Moreover, since $P_{j} \cap P_{k}=\{0\}$ whenever $j \neq k$, for a given hyperplane $K$ there is at most an index $j$ such that $\operatorname{dim}\left(K \cap P_{j}\right)=2$, or, equivalently, such that $P_{j} \subset K$.

The number of hyperplanes $K$ containing $P_{j}$ for a fixed index $j$ is $p+1$ : containing the 2-plane $P_{j}$ means imposing two linear conditions in the projective space $\mathbb{P}\left(H^{1}\left(A ; \mathbb{F}_{p}\right)\right)$, so the set of hyperplanes containing $P_{j}$ is a projective line in $\mathbb{P}\left(H^{1}\left(A ; \mathbb{F}_{p}\right)\right)$, which is a subset of cardinality $\| \mathbb{P}_{\mathbb{F}_{p}}^{1}=p+1$.

Therefore, there are $4(p+1)$ hyperplanes containing one among $P_{1}, \ldots, P_{j}$. Since
$$p^{3}+p^{2}+p+1-4(p+1)=p^{3}+p^{2}-3 p-3=\left(p^{2}-3\right)(p+1)>0$$
for every $p>1$, there is at least a hyperplane $K$ in $H_{1}\left(A ; \mathbb{F}_{p}\right)$ that does not contain any among $P_{1}, \ldots, P_{4}$, so in particular $\operatorname{dim}\left(K \cap P_{j}\right)=1$ for $j=1, \ldots, 4$, as required.

The second part of the statement is obvious by degree considerations. \(\square\)

Corollary 4.3. For every integer $e>1$ there exists an e-fold étale cover of $A$ such that the lifts of $C_{1}, \ldots, C_{4}$ are all connected.

Proof. We argue by induction on the number of (non-distinct) prime factors of $e$; the base case is when $e$ is prime, and this was proved in the previous lemma. If $e$ is not prime, choose a prime $p$ dividing it. By the previous lemma and by the inductive assumption, there is an $\frac{e}{p}$-fold cover $A^{\prime}$ of $A$ in which $C$ lifts to four tori $C^{\prime}$. Note that $C^{\prime}$ still satisfies the assumptions of Lemma 4.2. By Lemma 4.2, there is a $p$-fold cover $A^{\prime \prime}$ of $A^{\prime}$ in which $C^{\prime}$ lifts to four tori $C^{\prime \prime}$. Now $\left(A^{\prime \prime}, C^{\prime \prime}\right)$ is the required cover. \(\square\)

Remark 4.4. With a little more effort one can find a cyclic cover in Corollary 4.3; it suffices to take a $e^{4}$-fold cover $A^{\prime \prime} \rightarrow A$, as given by the corollary, and then observe that this corresponds to a subgroup $H \subset H_{1}(X ; \mathbb{Z})$ whose quotient $G=H_{1}(X ; \mathbb{Z}) / H$ has order $e^{4}$. Since $H_{1}(A ; \mathbb{Z}) \cong \mathbb{Z}^{4}, G$ is generated by (at most) four elements, one of
which has to have order divisible by $e$. In particular, $G$ has itself a cyclic quotient $G^{\prime}$ of order exactly $e$. Composing the maps $H_{1}(X ; \mathbb{Z}) \rightarrow G \rightarrow G^{\prime}$ gives the desired cover.

Let us now start with Hirzebruch's four tori $C_{0}, C_{\infty}, C_{1}, C_{\zeta} \subset A=E_{\zeta} \times E_{\zeta}$. Call $\left(A^{1}, C^{1}\right):=\left(A, C_{0} \cup C_{\infty} \cup C_{1} \cup C_{\zeta}\right)$. Fix a positive integer $e$. By the corollary above, there exists an $e$-fold étale cover $\pi: A^{e} \rightarrow A^{1}$ such that $C^{e}:=\pi^{-1}\left(C^{1}\right)$ is the union of four elliptic curves, each with self-intersection 0, and such that each two of them intersect pairwise $e$ times. Moreover, since $\pi$ is an étale cover, all $e$ intersection points are quadruple points where four distinct tori meet transversally. The 4 -manifold $A^{e}$ is an étale cover of the 4-torus $A^{1}$, so it is itself a 4-torus, therefore $c_{2}\left(A^{e}\right)=0$ and $\tau\left(A^{e}\right)=0$. The complex surface $A^{e}$ has first Chern class which is the pull-back of $c_{1}\left(A^{1}\right)$, so $c_{1}\left(A^{e}\right)=\pi^{*}\left(c_{1}\left(A^{1}\right)\right)=\pi^{*}(0)=0$.

Blow up at these $e$ intersection points, to obtain $\tilde{A}^{e}$. Since $\chi\left(A^{e}\right)=0, c_{1}^{2}\left(A^{e}\right)=0$, and $\tau\left(A^{e}\right)=0$, and since each blow-up increases $c_{2}$ by 1 , decreases $c_{1}^{2}$ by 1 (see, for instance, [BHPV04, Theorem I.9.1]) and $\tau$ by 1, we have that $c_{2}\left(\tilde{A}^{e}\right)=\chi\left(\tilde{A}^{e}\right)=e$, $c_{1}^{2}\left(\tilde{A}^{e}\right)=-e$, and $\tau\left(\tilde{A}^{e}\right)=-e$. The proper transform $D^{e}$ of $C^{e}$ consists of four disjoint tori $D_{1}^{e}, \ldots, D_{4}^{e}$, each of self-intersection $-e$, and in particular:
$$-\sum_{j} D_{j}^{e} \cdot D_{j}^{e}=4 e=3 e-(-e)=3 c_{2}\left(\tilde{A}^{e}\right)-c_{1}^{2}\left(\tilde{A}^{e}\right),$$
so $X_{e}:=\tilde{A}^{e} \backslash D^{e}$ is a complex-hyperbolic surface whose cusps all have Euler number $e$.
4.3. The proof of Theorem 1.1. The following proposition directly implies Theorem 1.1.

Proposition 4.5. Fix a positive integer $e$. Any 4-manifold $\bar{X}$ homeomorphic to the Dehn filling compactification $\tilde{A}^{e}$ of $X_{e}$ violates the Hitchin-Thorpe inequality, and in particular it carries no Einstein metric.
Proof. We compute the Euler characteristic and signature of $\tilde{A}^{e}:\left|\tau\left(\tilde{A}^{e}\right)\right|=\chi\left(\tilde{A}^{e}\right)$ by the computations above, so it violates the Hitchin-Thorpe inequality. Any 4-manifold $\bar{X}$ homeomorphic to $\tilde{A}^{e}$ has the same Euler characteristic and signature, so it also violates the Hitchin-Thorpe inequality. It follows that neither carries an Einstein metric. \(\square\)

\section*{5. Non-Einstein non-compact Dehn fillings}

Let us once again use Hirzebruch's example as a starting point. We start with a sequence of Abelian varieties $\left\{A_{e}\right\}, e \in \mathbb{N}$ defined as follows
$$A_{e}:=\mathbb{C} / \mathbb{Z}[1, \zeta] \times \mathbb{C} / \mathbb{Z}[e, \zeta] .$$
Notice that for $e=1$ we recover the Abelian surface considered by Hirzebruch. Inside the Abelian surface $A_{e}$ with coordinates $(z, w)$ consider the elliptic curves
$$w=0, \quad w=z, \quad w=\zeta z .$$
These curves meet transversally at $e$ distinct points
$$(0,0), \quad(0,1), \quad \ldots, \quad(0, e-1) .$$

Consider also $e$ vertical elliptic curves in $A_{e}$ of equations
$$z=0, \quad z=1, \quad \ldots, \quad z=e-1 .$$
(In the language of the previous section, this is an $e$-fold cyclic cover of Hirzebruch's example, but this time one of the curves has disconnected pre-image.) In other words, we have a configuration of $e+3$ elliptic curves meeting transversally at the points by Equations (10). We can now blow up these points to get a surface $Z_{e}$ birational to $A_{e}$ with $\chi\left(X_{e}\right)=e$. The proper transforms of the elliptic curves in $A_{e}$ described above, we obtain $e+3$ disjoint elliptic curves
$$D_{1}, \quad D_{2}, \quad D_{3}, \quad D_{4}, \quad \ldots, \quad D_{e+3},$$
where
$$D_{1}^{2}=D_{2}^{2}=D_{3}^{2}=-e, \quad D_{4}^{2}=D_{5}^{2}=\cdots=D_{e+3}^{2}=-1 .$$
Let us denote by $D^{e}$ the reduced divisor corresponding to the union of all of the $D_{j}$ 's. We then compute that the self-intersection of the log-canonical divisor of the pair $\left(Z_{e}, D^{e}\right)$ satisfy
$$\begin{aligned}
\left(K_{Z_{e}}+D^{e}\right)^{2} & =K_{Z_{e}}^{2}-\left(D^{e}\right)^{2}=-e+e+e+e+1+\ldots+1=3 e \\
& =3 \chi\left(Z_{e}\right)=3 \chi\left(Z_{e} \backslash D^{e}\right) .
\end{aligned}$$
Thus, the pair $\left(Z_{e}, D^{e}\right)$ saturates the log-BMY inequality and as a result $Y_{e}:=Z_{e} \backslash D^{e}$ is biholomorphic to a complex-hyperbolic surface with $e+3$ cusps, three of which have Euler number $e$.

We are now in position to proving Theorem 1.2. We will prove the following, slightly stronger statement.

Proposition 5.1. Let e be a positive integer. If e > 1, the 4-manifold obtained by Dehn filling the three cusps of $Y_{e}$ with Euler number e admits no complete Einstein metric with fibered cusp structure at infinity. If $e=1$, the 4-manifold obtained by Dehn filling the three cusps of $Y_{1}$ admits no complete Einstein metric with fibered cusp structure at infinity and with negative Einstein constant (e.g., asymptotic to the complex-hyperbolic metric).

Proof. Since $Y_{e}$ is the complement of $e+3$ pairwise disjoint divisors of negative self-intersections, by Novikov additivity (see for instance [Kir89, Section II.5]) we have
$$\tau\left(Y_{e}\right)=\tau\left(Z_{e}\right)+(e+3)=-e+e+3=3 .$$
If we now fill the three cusps of $Y_{e}$ with Euler number $e$, we get a manifold, call it $\bar{Y}$, with $e$ cusps. Again by Novikov additivity, $\tau(\bar{Y})=0$. If this is the case we can now obtain a contradiction if we assume we were able to Einstein Dehn fill these three cusps.

Let us call $\bar{Y}$ the manifold obtained from ( $X_{e}, D^{e}$ ) by filling the cusps $D_{1}, D_{2}, D_{3}$. Then $\bar{Y}$ has $e$ cusps with Euler number $1, \chi(\bar{Y})=e$, and $\tau(\bar{Y})=0$, so $\bar{Y}$ attains equality in the Dai-Wei inequality of Theorem 3.2. In particular, by Theorem 3.2, if it supports an Einstein metric with fibered structure at infinity, this metric is Ricci flat.

Now, since $e>1$, after filling the three cusps with Euler number $e$, we have that $\bar{Y}$ has at least two ends. Given any of the two non-compact ends, we can construct a line,
i.e., a geodesic $\gamma:(-\infty, \infty) \rightarrow \bar{Y}$ such that $d(\gamma(t), \gamma(s))=|t-s|$ for any $s, t \in \mathbb{R}$. By the Cheeger-Gromoll splitting theorem [CG72] such a line splits isometrically, and as a result our partially compactified manifold should have topological Euler characteristic equal to zero. On the other hand, $\chi(\bar{Y})=e$ and we then get a contradiction. Finally, if $e=1$, an Einstein metric asymptotic to a complex-hyperbolic one cannot be Ricci flat: the cosmological constant of the complex hyperbolic metric is negative and not zero as for Calabi-Yau surfaces. \(\square\)

\section*{6. Final remarks and questions}

We conclude with some remarks and questions concerning Theorems 1.1 and 1.2. In light of the theorem, one is naturally lead to ask the following question.
Question 6.1. Fix an integer $e>0$. Does there exist a complex-hyperbolic surface $Z_{e}$ with a torus-like cusp with Euler number $e$ such that Dehn filling of $Z_{e}$ does not support an Einstein metric with fibered cusp at infinity?

A positive answer would immediately imply that there is no single cusp-filling procedure that starts from one torus-like cusps of a complex-hyperbolic surface and produces an Einstein metric. In this sense, Theorem 1.1 proves the impossibility of complex-hyperbolic Dehn filling in a more constrained setting, namely when we require the Dehn filling to produce a closed orientable manifold. On the other hand, we could ask that the (hypothetical) metric produced by such an operation is itself asymptotic to a standard cusp-like metric at infinity. This is indeed true of the metrics produced by Thurston and by Anderson, where in fact the metric at the cusp is asymptotic to the original metric, thus allowing for the construction to be iterated [And06]. If we impose the further constraint that such an Einstein metric is asymptotic to the initial complex-hyperbolic metric, the proof of the second statement simplifies, and we can also produce answers to Question 6.1 whenever $e$ is divisible by 3. (These examples are 2-cusped, so after Dehn filling one cusp we cannot use the splitting theorem as we do for $X_{e}$.)

As mentioned at the end of Section 2, thanks to [DC12, Theorem A] and Yau's celebrated result [Yau78], we know that complex-hyperbolic Kähler-Einstein Dehn filling can be performed if we pass to a finite cover. The proof uses the ampleness of the canonical divisor of the toroidal compactification of a (sufficiently large) finite cover. It is interesting to ask whether such an argument holds for metric, rather than complex-algebraic reasons, as in Anderson's construction. More precisely, we ask the following question.
Question 6.2. Does there exists a constant $L$ such that, if the fiber of a torus-like cusp $c$ of a complex-hyperbolic surface $X$ has length larger than $L$, then the 4-manifold obtained by Dehn filling $X$ at $c$ supports an Einstein metric that is not Kähler-Einstein?

This would show that, given a complex-hyperbolic surface, one could find a finite cover in which the fiber of a cusp gets sufficiently long so as to assure that the corresponding Dehn filling is Einstein. In a way, the choice of the cover makes up for the lack of choice of slope of the filling. In this sense, this hypothetical construction would resemble Fine and Premoselli's branched covering construction [FP20].

\section*{References}
\begin{itemize}
\item[] [And06] Michael T. Anderson, Dehn filling and Einstein metrics in higher dimensions, J. Differential Geom. 73 (2006), no. 2, 219-261. MR 2225518
\item[] [And10] \_\_\_\_, A survey of Einstein metrics on 4-manifolds, Handbook of geometric analysis, No. 3, Adv. Lect. Math. (ALM), vol. 14, Int. Press, Somerville, MA, 2010, pp. 1-39. MR 2743446
\item[] [Bam12] Richard H. Bamler, Construction of Einstein metrics by generalized Dehn filling, J. Eur. Math. Soc. (JEMS) 14 (2012), no. 3, 887-909. MR 2911887
\item[] [BHPV04] Wolf P. Barth, Klaus Hulek, Chris A. M. Peters, and Antonius Van de Ven, Compact complex surfaces, vol. 4, Berlin: Springer, 2004 (English).
\item[] [Biq07] Olivier Biquard, Policopié on differential geometry and global analysis, Available on the Author's Webpage, 2007.
\item[] [BT18] Benjamin Bakker and Jacob Tsimerman, The Kodaira dimension of complex hyperbolic manifolds with cusps, Compos. Math. 154 (2018), no. 3, 549-564. MR 3731257
\item[] [CG85] Jeff Cheeger and Mikhael Gromov, Bounds on the von Neumann dimension of $L^{2}$ -cohomology and the Gauss-Bonnet theorem for open manifolds, J. Differential Geom. 21 (1985), no. 1, 1-34. MR 806699
\item[] [CG72] Jeff Cheeger and Detlef Gromoll, The splitting theorem for manifolds of nonnegative Ricci curvature, J. Differential Geometry 6 (1971/72), 119-128. MR 303460
\item[] [dC92] Manfredo Perdigão do Carmo, Riemannian geometry, Mathematics: Theory \& Applications, Birkhäuser Boston, Inc., Boston, MA, 1992, Translated from the second Portuguese edition by Francis Flaherty. MR 1138207
\item[] [DC12] Luca Fabrizio Di Cerbo, Finite-volume complex-hyperbolic surfaces, their toroidal compactifications, and geometric applications, Pacific J. Math. 255 (2012), no. 2, 305-315. MR 2928554
\item[] [DCDC15] Gabriele Di Cerbo and Luca F. Di Cerbo, Effective results for complex hyperbolic manifolds, J. Lond. Math. Soc. (2) 91 (2015), no. 1, 89-104. MR 3338610
\item[] [DCDC17] \_\_\_\_, On the canonical divisor of smooth toroidal compactifications, Math. Res. Lett. 24 (2017), no. 4, 1005-1022. MR 3723801
\item[] [DW07] Xianzhe Dai and Guofang Wei, Hitchin-Thorpe inequality for noncompact Einstein 4-manifolds, Adv. Math. 214 (2007), no. 2, 551-570. MR 2349712
\item[] [FP20] Joel Fine and Bruno Premoselli, Examples of compact Einstein four-manifolds with negative curvature, J. Amer. Math. Soc. 33 (2020), no. 4, 991-1038. MR 4155218
\item[] [Har71] G. Harder, A Gauss-Bonnet formula for discrete arithmetically defined groups, Ann. Sci. École Norm. Sup. (4) 4 (1971), 409-455. MR 309145
\item[] [Hir84] F. Hirzebruch, Chern numbers of algebraic surfaces: an example, Math. Ann. 266 (1984), no. 3, 351-356. MR 730175
\item[] [Hit74] Nigel Hitchin, Compact four-dimensional Einstein manifolds, J. Differential Geometry 9 (1974), 435-441. MR 350657
\item[] [Kir89] Robion C. Kirby, The topology of 4-manifolds, Lecture Notes in Mathematics, vol. 1374, Springer-Verlag, Berlin, 1989 (English).
\item[] [KL08] Bruce Kleiner and John Lott, Notes on Perelman's papers, Geom. Topol. 12 (2008), no. 5, 2587-2855. MR 2460872
\item[] [LeB99] Claude LeBrun, Four-dimensional Einstein manifolds, and beyond, Surveys in differential geometry: essays on Einstein manifolds, Surv. Differ. Geom., vol. 6, Int. Press, Boston, MA, 1999, pp. 247-285. MR 1798613
\item[] [LP72] François Laudenbach and Valentin Poenaru, A note on 4-dimensional handlebodies, Bull. Soc. Math. France 100 (1972), 337-344.
\item[] [NZ85] Walter D. Neumann and Don Zagier, Volumes of hyperbolic three-manifolds, Topology 24 (1985), no. 3, 307-332. MR 815482
\end{itemize}
[Per02] Grisha Perelman, The entropy formula for the Ricci flow and its geometric applications, preprint arXiv:math/0211159, 2002.
[Per03] \_\_\_\_, Ricci flow with surgery on three-manifolds, preprint arXiv:math/0303109, 2003.
[PP00] Carlo Petronio and Joan Porti, Negatively oriented ideal triangulations and a proof of Thurston's hyperbolic Dehn filling theorem, Expo. Math. 18 (2000), no. 1, 1-35. MR 1751141
[Pre42] Alexandre Preissman, Quelques propriétés globales des espaces de Riemann, Comment. Math. Helv. 15 (1942), 175-216.
[Tho69] John A. Thorpe, Some remarks on the Gauss-Bonnet integral, J. Math. Mech. 18 (1969), 779-786. MR 0256307
[Thu78] William P. Thurston, The geometry and topology of three-manifolds, available at http://msri.org/publications/books/gt3m/, 1978.
[TY87] G. Tian and S.-T. Yau, Existence of Kähler-Einstein metrics on complete Kähler manifolds and their applications to algebraic geometry, Mathematical aspects of string theory (San Diego, Calif., 1986), Adv. Ser. Math. Phys., vol. 1, World Sci. Publishing, Singapore, 1987, pp. 574-628. MR 915840
[Wal67] Friedhelm Waldhausen, Eine Klasse von 3-dimensionalen Mannigfaltigkeiten I, Invent. Math. 3 (1967), 308-333.
[Wal68] \_\_\_\_, Eine Klasse von 3-dimensionalen Mannigfaltigkeiten II, Invent. Math. 4 (1968), 87-117.
[Yau78] Shing-Tung Yau, On the Ricci curvature of a compact Kähler manifold and the complex Monge-Ampère equation. I, Comm. Pure Appl. Math. 31 (1978), no. 3, 339-411. MR 480350
Email address: ldicerbo@ufl.edu
Department of Mathematics, University of Florida, Gainesville, United States
Email address: marco.golla@univ-nantes.fr
CNRS, Laboratoire Jean Leray, Nantes University, Nantes, France