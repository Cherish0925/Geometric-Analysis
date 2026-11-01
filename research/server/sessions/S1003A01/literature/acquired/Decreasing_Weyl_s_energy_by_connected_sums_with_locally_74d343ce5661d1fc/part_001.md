---
retention_scope: session
part: 1
total_parts: 3
---

[Part 1/3 of: Decreasing Weyl's energy by connected sums with locally ...]

---
source_file: 2604_17547v1.pdf
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
We study the Weyl functional on connected sums of two four-dimensional manifolds $\left(M, g_{M}\right)$ and $\left(Z, g_{Z}\right)$, assuming $g_{M}$ is Bach-flat and $g_{Z}$ locally conformally flat. We show that if $g_{M}$ is neither self-dual nor anti self-dual and if $g_{Z}$ is of positive Yamabe class, there exists a metric $g_{Y}$ on $Y:=M \# Z$ with Weyl energy lower than that of $g_{M}$ (with the trivial exception of $\left.\left(Z, g_{Z}\right)=\left(\mathbb{S}^{4}, g_{\mathbb{S}^{4}}\right)\right)$. This result has a relation to a conjecture by I.Singer and has a perspective application to the minimization of Weyl's energy. The proof relies on a simultaneous interplay of $W_{M}^{+}, W_{M}^{-}$and the topology of $Z$, and also covers some orbifold cases.
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
$$B_{i j}:=-4\left(\nabla^{\alpha} \nabla^{\beta} W_{\alpha i j \beta}+\frac{1}{2} R^{\alpha \beta} W_{\alpha i j \beta}\right)=0,$$
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
Remark 1.2. (a) If $\left(Z, g_{Z}\right)=\left(\mathbb{S}^{4}, g_{\mathbb{S}^{4}}\right)$, the connected sum $Y$ would have trivially the topology of $M$, and an optimal choice of $g_{Y}$ would just be $g_{M}$. We recall that, by a result of Kuiper [Kui49], the sphere is the only locally conformally flat manifold that is simply connected, up to conformal diffeomorphisms. In our proof, as discussed below, we exploit the developing map in order to distinguish the round sphere from any other locally conformally flat manifold of positive Yamabe class, just like the $A D M$ mass does. Also, as noted before, if Singer's conjecture is true and $M$ is of positive Yamabe class, for (1.7) to hold one needs both $W_{+}^{M}$ and $W_{-}^{M}$ to be non zero somewhere. Therefore, we need to use crucially an interplay among $W_{M}^{+}, W_{M}^{-}$and the topology of $Z$ at the same time to diffuse efficiently Weyl energy from $M$ into $Z$.
\begin{itemize}
\item[(b)] We are assuming both $M$ and $Z$ to be Bach-flat. If one of them is not, it is very easy to construct a metric on $Y$ as in (1.7), modifying first either $g_{M}$ or $g_{Z}$.
\item[(c)] For Willmore surfaces in $\mathbb{R}^{n}$ the counterpart of local conformal flatness would be umbilicity, but in this case one has rigidity and the corresponding surface would be a round sphere.
\end{itemize}

In view of the applications to the minimization of Weyl's energy, discussed at the end of this introduction, we expect Theorem 1.1 to be most relevant in positive Yamabe class, where one controls the Sobolev inequality, in turn useful to avoid collapsing. It would be interesting to investigate the cases in which $Z$ has zero or negative scalar curvature.

As we remarked before, under the assumptions of Theorem 1.1 the main interaction term in (1.5) vanishes identically, and therefore we need a more precise choice of the metric and a finer expansion of Weyl's energy. To give a more precise idea of our procedure, we focus first on the locally conformally flat manifold $Z$, where near $q$ we can assume that the metric is flat, by the conformal invariance of the problem. Identifying $T_{p} \bar{M}$ and $T_{q} Z$ and denoting by $x$ normal coordinates centered at $q$, we can also use $x$ as inverted normal coordinates on $T_{p} M$ (after a proper dilation).

Denoting by $\tilde{g}_{M}$ the conformal blow-up of $g_{M}$, we have the expansion
$$\tilde{g}_{M} \simeq\left(\delta_{i j}+\tau W_{\mu i j \nu}^{\bar{M}} \frac{x^{\mu} x^{\nu}}{|x|^{4}}\right) d x^{i} d x^{j} \quad \text { for } x \simeq 0, x \neq 0$$
where $\tau>0$ is a small coefficient.

At this point, to match the two metrics across the gluing region, one needs to find a correction $\tau F$ to $g_{Z}$ with $F \simeq W_{\mu i j \nu}^{\bar{M}} \frac{x^{\mu} x^{\nu}}{|x|^{4}} d x^{i} d x^{j}$ near $q$. Moreover, it is clearly convenient to keep the metric on $Z$ as Bach-flat as possible, and therefore it is also natural to look for a correction that solves
$$\dot{B}_{g_{Z}}(F)=0 \quad \text { on } Z \backslash\{q\} .$$
This is reminiscent of other gluing constructions, and in particular to the one in [Sch84], where for the (scalar) Yamabe equation a highly concentrated bubble profile was attached to a suitable multiple of the Green's function of the conformal Laplacian, with pole at the location of the bubble. In particular, by the symmetries of $W$, in case $\left(Z, g_{Z}\right)=\left(\mathbb{S}^{4}, g_{\mathbb{S}^{4}}\right)$ this would be a global and transverse-traceless (TT) solution to (1.8) expressed in stereographic coordinates at $-q$.

Since on $\mathbb{R}^{4}$ the linearized Bach operator coincides with the bi-Laplacian on TT tensors, to have a solution $F$ as desired one can try to solve a distributional equation like
$$\dot{B}_{g_{Z}}(F)=W_{\mu i j \nu}^{\bar{M}} \nabla^{\mu} \nabla^{\nu} \delta_{q} d x^{i} d x^{j} \quad \text { on } Z,$$
where $\delta_{q}$ stands for the Dirac delta at $q$. Such an equation can be solved by abstract means (up to Lagrange multipliers), yielding a solution of the type
$$F=\left(W_{\mu i j \nu}^{\bar{M}} \frac{x^{\mu} x^{\nu}}{|x|^{4}}+A_{i j}(x)\right) d x^{i} d x^{j} \quad \text { near } q$$
and the prospect is that the extra term $A_{i j}$ might have a role in the expansion of Weyl's energy on $Y$.
While there is in general no hope to control the reminder term $A_{i j}$ with an abstract approach, the advantage of working with a locally conformally flat metric on $Z$ is that one can pass to the universal cover $\tilde{Z}$ of $Z$ and use the developing map $\Phi: \tilde{Z} \rightarrow \mathbb{S}^{4}$, which turns out to be injective in positive Yamabe class, see [SY88]. Here, the latter property allowed to prove positivity of the ADM mass of (non spherical) locally conformally flat manifolds by roughly writing the lift to $\tilde{Z}$ of the Green's function of the conformal Laplacian on $Z$ as a multi-pole singular solution.

The hope in the present situation is to use a similar strategy, in order to write $A_{i j}$ via a formal series expansion. In fact, one could start from the above solution on $\mathbb{S}^{4}$, use the conformal covariance of $\dot{B}$ and in a first attempt sum over all pull-backs via deck transformations of $\tilde{Z}$, as in (3.8). If this would converge, one might project such tensor onto $Z$ and find the metric perturbation $F$ as desired.

A model case one can consider is the product $\mathbb{S}_{t}^{1} \times \mathbb{S}^{3}$, with $\mathbb{S}_{t}^{1}$ standing for the circle of length $\log t, t>1$. The universal cover is $\mathbb{R}^{4} \backslash\{0\}$ (or $\mathbb{S}^{4}$ with two antipodal points removed) and the deck transformation group is isomorphic to $\mathbb{Z}$. Proceeding as described above, from (3.8) we obtain the expression for $\tilde{A}$ given by (3.11), see Section 3.1.1. Unfortunately, the series constructed in this way does not converge: since however the kernel of the linearized Bach operator contains all Lie derivatives, as a second attempt we modify each summand in the series by a non-TT element, allowing to solve the convergence problem, see the discussion before Lemma 3.3. We then obtain a solution of (1.8) that behaves as in (1.9).

Since we modified the metric on $Z$, which was locally flat, by a term like (1.9), in order to properly glue the new metric on $M$ we need to adjust $g_{M}$ in order to match the extra term $A$. If $y=\frac{x}{|x|^{2}}$ (with $x$ coordinates as before) are normal coordinates at $p \in M$, we need to add a suitable multiple of a correction $H$ that behaves like
$$H \simeq \frac{1}{2} \nabla_{\mu \nu}^{2} A_{i j}(0) x^{\mu} x^{\nu} d x^{i} d x^{j} \quad \text { near } p$$
Using integration by parts and some delicate expansions, we see that the correction to Weyl's energy (compared to $\mathcal{W}\left(g_{M}\right)$ ) for the connected sum $Y$ with metric profiles as described above is proportional
to $-W_{\bar{M}}^{k i j l} \nabla_{k l}^{2} A_{i j}$, so qualitatively $\nabla^{2} A$ plays the role of a tensorial mass that couples to the Weyl's tensor of $M$. After a direct calculation, for $Z=\mathbb{S}_{t}^{1} \times \mathbb{S}^{3}$ the term $W_{\bar{M}}^{k i j l} \nabla_{k l}^{2} A_{i j}$ becomes of the type
$$F(t) W^{M}(p) \circledast W^{\bar{M}}(p)$$
where $F(t)$ depends on the length of $\mathbb{S}_{t}^{1}$, see Section 6.2 for details. Qualitatively, $F(t)$, which is positive, behaves with respect to $t$ like the ADM mass of $Z=\mathbb{S}_{t}^{1} \times \mathbb{S}^{3}$, see Remark 3.5 (and in particular blows-up as $t \rightarrow 1^{+}$). Therefore, we get the desired comparison for the Weyl energies of $g_{Y}$ and $g_{M}$ whenever the interaction (1.10) is positive, which can be always achieved provided $M$ is not self-dual or anti self-dual.

Before discussing the case of a general $Z$, we comment on an aspect of the above gluing procedure that we find relevant. In order to perform a proper matching, we need to modify $g_{Z}$ so that the tensor $A_{i j}$ vanishes at $q$ together with its gradient and so that the term $W^{k i j l} \nabla_{k l}^{2} A_{i j}$ is not affected by this change. To prove this fact we again employ a translational gauge (i.e., we add a Lie derivative), which also allows us to project the hessian of $A$ on symmetrized curvature tensors and streamline many computations. This is analogous to the construction of normal coordinates by iterated polynomial change of variables, see Section 4 in [WY25].

We next turn to the case of a general locally conformally flat manifold $\left(Z, g_{Z}\right)$ of positive Yamabe class. By a result in [CTZ12] (which completes the work in [Ham97], [Ize95]), all such manifolds are diffeomorphic to connected sums of compact quotients of $\mathbb{S}^{1} \times \mathbb{S}^{3}$. We exploit this information by choosing a special family of metrics on $Z$ which will lead to the same conclusions as above. First, fixing one of the summands as just described, we take the corresponding parameter $t$ to be sufficiently close to 1 , in order to obtain a strong interaction term in (1.10) (i.e., $F(t)$ will be large). One can prove, see Proposition 3.10, that even passing to quotients, the interaction term $W^{k i j l} \nabla_{k l}^{2} A_{i j}$ stays positive. Taking connected sums with other quotients of this type, we choose sufficiently small necks, in order to obtain an interaction term very close to the original one, for capacity reasons, see Proposition 6.7.

Remark 1.3. Instead of working with a glued manifold $Y \cong Z \# M$, it will be easier in the next sections to perform a simpler gluing and consider $X \cong Z \# \bar{M}$. This does not create any issue, as in the end it will be sufficient to perform the same procedure with $\bar{M}$ replacing $M$, see Remark 6.1.

Theorem 1.1 can be extended to some orbifold settings:
Theorem 1.4. Let $\left(M, g_{M}\right),\left(Z, g_{Z}\right)$ be two four-dimensional closed, connected, oriented orbifolds. Assume that $g_{M}$ is Bach-flat and that $g_{Z}$ is locally conformally flat and with positive scalar curvature. Let $p \in M$ and $q \in Z$ be orbifold points, both with group $\Gamma \subset \operatorname{SO}(4)$, and denote by $Y:=Z \# M$ the orbifold connected sum at $p, q$. Assume that the Weyl tensor of $g_{M}$ at $p$ is neither self-dual nor anti-self-dual. Then, in case $\left(Z, g_{Z}\right)$ is not globally conformal to the round sphere or a football orbifold $\left(\mathbb{S}^{4} / \Gamma, g_{\mathbb{S}^{4} / \Gamma}\right)$, there exists a metric $g_{Y}$ on $Y$ such that
$$\mathcal{W}^{Y}\left(g_{Y}\right)<\mathcal{W}^{M}\left(g_{M}\right) .$$

We refer to Section 6.4 for the proof and the definitions of orbifolds and orbifold connected sums. The proof of Theorem 1.4 follows along the same lines of that of Theorem 1.1; indeed, by the results in [CTZ12], [Wan25] we have a classification of locally conformally flat orbifolds with positive scalar curvature, Theorem 6.9, which is similar to that of their smooth counterpart. In particular, these orbifolds are all finitely covered by a connected sum of $\mathbb{S}^{1} \times \mathbb{S}^{3}$ 's (with the difference that the group action this time is not fixed point free, hence the cover is branched), so we can repeat the same construction outlined above even in this setting.

This is important for what we believe to be one of the principal perspective applications of these gluing results, that is, to the blow-up analysis of (suitable) minimizing sequences for the Weyl energy, which will be briefly described next.

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
Using (3.9) (with $\bar{\xi}$ in place of $\bar{h}$ ), (3.10) and the definition of $\bar{\xi}$, we see that, for $y \sim-e_{4}$, there holds
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

Claim. Any $\gamma \in N$ is a composition of translations and rotations by a matrix $O \in \operatorname{SO}(4)$.
Proof. Since we are assuming that the quotient $Z$ is oriented, it is known that the action of each element $\gamma \in N$ must be orientation-preserving. This automatically excludes maps which act on $\left([-R / 2, R / 2] \times \mathbb{S}^{3}\right) / \sim$ as an inversion (plus translation) on the first factor and as a rotation in SO(4) on the second factor, as well as maps acting as a translation on the first factor and as a rotation in $\mathrm{O}(4) \backslash \mathrm{SO}(4)$ in the second one (as they are both orientation-reversing). Finally, let us consider maps in which we have an inversion on the first factor and a rotation $O \in \mathrm{O}(4) \backslash \mathrm{SO}(4)$ in the second one, namely $\gamma \in N$ satisfies
$$\gamma(r, w)=(L-r, O(w)),$$
for $|L| \leq r / 2$. Since $\operatorname{det}(O)=-1$, one has
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

Lemma 3.8. Let us write, for $y \sim-e_{4}$,
$$\bar{T}_{i j}=-\frac{1}{3} W_{\mu i j \nu} \frac{\left(y+e_{4}\right)^{\mu}\left(y+e_{4}\right)^{\nu}}{\left|y+e_{4}\right|^{4}}+\bar{A}_{i j}(y),$$
where $\bar{T}$ is given by (3.33). Then $\bar{A}_{i j}(y)$ is TT for $y$ close to $-e_{4}$, and one further has
$$\bar{A}\left(-e_{4}\right)=0, \quad \nabla \bar{A}\left(-e_{4}\right)=0,$$
$$\begin{aligned}
\partial_{k l}^{2} \bar{A}_{i j}\left(-e_{4}\right)=-\frac{1}{3} C_{2}(t)[ & \left(W_{k i j l}+W_{l i j k}\right)-4 \delta_{4 k}\left(W_{l i j 4}+W_{4 i j l}\right)-4 \delta_{4 l}\left(W_{k i j 4}+W_{4 i j k}\right) \\
& \left.-4 \delta_{k l} W_{4 i j 4}+24 \delta_{4 k} \delta_{4 l} W_{4 i j 4}\right]+O\left((t-1)^{-1}\right), \quad \text { as } t \rightarrow 1^{+} .
\end{aligned}$$
Here $C_{2}(t)$ is given by (3.19); in particular,
$$C_{2}(t)=\frac{\pi^{4}}{45(t-1)^{4}}+O\left((t-1)^{-3}\right), \quad \text { as } t \rightarrow 1^{+} .$$

Remark 3.9. Differently from the case of $\mathbb{S}^{1} \times \mathbb{S}^{3}$ (see Lemma 3.3), here we do not have an exact (useful) identity for the hessian of $\bar{A}$. However, by letting $t \rightarrow 1^{+}$(that is, by shrinking the length $R$ of the cylinder to zero), we see that the leading term in the hessian is again given by the quantity appearing in (3.18). This is motivated by the fact that, differently from the poles coming from pure dilations, the poles of $\bar{T}$ coming from dilations and rotations do not accumulate toward $-e_{4}$ as $t \rightarrow 1^{+}$.

Proof. The identities (3.34) and the fact that $\bar{A}$ is TT directly follow by construction, see (3.29), (3.30), (3.31), (3.33).