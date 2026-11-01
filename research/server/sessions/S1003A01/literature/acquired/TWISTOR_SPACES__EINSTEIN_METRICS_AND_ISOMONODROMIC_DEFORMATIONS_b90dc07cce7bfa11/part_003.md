---
retention_scope: session
part: 3
total_parts: 3
---

[Part 3/3 of: TWISTOR SPACES, EINSTEIN METRICS AND ISOMONODROMIC DEFORMATIONS]

**Remark.** The metrics which appear in two places in the list are those which have two different $SU(2)$ actions, or equivalently which have an isometry group which is a compact Lie group of rank 2. Only $SO(4), SO(5)$ and $SU(3)$ can act on a 4-manifold and these give the standard metrics on $S^4$ and $CP^2$. For the solution of Painlevé VI which gives rise to these, see [19].

A more useful classification is to consider the global condition of completeness. In this case we obtain the following list.

**Theorem 13.** Let $M$ be a complete $SU(2)$-invariant anti-self-dual Einstein metric with 3-dimensional generic orbits.

1. If $R > 0$, then $M$ is isometric to:
   (a) the constant curvature metric on $S^4$,

---

(b) the Fubini-Study metric on CP².

2. If R = 0, then M is isometric to:
(a) the flat metric on R⁴,
(b) the Taub-NUT metric on R⁴,
(c) the Eguchi-Hanson metric on the cotangent bundle of S²,
(d) the L² metric on the moduli space of two SU(2)-monopoles on R³.

3. If R < 0, then M is isometric to:
(a) the metric of constant negative curvature on the unit ball in R⁴,
(b) the Pedersen metric on the unit ball,
(c) one of the metrics of Theorem 7 on the unit ball,
(d) the Pedersen/LeBrun metric on a line bundle of degree -n over S²,
(e) the Bergmann metric on the unit ball,
(f) one of the metrics of Theorem 9 on the unit ball.

Proof. For the purposes of the proof, we shall distinguish the three types of solutions as follows:

• Type I: ∧³α ≡ 0.
• Type II: ∧³α ≠ 0 and vanishes with multiplicity 2.
• Type III: ∧³α ≠ 0 and vanishes nondegenerately.

(1) First consider the case R > 0. It is a well-known consequence of Myers' theorem that a complete Einstein manifold with positive scalar curvature is compact. We can then use Theorem (13.30) of [8] to deduce that M is isometric to CP² or S⁴, without using directly the symmetry assumption.

(2) Next consider the case R = 0, and metrics of Type I. Here Theorem 2 tells us that the metric is either conformally flat, Eguchi-Hanson or Belinskii-Gibbons-Pope. The latter is well-known to be incomplete, and the Eguchi-Hanson metric is complete. A conformally flat Einstein metric with zero scalar curvature is flat, and so M is covered by R⁴. Since SU(2) is simply connected, its action on M lifts to R⁴, where it has a unique fixed point, the origin. But SU(2) must commute with the covering transformations, which therefore have a fixed point which is a contradiction unless M = R⁴.

Now consider Type II metrics. Here the non-flat ones are given, up to a scalar multiple, by taking $V = 1 + m/r$. When $m > 0$, this gives the Taub-NUT metric (see e.g.[8]) which is complete, and when $m < 0$ a metric which is incomplete at $r = -m$.

The metrics of Type III, and their completeness properties, are discussed in [4], in fact in the same context as the Taub-NUT metric. The only complete one is the 2-monopole hyperkähler metric.

(3) Now consider the case $R < 0$. Beginning with Type I, the only possibility is a conformally flat metric and hence a manifold of constant negative curvature. Again, since the $SU(2)$ action on $H^4$ has a unique fixed point, $M$ must be isometric to $H^4$.

As for the metrics of Type II, there are two cases in Theorem 11, involving trigonometric or hyperbolic functions. Since we require negative scalar curvature, the formula for $R$ shows that we can take $c = 1, \epsilon = 1$ in the trigonometric case and $c = 1, \epsilon = -1$ in the hyperbolic case. In diagonal form the metrics (from [29]) can be written as

$$g = \frac{1}{(\cos \rho - m \sin \rho)^2} \left[ (1 + m \cot \rho) \left(d\rho^2 + 4 \sin^2 \rho \left(\sigma_1^2 + \sigma_2^2\right)\right) + \frac{4m^2}{(1 + m \cot \rho)} \sigma_3^2 \right],$$

or

$$g = \frac{1}{(-\cosh \rho + m \sinh \rho)^2} \left[ (-1 + m \coth \rho) \left(d\rho^2 + 4 \sinh^2 \rho \left(\sigma_1^2 + \sigma_2^2\right)\right) + \frac{4m^2}{(-1 + m \coth \rho)} \sigma_3^2 \right].$$

In both cases, near $\rho = 0$, the metric is given by

$$g = 4m \left(d\left(\rho^{1/2}\right)^2 + \left(\rho^{1/2}\right)^2 \left(\sigma_1^2 + \sigma_2^2 + \sigma_3^2\right)\right) + \ldots,$$

which clearly extends to the puncture $\rho = 0$, as remarked in [29].

In the first case, the conformal structure is regular, but the metric blows up at $\rho = \rho_0$, where $\cot \rho_0 = m$ and this induces the conformal structure

$$\sigma_1^2 + \sigma_2^2 + \frac{m^2}{1+m^2} \sigma_3^2$$

on the sphere. If $m > 0$, the metric is regular for $0 < \rho < \rho_0$, and this is Pedersen's metric (also found analytically in [14]) on the ball, inducing a conformal structure $\sigma_1^2 + \sigma_2^2 + \lambda \sigma_3^2$ on the boundary when $\lambda < 1$. For $\rho > \rho_0$, the metric becomes singular and incomplete at $\rho = \rho_1$ where cot $\rho = -1/m$, and for $\rho > \rho_1$ it changes signature. If $m < 0$, the behaviour is similar, replacing $\rho$ by $\pi - \rho$.

In the second, hyperbolic, case when $m > 1$ the metric is singular at $\rho = \rho_0$, where coth $\rho_0 = m$ and this induces the conformal structure

$$\sigma_1^2 + \sigma_2^2 + \frac{m^2}{m^2-1} \sigma_3^2$$

on the sphere. Since coth $\rho > 1 > 1/m$, in this case the conformal structure is regular for all $\rho$. For $\rho < \rho_0$ this is the Pedersen metric on the ball inducing the conformal structure $\sigma_1^2 + \sigma_2^2 + \lambda \sigma_3^2$ on the boundary for $\lambda > 1$. We need to estimate the metric as $\rho \to \infty$. This is easily seen to be

$$g = \frac{4}{(m-1)} \left(e^{-2\rho} d\rho^2 + \frac{4m^2}{(m-1)^2} e^{-2\rho} \sigma_3^2 + \sigma_1^2 + \sigma_2^2\right),$$

which is incomplete, and in fact has a conical singularity around a 2-sphere, for setting $r = e^{-\rho}$, the metric is a multiple of

$$dr^2 + \left(\frac{2m}{m-1}\right)^2 r^2 \sigma_3^2 + \sigma_1^2 + \sigma_2^2.$$

It can be extended to a metric on a smooth manifold, the complex line bundle of degree $n$ over $S^2$ if $m$ satisfies $m = n/(n-2)$. In this case, the conformal structure was found by LeBrun in [23] in the context of scalar-flat Kähler metrics (see also [30]), but it is a continuation of Pedersen's metric. The result is a complete Einstein metric with conformal infinity the Lens space $S^3/Z_n$. If $\rho < 0$, the metric is negative definite.

When $m = 1$ the metric is defined for all $\rho > 0$ and is the Bergmann metric (see [29]). If $m < 1$, the conformal factor is still non-vanishing, but the conformal structure is singular where coth $\rho = 1/m$. Since the coefficients of both $\sigma_1^2$ and $\sigma_2^2$ vanish, the metric does not extend to any 2-dimensional orbit.

Finally consider the generic case Type III, which relies on the solution (68) to the Painlevé equation. From Proposition 8, we saw that the two types of poles of $y(x)$, with positive or negative residues, give rise respectively to punctures or boundaries of Einstein metrics. When the conformal structure becomes singular as in Proposition 10, with $\Omega_2^2 \rightarrow 0$, the conformal factor (65) approaches

$$\frac{\Omega_2(x_0 - 4(1-x_0)\Omega_1^2)}{2\Omega_1\Omega_3(1-x_0)^2}.$$

Here we have used $\Omega_1^2 - \Omega_2^2 - \Omega_3^2 = -1/4$, which also shows that all three do not vanish simultaneously. Since, as in Proposition 10, $\Omega_2^2$ vanishes to higher order than either $\Omega_1^2$ or $\Omega_3^2$, the conformal factor tends to zero, and we do not obtain a complete metric at such a singularity.

Thus a complete Einstein metric must be defined on intervals in which the conformal structure is nonsingular, and whose end-points are either $1, \infty$ or poles of $y(x)$.

There are four possible domains of definition:

1. a finite interval $(x_0, x_1)$,
2. an interval $(1, x_1)$,
3. an interval $(x_1, \infty)$,
4. the whole interval $(1, \infty)$, where $x_0, x_1$ are poles of $y(x)$, and there are no poles in the interval. We begin with the case $k_3 \neq 0$, assuming as usual $k_3 > 0$ and $0 \leq k_1 < 2$. Suppose first that $k_1 \neq 0, 1$.

From Theorem 7, $y(x)$ has poles at the points $x(i k_3 / (k_1 + 2n - 2)) = x_n$ and as $n \rightarrow \infty$, $x_n \rightarrow \infty$, which means that any interval of the form (3) or (4) contains poles and so cannot define a complete metric.

For a finite interval, Proposition 13 describes the situation. On the interval $(\bar{x}_n, x_{n+1})$ we have a complete metric already. If such a metric existed on $(x_n, \bar{x}_n)$, the conformal structure would be an analytic continuation and we could produce an anti-self-dual conformal structure on a manifold homeomorphic to $S^4$. As argued in Theorem 8, this must be conformally flat, which is a contradiction.

Thus the metrics of Theorem 7 are the only complete ones occurring on a finite interval.

It remains to consider case (2), and for that we must estimate $y(x)$ as $x \rightarrow 1$, or equivalently $\sigma \rightarrow \infty$. In this limit, it is convenient to normalize the choice of $k_3, k_1$ by taking $0 < k_1 < 1$ and not fixing the sign of $k_3$. Since $y(x)$ depends only on the monodromy, this has no effect on the estimates.

---

Using the expansion

$$\vartheta_1(\nu) = \sum_{n=0}^{\infty} (-1)^n 2q^{(n+1/2)} \sin(2n + 1)\pi\nu$$

with $\nu = i(k_1\sigma - k_3)/2$ we obtain an expansion in increasing powers of $e^{-\sigma}$

$$\frac{\vartheta'_1}{\vartheta_1}(\nu) = i\pi \left(-1 - 2e^{2\pi i\nu} + 2e^{-2\pi\sigma-2\pi i\nu} + \dots\right),$$

and differentiating this to obtain expressions for $\wp(\omega)$ and $\wp'(\omega)$ we find

$$y(x) = 1 + \frac{k_1 e^{\pi k_3}(x - 1)^{k_1}}{2^{4k_1-2}(k_1 - 1)} + \dots,$$

By this expansion for $y(x)$ near $x = 1$, the Einstein metric from (64) and (65) is of the form

$$g = s^{k_1-2} ds^2 + \frac{4s_1^k}{(k_1 - 1)^2}\sigma_2^2 + c(\sigma_1^2 + \sigma_3^2) + \dots,$$

where $x = 1 + s$ and $c$ is a constant. Putting $t = s^{k_1/2}$ the metric can be seen to have a conical singularity of angle $\pi k_1/(1-k_1)$ around an $RP^2$ orbit (cf [19]) or twice the angle around an $S^2$ orbit on a double covering. If the angle is $2\pi n$ for an integer $n$, then the metric is well defined on a quotient by a right action of $Z_n$. But this requires the coefficients of $\sigma_1^2$ and $\sigma_3^2$ to be equal, which leads to the case of metrics of Type II. If the angle is $2\pi/n$, then the metric is defined on an $n$-fold covering branched over the orbit, but for topological reasons the generic orbit of $SU(2)$ is then $S^3/G$ where $G$ is the quaternion group, or a double covering.

Returning to the normalization with $k_3 > 0$, Proposition 13 shows that the first pole $x = x_0$ of $y(x)$ has positive residue if $0 < k_1 < 1$ and negative residue if $1 < k_1 < 2$. In the first case, $y(x) \rightarrow -\infty$ as $x \rightarrow x_0-$, so that $x_0$ is a puncture. But a smooth metric requires the orbit of $SU(2)$ to be a 3-sphere, and not a quotient as above. In the second case, $y(x) \rightarrow +\infty$ as $x \rightarrow x_0-$. But from (86), $y(x)$ approaches 1 from below as $x \rightarrow 1+$, thus the graph of $y(x)$ must meet the line $y = x$ with positive derivative, which gives a singular conformal structure from Proposition 10.

Hence the generic case $k_1 \neq 0, 1$, $k_3 > 0$ produces only the complete metrics of Theorem 7.

Consider next the special case $k_1 = 0$, where we can now take $k_3 > 0$. The arguments above hold except for the expansion as $x \rightarrow 1$. Here, $\nu$ is independent of $\sigma$ and as $\sigma \rightarrow \infty$, we use the expansion

$$\frac{1}{4\pi} \frac{\vartheta'_1(\nu)}{\vartheta_1(\nu)} = \frac{1}{4} \cot \pi\nu + q^2 \sin 2\pi\nu \ldots,$$

which yields the following behaviour for $y(x)$ near $x = 1$:

$$y(x) = 1 + \frac{1}{2}(x - 1) + \frac{\sinh^2(\pi k_3/2)}{2}(x - 1)^2 + \ldots.$$

Since $y(x)$ has derivative $1/2$ at $x = 1$, if $y \rightarrow +\infty$ as $x \rightarrow x_1-$, the graph must meet the line $y = x$ at some point $x_0$ with $y(x) - x$ having positive derivative, giving a singular conformal structure from Proposition 10. On the other hand if $y \rightarrow -\infty$, then $x_1$ is the point $\sigma = k_3/2$ and as $\sigma \rightarrow k_3/2+$, the expansion (83) shows that $\vartheta'_1/i\vartheta_1$ is large and negative. But from (88) it is positive as $\sigma \rightarrow \infty$, so again $y(x)$ must have a pole in the interval.

Now consider the other special case $k_1 = 1$ and $k_3 > 0$. Again the arguments above deal with the case of an interval $(x_0,x_1)$. Let $(1,x_1)$ be an interval on which a metric is defined and complete. Then $x_1$ must be the first pole of $y(x)$. From Proposition 13, $x_1 = x(ik_3)$. But then Theorem 9 describes a complete metric.

Finally consider the case $k_3 = 0$. We can now choose $0 \leq k_1 \leq 1$, and in fact since the monodromy is non-abelian, $k_1 \neq 0, 1$. In this case $\omega = k_1\omega_3$ and is never a period, so there are no punctures. The other pole of $y(x)$, for a boundary, occurs when

$$\frac{\vartheta'_1}{\vartheta_1}(k_1\tau/2,\tau) + ik_1\pi = 0.$$

Differentiating the identity

$$\vartheta_1(\nu/\tau,-1/\tau) = \frac{\sqrt{\tau}}{i\sqrt{i}} e^{\pi i\nu^2/\tau}\vartheta_1(\nu,\tau)$$ is equivalent to

$$\vartheta'_1(k_1/2, -1/\tau) = 0,$$

but the expansion (83) shows that this never occurs if $k_1 < 1$, thus $y(x)$ is regular on the whole interval $(1, \infty)$. As $x \rightarrow 1$, the asymptotic form (87) still holds, with $k_3 = 0$. The arguments advanced there hold too and imply that $k_1 = 2/3$ or $1/2$. In this case, with $k_3 = 0$, the monodromy is then from Theorem 5 finite, in fact the binary dihedral groups of the symmetries of a triangle or square. As discussed in ([19]), these cases are analytic continuations of the standard metrics on $S^4$ and $CP^2$, and the Einstein metrics of negative scalar curvature in these families are the hyperbolic metric and Bergmann metric, dealt with elsewhere and not, in fact, admitting an $SU(2)$ action of Type III.

Since all cases of Type and monodromy have now been considered, the classification follows.

## References

[1] V.I. Arnold, Mathematical methods of classical mechanics, Springer, New York, 1978
[2] A. Ashtekar, T. Jacobson & L. Smolin, A new characterization of half-flat solutions to Einstein's equations, Comm. Math. Phys. 115 (1988) 631-648.
[3] M.F. Atiyah, Magnetic monopoles in hyperbolic space, Proc. of Bombay Colloquium 1984 on Vector Bundles on Algebraic Varieties, Oxford University Press, 1987, 1-34.
[4] M.F. Atiyah & N.J. Hitchin, The Geometry and Dynamics of Magnetic Monopoles, Princeton University Press, Princeton, 1988.
[5] ___, Low energy scattering of non abelian monopoles, Phys. Lett. 107A (1985) 21-25.
[6] M.F. Atiyah, N.J. Hitchin & I.M. Singer, Self-duality in four-dimensional Riemannian geometry, Proc. Roy. Soc. London, A362 (1978) 425-61.
[7] V.A. Belinskii, G.W. Gibbons, C.N. Pope & D.N. Page, Asymptotically Euclidean Bianchi IX metrics in quantum gravity, Phys. Lett. 76B (1978) 433-435.
[8] A.L. Besse, Einstein manifolds, Springer, Berlin, 1987.

---

[9] C.P. Boyer, A note on hyperHermitian four-manifolds, Proc. Amer. Math. Soc. 102 (1988) 157-164.

[10] E. Calabi, Métriques kähleriennes et fibrés holomorphes, Ann. Sci. Écol. Norm. Sup. 12 (1979) 269-294.

[11] A.S. Dancer, Scalar-flat Kähler metrics with SU(2) symmetry, DAMTP Cambridge preprint, 1993.

[12] T. Eguchi & A.J.Hanson, Asymptotically flat self-dual solutions to Euclidean gravity, Phys. Lett. 237 (1978) 249-251.

[13] G.W. Gibbons & S.W. Hawking, Gravitational multi-instantons, Phys. Lett. 78B (1978) 430-432.

[14] G.W. Gibbons & C.N. Pope, CP² as a gravitational instanton, Comm. Math. Phys. 61 (1978) 239-248.

[15] C.R. Graham & J.M. Lee, Einstein metrics with prescribed conformal infinity on the ball, Adv. Math. 87 (1991) 186-225.

[16] G.-H. Halphen, Sur un système d'équations différentielles, C.R. Acad. Sci. Paris 92 (1881) 1101-1103.

[17] N.J. Hitchin, Monopoles and geodesics, Comm. Math. Phys. 83 (1982) 579-602.

[18] ___, Complex manifolds and Einstein’s equations, Twistor Geometry and Nonlinear Systems. Proc., Primorsko, Bulgaria 1980, (eds. H. D. Doebner & T. D. Palev), Lecture Notes in Math. Vol. 970, Springer, Berlin, 1982, 79-99.

[19] ___, A new family of Einstein metrics, Proc. Conference in Honour of E. Calabi, Pisa, 1993, Cambridge Univ. Press, to appear.

[20] M. Jimbo & T. Miwa, Monodromy preserving deformation of linear ordinary differential equations with rational coefficients II, Physica 2D (1981) 407-448.

[21] P.B. Kronheimer, Instantons and the geometry of the nilpotent variety, J. Differential Geometry 32 (1990) 473-490.

[22] C. LeBrun, H-space with a cosmological constant, Proc. Roy. Soc. London, A380 (1982) 171-185.

[23] ___, Counterexamples to the generalized positive action conjecture, Comm. Math. Phys. 118 (1988) 591-596.

---

[24] ___, Explicit self-dual metrics on CP₂#...#CP₂, J. Differential Geometry 34 (1991) 223-253.

[25] ___, On complete quaternionic-Kähler manifolds, Duke Math. J. 63 (1991) 723-743.

[26] B. Malgrange, Sur les deformations isomonodromiques I. Singularités régulières, Mathématique et Physique, Sém. École Norm. Sup., 1979-1982, Progr. Math. Birkhäuser, Boston 37 (1983) 401-426.

[27] L.J. Mason & N.M.J. Woodhouse, Self-duality and the Painlevé transcendents, Nonlinearity 6 (1993) 569-581.

[28] R. Maszczyk, L.J. Mason & N.M.J. Woodhouse, Self-dual Bianchi metrics and the Painlevé transcendents, Classical Quantum Gravity 11 (1994) 65-71.

[29] H. Pedersen, Einstein metrics, spinning top motions and monopoles, Math. Ann. 274 (1986) 35-59.

[30] H. Pedersen & Y.S. Poon, Kähler surfaces with zero scalar curvature, Classical Quantum Gravity 7 (1990) 1707-1719.

[31] M. Pontecorvo, On twistor spaces of anti-self-dual Hermitian surfaces, Trans. Amer. Math. Soc. 331 (1992) 653-661.

[32] S. Salamon, Riemannian geometry and holonomy groups, Pitman Research Notes in Math. 201, Longman, Harlow, 1989.

[33] J. Tannery & J. Molk, Fonctions elliptiques, Gauthier Villars, Paris, 1893.

[34] K.P. Tod, Self-dual Einstein metrics from the Painlevé VI equation, Phys. Lett. A 190 (1994) 221-224.

[35] R.S. Ward, Self-dual spacetimes with a cosmological constant, Comm. Math. Phys. 78 (1980) 1-17.