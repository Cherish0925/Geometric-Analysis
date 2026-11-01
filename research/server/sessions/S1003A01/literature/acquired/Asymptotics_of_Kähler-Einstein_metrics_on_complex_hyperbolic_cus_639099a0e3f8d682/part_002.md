---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Asymptotics of Kähler-Einstein metrics on complex hyperbolic cusps]

By construction, $\psi$ is a formal power series solution to the complex Monge-Ampère equation (3.1). Equivalently, by (3.31)-(3.32) and (3.36), $\psi$ formally solves the equation
$$x^{2} \psi^{\prime \prime}+(n+1) x \psi^{\prime}-(n+1) \psi=-(n+1)\left[(n-1) \mathbf{q}\left(x \psi^{\prime}\right)+\mathbf{q}\left(x(x \psi)^{\prime \prime}\right)\right],$$
where $\mathbf{q}(t)$ as in (3.35) is a convergent power series in $t$ without constant or linear terms. Any formal solution $\psi(x)=C_{1} x+C_{2} x^{2}+\cdots$ to (3.39) is uniquely determined by its leading coefficient $C_{1}$. Indeed, comparing terms of order $x^{k}$ in (3.39) yields a coefficient $(k-1)(k+n+1) C_{k}$ on the left side and some polynomial in $C_{1}, \ldots, C_{k-1}$ on the right. For $k=1$ this is a tautology, and for $k \geqslant 2$ we can solve this equation uniquely for $C_{k}$ in terms of $C_{1}, \ldots, C_{k-1}$. However, instead of actually solving this system of equations, it is simpler to observe that if $C_{1}=-(n+1) c$, then the function $-(n+1) \log (1+c x)$ has the right leading term and solves (3.39), so that $\psi(x)=-(n+1) \log (1+c x)$.

Theorem 3.1 has been proved.

\section*{4. Improvement of the remainder}

In this section, we complete the proof of the Main Theorem by improving the remainder $O\left(x^{\infty}\right)$ of Theorem 3.1 to the decay rate of the next generation of solutions of the homogeneous linearized PDE. This is done using a continuity argument. For this we first construct a right inverse to the model linear operator, which leads to a useful representation formula (Proposition 4.2). As in Section 3, the proof of this uses ODE arguments, although unlike in Section 3 we now need to work globally on the crosssection and consider the spectrum of the Laplacian (but it suffices to use $S^{1}$-invariant eigenfunctions). Using this formula, we then carry out the continuity argument in Proposition 4.4.
4.1. A representation formula. Assume the same setup as in the Main Theorem. By Theorem 3.1, there exists a $c \in \mathbb{R}$ such that if we define $\psi(x):=-(n+1) \log (1+c x)$, then the function $u^{*}:=u-\psi$ satisfies $u^{*}=O\left(x^{\infty}\right)$ along with all of its $\omega_{h}$-derivatives. Recall that we had originally defined $\psi$ to be the unique formal power series solution to $\left(\omega_{h}+i \partial \bar{\partial} \psi\right)^{n}=e^{\psi} \omega_{h}^{n}$ whose leading coefficient agrees with the Green's function coefficient of an asymptotic expansion of $u$. Using $\omega_{h}^{*}:=\omega_{h}+i \partial \bar{\partial} \psi$ as a reference metric instead of $\omega_{h}$, we can therefore rewrite our equation as
$$\left(\omega_{h}^{*}+i \partial \bar{\partial} u^{*}\right)^{n}=e^{u^{*}}\left(\omega_{h}^{*}\right)^{n} .$$
A crucial observation at this point is that $\omega_{h}^{*}=\omega_{h^{*}}$ for $h^{*}=e^{-c} h$. The radial coordinate associated with this new Hermitian metric is $x^{*}=\left(x^{-1}+c\right)^{-1}$. Passing from $\omega_{h}, x$ to $\omega_{h^{*}}, x^{*}$ makes no difference to the statement of the Main Theorem. Thus, we can assume without loss that $c=0$. In fact:

Reduction 4.1. To prove the Main Theorem, it is enough to prove that
$$\text { if }\left(\omega_{h}+i \partial \bar{\partial} u\right)^{n}=e^{u} \omega_{h}^{n} \text { and }|u|=O\left(x^{\infty}\right), \text { then }|u|=O\left(x^{-\frac{n}{2}+\frac{1}{4}} e^{-\frac{2 \sqrt{\lambda_{1}}}{\sqrt{x}}}\right) .$$

The desired derivative decay follows from standard elliptic regularity applied on the universal covers of $\omega_{h}$-geodesic balls of radius $\varepsilon \sqrt{t}$ centered at points of height $x=t$ for some small but fixed $\varepsilon>0$. The point is that $\sqrt{t}$ is the biggest order of magnitude such that functions of the form $e^{-\delta / \sqrt{x}}$ vary by bounded factors over such balls. At the same time, these balls have fundamental group $\mathbb{Z}$, and balls of radius $\varepsilon \sqrt{t}$ in their universal covers satisfy uniform geometry bounds at their own scale.

We now go back to the ODE version (3.31) of the Monge-Ampère equation, i.e.,
$$\begin{array}{r}
x^{2} u_{x x}+(n+1) x u_{x}-(n+1) u=G, \\
G=x^{-1} \varphi^{\bar{\beta} \alpha} u_{\alpha \bar{\beta}}-(2 x)^{-2} u_{\theta \theta}-(n+1)\left(F+Q_{h}(u)\right),
\end{array}$$
where $F$ is smooth in $x_{\alpha}, y_{\alpha}$ and linear homogeneous in $x^{-1} u_{\theta \alpha}, x^{-1} u_{\theta \bar{\alpha}}, x^{-1} u_{\theta \theta}$ and where $Q_{h}(u)$ is a power series in $i \partial \bar{\partial} u$ without constant or linear terms. We move the Laplacian in the $D$-directions out of the inhomogeneity, $G$, and average with respect to $\theta \in[0,2 \pi]$. This yields
$$\begin{aligned}
& x^{2} \stackrel{\circ}{u}_{x x}+(n+1) x \stackrel{\circ}{u}_{x}-(n+1) \stackrel{\circ}{u}-x^{-1} \varphi^{\bar{\beta} \alpha} \stackrel{\circ}{u}_{\alpha \bar{\beta}}=\stackrel{\circ}{G}, \\
& \stackrel{\circ}{u}:=\frac{1}{2 \pi} \int_{0}^{2 \pi} u d \theta, \stackrel{\circ}{G}:=-(n+1) \frac{1}{2 \pi} \int_{0}^{2 \pi} Q_{h}(u) d \theta .
\end{aligned}$$
Crucially, $\stackrel{\circ}{u}$ and $\stackrel{\circ}{G}$ are globally well-defined on $(0, \delta] \times D$ for some $\delta>0$, not just chart by chart. This is because the operator $Q_{h}$ is global and, for all global functions $v$, the integral $\int_{0}^{2 \pi} v d \theta$ in each chart can be identified with the $S^{1}$-invariant global function $\int_{S^{1}} g^{*} v d g$, where $\left(g^{*} v\right)(p)=v(g \cdot p)$ (using the given global $S^{1}$-action) and where $d g$ denotes the standard measure on $S^{1}$. Another key point is that $|u-i|=O\left(e^{-\varepsilon / x}\right)$ by Lemma 3.5, so $u$ satisfies the estimates in (4.2) if and only if $\stackrel{\circ}{u}$ does.

Let $\lambda_{\ell}, \varphi_{\ell}$ denote the eigenvalues and $L^{2}$-orthonormalized eigenfunctions of the operator $\varphi^{\bar{\beta} \alpha} \partial_{\alpha} \partial_{\bar{\beta}}$ on $D$, where $\ell \in \mathbb{N}_{0}$ and $0=\lambda_{0}<\lambda_{1} \leqslant \lambda_{2} \leqslant \ldots$ We will use the Fourier decompositions
$$\stackrel{\circ}{u}=\sum_{\ell=0}^{\infty} \dot{u}_{\ell}(x) \varphi_{\ell}, \quad \stackrel{\circ}{G}=\sum_{\ell=0}^{\infty} \dot{G}_{\ell}(x) \varphi_{\ell},$$
which converge in $C_{\text {loc }}^{\infty}$ as usual. Then (4.4) decomposes into the ODEs
$$x^{2} \dot{u}_{\ell}^{\prime \prime}(x)+(n+1) x \dot{u}_{\ell}^{\prime}(x)-(n+1) \dot{u}_{\ell}(x)-\lambda_{\ell} x^{-1} \dot{u}_{\ell}(x)=\dot{G}_{\ell}(x) .$$
We already treated the case $\ell=0$ in Section 3, although in Section 3 we were able to work pointwise on the cross-section with no need to integrate in any direction.

Denote $\alpha=n+2$. For all $\ell \in \mathbb{N}_{\geqslant 1}$ denote
$$H_{1, \ell}(x)=\frac{1}{x^{n / 2}} I_{\alpha}\left(2 \frac{\sqrt{\lambda_{\ell}}}{\sqrt{x}}\right), H_{2, \ell}(x)=\frac{1}{x^{n / 2}} K_{\alpha}\left(2 \frac{\sqrt{\lambda_{\ell}}}{\sqrt{x}}\right),$$
where $I_{\alpha}(s)$ is the modified Bessel function of the first kind and $K_{\alpha}(s)$ is the modified Bessel function of the second kind. It is known that as $s \rightarrow \infty$ there exist asymptotic expansions
$$\begin{aligned}
I_{\alpha}(s) & =\frac{e^{s}}{\sqrt{2 \pi s}}\left(1-\frac{4 \alpha^{2}-1}{8 s}+\frac{\left(4 \alpha^{2}-1\right)\left(4 \alpha^{2}-9\right)}{2!(8 s)^{2}}-\frac{\left(4 \alpha^{2}-1\right)\left(4 \alpha^{2}-9\right)\left(4 \alpha^{2}-25\right)}{3!(8 s)^{3}}+\cdots\right), \\
K_{\alpha}(s) & =\sqrt{\frac{\pi}{2 s}} e^{-s}\left(1+\frac{4 \alpha^{2}-1}{8 s}+\frac{\left(4 \alpha^{2}-1\right)\left(4 \alpha^{2}-9\right)}{2!(8 s)^{2}}+\frac{\left(4 \alpha^{2}-1\right)\left(4 \alpha^{2}-9\right)\left(4 \alpha^{2}-25\right)}{3!(8 s)^{3}}+\cdots\right) .
\end{aligned}$$
In particular, if $\alpha=n+2$ is fixed, then for all $\varepsilon \in(0,1)$ there exists a universal $s_{\varepsilon}>0$ depending only on $\varepsilon$ such that the two factors in parentheses in (4.8)-(4.9) are in the interval $[1-\varepsilon, 1+\varepsilon]$ for $s \geqslant s_{\varepsilon}$. This remark is useful because it provides uniform estimates for $H_{1, \ell}(x)$ and $H_{2, \ell}(x)$ as $x \rightarrow 0^{+}$, where the constants depend on $\ell$ but the estimates hold for all $x \in(0, \delta]$ with $\delta$ independent of $\ell$.

We are now able to state the main result of this section. A similar representation formula was used in a different setting in [15, Section 6]. We will say more about this at the end of the paper.

Proposition 4.2. Assume only that $u=\mathbf{O}\left(x^{M}\right)$ as $x \rightarrow 0^{+}$for some $M>1$ rather than $|u|=O\left(x^{\infty}\right)$. Denote the restriction of a function $v$ on the total space to the slice $\{x=t\}$ by $v(t)$. Fix $0<x_{0} \ll 1$.

Then, with all of the infinite sums converging in $C_{\text {loc }}^{0}$, it holds on $\left(0, x_{0}\right] \times D$ that
$$\begin{aligned}
\stackrel{\circ}{u}(x) & =-\frac{x^{-n-1}}{n+2} \int_{0}^{x} t^{n} \stackrel{\circ}{G}_{0}(t) d t+\frac{x}{n+2} \int_{0}^{x} t^{-2} \stackrel{\circ}{G}_{0}(t) d t \\
& +\sum_{\ell=1}^{\infty}\left(\frac{u_{\ell}\left(x_{0}\right)}{H_{2, \ell}\left(x_{0}\right)}+\frac{2 H_{1, \ell}\left(x_{0}\right)}{H_{2, \ell}\left(x_{0}\right)} \int_{0}^{x_{0}} t^{n-1} H_{2, \ell}(t) \stackrel{\circ}{G}_{\ell}(t) d t\right) H_{2, \ell}(x) \varphi_{\ell} \\
& -\sum_{\ell=1}^{\infty}\left(2 H_{1, \ell}(x) \int_{0}^{x} t^{n-1} H_{2, \ell}(t) \stackrel{\circ}{G}_{\ell}(t) d t\right) \varphi_{\ell}-\sum_{\ell=1}^{\infty}\left(2 H_{2, \ell}(x) \int_{x}^{x_{0}} t^{n-1} H_{1, \ell}(t) \stackrel{\circ}{G}_{\ell}(t) d t\right) \varphi_{\ell}
\end{aligned}$$
Proof. Consider an ODE of the general form
$$x^{2} v^{\prime \prime}(x)+(n+1) x v^{\prime}(x)-(n+1) v(x)-\lambda x^{-1} v(x)=f(x)$$
for some constant $\lambda>0$. A function of the form $v(x)=x^{-n / 2} F(2 \sqrt{\lambda / x})$ is a homogeneous solution of this ODE if and only if $F(s)$ satisfies the modified Bessel equation
$$s^{2} F^{\prime \prime}(s)+s F^{\prime}(s)-\left(\alpha^{2}+s^{2}\right) F(s)=0$$
for $\alpha=n+2$. Thus, the two homogeneous solutions of (4.11) are
$$H_{1}(x)=\frac{1}{x^{n / 2}} I_{\alpha}\left(2 \frac{\sqrt{\lambda}}{\sqrt{x}}\right), H_{2}(x)=\frac{1}{x^{n / 2}} K_{\alpha}\left(2 \frac{\sqrt{\lambda}}{\sqrt{x}}\right)$$
as above. By Abel's formula and by (4.8)-(4.9),
$$I_{\alpha}(s) K_{\alpha}^{\prime}(s)-I_{\alpha}^{\prime}(s) K_{\alpha}(s)=-\frac{1}{s} .$$
By variation of parameters, the general solution to (4.11) is
$$v(x)=c_{1} H_{1}(x)+c_{2} H_{2}(x)+H_{1}(x) \int_{x}^{x_{0}} \frac{H_{2}(t) f(t)}{t^{2} W(t)} d t-H_{2}(x) \int_{x}^{x_{0}} \frac{H_{1}(t) f(t)}{t^{2} W(t)} d t,$$
where thanks to (4.14) the Wronskian $W(t)$ is given by
$$W(t)=H_{1}(t) H_{2}^{\prime}(t)-H_{1}^{\prime}(t) H_{2}(t)=-\sqrt{\lambda} t^{-n-\frac{3}{2}}\left(I_{\alpha} K_{\alpha}^{\prime}-I_{\alpha}^{\prime} K_{\alpha}\right)(2 \sqrt{\lambda / t})=\frac{1}{2 t^{n+1}} .$$
Thus, (4.15) simplifies to
$$v(x)=c_{1} H_{1}(x)+c_{2} H_{2}(x)+2 H_{1}(x) \int_{x}^{x_{0}} t^{n-1} H_{2}(t) f(t) d t-2 H_{2}(x) \int_{x}^{x_{0}} t^{n-1} H_{1}(t) f(t) d t .$$
To solve out the constants $c_{1}, c_{2}$, we first take $x=x_{0}$, so that
$$v\left(x_{0}\right)=c_{1} H_{1}\left(x_{0}\right)+c_{2} H_{2}\left(x_{0}\right) .$$
Next we divide (4.17) by $H_{1}(x)$ and let $x \rightarrow 0^{+}$. Notice that $H_{1}(x) \rightarrow \infty$ and $H_{2}(x) \rightarrow 0$ as $x \rightarrow 0^{+}$. We claim that if $|v|=O(1)$ and $|f|=O(1)$, then it follows that
$$0=c_{1}+2 \int_{0}^{x_{0}} t^{n-1} H_{2}(t) f(t) d t$$
so we can solve for $c_{1}$ and $c_{2}$. This is clear except for the limit of the second integral term from (4.17). To see that this is zero, we can assume that $\left|\int_{x}^{x_{0}} t^{n-1} H_{1}(t) f(t) d t\right|$ goes to $\infty$ because otherwise (4.19) follows after passing to a subsequence. Then L'Hôpital's rule requires us to check that
$$\frac{\frac{d}{d x} \int_{x}^{x_{0}} t^{n-1} H_{1}(t) f(t) d t}{\frac{d}{d x} \frac{H_{1}(x)}{H_{2}(x)}}=\frac{x^{n-1} H_{1}(x) f(x)}{\frac{W(x)}{H_{2}(x)^{2}}} \rightarrow 0,$$
and we can easily see that this is true by using (4.16) and (4.8)-(4.9). In sum, if $|f|=O(1)$ as $x \rightarrow 0^{+}$ and if $v$ solving (4.11) remains uniformly bounded as well, then
$$\begin{aligned}
v(x) & =\left(\frac{v\left(x_{0}\right)}{H_{2}\left(x_{0}\right)}+\frac{2 H_{1}\left(x_{0}\right)}{H_{2}\left(x_{0}\right)} \int_{0}^{x_{0}} t^{n-1} H_{2}(t) f(t) d t\right) H_{2}(x) \\
& -2 H_{1}(x) \int_{0}^{x} t^{n-1} H_{2}(t) f(t) d t-2 H_{2}(x) \int_{x}^{x_{0}} t^{n-1} H_{1}(t) f(t) d t
\end{aligned}$$

To apply this result to our situation, we now let $\lambda=\lambda_{\ell}, f=\dot{G}_{\ell}$ and $v=\dot{u}_{\ell}$ for all $\ell \geqslant 1$. Thanks to our assumption that $u=\mathbf{O}\left(x^{M}\right)$ for some $M>1$, it is obvious that $v$ and $f$ are $O(1)$, so (4.21) holds. In fact, only $M \geqslant 0$ is needed for this. For the missing case $\ell=0$ we use the analogous representation formula (3.37), and here we only require that $M>\frac{1}{2}$. Thus, ignoring convergence issues,
$$\begin{aligned}
\stackrel{\circ}{u}(x) & =\left(\frac{\stackrel{\circ}{u}_{0}\left(x_{0}\right)}{x_{0}}+\frac{x_{0}^{-n-2}}{n+2} \int_{0}^{x_{0}} t^{n} \stackrel{\circ}{G}_{0}(t) d t\right) x \\
& -\frac{x^{-n-2}}{n+2} \int_{0}^{x} t^{n} \stackrel{\circ}{G}_{0}(t) d t-\frac{x}{n+2} \int_{x}^{x_{0}} t^{-2} \stackrel{\circ}{G}_{0}(t) d t \\
& +\sum_{\ell=1}^{\infty}\left(\frac{\stackrel{\circ}{u}_{\ell}\left(x_{0}\right)}{H_{2, \ell}\left(x_{0}\right)}+\frac{2 H_{1, \ell}\left(x_{0}\right)}{H_{2, \ell}\left(x_{0}\right)} \int_{0}^{x_{0}} t^{n-1} H_{2, \ell}(t) \stackrel{\circ}{G}_{\ell}(t) d t\right) H_{2, \ell}(x) \varphi_{\ell} \\
& -\sum_{\ell=1}^{\infty}\left(2 H_{1, \ell}(x) \int_{0}^{x} t^{n-1} H_{2, \ell}(t) \stackrel{\circ}{G}_{\ell}(t) d t\right) \varphi_{\ell}-\sum_{\ell=1}^{\infty}\left(2 H_{2, \ell}(x) \int_{x}^{x_{0}} t^{n-1} H_{1, \ell}(t) \stackrel{\circ}{G}_{\ell}(t) d t\right) \varphi_{\ell}
\end{aligned}$$
The following claim, which is not optimal but sufficient, makes this rigorous.
Claim: The three infinite sums in (4.22) converge in $C_{\text {loc }}^{0}$. Moreover, for all $N>0$ there exists a small number $x_{0, N}>0$ such that if $x_{0} \leqslant x_{0, N}$, then each of these sums is pointwise $O\left(x^{N}\right)$ as $x \rightarrow 0^{+}$.

Assume for a moment that the Claim is true. Note that $\left|t^{n} \dot{G}_{0}(t)\right|=O\left(t^{n+2 M}\right)$ because $u=\mathbf{O}\left(x^{M}\right)$. Thus, the first un-boxed term on the right-hand side of (4.22) is $O\left(x^{2 M-1}\right)=o(x)$ because $M>1$. By writing $\int_{x}^{x_{0}}=\int_{0}^{x_{0}}-\int_{0}^{x}$, we can split the second box in (4.22) into a constant multiple of $x$ plus a term which is $O\left(x^{2 M}\right)=o(x)$ because $M>\frac{1}{2}$. Then the constant multiple of $x$ must cancel the first box in (4.22) to make $\dot{u}(x)=o(x)$, so the proposition follows. Thus, it remains to prove the Claim.

We begin with two preliminary estimates. First, there is a constant $C$ such that for all $\ell \geqslant 1$,
$$\left\|\varphi_{\ell}\right\|_{L^{\infty}(D)} \leqslant C \ell^{\frac{1}{2}} .$$
This follows from a standard estimate for eigenfunctions of the Laplacian on a closed manifold together with Weyl's law. Second, for all $x \in(0,1]$, all $\ell \geqslant 1$ and all $N_{1}, N_{2}>0$,
$$\left|\stackrel{\circ}{u}_{\ell}(x)\right|+\left|\stackrel{\circ}{G}_{\ell}(x)\right| \leqslant C_{N_{1}, N_{2}} \ell^{-N_{1}} x^{N_{2}} .$$
Indeed, for any fixed $x$, integration by parts over $D$ shows as usual that $\dot{u}_{\ell}(x), \dot{G}_{\ell}(x)$ decay faster than any power of $\ell$, and the constants in these estimates can be bounded by the norms of sufficiently high tangential derivatives of $\stackrel{\circ}{u}(x), \stackrel{\circ}{G}(x)$. Since $u=\mathbf{O}\left(x^{M}\right)$, any tangential derivative of $\stackrel{\circ}{u}(x)$ is $O\left(x^{\infty}\right)$. The same holds for $\dot{G}(x)$ because as in the proof of Lemma 3.9, we can decompose $u$ into an $\mathbf{O}\left(x^{M}\right)$ radial part plus $\mathbf{O}\left(x^{\infty}\right)$, and this shows that $\dot{G}(x)$ decomposes into an $\mathbf{O}\left(x^{2 M}\right)$ radial part plus $\mathbf{O}\left(x^{\infty}\right)$.

We now apply (4.23)-(4.24) to each term of the three infinite sums in (4.22). Then we can see that in order to prove the Claim, it will be enough to prove a bound of the form
$$\frac{H_{2, \ell}(x)}{H_{2, \ell}\left(x_{0}\right)}+H_{1, \ell}(x) \sup _{0<t \leqslant x}\left(t^{\bar{N}} H_{2, \ell}(t)\right)+H_{2, \ell}(x) \sup _{x \leqslant t \leqslant x_{0}}\left(t^{\bar{N}} H_{1, \ell}(t)\right) \leqslant C_{x_{0}, \bar{N}} \ell^{N_{0}} x^{\bar{N}-N_{0}}$$
for some universal $N_{0}>0$ and for all $\bar{N} \geqslant N_{0}$. This bound needs to hold for all $x \in\left(0, x_{0}\right]$ and $\ell \geqslant 1$, but we can assume that $x_{0}$ is less than some small number $x_{0, \bar{N}}>0$ depending only on $\bar{N}$.

By the remark after (4.8)-(4.9), for all $\varepsilon>0$ there exists an $x_{0, \varepsilon}>0$ independent of $\ell$ such that for all $0<x \leqslant x_{0} \leqslant x_{0, \varepsilon}$, all $\ell \geqslant 1$ and all $\bar{N}>0$, the left-hand side of (4.25) is bounded by
$$\begin{aligned}
& (1+\varepsilon)\left(\frac{x}{x_{0}}\right)^{-\frac{n}{2}+\frac{1}{4}} x^{\bar{N}} \sup _{0<t \leqslant x_{0}}\left(t^{-\bar{N}} e^{2 \sqrt{\lambda_{\ell}}\left(\frac{1}{\sqrt{x_{0}}}-\frac{1}{\sqrt{t}}\right)}\right)^{1} \\
& +\frac{1+\varepsilon}{4 \sqrt{\lambda_{\ell}}} x^{-\frac{n}{2}+\frac{1}{4}}\left[e^{\frac{2 \sqrt{\lambda_{\ell}}}{\sqrt{x}}} \sup _{0<t \leqslant x}\left(t^{-\frac{n}{2}+\frac{1}{4}+\bar{N}} e^{-\frac{2 \sqrt{\lambda_{\ell}}}{\sqrt{t}}}\right)^{(2)}+e^{-\frac{2 \sqrt{\lambda_{\ell}}}{\sqrt{x}}} \sup _{x \leqslant t \leqslant x_{0}}\left(t^{-\frac{n}{2}+\frac{1}{4}+\bar{N}} e^{\frac{2 \sqrt{\lambda_{\ell}}}{\sqrt{t}}}\right)^{(3)}\right] .
\end{aligned}$$
As a function of $t$, ① is increasing from $t=0$ until it reaches its global maximum. Assume $\bar{N} \geqslant \frac{n}{2}-\frac{1}{4}$. Then (2) is increasing for all $t>0$, and (3) is decreasing from $t=0$ until it reaches its global minimum. The maximum of (1) and the minimum of (3) are obviously attained for $t / \lambda_{\ell}$ equal to some constant depending only on $\bar{N}$, i.e., these functions are monotone on $\left(0, x_{0}\right]$ if $x_{0} \leqslant x_{0, \bar{N}} \ll 1$. Thus,
$$(4.26) \leqslant C_{x_{0}, \bar{N}} x^{\bar{N}-\frac{n}{2}+\frac{1}{4}}+C \lambda_{\ell}^{-\frac{1}{2}} x^{\bar{N}-n+\frac{1}{2}}$$
for all $\bar{N} \geqslant \frac{n}{2}-\frac{1}{4}$, all $0<x \leqslant x_{0} \leqslant x_{0, \bar{N}}$ and all $\ell \geqslant 1$, where $C$ is a universal constant independent of all of these parameters. This implies (4.25) (with a large safety margin), hence the Claim after (4.22), and hence, as we have already explained, the proposition. \(\square\)

To make the above proposition useful for us, we also need the following calculus lemma. This is a sharper version of an estimate that was already used during the proof of the proposition.

Lemma 4.3. Let $c>0$ and $k>-\frac{3}{2}$. Then for all $x>0$ we have that
$$\int_{0}^{x} t^{k} e^{-\frac{c}{\sqrt{t}}} d t<\frac{2}{c} x^{k+\frac{3}{2}} e^{-\frac{c}{\sqrt{x}}} .$$
Moreover, for all $\varepsilon>0$ and for all $0<x \leqslant x_{0}$ with $x_{0} \leqslant\left(\frac{\varepsilon}{2+\varepsilon} \frac{c}{2 k+3}\right)^{2}$ we have that
$$\int_{x}^{x_{0}} t^{k} e^{\frac{c}{\sqrt{t}}} d t<\frac{2+\varepsilon}{c} x^{k+\frac{3}{2}} e^{\frac{c}{\sqrt{x}}} .$$
Proof. For (4.28) we begin by observing that for all $c>0$ and all $k>-\frac{3}{2}$,
$$\lim _{x \rightarrow 0} \frac{c \int_{0}^{x} t^{k} e^{-\frac{c}{\sqrt{t}}} d t}{x^{k+\frac{3}{2}} e^{-\frac{c}{\sqrt{x}}}}=2, \quad \lim _{x \rightarrow \infty} \frac{c \int_{0}^{x} t^{k} e^{-\frac{c}{\sqrt{t}}} d t}{x^{k+\frac{3}{2}} e^{-\frac{c}{\sqrt{x}}}}=0 .$$
This is an application of L'Hôpital's rule. The limit as $x \rightarrow 0$ is always of the form $\frac{0}{0}$, so L'Hôpital can be applied directly, while for $x \rightarrow \infty$ we need to consider the two cases $-\frac{3}{2}<k<-1$, where the limit is of the form $\frac{\text { finite }}{\infty}=0$, and $k \geqslant-1$, where it takes the form $\frac{\infty}{\infty}$ and L'Hôpital can be used.

If the function whose limits we found in (4.30) has no critical points, we are done. If $x \in(0, \infty)$ is a critical point, then the critical point equation implies that $c+(2 k+3) \sqrt{x}>0$ and
$$\frac{c \int_{0}^{x} t^{k} e^{-\frac{c}{\sqrt{t}}} d t}{x^{k+\frac{3}{2}} e^{-\frac{c}{\sqrt{x}}}}=\frac{2 c}{c+(2 k+3) \sqrt{x}} .$$
Because $k>-\frac{3}{2}$, this ratio is strictly less than 2, so the function cannot attain a global maximum at $x$ and is therefore strictly less than 2 everywhere in this case as well.

The argument for (4.29) is similar. The limits of the corresponding function as $x \rightarrow 0$ and $x \rightarrow x_{0}$ are 2 and 0 , respectively. If $x \in\left(0, x_{0}\right)$ is a critical point, then $c-(2 k+3) \sqrt{x}>0$ and
$$\frac{c \int_{x}^{x_{0}} t^{k} e^{\frac{c}{\sqrt{t}}} d t}{x^{k+\frac{3}{2}} e^{\frac{c}{\sqrt{x}}}}=\frac{2 c}{c-(2 k+3) \sqrt{x}} .$$

This ratio is strictly greater than 2 , but if $x_{0} \leqslant\left(\frac{\varepsilon}{2+\varepsilon} \frac{c}{2 k+3}\right)^{2}$ then it is strictly less than $2+\varepsilon$. \(\square\)
4.2 . The continuity argument. Fix $N \in(0,1)$ once and for all. Define
$$H(x):=x^{-\frac{n}{2}+\frac{1}{4}} e^{-\frac{2 \sqrt{\lambda_{1}}}{\sqrt{x}}} .$$
Throughout this section, write $v(t)$ to denote the restriction of a function $v$ on the total space to the compact slice $\{x=t\}$. Given $x_{0} \in(0,1], C>0$ and $x \in\left(0, x_{0}\right]$, consider the statement
$$\mathbf{S}_{x_{0}, C}(x) \text { : "For all } y \in\left(0, x_{0}\right] \text {, we have that } \max |u(y)| \leqslant \begin{cases}C H(y) & \text { if } y \in\left[x, x_{0}\right], \\ C H(x)\left(\frac{y}{x}\right)^{N} & \text { if } y \in(0, x] \text {." }\end{cases}$$
Proposition 4.4. Assume only that $u=\mathbf{O}\left(x^{M}\right)$ as $x \rightarrow 0^{+}$for some $M>\max \left\{\frac{3}{2}, 2-N\right\}$ rather than $|u|=O\left(x^{\infty}\right)$. There exist $x_{0} \in(0,1]$ and $C>0$ such that $\inf \left\{x \in\left(0, x_{0}\right]: \mathbf{S}_{x_{0}, C}(x)\right.$ is true $\}=0$.

If this is true, then $u$ satisfies the pointwise decay estimate stated in Reduction 4.1 uniformly on all intervals $\left[x_{i}, x_{0}\right]$ for some infinite sequence $x_{i} \rightarrow 0^{+}$. Thus, the Main Theorem is proved.

For the proof of Proposition 4.4 we need the following barrier property of the function $x^{N}$. This is a standard application of the maximum principle except for one twist.
Lemma 4.5. Assume only that $u=\mathbf{O}\left(x^{M}\right)$ as $x \rightarrow 0^{+}$for some $M>\frac{N}{2}$. There exists an $x_{1}>0$ such that the following is true. Let $\Omega \subset\left\{x<x_{1}\right\}$ be an open set. Let $p \in \Omega$. Let $c>0$. It is not possible to have $u \leqslant c x^{N}$ in $\Omega$ with equality at $p$, or to have $u \geqslant-c x^{N}$ in $\Omega$ with equality at $p$.
Proof. Define $B=c x^{N}$. If $u \leqslant B$ in $\Omega$ with equality at $p$, then $(i \partial \bar{\partial} B)(p) \geqslant(i \partial \bar{\partial} u)(p)$, so in particular $\left(\omega_{h}+i \partial \bar{\partial} B\right)(p)>0$ and the Monge-Ampère operator $M_{h}(B)$ as in (3.29) is defined at $p$. In addition, $0=M_{h}(u) \leqslant M_{h}(B) \leqslant L_{h}(B)=-\gamma B<0$ at $p$, where $\gamma=(1-N)(n+1+N)>0$ and where we have used the concavity of log det on the space of Hermitian matrices. This is a contradiction.

Fix $C_{M}$ so that $|i \partial \bar{\partial} u|_{\omega_{h}} \leqslant C_{M} x^{M}$. Note that $\left|i \partial \bar{\partial} x^{N}\right|_{\omega_{h}}=\delta x^{N}$ for some universal $\delta>0$. There is also a universal $\varepsilon>0$ such that $\left|Q_{h}(v)\right| \leqslant \varepsilon|i \partial \bar{\partial} v|_{\omega_{h}}^{2}$ for all functions $v$ at all points where $|i \partial \bar{\partial} v|_{\omega_{h}} \leqslant 1$. Then choose $x_{1}$ so that $\max \left\{C_{M} x_{1}^{M}, \delta x_{1}^{N}\right\} \leqslant 1$ and $\varepsilon C_{M}^{2} x_{1}^{2 M-N} \leqslant \lambda \gamma$, where $\lambda=\min \left\{1, \frac{\gamma}{\delta \varepsilon}\right\}$.

Now suppose that $u \geqslant-B$ in $\Omega$ with equality at $p$. If $c<\lambda$, then in particular $c<1$, so we have $|i \partial \bar{\partial} B|_{\omega_{h}}=c \delta x^{N}<1<\sqrt{n}=\left|\omega_{h}\right|_{\omega_{h}}$, hence $\omega_{h}-i \partial \bar{\partial} B>0$, on $\Omega$. Thus, the Monge-Ampère operator $M_{h}(-B)$ is defined on $\Omega$, and $0=M_{h}(u) \geqslant M_{h}(-B)=\gamma B+Q_{h}(-B) \geqslant\left(\gamma c-\varepsilon c^{2} \delta^{2} x^{N}\right) x^{N}>0$ at $p$ because $\delta x^{N}<1$ and $c<\frac{\gamma}{\delta \varepsilon}$. This is a contradiction. We also have $-Q_{h}(u)=L_{h}(u) \geqslant L_{h}(-B)=\gamma B$ at $p$. Thus, if $c \geqslant \lambda$, then $\lambda \gamma x^{N} \leqslant\left|Q_{h}(u)\right| \leqslant \varepsilon C_{M}^{2} x^{2 M}$ at $p$. This is another contradiction. \(\square\)

Proof of Proposition 4.4. We begin by setting notation and explaining some conventions that will be in force throughout the proof. Fix $M>\max \left\{\frac{3}{2}, 2-N\right\}$ and a constant $C_{M}$ such that $\max |u(x)| \leqslant C_{M} x^{M}$ for all $x \in(0,1]$. We let $C_{0}$ denote a generic constant that can increase from line to line or even within the same line but that is not allowed to depend on the constants $x_{0}, C$, which are still to be chosen, or on any unproved properties of $u$. By contrast, $C$ will always denote the specific constant in (4.34).

We will show that the proposition holds for all sufficiently small values of $x_{0}$ and for all sufficiently large values of $C$. Thus, there is no harm in assuming that $C \geqslant 1$ and $x_{0} \leqslant \frac{1}{2}$. We will also assume that $x_{0}$ is so small that $x_{0} \leqslant x_{1}$ as in Lemma 4.5, that the representation formula (4.10) holds on $\left(0, x_{0}\right] \times$ $D$, and that $\max |u(x)-\dot{u}(x)| \leqslant \frac{1}{6} H(x)$ for all $x \in\left(0, x_{0}\right]$. The latter is possible by Lemma 3.5.

Consider any two numbers $x_{0}$ and $C$ satisfying these constraints. We begin by observing that if, in addition, $C H\left(x_{0}\right) \geqslant C_{M} x_{0}^{N}$, then the statement $\mathbf{S}_{x_{0}, C}\left(x_{0}\right)$ is true because $\max |u(x)| \leqslant C_{M} x^{M}$ for all $x \in(0,1]$, where $M \geqslant N$. Thus, the set of all $x \in\left(0, x_{0}\right]$ for which $\mathbf{S}_{x_{0}, C}(x)$ is true is not empty.

The infimum, $x_{*}$, of this set is an element of $\left[0, x_{0}\right]$. We may assume that $x_{*}>0$ for all admissible choices of $x_{0}$ and $C$, aiming to derive a contradiction if $x_{0}$ is small and $C$ is large. Because $\max |u(y)|$ is continuous in $y$, clearly $\mathbf{S}_{x_{0}, C}(x)$ is true for $x=x_{*}$ but not for any $x<x_{*}$.

Claim 1: There exists a $y=y_{*} \in\left(0, x_{*}\right]$ for which (4.34) with $x=x_{*}$ is an equality.
Proof: If the inequality (4.34) with $x=x_{*}$ was strict for all $y \in\left(0, x_{*}\right]$, then, again because max $|u(y)|$ is continuous in $y$, the first line of (4.34) would obviously still be true for all $x \in\left[x_{*}-\varepsilon, x_{*}\right)$ for some $\varepsilon \in\left(0, \frac{x_{*}}{2}\right]$. We will now show that the second line of (4.34) also still holds for all $x \in\left[x_{*}-\varepsilon, x_{*}\right)$ after decreasing $\varepsilon$ if needed. If so, then $\mathbf{S}_{x_{0}, C}(x)$ holds for all $x \in\left[x_{*}-\varepsilon, x_{*}\right)$, contradicting the minimality of $x_{*}$ and proving the Claim. Thus, we need to prove that $\max |u(y)| \leqslant C H(x)\left(\frac{y}{x}\right)^{N}$ for all $y \in(0, x]$ and all $x \in\left[x_{*}-\varepsilon, x_{*}\right)$, given that this is true for $x=x_{*}$ with strict inequality for all $y \in\left(0, x_{*}\right]$.

To do so, we begin by defining $\bar{x}_{*}$ to be the largest number in ( $0, x_{*}$ ] such that
$$C_{M} \bar{x}_{*}^{M-N} \leqslant \min \left\{x^{-N} H(x): x_{*} / 2 \leqslant x \leqslant x_{*}\right\} .$$
This exists because $M>N$. Then for all $y \in\left(0, \bar{x}_{*}\right)$ it directly follows from (4.35), $C \geqslant 1$ and $\varepsilon \leqslant \frac{x_{*}}{2}$ that max $|u(y)| \leqslant C_{M} y^{M}<C H(x)\left(\frac{y}{x}\right)^{N}$ for all $x \in\left[x_{*}-\varepsilon, x_{*}\right)$. Thus, it remains to prove the desired inequality for all $y \in\left[\bar{x}_{*}, x\right]$ and all $x \in\left[x_{*}-\varepsilon, x_{*}\right)$. Then simply note that after decreasing $\varepsilon$ if needed the inequality actually holds for all $y \in\left[\bar{x}_{*}, x_{*}\right]$ because on the compact interval $\left[\bar{x}_{*}, x_{*}\right]$ the continuous function $y \mapsto \max |u(y)|$ is pointwise strictly smaller than the continuous function $y \mapsto C H\left(x_{*}\right)\left(\frac{y}{x_{*}}\right)^{N}$, which is uniformly approximated by the functions $y \mapsto C H(x)\left(\frac{y}{x}\right)^{N}$ as $x \rightarrow x_{*}$. \(\square\)

Lemma 4.5 rules out the possibility that $y_{*}<x_{*}$, so $y_{*}=x_{*}$ and hence $\max \left|u\left(x_{*}\right)\right|=C H\left(x_{*}\right)>0$. For a contradiction it then clearly suffices to prove that $\max \left|u\left(x_{*}\right)\right| \leqslant \frac{5}{6} C H\left(x_{*}\right)$ if $x_{0}$ is small and $C$ is large. This follows if we can prove that $\max \left|\dot{u}\left(x_{*}\right)\right| \leqslant \frac{2}{3} C H\left(x_{*}\right)$, and doing so will take up the rest of this paper. The idea is to bound max $\left|\dot{u}\left(x_{*}\right)\right|$ by applying the representation formula (4.10) at $x=x_{*}$, whose right-hand side is a linear functional of $\dot{G}$ (over the whole end $\left\{0<x \leqslant x_{0}\right\}$ ), i.e., a quadratic or higher functional of $i \partial \bar{\partial} u$. To make this precise, we first bound $i \partial \bar{\partial} u$ in terms of $u$ using Schauder theory (see the following Claim) and then bound $u$ pointwise by using (4.34) for $x=x_{*}$.

To state Claim 2 we need some more notation. For $t \in\left(0, x_{0}\right]$ and $r \in\left(0, \frac{1}{2}\right]$ define
$$A_{r}(t):=\{(1-r) t<x<(1+r) t\} .$$
Recall here that $\rho=-\sqrt{(n+1) / 2} \log x$ satisfies $|d \rho|_{\omega_{h}}=1$. Thus, for all $p \in A_{r}(t)$ with $x(p)=t$ there exists an $\omega_{h}$-geodesic ball of radius comparable to $r$ centered at $p$ which is contained in $A_{r}(t)$.

Claim 2: For all $Q \in \mathbb{N}_{0}$ there exists an absolute constant $C_{Q}$, and for all $\eta \in(0, M-1)$ there exists an absolute number $x_{0, \eta}>0$, such that if $x_{0} \leqslant x_{0, \eta}$, then for all $t \in\left(0, x_{0}\right]$, all $r \in[\sqrt{t} / 2,1 / 2]$ and all $(\ell, Q) \in\{(0,0)\} \cup\left(\mathbb{N}_{\geqslant 1} \times \mathbb{N}_{0}\right)$ we have that
$$\left|\dot{G}_{\ell}(t)\right| \leqslant C_{Q}\left(1+\lambda_{\ell}\right)^{-Q}\left(\frac{\sqrt{t}}{r}\right)^{2 Q} \frac{t^{\eta}}{r^{2}} \sup _{A_{r}(t)}|u| .$$

For $r \sim \sqrt{t}$, which is already a useful case, one can prove (4.37) by passing to a local covering space and reducing to the standard Schauder theory on $\mathbb{C}^{n}$ even if $D$ is a non-flat Calabi-Yau manifold; see the argument after Reduction 4.1. However, we also require (4.37) for $r \gg \sqrt{t}$, and for this we do need to assume that $D$ is flat. But this is the only point in Section 4 where the flatness of $D$ is used, and it again seems likely that this can be avoided by using the methods of [11].

Proof: We begin with the case $Q=0$, where $\ell \in \mathbb{N}_{0}$ is arbitrary. We first claim that
$$\left|\stackrel{\circ}{G}_{\ell}(t)\right| \leqslant C_{0}\left\|\varphi_{\ell}\right\|_{L^{1}(D)} \max _{2 \leqslant k \leqslant n} \max _{\{x=t\}}|i \partial \bar{\partial} u|_{\omega_{h}}^{k} \leqslant C_{0} \max _{2 \leqslant k \leqslant n}\left(\frac{1}{r^{2}} \sup _{A_{r}(t)}|u|\right)^{k} .$$
Here the first inequality is clear from (4.4)-(4.5). The second inequality follows from Schauder theory applied on balls of radius $\sim r$ in quasi-coordinates for $\omega_{h}$ (see the proof of Lemma 3.4), using also the
fact that $\left\|\varphi_{\ell}\right\|_{L^{2}(D)}=1$. As $M>1$, given any $\eta \in(0, M-1)$ we can choose $x_{0, \eta}$ so small that
$$C_{M}(3 / 2)^{M} x_{0, \eta}^{M-1-\eta} \leqslant 1 / 4 .$$
As $\max |u(y)| \leqslant C_{M} y^{M}$, it follows for all $r \in[\sqrt{t} / 2,1 / 2]$ that
$$\sup _{A_{r}(t)}|u| \leqslant C_{M}(3 t / 2)^{M} \leqslant t^{\eta}(t / 4) \leqslant t^{\eta} r^{2}<r^{2} .$$
This shows that the $k=2$ term in (4.38) dominates. It also allows us to estimate this quadratic term by a small linear term (which is actually more convenient), proving (4.37) for $Q=0$.

For $Q \geqslant 1$ and $\ell \geqslant 1$, we first integrate by parts $Q$ times in the definition of $\dot{G}_{\ell}(t)$, which brings out a factor of $\lambda_{\ell}^{-Q}$ while replacing $\dot{G}(t)$ by a 2Q-th covariant derivative of $\dot{G}(t)$ with respect to the given flat metric on $D$. We gain $2 Q$ factors of $\sqrt{t}$ by replacing each of these covariant derivatives on $D$ by a directional derivative with respect to some quasi-coordinate for $\omega_{h}$. By Schauder theory, we can trade each of the latter for a factor of $C_{0} / r$ if we also take the sup over a ball of radius $\sim r$.
$\square_{\text {Claim } 2}$
Thanks to Claim 2 and (4.34) for $x=x_{*}$, we are now able to estimate the right-hand side of (4.10) at $x=x_{*}$ and prove the desired result, i.e., that $\max \left|\dot{u}\left(x_{*}\right)\right| \leqslant \frac{2}{3} C H\left(x_{*}\right)$ if $x_{0}$ is small and $C$ is large. As discussed above, this will complete the proof of the proposition and of the Main Theorem.

Evaluate (4.10) at $x=x_{*}$, take $L^{\infty}$ norms over $\left\{x_{*}\right\} \times D$, apply the triangle inequality, and absorb irrelevant numerical constants. This yields the following:
$$\begin{aligned}
& \frac{1}{2} \max \left|\stackrel{\circ}{u}\left(x_{*}\right)\right| \leqslant(4) x_{*}^{-n-1} \int_{0}^{x_{*}} t^{n}\left|\dot{G}_{0}(t)\right| d t+{ }^{(5)} x_{*} \int_{0}^{x_{*}} t^{-2}\left|\dot{G}_{0}(t)\right| d t \\
& +\sum_{\ell=1}^{\infty}(1)\left(\text { (a) } \frac{\left|u_{\ell}\left(x_{0}\right)\right|}{H_{2, \ell}\left(x_{0}\right)}+(\text { b }) \frac{H_{1, \ell}\left(x_{0}\right)}{H_{2, \ell}\left(x_{0}\right)} \int_{0}^{x_{0}} t^{n-1} H_{2, \ell}(t)\left|\stackrel{\circ}{G}_{\ell}(t)\right| d t\right) H_{2, \ell}\left(x_{*}\right)\left\|\varphi_{\ell}\right\|_{L^{\infty}(D)} \\
& +\sum_{\ell=1}^{\infty}(3)\left(H_{1, \ell}\left(x_{*}\right) \int_{0}^{x_{*}} t^{n-1} H_{2, \ell}(t)\left|\dot{G}_{\ell}(t)\right| d t\right)\left\|\varphi_{\ell}\right\|_{L^{\infty}(D)} \\
& +\sum_{\ell=1}^{\infty}(2)\left(H_{2, \ell}\left(x_{*}\right) \int_{x_{*}}^{x_{0}} t^{n-1} H_{1, \ell}(t)\left|\dot{G}_{\ell}(t)\right| d t\right)\left\|\varphi_{\ell}\right\|_{L^{\infty}(D)} .
\end{aligned}$$
Here we have labeled all terms in order of increasing conceptual difficulty. We will now estimate these terms one by one. Because there are 6 contributions in total, it will be sufficient to prove that each of them (after summing over $\ell$ in cases (1)-(3)) is bounded above by $C H\left(x_{*}\right) / 20$.
(1) This is essentially the same as the estimates after (4.22) in the proof of Proposition 4.2. Claim 2 is not needed for this. Indeed, using (4.23)-(4.24) and choosing $x_{0}$ so small that the remark after (4.8) -(4.9) can be applied, we obtain as in (4.26) that
$$\sum_{\ell=1}^{\infty}(\mathrm{a}) \leqslant \sum_{\ell=1}^{\infty}\left[O\left(\ell^{-\infty} x_{0}^{\infty}\right)\left(\frac{x_{*}}{x_{0}}\right)^{-\frac{n}{2}+\frac{1}{4}} e^{-2 \sqrt{\lambda_{\ell}}\left(\frac{1}{\sqrt{x_{*}}}-\frac{1}{\sqrt{x_{0}}}\right)}\right] \leqslant O\left(x_{0}^{\infty}\right) \frac{H\left(x_{*}\right)}{H\left(x_{0}\right)} .$$
This will be bounded above by $C H\left(x_{*}\right) / 20$, as desired, if we choose $x_{0}$ to be smaller than some small absolute constant and then choose $C \geqslant 1 / H\left(x_{0}\right)$. Similarly,
$$\sum_{\ell=1}^{\infty}\left(\mathrm{b} \leqslant O\left(x_{0}^{\infty}\right) \frac{H\left(x_{*}\right)}{H\left(x_{0}\right)} \sum_{\ell=1}^{\infty}\left[O\left(\ell^{-\infty}\right) H_{1, \ell}\left(x_{0}\right) \int_{0}^{x_{0}} O\left(t^{\infty}\right) H_{2, \ell}(t) d t\right] \leqslant O\left(x_{0}^{\infty}\right) \frac{H\left(x_{*}\right)}{H\left(x_{0}\right)} .\right.$$
This concludes our discussion of (1).
In (2)-(5) we will use Claim 2 together with (4.34). We begin with some general remarks on the key question of how to choose $r$ in (4.37). A smaller $r$ makes (4.37) weaker. On the other hand, $r$ needs to be chosen sufficiently small so that the function on the right-hand side of (4.34), i.e., $y \mapsto C H(y)$ for $y \in\left[x_{*}, x_{0}\right]$ and $y \mapsto C H\left(x_{*}\right)\left(\frac{y}{x_{*}}\right)^{N}$ for $y \in\left(0, x_{*}\right]$, varies at most by a bounded factor over the interval
$y \in((1-r) t,(1+r) t)$ for all $t$ in the domain of the relevant integral in (4.41). If so, then we are able to bound $\sup _{A_{r}(t)}|u|$ on the right-hand side of (4.37) by the value of this function at $y=t$, so we at least retain a chance of estimating the integral by $\sim C H\left(x_{*}\right)$ rather than by some other function of $x_{*}$ that might decay much more slowly than $H$. For a function of the form $y \mapsto \exp \left(-\delta y^{-\alpha}\right)(\alpha, \delta>0)$ we thus require that $r \lesssim \frac{1}{\delta \alpha} t^{\alpha}$. We will apply this with $\alpha=\frac{1}{2}, \delta$ fixed, and with $\alpha \rightarrow 0, \delta \alpha$ fixed. However, for us, it will sometimes be beneficial (see (3)) or at least harmless (see (4)-(5)) to choose $r \ll \frac{1}{\delta \alpha} t^{\alpha}$.
(2) Here we have $\alpha=\frac{1}{2}$ because the domain of integration is $t \in\left[x_{*}, x_{0}\right]$. Thus, our only option is to set $r \sim \sqrt{t}$ in (4.37). More precisely, we let $r=\sqrt{t} / 2$. Then we claim that, as expected,
$$\sup _{A_{r}(t)}|u| \leqslant C_{0} C H(t) \text { for all } t \in\left[x_{*}, x_{0}\right] \text {. }$$
Indeed, if $A_{r}(t) \subset\left\{x_{*} \leqslant x \leqslant x_{0}\right\}$, this follows from the first line of (4.34) (with $x=x_{*}$ ) precisely by the above argument motivating the choice $r \lesssim \sqrt{t}$. For $t$ so close to $x_{*}$ that $A_{r}(t) \not \subset\left\{x_{*} \leqslant x \leqslant x_{0}\right\}$, we also need to use the second line of (4.34) and the trivial fact that $\sup _{A_{r}(t) \cap\left\{x<x_{*}\right\}} C H\left(x_{*}\right)\left(\frac{x}{x_{*}}\right)^{N}=C H\left(x_{*}\right)$. Similary, for $t$ so close $x_{0}$ that $A_{r}(t) \not \subset\left\{x_{*} \leqslant x \leqslant x_{0}\right\}$, we moreover need to use our assumption that $|u| \leqslant C_{M} x^{M}$ on $A_{r}(t) \cap\left\{x_{0}<x \leqslant 1\right\}$ and choose $C$ large enough so that
$$C_{M}\left(x_{0}\left(1+\sqrt{x_{0}} / 2\right)\right)^{M} \leqslant C H\left(x_{0}\right) .$$
Having proved (4.44), we now combine this with (4.37) to obtain that
$$\begin{aligned}
\sum_{\ell=1}^{\infty}(2 & \leqslant \sum_{\ell=1}^{\infty} O\left(\ell^{-\infty}\right) x_{*}^{-\frac{n}{2}+\frac{1}{4}} e^{-\frac{2 \sqrt{\lambda_{\ell}}}{\sqrt{x_{*}}}} \int_{x_{*}}^{x_{0}} t^{n-1} t^{-\frac{n}{2}+\frac{1}{4}} e^{\frac{2 \sqrt{\lambda_{\ell}}}{\sqrt{t}}} t^{\eta-1} C H(t) d t \\
& \leqslant \sum_{\ell=1}^{\infty} O\left(\ell^{-\infty}\right) x_{*}^{-\frac{n}{2}+\frac{1}{4}} e^{-\frac{2 \sqrt{\lambda_{\ell}}}{\sqrt{x_{*}}}} \int_{x_{*}}^{x_{0}} C t^{-\frac{3}{2}+\eta} e^{\frac{2 \sqrt{\lambda_{\ell}}-2 \sqrt{\lambda_{1}}}{\sqrt{t}}} d t .
\end{aligned}$$
This holds for any given $\eta \in(0, M-1)$ if $x_{0} \leqslant x_{0, \eta}$ for some absolute number $x_{0, \eta}>0$.
We now choose $\eta>\frac{1}{2}$ (this is possible because $M>\frac{3}{2}$ ), evaluate the integral directly if $\lambda_{\ell}=\lambda_{1}$, and estimate it using Lemma 4.3 if $\lambda_{\ell}>\lambda_{1}$. Fixing $\varepsilon=1$ in Lemma 4.3 and also assuming that
$$3 \eta \sqrt{x_{0}} \leqslant \min \left\{\sqrt{\lambda_{\ell}}: \ell \geqslant 2, \lambda_{\ell}>\lambda_{1}\right\}-\sqrt{\lambda_{1}},$$
we thus obtain the following estimate:
$$\sum_{\ell=1}^{\infty}(2) \leqslant C \sum_{\ell=1}^{\infty}\left[O\left(\ell^{-\infty}\right) x_{*}^{-\frac{n}{2}+\frac{1}{4}} e^{-\frac{2 \sqrt{\lambda_{\ell}}}{\sqrt{x_{*}}}}\left\{\begin{array}{ll}
x_{0}^{\eta-\frac{1}{2}} /(2 \eta-1) & \text { if } \lambda_{\ell}=\lambda_{1} \\
x_{*}^{\eta} e^{\frac{2 \sqrt{\lambda_{\ell}}-2 \sqrt{\lambda_{1}}}{\sqrt{x_{*}}}} & \text { if } \lambda_{\ell}>\lambda_{1}
\end{array}\right] \leqslant \frac{C_{0} x_{0}^{\eta-\frac{1}{2}} \cdot C H\left(x_{*}\right)}{\min \{1,2 \eta-1\}} .\right.$$
This will be bounded by $C H\left(x_{*}\right) / 20$ if we decrease the absolute number $x_{0, \eta}>0$.
(3) While shorter than (2), this step may be more confusing because the domain is now $t \in\left(0, x_{*}\right]$, so (4.34) bounds $|u|$ in terms of a polynomial rather than an exponential, but we are also still integrating this against the exponential-type function $H_{2, \ell}(t)$. Thus, it may not be obvious how $r$ should be chosen (from $r \sim \sqrt{t}$ for exponentials to $r \sim 1$ for polynomials). However, we will see that the "easy" choice, $r \sim \sqrt{t}$, which does not require us to assume that $D$ is flat, is actually better and sufficient.

First, while the analog of (4.44) would still hold for $A_{r}(t) \subset\left\{x \leqslant x_{*}\right\}$ with $r \sim 1$, it would be false for $A_{r}(t) \not \subset\left\{x \leqslant x_{*}\right\}$ with $r \sim 1$ because the barrier function of (4.34) is exponential on $\left(x_{*}, x_{0}\right]$. It is however true in both cases with $r \sim \sqrt{t}$. Thus, setting $r=\sqrt{t} / 2$,
$$\sup _{A_{r}(t)}|u| \leqslant C_{0} C H\left(x_{*}\right)\left(\frac{t}{x_{*}}\right)^{N} \text { for all } t \in\left(0, x_{*}\right],$$
where the case $A_{r}(t) \not \subset\left(0, x_{*}\right]$ follows from the fact that
$$t(1+\sqrt{t} / 2)>x_{*} \Longrightarrow \sup \left\{H(y): y \in\left(x_{*}, t(1+\sqrt{t} / 2)\right]\right\} \leqslant C_{0} H\left(x_{*}\right) \leqslant C_{0} H\left(x_{*}\right)\left(\frac{t}{x_{*}}\right)^{N} .$$

Second, by combining (4.37) and (4.49), we obtain for all $\eta \in(0, M-1)$ that if $x_{0} \leqslant x_{0, \eta}$, then
$$\begin{aligned}
\sum_{\ell=1}^{\infty}(3) & \leqslant \sum_{\ell=1}^{\infty} O\left(\ell^{-\infty}\right) x_{*}^{-\frac{n}{2}+\frac{1}{4}} e^{\frac{2 \sqrt{\lambda_{\ell}}}{\sqrt{x_{*}}}} \int_{0}^{x_{*}} t^{n-1} t^{-\frac{n}{2}+\frac{1}{4}} e^{-\frac{2 \sqrt{\lambda_{\ell}}}{\sqrt{t}}} t^{\eta-1} C H\left(x_{*}\right)\left(\frac{t}{x_{*}}\right)^{N} d t \\
& \leqslant \sum_{\ell=1}^{\infty} O\left(\ell^{-\infty}\right) x_{*}^{-\frac{n}{2}+\frac{1}{4}-N} e^{\frac{2 \sqrt{\lambda_{\ell}}}{\sqrt{x_{*}}}} \int_{0}^{x_{*}} t^{\frac{n}{2}-\frac{7}{4}+\eta+N} e^{-\frac{2 \sqrt{\lambda_{\ell}}}{\sqrt{t}}} d t \cdot C H\left(x_{*}\right)
\end{aligned}$$
We can now apply Lemma 4.3 directly and without assuming that $\eta>\frac{1}{2}$ :
$$\frac{1}{C H\left(x_{*}\right)} \sum_{\ell=1}^{\infty}\left(3 \leqslant \sum_{\ell=1}^{\infty} O\left(\ell^{-\infty}\right) x_{*}^{-\frac{n}{2}+\frac{1}{4}-N} e^{\frac{2 \sqrt{\lambda_{\ell}}}{\sqrt{x_{*}}}} x_{*}^{\frac{n}{2}-\frac{1}{4}+\eta+N} e^{-\frac{2 \sqrt{\lambda_{\ell}}}{\sqrt{x_{*}}}} \leqslant C_{0} x_{*}^{\eta} .\right.$$
(4) Here and in (5), the upper barrier for $|u|$ from (4.34) and the function against which we need to integrate this barrier over the interval ( $0, x_{*}$ ] in (4.41) are polynomials. Away from $t=x_{*}$ this suggests that we should apply Claim 2 with $r \sim 1$. It is actually possible to work with $r \sim t^{\alpha}$ for any $\alpha \in\left[0, \frac{1}{2}\right)$, but choosing $\alpha>0$ makes the algebra longer while in the proof of Claim 2 only the Schauder estimates for $\alpha=\frac{1}{2}$ are easy and the ones for $\alpha \in\left[0, \frac{1}{2}\right)$ are all equally difficult, requiring us to assume that $D$ is flat. Thus, for simplicity, we will stick to the choice $r \sim 1$. However, as $t$ approaches $x_{*}$ we do need to choose $r$ smaller than this because the right-hand side of (4.34) is exponential rather than polynomial on $\left(x_{*}, x_{0}\right]$. As it turns out, the following straightforward choice will be good enough:
$$r=r(t):=\max \left\{\frac{1}{2}\left(1-\frac{t}{x_{*}}\right), \frac{1}{2} x_{*}^{\frac{1}{2}}\right\} \text { for all } t \in\left(0, x_{*}\right] .$$

To see that this makes (4.49) true for all $t \in\left(0, x_{*}\right]$, first observe that (4.34) trivially implies (4.49) if the sup is taken over $A_{r}(t) \cap\left\{x \leqslant x_{*}\right\}$. Now $A_{r}(t) \not \subset\left\{x \leqslant x_{*}\right\}$ is possible only if $t \in\left(x_{*}-x_{*}^{3 / 2}, x_{*}\right]$ as otherwise the max in (4.53) is realized by the first term and then $t(1+r) \leqslant x_{*}$ by computation. But if $t \in\left(x_{*}-x_{*}^{3 / 2}, x_{*}\right]$, then $r \leqslant \sqrt{t}$, so we can deal with the sup over $A_{r}(t) \cap\left\{x_{*}<x\right\}$ (if nonempty) by replacing $\sqrt{t} / 2$ with $\sqrt{t}$ in (4.50), which makes no difference.

As in (3), given (4.49), we can proceed using (4.37): for all $\eta \in\left(\frac{1}{2}, M-1\right)$, if $x_{0} \leqslant x_{0, \eta}$, then
$$\frac{(4)}{C H\left(x_{*}\right)} \leqslant x_{*}^{-n-1} \int_{0}^{x_{*}} t^{n}\left[\frac{t^{\eta}}{r(t)^{2}}\left(\frac{t}{x_{*}}\right)^{N}\right] d t \leqslant x_{*}^{\eta-1} \int_{0}^{x_{*}} \frac{d t}{r(t)^{2}} .$$
Here we have simply estimated all powers of $t$ by powers of $x_{*}$. We split the integral in (4.54) into two parts: from 0 to $x_{*}-x_{*}^{3 / 2}$ (part I) and from $x_{*}-x_{*}^{3 / 2}$ to $x_{*}$ (part II). Then
$$(4.54)_{\mathrm{I}} \leqslant 4 x_{*}^{\eta-1} \int_{0}^{x_{*}-x_{*}^{3 / 2}}\left(1-\frac{t}{x_{*}}\right)^{-2} d t \leqslant 4 x_{*}^{\eta-\frac{1}{2}}, \quad(4.54)_{\mathrm{II}} \leqslant 4 x_{*}^{\eta-1} x_{*}^{\frac{3}{2}} x_{*}^{-1}=4 x_{*}^{\eta-\frac{1}{2}} .$$
(5) We can proceed as in (4) except that now not all powers of $t$ are positive. Thus, even though we know that the integral converges because $\left|\dot{G}_{0}(t)\right|=O\left(t^{M}\right)$ with $M>1$, in order to prove an effective inequality via (4.37) and (4.49) we need to impose conditions on these powers of $t$ so that all integrals along the way have an acceptable finite bound. This is where the condition $M>\max \left\{\frac{3}{2}, 2-N\right\}$ comes in: it lets us choose an $\eta \in\left(\frac{1}{2}, M-1\right)$ such that $-2+\eta+N>-1$. With this, and avoiding bounding powers of $t$ by powers of $x_{*}$ if the exponents are negative, we obtain for $x_{0} \leqslant x_{0, \eta}$ that
$$\frac{(5)}{C H\left(x_{*}\right)} \leqslant x_{*}^{1-N} \int_{0}^{x_{*}} t^{-2+\eta+N} \frac{d t}{r(t)^{2}} .$$
If $-2+\eta+N \geqslant 0$, we can finish the proof exactly as in (4). Otherwise we split this integral into three parts: from 0 to $x_{*} / 2$ (part I), where $r(t) \sim 1$, so we can drop $r(t)$ and integrate out the $t^{-2+\eta+N}$ term; and from $x_{*} / 2$ to $x_{*}-x_{*}^{3 / 2}$ (part II) and from $x_{*}-x_{*}^{3 / 2}$ to $x_{*}$ (part III), where $t^{k} \sim x_{*}^{k}$ for all $k \in \mathbb{R}$, so
that we only need to integrate or estimate the $r(t)$ term as in (4). Parts II and III are easily seen to be bounded on the same order as in (4), and part I is even smaller:
$$(4.56)_{\mathrm{I}} \leqslant 16 x_{*}^{1-N} \int_{0}^{\frac{x_{*}}{2}} t^{-2+\eta+N} d t \leqslant \frac{16\left(\frac{1}{2}\right)^{\eta+N-1}}{\eta+N-1} x_{*}^{\eta}$$
This completes the proof of the proposition, and hence of the Main Theorem. \(\square\)

To conclude this paper, we comment on a different geometric problem where the same method can be used to prove sharp estimates of solutions. This concerns the complete Calabi-Yau metrics of [24, Thm 4.2], which also play a role in the recent papers [3, 21] mentioned in the Introduction.

Interestingly, in the Calabi-Yau setting, scaling the Hermitian metric on the underlying line bundle changes the Calabi model potential by terms that are not $O(1)$, and there are no polynomially decaying solutions or supersolutions to the relevant PDE. This means in particular that barrier arguments and expansion methods as in [12, 16, 18, 19, 25] cannot be used. However, it was proved in [15, Cor 1.2] via separation of variables that bounded solutions converge to constants at infinity faster than any power of the metric distance $\rho$. Independently, using an energy decay argument, it was proved in [10, p.366] that this convergence rate is $O\left(\exp \left(-\delta \rho^{\frac{n}{n+1}}\right)\right)$ for some $\delta>0$ in dimension $n$.

In the present paper, all of the above methods (barriers, energy decay, separation of variables) were combined together and fed into a new continuity argument to obtain a very precise description of the solutions in the cuspidal Kähler-Einstein setting. It is then also possible to go back to the Calabi-Yau setting and use a similar approach (energy decay, separation of variables, continuity) to get a sharper estimate of the convergence rate there. In fact, one can now prove that this rate is
$$O\left(\rho^{-\frac{n-2}{2(n+1)}} \exp \left(-\delta(n) \sqrt{\lambda_{1}} \rho^{\frac{n}{n+1}}\right)\right),$$
with $\lambda_{1}$ the first eigenvalue of the Calabi-Yau metric on the divisor, as conjectured in [10, p.366].

\section*{References}
\begin{itemize}
\item[] [1] W. Allard, F. Almgren, On the radial behavior of minimal surfaces and the uniqueness of their tangent cones, Ann. of Math. (2) 113 (1981), 215-265.
\item[] [2] O. Biquard, Métriques d'Einstein à cusps et équations de Seiberg-Witten, J. Reine Angew. Math. 490 (1997), 129-154.
\item[] [3] O. Biquard, H. Guenancia, Degenerating Kähler-Einstein cones, locally symmetric cusps, and the Tian-Yau metric, preprint (2021), arXiv:2108.13318.
\item[] [4] J. Cheeger, G. Tian, On the cone structure at infinity of Ricci flat manifolds with Euclidean volume growth and quadratic curvature decay, Invent. Math. 118 (1994), 493-571.
\item[] [5] S.-Y. Cheng, S.-T. Yau, On the existence of a complete Kähler metric on non-compact complex manifolds and the regularity of Fefferman's equation, Comm. Pure Appl. Math. 33 (1980), 507-544.
\item[] [6] S.-Y. Cheng, S.-T. Yau, Inequality between Chern numbers of singular Kähler surfaces and characterization of orbit space of discrete group of $S U(2,1)$, Complex differential geometry and nonlinear differential equations (Brunswick, ME, 1984), 31-44, Contemp. Math., 49, Amer. Math. Soc., Providence, RI, 1986.
\item[] [7] V. Datar, X. Fu, and J. Song, Kähler-Einstein metric near an isolated log-canonical singularity, preprint (2021), arXiv:2106.05486.
\item[] [8] M. de Borbon, C. Spotti, Local models for conical Kähler-Einstein metrics, Proc. Amer. Math. Soc. 147 (2019), 1217-1230.
\item[] [9] H. Fang, X. Fu, On the construction of a complete Kähler-Einstein metric with negative scalar curvature near an isolated log-canonical singularity, Proc. Amer. Math. Soc. 149 (2021), 3965-3976.
\item[] [10] H.-J. Hein, Gravitational instantons from rational elliptic surfaces, J. Amer. Math. Soc. 25 (2012), 355-393
\item[] [11] H.-J. Hein, V. Tosatti, Higher-order estimates for collapsing Calabi-Yau metrics, Camb. J. Math. 8 (2020), 683-773.
\item[] [12] X. Jiang, Y. Shi, Asymptotic expansions of complete Kähler-Einstein metrics with finite volume on quasi-projective manifolds, preprint (2018), arXiv:1809.06504, to appear in Sci. China Math.
\item[] [13] E. Kähler, Über eine bemerkenswerte Hermitesche Metrik, Abh. Math. Sem. Univ. Hamburg 9 (1933), 173-186.
\item[] [14] R. Kobayashi, Einstein-Kaehler metrics on open algebraic surfaces of general type, Tohoku Math. J. (2) 37 (1985), 43-77.
\end{itemize}
[15] B. Koehler, M. Kühnel, On asymptotics of complete Ricci-flat Kähler metrics on open manifolds, Manuscripta Math. 132 (2010), 431-462.
[16] J. Lee, R. Melrose, Boundary behaviour of the complex Monge-Ampère equation, Acta Math. 148 (1982), 159-192.
[17] N. Mok, Projective algebraicity of minimal compactifications of complex-hyperbolic space forms of finite volume, Perspectives in analysis, geometry, and topology, 331-354, Progr. Math., 296, Birkhäuser/Springer, New York, 2012.
[18] F. Rochon, Z. Zhang, Asymptotics of complete Kähler metrics of finite volume on quasi projective manifolds, Adv. Math. 231 (2012), 2892-2952.
[19] G. Schumacher, Asymptotics of Kähler-Einstein metrics on quasi-projective manifolds and an extension theorem on holomorphic maps, Math. Ann. 311 (1998), 631-645.
[20] L. Simon, Isolated singularities of extrema of geometric variational problems, Harmonic mappings and minimal immersions (Montecatini, 1984), 206-277, Lecture Notes in Math., 1161, Springer, Berlin, 1985.
[21] S. Sun, R. Zhang, Collapsing geometry of hyperkaehler 4-manifolds and applications, preprint (2021), arXiv:2108. 12991.
[22] G. Tian, Canonical metrics in Kähler geometry, Lectures in Mathematics ETH Zürich, Birkhäuser Verlag, Basel, 2000.
[23] G. Tian, S.-T. Yau, Existence of Kähler-Einstein metrics on complete Kähler manifolds and their applications to algebraic geometry, Mathematical aspects of string theory (San Diego, CA, 1986), 574-628, Adv. Ser. Math. Phys., 1, World Sci. Publishing, Singapore, 1987.
[24] G. Tian, S.-T. Yau, Complete Kähler manifolds with zero Ricci curvature. I, J. Amer. Math. Soc. 3 (1990), 579-609.
[25] D. Wu, Higher canonical asymptotics of Kähler-Einstein metrics on quasi-projective manifolds, Comm. Anal. Geom. 14 (2006), 795-845.

Department of Mathematics, University of California, Irvine, CA 92697, USA
Email address: fux6@uci.edu
Mathematisches Institut, WWU Münster, 48149 Münster, Germany
Department of Mathematics, Fordham University, Bronx, NY 10458, USA
Email address: hhein@uni-muenster.de
Department of Mathematics, Fordham University, New York, NY 10023, USA
Email address: xjiang77@fordham.edu