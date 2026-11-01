---
retention_scope: session
part: 1
total_parts: 4
---

[Part 1/4 of: Families of singular Kähler–Einstein metrics]

---
source_file: Families_of_singular_Kähler_Einstein_metrics_7527d96faeef.pdf
converter: mathpix
format: mmd
---

\title{
FAMILIES OF SINGULAR KÄHLER-EINSTEIN METRICS \\ by
}

\author{
Eleonora Di Nezza, Vincent Guedj \& Henri Guenancia
}

\begin{abstract}
Refining Yau's and Kolodziej's techniques, we establish very precise uniform a priori estimates for degenerate complex Monge-Ampère equations on compact Kähler manifolds, that allow us to control the blow up of the solutions as the cohomology class and the complex structure both vary.

We apply these estimates to the study of various families of possibly singular Kähler varieties endowed with twisted Kähler-Einstein metrics, by analyzing the behavior of canonical densities, establishing uniform integrability properties, and developing the first steps of a pluripotential theory in families. This provides interesting information on the moduli space of stable varieties, extending works by Berman-Guenancia and Song, as well as on the behavior of singular Ricci flat metrics on (log) Calabi-Yau varieties, generalizing works by Rong-Ruan-Zhang, Gross-Tosatti-Zhang, Collins-Tosatti and Tosatti-Weinkove-Yang.
\end{abstract}

\section*{Contents}
Introduction ..... 1
1. Chasing the constants ..... 8
2. Uniform integrability ..... 14
3. Normalization in families ..... 26
4. Densities along a log canonical map ..... 37
5. Negative curvature ..... 43
6. Log Calabi-Yau families ..... 51
References ..... 62

\section*{Introduction}

Let $p: X \rightarrow Y$ be a proper, surjective holomorphic map with connected fibers between Kähler varieties. It is a central question in complex geometry to relate the geometry of $X$ to the one of $Y$ and the fibers $X_{y}$ of $p$. An important instance of such a situation

\footnotetext{
2000 Mathematics Subject Classification. - 14D06, 32Q20, 32U05, 32W20.
Key words and phrases. - Singular Kähler-Einstein metrics, Families of complex spaces, Stable families, Log Calabi-Yau manifolds.
}
is when one can endow $X_{y}$ with a Kähler-Einstein metric and study the geometry of $X$ induced by the properties of the resulting family of metrics. This is the main theme of this article.

Einstein metrics are a central object of study in differential geometry. A Kähler-Einstein metric on a complex manifold is a Kähler metric whose Ricci tensor is proportional to the metric tensor. This notion still makes sense on midly singular varieties as was observed in [EGZ09, section 7]. The solution of the (singular) Calabi Conjecture [Yau78, EGZ09] provides a very powerful existence theorem for Kähler-Einstein metrics with negative or zero Ricci curvature. It is important to study the ways in which these canonical metrics behave when they are moving in families. In this paper we consider the case when both the complex structure and the Kähler class vary and we try and understand how the corresponding metrics can degenerate.

Constructing singular Kähler-Einstein metrics on a midly singular variety $V$ boils down to solving degenerate complex Monge-Ampère equations of the form
$$(\omega+i \partial \bar{\partial} \varphi)^{n}=f e^{\lambda \varphi} d V_{X},$$
where
\begin{itemize}
\item[-] $\pi: X \rightarrow V$ is a resolution of singularities, $d V_{X}$ is a volume form on $X$,
\item[-] $\omega=\pi^{*} \omega_{V}$ is the pull-back of a Kähler form on $V$,
\item[-] the sign of $\lambda \in \mathbb{R}$ depends on that of $c_{1}(V)$,
\item[-] $f \in L^{p}(X)$ with $p>1$ if the singularities of $V$ are mild (klt singularities),
\end{itemize}
and $\varphi$ is the unknown. The latter should be $\omega$-plurisubharmonic ( $\omega$-psh for short), i.e. it is locally the sum of a psh and a smooth function, and satisfies $\omega+i \partial \bar{\partial} \varphi \geq 0$ in the weak sense of currents. We let $P S H(X, \omega)$ denote the set of all such functions.

The uniform estimate. - A crucial step in order to prove the existence of a solution to the above equation is to establish a uniform a priori estimate. In order to understand the behavior of the solution $\varphi$ as the cohomology class $\left\{\omega_{V}\right\}$ and the complex structure of $V$ vary, we revisit the proof by Yau [Yau78], as well as its recent generalizations [Koł98, EGZ09], and establish the following (see Theorem 1.1):

Theorem A. - Let $X$ be a compact Kähler manifold of complex dimension $n \in \mathbb{N}^{*}$ and let $\omega$ be a semi-positive form such that $V:=\int_{X} \omega^{n}>0$. Let $v$ and $\mu=f \nu$ be probability measures, with $0 \leqslant f \in L^{p}(v)$ for some $p>1$. Assume the following assumptions are satisfied:
(H1) there exists $\alpha>0$ and $A_{\alpha}>0$ such that for all $\psi \in \operatorname{PSH}(X, \omega)$,
$$\int_{X} e^{-\alpha\left(\psi-\sup _{X} \psi\right)} d v \leqslant A_{\alpha} ;$$
(H2) there exists $C>0$ such that $\left(\int_{X}|f|^{p} d v\right)^{1 / p} \leqslant C$.
Let $\varphi$ be the unique $\omega$-psh solution $\varphi$ to the complex Monge-Ampère equation
$$V^{-1}(\omega+i \partial \bar{\partial} \varphi)^{n}=\mu,$$
normalized by $\sup _{X} \varphi=0$. Then $-M \leqslant \varphi \leqslant 0$ where
$$M=1+C^{1 / n} A_{\alpha}^{1 / n q} e^{\alpha / n q} b_{n}\left[5+e \alpha^{-1} C(q!)^{1 / q} A_{\alpha}^{1 / q}\right],$$
$1 / p+1 / q=1$ and $b_{n}$ is a constant such that $\exp (-1 / x) \leqslant b_{n}^{n} x^{2 n}$ for all $x>0$.

Remark 0.1. — Let us observe that the condition (H1) in Theorem A above guarantees that the measure $v$ does not charge pluripolar sets, since any such set can be included in the polar locus of a global $\omega$-psh function by [GZ05, Thm. 7.2]. The existence (and uniqueness) of the solution $\varphi$ in Theorem A follows from [BEGZ10, Thm. A].

We also establish slightly more general versions of Theorem A valid for less regular densities (Theorem 1.5) or big cohomology classes (Theorem 1.9). We then move on to checking hypotheses (H1) and (H2) in various geometrical contexts.
- Hypothesis (H1). If $\pi: \mathcal{X} \rightarrow \mathbb{D}$ is a projective family whose fibers $X_{t}=\pi^{-1}(t)$ have degree $d$ with respect to a given projective embedding $\mathcal{X} \subset \mathbb{P}^{N} \times \mathbb{D}$, and $\omega=\omega_{t}$ is the restriction of the Fubini-Study metric, we observe in Proposition 2.5 that
$$V=\int_{X_{t}} \omega_{t}^{n}=\int_{\mathbb{P}^{N}} \omega_{F S}^{n} \wedge\left[X_{t}\right]=d$$
is independent of $t$ and the following uniform integrability holds.
Proposition B. - For for all $\psi \in \operatorname{PSH}\left(X_{t}, \omega_{t}\right)$,
$$\int_{X_{t}} e^{-\frac{1}{n d}\left(\psi-\sup _{X_{t}} \psi\right)} \omega_{t}^{n} \leqslant(4 n)^{n} \cdot d \cdot \exp \left\{-\frac{1}{n d} \int_{X_{t}}\left(\psi-\sup _{X_{t}} \psi\right) \omega_{t}^{n}\right\} .$$

The hypothesis (H1) is thus satisfied in this projective setting, with $\alpha=1 / n d$, as soon as we can uniformly control the $L^{1}$-norm of $\psi$. We take care of this in Section 3. This non-trivial control requires the varieties $X_{t}$ to be irreducible (see Example 3.5).

Bypassing the projectivity assumption, we show that (H1) is actually satisfied for many Kähler families of interest, by generalizing a uniform integrability result of Skoda-Zeriahi [Sko72, Zer01] (see Theorem 2.9). This is the content of Theorem 3.4.
- Hypothesis (H2). We analyze (H2) in section 4. We show that, up to shrinking the base, it is always satisfied if the $f_{t}$ 's are canonical densities associated to a proper, holomorphic surjective map $\pi: \mathcal{X} \rightarrow \mathbb{D}$ from a normal, Q-Gorenstein Kähler space $\mathcal{X}$ to the unit disk such that the central fiber has only canonical singularities, cf Lemma 4.4 and its application to families of Calabi-Yau varieties, Theorem F.

While previous works tend to use sophisticated arguments from Variations of Hodge Structures (see e.g. the Appendix by Gross in [RZ11a]), we use here direct elementary computations in adapted coordinates, in the spirit of [EGZ09, section 6].

In the context of families of varieties with negative curvature though, it is essential to allow worse singularities than the ones described above, cf Setting 4.1 for the precise context. The trade-off is that the canonical densities do not satisfy condition (H2) anymore, reflecting the fact that the local potentials of the Kähler-Einstein metrics at stake need not be bounded anymore. This legitimizes the introduction of a weaker condition (H2') (see Theorem 1.5 and Lemma 4.6). This allows us to derive an almost optimal control of the potentials of Kähler-Einstein metrics along a stable family, cf Theorem E below.

Let us end this paragraph by emphasizing that our approach enables us to work with singular families (i.e. families where the generic fiber is singular, cf Theorems E and F) as opposed to all previously known results on that topic, requiring to approximate a singular variety by smooth ones using either a smoothing or a crepant resolution.

We now describe more precisely four independent geometric settings to which we apply the uniform estimate provided by Theorem A.

Families of manifolds of general type. - Let $\mathcal{X}$ be an irreducible and reduced complex space endowed with a Kähler form $\omega$ and a proper, holomorphic map $\pi: \mathcal{X} \rightarrow \mathbb{D}$. We assume that for each $t \in \mathbb{D}$, the (schematic) fiber $X_{t}$ is a $n$-dimensional Kähler manifold $X_{t}$ of general type, i.e. such that its canonical bundle $K_{X_{t}}$ is big. In particular, $\mathcal{X}$ is automatically non-singular and the map $\pi$ is smooth.

We fix $\Theta$ a closed differential (1,1)-form on $\mathcal{X}$ which represents $c_{1}\left(K_{\mathcal{X}} / \mathbb{D}\right)$ and set $\theta_{t}=\Theta_{\mid X_{t}}$.

It follows from [BEGZ10], a generalization of the Aubin-Yau theorem [Aub78, Yau78], that there exists a unique Kähler-Einstein current on $X_{t}$. This is a positive closed current $T_{t}$ in $c_{1}\left(K_{X_{t}}\right)$ which is a smooth Kähler form in the ample locus $\operatorname{Amp}\left(K_{X_{t}}\right)$, where it satisfies the Kähler-Einstein equation
$$\operatorname{Ric}\left(T_{t}\right)=-T_{t} .$$

It can be written $T_{t}=\theta_{t}+d d^{c} \varphi_{t}$, where $\varphi_{t}$ is the unique $\theta_{t}$-psh function with minimal singularities that satisfies the complex Monge-Ampère equation
$$\left(\theta_{t}+d d^{c} \varphi_{t}\right)^{n}=e^{\varphi_{t}+h_{t}} \omega_{t}^{n} \quad \text { on } \operatorname{Amp}\left(K_{X_{t}}\right),$$
where $h_{t}$ is such that $\operatorname{Ric}\left(\omega_{t}\right)-d d^{c} h_{t}=-\theta_{t}$ and $\int_{X_{t}} e^{h_{t}} \omega_{t}^{n}=\operatorname{vol}\left(K_{X_{t}}\right)$. For $x \in \mathcal{X}$, set
$$\phi(x):=\varphi_{\pi(x)}(x)$$
and consider
$$V_{\Theta}=\sup \{u \in \operatorname{PSH}(\mathcal{X}, \Theta) ; u \leqslant 0\} .$$
We prove that conditions (H1) and (H2) are satisfied in this setting. It then follows from Theorem A and the plurisubharmonic variation of the $T_{t}$ 's ([CGP21, Thm. A]) that $\phi-V_{\Theta}$ is uniformly bounded on compact subsets of $\mathcal{X}$, cf Theorem 5.5 and Remark 5.6:

Theorem C. - Let $\pi: \mathcal{X} \rightarrow \mathbb{D}$ be a smooth Kähler family of manifolds of general type, let $\Theta \in c_{1}\left(K_{\mathcal{X} / \mathbb{D}}\right)$ be a smooth representative and let $\phi$ be the Kähler-Einstein potential as in (0.1). Given any compact subset $\mathcal{K} \Subset \mathcal{X}$, there exists a constant $M_{\mathcal{K}}$ such that the following inequality
$$-M_{\mathcal{K}} \leqslant \phi-V_{\Theta} \leqslant M_{\mathcal{K}}$$
holds on $\mathcal{K}$, where $V_{\Theta}$ is defined by (0.2).

The same results can be proved if the family $\pi: \mathcal{X} \rightarrow \mathbb{D}$ is replaced by a smooth family $\pi:(\mathcal{X}, B) \rightarrow \mathbb{D}$ of pairs $\left(X_{t}, B_{t}\right)$ of log general type, i.e. such that $\left(X_{t}, B_{t}\right)$ is klt and $K_{X_{t}}+B_{t}$ is big for all $t \in \mathbb{D}$.

Stable families. - A stable variety is a projective variety $X$ such that $X$ has semi-log-canonical singularities and the Q-line bundle $K_{X}$ is ample. We refer to [Kov13, Kol] for a detailed account of these varieties and their connection to moduli theory.

In [BG14], it was proved that a stable variety admits a unique Kähler-Einstein metric $\omega$, i.e. a smooth Kähler metric on $X_{\text {reg }}$ such that, if $n=\operatorname{dim}_{\mathbb{C}} X$,
$$\operatorname{Ric}(\omega)=-\omega \quad \text { and } \quad \int_{X_{\mathrm{reg}}} \omega^{n}=\left(K_{X}^{n}\right) .$$

The metric $\omega$ extends canonically across $X_{\text {sing }}$ to a closed, positive current in the class $c_{1}\left(K_{X}\right)$. It is desirable to understand the singularities of $\omega$ near $X_{\text {sing }}$. In [GW16, Thm. B], it is proved that $\omega$ has cusp singularities near the double crossings of $X$. Moreover, it is proved in [Son17] that the potential $\varphi$ of $\omega$ with respect to a given Kähler form $\omega_{X} \in c_{1}\left(K_{X}\right)$, i.e. $\omega=\omega_{X}+d d^{c} \varphi$, is locally bounded on the klt locus of $X$. In order to refine the latter assertion, let us introduce the following invariant.

Given a log resolution of singularities $f: Y \rightarrow X$ write $K_{Y}=f^{*} K_{X}+\sum_{i \in I} a_{i} E_{i}$ where $E=\sum_{i \in I} E_{i}$ is a divisor with simple normal crossings whose components are either exceptional or sit above the divisorial components of $\operatorname{Sing}(X)$. We set $J:=\left\{i \in I ; a_{i}=\right.$ $-1\}$ which we assume to be non-empty and define the non-klt locus of $X$ by $\operatorname{Nklt}(X)=$ $\cup_{j \in J} f\left(E_{j}\right)$; it is independent of $f$. Given $K \subset I$, we set $E_{K}=\cap_{i \in K} E_{i}$ and introduce the invariants
$$v(f):=\max \left\{|K| ; K \subset J, E_{K} \neq \varnothing\right\}, \quad \text { and } \quad v:=\inf _{f}\{v(f)\}$$
where the infimum is taken over all the log resolutions of $X$. We have $v \in\{1, \ldots, n\}$.
We establish the following (cf. Proposition 5.9).
Proposition D. - For any $\varepsilon>0$, there is a constant $C_{\varepsilon}$ such that
$$C_{1} \geqslant \varphi \geqslant-(n+v+\varepsilon) \log (-\log |s|)-C_{\varepsilon}$$
where $(s=0)$ is any reduced divisor containing the non-klt locus of $X$ and $v$ is as in (0.3).
This estimate is almost optimal as illustrated by the Baily-Borel-Satake compactification of a ball quotient or a Hilbert modular surface, cf Examples 5.11-5.12.

A slight refinement of Theorem A (cf. Theorem 1.5) allows us to establish a uniform family version of the estimate (0.4). In order to state it, let $\mathcal{X}$ be a normal Kähler space and let $\pi: \mathcal{X} \rightarrow \mathbb{D}$ be a proper, surjective, holomorphic map such that each fiber $X_{t}$ has slc singularities and $K_{\mathcal{X} / \mathbb{D}}$ is an ample Q-line bundle. If $\omega_{\mathcal{X}} \in c_{1}\left(K_{\mathcal{X} / \mathbb{D}}\right)$ is a relative Kähler form and $\omega_{X_{t}}:=\left.\omega_{\mathcal{X}}\right|_{X_{t}}$, then the Kähler-Einstein metric of $X_{t}$ can be written as $\omega_{X_{t}}+d d^{c} \varphi_{t}$ where $\varphi_{t}$ is uniquely determined by the equation (5.8) from section 5.

Given a semistable model $f: \mathcal{Y} \rightarrow \mathcal{X}$ write $K_{\mathcal{Y}}+Y_{0}=f^{*}\left(K_{\mathcal{X}}+X_{0}\right)+\sum_{i \in I} a_{i} E_{i}$ where $Y_{0}$ is the strict transform of $X_{0}$. We set $J:=\left\{i \in I ; a_{i}=-1\right\}$ which we assume to be non-empty and define the non-klt locus of $\left(\mathcal{X}, X_{0}\right)$ by
$$\operatorname{Nklt}\left(\mathcal{X}, X_{0}\right)=\cup_{j \in J} f\left(E_{j}\right) ;$$
it is independent of $f$. Given $K \subset I$, we set $E_{K}=\cap_{i \in K} E_{i}$ and introduce the invariants
$$v(f):=\max \left\{|K| ; K \subset J, E_{K} \neq \varnothing\right\}, \quad \text { and } \quad v:=\inf _{f}\{v(f)\}$$
where the infimum is taken over all the semistable models $f: \mathcal{Y} \rightarrow \mathcal{X}$. We have $v \in\{1, \ldots, n\}$.

The behavior of $\varphi_{t}$ is then described by the following (see Theorem 5.13)
Theorem E. - Let $\mathcal{X}$ be a normal Kähler space and let $\pi: \mathcal{X} \rightarrow \mathbb{D}$ be a proper, surjective, holomorphic map such that
\begin{itemize}
\item[-] Each schematic fiber $X_{t}$ has semi-log-canonical singularities.
\item[-] $K_{\mathcal{X} / \mathbb{D}}$ is an ample Q-line bundle.
\end{itemize}
In particular, $X_{t}$ is a stable variety for any $t \in \mathbb{D}$. Assume additionally that the central fiber $X_{0}$ is irreducible.

Let $\omega_{X_{t}}+d d^{c} \varphi_{t}$ be the Kähler-Einstein metric of $X_{t}$ and let $D=(s=0) \subset \mathcal{X}$ be a divisor which contains $\operatorname{Nklt}\left(\mathcal{X}, X_{0}\right)$, cf (0.5). Fix some smooth hermitian metric | | on $\mathcal{O}_{\mathcal{X}}(D)$. Up to shrinking $\mathbb{D}$, then for any $\varepsilon>0$, there exists $C_{\varepsilon}>0$ such that the inequality
$$C_{1} \geqslant \varphi_{t} \geqslant-(n+v+\varepsilon) \log (-\log |s|)-C_{\varepsilon}$$
holds on $X_{t}$ for any $t \in \mathbb{D}$, where $v$ is as in (0.6).
Let us finally mention the very recent results of Song, Sturm and Wang [SSW20, Proposition 3.1] where similar bounds are derived in the context of smoothings of stable varieties over higher dimensional bases, with application towards Weil-Petersson geometry of the KSBA compactification of canonically polarized manifolds.

Families of Q-Calabi-Yau varieties. - A Q-Calabi-Yau variety is a compact, normal Kähler space $X$ with canonical singularities such that the Q- line bundle $K_{X}$ is torsion. Up to taking a finite, quasi-étale cover referred to as the index 1 cover (cf e.g. [KM98, Def. 5.19]), one can assume that $K_{X} \sim_{\mathbb{Z}} \mathcal{O}_{X}$. Given any Kähler class $\alpha$ on $X$, it follows from [EGZ09] and [Pău08] that there exists a unique singular Ricci flat Kähler metric $\omega_{\mathrm{KE}} \in \alpha$, i.e. a closed, positive current $\omega_{\mathrm{KE}} \in \alpha$ with globally bounded potentials inducing a smooth, Ricci-flat Kähler metric on $X_{\text {reg }}$.

Now, we can consider families of such varieties and ask how the bound on the potentials vary. This is the content of the following (see Theorem 6.1 and Remark 6.2)

Theorem F. - Let $\mathcal{X}$ be a normal, Q-Gorenstein Kähler space and let $\pi: \mathcal{X} \rightarrow \mathbb{D}$ be a proper, surjective, holomorphic map. Let $\alpha$ be a relative Kähler cohomology class on $\mathcal{X}$ represented by a relative Kähler form $\omega$. Assume additionaly that
\begin{itemize}
\item[-] The relative canonical bundle $K_{\mathcal{X} / \mathbb{D}}$ is trivial.
\item[-] The central fiber $X_{0}$ has canonical singularities.
\item[-] Assumption 3.2 is satisfied.
\end{itemize}
Up to shrinking D, each fiber $X_{t}$ is a Q-Calabi-Yau variety. Let $\omega_{\mathrm{KE}, t}=\omega_{t}+d d^{c} \varphi_{t}$ be the singular Ricci-flat Kähler metric in $\alpha_{t}$, normalized by $\int_{X_{t}} \varphi_{t} \omega_{t}^{n}=0$. Then, given any compact subset $K \Subset \mathbb{D}$, there exists $C=C(K)>0$ such that one has
$$\operatorname{osc}_{X_{t}} \varphi_{t} \leqslant C$$
for any $t \in K$, where $\operatorname{osc}_{X_{t}}\left(\varphi_{t}\right)=\sup _{X_{t}} \varphi_{t}-\inf _{X_{t}} \varphi_{t}$.

In the case of a projective smoothing (i.e. when $\mathcal{X}$ admits a $\pi$-ample line bundle and $X_{t}$ is smooth for $t \neq 0$ ), the result above has been obtained previously by Rong-Zhang [RZ11a] by using Moser iteration process.

Log Calabi-Yau families. - Let $X$ be a compact Kähler manifold and let $B=\sum b_{i} B_{i}$ be an effective $\mathbb{R}$-divisor such that the pair $(X, B)$ has klt singularities and $c_{1}\left(K_{X}+B\right)=0$.

It follows from [Yau78, EGZ09, BEGZ10] that one can find a unique Ricci flat metric in each Kähler class $\alpha_{t}$. A basic problem is to understand the asymptotic behavior of these metrics as $\alpha_{t}$ approaches the boundary of the Kähler cone. Despite motivations coming from mirror symmetry, not much is known when the norm of $\alpha_{t}$ converges to $+\infty$ (this case is expected to be the mirror of a large complex structure limit, see [KS01]). We thus only consider the case when $\alpha_{t} \rightarrow \alpha_{0} \in \partial \mathcal{K}_{X}$.

The non-collapsing case ( $\operatorname{vol}\left(\alpha_{0}\right)>0$ ) can be easily understood by using Theorem A (see Theorem 6.5). We describe here a particular instance of the more delicate collapsing case $\operatorname{vol}\left(\alpha_{0}\right)=0$. Let $f: X \rightarrow Z$ be a surjective holomorphic map with connected fibers, where $Z$ is a normal Kähler space. Let $\omega_{X}$ (resp. $\omega_{Z}$ ) be a Kähler form on $X$ (resp. $Z$ ). Set $\omega_{t}:=f^{*} \omega_{Z}+t \omega_{X}$. There exists a unique singular Ricci-flat current $\omega_{\varphi_{t}}:=\omega_{t}+d d^{c} \varphi_{t}$ in $\left\{f^{*} \omega_{Z}+t \omega_{X}\right\}$ for $t>0$, where $\int_{X} \varphi_{t} \omega_{X}^{n}=0$. It satisfies
$$\omega_{\varphi_{t}}^{n}=V_{t} \cdot \mu_{(X, B)}, \quad \text { where } \quad \mu_{(X, B)}=(s \wedge \bar{s})^{\frac{1}{m}} e^{-\phi_{B}} .$$
Here, $s \in H^{0}\left(X, m\left(K_{X}+B\right)\right.$ ) is any non-zero section (for some $m \geqslant 1$ ) and $\phi_{B}$ is the unique singular psh weight on $\mathcal{O}_{X}(B)$ solving $d d^{c} \phi_{B}=[B]$ and normalized by
$$\int_{X}(s \wedge \bar{s})^{\frac{1}{m}} e^{-\phi_{B}}=1 .$$

The probability measure $f_{*} \mu_{(X, B)}$ has $L^{1+\varepsilon}$-density with respect to $\omega_{Z}^{m}$ thanks to [EGZ18, Lem. 2.3]. It follows therefore from [EGZ09] that there exists a unique current $\omega_{\infty} \in\left\{\omega_{Z}\right\}$ solution of the Monge-Ampère equation
$$\omega_{\infty}^{m}=f_{*} \mu_{(X, B)} .$$
In the case where $X$ is smooth, $B=0$ and $c_{1}(X)=0$, the Ricci curvature of $\omega_{\infty}$ coincides with the Weil-Petersson form of the fibration $f$ of Calabi-Yau manifolds.

Understanding the asymptotic behavior of the $\omega_{\varphi_{t}}{ }^{\prime}$ s as $t \rightarrow 0$ is an important problem with a long history, we refer the reader to the thorough survey [Tos20] for references. We prove here the following:

Theorem G. - Let $(X, B)$ be a log smooth klt pair such that $c_{1}\left(K_{X}+B\right)=0$ and such that $X$ admits a fibration $f: X \rightarrow Z$. With the notations above, the conic Ricci-flat metrics $\omega_{\varphi_{t}} \in\left\{f^{*} \omega_{Z}+t \omega_{X}\right\}$ converge to $f^{*} \omega_{\infty}$ as currents on $X$ when $t$ goes to 0 .

When $B=0$ is empty, it has been shown in [Tos10, GTZ13, TWY18, HT20] that he metrics $\omega_{\varphi_{t}}$ converge to $f^{*} \omega_{\infty}$ in the $\mathcal{C}^{\alpha}$-sense on compact subsets of $X \backslash S_{X}$ for some $\alpha>0$, where $S_{X}=f^{-1}\left(S_{Z}\right)$ and $S_{Z}$ denotes the smallest proper analytic subset $\Sigma \subset Z$ such that $\Sigma$ contains the singular locus $Z_{\text {sing }}$ of $Z$ and the map $f$ is smooth on $f^{-1}(Z \backslash \Sigma)$.

The proof of Theorem G follows the strategy developed by the above papers with several twists that notably require the extensive use of Theorem A and conical metrics.

Acknowledgements. - We thank S.Boucksom, M.Păun, J.Song and A.Zeriahi for several interesting discussions. We are grateful to the anonymous referees for a remarkably careful reading, for suggesting many improvements as well as for pointing out a gap in §3 of an earlier version. Finally, we thank Rui Tang for pointing out an error in the published version. The authors are partially supported by the ANR project GRACK.

\section*{1. Chasing the constants}

Our goal in this section is to establish the following a priori estimate which is a refinement of the main result of Kolodziej [Koł98] (see also [EGZ09, EGZ08, DP10]):

Theorem 1.1. - Let $\left(X, \omega_{X}\right)$ be a compact Kähler manifold of complex dimension $n \in \mathbb{N}^{*}$ and let $\omega$ be a semi-positive form which is big, i.e. such that
$$V:=\operatorname{Vol}_{\omega}(X)=\int_{X} \omega^{n}>0 .$$
Let $v$ and $\mu=f v$ be probability measures, with $0 \leqslant f \in L^{p}(v)$ for some $p>1$. Assume the following two assumptions are satisfied:
\begin{itemize}
\item[(H1)] there exists $\alpha>0$ and $A_{\alpha}>0$ such that for all $\psi \in \operatorname{PSH}(X, \omega)$,
$$\int_{X} e^{-\alpha\left(\psi-\sup _{X} \psi\right)} d v \leqslant A_{\alpha} ;$$
\end{itemize}
(H2) there exists $C>0$ such that $\left(\int_{X}|f|^{p} d v\right)^{1 / p} \leqslant C$.
Let $\varphi$ be the unique $\omega$-psh solution $\varphi$ to the complex Monge-Ampère equation
$$V^{-1}\left(\omega+d d^{c} \varphi\right)^{n}=\mu,$$
normalized by $\sup _{X} \varphi=0$. Then $-M \leqslant \varphi \leqslant 0$ where
$$M=1+C^{1 / n} A_{\alpha}^{1 / n q} e^{\alpha / n q} b_{n}\left[5+e \alpha^{-1} C(q!)^{1 / q} A_{\alpha}^{1 / q}\right],$$
$1 / p+1 / q=1$ and $b_{n}$ is a constant such that $\exp (-1 / x) \leqslant b_{n}^{n} x^{2 n}$ for all $x>0$.
Here $d=\partial+\bar{\partial}$ and $d^{c}=\frac{i}{2}(\partial-\bar{\partial})$ so that $d d^{c}=i \partial \bar{\partial}$. Recall that a function $\varphi: X \rightarrow$ $\mathbb{R} \cup\{-\infty\}$ is $\omega$-plurisubharmonic ( $\omega$-psh for short) if it is locally given as the sum of a smooth and a psh function, and such that $\omega+d d^{c} \varphi \geqslant 0$ in the weak sense of currents. We let $\operatorname{PSH}(X, \omega)$ denote the set of all $\omega$-psh functions.

The non-pluripolar Monge-Ampère measure of arbitrary $\omega$-psh functions has been defined in [BEGZ10]. It follows from assumption (H1) that the measure $\mu$ does not charge pluripolar sets, since the latter can be defined by $\omega$-psh functions (as follows easily from [GZ05, Thm. 7.2] since a big class contains a Kähler current). The existence of a unique normalized $\omega$-psh solution to $V^{-1}\left(\omega+d d^{c} \varphi\right)^{n}=\mu$ follows from [BEGZ10, Theorem A] (the case of Kähler forms had been earlier treated in [GZ07, Din09]).

We will use this result to obtain uniform a priori estimates on normalized solutions $\varphi_{t}$ to families of complex Monge-Ampère equations
$$V_{t}^{-1}\left(\omega_{t}+d d^{c} \varphi_{t}\right)^{n}=\mu_{t},$$
when the hypotheses (H1,H2) are satisfied, i.e. the constants $1 / \alpha_{t}, A_{\alpha_{t}}, q_{t}, C_{t}$ in the theorem are actually bounded from above by uniform constants $1 / \alpha, A, q, C$ independent of $t$. Here $q$ denotes the conjugate exponent of $p>1,1 / p+1 / q=1$. The assumption on this exponent is thus that $p>1$ stays bounded away from 1 .

The reader should keep in mind that assumption (H1) is the strongest of all. In some applications one can assume $f \equiv 1$ hence (H2) is trivially satisfied.

We are going to eventually obtain a version of Theorem 1.1 that applies to big cohomology classes, extending [BEGZ10, Theorem B]. The proof is almost identical but explaining the statement requires to introduce various notions and technical notations, so we first treat the case of semi-positive classes and postpone this to section 1.4.
1.1. Preliminaries on capacities. - Let $K \subset X$ be a Borel set and consider
$$V_{K, \omega}:=(\sup \{\psi \mid \psi \in \operatorname{PSH}(X, \omega) \text { and } \psi \leqslant 0 \text { on } K\})^{*},$$
where * denotes the upper semi-continuous regularization.
The Alexander-Taylor capacity is the following:
$$T_{\omega}(K):=\exp \left(-\sup _{X} V_{K, \omega}\right) .$$
It is shown in [GZ17, Lem. 9.17] that If $K$ is pluripolar then $V_{K, \omega} \equiv+\infty$ and $T_{\omega}(K)=0$. When $K$ is not pluripolar then
\begin{itemize}
\item[-] $0 \leqslant V_{K . \omega} \in \operatorname{PSH}(X, \omega)$ and $V_{K, \omega}=0$ on $K$ off a pluripolar set;
\item[-] the Monge-Ampère measure $\mathrm{MA}\left(V_{K, \omega}\right)$ is concentrated on $E$.
\end{itemize}
We denote here and in the sequel by
$$\operatorname{MA}(u)=\frac{1}{V}\left(\omega+d d^{c} u\right)^{n}$$
the normalized Monge-Ampère measure of a $\omega$-psh function $u$, where $V=\int_{X} \omega^{n}=$ $\{\omega\}^{n}$ is the volume of the cohomology class $\{\omega\}$. It is defined for any $\omega$-psh function $u$, cf. e.g. [GZ07, § 1.1]. For a Borel set $K \subset X$, the Monge-Ampère capacity is
$$\operatorname{Cap}_{\omega}(K):=\sup \left\{\int_{K} \operatorname{MA}(u) ; u \in \operatorname{PSH}(X, \omega) \text { and } 0 \leqslant u \leqslant 1\right\} .$$
This capacity also characterizes pluripolar sets, i.e.
$$\operatorname{Cap}_{\omega}^{*}(P)=0 \Longleftrightarrow P \text { is pluripolar. }$$
Here Cap ${ }_{\omega}^{*}$ is the outer capacity associated to Cap ${ }_{\omega}$ defined for any set $E \subset X$ as
$$\operatorname{Cap}_{\omega}^{*}(E):=\inf \left\{\operatorname{Cap}_{\omega}(G) ; G \text { open, } E \subset G\right\} .$$
Moreover, if $K \subset X$ is a compact set than $\operatorname{Cap}_{\omega}^{*}(K)=\operatorname{Cap}_{\omega}(K)$.
The Monge-Ampère and the Alexander-Taylor capacities compare as follows:

Lemma 1.2. -
$$T_{\omega}(K) \leqslant \exp \left[1-\frac{1}{\operatorname{Cap}_{\omega}(K)^{1 / n}}\right] .$$

We refer the reader to [GZ05, Proposition 7.1] for a proof which also provides a reverse inequality that is not needed in the sequel.
1.2. Proof of Theorem 1.1. -
1.2.1. Domination by capacity. - It follows from Hölder inequality and (H2) that
$$\mu \leqslant C v^{1 / q},$$
where $q$ is the conjugate exponent, $1 / p+1 / q=1$.
Let $K \subset X$ be a non pluripolar Borel set. Recall that $V_{K, \omega}(x)=0$ for $v$-almost every point $x \in K$. The hypothesis (H1) therefore implies that
$$v(K) \leqslant \int_{X} e^{-\alpha V_{K, \omega}} d v \leqslant A_{\alpha} T_{\omega}(K)^{\alpha}$$
Combining previous information we obtain
$$\mu(K) \leqslant C A_{\alpha}^{1 / q} e^{\alpha / q} \exp \left[-\frac{\alpha / q}{\operatorname{Cap}_{\omega}(K)^{1 / n}}\right] \leqslant D \operatorname{Cap}_{\omega}(K)^{2},$$
where
$$D=b_{n}^{n} C A_{\alpha}^{1 / q} e^{\alpha / q},$$
with $b_{n}$ a numerical constant such that $\exp (-1 / x) \leqslant b_{n}^{n} x^{2 n}$ for all $x>0$.
We now need to relate the Monge-Ampère capacity of the sublevel sets of a $\omega$-psh function to the Monge-Ampère measure of similar sublevel sets:

Lemma 1.3. - Let $\varphi$ be a bounded $\omega$-psh function. For all $s>0$ and $0<\delta<1$,
$$\delta^{n} \operatorname{Cap}_{\omega}(\{\varphi<-s-\delta\}) \leqslant \operatorname{MA}(\varphi)(\{\varphi<-s\})$$

We refer to [EGZ09, Lemma 2.2] for a proof.
1.2.2. Bounding the solution from below. - Under our assumptions (H1,H2), it follows from general arguments that there is a unique bounded $\omega$-psh solution $\varphi$ of $\operatorname{MA}(\varphi)=\mu$ normalized by $\sup _{X} \varphi=0$, cf Remark 0.1. The non-expert reader could even think that $\varphi$ is smooth: the point here is to establish a uniform a priori bound from below.

We let $f: \mathbb{R}^{+} \rightarrow \mathbb{R}^{+}$denote the function defined by
$$f(s):=-\frac{1}{n} \log \operatorname{Cap}_{\omega}(\{\varphi<-s\})$$
Observe that $f$ is non decreasing and such that $f(+\infty)=+\infty$. It follows from our previous estimates that for all $s>0$ and $0<\delta<1$,
$$f(s+\delta) \geqslant 2 f(s)+\log \delta-\frac{\log D}{n} .$$
Our next lemma guarantees that such a function reaches $+\infty$ in finite time:
Lemma 1.4. - $f(s)=+\infty$ for all $s \geqslant 5 D^{1 / n}+s_{0}$, where
$$s_{0}=\inf \left\{s>0 \mid e D^{1 / n} \operatorname{Cap}_{\omega}(\{\varphi<-s\})<1\right\} .$$

Proof. - We define a sequence $\left(s_{j}\right)$ of positive reals by induction as follows,
$$s_{j+1}=s_{j}+\delta_{j} \quad \text { with } \quad \delta_{j}=e D^{1 / n} \exp \left(-f\left(s_{j}\right)\right) .$$

We fix $s_{0}$ large enough (as in the statement of the Lemma) so that $\delta_{0}<1$. It is straightforward to check, by induction, that the sequence $\left(s_{j}\right)$ is increasing, while $\left(\delta_{j}\right)$ is decreasing. Thus $0<\delta_{j}<1$ and
$$f\left(s_{j+1}\right) \geqslant f\left(s_{j}\right)+1 \text {, hence } f\left(s_{j}\right) \geqslant j \text {. }$$

We infer $\delta_{j} \leqslant e D^{1 / n} \exp (-j)$ and
$$s_{\infty}=s_{0}+\sum_{j \geqslant 0}\left(s_{j+1}-s_{j}\right) \leqslant s_{0}+\sum_{j \geqslant 0} e D^{1 / n} \exp (-j) \leqslant s_{0}+5 D^{1 / n} .$$ \(\square\)

It remains to obtain a uniform bound on $s_{0}$. It follows from Chebyshev inequality and Lemma 1.3 (used with $\delta=1$ ) that for all $s>0$,
$$\operatorname{Cap}_{\omega}(\{\varphi<-s-1\}) \leqslant \frac{1}{s} \int_{X}(-\varphi) d \mu$$
since $\operatorname{MA}(\varphi)=\mu$. Hölder inequality and (H2) yield
$$\int_{X}(-\varphi) d \mu \leqslant C\left(\int_{X}(-\varphi)^{q} d v\right)^{1 / q} .$$
Observe that for all $t \geqslant 0$,
$$t^{q} \leqslant \frac{q!}{\alpha^{q}} \exp (\alpha t)$$
and use (H1) to conclude that
$$\operatorname{Cap}_{\omega}(\{\varphi<-s-1\}) \leqslant \frac{C(q!)^{1 / q} A_{\alpha}^{1 / q}}{\alpha s} .$$
Thus
$$s_{0}=1+e D^{1 / n} \frac{C(q!)^{1 / q} A_{\alpha}^{1 / q}}{\alpha}$$
is a convenient choice. This yields the desired a priori estimate and concludes the proof.
1.3. More general densities. - The setting of Theorem 1.1 is the most commonly used in geometric applications, as it allows e.g. to construct Kähler-Einstein currents on varieties with log-terminal singularities (see section 6). For varieties of general type with semi log-canonical singularities (see section 5.2), one has to deal with slightly more general densities. The following result is a refinement of [Koł98, Theorem 2.5.2] and [EGZ09, Theorem A].

Theorem 1.5. - Let $\left(X, \omega_{X}\right)$ be a compact Kähler manifold of complex dimension $n \in \mathbb{N}^{*}$ and let $\omega$ be a semi-positive form with $V:=\operatorname{Vol}_{\omega}(X)=\int_{X} \omega^{n}>0$. Let $v$ and $\mu=f v$ be probability measures, with $0 \leqslant f \in L^{1}(v)$. Assume the following assumptions are satisfied: (H1) there exists $\alpha>0$ and $A_{\alpha}>0$ such that for all $\psi \in \operatorname{PSH}(X, \omega)$,
$$\int_{X} e^{-\alpha\left(\psi-\sup _{X} \psi\right)} d v \leqslant A_{\alpha} ;$$
(H2') there exists $C, \varepsilon>0$ such that $\int_{X}|f||\log f|^{n+\varepsilon} d v \leqslant C$.
Let $\varphi$ be the unique $\omega$-psh solution $\varphi$ to the complex Monge-Ampère equation
$$V^{-1}\left(\omega+d d^{c} \varphi\right)^{n}=\mu,$$
normalized by $\sup _{X} \varphi=0$. Then $-M \leqslant \varphi \leqslant 0$ where $M=M\left(C, \varepsilon, n, A_{\alpha}\right)$.
Proof. - The proof follows the same lines as that of Theorem 1.1, so we only emphasize the main technical differences and focus on the case $\varepsilon=1$. Set, for $t \geq 0$,
$$\chi(t)=(t+1) \sum_{j=0}^{n+1}(-1)^{n+1-j} \frac{(n+1)!}{j!}(\log (t+1))^{j} .$$
Observe that $\chi$ is a convex function such that $\chi(0)=0$ and $\chi^{\prime}(t)=(\log (t+1))^{n+1}$. Its Legendre transform is
$$\chi^{*}(s)=\sup _{t>0}\{s \cdot t-\chi(t)\}=s t(s)-\chi(t(s)),$$
where $1+t(s)=\exp \left(s^{\frac{1}{n+1}}\right)$ satisfies $s=\chi^{\prime}(t(s))$, thus
$$\chi^{*}(s)=P\left(s^{\frac{1}{n+1}}\right) \exp \left(s^{\frac{1}{n+1}}\right)-s,$$
where $P$ is the following polynomial of degree $n$,
$$P(X)=\sum_{j=0}^{n}(-1)^{n-j} \frac{(n+1)!}{j!} X^{j} .$$

We let the reader check that (H2') is equivalent to $\|f\|_{\chi} \leq C^{\prime}$, where $\|f\|_{\chi}$ denotes the Luxemburg norm of $f$,
$$\|f\|_{\chi}:=\inf \left\{r>0, \int_{X} \chi(|f| / r) d v \leq 1\right\} .$$
Let $K \subset X$ be a non pluripolar Borel set. It follows from Hölder-Young inequality [BBE ${ }^{+}$19, Proposition 2.15] that
$$\mu(K) \leq 2 C^{\prime}\left\|\mathbf{1}_{K}\right\|_{\chi^{*}},$$
where $\left\|\mathbf{1}_{K}\right\|_{\chi^{*}}=\inf \left\{r>0, v(K) \chi^{*}(1 / r) \leq 1\right\}=r_{K}$, with
$$\chi^{*}\left(1 / r_{K}\right)=\frac{1}{v(K)} .$$

We are interested in the behavior of this function as $v(K)$ approaches zero, i.e. for small values of $r_{K}$. Observe that $\chi^{*}(s) \leq \exp \left(2 s^{\frac{1}{n+1}}\right)$ for $s \geq 1 / r_{n}$, hence
$$v(K) \leq \delta_{n} \Longrightarrow \mu(K) \leq 2 C^{\prime} r_{K} \leq \frac{2^{n+2} C^{\prime}}{(-\log v(K))^{n+1}} .$$

Recall that (H1) and Lemma 1.2 yield
$$v(K) \leq A_{\alpha} e^{\alpha} \exp \left(-\frac{\alpha}{\operatorname{Cap}_{\omega}(K)^{1 / n}}\right)$$

It follows that for $v(K) \leq \delta_{n}$,
$$\mu(K) \leq C^{\prime \prime} \operatorname{Cap}_{\omega}(K)^{1+1 / n},$$
and we can then conclude by reasoning as in Lemma 1.4. This completes the proof when $\varepsilon=1$. The proof for arbitrary $\varepsilon>0$ is similar, the crucial point being the domination of $\mu$ by a multiple of $\mathrm{Cap}_{\omega}^{1+\varepsilon / n}$, with an exponent $1+\varepsilon / n>1$. \(\square\)
1.4. Big cohomology classes. - We now consider a similar situation where the reference cohomology class $\alpha$ is still big but no longer semi-positive. We assume for convenience that the ambient manifold $\left(X, \omega_{X}\right)$ is again compact Kähler, but one could equally well develop this material when $X$ belongs to the Fujiki class (i.e. when $X$ is merely bimeromorphic to a Kähler manifold).

By definition $\alpha$ is big if it contains a Kähler current, i.e. there is a positive current $T \in \alpha$ and $\varepsilon>0$ such that $T \geqslant \varepsilon \omega_{X}$. It follows from [Dem92] that one can further assume that $T$ has analytic singularities, i.e. it can be locally written $T=d d^{c} u$, with
$$u=\frac{c}{2} \log \left[\sum_{j=1}^{s}\left|f_{j}\right|^{2}\right]+v,$$
where $c>0, v$ is smooth and the $f_{j}$ 's are holomorphic functions.
Definition 1.6. - We let $\operatorname{Amp}(\alpha)$ denote the ample locus of $\alpha$, i.e. the Zariski open subset of all points $x \in X$ for which there exists a Kähler current in $\alpha$ with analytic singularities which is smooth in a neighborhood of $x$.

It follows from the work of Boucksom [Bou04] that one can find a single Kähler current $T_{0}$ with analytic singularities in $\alpha$ such that
$$\operatorname{Amp}(\alpha)=X \backslash \operatorname{Sing} \mathrm{~T}_{0} .$$

We fix $\theta$ a smooth closed differential (1,1)-form representing $\alpha$. Following Demailly, one defines the following $\theta$-psh function with minimal singularities:
$$V_{\theta}:=\sup \{u ; u \in \operatorname{PSH}(X, \theta) \text { and } u \leq 0\} .$$

Definition 1.7. - A $\theta$-psh function $\varphi$ has minimal singularities if for every other $\theta$-psh function $u$, there exists $C \in \mathbb{R}$ such that $u \leqslant \varphi+C$.

There are plenty of such functions, which play the role here of bounded functions when $\alpha$ is semi-positive. Demailly's regularization result [Dem92] insures that $\alpha$ contains many $\theta$-psh functions which are smooth in $\operatorname{Amp}(\alpha)$. In particular a $\theta$-psh function $\varphi$ with minimal singularities is locally bounded in $\operatorname{Amp}(\alpha)$. The Monge-Ampère measure $\left(\theta+d d^{c} \varphi\right)^{n}$ is thus well defined in $\operatorname{Amp}(\alpha)$ in the sense of Bedford and Taylor [BT82].

Definition 1.8. - It follows from the work of Boucksom [Bou02] that
$$\int_{\operatorname{Amp}(\alpha)}\left(\theta+d d^{c} \varphi\right)^{n}=: V_{\alpha}>0$$
is independent of $\varphi$, it is the volume of the cohomology class $\alpha$.

One can therefore develop a pluripotential theory in the Zariski open set $\operatorname{Amp}(\alpha)$. This was done in [BEGZ10], where the following properties have been established:
\begin{itemize}
\item[-] the class $\operatorname{PSH}(X, \theta)$ enjoys several compactness properties;
\item[-] the operator $\operatorname{MA}(\varphi)=V_{\alpha}^{-1}\left(\theta+d d^{c} \varphi\right)^{n}$ is a well defined probability measure on the set of $\theta$-psh functions with minimal singularities;
\item[-] the extremal functions $V_{K, \theta}=\sup \{u ; u \in \operatorname{PSH}(X, \theta)$ and $u \leqslant 0$ on $K\}$ and the Alexander-Taylor capacity $T_{\theta}(K)=\exp \left(-\sup _{X} V_{K, \theta}\right)$ enjoy similar properties as in the semi-positive case;
\item[-] in particular it compares similarly to the Monge-Ampère capacity
$$\operatorname{Cap}_{\theta}(K):=\sup \left\{\int_{K} \operatorname{MA}(u) ; u \in \operatorname{PSH}(X, \theta) \text { and } 0 \leqslant u-V_{\theta} \leqslant 1\right\} ;$$
\item[-] the comparison principle holds so Lemma 1.3 holds here as well.
\end{itemize}

The same proof as above therefore produces the following uniform a priori estimate, which is a refinement of [BEGZ10, Thm. 4.1]:

Theorem 1.9. - Let $\left(X, \omega_{X}\right)$ be a compact Kähler manifold of complex dimension $n \in \mathbb{N}^{*}$. Let $\alpha$ be a big cohomology class of volume $V_{\alpha}>0$ and fix $\theta$ a smooth closed differential (1,1)-form representing $\alpha$.

Let $v$ and $\mu=f v$ be probability measures, with $0 \leqslant f \in L^{p}(v)$ for some $p>1$. Assume the following assumptions are satisfied:
(H1) $\exists \alpha>0, A_{\alpha}>0$ such that $\forall \psi \in \operatorname{PSH}(X, \theta), \int_{X} e^{-\alpha\left(\psi-\sup _{X} \psi\right)} d v \leqslant A_{\alpha}$;
(H2) there exists $C>0$ such that $\left(\int_{X}|f|^{p} d v\right)^{1 / p} \leqslant C$.
Let $\varphi$ be the unique $\theta$-psh function with minimal singularities such that
$$V_{\alpha}^{-1}\left(\theta+d d^{c} \varphi\right)^{n}=\mu,$$
and $\sup _{X} \varphi=0$. Then $-M \leqslant \varphi-V_{\theta} \leqslant 0$ where
$$M=1+C^{1 / n} A_{\alpha}^{1 / n q} e^{\alpha / n q} b_{n}\left[5+e \alpha^{-1} C(q!)^{1 / q} A_{\alpha}^{1 / q}\right],$$
where $b_{n}$ is a uniform constant such that $\exp (-1 / x) \leqslant b_{n}^{n} x^{2 n}$ for all $x>0$.
Remark 1.10. - We also have an analogue of Theorem 1.5 in the big setting.

\section*{2. Uniform integrability}

We wish to apply the previous uniform estimates when the complex structure of the underlying manifold is moving. In this section we pay a special attention to assumption (H1), by generalizing an integrability result of Skoda-Zeriahi [Sko72, Zer01].
2.1. Notations. - In all what follows, given a positive real number $r$, we denote by $\mathbb{D}_{r}:=\{z \in \mathbb{C} ;|z|<r\}$ the open disk of radius $r$ in the complex plane. If $r=1$, we simply write $\mathbb{D}$ for $\mathbb{D}_{1}$.

Setting 2.1. - Let $\mathcal{X}$ be an irreducible and reduced complex Kähler space. We let $\pi: \mathcal{X} \rightarrow$ $\mathbb{D}$ denote a proper, surjective holomorphic map such that each fiber $X_{t}=\pi^{-1}(t)$ is a $n$ -dimensional, reduced, irreducible, compact Kähler space, for any $t \in \mathbb{D}$.

For later purposes, we pick a covering $\left\{U_{\alpha}\right\}_{\alpha}$ of $\mathcal{X}$ by open sets admitting an embedding $j_{\alpha}: U_{\alpha} \hookrightarrow \mathbb{C}^{N}$ for some $N \geqslant n+1$. Moreover, we fix a Kähler form $\omega$ on $\mathcal{X}$. Up to refining the covering, the datum of $\omega$ is equivalent to the datum of Kähler metrics on open neighborhoods of $j_{\alpha}\left(U_{\alpha}\right) \subset \mathbb{C}^{N}$ that agree on each intersection $U_{\alpha}^{\text {reg }} \cap U_{\beta}^{\text {reg }}$. Equivalently, $\omega$ is a genuine Kähler metric on $\mathcal{X}_{\text {reg }}$ such that $\left(j_{\alpha}\right)_{*}\left(\left.\omega\right|_{U_{\alpha}^{\text {reg }}}\right)$ is the restriction of a Kähler metric defined on a an open neighborhood of $j_{\alpha}\left(U_{\alpha}\right) \subset \mathbb{C}^{N}$.

Let us point out that this definition of a Kähler metric on a singular space $X$ is much more restrictive than merely asking for a Kähler metric on $X_{\text {reg }}$ (even say, by requiring that the latter has local potentials near $X_{\text {sing }}$, and that those are bounded). One important property that Kähler metrics satisfy is that their pull back under a modification is a smooth form (i.e. locally the restriction of a smooth form under a local embedding in $\mathbb{C}^{N}$ ); in particular, it is dominated by a Kähler form.

For each $t \in \mathbb{D}$, we set
$$\omega_{t}:=\omega_{\mid X_{t}} .$$
An easy yet important observation is the following.
Lemma 2.2. - In the Setting 2.1 and using the notation above, the quantity $\int_{X_{t}} \omega_{t}^{n}$ is independent of $t \in \mathbb{D}$. We will denote it by $V$ in the following.

Proof. - The function $\mathbb{D} \ni t \mapsto \int_{X_{t}} \omega_{t}^{n}$ coincides with the push-forward current $\pi_{*} \omega^{n}$ of bidimension (1, 1). Its distributional differential is zero as $d$ commutes with $\pi_{*}$ and $\omega$ is closed. \(\square\)

We fix a smooth, closed differential (1,1)-form $\Theta$ on $\mathcal{X}$ and set $\theta_{t}=\Theta_{\mid X_{t}}$. Up to shrinking $\mathbb{D}$, one will always assume that there exists a constant $C_{\Theta}>0$ such that
$$-C_{\Theta} \omega \leqslant \Theta \leqslant C_{\Theta} \omega .$$
In particular, one has the inclusion $\operatorname{PSH}\left(X_{t}, \theta_{t}\right) \subseteq \operatorname{PSH}\left(X_{t}, C_{\Theta} \omega_{t}\right)$. We assume that the cohomology classes $\left\{\theta_{t}\right\} \in H^{1,1}\left(X_{t}, \mathbb{R}\right)$ are psef, i.e. the sets $\operatorname{PSH}\left(X_{t}, \theta_{t}\right)$ are nonempty for all $t$. The notions of (quasi)-plurisubharmonic functions, positive currents and Monge-Ampère measure are well defined on singular spaces [Dem85].
2.2. Uniform integrability index. - Recall from [Dem82, Déf. 3] that if $T$ is a closed, positive current of bi-dimension $(p, p)$ on a complex space $X$ and if $x \in X$ is a closed point, then the Lelong number of $T$ at $x$ is defined as the limit
$$v(T, x):=\lim _{r \rightarrow 0} \frac{1}{r^{2 p}} \int_{\{\psi<r\}} T \wedge\left(d d^{c} \psi\right)^{p}$$
where $\psi:=\sum_{i \in I}\left|g_{i}\right|^{2}$ and $\left(g_{i}\right)_{i \in I}$ is a (finite) system of generators of the maximal ideal $\mathfrak{m}_{X, x} \subset \mathcal{O}_{X, x}$. It is proved in loc. cit. that the limit above is a decreasing limit, independent of the choice of the generators. Moreover, one has the formula
$$v(T, x)=\int_{\{x\}} T \wedge\left(d d^{c} \log \psi\right)^{p}$$
cf [Dem82, bottom of p. 45]. Finally, if $\varphi$ is a $\theta$-psh function on $X$ for some smooth, closed (1,1)-form $\theta$, then the Lelong number of $\varphi$ at a given point $x \in X$ is defined to be the quantity $v\left(\theta+d d^{c} \varphi, x\right)$.

Proposition 2.3. - In the Setting 2.1, let $\varphi_{t} \in \operatorname{PSH}\left(X_{t}, \theta_{t}\right)$ be a collection of $\theta_{t}$-psh functions on $X_{t}$. Then
$$\sup _{t \in \overline{\mathbb{D}}_{1 / 2}} \sup _{x \in X_{t}} v\left(\varphi_{t}, x\right)<+\infty .$$
Proof. - Let $U_{\alpha}^{\prime} \Subset U_{\alpha}$ be a relatively compact open subset such that the $U_{\alpha}^{\prime}$ are still a covering of $\mathcal{X}$. Up to adding more elements to the initial covering, one can always assume that one can find such a refinement. One picks cut-off functions $\chi_{\alpha}$ such that $\chi_{\alpha} \equiv 1$ on $U_{\alpha}^{\prime}$ and $\operatorname{Supp}\left(\chi_{\alpha}\right) \subset U_{\alpha}$. Now, let $x \in \mathcal{X}$; there exists $\alpha=\alpha(x)$ such that $x \in U_{\alpha}^{\prime}$. Recall that we have an embedding $j_{\alpha}: U_{\alpha} \rightarrow \mathbb{C}^{N}$; we set $x^{\prime}:=j_{\alpha}(x)$ and $G_{x^{\prime}}: \mathbb{C}^{N} \ni z \mapsto \log \left(\sum_{i=1}^{N}\left|z_{i}-x_{i}^{\prime}\right|^{2}\right)$. One can easily check that there exists a constant $A>0$, independent of the point $x$ now ranging in the compact set $\pi^{-1}\left(\overline{\mathbb{D}}_{1 / 2}\right)$, such that the function
$$H_{x}:=\chi_{\alpha} \cdot j_{\alpha}^{*} G_{x^{\prime}}$$
defines an $A \omega$-psh function on the whole $\mathcal{X}$. By the formula (2.3), one has
$$\begin{aligned}
v\left(\varphi_{t}, x\right) & =\int_{\{x\}}\left(\theta_{t}+d d^{c} \varphi_{t}\right) \wedge\left(\left.d d^{c}\left(j_{\alpha}^{*} G_{x^{\prime}}\right)\right|_{X_{t}}\right)^{n-1} \\
& \leqslant \int_{U_{\alpha}^{\prime} \cap X_{t}}\left(\theta_{t}+d d^{c} \varphi_{t}\right) \wedge\left(d d^{c} H_{x}\right)^{n-1} \\
& \leqslant \int_{U_{\alpha}^{\prime} \cap X_{t}}\left(\theta_{t}+d d^{c} \varphi_{t}\right) \wedge\left(A \omega_{t}+d d^{c} H_{x}\right)^{n-1} \\
& \leqslant \int_{X_{t}}\left(C_{\Theta} \omega_{t}+d d^{c} \varphi_{t}\right) \wedge\left(A \omega_{t}+d d^{c} H_{x}\right)^{n-1} \\
& =C_{\Theta} A^{n-1} \cdot V
\end{aligned}$$
The conclusion follows. \(\square\)

It follows from Skoda's integrability theorem [Sko72] that the Lelong number $v\left(\varphi_{t}, x\right)$ controls the local integrability index $\alpha\left(\varphi_{t}, x\right)$ of a $\theta_{t}$-psh function $\varphi_{t}$,
$$\alpha\left(\varphi_{t}, x\right):=\sup \left\{c>0 ; e^{-c \varphi_{t}} \in L_{\mathrm{loc}}^{2}\left(X_{t}, x\right)\right\},$$
via
$$\frac{1}{v\left(\varphi_{t}, x\right)} \leqslant \alpha\left(\varphi_{t}, x\right) \leqslant \frac{n}{v\left(\varphi_{t}, x\right)} .$$
Proposition 2.3 thus yields:
Corollary 2.4. - In the Setting 2.1, the following quantity
$$\alpha(\Theta):=\inf \left\{\alpha\left(\varphi_{t}, x\right) ; t \in \overline{\mathbb{D}}_{1 / 2}, x \in X_{t}, \varphi_{t} \in \operatorname{PSH}\left(X_{t}, \theta_{t}\right)\right\}$$
is positive.
2.3. Skoda's integrability theorem in families: the projective case. - Zeriahi [Zer01] has established a uniform version of Skoda's integrability theorem. We now further generalize Zeriahi's result by establishing its family version.

We first provide a very explicit result in the projective case which does not rely on Corollary 2.4 unlike its general Kähler analogue that will be given later, cf. Theorem 2.9. This should also help the reader in following the somehow tricky computations in the general Kähler case.

Proposition 2.5. - Let $V \subseteq \mathbb{P}^{N}$ be a projective variety of complex dimension $n$ and degree $d$. Let $\omega=\left.\omega_{\mathrm{FS}}\right|_{V}$ and $\varphi \in \operatorname{PSH}(V, \omega)$ be such that $\sup _{V} \varphi=0$. Then
$$\int_{V} e^{-\frac{1}{n d} \varphi} \omega^{n} \leqslant(4 n)^{n} \cdot d \cdot \exp \left\{-\frac{1}{n d} \int_{V} \varphi \omega^{n}\right\} .$$

To our knowledge, the inequality given in Proposition 2.5 above is new.
Remark 2.6. — When $\pi: \mathcal{X} \rightarrow \mathbb{D}$ is a projective family whose fibers have degree $d$ with respect to a given projective embedding, the above result gives the integrability of $e^{-\frac{1}{n d} \varphi_{t}}$ on $V_{t}:=\pi^{-1}(t)$. In particular, one gets $\alpha\left(\omega_{\mathrm{FS}}\right) \geqslant \frac{1}{2 n d}$.

Proof. - Embedding $\mathbb{P}^{1}$ in $\mathbb{P}^{2}$ if necessary, we assume without loss of generality that $N \geq 2$. We first claim that it is enough to prove the Proposition when $\varphi$ is smooth. Indeed, thanks to [CGZ13, Cor. C], there exists a sequence of smooth functions $\varphi_{n} \in$ PSH $\left(V, \omega_{\mathrm{FS}}\right)$ decreasing pointwise to $\varphi$. Let $\varepsilon_{n}:=\sup _{V} \varphi_{n}$; by Hartog's theorem, we have $\varepsilon_{n} \rightarrow 0$. If the Proposition holds for smooth functions, we will have
$$\int_{V} e^{-\frac{1}{n d} \varphi_{n}} \omega^{n} \leqslant e^{\frac{\varepsilon_{n} \cdot(d-1)}{n d}}(4 n)^{n} \cdot d \cdot \exp \left\{-\frac{1}{n d} \int_{V} \varphi_{n} \omega^{n}\right\}$$
Using Fatou Lemma and the monotone convergence theorem, we deduce the expected inequality for $\varphi$. From now on, one assumes that $\varphi$ is smooth.

The projective logarithmic kernel on $\mathbb{P}^{N} \times \mathbb{P}^{N}$ is defined by the following formula
$$G(x, y):=\log \left(\frac{\|x \wedge y\|}{\|x\| \cdot\|y\|}\right), \quad x, y \in \mathbb{P}^{N},$$
writing $x, y$ in homogeneous coordinates. By [AAZ20, Lem. 4.1], for any fixed $y, x \mapsto$ $G(x, y)$ is a non positive $\omega_{\mathrm{FS}}$-psh function in $\mathbb{P}^{N}$ such that $\left(\omega_{\mathrm{FS}}+d d_{x}^{c} G(\cdot, y)\right)^{N}=\delta_{y}$. We set $g=\left.G\right|_{V}$ and $g_{y}=g(\cdot, y)$. By definition, $g_{y}$ has Lelong number one at $y$. Therefore, it follows from [Dem85, Cor. 4.8] that $\omega_{g_{y}}^{n}:=\left(\omega+d d^{c} g(\cdot, y)\right)^{n} \geqslant \delta_{y}$. From Stokes formula (cf Lemma 2.11 below) it follows that
$$\begin{aligned}
\varphi(y) & \geqslant \int_{V} \varphi \omega_{g_{y}}^{n}=\int_{V} \varphi\left(\omega+d d^{c} g_{y}\right) \wedge \omega_{g_{y}}^{n-1} \\
& =\int_{V} \varphi \omega \wedge \omega_{g_{y}}^{n-1}+\int_{V} g_{y}\left(\omega+d d^{c} \varphi\right) \wedge \omega_{g_{y}}^{n-1}-\int_{V} g_{y} \omega \wedge \omega_{g_{y}}^{n-1} \\
& \geqslant \int_{V} \varphi \omega \wedge \omega_{g_{y}}^{n-1}+\int_{V} g_{y} \omega_{\varphi} \wedge \omega_{g_{y}}^{n-1},
\end{aligned}$$
using that $g_{y} \leqslant 0$. One obtains similarly
$$\begin{aligned}
\int_{V} \varphi \omega \wedge \omega_{g_{y}}^{n-1} & \geqslant \int_{V} \varphi \omega^{2} \wedge \omega_{g_{y}}^{n-2}+\int_{V} g_{y} \omega \wedge \omega_{\varphi} \wedge \omega_{g_{y}}^{n-2} \\
& \geqslant \int_{V} \varphi \omega^{2} \wedge \omega_{g_{y}}^{n-2}+\int_{V} g_{y} \omega_{\varphi} \wedge \omega_{g_{y}}^{n-1},
\end{aligned}$$
where the second inequality follows from
$$\int_{V} g_{y} \omega \wedge \omega_{\varphi} \wedge \omega_{g_{y}}^{n-2}=\int_{V} g_{y} \omega_{\varphi} \wedge \omega_{g_{y}}^{n-1}+\int_{V} d g_{y} \wedge d^{c} g_{y} \wedge \omega_{\varphi} \wedge \omega_{g_{y}}^{n-2} \geqslant \int_{V} g_{y} \omega_{\varphi} \wedge \omega_{g_{y}}^{n-1} .$$
Iterating the process $n$ times we end up with
$$\varphi(y) \geqslant \int_{V} \varphi \omega^{n}+n \int_{V} g_{y} \omega_{\varphi} \wedge \omega_{g_{y}}^{n-1} .$$
Hence
$$\int_{V} e^{-\frac{1}{n d} \varphi} \omega^{n} \leqslant \exp \left\{-\frac{1}{n d} \int_{V} \varphi \omega^{n}\right\} \cdot I$$
where
$$I:=\int_{y \in V} \exp \left\{-\frac{1}{d} \int_{x \in V} g_{y}(x) \omega_{\varphi}(x) \wedge \omega_{g_{y}}(x)^{n-1}\right\} \omega(y)^{n}$$
The $(n, n)$-form $\frac{1}{d} \cdot \omega_{\varphi} \wedge \omega_{g_{y}}^{n-1}$ induces a probability measure on $V$ given that
$$\int_{V} \omega_{\varphi} \wedge \omega_{g_{y}}^{n-1}=\int_{\mathbb{P}^{N}} \omega_{\varphi} \wedge \omega_{g_{y}}^{n-1} \wedge[V]=\left\{\omega_{\mathrm{FS}}\right\}^{n} \cdot\{V\}=d$$
From Jensen's inequality, one can then derive
$$I \leqslant \frac{1}{d} \int_{y \in V} \int_{x \in V} e^{-g(x, y)} \omega_{\varphi}(x) \wedge\left(\omega(x)+d d_{x}^{c} g(x, y)\right)^{n-1} \wedge \omega(y)^{n} .$$
Lemma 2.8 (i) yields
$$\omega_{\varphi}(x) \wedge\left(\omega(x)+d d_{x}^{c} g(x, y)\right)^{n-1} \leqslant e^{-2(n-1) g(x, y)} \omega_{\varphi}(x) \wedge \omega(x)^{n-1} .$$
Lemma 2.8 (ii) below (for $\delta=1 / 2 n$ ) now yields
$$\begin{aligned}
I & \leqslant \frac{1}{d} \int_{y \in V} \int_{x \in V} e^{(-2 n+1) g(x, y)} \omega_{\varphi}(x) \wedge \omega(x)^{n-1} \wedge \omega(y)^{n} \\
& =\frac{1}{d} \int_{x \in V}\left(\int_{y \in V}\left[e^{-2\left(1-\frac{1}{2 n}\right) g(x, y)} \omega(y)\right]^{n}\right) \omega_{\varphi}(x) \wedge \omega(x)^{n-1} \\
& \leqslant(4 n)^{n} \int_{x \in V}\left(\frac{1}{d} \int_{y \in V}\left(\omega+d d^{c} \chi_{\frac{1}{2 n}} \circ g_{x}\right)^{n}\right) \omega_{\varphi}(x) \wedge \omega(x)^{n-1} \\
& =(4 n)^{n} \int_{x \in V} \omega_{\varphi}(x) \wedge \omega(x)^{n-1}=(4 n)^{n} \cdot d .
\end{aligned}$$ \(\square\)

Remark 2.7. - The same arguments as above show that for any $\gamma \in(0,2)$
$$\int_{V} e^{-\frac{\gamma}{n d} \varphi} \omega^{n} \leqslant C_{\gamma} \cdot d \exp \left\{-\frac{\gamma}{n d} \int_{V} \varphi \omega^{n}\right\},$$
where $C_{\gamma}>0$ depends on $n$ and $\gamma$. We have fixed $\gamma=1$ in the above proposition to simplify the statement.

Lemma 2.8. - With the notations of the proof of Proposition 2.5 above, we fix a point $y \in V$ and set $g:=g_{y}$. Moreover, let $\delta \in(0,1)$ be a given number. Then, the following set of inequalities hold as currents on $V$.
\begin{itemize}
\item[(i)] $\omega_{g} \leqslant e^{-2 g} \omega$
\item[(ii)] $\frac{\delta}{2} e^{-2(1-\delta) g} \omega \leqslant \omega+d d^{c} \chi_{\delta} \circ g$
\end{itemize}
Here, $\chi_{\delta}$ is the function defined on $\mathbb{R}$ by the expression $\chi_{\delta}(t):=\frac{e^{2 \delta t}}{4 \delta}$.
It is understood here that we take derivatives w.r.t. $x$ and the estimates are uniform both in $x$ and $y$.

Proof. - We proceed in three steps.
Step 1. Reduction to a computation on $\mathbb{C}^{N}$.
First of all we observe that the function $g$ as well as the (1,1)-currents $\omega$ and $\omega_{g}$ are the restriction to $V$ of a function or (1,1)-currents on $\mathbb{P}^{N}$. As positivity is preserved by restriction to a subvariety, it is enough to prove the inequalities of currents above on the whole $\mathbb{P}^{N}$ where they make sense as well.

Now, recall that $\operatorname{PU}(N, \mathbb{C})$ acts transitively on $\mathbb{P}^{N}$ by transformations preserving $\omega_{\mathrm{FS}}$ and an isometry $u$ sends $G_{y}$ to $G_{u(y)}$. Therefore it suffices to prove all the inequalities above on $\mathbb{P}^{N}$, for the special point $y=[1: 0: \cdots: 0]$. We work in the affine chart $\left(U_{1}, z\right)$ where $U_{1}:=\left\{x \in \mathbb{P}^{N}: x_{1} \neq 0\right\}$ and $z:=\left(z_{j}\right)_{j}, z_{j}=x_{j} / x_{1}$. In these coordinates $\left.\omega_{\mathrm{FS}}\right|_{U_{1}}=\frac{1}{2} d d^{c} \log \left(1+\|z\|^{2}\right)$. Note that $U_{1}$ is dense in $\mathbb{P}^{N}$ and both $\omega_{\mathrm{FS}}, \omega_{\mathrm{G}}$ are smooth on the complement $\mathbb{P}^{N} \backslash U_{1}$; thus it is sufficient to prove the inequalities on $U_{1} \simeq \mathbb{C}^{N}$.

We actually claim that is is sufficient to prove the inequalities on $U_{1} \backslash\{y\}$, where all the currents involved are smooth differential forms. This is because neither of the positive currents $e^{-2 \mathrm{G}} \omega_{\mathrm{FS}}$ and $\omega_{\mathrm{FS}}+d d^{c} \chi_{\delta} \circ G$ on $\mathbb{P}^{N}$ puts any mass on $\{y\}$. This follows from the integrability of $e^{-2 G}$ for the first one (recall that $N \geqslant 2$ ) and the boundedness of $\chi_{\delta} \circ G$ for the second one.

As observed in [AAZ20, Lem. 4.1], for $(x, y:=[1: 0 \cdots: 0]) \in U_{1} \times U_{1}$ we have
$$G(x, y)=N(z, 0)-\frac{1}{2} \log \left(1+\|z\|^{2}\right)$$
where $z=z(x)$ and $N(z, 0):=\frac{1}{2} \log \|z\|^{2}$. Thus in $U_{1}$ we have $e^{-2 G}=1+\frac{1}{\|z\|^{2}}$ and
$$\omega(x)+d d_{x}^{c} G_{y}(x)=d d_{z}^{c} N(z, 0)=\frac{1}{2} d d_{z}^{c} \log \|z\|^{2} .$$
Let us define $\beta:=d d^{c}\|z\|^{2}=i \sum_{k=1}^{N} d z_{k} \wedge d \bar{z}_{k}$ and let $\alpha_{1}:=\sum_{k=1}^{N} \bar{z}_{k} d z_{k}$.
Step 2. Proof of Item (i).
Standard computations give
$$\left(\omega_{\mathrm{FS}}\right)_{j \bar{k}}=\frac{\left(1+\|z\|^{2}\right) \delta_{j \bar{k}}-\bar{z}_{j} z_{k}}{2\left(1+\|z\|^{2}\right)^{2}} \quad \text { and } \quad N_{j \bar{k}}=\frac{1}{2} \cdot \frac{\|z\|^{2} \delta_{j \bar{k}}-\bar{z}_{j} z_{k}}{\|z\|^{4}}$$
or equivalently
$$\omega_{\mathrm{FS}}=\frac{1}{2}\left(\frac{1}{1+\|z\|^{2}} \beta-\frac{1}{\left(1+\|z\|^{2}\right)^{2}} i \alpha_{1} \wedge \bar{\alpha}_{1}\right) \quad \text { and } \quad \omega_{G}=\frac{1}{2}\left(\frac{1}{\|z\|^{2}} \beta-\frac{1}{\|z\|^{4}} i \alpha_{1} \wedge \bar{\alpha}_{1}\right)$$
The matrix $A(z):=\left(z_{i} \bar{z}_{j}\right)_{i j}$ is semipositive with rank at most one and trace $\|z\|^{2}$. Therefore, if $\lambda, \mu \in \mathbb{R}$ (they can depend on $z$ ), the matrix $\lambda \mathrm{Id}+\mu A$ is hermitian with eigenvalues $\lambda$ (with multiplicity $N-1$ ) and $\lambda+\|z\|^{2} \cdot \mu$ (with multiplicity one). In particular, it is semipositive if and only if $\lambda \geqslant \max \left(0,-\|z\|^{2} \cdot \mu\right)$.
The computations above show that the eigenvalues of the (1,1)-form $\lambda \beta+\mu i \alpha_{1} \wedge \bar{\alpha}_{1}$ with respect to $\beta$ are $\lambda$ and $\lambda+\|z\|^{2} \cdot \mu$. Now, if $C$ is some non-negative constant, the (1, 1)-form $C e^{-2 g} \omega_{\mathrm{FS}}-\omega_{G}$ can be rewritten as follows
$$\frac{1}{2\left(1+\|z\|^{2}\right)\|z\|^{4}} \cdot\left[(C-1)\|z\|^{2}\left(1+\|z\|^{2}\right) \cdot \beta+\left[\left(1+\|z\|^{2}\right)-C\|z\|^{2}\right] \cdot i \alpha_{1} \wedge \bar{\alpha}_{1}\right] .$$
The latter form is semipositive if and only if $C \geqslant 1$. This proves $(i)$.
Step 3. Proof of Item (ii).
Observe that $\chi_{\delta}$ is convex increasing with $0 \leqslant \chi_{\delta}^{\prime} \leqslant 1 / 2$ for $t \leqslant 0$. Standard computations give $d d^{c} \chi_{\delta} \circ G=\chi_{\delta}^{\prime} \circ G d d^{c} G+\chi_{\delta}^{\prime \prime} \circ G d G \wedge d^{c} G$. Next, we have
$$d d^{c} G=\frac{1}{2\|z\|^{2}\left(1+\|z\|^{2}\right)}\left[\beta-\frac{1+2\|z\|^{2}}{\|z\|^{2}\left(1+\|z\|^{2}\right)} \cdot i \alpha_{1} \wedge \bar{\alpha}_{1}\right]$$
with the notation introduced in Step 1. Similarly, one finds
$$d G \wedge d^{c} G=\frac{1}{4\|z\|^{4}\left(1+\|z\|^{2}\right)^{2}} i \alpha_{1} \wedge \bar{\alpha}_{1} .$$
To lighten notation, we will from now on write $\chi^{\prime}$ (resp. $\chi^{\prime \prime}$ ) to denote $\chi_{\delta}^{\prime} \circ G$ (resp. $\left.\chi_{\delta}^{\prime \prime} \circ G\right)$. One has
$$\omega_{\mathrm{FS}}+d d^{c} \chi_{\delta} \circ G=\frac{1}{2\left(1+\|z\|^{2}\right)}\left[\left(1+\frac{\chi^{\prime}}{\|z\|^{2}}\right) \beta+\frac{\frac{1}{2} \chi^{\prime \prime}-\chi^{\prime}\left(1+2\|z\|^{2}\right)}{\|z\|^{4}\left(1+\|z\|^{2}\right)} i \alpha_{1} \wedge \bar{\alpha}_{1}\right] .$$
As a result, the two eigenvalues $\lambda, \mu$ of $\omega_{\mathrm{FS}}+d d^{c} \chi_{\delta} \circ G$ with respect to $\omega_{\mathrm{FS}}$ are given by
$$\lambda=1+\frac{\chi^{\prime}}{\|z\|^{2}}$$
and
$$\mu=\left(1+\|z\|^{2}\right) \cdot\left(1+\frac{\chi^{\prime}}{\|z\|^{2}}+\frac{\frac{1}{2} \chi^{\prime \prime}-\chi^{\prime}\left(1+2\|z\|^{2}\right)}{\|z\|^{2}\left(1+\|z\|^{2}\right)}\right)=\left(1+\|z\|^{2}-\chi^{\prime}\right)+\frac{\chi^{\prime \prime}}{2\|z\|^{2}}$$
Using the definition of $\chi$ and the fact that $e^{-2 G}=1+\frac{1}{\|z\|^{2}}$, one easily sees that $\lambda \geqslant$ $\frac{1}{2} e^{-2(1-\delta) G}$ and $\mu \geqslant \frac{\delta}{2} e^{-2(1-\delta) G}$. The conclusion follows. \(\square\)
2.4. Skoda's integrability theorem in families: the general case. - In this section, we bypass the projectivity assumption and establish a quite general family version of Skoda's integrability theorem, valid for families of compact Kähler varieties:

Theorem 2.9. - In Setting 2.1, let us choose a positive number $\alpha \in(0, \alpha(\Theta))$, which is possible thanks to Corollary 2.4. Then, there exist constant $A_{\alpha}, C>0$ such that for all $t \in \overline{\mathbb{D}}_{1 / 2}$ and for all $\varphi_{t} \in \operatorname{PSH}\left(X_{t}, \theta_{t}\right)$ with $\sup _{X_{t}} \varphi_{t}=0$,
$$\int_{X_{t}} e^{-\alpha \varphi_{t}} \omega_{t}^{n} \leqslant C \exp \left\{-A_{\alpha} \int_{X_{t}} \varphi_{t} \omega_{t}^{n}\right\} .$$
Proof. - The proof follows the same strategy as in [Zer01], as presented in [GZ17, Thm. 2.50]. There exists a finite number of trivializing charts $\left\{U_{\tau}\right\}$ of $\mathcal{X}$ such that $\pi^{-1}\left(\overline{\mathbb{D}}_{1 / 2}\right) \subset \cup_{\tau} U_{\tau}$. The statement will then follow if we prove the bound for the integral on the left-hand side replacing $X_{t}$ by $X_{t} \cap U_{\tau}$. Moreover, w.l.o.g we can assume that we have an immersion $j_{\tau}: U_{\tau} \hookrightarrow \mathbb{B}$, where $\mathbb{B}$ is the unit ball in $\mathbb{C}^{N}$. Up to shrinking $U_{\tau}$, one can also assume that there exists a smooth function $\rho$ on $\mathbb{B}$ such that $\sup _{\mathbb{B}} \rho=$ -2 and $\Theta \mid{ }_{U_{\tau}}=d d^{c} j_{\tau}^{*} \rho$. We define $\rho_{t}:=\left.\left(j_{\tau}^{*} \rho\right)\right|_{U_{\tau} \cap X_{t}}$; this is a potential of $\left.\theta_{t}\right|_{U_{\tau} \cap X_{t}}$. Note that $\psi_{t}:=\varphi_{t}+\rho_{t}$ is a non-positive psh function in $U_{\tau} \cap X_{t}$ such that
$$\varphi_{t}-2 \geqslant \psi_{t} \geqslant \varphi_{t}-C_{\tau}$$
for some constant $C_{\tau}>0$ depending only on $U_{\tau}$. It is also clear that proving (2.4) is equivalent to showing that
$$\int_{U_{\tau} \cap X_{t}} e^{-\alpha \psi_{t}} \omega_{t}^{n} \leqslant C_{\tau} \exp \left\{-A_{\alpha, \tau} \int_{U_{\tau} \cap X_{t}} \psi_{t} \omega_{t}^{n}\right\},$$
for some constants $C_{\tau}, A_{\alpha, \tau}$ that do not depend on $t$.
Claim 2.10. - It is sufficient to prove (2.6) for smooth, non-positive psh functions $\psi_{t}$ on $U_{\tau} \cap X_{t}$ such that
$$d d^{c} \psi_{t} \geqslant\left.\left(j_{\tau}^{*} d d^{c}\|z\|^{2}\right)\right|_{X_{t}} .$$
Proof of Claim 2.10. — Indeed, as
$$\int_{U_{\tau} \cap X_{t}} e^{-\alpha \psi_{t}} \omega_{t}^{n} \leqslant e^{\alpha} \int_{U_{\tau} \cap X_{t}} e^{-\alpha\left(\psi_{t}+j_{\tau}^{*}\|z\|^{2}\right)} \omega_{t}^{n},$$
we can replace $\psi_{t}$ by the function $\psi_{t}+j_{\tau}^{*}\|z\|^{2}$, bounded above by -1. Next, thanks to a result of Fornaess-Narasimhan [FN80, Thm. 5.5], one can write $\psi_{t}$ as a decreasing limit of non-positive, smooth psh functions on $U_{\tau} \cap X_{t}$ (up to shrinking $U_{\tau}$ possibly). The combination of the monotone convergence theorem and the integrability of $e^{-\alpha \varphi_{t}}$ on $X_{t}$ provided by Corollary 2.4 settles the claim. \(\square\)

From now on, we assume that $\psi_{t}$ is smooth, and we work exclusively on $U_{\tau}$ that we view inside the unit ball $\mathbb{B}$ of $\mathbb{C}^{N}$. By abuse of notation, we will denote by $\mathbb{B} \cap X_{t}$ the set $U_{\tau} \cap X_{t}$. In the same vein, we will identify the coordinate functions $z=\left(z_{1}, \ldots, z_{N}\right)$ on $\mathbb{B} \subset \mathbb{C}^{N}$ with their pull-back by $j_{\tau}$ on $U_{\tau}$.

Let us pick some number $t \in \overline{\mathbb{D}}_{1 / 2}$ and some point $x \in \mathbb{B} \cap X_{t}$. We denote by $\Phi_{x}$ the automorphism of the unit ball B that sends $x$ to the origin and consider
$$G_{x}(z):=\log \left\|\Phi_{x}(z)\right\|$$
the pluricomplex Green function of the unit ball $\mathbb{B}$. Recall that $G_{x}$ is the unique plurisubharmonic function in $\mathbb{B}$ such that $\left(d d^{c} G_{x}\right)^{N}=\delta_{x}$ in the weak sense of currents, $G_{x} \leqslant 0$ and $G_{x}$ is identically zero on $\partial \mathbf{B}$. Standard computations yield
$$d d^{c} G_{x} \leqslant \frac{C_{0}}{\left\|\Phi_{x}(z)\right\|^{2}} d d^{c}\|z\|^{2} \quad \text { on } \mathbb{B} \text {. }$$
for some dimensional constant $C_{0}=C_{0}(N)>0$.
Since $\left[\left.X_{t}\right|_{\mathbb{B}}\right]$ is a positive $(N-n, N-n)$-current on $\mathbb{B}$ and the singular set of the restriction of the Green function $\left.G_{x}\right|_{X_{t}}$ is compact (it is indeed equal to $\{x\}$ ), the mixed Monge-Ampère measure $\left(d d^{c} G_{x}\right)^{n} \wedge\left[X_{t}\right]$ is well defined [GZ17, Prop. 3.15] and it has a Dirac mass with coefficient $\geqslant 1$ at the point $x$. Since $\psi_{t} \leqslant 0$ we then have
$$\psi_{t}(x) \geqslant \int_{\mathbb{B}} \psi_{t}\left(d d^{c} G_{x}\right)^{n} \wedge\left[X_{t}\right]=\int_{\mathbb{B} \cap X_{t}} \psi_{t}\left(d d^{c} G_{x}\right)^{n} .$$
Now, we have the following result, which is Stokes' formula in a context of isolated singularities.

Lemma 2.11. - Let $X \subset B_{\mathbb{C}^{N}}(0,2)$ be a a proper, $n$-dimensional complex subspace of the ball of radius 2 in $\mathbb{C}^{N}$, center at the origin. Let $u, v, w$ be psh functions on $B_{\mathbb{C}^{N}}(0,2)$ with isolated singularities, i.e. they are smooth outside a discrete set of points in $B_{\mathbb{C}^{N}}(0,2)$ which we assume does not meet $\partial B_{\mathbb{C}^{N}}(0,1)$. Finally, let $\mathbb{B}:=B_{\mathbb{C}^{N}}(0,1) \cap X$. Then, we have
$$\int_{\partial \mathbb{B}}\left(u d^{c} v-v d^{c} u\right) \wedge\left(d d^{c} w\right)^{n-1}=\int_{\mathbb{B}}\left(u d d^{c} v-v d d^{c} u\right) \wedge\left(d d^{c} w\right)^{n-1}$$

We include a proof for the reader's convenience.
Proof of Lemma 2.11. - By using a (regularized) maximum operation, we can find a family of smooth psh functions $u_{\varepsilon}$ (resp. $v_{\varepsilon}, w_{\varepsilon}$ ) decreasing to $u$ (resp. $v, w$ ) and which coincide with their limit outside a compact set $K_{\varepsilon} \Subset \mathbb{B}$ which collapses onto a finite set $S \in \mathrm{~B}$. By the usual Stokes' formula, one has
$$\int_{\partial \mathbb{B}}\left(u_{\varepsilon} d^{c} v_{\varepsilon}-v_{\varepsilon} d^{c} u_{\varepsilon}\right) \wedge\left(d d^{c} w_{\varepsilon}\right)^{n-1}=\int_{\mathbb{B}}\left(u_{\varepsilon} d d^{c} v_{\varepsilon}-v_{\varepsilon} d d^{c} u_{\varepsilon}\right) \wedge\left(d d^{c} w_{\varepsilon}\right)^{n-1}$$
The left-hand side of the formula above is identical to the left-hand side of (2.9). To prove that the right-hand side above converges to the right-hand side of (2.9), we prove that the current $\left(u_{\varepsilon} d d^{c} v_{\varepsilon}-v_{\varepsilon} d d^{c} u_{\varepsilon}\right) \wedge\left(d d^{c} w_{\varepsilon}\right)^{n-1}$ on $\mathbb{B}$ converges to $\left(u d d^{c} v-v d d^{c} u\right) \wedge$ $\left(d d^{c} w\right)^{n-1}$ weakly, globally on $\mathbb{B}$ and locally smoothly on $\overline{\mathbb{B}} \backslash S$. The local smooth convergence outside $S$ is obvious. As for the global weak convergence, it follows from the convergence $u_{\varepsilon} d d^{c} v_{\varepsilon} \wedge\left(d d^{c} w_{\varepsilon}\right)^{n-1} \rightharpoonup u d d^{c} v \wedge\left(d d^{c} w\right)^{n-1}$ (and its symmetrical version swapping $u$ and $v$ ), proved by Demailly, cf e.g. [Dem85, Thm. 2.6 and Rem. 2.10]. \(\square\)