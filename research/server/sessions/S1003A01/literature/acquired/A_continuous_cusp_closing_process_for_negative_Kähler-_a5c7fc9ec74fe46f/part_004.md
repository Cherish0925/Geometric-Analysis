---
retention_scope: session
part: 4
total_parts: 5
---

[Part 4/5 of: A continuous cusp closing process for negative Kähler- ...]

It remains to prove (3) and (4). The key point, carried out below, is to prove that if $|u| \leqslant C s^{-\delta}$, then $u$ actually has an expansion as $s \rightarrow 0$ and as $s \rightarrow 1$. The expansion as $s \rightarrow 1$ proves (2) for a general $u$. The expansion as $s \rightarrow 0$ proves (3) for a general $u$, with some constant as the leading term $(=: u(0))$ but without the sign information on $C_{1}, C_{2}$. For $u=\hat{u}$ we already know that $\hat{u}(0)=1$. In this case it is then easy to see that $C_{2}>0$ by plugging the expansion into the ODE $L_{\infty} \hat{u}=0$ (here the estimate (4.20) up to two derivatives is crucial). Then $C_{1}>0$ also follows: if $C_{1}<0$, then $\hat{u}$ would
obviously be strictly increasing for a short time, which contradicts (1); if $C_{1}=0$, the same argument applies because we already know that $C_{2}>0$. Lastly, (4) follows by applying the maximum principle to $u-u(0) \hat{u}$ because the expansion tells us that $u-u(0) \hat{u}$ vanishes as $s \rightarrow 0^{+}$and as $s \rightarrow 1^{-}$.

It remains to prove that a general solution $u$ to $L_{\infty} u=0$ on $(0,1)$ with $|u| \leqslant C s^{-\delta}$ for some $\delta \in(0,1)$ satisfies the expansions (2) and (3). For this, we use the standard general formula
$$u(x)=c_{1} h_{1}(x)+c_{2} h_{2}(x)+h_{1}(x) \int_{x}^{x_{0}} \frac{h_{2}(t) f(t)}{w(t) a(t)} d t-h_{2}(x) \int_{x}^{x_{0}} \frac{h_{1}(t) f(t)}{w(t) a(t)} d t$$
for solutions to $a u^{\prime \prime}+b u^{\prime}+c u=f$, where $h_{1}, h_{2}$ are two fundamental solutions to the homogeneous equation, $w=h_{1} h_{2}^{\prime}-h_{1}^{\prime} h_{2}$ is their Wronskian, $x_{0}$ is an arbitrary point and $c_{1}, c_{2}$ are constants.

We start with the easier case, $s \rightarrow 1^{-}$, which will give us (2) for a general $u$. By Lemmas 4.3-4.4 and (4.23), for any $\eta_{0} \in(0,1)$ there exist constants $c_{1}, c_{2}$ such that for all $\eta \in(0,1)$,
$$\begin{array}{r}
u(1-\eta)=c_{1} \eta^{n+1}+c_{2} \eta^{-1}+\eta^{n+1} \int_{\eta}^{\eta_{0}} t^{-n-2} f(t) d t-\eta^{-1} \int_{\eta}^{\eta_{0}} f(t) d t, \\
|f(\eta)| \leqslant c \eta^{n+1}\left(\eta^{2}\left|u^{\prime \prime}(1-\eta)\right|+\eta\left|u^{\prime}(1-\eta)\right|+|u(1-\eta)|\right)
\end{array}$$
for some dimensional constant $c$. We are assuming that $|u(1-\eta)|=O(1)$ as $\eta \rightarrow 0^{+}$.
Claim 4.6. We actually have that
$$|u(1-\eta)|+\eta\left|u^{\prime}(1-\eta)\right|+\eta^{2}\left|u^{\prime \prime}(1-\eta)\right|=O(1) \text { as } \eta \rightarrow 0^{+} .$$
Proof of Claim 4.6. We will first show that there exist $\varepsilon \in(0,1)$ and $C>0$ independent of $\eta$ such that for any fixed $0<\eta \ll 1$ the following sub-claim is true.

Sub-Claim 4.7. Define $F:[0,1] \rightarrow[0, \infty)$ via $F(\rho):=\max _{[\eta,(1+\rho) \eta]}\left|u^{\prime}(1-\cdot)\right|$. Then
$$F(\rho) \leqslant \varepsilon \cdot F(R)+\frac{C}{\eta}(R-\rho)^{-1} \text { for all } 0 \leqslant \rho<R \leqslant 1 \text {. }$$

If Sub-Claim 4.7 is true, then by a standard calculus iteration lemma (see [20, Lemma 3.4] based on [14, Lemma 8.18], or many other sources) there exists a universal $C_{0}=C_{0}(\varepsilon)$ such that
$$F(\rho) \leqslant C_{0} \frac{C}{\eta}(1-\rho)^{-1} \text { for all } 0 \leqslant \rho<1 .$$
Setting $\rho=0$ in (4.28) and using $L_{\infty} u=0$ to solve for $u^{\prime \prime}$ in terms of $u, u^{\prime}$, we obtain Claim 4.6.
Proof of Sub-Claim 4.7. We will prove (4.27) by a simple interpolation argument. Let $\tilde{u}:=u(1-\cdot)$. For any $0<\varepsilon \leqslant \frac{1}{10}$ and any $\eta_{*} \in[\eta,(1+\rho) \eta]$, expand
$$\tilde{u}\left(\eta_{*}+\varepsilon(R-\rho) \eta\right)=\tilde{u}\left(\eta_{*}\right)+\int_{\eta_{*}}^{\eta_{*}+\varepsilon(R-\rho) \eta}\left[\tilde{u}^{\prime}\left(\eta_{*}\right)+\int_{\eta_{*}}^{\xi} \tilde{u}^{\prime \prime}(\tilde{\xi}) d \tilde{\xi}\right] d \xi .$$
Then solve this equation for $\tilde{u}^{\prime}\left(\eta_{*}\right)$, express $\tilde{u}^{\prime \prime}$ in terms of $\tilde{u}^{\prime}$ and $\tilde{u}$ using the ODE $L_{\infty} u=0$, take the maximum over all $\eta_{*} \in[\eta,(1+\rho) \eta]$, and fix $\varepsilon$ sufficiently small depending only on $n$. \(\square\)

Plugging Claim 4.6 into (4.25), we get that $|f(\eta)|=O\left(\eta^{n+1}\right)$ as $\eta \rightarrow 0^{+}$. Inserting this into (4.24), letting $\eta \rightarrow 0^{+}$and using the boundedness of the left-hand side, we deduce that
$$c_{2}-\int_{0}^{\eta_{0}} f(t) d t=0$$
As a consequence, $|u(1-\eta)|=O\left(\eta^{n+1}|\log \eta|\right)$ as $\eta \rightarrow 0^{+}$. This would already be enough for us but another iteration easily yields the expected $|u(1-\eta)|=O\left(\eta^{n+1}\right)$, i.e., (2) holds for a general $u$.

To finish the proof, we now deal with the more difficult case $s \rightarrow 0^{+}$, i.e., statement (3). As above, and using also the fact that $a(t) w(t)=-\frac{n+1}{2}=$ const in this case, we have that
$$\begin{array}{r}
u(s)=c_{1} h_{1}^{-}(s)+c_{2} h_{2}^{-}(s)+h_{1}^{-}(s) \int_{s}^{s_{0}} h_{2}^{-}(t) f(t) d t-h_{2}^{-}(s) \int_{s}^{s_{0}} h_{1}^{-}(t) f(t) d t, \\
h_{1}^{-}(s)=c_{1,1} s^{\frac{1}{n}}+O\left(s^{\frac{n+2}{n}}\right), h_{2}^{-}(s)=c_{2,0}+c_{2,1} s^{\frac{1}{n}}+c_{2,2} s^{\frac{n+1}{n}}+O\left(s^{\frac{n+2}{n}}\right), \\
|f(s)| \leqslant c s^{\frac{n+1}{n}}\left(s^{\frac{n-1}{n}}\left|u^{\prime \prime}(s)\right|+s^{-\frac{1}{n}}\left|u^{\prime}(s)\right|+|u(s)|\right)
\end{array}$$
for some dimensional constants $c_{1,1}, c_{2,0}, c_{2,1}, c_{2,2}, c$. We are assuming that $|u(s)|=O\left(s^{-\delta}\right)$ as $s \rightarrow 0^{+}$ for some fixed $\delta \in(0,1)$. From this and from the ODE $L_{\infty} u=0$, we get
$$|u(s)|+s\left|u^{\prime}(s)\right|+s^{2}\left|u^{\prime \prime}(s)\right|=O\left(s^{-\delta}\right) \text { as } s \rightarrow 0^{+}$$
as in the proof of Claim 4.6. This again directly fits into (4.33), yielding an estimate $|f(s)|=O\left(s^{-\delta}\right)$ as $s \rightarrow 0^{+}$. Because of this, the integrals in (4.31) converge as $s \rightarrow 0^{+}$. In particular, $|u(s)|=O(1)$ as $s \rightarrow 0^{+}$. Again arguing as in the proof of Claim 4.6, this implies that
$$|u(s)|+s\left|u^{\prime}(s)\right|+s^{2}\left|u^{\prime \prime}(s)\right|=O(1) \text { as } s \rightarrow 0^{+},$$
so $|f(s)|=O(1)$. Writing $\int_{s}^{s_{0}}=\int_{0}^{s_{0}}-\int_{0}^{s}$ in (4.31), we thus obtain with new constants $\tilde{c}_{1}, \tilde{c}_{2}$ that
$$u(s)=\tilde{c}_{1} h_{1}^{-}(s)+\tilde{c}_{2} h_{2}^{-}(s)-h_{1}^{-}(s) \int_{0}^{s} h_{2}^{-}(t) f(t) d t+h_{2}^{-}(s) \int_{0}^{s} h_{1}^{-}(t) f(t) d t$$
where $|f(s)|=O(1)$. By itself this says that $u(s)=d_{0}+d_{1} s^{1 / n}+O\left(s^{(n+1) / n}\right)$, which is good but not enough. We now use this information to prove that $|f(s)|=O\left(s^{1 / n}\right)$. (Once we have this, we can feed it back into (4.36) to get that the two inhomogeneous terms are in fact $O\left(s^{(n+2) / n}\right)$, and this is the pointwise part of the desired estimate (4.20).) Here we need to be a bit more careful than before.

Consider again (4.33). The third term is negligible because $|u(s)|=O(1)$. For the first and second term, (4.35) and its proof tell us nothing new because these arguments are based on upper bounds and the upper bound $|u(s)|=O(1)$ cannot be improved. However, we now have enough information to use (4.36) directly. In fact, we can simply take one derivative of (4.36) and use $|f(s)|=O(1)$ to bound $s\left|u^{\prime}(s)\right|=O\left(s^{1 / n}\right)$. Then, from the ODE $L_{\infty} u=0$,
$$s^{2}\left|u^{\prime \prime}(s)\right| \leqslant O(s)\left|u^{\prime}(s)\right|+O\left(s^{\frac{n+1}{n}}\right)|u(s)|+O\left(s^{\frac{n+1}{n}}\right)|f(s)|=O\left(s^{\frac{1}{n}}\right),$$
using what we already know about $u^{\prime}, u, f$. Thus, from (4.33), $|f(s)|=O\left(s^{1 / n}\right)$. By feeding this back into (4.36), $|R(s)|=O\left(s^{(n+2) / n}\right)$ in (4.20). This is the pointwise part of the desired expansion (3).

We still need to prove the derivative estimates of $R(s)$ in (4.20) (as, without these, we would not be able to plug the expansion of $\hat{u}$ back into the ODE and deduce the sign of $C_{1}, C_{2}$, which is crucial). First, $s\left|R^{\prime}(s)\right|=O\left(s^{(n+2) / n}\right)$ is easily proved by differentiating the inhomogeneous terms in (4.36) and using that $|f(s)|=O\left(s^{1 / n}\right)$. Notice that the terms obtained by letting $d / d s$ act on the integral signs cancel out. Thus, when we differentiate one more time to estimate $R^{\prime \prime}$, there is no need for a bound on $f^{\prime}$, and $|f(s)|=O\left(s^{1 / n}\right)$ implies $s^{2}\left|R^{\prime \prime}(s)\right|=O\left(s^{(n+2) / n}\right)$. So (3) is proved for a general $u$. \(\square\)
4.1.4. Solving $L_{\infty} \hat{v}=\hat{u}$ with a Neumann boundary condition on the left. The inhomogeneous ODE $L_{\infty} v=\hat{u}$ has a 2-dimensional affine space of solutions on (0, 1). For the sake of transplanting $v$ to the approximating manifolds, we again require that $v(s) \rightarrow$ const as $s \rightarrow 0^{+}$and $s \rightarrow 1^{-}$. As in Section 4.1.3 this singles out a 1-dimensional affine subspace of solutions, any two members of which differ by a scalar multiple of $\hat{u}$. What makes things work in the end is the fact that there exists a canonical element $\hat{v}$ of this 1-dimensional affine subspace that satisfies a Neumann boundary condition at $s=0$. We also need to know that $\hat{v} \leqslant 0$ and $\hat{v}(0) \neq 0$, but the precise value of $\hat{v}(0)$ is irrelevant.

Lemma 4.8. There exists a solution $\hat{v} \leqslant 0$ to the inhomogeneous ODE $L_{\infty} \hat{v}=\hat{u}$ on $(0,1)$ such that
$$\begin{array}{r}
|\hat{v}(1-\eta)|+\eta\left|\hat{v}^{\prime}(1-\eta)\right|+\eta^{2}\left|\hat{v}^{\prime \prime}(1-\eta)\right|=O\left(\eta^{n+1}\right) \text { as } \eta \rightarrow 0^{+}, \\
\hat{v}(s)=C_{0}+C_{2} s^{\frac{n+1}{n}}+R(s),|R(s)|+s\left|R^{\prime}(s)\right|+s^{2}\left|R^{\prime \prime}(s)\right|=O\left(s^{\frac{n+2}{n}}\right) \text { as } s \rightarrow 0^{+},
\end{array}$$
where $C_{0}, C_{2}$ are constants and $C_{0} \neq 0$.
This satisfies a Neumann condition in the sense that the expected term $C_{1} s^{1 / n}$ in (4.39) vanishes.
Proof. We begin by constructing one particular solution $v$ to the ODE, which may not be the one we seek. For this we proceed as in the proof of Lemma 4.5, i.e., by solving Dirichlet rather than Neumann problems. Thus, for any fixed $\varepsilon \in(0,1)$ let $v_{\varepsilon}:[\varepsilon, 1-\varepsilon] \rightarrow \mathbb{R}$ be the unique solution to $L_{\infty} v_{\varepsilon}=\left.\hat{u}\right|_{[\varepsilon, 1-\varepsilon]}$ with $v(\varepsilon)=-1$ and $v(1-\varepsilon)=0$. At an interior maximum we must have that $-v_{\varepsilon} \geqslant L_{\infty} v_{\varepsilon}=\hat{u}$, i.e., $v_{\varepsilon} \leqslant-\hat{u} \leqslant 0$, and at an interior minimum we must have that $-v_{\varepsilon} \leqslant L_{\infty} v_{\varepsilon}=\hat{u}$, i.e., $v_{\varepsilon} \geqslant-\hat{u} \geqslant-1$. Thus, by comparison with the boundary values, $-1 \leqslant v_{\varepsilon} \leqslant 0$. Up to a subsequence, we can now pass to a limit $v:(0,1) \rightarrow \mathbb{R}$ locally smoothly. Clearly $L_{\infty} v=\hat{u}$ and $-1 \leqslant v \leqslant 0$.

A barrier argument as in the proof of Lemma 4.5 yields $\lim _{s \rightarrow 0^{+}} v(s)=-1$ and $\lim _{s \rightarrow 1^{-}} v(s)=0$. Indeed, consider the function $\hat{u}_{\text {sub }}(s)=1-C_{1} s^{1 / n}+C_{2} s^{(n+1) / n}$ from the previous proof, which satisfies $\hat{u}_{\text {sub }}\left(s_{*}\right)=0$ and $L_{\infty} \hat{u}_{\text {sub }} \geqslant 0$ on $\left(0, s_{*}\right]$ for some small dimensional $s_{*} \in(0,1)$. Then $v^{\text {sup }}:=-\hat{u}_{\text {sub }}$ trivially satisfies $L_{\infty} v^{\text {sup }} \leqslant 0 \leqslant \hat{u}$, so we can use $v^{\text {sup }}$ as an upper barrier for $v_{\varepsilon}$ on $\left[\varepsilon, s_{*}\right]$, proving that $\lim _{s \rightarrow 0^{+}} v(s)=-1$. For $s \rightarrow 1^{-}$almost the same trick works. From the proof of Lemma 4.5 we know that $\hat{u}^{\text {sup }}(1-\eta)=C_{1} \eta^{n+1}-C_{2} \eta^{2 n+2}$ satisfies $\hat{u}^{\text {sup }}\left(1-\eta_{*}\right)=1$ and $L_{\infty} \hat{u}^{\text {sup }} \leqslant 0$ on $\left[1-\eta_{*}, 1\right)$ for a small universal $\eta_{*} \in(0,1)$. Then we would like to use $v_{\text {sub }}:=-\hat{u}^{\text {sup }}$ as a lower barrier for $v_{\varepsilon}$ on $\left[1-\eta_{*}, 1-\varepsilon\right]$. This does not work immediately because we only have $L_{\infty} v_{s u b} \geqslant 0$ but not $L_{\infty} v_{s u b} \geqslant \hat{u}$. However, we can improve the construction of $\hat{u}^{\text {sup }}$ slightly by choosing $\eta_{*}$ small enough so that $\left(2 C_{*}^{\prime}+C_{*}^{\prime \prime \prime}\right) \eta_{*}^{n+1} \leqslant$ $(1 / 2)(\gamma(\gamma-n) /(n+1)-1)$ in the previous proof, hence $L_{\infty} v_{\text {sub }} \geqslant(1 / 2)(\gamma(\gamma-n) /(n+1)-1)>0$ on $\left[1-\eta_{*}, 1\right)$. Since we already know that $\hat{u}(1-\eta)=O\left(\eta^{n+1}\right)$ with a dimensional constant, this means we can arrange that $L_{\infty} v_{\text {sub }} \geqslant \hat{u}$ on $\left[1-\eta_{*}, 1\right)$ by making $\eta_{*}$ even smaller if necessary.

To sum up, we have constructed a solution $v:(0,1) \rightarrow \mathbb{R}$ to $L_{\infty} v=\hat{u}$ with $-1 \leqslant v \leqslant 0$ as well as $\lim _{s \rightarrow 0^{+}} v(s)=-1$ and $\lim _{s \rightarrow 1^{-}} v(s)=0$. In fact, $v(1-\eta)=O\left(\eta^{n+1}\right)$ as $\eta \rightarrow 0^{+}$, and by using Lemma 4.5(2) and the interpolation argument proving (4.26) we can easily upgrade this to (4.38). Also as in the proof of Lemma 4.5, we can now prove that $v(s)=-1+C_{1} s^{1 / n}+C_{2} s^{(n+1) / n}+R(s)$, where $R(s)=O\left(s^{(n+2) / n}\right)$ with two derivatives as in (4.20) or (4.39). In fact, nothing needs to be changed in the proof except that $\hat{u}(s)=1+O\left(s^{1 / n}\right)$ needs to be added to $f$.

Having proved this expansion of $v$, we note that if $C_{1}=0$, then we are done with $\hat{v}:=v$. Otherwise we can replace $v$ by $\hat{v}:=v+\lambda \hat{u}$ for some $\lambda \neq 0$ to make the $s^{1 / n}$ term vanish. Then we also need to make sure that $\hat{v} \leqslant 0$ and $\hat{v}(0) \neq 0$. By the maximum principle, it is enough to prove that $\hat{v}(0)<0$, which we do by contradiction. If $\hat{v}(0) \geqslant 0$, then the constant term of $\hat{v}(s)$ is nonnegative and the $s^{1 / n}$ term vanishes. Thus, in order to have $L_{\infty} \hat{v}(s)=\hat{u}(s)=1+O\left(s^{1 / n}\right)$, we need $C_{2}>0$ (again thanks to the fact that $R(s)$ is estimated with two derivatives). Thus, $\hat{v}(s)>\hat{v}(0)$ for $0<s \ll 1$. But this contradicts the inequality $\hat{v} \leqslant \hat{v}(0)$, which holds by the maximum principle. \(\square\)
4.1.5. Definition of the obstruction function. For all $0<|\sigma| \ll 1$ we first choose an $s_{*, \sigma} \in\left(0, \frac{1}{5}\right]$ with
$$\max \left\{3|T|^{\alpha-1}, 3 \frac{\tau}{T}\right\} \leqslant s_{*, \sigma} \rightarrow 0 \text { as } \sigma \rightarrow 0 .$$
Then we choose a smooth function $\chi_{\sigma}:(0,1) \rightarrow[0,1]$ such that
$$\chi_{\sigma}(s)=\left\{\begin{array}{ll}
0 & \text { for } s \in\left(0, s_{*, \sigma}\right] \\
1 & \text { for } s \in\left[2 s_{*, \sigma}, 1\right)
\end{array}\right\} \text { and } s_{*, \sigma}\left|\chi_{\sigma}^{\prime}\right|+s_{*, \sigma}^{2}\left|\chi_{\sigma}^{\prime \prime}\right| \leqslant C$$
for some constant $C$ independent of $\sigma$. Now recall Convention 4.1: We identify $\Re_{4} \subset \mathcal{X}_{\sigma}$ with the set $\left\{T+2 T_{0}<t<2 \tau\right\} \subset T Y_{0}$ using the diffeomorphism $\Phi_{\sigma}^{-1} \circ \Psi_{\sigma}$. In this way we can view (functions of) $s, \eta$ as functions on $\Re_{4}$. Thus, the following definition makes sense.

Definition 4.9. We define the obstruction function $\hat{u}_{\sigma} \in C^{\infty}\left(\mathcal{X}_{\sigma}\right)$ via $\hat{u}_{\sigma}:=L_{\sigma} \hat{v}_{\sigma}$, where
$$\hat{v}_{\sigma}:=\left[\chi_{\sigma} \hat{v}+\left(1-\chi_{\sigma}\right) \hat{v}(0)\right] \chi_{\sigma}(1-\cdot) \in C^{\infty}\left(\mathcal{X}_{\sigma}\right) .$$
Note that $\hat{v}_{\sigma}$ actually extends smoothly from $\Re_{4}$ to all of $\mathcal{X}_{\sigma}$ because it is constant equal to $\hat{v}(0)$ for $s<s_{*, \sigma}$ and zero for $s>1-s_{*, \sigma}$. By (4.40) this cutoff happens strictly within the boundaries of $\Re_{4}$. Also, $\hat{u}_{\sigma}$ is then constant equal to $-\hat{v}(0)$ to the left of $\Re_{4}$ and zero to the right of $\Re_{4}$.

Lemma 4.10. The obstruction function $\hat{u}_{\sigma}$ satisfies the following properties:
\begin{itemize}
\item[(1)] Fix $s_{1}<s_{2}$ in (0, 1). Lift $\hat{u}_{\sigma}$ and $\hat{u} \circ s$ to functions on the domain of the chart (4.2) on the universal cover of $\left\{s_{1}<s<s_{2}\right\}$. Then $\hat{u}_{\sigma} \rightarrow \hat{u} \circ s$ uniformly as $\sigma \rightarrow 0$.
\item[(2)] There exists a uniform constant $C$ such that $\left|\hat{u}_{\sigma}\right| \leqslant C \eta^{3}$ as functions on $\Re_{4}$ for all $\sigma$.
\end{itemize}

The main content of (2) is that $\hat{u}_{\sigma}$ remains bounded independently of $\sigma$ at the left boundary of $\Re_{4}$. This is not at all obvious due to the poor regularity of $\hat{u}(s)$ and $\hat{v}(s)$ as $s \rightarrow 0$. Here we crucially use the Neumann property of $\hat{v}$. (2) is also the key to the proof of our main result, Proposition 4.2.

Proof of Lemma 4.10. For item (1): From the proof of Lemma 4.3 we know that for $|\sigma| \ll 1$,
$$\begin{aligned}
\hat{u}_{\sigma} & =\left[\left(\Delta_{\omega_{T}}-\mathrm{Id}\right)+\left(\Delta_{\omega_{g l u e, \sigma}}-\Delta_{\omega_{T}}\right)\right] \hat{v}_{\sigma} \\
& =\left(\Delta_{\omega_{T}}-\mathrm{Id}\right) \hat{v}_{\sigma}+O_{s_{1, s_{2}}}\left(e^{-\frac{1}{2}|T|^{\alpha}}\right) \circledast\left(\check{\partial} \hat{v}_{\sigma}, \check{\partial}^{2} \hat{v}_{\sigma}\right) \\
& =L_{\infty} \hat{v}+\left[O_{s_{1}, s_{2}}\left(|b|^{\frac{1}{3}}|\tau|\right)+O_{s_{1}, s_{2}}\left(e^{-\frac{1}{2}|T|^{\alpha}}\right)\right] \circledast\left(\hat{v}^{\prime}, \hat{v}^{\prime \prime}\right) .
\end{aligned}$$
The point is that $\hat{v}_{\sigma}$ is radial in the chart (4.2) and for $|\sigma| \ll 1$ we have $2 s_{*, \sigma}<s_{1}<s_{2}<1-2 s_{*, \sigma}$, so the cutoffs in (4.42) are irrelevant and $\hat{v}_{\sigma}=\hat{v}$. Thus, according to the definition of $L_{\infty}$ as the first line of (4.12), $\left(\Delta_{\omega_{T}}-\mathrm{Id}\right) \hat{v}_{\sigma}$ is equal to $L_{\infty} \hat{v}$ modulo the operator error $O_{\delta}\left(|b|^{1 / 3}|\tau|\right) \hat{v}_{\sigma}$ from the second line of (4.12). Moreover, $\check{\partial}$ reduces to $d / d s$. This explains (4.43). Of course, $L_{\infty} \hat{v}=\hat{u}$, and the rest of the third line of (4.43) obviously goes to zero uniformly as $\sigma \rightarrow 0$.

For item (2): In this proof we prefer to use $n$-dimensional notation for clarity. We fix a sufficiently small but universal $\delta>0$ and distinguish three subregions of $\Re_{4}$ as follows.

Region (a): $s=1-\eta \in[\delta, 1-\delta]$. In this region, item (2) simply states that $\hat{u}_{\sigma}$ is bounded uniformly, independently of $\sigma$, and this statement is trivial from (4.43) for $s_{1}=\delta$ and $s_{2}=1-\delta$.

Region (b): $\eta \in(0, \delta]$. Here the goal is to prove that $\left|\hat{u}_{\sigma}\right| \leqslant C \eta^{n+1}$ with $C$ independent of $\sigma$. We want to argue as in (4.43) but $s_{2}$ is not bounded away from 1, so we need to make the following changes:
\begin{itemize}
\item[-] Use the formula $\hat{v}_{\sigma}=\chi_{\sigma}(1-\cdot) \hat{v}$ instead of $\hat{v}_{\sigma}=\hat{v}$.
\item[-] Instead of using the charts (4.2), which degenerate as $s_{2} \rightarrow 1$, we estimate the difference between $\Delta_{\omega_{\text {glue }, \sigma}}$ and $\Delta_{\omega_{T}}$ covariantly. Recall from Convention 4.1 and Lemma 3.10 that $g_{\text {glue }, \sigma}$ and $g_{T}$ differ from each other by $O\left(e^{-(1 / 2-\varepsilon)(t-T)}\right)=O\left(e^{-(1 / 2)|T|^{\alpha}}\right)$ uniformly over $\Re_{4}$, including derivatives. Also, from Proposition 2.26, $g_{T}$ and $g_{\text {cusp }}$ are uniformly equivalent over $\{0<\eta \leqslant \delta\}$, including derivatives because both are Einstein. Thus, we can estimate
$$\left|\left(\Delta_{\omega_{g l u e, \sigma}}-\Delta_{\omega_{T}}\right) \hat{v}_{\sigma}\right| \leqslant O_{\delta}\left(e^{-\frac{1}{2}|T|^{\alpha}}\right) \sum_{k=1}^{2}\left|\nabla_{\omega_{\text {cusp }}}^{k} \hat{v}_{\sigma}\right|_{\omega_{\text {cusp }}} \leqslant O_{\delta}\left(e^{-\frac{1}{2}|T|^{\alpha}}\right)\left(\eta^{2}\left|\hat{v}_{\sigma}^{\prime \prime}\right|+\eta\left|\hat{v}_{\sigma}^{\prime}\right|\right) .$$
\end{itemize}
- Note that the operator error $O_{\delta}\left(|b|^{1 /(n+1)}|\tau|\right)$ from (4.12) only depends on an upper bound for $\eta$. Thus, using (4.12) and the fact that $\hat{v}_{\sigma}$ is radial, we have on all of $\{0<\eta \leqslant \delta\}$ that
$$\left|\left(\Delta_{\omega_{T}}-\mathrm{Id}\right) \hat{v}_{\sigma}\right|=\left|\left(L_{\infty}+O_{\delta}\left(|b|^{\frac{1}{n+1}}|\tau|\right)\right) \hat{v}_{\sigma}\right| \leqslant O_{\delta}(1)\left(\eta^{2}\left|\hat{v}_{\sigma}^{\prime \prime}\right|+\eta\left|\hat{v}_{\sigma}^{\prime}\right|+\left|\hat{v}_{\sigma}\right|\right) .$$
The desired estimate of $\hat{u}_{\sigma}$ now easily follows from the estimates (4.38) for $\hat{v}$ and (4.41) for $\chi_{\sigma}$.
Region (c): $s \in(0, \delta]$. Here we prove that $\left|\hat{u}_{\sigma}\right| \leqslant C$ with $C$ independent of $\sigma$. We again follow a similar pattern but now need to use (2.154) instead of (2.144) or (4.12). Thus, we proceed as follows:
\begin{itemize}
\item[-] We use the formula $\hat{v}_{\sigma}=\chi_{\sigma} \hat{v}+\left(1-\chi_{\sigma}\right) \hat{v}(0)$.
\item[-] The comparison of $g_{\text {glue }, \sigma}$ and $g_{T}$ is the same as in (b). Then we compare $\omega_{T}$ and $|b|^{1 / 2} \omega_{\mathcal{C}, \sigma}$ using (2.164)-(2.165). The comparison is uniform over $\{0<s \leqslant \delta\}$ and each derivative costs at most a factor of $|T|^{K}(t-T)^{K}$ for some $K>0$ as long as $t-T \geqslant 1$. Thus,
$$\left|\left(\Delta_{\omega_{g l u e, \sigma}}-\Delta_{\omega_{T}}\right) \hat{v}_{\sigma}\right| \leqslant O_{\delta}\left(e^{-\frac{1}{2}|T|^{\alpha}}|T|^{2 K}\right)\left(s^{\frac{n-1}{n}}\left|\hat{v}_{\sigma}^{\prime \prime}\right|+s^{-\frac{1}{n}}\left|\hat{v}_{\sigma}^{\prime}\right|\right) .$$
\item[-] The operator error $O_{\delta}\left(|b|^{1 /(n+1)}|\tau|\right)$ from (2.154) only depends on an upper bound for $s$. Applying (2.154), we therefore get on all of $\{0<s \leqslant \delta\}$ that
$$\left|\left(\Delta_{\omega_{T}}-\mathrm{Id}\right) \hat{v}_{\sigma}\right|=\left|\left(L_{\infty}+O_{\delta}\left(|b|^{\frac{1}{n+1}}|\tau|\right)\right) \hat{v}_{\sigma}\right| \leqslant O_{\delta}(1)\left(s^{\frac{n-1}{n}}\left|\hat{v}_{\sigma}^{\prime \prime}\right|+s^{-\frac{1}{n}}\left|\hat{v}_{\sigma}^{\prime}\right|+\left|\hat{v}_{\sigma}\right|\right) .$$
\end{itemize}
To estimate the right-hand sides of (4.46)-(4.47) we need to be a little more careful than in (b). First notice that the $\left|\hat{v}_{\sigma}\right|$ term in (4.47) is obviously uniformly bounded. Next, $\hat{v}_{\sigma}=\chi_{\sigma}(\hat{v}-\hat{v}(0))+\hat{v}(0)$, so in the remaining terms with $\hat{v}_{\sigma}^{\prime}, \hat{v}_{\sigma}^{\prime \prime}$ we can replace $\hat{v}_{\sigma}$ by $\chi_{\sigma}(\hat{v}-\hat{v}(0))$. Using (4.41) to estimate $\chi_{\sigma}$ and (4.39) to estimate $\hat{v}-\hat{v}(0)$, we get the desired uniform bound. However, at this point it is crucially important that $\hat{v}$ satisfies a Neumann condition at $s=0$, i.e., that the expansion of $\hat{v}-\hat{v}(0)$ starts with $s^{(n+1) / n}$ rather than $s^{1 / n}$. (Otherwise the best bound we could get is $\left|\hat{u}_{\sigma}\right| \leqslant C s^{-1}$, which is not $L_{\text {loc }}^{1}$, destroying the dominated convergence argument in the proof of Proposition 4.2.) \(\square\)
4.1.6. Proof of Proposition 4.2. As $w_{\sigma_{i}}\left(x_{i}\right)\left|\psi_{i}\right| \leqslant w_{\sigma_{i}}$ on $\mathcal{X}_{\sigma_{i}}$ and $x_{i}$ lies in $\Re_{4}$ with $s\left(x_{i}\right) \rightarrow c \in(0,1)$, we can deduce from the definition, (3.110), of the weight function $w_{\sigma_{i}}$ that
$$\left|\psi_{i}\right| \leqslant \begin{cases}C & \text { on } \Re_{1}, \\ C \Psi_{\sigma}^{*}\left(\Phi_{\sigma}^{-1}\right)^{*} s^{-\delta} & \text { on } \Re_{2} \cup \Re_{3} \cup \Re_{4} \cup \Re_{5} \cup \Re_{6}, \\ C\left|T_{i}\right|^{\delta} & \text { on } \Re_{7}\end{cases}$$
Thus, RHS(4.4) exists because (4.48) implies $\left|\psi_{\infty}(s)\right| \leqslant C s^{-\delta}$ for all $s \in(0,1)$, and $|\hat{u}(1-\eta)| \leqslant C \eta^{3}$ from Lemma 4.5 and $\left|\mu_{\infty}(1-\eta)\right| \leqslant C \eta^{-3}$ from Lemma 2.31 for all $\eta \in(0,1)$. We now decompose $\mathcal{X}_{\sigma_{i}}$ into three regions and analyze their contributions to LHS(4.4).

Region $\Re_{1} \cup \Re_{2} \cup \Re_{3}$ : Here we obviously have $\hat{u}_{\sigma_{i}}=0$.
Region $\Re_{5} \cup \Re_{6} \cup \Re_{7}$ : Here $\hat{u}_{\sigma_{i}}$ is constant equal to $-\hat{v}(0)$. In the unrescaled Tian-Yau space, volume grows like $\log h$ as $h \rightarrow \infty$. Thus, the volume of $\Re_{5} \cup \Re_{6} \cup \Re_{7}$ with respect to $\omega_{\text {glue }, \sigma_{i}}$ is bounded by $C\left|b_{i}\right|\left|T_{i}\right|^{\alpha}$. Recalling that $\left|b_{i}\right| \sim\left|T_{i}\right|^{-3}$ and using the bound $\left|\psi_{i}\right| \leqslant C\left|T_{i}\right|^{\delta}$ from (4.48), we get that the total contribution of this region to LHS(4.4) goes to zero provided that $\alpha+\delta<1$. This is consistent with our standing convention that $\alpha, \delta$ are always chosen arbitrarily close to zero.

Region $\Re_{4}$ : By (2.173), the volume form of $\omega_{T_{i}}$ satisfies for all $\eta=1-s \in(0,1)$ that
$$\left.\omega_{T_{i}}^{2}\right|_{t=\eta T_{i}}=\left|T_{i}\right|^{-2} \mu_{T_{i}}(1-\eta) d s \wedge d \theta \wedge d \operatorname{Vol}_{E} .$$

Thus, by Fubini, and using Lemma 3.10 to compare the two volume forms,
$$\left|T_{i}\right|^{2} \int_{\Re_{4}} \psi_{i} \hat{u}_{\sigma_{i}} \omega_{g l u e, \sigma_{i}}^{2}=2 \pi \operatorname{Vol}(E) \int_{2\left|T_{i}\right|^{\alpha-1}}^{1-2 \frac{\tau_{i}}{T_{i}}} \overline{\psi_{i} \hat{u}_{\sigma_{i}}}(s) \mu_{T_{i}}(s)\left(1+O\left(e^{-\frac{1}{2}\left|T_{i}\right|^{\alpha}}\right)\right) d s,$$
where the bar denotes the average over the relevant level set of $s$ with respect to the fixed volume form $d \theta \wedge d \operatorname{Vol}_{E}$. By assumption and by Lemma 4.10, $\psi_{i} \rightarrow \phi_{\infty}$ and $\hat{u}_{\sigma_{i}} \rightarrow \hat{u}$ uniformly on every fixed level set of $s$. Thus, we obviously have that $\overline{\psi_{i} \hat{u}_{i}}(s) \rightarrow \phi_{\infty}(s) \hat{u}(s)$ for every fixed $s$. Thus, the integrand on the right-hand side of (4.50) converges pointwise to $\psi_{\infty}(s) \hat{u}(s) \mu_{\infty}(s)$. It is also uniformly bounded by $C s^{-\delta} \cdot C \eta^{3} \cdot C \eta^{-3} \leqslant C s^{-\delta}$ thanks to (4.48), Lemma 4.10 and Lemma 2.31. Since $C s^{-\delta}$ is integrable on ( 0,1 ), dominated convergence implies that (4.50) converges to the right-hand side of (4.4). \(\square\)
4.2. Statement of the uniform estimate modulo obstructions and set-up of the proof. Here we state the uniform weighted Hölder estimate of the inverse linearized operator modulo obstructions and explain the strategy of the proof. This is the standard blowup-and-contradiction scheme common to this type of problem, and the aim is to obtain a contradiction to some Liouville theorem in each of the 7 cases. In Sections 4.5-4.7 we carry out the details of this scheme in each case.

Definition 4.11. Given the obstruction function $\hat{u}_{\sigma}=L_{\sigma} \hat{v}_{\sigma}$ from Definition 4.9, we define
$$\left\langle\hat{u}_{\sigma}\right\rangle:=\mathbb{R} \cdot \hat{u}_{\sigma} \text { and }\left\langle\hat{v}_{\sigma}\right\rangle:=\mathbb{R} \cdot \hat{v}_{\sigma}$$
as 1-dimensional subspaces of $C^{\infty}\left(\mathcal{X}_{\sigma}\right)$. We also write
$$L_{\sigma}^{\perp}:\left\langle\hat{u}_{\sigma}\right\rangle^{\perp} \rightarrow\left\langle\hat{v}_{\sigma}\right\rangle^{\perp}$$
to denote the restriction of $L_{\sigma}=\Delta_{\omega_{g l u e, \sigma}}-\mathrm{Id}$ to the orthogonal complements of $\left\langle\hat{u}_{\sigma}\right\rangle$ resp. $\left\langle\hat{v}_{\sigma}\right\rangle$ inside $C^{2, \bar{\alpha}}\left(\mathcal{X}_{\sigma}\right)$ resp. $C^{0, \bar{\alpha}}\left(\mathcal{X}_{\sigma}\right)$ with respect to the $L^{2}\left(\mathcal{X}_{\sigma}, \omega_{\text {glue }, \sigma}\right)$-inner product for any $\bar{\alpha} \in(0,1)$. By basic elliptic theory, $L_{\sigma}^{\perp}$ is properly defined and is an isomorphism of Banach spaces.

Theorem 4.12. For all $\bar{\alpha} \in(0,1)$ there exists a constant $C(\bar{\alpha})$ independent of $\sigma$ such that
$$\|\phi\|_{C_{w}^{2, \bar{\alpha}}} \leqslant C(\bar{\alpha})\left\|L_{\sigma}^{\perp} \phi\right\|_{C_{\tilde{w}}^{0, \bar{\alpha}}}$$
for all $0<|\sigma| \ll 1$ and for all $\phi \in\left\langle\hat{u}_{\sigma}\right\rangle^{\perp} \subset C^{2, \bar{\alpha}}\left(\mathcal{X}_{\sigma}\right)$.
Using the standard weighted Schauder estimates (3.116), the theorem reduces to proving that
$$\|\phi\|_{C_{w}^{0}} \leqslant C\left\|L_{\sigma}^{\perp} \phi\right\|_{C_{\tilde{w}}^{0}} .$$
We prove this estimate by contradiction in the rest of Section 4, starting now.
Assume that there is a sequence of functions $\phi_{i} \in\left\langle\hat{u}_{\sigma_{i}}\right\rangle^{\perp} \subset C^{2, \bar{\alpha}}\left(\mathcal{X}_{\sigma_{i}}\right)$ such that $\sigma_{i} \rightarrow 0$ and
$$1=\left\|\phi_{i}\right\|_{C_{w}^{0}}>i\left\|L_{\sigma_{i}} \phi_{i}\right\|_{C_{\tilde{w}}^{0}} .$$
Let $x_{i} \in \mathcal{X}_{\sigma_{i}}$ such that $\left|\phi_{i}\left(x_{i}\right)\right|=w_{\sigma_{i}}\left(x_{i}\right)$. Set
$$\psi_{i}:=\frac{\phi_{i}}{w_{\sigma_{i}}\left(x_{i}\right)} .$$
Then $\psi_{i}\left(x_{i}\right)=1$ and
$$\left|\psi_{i}\right| \leqslant \frac{w_{\sigma_{i}}}{w_{\sigma_{i}}\left(x_{i}\right)} .$$

Assumption I. It is possible to choose scaling factors $\mu_{i} \geqslant 1$ such that if
$$\tilde{g}_{i}:=\mu_{i}^{2} g_{g l u e, \sigma_{i}},$$
then the spaces $\left(\mathcal{X}_{\sigma_{i}}, \tilde{g}_{i}, x_{i}\right)$ have a pointed Cheeger-Gromov limit (possibly collapsed) and the functions $w_{\sigma_{i}} / w_{\sigma_{i}\left(x_{i}\right)}$ have a locally uniform limit $w_{\infty}$ under this pointed Cheeger-Gromov convergence.

Then the rescaled operators
$$\tilde{L}_{i}:=\Delta_{\tilde{g}_{i}}-\mu_{i}^{-2} \mathrm{Id}=\mu_{i}^{-2}\left(\Delta_{g_{\sigma_{i}}}-\mathrm{Id}\right)=\mu_{i}^{-2} L_{\sigma_{i}}$$
satisfy
$$\left|\tilde{L}_{i} \psi_{i}\right|=\mu_{i}^{-2} \frac{\left|L_{\sigma_{i}} \phi_{i}\right|}{w_{\sigma_{i}}\left(x_{i}\right)}<\mu_{i}^{-2} \frac{1}{i} \frac{\tilde{w}_{\sigma_{i}}}{w_{\sigma_{i}}\left(x_{i}\right)} .$$
This will converge to 0 locally uniformly if we additionally make the following assumption:
Assumption II. The sequence
$$\mu_{i}^{-2} \frac{\tilde{w}_{\sigma_{i}}}{w_{\sigma_{i}}\left(x_{i}\right)}$$
is locally uniformly bounded under the Cheeger-Gromov limit of Assumption I.
In this situation, we can pass $\psi_{i}$ to a subsequential limit $\psi_{\infty}$ weakly in $W_{\text {loc }}^{2, p}$ and strongly in $C_{\text {loc }}^{1, \beta}$ for all $p, \beta$, where $\psi_{\infty}$ is smooth and satisfies an elliptic equation $\tilde{L}_{\infty} \psi_{\infty}=0$. This is clear from standard elliptic compactness and regularity if there is no collapsing in the Cheeger-Gromov limit, and in this case $\tilde{L}_{\infty}=\Delta_{\tilde{g}_{\infty}}-\mu_{\infty}^{-2} \mathrm{Id}$. In the collapsing cases, we first need to pass to a local universal cover and work in quasi-coordinates. Then $\psi_{\infty}$ will be radial and $\tilde{L}_{\infty}$ will reduce to an ODE operator. See the proof of Lemma 4.3 for the details of this argument in the most complicated case (region $\Re_{4}$ ).

Assumption III. There is a Liouville theorem: $\tilde{L}_{\infty} \psi_{\infty}=0$ and $\left|\psi_{\infty}\right| \leqslant w_{\infty}$ imply $\psi_{\infty}=0$.
This contradicts the property $\psi_{\infty}\left(x_{\infty}\right)=1$, which holds due to strong $C_{\text {loc }}^{1, \beta}$ convergence.
In the following sections, we will show that up to passing to subsequences, the above Assumptions I, II and III are indeed satisfied in our situation. The resulting contradictions prove Theorem 4.12.
4.3. GH limit and Liouville on the Kähler-Einstein building block (region $\Re_{1}$ ). Assume that after passing to a subsequence we have for all $i$ that $x_{i} \in \Re_{1}$, or $x_{i} \in \Re_{2}$ with $t\left(x_{i}\right)$ uniformly bounded from below. Then we set $\mu_{i}:=1$. The pointed limit space of the sequence $\left(\mathcal{X}_{\sigma_{i}}, \tilde{g}_{i}, x_{i}\right)$ is the complete cuspidal Kähler-Einstein manifold $\left(\mathcal{X}_{0}^{\text {reg }}, g_{K E, 0}\right)$. We now verify our three assumptions.

I: For simplicity we only consider the case $x, x_{i} \notin \Re_{1}$, so that $t(x), t\left(x_{i}\right)$ are actually defined. They are then uniformly bounded above and below, so
$$\frac{w_{\sigma_{i}}(x)}{w_{\sigma_{i}}\left(x_{i}\right)}=\frac{\left(t(x)-T_{i}\right)^{-\delta}}{\left(t\left(x_{i}\right)-T_{i}\right)^{-\delta}} \rightarrow 1$$
locally uniformly. Hence $w_{\infty}=1$.
II: Again assuming $x, x_{i} \notin \Re_{1}$ we have that
$$\mu_{i}^{-2} \frac{\tilde{w}_{\sigma_{i}}(x)}{w_{\sigma_{i}}\left(x_{i}\right)}=\left|b_{i}\right|^{-\frac{1}{2}}\left(t(x)-T_{i}\right)^{-\frac{3}{2}} \frac{w_{\sigma_{i}}(x)}{w_{\sigma_{i}}\left(x_{i}\right)} \rightarrow 1$$
locally uniformly because of I and because $\left|b_{i}\right| \sim\left|T_{i}\right|^{-3}$.
III: By the generalized maximum principle on complete Riemannian manifolds with Ricci curvature bounded below [39, p.207, Cor 1], there is a sequence $y_{i}$ in $\mathcal{X}_{0}^{\text {reg }}$ such that $\lim _{i \rightarrow \infty} \psi_{\infty}\left(y_{i}\right)=\sup \psi_{\infty}$ and $\limsup _{i \rightarrow \infty} \Delta_{g_{K E, 0}} \psi_{\infty}\left(y_{i}\right) \leqslant 0$. From the equation $\tilde{L}_{\infty} \psi_{\infty}=0$ one has $\psi_{\infty}\left(y_{i}\right)=\Delta_{g_{K E, 0}} \psi_{\infty}\left(y_{i}\right)$, hence $\sup \psi_{\infty} \leqslant 0$. Similarly, we can show $\inf \psi_{\infty} \geqslant 0$. Hence $\psi_{\infty}=0$.

\subsection*{4.4. GH limit and Liouville on the cusp (regions $\Re_{2}, \Re_{3}$ ).}
4.4.1. Region $\Re_{2}$ : The genuine cusp. Here we assume that $x_{i} \in \Re_{2}$ for all $i$. Also, we assume that $x_{i}$ tends to have infinite distance from $\Re_{1}$ as well as from $\Re_{3}$. Precisely,
$$t\left(x_{i}\right) \rightarrow-\infty, \quad t\left(x_{i}\right) / \tau_{i} \rightarrow 0 .$$
We set $\mu_{i}:=1$. The Gromov-Hausdorff limit (better: the collapsed Cheeger-Gromov limit) in this case is a line. I and II work exactly as in the previous case because $\left|t\left(x_{i}\right)\right|=o\left(\left|\tau_{i}\right|\right)=o\left(\left|T_{i}\right|\right)$.

III: Proceeding as in the proof of Lemma 4.3, we obtain a smooth limit function $\psi_{\infty}(t)$ with
$$\tilde{L}_{\infty} \psi_{\infty}=\frac{1}{3}\left(t^{2} \frac{d^{2} \psi_{\infty}}{d t^{2}}-t \frac{d \psi_{\infty}}{d t}\right)-\psi_{\infty}=0 .$$
Thus, $\psi_{\infty}(t)=a(-t)^{3}+b(-t)^{-1}$, where $a, b$ are constants. $w_{\infty}=1$ rules out all possibilities.
4.4.2. Region $\Re_{3}$ : The green gluing region between the cusp and the new neck. In this case, we consider the region within finite distance from $\Re_{3}$ with respect to $g_{\text {glue }, \sigma_{i}}$. More precisely, we assume that
$$t\left(x_{i}\right) \rightarrow-\infty, \quad t\left(x_{i}\right) / \tau_{i} \rightarrow c \in(0, \infty) .$$
Set $\mu_{i}:=1$ and apply Lemma 2.24, extended so that (2.119) holds for $t \in\left[C \tau_{i}, C^{-1} \tau_{i}\right]$ given any fixed constant $C>1$. The remainder of the discussion is similar to that in the case of region $\Re_{2}$.
4.5. GH limit and Liouville on the Tian-Yau building block (region $\Re_{7}$ ). Consider the case that the points $x_{i}$ stay on the Tian-Yau side, i.e., for all $i$ we either have that $x_{i} \in \Re_{7}$, or $x_{i} \in \Re_{6}$ and $t\left(x_{i}\right)-T_{i}=\log h\left(m_{\sigma_{i}}\left(x_{i}\right)\right)$ remains uniformly bounded above. Set $\mu_{i}:=\left|b_{i}\right|^{-1 / 4}$. Then $\tilde{g}_{i}=m_{\sigma_{i}}^{*} g_{T Y_{1}}$ and the pointed limit space is $\left(T Y_{1}, g_{T Y_{1}}\right)$ after applying the map $m_{\sigma_{i}}$.

We now apply the map $m_{\sigma_{i}}$ without writing it explicitly. Thus, $x_{i} \in T Y_{1}$ and $\log h\left(x_{i}\right) \leqslant N$.
For the three conditions, first, by taking a subsequence we can assume that $w_{\sigma_{i}}\left(x_{i}\right) \rightarrow c \in\left[N^{-\delta}, 1\right]$. Then $w_{\sigma_{i}} / w_{\sigma_{i}}\left(x_{i}\right)$ converges locally uniformly to $c^{-1}$ on $\Re_{7}$ and to $c^{-1}(\log h)^{-\delta}$ on $\Re_{6}$. Next,
$$\mu_{i}^{-2} \frac{\tilde{w}_{\sigma_{i}}}{w_{\sigma_{i}}\left(x_{i}\right)}=\left|b_{i}\right|^{\frac{1}{2}} \cdot\left(\left|b_{i}\right|^{\frac{1}{4}}(\log h)^{\frac{3}{4}}\right)^{-2} \cdot \frac{w_{\sigma_{i}}}{w_{\sigma_{i}}\left(x_{i}\right)}$$
is locally uniformly convergent by the previous step. Lastly,
$$\tilde{L}_{\infty} \psi_{\infty}=\Delta_{g_{T Y_{1}}} \psi_{\infty}=0, \quad\left|\psi_{\infty}\right| \leqslant c^{-1}(\log h)^{-\delta} \text { as } h \rightarrow \infty .$$
Then the maximum principle implies that $\psi_{\infty}=0$.
4.6. GH limit and Liouville on the Tian-Yau end (regions $\Re_{6}, \Re_{5}$ ).
4.6.1. Region $\Re_{6}$ : The genuine Tian-Yau end. In this case, we assume that the points $x_{i}$ lie strictly in the interior of region $\Re_{6}$ in the sense that
$$t\left(x_{i}\right)-T_{i} \rightarrow \infty, \quad \rho\left(x_{i}\right)^{-1}\left|T_{i}\right|^{\frac{3}{4} \alpha} \rightarrow \infty,$$
where $\rho$ is a geometric distance function for the unrescaled Tian-Yau metric,
$$\rho(x):=\left(t(x)-T_{i}\right)^{\frac{3}{4}} .$$
Then we define our scaling factors by
$$\mu_{i}:=\rho\left(x_{i}\right)^{-1}\left|b_{i}\right|^{-\frac{1}{4}} \gg\left|T_{i}\right|^{\frac{3}{4}(1-\alpha)} \rightarrow \infty,$$
so that the pointed Gromov-Hausdorff limit is the tangent cone at infinity of the Tian-Yau space, i.e., a half-line $[-1, \infty)$ in the natural parametrization given by $\tilde{\rho}:=\left(\rho-\rho\left(x_{i}\right)\right) / \rho\left(x_{i}\right)$. Technically this is a Cheeger-Gromov limit only away from the endpoint $\tilde{\rho}=-1$ but this subtlety is irrelevant for us.

For properties I and II we compute
$$\begin{aligned}
\frac{w_{\sigma_{i}}}{w_{\sigma_{i}}\left(x_{i}\right)} & =\frac{\left(t-T_{i}\right)^{-\delta}}{\left(t\left(x_{i}\right)-T_{i}\right)^{-\delta}}=(1+\tilde{\rho})^{-\frac{4}{3} \delta}, \\
\mu_{i}^{-2} \frac{\tilde{w}_{\sigma_{i}}}{w_{\sigma_{i}}\left(x_{i}\right)} & =\rho\left(x_{i}\right)^{2}\left|b_{i}\right|^{\frac{1}{2}} \cdot\left(\left|b_{i}\right|^{\frac{1}{4}}\left(t-T_{i}\right)^{\frac{3}{4}}\right)^{-2} \cdot \frac{w_{\sigma_{i}}}{w_{\sigma_{i}\left(x_{i}\right)}}=(1+\tilde{\rho})^{-2-\frac{4}{3} \delta} .
\end{aligned}$$

For III we obtain a smooth limit function $\psi_{\infty}(\tilde{\rho})$ of $\tilde{\rho} \in(-1, \infty)$ solving an ODE $\tilde{L}_{\infty} \psi_{\infty}=0$ as in the proof of Lemma 4.3. Here we show only the computation of $\tilde{L}_{\infty}$. The key step is to find suitable coordinates on the universal cover of the annulus $\left\{\tilde{\rho}_{1}<\tilde{\rho}<\tilde{\rho}_{2}\right\}$, where $\tilde{\rho}_{1}<\tilde{\rho}_{2}$ in $(-1, \infty)$ are given. For this we follow our work in Lemma 2.33, although the $T_{0}$ of that lemma gets replaced by $\rho\left(x_{i}\right)^{4 / 3}$ and instead of $y=t-T_{i} \in\left[T_{0}, 2 T_{0}\right]$ we are now considering the range $y \in\left[a_{1} \rho\left(x_{i}\right)^{4 / 3}, a_{2} \rho\left(x_{i}\right)^{4 / 3}\right]$ with $a_{j}=\left(1+\tilde{\rho}_{j}\right)^{4 / 3}(j=1,2)$. We define $(\check{z}, \check{w})$ and $(z, w)$ as in Lemma 2.33. In addition, we assume that $\varphi(z)=-|z|^{2}$ after scaling and translating $z$ if necessary. Then holomorphic quasi-coordinates for the scaled model metric $\mu_{i}^{2}\left|b_{i}\right|^{1 / 2} \omega_{\mathcal{C}, \sigma_{i}}=\rho\left(x_{i}\right)^{-2} \omega_{\mathcal{C}, \sigma_{i}}$ are given by
$$(\hat{z}, \hat{w}):=\left(\rho\left(x_{i}\right)^{-1} \check{z}, \rho\left(x_{i}\right)^{-1}\left(\check{w}-\rho\left(x_{i}\right)^{-\frac{1}{3}} \frac{T_{i}}{2}\right)\right)=\left(\rho\left(x_{i}\right)^{-\frac{2}{3}} z, \rho\left(x_{i}\right)^{-\frac{4}{3}}\left(w-\frac{T_{i}}{2}\right)\right) .$$
These are also (complex but slightly non-holomorphic) quasi-coordinates for our metric $\tilde{g}_{i}=\mu_{i}^{2} g_{g l u e, \sigma_{i}}$ by Lemma 3.8. Thus, by (2.194), up to errors that decay exponentially as $i \rightarrow \infty$,
$$\tilde{\omega}_{i} \approx \tilde{\omega}_{\infty}=\frac{1}{2}(1+\tilde{\rho})^{-\frac{2}{3}} i(d \hat{w}+\overline{\bar{z}} d \hat{z}) \wedge(d \overline{\hat{w}}+\hat{z} d \overline{\bar{z}})+(1+\tilde{\rho})^{\frac{2}{3}} i d \hat{z} \wedge d \overline{\bar{z}} .$$
Now notice that, from (2.192),
$$\hat{w}+\overline{\hat{w}}+|\hat{z}|^{2}=(1+\tilde{\rho})^{\frac{4}{3}} .$$
To follow the proof of Lemma 4.3 we would need to switch from $(\hat{z}, \hat{w})$ to real coordinates, where one of these coordinates is $\tilde{\rho}$ and the other three parametrize the level sets of $\tilde{\rho}$ or of $\hat{w}+\overline{\hat{w}}+|\hat{z}|^{2}$, which are the orbits of an $\tilde{\omega}_{\infty}$-isometric action of the continuous Heisenberg group $H_{3}(\mathbb{R})$. For simplicity we skip this coordinate change and instead note that thanks to the $H_{3}(\mathbb{R})$-symmetry it is enough to work at $\hat{z}=0$, where $\tilde{\omega}_{\infty}$ is diagonal in the coordinates $(\hat{z}, \hat{w})$. Then, since $\mu_{i} \rightarrow \infty$,
$$\tilde{L}_{\infty} \psi_{\infty}=\Delta_{\tilde{\omega}_{\infty}} \psi_{\infty}=2(1+\tilde{\rho})^{\frac{2}{3}}\left(\psi_{\infty}\right)_{\hat{w} \overline{\tilde{w}}}+(1+\tilde{\rho})^{-\frac{2}{3}}\left(\psi_{\infty}\right)_{\hat{z} \overline{\tilde{z}}}=0 .$$
The trivial solution is $\psi_{\infty}(\tilde{\rho})=$ const , and working at $\hat{z}=0$ one checks that $\psi_{\infty}(\tilde{\rho})=(1+\tilde{\rho})^{2 / 3}$ is the second fundamental solution. Then $\left|\psi_{\infty}\right| \leqslant w_{\infty}=(1+\tilde{\rho})^{-(4 / 3) \delta}$ implies $\psi_{\infty}=0$, as desired.
4.6.2. Region $\Re_{5}$ : The orange gluing region between the Tian-Yau end and the new neck. Now assume either that the sequence $x_{i}$ is contained in region $\Re_{5}$, or that it stays within finite distance of $\Re_{5}$ from the Tian-Yau side in an appropriately rescaled metric. More precisely, we assume that
$$0 \leqslant \rho\left(x_{i}\right)^{-1}\left(\left(2\left|T_{i}\right|^{\alpha}\right)^{\frac{3}{4}}-\rho\left(x_{i}\right)\right) \leqslant C$$
for some $C>0$, where $\rho$ is defined as in (4.70). Also as in the previous case we set
$$\mu_{i}:=\rho\left(x_{i}\right)^{-1}\left|b_{i}\right|^{-\frac{1}{4}} \sim\left|T_{i}\right|^{\frac{3}{4}(1-\alpha)} \rightarrow \infty .$$
Using Proposition 2.34 to estimate the gluing errors, one then checks that the arguments go through as before. The essential point is that the pointed convergence behavior of the rescaled spaces does not change because for every fixed $N>1$, due to the proof of Proposition 2.34, we still have an excellent comparison of $g_{\text {glue }, \sigma_{i}}$ and $\left|b_{i}\right|^{1 / 2} g_{\mathcal{C}, \sigma_{i}}$ in the range $t-T_{i} \in\left[T_{0, i}, N T_{0, i}\right]$ (even though for $N>2$ this set is not contained in the Tian-Yau side of $\mathcal{X}_{\sigma_{i}}$, i.e., in the region $\Re_{5} \cup \Re_{6} \cup \Re_{7}$ ).
4.7. GH limit and Liouville on the new neck (region $\Re_{4}$ ). For $x_{i} \in \mathcal{X}_{\sigma_{i}}$ satisfying
$$x_{i} \in \Re_{4} \Longleftrightarrow T_{i}+2 T_{0, i}<t\left(x_{i}\right)=: t_{i}<\tau_{i},$$
we define the quantity
$$F_{i}:=e^{-\psi_{T_{i}}\left(t_{i}\right)-a}\left|b_{i}\right| .$$
By (2.83) and by the monotonicity of $\psi_{T_{i}}$, this takes values in (0, 1). Thus, up to a subsequence,
$$F_{i} \rightarrow c \in[0,1] .$$
4.7.1. The subcase $c=1$ : Essentially the same as the Tian-Yau end. Then $\psi_{T_{i}}\left(t_{i}\right)-\log \left|b_{i}\right| \rightarrow-a$, or equivalently $\psi_{T_{i}}\left(t_{i}\right)-\psi_{T_{i}}\left(T_{i}\right) \rightarrow 0$. As in (2.181),
$$\int_{0}^{\psi_{T_{i}}\left(t_{i}\right)-\psi_{T_{i}}\left(T_{i}\right)}\left(e^{s}-1\right)^{-\frac{1}{3}} d s=\sqrt[3]{3}\left|b_{i}\right|^{\frac{1}{3}}\left(t_{i}-T_{i}\right),$$
so $t_{i}-T_{i} \rightarrow 0$. Given any $A \in \mathbb{R}$, if $i \gg 1$ and $t=T_{i}+A\left(t_{i}-T_{i}\right)$, then, as in (2.184),
$$\psi_{T_{i}}(t)-\psi_{T_{i}}\left(T_{i}\right)=\mathfrak{c}\left|b_{i}\right|^{\frac{1}{2}}\left(t-T_{i}\right)^{\frac{3}{2}}+O\left(\left|b_{i}\right|\left|t-T_{i}\right|^{3}\right) .$$
We then get a $C^{2}$ estimate as in (2.197). The rest of the proof is similar to the case of region $\Re_{5}$.
4.7.2. The subcase $c=0$ : Essentially the same as the cusp. If $c=0$, then $\psi_{T_{i}}\left(t_{i}\right)-\log \left|b_{i}\right| \rightarrow \infty$. By Proposition 2.25, $\psi_{\text {cusp }}\left(t_{i}\right)-\log \left|b_{i}\right| \rightarrow \infty$. Thus
$$\left(-t_{i}\right)^{3} b_{i} \rightarrow 0,$$
so for any finite constant $\varrho \in \mathbb{R}$, when $i$ is large, $\varrho t_{i} / T_{i}$ is small. By Proposition 2.26,
$$\begin{aligned}
& \psi_{T_{i}}^{\prime}\left(\varrho t_{i}\right)=\psi_{\text {cusp }}^{\prime}\left(\varrho t_{i}\right)\left(1+O\left(\left|b_{i}\right|^{\frac{1}{3}} \tau_{i}\right)+O\left(\left(\varrho t_{i} / T_{i}\right)^{3}\right)\right), \\
& \psi_{T_{i}}^{\prime \prime}\left(\varrho t_{i}\right)=\psi_{\text {cusp }}^{\prime \prime}\left(\varrho t_{i}\right)\left(1+O\left(\left|b_{i}\right|^{\frac{1}{3}} \tau_{i}\right)+O\left(\left(\varrho t_{i} / T_{i}\right)^{3}\right)\right)
\end{aligned}$$
as $i \rightarrow \infty$. So the pointed limit behavior of the (unrescaled) spaces $\left(\mathcal{X}_{\sigma_{i}}, g_{g l u e, \sigma_{i}}, x_{i}\right)$ is exactly the same as in the case of region $\Re_{3}$, and the rest of the discussion is then also the same.
4.7.3. The subcase $0<c<1$ : The genuine new neck, i.e., the obstructed case. If $c \in(0,1)$, then by combining Proposition 2.25, the convergence $F_{i} \rightarrow c$ and the fact that
$$e^{-\psi_{\text {cusp }}\left(t_{i}\right)-a}\left|b_{i}\right|=e^{-a}\left|t_{i}^{3} b_{i}\right|,$$
we immediately obtain that after taking a subsequence,
$$t_{i} / T_{i} \rightarrow \tilde{c} \in(0,1) .$$
We set $\mu_{i}:=1$. With our usual reparametrization $s=1-t / T \in(0,1)$ we get
$$\begin{aligned}
\frac{w_{\sigma_{i}}}{w_{\sigma_{i}}\left(x_{i}\right)} & \rightarrow(1-\tilde{c})^{\delta} s^{-\delta}, \\
\mu_{i}^{-2} \frac{\tilde{w}_{\sigma_{i}}}{w_{\sigma_{i}}\left(x_{i}\right)} & \leqslant C\left(\left|b_{i}\right|^{\frac{1}{4}}\left(t-T_{i}\right)^{\frac{3}{4}}\right)^{-2} \frac{w_{\sigma_{i}}}{w_{\sigma_{i}}\left(x_{i}\right)} \leqslant C^{\prime} s^{-\frac{3}{2}-\delta},
\end{aligned}$$
verifying I and II. Thus, as proved in Lemma 4.3, we get a smooth subsequential limit $\psi_{\infty}(s)$ solving the $\mathrm{ODE} \tilde{L}_{\infty} \psi_{\infty}=L_{\infty} \psi_{\infty}=0$ with $\psi_{\infty}(1-\tilde{c})=1$. Since $\left|\psi_{\infty}\right| \leqslant w_{\infty}=(1-\tilde{c})^{\delta} s^{-\delta}$, Lemma 4.5 tells us that $\psi_{\infty}=\lambda \hat{u}$ for some $\lambda \in \mathbb{R}$. We now use our assumption that $\phi_{i} \in\left\langle\hat{u}_{\sigma_{i}}\right\rangle^{\perp}$, which trivially implies $\psi_{i} \in\left\langle\hat{u}_{\sigma_{i}}\right\rangle^{\perp}$ and hence, by Proposition 4.2, $0=\int_{0}^{1} \psi_{\infty} \hat{u} \mu_{\infty} d s=\lambda \int_{0}^{1}|\hat{u}|^{2} \mu_{\infty} d s$. Since $\mu_{\infty}$ is uniformly positive by Lemma 2.31, we get $\lambda=0$, verifying III and contradicting $\psi_{\infty}(1-\tilde{c})=1$. (This step is the only reason why we need Proposition 4.2, which requires the hard work in Sections 4.1.4-4.1.6.)

\section*{5. Obstruction theory and proof of the Main Theorem}

We have now set up the pre-glued manifold $\left(\mathcal{X}_{\sigma}, \omega_{g l u e, \sigma}\right)$ (Definition 3.4) and the relevant complex Monge-Ampère equation (3.6), estimated the right-hand side $f_{\sigma}$ (Theorem 3.5), and proved a uniform weighted Hölder estimate for the inverse of the linearized operator $L_{\sigma}$ away from a certain obstruction space (Theorem 4.12). It remains to explain the (not quite standard) inverse function theorem with obstructions which will be used to prove our Main Theorem. Throughout this section, it is helpful to refer to Table 2 for the numerical behavior of the functions $\mathbf{r}_{\sigma}, w_{\sigma}, \tilde{w}_{\sigma}$ and $f_{\sigma}$.
5.1. Fixed-point iteration on the orthogonal complement of the obstruction space. This is a fairly standard argument using the weighted Hölder estimates of Theorem 4.12, but it only solves the equation modulo some undetermined scalar multiple of the obstruction function.

We introduce the Monge-Ampère operator
$$M_{\sigma} u:=\log \left(\frac{\left(\omega_{g l u e, \sigma}+i \partial \bar{\partial} u\right)^{2}}{\omega_{g l u e, \sigma}^{2}}\right)-u,$$
and we decompose $M_{\sigma}$ into its linearization at $u=0$ and a remainder as follows:
$$L_{\sigma}=\Delta_{\omega_{\text {glue }, \sigma}}-\mathrm{Id}, \quad Q_{\sigma}:=M_{\sigma}-L_{\sigma} .$$
Recall the obstruction function $\hat{u}_{\sigma}=L_{\sigma} \hat{v}_{\sigma} \in C^{\infty}\left(\mathcal{X}_{\sigma}\right)$ introduced in Definition 4.9, and recall the result of Theorem 4.12: the invertible operator
$$L_{\sigma}^{\perp}:\left\langle\hat{u}_{\sigma}\right\rangle^{\perp} \rightarrow\left\langle\hat{v}_{\sigma}\right\rangle^{\perp},$$
the restriction of $L_{\sigma}$ to the $L^{2}\left(\mathcal{X}_{\sigma}, \omega_{\text {glue }, \sigma}\right)$-complements inside $C^{2, \bar{\alpha}}\left(\mathcal{X}_{\sigma}\right)$ resp. $C^{0, \bar{\alpha}}\left(\mathcal{X}_{\sigma}\right)$, satisfies
$$\|\phi\|_{C_{w}^{2, \bar{\alpha}}} \leqslant C\left\|L_{\sigma}^{\perp} \phi\right\|_{C_{\tilde{w}}^{0, \bar{\alpha}}}$$
for all functions $\phi$ in its domain, with $C$ independent of $\sigma$.
We now introduce the following standard fixed-point iteration:
$$\tilde{u}_{\sigma, 0}:=0, \quad \tilde{u}_{\sigma, i+1}:=\left(L_{\sigma}^{\perp}\right)^{-1}\left[\left(f_{\sigma}-Q_{\sigma}\left(\tilde{u}_{\sigma, i}\right)\right)^{\perp}\right] .$$
Here $f_{\sigma}$ is a fixed Ricci potential of $\omega_{g l u e, \sigma}$ (recall that such a potential is unique only up to constants) and $\left(f_{\sigma}-Q_{\sigma}\left(\tilde{u}_{\sigma, i}\right)\right)^{\perp}$ denotes the $L^{2}\left(\mathcal{X}_{\sigma}, \omega_{\text {glue }, \sigma}\right)$-orthogonal projection of $f_{\sigma}-Q_{\sigma}\left(\tilde{u}_{\sigma, i}\right)$ onto $\left\langle\hat{v}_{\sigma}\right\rangle^{\perp}$.

Lemma 5.1. Let $f_{\sigma}$ be the particular choice of Ricci potential in (3.8). Then for all $\alpha, \bar{\alpha} \in(0,1)$ and for all $0<\delta \ll 1$ there exists a constant $C$ such that for all $0<|\sigma| \ll 1$ we have that
$$\left\|f_{\sigma}^{\perp}\right\|_{C_{\tilde{w}}^{0, \bar{\alpha}}} \leqslant C|b|^{\frac{5}{6}(1-\alpha)-\frac{\delta}{3}} .$$
Proof. This will follow from Theorem 3.5. By definition,
$$f_{\sigma}^{\perp}=f_{\sigma}-\frac{\left\langle f_{\sigma}, \hat{v}_{\sigma}\right\rangle_{L^{2}\left(\mathcal{X}_{\sigma}, \omega_{g l u e, \sigma}\right)}}{\left\langle\hat{v}_{\sigma}, \hat{v}_{\sigma}\right\rangle_{L^{2}\left(\mathcal{X}_{\sigma}, \omega_{g l u e, \sigma}\right)}} \hat{v}_{\sigma} .$$
Thus, we need to estimate four pieces: $f_{\sigma}$, the denominator and numerator of the fraction, and $\hat{v}_{\sigma}$.
(1) We claim that
$$\left\|f_{\sigma}\right\|_{C_{\tilde{w}}^{0, \bar{\alpha}}} \leqslant C|b|^{1-\alpha-\frac{\delta}{3}} .$$
To prove this, note that since $f_{\sigma}$ is exponentially small in terms of $b$ everywhere else, we only need to estimate $f_{\sigma}$ on $\Re_{3}$ and on $\Re_{5} \cup \Re_{6} \cup \Re_{7}$. On $\Re_{3}$ we have by Theorem 3.5 that
$$\left\|f_{\sigma}\right\|_{C_{\tilde{w}}^{0}\left(\Re_{3}\right)}=O\left(|b \| \tau|^{3}\right) \cdot|b|^{\frac{1}{2}}|T|^{\frac{3}{2}} \cdot|T|^{\delta}=O\left(|b|^{1-\frac{\delta}{3}}|\tau|^{3}\right) .$$

For the $C_{\tilde{w}}^{0, \bar{\alpha}}$ seminorm, if $p, q \in \Re_{3}$ and $d_{\omega_{g l u e, \sigma}}(p, q)<\mathbf{r}_{\sigma}(p)$, then
$$\frac{\mathbf{r}_{\sigma}(p)^{\bar{\alpha}}}{\tilde{w}_{\sigma}(p)} \frac{\left|f_{\sigma}(p)-f_{\sigma}(q)\right|}{d_{\omega_{g l u e, \sigma}}(p, q)^{\bar{\alpha}}} \leqslant C \frac{\mathbf{r}_{\sigma}(p)^{\bar{\alpha}}}{\tilde{w}_{\sigma}(p)}\left(\sup _{B_{\omega_{g l u e, \sigma}}\left(p, \mathbf{r}_{\sigma}(p)\right)}\left|\nabla_{\omega_{g l u e, \sigma}} f_{\sigma}\right|_{\omega_{g l u e, \sigma}}\right) \mathbf{r}_{\sigma}(p)^{1-\bar{\alpha}},$$
which has the same upper bound as (5.9) thanks to the gradient estimate in Theorem 3.5. Lastly, on $\Re_{5} \cup \Re_{6} \cup \Re_{7}$, we can similarly estimate
$$\left\|f_{\sigma}\right\|_{C_{\tilde{w}}^{0, \bar{\alpha}}\left(\Re_{5} \cup \Re_{6} \cup \Re_{7}\right)} \leqslant C|b|^{1-\alpha-\frac{\alpha \delta}{3}} .$$
Combining (5.9)-(5.11), we obtain the claim.
(2) It follows from Lemma 2.31 and (4.39) that for some $C>0$ independent of $\sigma$,
$$\left\langle\hat{v}_{\sigma}, \hat{v}_{\sigma}\right\rangle_{L^{2}\left(\mathcal{X}_{\sigma}, \omega_{g l u e, \sigma}\right)} \geqslant C^{-1}|T|^{-2} \geqslant C^{-1}|b|^{\frac{2}{3}} .$$
(3) Since $f_{\sigma}$ is exponentially small in terms of $b$ everywhere else, we need to estimate $\left\langle f_{\sigma}, \hat{v}_{\sigma}\right\rangle_{L^{2}}$ only on $\Re_{3}$ and on $\Re_{5} \cup \Re_{6} \cup \Re_{7}$. On $\Re_{3}$, we have by Theorem 3.5, (4.38) and Lemma 2.31 that
$$\left\langle f_{\sigma}, \hat{v}_{\sigma}\right\rangle_{L^{2}\left(\Re_{3}, \omega_{\text {glue }, \sigma}\right)}=O\left(|b||\tau|^{3}\right) \cdot|T|^{-2} \cdot\left|\frac{\tau}{T}\right|=O\left(|b|^{2}|\tau|^{4}\right) .$$
On $\Re_{5} \cup \Re_{6} \cup \Re_{7}$, we can similarly estimate
$$\left\langle f_{\sigma}, \hat{v}_{\sigma}\right\rangle_{L^{2}\left(\Re_{5} \cup \Re_{6} \cup \Re_{7}, \omega_{g l u e, \sigma}\right)}=O\left(|b|^{\frac{1}{2}} T_{0}^{\frac{3}{2}}\right) \cdot|b| \cdot T_{0}=O\left(|b|^{\frac{3}{2}-\frac{5}{6} \alpha}\right) .$$
(4) We first estimate the weighted $C^{0}$ norm of $\hat{v}_{\sigma}$ :
$$\left\|\hat{v}_{\sigma}\right\|_{C_{\tilde{w}}^{0}\left(\mathcal{X}_{\sigma}\right)} \leqslant C\left\|\tilde{w}_{\sigma}^{-1}\right\|_{L^{\infty}\left(\mathcal{X}_{\sigma}\right)} \leqslant C|T|^{\delta} \leqslant C|b|^{-\frac{\delta}{3}} .$$
Now we estimate the weighted $C^{0, \bar{\alpha}}$ seminorm of $\hat{v}_{\sigma}$. We claim that, in fact,
$$\left[\hat{v}_{\sigma}\right]_{C_{\tilde{w}}^{0, \bar{\alpha}}}=\sup \left\{\frac{\mathbf{r}_{\sigma}(p)^{\bar{\alpha}}}{\tilde{w}_{\sigma}(p)} \frac{\hat{v}_{\sigma}(p)-\hat{v}_{\sigma}(q) \mid}{d_{\omega_{g l u e, \sigma}}(p, q)^{\bar{\alpha}}}: 0<d_{\omega_{g l u e, \sigma}}(p, q)<\mathbf{r}_{\sigma}(p)\right\} \leqslant C|b|^{-\frac{\delta}{3}}$$
as well. This is an obvious consequence of the stronger claim
$$\mathbf{r}_{\sigma}\left|\nabla_{\omega_{\text {glue }, \sigma}} \hat{v}_{\sigma}\right|_{\omega_{\text {glue }, \sigma}} \leqslant C .$$
To prove (5.17), hence the lemma, we fix a universal $0<\varepsilon \ll 1$ and distinguish three cases.
(4a) $s=1-\eta \in[\varepsilon, 1-\varepsilon]$. (5.17) is clear thanks to the quasi-coordinates from Convention 4.1.
(4b) $\eta \in(0, \varepsilon]$. In this case, $\hat{v}_{\sigma}=\hat{v} \chi_{\sigma}(1-\cdot)$, where $\chi_{\sigma}$ is as in (4.41). Then
$$\left|\nabla_{\omega_{\text {glue }, \sigma}} \hat{v}_{\sigma}\right|_{\omega_{\text {glue }, \sigma}} \leqslant C \eta\left|\hat{v}_{\sigma}^{\prime}(1-\eta)\right| \leqslant C \eta^{3},$$
using Proposition 2.26 to compare the $\omega_{\text {glue }, \sigma}$-gradient to the $\omega_{\text {cusp }}$-gradient and using Lemma 4.8 and (4.41) to estimate $\hat{v}$ and $\chi_{\sigma}$, respectively.
(4c) $s \in(0, \varepsilon]$. In this case, $\hat{v}_{\sigma}=\chi_{\sigma}(\hat{v}-\hat{v}(0))+\hat{v}(0)$. From the proof of Proposition 2.30,
$$\mathbf{r}_{\sigma}\left|\nabla_{\omega_{\text {glue }, \sigma}} \hat{v}_{\sigma}\right|_{\omega_{\text {glue }, \sigma}} \leqslant C \mathbf{r}_{\sigma} s^{\frac{1}{4}}\left|\hat{v}_{\sigma}^{\prime}(s)\right| \leqslant C s\left|\hat{v}_{\sigma}^{\prime}(s)\right| .$$
Lemma 4.8 and (4.41) again tell us that this is bounded by $C s^{3 / 2}$. However, even the weaker version of Lemma 4.8 that allows for an $s^{1 / 2}$ term in the expansion of $\hat{v}$ would be sufficient to bound (5.19) by $C s^{1 / 2}=O(1)$ as $s \rightarrow 0$, which is still enough for the current lemma. \(\square\)

We can now state the main result of this subsection.

Proposition 5.2. Let $f_{\sigma}$ be the particular choice of Ricci potential in (3.8). Then for all $\alpha \in\left(0, \frac{1}{5}\right)$, $\bar{\alpha} \in(0,1)$ and $0<\delta \ll 1$, there exist constants $C, C^{\prime}$ such that for all $0<|\sigma| \ll 1$ the sequence $\tilde{u}_{\sigma, i}$ defined in (5.5) converges in the $C_{w}^{2, \bar{\alpha}}\left(\mathcal{X}_{\sigma}, \omega_{\text {glue }, \sigma}\right)$ norm, its limit $\tilde{u}_{\sigma} \in\left\langle\hat{u}_{\sigma}\right\rangle^{\perp}$ satisfies
$$\left\|\tilde{u}_{\sigma}\right\|_{C_{w}^{2, \bar{\alpha}}} \leqslant C\left\|f_{\sigma}^{\perp}\right\|_{C_{\tilde{w}}^{0, \bar{\alpha}}} \leqslant C^{\prime}|b|^{\frac{5}{6}(1-\alpha)-\frac{\delta}{3}},$$
and $\tilde{u}_{\sigma}$ is a solution to the equation
$$M_{\sigma} \tilde{u}_{\sigma}=f_{\sigma}+\lambda_{\sigma} \hat{v}_{\sigma}$$
for some unknown $\lambda_{\sigma} \in \mathbb{R}$.
Proof. We first explain the structure of the argument, which is of course standard. In order to prove that the sequence $\tilde{u}_{\sigma, i}$ converges in the $C_{w}^{2, \bar{\alpha}}\left(\mathcal{X}_{\sigma}, \omega_{g l u e, \sigma}\right)$ norm and to bound the norm of its limit $\tilde{u}_{\sigma}$, we prove that it is Cauchy by comparing it to a geometric sequence, as follows:
$$\begin{aligned}
\left\|\tilde{u}_{\sigma, i+1}-\tilde{u}_{\sigma, i}\right\|_{C_{w}^{2, \bar{\alpha}}} & \leqslant C\left\|\left(Q_{\sigma}\left(\tilde{u}_{\sigma, i}\right)-Q_{\sigma}\left(\tilde{u}_{\sigma, i-1}\right)\right)^{\perp}\right\|_{C_{\tilde{w}}^{0, \bar{\alpha}}} \\
& \leqslant C|b|^{-\frac{1}{6}-\frac{\delta}{3}}\left\|Q_{\sigma}\left(\tilde{u}_{\sigma, i}\right)-Q_{\sigma}\left(\tilde{u}_{\sigma, i-1}\right)\right\|_{C_{\tilde{w}}^{0, \bar{\alpha}}} \\
& \leqslant C|b|^{-\frac{2}{3}-\frac{\delta}{3}}\left(\left\|\tilde{u}_{\sigma, i}\right\|_{C_{w}^{2, \bar{\alpha}}}+\left\|\tilde{u}_{\sigma, i-1}\right\|_{C_{w}^{2, \bar{\alpha}}}\right)\left\|\tilde{u}_{\sigma, i}-\tilde{u}_{\sigma, i-1}\right\|_{C_{w}^{2, \bar{\alpha}}} .
\end{aligned}$$
Here, (5.22) follows directly from Theorem 4.12, (5.23) is a little technical and is deferred to Claim 5.3 below, and (5.24) then follows from elementary inequalities and from the fact that
$$\frac{1}{\tilde{w}_{\sigma}}\left(\frac{w_{\sigma}}{\mathbf{r}_{\sigma}^{2}}\right)^{2}=\tilde{w}_{\sigma} \leqslant|b|^{-\frac{1}{2}} .$$
Given (5.24), we can finish the proof as follows: We have $\tilde{u}_{\sigma, 0}=0$ and $\tilde{u}_{\sigma, 1}=\left(L_{\sigma}^{\perp}\right)^{-1}\left(f_{\sigma}^{\perp}\right)$, so
$$\left\|\tilde{u}_{\sigma, 1}\right\|_{C_{w}^{2, \bar{\alpha}}}=\left\|\left(L_{\sigma}^{\perp}\right)^{-1}\left(f_{\sigma}^{\perp}\right)\right\|_{C_{w}^{2, \bar{\alpha}}} \leqslant C\left\|f_{\sigma}^{\perp}\right\|_{C_{\tilde{w}}^{0, \bar{\alpha}}} \leqslant C|b|^{\frac{5}{6}-\frac{5}{6} \alpha-\frac{\delta}{3}}$$
by Lemma 5.1. Thus, we can aim to prove inductively that
$$\left\|\tilde{u}_{\sigma, i}\right\|_{C_{w}^{2, \bar{\alpha}}} \leqslant C|b|^{\frac{5}{6}-\frac{5}{6} \alpha-\frac{\delta}{3}} .$$
This can be combined with (5.24), resulting in the estimate
$$\left\|\tilde{u}_{\sigma, i+1}-\tilde{u}_{\sigma, i}\right\|_{C_{w}^{2, \bar{\alpha}}} \leqslant C|b|^{\frac{1}{6}-\frac{5}{6} \alpha-\frac{2}{3} \delta}\left\|\tilde{u}_{\sigma, i}-\tilde{u}_{\sigma, i-1}\right\|_{C_{w}^{2, \bar{\alpha}}} .$$
Thus, if $\alpha<\frac{1}{5}$, then our sequence is Cauchy and we can also complete the inductive step for (5.27). Then, passing to the limit $i \rightarrow \infty$ in (5.5), it is clear that $\tilde{u}_{\sigma} \in\left\langle\hat{u}_{\sigma}\right\rangle^{\perp}$ and
$$\left(M_{\sigma} \tilde{u}_{\sigma}\right)^{\perp}=L_{\sigma}^{\perp} \tilde{u}_{\sigma}+\left(Q_{\sigma} \tilde{u}_{\sigma}\right)^{\perp}=f_{\sigma}^{\perp},$$
which is equivalent to the claimed property (5.21).
It remains to prove the following claim, which directly implies (5.23).
Claim 5.3. For all $\Phi \in C^{0, \bar{\alpha}}\left(\mathcal{X}_{\sigma}, \omega_{\text {glue }, \sigma}\right)$ we have that
$$\left\|\Phi^{\perp}\right\|_{C_{\tilde{w}}^{0, \bar{\alpha}}} \leqslant C|b|^{-\frac{1}{6}-\frac{\delta}{3}}\|\Phi\|_{C_{\tilde{w}}^{0, \bar{\alpha}}} .$$
Proof of Claim 5.3. Most of the necessary steps were already done in the proof of Lemma 5.1 in the special case $\Phi=f_{\sigma}$. In fact, the only part that needs to be redone is the estimate of $\left\langle\Phi, \hat{v}_{\sigma}\right\rangle_{L^{2}}$ :
$$\left|\left\langle\Phi, \hat{v}_{\sigma}\right\rangle_{L^{2}\left(\mathcal{X}_{\sigma}, \omega_{\text {glue }, \sigma}\right)}\right| \leqslant C\|\Phi\|_{C_{\tilde{w}}^{0}}\left\|\hat{v}_{\sigma} \tilde{w}_{\sigma}\right\|_{L^{1}\left(\mathcal{X}_{\sigma}, \omega_{\text {glue }, \sigma}\right)} \leqslant C\|\Phi\|_{C_{\tilde{w}}^{0}}|b|^{\frac{1}{2}},$$
where the estimate of $\left\|\hat{v}_{\sigma} \tilde{w}_{\sigma}\right\|_{L^{1}}$ is proved as follows. Recall that
$$\tilde{w}_{\sigma}=\mathbf{r}_{\sigma}^{-2} w_{\sigma}= \begin{cases}|T|^{-\delta} & \text { on } \Re_{1}, \\ |b|^{-\frac{1}{2}} \Psi_{\sigma}^{*}\left(\Phi_{\sigma}^{-1}\right)^{*}\left((t-T)^{-\frac{3}{2}-\delta}\right) & \text { on } \Re_{2} \cup \cdots \cup \Re_{6}, \\ |b|^{-\frac{1}{2}} & \text { on } \Re_{7} .\end{cases}$$
Thus, using Lemma 2.31 to bound the volume form on the neck and Lemma 4.8 to bound $\hat{v}_{\sigma}$,
$$\begin{aligned}
\int_{\mathcal{X}_{\sigma}}\left|\hat{v}_{\sigma}\right| \tilde{w}_{\sigma} \omega_{g l u e, \sigma}^{2} & \leqslant C\left(|b| \cdot|b|^{-\frac{1}{2}}+|b| \cdot \int_{1}^{2|T|^{\alpha}}|b|^{-\frac{1}{2}} y^{-\frac{3}{2}-\delta} d y\right. \\
& \left.+|T|^{-2} \int_{2|T|^{\alpha-1}}^{1-\frac{\tau}{T}}|b|^{-\frac{1}{2}}(|T| s)^{-\frac{3}{2}-\delta} d s\right) \leqslant C|b|^{\frac{1}{2}}
\end{aligned}$$
Note that the decay $|\hat{v}(1-\eta)|=O\left(\eta^{3}\right)$ as $\eta \rightarrow 0$ compensates the blowup $\mu_{T}(1-\eta)=O\left(\eta^{-3}\right)$ of the radial volume density from Lemma 2.31. This observation will also be used several times below.

Then (5.31) is proved, and Claim 5.3 follows from this together with (5.12) and (5.15)-(5.16). \(\square\)
5.2. Killing the obstruction by varying the Ricci potential. Here we carry out the last step of the argument. Recall that for a fixed Ricci potential $f_{\sigma}$ we have solved the Monge-Ampère equation modulo obstructions in Proposition 5.2. Our final goal is to kill the obstruction by using the freedom of adding a constant to the Ricci potential. At first this seems contradictory because if we add a constant to $f_{\sigma}$, then the solution $u_{\sigma}$ to the Monge-Ampère equation changes by the same constant. However, $\tilde{u}_{\sigma}$, the solution "modulo obstructions," does not change in such an obvious way.

To be slightly more precise, we change $f_{\sigma}$ by a constant $s$ with $|s|$ not much bigger than the $C_{\tilde{w}}^{0, \bar{\alpha}}$ bound of $f_{\sigma}^{\perp}$ in (5.20). By running the same iteration as in the proof of Proposition 5.2, we obtain $\tilde{u}_{\sigma, s} \in\left\langle\hat{u}_{\sigma}\right\rangle^{\perp}$ solving the Monge-Ampère equation with right-hand side $f_{\sigma}+s$ modulo obstructions. Moreover, $\tilde{u}_{\sigma, s}$ satisfies a $C_{w}^{2, \bar{\alpha}}$ bound like (5.20) independently of $s$. The obstruction coefficient $\lambda_{\sigma, s}$ depends continuously on $s$. It turns out that we can calculate $\lambda_{\sigma, s}$ up to errors that are negligible at the boundary of the allowed range for $s$, and this "leading term" of $\lambda_{\sigma, s}$ is proportional to $s$. So by the intermediate value theorem, $\tilde{u}_{\sigma, s}$ is the true solution $u_{\sigma}$ for some $s$ in the allowed range.

The precise statement is as follows. After the proof we will deduce our Main Theorem from this.
Theorem 5.4. Let $f_{\sigma}$ be the choice of Ricci potential in (3.8). For all $\alpha \in\left(0, \frac{1}{5}\right), \mathbf{a} \in\left(\alpha, \frac{1}{5}\right), \bar{\alpha} \in(0,1)$ and $0<\delta \ll 1$, there exists a constant $C$ such that for all $0<|\sigma| \ll 1$ the following holds. Set
$$A:=|b|^{\frac{5}{6}(1-\mathbf{a})} .$$
Then for all $s \in[-A, A]$ there exists a $\tilde{u}_{\sigma, s} \in\left\langle\hat{u}_{\sigma}\right\rangle^{\perp} \subset C_{w}^{2, \bar{\alpha}}\left(\mathcal{X}_{\sigma}\right)$ solving the equation
$$M_{\sigma} \tilde{u}_{\sigma, s}=f_{\sigma}+s+\lambda_{\sigma, s} \hat{v}_{\sigma}$$
for some $\lambda_{\sigma, s} \in \mathbb{R}$ and satisfying the estimate
$$\left\|\tilde{u}_{\sigma, s}\right\|_{C_{w}^{2, \bar{\alpha}}} \leqslant C|b|^{\frac{5}{6}}(1-\mathbf{a})-\frac{\delta}{3} .$$
Moreover, there exists an $s_{\sigma} \in[-A, A]$ such that $\lambda_{\sigma, s_{\sigma}}=0$.
Proof. For all $s \in[-A, A]$ the proof of Proposition 5.2 yields a $\tilde{u}_{\sigma, s} \in\left\langle u_{\sigma}\right\rangle^{\perp}$ such that
$$M_{\sigma} \tilde{u}_{\sigma, s}=f_{\sigma}+s+\lambda_{\sigma, s} \hat{v}_{\sigma}$$
and such that (5.36) holds. To see this carefully, we only need to redo the estimate of Lemma 5.1:
$$\begin{aligned}
\left\|\left(f_{\sigma}+s\right)^{\perp}\right\|_{C_{\tilde{w}}^{0, \bar{\alpha}}} & \leqslant\left\|f_{\sigma}^{\perp}\right\|_{C_{\tilde{w}}^{0, \bar{\alpha}}}+|s|\left\|1-\frac{\left\langle 1, \hat{v}_{\sigma}\right\rangle_{L^{2}}}{\left\langle\hat{v}_{\sigma}, \hat{v}_{\sigma}\right\rangle_{L^{2}}} \hat{v}_{\sigma}\right\|_{C_{\tilde{w}}^{0, \bar{\alpha}}} \\
& \leqslant C|b|^{\frac{5}{6}(1-\alpha)-\frac{\delta}{3}}+|b|^{\frac{5}{6}(1-\mathbf{a})}\left(\left\|\tilde{w}_{\sigma}^{-1}\right\|_{L^{\infty}}+\frac{\left|\left\langle 1, \hat{v}_{\sigma}\right\rangle_{L^{2}}\right|}{\left\langle\hat{v}_{\sigma}, \hat{v}_{\sigma}\right\rangle_{L^{2}}}\left\|\hat{v}_{\sigma}\right\|_{C_{\tilde{w}}^{0, \bar{\alpha}}}\right) \\
& \leqslant C|b|^{\frac{5}{6}(1-\mathbf{a})-\frac{\delta}{3}}
\end{aligned}$$
thanks to (5.6), (5.15)-(5.16), (5.12), and the following upper bound of $\left|\left\langle 1, \hat{v}_{\sigma}\right\rangle_{L^{2}}\right|$ : for $\alpha \leqslant \frac{1}{3}$,
$$\left|\left\langle 1, \hat{v}_{\sigma}\right\rangle_{L^{2}}\right| \leqslant C\left(|b| \cdot|T|^{\alpha}+|T|^{-2} \int_{2|T|^{\alpha-1}}^{1-\frac{\tau}{T}} d s\right) \leqslant C|b|^{\frac{2}{3}} \leqslant C\left\langle\hat{v}_{\sigma}, \hat{v}_{\sigma}\right\rangle_{L^{2}}$$
Here we have used Lemmas 2.31 and 4.8 to bound the volume form on the middle neck and $\hat{v}_{\sigma}$. This proves (5.38), hence, as in the proof of Proposition 5.2, the existence of $\tilde{u}_{\sigma, s}$ and the estimate (5.36). Note that for $s= \pm A$ the operator ${ }^{\perp}$ did not change our estimate of the $C_{\tilde{w}}^{0, \bar{\alpha}}$ norm of $f_{\sigma}+s$ except for an arbitrarily small power of $|b|$. This is a key improvement over the case $s=0$, where we almost lost a factor of $|b|^{-1 / 6}$ (compare (5.6) to (5.8)), which is close to the worst possible loss (5.30).

By taking the $L^{2}\left(\mathcal{X}_{\sigma}, \omega_{\text {glue }, \sigma}\right)$-inner product with $\hat{v}_{\sigma}$,
$$\lambda_{\sigma, s}=\frac{\left\langle L_{\sigma} \tilde{u}_{\sigma, s}+Q_{\sigma} \tilde{u}_{\sigma, s}-f_{\sigma}-s, \hat{v}_{\sigma}\right\rangle_{L^{2}}}{\left\|\hat{v}_{\sigma}\right\|_{L^{2}}^{2}}=\frac{\left\langle Q_{\sigma} \tilde{u}_{\sigma, s}-f_{\sigma}-s, \hat{v}_{\sigma}\right\rangle_{L^{2}}}{\left\|\hat{v}_{\sigma}\right\|_{L^{2}}^{2}},$$
where we have used $\left\langle L_{\sigma} \tilde{u}_{\sigma, s}, \hat{v}_{\sigma}\right\rangle_{L^{2}}=\left\langle\tilde{u}_{\sigma, s}, L_{\sigma} \hat{v}_{\sigma}\right\rangle_{L^{2}}=\left\langle\tilde{u}_{\sigma, s}, \hat{u}_{\sigma}\right\rangle_{L^{2}}=0$. Our goal is to show that as $s$ goes from $-A$ to $A$, the numerator of $\lambda_{\sigma, s}$ will have a sign change. One can prove directly from (5.5) that, for a fixed $\sigma$, the solution $\tilde{u}_{\sigma, s}$ depends continuously on $s$ in the $C^{2, \bar{\alpha}}$ topology on $\mathcal{X}_{\sigma}$. Thus, if there is indeed a sign change, then $\lambda_{\sigma, s}$ must vanish for some $s \in[-A, A]$, as desired.