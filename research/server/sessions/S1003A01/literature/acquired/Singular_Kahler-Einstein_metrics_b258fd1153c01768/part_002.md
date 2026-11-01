---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Singular Kahler-Einstein metrics]

Then $\psi \in \mathcal{E}^{1}(X, \omega)$ and $\psi \equiv \varphi$.
Proof. Set $\psi_{j}:=\max (\psi,-j) \in P S H(X, \omega) \cap L^{\infty}(X)$. Observe that the probability measures $\left(\omega+d d^{c} \psi_{j}\right)^{n}$ converge in $X \backslash E$ towards the measure $\nu=e^{t \psi} \mu$. Since $\nu(X)=\nu(X \backslash E)=1$, it follows that $\left(\omega+d d^{c} \varphi_{j}\right)^{n}$ converges to $\nu$ on all of $X$.

Fix $\varepsilon>0$ and set $v_{\varepsilon}:=(\psi+\varepsilon v) /(1+\varepsilon) \in P S H(X, \omega)$, where $v \in$ $P S H(X, \omega), v \leq 0$, is such that $e^{v}$ is continuous and $(v=-\infty)=E$. It follows from lemma 2.2 that for all $s>0$,
$$\operatorname{Cap}_{\omega}\left(\psi_{j}<-s-1\right) \leq \int_{\left(\psi_{j}<-s\right)}\left(\omega+d d^{c} \psi_{j}\right)^{n} \leq \int_{\left(v_{\varepsilon} \leq-s /(1+\varepsilon)\right)}\left(\omega+d d^{c} \psi_{j}\right)^{n} .$$
Observe that $e^{v_{\varepsilon}}$ is continuous on $X$, hence the sublevel sets $\left(v_{\varepsilon} \leq c\right)$ are compact. We infer, letting $j \rightarrow+\infty$,
$$\operatorname{Cap}_{\omega}(\psi<-s-1) \leq \int_{\left(v_{\varepsilon} \leq-s /(1+\varepsilon)\right)} e^{t \psi} d \mu .$$
Letting $\varepsilon$ go to zero and using that $\mu(X)=1$ yields
$$\operatorname{Cap}_{\omega}(\psi<-s-1) \leq \int_{(\psi<-s)} e^{t \psi} d \mu \leq e^{-s} .$$
Therefore the capacity of the sublevel sets of $\psi$ decreases fast as $s \rightarrow+\infty$, hence by lemma 6.2 in [GZ 2] we get $\psi \in \mathcal{E}^{1}(X, \omega)$. Since $e^{-t \varphi}\left(\omega+d d^{c} \varphi\right)^{n} \equiv$ $e^{-t \psi}\left(\omega+d d^{c} \psi\right)^{n}$, it follows from proposition 4.3 that $\varphi \equiv \psi$. \(\square\)

Theorem 4.5. Let $X$ be projective algebraic complex manifold, $\omega_{0}$ a smooth semi Kähler form that is Kähler outside a complex subvariety $S \subset X$, and fix $\Omega$ be a Kähler form on $X$. Assume that $\omega_{o}^{n}=D \Omega^{n}$, where $D^{-\varepsilon}$ is in $L^{1}\left(\Omega^{n}\right)$, and that $\left[\omega_{0}\right],[\Omega] \in N S_{\mathbb{R}}(X)$.

Let $s_{1}, \ldots, s_{p}$ (resp. $t_{1}, \ldots, t_{q}$ ) be holomorphic sections of some line bundle $L$ (resp $L^{\prime}$ ) on $X$. Fix $k \in \mathbb{R}_{\geq 0}, l \in \mathbb{R}_{\geq 0}$ and $F \in \mathcal{C}^{\infty}(X, \mathbb{R})$. Assume that
$$\int_{X} \frac{1}{\left|t_{1}\right|^{2 l}+\ldots+\left|t_{q}\right|^{2 l}} \Omega^{n}<\infty \text { and } \int_{X} \frac{\left|s_{1}\right|^{2 k}+\ldots+\left|s_{p}\right|^{2 k}}{\left|t_{1}\right|^{2 l}+\ldots+\left|t_{q}\right|^{2 l}} e^{F} \Omega^{n}=\int_{X} \Omega^{n} .$$

For each $t>0$, the unique function $\varphi \in P S H\left(X, \omega_{0}\right) \cap \mathcal{C}^{0}(X)$ such that
$$\left(\omega_{0}+d d^{c} \varphi\right)^{n}=\frac{\left|s_{1}\right|^{2 k}+\ldots+\left|s_{p}\right|^{2 k}}{\left|t_{1}\right|^{2 l}+\ldots+\left|t_{q}\right|^{2 l}} e^{F+t \varphi} \Omega^{n}$$
is smooth outside $B=S \cup \cap_{i}\left\{s_{i}=0\right\} \cup \cap_{i}\left\{t_{i}=0\right\}$.
Proof. The proof of Theorem 3.5 applies here almost verbatim. \(\square\)

Remark 4.6. We will apply Theorem 4.1 in section 6 to construct singular Kähler-Einstein metrics on manifolds of general type. This will follow from the resolution of $\left(\omega+d d^{c} \varphi\right)^{n}=e^{t \varphi} \mu$ for large enough values of $t>0$. The Monge-Ampère equations
$$\left(\omega+d d^{c} \varphi\right)^{n}=e^{-t \varphi} \mu, \quad t>0,$$
can also be solved with a similar method, but only for small values of $t<t_{X}$. The critical exponent $t_{X}$ depends on the manifold $X$, and may be too small to produce Kähler-Einstein metrics when $c_{1}(X)>0$ : even smooth manifolds of positive scalar curvature do not necessarily admit Kähler-Einstein metrics (see [T]). Since technical details are much more involved in this case, we postpone this study to a forthcoming article.

\section*{5. Singularities in Mori theory}

The singular locus of the normal complex space of pure dimension $n$ is a codimension $\geq 2$ analytic subvariety denoted by $V^{\text {sing }}$. Let $V^{\text {reg }}=V-V^{\text {sing }}$ and $j: V^{\text {reg }} \rightarrow V$ be the natural open immersion.
5.1. Log terminal singularities. Since this material may not be familiar to complex analysts or differential geometers, we briefly recall some basic facts on some of the singularities encountered in the Minimal Model Program (MMP for short). See [KM] for a detailled account in the algebraic case, the analytic theory being also surveyed there in less detail.

The sheaf of holomorphic functions $\mathcal{O}_{V}$ is the subsheaf of the sheaf of continuous functions on $V$ consisting of the functions whose restriction to $V^{\text {reg }}$ is holomorphic. Actually, by Hartogs' theorem, any holomorphic function on $V^{\text {reg }}$ extends to $V$, which means that $j_{*} \mathcal{O}_{V^{\text {reg }}}=\mathcal{O}_{V}$.

Every meromorphic n-form $\alpha$ on $V^{\text {reg }}$ extends to $V$, i.e. let $\pi: X \rightarrow V$ be a resolution of singularities of $V$, then the meromorphic $n$-form $\pi^{*} \alpha$ defined on $\pi^{-1} V^{\text {reg }}$ extends to a meromorphic $n$-form on $X$. Let $\omega_{V^{\text {reg }}}$ be the canonical sheaf of the smooth variety $V^{\text {reg }}$. The sheaf $\omega_{V}=j_{*} \omega_{V^{\text {reg }}}$ is a coherent analytic sheaf on $V$.

More generally every meromorphic pluricanonical form on $V^{\text {reg }}$ extends to $V$ and $\omega_{V}^{[q]}=j_{*} \omega_{V^{\text {reg }}}^{q}, q>0$ is a coherent analytic sheaf on $V$.

Definition 5.1. Say $V$ is 1-Gorenstein iff one of the following equivalent conditions holds:
\begin{itemize}
\item[(1)] Every $x \in V$ has an open neighborhood $U$ such that $U^{\text {reg }}$ carries an holomorphic $n$-form with an empty zero divisor.
\item[(2)] $\omega_{V}$ is a rank one locally free sheaf.
\item[(3)] Every $x \in V$ has an open neighborhood $U$ such that $\omega_{U^{\text {reg }}}$ is isomorphic to $\left.\mathcal{O}_{V^{\text {reg }}}\right|_{U}$.
\end{itemize}

A local section of $\omega_{V}$ defining an holomorphic $n$-form without zeroes on $V^{\text {reg }}$ will be called a local generator of $\omega_{V}$. If furthermore $V$ is Cohen-Macaulay, $V$ is said to be Gorenstein.

Say $V$ is $\mathbb{Q}$-Gorenstein iff one of the following equivalent conditions is satisfied:
\begin{itemize}
\item[(1)] Every $x \in V$ has an open neighborhood $U$ such that $U^{\text {reg }}$ carries an holomorphic pluricanonical form with an empty zero divisor.
\item[(2)] For every $x \in V$, there exists $N_{x} \in \mathbb{N}$ and an open neighborhood $U$ of $x$ such that $\omega_{U}^{\left[N_{x}\right]}$ is a rank one locally free sheaf.
\item[(3)] For every $x \in V$ there is $N_{x} \in \mathbb{N}$ and an open neighborhood $U$ of $x$ such that $\omega_{U^{r e g}}^{N_{x}}$ is isomorphic to $\left.\mathcal{O}_{V^{r e g}}\right|_{U}$.
\end{itemize}

A local section of $\omega_{V}^{[N]}$ defining an holomorphic pluricanonical form without zeroes on $V^{\text {reg }}$ will be called a local generator of $\omega_{V}^{[N]}$.

For every $x \in V$, the smallest $N_{x}$ fulfilling condition 3 near $x$ is called the local index of $V$ at $x$. The l.c.m. of all local indices, if finite, is called the index of $V$.

Definition 5.2. Say $V$ has only canonical singularities iff $V$ is $\mathbb{Q}$-Gorenstein, of finite index N and one of the following equivalent conditions is fulfilled:
\begin{itemize}
\item[(1)] Let $\pi: X \rightarrow V$ be a resolution. Let $\alpha$ be a local generator of $\omega_{V}^{[N]}$. The meromorphic pluricanonical form $\pi^{*} \alpha$ is holomorphic.
\item[(2)] Let $\pi: X \rightarrow V$ be a resolution. For every $m \in \mathbb{N}, \pi_{*} \omega_{X}^{[N m]}=\omega_{V}^{[N m]}$.
\item[(3)] (Assuming $V$ is an algebraic variety) Let $\pi: X \rightarrow V$ be a resolution. Then $K_{X} \cong \pi^{*} K_{V}+\sum a_{E} E$ with $a_{E} \geq 0$ where $\cong$ means numerical equivalence of $\mathbb{Q}$-Cartier divisors and the sum runs over the exceptional divisors of $\pi$.
\end{itemize}

Observe that it is enough to check the first two conditions for some resolution. In the third condition $N a_{E}$ is the order of vanishing of $\pi^{*} \alpha$ along the divisor $E$.

Definition 5.3. Say $V$ has only log-terminal singularities iff $V$ is $\mathbb{Q}$ -Gorenstein, of finite index $N$ and the following holds: let $\pi: X \rightarrow V$ be a log-resolution and let $\alpha$ be a local generator of $\omega_{V}^{[N]}$ : then the pole along any component $E$ of $\operatorname{exc}(\pi)$ of the meromorphic $N$-canonical form $\pi^{*} \alpha$ on $X$ is of order $\leq N-1$.

When $V$ is algebraic an equivalent formulation is: let $\pi: X \rightarrow V$ be a log-resolution. Then $K_{X} \cong \pi^{*} K_{V}+\sum_{E} a_{E} E$ with $a_{E}>-1$.

The importance of the class of canonical singularities comes from a theorem due to M. Reid [R 1] (see also [Deb], p. 174):

Theorem 5.4. Let $X$ be a projective algebraic manifold of general type whose canonical ring $R=\oplus_{n \in \mathbb{N}} H^{0}\left(X, \omega_{X}^{n}\right)$ is of finite type. Then the canonical model of $X, X_{\text {can }}:=\operatorname{Proj}(R)$ has only canonical singularities. If $N=\operatorname{Index}\left(X_{\text {can }}\right)$ then $\omega_{X_{\text {can }}}^{[N]}$ is ample.

The finiteness of the canonical ring for varieties of general type is known in dimension 3 [Ka]. In higher dimension, Y.Kawamata has proved that it
is a consequence of the existence of minimal models. $X_{\text {can }}$ is a uniquely defined singular birational model of $X$. The minimal models of $X$ in the sense of the MMP are crepant terminalizations of $X_{\text {can }}$ and do not enjoy the above unicity since they may be related by non trivial flops.

Examples 5.5. Let $S$ be a normal algebraic surface. The following are equivalent:
\begin{itemize}
\item[(1)] $S$ has only canonical singularities.
\item[(2)] $S$ is locally analytically isomorphic to $X=\mathbb{C}^{2} / G, G \subset S L_{2}(\mathbb{C})$ a finite subgroup.
\item[(3)] The exceptional divisors of the minimal resolution $\pi_{\text {min }}$ of $S$, have simple normal crossings, their components are (-2) smooth rational curves, their incidence graphs are of type A-D-E (Du Val singularities).
\end{itemize}

The log terminal surface singularities are precisely the singularities of the form $X=\mathbb{C}^{2} / G, G \subset G L_{2}(\mathbb{C})$ a finite subgroup.

Examples 5.6. In higher dimension, quotient singularities are still log terminal. Fix $n>0$ and let $H \subset \mathbb{C P}^{n+1}$ be a smooth degree $d$ hypersurface. The affine cone over $H$ has only canonical singularities iff $d \leq n+1$.

In particular, the ordinary double point $x^{2}+y^{2}+z^{2}+t^{2}=0$ has only canonical singularities but it is not a quotient singularity.

The hypersurface singularities of type $A-D-E$ are canonical.

\subsection*{5.2. Normal Kähler spaces.}

Plurisubharmonic functions. Let $V$ be a normal analytic space of pure dimension $n$. A plurisubharmonic (psh) function $\varphi$ on $V$ is an upper semicontinuous function on $V$ with values in $\mathbb{R} \cup\{-\infty\}$, which is not locally $-\infty$, and extends to a psh function in some local embedding $V \rightarrow \mathbb{C}^{N}$. The function $\varphi$ is strongly psh (resp. $\mathcal{C}^{0}$, resp. $\mathcal{C}^{\infty}$ ) iff it extends to a strongly psh function (resp. $\mathcal{C}^{0}$, resp. $\mathcal{C}^{\infty}$ ) in some local embedding. A continuous function is psh iff its restriction to $V^{\text {reg }}$ is so [FN]. A bounded psh function on $V^{\text {reg }}$ extends to $V$.

A pluriharmonic function on $V$ is a real valued continuous function on $V$ $f$ on $V$ such that one of the following equivalent conditions holds:
\begin{itemize}
\item[-] $f$ is locally the real part of a holomorphic function.
\item[-] Given a local embedding $V \rightarrow \mathbb{C}^{N}, f$ extends locally to a pluriharmonic function on $\mathbb{C}^{N}$.
\item[-] $\left.f\right|_{V^{\text {reg }}}$ is pluriharmonic.
\end{itemize}

Semi-Kähler currents.
Definition 5.7. A semi-Kähler, resp. Kähler, resp. smooth Kähler, potential on $V$ is a family $\left(U_{i}, \varphi_{i}\right)_{i \in I}$ where $\left(U_{i}\right)$ is an open covering of $V$ and $\varphi_{i}$ a psh function, resp. a strongly psh function, resp. a $\mathcal{C}^{\infty}$-smooth strongly psh function, on $U_{i}$ such that $\varphi_{i}-\varphi_{j}$ is pluriharmonic on $U_{i} \cap U_{j}$.

Define an equivalence relation on semi-kähler potentials requiring that $\left(U_{i}, \varphi_{i}\right) \sim\left(V_{j}, \psi_{j}\right)$ iff $\varphi_{i}-\psi_{j}$ is pluriharmonic on $U_{i} \cap V_{j}$.

Definition 5.8. A smooth Kähler metric $\Omega$ on $V$ is a ~-equivalence class of smooth Kähler potentials. A semi-Kähler (resp. Kähler) current on $V$ is a ~-equivalence class of semi-Kähler (resp. Kähler) potentials.

A semi-Kähler current $\Omega=\left(U_{i}, \varphi_{i}\right)_{i \in I} \bmod \sim$ is said to have $L_{\text {loc }}^{\infty}$ (resp. $\mathcal{C}^{0}$, resp. Hölder continuous) potentials iff each $\varphi_{i}$ is $L_{\text {loc }}^{\infty}$ (resp. $\mathcal{C}^{0}$, resp. Hölder continuous).

We will on occasion drop the requirement that the local potentials of $\Omega$ are psh, replacing it by the requirement that they are locally the sum of a smooth and a psh function. The current $\Omega$ will then be called a quasi positive closed current on $V$.

If it has locally bounded potentials, $\Omega$ is fully determined by the closed $(1,1)$ form $\Omega_{\text {reg }}$ on $V_{\text {reg }}$ defined on $U_{i}$ by $\Omega_{\text {reg }}=d d^{c} \varphi_{i}$.

Let $\Omega$ be a smooth Kähler metric on $V$ with Kähler potential $\left(U_{i}, \varphi_{i}\right)$. An upper semi-continuous function $\varphi: X \rightarrow \mathbb{R} \cup-\infty$ is said to be $\Omega$-psh iff $\forall i$ $\varphi_{i}+\varphi$ is psh on $U_{i}$. The semi-Kähler current whose potential is $\left(U_{i}, \varphi+\varphi_{i}\right)$ is denoted by $\Omega+d d^{c} \varphi$.

Example 5.9. Let $V=\mathbb{C}^{2} / \pm 1$. Let $(x, y)$ be the usual affine coordinates on $\mathbb{C}^{2},(u, v, w)$ those on $\mathbb{C}^{3}$. The formulas $u=x^{2}, v=y^{2}, w=x y$ realize $V$ as the closed subscheme of $\mathbb{C}^{3}$ whose equation is $u v-w^{2}=0$. We have two 'natural'Kähler metrics on $V$, the first one is smooth with potential $\varphi^{1}=|u|^{2}+|v|^{2}+|w|^{2}$, induced by the euclidean Kähler metric of $\mathbb{C}^{3}$, the second one is the Kähler current whose potential is $\varphi^{2}=|u|+|v|$. On $V^{\text {reg }}$ it is the quotient of the euclidean metric restricted to $\mathbb{C}^{2}-\{0\}$. Near 0 , $d d^{c} \varphi^{2} \gg d d^{c} \varphi^{1}$.

The metric $d d^{c} \varphi^{2}$ is an example of an orbifold Kähler metric on $V$. The results of [Y] extend without major modifications to Kähler orbifolds. For instance, in each Kähler class of a nodal K3 surface there is a unique Ricci flat orbifold metric.

Chern-Weil forms and hermitian metrics. Let $\mathcal{P} \mathcal{H}_{V}$ be the sheaf of realvalued pluriharmonic functions on $V$. By definition, a closed (1,1)-form on $V$ is a section of the sheaf $\mathcal{C}_{V}^{\infty} / \mathcal{P} \mathcal{H}_{V}$. We have the exact sequence:
$$\mathcal{C}^{\infty}(V) \rightarrow \Gamma\left(V, \mathcal{C}_{V}^{\infty} / \mathcal{P} \mathcal{H}_{V}\right) \xrightarrow{[\cdot]} H^{1}\left(V, \mathcal{P} \mathcal{H}_{V}\right) \rightarrow 0 .$$

A class in $H^{1}\left(X, \mathcal{P} \mathcal{H}_{X}\right)$ will be called Kähler, if it is in the [ . ] image of a smooth Kähler metric.

Remark 5.10. Assume $X$ is smooth. A class $[\omega]$ in $H^{1}\left(X, \mathcal{P} \mathcal{H}_{X}\right)$ will be called numerically base point free iff there exists a proper surjective holomorphic mapping $X \rightarrow Y, Y$ normal, such that $[\omega]$ is the pull back of a Kähler class on $Y$. This is a stronger condition than being semi-Kähler.

In the non-big case (i.e.: $\int_{X} \omega^{n}=0$ ), it is straightforward to construct semi-Kähler classes that are not numerically base point free (e.g. on complex tori). On the other hand, it is still unknown whether there exists a smooth projective variety $X$ and a semi-Kähler form $\omega$ which is big without being numerically base point free.

Let $L$ be a holomorphic line bundle on $V$. The notion of smooth hermitian metric on $(V, L)$ is defined as in the smooth case. Let $h$ be such a metric on $(V, L)$.

Let $s \in H^{0}(U, L)$ be a nowhere zero local holomorphic section of $L$ (a local generator of $L$ ) defined over the open subset $U \subset V$. Set $e^{-\varphi_{s}}:=\|s\|_{h}^{2}$, where $\varphi_{s}$ is a $\mathcal{C}^{\infty}$-smooth function on $U$. The current $d d^{c} \varphi_{s}$ is a smooth closed (1,1)-form on $V$ which does not depend on $s$; it is a semi-Kähler current if $\varphi_{s}$ is psh.

More generally, let $\left(U_{i}\right)_{i}$ be an open covering of $V$ and $s_{i} \in H^{0}\left(U_{i}, \mathcal{O}_{V}(L)\right)$ a local generator of $L$. Let $\varphi_{i}=\varphi_{s_{i}}$. The datum $\left(U_{i}, \varphi_{i}\right)$ defines a smooth closed (1,1)-form on $V$.
Definition 5.11. The Chern-Weil form of ( $V, L, h$ ) (or of $h$ ) is the $\sim$ -equivalence class of the data $\left(U_{i}, \varphi_{i}\right)$ constructed above. We will denote it by $c_{1}(L, h)$.

It is immediate that $\left[c_{1}(L, h)\right]$ is independent of $h$. Hence there is a linear $\operatorname{map} c_{1}: \operatorname{Pic}(V) \rightarrow H^{1}\left(V, \mathcal{P} \mathcal{H}_{V}\right)$. The connection with the more widely known smooth case is made by the observation that, if $X$ is a compact Kähler manifold, $H^{1,1}(X, \mathbb{R})=H^{1}\left(X, \mathcal{P} \mathcal{H}_{X}\right)$.
Proposition 5.12. Let $V$ a compact normal complex analytic variety.
The space $H^{1}\left(V, \mathcal{P} \mathcal{H}_{V}\right)$ is finite dimensional.
Let $L$ a holomorphic line bundle on $V$. Every representative of $c_{1}(L)$ in $H^{1}\left(V, \mathcal{P} \mathcal{H}_{V}\right)$ is the Chern-Weil form of a smooth hermitian on $L$.

If there exists a smooth hermitian metric $h$ such that $c_{1}(L, h)$ is Kähler, then $V$ is projective-algebraic and $L$ is ample.
Proof. The most difficult task is to show that, in the last assertion, $V$ is Moishezon. This follows from Siu's solution of the Grauert-Riemenschneider conjecture [Siu]. \(\square\)

A singular metric on $L$ is an expression $h=e^{-\varphi} h_{s m}, \varphi$ being a locally smooth + psh function and $h_{s m}$ a smooth hermitian metric. Its Chern-Weil form is the quasi-positive current $c_{1}\left(L, h_{s m}\right)+d d^{c} \varphi$.

\section*{6. Adapted volume forms}
6.1. Monge-Ampère equations on normal Kähler spaces. Let $\Omega$ be a smooth Kähler metric on $V$. A classical result of P. Lelong states that if $U$ is relatively compact in $V$, then $U^{\text {reg }}$ is of finite volume with respect to the smooth volume form $\Omega_{\text {reg }}^{n}$.

This has been generalized by E.Bedford and A.Taylor in [BT], where the authors study Monge-Ampère measures for locally bounded psh functions. Since these measures do not charge proper analytic subsets, we obtain:
Proposition 6.1. Let $\Omega$ be a semi-Kähler current with $L_{\text {loc }}^{\infty}$ potentials on $V$. The Monge-Ampère measure $\Omega_{\text {reg }}^{n}$ is well defined on $V_{\text {reg }}$ and satisfies $\int_{U^{\text {reg }}} \Omega_{\text {reg }}^{n}<\infty$, for all relatively compact subset $U \subset V$.

For any resolution $\pi: X \rightarrow V$, the Monge-Ampère measure $\left(\pi^{*} \Omega\right)^{n}$ is well defined on X and satisfies $\pi_{*}\left(\pi^{*} \Omega\right)^{n}=j_{*} \Omega_{\text {reg }}^{n}$. Moreover if $\bar{\pi}: \bar{X} \rightarrow V$ is a resolution dominating $\pi$ (i.e. $\bar{\pi}=\pi \circ \psi$ for some bimeromorphic proper holomorphic map $\psi: \bar{X}^{\prime} \rightarrow X^{\prime}$ ), then $\psi_{*}\left(\bar{\pi}^{*} \Omega\right)^{n}=\left(\pi^{*} \Omega\right)^{n}$.

The measure $\pi_{*}\left(\pi^{*} \Omega\right)^{n}$ is thus well defined on $V$ and independent of the choice of resolution. We will call it the Monge-Ampère measure of $\Omega$ and denote it by $\Omega^{n}$. The mass of this measure only depends on the cohomology class of $\Omega$, as follows again from [BT]:

Lemma 6.2. Assume $V$ is compact. Let $\Omega_{1}, \Omega_{2}$ two semi Kähler currents with $L_{\text {loc }}^{\infty}$ potentiel on $V$. If they are cohomologous, i.e. $\Omega_{1}=\Omega_{2}+d d^{c} \varphi$ for some $\varphi \in L^{\infty}(X)$, then $\int_{V} \Omega_{1}^{n}=\int_{V} \Omega_{2}^{n}$.

We can now reformulate some of our previous results.
Theorem 6.3. Let $V$ be a $n$-dimensional compact normal Kähler space and $\Omega$ be a smooth Kähler form on $V$. Then for every $f \in L^{p}\left(V, \Omega^{n}\right), p>1$, such that $\int_{V} f \Omega^{n}=\int_{X} \Omega^{n}$, there is a unique $\varphi \in \mathcal{C}^{0}(V)$ such that
$$\left(\Omega+d d^{c} \varphi\right)^{n}=f \Omega^{n} \text { and } \sup _{V} \varphi=-1 .$$
Proof. Let $\pi: X \rightarrow V$ be a resolution of $V$. We may define a semipositive big smooth form on $X$ by $\omega=\pi^{*} \Omega$. By Theorem 2.1 and Proposition 3.1 we can solve uniquely $\left(\omega+d d^{c} \bar{\varphi}\right)^{n}=f \circ \pi \omega^{n}$ where $\bar{\varphi}$ is a continuous function on $X$ such that $\omega+d d^{c} \bar{\varphi}$ is semipositive. Let $F$ be a fiber of $\pi$ and $i: F \rightarrow X$ the inclusion map. $F$ is connected by Zariski's main theorem. Furthermore $i^{*} \omega+d d^{c} i^{*} \bar{\varphi}$ is semipositive on $F$. Since $i^{*} \omega=0$, it follows that $i^{*} \varphi$ is a continuous psh function on $F$. Hence $i^{*} \bar{\varphi}$ is constant. This implies that $\bar{\varphi}=\varphi \circ \pi$ where $\varphi$ is a continuous function on $V$. We do have $\left(\Omega+d d^{c} \varphi\right)^{n}=f \Omega^{n}$. \(\square\)
6.2. Adapted measures on log terminal Kähler spaces. Let $V$ be a $n$-dimensional Gorenstein Kähler space and $\Omega$ be a smooth Kähler form on $V$. Fix $x \in V$ and let $\alpha$ be a local generator of $\omega_{V}$ defined over an open subset $x \in U$; then $v=c_{n} \alpha \wedge \bar{\alpha}$ is a positive definite volume form on $U^{\text {reg }}$, for an appropriate choice of the constant $c_{n}=\sqrt{-1}^{n}(-1)^{\frac{n(n+1)}{2}}$.

When $V$ is merely $\mathbb{Q}$-Gorenstein of finite index $N$, we choose $\beta$ a local generator of $\omega_{V}^{[N]}$ defined over an open subset $x \in U$ and we set
$$v=v_{\beta}=\left(\sqrt{-1}^{N n}(-1)^{N \frac{n(n+1)}{2}} \beta \wedge \bar{\beta}\right)^{\frac{1}{N}} .$$
This is a positive definite volume form on $U^{\text {reg }}$.
Our next observation is that log terminal singularities are the worst singularities we can allow in order to globally solve Monge-Ampère equations associated to volume forms on $V$.

Lemma 6.4. For every $U_{1} \subset \subset U, \int_{U_{1}^{\text {reg }}} v<\infty$ iff $X$ is log terminal.
If $V$ is log terminal, then the Radon measure $\mu=j_{*} v$ satisfies $\mu=f \Omega^{n}$ with $f \in L^{1+\varepsilon}\left(U_{1}, \Omega^{n}\right)$ for some $\varepsilon>0$.

Proof. Let $\pi: X \rightarrow V$ be a log resolution. Write $K_{X} \cong \pi^{*} K_{V}+\sum a_{E} E$. Since $\operatorname{exc}(\pi)$ has simple normal crossings, at every $P \in E=\operatorname{exc}(\pi)$ there are local coordinates $\left(z^{i}\right)_{i=1, \ldots, n}$ such that $E$ is described by the equation $z^{1} \ldots z^{q}=0$. Let $E_{j}$ be the divisor $z_{j}=0$. We have: $\pi^{*} v=\prod_{j=1}^{q}\left|z^{j}\right|^{2 a_{E_{j}}} d \lambda$ where $d \lambda$ is a Lebesgue measure on $X$, hence the measure $\pi^{*} v$ has finite mass near $P$ iff $\forall j, a_{E_{j}}>-1$. Thus $\int_{U_{1}^{\text {reg }}} v<\infty$ iff $\forall E, a_{E}>-1$.

Let $f_{1}$ be the density of $\pi^{*} v$ with respect to $d \lambda$. Since $f_{1}$ is comparable to $\prod_{j=1}^{q}\left|z^{j}\right|^{2 a_{E_{j}}}$ near $P$, it follows that $f_{1}$ belongs actually to $L^{p}(X, d \lambda)$ for some $p>1$ when $X$ is log terminal.

Let $D=1 / f$ be the density of $\Omega^{n}$ with respect to $v$. We will see here below that $D$ is bounded but it might have zeroes on $E$, hence $f$ is unbounded in general. However we will show that $f \circ \pi \in L^{\alpha}(X, d \lambda)$ for $\alpha>0$ small enough, hence it follows from Hölder's inequality (as in the proof of lemma 3.2) that
$$\int_{U_{1}^{r e g}} f^{1+\varepsilon} \Omega^{n}=\int_{\pi^{-1} U_{1}^{r e g}} f^{\varepsilon} f_{1} d \lambda<+\infty$$
if $\varepsilon>0$ is small enough.
Fix $x \in V$ and let $i: U_{x} \rightarrow \mathbb{C}^{m}$ be a local embedding of a neighborhood $U_{x}$ of $x$. We consider the $\binom{m}{n} n$-forms on $U_{x}^{\text {reg }} d u^{I}=d u^{i_{1}} \wedge \ldots d u^{i_{n}}$, where $\left(u^{i}\right)$ is a set of affine coordinates on $\mathbb{C}^{m}$. Observe that $\Omega^{n}$ is comparable to $\sum_{I} v_{d u^{I}}{ }^{11}$. Since $\beta$ is a local generator at $x$ of $\omega_{V}^{[N]}$, we have $\left(d u^{I}\right)^{N}=f_{I} \beta$ where $f_{I} \in \mathcal{O}_{V, x}$ is the germ of an holomorphic function at $x$. Therefore $\Omega^{n}$ is comparable to $\sum_{I}\left|f_{I}\right|^{\frac{2}{N}} v$, hence $D$ is comparable to $\left[\sum_{I}\left|f_{I}\right|^{\frac{2}{N}}\right]^{-1}$ near $x$.

The functions $\left(f_{I}\right)$ generate an ideal $\mathcal{I}_{x} \subset \mathcal{O}_{V, x}$. Actually, the construction can be globalized to provide a coherent ideal sheaf $\mathcal{I} \subset \mathcal{O}_{V}$ cosupported on $V^{\text {sing }}$.

We may assume [Hi] that $\pi: X \rightarrow V$ is a log resolution of $(V, \mathcal{I})$, namely a log resolution of $V$ with the additional property that the ideal sheaf $\pi^{-1} \mathcal{I} . \mathcal{O}_{X}$ which is the ideal sheaf of $\mathcal{O}_{X}$ generated by the family of holomorphic functions $\left(\pi^{*} f_{I}\right)_{I}$, satisfies $\pi^{-1} \mathcal{I} . \mathcal{O}_{X}=\mathcal{O}_{X}\left(-\sum N b_{E} E\right) \subset \mathcal{O}_{X}$ where $N . b_{E} \in \mathbb{N}$ is a positive multiplicity attached to any exceptional divisor of $\pi$.

In local coordinates near $P \in X, \pi^{*} D$ is comparable to $\prod_{j}\left|z_{j}\right|^{2 b_{E_{j}}}$, hence $\pi^{*}\left(f_{1} D^{-\varepsilon}\right)$ is comparable to $\prod_{j}\left|z_{j}\right|^{2\left(a_{E_{j}}-\varepsilon b_{E_{j}}\right)}$. It follows that for every relatively compact subset $U_{1} \subset \subset U, \quad f \in L^{1+\varepsilon}\left(U_{1}, \Omega^{n}\right)$ iff $\forall E, \quad \pi(E) \cap U \neq$ $\emptyset \Rightarrow a_{E}-\varepsilon b_{E}>-1$. \(\square\)

Definition 6.5. Assume $V$ has only log terminal singularities. A positive definite adapted measure on $V$ is a positive Radon measure locally of the form $e^{f} . v$ where $f$ is a bounded measurable function. A positive definite adapted measure has $\mathcal{C}^{0}, \mathcal{C}^{\alpha}, \mathcal{C}^{\infty}$ density if so is $f$.

Remark 6.6. It follows from lemma 6.4 that if $V$ is $\mathbb{Q}$-Gorenstein but has non log terminal singularities, $v$ is a volume form on $V^{\text {reg }}$ but does not extend to a measure on $V$.
6.3. Adapted volume forms for klt Kähler pairs. We will be briefer since pairs are mainly of interest to MMP practitioners. The key definition for us will be:

Definition 6.7. A pair ( $V, \Delta$ ) is klt iff $K_{V}+\Delta$ is $\mathbb{Q}$-Cartier and if for any log-resolution $\pi: X \rightarrow V$ of $(V, \Delta)$, we have the numerical equivalence of

\footnotetext{
${ }^{11}$ Note that the formula for $v_{\beta}$ makes sense even if $\beta$ is not a local generator.
}

Cartier divisors:
$$N\left(K_{X}+\Delta^{\prime}\right) \cong \pi^{*} N\left(K_{V}+\Delta\right)+\sum_{E \text { exc. }} N a_{E} E$$
with $a_{E}>-1, \Delta^{\prime}$ the proper transform of $\Delta$ in $X$ (same multiplicities) and $N$ is an integer such that $N\left(K_{V}+\Delta\right)$ is Cartier.

Thus a variety $V$ has only klt singularities iff ( $X, \emptyset$ ) is klt.
Let $\beta$ be a local generator of $\mathcal{O}_{V}\left(N\left(K_{V}+\Delta\right)\right)$. Then $\beta_{V^{\text {reg }}}$ can be viewed as a meromorphic N-canonical form with a pole of order $N d_{i}$ on $E_{i}$ where $\Delta=\sum_{i} d_{i} E_{i}$ is the decomposition of $\Delta$ into prime divisors. Thus $v_{\beta^{\text {reg }}}$ defines a volume form with poles on $V^{\text {reg }}$, namely $v_{\beta_{V^{\text {reg }}}}$ is comparable to $\prod_{i}\left|s_{i}\right|^{-2 d_{i}} d \lambda$, where $s_{i}$ denotes the canonical section of $\mathcal{O}\left(E_{i}\right)$. If $v_{\beta_{V^{r e g}}}$ is a finite measure then $d_{i}<1$, but the converse is not true. We have the following staightforward extension of lemma 6.4:

Lemma 6.8. Let $j^{\prime}: V-\cup_{i} E_{i} \rightarrow V$ be the canonical inclusion. $j_{*}^{\prime} v_{\beta}$ is a well defined Radon measure on $V$ iff $(X, \Delta)$ is klt.

The definition of an adapted measure for a klt pair is left to the reader.

\section*{7. Singular Kähler-Einstein metrics}

\subsection*{7.1. Singular Ricci curvature.}

The smooth case. The link between Monge-Ampère equations and Kähler-Einstein metrics is provided by the following classical

Lemma 7.1. Let $X$ be complex manifold, let $h$ be a smooth hermitian metric on $\omega_{X}$ and $\Omega$ a Kähler form such that $\Omega^{n}=v(h)$. The Ricci curvature divided by $2 \pi$ of $\Omega$ is the Chern-Weil form $-c_{1}\left(K_{X}, h\right)$.

Adapted measures and hermitian metrics on the canonical sheaf. Assume $V$ is compact with only log terminal singularities, has index $N$ and let $h^{N}$ be a smooth hermitian metric on $\omega_{V}^{[N]}$. Let $\beta$ be a local generator local of $\omega_{V}^{[N]}$. Define $v_{\beta}(h)$ to be the volume form on $V^{\text {reg }}$ :
$$v_{\beta}(h)=\left(\sqrt{-1}^{N n}(-1)^{N \frac{n(n+1)}{2}} \frac{\beta \wedge \bar{\beta}}{\|\beta\|_{h^{N}}^{2}}\right)^{\frac{1}{N}}$$

Since $v_{\beta}(h)$ is independent of $\beta$, this expression defines an adapted measure $v(h)$ with $\mathcal{C}^{\infty}$ density on $V$.

Now, let $h_{\text {sing }}^{N}=e^{-N \chi} h^{N}$ be a singular metric on $\omega_{V}^{[N]}$. The Chern-Weil form $c_{1}\left(\omega_{X}^{N}, h_{\text {sing }}^{N}\right)$ is then well defined as a quasipositive current. Since $h_{\text {sing }}^{N}$ has locally $\mathcal{C}^{\infty}+$ psh potentials $\chi$ is locally bounded above and the above formula defines a measure $v\left(h_{\text {sing }}\right)=e^{\chi} v(h)$ on $V$ such that $\frac{v\left(h_{\text {sing }}\right)}{v(h)} \in L_{\text {loc }}^{\infty}$. In particular
$$\frac{v\left(h_{\text {sing }}\right)}{\Omega^{n}} \in L^{1+\varepsilon}\left(V, \Omega^{n}\right) \text { for } \varepsilon>0 \text { small enough. }$$
We have $c_{1}\left(K_{X}, h_{\text {sing }}\right)=c_{1}\left(K_{X}, h\right)+d d^{c} \chi$, where $c_{1}\left(K_{X}, h\right):=\frac{1}{N} c_{1}\left(\omega_{X}^{N}, h^{N}\right)$.

Definition 7.2. Assume $V$ has only log terminal singularities. An adapted measure on $V$ is a positive Radon measure locally of the form $e^{f} . v$ where $f$ is locally given as the sum of a psh and a smooth function on $V$. An adapted measure is $\mathcal{C}^{0}, \mathcal{C}^{\alpha}, \mathcal{C}^{\infty}$ density if so is $e^{f}$.

The definition has the virtue of generalizing the usual equivalence between smooth metrics on the canonical sheaf of a manifold and positive definite volume forms to singular metrics and log terminal spaces. This suggests the following ad hoc:

Definition 7.3. Let $V$ be a $\mathbb{Q}$-Gorenstein Kähler normal $n$-dimensional complex space with only log terminal singularities. Let $\Omega$ be a semi-Kähler current with $L_{\text {loc }}^{\infty}$ potential and adapted Monge-Ampère measure. Let $h$ be the singular metric on the canonical sheaf such that $\Omega^{n}=v(h)$. We define
$$\operatorname{Ric}(\Omega):=-c_{1}\left(K_{V}, h\right),$$
where the equality is to be taken in the sense of currents.
The metric $\Omega$ will be called a singular Kähler-Einstein metric if $\operatorname{Ric}(\Omega)=$ $c \Omega$ for some $c \in \mathbb{R}$.

\subsection*{7.2. Singular Ricci flat metrics.}

Definition 7.4. Let $V$ be a Kähler space with only log terminal singularities. $V$ is said to be $\mathbb{Q}-C Y$, iff there is some multiple $N^{\prime}$ of index $(X)$ such that $H^{0}\left(V, \omega_{V}^{\left[N^{\prime}\right]}\right)=\mathbb{C} \alpha$, where $\alpha$ is a global generator of $\omega_{V}^{\left[N^{\prime}\right]}$.

Theorem 7.5. Assume $V$ is a compact $\mathbb{Q}$-CY Kähler space. Let $\Omega$ be a smooth Kähler metric on $V$. Then there is a unique semi-Kähler current with continuous potential and adapted Monge-Ampère measure $\Omega^{\prime}=\Omega+$ $d d^{c} \varphi$, such that
$$\left(\Omega+d d^{c} \varphi\right)^{n}=C v_{\alpha} \text { and } \sup _{V} \varphi=-1,$$
where $\int_{V} \Omega^{n}=C \int_{V}(-1)^{n} v_{\alpha}$.
Furthermore, if $V$ is projective-algebraic and $[\Omega] \in N S_{\mathbb{R}}(V)$, then $\Omega+d d^{c} \varphi$ is smooth on $V^{\text {reg }}$ where it defines a bona fide Ricci flat metric.

Corollary 7.6. In each cohomology class of a smooth Kähler form, there is a unique singular Ricci flat metric..

Proof. This follows straighforwardly from Theorems 6.3, 3.6, Lemma 6.4 and Definition 7.3. \(\square\)

Example 7.7. A nodal quintic threefold is $\mathbb{Q}-C Y$ and has not quotient singularities, so the orbifold method of [Ko] does not work.

\subsection*{7.3. Singular Kähler-Einstein metrics of negative curvature.}

Theorem 7.8. Let $V$ be a general type projective algebraic variety with only canonical singularities such that $K_{V}$ is ample. Let $h^{N}$ a smooth hermitian metric on $\omega_{V}^{N}$ such that $\Omega=c_{1}\left(K_{V}, h\right)$ is a smooth Kähler form on $V$.

There is a unique $\varphi \in \mathcal{C}^{0}(V, \mathbb{R})$ such that:
\begin{itemize}
\item[(1)] $\varphi$ is $\Omega-p s h$.
\item[(2)] $\Omega+d d^{c} \varphi$ semi Kähler current with $\mathcal{C}^{0}$ potential.
\end{itemize}
$$\left(\Omega+d d^{c} \varphi\right)^{n}=e^{\varphi} v(h) .$$
Consequently $\Omega+d d^{c} \varphi$ is the unique singular $K E$ metric on $V$ of negative curvature in the canonical class of $V$. The current $\Omega+d d^{c} \varphi$ has continuous potentials and is smooth on $V^{\text {reg }}$ where it defines a bona fide $K E$ metric.

Proof. This is a consequence of Theorems 4.1, 4.4, and Definition 7.3. \(\square\)

Remark 7.9. Thanks to Theorem 5.4, for $X$ a projective algebraic manifold of general type such that $R(X):=\oplus_{n \in \mathbb{N}} H^{0}\left(X, \mathcal{O}_{X}\left(n K_{X}\right)\right)$ is finitely generated, $X$ has a unique birational model $V$ such that the above hypotheses hold. Thus we have a birational map $\pi: X \rightarrow$ - $V$ which is well defined outside an indeterminacy locus $S$ of codimension $\leq 2$. In particular $\pi^{*}\left(\omega+d d^{c} \varphi\right)$ is a closed positive current on $X-S$ that extends to a closed positive current $T$ on $X$ itself. The current $T$ defines a $K E$ metric on $X-S$. It needs not be a singular $K E$ metric on $X$ though, since its potentials may have logarithmic poles on $S$, in fact algebraic singularities of the form $\alpha \log \left(\sum\left|f_{i}\right|^{2}\right)+O(1)$ $f_{i}$ holomorphic and $\alpha \in \mathbb{Q}_{>0}$. Moreover, $T$ lies in the canonical class of $X$ iff $X$ is a smooth minimal model as in [Ts].

Connection with [Ts]. Let $X$ be a complex projective manifold such that $K_{X}$ is nef and big. Let $\Omega$ be a smooth Kähler metric on $X$ and consider the Kähler-Ricci flow
$$\frac{\partial \Omega_{t}}{\partial t}=-\operatorname{Ric}\left(\Omega_{t}\right)-\Omega_{t}, \quad \Omega_{0}=\Omega$$

In [Ts], it was proved that this flow has a global solution for all time $t \in[0, \infty[$, and an argument was given, recently fully completed in [TZ], to the effect that $\Omega_{t}$ converges to a closed positive current $T_{K E}$, independent of $\Omega$, which defines a smooth Kähler-Einstein metric outside the exceptional divisor $E$ of the holomorphic bimeromorphic map $X \rightarrow X_{\text {can }}$. Its potential satisfies the Monge Ampère équation considered in Theorem 7.8 outside $E$. It follows from proposition 4.4 that the current $T_{K E}$ coincides with the solution produced by Theorem 7.8.

The notes [ST], [TZ] announce a proof of the following properties, already conjectured by [Ts], that $T_{K E}$ has locally bounded potential and satisfies the degenerate Monge-Ampère equation considered in Theorem 7.8. Our Theorem 7.8 in this case gives the precision that $T_{K E}$ has continuous potentials.

Example 7.10. A nodal sextic threefold is of general type, Gorenstein, terminal, is its own canonical model, has no smooth minimal model and does not have quotient singularities. Therefore the orbifold method of [Ko] does not work and [Ts] does not apply.
7.4. Singular KE metrics on klt pairs. Let us now state the immediate generalization to klt pairs.

Definition 7.11. Let ( $V, \Delta$ ) be a klt compact Kähler pair.
The pair $(V, \Delta)$ is said to be $\mathbb{Q}-C Y$, iff there is some multiple $N^{\prime}$ of index $(X, \Delta)$ such that $H^{0}\left(V, \mathcal{O}_{V}\left(N^{\prime}\left(K_{V}+\Delta\right)\right)\right)=\mathbb{C} \alpha$ where $\alpha$ is a global generator of $\mathcal{O}_{V}\left(N^{\prime}\left(K_{V}+\Delta\right)\right)$.

The pair $(V, \Delta)$ is canonically polarized iff $K_{V}+\Delta$ is ample.

Theorem 7.12. Let $(V, \Delta)$ be a klt compact Kähler pair.
If $(V, \Delta)$ is $\mathbb{Q}-C Y$ it carries a singular Ricci flat metric with adapted volume form in any Kähler class of $V$, this current being smooth outside $\Delta \cup V^{\text {sing }}$ if $V$ projective and the Kähler class is rational.

If it is canonically polarized it carries a unique singular KE metric in the cohomology class of $K_{V}+\Delta$, regular outside $\Delta \cup V^{\text {sing }}$.

Proof. For regularity on the smooth locus, we need the full statement of Theorems 3.5 and 4.5, poles included. \(\square\)

Acknowledgements. We would like to thank Z. Blocki, S. Boucksom, A. Chiodo, J. Keller, S. Kolodziej, M. Paun and B. Toën for useful conversations and C. Simpson and Y.T. Siu for inspiring remarks.

\section*{References}

A T.AUBIN: Équations du type Monge-Ampère sur les variétés kählériennes compactes. Bull. Sci. Math. (2) 102 (1978), no. 1, 63-95.
BT E.BEDFORD \& B.A.TAYLOR: A new capacity for plurisubharmonic functions. Acta Math. 149 (1982), no. 1-2, 1-40.
Bl Z.BLOCKI: Uniqueness and stability for the Monge-Ampère equation on compact Kaehler manifolds. Indiana Univ. Math. J. 52 (2003), no. 6, 1697-1701.
Bl2 Z.BLOCKI: The Monge-Ampère equation on compact Kähler manifolds. Lecture Notes of a course given at the Winter School in Complex Analysis, Toulouse, 24-328/02/2005.
BK Z.BLOCKI \& S.KOLODZIEJ: Regularization of plurisubharmonic functions on manifolds. Preprint (2006).
BGK C.BOYER \& K.GALICKI \& J.KOLLÁR: Einstein Metrics on spheres, Ann. Math. 162 (2005), 557-580.
Ca E.CALABI: On Kähler manifolds with vanishing canonical class. Algebraic geometry and topology. A symposium in honor of S. Lefschetz, pp. 78-89. Princeton Univ. Press, Princeton, N. J. (1957).
CN P.CASCINI \& G.LA NAVE: Kähler-Ricci Flow and the Minimal Model Program for Projective Varieties. Preprint arXiv math.AG/0603064.
Ce U.CEGRELL: Pluricomplex energy. Acta Math. 180 (1998), no. 2, 187-217.
Cor A. CORTI \& F. AMBRO \& O. FUJINO \& C. HACON \& J. KOLLÁR \& J. Mc KERNAN \& H. TAKAGI: Finitely Generated Algebras and Flips in Higher Dimensions, book in project, http://www.ma.ic.ac.uk/\%7Eacorti/flips.html.
Deb O.DEBARRE: Higher-dimensional algebraic geometry. Universitext. Springer-Verlag, New York, 2001. xiv+233 pp.
Dem 1 J.-P.DEMAILLY: Monge-Ampère operators, Lelong numbers and intersection theory. Complex analysis and geometry, 115-193, Univ. Ser. Math., Plenum, New York (1993).
Dem 2 J.-P.DEMAILLY: A numerical criterion for very ample line bundles. J. Differential Geom. 37 (1993), no. 2, 323-374.
Dem 3 J.-P.DEMAILLY: Cohomology of q-convex spaces in top degrees, Math. Zeitschrift 203 (1990) 283-295.
DP J.-P.DEMAILLY \& M. PAUN: Numerical characterization of the Kähler cone of a compact Kähler manifold, Ann. of Math. 159 (2004), 1247-1274.
FN J.E.FORNAESS \& R.NARASIMHAN: The Levi problem on complex space with singularities. Math. Ann. 248 (1980), 47-72.

GR H.GRAUERT \& R.REMMERT: Coherent analytic sheaves. Grundlehren der Mathematischen Wissenschaften, 265. Springer-Verlag, Berlin, 1984. xviii+249 pp.
G V.GUEDJ: Approximation of currents on complex manifolds. Math. Ann. 313 (1999), no. 3, 437-474.
GZ 1 V.GUEDJ \& A.ZERIAHI: Intrinsic capacities on compact Kähler manifolds. J. Geom. Anal. 15 (2005), no. 4, 607-639.
GZ 2 V.GUEDJ \& A.ZERIAHI: Monge-Ampère operators on compact Kähler manifolds. Preprint ArXiv math.CV/0504234.
HMcK C. HACON \& J. McKERNAN: On the existence of flips, math.AG/0507597.
Ha 1 R.HARTSHORNE: Algebraic geometry. Graduate Texts in Mathematics, 52. Springer-Verlag, New York-Heidelberg, 1977. xvi+496 pp.
Ha 2 R.HARTSHORNE: Stable reflexive sheaves. Math. Ann. 254 (1980), no. 2, 121-176.
Hi H.HIRONAKA, Resolution of singularities over a field of characteristic zero. I,II. Annals of Math. 79 (1964), 109-326.
Hö L.HÖRMANDER: Notions of convexity, Birkhäuser (1994).
Hu A.T.HUCKLEBERRY: Subvarieties of homogeneous and almost homogeneous manifolds. Contributions to complex analysis and analytic geometry, 189-232, Aspects Math., E26, Vieweg, Braunschweig, 1994.
Ka Y.KAWAMATA: On the finiteness of generators of a pluricanonical ring for a 3-fold of general type. Amer. J. Math. 106 (1984), no. 6, 1503-1512.
Ko R. KOBAYASHI: Einstein-Kähler V-metrics on open Satake V-surfaces with isolated quotient singularities. Mathematische Annalen 272 (1985), 385 - 398.
KM J.KOLLÁR \& S.MORI: Birational geometry of algebraic varieties. With the collaboration of C. H. Clemens and A. Corti. Translated from the 1998 Japanese original. Cambridge Tracts in Mathematics, 134. Cambridge University Press, Cambridge, 1998. viii+254 pp.
K 1 S.KOLODZIEJ: The complex Monge-Ampère equation. Acta Math. 180 (1998), no. 1, 69-117.
K 2 S.KOLODZIEJ: The Monge-Ampère equation on compact Kähler manifolds. Indiana Univ. Math. J. 52 (2003), no. 3, 667-686
K 3 S.KOLODZIEJ: The complex Monge-Ampère equation and pluripotential theory. Mem. Amer. Math. Soc. 178 (2005), no. 840, x+64 pp.
MO K.MATSUKI \& M.OLSSON: Kawamata-Viehweg as Kodaira vanishing for stacks. Preprint arXiv math.AG/0212259.
Mo S.MORI: Flip theorem and the existence of minimal models for 3-folds. J. Amer. Math. Soc. 1 (1988), no. 1, 117-253.
Na M. NAKAMAYE: Stable base loci of linear series, Math. Ann. 318 (2000), 837-847.
Pa M. PAUN: Sur l'effectivité numérique des images inverses de fibrés en droites Math Ann 310 (1998) 3, 411-421.
R 1 M.REID: Canonical 3-folds. Journées de Géométrie Algébrique d'Angers, Juillet 1979 pp. 273-310, Sijthoff \& Noordhoff, Alphen aan den Rijn-Germantown, Md., (1980).
R 2 M.REID: Young person's guide to canonical singularities. Algebraic geometry, Bowdoin, 1985 (Brunswick, Maine, 1985), 345-414, Proc. Sympos. Pure Math., 46, Part 1, Amer. Math. Soc., Providence, RI, 1987.
Sho V. SHOKUROV: Prelimiting flips. Tr. Math. Inst. Steklova 240 (2003), 82-219.
S N.SIBONY: Dynamique des applications rationnelles de $\mathbf{P}^{k}$. Dynamique et géométrie complexes (Lyon, 1997), ix-x, xi-xii, 97-185, Panor. Synthèses, 8, Soc. Math. France, Paris, 1999.
Siu Y.T.SIU: A vanishing theorem for semipositive line bundles over non-Kähler manifolds. J. Differential Geom. 19 (1984), no. 2, 431-452.

Siu 2 Y.T.SIU: Multiplier ideal sheaves in complex and algebraic geometry. Preprint arXiv math.AG/0504259.
ST J.SONG \& G.TIAN: The Kähler-Ricci flow on surfaces of positive Kodaira dimension. Preprint arXiv math.DG/0602150.
T G.TIAN: Canonical metrics in Kähler geometry. Lectures in Mathematics ETH Zürich. Birkhäuser Verlag, Basel (2000).
TZ G.TIAN \& Z.ZHANG: On the Kähler-Ricci flow of projective manifolds of general type. Preprint.
Ts H.TSUJI: Existence and degeneration of Kähler-Einstein metrics on minimal algebraic varieties of general type. Math. Ann. 281 (1988), no. 1, 123-133.
Y S.T.YAU: On the Ricci curvature of a compact Kähler manifold and the complex Monge-Ampère equation. I. Comm. Pure Appl. Math. 31 (1978), no. 3, 339-411.
Z A.ZERIAHI: Volume and capacity of sublevel sets of a Lelong class of plurisubharmonic functions. Indiana Univ. Math. J. 50 (2001), no. 1, 671-703.

Philippe Eyssidieux
Institut Fourier - UMR5582
100 rue des Maths, BP 74
38402 St Martin d'Heres (FRANCE)
eyssi@fourier.ujf-grenoble.fr
Vincent Guedj \& Ahmed Zeriahi
Laboratoire Emile Picard
UMR 5580, Université Paul Sabatier
118 route de Narbonne
31062 TOULOUSE Cedex 04 (FRANCE)
guedj@picard.ups-tlse.fr
zeriahi@picard.ups-tlse.fr