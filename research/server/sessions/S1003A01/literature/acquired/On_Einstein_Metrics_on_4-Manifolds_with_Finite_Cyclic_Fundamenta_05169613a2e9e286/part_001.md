---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: On Einstein Metrics on 4-Manifolds with Finite Cyclic Fundamental Group]

---
source_file: 0804_4823.pdf
converter: mathpix
format: mmd
---

\title{
ON EINSTEIN METRICS ON 4-MANIFOLDS WITH FINITE CYCLIC FUNDAMENTAL GROUP
}

\author{
IOANA ŞUVAINA
}

\begin{abstract}
The existence or non-existence of Einstein metrics on 4manifolds with non-trivial fundamental group and the relation with the underlying differential structure are analyzed. For most points $(n, m)$ in a large region of the integer lattice, the manifold $n \mathbb{C P}^{2} \# m \overline{\mathbb{C P}^{2}}$ is shown to admit infinitely many inequivalent free actions of finite cyclic groups and there are no Einstein metrics which are invariant under any of these actions. The main tools are Seiberg-Witten theory, cyclic branched coverings of complex surfaces and symplectic surgeries.
\end{abstract}

\section*{1. Introduction}

The classical obstructions to the existence of an Einstein metric on a four-manifold are topological. If $(M, g)$ is a smooth compact oriented fourmanifold endowed with an Einstein metric $g$ then its Euler characteristic, $\chi(M)$, must be non-negative and it satisfies the Hitchin-Thorpe inequality:
$$(2 \chi \pm 3 \tau)(M) \geq 0$$
where $\tau(M)$ is the signature of $M$. Moreover, the equality is obtained only for manifolds which are covered by a flat 4-torus, the K3 surface with a hyperkähler metric or these with the reverse orientations.

Using the Seiberg-Witten equations, LeBrun [LeB96] found obstructions to the existence of Einstein metrics on a large class of manifolds for which the topological obstructions are satisfied. He later refined his arguments to improve the numerical condition in the obstruction. The main obstruction theorem that we are going to use in this paper is the following:

Theorem 1.1. [LeB01] Let $X$ be a compact oriented 4-manifold with a nontrivial Seiberg-Witten invariant and with $(2 \chi+3 \tau)(X)>0$. Then
$$M=X \# k \overline{\mathbb{C P}^{2}}$$
does not admit Einstein metrics if $k \geq \frac{1}{3}(2 \chi+3 \tau)(X)$.
These obstructions provided the means of exhibiting the strong dependence of the existence of Einstein metrics on the differential structure of the underlying four-manifold. Examples of pairs of homeomorphic but not diffeomorphic simply connected manifolds such that one manifold admits an Einstein metric while the other does not were first found by Kotschick
[Kot98]. Later on, other examples were constructed by LeBrun, Kotschick, the two in joint work with collaborators [IsLe02, IsLe03, BrKo05] and by others [RaSu09, IsRaSu09] in order to exhibit the existence or non existence of Einstein metrics for infinitely many homeomorphic non diffeomorphic smooth structures on the same topological space.

The explicit examples which are emphasized in the literature are of simplyconnected manifolds. In this paper we will analyze the case of non-simply connected manifolds. We also study some immediate consequences on the obstruction of invariant Einstein metrics on the standard smooth structure on the connected sum of complex projective planes and complex projective planes with reversed orientation.

Our first theorem is about manifolds with arbitrary finite cyclic fundamental group:

Theorem A. For any finite cyclic group $\mathbb{Z} / d \mathbb{Z}, d>1$, there exist infinitely many families of compact oriented smooth 4-manifolds $\left(Z_{i},\left\{M_{i, j}\right\}_{j \in \mathbb{N}}\right)_{i \in \mathbb{N}}$, all having fundamental group $\mathbb{Z} / d \mathbb{Z}$ and satisfying:
\begin{itemize}
\item[1.] For i fixed, any two manifolds in $\left\{Z_{i}, M_{i, j}\right\}$ are homeomorphic but not diffeomorphic to each other;
\item[2.] $Z_{i}$ admits an Einstein metric, while no $M_{i, j}$ admits an Einstein metric.
\end{itemize}

Moreover their universal covers, $\widetilde{Z}_{i}$ and $\widetilde{M_{i, j}}$, satisfy:
\begin{itemize}
\item[3.] $\widetilde{M_{i, j}}$ is diffeomorphic to $n \mathbb{C P}^{2} \# m \overline{\mathbb{C P}}^{2}$, where $n=b_{2}^{+}\left(\widetilde{Z}_{i}\right)$ and $m=b_{2}^{-}\left(\widetilde{Z}_{i}\right)$;
\item[4.] $\widetilde{Z}_{i}$ and $\widetilde{M_{i, j}}$ are not diffeomorphic, but become diffeomorphic after taking the connected sum with one copy of $\mathbb{C P}^{2}$.
\end{itemize}

This theorem generalizes the results on simply connected manifolds in [Kot98, Theorem 1.3] and [BrKo05, Theorem 2].

In [IsLe02, BrKo05], it was proved that on $n \mathbb{C P}^{2} \# m \overline{\mathbb{C P}}^{2}$ there are infinitely many distinct non standard structures for which no Einstein metric exists, for suitable $n, m$. But there is not much known about the properties of the metrics on standard smooth structure. Using constructions similar to the ones in the proof of Theorem A, we study Einstein metrics which are invariant under the actions of $\mathbb{Z} / d \mathbb{Z}$. Two of the examples with the smallest topological invariants are the following:

Proposition 1.2. 1. There exists a smooth, orientation preserving, involution $\sigma$ acting freely on the manifold $15 \mathbb{C P}^{2} \# 77 \overline{\mathbb{C P}^{2}}$ such that $15 \mathbb{C P}^{2} \# 77 \overline{\mathbb{C P}^{2}}$ does not admit a $\sigma$-invariant Einstein metric.
\begin{itemize}
\item[2.] There exists a free, smooth, orientation preserving action of $\mathbb{Z} / 3 \mathbb{Z}$ on $23 \mathbb{C P}^{2} \# 116 \overline{\mathbb{C P}^{2}}$, such that $23 \mathbb{C P}^{2} \# 116 \overline{\mathbb{C P}^{2}}$ does not admit a $\mathbb{Z} / 3 \mathbb{Z}$ invariant Einstein metric.
\end{itemize}

As we are discussing the geography of Einstein 4-manifolds, it is convenient to consider the following topological invariant $2 \chi+3 \tau$. This is equal
to the Chern number $c_{1}^{2}$ when the manifold supports an almost complex structure. To simplify the notations, we will denote $2 \chi+3 \tau$ by $c_{1}^{2}$ for any 4-manifold. Then the Hitchin-Thorpe inequality for Einstein manifolds requires that $c_{1}^{2} \geq 0$, with equality only in the few, known, special cases. A second topological invariant which we use is the Todd genus $\chi_{h}=\frac{\chi+\tau}{4}$. This invariant is a positive integer for manifolds which have finite fundamental group, and $b_{2}^{+}$odd, which is the case for 4-manifolds supporting an almost-complex structure, or the ones constructed by simple surgeries as in our paper. When the manifold supports an integrable complex structure, $\chi_{h}$ computes the holomorphic Euler characteristic. The Hitchin-Thorpe inequality $2 \chi-3 \tau \geq 0$ is equivalent to $c_{1}^{2} \leq 9.6 \chi_{h}$. For both examples in Proposition 1.2, the quotient manifolds have the following invariants: $c_{1}^{2}=1$ and $\chi_{h}=4$.

Theorem B. For any integer $d \geq 2$ and any $\epsilon>0$ there exists an $N(\epsilon)>0$ such that for any integer lattice point $(x, y)$ satisfying:
\begin{itemize}
\item[1.] free action admissibility condition: $d|x, d| y$,
\item[2.] either $0<y<(6-\epsilon) x-N(\epsilon)$ or $\left(9+\frac{\epsilon}{4}\right) x+\frac{1}{2} N(\epsilon)<y<9.6 x$ and $y$ is even,
\end{itemize}
there exist infinitely many inequivalent free $\mathbb{Z} / d \mathbb{Z}$-actions on the standard smooth manifold $X$ with $\chi_{h}(X)=x$ and $c_{1}^{2}(X)=y$. Moreover, there is no Einstein metric on $X$ invariant under any of the $\mathbb{Z} / d \mathbb{Z}$-actions.

The manifolds constructed in the theorem are diffeomorphic to $(2 x-$ 1) $\mathbb{C P}^{2} \#(10 x-y-1) \overline{\mathbb{C P}^{2}}$. The $\mathbb{Z} / d \mathbb{Z}$-actions are such that the quotient manifolds are homeomorphic, but not diffeomorphic. The differential structures are distinguished by their Seiberg-Witten invariants. As a consequence of the non-triviality of these invariants any invariant constant scalar curvature metric on $X$ must have non-positive constant. One important ingredient in the proof of the above result is the geography of almost completely decomposable symplectic manifolds, due to Braungardt and Kotschick [BrKo05].

Remark 1.1. For completeness, we mention the special when the manifolds are $\mathbb{C} \mathbb{P}^{2} \# m \overline{\mathbb{C} \mathbb{P}^{2}}, 0 \leq m \leq 8$. The existence of Einstein metrics is unobstructed by the Hitchin-Thorpe inequality, and in fact the standard smooth structure admits an Einstein metric of positive scalar curvature. This was given by the Fubini-Study metric for $m=0$, by Page [Pa79] for $m=1$, by Chen-LeBrun-Weber [CLW08] for $m=2$ and by Siu [Siu88] or Tian-Yau [TiYa87] for $3 \leq m \leq 8$. For $M=\mathbb{C P}^{2} \# m \overline{\mathbb{C P}^{2}}, 5 \leq m \leq 8$ the author and R. Răsdeaconu [RaSu09] showed that $M$ supports a nonstandard smooth structure which admits an Einstein metric of negative sign, as well as infinitely many smooth structures which do not admit Einstein metrics.

Remark 1.2. The result in Theorem B is stated for finite cyclic groups. However, it also holds for groups acting freely on the 3-dimensional sphere or for direct sums of the above groups.

In general, the existence or non-existence of Einstein metrics on an arbitrary manifold is hard to prove. On the remaining part of this paper we emphasize the non-existence of Einstein metrics on non-simply connected manifolds.

Theorem C. Let $G$ be any finitely presented group. There exists an infinite family of pairwise non-homeomorphic non-spin 4-manifolds $M_{i}, i \in \mathbb{N}$, with fundamental group $G$ such that each $M_{i}$ supports infinitely many distinct smooth structures $M_{i, j}, j \in \mathbb{N}$, which do not admit an Einstein metric. All $M_{i, j}$ satisfy Hitchin-Thorpe inequality.

The manifolds constructed in Theorems A, C are necessarily non-spin. However, using obstructions induced by a non-trivial Bauer-Furuta invariant [IsLe02, Theorem D], one can also find examples of spin manifolds which satisfy the Hitchin-Thorpe inequality, but do not admit Einstein metrics.
Theorem D. For any finite group $G$, there is an infinite family of spin 4 -manifolds $M_{i}$ with fundamental group $\pi_{1}\left(M_{i}\right)=G$ such that each space supports infinitely many distinct smooth structures, which do not admit an Einstein metric. All these manifolds satisfy the Hitchin-Thorpe inequality.

For a small fundamental group $\mathbb{Z} / d \mathbb{Z}$, some of the manifolds constructed in the theorem support a differential structure which admits a Kähler-Einstein metric, but most of the manifolds $M_{i}$ do not support a complex structure.

On simply connected spin manifolds it was proved that there are no Einstein metrics for some exotic smooth structures [IsLe02]. We prove that there are no $\mathbb{Z} / d \mathbb{Z}$-invariant Einstein metrics for the standard smooth structure on certain connected sums of $K 3$ 's and $S^{2} \times S^{2}$ 's.

Theorem E. There exists an $n_{0}>0$ such that for any $d>n_{0}$ the manifolds:
$$M_{1, n}=d(n+5)(K 3) \#(d(n+7)-1)\left(S^{2} \times S^{2}\right)$$
$$M_{2, n}=d(2 n+5)(K 3) \#(d(2 n+6)-1)\left(S^{2} \times S^{2}\right)$$
$n \in \mathbb{N}^{*}$, admit infinitely many inequivalent free $\mathbb{Z} / d \mathbb{Z}$-actions, such that there is no Einstein metric on $M_{1, n}, M_{2, n}$ invariant under any of the $\mathbb{Z} / d \mathbb{Z}$-actions.

The paper is organized as follows: in Section 2 we review some background results on the topology of 4-manifolds, in the third section we give a construction of manifolds which admit free $\mathbb{Z} / d \mathbb{Z}$-actions and in Section 4 we give the proofs of the above theorems.

Acknowledgments. I would like to thank Professor Claude LeBrun for suggesting the problem in Theorem A and for numerous discussions on the subject.

\section*{2. Background results on the topology of 4-manifolds}
2.1. Homeomorphism criteria. A remarkable result of Freedman [Fre82] and Donaldson [Don83] tells us that smooth compact simply connected oriented 4-manifolds are classified up to homeomorphism by their numerical
invariants: Euler characteristic $\chi$, signature $\tau$ and Stiefel-Whitney class $w_{2}$. In the non-simply connected case this was generalized in HaKr93, Theorem C]:

Theorem 2.1 (Hambleton, Kreck). Let $M$ be a smooth closed oriented 4manifold with finite cyclic fundamental group. Then $M$ is classified up to homeomorphism by the fundamental group, the intersection form on $H_{2}(M, \mathbb{Z})$ modulo torsion, and the $w_{2}$-type. Moreover, any isometry of the intersection form can be realized by a homeomorphism.

In contrast with simply connected manifolds, there are three $w_{2}$-types that can be exhibited: (I) $w_{2}(\widetilde{M}) \neq 0$, (II) $w_{2}(M)=0$, and (III) $w_{2}(\widetilde{M})=0$, but $w_{2}(M) \neq 0$.

Using Donaldson's and Minkowski-Hasse's classification of the intersection form we can reformulate this theorem on an easier form:

Remark 2.1. We have the following equivalent statement: a smooth, closed, oriented 4-manifold with finite cyclic fundamental group and indefinite intersection form is classified up to homeomorphism by the fundamental group, the numbers $b_{2}^{ \pm}$, the parity of the intersection form and the $w_{2}$-type.

In the presence of 2-torsion one must be careful to determine both the parity of the intersection form and the $w_{2}$-type, as there are known examples of non-spin manifolds with even intersection form, see for example the Enriques surface. On a 4-manifold with finite fundamental group, knowing the invariants $b_{2}^{ \pm}$is equivalent to knowing any other two numerical invariants, for example the Euler characteristic $\chi$ and signature $\tau$.
2.2. Almost complete decomposability. Freedman's and Donaldson's results tell us that any non-spin simply connected 4-manifold is homeomorphic to $n \mathbb{C P}^{2} \# m \overline{\mathbb{C P}^{2}}$, for appropriate positive integers $n, m$. Using nontriviality of the Seiberg-Witten invariants, infinitely many differential structures can be exhibited on many manifolds which admit a smooth, symplectic structure. In the case of $b_{2}^{+}>1$, such manifolds are never diffeomorphic to $n \mathbb{C P}^{2} \# m \overline{\mathbb{C P}^{2}}$ as the Seiberg-Witten invariant of the later manifold vanishes. One way of measuring how different the differential structures are, is by taking connected sum with a copy of $\mathbb{C} \mathbb{P}^{2}$. In this case, the Seiberg-Witten invariants of both manifolds vanish by Taubes' theorem. Hence it is natural to introduce the following definitions, due to Mandelbaum and Moishezon:

Definition 2.2. We say that a smooth, non-spin, 4-manifold $M$ is completely decomposable if it is diffeomorphic to a connected sum of $\mathbb{C P}^{2}$ 's and $\overline{\mathbb{C} \mathbb{P}^{2}}$ 's.

Definition 2.3. We say $M$ is almost completely decomposable (ACD) if $M \# \mathbb{C P}^{2}$ is completely decomposable.

Almost completely decomposable manifolds are quite common. It has been conjectured by Mandelbaum [Ma80] that simply connected analytic
surfaces are almost completely decomposable. In support of this conjecture he proved that any complex surface which is diffeomorphic to a complete intersection of hypersurfaces in some $\mathbb{C P}^{N}$ is almost completely decomposable. Moreover, he also considered the branched covers:

Proposition 2.4. Ma80 Let $X \subset \mathbb{C P}^{N}$ be a compact complex surface and suppose $M \longrightarrow X$ is an $r$-fold cyclic branched cover of $X$ whose branch locus is homeomorphic to $X \cap H_{r}$, for some hypersurface $H_{r}$ of degree $r$ of $\mathbb{C P}^{N}$. Then if $X$ is almost completely decomposable so is $M$.

For the definition of a $r$-fold cyclic cover see the next section.
Using iterated cyclic-covers of $\mathbb{C P}^{2}$ and symplectic surgeries, Braungardt and Kotschick, [BrKo05], were able to show the abundance of the ACD symplectic manifolds for fixed topological invariants:

Theorem 2.5. [BrKo05] For every $\epsilon>0$, there is a constant $c(\epsilon)>0$ such that every lattice point $(x, y)$ in the first quadrant satisfying
$$y \leq(9-\epsilon) x-c(\epsilon)$$
is realized by the Chern invariants $\left(\chi_{h}, c_{1}^{2}\right)$ of infinitely many, pairwise nondiffeomorphic, simply connected, minimal, symplectic manifolds, all of which are almost completely decomposable.

\section*{3. A construction of surfaces of general type with finite cyclic fundamental group}

One technique which yields a large family of examples of complex manifolds is the finite cyclic branched cover construction.

For more details on the constructions presented in this chapter we refer the reader to [BPV84] for an algebraic geometric point of view, or to [GoSt99] for a more topological description.

Definition 3.1. A (non-singular) $d$-fold branched cover consists of a triple $(X, Y, \pi)$, denoted by $\pi: X \rightarrow Y$, where $X, Y$ are connected compact smooth complex manifold and $\pi$ is a finite, generically $d$ : 1, surjective, proper, holomorphic map. The critical set, $R \subset X$, is called the ramification divisor of $\pi$ and its image $D=\pi(R)$ is called the branch locus.

For any point $y \in Y \backslash D$ there is a connected neighborhood $V_{y}$ with the property that $\pi^{-1}\left(V_{y}\right)$ consists of $d$ disjoint subsets of $X$, each of which is mapped isomorphically onto $V_{y}$ by $\pi$.
3.1. Cyclic branched covers. One special class of branched covers are the cyclic branched covers. They can be constructed as follows:

Construction 3.2. : Let $Y$ be a connected complex manifold and $D$ an effective divisor on $Y$. Let $\mathcal{O}(D)$ be the associated line bundle and $s_{D} \in$ $\Gamma\left(Y, \mathcal{O}_{Y}(D)\right)$ the section vanishing exactly along $D$. Suppose we have a line bundle $\mathcal{L}$ on $Y$ such that $\mathcal{O}_{Y}(D)=\mathcal{L}^{\otimes d}$. We denote by $L$ the total space of $\mathcal{L}$ and we let $p: L \rightarrow Y$ be the bundle projection. If $z \in \Gamma\left(L, p^{*} \mathcal{L}\right)$ is the
tautological section, then the zero divisor of $p^{*} s_{D}-z^{d}$ defines an analytic subspace $X$ in $L$. If $D$ is a smooth divisor then $X$ is smooth connected manifold and $\pi=\left.p\right|_{X}$ exhibits $X$ as a $d$-fold ramified cover of $Y$ with branch locus $D$. We call $(X, Y, \pi)$ the $d$-cyclic cover of $Y$ branch along $D$, determined by $\mathcal{L}$.

Given $D$ and $Y, X$ is uniquely determined by a choice of $\mathcal{L}$. Hence, $X$ is uniquely defined if $\operatorname{Pic}(Y)$ has no torsion.

A cyclic branched cover is a d-fold cover such that $\pi_{\mid X \backslash R}: X \backslash R \rightarrow Y \backslash D$ is a (regular) cyclic covering. Hence it is determined by an epimorphism $\pi_{1}(Y \backslash D) \rightarrow \mathbb{Z}_{d}$, and $Y=X / \mathbb{Z}_{d}$. Moreover, a cyclic $d$-cover is a Galois covering, meaning that the function field embedding $\mathbb{C}(Y) \subset \mathbb{C}(X)$ induced by $\pi$ is a Galois extension.

The following lemmas give us the main relations between the two manifolds:

Lemma 3.3. [BPV84] Let $\pi: X \rightarrow Y$ be a $d$-cyclic cover of $Y$ branched along a smooth divisor $D$ and determined by $\mathcal{L}$, where $\mathcal{L}^{\otimes d}=\mathcal{O}_{Y}(D)$. Let $R$ be the reduced divisor $\pi^{-1}(D)$ on $X$. Then:
\begin{itemize}
\item[(i)] $\mathcal{O}_{X}(R)=\pi^{*} \mathcal{L}$;
\item[(ii)] $\pi^{*}[D]=d[R]$, in particular $d$ is the branching order along $R$;
\item[(iii)] $\mathcal{K}_{X}=\pi^{*}\left(\mathcal{K}_{Y} \otimes \mathcal{L}^{d-1}\right)$.
\end{itemize}

As an immediate consequence, we are able to compute the relations between the topological invariants of $X$ and $Y$ in the case of complex surfaces:

Lemma 3.4. Let $X, Y$ complex surfaces and $\pi: X \rightarrow Y$ be as in Lemma 3.3. Then:
\begin{itemize}
\item[(i)] $c_{2}(X)=d c_{2}(Y)-(d-1) \chi(D)$;
\item[(ii)] $c_{1}^{2}(X)=d\left(c_{1}(Y)-(d-1) c_{1}(\mathcal{L})\right)^{2}$
\end{itemize}

In a more general set-up, we can define a d-cyclic branch cover $\pi: X \rightarrow Y$ branched along a divisor with simple normal crossing singularities and $Y$ smooth manifold. In this case, $X$ will be a normal complex surface ([BPV84] I.17.) with singularities over the singular points of $D$. In order to understand the type of singularity, we have to consider a small neighborhood of a singular point of $D, U \subset Y$. Let $(x, y)$ be local coordinates of $U$ such that $D$ is defined by the equation $x y=0$. Then $\pi^{-1}(0)$ is an isolated singularity of $X$ and the open neighborhood of $\pi^{-1}(0), \pi^{-1}(U) \subset X$ is modeled in local coordinates by $z^{d}=x y \subset \mathbb{C}^{3}$. This type of singularity is known as an $A_{d}$-singularity.

There are two techniques to associate a smooth manifold to $X$. The easiest method is to consider the resolution of the singularity (see for instance [BPV84, Chapter III, Theorems 6.1, 6.2]). For any normal surface $X$ there exist bi-meromorphic maps $\pi: X^{\prime} \rightarrow X$, with $X^{\prime}$ smooth, such that $\pi$ is an isomorphism outside the exceptional divisor $E=\pi^{-1}(\operatorname{Sing} X)$. If $\left(X^{\prime}, X, \pi\right)$ are chosen such that $E$ does not contain any rational curves of
self-intersection (-1), then the minimal resolution is called minimal. The minimal resolution is uniquely determined by the type of the singularities of $X$. A second method to eliminate singularities is given by deformations:

Definition 3.5. A smoothing of a normal surface $X$ is a proper flat map $f: \mathcal{X} \rightarrow \Delta$, smooth over $\Delta^{*}=\Delta \backslash 0$, where $\mathcal{X}$ is a three dimensional complex manifold, $\Delta$ is a small open disk in $\mathbb{C}$ centered at $0, f^{-1}(0)$ is isomorphic to $X$ and $f^{-1}(t)$ smooth if $t \neq 0$.

If $t, t^{\prime} \in \Delta^{*}$ then $f^{-1}(t)$ is diffeomorphic to $f^{-1}\left(t^{\prime}\right)$. In the case of cyclic branched coverings, a stronger result is true:

Proposition 3.6. If $\pi: X \rightarrow Y$ is a $d$-cyclic cover branched along a divisor $D$ with simple normal crossing singularities, such that the linear system $\mathbb{P}\left(H^{0}(Y, \mathcal{O}(D))\right)$ is base point free. Then, there is a smoothing $\varpi: \mathcal{X} \rightarrow \Delta$ of $X$ and the generic fiber $X_{t}=\varpi^{-1}(t)$ is diffeomorphic to the minimal resolution $X^{\prime}$ of $X$.

Proof. We will give the complete proof for the case of double covers and then argue using the properties of local deformations of $A_{d}$-singularities [HKK86] that the same is true in general.

First, we remark that $X$ has a finite number of singular points, corresponding to the singular points of $D$. Resolving these singularities is a local process. The singularity, modeled by $\left(z^{2}=x y\right) \subset \mathbb{C}^{3}$ is a quotient singularity. It is isomorphic to $\mathbb{C}^{2} / \mathbb{Z}_{2}$, where the $\mathbb{Z}_{2}$ action is given by the multiplication with -1, and the isomorphism is given by the map:
$$\mathbb{C}^{2} / \mathbb{Z}_{2} \rightarrow U, \widehat{(u, v)} \mapsto\left(u^{2}, v^{2}, u v\right)=(x, y, z) .$$
The minimal resolution of $\mathbb{C}^{2} / \mathbb{Z}_{2}$ can be constructed by blowing-up the origin of $\mathbb{C}^{2}$ extending the $\mathbb{Z}_{2}$ action trivially on the exceptional divisor and then considering the new quotient space. The total space of the blow-up of $\mathbb{C}^{2}$ is the line bundle $\mathcal{O}_{\mathbb{C P}^{1}}(-1)$, and factoring by the above $\mathbb{Z}_{2}$ action corresponds to squaring (tensor product) the line bundle. The resulting manifold, after taking the quotient, is $\mathcal{O}_{\mathbb{C P}^{1}}(-2)$. So, we resolved the singularities of $X$ by introducing an exceptional divisors which is a rational curve of self-intersection (-2).

Next, we explicitly construct a smoothing of $X$. The idea is to consider a smoothing of the branch locus and construct the corresponding double cover. As the linear system $\mathbb{P}\left(H^{0}(Y, \mathcal{O}(D))\right)$ is base point free, there exists a holomorphic path of sections of $\mathcal{O}(D)$ and a parametrization of this path given by $\varphi: \Delta \rightarrow \Gamma(Y, \mathcal{O}(D))$ such that $\varphi(0)=\varphi_{D}$ and $d \varphi_{\left.\right|_{0, \text { Sing }}} \neq 0$. The last condition implies that the curve $\varphi(t)=0, t \neq 0$ sufficiently small, doesn't contain any of the singularities of $D$. Moreover, by Bertini Theorem we can also assume that $\varphi_{t}:=\varphi(t), t \neq 0$ corresponds to a smooth divisor.

Let $\mathcal{X} \subset \mathcal{L} \times \Delta$ given locally by the equation $z^{2}-\varphi(t)(x, y)=0$, where $\mathcal{L} \rightarrow Y$ is a line bundle such that $\mathcal{L}^{2}=\mathcal{O}(D)$ and $z$ is a local coordinate on
the fiber of $\mathcal{L}$. Then $\varpi: \mathcal{X} \rightarrow \Delta$ is a smoothing of $X=\varpi^{-1}(0)$. First, we can show that $\mathcal{X}$ is a smooth manifold as:
$$d\left(z^{2}-\varphi(t)(x, y)\right)=2 z d z-\left(\frac{d}{d t} \varphi(t)(x, y)\right) d t-\left(\frac{d \varphi_{t}}{d x}(x, y) d x+\frac{d \varphi_{t}}{d y}(x, y) d y\right) \neq 0$$
This is never zero as for $t \neq 0$ the section $\varphi_{t}$ is smooth, hence the last parenthesis is non-zero and for $t=0$ we have $\left.\frac{d \varphi}{d t}\right|_{0, \text { Sing } D} \neq 0$ and $\left(\frac{d \varphi}{d x}+\right.$ $\left.\frac{d \varphi}{d y}\right)\left.\right|_{0, D \backslash \operatorname{Sing} D} \neq 0$. Then by Theorem 9.11 in Har77 the morphism $\varpi$ is flat.

The fact that the two constructions yield diffeomorphic manifolds is a local statement about the differential structures of the new manifolds in a neighborhood of the singularities. So, our proof is in local coordinates. Because the morphism $\varpi$ is a submersion away from the central fiber it is enough to show that one of the fibers is diffeomorphic to $X^{\prime}$.

In local coordinates the singularities are given by the equation
$$\left(z^{2}-x y=0\right) \subset \mathbb{C}^{3} .$$
Because the linear system associated to $\mathcal{O}(D)$ is base point free, then the zero locus of a generic section is smooth. We can consider a preferred local coordinates such that one of the smoothings, $X_{1}$, is given by ( $z^{2}-x y=$ $1) \subset \mathbb{C}^{3}$. If we change the local coordinates $(x, y, z)$ to $(u, v, z)$, such that $x=i u-v, y=i u+v$ then the smoothing is written in the canonical form $\left(z^{2}+u^{2}+v^{2}=1\right)$. Let $\xi=\operatorname{Re}(u, v, z), \eta=\operatorname{Im}(u, v, z), \xi, \eta \in \mathbb{R}^{3}$ the real, imaginary part, of ( $u, v, z$ ). Then:
$$\begin{aligned}
& X_{1}=\left\{(u, v, z) \in \mathbb{C}^{3} \mid z^{2}+u^{2}+v^{2}=1\right\} \\
& =\left\{(\xi, \eta) \in \mathbb{R}^{3} \times \mathbb{R}^{3} \mid\|\xi\|^{2}-\|\eta\|^{2}=1,<\xi, \eta>=0\right\} .
\end{aligned}$$
The map $f: X_{1} \rightarrow T^{*} S^{2} \subset \mathbb{R}^{3} \times \mathbb{R}^{3}$ defined by $f(\xi, \eta)=\left(\frac{\xi}{\|\xi\|},\|\xi\| \eta\right)$ is a orientation preserving diffeomorphism.

It is a well known fact that $\mathcal{O}_{\mathbb{C} \mathbb{P}^{1}}(-2)$ is diffeomorphic to $T^{*} S^{2}$, where exceptional divisor $\mathbb{C} \mathbb{P}^{1}$ is identified to the zero-section of the vector bundle. We have given an explicit construction for the case of double covers, as this sheds some light into the diffeomorphism between the minimal resolution and a smoothings, as well as emphasizes the different (local) holomorphic structures.

To prove the result for a $d$-cyclic cover, the extra ingredient needed is that the local smoothing of the singularities is diffeomorphic to its minimal resolution. For singularities of the form $z^{d}=x y$, or type $A_{d-1}$, the required diffeomorphism is proved by Harer, Kas and Kirby, [HKK86], by using topological Kirby calculus. \(\square\)

A similar statement is true for double covers branched along a divisor $D$ with simple singularities, i.e. the singularities are double or triple points with two or three different tangents or simple triple points with one tangent. The double cover branched along such a divisor has $A-D-E$ singularities, respectively. These singularities are called rational double points. It can be
proved [HKK86] that for these singularities, and only for these singularities, the minimal resolution and the smoothing are diffeomorphic.

Next we want to study the fundamental group of our manifolds. We need to introduce a new definition:

Definition 3.7. A smooth divisor $D$ is said to be flexible if there exists a divisor $D^{\prime} \equiv D$ such that $D \bigcap D^{\prime} \neq \emptyset$ and $D^{\prime}$ intersects $D$ transversally in codimension 2.

We remark that if $D$ is a flexible divisor then it must be connected.
Then, reformulating Catanese's Proposition 1.8 from [Cat84] in our easy situation, we have:

Proposition 3.8. [Cat84] Let $\pi: X \rightarrow Y$ a $d$-cyclic cover branched along a smooth flexible divisor $D$, then if $Y$ is simply connected so is $X$.

Notice that if the branch locus is not flexible then the covering manifold might not be simply connected: consider for example the double cover of $\mathbb{C P}^{1} \times \mathbb{C P}^{1}$ branched along four vertical $\mathbb{C} \mathbb{P}^{1}$.
3.2. Bi-cyclic covers of $\mathbb{C P}^{1} \times \mathbb{C P}^{1}$. In this section we introduce a new construction which we are going to call the simple bi-cyclic cover of $\mathbb{C P}^{1} \times$ $\mathbb{C P}^{1}$. Then, we study the analytical and topological properties of this class of manifolds. They are inspired by a construction due to Catanese. In his papers [Cat84], [Cat92], etc, he extensively studies two successive double covers of $\mathbb{C P}^{1} \times \mathbb{C P}^{1}$. For our purposes we need to consider cyclic covers of arbitrary degrees. We have the following construction:

Construction 3.9. Let $C, D$ be two smooth transversal curves in $\mathbb{C P}^{1} \times \mathbb{C P}^{1}$ such that the line bundles $\mathcal{O}(C), \mathcal{O}(D)$ are $d$, p-tensor powers of some line bundles on $\mathbb{C P}^{1} \times \mathbb{C P}^{1}$. We construct a new manifold $N$ by taking: first the $d$-cyclic cover of $\mathbb{C P}^{1} \times \mathbb{C P}^{1}$ branched along $C$, which we denote by $X$, and then the $p$-cyclic cover of this manifold branched along the proper transform of $D$. We have the following diagram:
$$N \rightarrow X \rightarrow \mathbb{C} \mathbb{P}^{1} \times \mathbb{C} \mathbb{P}^{1}$$
It can easily be checked that if $C, D$ are smooth and intersect transversally, then both $X$ and $N$ are smooth. We call the manifold $N$ a (simple) bi-cyclic cover of $\mathbb{C P}^{1} \times \mathbb{C P}^{1}$ of type ( $d, p$ ) branched along ( $C, D$ ).

Let $\pi_{1}, \pi_{2}: \mathbb{C P}^{1} \times \mathbb{C P}^{1} \rightarrow \mathbb{C P}^{1}$ be the projections on the first, second factor, respectively. The line bundles on $\mathbb{C} \mathbb{P}^{1} \times \mathbb{C P}^{1}$ are of the form $\pi_{1}^{*}\left(\mathcal{O}_{\mathbb{C P}^{1}}(a)\right) \otimes \pi_{2}^{*}\left(\mathcal{O}_{\mathbb{C P}^{1}}(b)\right)$, which we denote by $\mathcal{O}_{\mathbb{C P}^{1} \times \mathbb{C P}^{1}}(a, b)$ or simply $\mathcal{O}(a, b)$. With this notations, $\mathcal{O}(C)=\mathcal{O}(d a, d b)$ and $\mathcal{O}(D)=\mathcal{O}(p m, p n)$ where $a, b, m, n$ are non-negative integers. Let $\varphi_{C} \in \Gamma(\mathcal{O}(C))$ and $\varphi_{D} \in$ $\Gamma(\mathcal{O}(D))$ such that $C=\left\{\varphi_{C}=0\right\}$ and $D=\left\{\varphi_{D}=0\right\}$. Let $E$ be the total space of $\mathcal{E}=\mathcal{O}_{\mathbb{C P}^{1} \times \mathbb{C P}^{1}}(a, b) \oplus \mathcal{O}_{\mathbb{C P}^{1} \times \mathbb{C P}^{1}}(m, n)$ and $\pi: E \rightarrow \mathbb{C P}^{1} \times \mathbb{C P}^{1}$. Then the manifold $N$ can also be seen as a smooth compact submanifold of $E$. If $(z, w) \in \Gamma\left(E, \pi^{*} \mathcal{E}\right)$ is the tautological section, then $N$ is defined by
the following equations $\left\{z^{d}-\pi^{*} \varphi_{C}=0, w^{p}-\pi^{*} \varphi_{D}=0\right\}$. As an immediate consequence we obtain that Construction 3.9 is commutative, i.e. we obtain the manifold $N$ also as the type ( $p, d$ ) bi-cyclic cover of $\mathbb{C P}^{1} \times \mathbb{C P}^{1}$ branched along $(D, C)$.

Let $\pi$ be the projection from $N$ to $\mathbb{C} \mathbb{P}^{1} \times \mathbb{C P}^{1}$ induced by the fibration projection. Using Lemma 3.4, we can easily compute the topological invariants of $N$.

Lemma 3.10. Let $\pi: N \rightarrow \mathbb{C P}^{1} \times \mathbb{C P}^{1}$ be a bi-cyclic cover as above. Then:
\begin{itemize}
\item[1.] $K_{N}=\pi^{*}(\mathcal{O}((d-1) a+(p-1) m-2,(d-1) b+(p-1) n-2))$;
\item[2.] If $(d-1) a+(p-1) m \geq 3$ and $(d-1) b+(p-1) n \geq 3$ then $K_{N}$ is an ample line bundle;
\item[3.] $c_{1}^{2}(N)=2 p d((d-1) a+(p-1) m-2)((d-1) b+(p-1) n-2)$;
\item[4.] $c_{2}(N)=p d[4-2(d-1)(a+b-d a b)-2(p-1)(m+n-p m n)+$ $(p-1)(d-1)(a n+b m)]$.
\end{itemize}

Proof. The proofs of 1,3 and 4 are an immediate consequence of Lemmas 3.3 and 3.4. The extra ingredients that need to be computed are the Euler characteristics of the branch loci $C, D, \chi(C)=2 d((a+b)-d a b), \chi(D)=$ $2 p((m+n)-p m n)$, and $D^{\prime} \subset X$ the proper transform of $D . D^{\prime}$ is a $d$-cover of $D$ branched on $\operatorname{card}(C \cap D)=d p(a n+b m)$ points. Then: $\chi\left(D^{\prime}\right)=$ $d \chi(D)-(d-1)(C \cdot D)=p d(2(m+n-p m n)-(d-1)(a n+b m))$.

The canonical line bundle, $K_{N}$, is the pull-back of an ample line bundle through a finite map hence, see [Har77], $K_{N}$ is ample. \(\square\)

Next we analyze the topological properties of our manifolds.
Lemma 3.11. If $\pi: N \rightarrow \mathbb{C P}^{1} \times \mathbb{C P}^{1}$ be a bi-cyclic cover as above and $a, b, m, n$ are strictly positive integers, then $N$ is simply connected.

Proof. If $a, b, m, n$ are strictly positive integers, then the divisors $C, D$ are flexible divisors and applying Proposition 3.8 twice gives us that the manifold $N$ is simply connected. \(\square\)

As $N$ is a Kähler manifold it has non-trivial Seiberg-Witten invariants. Hence it does not decompose as connected sums of $\mathbb{C P}^{2}$ 's and $\overline{\mathbb{C P}^{2}}$ 's. At most we can hope that it will decompose after taking the connected sum with a copy of $\mathbb{C P}^{2}$. We have a more general statement:

Theorem 3.12. Iterated cyclic covers of $\mathbb{C P}^{1} \times \mathbb{C P}^{1}$ branched along smooth, flexible curves, such that any two curves intersect transversally, are almost completely decomposable.

Proof. We prove the theorem by double induction on the number of covers and the degree of the last cover. First we show that the $d$-cover $\pi_{2}$ : $X \rightarrow \mathbb{C} \mathbb{P}^{1} \times \mathbb{C P}^{1}$ branched along $C$ is almost completely decomposable. Let $\varphi_{(a, b)}: \mathbb{C} \mathbb{P}^{1} \times \mathbb{C P}^{1} \rightarrow \mathbb{C} \mathbb{P}^{P}$, where $P=(a+1)(b+1)-1$, be the Segre-type embedding, and $\left[p_{i j}\right]$ be homogeneous coordinates on $\mathbb{C P}^{P}$ corresponding
to $(a, b)$-bi-homogeneous monomials. Then if $\varphi_{C}$ is the bi-degree $(d a, d b)$ polynomial whose zero locus is $C$, then $\varphi_{C}=\varphi_{(a, b)}^{*}\left(f\left(p_{i j}\right)\right)$, where $f$ is a degree $d$ polynomial. Hence, by Proposition 2.4, $X$ is almost completely decomposable.

We need one more ingredient. The following lemma is proved in MaMo80:
Lemma 3.13. ([MaMo80], 3.4) Suppose W is a compact complex 3-manifold and $V, X_{1}, X_{2}$ are closed simply-connected complex submanifolds with normal crossing in $W$. Let $S=X_{1} \bigcap X_{2}$ and $C=V \bigcap S$. Suppose as divisors $V$ is linearly equivalent to $X_{1}+X_{2}$ and that $C \neq \emptyset$. Set $n=\operatorname{card} C$ and $g$ be the genus of $S$. Then we have the diffeomorphism:
$$V \# \mathbb{C} \mathbb{P}^{2} \cong X_{1} \# X_{2} \# 2 g \mathbb{C P}^{2} \#(2 g+n-1) \overline{\mathbb{C P}^{2}}$$

For the last step of induction, let $\pi_{2}: X \rightarrow \mathbb{C P}^{1} \times \mathbb{C P}^{1}$ be an iterated cyclic cover and let $\pi_{1}: N \rightarrow X$ be the p-cyclic cover branched along $D^{\prime}=\pi_{2}^{-1}(D)$. Then $\mathcal{O}\left(D^{\prime}\right)=\pi_{2}^{*}\left(\mathcal{O}_{\mathbb{C P}^{1} \times \mathbb{C P}^{1}}(p m, p n)\right)$ and let $\mathcal{L}=\pi_{2}^{*}\left(\mathcal{O}_{\mathbb{C P}^{1} \times \mathbb{C P}^{1}}(m, n)\right)$. Assuming the notations from Construction 3.2, there exists a tautological section $z \in \Gamma\left(L, p^{*}(\mathcal{L})\right)$ such that $N \subset L$ is the zero locus of $z^{p}-p^{*}\left(\varphi_{D^{\prime}}\right) \in$ $\Gamma\left(L, p^{*}\left(\mathcal{L}^{\otimes p}\right)\right)$. We can compactify $L$ to $W=\mathbb{P}\left(\mathcal{L} \oplus \mathcal{O}_{X}\right)$ by adding a divisor $W_{\infty}=W \backslash L$. Then $p^{\prime}: W \rightarrow X$ is a $\mathbb{C} \mathbb{P}^{1}$-bundle and we can try to extend the section $z$ to a section in $\Gamma\left(W, p^{\prime *}(\mathcal{L})\right)$. As $p^{\prime *}(\mathcal{L})$ restricts on the fiber to the trivial line bundle and $z$ has a zero at the origin of $L \rightarrow X$ then this section will have a pole of multiplicity one along $W_{\infty}$. To adjust to this problem we consider the section $z^{\prime} \in \Gamma\left(W, p^{\prime *}(\mathcal{L}) \otimes \mathcal{O}\left(W_{\infty}\right)\right), z^{\prime}=z \cdot \varphi_{W_{\infty}}$. Let $\varphi_{W_{\infty}}=\varphi_{\infty}$. Then $z^{\prime}$ has no zero along $W_{\infty}$ and rescales the values of $z$ outside $W_{\infty}$. Hence, our manifold $N$ is the zero locus $\left(z^{\prime p}-p^{\prime *}\left(\varphi_{D}\right) \cdot \varphi_{\infty}^{p}=0\right)$.

Let $D_{1}, D_{2}$ be two smooth curves on $\mathbb{C P}^{1} \times \mathbb{C P}^{1}$, such that $\mathcal{O}\left(D_{1}\right)=$ $\mathcal{O}(m, n), \mathcal{O}\left(D_{2}\right)=\mathcal{O}((p-1) m,(p-1) n)$ and which are transversal to each other and to the branch loci which where considered in the construction of $X$ and such that none of the intersection points of $D_{1}, D_{2}$ lie on the previous branch loci. Then $p^{\prime-1}\left(D_{i}\right)=D_{i}^{\prime}, i=1,2$ are smooth curves on $X$ transversal to each other and $D_{1}^{\prime}+D_{2}^{\prime}$ is linearly equivalent to $D^{\prime}$. Let
$$\begin{gathered}
X_{1}=\left(z^{\prime}-p^{\prime *}\left(\varphi_{D_{1}}\right) \cdot \varphi_{\infty}=0\right) \\
X_{2}=\left(z^{\prime p-1}-p^{\prime *}\left(\varphi_{D_{2}}\right) \cdot \varphi_{\infty}^{p-1}=0\right)
\end{gathered}$$

We remark that $X_{1}$ is a cover of $X$ of degree one, hence it is diffeomorphic to $X$, while $X_{2}$ is a $(p-1)$-cyclic cover of $X$. Then $N, X_{1}, X_{2}$ verify the requirements in the lemma so:
$$N \# \mathbb{C P}^{2} \cong X \# X_{2} \# r \mathbb{C P}^{2} \# s \overline{\mathbb{C P}^{2}}, \text { for suitable } r, s .$$
If $R=\left(\varphi_{D_{1}}^{p-1}-\varphi_{D_{2}}=0\right) \subset \mathbb{C P}^{1} \times \mathbb{C P}^{1}$. Then $X_{1} \bigcap X_{2}=S=\left(\pi_{2} \circ p^{\prime}\right)^{-1}(R)$ is an iterated cover of $R$. After taking the first branch cover we obtain a curve which is the $d$-cover of $R$ branched at $R \cdot C=d a m+d b n$ points, so its Euler characteristic is $d \chi(R)-(d-1) d(a m+b n) \leq 0$. Hence genus of $S$ is strictly greater than zero, i.e. $r \geq 1$.

If $p=2$ then both $X_{1,2}$ are diffeomorphic to $X$ hence almost completely decomposable, which implies $N$ almost completely decomposable by Lemma 3.13. The induction on degree of the cover finishes the proof. \(\square\)
3.3. Free actions of the finite cyclic group. On the remaining part of this section we give a recipe for constructing complex surfaces of general type with fundamental group isomorphic to $\mathbb{Z} / d \mathbb{Z}$. They are quotients of a free $\mathbb{Z} / d \mathbb{Z}$ action on bi-cyclic covers $\pi: N \rightarrow \mathbb{C P}^{1} \times \mathbb{C P}^{1}$ of type $(p, d)$. We construct the action of $\mathbb{Z} / d \mathbb{Z}$ explicitly.

First we consider actions on an arbitrary line bundle $\mathcal{O}(a, b)$. Let $x=\left[x_{0}: x_{1}\right], y=\left[y_{0}: y_{1}\right]$ be homogeneous coordinates on $\mathbb{C P}^{1} \times \mathbb{C P}^{1}$. We want to consider the action of $\mathbb{Z}_{d}=<e^{\frac{2 \pi i}{d}}>$ on $\mathbb{C P}^{1} \times \mathbb{C P}^{1}$ generated by:
$$e^{\frac{2 \pi i}{d}} *\left(\left[x_{0}: x_{1}\right],\left[y_{0}: y_{1}\right]\right)=\left(\left[e^{\frac{2 \pi i}{d}} x_{0}: x_{1}\right],\left[e^{\frac{2 \pi i}{d}} y_{0}: y_{1}\right]\right) .$$
This action has four fixed points:
$$([0: 1],[0: 1]),([0: 1],[1: 0]),([1: 0],[0: 1]),([1: 0],[1: 0]) .$$

Let $U_{0}=\left\{\left[1: x_{1}\right] \mid x_{1} \in \mathbb{C}\right\}$ and $U_{1}=\left\{\left[x_{0}: 1\right] \mid x_{0} \in \mathbb{C}\right\}$ be charts of $\mathbb{C P}^{1}$. Then the charts $U_{0} \times U_{0}, U_{0} \times U_{1}, U_{1} \times U_{0}, U_{1} \times U_{1}$ form an atlas of $\mathbb{C} \mathbb{P}^{1} \times \mathbb{C} \mathbb{P}^{1}$. The line bundle $\mathcal{O}(a, b)$ restricted to each of these charts admits a trivialization. Let $z_{00}, z_{01}, z_{10}, z_{11}$ be the corresponding coordinates on each trivialization.

On the chart $U_{1} \times U_{1} \times \mathbb{C}$, we let the $\mathbb{Z}_{d}=<e^{\frac{2 \pi i}{d}}>$ action be generated by:
$$e^{\frac{2 \pi i}{d}} *\left(\left[x_{0}: x_{1}\right],\left[y_{0}: y_{1}\right], z_{11}\right) \rightarrow\left(\left[e^{\frac{2 \pi i}{d}} x_{0}: x_{1}\right],\left[e^{\frac{2 \pi i}{d}} y_{0}: y_{1}\right], e^{\frac{2 \pi i}{d}} z_{11}\right)$$
Using the change of coordinates, the above action is generated in the other charts by:
$$\begin{aligned}
& \text { on } U_{0} \times U_{1}:\left(x_{1}, y_{0}, z_{01}\right) \rightarrow\left(e^{\frac{2 \pi i(d-1)}{d}} x_{1}, e^{\frac{2 \pi i}{d}} y_{0}, e^{\frac{2 \pi i(1+a)}{d}} z_{01}\right) ; \\
& \text { on } U_{1} \times U_{0}:\left(x_{0}, y_{1}, z_{10}\right) \rightarrow\left(e^{\frac{2 \pi i}{d}} x_{0}, e^{\frac{2 \pi i(d-1)}{d}} y_{1}, e^{\frac{2 \pi i(1+b)}{d}} z_{10}\right) ; \\
& \text { on } U_{0} \times U_{0}:\left(x_{1}, y_{1}, z_{00}\right) \rightarrow\left(e^{\frac{2 \pi i(d-1)}{d}} x_{1}, e^{\frac{2 \pi i(d-1)}{d}} y_{1}, e^{\frac{2 \pi i(1+a+b)}{d}} z_{00}\right) .
\end{aligned}$$

Hence, we have the following lemma:
Lemma 3.14. If each of the integers $a+1, b+1, a+b+1$ is relatively prime to $d$, then the above action of $\mathbb{Z} / d \mathbb{Z}$ on $\mathcal{O}(a, b)$ is semi-free with four fixed points on the 0-section.

We also consider a weighted action of $\mathbb{Z}_{d}$ which is defined on $U_{1} \times U_{1} \times \mathbb{C}$ as follows: $e^{\frac{2 \pi i}{d}} *\left(x_{0}, y_{0}, z_{11}\right) \rightarrow\left(e^{\frac{2 \pi i}{d}} x_{0}, e^{2 \frac{2 \pi i}{d}} y_{0}, e^{\frac{2 \pi i}{d}} z_{11}\right)$. This action extends
on the other coordinate charts as:
$$\begin{aligned}
& \text { on } U_{0} \times U_{1}:\left(x_{1}, y_{0}, z_{01}\right) \rightarrow\left(e^{\frac{2 \pi i(d-1)}{d}} x_{1}, e^{2 \frac{2 \pi i}{d}} y_{0}, e^{\frac{2 \pi i(1+a)}{d}} z_{01}\right) ; \\
& \text { on } U_{1} \times U_{0}:\left(x_{0}, y_{1}, z_{10}\right) \rightarrow\left(e^{\frac{2 \pi i}{d}} x_{0}, e^{\frac{2 \pi i(d-2)}{d}} y_{1}, e^{\frac{2 \pi i(1+2 b)}{d}} z_{10}\right) ; \\
& \text { on } U_{0} \times U_{0}:\left(x_{1}, y_{1}, z_{00}\right) \rightarrow\left(e^{\frac{2 \pi i(d-1)}{d}} x_{1}, e^{\frac{2 \pi i(d-2)}{d}} y_{1}, e^{\frac{2 \pi i(1+a+2 b)}{d}} z_{00}\right) .
\end{aligned}$$

We have a similar lemma:
Lemma 3.15. If each of the integers $a+1,2 b+1, a+2 b+1$ is relatively prime to $d$, then the above action of $\mathbb{Z} / d \mathbb{Z}$ on $\mathcal{O}(a, b)$ is free outside the four points on the 0-section.

Requiring that a smooth flexible divisor $D \subset \mathbb{C P}^{1} \times \mathbb{C P}^{1}$ be invariant under the first $\mathbb{Z} / d \mathbb{Z}$ action is equivalent to $\varphi_{D}=0$ is $\mathbb{Z} / d \mathbb{Z}$ invariant. But we need a stronger condition, we need to consider divisors $D$ such that $\varphi_{D}$ is a $\mathbb{Z} / d \mathbb{Z}$ invariant polynomial. Then $\varphi_{D}$ is a bi-homogeneous polynomial of bi-degrees divisible by $d$. So, there are strictly positive integers $(a, b)$ such that $\mathcal{O}(D)=\mathcal{O}(d a, d b)$ and
$$\varphi_{D}=\sum_{\substack{i=\overline{0, a} \\ j=\overline{0, b}}} a_{i j} X_{0}^{d i} X_{1}^{d(a-i)} Y_{0}^{d j} Y_{1}^{d(b-j)}+\sum_{i=\overline{0, d a}} \sum_{i \leq d j \leq d b+i} b_{i j} X_{0}^{i} X_{1}^{d a-i} Y_{0}^{d j-i} Y_{1}^{d(b-j)+i}$$
for some complex coefficients $a_{i j}, b_{i j}$. The linear system of $\mathbb{Z} / d \mathbb{Z}$-invariant sections of $\mathcal{O}(d a, d b)$ is base point free, hence by Bertini's Theorem the generic section is smooth, and we can choose $D$ such that none of the four points are on $D$. Hence $\mathbb{Z} / d \mathbb{Z}$ acts freely on $D$.

If we consider the weighted action then the class of $\mathbb{Z} / d \mathbb{Z}$-invariant divisors might be larger then the one described above (if d even). But this is not important from our point of interest.

Let $N^{\prime} \rightarrow \mathbb{C P}^{1} \times \mathbb{C P}^{1}$ a $d$-cyclic cover branched along $D$ with $\mathcal{O}(D)=$ $\mathcal{O}(d a, d b)$ and such that $\varphi_{D}$ is $\mathbb{Z} / d \mathbb{Z}$-invariant. Then $N^{\prime}$ is a submanifold in $\mathcal{O}(a, b)$ and the $\mathbb{Z} / d \mathbb{Z}$-action on $\mathcal{O}(a, b)$ restricts to $N^{\prime}$. Moreover, if $D$ does not contain any of the fixed four points and the conditions in the Lemma 3.14 are satisfied, then $\mathbb{Z} / d \mathbb{Z}$ acts freely on $N^{\prime}$.

Unfortunately, for what we need, the above construction is not sufficient, and we need to consider bi-cyclic covers.

Proposition 3.16. Let $C, D$ smooth, flexible, transversal divisors on $\mathbb{C P}^{1} \times$ $\mathbb{C P}^{1}$ such that both $\varphi_{D}$ and $\varphi_{C}$ are invariant under the $\mathbb{Z} / d \mathbb{Z}$ action and $\mathbb{Z} / d \mathbb{Z}$ acts freely on $D$. Let $a, b, m, n$ be positive integers such that $\mathcal{O}(D)=$ $\mathcal{O}(d a, d b), \mathcal{O}(C)=\mathcal{O}(p d m, p d n)$, and $d$ is relatively prime to each of the integers $a+1, b+1, a+b+1$. Then, the bi-cyclic cover $\pi: N \rightarrow \mathbb{C P}^{1} \times \mathbb{C P}^{1}$ of type $(d, p)$ branched along $(D, C)$ admits a free $\mathbb{Z} / d \mathbb{Z}$ action. The quotient $M=N /(\mathbb{Z} / d \mathbb{Z})$ has the following properties:
\begin{itemize}
\item[1.] $M$ is a smooth complex surface, with fundamental group $\pi_{1}(M)=$ $\mathbb{Z} / d \mathbb{Z}$;
\end{itemize}
\begin{itemize}
\item[2.] $K_{M}$ is an ample line bundle if $(d-1) a+d(p-1) m>2$ and $(d-$ 1) $b+d(p-1) n>2$;
\item[3.] $c_{1}^{2}(M)=2 p((d-1) a+d(p-1) m-2)((d-1) b+d(p-1) n-2)$;
\item[4.] $c_{2}(M)=p[4-2(d-1)(a+b-d a b)-2 d(p-1)(m+n-p d m n)+$ $2(d-1) d(p-1)(a n+b m)]$.
\end{itemize}

Proof. First, we need to define the $\mathbb{Z} / d \mathbb{Z}$ action on $N$. The action that we want to consider is the trivial extension of the action on $\mathcal{O}(a, b)$ to an action on $\mathcal{O}(a, b) \oplus \mathcal{O}(d m, d n)$. The conditions from the theorem imply that the action restricts to $N$ as a free holomorphic action. Its quotient is a smooth complex surface, with fundamental group $\pi_{1}(M)=\mathbb{Z} / d \mathbb{Z}$. The numerical invariants of $N$ are described by Lemma 3.10. The invariants of $M$ are related to those of $N$ by the following relations: $c_{2}(M)=\frac{1}{d} c_{2}(N), c_{1}^{2}(M)=$ $\frac{1}{d} c_{1}^{2}(N)$. The computations in 3. and 4. are immediate.

By Lemma 3.10, $K_{N}$ is ample which implies [Har77] that so is $K_{M}$. \(\square\)

The techniques developed in this section allow us to construct a family of manifolds with special topological properties:

Proposition 3.17. Given any integer $d \geq 2$, there are infinitely many complex surfaces of general type, $\left\{Z_{i}\right\}_{i \in \mathbb{N}}$, with ample canonical line bundle, such that their fundamental groups $\pi_{1}\left(Z_{i}\right)=\mathbb{Z} / d \mathbb{Z}$, they have $w_{2}$-type $I$, odd intersection form, and $c_{1}^{2}\left(Z_{i}\right)<5 \chi_{h}\left(Z_{i}\right)$. Moreover, their universal covers are almost completely decomposable manifolds.

Proof. We need to consider two cases, determined by the parity of $d$.
For $d$ odd we have the following construction: Let $M(d ; a, b, m, n)$ the manifold constructed in Proposition 3.16 as a $\mathbb{Z}_{d}$-quotient of a bi-cyclic cover of $\mathbb{C P}^{1} \times \mathbb{C P}^{1}$ of type $(d, 2)$, branched along $(D, C)$ with $\mathcal{O}(D)=\mathcal{O}(d a, d b)$, $\mathcal{O}(C)=(2 d m, 2 d n)$. Let $Z_{i}=M(d ; d, d, i, i)$. As $d+1,2 d+1$ are relatively prime to $d$, the conditions in Proposition 3.16 are satisfied. An easy computation of the numerical invariants of $Z_{i}$ yields:
\begin{itemize}
\item[-] $c_{1}^{2}\left(Z_{i}\right)=4(d(d-1)+d i-2)^{2}$;
\item[-] $\chi_{h}\left(Z_{i}\right)=\frac{1}{3} d^{2}(d-1)(2 d-1)+d(d-1)(d i-1)+d^{2} i^{2}-2 d i+2$.
\end{itemize}
We can compute the signature in terms of these invariants as $\tau\left(Z_{i}\right)=\left(-8 \chi_{h}+c_{1}^{2}\right)\left(Z_{i}\right)$. Rohlin's Theorem states that on a spin manifold we have the following relation: $\tau \equiv 0 \bmod 16$. For $i \operatorname{odd}, c_{1}^{2}\left(Z_{i}\right) \neq 0 \bmod 8$, hence $\tau\left(Z_{i}\right) \neq 0 \bmod 8$. If $d$ odd, then the first homotopy has no 2 -torsion hence $Z_{i}$ non-spin implies odd intersection form ( Gom95 5.7.6). Its universal cover $\widetilde{Z}_{i}$ has signature $\tau\left(\widetilde{Z}_{i}\right)=d \tau\left(Z_{i}\right)$, so for $d, i$ odd numbers $\tau\left(\widetilde{Z}_{i}\right) \neq 0 \bmod 16$. Hence $Z_{i}$ is of $w_{2}$-type (I) and odd intersection form.

As $i$ increases, $\frac{c_{1}^{2}}{\chi_{h}}\left(Z_{i}\right)$ approaches $\frac{4 d^{2} i^{2}}{d^{2} i^{2}}=4$.
In the case $d$ even the above arguments do not work as $\tau\left(Z_{i}\right)=0 \bmod$ 16. We need a different construction. The idea is, though, the same. Let $\pi: N(d ; a, b, m, m) \rightarrow \mathbb{C P}^{1} \times \mathbb{C P}^{1}$ be a bi-cyclic cover of type $(d, 3)$
branched along $(D, C)$ with $\mathcal{O}(D)=(d a, d b), \mathcal{O}(C)=(3 d m, 3 d m)$ and such that $D$ intersects $C$ transversally. To simplify the notation we use $N=N(d ; a, b, m, m)$ whenever we want to prove a general statement about the whole class of manifolds. Lemma 3.10 tells us that the canonical line bundle is $K_{N}=\pi^{*}(\mathcal{O}((d-1) a+2 d m-2,(d-1) b+2 d m-2))$, hence $N$ is a surface of general type, with ample canonical line bundle if $(d-1) a+2 m-2>0$, $(d-1) b+2 m-2>0$. Using Lemma 3.11, we can also conclude that $N$ is simply connected.

We want $N$ to be non-spin. We show that this is true if $d$ even and $b$ odd, by finding a class $[A] \in H_{2}(N, \mathbb{Z})$ such that $[A] \cdot w_{2}(N) \neq 0 \bmod 2$. We construct $N$ in two steps:
$$N \xrightarrow{\pi_{2}} X \xrightarrow{\pi_{1}} \mathbb{C} \mathbb{P}^{1} \times \mathbb{C} \mathbb{P}^{1}$$
where first we consider a 3-cyclic cover of $\mathbb{C P}^{1} \times \mathbb{C P}^{1}$ branched along $C$, and then a $d$-cyclic cover branched along $\pi_{1}^{-1}(D)$, the proper transform of $D$.

We construct a 1-parameter family of deformations of $N$ in the following way. Let $D^{\prime}=A \cup B \subset \mathbb{C P}^{1} \times \mathbb{C P}^{1}$ such that $A=\{p t\} \times \mathbb{C P}^{1}, B$ a smooth curve of bi-degree $(d a-1, d b)$, and such that $A, B, C, D$ intersect transversally at all points. Let $N_{0}$ be the $d$-cover of $X$ branched along $\pi_{1}^{-1}\left(D^{\prime}\right)$. This is singular surface, with $A_{d-1}$-type singularities. To resolve these singularities we introduce strings of exceptional divisors, which we denote by $E_{j}$. We denote the minimal resolution of $N_{0}$ by $N^{\prime}$. Proposition 3.6 tells us that $N^{\prime}$ is a complex surface diffeomorphic to $N$.

We have the following diagram:
$$N^{\prime} \xrightarrow{\pi_{0}} N_{0} \xrightarrow{\pi_{2}^{\prime}} X \xrightarrow{\pi_{1}} \mathbb{C} \mathbb{P}^{1} \times \mathbb{C} \mathbb{P}^{1}$$

Let $A^{\prime \prime} \subset N^{\prime}$ be the proper transform of $A^{\prime}=\left(\pi_{1} \circ \pi_{2}^{\prime}\right)^{-1}(A) \subset N_{0}$. Lemma 3.3 tells us that:
$$\begin{aligned}
\mathcal{O}\left(A^{\prime \prime}\right)= & \frac{1}{d}\left(\pi_{1} \circ \pi_{2}^{\prime} \circ \pi_{0}\right)^{*}(\mathcal{O}(1,0))+\Sigma a_{i} E_{i}, a_{i} \in \mathbb{Q}, a_{i} \leq 0 \\
K_{N^{\prime}}= & \left(\pi_{1} \circ \pi_{2}^{\prime} \circ \pi_{0}\right)^{*}(\mathcal{O}((d-1) a+2 d m-2,(d-1) b+2 d m-2)) \\
K_{N^{\prime}} \cdot A^{\prime \prime}= & c_{1}\left(\left(\pi_{1} \circ \pi_{2}^{\prime} \circ \pi_{0}\right)^{*}(\mathcal{O}((d-1) a+2 d m-2,(d-1) b+2 d m-2))\right) \cup \\
& c_{1}\left(\frac{1}{d}\left(\pi_{1} \circ \pi_{2}^{\prime} \circ \pi_{0}\right)^{*}(\mathcal{O}(1,0))+\Sigma a_{i} E_{i}\right) \\
= & \frac{1}{d} 3 d c_{1}(\mathcal{O}((d-1) a+2 d m-2,(d-1) b+2 d m-2)) \cup c_{1}(\mathcal{O}(1,0)) \\
= & 3((d-1) b+2 d m-2) \\
\equiv & 1 \bmod 2 \text { if } b \text { odd, } d \text { even }
\end{aligned}$$
Hence $N^{\prime}$ is non-spin, and so is $N$.
Let $d=2^{k} d^{\prime}, d^{\prime} \in \mathbb{N}$ odd be the decomposition of $d$.
We want to consider the manifolds:
$$N_{i}=N\left(d ; 2 d^{\prime}, d^{\prime}, i, i\right) \subset \mathcal{O}_{\mathbb{C P}^{1} \times \mathbb{C P}^{1}}\left(2 d^{\prime}, d^{\prime}\right) \oplus \mathcal{O}_{\mathbb{C P}^{1} \times \mathbb{C P}^{1}}(d i, d i) \text { if } d^{\prime} \neq 1,$$
$$\text { and } N_{i}=N(d ; 6,3, i, i) \text { if } d=2^{k} .$$
On these manifolds, we can define a weighted $\mathbb{Z} / d \mathbb{Z}$ action as in Lemma 3.15, where we extend the action trivially on the second factor. For this action to be well-defined we need $\varphi_{D}$ and $\varphi_{C}$ to be invariant under the induced action on $\mathbb{C} \mathbb{P}^{1} \times \mathbb{C} \mathbb{P}^{1}$. Such curves always exist. Moreover, we can choose $D, C$ such that $\mathbb{Z} / d \mathbb{Z}$ acts freely on them. The conditions in the Lemma 3.15 are automatically satisfied by our choice of degrees.

Let $Z_{i}=N_{i} /(\mathbb{Z} / d \mathbb{Z})$. $Z_{i}$ is complex surface of general type, with ample canonical line bundle, finite fundamental group $\pi_{1}\left(Z_{i}\right)=\mathbb{Z} / d \mathbb{Z}$ and of $w_{2}$ type (I). Its numerical invariants can be computed using Lemma 3.10 to be: $c_{1}^{2}\left(Z_{i}\right)=6\left(2(d-1) d^{\prime}+2 i-2\right)\left((d-1) d^{\prime}+2 i-2\right)$,
$c_{2}\left(Z_{i}\right)=3\left[4-2(d-1)\left(3 d^{\prime}-2 d^{\prime 2} d\right)-4\left(2 i-3 i^{2}\right)+3(d-1) d^{\prime} i\right]$,
$\tau\left(Z_{i}\right)=\frac{1}{3}\left(c_{1}^{2}-2 c_{2}\right)\left(Z_{i}\right) \equiv-6(d-1) d^{\prime} i \bmod 4$.
For the special case $d=2^{k}$ the numerical invariants are computed by the same formulas, for $d^{\prime}=3$. From the last relation we see that if $i$ is odd, then $\tau\left(Z_{i}\right) \neq 0 \bmod 8$ hence the intersection form is odd. We take $Z_{i}$ to be the subsequence indexed by odd coefficients. As $i$ increases, $\frac{c_{1}^{2}}{\chi_{h}}\left(Z_{i}\right)=$ $\frac{12 c_{1}^{2}}{c_{1}^{2}+c_{2}}\left(Z_{i}\right)$ approaches $\frac{12 \cdot 6 \cdot 4 i^{2}}{6 \cdot 4 i^{2}+3 \cdot 12 i^{2}}=\frac{24}{5}=4.8$ Hence considering both cases, $d$ odd or even, there is a constant $n_{0}>0$ such that for any $i \geq n_{0}$ we have $c_{1}^{2}\left(Z_{i}\right) \leq 5 \chi_{h}\left(Z_{i}\right)$. We will re-index our sequence starting from $Z_{n_{0}}$. Moreover, the universal covers of $Z_{i}$ are almost completely decomposable as they are bi-cyclic covers of $\mathbb{C P}^{1} \times \mathbb{C P}^{1}$ (Theorem 3.12). \(\square\)

\section*{4. Proofs of Theorems}

We can now prove the main theorems:
Proof of Theorem A. The manifolds $Z_{i}$ are the ones given by Proposition 3.17. They are complex surfaces of general type with ample canonical line bundle. Hence, Aubin-Yau's Theorem on Calabi Conjecture, Yau77, tells us that these manifolds admit Kähler-Einstein metrics. Moreover, they have odd intersection form and $w_{2}$-type (I).

By Theorem 2.5, there exist a constant $n_{1}>0$ such that for any lattice point $(x, y)$ in the first quadrant verifying $x>n_{1}, y \leq 8.5 x$ there exists a infinite family of homeomorphic, non-diffeomorphic simply connected minimal symplectic manifolds $M_{j}^{\prime}$ such that $y=c_{1}^{2}\left(M_{j}^{\prime}\right), x=\chi_{h}\left(M_{j}^{\prime}\right)=\frac{\left(c_{1}^{2}+c_{2}\right)\left(M_{j}^{\prime}\right)}{12}$. Eventually after truncating and relabeling the sequence $Z_{i}$, we can construct $M_{i, j}^{\prime}, i, j \in \mathbb{N}$, a family of simply connected symplectic manifolds satisfying:
\begin{itemize}
\item[(1)] for fixed $i, M_{i, j}^{\prime}$ are homeomorphic, but no two are diffeomorphic;
\item[(2)] $\chi_{h}\left(M_{i, j}^{\prime}\right)=\chi_{h}\left(Z_{i}\right)$ for any $j \in \mathbb{N}$;
\item[(3)] $c_{1}^{2}\left(M_{i, j}^{\prime}\right) \geq 8 \chi_{h}\left(M_{i, j}^{\prime}\right)$;
\item[(4)] $c_{1}^{2}\left(Z_{i}\right) \leq 5 \chi_{h}\left(Z_{i}\right)$.
\end{itemize}
Let $S_{d}$ be the rational homology sphere with fundamental group $\pi_{1}\left(S_{d}\right)=$ $\mathbb{Z} / d \mathbb{Z}$ and universal cover $\#(d-1) S^{2} \times S^{2}$ constructed in [Ue96].

The manifolds $M_{i, j}$ are constructed as:
$$M_{i, j}=M_{i, j}^{\prime} \# S_{d} \# k \overline{\mathbb{C} \mathbb{P}^{2}}, \text { where } k=c_{1}^{2}\left(M_{i, j}^{\prime}\right)-c_{1}^{2}\left(Z_{i}\right) .$$
We remark that by Theorem 1 [KMT95] the manifolds $M_{i, j}^{\prime} \# S_{d}$ are not symplectic, but they have non-trivial Seiberg-Witten invariant.

For fixed $i$ the manifolds $Z_{i}$ and $M_{i, j}$ are all of $w_{2}$-type (I), with odd intersection form, fundamental group $\pi_{1}=\mathbb{Z} / d \mathbb{Z}$ and have the same numerical invariants: Todd-genus and Euler characteristic. Hence by Theorem 2.1, these manifolds are homeomorphic.

In the construction theorem for $M_{i, j}^{\prime}$ the differential structures were distinguished by different Seiberg-Witten basic classes. After taking the connected sum with $\overline{\mathbb{C} \mathbb{P}^{2}}$ 's and $S_{d}$, and using Theorem 1 [KMT95] we see that the Seiberg-Witten basic classes remain different. Hence the manifolds $M_{i, j}$ are not diffeomorphic to one another.

An estimate of the number $k$ of copies of $\overline{\mathbb{C} \mathbb{P}^{2}}$ is given by: $k=c_{1}^{2}\left(M_{i, j}\right)-c_{1}^{2}\left(Z_{i}\right) \geq 8 \chi_{h}\left(Z_{i}\right)-5 \chi_{h}\left(Z_{i}\right)=3 \chi_{h}\left(Z_{i}\right)=3 \chi_{h}\left(M_{i, j}\right)$ We also know that the manifolds are under the Bogomolov-Miyaoka-Yau line, which implies: $\chi_{h}\left(M_{i, j}\right) \geq \frac{1}{9} c_{1}^{2}\left(M_{i, j}\right)$.
Hence $k \geq \frac{1}{3} c_{1}^{2}\left(M_{i, j}\right)=\frac{1}{3}(2 \chi+3 \tau)\left(M_{i, j}\right)$. Then Theorem 1.1 implies that $M_{i, j}$ does not admit any Einstein metric. As a consequence we also get that $Z_{i}$ and $M_{i, j}$ are not diffeomorphic.

For the results from the second part of the theorem we have to look at the universal covers $\widetilde{Z}_{i}$, and $\widetilde{M_{i, j}}$ respectively. From our construction, the universal cover of $Z_{i}$ is a simply connected minimal complex surface of general type. It can not be diffeomorphic to the connected sum of $\mathbb{C P}^{2}$ 's and $\overline{\mathbb{C P}^{2}}$ 's as it has non-trivial Seiberg-Witten invariants, but Theorem 3.12 tells us that after connected sum with one copy of $\mathbb{C P}^{2}$ it decomposes completely. The universal cover of $S_{d}$ is diffeomorphic to $(d-1)\left(S^{2} \times S^{2}\right)$, hence the manifold $\widetilde{M_{i, j}} \cong d M_{i, j}^{\prime} \# d k \overline{\mathbb{C P}^{2}} \#(d-1)\left(S^{2} \times S^{2}\right)$. But $\left(S^{2} \times S^{2}\right) \# \overline{\mathbb{C P}^{2}}$ is the complex surface $\mathbb{C P}^{1} \times \mathbb{C P}^{1}$ blown-up at one point, which can also be presented as $\mathbb{C P}^{2} \# 2 \overline{\mathbb{C} \mathbb{P}^{2}}$. So:
$$\widetilde{M_{i, j}} \cong d M_{i, j}^{\prime} \# d k \overline{\mathbb{C} \mathbb{P}^{2}} \#(d-1) S^{2} \times S^{2} \cong d M_{i, j}^{\prime} \#(d-1) \mathbb{C} \mathbb{P}^{2} \#(d k+d-1) \overline{\mathbb{C} \mathbb{P}^{2}}$$
The manifolds $M_{i, j}^{\prime}$ are almost completely decomposable, hence $\widetilde{M_{i, j}}$ is diffeomorphic to the connected sums of a number of $\mathbb{C P}^{2}$ 's and $\overline{\mathbb{C} \mathbb{P}^{2}}$ 's. \(\square\)

Proof of Proposition 1.2. Let $N$ be the double cover of $\mathbb{C P}^{2}$ branched along a smooth divisor $D$, such that $\mathcal{O}(D)=\mathcal{O}_{\mathbb{C P}^{2}}(8)$. Then $N$ is a simply connected, almost completely decomposable surface of general type and by Lemma 3.4 its numerical invariants are:
$$c_{2}(N)=46, c_{1}^{2}(N)=2, \tau(N)=-30 .$$
Hence $b_{2}^{+}=7$ and $b_{2}^{-}=37$. By Theorem 1.1 the manifold $M=N \# \overline{\mathbb{C P}^{2}} \# S_{2}$ does not admit any Einstein metric. Let $\widetilde{M}$ be the universal cover of $M$.

Then we have the following diffeomorphisms:
$$\widetilde{M} \cong 2 N \# 2 \overline{\mathbb{C} \mathbb{P}^{2}} \#\left(S^{2} \times S^{2}\right) \cong 2 N \# \mathbb{C} \mathbb{P}^{2} \# 3 \overline{\mathbb{C} \mathbb{P}^{2}} \cong 15 \mathbb{C} \mathbb{P}^{2} \# 77 \overline{\mathbb{C} \mathbb{P}^{2}} .$$
As $M$ does not admit any Einstein metrics this implies that $\widetilde{M}$ does not admit any Einstein metrics invariant under the covering involution $\sigma$.

Let now $M^{\prime}=N \# \overline{\mathbb{C P}^{2}} \# S_{3}$, where the manifold $N$ is the same as above and $S_{3}$ is a rational sphere. Then the universal cover $\widetilde{M^{\prime}}$ is diffeomorphic to
$$\widetilde{M^{\prime}} \cong 3 N \# 3 \overline{\mathbb{C P}^{2}} \# 2\left(S^{2} \times S^{2}\right) \cong 3 N \# 2 \mathbb{C} \mathbb{P}^{2} \# 5 \overline{\mathbb{C} \mathbb{P}^{2}} \cong 23 \mathbb{C} \mathbb{P}^{2} \# 116 \overline{\mathbb{C P} \mathbb{P}^{2}} .$$ \(\square\)

We can combine the idea of the above propositions with the geography of almost completely decomposable symplectic manifolds 2.5 to prove a general result:

Proof of Theorem B. We only need to prove that the statement holds for manifolds in the first region defined in condition 2. as the second region is obtained from the first region by a change of orientation.

Let $\epsilon>0$ be a small positive number. Theorem 2.5 tells us that for any $\epsilon^{\prime}>0$ there exists an $c\left(\epsilon^{\prime}\right)$ such that to any integer point $(x, y)$ in the latice:
$$0<y \leq\left(9-\epsilon^{\prime}\right) x-c\left(\epsilon^{\prime}\right)$$
we can associate infinitely many homeomorphic, non-diffeomorphic almost completely decomposable minimal symplectic manifolds which have topological invariants $\left(\chi_{h}, c_{1}^{2}\right)=(x, y)$. Let $\epsilon^{\prime}=\frac{3}{2} \epsilon$ then there exists an $c\left(\epsilon^{\prime}\right)$ with the above properties. Let $N(\epsilon)=\frac{2 d}{3}\left(c\left(\epsilon^{\prime}\right)+1\right)$.

Let $n, m$ integer points such that the conditions 1. and 2. in Theorem B. are satisfied. Condition 2. states the following:
$$n<(6-\epsilon) m-N(\epsilon)$$
Or equivalently:
$$\begin{aligned}
\frac{n}{d} & <(6-\epsilon) \frac{m}{d}-\frac{N(\epsilon)}{d} \\
\frac{3 n}{2 d} & <\left(9-\frac{3}{2} \epsilon\right) \frac{m}{d}-\frac{3 N(\epsilon)}{2 d} \\
\frac{3 n}{2 d} & <\left(9-\epsilon^{\prime}\right) \frac{m}{d}-c\left(\epsilon^{\prime}\right)-1 \\
\frac{3 n}{2 d}+1 & <\left(9-\epsilon^{\prime}\right) \frac{m}{d}-c\left(\epsilon^{\prime}\right)
\end{aligned}$$

Then $\left[\frac{3 n}{2 d}\right]+1$ and $\frac{m}{d}$ satisfy the conditions of Theorem 2.5, hence there are infinitely many symplectic manifolds $M_{i}$ such that $c_{1}^{2}\left(M_{i}\right)=\left[\frac{3 n}{2 d}\right]+$ 1 and $\frac{\chi+\tau}{4}\left(M_{i}\right)=\frac{m}{d}$. Moreover $M_{i}$ are homeomorphic non-diffeomorphic almost completely decomposable manifolds. The differential structures are distinguished by the difference in the Seiberg-Witten monopole classes.

Let:
$$X_{i}=M_{i} \# S_{d} \# k \overline{\mathbb{C P}^{2}}, k=\left[\frac{3 n}{2 d}\right]+1-\frac{n}{d}>\frac{1}{3} c_{1}^{2}\left(M_{i}\right)$$
Then $\frac{\chi+\tau}{4}\left(X_{i}\right)=\frac{m}{d}$ and $(2 \chi+3 \tau)\left(X_{i}\right)=\frac{n}{d}$. The manifolds $X_{i}$ remain homeomorphic to each other and using the formula for the Seiberg-Witten monopole classes for the connected sum we can immediately see that any two manifolds are not diffeomorphic. Their universal cover $\widetilde{X_{i}}$ is diffeomorphic to $d X_{i} \# d k \overline{\mathbb{C P}^{2}} \#(d-1)\left(S^{2} \times S^{2}\right)$ and as $X_{i}$ are almost completely decomposable, this implies that all $\widetilde{X_{i}}$ are diffeomorphic to $X=a \mathbb{C P}^{2} \# b \overline{\mathbb{C P}^{2}}$ for suitable $a, b$ such that $\frac{\chi+\tau}{4}(X)=m,(2 \chi+3 \tau)(X)=n$.

As $M_{i} \# S_{d}$ has non-trivial Seiberg-Witten invariants, we use Theorem 1.1 to conclude that the manifolds $X_{i}$ do not admit an Einstein metric. Hence their universal cover $X$ does not admit any Einstein metric invariant under any of the $\mathbb{Z} / d \mathbb{Z}$-actions. \(\square\)

Proof of Theorem C. The proof is again based on the obstruction given by Theorem 1.1. To construct the examples we employ Gompf's techniques, [Gom95], and use symplectic connected sum along symplectic submanifolds of self-intersection 0. We use some standard blocks of symplectic manifolds.

The first block, $X_{G}$, was constructed by Gompf in [Gom95, Theorem 6.2]. It has fundamental group $G, c_{1}^{2}\left(X_{G}\right)=0$ and contains a symplectic 2-torus of self-intersection 0.

The second block, denoted by $E(n)$, is the family of simply connected proper elliptic complex surfaces with no multiple fibers and Euler characteristic $\chi(E(n))=12 n$. A generic fiber is a symplectic torus of self-intersection 0 and it can easily be checked,[GoSt99], that its complement is simply connected.

The third block is the one used by Gompf [Gom95] in the proof of Theorem 6.1. Let $F_{1}, F_{2}$ be two Riemann surfaces of genera $k+1(k \geq 1)$ and 2 , respectively. Let $C_{i}, i=1, \ldots, 2 k+2$ be homologically nontrivial embedded circles in $F_{1}$ generating $H_{1}\left(F_{1}, \mathbb{Z}\right)$ and the circles $C_{i}^{\prime} \subset F_{2}, i=1, \ldots, 4$ be the generators of $H_{1}\left(F_{2}, \mathbb{Z}\right)$, such that $C_{2 i} \cap C_{2 j}=C_{2 i-1} \cap C_{2 j-1}=\emptyset$ if $i \neq j$ and $C_{2 i} \cdot C_{2 j-1}=\delta_{i}^{j}, i, j=\overline{1, k+1} . C_{i}^{\prime}$ are also satisfying the above conditions. Let $T_{i}$ be the collection of tori given by $C_{1} \times C_{1}^{\prime}, C_{2} \times C_{3}^{\prime}, C_{3} \times$ $C_{2}^{\prime}, C_{4} \times C_{4}^{\prime}, C_{i} \times C_{1}^{\prime}, i=5, \ldots, 2 k+2$. We can perturb this collection to a new collection of disjoint tori $\left\{T_{i}^{\prime}\right\}$, where $T_{i}^{\prime}$ is homologous to $T_{i}$. As $T_{i} \subset$ $F_{1} \times F_{2}$ is a Lagrangian torus we may choose $T_{i}^{\prime} \subset F_{1} \times F_{2}$ to be Lagrangian, too. Moreover these tori are also homologically non-trivial, hence we can perturb the product symplectic form on $F_{1} \times F_{2}$, see [Gom95], such that these tori become symplectic submanifolds. Let $X_{k}$ be the manifold obtained by performing symplectic connected sum of $F_{1} \times F_{2}$ and $2 k+2$ copies of $E(2)$ along the family $\left\{T_{i}^{\prime}\right\}_{i=\overline{1,2 k+2}}$ and generic fibers of $E(2)$. Then the manifold $X_{k}$ is a spin, symplectic 4-manifold, and by Seifert-Van Kampen Theorem it is also simply connected. The numerical invariants of $X_{k}$ are $\chi\left(X_{k}\right)=52 k+48, \tau\left(X_{k}\right)=-32(k+1)$.

The fourth block has a linking role, and it is $E(4)$ with a special symplectic structure. This manifold has an important feature [Gom95, proof of Theorem 6.2]: it contains a symplectic 2-torus and a disjoint symplectic surface of genus 2 . We denote them by $T$ and $F$, respectively. Both $T$ and $F$ have self-intersection zero and their complement $E(4) \backslash\{F \cup T\}$ is simply connected.

Let:
$$M_{i}=X_{G} \#_{T^{2}} E(4) \#_{\Sigma_{2}} X_{i} \#_{\Sigma_{2}} E(4) \#_{T^{2}} E(2) \# p \overline{\mathbb{C} \mathbb{P}^{2}},$$
where $\#_{T^{2}}$ 's are the symplectic sums along tori of self-intersection zero and $\#_{\Sigma_{2}}$ 's are fiber sums along Riemann surfaces of genus 2, represented by $F \subset E(4)$ and one generic $\{p t\} \times F_{2} \subset X_{i}$. The last operation is simply a connected sum and $p$ is a constant satisfying:
$$\left(c_{1}^{2}\left(X_{i}\right)+16\right)>p>\frac{1}{3}\left(c_{1}^{2}\left(X_{i}\right)+16\right)>0 .$$
The fundamental group of $M_{i}$ can be easily computed by Seifert-Van Kampen Theorem to be $G$. To obtain different differential structures on $M_{i}$, we take logarithmic transformations of different multiplicities along a generic fiber of $E(2)$. Then by the gluing formula for the Seiberg-Witten invariants [Par02] (Cor 15,20) the manifolds have different Seiberg-Witten invariants. Hence we have constructed infinitely many non-diffeomorphic manifolds. We denote them by $M_{i, j}$. For fixed $i$, these manifolds are all homeomorphic. To show this, we can first do the logarithmic transformations on $E(2)$, this yields homeomorphic manifolds. By taking the fiber sum along a generic fiber with the remaining terms we obtain homeomorphic manifolds. Theorem 1.1 implies that no $M_{i, j}$ admits an Einstein metric. \(\square\)

All the manifolds constructed up to now are non-spin. If we want to analyze the spin case then we need to use a new obstruction obtained by LeBrun and Ishida [IsLe02]. This uses a refinement of the Seiberg-Witten invariant defined independently by Bauer and Furuta.

Theorem 4.1. [IsLe02] Let $X_{j}, j=1, \ldots, 4$ be smooth, compact almostcomplex 4-manifolds for which the mod-2 Seiberg-Witten invariant is nonzero, and suppose that
$$\begin{aligned}
b_{1}\left(X_{j}\right) & =0 \\
b_{2}^{+}\left(X_{j}\right) & \equiv 3 \bmod 4, \\
\sum_{j=1}^{4} b_{2}^{+}\left(X_{j}\right) & \equiv 4 \bmod 8 .
\end{aligned}$$
Let $N$ be any oriented 4 -manifold with $b_{2}^{+}=0$. Then, for any $m=2,3$ or 4, the smooth 4-manifold $M=\#_{j=1}^{m} X_{j} \# N$ does not admit Einstein metrics if
$$4 m-(2 \chi+3 \tau)(N) \geq \frac{1}{3} \sum_{j=1}^{m} c_{1}^{2}\left(X_{j}\right) .$$

Proof of Theorem D. The manifolds $M_{i}$ are constructed as connected sums and fiber sums of different blocks.

For the first block we start with $X_{G}$, the spin symplectic 4-manifolds constructed by Gompf. Taking the symplectic connected sum with the elliptic surface $E(2 n)$ along arbitrary fibers $\left(\{p t\} \times T^{2} \cong F_{0} \subset E(2 n)\right)$ we obtain a new symplectic, spin manifold which we denote by $N_{G}(n)$. The elliptic surface $E(2 n)$ that we consider has no multiple fibers and its numerical invariants are $c_{2}(E(2 n))=24 n, \tau(E(2 n))=-16 n, c_{1}^{2}(E(2 n))=0$. Moreover the complement of the generic fiber $F_{0}$ is simply connected. Hence the manifold $N_{G}(n)$ satisfies the following: $\pi_{1}\left(N_{G}(n)\right)=G, c_{1}^{2}\left(N_{G}(n)\right)=0, c_{2}\left(N_{G}(n)\right)=$ $24 k+24 n$. Since $G$ is finite, $b_{1}\left(N_{G}(n)\right)=0$, and $b_{2}^{+}\left(N_{G}(n)\right)=4(k+n)-1 \equiv 3$ $\bmod 4$.