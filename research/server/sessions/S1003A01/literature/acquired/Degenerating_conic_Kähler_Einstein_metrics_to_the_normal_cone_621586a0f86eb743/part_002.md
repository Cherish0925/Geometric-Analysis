---
retention_scope: session
part: 2
total_parts: 3
---

[Part 2/3 of: Degenerating conic Kähler–Einstein metrics to the normal cone]

\section*{4. Automorphisms and related objects}
4.1. Relations between Aut ${ }^{\circ}(X, D)$ and Aut ${ }^{\circ}(D)$. Let $Y:=\mathbb{P}\left(L \oplus \mathcal{O}_{D}\right)$, let $p:$ $Y \rightarrow \bar{L}$ be the contraction of the divisor at infinity $D_{\infty}:=\mathbb{P}(L \oplus 0) \subset Y$ and let $x_{\infty}=p\left(D_{\infty}\right) \in \bar{L}$, cf section 2 for the definition of $\bar{L}$. The zero section $D:=$ $\mathbb{P}(L \oplus 1)$ can be equivalently seen inside $\bar{L}$ or $Y$. We have a natural sequence
$$1 \longrightarrow \mathbb{C}^{*} \longrightarrow \operatorname{Aut}^{\circ}(\bar{L}, D) \longrightarrow \operatorname{Aut}^{\circ}(D) \longrightarrow 1$$
where the action of $\mathbb{C}^{*}$ is given on $Y$ by $\lambda \cdot[v: z]:=[\lambda v: z]$; it obviously preserves $D=(v=0)$ and $D_{\infty}=(z=0)$ hence descends to an action of $\mathbb{C}^{*}$ on $\bar{L}$ preserving $D$. The second arrow is simply the restriction to $D$.
Lemma 4.1. The short sequence (4.1) is exact.
Proof. The rightmost arrow is exact since any automorphism of $D$ induces a linear automorphism of $L=(\alpha-1) K_{D}^{-1}$. It remains to see that we have exactness in the middle. So let $f \in \operatorname{Aut}^{\circ}(\bar{L}, D)$ acting trivially on $D$; we need to show that $f$ comes from the $\mathbb{C}^{*}$ action. First, $f$ obviously preserves the singular locus $\bar{L}^{\text {sing }}=\left\{x_{\infty}\right\}$. Since $p$ is simply the blow up of $x_{\infty} \in \bar{L}, f$ lifts to an automorphism $\widetilde{f} \in$ Aut ${ }^{\circ}(Y)$ acting trivially on $D$. A classical argument due to Blanchard [Bla56] shows that any element in the identity component of the automorphism group of a fiber bundle with compact fibers fixing the base has to preserve the fiber bundle structure. In our case it means that $\widetilde{f}$ preserves the $\mathbb{P}^{1}$ fibers of the projection $\rho: Y \rightarrow D$. Given $x \in D, \widetilde{f}$ acts on the fiber $\rho^{-1}(x) \simeq \mathbb{P}^{1}$ preserving 0 (i.e. $D \cap \rho^{-1}(x)$ ) and $\infty$ (i.e. $D_{\infty} \cap \rho^{-1}(x)$ ), hence it can be written as an homothety $[u: v] \mapsto[a(x) u, v]$. The function $a$ defines a holomorphic map $D \rightarrow \mathbb{C}^{*}$ hence it is constant. The lemma follows. \(\square\)

Lemma 4.2. Assume $(X, D) \neq\left(\mathbb{P}^{n}, H\right)$ for $H$ an hyperplane and consider the morphism $\rho_{D}$ induced by restriction to $D$
$$\rho_{D}: \operatorname{Aut}^{\circ}(X, D) \longrightarrow \operatorname{Aut}^{\circ}(D) .$$

The following hold.
\begin{itemize}
\item[(i)] $\rho_{D}$ has finite kernel.
\item[(ii)] If $X$ is toric, then $\rho_{D}$ is a surjective, finite étale cover.
\end{itemize}

Proof. Since the groups at stake are algebraic, the lemma can be rephrased by saying that
$$H^{0}\left(X, T_{X}(-\log D)\right) \rightarrow H^{0}\left(D, T_{D}\right)$$
is injective (first item) and surjective when $X$ is toric (second item). We have the following exact sequence
$$0 \longrightarrow T_{X}(-D) \longrightarrow T_{X}(-\log D) \longrightarrow T_{D} \longrightarrow 0 .$$
By a result of J. Wahl [Wah83], we have $H^{0}\left(X, T_{X} \otimes \mathcal{O}_{X}(-D)\right)=0$ since $(X, D) \neq$ $\left(\mathbb{P}^{n}, H\right)$, so this shows (i).

Using (4.3) again, (ii) reduces to showing that $H^{1}\left(X, T_{X}(-D)\right)=0$. Since $T_{X} \simeq \Omega_{X}^{n-1} \otimes K_{X}^{-1}$, we have to show that
$$H^{1}\left(X, \Omega_{X}^{n-1} \otimes L\right)=0,$$
where $L=-K_{X}-D \simeq(\alpha-1) D$ is an ample line bundle. But this follows precisely from Bott's vanishing theorem for toric varieties, cf [Oda88, § 3.3]. □

If $D$ is allowed to be singular, then $\rho_{D}$ need not be isomorphic as shown by the following example, which was communicated to us by Thibaut Delcroix.

Example 4.3. Let $X=Q_{4}=\left\{\sum_{i=0}^{5} z_{i}^{2}=0\right\} \subset \mathbb{P}^{5}$ be the four-dimensional smooth quadric and let $D=\left\{z_{0}^{2}+z_{1}^{2}+z_{2}^{2}=0=z_{3}^{2}+z_{4}^{2}+z_{5}^{2}\right\} \subset X$. Then $D$ is irreducible and reduced, with an action of $\mathrm{SO}_{3}(\mathbb{C}) \times \mathrm{SO}_{3}(\mathbb{C})$ with dense orbit, and satisfies $-K_{X} \sim_{\mathbb{Z}} 2 D$. But the one-parameter family of automorphisms
$$t \cdot\left[z_{0}: \ldots: z_{5}\right]=\left[t z_{0}: t z_{1}: t z_{2}: t^{-1} z_{3}: t^{-1} z_{4}: t^{-1} z_{5}\right]$$
does not extend to $\mathrm{PSO}_{6}(\mathbb{C})$. Moreover, one can check that $D$ admits a Kähler-Einstein metric combining [Del20] and [Li22].
4.2. About the normal bundle. In this section, we investigate whether the formal neighborhood of $D$ in $X$ of order one (that is, the ringed space $\left(D, \mathcal{O}_{X} / \mathcal{I}_{D}^{2}\right)$ coincides with the formal neighborhood of $D$ in $L$ (that is, the ringed space $\left.\left(D, \mathcal{O}_{L} / \mathcal{I}_{D}^{2}\right)\right)$. From [ABT09, Proposition 1.5], this is equivalent to the normal short exact sequence
$$\left.0 \longrightarrow T_{D} \longrightarrow T_{X}\right|_{D} \longrightarrow N_{D} \longrightarrow 0$$
being split. A sufficient condition for the splitting of (4.4) to happen is to have the vanishing $H^{1}\left(D, T_{D} \otimes N_{D}^{-1}\right)=0$ as we see by tensorizing the above sequence with $N_{D}^{-1}$ and observing that extensions of $\mathcal{O}_{D}$ by $T_{D} \otimes N_{D}^{-1}$ are parametrized by the image of $1 \in H^{0}\left(D, \mathcal{O}_{D}\right)$ in $H^{1}\left(D, T_{D} \otimes N_{D}^{-1}\right)$ under the connecting homomorphism in the long exact sequence in cohomology associated to (4.4). We give a couple of situations where (4.4) is split or non-split.

Example 4.4. If $X=\mathbb{P}^{n}$, then a theorem of Van de Ven [VdV59] shows that (4.4) is split if and only if $D$ is a linear subspace of $\mathbb{P}^{n}$. Alternatively, if (4.4) is split, then $T_{D}$ is a quotient of the ample bundle $\left.T_{\mathbb{P}^{n}}\right|_{D}$ hence it is ample, too. By Mori theorem [Mor79] (or Siu-Yau's proof of Frankel's conjecture [SY80]), $D \simeq \mathbb{P}^{n}$

Example 4.5. If $X$ is toric and $\alpha>2$, then (4.4) is split if and only if $(X, D)=$ $\left(\mathbb{P}^{n}, H\right)$ where $H$ is an hyperplane. Indeed, we have
$$H^{1}\left(X, T_{X}(-2 D)\right) \simeq H^{1}\left(X, \Omega_{X}^{n-1} \otimes K_{X}^{-1}(-2 D)\right)=H^{1}\left(X, \Omega_{X}^{n-1} \otimes \mathcal{O}_{X}((\alpha-2) D)\right)=0$$
by Bott vanishing theorem. In particular, the exact sequence
$$\left.0 \longrightarrow T_{X}(-2 D) \longrightarrow T_{X}(-D) \longrightarrow T_{X}\right|_{D} \otimes N_{D}^{-1} \longrightarrow 0$$
shows that any section of $\left.T_{X}\right|_{D} \otimes N_{D}^{-1}$ extends to a section of $T_{X}(-D)$. Now, if (4.4) splits, we precisely get a non-zero section $H^{0}\left(D,\left.T_{X}\right|_{D} \otimes N_{D}^{-1}\right)$, hence we obtain a non-zero section $H^{0}\left(X, T_{X}(-D)\right)$. By [Wah83], this implies that $(X, D)$ is isomorphic to $\left(\mathbb{P}^{n}, H\right)$ as announced.

Example 4.6. If $D$ is toric and $\alpha>2$, then (4.4) is always split. Indeed, we have $H^{1}\left(D, T_{D} \otimes N_{D}^{-1}\right) \simeq H^{1}\left(D, \Omega_{D}^{n-2} \otimes \mathcal{O}_{D}((\alpha-2) D)\right)=0$ by Bott vanishing theorem.

Example 4.7. If $X=Q_{n} \subset \mathbb{P}^{n+1}$ is the $n$-dimensional quadric and $D=Q_{n-1}=$ $Q_{n} \cap H$ for an hyperplane $H$, then we have $K_{X}^{-1}=\mathcal{O}_{X}(n) \sim n D$, i.e. $\alpha=n$, and $D$ is Kähler-Einstein. Moreover, for any $m \geqslant 1$, we have the vanishing $H^{1}\left(Q_{m}, T_{Q_{m}}(-1)\right) \simeq H^{1}\left(Q_{m}, \Omega_{Q_{m}}^{m-1}(m-1)\right)=0$ by [Sno86, p. 174]. Apply this to $m=n-1$ to get that (4.4) is split. Conversely, if $D \subset Q_{n}$ is an hypersurface such that (4.4) splits, then $D \simeq Q_{n-1}$ by [Jah05, Theorem 4.7].

\section*{5. The tubular neighbourhood of $D$}

Since $-K_{X} \sim \alpha D$, the normal bundle $L=N_{D}$ of $D$ in $X$ has a canonical volume form, which in local coordinates $\left(z^{0}, \ldots, z^{n-1}\right)$ such that $D=\left\{z^{0}=0\right\}$
can be written as
$$\Omega_{L}=v\left(z^{1}, \ldots, z^{n-1}\right) \frac{d z^{0}}{\left(z^{0}\right)^{\alpha}} \wedge d z^{1} \wedge \cdots \wedge d z^{n-1} .$$
This is not completely correct, since $\left(z^{0}\right)^{\alpha}$ a priori does not make sense: if we write $\alpha=\frac{p}{q}$ then we only have a section $\Omega^{q}$ of $K_{X}^{q}(p D)$ on $X$. But since at the end we need only to consider the real volume form $\Omega \wedge \bar{\Omega}$ which is well defined as $\left(\Omega^{q} \wedge \overline{\Omega^{q}}\right)^{\frac{1}{q}}$, we will simplify the notation and formulas by writing $\Omega$ (and $\Omega_{L}$ on $L$ ).
5.1. The complex structure. Let $\Delta_{L} \subset L$ be the disc normal bundle of $D$. The connection 1-form $\eta$ on $L \backslash D$ gives a horizontal space $H \subset T \Delta_{L}$ which is transverse to each disc. If we have another complex structure $J$ on $\Delta_{L}$, we compare it to the complex structure $J_{L}$ of $L$ by a tensor $\phi \in \Omega_{J_{L}}^{0,1} \otimes T_{J_{L}}^{1,0}$ so that
$$T_{J}^{0,1}=\left\{X+\phi_{X}, X \in T_{J_{L}}^{0,1}\right\} .$$
The integrability of $J$ gives the equation $\bar{\partial} \phi+\frac{1}{2}[\phi, \phi]=0$, where the bracket is constructed from the exterior product of forms and from the bracket of vector fields.

We will use the following canonical parametrization of a small tubular neighbourhood of $D$ by $\Delta_{L}$, see [Biq02, Theorem 4.1]:

Proposition 5.1. There exists a small neighbourhood $U_{L}$ of $D$ in $X$ and a diffeomorphism $\mathrm{Y}: \Delta_{L} \rightarrow U_{L}$ such that $\phi=\mathrm{Y}^{*} J_{X}-J_{L} \in \Omega^{0,1}\left(T^{1,0}\right)$ is a section of $H_{0,1} \otimes H^{1,0}$ (that is, $\phi$ is purely horizontal) which satisfies $\phi\lrcorner d \eta=0,\left.\phi\right|_{D}=0$ and is holomorphic along the discs of $\Delta_{L}$.

Moreover $\mathrm{Y}^{*} \Omega=v(1-\phi)^{*} \Omega_{L}$ where $v$ is a function on $\Delta_{L}$ which is holomorphic along the discs and satisfies $\left.v\right|_{D}=1$. \(\square\)
5.2. The complex volume form. The meaning of Proposition 5.1 is that any neighbourhood of $D$ which is close enough to a disc bundle $\Delta_{L}$ carries a unique fibration by holomorphic discs satisfying the conclusions of the proposition. But there is no particular choice of $U_{L}$. Therefore we get an additional freedom by perturbing $U_{L}$. Using this flexibility, one should be able to obtain $v \equiv 1$. As we need only finite developments, it will be sufficient to prove the following Proposition. We denote $\zeta$ the variable in the total space of $L$.

We decompose $T_{\mathbb{C}} L=\mathbb{C} \zeta \partial_{\zeta} \oplus T_{\mathbb{C}} D$. In the following proposition we will measure the norm of an endomorphism of $T L$ with respect to this decomposition (that is we consider $\bar{\zeta} \partial_{\zeta}$ as having norm 1).

Proposition 5.2. There are purely horizontal tensors $\phi_{i} \in \Omega_{D}^{0,1}\left(T^{1,0} D \otimes L^{-i}\right)$ for $i>0$ such that $\left.\phi_{i}\right\lrcorner d \eta=0$ and the following is true.

Given any $j>0$, one can choose a diffeomorphism $\mathrm{Y}: \Delta_{L} \rightarrow U_{L}$ such that:
\begin{itemize}
\item[(1)] $\phi=\mathrm{Y}^{*} J_{X}-J_{L}$ satisfies $\phi=\sum_{1}^{j-1} \zeta^{i} \phi_{i}+O\left(\zeta^{j}\right)$;
\item[(2)] $\mathrm{Y}^{*} \Omega=v(1-\phi)^{*} \Omega_{L}$ with $v=1+O\left(\zeta^{j}\right)$.
\end{itemize}
where $O()$ is meant with derivatives.
Note that this statement is weaker than Proposition 5.1 for the complex structure $\phi$ but gives more information on $v$. It is likely that one can obtain both the gauge of Proposition 5.1 and $v \equiv 1$, but this problem may involve a loss of derivatives which makes it difficult, so we will prove only Proposition 5.2.

The rest of this subsection is devoted to the proof of the Proposition. So we are on the disc bundle $\Delta_{L}$, with a complex structure $J$ whose difference with $J_{L}$ is given by the tensor $\phi$ as described in Proposition 5.1.

We consider the infinitesimal action of the real part of the $(1,0)$ vector field (for $J_{L}$ )
$$\xi=f i \zeta \partial_{\zeta}+X$$
where $X \in H^{1,0}$ is horizontal, and $i \zeta \partial_{\zeta}=R^{1,0}$ is the $(1,0)$ part of the Reeb vector field $R=\frac{d}{d \theta}$. The infinitesimal action on the complex structure $J_{L}$ is
$$\left.\bar{\partial} \xi=2 \eta^{0,1} \otimes\left(\bar{\zeta} \partial_{\bar{\zeta}} f \zeta \partial_{\zeta}+\bar{\zeta} \partial_{\bar{\zeta}} X\right)+\left(\bar{\partial}_{H} f+X\right\lrcorner d \eta\right) \otimes i \zeta \partial_{\zeta}+\bar{\partial}_{H} X .$$

Observe that if $X=-\sharp \bar{\partial}_{H} f$ and $f$ is holomorphic along the fibers ( $\partial_{\bar{\zeta}} f=$ 0 ), then $\bar{\partial} \xi=-\bar{\partial}_{H} \sharp \bar{\partial}_{H} f$ is purely horizontal, that is the vector field
$$\xi_{f}=f i \zeta \partial_{\zeta}-\sharp \bar{\partial}_{H} f$$
preserves infinitesimally the gauge of $\phi$ (of Proposition 5.1) if $f$ is holomorphic along the fibers. This is the flexibility alluded to on $U_{L}$ since $f$ is determined by its value on the boundary of $U_{L}$ and corresponds to perturbing this boundary. (This is actually the complexification of the action of the contactomorphisms of $\partial \Delta_{L}$ which was studied in [Biq19, § 7]).

Let us now investigate the action of such deformations on the function $v$. The model holomorphic volume form (5.1) can be written as
$$\Omega_{L}=\eta^{1,0} \wedge \Omega_{D}, \quad \Omega_{D} \in H^{0}\left(K_{D} L^{\alpha-1}\right) .$$

Recall that $-K_{D}=(\alpha-1) L$ so the section $\Omega_{D}$ is canonical up to a multiplicative constant, that we can choose so that it satisfies
$$i^{(n-1)^{2}} \Omega_{D} \wedge \overline{\Omega_{D}}=8 b_{n, \alpha} e^{-n \beta_{*} u} \omega_{D}^{n-1},$$
where $b_{n, \alpha}$ was defined in (3.43). The holomorphic volume form for the complex structure $J$ can be written as
$$\Omega=v(1-\phi)^{*}\left(\eta^{1,0} \wedge \Omega_{D}\right)$$
for some function $v$. Then the infinitesimal action of $\xi_{f}$ is given by
$$\begin{aligned}
\left(\mathcal{L}_{\xi_{f}} \Omega_{L}\right)^{1,0} & \left.=\partial\left(\xi_{f}\right\lrcorner \Omega_{L}\right) \\
& \left.=\partial\left(\frac{1}{2} f \Omega_{D}+\eta^{1,0} \wedge \sharp \bar{\partial}_{H} f\right\lrcorner \Omega_{D}\right) \\
& \left.=\eta^{1,0} \wedge\left(i \zeta \partial_{\zeta}\left(f \Omega_{D}\right)-\partial_{H}\left(\sharp \bar{\partial}_{H} f\right\lrcorner \Omega_{D}\right)\right) \\
& =i \eta^{1,0} \wedge\left(\zeta \partial_{\zeta}\left(f \Omega_{D}\right)-2 \Delta_{\partial}\left(f \Omega_{D}\right)\right) .
\end{aligned}$$

We now prove the Proposition by induction on $j$. From Proposition 5.1 we know that Proposition 5.2 is true for $j=1$. (One of course does not need the full strength of Proposition 5.1, it is sufficient to construct by hand a good enough Y). So suppose it is true for $j$ and let us prove it for $j+1$.

We begin by rectifying $\phi$ and constructing $\phi_{j}$. Let $\phi^{\prime}$ contain the order $j$ terms of $\phi$, that is $\phi=\sum_{1}^{j-1} \phi_{i} \zeta^{i}+\phi^{\prime}+O\left(\zeta^{j+1}\right)$. We first consider the infinitesimal problem, so we consider the infinitesimal action of for some vector field $\xi=i f \zeta \partial_{\zeta}+X$ of order $j$. Denote by $\phi_{H H}^{\prime}, \phi_{H V}^{\prime}, \phi_{V H}^{\prime}$ and $\phi_{V V}^{\prime}$ the various components of $\phi^{\prime}$ in the decomposition $T_{\mathbb{C}}=\mathbb{C} \zeta \partial_{\zeta} \oplus H_{\mathbb{C}}$. From the first term in (5.3) we see that we can find $\xi=f i \zeta \partial_{\zeta}+X$ of order $j$ so that $(\bar{\partial} \xi)_{V H}=\phi_{V H}^{\prime}$ and $(\bar{\partial} \xi)_{V V}=\phi_{V V}^{\prime}$; note that $f$ and $X$ are defined up to fibrewise holomorphic terms, that is up to terms $\zeta^{j}\left(f_{j} i \zeta \partial_{\zeta}+X_{j}\right)$. Thanks to the action of $\mathfrak{F}$ we are now reduced to the case where $\phi_{V H}^{\prime}=0$ and $\phi_{V V}^{\prime}=0$, that is $\phi^{\prime}$ has the form
$$\phi^{\prime}=\tilde{\phi}+\alpha \otimes i \zeta \partial_{\zeta}+\phi_{H H}^{\prime},$$
where $\alpha \in H_{0,1}$ and $\phi_{H H}^{\prime}$ are terms of order $j$. The integrability equation $\bar{\partial} \phi^{\prime}+$ $\frac{1}{2}\left[\phi^{\prime}, \phi^{\prime}\right]=0$ implies
$$\bar{\zeta} \partial_{\bar{\zeta}} \phi^{\prime}=O\left(\zeta^{j+1}\right)$$
and in particular $\partial_{\bar{\zeta}} \alpha=0$ and $\partial_{\bar{\zeta}} \phi_{H H}^{\prime}=0$. Defining a horizontal vector field $X$ by $X\lrcorner d \eta=\alpha$ we have from (5.3)
$$\bar{\partial} X=\alpha \otimes i \zeta \partial_{\zeta}+\bar{\partial}_{H} X$$
and therefore the infinitesimal action of $X$ kills the residual term $\alpha$.
Summarizing, we get a vector field $\xi$ of order $j$ which infinitesimally brings $\phi^{\prime}$ to a purely horizontal $\tilde{\phi}_{j}$. Choosing some smooth Kähler metric near $D$ and its exponential, we can now apply the diffeomorphism $\exp (\Re \xi)$ to $(J, \Omega)$ : we consider $\mathrm{Y}^{\prime}=\mathrm{Y} \circ \exp (\Re \xi)$ and the corresponding pair $\left(\phi^{\prime}, v^{\prime}\right)$. Since the dominant term of the action is given by the infinitesimal action of $\xi_{f}$ (the exponential gives only higher order terms) this implies that:
\begin{itemize}
\item[-] $\phi^{\prime}=\sum_{1}^{j-1} \phi_{j} \zeta^{j}+\tilde{\phi}_{j}+O\left(\zeta^{j+1}\right)$ with $\tilde{\phi}_{j}$ purely horizontal;
\item[-] we still have $v^{\prime}=1+O\left(\zeta^{j}\right)$ since $\xi$ has order $j$.
\end{itemize}
Also note that (5.10) implies that $\tilde{\phi}_{j}$ is holomorphic with respect to $\zeta$, that is has the required form $\zeta^{j} \tilde{\phi}_{j}$. So we have proved the induction for $\phi$, and there remains to rectify the function $v$.

One can remark here that since $\xi$ is obtained by solving a problem disk per disk, it a priori has the same regularity as $\phi^{\prime}$, when one would expect a better regularity (one more derivative on $X$ and two more on $f$ ). This explains the loss of derivatives alluded to above.

We now must kill the order $j$ term of $v^{\prime}$. From $\bar{\partial} \Omega=0$ and the fact that $\phi$ is purely horizontal up to order $j$, we deduce that the $j$-th order term of $v^{\prime}$ is holomorphic along the fiber (that is with respect to $\zeta$ ), which means that it can be written as $v_{j}^{\prime} \zeta^{j}$ for a section $v_{j}^{\prime}$ of $L^{-j}$. From the Weitzenböck formula $2 \Delta_{\partial}=$ $\nabla^{*} \nabla+j$ on sections of $K_{D} L^{\alpha-j-1}$, we deduce, for a section $f \Omega_{D}$ of $K_{D} L^{\alpha-j-1}$,
$$-\zeta \partial_{\zeta}\left(f \Omega_{D}\right)+2 \Delta_{\partial}\left(f \Omega_{D}\right)=\left(\nabla^{*} \nabla+\alpha-1\right)\left(f \Omega_{D}\right) .$$
Since $\alpha>1$ the operator $\nabla^{*} \nabla+\alpha-1$ is an isomorphism, and therefore the term $v_{j}^{\prime} \xi^{j}$ can be killed infinitesimally by a vector $\xi_{f}$ for some $f=f_{j} \zeta^{j}$ and $f_{j} \Omega_{D}$ is a section of $L^{-j}$. We now apply as above the diffeomorphism $\exp \left(\Re \xi_{f}\right)$ to $(J, \Omega)$ : we obtain a new pair $\left(\phi^{\prime \prime}, v^{\prime \prime}\right)$. Since the dominant term of the action is given by the infinitesimal action of $\xi_{f}$, this implies that:
\begin{itemize}
\item[-] the order $j$ term of $v^{\prime}$, that is $v_{j}^{\prime} \xi^{j}$, is killed by $\exp \left(\Re \xi_{f}\right)$, so we have now $v^{\prime \prime}=1+O\left(\zeta^{j+1}\right)$;
\item[-] as observed above, the vector field $\xi_{f}$ infinitesimally preserves the horizontal gauge, it actually modifies the order $j$ term of $\phi^{\prime}$ by $-\bar{\partial}_{H} \sharp \bar{\partial}_{H} f$ so we get an order $j$ term $\zeta^{j}\left(\tilde{\phi}_{j}+\bar{\partial}_{H} \sharp \bar{\partial}_{H} f_{j}\right)$.
\end{itemize}

So by choosing $\phi_{j}=\tilde{\phi}_{j}+\bar{\partial}_{H} \sharp \bar{\partial}_{H} f_{j}$ we have finished to prove the Proposition for $j+1$. \(\square\)

Proposition 5.3. Given the normal form from Proposition 5.2, the smallest integer $j_{0}$ such that $\phi_{j_{0}} \neq 0$ is intrinsic. Actually $j_{0}$ is the largest integer such that there exists a diffeomorphism $\mathrm{Y}: \Delta_{L} \rightarrow \mathcal{U}_{L}$ such that $\mathrm{Y}^{*} \Omega$ and $\Omega_{L}$ coincide up to order $j_{0}-1$.

Proof. Let $\ell$ be the order of coincidence of $\Omega$ and $\Omega_{L}$ as defined in the proposition, and $j_{0}$ the first integer so that $\phi_{j_{0}} \neq 0$. By definition we have $\ell \geq j_{0}-1$. On the other hand, if $\Omega$ and $\Omega_{L}$ coincide up to order $\ell$, then the complex structures $J$ and $J_{L}$ also coincide up to order $\ell$, since they are determined by the holomorphic forms. If $j_{0}<\ell+1$ it therefore means that our term $\zeta^{j_{0}} \phi_{j_{0}}$ can be killed by a diffeomorphism: as it is the first nonvanishing term, it means that it can be killed by an infinitesimal diffeomorphism which also preserves the condition $v=1$. The infinitesimal action of diffeomorphisms was calculated in the proof of Proposition 5.2, and it turns out that at each step the vector field is unique (to preserve the normal form of $\phi$ one needs $\mathfrak{Z}=\xi_{f}$ with $f$ holomorphic along the fibres; then the condition $v=1$ kills this remaining degree of freedom). Therefore it is impossible to kill the first term by an infinitesimal diffeomorphism, so we must have $\ell=j_{0}-1$. \(\square\)

Remark 5.4. The $T_{D}^{1,0}$-valued (0,1)-form $\phi_{1} \zeta$ is $\bar{\partial}$-closed and represent the extension class $\kappa$ of $N_{D}$ by $T_{D}$ in $H^{1}\left(D, T_{D} \otimes N_{D}^{-1}\right)$. In particular, we have $j_{0}=1$ if, and only if $\kappa \neq 0$, or equivalently, iff the normal exact sequence (4.4) does not split, cf the first paragraph of section 4.2.
5.3. The real volume form. Using Propositions 5.1 and 5.2 we can now give an optimal development of the volume form $\Omega \wedge \bar{\Omega}$ by comparison with $\Omega_{L} \wedge \overline{\Omega_{L}}$. We develop the tensor $\phi$ from Proposition 5.1 in powers of $\zeta$ as
$$\phi=\phi_{1} \zeta+\phi_{2} \zeta^{2}+\cdots$$
One can identify $\phi_{j}$ with a section on $D$ of $\Omega_{D}^{0,1}\left(T_{D}^{1,0} \otimes L^{-j}\right)$. This is valid up to some order which we can take large enough for what follows.

Suppose for simplicity that $\phi_{1} \neq 0$. The linearization with respect to $\phi$ of $(1-\phi)^{*} \Omega_{L}$ is $\left.\phi\right\lrcorner \Omega_{L}$ : here $\phi \in \Omega^{0,1} \otimes T^{1,0}, \Omega_{L} \in \Omega^{n, 0}$ and $\left.\phi\right\lrcorner \Omega_{L} \in \Omega^{n-1,1}$. It follows from Proposition 5.2 that
$$\left.\mathrm{Y}^{*} \Omega=\Omega_{L}-\phi_{1} \zeta\right\lrcorner \Omega_{L}+O\left(\zeta^{2}\right) .$$

Therefore
$$\begin{aligned}
\mathrm{Y}^{*}(\Omega \wedge \bar{\Omega}) & \left.=\Omega_{L} \wedge \overline{\Omega_{L}}+\left(\phi_{1} \zeta\right\lrcorner \Omega_{L}\right) \wedge \overline{\left.\left(\phi_{1} \zeta\right\lrcorner \Omega_{L}\right)}+O\left(\zeta^{3}\right) \Omega_{L} \wedge \overline{\Omega_{L}} \\
& =\Omega_{L} \wedge \overline{\Omega_{L}}\left(1-\left|\phi_{1} \zeta\right|^{2}+O\left(\zeta^{3}\right)\right) .
\end{aligned}$$
The essential feature in this formula is that no linear term in $\phi_{1}$ appears because $\left.\phi_{1}\right\lrcorner \Omega_{L}$ is of type $(n-1,1)$. This makes possible for the correction term to exhibit a sign which will be important for us.

The same calculation when the first nonzero term is $\phi_{j_{0}}$ leads to:
Proposition 5.5. Suppose Y is given by Proposition 5.2 and that the first nonzero term in (5.12) is of order $j_{0}$. Then
$$\mathrm{Y}^{*}(\Omega \wedge \bar{\Omega})=\Omega_{L} \wedge \overline{\Omega_{L}}\left(1-\left|\phi_{j_{0}} \zeta^{j_{0}}\right|^{2}+O\left(\zeta^{2 j_{0}+1}\right)\right) .$$ \(\square\)

\section*{6. The Tian-Yau metric and its formal perturbation}

Fix a Kähler-Einstein metric $\omega_{D}$ on $D$ such that $\operatorname{Ric} \omega_{D}=\omega_{D}$ and a Hermitian metric $h$ on $L=N_{D}$ such that $i \Theta(L, h)=\frac{1}{\alpha-1} \omega_{D}$. Let $\sigma$ be the section of $[D]$ vanishing on $D$, and $\Omega$ the holomorphic volume form on $X \backslash D$, normalized as in section 5.2 (again, only some power is well-defined). The Tian-Yau metric [TY91] of ( $X, D$ ) is defined in the following way: there is a unique Ricci flat Kähler metric $\omega_{\mathrm{TY}}=d d^{c} \Phi_{\mathrm{TY}}$ on $X \backslash D$, solving the Monge-Ampère equation
$$\left(d d^{c} \Phi_{\mathrm{TY}}\right)^{n}=i^{n^{2}} \Omega \wedge \bar{\Omega}$$
and such that near $D$
$$\Phi_{\mathrm{TY}} \sim|\sigma|^{-2 \beta_{*}} .$$
Here it may be necessary to adjust the metric on $L$ by a multiplicative constant in order to obtain exactly (6.1).

The asymptotic Calabi-Yau cone of the Tian-Yau metric is easily described using the formalism of section 3.1: it is the bundle $L$ equipped with the cone metric
$$\omega_{\mathrm{TY}, L}=d d^{c} e^{-\beta_{*} u} .$$

Indeed from (5.5) and (5.6) the holomorphic volume form satisfies
$$\begin{aligned}
i^{n^{2}} \Omega_{L} \wedge \overline{\Omega_{L}} & =8 b_{n, \alpha} i e^{-n \beta_{*} u} \eta^{1,0} \wedge \eta^{0,1} \wedge \omega_{D}^{n-1} \\
& =b_{n, \alpha} e^{-n \beta_{*} u} d u \wedge d^{c} u \wedge \omega_{D}^{n-1} \\
& =b_{n, \alpha} \Xi .
\end{aligned}$$
Comparing with (3.5), where $-\phi_{\mathrm{TY}, L}^{\prime}(u)=\beta_{*} e^{-\beta_{*} u}$, we obtain exactly
$$\omega_{\mathrm{TY}, L}^{n}=i^{n^{2}} \Omega_{L} \wedge \overline{\Omega_{L}}$$
which finishes the description of the Calabi-Yau cone. In particular the Calabi-Yau cone has radius $R=2 e^{-\frac{1}{2} \beta_{*} u}=2\left|\sigma_{L}\right|^{-\beta_{*}}$, where $\sigma_{L}$ is the tautological section of $L$ over $L$.
6.1. Asymptotic expansion of the Tian-Yau potential. We now use the diffeomorphism $\mathrm{Y}: \Delta_{L} \rightarrow U_{L}$ of section 5 to give an asymptotic expansion of $\Phi_{\mathrm{TY}}$. It will be convenient to distinguish objects on $\Delta_{L}$ from objects pulled-back by Y by an index (for example $d^{c}$ is for the complex structure $J$ on $U_{L}$ and $d_{J_{L}}^{c}$ for $J_{L}$ on $L$ ). To simplify notation, we will use Proposition 5.2 as if $j=\infty$ that is as if $\phi$ was purely horizontal at all orders: indeed taking the order $j$ large enough in the Proposition leads only to small error terms which do not play any role, see section 8 where the error terms are given.

On $L$ we have the exact potential $\Phi_{0}=\left|\sigma_{L}\right|^{-2 \beta_{*}}=R^{2} / 4$. Because the tensor $\phi$ expressing the difference $\mathrm{Y}^{*} J-J_{L}$ is horizontal and $\Phi_{0}$ depends only on $R$ (or $\left|\sigma_{L}\right|$ ), it follows that
$$d d^{c} \Phi_{0}=d d_{J_{L}}^{c} \Phi_{0} .$$
If we use $\Phi_{0}$ in equation (6.1), the first error therefore comes from the difference between $\Omega \wedge \bar{\Omega}$ and $\Omega_{L} \wedge \overline{\Omega_{L}}$ :
$$\frac{\left(d d^{c} \Phi_{0}\right)^{n}}{i^{n^{2}} \Omega \wedge \bar{\Omega}}=1+\left|\phi_{j_{0}}\right|^{2}+O\left(|\sigma|^{2 j_{0}+1}\right) .$$
Extend $\Phi_{0}$ as a potential on $X \backslash D$ and define $\omega_{0}=d d^{c} \Phi_{0}$ and $g=\frac{\left(d d^{c} \Phi_{0}\right)^{n}}{i^{n^{2}} \Omega \wedge \bar{\Omega}}$, so that the expansion of $g$ at infinity is given by the RHS of (6.6). To find the exact solution $\Phi_{\text {TY }}$ we must solve the Monge-Ampère equation on $X \backslash D$
$$\left(\omega_{0}+d d^{c} f\right)^{n}=g \omega_{0}^{n}$$

Observe that $\left|\phi_{j_{0}}\right|^{2}=O\left(|\sigma|^{2 j_{0}}\right)=O\left(R^{-\frac{2 j_{0}}{\beta_{*}}}\right)$, and that since $\alpha<n+1$, the decay rate satisfies
$$\frac{2 j_{0}}{\beta_{*}}>2 j_{0} \geq 2 .$$
We can now apply [CH13, Theorems 2.1 and 2.4]. There are two cases, depending whether the decay rate $\frac{2 j_{0}}{\beta_{*}}$ allows the Green's function $\left(R^{-2 n+2}\right)$ to be the first perturbation of $\Phi_{0}$, and an additional limit case:
\begin{itemize}
\item[-] if $\frac{2 j_{0}}{\beta_{*}}<2 n$, that is if $\alpha \geq 1+j_{0}$, then one can solve (6.7) with $f=$ $O\left(R^{-\frac{2 j_{0}}{\beta_{*}}+2}\right)$ (and the corresponding weighted decays for the derivatives);
\item[-] if $\frac{2 j_{0}}{\beta_{*}}>2 n$, that is if $\alpha<1+j_{0}$, then one can solve (6.7) with
$$f=\frac{a}{R^{2 n-2}}+O\left(R^{-2 n+2-\varepsilon}\right) ;$$
\item[-] if $\frac{2 j_{0}}{\beta_{*}}=2 n$, we have an indicial root of the Laplacian (corresponding to the decay $R^{-2 n+2}$ of the Green function) so we need to first kill by hand the term of order $R^{-2 n}$ of $g$ : we correct the potential by a function $f_{0}=$ $a R^{-2 n+2} \log R+O\left(R^{-2 n+2}\right)$ so that $\omega_{0}+d d^{c} f_{0}$ now satisfies (6.7) with $g-$ $1=O\left(R^{-2 n-\varepsilon}\right)$, then we can proceed as in the previous case.
\end{itemize}
In each case the solution is unique. We will introduce the notation
$$v_{0}:=\frac{j_{0}}{\beta_{*}}$$
so that the qualitative asymptotics of the solution $f$ depend on the value of $v_{0}$ in relation to $n$. This gives the first part of the following result:

Theorem 6.1. The potential of the Tian-Yau metric on $X \backslash D$ has the expansion
$$\mathrm{Y}^{*} \Phi_{\mathrm{TY}}=\frac{R^{2}}{4}+ \begin{cases}O\left(R^{-2 v_{0}+2}\right) & \text { if } v_{0}<n, \\ a \frac{\log R}{R^{2 n-2}}+O\left(R^{-2 n+2}\right) & \text { if } v_{0}=n, \\ \frac{a}{R^{2 n-2}}+O\left(R^{-2 n+2-\varepsilon}\right) & \text { if } v_{0}>n,\end{cases}$$
where $\varepsilon>0$ is small. Moreover in the last cases we have a > 0.
Proof. Here we work with the Tian-Yau metric as background metric. There remains to prove the statement on the sign of $a$. The two cases $v_{0}=n$ and $v_{0}>n$
are different in nature, since the argument is local in the first case, and global in the second case.

In the first case $\left(v_{0}=n\right)$ the coefficient $a$ is formally determined by the asymptotic terms of equation (6.7): the linearization of the LHS of (6.7) is $-\Delta f$, and on the asymptotic cone $-\Delta\left(R^{-2 n+2} \log R\right)=(2 n-2) R^{-2 n+2}$; since $g=$ $1+b R^{-2 n+2}+O\left(R^{-2 n+2-\varepsilon}\right)$ with $b>0$ (see (6.6), we have $a>0$.

The second case $\left(v_{0}>n\right)$ requires more work. For a one form $u$ on $X \backslash D$ denote by $\nabla^{-} u$ the $J$-anti-invariant part of $\nabla u$ :
$$\begin{aligned}
\left(\nabla^{-} u\right)_{X, Y} & =\frac{1}{2}\left(\left(\nabla_{X} u\right)_{Y}-\left(\nabla_{J X} u\right)_{J Y}\right) \\
& =-\frac{1}{2} \omega\left(\left(\mathcal{L}_{\sharp u} J\right) X, Y\right) .
\end{aligned}$$
Here ♯ denotes the Riemannian duality between $T X$ and $T^{*} X$. In particular $\nabla^{-} u=0$ if and only if $\sharp u$ is a holomorphic vector field. Given a function $f$ the $(0,2)$ part of $\nabla^{-} d f$ is the familiar operator $\bar{\partial} \sharp \bar{\partial} f$. Moreover one has the Weitzenböck type formula [Bes87, (2.51) and (2.53)]
$$\delta \nabla^{-} u=\frac{1}{2} \Delta u-\operatorname{Ric} u .$$

The Tian-Yau potential $\Phi=\Phi_{\text {TY }}$ satisfies $\Delta \Phi=-4 n$ and we deduce from (6.11) that
$$\delta \nabla^{-} d \Phi=\frac{1}{2} \Delta d \Phi=\frac{1}{2} d \Delta \Phi=0$$
By integration by parts, denoting $\vec{n}$ the outward normal vector to the hypersurface $S_{R}$ of level $R$ :
$$\begin{aligned}
0 & =\int_{X \backslash D}\left\langle\delta \nabla^{-} d \Phi, d \Phi\right\rangle \\
& \left.=\int_{X \backslash D}\left|\nabla^{-} d \Phi\right|^{2}-\lim _{R \rightarrow \infty} \int_{S_{R}} \nabla^{-} d \Phi(\vec{n}, \nabla \Phi) \vec{n}\right\lrcorner d \mathrm{vol}
\end{aligned}$$
From the development (5.12) of the complex structure and the development (6.10) of the potential, and denoting $p=\inf \left(2 n, \frac{j_{0}}{\beta_{*}}\right)$, we have:
$$\begin{aligned}
g & =g_{\text {cone }}+O\left(R^{-p}\right), \\
\vec{n} & =\partial_{R}+O\left(R^{-p}\right), \\
\nabla \Phi & =2 R \partial_{R}+O\left(R^{-p+1}\right), \\
\nabla^{-} d R^{2} & =O\left(R^{-p}\right) .
\end{aligned}$$

Under our hypothesis that $\frac{2 j_{0}}{\beta_{*}}>2 n$, we have that $p>n$ and therefore
$$\left.\left.\lim _{R \rightarrow \infty} \int_{S_{R}} \nabla^{-} d R^{2}(\vec{n}, \nabla \Phi) \vec{n}\right\lrcorner d \mathrm{vol}=\lim _{R \rightarrow \infty} \int_{S_{R}} \nabla^{-} d R^{2}\left(\partial_{R}, 2 R \partial_{R}\right) \partial_{R}\right\lrcorner d \mathrm{vol}$$
since the other (quadratic) terms are too small to give a nonzero limit. But the term at order $R^{-j_{0} / \beta_{*}}$ of $\nabla^{-} d R^{2}$ is linear in $\phi_{j_{0}}$ and $\overline{\phi_{j_{0}}}$, so has Fourier coefficients of orders only $\pm j_{0}$ so its integral on $S_{R}$ against constant terms vanishes.

Therefore our boundary term reduces to
$$\left.\lim _{R \rightarrow \infty} \int_{S_{R}} a \nabla^{-} d R^{-2 n+2}\left(\partial_{R}, 2 R \partial_{R}\right) \partial_{R}\right\lrcorner d \mathrm{vol}$$
But $\nabla^{-} d R^{-2 n+2}=4 n(n-1) \frac{\left((d R)^{2}\right)^{-}}{R^{2 n}}+$ l.o.t. and it follows that the limit in (6.15) is $a \ell$ for some $\ell>0$. Coming back to (6.13) we finally obtain
$$\int_{X \backslash D}\left|\nabla^{-} d \Phi\right|^{2}=a \ell$$
and it follows that $a \geq 0$, with $a=0$ if and only if $\nabla^{-} d \Phi=0$, that is if $\nabla \Phi$ is a (real) holomorphic vector field and an homothety of the metric. Since $\nabla \Phi \sim 2 R \partial_{R}$ we have a cone and $\nabla \Phi$ is the dilation vector field. Considering the asymptotics at infinity, the cone can only be the asymptotic cone of the Tian-Yau metric, that is $\bar{L} \backslash D$, where $\bar{L}$ is the one point compactification of $L$ considered in section 4. This can be smooth only in the case where $X=\mathbb{P}^{n}$ and $D$ is an hyperplane, which was excluded. \(\square\)

Remark 6.2. The result on the sign of $a$ in this Theorem is opposite to that obtained on crepant resolutions of a finite quotient of $\mathbb{C}^{n}$, see [Joy00, Theorem 8.2.3].

Remark 6.3. The proof of Theorem 6.1 is reminiscent of the argument in [BH23, § 3.2]. The difference is that the argument in [BH23] is in real Riemannian geometry, so formula (6.11) is replaced by $\nabla \Delta f=\Delta \nabla f+\operatorname{Ric} \nabla f$, and the complex Hessian $\nabla^{-} d f$ by the real Hessian of $f$.
6.2. The formal perturbation. The Tian-Yau metric is Ricci flat, but we want to glue it with a metric with $\operatorname{Ric}=\mu$. Given the scale $\varepsilon$, this means we will construct a perturbation $\omega_{\mathrm{TY}, \varepsilon}$ of $\omega_{\mathrm{TY}}$ such that $\operatorname{Ric}\left(\omega_{\mathrm{TY}, \varepsilon}\right)=\varepsilon \mu \omega_{\mathrm{TY}, \varepsilon}$. This perturbation will match better the metric constructed on the normal bundle $L$ and will be needed to successfully perform the gluing later, cf Remark 9.2.

Since $X \backslash D$ is not compact, this is of course not possible, but it can be done formally up to any order. Denote the development of the potential $\phi_{\beta_{*}, L}$ near the cone singularity by
$$\phi_{\beta_{*}, L}(x)=\frac{1}{4} r^{2}+a_{2} r^{4}+a_{3} r^{6}+\cdots$$

We want to solve the Kähler-Einstein equation on $X \backslash D$ :
$$P_{\varepsilon}(\varphi):=\log \frac{\left(\omega_{\mathrm{TY}}+d d^{c} \varphi\right)^{n}}{i^{n^{2}} \Omega \wedge \bar{\Omega}}+\varepsilon \mu\left(\Phi_{\mathrm{TY}}+\varphi\right)=0 .$$

Proposition 6.4. For any integer $k$ there is a development $\varphi=\varepsilon \varphi_{1}+\cdots+\varepsilon^{k} \varphi_{k}$ such that
\begin{itemize}
\item[(1)] there is a formal development $P_{\varepsilon}(\varphi)=\sum_{i>k} \varepsilon^{i} p_{i}$ with $p_{i}=O\left(R^{2 i}\right)$ (and the same for the weighted derivatives $R^{j} \nabla^{j}$ ); moreover, on any domain $R \leq C \varepsilon^{-\theta / 2}$ the series for $P_{\varepsilon}(\varphi)$ converges if $\varepsilon$ is small enough, and one has an estimate
$$\left|R^{j} \nabla^{j} P_{\varepsilon}(\varphi)\right| \leq C_{k, j} \varepsilon^{k+1} R^{2 k+2} .$$
\item[(2)] at infinity one has $\varphi_{k}(y)=a_{k+1} R^{2 k+2}+O\left(R^{2 k+2-2 v_{0}}\right)+O\left(R^{-2 n+2}\right)$; again the same estimates hold on the weighted derivatives $R^{j} \nabla^{j}$.
\end{itemize}

Proof. We solve inductively the equation (6.18) in powers of $\varepsilon$. The first equation is
$$-\Delta \varphi_{1}+\mu \Phi_{\mathrm{TY}}=0 .$$
Because $\phi_{\beta_{*}, L}$ is an exact solution on the cone, the function $a_{2} R^{4}$ is a solution of $\Delta\left(a_{2} R^{4}\right)=\mu \frac{R^{2}}{4}$ up to the order where the equations for $J$ and $J_{L}$ differ, that is up to the order where $\Omega \wedge \bar{\Omega}$ and $\Omega_{L} \wedge \bar{\Omega}_{L}$ differ: so given (6.10) we obtain
$$-\Delta\left(a_{2} R^{4}\right)+\mu \Phi_{\mathrm{TY}}=O\left(R^{2-2 v_{0}}\right) .$$
Therefore we can find $\varphi_{1}=\chi a_{2} R^{4}+\psi_{1}$ (where $\chi$ is a cutoff function near infinity) by solving $\Delta \psi_{1}=-\Delta\left(\chi a_{2} R^{4}\right)+\mu \Phi_{\mathrm{TY}}$, which is possible with $\psi_{1}=$ $O\left(R^{4-2 \nu_{0}}\right)+O\left(R^{-2 n+2}\right)$. (The second term is present for the case where $4-$ $2 v_{0}<-2 n+2$ ). The error term in $P_{\varepsilon}\left(\varepsilon \varphi_{1}\right)$ is:
\begin{itemize}
\item[-] the nonlinear terms in Monge-Ampère: $d d^{c}\left(\varepsilon \phi_{1}\right)=O\left(\varepsilon R^{2}\right)$ so the nonlinear terms are $O\left(\left(\varepsilon R^{2}\right)^{i}\right)$ with $i>1$; applying the log gives the formal development in $\varepsilon$;
\item[-] $\varepsilon^{2} \mu \varphi_{1}$ which is also $O\left(\varepsilon^{2} R^{4}\right)$.
\end{itemize}

On the domain $R \leq C \varepsilon^{-\theta / 2}$, we have $\varepsilon R^{2} \leq C \varepsilon^{1-\theta}$ which is small when $\varepsilon \rightarrow$ 0, and it follows that the series of the logarithm converges, which implies the estimate.

Continuing this process inductively we get the proposition. \(\square\)

\section*{7. Gluing and linear analysis}
7.1. Gluing with the conic Calabi Ansatz and the Tian-Yau metric. Recall that on $L$, we have the coordinate $u:=\log |v|_{h}^{2}$, as well as a Kähler-Einstein potential $\phi_{\beta, L}=\phi_{\beta, L}(u)$ defined for larger and larger values of $u$ as $\beta$ approaches $\beta_{*}$; more precisely it is defined in the zone ( $u \leqslant u_{\beta}$ ) where $u_{\beta}=-\frac{1}{n \beta_{*}} \log \left(\beta-\beta_{*}\right)$ up to a constant, cf (3.28).

In order to glue the potential $\phi_{\beta, L}$ to the Tian-Yau potential via Y, one first needs to rescale $L$ so that most of the domain of $\phi_{\beta, L}$ is included in the domain of Y. We have already identified the correct rescaling $\lambda_{\varepsilon}: L \rightarrow L$ in (3.53). It will be convenient to introduce the following notation
$$\phi_{\beta, L, \varepsilon}:=\left(\lambda_{\varepsilon}\right)_{*} \phi_{\beta, L}$$
as well as
$$\mathrm{Y}_{\varepsilon}:=\mathrm{Y} \circ \lambda_{\varepsilon}$$
which is defined on larger and larger regions in $L$. Finally, if $\zeta$ is the variable in $L$, we will write
$$\zeta_{\varepsilon}:=\lambda_{\varepsilon}^{*} \zeta=\varepsilon^{\frac{1}{2 \beta_{*}}} \zeta .$$

Moreover, in order for the potential to match the Tian-Yau potential, the gluing needs to be done near $u_{\varepsilon}$ (i.e. on a zone of the form $\left|u-u_{\varepsilon}\right| \leqslant 1$ ) satisfying
$$1 \ll u_{\varepsilon} \ll-\frac{1}{n \beta_{*}} \log \left(\beta-\beta_{*}\right),$$
or equivalently in terms of the variable $r=2 e^{-\frac{1}{2} \beta_{*} u}$
$$\left(\beta-\beta_{*}\right)^{\frac{1}{n}} \ll r_{\varepsilon}^{2} \ll 1,$$
where $r_{\varepsilon}:=2 e^{-\frac{1}{2} \beta_{*} u_{\varepsilon}}$. We will choose $r_{\varepsilon}$ of the form $r_{\varepsilon}=\varepsilon^{\frac{1-\theta}{2}}$ for some $\theta \in(0,1)$ to be determined later so that
$$\frac{\varepsilon}{r_{\varepsilon}^{2}}=\varepsilon^{\theta} .$$

We fix once and for all a point $x_{0} \in X \backslash U_{L}$ and we set $R=d_{g_{\mathrm{TY}}}\left(\cdot, x_{0}\right)$. Next, we introduce a positive function $\rho=\rho(\beta, \varepsilon)$ on $X$ by
$$\rho^{2}:=\left\{\begin{array}{lll}
-\frac{4}{\beta_{*}} \phi_{\beta, L}^{\prime} \circ \mathrm{Y}_{\varepsilon}^{-1} & \text { on } & \mathrm{Y}_{\varepsilon}\left(\left\{u \leqslant u_{\varepsilon}\right\}\right) \\
\varepsilon R^{2} & \text { on } & \mathrm{Y}_{\varepsilon}\left(\left\{u \geqslant u_{\varepsilon}\right\} \cap \Delta_{L}\right) \\
\varepsilon & \text { on } & X \backslash U_{L}
\end{array}\right.$$
The function $\rho$ has values in $\left[\sqrt{\varepsilon}, 2 \sqrt{\alpha / \beta_{*}}\right]$. More precisely, it is equal to $2 \sqrt{\alpha / \beta_{*}}$ on $D$, then "decreases" to reach the value $r_{\varepsilon}$ near the gluing zone, and from there keeps decreasing to $\sqrt{\varepsilon}$.

We fix two positive integers $j, k$ and we consider the diffeomorphism Y from Proposition 5.2 as well as the $k$-th order formal perturbation of the Tian-Yau potential $\Phi_{\mathrm{TY}, \varepsilon}=\Phi_{\mathrm{TY}}+\varphi$ constructed in section 6.2. We will determine suitable values for $j$ and $k$ further in the text.

Let $\chi:[0,+\infty) \rightarrow[0,1]$ be a non-increasing function which is identically 0 on $\left[0, \frac{1}{2}\right]$ and identically 1 on $[2,+\infty)$, and let $\chi_{\varepsilon}: X \rightarrow[0,1]$ be defined by $\chi_{\varepsilon}=\chi\left(\frac{\rho}{r_{\varepsilon}}\right)$, so that
$$\chi_{\varepsilon}= \begin{cases}1 & \text { on } \quad \rho \geqslant 2 r_{\varepsilon} \\ 0 & \text { on } \quad \rho \leqslant \frac{1}{2} r_{\varepsilon}\end{cases}$$
Finally, we introduce the potential
$$\varphi_{\beta, \varepsilon}:=\chi_{\varepsilon}\left(\mathrm{Y}_{\varepsilon}\right)_{*} \phi_{\beta, L}+\left(1-\chi_{\varepsilon}\right) \varepsilon \Phi_{\mathrm{TY}, \varepsilon}$$
which is well-defined globally on $X$. In the gluing zone, we have
$$\mathrm{Y}_{\varepsilon}^{*} \varphi_{\beta, \varepsilon}=\phi_{\beta, L}+\left(1-\chi_{\varepsilon}\right)\left(\mathrm{Y}_{\varepsilon}^{*}\left(\varepsilon \Phi_{\mathrm{TY}, \varepsilon}\right)-\phi_{\beta, L}\right) .$$

We set $\omega_{\beta, \varepsilon}:=d d^{c} \varphi_{\beta, \varepsilon}$, which is a Kähler metric on $X \backslash D$ with cone singularities of angle $2 \pi \beta$ along $D$. We denote by $g_{\beta, \varepsilon}$ the corresponding Riemannian metric.

We will solve the Kähler-Einstein equation $\operatorname{Ric}\left(\omega_{\beta, \varepsilon}+d d^{c} \varphi\right)=\mu \omega_{\beta, \varepsilon}+$ $d d^{c} \varphi$ under the form
$$P_{\beta, \varepsilon}(\varphi):=\log \frac{\left(\omega_{\beta, \varepsilon}+d d^{c} \varphi\right)^{n}}{\varepsilon^{n} i^{n^{2}} \Omega \wedge \bar{\Omega}}+\mu\left(\varphi_{\beta}+\varphi\right)=0,$$
where the normalization factor $\varepsilon^{n}$ comes from the rescaling $\lambda_{\varepsilon}$. Indeed, on $L$ the constants were choosen so that one has exactly $\left(d d^{c} \phi_{\beta, L}\right)^{n}=e^{-\mu \phi_{\beta, L}} i^{n^{2}} \Omega_{L} \wedge \bar{\Omega}_{L}$, see (3.42) and (6.4); therefore, we get
$$\left(d d^{c} \phi_{\beta, L, \varepsilon}\right)^{n}=\varepsilon^{n} e^{-\mu \phi_{\beta, L, \varepsilon} i \eta^{n^{2}} \Omega_{L} \wedge \bar{\Omega}_{L}}$$
with the notation (7.1), cf also (8.1) further below. We introduce the notations
$$L_{\beta, \varepsilon}:=\Delta_{\omega_{\beta, \varepsilon}}+\mu_{\beta}, \quad \text { and } \quad Q_{\beta, \varepsilon}:=P_{\beta, \varepsilon}-P_{\beta, \varepsilon}(0)-L_{\beta, \varepsilon} .$$
An elementary computation shows that if $\left|d d^{c} f\right|_{\omega_{\beta, \varepsilon}} \leqslant 1$, then
$$\left|Q_{\beta, \varepsilon}(f)\right| \leqslant C\left|d d^{c} f\right|_{\omega_{\beta, \varepsilon}}^{2}$$
for some $C>0$ independent of $f, \beta, \varepsilon$.
7.2. Functional spaces. Fix a real number $\delta$. For any function $f$ on $X$, we define the weighted norms (which depends on $\beta$ and $\varepsilon$ ):
$$\|f\|_{C_{\delta}^{0}}=\sup _{X} \rho^{\delta}|f|, \quad\|f\|_{C_{\delta}^{0, \alpha}}=\|f\|_{C_{\delta}^{0}}+\left[\rho^{\delta} f\right]_{\alpha}$$
where the semi-norm $[f]_{\alpha}$ is also weighted:
$$[f]_{\alpha}=\sup _{d_{g_{\beta, \varepsilon}}(x, y)<\operatorname{inj}} \min \left\{\rho^{\alpha}(x), \rho^{\alpha}(y)\right\} \cdot \frac{|f(x)-f(y)|}{d_{g_{\beta, \varepsilon}}(x, y)^{\alpha}} .$$
As for the $C^{2, \alpha}$ norm, since we will in general be working with cone angles $2 \pi \beta>$ $\pi$, we cannot require to control all the second order derivatives but rather only the mixed ones (normal to $D$ ), as observed by Donaldson [Don12]. Therefore we need to distinguish two regions $X=A \cup B$ where $A=(r \geqslant 1)$ and $B=(r \leqslant 1)$. On $B$, i.e. away from $D$, we set
$$\|f\|_{C_{\delta}^{2, \alpha}(B)}=\sup \sum_{0 \leq j \leq 2} \rho^{\delta+j}\left|\nabla^{j} f\right|_{g_{\beta, \varepsilon}}+\left[\rho^{\delta+2} \nabla^{2} f\right]_{\alpha} .$$

Now we need to define $\|f\|_{C_{\delta}^{2, \alpha}(A)}$; on $A$ the weight function is essentially one so it is irrelevant. The function $\left.\mathrm{Y}^{*} f\right|_{A}$ lives on a smaller and smaller neighborhood of the zero section in $\Delta_{L}$ as $\varepsilon$ decreases to 0 . Consider the dilation $\lambda_{\varepsilon}: L \rightarrow L,(x, v) \mapsto\left(x, \varepsilon^{\frac{1}{2 \beta *}} v\right)$. Then $f_{\varepsilon}:=\left.\lambda_{\varepsilon}^{*} Y^{*} f\right|_{A}$ lives on $\Delta_{L}$, and we are going to set
$$\|f\|_{C^{2, \alpha}(A)}:=\left\|f_{\mathcal{E}}\right\|_{C^{2, \alpha}\left(\Delta_{L}\right)}$$
where the $C^{2, \alpha}\left(\Delta_{L}\right)$ norm is the one defined by Donaldson, whose construction we recall in the paragraph below. Finally, we set
$$\|f\|_{C_{\delta}^{2, \alpha}}=\|f\|_{C^{2, \alpha}(A)}+\|f\|_{C_{\delta}^{2, \alpha}(B)} .$$

In this paragraph, let $h$ he a function on $\Delta_{L}$. Let $V$ be a chart $V$ with a holomorphic system of coordinates $\left(z_{1}, \ldots, z_{n}\right)$ where the zero section $D$ is given by $\left(z_{1}=0\right)$; set $z^{\prime}=\left(z_{2}, \ldots, z_{n}\right)$. The flat cone Kähler metric is given by $d d^{c}\left(\left|z_{1}\right|^{2 \beta}+\left|z^{\prime}\right|^{2}\right)$ and the associated Riemannian metric is
$$\bar{g}_{\beta}:=\left(d r^{2}+\beta^{2} r^{2} d \theta^{2}\right)+g_{\mathbb{C}^{n-1}}$$
where $r:=\left|z_{1}\right|^{\beta}$ and $\theta:=\arg \left(z_{1}\right)$. We consider the derivatives
$$D_{1}:=\partial_{r}, D_{2}:=\frac{1}{\beta r} \partial_{\theta} \quad \text { and } \quad D_{2 j-1}=\partial_{x_{j}}, D_{2 j}=\partial_{y_{j}}$$
where $z_{j}=x_{j}+i y_{j}$ for $2 \leqslant j \leqslant n$. The $C^{0, \alpha}$ norm of $h$ is simply
$$\|h\|_{C^{0, \alpha}(V)}=\sup _{V}|h|+\sup _{x, y \in V} \frac{|h(x)-h(y)|}{d_{\bar{g}_{k}}(x, y)^{\alpha}},$$
and we define the $\mathcal{C}^{2, \alpha}$ norm of $h$ on $V$ as
$$\|h\|_{C^{2, \alpha}(V)}=\sup _{V}\left(|h|+\left|\nabla^{\bar{g}_{\beta}} h\right|\right)+\sum_{i=1}^{2 n} \sum_{j=3}^{2 n}\left\|D_{i} D_{j} h\right\|_{C^{0, \alpha}(V)}+\left\|\Delta_{\bar{g}_{\beta}} h\right\|_{C^{0, \alpha}(V)} .$$
Finally, one can cover $\Delta_{L}$ with finitely many coordinate charts $V_{1}, \ldots, V_{N}$, and we set $\|h\|_{C^{2, \alpha}\left(\Delta_{L}\right)}=\sum_{k=1}^{N}\|h\|_{C^{2, \alpha}\left(V_{k}\right)}$.

Proposition 7.1. Let $L_{\beta, \varepsilon}:=\Delta_{g_{\beta, \varepsilon}}+\mu_{\beta}$. Then there exists a constant $C>0$ independent of $\beta, \varepsilon$ such that for any $f \in C_{\delta}^{2, \alpha}(X)$, we have
$$\|f\|_{C_{\delta}^{2, \alpha}} \leqslant C\left(\|f\|_{C_{\delta}^{0}}+\left\|L_{\beta, \varepsilon} f\right\|_{C_{\delta+2}^{0, \alpha}}\right) .$$
Proof. We first look at the zone $A=(\rho \geqslant 1)$ and we need to bound $\|f\|_{C^{2, \alpha}(A)}$. Given the definition of the norms involved, it amounts to proving the equivalent Schauder estimate for the operator $\Delta_{g_{\beta}}+\mu_{\beta}$ on $\Delta_{L}$, uniformly in $\beta$. This has been proved for the flat cone metric (i.e. for $\Delta_{\bar{g}_{\beta}}+\mu_{\beta}$ ) in [Don12] for a given fixed $\beta$,
and the uniformity in the cone angle (even when $\beta \rightarrow 0$, which is irrelevant here though) has been proved in [BG22, Theorem 6.1]. It is classical (cf e.g. [BG22, Remark 6.8]) to reduce the estimate for the operator $\Delta_{g_{\beta}}+\mu_{\beta}$ to the one for the flat cone metric by proving that $g_{\beta}$ is $C^{\alpha}$-close to $\bar{g}_{\beta}$. This, in turn, follows from the explicit description of $\omega_{\beta}$ in (3.4) and the expansion (3.16) (use the relation $\rho=e^{\frac{1}{2} \beta\left(u+\phi_{h}\right)}$ where $\phi_{h}$ is a local weight of the hermitian metric $h$ on $L$ ).

Next, in the zone ( $1 \geqslant \rho \geqslant \frac{1}{2} r_{\varepsilon}$ ), one can use as before the diffeomorphism $\mathrm{Y}_{\varepsilon}$ and the problem is equivalent to that with the Calabi metric $d d^{c} \phi_{\beta, L}$ on a compact subset $K_{\varepsilon} \Subset L \backslash D$. Over $K_{\varepsilon}$, the metric is uniformly comparable to the cone metric (3.55), so weighted Schauder estimates follow.

In the zone ( $\rho \leqslant \frac{1}{2} \rho_{\varepsilon}$ ), we have $g_{\beta, \varepsilon}=\varepsilon g_{\mathrm{TY}}$. The Tian-Yau metric is asymptotically conical hence satisfies the desired Schauder estimate with weight function $R$. Since $\rho \approx \sqrt{\varepsilon} R$ globally on the zone ( $\rho \geqslant \frac{1}{2} \rho_{\varepsilon}$ ), the desired estimate follows from the classical one for the Tian-Yau metric by the definition of our norms. \(\square\)
7.3. Vector fields and eigenfunctions of the Laplacian on the cone $L$. We begin with the following elementary computation relating eigenfunctions of the Laplacian for $g_{D}$ and $g_{\beta}$.

Lemma 7.2. Let $g \in C^{\infty}(D)$ such that $\left(\Delta_{\omega_{D}}+1\right) g=0$. Define for $\beta \geqslant \beta_{*}$ the function $f_{\beta}=\phi_{\beta}^{\prime} g$ on an open subset of $L$. Then we have
$$\left(\Delta_{\omega_{\beta}}+\mu_{\beta}\right) f_{\beta}=0 .$$
Proof. We omit the index $\beta$ to lighten notation. Let $\psi=\psi(u)$ be a smooth function of $u$. We have
$$d d^{c}(\psi g)=g\left(\psi^{\prime \prime} d u \wedge d^{c} u-\frac{2 \psi^{\prime}}{\alpha-1} \omega_{D}\right)+\psi d d^{c} g .$$
Given (3.4), we deduce
$$\begin{aligned}
\Delta_{\omega_{\beta}}(\psi g) & =\frac{\psi^{\prime \prime}}{\phi^{\prime \prime}} g+(n-1) \frac{\psi^{\prime}}{\phi^{\prime}} g-(\alpha-1) \frac{\psi}{\phi^{\prime}} \Delta_{\omega_{D}} g \\
& =\left(\frac{\psi^{\prime \prime}}{\psi \phi^{\prime \prime}}+(n-1) \frac{\psi^{\prime}}{\psi \phi^{\prime}}+(\alpha-1) \frac{1}{\phi^{\prime}}\right) \psi g .
\end{aligned}$$
Now, (3.7) can be rewritten as
$$\log \phi^{\prime \prime}+(n-1) \log \phi^{\prime}+\mu \phi+(\alpha-1) u=0,$$
and after differentiation, we obtain
$$\frac{\phi^{\prime \prime \prime}}{\phi^{\prime \prime}}+(n-1) \frac{\phi^{\prime \prime}}{\phi^{\prime}}+\mu \phi^{\prime}+(\alpha-1)=0 .$$
Plugging $\psi:=\phi^{\prime}$ into (7.14) and using (7.15), we obtain
$$\Delta_{\omega_{\beta}}\left(\phi^{\prime} g\right)=-\mu \phi^{\prime} g$$
as announced. \(\square\)

Remark 7.3. The $\mathbb{C}^{*}$ action on $L$ yields another eigenvector of $\Delta_{\omega_{\beta}}$, which is $\phi_{\beta}^{\prime}+$ $\lambda_{\beta}$. More precisely, the computation above shows that we have $\left(\Delta_{\omega_{\beta}}+\mu_{\beta}\right)\left(\phi_{\beta}^{\prime}+\right.$ $\left.\lambda_{\beta}\right)=0$.
Definition 7.4. Let $\left(f_{1}, \ldots, f_{\ell}\right)$ be a basis of $\left\{f \in C^{\infty}(D) ;\left(\Delta_{g_{D}}+1\right) f=0\right\}$. We define $E \subset C^{0}(L)$ to be the finite dimensional real vector space
$$E:=\operatorname{Span}\left\{\phi_{\beta_{*}}^{\prime}+\lambda_{\beta_{*}}, \phi_{\beta_{*}}^{\prime} f_{1}, \ldots, \phi_{\beta_{*}}^{\prime} f_{\ell}\right\} .$$

Proposition 7.5. Let $h \in C^{\infty}(L \backslash D)$ be a solution of $\left(\Delta_{g_{\beta_{*}}}+\mu_{\beta_{*}}\right) h=0$ such that $\|h\|_{C_{\delta}^{2, \alpha}}<+\infty$ for some $\delta \in(0,1)$ small enough and let $v \in H^{0}\left(\bar{L}, T_{\bar{L}}(-\log D)\right)$. Then
\begin{itemize}
\item[(i)] The vector field $v_{h}:=\operatorname{grad}_{g_{\beta *}}^{1,0} h$ is holomorphic and tangent to $D$.
\item[(ii)] There exists a unique $h_{v}$ such that $v=\operatorname{grad}_{g_{\beta_{*}}}^{1,0} h_{v}$ and $\left(\Delta_{g_{\beta_{*}}}+\mu_{\beta_{*}}\right) h_{v}=0$. Moreover, $h_{v} \in E$.
\end{itemize}
The two constructions are inverse to each other, in the sense that $h_{v_{h}}=h$.
Proof. We start by proving the first assertion. It turns out that we'll need to refine the condition $h \in C_{\delta}^{2, \alpha}(L)$ in the following computations. This is the aim of the following

Claim 7.6. One has
$$\sup _{0<r<1}|\nabla h|_{g_{\beta *}}+r\left|\nabla^{2} h\right|_{g_{\beta *}}<+\infty,$$
where $r=e^{-\frac{1}{2} \beta_{*} u}$.
Proof of Claim 7.6. By Remark 7.3, $\phi_{\beta}^{\prime}+\lambda_{\beta}$ satisfies the same linear equation as $h$ and clearly it satisfies the bounds in the claim. Therefore, up to replacing $h$ with $h-\left(\phi_{\beta}^{\prime}+\lambda_{\beta}\right)$, one can assume that $h(0)=0$. Then the behaviour of $h$ near $r=0$
is governed by the first positive exceptional weight $\delta_{1}$ of $\Delta$, which satisfies $\delta_{1}>1$ (see for example [CH13, Remark 2.10]). It follows that $h \in C_{\delta^{\prime}}^{2, \alpha}$ for any $\delta^{\prime}<\delta_{1}$ and in particular for $\delta^{\prime}=1$. So $\nabla h \in C_{0}^{1, \alpha}$ which gives the claim. \(\square\)

To lighten notation, we will drop the index $\beta_{*}$ in the following and simply write $v$ for $v_{h}$. Since Ric $\omega=\mu \omega$, a classical computation shows that
$$\bar{\partial}^{*} \bar{\partial} v=\operatorname{grad}^{1,0}\left[\left(\Delta_{g}+\mu\right) h\right]=0 .$$
Moreover, we have the identity
$$\left(\langle\bar{\partial} v, \bar{\partial} v\rangle_{g}-\left\langle\bar{\partial}^{*} \bar{\partial} v, v\right\rangle_{g}\right) d \operatorname{vol}_{g}=d\left(\langle * \bar{\partial} v, v\rangle_{g}\right),$$
where $*: \Omega_{X}^{0,1} \otimes T_{X}^{1,0} \rightarrow \Omega_{X}^{n, n-1} \otimes T_{X}^{1,0}$ is the Hodge star operator.
For $\varepsilon>0$, we set $L_{\varepsilon}:=\{\log \varepsilon \leqslant u \leqslant-\log \varepsilon\}$. Integrating (7.17) over $L_{\varepsilon}$ and using (7.16) yields
$$\begin{aligned}
\int_{L_{\varepsilon}}\|\bar{\partial} v\|^{2} d \operatorname{vol}_{g} & =\int_{\partial L_{\varepsilon}}\langle * \bar{\partial} v, v\rangle_{g} \\
& =\int_{u=\log \varepsilon}\langle * \bar{\partial} v, v\rangle_{g}+\int_{u=-\log \varepsilon}\langle * \bar{\partial} v, v\rangle_{g} \\
& =: I(\varepsilon)+J(\varepsilon)
\end{aligned}$$
and we now have to show that $I(\varepsilon)$ and $J(\varepsilon)$ go to zero when $\varepsilon \rightarrow 0$. Since $g$ is has conic singularities along $D$ and $h$ belongs do Donaldson's $C^{2, \alpha, \beta_{*}}$ space, the claim for $I$ has already been showed in the proof of [Don12, Proposition 8]. So we now focus on $J(\varepsilon)$. At infinity in $L$, recall from (3.51) that we have
$$g \approx d r^{2}+r^{2}\left(\eta^{2}+g_{D}\right)$$
where $r=e^{-\frac{1}{2} \beta_{*} u}$. Next, we have
$$\begin{aligned}
\|\langle * \bar{\partial} v, v\rangle\|_{g} & \leqslant\|\bar{\partial} v\|_{g} \cdot\|v\|_{g} \\
& \leqslant\left\|\nabla^{0,2} h\right\|_{g} \cdot\|\nabla h\|_{g} \\
& \leqslant r^{-1}
\end{aligned}$$
by Claim 7.6. On $\{u=-\log \varepsilon\}$, we have $r \simeq r_{\varepsilon}:=\varepsilon^{\frac{\beta_{*}}{2}}$ hence
$$|J(\varepsilon)| \lessapprox r_{\varepsilon}^{2 n-2}$$
goes to zero as desired.
We now move on to proving the second assertion. Let $\xi$ be the radial holomorphic vector field. By Lemma 4.1, we can decompose $v$ as
$$v=a \xi+w$$
where $a \in \mathbb{C}$ and $w$ is induced by vector field $v_{D} \in H^{0}\left(D, T_{D}\right)$; of course we have $\left.w\right|_{D}=v_{D}$. We want to find a function $h$ such that $v=\operatorname{grad}^{1,0} h$ or, equivalently, $i_{v} \omega=\bar{\partial} h$.

Thanks to Remark 7.3, we have $i_{\xi} \omega=\bar{\partial} \phi^{\prime}$. Therefore, it is enough to show the claim when $a=0$, i.e. when $v=w$ is induced by a vector field $v_{D}$ on $D$. By the classical case, one can write $i_{v_{D}} \omega_{D}=\bar{\partial} h_{D}$ for some smooth function $h_{D}$ on $D$ satisfying $\left(\Delta_{g_{D}}+1\right)\left(h_{D}\right)=0$. Set $h:=-\frac{1}{\alpha-1} \phi^{\prime} h_{D}$; since $\left(\Delta_{g_{\beta *}}+\mu_{\beta_{*}}\right)(h)=0$ by Lemma 7.2, all we have left to prove is
$$i_{v} \omega=\bar{\partial} h .$$
In order to prove (7.18), let $x \in D$ and let $\left(w_{1}, \ldots, w_{n-1}\right)$ be a system of coordinates defined on a open set $U \subset D$. On $U, L=-\frac{1}{\alpha-1} K_{D}$ is trivialized by $\sigma:=\left(d w_{1} \wedge \ldots \wedge d w_{n-1}\right)^{\otimes-\frac{1}{\alpha-1}}$ and we get another coordinate $z$ on $p^{-1}(U)$ given by $v=z \sigma$ if $v \in L_{x}$. On $U$, one can write $v_{D}=\sum a_{i} \frac{\partial}{\partial w_{i}}$. We have $L_{v_{D}} \sigma=\frac{\operatorname{div}\left(v_{D}\right)}{\alpha-1} \cdot \sigma$ so that the lift of $v_{D}$ to $p^{-1}(U)$ is
$$v=\frac{\operatorname{div}\left(v_{D}\right)}{\alpha-1} \cdot z \frac{\partial}{\partial z}+\sum_{i=1}^{n-1} a_{i} \frac{\partial}{\partial w_{i}} .$$
At $x$, we can always assume up to doing a linear change of coordinates that the local weight $\varphi$ of the hermitian metric on $-K_{D}$ satisfies $\varphi(x)=0$ and $d \varphi(x)=0$ so that $\partial u=\frac{d z}{z}$ at $x$. In particular, we have at any point in $p^{-1}(x)$
$$\omega=\phi^{\prime \prime} i \frac{d z}{z} \wedge \frac{d \bar{z}}{\bar{z}}-\frac{\phi^{\prime}}{\alpha-1} \omega_{D}, \quad \text { and } \quad \bar{\partial}\left(\phi^{\prime} h_{D}\right)=\phi^{\prime \prime} h_{D} \frac{d \bar{z}}{\bar{z}}+\phi^{\prime} \bar{\partial} h_{D} .$$
Since $i_{v_{D}} \omega_{D}=\bar{\partial} h_{D}$, we have $\operatorname{div}\left(v_{D}\right)=-i \Delta_{g_{D}} h_{D}=i h_{D}$. This implies that
$$\begin{aligned}
i_{v} \omega & =\frac{\operatorname{div}\left(v_{D}\right)}{\alpha-1} \phi^{\prime \prime} i \frac{d \bar{z}}{\bar{z}}-\frac{\phi^{\prime}}{\alpha-1} i_{v_{D}} \omega_{D} \\
& =\frac{-1}{\alpha-1}\left(\phi^{\prime \prime} h_{D} \frac{d \bar{z}}{\bar{z}}+\phi^{\prime} \bar{\partial} h_{D}\right) \\
& =\bar{\partial} h
\end{aligned}$$
which shows (7.18) at any point in the fiber of $x$, hence everywhere on $L$.
As for the last assertion, since $h_{v_{h}}$ and $h$ satisfy $i_{v_{h}} \omega=\bar{\partial} h=\bar{\partial} h_{v_{h}}$, we have that $h-h_{v_{h}}$ is constant, hence zero since it lies in the kernel of $\Delta_{g}+\mu$. \(\square\)
7.4. Reduction to a one-dimensional problem. Let $G_{D}=\operatorname{Isom}^{\circ}\left(D, \omega_{D}\right)$ be the connected component of the group of holomorphic isometries of the Kähler-Einstein manifold $\left(D, \omega_{D}\right)$. By Matsushima theorem [Mat57], $G_{D}$ is a compact connected Lie group such that $G_{D}^{\mathrm{C}}=\operatorname{Aut}^{\circ}(D)$.

From now on, we assume that the restriction morphism (4.2) is surjective. Thanks to Lemma 4.2, there exists a surjective, finite étale map $G \rightarrow G_{D}$ of algebraic groups where $G$ is a (compact) subgroup of $\operatorname{Aut}^{\circ}(X, D)$. We define the space of $G$-invariant functions $C_{\delta}^{2, \alpha}(X)^{G}:=\left\{f \in C_{\delta}^{2, \alpha}(X) ; \forall \sigma \in G, \sigma^{*} f=f\right\}$.

Let $\left(h_{1}, \ldots, h_{\ell}\right)$ be an orthonormal basis of $\left\{h \in C^{\infty}(D) ;\left(\Delta_{g_{D}}+1\right) h=0\right\}$, and let $\xi_{i}:=\operatorname{grad}_{g_{D}}^{1,0} h_{i}$ be the corresponding holomorphic vector field on $D$. By our assumption, there exists a unique vector field on $X$ tangent to $D$ extending $\xi_{i}$, cf proof of Lemma 4.2. We will abusively still denote it by $\xi_{i}$.

Next, recall from Remark 7.3 that $\phi_{\beta}^{\prime}+\lambda_{\beta}$ is the potential of the scaling $\mathbb{C}^{*}$ action on $\left(L, \omega_{\beta, L}\right)$. Borrowing the notation from the beginning of § 7, we set
$$\tau=\tau_{\beta, \varepsilon}:=\chi_{\varepsilon}\left(\mathrm{Y}_{\varepsilon}\right)_{*}\left(\phi_{\beta, L}^{\prime}\right)+\lambda_{\beta}$$
which is well-defined globally on $X$, and satisfies $\left\|\tau_{\beta, \varepsilon}\right\|_{C_{\delta}^{0}}=\alpha(\alpha+\lambda)$. It is asymptotical in the kernel of $L_{\beta, \mathcal{E}}$ in the following sense

Lemma 7.7. Let $f \in C_{\delta}^{2, \alpha}(X)$ and let $\delta \in(0,2 n)$, then we have
$$\left\langle L_{\beta, \varepsilon} f, \tau_{\beta, \varepsilon}\right\rangle=O\left(r_{\varepsilon}^{2 n-\delta}\|f\|_{C_{\delta}^{0}}\right)$$
If, moreover, one has $\delta<n-2$ and $\left|d^{c} g\right|_{\omega_{\beta, \varepsilon}} \leqslant 1$ then we have
$$\left\langle Q_{\beta, \varepsilon}(f), \tau_{\beta, \varepsilon}\right\rangle= \begin{cases}O\left(\|f\|_{C_{\delta}^{2, \alpha}}^{2}\right) & \text { if } n>2, \\ O\left(\varepsilon^{-\delta}\|f\|_{C_{\delta}^{2, \alpha}}^{2}\right) & \text { if } n=2,\end{cases}$$
where the $O()$ are uniform in $f, g, \beta, \varepsilon$.
Proof. Let us start with the first estimate. On $\left(\rho \geqslant 2 \rho_{\varepsilon}\right)$, we have $L_{\beta, \varepsilon} \tau_{\beta, \varepsilon} \equiv 0$ thanks to Remark 7.3.

On $\left(\rho \leqslant \frac{1}{2} \rho_{\varepsilon}\right)$, we have $L_{\beta, \varepsilon} \tau_{\beta, \varepsilon}=\mu_{\beta} \lambda_{\beta}=O(1)$. Since $f \leqslant \rho^{-\delta}\|f\|_{C_{\delta}^{0}}$ and $\int_{\rho \leqslant \frac{1}{2} \rho_{\varepsilon}} \rho^{-\delta} d \operatorname{vol}_{\varepsilon \mathrm{g}_{\mathrm{TY}, \varepsilon}} \approx \int_{\sqrt{\varepsilon}}^{\frac{1}{2} \rho_{\varepsilon}} t^{2 n-1-\delta} d t=O\left(\rho_{\varepsilon}^{2 n-\delta}\right)$, we are done.

It remains to analyze the contribution of the gluing zone $\left(\frac{1}{2} \rho_{\varepsilon} \leqslant \rho \leqslant 2 \rho_{\varepsilon}\right)$. In that zone, we know from (3.27) and (3.8) that $\phi_{\beta, \varepsilon, L}^{(k)}=O\left(r^{2}\right)$ for any $k \geqslant 0$, where the derivative is to take with respect to $u$ and $r=e^{-\frac{1}{2} \beta_{*} u} \approx \rho$. In particular, $d \phi_{\beta, \varepsilon, L}^{\prime}=O\left(r^{2}\right) d u$ and $d d^{c} \phi_{\beta, L, \varepsilon}^{\prime}=O\left(r^{2}\right) \cdot\left(d u \wedge d^{c} u+\omega_{D}\right)$. Since $g_{\beta, \varepsilon, L}$ is asymptotic to $d r^{2}+r^{2} g_{D}$, we find $\left|\nabla \phi_{\beta, \varepsilon, L}^{\prime}\right|=O(r)$ and $\left|\Delta \phi_{\beta, \varepsilon, L}^{\prime}\right|=O(1)$. Finally, we have $\left|\nabla^{k} \chi_{\varepsilon}\right|=O\left(r_{\varepsilon}^{-k}\right)$ so that in the end, $\left|L_{\beta, \varepsilon} \tau_{\beta, \varepsilon}\right|=O(1)$. One can now conclude with the same arguments as for the previous zone.

Let us now consider the integral involving $Q_{\beta, \varepsilon}$; unlike the previous one we will need to look at the normal bundle zone as well. From (7.9), we have $|Q(f)| \leqslant \rho^{-2 \delta-4}\|f\|_{C_{\delta}^{2, \alpha}}^{2}$ pointwise. The desired estimate now follows from the same computations as in the previous step combined with the fact that the integral $\int_{X} \rho^{-\kappa} \omega_{\beta, \varepsilon}^{n}$ is uniformly bounded when $\kappa<2 n$ while $\int_{\rho \leqslant 2 \rho_{\varepsilon}} \rho^{-2 \delta} \omega_{\beta, \varepsilon}^{2}=$ $O\left(\varepsilon^{-\delta}\right)$ when $n=2$. \(\square\)

Finally, we introduce
$$C_{\delta}^{2, \alpha}(X)^{\perp}:=\left\{f \in C_{\delta}^{2, \alpha}(X) ; \int_{X} f \tau_{\beta, \varepsilon} d \operatorname{vol}_{g_{\beta, \varepsilon}}=0\right\},$$
set $C_{\delta}^{2, \alpha}(X)^{G, \perp}:=C_{\delta}^{2, \alpha}(X)^{G} \cap C_{\delta}^{2, \alpha}(X)^{\perp}$ and write ${ }^{\perp}: C_{\delta}^{2, \alpha}(X) \rightarrow C_{\delta}^{2, \alpha}(X)^{\perp}$ the orthogonal projection, i.e. $f^{\perp}=f-\frac{\left\langle f, \tau_{\beta, \varepsilon}\right\rangle}{\left|\tau_{\beta, \varepsilon}\right|^{2}} \cdot \tau_{\beta, \varepsilon}$.
Proposition 7.8. Fix $0<\delta<1$. There is a constant $C>0$ independent of $\beta, \varepsilon$ (with $\left.\left|\beta-\beta_{*}\right|+\varepsilon \ll 1\right)$ such that for every $f \in C_{\delta}^{2, \alpha}(X)^{G, \perp}$, we have
$$\|f\|_{C_{\delta}^{2, \alpha}} \leqslant C\left\|\left(L_{\beta, \varepsilon} f\right)^{\perp}\right\|_{C_{\delta+2}^{0, \alpha}} .$$
Proof. We argue by contradiction. We can extract a sequence $\left(\beta_{j}, \varepsilon_{j}\right) \rightarrow 0$ and find functions $f_{j} \in C_{\delta}^{2, \alpha}(X)^{G} \cap C_{\delta}^{2, \alpha}(X)^{\perp}$ such that $\left\|f_{j}\right\|_{C_{\delta}^{2, \alpha}}=1$ but satisfying $\left\|\left(L_{\beta, \varepsilon} f_{j}\right)^{\perp}\right\|_{C_{\delta+2}^{0, \alpha}} \rightarrow 0$ when $j \rightarrow+\infty$.

Thanks to the first item in Lemma 7.7, we have $\left\langle L_{\beta, \varepsilon} f_{j}, \tau_{\beta, \varepsilon}\right\rangle \rightarrow 0$, hence $\left\|L_{\beta, \varepsilon} f_{j}\right\|_{C_{\delta+2}^{0, \alpha}} \rightarrow 0$ since $L_{\beta, \varepsilon} f_{j}=\left(L_{\beta, \varepsilon} f_{j}\right)^{\perp}+\frac{\left\langle f_{j}, L \tau_{\beta, \varepsilon}\right\rangle}{\left|\tau_{\beta, \varepsilon}\right|} \tau_{\beta, \varepsilon}$. By Proposition 7.1, $\|f\|_{C_{\delta}^{0}}$
does not converge to zero. For simplicity, one will assume that $\|f\|_{C_{\delta}^{0}}=1$ and we choose $x_{j} \in X$ such that $r^{\delta}\left|f_{j}\right|\left(x_{j}\right)=1$.

Case 1. $\rho\left(x_{j}\right)>\eta>0$.
Using $\mathrm{Y}_{\varepsilon}$, one can view the $f_{j}$ as functions on larger and larger open subsets of $L$, with controlled $C^{2, \alpha}$ bound with respect to $g_{\beta, L}$. Since $\rho\left(x_{j}\right) \geqslant \eta$, the points $x_{j}$ belong to a compact set of $L$ and one can assume that $\left(x_{j}\right)$ converges to $x_{\infty} \in L$. Thanks to Arzela-Ascoli theorem, one can extract a limit function $f \in C_{\delta}^{2, \alpha}(L)$ with respect to the cone metric $g_{\beta_{*}}$ satisfying $f\left(x_{\infty}\right) \neq 0$ and $\left(\Delta_{g_{\beta_{*}}}+\mu_{\beta_{*}}\right)(f)=0$. From Proposition 7.5, it follows that there are constants $a_{0}, \ldots, a_{\ell} \in \mathbb{R}$ such that
$$f=a_{0}\left(\phi_{\beta_{*}}^{\prime}+\lambda_{\beta_{*}}\right)+\sum_{i=1}^{\ell} a_{i} h_{i} .$$

Since $f_{j}$ is $G$-invariant, we have $L_{\xi_{i}} f_{j}=0$ on $X$ for any $i=1, \ldots, \ell$. Since $\xi_{i}$ is tangent to $D$, one can restrict the previous identity to $D$ and let $j \rightarrow+\infty$. It yields $L_{\xi_{i}}\left(\left.f\right|_{D}\right)=0$ on $D$. Since $\xi_{i}=\operatorname{grad}^{1,0} h_{i}$, we have
$$\int_{D} L_{\xi_{i}} f d \operatorname{vol}_{g_{D}}=\sum_{k=1}^{\ell} a_{k}\left\langle\operatorname{grad}^{1,0} h_{i}, \operatorname{grad}^{1,0} h_{k}\right\rangle=-\sum_{k=1}^{\ell} a_{k}\left\langle h_{i}, \Delta h_{k}\right\rangle=a_{i}$$
since $\Delta h_{k}=-h_{k}$. In particular, we get $a_{i}=0$ for all $i=1, \ldots, \ell$ so that $f=$ $a_{0}\left(\phi_{\beta_{*}}^{\prime}+\lambda_{\beta_{*}}\right)$.

Next, the same computations as in the proof of Lemma 7.19 show that
$$\left|\int_{r \leqslant 2 r_{\varepsilon}} f_{j} \tau_{\beta_{j}, \varepsilon_{j}} d \operatorname{vol}_{g_{\beta_{j}, \varepsilon_{j}}}\right| \leqslant C \int_{r \leqslant 2 r_{\varepsilon}} r^{-\delta} d \operatorname{vol}_{g_{\beta_{j}, \varepsilon_{j}}}=O\left(r_{\varepsilon}^{2 n-\delta}\right) .$$
Since $f_{j}$ is orthogonal to $\tau_{\beta_{j}, \varepsilon_{j}}$ it follows from the dominated convergence theorem that $\int_{L} f\left(\phi_{\beta_{*}}^{\prime}+\lambda_{\beta_{*}}\right) d_{\operatorname{vol}_{\beta_{\beta_{*}}}}=0$. Therefore, we get $a_{0}=0$, hence $f \equiv 0$, a contradiction.

Case 2. $1 \gg \rho\left(x_{j}\right) \gg \sqrt{\varepsilon}$. The set $\mathrm{Y}_{\varepsilon}^{-1}\left(U_{L}\right)$ is of the form $\{+\infty \geqslant r \geqslant \sqrt{\varepsilon}\}$ with the notation of (3.34). The set $\mathrm{Y}_{\varepsilon}^{-1}(1 \gg \rho \gg \sqrt{\varepsilon})$ in $L$ is simply ( $1 \gg$ $r \gg \sqrt{\varepsilon}$ ). We claim that in that zone, $\mathrm{Y}_{\varepsilon}^{*} g_{\beta, \varepsilon}$ is asymptotic to $g_{\mathrm{TY}, L}$ whose Kähler form is $\omega_{\mathrm{TY}, L}=d d^{c} \frac{r^{2}}{4}$. Let us briefly justify the claim in each of the three relevant zones. In the Tian-Yau part (i.e. when $g_{\beta, \varepsilon}=\varepsilon^{2} g_{\mathrm{TY}, \varepsilon}$ ), it follows from Theorem 6.1 since the first order asymptotics of the formal perturbation are the same as the
ones for the genuine Tian-Yau metric by Proposition 6.4. On the normal bundle part (i.e. before the gluing) the claim follows from (3.48) since $d d^{c} \phi_{\beta_{*}, L}$ has the same asymptotic cone as $\omega_{\mathrm{TY}, L}$. Finally, in the gluing zone, it follows from (8.9) below.

Now, set $r_{j}:=\rho\left(x_{j}\right), \hat{r}:=\frac{r}{r_{j}}$ and consider the function $\hat{f}_{j}:=\mathrm{Y}_{\varepsilon}^{*}\left(r_{j}^{\delta} f_{j} \mid U_{L}\right)$ on $\left(\frac{1}{r_{j}} \gg \hat{r} \gg \frac{\sqrt{\varepsilon}}{r_{j}}\right)$. It is bounded in the usual weighted $C^{2, \alpha}$ norm with respect to the metric $\mathrm{Y}_{\varepsilon}^{*}\left(r_{j}^{-2} g_{\beta, \varepsilon}\right)$ (whose Kähler form is asymptotic to $d d^{\hat{r}^{2}} \frac{\hat{r}^{2}}{4}$ ) and the weight $\hat{r}$. Moreover, it satisfies $\Delta_{\mathrm{Y}_{\varepsilon}^{*}\left(r_{j}^{-2} g_{\beta_{\beta, \varepsilon}}\right)} \hat{f}_{j}+r_{j}^{2} \mu_{\beta} \hat{f}_{j} \rightarrow 0$ in $C_{\text {loc }}^{\alpha}\left(L^{\times}\right)$in the usual sense. By Arzela-Ascoli, $\hat{f}_{j}$ converges (up to extracting a subsequence) in the usual $C_{\text {loc }}^{2}$ topology on $L^{\times}$to a non-zero function $f$ satisfying
$$\Delta_{g_{\mathrm{TY}, L}} f=0 \quad \text { and } \quad \sup _{L^{\times}} r^{\delta}|f|<\infty .$$
Let $\varepsilon>0$; since $\delta \in(0,1)$ and $n>1$, the function $\pm f-\frac{\varepsilon}{r^{2 n-2}}$ is harmonic and tends to $-\infty$ near the apex $r=0$ and 0 when $r \rightarrow+\infty$. By the maximum principle, it is non-positive hence $\pm f \leqslant \frac{\varepsilon}{r^{2 n-2}}$. Since this holds for any $\varepsilon>0$, we infer that $f \equiv 0$, hence the desired contradiction.

Case 3. $\rho\left(x_{j}\right)=O(\sqrt{\varepsilon})$.
In this case, $x_{j}$ belongs to a fixed compact subset of $X \backslash D$ and $\rho\left(x_{j}\right) \approx \sqrt{\varepsilon_{j}}$. Thanks to Arzela-Ascoli theorem, a diagonal extraction argument allows one to find a subsequential non-zero limit $f$ of the sequence of functions $\left(\varepsilon_{j}^{\frac{\delta}{2}} f_{j}\right)$ on $X \backslash D$ for the $C_{\text {loc }}^{2, \alpha}$ topology. Moreover, $f$ satisfies $\sup _{X \backslash D} \rho^{\delta}|f|<+\infty$ as well as $\Delta_{g_{\mathrm{TY}}} f=0$. By the maximum principle, we must have $f \equiv 0$, a contradiction. \(\square\)