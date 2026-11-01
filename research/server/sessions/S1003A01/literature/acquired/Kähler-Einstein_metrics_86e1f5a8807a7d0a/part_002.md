---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Kähler-Einstein metrics]

The starting point is to show that out of a sequence of solutions to (4.1) with $t_{i} \rightarrow T$, we obtain a limiting metric $\omega_{T}$ on the space $Z$ satisfying the equation
$$\operatorname{Ric}\left(\omega_{T}\right)=T \omega_{T}+(1-T) \beta,$$
where $\beta$ is a positive (1,1)-current on $Z$. This can be used to show that the automorphism group of the pair $(Z, \beta)$, suitably defined, is reductive, and moreover a version of the log Futaki invariant of the pair $(Z,(1-T) \beta)$ vanishes for all vector fields. The missing piece for exploiting this as above is to find a test-configuration for $M$ with central fiber $Z$, under which the form $\alpha$ on $M$ converges to the current $\beta$ on $Z$, but in the end we are not able to do this. Instead, in order to apply a result such as Luna's slice theorem, the idea is to approximate the currents $\alpha$ and $\beta$ with currents of integration along divisors.

Note first that according to Shiffman-Zelditch [149], we can write $\alpha$ as an average of currents of integration $[M \cap H]$ for hyperplane sections of $M$, under a suitable projective embedding $M \subset \mathbf{P}^{N}$. As discussed above, the geometric limit space $Z$ is also an algebraic limit $\lim _{k \rightarrow \infty} \rho_{k}(M)$ for automorphisms $\rho_{k}$ of $\mathbf{P}^{N}$. We can arrange that the limits $\rho_{\infty}(H)=\lim _{k \rightarrow \infty} \rho_{k}(H)$ exist for all hyperplanes $H$ and so $\beta$ is an average of the hyperplane sections $\left[Z \cap \rho_{\infty}(H)\right]$ of $Z$. This can be used to show that a suitable tuple $\left(Z, \rho_{\infty}\left(H_{1}\right), \ldots, \rho_{\infty}\left(H_{l}\right)\right)$ has the same automorphism group as $(Z, \beta)$. One simple example to keep in mind is when $Z$ is a line in $\mathbf{P}^{2}$, and $\beta$ is the Fubini-Study metric. In this case the automorphism group of $(Z, \beta)$ is trivial under our definition, and so we must "mark" $Z$ with at least 3 hyperplane sections to have a tuple with the same automorphism group.

We can argue as before with these tuples, and we obtain a test-configuration $X$ for $M$ with central fiber $Z$, such that in addition the limits of the hyperplanes $H_{1}, \ldots, H_{l}$ under this test-configuration are $\rho_{\infty}\left(H_{1}\right), \ldots, \rho_{\infty}\left(H_{l}\right)$. However, since we do not know that the form $\alpha$ converges to $\beta$ under this test-configuration, we cannot say anything about the Donaldson-Futaki invariant of $X$. To overcome this we choose enough hyperplane sections so that by an approximation argument the log Futaki invariant of the tuple is close to that of the pair $(Z, \beta)$. It remains then to use this to show that $D F(X)<0$, contradicting K-stability of $M$, unless we actually have $Z \cong M$ and $\beta=\alpha$, so that the continuity method can be continued past $t=T$.

To conclude this section we make some remarks about the situation when the limit space $Z$ is not smooth. The overall strategy remains the same, but there are substantial technical difficulties in carrying it through. To start with, one needs to make sense of the Kähler-Einstein equation (or more general equations such as (4.1)) on a singular variety $Z$. Working on a resolution of singularities $\pi: X \rightarrow Z$, the equation is equivalent to a complex Monge-Ampère equation
$$(\omega+\sqrt{-1} \partial \bar{\partial} \phi)^{n}=e^{F-\phi} d V,$$
on $X$, where $d V$ is a smooth volume form, however the function $F$ need not be bounded, and the form $\omega$ is only non-negative. More precisely we have $0 \leq e^{F} \in L^{p}$ for some $p>1$, and $\omega$ is also big, i.e. $\int_{X} \omega^{n}>0$. It cannot be expected that $\phi$ is twice differentiable, and so the equation needs to be defined in a weak sense. This was done for the local theory of the complex Monge-Ampère operator by Bedford-Taylor [14]. Further important progress in understanding such Monge-Ampère equations with right hand side in $L^{p}$ was made by Kołodziej [109] using techniques of pluripotential theory. A detailed study of Kähler-Einstein metrics on singular varieties is given in Eyssidieux-Guedj-Zeriahi [87].

The lack of regularity of such a Kähler-Einstein metric at the singular points means that results such a Matsushima's Theorem on the automorphism group and the vanishing of the Futaki invariant cannot be generalized in a straightforward way.

Instead Chen-Donaldson-Sun [44] proved these results in the singular setting using the theory of geodesics and Berndtsson's convexity and uniqueness results [22].

It is natural to expect that Theorem 2 can be extended to Q-Fano varieties, and indeed Berman [16] showed that Q-Fano varieties admitting (singular) Kähler-Einstein metrics are K-stable. The converse, however, is so far only known for smoothable Q-Fanos, by work of Spotti-Sun-Yao [154].

\section*{5. Applications}

In this final section we briefly survey some applications of the Yau-Tian-Donaldson conjecture for Fano manifolds, and the techniques involved in its solution. The first is perhaps the most direct type of application, namely obtaining new examples of Kähler-Einstein manifolds. The second and third are more theoretical, on understanding the moduli space of Fano Kähler-Einstein manifolds, and the behavior of singular Kähler-Einstein metrics at the singular points.
5.1. New examples. According to Theorem 2, K-stability is a necessary and sufficient condition for a Fano manifold $M$ to admit a Kähler-Einstein metric. As such it is natural to expect that the result can be used to show the existence of new Kähler-Einstein metrics. Unfortunately for any given Fano manifold $M$ of dimension at least two, there are infinitely many possible special degenerations, and so at present there is no general method for testing K-stability. On the other hand there are special circumstances in which one can show that certain varieties admit a Kähler-Einstein metric.

In the two-dimensional case, Tian [165] used the $\alpha$-invariant [163] and its refinements, to show that any Fano surface with reductive automorphism group admits a Kähler-Einstein metric. More generally, calculations of the $\alpha$-invariant, and related concepts such as Nadel's multiplier ideal sheaves [128], lead to many examples of Kähler-Einstein manifolds (see e.g. [40, 59]). Recently Fujita [91] showed that Fano $n$-folds $M$ with $\alpha$-invariant $\alpha(M)=n /(n+1)$, which are borderline for Tian's criterion [163], are still K-stable, and as such they admit Kähler-Einstein metrics.

A different source of examples where K-stability can be checked effectively is Fano manifolds $M$ with large automorphism groups, since in [56] we showed that it is enough to check special degenerations that are compatible with the automorphism group. For instance if $M$ is a toric manifold, then the only torus equivariant special degenerations for $M$ are products, and so $M$ admits a Kähler-Einstein metric whenever the Futaki invariants of all vector fields on $M$ vanish (this result is originally due to Wang-Zhu [175], using different methods). This result has recently been generalized to reductive group compactifications by Delcroix [58] using analytic methods. Subsequently, by classifying equivariant special degenerations, Delcroix [57] generalized this result to spherical varieties, giving new examples of Kähler-Einstein manifolds.

A more general setting is complexity-one spherical varieties [170], for instance Fano $n$-folds with an effective action of an $(n-1)$-dimensional torus. The equivariant special degenerations of these complexity-one T-varieties were classified by Ilten-Süß [101], using the theory of polyhedral divisors [2] and as an application they obtained several new examples of K-stable Fano 3-folds.

Theorem 2 was generalized to the setting of Kähler cones in [52] and, combined with the methods of Ilten-Süß [101], this lead to new examples of Ricci flat Kähler cones. As we discussed in Section 4.1, such Kähler cones arise as tangent cones
of Gromov-Hausdorff limits of Kähler-Einstein manifolds, but they have also been studied extensively from the point of view of Sasakian geometry [95, 26, 152]. To give a simple example, consider the affine variety $M_{p, q} \subset \mathbf{C}^{4}$, given by the equation $x y+z^{p}+w^{q}=0$. This has a natural action of a 2-torus, acting diagonally on $\mathbf{C}^{4}$. Using K-stability, it is shown in [52] that $M_{p, q}$ admits a Ricci flat Kähler cone metric compatible with the torus action, if and only if $2 p>q$ and $2 q>p$. These two conditions correspond to the calculation of a Donaldson-Futaki invariant for two torus equivariant degenerations of $M_{p, q}$, to the hypersurfaces given by the equations $x y+z^{p}=0$ and $x y+w^{q}=0$ respectively.

For manifolds without such large symmetry groups, the general approach of Tian 165 for Fano surfaces has recently been revisited in the work of Odaka-Spotti-Sun [134], Spotti-Sun [153] and Liu-Xu [119]. Here, given a family of Fano manifolds some elements of which are known to be Kähler-Einstein, one tries to find new Kähler-Einstein manifolds using a continuity method in the family. The key problem is to classify the possible Gromov-Hausdorff limits of Kähler-Einstein manifolds in the family. Using this method, and combined with work of Fujita [91], Liu-Xu [119] showed that all smooth 3-dimensional Fano hypersurfaces admit Kähler-Einstein metrics. Ultimately such a study can lead to a complete understanding of the Kähler-Einstein moduli space and its compactification, as we will discuss in the next section.

While a general algorithm for testing K-stability seems to be some ways off at present, it seems likely that these techniques will lead to many more examples.
5.2. The moduli space of Kähler-Einstein manifolds. A basic question in algebraic geometry is to understand the moduli space of a certain manifold, as well as its compactifications. Perhaps the most well known example is the Deligne-Mumford compactification of the moduli space of hyperbolic Riemann surfaces. This compactification of the moduli space of smooth Riemann surfaces is obtained by adding certain "stable" curves with nodal singularities, and the degeneration of smooth curves to these singular ones can in turn be modeled differential geometrically by degenerating families of hyperbolic metrics.

Canonically polarized manifolds are a higher dimensional generalization of hyperbolic Riemann surfaces and compact moduli spaces are obtained by adding the "KSBA-stable" varieties (see Kollár-Shepherd-Barron [108] Alexeev [1], and the survey [107]). It is interesting to note that the KSBA-stable varieties were subsequently found to coincide with the K-stable varieties by work of Odaka [131], and furthermore Berman-Guenancia [20] showed that these all admit (singular) Kähler-Einstein metrics. To complete the analogy with hyperbolic Riemann surfaces it remains to understand the convergence of smooth Kähler-Einstein metrics to the singular ones on a metric level. We emphasize that in the canonically polarized setting all smooth manifolds admit Kähler-Einstein metrics with negative Ricci curvature by Yau's theorem [177], and K-stability only enters in picking out the right type of singular varieties to allow.

By contrast, in the Fano case one cannot form a Hausdorff moduli space containing all the smooth manifolds, since there are non-trivial families over C that are isomorphic to a product over $\mathbf{C}^{*}$. For instance any non-trivial test-configuration for a Fano manifold with smooth central fiber gives such a family. One can hope, however, that K-stable Fano manifolds form good moduli spaces, and that a compactification is obtained by including certain singular K-stable varieties. Moreover
this compact moduli space should agree with the space of Kähler-Einstein Fano manifolds, compactified using the Gromov-Hausdorff topology. A first step is to understand the neighborhood of a Kähler-Einstein manifold in the moduli space. In [159] (see also Brönnle [27]) we proved that given a Kähler-Einstein manifold $M$, its small deformations that admit KE metrics are precisely the ones that are (poly)stable for the action of $\operatorname{Aut}(M)$ on the deformation space of $M$. Thus a small neighborhood of $M$ in the moduli space is modeled by a GIT quotient for the action of $\operatorname{Aut}(M)$.

In the case of surfaces, a global study of the moduli space of Kähler-Einstein manifolds was achieved by Odaka-Spotti-Sun [134], who explicitly identified the compactified moduli space in terms of certain algebro-geometric compactifications. In higher dimensions Spotti-Sun-Yao [154] and Li-Wang-Xu [114] showed that smoothable $K$-stable Q-Fano varieties, i.e. the ones that we expect to appear in the compactified moduli space, all admit singular Kähler-Einstein metrics, which in addition can be obtained as Gromov-Hausdorff limits of smooth KE metrics. Regarding the global structure of the moduli space, the smoothable K-stable Q-Fano varieties are parametrized by a proper algebraic space by work of Odaka [132] and Li-Wang-Xu [114], and moreover the K-stable smooth Fanos form a quasi-projective variety by Li-Wang-Xu [115]. It remains to understand more precisely what varieties these moduli spaces parametrize in analogy with Odaka-Spotti-Sun's work [134] on surfaces, but as we mentioned above, there are special cases where progress has been made, such as in the case of degree 4 del Pezzo manifolds by Spotti-Sun [153] and cubic threefolds by Liu-Xu [119].
5.3. Asymptotics of singular Kähler-Einstein metrics. In Section 4.3 we discussed how singular Kähler-Einstein metrics play an important role in the proof of Theorem 2. Of particular interest are those singular Kähler-Einstein varieties, which arise as limits of smooth Kähler-Einstein manifolds, in view of the importance of forming complete moduli spaces of Fano manifolds [134, 154, 132, 114], as well as Calabi-Yau manifolds [181]. We do not yet have a detailed understanding of the behavior of such singular Kähler-Einstein metrics near the singular points, although much progress has been made. Such an understanding would be necessary in order to use differential geometric techniques on these singular spaces (see e.g. 30, 97 for such applications).

A first step in understanding the metric behavior near the singular points is to understand the metric tangent cone, as discussed in Section 4.1. In the general Riemannian context the tangent cone may depend on the sequence of rescalings chosen to construct it, but in the setting of Kähler-Einstein manifolds Donaldson-Sun [66] showed that the tangent cone is unique, and it has the structure of an affine variety. They also made progress towards an algebro-geometric description of the metric tangent cone, and conjectured that in general the tangent cone at a point $x \in M$ of a singular Kähler-Einstein metric on $M$ can be determined from the germ of the singularity $(M, x)$ using K-stability. Note that it is not always the case that the germ of the tangent cone at the vertex is biholomorphic to the germ $(M, x)$. For example (see [157], [99]) there is a Calabi-Yau metric on a neighborhood of the origin in the hypersurface $x_{0}^{k}+x_{1}^{2}+x_{2}^{2}+x_{3}^{2}=0$ in $\mathbf{C}^{4}$ whose tangent cone at the origin is given by $\mathbf{C} \times \mathbf{C}^{2} / \mathbf{Z}_{2}$, if $k>4$.

An important special case of this conjecture for singular Calabi-Yau varieties was proven by Hein-Sun [100], namely when the germ $(M, x)$ is isomorphic to
the germ $(C, 0)$ of a Ricci flat Kähler cone $C$ at its vertex, and $C$ satisfies some additional technical conditions. This uses some ideas of Li [111] and Li-Liu [113] on an alternative characterization of K-semistability based on the work of Fujita [92] we mentioned in Section 3.4. Using this, Hein-Sun showed that the singular Ricci flat metric on $M$ near $x$ is asymptotic, in a strong sense, to the Ricci flat metric on $C$. Recently, using more algebro-geometric techniques, Li-Xu [117] have also made significant progress towards resolving Donaldson-Sun's conjecture, and they have announced a complete solution.

\section*{References}
\begin{itemize}
\item[] [1] Alexeev, V. Log canonical singularities and complete moduli of stable pairs. arXiv:9608013.
\item[] [2] Altmann, K., and Hausen, J. Polyhedral divisors and algebraic torus actions. Math. Ann. 334 (2006), 557-607.
\item[] [3] Anderson, M. Ricci curvature bounds and Einstein metrics on compact manifolds. J. Amer. Math. Soc. 2, 3 (1989), 455-490.
\item[] [4] Anderson, M. Convergence and rigidity of manifolds under Ricci curvature bounds. Invent. Math. 97 (1990), 429-445.
\item[] [5] Apostolov, V., Calderbank, D. M. J., Gauduchon, P., and Tønnesen-Friedman, C. W. Hamiltonian 2-forms in Kähler geometry III, extremal metrics and stability. Invent. Math. 173, 3 (2008), 547-601.
\item[] [6] Arezzo, C., and Pacard, F. Blowing up and desingularizing constant scalar curvature Kähler manifolds. Acta Math. 196, 2 (2006), 179-228.
\item[] [7] Arezzo, C., and Tian, G. Infinite geodesic rays in the space of Kähler potentials. Ann. Sc. Norm. Super. Pisa Cl. Sci. (5) 2, 4 (2003), 617-630.
\item[] [8] Atiyah, M. F., and Bott, R. The Yang-Mills equations over Riemann surfaces. Philos. Trans. Roy. Soc. London Ser. A 308 (1983), 523-615.
\item[] [9] Aubin, T. Équations du type Monge-Ampère sur les varietés kählériennes compactes. Bull. Sci. Math. (2) 102, 1 (1978), 63-95.
\item[] [10] Aubin, T. Réduction de cas positif de l'équation de Monge-Ampère sur les variétés kählériennes compactes à la démonstration d'une inégalité. J. Funct. Anal. 57, 2 (1984), 143-153.
\item[] [11] Bamler, R. Convergence of Ricci flows with bounded scalar curvature. arXiv:1603.05235.
\item[] [12] Bando, S., Kasue, A., and Nakajima, H. On a construction of coordinates at infinity on manifolds with fast curvature decay and maximal volume growth. Invent. Math. 97, 2 (1989), 313-349.
\item[] [13] Bando, S., and Mabuchi, T. Uniqueness of Einstein Kähler metrics modulo connected group actions. In Algebraic geometry, Sendai (1985), vol. 10 of Adv. Stud. Pure Math., pp. 11-40.
\item[] [14] Bedford, E., and Taylor, B. A. The Dirichlet problem for a complex Monge-Ampère equation. Invent. Math. 37, 1 (1976), 1-44.
\item[] [15] Berman, R. On the optimal regularity of weak geodesics in the space of metrics on a polarized manifold. arXiv:1405.6482.
\item[] [16] Berman, R. K-polystability of Q-Fano varieties admitting Kähler-Einstein metrics. Invent. Math. 203, 3 (2016), 973-1025.
\item[] [17] Berman, R., and Berndtsson, B. Convexity of the K-energy on the space of Kähler metrics and uniqueness of extremal metrics. J. Amer. Math. Soc. 30, 4 (2017), 1165-1196.
\item[] [18] Berman, R., Boucksom, S., and Jonsson, M. A variational approach to the Yau-TianDonaldson conjecture. arXiv:1509.04561.
\item[] [19] Berman, R., Darvas, T., and Lu, C. H. Regularity of weak minimizers of the K-energy and applications to properness and K-stability. arXiv:1602.03114.
\item[] [20] Berman, R., and Guenancia, H. Kähler-Einstein metrics on stable varieties and log canonical pairs. Geom. and Func. Anal. 24, 6 (2014), 1683-1730.
\item[] [21] Berndtsson, B. Curvature of vector bundles associated to holomorphic fibrations. Ann. of Math. (2) 169, 2 (2009), 531-560.
\end{itemize}
[22] Berndtsson, B. A Brunn-Minkowski type inequality for Fano manifolds and some uniqueness theorems in Kähler geometry. Invent. Math. 200, 1 (2015), 149-200.
[23] BøockI, Z. On geodesics in the space of Kähler metrics, vol. 21 of Adv. Lect. Math. (ALM). Int. Press, Somerville, MA, 2012, pp. 3-19.
[24] Boucksom, S., Favre, C., and Jonsson, M. Valuations and plurisubharmonic singularities. Publ. RIMS 44 (2008), 449-494.
[25] Boucksom, S., Hisamoto, T., and Jonsson, M. Uniform K-stability, Duistermaat-Heckman measures and singularities of pairs. arXiv:1504.06568.
[26] Boyer, C., and Galicki, K. Sasakian geometry. Oxford Mathematical Monographs. OUP, 2008.
[27] Brönnle, T. A. Deformation constructions of extremal metrics. Phd Thesis, Imperial College London.
[28] Calabi, E. The space of Kähler metrics. Proc. Internat. Congress Math. Amsterdm, 2 (1954), 206-207.
[29] Calabi, E. Extremal Kähler metrics. In Seminar on Differential Geometry, S. T. Yau, Ed. Princeton, 1982.
[30] Campana, F., Guenancia, H., and Păun, M. Metrics with cone singularities along normal crossing divisors and holomorphic tensor fields. Ann. Sci. École Norm. Sup. (4) 46 (2013), 879-916.
[31] Cao, H. D. Deformation of Kähler metrics to Kähler-Einstein metrics on compact Kähler manifolds. Invent. Math. 81, 2 (1985), 359-372.
[32] Catlin, D. The Bergman kernel and a theorem of Tian. In Analysis and geometry in several complex variables (Katata, 1997) (1999), Trends Math., Birkhäuser Boston Inc., pp. 1-23.
[33] Cheeger, J. Degeneration of Riemannian metrics under Ricci curvature bounds. Lezioni Fermiane. Scuola Normale Superiore, Pisa, 2001.
[34] Cheeger, J., and Colding, T. On the structure of spaces with Ricci curvature bounded below. I. J. Differential Geom. 46, 3 (1997), 406-480.
[35] Cheeger, J., and Colding, T. On the structure of spaces with Ricci curvature bounded below. II. J. Differential Geom. 54, 1 (2000), 13-35.
[36] Cheeger, J., and Colding, T. On the structure of spaces with Ricci curvature bounded below. III. J. Differential Geom. 54, 1 (2000), 37-74.
[37] Cheeger, J., and Ebin, D. G. Comparison theorems in Riemannian geometry. AMS Chelsea Publishing, Providence, RI, 2008.
[38] Cheeger, J., and Naber, A. Lower bounds on Ricci curvature and quantitative behavior of singular sets. Invent. Math. 191, 2 (2013), 321-339.
[39] Cheeger, J., and Naber, A. Regularity of Einstein manifolds and the codimension 4 conjecture. Ann. of Math. (2) 182, 3 (2015), 1093-1165.
[40] Cheltsov, I., and Park, J. Log canonical thresholds and generalized Eckardt points. Sb. Math. 193, 5-6 (2002), 779-789.
[41] Chen, X., Donaldson, S., and Sun, S. Kähler-Einstein metrics and stability. Int. Math. Res. Not. IMRN, 8 (2014), 2119-2125.
[42] Chen, X., Donaldson, S., and Sun, S. Kähler-Einstein metrics on Fano manifolds. I: Approximation of metrics with cone singularities. J. Amer. Math. Soc. 28, 1 (2015), 183-197.
[43] Chen, X., Donaldson, S., and Sun, S. Kähler-Einstein metrics on Fano manifolds. II: Limits with cone angle less than $2 \pi$. J. Amer. Math. Soc. 28, 1 (2015), 199-234.
[44] Chen, X., Donaldson, S., and Sun, S. Kähler-Einstein metrics on Fano manifolds. III: Limits as cone angle approaches $2 \pi$ and completion of the main proof. J. Amer. Math. Soc. 28, 1 (2015), 235-278.
[45] Chen, X., and Sun, S. Space of Kähler metrics V - Kähler quantization. In Metric and differential geometry, vol. 297 of Progr. Math. Birkhäuser Verlag, Basel, 2012, pp. 19-41.
[46] Chen, X., Sun, S., and Wang, B. Kähler-Ricci flow, Kähler-Einstein metric, and Kstability. arXiv:1508.04397.
[47] Chen, X. X. The space of Kähler metrics. J. Differential Geom. 56, 2 (2000), 189-234.
[48] Chen, X. X., and Tang, Y. Test configuration and geodesic rays. Astérisque, 321 (2008), 139-167.
[49] Chen, X. X., and Wang, B. Space of Ricci flows (II). arXiv:1405.6797.
[50] Chu, J., Tosatti, V., and Weinkove, B. On the $C^{1,1}$ regularity of geodesics in the space of Kähler metrics. arXiv:1611.02390.
[51] Colding, T. H. Ricci curvature and volume convergence. Ann. of Math. (2) 145, 3 (1997), 477-501.
[52] Collins, T., and Székelyhidi, G. Sasaki-Einstein metrics and K-stability. arXiv:1512.07213.
[53] Darvas, T. Morse theory and geodesics in the space of Kähler metrics. Proc. Amer. Math. Soc. 142, 8 (2014), 2775-2782.
[54] Darvas, T. The Mabuchi geometry of finite energy classes. Adv. Math. 285 (2015), 182-219.
[55] Darvas, T., and Rubinstein, Y. A. Tian's properness conjectures and Finsler geometry of the space of Kähler metrics. J. Amer. Math. Soc. 30, 2 (2017), 347-387.
[56] Datar, V., and Székelyhidi, G. Kähler-Einstein metrics along the smooth continuity method. Geom. and Func. Anal. 26, 4 (2016), 975-1010.
[57] Delcroix, T. K-stability of Fano spherical varieties. arXiv:1608.01852.
[58] Delcroix, T. Kähler-Einstein metrics on group compactifications. Geom. and Func. Anal. 27, 1 (2017), 78-129.
[59] Demailly, J.-P., and Kollár, J. Semi-continuity of complex singularity exponents and Kähler-Einstein metrics on Fano orbifolds. Ann. Sci. Éc. Norm. Supér. (4) 34 (2001), 525-556.
[60] Dervan, R. Relative K-stability for Kähler manifolds. arXiv:1611.00569.
[61] Dervan, R. Alpha invariants and K-stability for general polarizations of Fano varieties. Int. Math. Res. Not. IMRN, 16 (2015), 7162-7189.
[62] Dervan, R. Uniform stability of twisted constant scalar curvature Kähler metrics. Int. Math. Res. Not. 15 (2016), 4728-4783.
[63] Dervan, R., and Ross, J. K-stability for Kähler manifolds. arXiv:1602.08983.
[64] Ding, W. Y. Remarks on the existence problem of positive Kähler-Einstein metrics. Math. Ann. 282, 3 (1988), 463-471.
[65] Ding, W. Y., and Tian, G. Kähler-Einstein metrics and the generalized Futaki invariant. Invent. Math. 110, 2 (1992), 315-335.
[66] Donaldson, S., and Sun, S. Gromov-Hausdorff limits of Kähler manifolds and algebraic geometry, II. arXiv:1507.05082.
[67] Donaldson, S., and Sun, S. Gromov-Hausdorff limits of Kähler manifolds and algebraic geometry. Acta Math. 213, 1 (2014), 63-106.
[68] Donaldson, S. K. The Ding functional, Berndtsson convexity and moment maps. arXiv:1503.05173.
[69] Donaldson, S. K. A new proof of a theorem of Narasimhan and Seshadri. J. Differential Geom. 18, 2 (1983), 269-277.
[70] Donaldson, S. K. Anti self-dual yang-mills connections over complex algebraic surfaces and stable vector bundles. Proc. London Math. Soc. 50 (1985), 1-26.
[71] Donaldson, S. K. Infinite determinants, stable bundles and curvature. Duke Math. J. 54, 1 (1987), 231-247.
[72] Donaldson, S. K. Remarks on gauge theory, complex geometry and four-manifold topology. In Fields Medallists' Lectures, Atiyah and Iagolnitzer, Eds. World Scientific, 1997, pp. 384-403.
[73] Donaldson, S. K. Symmetric spaces, Kähler geometry and Hamiltonian dynamics. In Northern California Symplectic Geometry Seminar, vol. 196 of Amer. Math. Soc. Transl. Ser. 2. Amer. Math. Soc., Providence, RI, 1999, pp. 13-33.
[74] Donaldson, S. K. Planck's constant in complex and almost-complex geometry. In XIIIth International Congress on Mathematical Physics (London, 2000). Int. Press, Boston, MA, 2001, pp. 63-72.
[75] Donaldson, S. K. Scalar curvature and projective embeddings, I. J. Differential Geom. 59 (2001), 479-522.
[76] Donaldson, S. K. Holomorphic discs and the complex Monge-Ampère equation. J. Symplectic Geom. 1, 2 (2002), 171-196.
[77] Donaldson, S. K. Scalar curvature and stability of toric varieties. J. Differential Geom. 62 (2002), 289-349.
[78] Donaldson, S. K. Lower bounds on the Calabi functional. J. Differential Geom. 70, 3 (2005), 453-472.
[79] Donaldson, S. K. Scalar curvature and projective embeddings, II. Q. J. Math. 56, 3 (2005), 345-356.
[80] Donaldson, S. K. Discussion of the Kähler-Einstein problem. http://www2.imperial.ac.uk/ ${ }^{\sim}$ skdona/KENOTES.PDF (2009).
[81] Donaldson, S. K. Some numerical results in complex differential geometry. Pure Appl. Math. Q. 5, 2 (2009), 571-618.
[82] Donaldson, S. K. Kähler metrics with cone singularities along a divisor. In Essays in mathematics and its applications. Springer, Heilderlberg, 2012, pp. 49-79.
[83] Donaldson, S. K. Stability, birational transformations and the Kähler-Einstein problem, vol. 17 of Surv. Differ. Geom. Int. Press, Boston, MA, 2012, pp. 203-228.
[84] Donaldson, S. K. b-stability and blow-ups. Proc. Edinb. Math. Soc. (2) 57, 1 (2014), 125-137.
[85] Donaldson, S. K., and Kronheimer, P. B. The Geometry of Four-Manifolds. OUP, 1990.
[86] Eyssidieux, P. Mètriques de Kähler-Einstein sur les variétés de Fano [d'après Chen-Donaldson-Sun et Tian]. Astérisque, 380, Séminaire Bourbaki. Vol. 2014/2015 (2016).
[87] Eyssidieux, P., Guedj, V., and Zeriahi, A. Singular Kähler-Einstein metrics. J. Amer. Math. Soc. 22, 3 (2009), 607-639.
[88] Fine, J. Calabi flow and projective embeddings. With an appendix by Kefeng Liu and Xiaonan Ma. J. Differential Geom. 84, 3 (2010), 489-523.
[89] Fine, J. Quantisation and the Hessian of Mabuchi energy. Duke Math. J. 161, 14 (2012), 2753-2798.
[90] Fujiki, A. Moduli space of polarized algebraic manifolds and Kähler metrics [translation of Sûgaku 42 (1990), no. 3, 231-243;]. Sugaku Expositions 5, 2 (1992), 173-191.
[91] Fujita, K. K-stability of Fano manifolds with not small alpha invariants. arXiv:1606.08261.
[92] Fujita, K. Optimal bounds for the volumes of Kähler-Einstein Fano manifolds. arXiv:1508.04578.
[93] Futaki, A. An obstruction to the existence of Einstein-Kähler metrics. Invent. Math. 73 (1983), 437-443.
[94] Gauduchon, P. Calabi's extremal Kähler metrics: An elementary introduction.
[95] Gauntlett, J. P., Martelli, D., Sparks, J., and Yau, S.-T. Obstructions to the existence of Sasaki-Einstein metrics. Comm. Math. Phys. 273, 3 (2007), 803-827.
[96] Gromov, M. Metric structures for Riemannian and non-Riemannian spaces. Birkhäuser Boston Inc., 2007.
[97] Guenancia, H., and Taji, B. Orbifold stability and Miyaoka-Yau inequality for minimal pairs. arXiv:1611.0598.
[98] Hamilton, R. Three-manifolds with positive Ricci curvature. J. Differential Geom. 17, 2 (1982), 255-306.
[99] Hein, H.-J., and Naber, A. Isolated Einstein singularities with singular tangent cones. in preparation.
[100] Hein, H.-J., and Sun, S. Calabi-Yau manifolds with isolated conical singularities. arXiv:1607.02940.
[101] Ilten, N., and Süss, H. K-stability for varieties with torus action of complexity one. Duke Math. J. 166, 1 (2017), 177-204.
[102] Jeffres, T., Mazzeo, R., and Rubinstein, Y. A. Kähler-Einstein metrics with edge singularities. Ann. of Math. (2) 183, 1 (2016), 95-176.
[103] Jiang, W. Bergman kernel along the Kähler Ricci flow and Tian's conjecture. J. Reine Angew. Math. 717 (2016), 195-226.
[104] Kähler, E. Über eine bemerkenswerte Hermitesche Metrik. Abh. Math. Sem. Univ. Hamburg 9, 1 (1933), 173-186.
[105] Kazdan, J. L., and Warner, F. W. Curvature functions for compact 2-manifolds. Ann. of Math. 99 (1974), 14-47.
[106] Kempf, G., and Ness, L. The length of vectors in representation spaces. In Algebraic geometry (Proc. Summer Meeting, Univ. Copenhagen, Copenhagen, 1978), vol. 732 of Lecture Notes in Math. Springer, Berlin, 1979, pp. 233-243.
[107] Kollár, J. Moduli of varieties of general type. In Handbook of moduli. Vol. II. 2013, pp. 131-157.
[108] Kollár, J., and Shepherd-Barron, N. I. Threefolds and deformations of surface singularities. Invent. Math. 91, 2 (1988), 299-338.
[109] Kolodziej, S. The complex Monge-Ampère equation. Acta Math. 180, 1 (1998), 69-117.
[110] Lempert, L., and Vivas, L. Geodesics in the space of Kähler metrics. Duke Math. J. 162, 7 (2013), 1369-1381.
[111] LI, C. K-semistability is equivariant volume minimization. arXiv:1512.07205.
[112] LI, C. Constant scalar curvature Kähler metric obtains the minimum of K-energy. Internat. Math. Res. Notices, 9 (2011), 2161-2175.
[113] Li, C., and Liu, Y. Kähler-Einstein metrics and volume minimization. arXiv:1602.05094.
[114] Li, C., Wang, X., and Xu, C. On proper moduli space of smoothable Kähler-Einstein Fano varieties. arXiv:1411.0761.
[115] Li, C., Wang, X., and Xu, C. Quasi-projectivity of the moduli space of smooth Kähler-Einstein Fano manifolds. arXiv:1502.06532.
[116] Li, C., and Xu, C. Stability of Valuations and Kollár Components. arXiv:1604.05398.
[117] Li, C., and Xu, C. Stability of valuations: higher rational rank. arXiv:1707.05561.
[118] Li, C., and Xu, C. Special test configurations and K-stability of Fano varieties. Ann. of Math. (2) 180, 2 (2014), 197-232.
[119] Liu, Y., and Xu, C. K-stability of cubic threefolds. arXiv:1706.01933.
[120] Lu, Z. On the lower order terms of the asymptotic expansion of Tian-Yau-Zelditch. Amer. J. Math. 122, 2 (1998), 235-273.
[121] Luna, D. Slices étales. In Sur les groupes algébriques, Bull. Soc. Math. France, Paris, Mémoire 33. Soc. Math. France, Paris, 1973, pp. 81-105.
[122] Luo, H. Geometric criterion for Gieseker-Mumford stability of polarized manifolds. J. Dif-ferential Geom. 49 (1998), 577-599.
[123] Mabuchi, T. K-energy maps integrating Futaki invariants. Tohoku Math. J. 38, 4 (1986), 575-593.
[124] Mabuchi, T. Some symplectic geometry on compact Kähler manifolds. Osaka J. Math. 24 (1987), 227-252.
[125] Mabuchi, T. An energy-theoretic approach to theHitchin-Kobayashi correspondence for manifolds, I. Invent. Math. 159, 2 (2005), 225-243.
[126] Matsushima, Y. Sur la structure du groupe d'homéomorphismes analytiques d'une certaine variété kählérienne. Nagoya Math. J. 11 (1957), 145-150.
[127] Mumford, D., Fogarty, J., and Kirwan, F. Geometric invariant theory, third ed., vol. 34 of Ergebnisse der Mathematik und ihrer Grenzgebiete (2) [Results in Mathematics and Related Areas (2)]. Springer-Verlag, Berlin, 1994.
[128] Nadel, A. M. Multiplier ideal sheaves and Kähler-Einstein metrics of positive scalar curvature. Ann. of Math. (2) 132, 3 (1990), 549-596.
[129] Narasimhan, M. S., and Seshadri, C. S. Stable and unitary vector bundles on a compact Riemann surface. Ann. of Math. (2) 82 (1965), 540-567.
[130] Odaka, Y. A generalization of the Ross-Thomas slope theory. Osaka J. Math. 50, 1 (2013), 171-185.
[131] Odaka, Y. The GIT stability of polarized varieties via discrepancy. Ann. of Math. (2) 177, 2 (2013), 645-661.
[132] Odaka, Y. Compact moduli spaces of Kähler-Einstein Fano varieties. Publ. Res. Inst. Math. Sci. 51, 3 (2015), 549-565.
[133] Odaka, Y., and Sano, Y. Alpha invariant and K-stability of Q-Fano varieties. Adv. Math. 229, 5 (2012), 2818-2834.
[134] Odaka, Y., Spotti, C., and Sun, S. Compact moduli spaces of Del Pezzo surfaces and Kähler-Einstein metrics. J. Differential Geom. 102, 1 (2016), 127-172.
[135] Paul, S. T. Hyperdiscriminant polytopes, Chow polytopes, and Mabuchi energy asymptotics. Ann. of Math. (2) 175, 1 (2012), 255-296.
[136] Paul, S. T., and Tian, G. CM stability and the generalized Futaki invariant, I. arXiv:0605278.
[137] Perelman, G. The entropy formula for the Ricci flow and its geometric applications. math.DG/0211159.
[138] Phong, D. H., Song, J., and Sturm, J. Degenerations of Kähler-Ricci solitons on Fano manifolds. Univ. Iagel. Acta Math. 52 (2015), 29-43.
[139] Phong, D. H., and Sturm, J. Lectures on stability and constant scalar curvature. In Current Developments in Mathematics 2007. International Press.
[140] Phong, D. H., and Sturm, J. Test-configurations for K-stability and geodesic rays. Jour. Symplectic Geom. 5, 2 (2007), 221-247.
[141] Phong, D. H., and Sturm, J. Regularity of geodesic rays and Monge-Ampère equations. Proc. Amer. Math. Soc. 138, 10 (2010), 3637-3650.
[142] Ross, J., and Thomas, R. P. An obstruction to the existence of constant scalar curvature Kähler metrics. J. Differential Geom. 72 (2006), 429-466.
[143] Ross, J., and Thomas, R. P. A study of the Hilbert-Mumford criterion for the stability of projective varieties. J. Algebraic Geom. 16, 2 (2007), 201-255.
[144] Ross, J., and Witt Nyström, D. Harmonic discs of solutions to the complex homogeneous Monge-Ampère equation. Publ. Math. Inst. Hautes Études Sci. 122 (2015), 315-335.
[145] Rubinstein, Y. A., and Zelditch, S. Bergman approximations of harmonic maps into the space of Kähler metrics on toric varieties. J. Symplectic Geom. 8, 3 (2010), 239-265.
[146] Sano, Y., and Tipler, C. Extremal metrics and lower bound of the modified K-energy. J. Eur. Math. Soc. 17, 9 (2015), 2289-2310.
[147] Semmes, S. Complex Monge-Ampère equations and symplectic manifolds. Amer. J. Math. 114 (1992), 495-550.
[148] Seyyedali, R. Relative Chow stability and extremal metrics. arXiv:1610.07555.
[149] Shiffman, B., and Zelditch, S. Distribution of zeros of random and quantum chaotic sections of positive line bundles. Comm. Math. Phys. 200, 3 (1999), 661-683.
[150] Sjöström Dyrefelt, Z. K-semistability of cscK manifolds with transcendental cohomology class. arXiv:1601.07659.
[151] Song, J., and Zelditch, S. Bergman metrics and geodesics in the space of Kähler metrics on toric varieties. Anal. PDE 3, 3 (2010), 295-358.
[152] Sparks, J. New results in Sasaki-Einstein geometry. In Riemannian topology and geometric structures on manifolds, vol. 271 of Progr. Math. Birkhäuser Boston Inc., 2009, pp. 161-184.
[153] Spotti, C., and Sun, S. Explicit Gromov-Hausdorff compactifications of moduli spaces of Kähler-Einstein Fano manifolds. arXiv:1705.00377.
[154] Spotti, C., Sun, S., and Yao, C. Existence and deformations of Kahler-Einstein metrics on smoothable Q-Fano varieties. Duke Math. J. 165, 16 (2016), 3043-3083.
[155] Stoppa, J. K-stability of constant scalar curvature Kähler manifolds. Adv. Math. 221, 4 (2009), 1397-1408.
[156] Stoppa, J., and Székelyhidi, G. Relative K-stability of extremal metrics. J. Eur. Math. Soc. 13, 4 (2011), 899-909.
[157] Székelyhidi, G. Degenerations of $\mathbf{C}^{n}$ and Calabi-Yau metrics. arXiv:1706.00357.
[158] Székelyhidi, G. Extremal metrics and K-stability. Bull. Lond. Math. Soc. 39, 1 (2007), 76-84.
[159] Székelyhidi, G. The Kähler-Ricci flow and K-polystability. Amer. J. Math. 132 (2010), 1077-1090.
[160] Székelyhidi, G. Filtrations and test-configurations, with an appendix by S. Boucksom. Math. Ann. 362, 1-2 (2015), 451-484.
[161] Székelyhidi, G. The partial $C^{0}$-estimate along the continuity method. J. Amer. Math. Soc. 29, 2 (2016), 537-560.
[162] Thomas, R. P. Notes on GIT and symplectic reduction for bundles and varieties. In Surveys in differential geometry. Vol. X. Int. Press, Somerville, MA, 2006, pp. 221-273.
[163] Tian, G. On Kähler-Einstein metrics on certain Kähler manifolds with $c_{1}(M)>0$. Invent. Math. 89 (1987), 225-246.
[164] Tian, G. On a set of polarized Kähler metrics on algebraic manifolds. J. Differential Geom. 32, 1 (1990), 99-130.
[165] Tian, G. On Calabi's conjecture for complex surfaces with positive first Chern class. Invent. Math. 101, 1 (1990), 101-172.
[166] Tian, G. Kähler-Einstein metrics with positive scalar curvature. Invent. Math. 137 (1997), 1-37.
[167] Tian, G. Canonical metrics in Kähler geometry. Lectures in Mathematics ETH Zürich. Birkhäuser Verlag, Basel, 2000.
[168] Tian, G., and Zhang, Z. Degeneration of Kähler-Ricci solitons. Int. Math. Res. Not. IMRN, 5 (2012), 957-985.
[169] Tian, G., and Zhang, Z. Regularity of Kähler-Ricci flows on Fano manifolds. Acta Math. 216, 1 (2016), 127-176.
[170] Timashev, D. A. Homogeneous spaces and equivariant embeddings, vol. 138 of Encyclopaedia of Mathematical Sciences. Springer, Heilderlberg, 2011. Invariant Theory and Algebraic Transformation Groups, 8.
[171] Uhlenbeck, K. Connections with $L^{p}$ bounds on curvature. Comm. Math. Phys. 83 (1982), 31-42.
[172] Uhlenbeck, K. Removable singularities in Yang-Mills fields. Comm. Math. Phys. 83 (1982), 11-29.
[173] Uhlenbeck, K., and Yau, S.-T. On the existence of Hermitian-Yang-Mills connections in stable vector bundles. Comm. Pure Appl. Math. 39 (1986), 257-293.
[174] Wang, X. Height and GIT weight. Math. Res. Lett. 19, 4 (2012), 909-926.
[175] Wang, X.-J., and Zhu, X. Kähler-Ricci solitons on toric manifolds with positive first Chern class. Adv. Math. 188 (2004), 87-103.
[176] Witt Nyström, D. Test configurations and Okounkov bodies. Compos. Math. 148, 6 (2012), 1736-1756.
[177] Yau, S.-T. On the Ricci curvature of a compact Kähler manifold and the complex Monge-Ampère equation I. Comm. Pure Appl. Math. 31 (1978), 339-411.
[178] Yau, S.-T. Open problems in geometry. Proc. Symposia Pure Math. 54 (1993), 1-28.
[179] Zelditch, S. Szegő kernel and a theorem of Tian. Int. Math. Res. Notices 6 (1998), 317-331.
[180] Zhang, S. Heights and reductions of semi-stable varieties. Compos. Math. 104, 1 (1996), 77-105.
[181] Zhang, Y. Completion of the moduli space for polarized Calabi-Yau manifolds. J. Differential Geom. 103, 3 (2016), 521-544.

Department of Mathematics, University of Notre Dame, Notre Dame, IN 46556
E-mail address: gszekely@nd.edu