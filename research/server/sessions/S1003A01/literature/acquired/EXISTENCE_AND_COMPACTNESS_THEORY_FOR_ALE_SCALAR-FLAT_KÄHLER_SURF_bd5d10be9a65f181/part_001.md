---
retention_scope: session
part: 1
total_parts: 3
---

[Part 1/3 of: EXISTENCE AND COMPACTNESS THEORY FOR ALE SCALAR-FLAT KÄHLER SURFACES]

---
source_file: EXISTENCE_AND_COMPACTNESS_THEORY_FOR_ALE_SCALAR-FLAT_KÄHLER_SURFACES_4a0d25bd9db4.pdf
converter: mathpix
format: mmd
---

\title{
EXISTENCE AND COMPACTNESS THEORY FOR ALE SCALAR-FLAT KÄHLER SURFACES
}

\author{
JIYUAN HAN ${ }^{1}$ and JEFF A. VIACLOVSKY ${ }^{2}$ \\ ${ }^{1}$ Department of Mathematics, Purdue University, West Lafayette, IN, 47907, USA; email: han556@purdue.edu \\ ${ }^{2}$ Department of Mathematics, University of California, Irvine, CA, 92697, USA; email: jviaclov@uci.edu
}

Received 18 April 2019; accepted 4 November 2019

\begin{abstract}
Our main result in this article is a compactness result which states that a noncollapsed sequence of asymptotically locally Euclidean (ALE) scalar-flat Kähler metrics on a minimal Kähler surface whose Kähler classes stay in a compact subset of the interior of the Kähler cone must have a convergent subsequence. As an application, we prove the existence of global moduli spaces of scalar-flat Kähler ALE metrics for several infinite families of Kähler ALE spaces.
\end{abstract}

2010 Mathematics Subject Classification: 53C55 (primary); 53C25 (secondary)

\section*{Contents}
1 Introduction ..... 2
2 Preliminaries ..... 8
3 Compactness I. Convergence of birational structure ..... 20
4 Compactness II. The limit is birationally dominated by $X$ ..... 32
5 Compactness III. Bubbles are resolutions ..... 38
6 Existence results ..... 45

\section*{7 Examples}

\section*{8 Conclusion}

\section*{References}

\section*{1. Introduction}

Definition 1.1. An ALE Kähler surface ( $X, g, J$ ) is a Kähler manifold of complex dimension 2 with the following property. There exists a compact subset $K \subset X$ and a diffeomorphism $\Psi: X \backslash K \rightarrow\left(\mathbb{R}^{4} \backslash \bar{B}\right) / \Gamma$, such that for each multi-index $\mathcal{I}$ of order $|\mathcal{I}|$
$$\partial^{\mathcal{I}}\left(\Psi_{*}(g)-g_{\mathrm{Euc}}\right)=O\left(r^{-\mu-|\mathcal{I}|}\right),$$
as $r \rightarrow \infty$, where $\Gamma$ is a finite subgroup of U(2) containing no complex reflections, $B$ denotes a ball centered at the origin, and $g_{\text {Euc }}$ denotes the Euclidean metric. The real number $\mu$ is called the order of $g$.

REMARK 1.2. In this paper, henceforth $\Gamma$ will always be a finite subgroup of U(2) containing no complex reflections.

Any ALE Kähler surface can be blown down to a smooth minimal complex surface in its birational class, minimal in the sense that there is no rational curve of self-intersection -1. Our interest lies in building canonical metrics on minimal ALE Kähler surfaces. Specifically, we are interested in constructing a smooth family of ALE SFK (scalar-flat Kähler) metrics that corresponding to the versal deformation family of $\mathbb{C}^{2} / \Gamma$. Before we discuss existence results, we present our main theorem in this paper, which is a compactness result.

In the following, if $(X, g)$ is an ALE metric and $\varphi$ is a smooth tensor of any type, we say that $\varphi \in C_{\delta}^{\infty}(X, g)$ if $\phi$ is smooth and $\nabla_{g}^{\mathcal{I}} \varphi=O\left(r^{\delta-|\mathcal{I}|}\right)$ as $r \rightarrow \infty$, where $\mathcal{I}$ is any multi-index of length $|\mathcal{I}|$.

Definition 1.3. Let ( $X, J$ ) be a Kähler surface with a smooth ALE Kähler metric $g_{0}$, with Kähler form $\omega_{0}$. For $-2<\delta_{0}<-1$, define
$$\mathcal{P}\left(X, J, \omega_{0}, \delta_{0}\right)=\left\{\omega \mid \omega \text { is Kähler form satisfying } \omega-\omega_{0} \in C_{\delta_{0}}^{\infty}\left(X, g_{0}\right)\right\} .$$
The Kähler cone of ( $X, J$ ) with respect to $\omega_{0}$ and $\delta_{0}$ is
$$\mathcal{K}\left(X, J, \omega_{0}, \delta_{0}\right):=\left\{[\omega] \mid \omega \in \mathcal{P}\left(X, J, \omega_{0}, \delta_{0}\right)\right\},$$
where $[\omega]$ denotes the class of $\omega$ in $H^{2}(X, \mathbb{R})$.

Clearly, $\mathcal{K}\left(X, J, \omega_{0}, \delta_{0}\right)$ is a convex subspace in the de Rham cohomology group $H^{2}(X, \mathbb{R})$. We remark that if $J$ is Stein, then $\mathcal{K}\left(X, J, \omega_{0}, \delta_{0}\right)$ is the entire space $H^{2}(X, \mathbb{R})$, but if there exist any holomorphic curves, then it is a proper subset. This is because the integral of the Kähler form over a holomorphic curve must be strictly positive since it is the area, but if there are no holomorphic curves, then there are no constraints. See the discussion in Remark 6.1 for details.

Definition 1.4. The lower volume growth ratio of $(X, g)$ is
$$\mathcal{V}(g) \equiv \inf _{x \in X} \inf _{0<r<1} \frac{\operatorname{Vol}\left(B_{r}(x, g)\right)}{r^{4}} .$$

The following is our main compactness theorem dealing with sequences of ALE SFK metrics with respect to a fixed complex structure.

Theorem 1.5. Let $\left(X, J, g_{0}\right)$ be an ALE minimal Kähler surface, associated with an ALE coordinate of asymptotic rate $O\left(r^{\delta_{0}}\right),\left(-2<\delta_{0}<-1\right)$. Let $\kappa_{i} \in$ $\mathcal{K}\left(X, J, \omega_{0}, \delta_{0}\right)$ be a sequence with $\kappa_{i} \rightarrow \kappa_{\infty} \in \mathcal{K}\left(X, J, \omega_{0}, \delta_{0}\right)$ as $i \rightarrow \infty$. If $g_{i}$ is a sequence of ALE SFK metrics with $\omega_{i} \in \mathcal{P}\left(X, J, \omega_{0}, \delta_{0}\right)$ satisfying:
(1) $\left[\omega_{i}\right]=\kappa_{i}$;
(2) there exists a constant $v>0$, independent of $i$, such that $\mathcal{V}\left(g_{i}\right)>v$;
then there exists a subsequence $\{j\} \subset\{i\}$ and $\omega_{\infty} \in \mathcal{P}\left(X, J, \omega_{0}, \delta_{0}\right)$ such that $\omega_{j} \rightarrow \omega_{\infty}$ in $C_{\delta_{0}}^{k, \alpha}\left(X, g_{0}\right)$ norm for any $k \geqslant 0,0<\alpha<1$, as $j \rightarrow \infty$, where $g_{\infty}$ is an ALE SFK metric satisfying $\left[\omega_{\infty}\right]=\kappa_{\infty}$.

For the definition of the weighted norm, see Section 2.1 below. A brief outline of the proof of Theorem 1.5 is follows. First, we apply the compactness result of Tian and Viaclovsky [TV05b] to obtain an ALE SFK orbifold limit $X_{\infty}$, in the pointed Cheeger-Gromov sense. In Section 3, we also show that the limit $X_{\infty}$ is birationally equivalent to $(X, J)$. Then, in Section 4, we show that the limit space $X_{\infty}$ is moreover birationally dominated by $X$, that is, $X_{\infty}$ is a blowdown of $X$. The key point in this step is to show that there are no (-1) curves in the minimal resolution of $X_{\infty}$, the proof of which uses crucially the minimality assumption on $X$. Then in Section 5, using some key results of Lempert, we show that in the 'bubble tree' of each orbifold singularity in the limit space, each bubble is biholomorphic to a resolution of an orbifold singularity in the previous bubble. This, together with a result of Laufer, implies the area contraction of a holomorphic curve, which contradicts with the nondegeneracy of the limiting Kähler class, and therefore the limit space must be a smooth ALE SFK metric.

We remark that Theorem 1.5 in some sense can be viewed as a noncompact analogue of the main result in [CLW08].

Definition 1.6. For $\left(X, J, g_{0}\right)$ an ALE SFK Kähler surface, let
$$\mathcal{V}(\mathcal{P}(J))=\inf _{\substack{g \in \mathcal{P}(J) \\ R_{g}=0}} \mathcal{V}(g),$$
where $\mathcal{P}(J)=\mathcal{P}\left(X, J, \omega_{0}, \delta_{0}\right)$.
Our main existence result is the following.
Corollary 1.7. Let $\left(X, J, g_{0}\right)$ be as in Theorem 1.5, and assume that $g_{0}$ is $S F K$. If
$$\mathcal{V}(\mathcal{P}(J))>0,$$
then for any $\kappa \in \mathcal{K}\left(X, J, \omega_{0}, \delta_{0}\right)$, there exists an ALE SFK metric $\omega \in \mathcal{P}(J)$ with $[\omega]=\kappa$.

This theorem is proved by using the continuity method. Openness in the continuity method follows from the same method in [HV16, Section 8]. Closedness follows from Theorem 1.5.

Remark 1.8. The family of ALE SFK metrics constructed by the continuity method depends upon the initial metric we choose, but otherwise does not depend upon the specific value of $\delta_{0}$ for $-2<\delta_{0}<-1$.

Remark 1.9. In certain examples, we can prove the noncollapsing condition required in Corollary 1.7 by using a topological argument; we discuss these examples in Section 1.2 below.
1.1. General existence results. In order to state our next result, we need to recall some theory regarding the deformations of $\mathbb{C}^{2} / \Gamma$. By a classical theorem of Grauert [Gra72] (and see [Elk74] for the algebraic version), there exists a (mini)versal deformation $\mathcal{Y} \rightarrow \operatorname{Der}\left(\mathcal{Y}_{0}\right)$ of $\mathbb{C}^{2} / \Gamma$, such that any deformation of $\mathbb{C}^{2} / \Gamma$ over a complex space germ can be obtained by a pullback morphism from the versal deformation, on the level of germs (see [GLS07] for the complete definition of versality). Furthermore, there is a natural $\mathbb{C}^{*}$-action on $\operatorname{Der}\left(\mathcal{Y}_{0}\right)$, which lifts to a $\mathbb{C}^{*}$-action on $\mathcal{Y}$ (which is of negative weight, see [Pin78, Section 2]). The complex space germ $\operatorname{Der}\left(\mathcal{Y}_{0}\right)$ can be reducible in general.

Let $r+1$ denote the number of irreducible components, and denote each irreducible component by $\operatorname{Der}_{k}\left(\mathcal{Y}_{0}\right), k \in\{0, \ldots, r\}$. By [KSB88, BC94], for each irreducible component, there exists a unique $P$-resolution $Z_{k}^{P} \rightarrow \mathcal{Y}_{0}$, a unique $M$-resolution $Z_{k}^{M} \rightarrow Z_{k}^{P}$, and finite base changes $\operatorname{Der}^{\prime}\left(Z_{k}^{M}\right) \rightarrow \operatorname{Der}^{\prime}\left(Z_{k}^{P}\right) \rightarrow$ $\operatorname{Der}_{k}\left(\mathcal{Y}_{0}\right)$. Using the $\mathbb{C}^{*}$-action, we can extend $\operatorname{Der}^{\prime}\left(Z_{k}^{M}\right), \operatorname{Der}^{\prime}\left(Z_{k}^{P}\right), \operatorname{Der}_{k}\left(\mathcal{Y}_{0}\right)$ to global analytic spaces $\mathcal{J}_{k}^{M}, \mathcal{J}_{k}^{P}, \mathcal{J}_{k}$, which are bases spaces of deformations $\mathcal{X}_{k}$, $\mathcal{Z}_{k}, \mathcal{Y}_{k}$, respectively, and the total spaces admit $\mathbb{C}^{*}$-actions such that the following diagram is $\mathbb{C}^{*}$-equivariant
![](https://cdn.mathpix.com/cropped/9a120029-d3e2-4d90-8447-ba255e904003-05.jpg?height=178&width=406&top_left_y=543&top_left_x=524)
Define global base spaces
$$\mathcal{J}^{M}=\bigcup_{0 \leqslant k \leqslant r} \mathcal{J}_{k}^{M}, \quad \mathcal{J}^{P}=\bigcup_{0 \leqslant k \leqslant r} \mathcal{J}_{k}^{P}, \quad \mathcal{J}=\bigcup_{0 \leqslant k \leqslant r} \mathcal{J}_{k} .$$
Note that while $\mathcal{J}$ is connected, the spaces $\mathcal{J}^{P}, \mathcal{J}^{M}$ have $r+1$ connected components. We also note that $\mathcal{J}_{0}^{M}$ is the simultaneous resolution of the Artin component, up to a base change. Further details of this construction can be found in Section 2.3.

In a recent work of [HRŞ16], it is shown that any ALE Kähler surface is birationally equivalent to a deformation of $\mathbb{C}^{2} / \Gamma$. Their work indicates that the space of minimal ALE Kähler surfaces is essentially parameterized by $\operatorname{Der}\left(\mathcal{Y}_{0}\right)$. In Lemma 2.5 below, we show that any minimal ALE Kähler surface $(X, J)$ is biholomorphic to an element in $\mathcal{J}^{M}$. For this reason, it is reasonable to first restrict our attention to complex structures parameterized by the base space $\mathcal{J}^{M}$ (or $\mathcal{J}^{P}$ ).

Theorem 1.10. There exists a smooth family of background ALE Kähler metrics $\omega_{b, J}$, for all smooth fibers over $J \in \mathcal{J}^{M}$ (similarly for $J \in \mathcal{J}^{P}$ away from the discriminant locus).

This will be proved in Section 6 below. Our main interest is therefore in constructing ALE SFK metrics in these ALE Kähler classes. We emphasize that in all the following results, the Kähler cone is defined with respect to the background ALE Kähler metric $\omega_{b, J}$. Thus, in the following when there is no ambiguity, we abbreviate $\mathcal{P}\left(X, J, \omega_{b, J}, \delta_{0}\right)$ and $\mathcal{K}\left(X, J, \omega_{b, J}, \delta_{0}\right)$ as $\mathcal{P}(J)$ and $\mathcal{K}(J)$, respectively.

Recall from above that for each irreducible component $\mathcal{J}_{k}$ in the moduli space $\mathcal{J}$ associated to the versal deformation of $\mathbb{C}^{2} / \Gamma$, there corresponds a $P$-resolution
$Z_{k}^{P}$ and a $M$-resolution $Z_{k}^{M}$. The space $Z_{k}^{P}$ is an orbifold with singularities of type $T$, and the space $Z_{k}^{M}$ is an orbifold with only type $T_{0}$ singularities.

THEOREM 1.11. Let $\mathcal{J}$ be the moduli space associated to the versal deformation of $\mathbb{C}^{2} / \Gamma$ as defined in the previous paragraphs. Let $\mathcal{J}_{k}$ be an irreducible component.
\begin{itemize}
\item[(a)] If $\mathcal{J}_{k}=\mathcal{J}_{0}$ is the Artin component, then for any complex structure $J \in \mathcal{J}_{0}^{M}$ there exists an ALE SFK metric in some Kähler class in $\mathcal{K}(J)$.
\item[(b)] For $k>0$, if there exists an ALE SFK orbifold metric on the orbifold $Z_{k}^{M}$, then for any complex structure $J \in \mathcal{J}_{k}^{M}$ away from the central fiber, there exists an ALE SFK metric in some Kähler class in $\mathcal{K}(J)$.
\item[(c)] For $k>0$, if there exists an ALE SFK orbifold metric on the orbifold $Z_{k}^{P}$, then for any complex structure $J \in \mathcal{J}_{k}^{P}$ away from the discriminant locus, there exists an ALE SFK metric for some Kähler class in $\mathcal{K}(J)$.
\end{itemize}

Case (a) follows easily from [HV16, Theorem 1.4]. Cases (b) and (c) are obtained by applying a generalization of a result of Biquard-Rollin to the ALE case [BR15]. For the precise statement, see Theorem 6.2 below.

Recall that for integers $p, q$ satisfying $(p, q)=1$, the cyclic action $\frac{1}{p}(1, q)$ is that generated by $\left(z_{1}, z_{2}\right) \mapsto\left(\zeta_{p} z_{1}, \zeta_{p}^{q} z_{2}\right)$, where $\zeta_{p}$ is a primitive $p$ th root of unity.

Corollary 1.12. Let $\Gamma=\frac{1}{p}(1, q)$ be any cyclic group with $(p, q)=1$, and let $\mathcal{J}_{k}^{M}$ be any component of $\mathcal{J}^{M}$. Then for any $J \in \mathcal{J}_{k}^{M}$ ( $J$ is away from the central fiber if $k>0$ ), there exists a scalar-flat Kähler metric $\omega_{J}$ in some Kähler class.

This is obtained by using the Calderbank-Singer construction from [CS04], together with Theorem 1.11.
1.2. Global existence results. We now turn our attention to existence of global moduli spaces of ALE SFK metrics for certain groups $\Gamma$. The following theorem is an application of Case (a) in Theorem 1.11 together with Corollary 1.7.

THEOREM 1.13. Let $\Gamma \subset \mathrm{U}(2)$ be any of the following groups:
$$\frac{1}{3}(1,1), \quad \frac{1}{5}(1,2), \quad \frac{1}{7}(1,3) .$$
Note that for these groups, the versal deformation space of $\mathbb{C}^{2} / \Gamma$ has only the Artin component $\mathcal{J}$, which has $b_{2}(X)=1,2,3$, respectively, where $b_{2}$ denotes
the second Betti number. Then for any complex structure $J \in \mathcal{J}^{\mathcal{M}}$, and any Kähler class $[\omega] \in \mathcal{K}(J)$, there exists a scalar-flat Kähler ALE metric $g$ satisfying $\left[\omega_{g}\right]=[\omega]$.

Remark 1.14. Our method also proves an analogous global existence result for the case $\Gamma \subset \operatorname{SU}(2)$. However, this case was explicitly constructed by Kronheimer using the hyperkähler quotient construction [Kro89], so we do not devote any extra attention to this case. Note also that the $\mathbb{Q}$-Gorenstein smoothings of the type $T$ cyclic singularities admit Ricci-flat Kähler metrics which are just quotients of the $A_{k}$-type hyperkähler metrics by finite groups of isometries [Şuv12, Wri12]. These metrics play a crucial role in our analysis of non-Artin components.

Remark 1.15. A drastic difference between the ADE cases and the non-ADE cases, is that the global moduli spaces in the latter cases can have 'holes' which can only be filled in by certain smoothings of orbifolds which have nonminimal resolutions. This phenomenon arises already in the case of $\mathcal{O}(-n)$ for $n \geqslant 3$. See Section 8 below for details of these examples.

The groups in Theorem 1.13 have only Artin components. The next result deals with five infinite families of non-Artin components, and is an application of Case (b) in Theorem 1.11, together with Corollary 1.7.

Theorem 1.16. Let $\Gamma \subset \mathrm{U}(2)$ be any of the following groups for $r \geqslant 2$
$$\begin{aligned}
& \Gamma=\frac{1}{r^{2}+r+1}(1, r), \\
& \Gamma=\frac{1}{r^{2}+2 r+2}(1, r+1) \quad \text { or } \quad \Gamma=\frac{1}{2 r^{2}+2 r+1}(1,2 r+1), \\
& \Gamma=\frac{1}{r^{2}+3 r+3}(1, r+2) \quad \text { or } \quad \Gamma=\frac{1}{3 r^{2}+3 r+1}(1,3 r+2) .
\end{aligned}$$
There is a non-Artin component $\mathcal{J}(i)$ of the versal deformation space of $\mathbb{C}^{2} / \Gamma$ with $b_{2}(X)=i$ in Case ( $i$ ), $i=1,2,3$. For any complex structure $J \in \mathcal{J}^{M}(i)$ away from the central fiber, and any Kähler class $[\omega] \in \mathcal{K}(J)$, there exists a scalar-flat Kähler ALE metric $g$ satisfying $\left[\omega_{g}\right]=[\omega]$.

Finally, we conjecture that the assumption on the lower volume growth ratio is redundant, and that for any group $\Gamma$, there exists ALE SFK metrics in all Kähler classes for all complex structures in the versal family.

\section*{2. Preliminaries}
2.1. Notation. In this section, we record some symbols and notations that will be used in this article. Weighted Hölder spaces are defined as follows.

DEFINITION 2.1. Let $E$ be a tensor bundle on $X$, with Hermitian metric $\|\cdot\|_{h}$. Let $\varphi$ be a smooth section of $E$. We fix a point $p_{0} \in X$, and define $r(p)$ to be the distance between $p_{0}$ and $p$. Then define
$$\begin{aligned}
& \|\varphi\|_{C_{\delta}^{0}}:=\sup _{p \in X}\left\{\|\varphi(p)\|_{h} \cdot(1+r(p))^{-\delta}\right\} \\
& \|\varphi\|_{C_{\delta}^{k}}:=\sum_{|\mathcal{I}| \leqslant k} \sup _{p \in X}\left\{\left\|\nabla^{\mathcal{I}} \varphi(p)\right\|_{h} \cdot(1+r(p))^{-\delta+|\mathcal{I}|}\right\},
\end{aligned}$$
where $\mathcal{I}=\left(i_{1}, \ldots, i_{n}\right),|\mathcal{I}|=\sum_{j=1}^{n} i_{j}$. When there is no ambiguity, if $|\mathcal{I}|=d$, we abbreviate $\nabla^{\mathcal{I}} \varphi$ by $\nabla^{(d)} \varphi$. Next, define
$$[\varphi]_{C_{\delta-\alpha}^{\alpha}}:=\sup _{0<d(x, y)<\rho_{\mathrm{inj}}}\left\{\min \{r(x), r(y)\}^{-\delta+\alpha} \frac{\|\varphi(x)-\varphi(y)\|_{h}}{d(x, y)^{\alpha}}\right\},$$
where $0<\alpha<1, \rho_{\text {inj }}$ is the injectivity radius, and $d(x, y)$ is the distance between $x$ and $y$. The meaning of the tensor norm is via parallel transport along the unique minimal geodesic from $y$ to $x$, and then take the norm of the difference at $x$. The weighted Hölder norm is defined by
$$\|\varphi\|_{C_{\delta}^{k, \alpha}}:=\|\varphi\|_{C_{\delta}^{k}}+\sum_{|\mathcal{I}|=k}\left[\nabla^{\mathcal{I}} \varphi\right]_{C_{\delta-k-\alpha}^{\alpha}},$$
and the space $C_{\delta}^{k, \alpha}(X, E)$ is the closure of $\left\{\varphi \in C^{\infty}(X, E):\|\varphi\|_{C_{\delta}^{k, \alpha}}<\infty\right\}$.
\begin{itemize}
\item[-] $\epsilon(i \mid \delta)$ : The symbol $\epsilon(i \mid \delta)$ represents a small positive number, and for any fixed $\delta>0, \epsilon(i \mid \delta) \rightarrow 0$ as $i \rightarrow \infty$.
\item[-] $\Lambda^{\prime}, \Lambda^{\prime}, \Omega^{\prime}: \Lambda^{p}$ stands for the space of real $p$-forms, $\Lambda^{p, q}$ stands for the space of complex $(p, q)$-forms, $\Omega^{p}$ stands for the space of complex $(p, 0)$-forms.
\item[-] $\widetilde{X}$ : For a complex variety $X$ of complex dimension $2, \widetilde{X}$ stands for the minimal resolution of $X$.
\item[-] $\bar{V}$ : For a topological space $V, \bar{V}$ stands for its universal cover.
\item[-] $g, \omega$ : We denote the Riemannian metric by $g$ and $\omega=g(J \cdot, \cdot)$ as the corresponding Kähler form. But on occasion when there is no ambiguity, we use these two symbols alternatively for convenience.
\end{itemize}
2.2. Facts about ALE Kähler surfaces. We list some facts about ALE Kähler surfaces which we use later. We always assume the asymptotic rate $-\mu<-1$.

By applying Hodge index theorem as shown in [HL16, Proposition 4.2], an ALE Kähler surface has only one ALE end. As pointed out by Hein-LeBrun, for an ALE Kähler metric $(X, g, J)$ of order $\mu$, the complex structure has an asymptotic rate of
$$\partial^{\mathcal{I}}\left(J-J_{\mathrm{Euc}}\right)=O\left(r^{-\mu-|\mathcal{I}|}\right),$$
for any multi-index $\mathcal{I}$ as $r \rightarrow \infty$, where $J_{\text {Euc }}$ is the standard complex structure on Euclidean space. This is because, $\nabla_{g_{\text {Euc }}} J=\left(\nabla_{g_{\text {Euc }}}-\nabla_{g}\right) J=O\left(r^{-\mu-1}\right)$. The integral along each $g_{\text {Euc }}$-geodesic ray implies the ALE asymptotic rate of $J$ as above.

Remark 2.2. Although our proof will not require the following, we make a remark on the optimal decay rates of the metric and complex structure. For any ALE SFK metric, there exists an ALE coordinate with optimal metric asymptotic rate of $O\left(r^{-2}\right)$, see [AV12, LM08, Str10]. Furthermore, by [HL16, Proposition 4.5], for $(X, g, J)$ of order $\mu$, there exists an ALE coordinate which is still at least of order $\mu$, and for which $J$ converges to the Euclidean complex structure $J_{\text {Euc }}$ at the rate of $O\left(r^{-3}\right)$. Therefore, if $g$ is ALE SFK, there always exists an ALE coordinate so that the metric $g$ converges to $g_{\text {Euc }}$ at the rate of $O\left(r^{-2}\right)$ and $J \sim J_{\mathrm{Euc}}+O\left(r^{-3}\right)$ as $r \rightarrow \infty$.

For an ALE Kähler surface $X, \mathcal{H}_{-3}\left(X, \Lambda_{\mathbb{R}}^{1,1}\right)$ stands for the space of decaying real harmonic (1, 1)-forms. Note that any decaying real harmonic (1, 1)-form has a decay rate at least $O\left(r^{-3}\right)$, and $H^{2}(X, \mathbb{R}) \cong \mathcal{H}_{-3}\left(X, \Lambda_{\mathbb{R}}^{1,1}\right)$ (for details see [HV16, Section 7] and [Joy00, Sections 8.4 and 8.9]). We have the following which is a consequence of a $\partial \bar{\partial}$-lemma for Kähler forms as shown in [HV16, Lemma 8.3].

Lemma 2.3. For any two smooth Kähler metrics $\omega_{1}, \omega_{2}$ over an ALE Kähler surface $(X, J)$, if $\omega_{1}-\omega_{2}=O\left(r^{\nu-2}\right),(0<\nu<1)$, and $\int_{X}\left(\omega_{1}-\omega_{2}\right) \wedge h=0$ for any $h \in \mathcal{H}_{-3}\left(X, \Lambda_{\mathbb{R}}^{1,1}\right)$, then there exists $\phi \in C_{\nu}^{\infty}(X, \mathbb{R})$, such that $\omega_{2}=\omega_{1}+\sqrt{-1} \partial \bar{\partial} \phi$.

In particular, this shows that our definition of the Kähler cone in Definition 1.3 is the 'correct' one: any two Kähler forms whose difference decays and is zero in the de Rham cohomology group $H^{2}(X, \mathbb{R})$, must differ by $\sqrt{-1} \partial \bar{\partial} \phi$, where $\phi$ is of sublinear growth rate.

Another important fact about ALE Kähler surfaces is that they are one-convex, which we define next.

Definition 2.4 (One-convex surface). A one-convex surface $X$ is a noncompact complex surface carrying a $C^{\infty}$-exhaustion function $f: X \rightarrow[0, \infty)$ which is strictly plurisubharmonic outside a compact set.

To see that an ALE Kähler surface is one-convex: using an ALE coordinate system, extend the pullback of the function $r_{\text {Euc }}^{2}$ to a smooth nonnegative function on all of $X$, and this will be the required function $f$. Any one-convex surface $X$ is a point modification of a Stein space $Y$, that is, $X$ is obtained from $Y$ by substituting some points with compact analytic sets; for more details, see [Pet94, Theorem 2.1]. On a one-convex surface $X$, any holomorphic function defined outside of a compact set can be extended to a holomorphic function on $X$. This is because a holomorphic function defined outside of a compact set on the Remmert reduction $Y$ can be extended to a holomorphic function on $Y$ by [Ros63, Theorem 6.1], and then can be lifted up to a holomorphic function on $X$.
2.3. Versal deformation of $\mathbb{C}^{2} / \boldsymbol{\Gamma}$. In this subsection, we provide more details of the versal family, and the deformation to the normal cone construction.
By Artin [Art74] and Wahl [Wah79], there exists an irreducible component $\operatorname{Der}_{0}\left(\mathcal{Y}_{0}\right) \subset \operatorname{Der}\left(\mathcal{Y}_{0}\right)$, with a finite base change (which is a Galois cover) Res → $\operatorname{Der}_{0}\left(\mathcal{Y}_{0}\right)$, such that there exists a simultaneous resolution $\mathcal{X}$ that satisfies the commutative diagram:
![](https://cdn.mathpix.com/cropped/9a120029-d3e2-4d90-8447-ba255e904003-10.jpg?height=166&width=315&top_left_y=1116&top_left_x=569)
The base $\operatorname{Der}_{0}\left(\mathcal{Y}_{0}\right)$ is called the Artin component of the versal deformation. The Artin component is the only irreducible component which admits a simultaneous resolution. According to Wahl, $\operatorname{Der}_{0}\left(\mathcal{Y}_{0}\right)=\operatorname{Res} / W$, where $W$ is the Weyl group action. Since the $\mathbb{C}^{*}$-action is preserved under the finite base change, we can apply the $\mathbb{C}^{*}$-action on Res. Then we obtain a global analytic space $\mathcal{J}_{0}$ and a family $\mathcal{X} \rightarrow \mathcal{J}_{0}$. Each fiber $\mathcal{X}_{t}$ is smooth.
We recall some facts from [KSB88]. There exists a one-parameter $\mathbb{Q}$ -Gorenstein smoothing of $\mathbb{C}^{2} / \Gamma$ if and only if $\Gamma \subset \operatorname{SU}(2)$, or $\mathbb{C}^{2} / \Gamma$ is a type $T$ singularity, that is, $\Gamma$ is cyclic of type $\frac{1}{r^{2} s}(1, r s d-1)$ where $r \geqslant 2, s \geqslant 1$, $(r, d)=1$. See Section 7 below for more details about type $T$ singularities. For each non-Artin component $\operatorname{Der}_{k}\left(\mathcal{Y}_{0}\right)(k>0)$, there exists a $P$-resolution $Z_{k}^{P}$ with only type $T$ singularities, which has a local moduli space of $\operatorname{Der}^{\prime}\left(Z_{k}^{P}\right)$ which is the component corresponding to $\mathbb{Q}$-Gorenstein smoothings. Furthermore, there exists a finite base change $\operatorname{Der}^{\prime}\left(Z_{k}^{P}\right) \rightarrow \operatorname{Der}_{k}\left(\mathcal{Y}_{0}\right)$.

Next, we recall some facts from [BC94]. There exists an $M$-resolution $Z_{k}^{M} \rightarrow$ $Z_{k}^{P}$ with only type $T_{0}$ singularities (type $T$ singularities with $s=1$ ), which has a local moduli space $\operatorname{Der}^{\prime}\left(Z_{k}^{M}\right)$, where all nearby fibers are smooth; here $\operatorname{Der}^{\prime}\left(Z_{k}^{M}\right)$ denotes the component corresponding to $\mathbb{Q}$-Gorenstein smoothings. There exists a finite base change $\operatorname{Der}^{\prime}\left(Z_{k}^{M}\right) \rightarrow \operatorname{Der}^{\prime}\left(Z_{k}^{P}\right)$. All together, we have the commutative diagram
![](https://cdn.mathpix.com/cropped/9a120029-d3e2-4d90-8447-ba255e904003-11.jpg?height=175&width=676&top_left_y=435&top_left_x=389)

Each fiber $\mathcal{Z}_{t}$ is smooth away from the discriminant locus. Each fiber $\mathcal{X}_{t}$ is smooth save the central fiber. For $t^{\prime \prime} \in \operatorname{Der}^{\prime}\left(Z_{k}^{M}\right), t^{\prime} \in \operatorname{Der}^{\prime}\left(Z_{k}^{P}\right), t \in \operatorname{Der}_{k}\left(\mathcal{Y}_{0}\right)$ with $t^{\prime \prime}$ mapped to $t^{\prime}, t^{\prime}$ mapped to $t$, there exists resolutions $\mathcal{X}_{t^{\prime \prime}} \rightarrow \mathcal{Z}_{t^{\prime}} \rightarrow \mathcal{Y}_{t}$, and $\mathcal{X}_{t^{\prime \prime}}$ is minimal when $t^{\prime \prime} \neq 0 . \mathcal{J}_{k}^{M}, \mathcal{J}_{k}^{P}$ are generated by applying the $\mathbb{C}^{*}$-action on $\operatorname{Der}^{\prime}\left(Z_{k}^{M}\right), \operatorname{Der}^{\prime}\left(Z_{k}^{P}\right)$ respectively.

By [HRŞ16], any ALE Kähler surface is birationally equivalent to an element in the versal deformation of $\mathbb{C}^{2} / \Gamma$. We review some details of the construction in [HRŞ16] which will be needed in our proof. For an ALE Kähler surface $X$ under our consideration, the asymptotic rate of the complex structure is faster than $O\left(r^{-1-\epsilon}\right)$. By [HL16], the $O\left(r^{-1-\epsilon}\right)$ asymptotic rate of the complex structure implies that $X$ can be compactified analytically to a compact orbifold $\hat{X}=X \cup D$, where $D$ is isomorphic to $\mathbb{P}^{1}$ quotient by a finite group (see [Li14] for the more general asymptotically conical case). There exists a positive integer $m \in \mathbb{Z}_{+}$such that $m \cdot D$ is a Cartier divisor, which induces a line bundle $L$ in $\hat{X}$. By a Nakai-Moishezon type argument, it is shown in [HRŞ16] that for some $k \in \mathbb{Z}_{+}$large enough, $H^{0}\left(\hat{X}, L^{k}\right) \rightarrow H^{0}\left(D, L^{k}\right)$ is surjective and $L^{k} \rightarrow \hat{X}$ is globally generated. As a result, there exist holomorphic sections $s_{0}, \ldots, s_{N}$ in $H^{0}\left(\hat{X}, L^{k}\right)$, where $s_{0}$ is the defining section of $k m \cdot D$, that is, $s_{0}$ vanishes exactly on $D$, such that images of $s_{1}, \ldots, s_{N}$ in $H^{0}\left(D, L^{k}\right)$ are generators. Then the linear system $\left|H^{0}\left(\hat{X}, L^{k}\right)\right|$ maps $\hat{X}$ to $\mathbb{P}^{N}$ by $\left[s_{0}, \ldots, s_{N}\right]$, where the image $\hat{X}^{\prime}$ is birationally equivalent to $\hat{X}$. Furthermore, $u^{1}=s_{1} / s_{0}, \ldots, u^{N}=s_{N} / s_{0}$ can extend to holomorphic functions on $X$, and $u=\left(u^{1}, \ldots, u^{N}\right)$ maps $X$ to $X^{\prime}$ in $\mathbb{C}^{N}$. Define the graded ring
$$R=\bigoplus_{n \geqslant 0} H^{0}(\hat{X}, \mathcal{O}(n \cdot D))$$
which is finitely generated. Let $R[z]$ be a graded ring where $z$ is a free variable of the degree 1 and is defined as
$$R[z]=\bigoplus_{n \geqslant 0}\left(\bigoplus_{0 \leqslant j \leqslant n} H^{0}(\hat{X}, \mathcal{O}(j \cdot D)) \cdot z^{n-j}\right) .$$

The deformation to the normal cone is defined by
$$\hat{\mathcal{X}}^{\prime}=\{s-t z=0\} \subset \operatorname{Proj}(R[z]) \times \mathbb{C},$$
where $s$ is the defining section of $D, t \in \mathbb{C}, \hat{\mathcal{X}}_{1}^{\prime}$ is identified with $\hat{X}^{\prime}$, and $C(D):=$ $\hat{\mathcal{X}_{0}^{\prime}} \backslash D$ is the normal cone of $D$. This implies that $X^{\prime}$ is a deformation of $\mathbb{C}^{2} / \Gamma$. By versality, the deformation to the normal cone can be considered as a pullback of the versal deformation of $\mathbb{C}^{2} / \Gamma$.

We next have the following proposition which parameterizes all minimal ALE Kähler surfaces.

Proposition 2.5. Each minimal ALE Kähler surface is biholomorphic to an element in $\mathcal{J}^{M}$.

Proof. Let $X$ be a minimal ALE Kähler surface with an end asymptotic to $\mathbb{C}^{2} / \Gamma$. Then there exists no $(-1)$-curve in $X$. By the result of [HRŞ16], $X$ is birationally equivalent to $Y$, which is a deformation of $\mathbb{C}^{2} / \Gamma$. By the commutative diagram (2.7), there exists an element $X^{\prime}$ in $\mathcal{J}^{M}$, which is the minimal resolution of $Y$. Since $X, X^{\prime}$ are one-convex spaces and they are birationally equivalent with each other, there exist compact subsets $K \subset X, K^{\prime} \subset X^{\prime}$, and a biholomorphic map $\Phi: X \backslash K \rightarrow X^{\prime} \backslash K^{\prime}$. Furthermore, by choosing $K$ large enough, there exist holomorphic functions $u^{1}, \ldots, u^{N}$ on $X \backslash K$, which embed $X \backslash K$ into $\mathbb{C}^{N}$ by $u=\left(u^{1}, \ldots, u^{N}\right)$. Since $X$ is one-convex, $u$ can be extended to a holomorphic map on $X$. Meanwhile $u^{\prime}=u \circ \Phi^{-1}$ embeds $X^{\prime} \backslash K^{\prime}$ into $\mathbb{C}^{N}$ and can be extended to a holomorphic map on $X^{\prime}$. The image $u(X \backslash K)$ in $\mathbb{C}^{N}$ coincides with the image $u^{\prime}\left(X^{\prime} \backslash K^{\prime}\right)$, which is denoted by $V$. The boundary of $V$ is a strictly pseudoconvex manifold ( $V$ itself is called strictly pseudoconcave). By [HL75, Theorem 10.4], there exists a unique Stein space $W$ in $\mathbb{C}^{N}$, which extends from $V$ through its boundary smoothly. By uniqueness of analytic extension, $u(X), u^{\prime}\left(X^{\prime}\right)$ coincide with $W$, and thus $W$ is the Remmert reduction of $X, X^{\prime}$. Since each isolated 2-dimensional quotient singularity, there exists a unique minimal resolution, then $W$ has a unique minimal resolution. Then by the minimality of $X, X^{\prime}$, they are both biholomorphic to the minimal resolution of $W$. \(\square\)
2.4. Volume local noncollapsing. Let ( $X, g$ ) be an ALE SFK metric, with the complex orientation so that $W_{g}^{+} \equiv 0$, and group $\Gamma$ at infinity. Let ( $M,[\hat{g}]$ ) be the orbifold conformal compactification, with the reversed orientation so that the group at the orbifold point is also $\Gamma$ [Via10]. Since the orientation is reversed, we have that $W_{\hat{g}}^{-} \equiv 0$. Note that $[\hat{g}]$ is a priori a self-dual conformal structure, but by [CLW08, Proposition 12], we can assume that there is a metric representative $\hat{g} \in[\hat{g}]$ which is moreover a smooth Riemannian orbifold.

The Hirzebruch signature theorem for orbifolds [Kaw81] states that,
$$\tau(M)=\frac{1}{12 \pi^{2}} \int_{M}\left\|W^{+}\right\|^{2} d V_{g}-\eta\left(S^{3} / \Gamma\right),$$
and $\eta\left(S^{3} / \Gamma\right)$ is the $\eta$-invariant of the signature complex, which for a finite subgroup $\Gamma \subset \operatorname{SO}(4)$ acting freely on $S^{3}$, is given by
$$\eta\left(S^{3} / \Gamma\right)=\frac{1}{|\Gamma|} \sum_{\gamma \neq \mathrm{Id} \in \Gamma} \cot \left(\frac{r(\gamma)}{2}\right) \cot \left(\frac{s(\gamma)}{2}\right),$$
where $r(\gamma)$ and $s(\gamma)$ denote the rotation numbers of $\gamma \in \Gamma$.
The Chern-Gauss-Bonnet theorem for orbifolds [Kaw81] states that
$$\chi(M)=\frac{1}{8 \pi^{2}} \int_{M}\left(\|W\|^{2}-\frac{1}{2}|E|^{2}+\frac{1}{24} R^{2}\right) d V_{g}+\left(1-\frac{1}{|\Gamma|}\right),$$
where $E$ denotes the traceless Ricci tensor, and $R$ denotes the scalar curvature.
Using (2.11) and (2.13), we obtain
$$\begin{aligned}
2 \chi(M)-3 \tau(M)= & \frac{1}{4 \pi^{2}} \int_{M}\left(-\frac{1}{2}|E|^{2}+\frac{1}{24} R^{2}\right) d V_{\hat{g}} \\
& +2\left(1-\frac{1}{|\Gamma|}\right)+3 \eta\left(S^{3} / \Gamma\right)
\end{aligned}$$
Define the quantity
$$\mathcal{C}(X)=2 \chi(M)-3 \tau(M)-2\left(1-\frac{1}{|\Gamma|}\right)-3 \eta\left(S^{3} / \Gamma\right) .$$
Then we obtain
$$\mathcal{C}(X) \leqslant \frac{1}{96 \pi^{2}} \int_{M} R^{2} d V_{\hat{g}}$$
We note that the conformal class is of positive type, that is, $Y(M,[\hat{g}])>0[\mathbf{A B 0 4}$, CLW08]. If there exists a minimizing solution of the Yamabe problem on the orbifold ( $M,[\hat{g}]$ ) then since the scalar curvature is constant we obtain the lower estimate on the Yamabe invariant.
$$Y(M,[\hat{g}]) \geqslant 4 \sqrt{6} \pi \sqrt{\mathcal{C}(X)} .$$
If there does not exist a Yamabe minimizer, then the estimate of Akutagawa and Botvinnik [Aku12, AB04] says that the Yamabe invariant must be maximal
$$Y(M,[\hat{g}])=\frac{8 \sqrt{6} \cdot \pi}{\sqrt{|\Gamma|}} .$$

In either event, if $\mathcal{C}(X)>0$ we have that the Yamabe invariant is strictly bounded below by a positive constant. From (2.17), we have
$$\int_{M} u \square_{\hat{g}} u d V_{\hat{g}} \geqslant 4 \sqrt{6} \pi \sqrt{\mathcal{C}(X)}\left\{\int_{M} u^{4} d V_{\hat{g}}\right\}^{1 / 2}$$
for any $u \in C^{\infty}(M)$, where
$$\square_{\hat{g}}=-6 \Delta_{\hat{g}}+R_{\hat{g}}$$
is the conformal Laplacian.
Writing $\tilde{g}=v^{2} g$, we have the transformation formula
$$\square_{\tilde{g}}(u)=v^{-3} \square_{g}(u v) .$$
This yields
$$\int_{M} f \square_{g} f d V_{g} \geqslant 4 \sqrt{6} \pi \sqrt{\mathcal{C}(X)}\left\{\int_{M} f^{4} d V_{g}\right\}^{1 / 2} .$$
Since $g$ is scalar flat, $\square_{g}=-6 \Delta_{g}$, so we obtain the $L^{2}$-Sobolev inequality
$$\left\{\int_{X} f^{4} d V_{g}\right\}^{1 / 2} \leqslant \frac{\sqrt{6}}{4 \pi \sqrt{\mathcal{C}(X)}} \int_{X}|\nabla f|^{2} d V_{g},$$
for all $f \in C_{c}^{\infty}(X)$.
Note that since $M=X \cup\{p t\}$, we have $\chi(M)=\chi(X)+1$. Also, since the orientation is reversed, we have $\tau(M)=-\tau(X)$. Since $(X, g)$ is Kähler ALE, we have $b_{1}(X)=0$. Therefore,
$$\mathcal{C}(X)=2-b_{2}(X)+\frac{2}{|\Gamma|}-3 \eta\left(S^{3} / \Gamma\right) .$$
Therefore, we have the following:
Proposition 2.6. If ( $X, J, g$ ) is an ALE SFK metric with $\mathcal{C}(X)>0$, then there exists a constant $v>0$, depending only upon $X$, such that $\mathcal{V}(g)>v$.

Proof. The above argument shows that there is a uniform $L^{2}$-Sobolev inequality. The lower volume growth estimate follows from this by a standard argument, see [Heb96, Lemma 3.2]. \(\square\)

For any component $\mathcal{J}_{k}^{M}$, we define $\mathcal{C}\left(\mathcal{J}_{k}^{M}\right)$ to be $\mathcal{C}(X)$, where $X$ is diffeomorphic to a smooth fiber of the component $\mathcal{J}_{k}^{M}$ (noting that any two such fibers are diffeomorphic).
2.5. Cheeger-Gromov convergence. We begin this subsection with the following notion of convergence.

Definition 2.7 (Pointed Cheeger-Gromov convergence). A sequence of Kähler manifolds $\left(X_{i}, g_{i}, J_{i}, x_{i}\right)$ converges to a Kähler orbifold space $(Z, g, J, z)$ in the pointed Cheeger-Gromov sense if $\left(X_{i}, g_{i}, x_{i}\right)$ converges to $(Z, g, z)$ in the pointed Gromov-Hausdorff sense, and there exists a subset $S=\left\{p_{1}, \ldots, p_{m}\right\} \subset$ $Z$ which contains the singular set of $Z$, for any compact subset $K \subset Z \backslash S$ containing $z$, there exists diffeomorphisms $\psi_{i}: K \rightarrow X_{i}$, such that $\psi_{i}^{*} g_{i}, \psi_{i}^{*} J_{i}$ converges to $g, J$ in $C^{k, \alpha}(K)$-sense, for some $k, \alpha$.

We refer to [And89, Ban90, BKN89, Nak94, TV05b, Tia90] for more details on this type of convergence.
First recall the $\epsilon$-regularity theorem proved in [TV05a, TV08]. Let $(X, g)$ be a complete scalar-flat Kähler 4-dimensional manifold, with a local volume ratio lower bound $v>0$, that is, $\operatorname{vol}\left(B_{r}(x)\right)>v \cdot r^{4}$ for any $|r|<1$. In [TV05a, Theorem 1.1], by studying the PDE system with a Moser-iteration type argument,
$$\begin{aligned}
\Delta_{g} \operatorname{Ric} & =R m * \operatorname{Ric} \\
\Delta_{g} R m & =L\left(\nabla_{g}^{2} \operatorname{Ric}\right)+R m * R m
\end{aligned}$$
the authors proved that there exists an $\epsilon_{0}=\epsilon_{0}(v)>0$, such that if $\int_{X \backslash B_{R}\left(x_{0}\right)}\|R m(g)\|^{2} d V_{g}<\epsilon_{0}$, then there exists $C=C(v)>0$, such that $\|R m(g)\|<C \cdot r^{-2}$ on $X \backslash B_{R}\left(x_{0}\right)$, where $x_{0}$ is a point in $X, B_{R}\left(x_{0}\right)$ is the geodesic ball centered at $x_{0}$ with a radius of $R$. Note that the argument in [TV05a] required a Sobolev constant bound, but this was weakened to only a lower volume growth assumption in [TV08]. Furthermore, by Kato's inequality and a further analysis of the connection form, for any $-2<-\mu<-1$, for any positive integer $k$, there exists $C^{\prime}=C^{\prime}(v, k)>0$, such that, on $X \backslash B_{R}\left(x_{0}\right),\left\|\nabla^{(k)} R m(g)\right\|<C^{\prime} \cdot r^{-2-\mu-k}$. We call the $\epsilon_{0}$ above the 'energy threshold'.

By the proof of [BKN89, Theorem 1.1], there exists a harmonic coordinate on the universal cover of $X \backslash B_{R}\left(x_{0}\right)$, which provides an ALE coordinate
$$H: X \backslash B_{R}\left(x_{0}\right) \rightarrow \mathbb{R}^{4} / \Gamma,$$
and constants $C^{\prime \prime}=C^{\prime \prime}(v, k)>0$, such that
$$\left|\partial^{(k)}\left(H_{*} g-g_{\mathrm{Euc}}\right)\right|<C^{\prime \prime} \cdot r^{-\mu-k} .$$
Note that the harmonic coordinates are technically defined on the universal cover $\overline{X \backslash B_{R}\left(x_{0}\right)}$, which is a mapping $\bar{H}: \overline{X \backslash B_{R}\left(x_{0}\right)} \rightarrow \mathbb{R}^{4}$ defined by harmonic
functions of 'linear growth'. However, by the rigidity of harmonic coordinates proved in [Bar86, Corollary 3.2], for any $\gamma \in \Gamma, \gamma^{*} \bar{H}=\gamma \cdot \bar{H}$, where in the latter formula $\gamma$ is considered as a linear map in SO(4). This implies that $\bar{H}$ is $\Gamma$-equivariant and can descend to a map $H: X \backslash B_{R}\left(x_{0}\right) \rightarrow \mathbb{R}^{4} / \Gamma$.

DEFINITION 2.8. An energy concentration point $x_{\infty} \in X_{\infty}$ is a point such that for any $\delta>0$, there exists $x_{i} \in X_{i}$ with $x_{i} \rightarrow x_{\infty}$ (in the Gromov-Hausdorff distance), and such that
$$\int_{B_{\delta}\left(x_{i}\right)}\left\|R m\left(g_{i}\right)\right\|^{2} d V_{g_{i}} \geqslant \epsilon_{0},$$
where $\epsilon_{0}$ is the energy threshold.
We next define a stronger notion of pointed Cheeger-Gromov convergence in the ALE setting which includes the convergence near $\infty$.

Definition 2.9. Let ( $X_{i}, J_{i}, g_{i}, x_{i}$ ) be a sequence of ALE Kähler surfaces, where each $g_{i}$ is asymptotic to $g_{\text {Euc }}$ of order $O\left(r^{-\mu}\right)(-2<-\mu<-1)$ with respect to a fixed ALE coordinate. We say the sequence $\left\{\left(X_{i}, J_{i}, g_{i}, x_{i}\right)\right\}$ converges in the sense of 'pointed Cheeger-Gromov with a uniform ALE asymptotic rate of order $O\left(r^{-\mu}\right)^{\prime}$ if there exists an ALE Kähler orbifold ( $X_{\infty}$, $J_{\infty}, g_{\infty}, x_{\infty}$, where $p_{1}, \ldots, p_{m}$ are 'energy concentration' points in $X_{\infty}$, such that
$$\left(X_{i}, J_{i}, g_{i}, x_{i}\right) \xrightarrow{\text { pointed Cheeger-Gromov }}\left(X_{\infty}, J_{\infty}, g_{\infty}, x_{\infty}\right)$$
for any $k \in \mathbb{Z}_{\geqslant 0}, 0<\alpha<1$, and for any $\delta>0$, when $i$ is sufficiently large, there exists a diffeomorphism
$$\psi_{i}: X_{\infty} \backslash \bigsqcup_{1 \leqslant j \leqslant m} B_{\delta}\left(p_{j}\right) \rightarrow X_{i}$$
such that $\left\|\psi_{i}^{*} g_{i}-g_{\infty}\right\|_{C_{-\mu}^{k, \alpha}\left(g_{\infty}\right)}<\epsilon(i \mid k, \delta),\left\|\psi_{i}^{*} J_{i}-J_{\infty}\right\|_{C_{-\mu}^{k, \alpha}\left(g_{\infty}\right)}<\epsilon(i \mid k, \delta)$.
Note that if a sequence converges in the above sense, then $X_{\infty}$ has end diffeomorphic to $\mathbb{R}^{4} / \Gamma$ with the same group $\Gamma$ as for $X_{i}$. Also, for each 'energy concentration' point $p$ above, there exists a sequence of points $p_{i} \in X_{i}$, where $\lim _{i \rightarrow \infty}\left\|\operatorname{Rm}\left(p_{i}\right)\right\|_{C^{0}\left(g_{i}\right)} \rightarrow \infty$. We also remark that $p$ may not strictly be an orbifold point, since the 'bubble' appearing at $p$ could be $\mathcal{O}_{\mathbb{C} P^{1}}(-1)$ with the Burns metric [Bur86, Cal79].

Lemma 2.10. Consider a sequence of ALE SFK metrics ( $X_{i}, J_{i}, g_{i}, x_{i}$ ) which are ALE of asymptotic rate $O\left(r^{-\mu}\right)$ with respect to a fixed ALE coordinate,
where $-2<-\mu<-1$. Assume that:
\begin{itemize}
\item[(1)] the spaces $X_{i}$ are diffeomorphic to a fixed space $X$;
\item[(2)] there exists a constant $v>0$, independent of $i$, such that $\operatorname{Vol}\left(B_{r}\left(x, g_{i}\right)\right)>$ $v \cdot r^{4}$ for each $x \in X$ and $0<r \leqslant 1$;
\item[(3)] there exists $R>0$, such that $\int_{X_{i} \backslash B_{R}\left(x_{i}, g_{i}\right)}\left\|R m\left(g_{i}\right)\right\|_{C^{0}}^{2} d V_{g_{i}}<\epsilon_{0} / 2$, where $B_{R}\left(x_{i}, g_{i}\right)$ is a geodesic ball with respect to the metric $g_{i}$.
\end{itemize}

Then up to a subsequence, $\left(X_{i}, J_{i}, g_{i}, x_{i}\right)$ converges to an ALE SFK orbifold $\left(X_{\infty}\right.$, $\left.J_{\infty}, g_{\infty}, x_{\infty}\right)$ in the sense of pointed Cheeger-Gromov convergence with a uniform ALE asymptotic rate of order $O\left(r^{-\mu}\right)$.

Proof. For convenience, in the following of the proof, $C$ is denoted as a positive constant with value that may vary line by line. If $C$ depends on the subscript $i$ (index of the sequence) (or the superscript $k$ (degree of regularity)), we specify it as $C=C(i)$ (or $C(k)$ ).

The Hirzebruch signature theorem for an ALE SFK metric states that,
$$\tau(X)=-\frac{1}{12 \pi^{2}} \int_{X}\left\|W^{-}\right\|^{2} d V_{g}+\eta\left(S^{3} / \Gamma\right),$$
and the Chern-Gauss-Bonnet theorem in this setting [Hit97, Nak90] states that
$$\chi(X)=\frac{1}{8 \pi^{2}} \int_{X}\left(\left\|W^{-}\right\|^{2}-\frac{1}{2}|E|^{2}\right) d V_{g}+\frac{1}{|\Gamma|} .$$
Consequently, if the group $\Gamma$ is fixed, and all of the spaces are diffeomorphic, then there exists a constant $C$ so that
$$\int_{X_{i}}\|R m\|_{g_{i}}^{2} d V_{i} \leqslant C .$$
By (2.27), there exists an ALE coordinate $H_{i}: X_{i} \backslash B_{R}\left(x_{i}\right) \rightarrow \mathbb{R}^{4} / \Gamma$, such that
$$\left|\partial^{(k)}\left(H_{i *} g_{i}-g_{\mathrm{Euc}}\right)\right|<C(k) \cdot r^{-\nu-k},$$
where we can choose $-v$ between $-2<-v<-\mu$. By our assumption of lower volume growth, by [TV05b, Theorem 1.1] and [TV08, Theorem 1.3], up to a subsequence, ( $X_{i}, g_{i}, x_{i}$ ) converges to ( $X_{\infty}, g_{\infty}, x_{\infty}$ ) in the pointed Gromov-Hausdorff sense. Since $J_{i}$ is parallel with respect to $g_{i}$, it is easy to see that there is a limiting complex structure $J_{\infty}$. Moreover, using [TV05b, Theorem 6.1], the limit ( $X_{\infty}, J_{\infty}, g_{\infty}, x_{\infty}$ ) is an ALE SFK orbifold. Without loss of generality,
assume $x_{\infty}$ is the only energy concentration point in $X_{\infty}$. Then for any $\delta>0$, $R>\delta>0$, there exists a diffeomorphism
$$\psi_{i}^{\prime}: A_{\delta, 2 R}\left(x_{\infty}\right) \rightarrow X_{i}$$
such that $\psi_{i}^{\prime *} g_{i} \xrightarrow{C^{\infty}} g_{\infty}$. For a $R$ large enough (with its specific value to be determined later), there exists an ALE coordinate
$$\pi: X_{\infty} \backslash B_{R}\left(x_{\infty}\right) \rightarrow \mathbb{R}^{4} / \Gamma$$
such that $\left|\partial^{(k)}\left(\pi_{*} g_{\infty}-g_{\text {Euc }}\right)\right|<C(k) \cdot r^{-\nu-k}$, where $r$ is the Euclidean distance to the origin. Since on $A_{\delta, 2 R}\left(x_{\infty}\right), \psi_{i}^{\prime *} g_{i}$ converges to $g_{\infty}$ smoothly, for each $\epsilon^{\prime}>0$, by choosing $R$ large enough, and when $i$ is sufficiently large,
$$H_{i} \circ \psi_{i}^{\prime} \circ \pi^{-1}=A_{i}+Q_{i}$$
where $A_{i}$ is induced from a subgroup of $S O(4)$ acting on the universal cover of $\mathbb{R}^{4} / \Gamma,\left|Q_{i}\right|<\epsilon^{\prime}$. Since $A_{i}$ is induced from a subgroup of $S O(4), A_{i}^{-1} \circ H_{i}$ : $X_{i} \backslash B_{R}\left(x_{i}\right) \rightarrow \mathbb{R}^{4} / \Gamma$ is still an ALE coordinate with the same asymptotic rate. Then we can extend $\psi_{i}^{\prime}$ to a diffeomorphism $\psi_{i}$ from $X_{\infty} \backslash B_{\delta}\left(x_{\infty}\right)$ to $X_{i} \backslash B_{\delta}\left(x_{i}\right)$ by defining
$$\psi_{i}= \begin{cases}\psi_{i}^{\prime} & \text { on } A_{\delta, R}\left(x_{\infty}\right) \\ H_{i}^{-1} \circ A_{i} \circ \pi & \text { on } X_{\infty} \backslash B_{2 R}\left(x_{\infty}\right) \\ \left(1-\chi\left(\frac{r(x)}{R}\right)\right) \psi_{i}^{\prime}+\chi\left(\frac{r(x)}{R}\right) H_{i}^{-1} \circ A_{i} \circ \pi & \text { on } A_{R, 2 R}\left(x_{\infty}\right),\end{cases}$$
where $\chi: \mathbb{R}_{\geqslant 0} \rightarrow \mathbb{R}_{\geqslant 0}$ is a nondecreasing smooth function, $\chi(t)=0$ if $t \leqslant 1$, $\chi(t)=1$ if $t \geqslant 2, r(\cdot)$ is the distance to $x_{\infty}$ with respect to the metric $g_{\infty}$. Since $-v<-\mu$, for any $\epsilon^{\prime}>0$, we can fix a constant $R>0$ large enough, such that, when $i$ is sufficiently large, $\left\|\psi_{i}^{*} g_{i}-g_{\infty}\right\|_{C_{-\mu}^{k, \alpha}\left(X_{\infty}\left(B_{\delta}\left(x_{\infty}\right)\right)\right)}<\epsilon^{\prime}$. The convergence of the complex structure follows from the convergence of the Riemannian metric, using the same argument as in (2.5). \(\square\)
2.6. Bubble trees. The degeneration of convergence at 'energy concentration points' can be understood through a process called 'bubbling'. The sequence ( $X_{i}, g_{i}, x_{i}$ ) in Lemma 2.10 converges to an orbifold limit ( $X_{\infty}, g_{\infty}, x_{\infty}$ ). By studying different scales of convergence toward the energy concentration point $x_{\infty}$, there is a 'bubble tree' structure which captures the topological information that 'disappears' in the orbifold limit.

At any energy concentration point, we choose the smallest fixed $\delta>0$, and $r_{i} \rightarrow 0$, such that in $B_{\delta}\left(x_{i}\right)$
$$\int_{B_{\delta}\left(x_{i}\right) \backslash B_{r_{i}}\left(x_{i}\right)}\left\|R m\left(g_{i}\right)\right\|^{2} d V_{g}=\frac{\epsilon_{0}}{2} .$$
The rescaled sequence
$$\left(Y_{i}, g_{i}^{\prime}, y_{i}\right)=\left(B_{\delta}\left(x_{i}\right), \frac{1}{r_{i}^{2}} g_{i}, x_{i}\right)$$
then converges to an ALE orbifold limit ( $Y_{\infty}, g_{\infty}^{\prime}, y_{\infty}$ ) in the pointed Cheeger-Gromov sense, where the limit is called the 'first bubble'. For any energy concentration point $p \in Y_{\infty}$ in the rescaled limit, there exists a sequence of points $p_{i} \in Y_{i}$ that converges to $p$, and high curvature regions $B_{\delta^{\prime}}\left(p_{i}\right) \subset Y_{i}$ for some $\delta^{\prime}>0$, and $r_{i}^{\prime} \rightarrow 0$, such that
$$\int_{B_{\delta^{\prime}}\left(p_{i}\right) \backslash B_{r_{i}^{\prime}}\left(p_{i}\right)}\left\|\operatorname{Rm}\left(g_{i}^{\prime}\right)\right\|^{2} d V_{g_{i}^{\prime}}=\frac{\epsilon_{0}}{2},$$
and the rescaled sequence
$$\left(Z_{i}, g_{i}^{\prime \prime}, z_{i}\right)=\left(B_{\delta^{\prime}}\left(p_{i}\right), \frac{1}{r_{i}^{\prime 2}} g_{i}^{\prime}, p_{i}\right)$$
converges to an ALE orbifold $\left(Z_{\infty}, g_{\infty}^{\prime \prime}, z_{\infty}\right)$. The limit ( $Z_{\infty}, g_{\infty}^{\prime \prime}, z_{\infty}$ ) is called a 'deeper bubble' to the previous bubble $\left(Y_{\infty}, g_{\infty}^{\prime}, y_{\infty}\right)$. Iteratively, for each energy concentration point in a bubble, we can consider the rescaled limit (by energy scale) and obtain an ALE orbifold limit as a deeper bubble. Since the total energy is finite and each deeper bubble loses a definite amount of energy, there are at most finite iteration steps. The smooth bubbles with no energy concentration points are called the 'deepest bubbles'. By gluing each deeper bubble to the corresponding singularity in the previous bubble, we obtain a topological space which is called the 'bubble tree'. The bubble tree is homeomorphic to $B_{\delta}\left(x_{i}\right)$ for $i$ sufficiently large. We refer the reader to [Ban90] for a more detailed description of the bubbling process in the Einstein case, and [TV05b] for the SFK case.
If the bubble tree has only 1 branch, then the original manifold $X_{i}$ for $i$ sufficiently large is diffeomorphic to $X_{\infty} \# Y_{1} \# Y_{2} \# \cdots \# Y_{r}$, where $Y_{1}$ is the first bubble, and $Y_{r}$ is the deepest bubble. The notation \# stands for a generalized connected sum, which is obtained by attaching the boundary of a truncated ALE space onto the boundary of a punctured neighborhood of an orbifold point. By the

Mayer-Vietoris sequence, it follows that
$$b_{2}\left(X_{i}\right)=b_{2}\left(X_{\infty}\right)+\sum_{i=1}^{r} b_{2}\left(Y_{i}\right) .$$
A similar formula holds in the case of several branches.
In general, there can be energy concentration points which are smooth points of the limit space. In this case, the first bubble will be an asymptotically flat (AE) orbifold, that is, an ALE space with $\Gamma=\{e\}$. While these types of bubbles can certainly appear in general, one can rule out such bubbles which are topologically trivial.

Lemma 2.11. If ( $X, g, J$ ) is an AE SFK orbifold with $b_{2}(X)=0$, then ( $\left.X, J\right)$ is biholomorphic to $\mathbb{C}^{2}$ and $g$ is the flat metric.

Proof. Consider the minimal resolution of $(\widetilde{X}, \widetilde{J})$ of $(X, J)$. By a basic local gluing argument on the level of Kähler potentials (see [AP06] and also [ALM14]) we can glue on Lock-Viaclovsky ALE metrics (see [LV19]) on resolutions at the orbifold points to show that this resolution admits an ALE Kähler metric. By [HL16, Proposition 4.3], $(\widetilde{X}, \widetilde{J})$ is biholomorphic to $\mathbb{C}^{2}$ blown up at finitely many points. Since $b_{2}(X)=0$, this implies that $X$ is obtained from $\widetilde{X}$ by blowing down all possible holomorphic curves, and is therefore biholomorphic to $\mathbb{C}^{2}$. The Hirzebruch signature theorem for an AE SFK metric states that,
$$\tau(X)=-\frac{1}{12 \pi^{2}} \int_{X}\left\|W^{-}\right\|^{2} d V_{g},$$
since $\tau\left(\mathbb{C}^{2}\right)=0$, this implies that $W^{-} \equiv 0$. The Chern-Gauss-Bonnet theorem in this setting states that
$$\chi(X)=\frac{1}{8 \pi^{2}} \int_{X}\left(\left\|W^{-}\right\|^{2}-\frac{1}{2}|E|^{2}\right) d V_{g}+1,$$
and since $\chi\left(\mathbb{C}^{2}\right)=1$, this implies that $E \equiv 0$, and consequently $g$ is flat. \(\square\)

\section*{3. Compactness I. Convergence of birational structure}

In this section, we investigate more closely the pointed Cheeger-Gromov convergence of the sequence of metrics in Theorem 1.5. By results of Tian-Viaclovsky discussed above in Section 2.5, a subsequence converges to an ALE SFK metric. The main issue here is there could be a 'jump' of complex structure at the limit, or a 'jump' of birational type of the limit, even if every metric in the
sequence is biholomorphic. For example, if we rescale down an ALE SFK metric on a Stein surface $X$ by $r_{i}^{2} \cdot g, r_{i} \rightarrow 0$, the pointed Cheeger-Gromov limit is the flat cone $\mathbb{C}^{2} / \Gamma$. This limit is not birationally equivalent to $X$ since $X$ is Stein and smooth. However, note that in the setting of Theorem 1.5 with fixed complex structure and varying Kähler classes, such rescaling is excluded. Note also that as of yet, we do not know that the convergence is uniform at infinity, which is what we prove next (we do not even know yet that the group at infinity of the limit is the same for the limit as for the sequence).

Let $\Psi: X \backslash K \rightarrow \mathbb{R}^{4} / \Gamma$ be an ALE coordinate of order $O\left(r^{-\mu}\right)$ for $(X, J$, $g_{0}, x_{0}$ ), where $-2<-\mu<-1$. Recall as discussed in Section 2.3 above, there exist holomorphic functions $u^{1}, \ldots, u^{N}$ satisfying certain polynomial relations that determine the birational type of $(X, J)$. To prove the convergence of the birational structure, we need to show convergence of $u^{j}$ in a strong sense after the uniform Cheeger-Gromov diffeomorphism is applied.

Proposition 3.1. Let $\left(X, J, g_{i}\right)$ be the sequence of ALE SFK metrics as in Theorem 1.5 with group $\Gamma$ at infinity. Then there exist base points $x_{i} \in X$ such that the following holds:
\begin{itemize}
\item[(1)] Up to a subsequence, $\left(X, J, g_{i}, x_{i}\right)$ pointed Cheeger-Gromov converges with a uniform ALE asymptotic rate of order $O\left(r^{-\mu}\right)$ to an ALE SFK orbifold $\left(X_{\infty}, J_{\infty}, g_{\infty}, x_{\infty}\right)$. In particular, the group at infinity of the limit is also $\Gamma$.
\item[(2)] The limit space $X_{\infty}$ is birationally equivalent to $X$.
\item[(3)] There exists a constant $R>0$, such that all holomorphic curves are contained in geodesic ball $B_{R}\left(x_{i}, g_{i}\right)$ when $i$ is sufficiently large.
\end{itemize}

Proof. By the convergence results discussed in Section 2.5 above, for any sequence of basepoints $x_{i} \in X$, there exists a pointed Cheeger-Gromov limit
$$\left(X, J, g_{i}, x_{i}\right) \rightarrow\left(X_{\infty}, J_{\infty}, g_{\infty}, x_{\infty}\right) .$$
Without loss of generality, we can assume that $x_{\infty}$ is the only energy concentration point in the limit $X_{\infty}$, and that $x_{i}$ is chosen so that $\sup _{X}\left(\left\|R m\left(g_{i}\right)\right\|_{g_{i}}\right)$ is obtained at $x_{i}$.

First, let us assume the sequence $\left\{\left(X, J, g_{i}, x_{i}\right)\right\}$ has a uniform ALE energy bound, that is, that the assumption (3) in Lemma 2.10 is satisfied. (We then prove below that this assumption is necessarily satisfied). Under this assumption, by Lemma 2.10, there exist diffeomorphisms
$$\psi_{i}: X_{\infty} \backslash B_{\delta}\left(x_{\infty}\right) \rightarrow X$$
such that, $\left\|\psi_{i}^{*} g_{i}-g_{\infty}\right\|_{C_{-\mu}^{k, \alpha}\left(g_{\infty}\right)}<\epsilon(i \mid k, \delta),\left\|\psi_{i}^{*} J-J_{\infty}\right\|_{C_{-\mu}^{k, \alpha}\left(g_{\infty}\right)}<\epsilon(i \mid k, \delta)$, for $-2<-\mu<-1$.
Under this assumption, we next analyze the birational structure of the limit space. Recall that, for each $\left(X, J, g_{i}, x_{i}\right)$, there exists a harmonic coordinate $H_{i}: X \backslash B_{R}\left(x_{i}\right) \rightarrow \mathbb{R}^{4} / \Gamma$, under which $H_{i *} g_{i}, H_{i *} J$ are asymptotic to $g_{\text {Euc }}, J_{\text {Euc }}$ uniformly of rate $O\left(r^{-\mu}\right)$. In the following, we fix an $R>0$, and consider ( $H_{i *} g_{i}$, $\left.H_{i *} J\right)$ on the fixed space $A_{R, \infty}(0) \subset \mathbb{R}^{4} / \Gamma$. Furthermore, all the norms used in the following are over the space $A_{R, \infty}(0)$.
Recall the construction in Section 2.3. Since $(X, J)$ is a Kähler surface with an ALE coordinate $\Psi, X$ can be compactified analytically to $\hat{X}$, and there exist holomorphic functions $u^{1}, \ldots, u^{N}$ that determines the birational structure of $X$, obtained from holomorphic sections on $\hat{X}$. Define the degree of a function $f$ on $X$ with respect to the coordinate $\Psi$ as
$$d_{\Psi}(f)=\lim _{r \rightarrow \infty}\left(\frac{\log \left(\sup _{p \in S_{r}}\left|f\left(\Psi^{-1}(p)\right)\right|\right)}{\log (r)}\right)$$
where $r$ is the $g_{\text {Euc }}$-radius and $S_{r}$ is the $r$-sphere centered at $\{0\}$ in $A_{R, \infty}(0)$. For each $u^{j}$ above, $d_{\Psi}\left(u^{j}\right)$ is finite. Then we can rearrange $u^{1}, \ldots, u^{N}$ in the increasing order of $d_{\psi}$, and we have positive integers $d_{1}, \ldots, d_{l}$, such that there are $n_{j}$ th many elements among $u^{1}, \ldots, u^{N}$ that have degree of $d_{j}$, and $d_{j}<d_{j+1}$, $\sum_{j=1}^{l} n_{j}=N$. Define $\mathcal{H}$ as the $\mathbb{C}$-algebra of all holomorphic function on $X$ of finite $d_{\Psi}$-degree. We can assume $\left\{u^{1}, \ldots, u^{N}\right\}$ is a minimal set of generators of $\mathcal{H}$.

In a similar fashion, we can define $d_{H_{\infty}}$ for holomorphic functions on $X_{\infty}$, with respect to the ALE coordinate $H_{\infty}$ on $X_{\infty}$. There exist holomorphic functions $u_{\infty}^{1}$, $\ldots, u_{\infty}^{N}$ on $X_{\infty}$, which comprises a minimum set of generators of the $\mathbb{C}$-algebra of holomorphic functions on $X_{\infty}$ of finite $d_{H_{\infty}}$-degree.

We claim that $l_{\infty}=l, n_{j}^{\infty}=n_{j}, d_{j}^{\infty}=d_{j}$. This follows by constructing the deformation to the normal cone for both $X$ and $X_{\infty}$ as described above in (2.10). The line bundle $L$ is deformed to $\underline{L}$ along the deformation as $t \rightarrow 0$. Since $H^{0}(D$, $\left.\underline{L}^{k}\right) \simeq H^{0}\left(D, L^{k}\right)$, there exists $s_{j} \in H^{0}\left(C(D), \underline{L}^{k}\right)$ that corresponds with $s_{j}$. The normal cone $C(D)$ admits a flat conical metric $g_{C}$, so we can define the degree $\underline{d}_{j}$ for each $\underline{u}^{j}=\underline{s}_{j} / \underline{s}_{0}$ in a similar way. The metric cone $\left(C(D), g_{C}\right)$ is the tangent cone at infinity of $\left(X, g_{0}\right)$ and $\underline{u}^{j}$ is the scale-down limit of $u^{j}$, so it follows that $\underline{d}_{j}=d_{j}$, and consequently $\underline{n}_{j}=n_{j}, \underline{l}=l$. Applying the same argument to $\left(X_{\infty}, J_{\infty}\right)$ proves the claim.
Next, we study the convergence of the generating holomorphic functions. Let $u$ be a holomorphic function on $X$ with $d_{\Psi}(u)=d_{1}$, which is the lowest degree of a nonconstant holomorphic function. Since $\left\|H_{i *} u\right\|_{C_{d_{1}}^{0, \alpha}\left(H_{i *} g_{i}\right)}$ is finite, there exists a sequence of positive constants $c_{i}$, such that on $A_{R, \infty}(0),\left\|H_{i *}\left(c_{i} u\right)\right\|_{C_{d_{1}}^{0, \alpha}\left(H_{i *} g_{i}\right)}=1$.

Up to a subsequence, $H_{i *}\left(c_{i} u\right)$ pointwise converges to a limit function $w$, because on any annulus $A_{R, 2^{k+1} R}(0)$, the usual Hölder norm is uniformly bounded. We next use elliptic theory to refine the convergence.

Choose $\Delta_{H_{\infty *} g_{\infty}}$-harmonic functions $h_{1}, \ldots, h_{m}$ of $d_{H_{\infty}}$-degree $d_{1}$, such that for any function which is $\Delta_{H_{\infty *} g_{\infty}}$-harmonic and of $d_{H_{\infty}}$-degree $d_{1}$, its leading term can be represented as a linear combination of $h_{1}, \ldots, h_{m}$. Since $H_{i *} g_{i}$ converges to $H_{\infty *} g_{\infty}$ in any $C_{-\mu}^{k, \alpha}$-norm, for any $C^{2}$ function $f$, we have the pointwise bound
$$\left|\left(\Delta_{H_{\infty *} g_{\infty}}-\Delta_{H_{i *} g_{i}}\right) f\right|<\epsilon(i)\left(r^{-\mu} \cdot\left|\nabla_{H_{\infty *} g_{\infty}}^{2} f\right|+r^{-\mu-1} \cdot\left|\nabla_{H_{\infty *} g_{\infty}} f\right|\right),$$
where $\epsilon(i) \rightarrow 0$ as $i \rightarrow \infty$, and for any function $f$ with bounded $C_{\nu}^{2, \alpha}\left(H_{\infty *} g_{\infty}\right)$ - norm, we have
$$\left\|\left(\Delta_{H_{\infty *} g_{\infty}}-\Delta_{H_{i *} g_{i}}\right) f\right\|_{C_{\nu-\mu-2}^{0, \alpha}\left(H_{\infty *} g_{\infty}\right)}<\epsilon(i \mid \nu) \cdot\|f\|_{C_{\nu}^{2, \alpha}\left(H_{\infty *} g_{\infty}\right)}$$
where $\epsilon(i \mid \nu) \rightarrow 0$ as $i \rightarrow \infty$ for each fixed weight $\nu$. By the classical elliptic estimate in weighted norms (see [Bar86]), we have
$$\|f\|_{C_{d_{1}}^{2, \alpha}\left(H_{\infty *} g_{\infty}\right)}<C \cdot\left(\|f\|_{C_{d_{1}}^{0, \alpha}\left(H_{\infty *} g_{\infty}\right)}+\left\|\Delta_{H_{\infty *} g_{\infty}} f\right\|_{C_{d_{1}-2}^{0, \alpha}\left(H_{\infty *} g_{\infty}\right)}\right) .$$
Since $H_{i *}\left(c_{i} u\right)$ is $\Delta_{H_{i *} g_{i}}$-harmonic and $\left\|H_{i *}\left(c_{i} u\right)\right\|_{C_{d_{1}}^{0, \alpha}\left(H_{\infty *} g_{\infty}\right)}$ is uniformly bounded, the above estimates imply $\left\|H_{i *}\left(c_{i} u\right)\right\|_{C_{d_{1}}^{2, \alpha}\left(H_{\infty *} g_{\infty}\right)}<C$ for some uniform $C>0$. In particular, by estimate (3.5), and the invertibility of the Laplacian on the complement of a ball, there exists a function $\xi_{i} \in C_{d_{1}-\mu}^{2, \alpha}\left(H_{\infty *} g_{\infty}\right)$, such that $\Delta_{H_{\infty * g_{\infty}}} \xi_{i}=\Delta_{H_{\infty *} g_{\infty}}\left(H_{i *}\left(c_{i} u\right)\right)$ and
$$\left\|\xi_{i}\right\|_{C_{d_{1}-\mu}^{2, \alpha}\left(H_{\infty *} g_{\infty}\right)}<C \cdot\left\|\Delta_{H_{\infty *} g_{\infty}} H_{i *}\left(c_{i} u\right)\right\|_{C_{d_{1}-\mu-2}^{0, \alpha}\left(H_{\infty *} g_{\infty}\right)}<C \cdot \epsilon\left(i \mid d_{1}\right) .$$
By existence of harmonic expansions, we have the decomposition
$$H_{i *}\left(c_{i} u\right)=\xi_{i}+\sum_{j=1}^{m} a_{i, j} h_{j}+v_{i}$$
for some functions $v_{i}$ on $A_{R, \infty}(0)$. Then by the estimate of $H_{i *}\left(c_{i} u\right)$ above and
$$\left\|\xi_{i}\right\|_{C_{d_{1}}^{2, \alpha}\left(H_{\infty *} g_{\infty}\right)}<C \cdot\left\|\xi_{i}\right\|_{C_{d_{1}-\mu}^{2, \alpha}\left(H_{\infty *} g_{\infty}\right)}<C \cdot \epsilon\left(i \mid d_{1}\right),$$
we have $\sum_{j=1}^{m}\left|a_{i, j}\right|<C$ for some constant $C>0$, and there exists finite limit $a_{j}=\lim _{i \rightarrow \infty} a_{i, j}$ for each $1 \leqslant j \leqslant m$. Furthermore, $v_{i}$ is a $\Delta_{H_{\infty *} g_{\infty}}$ - harmonic function with degree $d_{H_{\infty}}\left(v_{i}\right)<d_{1}$. By the elliptic estimate (3.6), for $0<\epsilon^{\prime}<1$, we have $\left\|v_{i}\right\|_{C_{d_{1}-\epsilon^{\prime}}^{2, \alpha}}<C$ for a uniform $C>0$. Since $C_{d_{1}-\epsilon^{\prime}}^{2, \alpha}\left(H_{\infty *} g_{\infty}\right)$
is compactly embedded into $C_{d_{1}}^{0, \alpha}\left(H_{\infty *} g_{\infty}\right)$, we have $v_{i}$ converges strongly in $C_{d_{1}}^{0, \alpha}\left(H_{\infty *} g_{\infty}\right)$-norm on $A_{R, \infty}(0)$. Then by the analysis above, $v_{i}, \sum_{j=1}^{m} a_{i, j} h_{j}, \xi_{i}$ converge strongly in $C_{d_{1}}^{0, \alpha}\left(H_{\infty *} g_{\infty}\right)$-norm on $A_{R, \infty}(0)$ as $i \rightarrow \infty$. This implies that $H_{i *}\left(c_{i} u\right)$ converges to a limiting function $w$ strongly in $C_{d_{1}}^{0, \alpha}\left(H_{\infty *} g_{\infty}\right)$-norm, which satisfies
$$1-\epsilon<\|w\|_{C_{d_{1}}^{0, \alpha}\left(H_{\infty *} g_{\infty}\right)}<1+\epsilon$$
for some small $\epsilon>0$. By the convergence of the metric and the complex structure, we also have $w$ is $\Delta_{H_{\infty *} g_{\infty}}$-harmonic and $H_{\infty *} J_{\infty}$-holomorphic on $A_{R, \infty}(0)$. Since $X_{\infty}$ is a one-convex space, $w$ can be extended to a holomorphic function on $X_{\infty}$. Recall that $u$ is a nonconstant holomorphic function of finite degree on $X$, and the zero locus of $H_{i *}\left(c_{i} u\right)$ is a $H_{i *} J$-analytic subset which intersects with any annulus $A_{r, 2 r}(0)$ nontrivially for $r$ large enough. This implies that $\inf _{A_{r, 2 r}(0)}|w|=0$. Since $\|w\|_{C_{d_{1}}^{0, \alpha}\left(H_{\infty *} g_{\infty}\right)}>1-\epsilon$, we have $w$ is a nonconstant $H_{\infty *} J_{\infty}$-holomorphic function on $A_{R, \infty}(0)$. Since $\|w\|_{C_{d_{1}}^{0}\left(H_{\infty *} g_{\infty}\right)}$ is bounded, and $d_{1}$ is the lowest possible $d_{H_{\infty}}$ - degree for a nonconstant holomorphic function, we have $d_{H_{\infty}}(w)=d_{1}$ and $\sum_{j=1}^{m}\left|a_{j}\right|>0$.

Next, we want to show that there exists some positive constant $C>0$, such that $\frac{1}{C}<\left|c_{i}\right|<C$ for $i$ sufficiently large. By the convergence of $\xi_{i}, \sum_{j=1}^{m} a_{i, j} h_{j}, v_{i}$ as above, the $d_{1}$-degree term of $H_{i *}\left(c_{i} u\right)-w-\xi_{i}$ can be represented as $\sum_{j=1}^{m} b_{i, j} h_{j}$, where $b_{i, j} \rightarrow 0$ as $i \rightarrow \infty$. Then for $i$ sufficiently large, the $d_{1}$-degree term of $H_{i *}\left(c_{i} u\right)$ 'approximately' equals to the $d_{1}$-degree term of $w$. Define the 'growth ratio' for any $H_{\infty *} J_{\infty}$-holomorphic function $h$ on $A_{R, \infty}(0)$ with $d_{H_{\infty}}(h)=d$ by
$$I_{H_{\infty}}(h)=\lim _{r \rightarrow \infty}\left(\sup _{p \in S_{r}} \frac{|h(p)|}{r^{d}}\right) .$$
It is not hard to see that $I_{H_{\infty}}(w)$ is well defined and $0<I_{H_{\infty}}(w)<\infty$ unless $w$ is trivial. Similarly, we can define $I_{H_{i}}$ and $I_{\Psi}$ for $H_{i *} J$-holomorphic functions and $\Psi_{*} J$-holomorphic functions with respect to the corresponding coordinates. By the approximation above, $I_{H_{\infty}}(w) \approx\left|c_{i}\right| \cdot I_{H_{\infty}}\left(H_{i *} u\right)$. Since $g_{i}$ is an ALE Kähler metric over both the $\Psi$ and $H_{i}$ coordinates, by [Bar86, Corollary 3.2],
$$\overline{H_{i}}=A_{i} \cdot \bar{\Psi}+\text { lower order term },$$
where $\overline{H_{i}}, \bar{\Psi}$ are the universal covers of the coordinates, and $A_{i} \in U(2)$. It follows that $I_{\Psi}\left(\Psi_{*} u\right)=I_{H_{i}}\left(H_{i *} u\right)$, and since the harmonic coordinate $H_{i}$ converges to $H_{\infty}$, we also have $I_{H_{i}}\left(H_{i *} u\right)=I_{H_{\infty}}\left(H_{i *} u\right)$. Then we have $I_{H_{\infty}}(w) \approx\left|c_{i}\right| I_{\Psi}\left(\Psi_{*} u\right)$. Since $0<I_{\Psi}\left(\Psi_{*} u\right)<\infty$, there exists a constant $C>0$, such that for $i$ sufficiently large, $\frac{1}{C}<\left|c_{i}\right|<C$.

As a result, without loss of generality, we can assume $c_{i}=1$, and up to a subsequence, $H_{i *} u$ converges to a $H_{\infty *} J_{\infty}$-holomorphic function $w$ strongly in $C_{d_{1}}^{0, \alpha}\left(A_{R, \infty}(0), H_{\infty *} g_{\infty}\right)$-norm, and $d_{H_{\infty}}(w)=d_{\psi}(u)=d_{1}$. Then for generators $u^{1}, \ldots, u^{n_{1}}$ of holomorphic functions with $d_{\Psi}$-degree $d_{1}$, up to a subsequence, the functions $H_{i *} u^{1}, \ldots, H_{i *} u^{n_{1}}$ converge to $H_{\infty *} J_{\infty}$-holomorphic functions $w^{1}, \ldots$, $w^{n_{1}}$ of $d_{H_{\infty}}$-degree $d_{1}$. We claim that $w^{1}, \ldots, w^{n_{1}}$ are $\mathbb{C}$-linear independent, and are therefore generators of $H_{\infty *} J_{\infty}$-holomorphic functions of degree $d_{1}$. To see this, if there was any linear relation $\sum_{j=1}^{m} c_{j} w^{j}=0$, then for $i$ sufficiently large,
$$\sum_{j=1}^{m} c_{j} H_{i *} u^{j}=H_{i *}\left(\sum_{j=1}^{m} c_{j} u^{j}\right)$$
would be very small pointwise for all $r$ sufficiently large, which is a contradiction to the linear independence of $u^{1}, \ldots, u^{n_{1}}$.