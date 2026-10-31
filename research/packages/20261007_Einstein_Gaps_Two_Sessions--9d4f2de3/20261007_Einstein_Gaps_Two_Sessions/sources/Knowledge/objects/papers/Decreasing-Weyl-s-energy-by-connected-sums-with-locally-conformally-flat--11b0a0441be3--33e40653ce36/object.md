# Decreasing Weyl's energy by connected sums with locally conformally flat manifolds

- Category: papers
- Identity: doi:10.48550/arxiv.2604.17547
- Content status: fulltext_ok

---

---
source_file: 2604_17547.pdf
converter: mathpix
format: mmd
---

\title{
Decreasing Weyl's energy by connected sums with locally conformally flat manifolds
}

\author{
Andrea Malchiodi and Francesco Malizia*
}

\begin{abstract}
We study the Weyl functional on connected sums of two four-dimensional manifolds $\left(M, g_{M}\right)$ and $\left(Z, g_{Z}\right)$, assuming $g_{M}$ is Bach-flat and $g_{Z}$ locally conformally flat. We show that if $g_{M}$ is neither self-dual nor anti self-dual and if $g_{Z}$ is of positive Yamabe class, there exists a metric $g_{Y}$ on $Y:=M \# Z$ with Weyl energy lower than that of $g_{M}$ (with the trivial exception of $\left.\left(Z, g_{Z}\right)=\left(\mathbb{S}^{4}, g_{\mathbb{S}^{4}}\right)\right)$. This result has a relation to a conjecture by Singer and has a perspective application to the minimization of Weyl energy. The proof relies on a simultaneous interplay of $W_{M}^{+}, W_{M}^{-}$and the topology of $Z$, and also covers some orbifold cases.
\end{abstract}

Key Words: Weyl Functional, Self-Duality, Locally Conformally Flat Manifolds.
MSC 2020: 53C21, 53C25, 58E11, 49J99.

\section*{Contents}
1 Introduction ..... 1
2 Preliminaries ..... 8
3 Construction of the modified metric on the LCF manifold ..... 11
4 Weyl energy of the modified metric on $Z=\left(\mathbb{R} \times \mathbb{S}^{3}\right) / G$ ..... 22
5 Weyl energy of the perturbed non LCF metric ..... 31
6 Conclusion of the proofs ..... 34
References ..... 44

\section*{1 Introduction}

In Riemannian geometry it is often desirable to look for canonical metrics: in four dimension one natural condition for a metric $g$ is to be Einstein, namely when the Ricci tensor satisfies
$$\operatorname{Ric}(g)=\lambda g .$$
Analytically, the Einstein condition (up to a suitable gauge transformation such as a local choice of harmonic coordinates) gives rise to an elliptic system in the metric (see e.g. [Bes08, Chapter 5]),

\footnotetext{
*The authors are grateful to Matt Gursky for helpful discussions and suggestions. They are supported by the PRIN Project 2022AKNSE4 Variational and Analytical aspects of Geometric PDE and are members of Gruppo Nazionale per l'Analisi Matematica, la Probabilità e le loro Applicazioni (GNAMPA), as part of the Istituto Nazionale di Alta Matematica. Andrea Malchiodi is also supported by the project Geometric problems with loss of compactness from Scuola Normale Superiore.
}
allowing to obtain compactness properties up to a finite number of points ([And89], [BKN89]). This property is peculiar of the four-dimensional case, since in dimension 2 and 3 the Einstein condition is rigid and yielding constant sectional curvature, while in dimension greater or equal to five there might be an abundance of such metrics, see [Gro00].

However, there are known obstructions to the existence of Einstein metrics: for example, some topological ones are given by the Hitchin-Thorpe inequality ([Tho69; Hit74]), but some of them might depend as well on other properties, such as the differentiable structure, see e.g. [LeB96], [Kot98]. We refer the reader to the surveys [And10], [LeB03] for more detailed comments.

Other natural metrics to consider might arise from extremizing curvature functionals (see [Bes08, Chapter 4]), such as the integrals of the squares of the scalar curvature or of the norm of the Riemann tensor. An example without known obstructions, up to now, is Weyl's energy. In four dimensions, the curvature tensor admits the following $L^{2}$-orthogonal decomposition
$$\text { Riem }=W \oplus \frac{1}{2} E \oplus g \oplus \frac{R_{g}}{24} g \oplus g,$$
where $\Phi$ stands for the Kulkarni-Nomizu product (see e.g. [Via16]), $E:=\operatorname{Ric}-\frac{R_{g}}{4} g$ for the traceless Ricci tensor and $W$ denotes the Weyl tensor, the conformally covariant component of the curvature.

The Weyl functional is defined in this way:
$$\mathcal{W}^{M}(g):=\int_{M}\left|W^{g}\right|^{2} d V_{g}$$
The covariance of $W_{g}$ makes $\mathcal{W}^{M}(\cdot)$ conformally invariant, and therefore it only depends on the conformal class $[g]$ of $g$. Critical points of (1.2) are Bach-flat metrics, characterized by the equation
$$B_{i j}:=-4\left(\nabla^{k} \nabla^{l} W_{k i j l}+\frac{1}{2} R^{k l} W_{k i j l}\right)=0,$$
where $B=B_{i j}$ is the Bach tensor, see [Bac21], [Kob85].
Bach-flat metrics include conformally Einstein metrics, self-dual or anti self-dual metrics but not only, even though only few examples different from these ones are known, see [AGS13]. To our knowledge, there are no obstructions to the existence of Bach-flat metrics on closed 4-manifolds, so these might be a natural class of critical metrics to look for.

Still, the system (1.3) is not simple to treat for different reasons. First, as for the Einstein equation, there is a degeneracy due to the action of diffeomorphisms, and for the present situation also due to the conformal covariance of the problem. For this reason, the parabolic version of (1.3) has been treated in [BH11], [BH15] and [CLQ23] by applying suitable gauge transformations in the spirit of DeTurck's trick for the Ricci flow. As for Einstein metrics, it is also expected that sequences of Bach-flat metrics (or approximate Bach-flat) might develop collapsing (see [CG86; CG90]) or orbifold singularities, as explained in [And06]. Indeed, under suitable curvature and volume bounds one has orbifold precompactness (see [And05], [TV05a], [TV05b], [TV08], [Str10]).

Our goal in this paper is to exclude some type of topological degenerations for Bach-flat metrics via energy comparison, showing that on suitable connected sums of Bach-flat manifolds one can find a metric with lower energy than the sum of the two initial ones. To put our results into perspective, we begin by recalling the following theorem.

Theorem A. ([MM25]) Let $\left(M, g_{M}\right),\left(Z, g_{Z}\right)$ be two 4-dimensional closed, connected, oriented manifolds, and let $Y:=Z \# M$ be their connected sum. Assume that $g_{M}, g_{Z}$ are not locally conformally flat and that they are not both self-dual or both anti-self-dual. Then there exists a metric $g_{Y}$ on $Y$ such that
$$\mathcal{W}^{Y}\left(g_{Y}\right)<\mathcal{W}^{M}\left(g_{M}\right)+\mathcal{W}^{Z}\left(g_{Z}\right) .$$

The above result has a counterpart for the Willmore functional defined on immersions $f: \Sigma^{\rho} \rightarrow \mathbb{R}^{n}$ from surfaces of genus $\rho$, and given by
$$\mathbb{W}(f):=\frac{1}{4} \int_{\Sigma^{\rho}}|H|^{2} d \mu$$
where $H$ is the mean curvature of the immersion. Images of immersions that are stationary for $\mathbb{W}$ are known as Willmore surfaces. In [Sim86; Sim93] direct methods were used to study minimizing sequences, but one could not exclude a-priori convergence in the Hausdorff distance to surfaces of lower genus $\rho_{0}<\rho$. This possibility was ruled out in [BK03] by showing that if $\rho_{i} \geq 1, i=1,2$ and if $f_{i}: \Sigma^{\rho_{i}} \rightarrow \mathbb{R}^{n}$ are Willmore immersions, then there exists an immersed surface $f: \Sigma^{\rho} \rightarrow \mathbb{R}^{n}$ with the topology of the connected sum (i.e. $\Sigma^{\rho} \cong \Sigma^{\rho_{1}} \# \Sigma^{\rho_{2}}$ ) such that
$$\mathbb{W}(f)<\mathbb{W}\left(f_{1}\right)+\mathbb{W}\left(f_{2}\right)-4 \pi .$$
As a consequence, for a minimizing sequence of immersions in genus $\rho$ it is not convenient to split into immersions of lower genus. The above inequality was proved by joining the two surfaces $f_{i}\left(\Sigma^{\rho_{i}}\right)$ at two non-umbilic points, properly oriented according to their principal directions, Kelvin-inverting $\Sigma^{\rho_{1}}$, and biharmonically interpolating the two local graphs.

The strategy for proving Theorem A is in some way similar in spirit. In a first instance, given $p \in M$, one performs a conformal blow-up of $g_{M}$ on $M \backslash\{p\}$, a replacement for Kelvin's inversion on immersed surfaces. More precisely, one sets $\left(N, g_{N}\right)=\left(M \backslash\{p\}, f^{2} g_{M}\right)$, with $f(\cdot) \simeq d_{g}(\cdot, p)^{-2}$. If $x$ is a system of geodesic coordinates centered at $p$, in inverted coordinates $y=x /|x|^{2}$ one has $g_{N} \simeq d y^{2}$ for $|y|$ large, and therefore $g_{N}$ is asymptotically flat. Notice that this process involves a change of orientation, which is later accounted for by gluing a reversed copy of $M$.

For $a>0$ small, one then shrinks $\left(N, g_{N}\right)$ into a manifold $\left(N, g_{a}\right)$ by setting $g_{a}:=a^{2} g_{N}$, and at the same time enlarges $\left(Z, g_{Z}\right)$ into a manifold $\left(Z, g_{b}\right)$ via the scaling $g_{b}=b^{-2} g_{Z}:=\lambda^{-2} a^{-2} g_{Z}$, for some $\lambda>0$. Using then a nearly biharmonic interpolation of $g_{a}$ and $g_{b}$ in a proper annulus centered at $q \in Z$ and of relative width $\gamma \ll 1$, one can define a metric $g_{Y}$ on the connected sum $Y=M \# Z$ such that
$$\mathcal{W}^{Y}\left(g_{Y}\right)-\mathcal{W}^{M}\left(g_{M}\right)-\mathcal{W}^{Z}\left(g_{Z}\right)=a^{4}\left(C-\frac{4}{9} \pi^{2} \lambda^{2} W^{\bar{M}}(p) \circledast W^{Z}(q)+O\left(\lambda^{2} \gamma^{2}\right)\right)+\text { h.o.t.. }$$
Here $\bar{M}$ stands for $M$ with the opposite orientation, and $W^{\bar{M}}(p) \circledast W^{Z}(q)$ denotes the quantity
$$W^{\bar{M}}(p) \circledast W^{Z}(q):=\sum_{i, j, k, l} W_{k i j l}^{Z}(q)\left(W_{k i j l}^{\bar{M}}(p)+W_{l i j k}^{\bar{M}}(p)\right) .$$
In this procedure, we are identifying $T_{p} \bar{M}$ with $T_{q} Z$, and we are expressing tensor components with respect to a common orthonormal basis. Notice that the right-hand side in (1.6) depends upon the identification of the two tangent spaces.

It turns out that, under the assumptions of Theorem A, it is always possible to identify $T_{p} \bar{M}$ and $T_{q} Z$ so that $W^{\bar{M}}(p) \circledast W^{Z}(q)>0$, which by (1.5) gives the desired result. In fact, if $W_{ \pm}$denote the self-dual and anti self-dual components of the Weyl tensors, one sees in (1.6) an interaction between $W_{ \pm}^{M}(p)$ and $W_{\mp}^{Z}(q)$. The term $W^{\bar{M}} \circledast W^{Z}$ appeared in [GV16], where the authors constructed metrics on connected sums that are critical for proper linear combinations of $\mathcal{W}$ and the integral of the scalar curvature squared. In [Tau92] a related interaction was used to construct anti self-dual metrics on $M \# m \overline{\mathbb{C P}}^{2}$, where $M$ is arbitrary and $m$ is taken sufficiently large.

Theorem A does not apply when $g_{M}$ and $g_{Z}$ are both SD or ASD. Indeed, for such cases there is a conjecture by I.Singer, whose validity implies that if the two manifolds are also of positive Yamabe class,
it should be possible to find a family of self-dual (anti self-dual) metrics on $M \# Z$ with arbitrarily small necks. As such metrics would be all Bach-flat (indeed, global minima of $\mathcal{W}$ by the signature formula), their Weyl energies would all coincide along deformations, and thus one would have equality of both sides in (1.4) through such a family. We refer to [GG24] for recent progress about Singer's conjecture, to [Flo91] for a construction on connected sums of $\mathbb{C P}^{2}$ 's, and to [DF89] for the more general case in which the second cohomology groups associated to the SD deformation complexes vanish.

The purpose of the present paper is to understand the remaining case in which the assumptions of Theorem A are not satisfied, namely when one manifold, say $\left(M, g_{M}\right)$, is neither self-dual nor anti self-dual and the other manifold is locally conformally flat. Our main result is the following theorem.

Theorem 1.1. Let $\left(M, g_{M}\right),\left(Z, g_{Z}\right)$ be two four-dimensional closed, connected, oriented manifolds, and let $Y:=Z \# M$ be their connected sum. Assume that $g_{M}$ is Bach-flat and neither self-dual nor anti self-dual and that $g_{Z}$ is locally conformally flat and of positive Yamabe class. Then, in case $\left(Z, g_{Z}\right)$ is not globally conformal to $\left(\mathbb{S}^{4}, g_{\mathbb{S}^{4}}\right)$, there exists a metric $g_{Y}$ on $Y$ such that
$$\mathcal{W}^{Y}\left(g_{Y}\right)<\mathcal{W}^{M}\left(g_{M}\right) .$$

Before discussing the main ideas of the proof, we comment on the assumptions of the theorem.
Remark 1.2. (a) If $\left(Z, g_{Z}\right)=\left(\mathbb{S}^{4}, g_{\mathbb{S}^{4}}\right)$, the connected sum $Y$ would have trivially the topology of $M$, and an optimal choice of $g_{Y}$ would just be $g_{M}$. We recall that, by a result of Kuiper [Kui49], the sphere is the only locally conformally flat manifold that is simply connected, up to conformal diffeomorphisms. In our proof, as discussed below, we exploit the developing map in order to distinguish the round sphere from any other locally conformally flat manifold of positive Yamabe class, just like the ADM mass does. Also, as noted before, if Singer's conjecture is true and $M$ is of positive Yamabe class, for (1.7) to hold one needs both $W_{+}^{M}$ and $W_{-}^{M}$ to be non zero somewhere. Therefore, we need to use crucially an interplay among $W_{M}^{+}, W_{M}^{-}$and the topology of $Z$ at the same time to diffuse efficiently Weyl energy from $M$ into $Z$.
\begin{itemize}
\item[(b)] We are assuming both $M$ and $Z$ to be Bach-flat. If one of them is not, it is very easy to construct a metric on $Y$ as in (1.7), modifying first either $g_{M}$ or $g_{Z}$.
\item[(c)] For Willmore surfaces in $\mathbb{R}^{n}$ the counterpart of local conformal flatness would be umbilicity, but in this case one has rigidity and the corresponding surface would be a round sphere.
\end{itemize}

In view of the applications to the minimization of Weyl's energy, discussed at the end of this introduction, we expect Theorem 1.1 to be most relevant in positive Yamabe class, where one controls the Sobolev inequality, in turn useful to avoid collapsing. It would be interesting to investigate the cases in which $Z$ has zero or negative scalar curvature.

As we remarked before, under the assumptions of Theorem 1.1 the main interaction term in (1.5) vanishes identically, and therefore we need a more precise choice of the metric and a finer expansion of Weyl's energy. To give a more precise idea of our procedure, we focus first on the locally conformally flat manifold $Z$, where near $q$ we can assume that the metric is flat, by the conformal invariance of the problem. Identifying $T_{p} \bar{M}$ and $T_{q} Z$ and denoting by $x$ normal coordinates centered at $q$, we can also use $x$ as inverted normal coordinates on $T_{p} M$ (after a proper dilation).

Denoting by $\tilde{g}_{M}$ the conformal blow-up of $g_{M}$, we have the expansion
$$\tilde{g}_{M} \simeq\left(\delta_{i j}+\tau W_{k i j l}^{\bar{M}} \frac{x^{k} x^{l}}{|x|^{4}}\right) d x^{i} d x^{j} \quad \text { for } \quad x \simeq 0, x \neq 0$$
where $\tau>0$ is a small coefficient.

At this point, to match the two metrics across the gluing region, one needs to find a correction $\tau F$ to $g_{Z}$ with $F \simeq W_{k i j l}^{\bar{M}} \frac{x^{k} x^{l}}{|x|^{4}} d x^{i} d x^{j}$ near $q$. Moreover, it is clearly convenient to keep the metric on $Z$ as Bach-flat as possible, and therefore it is also natural to look for a correction that solves
$$\dot{B}_{g_{Z}}(F)=0 \quad \text { on } Z \backslash\{q\} .$$
This is reminiscent of other gluing constructions, and in particular to the one in [Sch84], where for the (scalar) Yamabe equation a highly concentrated bubble profile was attached to a suitable multiple of the Green's function of the conformal Laplacian, with pole at the location of the bubble. In particular, by the symmetries of $W$, in case $\left(Z, g_{Z}\right)=\left(\mathbb{S}^{4}, g_{\mathbb{S}^{4}}\right)$ this would be a global and transverse-traceless (TT) solution to (1.8) expressed in stereographic coordinates at $-q$.

Since on $\mathbb{R}^{4}$ the linearized Bach operator coincides with the bi-Laplacian on TT tensors, to have a solution $F$ as desired one can try to solve a distributional equation like
$$\dot{B}_{g_{Z}}(F)=W_{k i j l}^{\bar{M}} \nabla^{k} \nabla^{l} \delta_{q} d x^{i} d x^{j} \quad \text { on } Z,$$
where $\delta_{q}$ stands for the Dirac delta at $q$. Such an equation can be solved by abstract means (up to Lagrange multipliers), yielding a solution of the type
$$F=\left(W_{k i j l}^{\bar{M}} \frac{x^{k} x^{l}}{|x|^{4}}+A_{i j}(x)\right) d x^{i} d x^{j} \quad \text { near } q$$
and the prospect is that the extra term $A_{i j}$ might have a role in the expansion of Weyl's energy on $Y$.
While there is in general no hope to control the remainder term $A_{i j}$ with an abstract approach, the advantage of working with a locally conformally flat metric on $Z$ is that one can pass to the universal cover $\tilde{Z}$ of $Z$ and use the developing map $\Phi: \tilde{Z} \rightarrow \mathbb{S}^{4}$, which turns out to be injective in positive Yamabe class, see [SY88]. Here, the latter property allowed to prove positivity of the ADM mass of (non spherical) locally conformally flat manifolds by roughly writing the lift to $\tilde{Z}$ of the Green's function of the conformal Laplacian on $Z$ as a multi-pole singular solution.

The hope in the present situation is to use a similar strategy, in order to write $A_{i j}$ via a formal series expansion. In fact, one could start from the above solution on $\mathbb{S}^{4}$, use the conformal covariance of $\dot{B}$ and in a first attempt sum over all pull-backs via deck transformations of $\tilde{Z}$, as in (3.8). If this would converge, one might project such tensor onto $Z$ and find the metric perturbation $F$ as desired.

A model case one can consider is the product $\mathbb{S}_{t}^{1} \times \mathbb{S}^{3}$, with $\mathbb{S}_{t}^{1}$ standing for the circle of length $\log t, t>1$. The universal cover is $\mathbb{R}^{4} \backslash\{0\}$ (or $\mathbb{S}^{4}$ with two antipodal points removed) and the deck transformation group is isomorphic to $\mathbb{Z}$. Proceeding as described above, from (3.8) we obtain the expression for $\tilde{A}$ given by (3.11), see Section 3.1.1. Unfortunately, the series constructed in this way does not converge: since however the kernel of the linearized Bach operator contains all Lie derivatives, as a second attempt we modify each summand in the series by a non-TT element, allowing to solve the convergence problem, see the discussion before Lemma 3.3. We then obtain a solution of (1.8) that behaves as in (1.9).

Since we modified the metric on $Z$, which was locally flat, by a term like (1.9), in order to properly glue the new metric on $M$ we need to adjust $g_{M}$ in order to match the extra term $A$. If $y=\frac{x}{|x|^{2}}$ (with $x$ coordinates as before) are normal coordinates at $p \in M$, we need to add a suitable multiple of a correction $H$ that behaves like
$$H \simeq \frac{1}{2} \nabla_{k l}^{2} A_{i j}(0) x^{k} x^{l} d x^{i} d x^{j} \quad \text { near } p .$$
Using integration by parts and some delicate expansions, we see that the correction to Weyl's energy (compared to $\mathcal{W}\left(g_{M}\right)$ ) for the connected sum $Y$ with metric profiles as described above is proportional
to $-W_{\bar{M}}^{k i j l} \nabla_{k l}^{2} A_{i j}$, so qualitatively $\nabla^{2} A$ plays the role of a tensorial mass that couples to the Weyl's tensor of $M$. After a direct calculation, for $Z=\mathbb{S}_{t}^{1} \times \mathbb{S}^{3}$ the term $W_{\bar{M}}^{k i j l} \nabla_{k l}^{2} A_{i j}$ becomes of the type
$$F(t) W^{M}(p) \circledast W^{\bar{M}}(p)$$
where $F(t)$ depends on the length of $\mathbb{S}_{t}^{1}$, see Section 6.2 for details. Qualitatively, $F(t)$, which is positive, behaves with respect to $t$ like the ADM mass of $Z=\mathbb{S}_{t}^{1} \times \mathbb{S}^{3}$, see Remark 3.5 (and in particular blows-up as $t \rightarrow 1^{+}$). Therefore, we get the desired comparison for the Weyl energies of $g_{Y}$ and $g_{M}$ whenever the interaction (1.10) is positive, which can be always achieved provided $M$ is not self-dual or anti self-dual.

Before discussing the case of a general $Z$, we comment on an aspect of the above gluing procedure that we find relevant. In order to perform a proper matching, we need to modify $g_{Z}$ so that the tensor $A_{i j}$ vanishes at $q$ together with its gradient and so that the term $W^{k i j l} \nabla_{k l}^{2} A_{i j}$ is not affected by this change. To prove this fact we again employ a translational gauge (i.e., we add a Lie derivative), which also allows us to project the hessian of $A$ on symmetrized curvature tensors and streamline many computations. This is analogous to the construction of normal coordinates by iterated polynomial change of variables, see Section 4 in [WY25].

We next turn to the case of a general locally conformally flat manifold $\left(Z, g_{Z}\right)$ of positive Yamabe class. By a result in [CTZ12] (which completes the work in [Ham97], [Ize95]), all such manifolds are diffeomorphic to connected sums of compact quotients of $\mathbb{S}^{1} \times \mathbb{S}^{3}$. We exploit this information by choosing a special family of metrics on $Z$ which will lead to the same conclusions as above. First, fixing one of the summands as just described, we take the corresponding parameter $t$ to be sufficiently close to 1 , in order to obtain a strong interaction term in (1.10) (i.e., $F(t)$ will be large). One can prove, see Proposition 3.11, that even passing to quotients, the interaction term $W^{k i j l} \nabla_{k l}^{2} A_{i j}$ stays positive. Taking connected sums with other quotients of this type, we choose sufficiently small necks, in order to obtain an interaction term very close to the original one, for capacity reasons, see Proposition 6.7.

Remark 1.3. Instead of working with a glued manifold $Y \cong Z \# M$, it will be easier in the next sections to perform a simpler gluing and consider $X \cong Z \# \bar{M}$. This does not create any issue, as in the end it will be sufficient to perform the same procedure with $\bar{M}$ replacing $M$, see Remark 6.1.

Theorem 1.1 can be extended to some orbifold settings:
Theorem 1.4. Let $\left(M, g_{M}\right),\left(Z, g_{Z}\right)$ be two four-dimensional closed, connected, oriented orbifolds. Assume that $g_{M}$ is Bach-flat and that $g_{Z}$ is locally conformally flat and with positive scalar curvature. Let $p \in M$ and $q \in Z$ be orbifold points, both with group $\Gamma \cong \mathbb{Z}_{2}$, and denote by $Y:=Z \# M$ the orbifold connected sum at $p, q$. Assume that the Weyl tensor of $g_{M}$ at $p$ is neither self-dual nor anti-self-dual and that the number of orbifold points on $Z$ with group isomorphic to $\mathbb{Z}_{2}$ is at least 4 . Then there exists a metric $g_{Y}$ on $Y$ such that
$$\mathcal{W}^{Y}\left(g_{Y}\right)<\mathcal{W}^{M}\left(g_{M}\right) .$$

We refer to Section 6.4 for the proof and the definitions of orbifolds and orbifold connected sums. The proof of Theorem 1.4 follows along the same lines as that of Theorem 1.1; indeed, by the results in [CTZ12], [Wan25] we have a classification of locally conformally flat orbifolds with positive scalar curvature, Theorem 6.9, which is similar to that of their smooth counterpart. We point out that orbifold points corresponding to any given group always arise in even numbers, see Section 6.4.

We expect the result of Theorem 1.4 to hold in the more general case in which $Z$ is not conformally equivalent to a football orbifold, see Remark 6.12. This is important for what we believe to be one of the principal perspective applications of these gluing results, that is, to the blow-up analysis of (suitable) minimizing sequences for the Weyl energy, which will be briefly described next.

\section*{Connected sums and minimization of the Weyl energy}

As already outlined in [MM25], one of the most interesting applications of Theorems A, 1.1 and 1.4 concerns the minimization of Weyl's functional in the noncollapsing case.

Assume we have a minimizing sequence $\left(g_{i}\right)_{i}$ for the Weyl energy on a given closed four-manifold $Y$, and suppose that the volume of geodesic balls is uniformly bounded from below along the sequence ${ }^{1}$ Then it is reasonable to expect the validity of a bubble convergence/orbifold compactness theorem for suitable perturbations of Weyl's functional along $\left(g_{i}\right)_{i}$. Indeed, this holds true in the space of Bach flat metrics with (positive) constant scalar curvature by the works of Tian-Viaclovsky and Streets ([TV05a], [TV05b], [TV08], [Str10]), and a possible approach for minimizing sequences of a Sacks-Uhlenbeck type approximation of Weyl's functional was for instance proposed in [And06].

If we further assume to have an energy identity (that is, the infimum of Weyl's energy on $Y$ coincides with the Weyl energy on the limit orbifold plus the Weyl energy of each bubble), then we could employ Theorems A, 1.1, 1.4 to glue back together these spaces and obtain a manifold, diffeomorphic to $Y$, with a smooth metric whose Weyl energy is strictly smaller than the supposed infimum. This would give a contradiction and thus show us that there could not have been bubbling in the first place. As a consequence, $g_{i}$ subconverges to a smooth Bach flat metric on $Y$.

In other words, we expect these theorems to provide obstructions to the loss of topology/formation of orbifold points along minimizing sequences, as it happens for the Willmore functional (see [BK03]).

In this setting, after a suitable scaling the bubbles are expected to converge to Bach-flat and scalar-flat asymptotically locally Euclidean (ALE) orbifolds, and it has been shown in [Str10], [AV12] that said manifolds are ALE of order at least 2.

In the particular case of asymptotically Euclidean (AE) manifolds, then 2 is also the maximal order of decay by the rigidity statement of positive mass theorem. Moreover, it has been shown that these manifolds can be conformally compactified into smooth manifolds (see again [Str10]). Hence we are exactly in the setting of Theorems A, 1.1, which, coupled with a positive answer to Singer's conjecture, would provide a complete picture of bubbling via neckpinch in positive Yamabe class. In other words, the only expected bubbling behavior is that of a self-dual manifold which is developing self-dual bubbles, which is something obtainable by reversing the gluing constructions in [DF89], [Flo91].

However, to have a complete picture we would also need counterparts of our previous theorems for orbifolds, and in these situations we also expect the necessity to consider higher order obstructions (as the Weyl tensor might vanish at a given finite order at the orbifold point).

By analogy with smooth manifolds, we expect the bubbles to be self-dual (anti self-dual) orbifolds. This is indeed the situation for the Gibbons-Pope or Page construction ([GP79], [Pag78], [Top87], [LS94]). We also point out that a gluing result of self-dual orbifolds was established in [KS01], [AV15] with analytical techniques, see in particular [AV15], Theorems 1.13 and 1.14, which suggest that an analogue of Singer's conjecture might hold even in the orbifold setting.

Remark 1.5. We notice that, although Theorem 1.4 does not apply when $Z$ is a football orbifold, there are recent results showing that football orbifolds cannot arise as orbifold limits along bubbling sequences of Einstein manifolds ([Ozu24]) or locally conformally flat manifolds ([Wan25]). Therefore, we might expect a similar obstruction even in our case.

We end this Introduction with a brief description of the contents of each Section. In Section 2 we fix the notation and recall some known facts and preliminary results. In Section 3, we construct the correction $F$ on the locally conformally flat manifold $Z$ of the form $\left(\mathbb{S}^{1} \times \mathbb{S}^{3}\right) / G$, starting from the model case of $\mathbb{S}_{t}^{1} \times \mathbb{S}^{3}$. After that, in Section 4 we compute the Weyl energy expansion for the modified metric for $Z$ of the above type and in Section 5 we define the correction $H$ on $M$ and compute the relative energy expansion. Finally, in Section 6 we define the metric on the connected sum, study the sign of (1.10) and conclude the proof of Theorems 1.1 and 1.4.

\footnotetext{
${ }^{1}$ This can be achieved in suitable classes of four-manifolds, like the class $\mathcal{Y}_{2}^{+}$defined in [CGZ20].
}

\section*{2 Preliminaries}
2.1 Notation and definitions

In order to keep computations as clear as possible, throughout the paper we adopt the Einstein summation convention, but only for repeated indices appearing once as a subscript and once as a superscript. Thus, for instance, $\sum_{i} a_{i} b^{i}=a_{i} b^{i}$, but $\sum_{i} a_{i} b_{i} \neq a_{i} b_{i}$. As a consequence, we will usually denote local coordinates of a vector $x \in \mathbb{R}^{n}$ as $x^{i}$, but sometimes we will also use the notation $x_{i}$.

We define the Riemann tensor as
$$\begin{aligned}
R(X, Y) Z & :=\nabla_{X} \nabla_{Y} Z-\nabla_{Y} \nabla_{X} Z-\nabla_{[X, Y]} Z, \\
R(X, Y, Z, W) & :=g(R(X, Y) Z, W) .
\end{aligned}$$
In local coordinates,
$$R_{i j k l}=R_{i j k}{ }^{\alpha} g_{\alpha l}, \quad R_{i j}=R_{k i j l} g^{k l}=R_{i k l j} g^{k l}=R_{k i j}{ }^{k}, \quad R_{g}=R_{i j} g^{i j} .$$
The Weyl tensor in dimension 4 is defined by (1.1) and, in local coordinates, is given by
$$W_{i j k l}=R_{i j k l}-\frac{1}{n-2}\left(R_{j k} g_{i l}+R_{i l} g_{j k}-R_{i k} g_{j l}-R_{j l} g_{i k}\right)+\frac{R_{g}}{(n-1)(n-2)}\left(g_{j k} g_{i l}-g_{i k} g_{j l}\right) .$$

The curvature tensor can be regarded as a symmetric endomorphisms on 2-forms
$$\widehat{R}: \Lambda^{2}\left(T^{*} M\right) \rightarrow \Lambda^{2}\left(T^{*} M\right),$$
cf. [Via16, Lecture 5] or [Bes08]. Indeed, given a local frame $\left\{e_{1}, \ldots, e_{n}\right\}$ with local coframe $\left\{e^{1}, \ldots, e^{n}\right\}$, then the family $\left\{e^{i} \wedge e^{j}\right\}_{i<j}$ defines a local frame for $\Lambda^{2}\left(T^{*} M\right)$ and we can define
$$\widehat{R}\left(e^{i} \wedge e^{j}\right):=\frac{1}{2} R_{i j l k} e^{k} \wedge e^{l}=\sum_{k<l} R_{i j l k} e^{k} \wedge e^{l} .$$
Notice the position reversal between $k$ and $l$. In the same way, we can regard the Weyl tensor $W$ as a symmetric trace-free endomorphism $\widehat{W}$ on $\Lambda^{2}\left(T^{*} M\right)$. In particular, if $n=4$ and $M$ is oriented, then the Hodge star operator acting on 2-forms, $*: \Lambda^{2}\left(T^{*} M\right) \rightarrow \Lambda^{2}\left(T^{*} M\right)$, satisfies $*^{2}=\mathrm{Id}$ and, under its action, $\Lambda^{2}$ decomposes into
$$\Lambda^{2}\left(T^{*} M\right)=\Lambda_{+}^{2}\left(T^{*} M\right) \oplus \Lambda_{-}^{2}\left(T^{*} M\right),$$
which are the ±1-eigenspaces of $*$ respectively and satisfy $\operatorname{dim}\left(\Lambda_{ \pm}^{2}\left(T^{*} M\right)\right)=3$. The Weyl curvature operator decomposes accordingly as follows:
$$\widehat{W}=\widehat{W}_{+}+\widehat{W}_{-}, \quad \widehat{W}_{ \pm}: \Lambda_{ \pm}^{2}\left(T^{*} M\right) \rightarrow \Lambda_{ \pm}^{2}\left(T^{*} M\right) .$$
$\widehat{W}_{+}, \widehat{W}_{-}$are called self-dual and anti self-dual Weyl curvatures respectively (as well as $W_{+}, W_{-}$which are the associated (0, 4)-tensors).

We recall that the norm of a $(0,4)$ curvature-type tensor $|T|^{2}=T^{i j k l} T_{i j k l}$ differs by a factor of 4 from the norm $\|\widehat{T}\|^{2}$ of $T$ seen as a symmetric endomorphism of $\Lambda^{2}\left(T^{*} M\right)$ :
$$|T|^{2}=4\|\widehat{T}\|^{2} .$$

\subsection*{2.2 Decomposition of pairwise symmetric 4-tensors and inverted coordinates}

The next lemma provides a decomposition of 4-tensors which belong to $\operatorname{Sym}(2) \otimes \operatorname{Sym}(2)$. This is well-known, as it provides a way to recover the second-order expansion of the metric in normal coordinates without using Jacobi fields, see Proposition 2.4 and Section 4 in [WY25]. However, we include a proof for the reader's convenience.

Lemma 2.1. Let $A=A_{\text {kijl }}$ be a covariant 4-tensor in an $n$-dimensional (real) inner product space $V$, and assume that $A$ is symmetric in $\{i, j\}$ and in $\{k, l\}$, namely
$$A_{k i j l}=A_{k j i l}=A_{l i j k} \quad \forall i, j, k, l .$$
Then $A$ uniquely decomposes as the direct sum
$$A=T \oplus C,$$
where $T$ can be written as
$$T_{k i j l}=\frac{2}{3}\left(R_{k i j l}+R_{l i j k}\right),$$
for a suitable $R$ with the symmetries of Riemann's tensor, and $C$ is a gauge term that can be written as
$$C_{k i j l}=X_{i, j k l}+X_{j, i k l},$$
where $X$ is symmetric in the last three entries.
Proof. Define
$$R_{k i j l}=\mathcal{P}(A):=\frac{1}{4}\left(A_{k i j l}-A_{i k j l}-A_{k i l j}+A_{i k l j}\right) .$$
Then it is straightforward to verify that $R$ has the symmetries of Riemann's tensor; in particular, the antisymmetric property in the first and last two entries follows from the definition of $R$, while the symmetry $R_{k i j l}=R_{j l k i}$ and the first Bianchi identity are a consequence of both (2.3) and (2.7).

At this point, define $T$ as in (2.5), and let $C:=A-T$. Then
$$\begin{aligned}
C_{k i j l} & =A_{k i j l}-\frac{1}{6}\left(A_{k i j l}-A_{i k j l}-A_{k i l j}+A_{i k l j}+A_{l i j k}-A_{i l j k}-A_{l i k j}+A_{i l k j}\right) \\
& =\frac{2}{3} A_{k i j l}-\frac{1}{3} A_{i k l j}+\frac{1}{6}\left(A_{i k j l}+A_{k i l j}+A_{i l j k}+A_{l i k j}\right),
\end{aligned}$$
and a direct computation (together with (2.3)) shows that
$$\mathcal{P}(C)=\frac{1}{4}\left(C_{k i j l}-C_{i k j l}-C_{k i l j}+C_{i k l j}\right)=0,$$
namely $C$ has no curvature part.
We next show that we can further decompose $C$ as in (2.6). Define $X$ as
$$2 X_{i, j k l}:=C_{k i j l}+C_{j i k l}-C_{i j k l} .$$
Since $R$ has the symmetries of Riemann's tensor, it is immediate to see that $T$ satisfies the relations (2.3), which are therefore also satisfied by $C$. As a consequence,
$$2 X_{i, k j l}=C_{j i k l}+C_{k i j l}-C_{i k j l}=C_{j i k l}+C_{k i j l}-C_{i j k l}=2 X_{i, j k l} .$$

Moreover, using (2.8) we also got
$$\begin{aligned}
2\left(X_{i, j k l}-X_{i, j l k}\right) & =C_{k i j l}+C_{j i k l}-C_{i j k l}-C_{l i j k}-C_{j i l k}+C_{i j l k} \\
& =C_{j i k l}-C_{i j k l}-C_{j i l k}+C_{i j l k}=0 .
\end{aligned}$$
Hence $X$ is indeed symmetric in the last three entries, and one further has
$$2\left(X_{i, j k l}+X_{j, i k l}\right)=C_{k i j l}+C_{j i k l}-C_{i j k l}+C_{k j i l}+C_{i j k l}-C_{j i k l}=2 C_{k i j l},$$
so that (2.6) holds. Finally, we notice that any $T$ of the form (2.5) trivially satisfies $\mathcal{P}(T)=T$, and that any $C$ of the form (2.6) satisfies $\mathcal{P}(C)=0$, so the decomposition (2.4) is indeed a direct sum. \(\square\)

Having a tensor with the symmetries (2.5) of $T$ (instead of only being pairwise symmetric as in (2.3)) is useful when considering inverted normal coordinates:

Lemma 2.2. Let $g_{0}$ be a Riemannian metric on $M$ and let $g:=g_{0}+t H$ be a perturbation that, in normal coordinates at a point $p \in M$, has the following expression:
$$g(x)=\left[\delta_{i j}-\frac{1}{3} R_{k i j l} z^{k} z^{l}+t T_{k i j l} \frac{z^{k} z^{l}}{|z|^{4}}+O^{(4)}\left(|z|^{3}\right)\right] d z^{i} d z^{j}, \quad \text { as }|z| \rightarrow 0$$
Assume that $T$ can be written as in (2.5), and let $f$ be a positive function on $M$ such that $f(z)=|z|^{-2}$ for $|z|$ small. Then, in inverted normal coordinates $y=z /|z|^{2}$, the inverted metric $\tilde{g}:=f^{2} g$ has the following expansion:
$$\tilde{g}(y)=\left[\delta_{i j}-\frac{1}{3} R_{k i j l} \frac{y^{k} y^{l}}{|y|^{4}}+t T_{k i j l} y^{k} y^{l}+O^{(4)}\left(|y|^{-3}\right)\right] d y^{i} d y^{j}, \quad \text { as }|y| \rightarrow+\infty$$
Proof. If $I(y)=y /|y|^{2}$ denotes the inversion map, then
$$\tilde{g}=(f \circ I)^{2}(y) I^{*}\left(\left[\delta_{i j}-\frac{1}{3} R_{k i j l} z^{k} z^{l}+t T_{k i j l} \frac{z^{k} z^{l}}{|z|^{4}}+O^{(4)}\left(|z|^{3}\right)\right] d z^{i} d z^{j}\right)$$
Recalling that
$$I^{*}\left(d z^{\alpha}\right)=d\left(\frac{y^{\alpha}}{|y|^{2}}\right)=\frac{d y^{\alpha}}{|y|^{2}}-2 \frac{y^{\alpha}(y \cdot d y)}{|y|^{4}}=\frac{1}{|y|^{2}}\left(\delta_{s}^{\alpha}-2 \frac{y^{\alpha} y_{s}}{|y|^{2}}\right) d y^{s}$$
one obtains
$$\begin{aligned}
\tilde{g}=|y|^{4}\left[\delta_{\alpha \beta}-\frac{1}{3}\right. & \left.R_{k \alpha \beta l} \frac{y^{k} y^{l}}{|y|^{4}}+t T_{k \alpha \beta l} y^{k} y^{l}+O^{(4)}\left(|y|^{-3}\right)\right] \\
& \quad \times \frac{1}{|y|^{4}}\left(\delta_{\mu}^{\alpha}-2 \frac{y^{\alpha} y_{\mu}}{|y|^{2}}\right)\left(\delta_{\nu}^{\beta}-2 \frac{y^{\beta} y_{\nu}}{|y|^{2}}\right) d y^{\mu} d y^{\nu}, \quad \text { as }|y| \rightarrow+\infty
\end{aligned}$$
Computing the $d y^{i} d y^{j}$-coefficient of the above tensor yields
$$\begin{aligned}
\tilde{g}_{i j}=\left[\delta_{\alpha \beta}-\frac{1}{3}\right. & \left.R_{k \alpha \beta l} \frac{y^{k} y^{l}}{|y|^{4}}+t T_{k \alpha \beta l} y^{k} y^{l}+O^{(4)}\left(|y|^{-3}\right)\right] \\
& \quad \times\left(\delta_{i}^{\alpha} \delta_{j}^{\beta}-2 \delta_{i}^{\alpha} \frac{y^{\beta} y_{j}}{|y|^{2}}-2 \delta_{j}^{\beta} \frac{y^{\alpha} y_{i}}{|y|^{2}}+4 \frac{y^{\alpha} y^{\beta} y_{i} y_{j}}{|y|^{4}}\right), \quad \text { as }|y| \rightarrow+\infty .
\end{aligned}$$
The result now follows by expanding the above expression and using the symmetries of Riemann's tensor and of $T$ (cf. (2.5)) to make some terms vanish. \(\square\)

Remark 2.3. If we only assume $T$ to be pairwise symmetric as in (2.3), then in (2.9) we get additional terms in $T$ which grow quadratically at infinity.

\section*{3 Construction of the modified metric on the LCF manifold}

The objective of this section is to define a correction term for the metric on the locally conformally flat manifold $\left(Z, g_{Z}\right)$ in some specific cases. This will allow us to perform the gluing with the other (non SD/ASD) manifold $\left(M, g_{M}\right)$.

To begin, recall that we are considering 4-manifolds admitting a locally conformally flat metric with positive scalar curvature. These manifolds are classified according to the following theorem by Chen, Tang and Zhu (see also [Ham97], [Ize95]):

Theorem 3.1 ([CTZ12]). Let $\left(Z, g_{Z}\right)$ be a closed, oriented, locally conformally flat 4-manifold with positive scalar curvature. Then $Z$ is diffeomorphic to $\mathbb{S}^{4}$ or to a connected sum of manifolds of type $\left(\mathbb{R} \times \mathbb{S}^{3}\right) / G$, where $G$ is a cocompact, fixed point free, discrete subgroup of the isometry group of the standard metric on $\mathbb{R} \times \mathbb{S}^{3}$. In particular, if $Z \nsimeq \mathbb{S}^{4}$, then a finite cover of $Z$ is diffeomorphic to a connected sum of copies of $\mathbb{S}^{1} \times \mathbb{S}^{3}$.

Remark 3.2. The above statement slightly differs from the one of the Main Theorem in [CTZ12], which concerns the classification of closed 4-manifolds with positive isotropic curvature (PIC). However, closed 4-manifolds admit a PIC metric if and only if they admit a locally conformally flat metric with positive scalar curvature, cf. [CTZ12, Corollary 2]. Moreover, the last statement in Theorem 3.1 follows by Corollary 1 of the same paper.

Theorem 3.1 will allow us to construct the modified metric rather explicitly as any $Z$ will be diffeomorphic to one of the manifolds classified as above. The model case is that of $\mathbb{S}^{1} \times \mathbb{S}^{3}$ with its standard metric, whose universal cover $\mathbb{R} \times \mathbb{S}^{3}$ is conformal to $\mathbb{R}^{4} \backslash\{0\}$, allowing us to define the metric correction as the series of pullbacks (with respect to the action of the fundamental group) of a suitably defined (singular) tensor on $\mathbb{R}^{4}$. We will then employ a "perturbative" argument in order to extend the construction to other quotients of $\mathbb{R} \times \mathbb{S}^{3}$. Finally, in Section 6.3 we will deal with the general case of connected sums.

\subsection*{3.1 Construction of the modified metric on $\mathbb{S}^{1} \times \mathbb{S}^{3}$}

We represent $\mathbb{S}^{1} \times \mathbb{S}^{3}$ as a cylinder
$$(Z, g):=\left(\frac{[-R / 2, R / 2] \times \mathbb{S}^{3}}{\sim}, g\right),$$
where $R>0$, and we are identifying the points $(-R / 2, q)$ with $(R / 2, q)$, for $q \in \mathbb{S}^{3}$. However, instead of the standard metric $g_{0}=d r^{2}+g_{\mathbb{S}^{3}}$, we will consider the conformal metric
$$g:=\phi(r) e^{2 r} g_{0}+(1-\phi(r)) g_{0},$$
where $\phi=\phi_{R}$ is a smooth cutoff function with $\phi(r) \equiv 1$ for $|r|<R / 100$ and $\phi(r) \equiv 0$ for $|r|>R / 10$. By our choice, $g$ is Euclidean in a tubular neighborhood of $\{0\} \times \mathbb{S}^{3}$.
Denote by $\tilde{g}$ the pullback of $g$ to the universal cover $\pi: \tilde{Z}:=\mathbb{R} \times \mathbb{S}^{3} \rightarrow Z$. Since the fundamental group $\pi_{1}(Z) \simeq \mathbb{Z}$ acts on $\mathbb{R} \times \mathbb{S}^{3}$ by translations (and a generator is the right translation $\gamma(r, q)=(r+R, q)$ ), $\tilde{g}$ will be Euclidean in a tubular neighborhood of $\left\{\{n R\} \times \mathbb{S}^{3} \mid n \in \mathbb{Z}\right\}$.

Consider the map (here we regard $\mathbb{S}^{3} \subset \mathbb{R}^{4}$ )
$$\begin{aligned}
\Phi: \mathbb{R} \times \mathbb{S}^{3} & \rightarrow \mathbb{R}^{4} \backslash\{0\}, \\
(r, q) & \rightarrow e^{r} q .
\end{aligned}$$
$\Phi$ is conformal and $\bar{g}:=\Phi_{*}(\tilde{g})$ is a conformal metric on $\mathbb{R}^{4} \backslash\{0\}$ such that, letting $t:=e^{R}$,
$$\bar{g}(x)=e^{2 \varphi(x)} g_{E}= \begin{cases}t^{-2 n} g_{E} & \text { in a tubular neighborhood of } \partial B_{t^{n}}(0)^{2} \\ |x|^{-2} g_{E} & \text { away from }\left\{\partial B_{t^{n}}(0) \mid n \in \mathbb{Z}\right\} .\end{cases}$$

Moreover, the fundamental group will act on $\mathbb{R}^{4} \backslash\{0\}$ by dilations (a generator is the map $\psi_{\gamma}(y)=$ $\psi(y):=t y=e^{R} y$ ), and $\bar{g}$ is invariant under the action of such transformations.

\subsection*{3.1.1 The singular correction}

On $\mathbb{R}^{4}$, define the singular tensor
$$h(x):=-\frac{1}{3} W_{k i j l} \frac{\left(x+e_{4}\right)^{k}\left(x+e_{4}\right)^{l}}{\left|x+e_{4}\right|^{4}} d x^{i} d x^{j}$$
where $e_{4}=(0,0,0,1) \in \mathbb{R}^{4}$. Then $h$ is TT in $\mathbb{R}^{4} \backslash\left\{-e_{4}\right\}$, and a direct computation shows that
$$\dot{B}_{g_{E}}(h)=\Delta^{2}(h)=0 \quad \text { in } \mathbb{R}^{4} \backslash\left\{-e_{4}\right\} .$$
Recalling that the Bach operator satisfies the covariance law $B_{e^{2 \varphi}}=e^{-2 \varphi} B_{g}$, we deduce that
$$\dot{B}_{e^{2 \varphi} g}(T)=\lim _{s \rightarrow 0} \frac{B_{e^{2 \varphi} g+s T}-B_{e^{2 \varphi} g}}{s}=\lim _{s \rightarrow 0} \frac{B_{e^{2 \varphi}\left(g+s e^{-2 \varphi} T\right)}-B_{e^{2 \varphi} g}}{s}=e^{-2 \varphi} \dot{B}_{g}\left(e^{-2 \varphi} T\right) .$$
Therefore, if we let
$$\bar{h}:=e^{2 \varphi} h,$$
then
$$\dot{B}_{\bar{g}}(\bar{h})=0 \quad \text { in } \mathbb{R}^{4} \backslash\left\{0,-e_{4}\right\},$$
where here $\varphi, \bar{g}$ are given by (3.4) (but this holds more generally for any $g$ and $\bar{g}=e^{2 \varphi} g$ ).
We would now like to define a singular tensor on the manifold in (3.1), whose behavior around the singular point is similar to that of $h$. To define such an object, we might consider the series over $n \in \mathbb{Z} \simeq \pi_{1}(Z)$ of the pullbacks $\psi_{n}^{*} \bar{h}$. This would (theoretically) provide us with a tensor which lifts through $\Phi^{-1}$ to an equivariant tensor on $\mathbb{R} \times \mathbb{S}^{3}$, allowing us to pass it to the quotient.

First attempt. On $\mathbb{R}^{4} \backslash\{0\}$ with the standard Euclidean coordinates, let us formally define the (singular) tensor $\tilde{A}=\tilde{A}_{i j}(y) d y^{i} d y^{j}$ given by
$$\tilde{A}_{i j}(y):=\sum_{n \in \mathbb{Z}, n \neq 0}\left(\psi_{n}^{*} \bar{h}\right)_{i j}(y) .$$
By definition of pullback and of $\psi_{n}$,
$$\begin{aligned}
\left(\psi_{n}^{*} \bar{h}\right)_{i j}(y) & =e^{2\left(\varphi \circ \psi_{n}\right)(y)} h_{\psi_{n}(y)}\left(d_{y} \psi_{n}\left(\left.\partial_{i}\right|_{y}\right), d_{y} \psi_{n}\left(\left.\partial_{j}\right|_{y}\right)\right) \\
& =e^{2\left(\varphi \circ \psi_{n}\right)(y)}\left(\partial_{i} \psi_{n}(y)\right)^{k}\left(\partial_{j} \psi_{n}(y)\right)^{l} h_{\psi_{n}(y)}\left(\left.\partial_{k}\right|_{\psi_{n}(y)},\left.\partial_{l}\right|_{\psi_{n}(y)}\right) \\
& =e^{2\left(\varphi \circ \psi_{n}\right)(y)} t^{2 n} h_{i j}\left(t^{n} y\right) .
\end{aligned}$$
Moreover, since $\psi_{n}^{*} \bar{g}=\bar{g}$, we see that, for $y$ close to $-e_{4}$ (i.e. where $e^{2 \varphi(y)} \equiv 1$ ), one has
$$e^{2\left(\varphi \circ \psi_{n}\right)(y)} \psi_{n}^{*} g_{E}=e^{2 \varphi(y)} g_{E}=g_{E} \Longrightarrow e^{2\left(\varphi \circ \psi_{n}\right)(y)}=\left|\partial_{i} \psi_{n}(y)\right|^{-2}=t^{-2 n},$$
therefore
$$\left(\psi_{n}^{*} \bar{h}\right)_{i j}(y)=h_{i j}\left(t^{n} y\right), \quad \text { for } y \sim-e_{4} .$$

\footnotetext{
${ }^{2}$ The Euclidean size of the neighborhood depends on $n$, while the size with respect to $\bar{g}$ is constant.
}

Substituting in the formula for $\tilde{A}_{i j}$ we formally get, by (3.5),
$$\tilde{A}_{i j}(y)=-\frac{1}{3} \sum_{n \in \mathbb{Z}, n \neq 0} W_{\mu i j \nu} \frac{\left(t^{n} y+e_{4}\right)^{\mu}\left(t^{n} y+e_{4}\right)^{\nu}}{\left|t^{n} y+e_{4}\right|^{4}}, \quad \text { for } y \sim-e_{4} .$$
However, we immediately notice that, for any $t>1$ (fixed), when $n<0$ is large enough one has
$$W_{\mu i j \nu} \frac{\left(t^{n} y+e_{4}\right)^{\mu}\left(t^{n} y+e_{4}\right)^{\nu}}{\left|t^{n} y+e_{4}\right|^{4}} \simeq W_{4 i j 4}, \quad \text { for } y \sim-e_{4},$$
therefore the above series does not converge and $\tilde{A}$ is not well-defined. However, this lack of convergence is only caused by a bad choice of gauge term for $h$, which will be adjusted below.

Second attempt with a gauged $h$. We start by recalling that, at a Bach-flat metric, all Lie derivatives of the metric are kernel elements for the linearized Bach operator. ${ }^{3}$ The idea now is to gauge $h$ by adding suitable Lie derivatives of $g_{E}$ in such a way to obtain a well-defined and "nice" tensor when considering the series of pullbacks as above.

Let $0 \leq \eta_{0}, \eta_{1} \leq 1$ be smooth cutoff functions such that
$$\eta_{0}(s)=\left\{\begin{array}{ll}
1 & \text { for } s \leq t^{-3 / 8} \\
0 & \text { for } s \geq t^{-1 / 8},
\end{array} \quad \eta_{1}(s)= \begin{cases}1 & \text { for } t^{-1 / 8} \leq s \leq t^{1 / 8} \\
0 & \text { for } s \leq t^{-3 / 8} \text { or } s \geq t^{3 / 8}\end{cases}\right.$$
Define the 1-forms
$$\omega_{0}(y):=\frac{1}{6} \eta_{0}(|y|) W_{4 i k 4} y^{k} d y^{i},$$
and
$$\begin{aligned}
\omega_{1}(y):=\frac{1}{3} \eta_{1}(|y|)\left\{\frac{1}{2} C_{0}(t)\right. & W_{4 i k 4}\left(y+e_{4}\right)^{k}+C_{1}(t)\left[\left(W_{k i l 4}+W_{4 i l k}\right)\left(y+e_{4}\right)^{k}\left(y+e_{4}\right)^{l}\right. \\
& \left.\left.-2 W_{4 i k 4}\left(y+e_{4}\right)^{k}\left(y+e_{4}\right)_{4}+W_{4 k l 4} \delta_{i 4}\left(y+e_{4}\right)^{k}\left(y+e_{4}\right)^{l}\right]\right\} d y^{i}
\end{aligned}$$
where the constants $C_{0}(t)$ and $C_{1}(t)$ are given by (cf. proof of Lemma 3.3)
$$C_{0}(t):=\sum_{n>0}\left[\frac{1}{\left(1-t^{n}\right)^{2}}+\frac{1}{\left(1-t^{-n}\right)^{2}}-1\right], \quad C_{1}(t):=\sum_{n>0}\left[\frac{t^{n}}{\left(1-t^{n}\right)^{3}}+\frac{t^{-n}}{\left(1-t^{-n}\right)^{3}}\right] .$$
Let $X_{0}, X_{1}$ be the dual vector fields (with respect to $g_{E}$ ) to $\omega_{0}, \omega_{1}$, and define the gauged tensor
$$\xi:=h+\mathcal{L}_{X_{0}} g_{E}+\mathcal{L}_{X_{1}} g_{E} .$$
Recalling that $\left(\mathcal{L}_{X} g\right)_{i j}=\nabla_{i} \omega_{j}+\nabla_{j} \omega_{i}$, a straightforward computation shows
$$\begin{aligned}
\xi_{i j}(y)= & -\frac{1}{3} W_{\mu i j \nu} \frac{\left(y+e_{4}\right)^{\mu}\left(y+e_{4}\right)^{\nu}}{\left|y+e_{4}\right|^{4}} \\
& + \begin{cases}\frac{1}{3} W_{4 i j 4} & \text { near } y=0 \\
\frac{1}{3}\left\{C_{0}(t) W_{4 i j 4}+C_{1}(t)\left[\left(W_{k i j 4}+W_{4 i j k}\right)\left(y+e_{4}\right)^{k}-4 W_{4 i j 4}\left(y+e_{4}\right)_{4}\right]\right\} & \text { near } y=-e_{4} .\end{cases}
\end{aligned}$$

\footnotetext{
${ }^{3}$ Indeed, if $X$ is a vector field and $\left(\phi_{t}\right)_{t}$ the associated flow at time $t$, then differentiating the identity $B_{\phi_{t}^{*} g}=\phi_{t}^{*} B_{g}=0$ at time $t=0$ yields $\dot{B}_{g}\left(\mathcal{L}_{X} g\right)=\mathcal{L}_{X} B_{g}=0$.
}

In particular, we see that $\xi$ is TT both near the origin and near $-e_{4}$ (however, it is not globally TT since it is not transverse in the cutoff regions where $\eta_{0}, \eta_{1} \neq 0,1$ ), and, by construction, $\xi$ is again a solution for $\dot{B}(\xi)=0$ in $\mathbb{R}^{4} \backslash\left\{-e_{4}\right\}$.

Let now $\bar{\xi}:=e^{2 \varphi} \xi$ in $\mathbb{R}^{4} \backslash\{0\}$. By (3.6), $\bar{\xi}$ is a solution to (3.7). Define the tensor
$$\bar{T}:=\sum_{n \in \mathbb{Z}} \psi_{n}^{*} \bar{\xi}=\sum_{n \in \mathbb{Z}} \psi_{n}^{*}\left(e^{2 \varphi} \xi\right) .$$
Using (3.9) (with $\bar{\xi}$ in place of $\bar{h}$ ), (3.10) and the definition of $\bar{\xi}$, we see that, for $y ~ \sim-e_{4}$, there holds
$$\begin{aligned}
\bar{T}_{i j}(y)=\sum_{n \in \mathbb{Z}} \xi_{i j}\left(t^{n} y\right)= & -\frac{1}{3} W_{\mu i j \nu} \frac{\left(y+e_{4}\right)^{\mu}\left(y+e_{4}\right)^{\nu}}{\left|y+e_{4}\right|^{4}}-\frac{1}{3} \sum_{n>0} W_{\mu i j \nu} \frac{\left(t^{n} y+e_{4}\right)^{\mu}\left(t^{n} y+e_{4}\right)^{\nu}}{\left|t^{n} y+e_{4}\right|^{4}} \\
& -\frac{1}{3} \sum_{n>0}\left[W_{\mu i j \nu} \frac{\left(t^{-n} y+e_{4}\right)^{\mu}\left(t^{-n} y+e_{4}\right)^{\nu}}{\left|t^{-n} y+e_{4}\right|^{4}}-W_{4 i j 4}\right] \\
+ & \frac{1}{3}\left\{C_{0}(t) W_{4 i j 4}+C_{1}(t)\left[\left(W_{k i j 4}+W_{4 i j k}\right)\left(y+e_{4}\right)^{k}-4 W_{4 i j 4}\left(y+e_{4}\right)_{4}\right]\right\} .
\end{aligned}$$
The expression will be different at a generic point $y \in \mathbb{R}^{4} \backslash\{0\}$ (due to the non-constant conformal factor $e^{2 \varphi}$ and the change in gauge terms); however, it is not difficult to see that $\bar{T}$ is pointwisely convergent and well-defined on $\mathbb{R}^{4} \backslash\left(\{0\} \cup\left\{-t^{n} e_{4} \mid n \in \mathbb{Z}\right\}\right)$. Moreover, we got
$$\dot{B}_{\bar{g}}(\bar{T})=0 \quad \text { in } \mathbb{R}^{4} \backslash\left(\{0\} \cup\left\{-t^{n} e_{4} \mid n \in \mathbb{Z}\right\}\right) .$$

Lemma 3.3. Let us write, for $y \sim-e_{4}$,
$$\bar{T}_{i j}(y)=-\frac{1}{3} W_{\mu i j \nu} \frac{\left(y+e_{4}\right)^{\mu}\left(y+e_{4}\right)^{\nu}}{\left|y+e_{4}\right|^{4}}+\bar{A}_{i j}(y),$$
where $\bar{T}$ is given by (3.15). Then $\bar{A}_{i j}(y)$ is TT for $y$ close to $-e_{4}$, and moreover
$$\bar{A}\left(-e_{4}\right)=0, \quad \nabla \bar{A}\left(-e_{4}\right)=0,$$
$$\begin{array}{r}
\partial_{k l}^{2} \bar{A}_{i j}\left(-e_{4}\right)=-\frac{1}{3} C_{2}(t)\left[\left(W_{k i j l}+W_{l i j k}\right)-4 \delta_{4 k}\left(W_{l i j 4}+W_{4 i j l}\right)-4 \delta_{4 l}\left(W_{k i j 4}+W_{4 i j k}\right)\right. \\
\left.-4 \delta_{k l} W_{4 i j 4}+24 \delta_{4 k} \delta_{4 l} W_{4 i j 4}\right],
\end{array}$$
where
$$C_{2}(t):=\sum_{n \in \mathbb{Z}, n \neq 0} \frac{t^{2 n}}{\left(1-t^{n}\right)^{4}}=2 \sum_{n>0} \frac{t^{2 n}}{\left(1-t^{n}\right)^{4}} .$$
Proof. By (3.16), we see that $\bar{A}_{i j}$ is indeed TT near $-e_{4}$. Again from (3.16) we have
$$\bar{A}_{i j}\left(-e_{4}\right)=-\frac{1}{3} W_{4 i j 4} \sum_{n>0}\left[\frac{1}{\left(1-t^{n}\right)^{2}}+\frac{1}{\left(1-t^{-n}\right)^{2}}-1\right]+\frac{1}{3} C_{0}(t) W_{4 i j 4}=0$$
where the last identity follows by the definition of $C_{0}(t)$ in (3.14). The other identities are similarly proved by straightforward computations. \(\square\)

By Lemma 3.3, we see that $\bar{T}$ is almost the singular correction we are looking for (cf. Lemma 6.4). However, when taking connected sum, in order to match the hessian of $\bar{A}$, we would also like to add a singular perturbation to the metric on $M$, which, once inverted, will provide a quadratic term corresponding to the hessian of $\bar{A}$. However, this is not possible in general as, in order for the inverted perturbation to have the right form, we would need $\partial_{k l}^{2} \bar{A}_{i j}$ to possess the same symmetries of Riemann's tensor (or, more precisely, of a symmetrized version of it, see 2.1) and this property is not satisfied in general. To fix this problem, we can add a (final) gauge term to $\xi$ which will allow us to project the hessian at $-e_{4}$ onto the right space of tensors. This will allow us to obtain the following result:

Proposition 3.4. Let $(Z, g)$ be given as in (3.1), (3.2) and let $q:=(0, S) \in Z$, where $S=-e_{4} \in \mathbb{S}^{3}$ denotes the south pole. There exists a symmetric tensor $F$, which is smooth in $Z \backslash\{q\}$, such that $\dot{B}_{g}(F)=0$ in $Z \backslash\{q\}$ and, in suitable Euclidean coordinates centered at $q$,
$$F_{i j}(x)=-\frac{1}{3} W_{\mu i j \nu} \frac{x^{\mu} x^{\nu}}{|x|^{4}}+A_{i j}(x),$$
where $A$ is smooth in a neighborhood of zero and satisfies
$$A(0)=0, \quad \nabla A(0)=0,$$
$$\begin{array}{r}
W^{k i j l} \partial_{k l}^{2} A_{i j}(0)=-\frac{1}{3} C_{2}(t)\left[W^{k i j l}\left(W_{k i j l}+W_{l i j k}\right)-4 W^{4 i j l}\left(W_{4 i j l}+W_{l i j 4}\right)\right. \\
\left.-4 W^{k i j 4}\left(W_{k i j 4}+W_{4 i j k}\right)+24 W^{4 i j 4} W_{4 i j 4}\right],
\end{array}$$
where $C_{2}(t)$ is given by (3.19). Moreover, if we let
$$T_{k i j l}:=\frac{1}{2} \partial_{k l}^{2} A_{i j}(0),$$
then $T$ can be written as in (2.5).
Remark 3.5. As we will see in Lemma 6.6, the main interaction term for the Weyl energy is indeed given by (3.22). We notice that the ADM mass of (a scalar-flat conformal blow-up of) $\mathbb{S}_{t}^{1} \times \mathbb{S}^{3}$ is proportional to $\sum_{n \in \mathbb{Z}, n \neq 0} \frac{t^{n}}{\left(1-t^{n}\right)^{2}}$. Although not identical, the expression is similar to the one in (3.19), with a related qualitative behavior in the limits $t \rightarrow 1^{+}$or $t \rightarrow+\infty$.

Proof. To begin, we notice that the tensor $\bar{T}$ defined in (3.15) is equivariant (by construction) under the action of $\psi_{n}, \forall n \in \mathbb{Z}$. As a consequence, we could lift $\bar{T}$ to an equivariant tensor on $\mathbb{R} \times \mathbb{S}^{3}$, which therefore defines a singular tensor on $Z$ (which is only singular at $(0, S)$ ). Moreover, by Lemma 3.3, the tensor $\bar{A}$ satisfies (after a translation) properties (3.21) and (3.22). The only problem is that the hessian of $\bar{A}$ does not possess the symmetries of (2.5), but we can correct this last issue by adding another gauge term.

Let $A_{k i j l}:=\partial_{k l}^{2} \bar{A}_{i j}\left(-e_{4}\right)$. Then $A_{k i j l}$ satisfies (2.3), so, by Lemma 2.1, we can decompose $A$ as in (2.4), (2.6). Let us define
$$\omega_{2}(y):=-\frac{1}{6} \eta_{1}(|y|)\left[X_{i, s t u}\left(y+e_{4}\right)^{s}\left(y+e_{4}\right)^{t}\left(y+e_{4}\right)^{u}\right] d y^{i}$$
where $\eta_{1}$ is given by (3.12) and $X$ is given by (2.6). Then, letting $X_{2}$ be the vector field dual to $\omega_{2}$, we got, for $y \sim-e_{4}$,
$$\left(\mathcal{L}_{X_{2}} g_{E}\right)_{i j}(y)=-\frac{1}{2}\left(X_{i, j k l}+X_{j, i k l}\right)\left(y+e_{4}\right)^{k}\left(y+e_{4}\right)^{l}, \quad \partial_{k l}^{2}\left(\mathcal{L}_{X_{2}} g_{E}\right)_{i j}(y)=-X_{i, j k l}-X_{j, i k l} .$$

Therefore, if we define
$$\zeta:=\xi+\mathcal{L}_{X_{2}} g_{E}=h+\mathcal{L}_{X_{0}} g_{E}+\mathcal{L}_{X_{1}} g_{E}+\mathcal{L}_{X_{2}} g_{E}, \quad \bar{\zeta}:=e^{2 \varphi} \zeta,$$
and
$$\bar{F}:=\sum_{n \in \mathbb{Z}} \psi_{n}^{*} \bar{\zeta},$$
we see that, for $y \sim-e_{4}$,
$$\bar{F}_{i j}(y)=\bar{T}_{i j}(y)-\frac{1}{2}\left(X_{i, j k l}+X_{j, i k l}\right)\left(y+e_{4}\right)^{k}\left(y+e_{4}\right)^{l} .$$
Now, as for $\bar{T}$, the tensor $\bar{F}$ is equivariant under the action of $\psi_{n} \forall n \in \mathbb{Z}$, so the lift $\tilde{F}:=\Phi^{*} \bar{F}$ defines a tensor on $\mathbb{R} \times \mathbb{S}^{3}$ which is equivariant under translations of length $n R, \forall n \in \mathbb{Z}$. Therefore $\tilde{F}$ descends to a singular tensor $F:=\pi_{*}(\tilde{F})$ on $Z$, which is smooth outside $q=(0, S)$. Moreover, by (3.17) and the fact that $e^{2 \varphi} \mathcal{L}_{X} g_{E} \in \operatorname{ker}\left(\dot{B}_{\bar{g}}\right)$, we also have $\dot{B}_{g}(F)=0$ in $Z \backslash\{q\}$. If we take Euclidean coordinates $x^{i}:=y^{i}+e_{4}$ centered at $q$, we see that $F$ decomposes as in (3.20), where now the tensor $A$ satisfies
$$A_{i j}(x)=\bar{A}_{i j}\left(x-e_{4}\right)-\frac{1}{2}\left(X_{i, j k l}+X_{j, i k l}\right) x^{k} x^{l} .$$
Hence (3.21) holds and the Hessian in (3.23) has the symmetries of (2.5). Finally, by the symmetries of $X$ and the (anti-)symmetry of Weyl's tensor, we got
$$W^{k i j l}\left(X_{i, j k l}+X_{j, i k l}\right)=0,$$
so that (3.22) follows from (3.18), (3.24). \(\square\)

Remark 3.6. We point out that, while $\bar{A}$ is TT (cf. Lemma 3.3), the tensor $A$ in (3.20) is not TT, and in general is not even traceless. To see this we notice that, by (3.24),
$$\partial_{k l}^{2} A_{i j}(0)=\partial_{k l}^{2} \bar{A}_{i j}\left(-e_{4}\right)-X_{i, j k l}-X_{j, i k l},$$
so, recalling (2.5), (2.7), the fact that $\bar{A}$ is TT and (3.18), one has
$$\partial_{k l}^{2} \operatorname{tr}(A)(0)=\frac{1}{3}(\Delta \bar{A})_{k l}\left(-e_{4}\right)=\frac{8}{9} C_{2}(t) W_{4 i j 4},$$
which does not vanish in general for all $i, j$.

\subsection*{3.2 Construction of the modified metric on $\left(\mathbb{R} \times \mathbb{S}^{3}\right) / G$}

\subsection*{3.2.1 The geometric setting}

As pointed out in Theorem 3.1, all manifolds of diffeomorphism type $Z \simeq\left(\mathbb{R} \times \mathbb{S}^{3}\right) / G$ (where, we recall, $G$ is a cocompact fixed point free discrete subgroup of the isometry group of the standard metric on $\mathbb{R} \times \mathbb{S}^{3}$ ) are finitely covered by $\mathbb{S}^{1} \times \mathbb{S}^{3}$. Therefore, given any $R>0$, we can indeed represent $Z$ as a quotient $\left(\mathbb{R} \times \mathbb{S}^{3}\right) / G$ and, without loss of generality, we might assume that there exists a normal subgroup $H \unlhd G$, of finite index and isomorphic to $\mathbb{Z}$, which acts on $\mathbb{R} \times \mathbb{S}^{3}$ via translations of length $m R$, for $m \in \mathbb{Z}$.

Remark 3.7. Without loss of generality, we can assume that $H$ is exactly the subgroup consisting of elements $g \in G$ which act on $\mathbb{R} \times \mathbb{S}^{3}$ as a translation on the first factor (as that would indeed be a normal subgroup of $G$ of finite index containing $H$ and isomorphic to $\mathbb{Z}$, so we could replace $H$ with it).

The quotient $\left(\mathbb{R} \times \mathbb{S}^{3}\right) / H$ is isometric to $\left([-R / 2, R / 2] \times \mathbb{S}^{3}\right) / \sim$, where the equivalence relation is the usual identification of the boundaries. Moreover, the (finite) quotient group $N:=G / H$ acts on $\left([-R / 2, R / 2] \times \mathbb{S}^{3}\right) / \sim$, and its quotient is isometric to $\left(\mathbb{R} \times \mathbb{S}^{3}\right) / G$. Let $\pi: \mathbb{R} \times \mathbb{S}^{3} \rightarrow Z$ denote the projection and consider $\pi((0, S))=: q \in Z$ (where $S=(0,0,0,-1) \in \mathbb{S}^{3}$ ). If we modify the standard metric on $Z$ in a conformal metric $g$ that is locally Euclidean around $q$, we can pull back $g$ through $\pi$ to get a metric which is locally Euclidean around $\pi^{-1}(q)$. Let us call $\tilde{g}:=\pi^{*}(g)$. We have the following characterization of the action of $\gamma \in N$ in $\left([-R / 2, R / 2] \times \mathbb{S}^{3}\right) / \sim$ :

Lemma 3.8. Any $\gamma \in N$ is a composition of translations and rotations by a matrix $O \in \operatorname{SO}(4)$.
Proof. Since we are assuming that the quotient $Z$ is oriented, it is known that the action of each element $\gamma \in N$ must be orientation-preserving. This automatically excludes maps which act on $\left([-R / 2, R / 2] \times \mathbb{S}^{3}\right) / \sim$ as an inversion (plus translation) on the first factor and as a rotation in SO(4) on the second factor, as well as maps acting as a translation on the first factor and as a rotation in $\mathrm{O}(4) \backslash \mathrm{SO}(4)$ in the second one (as they are both orientation-reversing). Finally, let us consider maps in which we have an inversion on the first factor and a rotation $O \in \mathrm{O}(4) \backslash \mathrm{SO}(4)$ in the second one, namely $\gamma \in N$ satisfies
$$\gamma(r, w)=(L-r, O(w)),$$
for $|L| \leq R / 2$. Since $\operatorname{det}(O)=-1$, one has
$$\operatorname{det}(I-O)=\operatorname{det}\left(I-O^{-1}\right)=\operatorname{det}\left(O^{-1}\right) \operatorname{det}(O-I)=-\operatorname{det}(I-O),$$
which implies that $\exists v \in \mathbb{S}^{3}$ satisfying $O(v)=v$. Then $(L / 2, v)$ is a fixed point for $\gamma$, contradicting the fact that the action is free. \(\square\)

By the above construction, if we regard $\left([-R / 2, R / 2] \times \mathbb{S}^{3}\right)$ as a subset of $\mathbb{R} \times \mathbb{S}^{3}$, then $\pi^{-1}(q)$ will be given by the $N$-orbit of $(0, S)$ together with all of its translations by $m R, m \in \mathbb{Z}$, and the metric $\tilde{g}$ will be Euclidean in a neighborhood of all such points (and also equivariant under the action of $G$ ).

As before, we can consider the conformal map $\Phi$ into $\mathbb{R}^{4} \backslash\{0\}$ given by (3.3), and we let $\bar{g}:=$ $\Phi_{*}(\tilde{g})=: e^{2 \varphi} g_{E}$ be a metric on $\mathbb{R}^{4} \backslash\{0\}$ conformal to $g_{E}$. This time, the dilations $\psi_{n}(y)=t^{n} y, t:=e^{R}$, correspond to the action of $H \simeq \mathbb{Z}$, while, by the above claim, the other elements $\gamma \in G$ correspond, in $\mathbb{R}^{4} \backslash\{0\}$, to dilations composed with (nontrivial) rotations in SO(4).

\subsection*{3.2.2 The singular correction}

For any given $R>0$, let $t:=e^{R}>1$. To begin, by the previous claim it is possible to write the $G$-orbit of a point $(r, w) \in \mathbb{R} \times \mathbb{S}^{3}$ as
$$G((r, w)):=\bigcup_{n \in \mathbb{Z}} \bigcup_{a=1}^{N_{0}} \gamma_{n, a}((r, w))=\bigcup_{n \in \mathbb{Z}} \bigcup_{a=1}^{N_{0}}\left(r+r_{a}+n R, O_{a}(w)\right),$$
where $N_{0}:=\#(N)$ is the cardinality of the quotient group $N,-R / 2<r_{1} \leq \cdots \leq r_{N_{0}} \leq R / 2$ and $O_{a} \in \mathrm{SO}(4) \forall a=1, \ldots, N_{0}$. Passing to $\mathbb{R}^{4} \backslash\{0\}$ via $\Phi$, we see that the $G$-orbit of a point $0 \neq y \in \mathbb{R}^{4}$ is
$$G(y):=\bigcup_{n \in \mathbb{Z}} \bigcup_{a=1}^{N_{0}} \psi_{n, a}(y)=\bigcup_{n \in \mathbb{Z}} \bigcup_{a=1}^{N_{0}} t^{n} s_{a} O_{a}(y),$$
where $\psi_{n, a}=\psi_{\gamma_{n, a}} \in \mathcal{M}_{4}$ is the Möbius map $\psi_{n, a}(y):=t^{n} s_{a} O_{a}(y)$, and $s_{a}:=e^{r_{a}}$ satisfies $t^{-1 / 2}<s_{1} \leq$ $\cdots \leq s_{N_{0}} \leq t^{1 / 2}$.

On $\mathbb{R}^{4}$, let $h$ be given by (3.5) and define $\bar{h}:=e^{2 \varphi} h$. Then $\dot{B}_{\bar{g}}(\bar{h})=0$ in $\mathbb{R}^{4} \backslash\left\{0,-e_{4}\right\}$ by the conformal covariance (3.6). Given any $\gamma_{n, a} \in G$, let $\psi_{n, a} \in \mathcal{M}_{4}$ be the corresponding Möbius map, which, by construction, is an isometry for the metric $\bar{g}$. Therefore, writing $O \in \operatorname{SO}(4)$ as $O=O_{l}^{k} \partial_{k} \otimes d x^{l}$ and arguing as in (3.9), (3.10), we see that
$$\left(\psi_{n, a}^{*} \bar{h}\right)_{i j}(y)=\left(O_{a}\right)_{i}^{\alpha}\left(O_{a}\right)_{j}^{\beta} h_{\alpha \beta}\left(\psi_{n, a}(y)\right), \quad \text { for } y \text { close to }-e_{4}, \forall \gamma_{n, a} \in G .$$

Now, as in the case of $\mathbb{S}^{1} \times \mathbb{S}^{3}$, we would like to suitably gauge $\bar{h}$ in order to make the series of its pullbacks convergent and "well-behaved" around $-e_{4}$. Let $0 \leq \tilde{\eta}_{0}, \tilde{\eta}_{1} \leq 1$ be smooth cutoff functions on $\mathbb{R} \times \mathbb{S}^{3}$ such that
$$\tilde{\eta}_{0}(r, w)=\left\{\begin{array}{ll}
1 & \text { for } r \leq r_{1}-\frac{3}{4}\left(r_{1}+R / 2\right) \\
0 & \text { for } r \geq r_{1}-\frac{1}{4}\left(r_{1}+R / 2\right),
\end{array} \quad \tilde{\eta}_{1}(r, w)= \begin{cases}1 & \text { for } \operatorname{dist}_{g_{\mathbb{R} \times \mathbb{S}^{3}}}((r, w),(0, S)) \leq d_{0} / 4 \\
0 & \text { for } \operatorname{dist}_{g_{\mathbb{R} \times \mathbb{S}^{3}}}((r, w),(0, S)) \geq d_{0} / 2,\end{cases}\right.$$
where
$$d_{0}:=\min \left\{\operatorname{dist}_{g_{\mathbb{R} \times \mathbb{S}^{3}}}\left(\left(r_{a}, O_{a}(S)\right),(0, S)\right) \mid a=1, \ldots, N_{0},\left(r_{a}, O_{a}(S)\right) \neq(0, S)\right\}$$
denotes the minimal distance (in the standard metric) between $(0, S)$ and any other point in its $G$-orbit. We can then define, on $\mathbb{R}^{4} \backslash\{0\}$,
$$\eta_{i}(y):=\Phi\left(\tilde{\eta}_{i}\left(\Phi^{-1}(y)\right)\right), \quad i=0,1,$$
which are smooth cutoffs in the Euclidean space. In particular, $\eta_{0}$ will be identically equal to 1 around all points $x \in G\left(-e_{4}\right)$ with $|x| \leq t^{-1 / 2}$ and identically zero around the others, while $\eta_{1}$ will be identically 1 around $-e_{4}$ and will vanish around all the other points in $G\left(-e_{4}\right)$.

Let us define the (preliminary) tensor
$$\xi_{0}:=h+\mathcal{L}_{X_{0}} g_{E},$$
where $X_{0}$ is the vectorfield dual to $\omega_{0}$ defined in (3.13) (now the cutoff $\eta_{0}$ in (3.13) is the one defined in (3.27)). Then $\xi_{0}$ is TT both near the origin and near $-e_{4}$, and $\dot{B}_{g_{E}}\left(\xi_{0}\right)(y)=0$ if $y \neq-e_{4}$. Let $\bar{\xi}_{0}:=e^{2 \varphi} \xi_{0}$; by conformal covariance, $\dot{B}_{\bar{g}}\left(\bar{\xi}_{0}\right)(y)=0$ if $y \neq 0,-e_{4}$. Define
$$\bar{T}_{0}:=\sum_{a=1}^{N_{0}} \sum_{n \in \mathbb{Z}} \psi_{n, a}^{*} \bar{\xi}_{0},$$
where $\psi_{n, a}$ is given by (3.25). By (3.26), (3.28) we see that, for $y \sim-e_{4}$, there holds
$$\begin{aligned}
\left(\bar{T}_{0}\right)_{i j}(y)= & \sum_{a=1}^{N_{0}} \sum_{n \in \mathbb{Z}}\left(O_{a}\right)_{i}^{\alpha}\left(O_{a}\right)_{j}^{\beta}\left(\xi_{0}\right)_{\alpha \beta}\left(t^{n} s_{a} O_{a}(y)\right) \\
= & -\frac{1}{3} \sum_{a=1}^{N_{0}} \sum_{n \geq 0}\left(O_{a}\right)_{i}^{\alpha}\left(O_{a}\right)_{j}^{\beta} W_{\mu \alpha \beta \nu} \frac{\left(t^{n} s_{a} O_{a}(y)+e_{4}\right)^{\mu}\left(t^{n} s_{a} O_{a}(y)+e_{4}\right)^{\nu}}{\left|t^{n} s_{a} O_{a}(y)+e_{4}\right|^{4}} \\
& -\frac{1}{3} \sum_{a=1}^{N_{0}} \sum_{n>0}\left(O_{a}\right)_{i}^{\alpha}\left(O_{a}\right)_{j}^{\beta}\left[W_{\mu \alpha \beta \nu} \frac{\left(t^{-n} s_{a} O_{a}(y)+e_{4}\right)^{\mu}\left(t^{-n} s_{a} O_{a}(y)+e_{4}\right)^{\nu}}{\left|t^{-n} s_{a} O_{a}(y)+e_{4}\right|^{4}}-W_{4 \alpha \beta 4}\right]
\end{aligned}$$
Hence, being $t>1$, we see that the above series is convergent and well-defined at any point $y \neq-e_{4}$ close to $-e_{4}$ (indeed, the terms in the first sum behave as $t^{-2 n}$, while the ones in the second sum behave as $t^{-n}$ ). The expression will be different for a generic point $y \in \mathbb{R}^{4} \backslash\{0\}$ due to the non-constant conformal factor $e^{2 \varphi}$ and the cutoff functions; however, it is not difficult to see that $\bar{T}_{0}$ is pointwisely
convergent and well-defined on $\mathbb{R}^{4} \backslash\left(\{0\} \cup G\left(-e_{4}\right)\right)$. We also notice that, for $y \sim-e_{4}, \bar{T}_{0}(y)$ is also a TT tensor, as $\bar{\xi}_{0}$ is and the pullback by rotations and dilations preserve the TT condition with respect to the Euclidean metric $g_{E}\left(=\bar{g}\right.$ near $\left.-e_{4}\right)$. Now, let us write
$$\left(\bar{T}_{0}\right)_{i j}(y)=-\frac{1}{3} W_{\mu i j \nu} \frac{\left(y+e_{4}\right)^{\mu}\left(y+e_{4}\right)^{\nu}}{\left|y+e_{4}\right|^{4}}+\left(\bar{A}_{0}\right)_{i j}(y) .$$
By definition, $\left(\bar{A}_{0}\right)_{i j}$ is smooth and TT in a small neighborhood of $-e_{4}$. However, in general we have $\left(\bar{A}_{0}\right)_{i j}\left(-e_{4}\right) \neq 0$ and $\nabla\left(\bar{A}_{0}\right)_{i j}\left(-e_{4}\right) \neq 0$, so, in order to perform the match between the metrics on $M$ and $Z$, we need to further gauge $\bar{\xi}_{0}$.

Let us define
$$\begin{gathered}
S_{i j}:=\left(\bar{A}_{0}\right)_{i j}\left(-e_{4}\right), \quad S_{i j, k}:=\partial_{k}\left(\bar{A}_{0}\right)_{i j}\left(-e_{4}\right) \\
\omega_{1}(y):=-\eta_{1}(y)\left\{\frac{1}{2} S_{i s}\left(y+e_{4}\right)^{s}+\frac{1}{4}\left[S_{i s, t}+S_{i t, s}-S_{s t, i}\right]\left(y+e_{4}\right)^{s}\left(y+e_{4}\right)^{t}\right\} d y^{i}
\end{gathered}$$
where $\eta_{1}$ is given by (3.27). Then, if we let $X_{1}$ be the vector field dual to $\omega_{1}$, it is straightforward to check that
$$\left(\mathcal{L}_{X_{1}} g_{E}\right)_{i j}\left(-e_{4}\right)=-\left(\bar{A}_{0}\right)_{i j}\left(-e_{4}\right), \quad \nabla\left(\mathcal{L}_{X_{1}} g_{E}\right)_{i j}\left(-e_{4}\right)=-\nabla\left(\bar{A}_{0}\right)_{i j}\left(-e_{4}\right) .$$
Define
$$\xi:=h+\mathcal{L}_{X_{0}} g_{E}+\mathcal{L}_{X_{1}} g_{E},$$
and
$$\bar{T}:=\sum_{a=1}^{N_{0}} \sum_{n \in \mathbb{Z}} \psi_{n, a}^{*} \bar{\xi}, \quad \bar{\xi}:=e^{2 \varphi} \xi .$$
As for $\bar{T}_{0}, \bar{T}$ is well-defined on $\mathbb{R}^{4} \backslash\left(\{0\} \cup G\left(-e_{4}\right)\right)$, and it satisfies by construction
$$\dot{B}_{\bar{g}}(\bar{T})=0 \quad \text { in } \mathbb{R}^{4} \backslash\left(\{0\} \cup G\left(-e_{4}\right)\right) .$$

Lemma 3.9. Let us write, for $y \sim-e_{4}$,
$$\bar{T}_{i j}=-\frac{1}{3} W_{\mu i j \nu} \frac{\left(y+e_{4}\right)^{\mu}\left(y+e_{4}\right)^{\nu}}{\left|y+e_{4}\right|^{4}}+\bar{A}_{i j}(y),$$
where $\bar{T}$ is given by (3.33). Then $\bar{A}_{i j}(y)$ is TT for $y$ close to $-e_{4}$, and one further has
$$\bar{A}\left(-e_{4}\right)=0, \quad \nabla \bar{A}\left(-e_{4}\right)=0,$$
$$\begin{aligned}
\partial_{k l}^{2} \bar{A}_{i j}\left(-e_{4}\right)=-\frac{1}{3} C_{2}(t)[ & \left(W_{k i j l}+W_{l i j k}\right)-4 \delta_{4 k}\left(W_{l i j 4}+W_{4 i j l}\right)-4 \delta_{4 l}\left(W_{k i j 4}+W_{4 i j k}\right) \\
& \left.-4 \delta_{k l} W_{4 i j 4}+24 \delta_{4 k} \delta_{4 l} W_{4 i j 4}\right]+O\left((t-1)^{-1}\right), \quad \text { as } t \rightarrow 1^{+} .
\end{aligned}$$
Here $C_{2}(t)$ is given by (3.19); in particular,
$$C_{2}(t)=\frac{\pi^{4}}{45(t-1)^{4}}+O\left((t-1)^{-3}\right), \quad \text { as } t \rightarrow 1^{+} .$$

Remark 3.10. Differently from the case of $\mathbb{S}^{1} \times \mathbb{S}^{3}$ (see Lemma 3.3), here we do not have an exact (useful) identity for the hessian of $\bar{A}$. However, by letting $t \rightarrow 1^{+}$(that is, by shrinking the length $R$ of the cylinder to zero), we see that the leading term in the hessian is again given by the quantity appearing in (3.18). This is motivated by the fact that, differently from the poles coming from pure dilations, the poles of $\bar{T}$ coming from dilations and rotations do not accumulate toward $-e_{4}$ as $t \rightarrow 1^{+}$.

Proof. The identities (3.34) and the fact that $\bar{A}$ is TT directly follow by construction, see (3.29), (3.30), (3.31), (3.33).

Let us turn our attention to (3.35). Since the gauge terms in (3.32) are given (around $-e_{4}$ ) by polynomials of order $\leq 1$, we see that the hessian of $\bar{A}$ is equal to that of $\bar{A}_{0}$. Look at (3.30), and, for $y \sim-e_{4}$, consider a single term of the series
$$V_{i j}(y):=-\frac{1}{3} W_{\mu i j \nu} \frac{\left(t^{n} s O(y)+e_{4}\right)^{\mu}\left(t^{n} s O(y)+e_{4}\right)^{\nu}}{\left|t^{n} s O(y)+e_{4}\right|^{4}},$$
where we dropped the subscript $a$ for convenience. We have
$$\begin{aligned}
\partial_{k l}^{2} V_{i j}(y)= & -\frac{1}{3} t^{2 n} s^{2} W_{\mu i j \nu}\left[\frac{O_{k}^{\mu} O_{l}^{\nu}+O_{l}^{\mu} O_{k}^{\nu}}{\left|t^{n} s O(y)+e_{4}\right|^{4}}-4\left(t^{n} s y_{l}+O_{l}^{4}\right) \frac{O_{k}^{\mu}\left(t^{n} s O_{\beta}^{\nu} y^{\beta}+\delta_{4}^{\nu}\right)+\left(t^{n} s O_{\alpha}^{\mu} y^{\alpha}+\delta_{4}^{\mu}\right) O_{k}^{\nu}}{\left|t^{n} s O(y)+e_{4}\right|^{6}}\right. \\
-4 \delta_{k l} & \frac{\left(t^{n} s O_{\alpha}^{\mu} y^{\alpha}+\delta_{4}^{\mu}\right)\left(t^{n} s O_{\beta}^{\nu} y^{\beta}+\delta_{4}^{\nu}\right)}{\left|t^{n} s O(y)+e_{4}\right|^{6}}-4\left(t^{n} s y_{k}+O_{k}^{4}\right) \frac{O_{l}^{\mu}\left(t^{n} s O_{\beta}^{\nu} y^{\beta}+\delta_{4}^{\nu}\right)+\left(t^{n} s O_{\alpha}^{\mu} y^{\alpha}+\delta_{4}^{\mu}\right) O_{l}^{\nu}}{\left|t^{n} s O(y)+e_{4}\right|^{6}} \\
& \left.+24\left(t^{n} s y_{k}+O_{k}^{4}\right)\left(t^{n} s y_{l}+O_{l}^{4}\right) \frac{\left(t^{n} s O_{\alpha}^{\mu} y^{\alpha}+\delta_{4}^{\mu}\right)\left(t^{n} s O_{\beta}^{\nu} y^{\beta}+\delta_{4}^{\nu}\right)}{\left|t^{n} s O(y)+e_{4}\right|^{8}}\right] .
\end{aligned}$$
Let us now look at $\partial_{k l}^{2} V_{i j}\left(-e_{4}\right)$.
- Assume $O=\mathrm{Id}$ and $s=1$. Then
$$\begin{aligned}
\partial_{k l}^{2} V_{i j}\left(-e_{4}\right)=-\frac{1}{3} \frac{t^{2 n}}{\left(1-t^{n}\right)^{4}} & {\left[\left(W_{k i j l}+W_{l i j k}\right)-4 \delta_{4 k}\left(W_{l i j 4}+W_{4 i j l}\right)-4 \delta_{4 l}\left(W_{k i j 4}+W_{4 i j k}\right)\right.} \\
& \left.-4 \delta_{k l} W_{4 i j 4}+24 \delta_{4 k} \delta_{4 l} W_{4 i j 4}\right],
\end{aligned}$$
so, when summing over $n \in \mathbb{Z}, n \neq 0$, we obtain exactly the first term of (3.35), cf. (3.19).
- Assume $O \neq \mathrm{Id}$ and $t^{-1 / 2} \leq s \leq t^{1 / 2}$. Notice that, by virtue of Remark 3.7, we cannot have $s \neq 1$ and $O=\mathrm{Id}$, so all the remaining cases are included in this second one. Being $O \in \mathrm{SO}(4)$, looking at (3.37) we deduce
$$\left|\partial_{k l}^{2} V_{i j}\left(-e_{4}\right)\right| \leq C \frac{t^{2 n} s^{2}}{\left|-t^{n} s O_{4}^{\beta} e_{\beta}+e_{4}\right|^{4}}=C \frac{t^{2 n} s^{2}}{\left(t^{2 n} s^{2}-2 t^{n} s O_{4}^{4}+1\right)^{2}},$$
where $C>0$ does not depend on $n \in \mathbb{Z}$, neither on $O \in \operatorname{SO}(4)$ or $s \in\left[t^{-1 / 2}, t^{1 / 2}\right]$. Being $\operatorname{Id} \neq O \in \operatorname{SO}(4)$ with free action, then $\tau:=O_{4}^{4} \in[-1,1)$ necessarily. Consider the series over $n \in \mathbb{Z}$ of the above coefficients. Setting $\varepsilon=\log t$ we have
$$\begin{aligned}
\sum_{n \in \mathbb{Z}} \frac{t^{2 n} s^{2}}{\left(t^{2 n} s^{2}-2 t^{n} s O_{4}^{4}+1\right)^{2}} & =\frac{1}{s^{2}} \sum_{n \in \mathbb{Z}} \frac{e^{2 n \varepsilon}}{\left(e^{2 n \varepsilon}-2 \tau s^{-1} e^{n \varepsilon}+s^{-2}\right)^{2}} \\
& =\frac{1}{\varepsilon s^{2}}\left(\sum_{n \in \mathbb{Z}} \varepsilon \frac{e^{2 n \varepsilon}}{\left(e^{2 n \varepsilon}-2 \tau s^{-1} e^{n \varepsilon}+s^{-2}\right)^{2}}\right)=: \frac{1}{\varepsilon s^{2}} S(\varepsilon)
\end{aligned}$$

If $t \rightarrow 1^{+}$, then $\varepsilon \rightarrow 0^{+}$and the Riemann sum converges to
$$S(\varepsilon) \xrightarrow{\varepsilon \rightarrow 0^{+}} \int_{-\infty}^{-\infty} \frac{e^{2 x}}{\left(e^{2 x}-2 \tau s^{-1} e^{x}+s^{-2}\right)^{2}} d x=\int_{0}^{+\infty} \frac{r}{\left(r^{2}-2 \tau s^{-1} r+s^{-2}\right)^{2}} d r=: I(\tau, s),$$
where $I(\tau, s)$ is finite for any $\tau \in[-1,1)$ and $s \in[1 / 2,2]$, with $I(\tau, s) \rightarrow+\infty$ as $\tau \rightarrow 1^{-}$. Hence (recall that $\tau=O_{4}^{4}$ )
$$\sum_{n \in \mathbb{Z}}\left|\partial_{k l}^{2} V_{i j}\left(-e_{4}\right)\right| \leq \frac{C\left(O_{4}^{4}\right)}{(t-1)}, \quad \text { as } t \rightarrow 1^{+} .$$

The above considerations prove (3.35).
Finally, we prove (3.36). Letting again $\varepsilon:=\log t$, we rewrite
$$C_{2}(t)=2 \sum_{n>0} \frac{t^{2 n}}{\left(t^{n}-1\right)^{4}}=2 \sum_{n>0} \frac{e^{2 n \varepsilon}}{\left(e^{n \varepsilon}-1\right)^{4}}=: 2 \sum_{n>0}\left[\frac{1}{n^{4} \varepsilon^{4}}+f(n \varepsilon)\right],$$
where
$$f(x):=\frac{e^{2 x}}{\left(e^{x}-1\right)^{4}}-\frac{1}{x^{4}} .$$
One has
$$\sum_{n=1}^{+\infty} \frac{1}{n^{4} \varepsilon^{4}}=\frac{\pi^{4}}{90(t-1)^{4}}+O\left((t-1)^{-3}\right), \quad \text { as } t \rightarrow 1^{+} .$$
As for the other term, we notice that $f$ is continuous in $(0,+\infty), f(x)=O\left(x^{-3}\right)$ as $x \rightarrow 0^{+}$and $f(x)=O\left(x^{-4}\right)$ as $x \rightarrow+\infty$. Therefore there exists a constant $C>0$ such that $|f(x)| \leq C x^{-3} \forall x>0$, which implies
$$\sum_{n=1}^{+\infty} f(n \varepsilon) \leq \frac{C}{\varepsilon^{3}} \sum_{n=1}^{+\infty} \frac{1}{n^{3}} \leq \frac{C^{\prime}}{(t-1)^{3}}, \quad \text { as } t \rightarrow 1^{+}$$
so that (3.36) holds. \(\square\)

Finally, we have the extension of Proposition 3.4 to this setting:
Proposition 3.11. Let $(Z, g)$ and $q \in Z$ be given as in Section 3.2.1. There exists a symmetric tensor $F$, which is smooth in $Z \backslash\{q\}$, such that $\dot{B}_{g}(F)=0$ in $Z \backslash\{q\}$ and, in suitable Euclidean coordinates centered at $q$, (3.20) holds, where $A$ is smooth up to zero and satisfies
$$A(0)=0, \quad \nabla A(0)=0,$$
$$\begin{aligned}
W^{k i j l} \partial_{k l}^{2} A_{i j}(0)=- & \frac{1}{3} C_{2}(t)\left[W^{k i j l}\left(W_{k i j l}+W_{l i j k}\right)-4 W^{4 i j l}\left(W_{4 i j l}+W_{l i j 4}\right)\right. \\
& \left.-4 W^{k i j 4}\left(W_{k i j 4}+W_{4 i j k}\right)+24 W^{4 i j 4} W_{4 i j 4}\right]+O\left((t-1)^{-1}\right), \quad \text { as } t \rightarrow 1^{+},
\end{aligned}$$
where $C_{2}(t)$ is given by (3.19) and satisfies (3.36). Moreover, if we let
$$T_{k i j l}:=\frac{1}{2} \partial_{k l}^{2} A_{i j}(0),$$
then $T$ can be written as in (2.5).
The proof is identical to that of Proposition 3.4. As in Remark 3.6, we notice that $A$ will not be TT in general around 0.

\section*{4 Weyl energy of the modified metric on $Z=\left(\mathbb{R} \times \mathbb{S}^{3}\right) / G$}

We know that any locally conformally flat manifold $\left(Z, g_{Z}\right)$ is diffeomorphic to one of the models described in Theorem 3.1. Since we are only interested in the diffeomorphism class of the connected sum $Z \# M$, we might assume without loss of generality that ( $Z, g_{Z}$ ) is indeed one of the model manifolds described in Section 3. Then, by Propositions 3.4, 3.11, we know that, in the particular case in which $Z=\left(\mathbb{R} \times \mathbb{S}^{3}\right) / G$, there exists a point $q \in Z$ with $g_{Z}$ Euclidean around $q$, and there exists a tensor $F$, singular at $q$, which satisfies the properties described in the aforementioned propositions.

Let us consider the modified metric $g_{b}:=g_{Z}+b^{2} F$, where $b \ll 1$ is a small parameter. By virtue of (3.20), we have the following expansion of $g_{b}$ in Euclidean coordinates at $q$ :
$$\left(g_{b}\right)_{i j}(x)=\delta_{i j}+b^{2}\left(-\frac{1}{3} W_{k i j l}^{M} \frac{x^{k} x^{l}}{|x|^{4}}+A_{i j}(x)\right) \quad \text { in } B_{\delta}(0),$$
for $\delta>0$ small enough. Consider a small parameter $\gamma$ such that $0<a, b \ll \gamma \ll \delta / 2$; we now want to estimate
$$\mathcal{W}_{\gamma}^{Z}\left(g_{b}\right):=\int_{Z \backslash B_{\gamma}^{g}(q)}\left|W^{g_{b}}\right|^{2} d V_{g_{b}}$$
To begin, Taylor-expanding $g_{b}$ with respect to $t:=b^{2}$, we get
$$\mathcal{W}_{\gamma}^{Z}\left(g_{b}\right)=\mathcal{W}_{\gamma}^{Z}\left(g_{Z}\right)+\left.b^{2} \frac{d}{d t}\right|_{t=0} \mathcal{W}_{\gamma}^{Z}\left(g_{b}\right)+\left.\frac{b^{4}}{2} \frac{d^{2}}{d t^{2}}\right|_{t=0} \mathcal{W}_{\gamma}^{Z}\left(g_{b}\right)+O\left(b^{6}\right) .$$
Notice that the error term $O\left(b^{6}\right)$ also depends upon $\gamma$; however, since $b \ll \gamma$, the error term remains uniformly controlled by, e.g., $b^{5}$, and hence still of higher order. Being $g_{Z}$ locally conformally flat, we have $\mathcal{W}_{\gamma}^{Z}\left(g_{Z}\right)=0$ and
$$\left.\frac{d}{d t}\right|_{t=0} \mathcal{W}_{\gamma}^{Z}\left(g_{b}\right)=-4 \int_{Z \backslash B_{\gamma}^{g}(q)}\left(W_{\alpha i j \beta}^{g_{Z}} \nabla^{\alpha} \nabla^{\beta} F^{i j}+\frac{1}{2} W_{\alpha i j \beta}^{g_{Z}} R^{\alpha \beta} F^{i j}\right) d V_{g_{Z}}=0,$$
so we are left with
$$\mathcal{W}_{\gamma}^{Z}\left(g_{b}\right)=\left.\frac{b^{4}}{2} \frac{d^{2}}{d t^{2}}\right|_{t=0} \mathcal{W}_{\gamma}^{Z}\left(g_{b}\right)+O\left(b^{6}\right) .$$
Using again the fact that $g_{Z}$ is locally conformally flat, we see from (4.2) that
$$\left.\frac{d^{2}}{d t^{2}}\right|_{t=0} \mathcal{W}_{\gamma}^{Z}\left(g_{b}\right)=-4 \int_{Z \backslash B_{\gamma}^{g}(q)}\left(\dot{W}_{\alpha i j \beta} \nabla^{\alpha} \nabla^{\beta} F^{i j}+\frac{1}{2} \dot{W}_{\alpha i j \beta} R^{\alpha \beta} F^{i j}\right) d V_{g_{Z}}$$
Integrating by parts twice, one has
$$\begin{aligned}
\int_{Z \backslash B_{\gamma}}\left(\dot{W}_{\alpha i j \beta}\right. & \left.\nabla^{\alpha} \nabla^{\beta} F^{i j}+\frac{1}{2} \dot{W}_{\alpha i j \beta} R^{\alpha \beta} F^{i j}\right) d V_{g_{Z}} \\
= & -\int_{Z \backslash B_{\gamma}}\left(\nabla^{\alpha} \dot{W}_{\alpha i j \beta} \nabla^{\beta} F^{i j}+\frac{1}{2} \dot{W}_{\alpha i j \beta} R^{\alpha \beta} F^{i j}\right) d V_{g_{Z}}-\int_{\partial B_{\gamma}} \dot{W}_{n i j \beta} \nabla^{\beta} F^{i j} d \sigma_{g_{Z}} \\
= & \int_{Z \backslash B_{\gamma}}\left(\nabla^{\beta} \nabla^{\alpha} \dot{W}_{\alpha i j \beta} F^{i j}+\frac{1}{2} \dot{W}_{\alpha i j \beta} R^{\alpha \beta} F^{i j}\right) d V_{g_{Z}}-\int_{\partial B_{\gamma}} \dot{W}_{n i j \beta} \nabla^{\beta} F^{i j} d \sigma_{g_{Z}} \\
& \quad+\int_{\partial B_{\gamma}} \nabla^{\alpha} \dot{W}_{\alpha i j n} F^{i j} d \sigma_{g_{Z}}
\end{aligned}$$
where the $n$ subscript denotes the tensor component with respect to the inward pointing unit normal (so it points towards the exterior of $B_{\gamma}$ ).

We now observe the following:

Claim. Let $\left(g_{t}\right)_{t}$ be a smooth family of metrics. If $g=g_{0}$ is locally conformally flat, then
$$\left.\frac{d}{d t}\right|_{t=0}\left(\nabla^{\alpha} \nabla^{\beta} W_{\alpha i j \beta}^{g_{t}}\right)=\nabla^{\alpha} \nabla^{\beta} \dot{W}_{\alpha i j \beta}^{g} .$$
Proof. Let $h=\left.\frac{d}{d t}\right|_{t=0} g_{t}$. Being the metric tensor and its inverse parallel at each time and using the fact that $W^{g} \equiv 0$, we have
$$\begin{aligned}
\left.\frac{d}{d t}\right|_{t=0}\left(\nabla^{\alpha} \nabla^{\beta} W_{\alpha i j \beta}\right) & =\left.\frac{d}{d t}\right|_{t=0}\left(g^{\alpha \mu} g^{\beta \nu} \nabla_{\mu} \nabla_{\nu} W_{\alpha i j \beta}\right) \\
= & \left.g^{\alpha \mu} g^{\beta \nu} \frac{d}{d t}\right|_{t=0}\left(\nabla_{\mu} \nabla_{\nu} W_{\alpha i j \beta}\right)-\left(h^{\alpha \mu} g^{\beta \nu}+g^{\alpha \mu} h^{\beta \nu}\right) \nabla_{\mu} \nabla_{\nu} W_{\alpha i j \beta} \\
= & \left.g^{\alpha \mu} g^{\beta \nu} \frac{d}{d t}\right|_{t=0}\left[\partial_{\mu}\left(\nabla_{\nu} W_{\alpha i j \beta}\right)-\Gamma_{\mu \nu}^{s} \nabla_{s} W_{\alpha i j \beta}-\Gamma_{\mu \alpha}^{s} \nabla_{\nu} W_{s i j \beta}\right. \\
& \left.\quad-\Gamma_{\mu i}^{s} \nabla_{\nu} W_{\alpha s j \beta}-\Gamma_{\mu j}^{s} \nabla_{\nu} W_{\alpha i s \beta}-\Gamma_{\mu \beta}^{s} \nabla_{\nu} W_{\alpha i j s}\right] \\
= & g^{\alpha \mu} g^{\beta \nu}\left[\nabla_{\mu}\left(\left.\frac{d}{d t}\right|_{t=0}\left(\nabla_{\nu} W_{\alpha i j \beta}\right)\right)-\dot{\Gamma}_{\mu \nu}^{s} \nabla_{s} W_{\alpha i j \beta}-\dot{\Gamma}_{\mu \alpha}^{s} \nabla_{\nu} W_{s i j \beta}\right. \\
& \left.\quad-\dot{\Gamma}_{\mu i}^{s} \nabla_{\nu} W_{\alpha s j \beta}-\dot{\Gamma}_{\mu j}^{s} \nabla_{\nu} W_{\alpha i s \beta}-\dot{\Gamma}_{\mu \beta}^{s} \nabla_{\nu} W_{\alpha i j s}\right] \\
= & g^{\alpha \mu} g^{\beta \nu} \nabla_{\mu}\left[\left.\frac{d}{d t}\right|_{t=0}\left(\partial_{\nu} W_{\alpha i j \beta}-\Gamma_{\nu \alpha}^{s} W_{s i j \beta}-\Gamma_{\nu i}^{s} W_{\alpha s j \beta}-\Gamma_{\nu j}^{s} W_{\alpha i s \beta}-\Gamma_{\nu \beta}^{s} W_{\alpha i j s}\right)\right] \\
= & g^{\alpha \mu} g^{\beta \nu} \nabla_{\mu}\left[\nabla_{\nu} \dot{W}_{\alpha i j \beta}-\dot{\Gamma}_{\nu \alpha}^{s} W_{s i j \beta}-\dot{\Gamma}_{\nu i}^{s} W_{\alpha s j \beta}-\dot{\Gamma}_{\nu j}^{s} W_{\alpha i s \beta}-\dot{\Gamma}_{\nu \beta}^{s} W_{\alpha i j s}\right] \\
= & g^{\alpha \mu} g^{\beta \nu} \nabla_{\mu} \nabla_{\nu} \dot{W}_{\alpha i j \beta}=\nabla^{\alpha} \nabla^{\beta} \dot{W}_{\alpha i j \beta},
\end{aligned}$$
thus the claim holds. \(\square\)

As a consequence of the previous claim, we see that, at our locally conformally flat metric $g_{Z}$, one has
$$\dot{B}_{i j}(F)=-4\left(\nabla^{\alpha} \nabla^{\beta} \dot{W}_{\alpha i j \beta}+\frac{1}{2} R^{\alpha \beta} \dot{W}_{\alpha i j \beta}\right) .$$
Using this identity together with (4.3), (4.4), (4.5) and the fact that $\dot{B}_{g_{Z}}(F)(p)=0$ for $p \neq q$ (see e.g. Proposition 3.4), we deduce that
$$\mathcal{W}_{\gamma}^{Z}\left(g_{b}\right)=2 b^{4}\left(\int_{\partial B_{\gamma}} \dot{W}_{n i j \beta} \nabla^{\beta} F^{i j} d \sigma_{g_{Z}}-\int_{\partial B_{\gamma}} \nabla^{\alpha} \dot{W}_{\alpha i j n} F^{i j} d \sigma_{g_{Z}}\right)+O\left(b^{6}\right) .$$
In particular, since we are assuming $g_{Z}$ to be Euclidean inside $B_{\delta}(q)$ and since $\gamma<\delta / 2$, we finally get
$$\mathcal{W}_{\gamma}^{Z}\left(g_{b}\right)=2 b^{4}\left(\int_{\partial B_{\gamma}} \dot{W}_{\eta i j \beta} \partial^{\beta} F^{i j} \nu^{\eta} d \sigma-\int_{\partial B_{\gamma}} \partial^{\alpha} \dot{W}_{\alpha i j \eta} F^{i j} \nu^{\eta} d \sigma\right)+O\left(b^{6}\right)$$
where $\nu=\left(\nu^{1}, \ldots, \nu^{4}\right)=x /|x|$ is the unit normal and $d \sigma$ is the Euclidean surface element.
We now want to expand both integrals in (4.6), starting from the second one. To begin, recall the formula for the linearized Weyl tensor at the Euclidean metric (see [MM25], equation (2.8) for the linearized of Weyl tensor in the same notation employed here; in alternative, see e.g. [CM20], which employs a different convention):
$$\begin{aligned}
\dot{W}_{\alpha i j \beta}= & \frac{1}{2}\left[\partial_{\alpha j}^{2} F_{i \beta}+\partial_{i \beta}^{2} F_{\alpha j}-\partial_{\alpha \beta}^{2} F_{i j}-\partial_{i j}^{2} F_{\alpha \beta}\right]+\frac{1}{4}\left[\delta_{\alpha \beta} \Delta F_{i j}+\delta_{i j} \Delta F_{\alpha \beta}-\delta_{i \beta} \Delta F_{\alpha j}-\delta_{\alpha j} \Delta F_{i \beta}\right] \\
& +\frac{1}{4}\left[\left(\partial_{\alpha}(\delta F)_{j}+\partial_{j}(\delta F)_{\alpha}-\partial_{\alpha j}^{2}(\operatorname{tr} F)\right) \delta_{i \beta}+\left(\partial_{i}(\delta F)_{\beta}+\partial_{\beta}(\delta F)_{i}-\partial_{i \beta}^{2}(\operatorname{tr} F)\right) \delta_{\alpha j}\right. \\
& \left.-\left(\partial_{\alpha}(\delta F)_{\beta}+\partial_{\beta}(\delta F)_{\alpha}-\partial_{\alpha \beta}^{2}(\operatorname{tr} F)\right) \delta_{i j}-\left(\partial_{i}(\delta F)_{j}+\partial_{j}(\delta F)_{i}-\partial_{i j}^{2}(\operatorname{tr} F)\right) \delta_{\alpha \beta}\right] \\
& +\frac{1}{6}\left(-\Delta(\operatorname{tr} F)+\left(\delta^{2} F\right)\right)\left(\delta_{\alpha \beta} \delta_{i j}-\delta_{\alpha j} \delta_{\beta i}\right)
\end{aligned}$$
where $\delta F$ denotes the (Euclidean) divergence of $F$. We can also compute the Euclidean divergence of (4.7), obtaining
$$\begin{aligned}
\partial^{\alpha} \dot{W}_{\alpha i j \beta}= & \frac{1}{4}\left[\partial_{j} \Delta F_{i \beta}-\partial_{\beta} \Delta F_{i j}+\partial_{i \beta}^{2}(\delta F)_{j}-\partial_{i j}^{2}(\delta F)_{\beta}\right] \\
& +\frac{1}{12}\left[\left(\partial_{j}\left(\delta^{2} F\right)-\partial_{j} \Delta(\operatorname{tr} F)\right) \delta_{i \beta}-\left(\partial_{\beta}\left(\delta^{2} F\right)-\partial_{\beta} \Delta(\operatorname{tr} F)\right) \delta_{i j}\right] .
\end{aligned}$$

Let us write (cf. (3.20))
$$F_{i j}(x)=K_{i j}(x)+A_{i j}(x), \quad K_{i j}(x):=-\frac{1}{3} W_{\mu i j \nu} \frac{x^{\mu} x^{\nu}}{|x|^{4}} .$$
While it is immediate to check that $K(x)$ is a TT tensor with respect to the Euclidean metric for any $x \neq 0$, the tensor $A$ in general has nontrivial trace and divergence near the origin, see e.g. Remark 3.6. Moreover, from the definition of $K$ we easily compute
$$\partial_{\beta} \Delta K_{i j}=\partial_{\beta}\left(\frac{8}{3} W_{k i j l} \frac{x^{k} x^{l}}{|x|^{6}}\right)=\frac{8}{3} W_{k i j l}\left(\frac{\delta_{\beta}^{k} x^{l}+x^{k} \delta_{\beta}^{l}}{|x|^{6}}-6 \frac{x_{\beta} x^{k} x^{l}}{|x|^{8}}\right),$$
while, since the singular term of $F$ is TT, we further have
$$\partial_{i \beta}^{2}(\delta F)_{j}=\partial_{i \beta}^{2}(\delta A)_{j}, \quad \partial_{j}\left(\delta^{2} F\right)=\partial_{j}\left(\delta^{2} A\right), \quad \partial_{j} \Delta(\operatorname{tr} F)=\partial_{j} \Delta(\operatorname{tr} A) .$$

Lemma 4.1. In the above setting, it holds
$$\int_{\partial B_{\gamma}} \partial^{\alpha} \dot{W}_{\alpha i j \beta} F^{i j} \nu^{\beta} d \sigma=\mathcal{C}_{1} \gamma^{-4}+\frac{\pi^{2}}{6} \partial^{k l} A^{i j}(0) W_{k i j l}+O\left(\gamma^{2}\right), \quad \text { as } \gamma \rightarrow 0^{+}$$
for a real constant $\mathcal{C}_{1}=\mathcal{C}_{1}\left(W^{M}(p)\right)$.
Proof. From (4.8) one has
$$\begin{aligned}
\int_{\partial B_{\gamma}} \partial^{\alpha} \dot{W}_{\alpha i j \beta} & F^{i j} \nu^{\beta} d \sigma=\frac{1}{4} \int_{\partial B_{\gamma}}\left[\partial_{j} \Delta F_{i \beta}-\partial_{\beta} \Delta F_{i j}+\partial_{i \beta}^{2}(\delta F)_{j}-\partial_{i j}^{2}(\delta F)_{\beta}\right] F^{i j} \nu^{\beta} d \sigma \\
+ & \frac{1}{12} \int_{\partial B_{\gamma}}\left[\left(\partial_{j}\left(\delta^{2} F\right)-\partial_{j} \Delta(\operatorname{tr} F)\right) \delta_{i \beta} F^{i j} \nu^{\beta}-\left(\partial_{\beta}\left(\delta^{2} F\right)-\partial_{\beta} \Delta(\operatorname{tr} F)\right)(\operatorname{tr} F) \nu^{\beta}\right] d \sigma .
\end{aligned}$$
Using now (4.9), (4.11), the above expression becomes
$$\begin{aligned}
\int_{\partial B_{\gamma}} \partial^{\alpha} \dot{W}_{\alpha i j \beta} F^{i j} & \nu^{\beta} d \sigma=\frac{1}{4} \int_{\partial B_{\gamma}}\left[\partial_{j} \Delta K_{i \beta}-\partial_{\beta} \Delta K_{i j}\right] K^{i j} \nu^{\beta} d \sigma \\
& +\frac{1}{4} \int_{\partial B_{\gamma}}\left[\partial_{j} \Delta K_{i \beta}-\partial_{\beta} \Delta K_{i j}\right] A^{i j} \nu^{\beta} d \sigma \\
& +\frac{1}{4} \int_{\partial B_{\gamma}}\left[\partial_{j} \Delta A_{i \beta}-\partial_{\beta} \Delta A_{i j}+\partial_{i \beta}^{2}(\delta A)_{j}-\partial_{i j}^{2}(\delta A)_{\beta}\right] K^{i j} \nu^{\beta} d \sigma \\
& +\frac{1}{4} \int_{\partial B_{\gamma}}\left[\partial_{j} \Delta A_{i \beta}-\partial_{\beta} \Delta A_{i j}+\partial_{i \beta}^{2}(\delta A)_{j}-\partial_{i j}^{2}(\delta A)_{\beta}\right] A^{i j} \nu^{\beta} d \sigma \\
& +\frac{1}{12} \int_{\partial B_{\gamma}}\left(\partial^{j}\left(\delta^{2} A\right)-\partial_{j} \Delta(\operatorname{tr} A)\right) \delta_{i \beta} K^{i j} \nu^{\beta} d \sigma \\
& +\frac{1}{12} \int_{\partial B_{\gamma}}\left[\left(\partial_{j}\left(\delta^{2} A\right)-\partial_{j} \Delta(\operatorname{tr} A)\right) \delta_{i \beta} A^{i j} \nu^{\beta}-\left(\partial_{\beta}\left(\delta^{2} A\right)-\partial_{\beta} \Delta(\operatorname{tr} A)\right)(\operatorname{tr} A) \nu^{\beta}\right]
\end{aligned}$$

We now consider separately at each of the above integrals.
- By looking at (4.9), (4.10), it is easy to see (after a change of variables) that the RHS of (4.13) is of order $\gamma^{-4}$. Since we are going to show below that all the other integrals provide higher order contributions, we conclude that
$$\frac{1}{4} \int_{\partial B_{\gamma}}\left[\partial_{j} \Delta K_{i \beta}-\partial_{\beta} \Delta K_{i j}\right] K^{i j} \nu^{\beta} d \sigma=: \mathcal{C}_{1} \gamma^{-4}$$
where $\mathcal{C}_{1}=\mathcal{C}_{1}\left(W^{M}(p)\right)$ is the constant appearing in (4.12).
- Let us consider (4.14). To begin, recalling (4.10) and using the symmetries of Weyl's tensor and Bianchi's identity we got
$$\begin{aligned}
& W_{k i \beta l}\left(\frac{\delta_{j}^{k} x^{l}+x^{k} \delta_{j}^{l}}{|x|^{6}}-6 \frac{x_{j} x^{k} x^{l}}{|x|^{8}}\right)-W_{k i j l}\left(\frac{\delta_{\beta}^{k} x^{l}+x^{k} \delta_{\beta}^{l}}{|x|^{6}}-6 \frac{x_{\beta} x^{k} x^{l}}{|x|^{8}}\right) \\
= & \left(W_{j i \beta l}+W_{l i \beta j}-W_{\beta i j l}-W_{l i j \beta}\right) \frac{x^{l}}{|x|^{6}}-6 W_{k i \beta l} \frac{x_{j} x^{k} x^{l}}{|x|^{8}}+6 W_{k i j l} \frac{x_{\beta} x^{k} x^{l}}{|x|^{8}} \\
= & -3 W_{l i j \beta} \frac{x^{l}}{|x|^{6}}-6 W_{k i \beta l} \frac{x_{j} x^{k} x^{l}}{|x|^{8}}+6 W_{k i j l} \frac{x_{\beta} x^{k} x^{l}}{|x|^{8}} .
\end{aligned}$$
Substituting this formula in (4.14) and Taylor-expanding $A_{i j}$, we get
$$\begin{aligned}
\frac{2}{3} \int_{\partial B_{\gamma}}\left[-3 W_{l i j \beta}\right. & \left.\frac{x^{l}}{|x|^{6}}-6 W_{k i \beta l} \frac{x_{j} x^{k} x^{l}}{|x|^{8}}+6 W_{k i j l} \frac{x_{\beta} x^{k} x^{l}}{|x|^{8}}\right] \times \\
& \times\left(A^{i j}(0)+\partial_{s} A^{i j}(0) x^{s}+\frac{1}{2} \partial_{s t}^{2} A^{i j}(0) x^{s} x^{t}+\frac{1}{6} \partial_{s t u}^{3} A^{i j}(0) x^{s} x^{t} x^{u}+O\left(|x|^{4}\right)\right) \frac{x^{\beta}}{|x|} d \sigma .
\end{aligned}$$
Next, we notice that $W_{k i \beta l} x^{k} x^{l} x^{\beta}=0$ by skew-symmetry and that all the terms involving an odd number of derivatives of $A^{i j}$ are zero because we got an integral over a sphere of an odd number of coordinate functions (which vanishes because odd in at least one direction). Moreover, we have $A(0)=0, \nabla A(0)=0$, see (3.21), (3.38). Hence we obtain
$$(4.14)=\frac{1}{3} \int_{\partial B_{\gamma}}\left[-3 W_{l i j \beta} \frac{x^{l}}{|x|^{6}}+6 W_{k i j l} \frac{x_{\beta} x^{k} x^{l}}{|x|^{8}}\right] \partial_{s t}^{2} A^{i j}(0) \frac{x^{s} x^{t} x^{\beta}}{|x|} d \sigma+O\left(\gamma^{2}\right),$$
which, after a change of variables, can be rewritten as
$$(4.14)=W_{k i j l} \partial_{s t}^{2} A^{i j}(0) \int_{\mathbb{S}^{3}} z^{k} z^{l} z^{s} z^{t} d \sigma+O\left(\gamma^{2}\right)$$
We can now employ the identity (cf. [Bre08], Corollary 29)
$$\int_{\mathbb{S}^{3}} x^{\mu} x^{\nu} x^{k} x^{l} d \sigma_{\mathbb{S}^{3}}=\frac{\pi^{2}}{12}\left(\delta^{\mu \nu} \delta^{k l}+\delta^{\mu k} \delta^{\nu l}+\delta^{\mu l} \delta^{\nu k}\right)$$
to finally obtain that
$$(4.14)=\frac{\pi^{2}}{6} W_{k i j l} \partial^{k l} A^{i j}(0)+O\left(\gamma^{2}\right) .$$
- Consider now (4.15). Taylor-expanding the terms involving derivatives of $A$ and performing a subsequent change of variables, one gets
$$(4.15)=O\left(\gamma^{2}\right) .$$

Notice that there are no terms of order $\gamma$ because the integrals involve an odd number of coordinate functions. The same argument also shows that
$$(4.17)=O\left(\gamma^{2}\right) .$$
\begin{itemize}
\item[-] Finally, a change of variables shows that $(4.16)+(4.18)=O\left(\gamma^{3}\right)$.
\end{itemize}

Combining the last two items and (4.19), (4.21), we finally obtain (4.12), concluding our proof. \(\square\)

We now focus on the first integral in (4.6); using (4.7), (4.9) and the fact that $K$ is TT, we compute
$$\begin{aligned}
& \dot{W}_{\eta i j \beta} \partial^{\beta} F^{i j} \nu^{\eta}=\frac{1}{2}\left[\partial_{\eta j}^{2} F_{i \beta}+\partial_{i \beta}^{2} F_{\eta j}-\partial_{\eta \beta}^{2} F_{i j}-\partial_{i j}^{2} F_{\eta \beta}\right] \partial^{\beta} F^{i j} \nu^{\eta}+\frac{1}{4}\left[\Delta F_{i j} \partial^{\beta} F^{i j} \nu_{\beta}-\Delta F_{i \beta} \partial^{\beta} F^{i j} \nu_{j}\right] \\
& \quad+\frac{1}{4}\left[\Delta F_{\eta \beta} \partial^{\beta}(\operatorname{tr} A) \nu^{\eta}-\Delta F_{\eta j}(\delta A)^{j} \nu^{\eta}\right] \\
& \quad+\frac{1}{4}\left[\partial_{i}(\delta A)_{\beta}+\partial_{\beta}(\delta A)_{i}-\partial_{i \beta}^{2}(\operatorname{tr} A)\right] \partial^{\beta} F^{i j} \nu_{j}-\frac{1}{4}\left[\partial_{i}(\delta A)_{j}+\partial_{j}(\delta A)_{i}-\partial_{i j}^{2}(\operatorname{tr} A)\right] \partial^{\beta} F^{i j} \nu_{\beta} \\
& \quad+\frac{1}{4}\left[\partial_{\eta}(\Delta A)_{j}+\partial_{j}(\delta A)_{\eta}-\partial_{\eta j}^{2}(\operatorname{tr} A)\right](\delta A)^{j} \nu^{\eta}-\frac{1}{4}\left[\partial_{\eta}(\Delta A)_{\beta}+\partial_{\beta}(\delta A)_{\eta}-\partial_{\eta \beta}^{2}(\operatorname{tr} A)\right] \partial^{\beta}(\operatorname{tr} A) \nu^{\eta} \\
& \quad+\frac{1}{6}\left[-\Delta(\operatorname{tr} A)+\left(\delta^{2} A\right)\right]\left(\partial^{\beta}(\operatorname{tr} A) \nu_{\beta}-(\delta A)^{j} \nu_{j}\right)
\end{aligned}$$

To begin, we show that the integrals of all trace and divergence terms of (4.22) generate higher-order contributions.

Lemma 4.2. There holds
$$\begin{aligned}
\int_{\partial B_{\gamma}} \dot{W}_{\eta i j \beta} \partial^{\beta} F^{i j} \nu^{\eta} d \sigma & =\frac{1}{2} \int_{\partial B_{\gamma}}\left[\partial_{\eta j}^{2} F_{i \beta}+\partial_{i \beta}^{2} F_{\eta j}-\partial_{\eta \beta}^{2} F_{i j}-\partial_{i j}^{2} F_{\eta \beta}\right] \partial^{\beta} F^{i j} \nu^{\eta} d \sigma \\
& +\frac{1}{4} \int_{\partial B_{\gamma}}\left[\Delta F_{i j} \partial^{\beta} F^{i j} \nu_{\beta}-\Delta F_{i \beta} \partial^{\beta} F^{i j} \nu_{j}\right] d \sigma+O\left(\gamma^{2}\right), \quad \text { as } \gamma \rightarrow 0^{+}
\end{aligned}$$
Proof. We consider each divergence or trace term of (4.22) separately.
\begin{itemize}
\item[-] Consider the term in the second line of (4.22). Integrating and recalling (4.9), one has
\end{itemize}
$$\begin{aligned}
& \frac{1}{4} \int_{\partial B_{\gamma}}\left[\Delta F_{\eta \beta} \partial^{\beta}(\operatorname{tr} A)-\Delta F_{\eta j}(\delta A)^{j}\right] \nu^{\eta} d \sigma \\
& \quad=\frac{1}{4} \int_{\partial B_{\gamma}}\left[\left(\frac{8}{3} W_{k \eta \beta l} \frac{x^{k} x^{l}}{|x|^{6}}+\Delta A_{\eta \beta}(x)\right) \partial^{\beta}(\operatorname{tr} A)-\left(\frac{8}{3} W_{k \eta j l} \frac{x^{k} x^{l}}{|x|^{6}}+\Delta A_{\eta j}(x)\right)(\delta A)^{j}\right] \frac{x^{\eta}}{|x|} d \sigma \\
& \quad=\frac{2}{3} \int_{\partial B_{\gamma}}\left[\left(W_{k \eta \beta l} \partial^{\beta}(\operatorname{tr} A)-W_{k \eta j l}(\delta A)^{j}\right) \frac{x^{k} x^{l} x^{\eta}}{|x|^{7}} d \sigma+O\left(\gamma^{3}\right)=O\left(\gamma^{3}\right),\right.
\end{aligned}$$
due to symmetry properties of Weyl's tensor.
\begin{itemize}
\item[-] Consider the first term in the third line of (4.22), namely $\frac{1}{4}\left[\partial_{i}(\delta A)_{\beta}+\partial_{\beta}(\delta A)_{i}-\partial_{i \beta}^{2}(\operatorname{tr} A)\right] \partial^{\beta} F^{i j} \nu_{j}$.
\end{itemize} One has
$$\begin{aligned}
& \frac{1}{4} \int_{\partial B_{\gamma}}\left[\partial_{i}(\delta A)_{\beta}(x)+\partial_{\beta}(\delta A)_{i}(x)-\partial_{i \beta}^{2}(\operatorname{tr} A)(x)\right] \partial^{\beta}\left(-\frac{1}{3} W_{k}{ }^{i j} \frac{x^{k} x^{l}}{|x|^{4}}+A^{i j}(x)\right) \frac{x_{j}}{|x|} d \sigma \\
& =-\frac{1}{12} \int_{\partial B_{\gamma}}\left[\partial_{i}(\delta A)_{\beta}(x)+\partial_{\beta}(\delta A)_{i}(x)-\partial_{i \beta}^{2}(\operatorname{tr} A)(x)\right] W_{k}{ }^{i j}{ }_{l}\left(\frac{\delta^{\beta k} x^{l}+x^{k} \delta^{\beta l}}{|x|^{4}}-4 \frac{x^{\beta} x^{k} x^{l}}{|x|^{6}}\right) \frac{x_{j}}{|x|} d \sigma+O\left(\gamma^{3}\right)
\end{aligned}$$

Taylor-expanding the $A$-terms we get
$$\begin{aligned}
-\frac{1}{12} \int_{\partial B_{\gamma}}\left[\partial_{i}(\delta A)_{\beta}(0)+\partial_{\beta}(\delta A)_{i}(0)\right. & \left.-\partial_{i \beta}^{2}(\operatorname{tr} A)(0)\right]\left(\frac{W^{\beta i j}{ }_{k} x^{k}+W_{k}{ }^{i j \beta} x^{k}}{|x|^{4}}-4 W_{k}{ }^{i j}{ }_{l} \frac{x^{\beta} x^{k} x^{l}}{|x|^{6}}\right) \frac{x_{j}}{|x|} d \sigma \\
- & \frac{1}{12} \int_{\partial B_{\gamma}}\left\{\left[\partial_{i s}^{2}(\delta A)_{\beta}(0)+\partial_{\beta s}^{2}(\delta A)_{i}(0)-\partial_{i \beta s}^{3}(\operatorname{tr} A)(0)\right] x^{s} \times\right. \\
& \left.\times\left(\frac{W^{\beta i j}{ }_{k} x^{k}+W_{k}{ }^{i j \beta} x^{k}}{|x|^{4}}-4 W_{k}{ }^{i j}{ }_{l} \frac{x^{\beta} x^{k} x^{l}}{|x|^{6}}\right) \frac{x_{j}}{|x|}\right\} d \sigma+O\left(\gamma^{2}\right)
\end{aligned}$$
However, the first integral above vanishes due to the skew-symmetry and trace-free property of Weyl's tensor, while the second integral vanishes because of the odd number of coordinate functions. Hence
$$\frac{1}{4} \int_{\partial B_{\gamma}}\left[\partial_{i}(\delta A)_{\beta}(x)+\partial_{\beta}(\delta A)_{i}(x)-\partial_{i \beta}^{2}(\operatorname{tr} A)(x)\right] \partial^{\beta} F^{i j} \nu_{j} d \sigma=O\left(\gamma^{2}\right)$$
- A computation similar to the previous one also shows that the second term in the third line of (4.22) satifies
$$-\frac{1}{4} \int_{\partial B_{\gamma}}\left[\left(\partial_{i}(\delta A)_{j}+\partial_{j}(\delta A)_{i}-\partial_{i j}^{2}(\operatorname{tr} A)\right] \partial^{\beta} F^{i j} \nu_{\beta} d \sigma=O\left(\gamma^{2}\right)\right.$$

Finally, it is immediate to see that the terms in the last two lines of (4.22) are of order $O\left(\gamma^{3}\right)$. This concludes the proof. \(\square\)

We now compute the integral over $\partial B_{\gamma}$ of a generic term in the first line of (4.22); recalling (4.9) one has
$$\begin{aligned}
& \int_{\partial B_{\gamma}} \partial_{\alpha \beta}^{2} F_{i j} \partial_{\tau} F_{s t} \nu_{\eta} d \sigma=\int_{\partial B_{\gamma}} \partial_{\alpha \beta}^{2} K_{i j} \partial_{\tau} K_{s t} \nu_{\eta} d \sigma \\
&-\frac{1}{3} \int_{\partial B_{\gamma}} \partial_{\alpha \beta}^{2} A_{i j}(x) W_{\mu s t \nu}\left(\frac{\delta_{\tau}^{\mu} x^{\nu}+x^{\mu} \delta_{\tau}^{\nu}}{|x|^{4}}-4 \frac{x_{\tau} x^{\mu} x^{\nu}}{|x|^{6}}\right) \frac{x^{\eta}}{|x|} d \sigma \\
&-\frac{1}{3} \int_{\partial B_{\gamma}} W_{k i j l}\left(\frac{\delta_{\alpha}^{k} \delta_{\beta}^{l}+\delta_{\beta}^{k} \delta_{\alpha}^{l}}{|x|^{4}}-4 \frac{x_{\beta}\left(\delta_{\alpha}^{k} x^{l}+x^{k} \delta_{\alpha}^{l}\right)}{|x|^{6}}-4 \frac{\delta_{\alpha \beta} x^{k} x^{l}+x_{\alpha}\left(\delta_{\beta}^{k} x^{l}+x^{k} \delta_{\beta}^{l}\right)}{|x|^{6}}\right. \\
&\left.\quad+24 \frac{x_{\alpha} x_{\beta} x^{k} x^{l}}{|x|^{8}}\right) \partial_{\tau} A_{s t}(x) \frac{x^{\eta}}{|x|} d \sigma+\int_{\partial B_{\gamma}} \partial_{\alpha \beta}^{2} A_{i j}(x) \partial_{\tau} A_{s t}(x) \frac{x^{\eta}}{|x|} d \sigma .
\end{aligned}$$
Taylor-expanding $\partial_{\tau} A_{s t}$ and $\partial_{\alpha \beta}^{2} A_{i j}$ at 0, using the symmetry of the integrals and a change of variables, one gets
$$\begin{aligned}
& \int_{\partial B_{\gamma}} \partial_{\alpha \beta}^{2} F_{i j} \partial_{\tau} F_{s t} \nu_{\eta} d \sigma=\int_{\partial B_{\gamma}} \partial_{\alpha \beta}^{2} K_{i j} \partial_{\tau} K_{s t} \nu_{\eta} d \sigma \\
&-\frac{1}{3} \int_{\mathbb{S}^{3}} \partial_{\alpha \beta}^{2} A_{i j}(0) W_{\mu s t \nu}\left(\delta_{\tau}^{\mu} x^{\nu}+x^{\mu} \delta_{\tau}^{\nu}-4 x_{\tau} x^{\mu} x^{\nu}\right) x^{\eta} d \sigma \\
&-\frac{1}{3} \int_{\mathbb{S}^{3}} W_{k i j l}\left[\delta_{\alpha}^{k} \delta_{\beta}^{l}+\delta_{\beta}^{k} \delta_{\alpha}^{l}-4 x_{\beta}\left(\delta_{\alpha}^{k} x^{l}+x^{k} \delta_{\alpha}^{l}\right)-4\left(\delta_{\alpha \beta} x^{k} x^{l}+x_{\alpha}\left(\delta_{\beta}^{k} x^{l}+x^{k} \delta_{\beta}^{l}\right)\right)\right. \\
&\left.+24 x_{\alpha} x_{\beta} x^{k} x^{l}\right] \partial_{\tau \xi}^{2} A_{s t}(0) x^{\eta} x^{\xi} d \sigma+O\left(\gamma^{2}\right)
\end{aligned}$$

Lemma 4.3. There holds
$$\int_{\partial B_{\gamma}} \dot{W}_{\eta i j \beta} \partial^{\beta} F^{i j} \nu^{\eta} d \sigma=\mathcal{C}_{2} \gamma^{-4}+\frac{\pi^{2}}{6} \partial^{k l} A^{i j}(0) W_{k i j l}+O\left(\gamma^{2}\right), \quad \text { as } \gamma \rightarrow 0^{+}$$
for a real constant $\mathcal{C}_{2}=\mathcal{C}_{2}\left(W^{M}(p)\right)$.

Proof. By looking at (4.9), (4.10), it is easy to see (after a change of variables) that the first term on the RHS of (4.24) is of order $\gamma^{-4}$. Since from (4.24) it is clear that all the other terms are of order 1, we conclude from (4.23) and (4.24) that
$$\begin{aligned}
\frac{1}{2} \int_{\partial B_{\gamma}}\left[\partial_{\eta j}^{2} K_{i \beta}\right. & \left.+\partial_{i \beta}^{2} K_{\eta j}-\partial_{\eta \beta}^{2} K_{i j}-\partial_{i j}^{2} K_{\eta \beta}\right] \partial^{\beta} K^{i j} \nu^{\eta} d \sigma \\
+ & \frac{1}{4} \int_{\partial B_{\gamma}}\left[\Delta K_{i j} \partial^{\beta} K^{i j} \nu_{\beta}-\Delta K_{i \beta} \partial^{\beta} K^{i j} \nu_{j}\right] d \sigma=: \mathcal{C}_{2} \gamma^{-4}
\end{aligned}$$
where $\mathcal{C}_{2}=\mathcal{C}_{2}\left(W^{M}(p)\right)$ is the constant appearing in (4.25).
We now focus on the contribution of order 1; by looking again at (4.23) and (4.24), we see that it is given by the following integrals:
$$\begin{aligned}
& -\frac{1}{6} \int_{\mathbb{S}^{3}}\left(\partial^{\eta j} A^{i \beta}(0)+\partial^{i \beta} A^{\eta j}(0)-\partial^{\eta \beta} A^{i j}(0)-\partial^{i j} A^{\eta \beta}(0)\right) W_{\mu i j \nu}\left(\delta_{\beta}^{\mu} x^{\nu}+x^{\mu} \delta_{\beta}^{\nu}-4 x_{\beta} x^{\mu} x^{\nu}\right) x_{\eta} \\
& -\frac{1}{12} \int_{\mathbb{S}^{3}}\left[W_{\mu i j \nu}\left(\delta_{\beta}^{\mu} x^{\nu}+x^{\mu} \delta_{\beta}^{\nu}-4 x_{\beta} x^{\mu} x^{\nu}\right)\left(\Delta A^{i j}(0) x^{\beta}-\Delta A^{i \beta}(0) x^{j}\right)\right. \\
- & \frac{1}{6} \int_{\mathbb{S}^{3}} W_{k i \beta l}\left[\delta_{\eta}^{k} \delta_{j}^{l}+\delta_{j}^{k} \delta_{\eta}^{l}-4 x_{\eta}\left(\delta_{j}^{k} x^{l}+x^{k} \delta_{j}^{l}\right)-4\left(\delta_{j \eta} x^{k} x^{l}+x_{j}\left(\delta_{\eta}^{k} x^{l}+x^{k} \delta_{\eta}^{l}\right)\right)+24 x_{j} x_{\eta} x^{k} x^{l}\right] \partial^{\beta \xi} A^{i j}(0) x^{\eta} x_{\xi} \\
- & \frac{1}{6} \int_{\mathbb{S}^{3}} W_{k \eta j l}\left[\delta_{i}^{k} \delta_{\beta}^{l}+\delta_{\beta}^{k} \delta_{i}^{l}-4 x_{\beta}\left(\delta_{i}^{k} x^{l}+x^{k} \delta_{i}^{l}\right)-4\left(\delta_{i \beta} x^{k} x^{l}+x_{i}\left(\delta_{\beta}^{k} x^{l}+x^{k} \delta_{\beta}^{l}\right)\right)+24 x_{i} x_{\beta} x^{k} x^{l}\right] \partial^{\beta \xi} A^{i j}(0) x^{\eta} x_{\xi} \\
+ & \frac{1}{6} \int_{\mathbb{S}^{3}} W_{k i j l}\left[\delta_{\eta}^{k} \delta_{\beta}^{l}+\delta_{\beta}^{k} \delta_{\eta}^{l}-4 x_{\beta}\left(\delta_{\eta}^{k} x^{l}+x^{k} \delta_{\eta}^{l}\right)-4\left(\delta_{\eta \beta} x^{k} x^{l}+x_{\eta}\left(\delta_{\beta}^{k} x^{l}+x^{k} \delta_{\beta}^{l}\right)\right)+24 x_{\eta} x_{\beta} x^{k} x^{l}\right] \partial^{\beta \xi} A^{i j}(0) x^{\eta} x_{\xi} \\
+ & \frac{1}{6} \int_{\mathbb{S}^{3}} W_{k \eta \beta l}\left[\delta_{i}^{k} \delta_{j}^{l}+\delta_{j}^{k} \delta_{i}^{l}-4 x_{j}\left(\delta_{i}^{k} x^{l}+x^{k} \delta_{i}^{l}\right)-4\left(\delta_{i j} x^{k} x^{l}+x_{i}\left(\delta_{j}^{k} x^{l}+x^{k} \delta_{j}^{l}\right)\right)+24 x_{i} x_{j} x^{k} x^{l}\right] \partial^{\beta \xi} A^{i j}(0) x^{\eta} x_{\xi} \\
- & \frac{1}{12} \sum_{\alpha} \int_{\mathbb{S}^{3}} W_{k i j l}\left[2 \delta_{\alpha}^{k} \delta_{\alpha}^{l}-4 x_{\alpha}\left(\delta_{\alpha}^{k} x^{l}+x^{k} \delta_{\alpha}^{l}\right)-4 x^{k} x^{l}-4 x_{\alpha}\left(\delta_{\alpha}^{k} x^{l}+x^{k} \delta_{\alpha}^{l}\right)+24\left(x_{\alpha}\right)^{2} x^{k} x^{l}\right] \partial^{\beta \xi} A^{i j}(0) x_{\beta} x_{\xi} \\
+ & \frac{1}{12} \sum_{\alpha} \int_{\mathbb{S}^{3}} W_{k i \beta l}\left[2 \delta_{\alpha}^{k} \delta_{\alpha}^{l}-4 x_{\alpha}\left(\delta_{\alpha}^{k} x^{l}+x^{k} \delta_{\alpha}^{l}\right)-4 x^{k} x^{l}-4 x_{\alpha}\left(\delta_{\alpha}^{k} x^{l}+x^{k} \delta_{\alpha}^{l}\right)+24\left(x_{\alpha}\right)^{2} x^{k} x^{l}\right] \partial^{\beta \xi} A^{i j}(0) x_{j} x_{\xi}
\end{aligned}$$
We need to compute each term in (4.27). We start noticing that
$$\begin{aligned}
\int_{\mathbb{S}^{3}} W_{\mu i j \nu}\left(\delta_{\beta}^{\mu} x^{\nu}+x^{\mu} \delta_{\beta}^{\nu}-4 x_{\beta} x^{\mu} x^{\nu}\right) x_{\eta} & =\int_{\mathbb{S}^{3}}\left(W_{\beta i j \nu} x^{\nu}+W_{\mu i j \beta} x^{\mu}\right) x_{\eta}-4 W_{\mu i j \nu} \int_{\mathbb{S}^{3}} x_{\beta} x^{\mu} x^{\nu} x_{\eta} \\
& =\left(W_{\beta i j \eta}+W_{\eta i j \beta}\right) \int_{\mathbb{S}^{3}}\left(x_{\eta}\right)^{2}-4 W_{\mu i j \nu} \int_{\mathbb{S}^{3}} x_{\beta} x^{\mu} x^{\nu} x_{\eta} \\
& =\frac{\pi^{2}}{2}\left(W_{\beta i j \eta}+W_{\eta i j \beta}\right)-\frac{\pi^{2}}{3} W_{\mu i j \nu}\left(\delta_{\beta \eta} \delta^{\mu \nu}+\delta_{\beta}^{\mu} \delta_{\eta}^{\nu}+\delta_{\beta}^{\nu} \delta_{\eta}^{\mu}\right) \\
& =\frac{\pi^{2}}{6}\left(W_{\beta i j \eta}+W_{\eta i j \beta}\right),
\end{aligned}$$
where we used (cf. [Bre08, Corollary 29])
$$\int_{\mathbb{S}^{3}} x_{\eta} x_{\nu}=\frac{\pi^{2}}{2} \delta_{\eta \nu},$$
(4.20) and the trace-free property of Weyl tensor. Similar computations also show that
$$\int_{\mathbb{S}^{3}} W_{\mu i j \nu}\left(\delta_{\beta}^{\mu} x^{\nu}+x^{\mu} \delta_{\beta}^{\nu}-4 x_{\beta} x^{\mu} x^{\nu}\right) x^{\beta}=0=\int_{\mathbb{S}^{3}} W_{\mu i j \nu}\left(\delta_{\beta}^{\mu} x^{\nu}+x^{\mu} \delta_{\beta}^{\nu}-4 x_{\beta} x^{\mu} x^{\nu}\right) x^{j} .$$

Next, we got
$$\begin{aligned}
& \int_{\mathbb{S}^{3}} W_{k i \beta l} {\left[\delta_{\eta}^{k} \delta_{j}^{l}+\delta_{j}^{k} \delta_{\eta}^{l}-4 x_{\eta}\left(\delta_{j}^{k} x^{l}+x^{k} \delta_{j}^{l}\right)-4\left(\delta_{j \eta} x^{k} x^{l}+x_{j}\left(\delta_{\eta}^{k} x^{l}+x^{k} \delta_{\eta}^{l}\right)\right)+24 x_{j} x_{\eta} x^{k} x^{l}\right] \partial^{\beta \xi} A^{i j} x^{\eta} x_{\xi} } \\
&=\int\left(W_{\eta i \beta j}+W_{j i \beta \eta}\right) \partial^{\beta \xi} A^{i j} x^{\eta} x_{\xi}-4 \int\left(W_{j i \beta k}+W_{k i \beta j}\right) \partial^{\beta \xi} A^{i j} x^{k} x_{\xi} \\
&-4 \int\left[W_{k i \beta l} \partial^{\beta \xi} A^{i j} x^{k} x^{l} x_{j} x_{\xi}+\left(W_{\eta i \beta k}+W_{k i \beta \eta}\right) \partial^{\beta \xi} A^{i j} x^{k} x^{\eta} x_{j} x_{\xi}\right]+24 W_{k i \beta l} \partial^{\beta \xi} A^{i j} \int x^{k} x^{l} x_{j} x_{\xi} \\
&=-\frac{3}{2} \pi^{2} \partial^{\beta \xi} A^{i j}\left(W_{\xi i \beta j}+W_{j i \beta \xi}\right)-\frac{\pi^{2}}{3} \partial^{\beta \xi} A^{i j}\left(3 W_{j i \beta \xi}+3 W_{\xi i \beta j}\right)+2 \pi^{2}\left(W_{j i \beta \xi}+W_{\xi i \beta j}\right) \\
&=-\frac{\pi^{2}}{2} \partial^{\beta \xi} A^{i j}(0)\left(W_{j i \beta \xi}+W_{\xi i \beta j}\right) .
\end{aligned}$$
Similarly,
$$\begin{aligned}
\int_{\mathbb{S}^{3}} & W_{k \eta j l}\left[\delta_{i}^{k} \delta_{\beta}^{l}+\delta_{\beta}^{k} \delta_{i}^{l}-4 x_{\beta}\left(\delta_{i}^{k} x^{l}+x^{k} \delta_{i}^{l}\right)-4\left(\delta_{i \beta} x^{k} x^{l}+x_{i}\left(\delta_{\beta}^{k} x^{l}+x^{k} \delta_{\beta}^{l}\right)\right)+24 x_{i} x_{\beta} x^{k} x^{l}\right] \partial^{\beta \xi} A^{i j} x^{\eta} x_{\xi} \\
& =\int\left(W_{i \eta j \beta}+W_{\beta \eta j i}\right) \partial^{\beta \xi} A^{i j} x^{\eta} x_{\xi}-4 \int\left(W_{i \eta j k}+W_{k \eta j i}\right) \partial^{\beta \xi} A^{i j} x_{\beta} x^{k} x^{\eta} x_{\xi} \\
& -4 \sum_{i} W_{k \eta j l} \partial^{i \xi} A^{i j} \int x^{k} x^{l} x^{\eta} x_{\xi}-4 \int\left(W_{\beta \eta j k}+W_{k \eta j \beta}\right) \partial^{\beta \xi} A^{i j} x_{i} x^{k} x^{\eta} x_{\xi}+0 \\
& =\frac{\pi^{2}}{2} \partial^{\beta \xi} A^{i j}\left(W_{i \xi j \beta}+W_{\beta \xi j i}\right)-\frac{\pi^{2}}{3} \partial^{\beta \xi} A^{i j}\left(W_{i \xi j \beta}+W_{\beta \xi j i}+W_{i \beta j \xi}+W_{\xi \beta j i}\right) \\
& -0-\frac{\pi^{2}}{3} \partial^{\beta \xi} A^{i j}\left(W_{\beta \xi j i}+W_{i \xi j \beta}+W_{\beta i j \xi}+W_{\xi i j \beta}\right) \\
& =\frac{\pi^{2}}{6} \partial^{\beta \xi} A^{i j}\left(W_{i \xi j \beta}+W_{\beta \xi j i}\right) .
\end{aligned}$$
Also, by exchanging the indices $\beta$ and $j$ in (4.31) (except on $A$ ), we immediately see that
$$\begin{aligned}
\int_{\mathbb{S}^{3}} W_{k i j l} & {\left[\delta_{\eta}^{k} \delta_{\beta}^{l}+\delta_{\beta}^{k} \delta_{\eta}^{l}-4 x_{\beta}\left(\delta_{\eta}^{k} x^{l}+x^{k} \delta_{\eta}^{l}\right)-4\left(\delta_{\eta \beta} x^{k} x^{l}+x_{\eta}\left(\delta_{\beta}^{k} x^{l}+x^{k} \delta_{\beta}^{l}\right)\right)+24 x_{\eta} x_{\beta} x^{k} x^{l}\right] \partial^{\beta \xi} A^{i j} x^{\eta} x_{\xi} } \\
& =-\frac{\pi^{2}}{2} \partial^{\beta \xi} A^{i j}(0)\left(W_{\xi i j \beta}+W_{\beta i j \xi}\right)
\end{aligned}$$
Exchanging instead $\beta$ and $j$ in (4.32) (except on $A$ ), we got
$$\begin{aligned}
\int_{\mathbb{S}^{3}} W_{k \eta \beta l} & {\left[\delta_{i}^{k} \delta_{j}^{l}+\delta_{j}^{k} \delta_{i}^{l}-4 x_{j}\left(\delta_{i}^{k} x^{l}+x^{k} \delta_{i}^{l}\right)-4\left(\delta_{i j} x^{k} x^{l}+x_{i}\left(\delta_{j}^{k} x^{l}+x^{k} \delta_{j}^{l}\right)\right)+24 x_{i} x_{j} x^{k} x^{l}\right] \partial^{\beta \xi} A^{i j} x^{\eta} x_{\xi} } \\
& =\frac{\pi^{2}}{6} \partial^{\beta \xi} A^{i j}(0)\left(W_{i \xi \beta j}+W_{j \xi \beta i}\right)
\end{aligned}$$
Finally, we also have
$$\begin{gathered}
\sum_{\alpha} \int_{\mathbb{S}^{3}} W_{k i j l}\left[2 \delta_{\alpha}^{k} \delta_{\alpha}^{l}-4 x_{\alpha}\left(\delta_{\alpha}^{k} x^{l}+x^{k} \delta_{\alpha}^{l}\right)-4 x^{k} x^{l}-4 x_{\alpha}\left(\delta_{\alpha}^{k} x^{l}+x^{k} \delta_{\alpha}^{l}\right)+24\left(x_{\alpha}\right)^{2} x^{k} x^{l}\right] \partial^{\beta \xi} A^{i j} x_{\beta} x_{\xi} \\
=-8 \partial^{\beta \xi} A^{i j} W_{k i j l} \int x^{k} x^{l} x_{\beta} x_{\xi}=-\frac{2}{3} \pi^{2} \partial^{\beta \xi} A^{i j}\left(W_{\beta i j \xi}+W_{\xi i j \beta}\right)
\end{gathered}$$
and
$$\begin{gathered}
\sum_{\alpha} \int_{\mathbb{S}^{3}} W_{k i \beta l}\left[2 \delta_{\alpha}^{k} \delta_{\alpha}^{l}-4 x_{\alpha}\left(\delta_{\alpha}^{k} x^{l}+x^{k} \delta_{\alpha}^{l}\right)-4 x^{k} x^{l}-4 x_{\alpha}\left(\delta_{\alpha}^{k} x^{l}+x^{k} \delta_{\alpha}^{l}\right)+24\left(x_{\alpha}\right)^{2} x^{k} x^{l}\right] \partial^{\beta \xi} A^{i j} x_{j} x_{\xi} \\
=-8 \partial^{\beta \xi} A^{i j} W_{k i \beta l} \int x^{k} x^{l} x_{j} x_{\xi}=-\frac{2}{3} \pi^{2} \partial^{\beta \xi} A^{i j}\left(W_{j i \beta \xi}+W_{\xi i \beta j}\right)
\end{gathered}$$

Substituting (4.28), (4.30), (4.31), (4.32), (4.33), (4.34), (4.35) and (4.36) inside (4.27) and using the symmetries of the curvature tensor and the fact that $A$ is symmetric, we get
$$\begin{aligned}
& -\frac{1}{6}\left[\left(\partial^{\eta j} A^{i \beta}(0)+\partial^{i \beta} A^{\eta j}(0)-\partial^{\eta \beta} A^{i j}(0)-\partial^{i j} A^{\eta \beta}(0)\right) \frac{\pi^{2}}{6}\left(W_{\beta i j \eta}+W_{\eta i j \beta}\right)\right] \\
& -\frac{1}{6}\left[-\frac{\pi^{2}}{2} \partial^{\beta \xi} A^{i j}(0)\left(W_{j i \beta \xi}+W_{\xi i \beta j}\right)+\frac{\pi^{2}}{6} \partial^{\beta \xi} A^{i j}(0)\left(W_{i \xi j \beta}+W_{\beta \xi j i}\right)\right] \\
& +\frac{1}{6}\left[-\frac{\pi^{2}}{2} \partial^{\beta \xi} A^{i j}(0)\left(W_{\xi i j \beta}+W_{\beta i j \xi}\right)+\frac{\pi^{2}}{6} \partial^{\beta \xi} A^{i j}(0)\left(W_{i \xi \beta j}+W_{j \xi \beta i}\right)\right] \\
& +\frac{\pi^{2}}{18} \partial^{\beta \xi} A^{i j}(0)\left(W_{\beta i j \xi}+W_{\xi i j \beta}\right)-\frac{\pi^{2}}{18} \partial^{\beta \xi} A^{i j}(0)\left(W_{j i \beta \xi}+W_{\xi i \beta j}\right) \\
& =-\frac{1}{6}\left[\frac{\pi^{2}}{3}\left(\partial^{i \beta} A^{\eta j}(0)-\partial^{\eta \beta} A^{i j}(0)\right)\left(W_{\beta i j \eta}+W_{\eta i j \beta}\right)-\frac{\pi^{2}}{3} \partial^{\beta \xi} A^{i j}(0)\left(W_{\xi i \beta j}+W_{j i \beta \xi}\right)\right] \\
& -\frac{\pi^{2}}{18} \partial^{\beta \xi} A^{i j}(0)\left(W_{\xi i j \beta}+W_{\beta i j \xi}\right)+\frac{\pi^{2}}{18} \partial^{\beta \xi} A^{i j}(0)\left(W_{\beta i j \xi}+W_{\xi i j \beta}\right)-\frac{\pi^{2}}{18} \partial^{\beta \xi} A^{i j}(0)\left(W_{j i \beta \xi}+W_{\xi i \beta j}\right) \\
& =-\frac{\pi^{2}}{18} \partial^{i \beta} A^{\eta j}(0)\left(W_{\beta i j \eta}+W_{\eta i j \beta}\right)+\frac{\pi^{2}}{18} \partial^{\beta \xi} A^{i j}(0)\left(W_{\beta i j \xi}+W_{\xi i j \beta}\right) .
\end{aligned}$$
Finally, using again the symmetries of $W$ and $A$ together with Bianchi identity, we obtain the second term in the RHS of (4.25).

Since the remainder is $O\left(\gamma^{2}\right)$ (see (4.24)), the result follows. \(\square\)

It only remains to compute explicitly the coefficients $\mathcal{C}_{1}$ and $\mathcal{C}_{2}$ appearing in (4.12) and (4.25).
Lemma 4.4. Let $\mathcal{C}_{1}, \mathcal{C}_{2}$ be defined as in (4.19), (4.26) respectively. Then
$$\mathcal{C}_{2}-\mathcal{C}_{1}=\frac{\pi^{2}}{4}\left|W^{M}(p)\right|^{2} .$$
Proof. By definition, we got
$$\begin{aligned}
\left(\mathcal{C}_{2}-\mathcal{C}_{1}\right) \gamma^{-4}= & \frac{1}{2} \int_{\partial B_{\gamma}}\left[\partial_{\eta j}^{2} K_{i \beta}+\partial_{i \beta}^{2} K_{\eta j}-\partial_{\eta \beta}^{2} K_{i j}-\partial_{i j}^{2} K_{\eta \beta}\right] \partial^{\beta} K^{i j} \nu^{\eta} d \sigma \\
& +\frac{1}{4} \int_{\partial B_{\gamma}}\left[\Delta K_{i j} \partial^{\beta} K^{i j} \nu_{\beta}-\Delta K_{i \beta} \partial^{\beta} K^{i j} \nu_{j}\right] d \sigma . \\
& -\frac{1}{4} \int_{\partial B_{\gamma}}\left[\partial_{j} \Delta K_{i \beta}-\partial_{\beta} \Delta K_{i j}\right] K^{i j} \nu^{\beta} d \sigma
\end{aligned}$$

Consider the family of metrics $g_{t}:=g_{E}+t K$. Expanding the Weyl energy of $g_{t}$ at $t=0$ in $\mathbb{R}^{4} \backslash B_{\gamma}(0)$ (as in (4.3), (4.4)), we have
$$\int_{\mathbb{R}^{4} \backslash B_{\gamma}}\left|W^{g_{t}}\right|^{2} d V_{g_{t}}=-2 t^{2} \int_{\mathbb{R}^{4} \backslash B_{\gamma}} \dot{W}_{\alpha i j \beta} \partial^{\alpha} \partial^{\beta} K^{i j} d x+O\left(t^{3}\right), \quad \text { as } t \rightarrow 0$$
By looking at the definition of $K$ (4.9) and the formula for the linearized Weyl tensor (4.7), we notice that all the integrands on the RHS decay as $|x|^{-8}$ as $|x| \rightarrow \infty$, therefore we can integrate by parts twice as in (4.5). Recalling further that $K$ is TT and biharmonic (so in the kernel of the linearized Weyl at $g_{E}$ ), as in (4.6) we get
$$\int_{\mathbb{R}^{4} \backslash B_{\gamma}}\left|W^{g_{t}}\right|^{2} d V_{g_{t}}=2 t^{2}\left(\int_{\partial B_{\gamma}} \dot{W}_{\eta i j \beta} \partial^{\beta} K^{i j} \nu^{\eta} d \sigma-\int_{\partial B_{\gamma}} \partial^{\alpha} \dot{W}_{\alpha i j \eta} K^{i j} \nu^{\eta} d \sigma\right)+O\left(t^{3}\right),$$
where $\nu=x /|x|$ points toward the interior of $\mathbb{R}^{4} \backslash B_{\gamma}$. But now, using again (4.7) we see that indeed
$$\int_{\mathbb{R}^{4} \backslash B_{\gamma}}\left|W^{g_{t}}\right|^{2} d V_{g_{t}}=2 \frac{t^{2}}{\gamma^{4}}\left(\mathcal{C}_{2}-\mathcal{C}_{1}\right)+O\left(t^{3}\right)$$

Let us define
$$g(x)=\left(\delta_{i j}-\frac{1}{3} W_{k i j l} x^{k} x^{l}\right) d x^{i} d x^{j} .$$
If we let $y:=I(x)=x /|x|^{2}$, then
$$\tilde{g}(y):=I^{*}\left(|x|^{-4} g\right)(y)=\left(\delta_{i j}-\frac{1}{3} W_{k i j l} \frac{y^{k} y^{l}}{|y|^{4}}\right) d y^{i} d y^{j}$$
and therefore $t \tilde{g}=g_{t}$. Hence
$$\int_{\mathbb{R}^{4} \backslash B_{\gamma}}\left|W^{g_{t}}\right|^{2} d V_{g_{t}}=\int_{\mathbb{R}^{4} \backslash B_{\gamma / \sqrt{t}}}\left|W^{\tilde{g}}\right|^{2} d V_{\tilde{g}}=\int_{B_{\sqrt{t} / \gamma}}\left|W^{g}\right|^{2} d V_{g}=\frac{\pi^{2}}{2} \frac{t^{2}}{\gamma^{4}}\left|W^{M}(p)\right|^{2}+O\left(\frac{t^{3}}{\gamma^{6}}\right)$$
The result then follows from (4.37) and (4.38). \(\square\)

As a consequence of (4.6), Lemma 4.1 and Lemma 4.3 and Lemma 4.4, we obtain the expansion for the Weyl energy on $Z$ :

Corollary 4.5. Let $g_{b}$ be defined as in (4.1). Then
$$\mathcal{W}_{\gamma}^{Z}\left(g_{b}\right)=\int_{Z \backslash B_{\gamma}^{g_{Z}}(q)}\left|W^{g_{b}}\right|^{2} d V_{g_{b}}=\frac{\pi^{2}}{2} \frac{b^{4}}{\gamma^{4}}\left|W^{M}(p)\right|^{2}+O\left(b^{4} \gamma^{2}\right), \quad \text { as } 0 \ll b \ll \gamma \ll 1$$

\section*{5 Weyl energy of the perturbed non LCF metric}

On the Bach-flat manifold $\left(M, g_{M}\right)$, we want to adjust the metric in order to match its inverted and scaled counterpart to the modified metric $g_{b}$ on $Z$ (defined by (4.1)). The idea is that, since $A(0)=0$ and $\nabla A(0)=0$ (see (3.21), (3.38)), we want to add a perturbation to $g_{M}$ to match $\nabla_{k l}^{2} A_{i j}(0) x^{k} x^{l}$.

In conformal normal coordinates at $p \in M$, there exists $\varepsilon>0$ (small) such that
$$g_{M}=\left(\delta_{i j}-\frac{1}{3} W_{k i j l} z^{k} z^{l}+\zeta_{i j}(z)\right) d z^{i} d z^{j}, \quad|z|<4 \varepsilon,$$
where $\zeta_{i j}(z)=O^{(4)}(|z|)^{3}$ as $|z| \rightarrow 0$. Let us consider a smooth cutoff function $\phi$ satisfying $0 \leq \phi(r) \leq 1$ $\forall r \geq 0, \varphi(r) \equiv 0$ for $r \geq 2 \varepsilon$ and $\phi(r) \equiv 1$ for $r \leq \varepsilon$. We define a smooth tensor $H$ in $M \backslash\{p\}$ as
$$H_{i j}(z):=\frac{1}{2} \partial_{k l}^{2} A_{i j}(0) \frac{z^{k} z^{l}}{|z|^{4}} \phi(|z|)=: T_{k i j l} \frac{z^{k} z^{l}}{|z|^{4}} \phi(|z|), \quad \text { for }|z| \leq 4 \varepsilon,$$
with $H \equiv 0$ in $M \backslash B_{2 \varepsilon}^{g_{M}}(p)$. Letting $\tilde{g}_{M}:=g_{M}+a^{4} H$, one has
$$\tilde{g}_{M}=\left(\delta_{i j}-\frac{1}{3} W_{k i j l} z^{k} z^{l}+a^{4} T_{k i j l} \frac{z^{k} z^{l}}{|z|^{4}}+\zeta_{i j}(z)\right) d z^{i} d z^{j}, \quad|z|<\varepsilon$$
If we now multiply the metric $\tilde{g}_{M}$ via a positive function $f$ on $M \backslash\{p\}$, satisfying $f(z)=|z|^{-2}$ near $p$, and call $y=z /|z|^{2}$ the inverted conformal normal coordinates, by Lemma 2.2 we get
$$f^{2} \tilde{g}_{M}=: \tilde{g}_{N}=\left(\delta_{i j}-\frac{1}{3} W_{k i j l} \frac{y^{k} y^{l}}{|y|^{4}}+a^{4} T_{k i j l} y^{k} y^{l}+\tilde{\zeta}_{i j}(y)\right) d y^{i} d y^{j}, \quad|y|>\frac{1}{\varepsilon},$$
where $\tilde{\zeta}_{i j}(y)=O^{(4)}\left(|y|^{-3}\right)$ as $|y| \rightarrow+\infty$. Letting now $g_{a}:=a^{2} \tilde{g}_{N}$, then $x:=a y$ are the inverted normal coordinates for $g_{a}$ and one has
$$g_{a}=\left(\delta_{i j}-\frac{1}{3} a^{2} W_{k i j l} \frac{x^{k} x^{l}}{|x|^{4}}+a^{2} T_{k i j l} x^{k} x^{l}+\zeta_{i j}^{a}(x)\right) d x^{i} d x^{j}, \quad|x|>\frac{a}{\varepsilon},$$
where now $\zeta^{a}$ satisfies
$$\left|\nabla^{k} \zeta_{i j}^{a}(x)\right| \leq C a^{3}|x|^{-3-k}, \quad \text { for }|x|>\frac{a}{\varepsilon}, k=0, \ldots, 4 .$$

From (5.2), (4.1), (5.1) and (3.24) we see that, letting $a=b$ we can match $g_{a}^{M}$ and $g_{b}^{Z}$ in a very precise way (see Section 6.1 for the explicit construction).

We now want to compute the Weyl energy of the modified metric $g_{a}$ defined in (5.2). If we glue $\left(N=M \backslash\{p\}, g_{a}\right)$ to $\left(Z, g_{b}\right)$ at scale $\gamma$ (with $a=b \ll \gamma \ll 1$ ), then, being $\gamma=|x|=a|z|^{-1}$, we got $|z|=a \gamma^{-1}$ and therefore, using the pointwise conformal invariance of $\left|W^{g}\right|^{2} d V_{g}$, we need to compute
$$\int_{M \backslash B_{a \gamma^{-1}}^{g_{M}}(p)}\left|W^{\tilde{g}_{M}}\right|^{2} d V_{\tilde{g}_{M}}$$
Recalling the definition of $\tilde{g}_{M}$, we let $t:=a^{4}$ and employ the notation
$$\tilde{g}_{M}=g_{t}:=g_{M}+t H, \quad V(t):=\int_{M \backslash B_{t^{1 / 4} \gamma^{-1}}^{g_{M}}(p)}\left|W^{g_{t}}\right|^{2} d V_{g_{t}} .$$
We would now like to Taylor-expand $V$ at 0 , obtaining
$$V(t)=\mathcal{W}^{M}\left(g_{M}\right)+\left.t \frac{d}{d t}\right|_{t=0} V(t)+o(t) .$$
However, it is not immediately clear whether $V$ and $V^{\prime}$ are continuous up to zero.
Lemma 5.1. $V$ is continuous up to zero and $V(0)=\mathcal{W}^{M}\left(g_{M}\right)$.
Proof. By definition of $g_{t}$, for $|z|$ close to 0 we got
$$g_{t}=g_{M}+t O\left(|z|^{-2}\right), \quad \nabla g_{t}=\nabla g_{M}+t O\left(|z|^{-3}\right), \quad \nabla^{2} g_{t}=\nabla^{2} g_{M}+t O\left(|z|^{-4}\right),$$
where ∇ denotes the Euclidean gradient (w.r.t. the coordinates $z$ ). Moreover, for $a=t^{1 / 4}<|z|<\varepsilon$, the metric $g_{t}^{-1}$ has the following expansion:
$$g_{t}^{-1}=\left(\delta_{i j}+\frac{1}{3} W_{k i j l} z^{k} z^{l}-a^{4} T_{k i j l} \frac{z^{k} z^{l}}{|z|^{4}}+O^{(3)}\left(|z|^{3}\right)\right) d z^{i} d z^{j}, \quad a=t^{1 / 4}<|z|<\varepsilon,$$
so one also has
$$g_{t}^{-1}=g_{M}^{-1}+t O\left(|z|^{-2}\right), \quad \nabla g_{t}^{-1}=\nabla g_{M}^{-1}+t O\left(|z|^{-3}\right), \quad t^{1 / 4}<|z|<\varepsilon .$$
Notice that here the error terms do not depend on $t$ (but the range of $|z|$ in which the expansion holds does). Now, the Weyl tensor contains up to second order derivatives of the metric, and, if we look closely at $\left|W^{g_{t}}\right|^{2}$, we see that it has (at worst) additional terms given by perturbations of order $\approx t^{2}|z|^{-8}+t|z|^{-4}$. In other words,
$$\left|W^{g_{t}}\right|_{g_{t}}^{2}=\left|W^{g_{M}}\right|_{g_{M}}^{2}+t^{2} O\left(|z|^{-8}\right)+t O\left(|z|^{-4}\right), \quad t^{1 / 4}<|z|<\varepsilon .$$
But now
$$\int_{B_{\varepsilon} \backslash B_{t^{1 / 4} \gamma^{-1}}}\left(t^{2}|z|^{-8}+t|z|^{-4}\right) d z \approx t \int_{t^{1 / 4} \gamma^{-1}}^{\varepsilon} r^{-1} d r=O(t(\log t)) \quad \text { as } t \rightarrow 0^{+}$$
which implies that $V(t) \rightarrow V(0)=\int_{M}\left|W^{g_{M}}\right|^{2} d V_{g_{M}}=\mathcal{W}^{M}\left(g_{M}\right)$ as $t \rightarrow 0^{+}$(the error given by the perturbation vanishes in the limit). \(\square\)

Lemma 5.2. $V$ is differentiable at 0 and one has
$$V^{\prime}(0)=-\frac{\pi^{2}}{2} \gamma^{-4}\left|W^{M}(p)\right|^{2}+\frac{4}{3} W_{k i j l}^{M} T^{k i j l}+O\left(\gamma^{4}\right) .$$
Proof. In order to compute $V^{\prime}(0)$, we first compute $V^{\prime}(s)$ for $s>0$ and then take the limit as $s \rightarrow 0^{+}$. Using the chain rule, one has
$$\left.V^{\prime}(s)=-4 \int_{M \backslash B_{s^{1 / 4} \gamma^{-1}}^{g_{M}}}\left(W_{\alpha i j \beta}^{g_{s}} \nabla^{\alpha} \nabla^{\beta} H^{i j}+\frac{1}{2} R_{g_{s}}^{\alpha \beta} W_{\alpha i j \beta}^{g_{s}} H^{i j}\right) d V_{g_{s}}-\int_{\partial B_{s^{1 / 4} \gamma^{-1}}^{g_{M}}}\left|W^{g_{s}}\right|^{2} \frac{1}{4 \gamma s^{3 / 4}} d \phi_{s_{s}} \cdot 10\right)$$
We now claim that, up to a (small) error term, it is possible to substitute $g_{s}=g_{M}+s H$ by $g_{M}$ in the above expression. Indeed, consider for instance the first term of the first integral. Then, recalling (5.6), (5.7) and the formula for Weyl's tensor in local coordinates (2.1), one sees that
$$\begin{aligned}
& \left|\int_{M \backslash B_{s^{1 / 4} \gamma^{-1}}^{g_{M}}} W_{\alpha i j \beta}^{g_{s}} \nabla^{\alpha} \nabla^{\beta} H^{i j} d V_{g_{s}}-\int_{M \backslash B_{s^{1 / 4} \gamma^{-1}}^{g_{M}}} W_{\alpha i j \beta}^{g_{M}} \nabla^{\alpha} \nabla^{\beta} H^{i j} d V_{g_{M}}\right| \\
& \quad \leq C s+C \int_{B_{\varepsilon} \backslash B_{s^{1 / 4} \gamma^{-1}}^{g_{M}}} s\left(|z|^{-2}+|z|^{-3}+|z|^{-4}\right)|z|^{-4} d V_{g_{M}} \leq C s+C \gamma^{4},
\end{aligned}$$
where we also used that $d V_{g_{s}}=d V_{g_{M}}+O\left(s^{1 / 4}\right) d x$. Arguing in the same way, we also see that the second term of the first integral generates an error of order $\sqrt{s}$. As for the last integral in (5.10), using (5.8) we only obtain
$$\int_{\partial B_{s^{1 / 4} \gamma^{-1}}^{g_{M}}}\left|W^{g_{s}}\right|^{2} \frac{1}{4 \gamma s^{3 / 4}} d \sigma_{g_{s}}=\int_{\partial B_{s^{1 / 4} \gamma^{-1}}^{g_{M}}}\left|W^{g_{M}}\right|^{2} \frac{1}{4 \gamma s^{3 / 4}} d \sigma_{g_{M}}+O(1),$$
so we actually need to be more precise. Since $d \sigma_{g_{s}}=d \sigma_{g_{M}}+O\left(s^{1 / 4}\right) d \sigma_{\mathbb{S}^{3}}$, we focus only on the squared norm of the Weyl tensor. Being $\gamma \ll 1$, we can Taylor-expand this quantity in $\partial B_{s^{1 / 4} \gamma^{-1}}^{g_{M}}$ and obtain
$$\left|W^{g_{s}}\right|^{2}=\left|W^{g_{M}}\right|^{2}+\underbrace{s\left[-4\left(W_{\alpha i j \beta}^{g_{M}} \nabla^{\alpha} \nabla^{\beta} H^{i j}+\frac{1}{2} R_{g_{M}}^{\alpha \beta} W_{\alpha i j \beta}^{g_{M}} H^{i j}\right)-\frac{1}{2}\left|W^{g_{M}}\right|^{2} g_{M}^{i j} H_{i j}\right]}_{=O\left(\gamma^{4}\right)}+O\left(\gamma^{8}\right) .$$
Then, since $\left|\nabla^{2} H_{i j}\right|=O\left(|z|^{-4}\right)$, one has
$$\int_{\partial B_{s^{1 / 4} \gamma^{-1}}^{g_{M}}}\left|W^{g_{s}}\right|^{2} d \sigma_{g_{s}}=\int_{\partial B_{s^{1 / 4} \gamma^{-1}}^{g_{M}}}\left|W^{g_{M}}\right|^{2} d \sigma_{g_{M}}-4 s \int_{\partial B_{s^{1 / 4} \gamma^{-1}}^{g_{M}}} W_{\alpha i j \beta}^{g_{M}} \nabla^{\alpha} \nabla^{\beta} H^{i j} d \sigma_{g_{M}}+O\left(\gamma^{5} s^{3 / 4}\right)$$
From this formula and a change of variables, it follows that
$$\frac{1}{4 \gamma s^{3 / 4}} \int_{\partial B_{s^{1 / 4} \gamma^{-1}}^{g_{M}}}\left|W^{g_{s}}\right|^{2} d \sigma_{g_{s}}=\frac{\pi^{2}}{2} \gamma^{-4}\left|W^{g_{M}}(p)\right|^{2}-\int_{\mathbb{S}^{3}} W_{\alpha i j \beta}^{g_{M}}(p) \partial^{\alpha} \partial^{\beta} \tilde{H}^{i j} d \sigma+O\left(\gamma^{4}\right)+O\left(s^{1 / 4} \gamma^{\left.\left(5^{1} \cdot\right) 2\right)}\right.$$
where $\tilde{H}_{i j}(x):=T_{k i j l} x^{k} x^{l}|x|^{-4}$. But now, on $\mathbb{S}^{3}$,
$$\partial_{\alpha \beta}^{2} \tilde{H}_{i j}(x)=T_{k i j l}\left[\delta_{\alpha}^{k} \delta_{\beta}^{l}+\delta_{\beta}^{k} \delta_{\alpha}^{l}-4 x_{\beta}\left(\delta_{\alpha}^{k} x^{l}+x^{k} \delta_{\alpha}^{l}\right)-4\left(\delta_{\alpha \beta} x^{k} x^{l}+x_{\alpha}\left(\delta_{\beta}^{k} x^{l}+x^{k} \delta_{\beta}^{l}\right)\right)+24 x_{\alpha} x_{\beta} x^{k} x^{l}\right],$$
so
$$\begin{aligned}
\int_{\mathbb{S}^{3}} W_{g_{M}}^{\alpha i j \beta}(p) \partial_{\alpha} \partial_{\beta} \tilde{H}_{i j} d \sigma= & -W_{g_{M}}^{\alpha i j \beta} \int_{\mathbb{S}^{3}}\left[\left(T_{\alpha i j \beta}+T_{\beta i j \alpha}\right)-4\left(T_{\alpha i j k}+T_{k i j \alpha}\right) x_{\beta} x^{k}\right. \\
& \left.-4\left(T_{\beta i j k}+T_{k i j \beta}\right) x_{\alpha} x^{k}+24 T_{k i j l} x_{\alpha} x_{\beta} x^{k} x^{l}\right] d \sigma \\
= & -W_{g_{M}}^{\alpha i j \beta}\left(2 \pi^{2}-2 \pi^{2}-2 \pi^{2}+2 \pi^{2}\right)\left(T_{\alpha i j \beta}+T_{\beta i j \alpha}\right)=0,
\end{aligned}$$
where the last identity follows from (4.29) and (4.20). Substituting (5.11), (5.12) and (5.13) into (5.10), we finally obtain
$$\begin{gathered}
V^{\prime}(s)=-4 \int_{M \backslash B_{s^{1 / 4} \gamma^{-1}}^{g_{M}}}\left(W_{\alpha i j \beta}^{g_{M}} \nabla^{\alpha} \nabla^{\beta} H^{i j}+\frac{1}{2} R_{g_{M}}^{\alpha \beta} W_{\alpha i j \beta}^{g_{M}} H^{i j}\right) d V_{g_{M}} \\
-\frac{\pi^{2}}{2} \gamma^{-4}\left|W^{M}(p)\right|^{2}+O\left(\gamma^{4}\right)+O\left(s^{1 / 4} \gamma^{-1}\right) .
\end{gathered}$$
Integrating by parts twice and using that $g_{M}$ is Bach-flat, we further have
$$\begin{gathered}
V^{\prime}(s)=4 \int_{\partial B_{s^{1 / 4} \gamma^{-1}}^{g_{M}}} W_{n i j \beta}^{g_{M}} \nabla^{\beta} H^{i j} d \sigma_{g_{M}}-4 \int_{\partial B_{s^{1 / 4} \gamma^{-1}}^{g_{M}}} \nabla^{\beta} W_{n i j \beta}^{g_{M}} H^{i j} d \sigma_{g_{M}} \\
-\frac{\pi^{2}}{2} \gamma^{-4}\left|W^{M}(p)\right|^{2}+O\left(\gamma^{4}\right)+O\left(s^{1 / 4} \gamma^{-1}\right),
\end{gathered}$$
where here $n$ denotes the normal direction pointing towards the exterior of the ball. But now the second integral is an $O\left(s^{1 / 4} \gamma^{-1}\right)$, while, after scaling, the first integral satisfies
$$\begin{aligned}
\int_{\partial B_{s^{1 / 4} \gamma^{-1}}^{g_{M}}} W_{n i j \beta}^{g_{M}} \nabla^{\beta} H^{i j} d \sigma_{g_{M}} & =W_{\alpha i j \beta}^{M}(p) T^{k i j l} \int_{\mathbb{S}^{3}}\left(\delta_{k}^{\beta} x_{l}+x_{k} \delta_{l}^{\beta}-4 x^{\beta} x_{k} x_{l}\right) x^{\alpha} d \sigma_{\mathbb{S}^{3}}+O\left(s^{1 / 4} \gamma^{-1}\right) \\
& =W_{\alpha i j \beta}^{M}(p) \int_{\mathbb{S}^{3}}\left[\left(T^{\beta i j k}+T^{k i j \beta}\right) x^{\alpha} x_{k}-4 T^{k i j l} x^{\alpha} x^{\beta} x_{k} x_{l}\right] d \sigma_{\mathbb{S}^{3}}+O\left(s^{1 / 4} \gamma^{-1}\right) \\
& =W_{\alpha i j \beta}^{M}\left(\frac{\pi^{2}}{2}-\frac{\pi^{2}}{3}\right)\left(T^{\alpha i j \beta}+T^{\beta i j \alpha}\right)+O\left(s^{1 / 4} \gamma^{-1}\right) \\
& =\frac{\pi^{2}}{3} W_{\alpha i j \beta}^{M} T^{\alpha i j \beta}+O\left(s^{1 / 4} \gamma^{-1}\right),
\end{aligned}$$
where we used (4.29), (4.20) and the symmetry of $T$ in $\alpha, \beta$. Substituting inside the formula for $V^{\prime}(s)$ and taking the limit as $s \rightarrow 0^{+}$, we finally obtain (5.9). \(\square\)

By looking at (5.4), (5.5), (5.9) and recalling that $t=a^{4}$, we obtain the following:
Corollary 5.3. Let $g_{a}$ be given by (5.2) (in particular $W=W^{M}(p)$ and $T_{\text {kijl }}=\frac{1}{2} \partial_{k l}^{2} A_{i j}(0)$ ). Then
$$\int_{M \backslash B_{a \gamma^{-1}}^{g_{M}}(p)}\left|W^{\tilde{g}_{M}}\right|^{2} d V_{\tilde{g}_{M}}=\mathcal{W}^{M}\left(g_{M}\right)-\frac{\pi^{2}}{2} \frac{a^{4}}{\gamma^{4}}\left|W^{M}(p)\right|^{2}+\frac{4}{3} a^{4} W^{k i j l} T_{k i j l}+O\left(a^{4} \gamma^{4}\right)+o\left(a^{4}\right),$$
provided $0 \ll a \ll \gamma \ll 1$.
Remark 5.4. The approach adopted here is not the only viable one. Indeed, it is also possible to directly add a quadratic correction to the (scaled and) inverted metric directly in order to obtain an expansion as in (5.2). In this way, it is no longer necessary to project the hessian on its "curvature part" using Lemma 2.1 (as done in Section 3). However, we would then get additional terms when considering the correction in normal coordinates on $M$ during the proof of Lemma 5.2, which would make the above computations significantly more involved.

\section*{6 Conclusion of the proofs}

After having constructed the metric corrections $g_{a}$ on $M$ (see (5.2)) and $g_{b}$ on $Z$ (see (4.1)) and having estimated their Weyl energies in Corollary 5.3 and Corollary 4.5 respectively, we are now in position to define a competitor metric $g_{X}$ on the connected sum $Z \# \bar{M}$ and compute its Weyl energy. As we
will see in Proposition 6.2, the difference between the Weyl energy of $g_{X}$ and that of $g_{M}$ will depend upon the interaction term (3.22), which can be shown to have the right sign (i.e. to be negative) after a proper choice of coordinates on $M$, see Lemma 6.4. This will allow us to prove Theorem 1.1 in this setting, that is, for $Z$ diffeomorphic to a finite quotient of $\mathbb{S}^{1} \times \mathbb{S}^{3}$. Then, in Proposition 6.7 we will deal with the general case in which $Z$ is a connected sum of quotients as in Theorem 3.1. Finally, we will show how to extend the result to the orbifold setting and prove Theorem 1.4.

\subsection*{6.1 Definition and expansion of the metric on the connected sum}

We start by defining the connected sum between $Z$ and $M$. Let $\left\{x^{i}\right\}$ denote normal (flat) coordinates for $g_{Z}$ at $q \in Z$, defined for $|x|<\delta$. With a slight abuse of notation, let us also denote by $\left\{x^{i}\right\}$ the inverted normal coordinates for $g_{a}$ defined at the beginning of Section 5, which are defined for $|x|>a / \varepsilon$. As in the previous section, let us consider $\gamma>0$ satisfying $0<a \ll \gamma \ll \varepsilon, \delta \ll 1$. We now glue $M$ and $Z$ along the annular regions $\{x|\gamma / 2<|x|<2 \gamma\}$ (of both $M$ and $Z$, given by their respective coordinates) via the identification map $x \rightarrow x$. We denote by $X$ the resulting smooth manifold.
Remark 6.1. By construction, $X$ is diffeomorphic to $Z \# \bar{M}$, where $\bar{M}$ denotes the manifold $M$ endowed with its opposite orientation. This is the same choice adopted in [MM25], see Remark 3.5, as well as in [GV16], see their Remark 9.1. This does not create any problem, since we can easily get a manifold diffeomorphic to $Z \# M$ by simply repeating the same procedure with $\bar{M}$ in place of $M$.

We now want to define a competitor metric $g_{X}$ on $X$. To begin, recall the expressions (4.1) for $g_{b}$ in normal (flat) coordinates at $q \in Z$ and (5.2) for $g_{a}$ in inverted conformal normal coordinates at $p \in M$. We would like to glue these metrics at $|x|=\gamma$, but in order to do so we first need to cut off some higher order error terms.

Since we got $A(0)=0, \nabla A(0)=0$ (see e.g. (3.21)), we can write
$$A_{i j}(x)=\frac{1}{2} \partial_{k l}^{2} A_{i j}(0) x^{k} x^{l}+\eta_{i j}(x), \quad \text { for }|x|<\delta,$$
where
$$\left|\nabla^{k} \eta_{i j}(x)\right| \leq C|x|^{3-k}, \quad \text { for }|x| \leq \delta, k=0, \ldots, 4 .$$
Let us define a smooth cutoff function $\chi_{\gamma}$ satisfying
$$\chi_{\gamma}(r)=\left\{\begin{array}{ll}
0 & \text { for } r \leq \frac{\gamma}{4} \\
1 & \text { for } r \geq \frac{3}{4} \gamma,
\end{array} \quad\left|\left(\chi_{\gamma}\right)^{(k)}\right| \leq C \gamma^{-k}, \quad k=0, \ldots, 4,\right.$$
where $C>0$ does not depend upon $\gamma$. We now define the modified metric $\tilde{g}_{a}$ on $M \backslash\{p\}$ by
$$\left(\tilde{g}_{a}\right)_{i j}(x):=\delta_{i j}+a^{2}\left(-\frac{1}{3} W_{k i j l} \frac{x^{k} x^{l}}{|x|^{4}}+\frac{1}{2} \partial_{k l}^{2} A_{i j}(0) x^{k} x^{l}\right)+\chi_{\gamma}(\gamma-|x|) \zeta_{i j}^{a}(x), \quad \text { for }|x|>\frac{a}{\varepsilon},$$
with $\tilde{g}_{a}=g_{a}$ elsewhere on $M \backslash\{p\}$. Similarly, we define the modified metric $\hat{g}_{b}$ on $Z$ by
$$\left(\hat{g}_{b}\right)_{i j}(x):=\delta_{i j}+b^{2}\left(-\frac{1}{3} W_{k i j l} \frac{x^{k} x^{l}}{|x|^{4}}+\frac{1}{2} \partial_{k l}^{2} A_{i j}(0) x^{k} x^{l}+\chi_{\gamma}(|x|-\gamma) \eta_{i j}(x)\right), \quad \text { for }|x|<\delta,$$
with $\hat{g}_{b}=g_{b}$ elsewhere on $Z$. We now take $a=b$ and define
$$g_{X}:= \begin{cases}g_{a} & \text { in } M \backslash\{x| | x \mid>2 a / \varepsilon\} \\ \tilde{g}_{a} & \text { in }\{x|2 a / \varepsilon<|x|<\gamma\} \\ \hat{g}_{b} & \text { in }\{x|\gamma \leq|x| \leq \delta / 2\} \\ g_{b} & \text { in } Z \backslash\{x| | x \mid \leq \delta / 2\} .\end{cases}$$
By definition, $g_{X}$ is a smooth metric on $X$.

Proposition 6.2. Let $g_{X}$ be defined as in (6.5), and assume that $0<a=b \ll \gamma \ll \varepsilon, \delta \ll 1$. Then the following expansion holds:
$$\mathcal{W}^{X}\left(g_{X}\right)-\mathcal{W}^{M}\left(g_{M}\right)=\frac{2}{3} a^{4} W^{k i j l} \partial_{k l}^{2} A_{i j}(0)+O\left(a^{4} \gamma\right)+o\left(a^{4}\right) .$$
Proof. By Corollary 4.5, Corollary 5.3 and the definition of $g_{X}$, we see that
$$\begin{aligned}
\mathcal{W}^{X}\left(g_{X}\right)-\mathcal{W}^{M}\left(g_{M}\right)= & \frac{2}{3} a^{4} W^{k i j l} \partial_{k l}^{2} A_{i j}(0)+O\left(a^{4} \gamma^{2}\right)+o\left(a^{4}\right) \\
& +\int_{B_{2 \gamma} \backslash B_{\gamma / 8}}\left|W^{g_{X}}\right|^{2} d V_{g_{X}}-\int_{B_{2 \gamma} \backslash B_{\gamma}}\left|W^{g_{b}}\right|^{2} d V_{g_{b}}-\int_{B_{\gamma} \backslash B_{\gamma / 8}}\left|W^{g_{a}}\right|^{2} d V_{g_{a}} .
\end{aligned}$$
The proposition then follows from the next lemma. \(\square\)

Lemma 6.3. Under the assumptions of Proposition 6.2 (in particular $b=a$ ), one has
$$\int_{B_{2 \gamma} \backslash B_{\gamma / 8}}\left|W^{g_{X}}\right|^{2} d V_{g_{X}}-\int_{B_{2 \gamma} \backslash B_{\gamma}}\left|W^{g_{b}}\right|^{2} d V_{g_{b}}-\int_{B_{\gamma} \backslash B_{\gamma / 8}}\left|W^{g_{a}}\right|^{2} d V_{g_{a}}=O\left(a^{4} \gamma\right) .$$
Proof. We deal separately with the integrals in $B_{2 \gamma} \backslash B_{\gamma}$ and those in $B_{\gamma} \backslash B_{\gamma / 8}$.
\begin{itemize}
\item[-] Consider
$$\int_{B_{2 \gamma} \backslash B_{\gamma}}\left|W^{g_{X}}\right|^{2} d V_{g_{X}}-\int_{B_{2 \gamma} \backslash B_{\gamma}}\left|W^{g_{b}}\right|^{2} d V_{g_{b}}=\int_{B_{2 \gamma} \backslash B_{\gamma}}\left|W^{\hat{g}_{b}}\right|^{2} d V_{\hat{g}_{b}}-\int_{B_{2 \gamma} \backslash B_{\gamma}}\left|W^{g_{b}}\right|^{2} d V_{g_{b}}$$
\end{itemize}
and let us write $g_{b}=g_{E}+b^{2} F$ and $\hat{g}_{b}=g_{E}+b^{2} \hat{F}$, where we recall that $\hat{g}_{b}$ is given by (6.4). Since $b=a \ll \gamma$, we can Taylor-expand the Weyl energies in $b$ at $g_{E}$ as in the beginning of Section 4. Recalling that $\dot{B}(F)=0$, expanding and integrating by parts we obtain
$$\begin{aligned}
\int_{B_{2 \gamma} \backslash B_{\gamma}}\left|W^{g_{b}}\right|^{2} d V_{g_{b}} & =-2 a^{4} \int_{B_{2 \gamma} \backslash B_{\gamma}} \dot{W}(F)_{\alpha i j \beta} \partial^{\alpha} \partial^{\beta} F^{i j} d x+O\left(a^{6}\right) \\
& =2 a^{4} \int_{\partial\left(B_{2 \gamma} \backslash B_{\gamma}\right)}\left(\partial^{\alpha} \dot{W}(F)_{\alpha i j \eta} F^{i j}-\dot{W}(F)_{\eta i j \beta} \partial^{\beta} F^{i j}\right) \nu^{\eta} d \sigma+O\left(a^{6}\right),
\end{aligned}$$
where this time $\nu$ is the exterior unit normal vector. Similarly,
$$\begin{aligned}
\int_{B_{2 \gamma} \backslash B_{\gamma}}\left|W^{\hat{g}_{b}}\right|^{2} d V_{\hat{g}_{b}}= & -2 a^{4} \int_{B_{2 \gamma} \backslash B_{\gamma}} \dot{B}_{i j}(\hat{F}) \hat{F}^{i j} d x \\
& +2 a^{4} \int_{\partial\left(B_{2 \gamma} \backslash B_{\gamma}\right)}\left(\partial^{\alpha} \dot{W}(\hat{F})_{\alpha i j \eta} \hat{F}^{i j}-\dot{W}(\hat{F})_{\eta i j \beta} \partial^{\beta} \hat{F}^{i j}\right) \nu^{\eta} d \sigma+O\left(a^{6}\right)
\end{aligned}$$
We now decompose
$$\hat{F}_{i j}(x)=F_{i j}(x)-\left(1-\chi_{\gamma}(|x|-\gamma)\right) \eta_{i j}(x)=: F_{i j}(x)+E_{i j}(x),$$
so that
$$\dot{B}_{i j}(\hat{F}) \hat{F}^{i j}=\dot{B}_{i j}(E) \hat{F}^{i j} .$$
Recalling that $\dot{B}$ is a linear fourth-order operator, from the definition of $E$ and $\hat{F}$ (that depend upon $\eta, \chi_{\gamma}$ defined in (6.1), (6.2)), we see that
$$\left|\hat{F}^{i j}(x)\right| \leq C|x|^{-2}, \quad\left|\dot{B}_{i j}(E)\right| \leq C \gamma^{-1}, \quad \text { for } \gamma \leq|x| \leq 2 \gamma .$$

As a consequence,
$$\left|\int_{B_{2 \gamma} \backslash B_{\gamma}} \dot{B}_{i j}(\hat{F}) \hat{F}^{i j} d x\right|=\left|\int_{B_{2 \gamma} \backslash B_{\gamma}} \dot{B}_{i j}(E) \hat{F}^{i j} d x\right| \leq C \gamma .$$
Next, we look at the boundary integrals in (6.7), (6.8). To begin, we notice that $F^{i j}=\hat{F}^{i j}$ near $\partial B_{2 \gamma}$, so the integrals in the outer boundary $\partial B_{2 \gamma}$ cancel out when taking the difference in (6.6). Thus it only remains to estimate the integrals on $\partial B_{\gamma}$.

By linearity, $\dot{W}(\hat{F})_{\alpha i j \beta}=\dot{W}(F)_{\alpha i j \beta}+\dot{W}(E)_{\alpha i j \beta}$; moreover, again by (6.1), (6.2), we get the following estimates at scale $|x|=\gamma$ :
$$\left|\dot{W}_{\alpha i j \beta}(E)\right| \leq C \gamma, \quad\left|\partial^{\alpha} \dot{W}_{\alpha i j \eta}(E)\right| \leq C, \quad\left|E^{i j}\right| \leq C \gamma^{3}, \quad\left|\partial^{\beta} E^{i j}\right| \leq C \gamma^{2} .$$
Using these, we readily obtain
$$\begin{aligned}
\mid \int_{\partial B_{\gamma}}\left(\dot{W}(\hat{F})_{\eta i j \beta}\right. & \left.\partial^{\beta} \hat{F}^{i j}-\dot{W}(F)_{\eta i j \beta} \partial^{\beta} F^{i j}\right) \nu^{\eta} d \sigma \mid \\
= & \left|\int_{\partial B_{\gamma}}\left(\dot{W}(F)_{\eta i j \beta} \partial^{\beta} E^{i j}+\dot{W}(E)_{\eta i j \beta} \partial^{\beta} \hat{F}^{i j}\right) \nu^{\eta} d \sigma\right| \leq C \gamma,
\end{aligned}$$
and
$$\begin{aligned}
\mid \int_{\partial B_{\gamma}}\left(\partial^{\alpha} \dot{W}(\hat{F})_{\alpha i j \eta}\right. & \left.\hat{F}^{i j}-\partial^{\alpha} \dot{W}(F)_{\alpha i j \eta} F^{i j}\right) \nu^{\eta} d \sigma \mid \\
= & \left|\int_{\partial B_{\gamma}}\left(\partial^{\alpha} \dot{W}(F)_{\alpha i j \eta} E^{i j}+\partial^{\alpha} \dot{W}(E)_{\alpha i j \eta} \hat{F}^{i j}\right) \nu^{\eta} d \sigma\right| \leq C \gamma .
\end{aligned}$$
Using these estimates and (6.9) in (6.6), we obtain
$$\int_{B_{2 \gamma} \backslash B_{\gamma}}\left|W^{g_{X}}\right|^{2} d V_{g_{X}}-\int_{B_{2 \gamma} \backslash B_{\gamma}}\left|W^{g_{b}}\right|^{2} d V_{g_{b}}=O\left(a^{4} \gamma\right) .$$
- Consider now the inner integrals
$$\int_{B_{\gamma} \backslash B_{\gamma / 8}}\left|W^{g_{X}}\right|^{2} d V_{g_{X}}-\int_{B_{\gamma} \backslash B_{\gamma / 8}}\left|W^{g_{a}}\right|^{2} d V_{g_{a}}=\int_{B_{\gamma} \backslash B_{\gamma / 8}}\left|W^{\tilde{g}_{a}}\right|^{2} d V_{\tilde{g}_{a}}-\int_{B_{\gamma} \backslash B_{\gamma / 8}}\left|W^{g_{a}}\right|^{2} d V_{g_{a}}$$
Recalling the definitions (5.2), (6.3) of $g_{a}, \tilde{g}_{a}$, if we locally write $g_{a}=g_{E}+a^{2} V$, then
$$\left(\tilde{g}_{a}\right)_{i j}(x)=\delta_{i j}+a^{2} V_{i j}(x)+a^{2}\left(\chi_{\gamma}(\gamma-|x|)-1\right) \tilde{\zeta}_{i j}^{a}(x),$$
where here (recall (5.3))
$$\tilde{\zeta}^{a}=a^{-2} \zeta^{a}, \quad \text { so that } \quad\left|\nabla^{k} \tilde{\zeta^{a}}\right| \leq C a|x|^{3+k}, \quad k=0, \ldots, 4 .$$
Thus we see that the difference between $\tilde{g}^{a}$ and $g^{a}$ this time is given by a term of main order $a^{3}$ (instead of $a^{2}$ as before), so that we can argue as above to see that the error term coming from (6.10) is $o\left(a^{4} \gamma\right)$. This concludes the proof. \(\square\)

\subsection*{6.2 Sign of the interaction term}

As shown in Proposition 6.2, the key quantity appearing in the energy balance is given by a positive constant times the product between the hessian of $A$ and the Weyl tensor $W^{M}(p)$.

Lemma 6.4. Let $A$ be given as in Section 3, and recall that $W:=W^{M}(p)$. Then, if $M$ is not self-dual or anti-self-dual, one has
$$W^{k i j l} \partial_{k l}^{2} A_{i j}(0)<0,$$
for a suitable choice of $p \in M$, of conformal normal coordinates for $g_{M}$ at $p$ and for $t-1$ small enough.
Remark 6.5. We notice that the interaction term (6.11) is not affected by gauge terms on $Z$ generated by infinitesimal diffeomorphisms. Indeed, for each term of type $\left(\mathcal{L}_{X} g\right)_{i j}=\nabla_{i} \omega_{j}+\nabla_{j} \omega_{i}$, being $g_{Z}$ Euclidean around 0 one has
$$W^{k i j l} \partial_{k l}^{2}\left(\mathcal{L}_{X} g\right)_{i j}=W^{k i j l}\left(\partial_{k l i}^{3} \omega_{j}+\partial_{k l j}^{2} \omega_{i}\right)=0,$$
by the symmetry properties of Weyl's tensor.
In order to prove Lemma 6.4, we need the following identity:
Lemma 6.6. Let $\left(e_{1}, \ldots, e_{4}\right)$ be an orthonormal basis for $T_{p} M$. Then
$$\begin{aligned}
W^{k i j l} \partial_{k l}^{2} A_{i j}(0) & =-\frac{1}{3} C_{2}(t) W \circledast W^{P}+O\left((t-1)^{-1}\right) \\
& =:-\frac{1}{3} C_{2}(t) W^{k i j l}\left(W_{k i j l}^{P}+W_{l i j k}^{P}\right)+O\left((t-1)^{-1}\right), \quad \text { as } t \rightarrow 1^{+},
\end{aligned}$$
where $W^{P}:=W \circ P$ and $P: T_{p} M \rightarrow T_{p} M$ denotes the linear map given by $P\left(e_{i}\right):=(-1)^{\delta_{4 i}} e_{i}$.
Proof. To see this, we just need to explicitly compute both sides of (6.12). Being $C_{2}(t)=O\left((t-1)^{-4}\right)$ as $t \rightarrow 1^{+}$, we can forget about the lower order error terms in the following computations. For the LHS, using (3.22) we have
$$\begin{aligned}
W^{k i j l} \partial_{k l}^{2} A_{i j}(0)=- & \frac{1}{3} C_{2}(t)\left[W^{k i j l}\left(W_{k i j l}+W_{l i j k}\right)-4 W^{4 i j l}\left(W_{4 i j l}+W_{l i j 4}\right)\right. \\
& \left.-4 W^{k i j 4}\left(W_{k i j 4}+W_{4 i j k}\right)+24 W^{4 i j 4} W_{4 i j 4}\right] \\
=- & \frac{1}{3} C_{2}(t) \sum_{i, j}\left[\sum_{k, l \neq 4} W_{k i j l}\left(W_{k i j l}+W_{l i j k}\right)-3 \sum_{l} W_{4 i j l}\left(W_{4 i j l}+W_{l i j 4}\right)\right. \\
+ & \left.\sum_{k \neq 4} W_{k i j 4}\left(W_{k i j 4}+W_{4 i j k}\right)-4 \sum_{k} W_{k i j 4}\left(W_{k i j 4}+W_{4 i j k}\right)+24\left(W_{4 i j 4}\right)^{2}\right] \\
=- & \frac{1}{3} C_{2}(t) \sum_{i, j}\left[\sum_{k, l \neq 4} W_{k i j l}\left(W_{k i j l}+W_{l i j k}\right)-3 \sum_{l \neq 4} W_{4 i j l}\left(W_{4 i j l}+W_{l i j 4}\right)\right. \\
- & \left.3 \sum_{k \neq 4} W_{k i j 4}\left(W_{k i j 4}+W_{4 i j k}\right)+10\left(W_{4 i j 4}\right)^{2}\right] .
\end{aligned}$$

As for the RHS of (6.12), by definition of $P$ we have
$$\begin{aligned}
W \circledast W^{P}= & W^{k i j l}\left(W_{k i j l}+W_{l i j k}\right)(-1)^{\delta_{4 k}+\delta_{4 i}+\delta_{4 j}+\delta_{4 l}} \\
= & \sum_{i, j}(-1)^{\delta_{4 i}+\delta_{4 j}}\left[\sum_{k, l \neq 4} W_{k i j l}\left(W_{k i j l}+W_{l i j k}\right)-\sum_{k \neq 4} W_{k i j 4}\left(W_{k i j 4}+W_{4 i j k}\right)\right. \\
& \left.\quad-\sum_{l \neq 4} W_{4 i j l}\left(W_{4 i j l}+W_{l i j 4}\right)+W_{4 i j 4}\left(W_{4 i j 4}+W_{4 i j 4}\right)\right] \\
= & \sum_{i, j, k, l \neq 4} W_{k i j l}\left(W_{k i j l}+W_{l i j k}\right)-\sum_{j, k, l \neq 4} W_{k 4 j l}\left(W_{k 4 j l}+W_{l 4 j k}\right)-\sum_{i, k, l \neq 4} W_{k i 4 l}\left(W_{k i 4 l}+W_{l i 4 k}\right) \\
& +\sum_{k, l \neq 4} W_{k 44 l}\left(W_{k 44 l}+W_{l 44 k}\right)-\sum_{i, j, k \neq 4} W_{k i j 4}\left(W_{k i j 4}+W_{4 i j k}\right)+\sum_{j, k \neq 4} W_{k 4 j 4}\left(W_{k 4 j 4}+W_{44 j k}\right) \\
& -\sum_{i, j, l \neq 4} W_{4 i j l}\left(W_{4 i j l}+W_{l i j 4}\right)+\sum_{i, l \neq 4} W_{4 i 4 l}\left(W_{4 i 4 l}+W_{l i 44}\right)+2 \sum_{i, j \neq 4}\left(W_{4 i j 4}\right)^{2} \\
= & \sum_{i, j}\left[\sum_{k, l \neq 4} W_{k i j l}\left(W_{k i j l}+W_{l i j k}\right)-\sum_{k \neq 4} W_{k i j 4}\left(W_{k i j 4}+W_{4 i j k}\right)-\sum_{l \neq 4} W_{4 i j l}\left(W_{4 i j l}+W_{l i j 4}\right)\right] \\
& -2 \sum_{j, k, l \neq 4} W_{k 4 j l}\left(W_{k 4 j l}+W_{l 4 j k}\right)-2 \sum_{i, k, l \neq 4} W_{k i 4 l}\left(W_{k i 4 l}+W_{l i 4 k}\right) \\
& +2 \sum_{j, k \neq 4}\left(W_{k 4 j 4}\right)^{2}+2 \sum_{i, l \neq 4}\left(W_{4 i 4 l}\right)^{2}+2 \sum_{i, j}\left(W_{4 i j 4}\right)^{2} .
\end{aligned}$$
Relabeling the indices and using the symmetries of curvature tensors, we also have
$$\begin{aligned}
\sum_{j, k, l \neq 4} W_{k 4 j l}\left(W_{k 4 j l}+W_{l 4 j k}\right) & =\sum_{j, k, l \neq 4} W_{4 k l j}\left(W_{4 k l j}+W_{j k l 4}\right)=\sum_{i, j, l \neq 4} W_{4 i j l}\left(W_{4 i j l}+W_{l i j 4}\right) \\
& =\sum_{i, j} \sum_{l \neq 4} W_{4 i j l}\left(W_{4 i j l}+W_{l i j 4}\right)-\sum_{i, l \neq 4} W_{4 i 4 l}\left(W_{4 i 4 l}+W_{l i 44}\right),
\end{aligned}$$
and
$$\begin{aligned}
\sum_{i, k, l \neq 4} W_{k i 4 l}\left(W_{k i 4 l}+W_{l i 4 k}\right) & =\sum_{i, k, l \neq 4} W_{i k l 4}\left(W_{i k l 4}+W_{4 k l i}\right)=\sum_{i, j, k \neq 4} W_{k i j 4}\left(W_{k i j 4}+W_{4 i j k}\right) \\
& =\sum_{i, j} \sum_{k \neq 4} W_{k i j 4}\left(W_{k i j 4}+W_{4 i j k}\right)-\sum_{j, k \neq 4} W_{k 4 j 4}\left(W_{k 4 j 4}+W_{44 j k}\right) .
\end{aligned}$$
Substituting in (6.14) yields
$$\begin{array}{r}
W \circledast W^{P}=\sum_{i, j}\left[\sum_{k, l \neq 4} W_{k i j l}\left(W_{k i j l}+W_{l i j k}\right)-3 \sum_{k \neq 4} W_{k i j 4}\left(W_{k i j 4}+W_{4 i j k}\right)\right. \\
\left.-3 \sum_{l \neq 4} W_{4 i j l}\left(W_{4 i j l}+W_{l i j 4}\right)\right]+10 \sum_{i, j}\left(W_{4 i j 4}\right)^{2} .
\end{array}$$
(6.12) now follows by comparing the above identity with (6.13). \(\square\)

Proof of Lemma 6.4. As above, assume $\left\{e_{1}, \ldots, e_{4}\right\}$ is an orthonormal basis for $T_{p} M$ and let $\left\{e^{1}, \ldots, e^{4}\right\}$ denote the dual basis. To begin we recall that, given two tensors $S, T \in\left(T_{p}^{*} M\right)^{\otimes 4}$ with the symmetries of Riemann's tensor, they define symmetric endomorphisms $\widehat{S}, \widehat{T} \in \operatorname{End}\left(\Lambda^{2}\left(T_{p}^{*} M\right)\right)$ as in (2.2). In particular, with this convention
$$\operatorname{tr}(\widehat{S} \widehat{T})=\frac{1}{4}\langle S, T\rangle=\frac{1}{4} S^{k i j l} T_{k i j l} .$$

Given the map $P$ defined in Lemma 6.6, i.e. $P\left(e_{i}\right):=(-1)^{\delta_{4 i}} e_{i}$ (but this holds more generally $\forall P \in \mathrm{GL}(4, \mathbb{R})$ ), we define the map $W^{P}:=W \circ P$, to which we can associate $\widehat{W}^{P} \in \operatorname{End}\left(\Lambda^{2}\left(T_{p}^{*} M\right)\right)$. We can also extend $P$ to a linear map $\widehat{P} \in \operatorname{End}\left(\Lambda^{2}\left(T_{p}^{*} M\right)\right)$ by letting
$$\widehat{P}\left(e^{i} \wedge e^{j}\right):=P^{T}\left(e^{i}\right) \wedge P^{T}\left(e^{j}\right),$$
where $P^{T} \in \operatorname{End}\left(T_{p}^{*} M\right)$ denotes the transpose of $P$, defined by $P^{T}\left(e^{i}\right):=P_{j}^{i} e^{j}$. In this setting, a direct computation gives the following identity:
$$\widehat{W}^{P}=\widehat{P} \circ \widehat{W} \circ \widehat{P}^{*},$$
where $\widehat{P}^{*}$ is the adjoint of $\widehat{P}$.
By [Der83, Lemma 2], there exists an oriented orthonormal basis $\left\{e_{1}, \ldots e_{4}\right\}$ for $T_{p} M$ such that, letting
$$\begin{array}{ll}
\omega^{+}=e^{1} \wedge e^{2}+e^{3} \wedge e^{4} & \omega^{-}=e^{1} \wedge e^{2}-e^{3} \wedge e^{4} \\
\eta^{+}=e^{1} \wedge e^{3}+e^{4} \wedge e^{2} & \eta^{-}=e^{1} \wedge e^{3}-e^{4} \wedge e^{2} \\
\vartheta^{+}=e^{1} \wedge e^{4}+e^{2} \wedge e^{3} & \vartheta^{-}=e^{1} \wedge e^{4}-e^{2} \wedge e^{3},
\end{array}$$
then $\left\{\omega^{ \pm}, \eta^{ \pm}, \vartheta^{ \pm}\right\}$is an orthogonal basis for $\Lambda_{ \pm}^{2}\left(T_{p}^{*} M\right)$ and $\widehat{W}_{ \pm}$is diagonalized in such a basis. In particular, let us denote by $\lambda^{ \pm}, \mu^{ \pm}, \nu^{ \pm}$the eigenvalues of $\widehat{W}_{ \pm}$so that, in the basis (6.17), one has
$$\widehat{W}=\left(\begin{array}{llllll}
\lambda^{+} & & & & & \\
& \mu^{+} & & & & \\
& & \nu^{+} & & & \\
& & & \lambda^{-} & & \\
& & & & \mu^{-} & \\
& & & & & \nu^{-}
\end{array}\right) .$$
If we now look at the action of $\widehat{P}$ on the elements of (6.17), we see that
$$\widehat{P}=\left(\begin{array}{ccc|ccc} 
& 0 & & & & \\
& & & & \\
\hline 1 & & & & \\
& 1 & & & 0
\end{array}\right) .$$
Hence, by (6.15), (6.16) we got
$$W^{k i j l} W_{k i j l}^{P}=4 \operatorname{tr}\left(\widehat{W} \widehat{W}^{P}\right)=4 \operatorname{tr}\left(\widehat{W} \widehat{P} \widehat{W} \widehat{P}^{*}\right)=8\left(\lambda^{+} \lambda^{-}+\mu^{+} \mu^{-}+\nu^{+} \nu^{-}\right),$$
and the latter quantity can be made positive (for a suitable choice of $p \in M$ ) whenever $M$ is not self-dual or anti-self-dual, see the proof of Lemma 6.2 in [MM25]. We notice that under the assumptions of Theorem 1.1 we can always find a point $p \in M$ where both $W_{+}(p) \neq 0$ and $W_{-}(p) \neq 0$. In fact, the vanishing of $B_{i j}$, coupled with a proper conformal choice and the use of biharmonic coordinates, becomes an elliptic system. Therefore the metric $g$ has to be real analytic, see [ADN64, Theorem 12.1] (and [DK81] for the case of Einstein metrics), so neither $W_{+}$nor $W_{-}$can vanish on open sets of $M$ without being identically zero.

Finally, being $\widehat{W}^{P}$ diagonal as well, we can apply [GV16, Lemma 12.2] to show that
$$W \circledast W^{P}=\frac{3}{2} W^{k i j l} W_{k i j l}^{P},$$
which, together with (6.12) and (6.18), allows to obtain (6.11) provided $t-1$ is small enough. \(\square\)

\subsection*{6.3 Construction for a general locally conformally flat $Z$ of positive Yamabe class and conclusion of the proof of Theorem 1.1}

Here we will exploit the construction in Section 3 to deal with the case of a general $Z$. Recall that, by Theorem 3.1, $Z$ is a connected sum of quotients of the type $\left(\mathbb{S}_{t_{i}}^{1} \times \mathbb{S}^{3}\right) / G_{i}$ for some $t_{i}>1$ and finite groups $G_{i}$.

Let us focus our attention to the first summand, and let us set for brevity $\left(\mathbb{S}_{t}^{1} \times \mathbb{S}^{3}\right) / G=\left(\mathbb{S}_{t_{1}}^{1} \times\right.$ $\left.\mathbb{S}^{3}\right) / G_{1}:=Z_{1}$. Our goal is to extend the previous tensor $F$ from $Z_{1}$ to $Z$ so that the Weyl energy is affected as little as possible. Our goal is to prove the following result.

Proposition 6.7. Let $g_{Z_{1}}$ be a locally conformally flat metric on $Z_{1}$, and let $g_{b}=g_{Z_{1}}+b^{2} F(b \ll 1)$ be the metric as at the beginning of Section 4. For $\tilde{q} \in Z_{1}, \tilde{q} \neq q$, we assume that $Z$ is obtained from $Z_{1}$ via a connected sum near $\tilde{q}$. Then for every $\varepsilon>0$ there exists $\delta>0$ and a metric $g_{\varepsilon}$ on $Z$ such that $g_{\varepsilon}=g_{b}$ on $Z_{1} \backslash B_{\delta}(\tilde{q})$ and such that
$$\left.\left|\int_{Z}\right| W_{g_{\varepsilon}}\right|_{g_{\varepsilon}} ^{2} d V_{g_{\varepsilon}}-\int_{Z_{1}}\left|W_{g_{b}}\right|_{g_{b}}^{2} d V_{g_{b}} \mid<\varepsilon .$$
Here $q$, as before, is the point of $Z_{1}$ where we perform a connected sum to $M$.
In the proof of Theorem 1.1 below, we will need a number of small parameters. We will first take $b$ to be small, and later choose $\varepsilon$ much smaller.

Proof. Without loss of generality, we can assume that $g_{Z_{1}}$ is Euclidean in $B_{\delta}(\tilde{q})$, and we can choose $\delta$ so small that
$$\int_{B_{\delta}(\tilde{q})}\left|W_{g_{b}}\right|_{g_{b}}^{2} d V_{g_{b}}<\frac{\varepsilon}{2}$$
We choose $0<\tilde{\delta} \ll \delta$ and choose a radial cutoff function $\chi=\chi(r)$ in $\mathbb{R}^{4}$ such that
$$\begin{cases}\chi(r)=0 & \text { in } B_{\tilde{\delta}}(0) ; \\ \chi(r)=1 & \text { in } \mathbb{R}^{4} \backslash B_{\delta}(0) ; \\ \int_{B_{\delta}(0)}\left(\left|\nabla^{2} \chi\right|^{2}+|\nabla \chi|^{4}\right) d x=o_{\tilde{\delta} / \delta}(1) . & \end{cases}$$
Here $o_{\tilde{\delta} / \delta}(1)$ is a quantity that tends to zero as $\tilde{\delta} / \delta$ tends to zero: the latter property in the last formula can be satisfied by capacity reasons, see e.g. Theorem 2.1.6 in [Zie89].

Recalling that we assume $g_{Z_{1}}$ to be locally Euclidean near $\tilde{q}$, we define $g_{\varepsilon}$ in $g_{Z_{1}}$-normal coordinates $x$ at $\tilde{q}$ as
$$g_{\varepsilon}=d x^{2}+\chi(|x|) b^{2} F,$$
with $\tilde{\delta}$ to be determined later.
Recall from [MM25], formula (5.41), that the following estimate holds true:
$$\left|W^{g}\right|_{g}^{2}=W^{i j k l} W_{i j k l} \leq C\left(\left|\nabla g^{-1}\right|^{2}|\nabla g|^{2}+|\nabla g|^{4}+\left|\nabla^{2} g\right|^{2}\right) .$$
Here we are denoting by $g$ a metric on $\mathbb{R}^{4}$ whose coefficient matrix is pointwise close to the Kronecker symbols, as in our case.

By (6.19) and our choice of $\chi$, we have that also
$$\int_{B_{\delta}(\tilde{q})}\left|W_{g_{\varepsilon}}\right|_{g_{\varepsilon}}^{2} d V_{g_{\varepsilon}}<\frac{\varepsilon}{2},$$
whenever $\tilde{\delta}$ is chosen sufficiently small, depending on $b, \varepsilon$ and $\delta$.
By our choice of $\chi(|x|), g_{\varepsilon}$ is Euclidean in $B_{\tilde{\delta}}(\tilde{q})$. We can therefore assume that $g_{Z}$ is obtained via a connected sum in this ball with the other manifolds $\left(\mathbb{S}_{t_{i}}^{1} \times \mathbb{S}^{3}\right) / G_{i}, i>1$, and obtain a metric $g_{\varepsilon}$ on the whole $Z$ as desired. \(\square\)

We can now conclude the proof of Theorem 1.1.
Proof of Theorem 1.1. We start by considering the case in which the manifold $Z$ is a single quotient of $\mathbb{S}^{1} \times \mathbb{S}^{3}$. As pointed out in Remark 6.1, the manifold $X$ defined at the beginning of Section 6 is diffeomorphic to $Z \# \bar{M}$. However, if we perform the same procedure with $Z$ and $\bar{M}$, we end up with a manifold $Y \stackrel{\text { diff }}{\cong} Z \# M$. Applying Proposition 6.2, we obtain
$$\mathcal{W}^{Y}\left(g_{Y}\right)-\mathcal{W}^{M}\left(g_{M}\right)=\frac{2}{3} a^{4}\left(W^{\bar{M}}(p)\right)^{k i j l} \partial_{k l}^{2} A_{i j}(0)+O\left(a^{4} \gamma\right)+o\left(a^{4}\right) .$$
If $\left(M, g_{M}\right)$ is not self-dual/anti-self-dual, then the same is true for $\bar{M}$, so the proof now follows from Lemma 6.4 and a subsequent suitable choice of $0<a \ll \gamma \ll 1$. We therefore obtained the desired inequality $\mathcal{W}^{Y}\left(g_{Y}\right)-\mathcal{W}^{M}\left(g_{M}\right)<0$ for our special choice of $Z$.

In the general case in which $Z$ is a connected sum of quotients of $\mathbb{S}^{1} \times \mathbb{S}^{3}$, we call $Z_{1}$ one of these quotients and define $F$ on $Z_{1}$ as in Section 3. If, as before, $q \in Z_{1}$ be the gluing point to $M$, we recall that $g_{Y}=g_{b}$ away from $q$. Choosing then $\varepsilon<\frac{1}{2}\left(\mathcal{W}^{M}\left(g_{M}\right)-\mathcal{W}^{Y}\left(g_{Y}\right)\right)$ in Proposition 6.7, we obtain the inequality $\mathcal{W}^{Y}\left(g_{Y}\right)-\mathcal{W}^{M}\left(g_{M}\right)<0$ for a general locally conformally flat $Z$. \(\square\)

\subsection*{6.4 Connected sum of a Bach-flat orbifold with a locally conformally flat orbifold and proof of Theorem 1.4}

In this last subsection we show how to extend the proof of Theorem 1.1 for some orbifolds. We start by recalling the definition of orbifold:

Definition 6.8. A Riemannian orbifold ( $M^{n}, g$ ) is a topological space which is a smooth manifold with a smooth metric away from a finite set of singular points. At each singular point $p, M$ is locally diffeomorphic to a cone over a spherical space form $\mathbb{S}^{n-1} / \Gamma_{p}$, where $\Gamma_{p} \subset \operatorname{SO}(n)$ is a finite subgroup acting freely on $\mathbb{S}^{n-1}$. Moreover, we require that at each singular point the metric locally lifts to a smooth (up to the origin), $\Gamma_{p}$-equivariant metric on a small Euclidean ball.

As for the locally conformally flat four-manifolds with positive scalar curvature, we have a similar classification result for orbifolds of the same class:

Theorem 6.9 ([CTZ12], Corollary 5.3 and [Wan25], Theorem 1.6). Let $\left(Z, g_{Z}\right)$ be a closed, oriented, locally conformally flat 4-orbifold with positive scalar curvature. Then $Z$ is diffeomorphic to a connected sum of manifolds of type $\left(\mathbb{R} \times \mathbb{S}^{3}\right) / G$ and $\mathbb{S}^{4} / \Gamma$, where $G$ is a cocompact discrete subgroup of the isometry group of the standard metric on $\mathbb{R} \times \mathbb{S}^{3}$ with at most isolated singularities, and $\Gamma \subset \operatorname{SO}(4) \subset \operatorname{SO}(5)$ has two fixed antipodal points. In particular, a finite manifold cover of $Z$ is diffeomorphic to $\mathbb{S}^{4}$ or a connected sum of copies of $\mathbb{S}^{1} \times \mathbb{S}^{3}$.

Here by manifold cover we mean that $Z$ is obtained as a quotient of a smooth manifold by the action of some group with fixed points. The next two lemmas shed some light on the structure of each singular factor in the decomposition.

Lemma 6.10. All the factors $\mathbb{S}^{4} / \Gamma$ in Theorem 6.9 are football orbifolds.
Proof. The lemma follows from the fact that if $\Gamma \subset \operatorname{SO}(5)$ acts on $\mathbb{S}^{4}$ with only isolated fixed points, then $\Gamma$ fixes exactly two antipodal points on $\mathbb{S}^{4}$ and acts freely on the orthogonal $\mathbb{S}^{3}$-section of $\mathbb{S}^{4}$, see Lemma 5.1 and the discussion at p. 75 in [CTZ12]. \(\square\)

Lemma 6.11. All the factors $\left(\mathbb{R} \times \mathbb{S}^{3}\right) / G$ in Theorem 6.9 only possess $\mathbb{Z}_{2}$-orbifold singularities, and the number of orbifold points is either 0 or 4 .

Proof. By the discussion in Section 3.2.1, we can assume that there exists a normal subgroup $H \unlhd G$, of finite index and isomorphic to $\mathbb{Z}$, which acts on $\mathbb{R} \times \mathbb{S}^{3}$ via translations of length $m R$, for $m \in \mathbb{Z}$ and $R>0$ fixed, and which contains all translations in $G$. Therefore it is sufficient to consider finite quotients of the cylinder $\left([-R / 2, R / 2] \times \mathbb{S}^{3}\right) / \sim$ under the action of the quotient group $N:=G / H$. Looking at the proof of Lemma 3.8, we see that the only elements $\gamma \in N$ (all orientation-preserving) generating fixed points are maps acting as an inversion on the first factor and a rotation $O \in \mathrm{O}(4) \backslash \mathrm{SO}(4)$ on the second one, namely $\gamma(r, w)=(L-r, O(w))$, for $|L| \leq R / 2$. In this case, $\operatorname{det}(I-O)=0$ and there exists a (unique up to sign ${ }^{4}$ ) vector $v \in \mathbb{S}^{3}$ satisfying $O(v)=v$. Then
$$\left(\frac{L}{2}, \pm v\right), \quad\left(\frac{L+R}{2}, \pm v\right),$$
are four distinct fixed points for $\gamma$. Moreover, since $\gamma^{2}=\left(\mathrm{Id}, O^{2}\right)$ and $O^{2}$ fixes $\pm v$, then necessarily $O^{2}=\mathrm{Id}$ as otherwise $\gamma^{2}$ would fix a positive-dimensional set. This means that $O$ has only eigenvalues 1 (with multiplicity 1 ) and -1 (with multiplicity 3 ). Conversely, all elements in $N$ containing an inversion on the $\mathbb{S}^{1}$-factor are of this form and thus fix 4 points exactly.

Now, let us write $N=N_{+} \sqcup N_{-}$, where
$$N_{ \pm}:=\{\gamma=(\rho, O) \in N \mid \operatorname{det}(\rho)= \pm 1\} .$$
If $N_{-}=\emptyset$, then all elements in $N$ act freely and the quotient is a smooth manifold. Therefore assume from now on that $N_{-} \neq \emptyset$. Since the sign map
$$N \rightarrow\{ \pm 1\}, \quad \gamma=(\rho, O) \mapsto \operatorname{det}(\rho),$$
is a homomorphism, then $\left|N_{-}\right|=|N| / 2$. Moreover, each fixed point has stabilizer of order 2 (if nontrivial $\gamma_{1} \neq \gamma_{2}$ both fix $p=(s, w)$, then $\gamma_{1} \gamma_{2} \neq \mathrm{Id}$ would fix $\mathbb{S}^{1} \times\{w\}$, which is not possible), therefore we always have that, for any $\gamma_{1} \neq \gamma_{2}, \gamma_{1}, \gamma_{2} \in N_{-}$, the fixed point sets of $\gamma_{1}$ and $\gamma_{2}$ are always pairwise disjoint and each fixed point generates an orbit of cardinality $|N| / 2$. Hence the total number of fixed points is $4 \cdot\left|N_{-}\right|=2|N|$, which, once divided by the orbit size $|N| / 2$, descends to 4 orbifold points. This concludes the proof. \(\square\)

Proof of Theorem 1.4. The proof essentially goes along the same lines of that of Theorem 1.1, therefore we will only highlight how the arguments extend to the orbifold case.

The crucial point is that Theorem 6.9 allows us to extend the construction in Section 3 to this case whenever we have a $\mathbb{Z}_{2}$-orbifold point lifting to a cylinder quotient. Indeed, assume we have a singular tensor $F$ on $Z$ which behaves as in Proposition 3.11 near the orbifold point. Then, since the quadratic term $\partial_{k l}^{2} A_{i j}(0) x^{k} x^{l}$ will be $\mathbb{Z}_{2}$-equivariant at 0 , we can immediately define the correction $H$ on $M$, singular at the orbifold point $p \in M$, as in (5.1) (it's a purely local argument). At this point, we can perform all the energy expansions as in sections 4 and 5, where the only change will be a different coefficient (depending only on $|\Gamma|=2$, thus equal on $M$ and $Z$ ) multiplying each term in the energy expansions and caused by the different volume of geodesic balls around the orbifold points. We can then define the metric $g_{X}$ on the connected sum and conclude the proof just as above; in particular, the proof of Lemma 6.4 only depends on a choice of coordinates on a local covering of the orbifold point, so the argument extends with no further issue.

Given the above discussion, we now focus on the construction of the singular section $F$ on $Z$.
Let us start by assuming that $Z$ is a single quotient of type $\left(\mathbb{R} \times \mathbb{S}^{3}\right) / G$. In this case, the group $G$ does not act freely but with fixed points, which descend indeed to four orbifold points by Lemma 6.11. Up to composition with an isometry, we can assume that the orbifold point in $Z$ in which we would like to perform the gluing is $q=(0, S) \in \mathbb{R} \times \mathbb{S}^{3}$. We can then argue exactly as in Section 3.2

\footnotetext{
${ }^{4}$ With 2 vectors we could take combinations between them and obtain a positive-dimensional set of fixed points.
}
and, after possibly shrinking the cylindrical variable, define a singular tensor $\xi$ on $\mathbb{R}^{4} \backslash\{0\}$ as in (3.32), namely which is gauged in such a way to make the series of its pullbacks convergent and with covariant derivatives vanishing up to first order at $-e_{4}$. We can also add a further gauge term to also project the hessian on symmetrized curvature-type tensors. By construction, the series of pullbacks will be equivariant and thus define a tensor on $Z$ itself with all the desired properties. Note that the pullbacks by elements in the stabilizer of $(0, S)$ (which is a subgroup isomorphic to the orbifold group $\mathbb{Z}_{2}$ ) do not modify the asymptotic behavior of $\xi$ at $(0, S)$ by virtue of the fact that the Weyl tensor is evaluated at the orbifold point $p \in M$, and therefore it is already $\mathbb{Z}_{2}$-invariant.

We now consider the general case in which $Z$ is diffeomorphic to one of the manifolds described in Theorem 6.9, namely
$$Z \stackrel{\text { diff }}{\cong} \#_{i} \frac{\mathbb{R} \times \mathbb{S}^{3}}{G_{i}} \#_{j} \frac{\mathbb{S}^{4}}{\Gamma_{j}} .$$
If the orbifold point $q$ belongs to one of the $\left(\mathbb{R} \times \mathbb{S}^{3}\right) / G_{i}$ factors, then we can argue as before to define a singular tensor on that factor and then employ Proposition 6.7 to define a tensor on the whole $Z$. Now, from Lemmas 6.10 and 6.11, we know that the number of orbifold points with any given group $\Gamma$ is always an even number. Moreover, if there are at least 4 orbifold points with group $\mathbb{Z}_{2}$, then we can assume that the orbifold point $q$ always belongs to a cylinder quotient $\left(\mathbb{R} \times \mathbb{S}^{3}\right) / G$ in the orbifold decomposition (6.20). Indeed, the connected sum of two $\mathbb{Z}_{2}$-footballs is diffeomorphic to the quotient $\left(\mathbb{S}^{1} \times \mathbb{S}^{3}\right) / N$, where e.g. $N=\{\mathrm{Id}, \gamma\}$ and $\gamma(r, w)=(-r, O(w))$, where $O=\operatorname{diag}(1,-1,-1,-1)$. This concludes the proof. \(\square\)

Remark 6.12. We expect that Theorem 1.4 can be extended to the more general case in which $Z$ is not conformally equivalent to a football orbifold. Indeed, by Theorem 6.9 we know that any such orbifold admits a finite manifold cover diffeomorphic to a connected sum of copies of $\mathbb{S}^{1} \times \mathbb{S}^{3}$. Then the hope is to define a singular correction $F_{0}$ on one of these cylinder factors, and define $F$ afterwards as the sum of the pullbacks of $F_{0}$ by the (finitely many) deck elements. However, there are two issues related to this approach that need to be addressed. The first is that we need to suitably "normalize" the manifold cover (and thus $Z$ ) so that the orbifold point $q$ lifts to a point at the center of a narrow cylinder $\mathbb{S}_{t}^{1} \times \mathbb{S}^{3}$ with $t$ close to 1 . The second difficulty lies in the fact that, when $|\Gamma| \geq 3$, the representation of $\Gamma$ as a group of matrices depends on our choice of coordinates on the orbifold chart, and in general there will be multiple representations, any two of which agree only up to conjugation with a suitable matrix in SO(4). Hence we need to choose orbifold charts which simultaneously provide the same "matrix representation" of $\Gamma$ at $p \in M$ and $q \in Z$, while also diagonalizing the Weyl operator on $M$ and providing the right interaction on $Z$.

\section*{References}
\begin{itemize}
\item[] [AGS13] Elsa Abbena, Sergio Garbiero, and Simon Salamon. "Bach-flat Lie groups in dimension 4". In: C. R. Math. Acad. Sci. Paris 351.7-8 (2013), pp. 303-306. issn: 1631-073X,1778-3569. doi: 10.1016/j.crma.2013.04.011. URL: https://doi.org/10.1016/j.crma.2013.04.011.
\item[] [AV12] Antonio G. Ache and Jeff A. Viaclovsky. "Obstruction-flat asymptotically locally Euclidean metrics". In: Geom. Funct. Anal. 22.4 (2012), pp. 832-877. ISSN: 1016-443X,1420-8970. doi: 10.1007/s00039-012-0163-x. URL: https://doi.org/10.1007/s00039-012-0163-x.
\item[] [AV15] Antonio G. Ache and Jeff A. Viaclovsky. "Asymptotics of the self-dual deformation complex". In: J. Geom. Anal. 25.2 (2015), pp. 951-1000. ISSN: 1050-6926,1559-002X. DOI: 10.1007/s12220-013-9452-3. URL: https://doi.org/10.1007/s12220-013-9452-3.
\end{itemize}
\begin{itemize}
\item[] [ADN64] Shmuel Agmon, Avron Douglis, and Louis Nirenberg. "Estimates near the boundary for solutions of elliptic partial differential equations satisfying general boundary conditions. II". In: Comm. Pure Appl. Math. 17 (1964), pp. 35-92. ISSN: 0010-3640,1097-0312. doi: 10.1002/cpa.3160170104. URL: https://doi.org/10.1002/cpa.3160170104.
\item[] [And89] Michael T. Anderson. "Ricci curvature bounds and Einstein metrics on compact manifolds". In: J. Amer. Math. Soc. 2.3 (1989), pp. 455-490. ISSN: 0894-0347,1088-6834. DOI: 10.2307/1990939. URL: https://doi.org/10.2307/1990939.
\item[] [And05] Michael T. Anderson. "Orbifold compactness for spaces of Riemannian metrics and applications". In: Math. Ann. 331.4 (2005), pp. 739-778. ISSN: 0025-5831,1432-1807. doi: 10.1007/s00208-004-0603-5. URL: https://doi.org/10.1007/s00208-004-0603-5.
\item[] [And06] Michael T. Anderson. "Canonical metrics on 3-manifolds and 4-manifolds". In: Asian J. Math. 10.1 (2006), pp. 127-163. ISSN: 1093-6106,1945-0036. DOI: 10.4310/AJM.2006.v10.n1.a8. URL: https://doi.org/10.4310/AJM.2006.v10.n1.a8.
\item[] [And10] Michael T. Anderson. "A survey of Einstein metrics on 4-manifolds". In: Handbook of geometric analysis, No. 3. Vol. 14. Adv. Lect. Math. (ALM). Int. Press, Somerville, MA, 2010, pp. 1-39. ISBN: 978-1-57146-205-3.
\item[] [Bac21] Rudolf Bach. "Zur Weylschen Relativitätstheorie und der Weylschen Erweiterung des Krümmungstensorbegriffs". In: Math. Z. 9.1 (1921), pp. 110-135. ISSN: 1432-1823. doi: 10.1007/BF01378338. URL: https://doi.org/10.1007/BF01378338.
\item[] [BH11] Eric Bahuaud and Dylan Helliwell. "Short-time existence for some higher-order geometric flows". In: Comm. Partial Differential Equations 36.12 (2011), pp. 2189-2207. ISSN: 0360-5302,1532-4133. DOI: 10.1080/03605302.2011.593015. URL: https://doi.org/10.1080/03605302.2011.593015.
\item[] [BH15] Eric Bahuaud and Dylan Helliwell. "Uniqueness for some higher-order geometric flows". In: Bull. Lond. Math. Soc. 47.6 (2015), pp. 980-995. ISSN: 0024-6093,1469-2120. DOI: 10.1112/blms/bdv076. URL: https://doi.org/10.1112/blms/bdv076.
\item[] [BKN89] Shigetoshi Bando, Atsushi Kasue, and Hiraku Nakajima. "On a construction of coordinates at infinity on manifolds with fast curvature decay and maximal volume growth". In: Invent. Math. 97.2 (1989), pp. 313-349. ISSN: 0020-9910,1432-1297. DOI: 10.1007/BF01389045. URL: https://doi.org/10.1007/BF01389045.
\item[] [BK03] Matthias Bauer and Ernst Kuwert. "Existence of minimizing Willmore surfaces of prescribed genus". In: Int. Math. Res. Not. 10 (2003), pp. 553-576. ISSN: 1073-7928,1687-0247. doi: 10.1155/S1073792803208072. URL: https://doi.org/10.1155/S1073792803208072.
\item[] [Bes08] Arthur L. Besse. Einstein manifolds. Classics in Mathematics. Reprint of the 1987 edition. Springer-Verlag, Berlin, 2008, pp. xii+516.
\item[] [Bre08] Simon Brendle. "Blow-up phenomena for the Yamabe equation". In: J. Amer. Math. Soc. 21.4 (2008), pp. 951-979. ISSN: 0894-0347,1088-6834. doi: 10.1090/S0894-0347-07-00575-9. URL: https://doi.org/10.1090/S0894-0347-07-00575-9.
\item[] [CM20] Giovanni Catino and Paolo Mastrolia. A perspective on canonical Riemannian metrics. Vol. 336. Progress in Mathematics. Birkhäuser/Springer, Cham, 2020, pp. xix+247. ISBN: 978-3-030-57184-9. DOI: 10.1007/978-3-030-57185-6. URL: https://doi.org/10.1007/978-3-030-57185-6.
\item[] [CGZ20] Sun-Yung A. Chang, Matthew Gursky, and Siyi Zhang. "A conformally invariant gap theorem characterizing $\mathbb{C P}^{2}$ via the Ricci flow". In: Math. Z. 294.1-2 (2020), pp. 721-746. ISSN: 0025-5874,1432-1823. DOI: 10.1007/s00209-019-02331-8. URL: https://doi.org/10.1007/s00209-019-02331-8.
\end{itemize}
\begin{itemize}
\item[] [CG86] Jeff Cheeger and Mikhael Gromov. "Collapsing Riemannian manifolds while keeping their curvature bounded. I". In: J. Differential Geom. 23.3 (1986), pp. 309-346. ISSN: 0022-040X,1945-743X. URL: http://projecteuclid.org/euclid.jdg/1214440117.
\item[] [CG90] Jeff Cheeger and Mikhael Gromov. "Collapsing Riemannian manifolds while keeping their curvature bounded. II". In: J. Differential Geom. 32.1 (1990), pp. 269-298. ISSN: 0022-040X,1945-743X. URL: http://projecteuclid.org/euclid.jdg/1214445047.
\item[] [CTZ12] Bing-Long Chen, Siu-Hung Tang, and Xi-Ping Zhu. "Complete classification of compact fourmanifolds with positive isotropic curvature". In: J. Differential Geom. 91.1 (2012), pp. 41-80. ISSN: 0022-040X,1945-743X. URL: http://projecteuclid.org/euclid.jdg/1343133700.
\item[] [CLQ23] Jiaqi Chen, Peng Lu, and Jie Qing. "Conformal Bach flow". In: Ann. Global Anal. Geom. 63.2 (2023), Paper No. 19, 30. ISSN: 0232-704X, 1572-9060. DOI: 10.1007/s10455-023-09897-x. URL: https://doi.org/10.1007/s10455-023-09897-x.
\item[] [Der83] Andrzej Derdziński. "Self-dual Kähler manifolds and Einstein manifolds of dimension four". In: Compositio Math. 49.3 (1983), pp. 405-433. ISSN: 0010-437X,1570-5846. URL: http://www.numdam.org/item?id=CM_1983__49_3_405_0.
\item[] [DK81] Dennis M. DeTurck and Jerry L. Kazdan. "Some regularity theorems in Riemannian geometry". In: Ann. Sci. École Norm. Sup. (4) 14.3 (1981), pp. 249-260. ISSN: 0012-9593. url: http://www.numdam.org/item?id=ASENS_1981_4_14_3_249_0.
\item[] [DF89] S. Donaldson and R. Friedman. "Connected sums of self-dual manifolds and deformations of singular spaces". In: Nonlinearity 2.2 (1989), pp. 197-239. ISSN: 0951-7715,1361-6544. url: http://stacks.iop.org/0951-7715/2/197.
\item[] [Flo91] Andreas Floer. "Self-dual conformal structures on $l \mathbf{C P}^{2}$ ". In: J. Differential Geom. 33.2 (1991), pp. 551-573. ISSN: 0022-040X,1945-743X. URL: http://projecteuclid.org/euclid.jdg/1214446330.
\item[] [GP79] G. W. Gibbons and C. N. Pope. "The positive action conjecture and asymptotically Euclidean metrics in quantum gravity". In: Comm. Math. Phys. 66.3 (1979), pp. 267-290. ISSN: 0010-3616,1432-0916. URL: http://projecteuclid.org/euclid.cmp/1103905050.
\item[] [GG24] A. Rod Gover and Matthew J. Gursky. "The anti-self-dual deformation complex and a conjecture of Singer". In: J. Reine Angew. Math. 811 (2024), pp. 293-316. ISSN: 0075-4102,1435-5345. DOI: 10.1515/crelle-2024-0028. URL: https://doi.org/10.1515/crelle-2024-0028.
\item[] [Gro00] Misha Gromov. "Spaces and questions". In: GAFA 2000 (Tel Aviv, 1999). 2000, pp. 118-161.
\item[] [GV16] Matthew J. Gursky and Jeff A. Viaclovsky. "Critical metrics on connected sums of Einstein four-manifolds". In: Adv. Math. 292 (2016), pp. 210-315. ISSN: 0001-8708,1090-2082. doi: 10.1016/j.aim.2015.11.054. URL: https://doi.org/10.1016/j.aim.2015.11.054.
\item[] [Ham97] Richard S. Hamilton. "Four-manifolds with positive isotropic curvature". In: Comm. Anal. Geom. 5.1 (1997), pp. 1-92. ISSN: 1019-8385,1944-9992. DOI: 10.4310/CAG.1997.v5.n1.a1. URL: https://doi.org/10.4310/CAG.1997.v5.n1.a1.
\item[] [Hit74] Nigel Hitchin. "Compact four-dimensional Einstein manifolds". In: J. Differential Geometry 9 (1974), pp. 435-441. ISSN: 0022-040X,1945-743X. URL: http://projecteuclid.org/euclid.jdg/1214432419.
\item[] [Ize95] Hiroyasu Izeki. "Limit sets of Kleinian groups and conformally flat Riemannian manifolds". In: Invent. Math. 122.3 (1995), pp. 603-625. ISSN: 0020-9910,1432-1297. DOI: 10.1007/BF01231457. URL: https://doi.org/10.1007/BF01231457.
\end{itemize}
\begin{itemize}
\item[] [Kob85] Osamu Kobayashi. "On a conformally invariant functional of the space of Riemannian metrics". In: J. Math. Soc. Japan 37.3 (1985), pp. 373-389. issn: 0025-5645,1881-1167. doi: 10.2969/jmsj/03730373. URL: https://doi.org/10.2969/jmsj/03730373.
\item[] [Kot98] D. Kotschick. "Einstein metrics and smooth structures". In: Geom. Topol. 2 (1998), pp. 1-10. ISSN: 1465-3060,1364-0380. DOI: 10.2140/gt.1998.2.1. URL: https://doi.org/10.2140/gt.1998.2.1.
\item[] [KS01] A. Kovalev and M. Singer. "Gluing theorems for complete anti-self-dual spaces". In: Geom. Funct. Anal. 11.6 (2001), pp. 1229-1281. ISSN: 1016-443X,1420-8970. DOI: 10.1007/s00039-001-8230-8. URL: https://doi.org/10.1007/s00039-001-8230-8.
\item[] [Kui49] N. H. Kuiper. "On conformally-flat spaces in the large". In: Ann. of Math. (2) 50 (1949), pp. 916-924. ISSN: 0003-486X. DOI: 10.2307/1969587. URL: https://doi.org/10.2307/1969587.
\item[] [LeB96] Claude LeBrun. "Four-manifolds without Einstein metrics". In: Math. Res. Lett. 3.2 (1996), pp. 133-147. ISSN: 1073-2780. DOI: 10.4310/MRL.1996.v3.n2.a1. URL: https://doi.org/10.4310/MRL.1996.v3.n2.a1.
\item[] [LeB03] Claude LeBrun. "Einstein metrics, four-manifolds, and differential topology". In: Surveys in differential geometry, Vol. VIII (Boston, MA, 2002). Vol. 8. Surv. Differ. Geom. Int. Press, Somerville, MA, 2003, pp. 235-255. ISBN: 1-57146-114-0. DOI: 10.4310/SDG.2003.v8.n1.a8. URL: https://doi.org/10.4310/SDG.2003.v8.n1.a8.
\item[] [LS94] Claude LeBrun and Michael Singer. "A Kummer-type construction of self-dual 4-manifolds". In: Math. Ann. 300.1 (1994), pp. 165-180. ISSN: 0025-5831,1432-1807. DOI: 10. 1007 / BF01450482. URL: https://doi.org/10.1007/BF01450482.
\item[] [MM25] Andrea Malchiodi and Francesco Malizia. Weyl energy and connected sums of four-manifolds. 2025. arXiv: 2505.17752 [math.DG]. URL: https://arxiv.org/abs/2505.17752.
\item[] [Ozu24] Tristan Ozuch. "Integrability of Einstein deformations and desingularizations". In: Comm. Pure Appl. Math. 77.1 (2024), pp. 177-220. ISSN: 0010-3640,1097-0312. doi: 10.1002/cpa. 22129. URL: https://doi.org/10.1002/cpa.22129.
\item[] [Pag78] Don Page. "A physical picture of the K3 gravitational instanton". In: Physics Letters B 80.1 (1978), pp. 55-57. ISSN: 0370-2693. DOI: https://doi.org/10.1016/0370-2693(78)90305-2. URL: https://www.sciencedirect.com/science/article/pii/0370269378903052.
\item[] [SY88] R. Schoen and S.-T. Yau. "Conformally flat manifolds, Kleinian groups and scalar curvature". In: Invent. Math. 92.1 (1988), pp. 47-71. ISSN: 0020-9910,1432-1297. DOI: 10.1007/BF01393992. URL: https://doi.org/10.1007/BF01393992.
\item[] [Sch84] Richard Schoen. "Conformal deformation of a Riemannian metric to constant scalar curvature". In: J. Differential Geom. 20.2 (1984), pp. 479-495. issn: 0022-040X,1945-743X. url: http://projecteuclid.org/euclid.jdg/1214439291.
\item[] [Sim86] Leon Simon. "Existence of Willmore surfaces". In: Miniconference on geometry and partial differential equations (Canberra, 1985). Vol. 10. Proc. Centre Math. Anal. Austral. Nat. Univ. Austral. Nat. Univ., Canberra, 1986, pp. 187-216. ISBN: 0-86784-511-2.
\item[] [Sim93] Leon Simon. "Existence of surfaces minimizing the Willmore functional". In: Comm. Anal. Geom. 1.2 (1993), pp. 281-326. ISSN: 1019-8385,1944-9992. DOI: 10.4310/CAG.1993.v1.n2. a4. URL: https://doi.org/10.4310/CAG.1993.v1.n2.a4.
\item[] [Str10] Jeffrey Streets. "Asymptotic curvature decay and removal of singularities of Bach-flat metrics". In: Trans. Amer. Math. Soc. 362.3 (2010), pp. 1301-1324. ISSN: 0002-9947,1088-6850. doi: 10.1090/S0002-9947-09-04960-5. URL: https://doi.org/10.1090/S0002-9947-09-04960-5.
\end{itemize}
\begin{itemize}
\item[] [Tau92] Clifford Henry Taubes. "The existence of anti-self-dual conformal structures". In: J. Differential Geom. 36.1 (1992), pp. 163-253. ISSN: 0022-040X,1945-743X. url: http://projecteuclid.org/euclid.jdg/1214448445.
\item[] [Tho69] John A. Thorpe. "Some remarks on the Gauss-Bonnet integral". In: J. Math. Mech. 18 (1969), pp. 779-786.
\item[] [TV05a] Gang Tian and Jeff Viaclovsky. "Bach-flat asymptotically locally Euclidean metrics". In: Invent. Math. 160.2 (2005), pp. 357-415. ISSN: 0020-9910,1432-1297. DOI: 10.1007/s00222-004-0412-1. URL: https://doi.org/10.1007/s00222-004-0412-1.
\item[] [TV05b] Gang Tian and Jeff Viaclovsky. "Moduli spaces of critical Riemannian metrics in dimension four". In: Adv. Math. 196.2 (2005), pp. 346-372. ISSN: 0001-8708,1090-2082. doi: 10.1016/j.aim.2004.09.004. URL: https://doi.org/10.1016/j.aim.2004.09.004.
\item[] [TV08] Gang Tian and Jeff Viaclovsky. "Volume growth, curvature decay, and critical metrics". In: Comment. Math. Helv. 83.4 (2008), pp. 889-911. ISSN: 0010-2571,1420-8946. DOI: 10.4171/CMH/147. URL: https://doi.org/10.4171/CMH/147.
\item[] [Top87] P. Topiwala. "A new proof of the existence of Kähler-Einstein metrics on K3. I, II". In: Invent. Math. 89.2 (1987), pp. 425-448, 449-454. ISSN: 0020-9910,1432-1297. DOI: 10.1007/BF01389087. URL: https://doi.org/10.1007/BF01389087.
\item[] [Via16] Jeff A. Viaclovsky. "Critical metrics for Riemannian curvature functionals". In: Geometric analysis. Vol. 22. IAS/Park City Math. Ser. Amer. Math. Soc., Providence, RI, 2016, pp. 197-274. ISBN: 978-1-4704-2313-1. DOI: 10.1090/pcms/022/05. URL: https://doi.org/10.1090/pcms/022/05.
\item[] [WY25] Bing Wang and Hao Yin. Curvature at the infinity of asymptotically flat Einstein manifold. 2025. arXiv: 2508.16288 [math.DG]. URL: https://arxiv.org/abs/2508.16288.
\item[] [Wan25] Xiaokang Wang. On the structure of locally conformally flat orbifolds and ALE manifolds. 2025. arXiv: 2511.09857 [math.DG]. URL: https://arxiv.org/abs/2511.09857.
\item[] [Zie89] William P. Ziemer. Weakly differentiable functions. Vol. 120. Graduate Texts in Mathematics. Sobolev spaces and functions of bounded variation. Springer-Verlag, New York, 1989, pp. xvi+308. ISBN: 0-387-97017-7. DOI: 10.1007/978-1-4612-1015-3. URL: https://doi.org/10.1007/978-1-4612-1015-3.
\end{itemize}

Andrea Malchiodi
Scuola Normale Superiore, Piazza dei Cavalieri 7, 56126 Pisa, Italy
E-mail address: andrea.malchiodi@sns.it
Francesco Malizia
Scuola Normale Superiore, Piazza dei Cavalieri 7, 56126 Pisa, Italy
E-mail address: francesco.malizia@sns.it
