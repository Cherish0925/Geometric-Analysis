---
retention_scope: session
part: 1
total_parts: 3
---

[Part 1/3 of: [1304.2087] Kähler-Einstein metrics on stable varieties and ...]

---
source_file: 1304_2087.pdf
converter: mathpix
format: mmd
---

\title{
KÄHLER-EINSTEIN METRICS ON STABLE VARIETIES AND LOG CANONICAL PAIRS
}
by

\author{
Robert J. Berman \& Henri Guenancia
}

\section*{Contents}
Introduction ..... 1
1. Preliminaries ..... 7
2. Singular Kähler-Einstein metrics ..... 12
3. Variational solutions ..... 18
4. Smoothness of the Kähler-Einstein metric ..... 25
5. Applications ..... 38
6. Outlook ..... 40
References ..... 42

\section*{Introduction}

According to the seminal works of Aubin [Aub78] and Yau [Yau78] any canonically polarized compact complex manifold $X$ (i.e. $X$ is a non-singular projective algebraic variety such that the canonical line bundle $K_{X}$ is ample) admits a unique Kähler-Einstein metric $\omega$ in the first Chern class $c_{1}\left(K_{X}\right)$. One of the main goals of the present paper is to extend this result to the case when $X$ is singular or more precisely when $X$ has semi-log canonical singularities. A major motivation comes from the fact that such singular varieties are used to compactify the moduli space of canonically polarized manifolds - a subject where there has been great progress in the last years in connection to the (log) Minimal Model Program (MMP) in birational algebraic geometry [Kol, Kov13]. The varieties in question are usually refered to as stable varieties (or canonical models) as they are the higher dimensional generalization of the classical notion of stable curves of genus $g>1$, which form the Deligne-Mumford compactification of the moduli space of non-singular genus $g$ curves [Kol, Kov13]. It as a classical fact that any stable curve admits a unique Kähler-Einstein metric on its regular part, whose total area is equal to the (arithmetic) degree of the curve
$X$ (see the section on stable curves further in the introduction for more details). Our first (and main) result gives a generalization of this fact to the higher dimensional setting:

Theorem A. - Let $X$ be a projective complex algebraic variety with semi-log canonical singularities such that $K_{X}$ is ample. Then there exists a Kähler metric $\omega$ on the regular locus $X_{\text {reg }}$, satisfying
$$\operatorname{Ric} \omega=-\omega$$
and such that the volume of $\left(X_{\text {reg }}, \omega\right)$ coincides with the volume of $K_{X}$, i.e. $\int_{X_{\text {reg }}} \omega^{n}=$ $c_{1}\left(K_{X}\right)^{n}$. Moreover, the metric extends to define a current $\omega$ in $c_{1}\left(K_{X}\right)$ which is uniquely determined by $X$.

We will refer to the current $\omega$ in the previous theorem as a (singular) Kähler-Einstein metric on $X$. Moreover, the current $\omega$ will be shown to be of finite energy, in the sense of [GZ07, BBGZ13] and as discussed in the last section of the present paper this allows one to define a canonical (singular) Weil-Peterson metric on the compact moduli space in terms of Deligne pairings. The notion of semi-log canonical singularities of a variety $X$ - which is the most general class of singularities appearing in the (log) Minimal Model Program will be recalled below. For the moment let us just point out that the definition involves two ingredients: first a condition which makes sure that the canonical divisor $K_{X}$ is defined as a $\mathbb{Q}$ - Cartier divisor (i.e. $\mathbb{Q}$-line bundle) which is in particular needed to make so sense of the notion of ampleness of $K_{X}$ and secondly, the definition of semi-log canonical singularities involves a bound on the discrepancies of $X$ on any resolution of singularities.

In fact, we will conversely show that if $K_{X}$ is ample and the variety $X$ admits a KählerEinstein metric then $X$ has semi-log canonical singularities and this brings us to our second motivation for studying Kähler-Einstein metrics in the the singular setting, namely the Yau-Tian-Donaldson conjecture. Recall that this conjecture concerns polarized algebraic manifolds $(X, L)$, i.e. algebraic manifolds together with an ample line bundle $L \rightarrow X$ and it says that the first Chern class $c_{1}(L)$ of $L$ contains a Kähler metric $\omega$ with constant scalar curvature if and only if $(X, L)$ is $K$-stable. The latter notion of stability is of an algebrogeometric nature and can be seen as an asymptotic form of the classical notions of Chow and Hilbert stability appearing in Geometric Invariant Theory (GIT). However, while the notion of $K$-stability makes equal sense when $X$ is singular it is less clear how to give a proper definition of a constant scalar curvature metric for a singular polarized variety $(X, L)$. But, as it turns out, the situation becomes more transparent in the case when $L$ is equal to $K_{X}$ or its dual, the anti-canonical bundle $-K_{X}$. The starting point is the basic fact that, when $X$ is smooth, a Kähler metric in $\omega$ in $c_{1}\left( \pm K_{X}\right)$ has constant scalar curvature on all of $X$ precisely when it has constant Ricci curvature, i.e. when $\omega$ is a Kähler-Einstein metric. Various generalizations of Kähler-Einstein metrics to the singular setting have been proposed in the litterature, see e.g. $\left[\mathbf{E G Z 0 9}, \mathbf{B E G Z 1 0}, \mathbf{B B E}^{+} \mathbf{1 1}\right]$ etc. In this paper we will adopt the definition which appears in the formulation of the previous theorem (see also section 2), i.e. a positive current in $c_{1}\left( \pm K_{X}\right)$ is said to define a (singular) Kähler-Einstein metric if
defines a bona fide Kähler-Einstein metric on the regular locus $X_{\text {reg }}$ and if its total volume there coincides with the algebraic top intersection number of $c_{1}\left( \pm K_{X}\right)$. This definition, first used in the Fano case in $\left[\mathbf{B B E}^{+} \mathbf{1 1}\right]$, has the virtue of generalizing all previously proposed definitions, regardless of the sign of the canonical line bundle. Combing our results with recent results of Odaka [Oda13, Oda12], which say that a canonicaly polarized variety has semi-log canonical singularities precisely when $\left(X, K_{X}\right)$ is $K$-stable, gives the following theorem, which can be seen as a confirmation of the generalized form of the Yau-Tian-Donaldson conjecture for canonically polarized varieties (satisfying the conditions $G_{1}$ and $S_{2}$, cf 2.10 for a more precise statement):

Theorem B. - Let $X$ be a complex projective variety such that $K_{X}$ is ample. Then $X$ admits a Kähler-Einstein metric if and only if $\left(X, K_{X}\right)$ is $K$-stable.

It may also be illuminating to compare this result with the case when $L:=-K_{X}$ is ample (i.e. $X$ is Fano). Then it was shown in [Ber16], in the general singular setting, that the existence of a Kähler-Einstein metrics indeed implies $K$-(poly)stability. As for the converse it was finally settled very recently in the deep works by Chen-Donaldson-Sun [CDS15a, CDS15b, CDS15c] and Tian [Tia15], independently, in the case when $X$ is smooth. The existence problem in the singular case is still open in general, except for the toric case [BB13]; cf also [OSS16] for a related problem in the case of singular Fano surfaces.

Coming back to the present setting we point out that the starting point of our approach is that, after passing to a suitable resolution of singularities, we may as well assume that the variety $X$ is smooth if we work in the setting of log pairs $(X, D)$, where $D$ is a $\mathbb{Q}$-divisor on $X$ with simple normal crossings (SNC) and where the role of the canonical line bundle is played by the log canonical line bundle $K_{X}+D$ (which appears as the pull-back to the resolution of the original canonical line bundle). In this notation the original variety has semi-log canonical singularities precisely when the log pair $(X, D)$ is log canonical (lc) in the usual sense of the Minimal Model Program, i.e. the coefficents of $D$ are at most equal to one (but negative coefficents are allowed). However, it should be stressed that for this gain in regularity we have, of course, to pay a loss of positivity: even if the original canonical line bundle is ample, the corresponding log canonical line bundle is only semi-ample (and big) on the resolution, since it is trivial along the exceptional divisors of the corresponding resolution.

The upshot is that the natural setting for our results is the setting of log smooth log canonical pairs $(X, D)$ such that the log canonical line bundle $K_{X}+D$ is semi-ample and big. To any such pair we will associate a canonical Kähler-Einstein metric $\omega$ in the sense that $\omega$ is a current in the first Chern class $c_{1}\left(K_{X}+D\right)$ such that $\omega$ restricts to a bona fide Kähler-Einstein metric on a Zariski open set of $X$ and such that, globally on $X$, the current defined by the divisor $D$ gives a singular contribution to the Ricci curvature of $\omega$.

Theorem C. - Let $X$ be a Kähler manifold and $D$ a simple normal crossings $\mathbb{R}$-divisor on $X$ with coefficients in $]-\infty, 1]$ such that $K_{X}+D$ is semi-positive and big $\left(\right.$ i.e. $\left(K_{X}+D\right)^{n}>$ 0 ). Then there exists a unique current $\omega$ in $c_{1}\left(K_{X}+D\right)$ which is smooth on a Zariski open set $U$ of $X$ and such that
$$\operatorname{Ric} \omega=-\omega+[D]$$
holds on $X$ in the weak sense and $\int_{U} \omega^{n}=\left(K_{X}+D\right)^{n}$. More precisely, $U$ can be taken to be the complement of $D$ in the ample locus of $K_{X}+D$. Moreover, any such current $\omega$ on $X$ automatically has finite energy.

Recall that the ample locus of a big line bundle $L$ may be defined as the Zariski open set whose complement is the augmented base locus of $L$, i.e. the intersection of all effective $\mathbb{Q}$-divisors $E$ such that $L-E$ is ample. In particular, if $Y$ is a variety with semi-log canonical singularities and $\pi:(X, D) \rightarrow Y$ is a log resolution of the normalization (endowed with its conductor), then the exceptional locus of $\pi$ is contained in the augmented base locus of $K_{X}+D$ and hence Theorem C above indeed implies Theorem A.

The existence proof of Theorem C (and its generalizations described below) will be divided into two parts: in the first part we construct a variational solution with finite energy, by adapting the variational techniques developed in [BBGZ13] to the present setting. Then, in the second part, we show that the variational solutions have appropriate regularity using a priori Laplacian estimates, building on the works of Aubin [Aub78] and Yau [Yau78] and ramifications of their work by Kobayashi [Kob84] and Tian-Yau [TY87] to the setting of quasi-projective varieties - in particular we will be relying on Yau's maximum principle. For the second part we will need to perturb the line bundle $L:=K_{X}+D$ (to make it ample) and regularize the klt part of the divisor $D$ (to make the divisor purely log canonical).

It is interesting to note that, so far, we are not able of proving Theorem C without using the variational method, i.e. relying only on a priori estimates. The reason is that our estimates on the potential of the solution near $\operatorname{Supp}(D)$ are not good enough to extend it directly as a current with full Monge-Ampère mass, so as to get the Kähler-Einstein metric of $(X, D)$.

Let us also point out that the variational part of our proof only requires $K_{X}+D$ to be big and thus produces a unique singular Kähler-Einstein metric of finite energy on any variety of log general type. As for the regularity part it applies as long as the corresponding log canonical ring is finitely generated. In fact, according to one of the fundamental conjectures of the general log minimal model program the latter finiteness property always holds. Note that for log canonical pairs, the finite generation is known to hold for $n \leqslant 4$, cf $\left[\mathbf{K}^{+} \mathbf{9 2}\right.$, Fuj10 $]$ and the references therein. We also recall that in the case of varieties of log general type with log terminal singularities (which in our notation means that $D_{l c}$ vanishes) the finite generation in question was established in the seminal work [BCHM10] and Kähler-Einstein metrics were first constructed in [EGZ09].

In the last section of the paper some applications of Theorem A are given. First, we explain the link with Yau-Tian-Donaldson as we indicated above in Theorem B. Then, we give a short analytic proof of the fact that the automorphism group of a stable variety is finite (see [BHPS13] for algebro-geometric proofs). We also discuss the problem of deducing Miyaoka-Yau type inequalities from Theorem A.

\section*{Further comparison with previous results. -}

Stable curves. - A stable curve, as defined by [DM69], is a reduced one equidimensional projective scheme over $\mathbb{C}$ with only nodes as singularities and with finite automorphism group. The latter finiteness assumption can be replaced with various equivalent conditions, for example that the canonical sheaf of $X$ is ample or in differential geometric terms: every connected component of $X_{\text {reg }}=X \backslash\{$ nodes $\}$ is covered by the disk. In turn, this is equivalent to asking that every connected component of $X_{\text {reg }}$ admits a complete hyperbolic metric.

As above, the higher dimensional analogue of Deligne-Mumford stable curves are the socalled stable varieties which are reduced equidimensional complex projective schemes with semi-log canonical singularities (i.e. double normal crossing singularities in codimension one, and log canonical singularities in higher codimension) and ample canonical bundle. In the light of the discussion above one could be tempted to believe that the regular locus of a stable variety can always be endowed with a complete Kähler-Einstein metric. However, this is not the case, mainly because of the singularities in codimension $\geqslant 2$ (the relationship between the completeness of the metric and the singularities of the variety will be analyzed in [GW14]). Indeed, our main result says that if we are given a scheme $X$ (reduced, equidimensional, complex and projective) whose only singularities in codimension one are double normal crossings and such that $K_{X}$ is ample, then $X$ has semi-log canonical singularities (i.e. $X$ is stable) if and only if $X_{\text {reg }}$ admits a Kähler-Einstein metric $\omega$ with negative curvature such that $\operatorname{Vol}_{\omega}\left(X_{\text {reg }}\right)=c_{1}\left(K_{X}\right)^{n}$. This volume condition replaces in higher dimension the completeness condition, which does not hold in general. Further, this condition was known for a long time to be equivalent to the other ones in the one dimensional case already, see e.g. [HK14, §1].

Quasi-projective varieties. - Theorem C also extends some of the results of Wu in [Wu08, Wu09], concerning the setting of Kähler-Einstein metrics on quasi-projective projective varieties of the form $X_{0}:=X-D$, where $X$ is smooth and $D$ is reduced SNC divisor. We recall that the case when $K_{X}+D$ is ample was independently settled by Kobayashi [Kob84] and Tian-Yau [TY87]. The case when $X$ is an orbifold and $K_{X}+D$ is semiample and big was considered by Tian-Yau in [TY87] and as later shown by Yau [Yau93] the corresponding Kähler-Einstein metric is then complete on $X_{0}$. (in the orbifold sense). However, in our general setting the metric will typically not be complete on the regular locus. This is only partly due to the klt singularities (which generalize orbifold singularities) - there is also a complication coming from the presence of negative coefficents on a resolution.

To illustrate this we recall that a standard example of log canonical pairs $(X, D)$ is given by the Borel-Baily compactification $X:=X_{0}-D$ of an arithmetic quotient, i.e. $X_{0}=B / \Gamma$, where $B$ is a bounded symmetric domain and $\Gamma$ is discrete subgroup of the automorphism group of $B$. In this case any toroidal resolution $X^{\prime}$ has the property that the corresponding divisor $D^{\prime}$ on the resolution is reduced (and hence purely log canonical) if $\Gamma$ is neat, i.e. if there are no fixed points. The corresponding Kähler-Einstein metric on $X_{0}$ is the complete one induced from the corresponding metric on $B$, constructed in [CY80, MY83]. When $\Gamma$ has fixed points these give rise to an additional fractional klt part $D_{k l t}^{\prime}$ in $D^{\prime}$ so that the corresponding Kähler-Einstein metric is only complete in the orbifold sense [TY87]. However, for general log canonical singularity $(X, D)$ the klt part $D_{k l t}^{\prime}$ of $D^{\prime}$ may not be fractional or more seriously: it may contain negative coefficients and the main novelty of the present paper is to show how to deal with this problem by combining a variational approach with a priori estimates.

Behaviour at the boundary. - It is also interesting to compare with the case when the pair $(X, D)$ is log smooth with $K_{X}+D$ ample and with $D$ effective and klt (i.e. with coefficients in [ $0,1[$ ), where very precise regularity results have been obtained recently. For example, in [Bre13, CGP13, JMR16, GP16] it is shown that the corresponding Kähler-Einstein metric $\omega$ has conical singularities along $D$ (sometimes also called edge singularities in the litterature), thus confirming a previous conjecture of Tian. As for the mixed case when the coefficient 1 is also allowed in $D$ it was studied in [Gue14, GP16], where it was shown that $\omega$ has mixed cone and Poincaré type singularities. A commun theme in these results is that singularities of the metric $\omega$ are encoded by a suitable local model (with cone or Poincaré type singularities) determined by $D$. However, the difficulty in the situation studied in the present paper is the presence of negative coefficients in $D$ and the associated loss of positivity which appears when we pass to a log resolution of a singular variety $X$. It would be very interesting if one could associate local models to this situation as well, but this seems very challenging even in the case when $X$ has canonical singularities.

We should mention that the behaviour of the Kähler-Einstein metric of a log canonical pair $(X, D)$ such that $K_{X}+D$ is ample and $D$ is effective will be investigated in [GW14]. As a consequence of the results therein, the Kähler-Einstein metric of a stable variety is equivalent to the cusp metric near the ordinary double points.

Organization of the paper. -
\begin{itemize}
\item[-] §1: We introduce the preliminary material that we will need, concerning the pluripotential theoretic setting of singular metrics on line bundles over varieties which are not necessarily normal.
\item[-] §2: Here we give the definition of a Kähler-Einstein metric on a canonically polarized variety $X$ and more generally on a log pair $(X, D)$. As we explain a purely differentialgeometric definition can be given which only involves the regular locus $X_{\text {reg }}$ of $X$. But, at we show, the corresponding metric automatically extends in a unique manner to define a singular current on $X$ (which will allow us to prove the uniqueness of the
\end{itemize}

Kähler-Einstein metric, later on in section 3). We first treat the case when $X$ has log canonical (and hence normal singularities) and then the general case of a variety $X$ with semi-log singularities. Anyway, as we recall, the latter case reduces to the former (if one works in the setting of pairs) if one passes to the normalization.
\begin{itemize}
\item[-] §3: We prove the uniqueness and existence of a weak Kähler-Einstein metric in the general setting of varieties of log general type. The existence is proved by adapting the variational approach to complex Monge-Ampère equations introduced in [BBGZ13] to the present setting. This method produces a singular Kähler-Einstein metric with finite energy (the new feature here compared to [BBGZ13] is that the reference measure does not have an $L^{1}$ density). We also use the variational approach to establish a stability result for the solutions to the equations induced from an (ample) perturbation of the log canonical line bundle on a resolution.
\item[-] §4: Here we establish the smoothness of the Kähler-Einstein metric, produced by the variational approach, on the regular locus of the variety $X$ (or more generally, the pair $(X, D)$ ). The proof uses a perturbation argument in order to reduce the problem the the original setting of Kobayashi and Tian-Yau, combined with a priori estimates. But it should be stressed that in order to control the $\mathscr{C}^{0}$ norms we need to invoke the variational stability result proved in the previous section.
\item[-] §5: We give some applications to automorphism groups and show how to deduce the Yau-Tian-Donaldson conjecture for canonically polarized varieties from our results.
\item[-] §6: The paper is concluded with a brief outlook on possible applications to Miyaoka-Yau types inequalities, as well as the Weil-Peterson geometry of the moduli space of stable varieties. These applications will require a more detailed regularity analysis of the Kähler-Einstein metrics that we leave for the future.
\end{itemize}

\section*{1. Preliminaries}

We collect here some useful tools or notions that we are going to work with in this paper. We start with a compact Kähler manifold $X$ of dimension $n$, and we consider a class $\alpha \in H^{1,1}(X, \mathbb{R})$ which is big. By definition, this means that $\alpha$ lies in the interior of the pseudo-effective cone, so that there exists a Kähler current $T \in \alpha$, that is a current which dominates some smooth positive form $\omega$ on $X$. We fix $\theta$, a smooth representative of $\alpha$.

The ample locus. - An important invariant attached to $\alpha$ is the ample locus of $\alpha$, denoted $\operatorname{Amp}(\alpha)$, and introduced in [Bou04, §3.5]. This is the largest Zariski open subset $U$ of $X$ such that for all $x \in U$, there exists a Kähler current $T_{x} \in \alpha$ with analytic singularities such that $T_{x}$ is smooth in an (analytic) neighbourhood of $x$. Its complement, called the augmented base locus, is usually denoted by $\mathbb{B}_{+}(\alpha)$. In the case when $\alpha=c_{1}(L)$ is the

Chern class of a line bundle, it is known (see e.g. [BBP13]) that:
$$\mathbb{B}_{+}(L)=\bigcap_{\substack{L=A+E \\ A \text { ample, } E \geqslant 0}} \operatorname{Supp}(E)$$
Currents with minimal singularities. - We will be very brief about this well-known notion, and refer e.g. to [Bou04, §2.8], [BBGZ13, §1], [Ber09] or [BD12] for more details and recent results.
By definition, if $T, T^{\prime}$ are two positive closed currents in the same cohomology class $\alpha$, we say that $T$ is less singular than $T^{\prime}$ if the local potentials $\varphi, \varphi^{\prime}$ of these currents satisfy $\varphi^{\prime} \leqslant \varphi+O(1)$. It is clear that this definition does not depend on the choice of the local potentials, so that the definition is consistant. In each (pseudo-effective) cohomology class $\alpha$, one can find a positive closed current $T_{\text {min }}$ which will be less singular than all the other ones; this current is not unique in general; only its class of singularities is. Such a current will be called current with minimal singularities.

One way to find such a current is to pick $\theta \in \alpha$ a smooth representative, and define then, following Demailly, the upper envelope
$$V_{\theta}:=\sup \{\varphi \theta-\mathrm{psh}, \varphi \leqslant 0 \text { on } X\}$$
Once observed that $V_{\theta}$ is $\theta$-psh (in particular upper semi-continuous), it becomes clear that $\theta+d d^{c} V_{\theta}$ has minimal singularities.

Non-pluripolar Monge-Ampère operator. - In the paper [BEGZ10], the authors define the non-pluripolar product $T \mapsto\left\langle T^{n}\right\rangle$ of any closed positive (1, 1)-current $T \in \alpha$, which is shown to be a well-defined measure on $X$ putting no mass on pluripolar sets, and extending the usual Monge-Ampère operator for Kähler forms (or having merely bounded potentials, cf [BT87]). Let us note that when $T$ is a smooth positive form $\omega$ on a Zariski dense open subset $\Omega \subset X$, then its Monge-Ampère $\left\langle T^{n}\right\rangle$ is simply the extension by 0 of the measure $\omega^{n}$ defined on $\Omega$.

Given now a $\theta$-psh function $\varphi$, one defines its non-pluripolar Monge-Ampère by $\operatorname{MA}(\varphi):=$ $\left\langle\left(\theta+d d^{c} \varphi\right)^{n}\right\rangle$. Then one can check easily from the construction that the total mass of MA( $\varphi$ ) is less than or equal to the volume $\operatorname{vol}(\alpha)$ of the class $\alpha$ (cf [Bou02]):
$$\int_{X} \operatorname{MA}(\varphi) \leqslant \operatorname{vol}(\alpha)$$

A particular class of $\theta$-psh functions that appears naturally is the one for which the last inequality is an equality. We will say that such functions (or the associated currents) have full Monge-Ampère mass. For example, $\theta$-psh functions with minimal singularities have full Monge-Ampère mass (cf [BEGZ10, Theorem 1.16]).

Plurisubharmonic functions on complex spaces. - Here again, we just intend to give a short overview of the extension of the pluripotential theory to (reduced) complex Kähler spaces. A very good reference is [Dem85], or [EGZ09, §5] which is written in relation to singular Kähler-Einstein metric. We also refer to the preliminary parts of [Var89] or [FS90].

The data of a reduced complex space $X$ includes the data of the sheaves of continuous and holomorphic functions. So the first object we would like to give a sense to is the sheaf $\mathscr{C}_{X}^{\infty}$ of smooth functions. It may be defined as the restriction of smooth functions in some local embeddings of $X$ in some $\mathbb{C}^{n}$. One defines similarly the sheaves of smooth $(p, q)$-forms $\mathscr{A}_{X}^{p, q}$ which carry the differentials $d, \partial, \bar{\partial}$ satisfying the usual rules; the space of currents is by definition the dual of the space of differential forms as in the smooth case. The sheaves complexes that are induced (Dolbeault, de Rham, etc.) are however not exact in general.

Another important sheaf is the one of pluriharmonic functions. They are defined to be smooth functions locally equal to the imaginary part of some holomorphic functions. One can show (see e.g [FS90]) that a continuous function which is pluriharmonic on $X_{\text {reg }}$ in the usual sense is automatically pluriharmonic on $X$. We denote by $\mathcal{P} \mathcal{H}_{X}$ the sheaf of real-valued pluriharmonic functions on $X$.

Let us move on to psh functions now. There are actually two possible definitions which extend the usual one for complex manifolds. The first one, introduced by Grauert and Remmert, mimics the one in the smooth case: we will say that a function $\varphi: X \rightarrow \mathbb{R} \cup\{-\infty\}$ is plurisubharmonic if it is upper semi-continuous and if for all holomorphic map $f: \Delta \rightarrow X$ from the unit disc in $\mathbb{C}$, the function $\varphi \circ f$ is subharmonic.

We could also introduce a more local definition: a function $\varphi: X \rightarrow \mathbb{R} \cup\{-\infty\}$ is strongly plurisubharmonic if in any local embeddings $i_{\alpha}: X \supset U_{\alpha} \hookrightarrow \mathbb{C}^{n}, \varphi$ is the restriction of a psh function defined an open set $\Omega_{i} \subset \mathbb{C}^{n}$ containing $i_{\alpha}\left(U_{\alpha}\right)$, if $X=\cup_{\alpha} U_{\alpha}$ is an open covering.

Clearly, a strongly psh function is also psh. Actually, Fornaess and Narasimhan [FN80] showed that these notions coincide: a function on $X$ is psh if and only if it is strongly psh. On normal spaces one still has a Riemann extension theorem for psh functions, thanks to [GR56]. More precisely, if $X$ is normal, $Y \subsetneq X$ is any proper analytic subspace, and $\varphi: X \backslash Y \rightarrow \mathbb{R} \cup\{-\infty\}$ is psh, then $\varphi$ extends to a (unique) psh function on $X$ if and only if it is locally bounded above near the points of $Y$, condition which is always realized if $Y$ has codimension at least two in $X$. In particular, if $X$ is normal, the data of a psh function on $X$ is equivalent to the data of a psh function on $X_{\text {reg }}$.

Moreover, one can show (cf [BEG13, Lemma 3.6.1]) that a pluriharmonic function on $X_{\text {reg }}$ automatically extends to a pluriharmonic function on $X$.

On non-normal spaces, one has to be more cautious, and it is convenient to introduce the notion of weakly psh function. Let $X$ be a reduced complex space, and $\nu: X^{\nu} \rightarrow X$ its normalization. We say that a function $\varphi: X \rightarrow \mathbb{R} \cup\{-\infty\}$ is weakly psh if $\nu^{*} \varphi=\varphi \circ \nu$ is psh. It is not hard to see that a weakly psh function $\varphi$ induces a bona fide psh function on $X_{\text {reg }}$ which is locally bounded from above near the points of $X_{\text {sing }}$. Conversely, any psh
function on $X_{\text {reg }}$ which is locally upper bounded extends to a weakly psh function on $X$. On a normal space, a weakly psh function is of course psh, but in general these notions are different: consider $X=\{z w=0\} \subset \mathbb{C}^{2}$, and $\varphi(x)=0$ or 1 according to the connected component of $x \in X$. We refer to [Dem85, Théorème 1.10] for equivalent characterizations of weakly psh functions and conditions on a weakly psh function that ensure that it is already psh.

Finally, one can check that a (strongly) psh function $\varphi$ on a complex space $X$ is always locally integrable with respect to the area measure induced by any local embedding of $X$ in $\mathbb{C}^{n}$ (note that this is stronger than saying that $\varphi$ is locally integrable on $X_{\text {reg }}$ with respect to some volume form). Moreover, a locally integrable function $\varphi$ is (almost everywhere) weakly psh is and only if it is locally bounded from above and $d d^{c} \varphi$ is a positive current.

Weights and Chern classes. - From now on, $X$ will be a normal complex space unless stated otherwise.

The definition of a (smooth) Kähler form is rather natural: it is a smooth real (1, 1)-form written locally as $d d^{c} \psi$ for some (smooth) strictly psh function $\psi$; equivalently this is locally the restriction of a Kähler form in a embedding in $\mathbb{C}^{n}$. Note that we could interpret this definition in terms of hermitian metrics on the Zariski tangent bundle of $X$, cf [Var89].

Let us now consider a line bundle $L$ on $X$. A smooth hermitian metric $h$ on $L$ is defined as in the smooth case: using trivialisations $\tau_{\alpha}: L_{\mid U_{\alpha}} \xrightarrow{\simeq} U_{\alpha} \times \mathbb{C}$, we just ask $h$ to be written as $h(v)=\left|\tau_{\alpha}(v)\right|^{2} e^{-\varphi_{\alpha}(z)}$ where $\varphi_{\alpha}$ is a smooth function on $U_{\alpha}$. We say that the data $\phi:=\left\{\left(U_{\alpha}, \varphi_{\alpha}\right)\right\}$ is a weight on $L$, so that it is equivalent to consider a weight or an hermitian metric.

Observe that if $\left(g_{\alpha \beta}: U_{\alpha} \cap U_{\beta} \rightarrow \mathbb{C}^{*}\right)$ is the cocycle in $H^{1}\left(X, \mathcal{O}_{X}^{*}\right)$ determined by the $\tau_{\alpha}$ 's (more precisely $\tau_{\alpha} \circ \tau_{\beta}^{-1}(z, v)=\left(z, g_{\alpha \beta} v\right)$ ), then we have necessarily $\varphi_{\beta}-\varphi_{\alpha}=\log \left|g_{\alpha \beta}\right|^{2}$. In particular, the forms $d d^{c} \varphi_{\alpha}$ glue to a global smooth (1, 1)-form on $X$ called curvature of $(L, h)$ and denoted by $c_{1}(L, h)$. This forms lives naturally in the space $H^{0}\left(X, \mathscr{C}_{X}^{\infty} / \mathcal{P} \mathcal{H}_{X}\right)$, and using the exact sequence
$$0 \longrightarrow \mathcal{P} \mathcal{H}_{X} \longrightarrow \mathscr{C}_{X}^{\infty} \longrightarrow C_{X}^{\infty} / \mathcal{P} \mathcal{H}_{X} \longrightarrow 0$$
one may attach to $(L, h)$ a class $\hat{c}_{1}(L, h) \in H^{1}\left(X, \mathcal{P} \mathcal{H}_{X}\right)$. It is then easy to see that this class actually does not depend on the choice of $h$, so we will denote it by $\hat{c}_{1}(L)$. If $X$ is smooth, $H^{1}\left(X, \mathcal{P} \mathcal{H}_{X}\right) \simeq H^{1,1}(X, \mathbb{R})$, and it is well-known that $\hat{c}_{1}(L)$ coincides with the image of $L \in H^{1}\left(X, \mathcal{O}_{X}^{*}\right)$ in $H^{2}(X, \mathbb{Z})$ via the connecting morphism induced by the exponential exact sequence
$$0 \longrightarrow \mathbb{Z} \longrightarrow \mathcal{O}_{X} \xrightarrow{e^{2 i \pi}} \mathcal{O}_{X}^{*} \longrightarrow 0$$
This sequence also exists on any (even non-reduced) complex space, so that $c_{1}(L) \in H^{2}(X, \mathbb{Z})$ is well-defined; it will be more convenient for us to look at the image of $c_{1}(L)$ in $H^{2}(X, \mathbb{R})$ however. To relate it to $\hat{c}_{1}(L)$, we may use the following exact sequence:
$$0 \longrightarrow \mathbb{R} \longrightarrow \mathcal{O}_{X} \xrightarrow{-2 \operatorname{Im}(\cdot)} \mathcal{P} \mathcal{H}_{X} \longrightarrow 0$$

It is not hard to check that the connecting morphism $H^{1}\left(X, \mathcal{P} \mathcal{H}_{X}\right) \rightarrow H^{2}(X, \mathbb{R})$ sends $\hat{c}_{1}(L)$ to $c_{1}(L)$ as expected.

We will also have to consider singular weights, which are by definition couples $\phi:=\left\{\left(U_{\alpha}, \varphi_{\alpha}\right)\right\}$ where $U_{\alpha}$ is covering of $X$ trivializing $L$, and $\varphi_{\alpha}$ are locally integrable on $U_{\alpha}$, satisfying $\varphi_{\beta}-\varphi_{\alpha}=\log \left|g_{\alpha \beta}\right|^{2}$ on $U_{\alpha} \cap U_{\beta}$. The associated curvature current, denoted by $d d^{c} \phi$, is well-defined on $X$. The weight is said psh if the $\varphi_{\alpha}$ are, in which case $d d^{c} \phi$ is a positive current. Moreover, we can proceed as in the smooth case to attach to $d d^{c} \phi$ a class $\hat{c}_{1}(L) \in H^{1}\left(X, \mathcal{P} \mathcal{H}_{X}\right)$ (consider $\phi$ as a section of the sheaf $L_{\text {loc }}^{1} / \mathcal{P} \mathcal{H}_{X}$ and use the natural exact sequence), whose image in $H^{2}(X, \mathbb{R})$ via the long exact sequence in cohomology induced by (1.1) is $c_{1}(L)$. Therefore when $\phi$ is a singular weight on $L$, we may say that $d d^{c} \phi$ is a current in $c_{1}(L)$.

We claim that a (possibly singular) psh weight $\phi$ on $L_{\mid X_{\text {reg }}}$ - and thus a psh weight in the usual sense- automatically extends to a (unique) psh weight $\widetilde{\phi}$ on $L$. Indeed, by Grauert and Remmert's theorem, the $\varphi_{\alpha}$ 's defined on $U_{\alpha} \cap X_{\text {reg }}$ extend to a psh function $\widetilde{\varphi_{\alpha}}$ on the whole $U_{\alpha}$, which is moreover defined by $\widetilde{\varphi_{\alpha}}\left(z_{0}\right)=\limsup _{X_{\text {reg }} \ni z \rightarrow z_{0}} \varphi_{\alpha}(z)$. Therefore, the relation $\widetilde{\varphi_{\beta}}=\widetilde{\varphi_{\alpha}}+\log \left|g_{\alpha \beta}\right|^{2}$ is immediately satisfied on the whole $U_{\alpha} \cap U_{\beta}$, which proves the claim.

If we get back to the non-normal case, we can define psh weights using weakly psh functions instead of psh functions. So the general philosophy is that we always pull-back our objects to the normalization where things behave better, and the notions downstairs are defined and studied upstairs. For example, we can define on a normal variety the analogue of the non-pluripolar product and consider Monge-Ampère equations as in the smooth case (cf [BBE ${ }^{+}$11, §1.1-1.2]. Then, if we write them on a non-normal variety, they have to be thought as pulled-back to the normalization.

Log canonical pairs. - Following the by now common terminology of Mori theory and the minimal model program (cf e.g. [KM98]), a pair $(X, D)$ is by definition a complex normal projective variety $X$ carrying a Weil $\mathbb{Q}$-divisor $D$ (not necessarily effective). We will say that the pair $(X, D)$ is a log canonical pair if $K_{X}+D$ (which is a priori defined as a Weil divisor) is $\mathbb{Q}$-Cartier, and if for some (or equivalently any) $\log$ resolution $\pi: X^{\prime} \rightarrow X$, we have:
$$K_{X^{\prime}}=\pi^{*}\left(K_{X}+D\right)+\sum a_{i} E_{i}$$
where $E_{i}$ are either exceptional divisors or components of the strict transform of $D$, and the coefficients $a_{i}$ satisfy the inequality $a_{i} \geqslant-1$.

\section*{2. Singular Kähler-Einstein metrics}
2.1. Kähler-Einstein metrics on pairs. - In this section, we will consider log pairs $(X, D)$ where $X$ is a complex normal projective variety, $D$ is a Weil divisor, and $K_{X}+D$ is assumed to be $\mathbb{Q}$-Cartier. We choose a psh weight $\phi_{D}$ on $X_{\text {reg }}$ satisfying $d d^{c} \phi_{D}=\left[D_{\mid X_{\text {reg }}}\right]$. The first definition concerns the Ricci curvature of currents:

Definition 2.1. - Let $\omega$ be a positive current on $X_{\text {reg }}$; we say that $\omega$ is admissible if it satisfies:
\begin{itemize}
\item[1.] Its non-pluripolar product $\left\langle\omega^{n}\right\rangle$ defines a (locally) absolutely continuous measure on $X_{\text {reg }}$ with respect to $d \mathbf{z} \wedge d \overline{\mathbf{z}}$, where $\mathbf{z}=\left(z_{i}\right)$ are local holomorphic coordinates.
\item[2.] The function $\log \left(\left\langle\omega^{n}\right\rangle / d \mathbf{z} \wedge d \overline{\mathbf{z}}\right)$ belongs to $L_{\text {loc }}^{1}\left(X_{\text {reg }}\right)$.
\end{itemize}

In that case, we define (on $X_{\text {reg }}$ ) the Ricci curvature of $\omega$ by setting Ric $\omega:=-d d^{c} \log \left\langle\omega^{n}\right\rangle$.
Another way of thinking of this is to interpret the positive measure $\left\langle\omega^{n}\right\rangle_{\mid X_{\text {reg }}}$ as a singular metric on $-K_{X_{\text {reg }}}$ whose curvature is Ric $\omega$ by definition.

The measure $e^{\phi}$ for $\phi$ a weight on $K_{X}$. - In the same spirit, we will use the convenient but somehow abusive notation $e^{\phi}$ for $\phi$ a weight on $K_{X}$ (whenever the latter is defined as a $\mathbb{Q}$-line bundle) to refer to the positive measure $e^{\varphi_{\mathbf{z}}} d \mathbf{z} \wedge d \overline{\mathbf{z}}$ defined on $X_{\text {reg }}$ and extended by 0 to $X$; where $\varphi_{\mathbf{z}}$ is the expression on some trivializing chart of $X_{\text {reg }}$ (and hence of $K_{X_{\text {reg }}}$ too) of $\phi$. In particular, for $\phi$ a psh weight on $K_{X}+D$, the measure $e^{\phi-\phi_{D}}$ can easily be pulled-back to any log resolution $\left(\pi, X^{\prime}, D^{\prime}\right)$ of $(X, D)$ (we pull it back over $X_{\text {reg }} \backslash \operatorname{Supp}(D)$ and then extend it by 0), where it become $e^{\phi \circ \pi-\phi_{D^{\prime}}}$.

We may now introduce the notion of (negatively curved) Kähler-Einstein metric attached to a pair $(X, D)$ :

Definition 2.2. - Let $(X, D)$ be a log pair; we say that a positive admissible current $\omega$ is a Kähler-Einstein metric with negative curvature for $(X, D)$ if:
\begin{itemize}
\item[1.] Ric $\omega=-\omega+[D]$ on $X_{\text {reg }}$,
\item[2.] $\int_{X_{\text {reg }}}\left\langle\omega^{n}\right\rangle=c_{1}\left(K_{X}+D\right)^{n}$.
\end{itemize}

This conditions are sufficient to show that a Kähler-Einstein metric is a global solution of a Monge-Ampère equation. More precisely, we have the following:

Proposition 2.3. - Let $(X, D)$ be a log pair, and $\omega$ be a Kähler-Einstein metric for $(X, D)$. Then $\phi:=\log \left\langle\omega^{n}\right\rangle+\phi_{D}$ extends to $X$ as a psh weight with full Monge-Ampère mass on $K_{X}+D$, solution of
$$\left\langle\left(d d^{c} \phi\right)^{n}\right\rangle=e^{\phi-\phi_{D}}$$
Conversely, any psh weight $\phi$ on $K_{X}+D$ with full Monge-Ampère mass solution of the equation induces a Kähler-Einstein metric $\omega:=d d^{c} \phi$ for $(X, D)$.

Proof. - On $X_{\text {reg }}$, we have $d d^{c} \phi=\omega$ thus $\phi$ is a psh weight on $\left(K_{X}+D\right)_{\mid X_{\text {reg }}}$, and thanks to a theorem of Grauert and Remmert, it extends through $X_{\text {sing }}$ which has codimension at least 2. Clearly, we have $\omega=d d^{c} \phi$ on $X$, and by condition 3. in the definition of a Kähler-Einstein metric, $\phi$ has full Monge-Ampère mass. Then by definition, the two (non-pluripolar) measures $\left\langle\left(d d^{c} \phi\right)^{n}\right\rangle$ and $e^{\phi-\phi_{D}}$ coincide.

For the converse, let $\omega:=d d^{c} \phi$; clearly 1. and 3. are satisfied. Moreover, $\phi$ and $\phi_{D}$ are locally integrable, so that $\omega$ is admissible and $\operatorname{Ric} \omega=-d d^{c}\left(\phi-\phi_{D}\right)=-\omega+[D]$. \(\square\)

This proposition shows that the different definitions of what should be a singular Kähler-Einstein metric, appearing e.g. in [Ber13, BEGZ10, CGP13, EGZ09] etc. coincide. Moreover, one could equally define positively curved Kähler-Einstein metrics in an equivalent way as in $\left[\mathbf{B B E}^{+} \mathbf{1 1}\right]$. In particular this objects, intrinsically defined on $X$, can also be seen on any log resolution in the usual way; in practice, we will most of the time work on log resolutions when dealing with existence or smoothness questions.

Note also that we could have chosen to define a Kähler-Einstein metric attached to a pair $(X, D)$ (say satisfying $K_{X}+D$ ample) to be a smooth Kähler metric $\omega$ on $X_{\text {reg }} \backslash \operatorname{Supp}(D)$ which extends to an admissible current on $X_{\text {reg }}$ satisfying there $\operatorname{Ric} \omega=-\omega+[D]$ and the mass condition $\left(\int_{X_{\text {reg }}}\left\langle\omega^{n}\right\rangle=\right) \int_{X_{\text {reg }} \backslash \operatorname{Supp}(D)} \omega^{n}=c_{1}\left(K_{X}+D\right)^{n}$.

Then, our regularity Theorem (say combined with Proposition 5.1) shows a posteriori that this definition would have coincided with Definition 2.2.

Let us also mention that in the case of a log smooth log canonical pair $(X, D)$, the same proof as [Gue14, Proposition 2.5] combined with [GW14] will show that the data of a negatively curved Kähler-Einstein on $(X, D)$ is equivalent to giving an admissible current $\omega$ on $X \backslash \operatorname{Supp}(D)$ such that:
\begin{itemize}
\item[-] $\operatorname{Ric} \omega=-\omega$ on $X \backslash \operatorname{Supp}(D)$,
\item[-] There exists $C>0$ such that
$$C^{-1} d V \leqslant \prod_{a_{j}<1}\left|s_{j}\right|^{2 a_{j}} \cdot \prod_{a_{k}=1}\left(\left|s_{k}\right|^{2} \log ^{2}\left|s_{k}\right|^{2}\right) \omega^{n} \leqslant C d V$$
for some volume form $d V$ on $X$, and where $D=\sum a_{i} D_{i}, s_{i}$ being a defining section of $D_{i}$.
\end{itemize}
2.2. Kähler-Einstein metrics on stable varieties. - Stable varieties, as considered e.g. in [KSB88, Kar00, Kol, Kov13] are the appropriate singular varieties to look at if one wants to compactify the moduli space of canonically polarized projective varieties (cf also [Vie95]). Before giving the precise definition of a stable variety, we explain very briefly that notion and give the connection with Kähler-Einstein theory. In the next section, we will give a more detail account of the type of singularities involved.

So first of all, we will consider complex varieties that are Gorenstein in codimension 1 (this condition replaces regularity in codimension 1 for normal varieties) and satisfy the condition $S_{2}$ of Serre. Basically, the singularities in codimension 1 of our varieties are those of the union of two coordinate hyperplanes ("double crossing"), so it is important to be aware that such varieties are in general not irreducible, and hence their normalization will not be connected.

Now we want to recast them in the context given by the singularities of the minimal model program (MMP); so we consider such a variety $X$ and its normalization $\nu: X^{\nu} \rightarrow X$. One can write $\nu^{*} K_{X}=K_{X^{\nu}}+D$ for some reduced divisor $D$ called the conductor of $\nu$; its sits above the codimension 1 component of the singular locus of $X$. We then say that $X$ has semi log canonical singularities if the pair $\left(X^{\nu}, D\right)$ is log canonical in the usual sense. The generalization of the notion of stable curve is given by the following definition:

Definition 2.4. - A projective variety $X$ is called stable if $X$ has semi-log canonical singularities, and $K_{X}$ is an ample $\mathbb{Q}$-line bundle.

There is a subtlety for the definition of $K_{X}$, but we refer to §2.3 for appropriate explanations. Its is actually possible to define the notion of Kähler-Einstein metric for a stable variety:

Definition 2.5. - Let $X$ be a stable variety. A Kähler-Einstein metric on $X$ is a positive admissible current $\omega$ on $X_{\text {reg }}$ such that:
\begin{itemize}
\item[1.] Ric $\omega=-\omega$ on $X_{\text {reg }}$,
\item[2.] $\int_{X_{\text {reg }}}\left\langle\omega^{n}\right\rangle=c_{1}\left(K_{X}\right)^{n}$.
\end{itemize}

In the non-normal case however, psh weight do not automatically extend across the singularities, so that it is not clear that the Kähler-Einstein metric will extend as a positive current on $K_{X}$ satisfying the usual Monge-Ampère equation globally. Actually, this is the case as shows the following proposition:

Proposition 2.6. - Let $X$ be a stable variety, and $\omega$ a Kähler-Einstein metric on $X$. Then the weight $\phi:=\log \omega^{n}$ extends to $X$ as a weakly psh weight on $K_{X}$ solution of the Monge-Ampère equation $\left\langle\left(d d^{c} \phi\right)^{n}\right\rangle=e^{\phi}$.

Proof. - Taking the $d d^{c}$ of each side in the definition of $\phi$ and using the Ricci equation, we find $\omega=d d^{c} \phi$ on $X_{\text {reg }}$, and therefore $\phi$ satisfies $\left\langle\left(d d^{c} \phi\right)^{n}\right\rangle=\left\langle\omega^{n}\right\rangle=e^{\phi}$. Pulling back this equation to normalization $X^{\nu}$, we find a psh weight $\phi^{\prime}=\nu^{*} \phi$ on $c_{1}\left(\nu^{*} K_{X}\right)_{\mid \nu^{-1}\left(X_{\text {reg }}\right)}$ solution of $\left\langle\left(d d^{c} \phi^{\prime}\right)^{n}\right\rangle=e^{\phi^{\prime}-\phi_{D}}$ where $D$ is the conductor of the normalization. As we work inside $X_{\text {reg }}^{\nu}$ and the integral $\int_{\nu^{-1}\left(X_{\text {reg }}\right)} e^{\phi^{\prime}-\phi_{D}}$ is finite, we infer from Lemma 2.7 below that $\phi^{\prime}$ extends (as a psh weight) across $D_{\text {reg }}$. So $\phi^{\prime}$ induces a psh weight on $c_{1}\left(\nu^{*} K_{X}\right)_{\mid X_{\text {reg }}^{\nu} \backslash D_{\text {sing }}}$, and by normality of $X^{\nu}$, it extends to the whole $X^{\nu}$, which means precisely that $\phi$ extends as a weakly psh weight on $K_{X}$. The expected Monge-Ampère equation holds automatically on $X$ (or equivalently on $X^{\prime}$ ) since both measures $\left\langle\left(d d^{c} \phi\right)^{n}\right\rangle$ and $e^{\phi}$ put no mass on $X_{\text {sing }}$ by definition. \(\square\)

In the previous proof, we used the following extension result:
Lemma 2.7. - Let $U$ be a neighbourhood of $0 \in \mathbb{C}^{n}, H=\left\{z_{1}=0\right\} \subset \mathbb{C}^{n}$, and $\varphi$ be a psh function defined on $U \backslash H$. We assume that the integral
$$\int_{U \backslash H} \frac{e^{\varphi}}{\left|z_{1}\right|^{2}} d V$$
is finite. Then $\varphi$ extends across $H$, and more precisely $\varphi$ tends to $-\infty$ near $H$.
Proof. - (thanks to Bo Berndtsson for providing us with this elegant proof) Assume, to get a contradiction, that $\varphi$ does not tend to $-\infty$ near $H$, and let $V:=U \backslash H$. Then we can find a sequence $\left(x_{k}\right)$ of points in $V$ converging to $H$ such that $\varphi\left(x_{k}\right) \geqslant-C$ for some constant $C$. We write $x_{k}=\left(x_{1, k}, \ldots, x_{n, k}\right)$, and we set $r_{k}=\left|x_{1, k}\right| / 2$; the sequence $\left(r_{k}\right)$ converges to 0 , and if $D_{k}$ denotes the polydisk centered at $x_{k}$ with polyradius $\left(r_{k}, \delta, \ldots, \delta\right)$ for some fixed $\delta>0$, then we have $D_{k} \subset V$.
Using the mean value inequality for $\varphi$ at $x_{k}$, we find:
$$-C \leqslant \frac{1}{\operatorname{vol}\left(D_{k}\right)} \int_{D_{k}} \varphi d V$$
Therefore, using Jensen's inequality, we obtain, up to modifying $C$ by a normalization factor depending only on the dimension $n$ :
$$e^{-C} \leqslant \int_{D_{k}} \frac{e^{\varphi} d V}{r_{k}^{2} \delta^{2(n-1)}}$$
but on $D_{k},\left|z_{1}\right| \leqslant 3 r_{k}$ so
$$e^{-C^{\prime}} \leqslant \int_{D_{k}} \frac{e^{\varphi} d V}{\left|z_{1}\right|^{2}}$$
for $C^{\prime}=C+\log 9-2(n-1) \log \delta$. As the measure of $D_{k}$ goes to zero when $k \rightarrow+\infty$, it shows that the integral $\int_{U \backslash H} \frac{e^{\varphi}}{\left|z_{1}\right|^{2}} d V$ is infinite, which is absurd. \(\square\)
2.3. Singularities of stable varieties. - In this paragraph, we intend to give a more precise overview of the notion of semi-log canonical singularities. As we will just touch on this topic, we refer to the nice survey [Kov13] for a broader study. Other good references are [Kol, KSB88].
In the following, $X$ will always be a reduced and equidimensional scheme of finite type over $\mathbb{C}$, and we set $n:=\operatorname{dim} X$. We emphasize again on the fact that $X$ will not be irreducible in general.

The conditions $G_{1}$ and $S_{2}$. - As we saw earlier, we need a canonical sheaf. The condition $G_{1}$ will guarantee its existence, and the condition $S_{2}$ will (among other things) ensure its uniqueness.

If $X$ is Cohen-Macaulay (for every $x \in X$, the depth of $\mathcal{O}_{X, x}$ is equal to its Krull dimension), then $X$ admits a dualizing sheaf $\omega_{X}$. We say that $X$ is Gorenstein if $X$ is Cohen-Macaulay and $\omega_{X}$ is a line bundle. We say that $X$ is $G_{1}$ if $X$ is Gorenstein in codimension 1, which means that there is an open subset $U \subset X$ which is Gorenstein and satifies $\operatorname{codim}_{X}(X \backslash U) \geqslant 2$.

We say that $X$ satisfies the condition $S_{2}$ of Serre if for all $x \in X$, we have $\operatorname{depth}\left(\mathcal{O}_{X, x}\right) \geqslant$ $\min \left\{\operatorname{ht}\left(\mathfrak{m}_{X, x}\right), 2\right\}$, where $\operatorname{ht}\left(\mathfrak{m}_{X, x}\right)=\operatorname{codim}(\bar{x})$ denotes the height of the maximal ideal $\mathfrak{m}_{X, x}$ of $\mathcal{O}_{X, x}$. This condition is equivalent to saying that for each closed subset $i: Z \hookrightarrow X$ of codimension at least two, the natural map $\mathcal{O}_{X} \rightarrow i_{*} \mathcal{O}_{X \backslash Z}$ is an isomorphism.

If $X$ is $G_{1}$ and $S_{2}$, and $U \subset X$ is a Gorenstein open subset whose complement has codimension at least 2, one can then define the canonical sheaf $\omega_{X}$ by $\omega_{X}:=j_{*} \omega_{U}$ where $j: U \hookrightarrow X$ is the open embedding, and $\omega_{U}$ is the dualizing sheaf of $U$. By definition, this is a rank one reflexive sheaf. When $X$ is projective, we know that it admits a dualizing sheaf; as it is reflexive, it coincides with $\omega_{X}$ by the $S_{2}$ condition.

We would like to have an interpretation of $\omega_{X}$, or at least $\omega_{U}$ in terms of Weil divisor as in the normal case where we define the Weil divisor $K_{X}$ as the closure of some Weil divisor representing the line bundle $K_{X_{\text {reg }}}$. But we have to be more cautious in the non normal case it is not clear how we should extend a Weil divisor given on $X_{\text {reg }}$. Actually, this is where the $G_{1}$ conditions appears: as $\omega_{U}$ is a line bundle, or equivalently a Cartier divisor, we may choose a Weil divisor $K_{U}$ whose support does not contain any component of $X_{\text {sing }}$ of codimension 1 and represent $\omega_{U}$ (write $\omega_{U}$ as the difference of two very ample line bundles). Then we define $K_{X}$ to be the closure of $K_{U}$. Clearly, the divisorial sheaf $\mathcal{O}_{X}\left(K_{X}\right)$ is reflexive, and coincides with $\omega_{U}=\omega_{X \mid U}$ on $U$, so that by the $S_{2}$ condition, we get:
$$\omega_{X} \simeq \mathcal{O}_{X}\left(K_{X}\right)$$
In fact, if $\omega_{X}^{[m]}$ denotes the $m$-th reflexive power of $\omega_{X}$, the same arguments yield $\omega_{X}^{[m]} \simeq$ $\mathcal{O}_{X}\left(m K_{X}\right)$. Therefore, the Weil divisor is $\mathbb{Q}$-Cartier if and only if $\omega_{X}$ is a $\mathbb{Q}$-line bundle, i.e. $\omega_{X}^{[m]}$ is a line bundle for some $m>0$.

Conductors and slc singularities. - Let now $X$ be a (reduced) scheme, and $\nu: X^{\nu} \rightarrow X$ its normalization. We recall that if $X$ is not irreducible, its normalization is defined to be the disjoint union of the normalization of its irreducible components. The conductor ideal
$$\operatorname{cond}_{X}:=\mathscr{H}_{0} m_{\mathcal{O}_{X}}\left(\nu_{*} \mathcal{O}_{X^{\nu}}, \mathcal{O}_{X}\right)$$
is the largest ideal sheaf on $X$ that is also an ideal sheaf on $X^{\nu}$. If we think of the case where $B$ is the integral closure of some integral ring $A$, then we can easily see that $\operatorname{Hom}_{A}(B, A)$ injects in A (via the evaluation at 1), and the image of this map is the annihilator $\operatorname{Ann}_{A}(B / A)=\{f \in A ; f B \subset A\}$, or equivalently the largest ideal $\mathcal{I} \subset A$ that is also an ideal in $B$.

Coming back to the case of varieties, we will denote by $\operatorname{cond}_{X^{\nu}}$ the conductor seen as an ideal sheaf on $X^{\nu}$, and we define the conductor subschemes as $C_{X}:=\operatorname{Spec}_{X}\left(\mathcal{O}_{X} / \operatorname{cond}_{X}\right)$ and $C_{X^{\nu}}:=\operatorname{Spec}_{X^{\nu}}\left(\mathcal{O}_{X^{\nu}} / \operatorname{cond}_{X^{\nu}}\right)$. If $X$ is $S_{2}$, then one can show that these schemes have pure codimension 1 (and hence define Weil divisors) but they are in general not reduced (e.g. the cusp $y^{2}=x^{3}$ ).

If $K_{X}$ is $\mathbb{Q}$-Cartier and $X$ is demi-normal (i.e. $X$ is $S_{2}$ and has only double crossing singularities in codimension 1, cf [Kol]), we have the following relation:
$$\nu^{*} K_{X}=K_{X^{\nu}}+C_{X^{\nu}}$$

The proof of this identity goes as follows: first, using the demi-normality assumption, we may assume that the only singularities of $X$ are double normal crossings. Then, using the universal property of the dualizing sheaf (which coincide with the canonical sheaf as we observed above) and the projection formula, we have $\nu_{*} \omega_{X^{\nu}}=\omega_{X}\left(-C_{X}\right)$. We pull-back this relation to $X^{\nu}$ using the fact that the sheaf $\mathcal{O}_{X}\left(-C_{X}\right)$ becomes precisely $\mathcal{O}_{X^{\nu}}\left(-C_{X^{\nu}}\right)$. By the assumptions on the singularities, this last sheaf is actually an invertible sheaf so that we get the expected identity (cf point 8 in [Kol]). As we will explain below, we do not want to assume a priori that our varieties are demi-normal. Therefore, it may happen that $C_{X^{\nu}}$ is not Cartier, and the formula (2.1) may not be true anymore. So whenever we will deal with Kähler-Einstein on those varieties, we will have to apply the arguments on a log-resolution of the normalization instead of the normalization itself. Anyway, this will not cause any troubles.

An important point is that whenever the conductor is reduced, then necessarily $X$ is seminormal (i.e. every finite morphism $X^{\prime} \rightarrow X$ (with $X^{\prime}$ reduced) that is a bijection on points is an isomorphism); moreover, a seminormal scheme which is $G_{1}$ and $S_{2}$ has only double crossing singularities in codimension 1, i.e. it is demi-normal. We refer to [Tra70, GT80, KSS10]) for the previous assertions. This leads to the following definition:

Definition 2.8. - We will say that $X$ has semi-log canonical singularities if:
\begin{itemize}
\item[1.] $X$ is $G_{1}$ and $S_{2}$,
\item[2.] $K_{X}$ is $\mathbb{Q}$-Cartier,
\item[3.] The pair ( $X^{\nu}, C_{X^{\nu}}$ ) is log-canonical.
\end{itemize}

If $X$ has semi-log canonical singularities (slc), then $C_{X^{\nu}}$ is necessarily reduced, and therefore the codimension 1 singularities of $X$ are only double crossing as we explained above. This assumption is usually added in the definitions (cf [Kol, Kov13]), but we may keep it or not without any change. This justifies the seemingly different definition given in the previous section. Finally, we can give the definition of a stable variety:

Definition 2.9. - We say that $X$ is stable if
\begin{itemize}
\item[1.] $X$ is projective,
\item[2.] $X$ has semi-log canonical singularities,
\item[3.] $K_{X}$ is $\mathbb{Q}$-ample.
\end{itemize}

Singularities and Kähler-Einstein metrics: a summary. - If we take a closer look at the proof of Proposition 2.6, we see that we did not use all of the properties of a stable variety to see that a Kähler-Einstein metric always extend. Actually, we just used the fact that the conductor was a divisor. Therefore, using the existence and regularity results that we are going to prove in the next sections, and the restriction on the singularities of a pair carrying a Kähler-Einstein metric (cf Proposition 5.1), we can summarize the problem of the existence of a Kähler-Einstein metric on a stable variety in the following statement:

Theorem 2.10. - Let $X$ be a reduced $n$-equidimensional projective scheme over $\mathbb{C}$, satisfying the conditions $G_{1}$ and $S_{2}$, and such that $K_{X}$ is an ample $\mathbb{Q}$-line bundle. Then the following are equivalent:
\begin{itemize}
\item[1.] There exists a Kähler form $\omega$ on $X_{\text {reg }}$ such that $\operatorname{Ric} \omega=-\omega$ and $\int_{X_{\text {reg }}} \omega^{n}=c_{1}\left(K_{X}\right)^{n}$,
\item[2.] There exists $\omega$ as above which extends to define a positive current in $c_{1}\left(K_{X}\right)$,
\item[3.] $X$ has semi-log canonical singularities, i.e. $X$ is stable.
\end{itemize}

Moreover, by the results of Odaka [Oda13, Oda12], the latter condition is equivalent to:
\begin{itemize}
\item[4.] The pair $\left(X, K_{X}\right)$ is $K$-stable.
\end{itemize}

\section*{3. Variational solutions}
3.1. General setting. - Consider the following general setting: $X$ is a compact Kähler manifold and $[\omega]$ a big class, with $\omega$ smooth (but not necessarily positive). We say that a function $u \in P S H(X, \omega)$ has full Monge-Ampère mass, and we will write $u \in \mathcal{E}(X, \omega)$, if the total mass of $\operatorname{MA}(u)$ is equal to the volume of the class $[\omega]$, where the volume in question may be defined by $V:=\operatorname{vol}([\omega]):=\int_{X} \mathrm{MA}\left(u_{\text {min }}\right)$, for $u_{\text {min }}$ any element in $P S H(X, \omega)$ with minimal singularities, cf §1.

We now recall an important subspace of $\mathcal{E}(X, \omega)$ denoted by $\mathcal{E}^{1}(X, \omega)$, and consisting of functions with finite energy. The energy $\mathcal{E}(u)$ of an $\omega$-psh function $u$ (not necessarily in $\mathcal{E}(X, \omega)$ ) is defined in the following way (cf [GZ07, BEGZ10, BBGZ13] for more details - the energy is sometimes denoted by $E$ in the aforementioned papers).
First, if $u \in P S H(X, \omega)$ has minimal singularities, we set
$$\mathcal{E}(u):=\frac{1}{(n+1) V} \sum_{j=0}^{n} \int_{X}\left(u-V_{\theta}\right) \operatorname{MA}\left(u^{(j)}, V_{\theta}^{(n-j)}\right)$$
where MA is the mixed non-pluripolar Monge-Ampère operator. If now $u$ is any $\omega$-psh function, we defined
$$\mathcal{E}(u):=\inf \{\mathcal{E}(v) \mid v \in P S H(X, \omega) \text { with minimal singularities, } v \geqslant u\}$$
Then we set $\mathcal{E}^{1}(X, \omega):=\{u \in P S H(X, \omega), \mathcal{E}(u)>-\infty\}$. Actually, [BEGZ10, Proposition $2.11]$ gives another characterization of this last space: a function $u \in P S H(X, \omega)$ belongs to $\mathcal{E}^{1}(X, \omega)$ if and only if $u \in \mathcal{E}(X, \omega)$ and $\int_{X}\left(u-V_{\theta}\right) \mathrm{MA}(u)<+\infty$ (and for any $u \in \mathcal{E}(X, \omega)$, the explicit integral formula for $\mathcal{E}(u)$ above is still valid). Using this result, it becomes clear that $\mathcal{E}^{1}(X, \omega) \subset \mathcal{E}(X, \omega)$ as announced.

We should finally add that $\mathcal{E}$ is an upper-semicontinuous (usc) concave functional on $P S H(X, \omega)$, and that it is the normalized primitive of the Monge-Ampère operator, i.e.
$$(d \mathcal{E})_{u}=\frac{1}{V} \operatorname{MA}(u)^{n} .$$
3.2. Uniqueness. - Given a measure $\mu$ on $X$ (possible non-finite) we consider the following MA-equation for $u \in P S H(X, \omega)$ attached to the pair $(\omega, \mu)$ :
$$\omega_{u}^{n}=e^{u} \mu,$$
where $\omega_{u}^{n}:=\operatorname{MA}(u)$ is the non-pluripolar Monge-Ampère operator as before. This equation is equivalent to the following normalized MA-equation on $\mathcal{E}(X, \omega) / \mathbb{R}$ :
$$\frac{\omega_{u}^{n}}{V}=\frac{e^{u} \mu}{\int e^{u} \mu}$$
The equivalence follows immediately from the $\mathbb{R}$-invariance of the latter equation and the substitution $u \mapsto u-\log \int e^{u} \mu$ which maps solutions of equation (3.2) to solutions of the equation (3.3).

Proposition 3.1. - Any two solutions $u$ and $v$ of the $M A$-equation (3.2) such that $u$ and $v$ are in $\mathcal{E}(X)$ coincide.

Proof. - This is an immediate consequence of the comparison principle [BEGZ10, Corollary 2.3]: if $u$ and $v$ are in $\mathcal{E}(X)$ then
$$\int_{\{u<v\}} \operatorname{MA}(v) \leqslant \int_{\{u<v\}} \operatorname{MA}(u)$$
But the MA above then forces $u=v$ a.e wrt the measure $\mu$. Since $\mu$ cannot charge pluripolar sets (as MA(u) does not) it follows that $u=v$ away from a pluripolar set and hence everywhere, by basic properties of psh functions. \(\square\)
3.3. Existence results for log canonical pairs. - Let $(X, D)$ be a log canonical pair such that the log canonical divisor $K_{X}+D$ is big. Assume that $(X, D)$ is a log smooth, i.e. $X$ is smooth and
$$D=\sum_{i} c_{i} D_{i}$$
is a normal crossings divisor with $\left.\left.c_{i} \in\right]-\infty, 1\right]$. To the pair $(X, D)$ we can associate the following Kähler-Einstein type equation for a metric $\phi$ on $L:=K_{X}+D:$
$$\left(d d^{c} \phi\right)^{n}=e^{\phi-\phi_{D}},$$
where $\phi_{D}=\sum_{i} c_{i} \log \left|s_{i}\right|^{2}$ and $s_{i}$ are sections cutting out the divisors $D_{i}$ above.
Theorem 3.2. - There is a unique finite energy solution $\phi$ to the equation above.
Proof. - The proof is a modification of the variational approach in [BBGZ13] (concerning the case when $D$ is trivial). To explain this we fix a smooth form $\omega \in c_{1}\left(K_{X}+D\right)$. Then the equation above is equivalent to a Monge-Ampère equation for an $\omega$-psh function $u$ :
$$\omega_{u}^{n}=e^{u} \mu$$
where the measure $\mu$ is of the form $\mu=\rho d V$ for a function $\rho$ in $L^{1-\delta}(X)$ (but $\rho$ is not in $\left.L^{1}(X)!\right)$. We let
$$\mathcal{L}(u):=-\log \int e^{u} \mu$$

Then, at least formally, solutions of equation (3.5) are critical points of the functional
$$\mathcal{G}(u):=\mathcal{E}(u)+\mathcal{L}(u) .$$
in view of the equation (3.1) satisfied by $\mathcal{E}$. $\mathcal{L}$ also defines an usc concave functional on $\operatorname{PSH}(X, \omega)$ and we let $\mathcal{L}(X, \omega):=\{\mathcal{L}>-\infty\}$ (the upper semi-continuity follows from Fatou's lemma).

Note that Lemma 3.3 below guarantees that the intersection $\mathcal{E}^{1}(X, \omega) \cap \mathcal{L}(X, \omega)$ is nonempty. Hence, $\mathcal{G}(u)$ is not identically equal to $-\infty$ on its domain of definition that we will take to be $\mathcal{E}^{1}(X, \omega)$ (equipped with the usual $L^{1}(X)$-topology).

Next, we observe that
$$\mathcal{G}(u) \leqslant \mathcal{E}(u)-\int u \mu_{0}+C^{\prime \prime}$$

Indeed, since $\mu \geqslant C \mu_{0}$, where $\mu_{0}$ is finite measure on $X$ integrating all quasi-psh functions on $X$ (in our case we may take $\mu_{0}=\left\|s^{\prime}\right\| d V$ for some holomorphic section $s^{\prime}$ defined by the negative coefficients of $D$ ) :
$$\int e^{u} \mu \geqslant C \int e^{u} \mu_{0}$$
and hence
$$\mathcal{L}(u) \leqslant C^{\prime}-\log \int e^{u} \mu_{0} \leqslant C^{\prime \prime}-\int u \mu_{0}$$
using Jensen's inequality, which proves (3.6). In particular, $\mathcal{G}(u)$ is bounded from above. Indeed, by scaling invariance we may assume that $\sup _{X} u=0$ and then use that, by basic compactness properties of $\omega$-psh functions, $\sup u \leqslant \int u \mu_{0}+C$.

Let now $u_{j} \in \mathcal{E}^{1}(X, \omega)$ be a sequence such that
$$\mathcal{G}\left(u_{j}\right) \rightarrow \sup _{\mathcal{E}^{1}(X, \omega)} \mathcal{G}:=S<\infty$$
Again, by the scale invariance of $\mathcal{G}$ we may assume that $\sup _{X} u_{j}=0$. In particular,
$$\mathcal{L}\left(u_{j}\right) \geqslant S / 2-\mathcal{E}\left(u_{j}\right)$$
for $j>j_{0}$. But, by $(3.6), \mathcal{E}\left(u_{j}\right)$ is bounded from below and hence there is a constant $C$ such that
$$\mathcal{E}\left(u_{j}\right) \geqslant-C, \quad \mathcal{L}\left(u_{j}\right) \geqslant-C$$
Let now $u_{*}$ be a limit point of $u_{j}$. By upper-semicontinuity we have that
$$\mathcal{E}(u) \geqslant-C, \quad \mathcal{L}(u) \geqslant-C$$
Finally, we note that $u_{*}$ satisfies the equation (3.5) by applying the projection argument from [BBGZ13] as follows. Fixing $v \in \mathcal{C}^{\infty}(X)$ let $f(t):=\mathcal{E}_{\omega}\left(P_{\omega}\left(u_{*}+t v\right)\right)+\mathcal{L}\left(u_{*}+t v\right)$, where
$$P_{\omega}(u)(x):=\sup \{v(x): v \leqslant u, v \in P S H(X, \omega)\}$$
(note that $f(t)$ is finite for any $t$ ). The functional $\mathcal{L}(u)$ is decreasing in $u$ and hence the sup of $f(t)$ on $\mathbb{R}$ is attained for $t=0$. Now $\mathcal{E}_{\omega} \circ P_{\omega}$ is differentiable with differential $M A\left(P_{\omega} u\right)$ at
$u$ [BBGZ13]. Hence, the condition $d f / d t=0$ for $t=0$ gives that the variational equation (3.5) holds when integrated against any $v \in \mathcal{C}^{\infty}(X)$. \(\square\)

Let us now prove the following result, that we used in the proof:
Lemma 3.3. - Let $(X, D)$ be a log smooth pair and $L$ a big line bundle. Let $\theta$ be a smooth $(1,1)$ form whose cohomology class is $c_{1}(L)$. Let $s_{0}$ be a section of $D$, and $|\cdot|$ a smooth hermitian metric on $\mathcal{O}_{X}(D)$. Then there exists a $\theta$-psh function $u \in \mathcal{E}^{1}(X, \theta)$ such that $e^{u} /\left|s_{0}\right|^{2}$ is integrable.

Proof. - As $L$ is big, the exists $m$ big enough such that $m L-D$ is effective. We choose $t$ a holomorphic section of $m L-D$, and consider $s:=s_{0} t$ which is a section of $m L$ vanishing along $D$. Let $h_{0}$ be an smooth hermitian metric on $L$ with curvature form $\theta$, and let $V_{\theta}$ be the upper envelope of all (normalized) $\theta$-psh functions. We define on $m L$ the hermitian metric $h:=h_{0}^{\otimes m} e^{-m V_{\theta}}$. For $0<\alpha<1$ small enough we claim that the function
$$u:=V_{\theta}-\left(-\frac{1}{m} \log |s|_{h}^{2}\right)^{\alpha}$$
suits our requirements.

First of all, it is $\theta$-psh because of the following general fact: if $\psi$ is $\theta$-psh and $\chi: \mathbb{R} \rightarrow \mathbb{R}$ is convex and non-decreasing satisfying $\chi^{\prime} \leqslant 1$, then $V_{\theta}+\chi\left(\psi-V_{\theta}\right)$ is $\theta$-psh. Indeed, $d d^{c}\left(V_{\theta}+\chi\left(\psi-V_{\theta}\right)\right)=\left(1-\chi^{\prime}\right)\left(\theta+d d^{c} V_{\theta}\right)+\chi^{\prime}\left(\theta+d d^{c} \psi\right)+\chi^{\prime \prime}\left|d\left(\psi-V_{\theta}\right)\right|^{2}$ where $\chi^{\prime}$ and $\chi^{\prime \prime}$ are evaluated at $\psi-V_{\theta}$. Now we apply this to $\psi=1 / m \log |s|_{h_{0}^{m}}^{2}$.

For the integrability property, we use the following inequality for $x$ a real number (big enough): $x^{\alpha} \geqslant(n+1) \log x-C$ for some $C>0$ depending only on $\alpha$. Now we observe that $V_{\theta}+\chi\left(\psi-V_{\theta}\right) \leqslant \chi(\psi)$ : indeed, $\chi\left(\psi-V_{\theta}\right)-\chi(\psi) \leqslant \sup \chi^{\prime} \cdot\left(-V_{\theta}\right) \leqslant-V_{\theta}$, so that in our case, $u \leqslant\left(-\frac{1}{m} \log |s|_{h_{0}}^{2}\right)^{\alpha}$. If we apply the basic inequality stated above to $x=-\frac{1}{m} \log |s|_{h_{0}}^{2}$ which can be made big enough by multiplying $h_{0}$ by a big constant (this does not change the curvature), we get
$$e^{u} \leqslant C\left(-\frac{1}{m} \log |s|_{h_{0}}^{2}\right)^{-(n+1)}$$
As $D$ has snc support, and $|t|$ is bounded from above, we are left to check that the integral
$$\int_{D} \frac{d V}{\prod_{i \leqslant n}\left|z_{i}\right|^{2} \cdot \log ^{n+1}\left(\prod_{i \leqslant n}\left|z_{i}\right|^{2}\right)}$$
over the unit polydisc $D$ in $\mathbb{C}^{n}$ converges. But after a polar change of coordinate, we are led to estimate $\int_{[0,1]^{n}} \frac{d x_{1} \cdots d x_{n}}{\prod_{i \leqslant n} x_{i} \cdot \log ^{n+1}\left(\prod_{i \leqslant n} x_{i}^{2}\right)}$, which equals $\frac{1}{2^{n+1} n} \int_{[0,1]^{n-1}} \frac{d x_{1} \cdots d x_{n-1}}{\prod_{i \leqslant n-1} x_{i} \cdot \log ^{n}\left(\prod \prod_{i \leqslant n-1} x_{i}\right)}$. By induction, and using the Poincaré case, it concludes.

Finally, one has to check that $u \in \mathcal{E}^{1}(X, \theta)$. We compute the capacity $\operatorname{Cap}_{\theta}\left(u<V_{\theta}-t\right)$ for $t$ big. But $\left(u<V_{\theta}-t\right)=\left(\frac{1}{m} \log |s|_{h}^{2}<-t^{1 / \alpha}\right) \subset\left(\left(\frac{1}{m} \log |s|_{h_{0}}^{2}<-t^{1 / \alpha}\right)\right)$ and thus
$\operatorname{Cap}_{\theta}\left(u<V_{\theta}-t\right) \leqslant \frac{C}{t^{1 / \alpha}}$ because for every $\theta$-psh function $\psi$, one has $\operatorname{Cap}_{\theta}(\psi<-t) \leqslant \frac{C_{\psi}}{t}$ (this is an easy generalization of [GZ05, Proposition 2.6]). Therefore, if $\alpha<\frac{1}{n+1}$, one has
$$\int_{0}^{+\infty} t^{n} \operatorname{Cap}_{\theta}\left(u<V_{\theta}-t\right) d t<+\infty$$
which, using the characterization given in [BBGZ13, Lemma 2.9], ends the proof of the lemma. \(\square\)