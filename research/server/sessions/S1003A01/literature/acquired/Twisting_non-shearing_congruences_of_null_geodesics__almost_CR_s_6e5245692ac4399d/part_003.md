---
retention_scope: session
part: 3
total_parts: 3
---

[Part 3/3 of: Twisting non-shearing congruences of null geodesics, almost CR structures, and Einstein metrics in even dimensions]

The results presented in this article can easily be adapted to conformal structures of signature $(p+1, q+1)$ with both $p$ and $q$ even: here, the notion of almost Robinson structure is well-defined
since for these signatures, the existence of an almost null structure of real index one is possible - see [29]. The only point of caution is that since the screen bundle conformal structure is no longer positive definite, the norm of the twist of a congruence of null geodesics may be non-positive, in which case it cannot define an almost Robinson structure. In split signature $(m+1, m+1)$, one can define a totally real analogue of a twist-induced almost Robinson structure if the norm of the twist is negative. When both $p$ and $q$ are both greater than one, the twist endomorphism can be nilpotent, a property that allows yet another type of geometric structure. All these cases will be treated elsewhere. If the twist of a non-shearing congruence of null geodesics does induce an almost Robinson structure, the leaf space of the congruence inherits a partially integrable contact almost CR structure, this time, of signature $(p, q)$.

In odd dimensions, the geometry of non-shearing congruences of null geodesics is much more restrictive. The first point to note is that the leaf space is even-dimensional, which prohibits the existence of a contact structure there. Second, the algebraic constraint (5.1) forces the twist to be either identically zero or null, which restricts the possible metric signatures. Hence, in Lorentzian signature, odd dimensions, a non-shearing geodetic congruence with Weyl curvature prescription (1.1) must be non-twisting [49]. This is also true when $p<2$ or $q<2$. For other signatures, the situation is a little bit more delicate - again, this will be treated elsewhere.

\section*{A Computation of the curvature}

In this section, we compute the curvature tensors of the metric $g$ given in Section 5. The use of the open-source software cadabra [51, 52] was particularly helpful for that purpose. Not all components of the curvature tensors are given, but all may be obtained by means of complex conjugation and index manipulation. Parts of the first Bianchi identities are also given to bring out other forms of the components - the remaining, 'purely CR', parts being given by equations (4.3). We omit pullback maps for clarity.

\section*{A. 1 Riemann tensor}
$$\begin{aligned}
& R_{\gamma}{ }^{00}{ }_{\alpha}=0 \\
& R_{\bar{\gamma}}{ }^{00}{ }_{\alpha}=-\underline{h}_{\alpha \bar{\gamma}},
\end{aligned}$$
$$\begin{aligned}
R_{0}{ }^{00}{ }_{\alpha} & =\dot{E}_{\alpha}-\mathrm{i} E_{\alpha}, \\
R_{\beta \delta}{ }^{0}{ }_{\alpha} & =-2 \mathrm{i} \underline{\mathrm{~N}}_{\beta \delta \alpha} \\
R_{\beta \bar{\gamma}}{ }^{0}{ }_{\alpha} & =-2 \mathrm{i} E_{\alpha} \underline{h}_{\beta \bar{\gamma}}-\mathrm{i} E_{\beta} \underline{h}_{\alpha \bar{\gamma}},
\end{aligned}$$
$$\begin{aligned}
& R_{\gamma 0}{ }^{0}{ }_{\alpha}=-\underline{\nabla}_{\gamma} E_{\alpha}+\lambda_{\gamma} \dot{E}_{\alpha}+E_{\alpha} E_{\gamma}+E^{\beta} \underline{\mathrm{N}}_{\beta \alpha \gamma}-\frac{1}{2} \underline{\mathrm{i}}_{\alpha \gamma}-\mathrm{i} B_{\gamma \alpha}, \\
& R_{\bar{\beta} 0}{ }^{0}{ }_{\alpha}=-\underline{\nabla}_{\bar{\beta}} E_{\alpha}+\lambda_{\bar{\beta}} \dot{E}_{\alpha}+E_{\alpha} E_{\bar{\beta}}+\mathrm{i} E_{0} \underline{h}_{\alpha \bar{\beta}}-\mathrm{i} B_{\alpha \bar{\beta}}, \\
& R_{0}{ }^{00}{ }_{0}=\dot{E}_{0}-2 E_{\alpha} E^{\alpha}, \\
& R_{\gamma \delta \alpha \beta}=2 \underline{\nabla}_{[\gamma} \underline{\mathrm{N}}_{\alpha \beta \mid \delta]}, \\
& R_{\gamma \bar{\delta} \alpha \beta}=2 \mathrm{i} B_{\alpha \beta} \underline{h}_{\gamma \bar{\delta}}-2 \mathrm{i} B_{\gamma[\alpha} \underline{h}_{\beta] \bar{\delta}}-\underline{\nabla}_{\bar{\delta}} \underline{\mathrm{N}}_{\alpha \beta \gamma}+\mathrm{i} \underline{A}_{\gamma[\alpha} \underline{h}_{\beta] \bar{\delta}}, \\
& R_{\gamma \bar{\delta} \bar{\beta} \alpha}=\underline{R}_{\gamma \bar{\delta} \alpha \bar{\beta}}-2 \mathrm{i} B_{\alpha \bar{\beta}} \underline{h}_{\gamma \bar{\delta}}-2 \mathrm{i} B_{\gamma \bar{\delta}} \underline{h}_{\alpha \bar{\beta}}-\mathrm{i} B_{\gamma \bar{\beta}} \underline{h}_{\alpha \bar{\delta}}-\mathrm{i} B_{\alpha \bar{\delta}} \underline{h}_{\gamma \bar{\beta}}+\underline{\mathrm{N}}_{\epsilon \alpha \gamma} \underline{\mathrm{N}}_{\bar{\beta} \bar{\delta}},
\end{aligned}$$
$$\begin{aligned}
R_{0}^{0}{ }_{\alpha 0}= & \frac{1}{2} \underline{\nabla}_{0} E_{\alpha}-\frac{1}{2} \lambda_{0} \dot{E}_{\alpha}+E^{\beta} B_{\alpha \beta}+E_{\beta} B_{\alpha}{ }^{\beta}+\mathrm{i} C_{\alpha}-\dot{C}_{\alpha}, \\
R_{\gamma 0 \alpha \beta}= & \underline{\nabla}_{\gamma} B_{\alpha \beta}-\lambda_{\gamma} \dot{B}_{\alpha \beta}+2 B_{[\alpha}{ }^{\delta} \underline{N}_{\beta] \delta \gamma}+E_{[\alpha} \underline{A}_{\beta] \gamma}+2 E_{[\alpha} B_{\beta] \gamma}-\frac{1}{2} \underline{\nabla}_{0} \underline{N}_{\alpha \beta \gamma}, \\
R_{\beta \bar{\gamma} \alpha 0}= & -\underline{\nabla}_{\bar{\gamma}} B_{\alpha \beta}+\lambda_{\bar{\gamma}} \dot{B}_{\alpha \beta}+\underline{\nabla}_{\beta} B_{\alpha \bar{\gamma}}-\lambda_{\beta} \dot{B}_{\alpha \bar{\gamma}}-2 E_{\alpha} B_{\beta \bar{\gamma}}+E_{\beta} B_{\alpha \bar{\gamma}}-E_{\bar{\gamma}} B_{\alpha \beta} \\
& \quad+2 \mathrm{i} C_{\alpha} \underline{h}_{\beta \bar{\gamma}}-\frac{1}{2} E_{\bar{\gamma}} \underline{A}_{\alpha \beta}+B_{\bar{\gamma}}^{\delta} \underline{N}_{\delta \alpha \beta}-\frac{1}{2} \underline{\nabla}_{\bar{\gamma}} \underline{A}_{\alpha \beta}-\frac{1}{2} \underline{A}_{\bar{\gamma}}^{\delta} \underline{N}_{\delta \alpha \beta},
\end{aligned}$$
$$\begin{aligned}
R_{\beta 0 \alpha 0}=- & \frac{1}{2} \underline{\nabla}_{0} B_{\alpha \beta}+\frac{1}{2} \lambda_{0} \dot{B}_{\alpha \beta}+\underline{\nabla}_{\beta} C_{\alpha}-\lambda_{\beta} \dot{C}_{\alpha}-B_{\alpha}{ }^{\gamma} \underline{A}_{\beta \gamma}-E_{\alpha} C_{\beta}+B_{\alpha \gamma} B_{\beta}{ }^{\gamma} \\
& -C^{\gamma} \underline{N}_{\gamma \alpha \beta}+B_{\beta \gamma} B_{\alpha}{ }^{\gamma}+E_{\beta} C_{\alpha}-\frac{1}{2} E_{0} \underline{A}_{\alpha \beta}-E_{0} B_{\alpha \beta}-\frac{1}{4} \underline{\nabla}_{0} \underline{A}_{\alpha \beta}, \\
R_{\bar{\beta} 0 \alpha 0}=- & \frac{1}{2} \underline{\nabla}_{0} B_{\alpha \bar{\beta}}+\frac{1}{2} \lambda_{0} \dot{B}_{\alpha \bar{\beta}}+\underline{\nabla}_{\bar{\beta}} C_{\alpha}-\lambda_{\bar{\beta}} \dot{C}_{\alpha}-B_{\alpha \gamma} \underline{A}_{\bar{\beta}}^{\gamma} \\
& -E_{\alpha} C^{\beta}+B_{\alpha \gamma} B_{\bar{\beta}}^{\gamma}-B_{\alpha}^{\gamma} B_{\gamma \bar{\beta}}+E_{\bar{\beta}} C_{\alpha}-E_{0} B_{\alpha \bar{\beta}}-\frac{1}{4} \underline{A}_{\alpha \gamma} \underline{A}_{\bar{\beta}}^{\gamma} .
\end{aligned}$$

\section*{A. 2 The Ricci tensor}
$$\begin{aligned}
\operatorname{Ric}^{00} & =2 m, \\
\operatorname{Ric}_{\alpha}{ }^{0} & =\dot{E}_{\alpha}-4 \mathrm{i} E_{\alpha},
\end{aligned}$$
$$\begin{aligned}
& \operatorname{Ric}_{\alpha \beta}=2 \underline{\nabla}_{(\alpha} E_{\beta)}-2 \lambda_{(\alpha} \dot{E}_{\beta)}-2 E_{\alpha} E_{\beta}+\operatorname{im} \underline{A}_{\alpha \beta}+2 \underline{\nabla}^{\gamma} \underline{N}_{\gamma(\alpha \beta)}-2 \underline{N}_{\gamma(\alpha \beta)} E^{\gamma}, \\
& \operatorname{Ric}_{\alpha \bar{\beta}}=\underline{\nabla}_{\alpha} E_{\bar{\beta}}+\underline{\nabla}_{\bar{\beta}} E_{\alpha}-\lambda_{\alpha} \dot{E}_{\bar{\beta}}-\lambda_{\bar{\beta}} \dot{E}_{\alpha}-2 E_{\alpha} E_{\bar{\beta}}-4 \mathrm{i} B_{\alpha \bar{\beta}}+\underline{\operatorname{Ric}}_{\alpha \bar{\beta}}-\underline{\mathrm{N}}_{\alpha \delta \gamma} \underline{\mathrm{N}}_{\bar{\beta}}{ }^{\delta \gamma}, \\
& \operatorname{Ric}_{0}{ }^{0}=\underline{\nabla}_{\alpha} E^{\alpha}+\underline{\nabla}^{\alpha} E_{\alpha}-\lambda_{\alpha} \dot{E}^{\alpha}-\lambda^{\alpha} \dot{E}_{\alpha}-4 E_{\alpha} E^{\alpha}+2 \mathrm{i} B_{\alpha} \alpha+\dot{E}_{0},
\end{aligned}$$
$$\begin{gathered}
\operatorname{Ric}_{0 \beta}=\underline{\nabla}_{\beta} E_{0}-\frac{1}{2} \underline{\nabla}_{0} E_{\beta}-\lambda_{\beta} \dot{E}_{0}+\frac{1}{2} \lambda_{0} \dot{E}_{\beta}-\frac{1}{2} E^{\alpha} \underline{A}_{\beta \alpha}-2 E^{\alpha} B_{\alpha \beta}+2 E_{\alpha} B_{\beta}{ }^{\alpha} \\
-\mathrm{i} C_{\beta}+\underline{\nabla}^{\alpha} B_{\alpha \beta}-\lambda^{\alpha} \dot{B}_{\alpha \beta}-\underline{\nabla}_{\alpha} B_{\beta}{ }^{\alpha}+\lambda_{\alpha} \dot{B}_{\beta}{ }^{\alpha} \\
+\frac{1}{2} B^{\alpha \gamma} \underline{\mathrm{N}}_{\alpha \gamma \beta}+\frac{1}{2} \underline{\nabla}^{\alpha} \underline{A}_{\beta \alpha}+\frac{1}{2} \underline{A}^{\alpha \gamma} \underline{\mathrm{N}}_{\beta \alpha \gamma} \\
\operatorname{Ric}_{00}=\underline{\nabla}_{\alpha} C^{\alpha}+\underline{\nabla}^{\alpha} C_{\alpha}-\lambda_{\alpha} \dot{C}^{\alpha}-\lambda^{\alpha} \dot{C}_{\alpha}-\frac{1}{2} \underline{A}_{\alpha \beta} \underline{A}^{\alpha \beta}+2 B_{\alpha \beta} B^{\alpha \beta}-2 B_{\alpha}{ }^{\beta} B_{\beta}{ }^{\alpha}
\end{gathered}$$

\section*{A. 3 The Ricci scalar}
$$\begin{aligned}
\mathrm{Sc}=4 \underline{\nabla}_{\alpha} E^{\alpha}+4 \underline{\nabla}^{\alpha} E_{\alpha}-4 \lambda_{\alpha} \dot{E}^{\alpha}-4 \lambda^{\alpha} \dot{E}_{\alpha}-12 E_{\alpha} E^{\alpha} & \\
& +2 \dot{E}_{0}-4 \mathrm{i} B_{\alpha}{ }^{\alpha}+2 \underline{\mathrm{Sc}}-2 \underline{\mathrm{~N}}_{\alpha \beta \gamma} \underline{\mathrm{N}}^{\alpha \beta \gamma}
\end{aligned}$$

\section*{A. 4 The first Bianchi identities}
$$\begin{aligned}
0= & \dot{B}_{\alpha \beta}+2 \underline{\nabla}_{[\alpha} E_{\beta]}-2 \lambda_{[\alpha} \dot{E}_{\beta]}-\underline{\mathrm{N}}_{\alpha \beta \gamma} E^{\gamma}, \\
0= & \dot{B}_{\alpha \bar{\beta}}+\underline{\nabla}_{\alpha} E_{\bar{\beta}}-\underline{\nabla}_{\bar{\beta}} E_{\alpha}-\lambda_{\alpha} \dot{E}_{\bar{\beta}}+\lambda_{\bar{\beta}} \dot{E}_{\alpha}+\mathrm{i} E_{0} \underline{h}_{\alpha \bar{\beta}}, \\
0= & \dot{C}_{\alpha}+\underline{\nabla}_{\alpha} E_{0}-\underline{\nabla}_{0} E_{\alpha}-\lambda_{\alpha} \dot{E}_{0}+\lambda_{0} \dot{E}_{\alpha}-\underline{A}_{\beta \alpha} E^{\beta}, \\
0= & \underline{\nabla}_{[\alpha} B_{\beta \gamma]}-\lambda_{[\alpha} \dot{B}_{\beta \gamma]}+B_{[\alpha} \delta^{\delta} \underline{N}_{\beta \gamma] \delta}+2 E_{[\alpha} B_{\beta \gamma]}, \\
0= & 2 \underline{\nabla}_{[\alpha} B_{\beta] \bar{\gamma}}+\underline{\nabla}_{\bar{\gamma}} B_{\alpha \beta}-2 \lambda_{[\alpha} \dot{B}_{\beta] \bar{\gamma}}-\lambda_{\bar{\gamma}} \dot{B}_{\alpha \beta} \\
& \quad+4 E_{[\alpha} B_{\beta] \bar{\gamma}}+2 E_{\bar{\gamma}} B_{\alpha \beta}-2 \mathrm{i} C_{[\alpha} \underline{h}_{\beta] \bar{\gamma}}+\underline{\mathrm{N}}_{\alpha \beta \delta} B_{\bar{\gamma}}^{\delta}, \\
0= & \underline{\nabla}_{[\alpha} C_{\beta]}-\lambda_{[\alpha} \dot{C}_{\beta]}+\frac{1}{2} \underline{\nabla}_{0} B_{\alpha \beta}-\frac{1}{2} \lambda_{0} \dot{B}_{\alpha \beta} \\
& \quad+2 E_{[\alpha} C_{\beta]}+E_{0} B_{\alpha \beta}+B_{[\alpha}{ }^{\gamma} \underline{A}_{\beta] \gamma}-\frac{1}{2} \underline{\mathrm{~N}}_{\alpha \beta \gamma} C^{\gamma}, \\
0= & \underline{\nabla}_{\alpha} C_{\bar{\beta}}-\underline{\nabla}_{\bar{\beta}} C_{\alpha}-\lambda_{\alpha} \dot{C}_{\bar{\beta}}+\lambda_{\bar{\beta}} \dot{C}_{\alpha}+\underline{\nabla}_{0} B_{\alpha \bar{\beta}}-\lambda_{0} \dot{B}_{\alpha \bar{\beta}} \\
& \quad+2 E_{\alpha} C_{\bar{\beta}}-2 E_{\bar{\beta}} C_{\alpha}+2 E_{0} B_{\alpha \bar{\beta}}-B_{\bar{\beta}} \underline{A}_{\gamma \alpha}-\underline{A}_{\bar{\beta}} B_{\gamma \alpha} .
\end{aligned}$$

\section*{References}
\begin{itemize}
\item[] [1] D. V. Alekseevskiĭ. Quaternionic Riemannian spaces with transitive reductive or solvable group of motions. Funkcional. Anal. i Priložen., 4(4):68-69, 1970.
\item[] [2] D. V. Alekseevsky, M. Ganji, and G. Schmalz. CR-geometry and shearfree Lorentzian geometry. In Geometric complex analysis, volume 246 of Springer Proc. Math. Stat., pages 11-22. Springer, Singapore, 2018.
\item[] [3] D. V. Alekseevsky, M. Ganji, G. Schmalz, and A. Spiro. Lorentzian manifolds with shearfree congruences and Kähler-Sasaki geometry. Differential Geom. Appl., 75:101724, 2021.
\item[] [4] V. Apostolov, D. M. J. Calderbank, and P. Gauduchon. The geometry of weakly self-dual Kähler surfaces. Compositio Math., 135(3):279-322, 2003.
\item[] [5] V. Apostolov, T. Drăghici, and A. Moroianu. A splitting theorem for Kähler manifolds whose Ricci tensors have constant eigenvalues. Internat. J. Math., 12(7):769-789, 2001.
\item[] [6] J. Armstrong. An ansatz for almost-Kähler, Einstein 4-manifolds. J. Reine Angew. Math., 542:53-84, 2002.
\item[] [7] A. M. Awad and A. Chamblin. A bestiary of higher-dimensional Taub-NUT-AdS spacetimes. Classical Quantum Gravity, 19(8):2051-2061, 2002.
\item[] [8] T. N. Bailey, M. G. Eastwood, and A. R. Gover. Thomas's structure bundle for conformal, projective and related structures. Rocky Mountain J. Math., 24(4):1191-1217, 1994.
\item[] [9] F. A. Bais and P. Batenburg. A new class of higher-dimensional Kaluza-Klein monopole and instanton solutions. Nuclear Phys. B, 253(1):162-172, 1985.
\item[] [10] A. L. Besse. Einstein manifolds, volume 10 of Ergebnisse der Mathematik und ihrer Grenzgebiete (3) [Results in Mathematics and Related Areas (3)]. Springer-Verlag, Berlin, 1987.
\end{itemize}
\begin{itemize}
\item[] [11] A. Čap and A. R. Gover. CR-tractors and the Fefferman space. Indiana Univ. Math. J., 57(5):2519-2570, 2008.
\item[] [12] A. Čap and A. R. Gover. A holonomy characterisation of Fefferman spaces. Ann. Global Anal. Geom., 38(4):399-412, 2010.
\item[] [13] E. Cartan. Sur les espaces conformes généralisés et l'univers optique. C. R. Acad. Sci., Paris, 174:857-860, 1922.
\item[] [14] J. S. Case and A. R. Gover. The $P^{\prime}$-operator, the $Q^{\prime}$-curvature, and the CR tractor calculus. Ann. Sc. Norm. Super. Pisa Cl. Sci. (5), 20(2):565-618, 2020.
\item[] [15] C. L. Fefferman. Correction to: "Monge-Ampère equations, the Bergman kernel, and geometry of pseudoconvex domains" (Ann. of Math. (2) 103 (1976), no. 2, 395-416). Ann. of Math. (2), 104(2):393-394, 1976.
\item[] [16] C. L. Fefferman. Monge-Ampère equations, the Bergman kernel, and geometry of pseudoconvex domains. Ann. of Math. (2), 103(2):395-416, 1976.
\item[] [17] A. Fino, T. Leistner, and A. Taghavi-Chabert. Optical geometries. arXiv:2009.10012 preprint, 2020.
\item[] [18] A. Fino, T. Leistner, and A. Taghavi-Chabert. Almost Robinson geometries. arXiv:2102.05634 preprint, 2021.
\item[] [19] J. N. Goldberg and R. K. Sachs. A theorem on Petrov types. Acta Phys. Polon., 22(suppl, suppl):13-23, 1962.
\item[] [20] J. N. Goldberg and R. K. Sachs. Republication of: A theorem on petrov types. General Relativity and Gravitation, 41:433-444, 2009. 10.1007/s10714-008-0722-5.
\item[] [21] S. I. Goldberg. Integrability of almost Kaehler manifolds. Proc. Amer. Math. Soc., 21:96-100, 1969.
\item[] [22] A. R. Gover. Almost conformally Einstein manifolds and obstructions. In Differential geometry and its applications, pages 247-260. Matfyzpress, Prague, 2005.
\item[] [23] A. R. Gover and C. R. Graham. CR invariant powers of the sub-Laplacian. J. Reine Angew. Math., 583:1-27, 2005.
\item[] [24] C. R. Graham. On Sparling's characterization of Fefferman metrics. Amer. J. Math., 109(5):853-874, 1987.
\item[] [25] A. Gray and L. M. Hervella. The sixteen classes of almost Hermitian manifolds and their linear invariants. Ann. Mat. Pura Appl. (4), 123:35-58, 1980.
\item[] [26] C. D. Hill, J. Lewandowski, and P. Nurowski. Einstein's equations and the embedding of 3-dimensional CR manifolds. Indiana Univ. Math. J., 57(7):3131-3176, 2008.
\item[] [27] L. P. Hughston and L. J. Mason. A generalised Kerr-Robinson theorem. Classical Quantum Gravity, 5(2):275-285, 1988.
\end{itemize}
\begin{itemize}
\item[] [28] R. P. Kerr. Gravitational field of a spinning mass as an example of algebraically special metrics. Phys. Rev. Lett., 11:237-238, 1963.
\item[] [29] W. Kopczyński and A. Trautman. Simple spinors and real structures. J. Math. Phys., 33(2):550-559, 1992.
\item[] [30] W. Kundt. The plane-fronted gravitational waves. Z. Physik, 163:77-86, 1961.
\item[] [31] J. M. Lee. The Fefferman metric and pseudo-Hermitian invariants. Trans. Amer. Math. Soc., 296(1):411-429, 1986.
\item[] [32] J. M. Lee. Pseudo-Einstein structures on CR manifolds. Amer. J. Math., 110(1):157-178, 1988.
\item[] [33] F. Leitner. On transversally symmetric pseudo-Einstein and Fefferman-Einstein spaces. Math. $Z ., 256(2): 443-459,2007$.
\item[] [34] F. Leitner. A gauged Fefferman construction for partially integrable CR geometry. J. Geom. Phys., 60(9):1262-1278, 2010.
\item[] [35] J. Lewandowski. On the Fefferman class of metrics associated with a three-dimensional CR space. Lett. Math. Phys., 15(2):129-135, 1988.
\item[] [36] J. Lewandowski. Twistor equation in a curved space-time. Class. Quant. Grav., 8:L11-L18, 1991.
\item[] [37] J. Lewandowski and P. Nurowski. Algebraically special twisting gravitational fields and CR structures. Classical Quantum Gravity, 7(3):309-328, 1990.
\item[] [38] J. Lewandowski, P. Nurowski, and J. Tafel. Einstein's equations and realizability of CR manifolds. Classical Quantum Gravity, 7(11):L241-L246, 1990.
\item[] [39] L. Mason and A. Taghavi-Chabert. Killing-Yano tensors and multi-Hermitian structures. Journal of Geometry and Physics, 60:907-923, June 2010.
\item[] [40] Y. Matsumoto. GJMS operators, $Q$-curvature, and obstruction tensor of partially integrable CR manifolds. Differential Geom. Appl., 45:78-114, 2016.
\item[] [41] R. Milson, A. Coley, V. Pravda, and A. Pravdová. Alignment and algebraically special tensors in Lorentzian geometry. Int. J. Geom. Methods Mod. Phys., 2(1):41-61, 2005.
\item[] [42] E. Newman, L. Tamburino, and T. Unti. Empty-space generalization of the Schwarzschild metric. J. Mathematical Phys., 4:915-923, 1963.
\item[] [43] P. Nurowski. Einstein Equations and Cauchy-Riemann Geometry. PhD thesis, Scuola Internazionale Superiore di Studi Avanzati, 1993.
\item[] [44] P. Nurowski. Optical geometries and related structures. J. Geom. Phys., 18(4):335-348, 1996.
\item[] [45] P. Nurowski. Twistor bundles, Einstein equations and real structures. Class. Quant. Grav., 14:A261-A290, 1997.
\end{itemize}
[46] P. Nurowski and M. Przanowski. A four-dimensional example of a Ricci flat metric admitting almost-Kähler non-Kähler structure. Classical Quantum Gravity, 16(3):L9-L13, 1999.
[47] P. Nurowski and A. Trautman. Robinson manifolds as the Lorentzian analogs of Hermite manifolds. Differential Geom. Appl., 17(2-3):175-195, 2002. 8th International Conference on Differential Geometry and its Applications (Opava, 2001).
[48] M. Ortaggio. Bel-Debever criteria for the classification of the Weyl tensor in higher dimensions. Classical Quantum Gravity, 26(19):195015, 8, 2009.
[49] M. Ortaggio, V. Pravda, and A. Pravdova. Ricci identities in higher dimensions. Class. Quant. Grav., 24:1657-1664, 2007.
[50] M. Ortaggio, V. Pravda, and A. Pravdova. Algebraic classification of higher dimensional spacetimes based on null alignment. Class. Quant. Grav., 30:013001, 2013.
[51] K. Peeters. Introducing Cadabra: A symbolic computer algebra system for field theory problems. 2007.
[52] K. Peeters. Cadabra2: computer algebra for field theory revisited. Journal of Open Source Software, 3(32):1118, 2018.
[53] R. Penrose. Twistor algebra. J. Math. Phys., 8:345-366, 1967.
[54] R. Penrose and W. Rindler. Spinors and space-time. Vol. 2. Cambridge Monographs on Mathematical Physics. Cambridge University Press, Cambridge, 1986. Spinor and twistor methods in space-time geometry.
[55] A. Z. Petrov. Classification of spaces defining gravitational fields. Kazan. Gos. Univ. Uč. Zap., 114(8):55-69, 1954.
[56] I. Robinson. Null electromagnetic fields. J. Mathematical Phys., 2:290-291, 1961.
[57] I. Robinson and A. Trautman. Some spherical gravitational waves in general relativity. Proc. Roy. Soc. London Ser. A, 265:463-473, 1961/62.
[58] I. Robinson and A. Trautman. Conformal geometry of flows in $n$ dimensions. J. Math. Phys., 24(6):1425-1429, 1983.
[59] I. Robinson and A. Trautman. Integrable optical geometry. Letters in Mathematical Physics, 10:179-182, 1985.
[60] I. Robinson and A. Trautman. Cauchy-Riemann structures in optical geometry. In Proceedings of the fourth Marcel Grossmann meeting on general relativity, Part A, B (Rome, 1985), pages 317-324. North-Holland, Amsterdam, 1986.
[61] I. Robinson and A. Trautman. Optical geometry. In P. S. Ajduk, Z. and T. A., editors, New Theories in Physics, Proc. of the XI Warsaw Symp. on Elementary Particle Physics, Kazimierz 23-27 May 1988, pages 454-497. World Scientific, 1989.
[62] G. Schmalz and M. Ganji. A criterion for local embeddability of three-dimensional CR structures. Ann. Mat. Pura Appl. (4), 198(2):491-503, 2019.
\begin{itemize}
\item[] [63] K. Sekigawa. On some compact Einstein almost Kähler manifolds. J. Math. Soc. Japan, 39(4):677-684, 1987.
\item[] [64] J. Tafel. On the Robinson theorem and shearfree geodesic null congruences. Lett. Math. Phys., 10(1):33-39, 1985.
\item[] [65] A. Taghavi-Chabert. A characterisation of Fefferman spaces for almost CR geometry. In preparation.
\item[] [66] A. Taghavi-Chabert. The complex Goldberg-Sachs theorem in higher dimensions. J. Geom. Phys., 62(5):981-1012, 2012.
\item[] [67] A. Taghavi-Chabert. The curvature of almost Robinson manifolds. arXiv:1404.5810 preprint, 2014.
\item[] [68] A. Taghavi-Chabert. Pure spinors, intrinsic torsion and curvature in even dimensions. Differential Geometry and its Applications, 46:164-203, 2016.
\item[] [69] N. Tanaka. A differential geometric study on strongly pseudo-convex manifolds. Kinokuniya Book-Store Co., Ltd., Tokyo, 1975. Lectures in Mathematics, Department of Mathematics, Kyoto University, No. 9.
\item[] [70] A. H. Taub. Empty space-times admitting a three parameter group of motions. Ann. of Math. (2), 53:472-490, 1951.
\item[] [71] A. Trautman. Deformations of the Hodge map and optical geometry. J. Geom. Phys., 1(2):85-95, 1984.
\item[] [72] A. Trautman. Optical structures in relativistic theories. Number Numéro Hors Série, pages 401-420. 1985. The mathematical heritage of Élie Cartan (Lyon, 1984).
\item[] [73] A. Trautman. Gauge and optical aspects of gravitation. Classical Quantum Gravity, 16(12A):A157-A175, 1999.
\item[] [74] A. Trautman. Robinson manifolds and Cauchy-Riemann spaces. Classical Quantum Gravity, 19(2):R1-R10, 2002.
\item[] [75] A. Trautman. Robinson manifolds and the shear-free condition. In Proceedings of the Conference on General Relativity, Cosmology and Relativistic Astrophysics (Journées Relativistes) (Dublin, 2001), volume 17, pages 2735-2737, 2002.
\item[] [76] S. M. Webster. Pseudo-Hermitian structures on a real hypersurface. J. Differential Geometry, 13(1):25-41, 1978.
\end{itemize}