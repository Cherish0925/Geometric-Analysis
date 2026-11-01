---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Kähler-Einstein metrics on quasi-projective manifolds]

---
source_file: 2309_03858.pdf
converter: mathpix
format: mmd
---

\title{
Kähler-Einstein metrics on quasi-projective manifolds
}

\author{
Quang-Tuan Dang \& Duc-Viet Vu
}

April 29, 2025

\begin{abstract}
Let $X$ be a compact Kähler manifold and $D$ be a simple normal crossing divisor on $X$ such that $K_{X}+D$ is big and nef. We first prove that the singular Kähler-Einstein metric constructed by Berman-Guenancia is almost-complete on $X \backslash D$ in the sense of Tian-Yau. In our second main result, we establish the weak convergence of conic Kähler-Einstein metrics of negative curvature to the above-mentioned metric when $K_{X}+D$ is merely big, answering partly a recent question posed by Biquard-Guenancia. Potentials of low energy play an important role in our approach.
\end{abstract}

Keywords: Monge-Ampère equations, conic Kähler-Einstein metrics, almost-complete metrics, domination principle, analytic singularities.

Mathematics Subject Classification 2020: 32U15, 32Q15.

\section*{1 Introduction}

Let $M$ be a $n$-dimensional (non-compact) Kähler manifold. Let $\eta$ be a closed positive $(1,1)$ -current on $M$. Following [8, 7], we say that $\eta$ has a well-defined Ricci curvature if the non-pluripolar self-product $\left\langle\eta^{n}\right\rangle$ of $\eta$ is well-defined on $M$ (see [10] for this notion) and for every local holomorphic volume form $\Omega$ on $M$, one can write $\left\langle\eta^{n}\right\rangle=e^{-2 f} i^{n^{2}} \Omega \wedge \bar{\Omega}$ for some function $f \in L_{\text {loc }}^{1}$. In this case, we define Ric $\eta:=\frac{i}{\pi} \partial \bar{\partial} f$. The current $\eta$ is said to be singular Kähler-Einstein metric on $M$ if Ric $\eta=\lambda \eta$ for some constant $\lambda \in \mathbb{R}$. We are interested in studying (singular) Kähler-Einstein metrics in $M$. We will focus on the most common case where $M$ is the complement of a divisor in a compact Kähler manifold. Let us enter details.

Let $(X, \omega)$ be a compact Kähler manifold of dimension $n$. Let $D$ be a normal simple crossing divisor on $X$. By abuse of notation, we also denote by $D$ the support of $D$. About forty years ago, Cheng-Yau [13] established some necessary conditions for the existence of complete Kähler-Einstein metrics on non-compact manifolds (see also [39] for refinements). Based on this work, Kobayashi [35] proved that there exists a complete Kähler-Einstein metric of negative curvature (with Poincaré singularities near $D$ ) on $X \backslash D$ if $K_{X}+D$ is ample. The uniqueness of such a metric follows from [48].

More generally, Tian-Yau [42] proved the existence and uniqueness of an almost complete Kähler-Einstein metric $\tilde{\omega}_{D}$ on $X \backslash D$ provided that $K_{X}+D$ is big and nef, and $K_{X}+D$ is ample modulo $D$, (cf. Definition 4.2 below for almost complete metrics). We recall that
$K_{X}+D$ is ample modulo $D$ if for every effective reduced curve $C$ on $X$ not contained in $D,\left(K_{X}+D\right) \cdot C>0$, hence the non-Kähler locus of the Chern class of $K_{X}+D$ must lie in the support of $D$. We refer to [42] for more information and applications of this metric and to [4, 1, 2, 3, 9, 22, 31, 33, 46, 47, 26, 18] for related results.

In another approach, Berman-Guenancia [8] proved that there exists a unique closed positive current $\widehat{\omega}_{D}$ of full Monge-Ampère mass (in the sense of [10]) in $c_{1}\left(K_{X}+D\right)$ such that
$$\operatorname{Ric}\left(\widehat{\omega}_{D}\right)=-\widehat{\omega}_{D}+[D]$$
provided that $K_{X}+D$ is big, where $[D]$ denotes the current of integration along $D$. If $K_{X}+D$ is additionally nef, then $\widehat{\omega}_{D}$ is also smooth on the complement of $D$ in the ample locus of $K_{X}+D$ (see [8] or Lemma 4.4 below).

In the case where $K_{X}+D$ is ample, using the local description of $\tilde{\omega}_{D}$ and the Monge-Ampère equation satisfied by it (see [35, Page 407]), one sees that $\tilde{\omega}_{D}$ can be extended trivially through $D$ as a closed positive (1, 1)-current of full Monge-Ampère mass in $K_{X}+D$ and satisfies the same equation as $\widehat{\omega}_{D}$. Hence $\widehat{\omega}_{D}=\tilde{\omega}_{D}$. In other words, we obtain a global interpretation of the complete metric $\tilde{\omega}_{D}$ if $K_{X}+D$ is ample (see also [31] for more information). Here is our first main result giving an analogue in the case where $K_{X}+D$ is big and nef.

Theorem 1.1. Let $D$ be a simple normal crossing divisor such that $K_{X}+D$ is big and nef. Let $E$ denote the non-ample locus of $K_{X}+D$. Then there exists a unique almost-complete singular Kähler-Einstein metric $\omega_{D}$ on $X \backslash D$, and this metric satisfies the following properties:
\begin{itemize}
\item[(i)] $\omega_{D}$ is smooth Kähler metric on $X \backslash(D \cup E)$,
\item[(ii)] $\omega_{D}$ can be extended to a closed positive (1,1)-current on $X$ which is of full Monge-
\end{itemize}Ampère mass in the class $c_{1}\left(K_{X}+D\right)$ and there holds
$$\operatorname{Ric} \omega_{D}=-\omega_{D}+[D]$$
as currents on $X$.
We note that since $\omega_{D}$ is of full Monge-Ampère mass, one has
$$\int_{X \backslash(D \cup E)} \omega_{D}^{n}=\int_{X}\left(c_{1}\left(K_{X}+D\right)\right)^{n},$$
which is to say that the volume of the singular metric $\omega_{D}$ on $X \backslash D$ is finite and is equal exactly to the volume of the line bundle of $K_{X}+D$. Theorem 1.1 shows that this almost-complete metric on $X \backslash D$ is indeed equal to the above metric $\omega_{D}$ constructed by Berman-Guenancia, using the comparison principle [8, Proposition 4.1]. It generalizes the previous result of Tian-Yau when $K_{X}+D$ is big, nef and $K_{X}+D$ is ample modulo $D$ (because in this case, one has $E \subset D$ ).

We now come to the next part of the introduction in which we discuss a very recent question posed by Biquard-Guenancia [9] about the degeneration of conic Kähler-Einstein metrics. Our result gives a direct construction for the above metric $\omega_{D}$ as the weak limit of conic Kähler-Einstein metrics.

Let $D$ be a simple normal crossing divisor on $X$ such that $K_{X}+D$ is big. By [10, 36, 49], there exists a unique closed positive current $\omega_{\epsilon}$ of full Monge-Ampère mass in $c_{1}\left(K_{X}+(1-\right.$ $\epsilon) D)$ so that
$$\operatorname{Ric} \omega_{\epsilon}=-\omega_{\epsilon}+(1-\epsilon)[D],$$
for every constant $\epsilon \in(0,1)$ small enough. The equation is understood in the sense of currents. If $K_{X}+D$ is additionally ample, then the metric $\omega_{\epsilon}$ is, in fact, conic near $D$ by [32] refining [11, 12, 34] (see also [30, 38, 41]). For this reason, we say that $\omega_{\epsilon}$ is a Kähler-Einstein metric with a conic singularity of angle $2 \pi \epsilon$ along $D$ even if $K_{X}+D$ is merely big.

It is thus natural to study the relation between $\omega_{\epsilon}$ and $\omega_{D}$ as $\epsilon \rightarrow 0^{+}$. Biquard-Guenancia [9] asked whether the metric $\omega_{\epsilon}$ converges to $\omega_{D}$ as $\epsilon \rightarrow 0$ in an appropriate sense. Under some additional assumptions on the positivity of $K_{X}+D$, the local $\mathcal{C}^{\infty}$ convergence was established in [9, 31, 33]. Here is our second main result proving the weak convergence of $\omega_{\epsilon} \rightarrow \omega_{D}$ in the setting where $K_{X}+D$ is merely big.

Theorem 1.2. Let $X$ be a compact Kähler manifold and $D$ be a simple normal crossing divisor such that $K_{X}+D$ is big. Let $\omega_{\epsilon}$ be the Kähler-Einstein metric solving (1.2) for small $\epsilon>0$. Then, we have the weak convergence $\omega_{\epsilon} \rightarrow \omega_{D}$ as $\epsilon \rightarrow 0^{+}$in the sense of currents.

We note that Theorem 1.2 remains true in a slightly more general situation that $D=$ $\sum_{j=1}^{m} a_{j} D_{j}$ is a divisor whose support is simple normal crossing such that $a_{j} \leq 1$ for every $1 \leq j \leq m$. This can be proved essentially along the same line as in our proof of Theorem 1.2. To simplify the presentation, we only consider a simple normal crossing divisor $D$ as above.

In our proof, we actually don't need the existence of solutions for (1.1) from [8] and directly show that the sequence of potentials of $\left(\omega_{\epsilon}\right)_{\epsilon}$ is convergent in $L^{1}$ as $\epsilon \rightarrow 0^{+}$(we indeed prove a much stronger property that the sequence of potentials is decreasing in capacity, see Definition 2.3) and the limit current will solve the equation (1.1).

As far as we know, although it was known when the cohomology class $K_{X}+(1-\epsilon) D$ is big and nef ([10]), it is still open whether the metric $\omega_{\epsilon}$ is, in general, a genuine metric on the complement of some proper analytic subset in $X$. Thus, we could not for the moment address the question of local smooth convergence of $\omega_{\epsilon} \rightarrow \omega_{D}$ as $\epsilon \rightarrow 0^{+}$. We would like to point out, however, that the weak convergence of a sequence of metrics as currents is usually the first step in proving the $\mathcal{C}^{\infty}$ convergence locally outside a proper analytic subset in $X$.

In [9], under the assumption that $c_{1}\left(K_{X}+(1-\epsilon) D\right)$ is semi-positive, the authors were able to use the domination principle to show that a suitably normalized sequence of potentials $\left(u_{\epsilon}\right)_{\epsilon}$ is essentially decreasing to $u_{D}$, hence obtaining the desired $L^{1}$ convergence. In another context where $K_{X}+D$ is ample, the $L^{1}$ convergence of potentials of $\omega_{\epsilon}$ was proved in [31], using a variational approach. Both these assumptions are not available in our setting.

We now comment on our proofs of the main results. The proof of Theorem 1.1 is based on a uniform lower bound for solutions of certain classes of complex Monge-Ampère
equations whose proof uses an idea from [21]. The almost-completeness of $\omega_{D}$ is deduced from a more or less standard uniform $\mathcal{C}^{\infty}$-estimates for Monge-Ampère equations. For the uniqueness of $\omega_{D}$, we need a slightly more general version of Yau's Schwarz lemma for singular Kähler-Einstein metric, see Theorem 4.1 below for details.

The proof of Theorem 1.2 is much more involved because there is no available uniform $\mathcal{C}^{\infty}$-estimates (recall that $K_{X}+D$ is only big). We will indeed prove a more general result (Theorem 5.1 below) about the stability of complex Monge-Ampère equations. In contrast to some well-known non-collapsing situations where the $L^{1}$ convergence of potentials of metrics is relatively easy to establish, the difficulty in our present setting (i.e., in Theorem 5.1) lies in the fact that the complex Monge-Ampère equation corresponding to (1.2) has the measure on the right-hand side of unbounded mass on $X$ if $\epsilon=0$. Because of this reason, the expected $L^{1}$ convergence was obtained in previous works only under some additional assumption.

The strategy of our proof of Theorem 5.1 is to show that in the absence of any additional positivity (except the minimal assumption that $K_{X}+D$ is big, one can still use a sort of domination principle to obtain a quasi-decreasing property of potentials of metrics in consideration, hence, get the desired convergence. The version of the domination principle we need is the quantitative one obtained recently in [25] (see Theorem 5.1 in Section 2). It is robust enough to allow one to compare quasi-plurisubharmonic functions under relatively relaxed situations.

Aknowledgment. The authors would like to thank Henri Guenancia for fruitful discussions. Duc-Viet Vu is partially supported by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation)-Projektnummer 500055552 and by the ANR-DFG grant QuaSiDy, grant no ANR-21-CE40-0016. Part of this work was done when Quang-Tuan Dang was visiting the Department of Mathematics and Computer Science at the University of Cologne.

Conventions. The notations $\lesssim, \gtrsim$ stand for inequalities up to a multiplicative uniform positive constant. We use $C$ for a positive constant, whose value may change from line to line. For a divisor $D$, in some context we simply write $D$ instead of its support $\operatorname{Supp}(D)$. Denote $\mathrm{d}=\partial+\bar{\partial}$ and $d^{c}=\frac{i}{2 \pi}(\bar{\partial}-\partial)$ so that $d d^{c}=\frac{i}{\pi} \partial \bar{\partial}$.

Ethics declarations The author declares no conflict of interest.

\section*{2 Quantitative domination principle}

In this section, we recall the quantitative domination principle obtained in [25]. Let $X$ be a $n$-dimensional compact Kähler manifold equipped with a Kähler metric $\omega$. A function $u: X \rightarrow \mathbb{R} \cup\{-\infty\}$ is quasi-plurisubharmonic (qpsh) if it can be locally written as the sum of a plurisubharmonic function and a smooth function. Let $\theta$ be a smooth closed real (1, 1)-form. We say that $u$ is $\theta$-plurisubharmonic ( $\theta$-psh) if it is qpsh and $\theta_{u}:=d d^{c} u+\theta \geq 0$ in the sense of currents. We let $\operatorname{PSH}(X, \theta)$ denote the set of $\theta$-psh functions on $X$. Recall
that the cohomology class $\{\theta\}$ is big if there exists $\rho \in \operatorname{PSH}(X, \theta)$ such that $d d^{c} \rho+\theta \geq \delta \omega$ for some small constant $\delta>0$.

A $\theta$-psh function $u$ is said to have minimal singularities if it is less singular than any other $\theta$-psh function. Define
$$V_{\theta}:=\sup \{\varphi \in \operatorname{PSH}(X, \theta): \varphi \leq 0\} .$$
One can see that $V_{\theta}$ is a $\theta$-psh function with minimal singularities. Let $u_{1}, \ldots, u_{p}$, for $1 \leq p \leq n$ be $\theta$-psh functions and put $\theta_{u_{j}}:=d d^{c} u_{j}+\theta$. We recall how to define the non-pluripolar product $\theta_{u_{1}} \wedge \cdots \wedge \theta_{u_{n}}$. We write locally $\theta_{u_{j}}=d d^{c} v_{j}$, where $v_{j}$ is psh. By [6, 10], one knows that the sequence of positive currents
$$\mathbf{1}_{\cap_{j=1}^{p}\left\{v_{j}>-k\right\}} d d^{c} \max \left\{v_{1},-k\right\} \wedge \cdots \wedge d d^{c} \max \left\{v_{p},-k\right\}$$
is increasing in $k \in \mathbb{N}$ and converges to a closed positive current, which is independent of the choice of local potentials $v_{j}$ 's. Thus we obtain a well-defined global closed positive current on $X$ which is called the non-pluripolar product $\theta_{u_{1}} \wedge \cdots \wedge \theta_{u_{p}}$ of $\theta_{u_{1}}, \ldots, \theta_{u_{p}}$. If $p=n$, the resulting positive $(n, n)$-current is a Borel measure putting no mass on pluripolar sets. For any $u \in \operatorname{PSH}(X, \theta)$, the non-pluripolar complex Monge-Ampère measure of $u$ is
$$\theta_{u}^{n}:=\left(d d^{c} u+\theta\right)^{n} .$$
Given a potential $\phi \in \operatorname{PSH}(X, \theta)$, we let $\operatorname{PSH}(X, \theta, \phi)$ denote the set of $\theta$-psh functions $u$ such that $u \leq \phi$. We also define by $\mathcal{E}(X, \theta, \phi)$ the set of $u \in \operatorname{PSH}(X, \theta, \phi)$ of full Monge-Ampère mass with respect to $\phi$, i.e., $\int_{X} \theta_{u}^{n}=\int_{X} \theta_{\phi}^{n}$. When $\phi=V_{\theta}$ we simply denote by $\mathcal{E}(X, \theta)$. The volume of a big class $\{\theta\}$ is defined by
$$\operatorname{vol}(\{\theta\}):=\int_{X} \theta_{V_{\theta}}^{n} .$$
In this case, a $\theta$-psh function $u$ is said to have full Monge-Ampère mass if $\int_{X} \theta_{u}^{n}=\operatorname{vol}(\theta)$.
The following is a version of the domination principle.
Proposition 2.1 (Non-quantitative domination principle). Let $u \in \mathcal{E}(X, \theta)$ and $v \in \operatorname{PSH}(X, \theta)$. If $e^{-v} \theta_{v}^{n} \geq e^{-u} \theta_{u}^{n}$ then $u \geq v$.

Proof. For every $a>0$, we set $v_{a}=\max (u, v-a)$. By assumptions, we have $\theta_{u}^{n} \leq e^{-a} \theta_{v}^{n}$ on the set $\{u<v-a\}$. The locality of the complex Monge-Ampère measure with respect to the plurifine topology and the comparison principle yields
$$\int_{\left\{u<v_{a}\right\}} \theta_{u}^{n} \leq \int_{\left\{u<v_{a}\right\}} e^{-a} \theta_{v_{a}}^{n} \leq \int_{\left\{u<v_{a}\right\}} e^{-a} \theta_{u}^{n}$$
This means that $u \geq v_{a}$ a.e- $\theta_{u}^{n}$. By the domination principle [16, Proposition 3.11] we obtain $u \geq v_{a}$, hence $u \geq v-a$ on $X$. Since the latter holds for every $a>0$, we get $u \geq v$ as desired. \(\square\)

We now recall a particular case of the quantitative domination principle established in [25]. Let $\mathcal{W}^{-}$be the set of convex, non-decreasing functions $\chi: \mathbb{R}_{\leq 0} \rightarrow \mathbb{R}_{\leq 0}$ such that $\chi(0)=0$ and $\chi(-\infty)=-\infty$. Let $\theta$ be a closed smooth (1, 1)-form in a big cohomology class. Let $V_{\theta}$ be the $\theta$-psh function with minimal singularities defined above. Let $\varrho:=\int_{X} \theta_{V_{\theta}}^{n}>0$, which is the volume of the cohomology class of $\theta$. For $\chi \in \mathcal{W}^{-}$and $u \in \mathcal{E}(X, \theta)$, let
$$E_{\chi, \theta}^{0}(u):=-\varrho^{-1} \int_{X} \chi\left(u-V_{\theta}\right) \theta_{u}^{n}$$
which is called the (normalized) $\chi$-energy of $u$. For every Borel set $E$ in $X$, recall that the capacity of $E$ is given by
$$\operatorname{cap}(E)=\operatorname{cap}_{\omega}(E):=\sup \left\{\int_{E} \omega_{w}^{n}: w \in \operatorname{PSH}(X, \omega), 0 \leq w \leq 1\right\} .$$
Theorem 2.2 ([25, Theorem 4.4]). (Quantitative domination principle) Let $A \geq 1$ be a constant, and let $\theta \leq A \omega$ be a closed smooth real (1, 1)-form in a big cohomology class, and $\varrho:=\int_{X} \theta_{V_{\theta}}^{n}>0$. Let $B \geq 1$ be a constant, $u_{1}, u_{2} \in \mathcal{E}(X, \theta)$ and $\tilde{\chi} \in \mathcal{W}^{-}$such that $\tilde{\chi}(-1)=-1$ and
$$E_{\tilde{\chi}, \theta}^{0}\left(u_{1}\right)+E_{\tilde{\chi}, \theta}^{0}\left(u_{2}\right) \leq B .$$
Assume that there exists a constant $0 \leq c<1$ and a Radon measure $\mu$ on $X$ satisfying
$$\theta_{u_{1}}^{n} \leq c \theta_{u_{2}}^{n}+\varrho \mu$$
on $\left\{u_{1}<u_{2}\right\}$ and $c_{\mu}:=\int_{\left\{u_{1}<u_{2}\right\}} d \mu \leq 1$. Then there exists a constant $C>0$ depending only on $n, X$ and $\omega$ such that
$$\operatorname{cap}_{\omega}\left\{u_{1}<u_{2}-\epsilon\right\} \leq \frac{C \operatorname{vol}(X)(A+B)^{2}}{\epsilon(1-c) h^{\circ n}\left(1 / c_{\mu}\right)},$$
for every $0<\epsilon<1$, where $h(s)=(-\tilde{\chi}(-s))^{1 / 2}$ for every $0 \leq s \leq \infty$.
In particular, if $c_{\mu}=0$ then $\operatorname{cap}_{\omega}\left\{u_{1}<u_{2}-\epsilon\right\}=0$ for every $\epsilon>0$ and $u_{1} \geq u_{2}$ on $X$.
The standard domination principle (see, e.g., [16, Proposition 3.11]) corresponds to the case where $c=0$ and $\mu=0$. We underline that it is crucial for us in applications later that we consider the situation where $\mu \neq 0$.

We continue with some more auxiliary results about the continuity of Monge-Ampère operators. We now work in the local context. Let $\Omega$ be an open subset in $\mathbb{C}^{n}$ and $d \lambda$ denote the Lebesgue measure on $\mathbb{C}^{n}$. Let $\operatorname{PSH}(\Omega)$ denote the set of psh functions on $\Omega$.

Definition 2.3. Let $\left(w_{j}\right)_{j}$ be a sequence of Borel functions on $\Omega$. We say that $\left(w_{j}\right)_{j}$ is decreasing in capacity if for every open subset $U$ in $\Omega$, every compact $K \in U$, and for every constant $\delta>0$, for every $\epsilon>0$ there exists an index $j_{\epsilon}$ such that
$$\operatorname{cap}\left(\left\{w_{j}-w_{j^{\prime}} \leq-\delta\right\} \cap K, U\right) \leq \epsilon$$
if $j^{\prime} \geq j \geq j_{\epsilon}$.

We remark that the capacity in the above definition is in the sense of Bedford-Taylor [5]: for any Borel set $E \subset U$,
$$\operatorname{cap}(E, U):=\sup \left\{\int_{E}\left(d d^{c} u\right)^{n}: u \in \operatorname{PSH}(U), 0 \leq u \leq 1\right\} .$$

Proposition 2.4. Let $\left(w_{j}\right)_{j}$ be a sequence of uniformly bounded psh functions such that $\left(w_{j}\right)_{j}$ is decreasing in capacity, and $w_{j}$ converges to some bounded psh function $w$ in $L_{\text {loc }}^{1}$ as $j \rightarrow \infty$. Then we have $\left(d d^{c} w_{j}\right)^{k} \rightarrow\left(d d^{c} w\right)^{k}$ as $j \rightarrow \infty$ for every $1 \leq k \leq n$.

Proof. We argue as in the proof of the standard continuity of Monge-Ampère operators for decreasing sequences; see, e.g. [19]. Following the same lines in the aforementioned reference, we prove the desired limit by induction and assume now that $\left(d d^{c} w_{j}\right)^{k-1}$ converges weakly to $\left(d d^{c} w\right)^{k-1}$ as $j \rightarrow \infty$. To check the desired assertion for $k$, it suffices to show that $w_{j}\left(d d^{c} w_{j}\right)^{k-1}$ converges weakly to $w\left(d d^{c} w\right)^{k-1}$. Observe that we already have that any limit current of the sequence $w_{j}\left(d d^{c} w_{j}\right)^{k-1}$ is bounded from above by $w\left(d d^{c} w\right)^{k-1}$ by the induction hypothesis and Hartogs' lemma.

We can, without loss of generality, assume that $-2 \leq w_{j} \leq-1$ and $-2 \leq w \leq-1$. Denote by $w_{j}^{\epsilon}$ the standard regularization of $w_{j}$ by using convolution; cf. [19]. The problem is local. We can thus assume that $\Omega$ is the unit ball in $\mathbb{C}^{n}$. Let $\psi(z):=|z|^{2}-1$. We can assume that all $w_{j}, w_{j}^{\epsilon}$ and $w$ coincide with $A \psi$ outside a compact $K$ in $\Omega$, where $A$ is a constant big enough. We set $\beta:=d d^{c} \psi>0$, which is the standard Kähler form in $\mathbb{C}^{n}$. Let $\delta>0, \epsilon>0$ be constants. Choose an index $j_{\epsilon, \delta}$ so that for every $j \geq j_{\epsilon, \delta}$,
$$\operatorname{cap}\left(\left\{w_{j}-w \leq-\delta\right\} \cap K, \Omega\right) \leq \epsilon$$
Thus there exists a constant $C>0$ independent of $\delta, \epsilon$ such that for every $j \geq j_{\epsilon, \delta}$ we have
$$\begin{aligned}
\int_{\Omega} w\left(d d^{c} w\right)^{k-1} \wedge \beta^{n-k+1} \leq & \int_{\Omega}\left(w_{j}+\delta\right)\left(d d^{c} w\right)^{k-1} \wedge \beta^{n-k-1} \\
& +C \operatorname{cap}\left(\left\{w_{j}-w \leq-\delta\right\} \cap K, \Omega\right) \\
\leq & \int_{\Omega}\left(w_{j}^{\epsilon}+\delta\right)\left(d d^{c} w\right)^{k-1} \wedge \beta^{n-k-1}+C \epsilon \\
\leq & \int_{\Omega} w d d^{c} w_{j}^{\epsilon} \wedge\left(d d^{c} w\right)^{k-2} \wedge \beta^{n-k+1}+C(\epsilon+\delta) \\
\leq & \int_{\Omega}\left(w_{j}^{\epsilon}+\delta\right) d d^{c} w_{j}^{\epsilon} \wedge\left(d d^{c} w\right)^{k-2} \wedge \beta^{n-k+1}+C(\epsilon+\delta)
\end{aligned}$$
Note that in the above estimates, we have used integration by parts and the fact that $w$ and $w_{j}^{\epsilon}$ both vanish on $\partial \Omega$. Repeating this argument, we obtain
$$\int_{\Omega} w\left(d d^{c} w\right)^{k-1} \wedge \beta^{n-k+1} \leq \int_{\Omega} w_{j}^{\epsilon}\left(d d^{c} w_{j}^{\epsilon}\right)^{k-1} \wedge \beta^{n-k+1}+C(\epsilon+\delta),$$
for $j \geq j_{\epsilon, \delta}$ and for some constant $C>0$ big enough but independent of $\epsilon$ and $j$. Letting $j \rightarrow \infty$, then $\epsilon \rightarrow 0$, and then $\delta \rightarrow 0$ we obtain
$$\int_{\Omega} w\left(d d^{c} w\right)^{k-1} \wedge \beta^{n-k+1} \leq \liminf _{j \rightarrow \infty} \int_{\Omega} w_{j}\left(d d^{c} w_{j}\right)^{k-1} \wedge \beta^{n-k+1} .$$
The proof is thus complete. \(\square\)

\section*{3 Uniform lower bounds}

Let $D$ be a simple normal crossing divisor in $X$. Let $h$ be a smooth Hermitian metric on $\mathcal{O}_{X}(D)$ and $s$ a section of $\mathcal{O}_{X}(D)$ defining $D$, normalized so that $|s|_{h} \leq 1$. Let $\alpha$ be a big cohomology class, and let $\theta$ be a smooth representative in $\alpha$. Let $\left(f_{j}\right)_{j \geq 1}$ be an increasing sequence of continuous nonnegative functions converging pointwise to $f \in \mathcal{C}^{0}(X)$ as $j \rightarrow \infty$ such that $f_{1} \not \equiv 0$. Let $\left(\theta_{j}\right)_{j \in \mathbb{N}}$ be a sequence of smooth closed ( 1,1 )-forms in big cohomology classes converging to $\theta$ in the $\mathcal{C}^{0}$ topology as $j \rightarrow \infty$. Assume that for every $j \geq 0$, there exists $u_{j} \in \mathcal{E}\left(X, \theta_{j}\right)$ solving the equation
$$\left(d d^{c} u_{j}+\theta_{j}\right)^{n}=e^{u_{j}}|s|_{h}^{-2} f_{j} \omega^{n} .$$
We have the following standard observation.
Lemma 3.1. There exists a constant $C>0$ such that $u_{j} \leq C$ for every $j$.
Proof. Let $c_{j}:=\int_{X} f_{j} \omega^{n}$ which converges to $c:=\int_{X} f \omega^{n}>0$ as $j \rightarrow \infty$. Let $A>0$ be such that $\theta_{j} \leq A \omega$ for all $j$. Since the set $\left\{u \in \operatorname{PSH}(X, A \omega): \sup _{X} u=0\right\}$ is compact in the $L^{1}$ topology, we have
$$\int_{X}\left(u_{j}-\sup _{X} u_{j}\right) f \omega^{n} \geq-C_{1}$$
for $C_{1}>0$ only depending on $A$ and the measure $f \omega^{n}$, cf. [29, Proposition 8.5]. By the monotonicity of the sequence $\left(f_{j}\right)$ we have
$$\begin{aligned}
\int_{X} u_{j} f_{j} \omega^{n} & =c_{j} \sup _{X} u_{j}+\int_{X}\left(u_{j}-\sup _{X} u_{j}\right) f_{j} \omega^{n} \\
& \geq c_{j} \sup _{X} u_{j}+\int_{X}\left(u_{j}-\sup _{X} u_{j}\right) f \omega^{n} \geq c_{j} \sup _{X} u_{j}-C_{1}
\end{aligned}$$
Using Jensen's inequality and the fact that $|s|_{h} \leq 1$, we have that
$$\begin{aligned}
\int_{X} u_{j} f_{j} \omega^{n} & \leq c_{j} \log \left(\frac{1}{c_{j}} \int_{X} e^{u_{j}} f_{j} \omega^{n}\right) \leq c_{j} \log \left(\frac{1}{c_{j}} \int_{X}\left(d d^{c} u_{j}+\theta_{j}\right)^{n}\right) \\
& =c_{j} \log \left(\frac{1}{c_{j}} \operatorname{vol}\left(\left\{\theta_{j}\right\}\right)\right) \leq C
\end{aligned}$$
for $C>0$ independent of $j$. This provides a uniform upper bound for $u_{j}$. \(\square\)

Our main result in this section is Proposition 3.4 providing a uniform lower bound for $u_{j}$. We use an idea in [21].

Let $\gamma \in(0,1 / 2]$ be a fixed constant. For a closed smooth form $\eta$, we denote by $\{\eta\}$ the cohomology class of $\eta$, and if $E$ is a divisor, we denote by $\{E\}$ the cohomology class of $E$.

Let $\mathcal{I}_{D}$ be the ideal sheaf defining $D$. Since $\{\theta\}$ is big, we can find a Kähler current $T=d d^{c} \rho+\theta$ in $\alpha$ such that $T \geq \delta \omega$ for some $\delta>0$. It follows from [20] that we can further assume that $T$ has analytic singularities, i.e., there exists $c>0$ such that locally on $X$
$$\rho=\frac{c}{2} \log \sum_{\ell=1}^{N}\left|f_{\ell}\right|^{2}+v$$
where $v$ is smooth and $f_{1}, \ldots, f_{N}$ are local holomorphic functions. The coherent ideal sheaf $\mathcal{I}_{T}$ locally generated by these functions is then globally defined.
Lemma 3.2. There exists $\pi=\pi_{\gamma}: \widehat{X} \rightarrow X$ a finite composition of blowups with smooth centers, a smooth Kähler form $\widehat{\omega}$ and an effective divisor $E$ on $\widehat{X}$ so that the following conditions are satisfied:
(i) the total transform $\pi^{*}\left(\mathcal{I}_{D} \cdot \mathcal{I}_{T}\right)$ of $\mathcal{I}_{D} \cdot \mathcal{I}_{T}$ is generated by a divisor $\tilde{D}$, and $\operatorname{Supp} \tilde{D} \cup$ $\operatorname{Supp} E$ is of simple normal crossings,
(ii)
$$\pi^{*}\{\theta\}=\{\widehat{\omega}\}+\{E\},$$
and
$$\int_{\widehat{X}} \widehat{\omega}^{n} \geq \operatorname{vol}(\{\theta\})-\gamma .$$
Proof. By [10, Proposition 1.19], there exists $\pi^{\prime}: \widehat{X}^{\prime} \rightarrow X$ a finite composition of blowups with smooth centers so that
$$\pi^{*}\{\theta\}=\left\{\widehat{\omega}^{\prime}\right\}+\left\{E^{\prime}\right\},$$
where $\widehat{\omega}^{\prime}$ is a Kähler form on $\widehat{X}^{\prime}$ and $E^{\prime}$ is an effective divisor, and
$$\int_{\widehat{X}} \widehat{\omega}^{\prime n} \geq \operatorname{vol}(\{\theta\})-\gamma / 2 .$$
Let $E^{\prime}$ be the exceptional divisor of $\pi^{\prime}$ and $\mathcal{I}_{E^{\prime}}$ be the ideal sheaf generated by $E^{\prime}$. By performing some more blowups to principalize $\mathcal{I}_{E} \cdot \pi^{\prime *} \mathcal{I}_{D} \cdot \mathcal{I}_{T}$, we obtain a composition of blowups $\pi^{\prime \prime}: \widehat{X} \rightarrow \widehat{X}^{\prime}$ so that if $\pi:=\pi^{\prime \prime} \circ \pi$, then $\pi^{*} \mathcal{I}_{D} \cdot \mathcal{I}_{T}$ is given by some divisor $\tilde{D}$ with simple normal crossings support and the support of this divisor also has a simple normal crossing with exceptional divisors. Repeating the arguments from [10, Proposition 1.19] shows that $\pi$ satisfies the required properties. \(\square\)

We denote by $\widehat{D}$ the support of the divisor generating $\pi^{*} \mathcal{I}_{D}$. Hence, $\widehat{D}$ is of simple normal crossings. Let $E$ be the exceptional divisor of $\pi$ defined in Lemma 3.2. Let
$$\mu_{j}:=f_{j}|s|_{h}^{-2} \omega^{n} .$$
Since $u_{j} \in \mathcal{E}\left(X, \theta_{j}\right)$ is the solution of the equation
$$\left(d d^{c} u_{j}+\theta_{j}\right)^{n}=e^{u_{j}} \mu_{j},$$
we get
$$\left(d d^{c}\left(u_{j} \circ \pi\right)+\pi^{*} \theta_{j}\right)^{n}=e^{u_{j} \circ \pi} \pi^{*} \mu_{j} .$$
Let $\widehat{s}$ be a section in $\mathcal{O}_{\widehat{X}}(\widehat{D})$ defining $\widehat{D}$. Let $\widehat{h}$ be a smooth Hermitian metric on $\mathcal{O}_{\widehat{X}}(\widehat{D})$ whose curvature is a $(1,1)$ form $\Theta_{\widehat{h}}(\widehat{D})$. We normalize $\widehat{h}$ so that $|\widehat{s}|_{\widehat{h}}$ is very small (to be made precise later). Denote $\widehat{\mu}_{j}:=\pi^{*} \mu_{j}$, and $\widehat{\mu}:=\pi^{*} \mu$ and
$$\widehat{f}_{j}:=\pi^{*} \mu_{j} /\left(|\widehat{s}|_{\widehat{h}}^{-2} \widehat{\omega}^{n}\right), \quad \widehat{f}:=\pi^{*} \mu /\left(|\widehat{s}|_{\widehat{h}}^{-2} \widehat{\omega}^{n}\right) .$$
With these notations, we have $\widehat{\mu}_{j}=\widehat{f}_{j}|\widehat{s}|_{\widehat{h}}^{-2} \widehat{\omega}^{n}, \widehat{\mu}=\widehat{f}|\widehat{s}|_{\widehat{h}}^{-2} \widehat{\omega}^{n}$.

Lemma 3.3. We have that $\widehat{f}_{j}, \widehat{f}$ are continuous functions and $\widehat{f}_{j}$ increases pointwise to $\widehat{f}$.
Proof. It suffices to work locally. Let $\left(\widehat{z}_{1}, \ldots, \widehat{z}_{n}\right)$ be a local coordinate system around a point $\widehat{a}$ in $\widehat{X}$ and $\left(z_{1}, \ldots, z_{n}\right)$ be a local coordinate system around $\pi(\widehat{a})$ such that
\begin{itemize}
\item[(i)] $s(z)=z_{1} \cdots z_{k}$ near $\pi(\widehat{a})$,
\item[(ii)] $\widehat{D}$ is given near $\widehat{a}$ by the equation $\widehat{z}_{1} \cdots \widehat{z}_{m}=0$,
\item[(iii)] $z_{j} \circ \pi=\widehat{z}_{1}^{r_{1 j}} \cdots \widehat{z}_{m}^{r_{m j}}$ for $1 \leq j \leq k$, and some positive integers $r_{1 j}, \ldots, r_{m j}$.
\end{itemize}
Note that in (iii), since $\pi$ is a finite composition of blow-ups with smooth centers, the integers are independent of the choice of local charts; see, e.g., [27, page 184].

It follows that
$$\pi^{*}\left(d z_{j} \wedge d \bar{z}_{j}\right)=\sum_{1 \leq p, q \leq m} a_{p q}{\widehat{z_{p}}}^{-1} \overline{\widehat{z}}_{q}^{-1}\left|z_{j} \circ \pi\right|^{2} d \widehat{z}_{p} \wedge d \overline{\overline{z_{q}}},$$
for some constants $a_{p q}$ and $1 \leq j \leq k$. Hence
$$\pi^{*} \omega^{n}=a \prod_{j=1}^{k}\left|z_{j} \circ \pi\right|^{2} \prod_{j=1}^{m}\left|\widehat{z}_{j}\right|^{-2} \widehat{\omega}^{n}=a^{\prime}|s \circ \pi|_{h}^{2}|\widehat{s}|_{\widehat{h}}^{-2} \widehat{\omega}^{n},$$
where $a$ and $a^{\prime}$ are smooth functions. We deduce that $\widehat{f}=a^{\prime}(f \circ \pi), \widehat{f_{j}}=a^{\prime}\left(f_{j} \circ \pi\right)$. Therefore, $\widehat{f}_{j}, \widehat{f}$ are continuous functions, and $\widehat{f}_{j}$ increases pointwise to $\widehat{f}$ as desired. \(\square\)

Since $\pi^{*} \theta-\widehat{\omega}$ is cohomologous to $[E]$, we get
$$d d^{c} \varphi_{E}+\pi^{*} \theta-\widehat{\omega}=[E]$$
for some negative ( $\pi^{*} \theta-\widehat{\omega}$ )-psh function $\varphi_{E}$. Set
$$\widehat{\phi}:=-(n+2) \log \left(-\log |\widehat{s}|_{\widehat{h}}^{2}\right)+\varphi_{E} .$$
We compute
$$d d^{c} \widehat{\phi}=-\frac{(n+2) \Theta_{\widehat{h}}(\widehat{D})}{\left(-\log |\widehat{s}|_{\widehat{h}}^{2}\right)}+(n+2) \frac{d \log |\widehat{s}|_{\widehat{h}}^{2} \wedge d^{c} \log |\widehat{s}|_{\widehat{h}}^{2}}{\left(-\log |\widehat{s}|_{\widehat{h}}^{2}\right)^{2}}+[E]+\widehat{\omega}-\pi^{*} \theta .$$
For simplicity, we will omit the subscript $\widehat{h}$. Consequently, we have
$$d d^{c} \widehat{\phi}+\pi^{*} \theta \geq 3 \widehat{\omega} / 4$$
because $|\widehat{s}|$ is very small. Moreover, there holds
$$e^{\widehat{\phi}} \widehat{\mu} \leq \frac{\widehat{f} \widehat{\omega}^{n}}{|\widehat{s}|^{2}\left(-\log |\widehat{s}|^{2}\right)^{n+2}} \lesssim g \widehat{\omega}^{n}, \quad \text { where } g=\frac{1}{|\widehat{s}|^{2}\left(-\log |\widehat{s}|^{2}\right)^{n+2}}$$
By the argument in [21, Lemma 4.6] the density $g$ satisfies
$$\int_{\widehat{X}} g|\log g|^{n+1 / 2} \widehat{\omega}^{n}<\infty .$$

Indeed, $\log \left(-\log |\widehat{s}|^{2}\right)$ can be absorbed by the more singular one $-\log |\widehat{s}|^{2}$. The integral is dominated by
$$C \int_{\widehat{X}} \frac{1}{|\widehat{s}|^{2}(-\log |\widehat{s}|)^{n+2}}(-\log |\widehat{s}|)^{n+1 / 2} \widehat{\omega}^{n} \lesssim \int_{\widehat{X}} \frac{\widehat{\omega}^{n}}{|\widehat{s}|^{2}(-\log |\widehat{s}|)^{3 / 2}} .$$
Since $\widehat{D}$ has snc support, and $|\widehat{s}|<1$, it suffices to check that on the unit polydisc $\Delta^{n} \subset \mathbb{C}^{n}$, the integral
$$\int_{\Delta^{n}} \frac{d V_{\mathbb{C}^{n}}}{\prod_{i=1}^{k}\left|z_{i}\right|^{2}\left(-\log \left|z_{i}\right|\right)^{3 / 2}}$$
converges. Using polar coordinates, the conclusion follows from $\int_{0}^{1} \frac{d r}{r(-\log r)^{3 / 2}}<\infty$.
By [37] or [21, Theorem 1.5], we can find $\varphi$ a bounded $\widehat{\omega} / 2$-psh function satisfying
$$\left(d d^{c} \varphi+\widehat{\omega} / 2\right)^{n}=e^{\varphi+\widehat{\phi}} \widehat{\mu}$$
We note that $\varphi$ is bounded globally. Define
$$\widehat{\psi}_{\gamma}:=\varphi+\widehat{\phi}$$
which is a $\pi^{*} \theta_{j}$-psh function for $j \geq j_{\gamma}$ large enough since it follows from (3.6) that
$$d d^{c} \widehat{\psi}_{\gamma}+\pi^{*} \theta \geq d d^{c} \varphi+3 \widehat{\omega} / 4 \geq \widehat{\omega} / 4,$$
and $\pi^{*} \theta_{j}-\pi^{*} \theta \leq \widehat{\omega} / 4$ for $j$ big enough (depending on $\gamma$ ).
Proposition 3.4. For any $\gamma>0$, we have
$$u_{j} \circ \pi \geq \widehat{\psi}_{\gamma},$$
for $j \geq j_{\gamma}$. Moreover, there exists a smooth Hermitian metric $\widehat{h}$ (depending on $\gamma$ ) on $\mathcal{O}_{\widehat{X}}(\widehat{D})$ such that
$$\int_{\widehat{X}}\left(d d^{c} \widehat{\psi}_{\gamma}+\pi^{*} \theta_{j}\right)^{n} \geq \operatorname{vol}\left(\left\{\theta_{j}\right\}\right)-2 \gamma$$
for $j$ big enough (depending on $\gamma$ ).
Proof. Observe that
$$\left(d d^{c} \widehat{\psi}+\pi^{*} \theta_{j}\right)^{n} \geq\left(d d^{c} \varphi+\widehat{\omega} / 2\right)^{n}=e^{\varphi+\widehat{\phi}} \widehat{\mu} .$$
The domination principle (note that $\widehat{\psi}$ might not be of full mass, but $u_{j}$ is so) yields the first desired assertion. Indeed, from the above inequality, we have
$$e^{-\widehat{\psi}}\left(d d^{c} \widehat{\psi}+\pi^{*} \theta_{j}\right)^{n} \geq e^{-u_{j} \circ \pi}\left(d d^{c} u_{j} \circ \pi+\pi^{*} \theta_{j}\right)^{n} .$$
Therefore, $u_{j} \circ \pi \geq \widehat{\psi}$ on $\widehat{X}$ by Proposition 2.1.
We now check the second desired assertion. Put $v_{1}:=-(n+2) \log \left(-\log |\widehat{s}|_{\widehat{h}}^{2}\right)$, and $v_{2}:=\log |\widehat{s}|_{\widehat{h}}^{2}$. We choose $\widehat{h}$ so that $|\widehat{s}|_{\widehat{h}}^{2}$ is so small that $v_{2}$ is $\gamma \widehat{\omega}$-psh function with $\gamma \in(0,1 / 2]$,
and $v_{1} \geq-\left(-v_{2}\right)^{1 / 2}-C$ by the elementary inequality $(n+2) \log y+O(1) \leq y^{1 / 2}$ for $y>0$. It follows that $-\left(-v_{2}\right)^{1 / 2} \in \mathcal{E}(\widehat{X}, \gamma \widehat{\omega})$ (by [14, Example 2.7]), hence, $v_{1} \in \mathcal{E}(\widehat{X}, \gamma \widehat{\omega})$, cf. [28, Proposition 1.6]. Direct computations show
$$\begin{aligned}
d d^{c} \widehat{\psi}_{\gamma}+\pi^{*} \theta & =d d^{c} v_{1}+d d^{c} \varphi_{E}+d d^{c} \varphi+\pi^{*} \theta \\
& \geq\left(d d^{c} v_{1}+\gamma \widehat{\omega}\right)+\left(d d^{c} \varphi+\widehat{\omega} / 2\right)+(1-\gamma-1 / 2) \widehat{\omega}
\end{aligned}$$
using the equality (3.4) in the last inequality. Let $R$ be the right-hand side of the last inequality. Since $v_{1} \in \mathcal{E}(\widehat{X}, \gamma \widehat{\omega})$ and $\varphi \in \mathcal{E}(\widehat{X}, \widehat{\omega} / 2)$ (defined in (3.7)), one infers that
$$\int_{\widehat{X}} R^{n}=\int_{\widehat{X}} \widehat{\omega}^{n} \geq \operatorname{vol}(\{\theta\})-\gamma .$$
Consequently
$$\int_{\widehat{X}}\left(d d^{c} \widehat{\psi}_{\gamma}+\pi^{*} \theta\right)^{n} \geq \operatorname{vol}(\{\theta\})-\gamma .$$
Since $\theta_{j}$ is close to $\theta$ in the sup norm, we deduce that
$$\int_{\widehat{X}}\left(d d^{c} \widehat{\psi}_{\gamma}+\pi^{*} \theta_{j}\right)^{n} \geq \operatorname{vol}\left(\left\{\theta_{j}\right\}\right)-2 \gamma$$
for $j \geq j_{\gamma}$ big enough. We note that $\pi^{*} \theta_{j} \rightarrow \pi^{*} \theta$ in the $\mathcal{C}^{0}$ topology as $j \rightarrow \infty$. This finishes the proof. \(\square\)

Corollary 3.5. Let $u$ be a $L^{1}$ limit of $\left(u_{j}\right)_{j}$ as $j \rightarrow \infty$. Then $u \in \mathcal{E}(X, \theta)$ and
$$\left(d d^{c} u+\theta\right)^{n} \geq e^{u} f|s|_{h}^{-2} \omega^{n} .$$
Proof. Without loss of generality, we can assume that $u_{j} \rightarrow u$ in $L^{1}$. Let $\epsilon>0$ be a constant, and $\theta_{\epsilon}^{\prime}:=\theta+\epsilon \omega$. Let $j_{\epsilon} \in \mathbb{N}$ be such that $\theta_{j} \leq \theta_{\epsilon}^{\prime}$ for every $j \geq j_{\epsilon}$. Fixing $\gamma \in(0,1 / 2]$, we consider the modification $\pi: \widehat{X} \rightarrow X$ as in Lemma 3.2, and $\widehat{\psi}_{\gamma}$ is defined in (3.8). Let $\psi_{\gamma}:=\pi_{*} \widehat{\psi}_{\gamma}$ which is a $\theta_{j}$-psh function for $j$ large enough. It follows that $\psi_{\gamma}$ is $\theta_{\epsilon}^{\prime}$-psh and $d d^{c} \psi_{\gamma}+\theta_{\epsilon}^{\prime} \geq d d^{c} \psi_{\gamma}+\theta_{j}$ for $j \geq j_{\epsilon}$. Since $\pi$ is a bimeromorphic map, one obtains
$$\int_{X}\left(d d^{c} \psi_{\gamma}+\theta_{j}\right)^{n}=\int_{\widehat{X}}\left(d d^{c} \widehat{\psi}_{\gamma}+\pi^{*} \theta_{j}\right)^{n}$$
By this and Proposition 3.4, we get $u \geq \psi_{\gamma}$ and
$$\int_{X}\left(d d^{c} \psi_{\gamma}+\theta_{j}\right)^{n} \geq \operatorname{vol}(\{\theta\})-2 \gamma .$$
This, combined with the monotonicity of non-pluripolar products (see [16]), gives
$$\begin{aligned}
\int_{X}\left(d d^{c} u+\theta_{\epsilon}^{\prime}\right)^{n} & \geq \int_{X}\left(d d^{c} \psi_{\gamma}+\theta_{\epsilon}^{\prime}\right)^{n} \\
& \geq \int_{X}\left(d d^{c} \psi_{\gamma}+\theta_{j}\right)^{n} \geq \operatorname{vol}(\{\theta\})-2 \gamma
\end{aligned}$$
for every constant $\gamma>0$. Letting $\gamma \rightarrow 0$ gives
$$\int_{X}\left(d d^{c} u+\theta_{\epsilon}^{\prime}\right)^{n} \geq \operatorname{vol}(\{\theta\})$$
We underline here that since $u$ is independent of $\gamma$, we can take $\gamma \rightarrow 0$ in the above inequality. Taking $\epsilon \rightarrow 0$, we obtain $u \in \mathcal{E}(X, \theta)$.

It remains to check (3.10), whose proof is quite standard; see, e.g., [17, Lemma 2.8]. Since some slight modifications are needed (due to the fact that $\theta_{j}$ is not in the same cohomology class as $\theta$ ), we present the details for the reader's convenience. Let $u_{j}^{\prime}:=$ $\left(\sup _{k \geq j} u_{k}\right)^{*}$ which are $\theta_{\epsilon}^{\prime}$-psh for $j \geq j_{\epsilon}$. Note that $u_{j}^{\prime}$ decreases to $u$. By extracting a subsequence, if necessary, we can assume that
$$\left(d d^{c} u_{j}^{\prime}+\theta_{\epsilon}^{\prime}\right)^{n} \rightarrow \nu$$
weakly as $j \rightarrow \infty$. Since $u_{j}^{\prime}$ decreases to $u$, using [16, Theorem 2.3], we have
$$\nu \geq\left(d d^{c} u+\theta\right)^{n} .$$
Using this and the fact that $u \in \mathcal{E}(X, \theta)$, we obtain that
$$\begin{aligned}
\left\|\nu-\left(d d^{c} u+\theta\right)^{n}\right\| & \leq \nu(X)-\int_{X}\left(d d^{c} u+\theta\right)^{n} \\
& \leq \operatorname{vol}\left(\left\{\theta_{\epsilon}^{\prime}\right\}\right)-\operatorname{vol}(\{\theta\}) \lesssim \epsilon
\end{aligned}$$
where $\left\|\nu^{\prime}\right\|$ denotes the mass norm of a (signed) measure of $\nu^{\prime}$. On the other hand, for every continuous function $g$ with compact support in $X \backslash W$ ( $W$ is the union of $D$ and the non-Kähler locus of $\{\theta\}$ ), we have
$$g\left(d d^{c} u_{j}^{\prime}+\theta_{\epsilon}^{\prime}\right)^{n} \geq g e^{\inf _{k \geq j} u_{j}} f_{j}|s|_{h}^{-2} \omega^{n}$$
which converges to $g e^{u} f|s|_{h}^{-2} \omega^{n}$ as $j \rightarrow \infty$ by the Lebesgue dominated convergence theorem (note that $\inf _{k \geq j} u_{j}$ converges pointwise almost everywhere to $u$ ). Hence letting $j \rightarrow \infty$ gives
$$g \nu \geq g e^{u} f|s|_{h}^{-2} \omega^{n} .$$
Combining this with (3.12) implies
$$g\left(d d^{c} u+\theta\right)^{n} \geq g e^{u} f|s|_{h}^{-2} \omega^{n}-C\|g\|_{L^{\infty} \epsilon}$$
for every constant $\epsilon>0$. Letting $\epsilon \rightarrow 0$, we obtain the desired inequality. This finishes the proof. \(\square\)

Let $g$ be a function on $X$ and let $\eta$ be a smooth closed $(1,1)$-form in a pseudoeffective class. If there is a function $v \in \operatorname{PSH}(X, \eta)$ with $v \leq g$, then we define
$$P_{\eta}(g):=(\sup \{v \in \operatorname{PSH}(X, \eta): v \leq g\})^{*}$$
which is a well-defined $\eta$-psh function. Let $\epsilon>0$ be a small constant. Let $\theta_{\epsilon}^{\prime}:=\theta+\epsilon \omega$. Let $j_{\epsilon} \in \mathbb{N}$ be such that $\theta_{j} \leq \theta_{\epsilon}^{\prime}$ for every $j \geq j_{\epsilon}$. Hence $u_{j}$ is $\theta_{\epsilon}^{\prime}$-psh for $j \geq j_{\epsilon}$.

Corollary 3.6. Let
$$u_{j, \epsilon}^{\prime \prime}:=\lim _{k \rightarrow \infty} P_{\theta_{\epsilon}^{\prime}}\left(\min \left\{u_{j}, \ldots, u_{k}\right\}\right),$$
for $j \geq j_{\epsilon}$. Then $u_{j, \epsilon}^{\prime \prime}$ is a well-defined $\theta_{\epsilon}^{\prime}$-psh function and increases to some $\theta_{\epsilon}^{\prime}$-psh function $u_{\epsilon}^{\prime \prime}$ as $j \rightarrow \infty$ satisfying:
\begin{itemize}
\item[(i)] $u_{\epsilon}^{\prime \prime} \leq u$, where $u$ is a $L^{1}$-limit of the sequence $\left(u_{j}\right)_{j}$ as $j \rightarrow \infty$,
\item[(ii)] $u_{\epsilon}^{\prime \prime}$ decreases to some $\theta$-psh function $u^{\prime \prime} \in \mathcal{E}(X, \theta)$ as $\epsilon$ decreases to 0 .
\end{itemize}

Proof. Since $u_{j} \geq \psi_{\gamma}$ for $j \geq j_{\gamma}$ big enough (depending on $\gamma$ ), we see that $u_{j, \epsilon}^{\prime \prime}$ is well-defined for $j \geq j_{\gamma}$ because $\psi_{\gamma}$ is in the envelope defining $P_{\theta_{\epsilon}^{\prime}}\left(\min \left\{u_{j}, \ldots, u_{k}\right\}\right)$ for $k \geq j$ (and $\left(u_{j}\right)_{j}$ is bounded from above uniformly in $j$, see Lemma 3.1). The fact that $u_{j, \epsilon}^{\prime \prime}$ is increasing (for $\epsilon$ fixed) is clear. By the definition of the envelope $P_{\theta_{\epsilon}^{\prime}}$, one sees that $u_{\epsilon}^{\prime \prime}$ is decreasing as $\epsilon \searrow 0$. Since $u_{\epsilon}^{\prime \prime} \geq \psi_{\gamma}$, we see that $u^{\prime \prime}:=\lim _{\epsilon \rightarrow 0} u_{\epsilon}^{\prime \prime} \geq \psi_{\gamma}$ for every $\gamma \in(0,1 / 2]$. Using this and arguing as at the beginning of the proof of Corollary 3.5 (see (3.11)), we obtain
$$\int_{X}\left(d d^{c} u+\theta_{\epsilon}^{\prime}\right)^{n} \geq \operatorname{vol}(\{\theta\})-2 \gamma$$
for every $\gamma \in(0,1 / 2]$ and every constant $\epsilon>0$, where $\theta_{\epsilon}^{\prime}:=\theta+\epsilon \omega$. Letting $\gamma \rightarrow 0$ and then $\epsilon \rightarrow 0$ gives $u^{\prime \prime} \in \mathcal{E}(X, \theta)$. \(\square\)

\section*{4 Almost complete Kähler-Einstein metrics}

In this section, we prove Theorem 1.1. We begin by recalling the following definition for almost complete metrics. In what follows, we interchangeably use the terms Kähler forms and Kähler metrics. We start with a slightly more general version of Yau's Schwarz lemma for volume forms ([48] and also [43]).

Theorem 4.1. Let $\left(M, \eta_{1}\right)$ be a complete Kähler manifold with Ricci curvature bounded from below and the scalar curvature bounded from below by a constant $-\frac{n K_{1}}{2 \pi}$. Let $N$ be a complex manifold with $\operatorname{dim} N=\operatorname{dim} M$ and $\eta_{2}$ be a closed positive (1, 1)-current on $N$ having a well-defined Ricci curvature. Let $f: M \rightarrow N$ be a non-degenerate holomorphic map. Assume that the following conditions are satisfied:
\begin{itemize}
\item[(i)] $2 \pi \operatorname{Ric} \eta_{2} \leq-K_{2} \eta_{2}$ as currents for some constant $K_{2}>0$,
\item[(ii)] There exists a closed subset $E$ in $N$ such that $f^{-1}(E)$ is of zero Lebesgue measure in $M$, and $\eta_{2}$ is a smooth Kähler form on $N \backslash E$, and $\eta_{2}^{n}$ extends to a smooth form on $N$.
\end{itemize}

Then we have $K_{1} \geq 0$, and
$$f^{*} \eta_{2}^{n} \leq\left(\frac{K_{1}}{K_{2}}\right)^{n} \eta_{1}^{n}$$

We note that in (i) there is the factor $2 \pi$ because our Ric $\eta_{2}$ (see Introduction) is, in fact, equal to the $\frac{1}{2 \pi}$ times the usual Ricci curvature of the metric $\eta_{2}$.

Proof. The proof is almost identical to that of [43, Theorem. 1.2] (which goes back to [48]). Set
$$u:=\frac{f^{*} \eta_{2}^{n}}{\eta_{1}^{n}} .$$
Since $\eta_{2}^{n}$ is a smooth form on $N$, we see that $u$ is a well-defined nonnegative smooth function on $M$. Let $\Delta$ denote the Laplacian with respect to $\eta_{1}$. At any point $x \in M \backslash f^{-1}(E)$, we compute (recall $d d^{c}:=\frac{i}{\pi} \partial \bar{\partial}$ )
$$\begin{aligned}
\Delta u & =u \Delta \log u+\frac{|\nabla u|_{\eta_{1}}^{2}}{u} \\
& =\frac{2 n \pi d d^{c} \log u \wedge \eta_{1}^{n-1}}{\eta_{1}^{n}}+\frac{|\nabla u|_{\eta_{1}}^{2}}{u} \\
& =2\left(-\operatorname{tr}_{\eta_{1}} f^{*}\left(2 \pi \operatorname{Ric} \eta_{2}\right)+\operatorname{tr}_{\eta_{1}}\left(2 \pi \operatorname{Ric} \eta_{1}\right)\right) u+\frac{|\nabla u|_{\eta_{1}}^{2}}{u} \\
& \geq 2 K_{2} \operatorname{tr}_{\eta_{1}} f^{*} \eta_{2} \cdot u-2 n K_{1} \cdot u \\
& \geq 2 n K_{2} u^{1+\frac{1}{n}}-2 n K_{1} u,
\end{aligned}$$
using the arithmetic-geometric mean inequality. Since both sides of the last inequality are continuous on $M$, we infer
$$\Delta u \geq 2 n K_{2} u^{1+\frac{1}{n}}-2 n K_{1} u$$
on $M$. Now, it suffices to repeat arguments in [48, Pages 200-201] to obtain the desired estimate. \(\square\)

Recall that a closed positive (1, 1)-current on a complex manifold $M$ is said to be $a$ singular Kähler-Einstein metric of negative Ricci curvature on $M$ if $\eta$ has a well-defined Ricci curvature and Ric $\eta=-\eta$.

Definition 4.2. ([42] and also [13]) Let $M$ be a Kähler manifold and let $\eta$ be a singular Kähler-Einstein metric of negative Ricci curvature on $M$. We say that $\eta$ is almost complete if there exists a proper analytic subset $E \subset M$, and a sequence of complete smooth Kähler metrics $\omega_{j}$ on $M$ and a sequence of positive numbers $t_{j}$ converging to 1 such that the following conditions are fulfilled:
\begin{itemize}
\item[(i)] $\operatorname{Ric} \omega_{j} \geq-t_{j} \omega_{j}$ for every $j \in \mathbb{N}$,
\item[(ii)] $\eta$ is the limit of $\omega_{j}$ in the local $\mathcal{C}^{\infty}$ topology on $M \backslash E$ as $j \rightarrow \infty$,
\item[(iii)] $\eta$ is a smooth Kähler form on $M \backslash E$.
\end{itemize}

We stress that one should consider an almost-complete metric on $M$ rather than a smooth metric on $M \backslash E$. The key is the following property of almost-complete metrics.

Lemma 4.3 ([42]). Let $M$ be a Kähler manifold. Then there exists at most one almost complete Kähler-Einstein metric $\eta$ on $M$ with Ric $\eta=-\eta$.

Proof. We reproduce the proof from [42] for readers' convenience. Suppose that $\eta_{1}, \eta_{2}$ are two almost complete Kähler metrics on $M$ with Ric $\eta_{k}=-\eta_{k}$ for $k=1,2$. By definition,
there are sequences of complete Kähler metrics $\omega_{j k}$ and positive real numbers $t_{j k}$ converging to 1 such that
$$\operatorname{Ric} \omega_{j k} \geq-t_{j k} \omega_{j k}$$
and $\omega_{j k}$ converges to $\eta_{k}$ smoothly pointwise. By Theorem 4.1 applied to the identity map of $M$, we get
$$\eta_{1}^{n} \leq t_{j 2}^{n} \omega_{j 2}^{n}, \quad \eta_{2}^{n} \leq t_{j 1}^{n} \omega_{j 2}^{n}$$
for every $j \in \mathbb{N}$. Letting $j \rightarrow \infty$ and using the pointwise convergence of $\omega_{j k}$ to $\eta_{k}$ give $\eta_{1}^{n}=\eta_{2}^{n}$. Thus
$$\eta_{1}=-\operatorname{Ric} \eta_{1}=d d^{c} \log \eta_{1}^{n}=d d^{c} \log \eta_{2}^{n}=-\operatorname{Ric} \eta_{2}=\eta_{2} .$$
This finishes the proof. \(\square\)

Lemma 4.4. Let $D$ be a simple normal crossing divisor such that $K_{X}+D$ is big and nef. Let $s$ be a section of $\mathcal{O}_{X}(D)$ defining $D$ and $h$ be a smooth Hermitian metric on $\mathcal{O}_{X}(D)$. Let $\epsilon \in[0,1)$ and $f$ be a smooth function. Let $\theta$ be a smooth representative of big cohomology class $c_{1}\left(K_{X}+D\right)$. Let $v_{\epsilon} \in \mathcal{E}(X, \theta+\epsilon \omega)$ be the unique solution of the equation
$$\left(d d^{c} v_{\epsilon}+\theta+\epsilon \omega\right)^{n}=e^{v_{\epsilon}+f}|s|_{h}^{-2} \omega^{n} .$$
Let $E$ be the non-Kähler locus of $K_{X}+D$. Then the $\mathcal{C}^{k}$-norm of $v_{\epsilon}$ on compact subsets in $X \backslash(D \cup E)$ is uniformly bounded in $\epsilon$ for every $k$.

Proof. The domination principle (see Proposition 2.1) ensures that $v_{\epsilon}$ decreases to $v$ as $\epsilon \searrow 0$. It follows that $v_{\epsilon} \leq C$ for some uniform constant $C>0$. Theorem 5.1 shows that $v_{\epsilon}$ converges weakly toward $v$ as $\epsilon \rightarrow 0^{+}$. Moreover, $v$ belongs to $\mathcal{E}(X, \theta)$ and satisfies
$$\left(d d^{c} v+\theta\right)^{n}=e^{v+f}|s|_{h}^{-2} \omega^{n} .$$

We set $X_{0}:=X \backslash(D \cup E)$. We are going to prove that the family $\left(v_{\epsilon}\right)$ is precompact in $\mathcal{C}_{\text {loc }}^{\infty}\left(X_{0}\right)$, where $E$ is the non-ample locus of $K_{X}+D$. This amounts to establishing $\mathcal{C}_{\text {loc }}^{k}\left(X_{0}\right)$ estimates for all $k \in \mathbb{N}$ thanks to the Arzela-Ascoli theorem. According to the Evans-Krylov theory and Schauder interior estimates (the so-called bootstrapping arguments for elliptic PDEs), obtaining a local $L^{\infty}$ and Laplacian estimate on $X_{0}$ suffices. To do this, we repeat the estimates derived in [22, Sect. 5] with minor modifications.

Since $\theta$ represents a big cohomology class, we can find a $\theta$-psh function $\rho$ with analytic singularities such that $\rho \rightarrow-\infty$ near $E$ and $d d^{c} \rho+\theta \geq 2 \delta \omega$ for some $\delta>0$. We fix $c>0$ so small that $c d d^{c} \log |s|_{h}^{2}+\delta \omega \geq 0$. It follows from [15, Theorem. 3.1, Step 1] that
$$v \geq c \log |s|_{h}^{2}+\rho-C$$
for $C>0$ depending on $X, \omega, n, c, \delta$ and an upper bound for $\int_{X} e^{-2 P_{\omega}\left(c^{-1}\left(v-V_{\theta}\right)\right)} \omega^{n}$. Therefore, for every $\epsilon \in(0,1]$,
$$v_{\epsilon} \geq c \log |s|_{h}^{2}+\rho-C .$$

We are now in a position to establish the local Laplacian estimate. We recall Siu-Yau's inequality (cf. [40]): Let $\tau$ and $\tau^{\prime}$ are two Kähler forms on a complex manifold and let $F$ be defined by $\tau^{\prime n}=e^{F} \tau^{n}$. If the holomorphic bisectional curvature of $\tau$ is bounded from below by some constant $B>0$, then
$$\Delta_{\tau^{\prime}} \log \operatorname{tr}_{\tau}\left(\tau^{\prime}\right) \geq \frac{\Delta_{\tau} F}{\operatorname{tr}_{\tau}\left(\tau^{\prime}\right)}-B \operatorname{tr}_{\tau^{\prime}}(\tau) .$$

We are going to apply $\tau=\omega$ and $\tau^{\prime}=\omega_{\epsilon}^{\prime}:=d d^{c} v_{\epsilon}+\theta+\epsilon \omega$. We observe that the holomorphic bisectional curvature of $\omega$ is obviously bounded on $X$ by a constant $B>0$, hence we obtain the following inequality
$$\Delta_{\omega_{\epsilon}^{\prime}} \log \operatorname{tr}_{\omega}\left(\omega_{\epsilon}^{\prime}\right) \geq \frac{\Delta_{\omega}\left(v_{\epsilon}+F\right)}{\operatorname{tr}_{\omega}\left(\omega_{\epsilon}^{\prime}\right)}-B \operatorname{tr}_{\omega_{\epsilon}^{\prime}}(\omega),$$
where $F:=f-\log |s|_{h}^{2}$. We have $\Delta_{\omega} F \geq-n A$ on $X \backslash D$ for some uniform constant $A>0$. Moreover, one sees that
$$\Delta_{\omega} v_{\epsilon}=\operatorname{tr}_{\omega}\left(d d^{c} v_{\epsilon}+C_{0} \omega\right)-n C_{0} \geq-n C_{0},$$
for some uniform $C_{0}>0$. Combining this with the elementary inequality $\operatorname{tr}_{\omega}\left(\omega_{\epsilon}^{\prime}\right) \operatorname{tr}_{\omega_{\epsilon}^{\prime}}(\omega) \geq$ $n$, we obtain
$$\frac{\Delta_{\omega}\left(v_{\epsilon}+F\right)}{\operatorname{tr}_{\omega}\left(\omega_{\epsilon}^{\prime}\right)} \geq-\left(A+C_{0}\right) \operatorname{tr}_{\omega_{\epsilon}^{\prime}}(\omega) .$$
Plugging (4.4) into (4.3), we thus obtain
$$\Delta_{\omega_{\epsilon}^{\prime}} \log \operatorname{tr}_{\omega}\left(\omega_{\epsilon}^{\prime}\right) \geq-C_{1} \operatorname{tr}_{\omega_{\epsilon}^{\prime}}(\omega)$$
for $C_{1}=B+A+C_{0}$. We set $w_{\epsilon}:=v_{\epsilon}-c \log |s|_{h}^{2}-\rho$. By (4.2), we have that $w_{\epsilon}$ is bounded from below. We set
$$\omega_{\epsilon}:=d d^{c} c \log |s|_{h}^{2}+d d^{c} \rho+\theta+\epsilon \omega .$$
Since we have chosen $c>0$ so small that $d d^{c} c \log |s|_{h}^{2}+\delta \omega \geq 0$, hence $\omega_{\epsilon} \geq \delta \omega$ for every $\epsilon$. We observe that $\Delta_{\omega_{\epsilon}^{\prime}} w_{\epsilon}=n-\operatorname{tr}_{\omega_{\epsilon}^{\prime}} \omega_{\epsilon} \leq n-\delta \operatorname{tr}_{\omega_{\epsilon}^{\prime}} \omega$. Therefore, we obtain
$$\Delta_{\omega_{\epsilon}^{\prime}}\left(\log \operatorname{tr}_{\omega}\left(\omega_{\epsilon}^{\prime}\right)-\left(C_{1} \delta^{-1}+1\right) w_{\epsilon}\right) \geq \operatorname{tr}_{\omega_{\epsilon}^{\prime}}(\omega)-n\left(C_{1} \delta^{-1}+1\right) .$$
We are now in a position to apply the maximum principle. Indeed, if we put $C=C_{1} \delta^{-1}$ then since $w_{\epsilon}$ tends to $+\infty$ near $D \cup E$ the function $H:=\log \operatorname{tr}_{\omega}\left(\omega_{\epsilon}^{\prime}\right)-(C+1) w_{\epsilon}$ therefore attains its maximum at some point $x_{0} \in X_{0}$ (depending on $\epsilon$ ). At this point, the inequality (4.5) combined with the maximum principle yield $\operatorname{tr}_{\omega_{\epsilon}^{\prime}}\left(\omega_{\epsilon}\right)\left(x_{0}\right) \leq n(C+1)$. Using the elementary inequality $\operatorname{tr}_{\tau}\left(\tau^{\prime}\right) \leq n\left(\frac{\tau^{\prime n}}{\tau^{n}}\right)\left(\operatorname{tr}_{\tau^{\prime}}(\tau)\right)^{n-1}$ for any two Kähler forms $\tau, \tau^{\prime}$, one gets
$$\begin{aligned}
\log \operatorname{tr}_{\omega}\left(\omega_{\epsilon}^{\prime}\right) & \leq \log \operatorname{tr}_{\omega}\left(\omega_{\epsilon}^{\prime}\right)\left(x_{0}\right)+(C+1)\left(w_{\epsilon}-w_{\epsilon}\left(x_{0}\right)\right) \\
& \leq(n-1) \log n(C+1)+\log n+w_{\epsilon}\left(x_{0}\right)+F_{\epsilon}\left(x_{0}\right)+(C+1)\left(w_{\epsilon}-w_{\epsilon}\left(x_{0}\right)\right) \\
& \leq C_{3}+(C+1) w_{\epsilon}
\end{aligned}$$
since $w_{\epsilon}$ is uniformly bounded from below by (4.2). This implies that $H$ is uniformly bounded from above, hence
$$\operatorname{tr}_{\omega}\left(\omega_{\epsilon}^{\prime}\right) \leq C_{3} e^{-(C+1) \rho} \frac{1}{|s|_{h}^{2 c(C+1)}}$$
using that $v_{\epsilon}$ is uniformly bounded from above. Thus, we end up with uniformly (in $\epsilon$ ) positive constant $C>0$ such that
$$\left|\Delta_{\omega} v_{\epsilon}\right| \leq \frac{C e^{-C \rho}}{|s|_{h}^{2 C}} .$$
In particular, for any compact $K \subset \subset X_{0}$, one gets a uniform bound for $\left\|\Delta_{\omega} v_{\epsilon}\right\|_{L^{\infty}(K)}$. We can apply a complex version of the Evans-Krylov estimate, due to Trudinger [44] (cf. [40, Chap. 2] in this context) to obtain a local $\mathcal{C}^{\alpha}$ estimate on the metric $\omega_{\epsilon}^{\prime}$ for $0<\alpha<1$, i.e., $\left\|\Delta_{\omega} v_{\epsilon}\right\|_{\mathcal{C}^{2, \alpha}(K)} \leq C_{K}$ for a uniform constant $C_{K}>0$ (we also refer to [45] for a new proof). From this, we eventually differentiate the equation using Schauder estimates to obtain uniform estimates
$$\sup _{\epsilon \in(0,1]}\left\|v_{\epsilon}\right\|_{\mathcal{C}^{j, \alpha}(K)} \leq C_{j, \alpha}(K)<+\infty,$$
for each $0<\alpha<1, j \in \mathbb{N}$, which guarantee that $v_{\epsilon}$ is relatively compact in $\mathcal{C}_{\text {loc }}^{\infty}\left(X_{0}\right)$. The lemma is thus proved. \(\square\)

End of the proof of Theorem 1.1. Let $s$ be a section of $\mathcal{O}_{X}(D)$ defining $D$, and $h$ a smooth metric on $\mathcal{O}_{X}(D)$ such that $|s|_{h} \leq 1$. Let $\eta$ be the Chern form of $h$. Let $\{\omega\}$ denote the cohomology class of $\omega$.

Let $\theta$ be a smooth closed form in $c_{1}\left(K_{X}+D\right)$ and $\theta_{\epsilon}:=\theta+\epsilon \omega$ for $\epsilon \in[0,1]$ (hence $\left.\theta_{0}=\theta\right)$. Thus $\left(\theta_{\epsilon}\right)_{\epsilon}$ is a sequence of smooth closed forms such that $\theta_{\epsilon} \in c_{1}\left(K_{X}+D\right)+\epsilon\{\omega\}$ and $\theta_{\epsilon}$ converges to $\theta$ in $\mathcal{C}^{0}$-topology as $\epsilon \rightarrow 0$. For $0 \leq \epsilon \leq 1$, let $u_{\epsilon} \in \mathcal{E}\left(X, \theta_{\epsilon}\right)$ be the solution of
$$\left(d d^{c} u_{\epsilon}+\theta_{\epsilon}\right)^{n}=e^{2 u_{\epsilon}+2 F}|s|_{h}^{-2} \omega^{n},$$
where $F$ is a smooth function so that
$$\eta-\operatorname{Ric}(\omega)-\theta=-d d^{c} F .$$
We see that $\omega_{\epsilon}:=d d^{c} u_{\epsilon}+\theta+\epsilon \omega$ satisfies
$$\operatorname{Ric} \omega_{\epsilon}=-\omega_{\epsilon}+\epsilon \omega+[D]$$
and $\omega_{\epsilon}$ is of full Monge-Ampère mass in $c_{1}\left(K_{X}+D\right)+\epsilon\{\omega\}$ for $0 \leq \epsilon \leq 1$. Observe that the setting in Section 3 applies to $\left(u_{\epsilon}\right)_{\epsilon}$. Hence, by Corollary 3.5, we see that if $u$ is the $L^{1}$ limit of a subsequence $\left(u_{\epsilon_{j}}\right)_{j}$ as $j \rightarrow \infty$, then $u \in \mathcal{E}\left(X, \theta_{0}\right)$. Lemma 4.4 yields that $u_{\epsilon_{j}}$ also converges to $u$ in the local $\mathcal{C}^{\infty}$ topology in $X \backslash(D \cup E)$. Consequently, we get
$$\left(d d^{c} u+\theta_{0}\right)^{n}=e^{2 u+2 F}|s|_{h}^{-2} \omega^{n}$$
on $X \backslash(D \cup E)$. It follows that $u=u_{0}$ by uniqueness (see [10] or [23]). Consequently $u_{\epsilon}$ converges to $u_{0}$ as $\epsilon \rightarrow 0$ in $L^{1}$ and $u_{\epsilon}$ converges to $u_{0}$ in the local $\mathcal{C}^{\infty}$-topology in $X \backslash(D \cup E)$. Since $\omega_{\epsilon}$ is a complete smooth Kähler metric (by [35]) on $X \backslash D$ and Ric$\omega_{\epsilon} \geq-\omega_{\epsilon}$, we obtain that $\omega_{0}$ is almost-complete, and the uniqueness of $\omega_{0}$ follows from Lemma 4.3. The sought metric $\omega_{D}$ is exactly $\omega_{0}$ in the above discussion. This finishes the proof. \(\square\)

We end this section by presenting an example in which the non-Kähler locus of $K_{X}+D$ is not contained in $D$.

Example 4.5. Fix now a point $x_{0} \in \mathbb{P}^{2}$. Let $\pi=\pi_{x_{0}}: X \rightarrow \mathbb{P}^{2}$ be the blowup $\mathbb{P}^{2}$ at a given point $x_{0}$ and let $E$ be the exceptional divisor. Let $D^{\prime}=H_{1}+H_{2}+H_{3}+H_{4}$ be a smooth divisor in $\mathbb{P}^{2}$ where $H_{1}, H_{2}, H_{3}, H_{4}$ are hyperplanes in general position, and $x_{0} \in H_{1} \backslash\left(\cup_{j=2}^{4} H_{j}\right)$. Let $\pi^{*} D^{\prime}$ be the total transform of $D^{\prime}$ and let $D$ be the strict transform of $D^{\prime}$. They are both simple normal crossing divisors in $X$. By our choice of $x_{0}$, we get
$$\pi^{*} D^{\prime}=D+E .$$
Observe that $\pi^{*} K_{\mathbb{P}^{2}}=K_{X}-E$ (see, e.g., [27, page 187]) and $K_{\mathbb{P}^{2}}+D^{\prime}=\mathcal{O}_{\mathbb{P}^{2}}(1)$ which is a positive line bundle (see, e.g., [27, page 146]). We infer that
$$K_{X}+D=\pi^{*} K_{\mathbb{P}^{2}}+E+\pi^{*} D^{\prime}-E=\pi^{*}\left(K_{\mathbb{P}^{2}}+D^{\prime}\right)=\pi^{*} \mathcal{O}_{\mathbb{P}^{2}}(1)$$
which is a semi-ample and big line bundle on $X$. One can see that $E$ is equal to the non-Kähler locus of $K_{X}+D$, but is not contained in $D$.

\section*{5 Stability of complex Monge-Ampère equations}

The goal of this section is to prove the following result.
Theorem 5.1. Let $D$ be a simple normal crossing divisor in $X$. Let $s$ be a section of $\mathcal{O}_{X}(D)$ defining $D$ and $h$ be a smooth Hermitian metric on $\mathcal{O}_{X}(D)$ such that $|s|_{h}<1$. Let $\alpha$ be a big cohomology class and $\theta$ be a smooth representative in $\alpha$. Let $\left(f_{j}\right)_{j}$ be an increasing sequence of continuous nonnegative functions such that $f_{1} \not \equiv 0$, and $f_{j}$ converges pointwise to $f \in \mathcal{C}^{0}(X)$ as $j \rightarrow \infty$. Let $\left(\theta_{j}\right)_{j \in \mathbb{N}}$ be a sequence of smooth closed ( 1,1 )-forms in big cohomology classes converging to $\theta$ in the $\mathcal{C}^{0}$ topology as $j \rightarrow \infty$. Let $u_{j} \in \mathcal{E}\left(X, \theta_{j}\right)$ be a solution of the equation
$$\left(d d^{c} u_{j}+\theta_{j}\right)^{n}=e^{u_{j}}|s|_{h}^{-2} f_{j} \omega^{n}$$
for every $j \geq 0$. Then $\left(u_{j}\right)_{j \in \mathbb{N}}$ is a decreasing sequence in capacity and $u_{j}$ converges in $L^{1}$ to a $\theta$-psh function $u \in \mathcal{E}(X, \theta)$ satisfying
$$\left(d d^{c} u+\theta\right)^{n}=e^{u}|s|_{h}^{-2} f \omega^{n} .$$
In particular if (5.1) admits a solution in $\mathcal{E}\left(X, \theta_{j}\right)$, then (5.2) also possesses a (unique) solution in $\mathcal{E}(X, \theta)$.

To see the relevance of this result to Theorem 1.2, we recall the Monge-Ampère equation satisfied by $\omega_{\epsilon}$. Let $\theta$ be a smooth closed form representing $c_{1}\left(K_{X}+D\right)$. Thus $\omega_{D}=d d^{c} u+\theta$ where $u$ is an unknown $\theta$-psh function. Let $s$ be a section in $\mathcal{O}_{X}(D)$ defining $D$. Let $h$ be a smooth Hermitian metric on the latter line bundle. Let $\eta$ be the Chern form of $h$. We rescale $h$ so that $|s|_{h}^{2} \leq 1$. Observe that
$$[D]=d d^{c} \log |s|_{h}+\eta,$$
and by $d d^{c}$-Lemma one gets
$$\eta-\operatorname{Ric}(\omega)-\theta=-d d^{c} F,$$
for some smooth function $F$ on $X$. On the other hand,
$$2 \operatorname{Ric}\left(\omega_{D}\right)=-d d^{c} \log \left(\omega_{D}^{n} / \omega^{n}\right)+2 \operatorname{Ric}(\omega) .$$
Hence since Ric $\omega_{D}=-\omega_{D}+[D]$, one obtains
$$\frac{1}{2} d d^{c}\left(-\log \omega_{D}^{n} / \omega^{n}\right)+\operatorname{Ric} \omega=-\theta-d d^{c} u+[D]=-d d^{c} u+d d^{c} \log |s|_{h}-d d^{c} F+\operatorname{Ric} \omega .$$
Equivalently, we obtain
$$\omega_{D}^{n}=e^{2 u+2 F+2 c}|s|_{h}^{-2} \omega^{n},$$
for some constant $c>0$. Considering $u+c$ in place of $u$ gives
$$\left(d d^{c} u+\theta\right)^{n}=e^{2 u+2 F}|s|_{h}^{-2} \omega^{n} .$$
By [8, Theorem. 4.2], this equation admits a unique solution $u \in \mathcal{E}(X, \theta)$.
Now consider a constant $\epsilon>0$ small enough so that the class $K_{X}+(1-\epsilon) D$ is still big. Observe that $\theta_{\epsilon}:=\theta-\epsilon \eta$ is a smooth representative of the class $c_{1}\left(K_{X}+(1-\epsilon) D\right)$, It was shown in [10] that there exists a unique Kähler-Einstein metric $\omega_{\epsilon}$ of full Monge-Ampère mass such that
$$\operatorname{Ric}\left(\omega_{\epsilon}\right)=-\omega_{\epsilon}+(1-\epsilon)[D],$$
or equivalently $\omega_{\epsilon}=d d^{c} u_{\epsilon}+\theta_{\epsilon}$, where $u_{\epsilon} \in \mathcal{E}\left(X, \theta_{\epsilon}\right)$ is the unique solution of the equation
$$\left(d d^{c} u_{\epsilon}+\theta_{\epsilon}\right)^{n}=e^{2 u_{\epsilon}+2 F}|s|_{h}^{-2(1-\epsilon)} \omega^{n}=e^{2 u_{\epsilon}+2 F}|s|_{h}^{-2}\left(|s|_{h}^{2 \epsilon} \omega^{n}\right) .$$
Note that although $u_{\epsilon}-V_{\theta_{\epsilon}}$ is bounded for every $\epsilon>0$ (see [10, Theorem 4.1]), the function $u-V_{\theta}$ could be unbounded in general, the structure of $\omega_{D}$ near $D$ is mostly like a Poincaré metrics or a conic one; cf. [32]. One sees, hence, that Theorem 5.1 is more general than Theorem 1.2. We now proceed with the proof of Theorem 5.1.

Remark 5.2. In the setting of Theorems 1.2 by applying Theorem 5.1 to the equation (5.6), we see that (5.4) admits a solution in $\mathcal{E}(X, \theta)$. This gives an alternative proof of [8, Theorem. 4.2] without using the variational method.

Remark 5.3. Let $\left(u_{\epsilon}\right)_{\epsilon}$ be the sequence of potentials of the twisted Kähler-Einstein metrics $\omega_{\epsilon}$ in the proof of Theorem 1.1 We already know that $u_{\epsilon}$ converges to $u$ (the potential of $\omega_{D}$ ) locally in $\mathcal{C}^{\infty}$-topology in $X \backslash(D \cup E)$. Direct application of Theorem 5.1 to equations defining $\omega_{\epsilon}$ implies that $u_{\epsilon}$ decreases in capacity to $u$. This global property is much stronger than $L^{1}$-convergence of $u_{\epsilon}$ to $u$.

\subsection*{5.1 Discussions}

Our goal here is to give an informal discussion about the difficulties in the proof of Theorem 5.1 (hence of Theorem 1.2) and explain our strategy to overcome these issues.

Set $\mu_{j}:=f_{j}|s|_{h}^{-2} \omega^{n}$. The difficulty in proving the convergence in Theorem 5.1 is that, unlike some standard situations, the sequence of measures $\left(\mu_{j}\right)_{j}$ is not convergent in the mass norm (or even in the weak sense). This is due to the fact that $f|s|_{h}^{-2} \omega^{n}$ could be of infinite mass on $X$. To be more precise, a usual way to prove the $L^{1}$ convergence of potentials of $\left(u_{j}\right)_{j}$ is as follows (see, e.g., [10]). Let $\delta>0$ be a fixed positive constant. Without loss of generality, we can assume that $u_{j}$ converges to some $u^{\prime}$ in $L^{1}$ (ignore for the moment that $u_{j}$ might a priori converge to $-\infty$ ). Hence $u_{j}$ is $(\theta+\delta \omega)$-psh for every $j$ big enough. We consider $u_{j}^{\prime}:=\left(\sup _{j^{\prime} \geq j} u_{j}\right)^{*}$ which decreases to $u^{\prime}$. We have
$$\left(d d^{c} u_{j}^{\prime}+\theta+\delta \omega\right)^{n} \geq e^{\inf _{j^{\prime} \geq j} u_{j}} \mu_{j} .$$
It follows that for every (continuous) function $g \geq 0$, there holds
$$\liminf _{j \rightarrow \infty} \int_{X} g\left(d d^{c} u_{j}^{\prime}+\theta+\delta \omega\right)^{n} \geq \liminf _{j \rightarrow \infty} \int_{X} g e^{\inf _{j^{\prime} \geq j} u_{j}} \mu_{\epsilon} .$$
If one had that $\mu_{j}$ converges to $\mu:=|s|_{h}^{-2} f \omega^{n}$ in the mass norm, then it would follow from the last estimate that
$$\liminf _{j \rightarrow \infty} \int_{X} g\left(d d^{c} u_{j}^{\prime}+\theta+\delta \omega\right)^{n} \geq \liminf _{j \rightarrow \infty} \int_{X} g e^{u^{\prime}} \mu,$$
and hence, by letting $\delta \rightarrow 0$,
$$\left(d d^{c} u^{\prime}+\theta\right)^{n}=e^{u^{\prime}} \mu,$$
from this, one would conclude that $u^{\prime}=u$. However, as already mentioned, it is not true that $\mu_{j} \rightarrow \mu$ in the mass norm because $\mu(X)$ might be equal to infinity.

Our strategy is to use the quantitative domination principle from [25] because the standard domination principle is not sufficient for our purpose. Let us explain why. Since $|s|_{h}^{2} \leq 1$, we get
$$\left(d d^{c} u_{j_{1}}+\theta_{j_{1}}\right)^{n} \leq e^{u_{j_{1}}-u_{j_{2}}}\left(d d^{c} u_{j_{2}}+\theta_{j_{2}}\right)^{n}$$
if $j_{1} \leq j_{2}$. So, it is tempting to make use of the domination principles. In order to do so, one needs to consider $u_{j_{k}}, k=1,2$, in the same cohomology class.

Fix now a constant $\epsilon>0$. Put $\theta_{\epsilon}^{\prime}:=\theta+\epsilon \omega$. Let $j_{\epsilon} \in \mathbb{N}$ be such that $\theta-\epsilon \omega \leq \theta_{j} \leq \theta_{\epsilon}^{\prime}$ for $j \geq j_{\epsilon}$. Consider $j_{\epsilon}<j_{1} \leq j_{2}$. Hence $u_{j_{s}}$ is $\theta_{\epsilon}^{\prime}$-psh functions for $s=1,2$.
Lemma 5.4. We have
$$-C \epsilon \leq \int_{X}\left(d d^{c} V_{\theta_{j}}+\theta_{\epsilon}^{\prime}\right)^{n}-\int_{X}\left(d d^{c} V_{\theta_{\epsilon}^{\prime}}+\theta_{\epsilon}^{\prime}\right)^{n} \leq 0,$$
for some constant $C>0$ independent of $j$.

Proof. Since $V_{\theta_{j}} \leq V_{\theta_{\epsilon}^{\prime}}$, we get
$$\int_{X}\left(d d^{c} V_{\theta_{j}}+\theta_{\epsilon}^{\prime}\right)^{n}-\int_{X}\left(d d^{c} V_{\theta_{\epsilon}^{\prime}}+\theta_{\epsilon}^{\prime}\right)^{n} \leq 0$$
by monotonicity of non-pluripolar products. The other desired inequality follows from the fact that $\operatorname{vol}\left(\left\{\theta_{j}\right\}\right) \geq \operatorname{vol}(\{\theta-\epsilon \omega\}) \geq \operatorname{vol}(\theta+\epsilon \omega)-O(\epsilon)$. \(\square\)

By Lemma 3.1, we can assume that $u_{j} \leq 0$ for every $j \in \mathbb{N}$. There are two issues when working with $\theta_{\epsilon}^{\prime}$. The first problem is that $u_{j_{s}}$ is no longer in $\mathcal{E}\left(X, \theta_{\epsilon}^{\prime}\right)$ for $s=1,2$, but belongs to $\mathcal{E}\left(X, \theta_{\epsilon}^{\prime}, V_{\theta_{j_{s}}}\right)$, and $V_{\theta_{j_{s}}} \leq V_{\theta_{\epsilon}^{\prime}}$ in general. The second problem is that (5.7) is no longer true if $\theta_{j_{s}}$ is replaced by $\theta_{\epsilon}^{\prime}$. For a constant $M>0$, direct computations show that on $\left\{u_{j_{1}} \leq u_{j_{2}}-M\right\}$ there holds
$$\begin{aligned}
\left(d d^{c} u_{j_{1}}+\theta_{\epsilon}^{\prime}\right)^{n} & \leq e^{u_{j_{1}}-u_{j_{2}}}\left(d d^{c} u_{j_{2}}+\theta_{j_{2}}\right)^{n}+O(\epsilon) \\
& \leq e^{-M}\left(d d^{c} u_{j_{2}}+\theta_{\epsilon}^{\prime}\right)^{n}+O\left(e^{-M} \epsilon\right)+O(\epsilon),
\end{aligned}$$
where for a constant $A>0$ we denote by $O(A)$ a measure of mass bounded by $A$. This estimate suggests that the quantitative domination principle can be applied. To this end, one must, however, have that $u_{j_{s}} \in \mathcal{E}\left(X, \theta_{\epsilon}^{\prime}\right)$, which is not true in general. For that reason, we consider a big constant $k>0$ and put
$$u_{j, k}:=\max \left\{u_{j}, V_{\theta_{\epsilon}^{\prime}}-k\right\} \in \mathcal{E}\left(X, \theta_{\epsilon}^{\prime}\right) .$$