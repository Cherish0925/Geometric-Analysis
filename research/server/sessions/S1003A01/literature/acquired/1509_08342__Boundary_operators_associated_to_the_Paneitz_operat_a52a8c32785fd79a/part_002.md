---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: [1509.08342] Boundary operators associated to the Paneitz operator]

Proposition 6.7. Let $\left(X^{4}, M^{3}, g_{+}\right)$be a Poincaré-Einstein manifold with $2 \notin$ $\sigma_{p p}\left(-\Delta_{g_{+}}\right)$and let $h$ be a representative of the conformal boundary. Then $\mathcal{T}_{3}^{3}=Q_{3}$.

Proof. Let $r$ be the geodesic defining function associated to $h$. Let $v$ be the unique solution to $-\Delta_{g_{+}} v=3$ with
$$v=\log r+A+B r^{3}$$
for $A, B \in C^{\infty}(X)$ even in $r$ and $\left.A\right|_{M}=0$. Since $\left(L_{4}\right)_{g_{+}}=\Delta_{g_{+}}^{2}+2 \Delta_{g_{+}}$, it also holds that $\left(L_{4}\right)_{g_{+}} v+6=0$. By definition [21], $Q_{3}=\left.3 B\right|_{M}$.

Consider now the compactified metric $g=r^{2} g_{+}$. It follows from the conformal transformation formulae for $Q_{4}$ and $L_{4}$, the evenness of $A$ in $r$, and the fact that $M$ is minimal with respect to $g$ that $v-\log r$ solves (6.1). Note that $\operatorname{ker} L_{4} \cap \operatorname{ker} B_{0}^{3} \cap$ $\operatorname{ker} B_{1}^{3}=\{0\}$ since $2 \notin \sigma_{p p}\left(-\Delta_{g_{+}}\right)$. Hence, by Proposition 6.1
$$\mathcal{T}_{3}^{3}=\frac{1}{2}\left(T_{3}^{3}+B_{3}^{3}(v-\log r)\right) .$$
By direct computation, $T_{3}^{3}=0$ and $B_{3}^{3}(v-\log r)=\left.6 B\right|_{M}$. \(\square\)

In the setting of four-manifolds with boundary, the Paneitz operator and its boundary operators are related to the functionals $\mathcal{F}, \mathcal{G}: C^{\infty} \rightarrow \mathbb{R}$ defined by
$$\begin{aligned}
\mathcal{F}(u) & =\int_{X}\left(u L_{4} u+2 Q_{4} u\right)+\oint_{M}\left(f B_{3}^{3} u+2 T_{3}^{3} f+\psi B_{2}^{3} u+2 T_{2}^{3} \psi\right), \\
\mathcal{G}(u) & =\oint_{M}\left(B_{1}^{3}(u) B_{2}^{3}(u)+T_{2}^{3} B_{1}^{3}(u)+T_{1}^{3} B_{2}^{3}(u)\right) .
\end{aligned}$$
for $f=B_{0}^{3} u$ and $\psi=B_{1}^{3} u$. These constitute two of the integrals which naturally arise in log determinant formulas in this setting. More precisely, Chang and Qing showed [15] that the log determinant can be written as a linear combination of eleven functionals, one of which is $b_{2}+\frac{1}{12} D$, where
$$\begin{aligned}
b_{2}(u) & =\frac{1}{4} \int_{X}\left(u L_{4} u+2 Q_{4} u\right)+\frac{1}{2} \oint_{M}\left(f P_{3} u+2 T f\right), \\
D(u) & =\oint_{M} P_{3}^{2} u
\end{aligned}$$
for $u \in C^{\infty}(X)$, where $f=B_{0}^{3} u$. These functionals are defined precisely as they appear in [15, Theorem 3.3]. As an immediate consequence of Lemma 6.3, we find that $b_{2}+\frac{1}{12} D$ differs from a particular combination of $\mathcal{F}$ and $\mathcal{G}$ by integration against pointwise conformal invariants.

Corollary 6.8. Let $\left(X^{4}, g\right)$ be a compact Riemannian manifold with boundary $M^{3}=\partial X$. Then
$$4 b_{2}(u)+\frac{1}{3} D(u)=\mathcal{F}(u)-\mathcal{G}(u)+\oint_{M}\left[\frac{1}{4}\left|A_{0}\right|^{2} \psi-8\left(\left\langle W(\eta, \cdot, \eta, \cdot), A_{0}-\frac{2}{3} \operatorname{tr} A_{0}^{3}\right) f\right]\right.$$
for all $u \in C^{\infty}(X)$, where $f=B_{0}^{3} u$ and $\psi=B_{1}^{3} u$.
One reason to regard the $\mathcal{F}$ - and $\mathcal{G}$-functionals as natural components of the log determinant functional is that they independently satisfy the following "cocycle" condition (cf. [11]).

Proposition 6.9. Let $\left(X^{4}, g\right)$ be a compact Riemannian manifold with boundary $M^{3}=\partial X$. Given any $u, v \in C^{\infty}(X)$ it holds that
$$\begin{aligned}
\widehat{\mathcal{F}}(v) & =\mathcal{F}(u+v)-\mathcal{F}(u), \\
\widehat{\mathcal{G}}(v) & =\mathcal{G}(u+v)-\mathcal{G}(u),
\end{aligned}$$
where $\widehat{\mathcal{F}}$ and $\widehat{\mathcal{G}}$ are defined in terms of the metric $\widehat{g}=e^{2 u} g$.
Proof. This is an immediate consequence of Theorem 1.1 and Proposition 6.1 \(\square\)

The cocycle condition allows one to readily identify the geometric significance of critical points of the underlying functional.

Proposition 6.10. Let $\left(X^{4}, g\right)$ be a compact Riemannian manifold with boundary $M^{3}=\partial X$ and set
$$[g]_{1, M}=\left\{u \in C^{\infty}(X) \mid \oint_{M} e^{3 f}=1, \text { where } f=B_{0}^{3} u\right\} .$$
Suppose that $u \in[g]_{1, M}$ is a critical point of $\mathcal{F}:[g]_{1, M} \rightarrow \mathbb{R}$. Then the metric $\widehat{g}=e^{2 u} g$ is such that
$$\left\{\begin{array}{l}
\operatorname{Vol}_{\widehat{h}}(M)=1, \\
\widehat{Q}_{4}=0, \\
\widehat{T}_{2}^{3}=0, \\
\widehat{T}_{3}^{3}=\int Q_{4}+\oint T_{3}^{3} .
\end{array}\right.$$
Remark 6.11. By imposing the additional constraint $B_{1}^{3} u=0$, we obtain that the metric $\widehat{g}$ associated to a critical point $u$ satisfies $\widehat{T}_{1}^{3}=0$ instead of $\widehat{T}_{2}^{3}=0$.

Proof. Note that $[g]_{1, M}$ consists of all functions $u \in C^{\infty}(X)$ such that $M$ has unit volume with respect to $\widehat{h}=e^{2 f} h$. Let $v \in C^{\infty}(X)$ be such that $\oint B_{0}^{3}(v) e^{3 f}=0$. It follows from Proposition 6.9 that
$$0=\left.\frac{1}{2} \frac{d}{d t}\right|_{t=0} \mathcal{F}(u+t v)=\int_{X} \widehat{Q}_{4} v+\oint_{M}\left(\widehat{T}_{3}^{3} \widehat{B}_{0}^{3}(v)+\widehat{T}_{2}^{3} \widehat{B}_{1}^{3}(v)\right) .$$
We thus conclude that $\widehat{Q}_{4}=0=\widehat{T}_{2}^{3}$ and that $\widehat{T}_{3}^{3}$ is constant. By Corollary 6.2. this constant must be $\int Q_{4}+\oint T_{3}^{3}$. \(\square\)

The situation for the $\mathcal{G}$-functional is more subtle. Since the $\mathcal{G}$-functional depends only on the values of $u$ in a neighborhood of the boundary, it is easy to see that its critical points correspond to conformal metrics with vanishing $T_{2}^{3}$ - and $T_{3}^{3}$ -curvature. A more interesting Euler equation is obtained by restricting to Paneitz-harmonic functions on a Poincaré-Einstein manifold.

Proposition 6.12. Let $\left(X^{4}, g\right)$ be a conformal compactification of a Poincaré-Einstein manifold $\left(X^{4}, M^{3}, g_{+}\right)$. Suppose that $u \in \operatorname{ker} L_{4}$ is a critical point of $\mathcal{G}: \operatorname{ker} L_{4} \rightarrow \mathbb{R}$. Then the metric $\widehat{g}=e^{2 u} g$ is such that
$$2 \widehat{\mathcal{B}}_{1}^{3} \widehat{T}_{1}^{3}+\widehat{T}_{2}^{3}=0 .$$
Remark 6.13. The conclusion remains true if ( $X^{4}, g$ ) has the property that if $u \in$ $\operatorname{ker} L_{4} \cap \operatorname{ker} B_{1}^{3}$, then $B_{2}^{3} u=0$. By Lemma 4.3, this property ensures that $\mathcal{B}_{1}^{3}$ is well-defined without prescribing $B_{0}^{3} u$. The conclusion is also true for general compact Riemannian four-manifolds with boundary if $\mathcal{G}$ is restricted to $\operatorname{ker} L_{4} \cap \operatorname{ker} B_{0}^{3}$.

Proof. Let $v \in \operatorname{ker} L_{4}$. It follows from Proposition 6.9 that
$$0=\left.\frac{d}{d t}\right|_{t=0} \mathcal{G}(u+t v)=\oint_{M}\left(\widehat{T}_{2}^{3} \widehat{B}_{1}^{3}(v)+\widehat{T}_{1}^{3} \widehat{B}_{2}^{3}(v)\right) .$$
Set $\widehat{\psi}=\widehat{B}_{1}^{3}(v)$. By Theorem 1.4, it holds that $\widehat{B}_{2}^{3}(v)=2 \widehat{\mathcal{B}}_{1}^{3}(\widehat{\psi})$. Therefore
$$0=\oint_{M}\left(\widehat{T}_{2}^{3} \widehat{\psi}+2 \widehat{T}_{1}^{3} \widehat{\mathcal{B}}_{1}^{3}(\widehat{\psi})\right)=\oint_{M}\left(\widehat{T}_{2}^{3}+2 \widehat{\mathcal{B}}_{1}^{3} \widehat{T}_{1}^{3}\right) \widehat{\psi} .$$
Since $\widehat{\psi}$ is arbitrary, (6.3) holds. \(\square\)

We now restrict our attention to the $\mathcal{F}$-functional; with regards to geometric curvature prescription problems, comparison of Proposition 1.2 and Proposition 6.10 shows that the $\mathcal{F}$-functional should be regarded as the four-dimensional analogue of the volume-normalized energy functional $\mathcal{E}_{4}$. Pursuing this analogy further, one approach to constructing conformal metrics which satisfy (6.2) is to extremize
$$\mu_{4,2}(X, M, g)=\inf \left\{\mathcal{F}(u) \mid u \in C^{\infty}(X), \oint_{M} e^{3 u}=1\right\} .$$
This can be regarded as the four-dimensional analogue of $Y_{4,2}(X, M)$, though $\mu(X, M, g)$ is not a conformal invariant: It follows from Proposition 6.9 that
$$\mu_{4,2}\left(X, M, e^{2 v} g\right)=\mu_{4,2}(X, M, g)-\mathcal{F}(v) .$$
One can analogously define $\mu_{4,1}(X, M, g)$ by requiring also that $u \in \operatorname{ker} B_{1}^{3}$, with similar properties.

An initial step towards extremizing $\mu_{4,2}(X, M, g)$ is to compute the corresponding value and identify the extremal functions in the model space, namely the round upper hemisphere $\left(S_{+}^{4}, d \theta^{2}\right)$ (cf. [17]). Like Theorem 1.6 in higher dimensions, this result follows from Proposition 1.3 and the sharp fractional Sobolev inequalities on the round spheres [5]. The corresponding result for $\mu_{4,1}$ was recently proven by Ache and Chang [1].

Theorem 6.14. Let $\left(S_{+}^{4}, d \theta^{2}\right)$ be the four-dimensional upper hemisphere with the round metric. Given any $u \in C^{\infty}\left(S_{+}^{4}\right)$, it holds that
$$\int_{S_{+}^{4}}\left((\Delta u)^{2}+2|\nabla u|^{2}\right) \geq 4 \oint_{S^{3}} \psi \bar{\Delta} f+\frac{16 \pi^{2}}{3} \log \left(\frac{1}{2 \pi^{2}} \oint_{S^{3}} e^{f-\bar{f}}\right)+\left(4 \pi \oint_{S^{3}}|\psi|^{3}\right)^{\frac{2}{3}},$$
where $f=B_{0}^{3} u, \psi=B_{1}^{3}$, and $\bar{f}=\frac{1}{2 \pi^{2}} \oint f$. Moreover, equality holds if and only if $L_{4} u=0, f(x)=a_{1}+\ln \left(1+x \cdot \xi_{1}\right)$ and $\psi(x)=a_{2}\left(1+x \cdot \xi_{2}\right)^{-1}$ for constants $a_{1}, a_{2} \in \mathbb{R}$ and points $\xi_{1}, \xi_{2} \in B_{1}(0)$.

Proof. By Proposition 1.3, it holds that
$$\mathcal{E}_{4}(u) \geq 2 \oint_{S_{3}}\left(f P_{3} f+\psi P_{1} \psi\right)$$
with equality if and only if $L_{4} u=0$. On the other hand, Beckner [5] showed that
$$\begin{aligned}
& \oint_{S^{3}} f P_{3} f \geq \frac{8 \pi^{2}}{3} \log \left(\frac{1}{2 \pi^{2}} \oint_{S^{3}} e^{f-\bar{f}}\right), \\
& \oint_{S^{3}} \psi P_{1} \psi \geq\left(2 \pi^{2}\right)^{1 / 3}\left(\oint_{S^{3}}|\psi|^{3}\right)^{\frac{2}{3}}
\end{aligned}$$
with equality if and only if $f(x)=a_{1}+\ln \left(1+x \cdot \xi_{1}\right)$ and $\psi(x)=a_{2}\left(1+x \cdot \xi_{2}\right)^{-1}$ for constants $a_{1}, a_{2} \in \mathbb{R}$ and points $\xi_{1}, \xi_{2} \in B_{1}(0)$. Combining these inequalities with the formula for the energy $\mathcal{E}_{4}$ on the round upper hemisphere yields the result. \(\square\)

In fact, the extremizing functions $u \in C^{\infty}\left(S_{+}^{4}\right)$ can be written down explicitly, and they correspond to conformal factors for the adapted metrics [13] associated to the Einstein metrics on $S^{3}$; for details, see 1.

\section*{References}
\begin{itemize}
\item[] [1] A. G. Ache and S.-Y. A. Chang. Sobolev-trace inequalities of order four. arXiv:1509.06069, preprint.
\item[] [2] S. Agmon, A. Douglis, and L. Nirenberg. Estimates near the boundary for solutions of elliptic partial differential equations satisfying general boundary conditions. II. Comm. Pure Appl. Math., 17:35-92, 1964.
\item[] [3] S. d. M. Almaraz. An existence theorem of conformal scalar-flat metrics on manifolds with boundary. Pacific J. Math., 248(1):1-22, 2010.
\item[] [4] M. T. Anderson. $L^{2}$ curvature and volume renormalization of AHE metrics on 4-manifolds. Math. Res. Lett., 8(1-2):171-188, 2001.
\item[] [5] W. Beckner. Sharp Sobolev inequalities on the sphere and the Moser-Trudinger inequality. Ann. of Math. (2), 138(1):213-242, 1993.
\item[] [6] T. Branson. Spectral theory of invariant operators, sharp inequalities, and representation theory. In The Proceedings of the 16th Winter School "Geometry and Physics" (Srní, 1996), number 46, pages 29-54, 1997.
\item[] [7] T. Branson and A. R. Gover. Conformally invariant non-local operators. Pacific J. Math., 201(1):19-60, 2001.
\item[] [8] T. P. Branson. Differential operators canonically associated to a conformal structure. Math. Scand., 57(2):293-345, 1985.
\item[] [9] T. P. Branson. Sharp inequalities, the functional determinant, and the complementary series. Trans. Amer. Math. Soc., 347(10):3671-3742, 1995.
\item[] [10] T. P. Branson and P. B. Gilkey. The functional determinant of a four-dimensional boundary value problem. Trans. Amer. Math. Soc., 344(2):479-531, 1994.
\item[] [11] T. P. Branson and A. R. Gover. Origins, applications and generalisations of the $Q$-curvature. Acta Appl. Math., 102(2-3):131-146, 2008.
\item[] [12] L. Caffarelli and L. Silvestre. An extension problem related to the fractional Laplacian. Comm. Partial Differential Equations, 32(7-9):1245-1260, 2007.
\item[] [13] J. S. Case and S.-Y. A. Chang. On fractional GJMS operators. Comm. Pure Appl. Math., to appear.
\item[] [14] S.-Y. A. Chang and M. d. M. González. Fractional Laplacian in conformal geometry. Adv. Math., 226(2):1410-1432, 2011.
\item[] [15] S.-Y. A. Chang and J. Qing. The zeta functional determinants on manifolds with boundary. I. The formula. J. Funct. Anal., 147(2):327-362, 1997.
\item[] [16] S.-Y. A. Chang, J. Qing, and P. Yang. On the renormalized volumes for conformally compact Einstein manifolds. J. Math. Sciences (N. Y.), 149(6):1755-1769, 2008.
\item[] [17] S.-Y. A. Chang and P. C. Yang. Extremal metrics of zeta function determinants on 4-manifolds. Ann. of Math. (2), 142(1):171-212, 1995.
\item[] [18] J. F. Escobar. Sharp constant in a Sobolev trace inequality. Indiana Univ. Math. J., 37(3):687-698, 1988.
\item[] [19] J. F. Escobar. Conformal deformation of a Riemannian metric to a scalar flat metric with constant mean curvature on the boundary. Ann. of Math. (2), 136(1):1-50, 1992.
\item[] [20] J. F. Escobar. Addendum: "Conformal deformation of a Riemannian metric to a scalar flat metric with constant mean curvature on the boundary" [Ann. of Math. (2) 136 (1992), no. 1, 1-50; MR1173925 (93e:53046)]. Ann. of Math. (2), 139(3):749-750, 1994.
\item[] [21] C. Fefferman and C. R. Graham. $Q$-curvature and Poincaré metrics. Math. Res. Lett., 9(2-3):139-151, 2002.
\item[] [22] C. Fefferman and C. R. Graham. The ambient metric, volume 178 of Annals of Mathematics Studies. Princeton University Press, Princeton, NJ, 2012.
\end{itemize}
\begin{itemize}
\item[] [23] A. R. Gover. Conformal Dirichlet-Neumann maps and Poincaré-Einstein manifolds. SIGMA Symmetry Integrability Geom. Methods Appl., 3:Paper 100, 21, 2007.
\item[] [24] A. R. Gover and L. J. Peterson. Conformal hypersurfaces, boundary operators, and related curvatures. In preparation.
\item[] [25] C. R. Graham and M. Zworski. Scattering matrix in conformal geometry. Invent. Math., 152(1):89-118, 2003.
\item[] [26] D. H. Grant. A conformally invariant third order Neumann-type operator for hypersurfaces. Master's thesis, The University of Auckland, 2003.
\item[] [27] C. Guillarmou and L. Guillopé. The determinant of the Dirichlet-to-Neumann map for surfaces with boundary. Int. Math. Res. Not. IMRN, (22):Art. ID rnm099, 26, 2007.
\item[] [28] A. Juhl. Families of conformally covariant differential operators, $Q$-curvature and holography, volume 275 of Progress in Mathematics. Birkhäuser Verlag, Basel, 2009.
\item[] [29] H. Kumano-go. Pseudodifferential operators. MIT Press, Cambridge, Mass.-London, 1981. Translated from the Japanese by the author, Rémi Vaillancourt and Michihiro Nagase.
\item[] [30] E. H. Lieb. Sharp constants in the Hardy-Littlewood-Sobolev and related inequalities. Ann. of Math. (2), 118(2):349-374, 1983.
\item[] [31] F. C. Marques. Existence results for the Yamabe problem on manifolds with boundary. Indiana Univ. Math. J., 54(6):1599-1620, 2005.
\item[] [32] F. C. Marques. Conformal deformations to scalar-flat metrics with constant mean curvature on the boundary. Comm. Anal. Geom., 15(2):381-405, 2007.
\item[] [33] S. M. Paneitz. A quartic conformally covariant differential operator for arbitrary pseudo-Riemannian manifolds (summary). SIGMA Symmetry Integrability Geom. Methods Appl., 4:Paper 036, 3, 2008.
\item[] [34] R. C. Reilly. Applications of the Hessian operator in a Riemannian manifold. Indiana Univ. Math. J., 26(3):459-472, 1977.
\item[] [35] F. Robert. Fourth order equations with critical growth in Riemannian geometry. Notes from lectures given at Madison and Berlin (unpublished), 2009, available at http://www.iecn.unancy.fr/ frobert/LectRobertFourth.pdf.
\item[] [36] R. Stafford. Tractor calculus and invariants for conformal sub-manifolds. Master's thesis, The University of Auckland, 2006.
\item[] [37] F. Trèves. Introduction to pseudodifferential and Fourier integral operators. Vol. 1. Plenum Press, New York-London, 1980. Pseudodifferential operators, The University Series in Mathematics.
\item[] [38] R. Yang. On higher order extensions for the fractional Laplacian. arXiv:1302.4413, Preprint.
\end{itemize}

109 McAllister Building, Penn State University, University Park, PA 16801
E-mail address: jscase@psu.edu