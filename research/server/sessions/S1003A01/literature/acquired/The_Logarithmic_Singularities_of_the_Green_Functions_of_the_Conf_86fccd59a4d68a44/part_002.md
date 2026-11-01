---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: The Logarithmic Singularities of the Green Functions of the Conformal Powers of the Laplacian]

Step 7. Let $I_{g}(x)=\operatorname{Contr}_{g}\left(\nabla^{k_{1}} R \otimes \cdots \otimes \nabla^{k_{l}} R\right)$ be a Weyl Riemannian invariant of weight $w<n$. Then the following are equivalent:
\begin{itemize}
\item[(i)] $\tilde{I}_{g}(x)$ at $x=0$ for all metrics of signature $(n, 0)$ on $\mathbb{R}^{n}$.
\item[(ii)] $I_{g}(x)=0$ at $x=0$ for all metrics of signature $(n, 0)$ on $\mathbb{R}^{n}$ such that $\operatorname{Ric}(g)=\mathrm{O}\left(|x|^{n-2}\right)$ near $x=0$.
\item[(iii)] $I_{g}(x)=0$ at $x=0$ for all metrics of signature ( $n+1,1$ ) on $\mathbb{R}^{n+2}$ such that $\operatorname{Ric}(g)=$ $\mathrm{O}\left(|x|^{n-2}\right)$ near $x=0$.
\end{itemize}

The implication (i) ⇒ (ii) is an immediate consequence of Step 5. The implication (iii) ⇒ (i) follows from the construction of the conformal invariant $\tilde{I}_{g}(x)$, since the ambient metric is of the form given in (iii) if we use the variable $r=\sqrt{2 \rho}$ instead of $\rho$ (cf. [FG3, Chapter 4]; see in particular Theorem 4.5 and Proposition 4.7). Therefore, the bulk of Step 7 is proving that (ii) implies (iii).

It can be given sense to a vector space structure on formal linear combinations of complete metric contractions of tensor without any reference to dimension or the signature of the metric. If the weight is less than $n$, then the formal vanishing is equivalent to the algebraic vanishing by inputing tensors in dimension $n$. The idea in the proof of the proof of the implication (ii) ⇒ (iii) is showing that (ii) and (iii) are equivalent to the same system of linear equations on the space of formal linear combinations of complete metric contractions of Ricci-flat curvature tensors. This involves proving a version of the "2nd main theorem of invariant theory" for Ricci-flat curvature tensors, rather than for collections of trace-free tensors satisfying the Young symmetries of Riemannian curvature tensors. In other words, we need to establish a nonlinear version of [BEG, Theorem B.3].

Step 8. Proof of Theorem 7.3.
By Step 2 we know that $\gamma_{P_{k, g}}(x)$ is a linear combination of Weyl conformal invariants of weight $2 n-k$, so by Theorem 4.5 there is a Riemannian invariant $I_{g}(x)$ of weight $2 n-k$ such that
$$\gamma_{P_{k, g}}(x)=2 \Gamma(k)^{-1}(4 \pi)^{-\frac{n}{2}} \tilde{I}_{g}(x) .$$
We need to show that $I_{g}(x)=a_{n-2 k}\left(\Delta_{g} ; x\right)$. If $(M, g)$ is Ricci flat, then by Step 3 and Step 4,
$$I_{g}(x)=\tilde{I}_{g}(x)=\frac{1}{2} \Gamma(k)(4 \pi)^{\frac{n}{2}} \gamma_{P_{k, g}}(x)=\frac{1}{2} \Gamma(k)(4 \pi)^{\frac{n}{2}} \gamma_{\Delta_{g}^{k}}(x)=a_{n-2 k}\left(\Delta_{g} ; x\right) .$$
By Step 6 this result continues to hold at a point $x_{0} \in M$ if $\operatorname{Ric}(g)=\mathrm{O}\left(\left|x-x_{0}\right|^{n-2}\right)$ near $x_{0}$. Therefore, in this case the Riemannian invariant $I_{g}(x)-a_{n-2 k}\left(\Delta_{g} ; x\right)$ vanishes at $x_{0}$. Using Step 7
we then deduce that the associated conformal invariant vanishes. That is,
$$\gamma_{P_{k, g}}(x)=2 \Gamma(k)^{-1}(4 \pi)^{-\frac{n}{2}} \tilde{a}_{n-2 k}\left(\Delta_{g} ; x\right) .$$
This proves Theorem 7.3.

\section*{References}
\begin{itemize}
\item[] [ABP] Atiyah, M., Bott, R., Patodi, V.: On the heat equation and the index theorem. Invent. Math. 19, 279-330 (1973). Errata. Invent. Math. 28, 277-280 (1975).
\item[] [BEG] Bailey, T.N.; Eastwood, M.G.; Graham, C.R.: Invariant theory for conformal and CR geometry. Ann. Math. 139 (1994) 491-552.
\item[] [BGS] Beals, R.; Greiner, P.C. Stanton, N.K.: The heat equation on a CR manifold. J. Differential Geom. 20 (1984), no. 2, 343-387.
\item[] [BGM] Berger, M.; Gauduchon, P.; Mazet, E.: Le spectre dune variété riemannienne. Lecture Notes in Mathematics, vol. 194, Springer-Verlag, 1971.
\item[] [Br] Branson, T.: Sharp inequalities, the functional determinant, and the complementary series. Trans. Amer. Math. Soc. 347 (1995), 3671-3742.
\item[] [BG] Branson, T.; Gover, A.R.: Conformally invariant operators, differential forms, cohomology and a generalisation of $Q$-curvature. Comm. Partial Differential Equations 30 (2005), no. 10-12, 1611-1669.
\item[] [CS] Caffarelli, L.; Silvestre, L.: An extension problem related to the fractional Laplacian. Comm. Partial Differential Equations 32 (2007), 1245-1260.
\item[] [CM] Chang, S.-Y.A.; del Mar Gonzàlez, M.: Fractional Laplacian in conformal geometry. Adv. Math. 226 (2011), no. 2, 1410-1432
\item[] [CJ] Chen, L.; Jakobson, D.: Gaussian free fields and $K P Z$ relation in $\mathbb{R}^{4}$. E-print, arXiv, October 2012.
\item[] [CY] Cheng, S.-Y.; Yau, S.-T.: On the regularity of the Monge-Ampère equation $\operatorname{det}\left(\partial^{2} u / \partial x^{i} \partial x^{j}\right)=F(x, u)$. Comm. Pure Appl. Math. 30 (1977), 41-68.
\item[] [Fe1] Fefferman, C.: Monge-Ampère equations, the Bergman kernel, and geometry of pseudoconvex domains. Ann. of Math. (2) 103 (1976), no. 2, 395-416.
\item[] [Fe2] Fefferman, C.: The Bergman kernel and biholomorphic mappings of pseudo-convex domains. Invent. Math. 26 (1974), 1-65.
\item[] [Fe3] Fefferman, C.: Parabolic invariant theory in complex analysis. Adv. in Math. 31 (1979), no. 2, 131-262.
\item[] [FG1] Fefferman, C.; Graham, C.R.: Conformal invariants. Élie Cartan et les Mathématiques d'Aujourd'hui, Astérisque, hors série, (1985), 95-116.
\item[] [FG2] Fefferman, C.; Graham., C.R.: Q-curvature and Poincaré-Einsteinmetrics. Math. Res. Lett. 9 (2002), 139-151.
\item[] [FG3] Fefferman, C.; Graham, C.R.: The ambient metric. Ann. Math. Studies 178, Princeton Univ. Press, 2012.
\item[] [FG4] Fefferman, C.; Graham, C.R.: Juhls formulae for GJMS operators and Q-curvatures . To appear in J. Amer. Soc.. DOI: 10.1090/S0894-0347-2013-00765-1.
\item[] [Gi1] Gilkey, P.B.: Curvature and the eigenvalues of the Laplacian for elliptic complexes. Adv. Math. 10 (1973), 344-382.
\item[] [Gi2] Gilkey, P.B.: The spectral geometry of a Riemannian manifold. J. Differential Geom. 10 (1975), 601-618.
\item[] [Gi3] Gilkey, P.B.: Invariance theory, the heat equation, and the Atiyah-Singer index theorem. 2nd edition. Studies in Advanced Mathematics. CRC Press, Boca Raton, FL, 1995.
\item[] [Go] Gover, A.R.: Laplacian operators and Q-curvature on conformally Einstein manifolds. Math. Ann. 336 (2006), 311-334.
\item[] [GG] Gover, A.R.; Graham, C.R.: CR invariant powers of the sub-Laplacian. J. Reine Angew. Math. 583 (2005), 1-27.
\item[] [GH] A.R. Gover and K. Hirachi. Conformally invariant powers of the Laplacian - A complete non-existence theorem. J. Amer. Math. Soc. 17 (2004), 389-405.
\item[] [GP] Gover, A.R.; Peterson, L.J.: Conformally Invariant Powers of the Laplacian, Q-Curvature, and Tractor Calculus. Comm. Math. Phys. 235 (2003), 339-378.
\item[] [GW] Gover, A.R.; Waldron, A.: Boundary calculus for conformally compact manifolds. E-print, arXiv, April 2011.
\item[] [Gr1] C.R. Graham. Conformally invariant powers of the Laplacian. II. Nonexistence. J. London Math. Soc. (2) 46 (1992), no. 3, 566-576.
\item[] [Gr2] Graham, C.R.: Talk at the workshop Conformal structure in geometry, analysis, and physics. AIM, Palo Alto, Aug. 12-16, 2003.
\item[] [GJMS] Graham, C.R.; Jenne, R.; Mason, L.J.; Sparling, G.A.: Conformally invariant powers of the Laplacian. I. Existence. J. London Math. Soc. (2) 46 (1992), no. 3, 557-565.
\item[] [GrH] Graham, C.R.; Hirachi, M.: Inhomogeneous ambient metrics. Symmetries and overdetermined systems of partial differential equations, 403-420, IMA Vol. Math. Appl., 144, Springer, New York, 2008.
\item[] [GZ] Graham, C.R.; Zworki, M.: Scattering matrix in conformal geometry. Inv. Math. 152 (2003), 89-118.
\item[] [Gr] Greiner, P.: An asymptotic expansion for the heat equation. Arch. Rational Mech. Anal. 41 (1971) 163-218.
\end{itemize}
\begin{itemize}
\item[] [GS] Grubb, G.; Seeley, R.: Weakly parametric pseudodifferential operators and Atiyah-Patodi-Singer boundary problems. Inv. Math. 121 (1995), 481-530.
\item[] [Gu1] Guillarmou, C.: Meromorphic properties of the resolvent on asymptotically hyperbolic manifolds. Duke Math. J. 129 (2005), 1-37.
\item[] [Gu2] Guillarmou, C.: Personal communication.
\item[] [GMP1] Guillarmou, C.; Moroianu, S.; Park, J.: Eta invariant and Selberg zeta function of odd type over convex co-compact hyperbolic manifolds, Adv. Math. 225 (2010), no. 5, 2464-2516.
\item[] [GMP2] Guillarmou, C.; Moroianu, S.; Park, J.: Calderon and Bergman projectors on spin manifolds with boundary. J. Geom. Anal., doi:10.1007/s12220-012-9338-9.
\item[] [GN] Guillarmou, C.; Naud, F.: Wave 0-trace and length spectrum on convex co-compact hyperbolic manifolds. Comm. Anal. Geom. 14 (2006), no. 5, 945-967.
\item[] [Gui1] Guillemin, V.W.: A new proof of Weyl's formula on the asymptotic distribution of eigenvalues. Adv. Math. 55 (1985), no. 2, 131-160.
\item[] [Gui2] Guillemin, V.: gauged Lagrangian distributions. Adv. Math. 102 (1993), no. 2, 184-201.
\item[] [Ju1] Juhl, A.: Families of conformally covariant differential operators, $Q$-curvature and holography. Progress in Mathematics, Birkhäuser, Vol. 275, 2009, 500 pages.
\item[] [Ju2] Juhl, A.: Explicit formulas for $G J M S$-operators and $Q$-curvatures. To appear in Geom. Funct. Anal.. DOI: 10.1007/s00039-013-0232-9.
\item[] [Hi] Hirachi, K.: Construction of boundary invariants and the logarithmic singularity of the Bergman kernel. Ann. Math. 151 (2000) 151-191.
\item[] [Hi] Hirachi, K.: Personal communication.
\item[] [JS] Joshi, M.S.; Sá Barreto, A.: Inverse scattering on asymptotically hyperbolic manifolds. Acta Math. 184 (2000), 41-86.
\item[] [KV] Kontsevich, M.; Vishik, S.: Geometry of determinants of elliptic operators. Functional analysis on the eve of the 21st century, Vol. 1 (New Brunswick, NJ, 1993), 173-197, Progr. Math., 131, Birkhäuser Boston, Boston, MA, 1995.
\item[] [Ku] Kuiper, N.H.: On conformally flat spaces in the large. Ann. of Math. 50 (1949), 916-924.
\item[] [MS] McKean, H.P.; Singer I.M.: Curvature and the eigenvalues of the Laplacian. J. Differential Geom. 1 (1967), 43-69.
\item[] [Le] Lee, J.M.: The Fefferman metric and pseudo-Hermitian invariants. Trans. Amer. Math. Soc. 296 (1986), no. 1, 411-429.
\item[] [LM] Lee, J.M.; Melrose, M.: Boundary behaviour of the complex Monge-Ampre equation. Acta Math. 148 (1982) 159-192.
\item[] [Ma1] Mazzeo, R.: The Hodge cohomology of a conformally compact metric. J. Differential Geom. 28 (1988), 309-339.
\item[] [Ma2] Mazzeo, R.: Unique continuation at infinity and embedded eigenvalues for asymptotically hyperbolic manifolds. Amer. J. Math. 113 (1991), 25-45.
\item[] [MM] Mazzeo, R.; Melrose, R.: Meromorphic extension of the resolvent on complete spaces with asymptotically constant negative curvature. J. Funct. Anal. 75 (1987), 260-310.
\item[] [Mi] Minakshisundaram, S. Eigenfunctions on Riemannian manifolds. J. Indian Math. Soc. (N.S.) 17 (1953), 159-165.
\item[] [Ok] Okikiolu, K.: Critical metrics for the determinant of the Laplacian in odd dimensions. Ann. of Math. 153 (2001), 471-531.
\item[] [Pa] Paneitz, S.: A quartic conformally covariant differential operator for arbitrary pseudo-Riemannian manifolds. Preprint (1983). Reproduced as: SIGMA 4 (2008), 036, 3 pages.
\item[] [PR] Parker, T; Rosenberg, S.: Invariants of conformal Laplacians. J. Differential Geom. 25 (1987), no. 2, 199-222.
\item[] [Pe] Peterson, L.J.: Conformally covariant pseudo-differential operators. Diff. Geom. Appl. 13 (2000), 197-211.
\item[] [Po] Polterovich, I.: Heat invariants of Riemannian manifolds. Israel J. Math. 119 (2000), 239-252.
\item[] [Po1] Ponge, R.: Logarithmic singularities of Schwartz kernels and local invariants of conformal and CR structures operators. E-print, arXiv, October 2007.
\item[] [Po2] Ponge, R.: A microlocal approach to Fefferman's program in conformal and CR geometry. Clay Math. Proc. 12, Amer. Math. Soc. Providence, RI, 2011, pp. 219-242.
\item[] [Ra] Ramadanov, I.P.: A characterization of the balls in $\mathbb{C}^{n}$ by means of the Bergman kernel. C. R. Acad. Bulgare Sci., 34 (1981) 927-929.
\item[] [Sc] Schoen, R.: Conformal deformation of a Riemannian metric to constant scalar curvature. J. Diff. Geom. 20 (1984), 479-495.
\item[] [Se] Seeley, R.T.:Complex powers of an elliptic operator. Singular Integrals, Proceedings of Symposia in Pure Mathematics, Vol. 10, Amer. Math. Soc. Providence, RI, 1976) pp. 288-307. Corrections in Amer. J. Math. textbf91 (1969) 917-919.
\item[] [Ta] Taylor, M.E: Partial differential equations. II. Qualitative studies of linear equations. Applied Mathematical Sciences, 116. Springer-Verlag, New York, 1996. Gr:FCPDOBP
\end{itemize}
[Va1] Vasy, A.: Microlocal analysis of asymptotically hyperbolic spaces and high energy resolvent estimates. Inverse problems and applications. Inside Out II, MSRI Publications, no. 60, Cambridge University Press, 2012.
[Va2] Vasy, A.: Analytic continuation and high energy estimates for the resolvent of the Laplacian on forms on asymptotically hyperbolic spaces. E-print, arXiv, June 2012.
[Wi] Widom, H.: A complete symbolic calculus for pseudo-differerential operators. Bull. Sci. Math. 104 (1980), 19-63.
[Wo1] Wodzicki, M.: Local invariants of spectral asymmetry. Invent. Math. 75 (1984), no. 1, 143-177.
[Wo2] Wodzicki, M.: Noncommutative residue. I. Fundamentals. K-theory, arithmetic and geometry (Moscow, 1984-1986), 320-399, Lecture Notes in Math., 1289, Springer, Berlin-New York, 1987.

Department of Mathematical Sciences, Seoul National University, Seoul, South Korea
E-mail address: ponge.snu@gmail.com