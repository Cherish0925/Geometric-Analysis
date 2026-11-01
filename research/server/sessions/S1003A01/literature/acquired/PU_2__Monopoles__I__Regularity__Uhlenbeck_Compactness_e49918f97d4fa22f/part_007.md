---
retention_scope: session
part: 7
total_parts: 7
---

[Part 7/7 of: PU(2) Monopoles, I: Regularity, Uhlenbeck Compactness ...]

Since $\Delta_{A}=d_{A}^{*} d_{A}$, its derivative with respect to $A$ in the direction $\delta A=a$ is given by $\delta \Delta_{A}=[a, \cdot]^{*} d_{A}+d_{A}^{*}[a, \cdot]$; we use the abbreviation $\delta \Delta_{A}=\left(D \Delta_{(\cdot)}\right)_{A}(a)$. The connection $A_{0}$ is irreducible by hypothesis and so for a small enough open $L_{k}^{2}$ ball $B\left(A_{0}, r_{0}\right)$, there is a positive constant $\lambda_{0}>0$ such that $\lambda[A] \geq \lambda_{0}>0$ for all $A \in B\left(A_{0}, r_{0}\right)$, where $\lambda[A]$ is the least eigenvalue of $\Delta_{A}$. Thus,
$$\operatorname{Spec}\left(\Delta_{A}\right) \subset\left[\lambda_{0}, \infty\right), \quad A \in B\left(A_{0}, r_{0}\right),$$
and, for any holomorphic function $f$ on an open neighborhood $\Omega \subset \mathbb{C}$ with $\operatorname{Spec}\left(\Delta_{A}\right) \subset$ $\Omega$ and $\Gamma$ any contour that surrounds $\operatorname{Spec}\left(\Delta_{A}\right)$ in $\Omega$, we have [76]
$$\begin{aligned}
f\left(\Delta_{A}\right) & =\frac{1}{2 \pi i} \oint_{\Gamma} f(\lambda)\left(\lambda-\Delta_{A}\right)^{-1} d \lambda \\
(D f)_{\Delta_{A}}\left(\delta \Delta_{A}\right) & =\frac{1}{2 \pi i} \oint_{\Gamma} f(\lambda)\left(\lambda-\Delta_{A}\right)^{-1}\left(\delta \Delta_{A}\right)\left(\lambda-\Delta_{A}\right)^{-1} d \lambda,
\end{aligned}$$
and similarly for all higher-order derivatives. Note that
$$\begin{aligned}
& \left(1+\Delta_{A}\right)^{(k+1) / 2} f\left(\Delta_{A}\right) \\
& \quad=\frac{1}{2 \pi i} \oint_{\Gamma}(1+\lambda)^{(k+1) / 2} f(\lambda)\left(\lambda-\Delta_{A}\right)^{-1} d \lambda, \\
& \left(1+\Delta_{A}\right)^{(k+1) / 2}(D f)_{\Delta_{A}}\left(\delta \Delta_{A}\right) \\
& \quad=\frac{1}{2 \pi i} \oint_{\Gamma}(1+\lambda)^{(k+1) / 2} f(\lambda)\left(\lambda-\Delta_{A}\right)^{-1}\left(\delta \Delta_{A}\right)\left(\lambda-\Delta_{A}\right)^{-1} d \lambda .
\end{aligned}$$
We can fix $\Omega$ and $\Gamma \subset \Omega$ such that $\operatorname{dist}\left(\Gamma, \operatorname{Spec}\left(\Delta_{A}\right)\right) \geq d_{0}>0$, for some positive constant $d_{0}$ and all $A \in B\left(A_{0}, r_{0}\right)$ (see [34, §1.6]). Now choose $f(z)=e^{-t z}$ and $f_{k+1}(z)=(1+z)^{(k+1) / 2} f(z)$, and estimate as in [34, p. 53]:
$$\begin{aligned}
\left\|e^{-t \Delta_{A}} \eta\right\|_{L_{k+1, A}^{2}(Y)} & \leq c\left\|\left(1+\Delta_{A}\right)^{(k+1) / 2} e^{-t \Delta_{A}} \eta\right\|_{L^{2}(Y)} \\
& \leq c \oint_{\Gamma}\left|(1+\lambda)^{(k+1) / 2} e^{-t \lambda} d \lambda\right| \sup _{\lambda \in \Gamma}\left\|\left(\lambda-\Delta_{A}\right)^{-1} \eta\right\|_{L^{2}(Y)} \\
& \leq c\|\eta\|_{L^{2}(Y)},
\end{aligned}$$
which gives the desired $C^{0}$ bound
$$\sup _{A \in B\left(A_{0}, r_{0}\right)}\left\|e^{-t \Delta_{A}} \eta\right\|_{L_{k+1, A}^{2}(Y)} \leq c\|\eta\|_{L^{2}(Y)},$$
where $c=c\left(d_{0}, k, r_{0}, t\right)$.
To obtain the $C^{1}$ bound, observe that
$$\begin{aligned}
& \left\|(D f)_{\Delta_{A}}\left(\delta \Delta_{A}\right) \eta\right\|_{L_{k+1, A}^{2}(Y)} \\
& \leq c\left\|\left(1+\Delta_{A}\right)^{(k+1) / 2}(D f)_{\Delta_{A}}\left(\delta \Delta_{A}\right) \eta\right\|_{L^{2}(Y)} \\
& \leq c \oint_{\Gamma}\left|(1+\lambda)^{(k+1) / 2} f(\lambda) d \lambda\right| \sup _{\lambda \in \Gamma}\left\|\left(\lambda-\Delta_{A}\right)^{-1}\left(\delta \Delta_{A}\right)\left(\lambda-\Delta_{A}\right)^{-1} \eta\right\|_{L^{2}(Y)} \\
& \leq \sup _{\lambda \in \Gamma} c\left\|\left(\lambda-\Delta_{A}\right)^{-1}\left(\delta \Delta_{A}\right)\left(\lambda-\Delta_{A}\right)^{-1} \eta\right\|_{L^{2}(Y)} .
\end{aligned}$$

Our expression for $\delta \Delta_{A}$ gives
$$\begin{aligned}
& \left\|\left(\lambda-\Delta_{A}\right)^{-1}\left(\delta \Delta_{A}\right)\left(\lambda-\Delta_{A}\right)^{-1} \eta\right\|_{L^{2}(Y)} \\
& \leq\left\|\left(\lambda-\Delta_{A}\right)^{-1}\left([a, \cdot]^{*} d_{A}+d_{A}^{*}[a, \cdot]\right)\left(\lambda-\Delta_{A}\right)^{-1} \eta\right\|_{L^{2}(Y)} \\
& \leq c\left(\left\|[a, \cdot]^{*} d_{A}\left(\lambda-\Delta_{A}\right)^{-1} \eta\right\|_{L^{2}(Y)}+\left\|d_{A}^{*}[a, \cdot]\left(\lambda-\Delta_{A}\right)^{-1} \eta\right\|_{L^{2}(Y)}\right) \\
& \leq c\|a\|_{L_{2 ; A}^{2}(Y)}\left\|\left(\lambda-\Delta_{A}\right)^{-1} \eta\right\|_{L_{2 ; A}^{2}(Y)} \\
& \leq c\|a\|_{L_{k, A}^{2}(Y)}\|\eta\|_{L^{2}(Y)},
\end{aligned}$$
where $c=c\left(r_{0}, d_{0}\right)$. Combining these estimates yields
$$\left\|\delta\left(e^{-t \Delta_{A}}\right) \eta\right\|_{L_{k+1, A}^{2}(Y)} \leq c\|a\|_{L_{k, A}^{2}(Y)}\|\eta\|_{L^{2}(Y)},$$
and so we have the desired $C^{1}$ bound
$$\sup _{A \in B\left(A_{0}, r_{0}\right)} \sup _{\|a\|_{L_{k, A}^{2}(X)} \leq 1}\left\|\left(D e^{-t \Delta_{(\cdot)}}\right)_{A}(a) \eta\right\|_{L_{k+1, A}^{2}(Y)} \leq c\|\eta\|_{L^{2}(Y)} .$$
for some $c=c\left(d_{0}, k, r_{0}, t\right)$. The analysis can be repeated, essentially unchanged, for all higher differentials and is left to the reader. \(\square\)

Lemma A.16. The $\mathcal{G}_{E}$ equivariant holonomy maps
$$\mathfrak{m}_{j, l, \alpha}: \mathcal{A}_{E}(X) \rightarrow L_{k+1}^{2}(X, \mathfrak{s} \mathfrak{u}(E))$$
of (2.20) are $C^{\infty}$ with bounded differentials of all orders in the sense of (A.10).
Proof. Recall from (2.17) and (2.20) that
$$\begin{aligned}
\mathfrak{m}_{j, l, \alpha}(A) & =\beta_{j}[A] \chi_{j, \alpha}\left[\left.A\right|_{B\left(x_{j}, 2 R_{0}\right)}\right] \varphi_{j} \mathfrak{h}_{\gamma_{j, l, \alpha}}(A), \\
\varphi_{j} \mathfrak{h}_{\gamma_{j, l, \alpha}}(A) & =\varphi_{j} K_{t}\left(\left.A\right|_{B\left(x_{0}, 2 R_{0}\right)}\right) \hat{\mathfrak{h}}_{\gamma_{j, l, \alpha}}(A) .
\end{aligned}$$
The cutoff functions $\chi_{j, \alpha} \circ \pi \circ r_{B\left(x_{j}, 2 R_{0}\right)}: \mathcal{A}_{E}(X) \rightarrow[0,1]$ have bounded differentials of all orders, in the sense of (A.8), by the remarks following Proposition A.12; moreover, they are supported in $\mathcal{A}_{E}^{*}(X)$. The the functions $\beta_{j}: \mathcal{A}_{E}(X) \rightarrow[0,1]$ have bounded differentials of all orders, as is clear from their definition in (2.18). Finally, one can see from the proofs of Lemmas A. 3 and A.4, together with Lemma A.15, that the maps
$$\varphi_{j} K_{t}\left(\left.\cdot\right|_{B\left(x_{0}, 2 R_{0}\right)}\right) \hat{\mathfrak{h}}_{\gamma_{j, l, \alpha}}: \mathcal{A}_{E}^{*}(X) \rightarrow L_{k+1}^{2}(X, \mathfrak{s} \mathfrak{u}(E))$$
have bounded differentials of all orders in the sense of (A.10) on open subsets $\mathcal{G}_{E} \cdot$ $\mathbf{B}\left(A_{0}, r_{0}\right) \subset \mathcal{A}_{E}^{*}(X)$, where $\mathbf{B}\left(A_{0}, r_{0}\right)$ is an open $L_{k}^{2}$ ball in $\mathbf{K}_{A_{0}} \subset \mathcal{A}_{E}^{*}(X)$. \(\square\)

Given Lemma A.16, we have
$$M_{\alpha, s}:=\max _{j, l}\left\|\mathfrak{m}_{j, \alpha, l}\right\|_{C^{s}\left(\mathcal{A}_{E}\right)}<\infty,$$
where we recall that $1 \leq l \leq 3$ and $1 \leq j \leq N_{b}$. Now choose a sequence of positive weights $\delta=\left(\delta_{\alpha}\right)_{\alpha=1}^{\infty} \in \ell^{\infty}\left(\mathbb{R}^{+}\right)$by setting
$$\delta_{\alpha}:=\left(1+\max _{0 \leq s \leq \alpha} M_{\alpha, s}\right)^{-1}, \quad \alpha \in \mathbb{N},$$
and suppose $\vec{\vartheta} \in \ell_{\delta}^{1}\left(\mathbb{A}, C^{r}(X)\right)$. Then
$$\|\vec{\vartheta}\|_{\ell_{\delta}^{1}\left(C^{r}(X)\right)}=\sum_{j, l, \alpha} \delta_{\alpha}^{-1}\left\|\vartheta_{j, l, \alpha}\right\|_{C^{r}(X)}<\infty,$$
and therefore,
$$\begin{aligned}
\|\vec{\vartheta} \cdot \overrightarrow{\mathfrak{m}}\|_{C^{s}\left(\mathcal{A}_{E}\right)} & \leq \sum_{j, l, \alpha}\left\|\vartheta_{j, l, \alpha} \mathfrak{m}_{j, l, \alpha}\right\|_{C^{s}\left(\mathcal{A}_{E}\right)} \\
& \leq c \sum_{j, l, \alpha}\left\|\vartheta_{j, l, \alpha}\right\|_{L_{k+1}^{2}(X)}\left\|\mathfrak{m}_{j, l, \alpha}\right\|_{C^{s}\left(\mathcal{A}_{E}\right)} \quad \text { by (A.10) } \\
& \leq c \sum_{j, l, \alpha}\left\|\vartheta_{j, l, \alpha}\right\|_{C^{r}(X)} M_{\alpha, s},
\end{aligned}$$
since $r \geq k+1$. Here, $c=c(g, k)$ is a universal positive constant coming from the continuous Sobolev multiplication $L_{k+1}^{2} \times L_{k+1, A}^{2} \rightarrow L_{k+1, A}^{2}$. Hence, using the facts that $M_{\alpha, s} \leq 1+\max _{0 \leq t \leq \alpha} M_{\alpha, t}=\delta_{\alpha}^{-1}$ for $\alpha \geq s$ and $1 \leq \delta_{\alpha}^{-1}$ for $1 \leq \alpha \leq s-1$, we get
$$\begin{aligned}
\|\vec{\vartheta} \cdot \overrightarrow{\mathfrak{m}}\|_{C^{s}\left(\mathcal{A}_{E}\right)} & \leq c \sum_{j, l}\left(\sum_{\alpha=1}^{s-1} M_{\alpha, s}\left\|\vartheta_{j, l, \alpha}\right\|_{C^{r}(X)}+\sum_{\alpha \geq s} \delta_{\alpha}^{-1}\left\|\vartheta_{j, l, \alpha}\right\|_{C^{r}(X)}\right) \\
& \leq c\left(1+\max _{1 \leq \alpha \leq s-1} M_{\alpha, s}\right) \sum_{j, l}\left(\sum_{\alpha=1}^{s-1}\left\|\vartheta_{j, l, \alpha}\right\|_{C^{r}(X)}+\sum_{\alpha \geq s} \delta_{\alpha}^{-1}\left\|\vartheta_{j, l, \alpha}\right\|_{C^{r}(X)}\right) \\
& \leq c\left(1+\max _{1 \leq \alpha \leq s-1} M_{\alpha, s}\right) \sum_{j, l, \alpha} \delta_{\alpha}^{-1}\left\|\vartheta_{j, l, \alpha}\right\|_{C^{r}(X)} \\
& =C\|\vec{\vartheta}\|_{\ell_{\delta}^{1}\left(C^{r}(X)\right)}<\infty,
\end{aligned}$$
where $C=C(g, s, k)$ is defined by the last equality above. In particular, we see that $\vec{\vartheta} \cdot \overrightarrow{\mathfrak{m}}$ is a $C^{s}$ map on $\mathcal{A}_{E}(X)$, for every integer $s \geq 0$. The same argument gives
$$\|\vec{\tau} \cdot \overrightarrow{\mathfrak{m}}\|_{C^{s}\left(\mathcal{A}_{E}\right)} \leq C\|\vec{\tau}\|_{\ell_{\delta}^{1}\left(C^{r}(X)\right)}<\infty,$$
and $\vec{\tau} \cdot \overrightarrow{\mathfrak{m}}$ is a $C^{s}$ map on $\mathcal{A}_{E}(X)$, for every integer $s \geq 0$. \(\square\)

\section*{References}
\begin{itemize}
\item[] [1] R. Abraham, J. E. Marsden, and T. Ratiu, Manifolds, Tensor Analysis, and Applications, 2nd ed., Springer, New York, 1988.
\item[] [2] R. A. Adams, Sobolev Spaces, Academic Press, Orlando, FL, 1975.
\end{itemize}
\begin{itemize}
\item[] [3] S. Agmon, Unicité et convexité dans les problèmes differentiels, Sem. Math. Sup., 1965, Univ. of Montreal Press, 1966.
\item[] [4] S. Agmon and L. Nirenberg, Lower bounds and uniqueness theorems for solutions of differential equations in Hilbert spaces, Comm. Pure Appl. Math. 20 (1967) 207-229.
\item[] [5] N. Aronszajn, A unique continuation theorem for solutions of elliptic partial differential equations or inequalities of the second order, J. Math. Pures Appl. 36 (1957) 235-249.
\item[] [6] M. F. Atiyah, V. K. Patodi, and I. M. Singer, Spectral asymmetry in Riemannian geometry, I, Math. Proc. Cambridge Phil. Soc. 77 (1975) 43-69.
\item[] [7] T. Aubin, Nonlinear Analysis on Complex Manifolds. Monge-Ampère Equations, Springer, New York, 1982.
\item[] [8] P. J. Braam and S. K. Donaldson, Floer's work on instanton homology, knots, and surgery, in: The Floer Memorial Volume, eds. H. Hofer et al., Birkhäuser, Boston, 1995, pp. 196-256.
\item[] [9] S. B. Bradlow and G. D. Daskalopoulos, Moduli of stable pairs for holomorphic bundles over Riemann surfaces, Internat. J. Math. 2 (1991) 477-513.
\item[] [10] S. B. Bradlow and O. Garcia-Prada, Non-abelian monopoles and vortices, in: Proceedings of the Conference on Geometry and Physics (Aarhus, 1995), Lecture Notes in Pure and Appl. Math. 184, Dekker, New York, 1997, pp. 567-589; alg-geom/9602010.
\item[] [11] T. Bröcker and T. tom Dieck, Representations of Compact Lie Groups, Springer, New York, 1985.
\item[] [12] I. Chavel, Eigenvalues in Riemannian Geometry, Academic Press, Orlando, FL, 1984.
\item[] [13] R. Constantinescu, MIT Thesis (Mathematics), 1996.
\item[] [14] S. K. Donaldson, An application of gauge theory to four-dimensional topology, J. Differential Geom. 18 (1983) 279-315.
\item[] [15] \_\_\_\_, Connections, cohomology and the intersection forms of four-manifolds, J. Differential Geom. 24 (1986) 275-341.
\item[] [16] \_\_\_\_, Irrationality and the $h$-cobordism conjecture, J. Differential Geom. 26 (1987), 141-168.
\item[] [17] \_\_\_\_, The orientation of Yang-Mills moduli spaces and 4-manifold topology, J. Differential Geom. 26 (1987) 397-428.
\item[] [18] \_\_\_\_, Polynomial invariants for smooth four-manifolds Topology 29 (1990) 257-315.
\item[] [19] \_\_\_\_, The Seiberg-Witten equations and four-manifold topology, Bull. Amer. Math. Soc. 33 (1996) 45-70.
\item[] [20] S. K. Donaldson and P. B. Kronheimer, The Geometry of Four-Manifolds, Oxford University Press, Oxford, 1990.
\item[] [21] G. Ellingsrud and L. Göttsche, Wall-crossing formulas, Bott residue formula and the Donaldson invariants of rational surfaces, alg-geom/9506019.
\item[] [22] P. M. N. Feehan, Critical-exponent Sobolev norms and the slice theorem for the quotient space of connections, submitted to a print journal, October, 1996.
\item[] [23] \_\_\_\_, Generic metrics, irreducible rank-one PU(2) monopoles, and transversality, submitted to a print journal, August 27, 1997.
\item[] [24] P. M. N. Feehan and T. G. Leness, PU(2) monopoles and relations between four-manifold invariants, Topology Appl., to appear; dg-ga/9709022.
\item[] [25] \_\_\_\_, PU(2) monopoles, II: Highest-level singularities and relations between four-manifold invariants, in preparation.
\item[] [26] \_\_\_\_, PU(2) monopoles, III: Existence of gluing and obstruction maps, in preparation.
\item[] [27] \_\_\_\_, PU(2) monopoles, IV: Surjectivity of gluing maps, in preparation.
\item[] [28] R. Fintushel and R. Stern, Donaldson invariants of 4-manifolds with simple type, J. Differential Geom. 42 (1995) 577-633.
\item[] [29] A. Floer, An instanton-invariant for 3-manifolds, Comm. Math. Phys. 118 (1988) 215-240.
\end{itemize}
\begin{itemize}
\item[] [30] D. Freed and K. K. Uhlenbeck, Instantons and Four-Manifolds, 2nd ed., Springer, New York, 1991.
\item[] [31] R. Friedman and J. W. Morgan, Smooth Four-Manifolds and Complex Surfaces, Springer, Berlin, 1994.
\item[] [32] R. Friedman and Z. Qin, Flips of moduli spaces and transition formulas for Donaldson polynomial invariants of rational surfaces, Comm. Anal. Geom. (1995) 11-83.
\item[] [33] D. Gilbarg and N. Trudinger, Elliptic Partial Differential Equations of Second Order, 2nd ed., Springer, New York, 1983.
\item[] [34] P. B. Gilkey, Invariance Theory, the Heat Equation, and the Atiyah-Singer Index Theorem, Publish or Perish, Wilmington, DE, 1984.
\item[] [35] L. Göttsche, Modular forms and Donaldson invariants for 4-manifolds with $b_{+}=1$, J. Amer. Math. Soc. 9 (1996), 827-843.
\item[] [36] P. Hartman, Ordinary Differential Equations, 2nd ed., Birkhäuser, Boston, 1982.
\item[] [37] L. Hörmander, The Analysis of Linear Partial Differential Operators, Vol. III, Springer, New York, 1983.
\item[] [38] S. Hyun, J. Park, and J-S. Park, Topological QCD, Nuclear Phys. B 453 (1995) 199-224; hep-th/9503201.
\item[] [39] \_\_\_\_, $N=2$ Supersymmetric QCD and four-manifolds, I: the Donaldson and the Seiberg-Witten invariants, hep-th/9508162.
\item[] [40] R. V. Kadison and J. R. Ringrose, Fundamentals of the theory of operator algebras, Volume I, Academic Press, New York, 1983.
\item[] [41] T. Kato, Perturbation Theory for Linear Operators, 2nd ed., Springer, New York, 1984.
\item[] [42] J. Kazdan, Unique continuation in geometry, Comm. Pure Appl. Math. XLI (1988) 667-681.
\item[] [43] S. Kobayashi Differential Geometry of Complex Vector Bundles, Princeton University Press, Princeton, NJ, 1987.
\item[] [44] S. Kobayashi and K. Nomizu, Foundations of Differential Geometry, Vols. I \& II, Wiley, New York, 1963 and 1968.
\item[] [45] D. Kotschick and J. W. Morgan, SO(3) invariants for four-manifolds with $b^{+}=1$. II, J. Differential Geom. 39 (1994) 433-456.
\item[] [46] P. B. Kronheimer, Seiberg-Witten Invariants for Four-Manifolds, Lectures at Oxford University, Spring 1995.
\item[] [47] P. B. Kronheimer and T. S. Mrowka, The genus of embedded surfaces in the projective plane, Math. Res. Lett. 1 (1994) 797-808.
\item[] [48] \_\_\_\_, Embedded surfaces and the structure of Donaldson's polynomial invariants, J. Differential Geom. 43 (1995) 573-734.
\item[] [49] \_\_\_\_, Monopoles and contact structures, Invent. Math., to appear.
\item[] [50] J. M. F. Labastida and C. Lozano, Mathai-Quillen Formulation of Twisted $N=4$ Supersymmetric Gauge Theories in Four Dimensions, hep-th/9702106.
\item[] [51] J. M. F. Labastida and M. Mariño, Non-abelian monopoles on four-manifolds, Nuclear Phys. B 448 (1995) 373-395; hep-th/9504010.
\item[] [52] \_\_\_\_, Polynomial invariants for SU (2) monopoles, Nuclear Phys. B 456 (1995) 633-668; hep-th/9507140.
\item[] [53] \_\_\_\_, Twisted $N=2$ supersymmetry with central charge and equivariant cohomology, Comm. Math. Phys. 185 (1997) 37-71; hep-th/9603169.
\item[] [54] O. A. Ladyzhenskaya and N. N. Ural'tseva, Linear and Quasilinear Elliptic Equations, Academic Press, New York, 1968.
\item[] [55] S. Lang, Differential and Riemannian Manifolds, 3rd ed., Springer, New York, 1995.
\item[] [56] H. B. Lawson, The Theory of Gauge Fields in Four Dimensions, Conf. Board Math. Sci. 58, Amer. Math. Soc., Providence, RI, 1985.
\end{itemize}
\begin{itemize}
\item[] [57] H. B. Lawson and M-L. Michelsohn, Spin Geometry, Princeton Univ. Press, Princeton, NJ, 1988.
\item[] [58] T. G. Leness, Donaldson wall-crossing formulas via topology, dg-ga/9603016.
\item[] [59] J. Li and G. Tian, Virtual moduli cycles and Gromov-Witten invariants of general symplectic manifolds, alg-geom/9602007.
\item[] [60] G. Moore and E. Witten, Integration over the $u$-plane in Donaldson theory, hep-th/9709193.
\item[] [61] J. W. Morgan, Gauge Theory and the Topology of Smooth Four-Manifolds, Lecture Notes, Harvard University, 1988.
\item[] [62] \_\_\_\_, The Seiberg-Witten Equations and Applications to the Topology of Smooth Four-Manifolds, Princeton University Press, Princeton, NJ, 1996.
\item[] [63] J. W. Morgan, T. S. Mrowka, and D. Ruberman, $L^{2}$ moduli spaces and a vanishing theorem for Donaldson polynomial invariants, International Press, Cambridge, MA, 1994.
\item[] [64] C. B. Morrey, Multiple Integrals in the Calculus of Variations, Springer, New York, 1966.
\item[] [65] T. S. Mrowka, Seiberg-Witten Invariants for Four-Manifolds, Lectures at Harvard University, Spring 1995.
\item[] [66] T. S. Mrowka, P. S. Ozsváth, and B. Yu, Seiberg-Witten monopoles on Seifert-fibered spaces, Comm. Anal. Geom., to appear.
\item[] [67] C. Okonek and A. Teleman, The coupled Seiberg-Witten equations, vortices, and moduli spaces of stable pairs, Internat. J. Math. 6 (1995) 893-910; alg-geom/9505012.
\item[] [68] \_\_\_\_, Quaternionic monopoles, Comm. Math. Phys. 180 (1996) 363-388; alg-geom/9505029.
\item[] [69] \_\_\_\_, Recent developments in Seiberg-Witten theory and complex geometry, alg-geom/9612015.
\item[] [70] T. H. Parker, Gauge theories on four dimensional Riemannian manifolds, Comm. Math. Phys. 85 (1982) 563-602.
\item[] [71] V. Y. Pidstrigach, From Seiberg-Witten to Donaldson: SO(3) monopole equations, Lecture at Newton Institute, Cambridge, December 1994.
\item[] [72] \_\_\_\_, Seiberg-Witten and Donaldson invariants, Lecture at Oberwolfach, May 1996.
\item[] [73] V. Y. Pidstrigach and A. N. Tyurin, Invariants of the smooth structure of an algebraic surface arising from the Dirac operator, Russian Acad. Sci. Izv. Math. 40 (1993) 267-351.
\item[] [74] \_\_\_\_, Localization of Donaldson invariants along the Seiberg-Witten classes, dg-ga/9507004.
\item[] [75] Y. Ruan, Virtual neighborhoods and pseudoholomorphic curves, alg-geom/9611021.
\item[] [76] W. Rudin, Functional Analysis, McGraw-Hill, New York, 1973.
\item[] [77] D. Salamon, Spin Geometry and Seiberg-Witten Invariants, Birkhäuser, Boston, to appear.
\item[] [78] S. Sedlacek, A direct method for mimizing the Yang-Mills functional, Comm. Math. Phys. 86 (1982) 515-527.
\item[] [79] B. Siebert, Gromov-Witten invariants for general symplectic manifolds, alg-geom/9608005.
\item[] [80] S. Smale, An infinite-dimensional version of Sard's theorem, Amer. J. Math. 87 (1973) 213-221.
\item[] [81] C. H. Taubes, Self-dual Yang-Mills connections on non-self-dual 4-manifolds, J. Differential Geom. 17 (1982) 139-170.
\item[] [82] \_\_\_\_, Self-dual connections on 4-manifolds with indefinite intersection matrix, J. Differential Geom. 19 (1984) 517-560.
\item[] [83] \_\_\_\_, Path-connected Yang-Mills moduli spaces, J. Differential Geom. 19 (1984) 337-392.
\item[] [84] \_\_\_\_, A framework for Morse theory for the Yang-Mills functional, Invent. Math. 94 (1988) 327-402.
\item[] [85] \_\_\_\_, The stable topology of self-dual moduli spaces, J. Differential Geom. 29 (1989) 162-230.
\item[] [86] \_\_\_\_, Casson's invariant and gauge theory, J. Differential Geom. 31 (1990) 547-599.
\item[] [87] \_\_\_\_, $L^{2}$ moduli spaces on 4-manifolds with cylindrical ends, International Press, Cambridge, MA, 1993.
\end{itemize}
[88] \_\_\_\_, Unique continuation theorems in gauge theories, Comm. Anal. Geom. 2 (1994) 35-52.
[89] \_\_\_\_, The Seiberg-Witten invariants and symplectic forms, Math. Res. Lett. 1 (1994) 809-822.
[90] \_\_\_\_, Floer Theory for Twisted Circle Bundles, International Press, Cambridge, MA, to appear.
[91] A. Teleman, Non-abelian Seiberg-Witten theory and stable oriented pairs, Internat. J. Math. 8 (1997) 507-535; alg-geom/9609020.
[92] \_\_\_\_, Moduli spaces of PU(2) monopoles, dg-ga/9702006.
[93] \_\_\_\_, Untitled preprint.
[94] K. K. Uhlenbeck, Removable singularities in Yang-Mills fields, Comm. Math. Phys. 83 (1982) 11-29.
[95] \_\_\_\_, Connections with $L^{p}$ bounds on curvature, Comm. Math. Phys. 83 (1982) 31-42.
[96] \_\_\_\_, The Chern classes of Sobolev connections, Comm. Math. Phys. 101 (1985) 449-457.
[97] V. S. Varadarajan, Lie Groups, Lie Algebras, and their Representations, Springer, New York, 1984.
[98] E. Witten, Monopoles and four-manifolds, Math. Res. Lett. 1 (1994) 769-796.
[99] H-J. Yang, Transition functions and a blow-up formula for Donaldson polynomials, Columbia University Thesis, 1992.

Department of Mathematics, Harvard University, Cambridge, MA 02138
E-mail address: feehan@math.harvard.edu
Department of Mathematics, Michigan State University, East Lansing, MI 48824
E-mail address: leness@math.msu.edu