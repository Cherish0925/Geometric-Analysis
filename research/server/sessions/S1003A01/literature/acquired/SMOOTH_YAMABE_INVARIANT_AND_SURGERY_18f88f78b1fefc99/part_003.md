---
retention_scope: session
part: 3
total_parts: 3
---

[Part 3/3 of: SMOOTH YAMABE INVARIANT AND SURGERY]

Hence, we can construct a subsequence of $\theta$ and a sequence $\left(b_{\theta}\right)$ of positive numbers converging to 0 with
$$\liminf _{\theta \searrow 0}\left(\mu_{\theta} \sup _{U_{\epsilon}^{N}\left(b_{\theta}\right)} u_{\theta}^{p-2}\right) \geq \frac{(n-k-2)^{2}(n-1)}{8(n-2)} .$$
Choose a point $x_{\theta}^{\prime \prime} \in \overline{U_{\epsilon}^{N}\left(b_{\theta}\right)}$ such that $u_{\theta}\left(x_{\theta}^{\prime \prime}\right)=\sup _{U_{\epsilon}^{N}\left(b_{\theta}\right)} u_{\theta}$. Since $\mu_{\theta} \leq \mu\left(\mathbb{S}^{n}\right)$, we have
$$u_{\theta}\left(x_{\theta}^{\prime \prime}\right) \geq D_{1}:=\left(\frac{(n-k-2)^{2}(n-1)}{8 \mu\left(\mathbb{S}^{n}\right)(n-2)}\right)^{\frac{1}{p-2}} .$$
With similar arguments as in Subcase II.1.1 (just replace $x_{\theta}^{\prime}$ by $x_{\theta}^{\prime \prime}$ and $D_{0}$ by $D_{1}$ ), we get the existence of a $C^{2}$ function $u \geq 0$ that is a solution of
$$L^{G_{c}} u=\bar{\mu} u^{p-1}$$
on $\mathbb{H}_{c}^{k+1} \times S^{n-k-1}$. As in Subsubcase II.1.1, $u \not \equiv 0, u \in L^{\infty}\left(\mathbb{H}_{c}^{k+1} \times\right.$ $\left.S^{n-k-1}\right)$, and
$$\int_{\mathbb{R}^{k+1} \times S^{n-k-1}} u^{p} d v^{G_{c}} \leq 1 .$$
Moreover, the assumption of Subcase II. 2 implies that
$$\bar{\mu} u^{p-2}(0)=\lim _{\theta \searrow 0} \mu_{\theta} u_{\theta}^{p-2}\left(x_{\theta}^{\prime \prime}\right) \geq \frac{(n-k-2)^{2}(n-1)}{8(n-2)} .$$
By the definition of $\Lambda_{n, k}^{(2)}$, we have that $\bar{\mu} \geq \Lambda_{n, k}^{(2)} \geq \Lambda_{n, k}$.

\section*{Appendix A. Some details}
A.1. Scalar curvature. In this section $U$ denotes an open subset of a manifold and $q \in U$ a fixed point.

Proposition A.1. Let $g$ be a Riemannian metric on $U$ and $T$ a symmetric 2-tensor such that $\tilde{g}:=g+T$ is also a Riemannian metric. Then the scalar curvature $\operatorname{Scal}^{\tilde{g}}(q)$ of $\tilde{g}$ in $q \in U$ is a smooth function of the Riemann tensor $R^{g}(q)$ of $g$ at $q, T(q), \nabla^{g} T(q)$, and $\left(\nabla^{g}\right)^{2} T(q)$. Moreover, the operator $T \mapsto \operatorname{Scal}^{g+T}(q)$ is a quasilinear partial differential operator of second order.

Proof. The proof is straightforward; we will just give a sketch using notation from [8] which coincides with that of [26]. We denote the components of the curvature tensors of $g$ and $\tilde{g}$ by
$$R_{i j k l}=g\left(R^{g}\left(\partial_{k}, \partial_{l}\right) \partial_{j}, \partial_{i}\right), \quad \tilde{R}_{i j k l}=\tilde{g}\left(R^{\tilde{g}}\left(\partial_{k}, \partial_{l}\right) \partial_{j}, \partial_{i}\right) .$$
We work in normal coordinates for the metric $g$ centered in $q$, indices of partial derivatives in coordinates are added and separated with a comma "," and covariant ones with respect to $g$ separated with a semicolon ";". In particular $T=T_{i j} d x^{i} d x^{j}$,
$$T_{k l ; i}=\left(\nabla_{i} T\right)\left(\partial_{k}, \partial_{l}\right)=\partial_{i} T_{k l}-T_{m l} \Gamma_{i k}^{m}-T_{k m} \Gamma_{i l}^{m} .$$
At the point $q$ we have $\tilde{g}_{k l, i}=T_{k l ; i}$. As explained in [8, Formula (13)] we have
$$\nabla_{\alpha} \Gamma_{i j}^{k}=\partial_{\alpha} \Gamma_{i j}^{k}=-\frac{1}{3}\left(R_{i k \alpha j}+R_{i \alpha k j}\right)$$
at the point $q$. Hence in that point,
$$\begin{aligned}
T_{k l ; r s} & =\left(\nabla_{r s}^{2} T\right)\left(\partial_{k}, \partial_{l}\right) \\
& =\partial_{r} \partial_{s} T_{k l}+\frac{1}{3} T_{m l}\left(R_{s m r k}+R_{s r m k}\right)+\frac{1}{3} T_{m k}\left(R_{s m r l}+R_{s r m l}\right) .
\end{aligned}$$
In order to calculate the scalar curvature $\operatorname{Scal}^{\tilde{g}}(q)$ of $\tilde{g}$ in $q$ we use the curvature formula as in [26] and contract twice. We obtain
$$\operatorname{Scal}^{\tilde{g}}(q)=\tilde{g}^{i k} \tilde{g}^{j m}\left(\tilde{g}_{k m, i j}-\tilde{g}_{k i, m j}\right)+P\left(\tilde{g}^{r m}, \tilde{g}_{i j, k}\right)$$
where $P$ is a polynomial expression in $\tilde{g}^{-1}$ and $\partial \tilde{g}$ that is cubic in $\tilde{g}^{-1}=\tilde{g}^{r m}$ and quadratic in $\tilde{g}_{i j, k}$. Note that formula (64) holds for an arbitrary metric in arbitrary coordinates. The polynomial $P$ vanishes for $T=0$ in normal coordinates for $g$. \(\square\)

Corollary A.2. Let $\mathcal{R} \subset T_{q}^{*} M \otimes T_{q}^{*} M \otimes T_{q}^{*} M \otimes T_{q} M$ be a bounded set of curvature tensors. Then there is an $\epsilon>0$ and $C \in \mathbb{R}$ such that for all metrics $g$ on $U$ with $\left.R^{g}\right|_{q} \in \mathcal{R}$ we have the following: if
$$\max _{i \in\{0,1,2\}}\left|\left(\nabla^{g}\right)^{i} T(q)\right|<\epsilon,$$
then
$$\left|\operatorname{Scal}^{g+T}(q)-\operatorname{Scal}^{g}(q)\right| \leq C\left(\left|\left(\nabla^{g}\right)^{2} T(q)\right|+\left|\nabla^{g} T(q)\right|^{2}+|T(q)|\right) .$$
A.2. Details for equation (16). We compute the scalar curvature of the metric $d t^{2}+e^{2 \varphi(t)} h_{t}$ on $I \times W$. This is a generalized cylinder metric as studied in [11]. In the following computations we use the notation from [11], so $g_{t}=e^{2 \varphi(t)} h_{t}$ and we have
$$\dot{g}_{t}=2 \varphi^{\prime}(t) e^{2 \varphi(t)} h_{t}+e^{2 \varphi(t)} \partial_{t} h_{t},$$
and
$$\ddot{g}_{t}=\left(2 \varphi^{\prime \prime}(t)+4 \varphi^{\prime}(t)^{2}\right) e^{2 \varphi(t)} h_{t}+4 \varphi^{\prime}(t) e^{2 \varphi(t)} \partial_{t} h_{t}+e^{2 \varphi(t)} \partial_{t}^{2} h_{t} .$$
This implies that the shape operator $S$ of the hypersurfaces defined by having constant value $t$ is given by
$$S=-\varphi^{\prime} \mathrm{Id}-\frac{1}{2} h_{t}^{-1} \partial_{t} h_{t},$$
so
$$\operatorname{tr}\left(S^{2}\right)=k \varphi^{\prime}(t)^{2}+\varphi^{\prime}(t) \operatorname{tr}\left(h_{t}^{-1} \partial_{t} h_{t}\right)+\frac{1}{4} \operatorname{tr}\left(\left(h_{t}^{-1} \partial_{t} h_{t}\right)^{2}\right),$$
and
$$(\operatorname{tr} S)^{2}=k^{2} \varphi^{\prime}(t)^{2}+k \varphi^{\prime}(t) \operatorname{tr}\left(h_{t}^{-1} \partial_{t} h_{t}\right)+\frac{1}{4}\left(\operatorname{tr}\left(h_{t}^{-1} \partial_{t} h_{t}\right)\right)^{2} .$$
Further
$$\begin{aligned}
\operatorname{tr}^{g_{t}} \ddot{g}_{t} & =\left(2 \varphi^{\prime \prime}(t)+4 \varphi^{\prime}(t)^{2}\right) k+4 \varphi^{\prime}(t) \operatorname{tr}^{h_{t}}\left(\partial_{t} h_{t}\right)+\operatorname{tr}^{h_{t}}\left(\partial_{t}^{2} h_{t}\right) \\
& =\left(2 \varphi^{\prime \prime}(t)+4 \varphi^{\prime}(t)^{2}\right) k+4 \varphi^{\prime}(t) \operatorname{tr}\left(h_{t}^{-1} \partial_{t} h_{t}\right)+\operatorname{tr}\left(h_{t}^{-1} \partial_{t}^{2} h_{t}\right) .
\end{aligned}$$
From [11, Proposition 4.1, (21)] we have
$$\begin{aligned}
\text { Scal }^{e^{2 \varphi(t)}} h_{t}+d t^{2}= & \operatorname{Scal}^{e^{2 \varphi(t)} h_{t}}+3 \operatorname{tr}\left(S^{2}\right)-(\operatorname{tr} S)^{2}-\operatorname{tr}^{g_{t}} \ddot{g}_{t} \\
= & e^{-2 \varphi(t)} \operatorname{Scal}{ }^{h_{t}}-k(k+1) \varphi^{\prime}(t)^{2} \\
& -(k+1) \varphi^{\prime}(t) \operatorname{tr}\left(h_{t}^{-1} \partial_{t} h_{t}\right)-2 k \varphi^{\prime \prime}(t)+\frac{3}{4} \operatorname{tr}\left(\left(h_{t}^{-1} \partial_{t} h_{t}\right)^{2}\right) \\
& -\frac{1}{4}\left(\operatorname{tr}\left(h_{t}^{-1} \partial_{t} h_{t}\right)\right)^{2}-\operatorname{tr}\left(h_{t}^{-1} \partial_{t}^{2} h_{t}\right) .
\end{aligned}$$
When we add the scalar curvature of $\sigma^{n-k-1}$ we get Formula (16) for the scalar curvature of $g_{\mathrm{WS}}=d t^{2}+e^{2 \varphi(t)} h_{t}+\sigma^{n-k-1}$.
A.3. A cut-off formula. Here we state a formula used several times in the article. Assume that $u$ and $\chi$ are smooth functions on a Riemannian manifold $(N, h)$, and that $\chi$ has compact support. Then
$$\begin{aligned}
\int_{N}|d(\chi u)|^{2} d v^{h} & =\int_{N}\left(u^{2}|d \chi|^{2}+\langle u d \chi, \chi d u\rangle+\langle\chi d u, d(\chi u)\rangle\right) d v^{h} \\
& =\int_{N}\left(u^{2}|d \chi|^{2}+\chi u\langle d \chi, d u\rangle+\langle d u, \chi d(\chi u)\rangle\right) d v^{h} \\
& =\int_{N}\left(u^{2}|d \chi|^{2}+\chi u\langle d \chi, d u\rangle+\left\langle d u, d\left(\chi^{2} u\right)-\chi u d \chi\right\rangle\right) d v^{h} \\
& =\int_{N}\left(u^{2}|d \chi|^{2}+\left\langle d u, d\left(\chi^{2} u\right)\right\rangle\right) d v^{h} \\
& =\int_{N}\left(u^{2}|d \chi|^{2}+\chi^{2} u \Delta^{h} u\right) d v^{h}
\end{aligned}$$

\section*{References}
\begin{itemize}
\item[] [1] K. Akutagawa and B. Botvinnik, Yamabe metrics on cylindrical manifolds, Geom. Funct. Anal. 13 (2003), 259-333, MR1982146, Zbl 1161.53344.
\item[] [2] K. Akutagawa, L. Florit, and J. Petean, On Yamabe constants of Riemannian products, Comm. Anal. Geom. 15 (2007), 947-969, MR2403191, Zbl 1147.53032.
\item[] [3] K. Akutagawa and A. Neves, 3-manifolds with Yamabe invariant greater than that of $\mathbb{R P}^{3}$, J. Differential Geom. 75 (2007), 359-386, MR2301449, Zbl 1119.53027.
\item[] [4] B. Ammann, M. Dahl, and E. Humbert, Surgery and the spinorial $\tau$-invariant, Comm. Part. Diff. Eq., 34 (2009), 1147-1179, MR2581968, Zbl 1183.53041.
\item[] [5] \_\_\_\_, The conformal Yamabe constant of product manifolds, Proc. AMS 141 (2013), 295-307, http://arxiv.org/abs/1103.1826
\item[] [6] \_\_\_\_, Square-integrability of solutions of the Yamabe equation, Preprint, 2011, http://arxiv.org/abs/1111.2780
\item[] [7] \_\_\_\_, Low-dimensional surgery and the Yamabe invariant, Preprint, 2012, http://arxiv.org/abs/1204.1197.
\item[] [8] B. Ammann, J. F. Grosjean, E. Humbert, and B. Morel, A spinorial analogue of Aubin's inequality, Math. Z. 260 (2008), 127-151, MR2413347, Zbl 1145.53039.
\item[] [9] M. T. Anderson, Canonical metrics on 3-manifolds and 4-manifolds, Asian J. Math. 10 (2006), 127-163, MR2213687, Zbl pre05170984.
\item[] [10] T. Aubin, Équations différentielles non linéaires et problème de Yamabe concernant la courbure scalaire., J. Math. Pur. Appl., IX. Ser. 55 (1976), 269-296, MR0431287, Zbl 0336.53033.
\item[] [11] C. Bär, P. Gauduchon, and A. Moroianu, Generalized cylinders in semiriemannian and spin geometry, Math. Z. 249 (2005), 545-580, MR2121740, Zbl 1068.53030.
\item[] [12] B. Botvinnik and J. Rosenberg, The Yamabe invariant for non-simply connected manifolds, J. Differential Geom. 62 (2002), 175-208, MR1988502, Zbl 1071.53021.
\item[] [13] H. L. Bray and A. Neves, Classification of prime 3-manifolds with Yamabe invariant greater than $\mathbb{R P}^{3}$, Ann. of Math. (2) 159 (2004), 407-424, MR2081443, Zbl 1066.53077.
\end{itemize}
\begin{itemize}
\item[] [14] J. Cheeger, Finiteness theorems for Riemannian manifolds, Amer. J. Math. 92 (1970), 61-74, MR0263092, Zbl 0194.52902.
\item[] [15] P. Chruściel, J. Isenberg, and D. Pollack, Initial data engineering, Comm. Math. Phys. 257 (2005), 29-42, MR2163567, Zbl 1080.83002.
\item[] [16] J. Corvino, M. Eichmair, and P. Miao, Deformation of scalar curvature and volume, Preprint, 2012.
\item[] [17] L. C. Evans, Weak convergence methods for nonlinear partial differential equations, CBMS Regional Conference Series in Mathematics, vol. 74, AMS, 1990, MR1034481, Zbl 0698.35004.
\item[] [18] D. Gilbarg and N. Trudinger, Elliptic partial differential equations of second order, Grundlehren der mathematischen Wissenschaften, no. 224, Springer-Verlag, 1977, MR0473443, Zbl 0361.35003.
\item[] [19] M. Gromov, Structures métriques pour les variétés Riemanniennes, CEDIC, Paris, 1981, MR0682063, Zbl 0509.53034.
\item[] [20] \_\_\_\_, Metric structures for Riemannian and non-Riemannian spaces, Birkhäuser Boston Inc., Boston, MA, 1999, MR1699320, Zbl 0953.53002.
\item[] [21] M. Gromov and H. B. Lawson, The classification of simply connected manifolds of positive scalar curvature, Ann. of Math. (2) 111 (1980), 423-434, MR0577131, Zbl 0463.53025.
\item[] [22] N. Große, The Yamabe equation on manifolds of bounded geometry, Preprint, 2009, http://arxiv.org/abs/0912.4398v2.
\item[] [23] M. J. Gursky and C. LeBrun, Yamabe invariants and Spin ${ }^{c}$ structures, Geom. Funct. Anal. 8 (1998), 965-977, MR1664788, Zbl 0931.53019.
\item[] [24] B. Hanke, Positive scalar curvature with symmetry, J. Reine Angew. Math. 614 (2008), 73-115, MR2376283, Zbl 1144.53048.
\item[] [25] E. Hebey, Sobolev spaces on Riemannian manifolds, Lecture Notes in Mathematics, vol. 1635, Berlin: Springer, 1996, MR1481970, Zbl 0866.58068.
\item[] [26] \_\_\_\_, Introduction à l'analyse non-linéaire sur les variétés, Diderot Editeur, Arts et Sciences, out of print, no longer sold, 1997.
\item[] [27] E. Hebey and M. Vaugon, Le problème de Yamabe équivariant, Bull. Sci. Math. 117 (1993), 241-286, MR1216009, Zbl 0786.53024.
\item[] [28] D. Joyce, Constant scalar curvature metrics on connected sums, Int. J. Math. Math. Sci. (2003), 405-450, MR1961016, Zbl 1026.53019.
\item[] [29] S. Kim, An obstruction to the conformal compactification of Riemannian manifolds, Proc. Amer. Math. Soc. 128 (2000), 1833-1838, MR1646195, Zbl 0956.53032.
\item[] [30] B. Kleiner and J. Lott, Notes on Perelman's papers, Geom. Topol. 12 (2008), no. 5, 2587-2855.
\item[] [31] O. Kobayashi, On large scalar curvature, research report 11, Dept. Math. Keio Univ., 1985.
\item[] [32] \_\_\_\_, Scalar curvature of a metric with unit volume, Math. Ann. 279 (1987), 253-265, MR0919505, Zbl 0611.53037.
\item[] [33] A. A. Kosinski, Differential manifolds, Pure and Applied Mathematics, vol. 138, Academic Press Inc., Boston, MA, 1993, MR1190010, Zbl 0767.57001.
\item[] [34] C. LeBrun, Four-manifolds without Einstein metrics, Math. Res. Lett. 3 (1996), 133-147, MR1386835, Zbl 0856.53035.
\item[] [35] \_\_\_\_, Einstein metrics and the Yamabe problem, Trends in mathematical physics (Knoxville, TN, 1998), AMS/IP Stud. Adv. Math., vol. 13, Amer. Math. Soc., Providence, RI, 1999, pp. 353-376, MR1708770, Zbl 1050.53032.
\item[] [36] \_\_\_\_, Kodaira dimension and the Yamabe problem, Comm. Anal. Geom. 7 (1999), 133-156, MR1674105, Zbl 0996.32009.
\end{itemize}
\begin{itemize}
\item[] [37] \_\_\_\_, Einstein metrics, complex surfaces, and symplectic 4-manifolds, Einstein metrics, complex surfaces, and symplectic 4-manifolds, Math. Proc. Cambridge Philos. Soc. 147, (2009), 1-8, MR2507306, Zbl 1175.57014.
\item[] [38] J. M. Lee and T. H. Parker, The Yamabe problem, Bull. Am. Math. Soc., New Ser. 17 (1987), 37-91, MR0888880, Zbl 0633.53062.
\item[] [39] F. Madani, Equivariant Yamabe problem and Hebey-Vaugon conjecture, J. Func. Anal. 258 (2010), 241-254, MR2557961, Zbl 1180.53041.
\item[] [40] F. Madani, Hebey-Vaugon conjecture II, C. R. Math. Acad. Sci. Paris 350 (2012), no. 17-18, 849-852.
\item[] [41] R. Mazzeo, D. Pollack, and K. Uhlenbeck, Connected sum constructions for constant scalar curvature metrics, Topol. Methods Nonlinear Anal. 6 (1995), 207-233, MR1399537, Zbl 0866.58069.
\item[] [42] L. Mazzieri, Generalized connected sum construction for nonzero constant scalar curvature metrics, Comm. Part. Diff. Eq. 33 (2008), 1-17, MR2398217, Zbl 1156.53021.
\item[] [43] \_\_\_\_, Generalized connected sum construction for scalar flat metrics, Manuscripta Math. 129 (2009), 137-168, MR2505799, Zbl 1230.53034.
\item[] [44] J. Petean, The Yamabe invariant of simply connected manifolds, J. Reine Angew. Math. 523 (2000), 225-231, MR1762961, Zbl 0949.53026.
\item[] [45] J. Petean and G. Yun, Surgery and the Yamabe invariant, Geom. Funct. Anal. 9 (1999), 1189-1199, MR1736933, Zbl 0976.53045.
\item[] [46] P. Petersen, Convergence theorems in Riemannian geometry, Comparison geometry (Berkeley, CA, 1993-94), Math. Sci. Res. Inst. Publ., vol. 30, Cambridge Univ. Press, Cambridge, 1997, pp. 167-202, MR1452874, Zbl 0898.53035.
\item[] [47] J. Rosenberg, S. Stolz, Metrics of positive scalar curvature and connections with surgery, Surveys on surgery theory, Vol. 2, 353-386, Ann. of Math. Stud., 149, Princeton Univ. Press, Princeton, NJ, 2001, MR1818778, Zbl 0971.57003.
\item[] [48] R. Schoen, Conformal deformation of a Riemannian metric to constant scalar curvature, J. Diff. Geom. 20 (1984), 479-495, MR0788292, Zbl 0576.53028.
\item[] [49] \_\_\_\_, Recent progress in geometric partial differential equations, Proceedings of the International Congress of Mathematicians, Vol. 1, 2 (Berkeley, Calif., 1986) (Providence, RI), Amer. Math. Soc., 1987, pp. 121-130, MR0934219, Zbl 0692.35046.
\item[] [50] \_\_\_\_, Variational theory for the total scalar curvature functional for Riemannian metrics and related topics, Topics in calculus of variations, Lect. 2nd Sess., Montecatini/Italy 1987, Lect. Notes Math. 1365, pp. 120-154, 1989, MR0994021, Zbl 0702.49038.
\item[] [51] R. Schoen and S.-T. Yau, On the structure of manifolds with positive scalar curvature, Manuscripta Math. 28 (1979), 159-183, MR0535700, Zbl 0423.53032.
\item[] [52] \_\_\_\_, Conformally flat manifolds, Kleinian groups and scalar curvature., Invent. Math. 92 (1988), 47-71, MR0954421, Zbl 0658.53038.
\item[] [53] \_\_\_\_, Lectures on differential geometry., Conference Proceedings and Lecture Notes in Geometry and Topology, International Press, 1994, MR1333601, Zbl 0830.53001.
\item[] [54] C. Sung, Surgery and equivariant Yamabe invariant, Differential Geom. Appl. 24 (2006), 271-287, MR2216941, Zbl 1099.53031.
\item[] [55] \_\_\_\_, Surgery, Yamabe invariant, and Seiberg-Witten theory, J. Geom. Phys. 59 (2009), 246-255, MR2492194, Zbl 1163.53023.
\item[] [56] N. S. Trudinger, Remarks concerning the conformal deformation of Riemannian structures on compact manifolds, Ann. Sc. Norm. Super. Pisa, Sci. Fis. Mat., III. Ser. 22 (1968), 265-274, MR0240748, Zbl 0159.23801.
\item[] [57] H. Yamabe, On a deformation of Riemannian structures on compact manifolds., Osaka Math. J. 12 (1960), 21-37, MR0125546, Zbl 0096.37201.
\end{itemize}

Fakultät für Mathematik, Universität Regensburg, 93040 Regensburg, Germany,
E-mail address: bernd.ammann@mathematik.uni-regensburg.de
Institutionen för Matematik, Kungliga Tekniska Högskolan, 10044 Stockholm, Sweden,
E-mail address: dahl@math.kth.se
Laboratoire de Mathématiques et Physique Théorique, Université de Tours, Parc de Grandmont, 37200 Tours, France,
E-mail address: Emmanuel.Humbert@lmpt.univ-tours.fr