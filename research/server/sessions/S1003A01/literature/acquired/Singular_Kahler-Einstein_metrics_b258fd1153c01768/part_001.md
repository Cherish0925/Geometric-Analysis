---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Singular Kahler-Einstein metrics]

---
source_file: Singular_Kahler-Einstein_metrics_638a8626f57b.pdf
converter: mathpix
format: mmd
---

\title{
Singular Kahler-Einstein metrics
}

\author{
Philippe Eyssidieux, Vincent Guedj, Ahmed Zeriahi
}
- To cite this version:

Philippe Eyssidieux, Vincent Guedj, Ahmed Zeriahi. Singular Kahler-Einstein metrics. 2006. 〈hal-00021177〉

HAL Id: hal-00021177
https://hal.science/hal-00021177v1
Preprint submitted on 17 Mar 2006

HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific research documents, whether they are published or not. The documents may come from teaching and research institutions in France or abroad, or from public or private research centers.

L'archive ouverte pluridisciplinaire HAL, est destinée au dépôt et à la diffusion de documents scientifiques de niveau recherche, publiés ou non, émanant des établissements d'enseignement et de recherche français ou étrangers, des laboratoires publics ou privés.

\title{
SINGULAR KÄHLER-EINSTEIN METRICS
}

\author{
PHILIPPE EYSSIDIEUX \& VINCENT GUEDJ \& AHMED ZERIAHI
}

\begin{abstract}
We study degenerate complex Monge-Ampère equations of the form $\left(\omega+d d^{c} \varphi\right)^{n}=e^{t \varphi} \mu$ where $\omega$ is a big semi-Kähler form on a compact Kähler manifold $X$ of dimension $n, t \in \mathbb{R}^{+}$, and $\mu=f \omega^{n}$ is a positive measure with density $f \in L^{p}\left(X, \omega^{n}\right), p>1$. We prove the existence and unicity of continuous $\omega$-plurisubharmonic solutions.

In case $X$ is projective and $\omega=\psi^{*} \omega^{\prime}$, where $\psi: X \rightarrow V$ is a proper birational morphism to a normal projective variety, $\left[\omega^{\prime}\right] \in N S_{\mathbb{R}}(V)$ is an ample class and $\mu$ has only algebraic singularities, we prove that the solution is smooth in the regular locus of the equation.

We use these results to construct singular Kähler-Einstein metrics of non-positive curvature on projective klt pairs, in particular on canonical models of algebraic varieties of general type.
\end{abstract}

2000 Mathematics Subject Classification: 32W20, 32Q20, 32J27, 14J17.

\section*{Introduction}

Thirty years ago, in a celebrated article [Y], S.T. Yau (and independently T. Aubin [A]) solved the Calabi conjecture by studying complex Monge-Ampère equations on a compact Kähler manifold.

Since then, complex Monge-Ampère equations have been extremely useful in Kähler geometry (see for instance [DP]) and in the dynamical study of rational mappings (see [S] and references therein).

Two major developments in the theory of complex Monge-Ampère equations occurred in the last decade. In the local theory, a deeper analysis of the image of the complex Monge-Ampère operator [C], [K 1] has followed the pioneering work of E.Bedford and A.Taylor [BT]. In the global theory a new proof of the $\mathcal{C}^{0}$-estimate [K 1,2] has allowed one to treat complex Monge-Ampère equations with more degenerate R.H.S.

In [GZ1], [GZ2], two of us revisited and extended the results of [BT], [C], on complex Monge-Ampère operators to compact Kähler manifolds. In the present article, we use these methods to study complex Monge-Ampère equations with degenerate L.H.S. We first define, in the spirit of [C], [GZ 2], weak solutions to degenerate complex Monge-Ampère equations and then prove, using ideas of [K 1,2], that these solutions are continous:

Theorem A. Let $X$ be a compact Kähler manifold, $\omega$ a semi positive (1,1)-form such that $\int_{X} \omega^{n}>0$ and $0 \leq f \in L^{p}\left(X, \omega^{n}\right), p>1$, a density such that $\int_{X} f \omega^{n}=\int_{X} \omega^{n}$. Then there is a unique continuous function $\varphi$ on $X$ such that $\omega+d d^{c} \varphi \geq 0$ and
$$\left(\omega+d d^{c} \varphi\right)^{n}=f \omega^{n} \quad \text { with } \quad \sup _{X} \varphi=-1 .$$

Furthermore $f \mapsto \varphi$ is a continuous map from $L^{p}\left(X, \omega^{n}\right)$ to $\mathcal{C}^{0}(X)$.

When $\omega$ has algebraic singularities, then $\mu$ can be assumed to have $L^{p}$ density with respect to the Lebesgue measure. With this $\mathcal{C}^{0}$-estimate, it is possible to adapt classical ideas of [Y] and [Ts] and prove:

Theorem B. Let $X$ be projective algebraic complex manifold, $\omega$ a smooth semi Kähler form that is Kähler outside a complex subvariety $S \subset X$. Let $\Omega$ be a Kähler form on $X$. Assume furthermore that $\omega^{n}=D \Omega^{n}$ where $D^{-\epsilon}$ is in $L^{1}\left(\Omega^{n}\right)$ and that $[\omega],[\Omega] \in N S_{\mathbb{R}}(X)$.

Let $s_{1}, \ldots, s_{p}$ (resp. $t_{1}, \ldots, t_{q}$ ) be holomorphic sections of some line bundle. (resp. of some other line bundle). Assume $k, l \in \mathbb{R}_{\geq 0}$ and $F \in \mathcal{C}^{\infty}(X, \mathbb{R})$ are fixed so that
$$\int_{X} \frac{1}{\left|t_{1}\right|^{2 l}+\ldots+\left|t_{q}\right|^{2 l}} \Omega^{n}<\infty \text { and } \int_{X} \frac{\left|s_{1}\right|^{2 k}+\ldots+\left|s_{p}\right|^{2 k}}{\left|t_{1}\right|^{2 l}+\ldots+\left|t_{q}\right|^{2 l}} e^{F} \Omega^{n}=\int_{X} \Omega^{n} .$$

Then the unique continuous function $\varphi$ such that $\omega+d d^{c} \varphi \geq 0$ and
$$\left(\omega+d d^{c} \varphi\right)^{n}=\frac{\left|s_{1}\right|^{2 k}+\ldots+\left|s_{p}\right|^{2 k}}{\left|t_{1}\right|^{2 l}+\ldots+\left|t_{q}\right|^{2 l}} e^{F} \Omega^{n}, \text { with } \sup _{X} \varphi=-1,$$
is smooth outside $B=S \cup \cap_{i}\left\{s_{i}=0\right\} \cup \cap_{i}\left\{t_{i}=0\right\}$.
This result should be compared with [Y], Theorem 8, p. 403. Yau's result is stronger in many respects, most notably in the absence of any projectivity/rationality assumption and a more precise regularity theory. On the other hand, the condition on the poles of the L.H.S. is less optimal than here. We expect the projectivity/rationality assumptions to be superfluous.

Observe that the condition on the singularity in the L.H.S. is precisely the condition that the singular metric associated to $l\left(t_{i}\right)$ has a trivial multiplier ideal sheaf, or if $q=1$ that the pair ( $X, l\left(t_{1}\right)$ ) is klt (see definition 6.7). The possibility of solving complex Monge-Ampère equations with $L^{p}$-R.H.S. was first established by S.Kolodziej [K 1,2], and the connection with the singularities of the Minimal Model Program (MMP for short) has been a strong incentive to our work.
¿From an algebraic geometer's perspective, these results may be viewed as a version of [Y] for normal Kähler spaces.

As a by-product, S.T.Yau constructed Kähler-Einstein metrics on smooth canonically polarized manifolds and Ricci-flat metrics on what is now known as Calabi-Yau manifolds. It had been soon realized [Ko] that this also yields Kähler-Einstein metrics on Kähler orbifolds hence on the canonical models of surfaces of general type since they have isolated quotient singularities.

In higher dimension, in spite of the development of the MMP during the 1980s - culminating with [Mo] and the proof of the existence of canonical models for general type 3-folds [Ka] -, there was no satisfying analog of these Kähler-Einstein metrics.

For smooth minimal general type projective manifolds, H.Tsuji proved [Ts] that an appropriate Kähler-Ricci flow starting with an arbitrary Kähler datum exists in infinite time, converges towards a current representing the canonical class which is smooth outside the exceptional locus of the map
to the canonical model, and defines a Kähler-Einstein metric there ${ }^{1}$. The conjecture made there that the current has continuous (or even bounded) local potentials partly motivated our work.

The article [Ts] has been revisited in two recent preprints, [CN] and [TZ], we learnt of when finishing the present work, where a very satisfactory proof of convergence towards a current with bounded potentials is given. The independent work [TZ] uses a slightly weaker version of Theorem A and does not give any detail on the proof. On the other hand, the three approaches tend to emphasize different aspects of the problem and seem to complement each other nicely.

In this article we give a more general theory of singular Kähler-Einstein metrics as a consequence of the following result:

Theorem C. Let $(V, \Delta)$ be a projective klt pair such that $K_{V}+\Delta$ is an ample $\mathbb{Q}$-divisor. Then there is a unique semi-Kähler current in $\left[K_{V}+\Delta\right]$ with continuous potentials, which satisfies a global degenerate Monge-Ampère equation on $V$ and defines a smooth Kähler-Einstein metric of negative curvature on $(V-\Delta)^{\text {reg }}$.

Let $(V, \Delta)$ be a projective klt pair such that $K_{V}+\Delta \cong 0(\mathbb{Q}$-linear equivalence of $\mathbb{Q}$-Cartier divisors). Then in every ample class in $N S_{\mathbb{R}}(V)$ there is a unique semi-Kähler current with continuous potentials, which satisfies a global degenerate Monge-Ampère equation on $V$ and defines a Ricci flat metric on $(V-\Delta)^{\text {reg }}$.

The precise formulation and Monge-Ampère equations are to be found in Theorems 7.5 and 7.8 below.

Corollary D. Let $X$ be a projective threefold of general type and $V=X_{\text {can }}$ the unique model of $X$ with only canonical singularities and $K_{V}$ ample. Then $K_{V}$ contains a unique singular Kähler-Einstein metric $\omega_{K E}$ of negative curvature.

Note that we do not assume the singularities to be quotient singularities nor that $X$ has a smooth minimal model (a strong restriction present in [Ts], [TZ], [CN]). On the other hand if $\pi: X \rightarrow X_{\text {can }}$ is a resolution of singularities then $\left[\pi^{*} \omega_{K E}\right] \cong K_{X}+F$ where $F \geq 0$ and $=0$ iff $\pi$ is crepant and $X$ is a smooth minimal model. If the MMP is confirmed to work in higher dimension, then Corollary D extends there as well. In dimension 4, the MMP seems to work [Sho] but few people claim they understand this deep work in its manifold aspects. There is an active scientific project led by A.Corti aiming at making Shokurov's work more accessible [Cor]. In higher dimension, substantial progress has been recently announced in [HMcK], Shokurov's ideas being a major ingredient.

One may also try and construct these singular KE metrics unconditionnally in an approach to the finiteness of the canonical ring [Siu 2]. Needless to say, it is a substantially harder task.

\footnotetext{
${ }^{1}$ Although his idea was rather compelling, the details of the proof for convergence were somewhat hard to follow.
}

\section*{Notations and organization of the paper}

In the whole paper, $X$ will denote a compact Kähler manifold of dimension $n, \omega$ a smooth closed form of bidegree $(1,1)$ which is non-negative and big, i.e. the smooth measure $\omega^{n}$ is not identical to zero. For convenience we normalize $\omega$ so that
$$\operatorname{Vol}_{\omega}(X):=\int_{X} \omega^{n}=1 .$$
$V$ will denote a normal complex space. A resolution of $V$ will be a projective bimeromorphic holomorphic morphism $\pi: X \rightarrow V, X$ being smooth, such that $\pi: \pi^{-1}\left(V^{\text {reg }}\right) \rightarrow V^{\text {reg }}$ is an isomorphism. A resolution $\pi$ is a log-resolution iff $\pi^{-1}\left(V^{\text {sing }}\right)$ is a divisor with simple normal crossings. Assume we have a coherent ideal sheaf $\mathcal{I} \subset \mathcal{O}_{V}$. A log resolution of $(V, \mathcal{I})$ is a projective bimeromorphic holomorphic morphism $\pi: X \rightarrow V X$ being smooth, such that $\left.\pi: \pi^{-1}(V-Z(\mathcal{I}))^{\text {reg }}\right) \rightarrow(V-Z(\mathcal{I}))^{\text {reg }}$ is an isomorphism with the additional property that the ideal sheaf $\pi^{-1} \mathcal{I} . \mathcal{O}_{X}{ }^{2}$ satisfies $\pi^{-1} \mathcal{I} . \mathcal{O}_{X}=\mathcal{O}_{X}\left(-\sum \gamma_{E} E\right) \subset \mathcal{O}_{X}$ where $\gamma_{E} \in \mathbb{N}$ is a positive integer attached to any exceptional divisor $E$ of $\pi$.

A pair is a pair $(V, \Delta)$ with $V$ a normal complex space and $\Delta$ a $\mathbb{Q}$-Weil divisor $\Delta=\sum_{i} d_{i} E_{i}$ where $0 \leq d_{i} \leq 1$ are rational numbers and $\left(E_{i}\right)_{i}$ is a finite family of pairwise distinct irreducible codimension 1 subvarieties of $V$. A log resolution of a pair is a log resolution of the ideal $\mathcal{I}_{N \Delta}$ where $N$ is an integer such that $N d_{i} \in \mathbb{N} .^{3}$

All these flavors of log-resolutions exist by [Hi] if the variety (resp. pair) under consideration is open in (resp. a restriction to an open subset of) a compact variety (pair).

The paper is organized as follows. In section 1 we define, following [GZ $2]$, the set $\mathcal{E}^{1}(X, \omega)$ of $\omega$-psh functions with finite self-energy, and produce weak solutions to complex Monge-Ampère equations $\left(\omega+d d^{c} \varphi\right)^{n}=\mu$ in the class $\mathcal{E}^{1}(X, \omega)$ (see proposition 1.4). This is our first basic observation: weak solutions are easy to produce in $\mathcal{E}^{1}(X, \omega)$.

The continuity of the solutions is established in section 2 (see Theorem 2.1), by using ideas from [K 1,2,3] and [GZ 1]. This, together with propositions 3.1 and 3.3, yields Theorem A. We actually expect the solutions to be Hölder-continuous, as Theorem 3.5 indicates. We indeed establish further regularity results in section 3, especially Theorem 3.6, by using ideas of [Y],[Ts]. This yields Theorem B.

In section 4 we solve Monge-Ampère equations of the type $\left(\omega+d d^{c} \varphi\right)^{n}=$ $e^{t \varphi} \mu, t>0$ (see Theorems 4.1, 4.4) by a fixed point method. Here again the use of class $\mathcal{E}^{1}(X, \omega)$ makes life easier, and allows us to reduce our analysis to previously studied Monge-Ampère equations $\left(\omega+d d^{c} \varphi\right)^{n}=\mu^{\prime}$.

\footnotetext{
${ }^{2} \pi^{-1} \mathcal{I} . \mathcal{O}_{X}$ is locallly the ideal sheaf of $\mathcal{O}_{X}$ generated by the family of holomorphic functions $\left(\pi^{*} f_{I}\right)_{I}$, where $\left(f_{I}\right)_{I}$ are local generators of $\mathcal{I}$. The set $Z(\mathcal{I})$ is the analytic subvariety defined by $\mathcal{I}$.
${ }^{3}$ The MMP is conjectured to work for pairs. This seemingly technical extension of the MMP is known as log-MMP. log-MMP works in dimension $\leq 3$. The philosophy of the log-MMP is to define the canonical divisor of a pair to be $K_{(V, \Delta)}:=K_{V}+\Delta$ and to try and prove the same theorems for pairs and for varieties.
}

In section 5 we recall some basic facts on some of the singularities encountered in the MMP, and in section 6 we explain what sort of measures $\mu$ we need to consider in order to produce Kähler-Einstein metrics. An important observation is lemma 6.4, which shows that it is necessary to restrict to the case of log terminal singularities (see definition 5.3).

Finally in section 7 we show how our results from sections 2,3,4 allow us to produce singular Kähler-Einstein metrics (see Theorems 7.5, 7.8, 7.12). This is where we prove Theorem C.

\section*{1. Weak solutions to Monge-Ampère equations}

For any Kähler form $\Omega$ on $X$ and for all $\varepsilon>0$, the form $\omega_{\varepsilon}:=\omega+\varepsilon \Omega$ is again Kähler on $X$. We are going to extend several results that are known to hold true when $\omega$ is Kähler to the more general setting of semi-positive and big forms.

Recall that the set of $\omega$-plurisubharmonic functions ( $\omega$-psh for short) is
$$P S H(X, \omega):=\left\{\varphi \in L^{1}(X, \mathbb{R} \cup\{-\infty\}) / d d^{c} \varphi \geq-\omega \text { and } \varphi \text { is u.s.c. }\right\} .$$
We refer the reader to [GZ 1] for basic properties of $\omega$-psh functions. The following subclass has been extensively studied in [GZ 2]:

Definition 1.1. We let $\mathcal{E}^{1}(X, \omega)$ denote the set of $\omega$-psh functions with finite self-energy: this is the set of functions $\varphi \in P S H(X, \omega)$ for which there exists a sequence $\varphi_{j} \in P S H(X, \omega) \cap L^{\infty}(X)$ such that
$$\varphi_{j} \searrow \varphi \quad \text { and } \quad \sup _{j} \int_{X}\left(-\varphi_{j}\right)\left(\omega+d d^{c} \varphi_{j}\right)^{n}<+\infty .$$

This class of functions is studied in [GZ 2] when $\omega$ is a Kähler form. We leave it to the reader to check that the basic properties of this class of functions proved in [GZ 2] when $\omega$ is Kähler apply with no modification to the case where $\omega$ is merely semi-positive and big. In particular the complex Monge-Ampère operator $\left(\omega+d d^{c} \varphi\right)^{n}$ is well-defined for $\varphi \in \mathcal{E}^{1}(X, \omega)$, and it is continuous on decreasing sequences of functions in $\mathcal{E}^{1}(X, \omega)$.

We shall need a slightly more general continuity result, which takes into account the dependence in $\omega$ :

Proposition 1.2. Fix $\Omega$ a Kähler form on $X$, and let $\left(\varepsilon_{j}\right)$ be a sequence of positive real numbers decreasing to zero. Let $\varphi_{j} \in \mathcal{E}^{1}\left(X, \omega+\varepsilon_{j} \Omega\right)$ be a sequence of functions which decrease pointwise towards $\varphi$, and such that
$$\sup _{j \geq 1} \int_{X}\left|\varphi_{j}\right|\left(\omega+\varepsilon_{j} \Omega+d d^{c} \varphi_{j}\right)^{n}<+\infty .$$

Then $\varphi \in \mathcal{E}^{1}(X, \omega)$, and $\left(\omega+\varepsilon_{j} \Omega+d d^{c} \varphi_{j}\right)^{n} \rightarrow\left(\omega+d d^{c} \varphi\right)^{n}$.
Proof. Set $\omega_{j}:=\omega+\varepsilon_{j} \Omega$. We can assume w.l.o.g. that $\varphi_{j} \leq \varphi \leq 0$. Set $\varphi^{K}:=\max (\varphi,-K) \in P S H(X, \omega)$ and $\varphi_{j}^{K}:=\max \left(\varphi_{j},-K\right) \in P S H\left(X, \omega_{j}\right)$.

Observe that, $K$ being fixed, $\left(\varphi_{j}^{K}\right)_{j}$ is uniformly bounded and decreases towards $\varphi^{K}$ as $j$ goes to infinity. Therefore $\left(\omega_{j}+d d^{c} \varphi_{j}^{K}\right)^{n} \rightarrow\left(\omega+d d^{c} \varphi^{K}\right)^{n}$,
by a classical result of E.Bedford and A.Taylor [BT 82]. Moreover the sequence of positive measures $\left(-\varphi_{j}^{K}\right)\left(\omega_{j}+d d^{c} \varphi_{j}^{K}\right)^{n}$ has uniformly bounded mass, since by lemma 7.2 in [GZ 2],
$$0 \leq \int_{X}\left(-\varphi_{j}^{K}\right)\left(\omega_{j}+d d^{c} \varphi_{j}^{K}\right)^{n} \leq 2^{n} \int_{X}\left(-\varphi_{j}\right)\left(\omega_{j}+d d^{c} \varphi_{j}\right)^{n} \leq 2^{n} M,$$
where $M:=\sup _{j} \int_{X}\left(-\varphi_{j}\right)\left(\omega_{j}+d d^{c} \varphi_{j}\right)^{n}<+\infty$.
Since $\varphi_{j}$ is u.s.c., a standard argument yields that any cluster point $\nu$ of the sequence $\left(-\varphi_{j}^{K}\right)\left(\omega_{j}+d d^{c} \varphi_{j}^{K}\right)^{n}$ satisfies $0 \leq\left(-\varphi^{K}\right)\left(\omega+d d^{c} \varphi^{K}\right)^{n} \leq \nu$. In particular
$$0 \leq \int_{X}\left(-\varphi^{K}\right)\left(\omega+d d^{c} \varphi^{K}\right)^{n} \leq \liminf _{j \rightarrow+\infty} \int\left(-\varphi_{j}^{K}\right)\left(\omega_{j}+d d^{c} \varphi_{j}^{K}\right)^{n} \leq 2^{n} M$$
is bounded from above uniformly with respect to $K$. Since $\varphi^{K}$ decreases towards $\varphi$, this shows $\varphi \in \mathcal{E}^{1}(X, \omega)$.

It remains to show that $\left(\omega_{j}+d d^{c} \varphi_{j}\right)^{n} \rightarrow\left(\omega+d d^{c} \varphi\right)^{n}$. Since $\left(\omega_{j}+\right.$ $\left.d d^{c} \varphi_{j}^{K}\right)^{n} \rightarrow\left(\omega+d d^{c} \varphi^{K}\right)^{n}$ for any fixed $K$, it is enough to get an upper bound on the mass of $\left(\omega_{j}+d d^{c} \varphi_{j}^{K}\right)^{n}$ in $\left(\varphi_{j} \leq-K\right)$ which is uniform in $j$. This follows from Chebyshev inequality, namely
$$\int_{\left(\varphi_{j} \leq-K\right)}\left(\omega_{j}+d d^{c} \varphi_{j}\right)^{n} \leq \frac{1}{K} \int_{X}\left(-\varphi_{j}\right)\left(\omega_{j}+d d^{c} \varphi_{j}\right)^{n} \leq \frac{M}{K} .$$
This yields the desired result. \(\square\)

The Monge-Ampère capacity $C a p_{\omega}(\cdot)$ has been studied in [GZ 1],
$$\operatorname{Cap}_{\omega}(K):=\sup \left\{\int_{K} \omega_{u}^{n} / u \in \operatorname{PSH}(X, \omega), 0 \leq u \leq 1\right\},$$
where $K$ is a Borel subset of $X$. Here - and in the sequel - we use the notation $\omega_{u}:=\omega+d d^{c} u \geq 0$. In this article we are interested in measures which are dominated by the Monge-Ampère capacity in the following way:

Definition 1.3. A probability measure $\mu$ on $X$ satisfies condition $\mathcal{H}(\alpha, A, \omega)$ if for all Borel subset $K$ of $X$,
$$\mu(K) \leq A C a p_{\omega}(K)^{1+\alpha} .$$

It has been shown by S.Kolodziej that when $\omega$ is Kähler, a probability measure $\mu$ which satisfies $\mathcal{H}(\alpha, A, \omega)$ can be written as the Monge-Ampère measure of some continuous $\omega$-psh function. This is still true when $\omega$ is merely semi-positive and big, and the proof will occupy us until the end of section 2. We start by observing - following [GZ 2] - that $\mu$ is the Monge-Ampère of a function $\varphi$ which is not too singular.

Proposition 1.4. Let $\mu$ be a probability measure on $X$ which satisfies condition $\mathcal{H}(\alpha, A, \omega)$. Then there exists a unique function $\varphi \in \mathcal{E}^{1}(X, \omega)$ s.t.
$$\mu=\left(\omega+d d^{c} \varphi\right)^{n} \quad \text { and } \quad \sup _{X} \varphi=-1 .$$
Proof. Fix $\Omega$ a Kähler form on $X$, and set $\omega_{j}:=\omega+\varepsilon_{j} \Omega$, where $\varepsilon_{j}>0$ decreases to 0 . We start by showing that $\mathcal{E}^{1}\left(X, \omega_{j}\right) \subset L^{1}(\mu)$.

Fix $\varphi \in \mathcal{E}^{1}\left(X, \omega_{j}\right)$. We can assume without loss of generality that $\sup _{X} \varphi=$ -1. It follows from propositions 3.6 and 2.7 in [GZ 1] that there exists a constant $C=C(\omega, \Omega)>0$ independent of $j$ such that $\operatorname{Cap}_{\omega_{j}}(\varphi<-t) \leq C / t$ for all $t>0$. Since $\operatorname{Cap}_{\omega}(\cdot) \leq \operatorname{Cap}_{\omega_{j}}(\cdot)$, the measure $\mu$ satisfies $\mathcal{H}\left(\alpha, A, \omega_{j}\right)$. We infer
$$0 \leq \int_{X}(-\varphi) d \mu=\int_{t=1}^{+\infty} \mu(\varphi<-t) d t \leq \frac{A C^{1+\alpha}}{\alpha}<+\infty$$
with an upper-bound which is independent of $j$.
The main result in [GZ 2] guarantees in this case that there exists a unique function $\varphi_{j} \in \mathcal{E}^{1}\left(X, \omega_{j}\right)$ such that
$$\left(\omega_{j}+d d^{c} \varphi_{j}\right)^{n}=\lambda_{j} \mu \text { and } \sup _{X} \varphi_{j}=-1,$$
where $\lambda_{j}=\int_{X}\left(\omega+\varepsilon_{j} \Omega\right)^{n}>1$ decreases to 1 as $j$ goes to infinity.
The normalization $\sup _{X} \varphi_{j}=-1$ implies that the sequence $\left(\varphi_{j}\right)$ is relatively compact in $L^{1}(X)$ (see proposition 2.7 in [GZ 1]). Let $\varphi$ be a cluster point of $\left(\varphi_{j}\right)$. Relabelling if neccessary, we assume $\varphi_{j} \rightarrow \varphi$ in $L^{1}(X)$. Note that $\varphi \in P S H(X, \omega)$ and $\sup _{X} \varphi=-1$ (by Hartogs' lemma, see proposition 2.7, [GZ 1]). We are going to show that $\varphi \in \mathcal{E}^{1}(X, \omega)$ and $\omega_{\varphi}^{n}=\mu$.

Set $\Phi_{j}:=\left(\sup _{l \geq j} \varphi_{l}\right)^{*}$, where $u^{*}$ denotes the upper-semi-continuous regularization of $u$. Then $\Phi_{j} \in P S H\left(X, \omega_{j}\right)$ with $\Phi_{j} \geq \varphi_{j}$, hence $\Phi_{j} \in \mathcal{E}^{1}\left(X, \omega_{j}\right)$ (see proposition 3.2 in [GZ 2]), and $\Phi_{j}$ decreases towards $\varphi$. For $l \geq j$, we have
$$\left(\omega_{j}+d d^{c} \varphi_{l}\right)^{n} \geq\left(\omega_{l}+d d^{c} \varphi_{l}\right)^{n}=\lambda_{l} \mu \geq \mu .$$
It follows therefore from an inequality due to J.-P.Demailly [Dem 1] that $\left(\omega_{j}+d d^{c} \Phi_{j}\right)^{n} \geq \mu$. Now by (1) and lemma 7.2 in [GZ 2],
$$0 \leq \int_{X}\left(-\Phi_{j}\right)\left(\omega_{j}+d d^{c} \Phi_{j}\right)^{n} \leq 2^{n} \int_{X}\left(-\varphi_{j}\right)\left(\omega_{j}+d d^{c} \varphi_{j}\right)^{n}=2^{n} \lambda_{j} \int_{X}\left(-\varphi_{j}\right) d \mu$$
is uniformly bounded with respect to $j$ thanks to (1).
We infer from proposition 1.2 that $\varphi \in \mathcal{E}^{1}(X, \omega)$ and $\left(\omega_{j}+d d^{c} \Phi_{j}\right)^{n} \rightarrow$ $\left(\omega+d d^{c} \varphi\right)^{n}$. Thus $\left(\omega+d d^{c} \varphi\right)^{n} \geq \mu$, but these are two probability measures, whence $\mu=\left(\omega+d d^{c} \varphi\right)^{n}$. The uniqueness of $\varphi$ follows from Theorem 7.4, [GZ 2]. \(\square\)

Remark 1.5. It follows from the work of S.Kolodziej [K 1,2,3] that the $\varphi_{j}$ 's are actually continuous functions. Proving however that $\varphi=\lim \varphi_{j}$ is continuous is a difficult task and is the goal of the next section.

\section*{2. Continuous solutions}

The goal of this section is to prove the following result:
Theorem 2.1. Let $\mu$ be a probability measure on $X$ which satisfies condition $\mathcal{H}(\alpha, A, \omega)$. Then there exists a unique continuous function $\varphi \in P S H(X, \omega)$ such that
$$\mu=\left(\omega+d d^{c} \varphi\right)^{n} \quad \text { and } \quad \sup _{X} \varphi=-1 .$$
Moreover $\|\varphi\|_{L^{\infty}(X)} \leq C$, where $C$ only depends on $\alpha, A$ and $\omega$.

It follows from proposition 1.4 that we already know the existence of a unique solution $\varphi \in \mathcal{E}^{1}(X, \omega)$ to this Monge-Ampère equation. We need to show it is continuous. The following result is the key to everything to follow.

Lemma 2.2. Let $\varphi, \psi \in \mathcal{E}^{1}(X, \omega)$ be two negative functions. Then for all $s>0$ and $0 \leq t \leq 1$,
$$t^{n} \operatorname{Cap}_{\omega}(\varphi-\psi<-s-t) \leq \int_{(\varphi-\psi<-s-t \psi)} \omega_{\varphi}^{n} .$$
Proof. Fix $u \in \operatorname{PSH}(X, \omega)$ with $0 \leq u \leq 1$. For $\delta>0$ we set $t=\delta /(1+\delta)$. Observe that $0 \leq t \leq 1$ and
$$\{\varphi-\psi<-s-t\} \subset\left\{\varphi<\frac{\psi+\delta u}{1+\delta}-s-t\right\} \subset\{\varphi-\psi<-s-t \psi\} .$$
Set $\tilde{\varphi}:=(\psi+\delta u) /(1+\delta)-s-t \in P S H(X, \omega)$. Observe that
$$t^{n} \int_{(\varphi-\psi<-s-t)} \omega_{u}^{n} \leq \int_{(\varphi-\psi<-s-t)}\left[\frac{1}{1+\delta} \omega_{\psi}+\frac{\delta}{1+\delta} \omega_{u}\right]^{n} \leq \int_{(\varphi<\tilde{\varphi})}\left[\omega+d d^{c} \tilde{\varphi}\right]^{n}$$
It follows from the comparison principle in class $\mathcal{E}^{1}(X, \omega)$, that
$$\int_{(\varphi<\tilde{\varphi})}\left[\omega+d d^{c} \tilde{\varphi}\right]^{n} \leq \int_{(\varphi<\tilde{\varphi})}\left[\omega+d d^{c} \varphi\right]^{n} \leq \int_{(\varphi-\psi<-s-t \psi)}\left[\omega+d d^{c} \varphi\right]^{n} .$$
Taking the supremum over all u's yields the desired result. \(\square\)

We will also need the following elementary observation:
Lemma 2.3. Let $f: \mathbb{R}^{+} \rightarrow \mathbb{R}^{+}$be a decreasing right-continuous function such that $\lim _{+\infty} f=0$. Assume there exists $\alpha, B>0$ such that $f$ satisfies
$$H(\alpha, B) \quad t f(s+t) \leq B[f(s)]^{1+\alpha}, \forall s>0, \forall 0 \leq t \leq 1 .$$

Then there exists $S_{\infty}=S_{\infty}(\alpha, B) \in \mathbb{R}^{+}$such that $f(s)=0$ for all $s \geq S_{\infty}$.
Proof. Fix $s_{0}>0$ large enough so that $f\left(s_{0}\right)^{\alpha}<1 / 2 B$. We define a sequence $\left(s_{j}\right) \in \mathbb{R}_{+}^{\mathbb{N}}$ by induction in the following way. If $f\left(s_{0}\right)=0$ we stop here, otherwise we set
$$s_{1}:=\sup \left\{s>s_{0} / f(s)>\frac{1}{2} f\left(s_{0}\right)\right\} .$$
Observe that $s_{1} \leq 1+s_{0}$ thanks to $H(\alpha, B)$ and by definition of $s_{0}$.
Since $f$ is right-continuous we get $f\left(s_{1}\right) \leq f\left(s_{0}\right) / 2$. If $f\left(s_{1}\right)=0$ we stop here, otherwise we go on by induction, setting
$$s_{j+1}:=\sup \left\{s>s_{j} / f(s)>\frac{1}{2} f\left(s_{j}\right)\right\} .$$
At each step $f\left(s_{j+1}\right) \leq f\left(s_{j}\right) / 2$ and $s_{j+1} \leq 1+s_{j}$. However the sequence $\left(s_{j}\right)$ does not grow too fast. It follows indeed from $H(\alpha, B)$ that if $s \in] s_{j}, s_{j+1}[$,
$$\left(s-s_{j}\right) f(s) \leq B f\left(s_{j}\right)^{1+\alpha} \leq 2 B f(s) f\left(s_{j}\right)^{\alpha},$$
since $f\left(s_{j}\right) / 2 \leq f(s) \leq f\left(s_{j}\right)$ on the interval $\left[s_{j}, s_{j+1}\right]$. We infer
$$s_{j+1}-s_{j} \leq 2 B f\left(s_{j}\right)^{\alpha} \leq 2 B 2^{-j \alpha} f\left(s_{0}\right)^{\alpha} \leq 2^{-j \alpha} .$$

Thus the sequence $\left(s_{j}\right)$ is bounded from above, with limit
$$S_{\infty}=s_{0}+\sum_{j \geq 0}\left(s_{j+1}-s_{j}\right) \leq s_{0}+\frac{2 B f\left(s_{0}\right)^{\alpha}}{1-2^{-\alpha}} \leq s_{0}+\frac{1}{1-2^{-\alpha}} .$$ \(\square\)

Remarks 2.4. Observe that the starting time $s_{0}(f, \alpha, B)$ is invariant under dilatation $f \mapsto \lambda f$, which transforms $B$ into $B / \lambda^{\alpha}$. Note also that if $f(0)^{\alpha}<$ $1 / 2 B$, then we can take $s_{0}=0$, hence we get in this case
$$S_{\infty} \leq \frac{2 B}{1-2^{-\alpha}}[f(0)]^{\alpha} .$$

To see how previous lemmas can be used, we first prove that the unique solution $\varphi \in \mathcal{E}^{1}(X, \omega)$ given by proposition 1.4 is bounded.
$A$ uniform bound on the solution. Let $\varphi \in \mathcal{E}^{1}(X, \omega)$ be the unique function such that $\mu=\left(\omega+d d^{c} \varphi\right)^{n}$ and $\sup _{X} \varphi=-1$. Set
$$f(s):=\left[\operatorname{Cap}_{\omega}(\varphi<-s)\right]^{1 / n} .$$
Observe that $f: \mathbb{R}^{+} \rightarrow \mathbb{R}^{+}$is a right-continuous decreasing function with $\lim _{+\infty} f=0$. Since $\mu=\omega_{\varphi}^{n}$ satisfies $\mathcal{H}(\alpha, A, \omega)$, it follows from lemma 2.2 applied to the function $\psi \equiv 0$ that $f$ satisfies $H(\alpha, B)$ with $B=A^{1 / n}$.

It follows from propositions 2.7 and 3.6 in [GZ 1] that $f(s) \leq C_{1} / s^{1 / n}$ for some constant $C_{1}$ which only depends on $\omega$. We can thus take a starting time $s_{0}=2^{n / \alpha} C_{1}^{n} A^{1 / \alpha}$ (see the proof of lemma 2.3) and get $f(s)=0$ for $s \geq S_{\infty}:=s_{0}+\left(1-2^{-\alpha}\right)^{-1}$ : this shows that the sets $(\varphi<-s)$ are empty if $s \geq S_{\infty}$, hence
$$\|\varphi\|_{L^{\infty}(X)} \leq 2^{n / \alpha} C_{1}^{n} A^{1 / \alpha}+\frac{1}{1-2^{-\alpha}} .$$

We are now going to use a refinement of the previous reasoning in order to show that $\varphi$ is actually continuous.

Proposition 2.5. Let $\varphi, \psi \in \mathcal{E}^{1}(X, \omega)$ be two negative functions and fix $\varepsilon>0$. Assume $\omega_{\varphi}^{n}=\mu$ satisfies $\mathcal{H}(\alpha, A, \omega)$ and $\psi$ is bounded. There exists $C=C\left(\alpha, A, \omega,\|\psi\|_{L^{\infty}(X)}\right)>0$ such that
$$\sup _{X}(\psi-\varphi) \leq \varepsilon+C\left[\operatorname{Cap}_{\omega}(\varphi-\psi<-\varepsilon)\right]^{\alpha / n} .$$

This inequality can be interpreted as follows. Assume $\psi$ is also a solution to a Monge-Ampère equation $\omega_{\psi}^{n}=\mu^{\prime}$, where $\mu^{\prime}$ also satisfies $\mathcal{H}(\alpha, A, \omega)$. Then we can interchange the roles of $\varphi$ and $\psi$ and get an upper-bound on $\|\varphi-\psi\|_{L^{\infty}(X)}$. The proposition then tells us that if $\varphi$ and $\psi$ are close in capacity, they are close in $\mathcal{C}^{0}$-norm.

Proof. Set $M:=\|\psi\|_{L^{\infty}(X)}$. Observe that when $t \geq 0,(\varphi-\psi<-s-t \psi) \subset$ $(\varphi-\psi<-s+t M)$, hence it follows from lemma 2.2 that for all $s>0$, $0 \leq t \leq 1$,
$$t^{n} C a p_{\omega}(\varphi-\psi<-s-t) \leq(1+M)^{n} \int_{(\varphi-\psi<-s)} \omega_{\varphi}^{n},$$
using the obvious substitutions $s \mapsto s-M t, t \mapsto(1+M) t$. Since $\mu=\omega_{\varphi}^{n}$ satisfies $\mathcal{H}(\alpha, A, \omega)$, we infer
$$t^{n} C a p_{\omega}(\varphi-\psi<-s-t) \leq A(1+M)^{n} C a p_{\omega}(\varphi-\psi<-s)^{1+\alpha} .$$
Consider
$$f(s):=\left[\operatorname{Cap}_{\omega}(\varphi-\psi<-s-\varepsilon)\right]^{1 / n}, s>0 .$$
Then $f$ satisfies the condition $H(\alpha, B)$ of lemma 2.3 with $B=(1+M) A^{1 / n}$. Assume $f(0)=[\operatorname{Cap} \omega(\varphi-\psi<-\varepsilon)]^{1 / n}<\frac{1}{(2 B)^{1 / \alpha}}$. It follows in this case from Remarks 2.4 that $f(s)=0$ for $s \geq S_{\infty}$, where
$$S_{\infty} \leq \frac{2 B}{1-2^{-\alpha}}\left[\operatorname{Cap}_{\omega}(\varphi-\psi<-\varepsilon)\right]^{\alpha / n}$$
Therefore the sets $\{\varphi-\psi<-s-\varepsilon\}$ are empty for $s>S_{\infty}$, hence
$$\sup _{X}(\psi-\varphi) \leq \varepsilon+S_{\infty} \leq \varepsilon+\frac{2(1+M) A^{1 / n}}{1-2^{-\alpha}}\left[\operatorname{Cap}_{\omega}(\varphi-\psi<-\varepsilon)\right]^{\alpha / n} .$$
Thus we can take here $C \geq 2 B /\left(1-2^{-\alpha}\right)$.
If $f(0)=\left[\operatorname{Cap}_{\omega}(\varphi-\psi<-\varepsilon)\right]^{1 / n} \geq(2 B)^{-1 / \alpha}$, then
$$\sup _{X}(\psi-\varphi) \leq-\inf _{X} \varphi \leq C_{2}(\alpha, A, \omega),$$
by (2), hence it suffices to take $C \geq 2 B C_{2}$ to conclude. \(\square\)

Proof of theorem 2.1 Let $\varphi \in \mathcal{E}^{1}(X, \omega)$ be the unique solution to the normalized Monge-Ampère equation $\mu=\left(\omega+d d^{c} \varphi\right)^{n}, \sup _{X} \varphi=-1$ (see proposition 1.4). It follows from (2) that $\varphi$ is bounded.

Since $\omega$ is semi-positive and big, it follows from a result of J.P.Demailly (see [BK] for an elementary proof) that one can approximate any $\omega$-psh function by a decreasing sequence of smooth $\omega$-psh functions. Let $\varphi_{j}$ be such an approximating sequence for $\varphi$. Since $\sup _{X} \varphi=-1$, we can assume $\varphi_{j} \leq 0$. Since $\varphi$ is bounded and $\varphi_{j} \geq \varphi$, the functions $\varphi_{j}$ are uniformly bounded on $X$.

Observe that $\varphi_{j}$ converges towards $\varphi$ in capacity (see proposition 3.7 in [GZ 1]), hence $\lim \operatorname{Cap}_{\omega}\left(\varphi-\varphi_{j}<-\varepsilon\right)=0$, for all $\varepsilon>0$. It follows therefore from proposition 2.5 (applied with $\psi=\varphi_{j}$ ) that for all $\varepsilon>0$,
$$\lim _{j \rightarrow+\infty}\left\|\varphi-\varphi_{j}\right\|_{L^{\infty}(X)}=\lim _{j \rightarrow+\infty} \sup _{X}\left(\varphi_{j}-\varphi\right) \leq \varepsilon .$$
Thus $\left(\varphi_{j}\right)$ converges uniformly towards $\varphi$, hence $\varphi$ is continuous. \(\square\)

\section*{3. More regularity}
3.1. Measures with density. We now turn to the study of the complex Monge-Ampère equation
$$\left(\omega+d d^{c} \varphi\right)^{n}=\mu, \text { when } \mu=f \omega^{n}$$
is a measure with density $0 \leq f \in L^{p}\left(\omega^{n}\right), p>1$.

Proposition 3.1. Assume $\mu=f \omega^{n}$ is a probability measure with density $0 \leq f \in L^{p}(X)$, for some $p>1$. Then for any $\alpha>0$, there exists $A_{\alpha}>0$ such that $\mu$ satisfies $\mathcal{H}\left(\alpha, A_{\alpha}, \omega\right)$.

Proof. It is enough to establish $\mathcal{H}\left(\alpha, A_{\alpha}, \omega\right)$ for compact subsets, by regularity of $\mu$ and $C a p_{\omega}$. Let $K$ be a compact subset of $X$. It follows from Hölder's inequality that
$$0 \leq \mu(K) \leq\|f\|_{L^{p}\left(\omega^{n}\right)}\left[\operatorname{Vol}_{\omega}(K)\right]^{1 / q},$$
where $1 / p+1 / q=1$. Note that $\|f\|_{L^{p}\left(\omega^{n}\right)}=1$ since we assume $\mu$ is a probability measure. We claim that
$$\operatorname{Vol}_{\omega}(K) \leq C_{\omega} \exp \left[-\left(\operatorname{Cap}_{\omega}(K)\right)^{-\gamma_{\omega} / n}\right],$$
for some constants $C_{\omega}, \gamma_{\omega}>0$ that only depend on $\omega$. We will be done if we can prove (4) since we can then check by elementary computations that $\exp \left(-x^{-\delta}\right)$ is dominated from above by $A_{\alpha} x^{\alpha}$, for all $x \in[0,1]$.

The set of functions $\mathcal{F}_{0}:=\left\{\varphi \in P S H(X, \omega) / \sup _{X} \varphi=0\right\}$ is compact in $L^{1}(X)$ (see proposition 2.7, [GZ 1]). These functions have Lelong numbers $\nu(\varphi, x) \leq \nu_{\omega}$ bounded from above by a uniform constant. It follows therefore from Skoda's uniform integrability theorem [Z], that
$$\sup _{\varphi \in \mathcal{F}_{0}} \int \exp \left[-\frac{2 \varphi}{\nu_{\omega}+1}\right] \omega^{n} \leq C_{2}<+\infty .$$
Set $\gamma_{\omega}:=2 /\left(\nu_{\omega}+1\right)>0$ and let
$$V_{K, \omega}^{*}(x):=(\sup \{\varphi(x) / \varphi \in P S H(X, \omega), \varphi \leq 0 \text { on } K\})^{*}$$
denote the Siciak extremal function of $K$ (see section 5.1 in [GZ 1]). Then
$$\operatorname{Vol}_{\omega}(K) \leq \int_{X} \exp \left(-\gamma_{\omega} V_{K, \omega}^{*}\right) \omega^{n} \leq C_{2} T_{\omega}(K)^{\gamma_{\omega}},$$
where $T_{\omega}(K):=\exp \left(-\sup _{X} V_{K, \omega}^{*}\right)$ denote the Alexander capacity of $K$ (see section 5.2 in [GZ 2]). It follows now from theorem 7.1 in [GZ 1] that
$$T_{\omega}(K) \leq e \exp \left[-\operatorname{Cap}_{\omega}(K)^{-1 / n}\right],$$
which yields (4). \(\square\)

It follows therefore from theorem 2.1 that there exists a unique continuous function $\varphi \in P S H(X, \omega)$ such that
$$\mu=f \omega^{n}=\left(\omega+d d^{c} \varphi\right)^{n}, \text { with } \sup _{X} \varphi=-1,$$
when $0 \leq f \in L^{p}\left(\omega^{n}\right), p>1$, with $\int_{X} f \omega^{n}=1$.
Actually we will be interested in measures with $L^{p}$-density with respect to a positive definite volume form $d \lambda$, while the smooth measure $\omega^{n}$ may vanish along a divisor. This does not make much difference, as follows from Hölder's inequality:

Lemma 3.2. Let $V$ be a $n$-dimensional compact normal Kähler space and $\Omega$ be a smooth Kähler form on $V$. Let $\pi: X \rightarrow V$ a resolution, $\omega=\pi^{*} \Omega$, and let $d \lambda$ be a positive definite smooth volume form on $X$.

If $\mu=f_{1} d \lambda$, with $f_{1} \in L^{p}(X, d \lambda)$ for some $p>1$, then there exists $p^{\prime}>1$ such that $\mu=f \omega^{n}$ and $f \in L^{p^{\prime}}\left(X, \omega^{n}\right)$.

Proof. Observe that $\omega^{n}=E d \lambda$ for some smooth density $E \geq 0$ which vanishes along the exceptional divisor of $\pi$, thus
$$\mu=f_{1} d \lambda=f \omega^{n}, \text { where } f=f_{1} / E .$$

Fix local coordinates $\left(z^{i}\right)_{1 \leq i \leq n}$ on a polydisk $\mathbb{D} \subset X$ and a local embedding $F: V \rightarrow \mathbb{C}^{m}$. Note that $E$ is comparable to $\left|\frac{\partial F}{\partial z^{1}} \wedge \ldots \wedge \frac{\partial F}{\partial z^{1}}\right|^{2} \simeq$ $\sum_{i=1}^{r}\left|f_{i}\right|^{2}, f_{i}$ being holomorphic on $\mathbb{D}$. Therefore $E \in L_{l o c}^{\infty}(\mathbb{D})$ and $E^{-\alpha} \in$ $L_{l o c}^{1}(\mathbb{D}, d \lambda)$ for some $0<\alpha<1$.

Choose $0<\alpha^{\prime}<\alpha$ such that $\frac{1}{p}+\frac{1}{\alpha}=\frac{1}{\alpha^{\prime}}$. Then $f^{\alpha^{\prime}}=f_{1}^{\alpha^{\prime}} E^{-\alpha^{\prime}}$ is the product of a function in $L^{p / \alpha^{\prime}}(d \lambda)$ and a function in $L^{\alpha / \alpha^{\prime}}(d \lambda)$, hence it is in $L_{\text {loc }}^{1}(\mathbb{D}, d \lambda)$ by Hölder's inequality. A second application of Hölder's inequality yields
$$\int_{\mathbb{D}} f^{1+\varepsilon} \omega^{n}=\int_{\mathbb{D}} f^{\epsilon} f_{1} d \lambda \leq\left(\int_{\mathbb{D}} f^{\epsilon q} d \lambda\right)^{1 / q}\left(\int_{\mathbb{D}} f_{1}^{p} d \lambda\right)^{1 / p}<+\infty,$$
where $q$ denotes the conjugate exponent to $p$. This shows that $f \in L^{p^{\prime}}\left(\omega^{n}\right)$ if $p^{\prime}=1+\varepsilon>1$ is chosen so small that $\varepsilon q<\alpha^{\prime}$. \(\square\)

\subsection*{3.2. Hölder continuity.}

Proposition 3.3. Assume $\omega_{\varphi}^{n}=f \omega^{n}, \omega_{\psi}=g \omega^{n}$, where $\varphi, \psi \in P S H(X, \omega)$ are continuous and $f, g \in L^{p}\left(\omega^{n}\right), p>1$. Then for all $0<\gamma<2 /(2+n q)$,
$$\|\varphi-\psi\|_{L^{\infty}(X)} \leq C\|\varphi-\psi\|_{L^{2}\left(\omega^{n}\right)}^{\gamma},$$
where $q=p /(p-1)$ denotes the conjugate exponent to $p$.
Proof. Fix $\varepsilon>0$ and $\alpha>0$ to be chosen later. It follows from (2) and propositions 2.5, 3.1 that
$$\|\varphi-\psi\|_{L^{\infty}(X)} \leq \varepsilon+C_{1}\left[\operatorname{Cap}_{\omega}(|\varphi-\psi|>\varepsilon)\right]^{\alpha / n} .$$
Applying the refined version of lemma 2.2 which involves the uniform bound on $\|\varphi\|_{L^{\infty}(X)},\|\psi\|_{L^{\infty}(X)}$ (see inequality (3)), we obtain
$$\operatorname{Cap}_{\omega}(|\varphi-\psi|>\varepsilon) \leq \frac{C_{2}}{\varepsilon^{n+2 / q}} \int_{X}|\varphi-\psi|^{2 / q}(f+g) \omega^{n} .$$
It follows thus from Hölder's inequality that
$$\operatorname{Cap}_{\omega}(|\varphi-\psi|>\varepsilon) \leq \frac{C_{3}\|f+g\|_{L^{p}}}{\varepsilon^{n+2 / q}}\left[\|\varphi-\psi\|_{L^{2}\left(\omega^{n}\right)}\right]^{2 / q} .$$
Choose now $\varepsilon:=\|\varphi-\psi\|_{L^{2}}^{\omega}$ where $0<\gamma<2 /(2+n q)$. Then
$$\operatorname{Cap}_{\omega}(|\varphi-\psi|>\varepsilon) \leq C_{4}\left[\|\varphi-\psi\|_{L^{2}}\right]^{2 / q-\gamma(n+2 / q)} .$$
We infer
$$\|\varphi-\psi\|_{L^{\infty}(X)} \leq\|\varphi-\psi\|_{L^{2}}^{\gamma}+C_{5}\|\varphi-\psi\|_{L^{2}}^{\gamma^{\prime}}, \quad \text { where } \gamma^{\prime}=\frac{\alpha}{n}[2 / q-\gamma(n+2 / q)] .$$
We finally choose $\alpha>0$ so large that $\gamma \leq \gamma^{\prime}$ and adjust the value of the constant $C$ : this yields the desired estimate. \(\square\)

Being able to control the $L^{\infty}$-norm of $\varphi-\psi$ by its $L^{2}$-norm is a powerful tool. If for instance $\psi=\varphi_{j}, \varphi$ satisfy the assumptions of proposition 3.2 - with $\varphi_{j}$ being uniformly bounded -, and $\varphi_{j} \rightarrow \varphi$ in $L^{1}$, then $\varphi_{j} \rightarrow \varphi$ in $L^{2}\left(\omega^{n}\right)$, hence $\left(\varphi_{j}\right)$ actually uniformly converges towards $\varphi$. This yields the continuity of the map
$$f \in L^{p}\left(\omega^{n}\right) \mapsto \varphi \in \mathcal{C}^{0}(X),$$
where $\varphi$ is the unique $\omega$-psh solution to $\left(\omega+d d^{c} \varphi\right)^{n}=f \omega^{n}, \sup _{X} \varphi=-1$. Thus Theorem A is proved.

We now give an application of this estimate, which is new even when the form $\omega$ is Kähler, but requires the manifold $X$ to be homogeneous, i.e. such that its group of holomorphic automorphisms acts transitively on it. ${ }^{4}$.

Theorem 3.4. Assume $X$ is a homogeneous manifold. If $\mu=f \omega^{n}$ is a probability measure with density $0 \leq f \in L^{p}\left(\omega^{n}\right), p>1$, then the unique so-lution $\varphi \in P S H(X, \omega) \in \mathcal{C}^{0}(X)$ to the normalized Monge-Ampère equation
$$\left(\omega+d d^{c} \varphi\right)^{n}=\mu=f \omega^{n}, \sup _{X} \varphi=-1,$$
is Hölder continuous of exponent $\gamma>0$, for all $\gamma<2 /(2+n q)$, where $q=p /(p-1)$ is the conjugate exponent to $p$.

Proof. When $\operatorname{Aut}(X)$, the group of holomorphic automorphisms of $X$, acts transitively on $X$, one can regularize $\omega$-psh functions by averaging over the Haar measure of the connected component of the identity of $\operatorname{Aut}(X)$. This is very similar to the way one regularizes psh functions in $\mathbb{C}^{n}$ by using convolutions with an approximation of the identity for the convolution product. We refer the reader to [Hu] and the Appendix of [G] for more details.

Let $\varphi_{h}$ be the $\omega$-psh function which is the translate of $\varphi$ by an automorphism which is at distance $h$ from identity. We use the notation $\varphi_{h}$ by analogy with the $\mathbb{C}^{n}$-situation, where $\varphi_{h}(x)=\varphi(x+h)$. Since $\varphi$ is bounded, it has gradient in $L^{2}$, hence
$$\left\|\varphi_{h}-\varphi\right\|_{L^{2}} \leq C|h|,$$
by using Cauchy-Schwarz inequality in a local chart. We can thus apply proposition 3.2 to obtain that
$$\left\|\varphi_{h}-\varphi\right\|_{L^{\infty}} \leq C^{\prime}|h|^{\gamma},$$
for all $\gamma<2 /(2+n q)$. Since $\varphi_{h}(x) \simeq \varphi(x+h)$ in a local chart, this precisely means that $\varphi$ is Hölder-continuous of exponent $\gamma$. \(\square\)

\subsection*{3.3. Regularity on the smooth locus.}

Theorem 3.5. Let $X$ be projective algebraic complex manifold, $\omega_{0}$ a smooth semi Kähler form that is Kähler outside a complex subvariety $S \subset X$, and fix $\Omega$ be a Kähler form on $X$. Assume that $\omega_{o}^{n}=D \Omega^{n}$, where $D^{-\varepsilon}$ is in $L^{1}\left(\Omega^{n}\right)$, and that $\left[\omega_{0}\right],[\Omega] \in N S_{\mathbb{R}}(X)$.

\footnotetext{
${ }^{4}$ In particular, the cohomology class of $\omega$ is Kähler and $\omega$ itself can be supposed to be Kähler without loss of generality.
}

Let $s_{1}, \ldots, s_{p}$ (resp. $t_{1}, \ldots, t_{q}$ ) be holomorphic sections of some line bundle $L$ (resp $L^{\prime}$ ) on $X$. Fix $k \in \mathbb{R}_{\geq 0}, l \in \mathbb{R}_{\geq 0}$ and $F \in \mathcal{C}^{\infty}(X, \mathbb{R})$. Assume that
$$\int_{X} \frac{1}{\left|t_{1}\right|^{2 l}+\ldots+\left|t_{q}\right|^{2 l}} \Omega^{n}<\infty \text { and } \int_{X} \frac{\left|s_{1}\right|^{2 k}+\ldots+\left|s_{p}\right|^{2 k}}{\left|t_{1}\right|^{2 l}+\ldots+\left|t_{q}\right|^{2 l}} e^{F} \Omega^{n}=\int_{X} \Omega^{n} .$$

Then the unique continuous function $\varphi \in P S H\left(X, \omega_{0}\right)$ such that
$$\left(\omega_{0}+d d^{c} \varphi\right)^{n}=\frac{\left|s_{1}\right|^{2 k}+\ldots+\left|s_{p}\right|^{2 k}}{\left|t_{1}\right|^{2 l}+\ldots+\left|t_{q}\right|^{2 l}} e^{F} \Omega^{n} \quad \text { and } \sup _{X} \varphi=-1$$
is smooth outside $B=S \cup \cap_{i}\left\{s_{i}=0\right\} \cup \cap_{i}\left\{t_{i}=0\right\}$.
Remark 3.6. This result should be compared with [Y], Theorem 8. Yau's result is stronger in many respects (there is no projectivity/rationality assumption and it gives a more precise regularity theory); on the other hand the conditions on the poles of the L.H.S. is less optimal than here.

We expect the projectivity/rationality assumptions to be superfluous. We also expect that a finer regularity theory might be developed for singular KE metrics depending on a finer analysis of the klt singularities involved.

The rest of this subsection will be devoted to the proof of Theorem 3.5. For the reader's convenience, we will treat two special cases before tackling the general case ${ }^{5}$

Preliminary considerations. Thanks to Lemma 3.2 - here we use that $D^{-\varepsilon} \in$ $L^{1}$ - and Theorem 2.1, for every $t \in[0,1]$ there is a unique continuous function $\varphi_{t} \in P S H\left(X, \omega_{0}+t \Omega\right)$ such that
$$\left(\omega_{o}+t \Omega+d d^{c} \varphi_{t}\right)^{n}=C_{t} \frac{\left|s_{1}\right|^{2 k}+\ldots+\left|s_{p}\right|^{2 k}}{\left|t_{1}\right|^{2 l}+\ldots+\left|t_{q}\right|^{2 l}} e^{F} \Omega^{n} \text { and } \sup _{X} \varphi_{t}=-1,$$
where $C_{t}>0$ is an adequate normalisation constant and $\left\|\varphi_{t}\right\|_{\mathcal{C}^{0}(X)}$ is uniformly bounded by a constant independant of $t \geq 0$.

We cannot use right away [Y], Theorem 8 p. 403, to ensure that $\left(\varphi_{t}\right)$ be smooth outside $B$ for $t>0$, since our integral condition is stronger than his. However we can use [Y], Thm 3, p 365 to conclude that, in case $\cap_{i}\left\{t_{i}=0\right\}=\emptyset,\left(\varphi_{t}\right)$ is smooth outside $B$ and $d d^{c} \varphi_{t}$ is a form whose coefficients are globally bounded on $X$, hence $\varphi_{t} \in \mathcal{C}^{1,1}(X)$ for $t>0$. Since this does not imply ellipticity if $\cap_{i}\left\{s_{i}=0\right\} \neq \emptyset$, this does not imply higher regularity on the whole of $X$.

The required uniformity in $t>0$ is not proved in [Y]. To deal with this case, we use a nice trick due to H.Tsuji [Ts].

The simplest case. First, assume $\cap_{i}\left\{s_{i}=0\right\} \cup \cap_{i}\left\{t_{i}=0\right\}=\emptyset$. Hence the family of equations under consideration can be rewritten as:
$$\left(\omega_{o}+t \Omega+d d^{c} \varphi_{t}\right)^{n}=C_{t} e^{F} \Omega^{n},$$
$F$ being smooth.
Tsuji's trick is as follows. By Kodaira's lemma, there exists $E$ an effective Cartier divisor of $X$ such that $\left[\omega_{o}\right]=\left[\kappa_{\varepsilon}\right]+\varepsilon[E]$ where $\left[\kappa_{\varepsilon}\right]$ is ample, hence

\footnotetext{
${ }^{5}$ Notice that apart from the $\mathcal{C}^{0}$-estimate with degenerate L.H.S., the methods used here are standard and in [Y], [Ts] and [Ko]. Higher regularity in [TZ] is treated along similar lines given the $L^{\infty}$-estimate the authors announce.
}
we may choose a representative $\kappa_{\varepsilon}$ which is a Kähler form for every $\varepsilon>0$ small enough. We may actually assume $E$ contains $B$ and use a family of $E$ such that $\cap \operatorname{Supp}(E)=B$, by Nakamaye's theorem on base loci [Na].

Actually, despite the notation, it will NOT be necessary to let $\varepsilon$ decrease to $0^{6}$ and we will fix once for all such an $\varepsilon>0$.

Let $\sigma \in H^{0}\left(X, \mathcal{O}_{X}(E)\right)$ be the canonical section vanishing on $E$ with the appropriate multiplicity. We can fix a smooth hermitian metric on this line bundle such that the Poincaré Lelong equation holds,
$$\omega_{o}=\kappa_{\varepsilon}+\varepsilon[E]-\varepsilon d d^{c} \log |\sigma|^{2} .$$

The function $\varphi_{t}:=\varphi_{t}-\varepsilon \log |\sigma|^{2}$ is smooth in $X \backslash E$ and is a classical solution to the PDE
$$\left(\kappa_{\varepsilon}+t \Omega+d d^{c} \varphi_{t}\right)^{n}=e^{F_{\varepsilon, t}}\left(\kappa_{\varepsilon}+t \Omega\right)^{n},$$
where $\left(F_{\varepsilon, t}\right)_{1 \geq t>0}$ is uniformly bounded in the $\mathcal{C}^{\infty}(X)$-topology of functions and $\kappa_{t}=\kappa_{\varepsilon}+t \Omega$ is uniformly bounded in the $\mathcal{C}^{\infty}$-topology of Kähler forms on $X$.

We can use the result of the calculation in [Y], section 2. The important formula is (2.22) p. 351 and in a subsidiary fashion (2.21). In these formulae, at each point $p \in X-E$, an adequate system of normal coordinates for $\kappa_{t}$ is constructed and comparing the notations here and there, we substitute $n$ for $m, \kappa_{t}$ for $g_{i \bar{j}}, \kappa_{t}+d d^{c} \varphi_{t}$ for $g_{i \bar{j}}^{\prime}, \varphi_{t}$ for $\varphi$ and $F_{\varepsilon, t}$ for $F$. The operator $\Delta$ is the Laplace operator (with the analyst's sign) of $\kappa_{t}$ and $\Delta^{\prime}$ the Laplace operator of $\kappa_{t}+d d^{c} \varphi_{t}$. Also $R_{\text {iill }}=R_{\text {iill }}^{t}$ is the holomorphic bissectional curvature of $\kappa_{t}$ expressed in the above system of normal coordinates.

Since $\kappa_{t}$ is uniformly bounded in the $\mathcal{C}^{2}$ topology of Kähler forms then certainly there is constant $C=C_{\varepsilon}$ independent of $t$ such that (2.21) holds and $C^{\prime}$ also independent of $t$ such that $C^{\prime}>\inf R_{\text {iill }}^{t}$.

After these substitutions are made, (2.22) p. 351 reads:
$$e^{C \varphi_{t}} \Delta^{\prime}\left(e^{-C \varphi_{t}}\left(n+\Delta \varphi_{t}\right)\right) \geq \Delta\left(F_{\varepsilon, t}\right)-n^{2} C^{\prime}-C n\left(n+\Delta \varphi_{t}\right)+e^{-\frac{F_{\varepsilon, t}}{n-1}}\left(n+\Delta \varphi_{t}\right)^{\frac{n}{n-1}}$$

We can fix constants $C_{i}$ independent of $t$ such that
$$\Delta F_{\varepsilon, t} \geq C_{1} \quad \text { and } \quad e^{-F_{\varepsilon, t} / n-1} \geq C_{3}>0 .$$
Thus setting $y=n+\Delta \varphi_{t}$ yields
$$e^{C \varphi_{t}} \Delta^{\prime}\left(e^{-C \varphi_{t}}\left(n+\Delta \varphi_{t}\right)\right) \geq C_{5}+C_{6} y+e^{C_{7}} y^{\frac{m}{m-1}} .$$

Now by definition
$$e^{-C \varphi_{t}}\left(n+\Delta \varphi_{t}\right)=|\sigma|^{+C \varepsilon} e^{-C \varphi_{t}}\left(n+\Delta \varphi_{t}+\varepsilon \Delta \log |\sigma|^{2}\right) .$$

For each $t>0$ the functions $\varphi_{t}, \varepsilon \Delta \log |\sigma|^{2}$ and $\Delta \varphi_{t}$ are bounded on $X$. Hence the positive function $e^{-C \varphi_{t}}\left(n+\Delta \varphi_{t}\right)$ is continuous on $X$, vanishes on $E$ and is smooth on $X-E$. Its maximum is achieved at some point $p_{t} \notin E$. It follows from the maximum principle that
$$0 \geq C_{5}+C_{6} y+e^{C_{7}} y^{\frac{n}{n-1}} \text { at point } y=y\left(p_{t}\right) .$$

Therefore $y \leq C_{8}$ with a constant independent of $t>0$. Now $e^{-C \varphi_{t}\left(p_{t}\right)}=$ $\left|\sigma\left(p_{t}\right)\right|^{+C \varepsilon} e^{-C \varphi_{t}\left(p_{t}\right)}$. Using the uniform $\mathcal{C}^{0}$ estimate for $\varphi_{t}$, we get $0 \leq(n+$

\footnotetext{
${ }^{6}$ This technical device could be useful to study finer regularity results
}
$\left.\Delta_{t} \varphi_{t}\right) \leq C_{9} e^{+C \varphi_{t}}$. Since $\left|\varphi_{t}\right|$ and $\varepsilon \Delta \log |\sigma|^{2}$ are uniformly bounded by a constant independent of $t>0$, we infer
$$\left(n+\Delta_{t} \varphi_{t}\right) \leq C_{10}|\sigma|^{-C \varepsilon}=C_{10}|\sigma|^{-C_{\varepsilon} \varepsilon} .$$
This yields a $t$-independent $\mathcal{C}^{0}$ - estimate of $d d^{c} \varphi_{t}$ on the compact subsets of $X-E^{7}$.

Standard arguments of the theory of complex Monge-Ampère equations give an interior estimate of $\varphi_{t}$ in $\mathcal{C}_{\text {loc }}^{k, \alpha}(X-E)$ for every $\left.k \geq 2, \alpha \in\right] 0,1[$ which is independent of $t>0$ (see for instance Theorem 5.1, p. 15 in [Bl2]). Hence the family $\left(\varphi_{t}\right)_{t>0}$ is precompact in every $\mathcal{C}_{\text {loc }}^{k, \alpha}(X-E)$. Its cluster values are cluster values in $\mathcal{C}^{O}(X-E)$ hence they are all equal to $\left.\varphi\right|_{X-E}$. This implies $\varphi \in \mathcal{C}_{\text {loc }}^{k, \alpha}(X-E)$, hence that $\varphi \in \mathcal{C}^{\infty}(X-E)$.

Case where $\cap_{i}\left\{t_{i}=0\right\}=\emptyset .{ }^{8}$ We study here the equation
$$\left(\omega_{o}+t \Omega+d d^{c} \varphi_{t}\right)^{n}=C_{t}\left(\left|s_{1}\right|^{2 k}+\ldots+\left|s_{p}\right|^{2 k}\right) e^{F} \Omega^{n}$$

The first few steps of the preceding argument can be repeated without changes. Next we apply formula (2.22) in [Y] as earlier, except that we set $F=F_{\varepsilon, t}+\log \|s\|^{(2 k)}$, where $\|s\|^{(2 k)}:=\left|s_{1}\right|^{2 k}+\ldots+\left|s_{p}\right|^{2 k}$. This yields
$$\begin{aligned}
e^{C \varphi_{t}} \Delta^{\prime}\left(e^{-C \varphi_{t}}\left(n+\Delta \varphi_{t}\right)\right) \geq & \Delta F_{\varepsilon, t}+\Delta \log \|s\|^{(2 k)}-n^{2} C^{\prime}-C n\left(n+\Delta \varphi_{t}\right) \\
& +\left(\frac{e^{-F_{\varepsilon, t}}}{\|s\|^{(2 k)}}\right)^{1 /(n-1)}\left(n+\Delta \varphi_{t}\right)^{\frac{n}{n-1}}
\end{aligned}$$

We recall the two preceding inequalities and observe two new ones that are available:
$$\begin{aligned}
\Delta F_{\varepsilon, t} \geq C_{1} \quad & \text { and } \quad e^{-F_{\varepsilon, t} / n-1} \geq C_{3}>0 ; \\
\Delta \log \|s\|^{(2 k)} \geq C_{2} \quad \text { and } \quad & C_{4} \geq\|s\|^{(2 k)} .
\end{aligned}$$

Setting as earlier $y=n+\Delta \varphi_{t}$, we get
$$e^{C \varphi_{t}} \Delta^{\prime}\left(e^{-C \varphi_{t}}\left(n+\Delta \varphi_{t}\right)\right) \geq C_{5}+C_{6} y+e^{C_{7}} y^{\frac{m}{m-1}} .$$

After this point, the proof is entirely the same as before.
Remark 3.7. In order to carry out the second order a priori estimate, one needs information that only depend on $\sup _{X} F$ and $\inf _{X} \Delta F$. This is pointed out in [Y], p. 351, and it is the basis for the proof of [Y], Thm 3.
3.4. Formal reduction of the general case to the second case using smooth orbifolds. In order to carry out the present argument, which in essence is just a change of variables $z \rightsquigarrow \zeta=z^{1 / m}$, we need to use analysis on certain smooth orbifolds. We will not give complete definitions since they are in the recent reference [BGK], section 2 pp. 560-564, see also [MO] and the references therein.

Let $(X, \Delta)$ be a smooth orbifold pair. By this we mean that we have the prime decomposition $\Delta=\sum_{i}\left(1-m_{i}^{-1}\right) E_{i}$ where $m_{i} \in \mathbb{N}^{*}$ is an integer. We assume that $\operatorname{supp}(\Delta)$ is a simple normal crossing divisor. Then, a classical

\footnotetext{
${ }^{7}$ Note that $C=C_{\varepsilon}$ and that $\varepsilon C_{\varepsilon}$ might blow up as $\varepsilon$ goes to 0.
${ }^{8}$ It suffices to consider this case for constructing singular KE metrics on algebraic varieties with canonical singularities
}
construction surveyed in [BGK] enables to construct an orbifold $[X, \Delta]$ with a 1-morphism of orbifolds $c:[X, \Delta] \rightarrow X$ with the following properties:
\begin{itemize}
\item[-] $c$ is the reduction to the coarse moduli space of $[X, \Delta]$.
\item[-] $c_{X-\operatorname{Supp}(\Delta)}: U:=[X, \Delta] \times_{X} \rightarrow X-\operatorname{Supp}(\Delta)$ is an isomorphism. Hence $U$ is an open suborbifold of $[X, \Delta]$ which is an old-fashioned manifold).
\item[-] For every open polydisk $\mathbb{D} \subset X$ with local coordinates $z_{1}, \ldots, z_{n}$ such that $\operatorname{Supp}(\Delta)=\left\{\prod_{j=1}^{p} z_{j}=0\right\}[X, \Delta] \times_{X} \mathbb{D}=\left[\mathbb{D}^{\prime} / G_{\text {loc }}\right]$.
In this formula, the local isotropy group is $G_{\text {loc }}=\prod_{j=1}^{p} \mathbb{Z} / m_{j} \mathbb{Z}$, $m_{j}$ is the integer multiplicity of the divisor $E_{i_{j}}$ such that $E_{i_{j}} \cap \mathbb{D}=$ $\left\{z_{j}=0\right\}, G_{\text {loc }}$ acts on the polydisk $\mathbb{D}^{\prime}$ by $\left(\zeta_{1}, \ldots, \zeta_{p}\right) .\left(z_{1}^{\prime}, \ldots, z_{n}^{\prime}\right)=$ $\left(\zeta_{1} z_{1}^{\prime}, \ldots, \zeta_{p} z_{p}^{\prime}, z_{p+1}^{\prime}, \ldots\right)^{9}$.
The orbifold 1-morphism $\left[\mathbb{D}^{\prime} / G_{l o c}\right] \rightarrow \mathbb{D}$ is induced by $\varkappa_{l o c}$ : $\left(z_{1}^{\prime}, . ., z_{n}^{\prime}\right) \mapsto\left(\left(z_{1}^{\prime}\right)^{m_{1}}, \ldots\right)$.
\item[-] For sufficiently divisible $s, c_{*} \mathcal{O}_{[X, \Delta]}\left(s K_{[X, \Delta]}\right)=\mathcal{O}_{X}\left(s\left(K_{X}+\Delta\right)\right)$.
\end{itemize}

It is possible to define all the basic concepts of Kähler geometry on orbifolds such as smooth functions, Kähler metrics, etc... The principle is to think of $\varkappa_{l o c}^{-1}$ as a (multivalued) smooth coordinate chart.

A continuous function on $[X, \Delta]$ is a continuous function on $X$. A Radon measure on $[X, \Delta]$ is a Radon measure on $X$.

A smooth function $f$ on $[X, \Delta]$ is a continuous function on $X$ such that for every local chart $\varkappa_{\text {loc }}^{*} f$ is smooth. In particular $f$ is Hölder continuous.

A Kähler metric $\Omega_{[X, \Delta]}$ on $[X, \Delta]$ is a Kähler metric $\Omega_{X-S u p p(\Delta)}$ on $X-$ $\operatorname{Supp}(\Delta)$ with the property that $\varkappa_{\text {loc }}^{*} \Omega$ extends to a smooth Kähler metric on $\mathbb{D}^{\prime}$. In particular, it also extends as a closed Kähler current on $X$ with Hölder potentials.

The pull back of a Kähler form on $X$ to $[X, \Delta]$ is a semi-Kähler form that is actually cohomologous to a Kähler class ${ }^{10}$.

Observe that $\varkappa_{l o c}^{*} d z_{l}=m_{i_{l}}\left(z_{l}^{\prime}\right)^{m_{i_{l}}-1} d z_{l}^{\prime}$, hence a smooth volume form on $[X, \Delta]$ can be interpreted as a volume form $v$ on $X-\operatorname{Supp}(\Delta)$ such that
$$v \text { is comparable to } \frac{\prod_{l=1}^{n}\left(\sqrt{-1} d z_{l} \wedge d \bar{z}_{l}\right)}{\prod_{l=1}^{p}\left|z_{l}\right|^{2\left(1-1 / m_{i_{l}}\right)}} .$$

In case the pair ( $X, l^{-1}\left(t_{1}\right)$ ) is an orbifold pair, the equation
$$\left(\omega_{o}+d d^{c} \varphi_{t}\right)^{n}=C_{t} \frac{\left|s_{1}\right|^{2 k}+\ldots+\left|s_{p}\right|^{2 k}}{\left|t_{1}\right|^{2 l}} e^{F} \Omega_{X}^{n}$$
can be interpreted on $[X, \Delta]$ as an equation of the form
$$\left(c^{*} \omega_{o}+d d^{c} \varphi_{t}\right)^{n}=C_{t}\left(\left|s_{1}\right|^{2 k}+\ldots+\left|s_{p}\right|^{2 k}\right) e^{F} \Omega_{[X, \Delta]}^{n} .$$

The method used to analyze the case where $\cap_{i}\left\{t_{i}=0\right\}=\emptyset$ extends with almost no changes to the orbifold case. Hence the unique continuous solution of equation (5) is smooth outside its singular locus if ( $X, \frac{1}{l}\left(t_{1}\right)$ ) is an orbifold pair.

\footnotetext{
${ }^{9}$ The usual isomorphism of $\mathbb{Z} / m \mathbb{Z}$ with the group of $m$-th root of unity is used.
${ }^{10}$ Here no reference can be given. But it is easy to extend the gluing methods for Kähler forms developed in [Dem 3] and [Pa] to orbifolds. Hence [DP] extends to Kähler orbifolds.
}

Under the more general hypothesis that $\int_{X}\left|t_{1}\right|^{-2 l}<\infty$ and $\frac{1}{l}\left(t_{1}\right)$ is a divisor with simple normal crossings, then we can construct an orbifold pair ( $X, \Delta$ ) with $0 \leq \frac{1}{l}\left(t_{1}\right) \leq \Delta$ and we are back to the previous case.

For the most general case, consider the ideal $\mathcal{I}$ generated by the $t_{i}$ and fix $\mu: X^{\prime} \rightarrow X$ a log resolution of $(X, \mathcal{I})$. Then we are back to the previous case, with an equation on $X^{\prime}$. This ends the proof of Theorem 3.6.

In certain rare circumstances, there is a finite smooth covering $Y \rightarrow X$ such that $Y / G=X$ and $[Y / G]=[X, \Delta]$ and the argument we use here reduces to a $G$-equivariant argument on $Y$.

Remarks 3.8. If we start with $\omega_{o}$ Kähler, and the log-resolution is non trivial, $\mu^{*} \omega_{o}$ is not Kähler anymore.

This method that dates back to [Ko] can be used to prove a variant of [Y], Theorem 7 p. 399 where the divisor of $s_{2}$ is a simple normal crossing divisor, under the sole assumption that $\int_{M}\left|s_{2}\right|^{-2 k_{2}}<\infty$.

Now, it could not have been used to prove Theorem 8 p. 403 in 1978 since log-resolutions force the use of Monge-Ampère equations with degenerate L.H.S, for which the $\mathcal{C}^{0}$-estimate proved here was not available then.

\section*{4. More Monge-Ampère equations}

As we aim at constructing singular Kähler-Einstein metrics, it is important to consider Monge-Ampère equations of the following type,
$$\left(\omega+d d^{c} \varphi\right)^{n}=e^{t \varphi} \mu,$$
where $\mu$ is a probability measure which satisfies condition $\mathcal{H}(\alpha, A, \omega)$ (see definition 1.3), and $t$ is a real parameter. The case $t=0$, treated in Theorem 2.1, will correspond to Ricci-flat metrics (see section 6). We focus here on case $t>0$.

Theorem 4.1. Let $\mu$ be a probability measure which satisfies condition $\mathcal{H}(\alpha, A, \omega)$ and fix $t>0$. There exists a unique function $\varphi_{t} \in P S H(X, \omega) \cap$ $\mathcal{C}^{0}(X)$ such that
$$\left(\omega+d d^{c} \varphi_{t}\right)^{n}=e^{t \varphi} \mu .$$
Proof. The uniqueness easily follows from the comparison principle as we explain in proposition 4.3 below. We are going to prove the existence by a fixed point method.

Fix $\psi \in \mathcal{E}^{1}(X, \omega)$ such that $\int_{X} \psi d \mu=0$, and let us consider the equation
$$M A(\psi) \quad\left(\omega+d d^{c} \varphi\right)^{n}=e^{t \psi-c_{\psi}} \mu,$$
where the constant $c_{\psi}:=\log \left[\int_{X} e^{t \psi} d \mu\right]$ is chosen so that
$$1=\int_{X}\left(\omega+d d^{c} \varphi\right)^{n}=e^{-c_{\psi}} \int_{X} e^{t \psi} d \mu$$
Observe that $\mu_{\psi}:=e^{t \psi-c_{\psi}} \mu$ satisfies condition $\mathcal{H}\left(\alpha, A_{\psi}, \omega\right)$, where $A_{\psi}=$ $\exp \left(t \sup _{X} \psi-c_{\psi}\right)$. It follows therefore from Theorem 2.1 that there exists a unique continuous function $\varphi \in P S H(X, \omega)$ solution to $M A(\psi)$ and normalized by $\int_{X} \varphi d \mu=0$. We use here this linear normalization rather than
the non-linear sup-normalization: they are comparable thanks to proposition 2.7 in [GZ 1], which shows that
$$-M_{\mu} \leq \int_{X} u d \mu-\sup _{X} u \leq 0$$
for all functions $u \in P S H(X, \omega)$ and for some uniform constant $M_{\mu}>0$. Since $\int_{X} \psi d \mu=0$, we infer
$$0 \leq \mathcal{E}_{\omega}(\varphi):=\int_{X}|\varphi| \omega_{\varphi}^{n}=e^{-c_{\psi}} \int_{X}|\varphi| e^{t \psi} d \mu \leq 2 M_{\mu} e^{t M_{\mu}}$$
by observing that $c_{\psi} \geq 0$ since $t \geq 0$, and
$$\int_{X}|\varphi| d \mu \leq \int_{X}\left|\varphi-\sup _{X} \varphi\right| d \mu+\sup _{X} \varphi \leq 2 M_{\mu},$$
since $\int_{X} \varphi d \mu=0$.
The important fact here is that the energy $\mathcal{E}_{\omega}(\varphi)$ of $\varphi$ is bounded from above by a constant $M_{0}:=2 M_{\mu} e^{t M_{\mu}}$ which is independent of $\psi$. We have thus defined an operator
$$T: \psi \in \mathcal{C}_{M} \mapsto \varphi \in \mathcal{C}_{M_{0}}$$
which associates to $\psi \in \mathcal{C}_{M}$ the unique solution $\varphi \in \mathcal{C}_{M_{0}}$ to $M A(\psi)$, where
$$\mathcal{C}_{M}:=\left\{\psi \in \mathcal{E}^{1}(X, \omega) / \int_{X} \psi d \mu=0 \text { and } \mathcal{E}_{\omega}(\psi) \leq M\right\} .$$
It follows from proposition 3.2.3 in [GZ 2] that $\mathcal{E}^{1}(X, \omega)$ is convex. So is the subset of functions $\psi \in \mathcal{E}^{1}(X, \omega)$ such that $\int_{X} \psi d \mu=0$. The set $\mathcal{C}_{M}$ is not convex, but it is relatively compact in $L^{1}(X)$ and its closed convex hull $\hat{\mathcal{C}}_{M}$ is contained in $\mathcal{C}_{\kappa_{n} M}$ for some uniform constant $\kappa_{n}$ which only depends on the dimension of $X$ : this follows from easy computations (see lemma 7.2 and the proof of proposition 3.2 in [GZ 2]). Therefore $T$ maps the compact convex set $\hat{\mathcal{C}}_{M}$ into itself if $M$ is large enough.

We claim that $T$ is continuous. Let $\left(\psi_{j}\right) \in \mathcal{C}_{M}^{\mathbb{N}}$ be a sequence of functions which converges in $L^{1}(X)$ towards $\psi \in \mathcal{C}_{M}$. We need to show that $\varphi_{j}:=$ $T\left(\psi_{j}\right)$ converges in $L^{1}(X)$ towards $T(\psi)$. Since the set $\{u \in P S H(X, \omega) /$ $\left.\int_{X} u d \mu=0\right\}$ is relatively compact in $L^{1}(X)$ (see proposition 2.7 in [GZ 1]), we can assume - relabelling if necessary - that $\left(\varphi_{j}\right)$ converges in $L^{1}(X)$ towards a function $\varphi \in P S H(X, \omega)$. We show in lemma 4.2 below that $\left(\varphi_{j}\right)$ converges in $L^{1}(\mu)$ towards $\varphi$. In particular $\int_{X} \varphi d \mu=0$ and, passing to a subsequence if necessary, we can assume that $e^{t \psi_{j}(x)} \rightarrow e^{t \psi(x)}$ for $\mu$ almost every point $x$. Set
$$\hat{\varphi}_{j}:=\left(\sup _{l \geq j} \varphi_{l}\right)^{*} \quad \text { and } \quad \check{\psi}_{j}:=\inf _{l \geq j} \psi_{l} .$$
Observe that $\left(\hat{\varphi}_{j}\right)$ decreases towards $\varphi$, while $\left(e^{t \check{\psi}_{j}}\right)$ increases towards $e^{t \psi}$ at $\mu$ almost every point. The energy of $\hat{\varphi}_{j}$ is controlled by that of $\varphi_{j}$ since $\hat{\varphi}_{j} \geq \varphi_{j}$ (see lemma 7.2 in [GZ 2]), and $\mathcal{E}_{\omega}\left(\varphi_{j}\right) \leq M_{0}$ by (5), therefore
$\varphi \in \mathcal{E}^{1}(X, \omega)$ and $\left(\omega+d d^{c} \hat{\varphi}_{j}\right)^{n} \rightarrow\left(\omega+d d^{c} \varphi\right)^{n}$. It follows from an inequality of J.-P.Demailly [Dem 1] that
$$\left(\omega+d d^{c} \hat{\varphi}_{j}\right)^{n} \geq e^{t \check{\psi}_{j}-\hat{c}_{j}} \mu,$$
where $\hat{c}_{j}:=\sup _{l \geq j} c_{\psi_{l}}$. Observe that $\hat{c}_{j} \rightarrow c_{\psi}$, thus
$$\left(\omega+d d^{c} \varphi\right)^{n} \geq e^{t \psi-c_{\psi}} \mu .$$
Since these are two probability measures, there is actually equality hence $\varphi=T(\psi)$ : this shows that $T$ is continuous.

We can now invoke Schauder fixed point theorem, which yields a fixed point $\varphi=T(\varphi), \varphi \in \mathcal{C}_{M}$. The function $\varphi$ is automatically continuous (by Theorem 2.1, since $e^{t \varphi-c_{\varphi}} \mu$ satisfies $\left.\mathcal{H}\left(\alpha, A^{\prime}, \omega\right)\right)$, hence $\Phi:=\varphi-t^{-1} c_{\varphi}$ is the solution we were looking for. \(\square\)

Lemma 4.2. The functions $\varphi_{j}=T\left(\psi_{j}\right)$ (respectively $e^{t \psi_{j}}$ ) converge in $L^{1}(\mu)$ towards $\varphi$ (respectively $e^{t \psi}$ ).

Proof. We first show that $\left(\varphi_{j}\right)$ converges to $\varphi$ in $L^{1}(\mu)$. Observe that the sequence $\left(\varphi_{j}\right)$ is uniformly bounded: this follows from Theorem 2.1 since $\left(\omega+d d^{c} \varphi_{j}\right)^{n}$ satisfies $\mathcal{H}\left(\alpha, A_{j}, \omega\right)$, where $A_{j}=e^{t \sup _{X} \psi_{j}-c_{\psi_{j}}} A \leq e^{t M_{\mu}} A$ is bounded from above. It follows then from standard arguments that $\int_{X} \varphi_{j} d \mu \rightarrow \int_{X} \varphi d \mu$ (see e.g. the proof of lemma 5.2 in [Ce]).

Fix $\varepsilon>0$ and let $G$ be an open set of $X$ such that $\varphi$ is continuous on $X \backslash G$ and $\operatorname{Cap}_{\omega}(G) \leq \varepsilon$ (see corollary 3.8 in [GZ 1]). By Hartogs' lemma, $\varphi_{j} \leq \varphi+\varepsilon$ on the compact set $X \backslash G$, if $j \geq j_{\varepsilon}$. Observe that
$$\int_{X \backslash G}\left|\varphi-\varphi_{j}\right| d \mu \leq 2 \varepsilon+\int_{X \backslash G}\left[\varphi-\varphi_{j}\right] d \mu \leq 3 \varepsilon,$$
if $j \geq j_{\varepsilon}^{\prime}$. O the other hand since $\mu$ satisfies $\mathcal{H}(\alpha, A, \omega)$, we get
$$\int_{G}\left|\varphi-\varphi_{j}\right| d \mu \leq 2 M \mu(G) \leq 2 M A \varepsilon^{1+\alpha}$$
where $M=\sup _{j}\left\|\varphi_{j}\right\|_{L^{\infty}(X)}$. This shows that $\left\|\varphi-\varphi_{j}\right\|_{L^{1}(\mu)} \rightarrow 0$.
The proof for $\left(e^{t \psi_{j}}\right)$ is similar: it suffices to note that the functions $u_{j}:=$ $e^{t \psi_{j}-t \sup _{X} \psi_{j}}$ are $\omega$-psh and uniformly bounded. One can then apply the rest of the argument. \(\square\)

Proposition 4.3. Let $\varphi, \psi \in \mathcal{E}^{1}(X, \omega)$ and $t>0$ be such that
$$\left(\omega+d d^{c} \varphi\right)^{n} e^{-t \varphi}=\left(\omega+d d^{c} \psi\right)^{n} e^{-t \psi} .$$
Then $\varphi \equiv \psi$.
Proof. It follows from the comparison principle (see [GZ 2]) that
$$\int_{(\varphi<\psi)}\left(\omega+d d^{c} \psi\right)^{n} \leq \int_{(\varphi<\psi)}\left(\omega+d d^{c} \varphi\right)^{n}=\int_{(\varphi<\psi)} e^{t(\varphi-\psi)}\left(\omega+d d^{c} \psi\right)^{n} .$$
Since $e^{t(\varphi-\psi)}<1$ on $(\varphi<\psi)$, we infer $\varphi \geq \psi$ for $\nu$ almost every point, where $\nu=\left(\omega+d d^{c} \psi\right)^{n}$. Reversing the roles of $\varphi, \psi$ yields $\varphi=\psi$ for $\nu$ almost every point. Therefore $\left(\omega+d d^{c} \varphi\right)^{n}=\left(\omega+d d^{c} \psi\right)^{n}$, hence $\varphi-\psi=c$ is constant by Theorem 3.4 in [GZ 2]. Finally $c=0$ since $e^{t c}=1$ and $t>0$. \(\square\)

When $K_{X}$ is nef and big, H.Tsuji constructed in [Ts] - using Kähler-Ricci flow techniques - a function $\psi \in P S H(X, \omega)$ such that
$$\int_{X} e^{t \psi} d \mu=1, \psi \in \mathcal{C}^{\infty}(X \backslash E) \text { and }\left(\omega+d d^{c} \psi\right)^{n}=e^{t \psi} \mu \text { in } X \backslash E,$$
where $E$ is some exceptional divisor, $\psi$ is smooth outside the exceptionnal divisor of map associated to the base point free linear sustem $\left|N K_{X}\right|, N \in \mathbb{N}$ big enough and the current $T_{K E}=\omega+d d^{c} \psi$ defines a Kähler-Einstein metric. This function coincides with our solution thanks to the following unicity result.

Proposition 4.4. Let $\mu$ be a probability measure and $t>0$. Let $\varphi, \psi \in$ $\operatorname{PSH}(X, \omega)$ be such that $\int_{X} e^{t \varphi} d \mu=\int_{X} e^{t \psi} d \mu=1$. Assume $\varphi \in \mathcal{E}^{1}(X, \omega)$ is a global solution to the complex Monge-Ampère equation $\left(\omega+d d^{c} \varphi\right)^{n}=e^{t \varphi} \mu$, while $\psi \in \mathcal{C}^{0}(X \backslash E)$ satisfies $\left(\omega+d d^{c} \psi\right)^{n}=e^{t \psi} \mu$ only in $X \backslash E$.