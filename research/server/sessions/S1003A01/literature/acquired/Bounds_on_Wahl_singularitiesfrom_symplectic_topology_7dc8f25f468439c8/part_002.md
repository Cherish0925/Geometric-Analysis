---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Bounds on Wahl singularitiesfrom symplectic topology]

Proposition 8.4. - Let $E$ be a bad curve of type (B1), maximal with respect to nesting. Suppose that $E$ contains $n$ internal spheres. Then
$$n \leq \frac{1}{2}(\ell+4) .$$
The same inequality holds for bad curves of type (B2). If there are simultaneously bad curves $E_{1}$ of type (B1) and $E_{2}$ of type (B2) containing $n_{1}$, respectively $n_{2}$, internal spheres, then
$$n_{1}+n_{2} \leq \frac{1}{2}(\ell+5) .$$
Proof. - When we consider only bad curves of type (B1), the argument is very similar to the arguments used in type (A): there are three cases:
\begin{itemize}
\item[(B1.] 1) $1=x^{\prime}$,
\item[(B1.] 2) $1<x^{\prime}<x$,
\end{itemize}
In cases (B1.1) and (B1.3), the internal spheres form a chain of -2-spheres of length $n_{1}$. In case (B1.1), this implies that
$$n_{1} \leq K \cdot C_{y^{\prime}} \text { and } n_{1} \leq K \cdot C_{\ell} .$$
Since $y^{\prime} \neq \ell$ by Theorem 5.5(2), we find that
$$n_{1} \leq \frac{1}{2} K \cdot\left(C_{y^{\prime}}+C_{\ell}\right) \leq \frac{1}{2}(\ell+1) .$$
In case (B1.3), assuming $x+1 \neq \ell$, we get
$$n_{1}-1 \leq K \cdot C_{x+1} \text { and } n_{1} \leq K \cdot C_{\ell},$$
so
$$n_{1} \leq \frac{1}{2}(\ell+2) .$$
If $x+1=\ell$ then we necessarily have $y^{\prime}=x+1$, so $e$ intersects $C_{x+1}$. When we blow down $e$, we find
$$\pi_{1}\left(C_{\ell-1}\right) \cdot \pi_{1}\left(C_{\ell}\right)=2,$$
so
$$K \cdot \Pi_{n_{1}+1}\left(C_{x+1}\right)=K \cdot C_{x+1}-1-2 n_{1} \geq-1,$$
which implies
$$n_{1} \leq \frac{1}{2} K \cdot C_{x+1} \leq \frac{1}{2}(\ell+1) .$$
In case (B1.2), blowing down $e$ results in a configuration with $S=\pi_{1}\left(C_{y^{\prime}}\right)$ to which we can apply Lemma 2.17 and deduce
$$n_{1} \leq \frac{1}{2}\left(K \cdot C_{y^{\prime}}+2\right) \leq \frac{1}{2}(\ell+3) .$$
It remains to understand what happens when we have a maximal (B1) curve $E_{1}$ and a maximal (B2) curve $E_{2}$. Let $e_{1}$ and $e_{2}$ be the -1-spheres in $E_{1}$ and $E_{2}$; we know that $E_{1}$ and $E_{2}$ do not share any components, so $e_{1} \neq e_{2}$ and there is no overlap between
the internal spheres of $E_{1}$ and of $E_{2}$. Let $C_{x_{1}^{\prime}}, C_{y_{1}^{\prime}}$ be the spheres intersected by $e_{1}$ and $C_{x_{2}^{\prime}}, C_{y_{2}^{\prime}}$ be the spheres intersected by $e_{2}$. Let $C_{1}, \ldots, C_{x}$ be the chain of internal spheres for $E_{1}$ and $C_{y}, \ldots, C_{\ell}$ be the chain of internal spheres for $E_{2}$. We know that $e_{1}$ does not intersect any of $C_{y}, \ldots, C_{\ell}$ or else we would find a positive intersection between two exceptional classes, in contradiction to Lemma 2.5.

Note that T-strings cannot both start and end with 2, so if $E_{1}$ is of type (B1.1) or (B1.3) then $E_{2}$ is of type (B2.2). Up to symmetry (switching the roles of $E_{1}$ and $E_{2}$ ) we can therefore assume that $E_{2}$ has type (B2.2).

We now proceed according to the type of $E_{1}$ :
\begin{itemize}
\item[(B1.] 1) In this case, we need to distinguish between the subcases $C_{y_{1}^{\prime}} \neq C_{x_{2}^{\prime}}$ and $C_{y_{1}^{\prime}}=$ $C_{x_{2}^{\prime}}$. In the first case we get
$$n_{1} \leq \frac{1}{2} K \cdot\left(C_{y_{1}^{\prime}}+C_{\ell}\right) \text { and } n_{2} \leq \frac{1}{2}\left(K \cdot C_{x_{2}^{\prime}}+3\right),$$
so
$$n_{1}+n_{2} \leq \frac{1}{2}\left(K \cdot\left(C_{x_{2}^{\prime}}+C_{y_{1}^{\prime}}+C_{\ell}\right)+3\right) \leq \frac{1}{2}(\ell+4) .$$
In the second case, we can blow down $E_{1}$ and get
$$K \cdot \Pi_{n_{1}+1}\left(C_{y_{1}^{\prime}}\right) \leq K \cdot C_{y_{1}^{\prime}}-n_{1}-1 .$$
Moreover, we know that $n_{1} \leq K \cdot C_{\ell}$. Subsequently blowing down $E_{2}$ yields
$$\begin{aligned}
n_{1}+n_{2} & \leq n_{1}+\frac{1}{2}\left(K \cdot \Pi_{n_{1}+1}\left(C_{y_{1}^{\prime}}\right)+3\right) \\
& \leq \frac{1}{2}\left(K \cdot C_{y_{1}^{\prime}}+n_{1}-1+3\right) \\
& \leq \frac{1}{2}\left(K \cdot\left(C_{y_{1}^{\prime}}+C_{\ell}\right)+2\right) \\
& \leq \frac{1}{2}(\ell+3) .
\end{aligned}$$
\item[(B1.] 2) In this case, we need to distinguish between the subcases $C_{y_{1}^{\prime}} \neq C_{x_{2}^{\prime}}$ and $C_{y_{1}^{\prime}}=$ $C_{x_{2}^{\prime}}$. In the first case we get
$$n_{1}+n_{2} \leq \frac{1}{2}\left(K \cdot\left(C_{y_{1}^{\prime}}+C_{x_{2}^{\prime}}\right)+4\right) \leq \frac{1}{2}(\ell+5) .$$
In the second case, we first blow down $E_{1}$ and look at the blow-down of $S=$ $C_{y_{1}^{\prime}}$. Arguing as in Lemma 2.17, we see that at the end of the blowing down process, the resulting rational curve $S^{\prime}$ has
$$K \cdot S^{\prime} \leq K \cdot S-1-2\left(n_{1}-1\right) \text {. }$$
We now blow down $e_{2}$ and apply Lemma 2.17 to the blow-down of $S^{\prime}$. This gives
$$n_{2} \leq \frac{1}{2}\left(K \cdot S-1-2\left(n_{1}-1\right)+3\right),$$
\end{itemize}
\begin{itemize}
\item[] or
$$n_{1}+n_{2} \leq \frac{1}{2}\left(K \cdot C_{y_{1}^{\prime}}+4\right) \leq \frac{1}{2}(\ell+5) .$$
\item[(B1.] 3) In this case, we need to distinguish between the subcases $C_{x_{1}} \neq C_{x_{2}^{\prime}}$ and $C_{x_{1}}=$ $C_{x_{2}^{\prime}}$. In the first case, we get
$$n_{1} \leq K \cdot C_{x_{1}+1}+1, n_{1} \leq K \cdot C_{\ell}, n_{2} \leq \frac{1}{2}\left(K \cdot C_{y_{1}^{\prime}}+3\right),$$
so
$$n_{1}+n_{2} \leq \frac{1}{2}\left(K \cdot\left(C_{x_{1}+1}+C_{\ell}+C_{y_{1}^{\prime}}\right)+4\right) \leq \frac{1}{2}(\ell+5) .$$
In the second case, we have again $n_{1} \leq K \cdot C_{\ell}$. Blow-down $E_{1}$, and look at the blow down $S$ of $C_{x_{1}+1}$ along $E_{1}$. We have $K \cdot S \leq K \cdot C_{x_{1}+1}-n_{1}$. Let $S^{\prime}$ be the blow-down of $S$ along $e_{2}$; we have $K \cdot S^{\prime} \leq K \cdot C_{x_{1}+1}-n_{1}-1$, and can apply Lemma 2.17 to get
$$n_{2} \leq \frac{1}{2}\left(K \cdot S^{\prime}+3\right) \leq \frac{1}{2}\left(K \cdot C_{x_{1}+1}-n_{1}+2\right),$$
so, overall,
$$n_{1}+n_{2} \leq \frac{1}{2}\left(K \cdot\left(C_{x_{1}+1}+C_{\ell}\right)+2\right) \leq \frac{1}{2}(\ell+3) .$$ \(\square\)
\end{itemize}

Theorem 8.5. - We have $\ell \leq 4 K_{X}^{2}+7$.
Proof. - By Lemma 7.3, if there are $p$ bad curves, then
$$\ell \leq 2 K_{X}^{2}+p+1 .$$
We have seen in Propositions 8.3 and 8.4 that
$$p \leq \frac{1}{2}(\ell+5),$$
so
$$\ell \leq 4 K_{X}^{2}+7,$$
as required. \(\square\)

\section*{9. Special case}

If we assume more about the form of the T-string then we get stronger bounds.
Lemma 9.1. - Let $X$ be a symplectic 4-manifold with $b^{+}(X)>1$ and suppose that $X$ contains a chain of -2-spheres $C_{1}, \ldots, C_{n}$ where $C_{i}$ intersects $C_{i-1}$ and $C_{i+1}$ each once transversely and none of the other spheres in the chain. If $e$ is a -1 -sphere in $X$ then $e$ cannot intersect $C_{2} \ldots, C_{n-1}$.

Proof. - Suppose $e$ intersects $C_{i}$ for $i \in\{2, \ldots, n-1\}$. If we blow down $e$ then $C_{i}$ becomes a rational curve $C_{i}^{\prime}$ with $K \cdot C_{i}^{\prime}=-e \cdot C_{i}$, so by Corollary 2.2 $e \cdot C_{i}=1$ and $C_{i}^{\prime}$ is an embedded -1-sphere. Blowing down $C_{i}^{\prime}$ creates two new -1-spheres $C_{i-1}^{\prime \prime}$ and $C_{i+1}^{\prime \prime}$, and blowing down one of these turns the other into a sphere with self-intersection zero, in contradiction to Corollary 2.2 \(\square\)

Theorem 9.2. - For Wahl singularities whose $T$-string is $[2, \ldots, 2, \ell+1]$, there are no bad curves at all, so
$$\ell \leq 2 K_{X}^{2}+1 .$$
Proof. - Suppose there is a bad curve $E$ containing a -1-sphere $e$. The sphere $e$ intersects two of the components in the chain. By Lemma 9.1, $e$ can only intersect $C_{1}, C_{\ell-1}$ or $C_{\ell}$. It cannot intersect both $C_{1}$ and $C_{\ell}$ by Theorem 5.5(2) and it cannot intersect both $C_{1}$ and $C_{\ell-1}$ or else, upon blowing down, we create a sphere with self-intersection zero. Therefore the only possibility is that $e$ intersects $C_{\ell-1}$ and $C_{\ell}$. Blowing down $e, C_{\ell-1}, C_{\ell-2}, \ldots, C_{1}$ in that order, the curve $C_{\ell}$ becomes a rational curve $C_{\ell}^{\prime}$ with
$$K \cdot C_{\ell}^{\prime}=K \cdot C_{\ell}-2-2(\ell-1),$$
(it decreases by one after blowing down $e$, and then intersects $C_{\ell-1}$ with multiplicity 2, so it intersects all $\ell-1$ of the subsequent -1-spheres with multiplicity 2). Since $K \cdot C_{\ell}=\ell-1$, this gives
$$K \cdot C_{\ell}^{\prime} \leq-1-\ell<-1,$$
in contradiction to Corollary 2.2. \(\square\)

\section*{References}
\begin{itemize}
\item[] [1] V. Alexeev. Boundedness and $K^{2}$ for log surfaces. Internat. J. Math., 5(6):779-810, 1994.
\item[] [2] S. F. Barber and O. Zariski. Reducible Exceptional Curves of the First Kind. Amer. J. Math., 57(1):119-141, 1935.
\item[] [3] W. P. Barth, K. Hulek, C. A. M. Peters, and A. Van de Ven. Compact complex surfaces, volume 4 of Ergebnisse der Mathematik und ihrer Grenzgebiete. 3. Folge. A Series of Modern Surveys in Mathematics [Results in Mathematics and Related Areas. 3rd Series. A Series of Modern Surveys in Mathematics]. Springer-Verlag, Berlin, second edition, 2004.
\item[] [4] H. Chen and W. Zhang. Kodaira dimensions of almost complex manifolds. arXiv:1808.00885, 2018.
\item[] [5] J. D. Evans and I. Smith. Markov numbers and Lagrangian cell complexes in the complex projective plane. Geom. Topol., 22(2):1143-1180, 2018.
\item[] [6] J.D. Evans and G. Urzúa. Antiflips, mutations, and unbounded symplectic embeddings of rational homology balls. arXiv:1807.06073, 2018.
\item[] [7] R. Fintushel and R. J. Stern. Immersed spheres in 4-manifolds and the immersed Thom conjecture. Turkish J. Math., 19(2):145-157, 1995.
\end{itemize}
\begin{itemize}
\item[] [8] R. Fintushel and R. J. Stern. Rational blowdowns of smooth 4-manifolds. J. Differential Geom., 46(2):181-235, 1997.
\item[] [9] R. Fintushel and R. J. Stern. Knots, links, and 4-manifolds. Invent. Math., 134(2):363-400, 1998.
\item[] [10] R. Fintushel and R. J. Stern. Double node neighborhoods and families of simply connected 4-manifolds with $b^{+}=1$. J. Amer. Math. Soc., 19(1):171-180, 2006.
\item[] [11] P. Hacking. Compact moduli spaces of surfaces of general type. In Compact moduli spaces and vector bundles, volume 564 of Contemp. Math., pages 1-18. Amer. Math. Soc., Providence, RI, 2012.
\item[] [12] P. Hacking, J. Tevelev, and G. Urzúa. Flipping surfaces. J. Algebraic Geom., 26(2):279-345, 2017.
\item[] [13] Y. Kawamata. Moderate degenerations of algebraic surfaces. In Complex algebraic varieties (Bayreuth, 1990), volume 1507 of Lecture Notes in Math., pages 113-132. Springer, Berlin, 1992.
\item[] [14] T. Khodorovskiy. Bounds on embedding rational homology balls in symplectic 4-manifolds. arXiv:1307.4321, 2013.
\item[] [15] T. Khodorovskiy. Symplectic rational blow-up. arXiv:1303.2581, 2013.
\item[] [16] T. Khodorovskiy. Smooth embeddings of rational homology balls. Topology Appl., 161:386-396, 2014.
\item[] [17] Y. Lee. Numerical bounds for degenerations of surfaces of general type. Internat. J. Math., 10(1):79-92, 1999.
\item[] [18] Y. Lee and J. Park. A simply connected surface of general type with $p_{g}=0$ and $K^{2}=2$. Invent. Math., 170(3):483-505, 2007.
\item[] [19] Y. Lee and J. Park. A construction of Horikawa surface via $\mathbb{Q}$-Gorenstein smoothings. Math. Z., 267(1-2):15-25, 2011.
\item[] [20] Y. Lekili and M. Maydanskiy. The symplectic topology of some rational homology balls. Comment. Math. Helv., 89(3):571-596, 2014.
\item[] [21] T.-J. Li and A.-K. Liu. Uniqueness of symplectic canonical class, surface cone and symplectic cone of 4-manifolds with $B^{+}=1$. J. Differential Geom., 58(2):331-370, 2001.
\item[] [22] T.-J. Li and W. Zhang. J-holomorphic curves in a nef class. Int. Math. Res. Not. IMRN, (22):12070-12104, 2015.
\item[] [23] A.-K. Liu. Some new applications of general wall crossing formula, Gompf's conjecture and its applications. Math. Res. Lett., 3(5):569-585, 1996.
\item[] [24] D. McDuff. The structure of rational and ruled symplectic 4-manifolds. J. Amer. Math. Soc., 3(3):679-712, 1990.
\item[] [25] D. McDuff. The local behaviour of holomorphic curves in almost complex 4-manifolds. J. Differential Geom., 34(1):143-164, 1991.
\end{itemize}
\begin{itemize}
\item[] [26] D. McDuff. Immersed spheres in symplectic 4-manifolds. Ann. Inst. Fourier (Grenoble), 42(1-2):369-392, 1992.
\item[] [27] D. McDuff. Singularities and positivity of intersections of $J$-holomorphic curves. In Holomorphic curves in symplectic geometry, volume 117 of Progr. Math., pages 191-215. Birkhäuser, Basel, 1994. With an appendix by Gang Liu.
\item[] [28] D. McDuff and E. Opshtein. Nongeneric $J$-holomorphic curves and singular inflation. Algebr. Geom. Topol., 15(1):231-286, 2015.
\item[] [29] D. McDuff and D. Salamon. J-holomorphic curves and symplectic topology, volume 52 of American Mathematical Society Colloquium Publications. American Mathematical Society, Providence, RI, 2004.
\item[] [30] M. McLean. Reeb orbits and the minimal discrepancy of an isolated singularity. Invent. Math., 204(2):505-594, 2016.
\item[] [31] H. Park, J. Park, and D. Shin. Smoothly embedded rational homology balls. J. Korean Math. Soc., 53(6):1293-1308, 2016.
\item[] [32] J. Park. Simply connected symplectic 4-manifolds with $b_{2}^{+}=1$ and $c_{1}^{2}=2$. Invent. Math., 159(3):657-667, 2005.
\item[] [33] J. Rana. A boundary divisor in the moduli spaces of stable quintic surfaces. Internat. J. Math., 28(4):1750021, 61, 2017.
\item[] [34] J. Rana and G. Urzúa. Optimal bounds for T-singularities in stable surfaces. arXiv:1708.02278, 2017.
\item[] [35] J.-C. Sikorav. Singularities of $J$-holomorphic curves. Math. Z., 226(3):359-373, 1997.
\item[] [36] I. Smith, R. P. Thomas, and S.-T. Yau. Symplectic conifold transitions. J. Differential Geom., 62(2):209-242, 2002.
\item[] [37] A. Stern and G. Urzúa. KSBA surfaces with elliptic quotient singularities, $\pi_{1}=1, p_{g}=0$, and $K^{2}=1,2$. Israel J. Math., 214(2):651-673, 2016.
\item[] [38] M. Symington. Symplectic rational blowdowns. J. Differential Geom., 50(3):505-518, 1998.
\item[] [39] M. Symington. Generalized symplectic rational blowdowns. Algebr. Geom. Topol., 1:503-518, 2001.
\item[] [40] C. H. Taubes. The Seiberg-Witten invariants and symplectic forms. Math. Res. Lett., 1(6):809-822, 1994.
\item[] [41] C. H. Taubes. The Seiberg-Witten and Gromov invariants. Math. Res. Lett., 2(2):221-238, 1995.
\item[] [42] C. H. Taubes. SW ⇒ Gr: from the Seiberg-Witten equations to pseudo-holomorphic curves. J. Amer. Math. Soc., 9(3):845-918, 1996.
\item[] [43] M. Usher and D. Thurston. Open problems in geometric topology. In M. Usher, editor, Low-dimensional and symplectic topology, Proceedings of Symposia in Pure Mathematics, pages 215-228. American Mathematical Society, 2011.
\end{itemize}
[44] J. Wahl. Smoothings of normal surface singularities. Topology, 20(3):219-246, 1981.
[45] E. Witten. Monopoles and four-manifolds. Math. Res. Lett., 1(6):769-796, 1994.
[46] W. Zhang. Moduli space of $J$-holomorphic subvarieties. arXiv:1601.07855, 2016.
[47] W. Zhang. The curve cone of almost complex 4-manifolds. Proc. Lond. Math. Soc. (3), 115(6):1227-1275, 2017.

\footnotetext{
Jonathan David Evans, Department of Mathematics, University College London, Gower Street, London, WC1E 6BT, United Kingdom • E-mail : j.d.evans@ucl.ac.uk

Ivan Smith, Centre for Mathematical Sciences, University of Cambridge, Wilberforce Road, CB3 0WB, United Kingdom. • E-mail : is200@cam.ac.uk
}