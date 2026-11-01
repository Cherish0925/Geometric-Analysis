---
retention_scope: session
part: 3
total_parts: 4
---

[Part 3/4 of: Monodromy of certain Painlevé–VI transcendents and reflection groups]

Proof. If $y(x)$ is an algebraic function, then it admits an expansion in Puiseux series around 0
$$y(x)=\sum_{k=k_{0}}^{\infty} a_{k} x^{\frac{k}{n}}, \quad k_{0} \in \mathbb{Z}, \quad a_{k_{0}} \neq 0$$
where $n$ is some natural number. As a consequence, for $k_{0} \neq 0$, we have the following relation between the orders of the first and second derivative of $y$ :
$$\mathcal{O}\left(x^{2} y^{\prime \prime}\right)=\mathcal{O}\left(x y^{\prime}\right)=\mathcal{O}(y)=\mathcal{O}\left(x^{\frac{k_{0}}{n}}\right) .$$
We now reduce to the common denominator the $\mathrm{PVI} \mu$ equation and collect together all the terms of the same order in the numerator $\mathcal{N}$, using the rule (2.14). The numerator is
$$\begin{aligned}
\mathcal{N}= & 2 y^{\prime 2} x^{4}-y^{\prime 2} x^{3}-y^{\prime 2} x^{5}+2 y^{\prime 2} x^{2} y-2 y^{\prime} x^{3} y-2 y^{\prime 2} x^{3} y+2 y^{\prime \prime} x^{3} y+2 y^{\prime} x^{4} y-2 y^{\prime 2} x^{4} y- \\
& -4 y^{\prime \prime} x^{4} y+2 y^{\prime 2} x^{5} y+2 y^{\prime \prime} x^{5} y+x y^{2}-2 y^{\prime} x y^{2}-2 x^{2} y^{2}+4 \mu x^{2} y^{2}-4 \mu^{2} x^{2} y^{2}+ \\
& +6 y^{\prime} x^{2} y^{2}-3 y^{\prime 2} x^{2} y^{2}-2 y^{\prime \prime} x^{2} y^{2}-2 y^{\prime} x^{3} y^{2}+6 y^{\prime 2} x^{3} y^{2}+2 y^{\prime \prime} x^{3} y^{2}-2 y^{\prime} x^{4} y^{2}- \\
& -3 y^{\prime 2} x^{4} y^{2}+2 y^{\prime \prime} x^{4} y^{2}-2 y^{\prime \prime} x^{5} y^{2}-8 \mu x y^{3}+8 \mu^{2} x y^{3}+2 y^{\prime} x y^{3}+4 x^{2} y^{3}- \\
& -8 \mu x^{2} y^{3}+8 \mu^{2} x^{2} y^{3}-6 y^{\prime} x^{2} y^{3}+2 y^{\prime \prime} x^{2} y^{3}+4 y^{\prime} x^{3} y^{3}-4 y^{\prime \prime} x^{3} y^{3}+2 y^{\prime \prime} x^{4} y^{3}- \\
& -y^{4}+4 \mu y^{4}-4 \mu^{2} y^{4}-3 x y^{4}+16 \mu x y^{4}-16 \mu^{2} x y^{4}-2 x^{2} y^{4}+4 \mu x^{2} y^{4}- \\
& -4 \mu^{2} x^{2} y^{4}+2 y^{5}-8 \mu y^{5}+8 \mu^{2} y^{5}+2 x y^{5}-8 \mu x y^{5}+8 \mu^{2} x y^{5}-y^{6}+4 \mu y^{6}-4 \mu^{2} y^{6} .
\end{aligned}$$
The first term of the Puiseux series must be chosen in order to kill the lowest term in the numerator of the $\mathrm{PVI} \mu$ equation. If $k_{0}<0$, the lowest term is
$$-y^{6}+4 \mu y^{6}-4 \mu^{2} y^{6}$$
which, for $2 \mu \notin \mathbb{Z}$ cannot be zero for any choice of $a_{0} \neq 0$. Then $k_{0}$ cannot be negative. If $n \geq k_{0}>0$, the lowest order term is
$$2 x^{2} y^{\prime 2} y-2 x y^{\prime} y^{2}-2 x^{2} y^{\prime \prime} y^{2},$$
which is zero for any $y=a_{k_{0}} x^{\frac{k_{0}}{n}}$. For $k_{0}>n$, the lowest order term is
$$-x^{3} y^{\prime 2}+2 x^{3} y^{\prime \prime} y+x y^{2},$$
which cannot be zero. Furthermore, for $k_{0}=0$, the lowest order term in the numerator $\mathcal{N}$ is
$$-a_{0}^{4}\left(a_{0}-1\right)^{2}(2 \mu-1)^{2}$$
and, due to the assumptions $2 \mu \notin \mathbb{Z}$ and $a_{0} \neq 0$, the only possible value of $a_{0}$ is 1. Substituting $y=1+a_{1} x^{\frac{k_{1}}{n}}$, we obtain that the lowest order term in the numerator $\mathcal{N}$ is
$$x^{\frac{2 k_{1}}{n}} a_{1}^{2}\left(k_{1} / n+1-2 \mu\right)\left(k_{1} / n-1+2 \mu\right)$$
that is zero, for generic values of $\mu$, only if $a_{1}$ is 0 . If $\mu=\frac{1}{2} \pm \frac{k_{1}}{2 n}$, we can again repeat the procedure. The numerator will be
$$\begin{aligned}
\hat{\mathcal{N}}= & -4 \hat{\mu}^{2} \hat{y}^{2}-16 \hat{\mu}^{2} \hat{y}^{3}-24 \hat{\mu}^{2} \hat{y}^{4}-16 \hat{\mu}^{2} \hat{y}^{5}-4 \hat{\mu}^{2} \hat{y}^{6}+\hat{y}^{2} x+8 \hat{\mu}^{2} \hat{y}^{2} x+2 \hat{y}^{3} x+24 \hat{\mu}^{2} \hat{y}^{3} x+ \\
& +\hat{y}^{4} x+24 \hat{\mu}^{2} \hat{y}^{4} x+8 \hat{\mu}^{2} \hat{y}^{5} x+2 \hat{y} y^{\prime} x+4 \hat{y}^{2} y^{\prime} x+2 \hat{y}^{3} y^{\prime} x-\hat{y}^{2} x^{2}-4 \hat{\mu}^{2} \hat{y}^{2} x^{2}-2 \hat{y}^{3} x^{2}- \\
& -8 \hat{\mu}^{2} \hat{y}^{3} x^{2}-\hat{y}^{4} x^{2}-4 \hat{\mu}^{2} \hat{y}^{4} x^{2}-6 \hat{y} y^{\prime} x^{2}-12 \hat{y}^{2} y^{\prime} x^{2}-6 \hat{y}^{3} y^{\prime} x^{2}-y^{\prime 2} x^{2}-4 \hat{y} y^{\prime 2} x^{2}- \\
& -3 \hat{y}^{2} y^{\prime 2} x^{2}+2 \hat{y} y^{\prime \prime} x^{2}+4 \hat{y}^{2} y^{\prime \prime} x^{2}+2 \hat{y}^{3} y^{\prime \prime} x^{2}+6 \hat{y} y^{\prime} x^{3}+10 \hat{y}^{2} y^{\prime} x^{3}+4 \hat{y}^{3} y^{\prime} x^{3}+ \\
& +3 y^{\prime 2} x^{3}+10 \hat{y} y^{\prime 2} x^{3}+6 \hat{y}^{2} y^{\prime 2} x^{3}-6 \hat{y} y^{\prime \prime} x^{3}-10 \hat{y}^{2} y^{\prime \prime} x^{3}-4 \hat{y}^{3} y^{\prime \prime} x^{3}-2 \hat{y} y^{\prime} x^{4}- \\
& -2 \hat{y}^{2} y^{\prime} x^{4}-3 y^{\prime 2} x^{4}-3 \hat{y}^{2} y^{\prime 2} x^{4}+6 \hat{y} y^{\prime \prime} x^{4}+8 \hat{y}^{2} y^{\prime \prime} x^{4}+2 \hat{y}^{3} y^{\prime \prime} x^{4}+y^{\prime 2} x^{5}+ \\
& +2 \hat{y} y^{\prime 2} x^{5}-2 \hat{y} y^{\prime \prime} x^{5}-2 \hat{y}^{2} y^{\prime \prime} x^{5}
\end{aligned}$$
where $\hat{\mu}= \pm \frac{k_{1}}{2 n}$ and $\hat{y}=y-1$. Substituting $\hat{y}=a_{1} x^{\frac{k_{1}}{n}}$, the lowest order term in the numerator $\hat{\mathcal{N}}$ is automatically zero. Now, we want to eliminate the next lowest order term. Observe thet, now
$$\mathcal{O}\left(x^{2} y^{\prime \prime}\right)=\mathcal{O}\left(x y^{\prime}\right)=\mathcal{O}(\hat{y})=\mathcal{O}\left(x^{\frac{k_{1}}{n}}\right) .$$
For the sake of definitess, suppose $\frac{1}{2}<\mu \leq 1$, i.e. $\hat{\mu}=\frac{k_{1}}{2 n}<\frac{1}{2}$ (the case $\hat{\mu}=-\frac{k_{1}}{2 n}$ is analogous). The next lowest order terms in the numerator $\hat{\mathcal{N}}$ are
$$-16 \hat{\mu}^{2} \hat{y}^{3}+4 x \hat{y}^{2} y^{\prime}-4 x^{2} \hat{y} y^{\prime 2}+4 x^{2} \hat{y}^{2} y^{\prime \prime}+x \hat{y}^{2}+8 x \hat{\mu}^{2} \hat{y}^{2}-6 x^{2} \hat{y} y^{\prime}+3 x^{3} y^{\prime 2}-6 x^{3} \hat{y} y^{\prime \prime}$$
To eliminate them, we substitute $y=1+a_{1} x^{\frac{k_{1}}{n}}+a_{1} y^{\frac{k_{2}}{n}}$, for some $k_{2}>k_{1}$. The above terms give
$$-4 a_{1}^{3}\left(\frac{k_{1}}{n}\right)^{2} x^{3 \frac{k_{1}}{n}}+\mathcal{O}\left(x^{1+2 \frac{k_{1}}{n}}\right)$$
that is zero if and only of $a_{1}=0$. So we obtain the forbidden solution $y(x) \equiv 1$. So, $k_{0}$ can not be zero, and $y(x)$ satisfies (2.13) with $0<l=\frac{k_{0}}{n} \leq 1$, namely $0 \leq \sigma_{0}<1$. QED

In the above lemma we have seen the expected asymptotic behaviour of the algebraic solutions. We now state the main result of this section, which is more general, namely it holds also for non algebraic solutions.

Theorem 2.2. For any pair of values $\left(a_{0}, \sigma_{0}\right), 0 \leq \sigma_{0}<1$, there exists a unique branch of the solution of PVI $\mu$, for a fixed $\mu$, with the asymptotic behaviour
$$y(x)=a_{0} x^{1-\sigma_{0}}\left(1+x^{\varepsilon} f(x)\right) \quad \text { as } \quad x \rightarrow 0,$$
for some $\varepsilon>0$ and $f(x)$ smooth function such that $\lim _{x \rightarrow 0} f(x)=$ const.
In order that $x^{1-\sigma_{0}}$ is well defined, we have to make some cut in the complex plane. From now on, we cut along the line $\arg x=\varphi$ for some $\varphi$.

Remark 2.2. Theorem 2.2 can be proved also for complex values of the index $\sigma_{0}$, provided that $0 \leq \operatorname{Re} \sigma_{0}<1$. For algebraic solutions the index $\sigma_{0}$ must be a rational number. Because of this, we consider only real indices.
2.1.2. Proof of the existence. First of all we state the existence of solutions of the Schlesinger equations with a particular asymptotic behaviour. The following result will play an important role also in Section 2.3.

Lemma 2.2 (Sato-Miwa-Jimbo). Given three constant matrices $A_{i}^{0}, i=0,1, x$ with zero eigenvalues such that $\Lambda=A_{0}^{0}+A_{x}^{0}$ has eigenvalues $\pm \frac{\sigma}{2}, 0 \leq \sigma<1$, and $A_{1}^{0}=-\Lambda-A_{\infty}$, in any sector of $\overline{\mathbb{C}}$ containing none of the branch cuts, and sufficiently close to 0, there exists a solution of the Schlesinger equations that satisfy
$$\begin{aligned}
\left|A_{1}(x)-A_{1}^{0}\right| \leq K|x|^{1-\sigma^{\prime}} \quad\left|x^{-\Lambda}\left(A_{1}(x)-A_{1}^{0}\right) x^{\Lambda}\right| & \leq K|x|^{1-\sigma^{\prime}} \\
\left|x^{-\Lambda} A_{0}(x) x^{\Lambda}-A_{0}^{0}\right| \leq K|x|^{1-\sigma^{\prime}} \quad\left|x^{-\Lambda} A_{x}(x) x^{\Lambda}-A_{x}^{0}\right| & \leq K|x|^{1-\sigma^{\prime}},
\end{aligned}$$
where $K$ is some positive constant and $1>\sigma^{\prime}>\sigma$.
We want to show that it is possible to choose $A_{0,1, x}$ and $\Lambda$ such that the corresponding solution $y(x)$ of the Painlevé VI equation obtained via (2.7) has the asymptotic behaviour (2.15). Let us consider an arbitrary constant matrix $\Lambda$ with eigenvalues $\pm \frac{\sigma}{2}$; let $T$ be the diagonalizing matrix of $\Lambda$, namely
$$\Lambda=T\left(\begin{array}{cc}
\frac{\sigma}{2} & 0 \\
0 & -\frac{\sigma}{2}
\end{array}\right) T^{-1} .$$
Now, we choose $A_{1}^{0}=-A_{\infty}-\Lambda$ and $A_{0, x}^{0}$ such that $A_{0}^{0}+A_{x}^{0}=\Lambda$, namely
$$A_{0}^{0}=\frac{1}{2} \Lambda+F, \quad A_{x}^{0}=\frac{1}{2} \Lambda-F$$
for some constant matrix $F$. Then:
$$T^{-1} A_{0}^{0} T=\left(\begin{array}{cc}
\frac{\sigma}{4} & 0 \\
0 & -\frac{\sigma}{4}
\end{array}\right)+E, \quad T^{-1} A_{x}^{0} T=\left(\begin{array}{cc}
\frac{\sigma}{4} & 0 \\
0 & -\frac{\sigma}{4}
\end{array}\right)-E,$$
where we can choose $E=\left(\begin{array}{cc}0 & \frac{b \sigma}{4} \\ \frac{-\sigma}{4 b} & 0\end{array}\right)$, for some non-zero constant $b$. With this choice of $E, A_{0}$ and $A_{x}$ have zero eigenvalues. Using Lemma 2.2, we obtain that, as $x \rightarrow 0$ :
$$A_{0, x} \rightarrow T\left(\begin{array}{cc}
x^{\frac{\sigma}{2}} & 0 \\
0 & x^{\frac{-\sigma}{2}}
\end{array}\right)\left[\left(\begin{array}{cc}
\frac{\sigma}{4} & 0 \\
0 & -\frac{\sigma}{4}
\end{array}\right) \pm\left(\begin{array}{cc}
0 & \frac{b \sigma x^{\sigma}}{4} \\
\frac{-\sigma x^{-\sigma}}{4 b} & 0
\end{array}\right)\right]\left(\begin{array}{cc}
x^{\frac{-\sigma}{2}} & 0 \\
0 & x^{\frac{\sigma}{2}}
\end{array}\right) T^{-1},$$
and
$$A_{1} \rightarrow-A_{\infty}-\Lambda .$$
Substituting such asymptotic behaviors in the relation (2.7), taking $T_{12}, T_{11} \neq 0$ we obtain:
$$y(x) \sim-\frac{T_{12} x^{1-\sigma}}{4 b T_{11}} ;$$
we are now free to choose the arbitrary constants $b, T_{11}, T_{12}, \sigma$ in such a way that $-\frac{T_{12}}{4 b T_{11}}=$ $a_{0}, \sigma=\sigma_{0}$, for any fixed $a_{0}$ and $\sigma_{0}$.
Remark 2.3. Other existence results for $\sigma \in \mathbb{C} \backslash]-\infty, 0] \cup[1,+\infty[ \}$ can be found in [IKSY] and [S1], [S2], [S3]. For indices with $\operatorname{Re} \sigma \notin[0,1]$, the asymptotics obtained in these papers are valid in more complicated domains near 0.
2.1.3. Proof of the uniqueness. Now we prove that the solution $y(x), x \in \mathcal{B}(0, r)$, of Painlevé VI equation such that it satisfies (2.15) for some given constants $a_{0}$ and $\sigma_{0} \in[0,1)$, is uniquely determined by $a_{0}$ and $\sigma_{0}$. Here $\mathcal{B}(0, r)=\{x| | x \mid \leq r, \arg x \neq \varphi, x \neq 0\}$.
The proof is based on the fact that Painlevé VI is equivalent to the following reduced Schlesinger equations (1.17):
$$\begin{gathered}
\dot{q}=\frac{(q-1) q+2 p(q-1) q(q-x)}{(x-1) x}, \\
\dot{p}=\frac{-p^{2}\left(x-2 q-2 x q+3 q^{2}\right)-p(2 q-1)-(1-\mu) \mu}{(x-1) x},
\end{gathered}$$
where:
$$q=y, \quad p=\frac{x(x-1) \dot{y}-y(y-1)}{2(y-x) y(y-1)},$$
and the dot means the derivative $\frac{\mathrm{d}}{\mathrm{d} x}$ We shall prove the local uniqueness of the solutions of the Hamiltonian system with the following asymptotic behaviour
$$q(x) \sim a x^{l}+x^{l+\varepsilon} f(x) \quad p(x) \sim \frac{l-1}{2 a} \frac{1}{x^{l}}+\frac{x^{\varepsilon} g(x)}{x^{l}}$$
where $l=1-\sigma_{0}, a=a_{0}, \varepsilon>0$ and $f(x)$ and $g(x)$ are some smooth functions in $\mathcal{B}(0, r)$ which tend to zero as $x \rightarrow 0$.

This is equivalent to show the theorem. In fact, from the uniqueness of $q$ it follows trivially the uniqueness of $y$. The following lemma holds true:

Lemma 2.3. The estimates (2.20) on the asymptotic behaviour of $(q(x), p(x))$ are a consequence of (2.15).

Proof. Since $q=y$, the assertion on $y$ is obvious due to the hypothesis (2.15). Concerning $p$, we use its definition
$$p=\frac{x(x-1) \dot{y}-y(y-1)}{2(y-x) y(y-1)}$$
and by a straightforward computation we show (2.20) for p. QED

We now distinguish two cases: $0<l<1$, and $l=1$. Let us consider the former case; it is convenient to introduce the new variables $(\tilde{q}, \tilde{p})$
$$\tilde{q}=\frac{y}{x^{l}} \quad \tilde{p}=x^{l} p ;$$
which have a similar asymptotic behaviour
$$\tilde{q}(x)=a+x^{\varepsilon} f(x) \quad \tilde{p}(x)=\frac{l-1}{2 a}+x^{\varepsilon} g(x),$$
and the equations of the motion become
$$\begin{aligned}
\dot{\tilde{q}} & =f_{q}\left(\tilde{p}, \tilde{q}, x, x^{l}\right), \\
\dot{\tilde{p}} & =f_{p}\left(\tilde{p}, \tilde{q}, x, x^{l}\right),
\end{aligned}$$
with
$$f_{q}=\frac{-\tilde{q}(l-1-2 \tilde{p} \tilde{q})}{x}-\frac{\tilde{q}(1+2 \tilde{p} \tilde{q})}{x^{1-l}}+\frac{\tilde{q}(1+4 \tilde{p} \tilde{q})-2 x^{-l} \tilde{p} \tilde{q}-x^{l} \tilde{q}^{2}(1+2 \tilde{p} \tilde{q})}{1-x},$$
and
$$f_{p}=\frac{\tilde{p}(l-1-2 \tilde{p} \tilde{q})}{x}+\frac{\mu-\mu^{2}+2 \tilde{p} \tilde{q}+3 \tilde{p}^{2} \tilde{q}^{2}}{x^{1-l}}+\frac{\frac{\tilde{p}^{2}}{x^{l}}-\tilde{p}(1+4 \tilde{p} \tilde{q})+x^{l}\left(\mu-\mu^{2}+2 \tilde{p} \tilde{q}+3 \tilde{p}^{2} \tilde{q}^{2}\right)}{1-x} .$$
We want to prove the uniqueness of the solution $(\tilde{q}, \tilde{p})$ of (2.22), satisfying (2.21) for $x \in \mathcal{B}(0, r)$, in the ball $\left\|\tilde{p}-\frac{l-1}{2 a}\right\|,\|\tilde{q}-a\| \leq C_{r}$, for a constant $C_{r}$ vanishing when the radius $r \rightarrow 0$. Here $\|f\|=\sup _{\mathcal{B}(0, r)}|f(x)|$. Let us suppose that there are two solutions $\left(\tilde{q}_{1}, \tilde{p}_{1}\right)$ and $\left(\tilde{q}_{2}, \tilde{p}_{2}\right)$ of the system (2.22), satisfying (2.21). Then, if we define $\mathrm{X}=\binom{\tilde{q}_{1}-\tilde{q}_{2}}{\tilde{p}_{1}-\tilde{p}_{2}}$, we obtain, as a consequence of (2.21), that the following limits exist
$$\lim _{|x| \rightarrow 0, \arg (x)=\vartheta} \frac{\mathrm{X}^{(i)}(x)}{|x|^{\varepsilon}}=0, \quad i=1,2,$$
for some $0<\varepsilon, \mathrm{X}^{(i)}$ being the i-th component of X. Moreover, X satisfies the following
$$\mathrm{X}^{\prime}=\binom{\frac{\left[1-l+2 \tilde{p}_{1}\left(\tilde{q}_{1}+\tilde{q}_{2}\right)\right]\left(\tilde{q}_{1}-\tilde{q}_{2}\right)+2 \tilde{q}_{2}^{2}\left(\tilde{p}_{1}-\tilde{p}_{2}\right)}{x}+\frac{\Delta \mathrm{Q}_{1}}{x^{1-l}}+\frac{\Delta \mathrm{Q}_{2}}{x^{l}}+\Delta \mathrm{Q}_{3}}{\frac{\left[l-1-2 \tilde{q}_{2}\left(\tilde{p}_{1}+\tilde{p}_{2}\right)\right]\left(\tilde{p}_{1}-\tilde{p}_{2}\right)-2 \tilde{p}_{1}^{2}\left(\tilde{q}_{1}-\tilde{q}_{2}\right)}{x}+\frac{\Delta \mathrm{P}_{1}}{x^{1-l}}+\frac{\Delta \mathrm{P}_{2}}{x^{l}}+\Delta \mathrm{P}_{3}},$$
where
$$\Delta \mathrm{Q}_{i}=Q_{i}\left(\tilde{q}_{1}, \tilde{p}_{1}, x\right)-Q_{i}\left(\tilde{q}_{2}, \tilde{p}_{2}, x\right), \quad \text { and } \quad \Delta \mathrm{P}_{i}=P_{i}\left(\tilde{q}_{1}, \tilde{p}_{1}, x\right)-P_{i}\left(\tilde{q}_{2}, \tilde{p}_{2}, x\right),$$
$$\begin{aligned}
& Q_{1}=\tilde{q}(1+2 \tilde{p} \tilde{q}), Q_{2}=-2 \tilde{p} \tilde{q}, Q_{3}=\frac{\tilde{q}(1+4 \tilde{p} \tilde{q})-2 x^{1-l} \tilde{p} \tilde{q}-x^{l} \tilde{q}^{2}(1+2 \tilde{p} \tilde{q})}{1-x}, P_{1}=\mu-\mu^{2}+2 \tilde{p} \tilde{q}+3 \tilde{p}^{2} \tilde{q}^{2}, \\
& P_{2}=\tilde{p}^{2}, P_{3}=\frac{p^{2} x^{1-l}-\tilde{p}(1+4 \tilde{p} \tilde{q})+x^{l}\left(\mu-\mu^{2}+2 \tilde{p} \tilde{q}+3 \tilde{p}^{2} \tilde{q}^{2}\right)}{1-x} .
\end{aligned}$$

We want to prove that, under the hypothesis (2.23), $\mathrm{X} \equiv 0$ (this is equivalent to prove our theorem). Performing the constant linear transformation $\mathrm{X}=\mathrm{TZ}$, where
$$\mathrm{T}=\left(\begin{array}{cc}
1 & 0 \\
\frac{1-l}{2 a^{2}} & \frac{1}{2 a^{2}}
\end{array}\right),$$
we obtain
$$\mathrm{Z}^{\prime}=\binom{\frac{\left[1-l+2 \tilde{p}_{1}\left(\tilde{q}_{1}+\tilde{q}_{2}\right)\right]\left(\tilde{q}_{1}-\tilde{q}_{2}\right)+2 \tilde{q}_{2}^{2}\left(\tilde{p}_{1}-\tilde{p}_{2}\right)}{x}+\frac{\Delta \mathrm{Q}_{1}}{x^{1-l}}+\frac{\Delta \mathrm{Q}_{2}}{x^{l}}+\Delta \mathrm{Q}_{3}}{\frac{2 a^{2} G\left(\tilde{p}_{1}, \tilde{p}_{2}, \tilde{q}_{1}, \tilde{q}_{2}\right)}{x}+\frac{2 a^{2} \Delta \mathrm{P}_{1}+(l-1) \Delta \mathrm{Q}_{1}}{x^{1-l}}+\frac{2 a^{2} \Delta \mathrm{P}_{2}+(l-1) \Delta \mathrm{Q}_{2}}{x^{l}}+2 a^{2} \Delta \mathrm{P}_{3}+(l-1) \Delta \mathrm{Q}_{3}}$$
where
$$\begin{aligned}
G\left(\tilde{p}_{1}, \tilde{p}_{2}, \tilde{q}_{1}, \tilde{q}_{2}\right)= & {\left.\left[l-1-2 \tilde{q}_{2}\left(\tilde{p}_{1}+\tilde{p}_{2}\right)\right]\left(\tilde{p}_{1}-\tilde{p}_{2}\right)-2 \tilde{p}_{1}^{2}\left(\tilde{q}_{1}-\tilde{q}_{2}\right)\right\}+ } \\
& +(l-1)\left\{\left[1-l+2 \tilde{p}_{1}\left(\tilde{q}_{1}+\tilde{q}_{2}\right)\right]\left(\tilde{q}_{1}-\tilde{q}_{2}\right)+2 \tilde{q}_{2}^{2}\left(\tilde{p}_{1}-\tilde{p}_{2}\right),\right.
\end{aligned}$$
and, from (2.23):
$$\lim _{|x| \rightarrow 0, \arg (x)=\vartheta} \frac{\mathrm{Z}^{(i)}(x)}{|x|^{\varepsilon}}=0, \quad i=1,2 .$$
In order to prove that $\mathrm{Z} \equiv 0$, we fix any direction in the complex plane $\arg (x)=\vartheta$ for some fixed $\vartheta$, and we consider the real variable $t=|x|$. Then we define:
$$\mathrm{V}^{(i)}(t):=\left|Z^{(i)}(x)\right| .$$
We want to prove that the assumption $\mathrm{V}^{(i)}\left(t_{0}\right) \neq 0$ for some $t_{0}>0$ leads to a cotradiction. To this aim we prove a differential inequality for the right derivative $D_{+} \mathrm{V}^{(i)}$ of $V^{(i)}(t)$. Since $D_{+} \mathrm{V}^{(i)} \leq\left|\mathrm{Z}^{(i)^{\prime}}\right|$, to obtain such a differential inequality it is enough to estimate from above the modulus of the components of the right-hand-side of (2.24). To this aim we notice that all the polynomials $Q_{i}, P_{i}$ have the form:
$$Q_{i}=\sum_{k, n=0}^{3} a_{k, n}^{i} \tilde{p}^{n} \tilde{q}^{k}, \quad P_{i}=\sum_{k, n=0}^{3} b_{k, n}^{i} \tilde{p}^{n} \tilde{q}^{k},$$
with $a_{k, n}(x), b_{k, n}(x)$ regular functions $x \in \mathcal{B}(0, r)$. As a consequence, we obtain, in the ball $\left\|\tilde{p}-\frac{l-1}{2 a}\right\|,\|\tilde{q}-a\| \leq C_{r}$, the estimates:
$$\left|\Delta \mathrm{Q}_{i}\right|, \quad\left|\Delta \mathrm{P}_{i}\right| \leq c_{1}^{i}\left|\mathrm{Z}^{(1)}\right|+c_{2}^{i}\left|\mathrm{Z}^{(2)}\right|$$
for some positive constants $c_{1}^{i}, c_{2}^{i}$. In fact
$$\begin{aligned}
\left|\Delta Q_{i}\right| & =\left|\sum_{k, n} a_{k, n}\left[\tilde{q}_{1}^{k}\left(\tilde{p}_{1}^{n}-\tilde{p}_{2}^{n}\right)+\tilde{p}_{2}^{n}\left(\tilde{q}_{1}^{k}-\tilde{q}_{2}^{k}\right)\right]\right| \leq\left\{\sum_{k=0,1,2} C_{r}^{(1)^{k}}\left(\left\|a_{k, 1}\right\|+2 C_{r}^{(2)}\left\|a_{k, 2}\right\|\right)\right\} \\
& \cdot\left|\tilde{p}_{1}-\tilde{p}_{2}\right|+\left\{\sum_{n=0,1,2,3} C_{r}^{(2)^{n}}\left(\left\|a_{1, n}\right\|+2 C_{r}^{(1)}\left\|a_{2, n}\right\|+3 C_{r}^{(1)^{2}}\left\|a_{3, n}\right\|\right)\right\} \cdot\left|\tilde{q}_{1}-\tilde{q}_{2}\right|,
\end{aligned}$$
where $C_{r}^{(1)}=C_{r}+2|a|$ and $C_{r}^{(2)}=C_{r}+\frac{1-l}{|a|}$. We obtain (2.26) observing that $\left|\tilde{q}_{1}-\tilde{q}_{2}\right|$, $\left|\tilde{p}_{1}-\tilde{p}_{2}\right|$ are related to $\left|Z^{(1)}\right|,\left|Z^{(2)}\right|$ by the constant linear transformation $T$.
For the terms of order $\mathcal{O}\left(\frac{1}{x}\right)$ in (2.24) we have:
$$\begin{aligned}
\frac{\left|\left[1-l+2 \tilde{p}_{1}\left(\tilde{q}_{1}+\tilde{q}_{2}\right)\right]\left(\tilde{q}_{1}-\tilde{q}_{2}\right)+2 \tilde{q}_{2}^{2}\left(\tilde{p}_{1}-\tilde{p}_{2}\right)\right|}{|x|} \leq & \frac{\left|-(1-l)\left(\tilde{q}_{1}-\tilde{q}_{2}\right)+2 a^{2}\left(\tilde{p}_{1}-\tilde{p}_{2}\right)\right|}{|x|}+ \\
& +\frac{C_{r}^{(3)}\left|\tilde{q}_{1}-\tilde{q}_{2}\right|}{\left|x^{1-\varepsilon}\right|}+\frac{C_{r}^{(4)}\left|\tilde{p}_{1}-\tilde{p}_{2}\right|}{\left|x^{1-\varepsilon}\right|},
\end{aligned}$$
and
$$\begin{aligned}
& \left.\frac{1}{x} \right\rvert\, 2 a^{2}\left\{\left[l-1-2 \tilde{q}_{2}\left(\tilde{p}_{1}+\tilde{p}_{2}\right)\right]\left(\tilde{p}_{1}-\tilde{p}_{2}\right)-2 \tilde{p}_{1}^{2}\left(\tilde{q}_{1}-\tilde{q}_{2}\right)\right\}+(l-1)\left\{\left[1-l+2 \tilde{p}_{1}\left(\tilde{q}_{1}+\tilde{q}_{2}\right)\right] \cdot\right. \\
& \left.\left(\tilde{q}_{1}-\tilde{q}_{2}\right)+2 \tilde{q}_{2}^{2}\left(\tilde{p}_{1}-\tilde{p}_{2}\right)\right\} \left.\left|\leq \frac{C_{r}^{(5)}}{\left|x^{1-\varepsilon}\right|}\right| \tilde{q}_{1}-\tilde{q}_{2}\left|+\frac{C_{r}^{(6)}}{\left|x^{1-\varepsilon}\right|}\right| \tilde{p}_{1}-\tilde{p}_{2} \right\rvert\,,
\end{aligned}$$
for some positive constants $C_{r}^{(3)}, \ldots, C_{r}^{(6)}$. Let us prove (2.27):
$$\begin{aligned}
& \frac{\left|\left[1-l+2 \tilde{p}_{1}\left(\tilde{q}_{1}+\tilde{q}_{2}\right)\right]\left(\tilde{q}_{1}-\tilde{q}_{2}\right)+2 \tilde{q}_{2}^{2}\left(\tilde{p}_{1}-\tilde{p}_{2}\right)\right|}{|x|} \leq \frac{\left|-(1-l)\left(\tilde{q}_{1}-\tilde{q}_{2}\right)+2 a^{2}\left(\tilde{p}_{1}-\tilde{p}_{2}\right)\right|}{|x|}+ \\
& +\frac{\left|2 a g_{1}(x)+\frac{l-1}{a}\left(f_{1}(x)+f_{2}(x)\right)+x^{\varepsilon} g_{1}(x)\left(f_{1}(x)+f_{2}(x)\right)\right|}{\left|x^{1-\varepsilon}\right|}\left|\tilde{q}_{1}-\tilde{q}_{2}\right|+ \\
& +\frac{\left|2 f_{2}^{2}(x) x^{\varepsilon}+4 a f_{2}(x)\right|}{\left|x^{1-\varepsilon}\right|}\left|\tilde{p}_{1}-\tilde{p}_{2}\right| \leq \frac{\left|-(1-l)\left(\tilde{q}_{1}-\tilde{q}_{2}\right)+2 a^{2}\left(\tilde{p}_{1}-\tilde{p}_{2}\right)\right|}{|x|}+ \\
& +\frac{C_{r}^{(3)}}{\left|x^{1-\varepsilon}\right|}\left|\tilde{q}_{1}-\tilde{q}_{2}\right|+\frac{C_{r}^{(4)}}{\left|x^{1-\varepsilon}\right|}\left|\tilde{p}_{1}-\tilde{p}_{2}\right|,
\end{aligned}$$
for some positive constants $C_{r}^{(3)}$ and $C_{r}^{(4)}$. The proof of (2.28) is analogous. From the estimates (2.26), (2.27), (2.28), we obtain:
$$\binom{\left|\mathrm{Z}^{(1)^{\prime}}\right|}{\left|\mathrm{Z}^{(2)^{\prime}}\right|} \leq\left(\frac{1}{|x|}\left(\begin{array}{ll}
0 & 1 \\
0 & 0
\end{array}\right)+\frac{\mathrm{A}_{1}}{\left|x^{1-l}\right|}+\frac{\mathrm{A}_{2}}{\left|x^{l}\right|}+\frac{\mathrm{A}_{3}}{\left|x^{1-\varepsilon}\right|}+\mathrm{A}_{4}\right)\binom{\left|\mathrm{Z}^{(1)}\right|}{\left|\mathrm{Z}^{(2)}\right|}$$
for some constant matrices $\mathrm{A}_{1}, \mathrm{~A}_{2}, \mathrm{~A}_{3}$ and $\mathrm{A}_{4}$ (Here we mean $\leq$ component by component). Finally, choosing $\tilde{l}=\max \{1-\varepsilon, 1-l, l\}$, we obtain from (2.29):
$$\binom{D_{+, t} \mathrm{~V}^{(1)}}{D_{+, t} \mathrm{~V}^{(2)}} \leq\left(\frac{1}{t}\left(\begin{array}{ll}
0 & 1 \\
0 & 0
\end{array}\right)+\frac{\tilde{\mathrm{A}}}{t^{\tilde{l}}}+\mathrm{A}_{4}\right)\binom{\mathrm{V}^{(1)}}{\mathrm{V}^{(2)}},$$
where $\tilde{\mathrm{A}}=\mathrm{A}_{1}+\mathrm{A}_{2}+\mathrm{A}_{3}$ and $D_{+, t}$ is the right derivative w.r.t. $t$.
We perform the following change of variable $t^{1-\tilde{l}}=z$. The differential inequality for V in the new variable $z$ is
$$D_{+, z} \mathrm{~V} \leq\left(\frac{1}{z}\left(\begin{array}{ll}
0 & 1 \\
0 & 0
\end{array}\right) \frac{1}{1-\tilde{l}}+\mathrm{A}(z)\right) \mathrm{V}, \quad \text { with } \quad \mathrm{A}(z)=\frac{\tilde{\mathrm{A}}}{1-\tilde{l}}+\frac{\mathrm{A}_{4}}{1-\tilde{l}} z^{\frac{\tilde{l}}{1-l}},$$
where $D_{+, z}$ is the right derivative w.r.t. $z$. To show that $\mathrm{Z}=0$ we use the following:

Comparison Theorem. Let us consider the following systems of $n$ first order ODEs in the real variable $z \in(0, a]$, for some $a>0$ :
$$\begin{array}{rlr}
D_{+} \mathrm{V}^{(i)} \leq F^{(i)}(z, \mathrm{~V}), & \mathrm{V}^{(i)}\left(x_{0}\right)=\mathrm{V}_{0}^{(i)}, & i=1, . ., n \\
\frac{\mathrm{dU}^{(i)}}{\mathrm{d} z}=F^{(i)}(z, \mathrm{U}), & \mathrm{U}^{(i)}\left(x_{0}\right)=\mathrm{U}_{0}^{(i)}, & i=1, . ., n
\end{array}$$
where $F^{(i)}(z, \mathrm{U})$ are continuous functions in $z \in(0, a],\left\|\mathrm{U}-\mathrm{U}_{0}\right\|<b$, non-decreasing in $\mathrm{U}^{(i)}$. If $\mathrm{V}_{0}^{(i)} \geq \mathrm{U}_{0}^{(i)}$, for $i=1, . . n$, then $\mathrm{V}^{(i)}(z) \geq \mathrm{U}^{(i)}(z)$, for every $0<z \leq z_{0}, i=1, . . n$.

For the proof see [Lak].
We now apply Comparison Theorem to show that the assumption $Z\left(t_{0}\right) \neq 0$ for some $t_{0}>0$ leads to a contradiction. Observe that by definition $\tilde{l} \geq 1$, then V satisfies (2.31) with $\mathrm{V}_{0}^{(i)}>0$ and $F$ linear in V given by:
$$F(z, \mathrm{~V})=\left(\frac{1}{z}\left(\begin{array}{ll}
0 & 1 \\
0 & 0
\end{array}\right) \frac{1}{1-\tilde{l}}+\frac{\tilde{\mathrm{A}}}{1-\tilde{l}}+\frac{\mathrm{A}_{4}}{1-\tilde{l}} z\right) \mathrm{V} .$$
By Comparison Theorem, for any solution of (2.32) with $\mathrm{U}^{(i)}\left(z_{0}\right)=\mathrm{V}_{0}^{(i)}$, and $F(z, \mathrm{U})$ of the form (2.33), we have $\mathrm{V}^{(i)}(z) \geq \mathrm{U}^{(i)}(z)$, for every $0<z \leq z_{0}, i=1,2$. Moreover by standard arguments it is possible to take U in such a way that $\mathrm{U}^{(i)}(z) \geq 0$ and to continue the functions U, V to $z=0$ preserving the relation:
$$0 \leq \mathrm{U}^{(i)}(z) \leq \mathrm{V}^{(i)}(z) .$$
Thus, by (2.25) we obtain that U must satisfy
$$\lim _{z \rightarrow 0} \frac{\mathrm{U}^{(i)}(z)}{z^{\frac{\varepsilon}{(1-\bar{l})}}}=0, \quad i=1,2 .$$
Now, we use the following lemma:
Lemma 2.4. The only solution U of (2.32) with $F(z, \mathrm{U})$ given by (2.33) satisfying (2.34) is $\mathrm{U} \equiv 0$,

Proof. Any non-zero solution of (2.32) with $F(z, \mathrm{U})$ of the form (2.33) is given by
$$\mathrm{U}(z)=T(z) z^{\left(\begin{array}{cc}
0 & \frac{1}{1-\bar{l}} \\
0 & 0
\end{array}\right)}$$
where $T(z)$ is a holomorphic matrix function, $T(z)=\left(\begin{array}{cc}1 & 0 \\ 0 & 1\end{array}\right)+\mathcal{O}(z)$. Now it is obvious that (2.35) does not satisfy (2.34). Thus $\mathrm{U} \equiv 0$, as we wanted to prove. \(\square\)

Using the above lemma, we obtain $\mathrm{U}_{0}^{(i)}=\mathrm{V}_{0}^{(i)}=0$, that contradicts the assumption $\mathrm{V}_{0}^{(i)}=\neq 0$. This concludes the proof of the uniqueness in the case $0<l<1$.

Let us briefly explain how to prove the uniqueness in the case $l=1$. Since the procedure is essentially the same as before, we shall skip the details. First of all we introduce the new variables $(\tilde{q}, \tilde{p})$ :
$$\tilde{q}(x)=\frac{q(x)}{x} \sim a+x^{\varepsilon} f(x) \quad \tilde{p}(x)=p(x)-\mu(1-\mu) \sim x^{\varepsilon} g(x)$$
which satisfy the equations of the motion:
$$\begin{aligned}
& \dot{\tilde{q}}=Q_{1}(\tilde{q}, \tilde{p})+\frac{1}{x-1} Q_{2}(\tilde{q}, \tilde{p}) \\
& \dot{\tilde{p}}=-\frac{\tilde{p}}{x}+P_{1}(\tilde{q}, \tilde{p})+\frac{1}{x-1} P_{2}(\tilde{q}, \tilde{p})
\end{aligned}$$
where $Q_{1}(\tilde{q}, \tilde{p})=2\left(\mu-\mu^{2}+\tilde{p}\right)(\tilde{q}-1) \tilde{q}^{2}, Q_{2}(\tilde{q}, \tilde{p})=\tilde{q}(\tilde{q}-1)[1+(2 \mu(1-\mu)+2 \tilde{p})(\tilde{q}-1)]$, $P_{1}(\tilde{q}, \tilde{p})=\left(\mu-\mu^{2}+\tilde{p}\right)^{2}(2-3 \tilde{q}) \tilde{q}-\mu(1-\mu)$, and $P_{2}(\tilde{q}, \tilde{p})=\tilde{p}+\left(\mu-\mu^{2}+\tilde{p}\right)^{2}\left(4 \tilde{q}-3 \tilde{q}^{2}-\right.$ $1)-2\left(\mu-\mu^{2}+\tilde{p}\right) \tilde{q}$. Then, if we define X as before we obtain
$$\mathrm{X}^{\prime}=\binom{\Delta Q_{1}+\frac{\Delta Q_{2}}{x-1}}{-\frac{\tilde{p}_{1}-\tilde{p}_{2}}{x}+\Delta P_{1}+\frac{\Delta P_{2}}{x-1}}$$
that gives rise to the differential inequality:
$$\left|\mathrm{X}^{\prime}\right| \leq\left(\left(\begin{array}{ll}
0 & 0 \\
0 & 1
\end{array}\right) \frac{1}{|x|}+\mathrm{A}_{1}+\frac{\mathrm{A}_{2}}{|x-1|}\right)|\mathrm{X}|$$
for some constant matrices $\mathrm{A}_{1}$ and $\mathrm{A}_{2}$. Obviously X satisfies (2.23) with any $0<\varepsilon<1$. Again we apply Comparison Theorem to $\mathrm{V}:=\binom{\left|\mathrm{X}^{(1)}\right|}{\left|\mathrm{X}^{(2)}\right|}$ along any fixed direction on the complex plane. We take $x$ such that $\arg (x)=\vartheta$ for some fixed $\vartheta$ and define $t=|x|$. V satisfies (2.31) with:
$$F(t, \mathrm{~V})=\left(\frac{1}{t}\left(\begin{array}{ll}
0 & 0 \\
0 & 1
\end{array}\right)+\mathrm{A}_{1}+\frac{\mathrm{A}_{2}}{t-1}\right) \mathrm{V} .$$
If $\mathrm{V}_{0}^{(i)}>0$ then, thanks to Comparison Theorem, it is possible to take a solution U of (2.32), with $\mathrm{U}_{0}^{(i)}=\mathrm{V}_{0}^{(i)}, i=1,2$, such that
$$0 \leq \mathrm{U}^{(i)}(t) \leq \mathrm{V}^{(i)}(t),$$
thus $\mathrm{U}^{(i)}$ satisfies (2.34). The general solution of (2.32) is
$$\mathrm{U}=\mathrm{U}_{0}\left(\left(\begin{array}{ll}
1 & 0 \\
0 & t
\end{array}\right)+\mathcal{O}\left(t^{2}\right)\right)$$
that satisfies (2.34) iff $\mathrm{U}_{0}=0$, namely $\mathrm{U} \equiv 0$ that is absurd. This concludes the proof of the uniqueness. \(\square\)
2.1.4. Asymptotic behaviour of the solutions of the Schlesinger equations. An important corollary to Theorem 2.2 is the following:

Theorem 2.3. The solutions of the Schlesinger equations $A_{0,1, x}(x)$ corresponding to the solution of Painlevé VI equation with asymptotic behaviour (2.15) must satisfy the relations (2.16) and (2.17).
Proof. Let us consider the solution $y(x)$ of Painlevé VI equation with asymptotic behaviour (2.15) and let us suppose that the corresponding solution of the Schlesinger equations $A_{0,1, x}(x)$ does not satisfy the relations (2.16) and (2.17). As shown in the lemma 2.2, for any constant matrices $A_{0,1, x}^{0}, \Lambda$ such that $\Lambda=A_{0}^{0}+A_{x}^{0}$ has eigenvalues $\pm \frac{\sigma}{2}, \sigma \in[0,1[$, and $A_{1}^{0}=-\Lambda-A_{\infty}$, there exists a solution $\hat{A}_{0,1, x}(x)$ of the Schlesinger equations that satisfy the relations (2.16) and (2.17). Now, as shown in Section 2.2, we can choose $A_{0,1, x}^{0}$ in order that the corresponding solution $\hat{y}(x)$ of Painlevé VI equation has exactly the asymptotic behaviour (2.15). Due to the uniqueness proved in Theorem 2.2, we have that $y(x)=\hat{y}(x)$, namely $A_{0,1, x}=\hat{A}_{0,1, x}$ up to conjugation by a constant diagonal matrix. This contradiction proves the theorem. QED
2.1.5. Asymptotic behaviour of the $\mathbf{P V I} \mu$ solution near 1 and $\infty$. We now state the analogues of Theorem 2.2 for the local asymptotic behaviour of the solutions of (PVI) near the singular points $x=1, \infty$ :

Theorem 2.2'. For any pair of values $\left(a_{1}, \sigma_{1}\right), \sigma_{1} \in[0,1[$, there exists a unique branch of the solution of (PVI) with the asymptotic behaviour
$$y(x) \sim 1-a_{1}(1-x)^{1-\sigma_{1}}\left(1+\mathcal{O}\left((1-x)^{\varepsilon}\right)\right) \quad \text { as } \quad x \rightarrow 1,$$
for some $\varepsilon>0$.
The proof of this theorem is analogous to the proof of theorem 1, namely one can state the analogous of the lemma 2.2 replacing $x \mapsto 1-x$, and then choose suitably $\Lambda, A_{0,1, x}^{0}$. The uniqueness is proved in the same way as the case $x \mapsto 0$.

Theorem 2.2". For any pair of values $\left(a_{\infty}, \sigma_{\infty}\right), \sigma_{\infty} \in[0,1[$, there exists a unique branch of the solution of (PVI) with the asymptotic behaviour
$$y(x) \sim a_{\infty} x^{\sigma_{\infty}}\left(1+\mathcal{O}\left(\left(x^{-\varepsilon}\right)\right) \quad \text { as } \quad x \rightarrow \infty,\right.$$
for some $\varepsilon>0$.
The proof of uniqueness is analogous to the one of Theorem 2.2. The proof of existence follows the same strategy as the one of Theorem 2.2, but with a different formulation of the lemma 2.2:

Lemma 2.2'. Given some constant matrices $A_{i}^{0}, i=0,1, x$ with zero eigenvalues such that $\Lambda=A_{0}^{0}+A_{t}^{0}$ has eigenvalues $\pm \frac{\sigma}{2}, 0 \leq \sigma<1$, in any sector of $\overline{\mathbb{C}}$ containing none of the branch cuts, and sufficiently close to $\infty$, there exists a solution of the Schlesinger equations satisfying:
$$\left|x^{A_{\infty}} A_{x}(x) x^{-A_{\infty}}-A_{1}^{0}\right| \leq K|x|^{\sigma^{\prime}-1} \quad\left|x^{\Lambda}\left(x^{A_{\infty}} A_{x}(x) x^{-A_{\infty}}-A_{1}^{0}\right) x^{-\Lambda}\right| \leq K|x|^{\sigma^{\prime}-1}$$
$$\left|x^{\Lambda} x^{A_{\infty}} A_{0,1}(x) x^{-A_{\infty}} x-^{\Lambda}-A_{x}^{0}\right| \leq K|x|^{\sigma^{\prime}-1},$$
where $K$ is some positive constant and $1>\sigma^{\prime}>\sigma$.
Proof. Let us consider the Schlesinger equations (2.3) and perform the change of variable $x=\frac{1}{\hat{x}}$. Moreover we put:
$$A_{i}(x):=x^{-A_{\infty}} \hat{A}_{i}(x) x^{A_{\infty}} ;$$
Then we can apply Lemma 2.2 to the system:
$$\begin{aligned}
& \frac{\mathrm{d}}{\mathrm{~d} \hat{x}} \hat{A}_{0}(\hat{x})=-\frac{\left[\hat{A}_{0}, \hat{A}_{1}\right]}{\hat{x}}, \\
& \frac{\mathrm{~d}}{\mathrm{~d} \hat{x}} \hat{A}_{x}(\hat{x})=-\frac{\left[\hat{A}_{x}, \hat{A}_{1}\right]}{\hat{x}-1}, \\
& \frac{\mathrm{~d}}{\mathrm{~d} \hat{x}} \hat{A}_{1}(\hat{x})=\frac{\left[\hat{A}_{0}, \hat{A}_{1}\right]}{\hat{x}}+\frac{\left[\hat{A}_{x}, \hat{A}_{1}\right]}{\hat{x}-1},
\end{aligned}$$
and obtain the estimates (2.38) and (2.39). QED

\subsection*{2.2. The local asymptotic behaviour and the monodromy group of the Fuchsian system}

In this section we relate the local asymptotic behaviour of the solution $y(x)$ of $\mathrm{PVI} \mu$ to the monodromy data of the associated Fuchsian system (2.2). We essentially follow the same strategy of [Jim], even if we have to introduce some more tricks due to the fact that our matrices $A_{0,1, x}^{0}$ have eigenvalues all equal to zero. The main result of this section is the following:

Theorem 2.4. For the solution $y(x)$ of PVI $\mu$, such that $y(x) \sim a_{0} x^{1-\sigma_{0}}\left(1+\mathcal{O}\left(x^{\varepsilon}\right)\right)$, $0<\sigma_{0}<1$, the monodromy matrices of the Fuchsian system (2.2) have the form
$$\begin{aligned}
& M_{1}=\frac{-i}{\sin \pi \vartheta_{\infty}} \\
& \quad \cdot\left(\begin{array}{cc}
\cos \pi \sigma_{0}-e^{-i \pi \vartheta_{\infty}} & -2 e^{-i \pi \vartheta_{\infty}} \sin \frac{\pi\left(\vartheta_{\infty}+\sigma_{0}\right)}{2} \sin \frac{\pi\left(\vartheta_{\infty}-\sigma_{0}\right)}{2} \\
2 e^{i \pi \vartheta_{\infty}} \sin \frac{\pi\left(\vartheta_{\infty}+\sigma_{0}\right)}{2} \sin \frac{\pi\left(\vartheta_{\infty}-\sigma_{0}\right)}{2} & -\cos \pi \sigma_{0}+e^{i \pi \vartheta_{\infty}}
\end{array}\right) \\
& \quad C M_{x} C^{-1}=\frac{-i}{\sin \pi \sigma_{0}}\left(\begin{array}{cc}
e^{i \pi \sigma_{0}}-1 & 2 s e^{i \pi \sigma_{0}} \sin ^{2} \frac{\pi \sigma_{0}}{2} \\
-\frac{2}{s} e^{-i \pi \sigma_{0}} \sin ^{2} \frac{\pi \sigma_{0}}{2} & 1-e^{-i \pi \sigma_{0}}
\end{array}\right) \\
& \quad C M_{0} C^{-1}=\frac{-i}{\sin \pi \sigma_{0}}\left(\begin{array}{cc}
e^{i \pi \sigma_{0}}-1 & -2 s \sin ^{2} \frac{\pi \sigma_{0}}{2} \\
\frac{2}{s} \sin ^{2} \frac{\pi \sigma_{0}}{2} & 1-e^{-i \pi \sigma_{0}}
\end{array}\right)
\end{aligned}$$
where $\vartheta_{\infty}=2 \mu$ and:
$$\frac{s}{r}=\frac{1}{4 a_{0}} \frac{2 \mu+\sigma_{0}}{2 \mu-\sigma_{0}} \frac{\Gamma^{2}\left(1+\sigma_{0}\right) \Gamma^{2}\left(1-\frac{\sigma_{0}}{2}\right) \Gamma\left(1+\mu-\frac{\sigma_{0}}{2}\right) \Gamma\left(1-\mu-\frac{\sigma_{0}}{2}\right)}{\Gamma^{2}\left(1-\sigma_{0}\right) \Gamma^{2}\left(1+\frac{\sigma_{0}}{2}\right) \Gamma\left(1+\mu+\frac{\sigma_{0}}{2}\right) \Gamma\left(1-\mu+\frac{\sigma_{0}}{2}\right)}$$
with an arbitrary complex number $r \neq 0$ and the matrix $C$ is:
$$C=\left(\begin{array}{cc}
\sin \frac{\pi\left(\vartheta_{\infty}-\sigma_{0}\right)}{2} & r \sin \frac{\pi\left(\vartheta_{\infty}+\sigma_{0}\right)}{2} \\
\frac{1}{r} \sin \frac{\pi\left(\vartheta_{\infty}+\sigma_{0}\right)}{2} & \sin \frac{\pi\left(\vartheta_{\infty}-\sigma_{0}\right)}{2}
\end{array}\right) .$$
In the case where $\sigma_{0}=0$ the monodromy matrices of the Fuchsian system (2.2) have the form
$$\begin{gathered}
M_{1}=\frac{1}{\cos \frac{\pi \vartheta_{\infty}}{2}}\left(\begin{array}{cc}
e^{-i \pi \frac{\vartheta_{\infty}}{2}} & i \pi e^{-i \pi \frac{\vartheta_{\infty}}{2}} \\
-\frac{i}{\pi} \sin ^{2} \frac{\pi \vartheta_{\infty}}{2} e^{i \pi \frac{\vartheta_{\infty}}{2}} & e^{i \pi \frac{\vartheta_{\infty}}{2}}
\end{array}\right) \\
M_{0}=\left(\begin{array}{cc}
1-i s \tan \frac{\pi \vartheta_{\infty}}{2} & -i s \pi \exp \left(i \pi \frac{\vartheta_{\infty}}{2}\right) \sec \frac{\pi \vartheta_{\infty}}{2} \\
\frac{i}{\pi} s \sin ^{2} \frac{\pi \vartheta_{\infty}}{2} \exp \left(-i \pi \frac{\vartheta_{\infty}}{2}\right) \sec \frac{\pi \vartheta_{\infty}}{2} & 1+i s \tan \frac{\pi \vartheta_{\infty}}{2}
\end{array}\right), \\
M_{x}=\left(\begin{array}{cc}
1-i(1-s) \tan \frac{\pi \vartheta_{\infty}}{2} & -i(1-s) \pi \exp \left(i \pi \frac{\vartheta_{\infty}}{2}\right) \sec \frac{\pi \vartheta_{\infty}}{2} \\
\frac{i}{\pi}(1-s) \sin ^{2} \frac{\pi \vartheta_{\infty}}{2} \exp \left(-i \pi \frac{\vartheta_{\infty}}{2}\right) \sec \frac{\pi \vartheta_{\infty}}{2} & 1+i(1-s) \tan \frac{\pi \vartheta_{\infty}}{2}
\end{array}\right),
\end{gathered}$$
where $s=a_{0}$.
The main idea to prove this theorem is that, due to Theorem 2.3, the solutions of the Schlesinger equations corresponding to the $\mathrm{PVI} \mu$ solution with the asymptotic behaviour (2.15) must satisfy the relations (2.16) and (2.17). Using these relations, we obtain the monodromy matrices of the Fuchsian system (2.2) via the ones of two simpler systems, given in the following two lemmas (see [SMJ] and [Jim]):

Lemma 2.5. Under the hypotheses (2.16), (2.17), the limit of the fundamental solution of the system (2.2), normalized at infinity, $\lim _{x \rightarrow 0} Y_{\infty}(z, x)=\hat{Y}(z)$, exists, for $z \in \overline{\mathbb{C}} \backslash\left\{B_{0} \cup\right.$ $\left.B_{x} \cup B_{1} \cup B_{\infty}\right\}, B_{0}, B_{x}, B_{1}$ and $B_{\infty}$ being balls around $0, x, 1$ and $\infty$ respectively. This limit $\hat{Y}$ satisfies the differential equation:
$$\frac{\mathrm{d}}{\mathrm{~d} z} \hat{Y}=\left(\frac{A_{1}^{0}}{z-1}+\frac{\Lambda}{z}\right) \hat{Y} ;$$
and it has the following behaviour near the singularities of $(\hat{\Sigma})$
$$\begin{aligned}
\hat{Y}(z)= & \left(1+\mathcal{O}\left(\frac{1}{z}\right)\right) z^{-A_{\infty}} \quad z \rightarrow \infty \\
& =(1+\mathcal{O}(z)) z^{\Lambda} \hat{C}_{0} \quad z \rightarrow 0 \\
& =\hat{G}_{1}(1+\mathcal{O}(z-1))(z-1)^{J_{1}} \hat{C}_{1} \quad z \rightarrow 1
\end{aligned}$$
where $J_{1}$ is the Jordan normal forms of $A_{1}^{0}, \hat{G}_{1} J_{1} \hat{G}_{1}^{-1}=A_{1}^{0}, A_{\infty}=\left(\begin{array}{cc}\mu & 0 \\ 0 & -\mu\end{array}\right)$. Here $\hat{C}_{0}$, $\hat{C}_{1}$ are the connection matrices of the system $(\hat{\Sigma})$.
Remark 2.4. Observe that the matrix $\hat{C}_{0}$ is uniquely determined by the conditions (2.48).

Lemma 2.6. Under the hypotheses (2.16), (2.17), the limit of the fundamental solution of the system (2.2), normalized around $\infty, \lim _{x \rightarrow 0} x^{-\Lambda} Y(x z, x)=\tilde{Y}(z) \hat{C}_{0}$ exists for $z \in$ $\overline{\mathbb{C}} \backslash\left\{B_{0} \cup B_{x} \cup B_{1} \cup B_{\infty}\right\}$. It satisfies the system
$$\frac{\mathrm{d}}{\mathrm{~d} z} \tilde{Y}=\left(\frac{A_{x}^{0}}{z-1}+\frac{A_{0}^{0}}{z}\right) \tilde{Y} ;$$
and it has the following behaviour near the singularities of $(\tilde{\Sigma})$
$$\begin{aligned}
\tilde{Y}(z)= & \left(1+\mathcal{O}\left(\frac{1}{z}\right)\right) z^{\Lambda} & & z \rightarrow \infty \\
& =\tilde{G}_{0}(1+\mathcal{O}(z)) z^{J_{0}} \tilde{C}_{0} & & z \rightarrow 0 \\
& =\tilde{G}_{1}(1+\mathcal{O}(z-1))(z-1)^{J_{1}} \tilde{C}_{1} & & z \rightarrow 1
\end{aligned}$$
where $J_{0,1}$ are the Jordan normal forms of $A_{0, x}^{0}, \tilde{G}_{0,1}$ are such that $\tilde{G}_{0,1} J_{0,1} \tilde{G}_{0,1}^{-1}=A_{0, x}^{0}$. We denote $\tilde{C}_{0,1}$ the connection matrices of the system $(\tilde{\Sigma})$.

As we have seen above, the matrices of the two systems have the following form:
$$A_{0}^{0}=\frac{1}{2} \Lambda+F, \quad A_{x}^{0}=\frac{1}{2} \Lambda-F, \quad A_{1}^{0}=-A_{\infty}-\Lambda,$$
for some constant matrix $F$, and for $\Lambda$ and $T$ such that
$$\Lambda=T\left(\begin{array}{cc}
\frac{\sigma}{2} & 0 \\
0 & -\frac{\sigma}{2}
\end{array}\right) T^{-1} .$$
Using the relations (2.6), we have that
$$F=T\left(\begin{array}{cc}
0 & \frac{b \sigma}{4} \\
\frac{-\sigma}{4 b} & 0
\end{array}\right) T^{-1},$$
for some parameter $b$. As a consequence the systems $(\hat{\Sigma})$ and $(\tilde{\Sigma})$ are determined, up to diagonal conjugation, by the four entries of the matrix $T$ and by $b$.

Now, we explain how to compute the monodromy matrices of the original system (2.2) knowing the ones of the systems $(\hat{\Sigma})$ and $(\tilde{\Sigma})$. Later we will show how to compute the matrices $A_{0, x, 1}^{0}$ and the monodromy matrices of $(\hat{\Sigma})$ and $(\tilde{\Sigma})$.

Lemma 2.7. Let $\hat{M}_{0}, \hat{M}_{1}, \hat{M}_{\infty}=M_{\infty}$ be the monodromy matrices of the system ( $\hat{\Sigma}$ ) with respect to the fundamental matrix $\hat{Y}$ and the basis $\hat{\gamma}_{0}=\gamma_{0} \gamma_{x}, \gamma_{1}$ in $\pi_{1}(\overline{\mathbb{C}} \backslash\{0,1, \infty\})$. Let $\tilde{M}_{0}, \tilde{M}_{1}, \tilde{M}_{\infty}=\exp (-2 \pi i \Lambda)$ be the monodromy matrices of the system $(\tilde{\Sigma})$ with respect to the fundamental matrix $\tilde{Y}$ and the basis $\tilde{\gamma}_{0}, \tilde{\gamma}_{1}=\gamma_{x}$. Then the monodromy matrices of the original system (2.2) are given by the formulae:
$$M_{0}=\hat{C}_{0}^{-1} \tilde{M}_{0} \hat{C}_{0}, \quad M_{x}=\hat{C}_{0}^{-1} \tilde{M}_{1} \hat{C}_{0}, \quad M_{1}=\hat{M}_{1},$$

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/64ce0006-7367-4aae-9e25-7b8a1be4f808-63.jpg?height=486&width=486&top_left_y=238&top_left_x=857}
\captionsetup{labelformat=empty}
\caption{Fig.7. The paths $\gamma_{x}$ and $\gamma_{0}$ merge together as $x \rightarrow 0$. The homotopy class of $\gamma_{0} \gamma_{x}$ remains unchanged.}
\end{figure}
where $\hat{C}_{0}$ is defined by (2.48).
Proof. By the definition of $\hat{Y}$, the system $(\hat{\Sigma})$ is obtained by merging of the singularities 0 and $x$ of the system (2.2). We can choose the loop $\hat{\gamma}_{0}$ to be homotopic to $\gamma_{0} \gamma_{x}$, with $\hat{\gamma}_{0}$ not crossing a ball the $B_{0}$ (see figure 7).

As a consequence we obtain a relation between the monodromy matrices of the system (2.2) and the ones of the system $(\hat{\Sigma})$
$$\begin{aligned}
\hat{M}_{\infty} & =M_{\infty}, \\
\hat{M}_{1} & =M_{1}, \\
\hat{M}_{0} & =M_{x} M_{0} .
\end{aligned}$$
Similarly, by the definition of $\tilde{Y}$ the system $(\tilde{\Sigma})$ is obtained by the merging (see figure 8) of the singularities $z^{\prime}=\frac{1}{x}$ and $z^{\prime}=\infty$ of the system for $Y^{\prime}\left(z^{\prime}\right)$ :
$$\frac{\mathrm{d}}{\mathrm{~d} z^{\prime}} Y^{\prime}=\left(\frac{A_{0}}{z^{\prime}}+\frac{A_{1}}{z^{\prime}-\frac{1}{x}}+\frac{A_{x}}{z^{\prime}-1}\right) Y^{\prime} .$$

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/64ce0006-7367-4aae-9e25-7b8a1be4f808-63.jpg?height=493&width=709&top_left_y=1885&top_left_x=761}
\captionsetup{labelformat=empty}
\caption{Fig.8. The paths $\gamma_{1}$ and $\gamma_{\infty}$ merge together as $x \rightarrow 0$. The homotopy class of $\tilde{\gamma} \equiv \gamma_{1} \gamma_{\infty}$ coincides with the one of $\left(\gamma_{0} \gamma_{x}\right)^{-1}$}
\end{figure}

So, in the basis $\hat{Y}$, the monodromy matrices of $(\tilde{\Sigma})$ have the following form:
$$\begin{aligned}
\tilde{M}_{\infty} & =\hat{C}_{0}^{-1} M_{\infty} M_{1} \hat{C}_{0} \\
\tilde{M}_{1} & =\hat{C}_{0}^{-1} M_{x} \hat{C}_{0} \\
\tilde{M}_{0} & =\hat{C}_{0}^{-1} M_{0} \hat{C}_{0} .
\end{aligned}$$
The lemma is proved. QED

Now we want to compute the monodromy matrices $\hat{M}_{i}$ and $\tilde{M}_{i}$ and the connection matrix $\hat{C}_{0}$. To this aim we have to solve the systems $(\hat{\Sigma})$ and $(\tilde{\Sigma})$, namely we have to determine $T$ and $b$. For $\sigma_{0} \neq 0$, this can be done introducing a suitable gauge transformation of $\hat{Y}$ and $\tilde{Y}$ such that the systems $(\hat{\Sigma})$ and $(\tilde{\Sigma})$ are equivalent to a Gauss equation. The case $\sigma_{0}=0$ will be treated later.
2.2.1. Reduction to the Gauss equation. First of all let us notice that both the systems $(\hat{\Sigma})$ and $(\tilde{\Sigma})$ have similar form. We want to reduce them, via a suitable gauge transformation and a appropriate choice of the parameters $\alpha, \beta, \gamma$, to systems of the form:
$$\frac{\mathrm{d}}{\mathrm{~d} z} Y(z, \alpha, \beta, \gamma)=\left(\frac{B_{0}}{z}+\frac{B_{1}}{z-1}\right) Y(z, \alpha, \beta, \gamma)$$
where $B_{0}, B_{1}$ are some constant matrices with eigenvalues $1-\gamma, 0$ and $\gamma-\alpha-\beta-1,0$ respectively and $B_{0}+B_{1}=-\left(\begin{array}{cc}\alpha & 0 \\ 0 & \beta\end{array}\right)$.
Lemma 2.8. For $\alpha \neq \beta$, the system (2.52) is uniquely determined, up to a diagonal conjugation
$$B_{0} \rightarrow T^{-1} B_{0} T, \quad B_{1} \rightarrow T^{-1} B_{1} T, \quad \text { with } \quad T=\left(\begin{array}{cc}
1 & 0 \\
0 & r
\end{array}\right), r \neq 0 .$$
The entries $b_{i j}^{0}$ and $b_{i j}^{1}$ of the matrices $B_{0}$ and $B_{1}$ respectively, are given by the formulae
$$\begin{array}{ll}
b_{11}^{0}=\frac{\alpha(\gamma-1-\beta)}{\beta-\alpha}, & b_{22}^{0}=\frac{-\beta(\gamma-1-\alpha)}{\beta-\alpha}, \quad b_{11}^{1}=\frac{-\alpha(\gamma-1-\alpha)}{\beta-\alpha}, \\
b_{22}^{1}=\frac{\beta(\gamma-1-\beta)}{\beta-\alpha}, & b_{12}^{0} b_{21}^{0}=b_{12}^{1} b_{21}^{1}=\frac{-\alpha \beta(\gamma-1-\beta)(\gamma-1-\alpha)}{(\beta-\alpha)^{2}} .
\end{array}$$

The system (2.52) can be solved using the Gauss hypergeometric function. So, we can compute its connection matrices via the Kummer relations (see [Luke]) of the hypergeometric functions.
Lemma 2.9. The solutions of (2.52) have the form $Y=\binom{y_{1}}{y_{2}}$, with $y_{1}$ being an arbitrary solution of the following Gauss equation:
$$z(1-z) y_{1}^{\prime \prime}+[c-(a+b+1) z] y_{1}^{\prime}-a b y_{1}=0$$
where $a=\alpha, b=\beta+1, c=\gamma$ and $y_{2}$ given by:
$$y_{2}(z)=r^{-1} \frac{\beta-\alpha}{\beta(\gamma-\beta-1)}\left\{z(z-1) \frac{\mathrm{d}}{\mathrm{~d} z} y_{1}(z)+\left[\alpha z+\frac{\alpha(\gamma-\beta-1)}{\beta-\alpha}\right] y_{1}(z)\right\}$$
where $r=-\frac{(\beta-\alpha) b_{12}^{0}}{\beta(\gamma-\beta-1)}$.
Proof. After the gauge transformation:
$$Y(z, \alpha, \beta, \gamma)=z^{b_{11}^{0}}(1-z)^{b_{11}^{1}} U(z, \alpha, \beta, \gamma),$$
one obtains from (2.52) the following Riemann equation for $u_{1}$
$$u_{1}^{\prime \prime}+\left[\frac{1+b_{11}^{0}-b_{22}^{0}}{z}+\frac{1+b_{11}^{1}-b_{22}^{1}}{z-1}\right] u_{1}^{\prime}-\frac{b_{11}^{0} b_{22}^{0}}{z^{2}(z-1)^{2}} u_{1}=0 .$$
Now $u_{1}$ is related with the solution $y_{G}$ of the Gauss equation (2.56), with $a=-b_{11}^{0}-b_{11}^{1}$, $b=1-b_{22}^{0}-b_{22}^{1}, c=1-b_{11}^{0}-b_{22}^{0}$, via the relation $u_{1}=z^{-b_{11}^{0}}(1-z)^{-b_{11}^{1}} y_{G}$. As a consequence, thanks to (2.54), (2.55), we obtain that $y_{1}=y_{G}$ and $a=\alpha+1, b=\beta, c=\gamma$. $y_{2}$ it is given by:
$$\left(\frac{b_{12}^{0}}{z}+\frac{b_{12}^{1}}{z-1}\right) y_{2}=y_{1}^{\prime}-\left(\frac{b_{11}^{0}}{z}+\frac{b_{11}^{1}}{z-1}\right) y_{1}$$
that gives the equation (2.57). \(\square\)

To reduce the systems $(\hat{\Sigma})$ and $(\tilde{\Sigma})$ to the system (2.52) we need to diagonalize the matrices $A_{1}^{0}+\Lambda=-A_{\infty}$ and $\Lambda$ respectively and to perform a suitable gauge transform. We need to introduce some notations. Denote $C_{0,1}^{\alpha, \beta, \gamma}$ the connection matrices of the system (2.52). The matrices $J_{0,1}$ are the Jordan normal forms of $B_{0,1}$ and the matrices $G_{0,1}^{\alpha, \beta, \gamma}$ are such that $G_{0,1}^{\alpha, \beta, \gamma} J_{0,1}\left(G_{0,1}^{\alpha, \beta, \gamma}\right)^{-1}=B_{0,1}$. Then for the asymptotic behaviour of an appropriate fundamental matrix $Y(z, \alpha, \beta, \gamma)$ of the system (2.52) we have
$$\begin{aligned}
Y(z, \alpha, \beta, \gamma) & =\left(1+\mathcal{O}\left(\frac{1}{z}\right)\right) z^{-\left(\begin{array}{cc}
\alpha & 0 \\
0 & \beta
\end{array}\right)} & & z \rightarrow \infty \\
& =G_{0}^{\alpha, \beta, \gamma}(1+\mathcal{O}(z)) z^{J_{0}} C_{0}^{\alpha, \beta, \gamma} & & z \rightarrow 0 \\
& =G_{1}^{\alpha, \beta, \gamma}(1+\mathcal{O}(z-1))(z-1)^{J_{1}} C_{1}^{\alpha, \beta, \gamma} & & z \rightarrow 1 .
\end{aligned}$$
Some further remarks on the notations: from now on all the quantities with the hat are referred to the system $(\hat{\Sigma})$ and all the quantities with the tilde to the system $(\tilde{\Sigma})$. When we don't put any hat or tilde, the formulae are true for both the systems. In other words, they hold true for the generic system (2.52); substituting all the quantities with the correspondent hat or tilde ones, the formulae hold true for the systems $(\hat{\Sigma})$ or $(\tilde{\Sigma})$ respectively.

We now choose the values of $\alpha, \beta, \gamma$ in relation with the eigenvalues of the matrices of the systems $(\hat{\Sigma})$ and $(\tilde{\Sigma})$. Namely, for $(\hat{\Sigma})$ we take
$$\hat{\alpha}=\frac{\vartheta_{\infty}-\sigma_{0}}{2}, \quad \hat{\beta}=-\frac{\vartheta_{\infty}+\sigma_{0}}{2}, \quad \hat{\gamma}=1-\sigma_{0},$$
and for $(\tilde{\Sigma})$ we take:
$$\tilde{\alpha}=-\frac{\sigma_{0}}{2}, \quad \tilde{\beta}=\frac{\sigma_{0}}{2}, \quad \tilde{\gamma}=1 .$$
With this choice of the values of $\alpha, \beta, \gamma$, one has:
$$\hat{J}_{0}=\left(\begin{array}{cc}
1-\gamma & 0 \\
0 & 0
\end{array}\right), \quad \tilde{J}_{0}=\left(\begin{array}{ll}
0 & 1 \\
0 & 0
\end{array}\right), \quad \hat{J}_{1}=\tilde{J}_{1}=\left(\begin{array}{ll}
0 & 1 \\
0 & 0
\end{array}\right) .$$
Now we can reduce the systems $(\hat{\Sigma})$ and $(\tilde{\Sigma})$ to the system (2.52) via the following gauge transformations:
$$\hat{Y}=z^{\frac{\hat{\alpha}+\hat{\beta}}{2}} Y(z, \hat{\alpha}, \hat{\beta}, \hat{\gamma}), \quad \tilde{Y}=G_{0}^{\hat{\alpha}, \hat{\beta}, \hat{\gamma}} Y(z, \tilde{\alpha}, \tilde{\beta}, \tilde{\gamma}),$$
where $G_{0}^{\hat{\alpha}, \hat{\beta}, \hat{\gamma}}$ is such that
$$\Lambda-\frac{\hat{\alpha}+\hat{\beta}}{2} \mathrm{Id}=G_{0}^{\hat{\alpha}, \hat{\beta}, \hat{\gamma}}\left(\begin{array}{cc}
-\tilde{\alpha} & 0 \\
0 & -\tilde{\beta}
\end{array}\right)\left(G_{0}^{\hat{\alpha}, \hat{\beta}, \hat{\gamma}}\right)^{-1} .$$
As a consequence the connection matrices of (2.52) are related to the ones of $(\hat{\Sigma})$ and $(\tilde{\Sigma})$ by the following formulae:
$$\begin{aligned}
& \hat{G}_{1}=G_{1}^{\hat{\alpha}, \hat{\beta}, \hat{\gamma}}, \quad \hat{C}_{1}=C_{1}^{\hat{\alpha}, \hat{\beta}, \hat{\gamma}}, \quad \hat{C}_{0}=G_{0}^{\hat{\alpha}, \hat{\beta}, \hat{\gamma}} C_{0}^{\hat{\alpha}, \hat{\beta}, \hat{\gamma}} \\
& \tilde{G}_{0,1}=G_{0}^{\hat{\alpha}, \hat{\beta}, \hat{\gamma}} G_{0,1}^{\tilde{\alpha}, \tilde{\beta}, \tilde{\gamma}}, \quad \tilde{C}_{0,1}=C_{0,1}^{\tilde{\alpha}, \tilde{\beta}, \tilde{\gamma}}\left(G_{0}^{\hat{\alpha}, \hat{\beta}, \hat{\gamma}}\right)^{-1} .
\end{aligned}$$
2.2.2. Local behaviour of the solution of (2.52). The solutions of (2.56) around the singular points $0,1, \infty$ are known and one can compute $y_{2}$ by (2.57). In this way one obtains the local behaviour of the fundamental solution $Y$ for $z \rightarrow 0,1, \infty$, and one can compute the connection matrices by the Kummer relations (which are the connection formulae for the hypergeometric equation). The difference w.r.t. the situation of [Jim] is that in our case the Gauss equation is degenerate, namely:
$$\hat{c}-\hat{a}-\hat{b}=0, \quad \tilde{c}-\tilde{a}-\tilde{b}=0, \quad \tilde{c}=1 .$$
So, we have to consider the logarithmic solutions of the Gauss equation around $z=1$ for both the systems $(\hat{\Sigma})$ and $(\tilde{\Sigma})$, and around $z=0$ for $(\tilde{\Sigma})$; moreover, we shall use the extension of the Kummer relations to this logarithmic case (see [Nor]).

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/64ce0006-7367-4aae-9e25-7b8a1be4f808-67.jpg?height=354&width=409&top_left_y=251&top_left_x=886}
\captionsetup{labelformat=empty}
\caption{Fig.9. The branch cut $|\arg (z)|<\pi$.}
\end{figure}

In what follows we denote $F(a, b, c, z)$ the hypergeometric function and with $g(a, b, z)$ its logarithmic counterpart for $c=1$, namely:
$$\begin{gathered}
F(a, b, c, z)=\sum_{k=0}^{\infty} \frac{(a)_{k}(b)_{k}}{k!(c)_{k}} z^{k}, \\
g(a, b, z)=\sum_{k=0}^{\infty} \frac{(a)_{k}(b)_{k}}{k!} z^{k}[\ln z+\psi(a+k)+\psi(b+k)-2 \psi(k+1)],
\end{gathered}$$
with the branchcut $|\arg (z)|<\pi$ (see figure 9). Here $\psi$ is the logarithmic derivative of the gamma function, and the expressions of the parameters $a, b, c$ via $\alpha, \beta, \gamma$ are given in the lemma 2.9.
Fundamental solution near $\infty$ Since $a-b \neq 0$, the solutions of (2.56) around $\infty$ are not logarithmic. We obtain
$$\begin{gathered}
Y_{\infty}=\left(\begin{array}{cc}
z^{-\alpha} F\left(\alpha,-\beta, \alpha-\beta, \frac{1}{z}\right) & \frac{-\alpha \beta z^{-\beta-1} r}{(\beta-\alpha)(\beta-\alpha+1)} F\left(\beta+1,1-\alpha, \beta-\alpha+2, \frac{1}{z}\right) \\
\frac{-\alpha \beta z^{-\alpha-1}}{r(\beta-\alpha)(\beta-\alpha-1)} F\left(\alpha+1,1-\beta, \alpha-\beta+2, \frac{1}{z}\right) & z^{-\beta} F\left(\beta, \alpha, \beta-\alpha, \frac{1}{z}\right)
\end{array}\right) \\
Y_{\infty} \sim\left(1+\mathcal{O}\left(\frac{1}{z}\right)\right) z^{-\left(\begin{array}{cc}
\alpha & 0 \\
0 & \beta
\end{array}\right)}, \quad z \rightarrow \infty .
\end{gathered}$$
The monodromy around $\infty$ is $\left(\begin{array}{cc}\exp (2 \pi i \alpha) & 0 \\ 0 & \exp (2 \pi i \beta)\end{array}\right)$.
Fundamental solution near 1. Since $c-a-b=0$, the solutions are logarithmic:
$$Y_{1}=\left(\begin{array}{cc}
F(\alpha, \beta+1,1,1-z) & r g(\alpha, \beta+1,1,1-z) \\
\frac{1}{r} F(\alpha+1, \beta, 1,1-z) & g(\alpha+1, \beta, 1,1-z)
\end{array}\right) .$$
For $z \rightarrow 1$
$$Y_{1} \sim G_{1}^{\alpha, \beta}(1-z)\left(\begin{array}{cc}
0 & 1 \\
0 & 0
\end{array}\right),$$
with
$$G_{1}^{\alpha, \beta}=\left(\begin{array}{cc}
1 & r[\psi(\alpha)+\psi(1+\beta)-2 \psi(1)] \\
\frac{1}{r} & \psi(1+\alpha)+\psi(\beta)-2 \psi(1)
\end{array}\right) .$$
The monodromy around 1 is $\left(\begin{array}{cc}1 & 2 i \pi r \\ 0 & 1\end{array}\right)$.
Fundamental solution near 0. We have to distinguish the case $(\hat{\Sigma})$, where the solutions of (2.56) around 0 are not logarithmic, and the case $(\tilde{\Sigma})$, where $c=1$ and the solutions are logarithmic.

For $(\hat{\Sigma})$ one has
$$\hat{Y}_{0}=\left(\begin{array}{cc}
-\frac{\hat{\alpha}}{\hat{\beta}-\hat{\alpha}} z^{-\hat{\alpha}-\hat{\beta}} F(-\hat{\beta}, 1-\hat{\alpha}, 1-\hat{\alpha}-\hat{\beta}, z) & \hat{r} \frac{\hat{\beta}}{\hat{\beta}-\hat{\alpha}} F(\hat{\alpha}, \hat{\beta}+1, \hat{\alpha}+\hat{\beta}+1, z) \\
-\frac{\hat{\beta}}{\hat{r}(\hat{\beta}-\hat{\alpha})} z^{-\hat{\alpha}-\hat{\beta}} F(1-\hat{\beta},-\hat{\alpha}, 1-\hat{\alpha}-\hat{\beta}, z) & \frac{\hat{\alpha}}{\hat{\beta}-\hat{\alpha}} F(\hat{\alpha}+1, \hat{\beta}, \hat{\alpha}+\hat{\beta}+1, z)
\end{array}\right) .$$
For $z \rightarrow 0$ it behaves like
$$\hat{Y}_{0} \sim G_{0}^{\hat{\alpha}, \hat{\beta}}{ }_{z}\left(\begin{array}{cc}
-\hat{\alpha}-\hat{\beta} & 0 \\
0 & 0
\end{array}\right)$$
where
$$G_{0}^{\hat{\alpha}, \hat{\beta}}=\frac{1}{\hat{\beta}-\hat{\alpha}}\left(\begin{array}{cc}
-\hat{\alpha} & \hat{r} \hat{\beta} \\
-\frac{\hat{\beta}}{\hat{r}} & \hat{\alpha}
\end{array}\right) .$$
The monodromy around 0 is $\left(\begin{array}{cc}\exp (-2 i \pi(\hat{\alpha}+\hat{\beta}) & 0 \\ 0 & 1\end{array}\right)$.
For $(\tilde{\Sigma})$ one has
$$\tilde{Y}_{0}=\left(\begin{array}{cc}
F(\tilde{\alpha}, 1-\tilde{\alpha}, 1, z) & \tilde{r} g(\tilde{\alpha}, 1-\tilde{\alpha}, 1, z) \\
-\frac{1}{\tilde{r}} F(\tilde{\alpha}+1,-\tilde{\alpha}, 1, z) & -g(\tilde{\alpha}+1,-\tilde{\alpha}, 1, z)
\end{array}\right),$$
for $z \rightarrow 0$ it behaves like
$$\tilde{Y}_{0} \sim G_{0}^{\tilde{\alpha}} z\left(\begin{array}{ll}
0 & 1 \\
0 & 0
\end{array}\right)$$
with
$$G_{0}^{\tilde{\alpha}}=\left(\begin{array}{cc}
1 & \tilde{r}[\psi(1-\tilde{\alpha})+\psi(\tilde{\alpha})-2 \psi(1)] \\
-\frac{1}{\tilde{r}} & -\psi(1+\tilde{\alpha})-\psi(-\tilde{\alpha})+2 \psi(1)
\end{array}\right) .$$
The monodromy around 0 is $\left(\begin{array}{cc}1 & 2 i \pi \tilde{r} \\ 0 & 1\end{array}\right)$.
2.2.3. Connection formulae. In order to compute the connection matrices we write $Y_{\infty}$ in the form:
$$Y_{\infty}=\left(\begin{array}{lr}
\exp (-i \pi \alpha) U(\alpha, \beta+1, z) & \frac{-\alpha \beta \exp (-i \pi(\beta+1)) r}{(\beta-\alpha)(\beta-\alpha+1)} U(\beta+1, \alpha, z) \\
\frac{-\alpha \beta \exp (-i \pi(\alpha+1))}{r(\beta-\alpha)(\beta-\alpha-1)} U(\alpha+1, \beta, z) & \exp (-i \pi \beta) U(\beta, \alpha+1, z)
\end{array}\right)$$
where $U(a, b, z):=\left(z^{-1} e^{i \pi}\right)^{-a} F\left(a, 1-b, 1+a-b, \frac{1}{z}\right)$. For $z$ such that $|\arg (z)|<2 \pi$, there are the following connection formulae:
$$\begin{aligned}
\left.U(a, b, z)\right|_{z \rightarrow 1}= & \frac{-\exp (i \pi a) \Gamma(1+a-b)}{\Gamma(a) \Gamma(1-b)}\{[i \pi+\psi(1-b)-\psi(b)] F(a, b, 1,1-z)+ \\
& g(a, b, 1,1-z)\} \\
\left.U(a, 1-a, z)\right|_{z \rightarrow 0}= & \frac{-\Gamma(2 a)}{\Gamma(a)^{2}}\{[-i \pi+\psi(a)-\psi(1-a)] F(a, 1-a, 1, z)+g(a, 1-a, 1, z)\}, \\
\left.U(a, b, z)\right|_{z \rightarrow 0}= & \frac{\Gamma(1+a-b) \Gamma(1-a-b)}{\Gamma(1-b)^{2}} F(a, b, a+b, z)+\frac{\Gamma(1+a-b) \Gamma(a+b-1)}{\Gamma(a)^{2}} . \\
& \cdot z^{1-a-b} F(1-b, 1-a, 2-a-b, z) .
\end{aligned}$$
Using these relations we obtain the analytic continuation of $Y_{\infty}$ around 0 and 1, and by the definition of the connection matrices
$$\left.Y_{\infty}\right|_{z \rightarrow 0,1}=Y_{0,1} C_{0,1}^{\alpha, \beta, \gamma},$$
we obtain, by straightforward computations
$$\begin{gathered}
C_{0}^{\hat{\alpha}, \hat{\beta}}=\left(\begin{array}{cc}
\frac{\exp (i \pi \hat{\beta}) \Gamma(\hat{\alpha}+\hat{\beta}) \Gamma(\hat{\alpha}-\hat{\beta}+1)}{\Gamma(\hat{\alpha}) \Gamma(1+\hat{\alpha})} & -\hat{r} \frac{\exp (-i \pi \hat{\alpha}) \Gamma(\hat{\alpha}+\hat{\beta}) \Gamma(1-\hat{\alpha}+\hat{\beta})}{\Gamma(\hat{\beta}) \Gamma(1+\hat{\beta})} \\
\frac{1}{\hat{r}} \frac{\exp (-i \pi \hat{\alpha}) \Gamma(-\hat{\alpha}-\hat{\beta}) \Gamma(\hat{\alpha}-\hat{\beta}+1)}{\Gamma(1-\hat{\beta}) \Gamma(-\hat{\beta})} & -\frac{\exp (-i \pi \hat{\beta}) \Gamma(-\hat{\alpha}-\hat{\beta}) \Gamma(1-\hat{\alpha}+\hat{\beta})}{\Gamma(-\hat{\alpha}) \Gamma(1-\hat{\alpha})}
\end{array}\right), \\
C_{1}^{\hat{\alpha}, \hat{\beta}}=\left(\begin{array}{cc}
-\frac{\Gamma(\hat{\alpha}-\hat{\beta})}{\Gamma(\hat{\alpha}) \Gamma(-\hat{\beta})}[i \pi+\pi \cot (\pi \hat{\alpha})] & -\frac{\Gamma(-\hat{\alpha}+\hat{\beta})}{\Gamma(-\hat{\alpha}) \Gamma(\hat{\beta})}[i \pi+\pi \cot (\pi \hat{\beta})] \\
-\frac{1}{\hat{r}} \frac{\Gamma(\hat{\alpha}-\hat{\beta})}{\Gamma(\hat{\alpha}) \Gamma(-\hat{\beta})} & -\frac{\Gamma(-\hat{\alpha}+\hat{\beta})}{\Gamma(-\hat{\alpha}) \Gamma(\hat{\beta})}
\end{array}\right), \\
C_{0}^{\tilde{\alpha}}=\left(\begin{array}{cc}
\frac{\Gamma(2 \tilde{\alpha})}{\Gamma^{2}(\tilde{\alpha})} \exp (-i \pi \tilde{\alpha})[i \pi+\pi \cot (\pi \tilde{\alpha})] & \tilde{r} \frac{\Gamma(-2 \tilde{\alpha})}{\Gamma^{2}(-\tilde{\alpha})} \exp (i \pi \tilde{\alpha})[\pi \cot (\pi \hat{\alpha})-i \pi] \\
-\frac{1}{\tilde{r}} \frac{\Gamma(2 \tilde{\alpha})}{\Gamma^{2}(\tilde{\alpha})} \exp (-i \pi \tilde{\alpha}) & \frac{\Gamma(-2 \tilde{\alpha})}{\Gamma^{2}(-\tilde{\alpha})} \exp (i \pi \tilde{\alpha})
\end{array}\right), \\
C_{1}^{\tilde{\alpha}}=\left(\begin{array}{cc}
-\frac{\Gamma(2 \tilde{\alpha})}{\Gamma^{2}(\tilde{\alpha})}[i \pi-\pi \cot (\pi \tilde{\alpha})] & -\tilde{r}^{2} \frac{\Gamma(-2 \tilde{\alpha})}{\Gamma^{2}(-\tilde{\alpha})}[\pi \cot (\pi \hat{\alpha})+i \pi] \\
-\frac{1}{\tilde{r}} \frac{\Gamma(2 \tilde{\alpha})}{\Gamma^{2}(\tilde{\alpha})} & -\frac{\Gamma(-2 \tilde{\alpha})}{\Gamma^{2}(-\tilde{\alpha})}
\end{array}\right) .
\end{gathered}$$
Now we have to compute the monodromy matrices in the basis $Y_{\infty}$. Using the formulae (2.51), (2.61) and (2.62) we have
$$M_{1}=\left(C_{1}^{\hat{\alpha}, \hat{\beta}}\right)^{-1}\left(\begin{array}{cc}
1 & 2 \pi i \hat{r} \\
0 & 1
\end{array}\right) C_{1}^{\hat{\alpha}, \hat{\beta}}, \quad M_{0, x}=\left(C_{0}^{\hat{\alpha}, \hat{\beta}}\right)^{-1}\left(C_{0,1}^{\tilde{\alpha}}\right)^{-1}\left(\begin{array}{cc}
1 & 2 \pi i \tilde{r} \\
0 & 1
\end{array}\right) C_{0,1}^{\tilde{\alpha}} C_{0}^{\hat{\alpha}, \hat{\beta}} .$$
Now we put
$$\hat{r}=\frac{-\exp [-i \pi(\hat{\alpha}-\hat{\beta})] \Gamma(\hat{\alpha}-\hat{\beta}) \Gamma(\hat{\beta}) \Gamma(-\hat{\alpha})}{\Gamma(\hat{\beta}-\hat{\alpha}) \Gamma(-\hat{\beta}) \Gamma(\hat{\alpha})} r$$
and
$$\tilde{r}=\frac{\exp (-2 i \pi \tilde{\alpha}) \Gamma(2 \tilde{\alpha}) \Gamma(-\tilde{\alpha})^{2}}{\Gamma(-2 \tilde{\alpha}) \Gamma(\tilde{\alpha})^{2}} \tilde{s} .$$
In this way we immediately obtain the formula (2.40) for $M_{1}$ and it turns out that
$$C_{0}^{\hat{\alpha}, \hat{\beta}}=D^{\hat{\alpha}, \hat{\beta}} \cdot C$$
where $C$ is given in the formula (2.44) and
$$D^{\hat{\alpha}, \hat{\beta}}:=\left(\begin{array}{cc}
\frac{\exp (i \pi \beta) \Gamma(\hat{\beta}+\hat{\alpha}) \Gamma(1-\hat{\beta}+\hat{\alpha})}{\hat{\alpha} \Gamma(\hat{\alpha})^{2} \sin \pi \hat{\alpha}} & 0 \\
0 & \frac{-\exp (-i \pi \beta) \Gamma(-\hat{\beta}-\hat{\alpha}) \Gamma(1+\hat{\beta}-\hat{\alpha})}{\Gamma(1-\hat{\alpha}) \Gamma(-\hat{\alpha}) \sin \pi \hat{\alpha}}
\end{array}\right) .$$
As a consequence, one has
$$C M_{0, x} C^{-1}=\left(D^{\hat{\alpha}, \hat{\beta}}\right)^{-1}\left(C_{0,1}^{\tilde{\alpha}}\right)^{-1}\left(\begin{array}{cc}
1 & 2 \pi i \tilde{r} \\
0 & 1
\end{array}\right) C_{0,1}^{\tilde{\alpha}} D^{\hat{\alpha}, \hat{\beta}} .$$
By straightforward computations one can easily check that, for
$$\tilde{s}=-\frac{\exp (2 i \pi \beta) \Gamma(\hat{\beta}+\hat{\alpha}) \Gamma(1-\hat{\beta}+\hat{\alpha}) \Gamma(1-\hat{\alpha}) \Gamma(-\hat{\alpha})}{\Gamma(-\hat{\beta}-\hat{\alpha}) \Gamma(1+\hat{\beta}-\hat{\alpha}) \hat{\alpha} \Gamma(\hat{\alpha})^{2}} s$$
i.e. for
$$\frac{\tilde{r}}{\hat{r}}=-\frac{\Gamma\left(1-\sigma_{0}\right)^{2} \Gamma\left(\frac{\sigma_{0}}{2}\right)^{2}}{\Gamma\left(1+\sigma_{0}\right)^{2} \Gamma\left(-\frac{\sigma_{0}}{2}\right)^{2}} \frac{\Gamma\left(1+\frac{\vartheta_{\infty}+\sigma_{0}}{2}\right) \Gamma\left(1+\frac{-\vartheta_{\infty}+\sigma_{0}}{2}\right)}{\Gamma\left(1+\frac{\vartheta_{\infty}-\sigma_{0}}{2}\right) \Gamma\left(1-\frac{\vartheta_{\infty}+\sigma_{0}}{2}\right)} \frac{s}{r},$$
the formulae (2.41), (2.42) hold true.
To conclude the proof we have to prove the relation (2.43), namely we want to prove that $\frac{\tilde{r}}{\hat{r}}=-\frac{1}{4 a_{0}} \frac{2 \mu+\sigma_{0}}{2 \mu-\sigma_{0}}$. To this aim we compute the matrices $A_{0,1, x}^{0}$ and $\Lambda$ and then the asymptotic behaviour of $y$ in terms of $\sigma_{0}$ and $\tilde{r}$. To compute the matrices $A_{0,1, x}^{0}$ and $\Lambda$ we observe that, thanks to the gauges (2.60),
$$A_{1}^{0}=\hat{B}_{1}, \quad \Lambda=\hat{B}_{0}+\frac{\hat{\alpha}+\hat{\beta}}{2} \mathbf{1}, \quad A_{0, x}^{0}=G_{0}^{\hat{\alpha}, \hat{\beta}} \tilde{B}_{0,1}\left(G_{0}^{\hat{\alpha}, \hat{\beta}}\right)^{-1} .$$
First of all one has to compute the $B_{0,1}$ :
$$B_{0}=G_{0}^{\alpha, \beta, \gamma} J_{0}\left(G_{0}^{\alpha, \beta, \gamma}\right)^{-1}, \quad B_{1}=G_{1}^{\alpha, \beta, \gamma} J_{1}\left(G_{1}^{\alpha, \beta, \gamma}\right)^{-1}$$
then
$$\hat{B}_{0}=\frac{1}{\hat{\beta}-\hat{\alpha}}\left(\begin{array}{cc}
\alpha^{2} & -\hat{r} \hat{\alpha} \beta \\
\frac{\hat{\alpha} \beta}{\hat{r}} & -\hat{\beta}^{2}
\end{array}\right), \quad \hat{B}_{1}=\frac{\hat{\alpha} \hat{\beta}}{\hat{\beta}-\hat{\alpha}}\left(\begin{array}{cc}
-1 & \hat{r} \\
-\frac{1}{\hat{r}} & 1
\end{array}\right),$$
and
$$\tilde{B}_{1}=\frac{\tilde{\alpha}}{2}\left(\begin{array}{cc}
-1 & \tilde{r} \\
-\frac{1}{\tilde{r}} & 1
\end{array}\right), \quad \tilde{B}_{0}=-\frac{\tilde{\alpha}}{2}\left(\begin{array}{cc}
1 & \tilde{r} \\
-\frac{1}{\tilde{r}} & -1
\end{array}\right) .$$

It is then obvious that, referring to (2.49) and (2.50), $b=\tilde{r}, T=G_{0}^{\hat{\alpha}, \hat{\beta}}$. Using the formula (2.18),
$$y(x) \sim-\frac{\hat{r}\left(\sigma_{0}+2 \mu\right)}{4 \tilde{r}\left(2 \mu-\sigma_{0}\right)} x^{1-\sigma_{0}} .$$
This proves the formula (2.43) and concludes the proof of the theorem, in the case $\sigma_{0} \neq 0$.
For completeness we write here the result for the matrices $A_{0,1, x}^{0}$ and $\Lambda$ :
$$\begin{gathered}
\Lambda=\frac{1}{4 \vartheta_{\infty}\left(\begin{array}{cc}
-\vartheta_{\infty}^{2}-\sigma_{0}^{2} & \left(-\vartheta_{\infty}^{2}+\sigma_{0}^{2}\right) \hat{r} \\
\frac{-\sigma_{0}^{2}+\vartheta_{\infty}^{2}}{\hat{r}} & \vartheta_{\infty}^{2}+\sigma_{0}^{2}
\end{array}\right), \quad A_{1}^{0}=\frac{\vartheta_{\infty}^{2}-\sigma_{0}^{2}}{4 \vartheta_{\infty}}\left(\begin{array}{cc}
-1 & \hat{r} \\
-\frac{1}{\hat{r}} & 1
\end{array}\right),} \\
A_{0}^{0}=\frac{1}{8 \theta}\left(\begin{array}{l}
\frac{\theta^{2}-\sigma_{0}^{2}}{2}\left(\frac{\tilde{r}}{\hat{r}}+\frac{\hat{r}}{\tilde{r}}\right)-\theta^{2}-\sigma_{0}^{2} \\
\frac{1}{\hat{r}}\left(-\frac{\left(\theta-\sigma_{0}\right)^{2} \hat{r}}{2 \tilde{r}}-\frac{\left(\theta+\sigma_{0}\right)^{2} \tilde{r}}{2 \hat{r}}+\theta^{2}-\sigma_{0}^{2}\right) \\
\hat{r}\left(\frac{\left(\theta-\sigma_{0}\right)^{2} \tilde{r}}{2 \hat{r}}+\frac{\left(\theta+\sigma_{0}\right)^{2} \hat{r}}{2 \tilde{r}}+\sigma_{0}^{2}-\theta^{2}\right) \\
-\frac{\theta^{2}-\sigma_{0}^{2}}{2}\left(\frac{\tilde{r}}{\hat{r}}+\frac{\hat{r}}{\tilde{r}}\right)+\theta^{2}+\sigma_{0}^{2}
\end{array}\right) \\
A_{x}^{0}=\frac{1}{8 \vartheta_{\infty}}\left(\begin{array}{l}
\frac{\sigma_{0}^{2}-\vartheta_{\infty}^{2}}{2}\left(\frac{\tilde{r}}{\hat{r}}+\frac{\hat{r}}{\tilde{r}}\right)-\vartheta_{\infty}^{2}-\sigma_{0}^{2} \\
\frac{1}{\hat{r}}\left(\frac{\left(\vartheta_{\infty}-\sigma_{0}\right)^{2} \hat{r}}{2 \tilde{r}}+\frac{\left(\vartheta_{\infty}+\sigma_{0}\right)^{2} \tilde{r}}{2 \hat{r}}+\vartheta_{\infty}{ }^{2}-\sigma_{0}^{2}\right) \\
\hat{r}\left(-\frac{\left(\vartheta_{\infty}-\sigma_{0}\right)^{2} \tilde{r}}{2 \hat{r}}-\frac{\left(\vartheta_{\infty}+\sigma_{0}\right)^{2} \hat{r}}{2 \tilde{r}}+\sigma_{0}^{2}-\vartheta_{\infty}^{2}\right) \\
\left.\frac{\vartheta_{\infty}^{2}-\sigma_{0}^{2}}{2}\left(\frac{\tilde{r}}{\hat{r}}+\frac{\hat{r}}{\tilde{r}}\right)+\vartheta_{\infty}^{2}+\sigma_{0}^{2}\right)
\end{array}\right) .
\end{gathered}$$
2.2.4. Case $\sigma_{0}=0$. In this case the solution of the system $(\hat{\Sigma})$ has logarithmic behaviour around 0. Moreover, as seen before, it has a logarithmic behaviour around 1. For this system we can use all the formulae derived for $(\widetilde{\Sigma})$, substituting $\tilde{\alpha}$ by $\hat{\alpha}$. The treatment of the $(\tilde{\Sigma})$, is even easier. Ideed in this case $\Lambda$ has zero eigenvalues and it is straightforward to solve the system (2.52) exactly. In fact in this case we have
$$\tilde{B}_{0}+\tilde{B}_{1}=\left(\begin{array}{ll}
0 & 1 \\
0 & 0
\end{array}\right), \quad \operatorname{det} \tilde{B}_{i}=\operatorname{Tr} \tilde{B}_{i}=0, \quad i=0,1 .$$
Then the matrices $\tilde{B}_{0}$ and $\tilde{B}_{1}$ are uniquely determined up to an arbitrary parameter $s$ :
$$\tilde{B}_{0}=\left(\begin{array}{ll}
0 & s \\
0 & 0
\end{array}\right), \quad \tilde{B}_{1}=\left(\begin{array}{cc}
0 & 1-s \\
0 & 0
\end{array}\right),$$
and we can solve the differential equation (2.52) explicitly:
$$\tilde{Y}=\left(\begin{array}{cc}
1 & s \log z+(1-s) \log (z-1) \\
0 & 1
\end{array}\right) .$$

The solution $\tilde{Y}$ has the following asymptotic behaviour near the singular points:
$$\begin{aligned}
\tilde{Y} & =\left(\mathbf{1}+\mathcal{O}\left(\frac{1}{z}\right)\right) z^{J}, \quad \text { as } \quad z \rightarrow \infty, \\
& =\tilde{G}_{0}(\mathbf{1}+\mathcal{O}(z)) z^{J} \tilde{C}_{0}, \quad \text { as } \quad z \rightarrow 0, \\
& =\tilde{G}_{1}(\mathbf{1}+\mathcal{O}(z-1))(z-1)^{J} \tilde{C}_{1} \quad \text { as } \quad z \rightarrow 1,
\end{aligned}$$
where $J=\left(\begin{array}{ll}0 & 1 \\ 0 & 0\end{array}\right)$. It's easy to verify that
$$\tilde{C}_{0}=\left(\begin{array}{cc}
1 & 0 \\
0 & s
\end{array}\right), \quad \tilde{C}_{1}=\left(\begin{array}{cc}
1 & 0 \\
0 & 1-s
\end{array}\right), \quad \tilde{G}_{0}=\left(\begin{array}{cc}
1 & 0 \\
0 & \frac{1}{s}
\end{array}\right), \quad \tilde{G}_{1}=\left(\begin{array}{cc}
1 & 0 \\
0 & \frac{1}{1-s}
\end{array}\right) .$$
As a consequence the monodromy matrices of the system (2.52) are
$$\tilde{M}_{0}=\left(\begin{array}{cc}
1 & 2 \pi i s \\
0 & 1
\end{array}\right), \quad \tilde{M}_{1}=\left(\begin{array}{cc}
1 & 2 \pi i(1-s) \\
0 & 1
\end{array}\right) .$$
The correspondent monodromy matrices of the full system (2.2) are given by:
$$M_{1}=\left(C_{1}^{\hat{\alpha}}\right)^{-1}\left(\begin{array}{cc}
1 & 2 i \pi \hat{r} \\
0 & 1
\end{array}\right) C_{1}^{\hat{\alpha}}, \quad \text { and } \quad M_{0, x}=\left(C_{0}^{\hat{\alpha}}\right)^{-1} \tilde{M}_{0,1} C_{0}^{\hat{\alpha}},$$
where
$$C_{0}^{\hat{\alpha}}=\left(\begin{array}{cc}
\frac{\pi \Gamma(2 \hat{\alpha})}{\Gamma^{2}(\hat{\alpha}) \sin \pi \hat{\alpha}} & \hat{r} \frac{\pi \Gamma(-2 \hat{\alpha})}{\Gamma^{2}(-\hat{\alpha}) \sin \pi \hat{\alpha}} \\
-\frac{1}{\hat{r}} \frac{\Gamma(2 \hat{\alpha}) \exp (-i \pi \hat{\alpha})}{\Gamma^{2}(\hat{\alpha})} & \frac{\Gamma(-2 \hat{\alpha}) \exp (i \pi \hat{\alpha})}{\Gamma^{2}(-\hat{\alpha})}
\end{array}\right),$$
and
$$C_{1}^{\hat{\alpha}}=\left(\begin{array}{cc}
\frac{\pi \Gamma(2 \hat{\alpha}) \exp (-i \pi \hat{\alpha})}{\Gamma^{2}(\hat{\alpha}) \sin \pi \hat{\alpha}} & -\hat{r} \frac{\pi \Gamma(-2 \hat{\alpha}) \exp (i \pi \hat{\alpha})}{\Gamma^{2}(-\hat{\alpha}) \sin \pi \hat{\alpha}} \\
-\frac{1}{\hat{r}} \frac{\Gamma(2 \hat{\alpha})}{\Gamma^{2}(\hat{\alpha})} & -\frac{\Gamma(-2 \hat{\alpha})}{\Gamma^{2}(-\hat{\alpha})}
\end{array}\right) .$$
We observe that
$$\hat{C}_{0,1}^{\hat{\alpha}}=C^{0,1} D^{\hat{\alpha}},$$
where
$$D^{\hat{\alpha}}=\left(\begin{array}{cc}
\frac{\pi \Gamma(2 \hat{\alpha}) \exp (-i \pi \hat{\alpha})}{\Gamma(\hat{\alpha})^{2} \sin \pi \hat{\alpha}} & 0 \\
0 & \frac{-\Gamma(-2 \hat{\alpha})}{\Gamma(-\hat{\alpha})^{2}}
\end{array}\right),$$
and
$$C^{0}=\left(\begin{array}{cc}
\exp (i \pi \hat{\alpha}) & \frac{-\hat{r} \pi}{\sin \pi \hat{\alpha}} \\
\frac{-\sin \pi \hat{\alpha}}{\pi \hat{r}} & \exp (i \pi \hat{\alpha})
\end{array}\right), \quad C^{1}=\left(\begin{array}{cc}
1 & \frac{\hat{r} \pi \exp (i \pi \hat{\alpha})}{\sin \pi \hat{\alpha}} \\
\frac{-\sin \pi \hat{\alpha} \exp (i \pi \hat{\alpha})}{\pi \hat{r}} & 1
\end{array}\right) .$$
We can factor out the diagonal matrix $D^{\hat{\alpha}}$ in (2.65), and take $\hat{r}=1$. In this way, we obtain the formulae (2.45), (2.46), (2.47). The asymptotic behaviour of $y(x)$ can be computed as before. For $\sigma_{0}=0$ we obtain:
$$y \sim a_{0} x \quad \text { for } \quad a_{0}=s .$$