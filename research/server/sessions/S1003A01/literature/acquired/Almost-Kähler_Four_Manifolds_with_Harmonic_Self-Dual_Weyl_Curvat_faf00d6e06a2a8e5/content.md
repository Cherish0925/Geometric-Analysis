---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 2311_16729v1.pdf
converter: mathpix
format: mmd
---

\title{
ALMOST-KÄHLER FOUR MANIFOLDS WITH HARMONIC SELF-DUAL WEYL CURVATURE
}

\author{
INYOUNG KIM
}

\begin{abstract}
We show that a compact almost-Kähler four manifold $(M, g, \omega)$ with harmonic self-dual Weyl curvature and constant scalar curvature is Kähler if $c_{1} \cdot \omega \geq 0$. We also prove an integral curvature inequality for compact almost-Kähler four manifolds with harmonic self-dual Weyl curvature.
\end{abstract}

\section*{1. Introduction}

Let $(M, \omega)$ be a symplectic four-manifold. Then $(M, \omega)$ admits a compatible almostcomplex structure $J$, that is, $\omega(X, Y)=\omega(J X, J Y)$ and $\omega(v, J v)>0$ for any nonzero $v \in T M$ [12]. If we define a metric by $g(X, Y):=\omega(X, J Y)$, then $(M, g, \omega, J)$ is called an almost-Kähler structure. When $J$ is integrable, $\omega$ is parallel and this defines a Kähler structure.

The curvature operator of an oriented four-dimensional riemannian manifold decomposes according to the decomposition of $\Lambda^{2}=\Lambda^{+} \oplus \Lambda^{-}$as follows.
$$\Re=\left(\begin{array}{c|c}
W_{+}+\frac{s}{12} I & r i c_{0} \\
\hline r i c_{0}^{*} & W_{-}+\frac{s}{12} I
\end{array}\right)$$

If $W_{-}=0$, then $g$ is called to be self-dual. If $r i c_{0}=0$, then $g$ is called to be Einstein. A compact almost-Kähler Einstein manifold with nonnegative scalar curvature is Kähler [14]. In a four-dimensional case, it was shown in [8] that a compact almost-Kähler four manifold with $\delta W_{+}=0$ and nonnegative scalar curvature is Kähler with constant scalar curvature.

Using methods in proofs in [8], we prove two results. First, we show that a compact almost-Kähler four manifold with $\delta W_{+}=0$ and constant scalar curvature is Kähler if $c_{1} \cdot \omega \geq 0$. This shows in particular a compact almost-Kähler Einstein four manifold with $c_{1} \cdot \omega \geq 0$ is Kähler-Einstein.

Keywords: almost-Kähler, four manifold, self-dual Weyl curvature, Einstein metric
MSC: 53C21, 53C24, 53C25.
Republic of Korea
Email address: kiysd5@gmail.com

This result is not new since there is a more general result in [4]. On the other hand, our hypothesis $\delta W_{+}=0$ is weaker than an Einstein condition.

Secondly, we show that for a compact almost-Kähler four-manifold with $\delta W_{+}=0$, we have
$$\int_{M} \frac{s^{2}}{24} d \mu \geq \int_{M}\left|W_{+}\right|^{2} d \mu$$
The same result was shown in [10]. Our proof entirely depends on the formulas given in [8]. Using this inequality, it was shown that a compact almost-Kähler four manifold with $J$-invariant Ricci tensor is self-dual Kähler-Einstein if the scalar curvature is constant and $b_{-}=0$ [5]. We include a proof in case of compact almost-Kähler Einstein four manifolds.

\section*{2. Almost-Kähler four manifolds with curvature conditions}

Dräghici showed that a compact almost-Kähler four manifold $(M, g, \omega)$ with $J$-invariant Ricci tensor and constant scalar curvature is Kähler if $c_{1} \cdot \omega \geq 0$ [4]. In this article, we consider $\delta W_{+}=$condition instead of $J$-invariant Ricci tensor. Let $(M, g, \omega)$ be a compact almost-Kähler four manifold. Then $\omega$ is a self-dual harmonic 2-form with length $\|\omega\|=\sqrt{2}$ and this gives the following formula.
$$0=\Delta \omega=\nabla^{*} \nabla \omega-2 W_{+}(\omega)+\frac{s}{3} \omega .$$
LeBrun showed that this formula with $\delta W_{+}=0$ implies the following integral equality [8].
Proposition 1. (LeBrun) Let $(M, g, \omega)$ be a compact almost-Kähler four-manifold with $\delta W_{+}=0$. Then
$$\int_{M} s W_{+}(\omega, \omega) d \mu=8 \int_{M}\left(\left|W_{+}\right|^{2}-\frac{1}{2}\left|W_{+}(\omega)^{\perp}\right|^{2}\right) d \mu$$

The proof of Lemma 2 in [8] contains a stronger result that the statement in Lemma 2.
Lemma 1. (LeBrun) Let $(M, g, \omega)$ be an almost-Kähler four manifold. Then
$$\left|W_{+}\right|^{2}-\left|W_{+}(\omega)^{\perp}\right|^{2} \geq \frac{3}{8}\left[W_{+}(\omega, \omega)\right]^{2},$$
with equality at points where $W_{+}(\omega)^{\perp}=0$.
Lemma 1 implies in particular that
$$\left|W_{+}\right|^{2}-\frac{1}{2}\left|W_{+}(\omega)^{\perp}\right|^{2} \geq \frac{3}{8}\left[W_{+}(\omega, \omega)\right]^{2} .$$
Using this in Proposition 1, we get the following result [8].
Proposition 2. (LeBrun) Let $(M, g, \omega)$ be a compact almost-Kähler four-manifold with $\delta W_{+}=0$. Then
$$\int_{M} W_{+}(\omega, \omega)\left(W_{+}(\omega, \omega)-\frac{s}{3}\right) d \mu \leq 0$$

Theorem 1. Let $(M, g, \omega)$ be a compact almost-Kähler four-manifold with $\delta W_{+}=0$ and constant scalar curvature. If $c_{1} \cdot \omega \geq 0$, then the scalar curvature is nonnegative and $(M, g, \omega)$ is a Kähler surface with constant scalar curvature.

Proof. We note that
$$s^{*}:=2 R(\omega, \omega)=2\left(W_{+}(\omega, \omega)+\frac{s}{12}|\omega|^{2}\right) .$$
From this, we get
$$W_{+}(\omega, \omega)=\frac{s^{*}}{2}-\frac{s}{6} .$$
Using this in Proposition 2, we get
$$\int_{M}\left(3 s^{*}-s\right)\left(s^{*}-s\right) d \mu \leq 0$$
Suppose $s$ is negative constant. Then from
$$0 \leq 4 \pi c_{1} \cdot \omega=\int_{M} \frac{s+s^{*}}{2} d \mu$$
we have
$$\begin{gathered}
\int_{M}\left(3 s^{*}-s\right)\left(s^{*}-s\right) d \mu=\int_{M}\left(3\left(s^{*}\right)^{2}-4 s^{*} s+s^{2}\right) d \mu \\
=\int_{M}\left(-4 s\left(s^{*}+s\right)+5 s^{2}+3\left(s^{*}\right)^{2}\right) d \mu \geq 0
\end{gathered}$$
Thus, we get $s=0$, which is a contradiction. Thus, $s \geq 0$. One of the main results in [8] is that a compact almost-Kähler four manifold with $s^{*} \geq 0$ and $\delta W_{+}=0$ is a Kähler surface with constant scalar curvature. Using
$$0=\frac{1}{2} \Delta|\omega|^{2}+|\nabla \omega|^{2}-2 W_{+}(\omega, \omega)+\frac{s}{3}|\omega|^{2}=|\nabla \omega|^{2}-2 W_{+}(\omega, \omega)+\frac{s}{3}|\omega|^{2},$$
we get
$$s^{*}=2\left(W_{+}(\omega, \omega)+\frac{s}{12}|\omega|^{2}\right)=s+|\nabla \omega|^{2} .$$
Thus, $s^{*}-s \geq 0$, with equality on $M$ if and only if ( $M, g, \omega$ ) is Kähler. Then if $s^{*} \geq 0$, we have
$$\int_{M}\left(3 s^{*}-s\right)\left(s^{*}-s\right) d \mu=\int_{M}\left(s^{*}-s\right)^{2}+2 s^{*}\left(s^{*}-s\right) d \mu \geq 0$$
Since $\int_{M}\left(3 s^{*}-s\right)\left(s^{*}-s\right) d \mu \leq 0$ by Proposition 2, we get $s^{*} \equiv s$ if $s^{*} \geq 0$. Since $s^{*} \geq 0$ if $s \geq 0$, we get a compact almost-Kähler four manifold with $\delta W_{+}=0$ is Kähler if $s \geq 0$. We note that $s$ on a Kähler surface is constant if $\delta W_{+}=0$. \(\square\)

Since an Einstein metric has $\delta W_{+}=0$ and constant scalar curvature, we get the following corollary.

Corollary 1. Let $(M, g, \omega)$ be a compact almost-Kähler Einstein four manifold. Suppose $c_{1} \cdot \omega \geq 0$. Then $(M, g, \omega)$ is Kähler-Einstein.

This result can be also proved from Drăgichi's result [4] since an almost-Kähler Einstein four manifold has $J$-invariant Ricci tensor and has constant scalar curvature.

Let $(M, \omega)$ be a symplectic four manifold. If $c_{1} \cdot \omega>0$, then by [15], $b_{+}=1$. If a symplectic four manifold has $b_{+}=1$ and $c_{1} \cdot \omega>0$, then $M$ is diffeomorphic to a rational or ruled surface [11]. Conversely, there is a following result [9].

Proposition 3. (LeBrun) Let $M$ be a smooth four-manifold which is diffeomorphic to a rational or ruled surface. Suppose $2 \chi+3 \tau \geq 0$. Then $c_{1} \cdot \omega>0$ for any symplectic form $\omega$ on $M$.

This gives the following Corollary, which was pointed out in [2].
Corollary 2. Let $M$ be a smooth four manifold which is diffeomrophic to a rational or ruled surface. Then an almost-Kähler Einstien metric $(M, g, \omega)$ is Kähler-Einstein with positive scalar curvature.

Proof. From
$$2 \chi+3 \tau=\frac{1}{4 \pi^{2}} \int_{M}\left(\frac{s^{2}}{24}+2\left|W_{+}\right|^{2}-\frac{\left|r i c_{0}\right|^{2}}{2}\right) d \mu$$
we get $2 \chi+3 \tau \geq 0$ for an Einstein metric. By Corollary 1, $(M, g, \omega)$ is Kähler-Einstein since $c_{1} \cdot \omega>0$ by Proposition 3. For a Kähler surface, we have
$$4 \pi c_{1} \cdot[\omega]=\int_{M} s d \mu$$
From this, we get $s>0$. \(\square\)

We prove Proposition 1 in case of compact almost-Kähler Einstein four manifolds using the curvature formula of Blair connection given in [7]. Let $(M, g, \omega)$ be an almost-Kähler four manifold. We consider
$$\tilde{\nabla}_{X} Y:=\nabla_{X} Y-\frac{1}{2} J\left(\nabla_{X} J\right) Y,$$
where ∇ is Levi-Civita connection. Then $\tilde{\nabla}$ induces the connection on the anti-canonical line bundle. Then the curvature of $\tilde{\nabla}$ on the anti-canonical line bundle of an almost-Kähler Einstien four manifold is given by
$$i F_{\tilde{\nabla}}=W_{+}(\omega)^{\perp}+\frac{s+s^{*}}{8} \omega+\frac{s-s^{*}}{8} \hat{\omega} .$$
The anti-self-dual 2-form $\hat{\omega}$ is defined on $U$ and $|\hat{\omega}|=\sqrt{2}$, where $U=\left\{p \in M \mid s^{*}(p) \neq s(p)\right\}$.
Corollary 3. Let $(M, g, \omega)$ be a compact almost-Kähler Einstein four-manifold. Then
$$\int_{M}\left(\frac{s s^{*}}{8}-\frac{s^{2}}{24}\right) d \mu=\int_{M}\left(2\left|W_{+}\right|^{2}-\left|W_{+}(\omega)^{\perp}\right|^{2}\right) d \mu$$
Proof. For a compact almost-Kähler Einstein four-manifold, we have
$$c_{1}^{2}=\frac{1}{4 \pi^{2}} \int_{M}\left(\left|i F_{\nabla}^{+}\right|^{2}-\left|i F_{\nabla}^{-}\right|^{2}\right) d \mu$$
$$=\frac{1}{4 \pi^{2}} \int_{M}\left(\left|W_{+}(\omega)^{\perp}\right|^{2}+\left(\frac{s+s^{*}}{8}\right)^{2}|\omega|^{2}-\left(\frac{s-s^{*}}{8}\right)^{2}|\hat{\omega}|^{2}\right) d \mu$$

Using
$$c_{1}^{2}=2 \chi+3 \tau=\frac{1}{4 \pi^{2}} \int_{M}\left(\frac{s^{2}}{24}+2\left|W_{+}\right|^{2}\right) d \mu$$
the result follows. \(\square\)

\section*{3. Integral curvature inequality}

Using Seiberg-Witten theory, LeBrun showed the following result [6].
Theorem 2. (LeBrun) Let $(M, g)$ be a compact, Einstein four manifold. Assume $M$ admits an almost-complex structure $J$ for which the Seiberg-Witten invariant is nonzero. Suppose $M$ is not finitely covered by $T^{4}$. Then with respect to the orientation by $J, \chi \geq 3 \tau$. Moreover, $\chi=3 \tau$ if and only if up to rescaling, the universal cover of $(M, g)$ is complexhyperbolic 2-space with the standard metric.

The following result was also shown in [10].
Theorem 3. Let $(M, g, \omega)$ be a compact almost-Kähler four-manifold with $\delta W_{+}=0$. Then $\int_{M} \frac{s^{2}}{24} d \mu \geq \int_{M}\left|W_{+}\right|^{2} d \mu$, with equality if and only if $(M, g, \omega)$ is Kähler with constant scalar curvature.

Proof. By Proposition 1, we have
$$\int_{M}\left|W_{+}\right|^{2} d \mu=\int_{M}\left(\left(\left|W_{+}(\omega)^{\perp}\right|^{2}-\left|W_{+}\right|^{2}\right)+\frac{s s^{*}}{8} d \mu-\frac{s^{2}}{24}\right) d \mu$$
Using Lemma 1, we get
$$\left|W_{+}\right|^{2}-\left|W_{+}(\omega)^{\perp}\right|^{2} \geq \frac{3}{8}\left|W_{+}(\omega, \omega)\right|^{2} .$$
Then we get
$$\begin{gathered}
\int_{M} \frac{s^{2}}{24} d \mu-\int_{M}\left|W_{+}\right|^{2} d \mu \geq \int_{M}\left(\frac{s^{2}}{24}+\frac{3}{8}\left|W_{+}(\omega, \omega)\right|^{2}-\frac{s s^{*}}{8}+\frac{s^{2}}{24}\right) d \mu \\
=\int_{M}\left(\frac{s^{2}}{12}+\frac{3}{8}\left(\frac{s^{*}}{2}-\frac{s}{6}\right)^{2}-\frac{s s^{*}}{8}\right) d \mu=\int_{M} \frac{9\left(s^{*}-s\right)^{2}}{96} d \mu \geq 0
\end{gathered}$$
Moreover, $\int_{M} \frac{s^{2}}{24} d \mu=\int_{M}\left|W_{+}\right|^{2} d \mu$ if and only if $s^{*} \equiv s$, which implies ( $M, g, \omega$ ) is Kähler. \(\square\)

Using this, we get the following result in case of almost-Kähler Einstein four manifolds without using Seiberg-Witten theory.

Corollary 4. Let $(M, g, \omega)$ be a compact almost-Kähler Einstein four-manifold. Then we have $\chi \geq 3 \tau$, with equality if and only if $(M, g, \omega)$ is self-dual Kähler-Einstein.

Proof. From the following formulas,
$$\begin{gathered}
\chi=\frac{1}{8 \pi^{2}} \int_{M}\left(\frac{s^{2}}{24}+\left|W_{+}\right|^{2}+\left|W_{-}\right|^{2}-\frac{\left|r i c_{0}\right|^{2}}{2}\right) d \mu \\
\tau=\frac{1}{12 \pi^{2}} \int_{M}\left(\left|W_{+}\right|^{2}-\left|W_{-}\right|^{2}\right) d \mu
\end{gathered}$$
we have
$$\chi-3 \tau=\frac{1}{8 \pi^{2}} \int_{M}\left(\frac{s^{2}}{24}-\left|W_{+}\right|^{2}+3\left|W_{-}\right|^{2}-\frac{\left|r i c_{0}\right|^{2}}{2}\right) d \mu$$
For an Einstein metric, we have $\delta W_{+}=0$, and therefore by Theorem 3, we get
$$\chi-3 \tau \geq 0$$
with equality if and only if $(M, g, \omega)$ is Kähler-Einstein and self-dual. \(\square\)

Corollary 5. Let $(M, g, \omega)$ be a compact almost-Kähler Einstein four manifold. Suppose $b_{-}=0$. Then $(M, g, \omega)$ is self-dual Kähler-Einstein and $b_{1}=0$.

Proof. By Corollary 4, we have $\chi \geq 3 \tau$. Since $\chi=2-b_{1}+b_{+}-b_{3}$ and $\tau=b_{+}$, we have
$$\chi-3 \tau=2-b_{1}-b_{3}-2 b_{+} \geq 0 .$$
Since $b_{+} \geq 1$, we get $b_{1}=b_{3}=0$ and $b_{+}=1$. Moreover, $\chi=3 \tau$. The result follows from Corollary 4. \(\square\)

Corollary 6. (Satoh [13]) Let $(M, g, \omega)$ be a compact almost-Kähler four manifold with $\delta W_{+}=0$. Suppose $\int_{M} s^{2} d \mu=32 \pi^{2}(2 \chi+3 \tau)$. Then $(M, g, \omega)$ is Kähler-Einstein.

Proof. From $\int_{M} s^{2} d \mu=32 \pi^{2}(2 \chi+3 \tau)$, we get
$$\int_{M}\left(2\left(\frac{s^{2}}{24}-\left|W_{+}\right|^{2}\right)+\frac{\left|r i c_{0}\right|^{2}}{2}\right) d \mu=0 .$$
Since $\int_{M} \frac{s^{2}}{24} d \mu \geq \int_{M}\left|W_{+}\right|^{2} d \mu$, we get $\int_{M} \frac{s^{2}}{24} d \mu=\int_{M}\left|W_{+}\right|^{2} d \mu$ and $r i c_{0}=0$. Then by Theorem 3, $(M, g, \omega)$ is Kähler-Einstein. \(\square\)

Corollary 7. Let $(M, g, \omega)$ be a compact simply connected almost-Kähler Einstein four manifold with degenerate spectrum of $W_{+}$. Then $(M, g, \omega)$ is Kähler-Einstein.

Proof. By Derdziński's theorem [3], there exists a Kähler metric $h$ which is conformally equivalent to $g$ or $W_{+}=0$. Suppose $W_{+} \neq 0$. Since $L^{2}$-norm of $W_{+}$is conformally invariant, by Theorem 3, we have
$$\int_{M} \frac{s_{g}^{2}}{24} d \mu_{g} \geq \int_{M}\left|W_{+, g}\right|^{2} d \mu_{g}=\int_{M}\left|W_{+, h}\right|^{2} d \mu_{h}=\int_{M} \frac{s_{h}^{2}}{24} d \mu_{h}$$

On the other hand, we have
$$\begin{gathered}
2 \chi+3 \tau=\frac{1}{4 \pi^{2}} \int_{M}\left(\frac{s_{g}^{2}}{24}+2\left|W_{+, g}\right|^{2}-\frac{\left|r i c_{0, g}\right|^{2}}{2}\right) d \mu_{g} \\
=\frac{1}{4 \pi^{2}} \int_{M}\left(\frac{s_{h}^{2}}{24}+2\left|W_{+, h}\right|^{2}-\frac{\left|r i c_{0, h}\right|^{2}}{2}\right) d \mu_{h}
\end{gathered}$$
Since $g$ is Einstein, we have
$$\frac{1}{4 \pi^{2}} \int_{M}\left(\frac{s_{g}^{2}}{24}+2\left|W_{+, g}\right|^{2}\right) d \mu_{g} \leq \frac{1}{4 \pi^{2}} \int\left(\frac{s_{h}^{2}}{24}+2\left|W_{+, h}\right|^{2}\right) d \mu_{h}$$
Then we get
$$\int_{M} \frac{s_{g}^{2}}{24} d \mu_{g}=\int_{M}\left|W_{+, g}\right|^{2} d \mu_{g}=\int_{M}\left|W_{+, h}\right|^{2} d \mu_{h}=\int_{M} \frac{s_{h}^{2}}{24} d \mu_{h}$$
From Theorem 3, we get $(M, g, \omega)$ is Kähler-Einstein.
Suppose $W_{+}=0$. From $W_{+}(\omega, \omega)=\frac{s^{*}}{2}-\frac{s}{6}$, we get $s^{*}=\frac{s}{3}$ for an anti-self-dual almostKähler metric. Moreover, there is a point where $s^{*}=s$ unless $5 \chi+6 \tau=0$ [1]. Suppose $5 \chi+6 \tau \neq 0$. Then, $s=0$ since $s$ is constant. Then by [14], $(M, g, \omega)$ is Kähler-Einstein. Suppose $5 \chi+6 \tau=0$. Since $2 \chi+3 \tau \geq 0$ for an Einstien manifolds, we get $\chi \leq 0$. Then, from the following formula,
$$\chi=\frac{1}{8 \pi^{2}} \int_{M}\left(\frac{s^{2}}{24}+\left|W_{+}\right|^{2}+\left|W_{-}\right|^{2}-\frac{\left|r i c_{0}\right|^{2}}{2}\right) d \mu$$
we get $s=0$. \(\square\)

Let $M$ be a smooth oriented four manifold which is diffeomorphic to a rational or ruled surface. Suppose $M$ admits an almost-Kähler structure $(g, \omega)$ and $2 \chi+3 \tau \geq 0$. Then LeBrun showed the following inequality,
$$\int_{M}\left|W_{+}\right|^{2} d \mu \geq \frac{4 \pi^{2}}{3}(2 \chi+3 \tau)(M)$$
For more general results, we refer to [9]. If $M$ admits an almost-Kähler Einstein metric, then from this inequality, we get $\int_{M} \frac{s^{2}}{24} d \mu \leq \int_{M}\left|W_{+}\right|^{2} d \mu$. On the other hand, from Theorem 3, we have $\int_{M} \frac{s^{2}}{24} d \mu \geq \int_{M}\left|W_{+}\right|^{2} d \mu$. Thus, we get the equality and therefore, $(M, g, \omega)$ is Kähler-Einstein positive scalar curvature. This gives another proof for Corollary 2.

Acknowledgments: The author is thankful to Prof. Claude LeBrun for helpful comments.

\section*{References}
\begin{itemize}
\item[] [1] J. Armstrong, On four-dimensional almost Kähler manifolds, Quart. J. Math. Vol 48, Issue 4 (1997), 405-415.
\item[] [2] J. Armstrong, Almost-Kähler Geometry, Ph. D. Thesis, Oxford (1998).
\item[] [3] A. Derdziński, Self-dual Kähler manifolds and Einstein manifolds of dimension four, Compositio Mathematica 49(1983), 405-433.
\item[] [4] T. Drăghici, Almost-Kähler 4-manifolds with J-invariant Ricci tensor, Houston J. Math. 25 (1999), 133-145.
\item[] [5] I. Kim, Almost-Kähler four manifolds with nonnegative biorthogonal curvature, preprint.
\item[] [6] C. LeBrun, Einstein metrics and Mostow rigidity, Math. Res. Lett., 2 (1995), pp. 1-8.
\item[] [7] C. LeBrun, Einstein metrics, Symplectic minimality, and Pseudo-Holomorphic curves, Ann. Glob. An. Geom. 28 (2005), 157-177.
\item[] [8] C. LeBrun, Einstein metrics, harmonic forms, and symplectic four-manifolds, Ann. Glob. An. Geom. 48 (2015), 75-85.
\item[] [9] C. LeBrun, Weyl Curvature, Del Pezzo Surfaces, and Almost-Kähler Geometry, J. Geom. Analysis 25 (2015), 1744-1772.
\item[] [10] C. LeBrun, Curvature in the Balance: The Weyl Functional and Scalar curvature of 4-Manifolds, arXiv: 2203.02528 [math. DG], to appear in Pure Appl. Math. Q.
\item[] [11] A. -K. Liu, Some new applications of general wall-crossing formula, Gompf's conjecture and its applications, Math. Res. Lett., 3 (1996), pp. 569-585.
\item[] [12] D. McDuff and D. Salamon, Introduction to Symplectic Topology, Oxford University Press, 1998.
\item[] [13] H. Satoh, 4-dimensional almost Kähler manifolds and $L^{2}$-scalar curvature functional, Diff. Geom. Appl. 23 (2005), 114-127.
\item[] [14] K. Sekigawa, On some 4-dimensional compact Einstein almost Kähler manifolds, Math. Ann., 271 (1985), pp. 333-337.
\item[] [15] C. H. Taubes, More constraints on symplectic forms from Seiberg-Witten invariants, Math. Res. Lett., 2, 9-13 (1998).
\end{itemize}