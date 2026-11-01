---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Seiberg-Witten Invariants and Pseudo-Holomorphic Subvarieties for Self-Dual, Harmonic 2-Forms]

Fix a Spin ${ }^{\mathbb{C}}$ structure, a value of $r \geq 1$ and a solution $(A, \psi)$ to the associated version of (2.9). Let $B \subset X$ be an open set, and consider the energy of $B$ :
$$\mathcal{E}_{B} \equiv(4 \sqrt{2})^{-1} r \int_{B}|\omega|\left|\left(2^{-1 / 2}|\omega|-|\psi|^{2}\right)\right| .$$
Note that $\mathcal{E}_{B} \leq \mathcal{E}_{X}<\infty$ by virtue of Lemma 3.1 and the second line of (3.2) in particular. The purpose of this section is to first estimate $\mathcal{E}_{B}$ from the above and from below in the case where $B$ is a geodesic ball of some radius $s>0$. The second purpose will be to exploit the estimates for the energy to refine some of the bounds in the previous section.
a) Monotonicity

The following proposition describes the behavior of the energy $\mathcal{E}_{B}$ for the case where $B$ is a geodesic ball in $X$ of some radius $s>0$.

Proposition 4.1 Fix a Spin ${ }^{\mathbb{C}}$ structure for $X$. There is a constant $\zeta \geq 1$, and given $\delta>0$, there is a constant $\zeta_{\delta} \geq 1$; and these constants have the following significance: Fix $r \geq \zeta_{\delta}$ and consider a solution $(A, \psi)$ to the version of (2.9) which corresponds to the given Spin ${ }^{\mathbb{C}}$ structure and $r$. Let $B \subset X$ be a geodesic ball with center $x$ whose points all lie at distance $\delta$ or greater from $Z$. Let $s$ denote the radius of $B$ and require $1 / \zeta_{\delta} \geq s \geq 2^{-1} r^{-1 / 2}$. Then:
\begin{itemize}
\item[-] $\mathcal{E}_{B} \leq \zeta s^{2}$
\item[-] If $|\alpha(x)|<(2 \sqrt{2})^{-1}|\omega|$, then $\mathcal{E}_{B} \geq \zeta_{\delta}^{-1} s^{2}$.
\end{itemize}
Proposition 4.1 is proved in the next subsection. Note that this proposition has the following crucial corollary:

Lemma 4.1 Fix a Spin ${ }^{\mathbb{C}}$ structure of $X$. Given $\delta>0$, there is a constant $\zeta_{\delta}>4$ with the following significance: Fix $r \geq \zeta_{\delta}$ and let $(A, \Psi)$ be a solution to (2.9) for the given value of $r$ and the given Spin ${ }^{\mathbb{C}}$ structure. Let $\rho \in$ $\left(\zeta_{\delta} r^{-1 / 2}, \zeta_{\delta}^{-1} \delta\right)$. Then
\begin{itemize}
\item[-] Let $\Lambda$ be any set of disjoint balls of radius $\rho$ whose centers lie on $\alpha^{-1}(0)$ and have distance at least $\delta$ from $Z$. Then $\Lambda$ has less than $\zeta_{\delta} \rho^{-2}$ elements.
\item[-] The set of points in $\alpha^{-1}(0)$ with distance at least $\delta$ from $Z$ has a cover by a set $\Lambda$ of no more than $\zeta_{\delta} \rho^{-2}$ balls of radius $\rho$. Moreover, each ball in this set has center on $\alpha^{-1}(0)$ and distance to $Z$ at least $\delta / 2$. Finally, the set of concentric balls of radius $\rho / 2$ is disjoint.
\end{itemize}

Note that Lemma 4.1 plays the role in subsequent arguments that is played by Lemma 3.6 in [15].

Proof of Lemma 4.1 To prove the first assertion, use Proposition 4.1 to conclude that when $r$ is large, then the energy of each ball in the set $\Lambda$ is at least $\zeta_{\delta}^{-1} \rho^{2}$. If there are $N$ such balls and they are all disjoint, then $\mathcal{E}_{X} \geq N \zeta_{d}^{-1} \rho^{2}$. Since $\mathcal{E}_{X} \leq \zeta$, this gives the asserted bound on $N$. The second assertion follows from the first by setting $\Lambda^{\prime}$ to equal a maximal (in number) set of disjoint balls of radius $\rho / 2$ whose centers lie on $\alpha^{-1}(0)$ and have distance at least $\delta / 2$ from $Z$. With $\Lambda^{\prime}$ in hand, set $\Lambda$ equal to the set whose balls are concentric to those in $\Lambda^{\prime}$ but have radius $\rho$.
b) Proof of Proposition 4.1 The first two assertions follow from the following claim: For fixed center $x$, consider $\mathcal{E}_{B}$ as a function of the radius $s$ of $B$. Then
$\mathcal{E}_{B}$ is a differentiable function of $s$ which obeys the inequality:
$$\mathcal{E}_{B} \leq 2^{-1} s\left(1+\zeta_{\delta} s\right)\left(1+\zeta_{\delta} r^{-1 / 2}\right) \frac{d}{d s} \mathcal{E}_{B}+\zeta_{\delta} s^{4}$$
If one is willing to accept (4.3), then the proof of Proposition 4.1 proceeds by copying essentially verbatim that of Proposition 3.1 in [15].

With the preceding understood, the task at hand is to establish (4.3). In this regard, note that the argument for (4.3) is only a slightly modified version of that for Proposition 3.2 in [15]. For this reason, the discussion below is brief.

To begin, remark that because of (2.9), one has
$$\mathcal{E}_{B} \leq \int_{B} \omega \wedge 2^{-1} i F_{A}$$
Meanwhile, $\omega$ is exact on $B$, so can be written as $d \theta$ for some smooth 1-form on $B$. Thus,
$$\mathcal{E}_{B} \leq 2^{-1} \int_{\partial B} \theta \wedge 2^{-1} i F_{A} .$$
Since $\omega$ is assumed to be nowhere vanishing on $B$, it follows that there is a coordinate system which is centered at $x$ and valid in a ball of radius $\zeta_{\delta}^{-1}$ about $x$ for which $\omega$ pulls back to $\mathbb{R}^{4}$ as the standard form $\omega_{x}=|\omega(x)| \cdot\left(d y^{1} \wedge\right.$ $\left.d y^{2}+d y^{3} \wedge d y^{4}\right)$. Moreover, this coordinate chart can be chosen so that the pulled back metric is close to a constant multiple of the standard Euclidean metric on $\mathbb{R}^{4}$. To be precise, one can require that the metric $g$ differ from $g_{E}=\sum_{j} d y^{j} \otimes d y^{j}$ as follows:
\begin{itemize}
\item[-] $\left|g-g_{E}\right| \leq \zeta_{\delta}|y|$.
\item[-] $|\partial g| \leq \zeta_{\delta}$.
\end{itemize}
Here, $\partial g$ denotes the tensor of $y$-partial derivatives of $g$. Note that the second line in (4.6) implies that the distance $s$ from the origin as measured by the metric $g$ differs from that, $s_{E}$, measured by the Euclidean metric as follows: $\left|s-s_{E}\right| \leq \zeta_{\delta} s^{2}$.

In these coordinates, the choice $\theta=2^{-1}|\omega(x)|\left(y^{1} d y^{2}-y^{2} d y^{1}+y^{3} d y^{4}-y^{4} d y^{3}\right)$ will be made. Note that $|\theta|$ differs from $2^{-1} s$ by no more than $\zeta_{\delta} s^{2}$. With the preceding understood, it follows (as argued in (3.21-24) in [15]) that
$$\mathcal{E}_{B} \leq 2^{-1} s\left(1+\zeta_{\delta} s\right)\left(1+\zeta_{\delta} r^{-1 / 2}\right) 4^{-1} r \int_{\partial B}|\omega(x)|\left|\left(2^{-1}|\omega|-|\alpha|^{2}\right)\right|+\zeta_{\delta} s^{4} .$$

Moreover, since $\left\|\omega\left|-\left|\omega(x) \| \leq \zeta_{\delta} s\right| \omega\right|\right.$ on $\partial B$, the constant factor $|\omega(x)|$ above can be replaced by the variable factor $|\omega|$ at the cost of increasing $\zeta_{\delta}$. Thus, (4.7) implies that
$$\mathcal{E}_{B} \leq 2^{-1} s\left(1+\zeta_{\delta} s\right)\left(1+\zeta_{\delta} r^{-1 / 2}\right) 4^{-1} r \int_{\partial B}|\omega|\left|\left(2^{-1}|\omega|-|\alpha|^{2}\right)\right|+\zeta_{\delta} s^{4} .$$
To complete the argument for (4.3), use Proposition 3.1 in the previous section to replace the factor $\left(2^{-1}|\omega|-|\alpha|^{2}\right)$ in (4.8) with $\left(2^{-1}|\omega|-|\psi|^{2}\right)$ at the cost of slightly increasing $\zeta_{\delta}$. The resulting equation is (4.3) after the identification of the $s$ derivative of $\mathcal{E}_{B}$ with the quantity $4^{-1} r \int_{\partial B}|\omega|\left(2^{-1}|\omega|-|\psi|^{2}\right)$.
a) A refined curvature bound

The results in Proposition 4.1 about $\mathcal{E}_{B}$ can be used to refine the bound in Proposition 3.2 for $\left|F_{A}^{-}\right|$. The following proposition summarizes:

Proposition 4.2 Fix a Spin ${ }^{\mathbb{C}}$ structure $s$, and fix $\delta>0$. Then, there exist constants $\zeta_{\delta}, \zeta_{\delta}^{\prime} \geq 1$ with the following significance: Let $(A, \psi)$ be a solution to the $s$ version of (2.9) where $r \geq \zeta_{\delta}$. Then, at points in $X$ with distance $\delta$ or more from $Z$,
$$\left|F_{A}^{-}\right| \leq r(2 \sqrt{2})^{-1}\left(2^{-1 / 2}|\omega|-|\alpha|^{2}\right)+\zeta_{\delta}^{\prime} .$$
The remainder of this section is occupied with the
Proof of Proposition 4.2 The proof amounts to a slight modification of the arguments which prove Proposition 3.4 of [15]. To start, introduce the functions $q_{2}$ and $q_{3}$ as in (3.38) and (3.39). Because of (3.40) and (3.41) one has $\left|q_{2}\right| \leq \zeta_{\delta}$, and so (due to Proposition 3.1's bound on $|\beta|^{2}$ ), it is enough to bound $q_{3}$ by a uniform constant. In this regard, note that $q_{3}$ obeys the equation
$$2^{-1} d^{*} d q_{3}+4^{-1}|\alpha|^{2} q_{3} \leq \zeta_{\delta} r .$$
where $\sigma \geq \delta$ and when $r \geq \zeta_{\delta}$. Also, $q_{3}=0$ where $\sigma=\delta$.
With these last points understood, the key to the proof is the following lemma (compare with Lemma 3.5 in [15]):

Lemma 4.2 Fix a Spin ${ }^{\mathbb{C}}$ structure $s$, and fix $\delta>0$. Then, there is a constant $\zeta_{\delta} \geq 1$ with the following significance: Let $(A, \psi)$ be a solution to the $s$ version of (2.9) where $r \geq \zeta_{\delta}$. Then, there is a smooth function $u$ which is defined on the set of points in $X$ with distance $\delta$ or more from $Z$ and which obeys
\begin{itemize}
\item[-] $|u| \leq \zeta_{\delta}$.
\item[-] $2^{-1} d^{*} d u \geq r$ where $|\alpha| \leq(2 \sqrt{2})^{-1}|\omega|$.
\item[-] $\left|d^{*} d u\right| \leq \zeta_{\delta} r$.
\item[-] $u=0$ where $\sigma=\delta$.
\end{itemize}

The proof of Proposition 4.2 given Lemma 4.2 is essentially the same as that of Proposition 3.4 in [15] given Lemma 3.5 in [15]. Meanwhile, the proof of Lemma 4.1 is a Dirichlet boundary condition version of the proof of Lemma 3.5 in [15]. The modifications to the argument for the latter in [15] are straightforward and left to the reader.

\section*{5 Local properties of $\alpha^{-1}(0)$}

The purpose of this section is to summarize some of the local properties of $\alpha^{-1}(0)$ at points in the complement of $Z$. At issue here is the behavior of $\alpha^{-1}(0)$ at length scales of order $r^{-1 / 2}$.

The strategy for the investigation at such scales is as follows: Fix $\delta>0$ and a point $x$ whose distance from $Z$ is at least $\delta$. A Gaussian coordinate system based at $x$ defines an embedding $h: \mathbb{R}^{4} \rightarrow X$ which maps the origin to $x$ and which sends straight lines through the origin in $\mathbb{R}^{4}$ to geodesics in $X$ through $x$. Moreover, the pull-back via $h$ of the Riemannian metric agrees with the Euclidean metric to second order at the origin. The Gaussian coordinate charts at $x$ are parametrized by the group $S O(4)$ (to be precise, the fiber of the frame bundle at $X$ ). In particular, there are Gaussian coordinate systems at $X$ which pull $\omega$ back as $h^{*} \omega=|\omega(x)|\left(d y^{1} \wedge d y^{2}+d y^{3} \wedge d y^{4}\right)+\mathcal{O}(|y|)$. Such a Gaussian coordinate system will be called a complex Gaussian coordinate system. Indeed, a Gaussian coordinate system at $x$ is called complex precisely when the differential of the corresponding $h$ at the origin intertwines the standard almost complex structure on $\mathbb{R}^{4}=\mathbb{C}^{2}$ with $\left.J\right|_{x}$. The complex Gaussian coordinate systems at $x$ are parametrized by the $U(2)$ subgroup of $S O(4)$.

Now, fix a Spin ${ }^{\mathbb{C}}$ structure on $X$ and $r \geq 1$ and then let ( $A, \psi$ ) be a solution to the corresponding version of (2.9). Then, pull-back by the map $h$ of a Gaussian coordinate system at some $x$ defines $(A, \psi)$ as fields open $\mathbb{R}^{4}$.

Given $\lambda>0$, define the dilation map $\delta_{\lambda}: \mathbb{R}^{4} \rightarrow \mathbb{R}^{4}$ by its action on the coordinate functions $y: \delta_{\lambda}^{*} y=\lambda^{-1} y$. With $x$ chosen in the complement of $Z$
set $\lambda=(r|\omega(x)|)^{1 / 2}$ and let $h$ be a complex Gaussian coordinate system based at $x$. Given $(A, \psi=(\alpha, \beta))$, define the data $(\underline{A},(\underline{\alpha}, \underline{\beta}))$ on $\mathbb{R}^{4}$ by the rule:
$$(\underline{A},(\underline{\alpha}, \underline{\beta})) \equiv \delta_{\lambda}^{*} h^{*}\left(A,|\omega(x)|^{-1 / 2}(\alpha, \beta)\right) .$$
The plan now is to compare ( $\underline{A},(\underline{\alpha}, \underline{\beta})$ ) with some standard objects on $\mathbb{R}^{4}$. These standard objects are discussed in Proposition 4.1 of [15]. The following digression constitutes a brief summary: A connection $a_{0}$ on the trivial complex line bundle over $\mathbb{R}^{4}$ and a section $\alpha_{0}$ of this line bundle will be said to a solution to the Seiberg-Witten equations on $\mathbb{R}^{4}$ when the following conditions hold:
\begin{itemize}
\item[-] The curvature 2-form, $F_{a}$, of $a_{0}$ is of type 1-1 with respect to the standard almost complex structure on $\mathbb{R}^{4}$ and so defines a holomorphic structure (and associated $\bar{\partial}$ operator) on the trivial complex line bundle.
\item[-] The section $\alpha_{0}$ is holomorphic with respect to the $a_{0}$-complex structure on the trivial complex line bundle.
\item[-] $F_{a}^{+}=-i 8^{-1}\left(1-\left|\alpha_{0}\right|^{2}\right)\left(d y^{1} \wedge d y^{2}+d y^{3} \wedge d y^{4}\right)$
\item[-] $\left|\alpha_{0}\right| \leq 1$.
\item[-] $\left|F_{a}^{-}\right| \leq\left|F_{a}^{+}\right| \leq(4 \sqrt{2})^{-1}\left(1-\left|\alpha_{0}\right|^{2}\right)$.
\item[-] $\left|\nabla_{a} \alpha_{0}\right| \leq z\left(1-\left|\alpha_{0}\right|^{2}\right)$.
\item[-] For each $N \geq 1$, the integral of $\left(1-\left|\alpha_{0}\right|^{2}\right)$ over the ball of radius $N$ is bounded by $z N^{2}$.
\end{itemize}
Here, $z$ is a constant. (Note that these conditions differ from the conditions listed in (4.3) of [15] in that no assumption on the integrability of $\left|F_{a}^{+}\right|^{2}-\left|F_{a}^{-}\right|^{2}$ is made here. It is most probably true that the latter condition is a consequence of those in (5.2).)

The following proposition summarizes the basic properties of solutions to (5.2):
Proposition 5.1 Let $\left(a_{0}, \alpha_{0}\right)$ obey the conditions in (5.2). Then:
\begin{itemize}
\item[-] Either $\left|\alpha_{0}\right|<1$ everywhere or else $\left|\alpha_{0}\right|=1$ and $\left(a_{0}, \alpha_{0}\right)$ is gauge equivalent to the trivial solution $\left(a_{0}=0, \alpha_{0}=1\right)$. In the former case, $\alpha_{0}^{-1}(0) \neq \emptyset$ and $\alpha_{0}^{-1}(0)$ is the zero set of a polynomial in the complex coordinates for $\mathbb{R}^{4}=\mathbb{C}^{2}$.
\item[-] Either $\left|F_{a}^{-}\right|<\left|F_{a}^{+}\right|$everywhere or else $\left|F_{a}^{-}\right| \equiv\left|F_{a}^{+}\right|$and there is a $\mathbb{C}$ - linear map $s: \mathbb{C}^{2} \rightarrow \mathbb{C}$ and a solution $\left(a_{1}, \alpha_{1}\right)$ to the vortex equations on $\mathbb{C}$ with the property that $\left(a_{0}, \alpha_{0}\right)$ is gauge equivalent to the pull-back $s^{*}\left(a_{1}, \alpha_{1}\right)$. In this case, $\alpha_{0}^{-1}(0)$ is a finite set of parallel, complex planes.
\end{itemize}
\begin{itemize}
\item[-] Given the constant $z$ in (5.2), there is an upper bound on the order of vanishing of $\alpha_{0}$ at any point in $\mathbb{C}^{2}$.
\item[-] The set of gauge equivalence classes of $\left(a_{0}, \alpha_{0}\right)$ which obey (5.2) for a fixed value of $z$ is sequentially compact with respect to convergence on compact subsets of $\mathbb{R}^{4}$ in the $C^{\infty}$ topology.
\item[-] Given the value of $z$ in (5.2), there exists $z_{1}>0$ such that
$$\left(1-\left|\alpha_{0}\right|^{2}\right)+\left|\nabla_{a} \alpha_{0}\right|^{2} \leq z_{1} \exp \left[-\operatorname{dist}\left(\cdot, \alpha_{0}^{-1}(0)\right) / z_{1}\right] .$$
\end{itemize}
This proposition restates various assertions of Proposition 4.1 in [15]; the reader is referred to Section 4e of [15] for the proof.

End the digression.
The relevance of the solutions to the standard Seiberg-Witten solutions to the problem at hand is summarized by the next proposition:

Proposition 5.2 Fix a Spin ${ }^{\mathbb{C}}$ structure for $X$. Given $\delta>0$, there is a constant $z_{\delta} \geq 1$, and given $R \geq 1, k \geq 1$ and $\varepsilon>0$, there is another constant $\zeta_{\delta}$ and these have the following significance: Let $r>\zeta_{\delta}$ and let $(A, \psi)$ be a solution to (2.9) as defined with the given Spin ${ }^{\mathbb{C}}$ structure and with $r$. Suppose that $x \in X$ has distance at least $\delta$ from $Z$. Now define the fields $(\underline{A},(\underline{\alpha}, \underline{\beta}))$ as in (5.1). Then there exists a solution $\left(a_{0}, \alpha_{0}\right)$ to the $z_{1} \leq z_{\delta}$ version of (5.2) and a gauge transformation $\varphi: \mathbb{C}^{2} \rightarrow S^{1}$ such that $\varphi^{*}(\underline{A},(\underline{\alpha}, \underline{\beta}))-\left(2 a_{0},\left(\alpha_{0}, 0\right)\right)$ has $C^{k}$ norm less than $\varepsilon$ in the ball of radius $R$ and center 0 in $\mathbb{R}^{4}$. Furthermore, $\left|\alpha_{0}\right|$ is not constant if $|\alpha(x)| \leq 1-\varepsilon$.

Proof of Proposition 5.2 The proof of this proposition can be found by lifting from Section 4c of [15] the proofs of the analogous assertions of Proposition 4.2 of [15]. (The lack of control here on the integral over $\mathbb{R}^{4}$ of $\left|F_{a}^{+}\right|^{2}-\left|F_{a}^{-}\right|^{2}$ precludes only the use of the proofs in [15] of statements which actually refer to this integral.)

\section*{6 Large $r$ behavior away from $\alpha^{-1}(0)$}

Fix a Spin ${ }^{\mathbb{C}}$ structure for $X$ and then consider a solution $(A, \psi)$ to (2.9) for the given Spin ${ }^{\mathbb{C}}$ structure and for some large value of $r$. The purpose of this section is to investigate the behavior of $(A, \psi)$ to (2.9) at points which lie neither on $Z$ nor on $\alpha^{-1}(0)$. Here are the basic observations: First, $2^{-1 / 2}|\omega|-|\alpha|^{2}$ and $|\beta|$ are both $\mathcal{O}\left(r^{-1}\right)$. In particular, this means that $F_{A}$ is bounded. More to
the point, the connection $A$ is close to a canonical connection $A^{0}$ whose gauge orbit depends only on the metric and the choice of $\omega$. (Note that this orbit is independent of the chosen Spin ${ }^{\mathbb{C}}$ structure.) Proposition 6.1, below, gives the precise measure of closeness that is used here.

The statement of Proposition 6.1 requires a preliminary, three part digression whose purpose is to define the connection $A^{0}$. The first part of the digression remarks that the $-\sqrt{2} i|\omega|$ eigenspace of the Clifford multiplication endomorphism by $c_{+}(\omega)$ on $S_{+}$defines a complex line bundle $E \rightarrow X-Z$. The component $\alpha$ of $\psi$ is a section of $E$, and then the component $\beta$ is one of $K^{-1} E$. Here, $K^{-1}$ is the inverse of the canonical bundle, $K$, for the almost complex structure $J \equiv \sqrt{2} g^{-1} \omega /|\omega|$ on $X-Z$.

Note that the line bundle $L=\operatorname{det}\left(S_{+}\right)$restricts to $X-Z$ as
$$\left.L\right|_{X-Z} \approx K^{-1} E^{2} .$$
Meanwhile, $\alpha$ trivializes $E$ where $\alpha \neq 0$ and so the unit length section $\alpha^{2} /|\alpha|^{2}$ of $E^{2}$ provides an isometric identification of $L$ with $K^{-1}$ on the complement of $Z$ and $\alpha^{-1}(0)$.

The second part of the digression reviews the definition from [18] or Section 1c of [15] of a canonical connection on the line bundle $K^{-1} \rightarrow X-Z$. (Note that this connection is unique up to gauge equivalence.) To define a canonical connection, first remark that there is a canonical Spin ${ }^{\mathbb{C}}$ structure for $X-Z$ so that the $-\sqrt{2} i|\omega|$ eigenbundle for the $c_{+}(\omega)$ action on the corresponding $S_{+}$ is the trivial bundle over $X-Z$. For this Spin ${ }^{\mathbb{C}}$ structure, the corresponding line bundle $L$ is isomorphic to $K^{-1}$. With this understood, there is a unique connection (up to isomorphism) on $K^{-1}$ for which the induced connection on the aforementioned $-\sqrt{2} i|\omega|$ eigenbundle is trivial. Such a connection is a canonical one.

Part 3 of the digression defines a canonical connection on $\left.L\right|_{X-Z}$ by using the identification $\alpha^{2} /|\alpha|^{2}$ between $L$ and $K^{-1}$ (where $\alpha \neq 0$ on $X-Z$ ) to pull a canonical connection on $K^{-1}$ back to $L$.

End the digression.
Proposition 6.1 Fix a Spin ${ }^{\mathbb{C}}$ structure for $X$ and $\delta>0$. There is a constant $\zeta_{\delta} \geq 1$ with the following significance: Suppose that $r \geq \zeta_{\delta}$ and that $(A, \psi)$ are a solution to (2.9) as defined by $r$ and the given Spin ${ }^{\mathbb{C}}$ structure. There is a canonical connection $A^{0}$ on $\left.L\right|_{X-Z}$ for which $\left|A-A^{0}\right|+\left|F_{A}-F_{A^{0}}\right| \leq$ $\zeta_{\delta} r^{-1}+\zeta_{\delta} r \exp \left[-\sqrt{r} \operatorname{dist}\left(x, \alpha^{-1}(0)\right) / \zeta_{\delta}\right]$ at all points $x \in X$ with distance $\delta$ or more from $Z$ and distance $r^{-1 / 2}$ or more from $\alpha^{-1}(0)$.
(This proposition should be compared with Proposition 4.4 in [15].)
Proof of Proposition 6.1 Away from $Z$ and where $\alpha \neq 0$, the section $\alpha /|\alpha|$ defines a trivialization of the line bundle $E$, and with this understood, the difference between $A$ and a particular canonical connection $A^{0}$ is given by $2(\bar{\alpha} /|\alpha|) \nabla_{A}(\alpha /|\alpha|)$. Thus, the absolute value of $\nabla_{A}(\alpha /|\alpha|)$ measures the size of $A-A^{0}$. Likewise, the norm of $d_{A} \nabla_{A}(\alpha /|\alpha|)$ measures the size of $F_{A}-F_{A^{0}}$.

With the task ahead now clear, note that the arguments which establish the required bounds on the derivatives of $\alpha$ are, for the most part, straightforward modifications of the arguments which prove Proposition 4.4 in [15]. In particular, the reader will be referred to the latter reference at numerous points. In any event, the details are given in the subsequent four steps.

Step 1 A straightfoward modification of the proof of Proposition 4.4 in [15] (which is left to the reader) proves the following preliminary estimate:

Lemma 6.1 Fix a Spin ${ }^{\mathbb{C}}$ structure for $X$ and fix $\delta>0$. There is a constant $\zeta_{\delta}$ with the following significance: Let $(A, \psi)$ solve the version of (2.9) which is defined by the given Spin ${ }^{\mathbb{C}}$ structure and by $r \geq \zeta_{\delta}$. If $x \in X$ has distance $\delta$ or more from $Z$, then
$$\begin{aligned}
r\left|\left(2^{-1 / 2}|\omega|-|\alpha|^{2}\right)\right| 7 & +r^{2}|\beta|^{2}+\left|\nabla_{A} \alpha\right|^{2}+r\left|\nabla_{A} \beta\right|^{2} \\
& \leq \zeta_{\delta}\left(1+r \exp \left[-\sqrt{r} \operatorname{dist}\left(x, \alpha^{-1}(0)\right) / \zeta_{\delta}\right]\right) .
\end{aligned}$$

Step 2 Now, introduce $\underline{\alpha} \equiv 2^{1 / 4}|\omega|^{-1 / 2} \alpha$. Add the two lines of (3.53) to obtain a differential inequality for the function $y \equiv\left|\nabla_{A} \underline{\alpha}\right|^{2}+\left|\nabla_{A} \beta\right|^{2}$. Use Lemma 6.1 to bound $|w|$ to find that the aforementioned inequality implies that $2^{-1} d^{*} d y+4^{-1} r \zeta_{\delta}^{-1} y \leq \zeta_{\delta} r^{-1}$ at points with distance $\delta$ or more to $Z$ and distance $\zeta_{\delta} r^{-1 / 2}$ or more to $\alpha^{-1}(0)$. Note that (6.3) implies that $y^{\prime} \equiv y-4 \zeta_{\delta}^{2} r^{-2}$ obeys the inequality
$$2^{-1} d^{*} d y^{\prime}+4^{-1} r \zeta_{\delta}^{-1} y^{\prime} \leq 0 .$$
at points with distance $\delta$ or more to $Z$ and $\zeta_{\delta} r^{-1 / 2}$ or more to $\alpha^{-1}(0)$.
Given (6.3), a straightforward modification of the proof of Proposition 4.4 in [15] yields the bound
$$\left|\nabla_{A} \underline{\alpha}\right|^{2}+\left|\nabla_{A} \beta\right|^{2} \leq \zeta_{\delta} r^{-2}+\zeta_{\delta} r \exp \left(-\sqrt{r} \operatorname{dist}\left(\cdot, \alpha^{-1}(0)\right) / \zeta_{\delta}\right)$$
at points with distance $2 \delta$ or more from $Z$. (Bounds on the size of both $\left|\nabla_{A} \underline{\alpha}\right|^{2}$ and $\left|\nabla_{A} \beta\right|^{2}$ near $\alpha^{-1}(0)$ come via Proposition 3.3.)

Take the $\delta / 2$ version of (6.4) with the fact that $\underline{\alpha} /|\underline{\alpha}|=\alpha /|\alpha|$ to bound the difference between $A$ and a canonical connection on $L$ by
$$\zeta_{\delta}\left(r^{-1}+r^{1 / 2} \exp \left(-\sqrt{r} \operatorname{dist}\left(\cdot, \alpha^{-1}(0)\right) / \zeta_{\delta}\right)\right)$$
at points with distance $\delta$ or more from $Z$ and $r^{-1 / 2}$ or more from $\alpha^{-1}(0)$.

Step 3 As remarked above, a bound on $\left|\nabla_{A}^{2} \underline{\alpha}\right|$ provides a bound on $\left|F_{A}-F_{A^{0}}\right|$. To obtain the latter, first differentiate (3.55) and commute covariant derivatives to obtain an equation for $\nabla_{A}^{2} \underline{\alpha}$ of the form $\nabla_{A}^{*} \nabla_{A}\left(\nabla_{A}^{2} \underline{\alpha}\right)+(4 \sqrt{2})^{-1} r|\omega|\left(\nabla_{A}^{2} \underline{\alpha}\right)+$ Remainder $=0$. Take the inner product of this last equation with $\nabla_{A}^{2} \underline{\alpha}$ to obtain an equation for $\left|\nabla_{A}^{2} \underline{\alpha}\right|^{2}$ having the form $2^{-1} d^{*} d\left|\nabla_{A}^{2} \underline{\alpha}\right|^{2}+4^{-1} r|\omega|\left|\nabla_{A}^{2} \underline{\alpha}\right|^{2}+$ $\left|\nabla_{A}\left(\nabla_{A}^{2} \underline{\alpha}\right)\right|^{2}+\left\langle\nabla_{A}^{2} \underline{\alpha}\right.$, Remainder $\rangle=0$. Here, $\langle$,$\rangle denotes the Hermitian$ inner product on $E \otimes\left(\otimes_{2} T^{*} X\right)$. A similar equation for $\left|\nabla_{A}^{2} \beta\right|$ is obtained by differentiating (3.56). Add the resulting two equations. Then, judicious use Lemma 6.1, (6.5) and the triangle inequality produces a differential inequality for $y^{\prime} \equiv\left|\nabla_{A}^{2} \underline{\alpha}\right|^{2}+\left|\nabla_{A}^{2} \beta\right|^{2}-\zeta_{\delta} r^{-2}$ which has the same form as (6.3). And, with this understood, the arguments which yield (6.4) yield the bound
$$y^{\prime} \leq \zeta_{\delta} r^{-2}+\zeta_{\delta}\left(\sup _{\sigma \geq \delta}\left|y^{\prime}\right|\right) \exp \left(-\sqrt{r} \operatorname{dist}\left(\cdot, \alpha^{-1}(0)\right) / \zeta_{\delta}\right)$$
at points where $\sigma \geq 2 \delta$.

Step 4 The $\delta / 2$ version of (6.5) with a bound on $\left|\nabla_{A}^{2} \underline{\alpha}\right|^{2}+\left|\nabla_{A}^{2} \beta\right|^{2}$ where $\sigma \geq \delta / 2$ by $\zeta_{\delta} r^{2}$ gives Proposition 6.1's bound on $\left|F_{A}-F_{A^{0}}\right|$. Thus, the last task is to obtain a supremum bound on $\left|\nabla_{A}^{2} \underline{\alpha}\right|^{2}+\left|\nabla_{A}^{2} \beta\right|^{2}$.

For this purpose, fix a ball of radius $2 r^{-1 / 2}$ whose points all have distance $\delta / 4$ or more from $Z$. Take Gaussian coordinates based at the center of this ball and rescale so that the radius $r^{-1 / 2}$ concentric ball becomes the radius 1 ball in $\mathbb{R}^{4}$ with center at the origin. Equation (2.9) rescales to give an $r=1$ version of the same equation on the radius 2 ball in $\mathbb{R}^{4}$ with a metric $g^{\prime}$ which is close to the Euclidean metric $g_{E}$ and form $\omega^{\prime}$ which is close a constant self dual form of size $|\omega(x)|$. Here, $x$ is the center of the chosen ball in $X$. To be precise, $\left|g^{\prime}-g_{E}\right| \leq \zeta r^{-1}$ and the derivatives of $g^{\prime}$ of order $k \geq 2$ are $\mathcal{O}\left(r^{-k / 2}\right)$ in size. Meanwhile the form $\omega^{\prime}$ differs by $\mathcal{O}\left(r^{-1 / 2}\right)$ from a constant form, and its $k$-th derivatives are $\mathcal{O}\left(r^{-k / 2}\right)$ in size.

With the preceding understood, standard elliptic regularity results (as in Chapter 6 of [12]) bound the second derivatives of the rescaled versions of $\underline{\alpha}$ and $\beta$ by $\zeta_{\delta}$. Rescaling the latter bounds back to the original size gives $\left|\nabla_{A}^{2} \underline{\alpha}\right|^{2}+\left|\nabla_{A}^{2} \beta\right|^{2} \leq$ $\zeta_{\delta} r^{2}$ as required.

\section*{7 Proof of Theorem 2.2}

Fix a Spin ${ }^{\mathbb{C}}$ structure for $X$ and suppose that there exists an unbounded, increasing sequence $\left\{r_{n}\right\}$ of positive numbers with the property that each $r=r_{n}$ version of (2.9) with the given Spin ${ }^{\mathbb{C}}$ structure has a solution $\left(A_{n}, \psi_{n}\right)$. The purpose of this section is to investigate the $n \rightarrow \infty$ limits of $\alpha_{n}^{-1}(0)$ and in doing so, prove the claims of Theorem 2.2. This investigation is broken into six parts.
a) The curvature as a current

Each connection $A_{n}$ has its associated curvature 2-form, and the difference between $A_{n}$ 's curvature 2-form and the curvature 2-form of the canonical connection on $K^{-1}$ will be viewed as a current on $X$. This current, $\mathcal{F}_{n}$, associates to a smooth 2 -form $\mu$ the number
$$\mathcal{F}_{n}(\mu) \equiv 2^{-1} \int_{X} \frac{i}{2 \pi}\left(F_{A_{n}}-F_{A^{0}}\right) \wedge \mu$$
Here, $F_{A^{0}}$ is the curvature 2-form of the canonical connection on $K^{-1}$. (Even though the canonical connection on $K^{-1}$ is defined only over $X-Z$ (see the beginning of the previous section), the norm of its curvature is none-the-less integrable over $X$. Thus, (7.1) makes sense even for $\mu$ whose support intersects $Z$. The integrability of $\left|F_{A^{0}}\right|$ follows from the bound $\left|F_{A^{0}}\right| \leq \zeta \operatorname{dist}(\cdot, Z)^{-2}$.)

With the sequence $\left\{\mathcal{F}_{n}\right\}$ understood, fix $\delta>0$ and suppose that each point in the support of $\mu$ has distance $\delta$ or more from $Z$. It then follows from Lemma 3.1 and Proposition 4.2 that
$$\left|\mathcal{F}_{n}(\mu)\right| \leq \zeta_{\delta} \sup _{X}|\mu| .$$
This uniform bound implies that the sequence $\left\{\mathcal{F}_{n}\right\}$ defines a bounded sequence of linear functional on the space of smooth 2-forms on $X$ with support where the distance to $Z$ is at least $\delta$.

With the preceding understood, a standard weak convergence argument finds a subsequence of $\left\{\mathcal{F}_{n}\right\}$ (hence renumbered consecutively) which converges in the following sense: Let $\mu$ be a smooth 2-form with compact support on $X-Z$ and then $\lim _{n \rightarrow \infty} \mathcal{F}_{n}(\mu)$ exists. Moreover, this limit,
$$\mathcal{F}(\cdot) \equiv \lim _{n \rightarrow \infty} \mathcal{F}_{n}(\cdot),$$
defines a bounded linear functional when restricted to forms whose support has distance from $Z$ which is bounded from below by any fixed positive number.

Note that the current $\mathcal{F}$ is integral in the following sense: Let $\mu$ be a closed 2-form with compact support on $X-Z$ and with integral periods on $H_{2}(X-Z ; \mathbb{Z})$. Then
$$\mathcal{F}(\mu) \in \mathbb{Z} .$$
b) The support of $\mathcal{F}$

This part of the discussion considers the support of the current $\mathcal{F}$. Here is the crucial lemma:

Lemma 7.1 There is a closed subspace $C \subset X-Z$ with the following properties:
\begin{itemize}
\item[-] $\mathcal{F}(\mu)=0$ when $\mu$ is a 2-form on $X$ with compact support in $(X-Z)-C$.
\item[-] Conversely, let $B \subset X-Z$ be an open set which intersects $C$. Then there is a 2-form $\mu$ with compact support in $B$ and with $\mathcal{F}(\mu) \neq 0$.
\item[-] Fix $\delta>0$. Then the set of points in $C$ with distance at least $\delta$ from $Z$ has finite 2 -dimensional Hausdorff measure.
\item[-] Conversely, let $\delta>0$ and there is a constant $\zeta_{\delta} \geq 1$ with the following significance: Let $\rho \in\left(0, \zeta_{\delta}^{-1}\right)$ and let $B \subset X$ be a ball of radius $\rho$ and center on $Z$ whose points have distance $\delta$ or more from $Z$. Then the 2 -dimensional Hausdorff measure of $B \cap C$ is greater than $\zeta_{\delta}^{-1} \rho^{2}$.
\item[-] There is a subsequence of $\left(A_{n}, \psi_{n}\right)$ such that the corresponding sequence $\left\{\alpha_{n}^{-1}(0)\right\}$ converges to $C$ in the following sense: For any $\delta>0$, the following limit exists and is zero:
$$\left.\lim _{n \rightarrow \infty}\left[\sup _{\{x \in C: \operatorname{dist}(x, Z) \geq \delta\}} \operatorname{dist}\left(x, \alpha_{n}^{-1}(0)\right)+\sup _{\left\{x \in \alpha_{n}^{-1}(0): \operatorname{dist}(x, Z) \geq \delta\right\}} \operatorname{dist}(x, C)\right)\right] .$$
\end{itemize}

Proof of Lemma 7.1 To construct $C$, consider first a large positive integer $N$ and a very large positive integer $n$. (Here, a lower bound on $n$ comes from the choice of $N$.) Use Lemma 4.1 to find a set $\Lambda_{n}^{\prime}(N)$ of balls of radius $16^{-N}$ with the following properties: The balls are disjoint, their centers lie on $\alpha_{n}^{-1}(0)$ and have distance at least $4 \cdot 16^{-N}$ from $Z$, and the set $\Lambda_{n}(N)$ of concentric balls of radius $2 \cdot 16^{-N}$ covers the set of point in $\alpha_{n}^{-1}(0)$ with distance $8 \cdot 16^{-N}$ from $Z$. According to Lemma 4.1, when $n$ is sufficiently large, this set $\Lambda_{n}(N)$ has a bound on the number of its elements which is independent of $n$. Let $\nu(N)$ be an integer which is greater than the number of elements in each $\Lambda_{n}(N)$.

Label the centers of the balls in $\Lambda_{n}(N)$ and then add the final point some number of times (if necessary) to make a point $\underline{x}_{n}(N) \equiv\left(x_{n}(1 ; N), \ldots, x_{n}(\nu(N) ; N)\right)$ $\in \times_{\nu(N)} X$. By a diagonalization process, one can find an infinite sequence of indices $n$ (hence relabeled consecutively from 1) so that for each $N$, the sequence $\left\{\underline{x}_{n}(N)\right\}_{n \geq 1}$ converges in $\times_{\nu(N)} X$.

For each $N$, let $\underline{x}(N) \equiv\{x(1, N), \ldots, x(\nu(N), N)\}$ denote the limit of $\left\{\underline{x}_{n}(N)\right\}_{n \geq 1}$. One can think of $\underline{x}(N)$ as either a point in $\times_{\nu(N)} X$, or else an ordered set of $\nu(N)$ points in $X$. Think of $\underline{x}(N)$ in the latter sense, and let $U(N)$ denote the union of the balls of radius $4 \cdot 16^{-N}$ with centers at the points $\underline{x}(N)$ (that is, at $\{x(i, N)\}_{1 \leq i \leq \nu(N)}$ ). Lemma 5.1 of [15] argues that these sets are nested in that $U(N+1) \subset U(N)$. With this understood, set
$$C \equiv \bigcap_{N \geq 1} U(N) .$$
The argument for the asserted properties of $C$ is essentially the same as that for Lemma 5.2 in Section 5c of [15]. In this regard, Lemma 4.1 here replaces Lemma 3.6 in [15], and Proposition 4.2 here replaces Proposition 4.4 in [15]. The details are straightforward and left to the reader.
c) A positive cohomology assignment

The purpose of this subsection is to give a more precise characterization of the distribution $\mathcal{F}$.

To begin, note that the construction of $C$ indicated above can be used (as in the proof of Lemma 5.3 in [15]) to prove that the current $\mathcal{F}$ is type 1-1 in the sense that $\mathcal{F}(\mu)=0$ when $\mu$ is a section of the subbundle $K^{-1} \subset \Lambda_{+}$. The fact that $\mathcal{F}$ is type 1-1 is implied by Lemma 7.2 below which is a significantly stronger assertion:

Lemma 7.2 Let $D \subset \mathbb{C}$ denote the standard, unit disc, and let $\sigma: D \rightarrow X-Z$ be a smooth map which extends to the closure, $\underline{D}$, of $D$ as a continuous map that sends $\partial \underline{D}$ into $X-C$. Then, $\left\{2^{-1} \int_{D} \sigma^{*}\left(\frac{i}{2 \pi}\left(F_{A_{n}}-F_{A^{0}}\right)\right)\right\}_{n \geq 1}$ converges, and the limit, $I(\sigma) \in \mathbb{Z}$. Moreover,
\begin{itemize}
\item[-] $I(\sigma)=0$ if $\sigma(D) \cap C=\emptyset$.
\item[-] $I(\sigma)>0$ if $\sigma$ is a pseudo-holomorphic map and $\sigma^{-1}(C) \neq \emptyset$.
\end{itemize}

Proof of Lemma 7.2 The arguments which prove Lemma 6.2 in [15] are of a local character and so can be brought to bear directly to give Lemma 7.2.

The discussion surrounding Lemma 6.2 in [15] concerns the notion of a positive cohomology assignment for $C$. The latter is defined as follows: First, let $D \subset \mathbb{C}$ be the standard unit disk again. A map $\sigma: D \rightarrow X-Z$ is called admissible when $\sigma$ extends as a continuous map to the closure, $\underline{D}$, of $D$ which maps $\partial \underline{D}$ into $X-C$. A positive cohomology assignment specifies an integer, $I(\sigma)$, for each admissible map $\sigma$ from $D$ to $X-Z$ subject to the following constraints:
\begin{itemize}
\item[-] If $\sigma(D) \subset X-C$, then $I(\sigma)=0$.
\item[-] A homotopy $h:[0,1] \times D \rightarrow X$ is called admissible when it extends as a continuous map from $[0,1] \times \underline{D}$ into $X$ that sends $[0,1] \times \partial \underline{D}$ to $X-C$. If $h$ is an admissible homotopy, then $I(h(1, \cdot))=I(h(0, \cdot))$.
\item[-] Let $\sigma: D \rightarrow X$ be admissible and suppose that $\theta: D \rightarrow D$ is a proper, degree $k$ map. Then $I(\sigma \cdot \theta)=k I(\sigma)$.
\item[-] Suppose that $\sigma: D \rightarrow X$ is admissible and that $\sigma^{-1}(C)$ is contained in a disjoint union $\cup_{\nu} D_{\nu} \subset D$, where each $D_{\nu}=\theta_{\nu}(D)$ with $\theta_{\nu}: D \rightarrow D$ being an orientation preserving embedding. Then $I(\sigma)=\sum_{\nu} I\left(\sigma \cdot \theta_{\nu}\right)$.
\item[-] If $\sigma$ is admissible and pseudo-holomorphic with $\sigma^{-1}(C) \neq \emptyset$, then $I(\sigma)>$ 0. (7.8)
\end{itemize}
The next result follows from Lemma 7.2 and the particulars of the definition of $\mathcal{F}$ in (7.3) as a limit.

Lemma 7.3 Let $C$ be as in Lemma 7.1 and let $I(\cdot)$ be as described in Lemma 7.2. Then $I(\cdot)$ defines a positive cohomology assignment for $C$.

Proof of Lemma 7.3 Use the proof of Lemma 6.2 in [15].
d) $C$ as a pseudo-holomorphic submanifold

Proposition 6.1 in [15] asserts that a closed set in a compact, symplectic 4-manifold with finite 2-dimensional Hausdorff measure and a positive cohomology assignment is the image of a compact, complex curve by a pseudoholomorphic map. (Note, however that the proof of Proposition 6.1 in [15] has errors which occur in Section 6e of [15], and so the reader is referred to the revised proof in the version which is reprinted in [20].) It is important to realize that the assumed compactness of $X$ in the statement of Proposition 6.1 of [15] is present only to insure that the complex curve in question is compact. In particular, the proof of Proposition 6.1 in [15] from the reprinted version in [20] yields:

Proposition 7.1 Let $Y$ be a 4-dimensional symplectic manifold with compatible almost complex structure. Suppose that $C \subset Y$ is a closed subset with the following properties:
\begin{itemize}
\item[-] The restriction of $C$ to any open $Y^{\prime} \subset Y$ with compact closure has finite 2 -dimensional Hausdorff measure.
\item[-] $C$ has a positive cohomology assignment.
\end{itemize}

Then the following are true:
\begin{itemize}
\item[-] There is a smooth, complex curve $C^{0}$ (not necessarily compact) with a proper, pseudo-holomorphic map $f: C^{0} \rightarrow Y$ with $C=f\left(C^{0}\right)$.
\item[-] There is a countable set $\Lambda^{0} \subset C^{0}$ with no accumulation points such that $f$ embeds each component $C^{0}-\Lambda^{0}$.
\item[-] Here is an alternate description of the cohomology assignment for $C$ : Let $\sigma: D \rightarrow Y$ be an admissible map, and let $\sigma^{\prime}$ be any admissible perturbation of $\sigma$ which is transverse to $f$ and which is homotopic to $\sigma$ via an admissible homotopy. Construct the fibered product $T \equiv\{(x, y) \in$ $\left.D \times C_{1}: \sigma^{\prime}(x)=\varphi(y)\right\}$. This $T$ is a compact, oriented 0 -manifold, so a finite set of signed points; and the cohomology assignment gives $\sigma$ the sum of the signs of the points of $T$.
\end{itemize}

Proof of Proposition 7.1 As remarked at the outset, the proof of Proposition 6.1 in [15] from the revised version in [20] can be brought to bear here with negligible modifications.

Lemma 7.3 enables Proposition 7.1 to be applied to the set $C$ from Lemma 7.1. In particular, one can conclude that $C$ is the image of a smooth, complex curve $C^{0}$ via a proper, pseudo-holomorphic
$$f: C^{0} \rightarrow X-Z .$$
Moreover, $f$ can be taken to be an embedding upon restriction to each component of the complement in $C^{0}$ of a countable set with no accumulation points. In particular, it follows that $C$ restricts to any open subset with compact closure in $X-Z$ as a pseudo-holomorphic subvariety.
e) The energy of $\boldsymbol{C}$

The purpose of this subsection is to state and prove

Lemma 7.4 The set $C$ from Lemma 7.1 is a finite energy, pseudo-holomorphic subvariety in the sense of Definition 1.1. Furthermore, there are universal constants $\zeta_{1}, \zeta_{2}$ (independent of the metric) such that
$$\int_{C} \omega \leq \zeta_{1} e_{\omega}(s)+\zeta_{2} \int_{X}\left(\left|R_{g}\right|+\left|W_{g}^{+}\right|\right)|\omega| d \operatorname{vol}_{g} .$$
In this equation, $e_{\omega}(s)$ equals the evaluation on the fundamental class of $X$ of the cup product of $c_{1}(L)$ with $[\omega]$. Meanwhile, $R_{g}$ is the scalar curvature for the metric $g$, and $W_{g}^{+}$is the metric's self-dual, Weyl curvature. Also, dvol $_{g}$ is the metric's volume form.

Proof of Lemma 7.4 First of all, define an equivalence relation on the components of $C^{0}$ (from (7.9)) by declaring two components to be equivalent if their images via $f$ coincide. The quotient by this equivalence relation defines another smooth, complex curve, $C_{0}$, together with a proper, pseudo-holomorphic map $\varphi: C_{0} \rightarrow X-Z$ whose image is $C$. Moreover, there is a countable set $\Lambda_{0} \subset C_{0}$ which has no accumulation points and whose complement is embedded by $\varphi$.

With the preceding understood, it remains only to establish that $C$ has finite energy. For this purpose, fix $\delta>0$ and re-introduce the bump function $\chi_{\delta}$. (Remember that $\chi_{\delta}$ vanishes where the distance to $Z$ is greater than $2 \delta$, and it equals 1 where the distance to $Z$ is less than $\delta$.) Since $\omega$ restricts to $C$ as a positive form, it follows that $C$ has finite energy if and only if
$$\lim _{\delta \rightarrow 0} \int_{C}\left(1-\chi_{\delta}\right) \omega$$
exists, and this limit exists if and only if the set $\left\{\int_{C}\left(1-\chi_{\delta}\right) \omega\right\}_{\delta>0}$ is bounded in $[0, \infty)$. Thus, the task is to find a $\delta$-independent upper bound for this set.

With the preceding understood, remark first that Proposition 7.1 as applied to $C$ yields
$$\int_{C}\left(1-\chi_{\delta}\right) \omega \leq \int_{C^{0}} f^{*}\left(\left(1-\chi_{\delta}\right) \omega\right)=\mathcal{F}\left(\left(1-\chi_{\delta}\right) \omega\right) .$$
Now, given $\varepsilon>0$, the right-hand expression in (7.12) is no greater than
$$\mathcal{F}_{n}\left(\left(1-\chi_{\delta}\right) \omega\right)+\varepsilon$$
when $n$ is sufficiently large. Moreover, as $\mathcal{F}_{n}$ is defined on all smooth forms, the first term in (7.13) is equal to
$$(4 \pi)^{-1} \int_{X}\left(1-\chi_{\delta}\right) i F_{A} \wedge \omega-(4 \pi)^{-1} \int_{X}\left(1-\chi_{\delta}\right) i F_{A^{0}} \wedge \omega .$$
with $A=A_{n}$.
Both terms in (7.14) are $\delta$ dependent and so must be analyzed further. In particular, Lemma 7.4 follows with the exhibition of a bound on these terms by $\zeta\left(e_{\omega}(s)+\int_{X}\left(\left|R_{g}\right|+\left|W_{g}^{+}\right|\right)|\omega| \mathrm{dvol}_{g}\right.$.
For the right most term, remark that only $F_{A^{0}}^{+}$appears in (7.14) (since $\omega$ is self dual), and a calculation (which is left to the reader) finds a universal constant $\zeta$ with the property that
$$\left|F_{A^{0}}^{+}\right| \leq \zeta\left(|\nabla \underline{\omega}|^{2}+\left|R_{g}\right|+\left|W_{g}^{+}\right|\right) .$$
Here, $\underline{\omega} \equiv \omega /|\omega|$. Equation (7.15) implies that the right most term in (7.14) is not greater than
$$\zeta\left(\int_{X}|\omega||\nabla \underline{\omega}|^{2}+\int_{X}\left(\left|R_{g}\right|+\left|W_{g}^{+}\right|\right)|\omega| \mathrm{dvol}_{g}\right) .$$
Here the constant $\zeta$ is also metric independent. Meanwhile, the first integral in (7.16) is bounded by $\zeta \int_{X}\left(\left|R_{g}\right|+\left|W_{g}^{+}\right|\right)|\omega|$ dvol $_{g}$ which can be seen by integrating both sides of (3.7) and then integrating by parts to eliminate the $d^{*} d|\omega|$ term. This means in particular that the right most term in (7.16) is bounded by a universal multiple of $\int_{X}\left(\left|R_{g}\right|+\left|W_{g}^{+}\right|\right)|\omega| \mathrm{dvol}_{g}$.
Now consider the left most term in (7.14). For this purpose, use (2.9) to identify the latter with
$$(8 \sqrt{2} \pi)^{-1} r \int_{X}\left(1-\chi_{\delta}\right)|\omega|\left(2^{-1 / 2}|\omega|-|\alpha|^{2}+|\beta|^{2}\right) .$$
One should compare this expression for that implied by (2.9) for $e_{\omega}(s)$, namely
$$2^{-1} e_{\omega}(s)=(8 \sqrt{2} \pi)^{-1} r \int_{X}|\omega|\left(2^{-1 / 2}|\omega|-|\alpha|^{2}+|\beta|^{2}\right) .$$
In particular, note that (7.18) implies the identity
$$(8 \sqrt{2} \pi)^{-1} r \int_{X}|\omega||\beta|^{2}=4^{-1} e_{\omega}(s)-(16 \sqrt{2} \pi)^{-1} r \int_{X}|\omega|\left(2^{-1 / 2}|\omega|-|\psi|^{2}\right) .$$
It then follows from the second line of (3.2) (and the integration of (3.7)) that
$$(8 \sqrt{2} \pi)^{-1} r \int_{X}|\omega||\beta|^{2}=\zeta\left(e_{\omega}(s)+\int_{X}\left(\left|R_{g}\right|+\left|W_{g}^{+}\right|\right)|\omega| \mathrm{dvol}_{g}\right) .$$
This last bound can now be plugged back into bounding (7.17) since the expression in (7.17) is no greater than
$$(8 \sqrt{2} \pi)^{-1}\left(r \int_{X} \chi_{\delta}|\omega|\left|\left(2^{-1 / 2}|\omega|-|\psi|^{2}\right)\right|+2 r \int_{X}|\omega||\beta|^{2}\right) .$$

Thus, (7.20) and the second line of (3.2) bound the left most term in (7.14) by the required $\zeta\left(e_{\omega}(s)+\int_{X}\left(\left|R_{g}\right|+\left|W_{g}^{+}\right|\right)|\omega| \mathrm{dvol}_{g}\right)$.
f) Intersections with the linking 2-spheres

After Lemma 7.4, all that remains to prove Theorem 2.2 is to establish that Lemma 7.4's pseudo-holomorphic subvariety $C$ has intersection number equal to 1 with any 2 -sphere in $X-Z$ which has linking number 1 with $Z$.

To prove this last assertion, consider that each $\alpha_{n}$ defines a section of the bundle $E$ whose square is given in (6.1) as $\left.L\right|_{X-Z} K$. Now, $L$ is trivial over a linking 2 -sphere for $Z$ as $L$ is a bundle over the whole of $X$. This means that $E$ restricts to a linking 2-sphere of $Z$ as the square root of the restriction of $K$. Moreover, according to Lemma 2.1, the restriction of $K$ to a linking 2-sphere has degree 2 , so $E$ restricts to such a 2 -sphere with degree 1 . This means that the current $\mathcal{F}_{n}$ in (7.1) evaluates as 1 on any closed form which represents the Thom class of a fixed, linking 2-sphere. In particular, the same must be true for a limit current $\mathcal{F}$, and the nature of the convergence in Proposition 7.1 implies that $C$ has intersection number 1 with such a 2-sphere.

Achnowledgement This research was supported in part by the National Science Foundation.

\section*{References}
\begin{itemize}
\item[] [1] MF Atiyah, I Singer, NJ Hitchin, Self-duality in 4-dimensional Riemannian geometry, Proc. Roy. Soc. London Ser. A, 362 (1978) 425-461
\item[] [2] S K Donaldson, Symplectic submanifolds and almost complex geometry, Jour. Diff. Geom. 44 (1996) 666-705
\item[] [3] D S Freed, K K Uhlenbeck, Instantons and Four-Manifolds, Springer-Verlag (1984)
\item[] [4] M Gromov, Pseudo-holomorphic curves in symplectic manifolds, Invent. Math. 82 (1985) 307-347
\item[] [5] K Honda, Harmonic forms for generic metrics, preprint (1997)
\item[] [6] M Hutchings, Y-J Lee, Circle-valued Morse theory, $R$-torsion and Seiberg-Witten invariants of 3 -manifolds, Topology, to appear
\item[] [7] M Hutchings, Y-J Lee, Circle-valued Morse theory and Reidemeister torsion, preprint (1997)
\item[] [8] D Kotschick, P B Kronheimer, TS Mrowka, in preparation
\end{itemize}
\begin{itemize}
\item[] [9] C LeBrun, Yamabe constants and the perturbed Seiberg-Witten equations, Commun. Anal. Geom. 5 (1997) 535-553
\item[] [10] D McDuff, D Salamon, J-Holomorphic Curves and Quantum Cohomology, American Mathematical Society, Providence (1996)
\item[] [11] J M Morgan, The Seiberg-Witten Equations and Applications to the Topology of Smooth 4-Manifolds, Mathematical Notes, 44, Princeton University Press (1996)
\item[] [12] C B Morrey, Multiple Integrals in the Calculus of Variations, Springer-Verlag (1966)
\item[] [13] P Pansu, Pseudo-holomorphic curves in symplectic manifolds, from: "Holomorphic Curves in Symplectic Geometry", (M Audin and F Lafontaine, editors) Progress in Math. 117, Birkhäuser (1994) 233-250
\item[] [14] T Parker, J Wolfson, Pseudo-holomorphic maps and bubble trees, J. Geom. Anal. 3 (1993) 63-98
\item[] [15] CH Taubes, $S W \Rightarrow G r$ : From the Seiberg-Witten equations to pseudoholomorphic curves, J. Amer. Math. Soc. 9 (1996) 845-918
\item[] [16] C H Taubes, The structure of pseudo-holomorphic subvarieties for a degenerate almost complex structure and symplectic form on $S^{1} \times B^{3}$, Geometry and Topology, 2 (1998) 221-332
\item[] [17] CH Taubes, The geometry of the Seiberg-Witten invariants, from: "Surveys in Differential Geometry, 1996", (S T Yau, editor) International Press, to appear
\item[] [18] C H Taubes, The Seiberg-Witten and the Gromov invariants, Math. Res. Letters 2 (1995) 221-238.
\item[] [19] CH Taubes, $S W=G r$ : Counting curves and connections, preprint (1997)
\item[] [20] CH Taubes, $S W \Rightarrow G r$ : From the Seiberg-Witten equations to pseudoholomorphic curves, from: "Proceedings of the First IP Lecture Series, Vol. II", (R Wentworth, editor), International Press, to appear
\item[] [21] V Turaev, A combinatorial formula for the Seiberg-Witten invariants of 3-manifolds, preprint (1998)
\item[] [22] R Ye, Gromov's compactness theorem for pseudo-holomorphic curves, Trans. Amer. Math. Soc. 342 (1994) 671-694
\item[] [23] E Witten, Monopoles and 4-manifolds, Math. Res. Letters, 1 (1994) 769-796
\end{itemize}