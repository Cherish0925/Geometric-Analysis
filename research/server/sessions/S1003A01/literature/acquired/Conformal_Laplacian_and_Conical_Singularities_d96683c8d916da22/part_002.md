---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Conformal Laplacian and Conical Singularities]

Here we have either $a_{1}=0$ or
$$\nu_{i j}^{(o, \pm)}=-\frac{n}{2} \pm \sqrt{\left(\frac{n}{2}\right)^{2}+K_{i j}-(n-1)} .$$
Notice now that $\nu_{i j}^{e \pm}=\nu_{i j}^{o \pm}+1$ and, more then this, $K_{\nu_{i j}^{o \pm}+m+1}=K_{\nu_{i j}^{e \pm}+m}$. Comparing the power series solution $u_{i j}^{e \pm}(\ell)$ with even indices $m$ and $u_{i j}^{o \pm}(\ell)$ with odd indices $m$ we see that $u_{i j}^{e \pm}(\ell)=u_{i j}^{o \pm}(\ell)$. Thus it is enough to study the solution $u_{i j}^{e \pm}(\ell)$ only. We have for these solutions:
$$\begin{aligned}
\frac{n}{2}+\nu_{i j}^{e \pm} & =1 \pm \sqrt{\left(\frac{n-2}{2}\right)^{2}+K_{i j}} \\
& =1 \pm \frac{n-2}{2} \sqrt{1+\frac{\Lambda}{(n-1)(n-2)}+\frac{8}{(n-2)^{2}}\left(\frac{\lambda_{i}^{p}}{r_{p}^{2}}+\frac{\lambda_{j}^{q}}{r_{q}^{2}}\right)} \\
& =1 \pm \frac{n-2}{2} \sqrt{\mu^{2}+\frac{8}{(n-2)^{2}}\left(\frac{\lambda_{i}^{p}}{r_{p}^{2}}+\frac{\lambda_{j}^{q}}{r_{q}^{2}}\right)} .
\end{aligned}$$
Here
$$\mu^{2}=1+\frac{\Lambda}{(n-1)(n-2)}=\frac{2}{(n-1)(n-2)}\left[\frac{p(p-1)}{r_{p}^{2}}+\frac{q(q-1)}{r_{q}^{2}}\right],$$
see Appendix.
From this we conclude that the solution $u_{i j}^{e-}$ with the leading term $\ell^{\nu_{i j}^{e-}}$ never belongs to $H_{2}^{1}(K)$ but belongs to $L_{2}(K)$ if (and only if)
$$\frac{n-2}{2} \sqrt{\mu^{2}+\frac{8}{(n-2)^{2}}\left(\frac{\lambda_{i}^{p}}{r_{p}^{2}}+\frac{\lambda_{j}^{q}}{r_{q}^{2}}\right)}<1,$$
which is equivalent to
$$\mu^{2}+\frac{8}{(n-2)^{2}}\left(\frac{\lambda_{i}^{p}}{r_{p}^{2}}+\frac{\lambda_{j}^{q}}{r_{q}^{2}}\right)<\frac{4}{(n-2)^{2}} .$$

For $i=j=0$ (radial solution) this condition, after substitution of value for $\mu^{2}$, takes the form
$$\left[\frac{p(p-1)}{r_{p}^{2}}+\frac{q(q-1)}{r_{q}^{2}}\right]<\frac{2(n-1)}{n-2} .$$
These conditions on $n, p, r_{p}, r_{q}$ are met in the nonlinear case as well; we call this situation the "minus-case". Thus, in the minus-case, the solution $u_{00}^{e-}$ belongs to $L_{2}(K)$. On the other hand, the solution $u_{i j}^{e+}$ always belongs to $H_{2}^{1}(K)$ (see Proposition 3.7 and Appendix). It belongs to $H_{2}^{2}(K)$ (classical solution) if and only if
$$\begin{aligned}
& \frac{n-2}{2} \sqrt{\mu^{2}+\frac{8}{(n-2)^{2}}\left(\frac{\lambda_{i}^{p}}{r_{p}^{2}}+\frac{\lambda_{j}^{q}}{r_{q}^{2}}\right)}>1, \quad \text { that is if } \\
& \mu^{2}+\frac{8}{(n-2)^{2}}\left(\frac{\lambda_{i}^{p}}{r_{p}^{2}}+\frac{\lambda_{j}^{q}}{r_{q}^{2}}\right)>\frac{4}{(n-2)^{2}} .
\end{aligned}$$
For $i=j=0$ (the radial solution) this condition, after substitution of $\mu^{2}$, takes the form
$$\left[\frac{p(p-1)}{r_{p}^{2}}+\frac{q(q-1)}{r_{q}^{2}}\right]>\frac{2(n-1)}{n-2} .$$
We will work with the same condition on $n, p, r_{p}, r_{q}$ in the nonlinear case; we call this situation the "plus-case". Thus, in the plus-case, the solution $u_{00}^{e+}$ belongs to $H_{2}^{2}(K)$.

Now we return to the recursive equation $\left(Y_{m+2}\right)$ for the coefficients $a_{m}$ in the case $\nu_{i j}^{e+}$. We write it in the form:
$$K_{\nu_{i j}^{e+}+m} a_{m+2}=-Q_{1} a_{m}, \text { which gives } a_{m+2}=\frac{-Q_{1} a_{m}}{K_{\nu_{i j}^{e+}+m}}$$
provided the denominator is not zero.
Notice that, provided equation ( $Y_{0}$ ) is satisfied, the expression given above for $K_{\nu_{i j}^{e+}+m}$ can be rewritten as
$$K_{\nu_{i j}^{e+}+m}=(m+2)\left(2 \nu_{i j}+m+n\right) .$$
It follows from this formula that these coefficients are always nonzero. We use the previous formula for $a_{m+2}$ recursively to obtain
$$a_{2 m}=\frac{\left(-Q_{1}\right)^{m}}{\prod_{t=1}^{m} K_{\nu_{i j}^{e+}+2 t}} a_{0}=\frac{\left(-Q_{1}\right)^{m}}{\prod_{t=1}^{m}(2 t+2)\left(2 \nu_{i j}+2 t+n\right)} a_{0},$$
and for the solution $u_{i j}^{e+}$, which we redenote to be $u_{i j}$, we have
$$u_{i j}=a_{i j} \ell^{\nu_{i j}} \sum_{m=0}^{\infty} \frac{\left(-Q_{1}\right)^{m}}{\prod_{t=1}^{m}(2 t+2)\left(2 \nu_{i j}+2 t+n\right)} \ell^{2 m}$$
with arbitrary constants $a_{i j} \in R$.
We combine all calculations in the following theorem.
Theorem 6.1 Let $M$ be a manifold with tame conical singularity as above, with $\operatorname{dim} M \geq 5$, and $Q_{1}>0$.
\begin{itemize}
\item[(1)] There exists a solution $u_{i j}$ of the equation (22), restricted on the cone $K$, is given by
$$\begin{aligned}
& u_{i j}=\ell^{\nu_{i j}} \cdot\left(\sum_{m=0}^{\infty} \frac{(-1)^{m} Q_{1}^{m} \ell^{2 m}}{\prod_{t=1}^{m}(2 t+2)\left(2 \nu_{i j}+2 t+n\right)}\right) \cdot a_{0}, \text { with } \\
& \nu_{i j}=\frac{n-2}{2}\left[\sqrt{\mu^{2}+\frac{4}{(n-2)^{2}}\left(\frac{2 \lambda_{i}^{p}}{r_{p}^{2}+\frac{2 \lambda_{j}^{q}}{r_{q}^{2}}}\right)}-1\right], \text { where } \\
& \mu^{2}=\frac{2}{(n-1)(n-2)}\left[\frac{p(p-1)}{r_{p}^{2}}+\frac{q(q-1)}{r_{q}^{2}}\right] .
\end{aligned}$$
This solution belongs to the Sobolev space $H_{2}^{1}(M)$ and also to the space $H_{2}^{2}(M)$ in the plus-case (see (30)).
\item[(2)] The second linearly independent solution (denoted above as $u_{i j}^{e,-}$ ) of the equation (22) only belongs to $L_{2}(K)$ in the minus-case (see (31)).
\item[(3)] The general solution $u(\ell, \theta, \psi)$ of (22) in $H_{2}^{1}(K)$ has the form
$$u(\ell, \theta, \psi)=\sum_{i j} a_{i j} \ell_{i j}^{e+} f_{i j}(\ell) \kappa_{i}^{p}(\theta) \kappa_{j}^{q}(\psi) .$$
Here the functions $f_{i j}(x)$ are defined by
$$f_{i j}\left(\sqrt{Q_{1}} \ell\right)=\sum_{m=0}^{\infty} \frac{\left(-Q_{1}\right)^{m}}{\prod_{t=1}^{m}(2 t+2)\left(2 \nu_{i j}+2 t+n\right)} \ell^{2 m},$$
so that $u_{i j}^{e+}=a_{i j} \ell^{\nu_{i}^{e+}} f_{i j}(\ell)$ and the coefficients $a_{i j}$ ensure convergence of this series with respect to $H_{2}^{1}(K)$-norm.
\end{itemize}

We notice that the exponent $\nu_{i j}$ of the solution $u_{i j}$ does not depend on the eigenvalue $Q_{1}$.
Remark. We notice that the radial solution $u_{00}^{e+}(\ell)$ of the equation (20) has the following asymptotic
$$u_{00}(\ell) \sim \ell^{\nu_{00}}, \nu_{00}=\frac{n-2}{2}\left(\sqrt{1+\frac{\Lambda}{(n-1)(n-2)}}-1\right)=\frac{n-2}{2}(\mu-1),$$
and that for any solution $u(\ell, \theta, \psi)$ of (20), there exists the radial solution $u_{0}(\ell)$ of (20) (radial part of $u$ ) such that as $\ell \rightarrow 0$,
$$\left|u(\ell, \theta, \psi)-u_{0}(\ell)\right| \leqq C \ell^{\sigma}, \quad \text { for some } \sigma>0 .$$

\section*{7 Asymptotic of solutions: the nonlinear case}

In this section we study the nonlinear Yamabe equation near the singular point:
$$\frac{\partial^{2} u}{\partial \ell^{2}}+\frac{n-1}{\ell} \frac{\partial u}{\partial \ell}+\frac{2}{r_{p}^{2} \ell^{2}} \Delta_{\theta} u+\frac{2}{r_{q}^{2} \ell^{2}} \Delta_{\psi} u-\frac{n-2}{4(n-1)} \frac{\Lambda}{\ell^{2}} u+Q_{\alpha} u^{\alpha}=0$$
defined on the open set $(0, \varepsilon) \times S^{p} \times S^{q}$. Here $3 \leq p \leq n-3, \Lambda=\Lambda\left(p, q, r_{p}, r_{q}\right)$ is the curvature factor, see Appendix for the details.

We restrict our attention to the radial solutions, and return to the general case at the end of this section. Thus, we study positive solutions $u=u(\ell)$ of the equation (24).
7.1. Reduction to a dynamical system. We use the cylindrical coordinates $t=-\ln \ell$, or $\ell=e^{-t}$, so that $t \longrightarrow \infty$ as $\ell \longrightarrow 0$. Then the equation (24) becomes
$$u_{t t}-(n-2) u_{t}-\frac{n-2}{4(n-1)} \Lambda u+Q_{\alpha} e^{-2 t} u^{\alpha}=0 .$$
We are looking for solutions of (25) defined on the set
$$(-\ln (\varepsilon),+\infty) \times S^{p} \times S^{q} .$$
We use the substitution $u(t)=e^{\lambda t} w(t)$ in (25), where $\lambda=\frac{2}{\alpha-1}$. Then the time-dependence of the coefficients in (25) disappears, and one obtains the following equation:
$$w^{\prime \prime}+\left(\frac{4}{\alpha-1}-(n-2)\right) w^{\prime}+\left(\frac{4}{(\alpha-1)^{2}}-\frac{2(n-2)}{\alpha-1}-\frac{n-2}{4(n-1)} \Lambda\right) w+Q_{\alpha} w^{\alpha}=0 .$$

We exclude the case $\alpha=1$. Notice that the functions $u(\ell)$ and $w(t)$ are related as follows: $u(\ell)=\ell^{-\frac{2}{\alpha-1}} w(-\ln \ell)$. We denote
$$\bar{b}=-\frac{4}{\alpha-1}+(n-2), \quad \bar{a}=-\frac{4}{(\alpha-1)^{2}}+\frac{2(n-2)}{\alpha-1}+\frac{n-2}{4(n-1)} \Lambda .$$
Let $x=w, y=w^{\prime}$. Then (26) is equivalent to the dynamical system
$$\left\{\begin{aligned}
x^{\prime} & =y \\
y^{\prime} & =\bar{a} x+\bar{b} y-Q_{\alpha} x^{\alpha} .
\end{aligned}\right.$$
7.2. The equilibrium points. We find the equilibrium points of (28) by solving the system:
$$\left\{\begin{array}{l}
y=0, \\
\bar{a} x-Q_{\alpha} x^{\alpha}=x\left(\bar{a}-Q_{\alpha} x^{\alpha-1}\right)=0 .
\end{array}\right.$$
Since $y=0$, the second equation has the solution $x_{1}=0$ for all values of the parameters and, in addition, the solution
$$x_{2}=\left(\frac{\bar{a}}{Q_{\alpha}}\right)^{\frac{1}{\alpha-1}}>0$$
provided $\frac{\bar{a}}{Q_{\alpha}}>0$. Thus the system (28) has one equilibrium point $w_{1}=$ $(0,0)$ if $\frac{\bar{a}}{Q_{\alpha}} \leq 0$, and an additional one, $w_{2}=\left(x_{2}, 0\right)$ with $x_{2}$ given by (29) if $\frac{\bar{a}}{Q_{\alpha}}>0$.
Remark. Notice that we consider only positive values for the root $x_{2}$ since we are looking for the positive solutions of (26). In terms of the dynamical system (28) this means that a solution has to stay in the right half-plane for $t>T$ for some $T$.
7.3. The equilibrium point $w_{1}$. To study a behavior of (28) near $(0,0)$, we analyze its linear approximation:
$$A_{(0,0)}=\left(\begin{array}{cc}
0 & 1 \\
\bar{a} & \bar{b}
\end{array}\right) .$$
The parameters $\bar{b}$ and $\bar{a}$ are defined in (27). Thus, we have the characteristic equation
$$\lambda^{2}-\bar{b} \lambda-\bar{a}=0, \quad \text { with the roots } \quad \lambda_{ \pm}=\frac{\bar{b}}{2} \pm \sqrt{\frac{\bar{b}^{2}}{4}+\bar{a}} .$$

The corresponding eigenvectors $\vec{v}_{ \pm}$are given by
$$\vec{v}_{ \pm}=\binom{1}{\lambda_{ \pm}}, \quad \text { so that } \quad A_{(0,0)} \vec{v}_{ \pm}=\lambda_{ \pm} \vec{v}_{ \pm} .$$
We show (see Appendix, Claim 8.1) that $\bar{b}<0$ for all $1<\alpha \leq \alpha^{*}$, and that $\frac{\bar{b}^{2}}{4}+\bar{a}>0$ if $n \geq 3$. Therefore, the point $(0,0)$ is a saddle point if $\bar{a}>0$, and a stable focus if $\bar{a}<0$.
7.4. The equilibrium point $w_{2}$. Now we study the second equilibrium point $w_{2}$ :
$$w_{2}=\left(x_{2}, 0\right), \quad \text { with } \quad x_{2}=\left(\frac{\bar{a}}{Q_{\alpha}}\right)^{\frac{1}{\alpha-1}},$$
which exists provided $\bar{a} Q_{\alpha}>0$. Here we have the following linear approximation of (28) near the point $w_{2}$ :
$$A_{w_{2}}=\left(\begin{array}{cc}
0 & 1 \\
\bar{a}-\alpha Q_{\alpha} \frac{\bar{a}}{Q_{\alpha}} & \bar{b}
\end{array}\right)=\left(\begin{array}{cc}
0 & 1 \\
\bar{a}(1-\alpha) & \bar{b}
\end{array}\right)$$
with the characteristic equation $r^{2}-\bar{b} r+\bar{a}(\alpha-1)=0$. We have the following eigenvalues $r_{ \pm}$and the eigenvectors $\vec{z}_{ \pm}$:
$$r_{ \pm}=\frac{\bar{b}}{2} \pm \sqrt{\frac{\bar{b}^{2}}{4}-\bar{a}(\alpha-1)}, \quad \vec{z}_{ \pm}=\binom{1}{r_{ \pm}}, \quad \text { so that } \quad A_{\left(x_{2}, 0\right)} \vec{z}_{ \pm}=r_{ \pm} \vec{z}_{ \pm} .$$
Thus, we have the following alternatives for the equilibrium point $w_{2}$.
\begin{itemize}
\item[1.] If $\bar{a}<0$, then $w_{2}$ is a saddle.
\item[2.] If $\bar{a}>0$, but $\frac{\bar{b}^{2}}{4}-\bar{a}(\alpha-1)<0$, then the $w_{2}$ is a stable focus.
\item[3.] If $\bar{a}>0$, and $\frac{\bar{b}^{2}}{4}-\bar{a}(\alpha-1)>0$, then $w_{2}$ is a stable node.
\end{itemize}
It is shown in Appendix that all three cases are realized for different values of $\alpha$.
7.5. The phase pictures. Now we study the critical points of the system (28) for different values of parameters $\alpha, Q_{\alpha}$, and others. We determine asymptotic behavior of the solutions of system (28) by comparing them with the corresponding solutions of the linearized system at the points $w_{1}, w_{2}$. For all $\alpha<\alpha^{*}$ the points $w_{1}, w_{2}$ are hyperbolic. Thus, locally
(near critical points) linear and nonlinear phase pictures are trajectory-equivalent. Moreover, those solutions $w(t)$ of the nonlinear system which go to $w_{2}$ as $t \rightarrow+\infty$ have the asymptotic behavior $w(t) \simeq w_{2}$, and this determines to which Sobolev spaces they belong. For the unbounded solutions $(w(t) \rightarrow \infty)$, one has $x(t) \rightarrow \infty$. Thus, the corresponding asymptotic behavior of $u(\ell)$ is worse than that of an $\alpha$-basic function. This allows us to decide, in most cases, to which Sobolev space $H_{2}^{k}(M)$ those solutions belong.

Finally, there are solutions $w(t)$ that tend to $w_{1}=(0,0)$ as $t \rightarrow+\infty$. Locally (near $w_{1}$ ), the nonlinear system may be thought of as a perturbation of the linear one. We use results by Lettenmeyer, Hartman and Wintner (see [10, Ch. 4, Theorems 5,9], and [13, Ch. X, Theorem 13.1, Corollary 16.3]). We check below that in our case the conditions of those theorems are met. These results guarantee that the principal term of asymptotic behavior is the same for a solution tending to the origin for the system (28) and its linearization.

The results presented below depend on the inequalities below. We will also describe these cases as the "plus-case" and the "minus-case" respectively:
$$\begin{array}{ll}
\text { The plus-case: } & \frac{p(p-1)}{r_{p}^{2}}+\frac{q(q-1)}{r_{q}^{2}}>\frac{2(n-1)}{n-2} . \\
\text { The minus-case: } & \frac{p(p-1)}{r_{p}^{2}}+\frac{q(q-1)}{r_{q}^{2}}<\frac{2(n-1)}{n-2} .
\end{array}$$
We have the following alternative cases.
Case 1: $\bar{a}<0, Q_{\alpha}<0$. In this case the phase picture is given in Fig. 7.1. Here we have two families and three separate solutions:
(1) The family $C_{\infty}$ consists of the solutions $w(t)$ going to $\infty$ asymptotically as $t \rightarrow+\infty$ nestling at the unstable separatrix trajectory of the point $w_{2}$. We notice that for given $\alpha$ the corresponding solution $u(\ell)$ approaches $+\infty$ faster, compared to an $\alpha$-basic function $\ell^{-\frac{2}{\alpha-1}}$ as $\ell \rightarrow 0$.

As it is proved in the Appendix, in the plus-case (30), $\alpha_{0}<\frac{n+4}{n}$ and, since $\bar{a}<0, \alpha<\alpha_{0}$. Thus, an $\alpha$-basic function does not belong to $L_{2}(K)$. Therefore, the solutions from the family $C_{\infty}$ do not belong to $L_{2}(K)$.

In the minus case (31) if $\alpha<\frac{n+4}{n}$, the same argument leads to the same conclusion, i.e. that the solutions from the family $C_{\infty}$ do not belong
to $L_{2}(K)$. But if $\frac{n+4}{n}<\alpha<\alpha_{0}$, then an $\alpha$-basic function belongs to $L_{2}(K)$ and we do not know whether the solutions from the family $C_{\infty}$ belong to $L_{2}(K)$.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/32245020-4790-4b69-99f9-944eaca7e53e-40.jpg?height=672&width=1230&top_left_y=611&top_left_x=246}
\captionsetup{labelformat=empty}
\caption{Fig. 7.1. The phase picture for the case $\bar{a}<0, Q_{\alpha}<0$, here $s=1 / 4$.}
\end{figure}
(2) The family $C_{0}$. Each solution of the family $w(t) \in C_{0}$ goes to $w_{1}=(0,0)$ as $t \rightarrow+\infty$, nestling at the direction of the eigenvector $v_{+}$. Notice that all but one (denoted by $w_{s}$, see below) of the admissible solutions tending to $w_{1}$ belong to the family $C_{0}$. The solutions $w(t)$ and the corresponding solutions $u(\ell)$ have the following asymptotic behavior:
$$w(t) \sim e^{\lambda_{+} t}=e^{\left(\frac{\bar{b}}{2}+\sqrt{\frac{\overline{b^{2}}}{4}+\bar{a}}\right) t}, t \rightarrow \infty u(\ell) \sim \ell^{-\frac{2}{\alpha-1}-\left(\frac{\bar{b}}{2}+\sqrt{\frac{\bar{b}^{2}}{4}}+\bar{a}\right)}, \ell \rightarrow 0 .$$
To analyze the behavior of solutions from the family $C_{0}$, we use Lemma 3.6. We see that $u(\ell) \sim \ell^{q}$ with $q=-\frac{2}{\alpha-1}-\left(\frac{\bar{b}}{2}+\sqrt{\frac{\bar{b}^{2}}{4}+\bar{a}}\right)$.

Recall that $u(\ell) \in H_{2}^{k}(M)$ if and only if $k<\frac{n}{2}+q$. Since $\bar{b}=(n-2)-$ $\frac{4}{\alpha-1}$, we have $\frac{2}{\alpha-1}+\frac{\bar{b}}{2}=\frac{n-2}{2}$; therefore, in this case
$$\begin{gathered}
\frac{n}{2}+q=\frac{n}{2}-\frac{n-2}{2}-\sqrt{\frac{\bar{b}^{2}}{4}+\bar{a}}=1-\sqrt{\frac{\bar{b}^{2}}{4}+\bar{a}}=1-\frac{n-2}{2} \mu, \quad \text { where } \\
\mu=\sqrt{1+\frac{\Lambda}{(n-1)(n-2)}} .
\end{gathered}$$
As it is proved in the Appendix, such a solution never belongs to $H_{2}^{1}(M)$. It belongs to $L_{2}(M)$ only in the minus case (31).
(3) Two incoming separatrix trajectories of the saddle point $w_{2}$. For both these trajectories, $w_{\text {sep }}(t) \rightarrow w_{2}$. Thus, the corresponding solution $u_{\text {sep }}(\ell)$ is exactly an $\alpha$-basic function near $x^{*}$. If in this case $\alpha<\alpha_{0}<\frac{n+4}{n}$ (in the plus-case (30), see the Appendix), the solutions $u_{\text {sep }}(\ell)$ do not belong to $L_{2}(M)$ (recall that here $\alpha<\alpha_{0}$ since $\bar{a}<0$ ).
(4) The solution $w_{s}(t) \rightarrow w_{1}=(0,0)$, corresponding to the eigenvector $v_{-}$. This solution, obtained by a $C^{1}$-diffeomorphic twist of the corresponding solution of the linearization of (29) at $w_{1}$, has the asymptotic behavior $w_{s}(t) \sim e^{\lambda_{-} t}$. The corresponding solution $u_{s}(\ell) \sim l^{q}, q=-\frac{2}{\alpha-1}-\lambda_{-}$, where
$$q=-\frac{2}{\alpha-1}-\frac{\bar{b}}{2}+\sqrt{\frac{\bar{b}^{2}}{4}+\bar{a}}=-\frac{n-2}{2}+\sqrt{\frac{\bar{b}^{2}}{4}+\bar{a}},$$
see above. Therefore,
$$\frac{n}{2}+q=1+\sqrt{\frac{\bar{b}^{2}}{4}+\bar{a}}=1+\frac{n-2}{2} \mu .$$
As it is shown in the Appendix, the solution $u_{s}(t)$ always belongs to $H_{2}^{1}(M)$. Furthermore, $u_{s}(\ell) \in H_{2}^{2}(M)$ if and only if the plus case (30) condition is met.

Case 2: $\bar{a}<0, Q_{\alpha}>0$. In this case the phase picture is given in Fig. 7.2. Here we have one family $C_{0}$ of admissible solutions and a special solution $u_{s}(\ell)$. Solutions of the family $C_{0}$ tend to $w_{1}=(0,0)$ as $t \rightarrow+\infty$. Such solutions $w(t)$ asymptotically nestle in the direction of the eigenvector $v_{+}$.

The asymptotic behavior of $w(t)$ and of the corresponding solutions $u(\ell)$ is the following:
$$w(t) \sim e^{\lambda_{+} t}=e^{\left(\frac{\bar{b}}{2}+\sqrt{\frac{\bar{b}^{2}}{4}+\bar{a}}\right) t}, t \rightarrow \infty, \quad u(\ell) \sim \ell^{-\frac{2}{\alpha-1}-\left(\frac{\bar{b}}{2}+\sqrt{\frac{\bar{b}^{2}}{4}+\bar{a}}\right)}, \ell \rightarrow 0 .$$
The same argument as in Case 1 proves that solutions from the family $C_{0}$ belong to $L_{2}(M)$ only in the minus-case (31) and that none of these solutions belong to $H_{2}^{1}(M)$. Similar to Case 1, the solution $u_{s}(\ell)$ always belongs to $H_{2}^{1}(M)$ and belongs to $H_{2}^{2}(M)$ if and only if the plus-case condition (30)
is met.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/32245020-4790-4b69-99f9-944eaca7e53e-42.jpg?height=669&width=1225&top_left_y=498&top_left_x=247}
\captionsetup{labelformat=empty}
\caption{Fig. 7.2. The phase picture for the case $\bar{a}<0, Q_{\alpha}>0$, here $s=1 / 4$.}
\end{figure}

Case 3: $\bar{a}>0, Q_{\alpha}>0, \frac{\bar{b}^{2}}{4}-\bar{a}(\alpha-1)<0$. In this case the phase picture is given in Fig. 7.3.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/32245020-4790-4b69-99f9-944eaca7e53e-42.jpg?height=667&width=1239&top_left_y=1326&top_left_x=247}
\captionsetup{labelformat=empty}
\caption{Fig. 7.3. The phase picture for the case $\bar{a}>0, Q_{\alpha}>0$, $\frac{\bar{b}^{2}}{4}-\bar{a}(\alpha-1)<0$, here $s=1 / 4$.}
\end{figure}

Case $3^{\prime}: \bar{a}>0, Q_{\alpha}>0, \frac{\bar{b}^{2}}{4}-\bar{a}(\alpha-1)>0$. We have the following phase
given at Fig. 7.3'.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/32245020-4790-4b69-99f9-944eaca7e53e-43.jpg?height=671&width=1234&top_left_y=515&top_left_x=243}
\captionsetup{labelformat=empty}
\caption{Fig. 7.3'. The phase picture for the case $\bar{a}>0, Q_{\alpha}>0, \frac{\bar{b}^{2}}{4}-\bar{a}(\alpha-1)>0$.}
\end{figure}
We analyze the cases $3,3^{\prime}$ together since they have very similar classes of admissible solutions.

Here we have the class $C_{F}$ of Fowler solutions (see [8]): Here $w(t) \rightarrow w_{2}$ as $t \rightarrow+\infty$, and
$$u(\ell) \sim \ell^{-\frac{2}{\alpha-1}}, \quad \ell \rightarrow 0 .$$
Also we have a separatrix solution $w_{s}(t)$ that approaches $w_{1}=(0,0)$ as $t \rightarrow+\infty$. This solution asymptotically nestles at the eigendirection $v_{-}$. It has the following asymptotic:
$$w_{s}(t) \sim e^{\lambda-t}=e^{\left(\frac{\bar{b}}{2}-\sqrt{\frac{\bar{b}^{2}}{4}+\bar{a}}\right) t}, t \rightarrow+\infty, \quad u_{s}(\ell) \sim \ell^{-\frac{2}{\alpha-1}-\left(\frac{\bar{b}}{2}-\sqrt{\frac{\bar{b}^{2}}{4}+\bar{a}}\right)}, \ell \rightarrow 0 .$$

Remark. In fact, the solution $u_{s}(\ell)$ gives a minimum for the corresponding Yamabe functional. This asymptotic behavior refines the general result on the Yamabe minimizer for cylindrical manifolds for the particular "slice" $S^{p} \times S^{q}$, see [1].

The Fowler solutions in both cases 3 and $3^{\prime}$ do not belong to $H_{2}^{1}(M)$, by Proposition 3.7. Moreover, they even do not belong to $L_{2}(M)$ for $\alpha_{0}<\alpha \leq$ $\frac{n+4}{n}$ (the minus-case (31)); however, they belong to $L_{2}(M)$ for $\frac{n+4}{n}<\alpha$.

The separatrix solution $u_{s}(\ell)$ has the asymptotical behavior $\ell^{q}$ as $\ell \rightarrow$
$+\infty$, with $q=-\frac{2}{\alpha-1}-\left(\frac{\bar{b}}{2}-\sqrt{\frac{\bar{b}^{2}}{4}+\bar{a}}\right)$. Using $\frac{2}{\alpha-1}+\frac{\bar{b}}{2}=\frac{n-2}{2}$, we obtain
$$q=-\frac{n-2}{2}+\sqrt{\frac{\bar{b}^{2}}{4}+\bar{a}}=-\frac{n-2}{2}+\frac{n-2}{2} \mu .$$
Thus, $\frac{n}{2}+q=1+\frac{n-2}{2} \mu$. Similarly to the Case 1, solution $u_{s}(\ell)$ always belongs to $H_{2}^{1}(M)$ but belongs to $H_{2}^{2}(M)$ if and only if the plus-case condition (30) is met.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/32245020-4790-4b69-99f9-944eaca7e53e-44.jpg?height=672&width=1216&top_left_y=826&top_left_x=248}
\captionsetup{labelformat=empty}
\caption{Fig. 7.4. The phase picture for the case $\bar{a}>0, Q_{\alpha}<0$, here $s=3 / 4$.}
\end{figure}

Case 4: $\bar{a}>0, Q_{\alpha}<0$. Here the phase picture is given in Fig. 7.4. In this case we have the family $C_{\infty}$ of admissible solutions $w(t)$, such that $w(t) \rightarrow \infty$ as $t \rightarrow \infty$. The corresponding solution $u(\ell)$ goes to $\infty$ faster then the $\alpha$-basic function $\ell^{-\frac{2}{\alpha-1}}$ for a given $\alpha$. Thus, these solutions do not belong to $H_{2}^{1}(M)$.

Here, $\alpha>\alpha_{0}$, and in the plus case (30), or in the minus case (31) when $\alpha>\frac{n+4}{n}$, an $\alpha$-basic function belongs to $L_{2}(K)$. But, we do not know if solutions from $C_{\infty}$ belong to this space. On the other hand, in the minus-case (31), if $\alpha<\frac{n+4}{n}$, such solutions do not belong to $L_{2}(K)$.

In addition, we have the separatrix solution $w_{s}(t)$ that tends to $w_{1}=(0,0)$ as $t \rightarrow+\infty$. This solution asymptotically nestles in the direction of the eigenvector $v_{-}$. The asymptotic of $w_{s}(t)$ and $u_{s}(\ell)$ is the following:
$$w_{s}(t) \sim e^{\lambda_{-} t}=e^{\left(\frac{\bar{b}}{2}-\sqrt{\frac{\bar{b}^{2}}{4}+\bar{a}}\right) t}, t \rightarrow \infty, \quad u_{s}(\ell) \sim \ell^{-\frac{2}{\alpha-1}-\left(\frac{\bar{b}}{2}-\sqrt{\frac{\bar{b}^{2}}{4}+\bar{a}}\right)}, \ell \rightarrow 0 .$$

Thus, the separatrix solution $u_{s}(\ell)$ has asymptotic $\ell^{q}$ with
$$q=-\frac{2}{\alpha-1}-\left(\frac{\bar{b}}{2}-\sqrt{\frac{\bar{b}^{2}}{4}+\bar{a}}\right)=-\frac{n-2}{2}+\sqrt{\frac{\bar{b}^{2}}{4}+\bar{a}},$$
and $\frac{n}{2}+q=1+\frac{n-2}{2} \mu$. Similarly to the Case 1, solution $u_{s}(\ell)$ always belongs to $H_{2}^{1}(M)$ but belongs to $H_{2}^{2}(M)$ if and only if the plus-case condition (30) is met.

Now we consider the special cases that were previously left outside of the scope.

Case 5. $Q_{\alpha}=0$. In this case, we have a linear system with the matrix
$$A=\left(\begin{array}{ll}
0 & 1 \\
\bar{a} & \bar{b}
\end{array}\right) .$$
Thus, the solutions can be written out explicitly. Depending on the sign of $\bar{a}$, we have either a stable node (if $\bar{a}<0$, Case 5-, Fig. 7.5-) or a saddle point (if $\bar{a}>0$, Case 5+, Fig. 7.5+). Correspondingly, we have linear versions of cases 2 and 4. Conclusions that were made in these cases regarding asymptotics of admissible solutions are true in this case $\left(Q_{\alpha}=0\right)$ as well.

In the Case $5+$, where $\bar{a}>0$, the point $w_{1}$ is a saddle. A generic admissible solution from the family $C_{\infty}$ is growing faster than an $\alpha$-basic function. More specifically, we have $w(t) \sim e^{\lambda_{+} t}$ as $t \rightarrow+\infty$. Thus, the corresponding solution $u(\ell)$ has the asymptotic:
$$u(\ell) \sim \ell^{-\frac{2}{\alpha-1}-\lambda_{+}}, \quad \ell \rightarrow 0 .$$
We use Lemma 3.6: we have $q=-\frac{2}{\alpha-1}-\left(\frac{\bar{b}}{2}+\sqrt{\frac{\bar{b}^{2}}{4}+\bar{a}}\right)$. The same argument as before gives that $\frac{n}{2}+q=1-\sqrt{\frac{\bar{b}^{2}}{4}+\bar{a}}=1-\frac{2}{n-2} \mu$. Thus, this solution never belongs to $H_{2}^{1}(K)$, and it does belong to $L_{2}(K)$ if and only if the
minus-case condition (31) is met.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/32245020-4790-4b69-99f9-944eaca7e53e-46.jpg?height=673&width=1195&top_left_y=507&top_left_x=248}
\captionsetup{labelformat=empty}
\caption{Fig. 7.5+. The phase picture for the case $\bar{a}>0, Q_{\alpha}=0$, here $s=3 / 4$.}
\end{figure}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/32245020-4790-4b69-99f9-944eaca7e53e-46.jpg?height=674&width=1169&top_left_y=1256&top_left_x=249}
\captionsetup{labelformat=empty}
\caption{Fig. 7.5-. The phase picture for the case $\bar{a}<0, Q_{\alpha}=0$, here $s=1 / 4$.}
\end{figure}
We also have the stable separatrix solution $u_{s}(\ell)$, which has the asymptotic $\ell^{q}$ with
$$q=-\frac{2}{\alpha-1}-\left(\frac{\bar{b}}{2}-\sqrt{\frac{\bar{b}^{2}}{4}+\bar{a}}\right) .$$
Similarly to the above cases, we conclude that $u_{s}(\ell) \in H_{2}^{1}(M)$, and it also
belongs to $H_{2}^{2}(M)$ if and only if the plus-case condition (30) is met.
In the Case $5-$ (where $\bar{a}<0$ ) we have the linear version of the Case 2. Here, the generic (slow) admissible solutions from the family $C_{0}$, which are nestling in the eigendirection $v_{+}$, never belong to $H_{2}^{1}(M)$ and belong to $L_{2}(M)$ if and only if the minus-case condition (31) is met.

The fast-decreasing solution $u_{s}(t)=\ell^{-\frac{2}{\alpha-1}-\lambda_{-}}$, corresponding to the smaller eigenvalue, has the asymptotic $\sim \ell^{1+\sqrt{\frac{\bar{b}^{2}}{4}+\bar{a}}}=\ell^{1+\frac{2}{n-2} \mu}$. Thus, according to the discussion in the Appendix, it always belongs to $H_{2}^{1}(M)$ and belongs to $H_{2}^{2}(M)$ if and only if the plus-case condition (30) is met.

Case 6: $\bar{a}=0$. In this case, (when $\alpha=\alpha_{0}$, see Appendix) $w_{1}$ is the only singular point of the system (28). This point is degenerate: $\lambda_{-}=\bar{b}_{0}=$ $-(n-2) \mu, \lambda_{+}=0$. Depending on the sign of $Q_{\alpha}$ we have the cases 6+ or 6-.

Case 6+: $\left(Q_{\alpha}>0\right.$, a weak stable node). In this case the phase picture is the following:

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/32245020-4790-4b69-99f9-944eaca7e53e-47.jpg?height=670&width=1183&top_left_y=1292&top_left_x=268}
\captionsetup{labelformat=empty}
\caption{Fig. 7.6+. The phase picture for $\bar{a}=0, Q_{\alpha}>0$, here $s=1 / 2$.}
\end{figure}
This case is similar to Case 2. The difference is in the fact that $\lambda_{+}=0$. As a result, the solutions of the family $C_{0}$ tend to $w_{1}=(0,0)$ slowly and, similar to the Case 2, do not belong to $L_{2}(M)$.

The fast solution $w_{s}(t)$ corresponds to the second eigenvalue $\lambda_{-}=$
$\bar{b}$, where the corresponding eigenfunction $u_{s}(\ell)$ behaves asymptotically as $u_{s}(\ell) \sim l^{q}$, with $q=-\frac{2}{\alpha_{0}-1}-\bar{b}$. Thus, we have: $\frac{n}{2}+q=\frac{n}{2}-\frac{2}{\alpha_{0}-1}-\bar{b}=$ $1-\frac{\bar{b}}{2}=2-\frac{n}{2}+\frac{2}{\alpha_{0}-1}=1+\frac{n-2}{2} \mu$. Therefore, $u_{s}(\ell) \in H_{2}^{1}(M)$ and, in addition, it belongs to $H_{2}^{2}(M)$ if the plus-case condition (30) is met.

Case 6-: $\left(Q_{\alpha}<0\right.$, weak saddle $)$. In this case the phase picture is given at Fig. 7.6-. The Case 6- is similar to the Case 4. We have the family of solutions $C_{\infty}$ and a separatrix solution $w_{s}(t)$.

The family $C_{\infty}$ consists of solutions $u(\ell)$ which grow faster than the basic solutions $\ell^{-\frac{2}{\alpha_{0}-1}}$. Thus, these solutions do not belong to $L_{2}(M)$ if the value $\alpha_{0}$ (for which $\bar{a}=0$ ) is smaller then the critical value $\frac{n+4}{n}$ from Proposition 3.7, that is, in the minus-case (31). In the opposite case, we do not know if solutions from the family $C_{\infty}$ belong to $L_{2}(K)$ or not.

On the other hand, separatrix solution $u_{s}(\ell)$ has the asymptotic $\ell^{q}$ with $q=-\frac{2}{\alpha-1}-\bar{b}$. Similarly to the above consideration we conclude that separatrix solution $u_{s}(\ell) \in H_{2}^{1}(M)$ and it belongs to $H_{2}^{2}(K)$ if the plus-case condition (30) is met.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/32245020-4790-4b69-99f9-944eaca7e53e-48.jpg?height=671&width=1184&top_left_y=1343&top_left_x=268}
\captionsetup{labelformat=empty}
\caption{Fig. 7.6-. The phase picture for $\bar{a}=0, Q_{\alpha}<0$, here $s=1 / 2$.}
\end{figure}

Case 7. The critical: $\alpha=\alpha^{*}=\frac{n+2}{n-2}$. In this case $\alpha-1=\frac{4}{n-2}, s=1$. We have here $\bar{b}=0$, and $\bar{a}(1)=\bar{a}^{*}=\frac{(n-2)^{2}}{4}\left(1+\frac{\Lambda}{(n-2)(n-1)}\right)=\frac{(n-2)^{2}}{4} \mu^{2}$.

Therefore (see Appendix) $\bar{a}^{*}>0$. Our system takes the form
$$\left\{\begin{aligned}
x^{\prime} & =y \\
y^{\prime} & =\bar{a}^{*} x-Q_{\alpha^{*}} x^{\alpha^{*}} .
\end{aligned}\right.$$
We have the corresponding equation of the second order
$$w^{\prime \prime}-\bar{a}^{*} w+Q_{\alpha^{*}} w^{\alpha^{*}}=0 .$$
This equation has a first integral (a Hamiltonian function of system (32)):
$$I(x, y)=\frac{y^{2}}{2}-\frac{\bar{a}^{*} x^{2}}{2}+\frac{Q_{\alpha^{*}}}{\alpha^{*}+1} x^{\alpha^{*}+1}$$
For the singular point $w_{1}=(0,0)$ we have $\lambda_{ \pm}= \pm \sqrt{\bar{a}^{*}}$, thus $w_{1}$ is saddle point.

Case 7-: $Q_{\alpha^{*}}<0$. In this case $w_{1}$ is the only singular point. The phase picture is given at Fig. 7.7-.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/32245020-4790-4b69-99f9-944eaca7e53e-49.jpg?height=671&width=1106&top_left_y=1283&top_left_x=284}
\captionsetup{labelformat=empty}
\caption{Fig. 7.7-. The phase picture for the case $\alpha=\alpha^{*}, Q_{\alpha^{*}}<0$.}
\end{figure}

Here we have the family $C_{\infty}$ of admissible solutions and the incoming separatrix $w_{s}(t)$. All solutions of the family $C_{\infty}$ go to infinity as $t \rightarrow+\infty$. For such solutions $w(t) \rightarrow+\infty$ as $t \rightarrow+\infty$, and $u(\ell)$ goes to $+\infty$ faster than the basic function $\ell^{-\frac{2}{\alpha^{*}-1}}$ as $\ell \rightarrow 0$. Thus, none of the solutions $u(\ell) \in C_{\infty}$ belong to $H_{2}^{1}(M)$. Furthermore, since $\alpha^{*}>\frac{n+4}{4}$, an $\alpha^{*}$-basic function does
belong to $L_{2}(K)$, and in order to determine whether $u(\ell)$ belongs to $L_{2}(M)$, we have to study its asymptotic behavior in more detail.

The separatrix solution $w_{s}(t)$ that tends to $w_{1}=(0,0)$ as $t \rightarrow+\infty$. This solution asymptotically nestles in the direction of the eigenvector $v_{-}$. We have the asymptotic:
$$w_{s}(t) \sim e^{\lambda-t}=e^{-\sqrt{\bar{a}^{*}} t}, \quad t \rightarrow \infty, \quad u_{s}(\ell) \sim \ell^{-\frac{n-2}{2}+\sqrt{\bar{a}^{*}}} \quad \ell \rightarrow 0 .$$
For this solution $\frac{n}{2}+q=1+\frac{n-2}{2} \mu$. Thus, this solution always belongs to $H_{2}^{1}(M)$ and does belong to $H_{2}^{2}(M)$ if the plus-case condition (30) is fulfilled.

Case 7+: $Q_{\alpha^{*}}>0$. If $Q_{\alpha^{*}}>0$, we have the second singular point $w_{2}=$ $x_{2}=\left(\left(\frac{\bar{a}^{*}}{Q_{\alpha^{*}}}\right)^{\frac{n-2}{4}}, 0\right)$. The eigenvalues of the linearization at this point are
$$r_{ \pm}= \pm \sqrt{-\frac{4 \bar{a}^{*}}{n-2}} .$$
Thus, $w_{2}$ is a center, see Fig. 7.7+ for the phase picture.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/32245020-4790-4b69-99f9-944eaca7e53e-50.jpg?height=670&width=1190&top_left_y=1260&top_left_x=261}
\captionsetup{labelformat=empty}
\caption{Fig. 7.7+. The phase picture for the case $\alpha=\alpha^{*}, Q_{\alpha^{*}}>0$.}
\end{figure}
Thus, inside the homoclinic loop we have a family of periodic solutions. These solutions are known as Fowler or Delaunay solutions (see [15]). Notice that the value of the first integral $I$ on the separatrix loop is zero, and, at $w_{2}$,
$$I\left(w_{2}\right)=-\frac{Q_{\alpha^{*}}}{n}\left(\frac{\bar{a}^{*}}{Q_{\alpha^{*}}}\right)^{\frac{n}{2}}<0 .$$

Therefore, a Fowler solution is determined by the value of the integral $I$ in the interval $\left(I\left(w_{2}\right), 0\right)$, or by the minimal value $w_{\text {min }}$ of $w(t)=(x(t), y(t))$ along its trajectory. The integral $I(x, y)$ takes values in $\left[I\left(w_{2}\right), 0\right]$. Such a solution is also determined by the minimum value $x_{\text {min }}$ of $x(t), x_{\text {min }} \in$ $\left(0,\left(\frac{\bar{a}^{*}}{Q_{\alpha^{*}}}\right)^{\frac{n-2}{4}}\right)$. For such a trajectory $x_{\text {min }} \leq x(t) \leq x_{\text {max }}$ for all $t$. As a result, for the corresponding function $u(\ell)$ we have
$$x_{\min } \ell^{-\frac{n-2}{2}} \leq u(\ell) \leq x_{\max } \ell^{-\frac{n-2}{2}} .$$
Therefore, the Fowler solutions have the asymptotic $\ell^{-\frac{n-2}{2}}$ as $\ell \rightarrow 0$ and (see Proposition 3.7) do belong to $L_{2}(M)$, but not to $H_{2}^{1}(M)$.

In addition, we have the incoming separatrix solution $w_{s}(t)$ that tends to $w_{1}=(0,0)$ as $t \rightarrow+\infty$. This solution asymptotically nestles in the direction of the eigenvector $v_{-}$. We have the asymptotic
$$w_{s}(t) \sim e^{\lambda-t}=e^{-\sqrt{\bar{a}^{*}} t}, \quad t \rightarrow \infty \quad u_{s}(\ell) \sim \ell^{-\frac{n-2}{2}+\sqrt{\bar{a}^{*}}}, \quad \ell \rightarrow 0 .$$
The separatrix solution $u_{s}(\ell) \sim \ell^{q}$ with $q=-\frac{n-2}{2}+\sqrt{\bar{a}^{*}}=\frac{n-2}{2}(\mu-1)$. Thus, $\frac{n}{2}+q=1+\frac{n-2}{2} \mu$, and this solution always belongs to $H_{2}^{1}(M)$ and belongs to $H_{2}^{2}(M)$ if and only if the plus-case condition (30) is fulfilled.

We denote
$$\sigma=\frac{n-2}{2}(\mu-1), \quad \mu^{2}=\frac{2}{(n-1)(n-2)}\left[\frac{p(p-1)}{r_{p}^{2}}+\frac{q(q-1)}{r_{q}^{2}}\right] .$$
7.6. Perturbation near the point $w_{1}$. Now we consider the system (28) as a perturbation of its linearization near $w_{1}$. We will apply [10, Ch. 4, Theorems 5 and 9] or [13, Ch. X, Corollary 16.3] to those solutions, which tend to zero as $t \rightarrow \infty$. We claim that two following conditions for the nonlinear term $Q_{\alpha} x^{\alpha}$ (with $\alpha>1$ ) are satisfied.
(1) Indeed, the perturbation $f(t, x)$ must satisfy
$$\left.|f(t, x) \leq L| x\right|^{1+\rho}$$
for $t \geq t_{0},|x| \leq \delta$, where $L, \delta, \rho$ are positive constants. In our case, it is enough to take $\rho=\alpha-1$.
(2) The Lipschitz condition for $f(t, x)$ is satisfied since $x^{\alpha}$ is differentiable for $x \geq 0$ and its derivative $\alpha x^{\alpha-1}$ can be made arbitrarily small for $|x|<\delta$ with small enough $\delta$.

Thus [10, Ch. 4, Theorems 5 and 9] imply that there is one-to-one correspondence between those solutions of the system (28) that tend to zero as $t \rightarrow+\infty$ and of the corresponding solution of the linearization of (28). This shows that the norms $|w(t)|$ of corresponding solutions have the same asymptotical behavior as $t \rightarrow+\infty$. Using more refined results of (Hartman, Theorem 13.1 and Corollary 16.2) we may conclude the same about the asymptotic behavior of solutions $w(t)$ themselves, rather then their norms).

We have proved the following results.
Theorem 7.1 Let $M$ be a manifold with tame conical singularities as above, $n \geq 5, K \subset M$ be its conical part, and $1 \leq \alpha \leq \alpha^{*}$.
\begin{itemize}
\item[(1)] Then the equation (25) has unique radial solution $u_{s}(\ell)$ which belongs to the space $H_{2}^{1}(K)$. Moreover, $u_{s}(\ell) \sim \ell^{-\sigma}$, where $\sigma=\frac{n-2}{2}(\mu-1)$ (see (33)), and this solution is classical, i.e. belongs to the Sobolev space $H_{2}^{2}(M)$ if and only if the condition
$$\frac{p(p-1)}{r_{p}^{2}}+\frac{q(q-1)}{r_{q}^{2}}>\frac{2(n-1)}{n-2}$$
is fulfilled.
\item[(2)] If $\alpha \leq \frac{n+4}{4}<\alpha^{*}$, the equation (25) does not have other radial solutions in $L_{2}(K)$.
\item[(3)] For $Q_{\alpha}>0, \alpha>\frac{n+4}{4}$, there exists a family of solutions $C_{F}$ (Fowler solutions) which belong to the space $L_{2}(M)$, but not to $H_{2}^{1}(M)$.
\end{itemize}

We denote, as above, $Q_{\alpha}=\inf _{\varphi \in H_{2}^{1}(M), \varphi \neq 0} I_{\alpha}(\varphi)$.
Theorem 7.2 Let $M$ be a manifold with tame conical singularity as above.
\begin{itemize}
\item[(1)] If $1<\alpha<\alpha^{*}$, then a minimizing function $u_{\alpha}(\ell)$ exists, belongs to the space $H_{2}^{1}(M)$ and to the space $H_{2}^{2}(M)$ if the plus-case condition (30) is met. Asymptotically, $u_{\alpha}(\ell) \sim \ell^{-\sigma}$ near $x_{*}$, where $\sigma=\frac{n-2}{2}(\mu-1)$.
\item[(2)] If $\alpha=\alpha^{*}$, then a minimizing function $u_{\alpha}(\ell)$ (existing in $H_{2}^{1}(M)$ ) belongs to $H_{2}^{1}(M)$, and, if the plus-case condition (30) is met, to the space $H_{2}^{2}(M)$ and $u_{\alpha}(\ell) \sim \ell^{-\sigma}$ near $x_{*}$.
\end{itemize}

Remark. Notice that the asymptotic behavior of the solution $u_{s}(\ell) \in$ $H_{2}^{1}(M)$ is the same for all $\alpha, 1 \leqq \alpha \leqq \alpha^{*}$, including the linear case $\alpha=1$, compare Section 6.
7.7. Nonradial solutions. Theorem 7.2, describes the asymptotic behavior of those radial solutions of (24) which belong to the Sobolev space $H_{2}^{2}(M)$. It is important to determine whether general (non-radial) solutions have better or worse asymptotics then that of $u_{s}(\ell)$.

Similar questions have been studied extensively for the solutions of the Yamabe equation on $S^{n}$ with a finite number of singularities (in our terms, when $p=n, \alpha=\alpha^{*}$, see [15] for the most recent results and references to earlier works). It is shown in [15] that any nonradial solution asymptotically behaves as a shift (by $t$ ) of uniquely defined radial solutions of the same equation. There is clear evidence that the same holds in our case.

However, for our purposes we do not need such a result in full strength. We restrict our attention to the case when a solution tends to zero as $t \rightarrow+\infty$. Then a modification of the proof of [10, Ch. 4,Theorem 5] may be done, so that it will work in our case. That gives the following result:

Theorem 7.3 Let $u(\ell, \theta, \psi)$ be a solution of $(51)_{\alpha}$ such that
$$\|u\|_{L_{2}\left(S^{p} \times S^{q}\right)}(\ell) \rightarrow 0$$
as $\ell \rightarrow 0$. Then there exists a radial solution $u_{0}(\ell)$ of (24) with the same property such that
$$\left\|u(\ell, \theta, \psi)-u_{0}(\ell)\right\|=o\left(\left\|u_{0}(\ell)\right\|\right) \quad \text { as } \ell \rightarrow 0 .$$
As a result, the nonradial solutions of (24) that tend to zero, approaching the singular point $x_{*}$ have, for all $\alpha>1$, the same asymptotic behavior as corresponding radial solutions (which also approach zero).

Recall that the original metric $g$ on the cone is given by $g_{K}=d \ell^{2}+$ $\frac{r_{p}^{2} \ell^{2}}{2} d^{2} \theta+\frac{r_{q}^{2} \ell^{2}}{2} d^{2} \psi$. According to [1], there exists a Yamabe metric $\check{g}$ on $M$.

Corollary 7.4 Let $(M, g)$ be a manifold with tame conical singularity as above, and let $\check{g} \in[g]$ be a Yamabe metric on $M$. Then
$$\check{g} \sim \ell^{-\sigma}\left(d \ell^{2}+\frac{r_{p}^{2} \ell^{2}}{2} d^{2} \theta+\frac{r_{q}^{2} \ell^{2}}{2} d^{2}\right)$$
near the singular point $x_{*}$.

\section*{8 Appendix}

Here we collect some necessary computations, most of which are very simple.
8.1. Function $\Lambda=\Lambda(p)$. Recall that in the appropriate coordinates the scalar curvature on the cone $C\left(S^{p} \times S^{q}\right)$ is given as
$$R_{g_{K}}(\theta, \psi, \ell)=\frac{\Lambda}{\ell^{2}}, \quad \text { with } \quad \Lambda=p(p-1) \frac{2-r_{p}^{2}}{r_{p}^{2}}+q(q-1) \frac{2-r_{q}^{2}}{r_{q}^{2}}-2 p q .$$
We let $n$ be fixed and study $\Lambda$ as function of $p$ only, $\Lambda=\Lambda(p)$.
Substituting $q=n-p-1$, we transform $\Lambda$ to the expression
$$\begin{aligned}
\Lambda(p)= & -(n-1)(n-2)+2\left[\frac{p(p-1)}{r_{p}^{2}}+\frac{q(q-1)}{r_{q}^{2}}\right] \\
= & p(p-1) \frac{2-r_{p}^{2}}{r_{p}^{2}}+q(q-1) \frac{2-r_{q}^{2}}{r_{q}^{2}}-2 p q \\
= & 2 p^{2}\left(r_{p}^{-2}+r_{q}^{-2}\right)-2 p\left[\left(r_{p}^{-2}+r_{q}^{-2}\right)+(n-2) \frac{2}{r_{q}^{2}}\right] \\
& \quad+(n-1)(n-2)\left(\frac{2}{r_{q}^{2}}-1\right) .
\end{aligned}$$
To get the first equality we split $\frac{2-r_{p}^{2}}{r_{p}^{2}}=\frac{2}{r_{p}^{2}}-1$ and use the fact that $p(p-1)+q(q-1)-2 p q=(n-1)(n-2)$.
8.2. Minimal value of $\Lambda(p)$. To find the minimum of function $\Lambda(p)$ for $1<p<n-1$ we calculate
$$\frac{d \Lambda}{d p}=4 p\left(r_{p}^{-2}+r_{q}^{-2}\right)-2\left[\left(r_{p}^{-2}+r_{q}^{-2}\right)+(n-2) \frac{2}{r_{q}^{2}}\right],$$
and find
$$p_{\min }=\frac{\left(r_{p}^{-2}+r_{q}^{-2}\right)+(n-2) \frac{2}{r+q^{2}}}{2\left(r_{p}^{-2}+r_{q}^{-2}\right)}=\frac{1}{2}+\frac{n-2}{1+\frac{r_{q}^{2}}{r_{p}^{2}}} .$$
Correspondingly, $q$ takes the minimal value
$$q_{\min }=\frac{1}{2}+\frac{n-2}{1+\frac{r_{p}^{2}}{r_{r}^{2}}} .$$

Notice that for all possible values of $r_{p}>0, r_{q}>0$, we have
$$\frac{1}{2}<p_{\min }<n-\frac{3}{2} .$$
For the value of $\Lambda\left(p_{\text {min }}\right)$ we have
$$\begin{aligned}
\Lambda\left(p_{\min }\right)=-(n-1)(n-2) & +\frac{2}{r_{p}^{2}}\left(\frac{1}{2}+\frac{n-2}{1+\frac{r_{q}^{2}}{r_{p}^{2}}}\right)\left(\frac{-1}{2}+\frac{n-2}{1+\frac{r_{q}^{2}}{r_{p}^{2}}}\right) \\
& +\frac{2}{r_{q}^{2}}\left(\frac{1}{2}+\frac{n-2}{1+\frac{r_{p}^{2}}{r_{q}^{2}}}\right)\left(\frac{-1}{2}+\frac{n-2}{1+\frac{r_{p}^{2}}{r_{q}^{2}}}\right) \\
= & -(n-1)(n-2)-\frac{1}{2}\left(r_{p}^{-2}+r_{q}^{-2}\right)+\frac{2(n-2)^{2}}{r_{p}^{2}+r_{q}^{2}} .
\end{aligned}$$
In Section 7.5 we use the parameter $\mu^{2}$. We have:
$$\begin{aligned}
\mu^{2} & =1+\frac{\Lambda}{(n-1)(n-2)}= \\
& =1+\frac{p(p-1) \frac{2-r_{p}^{2}}{r_{p}^{2}}+q(q-1) \frac{2-r_{q}^{2}}{r_{q}^{2}}-2 p q}{(n-1)(n-2)}= \\
& =\frac{p(p-1) \frac{2}{r_{p}^{2}}+q(q-1) \frac{2}{r_{q}^{2}}}{(n-1)(n-2)}>0
\end{aligned}$$
if $p, q>0$. Here we have used $p(p-1)+q(q-1)+2 p q=(n-1)(n-2)$.
The maximal value is achieved at the end point of the interval $[3, n-3]$ of the admissible values of $p$. We have for $p=1$,
$$\begin{aligned}
\Lambda(1) & =-(n-1)(n-2)+(n-2)(n-3) \frac{2}{r_{q}^{2}}, \\
\Lambda(n-2) & =-(n-1)(n-2)+(n-2)(n-3) \frac{2}{r_{p}^{2}} .
\end{aligned}$$
Correspondingly, maximal value of $\Lambda(p)$ is achieved at one of these ends.
8.2. Parameters $\bar{a}, \bar{b}$ in (28). In order to analyze the "phase portraits" of the system (28) for different values of $Q_{\alpha}$ and $\Lambda$, we need particular information on the parameters $\bar{a}, \bar{b}$. Introduce the parameter $s=\frac{(\alpha-1)(n-2)}{4}$. Then it is easy to see that $0<s \leq 1$ since $1<\alpha \leq \alpha^{*}=\frac{n+2}{n-2}$.

Claim 8.1 For $n \geq 3, \bar{b}<0$.
Indeed, for $n \geq 3$, we have
$$\bar{b}=(n-2)-\frac{4}{\alpha-1}=(n-2)\left(1-\frac{4}{(\alpha-1)(n-2)}\right)=-\frac{(n-2)(s-1)}{s}<0 .$$
Now we study dependence of $\bar{a}$ on $s$ and $\Lambda$. We have
$$\begin{aligned}
\bar{a} & =\frac{(n-2)}{4(n-1)} \Lambda+\frac{2(n-2)}{\alpha-1}-\frac{4}{(\alpha-1)^{2}} \\
& =\frac{(n-2)}{4} \cdot \frac{\Lambda}{n-1}+\frac{4(n-2)^{2}}{2(\alpha-1)(n-2)}-\frac{4 \cdot 4(n-2)^{2}}{4(\alpha-1)^{2}(n-2)^{2}} \\
& =\frac{(n-2)}{4} \cdot \frac{\Lambda}{n-1}+\frac{(n-2)^{2}}{2 s}-\frac{(n-2)^{2}}{4 s^{2}} \\
& =\frac{(n-2)^{2}}{4}\left[\frac{\Lambda}{(n-1)(n-2)}+\frac{2}{s}-\frac{1}{s^{2}}\right] .
\end{aligned}$$
To analyze the equilibrium point $(0,0)$, we need to know the sign of expression $\frac{\bar{b}^{2}}{4}+\bar{a}$. We have (using expressions for $\bar{b}$ an $\bar{a}$ obtained above):
$$\begin{aligned}
\frac{\bar{b}^{2}}{4}+\bar{a} & =\frac{(n-2)^{2}(1-s)^{2}}{4 s^{2}}+\frac{(n-2)^{2}}{4}\left[\frac{\Lambda}{(n-1)(n-2)}+\frac{2}{s}-\frac{1}{s^{2}}\right] \\
& =\frac{(n-2)^{2}}{4}\left[1+\frac{\Lambda}{(n-1)(n-2)}\right]=\frac{(n-2)^{2}}{4} \mu^{2} \geq 0 .
\end{aligned}$$
Thus, we have that $\bar{a}(s) \rightarrow-\infty$ as $s \rightarrow 0$, and
$$\bar{a}(1)=\frac{(n-2)^{2}}{4}\left[\frac{\Lambda}{(n-1)(n-2)}+1\right]=\frac{(n-2)^{2}}{4} \mu^{2}>0$$
for all $\Lambda$. Also, we have
$$\frac{d \bar{a}}{d s}=\frac{(n-2)^{2}}{4}\left[-\frac{2}{s^{2}}+\frac{2}{s^{3}}\right]=\frac{(n-2)^{2}}{2 s^{3}}[1-s]$$
which is positive for all $s<1$, and zero for $s=1$.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/32245020-4790-4b69-99f9-944eaca7e53e-57.jpg?height=505&width=394&top_left_y=506&top_left_x=323}
\captionsetup{labelformat=empty}
\caption{Fig. 8.1.}
\end{figure}

Thus a graph of the function $\bar{a}(s)$ has a form given at Fig. 8.1. The point $s_{0}$ (when $\bar{a}\left(s_{0}\right)=0$ is a root of the equation
$$\frac{\Lambda}{(n-1)(n-2)} s^{2}+2 s-1=0 .$$
One has the following positive root:
$$s_{0}=\frac{1}{1+\sqrt{1+\frac{\Lambda}{(n-1)(n-2)}}}=\frac{1}{1+\mu}$$
for all $\Lambda$.
In terms of the parameter $\alpha, \bar{a}$ changes sign from negative to positive if $\alpha=\alpha_{0}$, with
$$\alpha_{0}=1+\frac{4}{(n-2)\left(1+\sqrt{1+\frac{\Lambda}{(n-1)(n-2)}}\right)}=1+\frac{4}{(n-2)(1+\mu)} .$$

Claim 8.2 The parameter $\bar{a}<0$ if $\alpha \in\left(1, \alpha_{0}\right), \bar{a}>0$ if $\alpha \in\left(\alpha_{0}, \alpha^{*}\right)$, and $\bar{a}=0$ if $\alpha=\alpha_{0}$, where $\alpha_{0}$ is given by (34).

For the expression $\frac{\bar{b}^{2}}{4}-\bar{a}(\alpha-1)$ we get
$$\begin{aligned}
& \frac{\bar{b}^{2}}{4}-\bar{a}(\alpha-1)=\frac{(n-2)^{2}(s-1)^{2}}{4 s^{2}}-\frac{4 s}{(n-2)} \frac{(n-2)^{2}}{4}\left[\frac{\Lambda}{(n-1)(n-2)}+\frac{2}{s}-\frac{1}{s^{2}}\right] \\
& =\left[\frac{(n-2)^{2}}{4}-2(n-2)\right]+\frac{(n-2)^{2}}{4} \frac{1}{s^{2}}+\left[(n-2)-\frac{(n-2)^{2}}{2}\right] \frac{1}{s}-(n-2)\left(\mu^{2}-1\right) s .
\end{aligned}$$
As $s \rightarrow 0$, the leading term is the first one, and the value of the function goes to $+\infty$. On the other hand, at $s=1$, the value of this function is equal to $-(n-2) \mu^{2}<0$. Thus, this expression takes both negative and positive values.

It was shown, in Lemma 3.6, that a function with the $\alpha$-basic asymptotic behavior at $x_{*}$ belongs to $L_{2}(M)$ iff $\frac{n+4}{n}<\alpha$. It is instructive to compare this condition with the condition on the $\operatorname{sign}(\bar{a})$.

The condition $\frac{n+4}{n}>\alpha_{0}$ is satisfied if and only if $\frac{n-2}{n}>\frac{1}{1+\mu}$, i. e. iff
$$\mu>\frac{2}{n-2} .$$
Taking the square of this inequality and using the expression for $\mu$ we see that this condition is equivalent to
$$\Lambda>(n-1)(n-2)\left[\frac{4}{(n-2)^{2}-1}\right]=-\frac{n(n-1)(n-4)}{n-2} .$$
Now we analyze the necessary and sufficient condition from Proposition 3.7 when a solution $u$ belongs to the Sobolev space $H_{2}^{k}$. The condition is
$$k<1 \pm \sqrt{\frac{\bar{b}^{2}}{4}+\bar{a}}=1 \pm \frac{n-2}{2} \mu .$$
Here we reformulate this condition in terms of $p, P, q, Q$. Consider first the minus-solutions, for which the condition takes the form
$$k<1-\frac{n-2}{2} \mu .$$
Since $\mu>0$, such solution can not belong to $H_{2}^{1}$. On the other hand, it belongs to $L_{2}$ if and only if $\frac{n-2}{2} \mu<1$, or when $\mu<\frac{2}{n-2}$. Substituting this expression for $\mu$, we get the result

Claim 8.3 The solution $u$ belongs to $L_{2}$ iff
$$\frac{p(p-1)}{r_{p}^{2}}+\frac{q(q-1)}{r_{q}^{2}}<\frac{2(n-1)}{n-2} .$$

Example: For $r_{p}=r_{q}=1$ this condition takes the form $(n-1-p)^{2}<$ $2(n-1)$, or $p<n-1-\sqrt{2(n-1)}$.
Consider now plus-solutions where the condition is $k<1+\frac{n-2}{2} \mu$. It is clear $(\mu>0)$ that the solution $u$ always belongs to $H_{2}^{1}$. This solution belongs to $H_{2}^{2}$ (i.e. is the classical solution) iff $\mu<\frac{2}{n-2}$, or, substituting the expression for $\mu$, when
$$\frac{p(p-1)}{r_{p}^{2}}+\frac{q(q-1)}{r_{p}^{2}}>\frac{2(n-1)}{n-2} .$$

Lemma 8.4 If $\bar{a}<0$, a function with the $\alpha$-basic asymptotic behavior at $x_{*}$ does not belong to $L_{2}(M)$.

\section*{References}
\begin{itemize}
\item[] [1] K. Akutagawa, B. Botvinnik, Yamabe metrics on cylindrical manifolds, to appear in GAFA, a preliminary version is availble at math.DG/0107164.
\item[] [2] T. Aubin, Équations différentielles non linéaires et problème de Yamabe concernant la courbure scalaire, J. Math. Pures Appl. (9) 55 (1976), 269-296.
\item[] [3] T. Aubin, Some nonlinear problems in Riemannian geometry. Springer Monographs in Mathematics. Springer-Verlag, Berlin, 1998. xviii+395 pp.
\item[] [4] T. Aubin, Le problème de Yamabe concernant la courbure scalaire. (French) C. R. Acad. Sci. Paris Sér. A-B 280 (1975), Aii, A721-A724.
\item[] [5] A. Besse, Einstein manifolds, Springer, Berlin, 1987.
\item[] [6] T. Branson, B. Örsted, Conformal geometry and global invariants. Differential Geom. Appl. 1 (1991), no. 3, 279-308.
\item[] [7] Y. Egorov, V. Kondratiev, On spectral theory of elliptic operators. (English. English summary) Operator Theory: Advances and Applications, 89. Birkhäuser Verlag, Basel, 1996. x+328 pp.
\item[] [8] A. Erdélyi, W.M. Wilhelm; F. Oberhettinger, F. Tricomi, Higher transcendental functions. Vols. I, II. Based, in part, on notes left by Harry Bateman. McGraw-Hill Book Company, Inc.,
\item[] [9] B. Botvinnik, J. Rosenberg, The Yamabe invariant for non-simply connected manifolds, math.DG/0104186.
\item[] [10] W. A. Coppel, Stability and asymptotic behavior of differential equations. D. C. Heath and Co., Boston, Mass. 1965.
\item[] [11] P. Gilkey, Invariance theory, the heat equation, and the Atiyah-Singer index theorem. Second edition. Studies in Advanced Mathematics. CRC Press, Boca Raton, FL, 1995. x+516 pp.
\item[] [12] G. Hardy, J. Littlewood, Pólya, G. Inequalities. 2d ed. Cambridge University Press, 1952. xii+324 pp.
\item[] [13] P. Hartman, Ordinary differential equations. Reprint of the second edition. Birkhuser, Boston, Mass., 1982.
\item[] [14] O. Kobayashi, Scalar curvature of a metric with unit volume. Math. Ann. 279 (1987), no. 2, 253-265.
\end{itemize}
\begin{itemize}
\item[] [15] N. Korevaar, R. Mazzeo, F. Pacard, R. Schoen, Refined asymptotics for constant scalar curvature metrics with isolated singularities, Invent. Math. 135 (1999) 233-272.
\item[] [16] V. Kozlov, V. Maz'ya, J. Rossmann, Elliptic boundary value problems in domains with point singularities. Mathematical Surveys and Monographs, 52. American Mathematical Society, Providence, RI, 1997. x+414 pp.
\item[] [17] M. Lesch, Operators of Fuchs type, conical singularities, and asymptotic methods. Teubner-Texte zur Mathematik [Teubner Texts in Mathematics], 136. B. G. Teubner Verlagsgesellschaft mbH, Stuttgart, 1997. 190 pp.
\item[] [18] V. Maz'ya, S. Nasarow, B. Plamenewski, Asymptotische Theorie elliptischer Randwertaufgaben in singulär gestörten Gebieten. I. (German) [Asymptotic theory of elliptic boundary value problems in singularly perturbed domains. I.] Störungen isolierter Randsingularitäten. [Perturbations of isolated boundary singularities] Mathematische Lehrbücher und Monographien, II. Abteilung: Mathematische Monographien [Mathematical Textbooks and Monographs, Part II: Mathematical Monographs], 82. Akademie-Verlag, Berlin, 1991. 432 pp.
\item[] [19] R. Mazzeo, F. Pacard, Constant scalar curvature metrics with isolated singularities, Duke Math. J. 99 (1999), 353-418.
\item[] [20] R. Mazzeo, D. Pollack, K. Uhlenbeck, Connected sum construction for constant scalar curvature metrics, Topol. Methods Nonlinear Anal. 6 (1995), 207-233.
\item[] [21] S. Mizohata, The theory of partial differential equations. Translated from the Japanese by Katsumi Miyahara. Cambridge University Press, New York, 1973. xii+490 pp.
\item[] [22] T. Parker, S. Rosenberg, Invariants of conformal Laplacians. J. Differential Geom. 25 (1987), no. 2, 199-222.
\item[] [23] J. Petean, G. Yun, Surgery and the Yamabe invariant. Geom. Funct. Anal. 9 (1999), no. 6, 1189-1199.
\item[] [24] J. Petean, Computations of the Yamabe invariant. Math. Res. Lett. 5 (1998), no. 6, 703-709.
\item[] [25] P. Petersen, Riemannian geometry. Graduate Texts in Mathematics, 171. Springer-Verlag, New York, 1998. xvi+432 pp.
\item[] [26] R. Schoen, Conformal deformation of a Riemannian metric to constant scalar curvature. J. Differential Geom. 20 (1984), no. 2, 479-495.
\end{itemize}
\begin{itemize}
\item[] [27] R. Schoen, Variational theory for the total scalar curvature functional for Riemannian metrics and related topics. Topics in calculus of variations (Montecatini Terme, 1987), 120-154, Lecture Notes in Math., 1365, Springer, Berlin-New York, 1989.
\item[] [28] R. Schoen, S. T. Yau, On the structure of manifolds with positive scalar curvature. Manuscripta Math. 28 (1979), no. 1-3, 159-183.
\item[] [29] H. Triebel, Interpolation theory, function spaces, differential operators. North-Holland Mathematical Library, 18. North-Holland Publishing Co., Amsterdam-New York, 1978. 528 pp.
\item[] [30] N. Trudinger, Remarks concerning the conformal deformation of Riemannian structures on compact manifolds, Ann. Scuola Norm. Sup. Pisa (3) 22 (1968), 265-274.
\item[] [31] H. Yamabe, On a deformation of Riemannian structures on compact manifolds, Osaka Math. J. 12 (1960), 21-37.
\item[] [32] K. Yosida, Functional analysis. Sixth edition. Grundlehren der Mathematischen Wissenschaften [Fundamental Principles of Mathematical Sciences], 123. Springer-Verlag, Berlin-New York, 1980.
\end{itemize}

Boris Botvinnik, University of Oregon, Eugene
e-mail: botvinn@math.uoregon.edu

Serge Preston, Portland State University,
serge@mth.pdx.edu