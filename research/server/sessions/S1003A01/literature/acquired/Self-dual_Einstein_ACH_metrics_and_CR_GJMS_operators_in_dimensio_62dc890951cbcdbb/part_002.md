---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Self-dual Einstein ACH metrics and CR GJMS operators in dimension three]

Theorem 5.1 ([21, Theorem 3.3]). Let $M$ be a three dimensional strictly pseudoconvex CR manifold and $g$ an ACH metric on a $\Theta$-manifold $\bar{X}$ with the boundary $M$. Let $\theta$ be a contact form on $M$ and let $\rho$ be the model defining function associated with $\theta$. Then, for any $k \in \mathbb{N}_{+}$and $f \in C^{\infty}(M)$, there exist $F, G \in C^{\infty}(\bar{X})$ with $\left.F\right|_{M}=f$ such that the function $u:=\rho^{-k+2} F+\left(\rho^{k+2} \log \rho\right) G$ satisfies
$$\left(\Delta+\frac{k^{2}}{4}-1\right) u=O\left(\rho^{\infty}\right),$$
where $\Delta=-g^{I J} \nabla_{I} \nabla_{J}$ is the Laplacian of $g$. The function $G$ is unique modulo $O\left(\rho^{\infty}\right)$ and $P_{2 k} f:=(-1)^{k+1} k!(k-1)!/\left.2 \cdot G\right|_{M}$ defines a formally self-adjoint linear differential operator $\mathcal{E}(k / 2-1, k / 2-1) \rightarrow \mathcal{E}(-k / 2-1,-k / 2-1)$ which is independent of the choice of $\theta$ and has the principal part $\Delta_{b}^{k}$.

We apply this theorem to our metric $g^{\lambda}$. Since $g^{\lambda}$ is determined to infinite order and the Taylor expansion has a universal expression in terms of the pseudohermitian structure, the operator $P_{2 k}^{\lambda}$ has a universal expression in terms of Tanaka-Webster connection. Thus, we obtain the CR GJMS operators $P_{2 k}^{\lambda}$ for all $k \geq 1$.

In order to prove that $P_{2 k}^{\lambda}$ is a polynomial in $\lambda$ of degree $\leq k / 3$, we will review the detail of its construction. A linear differential operator on $\bar{X}$ is called a $\Theta$-differential operator if it is the sum of linear differential operators of the form $a Y_{1} \cdots Y_{N}$, where $a \in C^{\infty}(\bar{X})$ and $Y_{j} \in \Gamma\left({ }^{\Theta} T \bar{X}\right)$. Note that a $\Theta$-differential operator preserves the subspace $\rho^{m} C^{\infty}(\bar{X}) \subset C^{\infty}(\bar{X})$ for each $m \geq 1$. We fix a contact form $\theta$ and denote the associated Tanaka-Webster connection by $\nabla^{\mathrm{TW}}$. Suppose that $g^{\lambda}$ is of the normal form
$$g^{\lambda}=k_{\rho}+4 \frac{d \rho^{2}}{\rho^{2}}$$
for $\theta$, where $k_{\rho}$ is a family of Riemannian metrics on $M$. Then, the Laplacian $\Delta$ of $g^{\lambda}$ is written as
$$\Delta=-\frac{1}{4}\left(\rho \partial_{\rho}\right)^{2}+\rho \partial_{\rho}+\rho^{2} \Delta_{b}-\rho^{4} T^{2}+\rho \Psi$$
with the $\Theta$-differential operator $\Psi$ defined by
$$\begin{aligned}
\Psi f= & -\frac{1}{8}\left(\partial_{\rho} \log \operatorname{det} k_{\rho}\right) \rho \partial_{\rho} f-\rho^{-1}\left(\left(k_{\rho}^{-1}\right)^{i j}-\left(k_{0}^{-1}\right)^{i j}\right) \nabla_{i}^{\mathrm{TW}} \nabla_{j}^{\mathrm{TW}} f \\
& +\frac{1}{2}\left(k_{\rho}^{-1}\right)^{i j}\left(k_{\rho}^{-1}\right)^{k l} \rho^{-1}\left(\nabla_{i}^{\mathrm{TW}}\left(k_{\rho}\right)_{j k}+\nabla_{j}^{\mathrm{TW}}\left(k_{\rho}\right)_{i k}-\nabla_{k}^{\mathrm{TW}}\left(k_{\rho}\right)_{i j}\right) \nabla_{l}^{\mathrm{TW}} f .
\end{aligned}$$
Here, the components are with respect to a $\Theta$-frame $\left\{\boldsymbol{Z}_{I}\right\}$, and we note that $\left(k_{\rho}^{-1}\right)^{i j}-\left(k_{0}^{-1}\right)^{i j}$ and $\nabla_{i}^{\mathrm{TW}}\left(k_{\rho}\right)_{j k}+\nabla_{j}^{\mathrm{TW}}\left(k_{\rho}\right)_{i k}-\nabla_{k}^{\mathrm{TW}}\left(k_{\rho}\right)_{i j}$ are $O(\rho)$ by (2.6). In particular, $\Psi$ involves $\partial_{\rho} g_{I J}^{\lambda}$ but not higher order derivatives.

Given a function $f \in C^{\infty}(M)$, we try to solve the equation
$$\left(\Delta+\frac{k^{2}}{4}-1\right)\left(\rho^{-k+2} F\right)=0$$
for $F \in C^{\infty}(\bar{X})$ with $\left.F\right|_{M}=f$. Let $F \sim \sum_{j=0}^{\infty} f^{(j)} \rho^{j},\left(f^{(j)} \in C^{\infty}(M)\right)$ be the Taylor expansion of $F$ along $M$. By (5.1), we have
$$\left(\Delta+\frac{k^{2}}{4}-1\right)\left(\rho^{-k+2+j} f^{(j)}\right)=\rho^{-k+2+j}\left(-\frac{1}{4} j(j-2 k) f^{(j)}+\rho \mathcal{D}_{j} f^{(j)}\right),$$
where $\mathcal{D}_{j}$ is a $\rho$-dependent linear differential operator on $M$. Starting with $f^{(0)}=f$, we inductively define $f^{(j)}$ so that $F$ satisfies
$$\left(\Delta+\frac{k^{2}}{4}-1\right)\left(\rho^{-k+2} F\right)=O\left(\rho^{-k+3+j}\right) .$$
Let $\mathcal{D}_{j} \sim \sum_{l=0}^{\infty} \mathcal{D}_{j}^{(l)} \rho^{l}$ be the Taylor expansion of $\mathcal{D}_{j}$. Then, by (5.2) $f^{(j)}$ is determined for $j \leq 2 k-1$ as
$$f^{(j)}=\frac{4}{j(j-2 k)} \sum_{l=0}^{j-1} \mathcal{D}_{l}^{(j-1-l)} f^{(l)} .$$
We cannot define $f^{(2 k)}$ due to the vanishing of the coefficient of $f^{(2 k)}$ in (5.2), and we need to introduce the logarithmic term $\left(\rho^{k+2} \log \rho\right) G$ in which the coefficient $\left.G\right|_{M}$ is a multiple of
$$\left.\left(\rho^{-k-2}\left(\Delta+\frac{k^{2}}{4}-1\right)\left(\rho^{-k+2} F\right)\right)\right|_{M} .$$
Therefore, up to a constant multiple, $P_{2 k}^{\lambda} f$ is given by
$$\sum_{j=0}^{2 k-1} \mathcal{D}_{j}^{(2 k-1-j)} f^{(j)}$$
Since $\Psi$ involves only $g_{I J}^{\lambda}$ and their first order derivatives in $\rho, \mathcal{D}_{j}^{(l)}$ involves $\partial_{\rho}^{m} g_{I J}^{\lambda}$ for $m \leq l+1$. Consequently, $P_{2 k}^{\lambda}$ is written in terms of $\partial_{\rho}^{m} g_{I J}^{\lambda}(m \leq 2 k)$, and by Proposition 4.2 it is a polynomial in $\lambda$ of degree $\leq k / 3$. Thus we complete the proof of Theorem 1.3.

\section*{6. Convergence of the formal solutions}

We will prove Theorem 1.4, which asserts that the formal solution $g^{\lambda}$ converges to a real analytic ACH metric near $M$ when $M$ is a real analytic CR manifold. In the case of $\lambda=0$, this recovers the result of Biquard [2]. The key tool is the result of Baouendi-Goulaouic [1] on the unique existence of the solution to a singular nonlinear Cauchy problem. Let us state their theorem in a form which fits to our setting.

We regard local coordinates $(x, \rho)$ of $M \times[0, \infty)_{\rho}$ as complex variables and consider an equation for a $\mathbb{C}^{N}$-valued holomorphic function $v(x, \rho)$ of the form
$$\begin{aligned}
\left(\rho \partial_{\rho}\right)^{m} v+A_{m-1}\left(\rho \partial_{\rho}\right)^{m-1} v & +\cdots+A_{0} v \\
& =F\left(x, \rho,\left\{\left(\rho \partial_{\rho}\right)^{l} \partial_{x}^{\alpha}(\rho v)\right\}_{l+|\alpha| \leq m, l<m}\right),
\end{aligned}$$
where $A_{j}$ is an $N \times N$ matrix and $F\left(x, \rho,\left\{y_{l, \alpha}\right\}_{l+|\alpha| \leq m, l<m}\right)$ is a holomorphic function near 0 . For each $k \in \mathbb{N}$, we set
$$\mathcal{P}(k):=k^{m} I+k^{m-1} A_{m-1}+\cdots+A_{0},$$
where $I$ is the identity matrix of size $N$. Then, by [1, Theorem 3.1] we have the following theorem:

Theorem 6.1. If $\operatorname{det} \mathcal{P}(k) \neq 0$ for all $k \in \mathbb{N}$, the equation (6.1) has a unique holomorphic solution $v(x, \rho)$ near $(0,0)$.

In the original statement of [1, Theorem 3.1], the right-hand side of the equation (6.1) is replaced by $G\left(\rho,\left\{\left(\rho \partial_{\rho}\right)^{l} \partial_{x}^{\alpha}(\rho v)\right\}_{l+|\alpha| \leq m, l<m}\right)$ with $G$ a $C^{\infty}$-map
$$G: \mathbb{C} \times B^{N^{\prime}} \longrightarrow B,$$
where $B$ is the Banach space of $\mathbb{C}^{N}$-valued bounded holomorphic functions of $x$ on a fixed polydisc, and $N^{\prime}$ is the number of multiindices $(l, \alpha)$ such that $l+|\alpha| \leq$
$m, l<m$. Also, the solution $v$ is given as a $C^{\infty}$-function of $\rho$ valued in $B$. In our equation (6.1), $G$ is given by $G\left(\rho,\left\{y_{l, \alpha}\right\}\right):=F\left(x, \rho,\left\{y_{l, \alpha}(x)\right\}\right)$. Since this is analytic in $\rho$, it follows from [1, Remark 2.2] and the proof of [1, Theorem 3.1] that the solution $v(x, \rho)$ is $C^{\infty}$ and $v\left(x, \rho^{m}\right)$ is holomorphic, which implies that $v(x, \rho)$ itself is holomorphic. Thus we obtain Theorem 6.1 as a special case of their theorem.

Now we apply this theorem to our case. We assume that $M$ is a real analytic CR manifold. Let $g_{I J}^{\lambda}$ be the components of the formal solution $g^{\lambda}$ in a $\Theta$-frame $\left\{\boldsymbol{Z}_{I}\right\}$, and let
$$g_{I J}^{(k)}:=\left.\frac{1}{k!} \partial_{\rho}^{k} g_{I J}^{\lambda}\right|_{M}$$
be the Taylor coefficients, which are analytic functions on $M$. We consider an ACH metric of the form
$$\widetilde{g}_{I J}^{\lambda}=\sum_{k=0}^{8} \rho^{k} g_{I J}^{(k)}+\rho^{9} \widetilde{\varphi}_{I J},$$
which automatically satisfies $E_{I J}=O\left(\rho^{9}\right)$. Then, we consider the equation
$$-8 \rho^{-9}\left(E_{00}, E_{1 \overline{1}}, E_{01}, E_{11}\right)=0$$
for $v=\left(\widetilde{\varphi}_{00}, \widetilde{\varphi}_{1 \overline{1}}, \widetilde{\varphi}_{01}, \widetilde{\varphi}_{11}\right)$. We shall show that this equation is written in the form (6.1) for $m=2$ and satisfies the assumption of Theorem 6.1; then we can conclude that $g_{I J}^{\lambda}$ converges since it gives the Taylor expansion of the solution $v$.

We see that in Lemma 3.1 the negligible term which we ignored in the computation of $E_{I J}$ is an analytic function in
$$x, \rho, \rho\left(\rho \partial_{\rho}\right)^{l} \partial_{x}^{\alpha}\left(\rho^{9} \widetilde{\varphi}\right) \text { for } l+|\alpha| \leq 2, l<2 .$$
Thus, it can be written in the form
$$f_{I J}^{(1)}(x, \rho)+\rho^{9} f_{I J}^{(2)}\left(x, \rho,\left\{\left(\rho \partial_{\rho}\right)^{l} \partial_{x}^{\alpha}(\rho \widetilde{\varphi})\right\}_{l+|\alpha| \leq 2, l<2}\right)$$
with analytic functions $f_{I J}^{(1)}, f_{I J}^{(2)}$. Then, by Lemma 3.1, we have
$$\begin{aligned}
-8 E_{00}= & I_{1}\left(\rho \partial_{\rho}\right) \varphi_{00}+I_{2}\left(\rho \partial_{\rho}\right) \varphi_{1 \overline{1}} \\
& +16 \rho^{4}|A|^{2}+f_{00}^{(1)}(x, \rho)+\rho^{9} f_{00}^{(2)}\left(x, \rho,\left\{\left(\rho \partial_{\rho}\right)^{l} \partial_{x}^{\alpha}(\rho \widetilde{\varphi})\right\}_{l+|\alpha| \leq 2, l<2}\right),
\end{aligned}$$
where
$$\varphi_{I J}=\sum_{k=1}^{8} \rho^{k} g_{I J}^{(k)}+\rho^{9} \widetilde{\varphi}_{I J}$$
and
$$I_{1}(t)=t^{2}-6 t-4, \quad I_{2}(t)=-4(t-2) .$$
Since $E_{00}=O\left(\rho^{9}\right)$, we have
$$I_{1}\left(\rho \partial_{\rho}\right)\left(\sum_{k=1}^{8} \rho^{k} g_{00}^{(k)}\right)+I_{2}\left(\rho \partial_{\rho}\right)\left(\sum_{k=1}^{8} \rho^{k} g_{1 \overline{1}}^{(k)}\right)+16 \rho^{4}|A|^{2}+f_{00}^{(1)}(x, \rho)=\rho^{9} f_{00}^{(0)}(x, \rho)$$
with some analytic function $f_{00}^{(0)}$. Therefore, the equation $-8 \rho^{-9} E_{00}=0$ is written as
$$I_{1}\left(\rho \partial_{\rho}+9\right) \widetilde{\varphi}_{00}+I_{2}\left(\rho \partial_{\rho}+9\right) \widetilde{\varphi}_{1 \overline{1}}+F_{00}\left(x, \rho,\left\{\left(\rho \partial_{\rho}\right)^{l} \partial_{x}^{\alpha}(\rho \widetilde{\varphi})\right\}_{l+|\alpha| \leq 2, l<2}\right)=0$$
with an analytic function $F_{00}$.

Similarly, the equations $-8 \rho^{-9} E_{I J}=0$ for $(I, J)=(1, \overline{1}),(0,1),(1,1)$ are respectively written as
$$\begin{aligned}
I_{3}\left(\rho \partial_{\rho}+9\right) \widetilde{\varphi}_{00}+I_{4}\left(\rho \partial_{\rho}+9\right) \widetilde{\varphi}_{1 \overline{1}}+F_{1 \overline{1}}\left(x, \rho,\left\{\left(\rho \partial_{\rho}\right)^{l} \partial_{x}^{\alpha}(\rho \widetilde{\varphi})\right\}_{l+|\alpha| \leq 2, l<2}\right) & =0, \\
I_{5}\left(\rho \partial_{\rho}+9\right) \widetilde{\varphi}_{01}+F_{01}\left(x, \rho,\left\{\left(\rho \partial_{\rho}\right)^{l} \partial_{x}^{\alpha}(\rho \widetilde{\varphi})\right\}_{l+|\alpha| \leq 2, l<2}\right) & =0, \\
I_{6}\left(\rho \partial_{\rho}+9\right) \widetilde{\varphi}_{11}+F_{11}\left(x, \rho,\left\{\left(\rho \partial_{\rho}\right)^{l} \partial_{x}^{\alpha}(\rho \widetilde{\varphi})\right\}_{l+|\alpha| \leq 2, l<2}\right) & =0,
\end{aligned}$$
where $F_{1 \overline{1}}, F_{01}, F_{11}$ are analytic functions and
$$I_{3}(t)=-t+4, \quad I_{4}(t)=t^{2}-6 t-8, \quad I_{5}(t)=(t+1)(t-5), \quad I_{6}(t)=t(t-4) .$$
Hence the equation (6.2) is of the form (6.1), and we have
$$\begin{aligned}
\operatorname{det} \mathcal{P}(k) & =\operatorname{det}\left(\begin{array}{ccc}
I_{1}(k+9) & I_{2}(k+9) & \\
I_{3}(k+9) & I_{4}(k+9) & \\
& & I_{5}(k+9) \\
& & I_{6}(k+9)
\end{array}\right) \\
& =(k+1)(k+3)(k+4)(k+5)(k+9)^{2}(k+10)(k+11) \\
& \neq 0
\end{aligned}$$
for any $k \in \mathbb{N}$. Thus, by Theorem 6.1 the equation (6.2) has a unique holomorphic solution and we complete the proof of Theorem 1.4.

\section*{References}
\begin{itemize}
\item[] [1] M. S. Baouendi and C. Goulaouic, Singular nonlinear Cauchy problems, J. Diff. Eq. 22 (1976), 268-291.
\item[] [2] O. Biquard, Sur les variétés CR de dimension 3 et les twisteurs, Ann. Inst. Fourier 57 (2007), no. 4, 1161-1180.
\item[] [3] A. Čap, J. Slovák, and V. Souček, Bernstein-Gelfand-Gelfand Sequences, Ann. of Math. 154 (2001), 97-113.
\item[] [4] J.-H. Cheng and J.M. Lee, The Burns-Epstein invariant and deformation of CR structures, Duke Math. J. 60 (1990) 221-254.
\item[] [5] C. L. Epstein, R. B. Melrose, and G. A. Mendoza, Resolvent of the Laplacian on strictly pseudoconvex domains, Acta Math. 167 no. 1-2 (1991), 1-106.
\item[] [6] C. L. Fefferman, Monge-Ampère equations, the Bergman kernel, and geometry of pseudoconvex domains, Ann. of Math. 103 (1976), 395-416; erratum 104 (1976), 393-394.
\item[] [7] C. L. Fefferman, C. R. Graham, $Q$-curvature and Poincaré metrics, Math. Res. Lett. 9 (2002), 139-151.
\item[] [8] C. L. Fefferman, C. R. Graham, The ambient metric, Princeton Univ. Press. 2011.
\item[] [9] C. Fefferman and K. Hirachi, Ambient metric construction of $Q$-curvature in conformal and CR geometries, Math. Res. Lett. 10 (2003) 819-832.
\item[] [10] A. R. Gover and C. R. Graham, CR invariant powers of the sub-Laplacian, J. Reine Angew. Math. 583 (2005), 1-27.
\item[] [11] A. R. Gover and K. Hirachi, Conformally invariant powers of the Laplacian-A complete non-existence theorem, Jour. Amer. Math. Soc. 17 (2004), 389-405.
\item[] [12] C. R. Graham, Scalar boundary invariants and the Bergman kernel, in Complex Analysis II, Lect. Notes in Math. 1276 pp. 108-135, Springer, 1987.
\item[] [13] C. R. Graham, R. Jenne, L. J. Mason, and G. A. J. Sparling, Conformally invariant powers of the Laplacian, I: Existence, J. London Math. Soc. 46 (1992), 557-565.
\item[] [14] C. R. Graham and M. Zworski, Scattering matrix in conformal geometry, Invent. Math. 152 (2003), 89-118.
\item[] [15] P. Hislop, P. Perry, and S.-H. Tang, CR-invariants and the scattering operator for complex manifolds with boundary, Analysis \& PDE 1 (2008), 197-227.
\item[] [16] C. LeBrun, $\mathcal{H}$-space with a cosmological constant, Proc. Roy. Soc. London A 380 (1982), 171-185.
\item[] [17] J.M. Lee, Pseudo-Einstein structures on CR manifolds, Amer. J. Math. 110 (1988) 157-178.
\item[] [18] J.M. Lee and R. Melrose, Boundary behaviour of the complex Monge-Ampère equation, Acta Math. 148 (1982) 159-192.
\item[] [19] Y. Matsumoto, Asymptotically complex hyperbolic Einstein metrics and CR geometry, Ph.D. Thesis, The University of Tokyo, 2013.
\end{itemize}
\begin{itemize}
\item[] [20] Y. Matsumoto, Asymptotics of ACH-Einstein metrics, J. Geom. Anal. 24 (2014), no. 4, 2135-2185.
\item[] [21] Y. Matsumoto, GJMS operators, $Q$-curvature, and obstruction tensor of partially integrable CR manifolds, Diff. Geom. Appl. 45 (2016), 78-114.
\end{itemize}

Institute of Mathematics, Academia Sinica, Astronomy-Mathematics Building, No.
1, Sec. 4, Roosevelt Road, Taipei 10617, TAIWAN
E-mail address: marugame@gate.sinica.edu.tw