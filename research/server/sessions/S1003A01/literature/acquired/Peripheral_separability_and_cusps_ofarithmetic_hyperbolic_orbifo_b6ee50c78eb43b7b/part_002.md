---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Peripheral separability and cusps ofarithmetic hyperbolic orbifolds]

We extend this to $\Gamma$ by declaring
$$\varphi_{j}(\alpha)=\left(z_{1}, t_{1}, \eta_{1}\right), \quad \varphi_{j}(\beta)=\left(z_{2}, t_{2}, \eta_{2}\right),$$
where $z_{1}, z_{2} \in \mathbf{C}, t_{1}, t_{2} \in \mathbf{R}$, and $\eta_{1}, \eta_{2} \in\langle\mathrm{U}(1), \iota\rangle$.
To solve Equation (1), we simply use the presentations above to ensure that this yields a homomorphism. By applying Lemma 7.2 (b), one can see that these solutions yield injective homomorphisms. For clarity, we solve the equations for the second family (2) and give a list of the equations and solutions for the seventh family (7). We relegate the rest of the solutions to the appendix.
The second family has presentation
$$\left\langle a, b, c, \alpha:[b, a]=c^{k},[c, a]=[c, b]=[c, \alpha]=1, \alpha a=a^{-1} \alpha, \alpha b=b^{-1} \alpha, \alpha^{2}=c\right\rangle$$
with $k \in 2 \mathbb{N}$. For this family we take the map $\varphi_{4}$. First, consider the relation $[b, a]=c^{k}$. Then
$$\begin{aligned}
{\left[\varphi_{4}(b), \varphi_{4}(a)\right] } & =[(i, 0,1),(1,0,1)] \\
& =(i+1,2 \operatorname{Im}\langle i, 1\rangle, 1)(-i-1,2 \operatorname{Im}\langle-i,-1\rangle, 1) \\
& =(0,4,1)
\end{aligned}$$
Since $\left[\varphi_{4}(b), \varphi_{4}(b)\right]=\varphi_{4}(c)^{k}$, it follows that $\varphi_{4}(c)=(0,4 / k, 1)$.
Next, consider the relation $\alpha^{2}=c$. We have
$$\begin{aligned}
\left(z_{1}, t_{1}, \eta_{1}\right)\left(z_{1}, t_{1}, \eta_{1}\right) & =\left(z_{1}+\eta_{1} z_{1}, 2 t_{1}+2 \operatorname{Im}\left\langle z_{1}, \eta_{1} z_{1}\right\rangle, \eta_{1}^{2}\right) \\
& =(0,4 / k, 1)
\end{aligned}$$
In particular, $\eta_{1}^{2}=1$. If $\eta_{1}=1$, then the above injection would yield an isomorphism between a group in the first family with a group in the second family. This is impossible, therefore $\eta_{1}=-1$. By considering the first coordinate equation with $\eta_{1}=-1$, we get no information. The second coordinate equation is $2 t_{1}=4 / k$, therefore $t_{1}=2 / k$. One can now check that $[c, \alpha]=1$, regardless of $z_{1}$.

Now, we take the relation $\alpha a=a^{-1} \alpha$. We have
$$\left(z_{1}, 2 / k,-1\right)(1,0,1)=\left(z_{1}-1,2 / k-2 \operatorname{Im} z_{1},-1\right) .$$
On the other hand,
$$(-1,0,1)\left(z_{1}, 2 / k,-1\right)=\left(-1+z_{1}, 2 / k+2 \operatorname{Im} z_{1},-1\right) .$$
The first and last coordinate equations yield no information, while the second coordinate equation yields $4 \operatorname{Im} z_{1}=0$. Hence $\operatorname{Im} z_{1}=0$.

Lastly, we have the relation $\alpha b=b^{-1} \alpha$. We have
$$\left(z_{1}, 2 / k,-1\right)(i, 0,1)=\left(z_{1}-i, 2 / k+2 \operatorname{Re} z_{1},-1\right) .$$
On the other hand,
$$(-i, 0,1)\left(z_{1}, 2 / k,-1\right)=\left(-i+z_{1}, 2 / k-2 \operatorname{Re} z_{1},-1\right) .$$
As above, the first and second coordinates yields no information, while the second coordinate implies that $\operatorname{Re} z_{1}=0$.

Hence, we deduce from the above computations, the desired homomorphism $\rho$ is defined by
$$\begin{array}{lr}
\rho(a)=(1,0,1), & \rho(b)=(i, 0,1) \\
\rho(c)=(0,4 / k, 1) & \rho(\alpha)=(0,2 / k,-1) .
\end{array}$$
Notice that these solutions are in $\mathbb{Q}(i)$ and not $\mathbb{Z}[i]$. This is rectified by conjugating the above representation by a dilation of $2 k$. This dilation is linear on the first factor, quadratic on the second factor, and trivial on the third factor. The resulting faithful representation is
$$\begin{array}{lr}
\rho(a)=(2 k, 0,1), & \rho(b)=(2 k i, 0,1) \\
\rho(c)=(0,16 k, 1) & \rho(\alpha)=(0,8 k,-1) .
\end{array}$$
That this is faithful follows from Lemma 7.2 (b) once the conditions of this lemma have been verified. The injectivity of $\rho_{\mid\langle a, b, c\rangle}=\varphi_{4}$ follows from Lemma 7.2 (a). To check that $\rho\left(\rho^{-1}(\langle a, b, c\rangle)\right)=\langle a, b, c\rangle$, by the remark proceeding the proof of Lemma 7.2 it suffices to show that $\alpha \notin \rho\left(\rho^{-1}(\langle a, b, c\rangle)\right)$. The validity of this is obvious.
For the seventh family (7), we have the presentation
$$\left\langle a, b, c, \alpha:[b, a]=c^{k},[c, a]=[c, b]=[c, \alpha]=1, \alpha a=a b \alpha, \alpha b=a^{-1} \alpha, \alpha^{6}=c^{k_{1}}\right\rangle$$
with
$$\begin{aligned}
& k \equiv 0 \quad \bmod 6, k_{1}=1, \text { or } k \equiv 4 \quad \bmod 6, k_{1}=1, \text { or } \\
& k \equiv 0 \quad \bmod 6, k_{1}=5, \text { or } k \equiv 2 \quad \bmod 6, k_{1}=5
\end{aligned}$$

We take $\varphi_{3}$ in this case. By considering all the relations, we get
$$\begin{aligned}
(0,4 / k, 1)= & (0, s, 1) \\
\left(z_{1}+\eta_{1}, t_{1}+2 \operatorname{Im}\left\langle z, \eta_{1}\right\rangle, \eta_{1}\right)= & \left(1+\zeta_{3}+z_{1}, t_{1}+\right. \\
& \left.2 \operatorname{Im}\left\langle 1+\zeta_{3}, z_{1}\right\rangle+2 \operatorname{Im}\left\langle 1, \zeta_{3}\right\rangle+t_{1}, \eta_{1}\right) \\
{\left[z_{1}+\eta_{1} \zeta_{3}, t_{1}+2 \operatorname{Im}\left\langle z_{1}, \eta_{1} \zeta_{3}\right\rangle, \eta_{1}\right)=} & \left(-1+z_{1}, t_{1}+2 \operatorname{Im}\left\langle-1, z_{1}\right\rangle, \eta_{1}\right)
\end{aligned}$$
We omit the last relation $\alpha^{6}=c^{k_{1}}$ as it is quite long. Note the commutator relations (aside from $[b, a]=c^{k}$ ) are all trivially satisfied. Solving these equations and conjugating by a dilation of $12 k$ to get the coefficients in $\mathbb{Z}\left[\zeta_{3}\right]$, we have
$$\begin{array}{lr}
\varphi_{3}(a)=(12 k, 0,1), & \varphi_{3}(b)=\left(12 k \zeta_{3}, 0,1\right), \\
\varphi_{3}(c)=(0,288 k \sqrt{3}, 1), & \varphi_{3}(\alpha)=\left(-6 k, 12 k\left(4 k_{1}+3 k\right) \sqrt{3}, \zeta_{6}\right) .
\end{array}$$
That this is faithful follows from Lemma 7.2 and the remark following the proof.
The other remaining families are handled similarly. \(\square\)

The proof is completed by following the injection $\rho$ from Theorem 7.1 with the injection
$$\psi: \mathfrak{N}_{3} \rtimes\langle\mathrm{U}(1), \iota\rangle \longrightarrow \mathrm{U}(2,1)$$
given by
$$\left(\xi, t, \iota^{\varepsilon} U\right) \longmapsto\left(\begin{array}{ccc}
1 & \xi & \xi \\
-\bar{\xi} & 1-\frac{1}{2}\left(\|\xi\|^{2}-i t\right) & -\frac{1}{2}\left(\|\xi\|^{2}-i t\right) \\
\bar{\xi} & \frac{1}{2}\left(\|\xi\|^{2}-i t\right) & 1+\frac{1}{2}\left(\|\xi\|^{2}-i t\right)
\end{array}\right)\left(\begin{array}{ccc}
U & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right) \iota^{\varepsilon} .$$
For completeness, we give all the linear representations in the appendix.
Remark Theorem 7.1 can be strengthened somewhat. Specifically, we can prove that there is a dense set of almost flat structures on any compact nil 3-manifold which can be realized in cusp cross-sections of arithmetic complex hyperbolic 2-orbifolds. We refer the reader for [24] for more on this.

\subsection*{7.3 Nil 5-manifolds}

Using the list of isomorphism types of holonomy groups for nil 5-manifolds given in [10], we can carry out the same analysis.

Proposition 7.3 The only complex holonomy groups which yield arithmetically inadmissible groups are $C_{5}, C_{10}, C_{12}$ and $C_{24}$.

To see this, by Corollary 5.5 it suffices to check the field of definition for all the distinct representations of the holonomy group in $\operatorname{GL}(2 ; \mathbf{C})$. For most of the groups, every representation will be conjugate to one defined over an imaginary quadratic number field. Both $C_{12}$ and $C_{24}$ can arise via central products of nil 3-manifold groups for which Theorem 6.4 can be applied to show that the resulting AB-groups are arithmetically inadmissible. For $C_{5}$-holonomy, we can apply Proposition 6.1, which in turn yields the result for $C_{10}$-holonomy, since any arithmetic representation for an AB-group with $C_{10}$-holonomy would yield one for an AB-group with $C_{5}$-holonomy.

\section*{8 Final comment}

As discussed in the remark following Corollary 6.5, one cannot expect to obtain manifolds of finite volume with just a single cusp in the above construction. However, a natural question is whether or not one can guarantee that $\mathbf{H}_{\mathbf{C}}^{2} / \Pi$ be constructed to be a manifold. For instance, in the second family (2), the only congruence subgroup which contains $\Gamma$ is the level two congruence subgroup. This is seen to have torsion though, as
$$\left(\begin{array}{ccc}
-1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right)$$
is an element of this subgroup. However by results of Borel [3], we can guarantee that the first and third families map into torsion free groups. We can simply conjugate by a dilation to ensure that the representation maps into a congruence subgroup which is torsion free. [3] is needed in showing that the congruence subgroup is torsion free.

\section*{9 Appendix: solutions to Equation (1)}

Here, we include the matrices found by solving Equation (1) in §7. For all possible faithful representations, see 24.
$$\begin{array}{rlrl}
a & =\left(\begin{array}{ccc}
1 & 2 k & 2 k \\
-2 k & 1-2 k^{2} & -2 k^{2} \\
2 k & 2 k^{2} & 1+2 k^{2}
\end{array}\right), & b=\left(\begin{array}{ccc}
1 & 2 k i & 2 k i \\
2 k i & 1-2 k^{2} & 2 k^{2} \\
-2 k i & 2 k^{2} & 1+2 k^{2}
\end{array}\right) \\
c & =\left(\begin{array}{ccc}
1 & 0 & 0 \\
0 & 1+8 k i & 8 k i \\
0 & -8 k i & 1-8 k i
\end{array}\right) . & &
\end{array}$$
\begin{itemize}
\item[(2)]
$$\begin{aligned}
& a=\left(\begin{array}{ccc}
1 & 2 k & 2 k \\
-2 k & 1-2 k^{2} & -2 k^{2} \\
2 k & 2 k^{2} & 1+2 k^{2}
\end{array}\right), \\
& c=\left(\begin{array}{ccc}
1 & 0 & 0 \\
0 & 1+8 k i & 8 k i \\
0 & -8 k i & 1-8 k i
\end{array}\right),
\end{aligned}$$
$$\begin{gathered}
b=\left(\begin{array}{ccc}
1 & 2 k i & 2 k i \\
2 k i & 1-2 k^{2} & 2 k^{2} \\
-2 k i & 2 k^{2} & 1+2 k^{2}
\end{array}\right), \\
\alpha=\left(\begin{array}{ccc}
-1 & 0 & 0 \\
0 & 1+k i & k i \\
0 & -k i & 1-k i
\end{array}\right) .
\end{gathered}$$
\item[(3)]
$$\begin{aligned}
& a=\left(\begin{array}{ccc}
1 & 4 k & 4 k \\
-4 k & 1-8 k^{2} & -8 k^{2} \\
4 k & 8 k^{2} & 1+8 k^{2}
\end{array}\right), \\
& c=\left(\begin{array}{ccc}
1 & 0 & 0 \\
0 & 1+16 k i & 16 k i \\
0 & -16 k i & 1-16 k i
\end{array}\right),
\end{aligned}$$
$$\begin{aligned}
b & =\left(\begin{array}{ccc}
1 & 4 k i & 4 k i \\
4 k i & 1-8 k^{2} & 8 k^{2} \\
-4 k i & 8 k^{2} & 1+8 k^{2}
\end{array}\right), \\
\alpha & =\left(\begin{array}{ccc}
1 & 2 k & 2 k \\
2 k & 1-2 k^{2} & -2 k^{2} \\
-2 k & 2 k^{2} & 1+2 k^{2}
\end{array}\right) \iota .
\end{aligned}$$
\item[(4)]
$$\begin{array}{rlr}
a=\left(\begin{array}{ccc}
1 & 4 k & 4 k \\
-4 k & 1-8 k^{2} & -8 k^{2} \\
4 k & 8 k^{2} & 1+8 k^{2}
\end{array}\right), & b=\left(\begin{array}{ccc}
1 & 4 k i & 4 k i \\
4 k i & 1-8 k^{2} & 8 k^{2} \\
-4 k i & 8 k^{2} & 1+8 k^{2}
\end{array}\right), \\
c=\left(\begin{array}{ccc}
1 & 0 & 0 \\
0 & 1+16 k i & 16 k i \\
0 & -16 k i & 1-16 k i
\end{array}\right), & \alpha=\left(\begin{array}{cc}
-1 & 2 k+2 k i \\
-2 k+2 k i & 1-4 k^{2} \\
2 k-2 k i & 4 k^{2} \\
1+4 k^{2}
\end{array}\right), \\
\beta=\left(\begin{array}{ccc}
1 & 2 k & 2 k \\
-2 k & 1-4 k^{2} & -4 k^{2} \\
2 k & 4 k^{2} & 1+4 k^{2}
\end{array}\right), &
\end{array}$$
\item[(5)]
$$\begin{aligned}
& a=\left(\begin{array}{ccc}
1 & 2 k & 2 k \\
-2 k & 1-2 k^{2} & -2 k^{2} \\
2 k & 2 k^{2} & 1+2 k^{2}
\end{array}\right), \\
& c=\left(\begin{array}{ccc}
1 & 0 & 0 \\
0 & 1+8 k i & 8 k i \\
0 & -8 k i & 1-8 k i
\end{array}\right),
\end{aligned}$$
$$\begin{gathered}
b=\left(\begin{array}{ccc}
1 & 2 k i & 2 k i \\
2 k i & 1-2 k^{2} & 2 k^{2} \\
-2 k i & 2 k^{2} & 1+2 k^{2}
\end{array}\right), \\
\alpha=\left(\begin{array}{ccc}
i & 0 & 0 \\
0 & 1+\frac{p k}{2} i & \frac{p k}{2} i \\
0 & -\frac{p k}{2} i & 1-\frac{p k}{2} i
\end{array}\right) .
\end{gathered}$$
\end{itemize}
\begin{itemize}
\item[(6)]
$$\begin{aligned}
a & =\left(\begin{array}{ccc}
1 & 24 k & 24 k \\
-24 k & 1-288 k^{2} & -288 k^{2} \\
24 k & 288 k^{2} & 1+288 k^{2}
\end{array}\right), \\
b & =\left(\begin{array}{ccc}
1 & -12+12 \sqrt{3} i & -12+12 \sqrt{3} i \\
12+12 \sqrt{3} i & 1-288 k^{2} & -288 k^{2} \\
-12-12 \sqrt{3} i & 288 k^{2} & 1+288 k^{2}
\end{array}\right), \\
c & =\left(\begin{array}{ccc}
1 & 0 & 0 \\
0 & 1+144 k \sqrt{3} i & 144 k \sqrt{3} i \\
0 & -144 k \sqrt{3} i & 1-144 k \sqrt{3} i
\end{array}\right), \\
\alpha & =\left(\begin{array}{ccc}
1 & \mu & \mu \\
6\left[k+2 k_{1}\right]+6 \sqrt{3}\left[k-2 k_{1}\right] i & 1-\sigma & -\sigma \\
-6\left[k+2 k_{1}\right]-6 \sqrt{3}\left[k-2 k_{1}\right] i & \sigma & 1+\sigma
\end{array}\right)\left(\begin{array}{ccc}
\zeta_{3} & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right),
\end{aligned}$$
where
$$\sigma=\frac{1}{2}\left[36\left(k+2 k_{1}\right)^{2}+108\left(k-2 k_{1}\right)^{2}-192 k \sqrt{3}\left(k\|z\|^{2}+2 k_{2}\right) i\right]$$
and
$$\mu=-6\left[k+2 k_{1}\right]+6 \sqrt{3}\left[k-2 k_{1}\right] i .$$
\item[(7)]
$$\begin{aligned}
a & =\left(\begin{array}{ccc}
1 & 12 k & 12 k \\
-12 k & 1-144 k^{2} & -144 k^{2} \\
12 k & 144 k^{2} & 1+144 k^{2}
\end{array}\right), \\
b & =\left(\begin{array}{ccc}
1 & -6 k+6 k \sqrt{3} i & -6 k+6 k \sqrt{3} i \\
6 k+6 k \sqrt{3} i & 1-144 k^{2} & -144 k^{2} \\
-6 k-6 k \sqrt{3} i & 144 k^{2} & 1+144 k^{2}
\end{array}\right), \\
c & =\left(\begin{array}{ccc}
1 & 0 & 0 \\
0 & 1+288 k \sqrt{3} i & 288 k \sqrt{3} i \\
0 & -288 k \sqrt{3} i & 1-288 \sqrt{3} i
\end{array}\right), \\
\alpha & =\left(\begin{array}{ccc}
1 & -6 k & -6 k \\
3 k-3 k \sqrt{3} i & 1-\chi & -\chi \\
-3 k+3 k \sqrt{3} i & \chi & 1+\chi
\end{array}\right)\left(\begin{array}{ccc}
\zeta_{6} & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right),
\end{aligned}$$
where
$$\chi=-36 k^{2}+12 k\left(4 k_{1}+3 k\right) \sqrt{3} i .$$
\end{itemize}

\section*{References}
\begin{itemize}
\item[] [1] D Allcock, Reflection groups on the octave hyperbolic plane, J. Algebra 213 (1999) 467-498 MR1673465
\item[] [2] N Bergeron, Premier nombre de Betti et spectre du laplacien de certaines variétés hyperboliques, Enseign. Math. 46 (2000) 109-137 MR1769939
\end{itemize}
\begin{itemize}
\item[] [3] A Borel, Compact Clifford-Klein forms of symmetric spaces, Topology 2 (1963) 111-122 MR0146301
\item[] [4] A Borel, Linear algebraic groups, second edition, Graduate Texts in Mathematics 126, Springer-Verlag, New York (1991) MR1102012
\item[] [5] MR Bridson, A Haefliger, Metric spaces of non-positive curvature, Grundlehren der Mathematischen Wissenschaften 319, Springer-Verlag, Berlin (1999) MR1744486
\item[] [6] J S Chahal, Solution of the congruence subgroup problem for solvable algebraic groups, Nagoya Math. J. 79 (1980) 141-144 MR0587415
\item[] [7] K Corlette, Archimedean superrigidity and hyperbolic geometry, Ann. of Math. 135 (1992) 165-182 MR1147961
\item[] [8] C W Curtis, I Reiner, Representation theory of finite groups and associative algebras, Reprint of the 1962 original, Wiley Classics Library, John Wiley \& Sons Inc. New York (1988) MR1013113
\item[] [9] K Dekimpe, Almost-Bieberbach groups: affine and polynomial structures, Lecture Notes in Mathematics 1639, Springer-Verlag, Berlin (1996) MR1482520
\item[] [10] K Dekimpe, B Eick, Computational aspects of group extensions and their applications in topology, Experiment. Math. 11 (2002) 183-200 MR1959262
\item[] [11] F T Farrell, S Zdravkovska, Do almost flat manifolds bound?, Michigan Math. J. 30 (1983) 199-208 MR0718265
\item[] [12] W M Goldman, Complex hyperbolic geometry, Oxford Mathematical Monographs, The Clarendon Press, Oxford University Press, New York (1999) MR1695450
\item[] [13] M Gromov, Almost flat manifolds, J. Differential Geom. 13 (1978) 231-241 MR0540942
\item[] [14] E Hamilton, Abelian subgroup separability of Haken 3-manifolds and closed hyperbolic $n$-orbifolds, Proc. London Math. Soc. 83 (2001) 626-646 MR1851085
\item[] [15] G C Hamrick, D C Royster, Flat Riemannian manifolds are boundaries, Invent. Math. 66 (1982) 405-413 MR0662600
\item[] [16] Y Kamishima, Cusp cross-sections of hyperbolic orbifolds by nilmanifolds, in preparation
\item[] [17] I Kim, JR Parker, Geometry of quaternionic hyperbolic manifolds, Math. Proc. Cambridge Philos. Soc. 135 (2003) 291-320 MR2006066
\item[] [18] D D Long, Immersions and embeddings of totally geodesic surfaces, Bull. London Math. Soc. 19 (1987) 481-484 MR0898729
\item[] [19] D D Long, A W Reid, On the geometric boundaries of hyperbolic 4-manifolds, Geom. Topol. 4 (2000) 171-178 MR1769269
\item[] [20] D D Long, A W Reid, All flat manifolds are cusps of hyperbolic orbifolds, Algebr. Geom. Topol. 2 (2002) 285-296 MR1917053
\end{itemize}
[21] C Maclachlan, A W Reid, The arithmetic of hyperbolic 3-manifolds, Graduate Texts in Mathematics 219, Springer-Verlag, New York (2003) MR1937957
[22] AI Mal'cev, On homomorphisms onto finite groups, Ivanov. Gos. Ped. Inst. Ucen. Zap. 18 (1958) 49-60
[23] G A Margulis, G A Soĭfer, Maximal subgroups of infinite index in finitely generated linear groups, J. Algebra 69 (1981) 1-23 MR0613853
[24] D B McReynolds, Ph.D. Thesis (In preparation)
[25] M Q Ouyang, Geometric invariants for Seifert fibred 3-manifolds, Trans. Amer. Math. Soc. 346 (1994) 641-659 MR1257644
[26] V Platonov, A Rapinchuk, Algebraic groups and number theory, translated from the 1991 Russian original by Rachel Rowen, Pure and Applied Mathematics 139, Academic Press, Boston, MA (1994) MR1278263
[27] MS Raghunathan, Discrete subgroups of Lie groups, Ergebnisse series 68, Springer-Verlag, New York (1972), MR0507234
[28] J G Ratcliffe, Foundations of hyperbolic manifolds, Graduate Texts in Mathematics 149, Springer-Verlag, New York (1994) MR1299730
[29] P Scott, The geometries of 3-manifolds, Bull. London Math. Soc. 15 (1983) 401-487 MR0705527
[30] J-P Serre, Linear representations of finite groups, translated from the second French edition by Leonard L. Scott, Graduate Texts in Mathematics 42, Springer-Verlag, New York (1977) MR0450380
[31] W P Thurston, Three-dimensional geometry and topology. Vol. 1, edited by Silvio Levy, Princeton Mathematical Series 35, Princeton University Press, Princeton, NJ (1997) MR1435975
[32] S Upadhyay, A bounding question for almost flat manifolds, Trans. Amer. Math. Soc. 353 (2001) 963-972 MR1804410
[33] M-F Vignéras, Arithmétique des algèbres de quaternions, volume 800 of Lecture Notes in Mathematics, Springer-Verlag, Berlin (1980)
[34] BAF Wehrfritz, Infinite linear groups. An account of the group-theoretic properties of infinite groups of matrices, Ergebnisse series 76, Springer-Verlag, New York (1973) MR0335656
[35] A Weil, Algebras with involutions and the classical groups, J. Indian Math. Soc. (N.S.) 24 (1960) 589-623 (1961) MR0136682
[36] A Weil, Basic number theory, reprint of the second (1973) edition, Classics in Mathematics, Springer-Verlag, Berlin (1995) MR1344916

University of Texas, Austin, TX 78712, USA
Email: dmcreyn@math.utexas.edu
Received: 2 April 2004 Revised: 24 August 04