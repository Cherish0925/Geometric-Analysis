---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 2011_12666.pdf
converter: mathpix
format: mmd
---

\title{
Angle deformation of Kähler-Einstein edge metrics on Hirzebruch surfaces
}

\author{
Yanir A. Rubinstein, Kewei Zhang
}

30 June 2020

Dedicated to Bernie Shiffman on the occassion of his retirement

\begin{abstract}
We construct a family of Kähler-Einstein edge metrics on all Hirzebruch surfaces using the Calabi ansatz and study their angle deformation. This allows us to verify in some special cases a conjecture of Cheltsov-Rubinstein that predicts convergence towards a non-compact Calabi-Yau fibration in the small angle limit. We also give an example of a Kähler-Einstein edge metric whose edge singularity is rigid, answering a question posed by Cheltsov.
\end{abstract}

\section*{1 Introduction}

Recently, Cheltsov-Rubinstein [4] put forward a conjectural picture in which non-compact Calabi-Yau fibrations emerge as the small angle limit of families of compact singular metrics known as Kähler edge metrics. In a recent article, we verfied this picture in the most elementary setting of Riemann surfaces [12]. Our goal in the present article is to give further evidence for the conjecture by verifying it for some special symmetric complex surfaces. In passing, we also answer a question of Cheltsov by proving the existence of a rigid Kähler-Einstein edge metric.

Let $M$ be a smooth complex projective manifold and let $D=D_{1}+\ldots+D_{r}$ be a simple normal crossing divisor in $M$. Following Tian [14, p. 147], a Kähler metric on $M$ with an edge singularity along a divisor $D \subset M$ is a smooth Kähler metric on $M \backslash D$ that has a cone singularity transverse to $D$ ('bent' at an angle $2 \pi \beta_{i}<2 \pi$ along $D_{i}$ ). Such metrics are called Kähler edge metrics; we refer to [9] for geometric analysis on such spaces and to [11] for a detailled survey and further references.

In op. cit. [4] one is concerned with small cone angle Kähler edge metrics that are also Einstein, called Kähler-Einstein edge (KEE) metrics and of positive Ricci curvature. For such metrics to exist it is necessary that $(M, D)$ be asymptotically log Fano [4, Definition 1.1], a positivity property generalizing positivity of the first Chern class (i.e., being Fano) in the sense that $c_{1}(M)-\sum_{i=1}^{r}\left(1-\beta_{i}(j)\right) D_{i}$ is positive for a sequence $\beta(j)=\left(\beta_{1}(j), \ldots, \beta_{r}(j)\right) \in(0,1)^{r}$ tending to the origin (being Fano corresponds to the other 'extreme' with $\beta_{1}=\ldots=\beta_{r}=1$ or alternatively there being no divisor, i.e., $D=0$ ). Assuming then that $(M, D)$ is asymptotically log Fano and that it admits KEE metrics $\left\{\omega_{\beta(j)}\right\}_{j \in \mathbb{N}}$ with angles $\beta_{i}(j)$ along $D_{i}$, it is conjectured there that by taking an appropriate limit these metrics will converge to a Calabi-Yau fibration on the non-compact space $M \backslash D$ [4, Conjecture 1.11].

Conjecturally, the fibration may be described in terms of the adjoint anticanonical linear system as follows. Let $K_{M}$ denote the canonical bundle, so that $c_{1}(M)=-c_{1}\left(K_{M}\right)$ by definition. By our assumption $-K_{M}-D$ is nef as it is a limit of ample divisors. Let
$d=\operatorname{dim} H^{0}\left(M,-K_{M}-D\right)$ and let $s_{1}, \ldots, s_{d}$ be a basis for the vector space $H^{0}\left(M,-K_{M}-D\right)$. The Kodaira map
$$M \ni z \mapsto\left[s_{1}(z): \ldots: s_{d}(z)\right] \in \mathbb{P}^{d-1},$$
is then a holomorphic map from $M$ onto its image, a projective variety we denote by $Y \subset \mathbb{P}^{d-1}$. Denote by $\kappa:=\operatorname{dim} Y$. It was conjectured [4, Conjecture 1.6] that $\kappa<\operatorname{dim} M$ (under the assumption that the KEE metrics $\omega_{\beta}$ exist for small $\beta$ ), or equivalently that $\left(K_{M}+D\right)^{\operatorname{dim} M}=0$, and this was established in dimension 2 [5] and subsequently in all dimensions [6]. The next step in the program described in [4] is to study the geometric limit, if such exists, of such KEE metrics when the angles tend to zero. More precisely, we are interested in the following conjecture [4, Conjecture 1.8] (as customary, when discussing dimension 2 we will use 'del Pezzo' instead of 'Fano', and replace $(M, D)$ by $(S, C)$ ):

Conjecture 1.1. Let $C=C_{1}+\ldots+C_{r} \nsim-K_{S}$ be a disjoint union of smooth curves in a projective surface $S$ such that $(S, C)$ is strongly asymptotically log del Pezzo. Let $\beta \in(0,1)^{r}$ be a sequence tending to the origin and suppose that there exist Kähler-Einstein edge metrics $\omega_{\beta}$ of angle $2 \pi \beta_{i}$ along $D_{i}$ and of positive Ricci curvature. Then as $\beta \rightarrow 0$ an appropriate limit of $\omega_{\beta}$ converges to a fibration of cylinders whose base is $\mathbb{P}^{1}$.

In fact, by general results of Kawamata and Shokurov $C$ can have at most two connected components, so that $r \in\{1,2\}$ [4, Remark 3.7]. Note that part of the challenge is to identify what exactly "appropriate" means in Conjecture 1.1. As we show in this note the appropriate sense, at least in some cases, turns out to be rescaling the fibers of the fibration (1.1) in a precise way and considering a certain pointed Gromov-Haussdorff limit, inspired by the asymptotic analysis in the Riemann surface case [12]. Moreover, we also show that the un-rescaled limit exists as a collapsed Gromov-Haussdorff limit, and is the Kähler-Einstein metric on the base $Y$ (in this case the Fubini-Study metric on $\mathbb{P}^{1}$ ). We believe this should generalize to the setting of Conjecture 1.1.

In this note we concentrate on a particular family of $(S, C)$ as in Conjecture 1.1 and first construct rather explicitly the sequence of KEE metrics $\omega_{\beta}$ for a sequence of small angles $\beta \in(0,1)^{2}$ tending to zero. Moreover, we analyze the small angle limit of this sequence and resolve Conjecture 1.1 for this family of pairs. The pairs we consider are
$$S=\mathbb{F}_{n}, n \in \mathbb{N} \cup\{0\}, \quad C_{1}=Z_{n}, C_{2} \in\left|Z_{n}+n F\right|,$$
where $\mathbb{F}_{n}$ is the $n$-th Hirzebruch surface [7], $C_{1}$ is the $-n$-curve, and $C_{2}$ is an $n$-curve; see \$2.3 and §3.3 for notation and precise definitions. The 'boundary' in these pairs consists of two disjoint components $C_{1}$ and $C_{2}$ which in some senses is an added difficulty, however, the pairs (1.2) have the advantage of being toric (by which we mean that $S$ is toric and each $C_{i}$ is a torus-invariant holomorphic curve in $S$ ), and in fact the pairs even admit the larger symmetry group of the Calabi ansatz. The simplest sub-case, $n=0$, serves as a general guide, and, in fact, as a nice bridge to our previous 1-dimensional work [12]. In the $n=0$ case, the boundary consists of two disjoint fibers in $\mathbb{P}^{1} \times \mathbb{P}^{1}$ and while the class $-K_{\mathbb{P}^{1} \times \mathbb{P}^{1}}-\left(1-\beta_{1}\right) C_{1}-\left(1-\beta_{2}\right) C_{2}$ is ample for all small $\beta_{1}$ and $\beta_{2}$, only the classes with $\beta_{1}=\beta_{2}$ admit KEE metrics which we denote by $\omega_{\beta_{1}, \beta_{1}}$. This is reminiscent of the situation for footballs, and for a good reason. In fact the reason that only the classes with $\beta_{1}=\beta_{2}$ admit KEE metrics is that if $\beta_{1} \neq \beta_{2}$ then $\mathbb{P}^{1}$ admits a conic Ricci soliton football metric with angles $2 \pi \beta_{1}$ at the North pole and $2 \pi \beta_{2}$ at the South pole (see, e.g., [12, §2]). Taking the product with the Fubini-Study metric on $\mathbb{P}^{1}$ we see that $\left(\mathbb{P}^{1} \times \mathbb{P}^{1}, C_{1}+C_{2}\right)$ admits a Kähler-Ricci soliton edge metric with nontrivial vector field, hence cannot admit a KEE metric. When $\beta_{1}=\beta_{2}$, the KEE metric $\omega_{\beta_{1}, \beta_{1}}$ is nothing
but the product of the volume one Fubini-Study metric on the base $Y=\mathbb{P}^{1}$ and the volume $4 \pi \beta_{1}$ constant scalar curvature conic metric, i.e., the football, on the fibers. Then, our previous work [12, Theorem 1.3] shows that after rescaling the fiber metrics by $1 / \beta_{1}^{2}$ there is a pointed Gromov-Haussdorff limit that converges to the product space $\left(\mathbb{P}^{1} \times \mathbb{C}^{\star}, \pi_{1}^{*} \omega_{\mathrm{FS}}+C \pi_{2}^{*} \omega_{\mathrm{Cyl}}\right)$ for some $C>0$. In fact, this can also be shown by elementary complex analysis (op. cit. is concerned with the more general setting of Ricci solitons).

When $n>0$ the results of [12] do not apply as the situation is no longer a product one and we need different tools. First, we describe some of the well-known Calabi ansatz computations that reduce the KEE equation to an ODE. These are classical when there are no edges, and as we show using the asymptotic expansion of [9, Theorem 1] they generalize naturally to the setting of edges. Similarly to the case $n=0$ it turns out there is a relation between $\beta_{1}$ and $\beta_{2}$ that is necessary and sufficient for the class $-K_{\mathbb{F}_{n}}-\left(1-\beta_{1}\right) C_{1}-\left(1-\beta_{2}\right) C_{2}$ to admit a KEE representative $\omega_{\beta_{1}, \beta_{2}}$. Moreover, $\beta_{2} \rightarrow 0$ as $\beta_{1} \rightarrow 0$ and moreover $\lim _{\beta_{1} \rightarrow 0} \beta_{2} / \beta_{1}=1$. We then generalize the asymptotic analysis from $n=0$ to prove Conjecture 1.1 for the pairs (1.2) by analyzing rather explicitly such sequences of KEE metrics $\omega_{\beta_{1}, \beta_{2}}$ using the Calabi ansatz.

Theorem 1.2. Consider the pairs (1.2). Then for each $n \in \mathbb{N}$ :
- There exists a family of KEE metrics $\omega_{\beta_{1}, \beta_{2}}$ on the pairs (1.2) for each
$$\left(\beta_{1}, \beta_{2}\right)=\left(\beta_{1}, \frac{1}{2 n}\left(n \beta_{1}-3+\sqrt{3\left(3-n \beta_{1}\right)\left(1+n \beta_{1}\right)}\right)\right), \quad \text { for all } \beta_{1} \in(0,2 / n) \cap(0,1],$$
with $\omega_{\beta_{1}, \beta_{2}}$ cohomologous to
$$\frac{2+n \beta_{2}}{2-n \beta_{1}}\left[C_{2}\right]-\left[C_{1}\right] .$$
- As $\beta_{1}$ tends to zero, $\left(\mathbb{F}_{n}, \omega_{\beta_{1}, \beta_{2}}\right)$ converges in the Gromov-Haussdorff sense to $\left(\mathbb{P}^{1}, n \omega_{\mathrm{FS}}\right)$, where $\omega_{\mathrm{FS}}$ is the Fubini-Study metric. Moreover, on the level of tensors, as $\beta_{1}$ tends to zero, $\omega_{\beta_{1}, \beta_{2}}$ restricted to $\mathbb{F}_{n} \backslash\left(C_{1} \cup C_{2}\right)$ converges in all $C^{k}$ norms to a degenerate tensor that is the pull-back of $n \omega_{\mathrm{FS}}$ on $\mathbb{P}^{1}$ under the projection map to the zero section of the natural fibration $\pi_{1}: \mathbb{F}_{n} \rightarrow \mathbb{P}^{1}$.
- The fiberwise-rescaled metrics $\widetilde{\omega_{\beta_{1}, \beta_{2}}}$ obtained by rescaling by $\beta_{1}^{-2}$ only the restriction of $\omega_{\beta_{1}, \beta_{2}}$ to each fiber (of the projection to $\mathbb{P}^{1}$ ) converges in $C^{k}$ on compact subsets as well as in the pointed Gromov-Haussdorff sense to a cylinder fibration over $\mathbb{P}^{1},\left(\mathbb{P}^{1} \times \mathbb{C}^{\star}, n \pi_{1}^{*} \omega_{\mathrm{FS}}+n \pi_{2}^{*} \omega_{\mathrm{Cyl}}\right)$, i.e.,
$$\lim _{\beta_{1} \rightarrow 0} \widetilde{\omega_{\beta_{1}, \beta_{2}}}=n\left(\pi_{1}^{*} \omega_{\mathrm{FS}}+\pi_{2}^{*} \omega_{\mathrm{Cyl}}\right),$$
where $\omega_{\mathrm{Cyl}}$ is the flat metric on $\mathbb{C}^{\star}$, and $\pi_{i}$ is the projection on to the $i$-th factor.
Remark 1.3. In the third statement of Theorem 1.2 there is a certain choice of coordinates $(Z, w)$ on $\mathbb{F}_{n} \backslash\left(C_{1} \cup C_{2}\right)$ (see (3.3)) which then determines projection maps $\pi_{1}$ and $\pi_{2}$. Thus, the limit is only unique up to automorphisms of $\mathbb{P}^{1} \times \mathbb{C}^{*}$.

In 2015, Cheltsov posed the following question [3].
Question 1.4. Let $D$ be a smooth connected divisor in a smooth variety $X$, and let $\beta \in(0,1)$. Does there exists a triple $(X, D, \beta)$ such that $(X, D)$ admits a KEE metric of positive Ricci curvature and angle $2 \pi \beta$ along $D$ but does not admit KEE metrics of angles $2 \pi \alpha$ along $D$ for any $(0,1) \ni \alpha \neq \beta$ ?

Observe that Cheltsov's question becomes interesting in dimension two and above since there does not exist a constant scalar curvature conic Riemann sphere with a single cone point. We answer question 1.4 affirmatively.

Corollary 1.5. Let $Z_{-1}$ be a smooth curve of self-intersection 1 disjoint from the -1-curve in the first Hirzebruch surface $\mathbb{F}_{1}$. The pair $\left(\mathbb{F}_{1}, Z_{-1}\right)$ admits a KEE metric of angle $2 \pi \beta \in(0,2 \pi]$ along $Z_{-1}$ if and only if $\beta=\sqrt{3}-1$.

Proof. The existence statement for $n=1$ and $\beta_{1}=1$ follows from Theorem 1.2 (or from Corollary 4.1) which implies that then $\beta_{2}=\sqrt{3}-1$. This gives a KEE metric with angle $2 \pi(\sqrt{3}-1)$ along $Z_{-1}$ and smooth elsewhere. This KEE metric cannot be deformed to have an edge singularity along the infinity section. Indeed, by [5, Example 2.8] the pair $\left(\mathbb{F}_{1}, Z_{-1}\right)$ does not admit KEE metrics for any angle smaller than $\sqrt{3}-1$ because $Z_{-1} \log$ slope destabilizes it, and neither for any angle larger than $\sqrt{3}-1$ because $Z_{1} \log$ slope destabilizes it. This proves Theorem 1.5. \(\square\)

The metric of Corollary 1.5 is quite remarkable in that it is in fact perhaps the first example of an "isolated" KEE metric whose edge singularity cannot be deformed at all.

\subsection*{1.1 Organization}

In Section 2, we provide several useful viewpoints of Hirzebruch surfaces for the reader's convenience. In Section 3, we characterize Kähler edge metrics on Hirzebruch surfaces (Proposition 3.3) using the Calabi ansatz and the asymptotic analysis of [9]. In Section [4, we solve explicitly the Kähler-Einstein edge equation and determine the corresponding angles along the boundary divisors (Corollary 4.1). We emphasize that the reader that is only interested in Corollary 1.5 can skip Section 5 as Corollary 1.5 follows directly from Corllary 4.1. Finally, in Section 5, we study the small angle limits of the Kähler-Einstein edge metrics and prove Theorem 1.2.

\section*{2 Several descriptions of Hirzebruch surfaces}

\subsection*{2.1 The quotient singularity}

Let $n \in \mathbb{N}$. The simplest singularity in complex geometry is the quotient singularity constructed as follows. Let $\mathbb{Z}_{n}$ act on $\mathbb{C}^{2}$ by the diagonal action, so that the $\mathbb{Z}_{n}$-orbit of a point $\left(a_{1}, a_{2}\right)$ is the collection of $n$ points
$$\left\{\left(e^{2 \pi \sqrt{-1} l / n} a_{1}, e^{2 \pi \sqrt{-1} l / n} a_{2}\right) \in \mathbb{C}^{2}: l=0, \ldots, n-1\right\} .$$
This is always a collection of $n$ distinct points, unless $\left(a_{1}, a_{2}\right)=(0,0)$. So if we consider the orbit space (or quotient space)
$$\mathbb{C}^{2} / \mathbb{Z}_{n}$$
defined, as a set, as $\mathbb{C}^{2}$ quotiented by the equivalence relation
$$\begin{aligned}
& \left(a_{1}, a_{2}\right) \sim\left(b_{1}, b_{2}\right) \text { if there is some } l \in\{0, \ldots, n-1\} \\
& \text { such that } a_{1}=e^{2 \pi \sqrt{-1} l / n} b_{1} \text { and } a_{2}=e^{2 \pi \sqrt{-1} l / n} b_{2}(\text { with the same } l),
\end{aligned}$$
we obtain an orbifold, smooth on the complement of a single singular point.

\subsection*{2.2 Blow-up description of the total space}

In the remainder of this note we always assume
$$n \in \mathbb{N},$$
since the case $n=0$ was treated in the Introduction. We resolve the quotient singularity by blowing up $\mathbb{C}^{2} / \mathbb{Z}_{n}$ at the single singular point. Next we give an alternative global description of the resulting resolution.

Denote by
$$\operatorname{Bl}_{0}\left(\mathbb{C}^{2} / \mathbb{Z}_{n}\right)$$
the blow-up at the origin of (the orbifold, if $n \geq 2$ ) $\mathbb{C}^{2} / \mathbb{Z}_{n}$. Denote by $H \rightarrow \mathbb{P}^{1}$ the hyperplane bundle over $\mathbb{P}^{1}$ and by $H^{*} \rightarrow \mathbb{P}^{1}$ the dual (tautological) line bundle. Then by
$$-n H_{\mathbb{P}^{1}}$$
we denote the (2-dimensional) total space of $-n H \equiv\left(H^{*}\right)^{\otimes n}$ considered as a line bundle over $\mathbb{P}^{1}$. The following is an elementary exercise.

Lemma 2.1. $\mathrm{Bl}_{0}\left(\mathbb{C}^{2} / \mathbb{Z}_{n}\right)$ is biholomorphic to $-n H_{\mathbb{P}^{1}}$.

\subsection*{2.3 Compactifying at infinity}

By adding a point at infinity in each $\mathbb{C}$ fiber (in the $-k H_{\mathbb{P}^{1}}$ description) we obtain a compact space, a $\mathbb{P}^{1}$ fibration over $\mathbb{P}^{1}$. The space is equivalently obtained by taking a product of each $\mathbb{C}$ fiber with another copy of $\mathbb{C}$ and then taking the quotient under the $\mathbb{C}^{*}$ action on the $\mathbb{C}^{2}$ fibers (but not acting on the base). This space is often denoted by
$$\mathbb{P}\left(-n H_{\mathbb{P}^{1}} \oplus \mathbb{C}_{\mathbb{P}^{1}}\right),$$
and we will simply denote it by
$$\mathbb{F}_{n},$$
for any $n \geq 0$. In effect, we have added a copy of $\mathbb{P}^{1}$. We therefore have two distinguished divisors in the space: the zero section
$$Z_{n}:=\{w=0\}$$
(the exceptional divisor in the blow-up description) and the infinity section
$$Z_{-n}:=\{w=\infty\} .$$
By construction the two do not intersect. We emphasize that
$$Z_{n} \text { is the }-n \text {-curve and } Z_{-n} \text { is the "section at infinity"; }$$
$Z_{n}$ can be contracted to give rise to the weighted projective space $\mathbb{P}(1,1, n)$.
We can take (2.4) as the definition of $\mathbb{F}_{n}$. In that case it actually makes sense for any $n \in \mathbb{Z}$. And, since for any vector bundle $A$ and line bundle $L$ we have $\mathbb{P}(A \otimes L)=\mathbb{P}(A)$, it follows that $\mathbb{F}_{-n}$ is biholomorphic to $\mathbb{F}_{n}$ (take $L=2 n H_{\mathbb{P}^{1}}$ ) with the biholomorphism exchanging the zero and the infinity sections (i.e., $Z_{n}$ with $Z_{-n}$ ). Recalling Lemma 2.1 we have shown the following:

Lemma 2.2. $\mathbb{F}_{n} \backslash Z_{-n}$ is biholomorphic to $\mathrm{Bl}_{0}\left(\mathbb{C}^{2} / \mathbb{Z}_{n}\right)$.
Lemma 2.3. $\operatorname{dim} H_{\bar{\partial}}^{1,1}\left(\mathbb{F}_{n}\right)=2$.
Proof. By [7],
$$\mathbb{F}_{n} \underset{\text { diffeo. }}{\cong} \begin{cases}S^{2} \times S^{2}, & n \text { even, } \\ \mathbb{P}^{2} \# \overline{\mathbb{P}^{2}}, & n \text { odd. }\end{cases}$$
So one has $\operatorname{dim} H^{2}\left(\mathbb{F}_{n}, \mathbb{C}\right)=2$. Thus $2 \operatorname{dim} H_{\bar{\partial}}^{2,0}\left(\mathbb{F}_{n}\right)+\operatorname{dim} H_{\bar{\partial}}^{1,1}\left(\mathbb{F}_{n}\right)=2$, so it follows that $\operatorname{dim} H_{\bar{\partial}}^{1,1}\left(\mathbb{F}_{n}\right)$ is either 0 or 2. The former possibility is excluded since $Z_{n} \cong \mathbb{P}^{1}$ is a non-trivial holomorphic (1, 1)-cycle. \(\square\)

Remark 2.4. We will explicitly construct (1,1)-forms in Section 3.3 below which gives an alternative direct description why $\operatorname{dim} H_{\bar{\partial}}^{1,1}\left(\mathbb{F}_{n}, \mathbb{Z}\right) \geq 2$ hence equal to 2 . In fact, we will construct explicit representatives for each Kähler class.

\section*{3 Edge metrics on Hirzebruch surfaces}

\subsection*{3.1 Edge metrics on powers of the tautological line bundle}

In this section we elaborate on Remark 2.4 and give a geometric approach to compactification.
We start by constructing some $U(2)$-invariant Kähler edge metrics on $-n H_{\mathbb{P}^{1}}$ (2.3). The construction goes back to Calabi [1, 2] who considered the case of smooth Kähler metrics. The generalization to the edge case is not much harder.

Consider the Hermitian metric $h$ on $-H$ that assigns to each point in the total space $(Z, w)$ the norm squared
$$|(Z, w)|_{h}^{2}:=|w|^{2}\|Z\|^{2}=|w|^{2}\left(\left|Z_{1}\right|^{2}+\left|Z_{2}\right|^{2}\right),$$
i.e., locally
$$h(Z)=\|Z\|^{2},$$
where $\|Z\|$ is the Euclidean norm of the vector $\left(Z_{1}, Z_{2}\right)$ in $\mathbb{C}^{2}$. Similarly, $h^{n}$ is a metric on $-n H$ and
$$|(Z, w)|_{h^{n}}^{2}:=|w|^{2}\|Z\|^{2}=|w|^{2}\left(\left|Z_{1}\right|^{2}+\left|Z_{2}\right|^{2}\right)^{n},$$
and
$$h^{k}(Z)=\left(\left|Z_{1}\right|^{2}+\left|Z_{2}\right|^{2}\right)^{k} .$$
On the chart $Z_{2} \neq 0$, we choose local holomorphic coordinates $z:=Z_{1} / Z_{2}$, so that
$$Z=\left[Z_{1}: Z_{2}\right]=[z: 1] .$$
The curvature of this metric is a Kähler form on the base (i.e., the zero section $Z_{n} \cong \mathbb{P}^{1}$ ) which is given by
$$\begin{aligned}
-\sqrt{-1} \partial \bar{\partial} \log h^{n} & =-n \sqrt{-1} \partial \bar{\partial} \log \|Z\|^{2}=-n \sqrt{-1} \partial \bar{\partial} \log \left(1+|z|^{2}\right)^{2} \\
& =-n\left(1+|z|^{2}\right)^{-2} \sqrt{-1} d z \wedge \overline{d z}=-n \omega_{\mathrm{FS}} .
\end{aligned}$$
In the sequel, we will use the above curvature property of $h^{n}$, as well as the fact that it is a globally defined $U(2)$-invariant smooth function on $\operatorname{Bl}_{0}\left(\mathbb{C}^{2} / \mathbb{Z}_{n}\right)$.

\subsection*{3.2 The Calabi ansatz on the total space}

We use the logarithm of the global invariant function from above as our coordinate from now on. That is, we set
$$s(Z, w):=\log |(Z, w)|_{h^{n}}^{2}=\log |w|^{2}+n \log \left(1+|z|^{2}\right), \quad(Z, w) \in-n H_{\mathbb{P}^{1}},$$
and seek canonical Kähler metrics on $\mathrm{Bl}_{0}\left(\mathbb{C}^{2} / \mathbb{Z}_{n}\right)$ that depend solely on $s$, namely, Kähler metrics of the form
$$\eta=\sqrt{-1} \partial \bar{\partial} f(s),$$
where $f$ is a smooth function. Our goal will be to determine appropriate $f$ that make $\eta$ have various desirable curvature properties and edge type singularities along $Z_{ \pm n}$.

Denote
$$f^{\prime}(s):=\frac{d f}{d s} .$$
Note,
$$\frac{\partial s}{\partial w}=\frac{1}{w}, \quad \frac{\partial s}{\partial Z_{i}}=n \frac{\overline{Z_{i}}}{\|Z\|^{2}}, \quad i=1,2 .$$
Working on the chart $Z_{2}=1$ (recall (3.1)),
$$\left(\begin{array}{cc}
\frac{\partial^{2} f}{\partial w \partial \bar{w}} & \frac{\partial^{2} f}{\partial w \partial \bar{z}} \\
\frac{\partial^{2} f}{\partial z \partial \bar{w}} & \frac{\partial^{2} f}{\partial z \partial \bar{z}}
\end{array}\right)=\left(\begin{array}{cc}
\frac{f^{\prime \prime}}{|w|^{2}} & \frac{n f^{\prime \prime} z}{w\left(|z|^{2}+1\right)} \\
\frac{n f^{\prime \prime} \bar{z}}{\bar{w}\left(|z|^{2}+1\right)} & \frac{n f^{\prime}+n^{2} f^{\prime \prime}|z|^{2}}{\left(|z|^{2}+1\right)^{2}}
\end{array}\right)$$
Set
$$\pi_{1}(Z, w):=z, \quad \pi_{2}(Z, w):=w,$$
and denote by $\omega_{\mathrm{FS}}$ the Fubini-Study metric on $\mathbb{P}^{1}$ and the flat Kähler form on the cylinder $\mathbb{C}^{\star}$ by
$$\omega_{\mathrm{Cyl}}:=\frac{\sqrt{-1} d w \wedge d \bar{w}}{|w|^{2}} .$$
Thus,
$$\begin{aligned}
\eta= & n f^{\prime} \pi_{1}^{*} \omega_{\mathrm{FS}}+f^{\prime \prime} \pi_{2}^{*} \omega_{\mathrm{Cyl}} \\
& +n \frac{f^{\prime \prime}}{1+|z|^{2}}\left(\sqrt{-1} \frac{d w}{w} \wedge z \overline{d z}+\sqrt{-1} \bar{z} d z \wedge \frac{\overline{d w}}{\bar{w}}\right) \\
& +n^{2} f^{\prime \prime}(s)\left(1+|z|^{2}\right)^{-2} \bar{z} d z \wedge z \overline{d z} .
\end{aligned}$$
From this computation we see that the two key quantities are $f^{\prime}$ and $f^{\prime \prime}$ (rather than $f$ itself). Both of these must be positive, i.e., $f$ must be an increasing convex function of $s$. Inspired by this, consider a Legendre type change of variables going back to Calabi [1] (cf. [8]; see [12] for a reference most closely following our notation):
$$\tau=\tau(s):=f^{\prime}(s), \quad \varphi=\varphi(\tau)=\varphi(\tau(s)):=f^{\prime \prime}(s), \quad \tau \in \operatorname{Im} f^{\prime}=f^{\prime}(\mathbb{R}) .$$
Setting
$$\alpha:=n \frac{\bar{z} d z}{1+|z|^{2}},$$
and using (3.6), we may rewrite (3.5) as
$$\eta=n \tau \pi_{1}^{*} \omega_{\mathrm{FS}}+\varphi\left(\pi_{2}^{*} \omega_{\mathrm{Cyl}}+\sqrt{-1} \alpha \wedge \bar{\alpha}+\sqrt{-1} \alpha \wedge \overline{d w / w}+\sqrt{-1} d w / w \wedge \bar{\alpha}\right) .$$

\subsection*{3.3 Kähler classes}

By construction, the normal bundle of $Z_{ \pm n}$ is $\mathcal{O}_{\mathbb{P}^{1}}(\mp n)=\mp n H_{\mathbb{P}^{1}}$, so
$$Z_{ \pm n}^{2}=\mp n, \quad Z_{n} \cdot Z_{-n}=0 .$$
It follows from this and Lemma 2.3 that $Z_{n}$ and $Z_{-n}$ generate the Picard group, and thus by the Nakai-Moishezon criterion the Kähler classes are precisely represented by $-x Z_{n}+y Z_{-n}$ with $y>x>0$ (this also follows directly from the Calabi ansatz). The divisor class
$$F:=\frac{1}{n}\left(Z_{-n}-Z_{n}\right),$$
has zero self intersection and intersects $Z_{ \pm n}$ exactly at one point, hence represents the fibers of the projection to the base $Z_{n}$. Setting
$$C_{1}=Z_{n}, \quad C_{2}=Z_{-n},$$
and using (3.9) we recover the notation (1.2). The canonical class can be determined as follows. Write $K_{\mathbb{F}_{n}}=-x Z_{n}+y Z_{-n}$. By Riemann-Roch,
$$-2=\left(K_{\mathbb{F}_{n}}+Z_{ \pm n}\right) \cdot Z_{ \pm n}=\left((1-x) Z_{n}+y Z_{-n}\right) \cdot Z_{n}=-n(1-x)=\left(Z_{n}+(1+y) Z_{-n}\right) \cdot Z_{-n}=n(1+y),$$
so $x=1-2 / n, y=-1-2 / n$, and
$$-K_{\mathbb{F}_{n}} \sim\left(1-\frac{2}{n}\right) Z_{n}+\left(1+\frac{2}{n}\right) Z_{-n} \sim 2 Z_{n}+(n+2) F .$$

\subsection*{3.4 The angle constraint as boundary data}

We rewrite the angle constraint in terms of $\tau$. Note that the domain of $\tau$ is
$$\operatorname{Im} f^{\prime}=\left(\inf f^{\prime}, \sup f^{\prime}\right),$$
and $\tau$ must be positive so $\inf f^{\prime} \geq 0$.
Lemma 3.1. Suppose that $\eta$ restricts to a Riemannian metric on $E$. Then, $\inf f^{\prime}>0$.
Proof. If $\inf f^{\prime}=0$, then by (3.5) and (2.6) the restriction of $\eta$ to $E$ is identically zero, which means the zero section is collapsed to a point, a contradiction. \(\square\)

To simplify computations we will henceforth assume we are in the situation of Lemma 3.1 and rescale $\eta$, equivalently $f$, by a positive constant so that
$$\inf f^{\prime}=1 .$$
This is equivalent to rescaling the Kähler class of $\eta$. Thus the only contribution to the Poincaré-Lelong formula aside from $\omega_{\mathrm{Cyl}}$ will be from any vanishing of $\varphi$ along $\{w=0\}$ and along $\{1 / w=0\}$.

By construction, $Z_{ \pm n}=\{s=\mp \infty\}$. By our normalization above $\tau$ ranges in the domain $(1, T)$ with
$$Z_{n}=\{\tau=1\} \quad Z_{-n}=\{\tau=T\} .$$

Lemma 3.2. $T<\infty$.

Proof. By assumption $\eta$ is a Kähler edge metric on the pair (1.2). Restricting $\eta$ to a fiber (i.e., say, to the vertical section $\{z=0\}$ ) using (3.8), we get an $S^{1}$-invariant metric
$$g=\frac{1}{2 \varphi(\tau)} d \tau^{2}+2 \varphi(\tau) d \theta^{2}$$
where $w=e^{s / 2+\sqrt{-1} \theta}$ is a coordinate on $\{z=0\}$. This follows in the same way as in the 1-dimensional setting [12, Lemma 2.1]. Note that here we implicitly used the fact that $\eta$ is $U(2)$-invariant, hence its restriction to any fiber is $S^{1}$-invariant. Since for any Kähler edge metric the volume of a complex submanifold is finite (in this case it is a cohomological constant) and since by (3.14) the volume form on the fiber is simply $d \tau \wedge d \theta$, it follows from (3.13) that the volume of the fiber is $2 \pi(T-1)$, that is finite if and only if $T<\infty$. \(\square\)

By our assumption (3.12) and Lemma 3.2, $\tau$ ranges in a domain $(1, T)$ with $T<\infty$. Thus,
$$\lim _{s \rightarrow \pm \infty} \frac{d \tau}{d s}=0,$$
i.e., using (3.6),
$$\varphi(1)=\varphi(T)=0 .$$

Next, we rewrite the angle constraint at the edges in terms of $\tau$.
Proposition 3.3. $\eta$ is a Kähler edge metric on the pair (1.2) with angle $2 \pi \beta_{1}$ along $C_{1}$ and $2 \pi \beta_{2}$ along $C_{2}$ if and only if
$$\varphi(1)=0, \quad \varphi^{\prime}(1)=\beta_{1}, \quad \varphi(T)=0, \quad \varphi^{\prime}(T)=-\beta_{2} .$$
Proof. By (3.15) it remains to determine the derivatives of $\varphi$ at 1 and $T$.
Suppose first that $\eta$ is a Kähler edge metric with angles as stated. It follows from [9, Theorem 1, Proposition 4.4] that $f$ has complete asymptotic expansions both near $w=0$ and $w=\infty$. Let us concentrate on the former first. The leading term in that expansion is $|w|^{2 \beta_{1}}$ and using (3.2),
$$\begin{aligned}
\varphi & \sim C_{1}+C_{2}|w|^{2 \beta_{1}}+\left(C_{3} \sin \theta+C_{4} \cos \theta\right)|w|^{2}+O\left(|w|^{2+\epsilon}\right) \\
& =C_{1}+C_{2} e^{\beta_{1} s}+\left(C_{3} \sin \theta+C_{4} \cos \theta\right) e^{s}+O\left(e^{(1+\epsilon) s}\right)
\end{aligned}$$
(note that $r$ in [9, (56)] is equal to $|w|^{\beta_{1}} / \beta_{1}$ in our notation, see [9, p. 102]). Note that $C_{1}=0$ by (3.15) (actually also $C_{3}=C_{4}=0$ as $\varphi$ is independent of $\theta$ but we do not need this). Moreover, the expansion can be differentiated term-by-term as $|w| \rightarrow 0$ or $s \rightarrow-\infty$. As $\varphi^{\prime}(\tau)=\frac{\partial \varphi}{\partial s} \frac{d s}{d \tau}=\frac{\partial \varphi}{\partial s} / \varphi$, we obtain
$$\varphi(1)=0, \quad \varphi^{\prime}(1)=\beta_{1} .$$
The same arguments imply that
$$\varphi(T)=0, \quad \varphi^{\prime}(T)=-\beta_{2},$$
the minus sign coming from the fact that the leading term in the expansion is now $1 /|w|^{2 \beta_{2}}=$ $e^{-\beta_{2} s}$.

Conversely, suppose that (3.16) holds. Then near $Z_{n}=\{\tau=1\}=\{w=0\}$ there exists a positive smooth function $F(z, w)$ and a positive constant $\delta$ so that
$$\varphi(\tau(z, w))=|w|^{2 \delta} F(z, w) .$$

Using (3.2), $|w|^{2 \delta}=e^{\delta s} /\left(1+|z|^{2}\right)^{\delta}$, and
$$\frac{d}{d \tau}=\frac{1}{\varphi} \frac{d}{d s},$$
so in the notation of (3.19),
$$\begin{aligned}
\varphi_{\tau}(1) & =\lim _{s \rightarrow-\infty} \frac{\frac{d}{d s}\left(F(s) e^{\beta s}\right)}{F(s) e^{\beta s}} \\
& =\lim _{s \rightarrow-\infty} \frac{F^{\prime}(s) e^{\beta s}+\beta F(s) e^{\beta s}}{F(s) e^{\beta s}} \\
& =\beta+\lim _{s \rightarrow-\infty} F^{\prime}(s) / F(s) .
\end{aligned}$$
By assumption, $\lim _{s \rightarrow-\infty} F(s)$ is some positive (finite) number, in particular we must have $\lim _{s \rightarrow-\infty} F^{\prime}(s)=0$ Thus, $d \varphi / d \tau(1)=\delta$ and
$$\delta=\beta_{1} .$$

Now, taking the top wedge product of (3.8) gives,
$$\begin{aligned}
\eta^{2} & =2\left(n \tau \varphi(\tau) \pi_{1}^{*} \omega_{\mathrm{FS}} \wedge \pi_{2}^{*} \omega_{\mathrm{Cyl}}+\varphi^{2}\left(\pi_{2}^{*} \omega_{\mathrm{Cyl}} \wedge \sqrt{-1} \alpha \wedge \bar{\alpha}+\sqrt{-1} \alpha \wedge \overline{d w / w} \wedge \sqrt{-1} d w / w \wedge \bar{\alpha}\right)\right) \\
& =2 n \tau \varphi(\tau) \pi_{1}^{*} \omega_{\mathrm{FS}} \wedge \pi_{2}^{*} \omega_{\mathrm{Cyl}}
\end{aligned}$$
Now (3.4), (3.19) and (3.21) imply that $\eta$ satisfies a complex Monge-Ampère equation with right-hand side equal to a smooth volume form times $1 /|w|^{2-2 \beta_{1}}$ near $Z_{n}$. Thus, [9, Theorem 1] applies and $\eta$ is a Kähler edge metric with a complete asymptotic expansion near $Z_{n}$ (note that op. cit. is stated in the case of a smooth connected divisor but applies verbatim in the case of smooth disjoint divisors). The same arguments apply near $Z_{-n}$ to conclude. \(\square\)

\section*{4 The Einstein constraint}

From the proof of Proposition 3.22 we can derive a formula for the Ricci tensor of $\eta$. Indeed, by (3.22) and the Poincaré-Lelong formula,
$$\operatorname{Ric} \eta=\left(1-\beta_{1}\right)\left[C_{1}\right]+\left(1-\beta_{2}\right)\left[C_{2}\right]+2 \pi_{1}^{*} \omega_{\mathrm{FS}}-\sqrt{-1} \partial \bar{\partial} \log \tau-\sqrt{-1} \partial \bar{\partial} \log \varphi,$$
where the last term is understood to be the restriction of $\sqrt{-1} \partial \bar{\partial} \log \varphi$ to the complement of $C_{1}+C_{2}$. For the remaining terms, compute
$$\begin{aligned}
\partial_{w} \log f^{\prime} & =\frac{f^{\prime \prime}}{f^{\prime}} \frac{\partial s}{\partial w}=\frac{f^{\prime \prime}}{w f^{\prime}} \\
\partial_{z} \log f^{\prime} & =\frac{f^{\prime \prime}}{f^{\prime}} \frac{\partial s}{\partial z}=n \frac{f^{\prime \prime}}{f^{\prime}} \frac{\bar{z}}{1+|z|^{2}} \\
\partial_{w \bar{w}} \log f^{\prime} & =\left(\frac{f^{\prime \prime}}{f^{\prime}}\right)^{\prime} \frac{1}{w} \frac{\partial s}{\partial \bar{w}}=\left(\frac{f^{\prime \prime}}{f^{\prime}}\right)^{\prime} \frac{1}{|w|^{2}} \\
\partial_{z \bar{w}} \log f^{\prime} & =n\left(\frac{f^{\prime \prime}}{f^{\prime}}\right)^{\prime} \frac{\overline{z / w}}{1+|z|^{2}} \\
\partial_{z \bar{z}} \log f^{\prime} & =n^{2}\left(\frac{f^{\prime \prime}}{f^{\prime}}\right)^{\prime} \frac{|z|^{2}}{\left(1+|z|^{2}\right)^{2}}+n \frac{f^{\prime \prime}}{f^{\prime}} \frac{1}{\left(1+|z|^{2}\right)^{2}},
\end{aligned}$$
and this can be simplified by noting that
$$\frac{d \tau}{d s}=f^{\prime \prime}=\varphi(\tau) .$$
Thus,
$$\begin{aligned}
\partial_{w} \log f^{\prime} & =\frac{\varphi}{w \tau} \\
\partial_{z_{i}} \log f^{\prime} & =n \frac{\varphi}{\tau} \frac{\bar{z}}{1+|z|^{2}} \\
\partial_{w \bar{w}} \log f^{\prime} & =\left(\frac{\varphi}{\tau}\right)_{\tau} \frac{\varphi}{|w|^{2}} \\
\partial_{z \bar{w}} \log f^{\prime} & =n\left(\frac{\varphi}{\tau}\right)_{\tau} \varphi \frac{\overline{z / w}}{1+|z|^{2}} \\
\partial_{|z|^{2}} \log f^{\prime} & =n^{2}\left(\frac{\varphi}{\tau}\right)_{\tau} \varphi \frac{|z|^{2}}{\left(1+|z|^{2}\right)^{2}}+n \frac{\varphi}{\tau} \frac{1}{\left(1+|z|^{2}\right)^{2}},
\end{aligned}$$
Next, $\sqrt{-1} \partial \bar{\partial} \log \varphi$ is computed similarly by replacing $f^{\prime}$ by $f^{\prime \prime}$ everywhere. A simplification is obtained by noting that
$$\frac{f^{\prime \prime \prime}}{f^{\prime \prime}}=\frac{\varphi_{\tau} \varphi}{\varphi}=\varphi_{\tau} .$$
Thus,
$$\begin{aligned}
\partial_{w} \log f^{\prime \prime} & =\frac{\varphi_{\tau}}{w} \\
\partial_{z} \log f^{\prime \prime} & =n \frac{\varphi_{\tau} \bar{z}}{1+|z|^{2}} \\
\partial_{w \bar{w}} \log f^{\prime \prime} & =\frac{\varphi_{\tau \tau} \varphi}{|w|^{2}} \\
\partial_{z \bar{w}} \log f^{\prime \prime} & =n \frac{\varphi_{\tau \tau} \varphi \overline{z / w}}{1+|z|^{2}} \\
\partial_{z \bar{z}} \log f^{\prime \prime} & =n^{2} \frac{\varphi_{\tau \tau} \varphi|z|^{2}}{\left(1+|z|^{2}\right)^{2}}+n \varphi_{\tau} \frac{1}{\left(1+|z|^{2}\right)^{2}} .
\end{aligned}$$
Altogether,
$$\begin{aligned}
\sqrt{-1} \partial \bar{\partial} \log \tau=n \varphi / \tau \pi_{1}^{*} \omega_{\mathrm{FS}} & \\
& +\varphi(\varphi / \tau)_{\tau}\left(\pi_{2}^{*} \omega_{\mathrm{Cyl}}+\sqrt{-1} \alpha \wedge \bar{\alpha}\right. \\
& +\sqrt{-1} \alpha \wedge \overline{d w / w}+\sqrt{-1} d w / w \wedge \bar{\alpha} .)
\end{aligned}$$
and
$$\begin{aligned}
\sqrt{-1} \partial \bar{\partial} \log \varphi=n \varphi_{\tau} \pi_{1}^{*} \omega_{\mathrm{FS}} & \\
& +\varphi \varphi_{\tau \tau}\left(\pi_{2}^{*} \omega_{\mathrm{Cyl}}+\sqrt{-1} \alpha \wedge \bar{\alpha}\right. \\
& +\sqrt{-1} \alpha \wedge \overline{d w / w}+\sqrt{-1} d w / w \wedge \bar{\alpha} .)
\end{aligned}$$
So, with $\alpha$ given by (3.7)
$$\begin{aligned}
\operatorname{Ric} \eta=\left(1-\beta_{1}\right)\left[C_{1}\right]+\left(1-\beta_{2}\right)\left[C_{2}\right]+(2 & \left.-n \varphi / \tau-n \varphi_{\tau}\right) \pi_{1}^{*} \omega_{\mathrm{FS}} \\
-\varphi\left(\varphi / \tau+\varphi_{\tau}\right)_{\tau}\left(\pi_{2}^{*} \omega_{\mathrm{Cyl}}+\right. & \sqrt{-1} \alpha \wedge \bar{\alpha} \\
& +\sqrt{-1} \alpha \wedge \overline{d w / w}+\sqrt{-1} d w / w \wedge \bar{\alpha}) .
\end{aligned}$$

The Einstein edge equation
$$\operatorname{Ric} \eta=\lambda \eta+\left(1-\beta_{1}\right)\left[C_{1}\right]+\left(1-\beta_{2}\right)\left[C_{2}\right]$$
becomes, using (3.8) and (4.8), the pair of equations
$$\begin{aligned}
& 2-n \varphi / \tau-n \varphi_{\tau}=n \lambda \tau \\
& -\varphi\left(\varphi / \tau+\varphi_{\tau}\right)_{\tau}=\lambda \varphi .
\end{aligned}$$
Observe that the first equation implies the second by differentiating in $\tau$. Also, setting $\tau=1$ and using (3.16) implies
$$\lambda=\frac{2}{n}-\beta_{1} .$$
Observe that this already puts a constraint, as we must require positive Ricci curvature on $\mathbb{F}_{n} \backslash C$, equivalently
$$\beta_{1} \in\left(0, \frac{2}{n}\right) \cap(0,1] .$$
Thus, the Einstein equation near $Z_{n}$ reduces to the first-order initial value problem
$$\varphi_{\tau}+\frac{\varphi}{\tau}=\frac{2}{n}+\left(\beta_{1}-\frac{2}{n}\right) \tau, \quad \varphi(1)=0 .$$

\subsection*{4.1 Solving the Einstein equation}

Using an integration factor $\tau$ this becomes
$$(\tau \varphi)_{\tau}=\frac{2}{n} \tau+\left(\beta_{1}-\frac{2}{n}\right) \tau^{2}, \quad \varphi(1)=0,$$
so
$$\varphi=\frac{1}{n} \frac{\tau^{2}-1}{\tau}+\frac{1}{3}\left(\beta_{1}-\frac{2}{n}\right) \frac{\tau^{3}-1}{\tau} .$$
Now, for this to correspond to a compact Kähler edge space with angle $2 \pi \beta_{2}$ at $Z_{-n}$ we must satisfy (3.16). To that end, let us determine $T, \varphi(T)$, and $\varphi_{\tau}(T)$ in (3.16) from (4.14). We factor $\varphi$ as
$$\varphi(\tau)=\frac{1}{3}\left(\beta_{1}-\frac{2}{n}\right)(\tau-1)\left(\tau-\alpha_{1}\right)\left(\tau-\alpha_{2}\right) / \tau,$$
with $\alpha_{1} \leq \alpha_{2}$. Then,
$$\frac{1}{3}\left(\beta_{1}-\frac{2}{n}\right)\left(\tau-\alpha_{1}\right)\left(\tau-\alpha_{2}\right)=\frac{1}{3}\left(\beta_{1}-\frac{2}{n}\right)\left(\tau^{2}+\tau+1\right)+\frac{1}{n}(\tau+1),$$
so
$$-\alpha_{1} \alpha_{2}=\alpha_{1}+\alpha_{2}=\frac{1+n \beta_{1}}{2-n \beta_{1}} .$$
By (4.11) we see that $\alpha_{1}<0<\alpha_{2}$, so $T=\alpha_{2}$ if we can show $\alpha_{2}>1$. Solving the quadratic equation for $\alpha_{1}, \alpha_{2}$ gives
$$\begin{aligned}
2 \alpha_{2} & =\frac{1+n \beta_{1}+\left[\left(1+n \beta_{1}\right)^{2}+4\left(1+n \beta_{1}\right)\left(2-n \beta_{1}\right)\right]^{1 / 2}}{2-n \beta_{1}} \\
& =\frac{1+n \beta_{1}+\left[\left(9+6 n \beta_{1}-3 n^{2} \beta_{1}^{2}\right]^{1 / 2}\right.}{2-n \beta_{1}} .
\end{aligned}$$

We claim that $\alpha_{2}>1$. According to (4.16), that amounts to verifying
$$\frac{1+n \beta_{1}+\left[\left(9+6 n \beta_{1}-3 n^{2} \beta_{1}^{2}\right]^{1 / 2}\right.}{2-n \beta_{1}}>2,$$
which, after some manipulation precisely reduces to (4.11), proving the claim.
Finally, it remains to compute the final equation in (3.16), i.e., $\varphi_{\tau}\left(\alpha_{2}\right)$. Using (4.15),
$$\begin{aligned}
\varphi_{\tau}\left(\alpha_{2}\right) & =\frac{1}{3}\left(\beta_{1}-\frac{2}{n}\right)(\tau-1)\left(\tau-\alpha_{1}\right) /\left.\tau\right|_{\tau=\alpha_{2}} \\
& =\frac{1}{3}\left(\beta_{1}-\frac{2}{n}\right)\left(\alpha_{2}-1\right)\left(\alpha_{2}-\alpha_{1}\right) / \alpha_{2} .
\end{aligned}$$
Note that
$$\begin{aligned}
\alpha_{2}-1 & =\frac{\sqrt{3\left(3-n \beta_{1}\right)\left(1+n \beta_{1}\right)}+3\left(n \beta_{1}-1\right)}{4-2 n \beta_{1}}, \\
\frac{\alpha_{2}-\alpha_{1}}{\alpha_{2}} & =\frac{2 \sqrt{3\left(3-n \beta_{1}\right)\left(1+n \beta_{1}\right)}}{1+n \beta_{1}+\sqrt{3\left(3-n \beta_{1}\right)\left(1+n \beta_{1}\right)}},
\end{aligned}$$
Thus,
$$\begin{aligned}
\varphi_{\tau}\left(\alpha_{2}\right)= & \frac{n \beta_{1}-2}{3 n} \frac{\sqrt{3\left(3-n \beta_{1}\right)\left(1+n \beta_{1}\right)}+3\left(n \beta_{1}-1\right)}{4-2 n \beta_{1}} \frac{2 \sqrt{3\left(3-n \beta_{1}\right)\left(1+n \beta_{1}\right)}}{1+n \beta_{1}+\sqrt{3\left(3-n \beta_{1}\right)\left(1+n \beta_{1}\right)}} \\
= & -\frac{1}{3 n} \frac{\sqrt{3\left(3-n \beta_{1}\right)\left(1+n \beta_{1}\right)}\left(\sqrt{3\left(3-n \beta_{1}\right)\left(1+n \beta_{1}\right)}+3\left(n \beta_{1}-1\right)\right)}{1+n \beta_{1}+\sqrt{3\left(3-n \beta_{1}\right)\left(1+n \beta_{1}\right)}} \\
= & -\frac{1}{3 n} \frac{3\left(3-n \beta_{1}\right)\left(1+n \beta_{1}\right)+3\left(n \beta_{1}-1\right) \sqrt{3\left(3-n \beta_{1}\right)\left(1+n \beta_{1}\right)}}{1+n \beta_{1}+\sqrt{3\left(3-n \beta_{1}\right)\left(1+n \beta_{1}\right)}} \\
= & -\frac{1}{3 n}\left[\frac{\left[3\left(3-n \beta_{1}\right)\left(1+n \beta_{1}\right)\right]^{3 / 2}+3\left(n \beta_{1}-1\right) 3\left(3-n \beta_{1}\right)\left(1+n \beta_{1}\right)}{-\left(1+n \beta_{1}\right)^{2}+3\left(3-n \beta_{1}\right)\left(1+n \beta_{1}\right)}\right. \\
& \left.\quad-\frac{3\left(3-n \beta_{1}\right)\left(1+n \beta_{1}\right)^{2}+3\left(n^{2} \beta_{1}^{2}-1\right) \sqrt{3\left(3-n \beta_{1}\right)\left(1+n \beta_{1}\right)}}{-\left(1+n \beta_{1}\right)^{2}+3\left(3-n \beta_{1}\right)\left(1+n \beta_{1}\right)}\right] \\
= & \frac{3-n \beta_{1}}{2 n}+\frac{1}{n} \frac{\sqrt{3\left(3-n \beta_{1}\right)\left(1+n \beta_{1}\right)}\left[3\left(3-n \beta_{1}\right)\left(1+n \beta_{1}\right)-3\left(n^{2} \beta_{1}^{2}-1\right)\right]}{-4 n^{2} \beta_{1}^{2}+8+4 n \beta_{1}} \\
= & \frac{3-n \beta_{1}-\sqrt{3\left(3-n \beta_{1}\right)\left(1+n \beta_{1}\right)}}{2 n}=-\beta_{2} .
\end{aligned}$$

Note that $\beta_{2}=\beta_{2}\left(\beta_{1}\right)<\beta_{1}$ for all $\beta_{1}$. Yet as $\beta_{1}$ tends to zero, $\beta_{2}$ tends to $\beta_{1}$, to wit,
$$\begin{aligned}
\beta_{2} & =\frac{n \beta_{1}-3+3 \sqrt{1+\frac{2}{3} n \beta_{1}-\frac{1}{3} n^{2} \beta_{1}^{2}}}{2 n} \\
& =\frac{1}{2 n}\left(n \beta_{1}-3+3\left(1+\frac{1}{3} n \beta_{1}-\frac{1}{6} n^{2} \beta_{1}^{2}-\frac{1}{8}\left(\frac{2}{3} n \beta_{1}-\frac{1}{3} n^{2} \beta_{1}^{2}\right)^{2}+O\left(\beta_{1}^{3}\right)\right)\right) \\
& =\beta_{1}-\frac{n}{3} \beta_{1}^{2}+O\left(\beta_{1}^{3}\right) .
\end{aligned}$$

Combining all the above together with (3.11), (4.10), and (4.9) we have shown the following.
Corollary 4.1. Let $n \in \mathbb{N}$. For each $\beta_{1} \in(0,2 / n) \cap(0,1]$, there exists a Kähler-Einstein edge metric $\omega_{\beta_{1}, \beta_{2}}$ cohomologous to
$$\frac{2+n \beta_{2}}{2-n \beta_{1}}\left[Z_{-n}\right]-\left[Z_{n}\right] \sim \frac{n\left(\beta_{1}+\beta_{2}\right)}{2-n \beta_{1}}\left[Z_{n}\right]+n \frac{2+n \beta_{2}}{2-n \beta_{1}}[F]$$
on the pair (1.2) with angles $2 \pi \beta_{1}$ along $C_{1}=Z_{n}$ and $2 \pi \beta_{2}=\pi\left(n \beta_{1}-3+\sqrt{3\left(3-n \beta_{1}\right)\left(1+n \beta_{1}\right)}\right) / n$ along $C_{2}=Z_{-n}$. One has $\beta_{2}<\beta_{1}$ and $\lim _{\beta_{1} \rightarrow 0} \beta_{1} / \beta_{2}=1$.

\section*{5 Small angle limits}

In this section we prove Theorem 1.2.
First, let us determine the un-rescaled small angle limit of the KEE metrics $\omega_{\beta_{1}, \beta_{2}}$. By (4.18)
$$\begin{aligned}
\alpha_{2} & =1+3 \frac{\sqrt{1+\frac{2}{3} n \beta_{1}-\frac{1}{3} n^{2} \beta_{1}^{2}}+n \beta_{1}-1}{4-2 n \beta_{1}} \\
& =1+3 \frac{\frac{4}{3} n \beta_{1}-\frac{2}{9} n^{2} \beta_{1}^{2}+O\left(\beta_{1}^{3}\right)}{4-2 n \beta_{1}}=1+n \beta_{1}+\frac{n^{2}}{3} \beta_{1}^{2}+O\left(\beta_{1}^{3}\right),
\end{aligned}$$
while,
$$\begin{aligned}
\alpha_{1} & =1+3 \frac{-\sqrt{1+\frac{2}{3} n \beta_{1}-\frac{1}{3} n^{2} \beta_{1}^{2}}+n \beta_{1}-1}{4-2 n \beta_{1}} \\
& =1+3 \frac{-2+\frac{2}{3} n \beta_{1}+\frac{2}{9} n^{2} \beta_{1}^{2}+O\left(\beta_{1}^{3}\right)}{4-2 n \beta_{1}}=-\frac{1}{2}+\frac{n}{2} \beta_{1}+\frac{5 n^{2}}{12} \beta_{1}^{2}+O\left(\beta_{1}^{3}\right) .
\end{aligned}$$
Recall that $\tau \in\left(1, \alpha_{2}\right)$. Thus, by (5.1) we have $|\tau-1|=O\left(\beta_{1}\right)$. Combining this with (4.15), (5.2), and since by Corollary 4.1 and (3.8), we have that
$$\omega_{\beta_{1}, \beta_{2}}=n \tau \pi_{1}^{*} \omega_{\mathrm{FS}}+\varphi\left(\pi_{2}^{*} \omega_{\mathrm{Cyl}}+\sqrt{-1} \alpha \wedge \bar{\alpha}+\sqrt{-1} \alpha \wedge \overline{d w / w}+\sqrt{-1} d w / w \wedge \bar{\alpha}\right),$$
we conclude that
$$\lim _{\beta_{1} \rightarrow 0} \omega_{\beta_{1}, \beta_{2}}=n \pi_{1}^{*} \omega_{\mathrm{FS}},$$
and the convergence of tensors occurs smoothly, so $\left(\mathbb{F}_{n} \backslash\left(Z_{n} \cup Z_{-n}\right), \omega_{\beta_{1}, \beta_{2}}\right)$ converges in the Gromov-Haussdorff sense to $\left(\mathbb{P}^{1}, n \omega_{\mathrm{FS}}\right)$. (This combination of smooth convergence of tensors and simultaneous collapse in the Gromov-Haussdorff sense is reminiscent of [10, Theorem 2.4 (ii) (a)].) This concludes the proof of the first two statements in Theorem 1.2.

We now turn to the last statement in Theorem 1.2. Inspired by [12, Lemma 3.1], we change variable from $\tau \in\left(1, \alpha_{2}\right)$ to
$$y:=\frac{\tau-1-\frac{n \beta_{1}}{2}}{n \beta_{1}^{2} / 2},$$
with $y \in\left(-\frac{1}{\beta_{1}}, \frac{1}{\beta_{1}}+O(1)\right)$ (recall (5.1)), with $y=0$ roughly corresponding to the mid-section between $Z_{n}$ and $Z_{-n}$. Thus, by (4.15), (5.1), and (5.2), and since $|\tau-1|=O\left(\beta_{1}\right)$,
$$\varphi(y)=\frac{2-n \beta_{1}}{2 n}\left(\frac{n^{2} \beta_{1}^{2}}{4}-\frac{n^{2} \beta_{1}^{4}}{4} y^{2}\right)+O\left(\beta_{1}^{3}\right), \quad\left(-\frac{1}{\beta_{1}}, \frac{1}{\beta_{1}}+O(1)\right) .$$

To determine a fiberwise-rescaled limit, define the fiberwise-rescaled metric, where the rescaling only occurs for the terms that have a well-defined restriction to each fiber, i.e.,
$$\widetilde{\omega_{\beta_{1}, \beta_{2}}}:=n \tau \pi_{1}^{*} \omega_{\mathrm{FS}}+\frac{1}{\beta_{1}^{2}} \varphi \pi_{2}^{*} \omega_{\mathrm{Cyl}}+\varphi(\sqrt{-1} \alpha \wedge \bar{\alpha}+\sqrt{-1} \alpha \wedge \overline{d w / w}+\sqrt{-1} d w / w \wedge \bar{\alpha}) .$$
with $\varphi$ given by (5.5). As in the proof of Lemma 3.2, the restriction of $\omega_{\beta_{1}, \beta_{2}}$ to a fiber is given by
$$\frac{1}{2 \varphi(\tau)} d \tau \otimes d \tau+2 \varphi(\tau) d \theta \otimes d \theta$$
so the restriction of $\widetilde{\omega_{\beta_{1}, \beta_{2}}}$ to a fiber is given by
$$\frac{n^{2} \beta_{1}^{2}}{8 \varphi(y)} d y \otimes d y+2 \frac{\varphi(y)}{\beta_{1}^{2}} d \theta \otimes d \theta$$
The Gromov-Haussdorff limit is then diffeomorphic to $\mathbb{P}^{1} \times \mathbb{C}^{\star}$. Indeed, using (5.5), the length, with respect to $\omega_{\beta_{1}, \beta_{2}}$, of the path on each fiber between the intersection point of the fiber with $Z_{n}$ and its midpoint, the intersection of the fiber with the smooth section $\{y=0\}$ is
$$\int_{1}^{1+n \beta_{1} / 2} \frac{d \tau}{\sqrt{\varphi(\tau)}} .$$
To estimate this, recall (4.15) and set $\xi:=\tau-1$,
$$\begin{aligned}
& \int_{1}^{1+n \beta_{1} / 2} \frac{d \tau}{\sqrt{\varphi(\tau)}} \\
= & \int_{0}^{\frac{n}{2} \beta_{1}} \frac{\sqrt{\xi+1}}{\sqrt{\frac{1}{3}\left(\beta_{1}-\frac{2}{n}\right) \xi\left(\xi+1-\alpha_{1}\right)\left(\xi+1-\alpha_{2}\right)}} \mathrm{d} \xi \\
= & \int_{0}^{\frac{n}{2} \beta_{1}} \frac{\sqrt{\xi+1}}{\sqrt{\frac{1}{3}\left(\beta_{1}-\frac{2}{n}\right) \xi\left(\xi+\frac{3}{2}-\frac{n}{2} \beta_{1}-\frac{5 n^{2}}{12} \beta_{1}^{2}+o\left(\beta_{1}^{2}\right)\right)\left(\xi-n \beta_{1}-\frac{n^{2}}{3} \beta_{1}^{2}+o\left(\beta_{1}^{2}\right)\right)}} \mathrm{d} \xi
\end{aligned}$$
As $\beta_{1} \rightarrow 0$, the term $\frac{\sqrt{\xi+1}}{\sqrt{\frac{1}{3}\left(\frac{2}{n}-\beta_{1}\right)}} \cdot \frac{1}{\sqrt{\xi+\frac{3}{2}-\frac{n}{2} \beta_{1}-\frac{5 n^{2}}{12} \beta_{1}^{2}+o\left(\beta_{1}^{2}\right)}}$ in the integral is uniformly bounded. Thus, to estimate the last displayed equation we consider
$$\begin{aligned}
& \int_{0}^{\frac{n}{2} \beta_{1}} \frac{\mathrm{~d} \xi}{\sqrt{-\xi\left(\xi-n \beta_{1}+o\left(\beta_{1}\right)\right)}} \\
& \xlongequal{\beta_{1}} \int_{0}^{\frac{\xi}{2}} \frac{\beta_{1} \mathrm{~d} u}{\sqrt{-\beta_{1} u\left(\beta_{1} u-\beta_{1} n+o\left(\beta_{1}\right)\right)}} \\
& \stackrel{\beta_{1} \rightarrow 0}{=} \int_{0}^{\frac{n}{2}} \frac{\mathrm{~d} u}{\sqrt{u(n-u)}}=O(1) .
\end{aligned}$$
Similarly we also get $O(1)$ for the distance between $Z_{-n}$ and $\{y=0\}$ with respect to $\omega_{\beta_{1}, \beta_{2}}$. Hence, after the rescaling the fiberwise metric by $\beta_{1}^{-2}$, these same distances must be $O\left(\beta_{1}^{-1}\right)$, and in the limit $\beta_{1} \rightarrow 0$ we must get the product differential structure on $\mathbb{P}^{1} \times \mathbb{C}^{*}$. Moreover, in the limit $\beta_{1} \rightarrow 0$, (5.6) converges pointwise on compact subsets to
$$\frac{n}{2} d y \otimes d y+\frac{n}{2} d \theta \otimes d \theta .$$

The limiting metric in the pointed Gromov-Hausdorff sense is
$$\lim _{\beta_{1} \rightarrow 0} \widetilde{\omega_{\beta_{1}, \beta_{2}}}=n\left(\pi_{1}^{*} \omega_{\mathrm{FS}}+\pi_{2}^{*} \omega_{\mathrm{cyl}}\right) .$$
whose Kähler form is $n d \zeta \wedge \overline{d \zeta} /|\zeta|^{2}=n \omega_{\text {Cyl }}$ (recall (3.4)) with $\zeta:=e^{y+\sqrt{-1} \theta}$. Combining this with (5.3), (5.5) and (5.6), the limiting metric, in the pointed Gromov-Hausdorff sense is then
$$\lim _{\beta_{1} \rightarrow 0} \widetilde{\omega_{\beta_{1}, \beta_{2}}}=n\left(\pi_{1}^{*} \omega_{\mathrm{FS}}+\pi_{2}^{*} \omega_{\mathrm{Cyl}}\right) .$$
This concludes the proof of Theorem 1.2.
Remark 5.1. We mention in passing an interesting borderline phenomenon that occurs in the cases $n \in\{1,2\}$. By Corollary 4.1, when $n=2$ the metrics $\omega_{\beta_{1}, \beta_{2}}$ exists for all $\beta_{1} \in(0,1)$. Naturally, one may ask about the large angle limit $\beta_{1} \rightarrow 1$. It turns out that in this case $\alpha_{2} \rightarrow \infty$ and one obtains Gromov-Haussdorff convergence to the complete Ricci flat Eguchi-Hanson metric on the non-compact space $-2 H_{\mathbb{P}^{1}}$ as $C_{2}=Z_{-n}$ gets pushed-off to infinity. Similarly, when $n=1$, the metrics $\omega_{\beta_{1}, \beta_{2}}$ exists for all $\beta_{1} \in(0,2)$. In the limit $\beta_{1} \rightarrow 2$ one has $\beta_{2} \rightarrow 1$ and the limit is now a complete Ricci flat metric on $-H_{\mathbb{P}^{1}}$ with angle $4 \pi$ along $Z_{1}$. We discuss these examples in detail elsewhere [13].

Acknowledgments. Thanks to I.A. Cheltsov for posing to us Question 1.4 and to Y. Ji for a careful reading and several corrections. Research supported by NSF grants DMS-1515703,1906370, a UMD-FAPESP Seed Grant, the China Scholarship Council award 201706010020, the China post-doctoral grant BX20190014 and the Rosi \& Max Varon Visiting Professorship at the Weizmann Institute of Science in Fall 2019 and Spring 2020 to which Y.A.R. is grateful for the excellent research conditions. K.Z. was a Visiting Scholar at the University of Maryland in 2017-2018 when this work was initiated and is grateful for its excellent research conditions.

\section*{References}
\begin{itemize}
\item[] [1] E. Calabi, Métriques Kählériennes et fibrés holomorphes, Ann. scient. Éc. Norm. Sup. 12 (1979), 269-294.
\item[] [2] E. Calabi, Extremal metrics, in: Seminar on Differential Geometry (S.-T. Yau, Ed.), Princeton University Press, 1982, pp. 259-290.
\item[] [3] I.A. Cheltsov, private communication, 2015.
\item[] [4] I.A. Cheltsov, Y.A. Rubinstein, Asymptotically log Fano varieties, Adv. Math. 285 (2015), 1241-1300.
\item[] [5] I.A. Cheltsov, Y.A. Rubinstein, On flops and canonical metrics, Ann. Sc. Norm. Super. Pisa Cl. Sci. (5) 18 (2018), 283-311.
\item[] [6] K. Fujita, On log K-stability for asymptotically log Fano varieties, Ann. Fac. Sci. Toulouse Math. 25 (2016), 1013-1024.
\item[] [7] F. Hirzebruch, Über eine Klasse von einfach-zusammenhängenden komplexen Mannigfaltigkeiten, Math. Ann. 124 (1951), 77-86.
\item[] [8] A.D. Hwang, M.A. Singer, A momentum construction for circle-invariant Kähler metrics, Trans. Amer. Math. Soc. 354 (2002), 2285-2325.
\item[] [9] T. Jeffres, R. Mazzeo, Y.A. Rubinstein, Kähler-Einstein metrics with edge singularities, (with an appendix by C. Li and Y.A. Rubinstein), Annals of Math. 183 (2016), 95-176.
\end{itemize}
\begin{itemize}
\item[] [10] A. Pulemotov, Y.A. Rubinstein, Ricci iteration on homogeneous spaces, Trans. Amer. Math. Soc. 371 (2019), 6257-6287.
\item[] [11] Y.A. Rubinstein, Smooth and singular Kähler-Einstein metrics, in: Geometric and Spectral Analysis (P. Albin et al., Eds.), Contemp. Math. 630, Amer. Math. Soc. and Centre de Recherches Mathématiques, 2014, 45-138.
\item[] [12] Y.A. Rubinstein, K. Zhang, Small angle limits of Hamilton's footballs, Bull. London Math. Soc. 52 (2020) 189-199.
\item[] [13] Y. Ji, Y.A. Rubinstein, K. Zhang, Eguchi-Hanson and Stenzel metrics as limits of Kähler-Einstein edge metrics, preprint, in preparation.
\item[] [14] G. Tian, Kähler-Einstein metrics on algebraic manifolds, Lecture Notes in Math. 1646 (1996), 143-185.
\end{itemize}

University of Maryland
yanir@alum.mit.edu
Beijing International Center for Mathematical Research, Peking University
kwzhang@pku.edu.cn