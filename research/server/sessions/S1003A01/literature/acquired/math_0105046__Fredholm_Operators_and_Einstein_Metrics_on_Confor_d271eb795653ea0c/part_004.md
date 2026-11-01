---
retention_scope: session
part: 4
total_parts: 4
---

[Part 4/4 of: [math/0105046] Fredholm Operators and Einstein Metrics on Conformally Compact Manifolds]

Proof. Let $u=\log \varphi$. Using Lemma
$$\begin{aligned}
\int_{M} & \left|e^{u} D\left(e^{-u} \omega\right)\right|_{g}^{2}+\left|e^{-u} D^{*}\left(e^{u} \omega\right)\right|_{g}^{2} d V_{g} \\
= & \int_{M}|D \omega-d u \wedge \omega|_{g}^{2}+\left|D^{*} \omega-d u \vee \omega\right|_{g}^{2} d V_{g} \\
= & \int_{M}|D \omega|_{g}^{2}-2\langle D \omega, d u \wedge \omega\rangle_{g}+|d u \wedge \omega|_{g}^{2} \\
& \quad+\left|D^{*} \omega\right|_{g}^{2}-2\left\langle D^{*} \omega, d u \vee \omega\right\rangle_{g}+|d u \vee \omega|_{g}^{2} d V_{g} \\
= & \int_{M}\langle\omega, \Delta \omega\rangle_{g}-2\langle d u \vee D \omega, \omega\rangle_{g}+\langle d u \vee(d u \wedge \omega), \omega\rangle_{g} \\
& \quad-2\langle\omega, D(d u \vee \omega)\rangle_{g}+\langle d u \wedge(d u \vee \omega), \omega\rangle_{g} d V_{g} \\
= & \int_{M}\langle\omega, \Delta \omega\rangle_{g}+|d u|_{g}^{2}|\omega|_{g}^{2}-2\langle\omega, H(u) \omega\rangle_{g}-2\left\langle\omega, \nabla_{\operatorname{grad} u} \omega\right\rangle_{g} d V_{g} \\
= & \int_{M}\langle\omega, \Delta \omega\rangle_{g}+|d u|_{g}^{2}|\omega|_{g}^{2}-2\langle\omega, H(u) \omega\rangle_{g}-(\Delta u)|\omega|_{g}^{2} d V_{g} \\
= & \int_{M}\langle\omega, \Delta \omega\rangle_{g}-e^{-u} \Delta\left(e^{u}\right)|\omega|_{g}^{2}-2\langle\omega, H(u) \omega\rangle_{g} d V_{g}
\end{aligned}$$ \(\square\)

To make use of this formula, we will use a power of the defining function $\rho$ as our weight function $\varphi$. It is convenient to introduce the following notation: If $P: C^{\infty}(M ; E) \rightarrow C^{\infty}(M ; E)$ is a differential operator on $M$ and $\lambda$ is a real number, we write
$$(u, P u) \gtrsim \lambda\|u\|^{2}$$
to mean that for every $\varepsilon>0$, there exists a compact set $K_{\varepsilon}$ such that
$$(u, P u) \geq(\lambda-\varepsilon)\|u\|^{2}$$
whenever $u$ is smooth and compactly supported in $M \backslash K_{\varepsilon}$.
Lemma 7.10. Let $M$ be an asymptotically hyperbolic $(n+1)$-manifold of class $C^{l, \beta}$, with $l \geq 2$ and $0 \leq \beta<1$, and suppose either $0 \leq q<n / 2$ or $(n+2) / 2<$
$q \leq n$. The covariant Laplace-Beltrami operator satisfies the following asymptotic estimate on $E$-valued $q$-forms:
$$(\omega, \Delta \omega) \gtrsim \lambda\|\omega\|^{2},$$
where $\lambda=(n-2 q)^{2} / 4$ if $0 \leq q<n / 2$ and $\lambda=(n+2-2 q)^{2} / 4$ if $(n+2) / 2<q \leq n$.
Proof. We will use (7.7) for forms $\omega$ supported near the boundary. Let $\rho$ be a smooth defining function. Using (7.1), we compute
$$(\log \rho)_{; i j}=\rho^{-2} \rho_{; i} \rho_{; j}-g_{i j}+O(\rho) .$$
The tensor $g$ acts as the identity on 1-forms, and since we extend it to act as a derivation, it acts on $E$-valued $q$-forms as $q$ times the identity. Using $(7.6)$, therefore, the action of $H(\log \rho)$ on an $E$-valued $q$-form $\omega$ can be written
$$\begin{aligned}
\langle\omega, H(\log \rho) \omega\rangle_{g} & =\left\langle\omega,(\log \rho)_{; i j} e^{i} \wedge\left(e^{j} \vee \omega\right)\right\rangle_{g} \\
& =\left\langle\omega, \frac{d \rho}{\rho} \wedge\left(\frac{d \rho}{\rho} \vee \omega\right)\right\rangle_{g}-q|\omega|_{g}^{2}+O\left(\rho|\omega|_{g}^{2}\right) \\
& =\left|\frac{d \rho}{\rho} \vee \omega\right|_{g}^{2}-q|\omega|_{g}^{2}+O\left(\rho|\omega|_{g}^{2}\right)
\end{aligned}$$
Thus with $\varphi=\rho^{s}$, where $s$ is a constant to be determined later, the integrand on the right-hand side of (7.71) can be estimated as follows:
$$\begin{aligned}
& \left\langle\omega,\left(\rho^{-s} \Delta\left(\rho^{s}\right)+2 s H(\log \rho)\right) \omega\right\rangle \\
& \quad \geq s(n-s-2 q)|\omega|_{g}^{2}+2 s\left|\frac{d \rho}{\rho} \vee \omega\right|_{g}^{2}-O\left(\rho|\omega|_{g}^{2}\right)
\end{aligned}$$

Given $\delta>0$, we can choose $\varepsilon$ small enough that the absolute value of the $O\left(\rho|\omega|_{g}^{2}\right)$ factor above is bounded by $\delta|\omega|_{g}^{2}$ on $A_{\varepsilon}$. If $s \geq 0$, we then have for $\omega$ compactly supported in $A_{\varepsilon}$
$$(\omega, \Delta \omega) \geq(s(n-s-2 q)-\delta)\|\omega\|_{g}^{2} .$$
This estimate is optimal when $s=(n-2 q) / 2$, so as long as $(n-2 q) / 2>0$, which is to say $q<n / 2$, we obtain the conclusion of the lemma with $\lambda=(n-2 q)^{2} / 4$.

If on the other hand $s \leq 0$, we use the fact that $|d \rho / \rho|_{g}$ approaches 1 uniformly at $\partial M$. We choose $\varepsilon$ small enough that the $O\left(\rho|\omega|_{g}^{2}\right)$ factor in (7.9) is bounded by $(\delta / 2)|\omega|_{g}^{2}$ and $2 s|d \rho / \rho|_{g}^{2} \geq 2 s-\delta / 2$ on $A_{\varepsilon}$, and conclude that
$$\begin{aligned}
(\omega, \Delta \omega) & \geq(s(n-s-2 q)-\delta / 2)\|\omega\|^{2}+(2 s-\delta / 2)\|\omega\|^{2} \\
& =(s(n-s-2 q+2)-\delta)\|\omega\|^{2}
\end{aligned}$$
This in turn is optimal when $s=(n+2-2 q) / 2$. Thus as long as $q>(n+2) / 2$, so that $s<0$, we obtain the conclusion of the lemma with $\lambda=(n+2-2 q)^{2} / 4$. \(\square\)

When applied to scalar-valued forms, this result can be used to obtain an elementary proof of the sharp $L^{2}$ Fredholm theorems and spectral bounds for the Laplace-Beltrami operator originally obtained by Mazzeo [39, 40]. (See [7], where this is carried out in detail.) Our main interest in this monograph, however, is in the covariant Laplacian acting on symmetric tensors. In this case, we consider the bundle $\Sigma^{r} M$ of symmetric $r$-tensors as a subbundle of the bundle $\Lambda^{1} T^{r-1} M$ of ( $r-1$ )-tensor-valued 1 -forms.

The following lemma gives a Weitzenböck formula relating the covariant Laplacian on such tensors to $\Delta$. For this purpose, we define zero-order operators $\widetilde{R c}(u)$ and $\widetilde{R m}(u)$ acting on $r$-tensors by
$$\begin{aligned}
\widetilde{R c}(u)_{i_{1} \ldots i_{r-1} j} & =R_{j}{ }^{k} u_{i_{1} \ldots i_{r-1} k} \\
\widetilde{R m}(u)_{i_{1} \ldots i_{r-1} j} & =\sum_{p=1}^{r-1} R_{i_{p}}{ }^{l}{ }_{j}{ }^{k} u_{i_{1} \ldots i_{\ldots} i_{r-1} k} .
\end{aligned}$$
Note that on symmetric 2-tensors, $\widetilde{R m}$ agrees with the operator $\stackrel{\circ}{R m}$ defined by $(1,1)$, but $\widetilde{R c}$ is not the same as $\stackrel{\circ}{R} c$ in general.

Lemma 7.11. For a section $u$ of $\Lambda^{1} T^{r-1} M$,
$$\Delta u=\nabla^{*} \nabla u+\widetilde{R c}(u)-\widetilde{R m}(u) .$$

Proof. This is easiest to see in components, noting that the last index of $u$ is considered to be the 1-form index.
$$\begin{aligned}
& \left(D^{*} D u\right)_{i_{1} \ldots i_{r-1} j}=-u_{i_{1} \ldots i_{r-1} j ; k}^{k}+u_{i_{1} \ldots i_{r-1} k ; j}^{k} \\
& \left(D D^{*} u\right)_{i_{1} \ldots i_{r-1} j}=-u_{i_{1} \ldots i_{r-1} k ;}^{k}{ }_{j} .
\end{aligned}$$
Applying the Ricci identity to the commutator
$$u_{i_{1} \ldots i_{r-1} k ; j}^{k}-u_{i_{1} \ldots i_{r-1} k ;{ }^{k} j}$$
yields the result. \(\square\)

Specializing Lemma to $\Sigma_{0}^{r} M$, we obtain the following sharp asymptotic estimate.

Lemma 7.12. The following asymptotic estimate holds for any smooth, compactly supported, trace-free symmetric $r$-tensor $u$ :
$$\left(u, \nabla^{*} \nabla u\right) \gtrsim\left(\frac{n^{2}}{4}+r\right)\|u\|^{2} .$$

Proof. Using $(4.3)$, we compute that the curvature operators $\widetilde{R c}$ and $\widetilde{R m}$ have the following asymptotic behavior on trace-free symmetric $r$-tensors near $\partial M$ :
$$\begin{aligned}
\widetilde{R c}(u) & =-n u+O\left(\rho|u|_{g}\right) ; \\
\widetilde{R m}(u) & =(r-1) u+O\left(\rho|u|_{g}\right) .
\end{aligned}$$
To prove the lemma, just use Lemma with $q=1$ together with Lemma to obtain
$$\begin{aligned}
\left(u, \nabla^{*} \nabla u\right) & =(u, \Delta u)-(u, \widetilde{R c}(u))+(u, \widetilde{R m}(u)) \\
& \gtrsim \frac{(n-2)^{2}}{4}\|u\|^{2}+n\|u\|^{2}+(r-1)\|u\|^{2} \\
& =\left(\frac{n^{2}}{4}+r\right)\|u\|^{2} .
\end{aligned}$$ \(\square\)

Remark. The same method yields similar estimates for Laplace operators acting on any other tensor bundle, but in cases other than fully symmetric or fully antisymmetric tensors, the estimates so obtained appear not to be sharp. It would be interesting to know if a modified version of (7.7) could be used to sharpen the estimate in those cases.

Lemma 7.13. The following asymptotic estimate holds for any smooth, compactly supported, trace-free symmetric 2-tensor $u$ :
$$\left(u, \Delta_{L} u\right) \gtrsim\left(\frac{n^{2}}{4}-2 n\right)\|u\|^{2} .$$

Proof. This follows immediately from the preceding lemma together with the asymptotic formulas (7.4) for $\stackrel{\circ}{R m}$ and $\stackrel{\circ}{R c}$. \(\square\)

Proof of Propositions $c$ are Fredholm on $L^{2}$ for the claimed values of $c$ by virtue of Lemmas 7.73 and 7.12 On the other hand, the indicial radius computations at the beginning of this chapter show that these are precisely the values of $c$ for which these operators have positive indicial radius, so these are the only values of $c$ for which the operators are Fredholm. The result for the Hodge Laplacian follows similarly from Lemma 7.10 in the case of scalar forms. The claims about the essential spectrum follow immediately from the Fredholm results: Since each of these operators is self-adjoint on $L^{2}$, its spectrum is contained in $\mathbb{R}$, and a real number $\lambda$ is in the essential spectrum if and only if $P-\lambda: L^{2}(M ; E) \rightarrow L^{2}(M ; E)$ is not Fredholm.

For the vector Laplacian $L^{*} L$, L. Andersson proved in $\left[\overline{\mathbf{7}}_{1}\right.$, Lemma 3.15] that the following asymptotic estimate holds:
$$\left(V, L^{*} L V\right) \gtrsim \frac{n^{2}}{8}\|V\|^{2} .$$
It follows from Proposition that $L^{*} L$ is Fredholm on $L^{2}$, and then the rest of the claims follow from Theorem \(\square\)

We conclude this chapter by observing that the sharp a priori $L^{2}$ estimates developed here for Laplace operators actually lead directly to sharp $L^{2}$ Fredholm theorems for such operators, without any need for the parametrix construction of the preceding chapter. This follows from the simple device of replacing $u$ by $\rho^{-\delta} u$ to convert unweighted $L^{2}$ estimates to weighted ones. (Cf. also [7, Lemma 3.8].)

Lemma 7.14. Let $E$ be any geometric tensor bundle over $M$, and let $P=$ $\nabla^{*} \nabla+\mathscr{K}$ be a Laplace operator acting on sections of $E$. Suppose that $P$ satisfies the asymptotic estimate
$$(u, P u) \gtrsim \lambda\|u\|^{2}$$
for some $\lambda>0$. If $|\delta|^{2}<\lambda$, there is a compact set $K \subset M$ such that the following weighted estimate holds for all $u \in C_{c}^{\infty}(M \backslash K ; E)$ :
$$\|u\|_{0,2, \delta} \leq C\|P u\|_{0,2, \delta} .$$

Proof. If $u \in C_{c}^{\infty}(M ; E)$, then
$$\begin{aligned}
\left(\rho^{-\delta} u, \nabla^{*} \nabla\left(\rho^{-\delta} u\right)\right)= & \left\|\nabla\left(\rho^{-\delta} u\right)\right\|_{g}^{2} \\
= & \int_{M}\left(\rho^{-2 \delta}|\nabla u|_{g}^{2}-2 \delta \rho^{-2 \delta}\left\langle\nabla u, u \otimes \frac{d \rho}{\rho}\right\rangle_{g}\right. \\
& \left.\quad+\delta^{2} \rho^{-2 \delta}|u|_{g}^{2}\left|\frac{d \rho}{\rho}\right|_{g}^{2}\right) d V_{g}
\end{aligned}$$
By the divergence theorem and the fact that $\Delta|u|_{g}^{2}=2\left\langle u, \nabla^{*} \nabla u\right\rangle_{g}-2|\nabla u|_{g}^{2}$,
$$\begin{aligned}
0 & =\frac{1}{2} \int_{M} d^{*}\left(\rho^{-2 \delta} d|u|_{g}^{2}\right) d V_{g} \\
& =\int_{M} \rho^{-2 \delta}\left\langle u, \nabla^{*} \nabla u\right\rangle_{g}-\rho^{-2 \delta}|\nabla u|_{g}^{2}+2 \delta \rho^{-2 \delta}\left\langle\nabla u, u \otimes \frac{d \rho}{\rho}\right\rangle_{g} d V_{g}
\end{aligned}$$
Substituting this into ( 7.13 ), we obtain
$$\left(\rho^{-\delta} u, \nabla^{*} \nabla\left(\rho^{-\delta} u\right)\right)=\left(\rho^{-\delta} u, \rho^{-\delta} \nabla^{*} \nabla u\right)+\delta^{2} \int_{M} \rho^{-2 \delta}|u|_{g}^{2}\left|\frac{d \rho}{\rho}\right|_{g}^{2} d V_{g}$$

Given $\varepsilon>0$, choose $r>0$ small enough that
$$(u, P u) \geq(\lambda-\varepsilon)\|u\|^{2}$$
whenever $u$ is smooth and compactly supported in $A_{r}$, and such that $|d \rho / \rho|_{g}^{2} \leq$ $1+\varepsilon /\left(\delta^{2}\right)$ on $A_{r}$. Applying $(\overline{1} \overline{1})$ to $\rho^{-\delta} u$ and using $(\overline{1} \overline{4})$, we obtain
$$\begin{aligned}
(\lambda-\varepsilon)\left\|\rho^{-\delta} u\right\|^{2} & \leq\left(\rho^{-\delta} u,\left(\nabla^{*} \nabla+\mathscr{K}\right)\left(\rho^{-\delta} u\right)\right) \\
& \leq\left(\rho^{-\delta} u, \rho^{-\delta}\left(\nabla^{*} \nabla+\mathscr{K}\right) u\right)+\left(\delta^{2}+\varepsilon\right)\|u\|_{0,2, \delta}^{2} \\
& \leq\|u\|_{0,2, \delta}\|P u\|_{0,2, \delta}+\left(\delta^{2}+\varepsilon\right)\|u\|_{0,2, \delta}^{2}
\end{aligned}$$
which implies (7.12) as long as $2 \varepsilon<\lambda-\delta^{2}$. \(\square\)

With this estimate in hand, it follows immediately from Lemma that $P$ is Fredholm on $H_{\delta}^{k, 2}(M ; E)$ provided that $|\delta|^{2}<\lambda$. If only $L^{2}$ results are needed, this provides an exceedingly elementary approach that can be used in many cases.

\section*{CHAPTER 8}

\section*{Einstein Metrics}

In this chapter, we will apply the linear theory we have developed so far to prove the existence of Einstein metrics. To do so, we first need to describe a systematic construction of asymptotic solutions to the Einstein equation, which will then be corrected by appealing to an appropriate linear isomorphism theorem and the inverse function theorem. The construction of asymptotic solutions is very similar to the one we described on hyperbolic space in [29], but more delicate because we start with less regularity at the boundary.

Suppose ( $M, h$ ) is an asymptotically hyperbolic Einstein ( $n+1$ )-manifold of class $C^{l, \beta}$, with $l \geq 2$ and $0<\beta<1$. Let $\rho$ be a smooth defining function for $h$, and put $\bar{h}=\rho^{2} h, \widehat{h}=\left.\bar{h}\right|_{\partial M}$.

Recall the spaces $C_{(s)}^{k, \alpha}(\bar{M} ; E)$ defined in Chapter ${ }^{3}$. By definition of the indicial map, if $P$ is a uniformly degenerate operator of order $m$ and $\bar{u} \in C_{(0)}^{m, \alpha}(\bar{M} ; E)$, then the behavior of $P\left(\rho^{s} \bar{u}\right)$ at the boundary is dominated by $\rho^{s} I_{s}(P) \bar{u}$. This in turn follows from the fact that $\rho^{-s} \partial_{i_{1}} \cdots \partial_{i_{j}}\left(\rho^{s} \bar{u}\right)=\rho^{-s} \partial_{i_{1}} \cdots \partial_{i_{j}}\left(\rho^{s}\right) \bar{u}+o\left(\rho^{-j}\right)$ in background coordinates whenever $\bar{u} \in C_{(0)}^{j, \alpha}(\bar{M})$. In the construction of our asymptotic solutions, we will need to make similar estimates when $\bar{u}$ has somewhat less regularity. The key is the following lemma.

Proposition 8.1. Suppose $0<\alpha<1,0<k+\alpha \leq l+\beta, \delta \in \mathbb{R}$, and $s, j$ are integers satisfying $1 \leq j \leq s<k+\alpha \leq l+\beta$. If $u \in C_{(s)}^{k, \alpha}(\bar{M})$, then for any indices $1 \leq i_{1}, \ldots, i_{j} \leq n+1$,
$$\rho^{-\delta} \partial_{i_{1}} \cdots \partial_{i_{j}}\left(\rho^{\delta} u\right)-\rho^{-\delta-s} \partial_{i_{1}} \cdots \partial_{i_{j}}\left(\rho^{\delta+s}\right) u \in C_{(s-j+\alpha)}^{k-j, \alpha}(\bar{M}) .$$

Proof. The proof is by induction on $j$. For $j=1$, consider first the case $\delta=0$, in which case the claim is
$$\partial_{i} u=s \rho^{-1}\left(\partial_{i} \rho\right) u \quad \bmod C_{(s-1+\alpha)}^{k-1, \alpha}(\bar{M}) .$$
We will prove this claim by induction on $k$. Observe that $\partial_{i} u$ and $s \rho^{-1}\left(\partial_{i} \rho\right) u$ are in $C_{(s-1)}^{k-1, \alpha}(\bar{M})$ by parts $\binom{e}{e}$ and $\binom{e}{\mathrm{~g}}$ of Lemma ${ }_{1}^{3} .1_{1}$. Thus to prove $(7.75 .00$ to show that the difference between the two terms is $O\left(\rho^{s-1+\alpha}\right)$.

For $k=1$, the only value of $s$ that satisfies the hypotheses is $s=1$. Since $\rho=\theta^{n+1}$ is a coordinate function, we consider separately the cases $i<n+1$ and $i=n+1$. When $i<n+1$ the right-hand side of ( 1) is zero. On the other hand, the left-hand side is in $C_{(0)}^{0, \alpha}(\bar{M})$ and vanishes on $\partial \bar{M}$ (since $u$ vanishes on $\partial M$ and $\partial_{i}$ is tangent to $\partial M$ ), so it is $O\left(\rho^{\alpha}\right)$. When $i=n+1, \rho^{-1} u \in C_{(0)}^{0, \alpha}(\bar{M})$ by Lemma
$3.1(\mathrm{~g})$, and by definition of the derivative,
$$\begin{aligned}
\partial_{n+1} u(\theta, 0) & =\lim _{\rho \rightarrow 0} \frac{u(\theta, \rho)-u(\theta, 0)}{\rho} \\
& =\lim _{\rho \rightarrow 0} \rho^{-1} u(\theta, \rho)
\end{aligned}$$
It follows that $\partial_{n+1} u-\rho^{-1}\left(\partial_{n+1} \rho\right) u=\partial_{n+1} u-\rho^{-1} u \in C_{(0)}^{0, \alpha}(\bar{M})$ and vanishes on $\partial M$, so it too is $O\left(\rho^{\alpha}\right)$. This proves (8.1) in the $k=s=1$ case.

Now let $k>1$, and suppose (8.1) holds for all smaller values of $k$. Observe that $v=\rho^{1-s} u \in C_{(1)}^{k-s+1, \alpha}(\bar{M})$ by Lemma $3.1(\mathrm{~g})$. Therefore, by the chain rule and the inductive hypothesis,
$$\begin{aligned}
\partial_{i} u & =\partial_{i}\left(\rho^{s-1} v\right) \\
& =(s-1) \rho^{s-2}\left(\partial_{i} \rho\right) v+\rho^{s-1} \partial_{i} v \\
& =(s-1) \rho^{-1}\left(\partial_{i} \rho\right) u+\rho^{s-1}\left(\rho^{-1}\left(\partial_{i} \rho\right) v+O\left(\rho^{\alpha}\right)\right) \\
& =s \rho^{-1}\left(\partial_{i} \rho\right) u+O\left(\rho^{s-1+\alpha}\right)
\end{aligned}$$
Finally, for $\delta \neq 0$, the product rule gives
$$\begin{aligned}
\rho^{-\delta} \partial_{i}\left(\rho^{\delta} u\right) & =\rho^{-\delta}\left(\delta \rho^{\delta-1}\left(\partial_{i} \rho\right) u+\rho^{\delta} \partial_{i} u\right) \\
& =\delta \rho^{-1}\left(\partial_{i} \rho\right) u+s \rho^{-1}\left(\partial_{i} \rho\right) u+O\left(\rho^{s-1+\alpha}\right) \\
& =\rho^{-\delta-s} \partial_{i}\left(\rho^{\delta+s}\right) u+O\left(\rho^{s-1+\alpha}\right) .
\end{aligned}$$
This completes the proof of the $j=1$ step.
Now suppose the proposition is true for some $j \geq 1$. For any $(j+1)$-tuple $\left(i_{1}, \ldots, i_{j+1}\right)$, beginning with the induction hypothesis in the form
$$\begin{aligned}
\partial_{i_{2}} & \cdots \\
& \in \partial_{i_{j+1}}\left(\rho^{\delta} u\right)-\rho^{-s} \partial_{i_{2}}^{k-j, \alpha} \cdots \partial_{i_{j+1}}\left(\rho^{\delta+s}\right) u \\
& (\bar{M}) \subset C_{(\delta+s-j+\alpha)}^{k-j, \alpha}(\bar{M})
\end{aligned}$$
we apply the chain rule to obtain
$$\begin{aligned}
\rho^{-\delta} \partial_{i_{1}} \cdots \partial_{i_{l+1}}\left(\rho^{\delta} u\right)= & \rho^{-\delta}\left(-s \rho^{-s-1}\left(\partial_{i_{1}} \rho\right) \partial_{i_{2}} \cdots \partial_{i_{l+1}}\left(\rho^{\delta+s}\right) u\right. \\
& +\rho^{-s} \partial_{i_{1}} \cdots \partial_{i_{l+1}}\left(\rho^{\delta+s}\right) u \\
& \left.+\rho^{-s} \partial_{i_{2}} \cdots \partial_{i_{l+1}}\left(\rho^{\delta+s}\right) \partial_{i_{1}} u\right)+O\left(\rho^{s-j-1+\alpha}\right) \\
= & \rho^{-\delta-s} \partial_{i_{1}} \cdots \partial_{i_{l+1}}\left(\rho^{\delta+s}\right) u+O\left(\rho^{s-j-1+\alpha}\right),
\end{aligned}$$
where in the last line we have used the induction hypothesis again to evaluate $\partial_{i_{1}} u$. \(\square\)

Corollary 8.2. Let $P: C^{\infty}(M ; E) \rightarrow C^{\infty}(M ; E)$ be a self-adjoint, elliptic, geometric partial differential operator of order $m \leq l$. Suppose $0<\alpha<1,0<$ $k+\alpha \leq l+\beta, \delta \in \mathbb{R}$, and $u \in C_{(s)}^{k, \alpha}(\bar{M} ; E)$, where $s$ is an integer satisfying $1 \leq s<k+\alpha \leq l+\beta$. Then
$$\left.\rho^{-\delta-s} P\left(\rho^{\delta} u\right)\right|_{\partial M}=I_{\delta+s}(P) \widehat{u},$$
where $\widehat{u}=\left.\rho^{-s} u\right|_{\partial M}$.

Proof. Write $P u$ in background coordinates as
$$P u=\sum_{0 \leq j \leq m} \sum_{i_{1}, \ldots, i_{j}} \rho^{j} a^{i_{1}, \ldots, i_{j}} \partial_{i_{1}} \cdots \partial_{i_{j}} u,$$
where $u$ is vector-valued and the coefficient functions $a^{i_{1}, \ldots, i_{j}}$ are matrix-valued. If $\bar{u} \in C_{(0)}^{m, \alpha}(M ; E)$, then an easy computation shows that
$$\rho^{-\delta-s} P\left(\rho^{\delta+s} \bar{u}\right)=\rho^{-\delta-s} \sum_{0 \leq j \leq m} \sum_{i_{1}, \ldots, i_{j}} \rho^{j} a^{i_{1}, \ldots, i_{j}} \partial_{i_{1}} \cdots \partial_{i_{j}}\left(\rho^{\delta+s}\right) \bar{u}+o(1),$$
which implies that
$$I_{\delta+s}(P) \widehat{u}=\left.\sum_{0 \leq j \leq m} \sum_{i_{1}, \ldots, i_{j}}\left(\rho^{-\delta-s} \rho^{j} a^{i_{1}, \ldots, i_{j}} \partial_{i_{1}} \cdots \partial_{i_{j}}\left(\rho^{\delta+s}\right)\right)\right|_{\partial M} \widehat{u} .$$
On the other hand, Proposition 8.1 shows that
$$\rho^{-\delta-s} P\left(\rho^{s} u\right)=\sum_{0 \leq j \leq m} \sum_{i_{1}, \ldots, i_{j}} \rho^{-\delta-s} \rho^{j} a^{i_{1}, \ldots, i_{j}} \partial_{i_{1}} \cdots \partial_{i_{j}}\left(\rho^{\delta+s}\right)\left(\rho^{-s} u\right)+O\left(\rho^{\alpha}\right),$$
which proves the result. \(\square\)

We will need an extension operator from tensor fields on $\partial M$ to $C^{l, \beta}$ tensor fields on $\bar{M}$. In [29], we did this by parallel translating along $\bar{h}$-geodesics normal to $\partial M$. However, in our present circumstances, because $\bar{h}$ may not be smooth up to the boundary, this parallel translation would lose regularity. Instead, we define our extension operator as follows.

Let $\pi:\left.T \bar{M}\right|_{\partial M} \rightarrow T \partial M$ denote the $\bar{h}$-orthogonal projection, which is clearly a $C^{l, \beta}$ bundle map over $\partial M$. Given any $C^{l, \beta}$ 2-tensor field $v$ on $\partial M$, lifting by $\pi$ yields a $C^{l, \beta}$ section $\pi^{*} v$ of $\left.\Sigma^{2} \bar{M}\right|_{\partial M}$ :
$$\pi^{*} v(X, Y)=v(\pi X, \pi Y) .$$
Define a linear map $E: C^{l, \beta}\left(\partial M ; \Sigma^{2} \partial M\right) \rightarrow C_{(0)}^{l, \beta}\left(\bar{M} ; \Sigma^{2} \bar{M}\right)$ by letting $E(\widehat{u})=$ $\varphi \Pi\left(\pi^{*} u\right)$, where $\varphi$ is a fixed cutoff function that is equal to 1 along $\partial M$ and is supported in a small collar neighborhood of the boundary, and $\Pi$ denotes parallel translation along normal geodesics with respect to some smooth background metric.

For any $C^{l, \beta}$ Riemannian metric $\widehat{g}$ on $\partial M$, we define a metric $T(\widehat{g})$ on $M$ by
$$T(\widehat{g})=h+\rho^{-2} E(\widehat{g}-\widehat{h}) .$$
Then $T: C^{l, \beta}\left(\partial M ; \Sigma^{2} \partial M\right) \rightarrow C^{l, \beta}\left(M ; \Sigma^{2} M\right)$ defines a smooth (in fact affine) map of Banach spaces. It is easy to see that if $\widehat{g}$ is sufficiently close to $\widehat{h}$ in the $C^{l, \beta}$ norm, then $T(\widehat{g})$ will be an asymptotically hyperbolic metric on $M$ of class $C^{l, \beta}$, whose conformal infinity is $[\widehat{g}]$. Moreover, since $E(0)=0$, our construction guarantees that $T(\widehat{h})=h$.

For higher-order asymptotics, we will use an extension lemma due to L. Andersson and P. Chruściel Lemma 3.3.1]. Translated into our notation, it reads as follows.

Lemma 8.3. Suppose $0 \leq \alpha<1$ and $k \geq 0$. Given an integer $s$ such that $0 \leq s \leq k$ and any $\psi \in C^{k-s, \alpha}(\partial M)$, there exists a function $u \in C_{(s)}^{k, \alpha}(\bar{M})$ such that $\left.\left(\rho^{-s} u\right)\right|_{\partial M}=\psi$.

The formula $[3.3 .6)]$ for the derivatives of $u$ makes it clear that the mapping $\psi \mapsto u$ is a bounded linear map from $C^{k-s, \alpha}(\partial M)$ to $C_{(s)}^{k, \alpha}(\bar{M})$.

Recall the operator $Q$ defined by (1.2). The next lemma gives a construction of asymptotic solutions to $Q\left(g, g_{0}\right)=0$ analogous to Theorem 2.11 of [29].

Lemma 8.4. Suppose $0<\beta<1,2 \leq l \leq n-1$, and $h$ is an asymptotically hyperbolic metric on $M$ of class $C^{l, \beta}$. Let $\widehat{g}$ be any metric on $\partial M$ of class $C^{l, \beta}$, and set $g_{0}=T(\widehat{g})$. There exists an asymptotically hyperbolic metric $g$ of class $C^{l, \beta}$ on $M$ such that $\left.\rho^{2} g\right|_{\partial M}=\widehat{g}$ and
$$Q\left(g, g_{0}\right) \in C_{(l-2+\beta)}^{l-2, \beta}\left(\bar{M} ; \Sigma^{2} \bar{M}\right) \subset C_{l+\beta}^{l-2, \beta}\left(M ; \Sigma^{2} M\right) .$$
The mapping $S: C^{l, \beta}\left(\partial M ; \Sigma^{2} \partial M\right) \rightarrow \rho^{-2} C_{(0)}^{l, \beta}\left(\bar{M} ; \Sigma^{2} \bar{M}\right)$ given by $S(\widehat{g})=g$ is a smooth map of Banach spaces.

Proof. Define a nonlinear operator
$$\bar{Q}: C_{(0)}^{l, \beta}\left(\bar{M} ; \Sigma^{2} \bar{M}\right) \times C_{(0)}^{l, \beta}\left(\bar{M} ; \Sigma^{2} \bar{M}\right) \rightarrow C_{(0)}^{l-2, \beta}\left(\bar{M} ; \Sigma^{2} \bar{M}\right)$$
by
$$\bar{Q}\left(\bar{g}, \bar{g}_{0}\right)=\rho^{2} Q\left(\rho^{-2} g, \rho^{-2} g_{0}\right) .$$
It is clear that (8.4) is equivalent to $\bar{Q}\left(\rho^{2} g, \rho^{2} g_{0}\right)=O\left(\rho^{l-2+\beta}\right)$. It follows from formula (2.19) of [29] that $\bar{Q}$ has the following expression in background coordinates:
$$\bar{Q}\left(\bar{g}, \bar{g}_{0}\right)=\mathscr{E}^{0}\left(\bar{g}, \bar{g}_{0}\right)+\rho \mathscr{E}^{1}\left(\bar{g}, \bar{g}_{0}\right)+\rho^{2} \mathscr{E}^{2}\left(\bar{g}, \bar{g}_{0}\right),$$
where $\mathscr{E}^{j}$ is a universal polynomial in the components of $\bar{g}, \bar{g}_{0}$, their inverses, and their coordinate derivatives of order less than or equal to $j$. It follows that $\bar{Q}$ takes its values in
$$C_{(0)}^{l, \beta}\left(\bar{M} ; \Sigma^{2} \bar{M}\right)+\rho C_{(0)}^{l-1, \beta}\left(\bar{M} ; \Sigma^{2} \bar{M}\right)+\rho^{2} C_{(0)}^{l-2, \beta}\left(\bar{M} ; \Sigma^{2} \bar{M}\right),$$
and is a smooth map of Banach spaces.
We will recursively construct a sequence of metrics $\bar{g}_{0}, \ldots, \bar{g}_{l} \in C_{(0)}^{l, \beta}\left(\bar{M} ; \Sigma^{2} \bar{M}\right)$ satisfying $\bar{Q}\left(\bar{g}_{k}, \bar{g}_{0}\right)=o\left(\rho^{k}\right)$. In fact, we will prove a bit more, namely that
$$\bar{Q}\left(\bar{g}_{k}, \bar{g}_{0}\right) \in \begin{cases}\rho C_{(0)}^{l-1, \beta}\left(\bar{M} ; \Sigma^{2} \bar{M}\right)+\rho^{2} C_{(0)}^{l-2, \beta}\left(\bar{M} ; \Sigma^{2} \bar{M}\right), & k=0, \\ \rho^{2} C_{(k-1)}^{l-2, \beta}\left(\bar{M} ; \Sigma^{2} \bar{M}\right), & 1 \leq k \leq l-1, \\ \rho^{2} C_{(l-2+\beta)}^{l-2, \beta}\left(\bar{M} ; \Sigma^{2} \bar{M}\right), & k=l .\end{cases}$$

Begin with $\bar{g}_{0}=\rho^{2} T(\widehat{g})$. It follows from Corollary 2.6 of [29] that
$$\bar{Q}\left(\bar{g}_{0}, \bar{g}_{0}\right)=O(\rho) .$$
Since the intersection of ( 8.5 ) with $O(\rho)$ is
$$\begin{aligned}
& C_{(1)}^{l, \beta}\left(\bar{M} ; \Sigma^{2} \bar{M}\right)+\rho C_{(0)}^{l-1, \beta}\left(\bar{M} ; \Sigma^{2} \bar{M}\right)+\rho^{2} C_{(0)}^{l-2, \beta}\left(\bar{M} ; \Sigma^{2} \bar{M}\right) \\
& \quad \subset \rho C_{(0)}^{l-1, \beta}\left(\bar{M} ; \Sigma^{2} \bar{M}\right)+\rho^{2} C_{(0)}^{l-2, \beta}\left(\bar{M} ; \Sigma^{2} \bar{M}\right)
\end{aligned}$$
we have ( 8.6 ) in the $k=0$ case.
Assume by induction that for some $k, 1 \leq k \leq l$, we have constructed $\bar{g}_{k-1} \in C_{(0)}^{l, \beta}\left(\bar{M} ; \Sigma^{2} \bar{M}\right)$ satisfying the analogue of ( 8.61 ). Then letting $\widehat{v}=$ $\left.\rho^{-k} \bar{Q}\left(\bar{g}_{k-1}, \bar{g}_{0}\right)\right|_{\partial M}$, we see from Lemma $\overline{3} \cdot \overline{1} \cdot(\overline{\mathrm{~g}})$ that $\widehat{v}$ is a $C^{l-k, \beta}$ section of $\left.T \bar{M}\right|_{\partial M}$.

If $\bar{r} \in C_{(k)}^{l, \beta}\left(\bar{M} ; \Sigma^{2} \bar{M}\right)$, the same argument as in the proof of $\left[\mathbf{2} \overline{\mathbf{q}}^{\prime}\right.$, Theorem 2.11] shows that
$$\bar{Q}\left(\bar{g}_{k-1}+\bar{r}, \bar{g}_{0}\right)=\bar{Q}\left(\bar{g}_{k-1}, \bar{g}_{0}\right)+\rho^{2}\left(\Delta_{\mathrm{L}}+2 n\right)\left(\rho^{-2} \bar{r}\right)+o\left(\rho^{k}\right)$$
By Corollary 8.2, we have
$$\left.\rho^{2-k}\left(\Delta_{\mathrm{L}}+2 n\right)\left(\rho^{-2} \bar{r}\right)\right|_{\partial M}=\left.I_{k-2}\left(\Delta_{\mathrm{L}}+2 n\right)\left(\rho^{-k} \bar{r}\right)\right|_{\partial M}+o(1) .$$
Because the indicial radius of $\Delta_{\mathrm{L}}+2 n$ is $R=n / 2, I_{s}\left(\Delta_{\mathrm{L}}+2 n\right)$ is invertible provided $-2<s<n-2$. Thus as long as $1 \leq k \leq l \leq n-1$, there is a unique $C^{l-k, \beta}$ tensor field $\psi$ along $\partial M$ such that $I_{k-2}\left(\Delta_{\mathrm{L}}+2 n\right) \psi=-\widehat{v}$. By Lemma 8.3i, there is a tensor field $\bar{r} \in C_{(k)}^{l, \beta}\left(\bar{M} ; \Sigma^{2} \bar{M}\right)$ such that $\left.\left(\rho^{-k} \bar{r}\right)\right|_{\partial M}=\psi$. Inserting this back into we conclude that $\bar{Q}\left(\bar{g}_{k-1}+\bar{r}, \bar{g}_{0}\right)=o\left(\rho^{k}\right)$, and thus actually satisfies ( $\overline{\text { 6. }}$ ). Setting $\bar{g}_{k}=\bar{g}_{k-1}+\bar{r}$ completes the inductive step.

After the $k=l$ step, we set $g=g_{l}$, and (8.4) is satisfied. The smoothness of the operator $S: \widehat{g} \mapsto g$ is immediate from the remark following Lemma \(\square\)

Proof of Theorem The proof follows closely that of Theorem 4.1 in 29 . We define an open subset $\mathscr{B} \subset C^{l, \beta}\left(\partial M ; \Sigma^{2} \partial M\right) \times C_{l+\beta}^{l, \beta}\left(M ; \Sigma^{2} M\right)$ by
$$\mathscr{B}=\{(\widehat{g}, r): \widehat{g}, T(\widehat{g}), \text { and } S(\widehat{g})+r \text { are all positive definite }\} .$$
Define a map $\mathscr{Q}: \mathscr{B} \rightarrow C^{l, \beta}\left(\partial M ; \Sigma^{2} \partial M\right) \times C_{l+\beta}^{l-2, \beta}\left(M ; \Sigma^{2} M\right)$ by
$$\mathscr{Q}(\widehat{g}, r)=(\widehat{g}, Q(S(\widehat{g})+r, T(\widehat{g}))),$$
where $T$ is defined in $(8)$ and $S$ in Lemma 4 , It follows just as in $[29]$ that $\mathscr{Q}$ is a smooth map of Banach spaces.

Since $T(\widehat{h})=S(\widehat{h})=h$ and $h$ is an Einstein metric, $\mathscr{Q}(\widehat{h}, 0)=(\widehat{h}, 0)$. As is shown in [29], the linearization of $\mathscr{Q}$ about $(\widehat{h}, 0)$ is the linear map $D \mathscr{Q}_{(\widehat{h}, 0)}$ from $C^{l, \beta}\left(\partial M ; \Sigma^{2} \partial M\right) \times C_{l+\beta}^{l, \beta}\left(M ; \Sigma^{2} M\right)$ to $C^{l, \beta}\left(\partial M ; \Sigma^{2} \partial M\right) \times C_{l+\beta}^{l-2, \beta}\left(M ; \Sigma^{2} M\right)$ given by
$$\begin{aligned}
D \mathscr{Q}_{(\widehat{h}, 0)}(\widehat{q}, r) & =\left(\widehat{q}, D_{1} Q_{(h, h)}\left(D S_{\widehat{h}} \widehat{q}+r\right)+D_{2} Q_{(h, h)}\left(D T_{\widehat{h}} \widehat{q}\right)\right) \\
& =\left(\widehat{q},\left(\Delta_{\mathrm{L}}+2 n\right) r+K \widehat{q}\right)
\end{aligned}$$
where
$$K \widehat{q}=D_{1} Q_{(h, h)}\left(D S_{\widehat{h}} \widehat{q}\right)+D_{2} Q_{(h, h)}\left(D T_{\widehat{h}} \widehat{q}\right) .$$

Because $\Delta_{\mathrm{L}}+2 n$ preserves the splitting $\Sigma^{2} M=\Sigma_{0}^{2} M \oplus \mathbb{R} g$, to show that it satisfies the hypotheses of Theorem ${ }^{7}$ we need to show that it has trivial $L^{2}$ kernel on each of these bundles separately. Since $\stackrel{\circ}{R m}(g)=\stackrel{\circ}{R} c(g)$, the action of $\Delta_{\mathrm{L}}$ on sections of $\mathbb{R} g$ is just given by the scalar Laplacian:
$$\Delta_{\mathrm{L}}(u g)=\left(\nabla^{*} \nabla u\right) g .$$
Since $2 n>0$, it follows easily from integration by parts that $\nabla^{*} \nabla u+2 n$ acting on scalar functions has trivial $L^{2}$ kernel. Thus the assumption that $\Delta_{\mathrm{L}}+2 n$ has trivial $L^{2}$ kernel on $\Sigma_{0}^{2} M$ is sufficient to allow us to apply the results of Theorem $\bar{C}_{i}$ In particular, $\Delta_{\mathrm{L}}+2 n: C_{\delta}^{l, \beta}\left(M ; \Sigma^{2} M\right) \rightarrow C_{\delta}^{l-2, \beta}\left(M ; \Sigma^{2} M\right)$ is an isomorphism for $|\delta-n / 2|<n / 2$, which is to say for $0<\delta<n$. This is true for $\delta=l+\beta$, so the linearization of $\mathscr{Q}$ has a bounded inverse given by
$$\left(D \mathscr{Q}_{(\widehat{h}, 0)}\right)^{-1}(\widehat{w}, v)=\left(\widehat{w},\left(\Delta_{\mathrm{L}}+2 n\right)^{-1}(v-K \widehat{w})\right) .$$

Therefore, by the Banach space inverse function theorem, there is a neighborhood of $(\widehat{h}, 0)$ on which $\mathscr{Q}$ has a smooth inverse. In particular, for $\widehat{g}$ sufficiently $C^{l, \beta}$ close to $\widehat{h}$, there is a solution $r \in C_{l+\beta}^{l, \beta}\left(M ; \Sigma^{2} M\right)$ to $\mathscr{Q}(\widehat{g}, r)=(\widehat{g}, 0)$.

Putting $g=S(\widehat{g})+r$ and $g_{0}=T(\widehat{g})$, we have $Q\left(g, g_{0}\right)=0$. Moreover, if the $C^{l, \beta}$ neighborhood of $\widehat{h}$ is sufficiently small, then $g$ will be uniformly $C^{2}$ close to $h$, and therefore $g$ will have strictly negative Ricci curvature. By Lemma 2.2 of [29], this implies that $g$ is Einstein. Note that $\rho^{2} r \in C_{l+2+\beta}^{l, \beta}\left(M ; \Sigma^{2} M\right)$, which is contained in $C_{(0)}^{l, \beta}\left(\bar{M} ; \Sigma^{2} \bar{M}\right)$ by Lemma $\overline{3}^{-} \overline{7}^{-}$. Since $\rho^{2} S(\widehat{g}) \in C_{(0)}^{l, \beta}\left(\bar{M} ; \Sigma^{2} \bar{M}\right)$ by construction, it follows that $g$ is asymptotically hyperbolic of class $C^{l, \beta}$ as claimed.

It remains only to prove that $\Delta_{\mathrm{L}}+2 n$ has trivial $L^{2}$ kernel on $\Sigma_{0}^{2} M$ under the assumptions stated in Theorem First suppose that $h$ has nonpositive sectional curvature. A simple algebraic argument (see [13, Lemma 12.71]) shows that if $h$ is an Einstein metric on an $(n+1)$-manifold with scalar curvature $-n(n+1)$, its Riemann curvature operator $\stackrel{\circ}{R m}$ acting on trace-free symmetric 2-tensors satisfies the following estimate at each point $p \in M$ :
$$\left\langle R^{\circ} m(u), u\right\rangle_{h} \leq\left(n+(n-1) K_{\max }(p)\right)|u|_{h}^{2},$$
where $K_{\text {max }}(p)$ is the maximum of the sectional curvatures of $h$ at $p$. (In [17, this is attributed to a hard-to-find 1979 paper of T. Fujitani; however, the argument was already given in 1978 by N. Koiso [35', Prop. 3.4].) Since the Einstein assumption implies that $\stackrel{\circ}{R} c(u)=-n u$, we have
$$\Delta_{\mathrm{L}}+2 n=\nabla^{*} \nabla-2 \stackrel{\circ}{R m}=D D^{*}+D^{*} D+n-\stackrel{\circ}{R m}$$
(see (7.10)). Therefore, if $h$ has sectional curvatures everywhere bounded above by $-\kappa \leq 0$, for any $u \in C_{c}^{\infty}\left(M ; \Sigma_{0}^{2} M\right)$ we have
$$\begin{aligned}
\left(u,\left(\Delta_{\mathrm{L}}+2 n\right) u\right) & =\left\|D^{*} u\right\|^{2}+\|D u\|^{2}+n\|u\|^{2}-(u, \operatorname{Rm}(u)) \\
& \geq(u,(n-\operatorname{Rm}) u) \\
& \geq(n-1) \kappa\|u\|^{2} .
\end{aligned}$$
The same is true for $u \in H^{2,2}\left(M ; \Sigma_{0}^{2} M\right)$ because $C_{c}^{\infty}\left(M ; \Sigma_{0}^{2} M\right)$ is dense in that space. If $\kappa>0$, it follows immediately that $\Delta_{\mathrm{L}}+2 n$ has trivial $L^{2}$ kernel. On the other hand, if $\kappa=0$, the sequence of inequalities above implies that if $u \in$ $H^{2,2}\left(M ; \Sigma_{0}^{2} M\right)$ is a solution to $\left(\Delta_{\mathrm{L}}+2 n\right) u=0$, the nonnegative quantity $\langle u,(n-$ $\stackrel{\circ}{R m}) u\rangle_{h}$ must vanish identically on $M$. Since the sectional curvatures of $h$ approach -1 at infinity, there is some compact set $K \subset M$ such that $K_{\max }(p) \leq-1 / 2$ for $p \in M \backslash K$, and then $(8.8)$ implies that $u \equiv 0$ on $M \backslash K$. Since $\Delta_{\mathrm{L}}$ is a Laplace operator, it satisfies the weak unique continuation property $[$.$] , and therefore$ $u$ is identically zero.

Finally, suppose that the conformal infinity $[\widehat{h}]$ has nonnegative Yamabe invariant. Then the result of shows that the Laplacian satisfies the following $L^{2}$ estimate for smooth, compactly supported scalar functions $u$ :
$$\left(u, \nabla^{*} \nabla u\right) \geq \frac{n^{2}}{4}\|u\|^{2} .$$
(The proof in [38] required $h$ to have a $C^{3, \alpha}$ conformal compactification. However, using Lemma 3.3.1 of , it is easy to reduce that to $C^{2, \alpha}$. See also for a
different proof.) By Lemma compactly supported tensor field, and by continuity for all $u \in H^{2,2}\left(M ; \Sigma_{0}^{2} M\right)$.

Suppose $h$ has sectional curvatures bounded above by $\left(n^{2}-8 n\right) /(8 n-8)$. Then (8.8) gives
$$2\langle u, \stackrel{\circ}{R m}(u)\rangle_{h} \leq 2\left(n+\frac{(n-1)\left(n^{2}-8 n\right)}{8 n-8}\right)|u|_{h}^{2}=\frac{n^{2}}{4}|u|_{h}^{2} .$$
If $u \in L^{2}\left(M ; \Sigma_{0}^{2} M\right)$ is a solution to $\left(\Delta_{\mathrm{L}}+2 n\right) u=0$, therefore,
$$\begin{aligned}
0 & =\left(u,\left(\Delta_{\mathrm{L}}+2 n\right) u\right) \\
& =\left(u,\left(\nabla^{*} \nabla-2 R^{\circ} m\right) u\right) \\
& =\|\nabla u\|^{2}-\frac{n^{2}}{4}\|u\|^{2}+\left(u,\left(n^{2} / 4-2 R^{\circ} m\right) u\right) \\
& \geq\left(u,\left(n^{2} / 4-2 R^{\circ} m\right) u\right) \\
& \geq 0
\end{aligned}$$
It follows as before that the nonnegative function $\left\langle u,\left(n^{2} / 4-2 \stackrel{\circ}{R m}\right) u\right\rangle_{h}$ must be identically zero, and since the operator $\left(n^{2} / 4-2 R m\right)$ is positive definite outside a compact set, $u$ must be identically zero by analytic continuation. \(\square\)

\section*{Bibliography}
\begin{itemize}
\item[1.] S. Agmon, A. Douglis, and L. Nirenberg, Estimates near the boundary for solutions of elliptic partial differential equations satisfying general boundary conditions. II, Comm. Pure Appl. Math. 17 (1964), 35-92.
\item[2.] Michael T. Anderson, $L^{2}$ curvature and volume renormalization of $A H E$ metrics on 4 manifolds, Math. Res. Lett. 8 (2001), 171-188.
\item[3.] $\_\_\_\_$, Einstein metrics with prescribed conformal infinity on 4-manifolds, arXiv:math.DG/0105243, 2001/2004.
\item[4.] $\_\_\_\_$, Boundary regularity, uniqueness and non-uniqueness for $A H$ Einstein metrics on 4-manifolds, Adv. Math. 179 (2003), 205-249.
\item[5.] $\_\_\_\_$, Some results on the structure of conformally compact Einstein metrics, arXiv:math.DG/0402198, 2004/2005.
\item[6.] $\_\_\_\_$, Geometric aspects of the AdS/CFT correspondence, AdS/CFT correspondence: Einstein metrics and their conformal boundaries, IRMA Lect. Math. Theor. Phys., vol. 8, Eur. Math. Soc., Zürich, 2005, pp. 1-31.
\item[7.] Lars Andersson, Elliptic systems on manifolds with asymptotically negative curvature, Indiana Univ. Math. J. 42 (1993), 1359-1388.
\item[8.] Lars Andersson and Piotr T. Chruściel, Solutions of the constraint equations in general relativity satisfying "hyperboloidal boundary conditions", Dissertationes Math. (Rozprawy Mat.) 355 (1996), 1-100.
\item[9.] N. Aronszajn, $A$ unique continuation theorem for solutions of elliptic partial differential equations or inequalities of second order, J. Math. Pures Appl. (9) 36 (1957), 235-249.
\item[10.] Thierry Aubin, Some nonlinear problems in Riemannian geometry, Springer-Verlag, Berlin, 1998.
\item[11.] Toby N. Bailey, Michael G. Eastwood, and C. Robin Graham, Invariant theory for conformal and CR geometry, Ann. of Math. (2) 139 (1994), 491-552.
\item[12.] Robert Bartnik, The mass of an asymptotically flat manifold, Comm. Pure Appl. Math. 39 (1986), 661-693.
\item[13.] Arthur L. Besse, Einstein manifolds, Springer-Verlag, Berlin, 1987.
\item[14.] Olivier Biquard, Einstein deformations of hyperbolic metrics, Surveys in differential geometry: essays on Einstein manifolds, Int. Press, Boston, MA, 1999, pp. 235-246.
\item[15.] $\_\_\_\_$, Métriques d'Einstein asymptotiquement symétriques, Astérisque 265 (2000), vi+109.
\item[16.] $\_\_\_\_$, Métriques autoduales sur la boule, Invent. Math. 148 (2002), 545-607.
\item[17.] Garrett Birkhoff and Gian-Carlo Rota, Ordinary differential equations, fourth ed., John Wiley \& Sons Inc., New York, 1989.
\item[18.] Mingliang Cai and Gregory J. Galloway, Boundaries of zero scalar curvature in the AdS/CFT correspondence, Adv. Theor. Math. Phys. 3 (1999), 1769-1783 (2000), arXiv:hep-th/0003046.
\item[19.] Isaac Chavel, Riemannian geometry-a modern introduction, Cambridge University Press, Cambridge, 1993.
\item[20.] S. Y. Cheng and S. T. Yau, Differential equations on Riemannian manifolds and their geometric applications, Comm. Pure Appl. Math. 28 (1975), 333-354.
\item[21.] Piotr T. Chruściel, Erwann Delay, John M. Lee, and Dale N. Skinner, Boundary regularity of conformally compact Einstein metrics, arXiv:math.DG/0401386, to appear in J. Differential Geom., 2005.
\item[22.] Erwann Delay, Étude locale d'opérateurs de courbure sur l'espace hyperbolique, J. Math. Pures Appl. (9) 78 (1999), 389-430.
\item[23.] $\_\_\_\_$, Essential spectrum of the Lichnerowicz Laplacian on two tensors on asymptotically hyperbolic manifolds, J. Geom. Phys. 43 (2002), 33-44.
\end{itemize}
24. Erwann Delay and Marc Herzlich, Ricci curvature in the neighborhood of rank-one symmetric spaces, J. Geom. Anal. 11 (2001), 573-588.
25. Harold Donnelly and Frederico Xavier, On the differential form spectrum of negatively curved Riemannian manifolds, Amer. J. Math. 106 (1984), 169-185.
26. Avron Douglis and Louis Nirenberg, Interior estimates for elliptic systems of partial differential equations, Comm. Pure Appl. Math. 8 (1955), 503-538.
27. Arthur Erdélyi, Wilhelm Magnus, Fritz Oberhettinger, and Francesco G. Tricomi, Higher transcendental functions, Vol. I, McGraw-Hill Book Company, Inc., New York-Toronto-London, 1953, Based, in part, on notes left by Harry Bateman.
28. Charles Fefferman and C. Robin Graham, Conformal invariants, Astérisque (1985), 95-116, The mathematical heritage of Élie Cartan (Lyon, 1984).
29. C. Robin Graham and John M. Lee, Einstein metrics with prescribed conformal infinity on the ball, Adv. Math. 87 (1991), 186-225.
30. C. Robin Graham and Edward Witten, Conformal anomaly of submanifold observables in AdS/CFT correspondence, Nuclear Phys. B 546 (1999), 52-64.
31. N. J. Hitchin, Twistor spaces, Einstein metrics and isomonodromic deformations, J. Differential Geom. 42 (1995), 30-112.
32. $\_\_\_\_$, Einstein metrics and the eta-invariant, Boll. Un. Mat. Ital. B (7) 11 (1997), 95-105.
33. James Isenberg and Jiseong Park, Asymptotically hyperbolic non-constant mean curvature solutions of the Einstein constraint equations, Classical Quantum Gravity 14 (1997), A189-A201, Geometry and physics.
34. Tosio Kato, Perturbation theory for linear operators, Classics in Mathematics, Springer-Verlag, Berlin, 1995, Reprint of the 1980 edition.
35. Norihito Koiso, Nondeformability of Einstein metrics, Osaka J. Math. 15 (1978), 419-433.
36. Robert Lauter, Bertrand Monthubert, and Victor Nistor, Pseudodifferential analysis on continuous family groupoids, Doc. Math. 5 (2000), 625-655 (electronic).
37. C. R. LeBrun, $\mathscr{H}$-space with a cosmological constant, Proc. Roy. Soc. London Ser. A 380 (1982), 171-185.
38. John M. Lee, The spectrum of an asymptotically hyperbolic Einstein manifold, Comm. Anal. Geom. 3 (1995), 253-271.
39. Rafe Mazzeo, Hodge cohomology of negatively curved manifolds, Ph.D. thesis, MIT, 1986.
40. $\_\_\_\_$, The Hodge cohomology of a conformally compact metric, J. Differential Geom. 28 (1988), 309-339.
41. $\_\_\_\_$, Elliptic theory of differential edge operators. I, Comm. Partial Differential Equations 16 (1991), 1615-1664.
42. Rafe Mazzeo and Richard B. Melrose, Meromorphic extension of the resolvent on complete spaces with asymptotically constant negative curvature, J. Funct. Anal. 75 (1987), 260-310.
43. H. P. McKean, An upper bound to the spectrum of $\Delta$ on a manifold of negative curvature, J. Differential Geometry 4 (1970), 359-366.
44. Richard B. Melrose, Transformation of boundary problems, Acta Math. 147 (1981), 149-236.
45. Richard B. Melrose and Gerardo Mendoza, Elliptic pseudodifferential operators of totally characteristic type, MSRI preprint, 1983.
46. Maung Min-Oo, Scalar curvature rigidity of asymptotically hyperbolic spin manifolds, Math. Ann. 285 (1989), 527-539.
47. Gen Nakamura, Gunther Uhlmann, and Jenn-Nan Wang, Unique continuation property for elliptic systems and crack determination in anisotropic elasticity, Partial differential equations and inverse problems, Contemp. Math., vol. 362, Amer. Math. Soc., Providence, RI, 2004, pp. 321-338.
48. Louis Nirenberg, Estimates and existence of solutions of elliptic equations, Comm. Pure Appl. Math. 9 (1956), 509-529.
49. Jiseong Park, Non-constant mean curvature hyperboloidal solutions of the Einstein constraint equations, Ph.D. thesis, University of Oregon, 1996.
50. H. Pedersen, Einstein metrics, spinning top motions and monopoles, Math. Ann. 274 (1986), 35-59.
51. R. Penrose, Structure of space-time, Battelle Rencontres: 1967 Lectures in Mathematics and Physics (Cecile M. DeWitt and John A. Wheeler, eds.), W. A. Benjamin Inc., New York, 1998, pp. 121-235.
\begin{itemize}
\item[52.] Jens Lyng Petersen, Introduction to the Maldacena conjecture on AdS/CFT, Int. J. Modern Phys. A 14 (1999), 3597-3672.
\item[53.] Johan Råde, Elliptic uniformly degenerate operators, Chalmers University of Technology (Göteburg University) preprint \#1998-19, 1998.
\item[54.] John Charles Roth, Perturbations of Kähler-Einstein metrics, Ph.D. thesis, University of Washington, 1999.
\item[55.] Peter Stredder, Natural differential operators on Riemannian manifolds and representations of the orthogonal and special orthogonal groups, J. Differential Geometry 10 (1975), 647-660.
\item[56.] Dennis Sullivan, Related aspects of positivity in Riemannian geometry, J. Differential Geom. 25 (1987), 327-351.
\item[57.] Xiaodong Wang, A new proof of Lee's theorem on the spectrum of conformally compact Einstein manifolds, Comm. Anal. Geom. 10 (2002), 647-651.
\item[58.] Edward Witten, Supersymmetry and Morse theory, J. Differential Geom. 17 (1982), 661-692 (1983).
\item[59.] $\_\_\_\_$, Anti de Sitter space and holography, Adv. Theor. Math. Phys. 2 (1998), 253-291, arXiv:hep-th/9802150.
\item[60.] Hung Hsi Wu, The Bochner technique in differential geometry, Math. Rep. 3 (1988), i-xii and 289-538.
\end{itemize}