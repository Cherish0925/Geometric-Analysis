---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Mass and rigidity in almost Kähler geometry]

Since $\tau>\frac{2}{3}(n-4)$, we have $2 \tau+4>n$. Hence the quantity in the right hand side of the equality in equation (16) is in $L^{1}$. Moreover as $r \longrightarrow \infty$, we also have
$$\begin{aligned}
\left\langle\rho^{*}, \nabla^{\mathrm{LC}} \omega\right\rangle & =O\left(\left|R \| \nabla^{\mathrm{LC}} \omega\right|\right)=O\left(r^{-\left(\frac{3 \tau}{2}+3\right)}\right) \\
d\left|\nabla^{\mathrm{LC}} \omega\right|^{2} & =O\left(\left|\left(\nabla^{\mathrm{LC}}\right)^{2} \omega \| \nabla^{\mathrm{LC}} \omega\right|\right)=O\left(r^{-\left(\eta+\frac{\tau}{2}+1\right)}\right)
\end{aligned}$$
Since $\eta \geq \frac{2}{3}(n-1)$ and $\tau>\frac{2}{3}(n-4)$, we have $\left(\eta+\frac{\tau}{2}+1\right),\left(\frac{3 \tau}{2}+3\right)>n-1$. Thereafter the following boundary integral vanish.
$$\int_{M}\left(8 \delta\left\langle\rho^{*}, \nabla^{\mathrm{LC}} \omega\right\rangle-\Delta\left|\nabla^{\mathrm{LC}} \omega\right|^{2}\right) d \mathrm{v}_{g}=\lim _{r \rightarrow \infty} \int_{S_{r} / \Gamma}\left(8\left\langle\rho^{*}, \nabla^{\mathrm{LC}} \omega\right\rangle-d\left|\nabla^{\mathrm{LC}} \omega\right|^{2}\right) d \mathrm{v}_{S_{r} / \Gamma}=0$$
Now integrating (16) over $M$ we obtain the theorem. \(\square\)

Next we discuss the proof of theorem 1.14. The proof is essentially due to LeBrun [18]. We compensate the non-compactness of the manifold with suitable decay properties of the curvature. Below we provide a brief outline of the proof, emphasizing where the decay assumptions enter. Before we delve into the details, we state a lemma gathering all the algebraic facts needed to prove the theorem.

Lemma 4.2 (LeBrun [18]). On an almost Kähler 4-manifold $(M, g, J)$, we have the following identities.
$$\begin{array}{r}
\frac{1}{2}\left|\nabla^{\mathrm{LC}} \omega\right|^{2}=W_{+}(\omega, \omega)-\frac{s}{3} \\
\left\langle W_{+},\left(\nabla^{\mathrm{LC}}\right)^{*} \nabla^{\mathrm{LC}}(\omega \otimes \omega)\right\rangle d \mathrm{v}_{g}=\left(W_{+}(\omega, \omega)\right)^{2}+4\left|W_{+}(\omega)\right|^{2}-s W_{+}(\omega, \omega) d \mathrm{v}_{g} \\
4\left|W_{+}\right|^{2}-4\left|W_{+}(\omega)\right|^{2}+\frac{1}{2}\left(W_{+}(\omega, \omega)\right)^{2} \geq 0
\end{array}$$
Moreover if $\delta W_{+}=0$, we have
$$0=\left(\nabla^{\mathrm{LC}}\right)^{*} \nabla^{\mathrm{LC}} W_{+}+\frac{s}{2} W_{+}-6 W_{+} \circ W_{+}+2\left|W_{+}\right|^{2} \mathrm{Id}$$

Proof. See § 2 of [18]. \(\square\)

Proof of theorem 1.14. Notice as $r \longrightarrow \infty$,
$$\begin{aligned}
\left|W_{+}\right| & =O\left(r^{-(2+\tau)}\right) \\
\left|\nabla^{\mathrm{LC}} W_{+}\right| & =O\left(r^{-(3+\tau)}\right) \\
s & =O\left(r^{-(2+\tau)}\right) \\
\left|\nabla^{\mathrm{LC}} \omega\right|^{2} & =O\left(r^{-(2+\tau)}\right)
\end{aligned}$$
We have used equation (17) for the asymptotics of $\nabla^{\mathrm{LC}} \omega$. Notice since $\tau>0$, all the terms $\left|W_{+}\right|^{2}, s W_{+},\left|\nabla^{\mathrm{LC}} \omega\right|^{4}, s\left|\nabla^{\mathrm{LC}} \omega\right|^{2}, s^{2} \in L^{1}$.

Equation (20) gives us
$$\left.0=\left.\int_{M}\left\langle\left(\nabla^{\mathrm{LC}}\right)^{*} \nabla^{\mathrm{LC}} W_{+}+\frac{s}{2} W_{+}-6 W_{+} \circ W_{+}+2\right| W_{+}\right|^{2} \mathrm{Id}, \omega \otimes \omega\right\rangle d \mathrm{v}_{g}$$

We focus on the first term of the integrand. Integrating by parts we get
$$\int_{M}\left\langle\left(\nabla^{\mathrm{LC}}\right)^{*} \nabla^{\mathrm{LC}} W_{+}, \omega \otimes \omega\right\rangle d \mathrm{v}_{g}=\int_{M}\left\langle\nabla^{\mathrm{LC}} W_{+}, \nabla^{\mathrm{LC}}(\omega \otimes \omega)\right\rangle d \mathrm{v}_{g}+\text { a boundary term }$$
As $r \longrightarrow \infty$,
$$\left|\nabla^{\mathrm{LC}} W_{+} \| \omega \otimes \omega\right|=O\left(r^{-(3+\tau)}\right)$$
Since $\tau>0,(3+\tau)>3$, the boundary term vanishes and we have
$$\int_{M}\left\langle\left(\nabla^{\mathrm{LC}}\right)^{*} \nabla^{\mathrm{LC}} W_{+}, \omega \otimes \omega\right\rangle d \mathrm{v}_{g}=\int_{M}\left\langle\nabla^{\mathrm{LC}} W_{+}, \nabla^{\mathrm{LC}}(\omega \otimes \omega)\right\rangle d \mathrm{v}_{g}$$
Integrating by parts again we get
$$\int_{M}\left\langle\nabla^{\mathrm{LC}} W_{+}, \nabla^{\mathrm{LC}}(\omega \otimes \omega)\right\rangle d \mathrm{v}_{g}=\int_{M}\left\langle W_{+},\left(\nabla^{\mathrm{LC}}\right)^{*} \nabla^{\mathrm{LC}}(\omega \otimes \omega)\right\rangle d \mathrm{v}_{g}+\text { a boundary term }$$
Again we see that as $r \longrightarrow \infty$,
$$\left|W_{+} \| \nabla^{\mathrm{LC}}(\omega \otimes \omega)\right|=O\left(\left|W_{+} \| \nabla^{\mathrm{LC}} \omega\right|\right)=O\left(r^{-\left(3+\frac{3 \tau}{2}\right)}\right)$$
Since $\tau>0,3+\frac{3 \tau}{2}>0$, the boundary term vanishes again. Therefore equation (21) can be written as
$$0=\int_{M}\left(\left\langle W_{+},\left(\nabla^{\mathrm{LC}}\right)^{*} \nabla^{\mathrm{LC}}(\omega \otimes \omega)\right\rangle+\frac{s}{2} W_{+}(\omega, \omega)-6\left|W_{+}(\omega)\right|^{2}+2\left|W_{+}\right|^{2}|\omega|^{2}\right) d v_{g}$$
Substituting the identity (18) for $\left\langle W_{+},\left(\nabla^{\mathrm{LC}}\right)^{*} \nabla^{\mathrm{LC}}(\omega \otimes \omega)\right\rangle$ into equation (22) yields
$$0=\int_{M}\left(\left(W_{+}(\omega, \omega)\right)^{2}-\frac{s}{2} W_{+}(\omega, \omega)-2\left|W_{+}(\omega)\right|^{2}+4\left|W_{+}\right|^{2}\right) d \mathrm{v}_{g}$$
Combining the above equation (23) with the inequality (19) we have
$$\int_{M} s W_{+}(\omega, \omega) d \mathrm{v}_{g} \geq \int_{M}\left(4\left|W_{+}\right|^{2}+\frac{3}{2}\left(W_{+}(\omega, \omega)\right)^{2}\right) d \mathrm{v}_{g}$$
which also reads
$$\frac{3}{8} \int_{M}\left(\frac{2 s}{3}-W_{+}(\omega, \omega)\right) W_{+}(\omega, \omega) d \mathrm{v}_{g} \geq \int_{M}\left|W_{+}\right|^{2} d \mathrm{v}_{g}$$
Substituting $W_{+}(\omega, \omega)=\frac{1}{2}\left|\nabla^{\mathrm{LC}} \omega\right|^{2}+\frac{s}{3}$ from (17) into the above equation we get
$$\frac{3}{8} \int_{M}\left(\frac{s}{3}-\frac{1}{2}\left|\nabla^{\mathrm{LC}} \omega\right|^{2}\right)\left(\frac{s}{3}+\frac{1}{2}\left|\nabla^{\mathrm{LC}} \omega\right|^{2}\right) d \mathrm{v}_{g} \geq \int_{M}\left|W_{+}\right|^{2} d \mathrm{v}_{g}$$

An algebraic simplification yields
$$\int_{M} \frac{s^{2}}{24} d \mathrm{v}_{g}-\frac{3}{32} \int_{M}\left|\nabla^{\mathrm{LC}} \omega\right|^{4} d \mathrm{v}_{g} \geq \int_{M}\left|W_{+}\right|^{2} d \mathrm{v}_{g}$$
On the other hand using the fact that $W_{+}$is trace-free and $|\omega|^{2} \equiv 2$, we have
$$2 \sqrt{\frac{2}{3}}\left|W_{+}\right| \geq W_{+}(\omega, \omega)$$
Combining it with the identity (17) yields
$$\left|W_{+}\right| \geq \frac{s}{2 \sqrt{6}}$$
Since $s \geq 0$, squaring and then integrating both sides we get
$$\int_{M}\left|W_{+}\right|^{2} d \mathrm{v}_{g} \geq \int_{M} \frac{s^{2}}{24} d \mathrm{v}_{g}$$
(24) and (25) together proves that $\nabla^{\mathrm{LC}} J \equiv 0$. \(\square\)

Remark 2. To prove the analogous statements for ALF, one needs to make sure again that under certain decay assumptions, the boundary terms do not contribute whenever we do any integration by parts. An $n+1$-dimensional ALF manifold of order $\tau>0$ has the following asymptotics for the curvature tensor: $|R|=O\left(r^{-(2+\tau)}\right)$ as $r \rightarrow \infty$. This is exactly like the ALE case except now $r$ represents the radius in $\mathbb{R}^{n}$ and not in $\mathbb{R}^{n+1}$ as in the ALE case; but that is okay, because the volume of a boundary hypersurface in an $n+1$-dimensional ALF space grows as $r^{n-1}$, one power less than the $n+1$-dimensional ALE case. Thereafter, all the same calculations go through the same.

\section*{Bibliography}
\begin{itemize}
\item[] [1] Vestislav Apostolov and Tedi Drăghici. "The curvature and the integrability of almost-Kähler manifolds: a survey." English. In: Symplectic and contact topology: Interactions and perspectives. Papers of the workshop on symplectic and contact topology, quantum cohomology, and symplectic field theory, Montreal and Toronto, Canada, March-April 2001. Providence, RI: American Mathematical Society (AMS), 2003, pp. 25-53. ISBN: 0-8218-3162-3 (cit. on p. 22).
\item[] [2] Vestislav Apostolov, Tedi Drăghici, and Andrei Moroianu. "A splitting theorem for Kähler manifolds whose Ricci tensors have constant eigenvalues." English. In: Int. J. Math. 12.7 (2001), pp. 769-789. ISSN: 0129-167X. doi: 10.1142/ S0129167X01001052 (cit. on p. 22).
\item[] [3] John Armstrong. "An ansatz for almost-Kähler, Einstein 4-manifolds". English. In: J. Reine Angew. Math. 542 (2002), pp. 53-84. issn: 0075-4102. doi: 10. 1515/crll. 2002.009 (cit. on p. 6).
\item[] [4] R. Arnowitt, S. Deser, and C. W. Misner. "Energy and the criteria for radiation in general relativity". English. In: Phys. Rev., II. Ser. 118 (1960), pp. 1100-1104. ISSN: 0031-899X. DOI: 10.1103/PhysRev.118.1100. URL: resolver.caltech. edu/CaltechAUTHORS:20180724-143009319 (cit. on p. 2).
\end{itemize}
\begin{itemize}
\item[] [5] Shigetoshi Bando, Atsushi Kasue, and Hiraku Nakajima. "On a construction of coordinates at infinity on manifolds with fast curvature decay and maximal volume growth". English. In: Invent. Math. 97.2 (1989), pp. 313-349. ISSN: 0020-9910. DOI: 10.1007/BF01389045. URL: https://eudml.org/doc/143705 (cit. on pp. 1, 6, 7).
\item[] [6] Robert Bartnik. "The mass of an asymptotically flat manifold". English. In: Commun. Pure Appl. Math. 39 (1986), pp. 661-693. issn: 0010-3640. doi: 10. 1002/cpa. 3160390505 (cit. on pp. 3, 13, 15).
\item[] [7] David E. Blair. Riemannian geometry of contact and symplectic manifolds. English. Vol. 203. Prog. Math. Boston, MA: Birkhäuser, 2002. isbn: 0-8176-4261-7 (cit. on p. 12).
\item[] [8] David E. Blair. "The "total scalar curvature" as a symplectic invariant and related results". English. In: Proceedings of the 3rd congress on geometry, Thessaloniki, Greece, May 26-June 1st, 1991. Thessaloniki (Greece): Aristoteles University, Department of Mathematics, Section of Geometry, 1992, pp. 79-83 (cit. on pp. 4, 8, 12, 16).
\item[] [9] Piotr Chruściel. Boundary conditions at spatial infinity from a Hamiltonian point of view. English. Topological properties and global structure of space-time, Proc. NATO/ASI, Erice/Italy 1985, NATO ASI Ser., Ser. B 138, 49-59 (1986). 1986 (cit. on pp. 3, 13).
\item[] [10] Mattias Dahl. "The positive mass theorem for ALE manifolds". English. In: Mathematics of gravitation. Part I: Lorentzian geometry and Einstein equations. Proceedings of the workshop on mathematical aspects of theories of gravitation, Warsaw, Poland, February 29-March 30, 1996. Warsaw: Polish Academy of Sciences, Inst. of Mathematics, 1997, pp. 133-142 (cit. on p. 4).
\item[] [11] Thomas Friedrich. Dirac operators in Riemannian geometry. Transl. from the German by Andreas Nestke. English. Vol. 25. Grad. Stud. Math. Providence, RI: American Mathematical Society (AMS), 2000. isbn: 0-8218-2055-9 (cit. on p. 13).
\item[] [12] Paul Gauduchon. "Hermitian connections and Dirac operators". English. In: Boll. Unione Mat. Ital., VII. Ser., B 11.2 (1997), pp. 257-288. ISSN: 0392-4041 (cit. on p. 10).
\item[] [13] S. I. Goldberg. "Integrability of almost Kaehler manifolds". English. In: Proc. Am. Math. Soc. 21 (1969), pp. 96-100. ISSN: 0002-9939. doi: 10.2307/2036867 (cit. on p. 6).
\item[] [14] Hans-Joachim Hein and Claude LeBrun. "Mass in Kähler geometry". English. In: Commun. Math. Phys. 347.1 (2016), pp. 183-221. ISSN: 0010-3616. doi: 10. 1007/s00220-016-2661-4 (cit. on pp. 1-4, 19).
\item[] [15] P. B. Kronheimer. "A Torelli-type theorem for gravitational instantons". English. In: J. Differ. Geom. 29.3 (1989), pp. 685-697. issn: 0022-040X. doi: 10. 4310/jdg/1214443067 (cit. on p. 6).
\item[] [16] P. B. Kronheimer. "The construction of ALE spaces as hyper-Kähler quotients". English. In: J. Differ. Geom. 29.3 (1989), pp. 665-683. issn: 0022-040X. doi: 10.4310/jdg/1214443066 (cit. on p. 6).
\item[] [17] Claude LeBrun. "Counter-examples to the generalized positive action conjecture". English. In: Commun. Math. Phys. 118.4 (1988), pp. 591-596. ISSN: 0010-3616. doi: 10.1007/BF01221110 (cit. on pp. 4, 6).
\item[] [18] Claude LeBrun. "Curvature in the balance: the Weyl functional and scalar curvature of 4-manifolds". English. In: Pure Appl. Math. Q. 19.6 (2023), pp. 2737-2763. ISSN: 1558-8599. DOI: 10.4310/PAMQ. 2023. v19.n6.a5 (cit. on pp. 6, 23).
\end{itemize}
\begin{itemize}
\item[] [19] Claude LeBrun. "Mass, Kähler manifolds, and symplectic geometry". English. In: Ann. Global Anal. Geom. 56.1 (2019), pp. 97-112. ISSN: 0232-704X. doi: 10.1007/s10455-019-09658-9 (cit. on pp. 2-4, 17-21).
\item[] [20] Claude Lebrun. "Einstein metrics, symplectic minimality, and pseudo-holomorphic curves". English. In: Ann. Global Anal. Geom. 28.2 (2005), pp. 157-177. ISSN: 0232-704X. DOI: 10.1007/s10455-005-3892-5 (cit. on p. 12).
\item[] [21] Tian-Jun Li and Ai-Ko Liu. "The equivalence between $S W$ and $G r$ in the case where $b^{+}=1$ ". English. In: Int. Math. Res. Not. 1999.7 (1999), pp. 335-345. ISSN: 1073-7928. DOI: 10.1155/S1073792899000173 (cit. on p. 21).
\item[] [22] Michael T. Lock and Jeff A. Viaclovsky. "A smörgåsbord of scalar-flat Kähler ALE surfaces". English. In: J. Reine Angew. Math. 746 (2019), pp. 171-208. issn: 0075-4102. doi: 10.1515/crelle-2016-0007 (cit. on p. 6).
\item[] [23] Dusa McDuff. "The structure of rational and ruled symplectic 4-manifolds". English. In: J. Am. Math. Soc. 3.3 (1990), pp. 679-712. issn: 0894-0347. doi: 10.2307/1990934 (cit. on pp. 7, 20).
\item[] [24] Hiraku Nakajima. Self-duality of ALE Ricci-flat 4-manifolds and positive mass theorem. English. Recent topics in differential and analytic geometry, Adv. Stud. Pure Math. 18-I, 385-396 (1990). 1990 (cit. on pp. 4, 7).
\item[] [25] Liviu I. Nicolaescu. Lectures on the geometry of manifolds. English. 2nd ed. Singapore: World Scientific, 2007. isbn: 978-981-270-853-3; 978-981-277-862-8 (cit. on p. 11).
\item[] [26] Hiroshi Ohta and Kaoru Ono. "Simple singularities and symplectic fillings". English. In: J. Differ. Geom. 69.1 (2005), pp. 1-42. issn: 0022-040X. doi: 10. 4310/jdg/1121540338 (cit. on p. 7).
\item[] [27] Hiroshi Ohta and Kaoru Ono. "Simple singularities and topology of symplectically filling 4-manifold". English. In: Comment. Math. Helv. 74.4 (1999), pp. 575-590. ISSN: 0010-2571. DOI: 10.1007/s000140050106 (cit. on p. 7).
\item[] [28] Richard Schoen and Shing-Tung Yau. "On the proof of the positive mass conjecture in general relativity". English. In: Commun. Math. Phys. 65 (1979), pp. 45-76. ISSN: 0010-3616. DOI: 10.1007/BF01940959 (cit. on p. 2).
\item[] [29] Richard Schoen and Shing-Tung Yau. "Proof of the positive mass theorem. II". English. In: Commun. Math. Phys. 79 (1981), pp. 231-260. ISSN: 0010-3616. doi: 10.1007/BF01942062 (cit. on p. 2).
\item[] [30] Kouei Sekigawa. "On some 4-dimensional compact Einstein almost Kähler manifolds". English. In: Math. Ann. 271 (1985), pp. 333-337. iSSN: 0025-5831. doi: 10.1007/BF01456071. URL: https://eudml.org/doc/163971 (cit. on p. 6).
\item[] [31] Kouei Sekigawa. "On some compact Einstein almost Kähler manifolds". English. In: J. Math. Soc. Japan 39 (1987), pp. 677-684. ISSN: 0025-5645. doi: 10.2969/ jmsj/03940677 (cit. on pp. 6, 21, 22).
\item[] [32] Ioana Şuvaina. "ALE Ricci-flat Kähler metrics and deformations of quotient surface singularities". English. In: Ann. Global Anal. Geom. 41.1 (2012), pp. 109-123. ISSN: 0232-704X. DOI: 10.1007/s10455-011-9273-1 (cit. on p. 6).
\item[] [33] Clifford Henry Taubes. Seiberg-Witten and Gromov invariants for symplectic 4-manifolds. Vol. 2. Edited by Richard Wentworth. English. Ed. by Richard Wentworth. 2nd ed. Vol. 2. First Int. Press Lect. Ser. Somerville, MA: International Press, 2005. isbn: 1-57146-089-6 (cit. on pp. 20, 21).
\item[] [34] Clifford Henry Taubes. "The Seiberg-Witten invariants and symplectic forms". English. In: Math. Res. Lett. 1.6 (1994), pp. 809-822. ISSN: 1073-2780. doi: 10.4310/MRL.1994.v1.n6.a15 (cit. on p. 11).
\end{itemize}
[35] Edward Witten. "A new proof of the positive energy theorem." English. In: Commun. Math. Phys. 80 (1981), pp. 381-402. ISSN: 0010-3616. DOI: 10.1007/ BF01208277 (cit. on p. 2).
[36] Evan P. Wright. "Quotients of gravitational instantons". English. In: Ann. Global Anal. Geom. 41.1 (2012), pp. 91-108. ISSN: 0232-704X. DOI: 10.1007/s10455-011-9272-2 (cit. on p. 6).

Sorbonne Université, Université Paris Cité, CNRS, IMJ-PRG, F-75005 Paris, France
E-mail address: Partha.Ghosh@imj-prg.fr