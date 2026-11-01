---
retention_scope: session
part: 4
total_parts: 4
---

[Part 4/4 of: [1404.3118] Yamabe type equations with a sign-changing nonlinearity, and the prescribed curvature problem]

Therefore,
$$\begin{aligned}
& \int_{\{\bar{u} \geq \theta\}}\left[(\bar{u}+\theta)^{p-1}-\bar{u}^{p-1}\right] \bar{u} \mathrm{~d} \mu_{f} \\
& \leq \begin{cases}\int_{\{\bar{u} \geq \theta\}} \theta^{p-1} \bar{u} \mathrm{~d} \mu_{f} \leq\|\theta\|_{L^{p}(\Omega)}^{p-1}\|\bar{u}\|_{L^{p}(\Omega)} & \text { if } p-1 \leq 1, \\
p 2^{p-1} \int_{\{\bar{u} \geq \theta\}} \theta \bar{u}^{p-1} \mathrm{~d} \mu_{f} \leq p 2^{p-1}\|\theta\|_{L^{p}(\Omega)}\|\bar{u}\|_{L^{p}(\Omega)}^{p-1} & \text { if } p-1>1 .\end{cases}
\end{aligned}$$
Inserting the obtained estimates into (7.17) we finally get
$$-\mathcal{B}(\bar{u})[\bar{u}] \geq-\int_{\Omega} V|\bar{u}|^{p} \mathrm{~d} \mu_{f}-C_{4}\|\bar{u}\|_{L^{p}(\Omega)}^{\max \{p-1,1\}}-C_{5}$$
for some constants $C_{4}, C_{5}>0$ independent of $\bar{u}$.
Combining (7.16) and (7.18) we obtain
$$\mathcal{F}(\bar{u})[\bar{u}] \geq\|\nabla \bar{u}\|_{L^{p}(\Omega)}^{p}-C_{3}\|\nabla \bar{u}\|_{L^{p}(\Omega)}^{p-1}-C_{6}-C_{4}\|\bar{u}\|_{L^{p}(\Omega)}^{\max \{p-1,1\}}-\int_{\Omega} V|\bar{u}|^{p} \mathrm{~d} \mu_{f} .$$
On the other hand, using Rayleigh characterization of $\lambda_{V}(\Omega)$, since $\bar{u} \in W_{0}^{1, p}(\Omega)$ we get
$$\|\nabla \bar{u}\|_{L^{p}(\Omega)}^{p}-\int_{\Omega} V|\bar{u}|^{p} \mathrm{~d} \mu_{f} \geq \lambda_{V}(\Omega)\|\bar{u}\|_{L^{p}(\Omega)}^{p},$$
thus,
$$\mathcal{F}(\bar{u})[\bar{u}] \geq \lambda_{V}(\Omega)\|\bar{u}\|_{L^{p}(\Omega)}^{p}-C_{4}\|\bar{u}\|_{L^{p}(\Omega)}^{\max \{p-1,1\}}-C_{3}\|\nabla \bar{u}\|_{L^{p}(\Omega)}^{p-1}-C_{6}$$
for some constants $C_{4}, C_{3}, C_{6}>0$ and independent of $\bar{u}$.
Since $\bar{u} \in W_{0}^{1, p}(\Omega)$, by Poincaré inequality on $\Omega$, there exists a constant $C_{P}>0$ independent of $\bar{u}$ such that
$$\|\bar{u}\|_{L^{p}(\Omega)} \leq C_{P}\|\nabla \bar{u}\|_{L^{p}(\Omega)} .$$
Now, let $\bar{u}_{k} \in \overline{\mathcal{K}}_{\psi, \theta}$ be any sequence such that $\left\|\bar{u}_{k}\right\|_{W^{1, p}(\Omega)} \rightarrow+\infty$ as $k \rightarrow+\infty$. Again by Poincaré inequality, $\left\|\nabla \bar{u}_{k}\right\|_{L^{p}(\Omega)} \rightarrow+\infty$ as $k \rightarrow+\infty$, and two cases may occur: either
$$(a) \quad \frac{\left\|\bar{u}_{k}\right\|_{L^{p}(\Omega)}}{\left\|\nabla \bar{u}_{k}\right\|_{L^{p}(\Omega)}} \rightarrow 0, \quad \text { or } \quad(b) \quad \limsup _{k \rightarrow+\infty} \frac{\left\|\bar{u}_{k}\right\|_{L^{p}(\Omega)}}{\left\|\nabla \bar{u}_{k}\right\|_{L^{p}(\Omega)}}=c>0 .$$
In the case (a), using (7.19), we deduce
$$\begin{aligned}
& \frac{\mathcal{F}\left(\bar{u}_{k}\right)\left[\bar{u}_{k}\right]}{\left\|\bar{u}_{k}\right\|_{W_{0}^{1, p}(\Omega)}^{1, p}} \geq \\
& \geq \frac{\left\|\nabla \bar{u}_{k}\right\|_{L^{p}(\Omega)}^{p}-\|V\|_{L^{\infty}(\Omega)}\left\|\bar{u}_{k}\right\|_{L^{p}(\Omega)}^{p}-C_{4}\left\|\bar{u}_{k}\right\|_{L^{p}(\Omega)}^{\max \{p-1,1\}}-C_{3}\left\|\nabla \bar{u}_{k}\right\|_{L^{p}(\Omega)}^{p-1}-C_{6}}{\left(1+C_{P}\right)\left\|\nabla \bar{u}_{k}\right\|_{L^{p}(\Omega)}} \rightarrow+\infty
\end{aligned}$$
as $\left\|\nabla \bar{u}_{k}\right\|_{L^{p}(\Omega)} \rightarrow+\infty$.
In case ( $b$ ), for each subsequence (still denoted with $\left\{\bar{u}_{k}\right\}$ ) satisfying
$$\frac{\left\|\bar{u}_{k}\right\|_{L^{p}(\Omega)}}{\left\|\nabla \bar{u}_{k}\right\|_{L^{p}(\Omega)}} \rightarrow \bar{c} \in(0, c] \quad \text { for } k \rightarrow+\infty$$
using (7.20) and $\lambda_{V}(\Omega)>0$ we get
$$\frac{\mathcal{F}\left(\bar{u}_{k}\right)\left[\bar{u}_{k}\right]}{\left\|\bar{u}_{k}\right\|_{W_{0}^{1, p}(\Omega)}^{1, p}} \geq \frac{\lambda_{V}(\Omega)\left\|\bar{u}_{k}\right\|_{L^{p}(\Omega)}^{p}-C_{4}\left\|\bar{u}_{k}\right\|_{L^{p}(\Omega)}^{\max \{p-1,1\}}-C_{3}\left\|\nabla \bar{u}_{k}\right\|_{L^{p}(\Omega)}^{p-1}-C_{6}}{\left(1+C_{P}\right)\left\|\nabla \bar{u}_{k}\right\|_{L^{p}(\Omega)}} \rightarrow+\infty$$
as $\left\|\nabla \bar{u}_{k}\right\|_{L^{p}(\Omega)} \rightarrow+\infty$. This concludes the proof of the coercivity of $\mathcal{F}$. \(\square\)

For $\theta=\psi$ we set $\mathcal{K}_{\psi}$ for $\mathcal{K}_{\psi, \psi}$. Next, we prove a minimizing properties for solutions of the obstacle problem.

Proposition 7.1. Let $u \in \mathcal{K}_{\psi, \theta}, u \not \equiv 0$ be a solution of the obstacle problem with $\psi \geq 0$. Suppose that $w \in W^{1, p}(\Omega), w \not \equiv 0$ solves $Q_{V}^{\prime}(w) \geq 0$ on $\Omega$, such that $\min \{u, w\} \in \mathcal{K}_{\psi, \theta}$. If
$$\frac{u}{w}, \frac{w}{u} \in L^{\infty}(\Omega),$$
then $u \leq w$ on $\Omega$.
Proof. Since $w, u$ are non-negative, nonzero supersolutions ( $u$ being a solution of the obstacle problem), by the half-Harnack inequality we have $u>0$ and $w>0$ on $\Omega$. Combining with (7.21) and since $\Omega$ is relatively compact, we deduce that the following set is non-empty.
$$A \doteq\{c>1: c w(x) \geq u(x) \quad \text { for a.e. } x \in \Omega\} .$$
Let $c_{0}=\inf A$, so that $c_{0} w \geq u$ a.e. on $\Omega$. We shall show that $c_{0}=1$. By contradiction suppose $c_{0}>1$, and choose $1<c<c_{0}$ close enough to $c_{0}$ to have
$$\frac{(c w)^{p}}{u^{p-1}} \geq \psi \quad \text { on } \Omega .$$
This is possible since, for $c \geq c_{0}^{\frac{p-1}{p}}$ we have
$$\frac{(c w)^{p}}{u^{p-1}} \geq \frac{(c w)^{p}}{\left(c_{0} w\right)^{p-1}}=\frac{c^{p}}{c_{0}^{p-1}} w \geq w \geq \psi, \quad \text { on } \quad \bar{\Omega}$$
Consider the non-empty set $U=\{x \in \Omega: u(x)>c w(x)\}$, and define
$$\varphi=u+\min \left\{\frac{(c w)^{p}-u^{p}}{u^{p-1}}, 0\right\}=\min \left\{u, \frac{(c w)^{p}}{u^{p-1}}\right\} .$$
Because of (7.22), $\varphi \geq \psi$ and $\varphi-\theta=u-\theta=0$ on $\partial \Omega$; in other words, $\varphi \in \mathcal{K}_{\psi, \theta}$.
Since $u$ solves the obstacle problem (7.7), using the above $\varphi$ we deduce
$$\begin{aligned}
0 \leq Q_{V}^{\prime}(u)[\varphi-u]= & \int_{U}|\nabla u|^{p-2}\left\langle\nabla u, \nabla\left(\frac{(c w)^{p}-u^{p}}{u^{p-1}}\right)\right\rangle \mathrm{d} \mu_{f} \\
& -\int_{U} V\left((c w)^{p}-u^{p}\right) \mathrm{d} \mu_{f} .
\end{aligned}$$
On the other hand, applying the definition of supersolution to $c w$ with the non-negative test function
$$\widetilde{\varphi}=\frac{\left(u^{p}-(c w)^{p}\right)_{+}}{(c w)^{p-1}} \in W_{0}^{1, p}(\Omega),$$
we get
$$\begin{aligned}
0 \leq Q_{V}^{\prime}(c w)[\widetilde{\varphi}]= & \int_{U}|\nabla(c w)|^{p-2}\left\langle\nabla(c w), \nabla\left(\frac{u^{p}-(c w)^{p}}{(c w)^{p-1}}\right)\right\rangle \mathrm{d} \mu_{f} \\
& -\int_{U} V\left(u^{p}-(c w)^{p}\right) \mathrm{d} \mu_{f} .
\end{aligned}$$
Summing up (7.23) and (7.24) we get
$$\int_{U}|\nabla(c w)|^{p-2}\left\langle\nabla(c w), \nabla\left(\frac{u^{p}-(c w)^{p}}{(c w)^{p-1}}\right)\right\rangle \mathrm{d} \mu_{f}-\int_{U}|\nabla u|^{p-2}\left\langle\nabla u, \nabla\left(\frac{u^{p}-(c w)^{p}}{u^{p-1}}\right)\right\rangle \mathrm{d} \mu_{f} \geq 0 .$$
Set $z=\max \{u, c w\}$, and note that (7.25) is equivalent to $I(c w, z) \leq 0$. Indeed, in the definition (3.7) of $I$, the part of the integral outside $U$ is zero since $z \equiv c w$. To conclude, applying Proposition 3.2 we deduce $I(c w, z)=0$, so that $c w$ and $z$ (hence $u$ ) are proportional. Since $c w=u$ on $\partial U$ we conclude that $u \equiv c w$ on $U$, contradicting the definition of this latter. \(\square\)

Remark 7.2. A typical case when (7.21) is automatically met is when the data $\psi, \theta$ satisfy $\psi, \theta \in W^{1, p}(\Omega) \cap C^{0}(\bar{\Omega})$ and $\theta>0$ on $\partial \Omega$, which we will frequently use. In fact, when $\psi, \theta \in C^{0}(\bar{\Omega})$, the solution $u \in \mathcal{K}_{\psi, \theta}$ of the obstacle problem is continuous on $\bar{\Omega}$. In this respect, see Theorem 5.4, page 235 of [52].

Remark 7.3. Although it is not explicitly stated, condition $\lambda_{V}(\Omega) \geq 0$ is automatic by assuming the existence of a $u$ solving the obstacle problem and $\psi \geq 0, \psi \not \equiv 0$. Indeed, $u$ is a positive solution of $Q_{V}^{\prime}(u) \geq 0$ on $M$, and $\lambda_{V}(\Omega) \geq 0$ follows from Proposition 3.4.

In particular from the above proposition we deduce the following characterization.
Corollary 7.1. Let $\Omega \Subset M$ be a relatively compact open set, and let $0 \leq \theta \in W^{1, p}(\Omega) \cap$ $C^{0}(\bar{\Omega})$ be such that $\theta>0$ on $\partial \Omega$. Then, a solution $u$ of the obstacle problem on $\mathcal{K}_{\psi, \theta}$ with obstacle $0 \leq \psi \leq \theta, \psi \not \equiv 0$ is the minimal $w \in \mathcal{K}_{\psi, \theta}$ satisfying $Q_{V}^{\prime}(w) \geq 0$ on $\Omega$. Consequently, such a solution is unique.

A second important consequence of Proposition 7.1 is
Proposition 7.2. Let $w_{1}, w_{2} \in W_{\text {loc }}^{1, p}(M) \cap C^{0}(M)$ be positive solutions of $Q_{V}^{\prime}\left(w_{j}\right) \geq 0$ on $M, j=1,2$. Then,
$$w \doteq \min \left\{w_{1}, w_{2}\right\}$$
solves
$$Q_{V}^{\prime}(w) \geq 0 \quad \text { on } \quad M .$$

Proof. Fix any relatively compact open set $\Omega$ with smooth boundary and consider a solution $s$ of the obstacle problem $\mathcal{K}_{w}$ on $\Omega$. This is possible since $w \in W^{1, p}(\Omega)$. From $s \in \mathcal{K}_{w}$ we have $s \geq w$, and, being a solution of the obstacle problem, $Q_{V}^{\prime}(s) \geq 0$. Next, since $w_{j}>0$ on $\bar{\Omega}$ and $Q_{V}^{\prime}\left(w_{j}\right) \geq 0$, we can apply Proposition 7.1 to obtain $s \leq w_{j}$ for each $j$, whence $s \leq w$. This shows that $s \equiv w$, so that $w$ solves (7.26) as claimed. \(\square\)

We are now ready for the

Proof of Lemma 3.1. First we show that $u \in W_{\text {loc }}^{1, p}\left(\bar{\Omega}_{2}\right)$. Let $U \subset \bar{\Omega}_{2}$ be a relatively compact open set. Without loss of generality we can assume that $\Omega_{1} \cap U \neq \emptyset$, for otherwise $u \equiv u_{2}$ on $U$ and the sought is immediate. Since $z=\min \left\{u_{1}-u_{2}, 0\right\} \in$ $W^{1, p}\left(\Omega_{1}\right)$ is zero on $\partial \Omega_{1} \cap \Omega_{2}$, there exists a sequence $\left\{\varphi_{j}\right\} \subset C^{0}\left(\overline{U \cap \Omega_{1}}\right) \cap W^{1, p}(U \cap$ $\left.\Omega_{1}\right), \varphi_{j} \equiv 0$ on some neighbourhood of $\partial \Omega_{1} \cap \Omega_{2}$, converging in the $W^{1, p}\left(U \cap \Omega_{1}\right)$ norm to $z$. Using that $z \leq 0$ on $\Omega_{1}$, one can take, for instance,
$$\varphi_{j}=\left(z+\frac{1}{j}\right)_{-} .$$
We extend each $\varphi_{j}$ to a continuous function on $U \backslash \Omega_{1}$ by setting $\varphi_{j} \equiv 0$ on $U \backslash \Omega_{1}$, so that $\varphi_{j} \in W^{1, p}(U)$ and clearly $\varphi_{j} \rightarrow z 1_{\Omega_{1}}$ in $W^{1, p}(U)$, which shows that $z 1_{\Omega_{1}} \in$ $W^{1, p}(U)$. It follows that $u=u_{2}+\varphi_{j} \in W^{1, p}(U)$ converges to $u=u_{2}+z 1_{\Omega_{1}}$, whence $u \in W^{1, p}(U)$.

To prove that $Q_{V}^{\prime}(u) \geq 0$ on $\Omega_{2}$, we shall reduce ourselves to Proposition 7.1. We take a smooth open set $U \Subset \Omega_{2}$ which, without loss of generality, intersects $\Omega_{1}$. Since $\lambda_{V}(U)>0$ by monotonicity of eigenvalues, Theorem 7.1 guarantees the existence of a solution $s$ of the obstacle problem in $\mathcal{K}_{u}$ on $U$ which, applying Theorem 5.4, page 235 in [52] is continuous on $\bar{U}$. We want to show that $s \equiv u$ on $U$. First, since $u>0$ on $\bar{U}$, using Proposition 7.2 we get
$$s \leq u_{2} \quad \text { on } U .$$
Hence, $s=u_{2}=u$ on $U \backslash \Omega_{1}$. Consequently, since also $s \in \mathcal{K}_{u}, s-u=0$ on $\partial U \cup$ $\left(\partial \Omega_{1} \cap U\right)=\partial\left(\Omega_{1} \cap U\right)$, and so by standard theory
$$s-u \in W_{0}^{1, p}\left(\Omega_{1} \cap U\right) .$$
(one can construct an approximating sequence as in (7.27) above). Therefore, $s$ is also a solution of the obstacle problem on the closed convex set
$$\hat{\mathcal{K}}_{u}=\left\{\varphi \in W^{1, p}\left(\Omega_{1} \cap U\right) \mid \varphi \geq u \text { a.e. and } \varphi-u \in W_{0}^{1, p}\left(\Omega_{1} \cap U\right)\right\} \text {. }$$
As $u_{1}$ is a positive supersolution on $\Omega_{1} \cap U$ and $\min \left\{s, u_{1}\right\} \in \hat{\mathcal{K}}_{u}$, by Proposition 7.1
$$s \leq u_{1} \quad \text { on } \Omega_{1} \cap U .$$
Coupling with (7.28) we get $s \leq u$ on $\Omega_{1} \cap U$, and combining with $s \geq u$ on $U\left(s \in \mathcal{K}_{u}\right)$, $s=u=u_{1}$ on $U \backslash \Omega_{1}$, we conclude $s \equiv u$ on $U$. This shows that $u$ solves $Q_{V}^{\prime}(u) \geq 0$ on $U$. As $U \Subset \Omega_{2}$ is arbitrary, $Q_{V}^{\prime}(u) \geq 0$ on $\Omega_{2}$, concluding the proof. \(\square\)

Acknowledgements: The second author is supported by the grant PRONEX - Núcleo de Análise Geométrica e Aplicacões Processo n° PR2-0054-00009.01.00/11.
It is a pleasure to thank Y. Pinchover for having suggested us, after we posted a first version of this work on arXiv, the very recent [23, 24] which contain results tightly related to those in Section 4.

\section*{References}
\begin{itemize}
\item[] [1] Adimurthi and A. Sekar. Role of the fundamental solution in Hardy-Sobolev-type inequalities. Proc. Roy. Soc. Edinburgh Sect. A, 136(6):1111-1130, 2006.
\item[] [2] G. Albanese, L. Mari, and M. Rigoli. On the role of gradient terms in coercive quasilinear differential inequalities on Carnot groups. Nonlinear Anal., 126:234-261, 2015.
\item[] [3] W. Allegretto. On the equivalence of two types of oscillation for elliptic operators. Pacific J. Math., 55:319-328, 1974.
\end{itemize}
\begin{itemize}
\item[] [4] W. Allegretto and Y.X. Huang. A Picone's identity for the $p$-Laplacian and applications. Nonlinear Anal., 32(7):819-830, 1998.
\item[] [5] W. Allegretto and Y.X. Huang. Principal eigenvalues and Sturm comparison via Picone's identity. J. Diff. Equations, 156(2):427-438, 1999.
\item[] [6] A. Anane. Simplicité et isolation de la première valeur propre du $p$-laplacien avec poids. C. R. Acad. Sci. Paris Sér. I Math., 305(16):725-728, 1987.
\item[] [7] A. Ancona. Théorie du potentiel sur les graphes et les variétés, volume 1427 of Lecture Notes in Math. Springer, Berlin, 1990.
\item[] [8] P. Aviles and R. Mc Owen. Conformal deformations of complete manifolds with negative curvature. J. Diff. Geom., 21(2):269-281, 1985.
\item[] [9] S. Bae. On positive entire solutions of indefinite semilinear elliptic equations. J. Diff. Equations, 247(5):1616-1635, 2009.
\item[] [10] G. Barbatis, S. Filippas, and A. Tertikas. A unified approach to improved $L^{p}$ Hardy inequalities with best constants. Trans. Amer. Math. Soc., 356(6):2169-2196 (electronic), 2004.
\item[] [11] G. Barles. Remarks on uniqueness results of the first eigenvalue of the $p$-Laplacian. Ann. Fac. Sci. Toulouse Math., Séries 5, 9(1):65-75, 1988.
\item[] [12] B. Bianchini, L. Mari, and M. Rigoli. On some aspects of oscillation theory and geometry. Mem. Amer. Math. Soc., 225 (1056), 2013.
\item[] [13] B. Bianchini, L. Mari, and M. Rigoli. Yamabe type equations with sign-changing nonlinearities on non-compact Riemannian manifolds. J. Funct. Anal., 268(1):1-72, 2015.
\item[] [14] B. Bianchini, L. Mari, and M. Rigoli. Yamabe type equations with sign-changing nonlinearities on the Heisenberg group, and the role of Green functions. Recent trends in Nonlinear Partial Differential Equations I. Evolution problems "Workshop in honour of Patrizia Pucci's 60th birthday. Contemp. Math., 594:115-136, Amer. Math. Soc., Providence, RI, 2013.
\item[] [15] B. Bianchini and M. Rigoli. Non existence and uniqueness of positive solutions of Yamabe type equations on non positively curved manifolds. Trans. Amer. Math. Soc., 349:4753-4774, 1997.
\item[] [16] L. Brandolini, M. Rigoli, and A.G. Setti. Positive Solutions of Yamabe Type Equations on Complete Manifolds and Applications. J. Funct. An., 160:176-222, 1998.
\item[] [17] H. Brézis and L. Nirenberg. Positive solutions of nonlinear elliptic equations involving critical Sobolev exponents. Comm. Pure Appl. Math., 36(4):437-477, 1983.
\item[] [18] F. E. Browder. Existence theorems for nonlinear partial differential equations. Symposia in Pure Mathematics, 16:1-60, 1970.
\item[] [19] G. Carron. Inégalités de Hardy sur les variétés riemanniennes non-compactes. J. Math. Pures Appl. (9), 76(10):883-891, 1997.
\item[] [20] G. Carron. Une suite exacte en $L^{2}$-cohomologie. Duke Math. J, 95(2):343-372, 1998.
\item[] [21] K.S. Cheng and J.T. Lin. On the elliptic equations $\Delta u=K(x) u^{\sigma}$ and $\Delta u=K(x) e^{2 u}$. Trans. Amer. Math. Soc., 304(2):639-668, 1987.
\item[] [22] L. D'Ambrosio and S. Dipierro. Hardy inequalities on Riemannian manifolds and applications. Ann. Inst. H. Poincaré Anal. Non Linéaire, 31(3):449-475, 2014.
\item[] [23] B. Devyver, M. Fraas, and Y. Pinchover. Optimal Hardy weight for second-order elliptic operator: an answer to a problem of Agmon. J. Funct. Anal., 266(7):4422-4489, 2014.
\item[] [24] B. Devyver and Y. Pinchover. Optimal $L^{p}$-Hardy inequalities. Ann. Inst. H. Poincaré Anal. Non Linéaire, 33(1):93-118, 2016.
\item[] [25] J. I. Díaz. Nonlinear partial differential equations and free boundaries. Vol. I, volume 106 of Research Notes in Mathematics. Pitman (Advanced Publishing Program), Boston, MA, 1985. Elliptic equations.
\item[] [26] J.I. Díaz and J.E. Saá. Existence et unicité de solutions positives pour certaines équations elliptiques quasilinéaires. C. R. Acad. Sci. Paris Sér. I Math., 305(12):521-524, 1987.
\item[] [27] E. DiBenedetto. $C^{1+\alpha}$ local regularity of weak solutions of degenerate elliptic equations. Nonlinear Anal., 7(8):827-850, 1983.
\item[] [28] J. Escobar. On the spectrum of the Laplacian on complete Riemannian manifolds. Comm. Partial Diff. Equations, 11:63-85, 1985.
\item[] [29] J.F. Escobar and R. Schoen. Conformal metrics with prescribed scalar curvature. Invent. Math., 86(2):243-254, 1986.
\item[] [30] V. Felli and A. Pistoia. Existence of blowing-up solutions for a nonlinear elliptic equation with Hardy potential and critical growth. Comm. Partial Diff. Equations, 31(1-3):21-56, 2006.
\item[] [31] V. Felli and S. Terracini. Nonlinear Schrödinger equations with symmetric multi-polar potentials. Calc. Var. Partial Diff. Equations, 27(1):25-58, 2006.
\end{itemize}
\begin{itemize}
\item[] [32] D. Fischer-Colbrie and R. Schoen. The structure of complete stable minimal surfaces in 3-manifolds of non negative scalar curvature. Comm. Pure Appl. Math., XXXIII:199-211, 1980.
\item[] [33] J. García-Melián and J. Sabina de Lis. Maximum and comparison principles for operators involving the $p$-Laplacian. J. Math. Anal. Appl., 218(1):49-65, 1998.
\item[] [34] A. Grigor'yan. Analytic and geometric background of recurrence and non-explosion of the Brownian motion on Riemannian manifolds. Bull. Amer. Math. Soc., 36:135-249, 1999.
\item[] [35] M. Gromov. Hyperbolic manifolds, groups and actions. In Riemann surfaces and related topics: Proceedings of the 1978 Stony Brook Conference (State Univ. New York, Stony Brook, N.Y., 1978), volume 97 of Ann. of Math. Stud., pages 183-213. Princeton Univ. Press, Princeton, N.J., 1981.
\item[] [36] M. Gromov. Hyperbolic groups. In Essays in group theory, volume 8 of Math. Sci. Res. Inst. Publ., pages 75-263. Springer, New York, 1987.
\item[] [37] D. Holcman. Prescribed scalar curvature problem on complete manifolds. J. Math. Pures Appl. (9), 80(2):223-244, 2001.
\item[] [38] I. Holopainen. Nonlinear potential theory and quasiregular mappings on Riemannian manifolds. Ann. Acad. Sci. Fenn. Ser. A I Math. Dissertationes, (74):45, 1990.
\item[] [39] I. Holopainen. Positive solutions of quasilinear elliptic equations on Riemannian manifolds. Proc. London Math. Soc., 65(3):651-672, 1992.
\item[] [40] I. Holopainen. Volume growth, Green's functions, and parabolicity of ends. Duke Math. J., 97(2):319-346, 1999.
\item[] [41] I. Holopainen and P. Koskela. Volume growth and parabolicity. Proc. Amer. Math. Soc., 129(11):3425-3435 (electronic), 2001.
\item[] [42] N. Kawano. On bounded entire solutions of semilinear elliptic equations. Hiroshima Math. J., 14(1):125-158, 1984.
\item[] [43] J.L. Kazdan. Prescribing the Curvature of a Riemannian Manifold, volume 57 of CBMS Regional Conference Series in Mathematics. Published for the Conference Board of the Mathematical Sciences, Washington, DC, by the American Mathematical Society, Providence, RI, 1985.
\item[] [44] S. Kichenassamy and L. Véron. Singular solutions of the $p$-Laplace equation. Math. Ann., 275(4):599-615, 1986.
\item[] [45] S. Kichenassamy and L. Véron. Erratum: "Singular solutions of the $p$-Laplace equation" [Math. Ann. 275 (1986), no. 4, 599-615]. Math. Ann., 277(2):352, 1987.
\item[] [46] V.K. Le. On some equivalent properties of sub- and supersolutions in second order quasilinear elliptic equations. Hiroshima Math. J., 28:373-380, 1998.
\item[] [47] J.M. Lee and T.H. Parker. The yamabe problem. Bull. Amer. Math. Soc., 17(1):37-91, 1987.
\item[] [48] P. Li, L.F. Tam, and D.Yang. On the elliptic equation $\Delta u+k u-K u^{p}=0$ on complete Riemannian manifolds and their geometric applications. Trans. Amer. Math. Soc., 350(3):1045-1078, 1998.
\item[] [49] P. Li and J. Wang. Weighted Poincaré inequality and rigidity of complete manifolds. Ann. Sci. École Norm. Sup. (4), 39(6):921-982, 2006.
\item[] [50] G.M. Lieberman. Boundary regularity for solutions of degenerate elliptic equations. Nonlinear Anal., 12(11):1203-1219, 1988.
\item[] [51] J.L. Lions. Quelques méthodes de résolution des problèmes aux limites non linéaires. Dunod, 1969, xx+554.
\item[] [52] J. Malý and W.P. Ziemer. Fine regularity of solutions of elliptic partial differential equations, volume 51 of Mathematical Surveys and Monographs. American Mathematical Society, Providence, RI, 1997.
\item[] [53] L. Mari and D. Valtorta. On the equivalence of stochastic completeness, Liouville and Khas'minskii condition in linear and nonlinear setting. Trans. Amer. Math. Soc., 365(9):4699-4727, 2013.
\item[] [54] W.F. Moss and J. Piepenbrink. Positive solutions of elliptic equations. Pac. J. Math., 75:219-226, 1978.
\item[] [55] M. Murata. Structure of positive solutions to $(-\Delta+V) u=0$ in $\mathbf{R}^{n}$. Duke Math. J., 53(4):869-943, 1986.
\item[] [56] M. Naito. A note on bounded positive entire solutions of semilinear elliptic equations. Hiroshima Math.J., 14:211-214, 1984.
\item[] [57] W.M. Ni. On the Elliptic Equation $\Delta u+K(x) u^{(n+2) /(n-2)}=0$, its Generalizations, and Applications in Geometry. Indiana Univ. Math. J., 31(4):493-529, 1982.
\item[] [58] P. Petersen. Riemannian Geometry. Springer-Verlag, 1997.
\end{itemize}
\begin{itemize}
\item[] [59] J. Piepenbrink. Finiteness of the Lower Spectrum of Schrödinger Operators. Math. Z., 140:29-40, 1974.
\item[] [60] J. Piepenbrink. Nonoscillatory Elliptic Equations. J. Diff. Equations, 15:541-550, 1974.
\item[] [61] S. Pigola, M. Rigoli, and A.G. Setti. Maximum principles on Riemannian manifolds and applications. Mem. Amer. Math. Soc., 174:no.822, 2005.
\item[] [62] S. Pigola, M. Rigoli, and A.G. Setti. Vanishing and finiteness results in Geometric Analisis. A generalization of the Böchner technique, volume 266 of Progress in Math. Birkhäuser, 2008.
\item[] [63] S. Pigola, M. Rigoli, and A.G. Setti. Existence and non-existence results for a logistic-type equation on manifolds. Trans. Amer. Math. Soc., 362(4):1907-1936, 2010.
\item[] [64] S. Pigola, A.G. Setti, and M. Troyanov. The topology at infinity of a manifold supporting an $L^{q, p}$-Sobolev inequality. Expo. Math., 32(4):365-383, 2014.
\item[] [65] Y. Pinchover, A. Tertikas, and K. Tintarev. A Liouville-type theorem for the $p$-Laplacian with potential term. Ann. Inst. H. Poincaré Anal. Non Linéaire, 25(2):357-368, 2008.
\item[] [66] Y. Pinchover and K. Tintarev. A ground state alternative for singular Schrödinger operators. J. Funt. Anal., 230(1):65-77, 2006.
\item[] [67] Y. Pinchover and K. Tintarev. Ground state alternative for $p$-Laplacian with potential term. Calc. Var. Partial Diff. Equations, 28:179-201, 2007.
\item[] [68] Y. Pinchover and K. Tintarev. On positive solutions of p-Laplacian-type equations, volume 193 of in: "Analysis, Partial Differential Equations and Applications - The Vladimir Maz'ya Anniversary Volume", eds. A. Cialdea et al., Operator Theory: Advances and Applications. Birkhäuser Verlag, Basel, 2009.
\item[] [69] P. Pucci, M. Rigoli, and J. Serrin. Qualitative properties for solutions of singular elliptic inequalities on complete manifolds. J. Diff. Equations, 234(2):507-543, 2007.
\item[] [70] P. Pucci and J. Serrin. The maximum principle. Progress in Nonlinear Differential Equations and their Applications, 73. Birkhäuser Verlag, Basel, 2007.
\item[] [71] A. Ratto, M. Rigoli, and L. Veron. Scalar curvature and conformal deformation of hyperbolic space. J. Funct. An., 121(1):15-77, 1994.
\item[] [72] A. Ratto, M. Rigoli, and L. Veron. Scalar curvature and conformal deformations of noncompact Riemannian manifolds. Math. Z., 225:395-426, 1997.
\item[] [73] M. Rigoli and A.G. Setti. Liouville-type theorems for $p$-subharmonic functions. Rev. Mat. Iberoam., 17:471-520, 2001.
\item[] [74] M. Rigoli and S. Zamperlin. "A priori" estimates, uniqueness and existence of positive solutions of Yamabe type equations on complete manifolds. J. Funct. Anal., 245(1):144-176, 2007.
\item[] [75] J. Serrin. Local behaviour of solutions of quasilinear equations. Acta Math., 111:247-302, 1964.
\item[] [76] J. Serrin. Isolated singularities of solutions of quasilinear equations. Acta Math., 113:219-240, 1965.
\item[] [77] P. Tolksdorf. On the Dirichlet problem for quasilinear equations in domains with conical boundary points. Comm. Partial Diff. Equations, 8(7):773-817, 1983.
\item[] [78] P. Tolksdorf. Regularity of a more general class of quasilinear elliptic equations. J. Diff. Equations, 51:126-150, 1984.
\item[] [79] M. Troyanov. Solving the $p$-Laplacian on manifolds. Proc. Amer. Math. Soc., 128(2):541-545, 2000.
\item[] [80] Q.S. Zhang. Positive solutions to $\Delta u-V u+W u^{p}=0$ and its parabolic counterpart in noncompact manifolds. Pacific J. Math., 213(1):163-200, 2004.
\end{itemize}

Bruno Bianchini, Dipartimento di Matematica Pura e Applicata, Università degli Studi di Padova, Via Trieste 63, I-35121 Padova (Italy)

E-mail address: bianchini@dmsa.unipd.it
Luciano Mari, Departamento de Matemática, Universidade Federal do Ceará, Av. Humberto Monte s/n, Bloco 914, 60455-760 Fortaleza (Brazil)

E-mail address: mari@mat.ufc.br
Marco Rigoli, Dipartimento di Matematica, Università degli studi di Milano, Via Saldini 50, I-20133 Milano (Italy)

E-mail address: marco.rigoli55@gmail.com