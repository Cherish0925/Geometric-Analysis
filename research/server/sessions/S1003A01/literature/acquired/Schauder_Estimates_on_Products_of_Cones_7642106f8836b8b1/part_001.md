---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Schauder Estimates on Products of Cones]

---
source_file: 2002_07668.pdf
converter: mathpix
format: mmd
---

\title{
SCHAUDER ESTIMATES ON PRODUCTS OF CONES
}

\author{
MARTIN DE BORBON AND GREGORY EDWARDS
}

\begin{abstract}
We prove an interior Schauder estimate for the Laplacian on metric products of two dimensional cones with a Euclidean factor, generalizing the work of Donaldson and reproving the Schauder estimate of Guo-Song. We characterize the space of homogeneous subquadratic harmonic functions on products of cones, and identify scales at which geodesic balls can be well approximated by balls centered at the apex of an appropriate model cone. We then locally approximate solutions by subquadratic harmonic functions at these scales to measure the Hölder continuity of second derivatives.
\end{abstract}

\section*{1. Introduction}

In [Don12], Donaldson laid the foundation for studying geometric and analytic properties of Kähler metrics with conical singularities along a smooth hypersurface. There, Donaldson proved the Schauder estimate for the Laplacian of such metrics, establishing an important step toward the eventual solution of the YauTian-Donaldson conjecture relating the existence of Kähler-Einstein metrics on Fano manifolds to K-stability [CDS15a, CDS15b, CDS15c]. The Schauder estimate for metrics with cone singularities along a smooth hypersurface was later reproved by Guo-Song [GS16] and Gui-Yin [GY18].

Conical Kähler metrics have since received considerable attention by geometers, particularly for Kähler metrics having conical singularities along a simple normal crossing divisor. The Schauder estimate is an important step in developing the linear elliptic theory necessary to construct conical Kähler-Einstein metrics, and Guo-Song established the Schauder estimate for linear elliptic and parabolic equations with conical singularities along a simple normal crossing divisor [GS18].

Near an intersection of irreducible components of the cone divisor, these conical Kähler metrics are locally modeled by the Cartesian product of two dimensional cones with cone angle less than $2 \pi$, and a Euclidean factor. In this paper we consider such products of cones as themselves Riemannian cones with singular rays, and establish a sharp Schauder estimate for the Laplacian, generalizing the work of Donaldson and reproving the results of Guo-Song. Our Schauder estimate is independent of Guo-Song, and we present it as the techniques may prove useful in further works.
1.1. Main result. Let us write $C\left(S_{2 \pi \beta}^{1}\right)$ for the cone over a circle of length $2 \pi \beta>0$. For $m \geq 3$ and $n \geq 1$, we consider the product space
$$C\left(S_{2 \pi \beta_{1}}^{1}\right) \times \ldots \times C\left(S_{2 \pi \beta_{n}}^{1}\right) \times \mathbf{R}^{m-2 n} .$$
In this article we restrict to the case where $0<\beta_{a}<1$ for all $a=1, \ldots, n$. We use polar coordinates $\left(r_{a}, \theta_{a}\right)$ on each of the cone factors and standard Cartesian
coordinates $s=\left(s_{1}, \ldots, s_{m-2 n}\right)$ on the Euclidean part, so the cone metric in these coordinates is
$$g=\sum_{a=1}^{n}\left(d r_{a}^{2}+\beta_{a}^{2} r_{a}^{2} d \theta_{a}^{2}\right)+d s^{2}$$

We use $a, b$ to denote indices in $1, \ldots, n$, corresponding to the cone factors, and indices $i, j$ in $1, \ldots, m-2 n$ for the Euclidean directions. Let $\mathcal{D}_{2}$ be the set of second order differential operators given by:
\begin{itemize}
\item[-] pure Euclidean:
$$\frac{\partial^{2}}{\partial s_{i} \partial s_{j}} ;$$
\item[-] mixed conical-Euclidean:
$$\frac{\partial^{2}}{\partial r_{a} \partial s_{i}}, \quad \frac{1}{r_{a}} \frac{\partial^{2}}{\partial \theta_{a} \partial s_{i}} ;$$
\item[-] mixed conical, $a \neq b$ :
$$\frac{\partial^{2}}{\partial r_{a} \partial r_{b}}, \quad \frac{1}{r_{a} r_{b}} \frac{\partial^{2}}{\partial \theta_{a} \partial \theta_{b}}, \quad \frac{1}{r_{b}} \frac{\partial^{2}}{\partial r_{a} \partial \theta_{b}} ;$$
\item[-] conical Laplacians:
$$\Delta_{\beta_{a}}=\frac{\partial^{2}}{\partial r_{a}^{2}}+\frac{1}{r_{a}} \frac{\partial}{\partial r_{a}}+\frac{1}{\beta_{a}^{2} r_{a}^{2}} \frac{\partial^{2}}{\partial \theta_{a}^{2}} .$$
\item[-] pure conical, for indices $a$ with $\beta_{a}<1 / 2$ :
$$\frac{\partial^{2}}{\partial r_{a}^{2}}, \quad \frac{1}{r_{a}^{2}} \frac{\partial^{2}}{\partial \theta_{a}^{2}}, \quad \frac{1}{r_{a}} \frac{\partial^{2}}{\partial r_{a} \partial \theta_{a}} ;$$
\end{itemize}
In this collection of differential operators we are excluding the pure conical elements of the Hessian for those angles $\beta \geq 1 / 2$.

Our main result is a version of the interior Schauder estimates for the Laplace operator of our singular metric,
$$\Delta=\Delta_{\beta_{1}}+\ldots+\Delta_{\beta_{n}}+\Delta_{\mathbf{R}^{m-2 n}} .$$

We define
$$\mu=\min \left\{\begin{array}{l}
1 \\
1 / \beta_{a}-1 \text { for } \beta_{a} \geq 1 / 2 \\
1 / \beta_{a}-2 \text { for } \beta_{a}<1 / 2
\end{array}\right.$$

Theorem 1.1. Let $0<\alpha<\mu$. There is a constant $C=C\left(\alpha, \beta_{a}, m\right)$ with the following property. If $u \in W^{1,2}\left(B_{2}\right)$ is a weak solution of $\Delta u=f$ with $f \in C^{\alpha}\left(B_{2}\right)$, then for every $x \in B_{1}$ and every $D \in \mathcal{D}_{2}$ there is $\tau \in \mathbf{R}$ and constant $K>0$ such that
$$\left(\rho^{-m} \int_{B(x, \rho)}|D u-\tau|^{2}\right)^{1 / 2} \leq K \rho^{\alpha}$$
for every $0<\rho<1$. Moreover,
$$|\tau|+K \leq C\left(|f(x)|+|f|_{C^{\alpha}(x)}+\|u\|_{L^{2}\left(B_{2}\right)}\right) .$$

Our main estimate (1.2) gives a bound for $D u$ in a Campanato space, which is known to be equivalent to a bound on its Hölder coefficient:
$$\sup _{|x-y|<1 / 2} \frac{|D u(y)-D u(x)|}{|x-y|^{\alpha}} .$$
We point out three main differences between Theorem 1.1 and the standard Schauder estimates for the Euclidean Laplacian.
\begin{itemize}
\item[(1)] We do not estimate all the second order derivatives. Indeed, it is easy to see that
$$u=r^{1 / \beta} \cos \theta$$
is a harmonic function on $C\left(S_{2 \pi \beta}^{1}\right)$ and $\partial_{r}^{2} u \sim r^{1 / \beta-2}$ is unbounded if $\beta>1 / 2$ and $r \rightarrow 0$. Note however that $\mathcal{D}_{2}$ contains all entries of the Hessian except for the terms $\partial_{r_{a}}^{2}$ and $r_{a}^{-2} \partial_{\theta_{a}}^{2}$ and $r_{a}^{-1} \partial_{\theta_{a} r_{a}}^{2}$ for those $\beta_{a}>1 / 2$.
\item[(2)] We require $\alpha<1 / \beta-1$ for those $\beta>1 / 2$. To see that this upper bound on $\alpha$ is optimal, consider the harmonic function
$$u=r^{1 / \beta} s \cos \theta$$
on $C\left(S_{2 \pi \beta}^{1}\right) \times \mathbf{R}$. Then $\partial^{2} u / \partial r \partial s$ is $C^{\alpha}$ for $\alpha=1 / \beta-1$. Similarly, for $\beta<1 / 2$, we have that $\partial_{r}^{2}\left(r^{1 / \beta} \cos \theta\right)$ is $C^{\alpha}$ with $\alpha=1 / \beta-2$.
A consequence of our methods is that the upper bound on $\alpha$ is determined by the next indicial root after 2. That is, there are no homogeneous harmonic functions with growth rate $2+\alpha$ for any $0<\alpha<\mu$. Note that, since we always assume $0<\alpha<1$, the restriction $\alpha<1 / \beta_{a}-2$ only applies if $1 / 3<\beta_{a}<1 / 2$.
\item[(3)] For $u$ as in Theorem 1.1, the first derivatives $\partial_{r_{a}} u$ and $r_{a}^{-1} \partial_{\theta_{a}} u$ vanish along $\left\{r_{a}=0\right\}$. This is a manifestation of the fact that $g$ has non-trivial holonomy along arbitrary small loops that go around the conical set. In particular, $\partial_{r_{a}} P$ and $r_{a}^{-1} \partial_{\theta_{a}} P$ vanish identically for any 'sub-linear harmonic polynomials' $P \in \mathcal{H}_{\leq 1}$; see Proposition 3.4
\end{itemize}

Our metric is locally Euclidean on its regular part, so it follows from the standard regularity theory for the Euclidean Laplacian that $u$ is locally $C^{2, \alpha}$ on the locus where none of the $r_{a}$ vanishes. The second derivative $D u$ is then point-wise defined outside the conical singularities, and Theorem 1.1 guarantees that $D u$ extends continuously over points $x$ lying on the singular part $S=\cup_{a}\left\{r_{a}=0\right\}$ by setting $D u(x)=\tau$. Note however that the estimate (1.2) is non-trivial even when $x$ lies on the regular part. In fact, for regular points arbitrary close to the singular set, the Euclidean Schauder estimates only apply in arbitrary small scales, while our bound (1.2) holds for all $0<\rho<1$ independent of $x$.
1.2. Sketch of proof of Theorem 1.1. We use the approximation by polynomials technique, see [HL11, Chapter 5.4]. For simplicity, let us assume that $u$ is harmonic. The idea is then to expand $u$ on $B(x, 1)$ as a sum of 'homogeneous harmonic polynomials' and then subtract the subquadratic part $P$ from $u$, so that $u-P$ will vanish to order $2+\alpha$ at $x$. If we set $\tau=D P(x)$, then $D u-\tau$ will vanish to order $\alpha$ as stated in equation (1.2), provided we have control on the $C^{\alpha}$-norm of $D P$. The problem is that $x$ is not necessarily the vertex of a cone, so there are no dilations centered at $x$ and there is not such a notion as 'homogeneous harmonic polynomials' on $B(x, 1)$.

To deal with this we use appropriate model cones at each scale. More precisely, we fix some $0<\lambda<1$ and consider the balls $B\left(x, \lambda^{k}\right)$ for integers $k \geq 0$. The key point is that, if we fix some error $\epsilon_{0}>0$, then all but at most a finite number $N\left(\epsilon_{0}, \lambda\right)$ of the scales $\lambda^{k}$ are 'good', meaning that the rescaled ball $\lambda^{-k} B\left(x, \lambda^{k}\right)$ is isometric to a unit ball in a model cone $C(Y)$ with center at distance at most $\epsilon_{0}$ from the vertex; see Section 4.1. We approximate $u$ by subquadratic harmonic functions at each scale $\lambda^{k}$ in an iterative manner. We start with $u_{0}=u$ on $B(x, 1)$. If $\lambda^{k}$ is a good scale, we set $u_{k+1}=u_{k}-P_{k}$ on $B\left(x, \lambda^{k+1}\right)$ where $P_{k}$ is the subquadratic part; see Proposition 5.1. If $\lambda^{k}$ is a bad scale, we let $u_{k+1}=u_{k}$. We set $\tau_{k}=D P_{k}(x)$ and verify that $\tau=\sum_{k} \tau_{k}$ approximates $D u$ around $x$ in the sense that the estimate (1.2) holds.

Note that we do not obtain a harmonic 'polynomial $P=\sum_{k} P_{k}$ ' on $B(x, 1)$ that approximates $u$ up to order $2+\alpha$. Indeed, the polynomials $P_{k}$ are defined on smaller scales as $\lambda^{k} \rightarrow 0$. However, their values $D P_{k}(x)$ are defined and we can identify ${ }^{\prime} \tau=D P(x)$ '.
1.3. Angles equal to $\pi$. The case where some cone factors have angle $\pi$ is somewhat exceptional due to the additional quadratic harmonic function, $r_{a}^{2} e^{i \theta_{a}}$.

Assume $\beta_{a}=1 / 2$ for some cone factor and let $u \in W^{1,2}$ be a weak solution of $\Delta u=f$ with $f \in C^{\alpha}$. We use the branched covering map $\left(r_{a}, \tilde{\theta}_{a}\right) \rightarrow\left(r_{a}, 2 \tilde{\theta}_{a}\right)$ to pull-back $C\left(S_{2 \pi \beta_{a}}^{1}\right)$ into $\mathbf{R}^{2}$. Let $\tilde{u}$ and $\tilde{f}$ be the pull-backs of $u$ and $f$. It is easy to see that $\tilde{\Delta} \tilde{u}=\tilde{f}$, by writing test functions as a sum of even an odd parts with respect to $\tilde{\theta} \rightarrow \tilde{\theta}+\pi$. Then, in addition to the results of Theorem 1.1, we have
$$\left\|\frac{\partial^{2} u}{\partial r_{a}^{2}}\right\|_{L^{\infty}\left(B_{1}\right)}+\left\|\frac{1}{r_{a}} \frac{\partial u}{\partial r_{a}}\right\|_{L^{\infty}\left(B_{1}\right)}+\left\|\frac{1}{r_{a}^{2}} \frac{\partial^{2} u}{\partial \theta_{a}^{2}}\right\|_{L^{\infty}\left(B_{1}\right)} \leq C,$$
so that the pure conical derivatives in the $C\left(S_{2 \pi \beta_{a}}^{1}\right)$ direction are bounded for every index $a$ with $\beta_{a}=1 / 2$. Note however that this bound is sharp as the second derivative $\partial_{r}^{2}$ of the harmonic function $r_{a}^{2} e^{i \theta_{a}}$ does not extend continuously over $r_{a}=0$.
1.4. Comparison with other works. A first precedent for Theorem 1.1 is the work of Donaldson [Don12], which considers the case $C\left(S_{2 \pi \beta}^{1}\right) \times \mathbf{R}^{m-2}$. Donaldson proves the Schauder estimates via classical potential theory, differentiating twice Green's representation formula. The main work is on deriving a suitable 'polyhomogeneous' expansion of the Green's function around the conical set, which is done via separation of variables. Later, Guo-Song [GS16] gave a new proof of Donaldson's Schauder estimate without using potential theory. The method of Guo-Song gives a sharp estimate on the modulus of continuity of the second derivatives in terms of the Dini condition, along the lines of Wang [Wan06] in the smooth case. Their proof relies on approximation by smooth metrics with nonnegative Ricci curvature and the Cheng-Yau gradient estimate. More recently, Guo-Song [GS18] adapted their method to the case of normal crossing singularities $C\left(S_{2 \pi \beta_{1}}^{1}\right) \times \ldots \times C\left(S_{2 \pi \beta_{n}}^{1}\right) \times \mathbf{R}^{m-2 n}$ as considered in this paper. Yet another approach for the Schauder estimates on $C\left(S_{2 \pi \beta}^{1}\right) \times \mathbf{R}^{m-2}$ was given by Gui-Yin [GY18], considering also $\beta>1$ and higher order estimates. A main ingredient in Gui-Yin's work is an expansion formula for bounded harmonic functions, GY18, Proposition 5.2], and their methods are closer to ours.

The main feature of our work, is that we exploit the explicit knowledge of $\mathcal{H}_{\leq 2}$, the space of homogeneous harmonic functions of degree $\leq 2$. We derive Theorem 1.1 from the bounds on $|D P|_{\alpha}$ for $D \in \mathcal{D}_{2}$ and $P \in \mathcal{H}_{\leq 2}$. Indeed $|D P|_{\alpha}=0$, see Proposition 3.4 and Corollary 3.5. There are other variants of Theorem 1.1 that can be obtained by minor changes to our proof. For example, we can relax the requirement $\alpha<1 / \beta_{a}-2$ for those angles $\beta_{a}<1 / 2$, if we are not willing to estimate $\partial^{2} / \partial r_{a}^{2}$, etc. Our work does not rely on approximation by smooth metrics, and we expect to extend it to more general conical type singularities.

Organization. The rest of the paper is organized as follows. In Section 2 we establish elementary properties of weak solutions and harmonic approximation, see Lemma 2.4. In Section 3 we compute the subspace of homogeneous subquadratic harmonic functions for the model cones, see Proposition 3.4. In Section 4 we bound the number of bad scales (Lemma 4.1), and establish the monotonicity property for harmonic functions (Lemma 4.3). Finally, in Section 5 we complete the proof of Theorem 1.1.

Acknowledgments. The authors would like to thank Gábor Székelyhidi for suggesting this approach to prove the Schauder estimates.

The first named author was supported by the ANR grant ANR-17-CE40-0034: CCEM and would like to thank Gilles Carron for useful discussions.

The second author was supported by the National Science Foundation RTG: Geometry and Topology at the University of Notre Dame, grant number DMS-1547292.

\section*{2. $L^{2}$-THEORY}
2.1. Preliminaries and notation. We write
$$\mathbf{R}_{(\beta)}^{m}=C\left(S_{2 \pi \beta_{1}}^{1}\right) \times \ldots \times C\left(S_{2 \pi \beta_{n}}^{1}\right) \times \mathbf{R}^{m-2 n}$$
for our product space. We denote by either $B(x, \rho)$ or $B_{\rho}(x)$, a geodesic ball of center $x$ and radius $\rho$, with respect to the distance $d=d_{g}$ induced by $g$. If the center of the ball is zero, we simply write $B_{\rho}=B_{\rho}(0)$.

Note that $g$ is uniformly equivalent to the Euclidean metric, since
$$\left(\min _{a} \beta_{a}\right)^{2} g_{\mathbf{R}^{m}} \leq g \leq g_{\mathbf{R}^{m}} .$$
In particular, $\left(\min _{a} \beta_{a}\right) d_{\mathbf{R}^{m}} \leq d \leq d_{\mathbf{R}^{m}}$ and the geodesic balls of $g$ are uniformly comparable to Euclidean balls, in the sense that
$$B_{\mathbf{R}^{m}}(x, \rho) \subset B(x, \rho) \subset B_{\mathbf{R}^{m}}\left(x,\left(\min _{a} \beta_{a}\right)^{-1} \rho\right) .$$
Note that, if the center of the ball is located at zero, then $B_{\rho}=\left\{\sum_{a} r_{a}^{2}+\sum_{i} s_{i}^{2}<\rho^{2}\right\}$ agrees with the standard Euclidean ball.

Our $W^{1,2}$ and $C^{\alpha}$ function spaces are the standard ones of $\mathbf{R}^{m}$. These Sobolev and Hölder spaces can also be interpreted by measuring the corresponding defining norms with respect to the conically singular metric $g$. If follows from equation (2.1) that the respective $W^{1,2}$ and $C^{\alpha}$ norms defined by $g$ and $g_{\mathbf{R}^{m}}$ are then equivalent. Likewise, our integrals are always referred with respect to the Riemannian volume measure $d V_{g}$. Still, $d V_{g}$ is a constant multiple of the ordinary Lebesgue measure; the constant factor being equal to the product of the $\beta_{a}$.

Remark 2.1. Most of the results in Sections 2, 3 and 4 are well known in the much more general settings of stratified metrics, see [ACM14, ACM15], and Ricci limit spaces, see [Din02]. Our space $\mathbf{R}_{(\beta)}^{m}$ fits into both of these theories. Since proofs are elementary, we have decided to include them.
2.2. The Sobolev space $W^{1,2}$. The gradient of a function $u$ that is $C^{1}$ on the regular set is given by the following expression
$$\nabla u=\sum_{a}\left(\frac{\partial u}{\partial r_{a}} \partial_{r_{a}}+\frac{1}{\beta_{a} r_{a}} \frac{\partial u}{\partial \theta_{a}} \frac{1}{\beta_{a} r_{a}} \partial_{\theta_{a}}\right)+\sum_{i} \frac{\partial u}{\partial s_{i}} \partial_{s_{i}} .$$
For a domain $\Omega \subset \mathbf{R}_{(\beta)}^{m}$ we set $H^{1}(\Omega)$ to be the standard Sobolev space, given by the completion of Lipschitz functions under the norm
$$\|u\|_{W^{1,2}(\Omega)}^{2}=\|u\|_{L^{2}(\Omega)}^{2}+\|\nabla u\|_{L^{2}(\Omega)}^{2} .$$
For regular domains $\Omega$ (e.g. a ball) $H^{1}(\Omega)$ agrees with $W^{1,2}(\Omega)$, that is the subspace of functions in $L^{2}(\Omega)$ that have first order weak derivatives also in $L^{2}(\Omega)$. We will always work with regular domains and keep the notation $W^{1,2}$.

It is a standard fact that, on a space with co-dimension two singularities, smooth functions with compact support on the regular locus, $C_{\mathrm{c}}^{\infty}\left(\Omega^{\text {reg }}\right)$, are dense in $W^{1,2}(\Omega)$; see Mon17. In our case, this follows by taking products with the following cut-off functions:

Lemma 2.2. For any $\epsilon>0$ there is a Lipschitz function $\chi$ on $\mathbf{R}^{2}$ with the following properties:
\begin{itemize}
\item[-] $\chi=0$ in a neighborhood of 0;
\item[-] $\chi=1$ outside $B_{\epsilon}$;
\item[-] $\int_{\mathbf{R}^{2}}|\nabla \chi|^{2}<\epsilon$.
\end{itemize}
Proof. Let $(r, \theta)$ be polar coordinates in $\mathbf{R}^{2}$. For $\delta, Q>0$ we set
$$f_{\delta, Q}=\left\{\begin{array}{l}
0 \text { if } r \leq \delta \\
\log (r / \delta) \text { if } \delta \leq r \leq Q \delta \\
\log Q \text { if } r \geq Q \delta .
\end{array}\right.$$
Let $1-\chi=(\log Q)^{-1}\left(\log Q-f_{\delta, Q}\right)$, so
$$\begin{aligned}
\int_{\mathbf{R}^{2}}|\nabla \chi|^{2} & =(\log Q)^{-2} \int_{\delta}^{Q \delta} \frac{1}{r^{2}} r d r \\
& =(\log Q)^{-1}
\end{aligned}$$
We take $Q \gg 1$ such that $(\log Q)^{-1}<\epsilon$ and then we choose $\delta \ll 1$ such that $Q \delta<\epsilon$. \(\square\)
2.3. Weak solutions. Let $u \in W^{1,2}(\Omega)$ and $f \in L_{\text {loc }}^{1}(\Omega)$. We say that $-\Delta u=f$, if for every Lipschitz test function $\psi$ with compact support contained in $\Omega$, we have
$$\int_{\Omega}\langle\nabla u, \nabla \psi\rangle=\int_{\Omega} f \psi .$$
The space $W_{0}^{1,2}(\Omega) \subset W^{1,2}(\Omega)$ is the completion of compactly supported Lipschitz functions. By continuity, the identity (2.2) also holds for test functions $\psi \in W_{0}^{1,2}(\Omega)$.

It is straightforward to show existence of weak solutions, by using the variational method as follows: The Poincaré inequality asserts that, if $\Omega$ is bounded,
$$\int_{\Omega} u^{2} \leq C \int_{\Omega}|\nabla u|^{2}$$
for $u \in W_{0}^{1,2}(\Omega)$. As a consequence, given $f \in L^{2}$, the functional $\varphi \mapsto \int \varphi f$ is continuous with respect to the Dirichlet norm $\|\varphi\|_{D}^{2}=\int|\nabla \varphi|^{2}$. By Riesz, there is $u \in W_{0}^{1,2}$ such that $\langle\cdot, u\rangle_{D}=\int \cdot f$, which is to say that $u \in W_{0}^{1,2}$ is a weak solution of $-\Delta u=f$.

Lemma 2.3 (Caccioppoli inequality). Let $u \in W^{1,2}\left(B_{1}\right)$ solve $-\Delta u=f$ with $f \in L^{2}\left(B_{1}\right)$, then
$$\int_{B_{1 / 2}}|\nabla u|^{2} \leq \int_{B_{1}} f^{2}+C \int_{B_{1}} u^{2} .$$
Proof. Let $\eta$ be a compactly supported function in $B_{1}$, with $\eta=1$ on $B_{1 / 2}$. We set our test function to be $\psi=\eta^{2} u \in W_{0}^{1,2}\left(B_{1}\right)$, so
$$\begin{aligned}
\int_{B_{1}} \eta^{2}|\nabla u|^{2} & =\int_{B_{1}} \eta^{2} u f-2 \int_{B_{1}} \eta u\langle\nabla u, \nabla \eta\rangle \\
& \leq \frac{1}{2} \int_{B_{1}} \eta^{2} u^{2}+\frac{1}{2} \int_{B_{1}} \eta^{2} f^{2}+\frac{1}{2} \int_{B_{1}} \eta^{2}|\nabla u|^{2}+2 \int_{B_{1}} u^{2}|\nabla \eta|^{2} .
\end{aligned}$$
The statement follows with $C=\max \left(\eta^{2}+4|\nabla \eta|^{2}\right)$ \(\square\)

The Caccioppoli inequality, combined with Rellich's compactness theorem give us the following useful result.

Lemma 2.4 (Harmonic approximation). For every $\epsilon>0$ there is $\delta>0$ with the following property: If $u \in W^{1,2}\left(B_{1}\right)$ satisfies $\Delta u=f$ with $\|u\|_{L^{2}\left(B_{1}\right)} \leq 1$ and $\|f\|_{L^{2}\left(B_{1}\right)}<\delta$, then there is a weak harmonic function $h \in W^{1,2}\left(B_{1 / 2}\right)$ such that $\|u-h\|_{L^{2}\left(B_{1 / 2}\right)}<\epsilon$.

Proof. If not, we would have some $\epsilon_{0}>0$ and a sequence of functions $u_{i}$ with $\left\|u_{i}\right\|_{L^{2}\left(B_{1}\right)}=1,\left\|\Delta u_{i}\right\|_{L^{2}\left(B_{1}\right)} \rightarrow 0$ and $\left\|u_{i}-h\right\|_{L^{2}\left(B_{1 / 2}\right)} \geq \epsilon_{0}$ for every weak harmonic function $h$ on $B_{1 / 2}$. The Caccioppoli inequality implies that $\|u\|_{W^{1,2}\left(B_{1 / 2}\right)} \leq C$. The Rellich theorem asserts that the inclusion
$$W^{1,2}\left(B_{1 / 2}\right) \subset L^{2}\left(B_{1 / 2}\right)$$
is compact. Taking a subsequence, we have $u_{\infty} \in W^{1,2}\left(B_{1 / 2}\right)$ with $\lim _{i \rightarrow \infty} \| u_{i}-$ $u_{\infty} \|_{L^{2}\left(B_{1 / 2}\right)}=0$ and $u_{i}$ converges weakly in $W^{1,2}$ to $u_{\infty}$. For every test function $\psi$ we have
$$\int_{B_{1 / 2}}\left\langle\nabla u_{\infty}, \nabla \psi\right\rangle=\lim _{i \rightarrow \infty} \int_{B_{1 / 2}}\left\langle\nabla u_{i}, \nabla \psi\right\rangle=0,$$
so $u_{\infty}$ is weakly harmonic. Taking $h=u_{\infty}$ gives $\left\|u_{i}-u_{\infty}\right\|_{L^{2}\left(B_{1 / 2}\right)} \geq \epsilon_{0}$, a contradiction. \(\square\)
2.4. Interior $L^{2}$-bound on $\boldsymbol{\operatorname { H e s s }}(u)$. The Hessian of a function with respect to our singular metric, $\operatorname{Hess}(u)=\nabla_{g}^{2} u$, is uniformly equivalent, as a quadratic form, to the Euclidean Hessian. Same as before, we have the usual Sobolev space $W^{2,2}$, and it is irrelevant whether we use the Euclidean metric or $g$ to define its norm. However, one difference is that smooth, compactly supported functions on the regular locus are no longer dense in $W^{2,2}$. The next result relies on the fact that eigenfunctions of the Laplace operator are Lipschitz, see [Mon17] and [BKMR18, Proposition 5.4], which depends on our cone angles $\beta_{a}$ being < 1 for all $a$.
Proposition 2.5. Let $u \in W^{1,2}\left(B_{1}\right)$ with $-\Delta u=f$ and $f \in L^{2}\left(B_{1}\right)$. Then $u \in W^{2,2}\left(B_{1 / 2}\right)$ and
$$\|\operatorname{Hess}(u)\|_{L^{2}\left(B_{1 / 2}\right)} \leq C\left(\|f\|_{L^{2}\left(B_{1}\right)}+\|u\|_{L^{2}\left(B_{1}\right)}\right)$$
Proof. Let $\eta$ be a smooth cut-off function, with compact support in $B_{1}$ and identically equal to 1 on $B_{1 / 2}$. We can clearly arrange so that $\Delta \eta$ is also smooth. The function $\tilde{u}=\eta u \in W_{0}^{1,2}\left(B_{1}\right)$ satisfies $-\Delta \tilde{u}=\tilde{f}$ with $\tilde{f}=-(\Delta \eta) u-2\langle\nabla u, \nabla \eta\rangle+\eta f$. Applying the Caccioppoli inequality, we obtain
$$\|\tilde{f}\|_{L^{2}\left(B_{1}\right)} \leq C\left(\|f\|_{L^{2}\left(B_{1}\right)}+\|u\|_{L^{2}\left(B_{1}\right)}\right) .$$
We shall show that $\tilde{u} \in W^{2,2}\left(B_{1}\right) \cap W_{0}^{1,2}\left(B_{1}\right)$ and $\|\tilde{u}\|_{W^{2,2}\left(B_{1}\right)} \leq C\|\tilde{f}\|_{L^{2}\left(B_{1}\right)}$.
Because of the compact inclusion $W_{0}^{1,2} \subset L^{2}$, we have an orthonormal basis of $L^{2}$ by eigenfunctions; see the proof of Lemma 3.1. Therefore, we can write $\tilde{f}=\sum_{\lambda} f_{\lambda}$ with $f_{\lambda} \in W_{0}^{1,2}\left(B_{1}\right)$ and $-\Delta f_{\lambda}=\lambda f_{\lambda}$. The eigenvalues form a discrete sequence of non-negative numbers tending to infinity. Note that any weakly harmonic function in $W_{0}^{1,2}$ must vanish identically. In particular, the lowest eigenvalue must be strictly positive. Let $u_{\lambda}=\lambda^{-1} f_{\lambda}$, we will show that the series $\sum_{\lambda} u_{\lambda}$ converges in $W^{2,2}\left(B_{1}\right) \cap W_{0}^{1,2}\left(B_{1}\right)$.

By standard regularity theory, any eigenfunction $u_{\lambda}$ is smooth outside the conical set. Moreover, on $B^{\text {reg }}$ we have the identity
$$\frac{1}{2} \Delta\left|\nabla u_{\lambda}\right|^{2}=\left|\operatorname{Hess}\left(u_{\lambda}\right)\right|^{2}-\lambda\left|\nabla u_{\lambda}\right|^{2} .$$
Take a cut-off function $\chi_{\epsilon}$, vanishing in a small neighborhood of the conical set and equal to 1 outside the $\epsilon$-tubular neighborhood. Multiply by $\chi_{\epsilon}$ and integrate to get
$$\int_{B_{1}} \chi_{\epsilon}\left|\operatorname{Hess}\left(u_{\lambda}\right)\right|^{2}=\lambda \int_{B_{1}} \chi_{\epsilon}\left|\nabla u_{\lambda}\right|^{2}+\frac{1}{2} \int_{B_{1}}\left(\Delta \chi_{\epsilon}\right)|\nabla u|^{2} .$$
We let $\epsilon \rightarrow 0$ and take $\chi_{\epsilon}$ such that $\lim _{\epsilon \rightarrow 0} \int_{B_{1}}\left|\Delta \chi_{\epsilon}\right|=0$. Since $\left|\nabla u_{\lambda}\right| \in L^{\infty}$, we conclude that $u_{\lambda} \in W^{2,2}\left(B_{1}\right)$ and
$$\begin{aligned}
\int_{B_{1}}\left|\operatorname{Hess}\left(u_{\lambda}\right)\right|^{2} & =\lambda \int_{B_{1}}\left|\nabla u_{\lambda}\right|^{2} \\
& =\lambda^{2} \int_{B_{1}} u_{\lambda}^{2} \\
& =\int_{B_{1}} f_{\lambda}^{2} .
\end{aligned}$$

We can proceed the same way with finite linear combinations of eigenfunctions, to show that
$$\int_{B_{1}}\left|\operatorname{Hess}\left(\sum u_{\lambda}\right)\right|^{2}=\sum \int_{B_{1}} f_{\lambda}^{2}$$
and similarly, $\int_{B_{1}}\left(\sum u_{\lambda}\right)^{2}=\sum \lambda^{-2} \int_{B_{1}} f_{\lambda}^{2}$ and $\int_{B_{1}}\left|\nabla\left(\sum u_{\lambda}\right)\right|^{2}=\sum \lambda^{-1} \int_{B_{1}} f_{\lambda}^{2}$. Therefore, the series $\sum_{\lambda} u_{\lambda}$ converges to a function $u^{\prime} \in W^{2,2}\left(B_{1}\right) \cap W_{0}^{1,2}\left(B_{1}\right)$ that satisfies $-\Delta u^{\prime}=f$ and $\left\|u^{\prime}\right\|_{W^{2,2}\left(B_{1}\right)} \leq C\|\tilde{f}\|_{L^{2}\left(B_{1}\right)}$. By uniqueness, $u^{\prime}=\tilde{u}$ and we have shown the desired estimate. \(\square\)
2.5. Scaled $L^{2}$-norms. Given a geodesic ball $B(x, \rho) \subset \mathbf{R}_{(\beta)}^{m}$, we set
$$\|u\|_{B(x, \rho)}=\left(\rho^{-m} \int_{B(x, \rho)} u^{2}\right)^{1 / 2}$$
This norm has the nice property of being scale invariant. More precisely, our space $\mathbf{R}_{(\beta)}^{m}$ is a cone, as we will explain with more detail on Section 3.1, with dilations given by
$$\lambda\left(r_{a}, \theta_{a}, s_{i}\right)=\left(\lambda r_{a}, \theta_{a}, \lambda s_{i}\right) .$$
Dilations scale the distance by $d(\lambda x, \lambda y)=\lambda d(x, y)$, and $\lambda B(x, \rho)=B(\lambda x, \lambda \rho)$. Given a function $u: B(\lambda x, \lambda \rho) \rightarrow \mathbf{R}$, we can pull-it back via the dilation map $\lambda: B(x, \rho) \rightarrow B(\lambda x, \lambda \rho)$, to $u(\lambda \cdot): B(x, \rho) \rightarrow \mathbf{R}$. It is immediate to check that
$$\|u(\lambda \cdot)\|_{B(x, \rho)}=\|u\|_{B(\lambda x, \lambda \rho)} .$$
2.5.1. Scaled estimates. The Poincaré inequality, as well as the Caccioppoli inequality Lemma 2.3 and the interior $L^{2}$-bound on the Hessian in Proposition 2.5, hold with a uniform constant for all balls $B_{1}(p) \subset B_{2}(p)$ independent of the center. A scaling argument allows us to obtain the corresponding inequalities on balls of arbitrary radius. For example, the scale invariant version of estimate (2.3) is
$$\|\operatorname{Hess}(u)\|_{B(x, \rho)} \leq C\left(\|\Delta u\|_{B(x, 2 \rho)}+\rho^{-2}\|u\|_{B(x, 2 \rho)}\right)$$
2.5.2. Campanato spaces. The following characterization of the Hölder property, in terms of the decay of the $L^{2}$-norm, is attributed to Campanato; see HL11, Chapter 3.2]. We denote averages by
$$f_{B}=(\operatorname{Vol}(B))^{-1} \int_{B} f$$

Lemma 2.6. Let $\alpha>0$. Then there is a constant $\kappa=\kappa\left(\alpha, \beta_{a}, m\right)$ with the following property: If $f$ is in $L^{2}\left(B_{2}\right)$ and there is $K>0$ such that
$$\left\|f-f_{B_{\rho}(x)}\right\|_{B_{\rho}(x)} \leq K \rho^{\alpha}$$
for all $0<\rho<1$ and all $x \in B_{1}$. Then $f$ is continuous on $B_{1}$ and
$$|f(x)-f(y)| \leq \kappa K d(x, y)^{\alpha}$$
for every $x, y \in B_{1}$ with $d(x, y)<1 / 2$.
Proof. Let $x \in B_{1}$ and $0<r<1 / 2$.
$$\begin{aligned}
& =\frac{1}{\operatorname{Vol}\left(B_{2 r}(x)\right) \operatorname{Vol}\left(B_{r}(x)\right)}\left|\int_{B_{2 r}(x) \times B_{r}(x)}(f(u)-f(v)) d u d v\right| \\
& \leq \frac{1}{\operatorname{Vol}\left(B_{2 r}(x)\right)^{\frac{1}{2}} \operatorname{Vol}\left(B_{r}(x)\right)^{\frac{1}{2}}}\left(\int_{B_{2 r}(x) \times B_{r}(x)}(f(u)-f(v))^{2} d u d v\right)^{\frac{1}{2}} \\
& \leq \frac{\sqrt{2}}{\operatorname{Vol}\left(B_{r}(x)\right)^{\frac{1}{2}}}\left(\int_{B_{2 r}(x)}\left(f(u)-f_{B_{2 r}(x)}\right)^{2} d u d v\right)^{\frac{1}{2}} \\
& \leq Q\left(\beta_{a}, m\right)\left\|f-f_{B_{2 r}(x)}\right\|_{B_{2 r}(x)} \\
& \leq Q K(2 r)^{\alpha}
\end{aligned}$$

Given $0<\rho<1 / 2$, we apply the above to $r=2^{-k} \rho$ for $k=0,1,2, \ldots, \infty$ to estimate $\sum_{k=0}^{\infty}\left|f_{B_{2-k+1} \rho}-f_{B_{2-k} \rho}\right|$. We conclude that
$$\left|f_{B_{\rho}(x)}-f(x)\right| \leq \kappa_{1} K \rho^{\alpha},$$
with $\kappa_{1}=Q\left(\sum_{k=0}^{\infty} 2^{-\alpha k}\right)$.
Fix a pair of points $x, y \in B_{1}$ with $d=d(x, y)<1 / 2$. The same reasoning as before gives us
$$\begin{aligned}
& \left|f_{B_{d}(x)}-f_{B_{d}(y)}\right| \\
& =\frac{1}{\operatorname{Vol}\left(B_{d}(x)\right) \operatorname{Vol}\left(B_{d}(y)\right)}\left|\int_{B_{d}(x) \times B_{d}(y)}(f(u)-f(v)) d u d v\right| \\
& \leq \frac{1}{\operatorname{Vol}\left(B_{d}(x)\right)^{1 / 2} \operatorname{Vol}\left(B_{d}(y)\right)^{1 / 2}}\left(\int_{B_{2 d}(x) \times B_{2 d}(x)}(f(u)-f(v))^{2} d u d v\right)^{1 / 2} \\
& \leq \frac{\sqrt{2} \operatorname{Vol}\left(B_{2 d}(x)\right)^{1 / 2}}{\operatorname{Vol}\left(B_{d}(x)\right)^{1 / 2} \operatorname{Vol}\left(B_{d}(y)\right)^{1 / 2}}\left(\int_{B_{2 d}(x)}\left(f(u)-f_{B_{2 d}(x)}\right)^{2} d u\right)^{1 / 2} \\
& \leq Q^{\prime}\left(\beta_{a}, m\right)\left\|f-f_{B_{2 d}(x)}\right\|_{B_{2 d}(x)} \\
& \leq Q^{\prime} K(2 d)^{\alpha} .
\end{aligned}$$
We let $\kappa_{2}=Q^{\prime} 2^{\alpha}$, so that $\left|f_{B_{d}(x)}-f_{B_{d}(y)}\right| \leq \kappa_{2} K d^{\alpha}$. Finally,
$$\begin{aligned}
|f(x)-f(y)| & \leq\left|f(x)-f_{B_{d}(x)}\right|+\left|f_{B_{d}(x)}-f_{B_{d}(y)}\right|+\left|f_{B_{d}(y)}-f(y)\right| \\
& \leq\left(2 \kappa_{1}+\kappa_{2}\right) K d^{\alpha}
\end{aligned}$$
which proves the claim. \(\square\)

Lemma 2.7. Let $0<\lambda<1$ and let $f \in L^{2}(B(x, 1))$. If for all integers $k \geq 0$ there are $\tau_{k} \in \mathbf{R}$ such that
$$\left\|f-\left(\tau_{1}+\ldots+\tau_{k}\right)\right\|_{B\left(x, \lambda^{k}\right)} \leq C \lambda^{k \alpha} ;$$
then $\sum_{k}\left|\tau_{k}\right|<\infty$. Moreover, if we set $\tau=\sum_{k} \tau_{k}$, then we have
$$\|f-\tau\|_{B(x, r)} \leq C^{\prime} r^{\alpha}$$
for all $0<r<1$ and some $C^{\prime}=\kappa(\alpha, \lambda) C$.

The proof is elementary and we omit it. Under the hypothesis of Lemma 2.7. the Campanato condition holds. Because, for any $\tau \in \mathbf{R},\left\|f-f_{B}\right\|_{B} \leq\|f-\tau\|_{B}$.

\section*{3. Homogeneous harmonic functions on products of cones}
3.1. Products of cones. The point we want to emphasize is that our space
$$\mathbf{R}_{(\beta)}^{m}=C\left(S_{2 \pi \beta_{1}}^{1}\right) \times \ldots \times C\left(S_{2 \pi \beta_{n}}^{1}\right) \times \mathbf{R}^{m-2 n}$$
is itself a Riemannian cone. This follows from the general fact that the product $C\left(L_{1}\right) \times C\left(L_{2}\right)$ of two cones is a cone $C(L)$. Indeed, we write $g_{C_{1}}=d r_{1}^{2}+r_{1}^{2} g_{L_{1}}$ and $g_{C_{2}}=d r_{2}^{2}+r_{2}^{2} g_{L_{2}}$, so that $\left(L_{1}, g_{L_{1}}\right)$ and $\left(L_{2}, g_{L_{2}}\right)$ are the respective links; and let $g_{C}=g_{C_{1}}+g_{C_{2}}$. We introduce coordinates $(\rho, \psi) \in(0,+\infty) \times(0, \pi / 2)$ by setting $r_{1}=\rho \sin \psi$ and $r_{2}=\rho \cos \psi$; it is then easy to check that
$$g_{C}=d \rho^{2}+\rho^{2}\left(d \psi^{2}+\left(\sin ^{2} \psi\right) g_{L_{1}}+\left(\cos ^{2} \psi\right) g_{L_{2}}\right) .$$
We can rewrite this as $g_{C}=d \rho^{2}+\rho^{2} g_{L}$, where the link is $L=[0, \pi / 2] \times L_{1} \times$ $L_{2} /\left(\{0\} \times L_{1}\right) \sqcup\left(\{\pi / 2\} \times L_{2}\right)$ endowed with $g_{L}=d \psi^{2}+\left(\sin ^{2} \psi\right) g_{L_{1}}+\left(\cos ^{2} \psi\right) g_{L_{2}}$. At $\psi=0$, the $L_{1}$ factor in $L$ collapses, so that $L \cap\{\psi=0\}$ is a copy of $L_{2}$ and the metric $g_{L}$ has a singularity modeled on $C\left(L_{1}\right)$. Similarly, at $\psi=\pi / 2$ the metric $g_{L}$ has a singularity modeled on $C\left(L_{2}\right)$ along $L_{1}=L \cap\{\psi=\pi / 2\}$.

In our particular case, $g$ is a cone over a singular metric $\bar{g}$ on the $(m-1)$-sphere. We write
$$g=d \rho^{2}+\rho^{2} \bar{g},$$
with
$$\rho^{2}=\sum_{a} r_{a}^{2}+\sum_{i} s_{i}^{2} ;$$
and we identify
$$\mathbf{R}_{(\beta)}^{m}=C\left(S_{\bar{g}}^{m-1}\right) .$$
Our $\bar{g}$ is a singular metric on the $(m-1)$-sphere, with cone angles $2 \pi \beta_{a}$ along the copies of $S^{m-3} \subset S^{m-1}$ cut-out by $r_{a}=0$. On its regular part, $\bar{g}$ is locally isometric to the round sphere of curvature 1 . As model examples, in dimensions $m=3,4$, we have:
\begin{itemize}
\item[-] $C\left(S_{2 \pi \beta}^{1}\right) \times \mathbf{R}$, so
$$\bar{g}=d \psi^{2}+\beta^{2} \sin ^{2} \psi d \theta^{2}$$
-with $\psi \in(0, \pi)$ - is the 'rugby ball' metric on the two-sphere with two antipodal points of angle $2 \pi \beta$.
\item[-] $C\left(S_{2 \pi \beta_{1}}^{1}\right) \times C\left(S_{2 \pi \beta_{2}}^{1}\right)$, so
$$\bar{g}=d \psi^{2}+\beta_{1}^{2} \sin ^{2} \psi d \theta_{1}^{2}+\beta_{2}^{2} \cos ^{2} \psi d \theta_{2}^{2}$$
-with $\psi \in(0, \pi / 2)$ - is a constant curvature 1 metric on the three-sphere with cone angles $2 \pi \beta_{1}$ and $2 \pi \beta_{2}$ along two Hopf circles of lengths $2 \pi \beta_{2}$ and $2 \pi \beta_{1}$ respectively.
\end{itemize}

The dilations of $g$ are given, in spherical coordinates $(\rho, \Theta) \in(0,+\infty) \times S^{m-1}$, by $\lambda(\rho, \Theta)=(\lambda \rho, \Theta)$. In terms of the $\left(r_{a}, \theta_{a}, s_{i}\right)$ coordinates, we have
$$\lambda\left(r_{a}, \theta_{a}, s_{i}\right)=\left(\lambda r_{a}, \theta_{a}, \lambda s_{i}\right) .$$
3.2. Spectral theory. Let $\bar{g}$ be the singular metric on the sphere, as in equation (3.1), equivalently $\bar{g}$ is the restriction of $g$ to $S^{m-1}=\left\{\sum_{a} r_{a}^{2}+\sum_{i} s_{i}^{2}=1\right\} \subset \mathbf{R}_{(\beta)}^{m}$. Clearly, $\bar{g}$ is uniformly equivalent to the smooth round metric $\left.g_{\mathbf{R}^{m}}\right|_{S^{m-1}}$. Same as before, we have a standard Sobolev space $W^{1,2}\left(S^{m-1}\right)$

Lemma 3.1. There is an orthonormal basis $\left\{\phi_{i}\right\}$ of $L^{2}\left(S^{m-1}\right)$ given by eigenfunctions of $\Delta_{\bar{g}}$. More precisely, $\phi_{i} \in W^{1,2}\left(S^{m-1}\right)$ solve $-\Delta_{\bar{g}} \phi_{i}=\lambda_{i} \phi_{i}$ with $0=\lambda_{0}<\lambda_{1} \leq \lambda_{2} \leq \ldots$ and $\lambda_{i} \rightarrow \infty$.

Proof. Recall that $\|u\|_{W^{1,2}}=\int u^{2}+\int\left|\nabla_{\bar{g}} u\right|^{2}$. Given $f \in L^{2}$, it defines a bounded linear functional on $W^{1,2}$ by $T(\phi)=\int f \phi$. If $u$ is such that $T=\langle u,-\rangle_{W^{1,2}}$, then $u$ is a weak solution of $-\triangle_{\bar{g}} u+u=f$. The map $f \rightarrow u$ is a bounded linear map from $L^{2}$ to $W^{1,2}$, composing this map with the compact inclusion we have a map $K: L^{2} \rightarrow L^{2}$ which is compact and self-adjoint. It follows from the spectral theorem that we can find an orthonormal basis $\left\{\phi_{i}\right\}_{i \geq 0}$ of $L^{2}$ such that $K\left(\phi_{i}\right)=s_{i} \phi_{i}$ and $s_{i} \rightarrow 0$. Unwinding the definitions, we get that $\triangle_{\bar{g}} \phi_{i}=-\lambda_{i} \phi_{i}$ with $0=\lambda_{0} \leq \lambda_{1} \leq \lambda_{2} \leq \ldots$ and $\lambda_{i}=\left(1-s_{i}\right) / s_{i} \rightarrow \infty$. \(\square\)

The set of indicial roots is a discrete subset $\mathcal{I} \subset \mathbf{R}$ given by the numbers $d$, such that
$$\lambda=d(d+m-2)$$
is an eigenvalue of $-\Delta_{\bar{g}}$ as in Lemma 3.1. In particular, since $\lambda \geq 0$ we always have $\mathcal{I} \cap(2-m, 0)=\emptyset$. For each eigenvalue $\lambda$ we have two indicial roots associated to it, $d_{ \pm}$, with $d_{+} \geq 0$ and $d_{-} \leq 2-m$. If $\phi_{\lambda}$ is a corresponding eigenfunction, then $\rho^{d_{ \pm}} \phi_{\lambda}$ are homogeneous harmonic on $C\left(S_{\bar{g}}^{m-1}\right)$. We will be interested in harmonic functions bounded in a neighborhood of the vertex, so we will mainly consider non-negative indicial roots.

Let $B_{1} \subset C\left(S_{\bar{g}}^{m-1}\right)$ be the unit ball centered at the vertex of the cone. In polar coordinates $\left(r_{a}, \theta_{a}, s_{i}\right), B_{1}=\left\{\sum_{a} r_{a}^{2}+\sum_{i} s_{i}^{2}<1\right\}$. Let us denote by $S=\cup_{a}\left\{r_{a}=\right.$ $0\}$ the singular set of $g$.

Lemma 3.2 (Maximum principle). Let $u \in C^{2}\left(B_{1} \backslash S\right) \cap C^{0}\left(\bar{B}_{1}\right)$ satisfy $\Delta u=0$ on $B_{1} \backslash S$ and $u=0$ on $\partial B_{1}$, then $u=0$ on $B_{1}$.

Proof. We reproduce the barrier function argument from [GS16]. For $\epsilon>0$ we let
$$u_{\epsilon}=u+\epsilon\left(\sum_{a} \log r_{a}\right) .$$
Clearly, $\Delta u_{\epsilon}=0$ on $B_{1} \backslash S$ and $u_{\epsilon}(x) \rightarrow-\infty$ as $x \rightarrow S$. By the standard maximum principle, we have $\max _{\bar{B}_{1}} u_{\epsilon}=\max _{\partial B_{1}} u_{\epsilon}$. On the other hand, $u_{\epsilon} \leq u=0$ on $\partial B_{1}$. We conclude that for any $x \in B_{1} \backslash S$, we have $u(x)=\lim _{\epsilon \rightarrow 0} u_{\epsilon}(x) \leq 0$. Similarly, $(-u)(x) \leq 0$, so $u \equiv 0$. \(\square\)

Lemma 3.3. If $u \in W^{1,2}\left(B_{1}\right)$ is harmonic, we have
$$u=\sum_{d_{i} \geq 0} \rho^{d_{i}} \phi_{i} .$$
Proof. Expand $\left.u\right|_{S^{m-1}}$ into eigenfunctions,
$$\left.u\right|_{S^{m-1}}=\sum_{d_{i} \geq 0} \phi_{i} .$$

Then $u-\sum_{d_{i} \geq 0} \rho^{d_{i}} \phi_{i}$ is harmonic on $B_{1}$ and vanishes identically on $S^{m-1}$, by the maximum principle it must be identically zero. \(\square\)

Let $\mathcal{H}_{d}$ be the space of homogeneous harmonic functions of degree $d$, so this is the zero vector space if $d$ is not an indicial root. If $d \in \mathcal{I}$, then $\mathcal{H}_{d}$ is identified with the corresponding space of eigenfunctions. For $d \geq 0$, we write $\mathcal{H}_{\leq d}$ for the finite dimensional vector space spanned by homogeneous harmonic functions with degrees $\leq d$. Clearly, if $d^{\prime}>d$ then $\mathcal{H}_{d} \subset \mathcal{H}_{d^{\prime}}$. On the other hand, if there are no indicial roots in the range $\left(d, d^{\prime}\right]$, then $\mathcal{H}_{\leq d^{\prime}}=\mathcal{H}_{\leq d}$. So, if we look at $\mathcal{H}_{\leq d}$ as $d \geq 0$ increases we see the following. We start with the constants $\mathcal{H}_{\leq d}=\mathbf{R}$ for $0 \leq d<d_{1}$, where $d_{1}>0$ is the first positive indicial root. We have $\mathcal{H}_{\leq d}=\mathbf{R} \oplus \mathcal{H}_{d_{1}}$ for $d_{1} \leq d<d_{2}$; and so on. By orthogonality of the eigenfunctions, the spaces $\mathcal{H}_{d_{i}}$ and $\mathcal{H}_{d_{j}}$, with $i \neq j$, are orthogonal in $L^{2}\left(B_{1}\right)$.
3.3. Separation of variables. Consider the product of two cones, as in Section 3.1. Let $h=g_{L}$ be the metric on its link, given by
$$h=d \psi^{2}+\left(\sin ^{2} \psi\right) g_{L_{1}}+\left(\cos ^{2} \psi\right) g_{L_{2}} .$$
Recall that $\psi \in(0, \pi / 2)$ and the radial coordinates of the two factors are $r_{1}=$ $\rho \sin \psi, r_{2}=\rho \cos \psi$. We proceed to analyze the spectrum of $\Delta_{h}$ by separation of variables, we follow [ACM15, Section 3.6]. Write $n_{i}=\operatorname{dim} L_{i}$ and let $\phi_{\lambda_{1}}, \phi_{\lambda_{2}}$ be eigenfunctions on the corresponding links, that is $-\Delta_{g_{L_{i}}} \phi_{i}=\lambda_{i} \phi_{i}$. We have
$$-\Delta_{h}=\oplus_{\lambda_{1}, \lambda_{2}} L_{\lambda_{1}, \lambda_{2}},$$
where $L_{\lambda_{1}, \lambda_{2}}$ acts on functions $f(\psi) \phi_{\lambda_{1}} \phi_{\lambda_{2}}$ by
$$L_{\lambda_{1}, \lambda_{2}}=-\frac{\partial^{2}}{\partial \psi^{2}}-\left(n_{1}(\tan \psi)^{-1}-n_{2} \tan \psi\right) \frac{\partial}{\partial \psi}+\frac{\lambda_{1}}{\sin ^{2} \psi}+\frac{\lambda_{2}}{\cos ^{2} \psi} .$$
We are led to analyze the eigenfunctions of $L_{\lambda_{1}, \lambda_{2}}$, which can be done via the Sturm-Liouville theory for ODE's.

We consider the space of smooth compactly supported functions in $(0, \pi / 2)$, endowed with the measure $d \mu=\sin ^{n_{1}} \psi \cos ^{n_{2}} \psi d \psi$ and quadratic form
$$\langle f, f\rangle_{\lambda_{1}, \lambda_{2}}=\int_{0}^{\pi / 2}\left(\left|\frac{\partial f}{\partial \psi}\right|^{2}+f^{2} \frac{\lambda_{1}}{\sin ^{2} \psi}+f^{2} \frac{\lambda_{2}}{\cos ^{2} \psi}\right) d \mu .$$
Then $L_{\lambda_{1}, \lambda_{2}}$ is the associated self-adjoint operator with respect to the $L^{2}$-inner product, that is
$$\langle f, g\rangle_{\lambda_{1}, \lambda_{2}}=\int_{0}^{\pi / 2}\left(L_{\lambda_{1}, \lambda_{2}} f\right) g d \mu$$

We want $f(\psi) \phi_{\lambda_{1}} \phi_{\lambda_{2}} \in W^{1,2}((L, h))$. Since smooth functions with compact support on the regular part are dense in $W^{1,2}$, this means that we want $f$ to be in the closure of compactly supported functions on $(0, \pi / 2)$ with respect to $\langle\cdot, \cdot\rangle_{\lambda_{1}, \lambda_{2}}+\|\cdot\|_{L^{2}(d \mu)}^{2}$. By standard theory, $L_{\lambda_{1}, \lambda_{2}}$ has discrete spectrum; actually we already proved that $\Delta_{\bar{g}}$ has discrete spectrum. Each eigenvalue has exactly one (up to scalar factor) eigenfunction $f$, smooth on $(0, \pi / 2)$, and which satisfies $f(\psi) \phi_{\lambda_{1}} \phi_{\lambda_{2}} \in W^{1,2}((L, h))$. Indeed, changing variables to $x=\sin ^{2} \psi$, the ODE has regular singularities at the end-points $x=0$ and $x=1$; see equation (3.2). The eigenfunctions of $L_{0,0}$ are hypergeometric functions and our claim on multiplicity
one eigenvalues is easily verified. On the other hand, if $\lambda_{1}>0$, then the indicial root equation of $L_{\lambda_{1}, \lambda_{2}} f=\lambda f$ at $x=0$ is
$$r\left(r-1+\frac{1+n_{1}}{2}\right)=\frac{\lambda_{1}}{4} .$$
This has two solutions $r_{1}>0$ and $r_{2}<0$ which are the leading order terms in the Frobenius series solutions, only the one with $r_{1}>0$ extends continuously over $x=0$. The same discussion applies for $L_{0, \lambda_{2}}$ at $x=1$ and $\lambda_{2}>0$. The first eigenvalue of $L_{\lambda_{1}, \lambda_{2}}$ is clearly $\geq \lambda_{1}+\lambda_{2}$ and its associated eigenfunction is nowhere vanishing in $(0, \pi / 2)$. The second eigenfunction vanishes exactly once on $(0, \pi / 2)$, and so on. Note that, since $f(\psi) \phi_{\lambda_{1}} \phi_{\lambda_{2}}$ extends continuously to $L$, we have that $f(0)=0$ if $\lambda_{1} \neq 0$ and likewise $f(\pi / 2)=0$ if $\lambda_{2} \neq 0$; which matches with the Frobenius solution having a positive power leading term.
3.4. The operators $L_{\lambda_{1}, \lambda_{2}}$. Let $x=\sin ^{2} \psi$, so $x$ varies in the interval (0, 1) and
$$L_{\lambda_{1}, \lambda_{2}}=-4 x(1-x) \frac{\partial^{2}}{\partial x^{2}}+2\left(\left(2+n_{1}+n_{2}\right) x-1-n_{1}\right) \frac{\partial}{\partial x}+\frac{\lambda_{1}}{x}+\frac{\lambda_{2}}{1-x}$$

We look first at $L_{0,0}$. Its eigenfunctions correspond to homogeneous harmonic functions which only depend on the radial coordinates of the two factors. That is, $u=u\left(r_{1}, r_{2}\right)$ and
$$\left(\frac{\partial^{2}}{\partial r_{1}^{2}}+\frac{n_{1}}{r_{1}} \frac{\partial}{\partial r_{1}}+\frac{\partial^{2}}{\partial r_{2}^{2}}+\frac{n_{2}}{r_{2}} \frac{\partial}{\partial r_{2}}\right) u\left(r_{1}, r_{2}\right)=0 .$$
The first eigenvalue of $L_{0,0}$ is 0, with constant eigenfunctions. To find the second eigenvalue we note the following:
$$\Delta_{C(L)} r_{a}^{2}=2\left(n_{a}+1\right), \quad a=1,2 .$$
Therefore, the function $u=\left(n_{1}+1\right)^{-1} r_{1}^{2}-\left(n_{2}+1\right)^{-1} r_{2}^{2}$ is a degree 2 homogeneous harmonic function on $C(L)$. We write $u=\rho^{2} f(\psi)$ with
$$\begin{aligned}
f(\psi) & =\left(n_{1}+1\right)^{-1} \sin ^{2} \psi-\left(n_{2}+1\right)^{-1} \cos ^{2} \psi \\
& =\left(\frac{1}{n_{1}+1}+\frac{1}{n_{2}+1}\right) x-\frac{1}{n_{2}+1} .
\end{aligned}$$
It is easy to check that $L_{0,0} f=-\lambda f$ with $\lambda=2\left(n_{1}+n_{2}+2\right)$. This matches with the formula $\lambda=d(d-2+m)$ with $m=\operatorname{dim} C(L)=n_{1}+n_{2}+2$ and $d=2$. Moreover, $f(x)$ vanishes exactly once for $x \in(0,1)$, which means that $\lambda=2 m$ is the next eigenvalue after $\lambda=0$. To find the next, we note that
$$\Delta_{C(L)} r_{a}^{4}=4\left(3+n_{a}\right) r_{a}^{2}, \quad \Delta_{C(L)}\left(r_{1}^{2} r_{2}^{2}\right)=2\left(n_{1}+1\right) r_{2}^{2}+2\left(n_{2}+1\right) r_{1}^{2} .$$
Therefore,
$$\begin{aligned}
u & =\frac{1+n_{2}}{3+n_{1}} r_{1}^{4}+\frac{1+n_{1}}{3+n_{2}} r_{2}^{4}-2 r_{1}^{2} r_{2}^{2} \\
& =\rho^{4}\left(\frac{1+n_{2}}{3+n_{1}} \sin ^{4} \psi+\frac{1+n_{1}}{3+n_{2}} \cos ^{4} \psi-2 \sin ^{2} \psi \cos ^{2} \psi\right)
\end{aligned}$$
is homogeneous harmonic of degree 4. This implies that
$$f=\frac{1+n_{2}}{3+n_{1}} x^{2}+\frac{1+n_{1}}{3+n_{2}}(1-x)^{2}-2 x(1-x)$$
satisfies $L_{0,0} f=\lambda f$, with $\lambda=4\left(4+n_{1}+n_{2}\right)$. Finally, we note that $f(x)$ vanishes exactly twice for $x \in(0,1)$. To sum up, the first three eigenvalues of $L_{0,0}$ give rise to homogeneous harmonic functions of degrees 0, 2 and 4.

We look now at $L_{\lambda_{1}, 0}$ for a non-zero eigenvalue of $\Delta_{L_{1}}$. Let $\phi_{1}$ be an eigenfunction, $-\Delta_{L_{1}} \phi_{1}=\lambda_{1} \phi_{1}$. Let $\gamma_{1}>0$ be given by $\gamma_{1}\left(\gamma_{1}+n_{1}-1\right)=\lambda_{1}$, so
$$\begin{aligned}
u & =r_{1}^{\gamma_{1}} \phi_{1} \\
& =\rho^{\gamma_{1}}(\sin \psi)^{\gamma_{1}} \phi_{\lambda_{1}}
\end{aligned}$$
is a homogeneous harmonic function on $C(L)$. Therefore, $f(x)=x^{\gamma_{1} / 2}$ satisfies $L_{\lambda_{1}, 0} f=\lambda f$ with $\lambda=\gamma_{1}\left(\gamma_{1}+m-2\right)$. Since $f(x)$ in non-vanishing on ( 0,1 ), it is the first eigenfunction. To find the next, we note the following:
$$\Delta_{C(L)}\left(r_{1}^{\gamma_{1}} r_{2}^{2} \phi_{\lambda_{1}}\right)=2\left(n_{2}+1\right) r_{1}^{\gamma_{1}} \phi_{\lambda_{1}}, \quad \Delta_{C(L)}\left(r_{1}^{\gamma_{1}+2} \phi_{\lambda_{1}}\right)=2\left(2 \gamma_{1}+1+n_{1}\right) r_{1}^{\gamma_{1}} \phi_{\lambda_{1}} .$$
Therefore,
$$\begin{aligned}
u & =\left(\left(n_{2}+1\right)^{-1} r_{1}^{\gamma_{1}} r_{2}^{2}-\left(2 \gamma_{1}+1+n_{1}\right)^{-1} r_{1}^{\gamma_{1}+2}\right) \phi_{\lambda_{1}} \\
& =\rho^{\gamma_{1}+2}\left(\left(n_{2}+1\right)^{-1} \sin ^{\gamma_{1}} \psi \cos ^{2} \psi-\left(2 \gamma_{1}+1+n_{1}\right)^{-1} \sin ^{\gamma_{1}+2} \psi\right) \phi_{\lambda_{1}}
\end{aligned}$$
is homogeneous harmonic on $C(L)$. We conclude that
$$f(x)=x^{\gamma_{1} / 2}\left(\frac{1}{n_{2}+1}-\left(\frac{1}{n_{2}+1}+\frac{1}{2 \gamma_{1}+1+n_{1}}\right) x\right)$$
satisfies $L_{\lambda_{1}, 0} f=\lambda f$ with $\lambda=\left(\gamma_{1}+2\right)\left(\gamma_{1}+m\right)$. Since $f(x)$ vanishes only once in (0, 1), it is the second eigenfunction. To sum up, the first two eigenvalues of $L_{\lambda_{1}, 0}$ correspond to homogeneous harmonic functions on $C(L)$ of degrees $\gamma_{1}$ and $\gamma_{1}+2$. Clearly, the same discussion applies to $L_{0, \lambda_{2}}$.

Finally, we consider $L_{\lambda_{1}, \lambda_{2}}$ where $\lambda_{a}$ are non-zero eigenvalues. Let $\phi_{a}$ be corresponding eigenfunctions, so $-\Delta_{L_{a}}=\lambda_{a} \phi_{a}$. We get that
$$\begin{aligned}
u & =r_{1}^{\gamma_{1}} r_{2}^{\gamma_{2}} \phi_{\lambda_{1}} \phi_{\lambda_{2}} \\
& =\rho^{\gamma_{1}+\gamma_{2}}\left(\sin ^{\gamma_{1}} \psi \cos ^{\gamma_{2}} \psi\right) \phi_{\lambda_{1}} \phi_{\lambda_{2}}
\end{aligned}$$
is homogeneous harmonic on $C(L)$. Hence
$$f(x)=x^{\gamma_{1} / 2}(1-x)^{\gamma_{2} / 2}$$
satisfies $L_{\lambda_{1}, \lambda_{2}} f=\lambda f$ with $\lambda=\left(\gamma_{1}+\gamma_{2}\right)\left(\gamma_{1}+\gamma_{2}-2+m\right)$. Since $f$ is non-vanishing on (0, 1), this is the first eigenfunction. We conclude that all homogeneous harmonic functions associated to eigenvalues of $L_{\lambda_{1}, \lambda_{2}}$ have degree at least $\gamma_{1}+\gamma_{2}$.
3.5. Sub-quadratic harmonic functions. We identify the space of subquadratic harmonic 'polynomials' $\mathcal{H}_{\leq 2}$, as defined in Section 3.2. for our space $\mathbf{R}_{(\beta)}^{m}=$ $C\left(S_{\bar{g}}^{m-1}\right)$.

Proposition 3.4. $\mathcal{H}_{\leq 2}$ is spanned by
\begin{itemize}
\item[(1)] $1, s_{i}$;
\item[(2)] $r_{a}^{1 / \beta_{a}} \cos \left(\theta_{a}\right), r_{a}^{1 / \beta_{a}} \sin \left(\theta_{a}\right)$ for those $\beta_{a} \geq 1 / 2$;
\item[(3)] $\mathcal{H}_{2}\left(\mathbf{R}^{m-2 n}\right), r_{a}^{2}-r_{b}^{2}$ and $r_{a}^{2}-2 s_{i}^{2}$.
\end{itemize}

Moreover, $\mathcal{H}_{\leq 2+\alpha}=\mathcal{H}_{\leq 2}$ provided that $0<\alpha<\mu$.

Proof. We assume $m \geq 4$, for the special case $m=3$ see Section 3.5.1 below. We proceed by induction on the number of cone factors, so consider first $C\left(S_{2 \pi \beta}^{1}\right) \times$ $\mathbf{R}^{m-2}$. We apply the analysis in Sections 3.3 and 3.4 to $L_{1}=S_{2 \pi \beta}^{1}$ and $L_{2}=$ $S^{m-3}(1)$. The operator $L_{0,0}$ gives rise to constants, $(1 / 2) r^{2}-(m-3)^{-1}|s|^{2}$ and then homogeneous harmonic functions of degree 4 are higher.

We proceed to analyze $L_{\lambda_{1}, 0}$. The first non-zero eigenvalue of $S_{2 \pi \beta}^{1}$ is $\lambda_{1}=1 / \beta^{2}$ with eigenfunctions $\cos \theta$ and $\sin \theta$. The corresponding homogeneous harmonic functions $r^{1 / \beta} \cos \theta, r^{1 / \beta} \sin \theta$ have degree $1 / \beta$. If $1 / 2 \leq \beta<1$, then these functions are subquadratic, otherwise, for $0<\beta<1 / 2$, they have degree > 2. The other eigenvalues of $L_{\lambda_{1}, 0}$ give rise to homogeneous harmonic functions of degree $2+(1 / \beta)$ and higher. The other eigenvalues on $S_{2 \pi \beta}^{1}$ are $k^{2} / \beta^{2}$ with $k \geq 2$ and give rise to homogeneous harmonic functions of degrees $2 / \beta>2$ and higher. We consider $L_{0, \lambda_{2}}$. The first non-zero eigenvalue of $S^{m-3}(1)$ is $\lambda_{2}=m-3$. The corresponding homogeneous harmonic functions $s_{i}$, have degree 1. The other eigenvalues of $L_{0, \lambda_{2}}$ give rise to homogeneous harmonic functions of degree 3 and higher. The next eigenvalue on $S^{m-3}(1)$ is $2(m-2)$, the corresponding homogeneous harmonic functions are $\mathcal{H}_{2}\left(\mathbf{R}^{m-2}\right)$. The other homogeneous harmonic functions coming from $L_{0,2(m-2)}$ have degree 4 and higher. Finally, the lowest eigenvalue of $L_{\lambda_{1}, \lambda_{2}}$ gives rise to the homogeneous harmonic functions $s_{i} r^{1 / \beta} \cos \theta$ and $s_{i} r^{1 / \beta} \cos \theta$, which have degree $1+1 / \beta$. As a result, we see that the next indicial root after 2 is the minimum of 3, 1/ β (if $\beta<1 / 2$ ), 1+1/ $\beta$ (if $\beta>1 / 2$ ). In particular, by our choice of $\alpha$, there are no indicial roots in $(2,2+\alpha]$ and the statement $\mathcal{H}_{\leq 2}=\mathcal{H}_{\leq 2+\alpha}$ follows.

More generally, we repeat the above argument with $\mathbf{R}^{m-2}$ replaced by $C\left(L_{2}\right)$ with $\mathcal{H}_{\leq 2}\left(C\left(L_{2}\right)\right)$ given as in the statement of the proposition. The first non-zero eigenvalue of $L_{2}$ gives rise, through $L_{0, \lambda_{2}}$, to homogeneous harmonic functions of degree 1,3 , and higher if there is at least one Euclidean factor on $C\left(L_{2}\right)$; or degree $1 / \beta_{a}, 1 / \beta_{a}+2$, and higher if $C\left(L_{2}\right)$ does not split off any Euclidean factor. The second non-zero eigenvalue of $L_{2}$ gives rise to the degree 2 functions $\mathcal{H}_{2}\left(\mathbf{R}^{m-2 n}\right)$, degree 4 and higher. If $m=2 n$, then the second non-zero eigenvalue of $L_{2}$ gives rise to homogeneous harmonic functions of degree $2 / \beta_{a}>2$ and higher. Similarly, the homogeneous harmonic functions coming from eigenvalues of $L_{\lambda_{1}, \lambda_{2}}$ have degree at least $1 / \beta_{1}+1$ if $m>2 n$, and $1 / \beta_{1}+1 / \beta_{a}$ for some $a \geq 2$ if $m=2 n$. As before, we see that the next indicial root after 2 is the minimum of $3,1 / \beta_{a}$ for those $\beta_{a}<1 / 2$, $1+1 / \beta_{a}$ for those $\beta_{a}>1 / 2$. In particular, by our choice of $\alpha$, there are no indicial roots in $(2,2+\alpha]$ and the statement of Proposition 3.4 follows. \(\square\)

Corollary 3.5. For every $D \in \mathcal{D}_{2}$ and every $P \in \mathcal{H}_{\leq 2}$ we have $D P \equiv \tau \in \mathbf{R}$. Moreover,
$$|\tau| \leq C\|P\|_{L^{2}\left(B_{1}\right)}$$
for some $C=C\left(m, \beta_{a}\right)$.
Proof. Given the explicit description of $\mathcal{H}_{\leq 2}$ in Proposition 3.4, the fact that $D P$ is constant follows by immediate check inspection. The estimate (3.3) follows from the general principle that any two norms on a finite dimensional vector space are equivalent. \(\square\)
3.5.1. Special case: $m=3$. We present an alternative proof to Proposition 3.4 for the case of $C\left(S_{2 \pi \beta}^{1}\right) \times \mathbf{R}$. In cylindrical coordinates $(r, \theta, s)$, the metric is $g=$
$d r^{2}+\beta^{2} r^{2} d \theta^{2}+d s^{2}$. In spherical coordinates, we introduce the angular variable $t \in(0, \pi)$ and write $r=\rho \sin t, s=\rho \cos t$. We have
$$\begin{aligned}
g & =d \rho^{2}+\rho^{2}\left(d t^{2}+\beta^{2} \sin ^{2} t d \theta^{2}\right) \\
& =d \rho^{2}+\rho^{2} \bar{g}
\end{aligned}$$
Here, $\bar{g}=d t^{2}+\beta^{2} \sin ^{2} t d \theta^{2}$ is the spherical 'rugby ball' metric on $S^{2}$. Let $d \geq 0$ and let $u=\rho^{d} \varphi$ be a homogeneous harmonic function, so $\varphi=\varphi(t, \theta) \in W^{1,2}\left(S^{2}\right)$ solves $-\Delta_{\bar{g}} \varphi=\lambda \varphi$.

The function $u$ is smooth away from $r=0$ and $\Delta(\partial u / \partial s)=0$. On the other hand,
$$\frac{\partial}{\partial s}=\cos t \frac{\partial}{\partial \rho}-\frac{\sin t}{\rho} \frac{\partial}{\partial t} .$$
Therefore, $\partial u / \partial s=\rho^{d-1} \psi$ where $\psi$ is a smooth function on $S^{2}$ away from the two conical points and satisfies $-\Delta_{\bar{g}} \psi=\tilde{\lambda} \psi$ point-wise on the regular part. It is given by
$$\psi=-(\sin t) \frac{\partial \varphi}{\partial t}+d(\cos t) \varphi .$$

We claim that $\psi$ extends as a Hölder continuous function over $t=0$. Indeed, by De Giorgi-Nash-Moser we know that $\varphi$ is $C^{\alpha}$ at $t=0$. Applying the standard Schauder estimates in small balls away from the conical point we get that $|\partial \varphi / \partial t|=$ $O\left(t^{\alpha-1}\right)$. Therefore, $\sin t(\partial \varphi / \partial t)$ extends by 0 over $t=0$ as a $C^{\alpha}$ function. Since $\psi$ is $C^{\alpha}$ and satisfies $-\Delta_{\bar{g}} \psi=\lambda \psi$ away from the conical point, the standard Schauder theory implies that $\left|\nabla_{\bar{g}} \psi\right|=O\left(t^{\alpha-1}\right)$, so $\psi \in W^{1,2}$ and it solves the eigenvalue equation in the weak sense.

We can repeat the argument for higher order tangential derivatives. The conclusion is that, if $\partial^{k} u / \partial s^{k} \neq 0$ then $d-k$ is an indicial root. If $d>0$ is not an integer we let $k$ be the smallest integer such that $d-k<0$, so $-1<d-k<0$. Since there are no indicial roots in the interval $(-1,0)=(2-m, 0)$, we conclude that $\partial^{k} u / \partial s^{k} \equiv 0$ and $u=u_{0}(r, \theta) p(s)$ for some polynomial $p(s)$ of degree $<d$. We see that, if $d<2$ then $p(s)$ must be affine and $\Delta_{\beta} u_{0}=0$. The possibilities are $u=$ constant, or, if $\beta>1 / 2$, a linear combination of $r^{1 / \beta} \cos \theta, r^{1 / \beta} \sin \theta$.

If $d=2$, then $\partial^{2} u / \partial s^{2}$ is homogeneous harmonic of degree zero, hence a constant. After subtracting a multiple of $r^{2}-2 s^{2}$, we can assume $\partial^{2} u / \partial s^{2}=0$, so $p(s)$ must be affine and $\Delta_{\beta} u_{0}=0$. The cone $C\left(S_{2 \pi \beta}^{1}\right)$ does not have non-zero homogeneous harmonic functions of either degree 1 (because $\beta<1$ ) or 2 (because $\beta \neq 1 / 2$ ). The statement of Proposition 3.4 for the case $C\left(S_{2 \pi \beta}^{1}\right) \times \mathbf{R}$ then follows.

\section*{4. Elementary quantitative considerations}
4.1. Geodesics balls. Let $\mathcal{C}$ be the finite collection of at most $2^{n}$ cones $C(Y)$, given by $\mathbf{R}^{m}, C\left(S_{2 \pi \beta_{i}}^{1}\right) \times \mathbf{R}^{m-2}$ and more generally
$$C\left(S_{2 \pi \beta_{i_{1}}}^{1}\right) \times \ldots \times C\left(S_{2 \pi \beta_{i_{\ell}}}^{1}\right) \times \mathbf{R}^{m-2 \ell}$$
with $\ell \leq n$ and $1 \leq i_{1}<\ldots<i_{\ell} \leq n$. Here, $Y$ denotes the $(m-1)$-sphere endowed with a possibly singular metric as the ones described in Section 3.1. Equivalently, $\mathcal{C}$ consists of all $\mathbf{R}_{\left(\beta^{\prime}\right)}^{m}$ where ( $\beta^{\prime}$ ) is a subset of $(\beta)=\left(\beta_{1}, \ldots, \beta_{n}\right)$.

Given $\epsilon>0$, we say that $B(x, \rho) \subset \mathbf{R}_{(\beta)}^{m}$ is $\epsilon$-close to a ball $B_{C(Y)}(0, \rho) \subset C(Y)$ for a cone $C(Y) \in \mathcal{C}$, if after introducing cuts in some cone factors (see Appendix
A.1) $B(x, \rho)$ is isometric to a ball $B_{C(Y)}(z, \rho) \subset C(Y)$ with $|z|=d_{C(Y)}(z, o)<\epsilon \rho$. Equivalently, $\rho^{-1} B(x, \rho)$ is isometric to $B_{C(Y)}(z, 1)$ with $|z|<\epsilon$.

For $x \in \mathbf{R}_{(\beta)}^{m}$, consider the sequence of geodesic balls $B\left(x, \lambda^{k}\right)$ for $k \in \mathbb{Z}$ and constant $0<\lambda<1$. If $B\left(x, \lambda^{k}\right)$ is $\epsilon$-close to $B_{C(Y)}\left(0, \lambda^{k}\right)$ for some $C(Y) \in \mathcal{C}$ (equivalently, $\lambda^{-k} B\left(x, \lambda^{k}\right)$ is $\epsilon$-close to $B_{C(Y)}(0,1)$ ), we say $\lambda^{k}$ is a good scale for $x$. If not, then we call $\lambda^{k}$ a bad scale.

If $\lambda^{k}$ is a good scale for $x$, and so the rescaled ball, $\lambda^{-k} B\left(x, \lambda^{k}\right)=B\left(x_{k}, 1\right)$ for $x_{k}=\lambda^{-k} x$, is isometric to $B_{C(Y)}(z, 1) \subset C(Y)$ with $|z|<\epsilon$, we sometimes identify $B\left(x_{k}, 1\right)$ with its image $B_{C(Y)}(z, 1)$ and write $B\left(x_{k}, 1\right) \subset C(Y)$ with $\left|x_{k}\right|<\epsilon$.
Lemma 4.1 (Finitely many bad scales). Fix $0<\lambda<1$ and $\epsilon_{0}>0$. Then there is $N=N\left(\epsilon_{0}, \lambda\right)$ such that for each $x \in \mathbf{R}_{(\beta)}^{m}$, and every integer $k$ except for at most $N$ bad scales, the geodesic ball $B\left(x, \lambda^{k}\right)$ is $\epsilon_{0}$-close to a ball $B_{C(Y)}\left(0, \lambda^{k}\right) \subset C(Y)$ for some $C(Y) \in \mathcal{C}$.

Proof. We fix some $c=c(\beta)>1$ such that the following holds. Any unit geodesic ball in $C\left(S_{2 \pi \beta}^{1}\right)$ whose center is at distance $>c$ from the vertex, is isometric -after a cut- to the unit Euclidean ball in $\mathbf{R}^{2}$.

Without loss of generality, we can assume that $r_{1}(x) \leq r_{2}(x) \leq \ldots \leq r_{n}(x)$ and $s=0$; we will write $r_{a}=r_{a}(x)$. We rescale $B\left(x, \lambda^{k}\right)$ to unit size, so we end up with $B\left(x_{k}, 1\right)$ where $x_{k}=\lambda^{-k} x$. The coordinates of $x_{k}$ are $r_{a}\left(x_{k}\right)=\lambda^{-k} r_{a}$. If $r_{1}\left(x_{k}\right)=\lambda^{-k} r_{1}>c$, that is
$$\left(\log \lambda^{-1}\right) k>\log r_{1}^{-1}+\log c,$$
then $B(x, 1)$ is $\epsilon_{0}$-close (indeed isometric) to the unit ball in $\mathbf{R}^{m}$. If $\lambda^{-k} r_{2}>c$ and $\lambda^{-k} r_{1}<\epsilon_{0}$, that is
$$\log c+\log r_{2}^{-1}<\left(\log \lambda^{-1}\right) k<\log r_{1}^{-1}-\log \epsilon_{0}^{-1},$$
then $B\left(x_{k}, 1\right)$ is $\epsilon_{0}$-close to the unit ball in $C\left(S_{2 \pi \beta_{1}}^{1}\right) \times \mathbf{R}^{m-2}$. If $\lambda^{-k} r_{3}>c$ and $\lambda^{-k} r_{2}<\epsilon_{0}$, that is
$$\log c+\log r_{3}^{-1}<\left(\log \lambda^{-1}\right) k<\log r_{2}^{-1}-\log \epsilon_{0}^{-1},$$
then $B\left(x_{k}, 1\right)$ is $\sqrt{2} \epsilon_{0}$-close to the unit ball in $C\left(S_{2 \pi \beta_{1}}^{1}\right) \times C\left(S_{2 \pi \beta_{2}}^{1}\right) \times \mathbf{R}^{m-4}$. We proceed likewise; if $\lambda^{-k} r_{n}<\epsilon_{0}$, so
$$\left(\log \lambda^{-1}\right) k<\log r_{n}^{-1}-\log \epsilon_{0}^{-1}$$
then $B\left(x_{k}, 1\right)$ is $\sqrt{d} \epsilon_{0}$-close to the unit ball in $C\left(S_{2 \pi \beta_{1}}^{1}\right) \times \ldots \times C\left(S_{2 \pi \beta_{n}}^{1}\right) \times \mathbf{R}^{m-2 n}$.
We conclude that the set of $k \in \mathbf{Z}$ for which $B\left(x, \lambda^{k}\right)$ is not $\sqrt{n} \epsilon_{0}$-close to a ball in some cone $C(Y) \in \mathcal{C}$, is contained in a union of at most $n$ intervals of length $\left(\log \lambda^{-1}\right)^{-1}\left(\log \epsilon_{0}^{-1}+\log c\right)$. In particular, the lemma follows with
$$N=n\left(\log \lambda^{-1}\right)^{-1}\left(\log \epsilon_{0}^{-1}+\log c+(1 / 2) \log n\right) .$$ \(\square\)
4.2. Monotonicity of scaled $L^{2}$-norms. Recall that $B_{\rho} \subset C\left(S_{\bar{g}}^{m-1}\right)$ is the ball centered at zero of radius $\rho$.
Lemma 4.2. Let $d \geq 0$ and assume that $u \in W^{1,2}\left(B_{1}\right)$ is harmonic and $L^{2}$ -orthogonal to $\mathcal{H}_{\leq d}$, which means $u=\sum_{d_{i}>d} \rho^{d_{i}} \phi_{i}$. Let $d_{*}=\min \left\{d_{i}>d\right\}$. Then, for any $0<\rho<1$, we have
$$\|u\|_{B_{\rho}} \leq \rho^{d_{*}}\|u\|_{B_{1}},$$
with equality if and only if $u$ is homogeneous of degree $d_{*}$.
Proof. By the orthogonality of eigenfunctions, we have
$$\begin{aligned}
\int_{B_{\rho}} u^{2} & =\sum_{i, j} \int_{B_{\rho}} r^{d_{i}} r^{d_{j}} \phi_{i} \phi_{j} \\
& =\sum_{i} \frac{1}{2 d_{i}+m} \rho^{2 d_{i}+m} \int_{S^{m-1}} \phi_{i}^{2} .
\end{aligned}$$
From here,
$$\begin{aligned}
\|u\|_{B_{\rho}}^{2} & =\rho^{2 d_{*}} \sum_{i} \frac{1}{2 d_{i}+m} \rho^{2 d_{i}-2 d_{*}} \int_{S^{m-1}} \phi_{i}^{2} \\
& \leq \rho^{2 d_{*}}\|u\|_{B_{1}}^{2} .
\end{aligned}$$
with equality if and only if $u$ is homogeneous of degree $d_{*}$. \(\square\)

Next, we provide a version of the above lemma, considering balls which are not necessarily centered at the vertex. In particular, this establishes the quantitative decay property for harmonic functions orthogonal to $\mathcal{H}_{\leq 2}$ for any good scale $B\left(x, \lambda^{k}\right)$.

Recall that, for $x \in C(Y)$, we use $|x|$ to denote the distance to the vertex and $\mathcal{C}$ denotes the finite collection of model cones defined in Section 4.1.

Lemma 4.3. Let $0<\alpha<\mu$ and let $0<\lambda<1$. There is $\epsilon_{0}=\epsilon_{0}(\alpha, \lambda)$ with the following property. If $x \in C(Y)$ for some $C(Y) \in \mathcal{C}$ and $|x|<\epsilon_{0}$, then for every harmonic function $u$ in $B(x, 1)$ which is $L^{2}$-orthogonal to $\mathcal{H}_{\leq 2}(C(Y))$ we have
$$\|u\|_{B(x, \lambda)}<\lambda^{2+\alpha}\|u\|_{B(x, 1)} .$$
Proof. Let $x \in C(Y)$ have $|x|<\epsilon$. Since $B(x, \lambda) \subset B(0, \lambda+\epsilon)$, we clearly have
$$\|u\|_{B(x, \lambda)}^{2} \leq(1+\epsilon / \lambda)^{m}\|u\|_{B(0, \lambda+\epsilon)}^{2} .$$
Since $u$ is $L^{2}$-orthogonal to $\mathcal{H}_{\leq 2}$, we have
$$\|u\|_{B\left(0, \rho_{1}\right)}^{2} \leq\left(\rho_{1} / \rho_{2}\right)^{2 d_{*}}\|u\|_{B\left(0, \rho_{2}\right)}^{2},$$
where $0<\rho_{1}<\rho_{2}$ and $d_{*}$ is the smallest indicial root bigger than 2. We take $\rho_{1}=\lambda+\epsilon$ and $\rho_{2}=1-\epsilon$. Equations (4.1) and (4.2), together with $\|u\|_{B(0,1-\epsilon)} \leq$ $(1-\epsilon)^{-m}\|u\|_{B(1, x)}$, give us
$$\|u\|_{B(x, \lambda)} \leq \lambda^{2+\alpha} F(\epsilon)\|u\|_{B(x, 1)}$$
with
$$F(\epsilon)=\lambda^{d_{*}-2-\alpha}(1+\epsilon / \lambda)^{m+d_{*}}(1-\epsilon)^{-m-d_{*}} .$$
Note that $2+\alpha<d_{*}$, by our choice of $\alpha$. Since $F$ is continuous with respect to $\epsilon<1$ and $F(0)=\lambda^{d_{*}-2-\alpha}<1$, it suffices to take $\epsilon_{0}$ such that $F(\epsilon)<1$ for all $\epsilon<\epsilon_{0}$. \(\square\)

\section*{5. Proof of Theorem 1.1}

As before, $\mathcal{C}$ denotes the finite collection of model cones defined in Section 4.1 and, for $x \in C(Y)$, we use $|x|$ to denote the distance to the vertex.

Proposition 5.1 (Key step). Let $0<\alpha<\mu$. There are $0<\lambda<1, \delta>0$ and $\epsilon_{0}>0$ with the following property. If $x \in C(Y)$ for some $C(Y) \in \mathcal{C},|x|<\epsilon_{0}$ and $\Delta u=f$ with $\|f\|_{B_{1}(x)}<\delta,\|u\|_{B_{1}(x)} \leq 1$. Then there is $P \in \mathcal{H}_{\leq 2}(C(Y))$ such that
$$\|u-P\|_{B_{\lambda}(x)}<\lambda^{2+\alpha} .$$
Moreover, $\|P\|_{B_{1}} \leq C$.
Proof. We take $\|f\|_{B_{1}(x)}<\delta$ small so that, by the harmonic approximation Lemma 2.4, there is $h \in W^{1,2}(B(x, 1 / 2))$ harmonic with $\|u-h\|_{B(x, 1 / 2)}<\epsilon$ for some $\epsilon$ to be determined later. Decompose $h$ into its sub-quadratic and super-quadratic parts, that is $h=h_{\leq 2}+h_{>2}$ with $h_{\leq 2} \in \mathcal{H}_{\leq 2}$ and $h_{>2}$ being $L^{2}$-orthogonal to $\mathcal{H}_{\leq 2}$. Clearly, $\|h\|_{B(x, 1 / 2)} \leq\|u-h\|_{B(x, 1 / 2)}+\|u\|_{B(x, 1 / 2)} \leq C$ and the same holds for its components $h_{\leq 2}, h_{>2}$.

Fix $\alpha<\alpha^{\prime}<\mu$ and let $0<\lambda<1 / 2$ to be determined. Let $\epsilon_{0}=\epsilon_{0}^{\prime}\left(\alpha^{\prime}, \lambda^{\prime}\right) / 2$ with $\epsilon_{0}^{\prime}\left(\alpha^{\prime}, \lambda^{\prime}\right)$ be as in Lemma 4.3 and $\lambda^{\prime}=2 \lambda$. Set $P=h_{\leq 2}$, so
$$\begin{aligned}
\|u-P\|_{B(x, \lambda)} & \leq\|u-h\|_{B(x, \lambda)}+\left\|h_{>2}\right\|_{B(x, \lambda)} \\
& \leq(\lambda / 2)^{-m}\|u-h\|_{B(x, 1 / 2)}+(2 \lambda)^{2+\alpha^{\prime}}\left\|h_{>2}\right\|_{B(x, 1 / 2)} \\
& \leq(\lambda / 2)^{-m} \epsilon+C(2 \lambda)^{2+\alpha^{\prime}} .
\end{aligned}$$
Take first $0<\lambda<1 / 2$ such that $C(2 \lambda)^{2+\alpha^{\prime}}<\lambda^{2+\alpha} / 2$ and then $\epsilon>0$ so that $(\lambda / 2)^{-m} \epsilon<\lambda^{2+\alpha} / 2$. \(\square\)

We take $\delta, \epsilon_{0}$ and $\lambda$ as in the key step Proposition 5.1 and proceed with the proof of Theorem 1.1. So, let $\Delta u=f$ on $B_{2}$ and fix some $x \in B_{1}$. We can assume $f(x)=0$. Indeed, if $u^{\prime}=u-f(x) r_{1}^{2} / 4$, then $\Delta u^{\prime}(x)=0$ and $|D u|_{C^{\alpha}(x)} \leq$ $\left|D u^{\prime}\right|_{C^{\alpha}(x)}+(1 / 4)\left|f(x) \| D r_{1}^{2}\right|_{C^{\alpha}(x)}$ and we clearly have $\left|D r_{1}^{2}\right|_{C^{\alpha}(x)} \leq C$. Moreover, dividing $u$ by $\|u\|_{B(x, 1)}+(1 / \delta)|f|_{C^{\alpha}(x)}$, we may assume that $\|u\|_{B(x, 1)} \leq 1$ and $|f|_{C^{\alpha}(x)}<\delta$.

The Hölder coefficient $|f|_{C^{\alpha}(x)}$ is given by
$$\sup _{d(x, y)<1} \frac{|f(y)-f(x)|}{d(x, y)^{\alpha}} .$$
In particular, we are assuming that
$$\left(\rho^{-m} \int_{B(x, \rho)}|f-f(x)|^{2}\right)^{1 / 2}<\delta \rho^{\alpha}$$
for all $0<\rho<1$.
For $k=0,1, \ldots, \infty$, we consider $B\left(x, \lambda^{k}\right)$. Rescaling to unit size, we have $\lambda^{-k} B\left(x, \lambda^{k}\right)=B\left(x_{k}, 1\right)$ with $x_{k}=\lambda^{-k} x$. By the finitely many bad scales Lemma 4.1, there is $N=N\left(\epsilon_{0}, \lambda\right)$ such that all but at most $N$ of the scales $\lambda^{k}$ are good. More precisely, the scale $\lambda^{k}$ being good means that, after introducing cuts on some of the cone factors, $B\left(x_{k}, 1\right) \subset C(Y)$ for some $C(Y) \in \mathcal{C}$ with $\left|x_{k}\right|<\epsilon_{0}$.

The set of bad scales can be divided into a collection of at most $n$ disjoint intervals $I_{1}=\left[a_{1}, b_{1}\right), \ldots, I_{n}=\left[a_{n}, b_{n}\right)$ with the following property. If $k<a_{1}$, then

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/18a0a9d0-28f6-4b2a-a175-3c41e80c3b49-21.jpg?height=186&width=1032&top_left_y=405&top_left_x=544}
\captionsetup{labelformat=empty}
\caption{Figure 1. This picture illustrates the bad scales, in red, for a point $x=\left(r_{1} e^{i \theta_{1}}, r_{2} e^{i \theta_{2}}\right)$ lying on the regular locus of $C\left(S_{2 \pi \beta_{1}}^{1}\right) \times$ $C\left(S_{2 \pi \beta_{2}}^{1}\right)$ with $0<r_{1} \leq r_{2}$. The model cones $C(Y)$ are indicated for the good scales.}
\end{figure}
$\lambda^{k}$ is a good scale with model cone $C\left(Y_{0}\right)=\mathbf{R}_{(\beta)}^{m}$. If $b_{1} \leq k<a_{2}$, then $\lambda^{k}$ is a good scale whose model cone $C\left(Y_{1}\right)=\mathbf{R}_{\left(\beta^{\prime}\right)}^{m}$ has replaced a cone factor $C\left(S_{2 \pi \beta_{a}}^{1}\right)$ of the previous model cone, $C\left(Y_{0}\right)$, with $\mathbf{R}^{2}$; and so on. Finally, for $k \geq b_{n}$ we have $C\left(Y_{d}\right)=\mathbf{R}^{m}$. The set of bad scales depends on the point $x$, for regular points arbitrary close to the conical set the numbers $b_{n}$ get arbitrary large. See Figure 1 For singular points, $I_{n}=\emptyset$ and the model cone $C(Y)$ agrees with the tangent cone at $x$ for $k$ sufficiently large. We do not have uniform control on how large $k$ has to be so that $\lambda^{k}$ is a good scale. All we shall use is the uniform bound on the number of bad scales, $\sum_{a}\left|I_{a}\right|<N$.

Set $u_{0}=u$. Suppose $\lambda^{k}$ is a good scale for $k=0, \ldots, a_{1}-1$. Since $k=0$ is a good scale, this means that $|x|<\epsilon_{0}$. By assumption $\|u\|_{B(x, 1)} \leq 1$ and $\|f\|_{B(x, 1)}<\delta$, so we can apply the key step Proposition 5.1 to obtain $P_{1} \in \mathcal{H}_{\leq 2}$ such that $\left\|u_{0}-P_{1}\right\|_{B(x, \lambda)}<\lambda^{2+\alpha}$ and $\left\|P_{1}\right\|_{B(0,1)} \leq C$.