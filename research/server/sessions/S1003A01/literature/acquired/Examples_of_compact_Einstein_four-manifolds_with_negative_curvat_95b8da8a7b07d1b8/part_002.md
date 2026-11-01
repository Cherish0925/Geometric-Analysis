---
retention_scope: session
part: 2
total_parts: 3
---

[Part 2/3 of: Examples of compact Einstein four-manifolds with negative curvature]

We begin with a word on the definition of unweighted Hölder spaces.
Definition 4.5. Let $(X, g)$ be a compact Riemannian manifold. Write $\rho(g)$ for the conjugacy radius of $g$ and fix $\rho_{0}<\rho(g)$. Given $x \in X$ write $\exp _{x}: T_{x} X \rightarrow X$ for the exponential map, which is a local diffeomorphism on the ball $B\left(0, \rho_{0}\right) \subset T_{x} X$. Let $s$ be a tensor field on $X$. Then $\exp _{x}^{*}(s)$ is a tensor field on the Euclidean vector space $T_{x} X$ and we can use the Euclidean metric to define the Hölder coefficient of $s$ near $x$ :
$$[s]_{\eta, x}:=\sup _{p \neq q \in B\left(0, \rho_{0}\right)} \frac{\left|\exp _{x}^{*}(s)(p)-\exp _{x}^{*}(s)(q)\right|}{|p-q|^{\eta}}$$
We then take the supremum over all points $x$ and combine with derivatives to take the full Hölder norm:
$$\|s\|_{C^{m, \eta}}:=\sum_{j \leq m} \sup _{x \in X}\left|\nabla^{j} s(x)\right|+\sup _{x \in X}\left[\nabla^{m} s\right]_{\eta, x}$$

This definition of the Hölder norm is well adapted to studying sequences ( $X_{k}, g_{k}$ ) for which there is a uniform bound for the curvature and its derivatives: for all $m \in \mathbb{N}$ there exists $C>0$ such that $\left\|\operatorname{Rm}\left(g_{k}\right)\right\|_{C^{m}} \leq C$.

Our sequence of approximately Einstein metrics have uniform $C^{m}$ bounds on $\operatorname{Rm}\left(g_{k}\right)$, thanks to part 4 of Proposition 3.1.

We now move to the weighted norms. We begin by defining the weight function $w$.
Lemma 4.6. For all large $k$, there exists a smooth function $w: X_{k} \rightarrow \mathbb{R}$ such that
\begin{itemize}
\item[1.] In the region $\left\{u<\frac{1}{2} U_{k, \max }\right\}, w=u$.
\end{itemize}
\begin{itemize}
\item[2.] Outside the region $\left\{u<U_{k, \max }\right\}, w=U_{k, \max }$.
\item[3.] For each $m$, there is a constant $C$ (not depending on $k$ ), such that $\left|\nabla^{m} w\right| \leq C|w|$ (where the norm is taken with $g_{k}$ ).
\end{itemize}

Proof. Near each component of the branch locus we have a distinguished coordinate $u$, used in the construction of the model metric, given by (3.2) and (3.3). It is defined for $u_{a} \leq u<U_{k, \text { max }}$ (where $a$ is chosen so that the metric on $M_{k}$ has cone angles $2 \pi / l$ ). We extend this to a function $w: X_{k} \rightarrow \mathbb{R}$ by setting it to be constant, equal to $U_{k, \text { max }}$ outside the region $\left\{u<U_{k, \text { max }}\right\}$. We then modify it in the region $\frac{1}{2} U_{k, \text { max }} \leq u \leq U_{k, \text { max }}$ to make this extension smooth. The estimate on the derivatives of $w$ follows from (3.4). \(\square\)

Definition 4.7. Let $m \in \mathbb{N}, 0 \leq \eta<1$ and $\alpha>0$. Given a symmetric bilinear form $s$, we define the weighted Hölder norm of $s$ to be
$$\|s\|_{C_{\alpha}^{m, \eta}}:=\left\|w^{\alpha} s\right\|_{C^{m, \eta}}$$
where $w$ is the weight function of Lemma 4.6 and the norm is taken for $g_{k}$.
The following result is typical in the use of weight functions and we refer for instance to [9], §3.8. Recall that the uniform control on sectional curvatures of $g_{k}$ gives a uniform lower bound on the conjugacy radius $\rho\left(g_{k}\right) \geq \rho_{0}$ of the manifolds $\left(X_{k}, g_{k}\right)$.

Lemma 4.8. Let $m \in \mathbb{N}, 0 \leq \eta<1$ and $0<\rho \leq \rho_{0}$. Then there exists a constant $C=C(m, \eta, \rho)>0$ such that for any $x \in X_{k}$ and any symmetric bilinear form $s$ of regularity $C^{m, \eta}$, we have
$$\frac{1}{C} w(x)^{\alpha}\|s\|_{C^{m, \eta}\left(B_{x}(\rho)\right)} \leq\|s\|_{C_{\alpha}^{m, \eta}\left(B_{x}(\rho)\right)} \leq C w(x)^{\alpha}\|s\|_{C^{m, \eta}\left(B_{x}(\rho)\right)}$$
where $B_{x}(\rho) \subset\left(X_{k}, g_{k}\right)$ denotes the geodesic ball centred at $x$ with radius $\rho$. In particular, $C$ is independent of both $x$ and $k$.

An easy consequence is the following:
Corollary 4.9. For any $m, 0 \leq \eta<1$ and $\alpha>0$ there is a constant $C$, independent of $k$, such that for all $s \in C^{m, \eta}$,
$$\|s\|_{C^{m, \eta}} \leq C\|s\|_{C_{\alpha}^{m, \eta}}$$
Proof. This follows from Lemma 4.8, taking the supremum over $x$, together with the fact that $w \geq u_{a}>0$, a lower bound which is independent of $k$. \(\square\)

As a consequence of the definition of the weighted norms and of Proposition (3.1) we have:

Lemma 4.10. For all integers $m \geq 0$ and real numbers $0 \leq \eta<1$, there is a constant $A$ such that
$$\left\|\operatorname{Ric}\left(g_{k}\right)+(n-1) g_{k}\right\|_{C_{\alpha}^{m, \eta}} \leq A U_{k}^{1-n+\alpha}$$

We conclude this section by stating without proof the weighted analogues of standard elliptic estimates.

Lemma 4.11. Fix an integer $m \geq 2$, and real numbers $0 \leq \eta<1$ and $\alpha>0$. There are constants $\delta, C>0$, independent of $k$, such that if $g$ and $h$ are Riemannian metrics on $X_{k}$ with
$$\left\|g-g_{k}\right\|_{C^{m+2, \eta}},\left\|h-g_{k}\right\|_{C^{m+2, \eta}} \leq \delta$$
then for all symmetric bilinear forms $s$ of regularity $C_{\alpha}^{m+2, \eta}$ we have
$$\left\|\left(L_{g}-L_{h}\right)(s)\right\|_{C_{\alpha}^{m, \eta}} \leq C\|g-h\|_{C^{m+2, \eta}}\|s\|_{C_{\alpha}^{m+2, \eta}}$$
(where all norms are taken with respect to $g_{k}$ ).
Remark 4.12. Note that by Corollary 4.9, we are free to replace the unweighted norms on the metrics in this result by weighted ones (at the expense of shrinking $\delta$ ). We will frequently do this in applications of this result.

Lemma 4.13. For any integer $m$ and real numbers $0<\eta<1$ and $\alpha \geq 0$ there are constants $\delta, C>0$, independent of $k$, such that if $g$ is a Riemannian metric on $X_{k}$ with
$$\left\|g-g_{k}\right\|_{C_{\alpha}^{m+2, \eta}} \leq \delta$$
then for all symmetric bilinear forms $s$ of regularity $C^{m+2, \eta}$, we have
$$\|s\|_{C_{\alpha}^{m+2, \eta}} \leq C\left(\left\|L_{g}(s)\right\|_{C_{\alpha}^{m, \eta}}+\|s\|_{C_{\alpha}^{0}}\right)$$
(where all norms are taken with respect to $g_{k}$ ).
Fix an integer $m \geq 2$, and real numbers $0<\eta<1$ and $\alpha>0$. We claim that there are constants $\delta>0$ (independent of $k$ ) and $C_{k}>0$ (depending on $k$ ) such that if $g$ is a Riemannian metric on $X_{k}$ with
$$\left\|g-g_{k}\right\|_{C_{\alpha}^{m+2, \eta}} \leq \delta$$
then for all symmetric bilinear forms $s$ of regularity $C^{m, \eta}$ we have
$$\|s\|_{C_{\alpha}^{m+2, \eta}} \leq C_{k}\left\|L_{g}(s)\right\|_{C_{\alpha}^{m, \eta}}$$

This follows from the previous results of this section and is essentially the standard contradiction argument used to remove the $C^{0}$ term in the elliptic estimate, based on the fact that $L_{g}$ is invertible by Proposition 4.3. Note that the constant in (4.17) depends on $k$, because the contradiction argument must be carried out on each $X_{k}$ separately.

\subsection*{4.4 The proof assuming a key estimate}

We now explain how to perturb $g_{k}$ to an Einstein metric, assuming temporarily one critical estimate, Theorem 4.15 below. We will prove this estimate in the case $\operatorname{dim} X_{k}=4$ in the following section.

The first step in the proof is to apply a version of the inverse function theorem to $\Phi_{k}$ with uniformity in $g$, if not in $k$. We state the result here:

Proposition 4.14. Fix an integer $m \geq 0$ and real numbers $0<\eta<1$ and $\alpha>0$. There exist constants $\delta>0$ (independent of $k$ ) and $r_{k}>0$ (depending on $k$ ) such that if $g$ is a Riemannian metric on $X_{k}$ with
$$\left\|g-g_{k}\right\|_{C_{\alpha}^{m+2, \eta}} \leq \delta$$
then $B\left(\Phi_{k}(g), r_{k}\right) \subset C_{\alpha}^{m, \eta}$ is contained in the image of $\Phi_{k}$ and there is a differentiable map
$$\Psi_{k}: B\left(\Phi_{k}(g), r_{k}\right) \rightarrow C_{\alpha}^{m+2, \eta}$$
inverting $\Phi_{k}$ on a neighbourhood of $g \in C_{\alpha}^{m+2, \eta}$.
Proof. This is just an application of the inverse function theorem to $\Phi_{k}$ at $g$, where the invertibility is given by Proposition 4.3. The inverse function theorem provides a quantitative estimate on the radius of a ball centred at $\Phi_{k}(g)$ which is contained in the image of $\Phi_{k}$. By the uniform Lipschitz continuity of $\Phi_{k}$ (Lemma 4.11) this radius depends only on the square inverse of the operator norm of $L_{g}=\mathrm{d} \Phi_{k}(g)$. By (4.17) we can choose such a bound to only depend on $k$. \(\square\)

Of course, this is far from enough to prove the existence of an Einstein metric. Whilst $\Phi_{k}\left(g_{k}\right)$ tends to zero as $k$ tends to infinity, the radius $r_{k}$ may tend to zero even quicker. To remedy this problem we will use a much sharper estimate on $L_{g}^{-1}$. It is at this point our argument requires $\operatorname{dim} X_{k}=4$.

As a matter of notation, write
$$S_{k}=\left\{\frac{1}{2} U_{k} \leq u \leq U_{k}\right\}$$
Recall that $\operatorname{Ric}\left(g_{k}\right)+3 g_{k}$ is supported in $S_{k}$. Recall also that until now, our choice of gluing parameter $U_{k}$ has only had to satisfy the requirements that $U_{k} \rightarrow \infty$ and $U_{k} \leq \frac{1}{2} U_{k, \text { max }}$. We will need to be more careful in our choice of $U_{k}$ in order to prove the estimate we want.

Theorem 4.15. Let $\operatorname{dim} X_{k}=4$. There is a choice $\left(U_{k}\right)$ of gluing parameters such that for the corresponding approximately Einstein manifolds $\left(X_{k}, g_{k}\right)$ the following holds. For any integer $m \geq 1$ and real number $0<\eta<1$ there exists real numbers $0<\alpha<3$ and $\delta>0$ and a sequence $\left(\epsilon_{k}\right)$ of positive real numbers, with $\epsilon_{k} \rightarrow 0$ as $k \rightarrow \infty$ which have the following property. For all large $k$, if $g$ is a Riemannian metric on $X_{k}$ with
$$\left\|g-g_{k}\right\|_{C_{\alpha}^{m+2, \eta}} \leq \delta$$
then for any symmetric bilinear tensor $s \in C_{\alpha}^{m+2, \eta}$, with $L_{g}(s)$ supported in $S_{k}$ we have
$$\|s\|_{C_{\alpha}^{0}} \leq \epsilon_{k} U_{k}^{3-\alpha}\left\|L_{g}(s)\right\|_{C_{\alpha}^{m, \eta}}$$

It is crucial in Theorem 4.15 that we restrict attention to those $s$ with $L_{g}(s)$ supported in $S_{k}$. It seems that the sought-after estimate will not hold otherwise. Whilst our proof does not extend to arbitrary dimensions, it seems plausible that the analogous estimate could hold in dimension $n$ (with the power $U_{k}^{n-1+\alpha}$ on the right-hand side). This would
then imply the existence of Einstein metrics for these higher dimensional Gromov-Thurston manifolds.

Theorem 4.15 is the core of the analysis of this paper and we prove it in the following section. For the remainder of this section we show how this refined estimate proves the existence of an Einstein metric.

Proof of Theorem 1.2, assuming Theorem 4.15. Let $\gamma(t)=(1-t) \Phi_{k}\left(g_{k}\right)$. Proposition 4.14 gives a smooth path of Riemannian metrics $g(t)$ solving $\Phi_{k}(g(t))=\gamma(t)$ for
$$0 \leq t<\frac{r_{k}}{\left\|\Phi_{k}\left(g_{k}\right)\right\|_{C_{\alpha}^{m, \eta}}}$$
We will show this path can be extended up to $t=1$, and then $g(1)$ is the Einstein metric we seek.

Let $\delta>0$ be small enough so that Lemma 4.13, Proposition 4.14 and Theorem 4.15 all apply simultaneously. Write $B_{\delta} \subset C_{\alpha}^{m+2, \eta}$ for the ball of radius $\delta$ centred at $g_{k}$. Consider the set
$T=\left\{\tau>0:\right.$ there is a differentiable map $g:[0, \tau] \rightarrow B_{\delta}$ with $\left.\Phi_{k}(g(t))=\gamma(t), g(0)=g_{k}\right\}$
Let $\sigma=\sup T$. By Proposition 4.14 we know that
$$\sigma \geq \frac{r_{k}}{\left\|\Phi_{k}\left(g_{k}\right)\right\|_{C_{\alpha}^{m, \eta}}}$$
We will show that $\sigma<1$ gives a contradiction. Consider
$$\tau=\sigma-\frac{r_{k}}{2\left\|\Phi_{k}\left(g_{k}\right)\right\|_{C_{\alpha}^{m, \eta}}}$$
We have $0<\tau<\sigma$ and so the path $g(t)$ exists on $[0, \tau]$ and stays inside $B_{\delta}$. By Proposition 4.14, $\Phi_{k}$ is a local diffeomorphism at $g(\tau)$ and its image contains the ball of radius $r_{k}$ centred at $\gamma(\tau)$. In particular it contains $\gamma(t)$ for
$$t \in\left[\tau, \sigma+\frac{r_{k}}{2\left\|\Phi_{k}\left(g_{k}\right)\right\|_{C_{\alpha}^{m, \eta}}}\right]$$
So we can actually extend $g(t)$ smoothly to solve $\Phi_{k}(g(t))=\gamma(t)$ for values of $t$ slightly larger than $\sigma$. The crux is to show that in doing so we do not leave $B_{\delta}$.

To prove this, differentiate $\Phi_{k}(g(t))=(1-t) \Phi_{k}\left(g_{k}\right)$ with respect to $t$ to get
$$L_{g(t)}\left(g^{\prime}(t)\right)=-\Phi_{k}\left(g_{k}\right)$$
For $t \in[0, \sigma), g(t) \in B_{\delta}$ and so, for these times, we can apply the elliptic estimate Lemma 4.13 and Theorem 4.15. This, together with the error estimate Lemma 4.10, gives
$$\begin{aligned}
\left\|g^{\prime}(t)\right\|_{C_{\alpha}^{m+2, \eta}} & \leq C\left(\left\|\Phi_{k}\left(g_{k}\right)\right\|_{C_{\alpha}^{m, \eta}}+\left\|g^{\prime}(t)\right\|_{C_{\alpha}^{0}}\right) \\
& \leq A C\left(1+\epsilon_{k} U_{k}^{n-1-\alpha}\right) U_{k}^{1-n+\alpha}
\end{aligned}$$

This bound tends to zero as $k$ tends to infinity and so for all large $k$ we have $\left\|g^{\prime}(t)\right\|_{C_{\alpha}^{m+2, \eta}}<$ $\delta$. Integrating this from $t=0$ to $t=\sigma$, we see that
$$\left\|g(\sigma)-g_{k}\right\|_{C_{\alpha}^{m+2, \eta}} \leq \sigma \delta$$
So the assumption that $\sigma<1$ means $g(\sigma) \in B_{\delta}$ and hence $g(t) \in B_{\delta}$ for $t$ slightly larger that $\sigma$. This is a contradiction with the fact that $\sigma=\sup T$.

We write $g$ for the Einstein metric on $X_{k}$ found in this way. To check that the sectional curvatures of $g$ are negative, recall that there is a constant $c>0$ such that the sectional curvatures of the approximate solution $g_{k}$ all satisfy $\sec \left(g_{k}\right) \leq-c$. By construction, our Einstein metric $g$ is of the form $g=g_{k}+s_{k}$ where $\left\|s_{k}\right\|_{C^{2, \eta}} \rightarrow 0$. From this it follows that the sectional curvatures of $g$ satisfy $\sec (g) \leq-c / 2$.

We now check that $g$ is not simply locally homogeneous. There is a constant $b>0$ such that the model metric of Propositon 3.2 has at least one sectional curvature at finite distance from the branch locus, which satisfies sec $\geq-1+b$. (This follows from the explicit form of the sectional curvatures given in the proof of Lemma 3.4.) Since $g$ is a $C^{2}$-small perturbation of this metric near the branch locus, it must have a a sectional curvature which satisfies $\sec \geq-1+b / 2$. However, the approximate solution $g_{k}$ is genuinely hyperbolic at large distances and so at these distances all sectional curvatures of the Einstein metric $g$ satisfy sec $<-1+b / 2$. It follows that $g$ near the branch locus is not locally isometric to $g$ at large distances and hence $g$ is not locally homogeneous. \(\square\)

Remark 4.16. In the proof of Theorem 4.15, the weighted control of $g_{k}-g$ plays a crucial role, as can be seen for instance in the proof of Lemma 5.10. We stated Lemma 4.13 and Proposition (4.14) with a weighted control on the metrics to be coherent, but they remain true if one only assumes that $\left\|g-g_{k}\right\|_{C^{m+2, \eta}} \leq \delta$.

\section*{5 Proving the key estimate}

In this section we prove Theorem 4.15, which completes the proof of Theorem 1.2. We quickly recall some of our notation. $U_{k, \text { max }}=\cosh \left(\frac{1}{2} i\left(M_{k}\right)\right)$, where $i\left(M_{k}\right)$ is the injectivity radius of $M_{k}$ with the hyperbolic metric; the gluing is carried out in the region $\frac{1}{2} U_{k} \leq u \leq$ $U_{k}$, where $U_{k}<\frac{1}{2} U_{k, \text { max }}$. In the course of the proof, it will be important how we choose the gluing parameter $U_{k}$. For now, we stipulate only that $U_{k} \rightarrow \infty$ whilst $U_{k} / U_{k, \text { max }} \rightarrow 0$. The precise choice will be made later.

The proof is by contradiction and so we assume Theorem 4.15 is false. I.e.:
Hypothesis which will lead to a contradiction. Let $m \geq 1$. Let $\alpha>0, \delta_{0}>0,\left(\epsilon_{k}\right)$ be a sequence of positive real numbers with $\epsilon_{k} \rightarrow 0$ and let $N_{0} \in \mathbb{N}$. Then there exist $k_{0} \geq N_{0}$, $\tilde{g}_{k_{0}}$ a metric on $X_{k}$ with
$$\left\|\tilde{g}_{k_{0}}-g_{k_{0}}\right\|_{C_{\alpha}^{m+2, \eta}} \leq \delta_{0}$$
and $s_{k_{0}} \in C_{\alpha}^{m+2, \eta}$ with $L_{\tilde{g}_{k_{0}}}\left(s_{k_{0}}\right)$ supported in $S_{k_{0}}$, such that
$$\left\|s_{k_{0}}\right\|_{C_{\alpha}^{0}}>\epsilon_{k_{0}} U_{k_{0}}^{3-\alpha}\left\|L_{\tilde{g}_{k_{0}}}\left(s_{k_{0}}\right)\right\|_{C_{\alpha}^{m, \eta}}$$

We fix $\alpha$ and take $\epsilon_{k}=U_{k}^{-p}$ for some small positive number $p$. Both $\alpha$ and $p$ will be determined in the course of the proof. We now apply our hypothesis with $\delta_{0}$ replaced by a sequence $\delta_{q}>0$ with $\delta_{q} \rightarrow 0$ and $N_{0}$ replaced by a sequence $N_{q} \in \mathbb{N}$ with $N_{q} \rightarrow \infty$. This gives a sequence $\tilde{g}_{k_{q}}$ of metrics and symmetric bilinear forms $s_{k_{q}}$ on $X_{k_{q}}$ such that the conclusions of the hypothesis are satisfied. To ease the notation, we pass to this subsequence and drop the $q$ subscript. This leads to a sequence $\left(\tilde{g}_{k}\right)$ of metrics with
$$\left\|\tilde{g}_{k}-g_{k}\right\|_{C_{\alpha}^{m+2, \eta}} \rightarrow 0$$
as $k \rightarrow \infty$, and a sequence $\left(s_{k}\right)$ of symmetric bilinear forms for which $L_{\tilde{g}_{k}}\left(s_{k}\right)$ is supported in $S_{k}$ and
$$\left\|s_{k}\right\|_{C_{\alpha}^{0}}>U_{k}^{3-\alpha-p}\left\|L_{\tilde{g}_{k}}\left(s_{k}\right)\right\|_{C_{\alpha}^{m, \eta}}$$

We will prove that (5.2) actually never holds, giving our contradiction. To do this, for each $k$ we pick $x_{k} \in X_{k}$ at which
$$w^{\alpha}\left(x_{k}\right)\left|s_{k}\left(x_{k}\right)\right|_{g_{k}}=\left\|s_{k}\right\|_{C_{\alpha}^{0}}$$
where $w$ is the weight constructed in Lemma 4.6.
First, a word on notation. Given sequences $\left(p_{k}\right)$ and $\left(q_{k}\right)$ of real numbers, we write $p_{k} \lesssim q_{k}$ to mean that there is a constant $C>0$ such that for all $k, p_{k} \leq C q_{k}$. In a chain of such inequalities, $p_{k} \lesssim q_{k} \lesssim r_{k}$, the constant $C$ may change, but will always be independent of $k$.

The first step in the proof is a preliminary lemma, showing that the $C_{\alpha}^{0}$-norm of $L_{\tilde{g}_{k}}\left(s_{k}\right)$ gives control of $s_{k}$ in $W^{1,2}$. It is at this point that the crucial bound on the volume of the branch locus, derived in §2, enters the analysis. Recall part 3 of Proposition 1.1, which says that, in arbitrary dimension,
$$\operatorname{vol}\left(\Sigma_{k}\right) \leq A \exp \left(\frac{n^{2}-3 n+6}{4} i\left(M_{k}\right)\right)$$
In our case, $n=4$. By definition of $U_{k, \text { max }}$ we deduce that
$$\operatorname{vol}\left(\Sigma_{k}\right) \lesssim U_{k, \max }^{5}$$

Lemma 5.1. We have
$$\begin{aligned}
\left\|L_{\tilde{g}_{k}}\left(s_{k}\right)\right\|_{L^{2}} & \lesssim U_{k, \max }^{\frac{5}{2}} U_{k}^{\frac{3}{2}-\alpha}\left\|L_{\tilde{g}_{k}}\left(s_{k}\right)\right\|_{C_{\alpha}^{0}} \\
\left\|s_{k}\right\|_{L^{2}}+\left\|\nabla s_{k}\right\|_{L^{2}} & \lesssim U_{k, \max }^{\frac{5}{2}} U_{k}^{\frac{3}{2}-\alpha}\left\|L_{\tilde{g}_{k}}\left(s_{k}\right)\right\|_{C_{\alpha}^{0}}
\end{aligned}$$
Both the $L^{2}$ and Hölder norms here are taken with respect to the metric $g_{k}$.
Proof. $L_{\tilde{g}_{k}}\left(s_{k}\right)$ is supported in $S_{k}$, so
$$\left\|L_{\tilde{g}_{k}}\left(s_{k}\right)\right\|_{L^{2}} \lesssim \operatorname{vol}\left(S_{k}\right)^{\frac{1}{2}}\left\|L_{\tilde{g}_{k}}\left(s_{k}\right)\right\|_{C^{0}}$$
But, by definition of $S_{k}$, at all points of $S_{k}$ the weight function $w$ satisfies $w \gtrsim U_{k}$ from which we have $\left\|L_{\tilde{g}_{k}}\left(s_{k}\right)\right\|_{C^{0}} \lesssim U_{k}^{-\alpha}\left\|L_{\tilde{g}_{k}}\left(s_{k}\right)\right\|_{C_{\alpha}^{0}}$. We have $\operatorname{vol}\left(S_{k}\right) \lesssim U_{k}^{3} \operatorname{vol}\left(\Sigma_{k}\right)$. Now (5.3) implies (5.4).

From here, Proposition 4.3 gives $\left\|s_{k}\right\|_{L^{2}} \lesssim\left\|L_{\tilde{g}_{k}}\left(s_{k}\right)\right\|_{L^{2}}$. Proposition 4.3 gives this with the $L^{2}$-norms defined by $\tilde{g}_{k}$ but by (5.1) these norms are equivalent to those defined by $g_{k}$. By (5.4) this proves (5.5) for $\left\|s_{k}\right\|_{L^{2}}$.

We now use (4.8), which gives
$$\int_{X_{k}}\left|\nabla s_{k}\right|_{\tilde{g}_{k}}^{2} \mathrm{dvol}_{\tilde{g}_{k}} \lesssim \int_{X_{k}}\left\langle L_{\tilde{g}_{k}}\left(s_{k}\right), s_{k}\right\rangle_{\tilde{g}_{k}}+\int_{X_{k}}\left|s_{k}\right| \tilde{\tilde{g}}_{k}^{2} \mathrm{~d} \operatorname{vol}_{\tilde{g}_{k}}$$
from which (5.5) follows by the previous arguments (we have used here the fact that $\operatorname{Rm}_{\tilde{g}_{k}}$ is bounded uniformly in $k$.) \(\square\)

At this point we divide the argument into three separate cases.
\begin{itemize}
\item[1.] There exists a constant $C>0$ such that, after passing to a subsequence, for all large $k$ we have
$$w\left(x_{k}\right) \geq \frac{1}{C} U_{k, \max }$$
The points $x_{k}$ are further and further from the branch locus. Moreover, since we choose the gluing distance with $U_{k} / U_{k, \text { max }} \rightarrow 0$, for large $k$ the points $x_{k}$ lie in the region of $X_{k}$ where $g_{k}$ is genuinely hyperbolic.
\item[2.] There exists a constant $C$ such that, after passing to a subsequence,
$$w\left(x_{k}\right) \leq C$$
The points $x_{k}$ remain at bounded distance from the branch locus $\Sigma_{k} \subset X_{k}$ and so lie in the region where $g_{k}$ is given by the model Einstein metric of §3.
\item[3.] The remaining possibility is that $w\left(x_{k}\right) \rightarrow \infty$ and $w\left(x_{k}\right) / U_{k, \text { max }} \rightarrow 0$. In this case the points $x_{k}$ live in a region where the model coordinate system near the branch locus makes sense, but they are moving further and further from the branch locus.
\end{itemize}
We will treat each of these cases separately, but each time the argument follows similar lines. We translate the problem onto a non-compact space (either $\mathbb{H}^{4}$ or the model metric of §3). We use a Green's representation formula in this non-compact space to give an expression for $s_{k}\left(x_{k}\right)$. We then prove estimates for the Green's operator. In cases 1 and 2 these are weighted integral estimates which enable us to turn $L^{2}$ estimates on $s_{k}$ into pointwise ones. In case 3 we can even use pointwise estimates on the Green's operator. At various steps we rely on facts about Green's operators which are essentially standard, but for which we were unable to find a clean reference which applies in the exact situations considered here. Accordingly, we have relegated proofs of these technical results to Appendix A.

In order to fix our notation and conventions, we quickly recall the general form of the representation formula for systems which are not necessarily self adjoint. Suppose $D$ is an elliptic operator on sections of a vector bundle $E$ with a fibrewise metric, over a Riemannian manifold. Let $G(y, x) \in \operatorname{Hom}\left(E_{x}, E_{y}\right)$ be defined for all $x, y \in X$ with $x \neq y$, depending smoothly on $x$ and $y$. We say that $G$ is a fundamental solution for $D$ if it satisfies the following distributional equation: let $\sigma \in E_{x}$ and write $G(\cdot, x)(\sigma)$ for the section $y \mapsto G(y, x)(\sigma)$ of $E$; then
$$D(G(\cdot, x)(\sigma))=\delta_{x} \sigma$$

Explicitly, for any compactly supported section $s$ of $E$,
$$\int_{X}\left\langle G(y, x)(\sigma), D^{*} s(y)\right\rangle \mathrm{dvol}_{y}=\langle s(x), \sigma\rangle$$
This is equivalent to the following representation formula: for any compactly supported section $s$ of $E$,
$$s(x)=\int_{X} G(y, x)^{t}\left(D^{*} s(y)\right) \mathrm{dvol}_{y}$$
Notice in particular that a fundamental solution for $D$ gives a representation formula for $s$ in terms of $D^{*} s$.

\subsection*{5.1 Case 1}

We assume that, after passing to a subsequence, $w\left(x_{k}\right) \gtrsim U_{k, \text { max }}$ and so $x_{k}$ lives in the region of $X_{k}$ where $g_{k}$ is hyperbolic. We write $h_{k}$ for the (hyperbolic) metric on $X_{k}$ given by pulling back the hyperbolic metric via the branched cover $p: X_{k} \rightarrow M_{k}$. On $X_{k} \backslash \Sigma_{k}$ this metric is smooth, but incomplete. We will find a large embedded hyperbolic ball in $\left(X_{k}, h_{k}\right)$ centred at $x_{k}$ which we will then use to transfer everything over to hyperbolic space. The next two lemmas show that a suitably large ball can be found.

Lemma 5.2. There exists $C>0$ such that for all large $k, d_{h_{k}}\left(x_{k}, \Sigma_{k}\right) \geq \log \left(U_{k, \max }\right)-C$.
Proof. If $w\left(x_{k}\right) \geq \frac{1}{2} U_{k, \text { max }}$ then, by definition of $w$ (in Lemma 4.6),
$$d_{h_{k}}\left(x_{k}, \Sigma_{k}\right) \geq \cosh ^{-1}\left(\frac{1}{2} U_{k, \max }\right)$$
Now for all $\xi \geq 1, \cosh ^{-1}(\xi) \geq \log (\xi)$ from which the lemma follows.
If $w\left(x_{k}\right)<\frac{1}{2} U_{k, \text { max }}$ then $x_{k}$ is in the region where the hyperbolic coordinate system (3.1) makes sense and $w=u$. The hyperbolic distance from $\Sigma_{k}$ is then given by
$$d_{h_{k}}\left(x_{k}, \Sigma_{k}\right)=\cosh ^{-1}\left(w\left(x_{k}\right)\right)$$
and the stated lower bound follows from the fact that $w\left(x_{k}\right) \gtrsim U_{k, \text { max }}$. \(\square\)

Lemma 5.3. There exists $C>0$ such that for all large $k, i_{h_{k}}\left(x_{k}\right) \geq \log \left(U_{k, \max }\right)-C$, where $i_{h_{k}}\left(x_{k}\right)$ denotes the injectivity radius of $h_{k}$ at $x_{k}$.

Proof. One possibility is that $i_{h_{k}}\left(x_{k}\right)=d_{h_{k}}\left(x_{k}, \Sigma_{k}\right)$; the exponential map of $h_{k}$ ceases to be an embedding because the geodesics reach the branch locus. In this case the result follows from the previous lemma. If $i_{h_{k}}\left(x_{k}\right)<d_{h_{k}}\left(x_{k}, \Sigma_{k}\right)$ then there is a geodesic loop $\gamma$, based at $x_{k}$ lying in $X_{k} \backslash \Sigma_{k}$ and of length $l(\gamma)=2 i_{h_{k}}\left(x_{k}\right)$. (Conjugate points cannot occur since $h_{k}$ is negatively curved.) Now the projection $p: X_{k} \rightarrow M_{k}$ is an isometric covering map; it follows that $p \circ \gamma$ is again a geodesic loop, and the lengths satisfy $l(\gamma) \geq l(p \circ \gamma)$. Since $p \circ \gamma$ is non-constant, we have $l(p \circ \gamma) \geq 2 i\left(M_{k}\right)$ and so $i_{h_{k}}\left(x_{k}\right) \geq i\left(M_{k}\right)$. Since $U_{k, \text { max }}=\cosh \left(\frac{1}{2} i\left(M_{k}\right)\right)$, this implies that $i_{h_{k}}\left(x_{k}\right) \geq 2 \log \left(U_{k, \text { max }}\right)$ which is even stronger than the stated lower bound. \(\square\)

Now let $0<\epsilon_{0}<1$ be some small number, to be chosen later. We set
$$R_{k}=\left(1-\epsilon_{0}\right) \log \left(U_{k, \max }\right)$$
By Lemma 5.3, for $k$ sufficiently large, $R_{k}<i_{h_{k}}\left(x_{k}\right)$ and so the geodesic ball $B_{h_{k}}\left(x_{k}, R_{k}\right)$ is embedded in $X_{k}$. Let $\chi_{k}: \mathbb{R}_{+} \rightarrow[0,1]$ be a sequence of cut-off functions with $\chi_{k}(r)=1$ for $0 \leq r \leq R_{k}-1, \chi_{k}(r)=0$ for $r \geq R_{k}$ and with $\left|\chi_{k}^{\prime}\right|+\left|\chi_{k}^{\prime \prime}\right| \lesssim 1$. Write
$$\tilde{s}_{k}=\chi_{k}\left(d_{h_{k}}\left(y, x_{k}\right)\right) s_{k}$$
The cut-off tensor $\tilde{s}_{k}$ is supported in $B_{h_{k}}\left(x_{k}, R_{k}\right)$. We fix an isometric identification of this ball with a standard hyperbolic ball $B_{h}\left(p, R_{k}\right) \subset\left(\mathbb{H}^{4}, h\right)$. (Here, $h$ denotes the hyperbolic metric on $\mathbb{H}^{4}$.) We think of $\tilde{s}_{k}$ as a compactly supported tensor on $B_{h}\left(p, R_{k}\right)$ and thus, extending by zero, as a tensor on the whole of $\mathbb{H}^{4}$.

We next turn to the metrics $\tilde{g}_{k}$ of (5.1). We will show that over the ball $B_{h_{k}}\left(x_{k}, R_{k}\right)$ they are arbitrarily close to the hyperbolic metric $h_{k}$. By Lemma 5.2, the geodesic ball $B_{h_{k}}\left(x_{k}, R_{k}\right)$ is contained in the region $\left\{w \geq C U_{k, \max }^{\epsilon_{0}}\right\}$ for some constant $C$ (independent of $k$ ). Now it follows from the definition (3.10) of $g_{k}$ that
$$\left\|g_{k}-h_{k}\right\|_{C^{m+2, \eta}\left(\left\{w \geq C U_{k, \max }^{\epsilon_{0}}\right\}\right)} \lesssim U_{k, \max }^{-3 \epsilon_{0}}$$
Together with (5.1) this gives
$$\left\|\tilde{g}_{k}-h_{k}\right\|_{C^{m+2, \eta}\left(B_{h_{k}}\left(x_{k}, R_{k}\right)\right)} \rightarrow 0$$

Just as for $\tilde{s}_{k}$, we will consider $\tilde{g}_{k}$ as a metric on $B_{h}\left(p, R_{k}\right) \subset \mathbb{H}^{4}$. We then extend it to a new metric, still denoted $\tilde{g}_{k}$, on the whole of $\mathbb{H}^{4}$, which coincides with the original in $B_{h}\left(p, R_{k}\right)$, with the hyperbolic metric $h$ outside of $B\left(p, 2 R_{k}\right)$ and which interpolates between these two metrics in the intermediate region. By (5.8) we can do this in such a way that, globally,
$$\left\|\tilde{g}_{k}-h\right\|_{C^{m+2, \eta}\left(\mathbb{H}^{4}\right)} \rightarrow 0$$
In an identical fashion we extend the original metrics $g_{k}$ from the ball $B_{h_{k}}\left(x_{k}, R_{k}\right) \cong$ $B_{h}\left(p, R_{k}\right)$ to the whole of $\mathbb{H}^{4}$. We continue to denote this extension by $g_{k}$.

Since $\tilde{s}_{k}$ is compactly supported on $\mathbb{H}^{4}$, it has a Green's representation (see Appendix A). Write $\tilde{H}_{k}(\cdot, p)$ for the fundamental solution of $L_{\tilde{g}_{k}}^{*}$, over $\mathbb{H}^{4}$, centred at $p$. (Recall the discussion leading up to (5.6) which explains our conventions.) Note that by $L_{\tilde{g}_{k}}$ here we mean the linearised Einstein operator in Bianchi gauge relative to the extension of the metric $g_{k}$ to the whole of $\mathbb{H}^{4}$. Of course, over $B\left(p, R_{k}\right)$ this is the same as the linearised operator back on $X_{k}$, in Bianchi gauge relative to $g_{k}$, hence we do not distinguish between them in the notation. The representation formula reads:
$$s_{k}\left(x_{k}\right)=\tilde{s}_{k}(p)=\int_{B_{h}\left(p, R_{k}\right)} \tilde{H}_{k}(q, p)^{t}\left(L_{\tilde{g}_{k}}\left(\tilde{s}_{k}\right)(q)\right) \operatorname{dvol}_{\tilde{g}_{k}}(q)$$
At points of $B_{h}\left(p, R_{k}\right)$ we have
$$\left|L_{\tilde{g}_{k}}\left(\tilde{s}_{k}\right)\right| \lesssim\left|\chi_{k}\right|\left|L_{\tilde{g}_{k}}\left(s_{k}\right)\right|+\left|\chi_{k}^{\prime}\right|\left|\nabla s_{k}\right|+\left|\chi_{k}^{\prime \prime}\right|\left|s_{k}\right|$$

The function $\chi_{k}$ is supported in $B_{h}\left(p, R_{k}\right)$ and $\chi_{k}^{\prime}$ and $\chi_{k}^{\prime \prime}$ are supported in $R_{k}-1 \leq$ $d_{h}(p, \cdot) \leq R_{k}$. So from (5.10) we have that
$$\begin{aligned}
\left|s_{k}\left(x_{k}\right)\right|_{g_{k}} \lesssim & \left(\int_{B_{h}\left(p, R_{k}\right)}\left|\tilde{H}_{k}(q, p)\right|_{\tilde{g}_{k}} \operatorname{dvol}_{\tilde{g}_{k}}(q)\right)\left\|L_{\tilde{g}_{k}}\left(s_{k}\right)\right\|_{C^{0}} \\
& \quad+\left(\int_{R_{k}-1 \leq d_{h}(p, q) \leq R_{k}}\left|\tilde{H}_{k}(q, p)\right|_{\tilde{g}_{k}}^{2} \operatorname{dvol}_{\tilde{g}_{k}}(q)\right)^{1 / 2}\left(\left\|s_{k}\right\|_{L^{2}}+\left\|\nabla s_{k}\right\|_{L^{2}}\right)
\end{aligned}$$
To write this, in some places we used norms defined by the metric $g_{k}$ whilst in others we prefered $\tilde{g}_{k}$. This is allowed because they are equivalent uniformly in $k$ by assumption (5.1). Taking into account Lemma 5.1 we have
$$\begin{aligned}
\left|s_{k}\left(x_{k}\right)\right|_{g_{k}} & \lesssim\left(\int_{B_{h}\left(p, R_{k}\right)}\left|\tilde{H}_{k}(q, p)\right|_{\tilde{g}_{k}} \operatorname{dvol}_{\tilde{g}_{k}}(q)\right)\left\|L_{\tilde{g}_{k}}\left(s_{k}\right)\right\|_{C^{0}} \\
+ & \left(\int_{R_{k}-1 \leq d_{h}(p, q) \leq R_{k}}\left|\tilde{H}_{k}(q, p)\right|_{\tilde{g}_{k}}^{2} \mathrm{~d} \operatorname{vol}_{\tilde{g}_{k}}(q)\right)^{1 / 2} U_{k, \max }^{\frac{5}{2}} U_{k}^{\frac{3}{2}-\alpha}\left\|L_{\tilde{g}_{k}}\left(s_{k}\right)\right\|_{C_{\alpha}^{0}}
\end{aligned}$$

We will estimate the right-hand side of (5.11) using a weighted $L^{2}$ estimate on $\tilde{H}_{k}$. We start with an optimal $L^{2}$-coercivity estimate for $L_{\tilde{g}_{k}}$. Since $\tilde{g}_{k} \rightarrow h$ in $C^{2}$, a combination of the arguments in the proof of Lemma 4.4 and in Delay [15] and Lee [31] (see for instance (4.3) of [15]) show that for all sufficiently large $k$ and for any symmetric bilinear form $s \in W^{2,2}\left(\mathbb{H}^{4}, \tilde{g}_{k}\right)$,
$$\int_{\mathbb{H}^{4}}\left\langle L_{\tilde{g}_{k}}(s), s\right\rangle \operatorname{dvol}_{\tilde{g}_{k}} \geq\left(\frac{9}{8}-\delta\right) \int_{\mathbb{H}^{4}}|s|_{\tilde{g}_{k}}^{2} \operatorname{dvol}_{\tilde{g}_{k}}$$
holds. (In the special case of hyperbolic space itself one can take $\delta=0$; see Proposition 4.1 of [15]).

We now give a technical Lemma which describes the effect of pulling a weight through $L_{\tilde{g}_{k}}$.

Lemma 5.4. Pick $\epsilon>0$. Let $\rho$ be a nowhere vanishing function in $C^{2}\left(\mathbb{H}^{4}, \tilde{g}_{k}\right)$ and $s$ be a symmetric bilinear form in $W^{2,2}\left(\mathbb{H}^{4}, \tilde{g}_{k}\right)$. For all sufficiently large $k$ (depending on $\epsilon$ ), and any $\beta>0$,
$$\begin{aligned}
\int_{\mathbb{H}^{4}}\left\langle L_{\tilde{g}_{k}}\left(\rho^{\beta} s\right), \rho^{\beta} s\right\rangle \operatorname{dvol}_{\tilde{g}_{k}} & \leq(1+\epsilon) \int_{\mathbb{H}^{4}} \rho^{2 \beta}\left\langle L_{\tilde{g}_{k}}^{*}(s), s\right\rangle \operatorname{dvol}_{\tilde{g}_{k}} \\
& \quad+\left(\frac{1}{2}+\epsilon\right) \beta^{2} \int_{\mathbb{H}^{4}} \rho^{2 \beta}\left|\frac{\mathrm{~d} \rho}{\rho}\right|_{\tilde{g}_{k}}^{2}|s|_{\tilde{g}_{k}}^{2} \operatorname{dvol}_{\tilde{g}_{k}}+\epsilon \int_{\mathbb{H}^{4}} \rho^{2 \beta}|s| \tilde{\tilde{g}}_{k}^{2} \operatorname{dvol}_{\tilde{g}_{k}}
\end{aligned}$$
Proof. Let $\sigma \in W^{2,2}\left(\mathbb{H}^{4}, \tilde{g}_{k}\right)$. Recall the formula (4.5) for the linearised Einstein operator in Bianchi gauge, which we write as:
$$L_{\tilde{g}_{k}}(\sigma)=\frac{1}{2} \nabla^{*} \nabla \sigma+\operatorname{div}_{\tilde{g}_{k}}^{*}\left(D_{k}(\sigma)\right)+B_{g_{k}}\left(\tilde{g}_{k}\right) * \nabla(\sigma)+Z_{k}(\sigma)$$
where
$$D_{k}(\sigma)=\left(\operatorname{div}_{g_{k}}-\operatorname{div}_{\tilde{g}_{k}}\right)(\sigma)+\frac{1}{2} \mathrm{~d}\left(\operatorname{Tr}_{g_{k}} \sigma-\operatorname{Tr}_{\tilde{g}_{k}} \sigma\right)$$
and $Z_{k}$ is zeroth order. Integrating by parts we have, for any $\sigma \in W^{2,2}\left(\mathbb{H}^{4}, \tilde{g}_{k}\right)$,
$$\begin{aligned}
\int_{\mathbb{H}^{4}}\left\langle L_{\tilde{g}_{k}}(\sigma), \sigma\right\rangle \operatorname{dvol}_{\tilde{g}_{k}}=\frac{1}{2} \int_{\mathbb{H}^{4}} & \left\langle\nabla^{*} \nabla \sigma, \sigma\right\rangle \operatorname{dvol}_{\tilde{g}_{k}}+\int_{\mathbb{H}^{4}}\left\langle Z_{k}(\sigma), \sigma\right\rangle \operatorname{dvol}_{\tilde{g}_{k}} \\
& +\int_{\mathbb{H}^{4}}\left(\left\langle D_{k}(\sigma), \operatorname{div}_{\tilde{g}_{k}}(\sigma)\right\rangle+\left\langle B_{g_{k}}\left(\tilde{g}_{k}\right) * \nabla \sigma, \sigma\right\rangle\right) \operatorname{dvol}_{\tilde{g}_{k}}
\end{aligned}$$
Since $\left\|\tilde{g}_{k}-g_{k}\right\|_{C^{2}}=o(1)$, the terms involving $D_{k}$ and $B_{g_{k}}\left(\tilde{g}_{k}\right)$ can be bounded by arbitrarily small amounts of the $W^{1,2}$-norm of $\sigma$. (This is identical to the argument used to derive (4.11), (4.12) and (4.13).) Choosing $\sigma=\rho^{\beta} s$ and integrating by parts (as in the arguments leading up to (7.14) in Lee [31]) shows that:
$$\begin{aligned}
& \int_{\mathbb{H}^{4}}\left\langle L_{\tilde{g}_{k}}\left(\rho^{\beta} s\right), \rho^{\beta} s\right\rangle \operatorname{dvol}_{\tilde{g}_{k}} \leq \\
& \quad\left(\frac{1}{2}+\epsilon\right) \int_{\mathbb{H}^{4}} \rho^{2 \beta}\left\langle\nabla^{*} \nabla s, s\right\rangle \operatorname{dvol}_{\tilde{g}_{k}}+\int_{\mathbb{H}^{4}} \rho^{2 \beta}\left\langle Z_{k} s, s\right\rangle \operatorname{dvol}_{\tilde{g}_{k}} \\
& \quad+\left(\frac{1}{2}+\epsilon\right) \beta^{2} \int_{\mathbb{H}^{4}} \rho^{2 \beta}\left|\frac{\mathrm{~d} \rho}{\rho}\right|_{\tilde{g}_{k}}^{2}|s|_{\tilde{g}_{k}}^{2} \operatorname{dvol}_{\tilde{g}_{k}}+\epsilon \int_{\mathbb{H}^{4}} \rho^{2 \beta}|s|_{\tilde{g}_{k}}^{2} \operatorname{dvol}_{\tilde{g}_{k}}
\end{aligned}$$

We will bound the first two terms on the right-hand side. From (5.13) applied to $\sigma=\rho^{2 \beta} s$ and integrated against $s$ we have, since $\tilde{g}_{k} \rightarrow h$ in $C^{2}$
$$\begin{aligned}
& \frac{1}{2} \int_{\mathbb{H}^{4}} \rho^{2 \beta}\left\langle\nabla^{*} \nabla s, s\right\rangle \operatorname{dvol}_{\tilde{g}_{k}}+\int_{\mathbb{H}^{4}} \rho^{2 \beta}\left\langle Z_{k} s, s\right\rangle \operatorname{dvol}_{\tilde{g}_{k}} \leq \\
& \quad \int_{\mathbb{H}^{4}} \rho^{2 \beta}\left\langle L_{\tilde{g}_{k}}^{*}(s), s\right\rangle \operatorname{dvol}_{\tilde{g}_{k}}+\epsilon \int_{\mathbb{H}^{4}} \rho^{2 \beta}\left(|\nabla s|_{\tilde{g}_{k}}^{2}+|s|_{\tilde{g}_{k}}^{2}+\beta^{2}\left|\frac{\mathrm{~d} \rho}{\rho}\right|_{\tilde{g}_{k}}^{2}|s|_{\tilde{g}_{k}}^{2}\right) \operatorname{dvol}_{\tilde{g}_{k}}
\end{aligned}$$
Now, integrating by parts
$$\int_{\mathbb{H}^{4}} \operatorname{div}\left(\rho^{2 \beta} \nabla\left(|s|_{\tilde{g}_{k}}^{2}\right)\right) \mathrm{d} \operatorname{vol}_{\tilde{g}_{k}}=0$$
we deduce that
$$\int_{\mathbb{H}^{4}} \rho^{2 \beta}|\nabla s|_{\tilde{g}_{k}}^{2} \operatorname{dvol}_{\tilde{g}_{k}} \leq 2 \int_{\mathbb{H}^{4}} \rho^{2 \beta}\left\langle\nabla^{*} \nabla s, s\right\rangle \operatorname{dvol}_{\tilde{g}_{k}}+4 \beta^{2} \int_{\mathbb{H}^{4}} \rho^{2 \beta}\left|\frac{\mathrm{~d} \rho}{\rho}\right|_{\tilde{g}_{k}}^{2}|s|_{\tilde{g}_{k}}^{2} \operatorname{dvol}_{\tilde{g}_{k}}$$
and so (5.15) implies that
$$\begin{aligned}
\left(\frac{1}{2}-2 \epsilon\right) & \int_{\mathbb{H}^{4}} \rho^{2 \beta}\left\langle\nabla^{*} \nabla s, s\right\rangle \operatorname{dvol}_{\tilde{g}_{k}}+\int_{\mathbb{H}^{4}} \rho^{2 \beta}\left\langle Z_{k}(s), s\right\rangle \operatorname{dvol}_{\tilde{g}_{k}} \leq \\
& \int_{\mathbb{H}^{4}} \rho^{2 \beta}\left\langle L_{\tilde{g}_{k}}^{*}(s), s\right\rangle \operatorname{dvol}_{\tilde{g}_{k}}+\epsilon \int_{\mathbb{H}^{4}} \rho^{2 \beta}\left(|s|_{\tilde{g}_{k}}^{2}+5 \beta^{2}\left|\frac{\mathrm{~d} \rho}{\rho}\right|_{\tilde{g}_{k}}^{2}|s|_{\tilde{g}_{k}}^{2}\right) \operatorname{dvol}_{\tilde{g}_{k}}
\end{aligned}$$

Together with (5.14) we conclude that
$$\begin{aligned}
& \int_{\mathbb{H}^{4}}\left\langle L_{\tilde{g}_{k}}\left(\rho^{\beta} s\right), \rho^{\beta} s\right\rangle \operatorname{dvol}_{\tilde{g}_{k}} \leq \\
& \int_{\mathbb{H}^{4}} \rho^{2 \beta}\left\langle L_{\tilde{g}_{k}}^{*}(s), s\right\rangle \operatorname{dvol}_{\tilde{g}_{k}}+\left(\frac{1}{2}+5 \epsilon\right) \beta^{2} \int_{\mathbb{H}^{4}} \rho^{2 \beta}\left|\frac{\mathrm{~d} \rho}{\rho}\right|_{\tilde{g}_{k}}^{2}|s|_{\tilde{g}_{k}}^{2} \operatorname{dvol}_{\tilde{g}_{k}}+2 \epsilon \int_{\mathbb{H}^{4}} \rho^{2 \beta}|s|_{\tilde{g}_{k}}^{2} \operatorname{dvol}_{\tilde{g}_{k}} \\
&+3 \epsilon \int_{\mathbb{H}^{4}} \rho^{2 \beta}\left\langle\nabla^{*} \nabla s, s\right\rangle \operatorname{dvol}_{\tilde{g}_{k}}
\end{aligned}$$
The last term in (5.17) is controlled using (5.16) and the fact that $Z_{k}$ is bounded uniformly in $k$, and this proves the result (after choosing a different $\epsilon$ ). \(\square\)

We now reach the technical crux: the weighted $L^{2}$ estimate for $\tilde{H}_{k}$. The following result can be interpreted as saying that $\tilde{H}_{k}$ has the same decay at infinity as the Green's operator for hyperbolic space.

Proposition 5.5. Given $0<\epsilon<3$, there exists a constant $C$ (depending only on $\epsilon$, but not on $k$ ) such that
$$\int_{\mathbb{H}^{4} \backslash B_{\tilde{g}_{k}}(p, 1)} e^{(3-\epsilon) d_{\tilde{g}_{k}}(p, q)}\left|\tilde{H}_{k}(q, p)\right|_{\tilde{g}_{k}}^{2} \operatorname{dvol}_{\tilde{g}_{k}}(q) \leq C$$
Proof. Let $\sigma \in S^{2} T_{p}^{*} \mathbb{H}^{4}$ with $|\sigma|=1$, and define
$$F(q)=\tilde{H}_{k}(q, p)(\sigma)$$
$F$ is the fundamental solution with $L_{\tilde{g}_{k}}^{*} F=\delta_{p} \cdot \sigma$ (in the distributional sense). Since $\sigma$ is arbitrary, it suffices to prove the stated inequality with $\left|\tilde{H}_{k}(q, p)\right|_{\tilde{g}_{k}}^{2}$ replaced by $|F(q)|_{\tilde{g}_{k}}^{2}$.

Let $\psi:[0, \infty) \rightarrow \mathbb{R}$ be a smooth bump function with $\psi \equiv 0$ on $[0,1 / 2]$ and $\psi \equiv 1$ on $[1, \infty)$. Let $\Psi_{k}(q)=\psi\left(d_{\tilde{g}_{k}}(p, q)\right)$ and $\tilde{F}=\Psi_{k} F$. Then $\tilde{F}$ is smooth on all of $\mathbb{H}^{4}$.

Next, pick $M>0$ and let $\chi:[0, \infty) \rightarrow \mathbb{R}$ be a smooth function with $\chi \equiv 2$ in [0,1], $\chi(r)=r$ for $r \in[3, M]$ and $\chi \equiv M+1$ in $[M+2, \infty)$. We choose $\chi$ so that $\left|\chi^{\prime}(r)\right| \leq 1$ for all $r$. We now let
$$\rho(q)=e^{\chi\left(d_{\tilde{g}_{k}}(p, q)\right)}$$
This function is $C^{2}$ globally and so can be used in Lemma 5.4.
Let $\delta>0$ be small and choose $0<\beta<3 / 2$. By (5.12) and Lemma 5.4, we have that for all sufficiently large $k$,
$$\begin{aligned}
\left(\frac{9}{8}-\delta\right) \int_{\mathbb{H}^{4}} \rho^{2 \beta}|\tilde{F}|_{\tilde{g}_{k}}^{2} \mathrm{dvol}_{\tilde{g}_{k}} \leq(1+\delta) & \int_{\mathbb{H}^{4}} \rho^{2 \beta}\left\langle L_{\tilde{g}_{k}}^{*}(\tilde{F}), \tilde{F}\right\rangle \mathrm{d} \operatorname{vol}_{\tilde{g}_{k}} \\
& +\left(\frac{1}{2}+\delta\right) \beta^{2} \int_{\mathbb{H}^{4}} \rho^{2 \beta}\left|\frac{\mathrm{~d} \rho}{\rho}\right|_{\tilde{g}_{k}}^{2}|\tilde{F}|_{\tilde{g}_{k}}^{2} \mathrm{~d} \operatorname{vol}_{\tilde{g}_{k}} \\
& \quad+\delta \int_{\mathbb{H}^{4}} \rho^{2 \beta}|\tilde{F}|_{\tilde{g}_{k}}^{2} \mathrm{~d} \operatorname{vol}_{\tilde{g}_{k}}
\end{aligned}$$

Since $F$ is a fundamental solution, $L_{\tilde{g}_{k}}^{*} \tilde{F}=L_{\tilde{g}_{k}}^{*}\left(\Psi_{k} F\right)$ is supported in the annulus $A=B_{\tilde{g}_{k}}(p, 1) \backslash B_{\tilde{g}_{k}}(p, 1 / 2)$. So in the first term on the right-hand side of (5.18), the
integrand is supported inside $A$. Moreover, since $\tilde{g}_{k}$ has uniformly bounded geometry, $\tilde{H}_{k}(q, p)$ is uniformly bounded in $C^{2}$ over $A$ (see the remark following Proposition A. 1 in the Appendix). Also, since $\tilde{g}_{k} \rightarrow h$ in $C^{m+2, \eta}$, the functions $\Psi_{k}$ are also uniformly bounded in $C^{2}$. It follows that there is a constant $C$, independent of $k$, such that
$$\int_{\mathbb{H}^{4}} \rho^{2 \beta}\left\langle L_{\tilde{g}_{k}}^{*}(\tilde{F}), \tilde{F}\right\rangle \operatorname{dvol}_{\tilde{g}_{k}} \leq C$$

Now, since we were careful to select $\left|\chi^{\prime}(r)\right| \leq 1$, we have $|\mathrm{d} \rho| \leq \rho$. Using this, and rearranging (5.18) we obtain
$$\left(\frac{9}{8}-\frac{1}{2} \beta^{2}-\delta \beta^{2}-2 \delta\right) \int_{\mathbb{H}^{4}} \rho^{2 \beta}|\tilde{F}|_{\tilde{g}_{k}}^{2} \mathrm{dvol}_{\tilde{g}_{k}} \leq C$$
Since $0<\beta<3 / 2$, we can find $\delta>0$ such that the coefficient on the left-hand side here is positive. Given $\epsilon>0$, we let $\beta=(3-\epsilon) / 2$. Taking $M \rightarrow \infty$ completes the proof since $\tilde{F}=F$ at points of $\mathbb{H}^{4} \backslash B_{\tilde{g}_{k}}(p, 1)$. \(\square\)

We now convert this weighted estimate into unweighted integral estimates on $\tilde{H}_{k}$.
Lemma 5.6. Let $0<\epsilon<3$ and $0<\epsilon_{0}<1$ and let $R_{k}=\left(1-\epsilon_{0}\right) \log \left(U_{k, \max }\right)$ as in (5.7). Then
$$\begin{aligned}
\int_{R_{k}-1 \leq d_{h}(p, q) \leq R_{k}}\left|\tilde{H}_{k}(q, p)\right|_{\tilde{g}_{k}}^{2} \operatorname{dvol}_{\tilde{g}_{k}}(q) & \lesssim U_{k, \max }^{(\epsilon-3)\left(1-\epsilon_{0}\right)} \\
\int_{B_{h}\left(p, R_{k}\right)}\left|\tilde{H}_{k}(q, p)\right|_{\tilde{g}_{k}} \operatorname{dvol}_{\tilde{g}_{k}}(q) & \lesssim U_{k, \max }^{\epsilon\left(1-\epsilon_{0}\right)}
\end{aligned}$$
Proof. To prove (5.19), note that since $\tilde{g}_{k} \rightarrow h$, if $q$ has $d_{h}(p, q) \leq R_{k}$ then for all sufficiently large $k, d_{\tilde{g}_{k}}(p, q) \leq R_{k}+1$. It follows that
$$\begin{aligned}
\int_{R_{k}-1 \leq d_{h}(p, q) \leq R_{k}}\left|\tilde{H}_{k}(q, p)\right|_{\tilde{g}_{k}}^{2} \mathrm{~d} \operatorname{vol}_{\tilde{g}_{k}}(q) & \lesssim e^{(\epsilon-3) R_{k}} \int_{\mathbb{H}^{4} \backslash B_{h}(p, 1)} e^{(3-\epsilon) d_{\tilde{g}_{k}}(p, q)}\left|\tilde{H}_{k}(q, p)\right|_{\tilde{g}_{k}}^{2} \mathrm{~d} \operatorname{vol}_{\tilde{g}_{k}}(q) \\
& \lesssim U_{k, \max }^{(\epsilon-3)\left(1-\epsilon_{0}\right)}
\end{aligned}$$

To prove (5.20), we start with a fact about the Green's operator, proved in the Appendix as Proposition A.1, that $\tilde{H}_{k}(q, p)$ is uniformly integrable on $B_{h}(p, 1)$. So we have
$$\begin{aligned}
\int_{B_{h}\left(p, R_{k}\right)}|\tilde{H}(q, p)|_{\tilde{g}_{k}} \operatorname{dvol}_{\tilde{g}_{k}} & \leq C+\int_{B_{h}\left(p, R_{k}\right) \backslash B_{\tilde{g}_{k}}(p, 1)}\left|\tilde{H}_{k}(q, p)\right|_{\tilde{g}_{k}} \operatorname{dvol}_{\tilde{g}_{k}} \\
& \leq C+\left(\int_{B_{\tilde{g}_{k}}\left(p, R_{k}+1\right)} e^{(\epsilon-3) d_{\tilde{g}_{k}}(p, q)} \operatorname{dvol}_{\tilde{g}_{k}(q)}\right)^{1 / 2}
\end{aligned}$$
In the second line, we have used Cauchy-Schwarz and the weighted $L^{2}$-estimate of Proposition 5.5. We have also replaced $B_{h}\left(p, R_{k}\right)$ with the larger ball $B_{\tilde{g}_{k}}\left(p, R_{k}+1\right)$. This second ball genuinely is larger, since $\tilde{g}_{k} \rightarrow h$.

We estimate this last integral using geodesic normal coordinates $(r, \theta)$ for $\tilde{g}_{k}$ centred at $p$. Since $\tilde{g}_{k} \rightarrow h$ in $C^{2}$, we have the uniform lower bound $\operatorname{Ric}\left(\tilde{g}_{k}\right) \geq-(3+\epsilon)$ for all
large $k$. By Bishop-Gromov comparison, $\operatorname{dvol}_{\tilde{g}_{k}} \lesssim \sinh ((3+\epsilon) r) \mathrm{d} r \wedge \mathrm{~d} \theta$. From this and the definition of $R_{k}$ it follows that
$$\int_{B_{\tilde{g}_{k}}\left(p, R_{k}\right)} e^{(\epsilon-3) d_{\tilde{g}_{k}}(p, q)} \operatorname{dvol}_{\tilde{g}_{k}}(q) \lesssim U_{k, \max }^{2 \epsilon\left(1-\epsilon_{0}\right)}$$
Taking the square root completes the proof \(\square\)

We are finally ready to prove the result which will contradict (5.2) (with $p<1 / 8$ ) showing that this case cannot actually occur after all.

Proposition 5.7. Let $0<\alpha<1 / 4$ and choose the gluing parameter $U_{k}$ so that
$$U_{k}^{-\frac{3}{2}} U_{k, \max }^{\frac{5}{4}+\alpha} \rightarrow 0$$
Then for all sufficiently large $k$,
$$\left\|s_{k}\right\|_{C_{\alpha}^{0}} \leq U_{k}^{3-\alpha-\frac{1}{8}}\left\|L_{\tilde{g}_{k}}\left(s_{k}\right)\right\|_{C_{\alpha}^{0}}$$
Proof. Recall that $x_{k}$ is the point at which $\left|w^{\alpha} s_{k}\right|_{g_{k}}=\left\|s_{k}\right\|_{C_{\alpha}^{0}}$. This (and the assumption that we are in Case 1) implies that $\left\|s_{k}\right\|_{C_{\alpha}^{0}} \leq U_{k, \text { max }}^{\alpha}\left|s_{k}\left(x_{k}\right)\right|$. Now we apply (5.11) together with Lemma 5.6: for any $0<\epsilon<3$ and any $0<\epsilon_{0}<1$,
$$\left\|s_{k}\right\|_{C_{\alpha}^{0}} \lesssim\left(U_{k, \max }^{\alpha+\epsilon\left(1-\epsilon_{0}\right)} U_{k}^{-\alpha}+U_{k, \max }^{\alpha+\frac{5}{2}+\frac{1}{2}(\epsilon-3)\left(1-\epsilon_{0}\right)} U_{k}^{\frac{3}{2}-\alpha}\right)\left\|L_{\tilde{g_{k}}}\left(s_{k}\right)\right\|_{C_{\alpha}^{0}}$$
(We have used the fact that $L_{\tilde{g}_{k}}\left(s_{k}\right)$ is supported in the region $S_{k}$ which implies that $\left.\left\|L_{\tilde{g}_{k}}\left(s_{k}\right)\right\|_{C^{0}} \lesssim U_{k}^{-\alpha}\left\|L_{\tilde{g}_{k}}\left(s_{k}\right)\right\|_{C_{\alpha}^{0}}.\right)$ We can write this coefficient as
$$U_{k}^{3-\alpha}\left(U_{k}^{-3} U_{k, \max }^{\alpha+O\left(\epsilon, \epsilon_{0}\right)}+U_{k}^{-\frac{3}{2}} U_{k, \max }^{\alpha+1+O\left(\epsilon, \epsilon_{0}\right)}\right)$$
By taking $\epsilon$ and $\epsilon_{0}$ sufficiently small and using the hypotheses on $\alpha$ and the choice of $U_{k}$, we get
$$\left\|s_{k}\right\|_{C_{\alpha}^{0}} \lesssim U_{k}^{3-\alpha} U_{k, \max }^{-\frac{1}{8}}\left(U_{k}^{-\frac{3}{2}} U_{k, \max }^{\alpha+\frac{5}{4}}\right)\left\|L_{\tilde{g}_{k}}\left(s_{k}\right)\right\|_{C_{\alpha}^{0}} \lesssim U_{k}^{3-\alpha-\frac{1}{8}}\left\|L_{\tilde{g}_{k}}\left(s_{k}\right)\right\|_{C_{\alpha}^{0}}$$ \(\square\)

\subsection*{5.2 Case 2}

We assume that, after passing to a subsequence, $w\left(x_{k}\right) \leq C$ for some constant $C$ independent of $k$. By definition of $g_{k}$, this means that the geodesic distance from $x_{k}$ to $\Sigma_{k}$ is uniformly bounded and so less than the normal injectivity radius (for all large $k$ ). We denote by $\Sigma_{k}^{\prime}$ the nearest component of $\Sigma_{k}$ to $x_{k}$. Just as in §3, we identify a tubular neighbourhood of $\Sigma_{k}^{\prime}$ with
$$\frac{\left[u_{a}, U_{k, \max }\right) \times S^{1} \times \Sigma_{k}^{\prime}}{\sim}$$
The quotient by the relation ~ denotes that we have collapsed the $S^{1}$ factor over $\left\{u_{a}\right\} \times$ $\Sigma_{k}$ to produce a smooth manifold without boundary. We use $u \in\left[u_{a}, U_{k, \text { max }}\right)$ for the
corresponding coordinate function in the radial direction, as in §3, which behaves at large distances as the exponential of the distance to $\Sigma_{k}$. Here the minimal value $u_{a}$ is the constant defined in the course of Lemma 3.3. We recall that it depends only on the degree $l$ of the cover, and not on $k$. We then transfer everything to the non-compact manifold
$$Y_{k}=\frac{\left[u_{a}, \infty\right) \times S^{1} \times \Sigma_{k}^{\prime}}{\sim}$$
The approximate Einstein metric $g_{k}$ restricts from $X_{k}$ to the region $u \leq U_{k, \text { max }}$ of $Y_{k}$; it is hyperbolic for $u \geq U_{k, \max } / 2$ and so extends directly, remaining hyperbolic, to the rest of $Y_{k}$. We continue to denote this extension by $g_{k}$. The metric $\tilde{g}_{k}$, satisfying (5.1) restricts to the region $u \leq U_{k, \max } / 2$ of $Y_{k}$; we then extend it to the whole of $Y_{k}$ by interpolating with $g_{k}$ over the region $U_{k, \text { max }} / 2 \leq u \leq U_{k, \text { max }}$. This gives a metric on the whole of $Y_{k}$ which we continue to denote by $\tilde{g}_{k}$. We remark that we still have the analogue of (5.1), namely
$$\left\|\tilde{g}_{k}-g_{k}\right\|_{C_{\alpha}^{m+2, \eta}\left(Y_{k}\right)} \rightarrow 0$$

The strategy is the same as for Case 1: we prove weighted $L^{2}$ estimates on the Green's operator which, together with the global $W^{1,2}$-estimates of Lemma 5.1 lead to a contradiction with (5.2). This time, however, we use the function $u$ as a weight. This choice is motivated by the fact that for the asymptotically hyperbolic model of §3, $u^{-1}$ is a boundary defining function, and such functions are the appropriate weight to use in that context.

For any pair $x, y$ of disjoint points of $Y_{k}$, denote by $\tilde{G}_{k}(y, x)$ the fundamental solution of $L_{\tilde{g}_{k}}^{*}$ in $Y_{k}$, centred at $x$. (See Appendix A for the construction of $\tilde{G}_{k}$.) We have the following weighted $L^{2}$ estimate on $\tilde{G}_{k}$.

Proposition 5.8. Given $0<\epsilon<3$, there exists a constant $C$ (depending only on $\epsilon$, but not on $k$ ) such that for any $x \in Y_{k}$ and for all large $k$,
$$\int_{Y_{k} \backslash B_{g_{k}}(x, 1)} u(y)^{3-\epsilon}\left|\tilde{G}_{k}(y, x)\right|_{\tilde{g}_{k}}^{2} \mathrm{dvol}_{\tilde{g}_{k}} \leq C u(x)^{3-\epsilon}$$
Proof. The proof follows the same lines as that of Proposition 5.5 with minor modifications. Accordingly we pass more quickly over the steps this time. The main difference is that the analogue of (5.12) now only holds asymptotically here. We first claim that for any $\delta>0$ there exists $U_{0}$ such that for any smooth symmetric bilinear form $s$ compactly supported in $\left\{u \geq U_{0}\right\}$ and any $k$ large enough we have
$$\int_{Y_{k}}\left\langle L_{\tilde{g}_{k}}^{*}(s), s\right\rangle \operatorname{dvol}_{\tilde{g}_{k}}=\int_{Y_{k}}\left\langle L_{\tilde{g}_{k}}(s), s\right\rangle \operatorname{dvol}_{\tilde{g}_{k}} \geq\left(\frac{9}{8}-\frac{\delta}{2}\right) \int_{Y_{k}}|s|_{\tilde{g}_{k}}^{2} \operatorname{dvol}_{\tilde{g}_{k}}$$
To prove this, note that $\left(Y_{k}, \tilde{g}_{k}\right)$ is an asymptotically hyperbolic manifold with boundary defining function $u^{-1}$ (it is even exactly hyperbolic at large distances). By definition of $g_{k}$ and by (5.22) we have in particular that for any $U_{0} \geq 1$
$$\left\|\tilde{g}_{k}-g_{h y p}\right\|_{C^{m+2, \eta}\left(\left\{u \geq U_{0}\right\}\right)} \leq C U_{0}^{-\alpha}$$
for some positive constant $C$ which is independent of $k$, where $g_{h y p}$ denotes the hyperbolic metric in the subset $\left\{u \geq U_{0}\right\} \subset Y_{k}$ given by
$$g_{h y p}=\frac{\mathrm{d} u^{2}}{u^{2}-1}+l^{2}\left(u^{2}-1\right) \mathrm{d} \theta^{2}+u^{2} h_{\Sigma_{k}^{\prime}},$$
with $h_{\Sigma_{k}^{\prime}}$ the hyperbolic metric on $\Sigma_{k}^{\prime}$. The rate of decay of $\tilde{g}_{k}$ to the hyperbolic metric therefore only depends on the radial coordinate $u$ and so is uniform in $k$. With (5.24), the proof of (5.23) now mimicks the one of (5.12) (see also Lemma 7.13 in [31]), and (5.23) holds true uniformly in $k$ provided $U_{0}$ is large enough.

Fix $\delta>0$ small and an associated $U_{0}$ as in (5.23). Let $\eta:[0, \infty) \rightarrow[0, \infty)$ be a smooth function with $\eta(u)=0$ when $u \leq U_{0}$ and $\eta(u)=1$ for $u \geq 2 U_{0}$. We will use $\eta$ to support the Green's function in the region $\left\{u \geq U_{0}\right\}$. Meanwhile we will use a second cut-off function $\chi$ to cut-off at large values of $u$, as in the proof of Proposition 5.5. For this, pick $M \gg 1$ and let $\chi:[0, \infty) \rightarrow[0, \infty)$ be smooth with $\chi(u)=U_{0}+1$ when $u \leq U_{0}, \chi(u)=u$ for $U_{0}+1 \leq u \leq M-1$ and $\chi(u)=M$ when $u \geq M+1$. We choose $\chi$ so that $\left|\chi^{\prime}\right| \leq 1$.

Let $x \in Y_{k}$ and $\sigma \in S^{2} T_{x}^{*} Y_{k}$ with $|\sigma|_{\tilde{g}_{k}}=1$ and as before, put
$$F(y)=\tilde{G}_{k}(y, x)(\sigma)$$
Let $\psi$ be a smooth cut-off function centred at $x$, with $\psi \equiv 0$ in $B_{\tilde{g}_{k}}(x, 1 / 2)$ and $\psi \equiv 1$ in $Y_{k} \backslash B_{\tilde{g}_{k}}(x, 1)$. We put
$$\tilde{F}(y)=\psi(y) \eta(u(y)) F(y)$$
$L_{\tilde{g}_{k}}^{*}(\tilde{F})$ is supported in the union of the annulus $B_{\tilde{g}_{k}}(x, 1) \backslash B_{\tilde{g}_{k}}(x, 1 / 2)$ and the region $\left\{U_{0} \leq u \leq 2 U_{0}\right\}$. Arguing as in the derivation of (5.1) we get that
$$\int_{Y_{k}} \chi(u(y))^{3-\epsilon}\left|L_{\tilde{g}_{k}}^{*} \tilde{F}(y)\right|_{\tilde{g}_{k}}^{2} \mathrm{dvol}_{\tilde{g}_{k}} \leq C u(x)^{3-\epsilon}$$
where $C$ does not depend on $\epsilon, M$ or $k$ but does depend on $U_{0}$. Two points in the proof of (5.25) are different from the previous discussion. On the one hand, to control the contribution of the integrand supported in $B_{\tilde{g}_{k}}(x, 1) \backslash B_{\tilde{g}_{k}}(x, 1 / 2)$ we must first bound uniformly the volume of the unit ball:
$$\operatorname{vol}\left(B_{\tilde{g}_{k}}(x, 1)\right) \leq C$$
This follows from the Bishop-Gromov inequality and the fact that the Ricci curvature of $\tilde{g}_{k}$ is uniformly bounded below. Then, we use that for large $k$ we have $|\mathrm{d} u|_{\widetilde{g}_{k}} \leq 2 V(u)^{1 / 2} \leq 2 u$, where $V$ is defined in (3.10). It follows that there is a constant $C$ such that for any $y \in B_{\tilde{g}_{k}}(x, 1), u(y) \leq C u(x)$.

On the other hand, the other possible support of the integrand in (5.25) is the region $\left\{U_{0} \leq u \leq 2 U_{0}\right\}$. For such $y$, we also have $u(y) \leq C u(x)$ where $C$ now depends on $U_{0}$ (this is because $u(x) \geq u_{a}>0$ ), and therefore $\chi(u(y))^{3-\epsilon} \leq C u(x)^{3-\epsilon}$. Together with the global uniform $L^{2}$ control on $\tilde{G}_{k}(y, x)$ and its covariant derivative given in Proposition A. 1 of the Appendix, this proves (5.25).

We now copy precisely the steps in the proof of Proposition 5.5 to obtain, for any $0<\beta<3 / 2$,
$$\int_{Y_{k}} \chi(u(y))^{2 \beta}|\tilde{F}(y)|_{\tilde{g}_{k}}^{2} \operatorname{dvol}_{\tilde{g}_{k}} \leq C u(x)^{2 \beta}$$
Here $C$ depends only on $\beta$ and $U_{0}$, but not on $M, k$ or $x$. Now letting $M \rightarrow \infty$ gives, by definition of $\eta$ and $\psi$ :
$$\int_{\left\{u \geq 2 U_{0}\right\} \backslash B_{\tilde{g}_{k}}(x, 1)} u(y)^{2 \beta}|F(y)|_{\tilde{g}_{k}}^{2} \operatorname{dvol}_{\tilde{g}_{k}} \leq C u(x)^{2 \beta}$$

Finally, the integral over the region $\left\{u \leq 2 U_{0}\right\} \backslash B_{\tilde{g}_{k}}(x, 1)$ is independently estimated by the global $L^{2}$ bound on $\tilde{G}_{k}(y, x)$ given in Proposition A.1. This completes the proof. \(\square\)

Note that this time, in Proposition (5.8), the weight is just a function of $u$ and is not normalized relative to $x$.

With this weighted $L^{2}$-estimate in hand, we prove the following bound on $s_{k}\left(x_{k}\right)$ which gives a contradiction with (5.2) (again with $p=1 / 8$ ). (For consistency, we choose $U_{k}$ to satisfy the same constraint (5.21). If we only cared about Case 2, we could have used a weaker constraint on $U_{k}$.)

Proposition 5.9. Let $1 / 8<\alpha<1 / 4$ and choose the gluing parameter $U_{k}$ so that
$$U_{k}^{-\frac{3}{2}} U_{k, \max }^{\frac{5}{4}+\alpha} \rightarrow 0$$
Then for all sufficiently large $k$,
$$\left\|s_{k}\right\|_{C_{\alpha}^{0}} \leq U_{k}^{3-\alpha-\frac{1}{8}}\left\|L_{\tilde{g}_{k}}\left(s_{k}\right)\right\|_{C_{\alpha}^{0}}$$
Proof. We first transport $s_{k}$ from $X_{k}$ to the model space $Y_{k}$. Let $\eta_{k}:[0, \infty) \rightarrow[0, \infty)$ be a smooth cut-off function with $\eta_{k}(u)=1$ for $u \leq U_{k, \max } / 4, \eta_{k}(u)=0$ when $u \geq U_{k, \max } / 2$ and
$$\left|\eta_{k}^{\prime}\right|+U_{k, \max }\left|\eta_{k}^{\prime \prime}\right| \lesssim \frac{1}{U_{k, \max }}$$
For such a choice of $\eta_{k}$ we have, in particular, that
$$\left|\nabla \eta_{k}(u(\cdot))\right|_{\tilde{g}_{k}}+\left|\Delta \eta_{k}(u(\cdot))\right|_{\tilde{g}_{k}} \lesssim 1$$
Let $\tilde{s}_{k}=\eta_{k} s_{k}$. This defines a symmetric tensor field supported in the region $u \leq U_{k, \text { max }}$ and we extend it by zero to a tensor on the whole of $Y_{k}$. We now take the Green's representation formula for $\tilde{s}_{k}$ :
$$s_{k}\left(x_{k}\right)=\tilde{s}_{k}\left(x_{k}\right)=\int_{Y_{k}} \tilde{G}_{k}\left(y, x_{k}\right)^{t}\left(L_{\tilde{g}_{k}}\left(\tilde{s}_{k}\right)(y)\right) \operatorname{dvol}_{\tilde{g}_{k}}(y)$$
Now $L_{\tilde{g}_{k}}\left(s_{k}\right)$ is by assumption supported in the region $S_{k}=\left\{U_{k} / 2 \leq u \leq U_{k}\right\}$, where $\eta_{k}=1$. It follows that
$$\begin{aligned}
&\left|s_{k}\left(x_{k}\right)\right|_{g_{k}} \lesssim\left(\int_{S_{k}}\left|\tilde{G}_{k}\left(y, x_{k}\right)\right|_{\tilde{g}_{k}} \operatorname{dvol}_{\tilde{g}_{k}}\right) U_{k}^{-\alpha}\left\|L_{\tilde{g}_{k}}\left(s_{k}\right)\right\|_{C_{\alpha}^{0}} \\
& \quad+\left(\int_{\frac{U_{k, \max }}{4} \leq u \leq \frac{U_{k, \max }}{2}}\left|\tilde{G}_{k}\left(y, x_{k}\right)\right|_{\tilde{g}_{k}}^{2}\right)^{1 / 2}\left(\left\|s_{k}\right\|_{L^{2}}+\left\|\nabla s_{k}\right\|_{L^{2}}\right)
\end{aligned}$$
(we used here the uniform bounds (5.26) on the derivatives of $\eta_{k}$.)
We make use of Proposition 5.8. Since we are assuming here that $u\left(x_{k}\right) \leq C$ is uniformly bounded, we can replace the bound of this result by a uniform constant, and we in particular have that $x_{k} \notin S_{k}$.

By Cauchy-Schwarz,
$$\begin{aligned}
\int_{S_{k}}\left|\tilde{G}_{k}\left(y, x_{k}\right)\right|_{\tilde{g}_{k}} \mathrm{dvol}_{\tilde{g}_{k}} & \leq\left(\int_{S_{k}} u(y)^{\epsilon-3} \mathrm{~d} \operatorname{vol}_{\tilde{g}_{k}}(y)\right)^{1 / 2}\left(\int_{S_{k}} u(y)^{3-\epsilon}\left|\tilde{G}_{k}\left(y, x_{k}\right)\right|_{\tilde{g}_{k}}^{2} \operatorname{dvol}_{\tilde{g}_{k}}(y)\right)^{1 / 2} \\
& \lesssim U_{k}^{\frac{1}{2}(\epsilon-3)} \operatorname{vol}\left(S_{k}\right)^{1 / 2}
\end{aligned}$$
Now $\operatorname{vol}\left(S_{k}\right) \leq U_{k}^{3} \operatorname{vol}\left(\Sigma_{k}\right)$ where $\operatorname{vol}\left(\Sigma_{k}\right)$ is the hyperbolic volume of the branch locus $\Sigma_{k}$. By part 3 of Proposition 1.1, we have $\operatorname{vol}\left(\Sigma_{k}\right) \lesssim U_{k, \text { max }}^{5}$ (as discussed before (5.3)) and from here we have that
$$\int_{S_{k}}\left|\tilde{G}_{k}\left(y, x_{k}\right)\right|_{\tilde{g}_{k}} \mathrm{dvol}_{\tilde{g}_{k}} \lesssim U_{k}^{\frac{\epsilon}{2}} U_{k, \max }^{\frac{5}{2}}=o\left(U_{k}^{3-\frac{1}{8}}\right)$$
(where we have used the condition on $U_{k}$ in the hypotheses, with $\epsilon>0$ chosen sufficiently small).

This deals with the first term in (5.27). For the second term we use Proposition 5.8 to write
$$\int_{\frac{U_{k, \max }}{4} \leq u \leq \frac{U_{k, \max }}{2}}\left|\tilde{G}_{k}\left(y, x_{k}\right)\right|_{\tilde{g}_{k}}^{2} \lesssim U_{k, \max }^{\epsilon-3}$$
From this and Lemma 5.1 we get that the second term in (5.27) is bounded by
$$U_{k, \max }^{\frac{\epsilon}{2}+1} U_{k}^{\frac{3}{2}-\alpha}\left\|L_{\tilde{g}_{k}}\left(s_{k}\right)\right\|_{C_{\alpha}^{0}}=\left(U_{k, \max }^{\frac{\epsilon}{2}+1} U_{k}^{-\frac{3}{2}}\right) U_{k}^{3-\alpha}\left\|L_{\tilde{g}_{k}}\left(s_{k}\right)\right\|_{C_{\alpha}^{0}}$$
When $\epsilon$ is sufficiently small, using the hypothesis on the choice of $U_{k}$ we have
$$U_{k, \max }^{\frac{\epsilon}{2}+1} U_{k}^{-\frac{3}{2}}=o\left(U_{k}^{-\frac{1}{8}}\right)$$
Together with (5.27) and (5.28), this completes the proof. \(\square\)

\subsection*{5.3 Case 3}

It remains to treat the case $w\left(x_{k}\right) \rightarrow \infty$ whilst $w\left(x_{k}\right) / U_{k, \text { max }} \rightarrow 0$. This means that $x_{k}$ lies in the intermediate region, between the model and the genuinely hyperbolic part of $X_{k}$. In particular, $w\left(x_{k}\right)=u\left(x_{k}\right)$. Here, like in Case 1, the metric is very close to hyperbolic. However, the radius on which this holds is not as large and so the same arguments do not work. Instead, we work directly.

Since $w\left(x_{k}\right) / U_{k, \text { max }} \rightarrow 0$ the point $x_{k}$ lies in a tubular neighbourhood of a component $\Sigma_{k}^{\prime}$ of the branch locus:
$$x_{k} \in \frac{\left[u_{a}, U_{k, \max }\right) \times S^{1} \times \Sigma_{k}^{\prime}}{\sim}$$
(where, as above, ~ denotes the relation collapsing $\left\{u_{a}\right\} \times S^{1}$ to form a smooth manifold without boundary). We use $(u, \theta) \in\left[u_{a}, U_{k, \text { max }}\right) \times S^{1}$ for the corresponding polar coordinates transverse to $\Sigma_{k}^{\prime}$. Recall that in these coordinates the metric $g_{k}$ is given by
$$g_{k}=\frac{\mathrm{d} u^{2}}{V(u)}+V(u) l^{2} \mathrm{~d} \theta^{2}+u^{2} h_{\Sigma_{k}^{\prime}}$$
where $l$ is the degree of the branched cover $X_{k} \rightarrow M_{k}, h_{\Sigma_{k}^{\prime}}$ denotes the hyperbolic metric on $\Sigma_{k}^{\prime}$ and where $V(u)=u^{2}-1+a \chi u^{-1}$ and $\chi$ is a cut-off function (see the discussion around (3.10)). When $u$ is large, this is close to the pull-back $h_{k}$ of the hyperbolic metric from $M_{k}$ :
$$h_{k}=\frac{\mathrm{d} u^{2}}{u^{2}-1}+l^{2}\left(u^{2}-1\right) \mathrm{d} \theta^{2}+u^{2} h_{\Sigma_{k}^{\prime}}$$
We will use the Green's operator of $h_{k}$ which, as we now explain, comes with explicit pointwise bounds.

First, we work on $\mathbb{H}^{4}$, with hyperbolic metric $h$. Given $x \in \mathbb{H}^{4}$, let $G_{h}(\cdot, x)$ denote the fundamental solution for $L_{h}$. Here, $L_{h}$ denotes the linearised Einstein operator in Bianchi gauge relative to $h$, given by (4.4). For any smooth compactly supported section $s$ of $S^{2} T^{*} \mathbb{H}^{4}$ we have
$$s(x)=\int_{\mathbb{H}^{4}} G_{h}(x, y)\left(L_{h}(s)(y)\right) \mathrm{dvol}_{h}(y)$$
Notice that here we have used the fact that, since $L_{h}$ is self-adjoint, the Green's operator has the symmetry property $G_{h}(x, y)=G(y, x)^{t}$.

Now we pass to the branched cover. Fix a totally geodesic copy of $\mathbb{H}^{2} \subset \mathbb{H}^{4}$ and write $p: \tilde{\mathbb{H}}^{4} \rightarrow \mathbb{H}^{4}$ for the $l$-fold cover, branched along $\mathbb{H}^{2}$. In polar coordinates $(u, \theta, x) \in$ $[1, \infty) \times S^{1} \times \mathbb{H}^{2}$ orthogonal to $\mathbb{H}^{2}$ (where $u=\cosh (d)$, with $d$ the distance to the copy of $\mathbb{H}^{2}$ ), the map $p$ is given by $p(u, \theta, x)=(p, l \theta, x)$. Write $\tilde{h}=p^{*} h$ for the pull-back of the hyperbolic metric. We set
$$D=(1, \infty) \times\left(-\frac{\pi}{l}, \frac{\pi}{l}\right) \times \mathbb{H}^{2}$$
The restriction of $p$ is an isometry between $(D, \tilde{h})$ and the complement in $\mathbb{H}^{4}$ of the set $\{\theta=\pi\}$. It follows that
$$G_{\tilde{h}}(x, y):=p^{*} \circ G_{h}(p(x), p(y)) \circ p_{*}$$
is a fundamental solution for $L_{\tilde{h}}$ over $D$. In other words, if $s$ is a section of $S^{2} T^{*} \tilde{\mathbb{H}}^{4}$ supported in $D$, then for any $x \in D$,
$$s(x)=\int_{D} G_{\tilde{h}}(x, y)\left(L_{\tilde{h}}(s)(y)\right) \operatorname{dvol}_{\tilde{g}}(y)$$

We will use cut-off functions to transfer $G_{\tilde{h}}$ to $X_{k}$. We will support our symmetric 2-tensors in a region of $X_{k}$, centred on $x_{k}$ and consisting of a large interval in $u$, a narrow interval in $\theta$ and a large ball in $\Sigma_{k}^{\prime}$. The idea is that the rapid decay of $G_{\tilde{h}}$ ensures that the contribution outside of this region to the representation formula will already be too small to matter.

We now turn to the details. Write $x_{k}=\left(u\left(x_{k}\right), 0, z_{k}\right) \in\left[u_{a}, U_{k, \text { max }}\right) \times S^{1} \times \Sigma_{k}^{\prime}$. Choose geodesic normal coordinates $(s, \phi)$ on $\Sigma_{k}^{\prime}$ centred at $z_{k}$, where $s$ denotes distance to $z_{k}$ in the hyperbolic metric and $\phi \in S^{1}$ is the angular coordinate. Then $(u, \theta, s, \phi)$ are a system of coordinates on $X_{k}$ with $x_{k}$ corresponding to the point $\left(u\left(x_{k}\right), 0,0, *\right)$ (the $\phi$-coordinate is not defined at $s=0$ ). Note that $\Sigma_{k} \subset M_{k}$ is totally geodesic and so the injectivity radii satisfy $i\left(\Sigma_{k}\right) \geq i\left(M_{k}\right)$. In particular, the coordinate $s$ is defined for $s \in[0, \sigma]$ for some $\sigma>2$ independent of $k$.

Let $M>0$ be large, to be chosen later. We define three cut-off functions as follows:
\begin{itemize}
\item[-] Let $\hat{\eta}_{1}: \mathbb{R} \rightarrow \mathbb{R}_{\geq 0}$ be smooth with $\hat{\eta}_{1}(v)=1$ for $v \in\left[-\log \left(u\left(x_{k}\right)\right)-M / 2, \log \left(u\left(x_{k}\right)\right)+\right.$ $M / 2]$ and with $\hat{\eta}_{1}(v)=0$ for $v \in\left[-\log \left(u\left(x_{k}\right)\right)-M, \log \left(u\left(x_{k}\right)\right)+M\right]^{c}$. We can choose $\hat{\eta}_{1}$ with
$$\left|\hat{\eta}_{1}^{\prime}\right|+\left|\hat{\eta}_{1}^{\prime \prime}\right| \leq \frac{C}{M}$$
for some positive constant $C$ independent of $M$.
We set $\eta_{1}(u, \theta, s, \phi)=\hat{\eta}_{1}(\log u)$. By (5.29), the derivatives of $\eta_{1}$ using the pulled-back hyperbolic metric $h_{k}$ satisfy
$$\left|\nabla \eta_{1}(y)\right|_{h_{k}}+\left|\nabla^{2} \eta_{1}(y)\right|_{h_{k}} \leq \frac{C^{\prime}}{M}$$
for any $y$, where $C^{\prime}$ is independent of $M$ and $k$ (and ∇ is taken for $h_{k}$ ).
\item[-] Let $\hat{\eta}_{2}:\left[-\frac{\pi}{l}, \frac{\pi}{l}\right] \rightarrow \mathbb{R}_{\geq 0}$ be smooth with $\hat{\eta}_{2}(\theta)=1$ for $\theta \in\left[-\frac{\pi}{2 l}, \frac{\pi}{2 l}\right]$ and $\hat{\eta}_{2}(\theta)=0$ for $\theta=\left[-\frac{3 \pi}{4 l}, \frac{3 \pi}{4 l}\right]^{c}$. We choose $\hat{\eta}_{2}$ so that
$$\left|\hat{\eta}_{2}^{\prime}\right|+\left|\hat{\eta}_{2}^{\prime \prime}\right| \leq C$$
We write $\eta_{2}(u, \theta, s, \phi)=\hat{\eta}_{2}(\theta)$. Again using $h_{k}$ to define derivatives, we have that for any $y$,
$$\left|\nabla \eta_{2}(y)\right|_{h_{k}}+\left|\nabla^{2} \eta_{2}(y)\right|_{h_{k}} \leq \frac{C^{\prime}}{\sqrt{u(y)^{2}-1}}$$
where $C^{\prime}$ is independent of $y, M$ and $k$ (but does depend on $l$ ).
After applying the first cut-off $\eta_{1}$, we will be left considering only those points $y$ with $e^{-M} u\left(x_{k}\right) \leq u(y) \leq e^{M} u\left(x_{k}\right)$. Now, by assumption, $u\left(x_{k}\right) \rightarrow \infty$ so taking $k$ large enough (depending on $M$ ) we can ensure that for these points $y, u(y) \geq \sqrt{M^{2}+1}$. This gives
$$\left|\nabla \eta_{2}(y)\right|_{h_{k}}+\left|\nabla^{2} \eta_{2}(y)\right|_{h_{k}} \leq \frac{C^{\prime}}{M}$$
\item[-] Let $\hat{\eta}_{3}: \mathbb{R}_{\geq 0} \rightarrow \mathbb{R}_{\geq 0}$ be smooth with $\hat{\eta}_{3}(s)=1$ for $s \in[0, \sigma-2]$ and $\hat{\eta}_{3}(s)=0$ for $s \in[\sigma-1, \infty)$. Put $\eta_{3}(u, \theta, s, \phi)=\hat{\eta}_{3}(s)$. Again we have
$$\left|\nabla \eta_{3}(y)\right|_{h_{k}}+\left|\nabla^{2} \eta_{3}(y)\right|_{h_{k}} \leq \frac{C^{\prime}}{u(y)} \leq \frac{C^{\prime}}{M}$$
for those $y$ with $e^{-M} u\left(x_{k}\right) \leq u(y) \leq e^{M} u\left(x_{k}\right)$ as long as $k$ is large enough (depending on $M$ ).
\end{itemize}

We now set $\eta: X_{k} \rightarrow \mathbb{R}_{\geq 0}$ to be $\eta=\eta_{1} \eta_{2} \eta_{3}$. Although each $\eta_{i}$ is only defined in the coordinate patch where the coordinates $(u, \theta, s, \phi)$ are valid, the product is supported in the subset of $\left[u_{a}, U_{k, \text { max }}\right) \times S^{1} \times \Sigma_{k}{ }^{\prime}$ defined by
$$A_{k}=\left\{e^{-M} u\left(x_{k}\right) \leq u \leq e^{M} u\left(x_{k}\right)\right\} \times\left\{-\frac{3 \pi}{4 l} \leq \theta \leq \frac{3 \pi}{4 l}\right\} \times\{s \leq \sigma-1\} \times S^{1}$$
and $\eta(y)$ vanishes for $y$ outside this region.