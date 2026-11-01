---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Local models and integrability of certain almost Kahler 4- ...]

We now prove (66). As in Lemma 5, we need to first investigate the 2-jet of $\bar{\Omega}$ (equivalently, the 1-jet of $\bar{a}$ ), with the help of the Ricci relations (62) and (61). Let $p_{i}, q_{i}, i=1,2$ be the 1-forms defined by the first relation below. The other three relations follow by (21) and (22).
$$\begin{aligned}
\nabla \bar{a} & =p_{1} \otimes \bar{a}+q_{1} \otimes J \bar{a}+p_{2} \otimes J_{1} \bar{a}+q_{2} \otimes J_{2} \bar{a} ; \\
\nabla(J \bar{a}) & =-q_{1} \otimes \bar{a}+p_{1} \otimes J \bar{a}+\left(a-q_{2}\right) \otimes J_{1} \bar{a}+\left(p_{2}-J a\right) \otimes J_{2} \bar{a} ; \\
\nabla\left(J_{1} \bar{a}\right) & =-p_{2} \otimes \bar{a}+\left(q_{2}-a\right) \otimes J \bar{a}+p_{1} \otimes J_{1} \bar{a}+\left(b-q_{1}\right) \otimes J_{2} \bar{a} ; \\
\nabla\left(J_{2} \bar{a}\right) & =-q_{2} \otimes \bar{a}+\left(J a-p_{1}\right) \otimes J \bar{a}+\left(q_{1}-b\right) \otimes J_{1} \bar{a}+p_{1} \otimes J_{2} \bar{a} .
\end{aligned}$$
From the formula (61) of Lemma 6, it follows immediately that the 1 -form $p_{1}$ is given by
$$p_{1}=\frac{1}{2} d\left(\ln |\nabla \bar{\Omega}|^{2}\right)=-\frac{1}{|\bar{a}|^{2}} I W_{3}^{-}(\bar{\phi})(\bar{a}) .$$
An important point of this formula is that $p_{1}^{\sharp} \in D^{\perp}$. For the 1 -forms $q_{1}, p_{2}, q_{2}$, one obtains
$$\begin{aligned}
& q_{1}=-I p_{1}-\bar{b}-d^{J}\left(\ln |\nabla \Omega|^{2}\right) \\
& p_{2}=-\frac{1}{2} I_{2} J_{1} \bar{a}+\frac{1}{2} J a \\
& q_{2}=I p_{2}
\end{aligned}$$
where $I_{1}$ and $I_{2}$ denote the (local) almost complex structures corresponding to $\bar{\phi}$ and $I \bar{\phi}$; recall that $J_{1}, J_{2}$ stand for the almost complex structures dual to $\phi$ and $J \phi$. Let us just briefly explain how the relations (69) are obtained. Since both $D$ and $D^{\perp}$ are involutive distributions, we have
$$\begin{aligned}
(d \bar{a})\left(X, X^{\prime}\right) & =(d(J \bar{a}))\left(X, X^{\prime}\right)=0, \forall X, X^{\prime} \in D^{\perp} \\
\left(d\left(J_{1} \bar{a}\right)\right)\left(Y, Y^{\prime}\right) & =\left(d\left(J_{2} \bar{a}\right)\right)\left(Y, Y^{\prime}\right)=0, \forall Y, Y^{\prime} \in D .
\end{aligned}$$
and using (67), these can be seen to be equivalent to $q_{2}=I p_{2}$. For the remaining two relations we use (67) and $q_{2}=I p_{2}$ plugged into the identities (62). Taking the $1 / 2(\Omega+\bar{\Omega})$ -components and the $\llbracket \Lambda_{J}^{0,2} M \rrbracket$-components of the identities thus obtained, we eventually get
$$q_{1}+I p_{1}+\bar{b}=-d^{J}\left(\ln |\nabla \Omega|^{2}\right),$$
which is the second relation of (69); the $\llbracket \Lambda_{I}^{0,2} M \rrbracket$-components of the Ricci identities (62) imply
$$p_{2}^{D}=-\frac{1}{2} I_{2} J_{1} \bar{a},$$
or, equivalently,
$$p_{2}=-\frac{1}{2} I_{2} J_{1} \bar{a}+p_{0} \text {, with } p_{0}^{\sharp} \in D^{\perp} \text {. }$$
So far we have basically followed the track of the computations made in Lemma 5. However, now we can obtain even more by determining completely the 1 -form $p_{0}$. For this, write the relation between $\Omega$ and $\bar{\Omega}$ as
$$\Omega=\frac{2}{|\bar{a}|^{2}} \bar{a} \wedge J \bar{a}-\bar{\Omega},$$
and take the covariant derivative of this relation, using (21), (56), (67-69). This eventually leads to $p_{0}=\frac{1}{2} J a$.

As we have already noticed, the opposite almost Hermitian structure $(g, \tilde{J})$ associated with $(g, I)$ is not a new structure, but just $(g,-J)$. However, the iteration of the construction, imposes a natural new gauge $\tilde{\phi} \in \llbracket \Lambda_{J}^{0,2} M \rrbracket$,
$$\tilde{\phi}=\bar{\phi}+\frac{2}{|\bar{a}|^{2}} I \bar{a} \wedge I \bar{\phi}(\bar{a}),$$
which may be different than the initial gauge $\phi$. Taking the covariant derivative of (70) and using (58), (61) and (67-69), one finds, after a long but straightforward computation, that the 1-form $\tilde{b}$ of the structure ( $g, \tilde{J}$ ) with respect to the gauge $\tilde{\phi}$ is given by (compare with (59)):
$$\tilde{b}=3 \bar{b}+d^{I}\left(\ln |\nabla \bar{\Omega}|^{2}\right)+2 d^{J}\left(\ln |\nabla \Omega|^{2}\right) .$$
Now relation (66) immediately follows since $d \tilde{b}=-\gamma_{\tilde{J}}=\gamma_{J}$. □
Proof of Proposition 2. We assume as in Lemma 7 that $(g, I)$ is not Kähler on an open set $U_{0} \subset U$. Then on $U_{0}$ both relations (51) and (66) hold, and taking the appropriate linear combination of them, we obtain
$$5\left(\gamma_{I}-\gamma_{J}\right)=d d^{I}\left(\ln |\nabla \bar{\Omega}|^{2}\right) .$$
On the other hand, starting from (25) and its companion relation giving $\gamma_{I}$, and by using (20) and the curvature information picked up in Lemma 6, we compute
$$\begin{aligned}
\gamma_{I}-\gamma_{J} & =R(\bar{\Omega})-\bar{a} \wedge I \bar{a}-R(\Omega)+a \wedge J a \\
& =-\frac{|\nabla \Omega|^{2}}{8}(\Omega+\bar{\Omega})-\frac{|\nabla \bar{\Omega}|^{2}}{16}(\Omega-\bar{\Omega}) .
\end{aligned}$$
From the last two identities we obtain the equality
$$-\frac{|\nabla \Omega|^{2}}{8}(\Omega+\bar{\Omega})-\frac{|\nabla \bar{\Omega}|^{2}}{16}(\Omega-\bar{\Omega})=\frac{1}{5} d d^{I}\left(\ln |\nabla \bar{\Omega}|^{2}\right),$$
which holds at every point of the open set $U_{0}$. Since $d^{I}\left(\ln |\nabla \bar{\Omega}|^{2}\right)$ is dual to a vector field in $D^{\perp}$ and $D^{\perp}$ is involutive, it follows that the right hand-side of (71) has a zero inner product with $\Omega+\bar{\Omega}$. For this to hold for the left hand-side of (71) as well, we must have $|\nabla \Omega|=0$ at every point of $U_{0}$. But that is a contradiction, since $U_{0}$ is a subset of $U$, the set of points where $|\nabla \Omega| \neq 0$. Therefore, the assumption that the opposite structure $(g, I)$ is not Kähler must be false, hence we proved Proposition 2. □

\section*{5. Proof of Theorem 2}

As a consequence of Theorem 1 and Proposition 1, we first obtain the following global version of Proposition 2, which is essential for the proof of Theorem 2, but also presents interest in its own.

Proposition 3. Any connected, strictly almost Kähler 4-manifold $(M, g, J, \Omega)$ satisfying the third Gray condition (3) admits a globally defined Kähler structure $(g, I)$ which yields the opposite orientation to the one of $(M, J)$.

Proof. We show that the opposite almost Kähler structure $(g, I)$ defined as in Theorem 3 can be extended globally on $M$. Let $p \in M-U$ be any point of the zero locus of the Nijenhuis tensor $N$. By the unique continuation property of $N$ (see Proposition 1), there exists a number $k \geq 2$ such that
$$\left(\nabla^{\ell} \Omega\right)(p)=0, \forall 1 \leq \ell \leq(k-1) ; \quad\left(\nabla^{k} \Omega\right)(p) \neq 0 .$$
As a consequence, we obtain
$$0=\left\langle\nabla^{*} \nabla\left(\nabla^{k-1} \Omega\right), \nabla^{k-1} \Omega\right\rangle_{p}=-\frac{1}{2} \Delta\left(\left|\nabla^{k-1} \Omega\right|^{2}\right)(p)+\left|\nabla^{k} \Omega\right|^{2}(p),$$
which shows that $\Delta\left(\left|\nabla^{k-1} \Omega\right|^{2}\right) \neq 0$ at $p$, hence also in a small neighborhood of $p$. On $U$, the distribution $D^{\perp}$ is spanned by the commuting hamiltonian Killing fields $\frac{\partial}{\partial z}$ and $\frac{\partial}{\partial t}$ (see Theorem 1), so that $d\left|\nabla^{k-1} \Omega\right|^{2}$ is zero on $D^{\perp}$; equivalently, $\left|\nabla^{k-1} \Omega\right|^{2}$ is a function on the Riemann surface $\Sigma$. It then follows that on $U$ we have (see (14)):
$$d d^{J}\left(\left|\nabla^{k-1} \Omega\right|^{2}\right)=-\Delta\left(\left|\nabla^{k-1} \Omega\right|^{2}\right) \Omega_{\Sigma},$$
where, recall, $\Omega_{\Sigma}$ denotes the volume form of the (locally defined) Riemann surface $\Sigma$; as a global object on $U, \Omega_{\Sigma}$ is given by the restriction of $\Omega$ to $D \subset T U$, i.e. $\Omega_{\Sigma}(\cdot, \cdot)=$ $\Omega\left(\operatorname{pr}^{D} \cdot, \operatorname{pr}^{D} \cdot\right)$ where $\operatorname{pr}^{D}$ denotes the projection to $D$. We thus can define $I$ in a small neighborhood of $p$ by setting
$$\Omega_{I}=-\Omega-\frac{2}{\Delta\left(\left|\nabla^{k-1} \Omega\right|^{2}\right)} d d^{J}\left(\left|\nabla^{k-1} \Omega\right|^{2}\right) .$$
By (72), this agrees with the definition of $I$ on $U$. Since $U$ is dense in $M$ and $(g, I)$ is Kähler on $U$, we conclude that $I$ can be extended as a Kähler structure on whole $M$. □

Now we are ready to prove Theorem 2.
Suppose for contradiction that $(M, g, J, \Omega)$ is a compact strictly almost Kähler 4-manifold whose curvature satisfies (3). According to Proposition 3, we can consider $(M, g, I)$ as a compact Kähler surface which also admits an almost Kähler structure $(g, J, \Omega)$, compatible with the opposite orientation to the one of $(M, I)$; equivalently, $\Omega$ is an indefinite Kähler structure on $(M, I)$ (see [42]). Note then that the distributions $D$ and $D^{\perp}$ are well defined on the whole $M$, respectively as the (-1) and the (+1)-eigenspace of the symmetric endomorphism $Q=J \circ I$ of $T M$. Moreover, since $(g, I)$ is Kähler, the relation (60) of Lemma 6 implies that on $U$ (and therefore, by continuity, on $M$ ) the Ricci tensor has the form
$$\text { Ric }=\frac{s}{2} g_{\Sigma},$$
where $g_{\Sigma}$ is defined on whole $M$ as the restriction of $g$ to the distribution $D$. Alternatively, (73) can be directly derived from the explicit form of $g$ given by (5) of Theorem 1. Using (73), it is easy to compute the Chern forms $\gamma_{I}$ and $\gamma_{J}$ of $(g, I)$ and $(g, J)$, respectively,
$$\gamma_{I}=\frac{s}{2} \Omega_{\Sigma}, \quad \gamma_{J}=\left(\frac{s}{2}+\frac{|\nabla \Omega|^{2}}{4}\right) \Omega_{\Sigma} .$$

It follows that $\gamma_{I}$ and $\gamma_{J}$ are both degenerate on $M$. From Wu's relations, we conclude
$$c_{1}^{2}(M, I)=2 e(M)+3 \sigma(M)=0 ; c_{1}^{2}(M, J)=2 e(M)-3 \sigma(M)=0,$$
hence the Euler characteristic $e(M)$ and the signature $\sigma(M)$ of $(M, I)$ both vanish. From the Kodaira classification [10] and the results of [31] and [42], we conclude that $(M, I)$ can be a ruled surface over an elliptic curve, a complex torus, a hyperelliptic surface, or a minimal properly elliptic surface which is a fibration over a curve of genus at least two, with no fibers of singular reduction. We can easily exclude the cases when $(M, I)$ is a torus or a hyperelliptic surface. Indeed, by replacing $M$ with a finite cover in the case when $(M, I)$ is hyperelliptic, we can always assume that $(M, I)$ is a complex torus. By results of Taubes [45, 46], we know that on a 4-torus any symplectic form is homotopic to an invariant one, i.e. $\left[\gamma_{I}\right]=0$ and $\left[\gamma_{J}\right]=0$, so that by (74) we obtain
$$0=\left[\gamma_{J}-\gamma_{I}\right] \cdot[\Omega]=-\frac{1}{4} \int_{M}|\nabla \Omega|^{2} d \mu$$
a contradiction with the assumption that $J$ is not integrable.
We thus have to analyze the remaining two cases, when $(M, I)$ is a ruled surface or a minimal elliptic surface. Since $\frac{\partial}{\partial t}$ (and $\frac{\partial}{\partial z}$ ) is a (real) $I$-holomorphic vector field in $D^{\perp}$, we conclude that $D^{\perp}$ is a holomorphic, complex rank one distribution on $(U, I)$, hence also on $M$, which gives rise to a non-singular holomorphic foliation $\mathcal{F}$ on the complex surface $(M, I)$. From (74) we get
$$\frac{1}{2}\left(\gamma_{I}-\gamma_{J}\right)=-\frac{|\nabla \Omega|^{2}}{8} \Omega_{\Sigma} \in 2 \pi c_{1}(T \mathcal{F}) .$$
Our next aim is to show that after replacing $M$ with a finite cover if necessary, $H^{0}(M, T \mathcal{F}) \neq$ 0.

In the case when $(M, I)$ admits an elliptic fibration (which also includes some ruled surfaces over an elliptic base), we can use an argument from [5]: since $e(M)=\sigma(M)=0$, we know that the elliptic fibers are smooth or multiple; since $c_{1}(M, I) \neq 0$, we have by Kodaira's formula that $c_{1}(M, I)$ is a non-zero multiple of the Poincaré-dual of any regular (elliptic) fiber $F$. From (74), (75) and using the Poincaré duality, we derive
$$0=\frac{1}{2 \pi} \int_{M} \gamma_{I} \wedge\left(\gamma_{J}-\gamma_{I}\right)=c_{1}(M, I) \cdot\left[\gamma_{J}-\gamma_{I}\right]=-\frac{1}{8 \pi} \int_{F}|\nabla \Omega|^{2} \Omega_{\Sigma},$$
where • denotes the cup-product of $H^{2}(M, \mathbb{R})$. Note that $\Omega_{\Sigma}$ is a semi-positive (1,1)-form on $(M, I)$ whose kernel, at any point of $U$, is $T \mathcal{F}$, while $F$ is a (smooth) holomorphic curve in $(M, I)$; it then follows from the above equality that, at any point $x \in U$, the fiber $F$ must be tangent to $\mathcal{F}$; since $U$ is dense in $M$, we conclude that $\mathcal{F}$ is tangent to the fibers everywhere. But as observed in [5], by replacing $M$ with a finite cover if necessary, $(M, I)$ then admits a globally defined, non-trivial holomorphic field tangent to the fibers, which is also a holomorphic section of $T \mathcal{F}$.

Suppose now that $(M, I)$ is a ruled surface over an elliptic base $B$. By the previous argument, we may also assume that $(M, I)$ does not admit any elliptic fibration. According to the the classification of non-singular holomorphic foliations (see [15, Prop.6] and [24, Sec.3]), under the above assumptions for $(M, I)$, the following two cases arise:

Case 1: $\mathcal{F}$ is tangent to the rational fibers; since $(M, I)$ is not an elliptic fibration, according to [39] we have $H^{0}(M, T \mathcal{F}) \neq 0$ as claimed.
Case 2: $\mathcal{F}$ is a foliation transversal to the rational fibers, i.e. a Riccati foliation in the terminology of [24]. In this case $c_{1}(T \mathcal{F})$ is the pull-back of a class of $H^{2}(B, \mathbb{Z})$ (see [24]), so
that $c_{1}(T \mathcal{F})$ is a multiple of the Poincaré-dual of any rational fiber $F$. Since $[F] \cdot[F]=0$ in homology and in view of (75), we then have
$$0=\frac{1}{2} \int_{F}\left(\gamma_{I}-\gamma_{J}\right)=-\frac{1}{16 \pi} \int_{F}|\nabla \Omega|^{2} \Omega_{\Sigma} .$$
Then, we conclude as in the case of elliptic fibrations that each fiber $F$ must be tangent to $\mathcal{F}$, which is a contradiction.

As a final step of the proof of Theorem 2, note that $T \mathcal{F}=D^{\perp}$ lies in the kernel of the Ricci tensor of $g$ (see (73)); then, by the well-known Bochner-Lichnerowicz argument, for any holomorphic section $\Xi$ of $T \mathcal{F} \subset T M$ we get $\nabla \Xi=0$. Since we already showed $H^{0}(M, T \mathcal{F}) \neq 0$, it follows that $T \mathcal{F}$ should be parallel, and then, so must be its orthogonal complement $D$. But then $J$ must be parallel too, a contradiction. □

Acknowledgments. The authors are grateful to O. Biquard, D. Calderbank and P. Gauduchon for their interest and stimulating discussions.

\section*{References}
\begin{itemize}
\item[] [1] B. Alexandrov, G. Grantcharov and S. Ivanov, Curvature properties of twistor spaces of quaternionic Kähler manifolds, J. Geom. 62 (1998), 1-12.
\item[] [2] V. Apostolov and J. Armstrong, Symplectic 4-manifolds with Hermitian Weyl tensor, Trans. Amer. Math. Soc. 352 (2000), 4501-4513.
\item[] [3] V. Apostolov, J. Armstrong and T. Draghici, Local rigidity of certain classes of almost Kähler 4manifolds, to appear in Ann. Glob. Anal. Geom.
\item[] [4] V. Apostolov, D. Calderbank and P. Gauduchon, The geometry of weakly selfdual Kähler surfaces, to appear in Compositio Math.
\item[] [5] V. Apostolov, T. Draghici and D. Kotschick, An integrability theorem for almost Kähler 4-manifolds, C. R. Acad. Sci. Paris 329, sér. I (1999), 413-418.
\item[] [6] V. Apostolov, T. Draghici and A. Moroianu, A splitting theorem for Kähler manifolds whose Ricci tensors have constant eigenvalues, Int. J. Math. 12 (2001), 769-789.
\item[] [7] N. Aronszajn, A unique continuation theorem for solutions of elliptic partial differential equations or inequalities of second order, J. Math. Pures Appl. 36 (1957), 235-249.
\item[] [8] J. Armstrong, On four-dimensional almost Kähler manifolds, Quart. J. Math. Oxford Ser.(2) 48 (1997), 405-415.
\item[] [9] J. Armstrong, An ansatz for Almost-Kähler, Einstein 4-manifolds, J. reine angew. Math. 542 (2002), 53-84.
\item[] [10] W.Barth, C.Peters and A.Van de Ven, Compact complex surfaces, Springer-Verlagh, Berlin Heidelberg New York Tokyo, 1984.
\item[] [11] A. L. Besse, Einstein manifolds, Ergeb. Math. Grenzgeb., Springer-Verlag, Berlin, Heidelberg, New York, 1987.
\item[] [12] D. E. Blair, The "total scalar curvature" as a symplectic invariant and related results, Proc. 3rd Congress of Geometry, Thessaloniki (1991), 79-83.
\item[] [13] D. E. Blair and S. Ianus, Critical associated metrics on symplectic manifolds, Contemp. Math. 51 (1986), 23-29.
\item[] [14] J.-P. Bourguignon, Les variétés de dimension 4 à signature non nule dont la courbure est harmonique sont d'Einstein, Invent. Math. 63 (1981), 263-286.
\item[] [15] M. Brunella, Feuilletages holomorphes sur les surfaces complexes compactes, Ann. Scient. Éc. Norm. Sup., Sér. 430 (1997), 569-594.
\item[] [16] J. Davidov and O. Muškarov, Twistor spaces with Hermitian Ricci tensor, Proc. Amer. Math. Soc. 109 (1990), 1115-1120.
\item[] [17] S. K. Donaldson, Remarks on Gauge theory, complex geometry and 4-manifolds topology, in "The Fields Medallists Lectures" (eds. M. Atiyah and D. Iagolnitzer), pp. 384-403, World Scientific, 1997.
\item[] [18] S. K. Donaldson, Symmetric spaces, Kähler geometry and Hamiltonian dynamics, in "Northern California Symplectic Geometry Seminar" (eds. Y. Eliashberg et al.), pp.13-33, American Mathematical Society, 1999.
\item[] [19] T. Draghici, On some 4-dimensional almost Kähler manifolds, Kodai Math. J. 18 (1995), 156-163.
\item[] [20] T. Draghici, Almost Kähler 4-manifolds with J-invariant Ricci tensor, Houston J. Math. 25 (1999), 133-145.
\end{itemize}
[21] P. Gauduchon, Hermitian connections and Dirac operators, Boll. U.M.I. (7) 11-B (1997), Suppl. fasc. 2, 257-288.
[22] G. Gibbons and S. Hawking, Classification of Gravitational Instanton Symmetries, Comm. Math. Phys. 66 (1979), 291-310.
[23] S. I. Goldberg, Integrability of almost Kähler manifolds, Proc. Amer. Math. Soc. 21 (1969), 96-100.
[24] X. Gómez-Mont, Holomorphic foliations in ruled surfaces, Trans. Amer. Math. Soc. 312 (1989), 179-201.
[25] A. Gray, Riemannian manifolds with geodesic symmetries of order 3. J. Differential Geom. 7 (1972), 343-369.
[26] A. Gray, Curvature identities for Hermitian and almost Hermitian manifolds, Tôhoku Math. J. 28 (1976), 601-612.
[27] M. Gromov, Pseudoholomorphic curves in symplectic manifolds, Invent. Math. 82 (1985), 307-347.
[28] D. Joyce, Explicit construction of self-dual 4-manifolds, Duke Math. J. 77 (1995), 519-552.
[29] J. Kazdan, Unique Continuation in Geometry, Comm. Pure and Appl. Math. XLI (1988), 667-681.
[30] S. Kobayashi and K. Nomizu, Foundations of differential geometry, Vol II Interscience Publishers (John Wiley Inc.) No 15, 1969.
[31] D. Kotschick, Orientations and geometrisations of compact complex surfaces, Bull. London Math. Soc. 29 (1997), 145-149.
[32] D. Kotschick, Einstein metrics and smooth structures, Geom. Topol. 2 (1998), 1-10.
[33] O. Kowalski, Generalized Symmetric Spaces, LNM 805, 1980.
[34] H.-V. Lê and G. Wang, Anti-complexified Ricci flow on compact symplectic manifolds, J. reine angew. Math. 530 (2001), 17-31.
[35] C.LeBrun, Explicit self-dual metrics on $\mathbb{C P}^{2} \sharp \ldots \sharp \mathbb{C P}^{2}$, J.Differential Geom. 34 (1991), 223-253.
[36] C.LeBrun, Four-manifolds without Einstein metrics, Math. Res. Lett. 3 (1996), 133-147.
[37] C. LeBrun, Weyl curvature, Einstein metrics, and Seiberg-Witten theory, Math. Res. Lett. 5 (1998), 423-438.
[38] C. LeBrun, Ricci curvature, minimal volumes, and Seiberg-Witten theory, Invent. Math. 145 (2001), 279-316.
[39] M. Maruyama, On automorphism groups of ruled surfaces, J. Math. Koyoto Univ. 11 (1971), 89-112.
[40] A. Newlander and L. Nirenberg, Complex analytic coordinates in almost complex manifolds, Ann. Math. 65 (1957), 391-404.
[41] P. Nurowski and M. Przanowski, A four-dimensional example of Ricci flat metric admitting almost Kähler non-Kähler structure, Classical Quantum Gravity 16 (1999), no 3, L9-L13.
[42] J. Petean, Indefinite Kähler-Einstein metrics on compact complex surfaces, Comm. Math. Phys. 189 (1997), 227-235.
[43] K. P. Tod, private communication to the second author.
[44] K. Sekigawa, On some compact Einstein almost Kähler manifolds, J. Math. Soc. Japan 36 (1987), 677-684.
[45] C.H. Taubes, The Seiberg-Witten Invariants and Symplectic Forms, Math. Res. Lett. 1 (1994), 809-822.
[46] C.H. Taubes, The Seiberg-Witten and Gromov Invariants, Math. Res. Lett. 2 (1995), 221-238.
[47] F. Tricerri and L. Vanhecke, Curvature tensors on almost Hermitian manifolds, Trans. Amer. Math. Soc. 267 (1981), 365-398.
[48] C. Wood, Harmonic almost-complex structures, Compositio Math. 99 (1995), 183-212.
Vestislav Apostolov, Département de mathématiques, UQAM, succursale Centre-ville c.p. 8888, Montréal, H3C 3P8, Canada
E-mail address: apostolo@math.uqam.ca
John Armstrong, 21 Alford House, Stanhope Rd, London, N6 5AL, UK
E-mail address: John.Armstrong@yolus.com
Tedi Drăghici, Department of Mathematics, Florida International University, Miami FL 33199, USA
E-mail address: draghici@fiu.edu