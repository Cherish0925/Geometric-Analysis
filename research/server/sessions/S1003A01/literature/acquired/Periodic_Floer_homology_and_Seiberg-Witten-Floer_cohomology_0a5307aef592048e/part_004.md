---
retention_scope: session
part: 4
total_parts: 4
---

[Part 4/4 of: Periodic Floer homology and Seiberg-Witten-Floer cohomology]

Lemma 5.11. Given $\mathcal{K} \geq 1$, there exists $\kappa \geq 1$ with the following significance: Suppose that $r \geq \kappa$, and that $(A, \psi=(\alpha, \beta))$ is an instanton solution to (4.4). Fix $s_{0} \in \mathbb{R}$ and $R \geq 1$; and suppose that
$$\sup _{s \in\left[s_{0}-R-3, s_{0}+R+3\right]} \underline{\mathrm{M}}(s) \leq \mathcal{K} .$$
Then
$$\begin{aligned}
& \left|\frac{\partial A}{\partial s}+B_{A}\right| \leq r\left(1-|\alpha|^{2}\right)+\kappa, \\
& \left|\frac{\partial A}{\partial s}-B_{A}\right| \leq r\left(1-|\alpha|^{2}\right)+\kappa
\end{aligned}$$
at all points in $\left[s_{0}-R, s_{0}+R\right] \times M$.
Proof. Copy the proof of Lemma 3.9 in [T4] using Lemmas 5.2, 5.7-5.9 to replace their [T4] analogs.

Arguments from [T4] refer to a connections on the pull-back of $E$ over $\mathbb{R} \times M$ that are denoted by $\hat{A}$. Each version of $\hat{A}$ differs from $A$ where $|\alpha|$ is near to 1 . Any given version is defined from a specified function $\wp:[0, \infty) \rightarrow$
$[0, \infty)$ which is a non-decreasing function that obeys $\wp(x)=x$ for $x$ near zero and $\wp(1)=1$. With $\wp$ in hand, set
$$\hat{A}=A-\frac{1}{2} \wp\left(|\alpha|^{2}\right)|\alpha|^{-2}\left(\bar{\alpha} \nabla_{A} \alpha-\alpha \nabla_{A} \bar{\alpha}\right) .$$

Here, and as previously, $\nabla_{A}$ denotes the covariant on $\mathbb{R} \times M$ as defined by $A$. The curvature, $F_{\hat{A}}$, of this connection is
$$F_{\hat{A}}=(1-\wp) F_{A}-\wp^{\prime} \nabla_{A} \bar{\alpha} \wedge \nabla_{A} \alpha .$$

If the assumptions of Lemma 5.10 hold, then
$$\left|F_{\hat{A}}\right| \leq c_{0}\left(r^{-1}+r \mathrm{e}^{-\sqrt{r} \operatorname{dist}\left(\cdot, X_{*}\right) / \kappa}\right)$$
on the whole of $\mathbb{R} \times M$. \(\square\)
5.7. Behavior near $\mathbb{R} \times \gamma$ when $\gamma$ is elliptic. The following is the analog here of Lemma 3.11 in [T4]:

Lemma 5.12. Fix a positive real number $L$. Then there exists a constant $\kappa>1$ depending on $L$, with the following significance: For any $r \geq \kappa$ and any solution $\mathfrak{d}=(A, \psi)$ to the $r$ 's version of instanton equation (4.4) satisfying (5.8), and for any elliptic periodic orbit $\gamma$ with tubular neighborhood map as described by (4.1), one has:
$$|\beta| \leq \kappa r^{-1}, \quad\left|\nabla_{A} \beta\right| \leq \kappa r^{-1 / 2}$$
at all points in $\mathbb{R} \times M$ with distance $\kappa^{-1}$ or less from $\mathbb{R} \times \gamma$.
Proof. Copy the proof of Lemma 3.11 in [T4]. \(\square\)

\section*{6. Generalizing to the non-monotone case}

In the non-monotone case of either the Periodic Floer homology or Seiberg-Witten-Floer cohomology, the definition of the Floer (co)homology in Section 1.1 or 1.2 no longer works, because the moduli space $\mathcal{M}_{1}\left(\Theta_{+}, \Theta_{-}\right)$or $\mathcal{M}_{1}\left(\mathfrak{c}_{-}, \mathfrak{c}_{+}\right)$used to define the differential fails to be compact. To make sense of the infinite sum in (1.9) or (1.16), the standard solution from the Floer theory literature is to work with Novikov coefficients. This is done in the Seiberg-Witten context in Chapter 30 in [KM]. We shall follow the formulation of Kronheimer and Mrowka, with notation and terminology modified so as to better accommodate both versions of Floer (co)homologies under discussion in one common framework. By way of a parenthetical remark, the formulation used in [T5] for embedded contact homology and Seiberg-Witten-Floer cohomology with group ring coefficients can be modified so as to apply in the present context with Novikov coefficients.
6.1. Local coefficients. We shall use the term "local system" in the following more general sense: In place of topological spaces, consider data sets of the following type.

Definition 6.1. A fundamental triple consists of:
\begin{itemize}
\item[-] a category $\mathfrak{G}$;
\item[-] a groupoid $\underline{\mathfrak{G}}$ with the same objects as $\mathfrak{G}$, and such that for every pair $a, b \in O b(\mathfrak{G})$, the set of morphisms $\mathscr{M o r}(\underline{\mathfrak{G}} ; a, b)$ in $\underline{\mathfrak{G}}$ from $a$ to $b$ has countably many elements;
\item[-] a functor $\pi_{\mathfrak{G}}$ from the former to the latter, which identifies the objects in both categories.
\end{itemize}

The model example. Take $\mathfrak{G}$ to be the category of points and paths in a topological space of countable $\pi_{1}$; let $\underline{\mathfrak{G}}$ be the fundamental groupoid of this space, and $\pi_{\mathfrak{G}}$ defined by taking the relative homotopy class.

Definition 6.2. Let $R$ be a commutative ring, and let $\operatorname{Mod}_{R}$ denote the category of $R$-modules. Given a fundamental triple $\pi_{\mathfrak{G}}: \mathfrak{G} \rightarrow \underline{\mathfrak{G}}$, we call a functor $\Lambda$ from $\underline{\mathfrak{G}}$ to $\operatorname{Mod}_{R}$ a local system of $R$-modules on $\mathfrak{G}$.

Definition 6.3. Let $R$ be a ring such that $-1 \neq 1$ in $R$. Let $\iota$ denote the generator of $\mathbb{Z} / 2 \mathbb{Z}$. An orientation functor of a category $\mathfrak{C}$ is a composition $\mathcal{R} \circ H$, where $H$ is a functor from $\mathfrak{C}$ to the category of $\mathbb{Z} / 2 \mathbb{Z}$-torsors, and $\mathcal{R}$ is the functor from the latter category to $\operatorname{Mod}_{R[\mathbb{Z} / 2 \mathbb{Z}]}$, which associated to a $\mathbb{Z} / 2 \mathbb{Z}$-torsor $Z$ the $R[\mathbb{Z} / 2 \mathbb{Z}]$-module $R[Z] /(1+\iota) R[Z]$.

An orientation local system $O$ of $\mathfrak{G}$ is a orientation functor $\mathcal{R} \circ H$ which is also a local system. When an element $u_{a} \in H(a)$ is chosen for each object $a$ of $\mathfrak{G}, \mathcal{O}(h)$ may be identified with an element in \{1, -1\} for each morphism $h$ in $\mathfrak{G}$. The fundamental triple is said to be orientable if it is possible to make such a system of choices $\left\{u_{a}\right\}_{a \in O b(\mathfrak{G})}$ such that for any $a, b \in O 6(\mathfrak{G})$, $H(h) u_{a}=u_{b}$ for all morphisms $h \in \operatorname{Mor}(\underline{\mathfrak{G}})$ from $a$ to $b$. Such a choice is said to be an orientation.
6.1.1. Floer theory package. Denote by $G_{\bullet}$ the groupoid of a single object ●, with $G$ as its set of morphisms.

A Floer theory in principle comes equipped with the following package:
[F1] a fundamental triple $\left\{\pi_{\mathfrak{G}}: \mathfrak{G} \rightarrow \underline{\mathfrak{G}}\right\}$,
[F2] a subset of $O b(\mathfrak{G})$ consisting of "regular" elements; denote the associated subcategories of $\mathfrak{G}$ and $\underline{\mathfrak{G}}$ by $\mathfrak{G}^{\text {reg }}$ and $\underline{\mathfrak{G}}^{\text {reg }}$, respectively;
[F3] a functor $\mathcal{S}$ from $\mathcal{G}^{\text {reg }}$ to $\mathbb{Z}_{\bullet}$, sending all objects to • This $\mathcal{S}$ factors as $\underline{\mathcal{S}} \circ \pi_{\mathfrak{G}}$. This is to define the notion of "spectral flow" or "relative $\mathbb{Z}$-grading,"
[F4] a parameter space $\mathcal{P}$ for the "flow equation" in the theory (such as of perturbations, metrics), so that corresponding to each $\mu \in \mathcal{P}$, there
\begin{itemize}
\item[] is a functor $\mathcal{E}_{\mu}$ from $\mathfrak{G}$ to $\mathbb{R}_{\bullet}$, sending all objects to • Each $\mathcal{E}_{\mu}$ factors as $\underline{\mathcal{E}}_{\mu} \circ \pi_{\mathfrak{G}}$. These are to be understood as notions of "action".
\item[] [F5] a subcategory $\mathfrak{C}_{\mu}$ of $\mathfrak{G}^{\text {reg }}$ defined for elements $\mu$ in a subset $\mathcal{P}^{\text {gen }} \subset \mathcal{P}$ consisting of "generic" elements, such that both $O b\left(\mathfrak{C}_{\mu}\right)$ and the set $\operatorname{Mor}_{1}\left(\mathfrak{C}_{\mu}\right):=\left\{z \mid z \in \operatorname{Mor}\left(\mathfrak{C}_{\mu}\right), \mathcal{S}(z)=1\right\}$ consist of countably many elements. Intuitively, $\mathfrak{C}_{\mu}$ represents the category of "critical points" and "broken trajectories" of the gradient flow of the actional functional parametrized by $\mu$.
\end{itemize}
Suppose $R$ is not of characteristic 2, but $R$ and $O$ are as in Definition 6.3 above. One needs additionally:
\begin{itemize}
\item[] [F6] an orientation of $O$ for the fundamental triple $\pi_{\mathfrak{G}}: \mathfrak{G} \rightarrow \underline{\mathfrak{G}}$, which induces an orientation functor $O_{\mu}$ of $\mathfrak{C}_{\mu}$ for every $\mu \in \mathcal{P}^{\text {gen }}$.
\end{itemize}
As previously explained, by choosing an element $u_{a} \in H(a)$ for each $a \in$ $O 6\left(\mathfrak{C}_{\mu}\right)$, one may identify $O_{\mu}(h)$ with a $\operatorname{sign}(z) \in\{-1,1\}$, for each morphism $z$ in $\mathfrak{C}_{\mu}$. This system of choice is called a coherent orientation for $\mathfrak{C}_{\mu}$. When $\pi_{\mathfrak{G}}: \mathfrak{G} \rightarrow \underline{\mathfrak{G}}$ comes from a (real) manifold $M$ and $\mathfrak{C}_{\mu}$ the category of critical points and broken trajectories of a Morse function on it, $O$ is defined from $\operatorname{det} T M$, and $O_{\mu}$ is defined from $\left\{\operatorname{det} T_{a} \mathcal{D}_{a}\right\}_{a \in O b\left(\mathfrak{C}_{\mu}\right)}$, where $\mathcal{D}_{a}$ denotes the descending manifold from the critical point $a$.

Note that by definition, $\underline{\mathfrak{G}}$ is groupoid; hence each $\operatorname{Mor}(\underline{\mathfrak{G}} ; a, b)$ may be identified with a group $\Pi$ after choosing a reference element in it. With respect to this choice, $\underline{\mathcal{S}}$ and $\underline{\mathcal{E}}_{\mu}$ identify, respectively, with the homomorphisms
$$s: \Pi \rightarrow \mathbb{Z} \quad \text { and } \quad e_{\mu}: \Pi \rightarrow \mathbb{R} .$$
6.1.2. Floer (co)homology with local coefficients. Given a Floer theory package described above and a local system, $\Lambda$, of $R$-modules on $\mathfrak{G}$, a purported Floer chain complex with local coefficient $\Lambda$ is defined from $\mathfrak{C}_{\mu}$ by the following chain groups and differentials:
$$\begin{aligned}
C_{*}(\mathfrak{G}, \mu ; \Lambda) & =\bigoplus_{a \in O b\left(\mathfrak{C}_{\mu}\right)} O_{\mu}(a) \otimes \Lambda(a), \\
\partial & =\sum_{z \in \operatorname{Mor} r^{\prime}\left(\mathfrak{C}_{\mu}\right),} O_{\mu}(z) \otimes \Lambda\left(\pi_{\mathfrak{G}} z\right),
\end{aligned}$$

Since $\mathcal{S}(h)-\mathcal{S}\left(h^{\prime}\right)=s\left(h-h^{\prime}\right)$, where $h, h^{\prime} \in \mathcal{M} o r(\underline{\mathfrak{G}} ; a, b)$ and hence $h-h^{\prime} \in$ $\Pi$, the functor $\mathcal{S}$ defines a $\mathbb{Z} / p \mathbb{Z}$-grading on the Floer complex by
$$\operatorname{gr}(a, b)=\mathcal{S}(h) \bmod p \quad \text { for any } h \in \operatorname{Mor}(\underline{\mathfrak{G}} ; a, b),$$
where $p$ is the divisibility of $s$.
The Floer cochain complex is obtained by replacing the category $\mathfrak{G}$ above by $\mathfrak{G}^{o p}$.

Let $\operatorname{Mor}_{1}\left(\mathfrak{C}_{\mu} ; a, b\right)$ denote the set consisting of elements in $\operatorname{Mor}_{1}\left(\mathfrak{C}_{\mu}\right)$ which go from the object $a$ to the object $b$, and let $\operatorname{Mor}_{1, h}\left(\mathfrak{C}_{\mu} ; a, b\right)$ be its subset
consisting of elements in the "relative homotopy class" $h \in \operatorname{Mor}(\underline{\mathfrak{G}} ; a, b)$. Let $\operatorname{Mor}_{1}(\underline{\mathfrak{G}} ; a, b)=\{h \in \operatorname{Mor}(\underline{\mathfrak{G}} ; a, b) \mid \underline{\mathcal{S}}(h)=1\}$. The chain groups and differentials given can be written more concretely once a coherent orientation of $\mathfrak{C}_{\mu}$ is chosen:
$$\begin{aligned}
C_{*}(\mathfrak{G}, \mu ; \Lambda) & =\bigoplus_{a \in O b\left(\mathfrak{C}_{\mu}\right)} \Lambda(a), \\
\partial a & =\sum_{b \in O b\left(\mathfrak{C}_{\mu}\right)} \sum_{h \in \mathcal{M} o r_{1}(\underline{\mathfrak{G}} ; a, b)} \sigma_{h}(a, b) \Lambda(h) b, \quad \text { where } \\
\sigma_{h}(a, b) & =\sum_{z \in \mathcal{M}_{r}\left(\underline{\mathfrak{C}_{\mu}} ; a, b\right),} \operatorname{sign}(z) .
\end{aligned}$$

In order for the map $\partial$ to be well-defined, certain bounds on the number of elements in $\operatorname{Mor}_{1}\left(\mathfrak{C}_{\mu} ; a, b\right)$ are required in order to make sense of the formula for $\partial$ above. These are typically provided by results of the following form:
$$\begin{aligned}
& \text { For a generic } \mu \text {, the number of elements in } \operatorname{Mor}_{1}^{L}\left(\mathfrak{C}_{\mu} ; a, b\right) \text { is } \\
& \text { finite for any } L \in \mathbb{R} \text {, }
\end{aligned}$$
where $\operatorname{Mor}_{1}^{L}\left(\mathfrak{C}_{\mu} ; a, b\right)=\left\{z \mid z \in \operatorname{Mor}_{1}\left(\mathfrak{C}_{\mu} ; a, b\right), \mathcal{E}_{\mu}(z) \leq L\right\}$.
Since $\mathcal{E}_{\mu}$ factors through $\pi_{\mathfrak{G}}$, this guarantees the finiteness of $\sigma_{h}(a, b)$ for each triple of $a, b, h$. However, $\operatorname{Mor}_{1}(\underline{\mathfrak{G}} ; a, b)$ often has infinitely many elements: with a choice a reference element, it identifies with Ker . Nevertheless, together with the following additional condition, (6.3) guarantees that $\sigma_{h}(a, b)=0$ except for only finitely many elements $h$ in $\operatorname{Mor}_{1}(\underline{\mathfrak{G}} ; a, b)$; hence the formula for $\partial$ is (6.2) is a finite sum when $O b\left(\mathfrak{C}_{\mu}\right)$ has finitely many elements: $\left.e_{\mu}\right|_{\text {Ker } s}=0$, or equivalently,
$$e_{\mu}=-\kappa s \quad \text { for some } \kappa \in \mathbb{R} \text { as elements in } \operatorname{Hom}(\Pi, \mathbb{R}) .$$
When (6.4) fails, the infinite sum in the second line of (6.2) may be made sense of via particular choices of the local coefficients $\Lambda$, as follows.

Let $L \in \mathbb{R}$ from this point on. Paraphrasing Definitions 30.2.1 and 30.2.2 in $[\mathbf{K M}]$, we say that:

Definition 6.4. subset $S \subset \operatorname{Mor}(\underline{\mathfrak{G}} ; a, b)$ is $\left(s, e_{\mu}\right)$-finite if:
\begin{itemize}
\item[(i)] for all $L$, the intersection $S \cap \mathcal{M} o r^{L}(\underline{\mathfrak{G}} ; a, b)$ is finite.
\item[(ii)] there exists $d$ such that $\mathcal{S}(h) \leq d$ for all $h \in S$.
\end{itemize}

A local system of complete, filtered topological abelian groups $\Lambda$ on $\mathfrak{G}$ is $\left(s, e_{\mu}\right)$-complete if, for any $a, b \in O 6(\mathfrak{G})$ and any $\left(s, e_{\mu}\right)$-finite set $S \subset$ $\operatorname{Mor}(\underline{\mathfrak{G}} ; a, b)$,
\begin{itemize}
\item[(i)] the set $\{\Lambda(h) \mid h \in S\} \subset \operatorname{Hom}(\Lambda(a), \Lambda(b))$ is equicontinuous;
\item[(ii)] the homomorphisms $\Lambda(h)$ converges to 0 as $h$ runs through $S$.
\end{itemize}

In the above, $\operatorname{Hom}(\Lambda(a), \Lambda(b))$ is equipped with the compact-open topology, and the notions of complete filtered groups and equicontinuity are as
explained in pp. 601-602 in $[\mathbf{K M}]$. Note that the above definitions depend only on $\left(s, e_{\mu}\right)$, not on the particular choices of $\mathcal{S}$ and $\mathcal{E}_{\mu}$, and a local system is $\left(s, e_{\mu}\right)$-complete if and only if it is $\left(s, \lambda e_{\mu}\right)$-complete, for any $\lambda \in \mathbb{R}^{+}$.

As was observed in [KM], the upshot of this definition is that for any function $\sigma: \operatorname{Mor}(\underline{\mathfrak{G}} ; a, b) \rightarrow \mathbb{Z}$ with $\left(s, e_{\mu}\right)$-finite support, a series of the form $\sum_{h} \sigma(h) \Lambda(h)$ converges to a continuous limit, and the terms of this series may be rearranged. Apply this observation to the series $\sum_{h \in \mathcal{M}_{0} r_{1}(\underline{\mathfrak{G}} ; a, b)} \sigma_{h}(a, b)$. The statement (6.3) implies that the function $h \mapsto$ $\sigma_{h}(a, b)$ is supported on a $\left(s, e_{\mu}\right)$-finite set, and hence the convergence of this series. In sum, the formula (6.2) gives a valid definition of Floer homology of local coefficient $\Lambda$, once the following two conditions are met:
$$\left\{\begin{array}{l}
\bullet \text { there are finitely many elements in } \mathfrak{C}_{\mu} ; \\
\bullet \text { the statement }(6.3) \text { holds. }
\end{array}\right.$$

Example. In the case of (6.4), any (local) coefficient is $\left(s, e_{\mu}\right)$-complete. In particular, Floer homology with coefficient $\mathbb{Z}$ is well-defined. The monotone cases discussed in Sections 1.1 and 1.2 belong to this case with $\kappa \neq 0$. (The $\kappa=0$ case is the "balanced" case in the terminology of $[\mathbf{K M}]$.)
6.2. The non-monotone case. As explained in the previous subsection, the periodic Floer homology and Seiberg-Witten cohomology can be defined in general with appropriate choice of local coefficients.
6.2.1. General Periodic Floer homology. Fix a volume form $w_{F}$ on $F$. In the terminology of the previous subsection, this Floer theory associates the following to each symplectic isotopy class of $f$ and $\Gamma \in H_{1}(M ; \mathbb{Z})$ :
\begin{itemize}
\item[-] One may take $\mathfrak{G}$ to be the category with integral one-cycles in $M$ in the class of $\Gamma$ as objects, and with $\operatorname{Mor}\left(\mathfrak{G} ; \Theta, \Theta^{\prime}\right)$ consisting of integral 2-cycles $\Sigma$ in $\mathbb{R} \times M$, which limit to $\Theta$ or $\Theta^{\prime}$, respectively, as $s \rightarrow \infty$ or $s \rightarrow-\infty$. Let $\underline{\mathfrak{G}}$ be the category with $\operatorname{Mor}\left(\underline{\mathfrak{G}} ; \Theta, \Theta^{\prime}\right)=H_{2}\left(M ; \Theta, \Theta^{\prime}\right)$, and let $\pi_{\mathfrak{G}}$ be the functor which sends an integral one-cycle $\Theta \subset M$ to itself, and an integral two-cycle $\Sigma \subset \mathbb{R} \times M$ described above to the relative homology class of its projection to $M$.
\item[-] The functor $\mathcal{S}$ in this context is given by the relative grading $I\left(\Theta_{+}, \Theta_{-} ; Z\right)$ described in Section 1.1.
\item[-] The parameter space $\mathcal{P}$ may be taken to be the space of pairs $(f, J)$, where $f$ is a symplectomorphism in a fixed Hamiltonian isotopy class, and $J \in \mathcal{J}_{f}$. Using the same notation to denote the pullback of $w_{f}$ under the projection $\mathbb{R} \times M \rightarrow M$, set
$$\mathcal{E}_{\mu}(\Sigma)=\int_{\Sigma} w_{f}, \quad \text { for } \Sigma \in \operatorname{Mor}(\mathfrak{G}) .$$
\end{itemize}
\begin{itemize}
\item[-] We call a $\mu=(f, J) \in \mathcal{P}$ "generic" in this context if $f$ is non-degenerate, and $J \in \mathcal{J}_{1 f}$. Let $\mathfrak{C}_{\mu}$ be the category with $O 6\left(\mathfrak{C}_{\mu}\right)=\mathcal{A}$ and with $\operatorname{Mor}\left(\mathfrak{C}_{\mu}\right)$ consisting of what is termed "broken GFL"s in Definition 9.3 of [H1]. By Lemma 9.3 in the same reference and its generalization in Section 9.5, the set $\operatorname{Mor}_{1}\left(\mathfrak{C}_{\mu} ; \Theta_{+}, \Theta_{-}\right)$is the set $\mathcal{M}_{1}\left(\Theta_{+}, \Theta_{-}\right) / \mathbb{R}$ previously introduced in Section 1.1.
\item[-] It is explained in Section 9 of [HT1] that a coherent orientation is provided by a choice of ordering of the positive hyperbolic periodic orbits in $\Theta$ for each $\Theta \in \mathcal{A}$.
\end{itemize}

In fact, the definitions of $\mathfrak{G}$ and $\mathcal{P}$ above may be chosen somewhat differently, since they do not directly enter into the definition of the Floer complex. Note also that in this Floer theory package,
$$\Pi=H_{2}(M ; \mathbb{Z}), \quad s=c_{\Gamma}, \quad e_{\mu}=\left[w_{f}\right],$$
regarding the latter two as homomorphisms from $H_{2}(M ; \mathbb{Z})$ to $\mathbb{Z}$ and $\mathbb{R}$, respectively. The condition (6.4) becomes the definition for monotone classes in Section 1.1: The cases $\kappa>0$ and $\kappa<0$ correspond to the positive monotone and negative monotone cases, respectively, and $\kappa \neq 0$ in this context.

With $\mathfrak{C}_{\mu}$ and $\mathcal{E}_{\mu}$ thus specified, the validity of the statement (6.3) follows from the typical Gromov compactness arguments as those which appeared in Lemma 9.8 of [H1]. It is also noted in Section 1.1 that $\mathcal{A}$ consists of finitely many elements. Thus, as both conditions in (6.5) are met, given a $\left(c_{\Gamma},\left[w_{f}\right]\right)$-complete local coefficient $\Lambda$ on $\mathfrak{G}$, the formula (6.1) gives a well-defined chain complex. We call the associated homology the periodic Floer homology with coefficient $\Lambda$ of the parameter set $\boldsymbol{\mu}_{P}=\left\{\left(F, w_{F}\right), f, \Gamma, J\right\}$, and denote it by
$$H P_{*}\left(f:\left(F, w_{F}\right) \circlearrowleft, \Gamma ; \Lambda\right)_{J},$$
or simply $H P_{*}(f, \Gamma ; \Lambda)$ when there is no danger of ambiguity. Under the monotonicity assumption, $\Lambda$ can be taken to be $\mathbb{Z}$; in this case the above definition of periodic Floer homology reduces to the version in Section 1.1.
6.2.2. General Seiberg-Witten cohomology. In this Floer theory, choose
\begin{itemize}
\item[-] $\mathfrak{G}$ such that its objects consist of gauge equivalence classes of configurations on $M$, and such that $\operatorname{Mor}\left(\mathfrak{G} ; \mathfrak{c}_{-}, \mathfrak{c}_{+}\right)=\mathcal{B}\left(\mathfrak{c}_{-}, \mathfrak{c}_{+}\right)$. Let $\underline{\mathfrak{G}}$ be the category with the same objects, and with $\operatorname{Mor}\left(\underline{\mathfrak{G}} ; \mathfrak{c}_{-}, \mathfrak{c}_{+}\right)=$ $\pi_{0}\left(\mathcal{B}\left(\mathfrak{c}_{-}, \mathfrak{c}_{+}\right)\right)$. Let $\pi_{\mathfrak{G}}$ be defined by taking the relative homotopy classes of elements in $\mathcal{B}\left(\mathfrak{c}_{-}, \mathfrak{c}_{+}\right)$.
\item[-] Define $\mathcal{S}$ using the relative grading $\mathfrak{I}\left(\mathfrak{c}_{-}, \mathfrak{c}_{+} ; \mathfrak{h}\right)$ introduced in Section 1.2.
\item[-] Take the parameter space $\mathcal{P}$ to be the set of triples $\mu=(\varpi, g,(\mathfrak{T}, \mathfrak{S}))$. Assume through out this article that $[\varpi] \neq 2 \pi c_{1}(\mathfrak{s})$ in $H^{2}(M ; \mathbb{R})$.
\end{itemize}

Choose $\mathcal{E}_{\mu}$ such that $\mathcal{E}_{\mu}(\gamma)=\frac{1}{2} \mathcal{E}_{\omega, \mathfrak{q}}^{\text {top }}(\gamma)$ in the notation of $[\mathbf{K M}]$, where $\omega=-\mathrm{i} \varpi / 4, \mathfrak{q}=(\mathfrak{T}, \mathfrak{S})$.
\begin{itemize}
\item[-] When $\mu$ is generic in the sense explained in Section 1.2, let $\mathfrak{C}_{\mu}$ be the category with $\mathcal{O} \delta\left(\mathfrak{C}_{\mu}\right)=\mathcal{C}$, and with $\operatorname{Mor}\left(\mathfrak{C}_{\mu} ; \mathfrak{c}_{-}, \mathfrak{c}_{+}\right)=\breve{M}^{+}\left(\mathfrak{c}_{-}, \mathfrak{c}_{+}\right)$ in the notation of $[\mathbf{K M}]$. In particular, $\operatorname{Mor}_{1}\left(\mathfrak{C}_{\mu} ; \mathfrak{c}_{-}, \mathfrak{c}_{+}\right)$is what is denoted by $\mathcal{M}_{1}\left(\mathfrak{c}_{-}, \mathfrak{c}_{+}\right) / \mathbb{R}$ in Section 1.1.
\item[-] The functor $O_{\mu}$ assigns to each $\mathfrak{c} \in \mathcal{C}^{r}$ the module in (22.1) of [KM] (the two element set $\Lambda$ in [KM] is $H$ in our notation), and to each $\gamma \in \mathcal{M}_{1}\left(\mathfrak{c}_{-}, \mathfrak{c}_{+}\right) / \mathbb{R}$, the isomorphism $\epsilon(\gamma)$ in (22.4) of [KM].
\end{itemize}
By the above choice of $\mathcal{S}, \mathcal{E}_{\mu}$ and the discussion in Section 1.1, in this Floer theory
$$\Pi=H^{1}(M ; \mathbb{Z}), \quad s=c_{1}(\mathfrak{s}), \quad e_{\mu}=p_{\mathfrak{s}, \varpi} .$$
The condition (6.4) now corresponds to the positive monotone, negative monotone, and balanced cases discussed in Chapter 29 of [KM] when $\kappa<0$, $\kappa>0$, and $\kappa=0$, respectively.

It is shown in $[\mathbf{K M}]$ that the conditions (1.12) and (6.5) hold under our assumption that $p_{\mathfrak{s}, \varpi} \neq 0$, and thus for any $\left(c_{1}(\mathfrak{s}), p_{\mathfrak{s}, \varpi}\right)$-complete local system $\Lambda$, the construction in the previous subsection defines a Floer homology with coefficient $\Lambda$ associated to each parameter set $\boldsymbol{\mu}_{S}=\{M, \mathfrak{s}, \varpi, g, \mathfrak{q}=$ $(\mathfrak{T}, \mathfrak{S})\}$. As previously observed, by replacing $\mathfrak{G}$ with $\mathfrak{G}^{o p}$, the same construction defines a Floer cohomology. Thus, for any $\left(c_{1}(\mathfrak{s}),-p_{\mathfrak{s}, \varpi}\right)$-complete local system $\Lambda$, there is a well-defined Floer cochain complex:
$$\begin{aligned}
C^{*}(\mathfrak{G}, \mu ; \Lambda) & =\bigoplus_{a \in O b\left(\mathfrak{C}_{\mu}\right)} O_{\mu}(a) \otimes \Lambda(a), \\
\delta & =\sum_{z \in \mathcal{M o r}_{1}\left(\mathfrak{C}_{\mu}\right)} O_{\mu}\left(z^{-1}\right) \otimes \Lambda\left(\pi_{\mathfrak{G}} z^{-1}\right) .
\end{aligned}$$
The resulting cohomology is the Seiberg-Witten-Floer cohomology with coefficient $\Lambda$ for $\boldsymbol{\mu}_{S}$. This Floer cohomology only depends on the data set (1.17). We denote it by $\operatorname{Hu}^{*}\left(M, \mathfrak{s}, p_{\mathfrak{s}, \varpi} ; \Lambda\right)$. To compare with the notation in $[\mathbf{K M}]$,
$$H M^{*}(M, \mathfrak{s},-\pi[\varpi] ; \Lambda)=\operatorname{H}^{*}\left(M, \mathfrak{s}, p_{\mathfrak{s}, \varpi} ; \Lambda\right),$$
and what we call a $\left(c_{1}(\mathfrak{s}),-p_{\mathfrak{s}, \varpi}\right)$-complete local system is in the terminology of $[\mathbf{K M}]$, a $c$-dual complete local system with $c=\pi[\varpi]$. When $\mathfrak{s}$, $\varpi$ are monotone with respect to each other, the coefficient $\Lambda$ will often be dropped from the notation when it is set to be $\mathbb{Z}$.
6.3. The general isomorphism theorem. We now generalize Theorem 1.1 to include the non-monotone cases. Associate to each periodic Floer homology data set $\boldsymbol{\mu}_{P}$ a Seiberg-Witten-Floer cohomology data set $\boldsymbol{\mu}_{S}$, as described in Section 1.3.

Fix $L \geq 1$. Given a pair, $\Theta_{-}$and $\Theta_{+}$, from $\mathcal{A}$, introduce $\mathcal{M}_{1 L}\left(\Theta_{+}, \Theta_{-}\right) \subset$ $\mathcal{M}_{1}\left(\Theta_{+}, \Theta_{-}\right)$to denote the elements $\Sigma$ such that
$$\int_{C} w_{f} \leq L,$$
where $C$ is the sole submanifold from $\Sigma$ that is not an $\mathbb{R}$-invariant cylinder. The space $\mathcal{M}_{1 L}\left(\Theta_{+}, \Theta_{-}\right)$has a finite set of components. This is asserted by Theorem 1.8 in [H1]. A value for $L$ in $[1, \infty)$ is said to be generic when there are no cases where (6.8) is an equality. The set of generic values is necessarily the complement of a countable set.

As will be seen momentarily, the space $\mathcal{M}_{1 L}\left(\Theta_{+}, \Theta_{-}\right)$has a precise analog on the Seiberg-Witten side of the ledger. To define this analog, fix $r \geq 1$ such that each solution to (3.13) is non-degenerate. Suppose that $\mathfrak{c}_{-}$and $\mathfrak{c}_{+}$are elements in $\mathcal{C}^{r}$. Given $L \geq 1$, use $\mathcal{M}_{1 L}\left(\mathfrak{c}_{-}, \mathfrak{c}_{+}\right) \subset \mathcal{M}_{1}\left(\mathfrak{c}_{-}, \mathfrak{c}_{+}\right)$to denote the subspace of instantons $\mathfrak{d}=(A, \psi)$ that obey (5.8), namely
$$\frac{\mathrm{i}}{2 \pi} \int_{\mathbb{R} \times M} \frac{\partial A}{\partial s} d s \wedge w_{f} \leq L .$$
Note in this regard that the above integral is absolutely convergent given that $\mathfrak{c}_{-}$and $\mathfrak{c}_{+}$are both non-degenerate.

Recall from Section 3 that Theorem 3.1 makes no assumption on monotonicity. Thus, it constructs an isomorphism $\Phi^{r}$ from $\mathcal{A}$ to $\mathcal{C}^{r}$. Keep in mind that both consist of finitely many non-degenerate elements. Let $\Theta_{-}$and $\Theta_{+}$ denote two elements in $\mathcal{A}$, and let $\mathfrak{c}_{-}$and $\mathfrak{c}_{+}$denote solutions to (3.11) that give $\Phi^{r}\left(\Theta_{-}\right)$and $\Phi^{r}\left(\Theta_{+}\right)$. Theorem 4.1 as stated does require the assumption of monotonicity to guarantee that both $\mathcal{M}_{1}\left(\Theta_{+}, \Theta_{-}\right)$and $\mathcal{M}_{1}\left(\mathfrak{c}_{-}, \mathfrak{c}_{+}\right)$ are finite. However, the theorem that follows is the non-monotone analog.

Theorem 6.1. Let $\boldsymbol{\mu}_{P}=\left\{\left(F, w_{F}\right), f, \Gamma, J\right\}$ and $\boldsymbol{\mu}_{S}=\left\{M, \mathfrak{s}_{\Gamma}, \varpi_{r}, g, \mathfrak{q}\right\}$ be as in the statement of Theorem 1.1. Fix a generic $L \geq 1$. Then there exists a constant $\kappa_{L}>1$ such that given $N>\kappa_{L}, \delta<\kappa_{L}^{-1}$ and a $(\delta, N)$ -approximation $\left(f^{\prime}, J^{\prime}\right)$ to $(f, J)$, there exists $\kappa_{L}^{\prime} \geq \kappa_{L}$ so that for any $r \geq \kappa_{L}^{\prime}$, the following hold for $\mathcal{A}$ and $\mathcal{C}^{r}$ defined using $\left(f^{\prime}, J^{\prime}\right)$ :
\begin{itemize}
\item[(0)] Theorem 3.1 can be invoked so as to provide the identification, $\Phi^{r}$, between $\mathcal{A}$ and $\mathcal{C}^{r}$.
\item[(1)] Fix a pair $\Theta_{-}$and $\Theta_{+}$in $\mathcal{A}$; and let $\mathfrak{c}_{-}$and $\mathfrak{c}_{+}$denote solutions to (3.13) whose respective gauge equivalence classes are $\Phi^{r}\left(\Theta_{-}\right)$and $\Phi^{r}\left(\Theta_{+}\right)$. Let $\mathcal{M}_{1 L}\left(\Theta_{+}, \Theta_{-}\right)$and $\mathcal{M}_{1 L}\left(\mathfrak{c}_{-}, \mathfrak{c}_{+}\right)$be the versions defined using $\left(f^{\prime}, J^{\prime}\right)$.
\begin{itemize}
\item[(a)] The space $\mathcal{M}_{1 L}\left(\mathfrak{c}_{-}, \mathfrak{c}_{+}\right)$has a finite set of components and each component consists of non-degenerate solutions to (4.4).
\item[(b)] There is a smooth $\mathbb{R}$-equivariant diffeomorphism
$$\Psi^{r}: \mathcal{M}_{1 L}\left(\Theta_{+}, \Theta_{-}\right) \rightarrow \mathcal{M}_{1 L}\left(\mathfrak{c}_{-}, \mathfrak{c}_{+}\right) .$$
\end{itemize}
\end{itemize}
\begin{itemize}
\item[(2)] There are coherent systems of orientations for sheaves $\left\{\Lambda\left(\Theta_{+}, \Theta_{-}\right)\right\}_{\Theta_{-}, \Theta_{+} \in \mathcal{A}}$ and $\left\{\Lambda\left(\mathfrak{c}_{-}, \mathfrak{c}_{+}\right)\right\}_{\mathfrak{c}_{-}, \mathfrak{c}_{+} \in \mathbb{e}^{r}}$ such that any given $\left(\Theta_{-}, \Theta_{+}\right)$version of $\Psi^{r}$ maps the orientation $\mathfrak{o}_{p F h}$ to the orientation $\mathfrak{o}_{S W}$.
\end{itemize}

Proof. The arguments used to prove Theorem 4.1 can be employed with only cosmetic changes to prove the following: Fix a generic $L \geq 1$. Then there exists an $L$-dependent constant $\kappa_{L}$ such that if $r \geq \kappa_{L}$, the conclusions of assertions (1) and (2) hold with $\mathcal{M}_{1}\left(\Theta_{+}, \Theta_{-}\right)$and $\mathcal{M}_{1}\left(\mathfrak{c}_{-}, \mathfrak{c}_{+}\right)$replaced, respectively, by $\mathcal{M}_{1 L}\left(\Theta_{+}, \Theta_{-}\right)$and $\mathcal{M}_{1 L}\left(\mathfrak{c}_{-}, \mathfrak{c}_{+}\right)$. Indeed, the only change to Part 1 is the change from $\mathcal{M}_{1}(\cdot)$ to $\mathcal{M}_{1 L}(\cdot)$. The gluing construction used in the proof shows that $\Psi^{r}$ maps $\mathcal{M}_{1 L}\left(\Theta_{+}, \Theta_{-}\right)$injectively into $\mathcal{M}_{1 L}\left(\mathfrak{c}_{-}, \mathfrak{c}_{+}\right)$ when $r$ is greater than a purely $L$-dependent constant. The proof that Theorem 4.1's version of $\Psi^{r}$ maps $\mathcal{M}_{1 L}\left(\Theta_{+}, \Theta_{-}\right)$surjectively onto $\mathcal{M}_{1 L}\left(\mathfrak{c}_{-}, \mathfrak{c}_{+}\right)$in the monotone case uses the monotonicity assumption only to obtain a bound on (4.7) from a bound on the index. The bound on (4.7) is then used to derive the global results in Section 5. In the case at hand, the bound on (4.7) is assumed because we are restricting attention to instantons in $\mathcal{M}_{1 L}\left(\mathfrak{c}_{-}, \mathfrak{c}_{+}\right)$. This understood, the arguments in Section 5 can be used verbatim to prove that $\Psi^{r}$ maps $\mathcal{M}_{1 L}\left(\Theta_{+}, \Theta_{-}\right)$surjectively onto $\mathcal{M}_{1 L}\left(\mathfrak{c}_{-}, \mathfrak{c}_{+}\right)$. \(\square\)

Noting that the conditions (5.8) and (6.9) correspond under $\Psi^{r}$, straightforward modifications of the direct limit arguments in Sections 4d-4i of [T1] then yield the following:

Theorem 6.2. Let $\boldsymbol{\mu}_{P}=\left\{\left(F, w_{F}\right), f, \Gamma, J\right\}$ be a periodic Floer parameter set, where $\Gamma \in H_{1}(M ; \mathbb{Z})$ is an arbitrary class. Associate to it a Seiberg-Witten parameter set $\boldsymbol{\mu}_{S}=\left\{M, \mathfrak{s}_{\Gamma}, \varpi_{r}, g, \mathfrak{q}\right\}$ according to the recipe described in Section 1.3. Let $\Lambda_{P}$ be a $\left(c_{\Gamma},\left[w_{f}\right]\right)$-complete local system for the periodic Floer homology, and let $\Lambda_{S}$ denote a corresponding $\left(c_{1}\left(\mathfrak{s}_{\Gamma}\right), 2 r \pi\left[w_{f}\right]\right)$-complete local system for the Seiberg-Witten cohomology, in the sense specified below. Then there is an isomorphism between the two Floer (co)homologies with coefficient $\Lambda$
$$H P_{*}\left(f:\left(F, w_{F}\right) \circlearrowleft, \Gamma ; \Lambda_{P}\right)_{J} \simeq \operatorname{HM}^{-*}\left(M, \mathfrak{s}_{\Gamma},-2 r \pi\left[w_{f}\right] ; \Lambda_{S}\right),$$
which reverses the relative $\mathbb{Z} / p \mathbb{Z}$-gradings.
Use the subscripts $P$ and $S$, respectively, to label the ingredients $\pi_{\mathfrak{G}}$ : $\mathfrak{G} \rightarrow \underline{\mathfrak{G}}$, etc. in the periodic Floer theory and Seiberg-Witten-Floer theory, as described in the previous subsection. To introduce $\Lambda_{S}$, note that only its restriction to $\mathfrak{C}_{\mu_{S}}$ is relevant in the statement of the preceding theorem. A $\left(c_{\Gamma},\left[w_{f}\right]\right)$-complete local system $\Lambda_{P}$ on $\mathfrak{G}_{P}$ specifies a local system on this restriction via the maps $\Phi^{r}, \Psi^{r}$. In particular, recall from Section 1.3 that for a periodic Floer parameter set $\boldsymbol{\mu}_{P}$ and its corresponding Seiberg-Witten
parameter set $\boldsymbol{\mu}_{S}$, one has $c_{\Gamma}=c_{\mathfrak{s}_{\Gamma}}$ and $p_{\mathfrak{s}, \varpi_{r}}=-2 r \pi\left[w_{f}\right]$. Moreover, comparing (6.6) and (6.7), and we see that the two Floer theories have identical $s$, while $e_{\mu}$ on the Seiberg-Witten side is $-2 r \pi$ times that on the periodic Floer homology side. Thus, $\Lambda_{P}$ is $\left(s, e_{\mu}\right)$-complete on the periodic Floer homology side if and only if $\Lambda_{S}$ is $\left(s,-e_{\mu}\right)$-complete on the Seiberg-Witten-Floer theory side. In other words, the Seiberg-Witten-Floer cohomology for $\boldsymbol{\mu}_{S}$ with coefficient $\Lambda_{S}$ is well-defined exactly when the periodic Floer homology for $\boldsymbol{\mu}_{P}$ with coefficient $\Lambda_{P}$ is.

Corollary 1.1 generalizes correspondingly:
Corollary 6.1. The general periodic Floer homology in the previous theorem depends only on the Hamiltonian isotopy class of $f$, the homology class $\Gamma$, and the local system $\Lambda$. In fact, the periodic Floer homology with "maximallytwisted coefficients" depends only on the symplectic isotopy class of $f$ and $\Gamma$, in the following sense:

Let $\Lambda_{\left[w_{f}\right]} \supset \mathbb{Z}\left[H_{1}(M ; \mathbb{Z})\right]$ denote the Novikov ring consisting of $\mathbb{Z}$-valued functions on $H_{1}(M ; \mathbb{Z})$ that are finitely supported on $\left[w_{f}\right]^{-1}(-\infty, \kappa]$ for any $\kappa \in \mathbb{R}$, regarding $\left[w_{f}\right]$ as an element in $\operatorname{Hom}\left(H_{2}(M ; \mathbb{Z}), \mathbb{R}\right)$. Then there is a $\mathbb{Z}\left[H_{1}(M ; \mathbb{Z})\right]$-module with relative $\mathbb{Z} / p \mathbb{Z}$-grading, denoted $H P_{*}^{[f]}(\Gamma)$, such that
$$H P_{*}\left(f, \Gamma ; \Lambda_{\left[w_{f}\right]}\right) \simeq H P_{*}^{[f]}(\Gamma) \otimes_{\mathbb{Z}\left[H_{1}(M ; \mathbb{Z})\right]} \Lambda_{\left[w_{f}\right]},$$
and $H P_{*}^{[f]}(\Gamma)$ depends only on the symplectic isotopy class $[f]$ and $\Gamma$.
Proof. Because of the previous Theorem, it suffices to check the corresponding statement for $\operatorname{Hm}^{*}\left(M, \mathfrak{s}_{\Gamma},-2 r \pi\left[w_{f}\right] ; \Lambda_{\left[w_{f}\right]}\right)$. First, observe that
$$\overline{\mathrm{HM}}^{*}\left(M, \mathfrak{s}_{\Gamma}, 0 ; \Lambda_{\left[w_{f}\right]}\right)=\overline{H M}^{*}\left(M, \mathfrak{s}_{\Gamma}, c_{b} ; \Lambda_{\left[w_{f}\right]}\right)=0,$$
due to the well-known fact that the Novikov homology of a torus is trivial. Thus, we may again write $\widehat{\operatorname{HM}}^{*}\left(M, \mathfrak{s}_{\Gamma}, 0 ; \Lambda_{\left[w_{f}\right]}\right)=\widehat{\operatorname{HM}}^{*}\left(M, \mathfrak{s}_{\Gamma}, 0 ; \Lambda_{\left[w_{f}\right]}\right)=$ $\operatorname{Hm}^{*}\left(M, \mathfrak{s}_{\Gamma}, 0 ; \Lambda_{\left[w_{f}\right]}\right)$. Now, the variant of Theorem 31.5.1 in $[\mathbf{K M}]$ with local coefficients states:
$$\operatorname{HM}^{*}\left(M, \mathfrak{s}_{\Gamma}, 0 ; \Lambda_{\left[w_{f}\right]}\right) \simeq \operatorname{HM}^{*}\left(M, \mathfrak{s}_{\Gamma},-2 r \pi\left[w_{f}\right] ; \Lambda_{\left[w_{f}\right]}\right) .$$
However, the coefficient ring $\mathbb{Z}\left[H_{1}(M ; \mathbb{Z})\right]$ is $\left(\mathfrak{s}_{\Gamma}, 0\right)$-complete, and $\Lambda_{\left[w_{f}\right]}$ is flat over $\mathbb{Z}\left[H_{1}(M ; \mathbb{Z})\right]$. Thus
$$\operatorname{Hm}^{*}\left(M, \mathfrak{s}_{\Gamma}, 0 ; \Lambda_{\left[w_{f}\right]}\right)=\operatorname{Hm}^{*}\left(M, \mathfrak{s}_{\Gamma}, 0 ; \mathbb{Z}\left[H_{1}(M ; \mathbb{Z})\right]\right) \otimes_{\mathbb{Z}\left[H_{1}(M ; \mathbb{Z})\right]} \Lambda_{\left[w_{f}\right]} .$$

For homologies classes $\Gamma$ with degree 1, the Periodic Floer homology reduces to the Floer homology of symplectic fixed points. Thus, in this special case, Corollaries 1.1, 6.1 reduce to the invariance properties of the latter Floer homology in the existent literature. \(\square\)

\section*{7. Appendices}

In Appendix 7.1, we describe the appropriate parameter space of the periodic Floer homology, and clarify its relation with the parameter space of the Seiberg-Witten-Floer cohomology. Note from the outset that in general, the coefficient system $\Lambda$ will not be considered to be among the parameters of a Floer theory since it is chosen extraneously. Moreover, it is clear from the discussion in Section 6 that local systems for two different Floer theories may be identified by identifying their respective versions of $\underline{\mathfrak{G}}$, which depend on the intrinsic parameters of the theory. So do the functions $s, e_{\mu}$ that determine the completeness condition of the local systems.

One application of the isomorphism theorem in this article is the computation of Seiberg-Witten-Floer cohomology for degree 1 Spin ${ }^{c}$ structures of all mapping tori, via the computation of Floer homology of symplectic fixed points for oriented surfaces in the existent literature. We denote this latter Floer homology by $H F$. In Appendix 7.2, we describe the version of $H F$ which is equivalent to the periodic Floer homology. In [C] and its sequel, Cotton-Clay has a more refined definition of $H F$, which may be used to compute the version described below.
7.1. The dependence of HP on $f$. Let $h \in \operatorname{Symp}\left(F, w_{F}\right)$ be an element in the group of symplectomorphisms of $\left(F, w_{F}\right)$, and let $\operatorname{Symp}_{h}\left(F, w_{F}\right) \subset$ $\operatorname{Symp}\left(F, w_{F}\right)$ denote the path component containing $h$. We now define family versions of $M, w_{f}$, and $c_{1}\left(K^{-1}\right)$ parametrized by $\operatorname{Symp}_{h}\left(F, w_{F}\right)$ and its universal covering.

Let $\underline{M} \rightarrow \operatorname{Symp}_{h}\left(F, w_{F}\right)$ be defined as follows:
$$\underline{M}=\left(\operatorname{Symp}_{h}\left(F, w_{F}\right) \times \mathbb{R} \times F\right) /((f, t, x) \sim(f, t+2 \pi, f(x))) .$$
By projecting to the first factor of the product $\operatorname{Symp}_{h}\left(F, w_{F}\right) \times \mathbb{R} \times F, \underline{M}$ may be viewed as a bundle over $\operatorname{Symp}_{h}\left(F, w_{F}\right)$ whose fiber over $f$ is the mapping torus $M_{f}$ of $f$. By projecting to the first two factors, $\underline{M}$ may be viewed as a fiber bundle over $\operatorname{Symp}_{h}\left(F, w_{F}\right) \times S^{1}$; and the Euler class of the vertical tangent bundle $\underline{K}^{-1}$ over this fiber bundle, denoted by $\underline{c}$, restricts to the class $c_{1}\left(K^{-1}\right)$ on each $M_{f} \subset \underline{M}$. Finally, one may pull-back $w_{F}$ from the projection to the last factor $F$. This induces a closed two-form $\underline{w}$, which restricts to each $M_{f}$ as $w_{f}$.

Choose a connection $a$ on the bundle $\underline{M} \rightarrow \operatorname{Symp}_{h}\left(F, w_{F}\right)$ which preserves the structure of its fibers $M_{f}$ as a mapping torus of symplectomorphisms of $\left(F, w_{F}\right)$. Let $X$ denote a symplectic vector field on $\left(F, w_{F}\right)$ and thus an element in $T_{f} \operatorname{Symp}_{h}\left(F, w_{F}\right)$. A connection as just defined assigns to $X$ the
following object:
$$\left\{\begin{aligned}
\bullet & X_{f} \text { is a section of the vertical tangent bundle Ker } \pi_{*} \text { over the } \\
& \text { mapping torus } \pi: M_{f} \rightarrow S^{1}, \\
- & X_{f} \text { is a map sending each } t \in S^{1} \text { to a symplectic vector field } \\
& X_{f}(t) \text { on }\left(F, w_{F}\right) . \\
& -\pi_{*} X_{f}=X .
\end{aligned}\right.$$
The preceding construction defines various associated bundles of $\underline{M} \rightarrow$ $\operatorname{Symp}_{h}\left(F, w_{F}\right)$ and connections on them. Note however that the monodromies of the various homology or cohomology bundles $H(M) \rightarrow$ $\underline{H}(M) \rightarrow \operatorname{Symp}_{h}\left(F, w_{F}\right)$ do not depend on the choice of connection on $\underline{M}$.

Let $\widetilde{M} \rightarrow{\widetilde{\operatorname{Symp}_{h}}}\left(F, w_{F}\right)$ be the pull-back bundle over $\underline{M}$ under the covering map of $\widetilde{\operatorname{Symp}}_{h}\left(F, w_{F}\right)$, and let $\widetilde{H}(M), \widetilde{c}, \widetilde{w}$, respectively denote the pull-backs of $\underline{H}(M), \underline{c}, \underline{w}$ over $\widetilde{M}$. The choice of connection on $\underline{M}$ above defines a trivialization of $\widetilde{M} \rightarrow \widetilde{\operatorname{Symp}}_{h}\left(F, w_{F}\right)$, which induces trivializations on its various associated bundles as well.

In order to compare with the Seiberg-Witten-Floer cohomology, we view the periodic Floer homology $H P$ as intrinsically an invariant of a fibered three-manifold $\pi: M \rightarrow S^{1}$, a homology class $\Gamma \in H_{1}(M ; \mathbb{Z})$, a closed twoform $w \in \Omega^{2}(M)$ which restricts to $w_{F}$ on the fibers, and an almost complex structure $J$ on $\mathbb{R} \times M$ satisfying the conditions (1.6), with $w_{f}$ therein replaced by $w$. From this point of view, $H P$ depends indirectly on the symplectomorphism $f$ through the choice of the two-form $w=w_{f}$, and through the vector field $\partial_{t}$. Thus, to compare the periodic Floer homologies of different symplectomorphisms, first fix a lifting $f_{0} \in \widetilde{\operatorname{Symp}}_{h}\left(F, w_{F}\right)$ of $h$. Identify $M$ with the fiber $M_{f_{0}} \subset \widetilde{M}$, and set $w=w_{f_{0}}$. Then for each triple consisting of $\Gamma \in H_{1}\left(M_{f_{0}} ; \mathbb{Z}\right)$, a suitable local system $\Lambda$, and $J \in \mathcal{J}_{f_{0}}$, the construction in Sections 1 and 6 gives rise to a periodic Floer homology, which we denote by $H P\left(f_{0}, \Gamma ; \Lambda\right)_{J}$. For an arbitrary $f \in \widetilde{\operatorname{Symp}}_{h}\left(F, w_{F}\right)$, use the trivializations given by $a$ to define isomorphisms $\iota_{f}: M_{f} \rightarrow M_{f_{0}}, \iota_{f}^{*}: \Omega^{2}\left(M_{f_{0}}\right) \rightarrow \Omega^{2}\left(M_{f}\right)$, $\left(\iota_{f}\right)_{*}: H_{1}\left(M_{f}\right) \rightarrow H_{1}\left(M_{f_{0}}\right)$, and $\left(\iota_{f}\right)_{*}: \mathcal{J}_{f} \rightarrow \mathcal{J}_{f_{0}}$.

Then for each triple consisting of a $\Gamma_{f} \in H_{1}\left(M_{f}\right)$, a local system $\Lambda_{f}$ for $f$, and a $J_{f} \in \mathcal{J}_{f}$, we define $H P\left(f, \Gamma_{f} ; \Lambda_{f}\right)_{J_{f}}$ to be the periodic Floer homology associated to $\left(\iota_{f}\right)_{*} \Gamma,\left(\iota_{f}^{-1}\right)^{*} w_{f},\left(\iota_{f}^{-1}\right)^{*} \Lambda_{f}$, and $\left(\iota_{f}\right)_{*} J$. The completeness condition for $\Lambda_{f}$ is provided by pull-backs of $\left.\widetilde{c}\right|_{M_{f}}+2 e_{\Gamma_{f}}$ and $\left[w_{f}\right]$ via $\left(\iota_{f}^{-1}\right)^{*}$.

In this manner, we have defined the periodic Floer homology over the parameter space $\widetilde{H}_{1}(M ; \mathbb{Z}) \times_{\widetilde{\operatorname{Symp}}_{h}} \widetilde{\mathcal{J}}$. Here, $\widetilde{\mathcal{J}}$ is the family version of $\mathcal{J}_{f}$ over $\widetilde{\operatorname{Symp}}_{h}=\widetilde{\operatorname{Symp}}_{h}\left(F, w_{F}\right)$. On the other hand, since the Seiberg-Witten-Floer cohomology depends only on the Spin ${ }^{c}$ structure and the cohomology
class of the perturbation two-form, one has $H M$ defined over the parameter space $\operatorname{Spin}^{c}(M) \times H^{2}(M ; \mathbb{Z})$, where $\operatorname{Spin}^{c}(M)$ denotes the set of $\operatorname{Spin}^{c}$ structures on $M$. Fix a sufficiently large $r$. The isomorphism $\Phi$ from $H P$ to $H M$ constructed in the main theorems of this article factors through a map $q$ between their parameter spaces, in the sense that $\Phi(H P(\cdot))=H M(q(\cdot))$. To describe this map $q$, first, note the aforementioned connection defines a trivialization
$$\widetilde{H}_{1}(M ; \mathbb{Z}) \times{\widetilde{\text { Symp }_{h}}} \widetilde{\mathcal{J}} \rightarrow H_{1}(M ; \mathbb{Z}) \times{\widetilde{\operatorname{Symp}_{h}}}^{\times} \times \mathcal{J}_{f_{0}} .$$
The map $q$ is the composition of this with the map which sends $(\Gamma, f, J) \in$ $H_{1}(M ; \mathbb{Z}) \times \widetilde{\operatorname{Symp}}_{h} \times \mathcal{J}_{f_{0}}$ to $\left(\mathfrak{s}_{\Gamma}, 2 r\left(\left[w_{f_{0}}\right]+\sigma\left(\theta_{f}\right)\right)+2 \pi c_{\Gamma}\right) \in \operatorname{Spin}^{c}(M) \times$ $H^{2}(M ; \mathbb{R})$. In the above, $\mathfrak{s}_{\Gamma}$ is defined as in Section 1.3, $\theta_{f}$ denotes the flux of a symplectic isotopy from $f_{0}$ to $f$, and the map $b$ is part of the Mayer-Vietoris sequence: $\cdots H^{1}(F ; \mathbb{R}) \xrightarrow{1-f^{*}} H^{1}(F ; \mathbb{R}) \xrightarrow{6} H^{2}(M ; \mathbb{R}) \cdots$. As a consequence, we have a family of periodic Floer homologies parametrized by $\operatorname{Spin}^{c}(M) \times$ $H^{2}(M ; \mathbb{R})$, and this does not depend on the choice of connection on $\underline{M}$. When $f$ vary through a path in $\widehat{\mathrm{Symp}}_{h}$ connecting two different lifts of the same symplectomorphism, the corresponding Spin ${ }^{c}$-structure (determined by the vector field $\partial_{t}$ ) and the class $\left[w_{f}\right]$ will change simultaneously. The periodic Floer homology, and hence the corresponding Seiberg-Witten-Floer cohomology, parametrized by these two elements in $\operatorname{Spin}^{c}(M) \times H^{2}(M ; \mathbb{R})$ will however be isomorphic.

Remark. Cotton-Clay pointed out to us that there is no such monodromy unless $g=1$; therefore the above observation is interesting only in very limited cases.

Appendix 7.2: Relation with the Floer homology of fixed points. When $\Gamma$ has degree 1, a generator of $C P$ may be regarded as a section of $\pi: M \rightarrow S^{1}$, and by [H1], an element in $\mathcal{M}_{1}\left(\Theta_{+}, \Theta_{-}\right)$used to define the differential of the periodic Floer chain complex consists of a holomorphic cylinder in $\mathbb{R} \times M$. When $J$ is admissible, such a cylinder may be viewed as a holomorphic section $\mathbb{R} \times(\mathbb{R} /(t \sim t+2 \pi) \rightarrow \mathbb{R} \times((\mathbb{R} \times F) / \sim)=\mathbb{R} \times M$. A section of $\pi: M \rightarrow S^{1}$ is by definition an element in the $f$-twisted loop space of $F$, which we denote by $\mathcal{L}_{f}$. A section of $\mathbb{R} \times M \rightarrow \mathbb{R} \times S^{1}$ can be interpreted as a path in $\mathcal{L}_{f}$. Given an element $\Gamma \in H_{1}(M ; \mathbb{Z})$, let $\mathcal{L}_{f, \Gamma}$ denote the space of sections of $\pi: M \rightarrow S^{1}$ in the homology class $\Gamma$. The $f$-twisted loop space decomposes as $\mathcal{L}_{f}=\coprod_{\Gamma \in \mathcal{N}} \mathcal{L}_{f, \Gamma}$, where $\mathcal{N}$ denotes the set of elements $\Gamma \in H_{1}(M ; \mathbb{Z})$ with $\left\langle e_{\Gamma^{\cdot}},[F]\right\rangle=1$. This is an affine space under $H_{1}(F ; \mathbb{Z}) /\left(1-f_{*}\right)$.

For lack of space, we shall only outline the construction of $H F$, and refer the reader to Sections 2 and 3 of [L2] for more details.

Fix the symplectic structure $\left(F, w_{F}\right)$. The space of admissible almost complex structures on $\mathbb{R} \times M$ is identical with the space $\mathcal{J}_{K}$ in [L2], and an element from this space defines a metric on $\mathcal{L}_{f}$. Let $\mathcal{X}_{f}$ be the space of elements satisfying the first two conditions of (7.1). Given an $X_{f} \in X_{f}$, equation (13) of [L2] defines an action one-form on $\mathcal{L}_{f}$. One may use the formal Morse-Novikov theory of this one-form over $\mathcal{L}_{f, \Gamma}$ and the aforementioned metric to define a Floer homology for a suitable choice of coefficient $\Lambda$. We denote this Floer homology by $H F\left(f, \Gamma, X_{f} ; \Lambda\right)_{J}$. The critical points of this action oneform consists of $f$-twisted periodic orbits of the symplectic vector fields $X_{f}$, and the flow lines satisfy the perturbed Cauchy-Riemann equation. In particular, when $X_{f}=0$, we have an isomorphism between the $H F$ chain complexes and the $H P$ chain complexes for the same triple $f, \Gamma, J$. Furthermore, in the language of Section 6.1, there is a natural functor from the fundamental groupoid of $\mathcal{L}_{f, \Gamma}$ to the version of $\underline{\mathfrak{G}}$ in the periodic Floer homology, whose morphism sets are $H_{2}\left(M ; \Theta_{+}, \Theta_{-}\right)$. (This is an variant of the map $\underline{\mathrm{im}}$ defined in Section 3.1.3 of [L2], and hence we denote it by the same notation.) The functors $\mathcal{S}, \mathcal{E}_{\mu}$ in $H F$ (defined from the Conley-Zehnder index and the aforementioned action one-form) both factor through $\underline{i m}$. Thus, by restricting the choice of local systems to those which factor through this map, we may use the same groupoid as the $\underline{\mathfrak{G}}$ in $H F$ as well. To continue the comparison, recall the basic fact (6.7) on $H P$. When $X_{f}=0$, the $H P$ -version of $e_{\mu}$, i.e., $\left[w_{f}\right]$, pulls back by $\underline{\mathrm{im}}$ to its counterpart in $H F$. However, the $H F$-version of $s$, which pulls back to $c_{1}\left(K^{-1}\right)$, is seemingly different from its counterpart in $H P$, namely $c_{\Gamma}=c_{1}\left(K^{-1}\right)+2 e_{\Gamma}$. However, this is inconsequential. The fact that in the degree 1 case, $\mathcal{M}_{1}\left(\Theta_{+}, \Theta_{-}\right)$consists of holomorphic cylinders implies that in both $H F$ and $H P$ of degree 1, the relative homology classes of the flow lines used to define their differentials fall in the image of im. Let $\mathfrak{H} \subset H_{2}(M ; \mathbb{Z})$ denote the image of im as in [L2]. Then $e_{\Gamma} \mid \mathfrak{H}=0$.

This has the following implications: First, the relative grading of the degree 1 periodic Floer homology can be refined to take value in $\mathbb{Z} / p_{1} \mathbb{Z}$, where $p_{1} \geq p$ is the divisibility of $c_{1}\left(K^{-1}\right)$ on $\mathfrak{H} /$ Tors. Second, the $\left(s, e_{\mu}\right)$ -completeness condition on the coefficient systems is weaker in the degree 1 case, since $s, e_{\mu}$ can now be viewed as a linear function from the smaller group $\mathfrak{H} \subset H_{2}(M ; \mathbb{Z})$. In particular, the monotonicity condition (6.4) requires only that $\left.\left[w_{f}\right]\right|_{\mathfrak{H}}$ is proportional to $c_{1}\left(K^{-1}\right) \mid \mathfrak{H}$. For example, if $f$ is monotone in the sense that $\left[w_{f}\right]$ and $c_{1}\left(K^{-1}\right)$ are proportional, then the periodic Floer homology with $\mathbb{Z}$-coefficients is well-defined for all $\Gamma \in \mathcal{N}$ at this $f$, and thus there is a well-defined notion of $H P_{1}(f ; \mathbb{Z})=\bigoplus_{\Gamma \in \mathcal{N}} H P(f, \Gamma ; \mathbb{Z})$, agreeing with the usual notion of $H F(f ; \mathbb{Z})$ (cf. Theorem 4.1.3 of [L2]).

Finally, we compare the parameter spaces of these two Floer theories. In contrast to the view point we adopted for $H P$ in Appendix 7.1, we view the symplectomorphism $f$ as an intrinsic parameter of $H F$. The space $\mathcal{P}_{H F}=\underline{\mathcal{N}} \times_{\text {Symp }_{h}} \underline{\mathcal{X}} \times_{\text {Symp }_{h}} \underline{\mathcal{J}}$ parametrizes the above construction of $H F$. Here, $\underline{\mathcal{N}}, \underline{\mathcal{X}}, \underline{\mathcal{J}}$ are, respectively, the family versions of $\mathcal{N}, \mathcal{X}, \mathcal{J}_{K}$ parametrized by $\operatorname{Symp}_{h}\left(F, w_{F}\right)$. The connection $a$ induces connections on each of these bundles, and hence a connection on the fibered product $\mathcal{P}_{H F}$ as well.

We now describe the map from the $H P$-parameter space to the $H F$-parameter space over which the isomorphism between the two Floer homologies is defined. When restricted to degree $1 H_{1}(M ; \mathbb{Z})$ classes, the $H P$ parameter space is trivialized by the connection $a$ as $\mathcal{P}_{H P_{1}}=\mathcal{N} \times \widetilde{\operatorname{Symp}}_{h} \times \mathcal{J}$. As explained above, the same connection gives a trivialization of the pullback of the $H F$-parameter space over $\widetilde{\operatorname{Symp}}_{h}: \widetilde{\mathcal{P}}_{H F} \simeq \mathcal{N} \times{\widetilde{\operatorname{Symp}_{h}}} \times \mathcal{X}_{f_{0}} \times \mathcal{J}$. (cf. Section 3.1.5 in [L2], where it is also shown that parallel transport along the connection on $\mathcal{P}_{H F}$ yields isomorphisms among the $H F$ Floer chain complexes so parametrized).

Let $\widetilde{m}=\mathrm{id} \times \widetilde{s}_{0} \times \mathrm{id}$, where $\widetilde{s}_{0}$ denotes the zero section of $\widetilde{\operatorname{Symp}_{h}} \times \mathcal{X}_{f_{0}} \rightarrow$ $\widetilde{\mathrm{Symp}_{h}}$. (Note that the zero section $\widetilde{s_{0}}$ is non-constant relative to the trivialization induced by $a$, and depends on the choice of the lift $f_{0}$.) This is the map underlying the isomorphism between the parametrized versions of $H P_{1}$ and $H F$. Notice that by the invariance of $H F$ under the parallel transport determined bya, one may identify $H F$ on the zero section with a fiber $\mathcal{N} \times\left\{f_{0}\right\} \times \mathcal{X}_{f_{0}} \times \mathcal{J}$ of $\widetilde{\mathcal{P}}_{H F}$. As a consequence, one may take $m: \mathcal{N} \times{\widetilde{\operatorname{Symp}_{h}}} \times \mathcal{J} \rightarrow \mathcal{N} \times \mathcal{X}_{f_{0}} \times \mathcal{J}$ to be the map underlying the isomorphism between the parametrized versions of $H F$ and $H P_{1}$, where $m$ sends $(n, f, J)$ to $\left(n, \theta_{f}, J\right)$, where $f \mapsto \theta_{f}$ is as in the definition of $q$ in Appendix 7.1.

\section*{References}
\begin{itemize}
\item[] [BEHWZ] F. Bourgeois, Y. Eliashberg, H. Hofer, K. Wysocki and E. Zehnder, Compactness results in symplectic field theory, Geom. Topol. 7 (2003), 799-888.
\item[] [C] A. Cotton-Clay, Symplectic Floer homology of area-preserving surface diffeomorphisms, Geom. Topol. 13(5) (2009), 2619-2674.
\item[] [H1] M. Hutchings, An index inequality for embedded pseudoholomorphic curves in symplectizations, J. Eur. Math. Soc. (JEMS) 4 (2002), 313-361.
\item[] [HL] M. Hutchings and Y. J. Lee, Circle-valued Morse theory and Reidemeister torsion. Geom. Topol. 3 (1999), 369-396.
\end{itemize}
\begin{itemize}
\item[] [HS] M. Hutchings and M. Sullivan, The periodic Floer homology of a Dehn twist, Alg. Geom. Topol. 5 (2005), 301-354.
\item[] [HT1] M. Hutchings and C. H. Taubes, Gluing pseudoholomorphic curves along branched covered cylinders II, J. Sympl. Geom. 7 (2009), 29-133.
\item[] [HT2] -, Gluing pseudoholomorphic curves along branched covered cylinders I, J. Sympl. Geom. 5 (2007), 42-137.
\item[] [KM] P. Kronheimer and T. Mrowka, Monopoles and three-manifolds, Cambridge University Press, Cambridge, UK, 2007.
\item[] [KT] C. Kutluhan and C. H. Taubes, The Seiberg-Witten-Floer homology and symplectic forms on $S^{1} \times M^{3}$, Geom. Topol. 13 (2009), 493-525.
\item[] [L1] Y. J. Lee, From Seiber-Witten to Gromov: manifolds with cylindrical ends, in preparation.
\item[] [L2] Y. J. Lee, Reidemeister torsion in Floer-Novikov theory and counting pseudoholomorphic tori, I. J. Sympl. Geom. 3 (2005), 221-311.
\item[] [MT] G. Meng and C. H. Taubes, $\underline{S W}=$ Milnor torsion, Math. Res. Lett. 2 (1995), 221-238.
\item[] [Q] D. Quillen, Determinants of Cauchy-Riemann operators over a Riemann surface, Funktsional Anal. i. Prilozhen. 19 (1985), 37-41.
\item[] [S] D. Salamon, Seiberg-Witten invariants of mapping tori, symplectic fixed points, and Lefschetz numbers, Turkish J. Math. 23 (1999), 117-143.
\item[] [T1] C. H. Taubes, Embedded contact homology and Seiberg-Witten-Floer cohomology I, Geom. Topol. 14 (2010), 2497-2582.
\item[] [T2] C. H. Taubes, Embedded contact homology and Seiberg-Witten-Floer cohomology II, Geom. Topol. 14 (2010), 2583-2720.
\item[] [T3] C. H. Taubes, Embedded contact homology and Seiberg-Witten-Floer cohomology III, Geom. Topol. 14 (2010), 2721-2818.
\item[] [T4] C. H. Taubes, Embedded contact homology and Seiberg-Witten-Floer cohomology IV, Geom. Topol. 14 (2010), 2819-2960.
\item[] [T5] C. H. Taubes, Embedded contact homology and Seiberg-Witten-Floer cohomology V, Geom. Topol. 14 (2010), 2961-3000.
\item[] [T6] C. H. Taubes, Seiberg-Witten and Gromov invariants for symplectic 4-manifolds, International Press, Somerville, MA, 2005.
\item[] [T7] C. H. Taubes, The Seiberg-Witten equations and the Weinstein conjecture, Geom. Topol. 11 (2007), 2117-2202.
\item[] [T8] C. H. Taubes, Asymptotic spectral flow for Dirac operators, Commun. Anal. Geom. 15 (2007), 569-587.
\item[] [T9] C. H. Taubes, The Seiberg-Witten equations and the Weinstein conjecture II: More closed integral curves for the Reeb vector field, Geom. Topol. 13 (2009), 1337-1417
\end{itemize}

Department of Mathematics
Harvard University
Cambridge, MA 02138
E-mail address: chtaubes@math.harvard.edu
Received 06/26/2009, accepted 06/8/2011
The authors owe a debt of gratitude to Michael Hutchings for sharing his knowledge of periodic Floer homology and for his thoughts about the correspondence between the latter and the Seiberg-Witten-Floer homology. We also thank Andrew Cotton-Clay for pointing out Corollary 1.3 and other helpful comments.

Both authors were supported in part by NSF grants.