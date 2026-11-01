---
retention_scope: session
part: 3
total_parts: 3
---

[Part 3/3 of: Almost-Kähler smoothings of compact complex surfaces with singularities.]

With the exact same proof, we show
Proposition 36. For all $k \geq 1$, for every compact set $K \subset X$, we have $\left\|h_{\varepsilon} J_{\varepsilon}-J_{X}\right\|_{\mathcal{C}^{4+k, \alpha}(K)} \xrightarrow{\varepsilon \rightarrow 0} 0$.

\section*{6 Hamiltonian stationary spheres.}

Through our construction, we have obtained a family of compatible almost-complex structures $\left(J_{f}\right)$ depending on a parameter $0<\varepsilon<\varepsilon_{0}$ in such a way that the almost-Kähler structure $\left(\omega_{\varepsilon}, J_{\varepsilon}, g_{\varepsilon}\right)$ on $M_{\varepsilon}$ has constant Hermitian scalar curvature for $0<\varepsilon<\varepsilon_{0}$.

Moreover, when $\varepsilon$ goes to zero, the pullback of $J_{f}$ on the ALE model $X$ converges in $\mathcal{C}^{2, \alpha}$-norm to $J_{X}$ in a compact neighborhood of the zero section of $T^{*} S^{2} \simeq X$, in the sense defined in 14, according to Theorem 33.

Remark 37. More precisely, in the proof of Theorem 33, we had obtained
$$\left\|h_{\varepsilon}^{*} J_{f}-J_{X}\right\|_{\mathcal{C}^{2, \alpha}(X)} \leq c \varepsilon^{\delta\left(1-\beta^{+}\right)}$$
which also gives us
$$\left\|\varepsilon^{-2} h_{\varepsilon}^{*} g_{f}-g_{X}\right\|_{\mathcal{C}^{2, \alpha}(X)} \leq c \varepsilon^{\delta\left(1-\beta^{+}\right)}$$

Besides, according to Corollary 17, the symplectic manifolds $\left(M_{\varepsilon}, \omega_{\varepsilon}\right)$ can actually all be identified to the same symplectic manifold that we call $(\hat{M}, \hat{\omega})$ (for instance by fixing some $\varepsilon_{1}$ ). For $\varepsilon \in\left(0, \varepsilon_{0}\right)$, we denote $J_{\varepsilon}$ the pullback of $J_{f}$ on $\hat{M}$ and $g_{\varepsilon}$ the pullback of $g_{f}$ on $\hat{M}$, and $\left(J_{0}, g_{0}\right)$ the pullback of the approximate solution $\left(J_{\varepsilon}, g_{\varepsilon}\right)$. Thus, we have a smooth family of almost-Kähler structures $\left(J_{\varepsilon}, g_{\varepsilon}\right)_{0 \leq \varepsilon<\varepsilon_{0}}$ on a fixed symplectic manifold $(\hat{M}, \hat{\omega})$.

Observe that in the ALE model space $\left(X=T^{*} S^{2}, \omega_{X}=d d^{c} u\right)$, the zero section $S_{0}$ of $T^{*} S^{2} \rightarrow S^{2}$ is a Lagrangian sphere. Moreover, $T^{*} S^{2}$ is an hyperKähler manifold, and for a different choice of complex structure in the hyperKähler family (namely, the choice that yields the minimal resolution of $\mathbb{C}^{2} / \mathbb{Z}_{2}$ ), the zero section is actually a holomorphic copy of $\mathbb{C} P^{1}$.

It is a well-known consequence of Wirtinger's inequality that holomorphic surfaces minimize volume in their homology class.

The zero section is not holomorphic for our choice of complex structure on $T^{*} S^{2}$, but it still is minimal, since we have endowed $T^{*} S^{2}$ with the Eguchi-Hanson metric. In particular, it is Hamiltonian stationary, which is to say that it verifies (2).

This implies that, when performing the gluing construction in Darboux charts, as we did in section 3. $S_{0}$ provides a Hamiltonian stationary (actually, minimal) sphere $S$ in the connected sum manifold $\left(\hat{M}, \hat{\omega}, J_{0}, g_{0}\right)$.

A natural question, therefore, is the following: For positive, small enough, $\varepsilon$, is there a representative of the homology class of $[S]$ - more precisely, a Hamiltonian deformation of $S$ - that is a Hamiltonian stationary sphere for the metric $g_{\varepsilon}$ ?

We prove that the answer is yes, extending what has been obtained in [8] to the case of almost-Kähler smoothings.

We need to find representative of the vanishing cycle $[S]$ that verify the equation (2) with respect to the metric $g_{\varepsilon}$, for $\varepsilon$ small enough. It was proven by Oh [37], Theorem 1, that the corresponding Euler-Lagrange equation is
$$\delta_{\varepsilon} \alpha_{\varepsilon}=0,$$
where $\delta_{\varepsilon}$ is the codifferential associated to the metric $\hat{g}_{\varepsilon}$, and $\alpha_{\varepsilon}$ is the Maslov form:
$$\left.\alpha_{\varepsilon}:=H_{\varepsilon}\right\lrcorner \hat{\omega},$$
where $H_{\varepsilon}$ is the mean curvature vector.
Consider the embedding
$$\iota_{0}: S^{2} \hookrightarrow \hat{M}$$
of the Lagrangian sphere in $(\hat{M}, \hat{\omega})$ that is minimal for $\left(J_{0}, g_{0}\right)$.
By Weinstein's Lagrangian neighborhood theorem (see [29], Theorem 3.3), we can identify a neighborhood of $\iota_{0}\left(S^{2}\right)$ with a neighborhood $\mathcal{U}$ of the zero section in $\left(T^{*} S^{2},-d \lambda\right)$ by a symplectomorphism $\psi$. Hamiltonian deformations of $\iota_{0}$ are therefore given by functions $u \in \mathcal{C}^{\infty}\left(S^{2}\right)$ such that $\|d u\|_{\mathcal{C}^{0}}$ is small enough that $d u \in \mathcal{U}$. For such a function $u$ we denote
$$i_{u}: S^{2} \hookrightarrow \mathcal{U}$$
the associated immersion. We still denote by $J_{\varepsilon}$ and $g_{\varepsilon}$ the almost complex structure and associated metrics pulled back by $\psi$ on $\mathcal{U}$. Let $g_{\varepsilon, u}$ be the restriction of $g_{\varepsilon}$ to $\iota_{u}\left(S^{2}\right)$. Then the immersion $\iota_{u}$ is Hamiltonian stationary for $g_{\varepsilon}$ if it is a critical point for the volume functional
$$u \mapsto \int_{i_{u}\left(S^{2}\right)} \operatorname{vol}_{g_{\varepsilon, u}} .$$

Notice that this equation is not linear in $u$, the induced metric on $S^{2}$ depends on the embedding encoded by $d u$. The linearisation $\mathcal{L}$ at 0, in the Kähler setting, is given by Oh's formula ([37], Theorem 3.4). He proves the following on a Kähler manifold: Let $u_{t}$ be a family of functions on $S^{2}$, such that $u_{0}=0$, giving a Hamiltonian deformation $S_{t}:=\iota_{u_{t}}\left(S^{2}\right)$. Then
$$\begin{aligned}
\frac{d^{2}}{d t^{2}}{ }_{\mid t=0} \operatorname{Vol}\left(S_{t}\right) & =\int_{S_{0}} \dot{u} \mathcal{L} \dot{u} \operatorname{vol}_{0} \\
& =\int_{S_{0}}\left\langle\Delta_{0} d \dot{u}, d \dot{u}\right\rangle-\operatorname{Ric}_{0}\left(J_{0} d \dot{u}, J_{0} d \dot{u}\right)-2\left\langle d \dot{u} \otimes d \dot{u} \otimes \alpha_{0}, S\right\rangle+\left\langle d \dot{u}, \alpha_{0}\right\rangle^{2} \operatorname{vol}_{0}
\end{aligned}$$
where $\alpha_{0}$ is the Maslov form for $\iota_{0}$, Ric ${ }_{0}$ is the Ricci curvature of $\hat{g}_{0}$ restricted to $S_{0}=i_{0}\left(S^{2}\right)$, and $\mathrm{vol}_{0}$ is the associated volume. In our setting, the manifold $\left(\hat{M}, \hat{\omega}, J_{0}\right)$ is not Kähler; however,up to reducing the Lagrangian neighborhood, we may assume that the structure ( $\hat{\omega}, J_{0}, g_{0}$ ) is Kähler on $\mathcal{U}$, since we may thus avoid the region where the Nijenhuis tensor does not vanish. As a consequence, we may apply Oh's formula, as in its proof, the Kähler hypothesis is only used at $t=0$.

This allow us to prove:
Proposition 38. For $\varepsilon$ small enough, the almost Kähler manifold $\left(\hat{M}, \hat{\omega}, J_{\varepsilon}\right)$ admits a Lagrangian homology class that is represented by a Hamiltonian stationary sphere.

Proof. Consider the operator
$$\begin{aligned}
B: \mathcal{C}^{2, \alpha}\left(\mathcal{A} \mathcal{C}_{\hat{\omega}}\right) \times \mathcal{C}^{4, \alpha}\left(S^{2}\right) & \rightarrow \mathcal{C}^{0, \alpha}\left(S^{2}\right) \\
(J, u) & \mapsto \delta_{J, u} \alpha_{J, u}
\end{aligned}$$
The operator is well defined on the family $\left(J_{\varepsilon}\right)$. Indeed, in local coordinates on $L$, if
$$\left\{\begin{array}{l}
g_{\varepsilon, u}=g_{a b} d x_{a} d x_{b} \\
\alpha_{\varepsilon, u}=\alpha_{a} d x_{a}
\end{array}\right.$$
then
$$\delta_{\varepsilon, u} \alpha_{\varepsilon, u}=-\frac{\partial h^{a b}}{\partial x_{b}} \alpha_{a}-h^{a b} \frac{\partial \alpha_{a}}{\partial x_{b}}-\frac{1}{2} h^{a b} \alpha_{a} \frac{\partial}{\partial x_{b}}\left(\log \left(\operatorname{det} h_{c d}\right)\right) .$$
Thus, the equation invovles first derivatives of the coefficients of $\alpha_{\varepsilon, u}$ and $g_{\varepsilon, u}$. Now, by definition, $g_{\varepsilon, u}$ involves second-order derivatives of $u$, as well as the coefficients of $g_{\varepsilon}$. The mean curvature vector (thus, the Maslow form) therefore involves third-order derivatives of $u$ and first-order derivatives of the coefficients of $g_{\varepsilon}$. Finally, as a whole, the equation is of order 4 in $u$ and its coefficients involve second derivatives of $g_{\varepsilon}$; we conclude using estimates (49) and (48).

It verifies $B\left(J_{X}, 0\right)=0$, and, by (54), our problem reduces to finding zeroes of $u \mapsto B\left(J_{\varepsilon}, u\right)$ for $\varepsilon$ small enough. We therefore need to apply the Implicit Function Theorem to $B$ at $\left(J_{X}, 0\right)$.

The linearisation of $u \mapsto B(J, u)$ at ( $J_{X}, 0$ ) is given by (55). In our framework, $S_{0}$ is actually minimal, thus $\alpha_{0}$ vanishes. Moreover, $g_{0}$ is given on $\mathcal{U}$ by the Ricci-flat Eguchi-Hanson metric. Thus in our setting, we get
$$\mathcal{L} \dot{u}=\Delta^{2} \dot{u} .$$

Thus, since constant functions $u$ result in trivial deformation, we have that for $k>4, \mathcal{L}$ realizes an isomorphism between the Hölder spaces
$$\mathcal{L}: \mathcal{C}^{k, \alpha}\left(S^{2}\right) / \mathbb{R} \rightarrow \mathcal{C}_{0}^{k-4, \alpha}\left(S^{2}\right):=\left\{f \in \mathcal{C}^{k-4, \alpha}\left(S^{2}\right), \int_{S^{2}} f \operatorname{vol}_{g_{0,0}}=0\right\} .$$
This observation, along with the estimate (49), allows us to apply the inverse function theorem to
$$\begin{aligned}
B: \mathcal{C}^{2, \alpha}\left(\mathcal{A} \mathcal{C}_{\hat{\omega}}\right) \times \mathcal{C}^{4, \alpha}\left(S^{2}\right) / \mathbb{R} & \rightarrow \mathcal{C}_{0}^{0, \alpha}\left(S^{2}\right) \\
(J, u) & \mapsto \delta_{J, u} \alpha_{J, u}
\end{aligned}$$
at $\left(J_{X}, 0\right)$; in particular for $\varepsilon$ small enough, there is a unique $u_{\varepsilon} \in \mathcal{C}^{4, \alpha}\left(S^{2}\right) / \mathbb{R}$ such that the embedding $\iota_{u_{\varepsilon}}: S^{2} \hookrightarrow \mathcal{U}$ is Hamiltonian stationary for the metric $g_{\varepsilon}$.

Now, $u_{\varepsilon}$ is solution of the 4th order elliptic equation
$$B\left(J_{\varepsilon}, u_{\varepsilon}\right)=0 .$$
Since, according to theorem 1, $J_{\varepsilon}$ is actually smooth, and so is the associated metric whose coefficients appear in the expression of the differential operator $B$, we can, once again, use a bootstrapping argument to ensure that each function $u_{\varepsilon}$ is actually smooth. \(\square\)

Remark 39. One may wonder wether we could also retrieve the second part of the result by Biquard and Rollin [8], Theorem D -namely, the minimizing property. To do this, one would need to check that the results obtained by Schoen and Wolfson [41] can be extended to the almost-Kähler setting.

\section*{Annex: ALE metric on $T^{*} S^{2}$ as a smoothing of the $A_{1}$ singularity.}

We recall some results from the last part of Stenzel's paper [43].
Consider thea singularity $\mathbb{C}^{2} / \mathbb{Z}_{2}$ endowed with the Euclidean Kähler structure $\left(J_{0}, \omega_{0}, g_{0}\right)$. We identify $\mathbb{C}^{2} / \mathbb{Z}_{2}$ to the cone
$$\mathcal{C}=\left\{z \in \mathbb{C}^{3}, z_{1}^{2}+z_{2}^{2}+z_{3}^{2}=0\right\} \subset \mathbb{C}^{3}$$
and we consider smoothings of the form
$$C_{\varepsilon}=\left\{z \in \mathbb{C}^{3}, z_{1}^{2}+z_{2}^{2}+z_{3}^{2}=\varepsilon^{2}\right\},$$
endowed with the restriction of the natural complex structure on $\mathbb{C}^{3}$. Here $\varepsilon$ is a positive real number. The construction would actually make sense for a complex parameter $\varepsilon$. In that case, we would retrieve the family of hyperKähler metrics on $O(-2)$ that were obtained by Kronheimer [23]. However, this will not intervene in our construction.

We now recall the construction of the Ricci-flat Kähler metric on $C_{\epsilon}$ obtained by Stenzel in [43].
We denote by $\tau=|z|_{\mid C_{\epsilon}}^{2}$ the restriction of the squared norm in $\mathbb{C}^{3}$ to the quadric $C_{\epsilon}$, and we look for a Kähler potential under the form $u=f \circ \tau$. To find a Ricci-flat metric, we wish to solve the Monge-Ampère equation :
$$\operatorname{Ric}\left(\omega_{u}\right)=-i \partial \bar{\partial} \log \operatorname{det}\left(u_{i \bar{j}}\right)=0,$$
where the subscripts denote derivation with respect to local coordinates on $C_{\epsilon}$.
Using proper coordinates, a straightforward if somewhat tedious computation, which can be found in Patrizio and Wong ([39]), shows that $f \circ \tau$ is a solution of the Monge-Ampère equation (58) whenever $f$ satisfies the following ODE :
$$\tau f^{\prime}(\tau)^{2}+f^{\prime \prime}(\tau) f^{\prime}(\tau)\left(\tau^{2}-\varepsilon^{4}\right)=c$$
where $c$ is a positive constant.
This EDO, together with sensible initial conditions, admits $f(\tau)=\sqrt{\tau+\varepsilon^{2}}$ as the unique solution. The Ricci-flat Kähler metric associated to this potential will be denoted $\omega_{X, \varepsilon}$ on $C_{\epsilon}$. The associated Riemannian metric $g_{X, \varepsilon}$ coincides with a rescaling of the Eguchi-Hanson metric; however, the complex structure $J_{X, \varepsilon}$ differs from the standard one, as explained earlier.

To study the ALE character of this metric, observe that $C_{\epsilon}$ can be identified to $T^{*} S^{2}$. Indeed, separating the real and imaginary parts, we have
$$C_{\epsilon}=\left\{X+i Y,(X, Y) \in \mathbb{R}^{3} \times \mathbb{R}^{3} \mid\langle X, X\rangle-\langle Y, Y\rangle=\epsilon,\langle X, Y\rangle=0\right\},$$
whereas
$$T^{*} S^{2}=\left\{(X, \xi) \in \mathbb{R}^{3} \times \mathbb{R}^{3} \mid\|X\|=1,\langle X, \xi\rangle=0\right\},$$
thus the map
$$\begin{aligned}
\Psi_{\varepsilon}: & T^{*} S^{2} \rightarrow Q_{\varepsilon} \\
(x, \xi) & \mapsto\left(\varepsilon \cosh (\|\xi\|) x, \varepsilon \frac{\sinh (\|\xi\|)}{\|\xi\|} \xi .\right.
\end{aligned}$$
identifies the smoothing $C_{\varepsilon}$ with the cotangent of the sphere.
Remark 40. This maps the zero section $S^{2}=\{(x, 0),\|x\|=1\} \subset T^{*} S^{2}$ to the subset $\{(\varepsilon x, 0),\| \|=$ $1\} \subset Q_{\varepsilon}$. When $\varepsilon$ goes to 0, the section nulle is collapses on the singular point $(0,0) \in \mathbb{C}^{2} / \mathbb{Z}_{2}$.

Using spherical coordinates on $T^{*} S^{2} \backslash S^{2}$ outside the zero section, we see that the Ricci-flat Kähler structure we have obtained on $C_{\varepsilon}$ pulls back to
$$\begin{aligned}
J_{X, \varepsilon} \frac{\partial}{\partial t} & =-X_{3}, J_{S} X_{1}=-\tanh (t) X_{2} \\
\omega_{X, \varepsilon} & =\sqrt{2} \varepsilon\left(\cosh (t) \alpha_{3} \wedge d t+\sinh (t) \alpha_{2} \wedge \alpha_{1}\right) \\
g_{X, \varepsilon} & =\sqrt{2} \varepsilon\left(\cosh (t) d t^{2}+\sinh (t) \tanh (t) \alpha_{1}^{2}+\cosh (t)\left(\alpha_{2}^{2}+\alpha_{3}^{2}\right)\right)
\end{aligned}$$

To compare to the Euclidean metric, rather than to the conical one, on $\mathbb{C}^{2} / \mathbb{Z}_{2}$, we change variables radially, setting $\cosh (t)=\frac{s^{2}}{2}$. This gives
$$\begin{aligned}
J_{X, \varepsilon} \frac{\partial}{\partial s} & =-\frac{2 s}{\sqrt{s^{4}-4}} X_{3}, J_{S} X_{1}=-\sqrt{1-\frac{4}{s^{4}}} X_{2} \\
\frac{1}{\sqrt{2} \varepsilon} g_{X, \varepsilon} & =\left(1-\frac{4}{s^{4}}\right)^{-1} d s^{2}+\frac{s^{2}}{4}\left(1-\frac{4}{s^{4}}\right) \alpha_{1}^{2}+\frac{s^{2}}{4}\left(\alpha_{2}^{2}+\alpha_{3}^{2}\right) \\
\omega_{X, \varepsilon} & =\sqrt{2} \varepsilon\left(\frac{s}{2 \sqrt{1-\frac{4}{s^{4}}}} \alpha_{3} \wedge d s+\frac{s^{2}}{4} \sqrt{1-\frac{4}{s^{4}}} \alpha_{2} \wedge \alpha_{1}\right)
\end{aligned}$$

Comparing to the Euclidean structure:
$$\begin{aligned}
J_{0} \frac{\partial}{\partial s} & =-\frac{2}{s} X_{3}, \quad J_{0} X_{1}=-X_{2} \\
g_{0} & =d s^{2}+\frac{s^{2}}{4}\left(\alpha_{1}^{2}+\alpha_{2}^{2}+\alpha_{3}^{2}\right)
\end{aligned}$$
we see that the derivatives of the coefficient at any order verify
$$\begin{aligned}
\partial^{j}\left(J_{X, \varepsilon}-J_{0}\right) & =O\left(s^{-4-j}\right) \\
\partial^{j}\left(\sqrt{2} \varepsilon g_{X, \varepsilon}-g_{0}\right) & =O\left(s^{-4-j}\right) ;
\end{aligned}$$
thus the metric is ALE of order 4.
Remark 41. We recognize a rescaling of the Eguchi-Hanson metric on $T^{*} S^{2}$. Howerver, the complex structure is different from the one on $T^{*} \mathbb{C} P^{1}=O(-2)$ obtained when blowing up the origin in $\mathbb{C}^{2} / \mathbb{Z}_{2}$. Indeed, instead of an exeptional divisor biholomorphic to $\mathbb{C} P^{1}$ (corresponding to the zero section), we have a Lagrangian 2-sphere.

\section*{References}
\begin{itemize}
\item[] [1] V. Apostolov and T. Draghici. The curvature and the integrability of almost-Kähler manifolds: a survey. Symplectic and contact topology: interactions and perspectives (Toronto, ON/Montreal, QC, 2001), 35:25-53, 2003.
\item[] [2] C. Arezzo and F. Pacard. Blowing up and desingularizing constant scalar curvature Kähler manifolds. Acta Math., 196(2):179-228, 2006.
\item[] [3] C. Arezzo and F. Pacard. Blowing up Kähler manifolds with constant scalar curvature. II. Ann. of Math. (2), 170(2):685-738, 2009.
\item[] [4] C. Arezzo, F. Pacard, and M. Singer. Extremal metrics on blowups. Duke Math. J., 157(1):1-51, 2011.
\end{itemize}
\begin{itemize}
\item[] [5] T. Aubin. Équations du type Monge-Ampère sur les variétés kählériennes compactes. Bull. Sci. Math. (2), 102(1):63-95, 1978.
\item[] [6] R. Bartnik. The mass of an asymptotically flat manifold. Comm. Pure Appl. Math., 39(5):661-693, 1986.
\item[] [7] A.L. Besse. Einstein manifolds, volume 10 of Ergebnisse der Mathematik und ihrer Grenzgebiete (3) [Results in Mathematics and Related Areas (3)]. Springer-Verlag, Berlin, 1987.
\item[] [8] O. Biquard and Y. Rollin. Smoothing singular constant scalar curvature Kähler surfaces and minimal Lagrangians. Adv. Math., 285:980-1024, 2015.
\item[] [9] F. Catanese. Everywhere nonreduced moduli spaces. Invent. Math., 98(2):293-310, 1989.
\item[] [10] Y. Choquet-Bruhat and D. Christodoulou. Elliptic systems in $H_{s, \delta}$ spaces on manifolds which are Euclidean at infinity. Acta Math., 146(1-2):129-150, 1981.
\item[] [11] J. Chu, V. Tosatti, and B. Weinkove. The Monge-Ampère equation for non-integrable almost complex structures. arXiv preprint arXiv:1603.00706.
\item[] [12] P. Delanoë. Sur l'analogue presque-complexe de l'équation de Calabi-Yau. Osaka J. Math., 33(4):829-846, 1996.
\item[] [13] M. Dellnitz and I. Melbourne. The equivariant Darboux theorem. In Exploiting symmetry in applied and numerical analysis (Fort Collins, CO, 1992), volume 29 of Lectures in Appl. Math., pages 163-169. Amer. Math. Soc., Providence, RI, 1993.
\item[] [14] S. K. Donaldson. Remarks on gauge theory, complex geometry and 4-manifold topology. In Fields Medallists' lectures, volume 5 of World Sci. Ser. 20th Century Math., pages 384-403. World Sci. Publ., River Edge, NJ, 1997.
\item[] [15] S. K. Donaldson and P. B. Kronheimer. The geometry of four-manifolds. Oxford Mathematical Monographs. The Clarendon Press, Oxford University Press, New York, 1990. Oxford Science Publications.
\item[] [16] A. Fujiki. Moduli space of polarized algebraic manifolds and Kähler metrics [translation of Sûgaku 42 (1990), no. 3, 231-243; MR1073369 (92b:32032)]. Sugaku Expositions, 5(2):173-191, 1992. Sugaku Expositions.
\item[] [17] A. Futaki. An obstruction to the existence of Einstein Kähler metrics. Invent. Math., 73(3):437-443, 1983.
\item[] [18] P. Gauduchon. Calabi's extremal kähler metrics: An elementary introduction. Preprint, 2010.
\item[] [19] H.-J. Hein, R. Rasdeaconu, and I. Suvaina. On the classification of ALE Kähler manifolds. arXiv preprint arXiv:1610.05239, 2016.
\item[] [20] D. Joyce, Y.-I. Lee, and R. Schoen. On the existence of Hamiltonian stationary Lagrangian submanifolds in symplectic manifolds. Amer. J. Math., 133(4):1067-1092, 2011.
\item[] [21] R. Kobayashi. A remark on the Ricci curvature of algebraic surfaces of general type. Tohoku Math. J. (2), 36(3):385-399, 1984.
\item[] [22] S. Kobayashi. Transformation groups in differential geometry. Springer Science \& Business Media, 2012.
\item[] [23] P.B. Kronheimer. The construction of ALE spaces as hyper-Kähler quotients. J. Differential Geom., 29(3):665-683, 1989.
\end{itemize}
[24] C. LeBrun and S. R. Simanca. Extremal Kähler metrics and complex deformation theory. Geom. Funct. Anal., 4(3):298-336, 1994.
[25] M. Lejmi. Extremal almost-Kähler metrics. Internat. J. Math., 21(12):1639-1662, 2010.
[26] M. Lejmi. Stability under deformations of Hermite-Einstein almost Kähler metrics. Ann. Inst. Fourier (Grenoble), 64(6):2251-2263, 2014.
[27] R.B. Lockhart and R.C. Mc Owen. Elliptic differential operators on noncompact manifolds. Ann. Sc. Norm. Super. Pisa Cl. Sci., 12(3):409-447, 1985.
[28] Y. Matsushima. Sur la structure du groupe d'homéomorphismes analytiques d'une certaine variété kählérienne. Nagoya Math. J., 11:145-150, 1957.
[29] D. McDuff and D. Salamon. Introduction to symplectic topology. Oxford Mathematical Monographs. The Clarendon Press, Oxford University Press, New York, second edition, 1998.
[30] R.B. Melrose. The Atiyah-Patodi-Singer index theorem, volume 4 of Research Notes in Mathematics. A K Peters, Ltd., Wellesley, MA, 1993.
[31] V. Minerbe. On the asymptotic geometry of gravitational instantons. Ann. Sci. Éc. Norm. Supér. (4), 43(6):883-924, 2010.
[32] R. Miranda. On canonical surfaces of general type with $K^{2}=3 \chi-10$. Math. Z., 198(1):83-93, 1988.
[33] O. Mohsen. Symplectomorphismes hamiltoniens et métriques kählériennes. 2003.
[34] C. B.Jr Morrey. On the analyticity of the solutions of analytic non-linear elliptic systems of partial differential equations. I. Analyticity in the interior. Amer. J. Math., 80:198-218, 1958.
[35] C.B. Morrey, Jr. Multiple integrals in the calculus of variations. Classics in Mathematics. SpringerVerlag, Berlin, 2008. Reprint of the 1966 edition [MR0202511].
[36] Y.-G. Oh. Second variation and stabilities of minimal Lagrangian submanifolds in Kähler manifolds. Invent. Math., 101(2):501-519, 1990.
[37] Y.-G. Oh. Volume minimization of Lagrangian submanifolds under Hamiltonian deformations. Math. Z., 212(2):175-192, 1993.
[38] R. Pacard and T. Rivière. Linear and Nonlinear Aspects of Vortices: The Ginzburg-andau Model, volume 39. Springer Science \& Business Media, 2012.
[39] G. Patrizio and P.-M. Wong. Stein manifolds with compact symmetric center. Math. Ann., 289(3):355-382, 1991.
[40] M. Schlessinger. Rigidity of quotient singularities. Invent. Math., 14(1):17-26, 1971.
[41] R. Schoen and J. Wolfson. Minimizing area among Lagrangian surfaces: the mapping problem. J. Differential Geom., 58(1):1-86, 2001.
[42] C. Spotti. Deformations of nodal Kähler-Einstein del Pezzo surfaces with discrete automorphism groups. J. Lond. Math. Soc. (2), 89(2):539-558, 2014.
[43] M.B. Stenzel. Ricci-flat metrics on the complexification of a compact rank one symmetric space. Manuscripta Math., 80(2):151-163, 1993.
[44] G. Székelyhidi. The Kähler-Ricci flow and K-polystability. Amer. J. Math., 132(4):1077-1090, 2010.
\begin{itemize}
\item[] [45] G. Székelyhidi. On blowing up extremal Kähler manifolds. Duke Math. J., 161(8):1411-1453, 2012.
\item[] [46] G. Székelyhidi. Blowing up extremal Kähler manifolds II. Invent. Math., 200(3):925-977, 2015.
\item[] [47] Gábor Székelyhidi. An introduction to extremal Kähler metrics, volume 152. American Mathematical Soc., 2014.
\item[] [48] B. Weinkove. The Calabi-Yau equation on almost-Kähler four-manifolds. J. Differential Geom., 76(2):317-349, 2007.
\end{itemize}