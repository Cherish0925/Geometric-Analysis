---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Conformal Dirichlet-Neumann Maps and Poincaré-Einstein Manifolds]

Recall from Section 2 there is a tractor twisting of the Yamabe operator $\square: \mathcal{T}^{*}[1-d / 2] \rightarrow$ $\mathcal{T}^{*}[-1-d / 2]$. Let us assume that on some Poincaré-Einstein manifold $\left(M^{d},[g], I\right)$ with boundary $\Sigma$ the Dirichlet problem for $\square: \mathcal{T}^{*}[1-d / 2] \rightarrow \mathcal{T}^{*}[-1-d / 2]$ is uniquely solvable. For example this is the case on the homogeneous model $(C,[g])$ from Section 4.3; since on $C$ the tractor bundle is trivialised by parallel sections this follows easily from the unique solvability of the density problem, as discussed in e.g. [6]. Since the conformal Robin operator $\delta$ is also strongly invariant it follows that we may construct a tractor twisted conformal Dirichlet-to-Neumann map,
$$P_{2, \mathbf{m}_{0}, 0}^{\mathcal{T}}: \mathcal{T}_{\Sigma}^{*}\left[\frac{1-n}{2}\right] \rightarrow \mathcal{T}_{\Sigma}^{*}\left[\frac{-1-n}{2}\right] .$$
Here we are using some key facts. Firstly $\mathcal{T}_{\Sigma}^{*}$ may be identified with the subbundle of the restriction to $\Sigma$ of some ambient tractor bundle $\mathcal{T}^{*}$, and that this subbundle is characterised by being the part of $\left.\mathcal{T}^{*}\right|_{\Sigma}$ annihilated by any contraction with the normal tractor $N^{A}$. Next since $I^{A}$ is parallel and recovers $N^{A}$ along $\Sigma$, it follows from the unique solvability that any solution $u$ to the Dirichlet problem has any contraction with $I^{A}$ vanishing everywhere. (Note that any such contraction itself solves a Yamabe Dirichlet problem, but with Dirichlet data the zero section.) From these observations it follows that the map $P_{2, \mathbf{m}_{0}, 0}^{\mathcal{T}}$ takes values in the bundle $\mathcal{T}_{\Sigma}^{*}\left[\frac{-1-n}{2}\right]$.

Next suppose $\mathcal{U}^{*}$ is an irreducible (conformally weighted) tensor bundle on $\Sigma$ and there is a conformal differential operator $S: \mathcal{U} \rightarrow \mathcal{T}_{\Sigma}^{*}\left[\frac{1-n}{2}\right]$ with conformal formal adjoint (as discussed in e.g. [7]) $S^{*}: \mathcal{T}_{\Sigma}^{*} \rightarrow \mathcal{U}_{*}$. Here $\mathcal{U}_{*}$ is $\mathcal{U} \otimes \mathcal{E}[w]$ where the weight $w$ is such that the natural pairing of a section of $\mathcal{U}^{*}$ with a section of $\mathcal{U}_{*}$, via the conformal metric, yields a density of weight $-n$. Then we may form the composition
$$\mathcal{U}^{*} \xrightarrow{S} \mathcal{T}_{\Sigma}^{*}\left[\frac{1-n}{2}\right] \xrightarrow{P_{2, \mathbf{m}_{0}, 0}^{\mathcal{T}}} \mathcal{T}_{\Sigma}^{*}\left[\frac{-1-n}{2}\right] \xrightarrow{S^{*}} \mathcal{U}_{*} ;$$
by construction this composition $\mathcal{P}:=S^{*} \circ P_{2, \mathbf{m}_{0}, 0}^{\mathcal{T}} \circ S$ is conformally invariant. It is easily verified that $P_{2, \mathbf{m}_{0}, 0}^{\mathcal{T}}$ is self-adjoint (by an adaption of the argument for $P_{2, \mathbf{m}_{0}, 0}$ ), so $\mathcal{P}$ is formally self-adjoint by construction.

The natural candidates for the operators $S: \mathcal{U}^{*} \rightarrow \mathcal{T}_{\Sigma}^{*}\left[\frac{1-n}{2}\right]$ are the so-called differential splitting operators; $S$ is of this form if there is a bundle map $T$ from a subbundle of $\mathcal{T}_{\Sigma}^{*}\left[\frac{1-n}{2}\right]$ to $\mathcal{U}^{*}$ satisfying $T \circ S=i d_{\mathcal{U}^{*}}$. There is a rich and well developed theory for the construction of such splitting operators see for example [17, 28]; for conformal geometry a general and practical construction is developed in [47], while for an elegant recent advance which applies to all parabolic geometries see [12].

Let us illustrate with a simple example. Let $d=4$, take $\mathcal{T}_{\Sigma}^{*}$ to be simply the standard tractor bundle $\mathcal{T}_{\Sigma}$ on $\Sigma$ and for $\mathcal{U}^{*}$ take the cotangent bundle $\mathcal{E}_{\Sigma}^{1}$. There is a splitting operator (see
e.g. [17])
$$E: \mathcal{E}_{\Sigma}^{1} \rightarrow \mathcal{T}_{\Sigma}[-1] \quad \text { by } \quad \phi_{b} \mapsto\left(\begin{array}{c}
0 \\
\phi_{a} \\
-\nabla^{c} \phi_{c}
\end{array}\right) .$$
Thus on the conformal 3-manifold $\Sigma$ we obtain $\mathcal{P}: \mathcal{E}_{\Sigma}^{1} \rightarrow \mathcal{E}_{\Sigma}^{1}[-1]$ by the composition $\mathcal{P}=$ $E^{*} \circ P_{2, \mathbf{m}_{0}, 0}^{\mathcal{T}} \circ E$. To see this is non-trivial we argue as follows. On the homogeneous model the Dirichlet and conformal Neumann problems for $\square: \mathcal{T}[1-d / 2] \rightarrow \mathcal{T}[-1-d / 2]$ are equivalent to trivial twistings of the Dirichlet and conformal Neumann problems for $P_{2}$. Thus they are both properly elliptic normal boundary problem satisfying the Lopatinski-Shapiro conditions and so each has finite dimensional kernel. See [6, Proposition 6.4] for a summary of the relevant facts from [35, 38]. It follows immediately that the composition $P_{2, \mathbf{m}_{0}, 0}^{\mathcal{T}} \circ E$ is non-trivial. Then using that $E$ is $G$-invariant splitting operator and considering the possible $G=\operatorname{SO}(n+1,1)$ intertwinors between $\mathcal{E}^{1}$ and other irreducibles [8] it follows easily that $E^{*} P_{2, \mathbf{m}_{0}, 0}^{\mathcal{T}} \circ E$ is non-trivial. From this point the non-triviality of this operator in general can be established from the pseudo-differential nature of the operator (it is a composition of differential and pseudo-differential operators) and symbol analysis.

It seems likely that a large class of integral order pseudo-differential operators will arise from the construction sketched above. For example a non-linear conformal tensorial Dirichlet-to-Neumann map was announced in [31]; in view of the uniqueness of intertwinors, its linearisation should be recoverable using these ideas.

There is scope to develop a similar translation of the scattering construction to yield tensorial Dirichlet-to-Neumann maps in the case of non-half integral weights. Here a key point is that, on the one hand, the operator $I^{A} D_{A}$ extends the scattering Laplacian to the boundary of the Poincaré-Einstein manifold (where it degenerates to a constant times $\delta$ ), while on the other it is a strongly invariant operator. Given a tractor bundle $\mathcal{T}^{*}[w]$ (of some possibly complex weight $w$ ) an idea for extending data off the boundary is to use sections $u \in \mathcal{T}^{*}[w]$ satisfying $I^{A} D_{A} u=0$ and satisfying the compatible property that $u$ is annihilated by any contraction with $I^{A}$. In particular we may seek solutions of the form $u=\sigma^{z} U_{\mathrm{o}}+\sigma^{2 w+n-z} U_{\mathrm{i}}$ where the tractor bundle sections $U_{\mathrm{o}}$ and $U_{\mathrm{i}}$ are smooth, have appropriate weights, and are annihilated by any contraction with $I^{A}$ (and as usual $\sigma$ is the Einstein scale $\sigma=h(X, I)$ ). The situation is most clear on the homogeneous model $(C,[g])$ from Section 4.3. Once again using that, in this case, the tractor bundles are trivialised by a parallel frame it follows from the density case that the required Poisson operators exist for a set of weights dense in $\mathbb{C}$. In any case, given a scattering map $\left.\left.U_{\mathrm{o}}\right|_{\Sigma} \rightarrow U_{\mathrm{i}}\right|_{\Sigma}$ one may translate to maps between weighted tensor bundles by composing fore and aft with differential splitting operators as for the construction above.

\section*{Acknowledgements}

ARG gratefully acknowledges support from the Royal Society of New Zealand via Marsden Grant no. 06-UOA-029. It is a pleasure to thank Andreas Čap, Robin Graham, Colin Guillarmou and Andrew Hassell for helpful discussions.

\section*{References}
\begin{itemize}
\item[] [1] Albin P., Renormalizing curvature integrals on Poincaré-Einstein manifolds, math.DG/0504161.
\item[] [2] Anderson M., $L^{2}$ curvature and volume renormalization of AHE metrics on 4-manifolds, Math. Res. Lett. 8 (2001), 171-188, math.DG/0011051.
\item[] [3] Armstrong S., Definite signature conformal holonomy: a complete classification, math.DG/0503388.
\end{itemize}
\begin{itemize}
\item[] [4] Bailey T.N., Eastwood M.G., Gover A.R., Thomas's structure bundle for conformal, projective and related structures, Rocky Mountain J. Math. 24 (1994), 1191-1217.
\item[] [5] Branson T., Sharp inequalities, the functional determinant, and the complementary series, Trans. Amer. Math. Soc. 347 (1995), 3671-3742.
\item[] [6] Branson T., Gover A.R., Conformally invariant non-local operators, Pacific J. Math. 201 (2001), 19-60.
\item[] [7] Branson T., Gover A.R., Conformally invariant operators, differential forms, cohomology and a generalisation of $Q$-curvature, Comm. Partial Differential Equations 30 (2005), 1611-1669, math.DG/0309085.
\item[] [8] Branson T., Ólafsson G., Ørsted B., Spectrum generating operators, and intertwining operators for representations induced from a maximal parabolic subgroup, J. Funct. Anal. 135 (1996), 163-205.
\item[] [9] Cartan E., Les espaces à connexion conforme, Ann. Soc. Pol. Math. 2 (1923), 171-202.
\item[] [10] Čap A., Gover A.R., Tractor calculi for parabolic geometries, Trans. Amer. Math. Soc. 354 (2002), 1511-1548.
\item[] [11] Čap A., Gover A.R., Standard tractors and the conformal ambient metric construction, Ann. Global Anal. Geom. 24 (2003), 231-295, math.DG/0207016.
\item[] [12] Čap A., Soǔcek V., Curved Casimir operators and the BGG machinery, arXiv:0708.3180.
\item[] [13] Čap A., Slovák J., Soǔcek V., Bernstein-Gelfand-Gelfand sequences, Ann. of Math. (2) 154 (2001), 97-113, math.DG/0001164.
\item[] [14] Chang A., Qing J., Yang P., On the renormalized volumes for conformally compact Einstein manifolds, math.DG/0512376.
\item[] [15] Cherrier P., Problèmes de Neumann non linéaires sur les variétés riemanniennes, J. Funct. Anal. 57 (1984), 154-206.
\item[] [16] Derdzinski A., Maschler G., Special Kähler-Ricci potentials on compact Kähler manifolds, J. Reine Angew. Math. 593 (2006), 73-116, math.DG/0204328.
\item[] [17] Eastwood M.G., Notes on conformal differential geometry, Supp. Rend. Circ. Matem. Palermo 43 (1996), 57-76.
\item[] [18] Eastwood M.G., Rice J., Conformally invariant differential operators on Minkowski space and their curved analogues, Comm. Math. Phys. 109 (1987), 207-228, Erratum, Comm. Math. Phys. 144 (1992), 213.
\item[] [19] Fefferman C., Graham C.R., The ambient metric, arXiv:0710.0919.
\item[] [20] Gover A.R., Aspects of parabolic invariant theory, The 18th Winter School "Geometry and Physics" (Srní, 1998), Rend. Circ. Mat. Palermo (2) Suppl. no. 59 (1999), 25-47.
\item[] [21] Gover A.R., Almost conformally Einstein manifolds and obstructions, in Proceedings of the 9th International Conference "Differential Geometry and Its Applications" (Matfyzpress, Prague, 2005), 2005, 247-260, math.DG/0412393.
\item[] [22] Gover A.R., Laplacian operators and Q-curvature on conformally Einstein manifolds, Math. Ann., 336 (2006), 311-334, math.DG/0506037.
\item[] [23] Gover A.R., Nurowski P., Obstructions to conformally Einstein metrics in $n$ dimensions, J. Geom. Phys. 56 (2006), 450-484, math.DG/0405304.
\item[] [24] Gover A.R., Peterson L., Conformally invariant powers of the Laplacian, $Q$-curvature, and tractor calculus, Comm. Math. Phys. 235 (2003), 339-378, math-ph/0201030.
\item[] [25] Gover A.R., Almost Einstein manifolds in Riemannian signature, in preparation.
\item[] [26] Gover A.R., Šilhan J., Commuting linear operators and decompositions; applications to Einstein manifolds, math.AC/0701377.
\item[] [27] Gover A.R., Šilhan J., Conformal operators on forms and detour complexes on Einstein manifolds, arXiv:0708.3854.
\item[] [28] Gover A.R., Šilhan J., The conformal Killing equation on forms - prolongations and applications, Differential Geom. Appl., to appear, math.DG/0601751.
\item[] [29] Gover A.R., Somberg P., Souček V., Yang-Mills detour complexes and conformal geometry, Comm. Math. Phys., to appear, math.DG/0606401.
\item[] [30] Graham C.R., Volume and area renormalizations for conformally compact Einstein metrics, in The Proceedings of the 19th Winter School "Geometry and Physics" (Srní, 1999), Rend. Circ. Mat. Palermo (2) Suppl. no. 63 (2000), 31-42.
\end{itemize}
\begin{itemize}
\item[] [31] Graham C.R., Dirichlet-to-Neumann map for Poincaré-Einstein metrics, Oberwolfach Reports 2 (2005), 2200-2203.
\item[] [32] Graham C.R., Jenne R., Mason L.J., Sparling G.A., Conformally invariant powers of the Laplacian. I. Existence, J. London Math. Soc. 46 (1992), 557-565.
\item[] [33] Graham C.R., Lee J.M., Einstein metrics with prescribed conformal infinity on the ball, Adv. Math. 87 (1991), 186-225.
\item[] [34] Graham C.R., Zworski M., Scattering matrix in conformal geometry, Invent. Math. 152 (2003), 89-118, math.DG/0109089.
\item[] [35] Grubb G., Functional calculus of pseudodifferential boundary problems, 2nd ed., Birkhäuser, Boston, 1996.
\item[] [36] Guillarmou C., Meromorphic properties of the resolvent on asymptotically hyperbolic manifolds, Duke Math. J. 129 (2005), 1-37, math.SP/0311424.
\item[] [37] Guillarmou C., Guillopé L., The determinant of the Dirichlet-to-Neumann map for surfaces with boundary, math.SP/0701727.
\item[] [38] Hörmander L., The analysis of linear partial differential operators III, Springer-Verlag, Berlin, 1985.
\item[] [39] Joshi M., Sá Barreto A., Inverse scattering on asymptotically hyperbolic manifolds, Acta Math. 184 (2000), 41-86, math.SP/9811118.
\item[] [40] Kumano-go H., Pseudo-differential operators, MIT Press, Cambridge, 1974.
\item[] [41] Maldacena J., The large $N$ limit of superconformal field theories and supergravity, Adv. Theor. Math. Phys. 2 (1998), 231-252, hep-th/9711200.
\item[] [42] Mazzeo R., The Hodge cohomology of a conformally compact metric, J. Differential Geom. 28 (1988), 309-339.
\item[] [43] Mazzeo R., Unique continuation at infinity and embedded eigenvalues for asymptotically hyperbolic manifolds, Amer. J. Math. 113 (1991), 25-45.
\item[] [44] Mazzeo R., Melrose R., Meromorphic extension of the resolvent on complete spaces with asymptotically constant negative curvature, J. Funct. Anal. 75 (1987), 260-310.
\item[] [45] Perry P., The Laplace operator on a hyperbolic manifold. II. Eisenstein series and the scattering matrix, J. Reine Angew. Math. 398 (1989), 67-91.
\item[] [46] Sasaki S., On the spaces with normal conformal connexions whose groups of holonomy fix a point or a hypersphere II, Japan J. Math. 18 (1943), 623-633.
\item[] [47] Šilhan J., Invariant operators in conformal geometry, PhD thesis, University of Auckland, 2006.
\item[] [48] Thomas T.Y., On conformal geometry, Proc. Natl. Acad. Sci. USA 12 (1926), 352-359.
\item[] [49] Witten E., Anti de Sitter space and holography, Adv. Theor. Math. Phys. 2 (1998), 253-291, hep-th/9802150.
\end{itemize}