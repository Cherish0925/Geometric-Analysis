---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Yamabe invariants and limits of self-dual hyperbolic monopole metrics]

Assume by contradiction that there is a sequence of unit-volume Yamabe minimizers in each conformal class $g_{Y, i}=v_{i}^{2} \tilde{g}_{i}$ with $R_{i} \rightarrow 0$ as $i \rightarrow \infty$, where $R_{i}$ is the (constant) scalar curvature of $g_{Y, i}$. The Yamabe equation is
$$-6 \Delta v_{i}+R\left(\tilde{g}_{i}\right) v_{i}=R_{i} v_{i}^{3} .$$
Multiply by $v_{i}$ and integrate to get
$$6 \int\left|\nabla v_{i}\right|^{2} d V_{\tilde{g}_{i}}+\int R\left(\tilde{g}_{i}\right) v_{i}^{2} d V_{\tilde{g}_{i}}=\int R_{i} v_{i}^{4} d V_{\tilde{g}_{i}}=R_{i} \operatorname{Vol}\left(g_{Y, i}\right)=R_{i} .$$
The right hand side limits to zero, therefore the left-hand side does also as $i \rightarrow \infty$. From (7.13), $R\left(\tilde{g}_{i}\right)$ is uniformly positive, so the $W^{1,2}$ norm of $v_{i}$ can be made arbitrarily small. Using the uniform Sobolev inequality and lower volume bound for $\tilde{g}_{i}$,
$$1=\operatorname{Vol}\left(g_{Y, i}\right)^{1 / 4}=\left\|v_{i}\right\|_{L^{4}} \leq C_{S}\left(\tilde{g}_{i}\right)\left(\left\|\nabla v_{i}\right\|_{L^{2}}+\left\|v_{i}\right\|_{L^{2}}\right) \leq C^{\prime}\left\|v_{i}\right\|_{W^{1,2}},$$
which is a contradiction for $i$ sufficiently large. \(\square\)
7.3. Convergence of constant scalar curvature metrics. We are now in a position to describe the possible limits of the Yamabe minimizers.

Theorem 7.5. Fix $n$, and let $\left(M, g_{i}\right)$ be an arbitrary sequence of $n$-pointed LeBrun metrics, with conformal compactifications $\left(\hat{M},\left[\hat{g}_{i}\right]\right)$. Assume that there exists a constant $\delta_{n}$ such that
$$0<\delta_{n} \leq Y\left(M,\left[g_{i}\right]\right) .$$

Let $g_{Y, i} \in\left[\hat{g}_{i}\right]$ be a sequence of unit volume Yamabe minimizers. Then there exists a subsequence $g_{Y, j},\{j\} \subset\{i\}$, which converges to either (1) a constant scalar curvature metric on a $k$-pointed LeBrun orbifold, $1 \leq k \leq n$, or (2) a single football metric, that is, $S^{4} / \mathbb{Z}_{m}$ with the round metric, for $2 \leq m \leq n$.

Proof. As in Theorem 7.1, we choose a compactification with fixed conformal factor $\tilde{g}_{i} \in\left[g_{i}\right]$, so that the sequence $\left(\hat{M}, \tilde{g}_{i}\right)$ will limit to a compactified LeBrun orbifold, with each bubble-tree consisting of a string of multi-Eguchi-Hanson orbifolds, and possibly other AF LeBrun orbifold metrics (in case some monopole points limit to the boundary of $\mathcal{H}^{3}$ ). Call this limit space $\left(M_{\infty}, g_{\infty}\right)$, and the finite singular set of convergence $S \subset M_{\infty}$. We write the sequence of unit volume Yamabe minimizers in each conformal class as $g_{Y, i}=v_{i}^{2} \tilde{g}_{i}$. Let $R_{i}$ denote the scalar curvature of $g_{Y, i}$. By passing to a subsequence, assume that $\lim _{i \rightarrow \infty} R_{i}=R_{\infty}$. From the assumption (7.17), $R_{\infty}>\delta>0$.

The assumption (7.17) implies that the Yamabe minimizers $g_{Y, i}$ satisfy a uniform Sobolev inequality of the following form [TV05b, Proposition 3.1]
$$\|f\|_{L^{4}} \leq C_{S}\|\nabla f\|_{L^{2}}+V o l^{-1 / 4}\|f\|_{L^{2}},$$
for any $f \in C^{0,1}(\hat{M})$. The $L^{2}$-norm of the curvature is uniformly bounded, as seen above in Section 6. We may therefore quote the compactness theorem of [TV05b, Theorem 1.1] to obtain a subsequence converging to a multi-fold limit. The Sobolev inequality (7.18) and $b_{1}(\hat{M})=0$ together imply that the limit must be an irreducible orbifold [TV05b, Proposition 7.2].

Let $C_{i}=\max _{M} u_{i}$. If $C_{i}$ remains bounded from above, then we argue as follows. On any compact subset $D \subset M_{\infty} \backslash S$, we have a Harnack inequality (since the conformal factors are bounded from above, and the sequence is smoothly converging away from the singular set). This implies that the conformal factors $u_{i}$ will either have a strictly positive limit on $M_{\infty}$ or will uniformly crash to zero on $M_{\infty}$. The latter case cannot happen since $\operatorname{Vol}\left(g_{Y, i}\right)=1$. Consequently, the limit must be a CSC (constant scalar curvature) metric conformal to $\left(M_{\infty}, g_{\infty}\right)$, and we are in Case (1).

So we next assume that $C_{i} \rightarrow \infty$ as $i \rightarrow \infty$. Let $x_{i}$ be points such that $u_{i}\left(x_{i}\right)=C_{i}$. We first assume that $x_{i} \rightarrow x \in M_{\infty} \backslash S$. Then the usual conformal dilation argument says that a bubble is forming on the smooth part [Sch91]. To summarize, this is by looking at the rescaled functions $\tilde{u}_{i}(y)=C_{i}^{-1} u_{i}\left(C_{i}^{-1} y\right)$. By elliptic theory, this sequence has a subseqence converging to a positive solution of $-6 \Delta u=R_{\infty} u^{3}$ on $\mathbb{R}^{4}$, satisfying $u(0)=1$. From our assumption on the Yamabe invariant, $R_{\infty}>\delta>0$. By Caffarelli-Gidas-Spruck [CGS89], the limit must be a standard bubble. This implies that the Yamabe invariant satisfies $Y\left(\left[g_{i}\right]\right) \gtrsim Y\left(S^{4}\right)$, for $i$ large, which contradicts Theorem 3.2 above. Therefore, we must have $x_{i} \rightarrow p \in S$ as $i \rightarrow \infty$. Let $\left(V_{1}, g_{1}\right)$ be the first bubble at $p$. Assume that, after the rescaling the sequence to limit to $\left(V_{1}, g_{1}\right)$ (pointed convergence based at $p$ ), $x_{i}$ limits to a finite point of $V_{1}$. The same conformal dilation argument shows that the rescaled conformal factor (with $g_{1}$ as background metric) must be bounded from above. Away from the singular points of convergence $p_{1, j^{\prime}}, j^{\prime}=1 \ldots k_{1}$, we again have a Harnack inequality. So the rescaled conformal
factor either (a) limits identically to zero away from the singlar points, or (b) has a finite positive limit everywhere. In Case (b), the limit of the original sequence must then be a CSC metric on the conformal compactification $\left(\hat{V}_{1}, \hat{g}_{1}\right)$, since this is the only possible irreducible orbifold limit. If $V_{1}$ is an Eguchi-Hanson orbifold, this cannot happen by Proposition 4.2. So the only possibility in Case (b) is that $\left(V_{1}, g_{1}\right)$ is an orbifold LeBrun AF metric, whose compactification is Case (1). Case (a) splits into two possibilities. Case (a1) is that $x_{i}$ will limit to $\infty$ in $\left(V_{1}, g_{1}\right)$. In this case, the only possible irreducible orbifold limit will be a metric on the compactification of the "neck" region. This follows since all ALE spaces in the bubble tree described in Theorem 7.1 have one end, the only possible neck regions are modeled on $\mathbb{R}^{4} / \mathbb{Z}_{m}$. The only CSC metric on the compactification of this is the $S^{4} / \mathbb{Z}_{m}$-football metric, by the Obata-Tashiro Theorem [Oba72, Tas65]. Therefore, Case (a1) is exactly Case (2). Case (a2) is that $x_{i}$ limits to one of the singular points of convergence of $V_{1}$ in this scaling. We then repeat the above argument around this singular point. In general, we repeat the entire argument at different scalings to see that the limit must be (i) a CSC metric on exactly one of the compactified orbifolds in the bubble-tree, or (ii) limit occurring on a neck region. For Case (i), the Gibbons-Hawing orbifolds do not admit CSC metrics by Proposition 4.2, so Case (i) is exactly Case (1). The argument above shows that Case (ii) is exactly Case (2).

Finally, in Case (1), the limit can never be a compactified 0-pointed LeBrun metric. This is conformal to $S^{4}$ with the round metric, and the only CSC metrics on $S^{4}$ are of constant curvature, so have maximal Yamabe invariant. This would contradict (1.1). This also proves $2 \leq m$ in Case (2). \(\square\)

We now return to the proofs of Theorems 1.2 and 1.5. The Yamabe invariant for $n=2,3$ is stricly positive by Proposition 6.1. For Theorem 1.2, as $d_{H}\left(p_{1}, p_{2}\right) \rightarrow \infty$, Theorem 7.5 says the only possible limit is the compactified 1-pointed LeBrun metric, since Case (2) obviously does not happen. This is conformal to the Fubini-Study metric, which is the unique CSC metric in its conformal class by Obata's Theorem [Oba72]. We note that the behavior of the Yamabe-minimizer on a connect sum is typically non-symmetric [Kob87, Joy03].

We next address the $K$-symmetric limit to $S^{4}$. The existence of $K$-symmetric minimizers follows from [Heb96]. Again, by [TV05b] we can find a subsequence converging to a multi-fold, but which now may have reducible points. But from the estimate on the $K$-Yamabe invariant in Theorem 5.4, as $d_{H}\left(p_{1}, p_{2}\right) \rightarrow \infty$, it is clear that the only possibility for a $K$-Yamabe minimizer is $S^{4}$ with the round metric. This follows because a reflection interchanging the two monopole point is clearly not an isometry of the two Yamabe minimizers, so these are not possible limits. From the arguments in the proof of Theorem 7.5, another possible limit is $\mathbb{C P}^{2} \vee \mathbb{C P}^{2}$, with the Fubini-Study metric scaled to have $V o l=1 / 2$ on each factor. But this cannot occur since the Yamabe invariant of this limit is $24 \pi>8 \pi \sqrt{6}=Y\left(S^{4}, g_{S}\right)$, and this would contradict Theorem 5.4. Similarly, the limit $\mathbb{C P}^{2} \vee S^{4}$ cannot happen either. Therefore, any sequence of Yamabe minimizers must concentrate entirely in the neck region. The only possible limit is then $S^{4}$ with the round metric, with Burns metrics bubbling off
at the 2 singular points of convergence. This follows since any reducible limit would be several $S^{4}$-s wedged together, which would have Yamabe invariant strictly larger than $8 \pi \sqrt{6}$.

Remark 7.6. As shown in [HV09], $G$ is generated by $K$ and an extra involution $\Lambda$ which is not a lift of a hyperbolic isometry, and is quite difficult to describe explicitly. It is likely that as $d\left(p_{1}, p_{2}\right) \rightarrow \infty$, the $G$-symmetric metric must also limit to $S^{4}$. But since the test metric in (5.12) is not invariant under $\Lambda$, we cannot say this for certain.

The fourth metric in Theorem 1.2 is obtained by adapting the CSC-gluing argument of Joyce to this problem [Joy03], see also [MPU95]. Very briefly, one chooses a conformal factor which is close to the Fubini-Study metric on neighborhoods of the monopole points, and is close to a Schwarzschild neck region in between; this will be the approximate CSC-metric. One then uses the implicit function theorem, together with the crucial fact that the Fubini-Study metric is CSC-nondegenerate. This adaptation is straightforward, but since the argument is quite lengthy, we omit the details due to space considerations.

As $d_{H}\left(p_{1}, p_{2}\right) \rightarrow 0$, Case (1) in Theorem 7.5 could only be a compactified LeBrun metric with a single point of multiplicity 2. This is conformal (minus the orbifold point) to the Eguchi-Hanson metric, which does not admit any CSC metric by Theorem 1.3, so this case cannot happen. Consequently, the only possibility for the limit is the $S^{4} / \mathbb{Z}_{2}$-football with the round metric (since the limit of Yamabe minimizers must be irreducible). Similarly, Theorem 1.3 implies that as $d_{H}\left(p_{1}, p_{2}\right) \rightarrow 0$, the only possible $K$-symmetric limit is the $S^{4} / \mathbb{Z}_{2}$-football with the round metric. To see this, again the only concentration can occur in the neck region, which is $\mathbb{R}^{4} / \mathbb{Z}_{2}$. The limit no longer has to be irreducible. But the lowest energy reducible limit would be the wedge of two $S^{4} / \mathbb{Z}_{2}$-footballs, whose Yamabe energy is $8 \pi \sqrt{6}$. However, since in this case the points are not limiting to the boundary of $\mathcal{H}^{3}$, Theorem 5.4 shows that the Yamabe energy must be strictly less than $8 \pi \sqrt{6}$, so this cannot happen, and therefore the limit must be the irreducible $S^{4} / \mathbb{Z}_{2}$-football.

For the first case in Theorem 1.5, as $p_{3} \rightarrow p_{2}$, the only possible limits from Theorem 7.5 are Case (1): a compactified LeBrun metric with a single monopole point, and another multiplicity 2 point, or Case (2): a $S^{4} / \mathbb{Z}_{2}$-football with the round metric. However, under the assumptions of Theorem 1.5, (4.11) says the Yamabe invariant is strictly less than that of the $S^{4} / \mathbb{Z}_{2}$-football, so the limit must be Case (1).

Finally, for the last case in Theorem 1.5, as $p_{3} \rightarrow \partial \mathcal{H}^{3}$, the Yamabe invariant is strictly less than that of $g_{F S}$ by Theorem 3.2. Thus the only possible limit is Case (1), a 2-pointed LeBrun compactified metric.

\section*{8. Questions}

We conclude with a list of questions.
\begin{itemize}
\item[-] What is the optimal lower bound for the Yamabe invariant in (1.2) for $n \geq 2$ ? We conjecture that $\delta_{n}=Y\left(S^{4} / \mathbb{Z}_{n},\left[g_{S}\right]\right)$; this is true for $n=2$, as seen above in Theorem 1.2. Furthermore, the assumption that the points are contained
\end{itemize}
\begin{itemize}
\item[] in a compact set $\mathcal{K} \subset \mathcal{H}^{3}$ should not be necessary. Removing this assumption would imply that the moduli space of Yamabe minimizing LeBrun metrics has a nice compactification for any $n$. As seen above, this is true for $n=2,3$.
\item[-] Does the compactified LeBrun metric on $\mathcal{O}(-n)$ admit a CSC metric for $n \geq 3$ ? The answer is no for $n=2$ since this is the compactified Eguchi-Hanson metric, which was ruled out by Theorem 1.3. For $n \geq 3$, Theorem 1.4 rules out any symmetric solution, but is there a non-symmetric solution? Furthermore, as shown in Theorem 7.1, if all monopole points approach a single point at a uniform rate, the bubble-tree structure is a compactified Le-Brun negative-mass metric on $\mathcal{O}(-n)$, with a Gibbons-Hawking multi-Eguchi-Hanson bubbling off. From the arguments in Section 7, the limit of the Yamabe minimizers could limit to either a CSC metric on compactified $\mathcal{O}(-n)$, or to the $S^{4} / \mathbb{Z}_{n}$-football (since the compactified GH metric does not admit a CSC metric by Theorem 1.3). Which one actually happens for $n \geq 3$ ?
\item[-] Except for the case of a single monopole point with multiplicity $n$, does a $\left[\hat{g}_{L B}\right]$ orbifold conformal class always admit a CSC metric?
\item[-] In Theorem 1.2, for $n=2$ we determined the limiting behavior of the $K$ -Yamabe minimizers as $d\left(p_{1}, p_{2}\right) \rightarrow \infty$ (the limit is $S^{4}$ ). Recall that $K$ is an index 2 subgroup of full conformal group $G$. What is the limit of the $G$-Yamabe minimizers?
\item[-] Are CSC metrics on compactified LeBrun metrics CSC nondegenerate? If so, then it would then be possible to apply the Joyce gluing technique to obtain more non-Yamabe-minimizing examples.
\item[-] LeBrun metrics with torus action are a special case of Joyce metrics Joy95. These depend on a choice of points on the boundary of hyperbolic 2-space. What happens as these metrics degenerate?
\end{itemize}

\section*{References}
\begin{itemize}
\item[] [AB03] K. Akutagawa and B. Botvinnik, Yamabe metrics on cylindrical manifolds, Geom. Funct. Anal. 13 (2003), no. 2, 259-333.
\item[] [AB04] Kazuo Akutagawa and Boris Botvinnik, The Yamabe invariants of orbifolds and cylindrical manifolds, and $L^{2}$-harmonic spinors, J. Reine Angew. Math. 574 (2004), 121-146.
\item[] [AKL89] Michael T. Anderson, Peter B. Kronheimer, and Claude LeBrun, Complete Ricci-flat Kähler manifolds of infinite topological type, Comm. Math. Phys. 125 (1989), no. 4, 637-642.
\item[] [Aku94] Kazuo Akutagawa, Yamabe metrics of positive scalar curvature and conformally flat manifolds, Differential Geom. Appl. 4 (1994), no. 3, 239-258.
\item[] [Aku96] \_\_\_\_, Convergence for Yamabe metrics of positive scalar curvature with integral bounds on curvature, Pacific J. Math. 175 (1996), no. 2, 307-335.
\item[] [And89] Michael T. Anderson, Ricci curvature bounds and Einstein metrics on compact manifolds, J. Amer. Math. Soc. 2 (1989), no. 3, 455-490.
\end{itemize}
[And05] \_\_\_\_, Orbifold compactness for spaces of Riemannian metrics and applications, Math. Ann. 331 (2005), no. 4, 739-778.
[Aub82] Thierry Aubin, Nonlinear analysis on manifolds. Monge-Ampère equations, Springer-Verlag, New York, 1982.
[Ban90] Shigetoshi Bando, Bubbling out of Einstein manifolds, Tohoku Math. J. (2) 42 (1990), no. 2, 205-216.
[Bar86] Robert Bartnik, The mass of an asymptotically flat manifold, Comm. Pure Appl. Math. 39 (1986), no. 5, 661-693.
[CGS89] Luis A. Caffarelli, Basilis Gidas, and Joel Spruck, Asymptotic symmetry and local behavior of semilinear elliptic equations with critical Sobolev growth, Comm. Pure Appl. Math. 42 (1989), no. 3, 271-297.
[CGY02] Sun-Yung A. Chang, Matthew J. Gursky, and Paul C. Yang, An equation of Monge-Ampère type in conformal geometry, and four-manifolds of positive Ricci curvature, Ann. of Math. (2) 155 (2002), no. 3, 709-787.
[CLW08] Xiuxiong Chen, Claude Lebrun, and Brian Weber, On conformally Kähler, Einstein manifolds, J. Amer. Math. Soc. 21 (2008), no. 4, 1137-1168.
[CQY07] Sun-Yung A. Chang, Jie Qing, and Paul Yang, On a conformal gap and finiteness theorem for a class of four-manifolds, Geom. Funct. Anal. 17 (2007), no. 2, 404-434.
[CW07] Xiuxiong Chen and Brian Weber, Moduli spaces of critical riemannian metrics with $L^{n / 2}$ norm curvature bounds, arXiv.org:0705.4440, 2007.
[DF89] S. Donaldson and R. Friedman, Connected sums of self-dual manifolds and deformations of singular spaces, Nonlinearity 2 (1989), no. 2, 197-239.
[Flo91] Andreas Floer, Self-dual conformal structures on $l \mathrm{CP}^{2}$, J. Differential Geom. 33 (1991), no. 2, 551-573.
[GH78] G. W. Gibbons and S. W. Hawking, Gravitational multi-instantons, Physics Letters B 78 (1978), no. 4, 430-432.
[GV03] Matthew J. Gursky and Jeff A. Viaclovsky, A fully nonlinear equation on four-manifolds with positive scalar curvature, J. Differential Geom. 63 (2003), no. 1, 131-154.
[Heb96] Emmanuel Hebey, From the Yamabe problem to the equivariant Yamabe problem, Actes de la Table Ronde de Géométrie Différentielle (Luminy, 1992), Sémin. Congr., vol. 1, Soc. Math. France, Paris, 1996, Joint work with M. Vaugon, pp. 377-402.
[Hit79] N. J. Hitchin, Polygons and gravitons, Math. Proc. Cambridge Philos. Soc. 85 (1979), no. 3, 465-476.
[Hit97] \_\_\_\_, Einstein metrics and the eta-invariant, Boll. Un. Mat. Ital. B (7) 11 (1997), no. 2, suppl., 95-105.
[Hon10] Nobuhiro Honda, Degenerations of LeBrun twistor spaces, arXiv.org:1001.3461, 2010.
[HV09] Nobuhiro Honda and Jeff Viaclovsky, Conformal symmetries of self-dual hyperbolic monopole metrics, arXiv.org:0902.2019, 2009.
[Joy95] Dominic D. Joyce, Explicit construction of self-dual 4-manifolds, Duke Math. J. 77 (1995), no. 3, 519-552.
[Joy03] Dominic Joyce, Constant scalar curvature metrics on connected sums, Int. J. Math. Math. Sci. (2003), no. 7, 405-450.
[Kob87] Osamu Kobayashi, Scalar curvature of a metric with unit volume, Math. Ann. 279 (1987), no. 2, 253-265.
[Kro89] P. B. Kronheimer, The construction of ALE spaces as hyper-Kähler quotients, J. Differential Geom. 29 (1989), no. 3, 665-683.
[LeB88] Claude LeBrun, Counter-examples to the generalized positive action conjecture, Comm. Math. Phys. 118 (1988), no. 4, 591-596.
[LeB91] \_\_\_\_, Explicit self-dual metrics on $\mathbf{C P}_{2} \# \cdots \# \mathbf{C P}_{2}$, J. Differential Geom. 34 (1991), no. 1, 223-253.
\begin{itemize}
\item[] [LNN97] Claude LeBrun, Shin Nayatani, and Takashi Nitta, Self-dual manifolds with positive Ricci curvature, Math. Z. 224 (1997), no. 1, 49-63.
\item[] [LP87] John M. Lee and Thomas H. Parker, The Yamabe problem, Bull. Amer. Math. Soc. (N.S.) 17 (1987), no. 1, 37-91.
\item[] [MPU95] Rafe Mazzeo, Daniel Pollack, and Karen Uhlenbeck, Connected sum constructions for constant scalar curvature metrics, Topol. Methods Nonlinear Anal. 6 (1995), no. 2, 207-233.
\item[] [Nak90] Hiraku Nakajima, Self-duality of ALE Ricci-flat 4-manifolds and positive mass theorem, Recent topics in differential and analytic geometry, Academic Press, Boston, MA, 1990, pp. 385-396.
\item[] [Nak94] \_\_\_\_, A convergence theorem for Einstein metrics and the ALE spaces, Selected papers on number theory, algebraic geometry, and differential geometry, Amer. Math. Soc. Transl. Ser. 2, vol. 160, Amer. Math. Soc., Providence, RI, 1994, pp. 79-94.
\item[] [Oba72] Morio Obata, The conjectures on conformal transformations of Riemannian manifolds, J. Differential Geometry 6 (1971/72), 247-258.
\item[] [Po86] Y. Sun Poon, Compact self-dual manifolds with positive scalar curvature, J. Differential Geom. 24 (1986), no. 1, 97-132.
\item[] [Rat06] John G. Ratcliffe, Foundations of hyperbolic manifolds, second ed., Graduate Texts in Mathematics, vol. 149, Springer, New York, 2006.
\item[] [Sch84] Richard Schoen, Conformal deformation of a Riemannian metric to constant scalar curvature, J. Differential Geom. 20 (1984), no. 2, 479-495.
\item[] [Sch91] Richard M. Schoen, On the number of constant scalar curvature metrics in a conformal class, Differential geometry, Longman Sci. Tech., Harlow, 1991, pp. 311-320.
\item[] [Tas65] Yoshihiro Tashiro, Complete Riemannian manifolds and some vector fields, Trans. Amer. Math. Soc. 117 (1965), 251-275.
\item[] [Tia90] G. Tian, On Calabi's conjecture for complex surfaces with positive first Chern class, Invent. Math. 101 (1990), no. 1, 101-172.
\item[] [TV05a] Gang Tian and Jeff Viaclovsky, Bach-flat asymptotically locally Euclidean metrics, Invent. Math. 160 (2005), no. 2, 357-415.
\item[] [TV05b] \_\_\_\_, Moduli spaces of critical Riemannian metrics in dimension four, Adv. Math. 196 (2005), no. 2, 346-372.
\item[] [TV08] \_\_\_\_, Volume growth, curvature decay, and critical metrics, Comment. Math. Helv. 83 (2008), no. 4, 889-911.
\end{itemize}

Department of Mathematics, University of Wisconsin, Madison, WI, 53706
E-mail address: jeffv@math.wisc.edu